# Yourco Handoff Sync

<metadata>
date: 2026-01-09
time: 17:03 UTC
duration: 89 minutes
organizer: ademilade@growthx.ai
participants: Matthew Panzarino (GrowthX), Pamela Weber (GrowthX), Ademilade Shodipe-dosunmu (GrowthX)
fathom_recording_id: 113138404
fathom_url: https://fathom.video/calls/528167993
share_url: https://fathom.video/share/_HzkcFn7fL3hoKTs5_8-7jM-kxyyJ1nW
source: fathom
enriched_on: 2026-02-28T00:00:00Z
</metadata>

---

## Summary

Matthew led a handoff sync to prepare Pamela to manage the Yourco and Discern accounts. Key decisions: Yourco will immediately adopt the agentic pipeline in the test workspace, with Pamela handling articles and automating post-processing; Discern's article-format issues stem from using the wrong PSEO pipeline per cluster, requiring new templates and samples for each, plus automated EPD fixes to reduce manual effort.

---

## Context

This meeting occurred on 2026-01-09 as the first formal handoff sync between Matthew (account strategy lead), Ademilade (production lead), and Pamela (incoming producer). Pamela is taking over two active client accounts: Yourco (6 articles/week) and Discern (26 articles/week), representing a significant increase in production volume and complexity. Matthew outlined strategic pipeline choices and operational workflows to ensure smooth knowledge transfer and alignment on automation priorities across both accounts.

The underlying tension: Yourco has an established but older pipeline, while Discern faces systematic article-format issues that cascade from pipeline misconfiguration. Both accounts require immediate attention to workflows, staging automation, and quality controls.

---

## Relevance

- **Operational handoff:** Documents the decision and rationale for pipeline choice (agentic vs. legacy) and sets expectation-setting for Pamela's first month
- **Process improvement:** Identifies specific automation gaps (Discern EPD, Yourco Prismic staging) and assigns ownership for fixes
- **Product roadmap:** Reveals need for cluster-specific PSEO templates as a systematic solution for Discern's quality issues
- **Team scaling:** Shows how GrowthX is expanding production capacity and the workflows needed to support multi-account producers
- **Risk mitigation:** Flagged image-matching issues and article-format problems, establishing baseline quality checks

---

## Overview

- **Yourco:** Immediately adopt the agentic pipeline in the `test` workspace. Pamela will run next week's articles, log all post-processing, and file weekly tickets to automate the most time-consuming tasks.
- **Discern:** The core issue of articles being "shoehorned" into the wrong format is due to using the wrong PSEO pipeline for a given topic cluster. The solution is creating a new, specific pipeline for each cluster.
- **Discern:** To accelerate the manual pipeline, Ademilade will request an EPD fix to automate all steps except the final publish. This will serve as a model for future pipeline improvements.
- **Discern:** Staging is a manual process managed via a recurring Linear ticket assigned to Suleiman. Pamela will move articles to `Ready for Staging`, add a `new article` tag, and notify Suleiman in the weekly thread.

---

## Key Topics

### Discern: PSEO Pipeline Strategy

  - **Problem:** Articles are being "shoehorned" into the wrong format (e.g., a general listicle forced into a competitor-alternative structure).
  - **Cause:** Using the wrong PSEO pipeline for a given topic cluster. Each cluster requires a specific pipeline to generate the correct structure.
  - **Solution:** Create a new PSEO pipeline for each new topic cluster.
      - **Process:**
        1.  **Create Artifacts:** A `Template` (Rule) and a `Sample Article` (Other) are required.
        2.  **Generate Template:** Use Claude to create a template based on SERP research and the cluster's specific article type.
        3.  **Create Sample:** Write a high-quality sample article that adheres to the template.
        4.  **Build Pipeline:** Copy an existing PSEO pipeline and use find-and-replace to update all references to the old template and sample with the new ones.
  - **Action:** Pamela will file Linear tickets for new pipelines, providing the template and sample artifacts.

### Discern: Workflow & Staging

  - **Goal:** Automate the manual pipeline to improve efficiency.
  - **Problem:** The current pipeline requires manual triggering of each step, which is slow.
  - **Action:** Ademilade will request an EPD fix to automate all steps except the final publish.
  - **Staging Process:**
      - Move approved articles to `Ready for Staging` in Linear.
      - Add a `new article` tag to the card.
      - Notify Suleiman in the weekly Linear ticket thread.
      - Post a link to the ticket in the internal Slack channel for visibility.

### Yourco: Pipeline & Staging

  - **Pipeline:** Immediately adopt the agentic pipeline in the `test` workspace.
  - **Rationale:** This aligns with the engine team's focus and provides a clear baseline for improvement.
  - **Action:** Pamela will run next week's articles, log all post-processing, and file weekly tickets to automate the most time-consuming tasks.
  - **Staging Process:**
      - A manual process in Prismic, taking \~7-15 minutes per article.
      - **Action:** Ademilade will find the old ticket or file a new one to automate this process.

### Handoff Logistics & Deadlines

  - **Yourco:**
      - **Deadline:** Deliver content by Wednesday for the following week's publication.
      - **Workflow:** Move articles to `Client Review`, then notify Carrie.
  - **Discern:**
      - **Deadline:** Deliver content by Friday for the current week's publication.
      - **Workflow:** Move articles to `Ready for Staging`, then notify Suleiman.
  - **Workload:**
      - **Yourco:** 6 articles/week.
      - **Discern:** 26 articles/week.
  - **Support:**
      - **Yourco:** Kari is the primary contact for account-specific questions.
      - **Discern:** Vivek is the contact for client priorities.

---

## Action Items

**Pamela Weber (GrowthX)**
- Run next week's Yourco articles in agentic pipeline; compile weekly post-processing list; file weekly CEPD tickets
- Watch Yourco staging/Looker Looms; stage Yourco Thursday; run Looker Monday
- Finish 13 Discern articles for next week; move to Ready for Staging; notify Suleiman; tag New/Refresh
- Fix Discern image mismatch (e.g., 'Best CSE alternatives'); ensure images match title/topic
- Send first Private Equity Fund Formation article to Vivek (Discern) for feedback
- Create CEPD tickets for 'Best Registered Agent Services' + 'Discern vs' pipelines; attach templates/samples
- Finish remaining 3 Yourco articles in agentic; send to Carrie (Yourco); move to Client Review; notify Carrie

**Ademilade Shodipe-dosunmu (GrowthX)**
- Post in EPD help re: Discern publishing: auto all steps except manual publish; tag Megika; share pipeline link
- Check with Carrie (Yourco) re: Yourco Prismic API publishing ticket; update/file new; send to Matthew
- Review 1–2 Discern PSEO units per cluster; send feedback to Pamela
- Send Discern cluster breakdown doc + CEPD pipeline request link to Pamela via Slack
- Update enriched Yourco article to LDR format

---

## Transcript

**Pamela Weber:** And I have like three articles left on your code to do, but I want to see what he wants for us for the agent.

**Pamela Weber:** Sorry.

**Matthew Panzarino:** Hello, hello.

**Matthew Panzarino:** Hey, How's it going?

**Pamela Weber:** Hey there.

**Pamela Weber:** How are you?

**Pamela Weber:** How's it going?

**Matthew Panzarino:** Good, good.

**Matthew Panzarino:** Sorry, one second.

**Matthew Panzarino:** Right.

**Matthew Panzarino:** Okay, cool.

**Matthew Panzarino:** So, Ademilade, was talking with family yesterday.

**Matthew Panzarino:** We were catching up, and I didn't know you guys hadn't done your first sync yet to like do a handoff.

**Matthew Panzarino:** So,

**Matthew Panzarino:** Um, so like, I don't want to get in the way too much of, you know, some of that that you're going to do naturally.

**Matthew Panzarino:** Um, I just wanted to kind of highlight a handful of things that, um, would be important for Pamela, you know, obviously to be successful and going forward.

**Matthew Panzarino:** Let me blur my background, my messy office.

**Matthew Panzarino:** I don't use Google Beats.

**Pamela Weber:** That's the best part of the call to like, see what's going on behind you.

**Pamela Weber:** Yeah, yeah, exactly.

**Pamela Weber:** All my collectibles.

**Pamela Weber:** I'm leaving me, block it.

**Matthew Panzarino:** It's all my son's collectibles.

**Matthew Panzarino:** Um, anyhow, so long story short, we were talking about your code specifically yesterday.

**Matthew Panzarino:** Um, although I'm sure this applies to, you any account that she's going to take over, but, um, I know that you had the original, like, non, the, the deterministic pipeline, the older pipeline kind of set up pretty well for you.

**Matthew Panzarino:** Um, I think it's probably most productive though, for her to just go right into the agentic pipeline.

**Matthew Panzarino:** Um, then if we need to like file any improvements or any updates, um, for that pipeline to get it performant, let's just do it right off the rip.

**Matthew Panzarino:** Um, because using the older pipeline, I think it's probably counterproductive, not because it's not effective for you because you've been like in it and you know the system, but because Pamela is brand new to it.

**Matthew Panzarino:** So we need to get her read in on the agentic pipelines and using those.

**Matthew Panzarino:** Um, it also means that like, if she's going to file tickets or, you know, need any improvements to the client, makes any changes or anything like going forward.

**Matthew Panzarino:** If she files a ticket, they're like, Hey, what is this old, why are you using this old pipeline?

**Matthew Panzarino:** Instead?

**Matthew Panzarino:** It's like, Oh yeah, the agentic pipeline where that's what the inch team is focused on.

**Matthew Panzarino:** So it's good on all counts.

**Matthew Panzarino:** Um, that was my basic take there.

**Matthew Panzarino:** You, it sounds reasonable, right?

**Matthew Panzarino:** Yeah.

**Ademilade Shodipe-dosunmu:** Okay, cool.

**Matthew Panzarino:** Um, yeah, I would say like, just talk us through, um, let's start with your code and just talk through a little bit.

**Matthew Panzarino:** Um, what's the current state of the pipeline there?

**Matthew Panzarino:** And, and, um, you know, what, what kind of like, I know you've built your hand off doc, which is great.

**Matthew Panzarino:** Um, I think.

**Matthew Panzarino:** Kind of made a couple of tweaks in there just to prioritize that agentic pipeline.

**Matthew Panzarino:** And I noticed you kind of recommended use the one in the test workspace.

**Matthew Panzarino:** Is that kind of the latest one you were tweaking?

**Ademilade Shodipe-dosunmu:** Yeah, so Jill was tweaking that one.

**Ademilade Shodipe-dosunmu:** I've been getting some good results.

**Ademilade Shodipe-dosunmu:** So that's the one he advised to use.

**Ademilade Shodipe-dosunmu:** I haven't had so much time to get testing done on it.

**Ademilade Shodipe-dosunmu:** So I wasn't like, that's why when she came on, my privacy was pretty much like, okay, just start with this pipeline that at least I know what's going on here.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** I understand what's going on in the account first.

**Ademilade Shodipe-dosunmu:** Then we moved to agentic.

**Ademilade Shodipe-dosunmu:** So I think she's probably gotten a decent hand on that.

**Ademilade Shodipe-dosunmu:** And she can probably explore agentic.

**Ademilade Shodipe-dosunmu:** The idea now is that because now she has a quality bar now, in terms of examples, and even people from the client, and so she has like a quality bar, knows exactly what ASCO should look like.

**Ademilade Shodipe-dosunmu:** it's easier for her to jump into a genetic now and pretty much say, okay, hey, this is all wrong, this is all wrong, I need to do post-processing here.

**Ademilade Shodipe-dosunmu:** Then after she does that for a week or two, she can just itemize all her post-processing and, like, find a ticket to engine.

**Matthew Panzarino:** Okay, cool.

**Matthew Panzarino:** that's, like, my thing here.

**Ademilade Shodipe-dosunmu:** Yeah, I think that's probably the best way to go.

**Matthew Panzarino:** So, like, let's, I think what I'm going to do, I just want to get the lay of the land before I made any major changes or, like, messed around in there.

**Matthew Panzarino:** But I think what I'm going to do is just move that pipeline from the test workspace to the standard workspace just to, like, and I'll archive the other one that was in there.

**Matthew Panzarino:** And we'll just start with that, you know, as, like, our baseline.

**Matthew Panzarino:** And then the best thing for you to do, Pamela, is probably to run next week's articles in the Agentec pipeline and just let it rip and see what you get.

**Matthew Panzarino:** But I would estimate that whatever you're going to get is probably not going to involve

**Matthew Panzarino:** More post-processing than you're already doing from the deterministic pipeline.

**Pamela Weber:** way.

**Pamela Weber:** Yeah, yeah.

**Pamela Weber:** A long time I can, yeah.

**Matthew Panzarino:** Yeah, baseline it'll be the same, which hopefully it'll be better.

**Matthew Panzarino:** And then once you do your next batch of pieces from there, then immediately look at your post-processing and say, okay, let me file a ticket on this and see which of these items we can internalize to the workflow.

**Matthew Panzarino:** And then as we talked about on the call, just do that every week.

**Matthew Panzarino:** Like basically every week go like, what, which of these post-processing things, maybe it's, maybe it's just one.

**Matthew Panzarino:** Maybe it's one, your most egregious one or longest.

**Matthew Panzarino:** But by that, I mean, the thing that takes you the longest, right?

**Matthew Panzarino:** But there could also be low-hanging fruit opportunities, but you can file a ticket on those.

**Matthew Panzarino:** The Client Ops Eng team just had a couple of more people on board, so they've got more resources.

**Matthew Panzarino:** They're aggressively tackling these items that will help us to build leverage across all the pots.

**Matthew Panzarino:** So your best bet is to, like, get some...

**Matthew Panzarino:** Reps in the tank on the agentic pipeline.

**Matthew Panzarino:** It's very similar to run, fortunately.

**Matthew Panzarino:** It's just drop the title in and some basic instructions and go.

**Matthew Panzarino:** I think your other account has an agentic pipeline that you're already using, so it's the same.

**Matthew Panzarino:** I would say let's get some reps in the tank on the next batch of content that you have due for your code, and then we can file an immediate ticket.

**Matthew Panzarino:** I can help, Nana can help, like, because you're new, you know, filing your first ticket or doing your first round of improvements.

