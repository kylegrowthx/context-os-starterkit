# Baseten <> GrowthX - Weekly Sync

<metadata>
date: 2025-10-23
time: 16:00 UTC
duration: 33 minutes
organizer: team@growthxlabs.com
participants: Andi Bailey (GrowthX), Aida Knezevic (GrowthX), Stevie Kim (GrowthX), Marylise Tauzia (Baseten), Mike Bilodeau (Baseten)
fathom_recording_id: 96328632
fathom_url: https://fathom.video/calls/449547986
share_url: https://fathom.video/share/YMmzG2LhNn1d_jVSxdbyp2Aass-X8p9u
source: fathom
enriched_on: 2026-03-02 14:30 UTC
</metadata>

---

## Summary

GrowthX and Baseten aligned on a major content strategy pivot: creating a separate "Learning Center" for foundational, 101-level content (including a comprehensive glossary) while keeping the main blog focused on practitioner-level, technical depth targeting sophisticated engineers and founders early in their product journey. Baseten emphasized that all content must deliver actionable tradeoffs and insights rather than surface-level specs, and noted they're reviewing samples from GrowthX's refined AI pipeline (tested by CTO Daniel with a 1-week reference time) to assess if it can match the technical quality bar set by Modal's GPU glossary. GrowthX will deliver outlines, blog drafts, and glossary samples by week's end for review.

---

## Context

Baseten is an AI infrastructure platform for LLM and model inference at scale. This is a weekly sync between Baseten's content and product team and GrowthX, a B2B content marketing agency ($200k+/year engagements). The relationship revolves around GrowthX building high-quality content and glossaries to establish Baseten's authority in the AI inference space, drive organic search traffic, and reach both early-stage founders and engineers early in their product journeys. Baseten introduced Stevie Kim, a product manager and former MLOps engineer with DevRel experience at companies like Algorithmia and DataRobot, to refine content and GrowthX's agentic pipelines. The call followed up on earlier content submissions and focused on validating the strategic pivot to separate 101-level foundational content (in a Learning Center) from expert-level blog content.

---

## Relevance

**To GrowthX Delivery:**
- Content quality bar is extremely high: factual accuracy is non-negotiable ("getting details wrong is pretty much like bar none unacceptable"). Baseten benchmarks against Modal's GPU glossary as the quality standard.
- Target audience is narrowly defined: sophisticated engineers and founders early in product development, not hobbyists or undergraduates. Content must provide practitioner POV with tradeoffs (quality vs. cost vs. speed).
- Two-track content strategy approved: Learning Center for SEO-focused 101-level content, main blog for technical depth. This requires careful structure and messaging to avoid brand dilution.
- GrowthX's refined AI pipeline (CTO Daniel's work) shows 1-week reference time on published articles — this is a proof point to validate against additional samples before full production.

**To GrowthX Business Development:**
- Baseten is evaluating whether GrowthX can deliver the technical depth required. Approval hinge on glossary samples, blog drafts, and comparison to Modal's quality bar.
- Potential for expanded scope: repurposing Baseten's internal expert content (blog posts, webinars) through GrowthX's pipeline could create additional content streams.
- Account is at a critical checkpoint: Mike and Marylise are evaluating whether to move forward with broader content production or handle some work internally.

---

## Overview

- **Content must be practitioner-focused, not 101-level.** The target audience is sophisticated engineers and founders, not hobbyists or students. Content must provide actionable tradeoffs and insights, not just specs.
- **A new "Learning Center" is needed to house SEO-driven content.** This separates it from the main blog, protecting the brand's credibility with its expert audience.
- **The proposed LLM inference glossary must be expanded to cover all inference types.** It must also meet the high-quality, technical bar set by competitor Modal's GPU glossary.
- **GrowthX will deliver new samples (glossary terms, outlines) for review.** These will test if their AI pipeline can meet Baseten's technical depth requirements.

---

## Key Topics

### Content Quality & Audience Alignment

  - Baseten's core concern is protecting its brand credibility with a highly technical audience.
  - **Target Audience:** Sophisticated engineers and founders who are early in their product journey but have deep technical knowledge.
      - **Not:** Hobbyists, undergrads, or those needing 101-level explanations.
  - **Content Standard:** Must provide actionable insights and tradeoffs (e.g., quality vs. cost vs. speed) from a practitioner's POV.
      - **Rationale:** This contrasts with surface-level content (e.g., NVIDIA marketing specs) that is perceived as "for bots" and would damage Baseten's credibility.

