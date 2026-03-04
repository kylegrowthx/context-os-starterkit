# CodeRabbit <> GrowthX - Weekly Sync

<metadata>
date: 2025-10-02
time: 19:30 UTC
duration: 45 minutes
organizer: Erik O'Brien
participants: Aida Knezevic, Amanda, Erik O'Brien
fathom_recording_id: 91540463
fathom_url: https://fathom.video/calls/428038104
share_url: https://fathom.video/share/pCNxVkQweoS-g2LrF1R9mCnTzxKEqs9W
source: fathom
enriched_on: 2026-03-02 12:00 UTC
</metadata>

---

## Summary

GrowthX and CodeRabbit aligned on a major content strategy pivot — CodeRabbit's CEO is prioritizing high-volume keywords (1000+ searches) across AI coding tools rather than focusing narrowly on code review content. Amanda flagged concerns about formulaic writing in GrowthX's guidelines and technical inaccuracies in examples, so Aida committed to updating guidelines to emphasize how to discuss adjacent tools and competitors with technical rigor. The team reviewed Atlas content pipeline workflows, clarified publishing processes (CodeRabbit handles final publication through Hashnode/Strapi), and agreed on next steps for content topic reviews and programming language prioritization.

---

## Context

CodeRabbit is a developer tool for AI-powered code review and an important product expansion for GrowthX beyond traditional B2B SaaS content work. This is a weekly execution sync during CodeRabbit's initial content engagement with GrowthX — Aida joined the account specifically as editorial account strategist and oversees content cluster development and artifact management through GrowthX's internal Atlas platform. Amanda from CodeRabbit is balancing multiple responsibilities (product marketing, team coordination, recent relocation) while shepherding content from conception through technical review and publication. The meeting occurs in week 2 of an 8-week engagement, after an initial kickoff where CodeRabbit's CEO provided strategic direction to focus SEO efforts on higher-volume keywords rather than the typical narrow approach to code-review-specific terms.

---

## Relevance

**To GrowthX Delivery:**
- Atlas platform is now in production use for technical content clients — workflow includes specialized agentic pipeline with multiple review cycles, fact-checking, and developer team input
- Technical accuracy requirements for code examples in articles require additional review steps beyond standard pipeline; GrowthX's implementation of technical QA is critical to client satisfaction
- Writing guidelines must now explicitly address adjacent tool/competitor evaluation methodologies, not just CodeRabbit positioning — impacts artifact templates and content generation instructions
- In-line image generation (code samples, diagrams) flagged as capability gap needing team follow-up with technical operations

**To GrowthX Business Development:**
- CodeRabbit CEO strategy (high-volume keyword targeting) contradicts GrowthX's initial artifact suggestions (many under 1000 search volume) — require recalibration of content cluster approach and client feedback loops
- Amanda is operating under significant personal/operational constraints (recent move, team coordination load) that may affect review velocity and decision-making speed — risk management opportunity
- Two-step review process (Amanda for editorial, topic-assigned technical reviewers) creates dependency on Amanda's availability and bottleneck risk if single-point-of-failure

**To CheckThat:**
- Scrunch integration flagged for AI visibility tracking using CodeRabbit audience personas — opportunity to demonstrate CheckThat's competitive monitoring capabilities and refine prompt methodology based on actual customer questions
- CodeRabbit audience research (sales feedback on top customer questions) identified as incomplete; could feed into AEO research and prompt design for long-term visibility tracking

---

## Overview

- CodeRabbit wants to focus on high-volume keywords (\>1000 searches) related to AI coding tools, not just AI code reviews
- GrowthX will update writing guidelines and content strategy based on CodeRabbit's feedback
- CodeRabbit will provide more specific guidance on preferred programming languages and topics to prioritize
- Publishing workflow and image creation process need further discussion and refinement

---

## Key Topics

### Content Strategy Alignment

  - CodeRabbit's CEO wants to target higher volume keywords beyond just AI code reviews
  - Focus on keywords with \>1000 monthly searches, with some exceptions for strategic languages/topics
  - GrowthX to adjust content ideas to align with this broader strategy
  - CodeRabbit to provide list of priority programming languages and topics

### Writing Guidelines and Content Quality

  - CodeRabbit flagged concerns about formulaic article starts and technical inaccuracies
  - GrowthX to update guidelines, focusing more on how to discuss adjacent tools/topics
  - Need for high technical accuracy and examples in content
  - GrowthX to implement additional technical review steps in content pipeline

### Content Publishing Workflow

  - CodeRabbit uses Hashnode as a headless CMS into Strapi
  - GrowthX can stage content, but final publishing will be done by CodeRabbit
  - Two-step review process: editorial (Amanda) and technical (assigned per topic)
  - Discussion needed on handling in-line images and meta images

### Performance Tracking

  - GrowthX to set up Looker and Scrunch dashboards for performance reporting
  - CodeRabbit to provide access to Google Search Console and GA4
  - Scrunch to be used for tracking AI visibility using audience-specific prompts

---

## Action Items

**Aida Knezevic (GrowthX)**
- Update writing guidelines. Remove CodeRabbit-specific examples. Add guidance for discussing other tools and competitive evaluation methodologies.
- Remove AI Coding Assistant cluster from content plan.
- Follow up with team on capability for in-line image generation in articles.
- Update content strategy. Focus on higher volume keywords (1000+ search volume). Prepare next batch of keyword ideas for review.

**Amanda (CodeRabbit)**
- Review remaining artifacts (excluding writing guidelines and audience personas). Provide feedback.
- Review and comment on suggested content topics in Airtable, explaining approvals and rejections. Prioritize topics with 1000+ monthly search volume.
- Provide list of prioritized programming languages for content focus (share languages where CodeRabbit has user strength and competitive advantage).

