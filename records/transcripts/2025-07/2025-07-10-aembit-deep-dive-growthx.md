# Aembit Deep Dive - GrowthX

<metadata>
date: 2025-07-10
time: 20:01 UTC
duration: 55 minutes
organizer: matthew@growthx.ai
participants: Marcel Santilli (GrowthX), Andi Bailey (GrowthX), Matthew Panzarino (GrowthX), Jakub Rudnik (GrowthX), Apurva Dave (Aembit), Dan Kaplan (Aembit), Ashur Kanoon (Aembit)
fathom_recording_id: 73491125
fathom_url: https://fathom.video/calls/349731788
share_url: https://fathom.video/share/NxByDXP62hCMyaeXT4VE7hX4ym7FtY2e
source: fathom
enriched_on: 2026-03-03 14:30 UTC
</metadata>

---

## Summary

Marcel Santilli walked Aembit's team through GrowthX's advanced content generation pipeline, emphasizing the importance of iterating on context artifacts (company context, audience personas, content-type guidelines) to drive quality outputs. Key outcomes included agreement to conduct 30-45 minute SME interviews with four of Aembit's engineers (Kevin, Victor, David Walker, Andrew McCormick) to deepen domain expertise captured in artifacts, shifting content review earlier to the outline phase rather than final drafts, and implementing a feedback loop where Aembit reviews outlines and provides domain-specific guidance before full content creation begins.

---

## Context

Aembit is a cloud infrastructure and security company (founded by Apurva Dave, Dan Kaplan, and others) building tools for identity and access management in cloud environments. GrowthX has been working with Aembit on content marketing for approximately 3-4 weeks at the time of this call, with an ongoing engagement that includes strategy work and content creation. Aembit is early-stage with their first few customers and is still refining their ideal customer profile (ICP) and positioning. This deep dive was scheduled to show Aembit how GrowthX's content pipeline works — both the inputs (artifacts, context documents) and the execution (AI-powered workflows with human review gates) — so Aembit could better understand the process and provide earlier feedback. The call also served to identify specific technical experts from Aembit's team who could participate in SME interviews to inform higher-quality content artifacts.

---

## Relevance

**To GrowthX Delivery:**
- Validated the importance of iterating on context artifacts early and often — Aembit team enthusiastically endorsed moving content review earlier to the outline phase, which aligns with GrowthX's proposed workflow improvements
- Confirmed that technical companies require multiple artifact versions and content-type-specific templates (e.g., separate guidelines for comparisons vs. definitional guides) to achieve differentiation at scale
- Demonstrated successful use of AI-powered workflows with three mandatory human review gates (brief, outline, final draft) that can be executed in 3-minute + editorial time per step
- Surfaced the need for domain-specific source lists and blacklist/whitelist management to improve research quality for technical audiences

