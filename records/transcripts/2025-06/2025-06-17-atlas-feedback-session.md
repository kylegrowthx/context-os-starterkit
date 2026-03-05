# Atlas Feedback Session

<metadata>
date: 2025-06-17
time: 17:01 UTC
duration: 80 minutes
organizer: jurgen@growthx.ai
participants: Jürgen Linde, Sydney Go, Jason Gong
fathom_recording_id: 68894778
fathom_url: https://fathom.video/calls/329307217
share_url: https://fathom.video/share/Nz_Awms-AoTsY_nFwVsj5pmxziqhQ-xV
source: fathom
enriched_on: 2026-03-03 20:01 UTC
</metadata>

---

## Summary

GrowthX's Jürgen Linde, Sydney Go, and Jason Gong evaluated the new Atlas content creation workflow, identifying critical bottlenecks in assignment brief generation and keyword research. The team proposed separating keyword research from content structure planning, incorporating broader keyword strategies from SEMrush (20-30 keywords) and semantic topics from top-ranking articles, and adding ICP knowledge gap sections to guide content depth by funnel position. Jürgen committed to documenting the improvements with video timestamps for ticket filing in their next session.

---

## Context

This internal GrowthX product team meeting focused on improving Atlas, an AI-driven content workflow tool used for client projects. Jürgen Linde, an engineering director, Sydney Go, a delivery lead, and Jason Gong, a technical specialist, gathered to address workflow inefficiencies discovered during recent testing with Webflow and Strappy clients. The meeting reflects ongoing tension between automation and control—while Atlas streamlines assignment brief generation, the team identified that the process oversimplifies keyword research and content structure decisions, reducing creative input and strategic nuance. The conversation reveals GrowthX's investment in building better internal tools to serve their high-value content marketing clients more effectively.

---

## Relevance

**To GrowthX Delivery:**
- Assignment brief generation workflow needs refinement to preserve strategic keyword research decisions without sacrificing speed
- New workflow separates keyword research (20-30 SEMrush broad matches + semantic topics) from content structure planning, allowing editors more control
- ICP knowledge gap framework proposed for assignment briefs to guide content depth by funnel position (top/middle/bottom of funnel)
- Atlas workflow efficiency issues with editing multiple briefs identified; usability improvements needed for scaling

**To CheckThat:**
- Keyword research process insights directly applicable to CheckThat's AI visibility indexing—semantic topic extraction and difficulty/volume weighting important for ranking signals
- Discussion of "People Also Ask" integration for content ideation mirrors CheckThat's approach to capturing query diversity in search visibility

**To GrowthX Business Development:**
- Client feedback loop strong (Webflow, Strappy test cases); indicates active iteration and client-driven product roadmap
- Assignment brief and keyword research improvements will reduce delivery timeline, enhancing competitive positioning against agencies using manual workflows
- Strong team collaboration (Jürgen, Sydney, Jason) managing complex handoffs and client-specific customizations signals operational maturity

---

## Overview

- Current Atlas workflow needs refinement, particularly in assignment brief and keyword research stages
- Team identified need for more control over keyword selection and content structure
- Proposed improvements include separating keyword research from content structure planning
- Importance of understanding ICP (Ideal Customer Profile) and user journey in content creation emphasized

---

## Key Topics

### Atlas Workflow Evaluation

  - Team ran test workflows for Webflow and Strappy clients
  - Identified issues with keyword selection, content structure, and workflow efficiency
  - Noted that assignment brief generation is slower in Atlas compared to AirOps
  - Output quality appears similar to previous system

### Keyword Research Process Improvement

  - Current keyword selection process relies too heavily on variations of the target keyword
  - Proposed improvements:
      - Incorporate broad match keywords from SEMrush (20-30 keywords)
      - Include semantically related topics from top-ranking articles
      - Consider keyword difficulty and search volume in selection
      - Integrate "People Also Ask" questions for content ideas

### Content Structure Planning

  - Suggestion to separate keyword research from content structure planning in the workflow
  - Importance of aligning content structure with ICP knowledge gaps and search intent
  - Proposed process:
    1.  Identify important topics from existing ranking articles
    2.  Conduct lighter keyword research for each topic
    3.  Create a cohesive assignment brief with primary and secondary keywords

### User Intent and ICP Consideration

  - Emphasized importance of understanding ICP's current knowledge and information gaps
  - Suggested tailoring content depth based on funnel position (top, middle, bottom)
  - Proposed adding an ICP knowledge gap section to inform content structure

### Workflow Usability Issues

  - Difficulty in editing multiple assignment briefs efficiently in the new interface
  - Need for better control over workflow steps and artifact referencing
  - Suggestion to improve assignment direction capabilities for specifying content types (e.g., how-to, listicle)

---

## Action Items

**Jürgen Linde (GrowthX)**
- Document meeting discussion on assignment brief improvements. Link timestamps from video recording (01:15:28 onwards). Include keyword research process, content structure creation, and proposed workflow changes.

- Schedule time with Jason tomorrow to review documented assignment brief improvement ideas. File tickets based on discussion.

**Sydney Go (GrowthX)**
- (Optional) Join meeting with Jason and Jürgen tomorrow to discuss assignment brief improvements if time allows.

**Jason Gong (GrowthX)**
- Review documented assignment brief improvements and provide feedback on technical implementation feasibility.

---

## Transcript
**Jürgen Linde:** A of How How you doing?

**Jürgen Linde:** How's it going?

**Jürgen Linde:** going good you say sorry my connection is very crap today i don't know what's wrong but i've been like my internet's been dead for the last week and i'm getting a technician out just to sort it out and i'm on my phone hotspot and it's just being so choppy i don't know what's wrong so thank you oh no worries um yeah no i so i

**Sydney Go:** And my parents have not had internet for a single week now, because the service provider is like, no, it's down, we can't make it, and they follow up every day, and I'm like, yep, it'll be up in 24 to 48 hours.

**Sydney Go:** Oh my god.

**Sydney Go:** I'm like, thank you god, didn't listen to your advice and get the same internet service provider.

**Sydney Go:** No.

**Sydney Go:** But yeah, no, internet struggle, I'm so sorry to go through that.

**Jürgen Linde:** Oops, sorry, my microphone was open.

**Jürgen Linde:** I said that sucks.

**Jürgen Linde:** I don't know what's wrong, but I keep hearing a robot voice on your side, not sure if that's me, well, it's likely me.

**Sydney Go:** Well, I'll have to ask Jason later and see if it's probably something on my end too.

**Sydney Go:** Honestly, it's been really weird recently.

**Sydney Go:** What's been weird?

**Sydney Go:** The whole internet.

**Jürgen Linde:** Yeah, I heard it was something to do with AWS.

**Jürgen Linde:** It's like my neighbors are fine, but I'm not doing fine for some reason.

**Jürgen Linde:** I've been in touch with technical support like four times.

**Jürgen Linde:** And they just keep telling me, have you tried switching it off and on again?

**Jürgen Linde:** And I'm like, duh.

**Sydney Go:** Yeah.

**Sydney Go:** Yeah, and at the end of the day, it's like, well, what can they do?

**Sydney Go:** It's not working.

**Sydney Go:** It's not working, unfortunately.

**Jürgen Linde:** Yeah.

**Sydney Go:** Yeah, but it's that.

**Sydney Go:** I'm sorry that you don't see that.

**Jürgen Linde:** Yeah, like I was literally working away from home today.

**Jürgen Linde:** Yeah.

**Jürgen Linde:** Thank

**Jürgen Linde:** Um, I've been at three different cafes.

**Jürgen Linde:** I went to one.

**Jürgen Linde:** The incident was bad there.

**Jürgen Linde:** So I moved to another place and then we found out they closed like almost immediately.

**Jürgen Linde:** And then we came back and like my partner and I, or my fiance, we work remotely together and we have like meetings, like on and off together.

**Jürgen Linde:** So we're trying to find like a place where we could both like leave, but then I had a meeting and then she had a meeting and then I had a meeting and then, yeah, that's where I rescheduled the day.

**Sydney Go:** Oh, no worries.

**Sydney Go:** Yeah.

**Jürgen Linde:** Yeah.

**Jürgen Linde:** Yeah.

**Jürgen Linde:** Yeah.

**Jürgen Linde:** So I guess, so what's our goal for this meeting?

**Jürgen Linde:** Because I don't know, I don't know if you saw, but Daryl has, it's a good call and they have some sort of issue with their workflow, not being.

**Jürgen Linde:** Properly imported from AirOps to Atlas, and it's apparently a very idiosyncratic client in terms of their requirements.

**Jürgen Linde:** So I'm hoping, if possible, if it's not dedicated to Webflow, we can use them sort of as a case study to test out the stuff, but I'm not sure if that's something we can do.

**Sydney Go:** Yeah, I actually don't know what Jason wanted to, I think he just wanted to run Workflow in parallel and see what breaks.

**Sydney Go:** Have you had any success running the Workflowers?

**Jürgen Linde:** Sorry, what?

**Sydney Go:** Have you had any success?

