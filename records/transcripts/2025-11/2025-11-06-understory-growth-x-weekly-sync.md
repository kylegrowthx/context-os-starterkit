# Understory <> Growth X - Weekly Sync

<metadata>
date: 2025-11-06
time: 15:57 UTC
duration: 30 minutes
organizer: team@growthxlabs.com
participants: Ali Yildirim, Alexander Fine, Katya Luscomb
fathom_recording_id: 99727171
fathom_url: https://fathom.video/calls/464555711
share_url: https://fathom.video/share/Ss2HB5rGss1sV4x9T8us3U7zcp6rC8dh
source: fathom
enriched_on: 2026-03-02 00:30 UTC
speaker_note: Only three speakers actively participated in this meeting. Sydney Go, Kyle Gaudreau, George Haikal, and Andi Bailey were invited but did not speak. Confirmed speakers are Katya Luscomb (GrowthX content lead), Ali Yildirim (Understory founder), and Alexander Fine (Understory, referred to as "Alex" throughout).
</metadata>

---

## Summary

Understory and GrowthX discussed blog content performance, technical blockers in analytics, and upcoming initiatives including podcast content and landing page projects. Katya Luscomb reported that 24 blog pieces have been published, with Google traffic now accounting for over 50% of sessions after sitemap fixes. The team identified GA4 misconfiguration and Google Search Console indexing issues as critical blockers, and agreed on plans to publish 2-3 podcast articles next week and expand content using ideas from Understory's Go-to-Market Engineering and Paid Media teams.

---

## Context

Understory is a content marketing agency working with GrowthX on blog content strategy and SEO. Katya Luscomb leads content delivery from GrowthX, while Ali Yildirim and Alexander Fine represent Understory. This is a recurring weekly sync where the team reviews content performance metrics, discusses technical issues blocking analysis, and coordinates on new content initiatives. The partnership involves publishing blog articles targeting high-volume keywords, tracking performance through Google Analytics and Looker dashboards, and now expanding into podcast content. Earlier in November, Understory had resolved sitemap issues that were blocking Google indexing; this call follows up on the impact of those fixes and discusses next steps for analytics configuration and content expansion.

---

## Relevance

**To GrowthX Delivery:**
- Content pipeline is accelerating: 24 pieces published to date, with 2-3 podcast articles going live next week. Atlas workflow upgrade in progress to improve automation and reduce manual review cycles.
- GA4 misconfiguration blocks Looker analytics — Katya needs admin access to fix setup around blog URL tracking (post vs. blog path issue). This directly impacts ability to measure content performance and inform future strategy.
- Google Search Console shows 125 unindexed pages — likely residual 404s and WordPress artifacts. Raise team investigation required to prevent continued indexing issues.

**To GrowthX Business Development:**
- Understory is requesting scope expansion: landing page project (improve existing Go-to-Market Engineering and Paid Media pages, build new RevOps as a Service page, add Paid Media Plus variation). Outside current engagement scope — opportunity to quote additional services.
- Client satisfaction signals: positive feedback on image aesthetic (gears concept preferred), proactive coordination on Sanity author profiles and dashboard access.

**To CheckThat:**
- Not directly relevant in this call, though SEO/indexing issues (sitemap, GSC, GA4 tracking) are foundational to AI visibility work.

---

## Overview

- **Analytics Blocked:** GA4 is misconfigured, reporting only 3 blog URLs. This blocks Looker performance analysis and requires Katya to get admin access to fix.
- **New Content Pipeline:** The Go-to-Market Engineering team is providing technical content ideas, enabling Understory to target high-volume keywords and expand into niche topics.
- **Podcast Strategy:** Podcast articles will be published to the main blog page next week to gain early performance signals, with a dedicated subpage planned for later.
- **Landing Page Project:** Understory will quote a new project for landing page improvements (optimizing existing, building new for RevOps), as this is outside the current scope.

---

## Key Topics

### Analytics & Technical Issues

  - **GA4 Misconfiguration:**
      - **Problem:** GA4 reports only 3 blog URLs, blocking Looker performance analysis.
      - **Cause:** Likely a residual issue from the old `/post` vs. `/blog` URL structure.
      - **Action:** Katya needs admin access to fix.
  - **Google Search Console Errors:**
      - **Problem:** 125 pages are unindexed, including 404s and other errors.
      - **Action:** Katya will have the Raise team investigate and resolve.
  - **Performance Context:**
      - A mid-October engagement dip was caused by sitemap errors.
      - Fixing the sitemap → Google traffic now accounts for \>50% of all sessions.
      - **Metrics Defined:** Impressions (seen in search) vs. Clicks (visited) vs. Sessions (time on page) vs. Engaged Sessions (\>10s on page).

