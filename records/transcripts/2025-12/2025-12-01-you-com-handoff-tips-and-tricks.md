# You.com handoff - Tips and Tricks

<metadata>
date: 2025-12-01
time: 14:00 UTC
duration: 33 minutes
organizer: Bailey Seybolt
participants: Aida Knezevic, Bailey Seybolt, Gabrielle Brogan, Iana Medvedeva, Tamara Luzajic
fathom_recording_id: 105180900
fathom_url: https://fathom.video/calls/485423828
share_url: https://fathom.video/share/nnXavidjLM4hRb_2VMUCgtoRpoPsmigB
source: fathom
enriched_on: 2026-03-01 18:45 UTC
</metadata>

---

## Summary

GrowthX's You.com content team walked Iana through their end-to-end content generation and post-processing workflow in preparation for her takeover next week. The team discussed how to structure outlines (using SERP + Claude), apply post-processing prompts to clean up Agentec output and humanize tone, and manage client feedback from Brooke—who had flagged early drafts as too robotic. The team identified a critical insight: updating internal Atlas artifacts (Company Context, audience personas) to match the client's desired writing style can cut post-processing time in half, a strategy that proved successful on the Logic account.

---

## Context

You.com is a B2B SaaS client that recently pivoted from a consumer AI app to an enterprise-focused search tool and embedded search API. GrowthX is delivering content marketing to build organic visibility for their new enterprise products, which are currently invisible on search for high-value keywords. Brooke, You.com's Head of Content Marketing, is the primary point of contact—highly engaged but often stretched thin and sometimes slow to review deliverables. The engagement is strong enough that Brooke has already brought a Phase 2 expansion to her procurement team, signaling serious intent to scale beyond the current 5 articles per week commitment.

---

## Relevance

**To GrowthX Delivery:**
- Artifact overhaul (Company Context, audience personas) is a high-leverage process fix that replicates Logic account success and can cut post-processing time by 50%. Applicable across all Agentec clients.
- Two-prompt post-processing system (cleanup + style) is now standardized for You.com; should be documented and shared with other teams using Agentec.
- Atlas generation time is stable at ~1 hour per article for deliverable-quality output, suggesting the workflow is scalable for 5+ articles per week.

**To GrowthX Business Development:**
- You.com has strong expansion signals: Brooke already discussed Phase 2 with procurement and expressed interest in programmatic content strategies beyond the current editorial sprint.
- Client engagement is high (Brooke cares about quality), mitigating sprint delay risk. Historical pattern: engaged clients move through sprints faster than less-invested clients.
- Potential upsell: programmatic content (PSCO) flagged as a separate package for Phase 2 discussion.

**To GrowthX Team Capacity:**
- You.com handoff to Iana this week (observation) and next week (takeover) is on track. Clear workflow documentation and prompt library provided.
- SpectreOps sprint extension pending Andy's decision; affects editing capacity allocation for Gabrielle this week.

---

## Overview

- **You.com Pivot:** The company pivoted from a consumer app to an enterprise search tool and search API. Content must target one product specifically to avoid confusing the audience and address their low organic visibility for enterprise keywords.
- **Agentec Refinement:** Initial Agentec drafts were flagged by the client for a "robotic" tone and repetition. The team has since refined the post-processing workflow and created prompts to ensure a more human, conversational style.
- **Critical Process Fix:** To improve Agentec output quality, the team will rewrite all internal artifacts (e.g., Company Context) to match the client's desired tone. This fix, proven on the Logic account, is expected to cut post-processing time in half.
- **Handoff Plan:** Iana will observe the current team's workflow this week (Week 8) before taking over content generation for You.com next week. SpectreOps' status is pending a decision from Andy.

---

## Key Topics

### You.com Context & Strategy

  - **Company Pivot:** You.com shifted from a consumer app to an enterprise search tool and a search API.
  - **Strategic Challenge:** Low organic visibility for enterprise keywords.
  - **Content Goal:** Build authority for the new enterprise products.
  - **Key Insight:** Enterprises often have a specific problem (e.g., searchable customer support tickets) but don't know they need a search API. Content should address these problems directly.
  - **Client Contact:** Brooke (Head of Content Marketing) is the primary contact.
      - **Engagement:** Highly engaged and cares about the work, but often busy.
      - **Communication:** Requires occasional follow-ups (e.g., tags) to ensure timely reviews.
      - **Future:** Has already discussed a Phase 2 transition with procurement, signaling a strong intent to scale.