**Sydney Go:** I'm so sorry, I can't properly hear you.

**Jürgen Linde:** It must be on my side.

**Sydney Go:** I'm not sure if I understood the question, but basically, like,

**Jürgen Linde:** The workflow that we have in Atlas is very templated, but the one in the ideal path in AeroOps is basically like has extra steps and stuff like that.

**Jürgen Linde:** And it needs to be replicated in Atlas because of client requirements and all that stuff.

**Jürgen Linde:** And I guess I can do it on my own, but it would be nice.

**Jürgen Linde:** Like the thing is, like, I know you've, you know, you know, the grid so well, like you said that you had like 30 steps integrated, which is mad.

**Jürgen Linde:** And I would love to just, I'm not familiar with mapping my own workflows.

**Jürgen Linde:** So that's something I definitely want to see how to do today is just so I can do it with, with good call if possible.

**Sydney Go:** Yeah, I've actually not dug into this new system yet because as I started.

**Sydney Go:** Well, yesterday, because I'm trying to get Stratley out the door, so that when we do the handoff, it's a little bit easier.

**Sydney Go:** Jason said that he's not going be here for another 15 minutes.

**Sydney Go:** No, I don't think I can help you there, unfortunately.

**Sydney Go:** That's all good.

**Sydney Go:** Sorry.

**Sydney Go:** But yeah, it's been a lot of moving parts.

**Sydney Go:** How are your team feeling about all of this?

**Jürgen Linde:** Well, it's hard to tell because I'm not working with Vappy anymore.

**Jürgen Linde:** Matt's just doing solo on that because it's going so well.

**Jürgen Linde:** And I don't have Saskia anymore as well.

**Jürgen Linde:** She's been moved to a different client.

**Jürgen Linde:** So I'm basically just working with Matt, and I'm just working with him.

**Jürgen Linde:** He's also been assigned to go to good call for the first time.

**Jürgen Linde:** Matt.

**Jürgen Linde:** We haven't had a chance to think of that, but based on the private channel with the other MEs, it seems like not everyone is exactly happy or not expecting the changes, which makes sense, because I feel like it was all only communicated between the directors and the MEs, which makes sense.

**Jürgen Linde:** Yeah, it's growing.

**Sydney Go:** Yeah.

**Sydney Go:** How's it going with your team?

**Sydney Go:** I told my team that, so I looked up to their directors going to be, reassured them that their directors are going to be awesome, their managers, managing editors are going to be awesome, they're going learn so much more from them, than they have already learned from me, so keep chugging along, and I'm available if they want to talk.

**Sydney Go:** Yeah.

**Sydney Go:** Yeah, it's been, yeah, and I think, I think everyone knows this is that I don't know, but I think it's such a pain point on my team was that we have already.

**Sydney Go:** Little relationships, and they're pretty fad to see those relationships go, so I think on my end, my main thing is I keep telling them I'm not going to die, you can still message me, their relationship is still here, and just reassuring them that they're really good hands, no matter where they're really good hands, it's a lot of change, we're all in flux with it all, it's going to be fine, yeah, tell them.

**Jürgen Linde:** Yeah, because like to me, this whole change reminds me of when they changed the whole Slack setup, so that it's like D and B slash, or whatever channel, and I was like, ooh, we're using linear, it's like, it feels like we're being micromanaged, but as soon as we got used to it, was like, okay, cool, this makes sense, but it felt scary to hear about that major change initially.

**Jürgen Linde:** I've seen about it scary.

**Jürgen Linde:** Yeah.

**Jürgen Linde:** But I guess one thing I'll never forget at a previous job, I was hired, and then my first onboarding call was basically like, if you're going to take anything away from this, remember, don't get used to anything.

**Jürgen Linde:** And it's always the truth.

**Jürgen Linde:** It's never, it's the one thing I've had to abide by.

**Jürgen Linde:** No matter how much you feel like you're comfortable, if you're comfortable, it means it's going to change, like, pretty soon, you know, touch wood.

**Jürgen Linde:** Yeah, yeah, especially in the tech industry.

**Sydney Go:** Like, that's the whole reason I left M Rushes, because nothing's changing.

**Sydney Go:** So it's the opposite problem.

**Sydney Go:** I was there for, like, I think, I was there for a year, and then I got a promotion, I got role changes, and it was all moving very quickly.

**Sydney Go:** think we were experimenting, things were changing, things were happening, it was a lot of fun.

**Sydney Go:** And then, like, two years later,

**Sydney Go:** Like, nothing had changed from that point on.

**Sydney Go:** Like, my skills aren't growing, I am stagnating, I can't work in the way that I want to work because we don't have room for experimentation anymore.

**Sydney Go:** At that point, I was like, yeah, okay, I'm going to go on one more.

**Sydney Go:** That's another thing.

**Jürgen Linde:** I don't know if you ever played Assassin's Creed, but there was one point where you, there was a point in the game where you explore this, like the present day version of a city that was quite popular during the Renaissance.

**Jürgen Linde:** And it looks exactly the same from like 500 years ago.

**Jürgen Linde:** And the thing is like, if something doesn't change, it means it's dead.

**Jürgen Linde:** You know, if it doesn't adapt, it means it's, well, if it does adapt, then it means it's living.

**Jürgen Linde:** If it looks exactly the same, then it's dead.

**Jürgen Linde:** Like the same with life.

**Jürgen Linde:** You know what I mean?

**Jürgen Linde:** Yeah, that's true.

**Jürgen Linde:** Yeah, I've actually started playing Spirit Faire.

**Sydney Go:** I'm not sure if you've heard of it.

**Sydney Go:** Say again?

**Jürgen Linde:** Spirit Faire.

**Jürgen Linde:** No, I don't think I've played that.

**Sydney Go:** It's pretty good, but it is.

**Sydney Go:** It's a lot of that.

**Sydney Go:** Clear up Spirit.

**Sydney Go:** Sorry?

**Sydney Go:** Sorry, clear up Spirit Faire.

**Sydney Go:** Oh, no, no, no, I haven't played that.

**Jürgen Linde:** It's really good.

**Sydney Go:** Like, if you have some time, just do it.

**Sydney Go:** joke about it lot of times now.

**Sydney Go:** But, yeah, in the time of play, it's really, really good.

**Sydney Go:** Storylines are all about that.

**Sydney Go:** Like, things change, you have to accept the past and also be forward.

**Sydney Go:** Ooh, it looks cozy.

**Sydney Go:** It's so cozy, I mean, like...

**Sydney Go:** Yeah.

**Sydney Go:** Yeah.

**Sydney Go:** But it's a massive world.

**Sydney Go:** I love it.

**Sydney Go:** So you're adventuring throughout the system, massive world.

**Sydney Go:** Like, yeah, I don't know when to be finished.

**Sydney Go:** Yeah.

**Sydney Go:** reminds me of what?

**Jürgen Linde:** I'm so sorry.

**Jürgen Linde:** I think it's my end.

**Jürgen Linde:** I'm really struggling to hear what you're saying.

**Jürgen Linde:** No, sorry.

**Jürgen Linde:** reminds you of what?

**Jürgen Linde:** Of Cisco Elysium.

**Jürgen Linde:** Have you ever heard of it?

**Jürgen Linde:** It's basically you play this deadbeat cop who is struggling with alcoholism.

**Jürgen Linde:** the world is, it's like, imagine if you play D&D, but it's all about like, you roll for dialogue and story.

**Jürgen Linde:** It's, you don't like, you don't fight, you don't do anything like that.

**Jürgen Linde:** It's all just like, you interact with the world.

**Jürgen Linde:** And it's honestly like, know, I

**Jürgen Linde:** One of the best story-driven games I've played, it's absolutely amazing, yeah, highly recommend it, because the sort of art style that I'm seeing right now, at least in the cover image, it reminds me a lot about that, the art style is amazing as well.

**Jürgen Linde:** Oh yeah.

**Sydney Go:** Yeah.

**Sydney Go:** I love a good game with good art.

**Jürgen Linde:** Yeah, yeah, like I checked out their artist's inspirations, and I'm like, oh my word, this is like, you know, I don't even know, Jenny Saville, I think, is the inspiration, just like the sort of acrylic, impressionist way of depictions, it's amazing, but yeah.

**Jürgen Linde:** Anyway, I think, I don't think Jason will be joining us right now.

**Sydney Go:** I think it may have slipped through the cracks, but he should be here at any minute now.

**Sydney Go:** Okay.

**Sydney Go:** I presume he has meetings at the same time.

**Jürgen Linde:** Actually, he's trying to.

**Sydney Go:** remember the CMS that I showed you last week?

**Sydney Go:** He's trying to get someone else access so that I don't need to upload.

**Sydney Go:** Again, spent two hours a day just uploading.

**Sydney Go:** No, that's unnecessary.

**Jürgen Linde:** I have so many things to do, also this is a deadline that we cannot receive.

**Jürgen Linde:** I feel like as soon as you'd say, hey, this is taking me too much time, someone will just say, let's automate it.

**Jürgen Linde:** How do you automate this really weird thing?

**Jürgen Linde:** Yeah, we're trying.

