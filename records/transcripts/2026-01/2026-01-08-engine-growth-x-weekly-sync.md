# Engine <> Growth X - Weekly Sync

<metadata>
date: 2026-01-08
time: 19:29 UTC
duration: 44 minutes
organizer: team@growthxlabs.com
participants: Kyle Gaudreau (GrowthX), Carrie Chowske (GrowthX), Carly Piekos (GrowthX), Joel Murphy (Engine/Hotel Engine), Luke Tubinis (Hotel Engine), George Haikal (GrowthX)
fathom_recording_id: 112874412
fathom_url: https://fathom.video/calls/524334761
share_url: https://fathom.video/share/gK_ZkpzAQtx4yeJNxp9Y9ZVR_N6naTKw
source: fathom
enriched_on: 2026-02-28T21:17:44Z
</metadata>

---

## Summary

Quarterly review meeting covering performance rebounds, Engine X content strategy challenges, Check That platform debut as design partner opportunity, and 12-month renewal proposal with emphasis on conversion-adjacent analytics. Carrie Chowske transitioning primary POC role to Carly Piekos.

---

## Context

Engine and GrowthX are in month two of a content partnership focused on building credibility through original articles and driving traffic/conversions. The relationship has been successful (2x traffic growth on GrowthX content vs. 23% on other Engine pages), but faces constraints: the Engine X product team is blocking a competitive comparison post to Engine's visibility in AI, and both teams need clearer workflows around content approval and citation accuracy. GrowthX is introducing a new internal tool (Check That) for AI visibility tracking and wants Engine to serve as an early design partner.

---

## Relevance

- **Product Strategy**: Engine X content team's approval constraints limiting competitive positioning; fact-checking workflow as path to unblock
- **Analytics & Data**: Amplitude clustering now live; conversion-adjacent analysis coming; GrowthX tracking citations and LLM referrers (ChatGPT, Perplexity)
- **Business Development**: 12-month renewal on table with data backing ROI; terms: 5 articles/week, focus shifting to conversion metrics
- **Operations**: POC transition requires smooth handoff; Engine offsite in late January will include product strategy clarity session

---

## Overview

- **Renewal Proposed:** GrowthX proposed a 12-month renewal for 5 articles/week, citing 2x traffic growth on their content vs. 23% on other pages. Joel will discuss the budget with Luke.
- **Engine X Content Blocked:** The Engine X product team blocked a competitor comparison post, demanding all mentions be approved by Stripe. Joel is seeking more product clarity to unblock content.
- **New POC:** Carly Piekos will become the primary point of contact, taking over from Carrie Chowske.
- **New Tool Preview:** GrowthX demoed "Check That," a new AI citation tracking tool. Joel will be a design partner, providing feedback on its UI and features.

---

## Key Topics

### Engine X Content Strategy

  - **Problem:** The Engine X product team blocked a competitor comparison post (Brex, Ramp), demanding all mentions be approved by Stripe.
  - **Rationale:** The post's goal was to build credibility by objectively comparing Engine X to major players, not to be a sales pitch.
  - **Solution:** Joel will get more product clarity from the Engine X team at an upcoming offsite.
      - **Artifact:** Luke and the product owner will record a "fake podcast" to serve as a single source of truth for Engine X capabilities.
      - **Process:** GrowthX will share its fact-checking workflow to prove content accuracy and reduce the review burden on the product team.

### Performance & Analytics

  - **Traffic:** Rebounding from a seasonal slowdown.
      - Organic traffic dropped \~14% over the holidays, but engagement remained steady.
      - New content bets continue to grow, with engagement rates \>65%.
  - **AI Visibility:**
      - **Referrers:** ChatGPT is the largest LLM referrer; Perplexity is showing strong growth.
      - **Citations:** Citations are up, and position has improved by 22%.
  - **Amplitude:**
      - **Clustering:** GrowthX content is now tagged, enabling conversion-adjacent analysis.
      - **Action:** Joel will create a dashboard to show conversion data for GrowthX content.

