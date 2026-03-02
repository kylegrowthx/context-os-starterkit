# Anything <> Growth X

<metadata>
date: 2026-01-13
time: 22:00 UTC
duration: 50 minutes
organizer: erik@growthx.ai
participants: Dhruv Amin (Anything), Kyle Gaudreau (GrowthX), Katya Luscomb (GrowthX), Erik O'Brien (GrowthX)
fathom_recording_id: 114030090
fathom_url: https://fathom.video/calls/531442930
share_url: https://fathom.video/share/RTn_DbzdAdjWXq4cMMn92y54oAxjPofx
source: fathom
enriched_on: 2026-02-28T14:32:05 UTC
</metadata>

---

## Summary

Reset SEO strategy to accelerate revenue impact and align on performance metrics.

---

## Context

Dhruv Amin (Anything founder) escalated concerns about SEO performance two months into the engagement. Current traffic (~280 sessions/week) is not on track to meet a 6-month payback period target, creating urgency to pivot strategy. The initial plan was to build editorial authority before launching programmatic SEO, but this timeline was never anchored to revenue goals. Anything.com has low domain authority (unlike create.xyz at DA 46), slowing ranking velocity. GrowthX (led by Kyle) brought in a strategy team to reset alignment, establish revenue-focused measurement, and deliver 6-month traffic/revenue projections to guide the path forward.

---

## Relevance

- **Client Escalation:** A key client (Anything) surfaced critical misalignment on strategy, pace, and measurement—a teachable moment for GrowthX's engagement process.
- **Revenue Anchor:** Demonstrates the importance of tying SEO projections to actual revenue (not just traffic) from day one. Anything's funnel metrics (25% visit-to-signup, 3% free-to-paid, 95% conversions in first session) are now the north star.
- **Domain Authority Bottleneck:** Classic SEO challenge—low domain authority slows ranking velocity. The decision to test publishing on create.xyz (DA 46) with 301 redirects to anything.com is a creative workaround for faster impact.
- **Activation & Segment Focus:** High-value insight: Anything Max ($200/month tier) drives 50%+ of revenue. Content should target entrepreneurs (10%+ F2P), consultants, and leadership—not broad audiences.
- **Programmatic SEO Path:** Moves PSEO from vague "future play" to concrete near-term action, balancing speed-to-impact against authority-building.
- **Mobile App Opportunity:** Anything is now 2x larger than competitors in mobile app coding. Underserved content opportunity around app design, app store submission, and mobile business models.

---

## Overview

- **Urgency:** The current SEO pace is too slow to meet the 6-month payback period goal. The focus must shift from traffic to direct revenue.
- **New Strategy:** A programmatic SEO (PSEO) play is now the primary path to revenue. The team will build its foundation while continuing editorial content.
- **Domain Pivot:** The team will test publishing content on `create.xyz` (DA 46) to leverage its authority for faster ranking, potentially replacing the `anything.com` canonical strategy.
- **Measurement:** Kyle will build a 6-month revenue projection and a PostHog dashboard to track SEO-driven revenue, using the new Google Search Console access for `anything.com`.

---

## Key Topics

### Performance Gap & Urgency

  - Dhruv flagged that current SEO performance is not on track to meet the 6-month payback period goal.
  - The team needs a clear path to scale that connects directly to revenue, not just traffic.
  - The current publishing pace (5 articles/week) is insufficient for meaningful impact.
  - **Key Question:** How much of the initial topic cluster search opportunity has been captured, and what is the timeline to reach the target?

### New Strategy: Programmatic SEO (PSEO)

  - PSEO is now the primary strategy to accelerate revenue impact.
  - **Rationale:** While PSEO takes longer to launch, it scales faster once live. The team will build its foundation in parallel with editorial content.
  - **Strategic Shift:** The initial plan focused on editorial content to build authority *before* PSEO. This timeline was not anchored to revenue goals, creating the current urgency.

### Domain Strategy Pivot

  - **Problem:** `anything.com` has low domain authority, hindering new content from ranking quickly.
  - **Proposed Solution:** Publish new content on `create.xyz` (DA 46) to leverage its authority for faster ranking.
  - **Implementation:** Use 301 redirects from `create.xyz/blog` to `anything.com/blog` to consolidate authority on the target domain over time.
  - **Decision:** Kyle will analyze this pivot's impact on projections. The current canonical strategy remains active for now.

### Revenue Measurement & Tracking

  - **Goal:** Track SEO-driven revenue, not just traffic.
  - **PostHog Setup:**
      - **Data Source:** Segment pipes all events to PostHog.
      - **Revenue Event:** `subscription start or upgrade` (fires on Stripe checkout return).
      - **Attribution:** Use the `initial referring domain` property to filter for Google traffic.
  - **Key Funnel Metrics:**
      - Homepage visit → Signup: \~25%
      - Signup → Paid: \~3% (95% of conversions happen in the first session)
      - Publish Rate: 20–30% (a key activation signal)
  - **Target User Segments (High F2P Conversion):**
      - Entrepreneurs (10%+ F2P)
      - Consultants
      - Leadership

### Product & Content Updates

  - **Anything Max:** The $200/month tier drives 50%+ of revenue.
      - **Opportunity:** Create content targeting this high-value audience (e.g., "browser use" or "dev agency alternatives").
  - **Mobile App Focus:** Anything is now a leader in mobile app coding.
      - **Opportunity:** Create content on underserved topics like app store submission, design tips, and mobile app business models.

---

## Action Items

**Kyle Gaudreau (GrowthX)**
- Validate canonical/publishing strategy; send recommendation to Dhruv (Anything) this week
- Build 6-month traffic projection incl. Google Search Console data; share with Dhruv (Anything) & Katya (GrowthX)
- Audit PostHog/Segment tracking setup; propose measurement/activation proxies to Dhruv (Anything)

---

## Transcript
**Katya Luscomb:** Hey, hey, Erik.

**Katya Luscomb:** Hey, Kyle.

**Kyle Gaudreau:** Hello.

**Katya Luscomb:** I just, I sent a ping in R's.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Yeah, I just, I think he updated it since I sent a note.

**Katya Luscomb:** Looks like it, which is great.

**Kyle Gaudreau:** Yeah, it's awesome.

**Kyle Gaudreau:** I think the way they have it set up is, makes it faster to instrument certain things.

**Kyle Gaudreau:** It has its pros and cons of sometimes, like, probably customization, what you want to have happen on one domain.

**Kyle Gaudreau:** But good to get things live quickly, it looks like, which is great.

**Kyle Gaudreau:** Totally.

**Kyle Gaudreau:** Let me just check it live just to see if any other issues have come up.

**Kyle Gaudreau:** Thank you.

**Kyle Gaudreau:** It looks like it's good.