**Sydney Go:** We really are.

**Sydney Go:** We just can't because they blow.

**Sydney Go:** Well, no, it's not that.

**Sydney Go:** It's that.

**Sydney Go:** It's a very complicated system.

**Sydney Go:** Both the customer and we are working on the API, because they want to get it through the door too, so that they have some writing team.

**Sydney Go:** They're running into the same issues.

**Sydney Go:** So it's a problem across the board that everyone is trying to solve.

**Sydney Go:** Hopefully something that we should support on is the nice thing, that we're adding value, even in the smallest way, there.

**Sydney Go:** Yeah, I say we, I mean Jason, because I know nothing about this.

**Sydney Go:** Yeah, yeah.

**Sydney Go:** Yeah, it's been very instrumental in keeping our customers happy because he's so good at all the technical things, but I can deliver the content and make sure that guests are on time and talk about it.

**Sydney Go:** Yeah.

**Sydney Go:** Yeah.

**Sydney Go:** Hey.

**Sydney Go:** Hey.

**Sydney Go:** Hi.

**Sydney Go:** How's it going?

**Sydney Go:** How's going?

**Jason Gong:** How's it going?

**Jason Gong:** Start uploading.

**Sydney Go:** Yeah, I'm telling you, I just went to DIY.

**Sydney Go:** Yeah, no, we need help, for sure.

**Jason Gong:** I mean, he got Okta, and he's downloading Island, and no issues yet.

**Jason Gong:** We, like, we spun up a virtual machine in San Jose, and he's using that.

**Sydney Go:** Okay.

**Sydney Go:** Okay, yeah.

**Sydney Go:** Everything went through, it all live.

**Sydney Go:** I mean, like, internally?

**Jason Gong:** You're sorry, say that again?

**Sydney Go:** Apparently, we're okay with doing all that.

**Sydney Go:** No comment.

**Jürgen Linde:** Jason, I watched that call, that interview call with, I can't remember what the guy was, the, the, the, the, the guy from Silicon Valley that you posted over the weekend, I think it was.

**Jürgen Linde:** I I don't know.

**Sydney Go:** I I

**Jürgen Linde:** Yes, yes.

**Jürgen Linde:** It was pretty professional looking.

**Jürgen Linde:** was surprised.

**Jürgen Linde:** was, you know, weird seeing you with a body below your torso.

**Jürgen Linde:** We got a whole production team here.

**Jason Gong:** Are you guys both off-camera or am just lagging?

**Sydney Go:** No, we were off-camera, but Jürgen's internet was lagging.

**Jürgen Linde:** We don't have a ton of time.

**Jason Gong:** Maybe we can just try to use some of these workflows.

**Jason Gong:** Have you guys successfully used anything yet?

**Jürgen Linde:** Like, actually, I spoke with Daryl today and he said, like I spoke, and I don't know what we're focusing on today, but if we could use Google as a case study in a way to test out these workflows, that would be great because that's something I need to do for him today.

**Jürgen Linde:** Yeah, like, I'm, like, jumping with Twitter.

**Jürgen Linde:** Webflow and GoodCall for this week, and both are, I can tell, are pretty critical, so, yeah.

**Jason Gong:** Why don't we try, I mean, really any of them, I mean, Webflow, GoodCall, or Abnormal, or Strappy.

**Jürgen Linde:** Yeah, go ahead.

**Sydney Go:** Sorry, I've seen it, Jason, so the Webflow integration pages, I saw that someone ran something, and it took 94 minutes to run one integration page, so I was like, I'm going leave this alone for now, and see.

**Sydney Go:** Oh, you tried to run it, and it took 90 minutes, is that what you said?

**Sydney Go:** Someone ran something, like, there's one entry in the Webflow thing, I didn't do that, so I could hear someone maybe troubleshooting, and it took 94 minutes.

**Sydney Go:** Thank you.

**Sydney Go:** you.

**Sydney Go:** Thank Thank

**Jürgen Linde:** By the way, Sydney, I think, like, I'm struggling to hear you, but I can hear Jason clearly.

**Jürgen Linde:** I'm not sure if you can do it on your end, but there's a setting in Google where you can switch off the studio sound in your microphone, because it usually makes things sound a bit like, Yeah, I'm not sure if you can hear me clearly.

**Sydney Go:** Is this better?

**Jason Gong:** No, yours sounds like it's just a bad microphone.

**Jason Gong:** Is this the normal microphone you're on?

**Jason Gong:** Yeah, this is the normal microphone.

**Jason Gong:** I feel like it's coming out of the wrong microphone.

**Sydney Go:** No, it is.

**Sydney Go:** Here, let me just switch to...

**Sydney Go:** Is this better?

**Sydney Go:** Oh, wait.

**Sydney Go:** Is this better?

**Sydney Go:** Yeah.

**Sydney Go:** Yes.

**Sydney Go:** Yeah.

**Sydney Go:** Can you hear me?

**Sydney Go:** you just by the...

**Jürgen Linde:** Ah, awesome.

**Jürgen Linde:** Okay, cool.

**Jürgen Linde:** Okay, cool.

**Jason Gong:** Let's just start...

**Jason Gong:** Generate...

**Jason Gong:** So you're saying, okay, why don't we just look at the Webflow one, because that one, I generated like 200 last night, because I fixed, I realized that domains, like, we didn't really set properly, still looked like it was maybe hallucinating some URLs or something, I don't know, but basically, like, the way we set it up, like, it would not put a developers.webflow.com, like, if you give it webflow.com, it's not going to look at developers.webflow.com, so you have to, like, explicitly list all the URLs, I think.

**Jason Gong:** Yeah, that's what it gave me.

**Jürgen Linde:** Like, I did that with Unstructured, and I gave it, like, the docs pages and the blog pages, like, the domain section, and it did not reference any of them.

**Jürgen Linde:** So I think it's only URLs.

**Jason Gong:** Are you talking about the research stuff, Jürgen, or?

**Jürgen Linde:** For the, I think it was, yeah, for the research URLs.

**Jason Gong:** Because we have this, like, we have a custom one built, but that one, too, yeah, basically the same.

**Jason Gong:** So, let's see, I don't even have this open, what is it against, do you, or?

**Jürgen Linde:** Atlas.growthx.ai, Atlas.ai, growthx.ai, yeah.

**Jürgen Linde:** Let's just try Webflow.

**Jason Gong:** Maybe I can show my screen, or do you want to go through it, Sydney, or do you want me to do it?

**Sydney Go:** No, you can do it.

**Sydney Go:** I don't think I put anything in there yet.

**Sydney Go:** Yeah, there's nothing in there yet.

**Jason Gong:** We'll make a lot of facts on the end there.

**Jason Gong:** Okay, so, because everything that we don't have is grayed out, why don't we look at editorial?

**Jason Gong:** there.

**Jason Gong:** We'll make We'll We'll make a of of

**Jason Gong:** Are there two articles?

**Jason Gong:** Oh, wait.

**Jason Gong:** Oh, okay.

**Jason Gong:** It's one for each.

**Sydney Go:** I don't know what the difference between editorial and dev pages are.

**Sydney Go:** Or is this just blog and then dev pages?

**Sydney Go:** Because I've only ever been using dev pages.

**Jason Gong:** I feel like they just copied everything over from here.

**Jason Gong:** So whichever one you're using here is what that one is.

**Jason Gong:** Which one were we using here?

**Jason Gong:** Dev pages.

**Sydney Go:** Not this one's ideal path one.

**Jason Gong:** Oh, yeah.

**Jason Gong:** That was the new one.

**Sydney Go:** Yeah.

**Sydney Go:** That one we just started using, so.

**Sydney Go:** Okay.

**Jason Gong:** There's nothing in here.

**Jason Gong:** I mean, let's just do one that we did here just to see what it looks like.

**Sydney Go:** If you want a pre-populated one, I already populated some for Strappy.

**Jason Gong:** Populated.

**Jason Gong:** Oh, okay.

**Jason Gong:** Yeah, because I kind of want to compare it to, like, something.

**Jason Gong:** So maybe using Strappy's better.

**Sydney Go:** I have it till the assignment generation.

**Sydney Go:** I'm editing it one by one though.

**Sydney Go:** Okay.

**Sydney Go:** Yes, I got the assignment brief.

**Jason Gong:** Oh, you're saying you've been using this one already?

**Jason Gong:** Yeah.

**Jason Gong:** Okay.

**Sydney Go:** Those are all new articles.

**Sydney Go:** So.

**Sydney Go:** Okay.

**Sydney Go:** Cool.

**Jason Gong:** So.

**Jason Gong:** Okay.

**Jason Gong:** Sure.

**Jason Gong:** Link site.

**Jason Gong:** Fact check.

**Sydney Go:** Strappy's fact checker isn't up yet.

**Sydney Go:** The copy AI, just so you know.

**Jason Gong:** Okay.

**Jason Gong:** But this, this works?

**Jason Gong:** It should work.

**Jason Gong:** Um, I've always wondered like, do we get any direct?

**Jason Gong:** man.

