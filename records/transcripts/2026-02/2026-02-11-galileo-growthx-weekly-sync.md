# Galileo <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-11
time: 18:30 UTC
duration: 31 minutes
organizer: team@growthxlabs.com
participants: Carrie Chowske (GrowthX), Jackson Wells (Galileo)
fathom_recording_id: 121677270
fathom_url: https://fathom.video/calls/562611198
share_url: https://fathom.video/share/1vKM2bxg6cB5rPSX7eaKTYYq5nzdeE3M
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

GrowthX and Galileo synced on three critical areas: clearing a content quality bottleneck by providing product artifact updates to fix AI hallucinations and spammy internal linking, unblocking the publishing pipeline with a new workflow ready for testing Friday (clearing ~15 pending blogs), and establishing a granular AEO/GEO reporting framework using Check That's new dual-categorization feature. Jackson flagged declining LLM referral traffic month-over-month and proposed increasing third-party content syndication (Reddit, YouTube, dev.to) as a long-term strategy to build referential citations.

---

## Context

Galileo is a GrowthX client in the AI/ML engineering space using Galileo's AI evaluation platform. Jackson Wells leads the marketing function at Galileo and is focused on visibility in LLM-driven search queries. The team syncs weekly to review content performance, unblock publishing workflows, and align on AEO strategy. This meeting was particularly important because Galileo is facing two parallel challenges: immediate tactical issues (content quality and publishing delays) that are preventing consistent weekly content cadence, and strategic pressure from Jason (Galileo leadership) to prove AEO ROI through more granular reporting. GrowthX has been supporting Galileo with content strategy and AI visibility measurement through CheckThat.

---

## Relevance

**To GrowthX Delivery:**
- Content quality auditing workflow using Claude + source docs is proving effective as a debugging tool when Galileo's AI pipelines miss hallucinations. This pattern could be productized for other clients.
- Publishing workflow bottlenecks are endemic in content ops — Galileo's blocker (15 pending blogs) echoes patterns GrowthX sees across the client base. The new workflow tested Friday may inform improvements for other clients.
- AEO reporting maturity is advancing: Galileo's three-tier metric system (broad weighted metric + LLM referrals + core prompt tracking) is a model reporting framework for future clients navigating AEO ROI conversations.

**To CheckThat:**
- Dual-categorization feature is directly unlocking internal reporting use cases. Galileo was previously blocked by inability to separate niche internal categories from public-facing ones; this feature removes that blocker.
- Core prompt tagging and filtering in CheckThat is in active use. Jackson and Carrie are co-creating a "core prompt" list for monthly tracking — this is real-world validation of CheckThat's filter extensibility.
- LLM referral traffic declining month-over-month for Galileo; this is consistent pressure across CheckThat customers and suggests the market may be shifting or saturation is setting in on some niches.

**To GrowthX Business Development:**
- Galileo is expanding engagement: access requests (Check That), new reporting demands (AEO/GEO metrics), and proactive syndication strategy discussions signal account health and appetite for deeper services.
- Risk: Jason's scrutiny of AEO metrics could create churn pressure if GrowthX can't deliver measurable gains. Month-over-month referral declines may force strategic pivot or expanded scope.

---

## Overview

- **Publishing Blocker Cleared:** The new publishing workflow is ready for testing this Friday, unblocking \~15 pending blogs and restoring the weekly cadence.
- **AEO Reporting Unlocked:** Check That's new dual-categorization feature enables internal reporting on niche topics without altering the public profile, directly addressing Jason's request for AEO/GEO metrics.
- **Data Integrity Audit:** A technical SEO audit is underway to resolve a data discrepancy between SEMrush and Looker (GA4/Search Console), ensuring accurate performance reporting.
- **Content Quality Fixes:** GrowthX will provide its AI corpus to help Galileo fix content hallucinations (e.g., misstating product strengths as weaknesses) and spammy internal linking.

---

## Key Topics

### Content Quality & Pipeline

  - **Problem:** AI-generated content has quality issues requiring manual fixes.
      - **Hallucinations:** Content misstates product strengths as weaknesses.
      - **Spammy Linking:** Over-linking to the "State of Eval Engineering" report (4-5+ times/post).
  - **Solution:** GrowthX will provide its AI corpus (artifacts) for Galileo to review and update, ensuring the AI uses the latest product info.
  - **Blocker:** The publishing queue has \~15 pending blogs (12 needing minor edits, 3 queued).
  - **Resolution:** The new publishing workflow is ready for testing this Friday. Carrie may test it sooner to expedite publishing.

