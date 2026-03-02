# Office hours part 2: Account Growth Review Training

<metadata>
date: 2026-02-13
time: 16:59 UTC
duration: 65 minutes
organizer: Kyle Gaudreau
participants: Aida Knezevic, Matthew Alves-Hill, Carrie Chowske, Megan Dickey, Andi Bailey, Jo Kaminska, Erik O'Brien, Bailey Seybolt, Katya Luscomb, Liz Kushnereit, Talal Syed, Ella Dillon, William Leborgne, Kathy Lam, Carly Piekos, Kyle Gaudreau
fathom_recording_id: 122346859
fathom_url: https://fathom.video/calls/565982906
share_url: https://fathom.video/share/iTASRs_mQduFW2o9ithvqA9DzCBeHoeE
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Kyle Gaudreau led a live training session walking through account growth review methodology with the GrowthX delivery team, applying the framework to four client accounts (Engine, AIMBit, Airbyte, and Augment). Key insight: traffic growth is plateauing across accounts, so the focus shifts to conversion optimization through better CTAs, content formatting, and attribution modeling. The team discussed how to frame organic content value to skeptical executives, use GA4 path explorations to credit content in multi-touch journeys, and apply audience research and page prioritization to drive both traffic and conversion growth.

---

## Context

This is an internal GrowthX office hours training session. Kyle Gaudreau, head of strategy, conducted a follow-up training exercise with the delivery team (including Carly, Carrie, Talal, and others) to practice live account reviews. Rather than lecturing, Kyle used this as a hands-on workshop where team members walked through their own client accounts, explained their thinking, and received feedback on how to apply GrowthX's account growth framework. This builds on a previous training session and prepares the team to conduct more strategic client work. The session focuses on translating high traffic volume into conversions and measurable business value — a shift that demands both analytical depth and better storytelling to stakeholders.

---

## Relevance

**To GrowthX Delivery:**
- Framework for converting high-traffic accounts into revenue — shift from "we drove traffic" to "we drove conversions." Pattern: CTAs, content format, internal linking, and audience research all matter more than raw traffic volume.
- GA4 path explorations and attribution modeling are now critical methodologies the team needs to execute. Talal emphasized multi-touch attribution; standard last-touch attribution severely undercredits organic content's influence.
- Content design lesson: "walls of text" with no CTAs destroy conversion potential. Augment's success (7k → 36k weekly traffic, 14 → 69 paid signups) required site redesign with embedded CTA components — format and calls-to-action matter as much as content.
- Executive communication: when POCs are absent, clarity on blockers and framing value against competitor spend/keyword capture are essential. Andi Bailey flagged that Notion/Slack updates need to spell out blockers explicitly for stakeholders not in daily calls.

**To GrowthX Business Development:**
- Augment case study provides a concrete playbook: targeted content refreshes (not mass rewrites), site redesign with conversion intent, product-led content pivot, and ~30 #1 keyword rankings for "code review tools" alongside 5x traffic growth. Liz Kushnereit's GPT analysis identified that strategy excels at bottom-of-funnel but may underdeliver on informational hub positioning.
- Account health signal: Engine facing CEO pushback on invoice + poor stakeholder buy-in with point-of-contact on maternity leave. Pattern recognition: early-stage accounts without strong engagement metrics and without clear conversion framework are renewal risk.
- Expansion insight: customers asking about conversions (like AIMBit, VisCom) represent opportunity to deepen GrowthX services beyond traffic into conversion strategy and analytics infrastructure.

**To CheckThat / AI Visibility:**
- Liz Kushnereit built a custom GPT fed with Fathom transcripts and meeting notes to analyze Augment's content strategy — this is live validation of CheckThat's core value (AI analyzing organic visibility patterns at scale).

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

**Talal Syed (GrowthX)**
- Engine: share GA4 journey exploration template w/ Carly

**Carly Piekos (GrowthX)**
- VisCom: update Slack/Notion updates w/ top-line blockers; add competitor/keyword-capture framing

**Carrie Chowske (GrowthX)**
- AIMBit: send Kyle analysis details; then run weekly engagement trend + query-level analysis

**Erik O'Brien (GrowthX)**
- Airbyte: run GSC query-level analysis; prioritize pages; enrich 3–5 high-SV/low-comp pages

**Kyle Gaudreau (GrowthX)**
- Evaluate Firecrawl access for team; then onboard Erik

**Liz Kushnereit (GrowthX)**
- Augment: share Fathom-to-JSON Python script w/ Kyle

**Andi Bailey (GrowthX)**
- Schedule next week's office hours w/ Bailey & Katya; include Matt if available

---

## Transcript
**Carly Piekos:** This meeting is being recorded.

**Carrie Chowske:** With my luck, somebody would have like popped in while I making that weird face at you.

**Carly Piekos:** Or while I was making funny noises.

**Carrie Chowske:** What was with these two weirdos?

**Carrie Chowske:** Listen, you can call me weird.

**Carrie Chowske:** I will call you weird.

**Carrie Chowske:** I forgot what I was looking for. I was looking for something that I saved during a meeting and now I can't find it.

**Carrie Chowske:** Oh, it's just Kyle.

**Carrie Chowske:** He doesn't care if you make weird noises.

**Carrie Chowske:** He knows how weird we both are.

**Carly Piekos:** Yeah.

**Carly Piekos:** Hey, I'm right up there with you.

**Carly Piekos:** Don't.

**Carrie Chowske:** We know.

**Kyle Gaudreau:** We know.

**Kyle Gaudreau:** Thank you.

**Carly Piekos:** I feel like you have to be a little weird to be in marketing, right?

**Carrie Chowske:** I was just going to say, I see that as a compliment.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Yeah.

**Carly Piekos:** Creative souls that need to get paid, right?

**Kyle Gaudreau:** I had a fun morning where my car is like, you don't have enough oil.

**Kyle Gaudreau:** I'm like, but I need to drop off my son.

**Carly Piekos:** And apparently new cars don't have dipsticks.

**Carrie Chowske:** Is this a new thing?

**Carly Piekos:** They don't?

**Kyle Gaudreau:** Mine doesn't.

**Kyle Gaudreau:** So I was like, I must be looking in the wrong place.

**Carly Piekos:** You have to be looking in the wrong place.

**Kyle Gaudreau:** It doesn't have it.

**Kyle Gaudreau:** It's like, it has like, it's like, read the sensor in the car.

**Kyle Gaudreau:** And I'm like, okay, but what if the sensor is broken?

**Carrie Chowske:** Right?

**Carly Piekos:** My husband's a mechanic, and I'm pretty sure there's dipsticks.

**Carrie Chowske:** Mine used to work in auto parts.

**Carly Piekos:** I decided to leave it out of the manual because they thought it was so obvious, but I've never struggled to find a dipstick in any car I've ever had to look for one ever.

