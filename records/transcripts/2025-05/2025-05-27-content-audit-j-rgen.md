# Content Audit: Jürgen

<metadata>
date: 2025-05-27
time: 14:01 UTC
duration: 29 minutes
organizer: Matthew Panzarino
participants: Matthew Panzarino (GrowthX), Jürgen Linde (GrowthX), Matthew Alves-Hill (GrowthX)
fathom_recording_id: 64808538
fathom_url: https://fathom.video/calls/310481145
share_url: https://fathom.video/share/Z9Hi-pmq3wS1nbVpTWmLh7Win1hBji-k
source: fathom
enriched_on: 2026-03-04 15:30 UTC
</metadata>

---

## Summary

Matthew Panzarino conducted a content audit focusing on quality improvements in GrowthX's AI-assisted workflow outputs, identifying systemic issues like skeletal structures and overuse of brevity prompts that create bullet-heavy content. The team discussed implementing calibration articles for each client, creating client-specific writing guides based on feedback, and tightening the feedback loop between workflow builders and content creators to improve output quality at scale. Key actions include developing better training on the editorial mindset required for AI tool effectiveness, hiring for first-principles thinking rather than copywriting skills, and creating structured onboarding processes that integrate writing style guidelines into workflows from the start.

---

## Context

This was an internal GrowthX meeting between Matthew Panzarino (VP of delivery), Jürgen Linde (content operations), and Matthew Alves-Hill (delivery specialist) to review GrowthX's content generation workflows and outputs. The meeting focused on practical challenges with AI-generated content quality and consistency across client deliverables. Matthew Panzarino shared concrete examples from recent client work (particularly BAPI and AIMBIT) highlighting recurring structural and stylistic issues that appear in approximately 50-60% of live content. The discussion centered on how to scale quality output without overwhelming the team with manual work, balancing speed with editorial rigor.

---

## Relevance

**To GrowthX Delivery:**
- Skeletal, bullet-heavy output is a widespread pattern in current workflows (50-60% of live content) driven by "brevity" and "clarity" prompts; requires reframing prompts to target 2-5 sentence paragraphs instead
- Core topic sections should be expanded into narratives rather than left underdeveloped; headline topics often receive the least development despite being the article's premise
- Calibration articles at client kickoff should be paired with client-specific writing guides (demonstrated with AIMBIT example); this is now required SOP
- Polishing workflows and external tools (Perplexity) can help generate refined instructions, but need to be fed back into operational workflows
- New clients onboarded with calibration should have writing style and structure guidelines integrated into workflows at setup, not applied retroactively

**To GrowthX Business Development:**
- Client quality expectations often shift from quantity-first to quality-first once executives see published work; proactive quality improvement positions GrowthX ahead of that shift
- BAPI represents a typical account trajectory (quantity-focused initially, shifting to quality); early intervention prevents future friction
- Strong references and case studies depend on consistently high-quality output; current quality issues may impact reference-ability
- Account expansion depends on delivery quality; structural improvements to workflows directly support account growth conversations

**To GrowthX Hiring & Training:**
- Current hiring focuses on copywriting skills; should shift to testing first-principles editorial mindset (ability to critique and improve AI output, not just write original copy)
- New hire assignments now include editing AI-generated content and explaining the reasoning, not just rewriting; this screens for editorial capability
- Training needs to be grounded and practical (example videos of workflow interactions) rather than theoretical; Daniel's Loom videos were a starting point but insufficient
- Team members using external workflows more than AR Ops indicates tooling or training gap; clear guidance needed on when AR Ops is appropriate vs. when manual polishing is required

---

## Overview

- Current workflows often produce skeletal, bullet-point heavy content; need to focus on fleshing out core topics into narratives
- Calibration articles and client-specific writing guides are being implemented to improve output quality and consistency
- Training and hiring for editorial mindset (vs. copywriting) is crucial for effective use of AI writing tools
- Workflows need more than just keywords; more detailed instructions and context are required for quality output

---

## Key Topics

### Content Quality Improvement Strategies

  - Expand skeletal outlines into narratives, especially for core topics
  - Aim for 2-5 sentence paragraphs, using single sentences sparingly for emphasis
  - Avoid overuse of "brevity" or "clarity" in prompts, which can lead to overly concise output
  - Focus on developing the most important sections, even if the overall structure seems adequate