**Matthew Panzarino:** We can jump in there.

**Matthew Panzarino:** Ara, you'll be busy, so it's not like you need to be, but if we need to consult you, we will.

**Matthew Panzarino:** But I think it's, that's probably the best path forward, I think.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** And, like, this actually is, like, the first proper handover meeting.

**Ademilade Shodipe-dosunmu:** we had, like, two others, like, in December.

**Ademilade Shodipe-dosunmu:** But, like, since January, we've not been able to meet, like, virtually because of, like, time zone.

**Ademilade Shodipe-dosunmu:** to to meet.

**Ademilade Shodipe-dosunmu:** Thank you.

**Ademilade Shodipe-dosunmu:** Just how busy everything has been, but I've just been sending a ton of rooms, because I figured that's better, because she has actual video evidence of how to do some stuff, so I've been really putting a ton of rooms, so I think I sent her every single room she needs for Yurko, so from Updating Looker to Staging, there was already a staging video, but it was a bit short, and I think it's easier for someone who has staged before to understand that one, so I just prepared a way longer one, that was like a step-by-step guide, and how to do everything in staging, and she should be fine for Yurko, and like Kairi is like super helpful, I know like Kairi would always like, you know, jump in if you know, she needs help, so I think, regarding like the state of like the Yurko Al-Khapet spirit, she was supposed to, I think, take over full production this week, for Monday, but I decided to give like one week, or on a way, so I worked on this week's articles, and I staged them.

**Ademilade Shodipe-dosunmu:** Okay, thank you.

**Ademilade Shodipe-dosunmu:** All of that, just to give like some more distance.

**Ademilade Shodipe-dosunmu:** So for next week, she's owning that.

**Ademilade Shodipe-dosunmu:** I was a bit worried about capacity because this has been crazy for me.

**Ademilade Shodipe-dosunmu:** Yeah, I bet.

**Ademilade Shodipe-dosunmu:** I'm happy that Timmy jumped in for diligence because that's been helping.

**Ademilade Shodipe-dosunmu:** Because now I'm having to edit those, then discern as well for the week of 26.

**Ademilade Shodipe-dosunmu:** PSU is a pain sometimes, you know.

**Ademilade Shodipe-dosunmu:** And also, obviously, with strategy sprint stuff.

**Ademilade Shodipe-dosunmu:** So I wanted to find out and also flag how would, like, sort of capacity planning for next week.

**Ademilade Shodipe-dosunmu:** And I wanted to do a recall as well, with Pamela here.

**Ademilade Shodipe-dosunmu:** know, like, I'm, you know, correct me if I'm assuming, but I know that you're pretty, probably a bit comfortable or a bit more comfortable a year ago now.

**Ademilade Shodipe-dosunmu:** But I don't know how you're feeling about diligent production.

**Ademilade Shodipe-dosunmu:** Sorry, not diligent, rather discern.

**Ademilade Shodipe-dosunmu:** We'll get to diligence in a minute.

**Ademilade Shodipe-dosunmu:** But, like, discern production, how are you feeling about taking that on next week?

**Pamela Weber:** Well, lot better arrangement.

**Pamela Weber:** I finished all my discernment for the week.

**Pamela Weber:** I'll see your feedback.

**Pamela Weber:** Hopefully, there's not much more I need to do with those.

**Pamela Weber:** The only thing is it was slow when you turn off the automatic thing.

**Pamela Weber:** have to do every step.

**Pamela Weber:** was wondering if there's a way to make that faster without it being on and go boom, boom, boom, but then it goes to publish, which I don't want.

**Pamela Weber:** So is there something I'm missing in how to make it quicker because I have to do every single step until I have to go the next one, and that's slowing it down.

**Pamela Weber:** Is there, like, a better way to do it?

**Ademilade Shodipe-dosunmu:** I think what I'll do is I would probably find a way to temporarily turn off the automated publishing until they fix it.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** So this way you can just run it all the way to the end.

**Ademilade Shodipe-dosunmu:** So for context, Pamela, the issue was that, like, she was running it all the way and automated publishing was on, so it was just creating drafts and workflow.

**Ademilade Shodipe-dosunmu:** So every single time I have to go in, I don't need to do those, so I think I'm just going to disconnect temporarily the workflow publishing.

**Ademilade Shodipe-dosunmu:** Yeah, I mean, I think that's like an eng ask.

**Matthew Panzarino:** mean...

**Matthew Panzarino:** That that's a ticket that we can just file or frankly it should be a few minutes fixed so maybe just an EPD help channel just ask if they can make all of the steps automated except for the last one like there should be no reason why it can't automatically run all of the steps and then stop before them and make the publishing one manually only right like that's that's definitely possible so let's let's ask them to do that because that's how it should work.

**Matthew Panzarino:** You should be able to run the entire pipeline and then once you've edited and saved your output then hit play and then boom it publishes.

**Matthew Panzarino:** That's my vision for how all of the publishing will work so let's make this our you know example and then we can point to it and say hey if you want this to work properly here's how this account does it and let's make all of them do that.

**Matthew Panzarino:** So I think that's that's the best thing let's start with the EPD help channel and just say hey we've got this pipeline point to the pipeline I would love for the last step to be if you could wouldn't mind taking the lead on that.

**Matthew Panzarino:** All right.

**Matthew Panzarino:** Just because you're familiar with exactly what's going on with that publishing step and say, hey, can we make this publishing step manual and the rest of it automatic or, you know, proceed in an automated fashion.

**Matthew Panzarino:** I think that's probably the best way to go forward here.

**Matthew Panzarino:** I see what the issue is, but I also don't want to, like, hack something that really should just be, it should just work the logic away, you know.

**Pamela Weber:** Yeah, when I ran some of the Yorko, that agentic pipeline last night, the articles were so quickly done versus when I went to do the discern last night, and it was, like, just the time before I get the content, I get to it.

**Pamela Weber:** So, yeah, so that'd be a big help.

**Matthew Panzarino:** Yeah, and then you have to remember, like, oh, I got to trigger the next step, you know.

**Matthew Panzarino:** And I don't publish something, I think on New Year's Eve, it's like, at hopefully nobody's around on seeing that.

**Pamela Weber:** So, yeah, it was really good.

**Pamela Weber:** yeah.

**Pamela Weber:** Okay, yeah.

**Pamela Weber:** And then the other thing, I think this is what you were asking that day about for next week, like, am I taking over staging and production?

**Pamela Weber:** I have no idea what those are yet.

**Pamela Weber:** I didn't get those videos.

**Pamela Weber:** I just wanted to get all the content to you this morning, which I did, except the last three.

**Pamela Weber:** Because now I know which pipeline to do, so I'll do that right after this.

**Pamela Weber:** So I don't know what does evolve or everything, but is that something you me to take over next week?

**Pamela Weber:** Or like I started, or what are we doing with that part?

**Ademilade Shodipe-dosunmu:** So details are in the video, so you can check the Loom.

**Ademilade Shodipe-dosunmu:** Everything is now about Yorco's staging.

**Ademilade Shodipe-dosunmu:** We don't publish for Yorco, we stage.

**Ademilade Shodipe-dosunmu:** They only give us Prismic access to stage, so our POC publishes.

**Ademilade Shodipe-dosunmu:** But we stage it in Prismic, because it's really annoying process.

**Ademilade Shodipe-dosunmu:** That's what I recorded in Loom.

**Ademilade Shodipe-dosunmu:** But once you get used to it, takes like...

**Ademilade Shodipe-dosunmu:** I think Joe estimated like it takes 10 to 15 minutes to stage in Prismic.

**Ademilade Shodipe-dosunmu:** I currently do it in like 7 minutes, so yeah.

**Ademilade Shodipe-dosunmu:** For all the articles?

**Pamela Weber:** Oh, it's only 5, okay.

**Ademilade Shodipe-dosunmu:** No, for each one.

**Ademilade Shodipe-dosunmu:** Oh, okay, okay.

**Matthew Panzarino:** The Prismic staging we don't have an automation for yet, right?

**Pamela Weber:** Yeah, don't.

**Ademilade Shodipe-dosunmu:** I think Bertrand said it was like a pain to do because the way the template is, is different for each account.

**Ademilade Shodipe-dosunmu:** It's not like workflow.

**Ademilade Shodipe-dosunmu:** It's like some sort of universal way to say, yeah, they haven't just committed end resources to that.

**Matthew Panzarino:** Yeah, that's still, mean, like, if we're talking about accounting, like doing it from an accounting perspective and really keeping ourselves honest, that tacks on seven minutes to all, like, every piece of content that we produce for them, like, from a post-processing perspective.

**Matthew Panzarino:** And, like, that's seven minutes that we can't eliminate with some engineering work.

**Matthew Panzarino:** Is it a pain?

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Yes, things are a pain.

**Matthew Panzarino:** They're a problem.

**Matthew Panzarino:** But he also has additional engineering resources now.

**Matthew Panzarino:** And the EPD, like the Client Ops Eng team, inside the EPD team, like that team is dedicated to solving these kinds of problems.

**Matthew Panzarino:** So have you filed a ticket for that?

**Matthew Panzarino:** It's a problem.

**Ademilade Shodipe-dosunmu:** I think I will check it with Carrie, but I think they did in the past, but it just sort of got lost in all of the resources to this.

**Matthew Panzarino:** the only reason I asked is because if there was a ticket, send it to me, and I will be like, hey, let's get this fixed, because I feel like that's easy performance wins, you know, because we're going to really start aggressively timing ourselves on all this stuff.

**Matthew Panzarino:** We need to.

**Matthew Panzarino:** We need to understand exactly how long it takes to do all of this stuff.

**Matthew Panzarino:** And as we do that, I think a lot of these things will pop out where it's like, wait, why?

**Matthew Panzarino:** Like, why is there additional, you know, seven minutes here for no reason?

**Matthew Panzarino:** Because sanity is a headless CMS.

**Matthew Panzarino:** I mean, it's the prime candidate for being able to publish via API.

**Matthew Panzarino:** There's no reason a human needs to interact with sanity in any way.

**Matthew Panzarino:** Like, it's honestly, it's annoying.

**Matthew Panzarino:** It's very ugly, annoying CMS.

**Matthew Panzarino:** I'm not a fan.

**Matthew Panzarino:** From a human perspective.

**Matthew Panzarino:** As a headless CMS, it's fine.

**Matthew Panzarino:** As long as you're interacting with it on a programmatic level, it's not a big deal, you know.

**Matthew Panzarino:** So let's surface that ticket to try to get it fixed, or we can file a new one, obviously, if there is any refreshed, you know, version of it.

**Matthew Panzarino:** You can just copy the old one and update it with any new information.

**Matthew Panzarino:** So if you think the ticket is too aged, you know, it is too like, oh, wait, and there's a bunch of stuff in here that's not actually true anymore.

**Matthew Panzarino:** Let's just refresh it, and then we will go from there.

**Matthew Panzarino:** This could even be...

**Ademilade Shodipe-dosunmu:** Yeah, go ahead.

**Ademilade Shodipe-dosunmu:** That's all I have to say about that.

**Ademilade Shodipe-dosunmu:** That's all.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** I said I would, I would, would like a note, I would, I would pack Harry after this call, just to find out what's going on there.

**Ademilade Shodipe-dosunmu:** Then I take it from there.

**Ademilade Shodipe-dosunmu:** Same thing for the auto-publishing deal with discern.

**Ademilade Shodipe-dosunmu:** I'll also get that, I'll tag Megika or someone in the PT channel to see if can just take a quick look at it.

**Ademilade Shodipe-dosunmu:** Yeah, I think that's mostly it.

**Ademilade Shodipe-dosunmu:** So I think if you watch, when Pamela watches the videos, she'll be able to stage for your call next week.

**Ademilade Shodipe-dosunmu:** And Pamela, in all the internal channels, like I said before, like our previous meeting, there's like a daily task sheet there.

**Ademilade Shodipe-dosunmu:** That was my personal task sheet of like everything you need to do for each account each day.

**Ademilade Shodipe-dosunmu:** So it's all laid out there.

**Ademilade Shodipe-dosunmu:** It was getting a bit crazy about it in the period, so I had to do that.

**Ademilade Shodipe-dosunmu:** So I remember what I have to do already.

**Ademilade Shodipe-dosunmu:** So it's all there.

**Ademilade Shodipe-dosunmu:** Things can change depending on like requests from your engagement manager, but those are like the typical things you need to do.

**Ademilade Shodipe-dosunmu:** But if there's anything you don't, any task you don't understand there, just like send me a message.

**Ademilade Shodipe-dosunmu:** And like that also includes like the days that Jessica expects articles to be ready for editing, the days she expects not to be ready for staging, like it's all there.

**Ademilade Shodipe-dosunmu:** So just let me know if like your problem is accessing that.

**Ademilade Shodipe-dosunmu:** But for this certain, we're still, Suleiman is still helping.

**Ademilade Shodipe-dosunmu:** So all you need to do is file a ticket.

**Ademilade Shodipe-dosunmu:** I think I've put an example in the handoff doc.

**Ademilade Shodipe-dosunmu:** I'll double check.

**Ademilade Shodipe-dosunmu:** But all you need to do is file a ticket to someone.

**Ademilade Shodipe-dosunmu:** Literally, you're just moving the articles from when you're done, just move it to ready for staging.

**Ademilade Shodipe-dosunmu:** Then in the staging column, indicates whether it's a new article or a refresh.

**Ademilade Shodipe-dosunmu:** And you know what to do from there.

**Ademilade Shodipe-dosunmu:** I don't think I've had many issues with him publishing this one.

**Ademilade Shodipe-dosunmu:** It's been pretty good.

**Ademilade Shodipe-dosunmu:** For your articles, because there's just a ton of them, my typical approach to reviewing PSU is that I review a couple under each cluster and give you feedback that you can apply to the rest of them.

**Ademilade Shodipe-dosunmu:** It's more productive use of time than editing each one manually.

**Ademilade Shodipe-dosunmu:** So I'll go through these and just give you feedback.

**Ademilade Shodipe-dosunmu:** Then you can implement them.

**Ademilade Shodipe-dosunmu:** The reason that I gave you like this weekend stuff was so that you could do half of your next unit.