### Agentec Workflow & Refinements

  - **Initial Feedback:** Brooke flagged early drafts for a "robotic" tone, repetition, and non-human phrasing.
  - **Refinement 1: Post-Processing Workflow**
      - **Generation:** Use simple outlines (SERP + Claude) in Atlas.
      - **Editing:** Post-processing takes \~1 hour per article.
      - **Prompt Library:** Use two prompts based on Brooke's feedback:
        1.  **Cleanup:** Removes AI patterns, vague language, and repetitions.
        2.  **Style:** Focuses on humanizing the tone (e.g., varied sentence structure, conversational phrases).
      - **Key Risk:** The humanizing prompts can make the tone "AI casual" (e.g., "Here's what it means"), which must be edited out.
  - **Refinement 2: Artifact Overhaul (New Initiative)**
      - **Problem:** Atlas mimics the tone of its source artifacts (e.g., Company Context), which are written in a generic "corporate SaaS" style.
      - **Solution:** Rewrite all artifacts to match the client's desired tone, using their writing guidelines and a preferred article as a style guide.
      - **Rationale:** This fix, proven on the Logic account, is expected to cut post-processing time in half.

### Handoff & Team Capacity

  - **You.com Handoff:**
      - **This Week (Week 8):** The current team will generate and edit content. Iana will observe the process.
      - **Next Week:** Iana will take over content generation.
  - **SpectreOps Status:**
      - **Request:** SpectreOps requested a sprint extension to calibrate their new product manager, who joined mid-sprint and has extensive feedback.
      - **Pending Decision:** Andy will decide how to manage the extended sprint.
  - **Team Capacity:**
      - Gabrielle's workload is already full for the week (Fleet, Field Guide, Redis).
      - Gabrielle will ask Andy in the sprint channel to clarify who is responsible for editing You.com and SpectreOps content this week.

---

## Action Items

**Bailey Seybolt (GrowthX)**
- Follow up in Linear re: you.com programmatic strategy ticket

**Tamara Luzajic (GrowthX)**
- Share you.com handoff materials w/ Iana: Agentec artifacts, prompt library, Claude project link
- Update you.com Atlas artifacts to match writing guidelines/approved tone
- Generate you.com content this week (5 articles); Iana shadow

**Gabrielle Brogan (GrowthX)**
- Add your editing prompts to you.com prompt library
- Message Andy in sprint channel re: you.com/SpectreOps editing this week; await decision

**Aida Knezevic (GrowthX)**
- Update sprint tracker re: Bailey joining you.com/SpectreOps syncs

---

## Transcript
**Bailey Seybolt:** Hello, morning, everyone, or whatever time it is for you.

**Tamara Luzajic:** For me?

**Tamara Luzajic:** It's three weekends here.

**Tamara Luzajic:** Is it early for you guys?

**Bailey Seybolt:** I always forget.

**Bailey Seybolt:** It's the start of my day.

**Bailey Seybolt:** It's like nine here.

**Tamara Luzajic:** Oh, okay.

**Tamara Luzajic:** That's not too dramatic.

**Bailey Seybolt:** Yeah, haven't seen you since your wedding.

**Tamara Luzajic:** How was it?

**Tamara Luzajic:** Yes, it was really, really nice.

**Tamara Luzajic:** Thank you so much for asking.

**Bailey Seybolt:** It was really lovely.

**Bailey Seybolt:** Congratulations.

**Tamara Luzajic:** Thank you.

**Bailey Seybolt:** Thank you.

**Bailey Seybolt:** Did you take a trip or something after?

**Tamara Luzajic:** Did you get to celebrate?

**Tamara Luzajic:** No, we are still nothing.

**Bailey Seybolt:** We just don't have time.

**Bailey Seybolt:** Yeah.

**Tamara Luzajic:** I mean, but soon we're going to figure it out.

**Tamara Luzajic:** No pressure.

**Tamara Luzajic:** Yeah.

**Bailey Seybolt:** It's hard to travel when you have kids.

**Bailey Seybolt:** Adds a lot of complication to it.

**Tamara Luzajic:** You know, you know how it is.

**Tamara Luzajic:** I mean, it's just, it's cool and stuff.

**Tamara Luzajic:** So, yeah, at one moment we will, we'll go somewhere.

**Bailey Seybolt:** Something to look forward to.

**Tamara Luzajic:** Yes, motivation.

**Tamara Luzajic:** Yeah.

**Tamara Luzajic:** So we're all here.

**Tamara Luzajic:** We gather here today to talk about Fathom.

**Tamara Luzajic:** I will let Gabby actually talk about this or Aida.

**Tamara Luzajic:** I will jump in if you guys agree about stuff that you need from my side with pipeline and stuff.

**Tamara Luzajic:** But, yeah, if you wish, Gabby, Aida, you can take the floor.

