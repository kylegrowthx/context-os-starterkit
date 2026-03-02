# Homebase <> Growth X - Weekly Sync

<metadata>
date: 2025-10-02
time: 14:01 UTC
duration: 32 minutes
organizer: matthew.alves-hill@growthx.ai
participants: Matthew Alves-Hill (GrowthX), Jakub Rudnik (GrowthX), Sonia Urlando (Homebase), Mark Velarga (Homebase)
fathom_recording_id: 91394299
fathom_url: https://fathom.video/calls/428054441
share_url: https://fathom.video/share/bcxgY_dnf4NVd3cy-S24Hdg221x493zy
source: fathom
enriched_on: 2025-10-02 14:45 UTC
</metadata>

---

## Summary

Homebase and GrowthX synced on significant progress in the TLDR pipeline, which now reads content correctly and uses condensed 600-word instructions (down from 2000) to avoid confusing the LLM. Matthew Alves-Hill walked through the updated TLDR structure—including listicle summaries, competitive mention handling, and removal of push-style CTAs—and will test the new instructions on a batch of articles next week for Sonia's feedback. The team also discussed the glossary content refresh and Mark introduced a new "start your business" content project launching 50-60 pieces simultaneously to test LLM and SEO signals, with keyword tracking planned in Scrunch.

---

## Context

Homebase is a GrowthX Labs client focused on workforce management software. This is a weekly operational sync between Homebase's content and SEO team (Sonia, Mark, Kerry) and GrowthX's content and delivery leads (Jakub, Matthew). Matthew recently joined the account as the new managing editor and has been focused on fixing two core workflows: TLDR generation and glossary content. Previously, the pipelines had stalled due to issues with instruction clarity and LLM confusion. This meeting showcases the breakthrough Matthew achieved by radically simplifying the prompt structure, which opened the door to scaling both initiatives.

---

## Relevance

**To GrowthX Delivery:**
- Matthew's approach to prompt simplification (2000 words → 600 words) is directly applicable to other content pipelines. The core insight—that LLMs struggle with contradictions and verbosity—should inform all instruction-writing going forward.
- Funnel-stage mapping (top-of-funnel vs. bottom-of-funnel intent) is now embedded in the TLDR instructions and could be extended to glossary, how-to, and other content types.
- The workflow shift from "big drop" prompts to sequenced, context-aware instructions represents a scalable methodology for content generation at Homebase's volume.

**To CheckThat:**
- The conversation highlights the practical challenge of balancing SEO signals with reader intent, which directly relates to CheckThat's visibility and citation-tracking mission. The discussion about what appears in TLDRs vs. the main article touches on how LLM visibility works in practice.

**To GrowthX Business Development:**
- Strong account momentum. Matthew's contributions in just 2-3 weeks have unblocked two major content workflows, signaling effective delivery and positioning GrowthX for expansion into Homebase's "start your business" initiative (50-60 pieces launching simultaneously).
- Renewal strength indicator: Homebase is actively investing in new content projects and expanding scope. The new "start your business" project and keyword tracking setup (Scrunch + Profound) suggest deeper integration with GrowthX's toolkit.
- Reference potential: This TLDR methodology and prompt-simplification approach could be case-study material for other content-heavy SaaS clients.

---

## Overview

- Significant progress made on TLDR pipeline, with improved instructions and content recognition
- New TLDR structure agreed upon, including listicle summaries and key features
- Glossary topics exhausted; Homebase team to provide guidance on next batch
- New "start your business" content project in the works, focusing on operational questions

---

## Key Topics

### TLDR Pipeline Improvements

  - Pipeline now reading content correctly and not inventing information
  - New instructions condensed from 2000 to 600 words, improving clarity and consistency
  - Structure includes headline, intro paragraph, content sections, and no CTA
  - Homebase team to provide feedback on a new batch of TLDRs for further refinement

### TLDR Content Structure

  - Aim for 150-200 words in TLDRs
  - Include listicle summaries when present in the main article
  - Avoid mentioning direct competitors (e.g., Clockify) in TLDRs
  - Focus on providing valuable takeaways for readers and optimizing for SEO

### Glossary and Content Refresh

  - Previous batch focused on hiring terms; new topics needed
  - Homebase team to identify gaps and provide direction for next batch
  - Ongoing content refreshes may impact TLDR generation for some articles

