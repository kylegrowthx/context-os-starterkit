# Office hours part 2: Account Growth Review Training

<metadata>
date: 2026-02-13
time: 16:59 UTC
duration: 65 minutes
organizer: Kyle Gaudreau (kyle@growthxlabs.com)
participants:
  - Andi Bailey (andi@growthx.ai)
  - Carly Piekos (carly@growthx.ai)
  - Carrie Chowske (carrie@growthx.ai)
  - Erik O'Brien (erik@growthx.ai)
  - Kyle Gaudreau (kyle@growthxlabs.com)
  - Liz Kushnereit (liz@growthx.ai)
  - Talal Syed (talal@growthx.ai)
fathom_recording_id: 122346859
fathom_url: https://fathom.video/calls/565982906
share_url: https://fathom.video/share/iTASRs_mQduFW2o9ithvqA9DzCBeHoeE
source: fathom
enriched_on: 2026-02-27T00:00:00Z
</metadata>

---

## Summary

Kyle led a strategic training session reviewing four client account reviews (Engine, AIMBit, Airbyte, and Augment) to demonstrate frameworks for converting traffic into signups and proving ROI to skeptical stakeholders. The team covered attribution methodology, competitive framing strategies, and hands-on analysis of low-conversion challenges across content-heavy B2B sites, with Augment serving as a success case study that drove weekly traffic from 7k to 36k and paid signups from 14 to 69.

---

## Context

This session is part of GrowthX's internal training for its account management and strategy teams to standardize how they approach one of their core challenges: clients with strong organic traffic metrics that aren't converting to leads or signups. The training reflects a shift in GrowthX's thinking from traffic growth (which has plateaued or proved harder to scale) to conversion optimization and better attribution modeling. Talal Syed introduced GA4 journey explorations, Kyle explained multi-touch attribution concepts, and Carrie Chowske demonstrated CTA/conversion problems using real client data. The underlying challenge—getting non-POC stakeholders (often CEOs or CFOs) to see value in organic content when conversion rates appear low—runs through multiple client examples.

---

## Relevance

- **Account growth strategy**: Conversion and attribution frameworks central to client retention and expansion
- **Team enablement**: Training junior team members (Carly, Erik, Carrie) on client relationship management and analytical approaches
- **Product planning**: Liz mentioned a custom GPT tool consuming meeting transcripts and Fathom data—potential signals for knowledge management improvements
- **Sales/retention**: Talal's competitive framing and stakeholder management techniques are directly applicable to client renewals and scope expansion

---

## Overview

- **Conversion is the new focus.** With traffic growth plateauing, the priority is now converting existing visitors. This requires adding CTAs and internal links to high-traffic blog posts.
- **Attribution is key to proving ROI.** Standard last-touch attribution undercredits content's influence. GA4 path explorations are needed to show how organic content contributes to the full conversion journey.
- **Frame value against competitors.** To secure executive buy-in, show how the client's organic traffic value compares to competitors' paid spend, or highlight their lead in capturing a specific keyword category.
- **Augment provides a playbook for success.** Its strategy of targeted refreshes, a site redesign, and a product-led content pivot drove weekly traffic from 7k to 36k and paid signups from 14 to 69.

---

## Key Topics

### The Challenge: High Traffic, Low Conversions

  - **Engine:** High engagement (\~76%) but low conversion (0.02% blog, 0.79% site-wide).
      - **Hypothesis:** Add CTAs and internal links to high-traffic posts to direct users to product pages.
      - **Proposed Test:** A/B test CTAs on a few related pages before a mass refresh.
  - **AIMBit:** Session growth is not translating to conversions.
      - **Problem:** Content is not built for conversion (e.g., "wall of text" pages with no CTAs).
      - **Data Discrepancy:** A Looker dashboard showed low engagement (\<40%) for clusters, while a top-pages view showed higher rates.
          - **Cause:** The dashboard used a blended rate over a long period, obscuring recent positive trends.
          - **Solution:** Change the Looker dimension to `ISO year week` to see weekly trends.
  - **Airbyte:** Consistent low engagement across all clusters, despite strong traffic.
      - **Problem:** Content format (e.g., "wall of text") may be the primary issue.
      - **Next Step:** Use an experimentation mindset.
          - **Prioritize:** Use GSC data (queries, rankings) to find low-hanging fruit (high-volume, low-difficulty keywords).
          - **Enrich:** Focus on improving a few high-potential pages rather than a mass refresh.
          - **Research:** Conduct sessions with Airbyte solution engineers to understand the target audience (AI/software engineers).