**Aida Knezevic:** Yeah, I can go ahead and just, like, cover some high-level stuff.

**Aida Knezevic:** So with you.com, they're kind of, like, as a company, they're at an interesting point because they have pivoted.

**Aida Knezevic:** So if you look at their content strategy, for example, they have a visibility problem in terms of what they want to be known for.

**Aida Knezevic:** So they used to be kind of more like a consumer application.

**Aida Knezevic:** They were kind of like perplexity.

**Aida Knezevic:** And then because they lost ground to perplexity and like some stronger competitors, they pivoted to an enterprise search tool.

**Aida Knezevic:** And they also have like a search API that people can embed into their applications like we're doing with perplexity and Tavoli and EXA.

**Aida Knezevic:** So those are like the two main use cases of their product.

**Aida Knezevic:** So it's something to be aware of when you're generating content that the content should specifically speak to.

**Aida Knezevic:** Sorry, should speak to either like one of those two products and we shouldn't like we shouldn't confuse them.

**Aida Knezevic:** So you can kind of see like the visibility issues that they were having around like what is search API.

**Aida Knezevic:** They didn't have any content that's like ranking for those keywords.

**Aida Knezevic:** And they didn't really have any existing organic content when they started working with us.

**Aida Knezevic:** They just had like a couple of blog posts that they had published, but nothing too major.

**Aida Knezevic:** They did publish some like comparison content, which is good.

**Aida Knezevic:** But yeah, these are the topic clusters that we're targeting.

**Aida Knezevic:** So I think there are four or five and then you can find like more topics in their content OS.

**Aida Knezevic:** The person that's joining week over week is Brooke.

**Aida Knezevic:** I think she's their head of content marketing, or she's basically like the primary point of contact.

**Aida Knezevic:** She owns their internal content strategy.

**Aida Knezevic:** She's very nice.

**Aida Knezevic:** She has worked at agencies before.

**Aida Knezevic:** So I feel like that, like her experience kind of, I feel like she's nicer to work with because she knows what it's like on the other side.

**Aida Knezevic:** But I think it's very important to kind of like not, I think when sometimes when like people are very nice to work, easy to work with, we might like fall and be like, okay, this is like fine.

**Aida Knezevic:** You know, like they, you know, like we can kind of like, you know, cut corners or like delay deliveries because they're nice.

**Aida Knezevic:** And I just don't want us to get into that situation because they are really good to work with and they have like already brought up the phase two transition internally to their procurement team.

**Aida Knezevic:** So they really do want to make this work.

**Aida Knezevic:** So I think in terms of like deliveries, I think it's just important to be on schedule, be on time.

**Aida Knezevic:** They really do want to do scale.

**Aida Knezevic:** So we did tell them for editorial content during the sprint, it's going to be five per week, but they are interested in doing some programmatic stuff as well.

**Aida Knezevic:** I think I filed a linear ticket for one of the directors to explore some like programmatic strategies for them.

**Aida Knezevic:** But Bailey, you can kind of follow up on that in linear because I don't know if anybody's picked that up yet.

**Aida Knezevic:** But it is something that we should be like bringing up on the calls because their CMO, Katty, I think she was kind of like, you know, looking for volume as well.

**Bailey Seybolt:** And is, they are, they've opted in, right?

**Bailey Seybolt:** They weren't the one we're waiting, that was SpectraOps that we're waiting on?

**Aida Knezevic:** Yeah, yeah, yeah, they have opted in.

**Bailey Seybolt:** They have options, okay.

**Bailey Seybolt:** And do they know about the PSCO idea yet?

**Aida Knezevic:** Or like, would that be news to them?

**Aida Knezevic:** Or is that something you've talked to them about already?

**Aida Knezevic:** No, I think they are, I did not tell them explicitly, but I think it would be something that we can tell them like in phase two, we can like start talking about like potentially doing some like PSCO stuff.

**Aida Knezevic:** But they do have to know that like, it's a separate work stream.

**Aida Knezevic:** So if they do want to add that in, it's like a different package.

**Bailey Seybolt:** And has their name been an issue with like tracking in Scrunch and stuff?

**Bailey Seybolt:** I'm just thinking of like Logic, how that was an issue.

**Bailey Seybolt:** When you set all that up, is that something to keep an eye on?

**Aida Knezevic:** Or does it seem to be going okay?

**Aida Knezevic:** I think if you go to context, this is a primary brand name, so it shouldn't be an issue.

**Bailey Seybolt:** Okay.

**Aida Knezevic:** And then...

**Aida Knezevic:** And you can kind of see, like, all the different products that they have here.

