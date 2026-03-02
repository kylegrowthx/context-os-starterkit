# EM training: Analyzing engagement and conversion performance

<metadata>
date: 2026-02-10
time: 17:59 UTC
duration: 68 minutes
organizer: Kyle Gaudreau (kyle@growthxlabs.com)
speakers_active: Kyle Gaudreau, Megan Dickey, Talal Syed, Carrie Chowske, Katya Luscomb, Andi Bailey
participants: Aida Knezevic (aida@growthx.ai), Vivek (vivek@growthx.ai), Matthew Alves-Hill (matthew.alves-hill@growthx.ai), Carrie Chowske (carrie@growthx.ai), Megan Dickey (megan@growthx.ai), Andi Bailey (andi@growthx.ai), Jo Kaminska (jo@growthx.ai), Erik O'Brien (erik@growthx.ai), Bailey Seybolt (bailey@growthx.ai), Katya Luscomb (katya@growthx.ai), Liz Kushnereit (liz@growthx.ai), Talal Syed (talal@growthx.ai), Ella Dillon (c-ella.dillon@growthx.ai), William Leborgne (william@growthx.ai), Kathy Lam (kathy@growthx.ai), Carly Piekos (carly@growthx.ai), Kyle Gaudreau (kyle@growthxlabs.com)
calendar_type: internal_only
meeting_type: training_session
fathom_recording_id: 121270167
fathom_url: https://fathom.video/calls/561191848
share_url: https://fathom.video/share/LYsYybEyQjeM2qXVKrHzqBFjp6zqq-mW
source: fathom
enriched_on: 2026-02-27T21:45:00Z
</metadata>

---

## Summary

Kyle Gaudreau led the GrowthX team through a data-driven framework for analyzing engagement and conversion performance across accounts at different maturity stages. Using Yurko (mature account, 0.07% conversion rate) and Cresta (early-stage account) as case studies, the team learned how to identify performance gaps, prioritize engagement over traffic, and tailor content strategies to drive measurable business impact. The session emphasized solving for conversion rate through UX improvements and strategic content refreshes, while setting realistic expectations for new accounts.

---

## Context

This was an internal team training session designed to build the GrowthX engagement management (EM) team's capability to analyze account growth systematically. The session directly supported GrowthX's core business model: the team delivers B2B content marketing at $200k+/year engagements, and success depends on demonstrating clear business impact (traffic, engagement, and conversion) to clients to justify renewals and upsells.

Kyle Gaudreau framed the analysis around account lifecycle stages—early-stage (0–6 months) focuses on indexation and traffic; mature accounts (6+ months) must drive engagement and conversion. This framework is critical because many GrowthX clients hire the agency to grow organic traffic, but without tracking engagement quality and conversion rate, the team risks delivering vanity metrics that don't translate to client revenue. The session directly addressed a strategic gap: how to move from "we published content and got traffic" to "we drove engagement and conversions that matter for your business."

---

## Relevance

**Content Strategy & Performance**
- Framework for evaluating content across account lifecycle stages (early vs. mature)
- Engagement rate target: 40–50%+ on high-traffic pages
- Data-driven approach to identifying low-engagement pages and refresh opportunities
- Case study: using visual, scannable content design to improve engagement

**Conversion Rate Optimization**
- Critical insight: traffic growth alone is insufficient if conversion rate is critically low (e.g., 0.07%)
- Multi-step form strategy to balance user experience with regulatory data collection
- CRO as a prerequisite for achieving ambitious conversion goals

**Account Management & Client Communication**
- Framework for setting realistic expectations (frame early wins as "cautiously optimistic")
- Context for strategic bets: evaluate GrowthX's content impact against client's total organic traffic
- Importance of diversifying content strategy beyond quick wins (alternatives/vs. content) for long-term sustainability

**Product Development (Looker/Analytics)**
- Process gap: Looker case statements need updates when new URLs are published to prevent false-negative indexing alerts
- Analytics insight: use page-level Google Search Console (GSC) data in Looker non-brand views
- Airtable API automation opportunity for syncing published URLs

**Team Development & Training**
- Friday follow-up session: team members to present account analyses and findings
- Skills being built: strategic thinking, data interpretation, client impact storytelling

---

## Overview

