# Jakub / Matthew - Innerwell & Siit Catch-up

<metadata>
date: 2025-12-01
time: 15:31 UTC
duration: 54 minutes
organizer: matthew.alves-hill@growthx.ai
participants: Jakub Rudnik, Matthew Alves-Hill
fathom_recording_id: 105222942
fathom_url: https://fathom.video/calls/491990177
share_url: https://fathom.video/share/wt6RGtGQQsbdxQbHQw-VWX-Czs5oRoqx
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Matthew and Jakub aligned on strategies for two clients: Siit, a ITSM software company, needs final recommendations on Reddit content integration and GA4 tracking issues; Innerwell, a ketamine/mental health provider, is blocked by client delivery gaps on a mental health landing page and 500 errors on availability pages, with Matthew planning daily Slack updates to manage dependencies. The team also wrapped Home Base (one-month severance) and confirmed Siit's traffic performance is strong despite earlier conversion pressure.

---

## Context

Matthew and Jakub are delivery leads at GrowthX, and this meeting covers two main client projects. Siit is a software company that sells ITSM solutions; GrowthX has been doing content marketing and SEO work, with strong recent performance on comparison and alternatives pages. Innerwell is a healthcare provider offering ketamine therapy and mental health services; the project involves a complex URL restructuring and content redirect plan that's been hampered by Innerwell's slow execution. Both clients represent different challenges: Siit has strategy questions that need closure, while Innerwell has blocking technical dependencies that the client keeps delaying.

---

## Relevance

**To GrowthX Delivery:**
- Siit's Reddit strategy shows three testable tactics: embedding existing high-traction Reddit posts, scraping subreddits for topic ideas, and creating a client-owned subreddit to bypass gatekeepers and get picked up by LLMs
- Siit's GA4 setup has multiple zero-conversion events ("form_submit_try_for_free") that strongly suggest misconfiguration; recommend asking Siit who configured GA4 (likely WebStacks) and requesting setup documentation before diagnosing further
- Innerwell project requires turning on all broken "availability" pages (currently returning 500 errors), creating 301 redirects with proper breadcrumbs, and implementing a new "Ketamine Near Me" directory page to fix broken navigation
- Innerwell is using GrowthX Labs for URL mapping and redirect implementation; Matthew is posting daily Slack updates in the Innerwell external channel to create visibility around client blockers and delays

**To GrowthX Business Development:**
- Siit sentiment has shifted from "we need conversions" to "we love the traffic and content." CMO is impressed; indicates solid account health and opportunity for Q1 content audit refresh due to messaging changes
- Innerwell is an account recovery story but remains high-maintenance; Jakub has flagged declining health scores due to POC (point-of-contact) not moving work forward despite GrowthX doing extra uncompensated work. Editorial roadmap is strong; technical execution is the blocker
- Home Base account ramping down to severance mode with 10 Q&A articles per week; project complete with audit and refresh sheet delivered

**To CheckThat / AI Visibility:**
- Siit exploring client-owned subreddit strategy specifically to bypass Reddit community gatekeepers and get content picked up by LLMs for better visibility in AI-driven search and recommendations

---

## Overview

- **Siit:** To finalize the Reddit strategy, the team will recommend three tactics: embedding Reddit content, scraping subreddits for ideas, and creating a client-owned subreddit. The product demo video will be embedded in articles to boost engagement, with the CTA leading to a "Book a Demo" page.
- **Innerwell:** The project is blocked by Innerwell's failure to deliver a mental health landing page and fix 500 errors on key "availability" pages. The immediate plan is to get these pages fixed and redirect them to the new URL structure, ensuring breadcrumbs and the "availability" module function correctly.
- **Client Management:** To manage risk, Matthew will post daily progress updates in Innerwell's external Slack channel to create a clear record of dependencies and highlight the client's delays.

---

## Key Topics

### Siit: Reddit & Video Strategy

  - **Reddit Content Strategy:**
      - **Goal:** Provide a final recommendation to resolve the client's indecision on using Reddit content.
      - **Recommendation:** Three tactics to test, with the scope dependent on whether the client's Reddit agency is still active.
        1.  **Embed Existing Reddit Content:** Integrate high-traction posts into articles (e.g., alternatives pages) to add authority and visuals.
        2.  **Scrape Subreddits for Ideas:** Use relevant subreddits (e.g., ITSM) to find topic ideas and FAQs for new content.
        3.  **Create a Client-Owned Subreddit:** Post repurposed content on a dedicated subreddit to bypass gatekeepers and potentially get picked up by LLMs.
  - **Product Demo Video CTA:**
      - **Goal:** Determine the best use for Siit's new product demo video.
      - **Recommendation:** Embed the video directly in articles.
          - **Rationale:** Improves time-on-page (SEO) and conversion rates.
      - **CTA Options:**
        1.  **"Book a Demo":** Higher friction but aligns with the client's primary goal.
        2.  **"Try for Free":** Lower friction, likely resulting in more conversions.
      - **V2 Idea:** Create a dedicated landing page with the video and conversion copy.

### Siit: GA4 Tracking Issues

  - **Problem:** Siit's GA4 setup is unreliable, with many conversion events showing zero activity. The client also uses HubSpot and PostHog for tracking.
  - **Initial Investigation:**
      - The "form\_submit\_try\_for\_free" event showing zero conversions is highly suspicious and likely indicates a setup error.
      - **Hypothesis:** The issues stem from a web agency (WebStacks) that previously handled the setup.
  - **Action Plan:**
    1.  **Identify Setup Owner:** Ask the client who configured the GA4 events and if documentation exists.
    2.  **Test Key Events:** Manually trigger the "Request a Demo" and "Try for Free" events to verify they fire correctly.
    3.  **Consult Experts:** If issues persist, consult internal experts like Kyle, Suleiman, or the \#general Slack channel.

### Innerwell: Project Blockers & Redirect Plan

  - **Project Blockers:**
      - **Missing Landing Page:** The project is stalled until Innerwell delivers the required mental health landing page.
      - **Broken "Availability" Pages:** Key "availability" pages are returning 500 errors, causing traffic loss and hurting SEO.
  - **Redirect Strategy:**
      - **Phase 1: Fix & Redirect "Availability" Pages**
        1.  **Innerwell:** Fix the 500 errors on all "availability" pages.
        2.  **GX Labs:** Create a URL map using GPT to match old "availability" URLs to the new `/ketamine/state/city/` structure.
        3.  **GX Labs:** Implement 301 redirects, ensuring breadcrumbs and the "availability" module function correctly.
      - **Phase 2: Redirect "Mental Health" Pages**
          - Once the client delivers the mental health landing page, redirect all mislabeled "ketamine therapy" pages (which are actually mental health content) to the new `/mental-health/state/city/` structure.
      - **Future Phase (V2/V3):** Build new, fully optimized city-level ketamine pages.
  - **Navigation Strategy:**
      - **Goal:** Fix the broken site navigation to ensure users can find city-level pages.
      - **Plan:** Replace the current state-selection module with a single link to a new "Ketamine Near Me" directory page.
      - **Function:** This page will list all states, with each state expanding to show its cities, all linking to the correct new URL structure.

### Home Base Project Status

  - The project is complete. Jakub delivered the content audit video and refresh sheet.
  - Matthew is now producing 10 question-and-answer articles per week.
  - The account is expected to ramp down over the next month.

---

## Action Items

**Jakub Rudnik**
- Slack Matthew Reddit example re: client posting on own Reddit
- Decline Tavern invite

**Matthew Alves-Hill**
- Confirm w/ Seat if Reddit agency still engaged; then decide Reddit recs
- Audit Seat GA4: check streams, test Request a Demo + Try for Free, review 6-mo conversions; then ask Kyle/Suleiman if needed
- Ask Seat who set up GA4 and request setup docs
- Post Innerwell channel: Mon waiting-for list; Fri check-in
- Forward Home Base severance details to Jakub

