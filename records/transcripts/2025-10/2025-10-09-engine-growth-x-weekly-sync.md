# Engine <> Growth X - Weekly Sync

<metadata>
date: 2025-10-09
time: 18:30 UTC
duration: 35 minutes
organizer: team@growthxlabs.com
participants: Kyle Gaudreau (GrowthX), Carrie Chowske (GrowthX), Cole Parker (Engine), Kali Wootton (Hotel Engine), Rory Conroy (Engine), George Haikal (GrowthX), Darrell Etherington (GrowthX), Feyisayo (GrowthX), James Winter (Hotel Engine), Joel Murphy (Hotel Engine), Colm Shalvey (Engine)
fathom_recording_id: 93153679
fathom_url: https://fathom.video/calls/434915855
share_url: https://fathom.video/share/yKbYsnphJ2tPVhD6SN93xzgRx6AJhsVt
source: fathom
enriched_on: 2026-03-02 14:32 UTC
</metadata>

---

## Summary

GrowthX and Engine aligned on Q3 content performance, LLM visibility progress, and strategic initiatives to improve discoverability. Engine's content saw steady growth with expense/financial management and industry-specific content performing strongest, plus a notable uptick in Claude and Poe referral traffic. The team identified and prioritized three major workstreams: fixing persistent "Hotel Engine" branding confusion in source code and schema markup, building a glossary and industry-specific FAQ structure to improve visibility and create referenceable components, and developing a consolidated content strategy that incorporates Reddit research, emphasizes finance-related topics, and establishes clearer content categorization for measurement.

---

## Context

Engine is a travel expense management platform for construction, manufacturing, and hospitality teams. GrowthX has been engaged for roughly Q3 2025 as their content marketing partner, focusing on SEO visibility and LLM/AI visibility (AEO/GEO). The relationship involves weekly syncs to review performance data, align on content strategy, and execute on agreed initiatives. Engine rebranded from "Hotel Engine" to just "Engine" to broaden market positioning beyond hospitality, but that rebrand left traces in source code, schema markup, and other technical layers that are creating LLM confusion and reducing visibility in AI answer engines like Claude and Poe. Meanwhile, GrowthX is running a parallel study on AEO/GEO signals and building internal tooling around AI visibility measurement, making Engine both a client and a research opportunity.

---

## Relevance

**To GrowthX Delivery:**
- Engine's LLM confusion case study: proving that rebranding detritus in source code and schema markup negatively impacts LLM visibility even when user-facing text is clean. Direct relevance to CheckThat positioning and AEO tooling roadmap.
- Glossary + FAQ structure experiment: provides real-world test case for content hierarchy and referenceable components approach that GrowthX can document and apply to other clients.
- Reddit-derived content strategy: validates GrowthX's research method for identifying user intent signals outside traditional search; early signal of viability for AEO/GEO positioning.

**To CheckThat:**
- Engine seeing 8-10 percentage point jumps in LLM presence week-over-week suggests early-stage but real growth in AI visibility; good case study for CheckThat impact metrics.
- Discussion of Perplexity vs. ChatGPT visibility differences directly feeds GrowthX's parallel study on platform-specific signals affecting AEO visibility.
- iPollRank webinar on answer engine mechanics — Joel flagged this as valuable; Kyle should review to sharpen CheckThat feature roadmap around synthesization and search patterns.

**To GrowthX Business Development:**
- Engine has explicit quarterly OKR for LLM visibility and is motivated to execute. Multiple action items assigned with clear ownership. Low renewal risk; expansion opportunity if GrowthX proves ROI on glossary/FAQ approach.
- James Winter and Joel Murphy (both from Hotel Engine/Engine) are engaged; Cole Parker (Engine) involved for specialty (possibly room blocks/GEO work). Broadening buyer base within account.

---

## Overview

- Content performance shows steady growth in Q3, with expense/financial management content performing strongest
- LLM referral traffic growing, especially from Claude and Poe
- Plans to create a glossary and industry-specific FAQs to improve content structure and visibility
- Need to address lingering "Hotel Engine" branding issues in website code and content
- Developing a focused content strategy with emphasis on finance-related aspects and better categorization

---

## Key Topics

### Content Performance Overview

  - Steady growth in Q3, particularly in clicks
  - Expense and financial management content performing strongest
  - Growth seen in industry-specific content, technology solutions, and calculators/practical tools
  - Peruvian page with calculators showing good traction

### LLM Referral Traffic

  - Overall steady growth
  - Significant increase from Claude and Poe in the last week
  - ChatGPT remains dominant for Engine's customer base
  - LLM presence up \~8-10 percentage points from previous week