### New Content Project: "Start Your Business"

  - Similar approach to glossary, but focusing on longer-tail query questions
  - Topics include payroll, business operations, and other startup-related subjects
  - Plan to publish 50-60 pieces simultaneously to test LLM and SEO signals
  - GrowthX to set up keyword tracking in Scrunch for data triangulation with Profound

---

## Action Items

**Matthew Alves-Hill (GrowthX)**
- Update TLDR instructions - include listicle summary, remove CTA, adjust length to 150-200 words

- Select suitable articles for TLDR testing, share in chat for Sonia's approval

- Prepare batch of TLDRs using updated instructions for next week's review


**Mark Velarga (Homebase)**
- Create & send brief for new "start your business" content project, including potential pipeline requirements and scope


**Sonia Urlando (Homebase)**
- Discuss with Homebase team to identify new glossary topics and fill gaps after the hiring terms batch


**Jakub Rudnik (GrowthX)**
- Send UserPilot TLDR example to team as a reference for competitive SEO best practices

- Set up keyword tracking in Scrunch for the new "start your business" content pipeline after launch, with triangulation against Profound data

---

## Transcript
**Jakub Rudnik:** Trying to figure out, like, what the position of the camera, you know, that type of stuff.

**Mark Velarga:** Yeah, and you set up and everything.

**Jakub Rudnik:** Yeah, yeah, so.

**Mark Velarga:** Yeah, was going to say your background seems a little bit different today than usual.

**Jakub Rudnik:** Yeah, yeah, no bed in the background, so different setup, all good, just, like, living out of boxes and all that stuff.

**Mark Velarga:** Nice, nice.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** Hey, Matt.

**Matthew Alves-Hill:** How's it going?

**Mark Velarga:** Hey, Matt.

**Matthew Alves-Hill:** Hey, Mark.

**Mark Velarga:** I don't think I'm ready yet.

**Mark Velarga:** Yeah, sorry, I wasn't in the call last week, but, yeah, I work with Sonia.

**Mark Velarga:** I'm part of the organic team, so I oversee, basically, the more, like, technical SEO, some of the programmatic SEO work as well.

**Mark Velarga:** So, yeah, nice to meet you.

**Matthew Alves-Hill:** Yeah, you too.

**Matthew Alves-Hill:** I know your face, because I, while I was jumping onto Homebase, I've been re-watching some of the Fathom videos, so.

**Mark Velarga:** Oh, nice.

**Mark Velarga:** nice.

**Jakub Rudnik:** If you've caught up on the last one, this is probably a recap, but Matt's been, so Matt's the new managing editor, obviously, and then really jumping into the two different workflows that we've been trying to stand up.

**Jakub Rudnik:** And, you know, I don't think stalled is the right word, but it had been a little bit sluggish.

**Jakub Rudnik:** And so really over the last two weeks, it's made a ton of progress on the TLDRs.

**Jakub Rudnik:** And that's what we want to talk through today and show off.

**Jakub Rudnik:** I think where, you know, I said this kind of in the last call, but to reiterate, really excited for Matt being on this call specifically with how much you all are, one, we have different work streams, and two, where we've struggled, you know, is like since Atlas getting the pipelines in the right place and the experimentation.

**Jakub Rudnik:** And I think that's where, just in our, you know, first few weeks of working really directly together, Matt's like brought a ton of expertise coming over from our...

**Jakub Rudnik:** Like our sprint team.

**Jakub Rudnik:** And so I'm excited for that.

**Jakub Rudnik:** And I think we've made a ton of progress already in just these two or three weeks that you've been on the account.

**Jakub Rudnik:** So hello, Sonia.

**Jakub Rudnik:** We were just talking about TLDRs and Matt's progress there.

**Jakub Rudnik:** And that's really like our top agenda item for today.

**Jakub Rudnik:** But I think that that was kind of a gap with, yeah, until a few weeks ago.

**Jakub Rudnik:** And so I think we have a really good fit here.

**Jakub Rudnik:** So yeah, that's our big agenda item for today.

**Jakub Rudnik:** Anything other than that that you all want to talk through?

**Jakub Rudnik:** TLDRs will show off our progress kind of workshop together, I would say.

**Jakub Rudnik:** I can kind of let you in under the hood.

**Jakub Rudnik:** But anything from the Homebase side before we begin?

**Sonia Urlando:** I think just in a similar way as we've done with the TLDRs, just tapping back into the glossary too.

