# Otto <> Growth X - Weekly Sync

<metadata>
date: 2025-12-11
time: 19:00 UTC
duration: 31 minutes
organizer: jakub@growthxlabs.com
participants: Bailey Seybolt, Jakub Rudnik, Jason Flateboe, Michael Gulmann
fathom_recording_id: 108155387
fathom_url: https://fathom.video/calls/502593202
share_url: https://fathom.video/share/NxTsoWM7f9eLyqoxtrnWwfeEd8isrx-y
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

GrowthX reviewed Otto's content and organic visibility progress one month into launch. The blog showed strong early signals: 40 articles published in 6 weeks with 100% MoM impression growth and clicks increasing from 11 to 50. Jakub presented a metrics framework for monitoring content health across three phases (publishing mechanics, keyword rankings, traffic & conversions), confirming Otto is solidly in phase 1-2. Key action items include monitoring Webflow's sitemap update cadence, implementing FAQ schema, adding a sticky CTA button to the blog template, and exploring inline CTAs and video embeds to boost engagement as traffic scales.

---

## Context

Otto, an emerging AI agent company, is one of GrowthX's content marketing clients. This is an internal GrowthX check-in with Bailey Seybolt (GrowthX Delivery) and Jakub Rudnik (GrowthX SEO), reviewing progress on Otto's content and organic visibility strategy. Jason Flateboe represents Otto and handles implementation on their Webflow site. The meeting serves as a monthly checkpoint to assess publishing velocity, technical health (indexing and sitemaps), search performance metrics, and organic traffic growth. Michael Gulmann (Otto) was invited but did not attend; results would be shared afterward.

---

## Relevance

**To GrowthX Delivery:**
- Webflow sitemap update cadence is critical to monitor; if slow, may require override solutions or third-party tools. This is a potential client-side blocker for future indexing.
- Content pipeline issue (product features error) flagged; Jason traveling this weekend may delay article delivery until Monday (minor impact, pre-communicated).
- FAQ schema implementation approach will rely on template-level changes in Webflow; confirm with ops if lift is acceptable before committing to timeline.

**To GrowthX Business Development:**
- Otto showed strong execution velocity: 40 articles in 6 weeks (15 Nov, 13 Dec) with healthy content operations and no residual indexing issues post-robots.txt fix.
- Early customer success signals: +100% impressions MoM, 11-50 click growth Oct-Nov, +200% Page 1 keywords on Ahrefs, LLM referral traffic already visible in GA4.
- Launch momentum: GeekWire press coverage drove hundreds of signups; Otto is now in general availability post-closed beta.

---

## Overview

- **Strong Early Signals:** The blog shows healthy growth, with impressions up 100% MoM and clicks increasing from 11 to 50. This broad traction across many articles is a strong indicator of future traffic potential.
- **Indexing Health Check:** A few articles are not indexing. This requires monitoring to confirm Webflow's sitemap updates are timely and prevent a recurrence of the initial `robots.txt` issue.
- **FAQ Schema Implementation:** GrowthX will investigate implementing FAQ schema for the blog, which is expected to be a low-effort change in Webflow that can improve search visibility.
- **Future Growth Tactics:** Key tactics for when traffic scales include adding a sticky CTA button, inline CTAs, and embedding relevant videos to increase conversions and engagement.

---

## Key Topics

### Content & Indexing Health

  - **Publishing Velocity:** High, with \~40 articles published in the first 6 weeks (15 in Nov, 13 in Dec).
  - **Indexing Issues:**
      - **Resolved:** The initial `robots.txt` issue is fixed; two straggler articles were manually submitted and are now indexed.
      - **New Concern:** Four recent articles are not indexed.
          - One (12/4) is in the sitemap.
          - Three (12/10) are not yet in the sitemap.
      - **Action:** Monitor Webflow's sitemap update cadence. If it's slow, GrowthX will research options to override it.

### Performance Review

  - **Site-Wide Metrics (GSC):**
      - Impressions: +100% MoM (Nov vs. Oct).
      - Traffic: Flat MoM.
      - **Note:** A large traffic spike was from a GeekWire press article, not organic growth. This will be filtered from future reports to ensure accurate SEO attribution.
  - **Blog-Specific Metrics (GSC):**
      - Organic Clicks: 11 (Oct) → 50 (Nov).
      - Impressions: Strong growth, driving most of the site-wide increase.
      - **Insight:** Clicks are distributed across many articles, signaling broad content health rather than reliance on a single viral post.
  - **LLM Visibility:**
      - Attributable referral traffic from ChatGPT is growing.
      - Citations (tracked via Scrunch) are also growing, though from a small base (1% of tracked content).

### Future Growth & Conversion Tactics

  - **Sticky CTA Button:** Add a universal, sticky "Sign Up" button to the blog template (e.g., in the right sidebar).
      - **Rationale:** A proven tactic for driving user sign-ups from blog traffic.
  - **Inline CTAs:** Embed specific, context-relevant CTAs within article bodies.
      - **Rationale:** More effective for conversion than a generic footer CTA.
      - **Implementation:** Use Webflow shortcodes for easy integration by writers.
  - **Video Integration:** Embed relevant videos (e.g., product demos) into blog posts.
      - **Rationale:** Increases engagement (time on page, pages per session).
      - **Opportunity:** Create blog posts around existing video content to maximize asset use.