**Ademilade Shodipe-dosunmu:** Half of like your next week's batch this week, then the other half of next week, next week.

**Ademilade Shodipe-dosunmu:** it's like half workload for your first two weeks before you're ready to take on the full workload.

**Ademilade Shodipe-dosunmu:** So from the week after the 17th, that's when you have to take on the full workload per week.

**Ademilade Shodipe-dosunmu:** So let me know if that works with you and let me know how you're feeling during the week.

**Pamela Weber:** Okay.

**Pamela Weber:** You were with me until you got a bunch of numbers, English major, so awesome.

**Pamela Weber:** And next week I have to go to my son's school.

**Pamela Weber:** They're going to do math games.

**Pamela Weber:** There's no fun with math, but I have to go because that's kind of mom I am.

**Pamela Weber:** I will never miss it.

**Pamela Weber:** So yeah, I have to pretend I know elementary math next week.

**Pamela Weber:** Hopefully he won't embarrass me, but he already started testing me last night.

**Pamela Weber:** And then, yeah, anyway, so I did 13 this week, so that's for next week.

**Pamela Weber:** And then the other 13, you did those or I'm going to do 13 more for next week?

**Ademilade Shodipe-dosunmu:** You just do 13 more for next week.

**Pamela Weber:** Okay.

**Pamela Weber:** Okay.

**Pamela Weber:** So then, yeah.

**Pamela Weber:** And those are in the already like assigned?

**Pamela Weber:** Because I want to get started on those.

**Pamela Weber:** For sure.

**Pamela Weber:** Are they in there?

**Pamela Weber:** Okay.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** So after, I don't know if you have a bit of time after this call, I want to show you how I set up PSU pipelines for discern.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** Because you have to do this because you do this for each cluster.

**Ademilade Shodipe-dosunmu:** That's what I was going to ask next, how I find myself in the future and all that.

**Pamela Weber:** Yeah.

**Pamela Weber:** How I do that.

**Pamela Weber:** Okay, cool.

**Pamela Weber:** Yeah.

**Pamela Weber:** Okay.

**Pamela Weber:** All right.

**Pamela Weber:** Yeah.

**Pamela Weber:** I mean, you guys can take it from here.

**Matthew Panzarino:** I mean, I think you're, you're, you're doing just fine.

**Matthew Panzarino:** know, Ademilade's produced a lot of documentation for you.

**Matthew Panzarino:** I think there's that Yurko thing.

**Matthew Panzarino:** I was just a little bit, I really wanted to get, sorry, put my, put my two cents in on that.

**Matthew Panzarino:** I think we should just move to the agentic pipeline, get whatever ticket file we need to fix to improve that.

**Matthew Panzarino:** On the, I'm actually not going to move the pipeline.

**Matthew Panzarino:** You know where it is now, Pamela.

**Matthew Panzarino:** I'm going to leave it alone for now.

**Matthew Panzarino:** And we'll just keep working on that.

**Matthew Panzarino:** And then eventually we can graduate it to the, to the standard space and clean that up.

**Matthew Panzarino:** But I don't want to move anything around while you're just getting used to everything.

**Matthew Panzarino:** And then, yeah, on the.

**Matthew Panzarino:** PSU thing, as Ademilade out, like, these things are very programmatic, right?

**Matthew Panzarino:** They're extremely templatized.

**Matthew Panzarino:** They are designed to be produced from data sources.

**Matthew Panzarino:** So spot checking is probably going to be fine.

**Matthew Panzarino:** For your first batch, I would probably just look at them all and make sure, you know, just familiarize yourself.

**Matthew Panzarino:** But in the future, you could probably spot check here and there, and you're probably going to be okay.

**Matthew Panzarino:** It's very rare that there's major issues with those kinds of engagements, but, you know, you never know.

**Pamela Weber:** Oh, for Discern, there is a few that they changed the title on me and, like, the tenor of the article.

**Pamela Weber:** And one, I put the note in there for you in Slack, Ademilade.

**Pamela Weber:** And Claude said, no, this is not their market at all, and this isn't the right way to go.

**Pamela Weber:** So it, like, added another table.

**Pamela Weber:** So I put all the notes on why they did that.

**Pamela Weber:** It happened a few times at that list with articles.

**Pamela Weber:** It changed the title, and it changed – it made the first paragraph about just one competitor instead of a general article, and then put each competitor later.

**Pamela Weber:** So I was wondering why Atlas does that, and is that just part of, like –

**Matthew Panzarino:** Our viewing, our viewing here, but in general, Atlas does that because the artifacts tell it to do that.

**Ademilade Shodipe-dosunmu:** Yeah, it's an artifact thing.

**Ademilade Shodipe-dosunmu:** So my guess is that you took an article from the wrong cluster and put it in the wrong PSEO pipeline, pretty much.

**Ademilade Shodipe-dosunmu:** So I'm guessing you took a general best X type of tools for whatever and put it in the best alternatives pipeline.

**Ademilade Shodipe-dosunmu:** And regardless of the topic you put in, for PSEO, it's good to force it into that general structure, regardless of what the topic is or whether it's correct or not.

**Ademilade Shodipe-dosunmu:** So I'm going show you how to set up a different pipeline depending on the topic or rather depending on the cluster.

**Ademilade Shodipe-dosunmu:** after this, I'll show you how to do that.

**Ademilade Shodipe-dosunmu:** And I'll do one live for you on the call.

**Ademilade Shodipe-dosunmu:** Then you can set up additional ones as you please.

**Ademilade Shodipe-dosunmu:** Yeah.

**Pamela Weber:** Thank you.

**Pamela Weber:** Yeah.

**Pamela Weber:** I didn't know what was going on.

**Pamela Weber:** All the articles made sense.

**Pamela Weber:** And I just.

**Pamela Weber:** It's been using a competitive pipeline.

**Pamela Weber:** And then when I did the next one, it changed like the whole, it just got legal zoom.

**Matthew Panzarino:** The reason it changed is because it's like a round peg, square hole, right?

**Matthew Panzarino:** It is saying like, hey, this is a different kind of thing.

**Matthew Panzarino:** And it's going to squeeze it into the mold, right?

**Matthew Panzarino:** It's just going to shove it into there.

**Matthew Panzarino:** And then you'll get very unpredictable results.

**Matthew Panzarino:** This account, mean, Ades set this up pretty well for you.

**Matthew Panzarino:** There are plenty of accounts across the org that like people are trying to do that on a regular basis.

**Matthew Panzarino:** And they're like, oh, man, I'm trying to write this competitor article.

**Matthew Panzarino:** I'm like, yeah, but this is set up for general articles, not competitor articles.

**Matthew Panzarino:** You know, like the example that I gave on this week's, last week's, this week's call.

**Matthew Panzarino:** What day is it?

**Matthew Panzarino:** This week's call about the, who was it, Augment?

**Matthew Panzarino:** Whoever it was.

**Matthew Panzarino:** And it doesn't matter about it being set up for general marketing post, not a post about two different competitors to Augment Code.

**Matthew Panzarino:** And that, it, like, tries to shoehorn in all of the mentions, and it's like, then it creates a mashed potatoes.

**Matthew Panzarino:** You know, now you're, like, spending all this time unraveling these narrative threads.

**Pamela Weber:** Yeah, it totally switched my article on me, yeah.

**Pamela Weber:** Yeah, there's no reason that you said you're completely wrong, so okay, I got Exactly.

**Matthew Panzarino:** So I think you're probably going to be fine once you start using, you know, the right pipelines for the right things, or you set them up properly, because the workflows are not, like, some sort of magic thinking machine, right?

**Matthew Panzarino:** They execute on tasks according to the instructions that you give them, the context that they understand, and then, of course, the rubric that it has to say is this good or not.

**Matthew Panzarino:** And, like, that, if you give it the wrong context, you give it great instructions, but the wrong context, mashed potatoes.

**Matthew Panzarino:** You know, or if you give it, like, bad instructions, but great context, same problem, right?

**Matthew Panzarino:** So those three things really have to line up.

**Matthew Panzarino:** If you are ever ending up with an output that feels really...

**Matthew Panzarino:** I would second-guess yourself on the instructions and context that you're giving the pipeline, rather than going like, oh, the pipeline is suddenly bad.

**Matthew Panzarino:** Probably not.

**Matthew Panzarino:** Think about it, everybody is delivering using the same basic workflows.

**Matthew Panzarino:** There are, of course, custom workflows or specific ones in many pipelines.

**Matthew Panzarino:** Almost every client has a workflow that exists here, but not in somebody else's pipeline.

**Matthew Panzarino:** But the core ones, like the agentic drafter or the post-processing workflow, those operate pretty much on the same principles for everybody.

**Matthew Panzarino:** And in general, if somebody is getting really bad results, like if somebody comes to me and they're like, man, it's taking me two and a half hours to edit these pieces into shape for shipping, my gut is not to blame the person, but really to blame the process, to say like, hey, I think you're giving it bad inputs here, right?

**Matthew Panzarino:** Because it is completely possible to get it online.

**Matthew Panzarino:** Now, there's always weirdness, right?

**Matthew Panzarino:** Yeah, but you can play me.

**Matthew Panzarino:** Maybe I went to the wrong pipeline.

**Matthew Panzarino:** That's why I did it.

**Pamela Weber:** But I looked at the research stuff, and it made sense.

**Pamela Weber:** The post-process.

**Pamela Weber:** But then the next one, they switched the article from research to the next.

**Pamela Weber:** And that's why I thought maybe it was Atlas, and I went to Cloak.

**Pamela Weber:** Because I didn't understand.

**Pamela Weber:** It was on the right track, and it switched on me.

**Pamela Weber:** So, okay.

**Pamela Weber:** All right.

**Pamela Weber:** So now I got it.

**Pamela Weber:** We'll figure it out.

**Matthew Panzarino:** But, yeah, Ademilade set you up pretty well.

**Matthew Panzarino:** And, you know, he's been pretty sophisticated about getting me set up to make his life easier.

**Matthew Panzarino:** So it should make your life easier, too.

**Matthew Panzarino:** So, cool.

**Matthew Panzarino:** Thanks.

**Matthew Panzarino:** You guys can keep talking, whatever.

**Matthew Panzarino:** I'm going to bounce my next thing.

**Matthew Panzarino:** But I appreciate you taking the time out of And I just wanted to kind of, like, chat that out.

**Matthew Panzarino:** Because I didn't want Pamela to be struggling, especially since we had the holidays.

**Matthew Panzarino:** So this is our first check-in.

**Matthew Panzarino:** Normally, I would have had this earlier with her.

**Matthew Panzarino:** I just wanted to follow up.

**Matthew Panzarino:** So thank you so much.

**Matthew Panzarino:** Appreciate it.

**Matthew Panzarino:** Thanks.

**Pamela Weber:** Gotcha.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** Let's, like, dive in.

**Ademilade Shodipe-dosunmu:** Let me just share my screen.

**Ademilade Shodipe-dosunmu:** So.

**Ademilade Shodipe-dosunmu:** So we kind of work through like how this process goes.

**Ademilade Shodipe-dosunmu:** Because if at any point, if you lost, please let me know.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** So I'm going to, I need to open up.

**Pamela Weber:** I've been lost a few times the last week, but like when I was in Claude, I was lost.

**Pamela Weber:** And then I got to Claude B, I was like, oh, it's a whole new world.

**Pamela Weber:** This makes sense now.

**Pamela Weber:** It's like, because I kept giving that to our guidelines to Claude.

**Pamela Weber:** I'm like, I thought you already knew this.

**Pamela Weber:** But then I wasn't in pod B, I didn't realize.

**Pamela Weber:** Yeah.

**Pamela Weber:** And then I was on the high point.

**Pamela Weber:** Yes.

**Pamela Weber:** It looks, yeah, and it makes more sense now.

**Pamela Weber:** So, yeah, thank you.

**Ademilade Shodipe-dosunmu:** So for your post-processing, just to make sure that you have everything down, you've been using the projects in Claude, yeah?

**Ademilade Shodipe-dosunmu:** No.

**Pamela Weber:** Yes.

**Pamela Weber:** Okay, great.

**Ademilade Shodipe-dosunmu:** So you've seen like the projects for each of the accounts here.

**Ademilade Shodipe-dosunmu:** Yeah, I've only been using this on your code.

**Pamela Weber:** There's nothing.

**Pamela Weber:** Anything beyond that, is there, like, specifics within it?

**Ademilade Shodipe-dosunmu:** There's one for diligence.

**Ademilade Shodipe-dosunmu:** Yeah, I didn't get that.

**Ademilade Shodipe-dosunmu:** And there's one for looker tasks.

**Ademilade Shodipe-dosunmu:** And I referenced this when I showed you how to do looker.

**Pamela Weber:** Yeah, I remember that.

**Pamela Weber:** And when do I have to start doing looker?

**Pamela Weber:** Is that next week?

**Pamela Weber:** Yeah, next week as well.

**Ademilade Shodipe-dosunmu:** I should do it on Mondays.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** So I'll update all the askers published a week prior.

**Pamela Weber:** And I may need help on that.

**Pamela Weber:** I'll look at the video, but then I should ask you or Kari if I'm stuck on that.

**Ademilade Shodipe-dosunmu:** Yeah, for Yoriko, look at the video, then ask me or Kari, yes.

**Ademilade Shodipe-dosunmu:** But for discern, for discern next week, I'm just trying to get a number of articles that were pushed.

**Ademilade Shodipe-dosunmu:** I'm to figure out the clusters.

**Ademilade Shodipe-dosunmu:** Yeah, for discern next week, don't worry about that.

**Ademilade Shodipe-dosunmu:** I'll do next week, but you have to do the one the week after.

**Ademilade Shodipe-dosunmu:** Because next week, you don't need work because of this week, we publish only refreshes.

**Ademilade Shodipe-dosunmu:** So you don't to do that again.

**Ademilade Shodipe-dosunmu:** Because you're...

**Ademilade Shodipe-dosunmu:** Freshers were already in the URL on the dashboard, so from next week, we're going to be publishing net new articles, so you need to add those to the course.

**Pamela Weber:** And then next week for discern, I do the staging thing you said, where I send a ticket, and then it's going to be published?