**Sonia Urlando:** I know we've kind of got that one like working on a steady flow.

**Sonia Urlando:** But if there is.

**Sonia Urlando:** Anything that we kind of want to look at there or kind of like sync up on there where we could make like improvements to our existing process since we've got like just some fresh energy, I think that would be great.

**Jakub Rudnik:** Cool.

**Jakub Rudnik:** I think a bunch of stuff with the artifact refreshes and, you know, the changes to the pipeline will impact all content, Matt, correct me if I'm speaking, how to turn on some of your processes.

**Jakub Rudnik:** You've been more in the weeds, but some of the changes we've made there can trickle over to Glossary and we should look for those improvements.

**Jakub Rudnik:** So I do think this is a good time to, you know, reset is too strong a word, but to refresh and to look at everything while we have that energy.

**Jakub Rudnik:** So, Matt, I'll go ahead to you.

**Sonia Urlando:** Oh, sorry.

**Sonia Urlando:** I just tried clicking into your agenda there and it looks like I might not have access.

**Matthew Alves-Hill:** Interesting.

**Jakub Rudnik:** Oh, I think I, this came up last time and I do think I did not follow through on figuring out what that

**Jakub Rudnik:** That was something like whatever happens in the beginning of the call.

**Jakub Rudnik:** You got to remember to come back to that.

**Jakub Rudnik:** Matt, do you mind just sharing the screen and I'll work on the access.

**Jakub Rudnik:** Let's get going.

**Jakub Rudnik:** Thank you.

**Matthew Alves-Hill:** Not sure if we have so many desktops here. Can you guys see that? Okay, cool.

**Matthew Alves-Hill:** I'll probably hop around screens-wise. Did you guys have a chance to watch that Loom I sent over last week?

**Sonia Urlando:** I didn't get a chance quite yet.

**Sonia Urlando:** We were kind of out on site a little bit this week for a case study.

**Sonia Urlando:** But Mark, I don't know if you had a chance.

**Mark Velarga:** I haven't had a chance yet, sorry.

**Matthew Alves-Hill:** It's all good.

**Matthew Alves-Hill:** So the TLDR fitting is that essentially there were kind of two main problems.

**Matthew Alves-Hill:** One issue is the pipeline and just recognizing the content and actually not inventing or adding new information, et cetera, et cetera.

**Matthew Alves-Hill:** So that was kind of like on the research side of the inputs, and we have been like iterating pipeline improvements obviously a lot since you guys like first joined with us.

**Matthew Alves-Hill:** So I've been testing a couple of things out, and I think that that problem is basically resolved.

**Matthew Alves-Hill:** Part of it is like setting up the researcher, and then part of it is the instructions as well, like not confusing the researcher.

**Matthew Alves-Hill:** So they're like kind of separate, but also linked, and I'll explain a little.

**Matthew Alves-Hill:** A bit more about the main change, but net is, the pipeline is now reading the content correctly.

**Matthew Alves-Hill:** Okay.

**Matthew Alves-Hill:** And, and as we, as we keep improving, like we're rolling out some like more agentic pipelines, which are even like more direct in their research capabilities.

**Matthew Alves-Hill:** So this should like improve even more, like maybe actually start drawing kind of insights or basically, we're going to see a lot of improvement in this space, but at right now, I feel like way more confident in just the performance of like reading the page correctly and drawing from the right input.

**Matthew Alves-Hill:** So, so that's like a first win.

**Matthew Alves-Hill:** Let me just swap this over to, I want to show you kind of like where we were and what I've been working on.

**Matthew Alves-Hill:** Gosh, I have a million tabs.

**Sonia Urlando:** I relate to that so much.

**Matthew Alves-Hill:** Yeah, it's like so many different Chrome profiles and all sorts.

**Matthew Alves-Hill:** Okay, cool.

**Matthew Alves-Hill:** So, Sonia, think you've seen this because I think you gave, you actually gave feedback on these.

**Matthew Alves-Hill:** Yeah, right.

**Matthew Alves-Hill:** Like this is the old, yeah.

**Sonia Urlando:** So these are the old instructions.

**Matthew Alves-Hill:** Yeah.

**Matthew Alves-Hill:** Now, like everything is in there that we need, but like it kind of gets lost.

**Matthew Alves-Hill:** And the way that like the way that the LLM and the pipeline is reading these instructions is like there's once you like once you start to put in contradictions, et cetera, it gets it like gets confused.