---

## Action Items

**Bailey Seybolt (GrowthX)**
- Confirm FAQ schema approach w/ Kirkland + ops; then implement Webflow blog template updates
- Check last week’s posts in GSC each Fri; verify indexing + sitemap inclusion
- Post slides + recording in Slack for Jason + Michael

**Jason Flateboe (Otto)**
- Implement sticky CTA on Otto blog; then add inline CTAs in new posts

**Jakub Rudnik (GrowthX)**
- Send Jason Scribe TikTok/Shorts examples
- Research Webflow sitemap control; share guidance w/ Jason

---

## Transcript
**Jakub Rudnik:** Um, right before the, well, I got like back from my walk and I got a new, uh, got a special espresso machine for the first time for Black Friday.

**Jakub Rudnik:** I'm to be a coffee snob.

**Jakub Rudnik:** No, I'm just like, whatever.

**Jakub Rudnik:** So I forgot a piece when I set up after this walk and I like, it like exploded coffee grounds on my walls twice in a row.

**Jakub Rudnik:** Uh, so I was like, I have an hour before this call.

**Jakub Rudnik:** And I had like 25 minutes because I was troubleshooting trying to, and then I'm like, I need a coffee.

**Jakub Rudnik:** And then think about this coffee for 45 minutes, 40 minutes.

**Jakub Rudnik:** I lost, I lost like 40 minutes in the afternoon.

**Jakub Rudnik:** But other than that, it was before.

**Jakub Rudnik:** I'm glad I didn't like wait to one o'clock to do everything.

**Bailey Seybolt:** That's like my dream, but I think I would be so over caffeinated that it would just be a bad idea.

**Bailey Seybolt:** If I could just make myself a latte, I think I would just like need to be sedated.

**Jakub Rudnik:** By the end of the day, it's, it's already, I'm like really trying to slow roll.

**Jakub Rudnik:** already had a lot of.

**Jakub Rudnik:** Caffeine, but now it's more enjoyable, and I can do different things, and it's just like a big pot of drip coffee, you know?

**Jakub Rudnik:** So the first day, it had a cool product guide.

**Jakub Rudnik:** was like digital in an app, and it like, whatever.

**Jakub Rudnik:** So it's like, if your coffee looks like this, you need to do this instead, or this.

**Jakub Rudnik:** Like, it was like, if it's too weak or too strong, or whatever.

**Jakub Rudnik:** So I made two, I was trying to taste it.

**Jakub Rudnik:** oh, do I taste it more bitter?

**Jakub Rudnik:** So I had like two double shots, like right at the end of the day.

**Jakub Rudnik:** And so then like, I also then did like a workout, and then afterwards, I was like buzzing.

**Jakub Rudnik:** So my wife's like, too much, dude, like they did too much.

**Jakub Rudnik:** I know it's a new toy, but don't do that.

**Bailey Seybolt:** That's like playing with fire when you have little kids who might still get you up in the middle of the night, too.

**Jakub Rudnik:** Oh, yeah.

**Jakub Rudnik:** Oh, yeah.

**Jakub Rudnik:** So we just both came, like I picked her up from daycare.

**Jakub Rudnik:** were just like running around.

**Jakub Rudnik:** She's like, you had a lot of coffee today, didn't you?

**Jakub Rudnik:** So we're trying not to, I mean, it was a positive.

**Jakub Rudnik:** It was positive experience.

**Jakub Rudnik:** a It

**Jakub Rudnik:** So I don't need the crashes or the headaches that come from that.

**Bailey Seybolt:** Hi, Jason.

**Bailey Seybolt:** You're muted.

**Jason Flateboe:** There we go.

**Bailey Seybolt:** You can just mime for us.

**Jason Flateboe:** I thought Michael was going to be joining, but I don't see him here in the office right now.

**Jason Flateboe:** So I'm not sure.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** Well, we can always, we'll share everything afterwards.

**Bailey Seybolt:** If he misses and wants to catch up, we can also share a recording too.

**Jason Flateboe:** Great.

**Jason Flateboe:** Okay.

**Bailey Seybolt:** All right.

**Bailey Seybolt:** I can share the agenda.

**Bailey Seybolt:** So not a ton to catch up on.

**Bailey Seybolt:** There was something I wanted to flag for you.

**Bailey Seybolt:** We were having an issue with one of the steps in the pipeline right now, making some mistakes on product features.

**Jason Flateboe:** So we have someone taking a look at it.

**Bailey Seybolt:** And fixing it right now, but there's a chance that the articles might not come until Monday if we can't get it figured out today.

**Bailey Seybolt:** So hopefully not.

**Bailey Seybolt:** Hopefully we'll just get them to you tomorrow like usual, but I just wanted to flag that.

**Jason Flateboe:** If you don't see them tomorrow, that's why.

**Jason Flateboe:** Okay.

**Jason Flateboe:** It's actually not a big deal because I'm going to be out tomorrow and Monday.

**Bailey Seybolt:** I'm traveling all weekend, so I won't get a chance to review anything before Tuesday after today.

**Bailey Seybolt:** Okay, great.

**Bailey Seybolt:** And I'll let them know that they might not have me breathing down their neck quite as much tomorrow.