### Workflow and Prompt Refinement

  - Tighten feedback loop between workflow builders and content creators
  - Create client-specific writing guides (e.g., AIMBIT guide) based on edits and client feedback
  - Integrate writing style and structure guidelines into workflows during client onboarding
  - Experiment with external tools (e.g., Perplexity) to refine prompts based on feedback

### Training and Hiring for AI-Assisted Content Creation

  - Develop better training for using AI tools effectively
  - Hire for "first principle" editorial mindset rather than just copywriting skills
  - Implement assignments testing ability to critique and improve AI-generated content
  - Consider recording examples of expert interaction with the grid and workflows for training

### Client-Specific Challenges

  - VAPI project highlighted issues with product-specific content generation and reliance on marketing copy
  - Balancing quality expectations with scale and efficiency remains a key challenge
  - Some clients (e.g., BAPI) may initially prioritize quantity over quality, but this often changes

---

## Action Items

**Matthew Panzarino (GrowthX)**
- Record example of working through grid + generating article from keyword to final output — showing interaction with AR Ops and polishing workflow to demonstrate realistic workflow steps for team training

---

## Transcript
**Matthew Panzarino:** First one, so I'm to go the hardest.

**Jürgen Linde:** No, I'm kidding.

**Matthew Panzarino:** So the, okay, this is a fun one to start with, obviously, because, we all know how BAPI is.

**Jürgen Linde:** Yeah.

**Matthew Panzarino:** Pretty.

**Jürgen Linde:** They're more like, they're not quality-intense.

**Jürgen Linde:** They're more just quantity-intense right now.

**Matthew Panzarino:** But I know eventually that would change.

**Jürgen Linde:** Yeah, exactly.

**Matthew Panzarino:** That's basically the way it works, right?

**Matthew Panzarino:** Like they're going to say, oh, we really care about quantity and we want to be all happy and loose and fast and free.

**Matthew Panzarino:** Until one of them happens to see something in an article, in an executive review, and they're like, oh, why are you not paying attention to this?

**Matthew Panzarino:** Or, you know, whatever.

**Matthew Panzarino:** Or their legal team sees it or, you know, anything, right?

**Matthew Panzarino:** So I am always happy to vibe with customers and all that.

**Matthew Panzarino:** But we should be preparing for the moment when it turns the corner into like, oh, why isn't this, you know, why haven't we been focusing on quality?

**Matthew Panzarino:** And why isn't quality our number one, our north star and blah, blah, blah, blah.

**Jürgen Linde:** I've been there.

**Matthew Panzarino:** Yeah, exactly.

**Matthew Panzarino:** You guys all know how it goes.

**Matthew Panzarino:** So, yeah, I went through this.

**Matthew Panzarino:** I did record a lumen stuff, so I won't like go super ad nauseum.

**Matthew Panzarino:** But what I have found like architecturally working through these things is that a lot of the default outputs have a couple of things in common.

**Matthew Panzarino:** The, our use of like brevity or brief or clarity or simplicity in the initial generation prompts and in the workflows tends to cue all of these pieces towards skeletal output, like a lot of bullet points, a lot of H2s, bullet points, H3s, bullet points, you know, single line sentences for introductions, all of that.

**Matthew Panzarino:** Thankfully, like, you know, you've done the work on this piece and like, it didn't really fall prey to a lot of that.

**Matthew Panzarino:** But there were some, some ways to lean in here and just expand some of the more points out a little bit.

**Matthew Panzarino:** And I think that that is a byproduct of like, prompted output is that a lot of times, hey, this is actually correct.

**Matthew Panzarino:** It has all the main points in it.

**Matthew Panzarino:** I think we're good here.

**Matthew Panzarino:** And then peace out.

**Matthew Panzarino:** When in reality, it's like, just a step back and thinking like, okay, what's the core tenets of this piece?

**Matthew Panzarino:** They should be treated a little bit differently than the other parts of it.

**Matthew Panzarino:** So, as an example, if we get like, two or three sections back to back that are like, one or two lines, bullet points, one

**Matthew Panzarino:** Two lines, bullet points, H3, and you get two or three of those back-to-back.

**Matthew Panzarino:** It's like, okay, this actually seems like it serves the purpose.

**Matthew Panzarino:** It's got the keywords in, it covers the topics, everything seems okay from a structural or from an inclusion perspective.