### The Solution: Proving Value & Driving Conversions

  - **Attribution:**
      - **Problem:** Standard last-touch attribution undercredits organic content's influence.
      - **Solution:** Use GA4 path explorations to show how organic content is a touchpoint in the full conversion journey.
  - **Executive Buy-in:**
      - **Problem:** Securing buy-in from stakeholders who don't see the day-to-day value.
      - **Solutions:**
          - **Frame Value Against Competitors:** Show how the client's organic traffic value compares to competitors' paid spend.
          - **Highlight Keyword Capture:** Demonstrate progress by showing the client's share of total search volume in a key category.
          - **Improve Communication:** Ensure updates are clear for non-POCs, explicitly stating any client-side blockers.
  - **Augment: A Playbook for Success:**
      - **Strategy:** Targeted refreshes, a site redesign with CTA components, and a product-led content pivot.
      - **Results:**
          - Weekly traffic: 7k → 36k
          - Weekly paid signups: 14 → 69
          - Keyword ownership: \~30 \#1 keywords for "code review tools"
      - **Insight:** Liz's custom GPT, fed with Fathom data and meeting transcripts, identified a gap: the strategy excels at Bofu conversions but underperforms on the client's long-term vision of being the informational hub for mid-to-senior devs.

---

## Action Items

**Talal Syed**
- Engine: share GA4 journey exploration template w/ Carly

**Carly Piekos**
- VisCom: update Slack/Notion updates w/ top-line blockers; add competitor/keyword-capture framing

**Carrie Chowske**
- AIMBit: send Kyle analysis details; then run weekly engagement trend + query-level analysis

**Erik O'Brien**
- Airbyte: run GSC query-level analysis; prioritize pages; enrich 3–5 high-SV/low-comp pages

**Kyle Gaudreau**
- Evaluate Firecrawl access for team; then onboard Erik

**Liz Kushnereit**
- Augment: share Fathom-to-JSON Python script w/ Kyle

**Andi Bailey**
- Schedule next week's office hours w/ Bailey & Katya; include Matt if available

---

## Transcript

_[Pre-meeting small talk removed: Carly and Carrie discussed weekend plans (Nine Inch Nails concert, murder mystery dinner), Kyle mentioned car maintenance issues, Talal joined briefly. Meeting began at 6:00 min mark.]_

**Kyle Gaudreau:** So as a reminder, today's a follow-up from the previous session—just trying to do a live walkthrough and apply some of what we went through. Hopefully this is helpful. This isn't meant to put you on the spot. We're trying to help you identify opportunities and apply the same thinking to your other accounts. This isn't a test, and we won't grade you. Just trying to be helpful. We'll spend about 15 minutes per person. Pick an account, walk us through what you're thinking, what you're seeing, where you feel stuck, and where we could help you dig deeper. What I walk through for your account won't follow the same pattern as others—it's more illustrative of how to apply the thinking. That should take you in different directions depending on your accounts. We'll probably try a similar version of this in the future. Who wants to go first, or should I pick?

**Carly Piekos:** Yeah, I'll do it. So please feel free to interrupt me if I'm not being on task. I watched the video from last time since I had conflicts during the session. I chose Engine because I wanted to help Joel come up with realistic measurable goals for 2026 Q1 and Q2. Since we won't have a QBR anytime soon, I figured if we make these goals now, they'll come to fruition mid-year, and we'll have actual conversions to measure by the time of our QBR in about four months.

**Carly Piekos:** So what I found here is that I have organic and referral traffic isolated. They didn't have direct traffic as we discussed, so I wasn't sure how to incorporate it. But looking at the data, they're sitting at about 76% engagement rate, averaging 60% overall—pretty good. The issue is that blog traffic doesn't directly contribute to conversions. We need to add stickier CTAs to point back to product pages.