**Bailey Seybolt:** Great.

**Bailey Seybolt:** I think, I don't know if you had any kind of feedback or kind of content quality or anything you wanted to discuss along those lines?

**Jason Flateboe:** No, not about the content.

**Jason Flateboe:** I was going to give you an update on just the, I did a little bit of research into the schema stuff for FAQ and starting to wrap my head around it.

**Jason Flateboe:** But I do think we kind of need to meet in the middle on exactly like what needs to be done and how we imagine that.

**Jason Flateboe:** I'm working because I still haven't completely figured out what I need to do.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** That sounds good.

**Bailey Seybolt:** I can ask Kirkland if he has any kind of best practices or I think it sounds like it might not be a crazy lift for us to help on our end.

**Bailey Seybolt:** I should confirm that with our ops person who sort of is in charge of that.

**Bailey Seybolt:** I know like Kirkland told me that when they create the content in the pipelines, it's essentially like schema ready.

**Bailey Seybolt:** So I don't think adjusting the template on the client end is like a crazy lift, especially if you see better results from that.

**Bailey Seybolt:** So let me check on that and then I'll follow up with you and let you know.

**Jason Flateboe:** Okay.

**Jakub Rudnik:** It sounds good.

**Jakub Rudnik:** It's Webflow.

**Jason Flateboe:** Is that correct?

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** think that's all correct.

**Jakub Rudnik:** I know we chatted briefly on that earlier this week.

**Jakub Rudnik:** I that's all, right, we've done FAQ with schema markup on Webflow before, now that I'm thinking about it longer, so I would sync with Kirkland, it's probably just a ticket from there, and then we can implement the, like, implement in the template of the blog for, like, at the high level, and then just update the pipeline with the FAQ, like, written, and it'll be schema ready, like you said.

**Jakub Rudnik:** So, I believe that's all correct, but, yeah, also not going to Kirkland and just confirming.

**Bailey Seybolt:** Cool.

**Bailey Seybolt:** Okay, yeah, I'll confirm all that, and then let you know, but hopefully, yeah, if we could take care of that, that would be great.

**Jason Flateboe:** Yeah, and I'm happy to, if we want to set up a separate quick meeting or whatever to kind of just, you know, hold hands and do it, that would be totally great, too.

**Bailey Seybolt:** Yeah, I'll see what, if anything, they need from us, because I know we already have access, so I'll see if there's anything else they would need from you, I mean, or if we could just go ahead and do it.

**Jason Flateboe:** Okay, cool.

**Bailey Seybolt:** Great.

**Bailey Seybolt:** Thank you.

**Bailey Seybolt:** you.

**Bailey Seybolt:** you.

**Bailey Seybolt:** you.

**Bailey Seybolt:** I think the next thing was sort of talking through some of this monthly reporting.

**Bailey Seybolt:** So, Jakub, maybe I'll stop sharing and let you share if that works.

**Jakub Rudnik:** Yeah, totally, totally, totally.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** Everyone see the screen here?

**Jakub Rudnik:** Yes.

**Jakub Rudnik:** Okay.

**Jakub Rudnik:** Pretty straightforward.

**Jakub Rudnik:** It's not the longest thing.

**Jakub Rudnik:** Even six months from now, it won't be terribly deep unless we have, or like, long presentation unless we have something very specific.

**Jakub Rudnik:** But I'm starting here, like, as when it's our first time doing this.

**Jakub Rudnik:** And so what I'm looking for metrics-wise, I think we can customize this to every client to some extent.

**Jakub Rudnik:** But, like, if I'm just thinking of brand new content, publishing for the first time, what are we looking for?

**Jakub Rudnik:** What signals do want early on?

**Jakub Rudnik:** I just have this slide in here that's not exactly pretty, but it can help, like, what I'm looking for and what health we're looking for at different stages.

**Jakub Rudnik:** Isn't this?

**Jakub Rudnik:** Fathom like, oh, I should set like certain time limits to them, but they can be different depending on site and different things.

**Jakub Rudnik:** But in the beginning, I just want, and like this with growthx is really good with the strategy sprint, but let's get publishing, let's make sure we get those mechanics all correct, right?

**Jakub Rudnik:** Like how do we get good content and get it on the site?

**Jakub Rudnik:** Then how do we make sure that content is indexed?

**Jakub Rudnik:** And then we had that little, like figure out that robot TXT, whatever that was that was blocking.

**Jakub Rudnik:** So we've mostly overcome that.

**Jakub Rudnik:** I'll have something here in a second.

**Jakub Rudnik:** And then from there, like, not only is Google found the content, but is it doing something with that content?

**Jakub Rudnik:** And that's where we see impressions and keywords just for the first time.

**Jakub Rudnik:** Like, of course, we want as many impressions as possible.

**Jakub Rudnik:** And we want those keywords to be as close to one or in rankings as possible.

**Jakub Rudnik:** But just seeing those first signs of life, really important.

**Jakub Rudnik:** I think we're basically through all these, the minor caveat of there's a little bit of indexing thing I want to talk through.

**Jakub Rudnik:** But otherwise, those are good.

**Jakub Rudnik:** The second, like we'll still look at impressions and total keywords, like ultimately, especially in those first six months.

**Jakub Rudnik:** I just want to see it up