**Carly Piekos:** What kind of car is it?

**Kyle Gaudreau:** It's an Audi.

**Kyle Gaudreau:** Oh, you're too fancy.

**Kyle Gaudreau:** It's new, so maybe that's why.

**Carly Piekos:** Yeah, it might be.

**Carly Piekos:** But.

**Carly Piekos:** I love outies.

**Carrie Chowske:** This is why my husband drives a 2007 Ford Ranger.

**Kyle Gaudreau:** Hey, you know what?

**Carrie Chowske:** He can work on it himself.

**Kyle Gaudreau:** He'll have to go back to it.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** But anyways, yeah, so then I turned it on after I dropped him off and then turned it on again and then it was gone.

**Carrie Chowske:** Were you parked on a hill?

**Carrie Chowske:** Maybe it's just slightly low.

**Kyle Gaudreau:** The way it's in my garage is maybe slightly tipped, but I don't know.

**Kyle Gaudreau:** It's weird.

**Kyle Gaudreau:** Hopefully it's nothing.

**Talal Syed:** Folks.

**Kyle Gaudreau:** Hey.

**Carly Piekos:** Hello.

**Kyle Gaudreau:** Well, we should be having something like eight people on this.

**Kyle Gaudreau:** I Okay.

**Kyle Gaudreau:** Okay.

**Kyle Gaudreau:** It's.

**Kyle Gaudreau:** We'll wait and give them a minute.

**Kyle Gaudreau:** Anyone have any fun plans for the weekend?

**Carly Piekos:** Yeah, I'm going to see Nine Inch Nails tomorrow.

**Kyle Gaudreau:** Nine Inch Nails?

**Carly Piekos:** Wow, throwback.

**Kyle Gaudreau:** didn't realize they were still playing.

**Carly Piekos:** Yeah, so Trent Reznor is doing a tour.

**Carly Piekos:** Did just call me Carly Old?

**Kyle Gaudreau:** First of all, I'm probably, I'm up there.

**Kyle Gaudreau:** I mean, I'm in my 40s.

**Carrie Chowske:** Come on now.

**Carly Piekos:** Yeah.

**Carly Piekos:** So, yeah, they're, like, baby Carly love Nine Inch Nails.

**Carly Piekos:** I, like, have little buns on top of my head, you know, like the N-I-N shirt.

**Carly Piekos:** I can't wait to buy merch when I'm there.

**Carly Piekos:** So that's what we're doing tomorrow.

**Carly Piekos:** What does a mosh pit look like at a Nine Inch Nails concert these days?

**Carly Piekos:** I don't know, but I'm in the pit.

**Carly Piekos:** I got pit tickets.

**Carrie Chowske:** Oh, my gosh.

**Carly Piekos:** I'm going to be throwing elbows.

**Carly Piekos:** My hips hurt.

**Carly Piekos:** So, yeah, I'm really, really excited.

**Carly Piekos:** One of our friends, actually, he's in, I don't know, the music industry, and he lives down the street from me, and he has traveled with Manchester Orchestra, and he, like, does all the sound and lights and things for that, and he, like, just travels to go see concerts.

**Carly Piekos:** He went to go see Radiohead, and he was like, you need to go see Nine Inch Nails in the pit, and I was like, okay, I'm definitely going to do that.

**Carly Piekos:** So I'm doing that, and then tonight I'm going to a murder mystery dinner that's overlooking New York City, so I'm pretty excited about it.

**Kyle Gaudreau:** Interesting.

**Carly Piekos:** Yeah, you get to get dressed up and do a whole thing, so it's, yeah, it's a pretty fun weekend planned.

**Kyle Gaudreau:** Wow.

**Kyle Gaudreau:** Very cool.

**Talal Syed:** You have a far more interesting life than I do.

**Carly Piekos:** Yeah, it's my husband.

**Carly Piekos:** He just wanted to wear a top hat, so.

**Kyle Gaudreau:** I don't know, Talal, this epic match between you and Nigel, we're going to get going on the tennis court this weekend.

**Talal Syed:** I don't know.

**Talal Syed:** Oh, absolutely.

**Kyle Gaudreau:** I already got it scheduled.

**Talal Syed:** It's going to be open slaughter, yeah.

**Carly Piekos:** I don't think I knew that you played tennis, Talal, but it makes so much sense.

**Carrie Chowske:** Like, that fits perfectly with how I think.

**Talal Syed:** I just started, like, a couple of years ago.

**Carrie Chowske:** Yeah, I love playing tennis.

**Carrie Chowske:** I'm awful at it, but I like it.

**Talal Syed:** Same, honestly.

**Talal Syed:** I love the game, but I wish I was better at it, so...

**Carly Piekos:** Yeah, I'm not a sports person, so good for you.

**Carrie Chowske:** A few years, like, about a year before I met my husband, or before my husband and I started dating, I was dating a guy whose sister had played, like, tennis competitively in college.

**Carrie Chowske:** And, like, I was, like, visiting his family over, like, Thanksgiving, and their idea of fun was going to the gym. They were like, let's go play tennis.

**Talal Syed:** And I'm like, oh, gosh.

**Carrie Chowske:** You know, and then the guy I was seeing had played golf in college, and they wanted to go golfing.

**Carrie Chowske:** And I'm like, oh, my God.

**Kyle Gaudreau:** They're going to think I'm like the biggest klutz ever.

**Kyle Gaudreau:** They probably still do.

**Carly Piekos:** Yeah.

**Carly Piekos:** Well, that's how I would be.

**Carly Piekos:** I would be on the golf cart the entire time, just in the shade.

**Carrie Chowske:** I got a good swing, but that's about it.

**Carrie Chowske:** I can drive the ball pretty far.

**Carrie Chowske:** Cannot get it where I want it to go.

**Carrie Chowske:** Yeah, it's a horrible short game, which is the whole point.

**Carly Piekos:** Yeah, I've never even tried it.

**Carly Piekos:** So you're still better than I.

**Kyle Gaudreau:** Well, we're at the six-minute mark, expecting a few more, but we should get started.

**Kyle Gaudreau:** So as a reminder, today's a follow-up from the previous session, just trying to do a bit of a live walkthrough, apply some of what we went through the last time.

**Kyle Gaudreau:** Hopefully this is helpful.

**Kyle Gaudreau:** This isn't meant to put you all on the spot or anything like that.

**Kyle Gaudreau:** It is more just trying to make sure we can.

**Kyle Gaudreau:** And, you know, as a team help you and identify different opportunities for your accounts and how you can apply the same type of thinking to your other accounts.

**Kyle Gaudreau:** And so none of this is to this isn't a test or anything.

**Kyle Gaudreau:** We're not going to grade you.