**Katya Luscomb:** Sweet.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** I haven't checked yet that we just want to ideally avoid for now, although, I don't know, it's...

**Kyle Gaudreau:** It's probably best to avoid for now is the, yeah, just the canonicals on the homepages, especially, so it looks like on CreateXYZ, the canonical on that home page is currently canonical to the CreateAnything home page.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Oh, hey.

**Katya Luscomb:** Hey, hey.

**Kyle Gaudreau:** How are we doing?

**Katya Luscomb:** Good, how are Good.

**Katya Luscomb:** Thanks for, I was going to say, yeah, thanks for making the time to connect kind of last minute.

**Katya Luscomb:** Appreciate you being willing to hop on today and chat through some stuff.

**Dhruv Amin:** Yep.

**Katya Luscomb:** Yeah, to start us off, just wanted to reiterate that, you know, we heard your concerns definitely on board to make sure that we are looking at all the different avenues to ensure that we're working

**Katya Luscomb:** Scaling and working towards, you know, key growth goals, making sure that we're executing quickly.

**Katya Luscomb:** And so really wanted to focus this conversation today on like key actions that we need to take and alignment between all of us as a team to, you know, help move that needle forward effectively and efficiently.

**Katya Luscomb:** So any questions before I jump in off the top of your mind?

**Dhruv Amin:** Um, no, just for context, Erik, it feels like we're like behind.

**Dhruv Amin:** Um, and so we're just comparing, like, I don't know, just in terms of like, what's the payback period and we're trying to hit the first six months.

**Dhruv Amin:** Um, and like, what do we need to like do to kind of get to a scale that actually like moves the needle, um, relatively to the investment, like investment.

**Dhruv Amin:** So I think when I was looking at like the, the recent performance, I think the biggest thing that concern.

**Dhruv Amin:** I mean, was like, it felt like we're, I don't know, the framing that we're on track, but it feels like we're nowhere near a level of scale or, I don't know, like whatever we need to do to hit like requisite scale to actually like be meaningful from like a revenue perspective or even from like a raw traffic perspective.

**Dhruv Amin:** So I think that's the biggest like thing.

**Dhruv Amin:** So like some of these basic, you know, quick, quick access things I can, I can definitely do today and give you this.

**Dhruv Amin:** On Canonicals, we'll, yeah, it's already up and running.

**Dhruv Amin:** I think the, on some of these questions, like I can run you through the post hoc, can run you through this, like we can get the sanity publishing thing up.

**Dhruv Amin:** Up to date, but I'm like curious, like, like, I feel like if we just continue on, on the current pace of like we're doing five articles, a, or I don't know, five articles a week.

**Dhruv Amin:** And we just keep publishing.

**Dhruv Amin:** I'm not seeing the path to like, what do we expect to hit by what timeframe that actually ends up making this like a meaningful channel in the requisite time.

**Dhruv Amin:** So that's the overall context.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** And just to level set on like how our team is organized here, just to make sure we're on the same page.

**Kyle Gaudreau:** So Erik was your initial engagement manager through the Strategy Sprint.

**Kyle Gaudreau:** And I brought him along just to ensure that he, any, you know, I know we had some communication challenges that we kind of had highlighted here.

**Kyle Gaudreau:** So bringing him into the mix to make sure we can accelerate just, you know, any potential like miscommunications, just get on the right path.

**Kyle Gaudreau:** So think of Katya and Erik, peers, working on different life cycles of how we work at GrowthX.

**Kyle Gaudreau:** Myself, I lead our strategy team brought on to these kind of situations.

**Kyle Gaudreau:** to help us get through sticky situations, reset strategy, whatever it may be.

**Kyle Gaudreau:** Definitely hear you loud and clear on like, how can we get more visibility into the, where are we at?

**Kyle Gaudreau:** What's the plan?

**Kyle Gaudreau:** What's the trajectory?

**Kyle Gaudreau:** Are we aligned on this?

**Kyle Gaudreau:** So currently what we have now is just like, how can we, one, make sure we have some of the right foundational pieces in place, just, you know, alignment on some of the new insights on the migration strategy.

**Kyle Gaudreau:** Two, how can we make sure we have clear sense of how you measure success so we can appropriately factor that into answering that question with the right urgency that you have connecting to revenue ultimately.

**Kyle Gaudreau:** And then three, in parallel, which we're working on currently, looking at a projection that can break this down into the next six months of where do we, in our current case, where does that take us?

**Kyle Gaudreau:** What are scenarios on top of that?

**Kyle Gaudreau:** And how does that inform, based off our alignment, what we're

**Kyle Gaudreau:** We may need to adapt in our plan to make sure we're all feeling good to getting you to, ultimately, think you framed it in the sense of, like, are we on the path of, like, a 2 to 3x channel?

**Kyle Gaudreau:** And so we're trying to do a lot of this in parallel at the moment, trying to meet that urgency.

**Kyle Gaudreau:** So I don't want, hopefully, it to feel like for you that we didn't hear that element of it.

**Kyle Gaudreau:** We're trying to address some of the foundational things first, some of that, which can also inform that work.

**Kyle Gaudreau:** But that's just a quick update on that element.

**Dhruv Amin:** Okay, cool.

**Dhruv Amin:** Great.

**Dhruv Amin:** We can knock a bunch of these things out.

**Dhruv Amin:** I think that's, like, the most, like, urgent thing.

**Dhruv Amin:** Not to, like, put too much pressure on it, but, like, even just rough.

**Dhruv Amin:** Like, hey, we think if we could just continue on as normal, we're going to get here.

**Dhruv Amin:** We can max get here.

**Dhruv Amin:** And I think, like, in the onboarding, we basically were like, all right, let's just get going.

**Dhruv Amin:** Let's get publishing.

**Dhruv Amin:** Let's get, see what's happening.

**Dhruv Amin:** And then I was kind of expecting, hey, by November, December, we have enough data to kind of know, like, all right.

**Dhruv Amin:** Are we doing okay?

**Kyle Gaudreau:** Are we not?

**Dhruv Amin:** And so, I don't know, I think I was just flagging on last week was like, doesn't, now we're like mid-Jan, so I'm like, all right, like, doesn't seem like we're anywhere near where we, like, need to be for, like, in, like, three months, like, what's it look like?

**Dhruv Amin:** Or, like, in six months, what's it look like?

**Dhruv Amin:** So, yeah, so hopeful, thanks for, thanks for flagging that, like, you may not have the productions yet, but I, but I do think that, like, it's, it's important that we, like, get to it.

**Dhruv Amin:** Or, like, otherwise, or we just, like, or, like, what's gonna happen is, like, in a year, we're gonna be like, all right, this is great, but, like, it didn't actually drive, like, the needle.