---

## Transcript
**Erik O'Brien:** Hello again.

**Erik O'Brien:** Here's Cross for this one.

**Aida Knezevic:** I saw, so there's a guy on Instagram who has like a parody account.

**Aida Knezevic:** It's called TechCEO.

**Aida Knezevic:** And I saw that CodeRabbit was doing some like ads with him, but like skits.

**Aida Knezevic:** They were pretty, he's pretty funny.

**Aida Knezevic:** You should check him out.

**Aida Knezevic:** He has like a twin brother who has a different parody account.

**Aida Knezevic:** And I think it's called European Rich Kid.

**Aida Knezevic:** And he plays, he pretends to be like this French guy who's like really wealthy, but his parents are wealthy.

**Aida Knezevic:** He's just like, you know, living off of their money.

**Aida Knezevic:** And he's just an annoying European.

**amanda:** Oh, hello.

**amanda:** Sorry.

**Aida Knezevic:** Hi, Amanda.

**amanda:** My microphone was off.

**Aida Knezevic:** How's it going?

**amanda:** Good, good.

**amanda:** Sorry.

**amanda:** Been slightly busy.

**amanda:** So my apologies for not getting back on some of the requests.

**Erik O'Brien:** No worries.

**Erik O'Brien:** I know moving is always a tax.

**amanda:** Yeah, we moved like an hour and a half away and we also moved a family member into my basement.

**amanda:** So it's just been a bit intense.

**amanda:** And we were there.

**amanda:** I was a month before I traveled three times for work.

**Erik O'Brien:** So it's just been.

**Erik O'Brien:** Oh, wow.

**amanda:** Yeah.

**Erik O'Brien:** So I'm very behind.

**amanda:** But luckily, catching up shouldn't be that.

**amanda:** But as soon as I actually have, you know, full week in the office.

**Erik O'Brien:** Right.

**amanda:** Yeah.

**Aida Knezevic:** No, no, I totally get it.

**Aida Knezevic:** And now we've been able to make progress.

**Aida Knezevic:** Yes.

**Aida Knezevic:** Like on the cluster development strategy.

**Aida Knezevic:** So we have plenty of time.

**Aida Knezevic:** I was just actually telling Erik, I saw that you were doing, CodeRabbit's doing paid ads with an Instagram creator called MyTechCEO.

**Aida Knezevic:** I don't know if you caught those, but I thought they were really funny.

**Aida Knezevic:** And I was like, oh, this is CodeRabbit.

**amanda:** It was really funny.

**amanda:** Oh, yeah.

**amanda:** I like the ones that we've done with them.

**amanda:** They're quite funny.

**Aida Knezevic:** Yeah, yeah, yeah.

**Aida Knezevic:** I was just telling Erik, he has to go check them out.

**amanda:** Yeah, yeah, yeah.

**amanda:** That guy is such a good actor.

**Aida Knezevic:** He is.

**Aida Knezevic:** And he has a twin brother who pretends to be like a rich European kid.

**Aida Knezevic:** They're like tag teaming the like annoying people spectrum.

**amanda:** That's funny.

**Aida Knezevic:** Yeah, yeah.

**Aida Knezevic:** All right.

**Aida Knezevic:** So yeah, just to do, I forgot to do a quick intro.

**Aida Knezevic:** I wasn't at your kickoff call.

**Aida Knezevic:** So I'm Ada.

**Aida Knezevic:** I'm an editorial account strategist.

**Aida Knezevic:** Strategist at GrowthX.

**Aida Knezevic:** I work with Erik and the team during the sprint process to set the clients up with a strategy, the content clusters, and initial content ideas.

**Aida Knezevic:** I also set up your Atlas workspace and just make sure that everything's in good shape during this eight-week process.

**Aida Knezevic:** I joined GrowthX in December.

**Aida Knezevic:** Before that, I was working at a content marketing agency called Animals.

**Aida Knezevic:** And then I went freelance.

**Aida Knezevic:** And I still do a lot of freelance writing and strategy development, but at a much smaller scale than before.

**Aida Knezevic:** So that's a little bit about my background, but I have a lot of just experience in B2B SaaS.

**Aida Knezevic:** And I'm excited to be working with you.

**Aida Knezevic:** I watched the kickoff call.

**Aida Knezevic:** You know, my understanding, you have a lot of experience and in content strategies.

**Aida Knezevic:** So today's meeting is going to be a little bit different than usual because...

**Aida Knezevic:** You've given us clear lanes to execute on and research, and I was just, you know, going to share that today, if you don't have any other questions in the meantime.

**amanda:** Yeah, I mean, so as I haven't had a chance, and I was trying to get everything done before the call, so I have looked through two of the documents, two of the artifacts, the writing guidelines, and then the audience personas, and I meant to have previously sent you our writing guidelines, but got lost in the move.

**amanda:** So I've sent those.

**amanda:** There's a few things that I did flag in the guidelines that you created, which is that, you know, you're giving a very specific way to start each article, and I think that will become very formulaic and bad.

**amanda:** So my suggestion is to, like,

**amanda:** Do more than that.

**amanda:** The other thing that I was a bit concerned about in reading the writing guidelines, and that's probably something we can address in this call or that you plan to, was that, you know, like we actually talked a lot more about, like we talked about the lane that you guys had being, you know, writing about these adjacent things to us that have like high volume.

**amanda:** And I don't, so, so what I was, what I was thinking would be more present in the writing guidelines would be like directed as about how to talk about them and not necessarily about how to talk about us because that wouldn't be a big part of, like absolutely we would be discussing CodeRabbit at some point.

