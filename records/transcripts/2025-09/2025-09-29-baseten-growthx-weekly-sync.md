# Baseten <> GrowthX - Weekly Sync

<metadata>
date: 2025-09-29
time: 21:00 UTC
duration: 31 minutes
organizer: Erik O'Brien
participants: Erik O'Brien (GrowthX), Kenzie Amack (BaseTen), Marylise Tauzia (BaseTen), Mike Bilodeau (BaseTen)
fathom_recording_id: 90613346
fathom_url: https://fathom.video/calls/423942947
share_url: https://fathom.video/share/2BJG36tH4pe_VP-zFDqFz78ZUri-VFkm
source: fathom
enriched_on: 2026-03-03 14:30 UTC
</metadata>

---

## Summary

Erik O'Brien walked BaseTen through GrowthX's Atlas content generation platform, demonstrating the full workflow from research through fact-checking to final article output, while BaseTen's team flagged concerns about outdated source material and GPU-focused content clusters. The team agreed to prioritize setting a one-year limit on source material age, reshape the content strategy to emphasize inference economics over GPU selection, and schedule a product deep dive for next week so GrowthX can better understand BaseTen's platform positioning for more accurate content creation. First articles and reporting dashboards are on track for next week's call.

---

## Context

BaseTen is an AI infrastructure company that provides hosted model serving and inference optimization. GrowthX is executing a $200k+ content marketing engagement to position BaseTen as a technical authority in AI inference, targeting ML engineers and technical leaders. This is week two of the engagement — the team finished artifact creation (company personas, writing guidelines, ICP) last week and is now in calibration mode, reviewing BaseTen's product positioning and finalizing the content strategy before ramping up article production. The call reveals important quality concerns from BaseTen around source freshness and positioning accuracy that are shaping how GrowthX tunes its content generation process.

---

## Relevance

**To GrowthX Delivery:**
- Mike's concern about stale source material (>1 year old) forces addition of time-filtering to the Atlas pipeline — this is a product enhancement that improves Atlas quality for all future AI/ML clients in fast-moving verticals.
- BaseTen wants source citations and the ability to whitelist/blacklist specific domains in the research phase — GrowthX should document this as a repeatable configuration pattern for technical clients.
- Client feedback on content cluster prioritization shows BaseTen values "build vs. buy" and cost efficiency positioning over GPU reseller positioning — reinforces that thought leadership framing beats hardware commoditization.

