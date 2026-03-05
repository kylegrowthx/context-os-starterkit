# Jakub & David – Sunbit Workflow & Process Insights

<metadata>
date: 2025-06-20
time: 16:16 UTC
duration: 47 minutes
organizer: Matthew Panzarino (GrowthX)
participants: David Galic (GrowthX Labs), Jakub Rudnik (GrowthX Labs), Feyisayo Odedeyi (GrowthX), Matthew Panzarino (GrowthX)
fathom_recording_id: 69651868
fathom_url: https://fathom.video/calls/331192340
share_url: https://fathom.video/share/m5JQAAssDajDKTdKbyvz-chVvx7J3vx_
source: fathom
enriched_on: 2026-03-03 18:45 UTC
</metadata>

---

## Summary

GrowthX delivery team (David Galic, Jakub Rudnik, Feyisayo Odedeyi) synced with Matthew Panzarino on workflow optimizations and client delivery insights across three accounts: Sunbit is shifting to purely educational B2B content (targeting dental offices and similar verticals) which required restructuring company context in Atlas to prevent financing/offers from bleeding into content; Airbyte successfully negotiated down from SEO score 80 to 65, freeing time for LLM-friendly formatting while exploring programmatic landing pages for data connector use cases; Hamlet requires highly specialized, technical content with multiple edit cycles due to terminology precision, necessitating custom writing instructions derived from before/after analysis. Key decision: GrowthX should position itself as expert advisor and push back on rigid client processes, particularly around SEO requirements and programmatic content strategy.

---

## Context

This is an internal GrowthX operations meeting where delivery leadership reviewed key insights from three client accounts—Sunbit, Airbyte, and Hamlet—to refine workflows and establish best practices. Matthew Panzarino (Director) wanted to understand what was working well across clients (based on feedback Marcel Panzarino gathered during client calls) and what bottlenecks the delivery team was hitting in Atlas, the platform they recently migrated to. David Galic (GrowthX Labs) has been running workflows and doing manual work on these accounts; Jakub Rudnik joined partway through to discuss Airbyte's programmatic SEO strategy; Feyisayo Odedeyi (content creator) participated to understand workflow improvements and keyword strategy. The broader context: GrowthX is positioning content generation as an expert advisory service, not just execution, and the team is learning that client relationships improve when GrowthX confidently advocates for what works rather than passively executing rigid requirements.

---

## Relevance

**To GrowthX Delivery:**
- Sunbit's success (50+ articles, zero rejections) required custom company/ICP context in Atlas separate from Sunbit's core business; pattern expected to repeat with other top-of-funnel clients. Document and reuse this approach.
- Airbyte negotiation (80→65 SEO score) removed major blocking constraint and improved content quality; clients often don't know what they actually want—expert pushback saves time and improves outcomes.
- Hamlet case demonstrates limits of generic workflows for highly specialized clients. Solution: extract custom writing instructions from before/after edit cycles using LLM analysis, then feed back into Atlas pipelines.
- Style Adaptation step in Atlas is being deprecated; no action needed, but workflows don't require manual editing to remove it.

**To GrowthX Business Development:**
- Sunbit, Airbyte, Hamlet all represent strong relationships and expansion opportunities: Sunbit moving to B2B (dental offices); Airbyte exploring tens of thousands of programmatic landing pages (data connectors × personas × jobs-to-be-done); Hamlet willing to invest heavily in custom editing cycles.
- All three clients explicitly trust GrowthX expertise and want us to lead strategy, not just execute specs. Reference this in renewal/expansion conversations.

**To CheckThat & AEO Research:**
- Airbyte's shift to LLM-friendly formatting (H2s, bullet points, Q&A structure) and deprioritization of SEO score reflects evolving client needs around AI visibility. Opportunity to research CheckThat's positioning here.
- Hamlet's multi-round edit cycles for technical content could inform CheckThat's prompt refinement for specialized domains (infrastructure, architecture, developer tools).

---

## Overview

- Sunbit content strategy shifting from SEO-focused to more educational/top-of-funnel approach
- Airbyte reducing keyword density requirements, focusing on LLM-friendly formatting
- Hamlet requires highly technical, specialized content needing multiple edit rounds
- Atlas workflow improvements discussed, including custom artifacts and pipeline adjustments

---

## Key Topics

### Sunbit Content Strategy

  - Shifting away from mentioning financing/offers to purely educational content
  - Creating new company info and target audience in Atlas based on blog content, not core business
  - Moving towards B2B content (e.g. tips for dental offices) requiring more depth
  - Jason (client contact) handles publishing, minimal red tape

### Airbyte Content Adjustments

  - Reducing SEO score requirement from 80 to 65, allowing focus on formatting and client priorities
  - Shifting towards LLM-friendly content structure (clear H2s, bullet points, questions)
  - Exploring programmatic landing pages for industries, personas, and use cases
  - Mario (client contact) encourages GrowthX to provide expert recommendations

### Hamlet Technical Content Challenges

  - Highly specific terminology requirements causing multiple edit rounds
  - David hesitant to create workflows due to output quality concerns
  - Suggestion to use LLM to analyze edits and create detailed writing instructions
  - Daryl has created custom artifacts/pipelines; collaboration needed to refine

### Atlas Workflow Improvements

  - Style adaptation step to be deprecated (redundant with article draft)
  - Creating custom artifacts (e.g. "Sunbit broad context") for different content types
  - Using brief's SEO metadata section to manually adjust keywords
  - Exploring ways to incorporate learnings from manual edits into workflows

---

## Action Items

**David Galic (GrowthX Labs)**
- Create new artifacts for Sunbit top-of-funnel content; name "Sunbit broad context" or "top of funnel company context", ensure matches original artifact naming format (artifact names like `company_context` must stay consistent with workflow references)

- Generate comprehensive Hamlet writing instructions via LLM by analyzing before/after article edits and client feedback; focus on terminology preferences and specific editorial rules, then input into custom Atlas workflow

- Sync with Daryl to review existing Hamlet workflows and artifacts; understand what's already been built (he's created custom pipelines with persona-based profiles like "Platform Architect"), avoid duplication


**Feyisayo Odedeyi (GrowthX)**
- Proactively report any workflow issues, misalignments, or gaps to David/Jakub/Matthew; focus on mechanical, tool-related, and process problems rather than client-specific issues
- Continue updating target audience and company context for Airbyte in Atlas; report blockers if next week's updates don't resolve keyword integration issues

---

## Transcript
**David Galic:** Right now, I'm running.

**Feyisayo Odedeyi:** The sound was not very clear.

**David Galic:** I did not hear what you said just now.

**David Galic:** Oh, yeah.

**David Galic:** I've been running a few of them.

**Feyisayo Odedeyi:** Okay.

**David Galic:** most of them are in the fact-checking section now.

**David Galic:** the article draft is done.

**David Galic:** So I'm going to just run them all the way through, and then I need a link if you can take look at it.

**David Galic:** All right.

**Matthew Panzarino:** Hey, how's it going?

**David Galic:** Hey, how's it going, Ben?

**Matthew Panzarino:** Good, good.

**Matthew Panzarino:** So good.

**Matthew Panzarino:** So good.