**Ademilade Shodipe-dosunmu:** Yeah, so let me just show you how staging works for discern.

**Ademilade Shodipe-dosunmu:** So, for discern, when you want to send something to staging, for example, so I'm just going to rename this, because, sorry, I don't know why it's not, okay, that's just annoying.

**Ademilade Shodipe-dosunmu:** Anyways, then I figured out how I edit these guys, I'm going to rename this, so that you sort of know.

**Ademilade Shodipe-dosunmu:** I'll just put it as assignments or something.

**Ademilade Shodipe-dosunmu:** But yeah, so generally, like, when you want to stage, just, you know, these refreshing ones for now, because I was wondering.

**Ademilade Shodipe-dosunmu:** I was doing them, but these are the ones we're looking at.

**Ademilade Shodipe-dosunmu:** For example, now let's say this article has been approved.

**Ademilade Shodipe-dosunmu:** You just move this from where it is.

**Ademilade Shodipe-dosunmu:** now it's definitely ready to start.

**Ademilade Shodipe-dosunmu:** It's not supposed to be ready to start.

**Ademilade Shodipe-dosunmu:** supposed to be in article gen because you've already started generating it.

**Pamela Weber:** yeah.

**Pamela Weber:** Sorry.

**Pamela Weber:** I didn't take all of it.

**Pamela Weber:** Okay.

**Ademilade Shodipe-dosunmu:** So all of these should be in article gen.

**Ademilade Shodipe-dosunmu:** Okay.

**Pamela Weber:** I did add my images back in the right place, so.

**Pamela Weber:** I was somewhere else, I guess.

**Pamela Weber:** I added the meta.

**Pamela Weber:** I didn't do it for the rest of them yet because I want to know your feedback.

**Pamela Weber:** Like if I got the article all wrong and I have to change the meta, I didn't want to, you know, do it twice.

**Pamela Weber:** So I'll give it back when I'll add all of those.

**Ademilade Shodipe-dosunmu:** I think the images here are fine, I guess.

**Ademilade Shodipe-dosunmu:** Okay, this image is weird.

**Ademilade Shodipe-dosunmu:** I don't know why it's weird.

**Pamela Weber:** I'm sorry?

**Ademilade Shodipe-dosunmu:** It's a bit odd.

**Ademilade Shodipe-dosunmu:** I think this image is a bit odd.

**Ademilade Shodipe-dosunmu:** But the article here is supposed to be best CSE alternatives.

**Ademilade Shodipe-dosunmu:** think that's...

**Ademilade Shodipe-dosunmu:** thing is discern, eliminate.

**Ademilade Shodipe-dosunmu:** Oh, did I put the wrong one?

**Ademilade Shodipe-dosunmu:** Yeah, think this was like a wrong image.

**Pamela Weber:** Okay.

**Ademilade Shodipe-dosunmu:** Like it has to match like with the title.

**Pamela Weber:** course.

**Pamela Weber:** I'm using the regenerative image, yeah.

**Pamela Weber:** Okay, I'll check.

**Ademilade Shodipe-dosunmu:** So, for example, now, let me use an article that I've worked on already.

**Ademilade Shodipe-dosunmu:** And that's been approved as like an example of like how we send stuff to stages.

**Ademilade Shodipe-dosunmu:** So this one has been approved by the client and the script to go.

**Ademilade Shodipe-dosunmu:** So once it's edited, I move it from article gen to ready for staging.

**Ademilade Shodipe-dosunmu:** So when I move that there, it's going to be on this list where you say ready to stage.

**Ademilade Shodipe-dosunmu:** The article is here.

**Ademilade Shodipe-dosunmu:** So here, when I move to ready to staging, I have to add what type of content it is.

**Ademilade Shodipe-dosunmu:** This is a new article.

**Ademilade Shodipe-dosunmu:** So I'll put a new tag.

**Ademilade Shodipe-dosunmu:** So Sulaiman knows it's a new article.

**Ademilade Shodipe-dosunmu:** If you don't put a tag, then he doesn't know whether it's new or not.

**Ademilade Shodipe-dosunmu:** So that might cause like issues down the line.

**Ademilade Shodipe-dosunmu:** So what?

**Ademilade Shodipe-dosunmu:** So

**Ademilade Shodipe-dosunmu:** What from here is you're now going to linear, so for example, let's say you've, so the idea with Diligent Discern is that we publish 26 articles every week, but we don't publish them all at once, so we do them in batches, so maybe a batch of 8 or 10, right, so once you're done, maybe 8 per the week, or 6 even, you just let Sulaiman know, oh, hey, I've moved, I've moved blah, blah, blah, no more articles to publish him.

**Ademilade Shodipe-dosunmu:** So, this is linear, so, oh, sorry, I don't know why it vanished, okay, so this is linear, and, oh, crap, okay, so I'm trying to figure out the best way to do this for you, okay, all right, let's do it this way, so where is this, okay, this is the same, all right, so you can use can can use you you.

**Ademilade Shodipe-dosunmu:** So typically I have like a recurring ticket for discern, so it comes up every week, like clockwork, it just comes up every week, so all you need to do is go to the ticket for that particular week, and so for example the ticket for this week is, I have to go to related here, so we're going to related here, okay here, this is the ticket for this week, and my first comment for this ticket is, oh I've uploaded the first Batch of Terran Freshers to our table, thanks, so he knows from this, ideally you can go the step forward by maybe copying this ticket link, then once you copy that, you can move into the internal channel for discern, and drop a message like this for Suleman, so hey, we're building a batch of this, here's the weekly ticket, I'll play the third and a half already, thank you.

**Ademilade Shodipe-dosunmu:** Thank

**Ademilade Shodipe-dosunmu:** Then, when you upload more for the week, because you know it's 26, you're going to come into this thread, this particular thread for that week, and just let him know, hey, at Slaman, maybe 10 more articles uploaded, just so he knows, and he'll work on it.

**Ademilade Shodipe-dosunmu:** That's pretty much it.

**Ademilade Shodipe-dosunmu:** And you also update the linear tickets here for company-wide visibility.

**Ademilade Shodipe-dosunmu:** Does that make sense?

**Ademilade Shodipe-dosunmu:** Yeah.

**Pamela Weber:** That's cool.

**Pamela Weber:** quickly shows up for me.

**Pamela Weber:** That's cool.

**Pamela Weber:** Yeah.

**Ademilade Shodipe-dosunmu:** So, yeah, that's honestly it.

**Ademilade Shodipe-dosunmu:** So it's already a recurring ticket.

**Ademilade Shodipe-dosunmu:** So all you need to do is just go.

**Ademilade Shodipe-dosunmu:** You see all these have been done.

**Ademilade Shodipe-dosunmu:** So you have to go to the one that has not been done.

**Ademilade Shodipe-dosunmu:** So that's obviously the latest one.

**Ademilade Shodipe-dosunmu:** And click that.

**Ademilade Shodipe-dosunmu:** And there it is.

**Ademilade Shodipe-dosunmu:** So it just goes like clockwork like this every week.

**Ademilade Shodipe-dosunmu:** And the only thing you need to do is just tag Slaman to the ticket.

**Ademilade Shodipe-dosunmu:** Make sure you tag him and put it in Slack and you should be good to go.

**Ademilade Shodipe-dosunmu:** next time.

**Ademilade Shodipe-dosunmu:** All right, next thing is, so you're going to do that next week.

**Ademilade Shodipe-dosunmu:** So let's see, you already have about, you have about, let me go to assignments, sorry.

**Ademilade Shodipe-dosunmu:** Okay, so here you already have like a copy of the generation, like you have 12 here, if I'm not mistaken.

**Ademilade Shodipe-dosunmu:** Yeah, you have 12 here already.

**Ademilade Shodipe-dosunmu:** So I think there's one missing because it was supposed to be 13.

**Ademilade Shodipe-dosunmu:** I don't know.

**Ademilade Shodipe-dosunmu:** I'm just going to assign these to you as well.

**Ademilade Shodipe-dosunmu:** Yeah, think when I started, you switched to your name, you took it over.

**Pamela Weber:** So I think that's why there was one, know there's another one I've started.

**Pamela Weber:** But it's okay, mean, I'll just go on.

**Pamela Weber:** can add whatever for next week.

**Pamela Weber:** Okay.

**Ademilade Shodipe-dosunmu:** So now we have, that is due to these.

**Ademilade Shodipe-dosunmu:** These are like 14, so that's like 26.

**Ademilade Shodipe-dosunmu:** So these will be next week.

**Ademilade Shodipe-dosunmu:** All right, so for these ones here, we've already generated them.

**Ademilade Shodipe-dosunmu:** So maybe when I review like one or two of them, when I'm done and you've affected it to all of them, you just like move them to ready for staging, then let Solomar know next week.

**Ademilade Shodipe-dosunmu:** Oh, hey, I've added X amount of hours to most, blah, blah, blah, blah, blah.

**Ademilade Shodipe-dosunmu:** Yeah, pretty much the flow for that.

**Ademilade Shodipe-dosunmu:** But then regarding like how you pick topics for yourself, usually you can ask, not like you can ask Vivek, you can ask Vivek if like the client prioritized anything.

**Ademilade Shodipe-dosunmu:** Because sometimes like for discern, we have like a schedule and I'll show you the schedule for the weeks ahead already.

**Ademilade Shodipe-dosunmu:** But like sometimes the client just like has these, oh, hey, let's do this instead, you know, or let's prioritize these.

**Ademilade Shodipe-dosunmu:** So in cases like those, you can just like ask Vivek if the client mentioned anything or we should move with a regular production schedule.

**Ademilade Shodipe-dosunmu:** Right.

**Ademilade Shodipe-dosunmu:** So for example, by next week, you'll done.

**Ademilade Shodipe-dosunmu:** But like these are the last, I think these are the last contest or comparisons, I think, I don't know if there are any others, let me check.

**Ademilade Shodipe-dosunmu:** So if you want to see what the other schedule looks like, you go to, not here, sorry, ready to start.

**Ademilade Shodipe-dosunmu:** Sorry, that's very strange.

**Ademilade Shodipe-dosunmu:** Oh, I don't know why this always happens.

**Ademilade Shodipe-dosunmu:** Okay, I should be ready to draft.

**Ademilade Shodipe-dosunmu:** All right.

**Ademilade Shodipe-dosunmu:** Yeah, so it's here, ready to draft.

**Ademilade Shodipe-dosunmu:** I'm going to just filter this.

**Pamela Weber:** Wait, can you go back, please?

**Pamela Weber:** I'm sorry and show me how, oh, it's right there.

**Pamela Weber:** So it's on the left.

**Pamela Weber:** Yeah.

**Pamela Weber:** Okay, got it.

**Pamela Weber:** Thank you.

**Ademilade Shodipe-dosunmu:** No problem.

**Ademilade Shodipe-dosunmu:** I'm just going to filter this to make sure you're just having the stuff you need.

**Ademilade Shodipe-dosunmu:** So where the assignment is either box.

**Ademilade Shodipe-dosunmu:** of of Dina

**Ademilade Shodipe-dosunmu:** Clock, plus, considering, plus, not ready to start, but approved for creation, or, yeah, yeah, yeah, this is, this is pretty much the flow.

**Ademilade Shodipe-dosunmu:** Yeah, so, for the next couple of weeks, you're just taking articles, you can see that there are like a ton of articles here.

**Ademilade Shodipe-dosunmu:** About, I think I put in about, yeah, 615.

**Ademilade Shodipe-dosunmu:** So that should take you guys to, probably, to the end of their current contract, before they decide to renew, obviously.

**Ademilade Shodipe-dosunmu:** But, yeah, that's pretty much, yeah, so what you do is, every week, you just come in and pick 26 of these.

**Ademilade Shodipe-dosunmu:** So, for example, next up, you're moving to another cluster.

**Ademilade Shodipe-dosunmu:** This cluster is private equity fund formation.

**Ademilade Shodipe-dosunmu:** So that's going to require another pipeline.

**Ademilade Shodipe-dosunmu:** So you're going to have to create a pipeline that can handle these type of topics, then for the first topic within each cluster, you need to send it to the client, the client will give feedback, the client gives feedback on that cluster, then use that as a calibration block for the remaining articles inside that cluster.

**Ademilade Shodipe-dosunmu:** How many?

**Pamela Weber:** I'm sorry, how many can you send over?

**Pamela Weber:** Okay, okay, got it, thank you.

**Ademilade Shodipe-dosunmu:** This is the first one.

**Ademilade Shodipe-dosunmu:** So what I usually do is like you read before I start a new cluster, I try to, you know, get that this is the first article under that cluster done, and send that to the client so you can review.

**Ademilade Shodipe-dosunmu:** So it doesn't affect my flow for next week.

**Ademilade Shodipe-dosunmu:** So next week, you need to probably send this first one, this Alabama, I read equity for information article, so they're there for the clients.

**Ademilade Shodipe-dosunmu:** I can probably take a look for you, give some feedback, and push it to the client, and let's see what he says.

**Ademilade Shodipe-dosunmu:** Then that's what we now use to kind

**Ademilade Shodipe-dosunmu:** So after you're done with next week, the PowerPoint, can just come in here and pick 26, you move them from Approach to Creation to Ready to Start, then once you've done that, you can just go to Assignments here, I would like to probably just rename, I don't know why it's not allowing me to rename this, sorry.

**Pamela Weber:** Wait, I'm sorry, had one question, so I see how you pick the 26, but how do you get them over, oh, that's what you're doing now, okay, how do you get them over there?

**Ademilade Shodipe-dosunmu:** Oh, let me just move that, sorry, just trying to, hmm, sorry, oh, ah, You

**Ademilade Shodipe-dosunmu:** Sorry, I don't know why this, like, sometimes I need to do those pieces right here.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** Oh, okay.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** Alright, I think this should work.

**Ademilade Shodipe-dosunmu:** And just add that's a favorite.

**Ademilade Shodipe-dosunmu:** This can actually go.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** Okay, that makes sense.

**Ademilade Shodipe-dosunmu:** So, when we want to move them, for example, I go to, remember, we're in Ready to Draft.

**Ademilade Shodipe-dosunmu:** There's assignments here.

**Ademilade Shodipe-dosunmu:** Yep.