**Sonia Urlando:** And especially like the length.

**Matthew Alves-Hill:** So, yeah, I put this in the in the loom so you guys can check that afterwards if you're still like a little bit.

**Matthew Alves-Hill:** Yeah.

**Matthew Alves-Hill:** You said, but like straight off the bat, when I look in here, like 2000 was instructions.

**Sonia Urlando:** It's like, yeah, well.

**Sonia Urlando:** Like, normally we would do kind of like a sequence of prompts rather than like a big drop.

**Sonia Urlando:** Exactly.

**Sonia Urlando:** Like, please read the brand guidelines and that's a heftier document.

**Matthew Alves-Hill:** Right, exactly.

**Matthew Alves-Hill:** So, like I said, like, all the right information is in here, but it's just too, it was just too verbose and like basically getting confused and just stopping at a certain point and not taking all the instructions.

**Matthew Alves-Hill:** So, the first like big change straight away was I built a new set of instructions for the TLDR.

**Matthew Alves-Hill:** And so, straight off the bat, you can see here that we're working from 600 words, not to two and a half thousand.

**Matthew Alves-Hill:** And, like, I'm sure you're like well aware, but like with AI, it's like you do like the tweaking and the heavy lifting that comes up front and then you scale, right?

**Matthew Alves-Hill:** That's like where we get the value out of it.

**Matthew Alves-Hill:** So, essentially...

**Matthew Alves-Hill:** Taken the original instructions and then kind of more context from what you've been sharing in some of the chats, like especially around intent, like mapping, you know, we need the pipeline to understand what, like what stage of the funnel this is, because that dictates like whether we're going to put a, you know, an explanation at the front of a TLDR for a reader who's just, you know, problem aware versus like some more bottom funnel type intent content in the TLDR that they're going to find useful.

**Sonia Urlando:** off the bat.

**Matthew Alves-Hill:** So essentially, like, this is what we're doing straight up front.

**Matthew Alves-Hill:** Like we're asking the engine, identify the funnel stage of this content and identify why the reader wants, why the reader might be visiting this.

**Matthew Alves-Hill:** And then the engine like has context straight away to then build the head, like this information has to be gathered up front.

**Matthew Alves-Hill:** And then the structure of the TLDR, like follows after that.

**Matthew Alves-Hill:** And then it's simple, like instead of, instead

**Matthew Alves-Hill:** Instead of multiple examples and crisscrossing instructions, we take the TLDR structure in specific stages.

**Matthew Alves-Hill:** Build a headline first.

**Matthew Alves-Hill:** Then we have an intro paragraph.

**Matthew Alves-Hill:** And I would like some of your input on the structure itself because I've seen a document that I'm not sure if it was built by you, Sonia, or maybe in tandem with Jess about your ideal structure for TLDR.

**Matthew Alves-Hill:** We can get there, but I've kind of inferred from everything I've heard to set a structure out.

**Matthew Alves-Hill:** So you can see here, like, the headline is using the keyword, but it's varying.

**Matthew Alves-Hill:** You know, we're not just repeating the H1.

**Matthew Alves-Hill:** We're, like, we're tying it in, but it's still, it needs to be distinct from the H1.

**Matthew Alves-Hill:** A short intro paragraph.

**Matthew Alves-Hill:** Again, these are the kind of things we can tweak pretty easily.

**Matthew Alves-Hill:** And, like, the main issue that we were having when it comes

**Matthew Alves-Hill:** The main issue we were having with content sections is that they can be different. For tool comparison blogs we were often having listicles. Now we have two batches of instructions: for tool comparison pages we have what matters most, key features, and how to pick wisely. For informational and how-to content, I'm giving the engine more leeway to look at what's relevant, but still prompting based on funnel stage. If it's top of funnel, we summarize what the topic is and why it's important. If it's more informed, we focus on key features and implementation.

**Matthew Alves-Hill:** I put in an instruction to include a CTA in the TLDR, but it's linked to the content, not an orphan hard sell. For example, if it's about mobile app tracking, it's "learn more about how Homebase enables this feature."

**Matthew Alves-Hill:** For voice and style, I've kept it limited because I've mapped the writing guidelines we built for you to the TLDR pipeline. You mentioned a couple of times we need to get the tone right. The TLDR will be more direct, but we still want to speak in Homebase language. These are non-negotiable rules, but you have to be careful about contradicting what's in the writing guidelines because the engine gets confused.