**Feyisayo Odedeyi:** Hello, Fathom.

**Matthew Panzarino:** Hello.

**Feyisayo Odedeyi:** to meet you.

**David Galic:** I know Jakub's, like, on a train.

**David Galic:** I think so.

**David Galic:** No problem.

**Matthew Panzarino:** It's all good.

**Matthew Panzarino:** I just want to talk a little bit.

**Matthew Panzarino:** I can catch up with David separately.

**Matthew Panzarino:** He'll be in town next week anyway, so.

**David Galic:** Yeah, yeah, yeah.

**Matthew Panzarino:** So I don't want to like take up a ton of time.

**Matthew Panzarino:** The context of this is, you know, the Marcel's making the rounds and talking to these clients and there were a handful that are like, you man, you guys are doing great.

**Matthew Panzarino:** These things are, you know, producing the results that we wanted.

**Matthew Panzarino:** We really have a good relationship with you.

**Matthew Panzarino:** We're very happy with the relationship, etc.

**Matthew Panzarino:** So I had Nana kind of gather some of those learnings and some of that understanding about, you know, what they were saying about the right things that you folks were doing from their side.

**Matthew Panzarino:** But I just want to gather from your side, kind of any insights you have into what, you know, how the relationship has developed, what the good things are, what you found were successful here.

**Matthew Panzarino:** Where, especially when it comes to like contrast with, like, oh, and this other client, you know, it's a little rockier and maybe it's because we didn't do X or maybe it's just the client relationship because they're.

**Matthew Panzarino:** There's also the big asterisk, which is that some clients are just like Jill and easier to deal with, et cetera.

**Matthew Panzarino:** So understand that.

**Matthew Panzarino:** But I just wanted to make sure that I made the time to do a little bit of a chat like this so that we could collate anything that we missed from their side about how relations have developed.

**Matthew Panzarino:** The basic rundown from what I understand on their side was, I mean, I'm talking about Sunbit in this case.

**Matthew Panzarino:** Like we could talk a little bit about like Airbyte or something too.

**Matthew Panzarino:** But like in Sunbit's case, you know, there was good research.

**Matthew Panzarino:** Like they were impressed with the research.

**Matthew Panzarino:** They really liked the collaboration that you did on content production.

**Matthew Panzarino:** That felt very seamless.

**Matthew Panzarino:** Like there was a good flow back and forth.

**Matthew Panzarino:** They, I guess they, there was at some point you shared, or they shared a new, like a nice, more detailed ICP and product details with you.

**Matthew Panzarino:** Which then improved the quality of the output a lot.

**Matthew Panzarino:** Mario really trusts you folks, which is great.

**Matthew Panzarino:** And then they're kind of excited about the long-term vision.

**Matthew Panzarino:** So these are all green lights.

**Matthew Panzarino:** The whole board is pretty solidly green in that regard, which is great.

**Matthew Panzarino:** And I kind of wanted to talk a little bit about, from your side, what you saw there.

**Matthew Panzarino:** Like, what was good about onboarding, the collaboration and relationship building parts, the strategic comms, and then, like, the agility.

**Matthew Panzarino:** Like, if they ask for something new or if they're giving you feedback, like, how'd go into that sort of thing?

**David Galic:** Okay.

**David Galic:** So we're definitely talking about Sunbit right now, right?

**Matthew Panzarino:** Because you mentioned Mario.

**Matthew Panzarino:** He's from Airbyte.

**Matthew Panzarino:** Oh, you know what?

**David Galic:** I think that was a mix-up.

**Matthew Panzarino:** Mario is from Airbyte.

**Matthew Panzarino:** Yes, Sunbit is what I'm talking about.

**David Galic:** We can talk about Airbyte 2.

**Matthew Panzarino:** It's all the same questions I have for both, to be honest.

**Matthew Panzarino:** All right.

**Matthew Panzarino:** Yeah, we can talk about Sunbit because they're really easy to talk about.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Jason is the contact there?

**David Galic:** Jason, yeah.

**David Galic:** Yeah, Jason, yeah, Belcher.

**David Galic:** Jason is super chill.

**David Galic:** He's, you know, and he does all the publishing itself, so we didn't have to worry about that.

**Matthew Panzarino:** He kind of likes that.

**David Galic:** Okay.

**David Galic:** takes care of it.

**David Galic:** He was really, he was expecting that there would be kind of like red tape because everything has to go through legal and through the bank first.

**David Galic:** So, like, we made sure, you know, not to, like, mention stuff that he told us not to mention, like financing and stuff like that.

**David Galic:** So, like, I don't think, I don't think any of our, like, 50 articles were ever flagged for anything, which is great.

**David Galic:** So, it's probably really easy.

**David Galic:** But the whole thing is that, really, it's easy to write about topics.

**David Galic:** So, you know, it's not very, it's not very technical.

**David Galic:** And I think they're, they're already in a really good place.

**David Galic:** So, it's, it's kind of chill.

**David Galic:** They have, like, crazy branded traffic already.

**David Galic:** So, like, they have that figured out already.

**David Galic:** And this is, like, a new project.

**David Galic:** So.

**David Galic:** It doesn't feel like there's a lot of pressure here, right?

**David Galic:** So I think since we're able to do everything very quickly for them and they're happy with the results, there's really like zero attention going on.

**David Galic:** The one big minus is that we weren't using the workflows almost at all for them.

**David Galic:** And a big part of that is what I just figured out like now when we switched to Atlas.

**David Galic:** So the biggest thing here is that what Sunbit does has nothing to do with what we're writing about mostly.

**David Galic:** So in the sense that like they don't want to talk about financing at all.

**David Galic:** They don't want to talk about their offers.

**David Galic:** They just want like purely educational content.

**David Galic:** You know, what are these sounds that my car is making?

**David Galic:** You know, how much do veneers cost and things like that?

**David Galic:** And like, and the CTA will be, they have like a, some like partners, like a directory.

**David Galic:** Like if you want, if you want.

**David Galic:** Check out our directory and find a local dental office close to you that we work with.

**Matthew Panzarino:** So it's like there's none.

**David Galic:** But, you we have a big problem with the workflows, which I recognize now as well.

**David Galic:** No matter what, like you would tell them, like, don't talk about financing.

**David Galic:** Since it's in the company info and it's very, very important in the company info and in the target audience, it's always going to kind of like flood into it no matter what you do.

**David Galic:** So for Atlas, I wrote a completely new, I wrote a completely new kind of like, not fake, but I wrote a company info and the target audience based on what the blog is and what the content is.

**Matthew Panzarino:** And I'll show that to you.

**Matthew Panzarino:** suggestion is like, you know, yes, almost all of our workflows are like writing content that is very close to the ICP and really should rely on the company content.

**Matthew Panzarino:** That's not help.

**Matthew Panzarino:** He helped the writer, you know, the workflow understand what.

**Matthew Panzarino:** What audience is talking to, but I think in some of these cases, we're going to find more of them, I would guess, where you're really building more of a link magnet or very top of funnel, like hyper top of funnel.

**Matthew Panzarino:** And when you're doing that, obviously, specificity will shoot you in the foot because it's like you're going to end up with a lot of topics that sound exactly the same.