### "Check That" Platform Preview

  - Kyle demoed "Check That," a new AI citation tracking tool.
  - **Key Features:**
      - **Curated Library:** Pre-built prompts for the "Expense & Travel" category to accelerate setup.
      - **Historical Data:** Instantly applies historical citation data when a new prompt is activated.
  - **Joel's Feedback:** The tool needs to surface *unknown* opportunities (e.g., high-volume prompts where competitors are cited but Engine X is not).
  - **GrowthX Response:** This deeper analysis will likely live in their broader "content OS," which integrates data from GSC, GA, and the website.

### Renewal Discussion

  - Kyle proposed a renewal for the February term.
  - **Proposal:**
      - **Scope:** Continue current agreement → 5 articles/week.
      - **Term:** 12-month agreement (standard for 98% of GrowthX clients).
  - **Rationale:** The partnership has built a strong foundation, driving 2x traffic growth on GrowthX content vs. 23% on other pages. The next phase will focus on driving conversions.

### Operational Updates

  - **Content Backlog:** 25 articles are awaiting Joel's review in Airtable.
      - **Guidance:** Review items in the "current week" bucket first, starting with FAQs for faster completion.
  - **Meeting Schedule:** No meeting next week due to the GrowthX offsite.
  - **Scrunch Cloudflare Worker:** Joel asked if the worker is necessary to get valuable data on what content bots are scraping.
      - **GrowthX Response:** They have not used the feature extensively and will investigate its value.

---

## Action Items

**Carly Piekos (GrowthX)**
- Message Andy re: reschedule call to next week

**Joel Murphy (Engine/Hotel Engine)**
- Review Airtable 'Current week' articles; prioritize FAQs
- Cancel next week's sync w/ GrowthX
- Build Amplitude charts: GrowthX-only conversion-adjacent; exclude Uncategorized
- Provide feedback on Check That platform UI/UX after receiving access

**Carrie Chowske (GrowthX)**
- Schedule backlog pubs across next 2 weeks
- Email Joel fact-checking/accuracy workflow for NGINX

**Kyle Gaudreau (GrowthX)**
- Grant Joel Check That access; send feedback intake steps
- Email Joel renewal deck + next steps
- Ask team re: Scrunch Cloudflare agent; report back to Joel

---

## Transcript

**Carrie Chowske:** So I think we're in week 30. Since we did async for a couple of weeks, the only downside is—Joel, and I'm so sorry—I have 25 articles that are needing your review.

**Carrie Chowske:** It's three weeks' worth of content. We can space it out if you want, or schedule it so they're not all publishing in one day. We have the week of Christmas, the week of New Year's, and then this week.

**Kyle Gaudreau:** Given the amount, do we have any context to help Joel prioritize?

**Carrie Chowske:** Focus on the stuff marked "current week" first. It doesn't matter the order—as long as we get it published, I'll spread it out. I'd tackle the FAQs first since they'll be faster.

**Joel Murphy:** So the stuff marked "current week" is the last two weeks. Got it.

**Carrie Chowske:** Next week, Carly will be leading the meeting, taking over fully as your point of contact. I'll work behind the scenes on content, but she'll be the face you see every week. I'm still around if you have questions.

**Joel Murphy:** Got it. On that note, no meeting next week?

**Carrie Chowske:** We have an in-person offsite next week.

**Joel Murphy:** I'll double-check if we canceled this one.

**Carly Piekos:** We did not cancel it yet.

**Carrie Chowske:** I had a note about changing two meetings, but I didn't want Dallas to cancel this one by mistake.

**Carrie Chowske:** Quick question on the Amplitude stuff—did you backfill the clustering? The back catalog has been categorized?

**Joel Murphy:** Yes, I was going to mention that.

**Carrie Chowske:** Kyle and I were wondering if we could get a chart showing conversion-adjacent information for just the GrowthX content. But this already gives us much more visibility.

**Joel Murphy:** I still need to work on that, but it's fairly easy. We can filter by topic cluster—only GrowthX stuff is tagged. If there's no value, it's not your content. So we can look at conversion-adjacent stuff per topic cluster or all grouped together.

**Carrie Chowske:** Perfect. That helps us adjust what we're producing to make sure we're giving you the right kind of stuff.

**Carrie Chowske:** I'm going to go over some performance stuff quickly, then hand to Kyle to talk about renewal and a preview of our Check That platform.

