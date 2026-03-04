# Engine Weekly Sync

<metadata>
date: 2025-09-12
time: 18:31 UTC
duration: 39 minutes
organizer: Kyle Gaudreau (GrowthX)
participants: Cole Parker (Engine), Carrie Chowske (GrowthX), Darrell Etherington (GrowthX), Feyisayo (GrowthX), George Haikal (GrowthX), James Winter (HotelEngine), Joel Murphy (HotelEngine), Kali Wootton (HotelEngine), Kyle Gaudreau (GrowthX), Rory Conroy (Engine), Colm Shalvey (Engine)
fathom_recording_id: 86985338
fathom_url: https://fathom.video/calls/406449045
share_url: https://fathom.video/share/uTtEf4WpHXSBoAeHT8dzyMEWHeVzib6f
source: fathom
enriched_on: 2025-03-03 12:45 UTC
</metadata>

---

## Summary

GrowthX and Engine/HotelEngine aligned on content strategy priorities and identified key technical challenges: a 3% week-over-week performance increase, but with clicks trending slower than expected—suggesting the need to focus on 2 high-conviction content lanes. Kyle shared analysis on FAQ schema implementation needs, PSEO opportunities with 4,000-7,000 unindexed pages ready to explore, and flagged a critical issue with AI-generated content hallucinating Engine product features that don't exist. The team also needs to close the loop on the Roomblocks SOW pricing and scope before proceeding.

---

## Context

Engine is a hotel management platform that GrowthX is providing content marketing services for. The relationship appears to span two entities—Engine.com (Cole Parker, Rory Conroy, Colm Shalvey) and HotelEngine.com (Joel Murphy, James Winter, Kali Wootton)—suggesting either a rebrand, product portfolio separation, or related business units. Kyle Gaudreau leads the GrowthX delivery on this engagement and was relatively new to the account at the time of this call, having spent the week diving into performance data and analysis. This weekly sync is a standard operational cadence where the teams review content performance, discuss technical implementation issues, and align on new initiatives like PSEO expansion and strategy work (Roomblocks SOW).

---

## Relevance

**To GrowthX Delivery:**
- AI hallucination in content output is a critical quality control issue—team needs fact-checking workflow improvements and more specific product language guidance to prevent false features from being attributed to clients in published content
- FAQ schema implementation in Webflow is breaking due to outdated domain references; consider building a HTML data-attribute-based component for dynamic schema generation to ensure long-term maintainability
- PSEO strategy needed for 4,000-7,000 unindexed pages—represents quick-win opportunity but requires thoughtful indexation strategy to avoid overwhelming search engines

**To GrowthX Business Development:**
- Roomblocks SOW pricing and scope concerns signal potential account friction; Kyle needs to align with Marcel on flexibility options and schedule a follow-up meeting with Cole Parker, Joel Murphy, and Colm Shalvey to close the deal
- Account shows engagement signals across multiple initiatives (content refresh, analytics dashboarding, new SOW) indicating health and willingness to invest, but pricing clarity is required to move forward

---

## Overview

- Performance is trending up but could be stronger; focus on strategic content lanes may help
- FAQ schema implementation in Webflow needs refinement for long-term maintainability
- PSEO opportunities exist with 4,000-7,000 unindexed pages; worth exploring for quick wins
- Roomblocks SOW needs further discussion to align on scope, deliverables, and pricing

---

## Key Topics

### Content Performance Analysis

  - Overall performance: 3% up week-over-week, relatively flat
  - Impression spike last week, clicks trending up but could be stronger
  - New content showing promise, refresh content mostly flat except for one standout article
  - Opportunity to focus on 2 high-conviction content lanes while leaving room for experimentation

### FAQ Schema Implementation

  - Current Webflow setup references outdated HotelEngine.com
  - Considering building a component that generates schema from HTML markup with data attributes
  - This approach would ensure FAQs stay in sync during future content refreshes

### PSEO Opportunities

  - 4,000-7,000 unindexed pages present potential quick wins
  - Need to explore indexation strategy without overwhelming search engines
  - Could be an area to experiment with alongside topical content focus

### Roomblocks SOW Discussion

  - Concerns raised about pricing and clarity of deliverables
  - Kyle explained the value of the strategy sprint in creating repeatable processes
  - Team to schedule a follow-up meeting to discuss options and find a mutually beneficial approach

### AI Content Hallucination Concerns

  - Joel identified instances of AI-generated content misrepresenting Engine's features
  - Team to implement more rigorous fact-checking and specific product language to mitigate issues

---

## Action Items

**Joel Murphy (HotelEngine)**
- Add AI hallucination examples re product features to Notion doc
- Set up quick Amplitude data review session with Kyle Gaudreau

**Kyle Gaudreau (GrowthX)**
- Follow up with team on FAQ schema implementation; validate HTML markup with data attributes approach
- Explore PSEO opportunities with team; analyze 4,000-7,000 unpublished pages and develop indexation strategy
- Discuss Roomblocks SOW with Marcel; prepare for potential meeting with Engine team, focusing on flexibility and pricing

**Cole Parker (Engine)**
- Schedule 15-minute sync with Joel Murphy, James Winter, and Colm Shalvey regarding Roomblocks SOW

---

## Transcript
**Kyle Gaudreau:** Yeah, I'm doing well.

**Kyle Gaudreau:** Happy Friday.

**Joel Murphy:** Amen to that.

**Kyle Gaudreau:** It's a different background for you today.

**Kyle Gaudreau:** Just switching it up in the house?

**Joel Murphy:** Yeah, yeah, yeah.

**Joel Murphy:** I just get sick of sitting in the same place.

**Joel Murphy:** And like, especially on Fridays, I feel like if I sit here on my couch, it doesn't feel like work as much.

