# You.com <> GrowthX - Bi-Weekly Sync

<metadata>
date: 2026-02-25
time: 19:01 UTC
duration: 28 minutes 27 seconds
organizer: Bailey Seybolt (bailey@growthx.ai)
participants: Bailey Seybolt (GrowthX), Brooke Grief (You.com), Justin Fink (You.com), Fred Fireflies (Fireflies.ai), Team GrowthX
fathom_recording_id: 125371183
fathom_url: https://fathom.video/calls/578884302
share_url: https://fathom.video/share/HMZxo3z3zEBvWY_MBEi69XDzzQYshMx4
source: fathom
enriched_on: 2026-02-27T17:15:00Z
</metadata>

---

## Summary

Bailey and Brooke aligned on three workstreams: (1) prioritizing 10 SME-review-free topics plus breaking down the "Emails" white paper into blog posts to maintain publishing velocity, (2) building a dual-path AI visibility strategy—one respecting the competitor-mention constraint and one showing unconstrained performance—to make the case to You.com executives, and (3) deploying Check That, GrowthX's in-house AI visibility tool, as the primary monitoring system alongside Brandlight testing.

---

## Context

You.com is building AI visibility and content-driven LLM ranking strategy with GrowthX's support. The marketing team faces conflicting directives: executives demand #1 AI visibility across platforms, but constraint against competitor mentions limits strategic options. SME review bandwidth is the primary bottleneck limiting content output. GrowthX has developed Check That, a custom-built AI visibility tool offering better usability and signal quality than Brandlight, which tracks 3,200 prompts but with significant noise.

---

## Relevance

- **Content Workflow:** Bailey proposed dual-track approach—immediate wins from 10 pre-approved SME-free topics plus repurposing white paper sections (e.g., "four-phase evaluation methodology" from Emails white paper as standalone posts).
- **Executive Strategy:** Brooke seeks documentation and comparative analysis showing performance impact of competitor-mention constraint to justify lifting it with Justin and executive team; already has internal sponsor and no need for CEO intervention.
- **Product & Tools:** Check That access enables data-driven SME conversations and monthly reporting; Brooke will test Check That against Brandlight for Feb report, comparing data quality and usability.
- **Persona Focus:** AI Laggard and technical developer personas remain primary targets; bottom-up motion through API documentation and developer targeting.

---

---

## Overview

- **Content Pipeline:** To bypass SME bottlenecks, the team will prioritize 10 approved topics that require no SME review. A new strategy will also break down existing white papers into blog posts.
- **AI Visibility Strategy:** GrowthX will deliver a dual-path strategy: one path for content that adheres to the no-competitor-mention rule, and another for content that does not, to demonstrate the performance trade-offs.
- **New Tooling:** Brooke now has access to "Check That," GrowthX's custom-built AI visibility tool. Brooke will test it against Brandlight for the February monthly report to compare usability and data quality.
- **SME Unblocking:** Brooke can now use AI visibility data from "Check That" to make a stronger case to SMEs, explaining how specific articles directly address ranking gaps and accelerate review times.

---

## Key Topics

### Content Pipeline & SME Bottlenecks

  - SME review is the primary bottleneck delaying content publication.
  - **Interim Plan:** Focus on 10 approved topics that require no SME review to maintain publishing velocity.
  - **Blocker:** Technical white paper articles are on hold until Brooke's team reviews the first two drafts.
      - **Rationale:** This review is needed to calibrate the pipeline and avoid rework.
  - **New Strategy:** Break down existing white papers into blog posts.
      - **Goal:** Create content without triggering new SME reviews.
      - **Pilot:** The "emails" white paper is ideal, with clear sections (e.g., "four-phase evaluation methodology") that can become standalone posts.
      - **Constraint:** New posts must also be validated for keyword relevance.

### AI Visibility Strategy

  - **Challenge:** The executive directive to be \#1 in AI visibility conflicts with the marketing team's constraint against mentioning competitors.
  - **Proposed Solution:** GrowthX will deliver a dual-path strategy in a Notion doc.
      - **Path A:** Content strategy that adheres to the no-competitor-mention rule.
      - **Path B:** Content strategy that does mention competitors, with projected results.
      - **Purpose:** This comparison will demonstrate the performance trade-offs and build the case for lifting the constraint.
  - **Executive Buy-in:** Brooke has the necessary support from Justin and does not require GrowthX's CEO to intervene.
      - **Need:** Documentation on the value of content for AI visibility, which Brooke can use internally.
  - **Persona Focus:** The AI Laggard and technical developer personas remain the focus.
      - **Rationale:** The developer persona is key for a bottom-up motion targeting LLM visibility (e.g., API documentation).

