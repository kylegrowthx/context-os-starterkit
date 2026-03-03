# Biologica <> Growth X - Weekly Sync

<metadata>
date: 2025-09-18
time: 19:00 UTC
duration: 29 minutes
organizer: matthew@growthx.ai
participants: Matthew Panzarino (GrowthX), Liz Zwillinger (Biologica), Brian Magida (Biologica)
fathom_recording_id: 88318129
fathom_url: https://fathom.video/calls/413696265
share_url: https://fathom.video/share/gipcyEKzVHxj6CYFdpXz6CZJLF835TSZ
source: fathom
enriched_on: 2026-03-03 14:32 UTC
</metadata>

---

## Summary

Liz Zwillinger flagged a significant quality regression in Biologica's article output — recent pieces on calcium and alcohol showed disorganization, repetitive content, off-brand recommendations, and failures to follow established guidelines (like excluding data contradicting supplement efficacy). Matthew committed to fast-tracking a new agentic pipeline with enhanced adherence checking, using the problematic articles as test cases, and integrating Liz's structural feedback on introducing clear article format (intro with euphemisms, data-focused key takeaways, supporting paragraphs, conclusion) to prevent topic repetition and improve logical flow.

---

## Context

Biologica is a health and wellness content company that works with GrowthX on content generation and optimization. This weekly sync is a critical check-in on the quality and consistency of Biologica's article output. After a period of positive progress through July, the process regressed starting in mid-August, generating articles that feel machine-written, repeat content across sections, and violate core writing guidelines. Liz has invested heavily in reviewing and annotating problematic articles, providing detailed feedback that should be reflected in the system but isn't being enforced. The relationship depends on GrowthX delivering a reliable, human-quality output engine that balances SEO requirements, AI accessibility for LLM citations, and genuine editorial standards.

---

## Relevance

**To GrowthX Delivery:**
- Article quality regression after Aug 14 is a critical delivery failure — need to investigate what changed in models, researchers, or pipeline configuration on that date to understand root cause
- Writing guidelines are too long and causing LLM confusion; Matthew is exploring segmentation into "theology" (core writing philosophy) vs. "rules" (tactical execution) to improve adherence
- Proposed standardized article structure (intro with euphemisms → data-driven key takeaways → supporting paragraphs → warm conclusion) needs to be formalized in guidelines and enforced by agentic pipeline
- New agentic pipeline with adherence scoring must solve the core issue: existing workflows don't validate that rules are actually being followed before output

**To GrowthX Business Development:**
- Risk signal: Liz has spent 50+ hours on review and feedback with minimal visible progress; this is eroding client trust and account health
- Positive momentum in July shows capability exists; recovery path is clear (new pipeline + rule enforcement) but requires delivery on promised timeline (late next week)
- Biologica may be test case for handling more complex, culturally sensitive content (like the perimenopause social media article mentioned); success here validates GrowthX's ability to handle nuanced topics

---

## Overview

- Recent articles (calcium, alcohol) show regression in quality, organization, and adherence to guidelines
- New agentic pipeline with updated writing guidelines to be implemented within a week
- Focus on improving article structure, realistic recommendations, and consistent adherence to content rules
- Team to use successful past articles as benchmarks and refine the process to match that quality

---

## Key Topics

### Article Quality Concerns

  - Liz expressed frustration with recent articles, noting regression since July
  - Issues include disorganization, repetitiveness, and inappropriate use of euphemisms
  - Specific problems in calcium article: inclusion of previously removed WHO data on kidney stones
  - Alcohol article criticized for unrealistic and outdated social recommendations

### Content Generation Process

  - Matthew proposed implementing new agentic pipelines to improve adherence to guidelines
  - Team to use recent problematic articles as controls to test improvements
  - Balancing act between human readability, SEO requirements, and AI-friendly content structure
  - Plan to standardize article format while maintaining SEO benefits

### Writing Guidelines and Artifacts

  - Current guidelines may be too long, causing LLM confusion
  - Proposal to separate general theology of writing from specific rules
  - Need for clearer structure: intro (with euphemisms), key takeaways (data-focused), supporting paragraphs, conclusion
  - Importance of logical flow and avoiding topic repetition