### Proposed Solution: A "Learning Center"

  - To resolve the conflict between SEO and brand credibility, Baseten proposed a separate "Learning Center" section on the website.
  - **Purpose:** House foundational, 101-level content (e.g., glossary terms, beginner guides) that is valuable for SEO but not suitable for the main blog.
  - **Benefit:** This structure allows Baseten to capture top-of-funnel traffic without diluting its expert brand.

### Glossary Proposal & Quality Benchmark

  - GrowthX proposed a glossary of 200+ LLM inference terms to build authority and drive SEO.
  - **Baseten's Feedback:**
      - **Scope:** Must expand beyond LLM inference to cover all inference types Baseten supports.
      - **Quality:** Must meet the high technical standard set by competitor Modal's GPU glossary.
      - **Location:** Should be a standalone section (`/glossary`), not part of the blog.

### GrowthX's AI Pipeline & New Samples

  - GrowthX introduced Stevie Kim (PM, ex-MLOps) to refine content and agentic pipelines.
  - GrowthX's CTO, Daniel, has been fine-tuning their AI pipeline to meet Baseten's technical requirements.
  - **Proof Point:** Daniel's internal articles, built with the refined pipeline, show a 1-week reference time, suggesting the pipeline can deliver the required depth.

---

## Action Items

**Mike Bilodeau (Baseten)**
- Share PyTorch/NVIDIA talk link with Baseten team

**Andi Bailey (GrowthX)**
- Email Mike/Marylise: 2 outlines, 3 blog drafts, glossary samples, recent AI-built articles, Learning Center/Glossary proposals
- Review Modal GPU Glossary; assess feasibility of matching quality

---

## Transcript
**Marylise Tauzia:** This meeting is being recorded.

**Marylise Tauzia:** Good morning.

**Aida Knezevic:** Hi.

**Andi Bailey:** Hi, Marylise.

**Marylise Tauzia:** Hello.

**Andi Bailey:** How are you?

**Marylise Tauzia:** Good.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Everyone should be added to the agenda.

**Aida Knezevic:** So you should be getting it in your email inbox via Notion.

**Marylise Tauzia:** Okay.

**Marylise Tauzia:** Sorry, I'm running around because we have a launch in a bit.

**Marylise Tauzia:** I nearly asked you to move the meeting, but I'm like, let's go for it.

**Marylise Tauzia:** Is anybody on the basis yet?

**Marylise Tauzia:** I just want to sure.

**Marylise Tauzia:** Just ping Mike to see if he's going to join.

**Marylise Tauzia:** Okay, he's arriving at the office, so give us a second.

**Andi Bailey:** Yeah, no worries.

**Andi Bailey:** I think we can also make this real.

**Andi Bailey:** Relatively quick and just like give you the new kind of direction and give you guys some things to chew over and then we can follow up async.

**Marylise Tauzia:** Good.

**Marylise Tauzia:** If he's coming, just grab a conference room, give me a second so that we can be together.

**Marylise Tauzia:** I'm going to connect to the TV and then we can get started.

**Marylise Tauzia:** Then you will join.

**Marylise Tauzia:** Recording in progress.

**Mike Bilodeau:** Hey, sorry.

**Mike Bilodeau:** Hey, sorry, it's Mike joining.

**Mike Bilodeau:** just on the road.

**Andi Bailey:** Hi, Mike.

**Mike Bilodeau:** Are we good?

**Andi Bailey:** Perfect.

**Andi Bailey:** Yeah, I think we are good.

**Andi Bailey:** We brought another person to the call today, wanted to introduce you all to Stevie, who I think we referenced in a message, but Stevie is our product manager and has spent a lot of time in this space, had a blog, and has written kind of DevRel content in the past.

**Andi Bailey:** And so Stevie is going to be reviewing our content, everything before it goes out, and is going to be helping to refine the agentic pipelines that we're

**Mike Bilodeau:** or building specifically for BaseTen.

**Mike Bilodeau:** Hi, nice to meet you.