**Jakub Rudnik:** And to the right for those two specifically, then we start looking at the keyword positions.

**Jakub Rudnik:** Are we moving from page five when we start to page three?

**Jakub Rudnik:** Like when something ranks right away, how close to one are we?

**Jakub Rudnik:** We want to see that inching towards one.

**Jakub Rudnik:** Even like the healthiest content programs will still often start on page two and three, but you just always want to see that moving closer to page one right away.

**Jakub Rudnik:** And then we'll start to certainly look at, do we actually have traffic from organic?

**Jakub Rudnik:** So Google being et cetera, and then certainly start to look at LLM referral traffic.

**Jakub Rudnik:** It's basically where we are right now.

**Jakub Rudnik:** We're at the very early parts of that stage where like we are seeing traffic, we're seeing impressions grow.

**Jakub Rudnik:** So that, and then as this is growing, we'll start to look at the traffic and not just what traffic is it, but how, like which pages are getting traffic?

**Jakub Rudnik:** How is that spread out over time?

**Jakub Rudnik:** Or like, oh, not over time, but across the different pages.

**Jakub Rudnik:** How many times are we cited in LLMs?

**Jakub Rudnik:** Where are those citations?

**Jakub Rudnik:** And then is that LLM referral traffic growing?

**Jakub Rudnik:** Is it to the right pages, et cetera.

**Jakub Rudnik:** And so.

**Jakub Rudnik:** So we'll always be thinking about these things, but this is where I'd be really focused, and as we go from there, you certainly want to track traffic, but it's like the relevancy of the traffic, and really that's when we'll dig into conversion events, right?

**Jakub Rudnik:** So we're still really in like somewhere between phase one and two.

**Jakub Rudnik:** I mean, we're definitely looking at those metrics still in phase three, but it's mostly just because they're overlapping.

**Jakub Rudnik:** Any questions on just how I think about like kind of the funnel of metrics and what we're talking through?

**Jakub Rudnik:** Yeah, I think that makes sense.

**Jakub Rudnik:** Cool.

**Jakub Rudnik:** So just at the publishing level, again, we're at that early stage, like publishing has been really healthy, where you're working well with us, Bailey and team are producing, all that looks really good to me.

**Jakub Rudnik:** You know, getting 40 blogs published basically in our first six weeks, like done this internally a ton of times, like getting that type of velocity.

**Jakub Rudnik:** mean, it's why you work with us, but this is like such a big thing to show Google.

**Jakub Rudnik:** We're doing content.

**Jakub Rudnik:** We're doing content every week, and it's good content.

**Jakub Rudnik:** It's seen that.

**Jakub Rudnik:** So that's all right.

**Jakub Rudnik:** 15 in November, think some of those that were like written in November, technically published in December, but already 13 in December, just like good momentum, our operations between the two teams are working well.

**Jakub Rudnik:** Minor concern is like, we had that initial issue with the index.

**Jakub Rudnik:** I found two more that weren't indexed, I think were like stragglers that hadn't indexed from the original issue.

**Jason Flateboe:** I pushed those.

**Jakub Rudnik:** You can like manually submit them to GSC.

**Jakub Rudnik:** don't know if we've gone over that with you.

**Jakub Rudnik:** I did that on Tuesday.

**Jakub Rudnik:** I checked again this morning.

**Jakub Rudnik:** were both working.

**Jakub Rudnik:** So like, it doesn't look like a residual error to me.

**Jakub Rudnik:** looks more of like Google didn't find them once.

**Jakub Rudnik:** It never came back.

**Jakub Rudnik:** Like, it doesn't seem like anything else is an issue.

**Jakub Rudnik:** These four I have flagged, I talked to Bailey Bump briefly, or I sent a Slack over.

**Jakub Rudnik:** They're all basically a brand new one from 12.4.

**Jakub Rudnik:** I did see it in the sitemap this morning.

**Jakub Rudnik:** The other three were just from 12.10, so just yesterday.

**Jakub Rudnik:** They're not in the sitemap yet, and not like a terrible sin.

**Jakub Rudnik:** just want to watch for how long the sitemap is taking to update.

**Jakub Rudnik:** I don't I don't have access to that.

**Jakub Rudnik:** It seems like everything is being submitted automatically unless I'm wrong.

**Jakub Rudnik:** I just don't know how long that's taking.

**Jakub Rudnik:** So we're just going to watch this and see what that cadence is, what Webflow is basically submitting over.

**Jakub Rudnik:** It basically looks healthy.

**Jakub Rudnik:** It's just like healthy with the caveat that I want to make sure that this isn't taking weeks or several days.

**Jakub Rudnik:** So if it is, we'll flag this that maybe there's something we have to do.

**Jakub Rudnik:** I have to, each CMS does a little bit differently.

**Jakub Rudnik:** Like there's, there's many caveats.

**Jakub Rudnik:** So I don't want to like dig in unless it's a true problem, but it's something that I just wanted to, both sides to watch.

**Jakub Rudnik:** And so just for our next steps, like let Bailey know it's worth probably each like Friday checking the last weeks of content and seeing if that's indexed and then checking the sitemap just to make sure we're healthy there.

**Jakub Rudnik:** But again, as we think of like, can I stop thinking about indexing?