### Realistic Recommendations

  - Emphasis on providing culturally relevant and up-to-date advice, especially for sensitive topics like alcohol consumption
  - Need to address more complex, cultural articles (e.g., perimenopause awareness on social media) with appropriate voice

### Technical Improvements

  - Investigation into potential changes in models or pipelines that may have caused quality regression
  - Plan to implement stricter adherence to rules, especially regarding supplement risks and controversies

---

## Action Items

**Matthew Panzarino**
- Review Liz's feedback on latest articles w/ fine-tooth comb. Focus on disorganization issues.

- Fast-track implementation of new agentic pipelines. Rerun problematic articles (calcium, alcohol) as test.

- Review "good" article example from previous week. Reverse-engineer for artifacts.

- Integrate Liz's feedback on article structure/flow into writing guidelines. Add instruction re: logical flow.

- Reinforce rule in guidelines: don't include data contradicting product purpose (e.g., supplementation worthless).

- Investigate changes around Aug 14 when articles were reportedly good. Check models, researchers used.

- Share progress updates, findings async in Slack for Liz to review.

- Have Alice add Liz and Brian to company Slack channel for easier communication.

---

## Transcript
**Liz Zwillinger:** Okay, I'll go ahead.

**Liz Zwillinger:** Hold on one second.

**Liz Zwillinger:** Hi.

**Liz Zwillinger:** All right.

**Liz Zwillinger:** This meeting is being recorded.

**Liz Zwillinger:** I had a chance to review the two new articles.

**Matthew Panzarino:** Okay, great.

**Liz Zwillinger:** They're not good.

**Liz Zwillinger:** I don't know how to, what's going on.

**Liz Zwillinger:** I'm feeling pretty frustrated.

**Liz Zwillinger:** I went back and looked at articles from July, and I don't see a ton of material progress in the last two months on this.

**Matthew Panzarino:** Okay.

**Liz Zwillinger:** I feel like I've been spinning my wheels.

**Liz Zwillinger:** I spent like at least 50 hours reviewing these articles and making notes, and it's not, we're not moving the ball.

**Liz Zwillinger:** I mean, I don't know from a process perspective if we're not doing things in the right way.

**Liz Zwillinger:** I mean, I went through and looked at the artifact and, like, made my comments and didn't seem like anything was, like, grossly off on that.

**Liz Zwillinger:** I felt like my comments were, like, fairly minor.

**Liz Zwillinger:** But somehow there's a disconnect between what's in the article and, like, how – sorry, what's in the artifact and how these articles are reading.

**Liz Zwillinger:** They are ultra-repetitive, which I know part of that is some of the LLM searching.

**Liz Zwillinger:** Things are – they feel disorganized.

**Liz Zwillinger:** There's, like, topics in the wrong sections.

**Liz Zwillinger:** So, for example, a section titled, you know, Other Ways to Build Bone Health Beside – an article about calcium supplements.

**Liz Zwillinger:** There's, like, other ways to build bone health besides calcium supplementation.

**Liz Zwillinger:** Strength training is, like, paragraph one.

**Liz Zwillinger:** Paragraph two, we're talking, again, about leafy greens and eating.

**Liz Zwillinger:** And it's, like –

**Liz Zwillinger:** No, that was already, we already covered that like four sections above in the diet section.

**Liz Zwillinger:** How did this like leafy, eating leafy greens end up in a other ways to build bone health section?

**Liz Zwillinger:** So it's very, it feels very disorganized.

**Liz Zwillinger:** The paragraphs are jumping around.

**Liz Zwillinger:** It's feeling more disorganized than the July articles, which had a better flow to them.

**Liz Zwillinger:** Um, I feel like some of the euphemisms, the use of euphemisms is still off.

**Liz Zwillinger:** It's substantially less than before, which is good, but they're being used in the wrong ways.

**Liz Zwillinger:** So like in areas that I want, like just clean, clear scientific statements, like in a bulleted list, key takeaways.

**Liz Zwillinger:** They're like, you know, a body working off a script you haven't read.

**Liz Zwillinger:** It's like, no, no, that's not those euphemisms, the place for the euphemisms to make you feel warm and seen are like the intro sentence, the concluding sentence, not in these like kind of more scientific.

**Liz Zwillinger:** Like, boom, boom, boom, kind of, you know, bullets.

**Liz Zwillinger:** Okay.