**Stevie Kim:** Yeah, nice to meet you too.

**Stevie Kim:** Yeah, I've done DevRel and I was an engineer and I've worked in the MLOps space for most of my career.

**Stevie Kim:** Algorithmia, small startup out of Seattle, DataRobot, and, you know, various others.

**Stevie Kim:** So I've been in the space for a long time.

**Stevie Kim:** So thank you for actually recommending that PyTorch, NVIDIA talk on Slack. Oh man, I watched it last night and it was one of the best talks that I've seen in a long time.

**Stevie Kim:** So thanks for recommending that. It was super fun to watch. You know, a lot of it was review, but a lot of it was new learnings too.

**Mike Bilodeau:** So appreciate that.

**Mike Bilodeau:** Yeah, you're welcome. Everybody here at BaseTen should listen to it.

**Andi Bailey:** Awesome.

**Andi Bailey:** So then just the other pieces to close the loop on are...

**Andi Bailey:** We redid the outline and we actually came up with two versions of the outline on that initial piece of content that we had submitted last week, two weeks ago.

**Andi Bailey:** So there were a couple of angles that we could have taken.

**Andi Bailey:** So we thought we would just present both to you as options.

**Andi Bailey:** One of them is obviously a little bit more SEO friendly.

**Andi Bailey:** One of them is a little bit more on the technical informational side.

**Andi Bailey:** So both of those are for review.

**Andi Bailey:** And then I believe that we will have three more by, I think, by the end of the week, possibly by Monday at the latest for review as well.

**Andi Bailey:** Those are, they will also be kind of more informational.

**Andi Bailey:** And then the piece that I think we should talk about today is the glossary content specifically. We made some suggestions and have questions. We can talk about what we think is possible, where we want to start, and kind of how we would build out our technical capabilities here.

**Andi Bailey:** So we added over 200 terms related to LLM inference, and so those are in that, yeah, in the content OS for you.

**Andi Bailey:** And so there are, like, more technical and more basic terms, really thinking about, like, top of funnel SEO discovery, and also just, like, building out authority by making sure that we're, we have really comprehensive coverage of, like, terms related to the space.

**Andi Bailey:** So those are the update, and we were thinking that glossaries would perform quite well in terms of driving traffic and building authority.

**Andi Bailey:** So I would love to get you guys to review that after this call and let us know what you think there.

**Andi Bailey:** Any questions on the glossary piece?

**Mike Bilodeau:** Yeah, two questions.

**Mike Bilodeau:** One, so you just took taking the NNM inference like narrower topic rather than just full inference.

**Mike Bilodeau:** And that's on purpose to focus on just LNM?

**Andi Bailey:** Because we do inference more than just LNMs.

**Andi Bailey:** Yeah, that is where we started.

**Andi Bailey:** If you'd like us to broaden it out, we can.

**Andi Bailey:** So we have like 200 here, but certainly can keep building from there.

**Mike Bilodeau:** Yeah, I guess I'm curious, like, what was the rationale for that?

**Andi Bailey:** Uh, Sydney on the call?

**Andi Bailey:** No, Sydney's not here.

**Andi Bailey:** Sydney, we're in this, um, and I think it...

**Andi Bailey:** Was just based on, like, the initial conversations that you had had?

**Mike Bilodeau:** Yeah, okay.

**Mike Bilodeau:** I mean, I think we talked about it, so yeah.

**Mike Bilodeau:** But I just want to point out that, you know, we do more than that.

**Mike Bilodeau:** So if it's to just focus on getting authority there, that's fine.

**Andi Bailey:** If, you know, I just don't want to limit it to just a lot of interest.

**Andi Bailey:** Okay, yeah.

**Andi Bailey:** We can add more terms there.

**Andi Bailey:** Sorry, Aida, go ahead.

**Aida Knezevic:** No, like, our original, excuse me, our original content strategy for the blog content was primarily focused on just building authority related to LLM inference.

**Mike Bilodeau:** So we kind of took that same position for the glossary.

**Mike Bilodeau:** So that was the, that was the rationale.

**Mike Bilodeau:** And the second question is, where is the glossary going to go?

**Andi Bailey:** So we can build out a new template and space in the blog. I saw that you kind of have different tags for content in the blog today.