### Tooling: Check That

  - Brooke now has access to "Check That," GrowthX's custom-built AI visibility tool.
  - **Key Features:**
      - **URL Search:** See top-cited URLs and their citation percentage.
      - **Prompt Library:** Access vetted, pre-populated prompts with 30 days of historical data.
      - **Custom Prompts:** Create new prompts (signal appears in 24–72 hours).
      - **Context Management:** Update tracked competitors, products, and personas.
  - **Comparison to Brandlight:**
      - **Usability:** "Check That" is more user-friendly.
      - **Prompt Volume:** Brandlight tracks 3,200 prompts, but many have low "query importance," yielding noisy data. "Check That" aims for a more focused, actionable approach.
  - **Feature Requests for Roadmap:**
      - Filter results by specific LLM engine.
      - Implement a weighted visibility score (e.g., higher weight for ChatGPT citations).
  - **Next Test:** Brooke will use "Check That" for the February monthly report to compare its data and usability against Brandlight.

---

## Action Items

**Brooke Grief (You.com)**
- Route 2 white-paper-derived posts to SMEs for review (00:01:44)
- Test Check That data for Feb monthly report; send feedback to Bailey (00:22:40)

**Bailey Seybolt (GrowthX)**
- Send 'Emails' white paper to editorial; request blog breakdown w/ keyword validation (00:03:55)
- Add persona labels in Airtable for Brooke (00:05:49)
- Build AI visibility strategy (Notion) w/ constrained + ideal-state options; share w/ Brooke (00:07:33)
- Send AI visibility/content-value docs to Brooke for exec convos (00:09:31)
- Add marketing ops team member to Check That; ask Brooke for email if needed (00:21:41)
- Resurface Check That Loom in Slack for Brooke; she'll share w/ team (00:21:54)

---

## Transcript

**Bailey Seybolt:** I'll share our agenda. So in terms of pipeline status, I took a look at the topics you approved and I prioritized the 10 that wouldn't need any SME review. I figured that would buy us runway and hopefully let us get some content live and published while we're figuring out some of the other shifts in strategy. My plan is to focus on those for now. We do have the other white paper topics too, which would be great for targeting that technical persona, but I'm reluctant to jump into those until you or your SME have a chance to review the two we already did. Just in case you have any flags there, I don't want us to get into a situation like we did before where you're adjusting the pipeline and then rerunning tons of content for review. So I think it might be better to hold off until you have a chance to calibrate on those first two posts.

**Brooke Grief:** Which two are you referring to?

**Bailey Seybolt:** Let me pull up your table. Of the ones in review, you'll see they're marked as article type. These two at the bottom are from the white paper. There should be a link to the source at the top so you can reference back, along with the keyword we scraped.

**Brooke Grief:** Perfect. Those will take a bit to get reviewed, but I'll make sure they get in front of the right people.

**Bailey Seybolt:** Great. In general, this pipeline has performed well when it has a good source document. My hope is minimal feedback and that this might be a lane we can continue to publish in without needing too much intensive SME review.

**Brooke Grief:** Yeah, another option to explore is separating the white papers—truly verbatim or just touching up slightly to make it read like a blog. That obviously wouldn't need review since it's already live, so it could help speed things up. I fear the same delay with SMEs versus just taking what we already have and breaking it up.

**Bailey Seybolt:** I'll take a look at the white papers. Do you have anyone in mind that would be particularly good?

**Brooke Grief:** The emails one actually has a framework where each section could be split out. There's a four-phase evaluation methodology that could be its own thing, or "What makes search evaluation so hard?"—that could be a blog post. The bigger chunks each could be their own thing.

**Bailey Seybolt:** Yeah, I think that's definitely something we could do, especially if it's already pre-structured. We'd need stronger guardrails for breaking it up versus scraping it. We'd also need to validate them from a keyword perspective.

**Brooke Grief:** Totally.

**Bailey Seybolt:** I'll send that to our editorial team with those guidelines and see if we can create a version that just breaks it up without changing anything that would trigger SME review.

**Brooke Grief:** That sounds great. I think there are 10 published now.

**Bailey Seybolt:** I'll add persona labels in Airtable to flag the blog personas, so it's easier to see at a glance.

**Brooke Grief:** Yeah, that would be great.

**Bailey Seybolt:** So in terms of strategy, I just want to confirm this feels like the right direction. We're focusing on the AI Laggard persona—I know those were the initial keywords, but we'll build out research so you have more topics. Then the white paper breakdown, and once you review the initial ones with SMEs and this additional one without too much review, we'll have several articles. We had talked about building a strategy targeting AI visibility. I know you have constraints around discussing competitors and building comparison content. For that strategy, how much do you want us to operate within those constraints versus making the case for pushing against them?

**Brooke Grief:** I think it would be great to show both. Here's content we could do within the competitor-mention constraint that we think could help with LLM visibility, and then: if we went full comparison content, here's the proven result we'd expect. We could show them we can do it. But ideally, the ideal state is being able to outright mention competitors.

**Bailey Seybolt:** That makes sense. I'll treat it that way. One thing our CEO is very good at is getting buy-in at the executive level. He had conversations with your former CMO about what content can do. I wondered if bringing him in to tell that story at the top level might be useful.