**Carrie Chowske:** Traffic has mostly rebounded from the seasonal slowdown we were expecting. Even though organic traffic dropped about 14%, engagement held steady—I'd call that a win for the holiday season. We're still seeing growth across our new content bets, with engagement rates above 65%. The content for "Technology & Software" is now showing growth too.

**Carrie Chowske:** Looking at Amplitude, the top traffic sources coming from ChatGPT are all GrowthX articles. ChatGPT is still our largest LLM referrer. I'd like to filter out the "Uncategorized" category if possible.

**Joel Murphy:** I can untick uncategorized and save. You should see it immediately.

**Carrie Chowske:** Perfect. For 2025 overall, we have solid traffic from ChatGPT and really strong growth from Perplexity, especially since we just started tracking them. According to Scrunch data, citations are back up—we doubled citations toward year-end, and position is up 22%.

**Carrie Chowske:** Kyle, want to show the Check That preview?

**Kyle Gaudreau:** Yeah, I can walk you through it.

**Kyle Gaudreau:** Like before Christmas, we'd love you to be a design partner on this. We'll give you access to the Check That workspace with prompts imported from Scrunch plus new ones. We're looking for feedback—what you love, what you hate. There's no added fee; it's a thank you for the partnership.

**Kyle Gaudreau:** The platform differs from Scrunch in how we organize prompts. We've set up categories with curated prompts to track visibility across different industries. You're in the Expense & Travel category.

**Kyle Gaudreau:** The dashboard shows trending, visibility, position, sentiment—similar to Scrunch. We have two kinds of prompts: our curated library (built on competitor data, keywords, search volume, and social signals) and custom prompts. When you activate a library prompt, it pulls in historical citation and visibility data automatically—unlike Scrunch, where new prompts start from zero and you have to wait weeks.

**Kyle Gaudreau:** At the prompt level, you see position, sentiment, citation score over time across platforms, and which sources are being cited most. You can search by competitor to see their top cited content. The plan is to integrate this into our content OS, which pulls in your GSC, GA, and website data to uncover opportunities and feed them into our AI platform.

**Joel Murphy:** So when I'm looking at this—high prompt volume, similar to traditional SEO search volume—that signals I should create content, right?

**Kyle Gaudreau:** To an extent. The basic logic: your competitors are visible but you're not. We're trying to expose which prompts have high intent. ChatGPT doesn't share usage data, so we connect to keywords and search volume to estimate intent levels. We can tweak categories if you want to optimize for Expense & Travel.

**Joel Murphy:** What I'm really looking for is the unknown—someone asking a question where a competitor like Navan is cited but Engine isn't. That's where the opportunity is.

**Kyle Gaudreau:** Exactly. That's where our content OS comes in, pulling GSC, GA, website data, and citation data together to surface those opportunities. This Check That data feeds into the content engine to prioritize what to write.

**Joel Murphy:** Perfect. That aligns with how we want to leverage this data.

**Carrie Chowske:** That's exactly the kind of feedback we're looking for. As you use it, let us know what doesn't feel intuitive—we've been staring at it so long we assume it makes sense, but your fresh perspective matters.

**Joel Murphy:** Totally understand. When can I get access?

**Kyle Gaudreau:** Within the next few days. I'll send you the steps and feedback intake process.

**Kyle Gaudreau:** I want to go through the renewal proposal. February will sneak up quickly, so let's get the ball rolling.

**Kyle Gaudreau:** Over the past six months, we've built a repeatable content engine. GrowthX content is up 2x in Traffic Guides versus 23% on non-GrowthX content. Citations are up, visibility is up, and we're closing the gap on Navan/Travelpert. But there's still room to grow—we need to understand deeper conversion impact and protect this traffic from AEO changes.

**Kyle Gaudreau:** The proposal: Continue 5 articles/week, but move to a 12-month term. We typically do 12-month engagements (98% of clients). We can also explore programmatic SEO or expanded editorial for Nginx and other launches.

**Joel Murphy:** No immediate concerns, but I need to talk to Luke about budget and sign off. A 12-month term makes sense to me. We'll be together at the offsite next week, so we can discuss then.

**Kyle Gaudreau:** Perfect. Feel free to reach out anytime; I'm happy to make time.