**Kyle Gaudreau:** This is merely just trying to be helpful as much as possible.

**Kyle Gaudreau:** The the thing we'll do is given the amount of people we have, we will spend like, you know, 15 minutes per person.

**Kyle Gaudreau:** Pick an account, walk us through kind of what you're thinking, what you're seeing, where you feel stuck, maybe where we could help you think through where to dig in deeper.

**Kyle Gaudreau:** You know, what I walk through for your code, for example, isn't going to follow the same exact pattern of each one of our accounts.

**Kyle Gaudreau:** That's more supposed to be like illustrative of how to apply the thinking.

**Kyle Gaudreau:** But that should take you different directions depending on what's happening with your accounts.

**Kyle Gaudreau:** So there's certainly some common patterns for sure.

**Kyle Gaudreau:** So I would imagine we'll have others that look similar to it.

**Kyle Gaudreau:** Your code.

**Kyle Gaudreau:** But that's the intention.

**Kyle Gaudreau:** We'll maybe try a similar version of this in the future.

**Kyle Gaudreau:** But anyways, who wants to go first?

**Kyle Gaudreau:** Or I could pick.

**Kyle Gaudreau:** So we want to volunteer.

**Carly Piekos:** Yeah, I guess I'll do it.

**Carly Piekos:** Okay, cool.

**Kyle Gaudreau:** And as we go through, like, you know, share screens, like walk us through what you're thinking.

**Kyle Gaudreau:** Like, this isn't meant to be, like, overly formal.

**Kyle Gaudreau:** It's more to, like, walk us through what you've seen, again, where you may be stuck, where we can help, etc.

**Carly Piekos:** Yeah, yeah, yeah.

**Carly Piekos:** So I got to watch the video.

**Carly Piekos:** So please feel free to, like, interrupt me if you feel like I'm not being on task.

**Carly Piekos:** I got to take a look at what we talked about because I had meetings during the last session.

**Carly Piekos:** So essentially, I chose Engine, as you're familiar with, Kyle, just because I wanted...

**Carly Piekos:** To help Joel come up with actually like realistic measurable goals for 2026, like quarter one and quarter two.

**Carly Piekos:** And since we're not going to have a QBR anytime soon, I feel like if we make these goals now, then it will actually come to fruition maybe like mid-year.

**Carly Piekos:** And then once we go to our QBR stage, which will be in like four months, then we'll have like actually like conversions to measure.

**Carly Piekos:** So what I found here, and I'll just, and this will take a second to load as Carrie knows, if I have to bounce between conversions and the overall.

**Carly Piekos:** But right now I just have organic traffic and referral traffic clicked.

**Carly Piekos:** They didn't have direct traffic as we discussed yesterday, Kyle.

**Carly Piekos:** So I wasn't really sure on how we were going to incorporate the direct.

**Kyle Gaudreau:** Oh, that will be actually.

**Carly Piekos:** There are a few low engagements on here, but around like 76% engagement rate for like maybe 60% on average, which I think is pretty good overall.

**Kyle Gaudreau:** For sure.

**Kyle Gaudreau:** Those are strong engagement rates.

**Carly Piekos:** Yeah.

**Carly Piekos:** So the issue is the blog traffic does not contribute directly to the conversions because what we need to do is add stickier like CTAs to kind of point back to those product pages.

**Carly Piekos:** So when I was doing like all of the research here, these main pages, and this is why I actually yesterday during yesterday's call suggested that we go back and refresh some pages.

**Carly Piekos:** So my goal is to take the top performing pages that have the highest engagement rate and add really good CTAs at either like the bottom of the page to point.

**Carly Piekos:** What it's showing is they're more likely to click to another page.

**Carly Piekos:** So if we refresh those lower performing, less engaged pages, and we're using the higher pages as, let's say, like a top of funnel type of deal, use those internal links and push that traffic to the lower engaged pages, it will bring a stronger signal to Google that more of our pages have engagement.

**Carly Piekos:** Yeah, it certainly could be that that would work.

**Kyle Gaudreau:** I think just the thing that I'd be careful with is just like, and you're probably thinking of this anyways, but just like the semantic relevance between them as well.

**Carly Piekos:** Yes, yes.

**Kyle Gaudreau:** Like at the end of the day, like, you know, the, the primary thing we should continue to come back to, as we think about this is like, user experience first, you know, optimization second, or whatever order, you know, down the line that is, but, but yeah, if

**Kyle Gaudreau:** If you're already thinking about that, then yeah, you know, think that's an interesting hypothesis to test out.

**Carly Piekos:** Yeah, I was kind of just like looking into, and I wanted to do an A-B test on this.

**Carly Piekos:** I didn't necessarily want to just revamp everything.

**Carly Piekos:** I wanted to take a few of the pages and the ones that are like highly related and refresh a few things, refresh maybe the internal links on some of the high traffic pages, and then add those like CTAs to the products, to the conversion pages, like the forms and such.

**Carly Piekos:** Because what we're seeing is like they're highly engaged, but they just don't have anywhere to go.

**Carly Piekos:** But when the users are like pushed to other product pages, they do end up going there.

**Carly Piekos:** We just have a 0.02% in conversion rate on the blog pages and a 0.79 on the overall site.

**Carly Piekos:** So it's just what we need to do is fix the kind of the funnel to.

**Carly Piekos:** Those product pages to those conversion pages from the blog.

**Carly Piekos:** At the end of the day, I feel like all of my accounts might need something like this, just like a way to track the actual blogs.

**Carly Piekos:** And I know that like, and how they're contributing to the conversions because they, CEOs and like the marketing team might get it, but I don't think the budget holders are going to see the value unless they're making some sort of wins with the conversions.

**Carly Piekos:** So that was my thinking behind it.

**Kyle Gaudreau:** I think just generally speaking, like, you know, we can only write off the backs of like awesome traffic growth for so long.

**Kyle Gaudreau:** Like it's really encouraging their traffic growth and that's a strong signal, but yeah, agree.

**Kyle Gaudreau:** Like we have to continue to like figure out how we help them realize the benefits of this.

**Kyle Gaudreau:** Also ensuring like.

**Kyle Gaudreau:** Are we telling the full story of our impact as well?

**Kyle Gaudreau:** Because my hunch is there's probably some things tracking-wise that those percentages are maybe undercrediting us here and there.

**Carly Piekos:** 100%.

**Kyle Gaudreau:** We're waiting on more information from Joel to kind of figure out.

**Kyle Gaudreau:** did you have something?

**Talal Syed:** Yeah, I want to touch on two things.

**Talal Syed:** So I think it's good that we're trying to measure conversions, but especially if they only have last-touch attribution.

**Talal Syed:** Then the impact of the blog and the work we do gets severely understated.