### Branding and Visibility Challenges

  - Confusion between "Hotel Engine" and "Engine" branding persists
  - Potential visibility issues due to inconsistent branding
  - Need to update source code, schema markup, and content to consistently use "Engine"
  - Fewer users searching for "Hotel Engine," indicating some brand recognition improvement

### Content Strategy Improvements

  - Proposal to create a glossary and industry-specific FAQs
  - Plans to structure content more effectively, possibly using Webflow CMS collections
  - Consideration of adding templates (e.g., travel policies) to complement content recommendations
  - Focus on finance-related aspects and consolidating content categories for better tracking

### AI/LLM Visibility Initiatives

  - Ongoing efforts to improve LLM visibility as part of quarterly OKRs
  - GrowthX working on comprehensive study of signals affecting AI/LLM visibility
  - Discussion of differences between various LLM platforms (e.g., Perplexity vs. ChatGPT)

---

## Action Items

**Joel Murphy (Hotel Engine)**
- Use Python script to search source code for remaining "Hotel Engine" references, remove/update in H3 headers, schema markup, and other hidden elements
- Check with Barry regarding refreshing "What is Engine" article; confirm no issues with tonality/content updates before proceeding
- Send iPollRank webinar guide on answer engines to Kyle Gaudreau and Carrie Chowske

**Carrie Chowske (GrowthX)**
- Finalize content strategy incorporating Kyle's Reddit research, finance-focused aspects, and category consolidation; share by next week's meeting

**Kyle Gaudreau (GrowthX)**
- Share early insights from GrowthX's AEO/GEO research study as they become available; prioritize findings that differentiate Perplexity vs. ChatGPT visibility

---

## Transcript
**Carrie Chowske:** This meeting is being recorded.

**Carrie Chowske:** Hey.

**Carrie Chowske:** How are you?

**Kyle Gaudreau:** Good, how are you?

**Carrie Chowske:** Working on a really nice headache.

**Carrie Chowske:** Other than that, I'm fine.

**Kyle Gaudreau:** Headache.

**Kyle Gaudreau:** Oh, no.

**Carrie Chowske:** Yeah, I don't know what's going on.

**Carrie Chowske:** We'll take some stuff after we're done with this meeting.

**Kyle Gaudreau:** Well, if you need to take it now, I mean...

**Kyle Gaudreau:** No, no, no, I'm fine.

**Kyle Gaudreau:** I get, like, bad migraines, so, like, as soon as I feel something, I have to, like, take it right away, or I can just get out of control, but I hope it gets better.

**Carrie Chowske:** Hey, Joel.

**Joel Murphy:** Hey, guys.

**Kyle Gaudreau:** How's it going?

**Kyle Gaudreau:** Good.

**Kyle Gaudreau:** How are you?

**Joel Murphy:** Not too bad.

**Kyle Gaudreau:** Good, good.

**Kyle Gaudreau:** Just you on your end today?

**Joel Murphy:** Most likely, yeah.

**Kyle Gaudreau:** Okay.

**Carrie Chowske:** Don't sound so excited to see us, Joel.

**Joel Murphy:** There's just a lot going on, and my head is spinning at the moment, so.

**Carrie Chowske:** I can feel like I'm really, well, we'll keep it, we'll keep it tight.

**Joel Murphy:** Yeah.

**Carrie Chowske:** Cool.

**Carrie Chowske:** So, we're doing fine on publishing.

**Carrie Chowske:** Thank you for getting back to us on those articles that you reviewed.

**Carrie Chowske:** Same stuff.

**Carrie Chowske:** We'll have some stuff ready, probably, probably publishing tomorrow.

**Carrie Chowske:** We just had to pause because we needed to commandeer our Webflow login for another client temporarily, but now we're ready to go ahead and publish, so I think we'll probably do that either today or tomorrow.

**Carrie Chowske:** And then in terms of performance, no new, like, no real revolutionary things to kind of go over this week, pretty similar to what we talked about last week.

**Carrie Chowske:** I did just go ahead and pull back so we could look at all of Q3 to kind of see, that's pretty much the length of the engagement you've had with GrowthX so far.

**Carrie Chowske:** So over that time, we've seen, you know, some pretty steady growth that, you know, we started out, these are impressions here, or I'm sorry, these are the clicks, these are the impressions, that's that drop off that we saw.

**Carrie Chowske:** So it's been pretty steady, we're up on clicks overall, which is nice.