**Andi Bailey:** So we can just like have a new tag for glossary content or, you know, build out a subsection there.

**Mike Bilodeau:** Is it better to be in a blog or better to be on like in the site in a different section?

**Mike Bilodeau:** And I guess like maybe I'm just trying to fully understand is like, is the idea that this is one glossary like page or one blogger?

**Mike Bilodeau:** we aiming to like build articles for each glossary term item?

**Andi Bailey:** Yeah.

**Andi Bailey:** So for most article, for most glossary terms, there would be a page for each item.

**Andi Bailey:** The simpler ones, we think that we can just have a definition and we would have like, it wouldn't, I guess it would be like slash glossary.

**Andi Bailey:** And then all the terms could be built out from there.

**Andi Bailey:** And then you could click into the ones that are more complex and then the ones where there.

**Andi Bailey:** It's just a definition.

**Mike Bilodeau:** We could just have the definition, so list it out that way. It's like standard SEO. I don't think it goes in the blog.

**Andi Bailey:** Yeah, so it be separate.

**Andi Bailey:** And then I think that's where we would want to start.

**Andi Bailey:** That's not to say that we wouldn't want to do more complex content as we build out the authority.

**Andi Bailey:** We just think that that's a good way to be able to publish at a higher velocity without that, you know, back and forth as we're collecting the context in the space and improving the pipelines.

**Andi Bailey:** We can continue to share outlines on the similar to the original topics that you approved and publish content there, too, and split it out a little bit.

**Andi Bailey:** But we don't want to put the.

**Andi Bailey:** And a review and training so much on you guys as we're spinning up the pipeline and improving the performance there.

**Mike Bilodeau:** How does the performance improve without us giving feedback?

**Andi Bailey:** So, Stevie, there are a couple of things that we're working on right now, like Daniel and Stevie's expertise.

**Andi Bailey:** I think they're working on those pipelines, and we would say that we want to continue to do the outlines and have you giving feedback.

**Andi Bailey:** But so that we could be publishing at a higher velocity, we would do them, the glossary in parallel and run through the glossary terms so that we could be publishing while we're doing the back and forth, the feedback of the more complex terms or more complex pages.

**Stevie Kim:** And I can speak to this a little bit.

**Stevie Kim:** But so, you know, we've got these kind of base pipelines, and we refine them.

**Stevie Kim:** As we learn, like, what's performing well for you, and what is your, like, I mean, it'd be great to know what articles have performed well for you in the past.

**Stevie Kim:** If we don't already have that information, sorry, I am just kind of, you know, jumping on midway through.

**Stevie Kim:** So I'm sure you've had a lot of these conversations.

**Stevie Kim:** But, you know, when we know, like, okay, this is the tone of voice you want, this is the type of content that, you know, performs well for you so far.

**Stevie Kim:** If you don't have that information, I'm sure that, you know, our team's already, you know, worked with you to kind of define that strategy.

**Stevie Kim:** And so, yeah, just, we can refine these pipelines on a technical level to be able to make them more custom to your use case.

**Stevie Kim:** And, you know, we ramp up also, like, through just reading your developer docs and everything, and we get to know your company, your product offerings, your strategy.

**Stevie Kim:** And that does take a little time, but that way, we don't have to keep.

**Stevie Kim:** You know, shoulder tapping on you guys to, you know, say, hey, could you, you know, take our, you know, our view of like these 20 articles?

**Mike Bilodeau:** Maybe you just have to review one or two.

**Mike Bilodeau:** If they're going to go on our site, we're going to review every article.

**Mike Bilodeau:** There's like no chance in hell we would ever publish something that we didn't review.

**Mike Bilodeau:** That seems pretty like negligent.

**Mike Bilodeau:** So, yeah, like I think for us, you know, tone of voice, like overall thing is like probably similar to what you've seen in other places.

**Mike Bilodeau:** Like it's really technical.

**Mike Bilodeau:** Credibility is really important to us.

**Mike Bilodeau:** Like getting details wrong is pretty much like bar none unacceptable.

**Mike Bilodeau:** And so I think that's where, where we come from on this of like glossary is good.

**Mike Bilodeau:** You know, there are a lot of glossaries out there for this type of stuff.