**amanda:** But I think like a third, if not more of the writing guidelines is how to talk about us, where like the type of content that you guys would be working on would actually not necessarily be primarily focused on us.

**Aida Knezevic:** Okay, okay, got

**Aida Knezevic:** Yeah, we're going to be updating them tomorrow based on the writing guidelines that you shared with us.

**Aida Knezevic:** So we're just going to factor that in and just remove any CodeRabbit related examples and anything.

**amanda:** I mean, think it's good.

**amanda:** I think it's good.

**amanda:** Like, obviously, like, at some point when you're talking about CodeRabbit, I do think that some of the things that you're mentioning are good.

**amanda:** It's just, like, it's kind of, like, everywhere of how to talk about us.

**amanda:** And there's nothing about, like, when you're talking about other solutions, how do you address them?

**amanda:** What is the, right?

**amanda:** Like, what are you evaluating on them?

**amanda:** How technical do you get on each of them?

**amanda:** Like, those are types of things that I would want to see in writing guidelines, specifically for the type of content that you're working on.

**amanda:** And also, like, what's our attitude towards these other tools?

**amanda:** Do we have an opinion?

**amanda:** Do we not?

**amanda:** Kind of just, like, narrowing in on that kind of part of the writing guidelines.

**amanda:** We answer some of those questions, which is like, we want, you know, a fairly high, a fairly, we want a good technical, like if it's about coding tools, for example, we would want fairly technical evaluations with lots of examples of why one coding tool works for people and what kind of use cases they like.

**amanda:** It's well-suited to kind of stuff like that, like very helpful content, you know, some of that info, if you're, you know, writing it with an LLM, you could get via, by doing like deep research using Reddit to, as a place to get some dev opinions, but really trying to showcase like, showcase that.

**Aida Knezevic:** Yeah, I I think there's a it's just Yeah, Yeah,

**Aida Knezevic:** Some of this would go in the writing guidelines, when we're talking about different tools, and specifically for like comparison articles, not comparison articles for like your direct competitors or CodeRabbit, but just like other like AI coding tools, we set up a separate content generation pipeline that uses a different artifact, and we would have to build that, that would include information about these different tools, and we could, that's where we would, you know, explain how we want to talk about these tools, like what kind of information we want to highlight to use that as the source of truth.

**Aida Knezevic:** But yes, we do want to have all that, this that you mentioned in the writing guidelines, just to make sure that like the content is technical enough for the audience that we're writing for.

**amanda:** Yeah, and I think the only other thing is that...

**amanda:** There was one piece, so I do have one concern, which is that, and I've already flagged it in that document, I don't know if you've seen it yet, but the last sentence actually is kind of, it doesn't really make sense from a technical point of view.

**amanda:** So I'm just a bit concerned about, so who will be editing the articles after they're written?

**Aida Knezevic:** Okay, so the, the writing guidelines, they don't have a fact checker.

**Aida Knezevic:** Okay.

**Aida Knezevic:** So the writing guidelines, these are, like, these are not facts that are going to be fed into the pipeline, so when we are, so the, these are just kind of examples to guide LLMs in the tone and, like, sentence structure, not specific examples or, like, things to mention in the content.

**Aida Knezevic:** When we are creating content for you and for, like, technical clients.

**Aida Knezevic:** We have an agentic pipeline, which is a more advanced version of our standard article generation pipeline, which does extra layers of like technical and code reviews.

**Aida Knezevic:** We have two software developers on our team who can assist with that and just making sure that like the output is accurate and isn't making like assumptions or just saying things that are flat out wrong.

**amanda:** Yeah, yeah, because the last sentence, doesn't, like I've explained why it doesn't make sense from a technical point of view and is actually kind of a bit of, it's either, I don't even know what it's trying to say or what it's trying to group together or why it's trying to group them together and what meaningful thing it's trying to say about those things.

**amanda:** Because it's kind of like, it's collapsing different types of things into each other and suggesting that we're doing reviews in JIRA, which we wouldn't be.

**amanda:** Because Jira is not a code writing or reviewing platform.

**amanda:** It's an issues and project management platform.

**amanda:** So just, yeah, so it's so unclear exactly what this could be saying, but also it seems to be inaccurate.

**amanda:** And it just kind of was like, wow, this is like really inaccurate.

**Aida Knezevic:** So I just want to flag that stuff like that is a red flag for me.

**Aida Knezevic:** Yeah, yeah, thank you.

**Aida Knezevic:** No, no, we'll note that.

**Aida Knezevic:** But yeah, these are examples.

**Aida Knezevic:** They're not like fact checked.

**Aida Knezevic:** So we have a, the pipeline has like multiple steps to address that.

**Aida Knezevic:** But I will like share your concerns with the customer ops team and see what we can do to kind of like customize the pipeline to make sure that you're doing like as little editing as possible.

**amanda:** Well, like stuff like this would actually be significant editing.

**amanda:** So it's the type of content that's hard to switch to something else because it's, anyways, yeah.

**Aida Knezevic:** Yeah, yeah, of course.

**Aida Knezevic:** Yeah, we don't want to, you know, we want to like, the goal is like to get to a place where, you know, don't have to, you might like leave a couple of comments, but it shouldn't be like substantive, like feedback that requires like rewrites and things like that.

**amanda:** Cool.

**Aida Knezevic:** All right, awesome.

**Aida Knezevic:** Well, we'll be, I mean, we'll wait for you to review the rest of the docs that we sent over.

**amanda:** Yeah, yeah, I'll do that later offline.

**Aida Knezevic:** Yeah, sure, sure.

**Aida Knezevic:** In the meantime, I kind of wanted to share what we put together in terms of the content calendar.

