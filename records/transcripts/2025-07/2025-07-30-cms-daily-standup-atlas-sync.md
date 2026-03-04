# CMs Daily Standup – Atlas Sync

<metadata>
date: 2025-07-30
time: 15:27 UTC
duration: 35 minutes
organizer: Saskia Wartnaby
participants: Mariana Marins, Matthew Panzarino, Sucheta Biswas, Tiandra Burns, Josip Sovar, Saskia Wartnaby
fathom_recording_id: 77421816
fathom_url: https://fathom.video/calls/365278813
share_url: https://fathom.video/share/A-KJ5ShTpf7LxTxNU57ybo9hzHUH5-E4
source: fathom
enriched_on: 2026-03-03 12:30 UTC
</metadata>

---

## Summary

GrowthX's content management team met to surface and troubleshoot recurring issues with the Atlas platform—covering keyword selection, article generation workflows, fact-checking configuration, and product context engineering. Matthew Panzarino explained how competitor keywords appear due to SERP analysis limitations, outlined the rationale behind article direction inconsistencies, and clarified that detailed product information should live in company context with strong structure rather than scattered across multiple artifacts. The team committed to filing tickets for known bugs (Atlas refresh loops, AI shortcuts not applying, bullet point generation) while Matthew emphasized that many of these will be addressed by upcoming agentic rewrites of both the assignment and article generation workflows.

---

## Context

This is an internal GrowthX standup for the content management (CMs) team who use the Atlas platform to execute the content production workflow. Atlas is a proprietary system that orchestrates keyword research, article direction, fact-checking, and article generation for clients. The meeting was facilitated by Mariana Marins with technical guidance from Matthew Panzarino (who built and maintains many of the underlying workflows). The team surfaced pain points encountered during daily work—things that are slowing them down or causing confusion—and Panzarino provided clarity on how the system actually works versus how CMs expect it to work. This level of transparency and troubleshooting is critical because the CMs are the validators of whether patches and updates work as intended; at a startup stage without automated validators, they serve as the QA layer.

---

## Relevance