**Carly Piekos:** My goal is to take top-performing pages with high engagement and add good CTAs at the bottom pointing to product pages. If we use those high-engagement pages as top-of-funnel and push traffic to lower-engaged pages via internal links, it sends a stronger signal to Google. I wanted to do an A/B test rather than revamp everything—take a few highly related pages, refresh some internal links on high-traffic pages, and add CTAs to conversion pages and forms. The problem is clear: users are highly engaged but have nowhere to go. When they get pushed to product pages, they do go. We're seeing 0.02% conversion on blog pages versus 0.79% site-wide. I think all my accounts need a way to track how blogs contribute to conversions because CEOs and marketing teams might get it, but budget holders won't see value unless we show conversion wins.

**Kyle Gaudreau:** One thing to be careful with is semantic relevance. User experience comes first, optimization second. But if you're thinking about that already, this is an interesting hypothesis to test.

**Kyle Gaudreau:** Generally speaking, we can only write off the back of awesome traffic growth for so long. Traffic growth is encouraging and a strong signal, but we have to figure out how to help them realize the benefits. We also need to tell the full story of our impact. My hunch is there are things tracking-wise that those percentages might be undercrediting us. We're waiting on more information from Joel to figure it out.

**Talal Syed:** I want to touch on two things. It's good we're measuring conversions, but if they only have last-touch attribution, the impact of the blog gets severely understated. The requirement is that they have proper event tracking in GA4. If they do, you can create an exploration—I've already done one for another client—that measures whether organic was part of the journey for any conversion. It answers the question: was this a touchpoint in the conversion path, regardless of how many steps there were?

**Kyle Gaudreau:** Right. Just to clarify on attribution: out-of-the-box, Google associates conversions to the landing page that created the session. But as Talal mentioned, if someone reads a blog, comes back later, searches your product, and converts from the homepage, you don't get credit. Our goal is to show the full journey—that organic content was an influential touchpoint even if it wasn't the final click.

**Kyle Gaudreau:** Right.

**Kyle Gaudreau:** And so obviously this comes in all shapes and fashions, but yeah, it's a good call of like, you know, starting to probably build those as a base just for the team to be able to look at.

**Kyle Gaudreau:** Some accounts will be harder to do than others if they don't have the right instrumentation, but we should at least explore it.

**Carly Piekos:** Yeah.

**Carly Piekos:** One of the, one of my new BlackSol, I think it is, has PostHog and I'm not familiar with it, but that's how they're tracking everything.

**Carly Piekos:** Probably a similar concept.

**Kyle Gaudreau:** mean, you know, some of these systems for sure can be different.

**Kyle Gaudreau:** You know, Amplitude has, for example, some of its own nuances, but it's fairly common that like out of the box, that's going to be the rough logic that's typically going to be applied.

**Kyle Gaudreau:** So, so yeah, when you look at, you know, engine here, for example, when we're filtered down, it would tell you specifically in that session after reading the blog, did they convert?

**Carly Piekos:** Yeah, that would be ideal.

**Carly Piekos:** Okay.

**Carly Piekos:** At least, even if we weren't catching every single attribution, it would really be good to just at least have some sort of correlation between the blogs.

**Kyle Gaudreau:** That's not 0.02%.

**Kyle Gaudreau:** Luckily, Joel seems to understand this pretty well and is really reasonable about it.

**Kyle Gaudreau:** so, you know, he is thinking through some of this as where he's trying to action that conversion request we've made to them recently.

**Kyle Gaudreau:** So hopefully we can get that more comprehensive view of our impact.

**Carrie Chowske:** I also gave him once, I looked at, I kind of like compared, looked at traffic, like visitors that were on a blog page and then viewed any of the product pages afterwards.

**Carrie Chowske:** Because like we couldn't, we had the same problem when I was working on it too.

**Carrie Chowske:** They're using Amplitude for tracking but don't have granular page-level data. We can track topic clusters now, but that's about it.

**Kyle Gaudreau:** We've given them a few requests they're going to action, but they're spread thin. Luckily they just hired someone.

