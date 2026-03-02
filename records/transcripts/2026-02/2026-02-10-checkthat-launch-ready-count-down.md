# CheckThat: Launch Ready Count Down

<metadata>
date: 2026-02-10
time: 15:58 UTC
duration: 32 minutes
organizer: stevie@growthx.ai
participants: Marcel Santilli, Daniel Lopes, Pedro Steimbruch, Jose Farias, Estevão Mascarenhas, Stevie Kim
fathom_recording_id: 121198985
fathom_url: https://fathom.video/calls/561192080
share_url: https://fathom.video/share/KHJJjeNgxSpGVi639ZQ6_BZyg2dCnzgz
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

The CheckThat team aligned on transitioning from pre-launch sprint mode to a more structured post-launch process. Key decisions included adopting a "shaping" methodology to reduce rework from ad-hoc changes, decoupling the core UX from subcategory accuracy by treating subcategories as non-critical tags, replacing daily standups with async Slack updates and a weekly technical sync, and establishing a weekly Friday strategy meeting for Daniel, Marcel, and Stevie. Stevie will tag all work in Linear using P0/P1 priority labels aligned with Daniel's prioritization list.

---

## Context

CheckThat is GrowthX's B2B software product for AI visibility indexing. The team had just completed the public launch countdown and is now working on stabilizing and improving the product based on initial user feedback and internal priorities. This meeting brought together the engineering leads (Jose, Pedro, Estevão) and product leads (Stevie, Marcel, Daniel) to reset operating cadence and align on priorities for the weeks ahead. The team had been operating in sprint mode to hit the launch deadline, but Daniel recognized the need for more structured decision-making going forward to prevent the chaos of ad-hoc product changes.

---

## Relevance