**David Galic:** So your top of funnel is really actually going to be like this, right?

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Actually kind of narrow.

**Matthew Panzarino:** So I think you did the exact right thing, and I think that could be something to document, at least.

**Matthew Panzarino:** You don't have to go crazy, but you can kind of document, hey, we have this issue, and this was what the solution is we came up with.

**Matthew Panzarino:** And we can share that because I have a feeling that either we will find it happening again, or I honestly think like T-Row could benefit from something like this.

**Matthew Panzarino:** You know, there's plenty of people that are essentially addressing like a broad consumer base, not necessarily like a B2B, right?

**Matthew Panzarino:** And I think that is an opportunity for us because actually our engines should be really good at that.

**Matthew Panzarino:** And in all honesty, they should like deliver better content at that level.

**Matthew Panzarino:** It's not highly technical.

**Matthew Panzarino:** It's not incredibly specialized, but it should be high volume.

**Matthew Panzarino:** And I think that that's, you know, it's like fish in a barrel for us.

**Matthew Panzarino:** I would really love to do more of that because it's less manual labor and it's good wins from a traffic perspective.

**Matthew Panzarino:** So, yeah, I think that's, you did the right thing there.

**David Galic:** That's great.

**David Galic:** Yeah.

**David Galic:** So, all right.

**David Galic:** So now we're shifting to like B2B where right now we're going to create like, because they want to attract more partners, stuff like that.

**David Galic:** So we're creating content for like dental offices, you know, like tips to how to get more people in the door, how to improve like weight Like times, how to write interview questions for dental assistants, things like that.

**David Galic:** So I think.

**David Galic:** Actually, for the first time, Jason is collaborating with his demand generation team, who are kind of leading this project.

**David Galic:** So they had some comments, like, you know, they maybe want the tips to be more actionable, less general, stuff like that.

**David Galic:** And so I think it's going to require a little more depth, the B2B stuff, but I don't think it's going to be a huge obstacle.

**David Galic:** So I've already run a bunch of workflows, and, you I'm going to have the team take a look at them, and I'll take a look at them myself on Monday.

**David Galic:** But they look pretty good so far.

**David Galic:** And with the new company and the Target stuff I've written, like the financing is completely out of it.

**Matthew Panzarino:** Okay, yeah, that's great.

**Matthew Panzarino:** That all sounds good.

**Matthew Panzarino:** Keep me posted if you run into issues, but I think you're thinking the right ways about it.

**Matthew Panzarino:** I think more people are starting to understand, like, think Atlas is just clearer, you know, and people are kind of seeing what components came over from.

**Matthew Panzarino:** And understanding now, oh, well, that's the real, that's what we actually built.

**Matthew Panzarino:** And like the rest of this little fiddly stuff was really just air ops nonsense.

**Matthew Panzarino:** You know, that really had nothing to do with power to link.

**Matthew Panzarino:** And they're starting to understand what they can manipulate and build there.

**Matthew Panzarino:** With the pipelines, if you're building new pipelines, the only caveat is document them so that Daniel knows about them and what we're going with.

**Matthew Panzarino:** I don't think I'm going to fiddle with Anthony right now.

**David Galic:** think I'm just going to have writing guides for the B2B right now.

**Matthew Panzarino:** And then if we move back to B2C, I'll just switch it out.

**Matthew Panzarino:** Okay, cool.

**Matthew Panzarino:** Yeah, sounds good.

**Matthew Panzarino:** I mean, you can duplicate the pipeline.

**David Galic:** That's no problem, right?

**Matthew Panzarino:** Like you can duplicate the same exact one.

**Matthew Panzarino:** That's relatively easy to do.

**Matthew Panzarino:** Daryl can help if I don't have the time, but it's actually very simple because you're copying and pasting the whole thing.

**Matthew Panzarino:** And you're not really manipulating anything deeply.

**Matthew Panzarino:** But that way you can have, like, one pipeline that calls the general artifacts and then one that calls the specific artifact, the B2B versus B2C or whatever you want to call it.

**Matthew Panzarino:** But you don't have to.

**Matthew Panzarino:** You can just delete the instructions and rewrite, you know, or whatever.

**Matthew Panzarino:** I would love to make it simpler just a dropdown for versioning so that you, like, look at previous versions of the writing instructions and be like, oh, yeah, I was using B2 for this and B3 for that.

**Matthew Panzarino:** cool.

**Matthew Panzarino:** That's a simple solve, you know.

**Matthew Panzarino:** But this will get more modular.

**Matthew Panzarino:** They just haven't built the modularity because that part of it is, like, a whole nother trance of work and they just want to make it work first.

**Matthew Panzarino:** Yeah, yeah.

**Matthew Panzarino:** But, yeah, copy-paste for now is fine.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** So that's good.

**Matthew Panzarino:** Let's talk a little bit about, so let's talk about Airbyte.

**David Galic:** Airbyte, yeah.

**David Galic:** Okay, yeah, so Airbyte is, like, the one that.

**David Galic:** You know, it's like the one client I've been the least involved with just because they don't have that many, you know, things to, you know, kind of like, everything's cool.

**David Galic:** Like, it'll just be like one CM working on it and delivering and they're okay with everything.

**David Galic:** They don't check a lot.

**David Galic:** They just want, you know, to move fast.

**David Galic:** Right now, we just had a talk about some formatting stuff they want because they're kind of shifting away from SEO and want to make the content more for LLMs and, like, that kind of stuff.

**David Galic:** we're working on formatting things, making sure that everything's clearly structured.

**David Galic:** There's lots of bullet points and there's lots of questions for the H2s, things like that are very important to them.

**David Galic:** So, you know, this is something that now that I have a little bit more kind of, like, leeway and health, I want to definitely get more on top of the quality.

**David Galic:** And we've also made a great, huge agreement today because they wanted, like, an 80 score on search for SEO, which is, it always requires.

**David Galic:** It's too much massaging to a point where it looks like a lot of fun.

**David Galic:** And it takes us too much time.

**Matthew Panzarino:** It's super keyword choppy nonsense.

**David Galic:** So we asked them today, can we just, you know, at like 65, it has like every keyword you really need.

**David Galic:** Like, can we stop there and just like focus on, you know, the formatting and the stuff you guys really care about?

**David Galic:** And it's no problem.

**David Galic:** It's fine.

**David Galic:** So that's like a big blocker we've just removed.

**David Galic:** So, you know, we always, we also pitched it to it, to them as, you know, if we don't have this 80 score, like we can do 25 instead of it, you know, OB, no problem.

**David Galic:** So I think it's going to be a win-win there.

**Matthew Panzarino:** Got it.

**Matthew Panzarino:** Okay, cool.

**Matthew Panzarino:** Yeah, that sounds good.

**Matthew Panzarino:** Yeah, keep me posted on how that develops.

**Matthew Panzarino:** You know, those shifts are, I think, important.

**Matthew Panzarino:** I think that is an important part of the conversation that we need to remember with all of our clients is that we are the experts.

**Matthew Panzarino:** And we can advocate for what we know will work best and what we know.

**Matthew Panzarino:** We'll produce higher quality content.

**Matthew Panzarino:** I think in a lot of cases, a lot of these engagements have taken on this very regimented approach where it's like, oh, well, hey, here's what it says, and we're delivering X amount of articles, and that's it.