---

## Transcript
**Jakub Rudnik:** Like, just a long day, but we're back.

**Jakub Rudnik:** I'm sure soon I'll feel back to normal, back in the swing.

**Jakub Rudnik:** But, yeah, all the beauty of the company that's worldwide is, like, everything keeps going.

**Jakub Rudnik:** But then the tough part is that you come back to stuff that's been going.

**Jakub Rudnik:** Yeah.

**Matthew Alves-Hill:** Where do your folks live?

**Jakub Rudnik:** My parents live in Michigan, so they're about two and a half hours north of us.

**Jakub Rudnik:** My wife's family is outside of Chicago.

**Jakub Rudnik:** So, what a good day.

**Jakub Rudnik:** That's, like, five and a half hours.

**Jakub Rudnik:** But, yeah, they got six inches of snow or something like that over the break.

**Jakub Rudnik:** And then on the drive home, there was still some of that, but it was snowing on and off.

**Jakub Rudnik:** We go around Lake Michigan, a lot of lakefront or lake effect, whatever you want to call it.

**Jakub Rudnik:** So, just gripping the steering wheel, going slow, everybody slamming on the brakes, all that stuff.

**Jakub Rudnik:** Verstanden.

**Matthew Alves-Hill:** Verstanden.

**Jakub Rudnik:** Yeah, I just feel like I was, like, wound up at, you know, 9 o'clock at night.

**Jakub Rudnik:** Like, how do I, like, calm my body down and, like, my brain down?

**Jakub Rudnik:** But we did it, so all good.

**Matthew Alves-Hill:** Yeah, I know the feeling, like, when we drive, when we go, like, to visit Leia's folks or into the bush, you do a lot of driving, and South Africa has, like, one main road between Cape Town and Johannesburg, and it's, like, a one-lane highway.

**Matthew Alves-Hill:** So you just, you're overtaking trucks, like, the entire way, and it's a 15-hour drive, and by the time you're there, you're, like, wired from, it's so...

**Jakub Rudnik:** oh my god.

**Jakub Rudnik:** That sounds, that's some stress, yeah.

**Jakub Rudnik:** Oh, man.

**Jakub Rudnik:** Yeah, I like driving, but that's, like...

**Matthew Alves-Hill:** 15 is too many.

**Matthew Alves-Hill:** 15 is too many, and then, like, the middle of South Africa is just desert, so there's nothing to look at either.

**Matthew Alves-Hill:** Like, two hours in, it desert starts, and then it's 15 hours.

**Jakub Rudnik:** Oh, no.

**Jakub Rudnik:** That's horrible.

**Jakub Rudnik:** horrible.

**Jakub Rudnik:** That's horrible.

**Jakub Rudnik:** Wow.

**Matthew Alves-Hill:** Cool.

**Matthew Alves-Hill:** So I'm not going to, I'll try not to drop you in and straight away.

**Matthew Alves-Hill:** Again, we had a bit of a, Moses messaged me actually this morning.

**Matthew Alves-Hill:** don't know if you saw that message seems to be doing better.

**Matthew Alves-Hill:** It was his last week, last week.

**Matthew Alves-Hill:** So I need to speak to Andy because he didn't, because he was off his last week.

**Matthew Alves-Hill:** There's no like handover documentation from him at all.

**Jakub Rudnik:** So I don't, I don't know.

**Matthew Alves-Hill:** It may be a case of like, that's just how the dice rolled and Lawrence is just going to get dropped in it and I'll have to help as much as I can.

**Matthew Alves-Hill:** But it's not, it's not ideal.

**Matthew Alves-Hill:** I've been looking into, I had to push some things for seat last week anyway, because Moses was off.

**Matthew Alves-Hill:** And Thanksgiving and all that stuff, but now like diving into it today, I've spent like six hours in Seat and he clearly wasn't doing a lot of like optimization on our side.

**Matthew Alves-Hill:** So it's a double whammy of stuff there.

**Matthew Alves-Hill:** But yeah, I'll let you know.

**Matthew Alves-Hill:** I guess at this point it's really kind of beyond you, but yeah, it's not, it's not great.

**Matthew Alves-Hill:** And I'm picking up him a bit this week.

**Matthew Alves-Hill:** So fun, fun start.

**Matthew Alves-Hill:** But on Seat, she, so we had a good, we had a good meeting.

**Matthew Alves-Hill:** She definitely has raised this Reddit discussion again.

**Matthew Alves-Hill:** I think like she can't make her mind up really about it.

**Matthew Alves-Hill:** But I think like, I'm not quite clear.

**Matthew Alves-Hill:** She's going back and forth with

**Matthew Alves-Hill:** Whether they should do that or whether they shouldn't.

**Matthew Alves-Hill:** I don't really know how to give her a clear recommendation on using the Reddit seeded posts and that kind of thing.

**Matthew Alves-Hill:** I could just stop it at like, I really can't help you here on that side, but because we broached it fast, I don't know if it's like, if you could help maybe just tying up like a final kind of like, this is, we'd recommend this or we wouldn't, and then kind of put the ball like completely in her court.

**Matthew Alves-Hill:** And then I don't want it to become like a continual topic that she raises.

**Matthew Alves-Hill:** So I don't know, that's one thing, whether you can help on that just to finalize it.

**Jakub Rudnik:** So they want, are they trying to figure out how to like use Reddit within their content?

**Jakub Rudnik:** Is that the, sorry, I'm not.

**Jakub Rudnik:** Yeah, it is.

**Matthew Alves-Hill:** And I think like she's seen the, so she's chuffed with like the.

**Matthew Alves-Hill:** The performance of the integration tools and that kind of thing, like, especially the comparisons and the alternatives.

**Matthew Alves-Hill:** So I think she sees, she's wondering whether there's value in, like, using those pages as, whether it's linking or content itself for, like, super long tail Reddit discussions, I suppose.

**Matthew Alves-Hill:** It's just a gap for me.

**Matthew Alves-Hill:** Like, I don't really know how to recommend, like, besides going, like, yeah, this kind of content is very relevant to those kind of forums.

**Matthew Alves-Hill:** I don't really know how to give her advice on, like, how to use that properly.

**Matthew Alves-Hill:** I think she was toying with the idea of literally just, like, copy and pasting this kind of article or summarizing it with GPT and then, like, using that to seed Reddit posts.

**Matthew Alves-Hill:** But, like, in terms of the actual ops of it, I don't, I mean, I don't know how to open that.

**Jakub Rudnik:** Yeah, things I would do with Reddit if I were.

**Jakub Rudnik:** It would be take the things that already have traction or good comments that you either find organically or the agency did and naturally embed them into the post that makes sense.

**Jakub Rudnik:** If they compare Seat to something, go find our alternatives or our versus page and put that and embed that content directly in.

**Jakub Rudnik:** It adds visuals.

**Jakub Rudnik:** It adds some authority and theory, stuff like that.

**Jakub Rudnik:** I'd link to those and embed them.

**Jakub Rudnik:** yeah, the topics, I do think if they find the perfect ICP, I think there are some of these like ITSM, if there's an ITSM subreddit, scraping those for potential topic ideas and that, or for like FAQs in the article, you know, like you basically need to like find all the things that people are talking about and then repurpose those.

**Jakub Rudnik:** And that's, something like, I think we've done elsewhere.

**Jakub Rudnik:** I don't remember.

**Jakub Rudnik:** I've never done it specifically, but I feel like Jason or somebody has done something like that.

**Jakub Rudnik:** And then