**Matthew Alves-Hill:** Accuracy is ensuring we're not making up facts. Length and format are things I've inferred, but we can check and change them.

**Matthew Alves-Hill:** Now we have a template that will deliver consistent results and can scale. There's a quality control review checklist.

**Matthew Alves-Hill:** So in effect, we have like everything that was in the previous instructions condensed and crystallized into a step-by-step prompt that, shouldn't hold up at scale.

**Matthew Alves-Hill:** That was a lot of information. Do you have any questions before I talk about what I want from you?

**Sonia Urlando:** Structurally this is looking a lot better. There are some things that need a quick edit where I can add context, but overall I'm interested to see the output and this makes sense procedurally.

**Matthew Alves-Hill:** The idea is to test this across batches and give you a batch of TLDRs we can workshop before our next call.

**Matthew Alves-Hill:** But in terms of output, like, so this was a previous one that we shared.

**Matthew Alves-Hill:** This was top five.

**Matthew Alves-Hill:** This is coming off this page.

**Matthew Alves-Hill:** So it's really long.

**Matthew Alves-Hill:** And another thing that you mentioned was like competitor mentions.

**Matthew Alves-Hill:** So this is kind of the first question that like Jakub and I were kind of workshopping and chatting about.

**Matthew Alves-Hill:** Like, I'm of the opinion that for scale on this TLDR pipeline, like it's a simple fix or an easy instruction to be like, we never mentioned any like listicle in the TLDR.

**Matthew Alves-Hill:** Now, if you do want, if it's like the top five, you know, in this case, so, okay, let me slow down here.

**Matthew Alves-Hill:** So, yeah, I saw the fact that you have kind of like no brand mentions up there.

**Sonia Urlando:** Yeah.

**Sonia Urlando:** And I would say maybe there's a little bit of crossed wires because with something like the

**Sonia Urlando:** Listicles, want to list like the software up in the TLDR as well.

**Sonia Urlando:** There's really just like a handful of specific competitors that we try not to mention.

**Sonia Urlando:** For example, like Connect Team is a direct competitor to Homebase.

**Sonia Urlando:** So they normally wouldn't appear in the body of the article, but those other brands that are listed would be like summarized in like, you know, one line per bullet point up in the TLDR.

**Matthew Alves-Hill:** Okay.

**Matthew Alves-Hill:** Okay.

**Matthew Alves-Hill:** So in this, like in this style?

**Sonia Urlando:** Yes.

**Sonia Urlando:** Yeah.

**Sonia Urlando:** So the style is correct.

**Sonia Urlando:** I think it was just the mismatch between what was in the body.

**Sonia Urlando:** And also there were some direct competitors.

**Sonia Urlando:** Like I think in this case, it was maybe Clockify that wasn't in the body of the article, but then like introduced in the TLDR sort of thing.

**Matthew Alves-Hill:** Got it.

**Matthew Alves-Hill:** Okay.

**Matthew Alves-Hill:** So is that, so, okay.

**Matthew Alves-Hill:** So there's, so there's a list of competitors we never want to mention, but if they're not direct competitors, then we would include these in the listicle.

**Sonia Urlando:** Okay.

**Matthew Alves-Hill:** Yeah.

**Matthew Alves-Hill:** Yeah.

**Matthew Alves-Hill:** If, if, we did have a listicle that.

**Matthew Alves-Hill:** Would the idea be that we just wouldn't include that specific competitor in a listicle?

**Matthew Alves-Hill:** Or if there's articles, yeah.

**Sonia Urlando:** I think the priority would be reflecting what's actually in the article.

**Sonia Urlando:** So say, for example, we have an inconsistency or there's an older article or, you know, just operating under a different kind of principle and we have some of those direct competitors in the body.

**Sonia Urlando:** That might be something that we would like edit in the body of an article like today when we're working on it.

**Sonia Urlando:** But the goal for TLDR would be to like reflect what content is there like accurately and succinctly.

**Sonia Urlando:** So rather than kind of a hard and fast rule with these, I think that like it should prioritize what's in the article.

**Sonia Urlando:** And there's a little bit more of like a bigger edit that would need to happen on our side around that kind of...

**Sonia Urlando:** Line of thought of not including direct competitors.

**Matthew Alves-Hill:** Gotcha.