**Talal Syed:** So the requisite for this is that they have event tracking set up properly in GA4.

**Carly Piekos:** Yes.

**Talal Syed:** But if they do, then you can create an exploration, which I've already done for some client.

**Talal Syed:** don't remember which one, but I can share that.

**Talal Syed:** And that essentially measures was organic a part of the journey for any conversion that took place.

**Talal Syed:** So if it was a touchpoint within the journey and they had like four or five steps or any amount of...

**Carly Piekos:** Definitely, like, more information on how to get that.

**Kyle Gaudreau:** Just to add a point around what Talal's mentioning around that journey, just to ensure, like, everyone is understanding of, like, out-of-the-box attribution on, like, how Google would associate these events is, you know, if you were to filter down for the conversion action here, our content, essentially what that's going to be telling you is what is the landing page that created that session?

**Kyle Gaudreau:** And it is attributing it back to that event.

**Kyle Gaudreau:** And in Talal's case, what he's mentioning is, like, hey, yeah, you may see some stuff there, but, like, if someone went to the blog, they read it, they came back later on, maybe they, you know, just searched for engine and went to the homepage and then converted, we wouldn't be getting the credit there.

**Kyle Gaudreau:** But if in the very overly simplistic journey, if that person, like, read a blog, they loved it, they came back, went to the homepage, like, that homepage touched and really strongly influenced what was that initial touch.

**Kyle Gaudreau:** Thank you much.

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

**Carrie Chowske:** It's like, he's tracking stuff in, I don't remember what he's using.

**Carly Piekos:** Amplitude?

**Carrie Chowske:** Amplitude, yep.

**Carrie Chowske:** And just, but not enough to like see really clear.

**Carrie Chowske:** We don't have anything, any way to like track.

**Carrie Chowske:** Tract those exact pages.

**Carrie Chowske:** Although I thought they were, they added, at least we can track, like, the, like, different topic clusters now, but that's about it.

**Kyle Gaudreau:** Yeah, we gave him a few, like, requests recently that he's going to be actioning, but he's also very spread thin at the moment, but luckily he just hired someone, so.

**Carrie Chowske:** I heard.

**Carrie Chowske:** That's great.

**Kyle Gaudreau:** Cool.

**Kyle Gaudreau:** Anything else, Carly, that would be helpful to dig through or things that, you know, we could help provide feedback on?

**Carly Piekos:** Um, I, guess my question would be, how do we go about, like, I, so this just came up this week, but I have, I have a client that wasn't the point of contact and the CEO didn't like the invoice that we sent and now wants to cancel because the point of contact is on maternity leave.

**Carly Piekos:** And all of that.

**Carly Piekos:** So I guess for those situations where the CEO has no buy-in, stakeholders, they just don't understand the value of this.

**Carly Piekos:** And right now we're in the very early stages.

**Carly Piekos:** How do we get the tracking together to prove our worth?

**Carly Piekos:** I guess that's kind of what I would like to set up for VisCom specifically.

**Kyle Gaudreau:** Yeah, that's a good question.

**Kyle Gaudreau:** I mean, there's a lot to unpack there, and I'm not fully in the loop on everything with them.

**Kyle Gaudreau:** But one, just making sure we have a really good foundation of the outcomes we're trying to build towards.

**Kyle Gaudreau:** And starting there, if they're getting a little bit too caught up in short-term focus and what has been the impact, they may not be thinking about the right way of what we're actually building towards.

**Kyle Gaudreau:** And so if we can get them to be excited about what we're building towards, you can get alignment on like this is what we're building towards and we can talk a little bit more with specificity of like the how we get there.

**Kyle Gaudreau:** The other thing just to keep in mind is, you know, I can't say this is like hasn't happened here or anything, but just knowing this is just a helpful like principle to think about with anything that we share with clients is like, it's good to assume that like there's someone important that isn't going to be have their pulse on the day to day and that our updates are written in a way that kind of reflects that, right?

**Kyle Gaudreau:** Like if someone was to go through and didn't join your meetings and read the agendas, like hopefully they can still capture like the key points, the most important things where we're focused or, you know, our analyses and how that connects to like where we're going.

**Kyle Gaudreau:** If that's only coming through in the calls and the agendas are like too high level, I'm not saying this is the case of the VisCom situation where they go to read Slack or whatever.

**Andi Bailey:** What would they see?

**Andi Bailey:** So just, yeah, like to Kyle's point, put it at the top that we're still blocked, like, because they know and we know, but somebody that's not paying attention might not know.

**Andi Bailey:** And so it's a little bit of like CYA, but yeah, yeah, no, maybe that has to, like, sometimes that kind of has to be the way that we operate too.

**Carly Piekos:** Yeah, I feel like he, did he pull from like Notion, like the agendas from Notion?

**Andi Bailey:** Yeah, think so.

**Andi Bailey:** then like Marcel hopped into the Slack channel and I like, I think he's connected to Notion and Slack.

**Kyle Gaudreau:** Yeah, Notion and Slack, think were the primary sources he pulled in.

**Kyle Gaudreau:** I was, and I won't go rabbit hole on that.

**Kyle Gaudreau:** I think there's some opportunities of improving what he's built, but to the, to the larger point of just making sure if someone is in the loop, whether that is a bot or a human, yeah, just like being mindful of if, if someone didn't have the same context as the day-to-day POC and they read this, would they get some?

**Carly Piekos:** value from this update, whatever that update is.

**Carly Piekos:** Okay.

**Kyle Gaudreau:** I certainly don't think that solves all your problems, but, you know, happy to dig in more if I can be helpful on Visigal and Aftris.

**Talal Syed:** Sarge, did you have something there?

**Talal Syed:** Yeah, I just wanted to add one more thing that if we do find ourselves in these situations, one thing that I've found that really helps, especially with management types, is showing how they're doing compared to some of the other data competitors in their field.

**Talal Syed:** So, like, just show them the velocity that your competitors are investing X amount of money in organic, because this is the dollar value of the organic traffic they're getting.

**Talal Syed:** And this is how it's accelerating over time when they're building a compounding advantage.

**Talal Syed:** So that frames it in a way where they feel for more left out.

**Talal Syed:** So that helps.

**Talal Syed:** The other thing you can potentially do is that if you have good early numbers in terms of keyword capture, you can tell them that, hey, you want to compete in this XYZ category.

**Talal Syed:** And there are like...

**Talal Syed:** 500 keywords here, and there's a total search volume of 500k, whatever, we're effectively starting to capture maybe 100k of that.

**Talal Syed:** So that's very, very top of funnel.

**Talal Syed:** It's going to lead down to more conversions down the line, but it shows them gaining ground on competition in a competitive field, which sort of like flips a switch in their head.

**Talal Syed:** So unless you frame it against their competition, they're always going to think that, hey, these numbers don't look good.