**Jason Gong:** right.

**Jason Gong:** gonna, Thank

**Jason Gong:** I how much to put here.

**Jason Gong:** This seems like a little thin.

**Sydney Go:** From the call earlier, Hanser said that we can only put in basically target audience and keep it focused on that.

**Sydney Go:** And we can't prompt it like we do in LLM.

**Sydney Go:** So, yeah, I was going to try doing like a whole full thing, but he said it doesn't quite work.

**Sydney Go:** Got it.

**Jason Gong:** Should we fill these out?

**Sydney Go:** Before generating?

**Jason Gong:** Yeah, I didn't know that those were filled.

**Sydney Go:** Okay, yeah, I'll fill those out.

**Jason Gong:** Yeah, let's just copy and paste what we have already.

**Jason Gong:** I just want to run one end to end.

**Sydney Go:** Strappy's ideal path should be good.

**Sydney Go:** The article generation ideal path.

**Jason Gong:** All right, so we have audience.

**Jürgen Linde:** So,

**Jason Gong:** Description, optional, guidelines, okay, you can pick, personas, okay, there's one, okay, yeah, let's make sure these are updated, I feel like these matter a lot, this one's a little short, wonder, are they all like that?

**Sydney Go:** Yeah, I made it a little bit shorter, I think, in the ideal path one, because it worked better.

**Jason Gong:** was just a little longer, that was just a new line, um, compliance, things like personas we're talking about here.

**Jason Gong:** Highlands, rules, page templates, other facts.

**Jason Gong:** Interesting.

**Jason Gong:** Writing guidelines.

**Sydney Go:** Try to get the last one.

**Sydney Go:** Or the second to the last one, sorry.

**Jason Gong:** This one?

**Jason Gong:** Yeah.

**Jason Gong:** Anything else?

**Jason Gong:** Name, Persona, company, CTAs.

**Sydney Go:** I don't love that one, so you can leave it if you don't want to use it.

**Sydney Go:** Okay.

**Jason Gong:** Okay.

**Jason Gong:** And then article generation.

**Sydney Go:** Okay, so should probably be runoff.

**Sydney Go:** Let's see.

**Sydney Go:** Okay, so only topic.

**Jason Gong:** Assignment Direction, Output, Steps, Artifacts.

**Jason Gong:** Okay, so the assignment group, we've got Audience, let's see what we have.

**Jason Gong:** So we have Audience, Company, Writing Guidelines, and here we have Audience, Company, Name, Assignment Direction, is that one-liner you put, opening context is here, that should be right, think, what's this last one, writing, that one goes in, Style Adaptation, and it goes in, Article Drop, seems right, which one do you think is a good one, to, so.

**Sydney Go:** Hmm, yeah, stop.

**Sydney Go:** Thank you.

**Jason Gong:** Are you sure this is, like, only supposed to not say anything about the article and just about the personas?

**Sydney Go:** That's where I was confused, because that's what it sounded like on our call earlier at, like, 830.

**Sydney Go:** Although we could look at what, I think GitHub's the one that was tested.

**Sydney Go:** We could look at GitHub and see what they're doing and see if it's more.

**Jason Gong:** Gitpod or GitHub?

**Jason Gong:** Gitpod, sorry.

**Jason Gong:** Let's see if it's populated.

**Jason Gong:** This is being recorded, right?

**Jason Gong:** Okay, good.

**Jason Gong:** Take

**Jason Gong:** There's like nothing in here.

**Jason Gong:** I'm just going to ask the question anyway.

**Jason Gong:** Cool.

**Jason Gong:** Let's see.

**Jason Gong:** Is there a channel we're all like dumping this into at the moment?

**Sydney Go:** Linear, I think is what they said, but maybe in general?

**Sydney Go:** Like D-general?

**Jason Gong:** Okay.

**Jason Gong:** I'm going to give you an email address.

**Jason Gong:** Oh.

**Jason Gong:** Okay.

**Jason Gong:** Okay.

**Jason Gong:** Yeah.

**Jason Gong:** Okay.

**Jason Gong:** Okay.

**Jason Gong:** Okay.

**Jason Gong:** Okay.

**Sydney Go:** Okay.

**Jason Gong:** Okay.

**Jason Gong:** Let's just run it, I guess, rerun, maybe I shouldn't rerun, I think it said four minutes, let's just do, okay, all right, so this is running, toggle developer info, okay, let's just start up, sure, how are you supposed to look at the output, save, no, so if you go to a different one that already has an output, after it runs the step, there's an output tab up there, because I didn't put output there, okay, got it, yeah, next step, sure, okay, so that means there's, there's like two views here, we have this, which is,

**Jason Gong:** I guess there's no configuration options for any of these.

**Sydney Go:** Because you have to run the step before for those to open up.

**Jason Gong:** URL, status, copy name, skip outline generation.

**Jason Gong:** Okay.

**Jason Gong:** mean, did they say anything about just running one at a time?

**Jason Gong:** Can I just run all of them?

**Sydney Go:** You can run all of them.

**Sydney Go:** They said, as long as you don't run like 5,000 at a time, it should be good.

**Jürgen Linde:** Yeah, this takes longer to do the quality.-hmm.

**Sydney Go:** It's going to run everything?

**Sydney Go:** Oh, if you select it like that, then it'll run all the way to the end, like auto run.

**Sydney Go:** So that's a good one.

**Sydney Go:** Yeah.

**Sydney Go:** And then on the side, yeah, you have to click on that.

**Sydney Go:** And then on the side of where assignment briefings are, yeah, in there.

**Sydney Go:** Okay.

**Sydney Go:** right.

**Sydney Go:** So, okay.

**Jason Gong:** I mean, we like add bookmarks, okay, let me just, let's see, okay, so somebody needs to like go through this after, and then, um, that was, um, we got, uh, now once everyone's, that one of the many at the top.

**Jason Gong:** Here, let's see, I'm moving on, close, oops, here.

**Jason Gong:** Um, okay, so you're telling me I have to, do this basically.

**Jason Gong:** Mm-hmm.

**Jason Gong:** And, what's this view called?

**Sydney Go:** Pipeline view?

**Sydney Go:** Pipeline input?

**Sydney Go:** Pipeline input?

**Sydney Go:** Pipeline Pipeline

**Jason Gong:** Okay, I think I just got somebody to go through this.

**Jason Gong:** Hopefully, create some tickets for them.

**Jason Gong:** Let's see.

**Jason Gong:** Okay, let's just run these.

**Jason Gong:** Oh, selected rows can be run at this time.

**Jason Gong:** What does that mean?

**Sydney Go:** Want to try to add it as a new, like as a new entry, since I've already run assignment brief, it might not want to go.

**Sydney Go:** That's dumb.

**Sydney Go:** Yeah, so maybe try to add, try to add it as a new row and see if it'll run.

**Sydney Go:** Oh, it died.

**Jason Gong:** Okay, so select a row with a step run review.

**Jason Gong:** Okay, so select a review.

**Jason Gong:** you.

**Jason Gong:** So we're going to go okay.

**Jason Gong:** Has new rows.

**Jason Gong:** I'm just saying you can import, okay.

**Jason Gong:** So I need to go through, paste, import.

**Jason Gong:** It goes to the top.

**Jason Gong:** It goes

**Jürgen Linde:** It's maybe not better to keep it at the top, because it's like your most recent stuff.

**Jürgen Linde:** I actually didn't mind it at the top.

**Jürgen Linde:** If it's at the bottom, you keep scrolling all the way down.

**Jürgen Linde:** That was actually quite annoying.

**Jürgen Linde:** Yeah, they have to rely less on archiving everything, and you just have the most recent stuff.

**Sydney Go:** Oh, did you save it?

**Sydney Go:** Do you remember which ones we just read?

**Jason Gong:** For the times to...

**Jason Gong:** Confuse.

**Jason Gong:** That'll be great.

**Jason Gong:** I think we were on this one.

**Jason Gong:** oh let's see um so basically the same format right as our old and the output is still the same problems like especially for this article i need a quick start right we definitely need a custom gpt can i chat with this other thing

**Sydney Go:** Is this Grammarly?

**Jason Gong:** What did I just click?

**Jason Gong:** That's Grammarly.

**Sydney Go:** Grammarly sucks, I hate Grammarly.

**Jason Gong:** Did I just change something by accident?

**Jason Gong:** Oh no, didn't.

**Jason Gong:** So...

**Jason Gong:** So...

**Jason Gong:** Keeps adding...

**Jason Gong:** Use cases, what were the other ones?

**Jason Gong:** Looking forward.

**Sydney Go:** Yep, yep.

**Jürgen Linde:** Or...

**Sydney Go:** There's one more at the end.

**Sydney Go:** Oh, um, Common Failures, like where it fails, basically.

**Jürgen Linde:** Yeah, and I'll always also use, um, the conclusion always reads conclusion, and if you just write conclusion, no one's going to read past that, so if it just has a more descriptive summarizing conclusion hitting, then it will help a lot, because, yeah.

**Jason Gong:** This doesn't really matter, I don't mean for this to be, like, perfect, I just want to see...