**Matthew Alves-Hill:** Gotcha.

**Matthew Alves-Hill:** Yeah.

**Matthew Alves-Hill:** So just, so for context, like, let's say, let's say this was, this was all right.

**Matthew Alves-Hill:** Like there was no direct competitors to mention in here.

**Matthew Alves-Hill:** Is this the, this is the kind of like structure and length you're, you're happy with this output?

**Sonia Urlando:** Yeah, I think that this, so generally I think we're trying to aim more for like 150 to 200 words.

**Sonia Urlando:** When we start getting into the like 300 words, we're maybe getting a little long.

**Sonia Urlando:** So this could probably be shorter as well, but the general idea of having an intro, couple lines, the main takeaway of the article really being like, here's a quick look at the, um, uh, platforms that we're comparing and probably as, as an.

**Sonia Urlando:** And you're looking at this, I would probably choose like the, how to choose the right software.

**Sonia Urlando:** I'm thinking about like, what is a quick takeaway?

**Sonia Urlando:** How does somebody read the TLDR and get something functional out of the article while still getting benefit out of reading the whole thing?

**Matthew Alves-Hill:** Yeah.

**Matthew Alves-Hill:** Okay.

**Matthew Alves-Hill:** That makes sense.

**Matthew Alves-Hill:** Okay.

**Matthew Alves-Hill:** So that's something then.

**Matthew Alves-Hill:** Okay.

**Matthew Alves-Hill:** So that's cool.

**Matthew Alves-Hill:** That's something I can work back into the instructions because let me just give you a bit of context.

**Matthew Alves-Hill:** Um, so these new instructions I had built, like essentially to shorten significantly.

**Matthew Alves-Hill:** Um, and then when there is a listicle present, um, like basically have no listicle in the, in the TLDR to avoid the competitor mention.

**Matthew Alves-Hill:** I get now that I get your point now.

**Matthew Alves-Hill:** So that's something we can include back in and we can just think, we can just build a, like a very clear instruction that says any of these competitors, like, in the article, we never mentioned them in the TLDR and just.

**Matthew Alves-Hill:** Cut them out of the TLDR, because with the new instructions, this is the kind of output that I was moving towards.

**Matthew Alves-Hill:** So in a listicle, then instead of having the actual competitors, it was like, what matters most when you're choosing and how to pick wisely, right?

**Matthew Alves-Hill:** So it's taking like, it's giving the reader guidance on the analysis of the listicle, if that makes sense.

**Sonia Urlando:** But yeah, we don't have a listicle.

**Sonia Urlando:** as like, tangible.

**Sonia Urlando:** Yeah, and something else I want to make a point of as well with the TLDRs is we're thinking about this both like, from the reader perspective, like, what's the valuable takeaway that they can, like, quickly use?

**Sonia Urlando:** And also there is the kind of like, SEO, GEO, kind of like framework as well.

**Sonia Urlando:** Like, when we think about how queries are answered, one of the things...

**Sonia Urlando:** I think that would come up in the way that we're trying to structure them is if someone is searching for a kind of like middle of funnel, like how do I pick a software?

**Sonia Urlando:** They probably will see a list pretty similar to what we're trying to do with the TLDRs, which is like this software is good for this, you know, and list a couple options for someone to compare.

**Sonia Urlando:** So just to share a little bit of that as well as like kind of looking at it with both of those lenses when we're thinking about how to structure it.

**Matthew Alves-Hill:** So we have a listicle in the main body with key features to look for and how to choose the right one, right?

**Matthew Alves-Hill:** With the new instructions, we grab the key features and how to choose instructions.

**Matthew Alves-Hill:** And so in an ideal world, then, you would also have, like, a summary of the listicle in here as well.

**Matthew Alves-Hill:** So if, for example, we had, like, the, you know, the top five employee monitoring software, and then we had, like, bullet points of the five in here, then is that, like, that's kind of what your ideal structure looks like.

**Sonia Urlando:** Yeah, I think that is looking, like, more in line with what, with what we want out of the TLDRs.

**Matthew Alves-Hill:** Okay, okay, that's super helpful.

**Matthew Alves-Hill:** Okay, that's, that's an easy, that's an easy fix.

**Matthew Alves-Hill:** I think I, I have a good understanding now of what, what needs to be in there.

**Matthew Alves-Hill:** Yeah, okay, so that kind of, that's where, like, we've been going.