**Jakub Rudnik:** Maybe the thing that they're thinking about, and I have shared with her before, can you hear my dog, like, weirdly growling?

**Jakub Rudnik:** She's like, I look very throaty, like, I'm not growling, but I am going on.

**Jakub Rudnik:** I've shared this with her before, I'll send to your Slack, just so it's there.

**Jakub Rudnik:** But this is, like, one of our clients, and they just, like, post on their own Reddit, and sometimes they get picked up in LLMs.

**Jakub Rudnik:** Instead of doing it to, like, a subreddit, they're just, like, bypassing the gatekeeper and getting worse engagement, but sometimes they're still getting picked up because it's, like, under the Reddit domain.

**Jakub Rudnik:** And so they just, like, repurpose a page that we created or that they created themselves.

**Jakub Rudnik:** And so I think versus or lists where they should be mentioned, the new list, the new alternatives, those would be good to test.

**Jakub Rudnik:** Yeah, just use ChatGPT, repurpose.

**Jakub Rudnik:** It shouldn't be an exact match, obviously, but like rewrite this, using this, post this.

**Jakub Rudnik:** I think those are all options.

**Jakub Rudnik:** I can let me know what to write up or what would be the best method to do some of those things.

**Jakub Rudnik:** Would those be the three?

**Matthew Alves-Hill:** Yeah, I think I need to clarify exactly whether they're still paying for this agency or not, because if they are, then it seems like we shouldn't be needing to do much here besides, like, suggesting these, making suggestions.

**Matthew Alves-Hill:** If it's her doing it herself and they've shared the agency, then I guess we can give her some more recommendations.

**Matthew Alves-Hill:** But, I mean, in theory, this is out of scope, this kind of thing, right?

**Matthew Alves-Hill:** Yeah, I think so.

**Jakub Rudnik:** I think, like, there's some of the work of, like, if she's like, I really want to embed all these comments or posts, and we can say, like, we will do that for a week.

**Jakub Rudnik:** Like, we need the, you know, I would get, like.

**Jakub Rudnik:** The long list of all the posts that the Reddit agency did, and then comments and stuff, then we can do a more manual week, but we should be subtracting output, like normal output, or something like that.

**Jakub Rudnik:** And then, like, if they were doing this full-time, like, we could build, like, potentially build something into Atlas, but that might be a, again, like, it's got to have a trade-off, so it should be extra.

**Jakub Rudnik:** Yeah, okay, cool.

**Matthew Alves-Hill:** Oh, the other thing she raised is this.

**Matthew Alves-Hill:** One second.

**Matthew Alves-Hill:** Oh, so.

**Matthew Alves-Hill:** This product demo video that they built.

**Matthew Alves-Hill:** So, has...

**Matthew Alves-Hill:** She's wondering whether we should use this as a CTA in the tools pages, and when I was on the call with her, was like, this is potentially something we could be embedding in the articles instead, and then still having the CTA as book a demo, as opposed to just watching the video as the CTA doesn't really necessarily make sense to me.

**Matthew Alves-Hill:** I mean, I guess it does, but I think this should probably, Webflow will let us embed this video directly in the content, which seems like a good idea.

**Jakub Rudnik:** Yeah, I would embed within the content, again, ads, visuals, it will extend the time on page, it'll have SEO results, it should have conversion results, assuming that it meets the intent.

**Jakub Rudnik:** And you could, like, if I was, like, a growth, if I was C and had this big growth team, I would, like, test the book a demo.

**Jakub Rudnik:** Oh, versus like watch a demo.

**Jakub Rudnik:** And then I would send them to a landing page that's like written, you know, about seats and had this at the top.

**Jakub Rudnik:** So it's like demo plus conversion copy.

**Jakub Rudnik:** So I think that's like an option, but I wouldn't just send them to like YouTube as the CTA for sure.

**Jakub Rudnik:** I would want that other page in the like shorter version should probably be sent to the landing page, give them the first view of the demo.

**Jakub Rudnik:** So, but that would be something that would be more of like a V2 would require more effort on their end.

**Jakub Rudnik:** But from a short term, definitely just go with the embed.

**Jakub Rudnik:** Embed, yeah.

**Matthew Alves-Hill:** And then the CTA like book a demo straight after it.

**Matthew Alves-Hill:** Yeah.

**Jakub Rudnik:** Or, I mean, I think that makes the most sense based on what they want to convert to.

**Jakub Rudnik:** I'd probably be like, now try, you know, I'd send them to a trial.

**Jakub Rudnik:** That'd be my instinct is like, you've now seen it.

**Jakub Rudnik:** So I would approach the, like, I'd probably give her those two options.

**Jakub Rudnik:** Like we think like this should improve from an SEO perspective.

**Jakub Rudnik:** Because of time and page and all that, it should improve conversions because people are seeing it right there.

**Jakub Rudnik:** It's a good video, et cetera.

**Jakub Rudnik:** Now the decision is like, do you want to be a little bit redundant and get a miss?

**Jakub Rudnik:** There'll be more friction, but it is the metric you want to move.

**Jakub Rudnik:** It's to be lower number of conversions.

**Jakub Rudnik:** The trials almost certainly will be a higher number, but is that truly what you want to be converting to?

**Jakub Rudnik:** So it's like, yeah, again, if they have a growth team behind this, they should be testing and like doing, like there's a bunch of math to like figure out what truly turns into users down the funnel, but that's like multiple stages of metrics for our purposes.

**Jakub Rudnik:** It's probably, which do you care about most?

**Jakub Rudnik:** But I would also advise that like, you can do it either way and here's the trade-offs.

**Matthew Alves-Hill:** Yeah, that makes sense.

**Matthew Alves-Hill:** And then, yeah, and then optimize the actual demo page.

**Matthew Alves-Hill:** So that includes this video in it and then, yeah.

**Jakub Rudnik:** And then like, they would, you know, like you have the resource and the time.

**Jakub Rudnik:** should be testing like demo page with nothing and just copy and visuals, demo page with this, like do people not.

**Jakub Rudnik:** Like

**Jakub Rudnik:** Actually booked the demo once they've seen this.

**Jakub Rudnik:** There's so many steps, but it's just her and us, and we don't get paid to do this stuff, really.

**Jakub Rudnik:** We can advise, but you're probably just going be like, here's the lowest friction and our best guess.

**Jakub Rudnik:** But if you were doing this, if they were a team of 100 people, they would be doing all these tests constantly, because this would be one of the most important pages.

**Jakub Rudnik:** Yeah, exactly.

**Matthew Alves-Hill:** Okay, that makes sense.

**Matthew Alves-Hill:** And the final thing is this GA4.

**Matthew Alves-Hill:** So I raised it with her.

**Matthew Alves-Hill:** They're tracking their conversions in, they're using HubSpot, they're using PostHog.

**Matthew Alves-Hill:** They mentioned that like GA4, they've been, her suspicion was that it also wasn't correct.

**Matthew Alves-Hill:** So it's a bit of a hot mess, to be honest.

**Matthew Alves-Hill:** I guess we don't really have like clear visibility. I don't think Looker is working correctly for us. It would be like tracking conversions for them.

**Matthew Alves-Hill:** I think like she's doing the lion's share of that work in HubSpot and PostHog.

**Matthew Alves-Hill:** So I guess number one, like, do you think, I think you mentioned that it's not really like an area that you're hot on in terms of GA4 and understanding whether things are actually firing correctly.

**Matthew Alves-Hill:** do think that needs to be like looked at.

**Matthew Alves-Hill:** It's over my head.

**Matthew Alves-Hill:** I don't really know what's going on in there.

**Matthew Alves-Hill:** didn't mean there's something I can raise with Suleiman or Birbeck, but I don't know whether there's anyone I can send.