### Content Strategy & Pipeline

  - **New Content Ideas:**
      - The Go-to-Market Engineering team will provide technical concepts for blog posts.
      - **Timeline:** Ideas expected by EOW or early next week.
      - **Action:** Katya will use these to target high-volume keywords.
  - **Podcast Articles:**
      - **Goal:** Publish 2–3 articles next week.
      - **Workflow:** Articles will be published to the main blog page with a "Podcast" category tag to gather early performance signals. A dedicated subpage is a future consideration.
      - **Technical:** The Raise team is adding code to embed YouTube videos.
  - **Workflow Automation (Atlas Upgrade):**
      - **Goal:** Improve content speed and accuracy with more advanced agents.
      - **Potential Change:** Auto-staging content in Sanity, reducing the need for Google Doc reviews. Katya will propose a new workflow next week.

### Website & Design Updates

  - **Image Mock-ups:**
      - **Feedback:** The "gears" concept is the preferred aesthetic.
      - **Action:** Katya will provide feedback to the design team to refine the style and ensure future images are more relevant to article content.
  - **Website Updates:**
      - **Completed:** Google Tag Manager added; empty "premium content" CTA removed.
      - **Action:** Add Spotify icon and link to the site footer.

### New Project: Landing Pages

  - **Request:** Understory to help improve existing landing pages and build new ones.
  - **Scope:**
      - Improve existing Go-to-Market Engineering and Paid Media pages.
      - Build a new page for RevOps as a Service.
      - Add variations (e.g., "Paid Media Plus").
  - **Action:** Katya will confirm if this is an add-on service and provide a quote.

---

## Action Items

**Alexander Fine (Understory)**
- Send voice notes for free trial nurture email to Katya
- Collect GTM Eng + Paid Media ideas/blurbs; add to shared folder; notify Katya
- Coordinate w/ Ali’s brother to grant Katya landing-page access
- Create Sanity author profiles; notify Katya

**Katya Luscomb (GrowthX)**
- Finish Fibblers podcast article; add to queue
- Grant Looker access to Ali + Alex; send GA4/Looker resources
- Investigate GSC indexing issues w/ Ray + Kyle; report findings
- Audit GA4 setup for blog URLs; report findings
- Propose Atlas/Sanity workflow improvements to Ali + Alex next week
- Share image style feedback w/ designer; test square-peg-round-hole concept
- Confirm w/ Kyle landing-page support; propose approach to Alex

**Unassigned**
- Add Spotify icon + link to site footer

**Ali Yildirim (Understory)**
- Create Sanity author profiles; notify Katya

---

## Transcript

**Katya Luscomb:** Good. How's it going?

**Ali Yildirim:** Pretty good. Sorry I'm a little late.

**Katya Luscomb:** It's all good. Sounds like a busy day for you guys.

**Ali Yildirim:** Yeah, I mean, it always is, but that's how it goes.

**Katya Luscomb:** Cool. Let me get my screen up.

**Alexander Fine:** Can you guys hear me?

**Katya Luscomb:** I can hear you now.

**Alexander Fine:** I just had every problem in the book trying to get into Zoom. Literally every single one that can ever happen.

**Katya Luscomb:** Ugh, I was just complaining about tech gremlins trying to share the agenda, and it shared this weird split screen. No worries. Good to have you on the call.

**Alexander Fine:** Good, how are you?

**Katya Luscomb:** Good. Cracking along. Kind of a busy week here, but making some progress.

**Katya Luscomb:** I can just jump right in if you guys are good to go.

**Alexander Fine:** Let's do it.

**Katya Luscomb:** Great.

**Katya Luscomb:** Some quick updates.

**Katya Luscomb:** We did get Google Tag Manager added this morning.

**Katya Luscomb:** Design team just confirmed.

**Katya Luscomb:** And they removed that empty call to action for the premium content.

**Katya Luscomb:** It's something we can look into bringing back.