**Aida Knezevic:** So, like, the enterprise AI solutions, it's basically, like, building, like, an internal AI agent that can, like, do different things in an enterprise.

**Aida Knezevic:** The tricky thing about this is, and what's interesting is that on one of the calls, this wasn't Brooke, but it was someone else on their team.

**Aida Knezevic:** She was talking about how sometimes enterprises, like, don't even know that they need a solution like u.com.

**Aida Knezevic:** They have this very specific problem that they're dealing with, like, for example, like, compiling all of their, like, customer support tickets in a searchable database that they can, like, use to kind of, like, uncover patterns and things like that.

**Aida Knezevic:** But they don't really know that what kind of tool they need to create that or how they can create that.

**Aida Knezevic:** So, I think that's something interesting to explore from a strategic and, like, keyword research perspective.

**Aida Knezevic:** But the search API.

**Aida Knezevic:** It's kind of like more, the more straightforward product.

**Aida Knezevic:** And then I don't know if we have an Agentec pipeline set up for them yet, Tamara, we do?

**Tamara Luzajic:** Yes, yes, we do.

**Tamara Luzajic:** We do.

**Tamara Luzajic:** We actually wrote, I think, the last two weeks using Agentec.

**Tamara Luzajic:** And how is it doing?

**Tamara Luzajic:** Are the artifacts doing okay?

**Tamara Luzajic:** Or does it feel like it's going to need an overhaul?

**Tamara Luzajic:** Yeah.

**Tamara Luzajic:** That mostly style-wise.

**Tamara Luzajic:** Artifacts, it was all correct.

**Tamara Luzajic:** But then Brooke had some comments about the style.

**Tamara Luzajic:** It sounded a bit robotic.

**Tamara Luzajic:** A lot of those AI-related mistakes, repetitions, weird phrases, and stuff like that.

**Tamara Luzajic:** But mostly the style sounded non-human.

**Tamara Luzajic:** So...

**Tamara Luzajic:** So we updated artifacts last week, and Gabby can also say what she thinks about it, but I think that it improved a lot, and we also created, we will also share that with you in the handoff.

**Tamara Luzajic:** We created some prompts that you can use based on Brooke's comments that are specifically about what she mentioned in some last batches of content, but it was mostly about style.

**Tamara Luzajic:** I didn't really notice some bigger issues when it comes to correct data information.

**Tamara Luzajic:** Is it right, Gabby?

**Tamara Luzajic:** I think that it improved much last week.

**Gabrielle Brogan:** Yeah, exactly.

**Gabrielle Brogan:** I agree from my perspective.

**Gabrielle Brogan:** So we essentially have eight blogs kind of in review at the moment with three that we're kind of going back and forth with Brooke on, and in those she did mention.

**Gabrielle Brogan:** And as Tamara mentioned, the kind of AI tone of voice and the repetition was like a big thing as well.

**Gabrielle Brogan:** So for me, that was really thinking about then structure and voice.

**Gabrielle Brogan:** And I think that this week's exactly what will be Artifact updating we did.

**Gabrielle Brogan:** The voice has improved massively.

**Gabrielle Brogan:** It's almost in some places, though, something to watch out for is it's now trending sometimes too casual because we're trying to create that human tone of voice.

**Gabrielle Brogan:** So, yeah, I'd say watch out for it trending a little bit to kind of it becomes so casual that it's AI casual.

**Gabrielle Brogan:** So that's something to look out for.

**Gabrielle Brogan:** And then structurally, there are still some repetitions coming through.

**Gabrielle Brogan:** But because we've got our eye on that now and we're using those prompts, we're able to catch them.

**Gabrielle Brogan:** But the kind of repetition that we're kind of referencing is concepts being explained a few times over kind of to intro a new section, like a new H2 is being introed by going back over the same concept again, sort of written in a different way.

**Gabrielle Brogan:** So it's not so much repeated lines coming through, but there has been one or two cases of that.

**Gabrielle Brogan:** It's more the ideas that are getting rehashed.

**Gabrielle Brogan:** So that's more structural, I think.

**Gabrielle Brogan:** So we've been addressing that this week as well, but definitely an improvement from the first ones and based on her feedback.

**Gabrielle Brogan:** Yeah.

**Bailey Seybolt:** And have they been pretty engaged in terms of like giving feedback and approving things?

**Bailey Seybolt:** And moving things through the content pipeline?

**Bailey Seybolt:** Or are they someone who needs a little more prodding?

**Aida Knezevic:** I think they're mostly like Brooke.

**Aida Knezevic:** feel like she's really busy, but she does try to review things.