**Brooke Grief:** I don't think it's a problem of them not understanding the value of content. They just want to know: why aren't we number one everywhere? And they know content is the channel. They're looking for: what did we publish and how is it showing up in LLMs? If there's any documentation on that, it would help me in conversations. The person we'd bring in is Justin—he's a defender of content and goes to bat with execs. Any resources you could share would be great to have in my back pocket.

**Bailey Seybolt:** Absolutely. When we build the AI visibility strategy, we can tell that broader story within it.

**Brooke Grief:** Yeah, even just saying: we're not showing up here, here's the blog post that would help, we'll create it and it'll be live. Showing them the gap, solution, and timeline, then reporting back with results. That's what they're looking for.

**Bailey Seybolt:** Do these two personas still feel right for the gaps?

**Brooke Grief:** Yes, definitely. For LLMs, it'll probably lean toward bottom-up motion—developers looking for answers on APIs and technical stuff. That might lean more technical, but at least I'll have the context to support it with SMEs: we're not ranking on LLMs, this will help, and it'll speed things up.

**Bailey Seybolt:** That makes sense. And if you're blocked on getting things published because of SME review, making that case could help unblock it.

**Brooke Grief:** Definitely. Going back to strategy: white papers aren't necessarily bottom-up and blogs aren't necessarily top-down. That evals one is bottom-up, but there are other ones in Notion that are more top-of-funnel. As long as we're not leaning heavily on SMEs and it's coming from existing content, that works.

**Bailey Seybolt:** That makes sense. I think those were my main questions. We'll build out the strategy and deliver it—usually in a Notion doc. Would a PowerPoint presentation be helpful, or is Notion fine?

**Brooke Grief:** Notion is fine.

**Bailey Seybolt:** On Check That—did you have any issues with access or a chance to look?

**Brooke Grief:** I haven't yet. Should I have an invite?

**Bailey Seybolt:** You should have one in your inbox. I've had a couple clients have issues, so let me resend it.

**Brooke Grief:** I found it—trying to log in. All right, I'm in.

**Bailey Seybolt:** Great. I just wanted to make sure that worked. I also talked to Brandlight—said GrowthX is building their own thing and to step it up. They introduced a feature called Impact, where you can search specifically by URL to see how it impacts citation percentage and visibility.

**Bailey Seybolt:** We have a Source section where you'll see top-cited URLs and can search by URL to see your own top-cited content. That's a great way to keep an eye on trends. For instance, there are quite a few lists about top platforms for enterprises, enterprise AI platform guides.

**Brooke Grief:** It's like a fraction of a percentage.

**Bailey Seybolt:** Exactly. Does it show which engine specifically?

**Bailey Seybolt:** It doesn't there, but if you go into your prompts, you'll see what's cited across each engine. That's a good question—I'll capture it for our dev team. We have a list of new features and filters to build, so that would be helpful.

**Brooke Grief:** If you want to dig in at the level of platform, here's the place. I know Brandlight has a weighted visibility score based on platform traffic—ChatGPT is visited most, so they weight that more heavily. Is that in the queue or already accounted for?

**Bailey Seybolt:** That's interesting. I'll check if it's on the roadmap. I don't think it's accounted for now, but I'll look.

**Brooke Grief:** Yeah, this is super helpful. It feels much more user-friendly than Brandlight. You basically take a list of prompts you should show up for, run them through, and see where you actually are.

**Bailey Seybolt:** Right. We track what we think is relevant based on your goals and personas. If you want additional ones, you can create custom prompts and tag them to funnel stage. Or use our shared library of vetted, relevant prompts for your category and adjacent ones. These collect historical data.

**Brooke Grief:** The nice thing is they're vetted and pre-populate with 30 days of data, so you don't wait a week for signal. Custom prompts would take a bit?

**Bailey Seybolt:** They usually show up within 24 hours, but depending on specificity, a few days for real signal.

**Brooke Grief:** Is it exportable?

**Bailey Seybolt:** Unfortunately, prompts aren't exportable yet—it's on the roadmap. But I linked you a spreadsheet with all current prompts. It's easier to review there, leave comments, and add new ones. I'm happy to add them for you.

**Brooke Grief:** That's incredible.

**Bailey Seybolt:** You can also add more competitors. We're tracking certain ones now, but you can add more professional competitors, and as you add products, features, or focus on different personas, you can update context to ensure it pulls the right info about your company.

**Brooke Grief:** Is there a limit on how many people from You.com can be added?

**Bailey Seybolt:** Good question. I've added about 10 from a team without hitting it, but I probably shouldn't say that.

**Brooke Grief:** I don't want everyone in there.

**Bailey Seybolt:** In that case, yes, there's definitely a strict limit. If you want to invite others, you should be able to. If not, drop their email in Slack and I'll add them.

**Brooke Grief:** Thanks. If you already sent it, I apologize, but a Loom walking through features for me to share with the team?

**Bailey Seybolt:** I sent one last week, but I can resurface it in Slack—it was in the weekly update, probably buried.