**Jakub Rudnik:** I just want to confirm that that's all working before we like just dismiss that from our brains.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** You don't need to worry about it at a certain point, but currently, especially with that robots issue early, I want to just triple check everything.

**Jason Flateboe:** Just real quick, on that original issue, which I can't remember exactly how long ago it was, but I think I realized that I literally just had like a checkbox that I had like not checked because I had had test pages that converted into real pages or something like that, where it really felt like it was a one-time thing.

**Jason Flateboe:** I was like, oh, okay, I fixed that.

**Jason Flateboe:** Like, so hopefully that issue won't pop up anymore.

**Jakub Rudnik:** And so I think it seems like that, I remember you describing that the first time we met, and it seems like that's the case.

**Jakub Rudnik:** Everything else, it looks like a different thing.

**Jakub Rudnik:** just looks like it doesn't get to the sitemap, and how often is the sitemap being crawled?

**Jakub Rudnik:** But those look pretty healthy.

**Jakub Rudnik:** I'm just double checking these because of that past thing.

**Jakub Rudnik:** At the site-wide level, what I do is just like look at site-wide from November versus October.

**Jakub Rudnik:** Obviously, there can be seasonality with months, and we'll talk through this,

**Jakub Rudnik:** But generally, at the site level across months, pretty flat from a traffic standpoint.

**Jakub Rudnik:** And I'm pulling that from search console.

**Jakub Rudnik:** But impressions up, you know, 100% month over month.

**Jakub Rudnik:** And so that's new content being published for the first time, Google finding it.

**Jakub Rudnik:** And that's all net new keywords that we never had an impression.

**Jakub Rudnik:** So an impression, you're ranking anywhere from, it used to be 0 to 100.

**Jakub Rudnik:** Now it's more of like 0 to 40 with some changes, but you're somewhere on the map.

**Jakub Rudnik:** So good things, Google's testing.

**Jakub Rudnik:** None of that's necessarily turning into a ton of traffic yet, but you're seeing good signals, impressions, and that keyword growth.

**Jakub Rudnik:** My experience are like an indicator that you'll have future traffic or at least a chance of future traffic.

**Jakub Rudnik:** So that looks really healthy for our stage and like just how early your site is in general and like all the content, really normal.

**Jakub Rudnik:** But that 100% feels really good.

**Jakub Rudnik:** That's a lot of impressions.

**Jakub Rudnik:** You know, maybe in six months, that won't feel like a ton because we'll have so many more.

**Jakub Rudnik:** But right now, that's really good growth there.

**Jakub Rudnik:** Um.

**Jakub Rudnik:** And also small numbers, but the bottom left graph, that's Ahrefs, one of our SEO tools, 200% into this year, page one, keywords, things are moving from either didn't exist before and then on page one, or they've moved from lower positions onto page one.

**Jakub Rudnik:** So just good traction.

**Jakub Rudnik:** We'll certainly want to see this grow in pure numbers, like the volume grow, but it's all up into the right.

**Jakub Rudnik:** So feel good.

**Jakub Rudnik:** And then I don't know what this is, it's more of like a question for you, but if you see in the middle graph, that's our screenshot from our looker that you have access to, but the organic just really spiked in December.

**Jakub Rudnik:** So that doesn't show in like the top bullet point of month over month because it's December 9th, November, but huge spike to your homepage, which to me is not like an organic thing.

**Jakub Rudnik:** Usually it's more of a, you did something brand wise, you know, TikTok or something.

**Bailey Seybolt:** Did you do anything?

**Jason Flateboe:** Yeah, had, we had press.

**Jason Flateboe:** We opened up the website.

**Jason Flateboe:** You know, we were in a closed beta and we're now like general, general availability.

**Jason Flateboe:** And so there was a GeekWire article and

**Jason Flateboe:** So yeah, we had several hundred people sign up, I believe.

**Jakub Rudnik:** Very cool.

**Jakub Rudnik:** So to me, like when I look at this next month or, you know, Bailey's, whoever's looking at this, we want to like, not, we want to note that, but not like factored in like, was that organic growth?

**Jakub Rudnik:** No, that's more of like, you did other things.

**Jakub Rudnik:** And so just like filtering that out or noting that, but also good, like, congrats on that launch.

**Jakub Rudnik:** And that's all really positive there that is showing up here, but just want to, that's really helpful so we don't over attribute or something.

**Jakub Rudnik:** On the blog, which is basically all us, I've got here, GSC again, then Ahrefs, but organic clicks.

**Jakub Rudnik:** we had 11 in October, 50, you know, very small numbers don't need to put those percentages in here, because that will look over and play.

**Jakub Rudnik:** But that's positive points, and that's what we want to see the first couple weeks of December are already growing on top of that November growth.

**Jakub Rudnik:** So up into the right, looks really normal, looks really healthy.

**Jakub Rudnik:** Impressions as well.

**Jakub Rudnik:** Like again, all the impression growth you saw sitewide, ton of that is just from this blog content.

**Jakub Rudnik:** So, uh,

**Jakub Rudnik:** So I expect we'll dig in more and see more.

**Jakub Rudnik:** We'll just want to track this to make sure that we're growing exponentially from here, but that's feeling really good at this stage.

**Jason Flateboe:** And just to clarify that, that's clicks coming to the blog, right?