**Katya Luscomb:** I was thinking through things that we might want to incorporate there, potentially if there's a way to incorporate subscribing to your YouTube channel or something, especially as we add podcast content.

**Katya Luscomb:** But in the meantime, wanted to take it off so it's not confusing folks.

**Katya Luscomb:** They're not expecting to get something if they actually stick their email in there.

**Katya Luscomb:** So that happened.

**Katya Luscomb:** And then big thing to discuss today is some mock-ups for some initial image ideas.

**Katya Luscomb:** I did share some additional feedback with the design team already.

**Katya Luscomb:** So there will be another round.

**Katya Luscomb:** I'll try and share that early next week so we don't have to wait a week for each call.

**Katya Luscomb:** I just wanted to get those over to you.

**Katya Luscomb:** So, and fairly standard five pieces of content in the works.

**Katya Luscomb:** Alex, I was curious if you had a chance to do some quick voice notes for that free trial nurture email piece.

**Alexander Fine:** Oh, I did not.

**Alexander Fine:** That's my bad.

**Alexander Fine:** I'll do that for you, though.

**Alexander Fine:** Also, we're going to have more ideas coming to you, by the way.

**Katya Luscomb:** Say again?

**Alexander Fine:** We're going to have more ideas.

**Alexander Fine:** So I had the go-to-market engineering team today.

**Alexander Fine:** I thought about this.

**Alexander Fine:** They're all going to send me ideas and blurbs about very technical concepts that we're doing on the go-to-market.

**Alexander Fine:** engineering side that we're going to be sharing with you.

**Alexander Fine:** Yeah.

**Alexander Fine:** So there's a lot more ideas in route as well.

**Katya Luscomb:** Perfect.

**Katya Luscomb:** Actually, that ties in well, because I'm going to be doing some more keyword research and assignment generation.

**Katya Luscomb:** And so I can pull from that and incorporate it into, like, high-volume keywords as well that we want to target and sort of cross-reference.

**Alexander Fine:** That'll be awesome.

**Katya Luscomb:** Cool.

**Katya Luscomb:** Cool.

**Katya Luscomb:** When are you thinking those will be over?

**Alexander Fine:** Maybe end of this week, early next week?

**Alexander Fine:** I'm going to push the team to get it this week.

**Alexander Fine:** We'll see if I can by the of the day tomorrow.

**Katya Luscomb:** That'd be great.

**Katya Luscomb:** If not, it'll be

**Katya Luscomb:** Early next week.

**Katya Luscomb:** Perfect.

**Alexander Fine:** I'm add that.

**Katya Luscomb:** You said that was specifically for go-to-market engineering?

**Alexander Fine:** Or just in general?

**Alexander Fine:** although all of you should have paid media team to do it, too.

**Alexander Fine:** Any, like, really unique niche things that they're doing that we can create blog content about.

**Alexander Fine:** I mean, what we show up for, right?

**Ali Yildirim:** Yeah, I mean, all the MCP stuff that we're doing for sure should have its own blog.

**Katya Luscomb:** Yep.

**Katya Luscomb:** Perfect.

**Katya Luscomb:** Great.

**Katya Luscomb:** I will keep an eye out for that.

**Katya Luscomb:** That's exciting.

**Katya Luscomb:** Perfect.

**Katya Luscomb:** Podcast article for this week and sort of more general podcast update.

**Katya Luscomb:** I'm going to go back to Fibblers and work on that one and incorporate.

**Katya Luscomb:** I saw, Ali, you left a couple comments on the Trigify piece just to tidy up that TLDR.

**Katya Luscomb:** So I shortened that up.

**Katya Luscomb:** I'm going to adjust our workflow a little bit.

**Katya Luscomb:** My goal is to start publishing, add those to our blog page next week.

**Katya Luscomb:** I have the design team adding in some code so that we can embed the YouTube videos.

**Katya Luscomb:** Let's see.

**Katya Luscomb:** I'll

**Katya Luscomb:** It just needs a little bit of extra back-end work to make that happen, but Ed on Raise is already on top of that.

**Katya Luscomb:** So we should be in good shape to get those up.

**Katya Luscomb:** And my thinking for right now, just so we can get some early signals, is to add a category for podcasts that we'll tag those with and just have them on the main blog site.

**Katya Luscomb:** And then as we scale more content and get more and more pieces, we can consider maybe making a subpage for podcast articles.