**Carly Piekos:** I have a VisCom situation that just came up. The CEO didn't like our invoice and wants to cancel because the main POC is on maternity leave. The CEO has no buy-in. For situations like that—early stage, stakeholders don't understand value—how do we set up tracking to prove our worth?

**Kyle Gaudreau:** Good question. Make sure you have alignment on the outcomes you're building toward. If they're caught up in short-term wins, they might not see the long-term vision. Also, here's a principle: assume someone important isn't in the day-to-day. Make sure your updates—whether in Slack or agendas—can be understood by people who don't join every call. They should get key points and understand how our analysis connects to where we're going, even if they don't have context from daily interactions.

**Andi Bailey:** Exactly. Put blockers at the top of updates. Everyone internally knows them, but someone not paying attention might miss them. It's a bit of CYA, but sometimes that's necessary.

**Talal Syed:** I'd add: for skeptical executives, competitive framing really helps. Show them how their competitors are investing in organic and the dollar value they're getting. Show how that advantage compounds over time. If you have keyword capture data, say: "In this category there are 500 keywords with 500k monthly search volume. We're capturing 100k of that." That's top-of-funnel but shows ground being gained. Unless you frame it against competitors, they'll think your numbers are bad. Instead, frame it as: we're going to drive X traffic in 12 months, which would cost Y paid ads. Here's how competitors are doing. Here's the total volume capture available. That framing usually works.

**Kyle Gaudreau:** Who wants to go next?

**Kyle Gaudreau:** Who wants to go next?

**Kyle Gaudreau:** Carrie, I see you're the one person off mute, so I'm going to pick you.

**Carrie Chowske:** Man, listen, you did mine already.

**Carrie Chowske:** I'm working on AIMBit's deck. What I'm seeing: sessions are trending up, but engagement isn't moving. There's a widening gap. Similar to Engine. They have many clusters but only a few performing. I dug into individual pages and found the same problem: no CTAs, walls of text. Pages aren't built for conversion. They've talked about conversions in our notes, but we're not doing anything to further that. They claim sessions are the only thing they care about, but also mention conversions.

**Kyle Gaudreau:** That's a classic AIMBit tension. Of course we want conversions, but without traffic, optimizing for conversion doesn't move the needle. We can do foundational work now—good UX, conversion-friendly structure. But if you're bleeding at the top of funnel, you can't magically create bottom-funnel conversions. Check if those engagement rates are trending up or down. I think we also need dashboard tweaks to make analysis easier.

**Carrie Chowske:** Vivek changed all the Lookers to monthly. I can't figure out how to switch back to weekly to see the trend.

**Kyle Gaudreau:** Easy fix. Go to date dimension, click the pencil, select ISO year week. Katya also set up a dropdown to change timeframes. I noticed there's a data disconnect—your Notion showed sub-40% clusters, but top traffic pages here are above 40%. It's probably a recency thing. When you blend engagement over long periods, you lose trend visibility. Check your timeframes and look at the actual queries driving engagement. You'll often see obvious patterns—like not capturing keywords you should be.

**Talal Syed:** Cluster analysis depends heavily on the mix of content. If a cluster has lots of bottom-of-funnel content, aggregate engagement will always be lopsided. You need to break down top, middle, and bottom-of-funnel keywords and factor that in.

**Carrie Chowske:** I'll send you what I pulled, Kyle. I was distracted trying to figure out what timeframe I'd used.

**Kyle Gaudreau:** We have Liz and Eric left.

**Kyle Gaudreau:** Any of you, either of you rather, want to go first?

**Erik O'Brien:** I'm happy to be a test subject here.

**Kyle Gaudreau:** Cool.

**Erik O'Brien:** So when you talk about looking at queries, I think that's a big gap that I have of like, where do we go to look at it and how do we do that?

**Erik O'Brien:** I have Deepgram and Airbyte. Airbyte is new post-November strategy sprint. Engagement rates are not where we want them. Low engagement across all topics and clusters. Traffic is evenly split but consistently low engagement. I'm stuck on what to optimize—blog format? Stronger hooks? We added TLDRs to keep people scrolling but hit a wall. Where do we go next?