**Joel Murphy:** You know what I'm saying?

**Joel Murphy:** So it's kind of like a way to start the weekend without actually starting a weekend.

**Kyle Gaudreau:** Yeah, yeah, for sure.

**Kyle Gaudreau:** I hear you.

**Kyle Gaudreau:** I try to mix it.

**Kyle Gaudreau:** I don't know if I'm doing it as better, as good as I used to.

**Kyle Gaudreau:** Sometimes what I would do is like certain types of work.

**Kyle Gaudreau:** I would, you know, if I need to get like super heads down, nerd out on some data, you know, have like a chair for that.

**Kyle Gaudreau:** And like put on some headphones, you know.

**Kyle Gaudreau:** But other times, it's just like the pros and cons of working from home.

**Kyle Gaudreau:** I can just like be, you know, here for a while.

**Joel Murphy:** And I'm like, oh my God, it's the end of the day.

**Joel Murphy:** I need to get up.

**Joel Murphy:** Like move around and get fresh air.

**Joel Murphy:** Yeah, that's the tricky part, especially with what I'm doing, sitting on my sofa.

**Joel Murphy:** It's like, well, where do you go when you're done for the day?

**Joel Murphy:** Like if you're already sitting on your couch, it's like, it gets weird and blurry.

**Joel Murphy:** And I try to sit in my office as much as I can for that reason, to have a separation of church and state, but, you know, kind of don't really succeed all that much.

**Kyle Gaudreau:** I was of the mind after COVID that I was never going back in the office again and, you know, even in form where we bought our home and just like so many different things.

**Kyle Gaudreau:** When I was at Homebase previous to this, they had a like two day a week policy.

**Kyle Gaudreau:** And I was like, all right, you know, I'll give it a shot.

**Kyle Gaudreau:** And actually, I really liked it, like the change of pace and this and that after working from home for so long.

**Kyle Gaudreau:** So, you know, definitely some pros and cons.

**Joel Murphy:** I do like that work from home time when I can get it, though.

**Joel Murphy:** I do, too.

**Joel Murphy:** It's my preference.

**Joel Murphy:** But, I mean, I like the...

**Joel Murphy:** Like, to be honest, I haven't been in an office in, like, way before COVID, but doing off-sites, it's kind of office-y, right?

**Joel Murphy:** And I like that better than WeWork.

**Joel Murphy:** Like, WeWork's like going to an office and you don't know anybody.

**Kyle Gaudreau:** Yeah, 100%.

**Kyle Gaudreau:** 100%.

**Kyle Gaudreau:** Yeah, we had that, I joined GrowthX pretty early on.

**Kyle Gaudreau:** I was here in October, and it was, like, just me, Daniel, and Marcel, like, in a very small, kind of, like, shared space.

**Kyle Gaudreau:** It wasn't WeWork, but it was kind of similar.

**Kyle Gaudreau:** Once we had our own office space, it feels definitely a lot different, like, going into the office and enjoyable, so.

**Joel Murphy:** Yeah.

**Kyle Gaudreau:** Hey, Cole.

**Kyle Gaudreau:** Happy Friday.

**Cole Parker:** What's up, guys?

**Kyle Gaudreau:** How we doing?

**Kyle Gaudreau:** Good, good.

**Kyle Gaudreau:** Really appreciate you both being flexible on time.

**Kyle Gaudreau:** Classic.

**Kyle Gaudreau:** Having an almost three-year-old and working at a startup is usually filled with curveballs, so I really appreciate it.

**Joel Murphy:** Yeah, no problem.

**Kyle Gaudreau:** Yeah, cool.

**Kyle Gaudreau:** Should we wait for Colm, or we good?

**Joel Murphy:** I, you know what, I don't know.

**Joel Murphy:** I haven't seen the calendar, but let me see if he can.

**Kyle Gaudreau:** It's like he accepted, but, you know, worst case, we'll make sure he has the recording, but.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Just drop the agenda in for you guys.

**Kyle Gaudreau:** This week was actually helpful, you know, for me to get up to speed more and more with Carry Out.

**Kyle Gaudreau:** It just, I used it as an opportunity for me to just dive in deeper and get more hands-on.

**Kyle Gaudreau:** And so I wanted to share just a few things I was seeing.

**Kyle Gaudreau:** Hopefully some of this is, I'm not being duplicative of anything we've talked about before, so please forgive me if some of that does come through, but tried my best to, like, comb through transcripts, get, like, pulse of date, like, where the conversations have progressed, and just, like, try to, like, relate that to some of the data I'm seeing.

**Kyle Gaudreau:** And so there's just a few things that kind of stuck out I would love your guys' take on.

**Kyle Gaudreau:** So let's jump into it.

**Kyle Gaudreau:** And so in terms of, like.

**Kyle Gaudreau:** Broader topics.

**Kyle Gaudreau:** Just want to, you know, go through a bit of, like, some of the performance things I'm seeing.

**Kyle Gaudreau:** Coming back to some of the discussion topics, we had some open items around the FAQ.

**Kyle Gaudreau:** just want to, like, make sure we're on the same page there.

**Kyle Gaudreau:** There's a few opportunities I just want to chat through around, like, per games and some potential PSEO opportunities.

**Kyle Gaudreau:** I've been playing around with the Amplitude Dash as well, and I just think, like, there's probably some views that could be helpful for us.

**Kyle Gaudreau:** So I just was curious to see how, like, process could work if we had requests and what that looks like.

**Kyle Gaudreau:** And we'd love to close the loop on the Roblox stuff.

**Kyle Gaudreau:** I realize, you know, some of the back and forth on the cost, and I just want to make sure, you know, we can find something to, I know you all have high conviction in that, and so I want to make sure we can be a good partner for you in helping realize that.