**Dhruv Amin:** And so, like, what's the, what's the point of continuing to, to do this?

**Kyle Gaudreau:** Yeah, I don't want to let perfect get in the way better here, hear you on that, we can certainly address that with urgency, and we can always, you know, as we get your feedback, adapt our, you know, how we're thinking about the projections and plans associated.

**Kyle Gaudreau:** So, I think, at this phase of wanting to move fast, getting rapid feedback.

**Kyle Gaudreau:** It's the best place to be, so I hear that.

**Dhruv Amin:** think the other thing that was kind of missing for me a little bit was last time was, okay, let's imagine you don't even care about revenue, right?

**Dhruv Amin:** And you guys are just like, we're just going to just focus on just getting AI visibility or whatever it is.

**Dhruv Amin:** The thing that was missing for me a little bit was like, well, did all this work on like the strategy set of like some topic clusters we wanted to own.

**Dhruv Amin:** Like those had an expected amount of like, of like search volume that we thought we could like realistically go after in our current thing.

**Dhruv Amin:** Where do we like currently even stand and compare it to our like prior projections?

**Dhruv Amin:** So like we set out these topic clusters, we wanted to, we wanted to publish content in these areas.

**Dhruv Amin:** We thought the total search opportunity was this.

**Dhruv Amin:** We're two months in, we've penetrated it by like 1%, 10% or like, or like, no, we've actually won that.

**Dhruv Amin:** Like we're actually like doing great and we're going up in like top 10 for enough of these.

**Dhruv Amin:** And if we're, like, behind on that, then, like, that's fine.

**Dhruv Amin:** It's just, like, what, like, how soon or how quick do we actually project with our current, like, publishing schedule that we'll actually get there.

**Dhruv Amin:** So, like, let's go through this today and guys can have a deeper walkthrough of how we actually finally, like, tie it to revenue.

**Dhruv Amin:** Because ultimately, like, that would be the biggest way to make impact fast.

**Dhruv Amin:** Like, if you guys said, hey, actually, like, because we're tying all the way to revenue, search volume is not that high.

**Dhruv Amin:** But actually, we're getting really high intent searches on these, like, top articles.

**Dhruv Amin:** And, oh, we actually put a CTA in there that actually takes you direct to checkout.

**Dhruv Amin:** And so, as a result, like, this is already, like, paying back revenue-wise.

**Dhruv Amin:** That's also fine.

**Dhruv Amin:** Like, I don't, like, if you're saying, like, there's, like, multiple ways to win.

**Dhruv Amin:** One would be, like, scale in, like, search visibility and then pick up a much smaller percentage.

**Dhruv Amin:** Or we could just make the content itself convert faster.

**Dhruv Amin:** If it's like, all right, we have domain migration, and actually, like, your guys' domain authority means that, like, we're not going to be able to appear really high up.

**Kyle Gaudreau:** So, okay.

**Kyle Gaudreau:** That's fair.

**Kyle Gaudreau:** Yeah, that's fair.

**Kyle Gaudreau:** I would think about it largely the same.

**Kyle Gaudreau:** And I think, you know, a lot of this comes back to, for me, is, like, we just aren't, we don't have that right anchor point to compare against.

**Kyle Gaudreau:** And I think that's a bit of a, something we could have solidified a bit better early on in our process and is a gap.

**Kyle Gaudreau:** And I think as we can establish that here, it should make it a lot easier just to get your feedback and have something that is, yeah, just more referenceable when we talk about these data points of, like, how does it connect to the ultimate goal?

**Kyle Gaudreau:** That's ultimately what we want to do here.

**Kyle Gaudreau:** And it's just clear that, you know, there's a few gaps to address to be able to get there.

**Kyle Gaudreau:** Speaking of the projections particularly, probably the most pressing thing for me for projections, at least from a non-revenue standpoint, is access to your Google Search Console for...

**Kyle Gaudreau:** Anything specifically, I checked this morning and we didn't have it, so, you know, just if you can add team at growthx labs, that just gives me another data point to include into the projections of what's actually happening on that domain specifically.

**Dhruv Amin:** Okay.

**Dhruv Amin:** Give me one second.

**Kyle Gaudreau:** me just do it now.

**Kyle Gaudreau:** Appreciate it.

**Katya Luscomb:** Awesome.

**Dhruv Amin:** You guys have the other two?

**Kyle Gaudreau:** Correct.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** have create, we have both the other create versions.

**Dhruv Amin:** Yeah.

**Dhruv Amin:** Okay.

**Dhruv Amin:** Team at growthxlabs.com.

**Katya Luscomb:** Correct.

**Dhruv Amin:** Okay.

**Kyle Gaudreau:** Thank you, sir.

**Kyle Gaudreau:** That will be definitely helpful.

**Kyle Gaudreau:** So, yeah, you know, I think depending on what we can kind of gather from posts, Ciao.

**Kyle Gaudreau:** So this first cut is probably going to be a bit more traffic focused than a projection, but happy to, as we can better assess, like, what kind of dots can we connect from a revenue standpoint, how to add that in as well.

**Kyle Gaudreau:** Because I would agree, if we can get to a state that allows us to look at, you know, hey, we may not be getting here from traffic, but we're getting there for revenue, you know, different cuts of the data, that tells us probably a more compelling story as you think about ROI.

**Kyle Gaudreau:** So we'd love to dig in a bit more to, like, what you have today in post-hog and what may be lacking.

**Kyle Gaudreau:** Our thinking was, like, if we could have a view of, like, how maybe you measure other channels or how you may or may not measure organic and just get a sense of kind of, like, what's there.

**Kyle Gaudreau:** That may help us just chime in on what may be missing.

**Dhruv Amin:** Okay.

**Dhruv Amin:** Ultimate, like, thing that actually I track all the time is probably just gross volume in Stripe.

**Kyle Gaudreau:** Like, Like, see.

**Dhruv Amin:** Yeah, have two major things like, you know, our Stripe revenue as people come in and then also our revenue, cat revenue as people download the iOS app.

**Dhruv Amin:** The flow, I think you guys have been through it, for most users is typically like you sign up, you sign up, you fill out, you auth, sorry, I'm already logged in, you auth and then you land into a new project page.

**Dhruv Amin:** I don't, like, to the extent to which we have some traffic coming from, I don't know, like blog articles, I'm imagining it's probably something more like, like you click, I don't know, you eventually just land on site and you click the homepage and you go back to the main and then you basically try to, try to log in, but we could make CTAs to actually sign up like more.

**Kyle Gaudreau:** In post-doc, for you guys by channel, we can make a dashboard pretty, let me first just give you guys access, so, team at growthx, labs.com, you got it, perfect.

**Dhruv Amin:** I'm just going to make you an admin, so you can make, oops, whatever, anything else that you kind of mentioned in your zone?

