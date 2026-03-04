# Content Audit: Vivek and Ismail

<metadata>
date: 2025-05-27
time: 14:27 UTC
duration: 29 minutes
organizer: matthew@growthx.ai
participants: Matthew Panzarino, Vivek Shankar, Ismail Ajagbe
fathom_recording_id: 64816253
fathom_url: https://fathom.video/calls/310484617
share_url: https://fathom.video/share/bTh4AsxxUaELat3U7r1mxKhC2zzaJxE4
source: fathom
enriched_on: 2026-03-04 15:30 UTC
</metadata>

---

## Summary

Matthew Panzarino shared findings from auditing 40 recent articles: only 30% met high standards, with key issues including overuse of colons in titles, repetitive outline-like structures lacking narrative flow, and inconsistent client-specific customization. The team discussed a new onboarding approach where sprint teams will handle new clients in their first few weeks with detailed per-client writing instructions, and aligned on creating a dedicated channel for the delivery team to report workflow breakages so the engineering team can respond quickly with rollbacks when necessary.

---

## Context

Matthew Panzarino held this audit meeting with Vivek Shankar and Ismail Ajagbe, both content strategists on the GrowthX delivery team, to address recurring content quality issues in the article generation workflow. Matthew had recently joined the organization to oversee delivery operations and quality improvement—a role distinct from running the editorial team day-to-day. The meeting served as a deep-dive on content standards: Matthew had personally sampled 40 recent articles and identified systemic patterns that were holding back quality, while Vivek and Ismail raised critical concerns about the engineering team's opacity and the lack of communication channels between delivery and the platform development team. The broader context: GrowthX is racing toward a June 10 deadline to migrate off the Aerofs platform while simultaneously scaling content delivery to multiple clients (AIMBIT, Rpod, DataGrid, Relay, and others), meaning engineering bandwidth is stretched and workflow reliability has degraded, forcing delivery teams to fall back on manual work and external LLMs to meet commitments.

---

## Relevance