**Matthew Alves-Hill:** Yeah.

**Matthew Alves-Hill:** Check here.

**Jakub Rudnik:** could probably even, I mean, use me as Suleiman to respond, but just like Kyle.

**Jakub Rudnik:** Kyle.

**Jakub Rudnik:** Would have a good experience here, like being on a growth team.

**Jakub Rudnik:** And you could even throw it to General, like, and see if anybody else that I don't know of has that.

**Jakub Rudnik:** But, like, he would be way more focused on this type of stuff, although it was probably other people doing it.

**Jakub Rudnik:** What I'm seeing here, like the screenshot I sent over, this is just the link that you sent in the internal.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** But no stream detected, no stream detected.

**Jakub Rudnik:** And so my understanding of this is, like, if there's no data for 28 days, and then I'd want to check, like, click phone, check this as a conversion over, like, six months and see if anything's there.

**Jakub Rudnik:** And then you would, like, because you're probably not, like, whitelisted, you would want to, like, do this conversion event on the site yourself and see if anything happens.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** Carmel's might be, but you can probably test this more formally.

**Jakub Rudnik:** Some of these, like, forms submit.

**Jakub Rudnik:** AI agent.

**Jakub Rudnik:** think this one's pretty new.

**Jakub Rudnik:** I would guess that there's, like, a chance that this is live.

**Jakub Rudnik:** And maybe some of these, like, I don't know.

**Jakub Rudnik:** But obviously, this many, they're either not useful, and then that's its own learning of, like, if it's set up and it's working, we can make one data point show up.

**Jakub Rudnik:** Then no way he's done this.

**Jakub Rudnik:** Like, we should figure out why and what we want them to be doing instead or whatever it is.

**Jakub Rudnik:** But, like, this one, form, submit, try for free, like, that almost feels like no way that this is...

**Jakub Rudnik:** Zero.

**Jakub Rudnik:** Like, it's either not set up properly or...

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** So that'd be my instincts on how to do it again a little bit.

**Jakub Rudnik:** GA4 is not my best software tool, but finding the report in here to explore each of these individually and then testing them.

**Jakub Rudnik:** You're, like, making the event happen and seeing what happens on the back end.

**Jakub Rudnik:** That's probably...

**Jakub Rudnik:** that will get you pretty close to answers.

**Jakub Rudnik:** They should be doing that when they set it up.

**Jakub Rudnik:** I don't know who set all these up for them, but I think they also work with like a web agency.

**Jakub Rudnik:** So I don't know how much of that is.

**Jakub Rudnik:** They were working with WebStacks, which is also one of our clients.

**Jakub Rudnik:** That's kind of why we know because we made the intro.

**Jakub Rudnik:** So I also ask like, are you still working with WebStacks?

**Jakub Rudnik:** Are they doing anything on the conversion analytics side?

**Jakub Rudnik:** I'm curious how these are set up.

**Jakub Rudnik:** If you can like get to the, who did this work?

**Jakub Rudnik:** And that could help too and why it's, they're missing.

**Jakub Rudnik:** You get lots of steps in here and going to some like Looker.

**Matthew Alves-Hill:** Could these have been like short-term like conversion events for like promotional?

**Matthew Alves-Hill:** Yeah, for sure.

**Jakub Rudnik:** For sure.

**Jakub Rudnik:** Or something could have changed like, you know, they're, yeah, they were put on like one page and then they like, they did make a website change.

**Jakub Rudnik:** And then that, you know, event is like tagged differently or they did just like, yeah.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** So this adds conversion, maybe that's set by an old, yeah, there's plenty of ways you're just like figuring out.

**Matthew Alves-Hill:** Yeah, it's a tricky one because it's like, clearly their reporting is not good and I'm not, we need some element of it to show our value, but I also don't want to go and like open up this whole new work stream with them that's like us going and trying to figure out like what's going on in all of their, conversion tracking, like it's a bit, it strikes me as a little bit like Cowboy on their side, between like Comel and like the rest of marketing, what's going on.

**Matthew Alves-Hill:** So I want to get like the minimum, but like what we're interested really is in like request a demo and try for free out of the organic channel.

**Matthew Alves-Hill:** I just need, really just need Looker to be tracking those accurately, but, and it seems that request a demo is

**Matthew Alves-Hill:** This is firing.

**Matthew Alves-Hill:** The other stuff is a little bit more.

**Matthew Alves-Hill:** And she's saying they had a really strong month, um, in November, but it's like, is this all it was?

**Jakub Rudnik:** Like they had two, four, seven demo requests.

**Jakub Rudnik:** Like that seems crazy.

**Jakub Rudnik:** I don't know if their other forms are.

**Jakub Rudnik:** Sometimes you can see in here, like, well, this actually is useful.

**Jakub Rudnik:** What's this?

**Jakub Rudnik:** They must have just been running ads.

**Jakub Rudnik:** Like point.

**Jakub Rudnik:** Like this one, like form, submit, try for free.

**Jakub Rudnik:** Uh, something, something changed on their site.

**Jakub Rudnik:** it.

**Jakub Rudnik:** Here, you can either change the button or the flow or something.

**Jakub Rudnik:** I guess agent as well will have the same.

**Matthew Alves-Hill:** Yeah, you register.

**Jakub Rudnik:** This one, like, there's no data before.

**Jakub Rudnik:** Let me just double check that.

**Matthew Alves-Hill:** Yeah, it looks like it's...

**Jakub Rudnik:** What the hell is this?

**Jakub Rudnik:** Sorry, I would have muted if I could have found it.

**Jakub Rudnik:** It's all good.

**Matthew Alves-Hill:** Yeah, like, this is, like, very clearly not a real thing.

**Jakub Rudnik:** I wish we would, like, hide these ones.

**Jakub Rudnik:** It don't matter.

**Matthew Alves-Hill:** Yeah, I'm wondering if there's actually a way to do that and just have the one.

**Matthew Alves-Hill:** Have, like, request a demo, try for free.

**Matthew Alves-Hill:** Like, that, those are the only two we're really...

**Matthew Alves-Hill:** Interesting, yeah, that's a bit of a mess.

**Matthew Alves-Hill:** Okay, what I'll do is dig a little bit more around the analytics.

**Jakub Rudnik:** Yeah, I would definitely ask them who set up the GA4 events and whether they have any documentation. That would be really helpful to understand what's going on.

**Matthew Alves-Hill:** I'll let you know what happens and if I need a little bit more help on this.

**Matthew Alves-Hill:** Okay.

**Matthew Alves-Hill:** Then the other thing is, so that's all on Seat.

**Matthew Alves-Hill:** think they're very happy.

**Matthew Alves-Hill:** I think it's interesting.

**Matthew Alves-Hill:** The tone seems to have changed because initially it was like, we need to convert, we need to convert, we need to convert.

**Matthew Alves-Hill:** And now they're going like, we love the two pages, like traffic's great.

**Matthew Alves-Hill:** I think the CMO is very impressed with the traffic.

**Matthew Alves-Hill:** So we're good there.

**Matthew Alves-Hill:** When I find time, I am going to start like a content audit of everything we've published for them and then probably recommend like in January that we start working back through all of those things because we publish a lot of random content on their preferred new topics, service desks, cetera.

**Matthew Alves-Hill:** But we published that a long time ago, and the messaging has fundamentally changed.

**Matthew Alves-Hill:** So it's a good time to do that.

**Matthew Alves-Hill:** So that's what's happening on Seed.

**Matthew Alves-Hill:** On Innerwell...

**Jakub Rudnik:** Pause really quickly.

**Jakub Rudnik:** Let's stay in touch on that, because it's on my list ticket-wise to also work through some of that.

**Jakub Rudnik:** And so obviously you're also taking a new client.