**Kyle Gaudreau:** I think that's it, access flows, I know we talked about segment at one point, but my take is just, given it's been some time I've been hands-on with segment, but I can't imagine there'd be much we'd want to tweak there, it could provide us some visibility, I guess, but I think largely, like, just understanding how things are piped together.

**Dhruv Amin:** How you may be connecting the dots?

**Kyle Gaudreau:** How that shows up in visualization?

**Dhruv Amin:** That's the main thing in my mind.

**Dhruv Amin:** Yeah.

**Dhruv Amin:** So Segment is the only, is really the only, like, base tracking, I don't know, system that's in there.

**Dhruv Amin:** And so it grabs the raw events from mainly, like, sources like the web app.

**Dhruv Amin:** And in the code, we basically fire for every page view, a page view event in Segment, and then a track event for different, like, key customer actions.

**Dhruv Amin:** That happens both client side and server side on, like, the actual client, and then also on the backend.

**Dhruv Amin:** And then we basically just pipe that Segment data to any sort of, like, downstream tool that needs analytics.

**Dhruv Amin:** So PostHog gets all of its events from Segment.

**Kyle Gaudreau:** Have you seen that?

**Dhruv Amin:** Google Tag to interrupt you, but I just didn't want to.

**Dhruv Amin:** Yeah, so Segment tracks both an anonymous ID, and then once the user signs up, it reconciles an anonymous ID with the user's actual ID, and so it has, like, essentially person profiles in PostHog.

**Dhruv Amin:** Where that shows up is PostHog has this concept of people.

**Dhruv Amin:** People are just, have certain event properties on them.

**Dhruv Amin:** The, and then there's also, like, events.

**Dhruv Amin:** In Segment, the key actions that we kind of map, actions are just a segment concept of, like, of, like, how do you take something that might be categorized with multiple events?

**Dhruv Amin:** Um, and, um, and map it to, like, a canonical action that that thing means, um, in case, like, the UI changes, the event tracking changes, these things stay stable.

**Dhruv Amin:** Um, the key ones for us are, like, you know, you visit the landing page, um,

**Dhruv Amin:** You sign up, and there's a couple of different events.

**Dhruv Amin:** If you're looking in Tag Manager, example, Tag Manager only sees this landing page form submitted.

**Dhruv Amin:** The backend actually, which was the old client-side way of doing it, the backend actually fires an event when the user's created in database.

**Dhruv Amin:** So there's a signed up event that happens in the backend, but in the actions, you have signed up, and then you have subscription start or upgrade, which is fired when Stripe returns back from the checkout to the actual core app.

**Dhruv Amin:** And so the, and then VisitBuilder is like actually go and create like this new project page is VisitBuilder, basically visiting one of these slash build URL.

**Kyle Gaudreau:** Do you have a concept of like activation that you measure on top of this in some way?

**Dhruv Amin:** We don't.

**Dhruv Amin:** So that, I mean, the, the, the.

**Dhruv Amin:** Product virtually, get like $3 in like free credits to kind of come in.

**Dhruv Amin:** And so the fastest like path is just like, all right, how do you like, do they at least buy credits to actually experience this?

**Dhruv Amin:** There's other events that exist in Segment for things like publish and submit to App Store.

**Dhruv Amin:** That's later in the funnel, like when they're actually building an app.

**Dhruv Amin:** And right now we're working a lot on like how to actually just get people to a published activated event.

**Dhruv Amin:** But we have a couple other like heuristics of like, okay, send to at least one generation or something like that.

**Dhruv Amin:** So like the like general funnel, and I think these are a little out of date post to anything thing.

**Dhruv Amin:** I think we actually have like a 25% visit to sign up conversion from the landing page.

**Dhruv Amin:** Yeah, these events are out of date on generated because I need to update things for anything.com.

**Dhruv Amin:** Um, and then.

**Dhruv Amin:** Um,

**Dhruv Amin:** Generally, we have a graph here that's like free-to-paid conversion by weekly cohort that exists.

**Dhruv Amin:** So we can make a dashboard that's like dedicated to growthx if we want.

**Dhruv Amin:** The very quick thing that you can, I don't know, we could probably do is...

**Dhruv Amin:** Let me actually just see if I can make a new insight.

**Dhruv Amin:** That would likely connect to all of this.

**Dhruv Amin:** Let me see what do.

**Dhruv Amin:** So let's just take page views, unique users.

**Dhruv Amin:** The content filter group being that the path contains...

**Kyle Gaudreau:** I think the challenge in that, maybe we're just going through, for example, but just, like, you know, initial reaction is, like, that would over credit our impact because you have content in there that's not us, right?

**Dhruv Amin:** Yeah, totally.

**Dhruv Amin:** I'm just trying to, like, see, like, like, like, can we even see this, right?

**Dhruv Amin:** And then, or the other thing you could do this as, for example, is, like, there's going to be some filter, but, like, one other filter would be, like, initial referring domain.

**Kyle Gaudreau:** that's what's crispy of that.

**Kyle Gaudreau:** That's probably.

**Kyle Gaudreau:** Okay.

**Dhruv Amin:** So, this is, like, all users who got set with initial referring domain of Google, unique users, and then all page views, an initial referring domain is a post hoc computed property, where they just look at the person.

**Dhruv Amin:** If we can find an insight that we think reasonably approximates the growthx-like traffic that we like in insight form, then we can very easily create a cohort that's just always dynamic of like that filter and then filter our downstream graphs from it.

**Dhruv Amin:** Because from there, could do like other, so this is now a funnel where we look at initial referring domain and then, for example, we could just look in this action at subscription start and upgrade as the downstream thing.

**Dhruv Amin:** And this would give us like a pretty high sense of like, okay, 1,200 people in the last seven days came in from Google and 200, 300 there, we could probably do a like compute really quickly because we have plans stored on each of like what's the revenue impact of that.

**Dhruv Amin:** So the biggest thing I figured

**Dhruv Amin:** It would just be like, what is our filter that actually captures just the growth that's content that could then turn into a thing.

**Dhruv Amin:** And then, yeah, you can, of course, like, filter this by, if we wanted to split this out, we could break this down, for example, by, I think, domain.

**Dhruv Amin:** I don't there should be one that's on the, or URL, I think, is the post-doc property.

**Dhruv Amin:** Initial URL.

**Dhruv Amin:** And so, very quickly, you can kind of see that, like, the rough traffic sources by anything, createxyz or createanything.com on just unique users by day from Google.

**Dhruv Amin:** And what's the biggest one?

**Dhruv Amin:** All other main, sorry, just the long tail.

**Dhruv Amin:** So we could probably filter this by some regex that's basically just looking at all domain things.

**Dhruv Amin:** But so, yeah.