**Matthew Panzarino:** We're delivering this back.

**Matthew Panzarino:** But in reality, it's like, hey, we came in not just because we can execute on this, also because we know this business better than they do.

**Matthew Panzarino:** And in some cases, there are some clients that our point of contact is like a CMO or a high-grade SEO or a person who does content, in which case the dialogue is different.

**Matthew Panzarino:** But in a lot of cases, you will be talking to people who really have no idea what they're talking about.

**Matthew Panzarino:** And that's what our job is, right?

**Matthew Panzarino:** Our job is not to make them feel ignorant or feel bad about it or to be belligerent about it, but it is to offer that expert advice and push back and at least have a conversation.

**Matthew Panzarino:** It's like, hey, we just want to present you with this.

**Matthew Panzarino:** We have experience in this.

**Matthew Panzarino:** We work with, you know, I personally have worked with dozens of clients and I've done this for years and years, but also we work with, you know, dozens of clients internally now and we can tell you what is working and best practices right now.

**Matthew Panzarino:** And you need to probably, or not me, you need to, but we have a recommendation that should result in, you'd love to test it.

**Matthew Panzarino:** Let's try it, right?

**Matthew Panzarino:** And I think that, that could save us a lot of heartache trying to like fit ourselves into a puzzle that does, we know is probably not going to result in the results that they want.

**Matthew Panzarino:** And it's causing us a lot of grief, you know, so great call.

**David Galic:** Cool.

**David Galic:** Can you guys hear me, Jakub?

**David Galic:** Oh, hey, Jakub.

**Jakub Rudnik:** Hey, Jakub.

**Jakub Rudnik:** Sorry, I was literally just slacking, waiting for this call.

**Matthew Panzarino:** just had the wrong time.

**Jakub Rudnik:** So that's my bad.

**David Galic:** That's fine.

**Jakub Rudnik:** This is a perfect moment for you.

**David Galic:** You can talk about some, uh, program, programmatic stuff right here, but I don't know about.

**Jakub Rudnik:** Well, yeah, we can talk to you about that, but I would just say on that note, that was good timing.

**Jakub Rudnik:** I put a note in here, but they were.

**Jakub Rudnik:** Legitimately, like, they want our recommendations, and David, this is a little bit of like, I'm glad you called that out, but call it out faster and more assertively in the future, because they were kind of doing what they were doing before they started using us, and we just continued on with the same approach, but we're fighting an uphill battle and they're not happy. They're wondering why something takes longer, why we're giving them mixed results and things. Mario's talked to me before about this. He's just like, we want you guys to sell us those recommendations.

**Jakub Rudnik:** We want you to be our experts. Their contact Tammy is good, but he also hasn't done this before, so he's learning and still wants to learn from us. So it needs to be collaborative, and they want to collaborate, but don't lean on them to have the opinion. They want our opinion. They want us to lead. Yeah, I'll push you to do more of that. I think this is a good start there. Think of it that way, and don't think of them as having a rigid process. They're like, whatever gets us traffic and revenue.

**Jakub Rudnik:** It's revenue.

**Jakub Rudnik:** That's all they care about.

**Jakub Rudnik:** And so if we're doing anything that slows that down or slows production and we're not saying something, that actually causes more of an issue than just going with what they were hoping for, what they asked us to do three months ago.

**Jakub Rudnik:** So, again, this is a good launching point for that and all these new things.

**Jakub Rudnik:** But if you see that with them, and I think that goes for most of our clients, especially everyone, just like Mario's pinging me and letting me know what we need to do if we're doing it wrong.

**Jakub Rudnik:** Just tell us what to do.

**Jakub Rudnik:** He tells me that all the time.

**Jakub Rudnik:** So, let's keep doing that stuff.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Yeah, I agree.

**Jakub Rudnik:** And then their SEO, I've been outlining, like doing some wireframing and working with like Chachibutian, some of these ideas that they have.

**Jakub Rudnik:** Connect your pages, basically, where like they're, I don't know, they're not at all like Zapier, but their content kind of is like that.

**Jakub Rudnik:** Like they connect to a lot of other things and so they can do SEO and content around those things.

**Jakub Rudnik:** So, it's like thinking two different data sources to really.

**Jakub Rudnik:** They oversimplify, and so they have these connector pages already, how to connect this to Airbyte.

**Jakub Rudnik:** They also have pages of how to connect two types of data sources together, and so we can scale those.

**Jakub Rudnik:** But then they also, what they want to do is other programmatic type landing pages, some for industry, like how marketers connect data or something.

**Jakub Rudnik:** Like less excited about those, but how certain personas, there's more volume around.

**Jakub Rudnik:** Persona-based data connection, and then especially the jobs to be done, how to connect data for this type of dashboard, or how to connect data for this use case.

**Jakub Rudnik:** There's tons and tons, and you can even segment those with like data source plus job to be done.

**Jakub Rudnik:** So you can do like the generic one, and you can do, I don't know if there's volume for all of those, but at least in like key moments.

**Matthew Panzarino:** I would also advocate for checking on the personas, like, you know, data architecture, construction for data managers, for- Yeah, yes.

**Jakub Rudnik:** For many-

**Matthew Panzarino:** Serial types for rank and file, just go down the stack because you can do permutes of all of those.

**Matthew Panzarino:** And a lot of times it's like that kind of person searching for that.

**Matthew Panzarino:** And that search intent can be pretty, pretty strong from a conversions perspective, probably not from a broad traffic perspective.

**Jakub Rudnik:** Totally.

**Jakub Rudnik:** So all of those they have.

**Jakub Rudnik:** And so we've done basically like I've been outlining such like where did those connect and like what would that ecosystem look like?

**Jakub Rudnik:** Like I've done like a V1 of all of those and have handed that to Ada who was bringing it to the strategy sprint and Marcel.

**Jakub Rudnik:** I think they will update those.

**Jakub Rudnik:** They should expand on it.

**Jakub Rudnik:** They should definitely change some things that I've gotten to.

**Jakub Rudnik:** don't think it's like a perfect fit, but we know the link page types and have like have examples of how they would connect together.

**Jakub Rudnik:** would be a matter of like wire for like actually doing a mock-up and then seeing this in action and then what data they have on the backend.

**Jakub Rudnik:** That actually makes those things really sing.

**Jakub Rudnik:** And then especially the jobs to be done and the personas like.

**Jakub Rudnik:** We need their manual help, but what can be scaled there?

**Jakub Rudnik:** Because I think there's potential, like even Anto, what you're saying, there's good things in there, but there would also be cannibalization if we do too many without like validating.

**Jakub Rudnik:** So I think there's like some pitfalls to watch for.

**Jakub Rudnik:** But anyway, there's like tens of thousands of pages potentially, and that's what they want from us is like scale their total like SEO coverage across, you know, all sorts of long fields that they've had success with the programmatic before.

**Jakub Rudnik:** They just want to stand up all new types, and we, that's why they're partnering or like expanding the SoW pretty quickly.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Yeah, sounds good.

**Matthew Panzarino:** On the PSEO front, I think, I mean, the good news is that like, since it's in the strategy team hands, it's probably not going to have to do a lot of manual lifting on accessing resources to get that built out.