- **To GrowthX Delivery:** Competitor keywords occasionally leak into assignment briefs due to SERP analysis limitations with low-volume keywords—an acceptable edge case unless clients explicitly forbid competitor mentions. Article direction sometimes ignores specified directions when edge-case parameters are met; requires manual fixes or ticket filing if pervasive. Bullet point generation is suppressed in the current workflow (known issue) but will be resolved in the agentic rewrite. Company context works best when well-structured and clear; avoid dumping raw feature lists—structure them as digestible sections under company context rather than creating separate artifacts unless extreme (Biologica's 40+ ingredients with deep cross-references).

- **To CheckThat:** Context engineering is a critical next frontier. The meeting highlighted how LLM token windows are no longer the constraint—clarity and structure are. Model performance depends on how artifacts are written, organized, and ingested by workflows, not on raw size.

- **To GrowthX Business Development:** CMs are catching bugs and validating patches in real time. Rapid ticket filing (refresh loops, AI shortcuts, outline consistency) shows healthy product feedback loops and team visibility into pain points. Address these with near-term hotfixes and road map transparency.

---

## Overview

- Competitor keywords may appear in results from zero/low-volume keywords; generally not a blocking issue unless client explicitly forbids competitor mentions
- Research is driven by brief sections, not primary keyword; article generation can be influenced by primary keyword, so swap if it's a competitor keyword
- Article directions generally work but occasionally ignore specified directions; file a ticket if it happens consistently (not just once in a while)
- Fact-checking only accepts top-level domains, not URLs or specific pages; for private/unlisted knowledge bases, use Cloud projects as a workaround and file a ticket for integration
- Company context works best when well-structured; avoid overwhelming detail—clarity and crisp formatting matter more than token count
- Custom workflows like Biologica's mention injector can be built for high-volume product catalogs (40+ items); use style adapters to inject mentions post-generation
- Known issues: Atlas refresh loops (need habitual refresh after certain tasks), AI shortcuts not applying without refresh, bullet point suppression in current workflow
- All three issues will be addressed by upcoming agentic rewrites of assignment generation (coming in 1-2 weeks) and article generation workflows (in progress)

---

## Key Topics

### Keyword Selection and Competitor Keywords

  - Competitor keywords occasionally appear due to SERP analysis
  - Not a major issue unless explicitly forbidden by client
  - New assignment generation workflow coming soon may address this

### Article Direction and Outline Generation

  - Generally working well, but occasional generic outlines still occur
  - File a ticket if article directions are consistently ignored
  - New agentic assignment generation process in development

### Fact Domain Checking

  - Only accepts top-level domains, not specific URLs
  - Can include up to 10 domains for fact-checking
  - For non-public knowledge bases, consider using Cloud projects temporarily

### Context Engineering and Product Information

  - Company context can include detailed product descriptions
  - Well-structured, clear context is crucial for effective use
  - For extensive feature lists, custom style adapter workflows can be created

### Custom Workflows for Specific Clients

  - Example: Biologica's mention review workflow
  - Injects brand mentions and specific ingredients into articles
  - Demonstrates ability to adapt articles post-generation

### Current Issues and Upcoming Fixes

  - Bullet point generation currently limited; fix coming with new workflow
  - AI shortcut application not working properly for some users
  - Article generation workflow being rebuilt with agentic approach

---

## Action Items

**Mariana Marins (GrowthX)**
- Check if ticket exists for Atlas refresh issue; file if not

**Matthew Panzarino (GrowthX)**
- File ticket for Yurko help site fact-checking workflow addition

**Tiandra Burns (GrowthX)**
- File ticket for AI shortcuts not applying without refresh in Atlas

---

## Transcript

**Mariana Marins:** Thank you. Two people here. Are you listening to me?

**Mariana Marins:** Okay, cool. So Matthew will be one minute late, but he is coming. So before he arrives, let me just ask you something. Is there anything that you would like to share regarding Atlas, etc.? Because I've prepared a PowerPoint, but I can include something now if you have anything.

**Mariana Marins:** If you want, just drop it in the chat and I can pick it up from there. Let me see who's here. Hello, Josip, Yana, Saskia, Sucheta, Usman, Jenny, and Bisera. Okay, cool. So, let's wait just one more minute.

**Mariana Marins:** Ah, Matthew is here. Okay, I think we can start because Sucheta is here.

**Mariana Marins:** Okay, so Panzar, do you want to say anything before we start?

**Matthew Panzarino:** No, not really. We can just get going.

**Mariana Marins:** Oh, just a second, guys. I see now that my headphones aren't actually connected here. Sorry.

**Matthew Panzarino:** No worries. Morning. Yeah, we can get rolling.

**Matthew Panzarino:** Do you want to just pull up a slideshow? We can work through from there and use that as a jumping off point, and then we can tackle anybody who didn't have a chance to speak up. The point of asking people to prepare topics in advance is to make sure these standups are focused and valuable. You never know when somebody else is running up against the same thing you are, right? But I want to make sure we use this time wisely in ways that are more valuable than you just doing your own work. So, in the future, if you have any issues, please submit them in advance so I can do advance work to figure out answers to your questions. If I'm totally clueless about what you're running up against, I can investigate. So, just flagging it.

**Mariana Marins:** Okay, so let's go. We're going to talk about some issues that you guys shared with us in Slack. In the end, if you want to share anything else, please feel free. We want to know what's blocking your work, what you think is slowing you down. Especially what keeps coming up and feels frustrating and confusing—because if it's happening a lot, maybe we should just file a ticket for that, right?

**Mariana Marins:** The first thing was two things about keyword and article direction from Sucheta. The first thing she said was that competitor keywords were picked up in the workflow. Has this happened to anyone else? Or do you guys think this is just a fluke?

**Mariana Marins:** I'm assuming the keywords that you guys are picking up are the only keywords from the clients that you need. Everything is working, right?

**Matthew Panzarino:** Okay, I can interject a little bit on why this happens sometimes.

**Matthew Panzarino:** For some clients, given the ranking of a particular keyword, there may not be enough information about that keyword. Let's say it's a zero-volume or low-volume keyword where it can't find enough competitive articles. It may bleed into a competitor keyword. There's not a whole lot we can do about it because it's just how aggressive the system is trying to pick up results for you. It's saying, "I went out to look for these keywords that are related to this according to the assignment brief, and all I could find was this hyper-focused competitor keyword." It's just a by-product of the way SERP analysis is done.

**Matthew Panzarino:** Unless it becomes a huge problem, just keep an eye on it and weed them out if the client doesn't want them in there. It's not necessarily a bad thing that a competitor keyword appears unless the client explicitly says, "Never, ever mention our competitors"—which some of them do. And if that's the case, then you just need to make sure it doesn't make its way from the brief into the outline or into the article. It's okay if we use it for reference because a competitor reference article is a valid keyword referential to make sure your article is ranking for that keyword.

**Matthew Panzarino:** The reason I'm not too stressed about this, especially if it's happening rarely, is because we're undergoing a rebuild of the assignment generation workflow right now. That will be new very soon. It won't work the same way as it does now. So there's a branch here: if this is a really big issue that's blocking or causing major workflow issues right now, let's tackle it. But in a week or two, we might have a completely new assignment generation workflow. So I don't want to spend too much time on the old stuff.

**Matthew Panzarino:** On refreshing—yeah, you've got to click out, in, and out, or refresh. None of the tasks, unless there's a plug-up, are usually taking longer than five to seven minutes. Some, like research, take a little longer. But if you find it clogging up, you can just refresh. This is a known bug. I believe there's already a ticket on it, so we'll get around to fixing that. But for now, just run several articles at once and refresh in a couple minutes to see where you're at. That's a habitual refresh, unfortunately—probably the answer.

**Matthew Panzarino:** On how much the research stage and article generation are influenced by the main keyword in the assignment brief: the researcher is influenced by the bulk of the brief. It goes through and takes the brief in chunks, then does research on each chunk to make sure you have enough information to write about those topics. It pulls back research on that chunk and assembles it into a dossier that the workflow references to write sections. So it's not really primarily influenced by the main keyword. It's influenced by the sections of the brief that are fed into the workflow.

**Matthew Panzarino:** Now, the article generation—it can be influenced by the main keyword, so I would keep an eye on that. If the main keyword is a competitor keyword, you might want to swap that out or ask for a new one.

**Matthew Panzarino:** Yeah, it is frustrating to have to refresh all the time. I agree. Let's make sure there's a ticket filed on that. I'm almost positive there is, but we'll double-check.

**Mariana Marins:** I have to check. We talked about this, right?

**Matthew Panzarino:** But I forgot to actually go look for it. I'll do that.

**Mariana Marins:** So, coming back to keywords from Sucheta, sometimes the target keyword in the assignment brief is either totally different or it's undefined.

**Matthew Panzarino:** Different from what?

**Sucheta Biswas:** Different from what we do normally. We give the keyword in the title, but when the assignment brief is generated, it strays quite far from the actual keyword we want. Or it's not near the keyword we want to put, or it just says "not defined" or "undefined target keyword." So this sometimes crops up, and we just have to manually change it.

**Matthew Panzarino:** Yeah, that definitely fits with how the research is done. The keyword researcher workflow's job is to figure out what's actually ranking. There are parameters there—it's not just "find the top one" or "match this exactly." It has parameters because, for example, if you're looking at "best healthcare apps for iPhone" and iPhone is the keyword, you're never going to win that. The client usually won't. So it defaults to a keyword that fits in that cloud or in the research. It goes into SEMrush, says "iPhone," does research based on that, finds one that maps with healthcare, and may spit something out. Eight times out of ten, it's completely logical. You look at it and think, "it makes sense." But there are edge cases where a keyword comes back and you're like, "how did it come up with this?" It's probably something you just have to change because it's a researcher, not an answer machine. It doesn't spit out exact parameters or exact answers that you asked for. You're asking it to give you an opinion based on a set of parameters and rankings. Those parameters can be better, but that's how it works.

**Sucheta Biswas:** Understood. It works.

**Matthew Panzarino:** Thank you.

**Mariana Marins:** Now, article direction. Article direction is always the star, right? The outline works like a charm most of the times, but sometimes it still generates the most popular outlines for a guide—like a five-point checklist before getting started. So how do we tell article direction to actually work?

**Matthew Panzarino:** There's two things here. One: if it's working most of the time for you, it's probably working as well as it's going to work right now. If it every once in a while spits out common pitfalls or a top-five checklist, I'd say just edit it out and move on. If it's working most of the time, that's fine. However, if it's not working most of the time—if that's flipped—file a ticket because Saskia ran into this. We jumped on a call with her, and when I checked, we could see it was ignoring the article directions, even though we ran that update to the engine that was supposed to make article directions adhere in all cases.

**Matthew Panzarino:** If you're finding it's not adhering, file a ticket, because we have to individually look at the pipeline to make sure the update was applied correctly. There's currently no validator that ensures updates are working as intended. This is startup stuff. Normally in a big company, you'd have code validators and validators to make sure patches rolled out correctly. We don't at the moment. So you are our validators. Welcome to your job. But if you find a major flaw where it's not adhering to article directions, file a ticket. I'm talking about most of the time, not once in a while—that's just expected.

**Matthew Panzarino:** This connects to what I mentioned earlier: we're creating a new version of the assignment generation—the brief process—that will be agentic in nature, more like how Cloud projects work. We're working on it. It won't ship tomorrow, but it's coming soon. So file a bug fix if it's blocking you. Otherwise, let's cruise for a bit because we're working on changing that whole process.

**Mariana Marins:** Do you guys have anything else to talk about article direction before we move on?

**Mariana Marins:** Okay, so let's go.

**Mariana Marins:** Fact domain to check. This is in the first step when we're creating the brief, right? Are you guys using this field? What domains are you putting there? And did you know you can feed it up to 10 entries?

**Matthew Panzarino:** I want to clarify something really quickly. This field works with top-level domains only. So technically, saying you can feed it up to 10 URLs is incorrect. You cannot feed it URLs; you can feed it domains. If you've got a slash in there with stuff after it, it's going to ignore it. It will just take the top-level domain. I want to be clear because if you're looking for it to reference a specific database or page—say, a list of auto parts manufacturers—it won't do that. It will only look at the entire domain. It may find that subpage through the process of crawling that top-level domain, so it's worth trying. Right now, it does not take a URL. It only takes a domain. For example, for Discern, we're feeding it .gov domains for various states, and that works well. There are other top-level domains that would be valid for you to check. I just don't want you frustrated thinking it's not looking at a specific page. Well, it won't at the moment.

**Mariana Marins:** I was actually doing it wrong, then. I was putting a URL, not a domain.

**Matthew Panzarino:** Yeah, it would just take the top-level domain. It only uses that for fact-checking. It does not use that for limiting research. Right now, there's no way to limit research to a specific domain.

**Josip Sovar:** I have one question, if it's okay.

**Matthew Panzarino:** Yeah, of course.

**Josip Sovar:** So our client asked us to place a help site in fact-checking along with the Yurko domain. I was wondering if that's in vain—basically, is it being checked?

**Matthew Panzarino:** Yeah, it's ignoring it. Is the help site the same domain?

**Josip Sovar:** It's like Yurko, just with "help" first, then Yurko at...

**Matthew Panzarino:** Is it a knowledge base, like their help page?

**Josip Sovar:** Yeah, it's a knowledge base, but it's not in the public domain. If I go on their site, I can see it.

**Matthew Panzarino:** Is it public but not listed, or is it literally...

**Josip Sovar:** Yeah, public but not listed. It exists on their site, but we can't find it if we search their site at the moment.

**Matthew Panzarino:** Okay, here's a workaround for this. Download the entire page, scrape it, put it in a Cloud project, and run the article against it for now. Then we'll file a ticket to add an additional fact checker—basically a style adapter that takes that information and runs it against the article content with that knowledge base as the artifact.

**Josip Sovar:** Yeah, we actually did that in Cloud. I found every use case on their site and compiled it in an Ocean doc, so we have a knowledge base there. We run it through Cloud.

**Matthew Panzarino:** Yeah, that's good. I'll file a ticket so we can make it part of the workflow. Then you won't have to run it through Cloud.

**Josip Sovar:** Okay.

**Mariana Marins:** Okay, cool. Anything else regarding fact domain to chat?

**Mariana Marins:** How much context is too much context? When we're setting up the pipeline to start working, should you require a separate artifact to describe product functionality and add it to the pipeline, or can I add a ton of product info to the company context? Or would that slow everything down and confuse the model? When we're starting, do we just write a little sentence and call the AI, or do we exhaust it and write a whole prompt?

**Matthew Panzarino:** Okay, there are a couple answers here. The simplest answer is: put it into company context. You can put detailed product descriptions and feature descriptions there, and it will generally pull them fairly well. I've seen it happen live—like, "your code's real-time translations feature does X, Y, and Z and does it 20% faster than competitors." It will pull those mentions contextually. The LLM context windows are enormous now, so it's not too much information.

**Matthew Panzarino:** The asterisk is: your company context needs to be well-structured. It needs to be very clear, crisp, and well-structured. Look at clients coming out of Sprint for examples. It still requires clarity. You can't just dump a feature set in there. You have to set it up properly. Put it in company context, not in writing guidelines, because writing guidelines are about editing. Company context is for establishing context.

**Matthew Panzarino:** The short version: put it in company context. However, there's a case in Biologica where we're working with 40 ingredients and a lot of detail about what products they're in, benefits, brand names, etc. If you want those applied organically into the article, there's a case for including a style adapter workflow that takes that list as an artifact and applies it to the drafted article before fact-checking. We're doing this for Biologica for the first time. Try company context for now, and you can file a ticket if it doesn't work or if you find it's very inconsistent and not mentioning products.

**Matthew Panzarino:** Context engineering is our next big hurdle. It's about how artifacts are structured, written, ingested, and interpreted by workflows. Token windows are no longer an issue. Any company context you have is far smaller than the research, and research fits inside the token window. Don't worry about length; worry about clarity and structure. Keep it crisp, write it well, put it in company context, and see where you stand. If you find you're manually injecting product mentions or using Cloud projects to do so, then we can build a workflow, insert it into your pipeline, and call that list as an artifact.

**Mariana Marins:** I'm going to share the Biologica pipeline so you can see what it looks like when we have this other artifact. They're in the business of vitamins for women. When the pipeline pulls context, it's going to find all kinds of ingredients related to vitamins for women, but they only want their specific ingredients mentioned. For example, if one general vitamin has five ingredients but theirs only has three, they only want those three mentioned. What this workflow does is remove the other ingredients and focus only on the ones that actually exist in their product. Am I correct, Penzo?

**Matthew Panzarino:** Not quite. That process is the one we're building. Right now it's a Claude project being productized by Pedro. What this one does is similar but different. It actually injects mentions of Biologica into the article with those ingredients, brand-named, because they want the brand names. They want "Afron" in there with a trademark, not just generic "Saffron." It takes the article and if it doesn't mention Biologica's Midlife Essentials product with Afron Saffron, it sticks it in where necessary. It's an injector that puts mentions in—basically a CTA injector. It demonstrates that we can take an article that's not properly adapted and adapt it by injecting mentions. They want one version with all products mentioned and another with ingredients mentioned.

**Matthew Panzarino:** There's a case for using a style adapter like this to inject specific product features where necessary. This isn't applicable to all clients. Some are writing marketing copy and want more features mentioned. But some clients say, "Don't mention us until the very end—we just want educational content." In that case, this wouldn't be valuable. But it can be done. We can build anything you want. You have to start thinking of these pipelines as malleable. They're not set in stone; they're modular. Each workflow exists in a library. There's a library of workflows, and we're only using six of them. So we can build more and inject them where necessary. If you're running into something recurring, and you're frustrated, and it's lengthening your editing time, file a ticket so we can build a workflow for it.

**Mariana Marins:** Do you guys have any other issues or things that are going on that you would like to bring up?

**Tiandra Burns:** I am. I don't know if anyone else is having this problem, but when I use the Ask AI feature—the AI shortcuts portion—it's not actually applying it. So I have to go into Ask AI and do it that way. Luckily, now our AI is really good, so it's generating well. I don't have to use shortcuts as much, but I'm just not able to apply those shortcuts when I would like to. I looked on Linear and didn't see anything, so I'll file a ticket. Maybe it could be just me.

**Matthew Panzarino:** Yeah, we should definitely file a ticket for that, because you shouldn't have to refresh after using a shortcut. Let's make sure we file a ticket for that. Brad will know to work on it.

**Timmy:** I don't know if this has been talked about, but for some reason I still don't get enough bullets in the articles. Is this going to be fixed?

**Matthew Panzarino:** Yeah, you will. This is definitely a known issue. The current article generation workflow is producing big blocks of text and sort of banning bullet points. That wasn't the intention. You all remember when we had the opposite problem—just a bunch of bullets with no prose. So we're on the opposite end of the scale now, but we'll fix it. Daniel is rebuilding the article generation workflow with an agentic approach, which means it will call all the context every time and put it together much more like a Cloud project does. That's a big change, and I'll be testing it first. Until then, we have to reflow bullets where necessary. Otherwise it's a question of resources: do we focus all engineering on fixing the bullet point issue, or do we get the big new version out the door, which is going to be a lot better? I think we should focus on that.

**Mariana Marins:** Anything else? Okay, so if you guys don't have anything else, Panzar, do you have anything else to say?

**Matthew Panzarino:** Not at the moment.

**Mariana Marins:** Okay, I think we can call it quits.

**Matthew Panzarino:** Sounds good.

**Mariana Marins:** Okay, we'll see you next week. Bye, guys.

**Saskia Wartnaby:** Bye.