**Ademilade Shodipe-dosunmu:** Ready to edit.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** So, Ready to Draft, all you need to do is just come here.

**Ademilade Shodipe-dosunmu:** When you want to pick the topic, you go, you select, for example, this one I put for creation and just click Ready to Start.

**Ademilade Shodipe-dosunmu:** Once you click this, it's going to leave this view.

**Ademilade Shodipe-dosunmu:** Then you go to assignments.

**Ademilade Shodipe-dosunmu:** Then Okay, we're going to see.

**Ademilade Shodipe-dosunmu:** That article has been added right here under a new close line, so, yeah.

**Pamela Weber:** Cool, and how did you make it, I get how it moved over there, but how did, how did it give it that title?

**Pamela Weber:** just decided?

**Ademilade Shodipe-dosunmu:** Is it this Alabama, is it this title?

**Pamela Weber:** Okay, but like that whole cluster now, have to rename it in this side, right?

**Ademilade Shodipe-dosunmu:** I'm I'm trying to clarify your question, is it this, what are you asking about essentially?

**Ademilade Shodipe-dosunmu:** Well, I get how they got over there, but now you have to like organize it here, so, are you going to organize it by the No, it's already, it's already, it's already pre-organized by cluster.

**Ademilade Shodipe-dosunmu:** Oh, okay, got it, okay.

**Pamela Weber:** I didn't know if that was the title of the article or the cluster, I can't tell, because it's, I get it.

**Ademilade Shodipe-dosunmu:** okay, yeah, so, yeah, so the one on top here is topic cluster, by week, that's like up to you.

**Ademilade Shodipe-dosunmu:** So, I'm currently trying to finalize these articles for this week, and I'll do that later today.

**Ademilade Shodipe-dosunmu:** That's why they're still here.

**Ademilade Shodipe-dosunmu:** But by then I'm done with these.

**Ademilade Shodipe-dosunmu:** You'll only be seeing your articles for the week.

**Ademilade Shodipe-dosunmu:** So that will be these ones that you have in generation and these ones that are ready to start.

**Ademilade Shodipe-dosunmu:** So these are the ones you need to work on for next week.

**Ademilade Shodipe-dosunmu:** So you have to just sort of take note of those.

**Ademilade Shodipe-dosunmu:** But ignore these ones that are up here that say refreshing.

**Ademilade Shodipe-dosunmu:** These ones are correctly for me, but they'll be gone.

**Ademilade Shodipe-dosunmu:** However, I do think Vivek wants to send some more refreshes our way, rather your way.

**Ademilade Shodipe-dosunmu:** So we'll see what it says on the internal channel.

**Ademilade Shodipe-dosunmu:** I saw some chatter on the external channel about having more refreshes because they lost some keyword positions for some task page.

**Ademilade Shodipe-dosunmu:** So we want to refresh to get them back up.

**Ademilade Shodipe-dosunmu:** But let's see how that works.

**Pamela Weber:** And for refresh, do you do it any differently in the pipeline or you just put that?

**Ademilade Shodipe-dosunmu:** Yeah, yeah.

**Ademilade Shodipe-dosunmu:** So refresh is a totally different process entirely.

**Ademilade Shodipe-dosunmu:** We don't have a working pipeline for refreshes.

**Ademilade Shodipe-dosunmu:** Because just the way they are, they're bit manual in the sense of like checking some dates, some secretary of state websites for like updated information.

**Ademilade Shodipe-dosunmu:** And when you have your first refresh, I'll show you how to do it.

**Ademilade Shodipe-dosunmu:** But eventually we're going to need to put that in a pipeline.

**Ademilade Shodipe-dosunmu:** So I'm going to show you the manual way that I do them.

**Ademilade Shodipe-dosunmu:** And you just need to communicate that to engineering to set up a pipeline for those.

**Ademilade Shodipe-dosunmu:** It's because like we do mainly net new, that's why I hadn't set up a pipeline for them yet.

**Ademilade Shodipe-dosunmu:** But like if we're going to be doing more refreshes here, we should set up a pipeline.

**Ademilade Shodipe-dosunmu:** There's a refresh pipeline there already, but like it doesn't really do a very good job.

**Ademilade Shodipe-dosunmu:** So, yeah.

**Pamela Weber:** Thank you.

**Ademilade Shodipe-dosunmu:** That's pretty much this.

**Ademilade Shodipe-dosunmu:** So, now I'm just wanting to show you how we set up pipelines for this.

**Ademilade Shodipe-dosunmu:** So, if you take a look at like this article.

**Ademilade Shodipe-dosunmu:** article.

**Ademilade Shodipe-dosunmu:** Or rather, let's go into here, let's go into the Content Planner.

**Ademilade Shodipe-dosunmu:** I think I separated it much better there.

**Ademilade Shodipe-dosunmu:** So yeah, you don't have to use this Content Planner anymore, because I think if you prefer it's in a table, you can just ignore these, yeah.

**Ademilade Shodipe-dosunmu:** So, from what I can see here, yeah, these are all the articles for, yeah, there are about 27 of them, yeah, yeah, yeah, okay.

**Ademilade Shodipe-dosunmu:** Okay, so, in general, for these competitor comparisons, they are split into three types of articles.

**Ademilade Shodipe-dosunmu:** If, like, you look at them, so first off, you have best company alternatives.

**Ademilade Shodipe-dosunmu:** So that's, like, alternatives, right?

**Ademilade Shodipe-dosunmu:** So it's like, hey, we're taking this company that people want to run away from, and here are the alternatives, and we position this one as number one, right?

**Ademilade Shodipe-dosunmu:** So that's a separate type of article.

**Ademilade Shodipe-dosunmu:** Then, if you go a bit deeper, you're going to have best platforms generally.

**Ademilade Shodipe-dosunmu:** For particular ICP pain points, so here you have best platforms for entity formation and whatever, you have compliance software that integrates to entity management, have all-in-one registered agents and compliance filing platforms, entity formation to this, that's one, two, three, four.

**Ademilade Shodipe-dosunmu:** You have this, best compliance software for multi-state businesses as well, that falls on that, that, or that bracket of best platforms for specific pain points, right, so that's different from alternatives, because alternative, you are like, so why do people want to go away from this particular provider, for these ones, you just have any general article, what are the best articles for this particular use case, and I put it in the center as number one, right, good, then the last, the second, the next one is best, is particular service, or I think all of these are registered agent, honestly, so, all of these are best registered agent service, for chocolate.

**Ademilade Shodipe-dosunmu:** Venture Capital Firms, Best Registered Agents for Defense Needs Entirely, this is 1, 2, 3, 4, 5, 6, so 6 different articles under this new one, Best Registered Agents for whatever use case, for Venture Capital, for whatever, that's going to be a separate pipeline that we're going to need to set up for that, if that makes sense.

**Ademilade Shodipe-dosunmu:** Then the last one, I get this, this is, are you a bit lost?

**Pamela Weber:** Yeah, I'm just, are these the ones I just worked on, or these are upcoming?

**Ademilade Shodipe-dosunmu:** I think some you have worked on, and that's why you're getting those fuzzy.

**Ademilade Shodipe-dosunmu:** Okay, yeah, because I was doing the contentors.

**Pamela Weber:** Okay, so then, do I need a different pipeline for next, to do the next ones, because I was going to start those.

**Pamela Weber:** Yeah.

**Ademilade Shodipe-dosunmu:** Okay, how do I do that?

**Pamela Weber:** I do that, or engineering does, or?

**Ademilade Shodipe-dosunmu:** Engineering can do it, but like, you need those pretty fast, so.

**Pamela Weber:** not today, I was hoping so today.

**Pamela Weber:** Yeah, exactly.

**Ademilade Shodipe-dosunmu:** I'll show you how to set one up.

**Ademilade Shodipe-dosunmu:** I'll probably even just set one up now, and we'll see where it goes.

**Pamela Weber:** Okay, thank you.

**Ademilade Shodipe-dosunmu:** So, then we have this versus articles, right?

**Ademilade Shodipe-dosunmu:** So based off of that, right, let me just even copy all of these.

**Ademilade Shodipe-dosunmu:** Okay, let me just copy all of these and put them in a new doc.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** Yeah, we put them in a doc just to show you pretty much what we're dealing with and how, as if I didn't want to separate them.

**Ademilade Shodipe-dosunmu:** So, we have best alternatives, right?

**Ademilade Shodipe-dosunmu:** So that's one cluster.

**Ademilade Shodipe-dosunmu:** We already have a pipeline for this, so we're good.

**Ademilade Shodipe-dosunmu:** Then we move on to best platforms.

**Ademilade Shodipe-dosunmu:** All.

**Ademilade Shodipe-dosunmu:** you.

**Ademilade Shodipe-dosunmu:** So best platform for this, this, compliance, there's NC promotion, this is all on our one, then.

**Pamela Weber:** So best alternatives, that's the competitor pipeline?

**Pamela Weber:** Yes, that's what I mean.

**Pamela Weber:** Okay.

**Pamela Weber:** So yeah, good for these ones.

**Ademilade Shodipe-dosunmu:** Then let me also just hit one.

**Ademilade Shodipe-dosunmu:** Just send you this doc in case, I'll send you on Slack, in case you need to.

**Ademilade Shodipe-dosunmu:** Okay, let me just add you here.

**Ademilade Shodipe-dosunmu:** Yep.

**Ademilade Shodipe-dosunmu:** Okay, I got it in.

**Ademilade Shodipe-dosunmu:** All right.

**Ademilade Shodipe-dosunmu:** Then next one is, best registered agent services for.

**Ademilade Shodipe-dosunmu:** Projects or dead.

**Ademilade Shodipe-dosunmu:** Yeah, so for this one, these are the articles on that app.

**Ademilade Shodipe-dosunmu:** Then the next one is discern versus context.

**Ademilade Shodipe-dosunmu:** Yeah, so this is a head-to-head comparison.

**Ademilade Shodipe-dosunmu:** Yeah, that's pretty much it.

**Ademilade Shodipe-dosunmu:** This is how they are broken down already.

**Ademilade Shodipe-dosunmu:** So I'm going to walk you through the process of...

**Ademilade Shodipe-dosunmu:** I'm going to create a pipeline for this particular one.

**Ademilade Shodipe-dosunmu:** All right, I'll show you how it's done.

**Ademilade Shodipe-dosunmu:** So we'll just go through the entire process.

**Ademilade Shodipe-dosunmu:** So you might need to watch the video again.

**Ademilade Shodipe-dosunmu:** But after I do this one, you're going to need to create for this one and to the email, so you can through one.

**Ademilade Shodipe-dosunmu:** Oh, yeah.

**Ademilade Shodipe-dosunmu:** give Nemechaud.

**Ademilade Shodipe-dosunmu:** So be answers a And I mean

**Ademilade Shodipe-dosunmu:** This one, before you can finish up this cluster.

**Ademilade Shodipe-dosunmu:** But I'm going to do this one for you so you can just get started on these ones.

**Ademilade Shodipe-dosunmu:** Because I think some of them were from the ones you did that you were getting wonky and wonky docs or something.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** Okay, so I simply use Claude when I want to come up with templates.

**Ademilade Shodipe-dosunmu:** So let's go to discern Claude.

**Ademilade Shodipe-dosunmu:** And let me open Atlas as well so that, like, you have an idea on how this works.

**Ademilade Shodipe-dosunmu:** So you can also use...

**Ademilade Shodipe-dosunmu:** Okay, let me just...

**Ademilade Shodipe-dosunmu:** All right, let's come up here.

**Ademilade Shodipe-dosunmu:** So this is a test.

**Ademilade Shodipe-dosunmu:** I'm just going to go ahead and archive this.

**Ademilade Shodipe-dosunmu:** Then I'm also just going to archive a bunch of these because...

**Ademilade Shodipe-dosunmu:** I just want the page to look a bit cleaner.

**Ademilade Shodipe-dosunmu:** And just also because of what we're done with all these clusters.

**Ademilade Shodipe-dosunmu:** those.

**Ademilade Shodipe-dosunmu:** So the problem with this one is that you end up with a lot of cluster, I mean, pipelines, because of the sheer amount of clusters you're doing, you know?

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** So all of these are out.

**Ademilade Shodipe-dosunmu:** This is out as well.

**Ademilade Shodipe-dosunmu:** And this is out as well.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** So I'll stop with this guy.

**Ademilade Shodipe-dosunmu:** So we want to have a few things.

**Ademilade Shodipe-dosunmu:** So I'm going to open artifacts as well, because we're going to need those.

**Ademilade Shodipe-dosunmu:** And we're going to create a new pipeline.

**Ademilade Shodipe-dosunmu:** So I'm going to first go to edit.

**Ademilade Shodipe-dosunmu:** So I go to edit this pipeline.

**Ademilade Shodipe-dosunmu:** And I just copy everything here first.

**Ademilade Shodipe-dosunmu:** All right.

**Ademilade Shodipe-dosunmu:** Wait, we're going to edit it.

**Pamela Weber:** I miss that.

**Pamela Weber:** Okay, so at the top right.

**Ademilade Shodipe-dosunmu:** At the artifact.

**Ademilade Shodipe-dosunmu:** Okay, got it.

**Pamela Weber:** Yeah.

**Ademilade Shodipe-dosunmu:** Then copy that.

**Ademilade Shodipe-dosunmu:** Then go here to create a new pipeline.

**Ademilade Shodipe-dosunmu:** And I just paste all of that over here.

**Ademilade Shodipe-dosunmu:** Then I now need to edit this pipeline to be able to give me the results that I'm looking for, pretty much.

**Ademilade Shodipe-dosunmu:** And this way, this might get a bit tricky, but it's fine.

**Ademilade Shodipe-dosunmu:** So now, this is a comparison.

**Ademilade Shodipe-dosunmu:** Let's just call these listicle, right?

**Ademilade Shodipe-dosunmu:** Because it's just a basic listicle of the best, or let's call it general listicle.

**Ademilade Shodipe-dosunmu:** Just so you can tag them.

**Ademilade Shodipe-dosunmu:** You can give them any name you want.

**Ademilade Shodipe-dosunmu:** But I'm putting general listicle because, like, that's how I understand this, what we're creating, essentially, because we're doing best, or should I put it as best platforms for pain points?