**Matthew Panzarino:** But I am also making sure that like any existing PSEO promises or SoW entries or work streams that were not actually leveraged or built out.

**Matthew Panzarino:** I'm I'm just just

**Matthew Panzarino:** Trying to, like, go around and make sure everybody is actually fully enabled to get those delivered.

**Matthew Panzarino:** It directly affects margins.

**Matthew Panzarino:** It affects workload and backlog and all of that.

**Matthew Panzarino:** Because, like, so many of the PSEO engagements we promised are really actually being delivered as editorial work streams, which is an enormous amount of labor, you know, that we shouldn't be having to do.

**Matthew Panzarino:** So we'll get all of that rectified.

**Matthew Panzarino:** In this case, I think you're already on the right track because it's going to go into sprint.

**Matthew Panzarino:** But if you come across anything else or if you get, like, surprises from SoWs, like, reviewing the SoWs of claims you're taking over is probably something all the directors should do just to make sure that we are actually delivering to the word of promises.

**Matthew Panzarino:** Or, in some cases, over-delivering, right?

**Matthew Panzarino:** And trying to figure out, like, okay, well, what do we actually promise them?

**Matthew Panzarino:** And where's the creep here?

**Matthew Panzarino:** And then figuring out how to navigate that.

**Matthew Panzarino:** I think that's an important one.

**Jakub Rudnik:** So I just wanted to call that out if that's occurring with you.

**Jakub Rudnik:** Yeah, for sure.

**Jakub Rudnik:** I think...

**Jakub Rudnik:** I think this one, starting from scratch, should be done properly, but I think, yes, good call for, especially David and Fey, if any of that comes in or starts leaking in a little snow where that is, let's do it the right way and not, like, gets, like, things to get it done, like we've done with PSCO in the past, it hasn't worked out well.

**Matthew Panzarino:** Yeah, exactly, and I appreciate, like, I really love the leaning in of, like, oh, let's just get it done, you know, but that's only, you can only do that for so long.

**Matthew Panzarino:** Every person only has so many, you know, units of energy in their life and in their work, and so if we're burning extra units on the stuff that we can automate or build a pipeline for, let's not mess with that.

**Matthew Panzarino:** Because I don't want people to burn out, you know, I want people to be able to do their job and then be like, cool, that was good, like, we did what we had to do and we're on track.

**Matthew Panzarino:** I don't want it to be like, oh, I guess I'll, you know, burn the midnight oil for weeks at a time to deliver something that we know really should just have a larger engine attached to it.

**Matthew Panzarino:** That's crazy town, so that's what we're here to do is make sure we're.

**Matthew Panzarino:** Building the tools to make this easier.

**Matthew Panzarino:** And then, like, for you, Feyisayo, if you are looking, if you are are looking, if what you prefer, or Feyisayo, or?

**Feyisayo Odedeyi:** Feyisayo, Feyisayo.

**Feyisayo Odedeyi:** Okay.

**Matthew Panzarino:** The, if you are, like, generating content, like, this is something that I've tried to communicate with a lot of the CMs, too, is that, you know, you'll get assignments down the pike.

**Matthew Panzarino:** Like, because a lot of, you know, kind of chatter back and forth has happened with the client, and then you're like, okay, cool.

**Matthew Panzarino:** So these are my deliverables.

**Matthew Panzarino:** If you are encountering, you know, issues or misalignments or things where you're like, hey, this, you know, I don't think this is going to do what you think it's going to do, or you're having difficulties, like, the best thing you could do is speak up immediately.

**Matthew Panzarino:** Obviously, cascade that up, you know, talk to David, talk to Jacob, if it's a strategic or tactical thing that you have concerns with.

**Matthew Panzarino:** And then if it's, like, a mechanical thing, also, too, to them.

**Matthew Panzarino:** But, you know, I'm here.

**Matthew Panzarino:** Of course, it's a resource.

**Matthew Panzarino:** And, you know, definitely chime in with other CMS or in the group settings to say, hey, is anybody else seeing X, Y, or Z?

**Matthew Panzarino:** Because we are in a transition time, and the faster everybody speaks up about mechanical things that are or are not working for them, the faster we can fix them.

**Matthew Panzarino:** So, you know, obviously lean into your pod for specific stuff that's client-related, where you're trying to, like, you know, match a client or output to a client's desires.

**Matthew Panzarino:** But don't hesitate to speak up, you know, if the tools are failing you or the process is failing you or creating additional friction where you would hope that there wouldn't be.

**Matthew Panzarino:** And rely on that ground truth of the people who are using these the most every day, you know, because Jakub and myself and David, get pulled in a lot of different directions.

**Matthew Panzarino:** And I try to use them every day to some degree, and I'm always helping people.

**Matthew Panzarino:** But, you know, you're using them day in, day out.

**Matthew Panzarino:** So don't hesitate to lean in there.

**Matthew Panzarino:** I really don't want any issues to stay unresolved, and you just kind of, like, pack together your own thing.

**Matthew Panzarino:** That's great.

**Matthew Panzarino:** In a near term, like a 24-hour, 48-hour period, but beyond that, how do we institutionalize that?

**Matthew Panzarino:** How do we build that into the system, or how do we improve the workflow so that you don't have to continue doing that manual work?

**Matthew Panzarino:** So always be thinking in a way like, what part of my day could have been, you know, productized?

**Matthew Panzarino:** Like, what part of it is so repetitive?

**Matthew Panzarino:** Boy, I always have to add an A at the end of every third sentence.

**Matthew Panzarino:** Well, that's, don't, you know, don't continue adding A's manually.

**Matthew Panzarino:** Like, okay, let's figure out how to do that from a programmatic perspective.

**Feyisayo Odedeyi:** So just always be thinking that way.

**Feyisayo Odedeyi:** Yeah, definitely.

**Feyisayo Odedeyi:** I always reach out to, especially David and the other CMT and Drive whenever I have issues, and they've been very helpful so far.

**Feyisayo Odedeyi:** I think right now we're just trying to update the target audience and company context generally for a bite especially.

**Feyisayo Odedeyi:** So hopefully next week things will be easier and smoother, but definitely if you have any issues.

**Feyisayo Odedeyi:** So I'll out to you or say it on the Slack channel.

**Matthew Panzarino:** Okay, great, great.

**Matthew Panzarino:** Yeah, I only mentioned that because I think that I came across a handful of issues for sure where people were like, oh, yeah, I've been having that issue for weeks or months.

**Matthew Panzarino:** And you're like, oh, wow, did you to tell anybody?

**Matthew Panzarino:** No, I just fixed it myself.

**Matthew Panzarino:** Okay, well, like, hey, I'm glad that you fixed it yourself.

**Matthew Panzarino:** That's really awesome.

**Matthew Panzarino:** But please speak up because if we don't, the system won't get better.

**Matthew Panzarino:** And any issue that you may be having, it's very likely if you never say anything about it, somebody else is having the same issue.

**Matthew Panzarino:** A lot of these things came up where it's like, I'm like, hey, is anybody seeing this?

**Matthew Panzarino:** And there's like a dozen responses.