**Dhruv Amin:** So I think the thing that's like, so I guess like for you guys, Google Search Console will just give you raw views of that content.

**Kyle Gaudreau:** It clicks, yeah, to me, it's like its utility is to just let us know, like, is your content getting as indexed as fast as we want it to be?

**Kyle Gaudreau:** Is it generating impressions?

**Kyle Gaudreau:** Is it getting clicks?

**Kyle Gaudreau:** And then a little bit deeper cuts into like what queries are actually driving it.

**Kyle Gaudreau:** So like we tend to, how this tends to go is in the early days, we tend to lean more on Google Search Console data because in those early like stages of building a program, like that's where like you're looking for that signal.

**Kyle Gaudreau:** And then as As that matures, we start to look at tend to lean.

**Kyle Gaudreau:** Either if our clients are using GA or PostHog or things of that nature, how do we think about the cuts of the data?

**Kyle Gaudreau:** Where is that traffic going?

**Kyle Gaudreau:** How engaged is it?

**Kyle Gaudreau:** And then different trajectories typically on when to expect conversion with a motion like yours that has a bit of a lower friction point to getting started.

**Kyle Gaudreau:** I think it's a bit more reasonable to expect faster there because, I mean, 25% conversion rate is crazy.

**Kyle Gaudreau:** Like compared to some industries, like that's like, you know, quite high, right?

**Kyle Gaudreau:** But like given the way your model works, that makes sense.

**Kyle Gaudreau:** I'm sure you probably want it to be higher, but.

**Dhruv Amin:** No, I mean, yeah, like if you think about it, it's like 25% visit of the homepage to sign up.

**Dhruv Amin:** So like to be clear, like that might be different for just.

**Kyle Gaudreau:** Totally.

**Kyle Gaudreau:** Yeah, blog is probably lower.

**Dhruv Amin:** And then probably like a 3% free to paid, like free sign up to actually convert.

**Dhruv Amin:** And then we're trying to raise all the reasons to raise free to pay.

**Dhruv Amin:** But something like 90% of our, 95% plus of all of our conversions happened in that first session.

**Dhruv Amin:** So like, really.

**Kyle Gaudreau:** the time lag to revenue?

**Dhruv Amin:** What's that on average?

**Dhruv Amin:** I mean, immediately, because it's consumer, right?

**Dhruv Amin:** So, time lag to revenue.

**Dhruv Amin:** Like, oh, sorry.

**Kyle Gaudreau:** Like, yeah, they buy a subscription and then they.

**Kyle Gaudreau:** Correct.

**Kyle Gaudreau:** Like, I wasn't sure if it's like on average, like two days or, you know.

**Dhruv Amin:** No, no, no.

**Dhruv Amin:** That's what I mean by our conversions to like paid.

**Dhruv Amin:** So, like 95% of our like paid conversions are actually in that first session.

**Dhruv Amin:** And so, and so, yeah, I just think we like get to a place where we're looking at this as like, yeah, how much traffic are there?

**Dhruv Amin:** And more importantly, like how many like actual users or actual subscriptions are we driving with the content soon?

**Dhruv Amin:** But maybe we're just not, I mean, you guys were saying it's 250 weekly impressions, right?

**Dhruv Amin:** Or like, and impressions are visits in your mind, right?

**Kyle Gaudreau:** We're looking at.

**Kyle Gaudreau:** sessions for that number you're quoting.

**Kyle Gaudreau:** This past week, I think, was in like the 280 plus range, if I recall correctly.

**Kyle Gaudreau:** So it's up, but, you know, in that relative ballpark.

**Kyle Gaudreau:** And so what we realize now after talking to you and like getting more depth and more context, essentially what GA is showing us is like the aggregate across all three domains, right?

**Kyle Gaudreau:** So that given the way your content is currently set up, it is in a sense giving us to say probably most more accurate view than pure going to a single GSC profile and seeing what the clicks tell us.

**Kyle Gaudreau:** Cause we're seeing like in aggregate, how many sessions are we getting across our content and across three domains?

**Dhruv Amin:** Yeah.

**Kyle Gaudreau:** And like, this is kind of doing the same in a sense, right?

**Dhruv Amin:** Yeah.

**Dhruv Amin:** Cause under the hood, all three of those domain domains are just a domain space level.

**Dhruv Amin:** So like all three of those domains are the same web app.

**Dhruv Amin:** They just different homepages, but it's the same segment tracking.

**Dhruv Amin:** It's the same, whatever the differences that the event ties, whatever the domain is.

**Dhruv Amin:** But then it all pipes to the same place.

**Dhruv Amin:** then there's further breakdowns where you can just be like, all right, I only care about the anything traffic or the Create traffic.

**Dhruv Amin:** But from our perspective, we don't really care.

**Dhruv Amin:** From our North Star, that's what I love a little bit.

**Dhruv Amin:** We do care in the long run that anything is the one that actually builds up all the brand and domain authority.

**Dhruv Amin:** But that takes time.

**Dhruv Amin:** So in the short term, it's much more like, okay, if you acquire on Create.

**Dhruv Amin:** And then what also happens is that users get, even if they land on Create or they land on createanything.com, when they do sign up, they get redirected to anything.com.

**Dhruv Amin:** And every ongoing email thing that would pull them back into the product is also anything.com.

**Dhruv Amin:** So I don't know.

**Dhruv Amin:** There's a part of me that's like, yes, we should do a really clean migration as fast as possible on anything, and we should do that stuff.

**Dhruv Amin:** But like, if you were to tell me like, no, actually like CreateXYZ has.

**Dhruv Amin:** And domain authority for blog content and we can get here faster if what we do is we just leverage CreateXIC's ability to publish blogs because Google will index it and we can rank higher faster, then maybe the right strategy is to actually just be like, well, screw anything indexing.

**Dhruv Amin:** We want to like, we'll just publish under Create, we'll make the anything blog for this like tail content, not look as legit.

**Dhruv Amin:** And then at some point when we start building up more anything authority, we're going to change it over.

**Dhruv Amin:** That also works.

**Dhruv Amin:** So I don't know.

**Dhruv Amin:** For us, it's more like what's the fastest path to impact on the channel?

**Kyle Gaudreau:** I can, I can noodle on that one a little bit more, but my off the cuff take on that is if we're looking at that from a pure time to impact perspective, Create.XYZ is your strongest profile.

**Kyle Gaudreau:** So, so that might be, if we're going to look at it from that perspective, might be the healthiest move.

**Kyle Gaudreau:** Although, um, you know, the canonicals that would help, that would reverse some of the recommendations around the canonicals.

**Kyle Gaudreau:** Not to create this circular confusion here, but ultimately, I think with where we are going now with the canonicals in place, I think we should be healthier.