**Matthew Panzarino:** Like, what do we have in here that needs to be in here?

**Matthew Panzarino:** And then go, okay, step back, though.

**Matthew Panzarino:** What's, like, the core piece of this article?

**Matthew Panzarino:** A lot of times where I found, not in this case, but a lot of times what I found is, you know, you'll have an article that'll have a topic in the headline.

**Matthew Panzarino:** It'll be like, hey, this is a guide to X or, you know, this is about Y.

**Matthew Panzarino:** And that piece will be the least developed component of the whole article.

**Matthew Panzarino:** You know, so you, the opportunity to expand that component is, like, right in your face.

**Jürgen Linde:** Like, there was a piece about, like, pricing of a particular cloud plan.

**Matthew Panzarino:** And the pricing section was just, like, I don't know, it could cost, like, this much.

**Jürgen Linde:** And it was, like, peace.

**Matthew Panzarino:** It was very easy to take that outline in that section and just feed it back in to either our workflow or polishing workflow or even a chat window for now until we get that cycle all built for ourselves.

**Matthew Panzarino:** But it was very easy to take that and say, hey, build a narrative off of this.

**Matthew Panzarino:** Like spool this out into a narrative.

**Matthew Panzarino:** Give me more detail and more specificity.

**Matthew Panzarino:** And it came back with stuff that's pretty good.

**Matthew Panzarino:** So I think just a lot of times what we end up with is we get into a state where we're like, hey, this is good enough.

**Matthew Panzarino:** And really, we should just lean in a little bit more.

**Matthew Panzarino:** Like this section here was just really about, you know, picking these bullets and then expanding them into a little bit more of a narrative, which creates a better flow for the piece.

**Matthew Panzarino:** creates a better, like, scene setting.

**Matthew Panzarino:** And I think a lot of the prompting issues come from this clarity and brevity thing.

**Matthew Panzarino:** If you are able, if you take it to, like, hyperspace.

**Matthew Panzarino:** Think about it and say, please make all the paragraphs two to five sentences.

**Matthew Panzarino:** You can use single sentence paragraphs only for emphasis of a core point or sparingly, right?

**Matthew Panzarino:** And then just give it those instructions.

**Jürgen Linde:** It generally will turn out pretty well.

**Matthew Panzarino:** You know, like you can give various models those instructions and it will flesh it out pretty well.

**Matthew Panzarino:** And then the app with most LLMs, it will never tell you no.

**Matthew Panzarino:** So if you give that and it gives you an answer back, you can choose not to use it, you know?

**Matthew Panzarino:** But there may be chunks of it that you can use to flesh things out.

**Matthew Panzarino:** Editing this piece, like taking this feature breakdown and turning it into a narrative component was not something that I am, and I should have said this at the top.

**Jürgen Linde:** None of these changes are like, you must do this with every article.

**Matthew Panzarino:** I'm just showing you ways that like we should probably alter our framework for deciding what looks and feels good.

**Matthew Panzarino:** That helped improve the overall output.

**Matthew Panzarino:** I'm going to say, like, I don't, I think this piece was pretty good already for Bappy.

**Matthew Panzarino:** And some of these things are very, like, these are more academic exercises because the in-brief section, I think, is something that they want, right?

**Matthew Panzarino:** Like, that's a client mandate.

**Jürgen Linde:** Not necessarily, but yeah.

**Matthew Panzarino:** Yeah, okay, good.

**Matthew Panzarino:** Well, that's good to know.

**Matthew Panzarino:** Some of the clients do, right?

**Matthew Panzarino:** They're like, we want an in-brief.

**Matthew Panzarino:** Like, we, you know, their internal content team believes very strongly that an in-brief section is the best way to go.

**Matthew Panzarino:** I don't agree, really, necessarily, but that's okay.

**Matthew Panzarino:** You know, if they mandate in-brief, leave it in.

**Matthew Panzarino:** But an in-brief section is easily transferable into an introduction, right?

**Matthew Panzarino:** And it's just, you're turning that into a narrative that says, hey, here are the things that we are about to do, about to talk about. Like, let's teach you in that place so that you're ready to read, and I think that the core tenet obviously should be build the outline and architecture from things, and then make sure that it's human readable, and at the end, execution is human readable.