**Mike Bilodeau:** Like it's fine, but I would say like a great example of this type of glossary I think that you're looking at is like on Modal's website.

**Mike Bilodeau:** And they have like the GPU glossary. It's like pretty high craft, like pretty technical.

**Mike Bilodeau:** I don't know if this is something where, yeah, like I'm a little hesitant to do things where it's like we're going to produce a pretty inferior version compared to a competitor.

**Mike Bilodeau:** So that's my only hesitation there is like, theirs is quite good.

**Mike Bilodeau:** And like very technically deep and like on the edge, certainly not doing this in the same way.

**Mike Bilodeau:** But like, that's my only, do we think that we can get close to that?

**Mike Bilodeau:** I would take a look at it maybe and like, can we get close to that type of bar of quality?

**Mike Bilodeau:** Because otherwise I would just say like, hey, I'd rather kick this down and we do this internally and do the high craft version versus like, you know, putting out SEO stuff to just kind of like purely make headway on SEO.

**Andi Bailey:** Yeah, so I would suggest that we send you some glossary terms and what we've built there and then a couple of the outlines from some of the topics that we had done.

**Andi Bailey:** In the last week, you guys inspired our CTO, Daniel, to fine-tune the pipeline for technicality to really test himself.

**Andi Bailey:** And he has started publishing, these are all AI-built, like AI pipelines-built articles.

**Andi Bailey:** So take a look at these and let us know kind of, he was able to refine kind of the reference time to down to a week.

**Andi Bailey:** And he's got, there are a couple of additional steps that he's added to these pipelines that we can duplicate into the base 10 based on his.

**Andi Bailey:** It's like research and what he's done.

**Andi Bailey:** So you lit a fire under him.

**Andi Bailey:** And from that, I think that can get to that level.

**Andi Bailey:** But let's generate a couple.

**Andi Bailey:** Have you review that?

**Andi Bailey:** Have you review these new outlines that we did this week and the three that are coming?

**Andi Bailey:** And then we'll go from there and make a decision.

**Mike Bilodeau:** Cool.

**Mike Bilodeau:** Yeah, it would definitely be helpful to just see, like, the outline, at least from the one that I saw, seems, like, structurally, there's some, like, kind of weird bits in it of, like, jump to conclusion things, but it might just be because it's an outline and that's, like, outline style.

**Mike Bilodeau:** Like, overall, at least looks mostly technically accurate.

**Mike Bilodeau:** So, yeah, I think we'd want to see it.

**Mike Bilodeau:** And then, like, the thing I noticed just in looking at it is that I, like, pretty quickly...

**Mike Bilodeau:** And I think we do want to be able to talk to, like, the, and maybe there's just more feedback, it's, like, you know, the 101 content is, like, yes, valuable, yes, interesting, unless there's kind of, like, a plan to get follow-on, like, 201, you know, 301, like, basically getting deeper into topics, potentially.

**Mike Bilodeau:** Um, it doesn't, like, we would have to, we would have to frame it as kind of as such, like, hey, this is the, you know, it's hard for us to almost, like, publish that in our blog, we would probably need to make a separate section that is, like, you know, XYZ for, for beginners.

**Mike Bilodeau:** Um, because the source material I know is, like, understanding, you know, inference 101, I think it's a medium or a TDS article.

**Mike Bilodeau:** what, what,

**Mike Bilodeau:** I just recognized the four things right away.

**Mike Bilodeau:** It's like this one's side-rooted.

**Stevie Kim:** I actually have a question around that.

**Stevie Kim:** So I read the notes that we have from calls with y'all.

**Stevie Kim:** And I did see that you've got your main target audience, people that are already feeling the problems that you're solving.

**Stevie Kim:** But there's also the desire to reach people earlier on in their journey, kind of before they start to hit these problems.

**Stevie Kim:** And so is that accurate that you're wanting to target those two segments?

**Mike Bilodeau:** Yes.

**Mike Bilodeau:** The journey usually is not defined by how knowledgeable they are, though.

**Mike Bilodeau:** The journey is defined by where they are in building their own product.

**Mike Bilodeau:** So I think I read it this way, it's like, you know, if you go and start a company tomorrow, like...

**Mike Bilodeau:** You