**Talal Syed:** You're producing a ton of content or you're just like button pushers at this point in time.

**Talal Syed:** So you need to frame it in a way where like you're telling them that we're going to drive this amount of organic traffic in 12 months.

**Talal Syed:** If you went out and paid for the traffic, this is what you would spend.

**Talal Syed:** This is how the competitors are doing.

**Talal Syed:** This is what like the volume capture exists in this field.

**Talal Syed:** So like all of that framing usually helps.

**Carly Piekos:** Okay.

**Carly Piekos:** Awesome.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Great point.

**Kyle Gaudreau:** Cool.

**Kyle Gaudreau:** Who wants to go next?

**Kyle Gaudreau:** Cool.

**Kyle Gaudreau:** Cool.

**Kyle Gaudreau:** Cool.

**Kyle Gaudreau:** Cool.

**Kyle Gaudreau:** Carrie, see you're the one person off mute, so I'm going to pick you.

**Carrie Chowske:** Man, listen, you did mine already.

**Carrie Chowske:** It's okay.

**Carrie Chowske:** I was really just, I'm fine with that.

**Kyle Gaudreau:** call your only account?

**Carrie Chowske:** No, no, no.

**Carrie Chowske:** I'm just saying you did one of mine already.

**Carrie Chowske:** But I was just saying I was being quiet because I was like, if somebody else wants to go, that's fine.

**Carrie Chowske:** I'm not going to like push it.

**Carrie Chowske:** I did aim bit for this because we're in the middle of, I'm in the middle of drafting like the slide deck for the And I think like, here, I'll share my screen.

**Carrie Chowske:** I think what's interesting like with what we did, like, sorry, I'm on wrong tab too.

**Carrie Chowske:** If you like look at this, like it looks good, like if it's an upward trajectory, so like, okay, that looks nice.

**Carrie Chowske:** But what does not look nice is that as we're getting more sessions, that this isn't moving.

**Carrie Chowske:** This little blue guy didn't move.

**Carrie Chowske:** So I'm kind of, this one has a very similar kind of story.

**Carrie Chowske:** I think to what you did with your co Kyle is like, that, I mean, the engagement rate looks good if you're just looking at that number, but like, it's like gap between them is widening, like we should, you know, I don't know, I just didn't, I wasn't really a big fan of that.

**Carrie Chowske:** So like, I looked at, like, I kind of like went in and like dug in on individual pages, because like, the ones where they've got like lower engagement rate, like, what's going on there?

**Carrie Chowske:** Like, is there stuff that we could, we could do?

**Carrie Chowske:** Because they're like, I forgot what I was going to say.

**Carrie Chowske:** I'm sorry, my head, my brain just like stopped mid thought.

**Carrie Chowske:** But so like, where we're where we're at with it is that they've got, like a lot of different clusters, but they've got only got a few that are performing, which kind of reminds me of what was going on with engine a while back when we like narrowed that down.

**Carrie Chowske:** And so like, if I was looking at the individual like clusters, like some only a couple of them are doing even remotely well by cluster.

**Carrie Chowske:** So I was thinking like doing like an evaluation of like the pages, like to see like if there's a pattern that I could notice.

**Carrie Chowske:** And the problem is the same one that we were having with like Yerko, like their pages don't have any sort of CTA on them.

**Carrie Chowske:** was trying to find where I dropped the link in here.

**Carrie Chowske:** I know I did.

**Carrie Chowske:** Here we go.

**Carrie Chowske:** And it's just like a big wall of text.

**Carrie Chowske:** Like what in the world would make you want to like read this, let alone interact with it in any way?

**Carrie Chowske:** You know, like, I mean, this is okay.

**Carrie Chowske:** That's fine.

**Kyle Gaudreau:** But.

**Kyle Gaudreau:** Actually, this is a pattern that like has always been actually gets a little bit better as you go through.

**Kyle Gaudreau:** But luckily, this isn't nearly as prevalent, but it's somewhat triggering for me because in the early days of growthx, God, like all our content looked this way was brutal, is just like header a sentence or two headers.

**Kyle Gaudreau:** Sentence or two.

**Kyle Gaudreau:** It's like, that is just not, yeah, it's not usually a great story or user experience, but this does seem to improve a little bit.

**Kyle Gaudreau:** Going back to the data, though, one thing to, there seems like there could be like a slight disconnect in kind of like what this is showing and then what you were showing in the Notion doc to some degree.

**Kyle Gaudreau:** Because you were basically showing that all clusters had sub 40%, I think is what it said.

**Kyle Gaudreau:** Maybe not all, but like those like handful of clusters.

**Kyle Gaudreau:** But then when we look at like the top traffic here in this time frame.

**Carrie Chowske:** Yeah, it's much better.

**Carrie Chowske:** Yeah.

**Kyle Gaudreau:** So once it just like called up.

**Carrie Chowske:** I don't know if I have this on the same time period either.

**Carrie Chowske:** Like, don't, that's what I was trying to look for.

**Carrie Chowske:** That's why I was stumbling through what I was saying.

**Carrie Chowske:** I was trying to look and see what I had told.

**Carrie Chowske:** Because I, I use more than just this, but.

**Kyle Gaudreau:** Try clicking like the first blog there.

**Kyle Gaudreau:** Just select it so.

**Kyle Gaudreau:** It updates the chart.

**Kyle Gaudreau:** I'm just curious what this shows.

**Kyle Gaudreau:** Okay.

**Kyle Gaudreau:** Maybe not in this case, but anyways, part of the point just to like watch out for is like if you're looking at an extended period of time and then you're looking at that like URL, like you're looking at the blended engagement rate over that period of time, that may not tell you like the recency on that trend.

**Kyle Gaudreau:** And so anyways, there seems like there's some kind of like disconnect where when you look at these top traffic pages, a good chunk of them are over 40%.

**Kyle Gaudreau:** But for whatever reason, that other view you were looking at is different.

**Carrie Chowske:** So just maybe there's a recency trend to be mindful of here and dig into.

**Carrie Chowske:** Yeah, you found the other reason why I didn't volunteer right away.

**Carrie Chowske:** So I was trying to figure out why it was showing differently because I use more than just the looker.

**Kyle Gaudreau:** Like I pulled other data for it.

**Kyle Gaudreau:** And I don't remember.

**Kyle Gaudreau:** And it's all good.

**Kyle Gaudreau:** Like this isn't, this isn't meant to be like.

**Carrie Chowske:** No, I know.

**Carrie Chowske:** I just wanted to give you a better answer.

**Carrie Chowske:** That's all.

**Kyle Gaudreau:** I didn't.

**Carrie Chowske:** All All good.

**Carrie Chowske:** But yeah, I think like, I think it's like the, the, the short version of it is that these pages aren't.