**Jason Gong:** You just want to see version of those.

**Jason Gong:** Okay.

**Jason Gong:** Lion

**Jürgen Linde:** Oh, yeah, and another thing, when you, it's not evergreen when you, like, give it a article and keeps contextualizing it within the current year.

**Jürgen Linde:** Like, I feel like I have to remove that every time, like, how do I rephrase this?

**Jürgen Linde:** So it's not saying, like, it's only irrelevant this year, but next, within a couple of months, it could be, like, out of date, when you have to go manually back to every post.

**Jürgen Linde:** Like, I've said it before where they were, I don't know how they did it, but there was this function where you could put it in, like, the color brackets and say the word year, and it would auto-correct it to the current year every time without having to manually edit it and keep track of all that.

**Jürgen Linde:** I'm not sure if we have that functionality.

**Jason Gong:** I think my functionality would have to be in the CMS, though, the customer CMS?

**Jürgen Linde:** Hmm.

**Jürgen Linde:** Like when you do listicles or best practices, like you have to do this in the year 2025, okay, then it's, you know, six months and irrelevant.

**Jürgen Linde:** Yeah.

**Jason Gong:** Okay, so save.

**Jason Gong:** And now.

**Jason Gong:** Do research.

**Sydney Go:** I know that there is a way to version, oh, did you hit save before hitting research?

**Sydney Go:** Yeah.

**Jason Gong:** Oh, so.

**Jason Gong:** Let's see.

**Jason Gong:** Okay.

**Jason Gong:** Okay.

**Jason Gong:** Okay.

**Jason Gong:** Thank you.

**Jason Gong:** Okay, run that one.

**Jürgen Linde:** Okay, also to add that that list of redundant sections, it always adds best practices.

**Jürgen Linde:** Like, best practices can often just be their own blog posts by default.

**Sydney Go:** That's The digital, oh, digital customer experience is already going to outline.

**Jason Gong:** I don't know what timestamp this is, but clicking this button does nothing.

**Jürgen Linde:** Yeah, it only goes from one step to the next.

**Jürgen Linde:** can't do, like, go to...

**Jürgen Linde:** Like step five, and then water runs the previous steps.

**Jürgen Linde:** You have to do it manually every time.

**Jürgen Linde:** I think we brought that up in the chat in our Atlas training yesterday.

**Sydney Go:** But if you go into the sidebar, will it work?

**Sydney Go:** Sidebar?

**Sydney Go:** Yes, if you open it and then do the pipeline view or whatever it is, will it work?

**Sydney Go:** Because it might just be a problem with the row.

**Jason Gong:** I I think the reason you insert at the bottom is like you don't shift everything down constantly.

**Jason Gong:** You know, like when you say it's row five, it's always row five.

**Jason Gong:** Mm-hmm.-hmm.

**Sydney Go:** Mm

**Jason Gong:** I like I don't know why this is down here now, and I thought something was running outline, but it's not anymore.

**Jason Gong:** Okay, now let's keep running with this one, quick click.

**Jürgen Linde:** Sydney, in your testing, how does the speed compare to air off when running?

**Jürgen Linde:** Oh, it's slower.

**Sydney Go:** It's definitely slower.

**Sydney Go:** Assignment brief is slower.

**Jürgen Linde:** Do you think the briefs are better quality than usual?

**Sydney Go:** It's the same.

**Sydney Go:** It's almost the exact same brief, I think.

**Jürgen Linde:** Okay, so we got a bunch of those.

**Sydney Go:** Yeah, Panzer did mention that this is set up with the exact same APIs as Aero, so it should be outputting the same thing.

**Jürgen Linde:** Yeah, except for the using Sonnet for Claude, which...

**Jürgen Linde:** Oh, it was fine.

**Jason Gong:** Now we go to outline.

**Jason Gong:** Outline, pulling all the previous steps.

**Jason Gong:** I mean, guess...

**Jason Gong:** I'm to think of what else we do here.

**Jason Gong:** I mean, is it annoying to you guys that you can't...

**Jason Gong:** on everything from the grid view and you have to like kind of come in here or not really like how do you guys usually work?

**Sydney Go:** It's pretty annoying because I usually like editing like the assignment briefs, I'll do it one after the other versus closing, opening, closing, opening.

**Sydney Go:** And it would be, it's, the problem is that I would have to open the pipeline view to even get to the assignment brief as well.

**Jürgen Linde:** So, XML format

**Jürgen Linde:** The XML format, the default editing in the grid, as a nice to have, because lockdown doesn't work and it makes it glitch out.

**Jason Gong:** So the answering...

**Jason Gong:** Nope.

**Sydney Go:** Okay, outline's done.

**Jason Gong:** ...

**Jason Gong:** ...

**Jason Gong:** ...

**Jason Gong:** Just a minute, view, we're clicking around, maybe it's just lagging, yeah, it's just lagging.

**Jason Gong:** Okay, so we have research stuff, the brief now, so now I am, this is the brief, okay, okay, here we go.

**Jason Gong:** Alright, so this is the outline, let's see, is it following, this step, hold on, let's say I remove this, here we go.

**Jason Gong:** Thank you.

**Jason Gong:** you.

**Jürgen Linde:** Thank you.

**Jürgen Linde:** you.

**Jason Gong:** What might be nice, if it's not off-topic, those...

**Jason Gong:** Say that again, and why am I in this view now?

**Jürgen Linde:** What might be nice, you know, those redundant sections that we always get.

**Jürgen Linde:** If, you know, like how Panda said, if we, like, prompt in this path where it doesn't loosen it stuff, and it says, like, input example here instead of making up something with the best practices and, you know, looking forward or whatever, if that's something that's worthy of a blog post, maybe there's a step that says, hey, there's a section that we generate.

**Jürgen Linde:** I mean, it's beyond the scope of the blog post.

**Jürgen Linde:** Maybe we could say, like, here's a step where there's related articles to generate or something like that.

**Jürgen Linde:** It might be too much to ask, but it would be nice.

**Jason Gong:** Yeah.

**Jason Gong:** I think I just want to steer this more, you know?

**Jason Gong:** That's the problem for me.

**Jason Gong:** It's like we have no ability to steer.

**Jason Gong:** Because you can do that in Cursor, which is what Daniel has recommended before.

**Jürgen Linde:** Or, like, you take it out of the Cursor and you put it in the Cursor.

**Jason Gong:** I'm just going to do that.

**Jason Gong:** You can have to look at your different sections.

**Jürgen Linde:** Yeah.

**Jürgen Linde:** It'll be too much work.

**Sydney Go:** And it's very hard to scale to do it that way.

**Sydney Go:** If we're going have to go into every single article and go in a Cursor and then prompt it that way, then it's just we're not going to hit our targets.

**Sydney Go:** It's also, I'm not sure if they're seeing where we'll even be able to do that.

**Jürgen Linde:** Yeah.

**Jürgen Linde:** I'm

**Jürgen Linde:** Yeah, I guess I'm just coming from the fact that no prompt will work the same across articles.

**Jürgen Linde:** So if you have to tinker every time with a prompt that may have worked really well in the previous article, even in the same sort of list.

**Jason Gong:** Is this for the outline step to do this?

**Jürgen Linde:** Outline and brief, I think.

**Jürgen Linde:** Yeah, because those are the parts we have to focus on most.

**Jürgen Linde:** I think, like, if we can make the workflow do well in the, like, literally the first two steps of the brief and outline gen, then the rest of the workflow would work much better.

**Jürgen Linde:** Because, you know, you have feedback where you get, like, love lines, like, fix this minor thing, and that's fine.

**Jürgen Linde:** But the outline, you need major edits to usually get it right, in my experience.

**Sydney Go:** I actually really, Jason, if you remember, had, for strappy integration pages, we had that.

**Sydney Go:** Assignment brief feedback column, that worked really well, especially for like, templated articles.

**Sydney Go:** That would be great.

**Sydney Go:** Yeah, it would generate the assignment brief, and then I would say, hey, here's the template that we need to follow, and then it would follow that template, and having something for the assignment brief steps just across the board.

**Jürgen Linde:** Yeah, because we have with VAPI, like, template articles where it's like, VAPI versus competitor, and it has to follow the certain outline with all the research, like, key decision factors that people care about.

**Jürgen Linde:** If you can follow this template, adapt your generated outline to this, and maybe mix and match, you know.

**Jürgen Linde:** But instead, you have the final draft with feedback, Jan, with feedback, that would be great.

**Jürgen Linde:** Again, that's like.

**Jürgen Linde:** As Panza said, 80% of your time spent in workflow generation should be spent on the brief.

**Jürgen Linde:** If there's more steps to control that, that would be great.

**Jürgen Linde:** Because I know Matt told me, like, his workflow works well, but he's still hesitant to trust the research based on the outline brief, and there's no way to control that or see where everything's coming from.

**Jürgen Linde:** So if there's more control, that would be great.

**Sydney Go:** This is, would it be possible to also basically feed this step secondary semantically related keywords?

**Sydney Go:** Because I feel like that's what a lot of our articles are missing that I've been adding back into Abnormal's brief.