### Performance Reporting & Strategy

  - **Problem:** A data discrepancy between SEMrush and Looker (GA4/Search Console) is delaying performance reporting.
      - **Discrepancy:** SEMrush shows a traffic spike, while Looker shows dips.
      - **Cause:** Suspected issue with Looker's data blending formulas.
  - **Resolution:** A technical SEO audit is underway to validate Looker's data integrity.
  - **New AEO Reporting Strategy:**
      - **Context:** Jason is requesting more granular AEO/GEO performance metrics.
      - **Solution:** A three-part metric system will be implemented.
        1.  **Weighted Metric:** Broad performance data.
        2.  **LLM Referral Traffic:** Secondary metric.
        3.  **Core Prompt Weighted Metric:** Performance on a curated list of high-value prompts.
      - **Execution:** Jackson and Carrie will co-create the "core prompt" list and tag them in Check That for tracking.

### AEO Strategy & Syndication

  - **Context:** AEO is a long-term strategy, not a quick fix, requiring consistent execution.
  - **Tactic:** Increase third-party content syndication (Reddit, YouTube, dev.to) to build referential citations.
  - **Caution:** Do not duplicate content verbatim.
      - **Rationale:** This avoids SEO penalties and is less effective, as AI often cites unique third-party content over branded listicles.

---

## Action Items

**Carrie Chowske (GrowthX)**
- Email Jackson: agenda + performance notes
- Email Jackson: corpus/artifact list (incl product/features)
- Coordinate w/ Usman: test publishing workflow early this week
- Add Galileo category in Check That
- Email Jackson: Check That access instructions/invite
- Email Jackson: AEO/GEO update + 2025 SEO article feedback

**Jackson Wells (Galileo)**
- Email Carrie: proposed core prompts for weighted metric

---

## Transcript
**Jackson Wells:** Hey, Carrie, how's it going?

**Carrie Chowske:** It's going well.

**Carrie Chowske:** I'm so sorry that I was running late.

**Carrie Chowske:** If you are short on time or you have something right after this, we can reschedule.

**Jackson Wells:** That's all good.

**Carrie Chowske:** I apologize so much for that.

**Carrie Chowske:** I didn't even get a chance to share the agenda with you.

**Carrie Chowske:** In fact, I didn't even get a chance to finish the performance part of it.

**Carrie Chowske:** I had notes drafted up, but I hadn't done it.

**Carrie Chowske:** So I will get that to you after the meeting.

**Carrie Chowske:** But the rest of my day is open now.

**Carrie Chowske:** So I don't have more meetings after you.

**Carrie Chowske:** So I will make sure I take care of that.

**Carrie Chowske:** But I do have some other things.

**Jackson Wells:** Well, I do have an 11 o'clock, but I'm chilling and we can go over anything that is prepared.

**Jackson Wells:** Sorry, I was just in the middle of editing one of the blogs.

**Jackson Wells:** I think.

**Jackson Wells:** Would you guys mind sending me?

**Jackson Wells:** Do you.

**Jackson Wells:** Do like a succinct collection of what you all are using as a corpus, like as your artifacts?

**Carrie Chowske:** Yep, absolutely we do.

**Jackson Wells:** Okay, if you wouldn't mind sending that over, I'd like to take a look just so I can maybe trim some of the older stuff and or replace some of the assets in there with newer ones.

**Jackson Wells:** Because there's still a couple of gaps here and there.

**Jackson Wells:** And I also know that some of these refreshes likely have some old terminology and language, but I want to double check that.

**Jackson Wells:** Yeah, and it may even be the refresher, we have a separate pipeline for refreshing, and it may be that that is calling up the wrong artifact too, or calling up old information, you know what I'm saying?

**Jackson Wells:** Totally, totally.

**Jackson Wells:** But we're definitely getting closer on quality.

**Jackson Wells:** Internal linking is still, it's getting better, it's getting better for sure.

**Jackson Wells:** There's been a couple of instances in these recent ones where we're linking our state of eval engineering report, like, four or five plus times, and it gets a little.

**Jackson Wells:** Spammy.

**Jackson Wells:** I'm trying to go through and weed that out.

**Jackson Wells:** And then there's been a couple of hallucinations that are pretty, one of those, this blog I found is particularly bad, where it says our weaknesses for our platform are actually our strengths, and that we don't have those.

**Jackson Wells:** So we should, I don't know where that came from.

**Carrie Chowske:** No, we definitely want to check the product.

**Carrie Chowske:** We have an artifact for products and features and products, and we should definitely check that one and make sure everything in that's correct.