**Liz Zwillinger:** And then the part that's, like, the most worrying is, like, we just went through on a most recent on this calcium supplementation article last week and commented on removing this World Health Organization data, which was showing increase in kidney stones and that calcium supplementation had no noticeable impact on hip fractures. And we said last week, like, don't include this.

**Liz Zwillinger:** And somehow it ended up again in the article again this week, the exact same thing.

**Matthew Panzarino:** Interesting.

**Liz Zwillinger:** Okay.

**Liz Zwillinger:** So, and then the alcohol article is a mess.

**Liz Zwillinger:** Just all over the place.

**Matthew Panzarino:** It's disorganized.

**Liz Zwillinger:** The, the, the, and really kind of what we just sent you, mean?

**Liz Zwillinger:** Yeah, I looked at the ones that were just sent and I looked at the edited draft, the tab, the alcohol one, you know, also like besides being very disorganized, it's like just really off.

**Liz Zwillinger:** Like, for example, talking about smart strategies that work in real life to cut back on alcohol use and one of them is, you know, it's just fine.

**Liz Zwillinger:** Like order, if you're at a restaurant, order a glass of wine and also order a sparkling water with citrus and like alternate them so that you're slipping the wine more slowly.

**Liz Zwillinger:** And then it says, this natural pacing cuts your alcohol intake while keeping your hands busy, your social presence intact.

**Liz Zwillinger:** Bonus, servers often assume the sparkling water is a gin and tonic, so no awkward questions.

**Liz Zwillinger:** And it's like, that's just not reality.

**Liz Zwillinger:** Like a server is never going to care whether you ordered a sparkling water.

**Liz Zwillinger:** Right.

**Liz Zwillinger:** Like, why, why, it's like bad feeling that like somehow you have to pretend like it's a gin and tonic, like.

**Liz Zwillinger:** It's fine to have a sparkling water.

**Liz Zwillinger:** In 2025, that's like a really off recommendation.

**Liz Zwillinger:** And it came up again in that same article on, where is it?

**Liz Zwillinger:** Oh yeah, hack the social game.

**Matthew Panzarino:** Keep your wine glass, but swap out the contents.

**Liz Zwillinger:** No one needs to know, is what it says.

**Liz Zwillinger:** Like, that's also, like, you're supposed to be hiding the fact that you have sparkling water in your wine glass.

**Liz Zwillinger:** Like, it's just not, it reads like a computer wrote it.

**Liz Zwillinger:** And I just, I don't know where to go from here, but I'm starting to get pretty frustrated that we're, like, many months down this road.

**Liz Zwillinger:** And it's, we're still, I don't think we've made any progress in terms of getting these articles out in a way that feels like a human wrote them.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Let me take a look.

**Matthew Panzarino:** I think we probably need to do some engineering work.

**Matthew Panzarino:** Let me look through your feedback in these latest ones with like a fine-tooth comb and try to understand what you're talking about on the disorganized aspects.

**Matthew Panzarino:** There's probably some engineering we can do there to help that.

**Matthew Panzarino:** I do feel that the agentic pipelines will show an improvement in this regard.

**Matthew Panzarino:** They have shown it for other clients.

**Matthew Panzarino:** We're trying to build this one out and reprocess articles with it, but it's not ready this week, hopefully early next week.

**Matthew Panzarino:** So let me try running it with the new pipelines rather than trying to belabor the point with like fine-tuning these existing artifacts because I think the artifacts are actually pretty sound.

**Matthew Panzarino:** Like I look through them after you edited them, look through your suggestions, and I think that the writing guidelines as an example are pretty sound.

**Matthew Panzarino:** It's just seemingly not adhering to them as well as we'd like.

**Matthew Panzarino:** And I think that's one of the strengths of the new pipelines is that they do improve adherence and actually score relevance and adherence where these existing pipelines don't.

**Matthew Panzarino:** So let me fast track that and then rerun these.

**Matthew Panzarino:** We can use these articles, especially since you've had a lot of thoughts on these and valid complaints.

**Matthew Panzarino:** Let's use these as controls and let's run new versions of these with the new pipeline and then do a litmus test there before we, you know, wander off into other articles.

**Matthew Panzarino:** Because if we can get these, which you were especially displeased with to be better, then I think we're in a better place.

**Matthew Panzarino:** So let's work on that.