**Jakub Rudnik:** I'm probably going to start working on clients that aren't mine, too.

**Jakub Rudnik:** I don't know.

**Jakub Rudnik:** That hasn't happened yet.

**Jakub Rudnik:** But right now it looks like I have time for that, but I don't know how that'll change.

**Jakub Rudnik:** But either way, just keep me in the loop on if, when, et cetera.

**Jakub Rudnik:** So I may be able to get to some of that as well.

**Jakub Rudnik:** Yeah, it definitely makes sense.

**Matthew Alves-Hill:** They are fundamentally changed.

**Matthew Alves-Hill:** All of their new messaging is a good opportunity for us to go, hey, okay, we want to go refresh now, like a lot of this stuff.

**Matthew Alves-Hill:** And it makes it seem like we're not backtracking.

**Matthew Alves-Hill:** It's like actually going in and improving.

**Matthew Alves-Hill:** So I think...

**Matthew Alves-Hill:** there's a lot to do, I just really want to get Lawrence, I just need a consistent managing editor on the seat because, yeah, you've been crazy, it's been crazy, okay, let's see, so, in a well, good progress last week, herding cats, but eventually, like, pretty good.

**Matthew Alves-Hill:** The LDR is that the blogs are done, and all the state-level pages are done, because there's been so much, like, so many things flying around, I need to, I just wanted to send a check with you where we're at, because Akina's like, we need to wrap this project up, and as far as I understand now, the ball is in their court on the mental health page, because it doesn't make sense for us to go and redirect the mental health page.

**Matthew Alves-Hill:** until they've built a landing page, right?

**Jakub Rudnik:** I still think that's correct.

**Jakub Rudnik:** I mean, like, we can, but it'll just be worse.

**Jakub Rudnik:** You know what mean?

**Jakub Rudnik:** Like, the URL, that's how I would do it.

**Jakub Rudnik:** And they've known about that page for two months now.

**Matthew Alves-Hill:** Yeah, so we need a mental health landing page, and then we can go in and redirect all the mental health, state-level mental health.

**Jakub Rudnik:** And then we also have all those city-level that we thought were ketamine, but they're really mental health.

**Jakub Rudnik:** And they have ketamine URLs, but they're mental health pages.

**Jakub Rudnik:** Yes.

**Matthew Alves-Hill:** So that's, like, that's crazy.

**Matthew Alves-Hill:** I am a bit worried here about, like, how much...

**Matthew Alves-Hill:** Okay, wait, hang on.

**Matthew Alves-Hill:** So...

**Matthew Alves-Hill:** So...

**Matthew Alves-Hill:** So...

**Matthew Alves-Hill:** Yeah, okay, so we talked a little bit ago about the city-level ketamine pages, which we actually never created, as far as I can tell.

**Jakub Rudnik:** Yeah, I thought originally, because of the URL thing, that we had, like, 75% of them created.

**Jakub Rudnik:** You know, we would have to fill in some of the gaps, but obviously those are mental health and not ketamine, and that was a discovery midway through.

**Jakub Rudnik:** And they do have old, the availability versions of the ketamine pages that now have bad, like, not ideal URLs, because they're connected to the availability state-level ketamine pages.

**Jakub Rudnik:** The goal for me would be to either just, I don't, I mean, their dev bringing up, like, the workflows on how they use the ketamine, like, the availability pages, that's like a...

**Jakub Rudnik:** I think that nobody flagged before.

**Jakub Rudnik:** Maybe there is something wonky.

**Jakub Rudnik:** We could move just like all of their city level pages with this old URL structure over to the new structure.

**Jakub Rudnik:** I guess that's not ideal because then it's like a very different experience.

**Jakub Rudnik:** It's like, it's just wonky.

**Jakub Rudnik:** Or we can create city level pages that are similar to, it's like a combo of mental health city level plus ketamine page.

**Jakub Rudnik:** And we just like create one template and then spit out 200 programmatic that match the ones that already exist and then do the redirects.

**Jakub Rudnik:** I really don't have a sense of whether those pages need, what would go wrong if we just, if we just keep the city levels as is.

**Jakub Rudnik:** They were, they work better than the state level.

**Jakub Rudnik:** I think partly there's less competition there.

**Jakub Rudnik:** There's less, we didn't have two competing pages, but like they do get traffic to their city level pages to some extent.

**Jakub Rudnik:** So.

**Matthew Alves-Hill:** Keep the city level.

**Matthew Alves-Hill:** So, okay.

**Matthew Alves-Hill:** So redirect the city level ketamine pages.

**Matthew Alves-Hill:** So, yes, we've got availability.

**Matthew Alves-Hill:** So we've got the availability and then we've got the ketamine therapy as two separate city level pages.

**Matthew Alves-Hill:** these don't work anymore either.

**Jakub Rudnik:** Oh my God.

**Jakub Rudnik:** God.

**Matthew Alves-Hill:** Um, the, uh, yeah, I've somehow lost all of these.

**Matthew Alves-Hill:** Like that's broken right now.

**Jakub Rudnik:** And that they do not, they will not succeed the way that they do work.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** Yeah.

**Matthew Alves-Hill:** So, um, so the.

**Matthew Alves-Hill:** The, so if we look at batch 2.5, hang on, me show you a Sorry, I know we've been around this million times, but it's, it's difficult.

**Matthew Alves-Hill:** Okay, so right now we have, we have this, we created this batch 2.5, right?

**Matthew Alves-Hill:** Which is actually where we, where we realize that these ketamine therapy pages are actually mental health.

**Matthew Alves-Hill:** City level, but what you're saying is that they're performing well for the ketamine city level, like, keyword.

**Jakub Rudnik:** No, the thing I just sent in the chat, the availability city levels, there is some traffic there.

**Jakub Rudnik:** Let's see if I can tell how much.

**Matthew Alves-Hill:** Okay, so that's the batch 3, availability.

**Matthew Alves-Hill:** Yeah, we just, their availability.

**Matthew Alves-Hill:** Except that there are availability pages.

**Jakub Rudnik:** Those work well.

**Jakub Rudnik:** Those should go there.

**Jakub Rudnik:** then where the decision to make really is do we want to create a new page type, like structure, for those ketamine or just move the availabilities over because they're now kind of stranded.

**Jakub Rudnik:** Okay, so mental health average.

**Matthew Alves-Hill:** Okay, so just to understand, so this corresponding one.

**Matthew Alves-Hill:** Oh, I don't know where these have gone now.

**Matthew Alves-Hill:** Someone's like removed these.

**Matthew Alves-Hill:** I've read, so this one, I don't know where these have gone, it's really annoying.

**Matthew Alves-Hill:** So that, so the point here is that like redirect this URL to, so this one and this one to, that, no, the, you're okay, you're okay, it's, this is the worst project we've ever had.

**Jakub Rudnik:** Go back.

**Jakub Rudnik:** Yeah, can do it, I can do it.

**Jakub Rudnik:** Yeah, the worst, one of the worst parts is that these ketamine 2.5 mental healths are labeled ketamine therapy, but they're mental.

**Jakub Rudnik:** Well, so this should say mental health Marietta, and this should go once we have the mental health page, then we'll be able to move the California pages, the California page here.

**Jakub Rudnik:** And then this page is a mental health page that should just be moved under the mental health umbrella for the city.

**Matthew Alves-Hill:** Yeah.

**Jakub Rudnik:** So there are ketamine pages, availability ketamines, anything availability is their creation.

**Jakub Rudnik:** These pages do exist.

**Jakub Rudnik:** They should go under this ketamine structure here.

**Jakub Rudnik:** So So So

**Jakub Rudnik:** Same kind of concept.

**Jakub Rudnik:** They did not have availability for mental health.