**Carrie Chowske:** Impressions is about where it was, considering that drop, I'd call that, I'd call that a net win, tentatively, without doing any actual math, because I hate math.

**Carrie Chowske:** So I'm so glad all the, everything does it for me these days.

**Carrie Chowske:** So glad.

**Carrie Chowske:** Okay, and so we saw some pretty good growth too in some specific clusters. Same kind of things that we were talking about with these clusters, which will lead me into something related to where we'll kind of go forward with the clusters.

**Carrie Chowske:** But this expense and financial management is still the strongest in terms of the number of sessions, but also we're seeing pretty good steady growth there as well and pretty solid engagement.

**Carrie Chowske:** The other big, like, growth that we've seen, though, are in these other three areas, industry-specific content, this technology and software solutions, which I'm to look at what that was specifically from because that one actually surprises me a little bit, and then calculators and practical tools, and then also some steady growth in travel booking and reservations.

**Carrie Chowske:** We really aren't seeing any kind of substantial drop-offs in anything there.

**Carrie Chowske:** Cool.

**Carrie Chowske:** Same top page, so we're going to keep kind of playing with some of those other keywords that are related to some state-specific stuff.

**Carrie Chowske:** That's hard to say.

**Carrie Chowske:** And run a few more little mini experiments there, but over that, we've seen some pretty solid traction from that Peruvian page.

**Carrie Chowske:** That's the one that Barry worked on and has actual calculators in there with some additional features.

**Carrie Chowske:** So those are some things too that I think are proving to be pretty useful for you guys to include if you're talking about costs.

**Carrie Chowske:** So I might talk a little bit about how we can maybe work some of that in some of the content we're creating.

**Carrie Chowske:** And because it's not something that we can do on our end, but if you're able to, if you've got them as like components in Webflow, it be something I can easily add in.

**Joel Murphy:** I don't know if they are components.

**Joel Murphy:** I know that Barry told me he, you know, it's kind of vibe codes that stuff, which, you know, fine with me.

**Joel Murphy:** But I don't know if they're components or HTML one-offs or not.

**Carrie Chowske:** Yeah, it might be something to look at too.

**Carrie Chowske:** If we, you know, start looking at pages that we're letting sunset a little bit or kind of focusing on pages that are performing well, maybe he could.

**Carrie Chowske:** Maybe Barry would even want to go in and see if there's things like that that he can add that would even boost it further might be a good idea.

**Carrie Chowske:** I don't know.

**Carrie Chowske:** We'll see.

**Carrie Chowske:** And also, it's good timing, too, for DM stuff, because the government just updated that, even though they didn't change for 2026.

**Carrie Chowske:** People are probably going to be searching that, so I'm going try to get some of that published in the next few days.

**Carrie Chowske:** And then I did notice some pretty good, some interesting things kind of happening with the LLM referral traffic.

**Carrie Chowske:** So overall, nothing major kind of going on here.

**Carrie Chowske:** This is about where it was a couple weeks ago.

**Carrie Chowske:** Pretty steady growth overall.

**Carrie Chowske:** But in the last week, we saw some pretty big growth for Claude and Poe, which are, Poe, I don't think was on the list before.

**Joel Murphy:** Poe's newbie.

**Carrie Chowske:** Yeah, same.

**Carrie Chowske:** I hadn't seen that at all on here, and I don't see it very often.

**Carrie Chowske:** Across the other clients that I, I don't even know if I've seen it pop up.

**Carrie Chowske:** trying to think if I had.

**Carrie Chowske:** But.

**Carrie Chowske:** But typically what we're seeing, and I've noticed this just as a trend with similar customer bases, the more blue-collar type stuff tends to be more present on ChatGPT.

**Carrie Chowske:** And if you look at, you know, this overall number of sessions, that's pretty clear that's what's going on for you as well.

**Carrie Chowske:** But it's just interesting to see this growth in these other areas.

**Carrie Chowske:** So might keep an eye on that to see, but it's the same kind of strategy either way in terms of what we're looking at to, you know, increase the visibility on those.

**Carrie Chowske:** Which, if you look at this, these top level numbers, these didn't really change.

**Carrie Chowske:** But we did see these kind of uptick in presence going up a little bit.

**Carrie Chowske:** went up about 10, I think about 8 percentage points there.

**Carrie Chowske:** And then on position, it went up a little bit as well.

**Carrie Chowske:** So 62% over the last three months.

**Carrie Chowske:** But also, I think this is up another like 8 to 10 percentage points over just the numbers that we talked about last week.

**Carrie Chowske:** So it's continuing to grow.