**Jason Flateboe:** Not clicks within a blog post.

**Jakub Rudnik:** Correct.

**Jakub Rudnik:** Yeah, this is, you if we're thinking about the, there's many ways that this content can be used for you, but our primary, especially at this stage, distribution channel is going to be, so I'm going to Google, find you somewhere on page one and clicking.

**Jakub Rudnik:** So, yeah, that's what I'm doing here, but we'll, that's a good point of, like, metrics later.

**Jakub Rudnik:** That's kind of not illustrated in that first page, but depending on what we're trying to do, we'll be measuring, you know, how people are actually interacting with that page, Their engagement, their clicks, their conversions, et cetera.

**Jakub Rudnik:** So I put that all under, like, conversion metrics in that last bullet point, but really good clarifying question.

**Jakub Rudnik:** Terrible screenshot, more of, like, look afterwards, but this is, like, the blog posts that are growing in one, if you see, like, 50 volumes, sometimes it's just, like, one blog post is working and we, like, struggled, but...

**Jakub Rudnik:** The overall health isn't there.

**Jakub Rudnik:** That's not what I'm seeing here.

**Jakub Rudnik:** I'm seeing a lot of, like, a few clicks across a ton of pages.

**Jakub Rudnik:** I actually much rather see that.

**Jakub Rudnik:** So we want to get a Google's, like, testing a lot.

**Jakub Rudnik:** And it's not saying, like, we just struggled or no one has done this.

**Jakub Rudnik:** And there's just some, like, some interest with this one topic.

**Jakub Rudnik:** It's more about, like, website health, content health.

**Jakub Rudnik:** we're seeing that.

**Jakub Rudnik:** looks like at least it's being tested.

**Jakub Rudnik:** And we're starting to see that traction across a lot of things.

**Jakub Rudnik:** So I like seeing it just in, like, breadth of all your URLs.

**Jakub Rudnik:** And the other thing I really like to see is, like, we've done a lot of different types of articles.

**Jason Flateboe:** Like, there's best lists, right?

**Jason Flateboe:** That top article is like best AI systems.

**Jakub Rudnik:** But there's also, like, more of, like, educational things that aren't in listicle format.

**Jakub Rudnik:** I see a template in here.

**Jakub Rudnik:** So there's different styles.

**Jakub Rudnik:** And so sometimes you'll just have, you know, just our listicles are working.

**Jakub Rudnik:** can't make other things.

**Jakub Rudnik:** Or it could be just our glossary content.

**Jakub Rudnik:** But it looks like, at least at the very first stage, we're seeing track, like, that first stage of attraction in a lot of different...

**Jakub Rudnik:** So that's what I want to see is like a ton of health.

**Jakub Rudnik:** You'll still always see outsized results from the rule is like 10% of your content will do 50% of your traffic.

**Jakub Rudnik:** But that's just like in all things, right?

**Jakub Rudnik:** Won't all be created equal.

**Jakub Rudnik:** You just need to take lots of shots on gold.

**Jakub Rudnik:** But right now that looks healthy.

**Jakub Rudnik:** This is good.

**Jason Flateboe:** So one thing just occurred to me too, you know, with our announcement, we had two founder blog posts that were written, you know, by our founders.

**Jason Flateboe:** And posted in, you know, so there's, there's a couple of, you know, this isn't something we plan on doing a lot of it.

**Jason Flateboe:** There's a couple of posts that we've done, you know, internally ourselves.

**Jason Flateboe:** Are, should those be separated out in terms of metrics and tracking and all that kind of stuff?

**Jakub Rudnik:** Or is that okay to just get all in the mix?

**Jakub Rudnik:** So it is in Looker completely separate out.

**Jakub Rudnik:** That's a good point.

**Jason Flateboe:** I didn't see anything in here, but now as I look at the screenshot, the second to last one introducing Otto, that appears to be one of those.

**Jakub Rudnik:** So it's not, it's a good cause.

**Jakub Rudnik:** I that this, like the clicks, this should be like 51 or 48 or something like that instead of, for our purposes, I didn't, I use GSC because it has the impressions data more connected, easier, but in Looker, we do have a filter to just remove anything that isn't created by growthx, so we have that ability, good to call it that, I hadn't thought about you writing anything else, so at this stage, but good call for future, future reporting, and if you do other, like, you know, some clients will like stand up, content motion on their own, or have a product person doing things, we, that will always be, like, attributed separately, so we can look at blog as a whole, just growthx blogs, etc.

**Jason Flateboe:** Perfect, and it's not important for me to do it one way or the other, but I think having that ability to filter it on or off for clarity is good.

**Jakub Rudnik:** Totally, and that's, that's why we have that, so that's, yeah, a good shout out that that's not done in the screenshot, but in some other places, and then, in the, I know it's like, where I put in a later of,

**Jakub Rudnik:** But I still do want to look at LLM visibility and start seeing the overall.

**Jakub Rudnik:** This first is your screenshot, and the upper left is your scrunch dashboard.

**Jakub Rudnik:** so this is LLM visibility, not necessarily, or no, I lied to you.

**Jakub Rudnik:** This is from GA4, and this is referral traffic from LLM specifically.

**Jakub Rudnik:** So you're looking at, like, someone went to chat GPT, did some sort of query, and then clicked a link in that query in the results, and actually brought them to auto directly.