**Aida Knezevic:** Sometimes she might not like get to it exactly when she says she will.

**Aida Knezevic:** But I think if you like tag her like a couple of times, she's going to respond.

**Aida Knezevic:** But yeah.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** We've only published one article so far because she has been a little bit late to review things, but she is engaged.

**Aida Knezevic:** The vibe I get for them is that she cares.

**Aida Knezevic:** It's not like SpectreOps where they were kind of like, I feel like most of the team just wasn't really interested in anything we were doing.

**Aida Knezevic:** So for her, it's the opposite, but I feel like she's just really busy.

**Aida Knezevic:** So, yeah.

**Aida Knezevic:** And they also, I'm not sure if we ever got to talk about this last week because I was out on Tuesday when we had our weekly sync, but she did, like, build a content strategy internally, and I think we can also talk to her about that and see what we can kind of do to support that.

**Iana Medvedeva:** Okay, I probably ask it to every same manager and editor, but if you could walk me through the content creation that you're doing right now, like, be

**Iana Medvedeva:** If you are doing outlines, so what exactly you are looking when you are doing post-processing, I would really appreciate it, just so I can mimic your process, at least in the beginning.

**Tamara Luzajic:** Sure.

**Tamara Luzajic:** Do you want me to walk you through as I wrote the content so far?

**Iana Medvedeva:** Yes, like maybe if you are doing outlines, and what type of outlines you are doing, because it really depends, someone is stressing pipeline to do the job, someone gives very strict outlines to follow, and what are the specific details that you are trying to catch in a post-processing?

**Tamara Luzajic:** Yeah, sure.

**Tamara Luzajic:** So I'm gonna share my screen real fast.

**Tamara Luzajic:** So basically what I do for you.com is I tried a few things.

**Tamara Luzajic:** I tested out, I don't know if you...

**Tamara Luzajic:** Iana, if you watched, I think Daniel shared that Loom video of how he creates outlines, where he uses AI assistant to create research questions and also an outline.

**Tamara Luzajic:** So I tried that, and I had good results, basically.

**Tamara Luzajic:** think that some of these earlier topics...

**Tamara Luzajic:** Do you see my screen, by the way?

**Iana Medvedeva:** Yeah?

**Tamara Luzajic:** Yes, yes.

**Tamara Luzajic:** Yeah, okay.

**Tamara Luzajic:** So this is...

**Tamara Luzajic:** Let me just see if this is the one...

**Tamara Luzajic:** Yeah, so this is one of the early blog posts.

**Tamara Luzajic:** What I did, basically, of course, I used SERP just to research the keyword to see in terms of outline what heading and subheadings

**Tamara Luzajic:** Readings, other articles have, the typical process.

**Tamara Luzajic:** And then I asked AI assistant to create an outline for this keyword and also to provide research questions.

**Tamara Luzajic:** So I can kind of get him more focused on what I want to get.

**Tamara Luzajic:** And then I added these research questions because, of course, I mean, in some cases, Atlas just focuses too much on statistics and data that we don't really need for this client.

**Tamara Luzajic:** And I then got some really nice results.

**Tamara Luzajic:** It wasn't bad.

**Tamara Luzajic:** I also used AI assistant to kind of focus it, to bring back the focus on the outline that I initially wanted.

**Tamara Luzajic:** And I did all the major, all the major editing here in Atlas.

**Tamara Luzajic:** Atlas.

**Tamara Luzajic:** Atlas.

**Tamara Luzajic:** And I was really happy with the results.

**Tamara Luzajic:** And then after, I don't know, maybe a week or two, we had another Atlas session with Panzer.

**Tamara Luzajic:** And then they talked about how Atlas actually needs not so much information.

**Tamara Luzajic:** And then I tried another plan to kind of provide less information.

**Tamara Luzajic:** So I went with an outline like this, you see, just like this is a typical outline that I use, just SERP and Claude, some basic Claude, prompting to get this outline.

**Tamara Luzajic:** As you can see, it's really, really simple.

**Tamara Luzajic:** And I got kind of the same result.

**Tamara Luzajic:** I can't say that this was better than the other one.

**Tamara Luzajic:** Again, I did all the editing in Atlas using AI Assistant.

**Tamara Luzajic:** And I was really, really happy.

**Tamara Luzajic:** I'm with the results, I'm generally really happy with how AI assistant works, and in terms of prompts, the prompts that I mentioned to you, they were based on Brooke's comments, let me just take a look where that is, I'm sorry, okay, here it is, so under prompt library and post processing, what we usually do before this first, before this step, sorry, went to the beginning again, so what we usually do, we go to Claude, course, to do some basic writing guidelines analysis, and then after removing those repetitions, AI stuff, if bluff is missing somewhere, we also, of course, we linked it here, so you can find it easier,