**Kyle Gaudreau:** Okay, got it.

**Kyle Gaudreau:** Joel, just wanted to follow up on what I was kind of flashing before with playing around with perplexity, and a few things kind of stuck out that I think we can play around with.

**Kyle Gaudreau:** So what was a little bit different than what I had showed you before in that, I've been playing around with different things, like going after particular personas and then trying to see what comes together.

**Kyle Gaudreau:** it comes out of that.

**Kyle Gaudreau:** In this case, I've had a bit more of a broader perspective across your personas, went through a similar exercise of identifying the subreddits and threads, and it basically helped us pull together this table.

**Kyle Gaudreau:** And so I just wanted to walk through a few things that I saw between this and just doing like manual checks myself.

**Kyle Gaudreau:** You know, some of this I think is probably like things like we know this to a degree, this is why the engine is what it

**Kyle Gaudreau:** Engine is, and, you know, validating in that respect.

**Kyle Gaudreau:** But these were some of, like, the high-frequency things that we saw come through.

**Kyle Gaudreau:** You know, things like challenges booking for larger teams, things of that nature.

**Joel Murphy:** Like, no surprise there.

**Kyle Gaudreau:** Perview came up, like, a pretty decent amount.

**Kyle Gaudreau:** Connected back to what we were kind of just talking about, you know, previous to this in the past couple weeks.

**Kyle Gaudreau:** There was a decent amount of, like, comparison.

**Kyle Gaudreau:** Comparison questions that were coming through.

**Kyle Gaudreau:** And if I'm not mistaken, I meant to check this, but I didn't validate.

**Kyle Gaudreau:** I don't think you all have really done much on the comparison side, right?

**Kyle Gaudreau:** I know, you know, company to company, like, this is always a, you know, there's differing opinions or whatever.

**Kyle Gaudreau:** But it's just, there's different tactics of, like, how to think about this, how to tackle it, doing, you know, it doesn't have to be bashing your competitors.

**Kyle Gaudreau:** But it's just clear, like, there's a lot of questions.

**Kyle Gaudreau:** It's up there.

**Kyle Gaudreau:** It ties in with the way LLMs are going to talk about, you know, the varying solutions.

**Kyle Gaudreau:** So I think it's a thread to pull on a little bit just to experiment with of like, what would that look like?

**Joel Murphy:** Yeah, I agree.

**Joel Murphy:** I mean, I like the stuff that you guys sent over in the last, I don't know if it was just this week or the last two weeks, but there was some like comparison, but it wasn't, it wasn't competitive bashing.

**Joel Murphy:** Yeah, was more like, engine does this, and you should check to see if your platform does.

**Joel Murphy:** know, so I like that approach.

**Kyle Gaudreau:** It's pretty, honestly, I like being more aggressive than that, but I like that approach because it invites less scrutiny from people.

**Kyle Gaudreau:** Yeah, it's generally been my mindset with this stuff.

**Kyle Gaudreau:** And so, yeah, I think there's some things we can explore there.

**Kyle Gaudreau:** Additionally, you know, just, just around like, there's a lot of like,

**Kyle Gaudreau:** Industry-specific questions, again, I wouldn't say that's like a surprise, a common thread through this was, it just feels like there's an opportunity for us, and I'm thinking through this a little bit and want to chat through it with Carrie, of like, going after the varying jobs to be done, related things that people are searching for, that is broader than just like booking your travel.

**Kyle Gaudreau:** And I realize we already do some of this today, don't get me wrong, but it just, that was a common thing I was seeing, you know, just the different apps and best practices and all the different things they're like thinking about, and just, you know, how can we frame engine as an authoritative source for, you know, construction teams, manufacturing teams that are, you know, travel is a part of what they're operationalizing and what are all the different like key things that go into that.

**Kyle Gaudreau:** And so, again, I know we kind of do that to a degree, but I think there is an opportunity to lean into that more heavily.

**Kyle Gaudreau:** The other thing I was noticing, maybe you've seen this a decent amount, just seeing a lot of like

**Joel Murphy:** Confusion over engine's branding.

**Joel Murphy:** my hunch is that this is actually hurting your visibility.

**Joel Murphy:** Yeah, I've been thinking about this from a couple angles.

**Kyle Gaudreau:** The one you've notated here that's like Hotel Engine versus Engine thing.

**Joel Murphy:** And the what is engine post that Carrie and I talked about last week actually has a call out for, yeah.

**Joel Murphy:** So I thought like, okay, that's probably a good idea.

**Joel Murphy:** Here's the other angle was our charge card product is called Nginx.