- **Prioritize Engagement over Traffic:** For mature accounts, focus on improving engagement (target: 40–50%+) on high-traffic pages. Low engagement signals poor content quality to Google, risking future rankings and failing to drive conversions.
- **Solve for Conversion Rate (CR):** A critically low site-wide CR (e.g., Yurko's 0.07%) makes traffic growth alone insufficient for client goals. Recommend high-impact CRO fixes, like multi-step forms for regulatory-heavy trials.
- **Set Realistic Expectations:** For new accounts, frame early wins as "cautiously optimistic." Diversify content beyond quick wins (e.g., "alternatives" posts) to build a sustainable, long-term growth strategy.
- **Contextualize Performance:** Evaluate our content's impact against the client's total organic traffic. This provides a realistic view of our contribution and helps set appropriate strategic bets.

---

## Key Topics

### Framework: Content Life Cycle & Account Maturity

  - The analysis framework aligns with account maturity, focusing on different metrics at each stage:
      - **Early Stage (0–6 mos):** Indexation, impressions, traffic, and initial engagement.
      - **Mature Stage (6+ mos):** Compounding engagement, learning signals (what to double down on), and conversion.

### Case Study: Yurko (Mature Account)

  - **Problem:** Yurko's 2026 conversion goal is a \~6x increase over 2025's monthly average of \~12.
  - **Root Cause:** A site-wide conversion rate of just **0.07%**.
      - **Implication:** Achieving the goal via traffic alone would require an unrealistic 8x increase. The strategy must address both traffic and CR.
  - **Key Finding: Engagement Gap**
      - Overall traffic is growing, but engaged sessions are not keeping pace.
      - **Why it matters:** Low engagement signals poor content quality to Google, risking future rankings. Engaged users are also more likely to convert.
  - **Actionable Insight: Low-Engagement Pages**
      - A clear pattern emerged: Yurko's "use case" pages have critically low engagement rates (9–16%), well below the 40–50% target.
      - **Hypothesis:** The pages' poor UX (dense, SEO-centric text) is the primary driver.
      - **Solution:** Propose a UX refresh inspired by competitors (e.g., Utext's clean, visual layout).
      - **Risk Mitigation:** The traffic at risk is minimal (\~850 sessions/mo, with only \~80 engaged), making the potential reward for conversion far greater than the risk of a traffic dip.
  - **Actionable Insight: Site-Wide CRO**
      - The trial form is a major conversion bottleneck (long, confusing, no social proof).
      - **Recommendation:** Implement a multi-step form. This solves the client's regulatory need to collect extensive data while improving the user experience.
  - **Actionable Insight: Content Refresh Opportunities**
      - **Finding:** High-engagement content is consistently more visual and scannable (tables, bullets, bolding).
      - **Strategy:** Identify pages with low engagement and keywords ranking just off page one (positions 11–50). Refresh these pages with improved UX to push them onto page one and capture more engaged traffic.

### Case Study: Cresta (Early Stage Account)

  - **Initial Check: Indexation**
      - 22 of 23 published assignments have sessions, confirming no major indexing issues.
      - **Process Note:** Ensure ME updates Looker case statements with new URLs to prevent false-negative indexing alerts.
  - **Growth Trend: Cautious Optimism**
      - Early traffic growth is positive but volatile.
      - **Why it matters:** Frame this as "cautiously optimistic" to manage client expectations; a few weeks of data do not establish a long-term trend.
  - **Content Strategy: Diversify for Sustainability**
      - Early wins come from "alternatives" and "vs." content, but this has limited headroom.
      - **Strategy:** Blend these quick wins with broader topics (e.g., "best lists," "AI agent platforms") to build a sustainable growth engine.
  - **Competitive Analysis: Right-Sizing the Strategy**
      - Dialpad, a competitor used for keyword sourcing, is a traffic behemoth (1.7M visits/mo).
      - **Why it matters:** Compare Cresta against peers of similar maturity (e.g., Sierra, Decagon) to find more realistic and actionable keyword gaps.

---

## Action Items

**Kyle Gaudreau (GrowthX, Operations/Leadership)**
- Reshare strategy doc in channel (Slack)
- Send Loom: Claude Co-Work refresh workflow to team
- Collect team feedback on session; schedule Friday follow-up session

**Talal Syed (GrowthX, Analytics/Product)**
- Explore Airtable API automation for published URLs to update Looker indexing case statements
- Revisit Looker non-brand views to use page-level GSC data
- Set OS assignment metrics to average for volume/difficulty

---

## Transcript

**Kyle Gaudreau:** This meeting is being recorded. Well, for the sake of time, I'm going to get started. Luckily, we're recording this so folks can catch up. So I shared this in the channel last week, but I will reshare it again.

**Kyle Gaudreau:** And this doc, just to set the stage a little bit of what we want to cover.

**Kyle Gaudreau:** So some of this came from a

**Kyle Gaudreau:** Discussion with Ella last week, I thought a good idea of just how to start to go through a few live sessions where I can kind of go through and show how I would think about driving growth in an account based off of the data I'm seeing, how I would approach it, what kind of questions I'm asking, et cetera, to also tee us up for an exercise where we're going to go through and do the same with you all later this week on Friday.

**Kyle Gaudreau:** And so when I said a little bit of a homework assignment, that's what I was alluding to.

**Kyle Gaudreau:** And so what we'll do in that next session is have each person kind of go through one of their own accounts, spend a little bit of the time ahead of that session, rather, to go through some of the motions we'll go through today and just come through and share some of your findings, share how you were thinking about it.

**Kyle Gaudreau:** And we'll ask questions, et cetera.

**Kyle Gaudreau:** Just want to continue to kind of build this muscle to ensure.

**Kyle Gaudreau:** We're doing the right things ultimately to grow these accounts.

**Kyle Gaudreau:** A lot of that connects back to what Marcel was mentioning earlier today and the importance of us being that partner that isn't just continuing to post a lot of new blogs and doing rinse and repeat around that, but really having the context of are we driving impact for their business that they're going to be excited about that's going to lead to upsells, renewals, etc.

**Kyle Gaudreau:** And so one of the ways of kind of thinking about this is going back and kind of considering based off the varying stages, life cycle of content, if you will, and the relative maturity of that account, what kind of things should we be looking at?

**Kyle Gaudreau:** And so I'm sure some of what I will cover today are going to be things that you all do.

**Kyle Gaudreau:** I'm going to go through a couple of accounts.

**Kyle Gaudreau:** This is not meant to be a critique on your work or anything.

**Kyle Gaudreau:** It is more to just try to demonstrate how I would think about it, the kind of things I would dig into next, how that would inform the strategy.

**Kyle Gaudreau:** And just, again, ensuring that we're going through and we're checking the right boxes to truly have the right foundation and have the right plan that drives growth.

**Kyle Gaudreau:** One of the ways of thinking about that, that I'm sure, you know, we hopefully do consistently, is this life cycle of content.

**Kyle Gaudreau:** Anytime we're going to be posting something new, whether it's a new cluster or an individual piece of content, we want to ultimately be, like, building towards this ideally having some sort of impact on site engagement and ideally conversion.

**Kyle Gaudreau:** But first, we can't do that if it's not getting indexed.

**Kyle Gaudreau:** So, you know, for an account that is relatively immature, it's a newer account that we've kicked off in the past handful of months.

**Kyle Gaudreau:** We'll probably want to be keeping a closer eye on the lower parts of this ladder, if you will.

**Kyle Gaudreau:** For an account that's been working with us for, say, plus months, 12 months, whatever it may be, we probably need to ask more questions around here.

**Kyle Gaudreau:** And so what I'm going to go through today is going to be one account that we've been working with for a while, and then another that is relatively new and the kind of things we should be looking at and asking.

**Kyle Gaudreau:** Some of that is kind of broken down here, you know, in terms of, like, phases of, like, what we should expect and what kind of questions we should typically be asking at a high level.

**Kyle Gaudreau:** But we'll go into far more specifics as we go through these accounts.

**Kyle Gaudreau:** So obviously, an early stage account, it's about building momentum.

**Kyle Gaudreau:** I think we all know that we need to make sure it's getting indexed.

**Kyle Gaudreau:** We're seeing compounding impressions, ideally starting to see some early traffic and clicks.

**Kyle Gaudreau:** From there, we should hopefully be getting signals of, like, what's working.

**Kyle Gaudreau:** What's not?

**Kyle Gaudreau:** What do we need to cut?

**Kyle Gaudreau:** What do we need to double down?

**Kyle Gaudreau:** Where are we seeing strong engagement?

**Kyle Gaudreau:** Where aren't we seeing strong engagement?

**Kyle Gaudreau:** And from there, taking those learnings and starting to compound and grow and hopefully starting to see that compounding engagement that's going to ultimately lead to converging.

**Kyle Gaudreau:** And so based off of kind of where, you know, your set of accounts are, where you feel like you could use more insight, feedback, et cetera, you know, just keep in mind this phase that they're in and the kind of questions you should be asking.

**Kyle Gaudreau:** At times can be relatively similar, but there's going to be some important tweaks to how do you think about that and which we can run through today.

**Kyle Gaudreau:** Any questions before I just dive into a few accounts?

**Kyle Gaudreau:** Cool.

**Kyle Gaudreau:** All right.

**Kyle Gaudreau:** With that in mind, picking the first account here, I want to focus on some things.

**Kyle Gaudreau:** things we did recently with Europe.

**Kyle Gaudreau:** So picking on you here, Carrie, a bit, but this is really, this is building on what we were doing last week for them.

**Kyle Gaudreau:** And I think it's a helpful exercise to talk through.

**Kyle Gaudreau:** And one that, you know, my hunch is, but you can let me know if you all are feeling differently, that we feel probably like pretty good about like the sort of things we should be looking at on our early stage accounts.

**Kyle Gaudreau:** But when it comes to those that we've been working with for a while, maybe that's a little bit less clear of like the types of things we should be, the type of questions we should be asking, how that informs what comes next.

**Kyle Gaudreau:** And so some of this actually came up with Yuriko recently.

**Kyle Gaudreau:** Before I dive into the, you know, the data that we're, you know, pretty used to looking at in Looker, I actually wanted to share just like some quick like scratch math I was doing for this in supporting Carrie last week.

**Kyle Gaudreau:** And I know this is not super pretty and probably not even the clearest to follow, but what Carrie supplied me with.

**Kyle Gaudreau:** So last week was this data from Yurko.

**Kyle Gaudreau:** And essentially what this is saying is, you know, this is what they did in 2025 across their different conversion types.

**Kyle Gaudreau:** They don't have a ton of volume in terms of conversion volume compared to some of our accounts.

**Kyle Gaudreau:** This is the monthly average.

**Kyle Gaudreau:** So, you know, they would average about 12 of these a month.

**Kyle Gaudreau:** Again, pretty, pretty low.

**Kyle Gaudreau:** And this is their 2026 goal.

**Kyle Gaudreau:** And so like significantly higher output of conversion that they need to get to.

**Kyle Gaudreau:** They just went through, I'm not actually 100% sure if they already fundraised or they're going, I think, leading up to that.

**Kyle Gaudreau:** I'm pretty sure that's still in progress.

**Kyle Gaudreau:** I'm not 100% sure on that.

**Kyle Gaudreau:** But ultimately, like the message for them is they have more resources.

**Kyle Gaudreau:** They need to drive more conversion.

**Kyle Gaudreau:** They need to find the ways to driving that more consistently throughout the year.

**Kyle Gaudreau:** And so they're excited about what we've done to generate more traffic for them.

**Kyle Gaudreau:** Part of the partnership now where we have to figure out how can we ultimately supply them with that impact, that clear impact to the bottom line.

**Kyle Gaudreau:** And that can lead to hopefully upsell opportunities with them as well.

**Kyle Gaudreau:** So if we just like look at the monthly average, I mean, we're talking practically 6x.

**Kyle Gaudreau:** Now, this is not like, this is not saying this is all growthx needs to do.

**Kyle Gaudreau:** This is, I believe, Carrie, right, this is their total that they need to hit as a team.

**Kyle Gaudreau:** But the website is a huge part of what they do.

**Kyle Gaudreau:** We're a big part of what they do.

**Kyle Gaudreau:** They do some paid things here and there.

**Kyle Gaudreau:** And so anyways, I just want to set this context because how we may approach this for another account may be a little bit different based off of the context they share, how they think about their goals, etc.

**Kyle Gaudreau:** But what I did thinking through this was, okay, you know, this is their monthly average that they saw.

**Kyle Gaudreau:** What's been their average for traffic recently?

**Kyle Gaudreau:** And this is their broad, like, overall traffic, not just organic.

**Kyle Gaudreau:** If we were...

**Kyle Gaudreau:** Looking at their organic targets, maybe that makes sense to work back to.

**Kyle Gaudreau:** This tells me that their conversion rate overall on their website is 0.07%.

**Kyle Gaudreau:** That is insanely low.

**Kyle Gaudreau:** That is like really, really, really bad.

**Kyle Gaudreau:** You know, this can vary widely, like a really PLG heavy motion that, you know, has like a free trial sign up that it's pretty low friction to getting started.

**Kyle Gaudreau:** It's not unusual to see like double digit conversion rates for those types of clients.

**Kyle Gaudreau:** Call it like 10%, 20%, whatever it may be.

**Kyle Gaudreau:** For, you know, B2B SaaS that has like a sales led motion.

**Kyle Gaudreau:** This also can vary in a lot of ways, but at the very least, like I'd want to see this be like in like the 1% range, call it.

**Kyle Gaudreau:** But even then, like that's kind of low.

**Kyle Gaudreau:** Like it wouldn't be unusual for that to be like 2%, 3% for some brands, even higher.

**Kyle Gaudreau:** And so that initially is like a red flag, right?

**Kyle Gaudreau:** So.

**Kyle Gaudreau:** Cool.

**Kyle Gaudreau:** Already before we dig into their data, like, this is something that's telling me, like, they have a bit of a conversion rate challenge on their website.

**Kyle Gaudreau:** We can't just throw traffic at this problem and for them to get to their goal.

**Kyle Gaudreau:** So building off of that a bit, like, let's just say they don't fix this at all.

**Kyle Gaudreau:** Like, what do they need to do to generate enough traffic to hit this monthly average?

**Kyle Gaudreau:** And so literally all this is doing is dividing these two numbers.

**Kyle Gaudreau:** And that tells us they would need to essentially almost, like, 8x their traffic.

**Kyle Gaudreau:** That's most likely not going to happen.

**Kyle Gaudreau:** They're not going to spend a bunch more on paid.

**Kyle Gaudreau:** They're not going to, we're not going to be able to just throw a ton of content to help them 8x their traffic this year.

**Kyle Gaudreau:** So maybe it looks like something where they need to, like, 2 to 3x their traffic.

**Kyle Gaudreau:** You know, if we do that, what does that look like?

**Kyle Gaudreau:** Okay, that means, like, they still would be at a fairly low conversion rate, but they need to over 2x that.

**Kyle Gaudreau:** And so anyways, I just want to set this context a little bit of, like, again, this could be a little bit different from account to account.

**Kyle Gaudreau:** But before we dive into the data, this tells me like, yes, they need to drive more traffic, but if I'm just throwing traffic at the problem, that's not going to get them anywhere close to their goals.

**Kyle Gaudreau:** And so it's important for us to dig into that level with them and understand it and guide them through that.

**Kyle Gaudreau:** So we're not surprised later on and we're just hoping and praying that like by putting out a lot of content that ultimately hopefully it ladders down, even though I'm not trying to say we wouldn't have some sort of strategy behind that.

**Kyle Gaudreau:** But if it's purely about more traffic, more traffic doesn't get them there.

**Kyle Gaudreau:** More traffic helps, but they also need to address a variety of things in conversion.

**Kyle Gaudreau:** Before I dig in deeper, any questions on that?

**Kyle Gaudreau:** Cool.

**Kyle Gaudreau:** So with that in mind, digging into their data a bit.

**Kyle Gaudreau:** The thing I am curious to hear from the team, if you all do consistently or, you know.

**Kyle Gaudreau:** Maybe this doesn't get as much of your attention.

**Kyle Gaudreau:** The first thing that stands out when I look at their data is, well, one, I mean, certainly excited to see this traffic growth.

**Kyle Gaudreau:** you back this out even further, like traffic growth has not been the problem for this account.

**Kyle Gaudreau:** No doubt we can continue to grow more traffic.

**Kyle Gaudreau:** But the thing that starts to stand out is I'm not seeing this engaged session number follow that same trajectory.

**Kyle Gaudreau:** Like, it is relatively low in comparison to these overall sessions.

**Kyle Gaudreau:** So let's take this, for example.

**Kyle Gaudreau:** So in this time range, we increased by about 2,100 sessions.

**Kyle Gaudreau:** And then for engaged sessions, we added a little under 500.

**Kyle Gaudreau:** So I'm not expecting that maybe to follow the exact same curve.

**Kyle Gaudreau:** But clearly, like we're growing traffic more than we're growing in gates.

**Kyle Gaudreau:** Engaged sessions.

**Kyle Gaudreau:** Why is that important?

**Kyle Gaudreau:** Well, if we're trying to drive them more conversion, and we're just driving a lot of traffic that isn't getting super engaged, that's not going to help them drive more conversion, right?

**Kyle Gaudreau:** You know, an engaged session, you could think about that as a leading indicator to conversion.

**Kyle Gaudreau:** You need someone who's going to be engaged to ultimately convert.

**Kyle Gaudreau:** Now, that can be a little bit of an oversimplification.

**Kyle Gaudreau:** That doesn't mean maybe they wouldn't come back and convert later.

**Kyle Gaudreau:** This doesn't always have to happen in a single session.

**Kyle Gaudreau:** But I think it is fair to assume that if they weren't super engaged to begin with on that session of the content we created, they're probably not going to be super likely to come back, right?

**Kyle Gaudreau:** So that right there, like, that is a clear opportunity to focus on.

**Carrie Chowske:** It's worth noting, too, Kyle, that they're, like, we've predominantly done, like, more top-of-funnel content for them, too.

**Kyle Gaudreau:** Oh, totally.

**Carrie Chowske:** Yeah, so we'd, like...

**Carrie Chowske:** It's a definite correlation there as well, which we've recommended more, but it's not.

**Kyle Gaudreau:** A hundred percent.

**Kyle Gaudreau:** I'm sure there's a variety of things that contribute to this, but even then, I would say, the top of funnel stuff is only going to work if it's engaged, especially too, if we dig into some of this, the signals we need to be careful of is, if it isn't coming through as super engaged, that traffic isn't going to typically be super sticky.

**Kyle Gaudreau:** either, right?

**Kyle Gaudreau:** The thing to keep in mind is for Google, what they're trying to do as much as possible is there is a user behind this search.

**Kyle Gaudreau:** They have an intent to find a useful answer.

**Kyle Gaudreau:** If they are bouncing quickly and not engaging with our content, that's communicating to Google that they're not finding a useful answer.

**Kyle Gaudreau:** So we may be able to drive some traffic, but if we consistently aren't engaging that traffic, Google is going to stop ranking that content eventually.

**Kyle Gaudreau:** So I'm sure we'll see that pattern in here if we kind of dig into this.

**Kyle Gaudreau:** So before digging into the Engage session stuff, the other thing I'm curious about is how much momentum do we really have here?

**Kyle Gaudreau:** How much can I continually expect this to grow?

**Kyle Gaudreau:** I know that this chart can break for a lot of our accounts, and this is probably something that we need to refine and find different ways of showing this data.

**Kyle Gaudreau:** By the way, just to make sure we're all understanding this again, this trend that you'll see on a lot of our accounts, this drop in September, this goes back to Google's parameter changes, dropping tools such as even their own tool, Google Search Console, SEMrush, et cetera, that used to be able to pull 100 search results at once, and that was removed.

**Kyle Gaudreau:** And that leads to things like impressions and sometimes queries looking a little wonky when you look at a longer trend.

**Kyle Gaudreau:** But what this is telling me is, you know, yes, there

**Kyle Gaudreau:** There's a little bit of a drop here, but, you know, I would be more worried if that's, continual over time.

**Kyle Gaudreau:** But, like, generally, like, we have upward momentum in terms of rankings.

**Kyle Gaudreau:** I know this chart can be, like, a little confusing.

**Kyle Gaudreau:** You know, like, the green at the bottom, that's the first position.

**Kyle Gaudreau:** You know, that purple is also first page here.

**Kyle Gaudreau:** So, good, we're seeing growth in each of these.

**Kyle Gaudreau:** But the other thing that's, like, really standing out, all the other colors, like, that is, like, lower page rankings.

**Kyle Gaudreau:** That is momentum of our content continuing to build.

**Kyle Gaudreau:** So, that's a positive for sure.

**Kyle Gaudreau:** You know, there's probably some things we can dig into and understand from a refresh standpoint of, like, does need a little bit more to get to that top of page?

**Kyle Gaudreau:** But this tells me that, at least from this perspective, we're looking good to continue this trend of, like, increasing our traffic.

**Kyle Gaudreau:** And we should expect more in the not-too-distant future.

**Kyle Gaudreau:** I would certainly want to...

**Kyle Gaudreau:** Dig more into, like, what clusters are driving that and, you know, try to understand that at a deeper level, not just, like, broadly.

**Kyle Gaudreau:** But I do want to focus on this kind of, like, engage session piece here because if we just continue to drive this and this blue line is not moving up, then that's not going to be helping us much.

**Kyle Gaudreau:** So the next thing to kind of, like, think about is, like, what content is driving engagement?

**Kyle Gaudreau:** What isn't driving engagement?

**Kyle Gaudreau:** One way of thinking about this, this isn't necessarily, like, a hard, fast rule, but generally speaking, like, a good engagement rate is typically going to be somewhere around, like, 50 plus percent.

**Kyle Gaudreau:** You could call it, like, 40 to 50 is, like, pretty good, and obviously you want it as high as possible.

**Kyle Gaudreau:** I would say, like, I saw this with WebStacks recently, and I still need to dig into it.

**Kyle Gaudreau:** But some of their content is, like, 95% engagement or whatever.

**Kyle Gaudreau:** Would you see that?

**Kyle Gaudreau:** That's kind of, like, eh, there's...

**Kyle Gaudreau:** There's broken here.

**Kyle Gaudreau:** There's no way almost every single person seeing this content is engaged.

**Kyle Gaudreau:** But generally speaking, if you see things that are sub 40%, especially well below that, that is a signal of something is going on here, perhaps.

**Kyle Gaudreau:** And what that is, it can be a variety of different things.

**Kyle Gaudreau:** Now, I realize as I go through this, some of this is a bit more manual in terms of the investigation of it.

**Kyle Gaudreau:** But truly, this is where the gold can be for these programs that have started to continually create a lot of content over time, is finding those refresh opportunities, finding ways of improving the user experience, learning from that in some way to inform what also you should be thinking about the net new.

**Kyle Gaudreau:** That is how you're going to get to that next level of growth and impact down the funnel in my experience.

**Kyle Gaudreau:** So, and additionally, like some of what Marcel shared earlier, you know, about what content OS is going to be solving for and how keeping the pulse on a lot of this stuff can be challenging.

**Kyle Gaudreau:** Certainly, there is going to be a time where this will be a lot easier for us and less manual, but I'm sure there will still be certain things you'll need to dig into.

**Kyle Gaudreau:** But understanding the why behind it is also super helpful to how would you approach this and how is OS making this more efficient for you, right?

**Kyle Gaudreau:** So, anyway, so digging into this a little bit.

**Kyle Gaudreau:** So, as I mentioned, like 40%, 50% plus is kind of like where we want to be.

**Kyle Gaudreau:** So, okay, cool.

**Kyle Gaudreau:** Like some of this top stuff here, you know, pretty good.

**Kyle Gaudreau:** But what I'm really looking for is like what kind of patterns are sticking out of like low engagement.

**Kyle Gaudreau:** So, here's a couple.

**Kyle Gaudreau:** I see this blog here, a use case page, another use case page, pretty low, another one.

**Kyle Gaudreau:** Pretty low.

**Kyle Gaudreau:** Okay.

**Kyle Gaudreau:** So like one of the things that's clearly standing out here is like the use case pages are pretty low in terms of their engagement rates, like, you know, 10%, 9%, 16, like, okay, there's clearly something like not working here that we need to build on because, you know, we don't want to just like, we don't want to just treat this as like some sort of vanity metric, right?

**Kyle Gaudreau:** Like, it's great that we're driving traffic here, but look at 189 sessions in this time period, given it's a longer time period, but in only 10 of those being engaged sessions, right?

**Kyle Gaudreau:** And I would bet if we look at some of this, let's see.

**Kyle Gaudreau:** As a reminder, I think I showed this in the previous session, but like you can click on some of these and like update the chart.

**Kyle Gaudreau:** Okay.

**Kyle Gaudreau:** So like, this is like a relatively new one that's growing.

**Kyle Gaudreau:** That's good.

**Kyle Gaudreau:** But sometimes what you'll see in these, let's see if I can find a good example.

**Kyle Gaudreau:** Maybe not.

**Kyle Gaudreau:** Not so far.

**Kyle Gaudreau:** But sometimes what you'll see with these is it's not uncommon that you look at that kind of low engagement and you may see strong traffic here and then traffic starting to drop because of that low engagement related to kind of I was talking about earlier.

**Kyle Gaudreau:** But even still, like, there's a clear pattern here of, like, their use case pages need a bit more love.

**Kyle Gaudreau:** So let's take a look at that, like, in particular.

**Kyle Gaudreau:** Like, there's a few different ways of, like, kind of unpacking, like, what's happening with these.

**Kyle Gaudreau:** It's not just always going to be about user experience.

**Kyle Gaudreau:** We also need to think about, like, what are the types of searches we're capturing here?

**Kyle Gaudreau:** And so one way you could approach that is just going into their search console, going into something like this, pulling out one of these particular use cases.

**Kyle Gaudreau:** Okay.

**Kyle Gaudreau:** Like, you know, this is.

**Kyle Gaudreau:** It's not too surprising to see, like, it's targeting employee alerts, the queries are pretty spot on and related to that.

**Kyle Gaudreau:** One of the things I'm curious about, though, is like, I don't know, employee alert itself feels like kind of broad.

**Kyle Gaudreau:** Like, let's see what else is ranking for this.

**Kyle Gaudreau:** Oops.

**Kyle Gaudreau:** What did I just do?

**Kyle Gaudreau:** Apparently, when you use that new tab hockey in Zoom, it tries to do a screenshot.

**Kyle Gaudreau:** But, yeah, I learned.

**Kyle Gaudreau:** So digging into this a little bit more, like, what I'm going to be looking for is, like, is there anything that's, like, kind of standing out of other ranking content for other brands that is just, like, it's, are they looking for something else that is, and that is a sign of why Yurko is, you know, seeing low engagement?

**Kyle Gaudreau:** I know that Envoy is...

**Kyle Gaudreau:** Isn't really necessarily what they would consider like a direct competitor, just from my own knowledge of them.

**Kyle Gaudreau:** So maybe like some subtle signs there, but a bit of like a mixed bag.

**Kyle Gaudreau:** And I think that just like speaks to the broadness of the intent of this.

**Kyle Gaudreau:** So, so far what I'm seeing is like, sometimes you'll look at that query data and it can be clear like, hey, we're just capturing a lot of traffic that, well, the URL makes sense, the content makes sense, but we're actually capturing in terms of queries is too broad or out of left field for that brand.

**Kyle Gaudreau:** So, so far that does not, at least for this particular page, appear to be the case.

**Kyle Gaudreau:** But let's dig into like the actual page and see like what's going on here.

**Kyle Gaudreau:** I've already kind of looked at these pages and had a bit of time to dig into them.

**Kyle Gaudreau:** But what I would say is like some basics of, okay, yeah, this, you know, nailing the keyword and things of that nature.

**Kyle Gaudreau:** But, like, this user experience at the top is not bad.

**Kyle Gaudreau:** I personally don't love their website.

**Kyle Gaudreau:** Carrie has heard me say this before.

**Kyle Gaudreau:** Visually, I don't find it the most appealing.

**Kyle Gaudreau:** I think they need to work on that in a variety of ways.

**Kyle Gaudreau:** But I'm not convinced that is the core problem.

**Kyle Gaudreau:** They have a lot of other pages that are getting high engagement.

**Kyle Gaudreau:** Generally, like, this top section, like, could I nitpick of, like, the flow and things of that nature?

**Kyle Gaudreau:** Probably.

**Kyle Gaudreau:** But, like, I don't know.

**Kyle Gaudreau:** I'm not seeing anything that I'm just, like, oh, you do this and it's going to, like, game change, like, this portion of it.

**Kyle Gaudreau:** But when I get down to here, this is where, like, the user experience kind of really breaks down for me.

**Kyle Gaudreau:** They're kind of, like, just doing this hybrid.

**Kyle Gaudreau:** This feels very, like, SEO-centric and not user-centric.

**Kyle Gaudreau:** And so, you know, maybe one of the hypotheses here is, like, okay, like, how could we create something that's a little bit more engaging?

**Kyle Gaudreau:** Maybe some of this content can continue to exist, but break it up in different ways.

**Kyle Gaudreau:** And so, what that looks like...

**Kyle Gaudreau:** You know, there's different ways of kind of like getting inspiration.

**Kyle Gaudreau:** One of the things we could do is going back to that search.

**Kyle Gaudreau:** And let's see like what other competitors are doing.

**Kyle Gaudreau:** I know one of their competitors, Utext, actually has like a pretty good experience.

**Kyle Gaudreau:** Actually, okay, this is interesting.

**Kyle Gaudreau:** This page was not ranking before.

**Kyle Gaudreau:** But I know that this page has been the one that's typically ranked.

**Kyle Gaudreau:** Maybe it was like a variant or something like that last time I looked at it.

**Kyle Gaudreau:** First, I would just say like, I'm not going to turn this into like a bigger like training of like UX and things of that nature.

**Kyle Gaudreau:** But like, just like right off the bat, like I would say this just looks like way more clean.

**Kyle Gaudreau:** Product features are like much more front and center.

**Kyle Gaudreau:** And just like it, this is a brand, like if you saw both of those, like which one of those would you probably more trust?

**Kyle Gaudreau:** To like potentially buy.

**Kyle Gaudreau:** So that's one element for sure.

**Kyle Gaudreau:** But just generally like, okay, like the top of the flow of this page is actually like not that different.

**Kyle Gaudreau:** But like you can see here as you get to the bottom part is like, okay, maybe like some similar content is certainly shorter form content, but breaking it up into this kind of like checkerboard format where you have like a nice visual that supports it.

**Kyle Gaudreau:** Like this is just more readable and user friendly for this type of intent.

**Kyle Gaudreau:** And so, again, I don't want to get this like too into the weeds on like the UX, but like looking at some of the other ranking pages and what some of the user experiences they have can be leveraged as inspiration for you to maybe make some recommendations for them to rethink like what they're doing.

**Kyle Gaudreau:** And this doesn't mean to copycat exactly what's out there, but clearly they can improve this user experience here.

**Kyle Gaudreau:** Now, knowing...

**Kyle Gaudreau:** knowing...

**Kyle Gaudreau:** And knowing your co a bit, knowing how Jessica thinks a bit, who's our POC over there, I think what she would probably say, but Carrie, keep me honest, is that she would be worried if we revamped those pages that they would lose all this traffic, right?

**Kyle Gaudreau:** Would that be accurate?

**Carrie Chowske:** A thousand percent, yes.

**Carrie Chowske:** And that page was 100% a keyword grab.

**Carrie Chowske:** It was performing, so we consolidated some other content and put it on that page.

**Kyle Gaudreau:** Totally.

**Kyle Gaudreau:** So let's look at that from a couple angles.

**Kyle Gaudreau:** So one, let's look at this very different user experience, and I know it wasn't ranking like it was before, but let's just see, go into SEMrush and look at this URL and try to get a sense, and we could do this for some of their other pages as well, but is this actually ranking relatively well?

**Kyle Gaudreau:** Hopefully this doesn't blow up my whole point.

**Kyle Gaudreau:** here because when I looked at it before, it actually was.

**Kyle Gaudreau:** Okay.

**Kyle Gaudreau:** So, you know, some like, you know, ups and downs that, you know, are not too unusual for any ranking, but like the ranking number three for employee alert, eight for employee alert system, mixed bag of other things underneath.

**Kyle Gaudreau:** But anyways, like what this is showing so far is like a page like that can rank for a keyword like that.

**Kyle Gaudreau:** My, I think I would probably be fair in assuming that that page is probably driving way better engagement and is probably converting more than the other.

**Kyle Gaudreau:** So kind of layer number one of like thinking about that argument.

**Kyle Gaudreau:** The other though, is like going back to some of what I was talking about earlier.

**Kyle Gaudreau:** If we just look at like these use case pages and actually just to make this easier, I did pull out this data.

**Kyle Gaudreau:** I just exported it from that table.

**Kyle Gaudreau:** And, you know, that just at times like easier to play around with the data from, from Looker.

**Kyle Gaudreau:** you just export from the tables and just upload into a spreadsheet.

**Kyle Gaudreau:** So, all right.

**Kyle Gaudreau:** So.

**Kyle Gaudreau:** Like, let's take, I think I'm still filtered for engagement.

**Kyle Gaudreau:** Oops, sorry.

**Kyle Gaudreau:** There we go.

**Kyle Gaudreau:** Oh, okay.

**Kyle Gaudreau:** They all still meet that criteria.

**Kyle Gaudreau:** All right.

**Kyle Gaudreau:** So apparently these are all our use case pages.

**Kyle Gaudreau:** I actually thought they had more for whatever reason, but maybe not.

**Kyle Gaudreau:** So here's the content we kind of like stand to, or the traffic we stand to lose about 850 sessions.

**Kyle Gaudreau:** I think this was like a similar time.

**Kyle Gaudreau:** I think this was actually going back to December, if I remember correctly.

**Kyle Gaudreau:** So, you know, past couple months, but only like 79, 80 of those are actually engaged.

**Kyle Gaudreau:** So we're not really talking about much risk here.

**Kyle Gaudreau:** Like there's not like you're talking about maybe a couple sessions a day that we're talking about here.

**Kyle Gaudreau:** So like keeping that context in mind, like we don't want to be just chasing this traffic number all the time.

**Kyle Gaudreau:** If we always chase this traffic number and they're seeing low engagement, they're not going to be seeing the conversions ultimately that we're trying to get them to.

**Kyle Gaudreau:** So the point I would probably make to Jessica in this case is, hey, I think we can really improve this user experience.

**Kyle Gaudreau:** Here are some of our ideas around that.

**Kyle Gaudreau:** But, you know, if you need further support and thinking around, like, CRO, UX, like, feel free to pull myself into Lull, et cetera.

**Kyle Gaudreau:** I've done a ton of different experimentation around these things for a ton of different websites.

**Kyle Gaudreau:** So I'm sure I can be helpful for you all as you think through that.

**Kyle Gaudreau:** But also, like, you know, hopefully we're working with some teams that have their own perspective and we can come to some sort of, you know, alignment of, like, what should be actioned here and what is reasonable.

**Kyle Gaudreau:** And everyone's feeling good about it.

**Kyle Gaudreau:** So I would make the case, like, hey, we can improve this user experience.

**Kyle Gaudreau:** We don't have a lot that we're risking here if you really need to drive conversion.

**Kyle Gaudreau:** Like, a lot of these queries that are going to these pages are those that are probably going to be closer to, like, lower funnel intent.

**Kyle Gaudreau:** It's people who are starting to look around.

**Kyle Gaudreau:** Around features, functionality, things related to some level of buying intent for their platform, they need to be ranking here.

**Kyle Gaudreau:** They need to have a good user experience.

**Kyle Gaudreau:** So I would say the risk is like relatively low here.

**Kyle Gaudreau:** So this would be like probably like at this point, the number one thing I would focus on of like Jessica, if you could do nothing else outside of, you know, some other things I've shared with her, like I would improve this user experience on these pages.

**Carrie Chowske:** And she even brought up the other day too, like she wanted to try some A-B testing.

**Kyle Gaudreau:** I'm like, if she's that hesitant, I'm just going to tell her like, test it.

**Kyle Gaudreau:** mean, don't like, yeah, can't her.

**Kyle Gaudreau:** 100%.

**Kyle Gaudreau:** Yeah, you know, it's a little tricky at times with Jessica specifically.

**Kyle Gaudreau:** But the other thing just to call out too is like, I'm sure you all do some form of this already, but like just take the time to like see what the latest is on like, what is the user journey look like?

**Kyle Gaudreau:** Like on their website, like, are you seeing anything in there that like just looks like potentially broken or confusing?

**Kyle Gaudreau:** And so at times, like just sprinkling in those different insights and recommendations, our clients appreciate.

**Kyle Gaudreau:** And so like one of the things that has stuck out for a while, and I think they've just been slow to action, this is their trial form.

**Kyle Gaudreau:** It is terrible.

**Kyle Gaudreau:** It is very confusing.

**Kyle Gaudreau:** It is long.

**Kyle Gaudreau:** It's not like it doesn't have anything in terms of social proof, anything that like would excite someone to get started.

**Kyle Gaudreau:** They have weird things like this where you have to click this and then you have to add your info here.

**Kyle Gaudreau:** So I'm pretty confident this is another thing that's like driving their low conversion rates.

**Kyle Gaudreau:** And so anyways, I don't want to turn this into like a bigger like CRO session, but this is one of the things I said to Jessica, like this, this actually should be like the number one thing you do on your website right now is.

**Kyle Gaudreau:** Like fix this.

**Kyle Gaudreau:** Like this should be like high conversion, low friction to getting started.

**Kyle Gaudreau:** This is probably where most people want to go.

**Kyle Gaudreau:** It's your primary CTA.

**Kyle Gaudreau:** This is just a crappy user experience.

**Kyle Gaudreau:** And so I had walked Jessica through, you know, some examples of like how to think about it.

**Kyle Gaudreau:** Like if you have to have a really long form, which ideally like, do you really need to ask all these questions?

**Kyle Gaudreau:** Can you, can you strip some of these fields out?

**Kyle Gaudreau:** If you do need a long form, like a sequential form can work really well to like show you a quick example that I showed Jessica having been at home base.

**Kyle Gaudreau:** I had a chance to see how this converted and tested different things.

**Kyle Gaudreau:** And we had a pretty long form here.

**Kyle Gaudreau:** Um, but like, if you ever run into a customer that has something like that, like a multi-step form can work quite well.

**Kyle Gaudreau:** Like, um, where you're just asking for a little bit less each time you show them what step they're at in the journey.

**Kyle Gaudreau:** Uh, you have some social proof alongside, like those are the subtle.

**Carrie Chowske:** Little things that can improve conversion.

**Carrie Chowske:** anyways, like, we can...

**Carrie Chowske:** too, Kyle, like, it's important with this one, like, remember she was saying about it being, like, regulatory stuff where they have to collect all that information.

**Carrie Chowske:** It's like, this is really important because they can't really cut a lot of that, right?

**Carrie Chowske:** So I thought this was a really great idea for them to, like, do this multi-step thing.

**Kyle Gaudreau:** Totally.

**Kyle Gaudreau:** So, this doesn't solve their problem alone, but, like, this is an example of something where we can give recommendations.

**Kyle Gaudreau:** We're going to be relying on them to take some sort of action.

**Kyle Gaudreau:** And so what we need to focus our time in on is what are some things that we do have in our control.

**Kyle Gaudreau:** We can make some recommendations around use cases.

**Kyle Gaudreau:** We need to get their buy-in around that, of course.

**Kyle Gaudreau:** But I would also look at, like, are there other blogs that are just, like, let's look at blogs that are relatively low engagement.

**Kyle Gaudreau:** So, I'll just filter for less than 40

**Kyle Gaudreau:** And so that should show me, okay, so again, where I pulled this, by the way, just so it's clear, like you can go to this table, the benefit here is like we're obviously filtering for just our content here, and I can just go here, I can export the data, that will give me a CSV that I can upload to here, and the reason being is it just like makes it easier to like go filter and like find different things.

**Kyle Gaudreau:** Like you could scroll through it, but Yurko has a decent amount of content, so this just makes it a bit easier.

**Kyle Gaudreau:** So the way I would probably think about this, again, this was like back into about December time range, so a couple months of data.

**Kyle Gaudreau:** I'd probably look somewhere in the range of like, you know, you could call it like maybe like 50 plus sessions or so that have low engagement.

**Kyle Gaudreau:** Like what's happening with some of these pages that, you know, what are some of the patterns of like low engagement, high engagement?

**Kyle Gaudreau:** I was going to go.

**Kyle Gaudreau:** Go through and show a little bit of, like, how you could approach this with, like, say, a Claude code to help you out, or Claude co-work, rather.

**Kyle Gaudreau:** Unfortunately, like, Claude's been acting quite weird on my computer and was, like, causing, it was, like, basically sucking up all my RAM earlier.

**Kyle Gaudreau:** And so don't think I'll be able to do that.

**Kyle Gaudreau:** But, like, just looking at a few that I, like, pulled out prior to this is, like, this is an example of a page that had relatively, like, low engagement.

**Kyle Gaudreau:** So, again, like, I would continue to look at the patterns I was looking at earlier.

**Kyle Gaudreau:** Like, is that a function of the queries we're ranking for, or is it the content and what we're putting into this content?

**Kyle Gaudreau:** So, I mean, I would say, like, overall, I'm just going to do a quick skim just for, like, time's sake.

**Kyle Gaudreau:** But, you know, we have some CTAs, like, clear headers, which is good.

**Kyle Gaudreau:** But, I don't know, you know, maybe missing a few elements that we could consider adding into the mix.

**Kyle Gaudreau:** But, this

**Kyle Gaudreau:** This is one that was considered high engagement.

**Kyle Gaudreau:** So, okay, you know, generally like, oh, actually, sorry, this was one that was also low engagement.

**Kyle Gaudreau:** Sorry.

**Kyle Gaudreau:** What stands out about this is like, some of these headers, maybe like the formatting got broken, like, right, like, so like, you know, they didn't have H3s until a month ago.

**Kyle Gaudreau:** Yeah, again, so I'm not trying to like, you on the spot and say like, y'all, I'm just trying to like, you know, use this as a demonstration of like, some of the things that could be like, hiding out underneath that could be driving better engagement.

**Kyle Gaudreau:** So like, one of the things here is like, yeah, like, it sounds like Carrie's already on it, which is great of like, the way we're handling headers here does not lead to the most visually appealing experience here and maybe a little inconsistent.

**Kyle Gaudreau:** Trying to find, so this was an example of something that was like, really high engagement for them.

**Kyle Gaudreau:** And one of the patterns I've noticed for anything that's high engagement, there's more visuals, there's more tables.

**Kyle Gaudreau:** There's way clearer formatting of like bullets and bolding.

**Kyle Gaudreau:** It's just like generally better to scan through and more visually and just clean looking.

**Kyle Gaudreau:** And so that was one of the things that certainly stuck out around that.

**Kyle Gaudreau:** And so the pattern I would just not lose sight of here is like we cannot always just throw net new content at the problem.

**Kyle Gaudreau:** We should be going back and enriching these pages.

**Kyle Gaudreau:** We should be continuing to learn what are the pages that, you know, have the most opportunity behind them.

**Kyle Gaudreau:** You know, if we wanted to, you know, there's different ways you could kind of like break down that analysis.

**Kyle Gaudreau:** You could look at something like, you know, let's go to Yerko again.

**Kyle Gaudreau:** Actually, let's look at just the blog in SEMrush.

**Kyle Gaudreau:** Um, and we could look at like, uh, one angle is like,

**Kyle Gaudreau:** On engagement, of course, as I mentioned, but you could also pull out, like, how do you also look at, like, engagement as well as, call it, like, ranking 20 to, or sorry, 11 to 50, call it.

**Kyle Gaudreau:** So, you know, not page one yet, you know, what blogs have some low-hanging fruit.

**Kyle Gaudreau:** So, again, I wish I could do a little bit of, like, Claude walkthrough, I'll follow up with, like, a loom on that, but what you could do is you could export this data here, so that gives me, like, all, like, the keywords that are ranking below page one, and, like, what pages have opportunity behind them, and then I could compare that against this data, which also then allows me to think about the engagement rates of those.

**Kyle Gaudreau:** And so, if I consider those two signals, I'm trying to think about, like, where do we have, like, some bubbling keyword opportunity, but also, like, lower engagement rates, and should we...

**Kyle Gaudreau:** Go back and start to enrich and improve those experiences to hopefully push that up and actually be high-ranking, good-quality content.

**Kyle Gaudreau:** So one way you could kind of approach that.

**Kyle Gaudreau:** Claude can be great for that.

**Kyle Gaudreau:** You could even do this outside of co-work and probably get some pretty decent results of just like feeding in those two data tables and essentially giving that guidance of trying to look for those common patterns, like which URLs should you really be focusing on?

**Kyle Gaudreau:** What are those top 20, top 40, whatever it is?

**Kyle Gaudreau:** And then starting to put that into your refresh queue.

**Kyle Gaudreau:** The thing I would just stress to do is while you could do that fast, you could just dump it into Claude, get its insight, I would spend the time in actually looking at this content, looking at the SERPs, what is ranking, what's working, what are the patterns of other content that we're not doing?

**Kyle Gaudreau:** And as we go through and we go through those refreshes, hopefully having more of a perspective of like, what do we need to action here for this?

**Kyle Gaudreau:** It's actually to be more effective rather than just hoping the different automated systems bring something together, whether it's our agentic workflows or what Claude spits out that you can have some sort of guidance on what to do.

**Kyle Gaudreau:** Questions?

**Kyle Gaudreau:** this like a quick like check?

**Kyle Gaudreau:** Like, is this a lot of stuff you all already do today?

**Kyle Gaudreau:** You feel like this is kind of something you're already well accustomed to?

**Kyle Gaudreau:** Or is this, hopefully this is helpful in some things that you can build on?

**Katya Luscomb:** I know, I was going to say, know for me, it's like, there was some surface level of this that I was doing, but this is really helpful as like a much deeper dive and some, some angles on how to approach it and how to think about it in, in a more thorough way.

**Kyle Gaudreau:** Cool, cool.

**Kyle Gaudreau:** And what I'll say, and this is a bit of the challenge.

**Kyle Gaudreau:** Sometimes and like everything I just went through, like there's different ways of approaching this.

**Kyle Gaudreau:** There's layers I didn't go into that we could probably dig into.

**Kyle Gaudreau:** That is part of what I've always actually enjoyed about this type of work.

**Kyle Gaudreau:** I think I've mentioned this in the not too distant past of like there's, you know, you kind of have to put your detective hat on and kind of like dig into different things.

**Kyle Gaudreau:** You're like, oh, there's something interesting.

**Kyle Gaudreau:** Let me dig in deeper to understand the why behind that.

**Kyle Gaudreau:** Is that important trend to the larger trend that I'm seeing?

**Kyle Gaudreau:** And just the more you can think about like, where do they need to get to?

**Kyle Gaudreau:** What is the impact we need to drive?

**Kyle Gaudreau:** And in focusing, I realize like it's so easy to rabbit hole in these different systems.

**Kyle Gaudreau:** And there's a lot of data that can sometimes be distracting.

**Kyle Gaudreau:** But I think the more intentional you are behind that and you can dig in that way, finding that, finding those nuggets, you can kind of slice that in a variety of different ways.

**Kyle Gaudreau:** And so what I walked through today, I think.

**Kyle Gaudreau:** Is a pattern that I'd assume like a decent amount of our accounts could use this sort of love.

**Kyle Gaudreau:** But there's other things certainly to dig into outside of that.

**Kyle Gaudreau:** Not to put you on the spot, Talal, but I'm curious of what I've run through.

**Kyle Gaudreau:** Is there anything like you would add as like enhancement or like an additional thing in this workflow to call out?

**Talal Syed:** Talal, think the only thing I would probably add is that I really like to look at Google Search Console data.

**Talal Syed:** So there's an extension in the team account called Search Analytics for Sheets.

**Talal Syed:** So what that allows you to do is pull the GSC data through the API so you aren't limited to a thousand rows.

**Talal Syed:** And that can be very useful for essentially manipulating and figuring out what's actually going on with an account.

**Talal Syed:** So that's usually something that I almost always do.

**Talal Syed:** So that's one thing that you can explore around with as well.

**Kyle Gaudreau:** Yeah, that's a good call.

**Kyle Gaudreau:** Thank

**Kyle Gaudreau:** Thanks for calling that out.

**Kyle Gaudreau:** Recently upgraded this plan, by the way, and if you guys ever run into limits with this, now you can pull 100,000 rows at once.

**Kyle Gaudreau:** This is just a bit of like a stopgap tool, like some of this should be easier once we have ContentOS running, but I think there's always going to be some application of using a tool like this.

**Kyle Gaudreau:** So if you're not familiar with it, yeah, it just allows you via the API to pull different date ranges.

**Kyle Gaudreau:** You can group by different things.

**Kyle Gaudreau:** And so I could say like group by date in query.

**Kyle Gaudreau:** I could add filters, right?

**Kyle Gaudreau:** Like if I wanted to like say, I wanted to like filter for their non-brand traffic, I could say like Yerko.

**Kyle Gaudreau:** If you put in, oh, I think everyone's familiar with this, but like if you put in the pipe for regex, that's an or.

**Kyle Gaudreau:** And so here's another spelling and I could then just record.

**Kyle Gaudreau:** Request that data and what that would give me, and just for time's sake, I won't do this live, but that would give me day-over-day data by query that I could start to pull out in review.

**Kyle Gaudreau:** You could do page, you could do different cuts of this data, depending on what you're trying to look at.

**Kyle Gaudreau:** And so that can sometimes allow you just to dig in a little bit deeper.

**Kyle Gaudreau:** But at times as well, like playing around with filters and GSC is another way of approaching this, for sure.

**Kyle Gaudreau:** Dang, all right.

**Kyle Gaudreau:** We're actually, that took a little bit longer than I was anticipating.

**Kyle Gaudreau:** Wanted to look at one other example that is a bit more of like an early stage account.

**Kyle Gaudreau:** And so this is one where I don't have a lot of context on Cresta.

**Kyle Gaudreau:** I know that we just started publishing, I believe, back in like December.

**Kyle Gaudreau:** And so one of the things, like, obviously, if you're in an account, like, you're looking at this a lot.

**Kyle Gaudreau:** But the things I'm typically trying to look for here is...

**Kyle Gaudreau:** Like one in an early stage account, like how much have we published and are we actually starting to see like sessions across a lot of that?

**Kyle Gaudreau:** So I can see we've published down here 23 assignments.

**Kyle Gaudreau:** Looks like we've tested a few different clusters, relatively like even spread, which is good.

**Kyle Gaudreau:** You know, at this phase, we don't want to be like too presumptuous and put all our eggs into a single basket.

**Kyle Gaudreau:** I feel like we're pretty good about this across most accounts, but perhaps there's some edge cases where we're doing less of this.

**Kyle Gaudreau:** But, you know, a red flag for me looking at this would have been like we're just putting a lot of data, a lot of content into a single cluster.

**Kyle Gaudreau:** Like we don't know at this phase is what's going to work.

**Kyle Gaudreau:** So usually you want to be like trying to diversify around like somewhere in the ballpark of three to four, maybe less if there's like a bigger opportunity that you're trying to validate.

**Kyle Gaudreau:** But so far, that's that's good.

**Kyle Gaudreau:** But looking at.

**Kyle Gaudreau:** You you

**Kyle Gaudreau:** So this helps if you're ever just trying to get like a very quick pulse on how your content's indexing, this is just like a very quick check that you could do against that is like, okay, we saw that there was 23 assignments that have been published.

**Kyle Gaudreau:** And so far, we have 22 that have driven the session.

**Kyle Gaudreau:** So, so far, like no red flags in terms of this content getting indexed, which is good.

**Kyle Gaudreau:** The thing I have seen a few times, and I'll just call out, I found a few of these recently, make sure that your ME is going through and updating the rules, the case statements for that powers this filter.

**Kyle Gaudreau:** I think everyone, you know, unless someone wants to raise their hand, they're not familiar with what I'm referring to.

**Kyle Gaudreau:** It seems like we all are, and it's just a part of our process as we publish, but I found a few.

**Kyle Gaudreau:** instances where I only see like, you know, I see a number here that's far smaller, that initially would make me worried that like we're having an indexation problem.

**Kyle Gaudreau:** But the first thing I'm going to check before like going into this rabbit hole of that is like, check your case statement, like how many URLs are in that.

**Kyle Gaudreau:** Talal, one of the things that's been on my mind, it's like a pre-OS thing to consider is like, I feel like there's got to be some way via the Airtable API that we can do something more automated that is pulling out published URLs into a spreadsheet that can be referenced so the team doesn't always have to update these case statements.

**Kyle Gaudreau:** I'm not 100% sure how that's going to come together.

**Kyle Gaudreau:** But now that I've just seen a few examples of our clients recently where that's happened, that's just like one of the things that back in the moment.

**Kyle Gaudreau:** Okay, so so

**Kyle Gaudreau:** It's good to see that we're seeing relatively good indexation.

**Kyle Gaudreau:** Good to see actually this trend in traffic starting to uptick, but it's limited data right now.

**Kyle Gaudreau:** The thing I would stress as you're talking about this with your customers when you see these sorts of trends is certainly frame this as a positive, but try to be more cautiously optimistic here.

**Kyle Gaudreau:** Don't overly celebrate and say, we've figured this out and now we're going to be seeing even crazier growth.

**Kyle Gaudreau:** Three weeks of traffic is not going to make a trend typically at this early phase of an account.

**Kyle Gaudreau:** What you're trying to understand is how sticky is this traffic going to be?

**Kyle Gaudreau:** And so, so far, like, you know, going back to like thinking about some of the engagement rate things we were talking about earlier, seeing pretty good engagement rates across the board outside of this one that's like a bit.

**Kyle Gaudreau:** So maybe that's something to dig into all this.

**Kyle Gaudreau:** This is like kind of odd.

**Kyle Gaudreau:** This is like the one thing that's a blog and the rest of these aren't.

**Kyle Gaudreau:** So I'm not sure what to do with that at this point in time, but maybe that's not worth paying attention to.

**Kyle Gaudreau:** So that piece is good.

**Kyle Gaudreau:** What I'd also probably want to look at is to understand like what's going on with this traffic at this point in time is similar as we looked at earlier.

**Kyle Gaudreau:** Like what are we seeing in terms of some of these query rankings?

**Kyle Gaudreau:** Like right now you're seeing a little bit more volatility than what we were seeing for a year ago, right?

**Kyle Gaudreau:** Like we see some growth, I would say, overall, but now it's starting to come back down again.

**Kyle Gaudreau:** Not super unusual at this phase, but kind of leads to my cautious, like be cautiously optimistic.

**Kyle Gaudreau:** Don't just assume like we're going to continue to see this strong growth.

**Kyle Gaudreau:** The other thing I would be trying to think about is like, where is this growth coming from?

**Kyle Gaudreau:** Like, is this, are there certain patterns?

**Kyle Gaudreau:** Patterns of the types of content.

**Kyle Gaudreau:** And certainly, like, we have one post that's kind of, like, dominating here, if you will.

**Kyle Gaudreau:** Like, these top two, I guess, are driving most of it.

**Kyle Gaudreau:** But, like, the pattern I would be careful with, and hopefully we're already doing this, is, like, if we need to drive them really strong growth over the next 12-plus months, it's good to find these sorts of wins of the alternatives content, the versus content, all of that kind of stuff.

**Kyle Gaudreau:** But there's a natural headroom when it comes to that.

**Kyle Gaudreau:** Like, they only have so many competitors that they're going to care about, right, writing this content for.

**Kyle Gaudreau:** So hopefully we feel like we're seeing some signals from other content, which it looks like we are.

**Kyle Gaudreau:** But that's one of the things I would be thinking about is, like, here, you know, I'm assuming this is driving, yeah, a lot of that trend that we're seeing.

**Kyle Gaudreau:** Encouraging to see that.

**Kyle Gaudreau:** don't know.

**Kyle Gaudreau:** I don't know.

**Kyle Gaudreau:** I

**Kyle Gaudreau:** I would certainly be looking at are there other competitor comparisons we could be doing, but that may give us like, say, like two months more of content, maybe more, maybe less, but somewhere in that ballpark.

**Kyle Gaudreau:** Some growth for sure, but hopefully you're also going to be thinking about diversifying the different clusters that you're going through here and where we're going to have more headroom.

**Kyle Gaudreau:** So things like, you know, even these best lists and things of that nature, there's going to be some natural headroom.

**Kyle Gaudreau:** But this at least is another theme where it's not about another brand and we're talking about more AI agent platform.

**Kyle Gaudreau:** So that's at least good.

**Kyle Gaudreau:** But I would try to think about those sorts of like bets of like the best list, the best alternatives, the comparison, like all that stuff is seeming to do well with AI visibility can get us some early wins.

**Kyle Gaudreau:** But I would try to think about blending in some other things into that mix just to make sure we're setting them up for healthy growth in the long term.

**Kyle Gaudreau:** So But for guys, try

**Kyle Gaudreau:** Additionally, and realize we're running a little bit short on time here, but would keep a close eye also on this non-brand side of things as well, obviously for any account.

**Kyle Gaudreau:** What's promising here is like impressions are increasing.

**Kyle Gaudreau:** We want to see this, like think about this, when you are in the first three months of an account and publishing, you want to consistently see this impression number go up each and every week.

**Kyle Gaudreau:** If it goes down a little bit for a week, not necessarily a concern, but what we want to be seeing is like if this continues for like say another week or two, and it's on that downward trajectory, that's where maybe we get a little bit more concerned or is our content sticky enough.

**Kyle Gaudreau:** Digging into like where the next level of growth would come for this, the things I would also be thinking about is like, what do we have?

**Kyle Gaudreau:** Have in the queue that ultimately like actually going back here for a second, sorry.

**Kyle Gaudreau:** One helpful thing that I would say, I'm not sure if we're doing this all the time, but a helpful way to just kind of like take a step back and think about our impact for them is looking at their total non-brand traffic, not just what we're creating content for for them.

**Kyle Gaudreau:** The reason being is if they are coming to us and they want to radically increase their organic presence and drive more growth via that channel, it's one thing if you're always filtering for our traffic and looking at that and showing that chart.

**Kyle Gaudreau:** And that can be helpful to look at, of course, but keep that in perspective of like the larger, their larger program that we're working within.

**Kyle Gaudreau:** And so in this case, I would say, you know, they only have 50 clicks a week.

**Kyle Gaudreau:** It's another

**Kyle Gaudreau:** Not super high, but sometimes for some of our clients, you may see hundreds of clicks a week, thousands of clicks a week.

**Kyle Gaudreau:** If we've been working with them for four plus months and our content's only creating like 50 clicks a week, 100 clicks a week, that's not going to radically change their overall trend.

**Kyle Gaudreau:** So it's an important framing to think about what kind of bets we're making, what we're trying to build towards, what are their goals, what are the objectives we're trying to build towards in six, 12 months with that in mind.

**Kyle Gaudreau:** Because we want to actually be putting a dent into a notable growth story is a better way of framing it within their larger program yet to law.

**Talal Syed:** Yeah, one thing I just wanted to call out specifically with non-branded view is I don't know if I surfaced this or not, but if you don't have any filters applied, the numbers look great and the impressions and clicks look great too.

**Talal Syed:** But if you apply any sort of filter on the query, Google drops all the hidden queries, which account for like 60 to 70%.

**Talal Syed:** you.

**Talal Syed:** Of the total site.

**Talal Syed:** So the actual numbers here when you filter for the impact our content might be driving, they look like 5x worse than they actually are.

**Talal Syed:** So if you want to sort of navigate around that, you have to look at the page level data, not the query level data.

**Talal Syed:** Because if you filter that, like 70% of all impressions and clicks are just going to go away.

**Talal Syed:** And that just presents like a significantly worse view of our performance than actual reality.

**Kyle Gaudreau:** I think some brands, suffer from that more than others, but that can be true.

**Kyle Gaudreau:** I do think we should probably explore, like, do we want to, like, revisit, like, the logic of some of these views and, yeah, maybe making it more page centric.

**Kyle Gaudreau:** The challenge is, like, some of those brands will have some branded stuff that will come through, but maybe this is an overall enhancement to consider.

**Kyle Gaudreau:** And so anyways, with that in mind, like, this looks like we actually can drive some healthy growth from where we're driving something like 10.

**Kyle Gaudreau:** 10.

**Kyle Gaudreau:** Plus clicks or whatever to like around 50, but like I've kind of seen the pattern of times I've even fallen into this trap with some of our clients where like if you just look at our content, you look at the impact of that, it can tell a really strong story, but you need to keep that in context of the overall program.

**Kyle Gaudreau:** And where that gets important is like as you start to think about it from that view is like what do we have that's in the queue that's coming up, right?

**Kyle Gaudreau:** So, you know, in this case for like ideas for review, like you want to be thinking about again, like where do they, where do we need to get to in like six plus months?

**Kyle Gaudreau:** Like if they need to like 3x, 4x, whatever it is, like really, really aggressively increase their traffic, that needs to be informing the type of bets that we're putting in here.

**Kyle Gaudreau:** And I'm sure a lot of you are already thinking about that, but just like a good thing to like keep in mind the overall like size of their program, where they need to get to, and like are our bets actually going to get them to, even if we.

**Kyle Gaudreau:** Knock it out of the park and like rank super high for everything.

**Kyle Gaudreau:** Is it even going to get to that level of traffic?

**Kyle Gaudreau:** I know this is at times like hard for upkeep, but like I would encourage you all like I've seen this on a bunch of our OS's.

**Kyle Gaudreau:** This isn't to point out a single like almost every OS has some level of this.

**Kyle Gaudreau:** It really helps you by having not only just the client, but you to like have this keyword volume and this keyword difficulty volume attached to your assignments.

**Kyle Gaudreau:** Because it can be helpful to start to go through and like look at your bets and start to see like what again from that framing, like where should we be spending our time?

**Kyle Gaudreau:** What should we be thinking about next?

**Kyle Gaudreau:** Also things to keep in mind, like play around with these defaults.

**Kyle Gaudreau:** Like it should not be average.

**Kyle Gaudreau:** It should not be sum.

**Kyle Gaudreau:** It should be average.

**Kyle Gaudreau:** So, okay.

**Kyle Gaudreau:** So now I can see like based off of this, at least from what's here, like in the limited knowledge I have, like context center operations feels like the most fruitful.

**Kyle Gaudreau:** Well, it's relatively low.

**Kyle Gaudreau:** So difficulty, high traffic, etc.

**Kyle Gaudreau:** So I'm sure you all are doing aspects of that, but like taking a step back, making sure we're understanding what we're building towards and like it aligns with our bets quite well.

**Kyle Gaudreau:** The other thing to think about is like, who are you comparing against?

**Kyle Gaudreau:** And I don't know how valid this is here for Acresta.

**Kyle Gaudreau:** Again, I'm not super familiar with the account.

**Kyle Gaudreau:** But, you know, I noticed through like the sprint, like if I look at some of like the sourcing of these keywords, a lot of like dial pad in here, one decagong.

**Kyle Gaudreau:** But like, I noticed that maybe, and I don't know if this is true, is a little bit of a disconnect of who they see as their top competitors and what maybe we're sourcing from like our plans and inspiration.

**Kyle Gaudreau:** I would need to dig in more to validate, but certainly like if I dig into some of these brands, I add in dial pad into this mix, like dial pad is like...

**Kyle Gaudreau:** Clearly, the behemoth here of all these other websites, 1.7 million in terms of organic traffic, they have a way higher authority score.

**Kyle Gaudreau:** That doesn't mean sourcing from them is necessarily wrong and there isn't things that we can't learn, I'm sure.

**Kyle Gaudreau:** But knowing that, at least looking at some of their data like Sierra and Decagon seem a bit closer to where their focus is, and that if we just look at like their overall authority scores being in the same ballpark, yet like look at Decagon like 5x their traffic, you know, some of that is driven by brand.

**Kyle Gaudreau:** As you can see, they're like pretty brand heavy, but like, if we compare like, you know, where Cresta is non-brand, they're at, you know, estimated to be around 1300 to around like 12k, so maybe even 12x higher in momentum.

**Kyle Gaudreau:** So like, I would just continually like, don't just...

**Kyle Gaudreau:** always assume that your OS has all your opportunities in it as you're thinking about how to grow these brands next.

**Kyle Gaudreau:** Don't assume it was all nailed within Sprint.

**Kyle Gaudreau:** Continue to go back and refresh this and look at the different trends that you're seeing.

**Kyle Gaudreau:** For example, Decagon, they're seeing some upward momentum here, a little bit ups and downs, but Sierra is seeing some momentum here as well.

**Kyle Gaudreau:** Going through and doing a fresh look at the keyword gap analysis that I'm sure you all are, we could always dig into this more, but to my understanding, it seems most of the team is already pretty well attuned to how to do this and what to look for and things of that nature.

**Kyle Gaudreau:** But are we missing any notable easy win opportunities that competitors that are more in their wheelhouse currently and their relative maturity of a SEO program that we can be tackling?

**Kyle Gaudreau:** So, quickly, I already ran through time.

**Kyle Gaudreau:** You know, I did want to spend most of the time on your code anyways, just because my hunch is, again, that I feel like that's probably the area we feel a little less comfortable in our workflows and our approach.

**Kyle Gaudreau:** So hopefully this was helpful.

**Kyle Gaudreau:** I saw some head nods and some comments.

**Kyle Gaudreau:** You know, Andi, you had a...

**Andi Bailey:** We have an action item for the team, right?

**Kyle Gaudreau:** Yeah, I was just building towards that.

**Kyle Gaudreau:** Appreciate the tee up, though.

**Kyle Gaudreau:** And so the next step here is on Friday, like, pick one of your accounts and, like, spend a little bit of time ahead of time. But, like, walk us through this live. Like, walk us through your thinking. We'll all ask questions. This is meant to just, like, this is going to help to, like, continue to just, like, strengthen that muscle for you all. And then as we, you know, continue to build on this, look at different use cases, we can take a similar approach for some future sessions. But the ask will be for this coming Friday, come prepared with one account.

**Kyle Gaudreau:** We'll spend, you know, I'll have to do some quick math here of like how many people we'll have on there, but call it like probably no more than 15 minutes per account ballpark and walk through kind of what have you uncovered and how does that inform where you think we should be spending our time next?

**Kyle Gaudreau:** What kind of bets we should be making?

**Kyle Gaudreau:** Totally okay if you don't have a, like, you don't have to have this end-to-end plan that you come with, but like come with some of that thinking where you feel stuck, where you need clarification, where your mind's going directionally, and just walk us through that thinking, and that's where we can continue to just build off this live and give feedback.

**Kyle Gaudreau:** Do you all feel like this is going to be helpful for you?

**Kyle Gaudreau:** Quick pulse check.

**Kyle Gaudreau:** Ok.

**Kyle Gaudreau:** Thank you.

**Kyle Gaudreau:** Okay.

**Kyle Gaudreau:** Thank you for covering your code, though, because that one's been like a, you know, you know, the challenge that one has been.

**Kyle Gaudreau:** Totally.

**Kyle Gaudreau:** 100%.

**Kyle Gaudreau:** Cool.

**Kyle Gaudreau:** Well, appreciate y'all sticking through this, the feedback.

**Kyle Gaudreau:** Give me any feedback you have after this as well.

**Kyle Gaudreau:** If there's certain areas you even want to dig in deeper that we maybe didn't get to today, happy to do some other sessions around that.

**Kyle Gaudreau:** All right, y'all.

**Kyle Gaudreau:** Enjoy the rest of the day.

**Kyle Gaudreau:** Talk to you on Friday.