**Matthew Panzarino:** And I think that's, that's kind of where we, so, just to fix it in here, you can look over, and if you have any questions, you can know, but that's basically the gist of it that I found in a lot of these cases, human like, opportunities to flesh out sections that are a little anemic, especially if they are, you know, kind of like a core performance part of it, or core part of the article's premise.

**Matthew Panzarino:** I think those are, those are major things that I thought, but, make sense?

**Jürgen Linde:** Yeah, yeah, definitely.

**Jürgen Linde:** Like, a lot of these things I've been taught myself before, um, I just, I think what happened with this article is that it got lost in translation.

**Jürgen Linde:** The many iterations we had initially, and I think as well, our workflows are not ideal, and it's a very tricky thing to have a generalizable polishing instruction that actually gets consistent outputs, and this is just general feedback, like this article ended up having a lot of manual work, but Matt and I were discussing that.

**Jürgen Linde:** It's quite difficult to get our workflows just to sort of listen to us, and I think someone mentioned this before, think Jess, that you can expect one output from one prompt, use the exact same thing again, and it won't do it well at all, and it's a very hit and miss thing that you have to deal with.

**Jürgen Linde:** And I know it's something we should be discussing about often and bringing it up, but the problem we're facing is how can we generate quality content at scale at this level that doesn't require like all the human.

**Jürgen Linde:** Like, we want to get to a point where it does most of the work for us, but that's the hurdle, the bottleneck.

**Matthew Panzarino:** Yeah, I think there's a combination of things going on.

**Matthew Panzarino:** One of the things that, you know, we are addressing is, like, trying to get a tighter loop between, you know, what the workloads are actually delivering, what people think they are delivering, you know, on the build side, and then what they are actually delivering.

**Matthew Panzarino:** I think it's important to keep that loop tighter.

**Matthew Panzarino:** We're having a meeting about that today, and we'll continue to do so.

**Matthew Panzarino:** There's also, you know, prompting is an interesting thing, because it is not a one-size-fits-all.

**Matthew Panzarino:** It can be, like, there can be ways to help.

**Matthew Panzarino:** There are ways to help.

**Matthew Panzarino:** So, one of the actions that I'm doing now is, every kickoff, I'm doing calibration articles with the directors and MEs. Any calibration articles we produce for any client now, I'm going to take a look at and I'm going to go through.

**Matthew Panzarino:** And I've already done that exercise with one of our clients, which is Aimbit.

**Matthew Panzarino:** And that was a good exercise to go through to see kind of like where, what our workflows were putting out, you know, as far as calibration pieces for top of something we're interested in, how far we needed to get to where we needed to go.

**Matthew Panzarino:** And then on the other side of it, David did an interesting thing.

**Matthew Panzarino:** I'm going to have him share it, but he wrote a writing guide or collated, really, a writing guide. He didn't write it manually, but collated a writing guide based on the edits that Jacob and I made and the feedback, thankfully, that was very, very good and very pointed from Aimbit on what they wanted.

**Matthew Panzarino:** And created a writing guide for Aimbit that we can use going forward that has like a lot of specificity.

**Matthew Panzarino:** About what they want, what they don't want, you know, the things that they care about.

**Matthew Panzarino:** This is, you can see it here, this is the kind of refined instructions for AIMBIT.

**Matthew Panzarino:** And it's, you can see it's very detailed, right?

**Matthew Panzarino:** You know, subtle call to action, if including a CTA, clean, non-intrusive, you know, to the end.

**Matthew Panzarino:** Understanding their core identity, focusing on their problems.

**Matthew Panzarino:** So this is very, very, very specific.

**Matthew Panzarino:** He used perplexity for this, so he didn't manually write this.

**Matthew Panzarino:** But it ingested all of our instructions, and then, of course, you can review it and make sure that it actually is correct.

**Matthew Panzarino:** But there's a lot of...

**Jürgen Linde:** There is actually something that Matt did today. He took all your comments and feedback and made a new prompt based on that.

**Matthew Alves-Hill:** You can chime in if you have extra stuff to say, Matt.

**Matthew Alves-Hill:** Yeah, go ahead, go ahead.

**Jürgen Linde:** No, I was just saying that Matt made a prompt based on all the feedback that you gave us today.

**Jürgen Linde:** I didn't necessarily feed it into the workflow because it's too beefy to handle at this point.