**Mike Bilodeau:** Have all your pre-existing knowledge, which is quite vast, you're pretty sophisticated, and like also you're very early, you have no product.

**Mike Bilodeau:** So like that's really, I think, the lens that we're coming from.

**Mike Bilodeau:** We do not want to target hobbyists.

**Stevie Kim:** Cool.

**Stevie Kim:** Great.

**Stevie Kim:** That's super great clarification.

**Mike Bilodeau:** And I think like even students is like, is she academia?

**Mike Bilodeau:** Yes.

**Stevie Kim:** Undergrad?

**Stevie Kim:** Largely no.

**Stevie Kim:** No.

**Stevie Kim:** Okay.

**Stevie Kim:** No, that's, that's great clarification.

**Mike Bilodeau:** Yeah.

**Mike Bilodeau:** Which is like, kind of a weird nuance in our case of where, like again, the traffic's valuable, there's huge reasons to do it, and we, we certainly want to think about how to be thoughtful.

**Mike Bilodeau:** It's more that I think we would potentially do this in like a different spot on the, on the website under a different framing, like, hey, this is for beginners, and it is for whatever.

**Mike Bilodeau:** Or, like in our blog, we're, we're usually getting into more, more talking to the core audience.

**Mike Bilodeau:** So like learning.

**Mike Bilodeau:** Center content, things that are for beginners, whatever, I think is totally, makes a ton of sense.

**Mike Bilodeau:** Yeah, we had created this foundation, so, you know, maybe we want to rename it, the other product, but that's where we put the AI influence kind of like into it, when we want to recognize you at the beginning.

**Mike Bilodeau:** Yeah, we probably want, I think like, and this is more, we probably just want a learning center on the website, in general, because we do want to like, step people through larger concepts on our side.

**Mike Bilodeau:** I, yeah, I think that there is a, and like, this is the part I think we're feeling now, is there's a lot of content that's out there on the internet that talks to like, understanding the problem space, in a lot of cases, that is, you know, generally skews towards like, very, very, very one-on-one level.

**Mike Bilodeau:** Right, yeah.

**Mike Bilodeau:** And even, even like, in terms of, of hardware, most people writing about hardware are like, H100.

**Mike Bilodeau:** This versus B200s are not typically writing about it very intelligently.

**Mike Bilodeau:** They're writing about it using the invidia marketing materials versus the more technical reasons why people would actually do things.

**Stevie Kim:** So I just want to make sure I'm grasping this correctly because I think it's a problem I felt before too.

**Stevie Kim:** So you're desiring content that, yes, it's factual, but it's really telling a story around this problem, this pain point that's felt already by somebody and written from like, hey, this is not just facts we're spewing out, but this is an experience that we've had and we felt this pain and this is, you know, how we've solved it.

**Stevie Kim:** So it's more of like,

**Stevie Kim:** An authoritative voice, like from an, you know, engineering's perspective.

**Mike Bilodeau:** Is that right?

**Mike Bilodeau:** Yeah, sort of.

**Mike Bilodeau:** I think that's like mostly it is.

**Mike Bilodeau:** I think more it is, you know, like practitioner POV is like, I think that there is a part of like, for instance, do I use a good question is like, hey, what is an H100 versus an H200 versus a B200?

**Mike Bilodeau:** It's like, that is, you know, sort of useful information.

**Mike Bilodeau:** Understanding like, hey, here's when you should really think about using this.

**Mike Bilodeau:** Like, where would you, what is the tradeoff?

**Mike Bilodeau:** What is like the actual consideration you're making?

**Mike Bilodeau:** Because it's like everything in engineering, right?

**Mike Bilodeau:** It's like, most of these things are tradeoffs and compromises on like, do you want quality?

**Mike Bilodeau:** Do want cost?

**Mike Bilodeau:** Do you speed?

**Mike Bilodeau:** Like, where are you kind of willing to go?

**Mike Bilodeau:** And that conversation, that way of thinking from our positioning is.

**Mike Bilodeau:** It's like pretty important versus, you know, I think the things that skew more towards like, hey, here's sort of what the landscape is.

**Mike Bilodeau:** And like, it's pretty surface level, you know, here, the speeds and feeds or the specs on this stuff.