**Matthew Panzarino:** Yeah, yeah, it's me.

**Matthew Panzarino:** Okay, did any of you mention this?

**Matthew Panzarino:** And they're like, no.

**Matthew Panzarino:** So definitely mention it.

**Matthew Panzarino:** Obviously, it's great that you're already communicating, but just wanted to encourage that with everybody.

**Matthew Panzarino:** Okay.

**Feyisayo Odedeyi:** Cool.

**Matthew Panzarino:** Yeah, thanks.

**Matthew Panzarino:** And then on the end, we might as well use this to just talk about any, we talked a little bit about.

**Matthew Panzarino:** Specific workflows, I think you're already on the way to setting things up correctly here.

**Matthew Panzarino:** But if you folks have any questions about, you know, Atlas-related stuff or flow or, you know, how these things are set up or if you need any tweaking or adjustment, you know, let me know.

**Feyisayo Odedeyi:** Yeah, I wanted to clarify because with Airbyte, have to use, okay, now the client says we don't have to use all of the keywords anymore, but we still have to use like a bunch of them.

**Feyisayo Odedeyi:** So what's the best way to include those keywords in Atlas that, to use them naturally within the article?

**Matthew Panzarino:** My current, my current advice that I'm working with, I'm working off of is to use the brief to do that.

**Matthew Panzarino:** So the brief, every brief has a keyword-related section.

**Matthew Panzarino:** That keyword-related section is based off of the set of parameters that are coded into the workflow.

**Matthew Panzarino:** So it's not something you can see or interact with.

**Matthew Panzarino:** This is something that happens at a lower level.

**Matthew Panzarino:** So when you say, give me a brief.

**Matthew Panzarino:** It comes back with something that it's built off of a framework.

**Matthew Panzarino:** It's like a certain keyword rank, a SERP rank.

**Matthew Panzarino:** It filters out some lower quality stuff, but it also doesn't pick stuff that's too high score.

**Matthew Panzarino:** Cricklin has actually detailed it in a couple of places.

**Matthew Panzarino:** I can link it to you.

**Matthew Panzarino:** But it's basically like, hey, we've got a rough outline of what we want keyword-wise, and then that's what comes back.

**Matthew Panzarino:** It spits that out into the brief for you, but you don't have any fine-tuned control over that currently.

**Matthew Panzarino:** Like in the future, I would imagine that we would, right?

**Matthew Panzarino:** We'll probably have control over a lot more things in the future.

**Matthew Panzarino:** For now, when it spits that brief back, just scroll down to the keyword section, because you'll have that section where it's like keywords, ranks, SEO, the SEO section, which is the second section usually in the brief.

**Matthew Panzarino:** Jump in there and tweak it to exactly what the client wants.

**Feyisayo Odedeyi:** So just if you've got a list of keywords, paste them in there.

**Feyisayo Odedeyi:** So I just wanted to confirm, like, it's okay to use not just one keyword.

**Feyisayo Odedeyi:** But if you have about 10 of them, you can use all 10.

**Matthew Panzarino:** Yeah, I don't think that's a problem.

**Matthew Panzarino:** Let me show you just as an example of what section, just for visual recognition, if you look in article generation, of course, I was looking at a pipeline that has nothing generated.

**Matthew Panzarino:** Let me show you the pipeline here.

**Matthew Panzarino:** Is it sharing my whole screen or something?

**Matthew Panzarino:** Okay, that's just a window, okay, cool.

**Matthew Panzarino:** So the brief. Okay, so we go to the brief.

**Matthew Panzarino:** This is Airbyte, obviously.

**Matthew Panzarino:** If you go into the brief, you go to the output, then, you know, it's got some stuff here.

**Matthew Panzarino:** This SEO metadata section right here, you know, this all informs everything that is created from here.

**Matthew Panzarino:** This is fine.

**Matthew Panzarino:** But this keyword stuff here, you can replace this entire section with whatever you want, right?

**Matthew Panzarino:** And you can say, like, these are the keywords that I want you to target.

**Matthew Panzarino:** You don't even have to include the volume and competition level and stuff.

**Matthew Panzarino:** You can just tell it the keywords that you want to focus on.

**Matthew Panzarino:** Or you can export those, you know, into a structure that makes sense.

**Matthew Panzarino:** It doesn't hurt to include this structure because it uses this to prioritize the keywords, like where they appear in the articles and that sort of thing.

**Matthew Panzarino:** But that's what I would suggest.

**David Galic:** I wanted to ask, like, if you have a longer list of keywords, would it be better to list them separated by commas or as a bullet list?

**David Galic:** I don't know.

**Matthew Panzarino:** To be honest, I don't know.

**David Galic:** I'll try both out and see where it happens.

**Matthew Panzarino:** Yeah, I would run.

**Matthew Panzarino:** One and then run the other and then see which one results in an outline that feels more like, okay, this is a good organic integration of the keywords that I wanted.

**Matthew Panzarino:** Give it a try.

**Matthew Panzarino:** But for now, until we have like a specific SEO input for the assignment brief, this is where I would make that adjustment.

**Matthew Panzarino:** So once you do that, then of course, the brief is used to conduct the research.

**Matthew Panzarino:** So the research would then focus on those keywords.

**Matthew Panzarino:** The brief is used to create the outline.

**Matthew Panzarino:** The outline will be your litmus test for whether or not those keywords were, you know, accessed.

**Matthew Panzarino:** And then, of course, the article draft, you know, to see if they're integrated well.

**Matthew Panzarino:** But the outline should, the key topics should reflect the keywords, you know, to put in there.

**Matthew Panzarino:** That's fine, right?

**Matthew Panzarino:** So that's what I would suggest for now if you want to integrate specific keywords.

**David Galic:** For me, the only question I really not have is like the style of action.

**David Galic:** Like what am I expecting from that?

**David Galic:** What should be that output?

**David Galic:** So I'm not really understanding how it's like making it better.

**Matthew Panzarino:** What's that now?

**David Galic:** The style adaption part?

**Matthew Panzarino:** Hmm, yeah.

**David Galic:** I'm not really understanding what it's doing.

**Matthew Panzarino:** deprecated.

**Matthew Panzarino:** Style adaption is useless.

**David Galic:** Okay.

**Matthew Panzarino:** It's not useless.

**Matthew Panzarino:** It's like, what it does is it reapplies the writing guidelines, but the writing guidelines are already called an article draft.

**Matthew Panzarino:** So Daniel is actually going to delete these.

**David Galic:** Style adaption will silently disappear for you fairly soon.

**Matthew Panzarino:** So I wouldn't worry about it too much because it's going to go away.

**Matthew Panzarino:** Like, it is, all it does is rewrite the entire article with the writing guidelines again.

**Matthew Panzarino:** There's no need for that.

**Matthew Panzarino:** It already did it in the article draft.

**Matthew Panzarino:** So, yes, it's a whisker from the previous, this used to be called polishing instructions, if you'll recall.

**Matthew Panzarino:** That's what it is, right?

**Matthew Panzarino:** And so, like, it's no longer necessary.

**Matthew Panzarino:** It's the article draft calls as an input the writer guidelines, right?

**Matthew Panzarino:** So article draft calls writer guidelines as an input.