**Joel Murphy:** And it's spelled differently than the server configuration Nginx, but they sound exactly the same.

**Joel Murphy:** I was like, I introduced some weird issue in this in the same kind of way.

**Kyle Gaudreau:** That's a good point.

**Kyle Gaudreau:** Well, I think there's a few things we can do perhaps.

**Kyle Gaudreau:** But yeah, like I was even seeing for some of this comparison stuff that I had to scrub out.

**Kyle Gaudreau:** So like it was even comparing Nginx to like Hotel Engine as like a.

**Kyle Gaudreau:** And I was just like, that's clear to me, like, the LLM doesn't get it.

**Kyle Gaudreau:** And so, like, that's going to manifest in varying ways, right?

**Kyle Gaudreau:** So, like, I did find, like, I was just trying to find where some of this could come from outside of what you mentioned.

**Kyle Gaudreau:** It does look like it's probably hiding out in your source code in varying places.

**Kyle Gaudreau:** Like, this is an H3 that, like, isn't actually being shown on a page, but, like, I can see it in the source code when I look at pages, like, the customer success.

**Joel Murphy:** Oh, that's a good find.

**Joel Murphy:** I'll tell you, another place where it's probably historically coming from is all our schema markups said Hotel Engine and HotelEngine.com until two or three weeks ago.

**Kyle Gaudreau:** Okay, got it.

**Kyle Gaudreau:** Do you have organization schema in place already? Because that was another thing I was thinking just to tackle, just to make sure it says engine versus Hotel Engine.

**Joel Murphy:** We do. And I noticed that when we started talking about schema for the posts themselves, I was like, what's there? It all says Hotel Engine.

**Kyle Gaudreau:** That's not good. So, yeah, I changed it all.

**Carrie Chowske:** Okay, good, good, good.

**Carrie Chowske:** Do you want some good news, though?

**Carrie Chowske:** Fewer people, like a few months ago when I was pulling some GSC data, like looking at the queries and stuff, like fewer people are getting to your site by searching Hotel Engine.

**Carrie Chowske:** So that means that they're recognizing if they're doing a branded search, you're getting more for Engine than you are for Hotel Engine, and Hotel Engine ones are declining.

**Carrie Chowske:** So it's a small, bright spot, but also means we need to double down on it, make sure that everything's good so that people can find you if they are searching Hotel Engine, but that they hopefully make them not search that anymore.

**Joel Murphy:** Cool.

**Joel Murphy:** Just a quick aside on this note.

**Joel Murphy:** So Barry was sharing some negative threads on Reddit about Engine, and they're all from what we call the supply side, so like hoteliers talk.

**Joel Murphy:** Hey, do you guys get bookings from Hotel Engine?

**Joel Murphy:** It's like two, three-year-old threads or whatever.

**Joel Murphy:** And he was kind of like, oh, this is super negative, super bad.

**Joel Murphy:** And we were saying like, well, you know, customers probably don't come across this.

**Joel Murphy:** But funny enough, there was one guy going through all of these threads and calling us Hotel Engines, plural.

**Joel Murphy:** And it's like 90% of the negativity is from this one dude who doesn't even have the name right. This is a dead giveaway that this is, at best, one person with a grudge, or at worst, someone trying to sully the brand on Reddit.

**Joel Murphy:** So I don't know.

**Joel Murphy:** It just, I thought it was funny.

**Kyle Gaudreau:** That stuff is annoying.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** I came across certainly varying references of you all.

**Kyle Gaudreau:** Some positives for sure.

**Kyle Gaudreau:** I'd say like largely positive, actually.

**Kyle Gaudreau:** I found somewhere it was like old employees or maybe it was the buried thing you were mentioning before, just like mentioning Engine in varying places.

**Kyle Gaudreau:** So yeah.

**Kyle Gaudreau:** So basically what this breaks down is just like some of the common themes, and this is basically sorted by the amount of threads and upvotes and comments we found, and so higher up is the most engaged.

**Kyle Gaudreau:** So, you know, one of the things I think just more broadly out of what I mentioned before up here that I was thinking about was, again, like we're seeing just some clear trends around industries, which is no surprise.

**Kyle Gaudreau:** I know you guys have this FAQ section.

**Kyle Gaudreau:** I'm just thinking of a potential idea of like, how could we almost think of an FAQ section similar as like a glossary in a sense?

**Kyle Gaudreau:** And so maybe there's an opportunity to create more structure underneath this, and then it would be like construction, focus, frequently asked questions, manufacturing, et cetera.