**Aida Knezevic:** So I'm going to share my screen.

**Aida Knezevic:** Okay, so, yeah, in the last call, you kind of gave us pretty clear, like, lanes to pursue.

**Aida Knezevic:** I did put together, this really isn't a strategy.

**Aida Knezevic:** strategy as much as it is just like an execution plan, but it is a notion in case you want to take a look.

**Aida Knezevic:** I kind of like outline the content objectives, just to kind of recap and make sure we're on the same page.

**Aida Knezevic:** So yes, so your request was basically for growthx to focus on like roundup content.

**Aida Knezevic:** So like best AI coding tools for whatever use case and other types of like listicle.

**Aida Knezevic:** type content that's more commercial, like that's more not commercial in nature.

**Aida Knezevic:** And then we would also do direct comparisons of AI coding tools that aren't direct CodeRabbit competitors, so that don't specifically deal with code reviews.

**Aida Knezevic:** So two of the three clusters below focus on these types of content.

**Aida Knezevic:** The third one is aimed at more informational content related to AI encoding.

**Aida Knezevic:** But these topics are very like general, don't deal with code

**Aida Knezevic:** CodeReviews, so it's just there to help us capture like more higher volume searches, because a lot of these, the content in these two clusters, there is search volume there, but if we were to like do a couple of like more higher volume keywords, that would also be very helpful.

**Aida Knezevic:** And we would like to recapture search visibility from these competitors.

**amanda:** So this is, yeah, so this is the first cluster, the second one with just like.

**amanda:** Can you just scroll back out, just AI Coding Assistant is one that we're doing internally, so take that one off.

**Aida Knezevic:** Right, okay.

**Aida Knezevic:** Yeah, we'll can.

**amanda:** The other two are fine.

**Aida Knezevic:** Okay, okay, that's good.

**Aida Knezevic:** Yeah, I'll flag that also in the content calendar, so we're not doing it, okay.

**Aida Knezevic:** Okay, yeah, so the second one just focuses on comparisons, and then this one would be the third one, so like things about like agenda.

**amanda:** Scroll back up.

**amanda:** Take out.

**amanda:** Visual Studio versus, yeah, it's not relevant, it's a bit too, it's not an AI tool.

**Aida Knezevic:** Okay, so you just want to do AI tools and under versus content.

**amanda:** AI tools, also we could do linters.

**Aida Knezevic:** Okay.

**amanda:** We could do not comparisons or not best linters, but let me see, we had a list of, I have to find it.

**amanda:** And it's from like a year, like, no, I feel like it's a year ago.

**amanda:** It's from five months ago.

**amanda:** So let me get you some of the examples that our CEO had.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Thanks.

**Aida Knezevic:** Yeah, and then the third one would be around like keywords like agentic AI unit versus integration testing.

**Aida Knezevic:** I think we can go over like the example assignments that I have.

**Aida Knezevic:** think they'll give you like a better idea of what each cluster contains.

**Aida Knezevic:** So you should have access to this already.

**Aida Knezevic:** I shared it with your email.

**Aida Knezevic:** But you can also find the link in the agenda.

**Aida Knezevic:** So the way we discovered these keywords is we did a keyword gap analysis.

**Aida Knezevic:** I did one.

**Aida Knezevic:** I know that you already did a keyword gap analysis with your direct competitors.

**Aida Knezevic:** I did one, again, just because it's our process.

**Aida Knezevic:** And those are, sorry, let me just, yeah, so these URLs are grouped in external direct competitor.

**Aida Knezevic:** So that gives us like an idea of like, okay, what are the URLs that, you know, that are leading them to rank for keywords that you're not ranking for?

**Aida Knezevic:** It just gives us a better.

**amanda:** Yeah, so I need to, so I need to just flag something.

**amanda:** Okay.

**amanda:** So graphite, when you're doing a direct competitor analysis with them, you're going to get

**amanda:** A lot of false positives around SEO, and the reason why is that Graphite competes with us on code reviews, but they aren't primarily a code review tool.

**amanda:** They're actually a stacked PR tool.

**amanda:** So if you look at some of the things they rank for, go back to that, what are NITs and what is a merge queue?

**amanda:** So that's actually SEO that they've done for their stacked PR tool, which we don't compete with in any way, and would not be relevant even if we're writing anything about things external to us.

**amanda:** Even like stuff like almost everything here would be irrelevant, if that makes sense.

**Aida Knezevic:** Yeah, yeah.

**Aida Knezevic:** And we did not consider any of these URLs for the topic clusters.

**amanda:** Yeah.

**amanda:** I just want to flag that most of their content is around their stacked PR product.

**Aida Knezevic:** All right.

**Aida Knezevic:** Got it.

**Aida Knezevic:** Thanks.

**Aida Knezevic:** So yeah, we just like pulled these.

**Aida Knezevic:** It's the process.

**Aida Knezevic:** you're just like...

**Aida Knezevic:** Okay.

**Aida Knezevic:** Thank

**Aida Knezevic:** But I did, like, I went in and I did a keyword gap analysis with three AI coding tools that you can find here.

**Aida Knezevic:** They just, I mean, the requirement was mostly, like, the content that they have on their website.

**Aida Knezevic:** There are AI coding tools that just don't have a lot of SEO content on their site.

**Aida Knezevic:** So it's just not helpful for us to do a keyword gap analysis there.

**Aida Knezevic:** But these URLs can be found in this tab.

**Aida Knezevic:** So the assignments, you can find them here in the client view.

**Aida Knezevic:** If you want to just take a look at, like, what topics we're suggesting, you can just go to topics for approval.

**Aida Knezevic:** And I selected 34 assignments for you to review in the beginning.