**Jürgen Linde:** But the output was much better than what the workflow generated itself.

**Jürgen Linde:** So that's definitely a good exercise, what you're showing right now.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** And did you see the feedback in the content audit hub?

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** So that can also be used.

**Matthew Panzarino:** Nana collated that.

**Matthew Panzarino:** So that's not something that I wrote manually, but she collated that out of my comments on those pieces.

**Matthew Panzarino:** But then I also came up with my own kind of specific instructions.

**Matthew Panzarino:** So I'll try and host those or share those at some point as well.

**Matthew Panzarino:** I'll refine them a little bit more, but just as some general guidelines of things that I found.

**Matthew Panzarino:** And these are, I do not view that as like, oh, this is the only way to get good output.

**Matthew Panzarino:** It's just current issues that I see very repeatedly across all of our content.

**Matthew Panzarino:** Like there's a bunch of things that you have, you know, like in the vacuum piece that you've already done away.

**Matthew Panzarino:** The vast majority of them, because, you know, you guys did good work there, but there's, I would say 70% of our headlines, blah, blah, blah, colon, blah, blah, blah.

**Jürgen Linde:** That's stupid.

**Matthew Panzarino:** It's a huge LLM pattern, anti-pattern, and it's just very easy to get rid of, right?

**Jürgen Linde:** So I think the part of it is just getting numb to the output, right?

**Matthew Panzarino:** And that's why I'm talking to people and being like, hey, you know, pay attention, please.

**Matthew Panzarino:** Because, like, there's a lot of stuff that's really easy to, not easy, I shouldn't, I don't want use the word easy, because I don't want to, like, reduce, be reductive about this.

**Matthew Panzarino:** But it is very obvious and straightforward that some of these things need to change.

**Matthew Panzarino:** That colon, the headline, the single sentence, the H3 single sentence bullet point single sentence H3 construction, that's an outline.

**Jürgen Linde:** That's not an article, right?

**Matthew Panzarino:** And, like, 50 to 60% of our content has that in it.

**Matthew Panzarino:** Live right now, I would be shocked if people weren't looking at it and going, why did we hire these guys?

**Matthew Panzarino:** So I think that's something to watch out for.

**Matthew Panzarino:** I think that the contextual part of it, and this is something that I think obviously Matt does well, but one thing to keep an eye out for is I did find about 20% of the articles that we have where there's a good chunk of articles, maybe not a quarter, but that really kind of hallucinate information and it's still in the article.

**Matthew Panzarino:** Like there was an article about hub and spoke models for data architecture.

**Jürgen Linde:** That was something we actually talked about today, that when we're researching product stuff, especially, it tends to hallucinate a lot. And Matt can speak to that, because VAPI's articles were talking a lot about VAPI-specific stuff. And it seems like every time the research gen is run, it only uses the marketing copy that's straight from a client's landing page.

**Jürgen Linde:** And there's not real information to be found online that can, you know, make an informed article.

**Jürgen Linde:** It's like there's a lot of the manual work that we have to deal with.

**Matthew Alves-Hill:** Yeah, I think there's like two things I'm thinking about.

**Matthew Alves-Hill:** Like number one, Panzar, like this, the contents, like the quality, the content quality side, the points that you're putting out, like absolutely 100% on board, agree with like everything you're saying.

**Matthew Alves-Hill:** There's like no doubt that that's the kind of quality that we want to put out.

**Matthew Alves-Hill:** But then there's like, on the other hand, there's like the, I don't know, capability and like feasibility of doing that at scale for the, like, that's one part, but also like using the grid to, like in some cases.

**Matthew Alves-Hill:** I'm sure that I expect as you have more meetings, you might find that actually it's almost basically generating an article completely out of air ops is sometimes more efficient in a way.

**Matthew Alves-Hill:** Now, what would be really interesting for me is if you could record some examples of yourself going through one of these grids and generating an article and then whether you're then taking it out and polishing it with whatever model you might be using.

**Matthew Alves-Hill:** Like, I think it would be really, like, the onboarding training was kind of, like, here's the grid and this is going to, like, these are how the articles are going to be finished.

**Matthew Alves-Hill:** And then it's like, you should, in theory, be able to copy and paste straight out of that into, and I know.

**Matthew Alves-Hill:** That's not the case, and we're humans in the loop.