**Carrie Chowske:** One note: Carly comes from a finance background—she's worked with Amex and other major names—so she'll be a great resource for Engine X content work.

**Joel Murphy:** Good to know. We have specific OKRs around organic Nginx content, so that will be important to track.

**Carrie Chowske:** Carly brings valuable finance background—she navigated Amex's complex disclaimers and content approval processes. She'll be helpful for Engine X work.

**Carly Piekos:** And then I was like, we probably should talk to Joel about that.

**Carly Piekos:** Yeah, there are a lot of disclaimers for American Express.

**Carly Piekos:** It was quite the issue with duplicate content all over their site.

**Carly Piekos:** And there was a lot of ropes to jump through before they could even publish their content.

**Carly Piekos:** It would take months.

**Carly Piekos:** So I feel like you are already one upping them, at least their corporate business strategy and travel.

**Joel Murphy:** So, so, well, so speaking of that, I don't want to like, you know, step on the renewal conversation, but do have something to share about, about kind of related to that.

**Kyle Gaudreau:** Yeah, let's kick into that.

**Joel Murphy:** Yeah.

**Joel Murphy:** Okay, cool.

**Joel Murphy:** So I had to take down our, just before.

**Joel Murphy:** Christmas Best Corporate Travel Card Post, because the Nginx product team came to me all up in arms about it.

**Joel Murphy:** And they're basically saying, we're recommending Brex, and we're recommending Ramp, and, you know, it seems like we messed up and should have said Nginx where we're saying Ramp and Brex.

**Joel Murphy:** I said, no, we didn't mess this up.

**Joel Murphy:** Like, this is, there was an intention here.

**Joel Murphy:** You know, the goal is to mention us in the same breath with these huge players that, like, lend credibility.

**Joel Murphy:** The goal is an objective comparison piece, not a sales pitch, you know, all that stuff.

**Joel Murphy:** So they want me to take it down.

**Joel Murphy:** said, no.

**Joel Murphy:** But I said, look, we're happy to, like, clarify anything here, and I'm, Ed, it's like, we don't have the capacity to do that right now, blah, blah, blah.

**Joel Murphy:** We, you know, blah, So, long story short, it's like, okay, we'll take it down, but we're going to refactor it.

**Joel Murphy:** So, the reason why I'm sharing it is

**Joel Murphy:** And this with you guys is because one thing we're doing next week in person is that team is going to like do a whole presentation about engine X to the growth team.

**Kyle Gaudreau:** So I'll have more of my mind wrapped around what it is, what it will be, all this stuff.

**Joel Murphy:** Because honestly, that's not clear to very many people here right now.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** And I mean, they shouldn't have to like be reviewing everything either if they can give us a comprehensive like, you know, it should be similar to what we've got with like our fact checking process and all the other features.

**Carrie Chowske:** Like, you know, once they have it all, they just give it to us.

**Carrie Chowske:** They don't need to be checking in.

**Carrie Chowske:** We'll make sure that it's, especially I know Carly can help to verify that we're following the right stuff.

**Joel Murphy:** Yeah.

**Joel Murphy:** So a couple of things beyond that, like presentation they're doing next week.

**Joel Murphy:** One idea Luke had was to do basically a kind of a fake podcast between himself and and, you know,

**Joel Murphy:** The product owner and just basically use that as like we can feed that into the systems like this is what Nginx is, what it's not, what it's capable of like as just sort of like an artifact that we can use for all that stuff.

**Joel Murphy:** Not me relaying it to you guys and put, you know, it's like a game of telephone at that point.

**Joel Murphy:** So it sounds like we're going to do that.

**Kyle Gaudreau:** That would be very helpful.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** I mean, we can use that in a variety of different ways.

**Kyle Gaudreau:** We can plug that into our system with like different rules and guidelines and, you know, so that anything like that, where you can capture that sort of context that we can repurpose in a variety of ways.

**Joel Murphy:** Here's the real challenge: Nginx product team says everything mentioning Nginx must be approved by Stripe. I'm cautiously optimistic that's not literally everything. Our disagreement on approval scope aside, we need to get creative. Maybe we build pre-approved CTAs and copy we can use without re-review.