**Tamara Luzajic:** So this is the project in Claude, and I don't have permission to do that now because I'm not on my account, but you will have.

**Tamara Luzajic:** Sorry about that.

**Tamara Luzajic:** So back to the prompt, this is specifically built on Brooke's comments.

**Tamara Luzajic:** And so as you can see, this is the regular stuff, repetitions, AI patterns, vague language, sources if they're missing somewhere, pretty, pretty typical stuff that AI does.

**Tamara Luzajic:** And then after this one, this is the final check that I do before I send it to Gabby.

**Tamara Luzajic:** This is the more focused on style.

**Tamara Luzajic:** As you can see here, know, mix sentence lengths and structures, vary the structure, use occasional conversational phrases to engage readers.

**Tamara Luzajic:** Anything that kind of makes it look and feel more like human.

**Tamara Luzajic:** But then as...

**Tamara Luzajic:** Gabby said, we really have to, you really have to watch out for phrases like, here's what it means, here's, you know, here's what the trick is, and stuff like that, because it gets too casual, but then it's AI casual.

**Tamara Luzajic:** And that's it, that's really all that I did in terms of writing process and post-processing.

**Tamara Luzajic:** Gabby, do you have something else to add?

**Gabrielle Brogan:** Did I miss anything?

**Gabrielle Brogan:** No, I think that's a really good overview.

**Gabrielle Brogan:** I think, yeah, I guess, from my perspective, what I usually focus on first is looking at the kind of information architecture to make sure that we're building on information as we go through the blog.

**Gabrielle Brogan:** Instead of, yeah, just kind of using the same information to intro new concepts, because I think that was something that we really were focusing on last week.

**Gabrielle Brogan:** And yeah, just to, like you said, calibrate towards that more natural tone of voice.

**Gabrielle Brogan:** And

**Gabrielle Brogan:** Checking for that.

**Gabrielle Brogan:** The links always tend to be really good.

**Gabrielle Brogan:** We mostly link to u.com's products in the CTA, and obviously the internal links there, they're usually all fine, but obviously checking those.

**Gabrielle Brogan:** And yeah, so I'm still kind of building up my kind of go-to prompt library at the moment, but I'll also take a look through and drop in the prompts that I'm using just to do that kind of editing and final pass checking as well.

**Iana Medvedeva:** Good, good.

**Iana Medvedeva:** Thank you.

**Iana Medvedeva:** How long it takes for you to get output from Atlas to look in deliverable?

**Iana Medvedeva:** How much of editing Atlas output requires?

**Tamara Luzajic:** Well, that's a good question, but I would say that for one article from Atlas, what it does to something that it's deliverable for an ME, I wouldn't say like not over an hour.

**Tamara Luzajic:** And that's like for the more complicated ones that I'm not really familiar with.

**Tamara Luzajic:** It has a lot of, like, technical stuff that I don't understand, so I have to go back and make sure that I didn't miss anything or maybe I misuse a term or something else, but not over an hour.

**Tamara Luzajic:** I think that's okay.

**Iana Medvedeva:** Yeah, sounds good.

**Iana Medvedeva:** Sounds so close to, like, pipeline is getting closer.

**Iana Medvedeva:** That's what we want to do.

**Tamara Luzajic:** I really hope so.

**Tamara Luzajic:** I really, really hope so.

**Tamara Luzajic:** The thing is, we didn't have too much feedback, so you guys will know more than we do at the moment, but hopefully we are closer at this moment.

**Aida Knezevic:** I think some things that we, like, they experimented with Fleet is that they updated all of the artifacts to use the tone that we want the articles to be written in.

**Aida Knezevic:** So I think, I'm not sure if we've done that for you already.

**Tamara Luzajic:** No, we haven't done that for you.

**Tamara Luzajic:** So I just updated them to use some terms.

**Bailey Seybolt:** Hassan did the same thing with Logic and it made a huge difference.

**Bailey Seybolt:** We cut our editing post-processing in half.

**Aida Knezevic:** So yeah.

**Aida Knezevic:** I think that's one of the things.

**Aida Knezevic:** And it shouldn't take us too long, I feel, just to update the style.

**Aida Knezevic:** But yeah, I think that is like a huge reason why like Atlas struggles because it clearly mimics the writing style in the artifacts.

**Aida Knezevic:** So I think, yeah, for all existing clients that we have in the sprints, we need to make sure that the artifacts are updated to sound like the writing guidelines.

**Aida Knezevic:** And then, yeah, I think it shouldn't take us too long, but it does like save us time for editing.