**Jakub Rudnik:** I think that's one of the things that trips us up.

**Jakub Rudnik:** We made the availabilities for mental health, but we also named them the wrong thing.

**Jakub Rudnik:** Or they did.

**Jakub Rudnik:** I don't know how that worked.

**Matthew Alves-Hill:** hell.

**Jakub Rudnik:** So this one has Proketamine Cities only has their page availabilities.

**Jakub Rudnik:** Mental health only has ours, but they're named Ketamine.

**Jakub Rudnik:** terrible.

**Jakub Rudnik:** These pages, let me actually share my window.

**Jakub Rudnik:** That's the tab.

**Jakub Rudnik:** This page, I think because of what they just did right now, are all doing 500 server errors.

**Jakub Rudnik:** They don't do anything right now because they're all broken.

**Jakub Rudnik:** 22 impressions, one click a day.

**Jakub Rudnik:** Veil is one that I just found.

**Jakub Rudnik:** We're still showing up top 10.

**Jakub Rudnik:** They were getting top 10 on a lot of these cities.

**Jakub Rudnik:** But they're broken.

**Jakub Rudnik:** So now Google's like punishing them, obviously.

**Jakub Rudnik:** Three months, you can see this a little bit better.

**Jakub Rudnik:** Yeah, it's all good.

**Jakub Rudnik:** Then they like, all the pages broke.

**Jakub Rudnik:** So the question for me, can these be turned back on?

**Jakub Rudnik:** Why does everything just keep going 500 error?

**Jakub Rudnik:** Not good.

**Jakub Rudnik:** And then, and I would want them to do that in the short term.

**Jakub Rudnik:** The next step thing is like, these availability pages, we can't see them, but they had that like availability module with like the.

**Jakub Rudnik:** Yeah, yeah.

**Jakub Rudnik:** I don't love this, but the short term is like, if you can turn these back on, at least like something's happening.

**Jakub Rudnik:** As long as like nothing is terrible from a user experience, I would rather just turn these back on, redirect them.

**Jakub Rudnik:** Probably add, let's see what these look like right now.

**Jakub Rudnik:** Are the ketamines still?

**Jakub Rudnik:** Are they still like this?

**Jakub Rudnik:** is able to find

**Jakub Rudnik:** Okay.

**Jakub Rudnik:** Oh, this one.

**Jakub Rudnik:** That's not good.

**Jakub Rudnik:** Oh, that's just...

**Jakub Rudnik:** Those are paid...

**Jakub Rudnik:** Okay.

**Matthew Alves-Hill:** This is what Israel completed on Friday.

**Matthew Alves-Hill:** Okay, that makes sense.

**Jakub Rudnik:** I clicked something that didn't exist yet.

**Jakub Rudnik:** Oh, and this exists here.

**Jakub Rudnik:** So Ketamine, Connecticut.

**Jakub Rudnik:** The big thing with, like, the availabilities, which I can't show you because they're 500-ing, but they would have a different...

**Jakub Rudnik:** We would need to make sure the cookies, or not the cookies, the breadcrumbs are updated properly.

**Jakub Rudnik:** And then we need to make sure the availability portion doesn't break anything.

**Jakub Rudnik:** But otherwise, assuming those two things, turn these back on, make, like, all they...

**Jakub Rudnik:** Like, this is the result of them being broken.

**Jakub Rudnik:** They don't work.

**Jakub Rudnik:** So we want to get anything we can back there.

**Jakub Rudnik:** And then, assuming those two other things, I would redirect each of them.

**Jakub Rudnik:** them.

**Jakub Rudnik:** And

**Jakub Rudnik:** Over to the new Ketamine version, and make sure breadcrumbs and availability modules both work.

**Jakub Rudnik:** Then they're here.

**Jakub Rudnik:** Then longer term, should that availability version of the Ketamine city-level page, should it look more like this page?

**Jakub Rudnik:** This page, right.

**Jakub Rudnik:** one that we designed, the mental health page, because it's going to be the only thing that has the old availability, styling, setup, etc.

**Jakub Rudnik:** They didn't, they were like working like okay SEO-wise, but everything we created is better SEO-wise.

**Jakub Rudnik:** But I think the availability has like conversion impact and stuff.

**Jakub Rudnik:** So that's where we were trying to like merge the two things.

**Jakub Rudnik:** Like let's take our formatting, add the availability module, redirect two sets of things.

**Jakub Rudnik:** Again, mental health has our pages only.

**Jakub Rudnik:** Ketamine has their pages only.

**Jakub Rudnik:** Mental health pages are named improperly.

**Jakub Rudnik:** So again, don't worry about like not like tracking all of it.

**Jakub Rudnik:** I have to like, go through it every time too.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** Okay.

**Jakub Rudnik:** Okay.

**Matthew Alves-Hill:** So, so essentially what we need to do now is, I don't know where all these URLs have gone.

**Jakub Rudnik:** These ones, I think what happened was like, we, okay, this, yeah, this is what happened.

**Jakub Rudnik:** So we, because we thought these were the new, these are the new ketamine URLs, but we thought that these were ketamine URLs.

**Jakub Rudnik:** So this list and this list were next to each other and mapped, but because it wasn't the same page type, the ketamines are actually mental health.

**Jakub Rudnik:** We split them up and we need to go find these basically.

**Jakub Rudnik:** And what we've done on mental health, I don't think is going to be a one-to-one map.

**Jakub Rudnik:** Like they had different lists that we did or something like that.

**Jakub Rudnik:** That's where we thought that we were going to have to create a few more ketamine pages, but it was going to be close.

**Jakub Rudnik:** So then, well, have to, we, they may have it somewhere, but like you can get a D.

**Jakub Rudnik:** Where did they?

**Jakub Rudnik:** I actually think they sent it somewhere.

**Matthew Alves-Hill:** All of the URLs for this.

**Matthew Alves-Hill:** Yeah, yeah, yeah.

**Jakub Rudnik:** Sorry, didn't know we're along, but...

**Jakub Rudnik:** No, no, this is, like, crucial.

**Matthew Alves-Hill:** I think it's somewhere in here.

**Jakub Rudnik:** Thank you.

**Jakub Rudnik:** So I don't see the URL, but I think this is their list.

**Jakub Rudnik:** It's probably their list.

**Jakub Rudnik:** You could probably use GPT to identify these.

**Jakub Rudnik:** I can't.

**Matthew Alves-Hill:** I mean, to be fair, I can probably just ask GPT to, like, just take that one example that's in there and then convert all the others.

**Jakub Rudnik:** Yeah, you basically need to pull state and city and recreate this URL format.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** And then...

**Jakub Rudnik:** Yeah, like, I could probably give you the whole new URL column and say, like...

**Matthew Alves-Hill:** Format it in this format.

**Matthew Alves-Hill:** Yeah.

**Jakub Rudnik:** The problem, right?

**Jakub Rudnik:** The two problems are, the biggest problem is identifying what exists from their availability standpoint.

**Jakub Rudnik:** I think that's here, and you could give ChatGPT this example and say, "this is the format, find all the city-level URLs like this."

**Jakub Rudnik:** Go find them with the state and city from this page, city-level content one, that's at the bottom of the technical SEO document, and populate the list, and then the second step after that is take that list and put it in this new URL.

**Jakub Rudnik:** Format, and then put them side by side, and then just do those redirects.

**Jakub Rudnik:** But again, these all need to be turned back on.

**Jakub Rudnik:** They're all broken right now.

**Matthew Alves-Hill:** So turn on all these availability pages back on, and then redirect them all to this format on the right.

**Jakub Rudnik:** Yes, while also ensuring that the breadcrumbs are updated to the new format.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** They're going to have availability, and you'll create a redirection.