**Brooke Grief:** I appreciate that. I'll share it with the team. As you look at prompts, I'm happy to answer questions and review, especially given changes in focus and personas. We'll want to make sure we're not missing anything important.

**Bailey Seybolt:** Yeah, that sounds great. I do a monthly report pulling from Brandlight. Next week for February's, I'll use this too to test-run and compare data and ease of use. I'm sure I'll have questions.

**Brooke Grief:** Do you have your Brandlight prompt list? Can you export it?

**Bailey Seybolt:** No, certainly not.

**Brooke Grief:** They do on Scrunch. It's a very engineering-developed platform. If those are refined and you know what to track, we could run a check to see gaps between what you're tracking there and what we're tracking on Check That.

**Bailey Seybolt:** They have 3,200 prompts tracking now.

**Brooke Grief:** Do you feel you're getting useful signal?

**Bailey Seybolt:** No. They have "query importance" marked as low, low, low. I'm like: why are we tracking this? Exactly. It's interesting. The opposite challenge is Scrunch—a total green field where you create all your own prompts. You have to know exactly what you want, and it takes weeks to get signal. So the goal here was in between: customize and refine, but with a starting point of vetted data. As you get in, let me know if there are features you wish you could see. This was useful feedback for the roadmap.

**Brooke Grief:** I'll definitely share that. Did GrowthX build the actual tech going out and querying LLMs and pulling information, or is it through a third party?

**Bailey Seybolt:** We have a product team and dev team just working on Check That. I don't know exactly what models they use, but it's all custom work they built over four to six months.

**Brooke Grief:** That's cool. I was curious if it was all pulled from SEMrush—whether all these tools use the same data but display it differently.

**Bailey Seybolt:** You never know, but no, it's all custom.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** So in terms of pipeline status, I took a look at the topics you approved and I prioritized the 10 that wouldn't need any SME review because I figured that would buy us that runway and hopefully let us get some content live and published while we're kind of figuring out some of the other shifts in strategy that seemed like So my plan is to focus on those for now.

**Bailey Seybolt:** We do have the other white paper topics too, which would be great for targeting that technical persona.

**Bailey Seybolt:** But I'm sort of loathe to jump into those until you or your SME have a chance to review those two that we already did.

**Bailey Seybolt:** Just in case you have any flags there, I don't want us to get into a situation.

**Bailey Seybolt:** Excellent.

**Bailey Seybolt:** Thank

**Bailey Seybolt:** Like we did before, where you're sort of then going back and adjusting the pipeline and then rerunning tons of content for you to review.

**Bailey Seybolt:** So I feel like it might be better to hold off on those until you have a chance to calibrate on those first two posts.

**Brooke Grief:** Which two, sorry, are for?

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** Here, let me pull up your table.

**Bailey Seybolt:** It is.

**Bailey Seybolt:** So of the ones in review, you'll see it's marked as article type.

**Bailey Seybolt:** These two at the bottom are from the white paper.

**Brooke Grief:** Okay.

**Bailey Seybolt:** And there should be a link to the source here at the top.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** So you can reference back as well as the keyword that we scraped from that.

**Brooke Grief:** Perfect.

**Brooke Grief:** Those will take a bit to get reviewed, but I will make sure that we can.

**Brooke Grief:** And put them in front of the right people, at least.

**Bailey Seybolt:** Okay, great.

**Bailey Seybolt:** So my hope there is because, in general, this pipeline has performed pretty well, in my experience, when it has, like, a good source document.

**Bailey Seybolt:** So my hope is that it's minimal feedback and that, hopefully, that might be a lane that we can continue to publish in without needing too much intensive SME review.

**Brooke Grief:** Yeah, do also think, like, if we, another option to explore is more of what I was talking about of just separating the white papers and, like, truly verbatim or, like, you know, touching up slightly to make it read like a blog.

**Brooke Grief:** But that obviously would not need a review since it's already live.

**Brooke Grief:** So that could help speed stuff up as well.

**Brooke Grief:** But obviously, these are great topics.

**Brooke Grief:** I just, you know, I fear the same delay with SMEs versus just, like, taking what we already have and breaking it up.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** I'll take a look at the white papers.

**Bailey Seybolt:** I mean, I'm sure that depends a lot.

**Bailey Seybolt:** A bit on how their format, have you, do you have anyone in mind that you feel like would be particularly good?

**Brooke Grief:** The emails one actually has, like, a framework where each of the sections could be split out.

**Bailey Seybolt:** Yeah, okay.

**Brooke Grief:** And that could be something, like, let me see if I can, yeah, so, like, it has the framework, and there's four-phase evaluation methodology, like, that could be its own thing, or, like, what makes search evaluation so hard?

**Brooke Grief:** That could be a blog post, like, the bigger chunks of it each could be their own thing.

**Bailey Seybolt:** Yeah, I think that's definitely something we could do.

**Bailey Seybolt:** I think especially if it's already pre-structured that way, and then we could just have stronger guardrails in place in terms of breaking it up versus, like, scraping it to create new content.