**Katya Luscomb:** I just don't want that page to look empty when we start pushing content out initially.

**Ali Yildirim:** Yeah, that's fair.

**Katya Luscomb:** Cool.

**Katya Luscomb:** Oh, yeah.

**Katya Luscomb:** And I had some fun stats to consider.

**Katya Luscomb:** We've published 24 pieces since we got started.

**Katya Luscomb:** It's nice to see that we're getting some volume there, which is cool.

**Katya Luscomb:** So, and then just quickly, like, yeah, our typical staging five, as I mentioned, my goal is to publish two podcast articles.

**Katya Luscomb:** If this third one with Fibbler looks good, we can also add that onto the queue as well.

**Katya Luscomb:** And then, like I mentioned last week, I'm going to start doing a more detailed performance review with some stats from Looker.

**Katya Luscomb:** And my goal is to have them just in the agenda for QuickView.

**Katya Luscomb:** And there's also a link to Looker if you guys ever want to poke around a little bit more.

**Alexander Fine:** Yes, that would actually be great.

**Katya Luscomb:** Can you show us how to do that?

**Katya Luscomb:** Yeah, so it's got this link right here.

**Katya Luscomb:** And then there's...

**Katya Luscomb:** need to share access to this because I have the link, but we just can't access it.

**Katya Luscomb:** Oh, interesting.

**Katya Luscomb:** Okay, I will look into that because it should...

**Katya Luscomb:** Oh, yeah, look at that.

**Katya Luscomb:** Let me...

**Katya Luscomb:** I will add your emails right after this call so you guys don't have to sit here while I do that.

**Katya Luscomb:** No worries.

**Katya Luscomb:** Perfect.

**Katya Luscomb:** Sorry about that.

**Ali Yildirim:** I thought that was already done.

**Ali Yildirim:** No worries.

**Ali Yildirim:** No worries.

**Katya Luscomb:** Okie dokie.

**Katya Luscomb:** dokie.

**Katya Luscomb:** So some quick things.

**Katya Luscomb:** These are for all of your URLs.

**Katya Luscomb:** There was a slight dip in engagement in mid-October.

**Katya Luscomb:** I think that's most likely because of some of those sitemap errors that we were working on and Google just having trouble with indexing some blog pages.

**Katya Luscomb:** Now that we've got that going, as we see for referrals, like Google traffic has actually spiked quite considerably.

**Katya Luscomb:** So the second chart here is showing where people are finding your site.

**Katya Luscomb:** So we see like obviously Google was having trouble recognizing pages kind of early, mid-October.

**Katya Luscomb:** And then once we got those sitemap updates, Google is now like well over half of the traffic compared to everything else.

**Alexander Fine:** We were both talking about this.

**Alexander Fine:** So can you talk to us a little bit about, so this is what, in sessions by refers?

**Alexander Fine:** That's what we're looking for.

**Alexander Fine:** The last thing that were looking at, we were looking in the actual Google Analytics, and we noticed impressions were way up, which is great.

**Alexander Fine:** I don't what that means.

**Alexander Fine:** Could you tell us a little bit more about what that actually means?

**Katya Luscomb:** Yeah.

**Katya Luscomb:** So impressions, what that's looking at is when folks come across one of your URLs on a Google page, and they might spend some time looking at that page with your URL on it.

**Katya Luscomb:** And then clicks, obviously, are tracking when someone actually clicks into that content.

**Katya Luscomb:** So that's the ultimate goal, is for folks to click in.

**Katya Luscomb:** And then in here, where it's talking about sessions, so this is looking at time that people are spending on your actual pages.

**Katya Luscomb:** So sessions means someone came to it, and engaged sessions means that they spent, like, more than, I believe it's 10 seconds on a page, like, scrolled slowly.

**Katya Luscomb:** It's an indication that they're actually reading and engaging with the content.

**Katya Luscomb:** So it's kind of a quick dive into what those mean.

**Katya Luscomb:** And I can try and send over some more specific resources.

**Katya Luscomb:** resources that talk about those a little bit more in depth, if you guys would like, so that as you're poking around Looker, you've got some perspective on that too, if that would be helpful.

**Ali Yildirim:** Yeah, that would be good.