**Aida Knezevic:** Don't want to, like, give you too much at once.

**Aida Knezevic:** So these are, I think we can, like, even go through them, like, right away.

**Aida Knezevic:** So you have an idea of, like, where...

**Aida Knezevic:** We went initially and, you know, let us know if we're on the right track.

**amanda:** Yeah, I mean, so the, so, so I'm not sure if this was covered in the kickoff call.

**amanda:** It is just about the VS Code stuff.

**amanda:** So our VS Code integration isn't actually, it's like, we don't, like, it's, it's, it's like a, you know, a supermarket where you have a lost leader, right?

**amanda:** You offer something for a very low price and the goal is to get them to come in and use your, and buy other things.

**amanda:** So basically, we don't want to spend too much time advertising the, our VS Code stuff, if that makes sense.

**Aida Knezevic:** Okay.

**amanda:** So some of these still work, like Windsor versus Cursor, that makes sense for us to do.

**amanda:** CloudAI versus ChatGPT, I just don't think you should do that because we're now doing those with each model release, right?

**amanda:** So we're actually, we're now like not necessarily comparing them, but we're doing stuff and it's a very high, like our director of AI is writing them.

**amanda:** So I think there would just be a huge quality gap between what they're doing, where they're doing like benchmarks and, you know, you guys working on it.

**amanda:** And I just think that it would, it's better just to avoid that.

**amanda:** But let me look at some of these other ones.

**amanda:** Um.

**amanda:** Yeah, I think things like best free AI coding agents are good.

**amanda:** People are always looking for that, even though there's not often anything great.

**Aida Knezevic:** Okay.

**amanda:** I think I need to look into some of these a bit more before approving it.

**Aida Knezevic:** Sure.

**Aida Knezevic:** I'll just drop a link in the chat as well.

**Aida Knezevic:** All right.

**Aida Knezevic:** Okay.

**Aida Knezevic:** And then, yeah, the more informational stuff is here as well.

**Aida Knezevic:** This is kind of, yeah, you can leave comments here.

**Aida Knezevic:** Just if there's something that's like very off, you know, just let us know why and especially where to focus.

**Aida Knezevic:** We would really appreciate that.

**amanda:** Awesome.

**amanda:** I can do that.

**Aida Knezevic:** That's great.

**Aida Knezevic:** All right.

**Aida Knezevic:** Perfect.

**Aida Knezevic:** So I can also, yeah, so the next step sort of beyond just you looking at like the artifacts and us updating them and also like looking at the assignments.

**Aida Knezevic:** So our goal is to set up a Looker dashboard for you and a Scrunch dashboard for you.

**Aida Knezevic:** So that's why we asked for access to Google Search Console in GA4.

**Aida Knezevic:** So we used it for performance reporting and also your CMS.

**amanda:** I don't know if you've talked about this, but I was curious which CMS you're using.

**amanda:** So we actually use, we don't like it.

**amanda:** We want to switch off, but we actually use Hashnode as a headless CMS into our website CMS, which is Strapi.

**amanda:** So to use our blog, you have to log into Hashnode and you work on it from there.

**amanda:** And Hashnode is a developer focus.

**amanda:** It's headless CMS slash website where you can publish stuff yourself.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Okay.

**Aida Knezevic:** That makes sense.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** We typically need, this has been kind of coming up recently.

**Aida Knezevic:** We typically need access to like a team Gmail account.

**Aida Knezevic:** So just wanted to flag that ahead of time in case like, you know, you might have some questions around like who's going to have access to the account or anything like that.

**amanda:** Yeah.

**amanda:** I mean, I don't have an issue with that.

**amanda:** It was mostly just like, I, I just want to make sure that nothing gets published without us signing off on it.

**amanda:** Um, and, and then the question is like, so another thing that we do is we try to include a lot of images, um, in our content.

**amanda:** We also have very specific specs for like meta images.

**amanda:** So how does that work if you're publishing it?

**amanda:** Do you guys create those in our style or how does that, what's the, yeah.

**Aida Knezevic:** So, all right.

**Aida Knezevic:** So what.

**Aida Knezevic:** We do right now, what we can support right now, is generating featured images for blogs.

**Aida Knezevic:** So, like, let me share my screen again.

**Aida Knezevic:** So what I'm seeing on your blog is, yeah, you're just a lot of, like, using graphics, text, some images.

**Aida Knezevic:** So we have in-house designers who can take your visual, like, branding guidelines, if you have a Figma file or a Google Drive folder, and they can set up an image generation pipeline at the end of the article generation workflow that would generate an image.

**Aida Knezevic:** When it comes to in-line images, this is a capability that we're developing.

**Aida Knezevic:** I think, Erik, we're going to have to check and see, like, if we can provide this at this time.

**Erik O'Brien:** Yeah, I've got an actual another request out to Katia to see where we're at with that.

**amanda:** Oh, I mean, inn í.

**Aida Knezevic:** By inline, you mean inside the blog?

**amanda:** Yeah.

**amanda:** Yeah, so in which case, like, I think the one, like, I don't mind people uploading things into a blog for me because, and getting it ready.

**amanda:** But yeah, in that case, we might just generate, get images created ourselves and add them and then send it live, which could be one workflow.

**amanda:** Okay.

**Aida Knezevic:** If you can't do, like, in-article images.

**Aida Knezevic:** Okay, yeah, yeah, we'll follow up on that.

**Aida Knezevic:** But, yeah, I mean, when it comes to publishing some, yeah, we can definitely just stage the content.

**Aida Knezevic:** Like, after, so the review process works like this.

**Aida Knezevic:** So we will generate a first draft.

**Aida Knezevic:** We will send you an Airtable notification with, you know, it's just going to be, have, like, a Google Doc link.