**Jackson Wells:** Because that's something that's easy enough.

**Carrie Chowske:** Like even if, sometimes what will happen is like when we run a workflow like that, it'll tell you it checked the thing, but it did, but it kind of like was getting a little lazy, I think, around that point.

**Carrie Chowske:** And so you kind of have to tell it at the end, okay, let's do a final check against all of these things.

**Carrie Chowske:** I always would do that because it's, it's, it can just have a moment.

**Jackson Wells:** It's not even, yeah, ignoring something.

**Jackson Wells:** A hundred percent.

**Jackson Wells:** That's, I've just been my new workflow for editing things.

**Jackson Wells:** Is having Claude in the browser go through and validate everything against the most recent docs and product pages and then come up with lists of stuff.

**Carrie Chowske:** That's my trick for when our pipelines aren't working so I can go back and make them work.

**Carrie Chowske:** I run it through Claude and I'm like, all right, what's getting missed consistently?

**Carrie Chowske:** Go back in and be like, okay.

**Jackson Wells:** Where is context too big and we've broken down?

**Carrie Chowske:** Yeah.

**Jackson Wells:** But we're getting better.

**Jackson Wells:** We're getting better for sure.

**Jackson Wells:** Did you hear back on the publishing pipeline?

**Carrie Chowske:** I have not heard back on it.

**Carrie Chowske:** last I heard from them was that it was in the works.

**Carrie Chowske:** The ticket was open.

**Carrie Chowske:** I can pull that up and see real quick if it's been moved at all.

**Jackson Wells:** Great.

**Carrie Chowske:** Well, we're all about anything we can do to make publishing happen faster because that's really the name of the game these days — the speed.

**Jackson Wells:** Yeah.

**Jackson Wells:** Because.

**Jackson Wells:** It looks like we have 12 blogs that are in the needs edits category, and I think they were pretty minor edits.

**Jackson Wells:** Most of them were just accepting some suggestions and changes I had.

**Jackson Wells:** I don't know where we're at in the publishing queue.

**Jackson Wells:** And we have three queued for publishing, so that's roughly 15 or so in the publishing queue, give or take.

**Jackson Wells:** So it'd be cool to get that cleared out.

**Carrie Chowske:** Okay, yep, it's our, this is actually ready to test our publishing workflow.

**Carrie Chowske:** That's just literally from today.

**Carrie Chowske:** So I think Usman is out for this week.

**Carrie Chowske:** He's taking so much deserved time off, but he said he's going to test it on Friday.

**Carrie Chowske:** So we should have that this week.

**Carrie Chowske:** And maybe get with him and see if I can do it for him before then, just to move it along.

**Carrie Chowske:** 단ord the something...

**Carrie Chowske:** But be

**Carrie Chowske:** Yeah, it's ready to go. It's working like it should, which is good.

**Jackson Wells:** The publishing workflow has been one of the easiest ones to get set up anytime we have to do it.

**Jackson Wells:** Yeah.

**Carrie Chowske:** Great.

**Carrie Chowske:** Okay, that's good.

**Carrie Chowske:** That's good news.

**Carrie Chowske:** Yeah.

**Jackson Wells:** Sweet deal.

**Carrie Chowske:** Okay, and I'm trying to see what else I had here.

**Carrie Chowske:** Oh, yeah.

**Carrie Chowske:** And then the internal linking thing that you brought up, Usman's always also working on adding that artifact.

**Carrie Chowske:** I think he was trying to prioritize the publishing part of it.

**Carrie Chowske:** And then where one of the things that he wanted me to mention for you is that he just had a he said to me, and I trust him on this one.

**Carrie Chowske:** He's like, I just have a feeling that this data isn't, isn't showing correctly in Looker.

**Carrie Chowske:** So we put in a ticket with our director level team to look at it, to do it like a just a quick technical SEO audit to make sure that good.

**Carrie Chowske:** that.

**Carrie Chowske:** What we're seeing in Looker is accurate from what we're pulling from GA and Search Console.

**Carrie Chowske:** So just to be aware of, that's why I didn't kind of pull that for you this week.

**Carrie Chowske:** He said that to me and I was like, okay, fair enough. I'll hold off because there might have been some recent updates to formulas. I'll have to look into it, but we're going to clean that up so we know what we're reporting is accurate.

**Jackson Wells:** What's the gut reaction of?

**Carrie Chowske:** We're seeing more positive, which is not rare to happen, but seeing more positive stuff coming out of SEMrush.

**Carrie Chowske:** But it's also, it's not so much that it's just showing an overall more positive.