**Ali Yildirim:** The one other thing I had a question about, because I was also looking in Search Console, and it looked like there was still some issues with pages not being indexed.

**Ali Yildirim:** I saw it said 125 pages, you know, without being indexed.

**Ali Yildirim:** I can share my screen and show you, but that's what I'm seeing.

**Katya Luscomb:** Yeah, and I know that actually, I think, tails into, and you mentioned Google Search Console.

**Katya Luscomb:** I'm going to have Ray's look back into the posts problem, because I think that even though they fixed the sitemap, there might be some residual errors, especially since you flagged that that URL came through.

**Katya Luscomb:** So I'm to have them dig into that a little bit more, and that might be part of the issue with the indexing.

**Katya Luscomb:** I can also dig a little bit more in with Kyle, as for those other pages, because I know the blog pages are indexing.

**Katya Luscomb:** to rules-

**Katya Luscomb:** I believe your, like, main landing pages are as well.

**Katya Luscomb:** When I was looking into some of those other pages, it looked like they were maybe some older pages from, like, WordPress or something.

**Katya Luscomb:** But I'll do a little bit more digging and see if we can resolve that.

**Ali Yildirim:** Yeah, it looks like there's just 404s and some, I don't know, errors that I don't understand.

**Ali Yildirim:** So, yeah, just let me know what you find.

**Katya Luscomb:** Yeah, for sure.

**Katya Luscomb:** And we'll flag, like, if there's any cleanup that we need to do and, like, if any of that's going to be impacting traffic.

**Katya Luscomb:** Okay, sounds good.

**Katya Luscomb:** There was one thing in starting to look over the analytics that our team noticed there seems to be a potential issue with the way GA4 is set up.

**Katya Luscomb:** They shared this screenshot with me where your Google Analytics is only pulling, like, three URLs that have blog associated with it.

**Katya Luscomb:** My thought is maybe when this got set up, there was still that issue with the backslash post instead of backslash blog.

**Katya Luscomb:** I don't actually have access to.

**Katya Luscomb:** I

**Katya Luscomb:** Dig into your Google Analytics to look at what the issue might be.

**Katya Luscomb:** So if you guys are able to dig into that a little bit, I just don't have ownership access on my end.

**Ali Yildirim:** Can I give you access to Google Analytics?

**Katya Luscomb:** Potentially, that could work.

**Katya Luscomb:** And then I could poke around and see.

**Katya Luscomb:** I don't know if my email, it might be like a, it might let a GrowthX email in as owner access.

**Ali Yildirim:** But that's the level of permission you need.

**Katya Luscomb:** That's what it was saying when I was trying to go in and poke around a little bit more.

**Katya Luscomb:** But essentially, this is just limiting Looker's ability to pull some more specific stats for like our clusters.

**Katya Luscomb:** Because eventually, I'll be doing a deep dive on like which clusters are performing the best and what's drawing in traffic and some of those things.

**Katya Luscomb:** But because...

**Katya Luscomb:** Because Google Analytics is only recognizing two of the blog posts right now.

**Ali Yildirim:** That's just a little limited.

**Ali Yildirim:** So if I give you administrator access, will that work for Google Analytics?

**Katya Luscomb:** Give it a try, and I will look into it today or tomorrow and let you know.

**Ali Yildirim:** All right, let me add you.

**Katya Luscomb:** Cool.

**Katya Luscomb:** It depends on what the issue is for how much I'll need.

**Ali Yildirim:** Okay, cool.

**Katya Luscomb:** Just happy with you.

**Katya Luscomb:** Perfect.

**Katya Luscomb:** All righty.

**Katya Luscomb:** And then I sort of jumped around.

**Katya Luscomb:** Oh, yeah, we've talked about all this.

**Katya Luscomb:** There is something upcoming.

**Katya Luscomb:** For a lot of our accounts, we are upgrading our Atlas workflow.

**Katya Luscomb:** So we're basically adding in more.

**Katya Luscomb:** More agentic agents, which will help improve, hopefully, speed and accuracy and start to incorporate more and more of those, like, specific expert perspectives that you're going to share without me having to do as much post-processing on the back end.

**Katya Luscomb:** So ideally, that'll help speed up our process and I can deliver things a little bit faster to you all.

**Katya Luscomb:** And with that, I'm also going to have the team looking to see if we can get the pipeline to auto-stage content.