**Kyle Gaudreau:** There's different ways we could kind of like play around.

**Kyle Gaudreau:** And so I think there's an argument to be made where that just kind of lives here and that can have value and perhaps drive some visibility.

**Kyle Gaudreau:** I was thinking of an additional idea, though, that we could consider where if those are structured in a referenceable component, we could also reference those in relevant posts.

**Kyle Gaudreau:** And, like, there's an argument to be made of, like, well, that's duplicate content.

**Kyle Gaudreau:** But usually duplicate content doesn't matter at that.

**Kyle Gaudreau:** Like, when it's only, like, a small subset of what is being referenced in multiple pages.

**Kyle Gaudreau:** It's more, like, looking at totality of a page and how, like, similar is it.

**Kyle Gaudreau:** And so the thought being is, like, you know, just creating this kind of, like, weaving of, you know, it could be even a phase test.

**Kyle Gaudreau:** Like, it could be something we test, like, does it drive visibility here?

**Kyle Gaudreau:** And does it help visibility on, like, some of the individual pages that we reference it?

**Kyle Gaudreau:** It doesn't have to be just all one big project. Nonetheless, I think it could be an interesting thing to experiment with — what do we do with all these different questions, and how do we surface that in some meaningful way on the website?

**Joel Murphy:** I like the idea, and in fact, it's something I was going to talk to you guys about, because when I was at Dio, we did a glossary, and it performed really well.

**Joel Murphy:** I'll link you to it, and somebody wrote an article about it and how it performed, and I'll send that to you, but I was thinking, like, hmm, maybe that's something we could do here.

**Joel Murphy:** So, like, I like the idea for sure.

**Joel Murphy:** Also, as soon as you said this, I thought it would be pretty easy for us to create a CMS collection for this to make it easier than working with FAQ things. What you can do in Webflow is dynamically pull from that CMS collection and specify the specific entry you want to include.

**Kyle Gaudreau:** That's where our case studies work.

**Joel Murphy:** So we could do that in fairly simply.

**Carrie Chowske:** That solves kind of the problem, too.

**Carrie Chowske:** We were talking about doing something like that anyway. A CMS collection approach gives us the benefits of something we can easily add to and expand over time.

**Joel Murphy:** Yeah.

**Joel Murphy:** I mean, honestly, reading some of the content you guys sent over in the last couple of weeks, there's a lot of defining certain things, which is exactly what we did at Dio — defining all this technical stuff that people don't really understand clearly.

**Kyle Gaudreau:** I think it can be helpful, too, to start to like, as any website kind of matures and has more content, to just have very clear, like, this is where this type of content should live, this type of intent should live.

**Kyle Gaudreau:** And so, as we think about it.

**Kyle Gaudreau:** From a glossary standpoint, as we are going to define something that is a better fit for the blog, and it can be also like, okay, within that, what I've seen some glossaries do effectively is not only define something, but like, why is this important to, you know, the audience and your product and like doing something that's a bit more of an added angle.

**Kyle Gaudreau:** And that can open up particular subjects where you're going to talk about something more deeply, which then is a better fit for like the guide section, right?

**Kyle Gaudreau:** And so then it creates just this nice, like, you can link between the two, they have, it provides us more clarity of like, what are we like executing on and why and how much headroom there is and measuring it in different ways.

**Kyle Gaudreau:** And so I've just found that typically just beneficial for a whole host of reasons.

**Kyle Gaudreau:** So I do think it makes sense to like consider a glossary and we can certainly do some research around that.

**Kyle Gaudreau:** And yeah, additionally, like what I hadn't thought of here from like FAQ.

**Kyle Gaudreau:** It could maybe be blended into it, but it also could be similar.

**Joel Murphy:** I don't know.

**Joel Murphy:** Cool.

**Joel Murphy:** Another thing we did at Dio was job description templates.

**Kyle Gaudreau:** Dio is an HR platform. There was a decent amount of job-related content coming through in my research, and I almost removed it. But it did keep coming up in varying places, so there seems to be real demand there.

**Carrie Chowske:** Yeah, we've had a piece in production for a while that I haven't moved forward with because I wasn't sure where to go with templated content — I think it was expense-related. I'd have to look for it, but I can send it over. The issue we're having on our end is making sure that we can do templates at scale while keeping them branded and not looking like junk. That's where I paused, but if that's a priority, we can dig into it.

**Joel Murphy:** Yeah, so what I was thinking was, for Engine, the template idea works like this: we create content saying "your travel policy should spell out X," and then provide a downloadable template. So instead of job descriptions, it's templates for travel policies, expense frameworks, best practices for construction or manufacturing teams. Templates that connect back to what we're recommending in the content.