**Sydney Go:** But what I would do is I'd just make up the numbers for them, just that they're in the same format.

**Jürgen Linde:** Because it's easy to generate, like, you know, like related e-terms, because all it does is generate the keyword and often does it verbatim.

**Jürgen Linde:** easy to do.

**Jürgen Linde:** Like, what is this?

**Jürgen Linde:** Like, people always ask, quote, what is this?

**Jürgen Linde:** That's bad SEO.

**Jürgen Linde:** You can at least, like, say, how could you phrase this differently?

**Jürgen Linde:** Because it always, like, gives the keyword, holds it, and that's all it goes over.

**Jürgen Linde:** Instead of, you know, talking more organically.

**Sydney Go:** So, one of the...

**Jürgen Linde:** Keyword stuffs instead of talking about the keyword organically in a way that you would say it in a sentence if you were a human.

**Jürgen Linde:** That happens briefly or during the outline, I think.

**Jürgen Linde:** Actually, might be talking about different things.

**Sydney Go:** We're going to get the final article.

**Jürgen Linde:** Yep.

**Jürgen Linde:** So, I'd like to steer the keywords as well.

**Sydney Go:** So, one easy way to do it is if, since we're already using SEMrush, can I share my screen for a little bit?

**Sydney Go:** Go.

**Sydney Go:** Go.

**Sydney Go:** So just having simple things like this in there, that it's not just, so our, for example, our keyword is custom digital experience, having things that are not just variations of customer digital experience in there would really help.

**Sydney Go:** And this is in SEMrush, so we can pull it.

**Sydney Go:** Though I don't know how the API works, but we can pull it from SEMrush.

**Sydney Go:** It's an easy way to do it.

**Jürgen Linde:** How do you use this keyword in a sentence?

**Jürgen Linde:** Use that variation across the article as well.

**Jason Gong:** Let's break this down.

**Jason Gong:** So like if we're picking keywords and secondary keywords, if you're just doing it fully manually and you have like 10 hours to do one article, like what would you do?

**Jürgen Linde:** Like honestly, like to me, it's about, you know, phrasing the keyword differently.

**Jürgen Linde:** Like there's no step in the, in the workflow to my knowledge.

**Jürgen Linde:** form.

**Jürgen Linde:** Thank

**Jürgen Linde:** Where you can give it the keyword, like, in the topic or the article name.

**Jason Gong:** Let's stop thinking about the workflows.

**Jason Gong:** Just like, if you were writing one article and you wanted, like, the best set of keywords for the assignment brief, like, what would you do?

**Sydney Go:** Yeah.

**Sydney Go:** So what I would do is I would go through the primary keywords, go through the broad match keywords in SEMrush, right?

**Sydney Go:** Look at all the ones that actually seem relevant that aren't duplicates, have some duplicates in there, but not all of them.

**Sydney Go:** And then I'd go through the top 10 articles, see what topics they cover.

**Sydney Go:** Because those are just semantically related keywords.

**Jason Gong:** Like, I want to, like, change how it's done now.

**Jason Gong:** Because I think right now it's pretty, like, probably just a prompt with the root keyword.

**Sydney Go:** then, I mean, it doesn't matter.

**Jason Gong:** Maybe I call it.

**Jason Gong:** I don't know.

**Jason Gong:** Yeah.

**Jason Gong:** But I just want to see how you would do it.

**Sydney Go:** Oh, do you want me?

**Sydney Go:** I don't think I can run through it.

**Sydney Go:** But, like, the second step for me after, like, the broad match keywords would be identifying topics.

**Jason Gong:** Like, I want to see the screen in SEMrush.

**Jason Gong:** I want to see, like, what the keyword is.

**Jason Gong:** Like, let's just do it.

**Jason Gong:** Like, correct.

**Jason Gong:** One of these, like, let's take the keyword.

**Jason Gong:** Okay.

**Jason Gong:** What's this one?

**Jason Gong:** Okay.

**Jason Gong:** So this is the one that I'm doing, customer digital experience.

**Sydney Go:** Yeah, digital customer experience.

**Sydney Go:** Okay.

**Sydney Go:** Sorry.

**Sydney Go:** I may have changed it.

**Sydney Go:** Anyway, so what I would do is really quickly, if I'm going to do it manually, is I go here.

**Sydney Go:** Let's say you have 10 hours.

**Jason Gong:** Like, don't, don't think about, like, oh, I need to do this in five minutes.

**Jason Gong:** Like, everything you would do to do this 100%.

**Jason Gong:** Yeah.

**Sydney Go:** So, digital experience.

**Sydney Go:** I look at the questions, keyword variations, and, oh, 1,000.

**Jürgen Linde:** You can do that in perplexity when you give it a prompt.

**Jürgen Linde:** I mean, solutioning with LLMs.

**Sydney Go:** Okay.

**Sydney Go:** Think about how you use manually.

**Sydney Go:** Let the interview team in this.

**Jason Gong:** Okay, like, they can prompt an engineer to push together these APIs, but...

**Jason Gong:** So we can, like, let's just do it fully manually.

**Jason Gong:** Yeah.

**Sydney Go:** So I would add maybe 20 keywords from this broad match list into the list and then have those somewhere so I can put those into the article later.

**Sydney Go:** And then I'd go back to keyword overview, look at the questions that need to be answered and have those somewhere as well to make sure that I have sections to answer those specific questions.

**Sydney Go:** And then I'll open these, all of them, one by one.

**Sydney Go:** And then I'll have a list somewhere.

**Sydney Go:** And then even the people also ask, I might look at that as well.

**Jason Gong:** So that, like, very first step when you picked the broad match, like, what basis were you picking those?

**Jason Gong:** Because there were other ones that you didn't pick.

**Jason Gong:** Like, why'd you pick those?

**Sydney Go:** I look, oh, where is it?

**Sydney Go:** I look at the keyword difficulty and the keyword difficulty and search volume.

**Sydney Go:** So I didn't actually do it that first time, but keyword difficulty and search volume.

**Sydney Go:** when you generated.

**Sydney Go:** 1,640, that might be a good one.

**Sydney Go:** This is 1,030.

**Sydney Go:** And then some of the easier to rank for as well.

**Sydney Go:** So the keywords are the easier ones to rank for, but still good volume.

**Jason Gong:** How do you know they like, are you assuming all of these like kind of match the intent of the keyword?

**Sydney Go:** No, that would be, so that would be a later step.

**Sydney Go:** So I'm just compiling all the keywords that I want first.

**Sydney Go:** I would try to put myself.

**Jürgen Linde:** I would try to put myself.

**Jürgen Linde:** In the shoes of the ICP and say, like, if the ICP was defined well enough, I would be able to see, like, cool.

**Jürgen Linde:** This is the, like, the circle of my knowledge base.

**Jürgen Linde:** This is what I would not know.

**Jürgen Linde:** These are the keywords I would not understand.

**Jürgen Linde:** And then take that of, like, this is what I would also ask.

**Jürgen Linde:** Like, every time I read an article, like, that's a fact.

**Jürgen Linde:** Cool, that's a fact.

**Jürgen Linde:** But why?

**Jürgen Linde:** But what do I do with that?

**Jürgen Linde:** Yeah.

**Jürgen Linde:** Yeah.

**Jürgen Linde:** No.

**Jürgen Linde:** I guess it's based on intuition.

**Jürgen Linde:** It's hard to sort of automate in my mind.

**Jürgen Linde:** You have to vibe with it.

**Jürgen Linde:** I'm not sure how to automate that, I guess.

**Jason Gong:** Okay, so you're putting yourself in the ICP shoes, and then the questions you're asking yourself is like, this is a topic I'm researching.

**Jason Gong:** This is kind of my current knowledge level.

**Jason Gong:** And then that's You go from top to middle to bottom of the funnel.

**Jürgen Linde:** If it's top, you would not know what this complicated topic is.

**Jürgen Linde:** You should define it.

**Jürgen Linde:** Or if you're bottom of the funnel, you would know pretty much everything else.

**Jürgen Linde:** And then you draw the sort of...

**Jürgen Linde:** Like, I read an article, and I would read it as if I'm the reader.

**Jürgen Linde:** I'm like, cool, but why?

**Jürgen Linde:** But what?

**Jürgen Linde:** But what are you talking about?

**Jürgen Linde:** And you do that by funnel.

**Jason Gong:** Like, a concrete example would be like this.

**Jason Gong:** Like, let's say I was searching about how to run a customer...

**Jason Gong:** ...

**Jason Gong:** ...

**Jason Gong:** ...

**Jason Gong:** ...

**Jason Gong:** ...

**Jason Gong:** Digital experience, like interview, like you wouldn't care about what is customer digital experience because like presumably if you're that deep into whatever this journey is, you already know.

**Jürgen Linde:** I feel like if it's a definitional topic, you would care about the definition, not about the product, not about the technical stuff.

**Jürgen Linde:** You just want to know what it means.

**Jürgen Linde:** Therefore, would need like, you know, interlinking that shows you where to go to next if you do get it.