**Carrie Chowske:** They're not built for conversion.

**Carrie Chowske:** That's really the TLDR, right?

**Carrie Chowske:** So, and that's a commonality across all of their content and, like, a thing.

**Carrie Chowske:** And I think when I was going back through, like, notes and stuff, they've talked more about conversions, but we've not been doing anything to, like, further that for them.

**Carrie Chowske:** So that was another thing for me that really flagged that as, like, that's something where they're watching it, but we're not.

**Carrie Chowske:** But when they talk to us, they're wanting us to just, like, talk about, like, lately, I think there was, like, we were talking about sessions was, like, the only thing that they really cared about.

**Kyle Gaudreau:** And I'm kind of like, well, do you really, though?

**Kyle Gaudreau:** Because you're also talking about all these other things.

**Kyle Gaudreau:** So.

**Kyle Gaudreau:** Yeah, mean, knowing AIMBit a little bit, I think one of the struggles in the early going when they were talking about conversion was, it's like, of course, that's what we want to build towards.

**Kyle Gaudreau:** But if you don't have the traffic, then us optimizing towards conversion when you have no traffic isn't necessarily going to move the needle.

**Kyle Gaudreau:** That doesn't mean we can't.

**Kyle Gaudreau:** And do some foundational things to like, would be a good user experience and conversion foundation to like set with these blogs that we're creating.

**Kyle Gaudreau:** But at the same time, it's like, you know, if you're bleeding at the top of the funnel, you can't just magically create conversions at the bottom.

**Kyle Gaudreau:** So, yeah, I would dig in a little bit more of what's happening on like, is there, like on the recency of those engagement rates, is that trending up?

**Kyle Gaudreau:** Is that trending down?

**Kyle Gaudreau:** I do think we have to explore like, probably some like tweaks to our dashboards to make some of those kind of like analyses a little bit easier to parse, because I do think you have to dig a little bit more than is ideal.

**Carrie Chowske:** That's the other thing, I can't see the trend, because Vivek changed all of his lookers to monthly, and I can't figure out how to change it back to weekly.

**Kyle Gaudreau:** Oh, I can help you with that real quick.

**Kyle Gaudreau:** Let's do this live just so everyone knows how to do this.

**Kyle Gaudreau:** I even noticed Katya set up something, I haven't validated that it works 100%, but she did something fancy, at least.

**Kyle Gaudreau:** I assume it was her, that like you can actually like change the time frame with a drop down.

**Carrie Chowske:** But if you want to share your screen real quick, I can help you fix that.

**Carrie Chowske:** Yeah, I was like, I know how to do a lot of things, but why I couldn't figure out how the hell.

**Kyle Gaudreau:** It's a little hidden, to be honest.

**Kyle Gaudreau:** So go to date on the dimension and click the little calendar.

**Kyle Gaudreau:** I don't know, sorry, on the right side, click that pencil in there, go to ISO year week.

**Kyle Gaudreau:** Under date and time, yep.

**Kyle Gaudreau:** And that will give you weeks.

**Carrie Chowske:** Cool. I do that on all of my Looker dashboards.

**Kyle Gaudreau:** Yeah, so sometimes I'll just like go in and play around with that and swap it.

**Kyle Gaudreau:** But yeah, you can always do that quite quickly.

**Kyle Gaudreau:** But yeah, Katya, one of her dashes, I noticed she had like a drop down that let you like swap.

**Kyle Gaudreau:** I didn't even realize you could do that in Looker Studio.

**Kyle Gaudreau:** So maybe that's an easier workflow.

**Carrie Chowske:** Yeah, I find that like...

**Talal Syed:** So I think that heavily depends on what kind of topics exist within that cluster.

**Talal Syed:** So if one cluster has a lot of bottom of funnel content, when you do like an aggregate engagement rate, it's always going to be lopsided.

**Talal Syed:** So I think like if you want to do that level of analysis, you kind of have to figure out if there are like top of funnel, middle of funnel, and what are the bottom of funnel keywords in there.

**Carrie Chowske:** Yeah.

**Talal Syed:** And sort of like factor that in.

**Talal Syed:** Otherwise, it's always going to be not accurate of what's actually going on, I think.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** That might have even been what I did actually. I don't remember.

**Carrie Chowske:** I know I like sorted through at first.

**Carrie Chowske:** I didn't like use everything because I was trying to look at something specific and I apparently did not keep track of what I used to filter.

**Carrie Chowske:** So that's really useful for this, isn't it?

**Kyle Gaudreau:** And yeah, like go through and like take a look at some of those queries too.

**Kyle Gaudreau:** Just, I know it's like super manual, but like it can be really helpful because it is not uncommon for you.

**Kyle Gaudreau:** You look at the queries and it's like obvious — oh, we're not even capturing something in tech, we should be.

**Carrie Chowske:** And that's why the engagement rate is bad.

**Carrie Chowske:** That was actually part of it.

**Kyle Gaudreau:** Yeah, so I certainly would.

**Carrie Chowske:** I'll send you what I actually did, Kyle, and you can be like, hey, I just, I was like distracted by the fact that I couldn't, I couldn't figure out what timeframe I had used, so.

**Kyle Gaudreau:** All good, all good.

**Kyle Gaudreau:** All right, well, who do we have on?

**Kyle Gaudreau:** We have Liz and Eric left.

**Kyle Gaudreau:** Any of you, either of you rather, want to go first?

**Erik O'Brien:** I'm happy to be a test subject here.

**Kyle Gaudreau:** Cool.

**Erik O'Brien:** So when you talk about looking at queries, I think that's a big gap that I have of like, where do we go to look at it and how do we do that?

**Erik O'Brien:** Because I think I've got two accounts, Deepgram and Airby, both seemingly great traffic for how long we've been publishing.

**Erik O'Brien:** Like I treat.

**Erik O'Brien:** treat.

**Erik O'Brien:** Airbyte is basically a net new kind of client after November strategy sprint, but engagement rates are not really where we want them.

**Erik O'Brien:** So let me go to Airbyte, actually.

**Erik O'Brien:** And it's across the board for basically all the topics that we've been putting out across clusters.

**Erik O'Brien:** Like it's pretty even split of traffic that we're getting, but it's also pretty consistently like low on engagement rates.

**Erik O'Brien:** And so that's kind of where I get stuck, given my lack of experience in this space of like, where do we go to next of understanding engagement rates?

**Erik O'Brien:** Is it kind of looking at the specific kind of format of the blog template that we use?

**Erik O'Brien:** Is it kind of having strong...

**Erik O'Brien:** stronger hooks at the top.

**Erik O'Brien:** We added a lot of these TLDRs to try to keep people at least engaged for the first few scrolls, but I think I'm kind of running into a wall of, like, what ideas do we want to explore to try to kind of boost engagement for these guys as they continue to try to build traction here.