**Liz Zwillinger:** I just want to make sure that like, I mean, for the last two months, all of these edits we've been doing, like that they are being incorporated. I'm sort of feeling like I was spinning my wheels.

**Matthew Panzarino:** Those edits all make their way into the writing guidelines.

**Matthew Panzarino:** The guidelines that exist today are based on your comments. And so like when you went through and added some new edits to the guidelines, which is appreciated.

**Liz Zwillinger:** Yeah, I saw some of them in there. But one thing that keeps coming up is the need for realistic suggestions. For example, the first edit of the alcohol article that we talked about last week was pairing your martini with a cup of Greek yogurt — that's not realistic.

**Liz Zwillinger:** And this time around, it's like sparkling water.

**Liz Zwillinger:** Your server doesn't need to know that it's sparkling water.

**Liz Zwillinger:** He's going to think it's a gin and tonic, like also like no human, whatever.

**Liz Zwillinger:** So it's like multiple times, like I keep.

**Liz Zwillinger:** Getting the like no human, forget about like someone who knows anything about women's health, like just a human wouldn't recommend that.

**Liz Zwillinger:** And so I don't know like where that, like where that is in the artifacts.

**Liz Zwillinger:** I tried to write at one point like kind of realistic, but there still is like really lacking like a human, like I still feel like it's lacking that human touch in the way that these recommendations are just, it feels like a robot spit it out because no one would ever do that.

**Matthew Panzarino:** Mm-hmm.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Let me take these recent edits too, and I'll go over these and look at ways to engineer these specific pieces of feedback as a separate workflow as well.

**Matthew Panzarino:** Because that way we can do an adherence check pass, just saying "Hey, are you actually doing these things?" This is why the new pipelines are so much better because LLMs need validators to tell them when they're missing the mark and to check again.

**Matthew Panzarino:** The guidelines are, one of the major issues is that these guidelines are long.

**Matthew Panzarino:** And they're long because we've taken, you know, all of your comments and sort of added them as instrumental elements to the style that you want to put out.

**Matthew Panzarino:** But they are, when they get long, the LLMs sometimes get a little lost.

**Matthew Panzarino:** So I'm also trying to think about ways to segment this.

**Matthew Panzarino:** One of the ways we've been thinking about this with some other clients is separating out the general theology of the way you want to write.

**Matthew Panzarino:** Like grounded, you know, simplistic, straightforward examples.

**Matthew Panzarino:** Don't get too fancy with the examples.

**Matthew Panzarino:** Don't get too elaborate. Rules are about punctuation and keeping sentences simplistic and straightforward.

**Liz Zwillinger:** Yeah, you've got to try a few different strategies.

**Liz Zwillinger:** Because it's not working, we currently have, so whether it's a new pipeline, or two different documents, I think you can simplify the structure, because I'm seeing it kind of all over the place.

**Liz Zwillinger:** So for example, we have like an intro section, right, right underneath the heading, which that will, that's where the euphemism comes in on, you know, making you feel like you're not making this up, whatever that, like, the soft, softer, friendlier language is.

**Liz Zwillinger:** Then it goes to the key takeaways, which are zero euphemisms, bullet points, like here is the data, there should be the most number of like MD sites in the key takeaways.

**Liz Zwillinger:** And then it should break into, you know, three to four paragraphs that support each of those bullet points.

**Liz Zwillinger:** Like I feel in some ways, like my sixth graders who are learning how to write an argumentative essay, you know, you like, write your thesis, and then you put your supporting paragraphs.

**Liz Zwillinger:** So each paragraph should be based on bullet point number one, bullet point number two, etc.

**Liz Zwillinger:** And then, you know, the end, and then, you know, biologica should be woven throughout where it makes sense.

**Liz Zwillinger:** And then there's a concluding paragraph that mirrors the intro paragraph, which has warm euphemisms and a summary of the key takeaways in sentence form. If you follow that structure, it won't get as messy in terms of organization.

**Liz Zwillinger:** I mean, the alcohol article just has, it's like all over the place in the way that it's organized.

**Matthew Panzarino:** We can create a rough format for these articles, especially the ones that are, you know, informational, right?

**Matthew Panzarino:** This cluster of work that we've been doing is all kind of informational.

**Matthew Panzarino:** The way that the pipelines generate things now is what is the structure that makes the most sense for the keywords?