**Carrie Chowske:** It's not even showing some of the like dips that we're seeing.

**Carrie Chowske:** And so we're seeing things like, we're seeing it completely differently in Looker than in SEMrush.

**Carrie Chowske:** And then we go to like, and because our Looker is blending the data from GA4 and Search Console, we can't really.

**Carrie Chowske:** They just like go direct to the source and see it.

**Carrie Chowske:** So that's kind of why we're going to have them audit that for us.

**Jackson Wells:** So that shouldn't take very long though.

**Jackson Wells:** Got it.

**Jackson Wells:** Got it.

**Jackson Wells:** Got it.

**Jackson Wells:** Got it.

**Jackson Wells:** Yeah.

**Jackson Wells:** Let me, oh, oh, that's, yeah, that is very odd.

**Jackson Wells:** Sorry.

**Carrie Chowske:** I just pulled up our own SEMrush.

**Jackson Wells:** And for some reason we were seeing an insane spike in organic traffic.

**Jackson Wells:** Well, not insane, but a very measurable spike in organic traffic there.

**Jackson Wells:** And some of that I'm seeing in, in GA4, but not quite as intense because yeah, that's.

**Carrie Chowske:** And it's just a pattern because I think Vivek had been reporting some, like some valleys in that recently, some dips, and that's not reflected anywhere else.

**Carrie Chowske:** So we're kind of like, okay, where's this coming from?

**Carrie Chowske:** So just double checking that the settings and everything are right so that I'm not like giving you someone else's data or something when I'm reporting.

**Carrie Chowske:** Um, but yeah, yeah.

**Carrie Chowske:** Um, but that.

**Carrie Chowske:** That's pretty much it.

**Carrie Chowske:** I am still kind of working, kind of refining the prompts and stuff in Check That.

**Carrie Chowske:** I actually was going to pull that up because I think this might be an old screenshot that I didn't replace.

**Jackson Wells:** Yeah, do we have an update on the potential recategorization or any of those types of...

**Carrie Chowske:** Yeah, so they did some things to make it...

**Carrie Chowske:** I just got this today, actually.

**Carrie Chowske:** I'm glad you asked about that.

**Carrie Chowske:** We are...

**Carrie Chowske:** They switched how they're doing the categorization so that...

**Carrie Chowske:** Because they're trying...

**Carrie Chowske:** The front-facing part of it...

**Carrie Chowske:** Because right now, what would happen...

**Carrie Chowske:** Before, what would happen is if we changed on your workspace, if we changed your category, that would then also change the front-facing part of it, too.

**Carrie Chowske:** And their idea behind Check That is that that public-facing free data is like what G2 does with reviews or like Crunchbase does with financial information.

**Carrie Chowske:** The front-facing data is like what G2 does with reviews — you can trust it because we've researched it and brands can't edit it. The backend is what we use for reporting so you can categorize yourself the way you want to see the data. It keeps it manageable.

**Carrie Chowske:** That way we can get deeper into a niche for our reporting purposes versus a broader topic like you might use publicly.

**Jackson Wells:** Got it.

**Jackson Wells:** Okay.

**Jackson Wells:** That makes, that makes sense.

**Carrie Chowske:** So now I can add the category and they won't complain.

**Jackson Wells:** Great. That is super useful and will help us with internal visibility and segment the data better. I'm definitely getting pressure from Jason on AEO and GEO reporting. I think the weighted metric idea is great and he'd sign off on it. I pitched it as three parts: a broad weighted metric covering all performance data, GEO and LLM referral traffic as secondary metric, and then applying the weighted metric to a specific collection of high-value prompts spanning subcategories.

**Jackson Wells:** There'll be some for observability, some for eval, and so on. Those three metrics would help him understand it better. Should I suggest some prompts or do you want to go first?

**Carrie Chowske:** Let's both come up with a list and meet in the middle. Then we can tag them in Check That. We can create custom tagging — filter by stage, branded/non-branded, library/custom, and add a core prompts filter.

**Jackson Wells:** Awesome. I think he was envisioning a monthly report. He's been very hands-on with organic search and AEO.

**Carrie Chowske:** I can get you access. Let me check if you need to create an account first or if I can set it up for you.

**Jackson Wells:** That would be great. I can look at the data and think about how we want to segment it. The LLM referral traffic dropping month-over-month for a couple months is raising concerns. I haven't been reporting on it for obvious reasons, but I'm thinking about strategies to improve it. Do we have a regular publishing cadence?

**Carrie Chowske:** Are we behind on publishing at all?