**Mike Bilodeau:** It's like, yeah, it's valuable.

**Mike Bilodeau:** It's kind of like a, you know, marketing pamphlet.

**Mike Bilodeau:** I think it's just that the, you know, we almost need the view of like, hey, that's great information.

**Mike Bilodeau:** If I'm a developer and I read that and I'm one of our audience that actually cares about it, like, cool.

**Mike Bilodeau:** So what do I do?

**Mike Bilodeau:** What do I do with that information?

**Mike Bilodeau:** Where do I go with it?

**Mike Bilodeau:** And so that's why when I say like, I think we, you know, we can have things in like a one-on-one-ish spot.

**Mike Bilodeau:** That's kind of separate or in most cases, we need there to be a clear like, okay, so what, what do I do with this information?

**Mike Bilodeau:** How do I apply it to, to what I'm working towards, which, yeah, either needs like follow-on articles and...

**Mike Bilodeau:** And more of a serialized view of how we're creating these things, so that they kind of layer with each other, or it's, hey, we just, you know, put these in a box over here, and like, this is more what we're doing, kind of pamphlet-y, you know, listicles, and sort of like, very high-level comparisons that are essentially like 99% for bots versus humans, versus like, here's where we really focus on humans.

**Stevie Kim:** Yeah, no, that makes a ton of sense.

**Stevie Kim:** And that's, I mean, that's the content that people share, you know, and, you know, it's super valuable.

**Stevie Kim:** Those are the talks that you, you want to go to, because that's, you know, like you said, there's an action you can take after getting that information.

**Mike Bilodeau:** Yeah, like, I'll send you the article that I'm pretty sure a bunch of the things from the H-100s took from, and like, it's a really good article for bots.

**Mike Bilodeau:** Like, it ranks super high, like, it's really, really well-structured.

**Mike Bilodeau:** Like, it's kind of all of the things that you'd want for, like, if I was building solely for LLMs and for SEO, like, this is probably what I would write.

**Mike Bilodeau:** However, I read it, and I'm like, oh, no, this would lose us credibility if this was on our website, even as it was, like, accomplishing this other goal.

**Mike Bilodeau:** So that's the balance, I think, from our side that's a little bit tough is, like, the most naive way of talking about these things, which, like, bots tend to love, is also, you know, for when you're serving PhDs, kind of, like, potentially brand damaging.

**Mike Bilodeau:** So more, again, where I think we see the articles, we can start to get to that, that feedback, but I think, you know, regardless, we may want to look at this as, hey, we're putting this in, and we're caveating it heavily as, like, this is the, the beginner's POV, which, in my mind, is, like, probably, if we think about.

**Mike Bilodeau:** But LLMs, unless you prompt them heavily saying you're an expert computer scientist with a PhD and you only want whatever, whatever, whatever, they default to the not good source or like to the naive sources.

**Stevie Kim:** Right.

**Mike Bilodeau:** So I think like in my mind, it's not necessarily a blocker thing.

**Mike Bilodeau:** It is I think we want to be like super transparent about where we're getting to as far as, you know, like required level of technical depth.

**Andi Bailey:** Yeah.

**Andi Bailey:** Yeah.

**Andi Bailey:** That makes a lot of sense.

**Andi Bailey:** I think the other thing then to think about is whether you would want us to post on like a Reddit or Medium referencing BaseTen or from BaseTen might be a slightly different audience, slightly different perspective.

**Mike Bilodeau:** But, you know, that's another question that you asked about seeding.

**Mike Bilodeau:** Yeah, for sure.

**Mike Bilodeau:** I think there's like two things.

**Mike Bilodeau:** There's like, you know, if it's like, you know, I started the, the love.

**Mike Bilodeau:** Like, TRT LLM subreddit, which exists, is like, we don't want to post the intro stuff there.

**Andi Bailey:** Like, that's going to make us look like idiots.

**Mike Bilodeau:** If it's the TRT LLM group and we're posting, like, you know, some of the stuff that our model performance engineers are writing, like, from our own content, that probably looks good there.

**Mike Bilodeau:** And we can figure out how to do that.

**Mike Bilodeau:** But I do think, like, the learning center type of thing for the SEO purposes as well is just like, hey, look, there are students, there are other people who can engage with the site in our, like, technically useful is fine.