**Matthew Panzarino:** And so it does SERP analysis and says, hey, what ranks well for these keywords?

**Matthew Panzarino:** What are the kinds of articles and how are those structured?

**Matthew Panzarino:** That can introduce oddities, right?

**Matthew Panzarino:** It can introduce sections that you're like, why is this section in here?

**Matthew Panzarino:** Well, the answer is really because it ranks really well for these keywords, right?

**Matthew Panzarino:** And it will generate organic traffic, all that.

**Matthew Panzarino:** But at this point, if you're building an establishing body of content, maybe we should standardize around a rough format, like the one you described, which I think is totally fine.

**Liz Zwillinger:** I saw some version of that in the artifacts.

**Liz Zwillinger:** I saw a version of the format in the artifacts.

**Matthew Panzarino:** And so maybe instead of starting from scratch, because again, I don't want to overcorrect.

**Liz Zwillinger:** And then use that, the ranking, which I get is really important for this.

**Liz Zwillinger:** So maybe, you know, I don't want you to, like, take what I'm saying literally.

**Matthew Panzarino:** Literally.

**Matthew Panzarino:** And then do it.

**Matthew Panzarino:** No, no, I get to feel like the articles are better.

**Liz Zwillinger:** And then lose the whole point of that.

**Matthew Panzarino:** Yeah, it's a balance because you have to balance.

**Matthew Panzarino:** Now we're balancing three different things, which is human readability and actual value.

**Matthew Panzarino:** So time on site, whether they feel it's actually viable information, which therefore adds to your authority, you know, as an authority on the topic.

**Liz Zwillinger:** And therefore, your product should be good.

**Matthew Panzarino:** And you have to balance geo, which it definitely prioritizes clustered questions and answers and clustered content.

**Matthew Panzarino:** Because it takes like six to 800 token chunks at a time and says, is there an answer for me here?

**Matthew Panzarino:** Cool.

**Matthew Panzarino:** I'm going to cite this as an answer for this question that somebody's asking in an LLM.

**Matthew Panzarino:** And then the third, of course, is the bog standard SEO stuff.

**Matthew Panzarino:** So it's a balancing act between those three.

**Matthew Panzarino:** And it can, there's some tension and elasticity there where an article could be like.

**Liz Zwillinger:** Well, and I don't have visibility into two and three.

**Liz Zwillinger:** That's where I have to rely on your expertise.

**Liz Zwillinger:** And I don't want you to feel like I don't want to tie your hands.

**Matthew Panzarino:** No, no, I get it.

**Liz Zwillinger:** Yeah.

**Liz Zwillinger:** To be able to like really.

**Liz Zwillinger:** I want to make sure that's very clear.

**Liz Zwillinger:** So, and I just, I don't know, it's a kind of a bummer, but like when I was going back and looking at those July articles right before this call, I'm like, it's not, these are not that bad.

**Liz Zwillinger:** Like, did we overdo it?

**Matthew Panzarino:** Okay.

**Brian Magida:** And like, yeah, actually, sorry, just to, just to tie that for a hot second, because I, I'm just, I've been like trying to play this, this whole thing, like, almost like, how did we get here?

**Brian Magida:** And I, I do recall one of the, the things I heard from Liz back over the summer, it was like, it seemed like we're getting closer.

**Brian Magida:** Like, there was this moment where it's like, we're getting closer.

**Brian Magida:** And then it was almost like a, like, it's that meme where it's like, we got to the fork in the road and we just went like, like all the way over.

**Brian Magida:** And it's, it's like unclear, like what exactly happened.

**Brian Magida:** Cause it seemed like we kept on doing the things that we had been doing and then in my like sort of ad hoc check-ins with Liz, it was, I.

**Brian Magida:** I kept on hearing more like, oh, we're feeling off.

**Brian Magida:** It's like, it's going more in the wrong direction.

**Brian Magida:** So I don't, I can go back in my notes and try to find like that exact moment in time, like what week that was.

**Brian Magida:** But it's, again, I don't know if we introduced something into an artifact or if like the underlying models that you're using, because they're obviously updating these models all the time.

**Brian Magida:** Like, are we using a different model that might be causing this?

**Brian Magida:** So we're just like putting it out there.