**Ademilade Shodipe-dosunmu:** I think that would make it easier for you to identify.

**Ademilade Shodipe-dosunmu:** Let me just name it best platforms for pain points.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** All right.

**Ademilade Shodipe-dosunmu:** We good?

**Ademilade Shodipe-dosunmu:** Are you good so far?

**Pamela Weber:** Yeah.

**Pamela Weber:** Okay.

**Pamela Weber:** All right.

**Ademilade Shodipe-dosunmu:** So, for each...

**Ademilade Shodipe-dosunmu:** For each, what do you call it, for each time you create a new PSEO pipeline, there are a few things that you need to change, right?

**Ademilade Shodipe-dosunmu:** We need to have a template for each PSEO pipeline.

**Ademilade Shodipe-dosunmu:** Just so you know, this is like a bit of a workshop.

**Ademilade Shodipe-dosunmu:** So each PSEO pipeline needs a template.

**Ademilade Shodipe-dosunmu:** It needs a sample article.

**Ademilade Shodipe-dosunmu:** And, what is that?

**Ademilade Shodipe-dosunmu:** Here, a sample article.

**Ademilade Shodipe-dosunmu:** But that's all.

**Ademilade Shodipe-dosunmu:** Yeah, that's pretty much it.

**Ademilade Shodipe-dosunmu:** A template and a sample article.

**Ademilade Shodipe-dosunmu:** I started that as if it was three things.

**Ademilade Shodipe-dosunmu:** But yeah, a template and a sample article.

**Ademilade Shodipe-dosunmu:** That's what you need for each PSEO article.

**Ademilade Shodipe-dosunmu:** For each PSEO pipeline, just a template and a sample article.

**Ademilade Shodipe-dosunmu:** Those are the only things we change with each template.

**Ademilade Shodipe-dosunmu:** Alright.

**Ademilade Shodipe-dosunmu:** So that means we need to create a template.

**Ademilade Shodipe-dosunmu:** And this is my alternative template here already.

**Ademilade Shodipe-dosunmu:** It's the one that I'm already using.

**Ademilade Shodipe-dosunmu:** It's just a template that shows the pipeline, oh, okay, this is how the ASCII should look, and this is what you're supposed to cover in each section.

**Ademilade Shodipe-dosunmu:** So we have to create something like this, but for the new cluster that we're doing.

**Ademilade Shodipe-dosunmu:** For example, if you go to...

**Ademilade Shodipe-dosunmu:** All right, so I sent you this resources doc before.

**Ademilade Shodipe-dosunmu:** This is where I keep a lot of my resources.

**Ademilade Shodipe-dosunmu:** We're going to schema here.

**Ademilade Shodipe-dosunmu:** No, I don't know if have this one.

**Pamela Weber:** I don't...

**Pamela Weber:** Oh, okay.

**Pamela Weber:** Thank you.

**Ademilade Shodipe-dosunmu:** Let me...

**Ademilade Shodipe-dosunmu:** I'm just going to add you to it.

**Ademilade Shodipe-dosunmu:** So you go to schema here, and you open this up.

**Ademilade Shodipe-dosunmu:** have...

**Ademilade Shodipe-dosunmu:** So let me just close this.

**Ademilade Shodipe-dosunmu:** Is there some work on another client?

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** So you have this.

**Ademilade Shodipe-dosunmu:** So different schema here.

**Ademilade Shodipe-dosunmu:** So yeah, best alternative, this is my...

**Ademilade Shodipe-dosunmu:** The current schema for this one.

**Ademilade Shodipe-dosunmu:** That's the one you're currently using.

**Ademilade Shodipe-dosunmu:** I've not created the one for versus articles or best x-listicles, but this is the next one we're going to do.

**Ademilade Shodipe-dosunmu:** So that's what we need to create.

**Ademilade Shodipe-dosunmu:** So there are different ways to create this schema.

**Ademilade Shodipe-dosunmu:** But the idea is that you're supposed to do research of what those articles look like on the SERPs and what they include.

**Ademilade Shodipe-dosunmu:** So, for example, let's say, what are the articles here?

**Ademilade Shodipe-dosunmu:** It's the best platform for both entity formation and ongoing compliance.

**Ademilade Shodipe-dosunmu:** Let's just see.

**Ademilade Shodipe-dosunmu:** All right.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** There's an article here.

**Ademilade Shodipe-dosunmu:** There are not that many articles for this particular keyword.

**Ademilade Shodipe-dosunmu:** Yep.

**Ademilade Shodipe-dosunmu:** I'm trying to find listicles.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** So nice listicle formats here.

**Ademilade Shodipe-dosunmu:** Yeah, I don't really like this article.

**Ademilade Shodipe-dosunmu:** I don't know why this article rungstumbed my word.

**Ademilade Shodipe-dosunmu:** I hate the formatting so much.

**Ademilade Shodipe-dosunmu:** All right.

**Ademilade Shodipe-dosunmu:** Some other articles here.

**Ademilade Shodipe-dosunmu:** Okay, so now I'm going to Claude, and we're just going to do a prompt change.

**Ademilade Shodipe-dosunmu:** So I'm going to start off with something like, so context, we were working on PSU templates for competitor comparisons earlier.

**Ademilade Shodipe-dosunmu:** And this is what we came up with for articles that fall under...

**Ademilade Shodipe-dosunmu:** Thank you.

**Ademilade Shodipe-dosunmu:** much.

**Ademilade Shodipe-dosunmu:** Thank you.

**Ademilade Shodipe-dosunmu:** Thanks.

**Ademilade Shodipe-dosunmu:** And when you go into the design project, you have access to this chat, so you don't have to remember this prompt or anything.

**Ademilade Shodipe-dosunmu:** Because I'm just coming up with it on the fly.

**Ademilade Shodipe-dosunmu:** So I'm going to drop in the articles that we had on that.

**Ademilade Shodipe-dosunmu:** So I always like to look up context first so that it knows where we're coming from, where we're going, all that good stuff.

**Ademilade Shodipe-dosunmu:** I've attached, sorry, the templates we came up with, as well as the article that was approved by clients, it's based on...

**Ademilade Shodipe-dosunmu:** ...

**Ademilade Shodipe-dosunmu:** So I'm not going to attach the ads code that was approved, which is this one.

**Ademilade Shodipe-dosunmu:** Last context.

**Ademilade Shodipe-dosunmu:** Now, we want to create a PSU template for another competitor cluster.

**Ademilade Shodipe-dosunmu:** This time for general best of listed goals.

**Ademilade Shodipe-dosunmu:** So I'm starting.

**Ademilade Shodipe-dosunmu:** Let's put that there.

**Ademilade Shodipe-dosunmu:** And now, let's just see, you know, let's just see how this goes.

**Ademilade Shodipe-dosunmu:** Let's just start off with this.

**Ademilade Shodipe-dosunmu:** And then we'll take it from there.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** So what I like about, like, when you context load up like this, is that, like, Claude actually sort of explains its reasoning.

**Ademilade Shodipe-dosunmu:** And then you can easily, like, poke holes in it.

**Ademilade Shodipe-dosunmu:** So if there's any reasoning that's off, you have to read a lot of these and figure out whether, like, oh, yeah.

**Ademilade Shodipe-dosunmu:** Okay, this is , like I didn't ask you to do that, or something.

**Ademilade Shodipe-dosunmu:** So, yeah.

**Pamela Weber:** Just one sec, I'll be right back, someone's at the door one sec, sorry.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** Thank you.

**Ademilade Shodipe-dosunmu:** Thank you.

**Ademilade Shodipe-dosunmu:** Thank Thank

**Ademilade Shodipe-dosunmu:** Thank you.

**Pamela Weber:** Okay, sorry about that.

**Pamela Weber:** I'm Okay, all good.

**Ademilade Shodipe-dosunmu:** So now, like, you have, like, a template here, right?

**Ademilade Shodipe-dosunmu:** And just, like, for you to note, like, you might, you definitely need to,

**Ademilade Shodipe-dosunmu:** You these depending on like if it's putting stuff that you generally don't need for whatever the case may be, right?

**Ademilade Shodipe-dosunmu:** But yeah, just as an example, I'm just going to copy this.

**Ademilade Shodipe-dosunmu:** So let me just say convert, yeah, move to markdown feeds.

**Ademilade Shodipe-dosunmu:** Just so that I can put that into the pipeline.

**Ademilade Shodipe-dosunmu:** So creating that file.

**Ademilade Shodipe-dosunmu:** So like this, we have one of the things we're looking for, which is the templates.

**Ademilade Shodipe-dosunmu:** So after the template, the next thing we need is the sample article, if that makes sense.

**Ademilade Shodipe-dosunmu:** All right, great.

**Ademilade Shodipe-dosunmu:** So we're going to create a sample article.

**Ademilade Shodipe-dosunmu:** Cause the sample article is pretty much, sorry, give me a sec.

**Ademilade Shodipe-dosunmu:** don't have any message.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** I don't have I don't have any message.

**Ademilade Shodipe-dosunmu:** So,

**Ademilade Shodipe-dosunmu:** The sample article pretty much gives the pipeline, oh, hey, this is how these articles are supposed to look, right?

**Ademilade Shodipe-dosunmu:** So, hey, you have a template that says, okay, this is you're supposed to cover, but like, hey, this is an approved article that sort of walks you through what you need, right?

**Ademilade Shodipe-dosunmu:** You know, that type of thing.

**Ademilade Shodipe-dosunmu:** So, I'm going into, so this is alternatives template, so we're going to need to create a new artifact here.

**Ademilade Shodipe-dosunmu:** So, I'm going to hop into here and create an artifact, and we're going to call it, so this artifact is going to be a rule, it has to be a rule, because it's template, and we want the workflow to follow it, so it's a rule.

**Ademilade Shodipe-dosunmu:** And the name for this one, we can call it, um, best, maybe best of, or best of, I'm so sorry, what's And then we get it before, I don't remember.

**Ademilade Shodipe-dosunmu:** All right, best platforms for pain points, so we're here, I'm just going to put that best platforms for pain points, template, yeah, that's log, all right, then we're going to paste in what we're getting for this, right, so for my artifacts here, I'm going to convert this to lockdown, copy it, then I'm going to put it here, remember this is just an example, ideally I would go through the entire cloud output and check and edit it extensively because of your artifacts determining the quality of content your pipeline gives you, so ideally you're supposed to go in there and edit all of that, but I'm just showing you an example of how to set it up so you can do it on your own, so I will now paste it on your own, that here.

**Ademilade Shodipe-dosunmu:** I don't think we need this.

**Ademilade Shodipe-dosunmu:** don't need to add sample topics here.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** This is mostly fine.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** Yeah, we're good here.

**Ademilade Shodipe-dosunmu:** So once you're done, you hit save.

**Ademilade Shodipe-dosunmu:** Save this.

**Ademilade Shodipe-dosunmu:** Yeah, create artifacts.

**Ademilade Shodipe-dosunmu:** So for best pain points, we have an artifact for this now.

**Ademilade Shodipe-dosunmu:** Remember I said we needed two things.

**Ademilade Shodipe-dosunmu:** We need an artifact, and we need a sample artifact.

**Ademilade Shodipe-dosunmu:** This is a different sample, I suppose.

**Ademilade Shodipe-dosunmu:** And sample artifacts fall on the...

**Ademilade Shodipe-dosunmu:** Over.

**Ademilade Shodipe-dosunmu:** Okay, other.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** Yeah, they fall on that other.

**Ademilade Shodipe-dosunmu:** So create artifacts is on that other, and we call this...

**Ademilade Shodipe-dosunmu:** The Well, best...

**Ademilade Shodipe-dosunmu:** Performs, oh, sorry, Best Platform for Pinpoint Sample, right?

**Ademilade Shodipe-dosunmu:** And this is where we'll the sample article.

**Ademilade Shodipe-dosunmu:** So now we're going to go back into Cloud.

**Ademilade Shodipe-dosunmu:** Since we have this, like I said, just an example.

**Ademilade Shodipe-dosunmu:** So we'll have this, based on this template, Meet Best Platform.

**Ademilade Shodipe-dosunmu:** So we're going to get one from the list, and Best Platform, so both.

**Ademilade Shodipe-dosunmu:** All right, and we're going to put that into Cloud.

**Ademilade Shodipe-dosunmu:** Because we need an example for the pipeline to know what it is.

**Ademilade Shodipe-dosunmu:** So let's what happens with these articles.

**Ademilade Shodipe-dosunmu:** Typically, in most cases, I would create the first sample out of Atlas.

**Ademilade Shodipe-dosunmu:** would do some perplexity research, some plot, all of that, create a really good article, send it to the client.

**Ademilade Shodipe-dosunmu:** The client approves it.

**Ademilade Shodipe-dosunmu:** Once we're done with that phase and the client has approved it, I will now bring that article as an example into Atlas.

**Ademilade Shodipe-dosunmu:** So Atlas knows what good looks like and add that as a sample.

**Ademilade Shodipe-dosunmu:** So, you don't have as much time now since the live call, but even though I'm skipping some steps, I still wanted you to know the entire proper process so that when you're doing it, can follow the right process.

**Pamela Weber:** And just the other thing, please, if you still have time after that to show me in your call, I still can't find where to put the meta and images and all that.

**Pamela Weber:** And then to how for my next stuff for next week about.

**Pamela Weber:** All that.

**Pamela Weber:** So those are my only other questions.

**Ademilade Shodipe-dosunmu:** Well, there's been another show you know, think, you know.

**Pamela Weber:** And for pipeline, if I put it into engineering, how long before the user can get it, like, done?

**Ademilade Shodipe-dosunmu:** Depends on, like, your request, honestly.

**Ademilade Shodipe-dosunmu:** If it's something simple, they can get it in, like, a day or two.

**Ademilade Shodipe-dosunmu:** Sometimes that's in the, depending on, like, how easy it is for them to get it done.

**Pamela Weber:** Are these simple, the ones that we're doing?

**Pamela Weber:** These look simple, right?

**Pamela Weber:** Uh, yeah, yeah, Okay.

**Pamela Weber:** simple fixes.

**Pamela Weber:** Okay.