**Aida Knezevic:** And then you'll review it, leave comments, we'll implement them.

**Aida Knezevic:** And then based on, like, you could just tell us, like, okay, just, you know, implement the feedback and then stage it.

**Aida Knezevic:** Or if you want to take another look, we can do that.

**Aida Knezevic:** And then we can.

**Aida Knezevic:** Just stage the content and then you can publish it.

**amanda:** So if that works better for you, we can do that.

**amanda:** Yeah, I mean, so depending on the nature of the content, might require two reviewers on our end.

**amanda:** So myself would be the, you know, editorial and style review.

**amanda:** And then depending on how technical it is, we'd have a technical reviewer as well.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Yeah, that's totally fine.

**Aida Knezevic:** And if you want, like, once we get to that point, you can provide their email and we can set up an automation with them as well.

**amanda:** Yeah, I mean, it depends.

**amanda:** It might depend on the topic, who it is.

**amanda:** But, yeah, maybe there's a way to assign a reviewer for each of them because I don't want anyone to be doing all of them.

**amanda:** Okay, yeah, that makes sense.

**amanda:** a couple of reviewers and assign them to different ones.

**Aida Knezevic:** Yeah, yeah, that works too.

**Aida Knezevic:** That's totally fine.

**Aida Knezevic:** All right, I don't think, yeah, and when it comes to Scrunch setup, so the way we use Scrunch is we will generate, we will like use your audience personas, like the artifact, to generate a list of prompts that these personas would ask LLMs, and we use them to track your AI visibility and the visibility of your competitors.

**Aida Knezevic:** What we can do is if you have any insights from sales or product about what are the most frequent questions that come up from your audience about CodeRabbit, we could use them to generate like better prompts that are coming from your actual audience versus us just trying to, you know, assume, okay, this is what your audience would ask with the help of AI.

**amanda:** could use see.

**amanda:** Yeah, I will, I will see, like we don't have a list of that, definitely.

**amanda:** So if there's anything, if there's like a top five that I can think of, then I will share.

**amanda:** It's one of the things that we were just talking today in a product marketing meeting about needing to meet with sales and get greater clarity on.

**amanda:** So it's not, I don't actually know 100% what are the stuff that is coming up most often.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Yeah, that's, that's totally fine.

**Aida Knezevic:** I just wanted to kind of flag that for you.

**Aida Knezevic:** And then before, I mean, we have 15 minutes.

**Aida Knezevic:** I did want to walk you through Atlas, but really quickly, just to go back to the content OS, because I did realize that I forgot something very important.

**Aida Knezevic:** And so we, the keywords that you're going to find here are the keywords that are competing.

**Aida Knezevic:** URL is ranking for, so like for example, like Builder.io, for example, like they're ranking for all of these keywords, and the total volume is based on all of the volume of these keywords that a single URL is ranking for, so I just wanted to flag that in case you got, get like confused as you're reviewing it, and then this is like the average keyword difficulty in it, like we use this system to filter, filter the content.

**amanda:** Okay, and how do I get, how do I get to these pages?

**Aida Knezevic:** What do you mean?

**amanda:** How do I get to the page that you're showing me?

**amanda:** Okay, so I can send you a link.

**amanda:** Oh, I don't think I'm in Airtable, that's why.

**amanda:** I don't think I've, I'm in Notion right now.

**Aida Knezevic:** Oh, right, okay, let me resend it.

**amanda:** That's why.

**amanda:** Okay, yeah, I do see it from earlier today.

**amanda:** Okay, sorry.

**amanda:** Or.

**amanda:** we

**amanda:** Whenever you sent it.

**Aida Knezevic:** Yeah, just sent it again in the chat.

**Aida Knezevic:** Like, it keeps, Zoom keeps, like, on to growthx notetaker.

**Aida Knezevic:** So I'm, like, DMing the notetaker without realizing it.

**Aida Knezevic:** Like, I'm, like, instead of, like, messaging the chat, I don't know why that is the default option.

**Aida Knezevic:** So weird.

**amanda:** Let's see.

**amanda:** I'm just signing up for Airtable.

**Aida Knezevic:** We don't use it here, so I don't have it.

**Aida Knezevic:** Oh, okay.

**amanda:** Yeah, because I was, like, how do, what are you showing me, and how do I review this?

**Aida Knezevic:** I'm glad I asked.

**amanda:** Sorry.

**amanda:** I also, to be honest, in my role, I don't get very many emails other than, like, people who are trying to, like, emails.

**amanda:** So I very rarely check my emails.

**amanda:** I check them, like, once a day.

**Aida Knezevic:** Yeah, okay.

**amanda:** So, so...

**amanda:** Usually at some time in the middle of the day or at the end of the day because it's unlikely.

**amanda:** Like other than that, what you sent me, I have like 12 emails that are all just spam.

**amanda:** Okay.

**amanda:** Okay.

**amanda:** Go ahead.

**Aida Knezevic:** Sorry.

**Aida Knezevic:** No, no.

**Aida Knezevic:** So yeah, that's just what I wanted to show you.

**Aida Knezevic:** So you have like a client view here and this is basically what, these are like the views that are most interesting to you.

**Aida Knezevic:** Um, so yeah, the, the different columns, um, you have like all the keywords here that a URL is ranking for that we used to generate a content idea.

**Aida Knezevic:** And then, um, you have like the total volume of the keywords that, that URL is ranking for and the average keyword difficulty.

**Aida Knezevic:** Um, so that kind of gives us a better idea of like how much traffic you could capture rather than just like giving you one keyword.

**Aida Knezevic:** So it's like, for example, like, um, the.