**To CheckThat Development:**
- Subcategory accuracy problem is architectural and needs immediate attention. Will shift from a critical dependency to a filtering tag, reducing perfection requirements while still improving accuracy where possible.
- Filters on the overview screen are now P0 (Marcel's top request). Implementation requires re-enabling competitor/prompt performance snapshots, with storage offset by removing subcategory snapshots.
- PostHog release tracking needs implementation to measure impact of the new onboarding flow and subcategorization changes.
- Prompt suggestions investigation (Pedro) presents opportunity to reduce reliance on subcategories and improve initial user experience.

**To GrowthX Process:**
- Team adopting Shape Up methodology (Ryan Singer) with Claude AI skills to accelerate product planning and reduce rework from ambiguous specs.
- Shift from unstructured daily standups to async Slack updates + weekly technical sync is expected to improve documentation for future team members and AI agents.
- Friday strategy meetings will be intentionally high-level and "messy" (Daniel/Marcel/Stevie). Stevie will translate decisions into technical specs for engineering team during weekly sync.

---

## Overview

- **Process Shift:** Adopting a structured "shaping" process to reduce rework from ad-hoc changes. Daily stand-ups will be replaced with async updates and a weekly sync.
- **Subcategory Strategy:** Subcategories will become a non-critical "tag" for filtering, decoupling core UX from their accuracy. This enables a faster, less error-prone user experience.
- **Priority Alignment:** All work must align with Daniel's new priority list (shared in Slack), which Stevie will tag in Linear as P0/P1 to provide clear visibility.

---

## Key Topics

### Process & Cadence

  - **Problem:** Unstructured work, like Daniel's recent ad-hoc onboarding changes, causes rework and makes building a consistent mental model difficult.
  - **Solution:** Adopt a "shaping" process for more upfront planning, balancing speed with reduced rework.
      - **Goal:** Define the problem, opportunity, and solution before implementation.
      - **Tool:** Use Ryan Singer's Claude skills for shaping to accelerate the process.
  - **Meeting Cadence:**
      - **Daily Stand-ups:** Replaced with async updates in Slack.
      - **Weekly Sync:** A longer, weekly meeting will replace daily stand-ups for technical alignment.
      - **Friday Strategy Meeting:** Daniel, Marcel, and Stevie will meet; others can join but should expect a high-level, unstructured discussion.

### Subcategory Strategy

  - **Problem:** The core UX is too dependent on perfect subcategory accuracy, which is difficult to achieve from limited data (e.g., a vague homepage).
  - **Solution:** Decouple the core UX from subcategories by treating them as a non-critical "tag" for filtering, not a core architectural component.
  - **Implementation:**
      - **Estevão:** Shipping a basic research workflow to improve subcategory accuracy for \~30 brands.
          - **New Onboarding:** Users will see all suggested subcategories and can remove irrelevant ones.
          - **Tracking:** Needs a Post-Hog plan to track changes made by this new flow.
      - **Pedro:** Investigating prompt suggestions as a way to further reduce reliance on subcategories.

### Current Priorities & Updates

  - **Jose:** Implementing filters on the overview screen (a high priority for Marcel).
      - **Technical:** Requires re-enabling snapshotting of competitor/prompt performance, which was previously removed to save storage.
      - **Trade-off:** This is offset by no longer needing to snapshot subcategories, as the categories chart was removed.
  - **Pedro:**
      - Shipped: Pagination for sources page, timezone handling for charts, and on-demand sitemap regeneration to S3.
      - Next: Investigate prompt suggestions.

---

## Action Items

**Stevie Kim (GrowthX)**
- Review Daniel's onboarding/subcategorization shaping doc; post clarifying questions in comments
- Tag Linear tickets P0/P1 per Daniel's prioritization; update labels to P0/P1

**Jose Farias (GrowthX)**
- Share Ryan Singer's Shape Up Claude skills in Slack channel
- Re-enable snapshotting of competitor and prompt performance for onboarding overview filters

**Estevão Mascarenhas (GrowthX)**
- Investigate PostHog release tracking for onboarding flow changes

---

## Transcript

**Stevie Kim:** Before we get started, I just wanted to ask a couple things about the launch milestones. So Daniel removed the launch milestones, but the labels still exist. But I think I'm probably just going to change those to, instead of "launch P2", just a regular P2. He, yeah, we talked about retiring the project or, you know, closing the project out and starting a new one. But for now, I think we're just going to use the same project because we're not really using projects in any way that matters. But anyway, I just wanted to let you guys know I'm going to be fiddling with the labels a little bit, but I'm trying to give you guys a little bit more visibility into priorities. I mean, I think we've been fine up until now because we had a very clear idea what were priorities, but now it's getting a little bit more vague. So I'm going to try to organize the board a little bit better. I already moved some of the growth ones out from "To Do" to "Backlog" because there were just so many.

**Stevie Kim:** And then also Daniel had me remove the second meeting on Monday, so like the second check-in. Him, Dan, or him, Marcel, and I are going to meet on Friday, but he said that anyone can join. It's just going to be a messy meeting, like yesterday was, he said. So kind of a messy strategy meeting instead of, you know, more technical. And then I wanted to see if you guys wanted to keep the daily stand-ups or do them less often.

**Jose Farias:** I don't mind the stand-ups. That said, I do think the technical discussions that have been happening in stand-ups would have happened anyway, async. Like I feel like all of us on the team were diligent enough that we know when we need to have a conversation and we can just write it down. And I actually kind of think that's better for transparency with the whole team and also, with all the AI stuff, right? Like if we write it down, then we can point agents to it and be smart about things. So no strong feelings on the check-ins. I do think we can do without them, maybe one weekly one if we're comfortable with that. The other thing I'd like to add is sort of tangential to this conversation, so we can pick this back up later, but.

**Jose Farias:** There were some, I don't want to say major changes, well, were kind of major changes done by Daniel last night to the onboarding and the changing the overall strategy to not rely that much on categorization.

**Jose Farias:** Good changes, but I feel they're a consequence of not spending enough time in shaping.

**Jose Farias:** So more than daily cadence of a daily cadence of like what's going on, what's everyone working on, think we would benefit from more structured, less chaotic strategizing to your point about yesterday's meeting being a little bit unstructured.

**Stevie Kim:** Yeah, yeah, a hundred percent.

**Stevie Kim:** a hundred percent.

**Stevie Kim:** So first, I want to clarify, did you mean, by changes, do you mean, like, you know, like, he made changes already to the workflow in prod, or he created a shaping doc laying out his thoughts on what changes we need to push into production?

**Jose Farias:** I believe it started as a doc, and then he actually pushed the changes, which is fine, like, it's not a problem or anything, and they're good changes, like, it's just that trying to balance the rework, right, or moving fast, and then Daniel's going in and, like, having to, like, spend long nights changing things.

**Jose Farias:** A hundred percent.

**Stevie Kim:** So, so typically, what I've done in the past, when I've done product is, there's a lot more upfront work, you know, I typically...

**Stevie Kim:** You know, like, so what I was doing, for instance, with the categorization, so laying, laying out, okay, this is the problem.

**Stevie Kim:** These are the problem statements.

**Stevie Kim:** Here's some opportunities.

**Stevie Kim:** This is why we think this is important.

**Stevie Kim:** And then once we all can kind of align on, okay, well, these are the most important ones to capture, you know, to target right now.

**Stevie Kim:** We flesh those out a little bit and have, like, more of a technical discussion and, you know, engineering is always in those, you know, discussions and stuff.

**Stevie Kim:** And then once we kind of figure out a solution together, you know, kind of write that out a little bit more detailed.

**Stevie Kim:** So, you know, you guys have, like, because I'm used to working with QA teams, too.

**Stevie Kim:** So there has to be, like, acceptance criteria and everything.

**Stevie Kim:** But, yeah, so, you know, I mean, we can do, like, a version of that that's not, you know, so heavy.

**Stevie Kim:** But, absolutely, it's been really,

**Stevie Kim:** It's hard for me to build mental models of any of the decisions that have been made in the past, because there's, you know, nothing written down, really.

**Stevie Kim:** And so, and it helps me, like, I think through writing.

**Stevie Kim:** And so for me to not be able to write these ideas down also makes it really hard.

**Stevie Kim:** So I'm all for having more structure there.

**Stevie Kim:** And I think what my job is really gonna have to be here, because it is different in the way we're, you know, it's very top down, the decisions.

**Stevie Kim:** I'm going to be in those Friday meetings with Daniel and Marcel, letting them kind of hash things out.

**Stevie Kim:** And, you know, I'll bring things to attention, their attention that need to be, that meeting is just inherently going to be messy.

**Stevie Kim:** And I'm going to try to create some structure.

**Stevie Kim:** And then we can meet in maybe, like you said, a weekly meeting, maybe a little bit longer one than a half hour, because we'll need some time to talk about, you know, what we're going to, what, you know, what was prioritized in the Friday meeting and any kind of outlying questions that you guys might have.

**Stevie Kim:** And so I think, I think I need to be kind of a buffer, like, not a buffer, but like a, you know, translator in some sense, because I don't think some of those meetings are super useful for, for engineering, just because they are very high level, they're very messy, and they're not as technical.

**Stevie Kim:** So anyway, that's those are my thoughts.

**Stevie Kim:** Again, like, I mean, we move super fast, like you said.

**Stevie Kim:** And so I'm, I think like, what's going to be hard for me.

**Stevie Kim:** Is to understand like what is just enough, you know, on the shaping side.

**Stevie Kim:** Because I do tend to, I'm a heads down like deeper thinker versus like very move fast, random, you know, like multitasking and all of that.

**Stevie Kim:** And so I do tend to like go too deep on some things, which is great for like research work.

**Stevie Kim:** Not as good for, you know, just like writing a lightweight PRD that doesn't need a lot of, you know, research or, you know, so I think that's maybe what I'll need help from you guys with just like, okay, you know, just like, okay, this is good enough for us.

**Stevie Kim:** We understand like the why and Marcel and Daniel's vision of how things, you know, should be or could be and we can run with this.

**Jose Farias:** That sounds good.

**Jose Farias:** For what it's worth, I think.

**Jose Farias:** We can err on the side of less structure just because we've been operating with zero structure, basically, and things have been going okay, not perfect, but evidently we're an experienced team that's capable of tackling ambiguity.

**Jose Farias:** I think the more we shape, the less rework we'll have to do, and the less, I feel like it's relatively common that, for example, Marcel might go in the product and be like, none of this works the way I was picturing it, and so that'll happen less, but we'll also move slower.

**Jose Farias:** So, like, that's a balance to keep in mind.

**Jose Farias:** For what it's worth, less structure, I mean, I think results more rework, and I think that's okay as long as, like, is, like, okay with that kind of thing happening and not being super frustrated, like, the thing that shipped was, like, not ideal, which I think we've been.

**Jose Farias:** Okay.

**Jose Farias:** It's just like I know it can get grading if it happens for too long.

**Jose Farias:** Anyway, I feel like I derailed the conversation with bringing in the shaping stuff, but it's like it sort of like ties down into how much structure and recurring meetings we need.

**Jose Farias:** No, no.

**Stevie Kim:** It's something that's been on my mind a lot, too.

**Stevie Kim:** So I'm glad you brought it.

**Stevie Kim:** Cool.

**Jose Farias:** Curious to hear what others think.

**Jose Farias:** Pedro, any thoughts?

**Estevão Mascarenhas:** Yeah.

**Estevão Mascarenhas:** Regarding the stand-ups, I'm also okay.

**Estevão Mascarenhas:** Just a quick comment.

**Estevão Mascarenhas:** I'm okay.

**Estevão Mascarenhas:** Like for the technical discussions or maybe like more lengthy discussions, actually personal preference, I prefer a sync in the channel for the reasons Jose mentioned, like to have history and then we can use AI for that.

**Estevão Mascarenhas:** And also like I have more thought to organize my thoughts.

**Estevão Mascarenhas:** I have more time to organize my thoughts first before just saying a lot of unorganized.

**Estevão Mascarenhas:** But okay, yeah, I was thinking about this subcategorization.

**Estevão Mascarenhas:** I agree that we don't have too much structure.

**Estevão Mascarenhas:** Like we're discussing, at least like I watched this morning, both recordings yesterday.

**Estevão Mascarenhas:** And I think we were discussing like a really critical point of the product.

**Estevão Mascarenhas:** Because for me, the subcategorization, it was part of this intelligence contextual layer that we talk about.

**Estevão Mascarenhas:** Not just the brand data, but how do we group those brands?

**Estevão Mascarenhas:** And when I hear Daniel telling that we shouldn't be too tight to subcategory, my understanding is that we shouldn't, like the user experience shouldn't depend on the subcategory being right.

**Estevão Mascarenhas:** Because there are business that we won't have category for those.

**Estevão Mascarenhas:** But I don't think we're like subcategorization is going to go away.

**Estevão Mascarenhas:** We need to fix that.

**Estevão Mascarenhas:** And I was like, I'm working on the workflow that we subcategorize the brands.

**Estevão Mascarenhas:** Like it's a tricky problem because we only scraped the initial page of the company.

**Estevão Mascarenhas:** And I was checking the companies myself and I like lots of cases, like the page, the first, the homepage of those companies, they're very, very vague about what they do.

**Estevão Mascarenhas:** So we're trying to infer subcategorization from that data.

**Estevão Mascarenhas:** So, but at the same time, if we scrape lots of other pages, then it becomes like a lengthy workflow and we don't want the user to wait that much.

**Estevão Mascarenhas:** Yeah, sorry, just dumping out some thoughts that I was having that I'm not sure what's the best way to discuss this because I think this is really critical.

**Estevão Mascarenhas:** It's not just a matter of, okay, let's abandon subcategory because lots of things that we built are tied to those.

**Estevão Mascarenhas:** It's just like, should we fix it?

**Estevão Mascarenhas:** How we should fix it?

**Estevão Mascarenhas:** And I'm not sure, like I was, I'm a bit confused about that.

**Estevão Mascarenhas:** Like, should we, like what we are discussing in the first minute.

**Stevie Kim:** Yeah, I mean, I think, I don't think that there was ever the point where

**Stevie Kim:** Anyone said that they would go away.

**Stevie Kim:** was more that it would be less part of like the critical like architecture versus like, okay, just like a filter or a tag.

**Stevie Kim:** Like you put tags on your prompts and you filter by them.

**Stevie Kim:** That's not critical to how everything works together, how the system works together, right?

**Stevie Kim:** It's more isolated.

**Stevie Kim:** And I think he was talking more about how subcategories should be just kind of like a tag, a way that people group things to, you know, together, their prompts together.

**Stevie Kim:** So it was less of like, oh, they should just go away.

**Stevie Kim:** But yeah, making them, making things, I think, less dependent on getting them perfect because we're never going to get them right.

**Stevie Kim:** Right.

**Stevie Kim:** And so that, you know, there, there wasn't mention of that.

**Stevie Kim:** Getting rid of them.

**Stevie Kim:** was just less dependency on them for everything else.

**Stevie Kim:** But yeah, I think there's still quite a bit of ambiguity around that.

**Stevie Kim:** haven't had time.

**Stevie Kim:** Well, I haven't been awake for, not that I haven't had time, I haven't been awake for to look at a shaping doc.

**Stevie Kim:** And so I will take a look at that and see what changes, because I need to make sure I'm understanding, you know, what the vision, because I think one of the challenging things for me is that, you know, I was of the mind like, oh, this is how it was designed intentionally, how it was always meant to work.

**Stevie Kim:** How, so we just need to fix what exists, without, you know, letting myself break from that mental model and think, oh, wait, is this even right?

**Stevie Kim:** So I think we need to have more of those discussions.

**Stevie Kim:** Instead of trying to just fix what exists because that's, you know, especially like, you know, I don't have historical context and anyone else jumping on board isn't going to either.

**Stevie Kim:** So just kind of, this is kind of a reminder more for me than anyone else, but making sure that I don't get stuck in like, oh, well, this is how it's supposed to work and this is how it's supposed to be.

**Stevie Kim:** So we just need to fix what exists.

**Stevie Kim:** Sorry.

**Stevie Kim:** Yeah.

**Stevie Kim:** A little bit of a tangent, but I will get clarity on anything that is still outstanding in the shaping doc.

**Stevie Kim:** Like if there's something that's, you know, that I'm not understanding, you're not understanding, let's get clarity on that.

**Stevie Kim:** Just put it in the comments and let's, let's push harder on them for some, some of the, you know.

**Stevie Kim:** When they do some hand-wavy stuff, and go, yeah, this is how it's going to work.

**Estevão Mascarenhas:** Yeah, sounds good.

**Estevão Mascarenhas:** Yeah, yeah.

**Pedro Steimbruch:** I agree with Jose on terms that we were running in a structured way till now, and I understand that.

**Pedro Steimbruch:** were sprinting all we could to the launch, but now I think we need to be a bit slower to be faster.

**Pedro Steimbruch:** If we, right, I think that we need to think on what value we really want to deliver and shape that and work on some kind of cycles.

**Pedro Steimbruch:** Because if we keep sprinting, I think we will deliver a lot, but we want, you know, be on point on our delivers.

**Pedro Steimbruch:** Yeah, I think we definitely need some cycles or more structures shape up towards a goal and come.

**Pedro Steimbruch:** Yeah.

**Pedro Steimbruch:** Down a bit after the launch.

**Jose Farias:** Quick side note, Ryan Singer, the author of ShapeUp, recently released some Claude skills for shaping.

**Jose Farias:** Did anyone see that?

**Jose Farias:** No.

**Jose Farias:** I've used them.

**Pedro Steimbruch:** They're good.

**Stevie Kim:** It's not perfect.

**Jose Farias:** And you can, as anything with LLMs and AI, like, as a user, you can derail the skill, even if it's well-written.

**Jose Farias:** But I think we can lean a little bit on that and speed up the shaping process that way, maybe.

**Jose Farias:** I'll share them in the channel.

**Jose Farias:** I'll find them.

**Jose Farias:** I bookmarked it.

**Jose Farias:** Yeah, I'll share them later.

**Stevie Kim:** Yeah, anything that helps us.

**Stevie Kim:** I found that with writing PRDs, as long as I get, like, basically what I wrote down in that categorization, you know, know,

**Stevie Kim:** At that level, any LLMs can really take it from there.

**Stevie Kim:** And, you know, there's a lot of assumptions that the tools have raised.

**Stevie Kim:** I'm like, oh, I didn't even think about that.

**Stevie Kim:** So it does get like, it does kind of flesh things out and helps you think of different cases that you didn't think of in the past.

**Stevie Kim:** I've had, yeah, just getting that basic kind of, as I said, problem, making sure we have the problem statement and then, you know, the scenarios kind of in place.

**Stevie Kim:** I think that's like, and the opportunity is like, why are we even bothering?

**Stevie Kim:** Like, what, what does it unlock for us?

**Stevie Kim:** What does it unlock for the user?

**Stevie Kim:** Because that's the context that I think is most important.

**Stevie Kim:** Sorry, stand-up was a little bit derailed, but these were, these were kind of like conversations.

**Stevie Kim:** that we just kind of need, haven't had the chance to have after the launch, so.

**Jose Farias:** Absolutely.

**Jose Farias:** Important conversations.

**Jose Farias:** I'm glad you brought it up.

**Jose Farias:** Should we give quick updates?

**Jose Farias:** We have the all hands coming up just to, like, get a sense of what everyone's working on.

**Jose Farias:** Today, after yesterday's meeting, it became apparent, or evident, rather, that Marcel really is yearning for some filters on the onboarding, on the overview.

**Jose Farias:** screen.

**Jose Farias:** Essentially, the same filters that we have in the prompt tables, bring them over to overview.

**Jose Farias:** I'm working on that, and the way that works technically so far, let me know if anyone has any better ideas.

**Jose Farias:** But, of course, the overview screen shows brand perception snapshots, but if you want to filter them by, like, oh, only show me stats for prompts with these characteristics, then we need to drop down a level and aggregate brand prompt performance.

**Jose Farias:** It's going to be slower, but I think fine, because it's not the first screen.

**Jose Farias:** So the first screen loads quickly, and then you filter it, and it just takes like two to three seconds.

**Jose Farias:** I think that's fine.

**Jose Farias:** But we are going to have to snapshot more.

**Jose Farias:** Remember, Pedro, that we recently removed the snapshotting of competitors and prop performances?

**Jose Farias:** I think we're going to have to bring that back.

**Pedro Steimbruch:** It makes sense.

**Jose Farias:** And so we're going to, we can take this offline, but I think the reason we removed that was because of the explosion in storage, right?

**Jose Farias:** Was that the main reason?

**Pedro Steimbruch:** The main reason is we didn't need them at that point, because we were only showing aggregates for the brand itself.

**Pedro Steimbruch:** Okay.

**Pedro Steimbruch:** So I think we should be good if we bring them back.

**Jose Farias:** And also with the removal of the chart, the categories chart, we can stop snapshotting the subcategory stats. So that's a tradeoff. It's not like we're still going to be storing a lot more. Anyway, I'm getting a reminder about timing, so I'll stop there.

**Jose Farias:** That's what I'm working on.

**Jose Farias:** It'll probably take like at least one or two more days.

**Jose Farias:** It's not an easy one.

**Jose Farias:** But we'll get there.

**Jose Farias:** And that's me.

**Estevão Mascarenhas:** I can go next.

**Pedro Steimbruch:** Go ahead.

**Pedro Steimbruch:** Yeah, just a quick one.

**Estevão Mascarenhas:** I post on the channel to be more transparent.

**Estevão Mascarenhas:** But so I'm working on the basic research workflow so we can get better subcategorizations and better streaky because it depends on the company.

**Estevão Mascarenhas:** So I'm also shipping like I evolve, but it's much simpler just to make sure that for some brands, like 30 brands, that workflow is working better than we have right now.

**Estevão Mascarenhas:** But I'm not changing it too much.

**Estevão Mascarenhas:** I think the main difference is that we're going to expose all the trees.

**Estevão Mascarenhas:** Subcategories suggested during the onboarding, hoping that the user can pick up and drop whatever is not relevant.

**Estevão Mascarenhas:** I think with Daniel's change on copy, I think that's going to work out.

**Estevão Mascarenhas:** Also, I think we should take a look on how can we, in post-hog, maybe track also the release, because it's going to be hard to track those, like, what caused some changes in the onboarding flow.

**Estevão Mascarenhas:** So, don't know, I was going to take a look today as well, but basically this is what I'm doing, and I should be finishing in, like, two, three hours.

**Estevão Mascarenhas:** And then I will tackle whatever we have on P1.

**Estevão Mascarenhas:** I have some tasks assigned to me, so I will start with those.

**Pedro Steimbruch:** Nice.

**Pedro Steimbruch:** So, today I added the pagination back to the sources page.

**Pedro Steimbruch:** I submit also a PR for handling time zones correctly when showing charts in the prompt show page.

**Pedro Steimbruch:** Um...

**Pedro Steimbruch:** I merged that PR from yesterday to update the subcategory for a workspace.

**Pedro Steimbruch:** And now I just shipped the ability to regenerate sitemaps on demand.

**Pedro Steimbruch:** So now our sitemaps are on S3.

**Pedro Steimbruch:** OK, and that's the biggest one today.

**Pedro Steimbruch:** And tomorrow I start investigating how to suggest prompts, because I think there are some good opportunities there, even to rely less on subcategories for a brand, for a workspace.

**Stevie Kim:** So just to bring it back to the priorities that Daniel wrote in his notes and put in the weekly check-in from yesterday in Slack. I want to make sure that we're prioritizing those things over everything. He broke them down into first and second priorities. I can't remember off the top of my head what they all are, but I want to make sure everyone's checking that doc so we're prioritizing the right thing. Filters is one I know. It's something I throw in Slack after the meetings. Daniel moved some things around, so let me find the link... Okay, here it is. This one's kind of messy, but there's the link to his notes and his prioritization list. So I'm going to go into Linear and make sure those things are tagged as P0 and P1. Does that work for everyone?

**Stevie Kim:** Cool. I had a quick question about an older ticket, but it can absolutely be addressed asynchronously. I'm not super clear on what it entails, so let's jump to all hands. Thanks, guys.