**Joel Murphy:** What we wrote before: an objective comparison where Nginx is mentioned alongside Brex and Ramp for credibility. The product team misread our intent. I'll get more details from them to make this less of a black box.

**Carrie Chowske:** We can share our fact-checking workflow with them. For Engine, we've built common accuracy traps based on early feedback you gave—things like "don't say it this way, say it this way because..." We run a final accuracy check on all features and rarely have issues (maybe one thing in six weeks).

**Joel Murphy:** That would help. I know our other products well enough to spot issues and feed back fixes. With Nginx, I only know it's a black card with an X—I can't fact-check what I don't understand. That's the gap we need to close.

**Carrie Chowske:** But that's all I've given it.

**Carrie Chowske:** That's all I've given it so far.

**Carrie Chowske:** And so it's able to, like, still, we can still do a lot with even just that little stuff, even as like a CTA.

**Carrie Chowske:** So it's been accurate on it.

**Carrie Chowske:** flagged things for me about NGINX.

**Carrie Chowske:** And mostly because we have that slide deck and then we have the more updated stuff you gave us.

**Carrie Chowske:** And it'll try to, like, sometimes if I'm still on our CLAWD project, so sometimes when I'm doing, like, a last, I'll do, like, a quick little check in there, too, to make sure.

**Carrie Chowske:** And it'll still try to use that slide deck.

**Carrie Chowske:** And I'm like, I don't want to get rid of it because there is stuff in there that we use.

**Carrie Chowske:** But I'm like, no, no, no, that's okay.

**Carrie Chowske:** This is the more recent data.

**Joel Murphy:** Yeah, so if you could share those details, when I make that comment to them, it'll hold some weight.

**Joel Murphy:** We're like, look, this is the process.

**Joel Murphy:** All I need is the input.

**Joel Murphy:** That's the missing piece.

**Joel Murphy:** So that would be very helpful.

**Joel Murphy:** So, you know, it ended up fine.

**Joel Murphy:** The conversation ended up being like, oh, we're happy to do a line and blah, blah, blah.

**Carly Piekos:** Yeah, a lot of companies have issues with mentioning their competitors at all.

**Carly Piekos:** They just want to pretend they don't exist.

**Carly Piekos:** But controlling the narrative is like what you need to do with AI, though.

**Kyle Gaudreau:** Exactly, yeah.

**Kyle Gaudreau:** And I'm sure Luke understands this as well because just his background, and I know he's in those conversations with you all.

**Kyle Gaudreau:** Like, yeah, Listicles is like a, you know, a very common thing nowadays.

**Kyle Gaudreau:** It works for SEO.

**Kyle Gaudreau:** It works really well for AEO.

**Kyle Gaudreau:** It's kind of just this game you have to play.

**Kyle Gaudreau:** Because sometimes what can help when you do this, maybe we can show some specific examples, is like just do some of those searches that, like, we would appear for in the intent of those articles.

**Kyle Gaudreau:** And you'll see your competitors popping up.

**Kyle Gaudreau:** You'll see Reddit popping up.

**Kyle Gaudreau:** You'll see other websites.

**Kyle Gaudreau:** And it's like if you choose not to do this, then you're, to Carly's point, you're not having any kind of, like, control over this narrative in a meaningful way.

**Kyle Gaudreau:** And so it's just a lost opportunity that, you know, I think misses the broader context of what, where you all are actually appearing.

**Carrie Chowske:** At the very least.

**Carrie Chowske:** If you're stacking yourself up against those other ones, you can like, this is the best one for travel, though.

**Carrie Chowske:** You can say just why it's better.

**Carrie Chowske:** And then also, if you're also using Engine or you're using Concur, now that you're going to have that partnership, you can be like, and here's the benefit if you also use Engine.

**Carrie Chowske:** I think the differentiation is going to be the door in for you guys with the card, for sure.

**Joel Murphy:** Yeah, cool.

**Joel Murphy:** Okay, so I'll keep you guys posted on all that.

**Joel Murphy:** And then the last thing for me was I was tinkering around in Scrunch yesterday and noticed we had not connected, like, their Cloudflare worker thing.

**Joel Murphy:** And I was like, okay, let's go and do that.

**Joel Murphy:** So the infrastructure team kind of pushed back a little bit.