**Pamela Weber:** Okay, is this, oh, good, yeah.

**Pamela Weber:** Okay, why, for some reason, I don't know, I looked everywhere, I didn't see where the field for meta and the image is a slug.

**Pamela Weber:** Okay.

**Ademilade Shodipe-dosunmu:** So it's gonna be here, so you just click this, um, you scroll down, and you find, so this is for the link, then this is for the slug.

**Pamela Weber:** Okay.

**Pamela Weber:** Kind of about

**Pamela Weber:** But I clicked on that and I didn't see it online, so I still don't.

**Pamela Weber:** Okay, I'll look again.

**Pamela Weber:** I remember clicking on that thing.

**Pamela Weber:** All right.

**Pamela Weber:** So that's in the little tooltip thing or whatever.

**Pamela Weber:** Yeah, exactly.

**Ademilade Shodipe-dosunmu:** Oh, I'm sorry.

**Pamela Weber:** I'll wait until you don't have all this and I'll ask my other Yoko stuff.

**Pamela Weber:** That's the only other thing.

**Pamela Weber:** Go ahead.

**Ademilade Shodipe-dosunmu:** I'm to get it.

**Ademilade Shodipe-dosunmu:** Yes, running that.

**Ademilade Shodipe-dosunmu:** don't know why it's taking so long.

**Ademilade Shodipe-dosunmu:** But the idea thing is that, like, you know, we need to create this so that we can edit this with the details.

**Ademilade Shodipe-dosunmu:** And the pipeline can be set up.

**Ademilade Shodipe-dosunmu:** But still, you're labeling.

**Ademilade Shodipe-dosunmu:** You don't to to like,

**Ademilade Shodipe-dosunmu:** How that's going on, like, you can just like ask me the Yurko stuff and yeah.

**Ademilade Shodipe-dosunmu:** Okay.

**Pamela Weber:** Then the other thing is, so, so for the articles for next week, those are the six I'm doing this week.

**Pamela Weber:** Yeah, we usually deliver one week ahead.

**Ademilade Shodipe-dosunmu:** So you would, all of this is already in the rooms I sent.

**Pamela Weber:** Okay.

**Pamela Weber:** No, no, we don't have to go with that.

**Pamela Weber:** Yeah, I'll, watch all those for sure.

**Pamela Weber:** I'm just trying to figure out the workflow for next week.

**Pamela Weber:** So, so discern.

**Ademilade Shodipe-dosunmu:** Remember that we swapped, we swapped a couple of these.

**Pamela Weber:** Yeah.

**Pamela Weber:** Yeah.

**Pamela Weber:** And then the Yurko, it's, it's that staging thing.

**Pamela Weber:** And then you're going to do that ticket about making that faster, I think.

**Pamela Weber:** Okay.

**Pamela Weber:** So staging.

**Pamela Weber:** And then, so it's six.

**Pamela Weber:** All right.

**Pamela Weber:** And then how do I get my next six so I can keep going?

**Pamela Weber:** Because I want to really get ahead on content.

**Pamela Weber:** Is it the same?

**Ademilade Shodipe-dosunmu:** Yeah, so it's all, it's all here.

**Ademilade Shodipe-dosunmu:** It's in the, it's in the loom.

**Ademilade Shodipe-dosunmu:** So I need a loom.

**Ademilade Shodipe-dosunmu:** Oh, okay.

**Pamela Weber:** That's one there too.

**Pamela Weber:** Yeah.

**Ademilade Shodipe-dosunmu:** Always confirm from Carrie before you start like contact with the next week because sometimes Jessica likes to come in and say, hey, let's swap these or let's add this or something like that.

**Ademilade Shodipe-dosunmu:** So, you know, it's always good to confirm.

**Ademilade Shodipe-dosunmu:** So you don't go ahead and do all that work and have to still do more.

**Ademilade Shodipe-dosunmu:** Okay.

**Pamela Weber:** Do you mind going up then?

**Pamela Weber:** Just one sec.

**Pamela Weber:** A little bit up.

**Pamela Weber:** Okay.

**Pamela Weber:** So I didn't toggle them.

**Pamela Weber:** So I think these are the ones, yeah, those are the ones I'm probably already in, right, already.

**Pamela Weber:** Probably.

**Pamela Weber:** Yeah.

**Pamela Weber:** I just didn't toggle it.

**Pamela Weber:** Okay.

**Pamela Weber:** So those look familiar.

**Pamela Weber:** I as much as was supposed to try to keep, like, the goggles out of it, so, like, you need to stop there and get goggles.

**Pamela Weber:** I was so lost in everything on it.

**Pamela Weber:** I didn't even do, like, things like that.

**Pamela Weber:** I was just trying to figure out what is where.

**Pamela Weber:** I was, like, in the wrong cloud, in the wrong pipeline, and nothing was, like, making sense.

**Pamela Weber:** So, yeah, I didn't even do these little details, but I'll definitely be on top of all that.

**Pamela Weber:** I'm a detail person.

**Pamela Weber:** I was just trying to get the big thing done to even figure out if it's worth it to go back to this.

**Pamela Weber:** I thought I was in the wrong place for a lot of time.

**Pamela Weber:** And then if we, so week two, so this is the next six.

**Pamela Weber:** Okay, got it.

**Pamela Weber:** So that

**Pamela Weber:** Oh, yeah, yeah.

**Ademilade Shodipe-dosunmu:** So, next six, next six.

**Ademilade Shodipe-dosunmu:** It's always, like, four weeks.

**Pamela Weber:** though.

**Pamela Weber:** I see five, though, the other one.

**Pamela Weber:** So, do I need to add one?

**Ademilade Shodipe-dosunmu:** Yeah, you probably need to add one more to this also.

**Pamela Weber:** And that's the same thing?

**Pamela Weber:** go to that draft thing to find another one?

**Pamela Weber:** Or I pull it from below?

**Ademilade Shodipe-dosunmu:** From this one, you remove them from pool.

**Ademilade Shodipe-dosunmu:** So, you go to pool, then you move all the data.

**Ademilade Shodipe-dosunmu:** You drag the audio around, you know, the right side of the screen.

**Ademilade Shodipe-dosunmu:** You have this data.

**Ademilade Shodipe-dosunmu:** you want to move something from the pool.

**Ademilade Shodipe-dosunmu:** So, you can move it to four weeks out, three weeks out, two weeks out, if move it up.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** Okay.

**Pamela Weber:** And then, do I need any pipelines for this?

**Pamela Weber:** Or the pipelines we have?

**Ademilade Shodipe-dosunmu:** Yeah, that's the agency one that you're currently using.

**Ademilade Shodipe-dosunmu:** Oh, talked about.

**Pamela Weber:** Okay.

**Pamela Weber:** So, that's it.

**Pamela Weber:** yeah, yeah.

**Pamela Weber:** So, I don't need a second one.

**Ademilade Shodipe-dosunmu:** Yes, you can run that and do any processing you need.

**Ademilade Shodipe-dosunmu:** But, like, if you need any or other, like, if you have any, they don't be confused about this editing.

**Ademilade Shodipe-dosunmu:** There you go.

**Ademilade Shodipe-dosunmu:** go.

**Ademilade Shodipe-dosunmu:** Just ask Kari, because she's the that sent it out.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** Yeah, I saw that right before this meeting, is what she said.

**Pamela Weber:** Okay.

**Ademilade Shodipe-dosunmu:** Yeah, so another way to step up to, like, just, like, around, like, how she prefers stuff to be done.

**Ademilade Shodipe-dosunmu:** So, you know, she's, like, the single source of truth for that.

**Pamela Weber:** Okay.

**Pamela Weber:** I think this guy should be done.

**Ademilade Shodipe-dosunmu:** Okay, so there's an answer here.

**Ademilade Shodipe-dosunmu:** Again, you know, also just assuming that, like, this is all correct, and, like, this looks good.

**Ademilade Shodipe-dosunmu:** Ideally, I'm not just going to copy content like this.

**Ademilade Shodipe-dosunmu:** I'm going to review it, edit it, make sure it's standard.

**Ademilade Shodipe-dosunmu:** But simply, around this point is, you know, you do your edits, you do all of the stuff that needs to be done, and you present this in your documents, do your internal linking, do everything that you need to do, honestly.

**Ademilade Shodipe-dosunmu:** Then we send this to the clients to review.

**Ademilade Shodipe-dosunmu:** So once the client reviews, the first article may be.

**Ademilade Shodipe-dosunmu:** But, however, we're not going to do that for this article because the client has already given us a benchmark for this competitor comparisons.

**Ademilade Shodipe-dosunmu:** Oh.

**Ademilade Shodipe-dosunmu:** That was the first one I did here.

**Ademilade Shodipe-dosunmu:** He gave us the benchmark, so we don't need to send this to him.

**Ademilade Shodipe-dosunmu:** But you do need to edit this and, you know, just make sure, like, it's good based off of, like, what we're trying to get done.

**Ademilade Shodipe-dosunmu:** And once we're sure that it's good and we've done all what we need, we're going to put that into this as an example.

**Ademilade Shodipe-dosunmu:** So the pipeline is, oh, hey, this is a good article that you can emulate for all your content needs.

**Ademilade Shodipe-dosunmu:** That is one, two, three, four, five, six.

**Ademilade Shodipe-dosunmu:** Okay, six platforms.

**Ademilade Shodipe-dosunmu:** This conclusion is probably a bit too long, but okay.

**Ademilade Shodipe-dosunmu:** This is just an example.

**Ademilade Shodipe-dosunmu:** So now we have our, you know, we have two things now.

**Ademilade Shodipe-dosunmu:** We have, I just want to bring up the two artifacts we just created.

**Ademilade Shodipe-dosunmu:** We have created best platform for pinpoints, this template, and we have created this sample.

**Ademilade Shodipe-dosunmu:** So, right, I remember that I said that the first two things we need for each article type, I mean, for each PSU pipeline is a

**Ademilade Shodipe-dosunmu:** Template, and an article sample.

**Ademilade Shodipe-dosunmu:** Once you have those two, we're pretty much golden, right?

**Ademilade Shodipe-dosunmu:** So here, now we can create a new pipeline.

**Ademilade Shodipe-dosunmu:** So we're hoping to go back into that programmatic pipeline that we copied from the other place, if remember, and we start making edits.

**Ademilade Shodipe-dosunmu:** So we go into, if you have changed the name already, we're going to change some of these artifacts.

**Ademilade Shodipe-dosunmu:** So you first come all the way down to, yeah.

**Ademilade Shodipe-dosunmu:** So here you're going to see goal.

**Ademilade Shodipe-dosunmu:** So the goal is to create an article with the following template.

**Ademilade Shodipe-dosunmu:** This is the alternatives template.

**Ademilade Shodipe-dosunmu:** So we need to change this to our new templates, right?

**Ademilade Shodipe-dosunmu:** And the good thing about the pipeline is that when you highlight something once, it's going to highlight the other cases of it appearing.

**Ademilade Shodipe-dosunmu:** So what I do here is that I'm going to take this.

**Ademilade Shodipe-dosunmu:** So I'm going to copy this.

**Ademilade Shodipe-dosunmu:** Sorry.

**Ademilade Shodipe-dosunmu:** Just the words.

**Ademilade Shodipe-dosunmu:** Copy this.

**Ademilade Shodipe-dosunmu:** I'm going to do a control H.

**Ademilade Shodipe-dosunmu:** Oh, darn.

**Ademilade Shodipe-dosunmu:** Sorry.

**Ademilade Shodipe-dosunmu:** I'm going to go with control F.

**Ademilade Shodipe-dosunmu:** The control F is here, so he's going to find it, and I'm going to get it to replace it.

**Ademilade Shodipe-dosunmu:** So all mentions of this alternative template, I want to replace it with this other template that I created.

**Ademilade Shodipe-dosunmu:** So I'm going to copy the name here, right?

**Ademilade Shodipe-dosunmu:** And I'm going to come here.

**Ademilade Shodipe-dosunmu:** I'm sorry, I don't know what happened then.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** Pinpoint template.

**Ademilade Shodipe-dosunmu:** Let me just remove this.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** So remove the extra.

**Ademilade Shodipe-dosunmu:** So best platforms for Pinpoint templates.

**Ademilade Shodipe-dosunmu:** I'm just going to replace all.

**Ademilade Shodipe-dosunmu:** Right.

**Ademilade Shodipe-dosunmu:** Right.

**Ademilade Shodipe-dosunmu:** Pretty simple.

**Ademilade Shodipe-dosunmu:** Then we're going to go up here.

**Ademilade Shodipe-dosunmu:** We're going to see that this has changed to best platforms for Pinpoint templates.

**Ademilade Shodipe-dosunmu:** So now it isn't correct templates, right?

**Ademilade Shodipe-dosunmu:** I'm actually making sense.

**Ademilade Shodipe-dosunmu:** So have lost you?

**Pamela Weber:** Yeah.

**Pamela Weber:** It's making sense.

**Pamela Weber:** Yeah.

**Pamela Weber:** Yeah.

**Pamela Weber:** Yeah.

**Pamela Weber:** Okay.

**Ademilade Shodipe-dosunmu:** Alright, so that's one.

**Ademilade Shodipe-dosunmu:** So we've changed the template.

**Ademilade Shodipe-dosunmu:** Now we need to change the sample.

**Ademilade Shodipe-dosunmu:** And the example is just right here, under Example Articles.

**Ademilade Shodipe-dosunmu:** So you're going to come here, copy this, do the same control here, and you're going to replace it with the sample that we have here.

**Ademilade Shodipe-dosunmu:** So I'll just copy the name of this artifact here, and I'm going to paste that here, and I'm going to replace all.

**Ademilade Shodipe-dosunmu:** And, yep, there we go.

**Ademilade Shodipe-dosunmu:** Then I'm going to go down and create pipeline.

**Ademilade Shodipe-dosunmu:** Pipeline created successfully, no errors whatsoever, so we're good.

**Ademilade Shodipe-dosunmu:** So now all you need to do is come in here, best platforms for pain points, add in your topic here.

**Ademilade Shodipe-dosunmu:** Put that there, create.

**Ademilade Shodipe-dosunmu:** And let it run.