**Bailey Seybolt:** I think we just have to see if it made sense from a keyword perspective, like, if those, if the parts that felt distilled.

**Bailey Seybolt:** We're also, we could like validate them with keyword information.

**Brooke Grief:** Yep, totally.

**Bailey Seybolt:** Okay, that sounds good.

**Bailey Seybolt:** I'll send that one to our editorial team just with those guidelines in mind and see if we can create a version for that one in particular that really just was breaking up that piece and not changing anything that would trigger SME review.

**Brooke Grief:** Cool.

**Brooke Grief:** Yeah, that sounds great.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** All right.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** I think there are 10 published.

**Brooke Grief:** I think I looked today and there are 10 now.

**Brooke Grief:** So I didn't just try not to move this over.

**Brooke Grief:** So cruise in.

**Bailey Seybolt:** We got something.

**Bailey Seybolt:** Definitely.

**Bailey Seybolt:** Sorry.

**Bailey Seybolt:** Wow.

**Bailey Seybolt:** You just, you just triggered my Siri.

**Bailey Seybolt:** It must sound like, you know, yes.

**Brooke Grief:** Yes.

**Bailey Seybolt:** Type label.

**Bailey Seybolt:** I'll do that too in Airtable to flag the blog, like the blog persona as well.

**Bailey Seybolt:** I don't want to add like another column for you to look at, but I think I can just differentiate between like the blog personas that you're looking at too.

**Brooke Grief:** So it's easier to see at a glance.

**Brooke Grief:** Yeah, that would be great.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** So in terms of strategy, I just kind of wanted to confirm with you that this feels like the right direction to go for now.

**Bailey Seybolt:** I think for now, focusing on the AI laggard persona, and I think those were the initial keywords, but we'll build out that research so you have more topics to choose from.

**Bailey Seybolt:** And then the white paper breakdown.

**Bailey Seybolt:** And then those, I think, once you review with SME, those initial ones, and then hopefully this additional one we can do without too much review, that'll sort of be a few articles there.

**Bailey Seybolt:** And then the other thing I wanted to touch base with, um, was around, I

**Bailey Seybolt:** We had talked last time around building a strategy that targets AI visibility, and I was wondering a couple things.

**Bailey Seybolt:** One, I know that you as the marketing team have these constraints around, especially, particularly around discussing competitors and building out comparison content, which obviously also affects, I could talk about use cases.

**Bailey Seybolt:** I'm wondering, for building out that strategy, how much do you want us to kind of operate within those constraints, or how much do you think it makes sense to make the case for why we should kind of push against those constraints, if it makes sense?

**Brooke Grief:** Yeah, I think it would be great to show both, honestly, of like, here's, given the feedback that we've heard, we can't, you know, talk about competitors, here's the kind of content we could do that we think could potentially help us get LLM visibility.

**Brooke Grief:** on.

**Brooke Grief:** All right.

**Brooke Grief:** All

**Brooke Grief:** That being said, you know, if we were to go full, you know, comparison content, this is a proven and this is what we would see as a result of that.

**Brooke Grief:** And then it can show them like we could do it and like we still can and that's fine.

**Brooke Grief:** But ideally, the ideal state is being able to outright mention competitors.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** I think that makes sense.

**Bailey Seybolt:** So we'll treat it that way.

**Bailey Seybolt:** And then my other question here was, I'm wondering, it sounds like there's some like just from the top, like you're getting, you know, multiple kind of directions, right?

**Bailey Seybolt:** Like being number one in AI visibility versus not being able to mention your competitors.

**Bailey Seybolt:** One thing our CEO, I think, is very good at is sort of just getting, I think, buy-in at that, at the executive level on strategy and kind of what content can do for a company.

**Bailey Seybolt:** And I know that he had some of those early conversations with your CMO who's no longer there.

**Bailey Seybolt:** Like I'm wondering if bringing him in to do some of that storytelling around AI visibility at that top level feels like something that might be useful for getting kind of buy-in for your team.

**Brooke Grief:** I don't know because I don't think it's a problem in terms of them not understanding the value of content.

**Brooke Grief:** I think it's just them being like, why aren't we number one everywhere?

**Brooke Grief:** Let's be number one everywhere.

**Brooke Grief:** And like they know that content is the channel to do it.

**Brooke Grief:** They're just looking for like, okay, what did we publish and how is it showing up in LLMs?

**Brooke Grief:** I mean, that stuff from him would be helpful for me.

**Brooke Grief:** Like if there is any documentation on that, that would be helpful to just, I can use that in conversation.

**Brooke Grief:** But the person that we would bring in is Justin and he's also like very much a defender of content and knows the value.

**Brooke Grief:** You

**Brooke Grief:** So he's been going to bat for it when it comes to execs.

**Brooke Grief:** So I don't think it's totally necessary now, but any resources that you could share over with me would be great.

**Brooke Grief:** And then I can just have those in my back pocket in case.