**Kyle Gaudreau:** So a few things on my mind, but anything outside of that you guys want to cover?

**Joel Murphy:** Yeah, I had one out.

**Joel Murphy:** I'm not sure where it would slot in here, but I was reviewing this week's article earlier in the week, and there were about five...

**Joel Murphy:** Some blurbs that kind of stuck out to me as like kind of didn't ring true for like our feature set for the product.

**Joel Murphy:** And I went to our product team like, hey, guys, like, is any of this like making sense?

**Joel Murphy:** And most of it wasn't.

**Joel Murphy:** And I went back to the articles just today to see if I could leave those comments there.

**Joel Murphy:** And then I was like, I don't know if these are different articles from what I'm looking at because I forgot to like mark that stuff in the docs earlier this week.

**Joel Murphy:** So I have the blurbs.

**Joel Murphy:** So I wanted to share those with you and just to provide the context that like I think it's AI hallucination about how the product works because it's just stuff Engine flatly doesn't do.

**Joel Murphy:** Yeah.

**Joel Murphy:** But also need help finding which articles those were in at this point because I've kind of lost my place.

**Kyle Gaudreau:** Yeah, I can have the team help us track that down a little bit.

**Kyle Gaudreau:** But I feel like you all mentioned something somewhat.

**Kyle Gaudreau:** In the last session, so it's like something just like bubbling up, we have to be careful of just like how do we reference the product?

**Joel Murphy:** Yeah, the last week was, it was kind of conflating groups and travel together.

**Joel Murphy:** I think we were kind of saying the group side did something that's more of a feature of the travel side.

**Joel Murphy:** This was more like, there was something in there about like real-time compliance tracking, I think is one of them, and almost like, like some sort of like proactive system for, it wasn't clear on what the compliance was, it's just something, like we don't have a real-time alerting system for anything that I can tell right now.

**Joel Murphy:** So it was more like, we just kind of made this up.

**Kyle Gaudreau:** Yeah, we'd love to see the examples we can take in and try to understand, you know, do we need to tweak this from an order?

**Kyle Gaudreau:** So Fathom standpoint, a prompt standpoint, you know, maybe there's things we can do in our fact-checking.

**Kyle Gaudreau:** It's an interesting challenge.

**Kyle Gaudreau:** You know, like something we're finding that's been an interesting pattern.

**Kyle Gaudreau:** We really started to pick up on it more and more with this engagement we're doing with augment code where we're just finding a lot of the language that we use is being actually like that.

**Joel Murphy:** Those specific phrases are being used within the outputs in LLMs, things like AI mode, chat GT, et cetera.

**Kyle Gaudreau:** And so it just makes me now think a little bit differently of like how to sometimes, you you have to like conventionally, it's like not being too forward with like your product in certain types of topics and, you know, being selective with that.

**Kyle Gaudreau:** And, you know, it's now making me think, hey, maybe, you know, maybe that still is true to a degree, but how we talk about the product...

**Kyle Gaudreau:** It was always important, but now even more important if that is going to get done by these alums.

**Kyle Gaudreau:** And so what you are then saying is even more critically important because we don't want to, you know, spread that in a way that could get messy.

**Kyle Gaudreau:** So, yeah, we definitely need to learn, like, why is that happening?

**Kyle Gaudreau:** How do we monitor it?

**Kyle Gaudreau:** How do we make sure it's like a repeatable fix?

**Joel Murphy:** So, yeah, we'd love to see the examples.

**Joel Murphy:** Yeah, think, do I have edit permissions on this Notion doc?

**Kyle Gaudreau:** Maybe I can just drop them in there at the end.

**Kyle Gaudreau:** You should be able to, to my knowledge.

**Joel Murphy:** Yeah, yeah, I can.

**Kyle Gaudreau:** Okay, I'll put them in there.

**Joel Murphy:** Yeah, perfect.

**Joel Murphy:** Appreciate that.

**Joel Murphy:** Yeah, man, but I mean, I'm totally aligned with you there.

**Joel Murphy:** mean, like, want to be specific about the product because that is what the answer engines prefer.

**Joel Murphy:** But at the same time, like, to your point of, like, almost explicitly what you say is, like, it just...

**Joel Murphy:** Parrot's that.

**Joel Murphy:** And, yeah, I just don't want to get into a situation.

**Joel Murphy:** I mean, it probably would be like a one-time thing as whatever happened, but some customer would be like, At OpenAI, I told me you had these proactive whatever the hell that thing was, and like you don't, you know, it's just like half a hundred times now.

**Kyle Gaudreau:** I was just talking about that at a recent happy hour with a founder I had bumped into, and they were talking about a similar issue.

**Kyle Gaudreau:** And I was kind of saying in jest of like, oh, we don't have that feature, but maybe now we probably should build that, because that sounds interesting.

**Kyle Gaudreau:** But, yeah, it's definitely an interesting challenge.

**Kyle Gaudreau:** What we can control is at least the words that we put out as much as possible, making sure they're accurate.

**Joel Murphy:** I think a decent working solution, barring some completely programmatic way of doing it is, you know, it's pretty easy for me at this point to, like, read through the articles.

**Joel Murphy:** Yeah.

**Joel Murphy:** So at one level of cognition, and then when I see something that's called out specifically about engine, you know, kind of shifting my focus more surgically on that stuff, picking it out, and then either finding the answer myself or going to the product team and then feeding that back to you guys.

**Joel Murphy:** And if you guys can take that feedback, and then I don't know what you do on the, you know, kind of the artifact side, but that's not all that cumbersome for me to do that.

**Kyle Gaudreau:** Okay, that makes sense.