**Matthew Panzarino:** But style adaptation calls.

**Matthew Panzarino:** Um.

**Matthew Panzarino:** Content, and then, like, I think this should call, I'm pretty sure this is just writer guidelines.

**Matthew Panzarino:** I don't know why this variable is named different.

**Matthew Panzarino:** That's programmer's code.

**Matthew Panzarino:** I don't mean to go, but that's what this is.

**Matthew Panzarino:** You can see here, it's the writing and editorial style guide, right?

**Matthew Panzarino:** The same thing that is called in writer guidelines.

**David Galic:** Yeah?

**Matthew Panzarino:** Okay, cool.

**Matthew Panzarino:** So that's what that does.

**Matthew Panzarino:** What can you do for now to ignore that?

**Matthew Panzarino:** You can delete it manually from the workflow.

**Matthew Panzarino:** Actually, I can delete it manually from your workflow if you want.

**Matthew Panzarino:** It does not matter.

**Matthew Panzarino:** The trick is I can't do it, like, on the fly because internal links then has to be updated to take the output of fact-checking and so on and so forth.

**Matthew Panzarino:** I'm not going to mess with it only because Daniel said he's going to remove it from everything, so I'm not going to manually go around touching stuff.

**Matthew Panzarino:** That should, in a commit soon, go away.

**Matthew Panzarino:** That's what that is, though.

**Matthew Panzarino:** It's just a reapplication of.

**Matthew Panzarino:** What already happened in article draft, so.

**David Galic:** Okay.

**Matthew Panzarino:** Sweet.

**Matthew Panzarino:** And then, of course, feedback, the feedback column has been replaced by our little AI suggestion tool, which will hopefully get better and better as we go, so.

**David Galic:** That's good.

**Matthew Panzarino:** Yep.

**Matthew Panzarino:** Any other workflow questions or quirks?

**Matthew Panzarino:** You're already doing the right thing, like creating specific instructions.

**Matthew Panzarino:** That's exactly the way to go.

**Matthew Panzarino:** You know, a different company profile and ICP profile.

**Matthew Panzarino:** You can even change, you can change all of them, right?

**Matthew Panzarino:** Like, can, you can create, the cool thing is, you can create new artifacts all you want.

**Matthew Panzarino:** Like, those don't require any, any weird, you know, adjustments or, or any code from your end.

**Matthew Panzarino:** So, if you want to create artifacts specifically for those, for those pipelines, do so.

**Matthew Panzarino:** So, if, which one, was it Airbyte or was it Sunbit that we were talking about with that?

**Matthew Panzarino:** It was Sunbit.

**David Galic:** Sunbit.

**Matthew Panzarino:** Sunbit with Sunbit.

**Matthew Panzarino:** No, yeah.

**Matthew Panzarino:** Sunbit is...

**Matthew Panzarino:** Really simple.

**Matthew Panzarino:** You go in and I'm going to miss when these aren't alphabetical.

**Matthew Panzarino:** like that.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** So artifacts, if we go into the artifacts here, you've got, you know, the company context and you were mentioning, okay, I need to change this.

**Matthew Panzarino:** it stops mentioning, you know, specific topics.

**Matthew Panzarino:** You can just create artifacts here, right?

**Matthew Panzarino:** And then just name this, you know, Sunbit broad context, company context or whatever, a top of funnel company context, whatever makes sense for you.

**Matthew Panzarino:** And then just make sure that this is actually named the same thing as the previous one.

**Matthew Panzarino:** Like, in other words, if this company context right here, you see how it says company underscore context?

**Matthew Panzarino:** So it just has to be company underscore context because right now it's not the, the workflows are calling these things specifically.

**David Galic:** Yeah.

**Matthew Panzarino:** I've changed.

**David Galic:** I've all of them already.

**Matthew Panzarino:** What's that?

**David Galic:** I've changed all of them already.

**Matthew Panzarino:** Yeah, yeah, yeah.

**Matthew Panzarino:** And then if you, if you, but if you go in and if you want to create a new one, you can just create one.

**David Galic:** Is what I mean.

**Matthew Panzarino:** Create as many as you want.

**Matthew Panzarino:** Just name them different stuff.

**Matthew Panzarino:** Yeah, got it.

**Matthew Panzarino:** Yeah, I think, if I remember correctly, no, I didn't remember correctly.

**Matthew Panzarino:** I'm trying to remember here who it was.

**Matthew Panzarino:** I think it was Matt.

**Matthew Panzarino:** Okay, well, here's one example.

**Matthew Panzarino:** Like, he's got, like, this other completely different type of format, right?

**Matthew Panzarino:** And this is, like, a completely different artifact.

**Matthew Panzarino:** So creating new artifacts is a-okay.

**Matthew Panzarino:** Like, you can do that.

**Matthew Panzarino:** They, they are not, that's not going to disrupt any code or anything.

**Matthew Panzarino:** They're there for you.

**Matthew Panzarino:** There's a reason there's a create artifact button.

**Matthew Panzarino:** So if you want to create a separate one for that separate pipeline, you can do so.

**Matthew Panzarino:** And in that separate pipeline, we can help you build that to call those other artifacts.

**Matthew Panzarino:** But for now, as I mentioned, the copy-paste method will work.

**David Galic:** Cool.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Sweet.

**Matthew Panzarino:** All right.

**Matthew Panzarino:** Any other immediate topics?

**David Galic:** I don't know if we want to talk about Hamlet.

**Matthew Panzarino:** Oh, yeah.

**Matthew Panzarino:** I mean, we can talk a little bit about it.

**Matthew Panzarino:** What do we want to talk about?

**Matthew Panzarino:** We want to talk about workflows for them or strategy or whatever?

**David Galic:** I haven't even put together any workflows for them because I'm so afraid of the output.

**David Galic:** Because even when I'm doing anything manually, it's not good enough.

**David Galic:** So it's like a frightening thing to me right now.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Interesting.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** That's an interesting topic and probably not a 15-minute topic.

**David Galic:** Yeah.

**David Galic:** Yeah.

**Matthew Panzarino:** I think we can do that some other time.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** No.

**Matthew Panzarino:** I mean, some other time is probably very soon, though, right?

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Let me think...

**Matthew Panzarino:** Let me take a look at them.

**Matthew Panzarino:** I noticed that we've got a lot of artifacts already created in here.

**Matthew Panzarino:** Were these ported over from Airtable, or were you manually creating these?

**David Galic:** That might have been stuff that Daryl was working on.

**Matthew Panzarino:** Okay, got it.

**Matthew Panzarino:** Yeah, this might have been Daryl's messing around.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** And the pipelines here are the same thing.

**Matthew Panzarino:** He's created some new pipelines here.

**Matthew Panzarino:** The comprehensive, the comparison, the platform architect, this is a specific persona-based profile.

**Matthew Panzarino:** Yeah, yeah, because it calls just the artifact platform persona.

**Matthew Panzarino:** Interesting.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** I think it's probably best, since Daryl was messing around with this, let me get with him and see what's up.

**Matthew Panzarino:** But yeah, we'll probably need to do a little hands-on work kind of building stuff because they have such specific requirements.