**To CheckThat:**
- Erik mentioned tracking LLM visibility alongside SEO using Scrunch (GrowthX's internal LLM visibility tool), testing dozens of prompt variants in Perplexity and Claude — validates that AEO and SEO strategy should be co-optimized for technical audiences.

**To GrowthX Business Development:**
- BaseTen team is engaged and critical, which signals a healthy, mature account. They're requesting access to Google Search Console, Analytics, and CMS — indicates trust and intent to track performance.
- Four content clusters with explicit ranking goals (top 10 for 15+ inference keywords in 8 weeks) is a measurable success metric that supports future case study and reference potential.

---

## Overview

- GrowthX presented their content generation platform (Atlas) and editorial process
- BaseTen team provided feedback on content focus areas and SEO strategy
- Product deep dive to be scheduled for next week to inform content creation
- Adjustments needed to content clusters and priorities based on BaseTen's core positioning

---

## Key Topics

### Content Generation Platform Overview

  - Atlas platform used for content generation, including artifacts, research, and article creation
  - Process includes assignment brief, research, outline, draft, fact-checking, and final output
  - Human editors involved at key stages to ensure quality and alignment

### Content Source and Accuracy Concerns

  - Mike raised concerns about blended context and outdated information in AI-generated content
  - Suggestion to avoid source material over a year old due to rapid changes in ML/AI field
  - GrowthX to investigate setting time frame limits on sources and providing citations

### Content Distribution Strategy

  - Discussion on whether new content will go on BaseTen blog or create a new area
  - Consideration of blog vs. guides section based on content length and technicality
  - Guides offer SEO benefits with displayed copy and downloadable PDFs

### Editorial Content Strategy

  - Focus on ML engineers and technical leaders as core audience
  - Goal: Rank in top 10 for 15+ target inference keywords in first 8 weeks
  - Position BaseTen as synonymous with fast inference and technical authority
  - Four initial content clusters identified, with team feedback on priorities

### Content Cluster Refinement

  - Team discussion on adjusting cluster priorities and focus areas
  - Suggestion to de-emphasize GPU-specific content in favor of broader inference economics
  - Consideration of adding "build vs. buy" oriented content
  - Agreement to reshape GPU-related content to include BaseTen positioning

### Next Steps and Scheduling

  - Product deep dive to be scheduled for next week (early morning preferred)
  - GrowthX to access BaseTen's brand style guides for design alignment
  - Draft articles or topics to be presented next week for review
  - Performance tracking and reporting setup to begin

---

## Action Items

**Marylise Tauzia (BaseTen)**
- Finish reviewing ICP & writing guidelines docs; add comments in Notion

- Coordinate w/ Rachel to schedule product deep dive w/ Erik's team early AM next week

- Share BaseTen brand style guides & Figma files w/ Erik for design team


**Erik O'Brien (GrowthX)**
- Check w/ team re: setting 1yr limit on source material age; report back


**Kenzie Amack (BaseTen)**
- Review content strategy doc; add comments/suggestions on clusters & keywords


**Mike Bilodeau (BaseTen)**
- Review content strategy doc; comment on cluster priorities & keyword relevance

- Provide GrowthX team access to Google Search Console, Analytics & CMS

---

## Transcript
**Kenzie Amack:** Hi, Erik.

**Erik O'Brien:** Hey, Kenzie.

**Kenzie Amack:** Nice to meet you.

**Erik O'Brien:** You too.

**Erik O'Brien:** How's your Monday going?

**Kenzie Amack:** Not bad.

**Kenzie Amack:** Our whole team is headed down to an offsite in San Diego this week.

**Erik O'Brien:** I've heard.

**Kenzie Amack:** Yeah.

**Kenzie Amack:** Is that all everyone at BaseTen talks about when they join Zoom calls right now?

**Erik O'Brien:** Oh, they, we just heard last week that we were going to schedule for like Wednesday or Thursday.

**Erik O'Brien:** And they're like, well, you're going to be on an offsite.

**Kenzie Amack:** So we switched it to today.

**Kenzie Amack:** Right.

**Kenzie Amack:** Yes.

**Kenzie Amack:** There's Marylise.

**Marylise Tauzia:** Hi, everyone.

**Erik O'Brien:** Hey, Marylise.

**Marylise Tauzia:** I was actually dipping your documents.

**Marylise Tauzia:** I was like, oops, it's them.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** That is first on the agenda today.

**Marylise Tauzia:** Yeah.

**Marylise Tauzia:** I through the ICP and the writing guidelines, which are both awesome.

**Marylise Tauzia:** I do have comments on the ICP.

**Marylise Tauzia:** And then I started the other one, but I don't have time to read all of it.

**Erik O'Brien:** Okay.

**Erik O'Brien:** And are we waiting for Mike?

**Marylise Tauzia:** Possibly.

**Marylise Tauzia:** Did you pay him, Kenzie, or should I?

**Marylise Tauzia:** No, I can.

**Marylise Tauzia:** And I'll do it.

**Kenzie Amack:** Okay.

**Kenzie Amack:** Cool.

**Kenzie Amack:** Hey, Mike.

**Mike Bilodeau:** Hey.

**Mike Bilodeau:** How are you doing?

**Erik O'Brien:** All right, let's jump into it.

**Erik O'Brien:** All right, you should be able to see my screen now.

**Erik O'Brien:** So just briefly wanted to go over the agenda.

**Erik O'Brien:** So since last week we did share those artifacts, it sounds like Marylise was just going through them, but any comments or feedback that you guys have after your review, just feel free to leave them in Notion.

**Erik O'Brien:** We'll have our team kind of update those based off feedback and if any other context changes as we get going with you guys.

**Erik O'Brien:** Our managing editors worked on your content strategy, so did a little bit of research to come up with that, which I can share in a bit.

**Erik O'Brien:** And then we also set up the Atlas, which is our content generation platform.

**Erik O'Brien:** And so we use those.

**Erik O'Brien:** It's three artifacts pretty heavily in Atlas.

**Erik O'Brien:** I'll just give you a quick preview of that.

**Erik O'Brien:** So they live here in the artifacts section.

**Erik O'Brien:** So the personas, guidelines, and company context.

**Erik O'Brien:** We also have products and services, which we will enrich based off, I think, we still need to schedule a product deep dive with you guys.

**Erik O'Brien:** And that's really just to hear from you guys how you would talk about the product, the main features, or the platform, rather.

**Erik O'Brien:** And so we can enrich those, and it'll get pulled in to our different pipelines.

**Erik O'Brien:** So article generation and assignments.

**Erik O'Brien:** Assignments you can think of as just blog titles.

**Erik O'Brien:** So we use a bunch of keyword research to fill that assignments pipeline, and it'll come up with dozens of different topics that we can explore.

**Erik O'Brien:** And then our main one is the article generation pipeline.

**Erik O'Brien:** So I just threw in a...

**Erik O'Brien:** A sample here for Top Runtime Optimization Techniques for LLM Inference.

**Erik O'Brien:** This is where, again, you can put in the topic a lot of assignment direction.

**Erik O'Brien:** So if we want it to be more technical or if we want it to be a listicle or a how-to, different direction there.

**Erik O'Brien:** And then once we run that, it kind of generates an assignment brief.

**Erik O'Brien:** So this is run against the SEMrush API.

**Erik O'Brien:** So really be able to target kind of our keywords and SEO optimizations for every article that we generate.

**Erik O'Brien:** So it'll kind of, as you see, target keywords.

**Erik O'Brien:** It'll come up with kind of a page title, meta description, URL slug for us.

**Erik O'Brien:** Look at who's doing well kind of in that organic search results against that topic keyword.

**Erik O'Brien:** But from there, once we have, you know...

**Erik O'Brien:** A little bit of editorial, kind of one of our experts come in and make sure that this all looks good, we will have it go run against the research, so perplexity API and other APIs to break down that initial assignment brief into multiple different questions, which are all run against, like I said, that API to go do research.

**Erik O'Brien:** And so it'll come up with multiple different questions, as you can see, each question goes pretty in-depth.

**Erik O'Brien:** And then once we're happy with the research and feel like it's fully fleshed out, we'll create an outline.

**Erik O'Brien:** Again, this is where our human editors spend a lot of time between the brief and the outline is probably most of the time, just to make sure we've got word count and everything looks good.

**Erik O'Brien:** From kind of where we're going directionally, just like everywhere else, garbage in, garbage out, so every step of the process, we kind of have our experts come in.

**Erik O'Brien:** And put their hand in the process.

**Erik O'Brien:** Once we're fine with the outline, then we come up with the article draft.

**Erik O'Brien:** As you can imagine, it is a draft.

**Erik O'Brien:** So we're going to go through, make sure that some of the H2s are looking good.

**Erik O'Brien:** Again, spend some time here and be able to just make sure everything's looking good before we send it upon the fact checker.

**Erik O'Brien:** So, again, this is where, well, open for me, but everything that's stated in here will run against multiple fact checkers and make sure that everything is technically accurate before we move on to internal linking.

**Erik O'Brien:** So this is where we can kind of cross link between other posts on your guys' website, generate SEO meta tags, and then even come up with some header images.

**Erik O'Brien:** We can definitely probably use some of your brand and style guidelines.

**Erik O'Brien:** And have our design team updated with some of those directions so that once we do kind of start getting to more content at Velocity, these will be a little bit more in line with your current brand and style guidelines that you guys have on like the guides and blog today.

**Erik O'Brien:** And then lastly, it'll come up with the final output of our article.

**Erik O'Brien:** Any questions before I move on from this?

**Mike Bilodeau:** No, I think the question for me is mostly going to be on source material.

**Mike Bilodeau:** What are the, yeah, do we have like citations or sources for where some of these things are getting pulled from?

**Erik O'Brien:** It will have that in the fact checker if for some reason it's not pulling it up.

**Erik O'Brien:** But yeah, we can go in and inspect what it used to find those sources.

**Erik O'Brien:** We can also...

**Erik O'Brien:** We also...

**Erik O'Brien:** Setup and the assignment brief, different, oh, maybe it's, we can basically set like different sites, blacklisted sites that we don't want to use as sources.

**Erik O'Brien:** So any competitors, anything that you guys know are kind of a little bit sensitive to kind of the content we want to pull in, we can exclude those.

**Erik O'Brien:** Or if you have whitelisted sources like your developer docs, we can include those as well.

**Erik O'Brien:** So we can get pretty custom if there's any concern about kind of where we're pulling any information from source-wise.

**Mike Bilodeau:** No, I think what I've run into in the past doing something similar is blended context and timeframes on content. Things go out of date really, really fast. Models have a tendency to get confused on the context of where certain things are talked about.

**Mike Bilodeau:** So I think citations would be useful for us to just, like, fully be able to kind of, like, vet against where certain content came from.

**Mike Bilodeau:** One on a, hey, like, if this is over a year old, odds are it's wrong.

**Mike Bilodeau:** And the second part is, like, if, yeah, it just kind of vetting again and again.

**Mike Bilodeau:** It's, like, making sure, yeah, like, okay.

**Erik O'Brien:** Yeah, so it's pulling from, like, archives, open review.

**Mike Bilodeau:** Yeah, quantization is not very complicated, so that one's probably fine.

**Erik O'Brien:** Yeah, I hear you.

**Erik O'Brien:** If there's...

**Erik O'Brien:** Let me just double check with the team to see how we can maybe pull from relevant or kind of set a time frame for sources that we use.

**Mike Bilodeau:** Yeah, we just want citations because I don't want to get attached to a single architecture view of the world. For us, there's TRT and vLLM, which we're more likely to recommend, and SGLang as the primary engines. Getting citations helps us figure out what to avoid and make sure we're linking to high credibility sources that are up to date.

**Erik O'Brien:** Yeah, and then for any of the linking that we do, we have a pretty heavy hand on that as well.

**Erik O'Brien:** Like, I'll go through before we even show it to you guys to just be like, does this make sense to link it here?

**Erik O'Brien:** Does this make sense to have as a, if it's, especially if it's external, is it, make sure it's not a competitor, make sure that it's not something that we wouldn't recommend or you guys wouldn't have as like stuff associated with your brand.

**Erik O'Brien:** So we can definitely kind of use our calibration period in these first few weeks to make sure that we get aligned and all that.

**Mike Bilodeau:** Yeah, cool. There are definitely things to vet, like quantization techniques we don't implement that way anymore. I think we'll want to dig through some of these because this may be from a year or two or three ago. The product has changed quite a lot, so I just want to make sure we're up to date.

**Mike Bilodeau:** would say, like, potentially part of the way to solve for some of these things is, like, we should just largely avoid source material that's over about a year old.

**Mike Bilodeau:** Yeah, and, like, the state-of-the-art change is really fast.

**Mike Bilodeau:** And, you know, with the exception of, yeah, yeah, I figure somebody's probably written on these topics in the last year that we can kind of go to.

**Mike Bilodeau:** But I worry, even for our own things, like, anything outside of a certain date is going to be...

**Mike Bilodeau:** Potentially off-base, especially for more technical aspects.

**Erik O'Brien:** Gotcha.

**Marylise Tauzia:** I have a question.

**Marylise Tauzia:** No, ahead.

**Marylise Tauzia:** Finish.

**Erik O'Brien:** It's another topic.

**Erik O'Brien:** No, I was saying I will definitely check with our team to see if we can get that set up to, like, avoid any source material that's over a year old.

**Mike Bilodeau:** Cool.

**Marylise Tauzia:** Yeah, the question I had was for these articles you're writing, will they go on our blog or are you going to create a new, new area?

**Marylise Tauzia:** I think we talked about it in the intro call.

**Marylise Tauzia:** Where do you see them go?

**Erik O'Brien:** Yeah, I think that's probably a discussion point.

**Erik O'Brien:** Because you guys do have dash blog, right?

**Marylise Tauzia:** Yeah.

**Erik O'Brien:** Yeah.

**Marylise Tauzia:** And we have guides when it comes to, like, more extensive white paper type things.

**Erik O'Brien:** Yep.

**Marylise Tauzia:** Yeah, so you're, yeah, blogging guide.

**Erik O'Brien:** Yeah, so.

**Erik O'Brien:** I would

**Erik O'Brien:** We can have a larger discussion on that.

**Erik O'Brien:** It might depend on the specific piece as well.

**Erik O'Brien:** Like if we want to go into something a little bit longer or more technical, putting that in guides versus any other kind of more SEO-friendly articles, have those live on the blog.

**Erik O'Brien:** At least that's the approach we've seen kind of with most clients.

**Marylise Tauzia:** Yeah, and for the guides, we actually have the copy displayed, but if they want to download, we're in the process of getting them, at least for them to just get a pure PDF out of it.

**Marylise Tauzia:** But the content is still there, so there is SEO benefits to them as well.

**Erik O'Brien:** Okay, perfect.

**Erik O'Brien:** So, yeah, so I think for this week, as we're still kind of getting calibrated, all of your feedback on the artifacts will be super helpful.

**Erik O'Brien:** But I see the space.

**Erik O'Brien:** Bye

**Erik O'Brien:** That product deep dive scheduled.

**Erik O'Brien:** I don't know if that's with you, Marylise, or somebody else on the team, but you can kind of think of it as, you know, if you're in a later stage with a client, like what would you present to kind of close the deal?

**Marylise Tauzia:** Yeah, yeah, we can do that.

**Marylise Tauzia:** think Rachel and myself can help.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** Editorial content strategy.

**Erik O'Brien:** So team, we have a bunch of reasons why we went this way, but I won't read all of that to you.

**Erik O'Brien:** I'll send you the link to this afterwards.

**Erik O'Brien:** But it's basically what we heard from kickoff and some of the kind of goals that you guys shared of how we came up with the strategy.

**Erik O'Brien:** And so really targeting kind of your core audience of ML engineers and technical leaders with the goal of kind of creating SEO and AEO optimized content that ranks in the top 10 for 15 or so target inference keywords in the first eight weeks.

**Erik O'Brien:** So really with the goal of positioning BaseTen is synonymous with fast inference, which we heard in kickoff, really building a content foundation for technical authority and association with performance, targeting these high intent inference optimization queries where competitors have kind of weaker coverage.

**Erik O'Brien:** So our team did some keyword gap analysis with competitors and really focused in on what topics and clusters can we start to go after and fill those gaps.

**Erik O'Brien:** And then really start to kind of lay the groundwork and establish a publishing rhythm so that we can measurably start to see like lead generation come through the next three, six months post-launch.

**Erik O'Brien:** So we'll get into some of the topic clusters I just want to preview for you guys.

**Erik O'Brien:** So again, a lot of rationale that we can, I'll have you guys.

**Erik O'Brien:** Read through rather than speak to you, but focus on audience personas, your goals, and that competitor content gap analysis that our team did to come up with these top four clusters.

**Erik O'Brien:** And again, we do a cluster approach so that we don't have to do spray and pray.

**Erik O'Brien:** I've kind of covered the entire gambit of what would be SEO optimized content, but really focus on ones that really align with the brand and that competitor gap analysis.

**Erik O'Brien:** So performance and optimization for production inference is the top high priority keyword, or sorry, top high cluster.

**Erik O'Brien:** So you can see kind of some of the sample keywords that fit under this cluster.

**Mike Bilodeau:** I was going pretty quick — when you're saying the competitors dominate with model release and GPU content, what does that mean specifically?

**Erik O'Brien:** Sorry, were you seeing that on screen?

**Mike Bilodeau:** Yeah, the top bullet that's currently visible about competitor content.

**Erik O'Brien:** So that's basically most of their content is about model releases and GPU content.

**Erik O'Brien:** So everything that they put out, sorry, I did skip over it.

**Kenzie Amack:** Oh, that like related?

**Mike Bilodeau:** Like everything that they focus on.

**Mike Bilodeau:** I think the question maybe from my side is like, I know they're putting out a lot of content.

**Mike Bilodeau:** But like, is it, is it effective?

**Mike Bilodeau:** Is it ranking?

**Erik O'Brien:** Yeah, that's what the team kind of came back with is that they're ranking for that model release and GPU content.

**Mike Bilodeau:** I'm just Google searching for the new models, and when I search for things like Llama or other models, I'm on page five and don't see Fireworks appearing. Everyone talks about new models — we do too, it's ubiquitous in the industry. But I'd love to understand: is what they're doing working? When I look at how their stuff performs on social, it doesn't seem to perform unless they boost it. From a search perspective, I don't really see it. Maybe I'm just missing what you're getting on the data side.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** So I will ask the team to kind of clarify that.

**Erik O'Brien:** They would typically be on with me, but they are ones in Bosnia.

**Erik O'Brien:** And one's in the Philippines, so they're getting close to midnight or 2 a.m.

**Erik O'Brien:** there.

**Erik O'Brien:** But next week, we will have a managing editor, one of our teammates that does most of this research, here on these calls, so they can kind of explain what they found in the data and answer that more directly for you.

**Erik O'Brien:** But in the meantime, I'll follow up with them and get an answer for you.

**Mike Bilodeau:** Cool.

**Marylise Tauzia:** Eric, sorry, go ahead.

**Kenzie Amack:** No, just want to say, Eric, just for, I think we have access to this, if not, or do you want comments live, just on the, I think I'm just looking at like one, a few balls under performance optimization.

**Kenzie Amack:** Like, how can we edit this?

**Erik O'Brien:** Yes, so comment, or you can suggest.

**Erik O'Brien:** Awesome.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Interesting.

**Kenzie Amack:** Feel free to leave as many comments as you like.

**Kenzie Amack:** Okay, cool.

**Marylise Tauzia:** Thank you.

**Marylise Tauzia:** Yeah, I had a similar comment because I think it's a lot of LLMs, and I think on performance, we shine with a lot with other models.

**Marylise Tauzia:** So I think we should capitalize on that.

**Marylise Tauzia:** I mean, LLMs are important, but I think we can say more with, like, crude and stuff, which is partly LLMs.

**Kenzie Amack:** Yeah.

**Kenzie Amack:** The other thing I think, too, is that, and just to clarify, so the sample keywords are the sample keywords that rank the highest for this category, or is that sample keywords that we think, no, just within those categories?

**Erik O'Brien:** Okay.

**Erik O'Brien:** Yeah, just to give a little flavor of, like, keywords that will be relevant to performance and optimization for production inference.

**Erik O'Brien:** Okay.

**Erik O'Brien:** So we probably won't use these after we do full keyword research to find what would go into those assignments pipeline that I showed you.

**Kenzie Amack:** But, yeah, these are just for example only.

**Kenzie Amack:** Yeah.

**Kenzie Amack:** So, Mike, Marilise, I'm curious of what's your – I kind of want to see what the rest

**Kenzie Amack:** Most of the numbers are here, but my thought is, like, these numbers should be, if I understand it correctly, our core positioning points, or am I off there of, like, the first thing that we want to position on is performance, and then that.

**Marylise Tauzia:** You mean the 80% latency reduction and 20 to 25%?

**Kenzie Amack:** No, even just the sections, right?

**Kenzie Amack:** Because if this is about, like, okay, these are the categories that we're going to build content around, like, my second one would be, like, yeah, I mean, I guess if we wrote content around GPU choice, we would show up there, but, like, that's not really core to our positioning.

**Kenzie Amack:** And so it's, like, how do we want to think about writing in that category?

**Kenzie Amack:** Because that's a very much GPU reseller.

**Kenzie Amack:** And then the other, like, I think the big one is, like, scaling and reliability, yes, of course.

**Kenzie Amack:** And then there's, like, security.

**Kenzie Amack:** And then there's something, there's probably something around, like, DevX.

**Kenzie Amack:** Thanks, Lam.

**Kenzie Amack:** Model management.

**Erik O'Brien:** We just started with these top four, but if there's a fifth cluster you guys want to go after that you know of, then absolutely, we can add it.

**Kenzie Amack:** Yeah.

**Mike Bilodeau:** I think, Kenzie, you're right.

**Mike Bilodeau:** I mean, I would, if we're stack ranking these, I would put number two fourth.

**Mike Bilodeau:** I also think two is mainly around, like, we know that this type of content performs because it is, like, a very narrow view, but I think we're more maybe interested in, like, economics of inference versus just GPUs.

**Mike Bilodeau:** Because, yeah, if we're fighting in that, the GPU choice and, like, cost efficiency realm, there's a little bit, like, we, it's almost thought leadership stuff versus not, like, most of that is going to put us in the same realm as, you know, Lambda.

**Mike Bilodeau:** And all the NeoClouds, the hyperscalers, NVIDIA, et cetera.

**Mike Bilodeau:** That said, like that content performs extremely well.

**Kenzie Amack:** I just don't know that it pushes our ICP.

**Kenzie Amack:** Yeah, but the two things I'm wondering, and I just want to get thoughts here is like, if we think about, if I think about like, what would our ICP be searching?

**Kenzie Amack:** And therefore, what, when would we want to be in front of them?

**Kenzie Amack:** It's like a model optimization, absolutely.

**Kenzie Amack:** Reliability, absolutely.

**Kenzie Amack:** And then the other one is something around like build versus buy.

**Kenzie Amack:** So it is something around cost efficiency.

**Kenzie Amack:** I'm trying to think of like the right category for it, but I think maybe.

**Kenzie Amack:** Yeah, that's correct.

**Mike Bilodeau:** Yeah.

**Mike Bilodeau:** It's more build versus buy oriented content.

**Mike Bilodeau:** Yeah.

**Mike Bilodeau:** Like there's a through line there for all of it, but yeah, I mean, the GPU choice, like we do have, we have a blog that is, I think, A100 versus A10G, which is like our probably probably best performing.

**Kenzie Amack:** You know, GPU content has value there.

**Mike Bilodeau:** think the difference is that, yeah, like we also have, you know, LLM transformer guide or like whatever, which feels a lot more relevant to our audience.

**Mike Bilodeau:** So I agree.

**Mike Bilodeau:** I think I would just, I think we need to probably reshape that one because like best GPU for imprints.

**Kenzie Amack:** Yeah, but maybe, Erik, what we could add is that if we do, like Mike, if these do perform, then we just need to think about adding a small block somewhere in there that positions us within this category.

**Mike Bilodeau:** Yeah, that's the thing.

**Mike Bilodeau:** I think this stuff performs probably better than anything else.

**Mike Bilodeau:** It's like we would just need, like there needs to be thought around how we use it to move people from this way of thinking to, you know, more holistic TCO economics.

**Kenzie Amack:** Okay.

**Marylise Tauzia:** Yeah, and I think it can be part of the content, the content of the piece.

**Marylise Tauzia:** Because you're going to get the traffic from that.

**Marylise Tauzia:** as long as you talk about, like, you know, the elastic access to the GPU and the fact that you use them only when you need them, like, it's all around cost efficiency.

**Marylise Tauzia:** But at least we get the traffic.

**Mike Bilodeau:** Yeah, I agree.

**Mike Bilodeau:** Yeah, it's probably the fun side of those things.

**Mike Bilodeau:** But I do think, yeah, it's, people are talking about hardware always.

**Mike Bilodeau:** We see that.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Yeah, so I think I'll definitely move this down to fourth.

**Erik O'Brien:** And then if you guys have any other thoughts, comments, of kind of how you want to reposition this cluster, more than happy to take another spin on this.

**Erik O'Brien:** Or if we want to add a fifth cluster, open to that too.

**Mike Bilodeau:** Yep.

**Erik O'Brien:** And just make sure they're in priority order or however you guys see them.

**Marylise Tauzia:** Okay.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** So, yeah, just a quick preview of this.

**Erik O'Brien:** know it's a little bit of an article itself to read.

**Erik O'Brien:** So all feedback on the content strategy and the artifacts are super important as we get calibrated and make sure that we're heading in the right direction here in week two.

**Erik O'Brien:** Marylise, it sounds like we can schedule that deep dive probably for next week, I assume, because you guys have the offsite this week.

**Marylise Tauzia:** Yeah, yeah, if you want to give us time, like early, early in the morning would be better because Rachel is in Germany.

**Erik O'Brien:** Okay.

**Marylise Tauzia:** But yeah, we'll coordinate.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** And then is there any, do you guys have any brand style guides, Figma files, anything that our design team can take a look at?

**Marylise Tauzia:** Yep.

**Marylise Tauzia:** Just to adjust some direction of that imagery.

**Marylise Tauzia:** Yeah.

**Erik O'Brien:** Okay, wonderful.

**Erik O'Brien:** All right.

**Marylise Tauzia:** And so for next week, we're both...

**Marylise Tauzia:** So I have a question.

**Marylise Tauzia:** Like, you were, like, talking about the SEO optimization and stuff.

**Marylise Tauzia:** Just making sure that's also working for L&M searches.

**Marylise Tauzia:** Like, that's all part of it.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** So just like you guys were saying, like, we try to get these first pieces in place.

**Erik O'Brien:** So definitely audience personas and really get into the mind of people that are your ICPs and core audience.

**Erik O'Brien:** And then we'll start to track in Scrunch, which is our LLM visibility tool of, you know, dozens of different prompts and variants of those prompts to start tracking.

**Erik O'Brien:** Like, are we showing up, especially after we get content generating?

**Erik O'Brien:** Like, are these keywords relevant to the people that are searching within Perplexity, Claude, et cetera?

**Erik O'Brien:** And so our...

**Erik O'Brien:** Our kind of core philosophy is like if you're doing that towards your audience and you're still playing the SEO game, then you're probably doing GEO pretty well too.

**Erik O'Brien:** So yeah, LLM visibility is kind of top priority along with SEO and their content strategy to go hand in hand.

**Mike Bilodeau:** Cool.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** So yeah, next week we'll have a little bit more on the content based off keyword research.

**Erik O'Brien:** So we'll have a few draft articles or at least topics for you guys to review and approve.

**Erik O'Brien:** From there, we'll get into calibration and start to set up some performance tracking and reporting.

**Erik O'Brien:** And I think that's the last ask that I have is we sent over some Google Search Console, Google Analytics, and CMS emails to share access with.

**Erik O'Brien:** If you guys have any issues with sharing to a team access account, just let us know.

**Mike Bilodeau:** No, that's fine.

**Marylise Tauzia:** Cool.

**Marylise Tauzia:** OK.

**Marylise Tauzia:** Great.

**Marylise Tauzia:** Thank you.

**Erik O'Brien:** Thanks, guys.

**Erik O'Brien:** Have a good offsite.

**Erik O'Brien:** See you.

**Erik O'Brien:** Bye.