**Kyle Gaudreau:** And I mean, theoretically, as we go through that motion, like, there should only be so much variability convention, right, of, like, common patterns we just need to watch out for that, you know, maybe there's an edge case or two that pop up.

**Kyle Gaudreau:** But, and yeah, I can make sure that for the team as well of, like, you know, basically what you just described is, like, when you see this, like, please make sure this is accurate.

**Kyle Gaudreau:** Flag it, et cetera, and then we can also do the same just to make sure you can help if we need an extra.

**Joel Murphy:** Cool, yeah, I'm kind of on the inverse of this point is I did leave a couple comments in a couple of the articles this week about being more specific, and the one that's jumping out at me right now was something about engine integrates with leading, you know, ERM software, and being more specific in those ways, like calling out what those are, so when that thing potentially does get picked up and it's parroted back, it's literally like a more complete answer than, yeah, we do it with somebody, but we're not saying that.

**Kyle Gaudreau:** Yeah.

**Joel Murphy:** ERM, what's ERM?

**Joel Murphy:** ERM, I had to look it up.

**Joel Murphy:** It was like employment, you know, hi, Bob, work, it was kind of like, you know, but I I

**Joel Murphy:** I've not referred to as ERM before, but I think that's what the article said.

**Kyle Gaudreau:** Maybe I'm hallucinating now.

**Kyle Gaudreau:** ERP?

**Kyle Gaudreau:** ERP, yes, ERP.

**Kyle Gaudreau:** Okay, it doesn't sound right.

**Joel Murphy:** You got it, Cole.

**Joel Murphy:** Thanks, Cole.

**Kyle Gaudreau:** I knew I had to be screwing it up somehow.

**Cole Parker:** It's close enough.

**Kyle Gaudreau:** Once you say work day, we all get it.

**Kyle Gaudreau:** Yeah, there's a lot of acronyms up there.

**Kyle Gaudreau:** It's all good.

**Kyle Gaudreau:** Yeah, no, I agree.

**Kyle Gaudreau:** It is another good example of, like, how that can get referenced and picked up.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Okay.

**Kyle Gaudreau:** Cool.

**Kyle Gaudreau:** Well, a few different performance things that I just wanted to jump into.

**Kyle Gaudreau:** You know, one of the things I'm just seeing now, digging our data a little bit more, is I just think we have an opportunity to address a few different data gaps, if you will, just to make it easier if we had the right pulse on our data.

**Kyle Gaudreau:** So that's something I'm work on with the team, and that kind of goes back to the amplitude.

**Kyle Gaudreau:** Two questions I have a little bit.

**Kyle Gaudreau:** Generally, I just think about this in a way of, like, what are the key questions that we should be asking each and every week?

**Kyle Gaudreau:** Do we have the right data to support that?

**Kyle Gaudreau:** So I think we have some of it, but there's a few cuts, I think, that would hopefully surface some unique trends, because essentially what I'm seeing is, you know, 3% up a week, relatively flat.

**Kyle Gaudreau:** Like, you know, we've had this kind of, like, spike in the past few weeks per day, and, you know, definitely seeing some signs that, like, hopefully this is, you know, some more growth to come.

**Kyle Gaudreau:** We did see impression spike last week.

**Kyle Gaudreau:** You know, the hope is, like, typically when you're early on and getting a lot of content out there, it's one of the first things we're looking at is, like, how fast is it getting indexed?

**Kyle Gaudreau:** Is it starting to compound impressions?

**Kyle Gaudreau:** That should be a trend to eventually start to lead to clicks.

**Kyle Gaudreau:** I think we're doing pretty good there.

**Kyle Gaudreau:** think we can be doing better in the trajectory, and so there's just a few things I'm trying

**Kyle Gaudreau:** Kind of think through of like, where can we focus?

**Kyle Gaudreau:** Where can we move the needle?

**Kyle Gaudreau:** From a new content standpoint, that's kind of where we're seeing that impression spike.

**Kyle Gaudreau:** Clicks certainly trending up as well.

**Kyle Gaudreau:** At this phase, I would like to see us like probably at a stronger clip in terms of like weekly clicks for new content.

**Kyle Gaudreau:** It's not bad to be clear.

**Kyle Gaudreau:** It's just, and this is very different from customer to customer.

**Kyle Gaudreau:** But generally, I just think about it of roughly around the three-month horizon is where we want to first see that like notable spike in traffic.

**Kyle Gaudreau:** And I think we're on that track, but in these next few weeks, we'll be telling for us.

**Kyle Gaudreau:** But I just want to make sure we're, you know, doing what we can to continue and build some additional momentum.

**Kyle Gaudreau:** I know we've been kind of like splitting our time across new and refresh, taking a look at some of the refreshes.

**Kyle Gaudreau:** And in like the aggregate, it's nothing to write home about.

**Kyle Gaudreau:** This isn't the most ideal way of looking at this.

**Kyle Gaudreau:** Because, you know, there's, like, varying published dates of when we refreshed it and things of that nature.

**Kyle Gaudreau:** But you just look at the total trend, it's relatively flat.

**Kyle Gaudreau:** I am curious to, like, get a sense of, it's just a little hard to get the data in the most ideal way of, like, does this look any different if we're looking at L1 referrals from a GSC standpoint?

**Kyle Gaudreau:** You know, nothing crazy.

**Kyle Gaudreau:** It's actually interesting, though, when you double-click underneath this, the one thing that did stand out is this refresh.

**Kyle Gaudreau:** This is, like, pretty dang good growth.

**Kyle Gaudreau:** It was refreshed on, it was published on August 1st, or refreshed on August 1st, and saw, like, a pretty healthy spike afterwards.

**Kyle Gaudreau:** I was taking a look at, like, you know, looking at Wayback Machine, trying to get a sense of, like, where it was before and where it is now.