**Kyle Gaudreau:** That makes sense.

**Kyle Gaudreau:** Yeah.

**Joel Murphy:** Yeah.

**Carrie Chowske:** That's something we can work with.

**Kyle Gaudreau:** So a few different things here. Basically, next steps outside of the FAQs: Carrie and I are putting our heads together on a few different focus areas strategically.

**Kyle Gaudreau:** We're going to leverage some of this to inform that to a degree.

**Kyle Gaudreau:** There will be some experiments that come out of this, but essentially I want to get us to a layer of focus that helps figure out where our bets are for the next couple of months. We'll layer in experiments, get your feedback, and measure specifically against those outcomes. That could be focusing on construction, or whatever makes the most sense. We'll take some of this research, weave it into the strategy, and include it in the agenda for you.

**Joel Murphy:** Just keep me posted on what you need from us. If we want to do the glossary or templated content, I have an OKR for continually improving LLM visibility this quarter.

**Kyle Gaudreau:** There's no problem for us to take that work on. Outside of that, I'd recommend doing a scrub of your source code for any remaining "Hotel" Engine references.

**Joel Murphy:** We've got a Python script that extracts all the content and searches through it. I think we did that for Hotel Engine, but it probably just catches rendered copy within components, not hidden source code.

**Kyle Gaudreau:** Right. When I do a quick control F on the pages, I'm not finding it, but when I look at the actual source code, that's when I see it.

**Joel Murphy:** Yeah, we'll figure it out.

**Kyle Gaudreau:** It's not certain that LLMs are seeing the hidden source code, but it was happening frequently enough that I wanted to flag it. What are ways we can control around this?

**Joel Murphy:** Yeah, I hear you.

**Joel Murphy:** But honestly, I mean, for no other reason than to me, it's just annoying.

**Joel Murphy:** Like, you rebranded and you didn't do a thorough job.

**Joel Murphy:** That irritates me.

**Joel Murphy:** Yeah.

**Kyle Gaudreau:** The stakes are different nowadays, right? It used to be just the obvious checks that show up in search engines, but now this stuff is sticky in LLMs.

**Joel Murphy:** Yeah, exactly.

**Joel Murphy:** And if I don't remember to fix this, we're going to be battling it for years if we're not careful.

**Joel Murphy:** So yeah, I mean, exactly.

**Joel Murphy:** Well, yeah, I'll take a look at that.

**Carrie Chowske:** I remember trying to add someone to Slack and I sent it to the Engine email, but Joel was like, "No, you need to use the Hotel Engine one."

**Joel Murphy:** It's the most annoying thing ever. I go to log into something, put the wrong email address, and get a new account created.

**Kyle Gaudreau:** It's really the worst thing.

**Carrie Chowske:** We shouldn't talk. We have the same issue with "growthx labs" in some of our emails. I've been here so long my actual email is growthx.labs, which creates all sorts of weird issues. I have it as an alias, but it's not my primary one.

**Joel Murphy:** The Hotel Engine email is actually the alias at this point, but it's the one we use to log into almost everything.

**Kyle Gaudreau:** That's exactly the same situation.

**Joel Murphy:** So it's backwards, man.

**Carrie Chowske:** At least it might make it harder to hack if people can't guess your email address.

**Joel Murphy:** SDRs are pretty good at figuring that stuff out anyway.

**Carrie Chowske:** True, true.

**Carrie Chowske:** In line with that.

**Carrie Chowske:** So here's what I was going to suggest then on that what is it.

**Carrie Chowske:** Because we have two what is engine articles, and the one is pretty outdated.

**Carrie Chowske:** My suggestion would be to maybe get rid of that one and do a redirect to the newer one, and we should just refresh that newer one.

**Carrie Chowske:** That's my guess.

**Carrie Chowske:** That way we're not, like, it's not confusing things.

**Carrie Chowske:** It's not, you know, it's just one article for both, and we can still maybe get the traffic of the original one.

**Carrie Chowske:** Because they're not, like, the newer one is coming up more often, is from what I'm seeing.

**Carrie Chowske:** I'm seeing it as having more traction in any way, so.

**Joel Murphy:** Okay.

**Joel Murphy:** Yeah, I'm just looking at the post in Webflow.

**Joel Murphy:** So Barry created that latest one there.

**Carrie Chowske:** And I'm just suggesting, too, like, going through it.

**Carrie Chowske:** What I was going to do was, like, run it.