**Kyle Gaudreau:** I'm almost apprehensive to jump to that because I think it's too presumptuous.

**Kyle Gaudreau:** My take would be to post to anything.

**Kyle Gaudreau:** It seems like it's going to post across all three anyways, if I'm understanding the architecture correctly anyway, from what I see and what you've mentioned.

**Dhruv Amin:** But like to your point, like on this sanity publishing piece, it's pretty fast for us to just do a 301 redirect across every article if the domain is createanything.com slash blog or create.com slash blog.

**Dhruv Amin:** So like that would be the fastest way, like when publishing just to publish anything would just be like it publishes everywhere, but those links all 301 redirect quickly to anything.

**Kyle Gaudreau:** like that be be the

**Kyle Gaudreau:** In that case, though, if I'm understanding that correctly, we publish a net new article tomorrow in that way.

**Kyle Gaudreau:** It's set up.

**Kyle Gaudreau:** It programmatically creates a 301 from the other domains to anything?

**Dhruv Amin:** We would just set a next.

**Dhruv Amin:** So it's all a single Next.js app that's using Sanity as the backend.

**Dhruv Amin:** And so when you go to that slash blog route, it's just fetching the data from Sanity, but it's all the same data.

**Dhruv Amin:** And then the domain is different, but it's all pointing at this.

**Dhruv Amin:** All three domains are pointing at the same app.

**Dhruv Amin:** So the app, we could just do some code if you want it.

**Dhruv Amin:** If you're like, hey, we just want from like a, like there'll still be, if a crawler comes and hits that blog, create xyz slash blog, that crawler like would crawl and see, oh, create xyz slash blog is now 301ing to, to.

**Dhruv Amin:** Createanything.com slash blog.

**Dhruv Amin:** And then if there is a leaf page out there for some reason for createanything.com slash blog slash series A or announcement, there's some link and someone follows it, it'll just link back to the anything thing.

**Dhruv Amin:** So that would effectively take down the other editorial blog content site.

**Dhruv Amin:** And I'm fine with that on the blog content because, to be with none of the blog content is really getting indexed in the first place.

**Dhruv Amin:** Yeah.

**Dhruv Amin:** We're not indexed.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** As I go through these projections, gives me a further deep cut to consider this with.

**Kyle Gaudreau:** However, my initial take is we probably want to continue with the current canonicalization strategy.

**Kyle Gaudreau:** I, you know, I understand urgency is a thing here, but I think given just the mixture of signals we're seeing, it should be a balance of the best of both worlds.

**Kyle Gaudreau:** But, oh.

**Kyle Gaudreau:** you.

**Kyle Gaudreau:** I'll think about it a little bit more to know that I have been looking at this framing that anything is the gospel that we're moving towards and that that's like the primary domain.

**Kyle Gaudreau:** And how do you do that in the most effective way?

**Kyle Gaudreau:** So let me validate that, but I think we still should stick with the current path for the time being.

**Dhruv Amin:** Yeah, mean, look, I think like, yeah, North Star is just like time to revenue.

**Dhruv Amin:** So the last time you were like, you're like, oh, well, like, it's going to take a while to build up authority.

**Dhruv Amin:** And then, and only then can we get to revenue.

**Dhruv Amin:** I'm like, well, if we have a 46 DA domain and, and really a lot of this leaf content is just being published to be a landing point in search.

**Dhruv Amin:** So, yeah, I don't know.

**Dhruv Amin:** Let's use it as fast as possible, but, but yeah.

**Kyle Gaudreau:** Yeah, I'll get you for the many things we have.

**Kyle Gaudreau:** We'll, for whatever reason, we have a strong take to diverge.

**Kyle Gaudreau:** We won't let that lag.

**Dhruv Amin:** We'll get back to you this week on that.

**Dhruv Amin:** Okay.

**Kyle Gaudreau:** Okay, that's helpful.

**Kyle Gaudreau:** Certainly can play around, post-talk, see what's there.

**Kyle Gaudreau:** Happy to propose any ideas or get any feedback as it relates to how do we measure our success, like what are those metric points.

**Kyle Gaudreau:** Some of the things I was mentioning for activation reasons, I'm not pushing it here, but just some brands I've been at the past, you know, for example, even growth at home base before this, we tend to look at some proxy numbers that based off of like certain windows of time, if we saw certain signals of activation, it was strongly correlated to revenue.

**Kyle Gaudreau:** But that was some of my reasoning behind the time lag question of like how quickly we get that signal back.

**Kyle Gaudreau:** So my hunch is like there's not something to explore there, but I just want to continue to like, if we can make some recommendations of like what's the right proxy for thinking about the success of our content from a sign up to revenue standpoint, it does feel like still rooted in what you mentioned, but just some content.

**Kyle Gaudreau:** That's what's going through my mind.

**Dhruv Amin:** Yeah, I mean, there are some, like, interesting tells that could be interesting to think about.

**Dhruv Amin:** The highest retention segment and the highest free-to-pay conversion segment, like, I think free-to-pay conversion is already above 10% for the, like, self-identified entrepreneur cohort, someone who's actually trying to launch a new product and service.

**Dhruv Amin:** And so that's why I think most of the content has been focused around that.

**Dhruv Amin:** And so the other two segments with similarly high free-to-pay conversion ratios up front are consultants and then, like, leadership, or honestly, someone who's, like, high up in an org that calls themselves leadership.

**Dhruv Amin:** We're doing some enrichment of person profiles that don't require a user to actually, like, tell us who they actually are.

**Dhruv Amin:** But, you know, if we did a breakdown of, like, here's all the GrowthX content, like, as a proxy, one step earlier proxy, just demographically, would be like, okay, we just look at the GrowthX signups.

**Dhruv Amin:** And we look look at...

**Dhruv Amin:** And

**Dhruv Amin:** In product survey data, we also look at the enriched data, how well is the growthx content bringing in our target profile, right?

**Dhruv Amin:** Which is another way to kind of, I don't know, one proxy up.

**Dhruv Amin:** And then on activation, you do have to capture that user in the first session to a paid user to have them keep using the product, which is why that really matters.

**Dhruv Amin:** But then the other thing we look at is, yeah, honestly, like, can you get to publish?

**Dhruv Amin:** Right now, our overall publish rate is about 20 to 30%.

**Dhruv Amin:** And then what we're trying to work on is, like, if you can get to publish, you're more likely to stick with the product.

**Dhruv Amin:** There's a handful of other signals that are, like, clearly there in our ICP, like, connecting payments, connecting other pieces, like, numchat messages sent per time or, like, X of Y days, like, login.

**Kyle Gaudreau:** But the problem is they're all a little bit behind, like, did you even convert them to paid?

**Kyle Gaudreau:** Because if you didn't convert them to paid, then...