**Kyle Gaudreau:** It looks like quite a bit was changed, you know, adding an FAQ, even some, like, formatting.

**Kyle Gaudreau:** And so, one, I'm curious if there's just anything we can learn for particularly how this refresh was approached versus others, but also I just think that there is, you know, taking this to some of our experience with RAMP, there's a lot of variance around per medium that we could probably go after.

**Kyle Gaudreau:** I, you know, try to go at an angle that makes sense if I just think about your audience, you know, I could see how, you know, that would be something top of mind, but what I think of as variance is like, you know, there's all this city and state level intent behind that, and so we did a lot of different things with the RAMP team to capture that, and it ended up, like, ranking pretty easily because a lot of the things we were competing with was, like, crappy government websites.

**Kyle Gaudreau:** So, I wonder if there's, like, a similar play here, but I'm also curious just to understand the relative value of the traffic.

**Kyle Gaudreau:** It's not always just a one.

**Kyle Gaudreau:** This session doesn't convert.

**Kyle Gaudreau:** We should look at that.

**Kyle Gaudreau:** But there is a play at the very least here of building topical authority that can help us elsewhere.

**Kyle Gaudreau:** So this is a pretty encouraging trend.

**Kyle Gaudreau:** This may be one of these things we've already flagged and talked about with you, but I think there is likely more we can do to capture some demand here.

**Kyle Gaudreau:** From a cohort standpoint, I mean, you know, relatively like just kind of holding flat in terms of the mix.

**Kyle Gaudreau:** Expensive financial management continues to be the biggest driver.

**Kyle Gaudreau:** Looking week to week, there isn't like an obvious like construction is driving like a healthy portion of this traffic.

**Kyle Gaudreau:** I think the construction intent is something like 35% of this or so.

**Kyle Gaudreau:** So, you know, maybe there's a focus there.

**Kyle Gaudreau:** Obviously, that's a key audience for you all.

**Kyle Gaudreau:** So, you

**Kyle Gaudreau:** You know, that makes some sense.

**Kyle Gaudreau:** But the one thing I have been kind of like curious in like thinking about this is like perhaps, you know, are we spreading ourselves a bit thin in terms of topics that we're covering?

**Kyle Gaudreau:** And would it be helpful to play some more like strategic kind of one of the questions I coming into this with a fresher perspective had been looking at?

**Kyle Gaudreau:** Generally, the way I like to think about this isn't a hard, fast rule, but like on two lanes, we have high conviction on for whatever reason that can be traffic, relative value to your business, some conversion metrics, whatever it may be.

**Kyle Gaudreau:** Focus on two of those lanes, you know, continue to make that repeatable, scale it, and then leave some room for like experimentation and some other pockets where we're just like less sure.

**Kyle Gaudreau:** Maybe some things bubble up and so, you know, I think we've been doing that too.

**Kyle Gaudreau:** But I think there's probably some focus, and so that's one of the areas I'm curious to dig more into the team, with the team, and understand this data at deeper level, of course, with your input as well.

**Joel Murphy:** Yeah, I like that approach.

**Joel Murphy:** I don't have, like, a, I don't know, a strong opinion on the general question about, you know, kind of more laser focusing on two lanes versus spreading thin.

**Joel Murphy:** And, like, immediately I don't know enough to, you know, say I think this versus that, but that sounds like a good plan to me just from a logical standpoint of nothing else.

**Kyle Gaudreau:** Yeah, because, you know, I mean, what, the, some of the reasons behind that, right, is, like, if we, it's not that there isn't value of planting a lot of different seeds across varying topics, but if we're not planting enough to meaningfully tell us something, we're not learning enough to help us figure out where to grow next, and so.

**Kyle Gaudreau:** I'm not saying that is where we're at, but that's one of the things I'm curious to understand as I dig in.

**Kyle Gaudreau:** I just want to make sure I'm careful with you all, and like we're building a plan that continues to help us grow.

**Kyle Gaudreau:** So those were some of key things.

**Kyle Gaudreau:** I'm curious, you know, just your perspective on the Pergium stuff.

**Kyle Gaudreau:** Again, you know, there's some state and city level things here.

**Joel Murphy:** I'm not sure if we ever showed this to you all, but we built this.

**Joel Murphy:** It would certainly probably be a different plan, but we built this basically like set up calculators, city, state level things.

**Joel Murphy:** Well, so we have our card product launching in January.

**Joel Murphy:** Waitlist comes in a couple weeks for existing customers.

**Joel Murphy:** I'm not sure if we, I feel like we have, but like I don't know for certain if we've talked about Rant being a competitor for that product.

**Joel Murphy:** But even if we did or we didn't.

**Joel Murphy:** And I think this type of stuff becomes more pertinent as we, you know, get closer to that launching that product because it's, it's very similar to the, you know, ramped business.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Cool.

**Kyle Gaudreau:** Well, there's definitely a lot of things we've learned through that that we can, we can experiment with you all.

**Kyle Gaudreau:** So, and I think there's an interesting flavor of how we layer in some of the, you know, you know, kind of more like blue collar skewing nature of this and kind of what does that mean?

**Kyle Gaudreau:** And, you know, actually mean for how we may adapt the place and some meaning.

**Joel Murphy:** Right.

**Kyle Gaudreau:** Yep.

**Kyle Gaudreau:** Cool.

**Kyle Gaudreau:** So, to some of the discussion topics, I recall us talking about this FAQ schema stuff you were going to look into just like, it didn't sound complicated at all, but just making sure we're set up in Webflow for that.

**Kyle Gaudreau:** So, um, I need to check in on the status of where the team's at and something like, like,

**Kyle Gaudreau:** This shouldn't be terribly complicated.