**Aida Knezevic:** This cluster for the best and alternatives roundups content, like the total volume of all of these URLs is close to 20,000 per month.

**Aida Knezevic:** In the versus content, it's close to 9,000.

**Aida Knezevic:** So it's a lot higher than if we were just like to provide like a single target keyword.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Great.

**Aida Knezevic:** So I did want to show you your Atlas workspace.

**Aida Knezevic:** Um, like I meant, said, we are working to set up, um, a different type of pipeline for you because this is technical content.

**Aida Knezevic:** Um, but I think it would be helpful just to show you, um, where the artifacts live, um, and why we need them.

**Aida Knezevic:** So, um, we, this is like your, your, your Atlas workspace, um, and Atlas is our in-house content generation platform that we built around and launched around four months ago.

**Aida Knezevic:** Um, it's just, you know, used by us.

**Aida Knezevic:** Um, All right.

**Aida Knezevic:** And we have your context artifacts here.

**amanda:** Did I get an invite to that as well?

**Aida Knezevic:** This is just accessible to growthx employees.

**amanda:** Oh, okay.

**amanda:** Okay, good.

**Aida Knezevic:** Yeah, yeah.

**Aida Knezevic:** So, yeah, we have, like, your company context here.

**Aida Knezevic:** And this directly, like, impacts the output as well as the audience personas and the writing guidelines.

**Aida Knezevic:** We can also add, like, information about your products and services here.

**Aida Knezevic:** The company research is more there to support, like, the company context and the audience personas.

**Aida Knezevic:** And then if I go to the pipelines, so there are two that are set up right now.

**Aida Knezevic:** The assignments one is just to help us generate different topic ideas, like different blog ideas for you.

**Aida Knezevic:** So it's not that interesting.

**Aida Knezevic:** It's pretty simple.

**Aida Knezevic:** But this is the, like, article generation pipeline.

**Aida Knezevic:** That's the baseline pipeline that everyone

**Aida Knezevic:** Everybody that starts out with growthx works with, the agentic one is different, it has more steps, and it has like multiple review, like more review cycles than the standard one.

**Aida Knezevic:** This one is more tailored for non-technical content, but it does start with, they do start similarly, so the first input is either a keyword or a title, and then from then, then from there, the workflow generates like an assignment brief, so this is connected, I did pick this one, which knowing what I know now is probably not a good choice, but it was just like a random pick, so I can have something to show you, so this, the assignment brief, it uses a SEMrush API to analyze the target keyword, so for example, if you have like ChatGPT versus Claude for coding, like it returns all of this data,

**Aida Knezevic:** It returns like the top ranking content and like all the other related keywords that the content should mention and for the first step, it does generate a proposed content structure and we edit this very, very heavily, but we also when we are just inputting the assignment, we will also provide a very detailed assignment direction.

**Aida Knezevic:** So at this point, we might already have an idea for the outline and like the points that we want to make.

**Aida Knezevic:** So we will plug that in here and the assignment brief is going to reflect that.

**Aida Knezevic:** So because I didn't do this as the first step, the assignment brief right now is pretty like, you know, pretty general, not doesn't have like a very unique angle.

**Aida Knezevic:** So we will typically like go in and edit this, provide like additional bullet points, remove sections, things like that.

**Aida Knezevic:** And then when this step is done, then we run the research step.

**Aida Knezevic:** Which takes all the information in the brief and then uses AI to research the brief in detail.

**Aida Knezevic:** So it asks questions about different parts of the brief and it returns information from the internet that covers different parts of the brief so that we have enough information to actually generate an article that's in-depth.

**Aida Knezevic:** From there, we review and edit the outline.

**Aida Knezevic:** We do a lot of editing here so we might remove certain sections, add sections, especially if we want to reference any particular stats or pieces of research.

**Aida Knezevic:** And then when we're happy with the outline, we'll generate the draft.

**Aida Knezevic:** The better the outline, the easier it is to edit the draft.

**Aida Knezevic:** And we will edit this in Atlas.

**Aida Knezevic:** We run the fact checker and then we also run the internal list.

**Aida Knezevic:** Link workflow, just to add internal links to the content, just to save us some time.

**Aida Knezevic:** And then we will do one final edit.

**Aida Knezevic:** Actually, do the edit after the fact checker.

**Aida Knezevic:** And then we do one final edit after the internal links to make sure that the links make sense and are, you know, not leading to, like, four or fours.

**Aida Knezevic:** And then we will upload this to Google Docs and share it with you.

**Aida Knezevic:** So, yeah, that's kind of the process from beginning to end for the standard article generation pipeline.

**amanda:** Cool.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Do you have any other questions, anything that, like, you wanted to discuss today that I didn't bring up?

**amanda:** No.

**amanda:** No, not that I can think of things.

**Aida Knezevic:** Okay.

**Aida Knezevic:** All right.

**Aida Knezevic:** Well, yeah, thank you so much for your time.

**Aida Knezevic:** I'll follow up in Slack with the link.

**Aida Knezevic:** To all of the resources that I shared today, we'll be on the lookout for your feedback, and then, yeah, we can take it from there.

**amanda:** Yeah, yeah, I'll finish giving feedback on the, what was I working on?

**amanda:** was working on company context, and then I will start going through some of those things.

**amanda:** The one thing that I'm looking at is that there's some that are very, so like part of what I was saying about going for adjacent keywords was that some of them have very high search volumes, and there's some like suggested articles that have under 100 that you've suggested.

**amanda:** So like that's a mismatch between the strategy that, you know, I asked you guys to follow.

**amanda:** So why is that?

**amanda:** Is there a reason why you're presenting those?

**Aida Knezevic:** Can I understand?