**Matthew Alves-Hill:** At the end of the day, there needs to be, but I think there's probably not a lot of clarity around what's good practice and what's not.

**Matthew Alves-Hill:** What can we expect, what we can't.

**Matthew Alves-Hill:** And I understand it's developing and there's improvement all the time, but polishing instructions seem like you have this one shot to try and improve the article, and then you need to go back and A, test it, and then it's tried and slightly improve and slightly improve.

**Matthew Alves-Hill:** So I find the relationship with the grid and then what we're ultimately giving to clients, I think that's like, it would be great to have more guidance from growthx, I guess.

**Matthew Alves-Hill:** This is where we're at right now.

**Matthew Alves-Hill:** This is the kind of heavy lifting that we need to still do. This is what we can expect from the grid because I see the value. When we were rushing for VAPI last week, it was helpful to, like, Marcel was like, look, just crank, you know, and just whatever's being put out, like, a rough edit and then just put it on the website.

**Matthew Alves-Hill:** We just need to give them 40 articles.

**Matthew Alves-Hill:** But, you know, Marcel is obviously going to be a lot better at, like, polishing or prompting or knowing how to use the grid than I perhaps might be.

**Matthew Alves-Hill:** So I think it's, like, you know, for new joiners on the grid specifically, like, how do we get, how do we just train to a level using the grid that that's an acceptable standard?

**Matthew Alves-Hill:** Like, that's where I find myself.

**Jürgen Linde:** I feel like it's an open secret that people use external workflows more than the actual AR Ops.

**Matthew Panzarino:** It's not a secret. I think it is open.

**Jürgen Linde:** Yeah, I agree.

**Matthew Panzarino:** We definitely need to figure out ways to improve those.

**Matthew Panzarino:** And that's what the delivery meeting is today.

**Matthew Panzarino:** We're talking about where the grids are, where they need to be, and what we need to include.

**Matthew Panzarino:** I think better prompting is part of it.

**Matthew Panzarino:** Using the calibration time to come up with writing styles for each client is not done currently.

**Matthew Panzarino:** You know, it's not anywhere in the flow.

**Matthew Panzarino:** And like creating a custom style, like this one that I happened to share from Invit, but like this kind of document fed into a workflow as publishing instructions or voice instructions can get you a long way towards something that's more usable.

**Matthew Panzarino:** And that's not currently part of that SOP in like, you know, how we go about calibrating a new client.

**Matthew Panzarino:** And it's becoming one, right, as we speak.

**Matthew Panzarino:** And so I think there's a lot of like, if the Vappy onboarding, I hate to use Vappy as an example.

**Matthew Panzarino:** I only did it because this is a recent example, and we did it, right?

**Matthew Panzarino:** And so I don't want you to hyper-focus on anything that I changed in this particular article.

**Matthew Panzarino:** I just was using this as an exercise, right?

**Matthew Panzarino:** And Matthew is such a unique, weird client because we onboarded them with an SoW that we don't have the ability to build on the fly.

**Matthew Panzarino:** So let's set that aside for the moment, right?

**Matthew Panzarino:** Like if during the onboarding of a client where we did have a work stream currently active, let's say editorial organic content for their blog.

**Matthew Panzarino:** So that was a simple work stream.

**Matthew Panzarino:** Okay, we're onboarding this.

**Matthew Panzarino:** When we're doing the onboarding and calibration, first of all, the sprint team is going to go a lot harder on this from now on.

**Matthew Panzarino:** Having a team dedicated to kickoffs should get us a long way towards having a lot of this calibration work done so that they have a lot of voice and tone and writing guidelines.

**Matthew Panzarino:** All that in place and sort of architecture in place to make sure that the workflows are tuned to them.

**Matthew Panzarino:** Because right now we just copy the workflows into a folder and then start running them.

**Matthew Panzarino:** And that really should be, okay, hey, we've onboarded a new client.

**Matthew Panzarino:** We're going to take the big templates of our workflows and integrate writing style and structure guidelines like these you see here.

**Matthew Panzarino:** And a bunch of probably other tweaks for that particular client according to their desires.

**Matthew Panzarino:** And that workflow may be, you know, a dozen steps versus six steps.

**Matthew Panzarino:** You know, because of that particular client.

**Matthew Panzarino:** And when we're running it and doing the intervention, we're in the 80th to 90th percentile versus in the 20th percentile.