**Matthew Panzarino:** There was like a moment where.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** One way to triangulate that, or at least give me something to look at, because I can look at, I mean, everything is recorded, right?

**Matthew Panzarino:** So we have what versions of the artifacts we were using at that time.

**Matthew Panzarino:** We also have the changes to the pipeline, et cetera.

**Matthew Panzarino:** So I kind of know what the product worked and looked like at any given moment.

**Matthew Panzarino:** So if you want to, if you think you can identify, and it doesn't have to be to the day and date, but like kind of like a week or two window where you're like, hey, know, things started to get a little bit haywire.

**Matthew Panzarino:** So we're like,

**Matthew Panzarino:** After this point, let me know.

**Matthew Panzarino:** And then I will look at that.

**Matthew Panzarino:** And if I can isolate something there and, you know, roll it back or look at some way to kind of reset ourselves to that point, that can be helpful.

**Matthew Panzarino:** And then in parallel.

**Liz Zwillinger:** There's also like examples.

**Liz Zwillinger:** We have plenty of examples of like great articles.

**Liz Zwillinger:** Remember like from last week, I was like, this one's great.

**Liz Zwillinger:** Like how did this one, you know, and so I asked you if you could reverse engineer and figure out how that one was written and like put that in the artifacts.

**Liz Zwillinger:** But if you guys could go through, I think you said you were going to go through the good one.

**Liz Zwillinger:** Yeah.

**Matthew Panzarino:** I haven't had a chance to go through the good one yet, but I will.

**Matthew Panzarino:** It's the reason that I said we marked those, but they can be used as inputs to the agentic pipeline as artifacts.

**Matthew Panzarino:** And we can have it reference them as like examples of good.

**Matthew Panzarino:** This pipeline doesn't work.

**Liz Zwillinger:** From a process perspective, I don't want to look at articles if you haven't fixed the model.

**Liz Zwillinger:** Like, so, it just, it takes too long.

**Matthew Panzarino:** It's so much time I've spent on this already.

**Liz Zwillinger:** Right.

**Liz Zwillinger:** So I feel like we got new articles today that I looked at, but it sounds like you hadn't made the edits yet.

**Liz Zwillinger:** So, I don't know.

**Matthew Panzarino:** I just want to, like, Brian, you've been making this These new articles have the new writing guidelines in that pipeline.

**Matthew Panzarino:** So we regenerated these with the new guidelines.

**Matthew Panzarino:** That's why they're, like, if you look through here, there are not a ton of sentences with a lot of secondary clauses and things like that.

**Matthew Panzarino:** So that adherence is improved from those rough standpoints.

**Matthew Panzarino:** But obviously, the flow of the article still needs to be addressed.

**Matthew Panzarino:** And that's something that I need to think about.

**Matthew Panzarino:** I mean, I'll take your feedback from this and think about how we parse that for, like, a rough format and flow standpoint.

**Matthew Panzarino:** and feedback from then then I'll I'll I'll I'll I'll I'll

**Matthew Panzarino:** Try and kick over the agentic pipelines.

**Matthew Panzarino:** I don't know if it's like, I'm trying to think what is like the most valuable and least impactful use of your, or least impact on your time, and the most valuable way to go about this would be.

**Matthew Panzarino:** And I'm almost positive that it's, we should just get the agentic pipeline shipped with the new writing guidelines, with some feedback that you just gave me integrated, and then regenerate these control articles, and use those examples of good, and see where we come out.

**Matthew Panzarino:** Let me do that before we start like embarking on, hey, look at this random stuff.

**Liz Zwillinger:** Is this good?

**Matthew Panzarino:** And we'll see where we go for it.

**Liz Zwillinger:** when do we get that?

**Matthew Panzarino:** When can we have that done by?

**Matthew Panzarino:** I would say like, give me a week.

**Matthew Panzarino:** So maybe late next week.

**Matthew Panzarino:** I'll try and kick engineering in the pants to get that rolling as well.

**Matthew Panzarino:** I know it's already in process, they're building it, I just need to get them to finish it so and hand it over.

**Matthew Panzarino:** But let me work on that.

**Matthew Panzarino:** We should be able to get you new articles almost on schedule next week, I would guess, but with an asterisk of I don't know exactly how close they are to finishing.

**Matthew Panzarino:** So let me check on it.