**To GrowthX Business Development:**
- Early signal that Aembit is serious about committing resources to content partnership (willingness to do SME interviews, iterate on outlines, and challenge GrowthX's approach) suggests strong account health
- Product launches planned for the year create expansion opportunity to develop launch-specific content and messaging, potentially leading to multi-month content sprints
- Aembit's need to finalize ICP and messaging may warrant a strategic positioning workshop or deeper consulting engagement beyond content generation

---

## Overview

- GrowthX to conduct SME interviews with Aembit team members to gather deeper domain expertise
- Aembit to review content outlines before full drafts to provide earlier feedback
- GrowthX showcased their advanced AI-powered content generation and optimization pipeline
- Focus on creating high-quality, well-structured content optimized for both search engines and LLMs

---

## Key Topics

### Content Generation Process

  - GrowthX uses a "context engine" to shape high-level content strategy
  - Multiple artifacts (e.g., company context, audience personas) inform the content pipeline
  - AI-powered workflows handle research, outlining, writing, and optimization
  - Human editors review at key stages: brief, outline, and final draft
  - Process includes fact-checking, internal linking, and FAQ generation

### SME Interviews

  - GrowthX to interview Aembit team members (Kevin, Victor, David Walker, Andrew McCormick)
  - 30-45 minute sessions to capture domain expertise
  - Aembit to provide 2-3 bullet points on each SME's areas of expertise
  - Interviews will inform content strategy and improve artifact quality

### Content Review Process

  - Aembit to review outlines before full drafts are created
  - Goal: Provide strategic input earlier in the process
  - GrowthX to run multiple versions to demonstrate impact of outline feedback

### Content Performance Tracking

  - GrowthX uses Looker dashboard to track metrics (clicks, impressions, keywords)
  - Monitoring LLM referrals and brand mentions in queries
  - Focus on overall trend of increasing referral traffic from LLMs

### LLM Optimization

  - Structure content in \~800-word chunks for better LLM processing
  - Use question-answer pairs in intros and conclusions for improved authority
  - Maintain freshness, citation quality, and overall content organization

### Content Refreshing

  - GrowthX demonstrated a content refresher workflow
  - Updates citations, internal links, and improves readability
  - Option to add FAQ sections to existing articles

---

## Action Items

**Apurva Dave (Aembit)**
- Send list of SME names (Kevin, Victor, David Walker, Andrew McCormick) + 2-3 bullet points on their expertise areas to GrowthX team
- Review 2 specific documents for fact-checking (as mentioned in Slack)

**Jakub Rudnik (GrowthX)**
- Share article outlines with Aembit team for review before full content creation

**Dan Kaplan (Aembit)**
- Review 2 specific documents for fact-checking (as mentioned in Slack)
- Introduce SMEs to Daryl for interview scheduling via email

**Ashur Kanoon (Aembit)**
- Review 2 specific documents for fact-checking (as mentioned in Slack)

---

## Transcript
**Jakub Rudnik:** Howdy.

**Matthew Panzarino:** Hello.

**Marcel Santilli:** Hello.

**Marcel Santilli:** Can you hear me okay?

**Matthew Panzarino:** Yes, sir.

**Jakub Rudnik:** Yeah, that sounds good.

**Marcel Santilli:** I'm going to shove some food in my mouth as quickly as possible.

**Marcel Santilli:** Thank you.

**Marcel Santilli:** What's name of the game?

**Marcel Santilli:** A keto bowl from this ministry name place, also a tar.

**Matthew Panzarino:** Oh, nice.

**Matthew Panzarino:** That's good.

**Marcel Santilli:** Rice, cauliflower, growth, chicken, and some veggies.

**Marcel Santilli:** Some tahini sausage.

**Matthew Panzarino:** Chicken and rice is God's gift to protein enjoyers.

**Marcel Santilli:** Ugh.

**Matthew Panzarino:** I see all these bodybuilders eating, like, boiled chicken and white rice, and I'm like, you guys know that the Mediterranean peoples as a whole have really kind of mastered this.

**Matthew Panzarino:** You don't have to eat boiled chicken and white rice.

**Matthew Panzarino:** Turmeric and cumin are not going to kill you.

**Marcel Santilli:** God.

**Andi Bailey:** we

**Andi Bailey:** Marcel, just so you know, in the call yesterday, Apurva gave us, like, a couple of key insights that we can use to dive in a little bit further today, mainly that they have not, you know, finalized their ICP, so they're still working on that, so we can kind of, like, push them a little on that and try and help refine it.

**Andi Bailey:** And then we got a couple of upcoming product launches that they're working on, and so we can talk about, you know, that for the next year.

**Marcel Santilli:** That's perfect.

**Marcel Santilli:** Hey, Dan.

**Apurva Dave (Aembit):** Sounds like you're talking about us.

**Marcel Santilli:** You are.

**Marcel Santilli:** Like, shh, come on, shh, shh, shh, shh, Okay, there's only seven note-takers, so it's not like you missed anything.

**Apurva Dave (Aembit):** Okay, right, right, exactly.

**Marcel Santilli:** If you don't mind, I'm, like, shoving some food because I'm in back-to-back calls also, but I'll try to, you know.

**Marcel Santilli:** Make sure I only talk with my mouth full.

**Marcel Santilli:** It's all good.

**Marcel Santilli:** It's all good.

**Apurva Dave (Aembit):** Oh, I get it now.

**Apurva Dave (Aembit):** That was good.

**Marcel Santilli:** I like it.

**Marcel Santilli:** Yeah, yeah.

**Andi Bailey:** Andi, you want to kick us off?

**Andi Bailey:** Yeah, yeah.

**Andi Bailey:** Hey, guys.

**Andi Bailey:** We just spoke, and so we're doing a quick recap of all the things we talked about so that we weren't duplicating and wasting your time.

**Andi Bailey:** But we thought that we could use today to both show you the improvements that we were talking about in terms of the inputs, the workflows, and the pieces of the pipeline that we updated that went into creating the outputs that we thought we made better, we think we've made better.

**Andi Bailey:** And then also, just go deeper on, we want to push you a little bit on helping define that ICP, because I think, and we have a couple of questions there.

**Andi Bailey:** And then also, we want to talk about, with all of these big pieces that you have coming up.

**Andi Bailey:** with have come up

**Andi Bailey:** Fall, like, events and product launches, things like that.

**Andi Bailey:** You know, what are the goals that you're aiming towards so that we can set a strategy with a little bit more clarity on how we align what we're doing with that rather than just thinking about, like, those five pieces of content every week.

**Andi Bailey:** So those are the big goals for today.

**Andi Bailey:** I think we gave you, Marcel gave you a little sneak peek of Atlas last time, but given how much work went in yesterday, we want to also give you the ability to see the inputs and maybe talk about where we can refine those even further in the workflows.

**Marcel Santilli:** And then before I come in, like, maybe I can share, like, super, super high level, because we are working with a lot of technical companies, and I know when we say technical, it's like there's different types of technical, right?

**Marcel Santilli:** And I think, like, the biggest insight we're finding is that we need to be iterating on artifacts way, way, way, way, way more.

**Marcel Santilli:** And so there are some clients that we're kicking off now where we're, like, three, four weeks in, and we're, like, on the eighth version of some of these artifacts already, you know.

**Marcel Santilli:** And essentially that drives so much of kind of, like, the nuanced things, you know, and it's using, like, every feedback loop to then see if there's an opportunity to rethink how we're doing the artifacts and tweak it a little bit more, you know.

**Marcel Santilli:** So I can jump in.

**Marcel Santilli:** Panzar, anything before I jump in that you think would be relevant?

**Marcel Santilli:** Because I know you've done a ton of work here as well.

**Matthew Panzarino:** Yeah, no, mean, one thing that I think is very, has been very helpful is how much you have shared.

**Matthew Panzarino:** I think there's always opportunity to share more.

**Matthew Panzarino:** The moment you feel that you have reached, it doesn't even need to be complete consensus, but you realize you're on to something, whether that's related to ICP, the way you're positioning the company to the public, the way that you're about to change your stance on a particular topic or product launches.

**Matthew Panzarino:** We talked a little bit about this yesterday, but anything you've garnered there internally or anything you've collated to help you make those decisions, if you are comfortable sharing any of those items, things like case studies.

**Matthew Panzarino:** And I know you're early, and you've got your first few customers, and you're still trying to learn from them, but if you gather learnings from them about the things that they love about the product, the ways that it is improving them, improving their experience, et cetera, any of those kinds of learnings that you collate to help you make your decisions, we are very happy to have those and any of you've given.

**Matthew Panzarino:** Thankfully, you've been very communicative so far, so we had a ton of information to work with, to re-compose these artifacts.-compose these But anything you

**Matthew Panzarino:** Anything you do there that we can integrate, we'll do it rapidly, that way your messaging stays consistent publicly with the decisions you're making, so that we don't end up out of step or out of sync with where you're headed.

**Matthew Panzarino:** So, that's what I'm going to put.

**Marcel Santilli:** Cool.

**Marcel Santilli:** Okay, so, I can jump in unless, is there anything before I jump in, Cora, with help to touch on, or that you want to make sure we cover before I just kind of show you, like, how what we're doing gets input, you know, a little bit.

**Apurva Dave (Aembit):** I'm good with us, with you talking to us for a while about what you're doing, because we have our weekly where we can keep pushing things that you, this time, so for me, it's like, as we talked about in our kind of listening session, like, we need to understand more of what you're doing, so that partially, like, we have, by the way, internally, we all have a lot of confidence that you're building something that will support us, but at the same time, we have to be naturally skeptical, that, like, okay, are you doing

**Apurva Dave (Aembit):** So learning from you in this case will really help.

**Marcel Santilli:** I love that.

**Marcel Santilli:** And thanks for challenging us and pushing us too.

**Marcel Santilli:** Okay, so what we found, right now there's this trend, and you can Google it, right?

**Marcel Santilli:** But on context engineering, and that's literally the same conclusion we arrived at for quite a while, which is, it's not just the input, garbage in, garbage out, or inputs, the right outputs, it's more than that.

**Marcel Santilli:** It's like, you need to shape what is the big picture way more.

**Marcel Santilli:** And that has a much, much, much, much, much bigger impact on the quality of the outputs, and where those outputs are getting to faster than it does with just like crafting a prompt.

**Marcel Santilli:** And given point, like as we're doing a lot of this research, right, when we generate a really high quality output, sometimes, and you take a frontier model and you put a one-sentence prompt, the output will be way, way, way, closer than having okay outputs at a really creative prompt, right?

**Marcel Santilli:** So that's the way to think about it.

**Marcel Santilli:** So because of that, we pretty much built this all in like a context engine that, and you've seen this with coding agents as well, right?

**Marcel Santilli:** Like an ability for a cursor or augment code or others to like be able to help you with a really complex code base is how good it is about finding the right context and pulling the right context in the right places every time, right?

**Marcel Santilli:** So it's the same thing here.

**Marcel Santilli:** So a lot of what we're doing here is like the company context, for instance, right?

**Marcel Santilli:** Like there might be like, multiple different like iterations of it.

**Marcel Santilli:** And these are kind of like guidelines that you can see kind of, there's like a history of like different versions.

**Marcel Santilli:** And what we're trying to understand too over time is like by us capturing different versions, we can actually start to A-B test the hell out of it and work with it, right?

**Marcel Santilli:** Like we're not quite there yet.

**Marcel Santilli:** So we're not yet like the A-B test engine for, you know, for being able to do this.

**Marcel Santilli:** But this gives you an idea of like why we're doing it the way we're doing it.

**Marcel Santilli:** we're it.

**Marcel Santilli:** And tracking all the changes so that we can see how it impacts, right?

**Marcel Santilli:** So if we create a new artifact, I'm just going to show you, there's different types of artifacts where it can be like text, it can be guidelines, it can be like specific rules, page types, and really anything else that we can pull into our workflows, right?

**Marcel Santilli:** And so right now, like a lot of these, what we're starting to see is like there's not only like kind of the audience personas, company context, but then starting to create like persona-specific or topic-specific or lane-specific artifacts as well, right?

**Marcel Santilli:** And so for instance, like if we're doing a product comparison or if we're doing like a definitional guide, there can be an artifact that is going to be more about the do's and don'ts and how to approach this thing, but in the context of what we're doing for you specifically, right?

**Marcel Santilli:** And all of this can be pulled more programmatically in the pipeline, right?

**Marcel Santilli:** So I can pause here, but that's.

**Marcel Santilli:** The TLDR, can go into the artifacts, because I want to show you like the full end-to-end picture, right?

**Marcel Santilli:** And then we can kind of come back and dig into specific artifacts if we need to.

**Marcel Santilli:** But that's the big thing to think of these are like, these are like the context docs that you feed, you know, different pieces of it throughout the pipeline as we're generating content.

**Marcel Santilli:** But also the process of generating these context and the process of getting inputs and comments from you on these is extremely valuable, not only to make these artifacts better, but also for our editors working on this to internalize that.

**Marcel Santilli:** You know, because you can think of our editors and the team working for you as the output bar raisers, right?

**Marcel Santilli:** Like, so ideally, they're not going to be the ultimate domain experts, but if they can internalize these artifacts, which is like the measuring stick for context and for what good looks like, then when they're reviewing different steps and guiding it along.

**Marcel Santilli:** For editing, they know how to raise the bar of that and make sure like they're rethinking if something's not meeting that bar I see in that bar, you know?

**Marcel Santilli:** So pause here, make sense?

**Marcel Santilli:** Questions?

**Marcel Santilli:** I know it's just the high level, but...

**Apurva Dave (Aembit):** Good.

**Marcel Santilli:** Cool.

**Marcel Santilli:** Okay.

**Marcel Santilli:** So now what we have is two things.

**Marcel Santilli:** Think of pipelines as like a table that then has you know, multiple workflows at each column, right?

**Marcel Santilli:** and so...

**Marcel Santilli:** Tanner, is there one here that you think I should start at?

**Marcel Santilli:** I just want to make sure.

**Matthew Panzarino:** Uh, yeah, just the article generation, the bottom one there.

**Matthew Panzarino:** That's, yeah, good place to begin.

**Marcel Santilli:** Okay, perfect.

**Marcel Santilli:** Okay, so...

**Marcel Santilli:** So the way this works is like if you go in here, um, is literally like this markdown, you know, uh, that is just like the settings, right?

**Marcel Santilli:** Like this is calling all these workflows, so each one of these columns is a workflow in our system, right?

**Marcel Santilli:** So if you think of these workflows, what they do is like I'll click on one specific here, I'll just like go into like behind the scenes, and of course it locks me out every time, but I can, sorry about that, okay, so what this this does is like, behind the scenes, what we have is, think of it as like process architects, like I'm a process architect, Hansar, others might be process architects, and what we're doing is thinking through like, what is the process we would actually do as experts in this, if we had unlimited time, like step one, we would do this, step two, step three, right?

**Marcel Santilli:** And then we feed this into an AI coding agent that then translates this into executable code, right?

**Marcel Santilli:** Like that has the prompts, the steps in the workflow, That's good, Thank you.

**Marcel Santilli:** You know, and all this is code, right?

**Marcel Santilli:** And so then what ends up happening is we're able to iterate but also have best practices in all of this based on a plan that comes from a process architect, right?

**Marcel Santilli:** And that process architect should be, you know, someone that knows how to do this really well, has done this their whole life, right?

**Marcel Santilli:** So then what ends up happening here is like we're stitching together for a process for you is a bunch of these things that are very complex workflows.

**Marcel Santilli:** that are easily maintainable because they're maintainable in code, and they call different tools, different APIs, and different models, and they do it in the best way possible, but they also know how to not only pull in the inputs, but also the right context, right?

**Marcel Santilli:** So you can see here like the input is not just a keyword in this case, there's direction, there's company name, and there's like a bunch of context that is pulling, you know, in each one of these, like the company's summary, user context, and a bunch of different settings of things.

**Marcel Santilli:** go.

**Marcel Santilli:** And then what it's doing is, as it's going through these things, it's not just saying, hey, go fetch this or do that.

**Marcel Santilli:** It's thinking about, hey, what's the intent here?

**Marcel Santilli:** The search for workload IAM versus API security reflects blah, blah, blah, blah.

**Marcel Santilli:** And a lot of this is shaped by the input and the fact that this had the context that was fed from some of the artifacts.

**Marcel Santilli:** And then it's guiding all this process along, and it's the equivalent of not just an expert in SEO doing this.

**Marcel Santilli:** It's like an expert in SEO that happens to also be somewhat of an expert in your domain-specific, you know, and that knows your company, you know?

**Marcel Santilli:** So then, like, if you think about this, what's really powerful about this is, like, it's going in, it's doing all of these different steps, right?

**Marcel Santilli:** But then if you look at our execution here, like, that took three minutes, right?

**Marcel Santilli:** And it comes back here, then an editor can hopefully, like, look at this, and, you know, it's not shaping a crazy amount of the assignment.

**Marcel Santilli:** But it's back.

**Marcel Santilli:** Later on phases, it's going to go do a lot, right?

**Marcel Santilli:** And so, for instance, like in the research phase, it's taking the topic and then generating questions.

**Marcel Santilli:** For instance, what are the primary purposes and core security goals of workload IAM versus API security?

**Marcel Santilli:** How do they complement each other, right?

**Marcel Santilli:** And then it's going to go do deep research and then fetch a lot of different sources for it to use, right?

**Marcel Santilli:** And this deep research, there's a lot of things we can tweak in this, right?

**Marcel Santilli:** So, for instance, like we're not doing this right now, but there's domains we can ignore.

**Marcel Santilli:** There's custom questions we can put in there.

**Marcel Santilli:** There's custom contexts, right?

**Marcel Santilli:** There's blacklisted sources, whitelisted sources focused mostly on these sources and not those, right?

**Marcel Santilli:** There's a lot of things we can do to tweak this to continue to improve.

**Marcel Santilli:** So when you get an output at the very end, it's going to be good for you to understand this process because it could be an artifact that we need to tweak.

**Marcel Santilli:** It could be a research contest or instance.

**Marcel Santilli:** That we need to do a better job with, it could be the overall plan, which is the outline, and how we could have tweaked the outline by giving it more of like a template, and more of like fill in this, this is the kind of structure we want to have, right?

**Marcel Santilli:** Or it could have been an editorial, like, an editorial choice, or stylistic choice that we could have done better, right?

**Marcel Santilli:** And then it kind of continues to go on to like these different, like the plan.

**Marcel Santilli:** So this is like the actual plan for what is going to go executed right.

**Marcel Santilli:** You know, so it took the research, it took the estimate, it took all the context, and then it came up with the plan of like, hey, these are the different sections we want to go right against, right?

**Marcel Santilli:** And then it's going to go and actually execute against this as a first step, right?

**Marcel Santilli:** And I think this is like pretty cool because like where we're heading towards like, this is a 13 minute read, right?

**Marcel Santilli:** Does the outline get manual review?

**Marcel Santilli:** Yes.

**Marcel Santilli:** It should, it does, yeah, it should, and this is where, like, especially for more technical customers like you, this is where most of our editors should be spending most of their time, ideally, you know, because it's like, it's where the plan should be.

**Marcel Santilli:** But I will tell you, like, especially with, like, technical topics, it does help a lot for us to build content-type-specific templates.

**Marcel Santilli:** And what I mean by that is, like, when you're comparing two concepts, there might be very specific things and types of sections we want to have, and then you're kind of, like, holding some things a little bit more constant so that then in the outline plan, it's not just, like, this blank thing that's just, like, anything you, you know, like, it's just anything that's up for interpretation, you know, but, yeah.

**Matthew Panzarino:** Yeah, and in the case of this one, I'd just like, Dan, to answer your question about, like, the outline, in the case of this article, you know, the...

**Matthew Panzarino:** Feedback that we had gotten from you was like, oh, you know, I don't know if there's enough of a differentiation between, you know, the API security and the way we handle things.

**Matthew Panzarino:** We want to create like a clear differentiating line between them.

**Matthew Panzarino:** That's great feedback for us because then we're able to go into the outline or into the initial prompt to begin with and say, hey, I want a clear differentiator between these two.

**Matthew Panzarino:** Make sure you make the lines crisp and hard.

**Matthew Panzarino:** And this informs, of course, any future comparisons that we do, especially compare and contrast particles.

**Matthew Panzarino:** We're like, hey, you could do it this way, but, and that helps us to build that in.

**Matthew Panzarino:** So we do it, we run it, we test it.

**Matthew Panzarino:** An editor has roughly three human intervention steps for each pipeline.

**Matthew Panzarino:** So the outline is, a brief is a big one, then the outline is a big one, and then, of course, final review.

**Matthew Panzarino:** There are other places in between that they can tweet, but those are the big ones.

**Matthew Panzarino:** And we, they want to make sure to give those kinds of specific instructions to the pipeline so that it can then produce a good result.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Any thoughts here, or any other questions, or does that make sense?

**Dan Kaplan:** No, that's great.

**Marcel Santilli:** That's helpful.

**Marcel Santilli:** Thank you.

**Marcel Santilli:** Yeah, absolutely.

**Apurva Dave (Aembit):** One question I have, which is maybe more operational for us, is as we don't review the outline phase with you guys, right?

**Apurva Dave (Aembit):** You do that internally.

**Apurva Dave (Aembit):** And I wonder if we could get to better articles faster if we reviewed the outline review, as opposed to reviewing the end result.

**Marcel Santilli:** I one million percent agree.

**Marcel Santilli:** That's how I actually used to do it when I was at DeepGram.

**Marcel Santilli:** Our dev advocate, was a bit, not a bit, was more technical, but not a PhD in ML, you know, but, like, had been in a space computer science background, would review the outline, and that would help quite a bit.

**Marcel Santilli:** It would also give us a lot of guidance around, like, hey, for this one, you did the research, these are the sources you used.

**Marcel Santilli:** Actually, these are kind of, like, garbage.

**Marcel Santilli:** right.

**Marcel Santilli:** Sources never use this again.

**Marcel Santilli:** Like, those types of things are, like, one-time feedbacks that then won't prove it forever, if that makes sense, you know?

**Apurva Dave (Aembit):** Yeah, it does.

**Apurva Dave (Aembit):** I also wonder if, like, so I actually suck at reviewing outlines, personally.

**Apurva Dave (Aembit):** I have just no idea.

**Apurva Dave (Aembit):** I'm always like, yeah, they're good.

**Apurva Dave (Aembit):** Go, right?

**Apurva Dave (Aembit):** But I want to see the gap.

**Apurva Dave (Aembit):** Like, does reviewing the outline actually get us to a better article?

**Apurva Dave (Aembit):** Or then are we still doing a hard edit like we are right now, which might train us to be better at giving outline feedback, like, out how to do it well for you guys?

**Marcel Santilli:** But, and it seems like...

**Marcel Santilli:** run both.

**Marcel Santilli:** We can run both.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** As say, like, the outline, here's where outlines go wrong, right?

**Marcel Santilli:** It's about clear, clearly missing the sequence of events to tell the right story.

**Marcel Santilli:** Like, so it's like, you know, if there's, like, a big gotcha, right, where it's just like, no, no, no, hold on.

**Marcel Santilli:** Like, there's a very nuanced thing about workload, identity and access management versus the high security.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** It's missing the point, API's thinking about activity, IAM's thinking about the identity of blah, blah, blah, I don't know, I'm making this , you know, and it's just like, if you don't lead with that, you immediately lose trust for the audience, because you're not calling out the audience, like, and you need a section to call out the that's the gotchas, it's less of, like, reviewing every word in every single section, it's more like, it's more the blocks and the sequence of the blocks.

**Apurva Dave (Aembit):** Yeah, okay, so this feels strong, this is something we should do, this is probably something you might want to consider doing with all your clients in the first, you know, for the first few articles, at least, I don't think everybody needs it all the time, I think we do a lot of this too, but having that may be the right place for us to inject our opinion, which is something we've talked about in our, you know, in our weekly, which is like, a lot of times the articles are a bit bland, because they're just munging together what they find on the internet, internet, as opposed to having a point of view, and it seems like by articulating a main position for

**Apurva Dave (Aembit):** An article in an outline that backs up that position, you should have a strong article, it's cleaner to do that in an outline form than it is with the entire article, because then we get into wordsmithing.

**Apurva Dave (Aembit):** And it's just like, our human nature is to go deep and start wordsmithing a thing.

**Marcel Santilli:** Yeah, exactly.

**Apurva Dave (Aembit):** It really shouldn't be what we, that's not how we should do this.

**Marcel Santilli:** And I think there's like, really, the biggest, biggest unlock we've seen with clients, and personally as well, right, is if you take a set of questions or a set of topics that you know you want to cover, they don't need to be in this format, right?

**Marcel Santilli:** And you have whoever you're a domain expert in, in those topics are, if we have 30 minutes with that person, I promise you that 30 minutes will pay just an obscene amount of dividends for a very long time, and you don't need 30 minutes every week, and you don't need 30 minutes forever.

**Marcel Santilli:** But it's like just having the hot takes from someone that is the person that can keynote, you know, at RSA, you know?

**Marcel Santilli:** And I know there are times extremely valuable, normally like when you're just asking questions, like, hey, can you, I know you're an expert in identity and access management.

**Marcel Santilli:** Can you just explain to me how you think about it?

**Marcel Santilli:** Like if you're explaining it to someone and you start asking these types of questions and they just start to kind of give that.

**Marcel Santilli:** And we can create a library of that.

**Marcel Santilli:** And the reason I bring it up is because absolutely we should review the outline, but if we can also get a little bit of the hot taste, like that will make that thing that you're talking about, Okay.

**Marcel Santilli:** Yeah.

**Apurva Dave (Aembit):** Yeah, anyways.

**Apurva Dave (Aembit):** got it.

**Apurva Dave (Aembit):** DK, so we should think about Kevin, Victor, David Walker, Andrew McCormick.

**Apurva Dave (Aembit):** And maybe we can help by like describing a few areas where we think they're the top SME, right?

**Apurva Dave (Aembit):** And then structure the interviews.

**Apurva Dave (Aembit):** can get a half hour with each of them over the course of the next few weeks.

**Apurva Dave (Aembit):** course of

**Apurva Dave (Aembit):** Record those things, and those become, like, the assets for you.

**Marcel Santilli:** And we can do a lot of the, like, we're here, and host a session if you want.

**Marcel Santilli:** We actually prefer that, to ask this question.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And I'll personally make sure that we do a really, really good job with that.

**Dan Kaplan:** Anyways, the reason I think we have...

**Dan Kaplan:** you all would be doing, kind of, conducting an interview, right?

**Marcel Santilli:** Correct.

**Dan Kaplan:** Because, in theory, a lot of the stuff we've talked about in various formats, this would be a more direct way for you to, kind of, get it all in one place, right?

**Marcel Santilli:** I can see that being useful.

**Marcel Santilli:** Correct.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And the only times where we would need a little bit more guidance from you is if they're working on something that's not publicly available, and based on their profile, and they never spoke publicly, and you just have no clue what the  they actually do.

**Marcel Santilli:** That's the only time, like, you know, like, hey, this person is actually working on the super secret cryptography thing, blah, blah, blah, and they actually, like, fun fact, here, you know, like, those things.

**Marcel Santilli:** It's like will give us insight to come up with better questions.

**Marcel Santilli:** So that, like three bullets essentially, like make sure we're like, these are the things this person is exceptionally expert, you know.

**Marcel Santilli:** And let me give you an example.

**Marcel Santilli:** I know it's not your level of technical, but it's a different type of technical.

**Marcel Santilli:** We're working with a company that hasn't launched yet and it's in the medical space.

**Marcel Santilli:** And they've done over 12 months of developing these supplements for women, like pre and postmenopausal.

**Marcel Santilli:** And we're working with our chief medical officer who's this holistic doctor, and there's a lot of nuance of the content around like, hey, you need to be an endocrinologist to understand the nuances of what we're talking about.

**Marcel Santilli:** And like between not only going through the artifact iteration and planning the right topics and things like that, but then like some of the reviews that we had and interviews we had with the chief medical officer made our content like the level of feedback we're getting from them is very nuanced now.

**Marcel Santilli:** And they're super happy, you know.

**Marcel Santilli:** And it's only week four.

**Marcel Santilli:** so I think like it just helps everything else better.

**Marcel Santilli:** And it has that flavor across your whole content from that point on, because then we'll take those interviews and regenerate a lot of our artifacts also from those interviews.

**Apurva Dave (Aembit):** Yeah, no problem.

**Apurva Dave (Aembit):** We can do that.

**Apurva Dave (Aembit):** Sounds like we should have done that.

**Marcel Santilli:** Yes, that's on us.

**Marcel Santilli:** That's 100% on us.

**Marcel Santilli:** And we'll force correct and over deliver for here.

**Marcel Santilli:** Yeah, you know, and, you know, but I am so, so confident that, like, I don't think anyone else on the planet has this much thought process on making a content process this, you know, thoughtfully, you know.

**Marcel Santilli:** And we just need to make sure we're getting the right inputs, processing the right inputs, and getting the right feedback in the right place, you know.

**Marcel Santilli:** And I think like one of the ones that I really think is somewhat underutilized, but hopefully starts to see what's possible is the.

**Marcel Santilli:** Fact checker I might have shown you last time, but this is for everyone else.

**Marcel Santilli:** So the fact checker, what it's doing is, it's taking a piece of content that's thousands of words and breaking it down into chunks, and then extracting passages, right?

**Marcel Santilli:** Snowflake shift to secret-less workload identities, cut credential operations by 85%, right?

**Marcel Santilli:** That's a very specific passage, like, hey, this is a specific numerical claim about a well-known company's technology adoption, right?

**Marcel Santilli:** Questions, did Snowflake implement secret-less workload identities as described, and what specific measures were involved in this ship?

**Marcel Santilli:** Like, and it's good, like, that's the level it's doing, right?

**Marcel Santilli:** If a human was doing this, would be virtually impossible to do this for every single article, for every single sentence, right?

**Marcel Santilli:** And it's doing that, and then it's going and researching the passage, did Snowflake implement blah, blah, blah?

**Marcel Santilli:** And it's finding where the sources would be for this.

**Marcel Santilli:** And then what it's doing, and doing all this in parallel, is verifying if there's enough evidence to be confident in it or not.

**Marcel Santilli:** So zero would be, we just don't know, there's no evidence against it or for it, you know?

**Marcel Santilli:** And so we don't have strong confidence either way, right?

**Marcel Santilli:** And in those cases, it won't rewrite the whole thing, but we can look at it in black, right?

**Marcel Santilli:** And then in these cases where it's like a two, it's like, okay, cool, it's like minus two to plus two, right?

**Marcel Santilli:** And then if there's anything where it's like a minus, let me see if there's anything here that's a minus.

**Marcel Santilli:** So far, nothing, which is actually pretty positive.

**Marcel Santilli:** So far, everything is true.

**Matthew Panzarino:** Yeah, these were with the updated artifacts, so they had a little bit more direct context.

**Marcel Santilli:** Okay, that's actually pretty impressive.

**Dan Kaplan:** In a lot cases, that might be self-fulfilling, like we may have said it.

**Marcel Santilli:** That's true.

**Marcel Santilli:** But then there's like also a lot of inputs to make sure that it is true.

**Marcel Santilli:** But yes, if in the past.

**Marcel Santilli:** You

**Marcel Santilli:** You cited that, and there's multiple places where you say that, it is going to assume that what you said, what it's looking for is not a, like, conclusive, it is a fact, help, you know, that can universally true fact, you know, what it's looking for, is there enough to back up this, is there anything to back it up, because what, like, LMMs do, one, they're rewarding recency and freshness of content.

**Marcel Santilli:** Two, they're rewarding structure and readability, and it's this well-organized, and it's this organized in a way that there's a lot of question and answer pairs to make it easy, because these systems are lazy, and they have so much compute, and they're burning so much money in compute that they're trying to take shortcuts, right?

**Marcel Santilli:** And then the last thing it's looking at, is not, is this super crazy factual, because there is a million sources saying this is factual, what they're looking for is this cited, is this well-researched, is this, like, well-cited, that's it, right?

**Marcel Santilli:** And is there a good attribution here?

**Marcel Santilli:** And if it's doing that, then that's good, right?

**Marcel Santilli:** And that's already, you know, you're in the, you know, five percentile of, like, quality of content already, you know?

**Marcel Santilli:** You might not be, you know, Wall Street Journal level of scrutiny, but I think that's okay for now, you know?

**Marcel Santilli:** That's kind of the idea that I think about, but challenge us, right?

**Marcel Santilli:** Like, and so hopefully, like, if there's things here where it's, like, domains to search or things to ignore, you know, or if we get it to a point where, like, actually, we have a lot of things in our own domain that's just plain not true and we have stuff here, so never use our domain, you know?

**Marcel Santilli:** And then, like, we can kind of go through that, you know?

**Marcel Santilli:** But anyways, and then this part is really, really good because, like, what, this is really cool, what it does is, like, this part was always really hard to do for me personally, right?

**Marcel Santilli:** You hire a writer, this hires charge me $2 a word, this technical writer, and then, first of all, they don't do any research.

**Marcel Santilli:** Their own, and they're not the world expert in every single topic and every single thing they're writing about, so then they're going to miss things.

**Marcel Santilli:** Second, they don't know what's already been written out there, and they don't know what is the gap in the information.

**Marcel Santilli:** But then third, you're like, okay, now you wrote this, can you please make sure to cross-link to other things that are relevant that we already wrote, you know, and you weren't even a rarer, right?

**Marcel Santilli:** And so what this does, it analyzes the content, and then it looks for different opportunities where there are pages that you're already ranking for in certain words, and then it finds additional opportunities within the content, and then it tries to insert these, it validates that those URLs are still valid, and then it inserts those links programmatically in the best place possible in the article.

**Marcel Santilli:** So it's essentially finding, like, pages that are already ranking for certain keywords, and what is the primary keyword those pages are already ranking for, even if they're not ranking high, and then it scores them based on relevancy.

**Marcel Santilli:** And then it grabs that, and...

**Marcel Santilli:** Inserts it in the best place possible for this piece of content.

**Marcel Santilli:** So, for instance, here, right, often discussed as NHI non-human ideas, and it links to that piece of content from you.

**Marcel Santilli:** Like, this is so, so, so hard to get it right and so important in all the content you're doing because you're building a knowledge graph for LLMs and for search engines to understand how all your content is interrelated and what you have topical authority around, you know, if that makes sense.

**Marcel Santilli:** And, anyways, I'll leave it at here, but hopefully you kind of see what's possible and kind of how these things work, you know, and also how cool some of the stuff is that we're building, you know.

**Apurva Dave (Aembit):** That's cool.

**Marcel Santilli:** Questions or anything we didn't cover?

**Marcel Santilli:** Hopefully that, that is helpful, but I'm happy to kind of dig in more or, or talk about.

**Apurva Dave (Aembit):** One question I had was kind of, like, on maintenance and upkeep of articles.

**Apurva Dave (Aembit):** Like, if

**Apurva Dave (Aembit):** It feels as though you can almost, maybe not all of it, you don't need to run through the whole pipeline again, but on some regular basis, it seems like there are pieces of these pipelines you'd want to run through again.

**Apurva Dave (Aembit):** The most obvious would be those, like the links component, right?

**Apurva Dave (Aembit):** It seems like in six months, a bunch more articles that maybe are more appropriate or some have ranked better than others, these terms, and we want to kind of amp that by reintroducing those into these older articles.

**Marcel Santilli:** That's exactly right, yeah, so this is an example of a refresher workflow for you, okay, I think this is just a sample one, and the input here is the, sorry, it's this article right here, so let's just pull it up and look at it, so this is, I think this is just like one we might have already, or you've already recently done it, so it's like it might We're

**Marcel Santilli:** This the best example of an outdated one because it's the recent, but then what it's doing is it's going and researching all the topics, right?

**Marcel Santilli:** So it's doing a similar research process we did before, right, and performing all that research.

**Marcel Santilli:** Then it's like going in and finding opportunities to refresh and clean up the article, but keep as much of the basis of it as possible.

**Marcel Santilli:** And it's very, very, very nuanced, right?

**Marcel Santilli:** It's hard to explain.

**Marcel Santilli:** And then it's doing the internal linking as well, right?

**Marcel Santilli:** It's finding additional internal links and then adding them here.

**Marcel Santilli:** But the nuanced piece here, it's doing things that LLMs reward today, which is like, let me try to compare side by side.

**Marcel Santilli:** So hopefully you can see a little bit.

**Marcel Santilli:** So give me this, bear with me for a second.

**Marcel Santilli:** Okay, so you can see here, there's this.

**Marcel Santilli:** The 2024 report, and this is the intro, right?

**Marcel Santilli:** Here you have the 2024 report, and then this link here, and then this, and this.

**Marcel Santilli:** And it's like very nuanced.

**Marcel Santilli:** It's not fundamentally changing what you wrote, but it's making it slightly more cited, slightly more researched, and better interlinking.

**Marcel Santilli:** You know, in an area that it's really shallow or redundant, it's trying to either, you know, get to the point a little bit more, or expand because it's just too shallow, you know, or not enough.

**Marcel Santilli:** And that's about it.

**Marcel Santilli:** Like, it's not going to fundamentally change the examples, the images, almost anything else, you know?

**Marcel Santilli:** But it's very, very nuanced.

**Marcel Santilli:** We're working on a way to be able to look at the depth between them.

**Marcel Santilli:** It's like, it's very, very nuanced, you know?

**Marcel Santilli:** So this, like, you can see, like, in this example, in GitHub Action, the environment variable,

**Marcel Santilli:** Coming to three primary types, each survey listing roles within their workflows, and it's like, same sentence, but then this is a bit more detail, or more verbose, I mean, I don't know, detail, verbose, we gotta check, right, like, but, and this, like, gets to the point a little bit more, you know, and so, it's not subtracting substance, but it might be subtracting words where it gets to the point a little bit more, it's definitely citing and cross-linking a lot more, you know, but it's keeping almost every the bones as much as possible, and then the last thing it's doing is potentially generating this, like, well, not potentially, it's generating for you to potentially use an FAQ, which is taking the content and then repositioning it as question and answers, which can be really valuable for a lot of alums as well, but also for sales or, you know, enablement.

**Apurva Dave (Aembit):** That's cool.

**Apurva Dave (Aembit):** And that, right, are you just augmenting the article?

**Marcel Santilli:** This is, like, the tail of the article?

**Marcel Santilli:** This could be an additional section at the bottom of the article, correct.

**Marcel Santilli:** Okay.

**Marcel Santilli:** Yeah.

**Apurva Dave (Aembit):** Right.

**Marcel Santilli:** And obviously, like, this could also be used as, like, you know, if you type this, like, your number two right now.

**Marcel Santilli:** No, I'm actually, okay.

**Marcel Santilli:** So that's actually pretty good, right?

**Marcel Santilli:** Pretty good.

**Marcel Santilli:** Yeah, that is great.

**Marcel Santilli:** It's great job.

**Marcel Santilli:** But obviously, it's a very specific question here, right?

**Marcel Santilli:** And, but it's, you know, like, might be, or number three, but there might be cases where, oh, look at this, you're the number one referral, your number one link on AI Answer.

**Marcel Santilli:** That's pretty good, too.

**Apurva Dave (Aembit):** It's not down.

**Marcel Santilli:** Okay, now, now I'm really curious, Dan.

**Marcel Santilli:** Let's see.

**Marcel Santilli:** Let's see.

**Marcel Santilli:** I'm always curious.

**Apurva Dave (Aembit):** Okay.

**Apurva Dave (Aembit):** All right.

**Marcel Santilli:** That's good.

**Marcel Santilli:** That's positive, I think.

**Marcel Santilli:** You know?

**Marcel Santilli:** Good job, Dan.

**Apurva Dave (Aembit):** You already have a static sequence.

**Apurva Dave (Aembit):** Yeah.

**Apurva Dave (Aembit):** Okay, got it.

**Apurva Dave (Aembit):** So right now we're already we're showing results where we get really specific in the question and then our goal should be to get more and more general within the same zone, but have the authority to, you know, to kind of like have the LLMs trust us.

**Marcel Santilli:** Yeah, yeah, exactly.

**Marcel Santilli:** So like, let's just do another test here.

**Apurva Dave (Aembit):** Yeah, that's exactly what I would do, right?

**Apurva Dave (Aembit):** Just what are the risks?

**Marcel Santilli:** All right, let's see the sources.

**Marcel Santilli:** I hate how they're hiding all the sources now.

**Marcel Santilli:** Uh-huh.

**Apurva Dave (Aembit):** You don't need a source to have TPT till it's true.

**Marcel Santilli:** Interesting.

**Apurva Dave (Aembit):** Okay.

**Apurva Dave (Aembit):** Yeah, okay, so that's, this is, this is what we're striving for.

**Marcel Santilli:** This is great.

**Marcel Santilli:** We're not listed here yet.

**Apurva Dave (Aembit):** Yeah.

**Apurva Dave (Aembit):** But we will.

**Marcel Santilli:** Yeah, exactly.

**Marcel Santilli:** And by the way, like we, we're.

**Marcel Santilli:** We're tracking a lot of these things, and we'll make sure we have these, like, we're sharing these reports with you, and we did a partnership with a vendor that does a lot of this collecting of data, and then we can come up with these queries, and so, like, this should inform a lot of these queries, right?

**Marcel Santilli:** But the goal is, you want to go in the long, long tail, and then show up, and then when you just show up, people click, and you get really positive signals, so that then you can work your way up to the, you know, to the higher level.

**Marcel Santilli:** But now, I am really curious if, if this, if this, okay, all right, so the long tail, I think we have work to do.

**Apurva Dave (Aembit):** Yeah.

**Marcel Santilli:** But, but anyways, like, that's part of it, too, you know, it's like, if you can win the, like, the FAQ is cooler, because, like, you can take these FAQs, whether it's just for testing, but you can also insert the FAQs, you can all, we can also do tests where, like, we have.

**Marcel Santilli:** FAQs at the bottom of, you know, five articles, a whole five constant or something, you know, for one strategy ranking that we're doing a refresh for, you know, and see like, like for instance, like you can take, you know, a set of 20 articles that haven't been updated for more than a year, we can refresh 10 with FAQs and refresh 10 without FAQs, and we can monitor those 10 differently and see if there's any delta in, because there's just like so much stigma that you just don't know.

**Marcel Santilli:** There's no volume in those searches, you know, and then like with LLMs, there's like all over the place, they're changing the weight, they're ranking and inciting things so much, that it's just like, you can monitor, but it's really hard to perfectly predict, you know, so you just got to test a lot and hit it a lot, you know.

**Apurva Dave (Aembit):** Cool.

**Marcel Santilli:** Anything we didn't cover that would be helpful?

**Marcel Santilli:** Hopefully you see this as part art, part science, you know.

**Marcel Santilli:** Yeah, lot that goes into it, and we're collaborating together with you, you

**Marcel Santilli:** On what makes it, what works, you know?

**Ashur Kanoon:** Question on, like, article performance.

**Ashur Kanoon:** How are you guys tracking, if you guys are tracking, how are you tracking, like, some of the articles you've given to us?

**Marcel Santilli:** Yeah, absolutely.

**Marcel Santilli:** Jakub, do want to talk a little bit about, like, the Looker dashboard?

**Jakub Rudnik:** Yeah, so we've got a Looker that we shared in the last week.

**Jakub Rudnik:** There is, there's cleanup we need to do on the content OS to make sure everything that we have published, it's just slightly stale data, so we're cleaning that up actively as we hand that over to Daryl and Edisham, but that will have, there's a couple things, but keywords, impressions, clicks as a starting point for the article we've published and tracking that data.

**Jakub Rudnik:** There's definitely customizations we can make on top of that, so as we get deeper and we have more published and more data, we'll have, we'll make those and add on to that.

**Jakub Rudnik:** The one that looker and then that partnership that Marcel mentioned on the LLM tracking side, we've got data to share there over time.

**Jakub Rudnik:** So those are the different pieces.

**Jakub Rudnik:** Again, the looker is up what there's some cleanup again that we're doing right now to get the cohort set up.

**Jakub Rudnik:** That's the one you look in that looker dashboard.

**Jakub Rudnik:** That's the one that's not operating properly.

**Jakub Rudnik:** So that should be cleaned up this week.

**Jakub Rudnik:** But that's what we're, that's what we're tracking currently.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And I'll just flash it really quickly.

**Marcel Santilli:** The idea is like tracking overall, like non, non-branded clicks and impressions by, by different URLs, like overall, and then different cohorts of data.

**Marcel Santilli:** This one's one that's like, still like needs to make sure we're tracking all the right URLs.

**Marcel Santilli:** And then like LLMs, which is like, we're, we can add more and more.

**Marcel Santilli:** So there's like tracking queries, which we can set this up, you know, right now it's mostly like basic queries across, you know, different URLs or just basic queries, but then on the LLM side, what we're looking at is like referrals from different referrers, right?

**Marcel Santilli:** Like silver plastic versus Gemini versus, you know, chat TPT and then which landing pages are getting those sessions if we can find it, you know, and then tracking that over time, you know, and so like, we'll, we'll, we'll, we'll, clean this up and continue to share, but the, the foundation is there is, is, you know, the, kind of the big, the point.

**Marcel Santilli:** And, and then now we want to start to see is like aggregate this weekly and monthly and then hopefully start to see that, that trend continue to go up now as we ramp up on, on fall time as well.

**Marcel Santilli:** I will tell you, the LLM tracking, tracking referrals, no-brainer, whether they refer what page they refer to, tracking what queries you have brand mentions in is a very non-deterministic thing, because it's like, we need to manually come up with every query you can possibly want to think about, and the problem is no one is putting just, like, plain queries only, they're putting sometimes, like, it's an exchange of messages, sometimes you turn on search, sometimes they don't, you know, like, sometimes they'll do deep research, sometimes they don't, right?

**Marcel Santilli:** Like, so, it's a, you know, what really matters is, are you putting really good content out there and keeping it fresh and doing it regularly, and is the referral traffic going up?

**Marcel Santilli:** And then for the things you really, really care about, like, put out some queries out there for us to monitor, and hopefully, like, you'll get mentioned more often, right?

**Marcel Santilli:** Like, but, but it's kind of like, it's hard, the middle is not.

**Marcel Santilli:** I have a perfect science, but what you can control, the controllable input is high quality content that hits the bar of the things that LLMs care about, which is freshness of content, know, question and answer pairs, well cited, well researched, well organized, you know, good paid experiences, and all of that, right?

**Marcel Santilli:** And then what you want to look at as the output is like, are people clicking through as much as possible, you know?

**Apurva Dave (Aembit):** Yeah.

**Apurva Dave (Aembit):** So you kind of think of the LLM as a reader of the article.

**Apurva Dave (Aembit):** Is that it?

**Marcel Santilli:** It is, and what we're seeing with clients, this is more transactional clients, we have one website that is seeing now, I think more than half of their new opportunities during a web agency are coming from LLMs, and they know because they started asking in their form how they heard of them, and we've worked with them for like nine months.

**Marcel Santilli:** And they're like, man, this is insane.

**Marcel Santilli:** Like we had no idea this.

**Marcel Santilli:** This was going to happen, and then I thought it was starting to happen because we were seeing the traffic, and then we changed our form to ask, and now we're asking on calls, too, and almost all of everybody at GPT, and when they're searching for agencies to help me with LSMS implementation, we keep coming up, and it's like a lot of the content that we did, and so it's like, but it takes a while.

**Marcel Santilli:** was not like, that wasn't happening three months ago as much, right?

**Marcel Santilli:** It certainly wasn't happening nine months ago, and so not only is the trend of more people searching for it happening, but then these models are getting retrained a lot faster, so then some of these recommendations are happening even without search turn on, but then, like, if you publish an article today, that article is high quality, that might get pulled into the training data later, you know, like three months from now, and then that might become, like, knowledge on the model based on the cutoff date, even if don't have search turn on, you know, and that's certainly true for long tail technical content, right?

**Marcel Santilli:** Like, the long tail is even more important, you know, where, for that to be true, because there might not be

**Marcel Santilli:** You know, 50 different, like, authoritative sources talking about some nuanced piece of IAM or something, you know.

**Matthew Panzarino:** Yeah, and that's something we take into account, too, when we're structuring the content, because there are certain ways, and obviously this is always changing.

**Matthew Panzarino:** The state-of-the-art is the state-of-the-art five minutes ago, right, with LLM's results.

**Matthew Panzarino:** One of the things that we're seeing is that there's a limited window in which to get your point across and to answer a question.

**Matthew Panzarino:** LLM takes all these articles, the way it reads them is generally by chunking them.

**Matthew Panzarino:** So it'll take a chunk of about 800 words or so, maybe a little bit less at a time, and if it finds an answer within that chunk, then it rates it better, right, more authoritatively.

**Matthew Panzarino:** This is the currently accepted understanding, by the way, because the only people that really know, and even them, it's a little hazy, are the people actually building it internally.

**Matthew Panzarino:** But that means that when you see structure of content that we put out, those best practices are integrated into our pipelines and into the prompts that we use to create that content.

**Matthew Panzarino:** So you don't have to worry about that.

**Matthew Panzarino:** worry that.

**Matthew Panzarino:** But if...

**Matthew Panzarino:** If you ever see architecture, you're like, man, I wonder why they structured it this way.

**Matthew Panzarino:** Sometimes that's informing it.

**Matthew Panzarino:** These can realize or materialize as things like introductions that ask and answer a question or conclusions that ask and answer a question so that within the same chunk, you can see that the LLM can see that and says, hey, this is probably an authoritative source for this.

**Matthew Panzarino:** Let me process additional chunks to see where we're at here.

**Matthew Panzarino:** Whereas Google would index an entire page at once, LLMs tend to index chunks of content at once.

**Matthew Panzarino:** So we integrate that into our best practices that will pay it forward to the content.

**Matthew Panzarino:** We are paying attention, of course, to what the state of the art is there, and we'll keep tweaking that.

**Marcel Santilli:** Well, anything else before we wrap up?

**Marcel Santilli:** Hopefully this is helpful and we have some action items on our end to work with.

**Marcel Santilli:** You're going to send us a list of the names you already mentioned, but we'll read.

**Marcel Santilli:** Talk to them, or if you want to do an intro, and then we'll make sure we do it in the next week or two at most, and set up at least 30 minutes, if not 45, but each person.

**Marcel Santilli:** We'll prepare, and you'll just send us two or three bullets, and then we'll come with really good questions and host the whole thing.

**Marcel Santilli:** And then from there, the only other action that I heard as well, in addition to what we already covered in other meetings, is making sure that we take one of the articles before you go into, let me go do a bunch of work on this article, give you an opportunity to also look, give you a final output, and also give you the outline version of that output, or input, I should say.

**Marcel Santilli:** I think you get an opportunity to make some tweaks in that, and then run multiple versions of that, so that you can see the difference between the impact and the outline, you know, so that you understand better where your, the impact that your feedback would have in different stages of the process.

**Marcel Santilli:** Is that a fair, like, summary of what?

**Apurva Dave (Aembit):** That seems good to me, Dan, Asher, check for you guys.

**Apurva Dave (Aembit):** Silence is acceptance.

**Dan Kaplan:** Yeah, that works.

**Dan Kaplan:** And obviously we're still, and then Jacob, I was back and forthing with you a lot on Slack, but that channel is still kind of the.

**Jakub Rudnik:** Yeah, same channel.

**Jakub Rudnik:** And I'll, again, remain in there and be supportive.

**Jakub Rudnik:** We've already shared, like Daryl's not here, but the, you know, change to the outlines or inserting you all in there.

**Jakub Rudnik:** I already pinged him.

**Jakub Rudnik:** We've talked through that.

**Jakub Rudnik:** He's got another client that we do that for.

**Jakub Rudnik:** So it's just building in that process.

**Jakub Rudnik:** So that should be easy to go into right away with any content going forward.

**Jakub Rudnik:** And same thing, we'll schedule that, those kind of.

**Dan Kaplan:** I know we've had some articles in Flux and then some articles that were recalibrated or redone with some additional calibration.

**Dan Kaplan:** Maybe just, I know there's a couple of articles.

**Dan Kaplan:** Facts that we need to look at.

**Dan Kaplan:** So I've shared that with the team, Apurva and Ashur, for us to review those two documents specifically.

**Dan Kaplan:** But in terms of the active pieces of content, maybe just remind me, if you don't mind.

**Dan Kaplan:** I will share those over Slack.

**Jakub Rudnik:** David is back from vacation tomorrow.

**Jakub Rudnik:** So those that he has taken to the 90% of the way there that we've gone back and forth, I want him to close those out.

**Jakub Rudnik:** Just so we're bringing in Daryl at the show with these new fresh pieces of content.

**Jakub Rudnik:** So you, in the very short term, focus on those three artifacts to review and the three pieces of content that Panzer went through yesterday.

**Jakub Rudnik:** And then we'll clean up those other, I think there's four pieces that are close, but we need to take your reviews and apply those.

**Jakub Rudnik:** We'll get that final sign-off, publish those, close out like David's outstanding pieces there.

**Jakub Rudnik:** And then we'll move forward with new outlines and build that process.

**Dan Kaplan:** Okay.

**Dan Kaplan:** And I'll introduce our SMEs to you all.

**Dan Kaplan:** Who, who would be conducting those interviews, or who?

**Marcel Santilli:** Yeah, it would be, it would be Daryl, so Daryl, just, did y'all, did Daryl already get a chance to meet everybody?

**Jakub Rudnik:** Yeah, Daryl's already got a chance to meet yep.

**Marcel Santilli:** Okay, cool, yeah, so Dan, like, full confidence there, as well, like, a lot of our directors, like Jacob, but also Daryl have editorial background, and Daryl, I don't know if you mentioned, but he ran Apple's blog, and then he was at Com for all of Shopify, and then he was finishing at TechCrunch for several years, so he's done probably over 1,000 stakeholder interviews in his lifetime, and so he's world-class at that, a lot better than Of course, that's great, yeah.

**Dan Kaplan:** You got a world-class group there, I hope, I hope, I hope it all pans out.

**Marcel Santilli:** Thank you, yeah.

**Marcel Santilli:** A hell of a crew you've assembled, yeah.

**Marcel Santilli:** Yeah, I appreciate it.

**Marcel Santilli:** Awesome team, well, I appreciate the collaboration, thank you so much, and we're excited to keep building fast and furiously on our end to keep raising the bar, hopefully.

**Marcel Santilli:** And making this process easier and easier for you as well.

**Marcel Santilli:** Perfect.

**Marcel Santilli:** Thanks for the time.

**Marcel Santilli:** really appreciate it.

**Marcel Santilli:** Awesome.

**Marcel Santilli:** Thanks, team.

**Marcel Santilli:** soon.

**Marcel Santilli:** you.