**Kyle Gaudreau:** Yeah, interesting.

**Kyle Gaudreau:** The fact that it is happening across most clusters could certainly point to that there's some broader things we need to consider with the experiences.

**Kyle Gaudreau:** Taking it to the queries, there's a few kind of layers you could consider this in.

**Kyle Gaudreau:** One way that this can be helpful is just, like, picking one of, like, the top traffic pages and, like, starting to work through.

**Kyle Gaudreau:** So if we take, like, that URL, for example, and, like, if you can, like, copy this, I know it's a little hard to select.

**Kyle Gaudreau:** There, yeah, let's go to GSC, and yeah, let's pop that in there.

**Kyle Gaudreau:** So I'm not like as familiar, obviously, with this, but what we want to try to understand is like, well, that's weird.

**Kyle Gaudreau:** Sometimes you are going to see weird queries like that.

**Kyle Gaudreau:** But are there any patterns of things that we see in here that like does not seem to be like as relevant to like the intention of the content we were creating?

**Kyle Gaudreau:** And so a little hard for me to say without like knowing the piece super well or like being as in the loop with like the direction you all been going with Airbyte recently.

**Kyle Gaudreau:** But, you know, it's a little bit tough when you don't see like all the clicks in here.

**Kyle Gaudreau:** This is just this is unfortunately.

**Kyle Gaudreau:** Like part of the reality with GSC, it's not going to give us all the query data.

**Kyle Gaudreau:** This doesn't mean you haven't, you've only gotten clicks from that one query.

**Kyle Gaudreau:** So, you know, directionally, like looking at like what's driving the most impressions, if you sort by impressions in that table, just like click the impressions.

**Kyle Gaudreau:** No, down by like the area.

**Kyle Gaudreau:** Yeah, yeah.

**Kyle Gaudreau:** So this might be able to give you like a slightly better pulse on like what's serving this more often, but like not 100% true.

**Kyle Gaudreau:** And then I would just like take some of these as well.

**Kyle Gaudreau:** Like if there's, you know, if this is passing like the initial test of like, yeah, these look like the kind of things we were intending to be going after and do seem relevant.

**Kyle Gaudreau:** You know, certainly consider like, are we like actually answering some of these, if these do feel relevant, like, are we actually like effectively answering, you know, these sorts?

**Kyle Gaudreau:** We're

**Kyle Gaudreau:** Yeah, that's a good point.

**Kyle Gaudreau:** That is a simpler way of starting for sure.

**Kyle Gaudreau:** Yeah, because jumping into the queries may get you into the weeds a bit too much.

**Kyle Gaudreau:** So, but the fact that this is happening across all their clusters does feel telling.

**Kyle Gaudreau:** When did we first start publishing content?

**Kyle Gaudreau:** It was like December?

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Okay.

**Kyle Gaudreau:** Interesting.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** mean, it's trying to reach like AI engineers and software engineers building for agents.

**Erik O'Brien:** Obviously, there's not a lack of content out there right now.

**Erik O'Brien:** I think coming to Airbyte, maybe like in landing on some of these pages of like walls of text might just be what it is.

**Erik O'Brien:** So we've.

**Erik O'Brien:** I've talked to Mario kind of about, like, how do we do some sessions?

**Erik O'Brien:** And I think I told you, Kyle, like, how do we do some sessions with one of their solution engineers and kind of be like, what do you read if you're out there looking for information?

**Erik O'Brien:** Trying to get better insights from some of their gong calls of where they're talking to customers, like, what questions are they asking?

**Erik O'Brien:** So we've got some of that kind of, how do we get a little bit closer to what developers want and are asking for?

**Erik O'Brien:** Like, in the backlog of things to get done?

**Erik O'Brien:** But yeah, I'm just kind of at the point where, like, do we go back and refresh all 40 articles that we've done right now?

**Kyle Gaudreau:** I wouldn't do it in mass.

**Kyle Gaudreau:** You know, I would just try to think about this in, like, an experimentation mindset.

**Kyle Gaudreau:** But, you know, doing some of the steps you're already taking sounds great.

**Kyle Gaudreau:** right.

**Kyle Gaudreau:** All

**Kyle Gaudreau:** And, you know, related to what Talal mentioned of starting with the primary keyword, I would try to think about like, you know, try to see some of the patterns of like how well you are capturing those and ranking and like taking that alongside like the relative difficulty of them, it can be helpful.

**Kyle Gaudreau:** So meaning that like, are we struggling to rank for a lot of these because they're like pretty competitive?

**Kyle Gaudreau:** If it's maybe not super competitive, the other thing to like consider is just like, where do we have the highest search volume opportunity right now and picking a few of those and perhaps starting with, you know, enriching those.

**Kyle Gaudreau:** But there's just like, you know, where do we have low hanging fruit, where do we have a lot of search volume opportunity to capture, picking off a few of those and trying to enrich those pages.

**Kyle Gaudreau:** But yeah, I would look at, you know, if you take like all the URLs that we've done for them so far and just look at like, like what's the relative like number of queries each one of those has and like the rankings of them, you could start to just like prioritize that list a little bit more.

**Kyle Gaudreau:** I can show you how to do that just to, you know, for time's sake, you know, probably won't be able to do that live, but you could do that using search analytics for Google Sheets add-on that we were showing last time and just like connect it to Google Search Console, pull out some of the data and just start to play around with like what are we seeing in there.

**Kyle Gaudreau:** So, so yeah, just a few different cuts to like help you prioritize and like whittle through the list rather than just trying to update everything in mass.

**Kyle Gaudreau:** And then as you're doing that, as you're having those conversations with Mario, like what are just some of the ideas, the hypotheses we have to start to make these content experiences better, focus it on that.

**Kyle Gaudreau:** I haven't actually played around with Firecrawl yet.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** I've been hearing about it here and there, I'm like, yeah, this is just an event.

**Talal Syed:** Claude's own webfetch can be a little tricky.

**Talal Syed:** Firecrawl has everything.

**Talal Syed:** Yeah.

**Talal Syed:** And it gives you everything in Markdown.

**Kyle Gaudreau:** So it's really good.

**Kyle Gaudreau:** Is that a paid subscription that you're using?

**Talal Syed:** Or how does Firecrawl use?

**Talal Syed:** It's pretty cheap.

**Talal Syed:** It's, like, $19 for, like, thousands of scrapes.

**Kyle Gaudreau:** Cool.

**Kyle Gaudreau:** Maybe we've to figure out getting the team access to that then.

**Kyle Gaudreau:** Cool.

**Kyle Gaudreau:** Last but not least.

**Liz Kushnereit:** What do you want to run through, I wasn't sure how to approach this since I only have three accounts and two of them are actively in review with Talal at this moment for the strategy.