**Kyle Gaudreau:** Low engagement across clusters suggests broader experience issues. Start by picking a top-traffic page, pull its queries from GSC, and look for misalignment with your content intent. Use Google Search Analytics add-on to prioritize pages by search volume and ranking difficulty. Pick high-volume, low-competition pages and enrich those—don't mass-update 40 articles. Have conversations with Mario about what developers actually want. Use an experimentation mindset on specific hypotheses to improve engagement.

**Talal Syed:** By the way, Firecrawl is great for scraping. Claude's webfetch can be tricky, but Firecrawl gives everything in Markdown. It's cheap—$19 for thousands of scrapes.

**Kyle Gaudreau:** We should get team access to Firecrawl.

---

### Liz Kushnereit - Augment

**Liz Kushnereit:** Augment redid their website with CTA components and embedded tables for top pieces. Targeting the "code review tools" category. They now own that space with ~30 #1 keywords. Weekly traffic went from 7k to 36k. Paid signups spiked this week—69 signups (they removed free trial so these are valuable). Prior weeks were 14-39. Their contact Syl says he gets value week over week. The strategy worked: targeted refreshes (120 of 300 articles), site redesign with CTAs, and product-led pivot (coding assistant, code review, intent app). CTR is finally going up. Talal's helping with bigger-picture strategy on MCP relaunch.

**Liz Kushnereit:** But yeah, but yeah, and then, but this is all just like a tiny snapshot.

**Liz Kushnereit:** I'm still working on that strategy with Talal to see like what other work streams we build out.

**Liz Kushnereit:** Oh, and then the other really important thing I'll mention, which I've talked about, I know we're like two minutes, is the GPT on Augment.

**Liz Kushnereit:** So I know that, yeah, Panzer made that tool for, or however he did it, like some kind of like quasi MCP for, I think that a lot more comes out of the transcripts, because you get like actual like stakeholders voice.

**Liz Kushnereit:** And so I was showing Talal like grade me on, or grade growthx on our progress towards Augment's North Star.

**Liz Kushnereit:** And then that helped a lot because it kind of showed like, are we actually, have we been listening to Sil?

**Liz Kushnereit:** Like, do we do what he says?

**Liz Kushnereit:** And then it just kind of goes through like where we are performing strongly and where we're not.

**Liz Kushnereit:** And what's really important about, yeah, so like.

**Liz Kushnereit:** If you get an A-, we want to dig into that.

**Liz Kushnereit:** And so we've done really good with Bofu.

**Liz Kushnereit:** He likes that he sees traffic growing.

**Liz Kushnereit:** He likes he sees conversion growing.

**Liz Kushnereit:** But his true vision was that Augment is the informational place that mid-to-senior-level devs go to to learn about AI coding.

**Liz Kushnereit:** And so I'm like, are we doing work streams that work towards that vision as well beyond just this one really strong work stream?

**Liz Kushnereit:** No.

**Liz Kushnereit:** And so like, how do we now pivot a little bit to better meet him?

**Liz Kushnereit:** But that's like what all of that digging in.

**Liz Kushnereit:** So yeah, the compounding is where we're not doing a great job and everything like that.

**Liz Kushnereit:** But yeah, so that's about it.

**Kyle Gaudreau:** B-plus is, you know, obviously some room to improve, but you clearly were one of those students who gets mad if they didn't get an A, which is all good.

**Liz Kushnereit:** You know, hold the highest standing.

**Liz Kushnereit:** Oh, sorry.

**Kyle Gaudreau:** I love it.

**Kyle Gaudreau:** Are you plugging into Fireflies MCP with that?

**Liz Kushnereit:** I just, I had like a little script, which I'm happy to share, but it's just, it just pulls, it's a one.

**Liz Kushnereit:** just, I

**Liz Kushnereit:** weekly, like, pull in a JSON of everything in Fathom, because Fathom goes way further back in time, you know, which I'm happy to share.

**Kyle Gaudreau:** shared it a little bit the other I did not see that if you had shared that at one point.

**Liz Kushnereit:** in DMs.

**Kyle Gaudreau:** mean, because it's, yeah, sorry, it's a little embarrassing.