**Bailey Seybolt:** Yeah, 100%.

**Bailey Seybolt:** So, yeah, it sounds like then maybe like when we do building that strategy around AI visibility and then kind of telling some of that broader story within that could be the most useful thing to handle.

**Brooke Grief:** Yeah, even just saying like, hey, you know, we're not showing up here.

**Brooke Grief:** This is the blog post that would help do that.

**Brooke Grief:** And so we're going to create that blog post and it'll be live.

**Brooke Grief:** Like that, showing them like, here's a gap, here's a solution, and this is when it'll go live.

**Brooke Grief:** And then later, obviously, reporting back and saying like, here's the result of that.

**Brooke Grief:** Like that, I think, is really what they're just looking for.

**Bailey Seybolt:** Yeah, okay.

**Bailey Seybolt:** That makes sense.

**Bailey Seybolt:** And do you feel like, given our focus, like, do these still feel like the two right personas to focus on for those gaps?

**Brooke Grief:** Yes, yeah, definitely.

**Brooke Grief:** think it'll probably, for LLMs, it'll probably

**Brooke Grief:** Probably lean more towards the like bottom up motion of just like developers looking for answers on APIs and all of that technical stuff.

**Brooke Grief:** So it might lean a little bit more technical, but if that's the case, at least I'll have the context to support it when going to SMEs of like, hey, we need this turned around.

**Brooke Grief:** You know, we're not ranking on LLMs and this is going to help us and that'll hopefully speed it up.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** That makes sense.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** That was going to be my next question.

**Bailey Seybolt:** And then if it feels like, you know, if you're blocked from a content perspective on getting things published for SME review, it sounds like making that case could help unblock that for publishing too.

**Brooke Grief:** Definitely.

**Brooke Grief:** Yeah.

**Brooke Grief:** And I also think just going back up to that strategy, that first section, the white papers aren't necessarily always bottoms up and blogs aren't necessarily always top down.

**Brooke Grief:** Um, that evals one is just a bottom up one that we have, but there's other ones in notion that you'll find are definitely more top of funnel, but I think that's fine.

**Brooke Grief:** Okay.

**Brooke Grief:** Um,

**Brooke Grief:** And some of the stuff, it'll, wherever the audience's fault, based on that stuff, I think it's fine as long as, you know, we're not leaning heavily on SMEs and it's coming from existing content for Bottoms Up, then that works.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** I think that makes sense.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** I think those were basically my questions on how to approach this.

**Bailey Seybolt:** So we'll take that and then I'll touch base with our team, but my hope would be that we can kind of build out that strategy and then deliver it to you.

**Bailey Seybolt:** Usually we just do this in a Notion doc.

**Bailey Seybolt:** Would it be useful for you?

**Bailey Seybolt:** Like, I know you're sort of trying to make the case.

**Bailey Seybolt:** Would it be helpful for you to pull together a presentation, like more of a PowerPoint as well, or just Notion doc for now?

**Brooke Grief:** I think Notion is fine.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** And then the only other thing I had a question on was, check that.

**Brooke Grief:** If you had had any issues with access or if you had a chance to take a look at all.

**Brooke Grief:** I have not.

**Brooke Grief:** Should I have an invite somewhere?

**Bailey Seybolt:** You should have had an invite in your inbox.

**Bailey Seybolt:** I've had a couple clients having an issue getting access from their invite.

**Bailey Seybolt:** So here I am just going to resend it to you.

**Brooke Grief:** So it's.

**Brooke Grief:** I found it and I'm trying to do.

**Brooke Grief:** To log in.

**Brooke Grief:** I agree.

**Brooke Grief:** Except.

**Brooke Grief:** All right, I'm in.

**Bailey Seybolt:** Okay, great.

**Bailey Seybolt:** I just want to make sure that that was.

**Brooke Grief:** Sweet.

**Brooke Grief:** I just also talked to Brandlight and was like, by the way, growthx is building their own thing.

**Brooke Grief:** So if you guys want to step it up, I welcome you to the challenge.

**Brooke Grief:** And they introduced a.

**Brooke Grief:** A new feature called Impact, which shows like you can search specifically by URL of how it is impacting citation percentage and visibility of the brand as a whole.

**Brooke Grief:** So I thought that was interesting.

**Brooke Grief:** So they're trying.

**Bailey Seybolt:** We do have also like a source you'll see and you'll be able to see like the top cited URLs across your prompts.

**Bailey Seybolt:** And you can also search by URL too, like if you want to see what are your own also top cited content.

**Bailey Seybolt:** So that's a great way to kind of keep an eye on that.

**Bailey Seybolt:** And also to keep just an eye on the trends like we were talking about.

**Bailey Seybolt:** You know, a lot of these comparison articles, best AI agents, you'll see, you know, for you, there's quite a few lists talking about top platforms for enterprises.

**Bailey Seybolt:** I noticed there's lot of enterprise AI platform guide.

**Bailey Seybolt:** past.

**Bailey Seybolt:** I I there's