**Joel Murphy:** So, like, do we really need this tool?

**Joel Murphy:** And I was like, well, can it do these three very specific things that Scrunch is?

**Joel Murphy:** And it can do some of it.

**Joel Murphy:** And I guess before I kind of keep pushing on them, like, do we feel like that's going to give us a valuable signal that we don't have?

**Joel Murphy:** I feel like it, but I wanted to gut check that with you guys.

**Kyle Gaudreau:** Sorry, my son is having a tantrum in the background, so I only caught some of that.

**Kyle Gaudreau:** He's homesick with the flu.

**Kyle Gaudreau:** Bummer.

**Kyle Gaudreau:** I think he was asking about the agent, like, the way you got the agent scrunch.

**Kyle Gaudreau:** Frankly, like, I haven't played with that feature a lot to be able to, like, tell you anything meaningful.

**Kyle Gaudreau:** Like, whether the frequency of, like, how this is, you know, these agents are hitting your website, like, I could see maybe they're being some benefit.

**Joel Murphy:** I think that's the intent, right?

**Joel Murphy:** Well, we have that through another tool that they showed me.

**Joel Murphy:** The one thing that they haven't been able to show so far, and they're like, oh, the security team will let you know what they have, and I'm pretty sure it's not going to tell me this, was what content are the bots actually scraping when they're there?

**Joel Murphy:** Yeah.

**Joel Murphy:** They can tell me, oh, we saw ChatGPT and all the others this many times as when they came back, and they can tell which agent it was.

**Joel Murphy:** But

**Joel Murphy:** That specific thing, they weren't able to show.

**Joel Murphy:** So I'm like, I told him, look, if you can show me this some other way, we don't have to worry about setting this up.

**Joel Murphy:** But yeah, I was just looking for from you guys, if you guys have used that at all.

**Kyle Gaudreau:** And I can say.

**Kyle Gaudreau:** Ask around to see if someone else has experimented with it that I'm just not aware of.

**Carrie Chowske:** But to my knowledge, I'm not sure we've actually leveraged that feature.

**Carrie Chowske:** Yeah, I just went to look because at one point Airbyte was talking about they wanted to set it up and they still haven't done it.

**Carrie Chowske:** So I don't, I don't have any.

**Joel Murphy:** All right.

**Joel Murphy:** Well, I'll keep you posted on where I get with it.

**Joel Murphy:** If it's going to end up being a fight, I probably will just back away.

**Joel Murphy:** Sick of that.

**Kyle Gaudreau:** So enough fires to fight at the moment.

**Joel Murphy:** Yeah.

**Joel Murphy:** Yeah.

**Joel Murphy:** But I'd love to get, I mean, I'll take any signal I can get in this area just because of the nature of it.

**Joel Murphy:** So, yeah.

**Joel Murphy:** Okay, cool.

**Joel Murphy:** Well, that's it for me.

**Carrie Chowske:** Cool.

**Carly Piekos:** Fantastic.

**Carrie Chowske:** Well, it's been really wonderful working with you, Joel.

**Carrie Chowske:** I'm happy to have.

**Joel Murphy:** Thank

**Carrie Chowske:** I'm happy but sad to hand over the reins to Carly, but I know you're in good hands, and I already love working with her, so it's going to be great.

**Joel Murphy:** Awesome.

**Joel Murphy:** Yeah, likewise, it's lovely working with you.

**Carly Piekos:** Ping me any time if I can help with anything.

**Carly Piekos:** Oh, she'll be on calls, don't worry.

**Carly Piekos:** All right, all right.

**Carrie Chowske:** She'll be on some of the calls at least.

**Carrie Chowske:** I'll just pop in for fancy.

**Carly Piekos:** Yeah, but I will see you next week with new information.

**Carly Piekos:** Oh, two weeks.

**Carly Piekos:** Yes, two weeks.

**Carly Piekos:** Yeah, so have a good two weeks, and good luck with your conversation.

**Joel Murphy:** Thank you.

**Carly Piekos:** appreciate that.

**Kyle Gaudreau:** All right, Joel.

**Carrie Chowske:** Appreciate the time.

**Joel Murphy:** Bye.

**Carly Piekos:** See you guys.

**Kyle Gaudreau:** Bye.