**Kyle Gaudreau:** Yeah, it becomes less useful in that case.

**Kyle Gaudreau:** Unless it's, like, have a suspicion that...

**Kyle Gaudreau:** The quality of your paid is just highly variable.

**Kyle Gaudreau:** Maybe that's where it increases in importance.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** It's one thing to get them to pay it.

**Kyle Gaudreau:** How long are they paying for, for example?

**Kyle Gaudreau:** But anyways, yeah, that's helpful.

**Kyle Gaudreau:** I think it's still worth exploring how we did this at Homebase.

**Kyle Gaudreau:** we learned was because that's an app for managing your local small business hourly team, if they added a team member and that person logged in, that was a very useful proxy to they are using the platform for the intention of it.

**Kyle Gaudreau:** And if we back off that, like that's how my team was like measured off of other metrics was can you drive that efficiently?

**Kyle Gaudreau:** What's the cost of that?

**Kyle Gaudreau:** And we obviously had all the other associated metrics to that.

**Kyle Gaudreau:** Like, you know, how do you work back off of CAC payback and things with that in mind?

**Kyle Gaudreau:** But that was like the, that was like the ultimate North Star my team had been measured on.

**Dhruv Amin:** So that was just what was driving some of the curiosity.

**Dhruv Amin:** Yeah.

**Dhruv Amin:** We have.

**Dhruv Amin:** Similar, we're actually in the midst of doing all these retention cuts as well on, like, the PLG drivers to see if there's anything else besides, like, publish.

**Dhruv Amin:** But it is, like, you know, make a mobile app.

**Dhruv Amin:** So, yeah, so this is where, like, a little bit of, I'm like, how are we doing in, this is why I'm curious how we're doing in topic clusters, because, like, you know, I think, like, over time, want anything to become known as the best for building, like, mobile apps.

**Dhruv Amin:** And so it's, like, okay, in the mobile app topic cluster, like, how visible are we right now?

**Dhruv Amin:** Or, like, for entrepreneurs generally of building a business online, like, what is that total, like, size of price search-wise that we could be getting to?

**Dhruv Amin:** And, like, where, how much of it do we think we've penetrated in the first two months?

**Dhruv Amin:** And what do we think the path is to kind of get there?

**Dhruv Amin:** Is, because, yeah, I mean, like, there's, like, the very short-term goal of, like, can we actually start driving significant traffic and revenue?

**Dhruv Amin:** But there's a bigger, longer-term goal of, like, all right, we actually want the site to start pulling in the right types of users.

**Dhruv Amin:** So yeah, I'm trying to think of like other, yeah, think that's the main thing.

**Dhruv Amin:** So thanks for doing the projections.

**Kyle Gaudreau:** We'd love to chat when you have a sense.

**Kyle Gaudreau:** that's very helpful framing.

**Kyle Gaudreau:** Yeah, it gives me some additional things to think about as we think about, you know, a deeper meaning behind those numbers and what we're going after.

**Kyle Gaudreau:** So yeah, very much appreciate that.

**Kyle Gaudreau:** And certainly, you know, learning for us of like, how do we do these sorts of things a bit more consistently early on, but appreciate you working through it with us.

**Dhruv Amin:** Yeah, no worries.

**Dhruv Amin:** No, look, I wanted to be successful ASAP.

**Dhruv Amin:** So that's my like goal.

**Dhruv Amin:** And so, and like, and that like realistically look back and we're like, yeah, that was like a big reason why we drove a lot of, a lot of, in the short term revenue.

**Dhruv Amin:** But honestly, like,

**Dhruv Amin:** Everything's kind of aligned right now.

**Dhruv Amin:** The ICP is kind of clear.

**Dhruv Amin:** If we just capture those ICP users, they tend to like the product.

**Dhruv Amin:** And so when I think about organic search, it's really like, okay, how do we just make sure we're in the places that they want to be found?

**Kyle Gaudreau:** So I don't know.

**Dhruv Amin:** If you guys found other opportunities where you're like, hey, okay, this editorial strategy, we're not going to actually nail SEO fast enough with your domain authority.

**Dhruv Amin:** But we think there's bigger size of prize to do something programmatic or do something else than I'm down for it.

**Dhruv Amin:** just, yeah, I don't know.

**Dhruv Amin:** Just trudging along with like the same thing, but not being on a path to like a meaningful change in performance because we did something feels like the worst part.

**Kyle Gaudreau:** Yeah, understandable.

**Kyle Gaudreau:** And, you know, certainly understand the urgency in your position.

**Kyle Gaudreau:** You have to have that urgency and, you know, we need to be a good partner to help you get there.

**Kyle Gaudreau:** So

**Kyle Gaudreau:** You know, I appreciate the context today.

**Kyle Gaudreau:** think this definitely helps us figure out a couple things moving forward.

**Kyle Gaudreau:** On the PSEO side of this programmatic side of it, it's something certainly that we're going to be thinking about related to the projections.

**Kyle Gaudreau:** You know, it could be a path where we explore how do we do some editorial things in parallel as we're building the scaffolding, the foundation for that programmatic play.

**Kyle Gaudreau:** And, you know, what is the time frame to impact from that?

**Kyle Gaudreau:** Just the thing we have to be mindful of in those scenarios is programmatic plays tend to take longer to get off the ground.

**Kyle Gaudreau:** Once you get them off the ground, they can move a lot faster.

**Kyle Gaudreau:** So there's just a few things kind of the way, but I think there's some things we can do in parallel.

**Kyle Gaudreau:** The reason the team had gone the direction they had was, you know, just this idea of like authority building pre-programmatic, because we've just seen some brands come to us where they're very...

**Kyle Gaudreau:** Like, early on in their authority, and they just have seen other brands do some, like, pretty cool programmatic things, want to move fast, and that doesn't always set them up for success.

**Kyle Gaudreau:** So I think that was some of the reason behind where the miss was, was connecting the dots to, okay, maybe we agree that logic is correct, but, like, when, like, what is that timeline to programmatic?

**Kyle Gaudreau:** What is that play?

**Kyle Gaudreau:** How does that relate to the projections?

**Dhruv Amin:** It just didn't, we didn't anchor it enough into the timeline.

**Dhruv Amin:** Yeah, okay.

**Dhruv Amin:** Yeah, I mean, if you've come from growth at a startup, you know what it is.

**Dhruv Amin:** It's like, it's like, all right, you guys are spending X on marketing on, like, on, like, Y thing.

**Dhruv Amin:** What is the actual, what is the actual payback period for that cap?

**Dhruv Amin:** Oh, totally.

**Kyle Gaudreau:** I mean, literally, I was the first growthx customer, so, like, when I signed up, like, you know, if I only came back to the exec team and showed them, you know, traffic numbers, and that was it, they would not have taken that as confidence in the investment, and so.