**Jakub Rudnik:** So you'll see there will be other traffic that comes from LLMs that is reported either as, like, organic to your homepage or direct, right?

**Jakub Rudnik:** Someone types in your website into their URL afterwards, or they type in auto, and it looks like it's searched, but it's really coming from LLMs, and that's what makes this LLM search really murky.

**Jakub Rudnik:** This is at least very attributable.

**Jason Flateboe:** Someone's on chat GPT, their very next click took them to your website.

**Jakub Rudnik:** And so overall, this is growing, and your best week ever was last week.

**Jakub Rudnik:** So this is homepage.

**Jakub Rudnik:** This is not...

**Jakub Rudnik:** The upper left is your whole site, so that doesn't get rid of anything, but really good positive momentum.

**Jakub Rudnik:** Last week it makes sense with the launch.

**Jakub Rudnik:** We'll see if that momentum continues, but really good there.

**Jakub Rudnik:** And then the upper right is just the blog, so we've created much smaller.

**Jakub Rudnik:** It's not like we've seen huge results with some clients.

**Jakub Rudnik:** This is very early stages, but it is happening, right?

**Jakub Rudnik:** So someone searched something, clicked on the blog.

**Jakub Rudnik:** If there's clicks, that means there's even more citations and impressions, right?

**Jakub Rudnik:** So the right graph looked like the left graph over time, but at this stage, I've seen the LM referrals.

**Jakub Rudnik:** Typically, it's a smaller amount of traffic, not universally, but for most of our clients, it's a portion of that traffic.

**Jakub Rudnik:** And it also seems to lag behind.

**Jakub Rudnik:** In my experience, especially with newer websites, is that LMs are citing other things first and take longer to pick up.

**Jakub Rudnik:** They wait for Google to start citing so, but to see this at this stage, that's positive.

**Jakub Rudnik:** And then the last one is the scrunch dashboard that I mentioned a little bit too early, but this is like citations and not necessarily clicks.

**Jakub Rudnik:** It's still really small.

**Jakub Rudnik:** If you look at the center of the circle, 1% of the things we're tracking, we're seeing citation, but those citations are growing, especially in the last things you want to be referenced in overall, but you're starting to be cited, tracked, et cetera.

**Jakub Rudnik:** So positive signal there.

**Jakub Rudnik:** And then the things I just saw from this exercise in the couple brief, so I don't know that these need to be done immediately, but as we start to get just a bigger end of traffic, we want to have a better chance that people will sign up, test the product, et cetera.

**Jakub Rudnik:** So I'd put a sticky CTA button on the side of the blog, probably under the table of contents.

**Jakub Rudnik:** It could be on the right hand, but just send over one of the...

**Jakub Rudnik:** Yeah, I can imagine that.

**Jakub Rudnik:** It should be easy to implement, did this and done this in Webflow many times.

**Jason Flateboe:** Yes, I will call it as all just custom layout stuff to make it bad, Exactly.

**Jakub Rudnik:** This is one of my, like where I used to, a couple stops ago, in Webflow, they just have this sticky, they've done so many different tests on it, but it's driving thousands of signups to their blog every month from their content, you know, 70,000 people a month or something, but three to 5% of those people every single month turn into a free user of their product, so just to them, because we had a really good growth team over there.

**Jakub Rudnik:** A little bit more difficult with Webflow, you need some design, you need to like use short codes and things, but as we get going and see more traction on those pages, we'll want to put like inline CTAs, I'd say, within pages.

**Jakub Rudnik:** So one of my favorite moves is like, what's the challenge of whatever the topic is, and you explain it, and then you show your product right afterwards to give someone a reason to test this out, right?

**Jakub Rudnik:** So I want to add more of those.

**Jakub Rudnik:** would put the sticky CTA as universal, typically, and can be done once, set it, and forget it, and then we can test as we get more traffic.

**Jakub Rudnik:** But I do that one before the inline thing.

**Jason Flateboe:** Is that, maybe I missed this while you're describing it, but would that appear in the middle of the body or, like, after all of the content?

**Jakub Rudnik:** So you have one at the bottom of the template.

**Jakub Rudnik:** This will be in the body of the content, so you find the right kind of conversion point.

**Jason Flateboe:** a little different for each blog.

**Jason Flateboe:** This is just a technical thing I need to work out.

**Jason Flateboe:** Like, how do you inject it in the middle?

**Jason Flateboe:** Do you just reference it and it sucks it in?

**Jason Flateboe:** Yeah, Webflow is, like, not my favorite CMS to do it with, but you, like, can design it and then, forget exactly, but you create a short code for that, and you just dump the short code in that section of the blog, and then it's, like, you guys, when you write the rich text content or whatever, you just put it up, like,

**Jason Flateboe:** And you guys would sort of own like where that lives in there and where you want to call it?

**Jason Flateboe:** Correct.

**Jason Flateboe:** Okay, got it.

**Jakub Rudnik:** Again, I would think of that later than the other CTA type, but still would want to put that on the radar.

**Jakub Rudnik:** It's down the road, but thinking about that once we have the traffic, better to do now.

**Jakub Rudnik:** And then I found, this is the YouTube and like YouTube shorts, same company, we had a huge influencer play and finding like really successful influencer videos.