**Jürgen Linde:** But if you're problem with the funnel, you maybe want to look for like, okay, cool.

**Jürgen Linde:** This is how this is implemented.

**Jürgen Linde:** And I don't know.

**Jason Gong:** Yeah.

**Jason Gong:** Okay.

**Jason Gong:** So that's the lens.

**Jason Gong:** mean, do you like, is that what you would do, Sydney?

**Jason Gong:** Any kind of.

**Jason Gong:** That would be like later, later stuff for me for keyword research.

**Sydney Go:** Are you beginning with you?

**Sydney Go:** It's more about like.

**Sydney Go:** I would start with a list of keywords and then going through each of these articles one by one as well.

**Sydney Go:** And then identifying what the.

**Sydney Go:** Basically the semantically.

**Sydney Go:** Related topics are, so like for digital experience, whatever, core principles, that's one thing we maybe should look at, and then business context, customers, so bureau-based decisions, like those keywords would stand out to me, and then I'd put them all in a list as well.

**Sydney Go:** Digital experience versus customer experience, that might be something as well, so all of this would go into a list that I will later research one by one, and then identify from there what my sections would be, because we have keywords to target these, and so it's kind of like what Jürgen said, is putting yourself in this key, in the shoes of the searcher, because that's basically what Google does, it tries to identify what topics people are actually searching for, and that would be this step, like if these are the things that everyone else covers, users, then we should cover all of these things too, and that should be in your keyword research.

**Jürgen Linde:** It's kind of like when you search the core keyword on people also ask, that app, and then you get that flow chart of like, okay,

**Jürgen Linde:** Well, is the main keyword, and this is how it roaches off into related topics.

**Jürgen Linde:** If it seems relevant enough, you pull that into the main article, and they are not worthy of being their own articles, and it could be covered in the scope of the goal.

**Jürgen Linde:** Your microfilm is, like, off a lot.

**Jason Gong:** Oh, it might just be because you're touching it.

**Jason Gong:** Okay, cool.

**Jason Gong:** I think that makes sense.

**Jason Gong:** Yes.

**Jason Gong:** I guess maybe an added layer we can do now is, like, we can also check what prompts we care about, have this rough keyword space in it to see, like, what's being cited there.

**Jason Gong:** Maybe that can also be something you review to get, like, a sense of, like, hey, here's what the good articles that do well kind of talk about and how they cover it.

**Jürgen Linde:** Yeah.

**Jason Gong:** Sorry, go ahead.

**Jürgen Linde:** Nah, like, if I were to do this, like, you know, just our usual...

**Jürgen Linde:** If you actually would have done it in the past, I would say, here's a keyword, who do you assume would care about this keyword?

**Jürgen Linde:** What do you think the questions would naturally come up in their minds if you were to explain this as of their five?

**Jason Gong:** Right, right.

**Jason Gong:** I mean, honestly, I think LMs would be amazing at this, right?

**Jason Gong:** Like, you tell it, hey, you're this, and then you ask your questions.

**Jason Gong:** Like, I just don't think we can pick keywords right now if it's doing that at all.

**Jason Gong:** But that's why I'm trying to, like, bring us through this exercise.

**Jason Gong:** Okay, so you do that, you have the keywords, have the article references, you have kind of, like, thinking around user journeys and ICP and their mindset.

**Jason Gong:** And then, based on that, like, how are you filtering the keywords down at this point?

**Jason Gong:** And I guess based on this, you probably also have ideas on what the content structure should be.

**Jason Gong:** So how do you do, like, how do you do this last part?

**Jason Gong:** Take all that and actually make something like an assignment brief.

**Jason Gong:** Yeah.

**Jürgen Linde:** It's almost better if you are brand new to the client industry, because then you think like the reader.

**Jürgen Linde:** You think about like, okay, cool.

**Jürgen Linde:** I don't know what we're talking about here.

**Jürgen Linde:** Therefore, I should know about it.

**Jürgen Linde:** What should I learn?

**Jürgen Linde:** And then you branch from there as if you're the reader, and that's kind of guiding you.

**Jürgen Linde:** If you know too much about the industry, then it's hard to empathize with the reader at the top of the funnel.

**Jürgen Linde:** Yeah, that makes sense.

**Jason Gong:** I mean, okay, so let's do keywords and propose content structure separately.

**Jason Gong:** like keywords, like what are the problems you guys generally see right now for the keywords that get picked?

**Jason Gong:** That there's not enough.

**Sydney Go:** For the keywords, there's not enough.

**Sydney Go:** They're two, they're just variations of the target keyword basically, which is great, but also they're not super useful.

**Sydney Go:** And it doesn't steer the article enough.

**Sydney Go:** It's almost like you couldn't use like.

**Jürgen Linde:** FAQ section to supplement your core keyword, and integrate that with the rest of the article.

**Jürgen Linde:** Got it.

**Jürgen Linde:** then, that's part of the keywords.

**Jason Gong:** And then one of the things you said earlier was, like, the keywords themselves, like the ones that are, like, the way it's kind of weaved in is too keyword stuffing-like, and not trying to, like, actually integrate it into the structure of the article.

**Sydney Go:** It's like you should have a step or, yeah.

**Jürgen Linde:** It's like as if you should have an extra step in the workflow where it's like, okay, cool, here's the core keyword.

**Jürgen Linde:** Like, how else would someone naturally use this or ask about this and then add that into, like, your keyword strategy to integrate it more naturally into the rest of the article?

**Jürgen Linde:** I mean, in this case, like, because we have digital customer experience, right?

**Jason Gong:** Okay.

**Jason Gong:** And one of the keywords is...

**Jason Gong:** Digital custom experience solutions.

**Jürgen Linde:** Because that's like just variations on how people would discover the topic, but not necessarily how they would think about the topic, if that makes sense.

**Jürgen Linde:** Okay, so that one didn't appear.

**Jason Gong:** I guess we should just run this just to see how it's throwing it in there.

**Jason Gong:** Okay, so that one, let's see what the article jumps out.

**Jason Gong:** And then as far as the proposed content structure, how would you guys come up with that?

**Jason Gong:** Like now that you have the articles that do well, that are like reference articles, you have the keywords, you have all this thinking around customer persona.

**Jürgen Linde:** To me, that's all dependent on how well you know what the target route as context is.

**Jürgen Linde:** So maybe there needs to be an extra, like in your ICPs, there should be maybe like an extra gap or like an extra section where...

**Jürgen Linde:** This is what they definitely do not know and that can maybe inform how you steer the article to like make more relevant sections instead of like the templates of the sections like, okay, if you like know what they don't know, that can help steer it into knowing what sections to add or remove like it.

**Jürgen Linde:** I don't know.

**Jürgen Linde:** Does it help?

**Jürgen Linde:** it help?

**Jason Gong:** So you have like, I mean, I think that's one framework, I guess you have like an outcome for the article and then you're kind of trying to like piece together what's missing in the person's head and why they're here and then maybe let that steer towards the...

**Jason Gong:** help with the interlinking strategy.

**Jürgen Linde:** Like instead of just like if you're a top of the funnel customer and you do the interlinking stage, it always directs you to the demo, whatever.

**Jürgen Linde:** People don't care about that.

**Jürgen Linde:** They want to learn more and go to the...

**Jason Gong:** How would you use the reference articles to guide that?

**Jason Gong:** Because I think what you're describing is the very first principles, but I think it'd be very hard.

**Jason Gong:** We need concrete steps to do that.

**Jürgen Linde:** Is it 20 sections or 50?

**Jason Gong:** You know, like, like, how would you use all this stuff you've collected now to, like, create a good outline?

**Jürgen Linde:** I guess.

**Jason Gong:** Like, how would you do it, Sydney?

**Jason Gong:** Like, how would you even decide what H2s to have?

**Sydney Go:** I would do that based on the existing ranking articles.

**Sydney Go:** Or, honestly, now that we have LLMs and we're going for LLM citations, ask it, what people are actually asking, and then weave the keywords in through there because those will usually align.

**Sydney Go:** The sections that you have, the important topics to cover, those should be, like, the best.

**Sydney Go:** to be one of the first few steps.

**Sydney Go:** What are the important topics to cover?

**Sydney Go:** And then, you know, get keywords from there, as well as like the overall topic, because, yeah, like what Jürgen was saying, it's, you have to know what it doesn't go on.

**Jürgen Linde:** If you have like a brand new reader, they're going to want to know what the acronyms and jargon mean.

**Jürgen Linde:** If a bottle or funnel one, they will know exactly what you're talking about.

**Jürgen Linde:** So you don't want to come across as this kind of same thing.

**Jürgen Linde:** And at the other end, you want to be more informative and helpful.

**Jason Gong:** Okay, so you're, I guess, I'm just trying to break this down into something we can actually make a workflow around.

**Sydney Go:** So it's like.

**Sydney Go:** So, um, let's see for this digital experiences platform, right?

**Sydney Go:** So what I would first do is look through all the keywords and then look for the variations of the keyword and then side by side with that, look for the topics to cover.

**Sydney Go:** That would be the first step.