**Katya Luscomb:** Right now, we have someone go in and manually stage and publish the pieces.

**Katya Luscomb:** And so then what we'll do, and we can talk a little bit more about this this next week once I dig into if that's possible with Sanity, we can talk about workflow.

**Katya Luscomb:** Like, if you guys still want to review the content in a Google Doc, or since you all have Sanity access, I can just flag what content is in Sanity for you all to go in and review.

**Katya Luscomb:** So Google Doc tends to be the easiest to see, but if you're all also comfortable with the content as it has been for the most part, I can just pick specific articles.

**Katya Luscomb:** Maybe there's one that has like.

**Katya Luscomb:** Your specific perspective in it that needs a closer read, and I can put those into a Google Doc, free to review, and then push it to sanity after the fact.

**Katya Luscomb:** So I just wanted to flag that as something for us to kind of think about what that process might look like, and I can give a more specific proposal of what that workflow would be next week for us to discuss.

**Katya Luscomb:** Sounds good.

**Katya Luscomb:** And then the real big discussion piece, we have some initial image mock-ups.

**Katya Luscomb:** And like I said, I've provided some feedback to the design team already.

**Katya Luscomb:** So our designer specifically was looking at this MQL to SQL.

**Katya Luscomb:** The workflow that she set up is not pulling content from the article, which is why some of these images look a little bit more generic.

**Katya Luscomb:** It's more about the style here.

**Katya Luscomb:** I did make sure that the content of the images will be more relevant.

**Katya Luscomb:** like this funnel piece, interesting, but the random shapes don't necessarily make sense.

**Katya Luscomb:** So trying to make sure that that actually relates to MQL and SQL conversion, so it's not just a kind of generic alphabet soup.

**Katya Luscomb:** Some other pieces that I was offering is potentially scaling up the size of the image a little bit.

**Katya Luscomb:** There's a lot of white space kind of between the image and the header.

**Katya Luscomb:** And then playing with some ideas, some other content that I've seen has had like some subtle background effects that sort of blur into the edges, which I think could create more cohesion between this new like sort of pixelated dot image style and the blocky text that is your brand.

**Ali Yildirim:** Yeah.

**Katya Luscomb:** But was curious if you all had any other thoughts on these.

**Ali Yildirim:** Yeah, it's interesting.

**Ali Yildirim:** I definitely see what you mean with the abstract shapes.

**Katya Luscomb:** Like it doesn't really make sense.

**Ali Yildirim:** I don't really like the middle one.

**Katya Luscomb:** would say that's my least favorite.

**Ali Yildirim:** just seems pretty flat and kind of cartoonish.-hmm.

**Alexander Fine:** The gears?

**Ali Yildirim:** Yeah, I don't really know what, I guess there's...

**Alexander Fine:** Cooking up MQLs and SQLs.

**Katya Luscomb:** Yeah.

**Ali Yildirim:** It's getting a good pipeline flowing, right?

**Alexander Fine:** Yeah, they are falling under the bottom, yeah.

**Ali Yildirim:** But yeah, I think out of all of them, the gears look my favorite, like, aesthetically, but again, you know, doesn't really make sense.

**Alexander Fine:** You want to scroll up to the one above, Katya?

**Alexander Fine:** Yep.

**Katya Luscomb:** And so with the way our pipeline generates, it'll generate, like, six options for images, and then we go through and pick what we like for each article that seems to be trending, and we can get it to regenerate a little bit.

**Katya Luscomb:** And so we do play with these each time to try and get something that's more and more appropriate.

**Katya Luscomb:** Yep, so really, this is about kind of dialing in the illustration style, and then on the back end, we play with our inputs so that the actual content of the image...

**Katya Luscomb:** This more relevant to each article.

**Alexander Fine:** I know this was automatically generated, but what could be cool is square things going to a funnel, below it being a pegboard with round holes, and it's turning into a circle so it fits into the round holes.

**Alexander Fine:** So you can't fit a square peg to a round hole.

**Alexander Fine:** Uh-huh.

**Katya Luscomb:** I don't know if you can specify that much, but I can check and see.

**Alexander Fine:** It's all good.

**Alexander Fine:** It's not a big deal.

**Alexander Fine:** I agree with Ali, though, out of these three, the Needy Gear one is my favorite, too.

**Katya Luscomb:** Cool.

**Katya Luscomb:** Perfect.