**Jackson Wells:** Yeah, we usually do weekly. We published at the start of last week. It was Fridays for a while, then Mondays, but it's weekly. That's why I flagged 15 or so blogs ready for publishing.

**Carrie Chowske:** Yeah, that's the thing we're focused on.

**Jackson Wells:** That's the good news. Should all help.

**Jackson Wells:** I think the refresh with FAQ Q&A format feels like an AEO silver bullet for blog content.

**Carrie Chowske:** There's pushback starting. It'll follow a pattern like keyword stuffing back in the day. I don't want too many eggs in that strategic basket. For now it works. Even if they shift, you still need the content — it's an algorithm signal. If your name and their name are on the same list, the algorithm thinks you're similar.

**Jackson Wells:** That makes sense.

**Carrie Chowske:** It's like the Charlie Day meme with all the strings — how the LLM makes connections.

**Jackson Wells:** At the end of the day, it's such a new field. A lot of people claim to know, but I don't think anyone really does. Marketing execs want it to be concrete, so I'm playing middleman.

**Carrie Chowske:** The concrete thing is: if you don't do anything, you won't show up. Doing something produces way more results than not trying or not being able to publish. We're getting traction.

**Carrie Chowske:** The challenge is that Galileo and a lot of our clients operate in tech space where people use AI. There's a lot of competition to appear in these searches. That's just the reality — it's the same with SEO.

**Carrie Chowske:** So that's just the challenge we're facing, and it's, you know, the main problem that Marcel is always trying to solve.

**Carrie Chowske:** It's why they created Check That and why, you know, it's because we wanted the data.

**Carrie Chowske:** We were sick and tired of trying to figure out how the hell Scrunch was determining what they were showing us, or Profound, or Peak, or any of those.

**Carrie Chowske:** Like, I didn't know how they were doing it.

**Carrie Chowske:** Now we know how it's done and can confidently say this is accurate. We know people are actually searching these things and here's the exact page cited. That's great and something we're not seeing as consistently from other platforms. Hopefully we'll keep improving.

**Jackson Wells:** Yeah, I'm sure.

**Jackson Wells:** On our end, I'm definitely pushing for more third-party content syndication — Reddit posts, optimized YouTube descriptions, and dev.to content to build third-party citations referential to Galileo.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** One thing — make sure you're not duplicating one-to-one, even with canonical tags. We had issues with that before. When someone tried it, we had to backpedal a lot of stuff. It took a while to get things indexed again. Just a warning.

**Jackson Wells:** Totally, not one-to-one.

**Carrie Chowske:** That'll help because when AI cites listicles from third parties like Reddit or dev.to, they're more likely to get cited than branded listicles.

**Jackson Wells:** I wish people were giving it enough time to research and understand it. There are a lot of assumptions about how it works and that it's easy to optimize for — it's not. I'm trying to rewrite marketing priorities to say "we're going to become experts at AEO," but it's not a tooling issue. It's strategy and resourcing. We have the tooling. You're not going to see immediate one-to-one gains.

**Carrie Chowske:** Yeah, that's exactly it. The more people say they know, the more I know they don't have a clue. I'm the type who says "here's what I know." Today I started thinking about Google's influence in the AI game, and that's why we're starting to see that pick up.

**Carrie Chowske:** It's basically CRO — on mobile, when you search Google traditionally, it gives you an AI overview and immediately prompts you to use their full AI search. We're seeing an uptick because it's asking users to try it. It's really nice — has the accessibility of ChatGPT but the citation level and accuracy of Perplexity. You can see where info came from and verify it. People trust Google right or wrong, so they'll use it over ChatGPT. The average consumer especially will switch.

**Jackson Wells:** Yeah, it's hard with our persona being so AI-focused to say what our user behavior is compared to average. I also sent an article on 2025's SEO and GEO updates that I found interesting and want your take on.

**Carrie Chowske:** I have to run to my next call, but I'll add the performance and SEO/GEO/AEO updates and get those to you today. Apologies for the rush — it was a chaotic morning.

**Jackson Wells:** It is all good.

**Jackson Wells:** I appreciate it as always.

**Jackson Wells:** And yeah, ping me if anything else comes up.

**Carrie Chowske:** Okay, will do.

**Carrie Chowske:** All right.

**Carrie Chowske:** Thanks, Jackson.

**Jackson Wells:** Awesome.

**Jackson Wells:** Thanks, Carrie.

**Carrie Chowske:** Have a good one.

**Carrie Chowske:** You too.

**Carrie Chowske:** Bye.