**Jakub Rudnik:** Loop, and then whatever they were worried about with the availability module, we just need to check that out and figure out what that is and if it is a real problem.

**Jakub Rudnik:** What happens?

**Jakub Rudnik:** It's off.

**Matthew Alves-Hill:** Do you have any context on why they would have done that?

**Jakub Rudnik:** It seemed like they're running ads to those availability pages and then something about like you go to a state and they drop down a city or something like that.

**Jakub Rudnik:** Again, I can't reproduce these because I can't see the fricking page, but something was happening there.

**Jakub Rudnik:** But again, like they've had a 404 on, no, that's not, they've had a 500 on these for weeks and they like don't even notice.

**Jakub Rudnik:** So that's what's crazy.

**Jakub Rudnik:** It's like, you're going to delay this.

**Jakub Rudnik:** You've broken your pages and your business isn't even aware of this.

**Jakub Rudnik:** So, okay.

**Jakub Rudnik:** Okay.

**Matthew Alves-Hill:** And then like the navigation on the site needs to be addressed because you can put the, so.

**Matthew Alves-Hill:** Yeah.

**Jakub Rudnik:** All these need, like right now, need to be updated to the new URL format that's been set up that is correct.

**Jakub Rudnik:** That's a minimum, because right now you're opening into this.

**Jakub Rudnik:** Is that redirect?

**Jakub Rudnik:** Yeah, it's still the availability, if you can see in the bottom left there.

**Jakub Rudnik:** And so then they do redirect, but you just have that.

**Jakub Rudnik:** And then what I would say is like, I still have been recommending all the index pages should replace this module.

**Jakub Rudnik:** And it should say like, find kidney treatment near me.

**Jakub Rudnik:** And that's the single URL.

**Jakub Rudnik:** And then it takes you to a page that looks like this.

**Jakub Rudnik:** Yes.

**Jakub Rudnik:** It's linked to the correct URLs.

**Jakub Rudnik:** And under each of these is like a dropdown that has the individual cities.

**Jakub Rudnik:** But those cities aren't correct.

**Matthew Alves-Hill:** Yeah, because there's no, like, there's no nav on the site to get to the city level page.

**Matthew Alves-Hill:** Correct.

**Matthew Alves-Hill:** So you could put, so we can put the, we can set up the availability pages so that they are folded correctly with the redirects and has the breadcrumb, like, through.

**Matthew Alves-Hill:** But there's still, we still need to fix the navigation of the site.

**Matthew Alves-Hill:** And what we do by that is this, these 50 states, or however many there are, they need to be on hellonrl.com forward slash ketamine.

**Matthew Alves-Hill:** It needs to live there.

**Matthew Alves-Hill:** And then you click through.

**Jakub Rudnik:** Yes, it doesn't need.

**Matthew Alves-Hill:** Yeah, so, so would the index live here, actually?

**Matthew Alves-Hill:** I think it's actually a separate page.

**Jakub Rudnik:** I mean, they could do, they should do it here, too.

**Jakub Rudnik:** There should.

**Jakub Rudnik:** be like a, what states do you offer it in?

**Jakub Rudnik:** And it opens up or something like that.

**Jakub Rudnik:** That's probably a good way.

**Jakub Rudnik:** But I've got like, I would link to a, there's going be a new page that's ketamine near me.

**Jakub Rudnik:** Ketamine therapy near me.

**Jakub Rudnik:** And that page is what we'll link down here.

**Jakub Rudnik:** So you have like, you still have your ketamine should be up here.

**Jakub Rudnik:** It should probably also be down here somewhere.

**Jakub Rudnik:** But like, we can't even get them to do anything.

**Jakub Rudnik:** And then this should be a ketamine near me page that's separate.

**Jakub Rudnik:** And it's just the locations.

**Matthew Alves-Hill:** Ketamine near me, it takes them to a separate page.

**Matthew Alves-Hill:** It's basically a directory.

**Matthew Alves-Hill:** And then once they click on a state, it takes them back into the correct subfoldering.

**Matthew Alves-Hill:** And then the breadcrumbs apply and it works down to city level.

**Matthew Alves-Hill:** You got it.

**Matthew Alves-Hill:** Yep.

**Jakub Rudnik:** Okay.

**Matthew Alves-Hill:** So this is great.

**Matthew Alves-Hill:** This is what I will.

**Matthew Alves-Hill:** So two things.

**Matthew Alves-Hill:** So bowl in inner Wells court right now.

**Matthew Alves-Hill:** Give us a mental health.

**Matthew Alves-Hill:** Landing page, turn all these availability pages back on, please.

**Matthew Alves-Hill:** Then we will go and redirect all the availability pages to the correct couldering, add the breadcrumbs, and we can also redirect the mental health pages in batch two, but we need the landing page.

**Matthew Alves-Hill:** There is definitely, clearly, like, Akina is probably under pressure a little bit to get this wrapped up, or she's, I don't know, actually.

**Matthew Alves-Hill:** I don't know if anyone's under pressure at NLW, to be honest, it seems like.

**Jakub Rudnik:** She seemed like she was under pressure the last one I joined, when she said, like, they're asking us to finish this up now.

**Jakub Rudnik:** Can we do this?

**Jakub Rudnik:** It's like, that's the first time I've heard her in six months have pressure.

**Matthew Alves-Hill:** Yeah, I mean, I think all, I think that's what I was, that's why I was, like, very, I guess, aggressive last week on, like, pushing things through to get things done, because they're, like, I definitely.

**Matthew Alves-Hill:** I worry that we get caught in a crossfire here because we're moving as quickly as we can, but they are messing things up.

**Jakub Rudnik:** 100%.

**Jakub Rudnik:** 100%.

**Jakub Rudnik:** You're completely correct to be worried.

**Matthew Alves-Hill:** So that's like, I don't know if it's a flag, whatever, but that's definitely like a situation that like our POC is not moving things on their side.

**Matthew Alves-Hill:** We're doing everything we can, but yeah, I mean, like, I don't know what's going on.

**Matthew Alves-Hill:** Like, it's clearly nothing's been communicated to Ilya.

**Matthew Alves-Hill:** Then they pulled in some, like, I guess the head of dev who's like never even been mentioned in the discussions at all.

**Matthew Alves-Hill:** Like, doesn't really know what's going on.

**Matthew Alves-Hill:** But yeah, mean, the redirect, like she's saying, finish up this project, but I'm like, I'm just going to say, this is what you need to do now.

**Matthew Alves-Hill:** Move as quickly as you can.

**Matthew Alves-Hill:** Yeah.

**Jakub Rudnik:** mean, it's got to be like.

**Jakub Rudnik:** Laid out in that channel, because there's more visibility for other folks, because we do it every call.

**Jakub Rudnik:** it's like Monday, it's like things we're waiting for Interwell.

**Jakub Rudnik:** Create this, create this, create this, create this.

**Jakub Rudnik:** And just like, it's probably like that.

**Jakub Rudnik:** And then we meet on Wednesday, and then on Friday, you check in and be like, any update to this, this, or this?

**Jakub Rudnik:** And you just keep doing that every week, and that's what you can control on our side.

**Jakub Rudnik:** I'm, I mean, one, they were like our least happy client for a while.

**Jakub Rudnik:** We've like gotten them back, and we've done a great, like, everyone's very happy with where they've gotten to.

**Jakub Rudnik:** And now, I've definitely mentioned every time we have one of these, like, client status calls, like, they're still on the shoot.

**Jakub Rudnik:** They're not moving forward.

**Jakub Rudnik:** And I've given them, I flagged and lowered their scores because POC is now, seems to have pressure.

**Jakub Rudnik:** They're not moving anything forward.