**Dhruv Amin:** yeah, I totally understand.

**Dhruv Amin:** And yeah, just, I just like, there's lots of, like we email a bunch of SEO players and a lot of people were kind of giving the classic answer of like, oh yeah, it's SEO.

**Dhruv Amin:** It takes, you know, two years and then like, you know, year two, you kind of get there and, and we just have to stay with it and go do it.

**Dhruv Amin:** And I think part of the reason I went with growthx was it felt like it was much more like, no, we, we like are good at making this stuff work fast.

**Dhruv Amin:** And so, so I don't I'm just raising the red flag over like, we're three months in and like, it's, and maybe there's a miscommunication miss on our side as well.

**Dhruv Amin:** On my side, I'm actually, I'm trying to find like a day-to-day owner for a lot of this stuff because I don't know, I think with like, a lot of the changes you guys want us to make, like we should be able to go pretty quick.

**Dhruv Amin:** But, but yeah, and like, on our side, like, I honestly don't, I think you guys have been asking for a lot of permission or waiting for like our reviews.

**Dhruv Amin:** I would just say, skip all that.

**Katya Luscomb:** Let's just like, whatever helps you guys move quicker.

**Dhruv Amin:** Create, publish, like, if it's not good, I'll give you some feedback of, like, hey, that, like, we should maybe adjust this in it or, like, or, like, I don't know, like, but, like, I think because I, because I, there's a lag here in, like, in, like, how quick we can even get data from, like, what gets indexed, what gets put out, and it's, like, close enough in messaging that, that we could, we could, I don't know, we'll just learn, like, what's better to double down on.

**Kyle Gaudreau:** So, thanks, guys.

**Katya Luscomb:** Yeah, that makes sense.

**Katya Luscomb:** I know we're, over time, really appreciate the conversation, like Kyle said, echoing helpful insight.

**Katya Luscomb:** One other thing that I think could be helpful, we had some documentation around messaging and initiatives that you all had coming up through the end of 2025, and I was curious if you had any documentation similar around initiatives you've got in 2026.

**Katya Luscomb:** A lot of it was around, like, your, your mobile app launch, and some of those different elements, just so that we can make sure that as we're looking big picture strategy, we're considering all those different aspects, too.

**Dhruv Amin:** I mean, I think, I think everything's, like, kind of the same.

**Dhruv Amin:** Like, yes, we're going to keep making the agent better.

**Dhruv Amin:** Yes, we're going to keep making the mobile app better.

**Dhruv Amin:** But like overarching vision for the company is still kind of the same.

**Dhruv Amin:** We want people to start products and services built on top of anything, targeting like entrepreneurs.

**Dhruv Amin:** If there's any one update, I think we're like 2x bigger than now post-launch any of the other mobile vibe coding players, the ones that can actually make mobile apps that can actually get to the app store.

**Dhruv Amin:** Or I think we had, right when we first started with GrowthX, we had like just launched.

**Dhruv Amin:** And so, you we were like a mobile vibe coding player.

**Dhruv Amin:** think right now we were like one of the mobile vibe coding players.

**Dhruv Amin:** And so that changes your like content strategy or like just bias of like, this is the best one by far for making native mobile apps that can actually publish to the app store.

**Dhruv Amin:** Or like more of a mobile lens that's maybe more of like a focus.

**Dhruv Amin:** It's still just a wedge for us.

**Dhruv Amin:** Like in the long term, we don't really care if you're building a web app or a mobile app or an agent or whatever it is.

**Dhruv Amin:** And we're

**Dhruv Amin:** I want anything to support it, but that's maybe one, like, area where I'm like, and actually, I think when I look at SERPs, like, like, just by hand, like, there actually isn't a lot of great content on, like, on, like, so you're vibe cutting a mobile app, like, how do you actually, like, like, figure out, like, how to design it?

**Dhruv Amin:** And, like, tips of, like, go to Mobbin, or, like, oh, you need to go to the app store, like, how do you, what are the best 10, like, business models that, like, apps usually use to get on the app store, or that succeed, or, like, break, like, more research breakdowns of, like, okay, like, here's actually all the charts in the app store today, like, what are the actually interesting, like, opportunities that are uniquely opened up, like, where, where you don't have apps actually being published?

**Dhruv Amin:** So, like, there's stuff like this that I kind of think I could imagine seeing ranking around, like, app store submission or something else, just as a point of emphasis, but otherwise, I think it's the same, like, topic.

**Dhruv Amin:** Areas, like AI, entrepreneurs, yeah, yeah, and so I, like, this is where, this is where I was going to do the projections, I'm like, yeah, like, where are we today, I guess, in, like, the initial set, like, how penetrated are we, how big is that actual search rise, if, I think you'd give me slightly more ideas on, on where else we could go with the content.

**Kyle Gaudreau:** Yeah, that makes sense, cool, well, put our, put our heads together on some of that, very, very helpful feedback, and I will be jamming on the projections, especially helpful now that I have GSC access, so, appreciate that, and then, probably towards the tail end of week, we'll, mid-tail week, we'll dig into a post-talk a bit more in depth.

**Dhruv Amin:** I think one other, like, updated piece of thinking that might be, like, new for you guys, we launched Anything Max in late September.

**Dhruv Amin:** And we now launched, like, we relaunched it in, like, December.

**Dhruv Amin:** And I think it's like now it drives something like 50% of our revenue plus, and it's like the $200 a month tier, like, and which a lot of AI products like us are kind of like putting into place.

**Katya Luscomb:** I think we might have lost you, Dhruv.

**Dhruv Amin:** The cost of like a dev agency and is actually just much more serious about their build.

**Dhruv Amin:** And so like the base logic of like the company right now is like push to that $200 a month tier plan of like the browser.

**Dhruv Amin:** So we could make more dedicated content around it.

**Dhruv Amin:** I don't know how it'd rank though.

**Dhruv Amin:** Like, I think this is where I'm a little bit like lost to like how do actually get that to rank on like, I don't know, things around browser use or things around like what you're doing with the product.

**Dhruv Amin:** So I don't know.

**Dhruv Amin:** It's just like another insight.

**Kyle Gaudreau:** Oh, cool.

**Dhruv Amin:** Like, I think there was a thread that also got lost around CT.

**Dhruv Amin:** CTAs in the onboarding and making our blog content better.

**Dhruv Amin:** So if you do come away and you're like, hey, we're low on traffic, but we can actually drive more revenue with better CTAs, then maybe that's another area to focus.

**Kyle Gaudreau:** Makes sense.

**Dhruv Amin:** Okay.

**Kyle Gaudreau:** Well, really appreciate it.

**Dhruv Amin:** See ya.

**Katya Luscomb:** Yeah, thank you.