**Matthew Panzarino:** But it is a stress test for the system to help figure out what sources of truth we can access and what the limits are. You know, what can we build that can get us a lot closer to what they need?

**Matthew Panzarino:** And then with them, you know, we may have to do some manual tweaking from there.

**Matthew Panzarino:** But remind me, are we concentrating on top of funnel stuff for them right now or higher up?

**David Galic:** So right now I gave them two articles about secrets management and they still had comments, but it seems like it was a lot quicker to edit.

**David Galic:** Whereas the other stuff, the stuff that's directly related to them, everything goes like three or four rounds of edits because it's just the terminology. I'm not getting it right in either the AI output or manually.

**David Galic:** And I also wanted to ask, like, if we get like four or five that they like that are related to them, how do we put that into the workflow?

**David Galic:** Do we just run a fake workflow and add the final version at the end, so the workflow can look at it later?

**Matthew Panzarino:** Um, okay.

**Matthew Panzarino:** So there are a couple of ways.

**Matthew Panzarino:** So think about this.

**Matthew Panzarino:** One is like all of the work that you've done canonically to get these where they need to go, that is invisible to Atlas at the moment, right?

**Matthew Panzarino:** Like it's invisible to our, or more like it's actually invisible to Flow, which is the engine that runs Apple.

**Matthew Panzarino:** But it's invisible right now because we've been doing it off-prem, right?

**Matthew Panzarino:** And so I think to integrate the instructions, one way to do it would be, do you have initial versions of the articles and then final versions that you've created?

**David Galic:** I can, I can go through versions, you know, and I can, I can also look at all the comments that are left and kind of like put them into my document.

**Matthew Panzarino:** Yeah, I would say you can feed those diffs to an LLM and ask it, "Here's what I did."

**Matthew Panzarino:** Unfortunately, it's really hard for it to take versioning in Google Docs because Google Docs' API sucks.

**Matthew Panzarino:** And they don't really even give you access to versioning.

**Matthew Panzarino:** In a rough way, they do, but they definitely don't give you access to some of the things I wish they would have.

**Matthew Panzarino:** We could probably build a make.com workflow that could pull all the versions apart, but there may be more labor than it's worth.

**Matthew Panzarino:** I think it's really the beginning and end that matter.

**Matthew Panzarino:** And then, are you using a context window to edit these?

**Matthew Panzarino:** Or are you using a chat window to edit these specifically?

**David Galic:** Yeah.

**David Galic:** So I'm kind of like, here's what I wrote.

**David Galic:** Here's what they highlighted.

**David Galic:** Here was the comment.

**David Galic:** And then I'll go through all that work, show it to the LLM, and it will give me that summary and those rules.

**Matthew Panzarino:** So I think it's step one is like you can mess around with the pipelines.

**Matthew Panzarino:** You can talk to Daryl about this, but since you have been doing a lot of the work, you hold that information.

**Matthew Panzarino:** Right now, it's in you, right?

**Matthew Panzarino:** Your brain.

**Matthew Panzarino:** Your context window, your docs, and we don't have that.

**Matthew Panzarino:** Nobody else has access to that to mess around.

**Matthew Panzarino:** So I think the next step is take your diffs, take your originals and your edited pieces, put them into that same window that you've been using to edit this thing, and write fairly detailed instructions on it.

**Matthew Panzarino:** Say, hey, you are a high-level editor, and you've been working with me to edit these articles.

**Matthew Panzarino:** I'm giving you the before and after.

**Matthew Panzarino:** Here's the prompt I would give the LLM: "As a high-level editor, you've been working with me to refine these articles. I'm going to show you before and after versions. For each one, please ask me about it. Don't just dump all the content at once or you'll get confused. As soon as we're done with this conversation, please"

**Matthew Panzarino:** Please enumerate explicitly for me all of the edits and changes that were made between these articles.

**Matthew Panzarino:** Then I'd like you to enumerate the rules by which you think these articles should be edited.

**Matthew Panzarino:** Given the conversations we've had about these pieces.

**Matthew Panzarino:** Then I'd like you to combine those two into writing instructions for this company.

**Matthew Panzarino:** Be very specific and explicit about things that they like, that they don't like, the terminology that they like to use.

**Matthew Panzarino:** Get as explicit or as specific as you need to get.

**Matthew Panzarino:** Produce writing instructions for me and then drop that into the pipeline and see what happens.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** That's the way I would go about it, just to start, at the very least.

**Matthew Panzarino:** And Daryl may have already done some of this, so I would talk to him a little bit about it.

**Matthew Panzarino:** He doesn't have all of the information you have because he doesn't have all of your chat window, you know, et cetera.

**Matthew Panzarino:** So I think it's important to export that learning from there somehow.

**Matthew Panzarino:** I've been doing this as well.

**David Galic:** So after every chat session, I would ask him to create, to update my guidance.

**David Galic:** So I have some of it.

**Matthew Panzarino:** Yeah, I would try to do a comprehensive one that concentrates on it and gives context too.

**Matthew Panzarino:** The client that we, you and I are editing these for is extremely particular, very specific.

**Matthew Panzarino:** They have, I can provide you with information on the company and what they do and with their developer documentation and, you know, ask me for those when you're ready.

**Matthew Panzarino:** The output I would like is a document that I can use to give someone else instructions on how to write for this client in incredibly specific detail.

**Matthew Panzarino:** Let's go.

**Matthew Panzarino:** What do you need first, right?

**Matthew Panzarino:** And then see what it asks you for.

**Matthew Panzarino:** Just walk it through to create a first principle starting place that we can use to generate a custom workflow specifically for those highly technical articles.

**Matthew Panzarino:** For the other ones that you mentioned, it seems like we could probably tweak the existing article generation pipeline enough to get, like, within striking distance.

**Matthew Panzarino:** And

**Matthew Panzarino:** You know, they're close reading during the kickoff period.

**Matthew Panzarino:** That's normal.

**Matthew Panzarino:** Eventually, they'll probably zoom out a bit, you know.

**David Galic:** Okay, cool.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Sweet.

**Matthew Panzarino:** And, yeah, I'll mention it to Daryl to kind of, like, jump in with you on it because given that he has a lot of custom work in these workflows and some of it's stubs and some of it seems to be more complete, I think it's important to get a close read on those so you understand where he's at rather than me barging in trying to create new stuff on top of the stuff that he's already working on.

**David Galic:** Got it.

**Matthew Panzarino:** Cool.

**David Galic:** Great.

**Matthew Panzarino:** All right.

**Matthew Panzarino:** Thanks, folks.

**Matthew Panzarino:** Appreciate it.

**Matthew Panzarino:** Yeah, I'm here.

**Jakub Rudnik:** Yeah, what's up, Jacob?

**Jakub Rudnik:** It's the same.

**Jakub Rudnik:** Thanks for the help.

**Jakub Rudnik:** Appreciate it.

**David Galic:** Of course.

**David Galic:** Of course.

**David Galic:** Yeah, great.

**Matthew Panzarino:** Great call.

**Matthew Panzarino:** All right.

**Matthew Panzarino:** Thanks.

**David Galic:** See you, man.

**Jakub Rudnik:** Bye.

**Jakub Rudnik:** Ciao.

**Jakub Rudnik:** Bye.