**Bailey Seybolt:** It's a very, like, low rate compared to the full number.

**Bailey Seybolt:** So it's like essentially saying it's like a, it's a percentage.

**Brooke Grief:** It's like a fraction of a percentage.

**Brooke Grief:** Got it.

**Brooke Grief:** Okay.

**Brooke Grief:** Interesting.

**Brooke Grief:** Yeah, this is, this is super helpful.

**Brooke Grief:** And does it anywhere show which engine specifically?

**Bailey Seybolt:** So here, whoops, nope.

**Bailey Seybolt:** If you go, I think it doesn't there, but if you go into your prompts specifically there, you'll be able to see, like, what's being cited across with engine.

**Bailey Seybolt:** But that's, that's actually a good question, which I should capture and share with our dev team because they're always looking, we have a list of new features and filters to build.

**Bailey Seybolt:** So that would be a helpful one.

**Brooke Grief:** But yes, I think if you want to dig in at the level of platform, here is the place to do it.

**Brooke Grief:** Okay.

**Brooke Grief:** And then I know Brandlight also has a weighted visibility score option where it's like dependent on the number or the traffic that these different AI platforms get.

**Brooke Grief:** They obviously like ChatGPT is visited the most.

**Brooke Grief:** So if we're present on ChatGPT, they weight that more heavily.

**Brooke Grief:** I'm curious if that's in the queue or if that is already taken into account here.

**Bailey Seybolt:** Yeah, that's interesting.

**Bailey Seybolt:** I think I'll check and see if that's on the roadmap.

**Bailey Seybolt:** I think it is not taken into account now, but I'd be curious if that's on our roadmap or not.

**Brooke Grief:** So I can check on that for you.

**Brooke Grief:** Cool.

**Brooke Grief:** Yeah, no, this is great.

**Brooke Grief:** I mean, it already feels a lot more user-friendly, which is sort of what I was lacking or am lacking on Brandlight.

**Brooke Grief:** And it's basically just you take a list of prompts that you think we should be showing up for, run those through, and determine where we actually are showing up.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** That we're tracking for you that, like you said, we just decided what we thought was relevant based on your goals and personas.

**Bailey Seybolt:** You, if you have additional ones you want to add, you can either create custom prompts and then you can just input them and tag them to the funnel stage.

**Bailey Seybolt:** You can also go in and we have a shared library of prompts, which is basically what we've created, what we think is most relevant for the category that you're in and then adjacent categories.

**Bailey Seybolt:** And any of these, you can just check and add and these will be collecting historical data.

**Brooke Grief:** So the nice thing about these is A, they've already been vetted and then B, they usually pre-populate with like 30 days worth of data.

**Bailey Seybolt:** So you don't have to, you know, often you're waiting a week to see if you're getting any signal.

**Bailey Seybolt:** So that's the other way to do it is to go through and think about what if these feel relevant.

**Brooke Grief:** So custom prompts would take a bit to just.

**Bailey Seybolt:** Yeah, like, they'll usually show up within 24 hours, but depending on how specific they are, like, they can take a few days to get any, like, real signal there, I would say.

**Brooke Grief:** Got it.

**Brooke Grief:** Okay.

**Brooke Grief:** And is this exportable at all?

**Bailey Seybolt:** Yes.

**Bailey Seybolt:** So, unfortunately, the prompts are not exportable.

**Bailey Seybolt:** That is definitely on the roadmap.

**Bailey Seybolt:** But I did, in Notion, link you.

**Bailey Seybolt:** I did pull them out.

**Bailey Seybolt:** So, there are, I did link you to a spreadsheet that has all of the current prompts in them now, because I think it's so much easier to review there.

**Bailey Seybolt:** So, if you want to go in, you can leave comments on the spreadsheet.

**Bailey Seybolt:** You can, you know, add new prompts.

**Brooke Grief:** And I'm happy to take care of that, of adding them for you as well.

**Brooke Grief:** Incredible.

**Brooke Grief:** That's great.

**Brooke Grief:** Thank you.

**Bailey Seybolt:** And then the other thing would be competitors.

**Bailey Seybolt:** If you want to, you can continue to add other competitors.

**Bailey Seybolt:** So, this is who we're tracking right now, but you can add additional.

**Bailey Seybolt:** Professional competitors or, you know, competition as well as, you know, product.

**Bailey Seybolt:** And then context is as, you know, you add product and features or want to focus or not focus on different personas, you can update this here too to make sure it has pulling the right context about your company as well.

**Brooke Grief:** This is great.

**Brooke Grief:** Is there any limit to number of people that can be in there from U.com?

**Bailey Seybolt:** That's a great question.

**Bailey Seybolt:** Um, I've added like 10 people from a team and haven't hit the limit.

**Brooke Grief:** Okay.

**Bailey Seybolt:** I probably shouldn't say that because, you know, then you can add your entire company and I'm going to get in trouble.

**Brooke Grief:** I actually don't want everyone in there.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** Um, in that case, yes, there's definitely a strict limit.