**Liz Kushnereit:** So I don't know what's super helpful for me.

**Liz Kushnereit:** I can, like, just go off the cuff.

**Liz Kushnereit:** All right.

**Liz Kushnereit:** just All Good, you.

**Liz Kushnereit:** The result of that is a really large amount of cannibalization.

**Liz Kushnereit:** And so that had to be dealt with later on.

**Liz Kushnereit:** But before I get into that, I'll just show you guys what it looks like now.

**Liz Kushnereit:** So Syl, who's our contact, think, just did this in a weekend.

**Liz Kushnereit:** He redid the website.

**Liz Kushnereit:** And it looks so much better, as we can see.

**Liz Kushnereit:** He created CTA components for us.

**Liz Kushnereit:** And so this is one of them.

**Liz Kushnereit:** And then we did a lot of work with the help of Saskia to actually embed tables for our highest performing pieces.

**Liz Kushnereit:** And so, yeah, I think you can see this obviously does a lot better.

**Liz Kushnereit:** I think this speaks more to a dev.

**Liz Kushnereit:** And this piece gets cited a lot in AI visibility.

**Liz Kushnereit:** But it doesn't, as we know, doesn't always recommend Augment as the tool of choice.

**Liz Kushnereit:** And then the UX, I think, has been improved quite a bit as well.

**Liz Kushnereit:** So before, it didn't have this much information on the page.

**Liz Kushnereit:** It would just be like, just go install.

**Liz Kushnereit:** So there was definitely, it was tricky, like, how to address that.

**Liz Kushnereit:** Well, we need to do refreshes.

**Liz Kushnereit:** And so this is the direct result of refreshes and they were targeted, right?

**Liz Kushnereit:** Like the best performing pieces.

**Liz Kushnereit:** And then we refreshed all of them that took forever.

**Liz Kushnereit:** Because at that point, I think we had 300 live articles and refreshed like 120 or something of them.

**Liz Kushnereit:** But then we started to see that bump here, like of all of that work into December.

**Liz Kushnereit:** The trough is redirects.

**Liz Kushnereit:** And so like we built learn tools as new pages.

**Liz Kushnereit:** And then tools, we migrated basically all of our high performing content there.

**Liz Kushnereit:** And then also added new high performing, like there's a new canonical piece now on tools.

**Liz Kushnereit:** So we have like two really strong pieces there.

**Liz Kushnereit:** And then that lifted up again.

**Liz Kushnereit:** So that was cool.

**Liz Kushnereit:** But also around here, a lot of it is switched to like product led.

**Liz Kushnereit:** So they have the coding assistant, they have code review.

**Liz Kushnereit:** And then this week, they launched the intent app.

**Liz Kushnereit:** And so a lot.

**Liz Kushnereit:** A of what's here in that new canonical piece is for code review.

**Liz Kushnereit:** So we, at this moment in time, own the category of code review tools, and we have like almost 30 number one keywords.

**Liz Kushnereit:** So that worked really well, taking that approach and producing them fast.

**Liz Kushnereit:** And then we are still, so like what Talal is helping with is like the bigger picture, though, because we can't just do everything based on that.

**Liz Kushnereit:** So we're actively trying to relaunch MCP with much better content.

**Liz Kushnereit:** And I'm getting a little bit ahead of myself, though.

**Liz Kushnereit:** And then I wanted to point out conversions because a lot of the conversation comes down to conversions.

**Liz Kushnereit:** And then what we saw is that just this previous week was the first time I saw conversions like truly, truly jump.

**Liz Kushnereit:** So this last month we had, these are signups.

**Liz Kushnereit:** these are paid signups.

**Liz Kushnereit:** Augment took away any free trial.

**Liz Kushnereit:** So these are like really valuable.

**Liz Kushnereit:** This last week we had 69 signups.

**Liz Kushnereit:** Thanks for for for running.

**Liz Kushnereit:** And the weeks prior was like 39, 39, 30, 20, 17.

**Liz Kushnereit:** I think it was like 14 in December at one point.

**Liz Kushnereit:** And so that has helped us a lot.

**Liz Kushnereit:** And then we have it broken down.

**Liz Kushnereit:** So I told you guys, top AI coding assistance is what our top piece.

**Liz Kushnereit:** Our second top is open source.

**Liz Kushnereit:** And then we see conversions there.

**Liz Kushnereit:** And then also Claude versus Augment, which is great.

**Liz Kushnereit:** Like if that's a true decision maker one and they're choosing Augment.

**Liz Kushnereit:** Um, but yeah, so that's kind of like looking back at Augment, we've done a lot to get them to like a better place where we are now.

**Liz Kushnereit:** And they also helped as a client and still says he feels like he gets his money worth week over week because I didn't mention traffic, but traffic also is just gone up every week since December.

**Liz Kushnereit:** So it went from like, I think 7,000 a week to now it's like 36,000 a week.

**Liz Kushnereit:** And so we're really happy with that.

**Liz Kushnereit:** Our CTR is finally going up, but all, I guess it's just proving Kyle's point.

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

**Liz Kushnereit:** I just had like a little script, which I'm happy to share. It pulls a weekly JSON of everything in Fathom, because Fathom goes way further back in time, you know, which I'm happy to share.

**Kyle Gaudreau:** You may have shared it in DMs. Sorry, I don't see that if you had shared that at one point, but yeah, sorry, it's a little embarrassing.

**Liz Kushnereit:** It's just like a little Python script, you know, but just, yeah, it helps.

**Liz Kushnereit:** I think, like, long term, we should, sorry, go ahead, Talal.

**Talal Syed:** No, you're good.

**Liz Kushnereit:** Oh, just, like, long term, I think we need MCPs — and this has been talked about across all clients — to pull in all of that context indefinitely, like Notion, Slack. But I think the transcripts are where you really learn the stakeholders' vision, where the risks are, who cares about what. My experience comes out there.

**Kyle Gaudreau:** Yeah, agreed.

**Kyle Gaudreau:** I love the thing that Panzer built of, that we were talking about earlier, the gap I do see in it, it doesn't have, it didn't have anything around transcripts, and there's just, like, yeah, there's so much richness that comes through that.

**Andi Bailey:** We had this conversation yesterday, so we're working on figuring out the right way to do it.

**Andi Bailey:** The danger, Liz, you have your own GPT, so it's very useful, but we can't put it in our podclods because it doesn't know how to distinguish between private and public documents and conversations yet.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** So we'll figure it out.

**Kyle Gaudreau:** If we need to create a personal account for each person, I think the efficiency in itself will pay off tenfold for the engagement managers.

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

**Kyle Gaudreau:** Yeah. And Matt mentioned he couldn't make it today because of the time zone.

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