**To GrowthX Delivery:**
- Content quality baseline is 30% acceptable; writing style patterns (colon abuse, outline-like structures, repetitive CTAs) are systemic and addressable via better polishing prompts and client-specific instructions
- New client onboarding will use dedicated sprint teams for first weeks to establish detailed per-client writing standards (e.g., Dave Gaelic's AIMBIT writing guide), reducing manual remediation downstream
- Shifting from outline-to-prose conversion (2-5 sentence paragraphs) is proven to improve narrative flow; deliverable teams now have a playbook for remediating articles already in production

**To GrowthX Engineering / Product:**
- Workflow breakage (e.g., Rpod article generation collapse ~1 month ago) has no early-warning system; delivery team feedback disappears into EPD request channel with no visibility on root cause or rollback strategy
- Lack of testing environment (sandbox/pre-prod) means changes deployed to production hit 20+ client workflows simultaneously; engineering should implement controlled deployment with ME sign-off and rapid rollback capability
- Opacity in workflow functionality is blocking adoption of advanced features like assignment workflow; engineering should publish changelogs and gather requirements monthly (Matthew now scheduling this)

**To GrowthX Business Development:**
- AIMBIT nearly churned at calibration due to quality delta expectations; the new sprint-team onboarding with detailed writing standards directly reduces early-stage churn risk on new engagements
- Rpod and DataGrid experiencing workflow reliability issues (image generation failing daily, article gen broken) that require fast remediation to protect account retention

---

## Overview

- Content quality varies; \~30% meets high standards, but improvements needed in writing style, structure, and client-specific customization
- Workflow issues causing significant manual work; need better client-specific calibration and writing instructions
- Engineering team communication and deployment process needs improvement; lack of testing environment causing disruptions

---

## Key Topics

### Content Quality Assessment

  - \~30% of sampled articles meet high standards; others need improvement
  - Key issues: overuse of colons in titles, repetitive structures, lack of narrative flow
  - Recommendations:
      - Avoid "X: Y" title format unless absolutely necessary
      - Transform outline-like content into 2-5 sentence paragraphs
      - Vary content structure to avoid repetitive patterns

### Client-Specific Calibration

  - New process: Sprint team handles initial weeks for new clients
  - Detailed writing instructions document created for each client (e.g., AIMBIT)
  - Instructions include client preferences, technical details, and audience considerations
  - Goal: Improve initial output quality and reduce manual editing

### Workflow and Engineering Challenges

  - Recent workflow breakdowns, particularly for RPod and DataGrid clients
  - Lack of communication channel with engineering team
  - No testing environment; changes deployed directly to production
  - Opacity in workflow functionality and requirement gathering process

### Proposed Solutions

  - Create dedicated channel for reporting delivery team issues
  - Implement controlled sandbox/pre-prod environment for testing
  - Improve communication between delivery and engineering teams
  - Monthly meetings to collect and prioritize feedback for engineering

---

## Action Items

**Vivek Shankar (GrowthX)**
- Identify approx. date when article gen workflow broke for Rpod; find original/recent comment about issue; share info with Matthew

**Matthew Panzarino (GrowthX)**
- Create new channel for delivery team to report workflow breakages; ensure eng team can see/act on issues
- Collate feedback from delivery team on workflow issues; prioritize for eng team; drive updates/changes
- Schedule monthly meeting with engineering to gather requirements and discuss feature requests

---

## Transcript
**Matthew Panzarino:** After this, so we're going to vanish here.

**Matthew Panzarino:** Okay, we're just going to chat a little bit about this.

**Matthew Panzarino:** And I did, you know, I chose like one relatively recent, but just one article.

**Matthew Panzarino:** And this is not like, I want to preface this by saying this is not a task list for everything that you should always do or not do.

**Matthew Panzarino:** I just wanted to use this as an opportunity to kind of like hone a little bit and talk about philosophy and talk about how we need to push, you know, especially that the workflow output and push our content a little bit further.

**Matthew Panzarino:** I will also acknowledge right at the top that like, yes, we all know that the workflows are rough and that they need improvement.

**Matthew Panzarino:** And that we're doing a lot of manual work or work outside of the workflow.

**Matthew Panzarino:** Close in prompting engines.

**Matthew Panzarino:** And that's acknowledged, right?

**Matthew Panzarino:** And we'll get better at that.

**Matthew Panzarino:** That's part of what our delivery meeting is about later today.

**Matthew Panzarino:** It's just workflow improvement and better cycles on that.

**Matthew Panzarino:** There's also some improvements that we can do in the onboarding process for new clients.

**Matthew Panzarino:** I think that I have started to go through all of the calibration articles for each new client as we do onboarding.

**Matthew Panzarino:** And that's already been a really illuminating exercise, kind of getting those in better shape before we present them to the client.

**Matthew Panzarino:** We've had some clients offer literally based on calibration articles, which is not ideal, because they're just like, oh, the delta between what I expected to see and what I am seeing is too wide.

**Matthew Panzarino:** And, you know, for the delta, 20% or 15% or whatever, somewhere in that range, we'll get there, you know, and that's what calibration articles are about.

**Matthew Panzarino:** I do not expect us to deliver something perfect for the client at calibration, but it's clear that, like, we need...

**Matthew Panzarino:** Better expectations about what the first things that they see from us are to set expectations about what we can deliver.

**Matthew Panzarino:** Because if they think we're way off, they're going to be like, this is not worth my time, you know, especially young companies.

**Matthew Panzarino:** You know, they don't have patience for it.

**Matthew Panzarino:** They're like, oh, I've got a hundred other things on my plate.

**Matthew Panzarino:** I thought you guys were going to take this off my plate.

**Matthew Panzarino:** Now it looks like I'm going to have to do a lot of work.

**Matthew Panzarino:** So we'll get there.

**Matthew Panzarino:** But as a part of that calibration exercise, one of the things that has come out of it is it's very obvious that we need better writing instructions and better, like, per client's calibration instructions for our workflows.

**Matthew Panzarino:** So creating a specific workflow for a client should be much more than just copying and pasting our grids into their folder and then just starting to run them off of keywords.

**Matthew Panzarino:** It should really utilize a document that can house all of the feedback that they've given us during the calibration process, in addition to best practices.

**Matthew Panzarino:** But tuned for each client.

**Matthew Panzarino:** Giving our workflows a keyword and a company outline is not enough.

**Matthew Panzarino:** There really needs to be additional layers of polishing instructions.

**Matthew Panzarino:** So we're working towards that.

**Matthew Panzarino:** I think this will come out of the process that we're going to start creating for new clients.

**Matthew Panzarino:** The new client kickoff process is that a sprint team is going to handle that client for the first few weeks.

**Matthew Panzarino:** And either Marcel or Jason or myself or somebody else will be really in the mix with them doing a high-level calibration.

**Matthew Panzarino:** And then when it's handed off to teams, you already have an inflow process.

**Matthew Panzarino:** Okay, this is the expectation.

**Matthew Panzarino:** It's been calibrated.

**Matthew Panzarino:** We have workflows that are tailored to this client's actual desires, all of that stuff.

**Matthew Panzarino:** So I'm going to preface this with we're working on all that stuff.

**Matthew Panzarino:** And, of course, feedback from you and feedback from everybody is welcome and desired.

**Matthew Panzarino:** That's why we're having the meeting later today to try and get a type of loop between, hey, what do we hope workflows are delivering and what are they actually delivering?

**Matthew Panzarino:** I think that's a big deal.

**Matthew Panzarino:** So this piece that I had, I think this is the one.

**Matthew Panzarino:** This is the piece that I had chosen, just grabbed out of here, the misinformation vulnerabilities in LLM's piece.

**Matthew Panzarino:** I actually thought this was a great piece.

**Matthew Panzarino:** Please don't pay attention to how much I commented on it.

**Matthew Panzarino:** That's just me.

**Matthew Panzarino:** You know, I thought it was pretty solid.

**Matthew Panzarino:** I think it did a great job of covering the topic.

**Matthew Panzarino:** I think it was accurate.

**Matthew Panzarino:** It included the right mix of like statistics and grounding in technical language without getting too like jargon heavy.

**Matthew Panzarino:** So I think this struck a pretty good balance overall.

**Matthew Panzarino:** I was pretty happy with this.

**Matthew Panzarino:** I would say I was only pretty happy with about 30% of our overall content.

**Matthew Panzarino:** And by 30%, I mean, I took a sampling of 40 articles, right?

**Matthew Panzarino:** Recent articles.

**Matthew Panzarino:** And I was happy with about 30% of that.

**Matthew Panzarino:** The other chunk, I was like, oh, okay, this is all right.

**Matthew Panzarino:** And then there was a chunk that was like, I can't believe this is live, right?

**Matthew Panzarino:** You know, that's kind of where we are right now.

**Matthew Panzarino:** That's startups, right?

**Matthew Panzarino:** We'll get better.

**Matthew Panzarino:** But on this piece, I actually thought it was pretty good.

**Matthew Panzarino:** I thought, you know, it's clear that you guys did work to make sure that this was grounded in the reality of what they wanted.

**Matthew Panzarino:** I left a few comments here that were just more stylistic or really just, like, optional, you know?

**Matthew Panzarino:** And it's ways to think about this content that you could expand or could improve.

**Matthew Panzarino:** One of the big things right at the top that I'm trying to address with everybody is please, please, please, like, ditch the colon, you know, the blah, blah, blah, colon, blah, blah, blah structure whenever possible.

**Matthew Panzarino:** There are times, this is why I always hate, you know, or at least I personally hate it when, like, I'm having a conversation with somebody I'm trying to get a calibration on.

**Matthew Panzarino:** So you mean never do that?

**Matthew Panzarino:** And the answer is not really.

**Matthew Panzarino:** Like, if it really, really makes sense, like, if it is, like, the colon is, like, the only way to say this thing, okay, you know.

**Matthew Panzarino:** Go for it.

**Matthew Panzarino:** It's not like a hard, fast rule, but like literally 70% of the articles that I reviewed had this in the head, which is crazy.

**Matthew Panzarino:** Like that shouldn't be.

**Matthew Panzarino:** That's no, nothing in the English language should happen 70% of the time, you know, every time like that.

**Matthew Panzarino:** So I would say, you know, find another way to phrase it, you know, play around with that a little bit to help re-architect it.

**Matthew Panzarino:** In general, if there's a colon in it, there's another way to say it.

**Matthew Panzarino:** And maybe that's a connecting word and maybe it gets a little bit, cues a little bit away from keyword stuffing.

**Matthew Panzarino:** And instead you keyword stuff the meta title when we're publishing.

**Matthew Panzarino:** So create a separate meta title and keyword stuff the meta title and then write a human readable title.

**Matthew Panzarino:** Now I know there will also be client input on all of this stuff, right?

**Matthew Panzarino:** So if they are like, no, no, we really want this colonist.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** You know, clients always write to a degree.

**Matthew Panzarino:** We have to also then establish our bona fides and say, hey, we're the experts at this.

**Matthew Panzarino:** And we really feel like the human readable headline would be better here.

**Matthew Panzarino:** We're happy to do this if this is what you want.

**Matthew Panzarino:** But.

**Matthew Panzarino:** We want to give our two cents on this because that'll CYA us when it doesn't deliver and under-indexes or under-performs from a traffic perspective.

**Matthew Panzarino:** And you're like, hey, can we do a content refresh and see if more human-readable headlines will be better here?

**Matthew Panzarino:** Yada, yada, yada.

**Matthew Panzarino:** A few other things here were just, you know, this guide explores, that's like a pretty common LLM pattern.

**Matthew Panzarino:** And it showed up in a lot of our articles.

**Matthew Panzarino:** You know, this guide explores or this guide will, you know, blah, blah, blah.

**Matthew Panzarino:** There are other ways to talk about it.

**Matthew Panzarino:** This analysis is a really, like, cheap way to fix that problem.

**Matthew Panzarino:** But, you know, there are other ways to phrase it.

**Matthew Panzarino:** So keep an eye out for that.

**Matthew Panzarino:** This particular section here is okay.

**Matthew Panzarino:** But I did notice, just using this as an opportunity to talk about this thing, a lot, a lot of our workflows turn out, it seems, by default.

**Matthew Panzarino:** Single-sentence intro, H3s, single-sentence intros, bullets, single-sentence hours.

**Matthew Panzarino:** Outros, page 3s.

**Matthew Panzarino:** That's not an article that's an outline, right?

**Matthew Panzarino:** So we need to take those.

**Matthew Panzarino:** Anytime we see that pattern appear, it's almost always possible to just take that chunk and feed it back in either to the polishing step or to just an LLM right now before we have, you know, these workflows more improved and ask it, give me these, give me this section in two to five sentence paragraphs with more narrative, more narratively driven.

**Matthew Panzarino:** You can use, still use single sentence paragraphs, but only for emphasis and occasionally and see what it gets back.

**Matthew Panzarino:** I did that for a large, a large amount of these articles and I got back great stuff.

**Matthew Panzarino:** You know, it's pretty solid.

**Matthew Panzarino:** You know, it used all of the points, like the accurate bullet points and accurate lines that were there and just expanded them a bit.

**Matthew Panzarino:** If you say two to five, it gets enough room for it to expand it and create a more organic flow of thought without too much room for it to get florid, you know.

**Matthew Panzarino:** Be out beyond that, it starts to get really, you know, expansive, and you're like, it's talking to you like an academic, and you're like, all right, you know, LLM, please.

**Matthew Panzarino:** So keep an eye out for those patterns.

**Matthew Panzarino:** The list format, I think this had a numbered list format with these.

**Matthew Panzarino:** I also do not feel that numbered lists in H3s are almost ever a good idea, especially with case sentence, or excuse me, title case sentences.

**Matthew Panzarino:** So like this, where it would say like one, you know, like that.

**Matthew Panzarino:** It's almost never a good idea unless it actually is a sequence.

**Matthew Panzarino:** So if there is a sequence of things that is happening, it's like, hey, let's go through the steps you would do to do X, Y, Z.

**Matthew Panzarino:** Okay, cool.

**Matthew Panzarino:** One, two, three, right?

**Matthew Panzarino:** These are steps.

**Matthew Panzarino:** Or if it's a top 20 list, okay, numbering fine, that sounds good.

**Matthew Panzarino:** But other than that, stay away from the numbering thing.

**Matthew Panzarino:** I saw that crop up a lot in our articles, just like numbers where they really don't need to be numbers.

**Vivek Shankar:** Yeah, yeah, go ahead.

**Vivek Shankar:** Yeah, I just wanted to clarify that.

**Vivek Shankar:** So I can't speak for the others, but one of the reasons we add that, at least I do that a lot, is because of how the algorithm works in Google.

**Vivek Shankar:** It actually picks up those one, two, three lists.

**Vivek Shankar:** Agreed, we don't need to have numbers, but I usually have told the guys to have like bulleted H3s sometimes.

**Vivek Shankar:** Because Google kind of consolidates that in the snippet and now the AI overviews.

**Vivek Shankar:** So if somebody searches, for example, like causes, or whatever, it'll pick up those H3s as bullets and then just consolidate them in there.

**Vivek Shankar:** And I've noticed in the past that if it's not bulleted, it usually doesn't pick it up.

**Matthew Panzarino:** So it was more of an SEO thing, not really a writing thing.

**Matthew Panzarino:** You're talking about if it's not numbered?

**Vivek Shankar:** If it's not bulleted.

**Vivek Shankar:** So if the H3 is bulleted, it kind of, it picks it up as a list, right?

**Vivek Shankar:** So it will just use the H3 titles as a list, and it will show them in either what used to be the snippet, and now is the AI overview.

**Vivek Shankar:** But if it's not bulleted, if it's just like standalone H3s, for some reason, it doesn't, the algorithm doesn't pick up those H3s as a list.

**Vivek Shankar:** So it's just one of the quirks of the algorithm.

**Vivek Shankar:** So that's why we either have the numbers or the bullets in there in the H3s.

**Matthew Panzarino:** Interesting.

**Matthew Panzarino:** Yeah, I mean, it looks awful, right, from a human-reader perspective.

**Matthew Panzarino:** So let's figure out, okay, let me think about that.

**Matthew Panzarino:** I know there's, I mean, obviously, best practices are good.

**Matthew Panzarino:** You know, at the end of the day, most of our clients care about traffic and conversions more than they care about, you know, humans.

**Matthew Panzarino:** But we should care about humans because at the end of the day, that's the consumer of our product.

**Matthew Panzarino:** And so, like, the way that it, like.

**Matthew Panzarino:** The way that it displays and shows for a human can make the difference between, you know, us getting a new client or not, you know, or a current client being happy when one of their content team reviews it or not.

**Matthew Panzarino:** So let's think about a way to service that that does not look so bad.

**Matthew Panzarino:** But yeah, that's point taken.

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** And I appreciate you raising those because we'll integrate that into how we think about this.

**Matthew Panzarino:** But yeah, as I mentioned, like most of the, most of this piece was pretty good.

**Matthew Panzarino:** There, there was one thing here I noticed that this was a very repetitive structure.

**Matthew Panzarino:** So, you know, paragraph, prompt, blue, call out, paragraph, or paragraph, paragraph, blue, prompt, blue, out.

**Matthew Panzarino:** That was kind of a repetitive pattern throughout.

**Matthew Panzarino:** I wanted to flag that for two reasons.

**Matthew Panzarino:** One, obviously it's a repetitive pattern so that feels generated.

**Matthew Panzarino:** But the second thing is that I think a lot of our clients are going to differ dramatically.

**Matthew Panzarino:** Radically on whether or not they want or care about or what their sensibilities are for marketing, you know, in these pieces.

**Matthew Panzarino:** And whether CTAs at the end or woven throughout will largely depend on the client.

**Matthew Panzarino:** AIMBID, as an example, pushed back a lot.

**Matthew Panzarino:** We, you know, did integration and they were like, oh, man, it feels kind of market-y and we want this to be more informational.

**Matthew Panzarino:** Cool.

**Matthew Panzarino:** No problem.

**Matthew Panzarino:** Let's drop your CTA to the end and let's say, you know, we'll put a nice clean one.

**Matthew Panzarino:** It says, I'm sure you found this helpful.

**Matthew Panzarino:** Hopefully, if you need more help, we're here.

**Matthew Panzarino:** You know, that kind of thing.

**Matthew Panzarino:** Just a nice clean outro.

**Matthew Panzarino:** If FrontFu or any of our clients want it more integrated, this isn't a terrible way to do it.

**Matthew Panzarino:** Just be cautious about like the pattern repeating itself very, very, you know, exactly over and over and over and over and find different ways to integrate.

**Matthew Panzarino:** But overall, I thought it was pretty good.

**Matthew Panzarino:** You know, I didn't really find too many things to really complain about here.

**Matthew Panzarino:** thought the.

**Matthew Panzarino:** This is a pretty good piece.

**Matthew Panzarino:** yeah, that's about it.

**Matthew Panzarino:** And then on the other side of it, you know, the workflow side, we have a meeting later today talking about, you know, trying to get deliverables a little bit tighter loop with what we're actually building on the workflow side.

**Matthew Panzarino:** And I know, like a lot of people know here, that the workflows are just weaker than they should be, right?

**Matthew Panzarino:** They're not delivering the kind of 70th percentile, 80th percentile output that we can then edit and get into proper shape.

**Matthew Panzarino:** And everybody's having to fall back onto external engines and stuff a lot more than I think we want, than anybody wants.

**Matthew Panzarino:** And there's a combination of things happening there, most likely not enough polishing and writing instructions set up in the workflows.

**Matthew Panzarino:** In other words, the workflows are not customized enough for each client, which will happen, which we'll do, we'll start doing more as we onboard new clients.

**Matthew Panzarino:** They should all have custom workflows by the time you folks as...

**Matthew Panzarino:** Delivery team gets a hold of them and starts having to produce content over and over on them.

**Matthew Panzarino:** That's what the point of this whole sprint group is for onboarding new clients.

**Matthew Panzarino:** But then we'll take those learnings and then apply them to existing clients and say, okay, how can we customize the workflow for this client to include additional writing instructions and input?

**Matthew Panzarino:** As an example, like I just went through, so part of the new process that I'm doing with clients is I'm doing all the calibration articles, or not I'm doing them, the MEs are writing them or shepherding them.

**Matthew Panzarino:** And then myself and the director are editing them very thoroughly before the client sees them.

**Matthew Panzarino:** And then out of those edits, this is Dave Gaelic wrote this for AIMBIT.

**Matthew Panzarino:** And this is basically a writing instructions for writing about AIMBIT and collated out of their feedback to the calibration.

**Matthew Panzarino:** But also Jacob's and my edits to the piece and really detailed, like thorough overview of what AIMBit wants, what the philosophy is, what's missing in here.

**Matthew Panzarino:** I mean, down to very specific things.

**Matthew Panzarino:** One thing that they really cared about was AIMBit.

**Matthew Panzarino:** Sorry, it's very dense, but that's the whole point, right?

**Matthew Panzarino:** It's just like very detailed prompting instructions, basically saying, this is the way you write about this company.

**Matthew Panzarino:** Don't write different ways about this company.

**Matthew Panzarino:** Write this way about this company.

**Matthew Panzarino:** But there's, you know, obviously double checking technical details.

**Matthew Panzarino:** But one of the things they really want was like, you know, hey, we really view our solution as different from a standard KMS or key management system.

**Matthew Panzarino:** Please make sure that that's throughout, you know, everything we write about, the difference between us and the traditional secret list access.

**Matthew Panzarino:** not secret, the security, you know, these are hyper-specific to AIMBit's, you know, body of work.

**Matthew Panzarino:** What they do, and of course, to their audience.

**Matthew Panzarino:** So these kinds of instructions, frankly, should be written for every client.

**Matthew Panzarino:** Like every client should have a document like this that is fed into the prompts that the workflows utilize to make sure that the output is much closer to where we want to be.

**Matthew Panzarino:** And currently, I would guess that unless you, as a CMS male or as an ME, Vivek, or anybody else has just done this ad hoc, nobody has been told to do this, right?

**Matthew Panzarino:** And this is, I think, base stakes.

**Matthew Panzarino:** We need something as detailed as this for every client so that we can get a hell of a lot closer on that initial output and then be able to, like, use humans to get the rest of the way.

**Matthew Panzarino:** Right now, we're just doing a lot of manual lifting, so I know it can get a little woman.

**Matthew Panzarino:** So we'll figure it out.

**Matthew Panzarino:** We'll get better at it, and that whole process will get better.

**Matthew Panzarino:** And of course, you know, we'll continue to take feedback.

**Matthew Panzarino:** We want to know where these things are breaking and failing and falling down.

**Matthew Panzarino:** Cool.

**Matthew Panzarino:** So that's a bit for my side.

**Matthew Panzarino:** And then I have a couple of minutes.

**Matthew Panzarino:** Like, you know, what are your pain points?

**Matthew Panzarino:** What's breaking?

**Matthew Panzarino:** I know it's just a handful of minutes here, but we will have that meeting later today and more to talk about this.

**Matthew Panzarino:** But what are your pain points?

**Matthew Panzarino:** What's breaking for you on, like, article generation, that sort of thing?

**Matthew Panzarino:** How much are you still relying on external engines to manually write all this?

**Vivek Shankar:** I would guess a lot, you know, that kind of thing.

**Vivek Shankar:** I would say Rpod was a bit of an exception because we relied on the grid quite a lot until about a month ago when the article gen workflow completely broke.

**Vivek Shankar:** And it just started spitting out stuff that was, it wasn't the same level, right?

**Vivek Shankar:** So I think I would say that has been the most frustrating aspect so far.

**Vivek Shankar:** It seems like the dev team, and I raised this with Mara as well, it seems like the engineering team, it's just like a black box over there.

**Vivek Shankar:** Like,

**Vivek Shankar:** I'm kind of giving feedback.

**Vivek Shankar:** just goes in.

**Vivek Shankar:** Something comes out that makes no sense.

**Vivek Shankar:** Like they deployed a few fixes, I think, a couple of weeks ago, and then it just kind of broke everything.

**Vivek Shankar:** So it's been a little weird in that sense.

**Vivek Shankar:** Like before, like I've been here since December, obviously.

**Vivek Shankar:** So in the initial days, it was like we had an open line to Daniel, right?

**Vivek Shankar:** And Daniel was always actively soliciting feedback.

**Vivek Shankar:** And he was like, okay, tell me what better.

**Vivek Shankar:** And that's where literally the idea for the outline and the assignment flows came because it was something that we suggested to him.

**Vivek Shankar:** It's like we need more control over the output.

**Vivek Shankar:** So these are two ways of doing it.

**Vivek Shankar:** And he actioned that and he sort of got that going.

**Vivek Shankar:** And back then it was just him and Marcus.

**Vivek Shankar:** So it was nice having that sort of channel.

**Vivek Shankar:** Now it seems like it's not there anymore.

**Vivek Shankar:** Like even in the EPD request channel, we kind of post things.

**Vivek Shankar:** A fix happens and it's like...

**Vivek Shankar:** Okay, you know, and the next day it's broken again, right?

**Vivek Shankar:** Like, for example, with DataGrid, that's a very sort of programmatic sort of client.

**Vivek Shankar:** And, you know, we have freelancers running it, right?

**Vivek Shankar:** So the image generation over there, it fails almost every other day for some reason, and it's always for this reason.

**Vivek Shankar:** So these kinds of things, like what I'm trying to say is like TLDR, it'd be nice to have some sort of a channel there.

**Vivek Shankar:** I don't know if we have enough engineering resources to sort of have somebody embedded.

**Matthew Panzarino:** I mean, that's really what it boils down to.

**Matthew Panzarino:** Like, they're trying to get off air ops between now and June 10th.

**Matthew Panzarino:** Like, that's like, you know, our contract ends, we've got to get the hell off of air.

**Matthew Panzarino:** That's like, we'll all fall over if that doesn't happen.

**Matthew Panzarino:** So that's also why I'm here.

**Matthew Panzarino:** It's like, you know, race hell and get things fixed.

**Matthew Panzarino:** And help understand why these things are broken.

**Matthew Panzarino:** I mean...

**Matthew Panzarino:** The workflows having worked and giving you at least something you can work for your programmatic clients and for some of your clients, and then stopping is a huge deal.

**Matthew Panzarino:** If you could do me a favor after this, and we can talk more about this, and we'll talk more about it, because there's a couple of quality improvement exercises happening right now.

**Matthew Panzarino:** And I'm essentially the voice in that room for the delivery team, not that you can't be, or I'm not saying don't talk to them.

**Matthew Panzarino:** Of course, like voice it, but sometimes it requires a focused point at which you can apply pressure, you know, and I'm happy to see that point, you know, just hammer on my back and I'll push that forward.

**Matthew Panzarino:** But there is opportunity to improve there, but more importantly, if something was working and then broke, do me a favor after this, when you have a minute, look up if you can kind of when that broke, if you can find your original comment about, or...

**Matthew Panzarino:** At least the most recent time that it stopped working.

**Matthew Panzarino:** And let me look at that because the theory is, it's why you use GitHub.

**Matthew Panzarino:** You should be able to tell what it was that broke it.

**Matthew Panzarino:** And, you know, I think that's one of the big deals.

**Matthew Panzarino:** If it's like something suddenly stops working, there should be.

**Matthew Panzarino:** And I'm almost positive that, let me look here.

**Matthew Panzarino:** Okay, I don't have one.

**Matthew Panzarino:** I'm going to have Nana create a channel that is basically like delivery team stuff is breaking.

**Matthew Panzarino:** And I know that there's a build one where you're supposed to be like, oh, tell us if stuff broke, whatever.

**Matthew Panzarino:** Well, clearly, that's not working, right?

**Matthew Panzarino:** So I'll probably create a delivery side version of that and that I can see.

**Matthew Panzarino:** And then it helps me to sort of like tag people in on issues or lean on people.

**Matthew Panzarino:** Just know that right now, yeah, our engineering team is kind of like stretched.

**Matthew Panzarino:** Because we're trying to get the heck off of Aerofs and having to really rapidly develop the platform.

**Matthew Panzarino:** But if your workflow stops, if it breaks and we're able to call on it fast enough, we should be able to do a rollback.

**Matthew Panzarino:** We should be able to say, hey, JK, we're going to go back to an earlier version of this that's working for now so that we can get client deliverables out.

**Matthew Panzarino:** I mean, I think that's just standard when engineering is pushing something and it breaks fraud.

**Matthew Panzarino:** You just roll it back.

**Ismail Ajagbe:** You know what mean?

**Vivek Shankar:** That's the way.

**Ismail Ajagbe:** Yeah, exactly.

**Ismail Ajagbe:** Can I just take a minute to read the points on that?

**Ismail Ajagbe:** So I feel like the engineering should have like a controlled sandbox environment where they deploy life changes.

**Ismail Ajagbe:** And we at CMS and M is there to test the environment first before they deploy the code support.

**Ismail Ajagbe:** So the major issue we had a month ago when it happened, I noticed it's first-hand.

**Ismail Ajagbe:** So assuming that was a demo environment where data are going to be called up.

**Ismail Ajagbe:** So, like Vivek said, I'm not sure about the resources for the engineering team, but I hope that's something that can come live as soon as possible.

**Matthew Panzarino:** Yeah, I mean, I definitely put that, so the idea of a fraud environment and a pre-prod environment is definitely there, and I put that into the air.

**Matthew Panzarino:** I want it to happen.

**Matthew Panzarino:** It needs to happen.

**Matthew Panzarino:** I mean, we are a production team, and so having prod be suddenly changed, I mean, if it was a public-facing website, nobody would do that , right?

**Matthew Panzarino:** You'd have to have three people stack them on before you'd change anything.

**Matthew Panzarino:** So we just have to treat ourselves like clients a little bit better, so that's heard.

**Vivek Shankar:** Thank you.

**Vivek Shankar:** Yeah, that was actually a point that I raised with Daniel as well, long time back.

**Vivek Shankar:** I think late December, in fact, or before we went on year-end.

**Vivek Shankar:** Like, you can't keep deploying stuff on production.

**Vivek Shankar:** So I think that's the response I got was, like, what I understood was it's more of a resource thing.

**Vivek Shankar:** Like, you know, you can't have, like, separate environments, et cetera.

**Vivek Shankar:** So that is, that's understandable.

**Vivek Shankar:** But at the very least, you know, my response back then was at least we didn't have the directors back then.

**Vivek Shankar:** was just the MEs, at least have the MEs sign off on the changes.

**Vivek Shankar:** Something else I wanted to raise was the, one of the reasons I feel, and this came from me speaking with, you know, Jess and Aida, Mariana as well, back when, you know, we were sort of the only MEs.

**Vivek Shankar:** The flows themselves were very opaque.

**Vivek Shankar:** We didn't really understand what was happening in the background.

**Vivek Shankar:** And I know one of the reasons, like, for example, the assignment workflow, I feel we're one of the few pods who's actually using the assignment workflow because most people just don't know what's going on behind the grid.

**Vivek Shankar:** And that goes back to the opacity with which the engineering team is currently operating.

**Vivek Shankar:** It's like we don't know what's going on there.

**Vivek Shankar:** It's like they do something and something shows up on the grid.

**Vivek Shankar:** Like today, I checked the grid just before this call.

**Vivek Shankar:** The format of the outline has changed.

**Vivek Shankar:** I don't know why it's changed, but it's changed.

**Vivek Shankar:** So these things happen a lot.

**Vivek Shankar:** I think there needs to be some sort of communication there.

**Vivek Shankar:** And I don't know where they're gathering requirements from for the functionality of the grid.

**Vivek Shankar:** So that dialogue needs to happen.

**Matthew Panzarino:** Yeah, honestly, I don't even know if they are.

**Matthew Panzarino:** I mean, they are ad hoc.

**Matthew Panzarino:** Like Kirkman is doing his best to collate what people are telling him.

**Matthew Panzarino:** He just shipped one now.

**Vivek Shankar:** So we'll see what happens.

**Vivek Shankar:** Yeah, I saw it, yeah.

**Matthew Panzarino:** But yeah, I just recently got read in on some of that stuff.

**Matthew Panzarino:** And so part of the answer is like me to all of you.

**Matthew Panzarino:** And you'll see probably that I put a monthly meeting on the calendar.

**Matthew Panzarino:** Part of that monthly meeting will be like, hey, I want to hear all this stuff so that I can collate it, prioritize it, make sure that I can drive or help drive some change or updates there.

**Matthew Panzarino:** But yeah, the quality thing, I'll be honest with you, I'm still onboarding, right?

**Matthew Panzarino:** Like, in general, I'm still onboarding to getting this org up and running.

**Matthew Panzarino:** But part of the reason, well, not part of the reason, a good chunk of the reason I'm here is to, like, create that loop between, hey, here's my, like, you know, what I've done here with these articles is just really take from an end state and say, like, oh, man, this, it could be better so many of these ways.

**Matthew Panzarino:** Well, part of my job is to institutionalize that feedback, not only mine, but also yours that you're giving me, and the feedback between what you're getting in the output and what is there, and then take that and then feed that back into the beginning, you know, and institutionalize it across the workflows.

**Matthew Panzarino:** We'll get there.

**Matthew Panzarino:** I haven't even really started that work.

**Matthew Panzarino:** I'm really anxious to get going there.

**Matthew Panzarino:** So the answer is largely, I will.

**Matthew Panzarino:** I'll drive that, right?

**Matthew Panzarino:** And I'll make sure that that gets done.

**Matthew Panzarino:** Because, like, that's one of the reasons I'm here.

**Matthew Panzarino:** I don't want to, like, I didn't want to come here and run an editorial team.

**Matthew Panzarino:** I've done that a lot, you know, very thoroughly.

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** I wanted to, like, help build tools, right?

**Matthew Panzarino:** And helping to build tools with the help of all of you is, like, the thing that is exciting to me about this.

**Matthew Panzarino:** And that's the thing that will even make our job feasible long term, right?

**Matthew Panzarino:** There's only so many hours you can burn the midnight oil until you're like, well, I guess I'm burnt out.

**Matthew Panzarino:** I'll go do an easier job.

**Matthew Panzarino:** It's like, no, we need to work towards a place where people can, like, have a steady state and feel not overwhelmed.

**Matthew Panzarino:** So I have to jump.

**Matthew Panzarino:** I have another one back to back.

**Matthew Panzarino:** I'm sorry.

**Matthew Panzarino:** But we'll talk a little more.

**Matthew Panzarino:** We will have more chats.

**Vivek Shankar:** This is just the first of many.

**Vivek Shankar:** We will talk later today in that call, too.

**Matthew Panzarino:** All right.

**Ismail Ajagbe:** Thank you.

**Matthew Panzarino:** Ciao.

**Matthew Panzarino:** Ciao.