**Sydney Go:** Go through all the articles, topics to cover.

**Sydney Go:** From each topic to cover that I have now identified.

**Sydney Go:** Um.

**Sydney Go:** That I've verified is important for the article and for the ICP.

**Sydney Go:** I would then do keyword research on each of those topics, but like lighter touches that are still related to your main topic keyword.

**Sydney Go:** So this would be like your pillar page or whatever, and that you can later link out to other articles.

**Sydney Go:** So it's instead of taking it as one whole article and it's just keyword research for this whole thing, it's breaking it down into the sections and then doing keyword research for those sections, because those are the important topics to cover and what people are actually looking for.

**Sydney Go:** And then from there, you've got this whole cohesive assignment brief that has your target keyword, your main target keywords, and then your secondary keywords are semantically related, but not just variations of your target keyword.

**Sydney Go:** Does that make sense?

**Sydney Go:** Yeah.

**Jason Gong:** So you have a bunch of keywords, a bunch of topics.

**Jason Gong:** And then how are you filtering down all those topics into something cohesive that actually becomes an article?

**Jason Gong:** Like presumably you don't use.

**Jason Gong:** All the topics right so how do you decide there?

**Jason Gong:** That's where your target market comes in.

**Sydney Go:** If it's irrelevant to them then you probably don't need it but it comes back down like to understanding your ICPs what they don't know.

**Jürgen Linde:** If it's going too in-depth then it's like going beyond the scope of their search and taint and they might as well be secondary articles that you can help into linking and you know you're brand new you're like learning about the stuff and like oh I don't know what that means second article maybe that goes to you know more bottom of the bottom it's kind of like a cascading effect as long as you understand your ICPs.

**Jason Gong:** Like do you do you factor in at all like you know hey when you search digital customer experiences and there's the one article and you see like that same article ranks for like a couple other keywords like does that matter for you at all with us?

**Jason Gong:** you

**Jason Gong:** Your keywords are or not, really?

**Sydney Go:** Sometimes it does.

**Sydney Go:** Most of the times, though, I see that the other keywords are either weirdly related, tangentially related, or they're ranking for it because they have a cluster page that targets that specific keyword that the pillar page links out to.

**Sydney Go:** Then it may be relevant, but not super relevant for that article.

**Sydney Go:** So also branded keywords.

**Sydney Go:** Sometimes it doesn't make sense, but a lot of the times it's just variations on that keyword.

**Sydney Go:** That's good.

**Sydney Go:** Going back to your original question, though, I don't think so.

**Sydney Go:** If you do, if you look at the top ranking articles and then pick your topics from there, generally you shouldn't go beyond the scope.

**Sydney Go:** But someone still needs to go in and check that, you know, all the articles are, all the sections are indeed not beyond the scope.

**Jason Gong:** Okay, that makes sense.

**Jason Gong:** That's, I'm sure those practices are replicated.

**Jürgen Linde:** don't

**Jason Gong:** Maybe later in the week to go through the rest of this.

**Jason Gong:** Or if you guys want to keep spending more time here, that would be helpful.

**Jason Gong:** But just, I mean, in this case, right, we have this as like a secondary keyword.

**Jason Gong:** I guess if I read the...

**Jürgen Linde:** Like the keyword itself is definitional, but that H3 or H4 is more of like a second article.

**Jürgen Linde:** Like how to improve customer experience, that's like its own thing.

**Jürgen Linde:** But if you're just looking at customer experience, then you're like...

**Jürgen Linde:** Right.

**Jürgen Linde:** So then I guess in this case, like how should this part of it?

**Jason Gong:** Like do you think this keyword just should just not have been in here?

**Jürgen Linde:** It could be sectioned off as like a recommendation for a second article or not.

**Jürgen Linde:** I don't know, like it could be a CTA if you have an existing article or it should be like an escape hatch where it's always going be like, Hey, don't include this, but it's a good opportunity to make a second article.

**Jürgen Linde:** I'm not sure if that's feasible, but that's how I would think.

**Jürgen Linde:** Got it.

**Sydney Go:** Three of the top five ranking articles do cover how-to, so that would have to be in the article.

**Sydney Go:** Okay.

**Jason Gong:** I feel like we should separate keywords from proposed content structures, just be like a different step or something.

**Sydney Go:** Because, like, right now- Usually when you manually create it, that is the first- Sorry, go.

**Sydney Go:** Okay, so you're saying if you manually do it, you would separate assignment brief from keyword research?

**Jason Gong:** Yeah, okay.

**Jason Gong:** I mean, it's probably a separate step in the workflow, but I guess I don't know how that works.

**Jason Gong:** But, like, in this case, it's like- Okay, so, like, presumably this is an important topic, but the way, I guess, this proposed content structure was done, like, it's not It goes the same route as when you generate the first draft.

**Jürgen Linde:** It goes, like, by 4,000

**Jürgen Linde:** Some words, but you only need like 1,500, but the brief goes like also too much in depth, but you could actually cover far less in order to rank.

**Jürgen Linde:** We also, like, you know, top ranking pages organically will probably just have like 500 words and they are like in the top three, so.

**Jason Gong:** Right, so there's also like word count that we're like not.

**Jürgen Linde:** Yeah, word count means a lot, like, but at the same time, that's, you know, it's going to be removing feedback stuff, feedback column, but I guess that needs to be like.

**Jason Gong:** I think you're, if you can kind of, because I feel like you have a pretty good grasp of like what we need to do here in this discussion, like if you can take this and the video recording and just kind of like.

**Jason Gong:** Can you send me a link to this notion page?

**Jason Gong:** Yeah, you should get me a notification.

**Jason Gong:** If you can do a pass at trying to document all the things we want to change.

**Jason Gong:** And I think linking it back to timestamps of the video is pretty critical.

**Jason Gong:** Yeah, I can go there.

**Jason Gong:** Hearing the keyword thing, I really want to link it to whatever we just talked about for the last 15 minutes.

**Jason Gong:** And then we can work together to file a bunch of tickets maybe tomorrow or something.

**Jason Gong:** I I think I've wanted to improve assignment brief for a really long time, but it's just not happening.

**Jason Gong:** So I need, like, we need to, like.

**Jürgen Linde:** Yeah, like, if Panzer says you should be spending 80% of your time on the assignment brief, that means it's something true.

**Jürgen Linde:** It's totally fair.

**Jason Gong:** I mean, as the human part, but, like, also, I mean, engineers should be spending their time on that, too.

**Jason Gong:** So, like, I think all the stuff we talked about seems sensible to me.

**Jason Gong:** I think I just want to, like, document it somewhere.

**Jason Gong:** Okay, cool.

**Jason Gong:** You got to hop.

**Jason Gong:** But yeah, if you could do that, then maybe you can find some time tomorrow to chat through that, and we can include Sydney as optional if you have time, Sydney.

**Jason Gong:** But overall, mean, at least it works.

**Jason Gong:** nothing's broken.

**Jason Gong:** It's just, like, a little bit more cumbersome.

**Sydney Go:** I think ours is working on the call earlier.

**Sydney Go:** Jess was saying her outline stuff wasn't working.

**Sydney Go:** Like, it wasn't generating an outline.

**Sydney Go:** Like, oh, thank God, that's not happening in our group.

**Jason Gong:** I mean, I would say, like, I think it's, like, not visible at all.

**Jason Gong:** But, like, if something is broken with this, I would assume it's, like, something here.

**Jason Gong:** Where, like, you're not referencing an artifact.

**Jason Gong:** You you set the wrong name for an artifact so it's not getting fed in.

**Jason Gong:** Or, you know, I mean, this topic thing.

**Jason Gong:** This part still confuses me a little bit.

**Jason Gong:** I guess your only way to steer what's even being written is this, right?

**Jason Gong:** So, like, I think you should almost, like...

**Jason Gong:** Write the title a little bit differently.

**Sydney Go:** The assignment direction, I think Carol has responded to your question.

**Sydney Go:** Apparently, can steer if we want it to be a how-to article or a listicle or something using assignment direction as well.

**Jason Gong:** Okay, I mean, we should, I guess I'll read it.

**Jason Gong:** Okay, I'm going to hop, but yeah, I mean, Sydney, I know you have a lot as well, so let me know if there's anything I help with.

**Jason Gong:** I actually have a pretty free afternoon, and we're trying to hand off two of our clients, and still on the hook for a bunch of articles.

**Jason Gong:** I know there's a lot of strategy.

**Jason Gong:** If Jürgen can support, please let him know.

**Jason Gong:** Yeah.

**Jason Gong:** Yeah, we're going to meet after this.

**Jürgen Linde:** Cool.

**Jason Gong:** Yeah.

**Jason Gong:** All right, I got a hot bell.

**Jason Gong:** I'll see you guys later.

**Sydney Go:** Cool.

**Sydney Go:** Okay, thanks, Jason.

**Sydney Go:** Hope to see you tomorrow.

**Jürgen Linde:** Bye.

**Jürgen Linde:** Do you want to stay here?

**Jürgen Linde:** Oh.

**Sydney Go:** Bye.