**Katya Luscomb:** I can share that with the designer as well.

**Katya Luscomb:** Yeah, I'm also going to share that we're making some progress there, hopefully fine-tuning.

**Katya Luscomb:** And then once we really dial in what we want that to look like, I will start to incorporate that into our upcoming articles, and then we can look at going back and refreshing and updating past content with these new images so there's cohesion as well.

**Katya Luscomb:** So I just want to make sure, in all of this, that we're really focused on continuing.

**Katya Luscomb:** time.

**Katya Luscomb:** See next

**Katya Luscomb:** To keep a good publishing cadence and then dialing in the images kind of as like a priority one, whereas priority zero is just continuing to publish so we can keep getting those signals for everything.

**Katya Luscomb:** It's kind of a quick update and discussion for everything on my end.

**Ali Yildirim:** Do you guys have any questions or anything that you wanted to discuss?

**Ali Yildirim:** I know Alex had a few things he wanted to talk about.

**Alexander Fine:** Yeah, so for me, there's a couple landing pages I want to spin up and we have some example pages now.

**Alexander Fine:** I'm wondering if that's something you can help us with.

**Alexander Fine:** I don't know if that's included for us.

**Katya Luscomb:** Essentially, it might be an addition to the service we're offering.

**Katya Luscomb:** can check with Kyle.

**Katya Luscomb:** Do you have some more specifics that I can bring to him?

**Alexander Fine:** Yeah, so basically we have these landing pages right now for go-to-market engineering and for paid media that we send to clients or prospects after we have a sales call.

**Alexander Fine:** And I want to spin up for RevOps as well.

**Katya Luscomb:** And we can provide the copy and do all that.

**Alexander Fine:** But I would like to...

**Alexander Fine:** A few things.

**Katya Luscomb:** So one, I'd like to improve landing pages that we already have.

**Alexander Fine:** And I have to figure out how to even get you access to those.

**Alexander Fine:** Neither Ali or I know how to do it.

**Alexander Fine:** So we have to talk to Ali's brother who helped us out with that.

**Alexander Fine:** So that's priority number one, I would say, is cleaning those up a little bit even more.

**Alexander Fine:** They're not bad now, but even better.

**Alexander Fine:** And then priority number three is just spin up a new one for RevOps as a service.

**Alexander Fine:** And then I'd also like to add some stuff to the other ones, like cold calling to one of them.

**Alexander Fine:** And then on the paid media side, I'd like to add another variation of it, which we'd call paid media plus.

**Alexander Fine:** But there's a handful of different things with landing pages that I would love help with.

**Alexander Fine:** And I'm happy to schedule like a separate session to go over that.

**Katya Luscomb:** But yeah, let me, let me check with Kyle and see what that might require from us.

**Katya Luscomb:** know.

**Alexander Fine:** Let us know.

**Alexander Fine:** We'll go from there.

**Katya Luscomb:** Perfect.

**Katya Luscomb:** Yeah.

**Ali Yildirim:** I think I'll

**Ali Yildirim:** So you sent over all of the files for the landing pages, right, in Slack?

**Alexander Fine:** Yeah.

**Alexander Fine:** Yeah, we have the files and the elements and all that.

**Alexander Fine:** We do have those.

**Katya Luscomb:** But I showed that a hack.

**Katya Luscomb:** Got it.

**Katya Luscomb:** Because Ray set up Sanity, I think we have some basic access to do some changes.

**Katya Luscomb:** I don't know the extent of it, so I would need to check on that as well.

**Katya Luscomb:** I'm mostly just in playing with the blog content from my perspective.

**Katya Luscomb:** It sounds like, so the edits that you'd be looking for, partially design, partially changing the wording and looking at other potentially strategies to drive more traffic?

**Alexander Fine:** Less of our traffic.

**Alexander Fine:** It's more so just the things we need help with.

**Alexander Fine:** And I just don't know if you guys have put that in the services that we're paying for, but if you do, it'd be great if you don't.

**Alexander Fine:** Thank Thank

**Alexander Fine:** I get it.

**Katya Luscomb:** Yeah, I will check in for sure.

**Katya Luscomb:** Okay.

**Katya Luscomb:** Anything else that you wanted to talk about while that's kind of pending?

**Alexander Fine:** Yeah, the other thing is Spotify.