**Liz Kushnereit:** It's just like a little Python script, you know, but just, yeah, it helps.

**Liz Kushnereit:** I think, like, long term, we should, sorry, go ahead, Talal.

**Talal Syed:** No, you're good.

**Liz Kushnereit:** Oh, just, like, long term, I think, like, it's not true, you know, like, we need MCPs, think, and this has been talked about across all clients to pull in all of that context indefinitely, like, Notion, Slack, but I think the transcripts are where you really learn the stakeholders' vision, where the risks are, you know, like, who cares about what, it all, and my experience comes out there.

**Kyle Gaudreau:** Yeah, agreed.

**Kyle Gaudreau:** I love the thing that Panzer built of, that we were talking about earlier, the gap I do see in it, it doesn't have, it didn't have anything around transcripts, and there's just, like, yeah, there's so much richness that comes through that.

**Andi Bailey:** We had this conversation yesterday, so we're working on figuring out the right way to do it.

**Andi Bailey:** The danger, Liz, you have your own GPT, so it's very useful, but we can't put it in our podclods because it doesn't know how to distinguish between private and public documents and conversations yet.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** So we'll figure it out.

**Kyle Gaudreau:** I'll move the mind if we need to create a personal account for each person, I think the efficiency in itself will pay off tenfold for the engagement managers.

**Kyle Gaudreau:** But yeah, there's a few guardrails we need to think through.

**Talal Syed:** Yeah, I think we also kind of need a version of this for the shared strategy team because I feel like since we have so many accounts, I feel like whenever we get a ticket, I have to first...

**Talal Syed:** Yeah.

**Talal Syed:** Figure out what are we doing for the account, what's the health, what do they actually do, and then dig into the documentation.

**Talal Syed:** So if there's a way for us to connect to all the documentation that exists, including the transcripts, I can, instead of taking 30 minutes away from the EM or the ME or whoever, I can just quickly get a snapshot of what they're doing and then have a more educated call.

**Talal Syed:** So I think it could save us a lot of time.

**Kyle Gaudreau:** Yeah, agreed, agreed.

**Kyle Gaudreau:** Cool.

**Kyle Gaudreau:** Well, appreciate you all going through the exercise.

**Kyle Gaudreau:** Hopefully this was helpful.

**Kyle Gaudreau:** Certainly, you know, no, this is just probably scratching the surface on a few different things.

**Kyle Gaudreau:** So if there's anything you want to dig in deeper, we can certainly do that in future office hour sessions or one-on-ones, wherever it may be.

**Kyle Gaudreau:** So please don't be shy on reaching out because we're here to help.

**Andi Bailey:** Yeah, and I think we should, we'll have Bailey and Katya do theirs next week too.

**Kyle Gaudreau:** yeah.

**Kyle Gaudreau:** And Matt mentioned he.

**Kyle Gaudreau:** couldn't make it today because of the time zone.

**Kyle Gaudreau:** So, you know, if he's around on Tuesday, we can do that then as well.

**Kyle Gaudreau:** But I also offered to do it 101 if he needs to do another time.

**Carrie Chowske:** All joking aside, Kyle, can I send you what I actually did?

**Kyle Gaudreau:** Oh, yeah, 100%.

**Kyle Gaudreau:** This should be just a jumping off point on the ways we can continue to help you all think through your account.

**Carrie Chowske:** I more so made the mistake when I was showing the screen here.

**Carrie Chowske:** But if anyone didn't see my comment, I looked at organic versus, but I was looking at all content because we're trying to, I was at the stage where we need to be converting.

**Carrie Chowske:** So there you go.

**Carrie Chowske:** Lesson learned.

**Kyle Gaudreau:** Well, happy Friday, y'all.

**Kyle Gaudreau:** Hope you have a great weekend.

**Kyle Gaudreau:** None of us are going to have nearly as interesting a weekend as Carly, but looking forward to seeing all the amazing pictures that you should share with us after.

**Kyle Gaudreau:** Bye, everyone.

**Kyle Gaudreau:** All right, see ya.

**Kyle Gaudreau:** Bye, everyone.