**Jakub Rudnik:** So everyone's aware of this.

**Jakub Rudnik:** They know it's the POC.

**Jakub Rudnik:** I think if you do those posts — Monday and Friday — very clear, that goes a long way.

**Jakub Rudnik:** You know, don't pull any punches.

**Jakub Rudnik:** Noah is hopefully seeing this and whoever's Noah's boss right now.

**Jakub Rudnik:** And from there, like, that's all you can do.

**Jakub Rudnik:** They're not like our ICP anymore.

**Jakub Rudnik:** Like we've, I mean, whatever, that kind of shifts over time.

**Jakub Rudnik:** But like, we don't want to lose them, certainly, but there's only so much we can do.

**Jakub Rudnik:** We've done so much extra work.

**Jakub Rudnik:** They're the biggest pain in our side.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** And it's like, so many things have been off about this for a long time.

**Jakub Rudnik:** They're like, one of the clients we talk about won't like why we change things and why we turn down clients now and so on.

**Jakub Rudnik:** So it's like, it wouldn't, it's, it's annoying things are like, there's only so much you can do in there.

**Jakub Rudnik:** We shouldn't continue.

**Jakub Rudnik:** Like, you just have to.

**Matthew Alves-Hill:** It's annoying because like the, like the editorial now is in like such an like easy place that it's like right in the wheelhouse.

**Matthew Alves-Hill:** Actually, like I know they're not like, editorial strategy is like.

**Matthew Alves-Hill:** We could run, like, there's a year's worth of roadmap there easily.

**Matthew Alves-Hill:** It's just the redirects that, like, I don't know.

**Matthew Alves-Hill:** I do think that we have good rapport with Noah because it seems like she joined at the same time that we started, like, pulling finger and getting things, like, moving.

**Matthew Alves-Hill:** So I'm hoping that, I think it's a good call.

**Matthew Alves-Hill:** I'll make it much clearer in the external channel so that Noah's, like, oh, these guys are working their  off.

**Matthew Alves-Hill:** And actually, maybe there's, like, other problems, not them.

**Matthew Alves-Hill:** But I think it has also been, like, quite clear.

**Matthew Alves-Hill:** We've been very active there.

**Matthew Alves-Hill:** So, okay.

**Jakub Rudnik:** I agree.

**Jakub Rudnik:** I think that's, like, the last thing you can do.

**Jakub Rudnik:** And then we have a good, you set up a really good editorial.

**Jakub Rudnik:** I think they know that.

**Jakub Rudnik:** They were happy with this.

**Jakub Rudnik:** I think even the technical, like, it's been, it is a mess.

**Jakub Rudnik:** But that's, like, mostly whatever.

**Jakub Rudnik:** We've worked through it.

**Jakub Rudnik:** We've given them a clear roadmap and they just haven't executed.

**Jakub Rudnik:** The editorial is growing, whatever.

**Jakub Rudnik:** But yeah, make those things clear, then that's what you can do, and we've got a plan, so.

**Matthew Alves-Hill:** And then just one more, on these, like, on these, like, city-level pages that we've actually, we've called them ketamine therapy, but they're actually mental health.

**Matthew Alves-Hill:** So we do the, we get the mental health landing page built, we redirect that batch to, like, as we've done for ketamine, so there's mental health dash state.

**Matthew Alves-Hill:** And then we redirect all those ketamine therapy, ketamine therapy pages, actually, to the mental health.

**Matthew Alves-Hill:** It's the same way, but then the elephant in the room is, like, those will look nice, that's what we want the city-level ketamine therapy pages to look like, but we're going to have to go and build those out, because we never, we never did that.

**Matthew Alves-Hill:** So that's, like, a PSEO thing down the line.

**Matthew Alves-Hill:** For now, ketamine therapy at city level will just look like these little availability.

**Jakub Rudnik:** Yeah, and, like, we want to do that, but there's a lot of prior, like, let's get everything else.

**Jakub Rudnik:** Before we go try to launch 200 more pages on top of these things.

**Jakub Rudnik:** That will be like a V2 or V3.

**Jakub Rudnik:** Yeah, 100%.

**Matthew Alves-Hill:** Okay, that was super, super helpful.

**Matthew Alves-Hill:** Okay, good.

**Jakub Rudnik:** Cool.

**Jakub Rudnik:** Let me know if you need it.

**Jakub Rudnik:** Do you need any calls you want me on or would be useful for me to be on this week?

**Matthew Alves-Hill:** I don't know.

**Matthew Alves-Hill:** Let me see how I go with...

**Matthew Alves-Hill:** I need to prep for seat and then it might be like...

**Matthew Alves-Hill:** I think it could be helpful depending on what I dig up on like the analytics front because it is just like a little bit of a gap for me.

**Matthew Alves-Hill:** And if she is asking some of those questions, it might be handy.

**Matthew Alves-Hill:** But I've given her a performance.

**Matthew Alves-Hill:** I gave her like a big performance review last week.

**Matthew Alves-Hill:** So now I just want to like...

**Matthew Alves-Hill:** I've said like we're just heads down on production.

**Matthew Alves-Hill:** So I actually might not even broach the topic until I can dig into some more things.

**Matthew Alves-Hill:** I'll let you know.

**Matthew Alves-Hill:** I think let's see.

**Matthew Alves-Hill:** I'll keep you posted on in a while.

**Matthew Alves-Hill:** while.

**Matthew Alves-Hill:** keep posted on I'll I'll I'll keep I'll while.

**Matthew Alves-Hill:** um

**Matthew Alves-Hill:** Let's see how we go up until Wednesday, because if she's like, if we're getting comms, it's like, why is it taking so long or whatever, then it might be handy.

**Matthew Alves-Hill:** But I think the other ones, no, the other ones are fine.

**Jakub Rudnik:** I'll decline tavern.

**Jakub Rudnik:** I'll keep seat and interval on.

**Jakub Rudnik:** Just let me know.

**Jakub Rudnik:** By Wednesday, no problem.

**Jakub Rudnik:** Yeah, that's all fine.

**Jakub Rudnik:** Yeah, and home bases.

**Jakub Rudnik:** Oh, home base.

**Jakub Rudnik:** Are they done?

**Matthew Alves-Hill:** Yeah, we got, like, we gave them 10 questions in articles last week, and Sonia said they look great, so now we're just going to ramp those.

**Matthew Alves-Hill:** And they are waiting on, like, this audit that you said you'd do, but I know it's like, this is like a scope problem.

**Jakub Rudnik:** I sent them the audit.

**Jakub Rudnik:** Oh, did you?

**Jakub Rudnik:** Okay.

**Matthew Alves-Hill:** Yeah, I sent them a video with...

**Jakub Rudnik:** Yes, I remember now.

**Matthew Alves-Hill:** Sorry.

**Matthew Alves-Hill:** Very good.

**Matthew Alves-Hill:** Yeah, there's a refresh sheet, a loom.

**Jakub Rudnik:** Yeah, nobody else said anything.

**Matthew Alves-Hill:** If they mention that, then we can talk about that.

**Matthew Alves-Hill:** If not, I'm just going to do 10 question center articles a week until they ramp off.

**Matthew Alves-Hill:** I don't know what's happening at a high level with the account.

**Jakub Rudnik:** That's all it is.

**Jakub Rudnik:** We accepted a one-month severance, I believe.

**Jakub Rudnik:** Okay, cool.

**Matthew Alves-Hill:** I'll forward you to that.

**Matthew Alves-Hill:** Cool.

**Matthew Alves-Hill:** All right, Jakub.

**Matthew Alves-Hill:** Welcome back.

**Jakub Rudnik:** Thank you.

**Matthew Alves-Hill:** Bye.

**Matthew Alves-Hill:** Bye.