**Mike Bilodeau:** We just want to put it in, like, the appropriate box because people kind of get the perspective of, like, hey, this is how you talk about the space when you're not really explicitly messaging to a, you know, earlier in their technical journey audience or earlier in their AI journey audience.

**Mike Bilodeau:** It's just like, you know, it doesn't, it looks discordant with the rest of kind of how we're positioning ourselves.

**Andi Bailey:** Okay.

**Andi Bailey:** Yeah.

**Andi Bailey:** Great.

**Andi Bailey:** This gives us good direction.

**Mike Bilodeau:** And I think we can come up with some, like, proposals of how to structure this stuff.

**Mike Bilodeau:** Yeah.

**Mike Bilodeau:** Cool.

**Mike Bilodeau:** We were just saying we should probably make that anyway.

**Mike Bilodeau:** We have, like, other stuff that is kind of related to this that we're thinking about.

**Mike Bilodeau:** So, like, this is not a negative.

**Mike Bilodeau:** It's sort of, like, a known limitation.

**Mike Bilodeau:** I just think we're probably going to have a hard time getting to the point where most of the stuff we would want to put on our, like, our blog versus, you know, putting it into kind of a separate zone and we can think about what the best way is to do that.

**Andi Bailey:** Yeah.

**Andi Bailey:** Perfect.

**Andi Bailey:** Okay.

**Andi Bailey:** And we can supply some ideas there as well.

**Andi Bailey:** We can also, when you do put out, like, that expert content by your engineers, you know, we can start to think about how we repurpose that in other places, like I said, and even the webinars.

**Andi Bailey:** That is something where we can put those through a pipeline and give you additional, like, content that you can put on the blog that's from the webinar, things like that.

**Andi Bailey:** So just some other ideas of directions that we can take this.

**Andi Bailey:** But the follow-ups for us are to send you guys the last three blogs and give some options on how we might want to present this content so that it's clear that it's not your experts, but it's still valuable for kind of that search and LLM piece that you want to rank for.

**Mike Bilodeau:** Yeah, honestly, it's like, these things would not be bad if they were just like, hey, we're, this is for if you're just getting started, and we kind of put that out there, and it's, again, in the right thing of, like, introductions or foundations or 101 or whatever, like, if anything, it's actually good.

**Mike Bilodeau:** This is the stuff when, you know, this is sort of like what I used to look at, you know, through.

**Mike Bilodeau:** Four years ago, and I didn't need to know deeply.

**Mike Bilodeau:** Yeah.

**Mike Bilodeau:** And so, like, I think it's valuable.

**Mike Bilodeau:** Okay.

**Mike Bilodeau:** I think it's just more the, like, we're pretty focused on the, the brand is really built around, like, power user, premium, the people who are pushing the red line of everything.

**Mike Bilodeau:** Yeah.

**Mike Bilodeau:** So that's where I think we just need to, yeah, we just need to, like, put it in the appropriate place, and then it becomes potentially useful.

**Andi Bailey:** Okay, cool.

**Andi Bailey:** We'll take a look at what, at our, like, brand new tech blog, too, and let us know what you think of that in terms of the tone and audience, and whether it gets closer to the mark.

**Andi Bailey:** But we'll, we'll plan to start presenting these as something that can start to build out a learning space for you.

**Mike Bilodeau:** Cool.

**Mike Bilodeau:** I'm just emailing over to Zoom, the, the article is referencing.

**Andi Bailey:** Oh, perfect.

**Mike Bilodeau:** Yeah, and for the, the glossary, I, I do think, especially based on this conversation, we need to expand.

**Mike Bilodeau:** Yeah, we can figure out, I don't mind us having a glossary website, I think it's great, and we can make a high craft version like modal, I think we just want to be, we want to be thoughtful, because unfortunately somebody made like a pretty incredible version of this thing that's a direct competitor of ours, so like we don't want to make it, or yeah, we just got to think about it a bit.

**Andi Bailey:** Yeah, got it, all right, we can send those updates, thank you guys for your time, thank you.

**Andi Bailey:** thank you so much.

**Stevie Kim:** Nice to meet you.

**Mike Bilodeau:** Bye.

**Mike Bilodeau:** Nice to meet you.