**Alexander Fine:** So I want to get our Spotify.

**Alexander Fine:** You know, we have our LinkedIn and our YouTube linked on our page.

**Alexander Fine:** I'd love that we're spot.

**Katya Luscomb:** I linked there too.

**Katya Luscomb:** Okay.

**Alexander Fine:** So I can send you the link to that.

**Katya Luscomb:** Let me just drop in the chat right now.

**Katya Luscomb:** Does that work?

**Katya Luscomb:** Yeah, that's totally great.

**Alexander Fine:** And I can, that should be something pretty quick for Raises to be able to add in.

**Alexander Fine:** Yeah, just the icon.

**Alexander Fine:** And link to it.

**Katya Luscomb:** Perfect.

**Katya Luscomb:** Well, actually, it does remind me, as we're, one of the things that I'm going be working on is adding authors to all the blogs and categories, now that we have a good concentration of content.

**Katya Luscomb:** Yep.

**Katya Luscomb:** I noticed in authors that I think it's, I don't think either of you have an author profile under that, that group of authors specifically.

**Katya Luscomb:** I can share that with you all again.

**Katya Luscomb:** I think, let me pull up.

**Katya Luscomb:** So I'm going to be really quick.

**Alexander Fine:** Okay.

**Alexander Fine:** This is our Spotify link, by the way.

**Katya Luscomb:** Perfect.

**Katya Luscomb:** Snag that.

**Katya Luscomb:** It would just hit it from me.

**Katya Luscomb:** Oh, there it is.

**Katya Luscomb:** Oh, man, there's so many automated notes in here.

**Alexander Fine:** Sorry, I'm going to snag this before I hang up, because otherwise I'll lose it.

**Alexander Fine:** No worries.

**Katya Luscomb:** There we go.

**Katya Luscomb:** So, under people, so that I can assign authors, I just need you guys to add a quick profile in here, and I can share this over to you all as well.

**Katya Luscomb:** Because right now, I've just got Chris, Nofel, and Anna.

**Katya Luscomb:** And for some of those, we've got some thought leadership pieces coming up in the next week or two.

**Katya Luscomb:** And I think it would be great to have you guys on as authors and rotate through.

**Katya Luscomb:** Thank you.

**Katya Luscomb:** Thank

**Katya Luscomb:** There is that.

**Katya Luscomb:** Perfect.

**Katya Luscomb:** And that is actually everything that I had to talk about this week.

**Alexander Fine:** Perfect.

**Katya Luscomb:** Other than adding the Spotify, do you have anything else, Alex?

**Alexander Fine:** That's it for now.

**Alexander Fine:** Just be prepared that we're going to send over a bunch of ideas.

**Alexander Fine:** No worries.

**Katya Luscomb:** It's like a Google Doc?

**Katya Luscomb:** Yeah, whatever is easiest.

**Katya Luscomb:** Google Doc, voice notes.

**Katya Luscomb:** We can scrape voice notes, transcripts, and turn them into content.

**Katya Luscomb:** Yeah, there's a couple different options we've got.

**Katya Luscomb:** So really, whatever is easier for your team to send over, and then we can pull ideas from there.

**Alexander Fine:** Sounds good.

**Katya Luscomb:** Great.

**Katya Luscomb:** And for the Google Doc, if you just want to toss that, if that is what you do, if you just want to toss that into that shared folder where we have all of the published pieces, that can just kind of be a hub for a lot of content that we've got.

**Alexander Fine:** Okay.

**Katya Luscomb:** Works for me.

**Katya Luscomb:** Great.

**Katya Luscomb:** Well, if that's all, I can give you guys a few minutes back in your morning.

**Ali Yildirim:** Appreciate all the time.

**Alexander Fine:** Yeah, thank you.

**Katya Luscomb:** Yeah, no worries.

**Alexander Fine:** Have a good one.

**Alexander Fine:** Oh, by the way, wait, can you make sure you give us access to your dashboards?

**Katya Luscomb:** Yes, yeah, I have that.

**Katya Luscomb:** Yep, I've got that right here.

**Alexander Fine:** I will make sure that that happens.

**Alexander Fine:** All right, thank you.

**Katya Luscomb:** Yeah, no worries.

**Alexander Fine:** Have a good one.

**Alexander Fine:** you too.

**Alexander Fine:** Bye.