**Matthew Alves-Hill:** I wonder if it would be interesting for onboarding...

**Jürgen Linde:** I was just going to say, I wonder if it would be an interesting exercise for onboarding hires. Maybe in addition to, or maybe just a replacement instead of doing the big assignment, you could have an exercise where you train people to get a final output that's as workable as possible. Because when I started, I watched Daniel's Loom videos over and over again to conceptualize how AR Ops works in general. But there was minimal training on how to make it work for you. Maybe there was an assignment where the prompting side of it was the exercise, and the final output is just a measure of how well you can prompt.

**Matthew Panzarino:** Yeah, that's part of the chat we'll have later today.

**Matthew Panzarino:** It is, we need better training for sure, and we need more realistic, kind of like grounded training in, okay, how do you exactly do this?

**Matthew Panzarino:** Here's part of the problem, though.

**Matthew Panzarino:** I think that some of the CMs that we are hiring, and some of the ones that we have hired, just don't have that first principle mindset.

**Matthew Panzarino:** Like, they're never going to be good writers, they're copywriters, and they're probably good at that, and in many cases great at that.

**Matthew Panzarino:** But this mentality is different.

**Matthew Panzarino:** It's an editorial mindset. Imagine if your writer was intelligent but had no idea how to put sentences together — imagine if your writer said, "I know all the words in the English language, but I have no idea how to put them together."

**Matthew Panzarino:** Like, how accurate, you know, would you be?

**Matthew Panzarino:** How articulate would you have to be with them about what you expect and how to get good outputs?

**Matthew Panzarino:** And I think that we have to hire more for that mindset and we will do that.

**Matthew Panzarino:** And then, of course, the people that are on or have already been hired, we have to train, right?

**Matthew Panzarino:** And we have to find ways to upskill and lean into that.

**Matthew Panzarino:** And out of that will come, very obviously, improvement.

**Jürgen Linde:** I think what would be a good measure of how good someone actually is in their job, instead of looking at someone with a good track record in their CV or resume, is if assignment is part of the application where you get given something that's straight from AR Ops and have to critique it.

**Matthew Panzarino:** Yeah, it's already in there.

**Jürgen Linde:** I already did it.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** I added it last week, yeah, because it's like, hey, we can't hire people and expect them to do this, and I have no idea whether they're good at it.

**Matthew Panzarino:** So we give them raw output and then have them edit it.

**Jürgen Linde:** Yeah, not just edit, but like say why this piece is not functioning well.

**Matthew Panzarino:** Yeah, they need to not just edit it.

**Matthew Panzarino:** They need to explain why they edit it, what their thought process is.

**Matthew Panzarino:** because people that can articulate that can articulate it to a workflow just as well as they can to another human, right?

**Matthew Panzarino:** And like the prompting aspect of it is really just the format you put it in.

**Matthew Panzarino:** But this is all really good feedback, and I'm not shooting any of this down.

**Matthew Panzarino:** I'm actually talking to people because of this.

**Matthew Panzarino:** So thanks.

**Matthew Alves-Hill:** I have to jump to my next one, but there'll be more opportunity to talk this over a little bit later today, too, in our delivery.

**Matthew Alves-Hill:** Amazing.

**Matthew Alves-Hill:** Yeah, just before you go, I want to reiterate that it would be incredible for me to see an example of you going through one row of the grid — here's a keyword, and here's how we get to a final result. That would be super cool.

**Matthew Panzarino:** So, I'll show you how I interact with the grid.

**Matthew Panzarino:** You also need to give the workflows more than keywords, by the way.

**Matthew Panzarino:** I mean, keywords are not enough in the slightest, you know.

**Matthew Panzarino:** Sure, keyword is a seed, but it's quite obvious that our workflows do not build good content off of single keywords.

**Matthew Panzarino:** They need more instruction, but we'll get there.

**Matthew Panzarino:** But, yeah, I'm happy to do that.

**Matthew Panzarino:** I'll get into it.

**Matthew Panzarino:** I have done it.

**Matthew Panzarino:** I can record it and show you where I'm at.

**Matthew Panzarino:** All right.

**Jürgen Linde:** Cool.

**Jürgen Linde:** Good.

**Matthew Panzarino:** Cool.

**Jürgen Linde:** Thanks so much.

**Jürgen Linde:** Ciao.