**Kyle Gaudreau:** I'm just not 100% sure.

**Kyle Gaudreau:** Like, it shouldn't be much longer and it should be simple for us, but I wanted to get a pulse check on that.

**Joel Murphy:** Yeah, so I did look into this.

**Joel Murphy:** And funny enough, I did discover an issue with our schema.

**Joel Murphy:** It was still referencing HotelEngine.com, which I was like, oh, okay, that's, you know, less than ideal.

**Joel Murphy:** So there is schema, like blog post schema in the blog post template with variables for publish date, title, all that kind of stuff.

**Joel Murphy:** I did add an open text field for FAQ schema, but before I kind of went any further than that, wanted to confirm, because I couldn't quite remember from last week, is that all you guys need is a place for it to go and then we just need to render it within the template or is it better, easier, more scalable, something like

**Joel Murphy:** Like that, if we built out an FAQ section that the schema came from the actual HTML markup with data attributes and stuff like that, so you didn't have to build out the JSON stuff and then paste it in there?

**Kyle Gaudreau:** That would probably be better.

**Kyle Gaudreau:** I can validate that with the team, but I don't see why that would be easier for us to kind of manage and just drop in.

**Joel Murphy:** Well, I'm looking at it for more of a long-term thing.

**Joel Murphy:** Let's say we wrote something this week and published it and we wanted to refresh it next September, and part of that was FAQs, and then we updated the body but then forgot to do the schema version of those things that's out of sync at that point.

**Joel Murphy:** So maybe from that alone might be worth just building the component that way.

**Kyle Gaudreau:** Yeah, that's a fair point.

**Kyle Gaudreau:** We can certainly, yeah, we can close.

**Kyle Gaudreau:** I mean, something that does ensure that if we are, if we have to come back and refresh that, whether it's refresh or added, it probably doesn't make too much of a difference, but yeah, you know, if we're getting into a potential scenario where we're forgetting to refresh and that's getting missed, that would not be ideal.

**Joel Murphy:** Yeah, especially all the LL stuff you talked about, right?

**Joel Murphy:** Like, it picks up an outdated FAQ and just commits it to super permanent memory and won't, you know, won't pick up the updated one because we, I don't know, I just don't want to deal with that, so.

**Joel Murphy:** Agreed.

**Joel Murphy:** Yeah, just let me know there.

**Joel Murphy:** We'll build out what's best.

**Kyle Gaudreau:** Okay, cool.

**Kyle Gaudreau:** One of the things that I saw that popped through is I was just coming through the transcripts is I saw we had been talking about some PSCO opportunities in the early days.

**Kyle Gaudreau:** You all were sharing some challenges around.

**Kyle Gaudreau:** And some potential indexation things amongst many other areas, I'm sure.

**Kyle Gaudreau:** I wasn't quite clear where some of that left off.

**Kyle Gaudreau:** I think some of that came through primarily during the Sprint phase.

**Kyle Gaudreau:** But I'm just curious if there's something here for us to help in some way.

**Kyle Gaudreau:** I have no doubt there is an opportunity there.

**Kyle Gaudreau:** It's just more I was less familiar if there was an intention behind us not focusing there.

**Joel Murphy:** No, there's not an intention.

**Joel Murphy:** It's more of like this stuff exists.

**Joel Murphy:** There's a ton of it and, you know, other  has come up and it's just felt a back burner.

**Joel Murphy:** But essentially it was there's all these pages.

**Joel Murphy:** They exist already.

**Joel Murphy:** And if I remember correctly from the couple conversations we had about it, it was about how do we get this stuff to index and rank, but do it in a way that we're not like unknowingly shooting ourselves in the foot.

**Joel Murphy:** But like what I want to release, I don't remember how many.

**Joel Murphy:** don't

**Kyle Gaudreau:** Was it a bunch, though?

**Kyle Gaudreau:** It wasn't like the, at least if the, if the cloud response on the transcript was accurate, it was like 4,000 to 7,000 range, if I recall correctly.

**Joel Murphy:** That's what I have in my head, but I swear I said that to James one day.

**Joel Murphy:** He's like, oh, it's only X, and I don't remember what X was, but it's what I would call a lot.

**Joel Murphy:** And if we just, like, try to ram them through to Google, it's like, it's just going to look like what it is.

**Kyle Gaudreau:** You certainly need to be careful.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** So just to make sure I'm understanding that correctly, these are pages that are actively published, just not indexed, and it's more about if we did a push, obviously, then it hits index, and a lot could hit the index at one time.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Got it.

**Kyle Gaudreau:** That's right.

**Kyle Gaudreau:** Got it.

**Kyle Gaudreau:** Yeah, I think it's worth exploring, because, you know, I just think, like, there's got to be some...

**Kyle Gaudreau:** there's got to be some quick wins in there somewhere as we're, you know, we're making some of this more like editorial, you know, repeatable engine here for pun not intended.

**Kyle Gaudreau:** You know, going back to kind of like my friend earlier, right, like two areas of like high conviction that we were spending on maybe that's largely like topical stuff and like what can we experiment with on the PSCO side and just see like does something bubble up?

**Kyle Gaudreau:** Does this, should this, should this be a heavier focus of ours because we're just finding some quick wins that are promising?

**Kyle Gaudreau:** And so that's where it came to mind for me.

**Kyle Gaudreau:** So would love to dig in more on that.

**Kyle Gaudreau:** I don't know.

**Kyle Gaudreau:** I don't know particularly what the actions look like yet, but certainly we can explore varying ideas.

**Kyle Gaudreau:** Did you have any strong?

**Kyle Gaudreau:** Hypotheses of, like, why it wasn't getting indexed?

**Kyle Gaudreau:** Is that, like, a function of, like, sitemaps or, like, where it is?