**Jakub Rudnik:** And embedding them into our content, saw instant like time on page increases, conversion increases, pages per session.

**Jakub Rudnik:** So, it's a little bit more difficult thing as well.

**Jakub Rudnik:** And often I wait till I have traffic in like really good videos, but since you have a library of videos, it's something that we should consider doing.

**Jakub Rudnik:** Especially if one, they're successful on YouTube or another platform.

**Jakub Rudnik:** don't know if you're doing stuff beyond YouTube shorts, just find it there first.

**Jason Flateboe:** Yeah, the only real video is, yeah, we had one created by a third party for the homepage, the one that's sitting at the top, and then I've been starting to do some, like, just kind of product how it works short little videos that literally are just, like, recorded screens with voiceover, and we might continue to do more of those, and I could create those fairly quickly if we have a particular case or something we want to show.

**Jakub Rudnik:** Cool, yeah, I mean, that's, like, the sticky CTA, easy, universal, these ones are, like, you have to match the, you know, the content's got to be decent, least since you've got to match the context of the blog, but when applicable, I would look for those opportunities, so this is a little bit of a call for both sides, but since you're doing that already, and I've shown the ability to do that, I would recommend that where possible.

**Jason Flateboe:** You know, what I could imagine is taking videos, which are already sort of patterned after, like, our main use case, like, we've identified, like, these are the ones.

**Jason Flateboe:** We want to make videos for, and if we have them, those could also, you could use that as a jump-off point, like, let's create a blog post about the particular use case, because we already have it, and it's important to us, so let's write about that.

**Jakub Rudnik:** Yeah, they're really, when you are really, like, cooking with both channels, it's like, you find the blog topic that's good, and then you, like, build that, and then what's the perfect video on the other side, or you are doing influencer stuff, or internal, something really takes off, then you go create the blog, so it'll be relevant for it, right?

**Jakub Rudnik:** So it can, it can go both directions, so I really like that.

**Jakub Rudnik:** I'll send over a couple things we did at Scribe, like, one of the first videos, like, the fifth video we did, did, like, it did, like,.4, 1.7 million views, and just, like, was one of those, we have to do this forever type of thing, so I'll share a couple of those examples right after this call.

**Jakub Rudnik:** Okay, that's bookmarked, and then the CMS thing, this is a little bit of a, I don't know if we need to, but this is what we're tracking right now, right, but just making sure that everything's updating,

**Jason Flateboe:** Automatically, we're seeing the indexing as we believe they are.

**Jason Flateboe:** Again, there's some more just overabundance of caution.

**Jason Flateboe:** Is that, that feels like just a Webflow thing.

**Jason Flateboe:** Like, is there anything we can actually control there?

**Jason Flateboe:** Or that, you know, is, are we influencing that in any way?

**Jakub Rudnik:** Or is it just kind of, it is what it is?

**Jakub Rudnik:** I need to double check what, so Webflow is, sorry, where are you?

**Jakub Rudnik:** Webflow is doing that out of the box.

**Jakub Rudnik:** With, depending on the CMS, there's either third-party tools or settings you can change.

**Jakub Rudnik:** I need to look at what Webflow does specifically.

**Jakub Rudnik:** So let me get back to you there.

**Jakub Rudnik:** But some of those can be updated.

**Jakub Rudnik:** And, like, each CMS does out of the box, like, site mapping differently.

**Jakub Rudnik:** Like, some now are adding, like, time or dates that things were last updated.

**Jakub Rudnik:** And that's supposed to be good for LLMs.

**Jakub Rudnik:** Webflow, I don't believe, is doing that.

**Jakub Rudnik:** I don't, and we were having issues.

**Jakub Rudnik:** Could you, like, override what Webflow is doing in a way?

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** So let me go find like the best guide on that right now.

**Jakub Rudnik:** Again, we work with just so many CMSs, it's escaping me, but you can do things, it's just CMS to CMS.

**Jason Flateboe:** Okay.

**Jakub Rudnik:** Yeah, so that's what I had.

**Jakub Rudnik:** know we're also up to time, but I have a comment.

**Jason Flateboe:** Anything you want to chat through on those?

**Jason Flateboe:** I know it was a good discussion throughout.

**Jason Flateboe:** No, that was great.

**Jason Flateboe:** Yeah, great to see the metrics, and yeah, thanks for answering the questions too.

**Jakub Rudnik:** For sure.

**Jakub Rudnik:** Bailey, anything else?

**Bailey Seybolt:** I think that's it on my end, so.

**Jason Flateboe:** Cool, yeah, if you could share some of those slides just so that Michael can put an eye on them, that would be great.

**Bailey Seybolt:** Yeah, I can share the slides and also the recording of the walkthrough as well.

**Jason Flateboe:** I can put them on Slack.

**Jason Flateboe:** Okay, perfect.

**Jakub Rudnik:** Cool.

**Jakub Rudnik:** I'll send over a couple of those TikToks just to show you what we're doing and maybe inspiration and look into the Webflow sitemap stuff as in tandem while we watch the indexing.

**Jason Flateboe:** Sounds good.

**Bailey Seybolt:** Thanks, everyone.

**Jason Flateboe:** Thank you.

**Bailey Seybolt:** Bye.