**Matthew Alves-Hill:** Effectively, now we have, like, a much more, we know that the, we know that the work,

**Matthew Alves-Hill:** Flow is reading the page correctly, and we have an easily manipulated set of instructions that we can now hone in.

**Matthew Alves-Hill:** I think in the past, perhaps, there was a little bit of talking past each other, and then rigidity, and how much we could tweak the pipeline.

**Matthew Alves-Hill:** But, yeah, I feel in a much, like, happier place about this, and I think now the next step is to generate a batch.

**Matthew Alves-Hill:** I see that we have some, let me just, we have some here that, like, I think we generated, but you weren't too happy with.

**Sonia Urlando:** I think, yeah, we did, like, a small sample of these to get started, and that's kind of where we got lost in the back and forth of trying to get the quality right.

**Sonia Urlando:** Yeah.

**Sonia Urlando:** This batch probably needs another look. We refresh so much content on a monthly basis that some of these may have been refreshed since. Writers are adding TLDRs as part of their process now, but there are examples here we could use for testing that haven't gotten a TLDR yet.

**Matthew Alves-Hill:** I did notice there were a couple of redirects, but that's fine. I'll find suitable articles to test. Now we'll test the batch and hopefully we're at a place where we can ramp up once we've proven this is working well. The TLDRs are in a much better spot.

**Matthew Alves-Hill:** I wanted to ask about the CTA structure. We put a generic instruction at the bottom asking it to link to the topic. Do we want a CTA in the TLDR? I know you were keen on the language and tone. Does it feel pushy?

**Sonia Urlando:** We've been moving toward CTAs that are organic to what's being written, not sales taglines. We're also introducing banner CTAs to our blog.

**Sonia Urlando:** So it might not be necessary. For simplicity, I think it would be okay to leave it out.

**Sonia Urlando:** Mark, I don't know if you have a different opinion on that.

**Mark Velarga:** I agree. We'll talk about it internally since we're testing internal linking. If it moves the needle, we could add it back, but for now we'll leave it out.

**Matthew Alves-Hill:** These instructions are easy to edit. I'll drop the CTA instruction and add a natural one-sentence flow into the main body for a natural reader journey.

**Matthew Alves-Hill:** I have everything I need. I'll choose suitable articles that aren't up for refresh and share them in chat for your approval. Next week we'll get you a batch to workshop. Once we get this right and you're happy, scaling is easy.

**Matthew Alves-Hill:** So, okay, that's great.

**Sonia Urlando:** Good.

**Sonia Urlando:** Thanks for your work on this.

**Matthew Alves-Hill:** No, it's a pleasure.

**Mark Velarga:** I have a quick update on a new project we want to test on the site.

**Mark Velarga:** It's similar to the glossary approach but focused on longer-tail query questions instead of keywords. We want to publish 50-60 pieces simultaneously to see what signals we get from LLM and SEO. The topics are "start your business" type questions from an operational standpoint.

**Mark Velarga:** Topics could include payroll or starting a business. We're doing research now and I'll create a brief with context on potential pipeline requirements. I'll send it over on Slack.

**Matthew Alves-Hill:** One more thing on glossary topics: we've exhausted the current batch as of this week. Do you have guidance on where we should look next for research?

**Sonia Urlando:** Let me take this back with the team. The last batch focused on hiring terms and we may have hit the end of that road. I'll look at what the gaps are and get back to you.

**Matthew Alves-Hill:** Perfect. That's everything. Jakub, do you have anything?

**Jakub Rudnik:** I'll send a UserPilot TLDR example that's similar to what we're discussing. It's not just about avoiding competitor mentions, but also user experience. Putting Homebase at the top of a TLDR feels pushy and contrary to brand guidelines. There were two directions here—competitor mentions and brand voice. We chose one way, but the feedback makes sense and we'll follow your lead. I'll share this as a visual reference of how SEO-focused companies handle it.

**Jakub Rudnik:** Matt covered everything I wanted today. For that project—do you use Profound?

**Mark Velarga:** Yes, Profound.

**Jakub Rudnik:** Good. I want to set up keyword tracking on that new pipeline in Scrunch after launch so we're tracking from two LLM citation tools. We can triangulate the data once we launch, so we'll coordinate setup properly.

**Mark Velarga:** Sounds good.

**Sonia Urlando:** Thanks, guys.

**Matthew Alves-Hill:** Ciao.