**Joel Murphy:** No, it's more like, hey, this thing happened before you got here, and can you figure it out?

**Joel Murphy:** Oh, I got it.

**Joel Murphy:** One of those.

**Joel Murphy:** Okay, cool.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Sounds good.

**Kyle Gaudreau:** Dang, we're already almost at time.

**Kyle Gaudreau:** In terms of ImpliDue-request, I can probably handle this async, but was curious, like, if it would be possible to just, I don't know if this is, like, thing with you, Joel, but to do, like, just, like, a quick live session.

**Kyle Gaudreau:** we can do that.

**Kyle Gaudreau:** Perfect.

**Kyle Gaudreau:** Yeah, I would just love to understand the data better.

**Kyle Gaudreau:** On the Roomblocks, SoW side of things, just want to close the loop on that.

**Kyle Gaudreau:** Like, totally understand, you know, one to make sure you're all feeling good about, like, the ROI.

**Kyle Gaudreau:** You know, was just curious to get the take of, like, you know, it seems like there's this perception of, like, hey, you know, that's an additional cost.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** We're hoping to be less expensive and like, are we getting enough value back?

**Kyle Gaudreau:** You know, I guess the way I want to just make sure it's clear is like, what we're really trying to do with that is like, how do we develop a repeatable cadence of like, of creating content that aligns to the right strategy for you all?

**Kyle Gaudreau:** And so it's not supposed to be just like a, hey, let's go heads down and do pure strategy work.

**Kyle Gaudreau:** It's more like, how do we create the repeatable engine for Roblox specifically?

**Kyle Gaudreau:** And, you know, part of that is the publishing of content.

**Kyle Gaudreau:** And so when I at look back at like, what hadn't happened to date with the engine, it seemed like we got to a pretty good cadence of publishing.

**Kyle Gaudreau:** But, you know, Cole, I, yeah, I'm just curious if you're, you're taking anything I can do to just make sure it like, it felt like you all had a lot of urgency around, you know, this initiative.

**Kyle Gaudreau:** And we want to be a good partner for you all to ensure, you know, on things that have high conviction on, we can help support you as well.

**Cole Parker:** So, yeah, there's definitely urgency on our part.

**Cole Parker:** I think we want to kick this off.

**Cole Parker:** As quickly as possible, I think just I was not included in like the previous discussions about what we're doing with you guys.

**Cole Parker:** So I've kind of been brought in and this is my first time going through an SoW with you guys.

**Cole Parker:** Just what isn't clear to me as I look at the deliverables here, it's like calibration content.

**Cole Parker:** says articles that set quality tone, blah, blah, blah, blah.

**Cole Parker:** Like there's no clear we will deliver X amount of articles per week if that is included in the sprint.

**Cole Parker:** So to me, it just seemed like 20K for, like I already know who our competitors are.

**Cole Parker:** We have a general voice.

**Cole Parker:** Like obviously that has to be built with templates that you guys would produce.

**Cole Parker:** And there's certain information that we have to give from our team to your team.

**Cole Parker:** But it just seemed a little steep on that front, not to discount the importance of strategy.

**Cole Parker:** But for us, it just seemed relatively high.

**Kyle Gaudreau:** Yeah, I mean, I appreciate the feedback.

**Kyle Gaudreau:** You know, the thing about...

**Kyle Gaudreau:** You know, competitive space and voice tone, whatever it may be.

**Kyle Gaudreau:** I mean, that's true for, like, any business we work with during these strategy sprints is they have some version of that.

**Kyle Gaudreau:** Really, it's about, like, how are we translating that down to things like artifacts, to a content strategy?

**Kyle Gaudreau:** And how are we then taking that and blending that with the content we're creating, continuing to refine those artifacts?

**Kyle Gaudreau:** That's essentially the process that helps us just, like, get to that repeatable bar of quality.

**Kyle Gaudreau:** It's actually intentionally broad in terms of number of articles, because what that can mean for each business is wildly different.

**Kyle Gaudreau:** Like, the purpose of the sprint is to go and say, hey, we have a relative understanding of, like, your strategy, your opportunity.

**Kyle Gaudreau:** Let's collaborate on, like, building what that looks like with you all and start to execute against that to a point where we all feel really, really confident.

**Kyle Gaudreau:** Like, now we feel like we have the plan for the ongoing effort.

**Kyle Gaudreau:** Let's

**Kyle Gaudreau:** And so, you know, it's also an opportunity for you all to opt out of this as well.

**Kyle Gaudreau:** And so, like, that's a, you know, hey, you know, this is like, given when it's in a relationship where we're already actively working, it's a little bit different, but that's usually how we think about the strategy sprint.

**Kyle Gaudreau:** And it's, you know, and actually, really, when you break down on a monthly basis, it is already kind of discounted from our usual work.

**Kyle Gaudreau:** But it's quite a bit of, like, labor intensive time for us just to, like, dial that in and get it going.

**Kyle Gaudreau:** But, you know, we break it down to, like, a number of articles that were done in the previous strategy sprint.

**Kyle Gaudreau:** I think we would be at a pretty healthy spot where, you know, we were averaging four articles a week during that time, from what I can gather.

**Kyle Gaudreau:** And, you know, us averaging five now is not that far off.

**Cole Parker:** Joel, what are your thoughts?

**Joel Murphy:** Is it worth doing strategy sprint only?

**Joel Murphy:** If we did that, Kyle, your professional opinion, would you feel good enough about handing off a client of yours that just did strategy and letting them run with that?

**Joel Murphy:** Or is that really not enough?

**Kyle Gaudreau:** It is absolutely doable.