**Liz Zwillinger:** But I just feel like it's the path forward for all of the stuff we're going to generate with you, so we might as well calibrate to the newest version of what we have.

**Liz Zwillinger:** Yeah.

**Liz Zwillinger:** And then how are we going to address, like, the realistic?

**Liz Zwillinger:** You know, like, this issue with the alcohol article issue with, like, servers carrying, you have a fake gin and tonic in your glass.

**Liz Zwillinger:** Yeah.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** That's an interesting one, because, like, if you pull that apart, it's like, okay, don't address.

**Matthew Panzarino:** It's like, the societal norms thing is interesting, because if you were to position it as, if you are in a social.

**Matthew Panzarino:** And you don't want to talk about it, then that's almost acceptable, even though I don't care.

**Matthew Panzarino:** You know, like I personally am like, why would you even care?

**Matthew Panzarino:** And I think more people are thinking that way.

**Matthew Panzarino:** I mean, if you think in a larger context, you know, NA beverages and not drinking in social settings is essentially the new wave, both generationally and, you know, just topically.

**Liz Zwillinger:** I mean, that article is particularly tricky because most of our other articles don't have like this kind of human piece of, there's no social part to it, right?

**Liz Zwillinger:** Like when you're talking about calcium supplementation and ways to improve your bones, like what your friend thinks about you taking calcium supplements, not part of the article.

**Liz Zwillinger:** So I guess alcohol, maybe alcohol one is kind of a bad example because it's.

**Matthew Panzarino:** It might be, I mean, it's a hot button topic at the best of times, right?

**Liz Zwillinger:** It's just, but it, you know, it doesn't give me any confidence that like for less science-based articles.

**Liz Zwillinger:** We're trying to write an article about increased awareness of even the word perimenopause in social media.

**Liz Zwillinger:** I want you guys to write an article about a summary of last week's perimenopause posts, like the new data that's come out.

**Liz Zwillinger:** And you're trying to reference all these doctors posting about perimenopause on Instagram.

**Liz Zwillinger:** That's not a science-based article.

**Liz Zwillinger:** It's like more of a cultural, there's a cultural piece to it.

**Liz Zwillinger:** And I want to make sure that that voice is right also.

**Matthew Panzarino:** Yeah, I don't think we should shy away from trying to make this work, right?

**Matthew Panzarino:** I think it's a, the more complex it is, the more it's going to tell us about the strengths or weaknesses of the product, the more tricky of Okay, so let's keep the alcohol one in as a good example.

**Matthew Panzarino:** Yeah, exactly.

**Matthew Panzarino:** Because I don't think shying away from those is the smart thing to do long-term, you know?

**Matthew Panzarino:** Because you will want more complex issues addressed, and we want to be prepared for it.

**Matthew Panzarino:** So, um...

**Matthew Panzarino:** Yeah, we'll keep it in as a control.

**Matthew Panzarino:** I'll take a look at what we can generate there that's new.

**Matthew Panzarino:** And then on the, like, the calcium part, a lot of that is flow-based.

**Matthew Panzarino:** So I think I can come up with something as well, an additional instruction for the writing guidelines that just reinforces logical flow.

**Matthew Panzarino:** And it's like, you know, don't readdress topics, move on to the next, keep a logical flow through here.

**Liz Zwillinger:** Yeah.

**Liz Zwillinger:** The other big one, though, in the calcium, I don't want to get this overlooked, is, like, including data that says that supplementation is worthless.

**Liz Zwillinger:** Like, let's, can we, like, write a rule about that, you know?

**Matthew Panzarino:** Yeah, yeah.

**Liz Zwillinger:** You know, we have a rule about that.

**Liz Zwillinger:** You know, but it didn't, you go back and look at my comments.

**Liz Zwillinger:** It didn't register.

**Matthew Panzarino:** didn't adhere to that.

**Matthew Panzarino:** Yeah, yeah.

**Matthew Panzarino:** Actually, let me look at something really quickly.

**Matthew Panzarino:** One thing I did notice is that we may have to double down on adherence to that because...

**Matthew Panzarino:** I think I, let me look, because we have internal versions of these two that we looked at, and I think in our internal version, I'm almost positive, I'd have to look it up, but I believe that it is, it introduced some discussion in there about supplement risk, and it wrote like a whole section on supplement risk, and we alighted that, because we were like, please don't, this does not.