**Tamara Luzajic:** I have one question, sorry, while we're at this.

**Tamara Luzajic:** So when you say like using the writing style, it doesn't mean like using the phrases that...

**Tamara Luzajic:** What this client prefers and to kind of rewrite all the artifacts, not just writing guidelines?

**Aida Knezevic:** I think we can use an article.

**Aida Knezevic:** I think that, okay, so the writing guidelines that we have, the artifacts should follow those writing guidelines.

**Aida Knezevic:** Because the issue is that right now the company context and the audience personas, they have like this kind of choppy tone that doesn't, like that gets pulled over into the articles.

**Aida Knezevic:** I think you can use the writing guidelines.

**Aida Knezevic:** You can use like an article of ours that they liked and just ask Claude to like rewrite the artifacts using that like language to entone.

**Aida Knezevic:** But like still preserve all of like the key information.

**Aida Knezevic:** So I think we can get creative with it.

**Aida Knezevic:** So as long as it's not written in that original like corporate SaaS startup Bay Area LinkedIn post tone that we have right now.

**Tamara Luzajic:** Yeah.

**Aida Knezevic:** Yeah, so I think that would help me help.

**Tamara Luzajic:** Very specific.

**Tamara Luzajic:** Yeah.

**Tamara Luzajic:** Okay, thank you.

**Aida Knezevic:** Yeah.

**Bailey Seybolt:** Yeah, and even talking about MDashes, we found, like, we had our, in our proofreader checklist, we had it everywhere, and we're like, why are these MDashes creeping in?

**Bailey Seybolt:** And it's because obviously, you know, the, like, company context document was full of MDashes.

**Bailey Seybolt:** It seems so obvious in hindsight, but there we go.

**Aida Knezevic:** Yeah, yeah, because I feel like, yeah, I think these are all just, it's, like, kudos to Hassan for, like, figuring it out, because I think that sometimes when people come in who are new and have, like, a fresh perspective on things, they think they might think about this differently, and I think it was a really good approach to, like, you know, because it does make sense.

**Aida Knezevic:** It's, like, why is it, why does Claude know how to follow these instructions, but Atlas doesn't, like, what is the difference, so.

**Iana Medvedeva:** Yeah, and what actually gives a lot of difference is to make sure that every second example, especially in an assignment, sometimes in assignment direction, we are using example that using each and every client, for example, even for links, like there is the directions how to format links, and we are just pulling from one client to another, those examples.

**Iana Medvedeva:** And it kind of, it gets confused with which style to use.

**Iana Medvedeva:** There is an example, it says that it's good to say it tries to use as a style sample.

**Bailey Seybolt:** In terms of content runway, it seems like there's a good list of kind of approved articles.

**Bailey Seybolt:** Anything sort of to know about there, about like upcoming research or like places they want to lean into the strategy or anything we should keep in mind?

**Aida Knezevic:** Not that I know.

**Aida Knezevic:** I don't think so.

**Tamara Luzajic:** What I did, I intended just to take one, like, everyone does so far, like, choose one from a cluster, each from one cluster, so nothing special.

**Iana Medvedeva:** Okay, great.

**Iana Medvedeva:** I also wanted to ask how it's going to be, like, a timeline here, if I'm taking over this week's generation, or you're still going to generate and edit for this week, and I'm going to, kind of, more like a viewer, and following your process.

**Iana Medvedeva:** So, some timelines and edits, how it's going to be this transition.

**Aida Knezevic:** I think it's week eight, so we should still generate the content and the sprints this week.

**Aida Knezevic:** And, yeah, and then from next week, once we get, like, the official confirmation, then they can go over.

**Iana Medvedeva:** Okay.

**Iana Medvedeva:** So, this week, I'm just going to be following your steps, just looking how and when you're delivering, and what states.

**Iana Medvedeva:** So, I know.

**Iana Medvedeva:** For sure, how it should look like in the client's hands.

**Iana Medvedeva:** And I believe it's the same for SpectreOps, or there's more caveats in this situation?

**Aida Knezevic:** SpectreOps, we are waiting on a couple of things.

**Aida Knezevic:** They've requested an extension in the sprints just to calibrate some more.

**Aida Knezevic:** So I'm not sure what's happening.

**Aida Knezevic:** I'm waiting for the Americans to wake up on the West Coast.

**Aida Knezevic:** To let us know what are the next steps.

**Aida Knezevic:** I think it's just that it's not that they're unhappy.

**Aida Knezevic:** They see the value and they want to work with us.

**Aida Knezevic:** But the issue is that their product managers joined the company halfway through the sprint.