**Kyle Gaudreau:** It's not what I would typically recommend for most of the situations we're in because typically the teams to work with wouldn't have the capacity to execute that from a week-to-week basis.

**Kyle Gaudreau:** But, you know, it is framed in the sense of like, even like the artifacts we use with a variety of different sprint clients and different initiatives they're doing along the edges, they leverage those artifacts and get some pretty good results out of them.

**Kyle Gaudreau:** Compared to what they were doing previously with AI.

**Kyle Gaudreau:** So there's value that comes out of the content that's produced, the strategy, et cetera.

**Kyle Gaudreau:** But the intention of it is really just to make sure we all feel really good about what we're building towards.

**Kyle Gaudreau:** And also you have that dedicated team that's helping build that and particularly focused on laying that right strategic foundation.

**Kyle Gaudreau:** We have done these, I think I might have shared this before, but we have done these with active accounts before.

**Kyle Gaudreau:** did this with the AirBite team where we've been working with them for a while.

**Kyle Gaudreau:** We did a strategy sprint, we uncovered new lanes and opportunities.

**Kyle Gaudreau:** We then brought that back to the team and they're executing upon that alongside what they were already doing before.

**Kyle Gaudreau:** And so that's why we had proposed this model essentially was the team can continue to operate and think about engine.

**Kyle Gaudreau:** you know, the strategy sprint team can particularly focus on like building that right foundation and scaling, making something repeatable from room blocks.

**Kyle Gaudreau:** And then, you know, both things can continue to execute in parallel.

**Kyle Gaudreau:** It doesn't mean to be clear that is the only path here.

**Kyle Gaudreau:** It's just one that we had found to be successful, and that's why we had led with that.

**Joel Murphy:** Yeah.

**Joel Murphy:** Yeah, I guess what I'm like, and I don't have the SoW in front of me, but I guess I'm looking for a spot where, like, we feel like the price is comfortable, you know, does that mean trimming some of the work out?

**Joel Murphy:** But does that trim of whatever those things are, does that, you know, are we setting ourselves up for suboptimally by doing that?

**Kyle Gaudreau:** Yeah, I mean, for me, like, the way I would, I would probably get more flexibility on, like, what comes out of the sprint and the cost of that ongoing engagement and, like, how we think about what you already are committed today with us is, like, how do we scope that in a way that, like, makes sense for you all, rather than just, like, 2x.

**Kyle Gaudreau:** Flexing what you pay today because we've added something else.

**Kyle Gaudreau:** I think that's where I can go to Marcel and team and get more flexibility on that.

**Kyle Gaudreau:** When it comes to the strategy sprint side, to my knowledge, I don't think we've ever gone below $20,000 on that.

**Kyle Gaudreau:** It's already worth discounting that.

**Kyle Gaudreau:** Because our average rate is going to be in that $15,000 range per month.

**Kyle Gaudreau:** And so, you know, strategy sprinting two months, you know, me going back and saying, hey, whatever it is, $15,000 or whatever, Marcel will probably balk at that a bit.

**Kyle Gaudreau:** But, again, not the only path of doing this.

**Kyle Gaudreau:** I just wanted to, like, make sure I close the loop because, you know, this is less of me trying to, like, pitch or whatever and more just, like, making sure we're a good partner for you all and executing on an opportunity.

**Kyle Gaudreau:** And so, you know, I'm happy to, if helpful, if you want to find time to talk through this more.

**Kyle Gaudreau:** Like, I can take that back and try to figure that out.

**Kyle Gaudreau:** But my intention is to stay here, just to make sure, you know, you're all feeling good about, hey, you have a cool opportunity in front of you and that you have a partner who can help you do that.

**Joel Murphy:** Cole, you think it warrants a conversation that we don't run out of time for, given that, you know, we're kind of tacking this on at the end of our normal stuff?

**Joel Murphy:** For sure.

**Kyle Gaudreau:** Yeah, I think with James, too.

**Kyle Gaudreau:** James and Colin.

**Cole Parker:** Cool.

**Cole Parker:** Yeah.

**Cole Parker:** I just think we need to make a shot, call a shot.

**Kyle Gaudreau:** So I will follow up with them.

**Cole Parker:** Okay.

**Cole Parker:** Obviously, around the James out of office.

**Cole Parker:** I think on Monday, Joel, fire up a discussion with the four of us or I'll just grab time for us and we do a 15-minute sync.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** All right.

**Kyle Gaudreau:** Cool.

**Cole Parker:** Appreciate it.

**Cole Parker:** And Kyle, if we could meet, we'll let you know.

**Kyle Gaudreau:** I'll have a discussion on Monday with them and then we can go from there.

**Kyle Gaudreau:** let We'll you know.

**Kyle Gaudreau:** uh

**Kyle Gaudreau:** We'll be able to find time.

**Kyle Gaudreau:** I would love to bring Marcel, if I can, into it.

**Kyle Gaudreau:** We're in the midst of fundraising right now, so his calendar is insane.

**Kyle Gaudreau:** But, yeah, I would love to just close the loop on this and make sure you all have some clarity.

**Kyle Gaudreau:** And, you know, would love to help on this just to make sure, again, we're a good partner for you.

**Joel Murphy:** Cool.

**Cole Parker:** Cool.

**Kyle Gaudreau:** Well, happy Friday, guys.

**Kyle Gaudreau:** Appreciate you going a bit over.

**Kyle Gaudreau:** Anything else comes up, let me know.

**Kyle Gaudreau:** But I'll have a bunch of things to catch up carrying when she's back next week.

**Cole Parker:** Cool.

**Cole Parker:** Thanks, Kyle.

**Kyle Gaudreau:** Appreciate you.

**Joel Murphy:** All right.

**Joel Murphy:** Take care, guys.

**Joel Murphy:** See you, guys.