**Brooke Grief:** Um, Yeah.

**Brooke Grief:** I'll tell them that.

**Brooke Grief:** No, I was just thinking like, I'll invite Justin.

**Brooke Grief:** And then I like marketing ops person was curious about the tool as well.

**Bailey Seybolt:** I I already added Justin.

**Bailey Seybolt:** Um, yeah, if there's anyone else, I think you should be able to invite.

**Bailey Seybolt:** But if you can't just drop their email into Slack and I will add them.

**Brooke Grief:** Incredible.

**Brooke Grief:** This is great.

**Brooke Grief:** And then, yeah, if there is, I don't know if you sent it already, so I apologize, but a loom just like kind of high level walking through some of these features that I can then share.

**Bailey Seybolt:** I did send a loom last week, but I can just resurface it on Slack because I think it was in the weekly update.

**Brooke Grief:** So it's probably just a little bit buried.

**Brooke Grief:** Sorry.

**Brooke Grief:** Yeah, I will be better about that.

**Brooke Grief:** But I appreciate if you could just resurface and I'll share it out with the team.

**Brooke Grief:** No problem.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** And as you get in there and you look at your prompts, you know, I'm happy to answer additional questions and like take a look at those, especially I think given that there's been some change in like your focus and your personas.

**Bailey Seybolt:** I'm sure we'll want to take a look at those and make sure we're not like missing anything that feels important.

**Brooke Grief:** Yeah, that sounds great.

**Brooke Grief:** And I generally do like a monthly report where I'll pull some stuff in that I usually pull from Brandlight.

**Brooke Grief:** So next week when I do February's report.

**Brooke Grief:** I'll use this as well to sort of test run and see how the data looks compared to Brandlight and like for ease of use and stuff.

**Brooke Grief:** So I'm sure I'll have some like questions and thoughts as I do that, but it'll be a really helpful test run.

**Bailey Seybolt:** Do you have a list of prompts tracking on Brandlight?

**Brooke Grief:** Do they let you export them?

**Brooke Grief:** Oh, certainly not.

**Bailey Seybolt:** They do on Scrunch, so I wasn't sure.

**Brooke Grief:** No, it's like, it's a very engineering developed platform that I find.

**Bailey Seybolt:** Yeah, I was gonna say we could, like, if those are really refined and you know what you want to be tracking, we can also just run a check to see if there are gaps between what you're checking, what you're tracking there and what we're tracking on Check That.

**Brooke Grief:** They have 3,200 prompts in their tracking right now, so.

**Bailey Seybolt:** And do you feel like you're getting useful signal there?

**Brooke Grief:** No.

**Brooke Grief:** Well, one is.

**Brooke Grief:** have like query importance and it's like low, low, low, low, low.

**Bailey Seybolt:** And I'm like, okay, so why are we tracking this query?

**Bailey Seybolt:** Yeah, exactly.

**Brooke Grief:** Okay, that's fine.

**Brooke Grief:** But then I don't care.

**Bailey Seybolt:** Yeah, it's interesting.

**Bailey Seybolt:** Scrunch-Rum was the challenge there is the opposite.

**Bailey Seybolt:** It's a total green field because you have to create all your own prompts.

**Bailey Seybolt:** And so it's like you have to kind of know exactly what you want and what to do.

**Bailey Seybolt:** And then it takes, you know, weeks to get any signal.

**Bailey Seybolt:** And so I think from there, it's like the opposite problem.

**Bailey Seybolt:** You've got the blank slate.

**Bailey Seybolt:** But so I think this, the goal here was to make it a little bit in between where you have the ability to customize them and refine them, but also have a starting point of like vetted data.

**Bailey Seybolt:** So as you get in there, let me know if you, like this was actually a really useful conversation because clearly there's some features you're looking for that we don't have, which I feel like is always the best feedback to pass on to help build out the roadmap.

**Bailey Seybolt:** So I would love to, as you get in there, if there are things you wish you could see that if you can't.

**Bailey Seybolt:** Definitely.

**Bailey Seybolt:** Definitely share that with us.

**Brooke Grief:** Oh, yeah, I will.

**Brooke Grief:** And is this like, did you, did GrowthX build the actual tech that's like going out and putting the queries into these LLMs and pulling all the information as a result?

**Brooke Grief:** Like how, or is it being just through another third party?

**Bailey Seybolt:** We have a whole product team and like a dev team that are just working on Check That.

**Bailey Seybolt:** In terms of what they used versus like what models they pull from, that I don't 100% know the answer to, but it is all like custom work that they built over the course of like four, four to six months, I want to say.

**Brooke Grief:** Yeah, that's super cool.

**Brooke Grief:** And I was just curious if was like all being pulled from SEMrush and like all these different tools are all using SEMrush and it's like, you know, are we all looking at the same data and just different?

**Bailey Seybolt:** Yeah, I was just curious because you never know.

**Bailey Seybolt:** No, I should, I should.