**Aida Knezevic:** And he just started editing content like two weeks ago.

**Aida Knezevic:** And he just had like, obviously, they always have a lot of feedback in the beginning.

**Aida Knezevic:** So they were just a little bit like concerned if, you know, they could handle that amount.

**Aida Knezevic:** So I think they just want to do a couple of more weeks in the sprint and then transition to a steady state.

**Iana Medvedeva:** If they're staying in the sprint, they're staying still with your team, they're staying still with Kavishka, and he's going to be working on the content generation, or they're going to try to transition already?

**Aida Knezevic:** I don't know.

**Aida Knezevic:** We have to wait and see what Andy says, but we'll keep you posted.

**Iana Medvedeva:** Yeah, okay.

**Iana Medvedeva:** Thank you.

**Bailey Seybolt:** Yeah, and I was going to say, with you.com and SpectraOps, let me know if you want me to join those syncs, or if I should hold off.

**Aida Knezevic:** Okay, yeah, yeah, I will.

**Aida Knezevic:** Let me actually note that in the sprint tracker.

**Bailey Seybolt:** Yeah, sometimes it seems like with the clients, the ones that are less engaged in strategy.

**Bailey Seybolt:** doesn't...

**Bailey Seybolt:** It's like they end up there for longer.

**Bailey Seybolt:** feel like it's so much harder to get them kind of moving through.

**Bailey Seybolt:** At least that's how I felt with HX when we were in.

**Aida Knezevic:** Yeah, I think with, I don't know, it just, yeah, it's really different based on who you're working with.

**Aida Knezevic:** Like, I don't know, it's just so dependent on different clients.

**Aida Knezevic:** I do have to say that if I notice that a client, like, if I'm in a meeting with people and their cameras are off, it's always a really bad sign.

**Aida Knezevic:** So it just signals to me, like, you're not, probably not even listening to this meeting.

**Aida Knezevic:** It's like a weird rash that day or something.

**Aida Knezevic:** Yeah, it was just like a sporadic and like with Spectro Ops every other week, there would be different people on the call.

**Aida Knezevic:** They were just kind of like, so it just wasn't, it was just hard to kind of, like, develop that report, but.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** Well, we'll see.

**Gabrielle Brogan:** Yeah.

**Gabrielle Brogan:** Yeah.

**Gabrielle Brogan:** I have a question.

**Gabrielle Brogan:** Quick question as well, actually, is the idea then that this week I will be editing for you.com and SpectreOps, because I, Andy messaged me, we were talking earlier in the week, last week, and she mentioned that this week I'm going to be generating and editing all content for Fleet, as well as generating half the content for Field Guide and editing all of it, and working on Redis editing.

**Gabrielle Brogan:** So I'm just wondering, in terms of capacity, if the idea is also that I'm on SpectreOps and you.com this week as well.

**Aida Knezevic:** If that's happening, I don't know, Bailey, like, well, you're not actually editing content anymore, right, from this week?

**Bailey Seybolt:** No, I'm only, I'm editing some of the things that were left over from last week, but yeah, now I'm supposed to be taking on, but I mean, I think if we...

**Bailey Seybolt:** It depends.

**Bailey Seybolt:** It's all like, it's like, but if you guys are keeping more and I'm not sort of managing those clients, I could potentially, well, probably not because I've got to do the strategy for these other ones.

**Bailey Seybolt:** Yeah, I'm not exactly sure how it's working.

**Bailey Seybolt:** My understanding was that people were taking over generating for their new clients today, but I think it's a little different if they're still in the sprint, right?

**Bailey Seybolt:** If they haven't moved out of the sprint.

**Bailey Seybolt:** So this may just be a question for Andy, how she wants to, like, handle it if clients are still in sprint, if the new team should take them over, or if you should hold on to them for another week.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Okay.

**Aida Knezevic:** I think, Gabby, what you can do is you can just message Andy in the sprint channel and just let her know and have her make the call and how this is going to go.

**Aida Knezevic:** So, because it does, like, the content does need to go through another round of human review before it goes to the client.

**Aida Knezevic:** So I don't know, like.

**Aida Knezevic:** What's the best way to do this, but the sooner we get ahead of it, the better.

**Gabrielle Brogan:** Yeah, definitely.

**Gabrielle Brogan:** Okay, cool.

**Aida Knezevic:** I'll post that in the channel then.

**Aida Knezevic:** Okay, thank you.

**Aida Knezevic:** All right.

**Aida Knezevic:** I will see you guys later.

**Aida Knezevic:** Bye.

**Aida Knezevic:** Thank you.

**Aida Knezevic:** Bye.