**Carrie Chowske:** I'm incorporating your feedback and tonality analysis to make sure we're addressing the points of confusion and terminology, hitting all the points we want to hit, and creating a good foundation from there.

**Joel Murphy:** Yeah, so I'm good with redirecting that old one to this one.

**Joel Murphy:** Before we update it, let me check with Barry since he created it. I want to make sure he didn't have some other logic behind how it's written that I should know about before we freshen it up with this tonality work.

**Carrie Chowske:** Yeah, gotcha.

**Carrie Chowske:** Okay, not a problem.

**Carrie Chowske:** Yeah, let me know, no problem.

**Carrie Chowske:** I've put together a preliminary content strategy, but we're going to incorporate Kyle's Reddit research and finalize it. I think we should really focus on finance-related aspects and make sure we have a solid foundation there. We also need to consolidate how we categorize things so we can better track what each piece of content is doing. There'll be some experiments too, but we should have it finalized by next week.

**Kyle Gaudreau:** It seems like AEO/GEO is more and more on the team's mind. Is there anything else you all are thinking about? I'm curious if there are dots to connect where we can help you.

**Joel Murphy:** Honestly, I don't know why they asked for it specifically. I'm guessing because Cole was involved it had to do with room blocks stuff, but I'm not sure. It's not on the team's mind as much as it should be. It's really just James and I trying not to get behind the eight ball with this.

**Joel Murphy:** Like, we know that it's a small driver right now, but it's not always going to be the case.

**Joel Murphy:** And I just want to keep pushing in the right direction.

**Joel Murphy:** And, you know, up and to the right doesn't have to be drastic as long as we're moving in the right direction.

**Joel Murphy:** That's really what I care about.

**Joel Murphy:** And whatever we need to do to get there is cool with me.

**Joel Murphy:** You know what I mean?

**Joel Murphy:** The good news is almost anything works at this point. I'm really the one beating the drum here. Frankly, a lot of people don't even understand AI yet.

**Kyle Gaudreau:** I'm trying to be a driver and socialize this stuff. I dig it.

**Kyle Gaudreau:** In the background, by the way, we are working through a study now that's going to be pretty comprehensive of, like, what are the signals we can see that, from a data-driven standpoint, are actually positively affecting AEO, GEO.

**Kyle Gaudreau:** We're also incorporating this into just, like, a larger product we're working on in a variety of ways.

**Kyle Gaudreau:** Like, for us, like, this is, like, our number one right now is really, like, winning and getting ahead on this space.

**Kyle Gaudreau:** We see a lot of opportunities where existing AI visibility tools show basic things but don't connect the dots to action well, and they don't drive insights in a meaningful way. We're working on things we'll roll out to customers in the coming months. Early research is part of that process, and as insights come out, I'll share them because this feels like a gap in the market right now.

**Joel Murphy:** Yeah, agreed.

**Joel Murphy:** I mean, couldn't agree more.

**Joel Murphy:** Glad you guys are working on that.

**Joel Murphy:** Excited to see more.

**Joel Murphy:** Are you guys familiar with a company called iPollRank?

**Joel Murphy:** Have ever heard of them?

**Kyle Gaudreau:** I've definitely heard of it.

**Kyle Gaudreau:** Oh, I think I was following one of the guys.

**Kyle Gaudreau:** I can't remember his name now, but I saw some of his content on LinkedIn.

**Joel Murphy:** Yeah, so I sat through a webinar a couple months ago and they had a comprehensive guide on how answer engines work. It starts from traditional search and goes deep. It helped me understand how these things work and made me realize that existing tools show you some things but not enough real insights.

**Joel Murphy:** I'll pass it along.

**Joel Murphy:** You might find it helpful, but it was specifically like the differences between them, you know, like how they synthesize, how they search.

**Kyle Gaudreau:** Oh, like Perplexity versus ChatGPT? Yeah, because Perplexity tends to be closer to typical Google search results, but that will probably change. There are nuances there I'd want to understand better. This stuff is changing so fast.

**Joel Murphy:** I'm always anxious to deepen my knowledge. I'd love to check it out. I'm reading it when I have time, but I don't have much time.

**Kyle Gaudreau:** If there's anything else we can help take off your plate, let us know. We'll be putting our heads together on strategy and weaving in a good amount of AEO/GEO work into it.

**Joel Murphy:** Cool.

**Joel Murphy:** Sounds good.

**Kyle Gaudreau:** All right.

**Carrie Chowske:** Okay.

**Joel Murphy:** Talk to you next week.

**Kyle Gaudreau:** Appreciate it. Bye.