**Ademilade Shodipe-dosunmu:** And see what the output gives you.

**Ademilade Shodipe-dosunmu:** You do that for all the topics that are under there.

**Ademilade Shodipe-dosunmu:** Then you rinse and repeat for the next one, and the next one.

**Ademilade Shodipe-dosunmu:** That's the typical approach to these articles.

**Ademilade Shodipe-dosunmu:** So this is how you can set up a PSA pipeline.

**Ademilade Shodipe-dosunmu:** So by the time you want to move to the other cluster we spoke about, so inside Ready to Draft, by the time you're moving to this cluster, sorry, me, you have this one, this private equity fund formation.

**Ademilade Shodipe-dosunmu:** You're going to need to create a new pipeline for this cluster.

**Ademilade Shodipe-dosunmu:** Then when you're done with this one, you're going to move to another pipeline called fund management.

**Ademilade Shodipe-dosunmu:** Sorry.

**Ademilade Shodipe-dosunmu:** I'm sorry, where are the, I'm using the wrong, okay, these are the clusters, yeah.

**Ademilade Shodipe-dosunmu:** So while that you're doing that first one, you're to, okay, so all of this is under fund management formation.

**Ademilade Shodipe-dosunmu:** When you're done with this, you're going to encounter.

**Ademilade Shodipe-dosunmu:** Oh, this is so old.

**Ademilade Shodipe-dosunmu:** That's everything on that fund management.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** There we go.

**Ademilade Shodipe-dosunmu:** Fund management.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** This is also a fund management.

**Ademilade Shodipe-dosunmu:** problem.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** So, yeah, you're going to create another one for industry-specific compliance and so on and so forth.

**Ademilade Shodipe-dosunmu:** With that, anytime you look at a new cluster, you need to create a new pipeline for it.

**Pamela Weber:** Okay.

**Pamela Weber:** when's the next one?

**Pamela Weber:** The is...

**Pamela Weber:** Oh, sorry.

**Pamela Weber:** Go ahead.

**Pamela Weber:** Yeah.

**Ademilade Shodipe-dosunmu:** next one I thought this is private equity fund information.

**Ademilade Shodipe-dosunmu:** probably two weeks or three?

**Pamela Weber:** Yeah.

**Pamela Weber:** In two weeks.

**Ademilade Shodipe-dosunmu:** So, the week after next week, you're going to work on these articles.

**Ademilade Shodipe-dosunmu:** So, ideally, sometime next week, if can find some time, you should put out, like, probably, I usually block out, like, two to three hours to create a new pipeline.

**Ademilade Shodipe-dosunmu:** And do research about the topic, find out the top-ranking articles, the types of details I want to be in my own article, and figure out how to create a sample article and send that over to the cloud.

**Ademilade Shodipe-dosunmu:** Then, based on this feedback, I fixed that, then used that sample as a tool to create a template, set up a pipeline, and take it from there.

**Ademilade Shodipe-dosunmu:** Okay.

**Pamela Weber:** Yeah, but you know, I don't think I'm going to have time to make these next two pipelines, so could you help me figure out how to do the ticket?

**Pamela Weber:** Would I need to give them the article sample and the template when you ask for a pipeline?

**Ademilade Shodipe-dosunmu:** Yeah, can tell them you want a new PSU pipeline for the CERN, and you need, and you send a visual artifacts you need, and a sample of the article.

**Ademilade Shodipe-dosunmu:** Yeah, you can do that from there.

**Ademilade Shodipe-dosunmu:** The sample and then the template is the other thing, right?

**Pamela Weber:** Yeah, sample and a template.

**Ademilade Shodipe-dosunmu:** So yeah, this is a template and this is a sample article.

**Pamela Weber:** Because after that, I mean, I want to do the pipelines, but I need to catch up on all this stuff, like, so to do one more thing, I'm not going to time these next few days.

**Pamela Weber:** I want to get ahead of everything, so just, you know, barely being where I am.

**Pamela Weber:** So then where do I send that ticket, or what is it in?

**Pamela Weber:** don't know if that's what

**Pamela Weber:** Linear?

**Ademilade Shodipe-dosunmu:** Yeah, so you go to Linear, and you go to here, Create Issue, and you choose Client Ops, CEPD, and you go to a Templates here, and you just tell them, so Workflow Requests, you just put that here, and sort of describe what you need to be created.

**Ademilade Shodipe-dosunmu:** I want to see if I can find, like, the last one that I needed to do.

**Pamela Weber:** And by the way, thank you for showing me all that, I mean, that's really valuable, and I'll use it when I make, hopefully the next one I'll do it for the next week.

**Pamela Weber:** But I'm like already so swamped, there's no, we're just going to work on the ones that I have pipelines for, and hopefully these will be done in the next day or two, and I can keep going.

**Ademilade Shodipe-dosunmu:** Yeah, no problem there, I'm just trying to find the, because it's been a while since I asked them to do.

**Pamela Weber:** I'll get there too, I'll get there, but just now with, yeah, I'm just trying to catch up to where I need to be.

**Ademilade Shodipe-dosunmu:** So like this one is support request, I don't know if this was closed.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** All right, yeah, so this was the last time I did this.

**Ademilade Shodipe-dosunmu:** Yeah, so I asked them, so this was it, custom PSEO pipelines.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** Yeah, so I'm just going to copy this link and send it to your next slide.

**Ademilade Shodipe-dosunmu:** Okay.

**Pamela Weber:** So I just edit that for this topic and add the article and template.

**Pamela Weber:** that.

**Pamela Weber:** have question, Thank you much.

**Pamela Weber:** You're

**Pamela Weber:** And then I have to tell it's like filing a ticket.

**Ademilade Shodipe-dosunmu:** No, no, it's automated.

**Ademilade Shodipe-dosunmu:** So like, once you file a ticket in CEPD, it's supposed to sell.

**Pamela Weber:** Okay.

**Pamela Weber:** And how do you know when it's done?

**Ademilade Shodipe-dosunmu:** They'll tag you.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** Yeah, they'll let you know.

**Ademilade Shodipe-dosunmu:** So, keep an eye on your linear, and, yeah, pick them up.

**Ademilade Shodipe-dosunmu:** So I created, I've created one for, I've created for this.

**Ademilade Shodipe-dosunmu:** Thank you, yeah.

**Ademilade Shodipe-dosunmu:** Already, so you have what you need for this, but like, you're going to need ones to run this one.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** These guys here are going to need for this one, too.

**Ademilade Shodipe-dosunmu:** And all of this is, and you're doing all of these next week as well.

**Ademilade Shodipe-dosunmu:** So, you're going to need that set up first, and you're going to need that before you, start working on the askers of your students.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** I'm going to ask today.

**Pamela Weber:** So hopefully it'll be like early next week.

**Pamela Weber:** They'll be done.

**Pamela Weber:** When are the articles due during the week?

**Pamela Weber:** Oh, I know it's actually in the task.

**Pamela Weber:** I'll go look.

**Ademilade Shodipe-dosunmu:** I didn't get that.

**Pamela Weber:** When are the articles due?

**Pamela Weber:** Every week?

**Ademilade Shodipe-dosunmu:** Just before the end of the week.

**Ademilade Shodipe-dosunmu:** I want to beat a lot of trust with the client.

**Ademilade Shodipe-dosunmu:** So he doesn't really babysit us for like deadlines and stuff.

**Ademilade Shodipe-dosunmu:** But you still have to get it done that week.

**Ademilade Shodipe-dosunmu:** So typically by Friday, you should have all your articles done.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** Well, I'm just thinking whenever the pipeline is.

**Pamela Weber:** definitely by Friday, hopefully earlier.

**Pamela Weber:** And Yorco?

**Ademilade Shodipe-dosunmu:** Yorco is different.

**Ademilade Shodipe-dosunmu:** You have to deliver by Wednesday.

**Ademilade Shodipe-dosunmu:** Oh, okay.

**Pamela Weber:** Yeah.

**Pamela Weber:** Like everything is.

**Ademilade Shodipe-dosunmu:** So like if you go into the internal channel, for example, let's see Yorco.

**Pamela Weber:** I've got the list.

**Pamela Weber:** Okay.

**Ademilade Shodipe-dosunmu:** So weekly, recurring.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** So this is my list.

**Ademilade Shodipe-dosunmu:** And you see that deliver the next batch of content to Jessica no later than Wednesday of the week.

**Ademilade Shodipe-dosunmu:** Prior to work.

**Ademilade Shodipe-dosunmu:** So that's Wednesday.

**Ademilade Shodipe-dosunmu:** Then Thursday, stage for the current week.

**Pamela Weber:** But I deliver to Jessica or I give it to Carrie because she's running the account and she gives it to her?

**Ademilade Shodipe-dosunmu:** So by deliver, what that means is you change the status to when you're done.

**Ademilade Shodipe-dosunmu:** For example, these ones, these have to be, ideally, these are all supposed to have been delivered by this week, Wednesday.

**Pamela Weber:** Because that's the content for the next week.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** but like, she understands that I got behind.

**Ademilade Shodipe-dosunmu:** So, I mean, if you're done with this one, so if Carrie is done, hopefully by Monday, you guys can send these out.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** Right?

**Ademilade Shodipe-dosunmu:** Then, like, you know.

**Ademilade Shodipe-dosunmu:** Oh, then I'm confused.

**Ademilade Shodipe-dosunmu:** I thought those were for next week.

**Pamela Weber:** Okay.

**Pamela Weber:** All right.

**Pamela Weber:** I got it.

**Ademilade Shodipe-dosunmu:** So, ideally, this is supposed to be a publishing schedule, not a delivery schedule.

**Pamela Weber:** So, it's like, this week, these guys have to be published, right?

**Ademilade Shodipe-dosunmu:** are published this week.

**Ademilade Shodipe-dosunmu:** So, next week, these guys have to be published.

**Ademilade Shodipe-dosunmu:** Right?

**Ademilade Shodipe-dosunmu:** Thanks, Thank

**Ademilade Shodipe-dosunmu:** And these guys have to be delivered.

**Ademilade Shodipe-dosunmu:** That's usually the arrangement.

**Ademilade Shodipe-dosunmu:** So it's a bit much now.

**Ademilade Shodipe-dosunmu:** you can ask Carrie for support.

**Ademilade Shodipe-dosunmu:** If you need contact on support or something, she can jump in if she has capacity.

**Ademilade Shodipe-dosunmu:** I would have jumped in to help you with a couple more of these, but I'm a bit strapped now.

**Ademilade Shodipe-dosunmu:** No, no, that's the point.

**Pamela Weber:** I'm just trying to figure out what to do when.

**Pamela Weber:** That's why.

**Pamela Weber:** I know I appreciate your help.

**Pamela Weber:** So this next week one.

**Pamela Weber:** So those, I'm going to finish the last three.

**Pamela Weber:** I was just waiting in which pipeline to know.

**Pamela Weber:** But I ran some last night.

**Pamela Weber:** so you could just like.

**Pamela Weber:** Yeah, I'll send them to you right after the call.

**Pamela Weber:** And then when you tell me they're good to go, then like you said, maybe have Carrie.

**Pamela Weber:** You want to Carrie look at it one more time.

**Pamela Weber:** And then I toggle that to ready.

**Pamela Weber:** What does it go to?

**Pamela Weber:** So she knows for Jessica.

**Pamela Weber:** You toggle it to.

**Ademilade Shodipe-dosunmu:** Just a client review when it's ready for her.

**Ademilade Shodipe-dosunmu:** I interview myself.

**Pamela Weber:** That's what deliver.

**Pamela Weber:** Yeah.

**Pamela Weber:** Okay.

**Ademilade Shodipe-dosunmu:** So that's deliver.

**Ademilade Shodipe-dosunmu:** So once it's there, you just let Carrie know on.

**Ademilade Shodipe-dosunmu:** But like, she can shoot videos,

**Ademilade Shodipe-dosunmu:** Also, for these other three, you can just send those directly to Kari, because I think you sent the last one to her as well.

**Pamela Weber:** So we can just send them.

**Pamela Weber:** Yeah, okay.

**Ademilade Shodipe-dosunmu:** We can just send directly to her, like Shigeru, because I won't have time to look at them today.

**Ademilade Shodipe-dosunmu:** Oh, maybe she put that to client reviews, is you or her?

**Pamela Weber:** Yeah, maybe one of them I sent, yeah.

**Ademilade Shodipe-dosunmu:** This was like the enriched one that like I edited.

**Pamela Weber:** Okay, I see you did that.

**Pamela Weber:** Okay, so at least we're not 100% behind.

**Pamela Weber:** And there's one that's already in.

**Pamela Weber:** Okay, that's good.

**Ademilade Shodipe-dosunmu:** have to switch this to LDR because of the new formats that she sort of acts for.

**Pamela Weber:** Yeah, yeah.

**Ademilade Shodipe-dosunmu:** So I have to change this to like irregular, like TLO, LDR, at the top of the article, and in paragraph.

**Ademilade Shodipe-dosunmu:** So I'll just add that up.

**Ademilade Shodipe-dosunmu:** thought was cool.

**Ademilade Shodipe-dosunmu:** Yeah.

**Pamela Weber:** Great.

**Pamela Weber:** Cool.

**Pamela Weber:** Thank you.

**Pamela Weber:** No problem.

**Pamela Weber:** problem.

**Ademilade Shodipe-dosunmu:** But let me know if you need anything, and yeah, we can chat during the week.

**Ademilade Shodipe-dosunmu:** Yeah, just like go through like the weekly, the daily checklist, and let me know if like you're behind or you need support and all, because we have to flag things early so that production share doesn't go, you know, behind.

**Ademilade Shodipe-dosunmu:** Yeah, for sure.

**Ademilade Shodipe-dosunmu:** Yeah, I didn't realize that.

**Pamela Weber:** I thought, yeah, okay, I got it.

**Pamela Weber:** I'll go look and see what's going on.

**Pamela Weber:** I thought everything was on track, so I'll get there.

**Pamela Weber:** Thank you for all your help.

**Pamela Weber:** I appreciate it.

**Pamela Weber:** Have a good one.

**Pamela Weber:** Thanks.

**Pamela Weber:** Have a good weekend.

**Pamela Weber:** Bye.