**Aida Knezevic:** Yeah, sure.

**Aida Knezevic:** Let me go back to the content strategy.

**Aida Knezevic:** So we do want like the, since the primary like objective.

**Aida Knezevic:** With content overall is to support trial signups.

**Aida Knezevic:** There are some suggestions in there that are more like more niche and would more specifically like target like very specific parts of your audience that might be more likely to convert to trial signups.

**Aida Knezevic:** If you want us to completely remove those assignments, that's totally fine.

**Aida Knezevic:** But I thought it wouldn't hurt to flag them at the very least.

**amanda:** Yeah, I think I'm going to, because I think, so basically the reason why I'm asking you to go in is I have to give you this context.

**amanda:** The reason why I asked you to have this like kind of lane is because our CEO who was like, okay, his strategy, and it's been successful for him in the past, is to go after much higher volume keywords, not necessarily like, so AI code review, it's a growing in how many people are searching in a month.

**amanda:** But all AI code review, you know.

**amanda:** uh.

**amanda:** So,

**amanda:** Keywords are going to be much smaller than a number of other keywords that might be related to AI coding tools or linters or something like that.

**amanda:** And so his strategy is don't go for the smaller pieces of the pie, just focusing on AI code reviews for an SEO perspective, but go after some of these larger volume keywords.

**amanda:** So probably, unfortunately, I'm going to reject most of what you've suggested, just because it doesn't follow that.

**amanda:** Because what I'm going to be doing internally here is presenting this as doing what this EO asked, which was to go after these things.

**amanda:** So some of them absolutely work, like Windsurf versus Cursor, that's 6,000 searches.

**amanda:** But anything under 1,000 searches would be something that I would just outright reject.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** that makes sense.

**Aida Knezevic:** So you want very, very, like, top of the funnel or high volume.

**Aida Knezevic:** Okay.

**amanda:** Yeah, I mean, I think some of them that I'll look closer, like, before rejecting any of them, you know, completely, I'll look closer because there might be some that it does make sense, right?

**amanda:** I might agree with you that it does make sense to do.

**amanda:** But essentially, like, that's kind of the strategy that he wants us to take with SEO.

**amanda:** And I told him I would work on doing that.

**amanda:** So, but we've prioritized doing, like, with our other resources, working on AI code review keywords from the perspective of, like, offensive and defensive reasons, that those are a priority to do and do well.

**amanda:** So, so, so, yeah, so, so one thing we want to use, you know, growthx for is being able to, to, to do the thing, do it.

**amanda:** He asked us to do, right, which is follow a strategy that's been successful for him in the past.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Okay.

**Aida Knezevic:** That makes sense.

**Aida Knezevic:** So, yeah, that's helpful context.

**Aida Knezevic:** So, yeah, we're going to just focus then on, like, the anything that's, like, over a thousand in combined search volume, we can do that.

**Aida Knezevic:** But let me know if, like, if there's a, like, I would be very interested to hear from you.

**Aida Knezevic:** Like, you can just leave, like, a quick comment in Airtable, like, why, like, you approved a specific topic.

**Aida Knezevic:** And then if you can think of anything that's, like, related, feel free to, like, make suggestions and we can just take it from there.

**Aida Knezevic:** Like, I would just like to just get into, like, sounds weird, but get into your head as much as possible, like, how you're thinking about this so that we can, like, the next batch of assignments can be, like, very close to what your CEO wants us to do.

**amanda:** Yeah.

**amanda:** Yeah.

**amanda:** And there's some that I might, like, I'm just looking, like, you have best.

**amanda:** So, one thing he also said at a different time, he likes to have, like, the best.

**amanda:** You have something about best React charting libraries in 2025.

**amanda:** He wasn't that specific, but he did say like best React libraries in 2025 with something or best JavaScript libraries.

**amanda:** And there's also like, I'm going to double check and I'll get you this info because I think it will be helpful.

**amanda:** But there are certain types of languages that we're better at and that more people who use us use.

**amanda:** So you're going after those types of language specific stuff, which is definitely something that we want to do.

**amanda:** Definitely something that he's flagged as important.

**amanda:** I might just, I might get you that information of what languages are probably ones to prioritize.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Yeah.

**amanda:** We'd love to have that.

**amanda:** Yeah.

**amanda:** Because in that case, like those ones would make a lot of sense for us to do, even if they're lower volume, just because of their, because we have data that one, we're particularly good for that language or two, you know, people who use.

**amanda:** That language are particularly likely to use our product.

**Aida Knezevic:** Okay.

**Aida Knezevic:** All right.

**Aida Knezevic:** Well, thank you for your time.

**Aida Knezevic:** Yeah, we'll be just waiting for your comments, and then we can do, like, this is, I mean, already, like, the context that you've given is helpful for the next round of keyword research.

**Aida Knezevic:** I already have a better idea of, you know, what kind of topic ideas you want to see.

**Aida Knezevic:** So, yeah, I'll let you know when we have a next batch for you to review.

**amanda:** Awesome.

**amanda:** Okay.

**amanda:** I will go through, and, like, I'm not going to outright reject everything under 1,000, but, like, if it does make sense, then we'll go forward with it.

**amanda:** But I am going to, I'll have a look at these and get you something, if not today, then tomorrow.

**amanda:** Okay.

**amanda:** I'll start today, but I might not be able to, and I'll try to explain why for each of them.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Amazing.

**amanda:** Thank you.

**amanda:** Awesome.

**amanda:** Thanks.

**Aida Knezevic:** All right.

**Aida Knezevic:** See you next week.

**amanda:** Bye.

**Erik O'Brien:** Bye.

**Erik O'Brien:** Bye.

**Erik O'Brien:** Bye.