**Matthew Panzarino:** And I'm almost positive it was, like, there was two sections, like a risks and controversy section, and then a how recommendations have shifted over time for, you know, supplements recommendation, which also included a lot of the comparisons of risk, and I think that those we alighted, because it's like, oh, obviously we don't want these in here, but it's clear that something in the pipeline is not, it's not enforcing that rule enough.

**Matthew Panzarino:** So, let me look at that, we need to double down on that.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Yeah.

**Brian Magida:** Um, to the extent it's helpful, I was just going through my email, um, and this is not going to probably perfectly align with the article generation, but I just have a note from Liz that the articles are looking good on August 14th, um, and so maybe, like, call it, or maybe I was looking at a good place then.

**Brian Magida:** Yeah, don't know if that's, like, I do, like, try to find, like, these needles in a haystack, so it might be, like, something from an engineering perspective around, like, that time.

**Matthew Panzarino:** I would just take a...

**Matthew Panzarino:** Yeah, yeah, I won't, I won't go, like, snipe hunting, but I will use it as a window to look at, just to make sure, because it never hurts to check your preconceptions and make sure it's, like, oh, wow, we changed, you know, the researcher from this model to that model, or we changed the, the underlying drafting model, because we do change those things, um, and we try to keep a track of, of whether or not they're...

**Matthew Panzarino:** But let me check on it, and I will see, and I'll let you know if I come up with anything there, just to give you some insights.

**Matthew Panzarino:** But beyond that, let me work on getting this new pipeline shipped, and then let's work on our control articles here, these two.

**Matthew Panzarino:** And I'm going to try and get as close to a raw output out of the pipeline as possible, and then take a look at it myself, and then see where we're at.

**Matthew Panzarino:** Rather than doing any heavy post-processing, they can confuse the matter.

**Matthew Panzarino:** So let me take a look at it.

**Liz Zwillinger:** We'll see what we get.

**Brian Magida:** Okay.

**Matthew Panzarino:** I'll get back to you, Aiden.

**Liz Zwillinger:** And as you're, you know, going through this, if there's anything that, like, is, you need to just do, like, a quick check-in.

**Liz Zwillinger:** I mean, I don't think I'm on a Slack.

**Liz Zwillinger:** You can add me, maybe, Brian, or whatever.

**Liz Zwillinger:** But, like, you know, as you're building it, like, just keep me posted if you need something or want to, like, run something.

**Matthew Panzarino:** Yeah, yeah, sounds great.

**Matthew Panzarino:** Okay, feel free to jump in the Slack, or we can add you.

**Matthew Panzarino:** Whichever way works, and then, or whichever needs to happen, and I can share stuff async in there, you know, that you can skim at your perusal, or at your leisure, because, like, if it's something interesting, or a finding, or a gut check, I'll just throw it in there.

**Brian Magida:** I think this is, like, a technical thing.

**Brian Magida:** I think for some reason, it's hooked up to my consulting, like, I think my consulting email is the Slack, but.

**Brian Magida:** Yeah, okay.

**Brian Magida:** So, it might just actually, this could be a good opportunity, maybe just to, like, add my biologica, as well as, we could add Liz's, and then, I actually don't know how to do that.

**Matthew Panzarino:** Yeah, I'll have Alice take care of it.

**Liz Zwillinger:** It's all good.

**Liz Zwillinger:** We'll handle it on our side.

**Brian Magida:** It's less, you don't worry about.

**Liz Zwillinger:** Well, thank you.

**Matthew Panzarino:** Yeah, thank you, Liz.

**Matthew Panzarino:** No, no, I appreciate the feedback.

**Matthew Panzarino:** I want it.

**Matthew Panzarino:** It's a challenge.

**Matthew Panzarino:** We'll take it.

**Matthew Panzarino:** We'll figure it out.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** We do pretty complex engagements for some other folks, incredibly technical topics, etc.

**Matthew Panzarino:** We're delivering.

**Matthew Panzarino:** think some pretty good work, so I think it's just a matter of time before we get this, and hopefully it's less time rather than more.

**Matthew Panzarino:** So we'll lock in and figure it out for you.

**Liz Zwillinger:** Thank you.

**Matthew Panzarino:** Thank you.

**Brian Magida:** Thanks.

**Brian Magida:** Bye.
