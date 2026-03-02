# Webstacks <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-05
time: 17:30 UTC
duration: 39 minutes
organizer: kyle@growthxlabs.com
participants: Kyle Gaudreau, Katya Luscomb, Jesse Schor, Nikan Shahidi
fathom_recording_id: 120117568
fathom_url: https://fathom.video/calls/557236388
share_url: https://fathom.video/share/Vs2uzs9Kz8cfy1X-KoDZ4-NGaR8wENFr
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Kyle and Katya from GrowthX diagnosed Webstacks' post-refresh traffic drop by identifying a sharp decline in Googlebot crawl requests paired with significantly increased response times—triggered by a Vercel build process that updates the entire sitemap (600+ articles) on every change, combined with a 403 Cloudflare block on AI tools. Beyond the technical fix, the team shifted focus toward high-quality LLM-referred leads using GrowthX's newly launched Check That tool, emphasized YouTube and Reddit as strongest AEO signals, and discussed the path to an annual contract pending clear value-add to justify moving from Webstacks' current flexible 3-month term.

---

## Context

Webstacks is a web design and development agency, built on Sanity CMS, serving as a key GrowthX client. GrowthX provides content marketing and AI visibility services (Check That) to help Webstacks improve organic performance and LLM-referred lead quality. The meeting was triggered by a critical post-website-refresh traffic decline that accelerated over the past 1.5 weeks, impacting both organic impressions and overall lead volume. Kyle Gaudreau (GrowthX) brought GSC crawl data showing the root technical issue; Jesse Schor (Webstacks) and team investigated Vercel build processes and Cloudflare access controls. The discussion centered on collaborative diagnosis and roadmap alignment around AEO (answer engine optimization), content strategy, and potential contract restructuring.

---

## Relevance

**To GrowthX Delivery:**
- Traffic diagnosis workflow proved effective: combining GSC crawl reports with client-side infrastructure knowledge (Vercel logs, Cloudflare access) to isolate root causes. Applies to other clients with Vercel/Sanity stacks.
- Identified Cloudflare 403 blocking on AI tools (Claude) as collateral AEO issue—established pattern to flag with clients going forward.
- Sanity schema request: blog FAQ and TLDR modules needed alongside site pages. Jesse will audit blog schema; impacts refresh content pipeline for Webstacks and similar clients.

**To CheckThat:**
- Check That launch and demo (Katya sends by Feb 7) validates product direction: shift from top-of-funnel keyword/prompt monitoring to systematic lead data + AEO visibility. Jesse noted high-quality LLM conversions and openness to using Check That for content strategy.
- YouTube and Reddit identified as strongest signals for AEO visibility—factored into Check That positioning and future content recommendations.
- Gong calls from Webstacks to inform content strategy—establishes pattern for feeding business context into Check That prompts and AEO analysis.

**To GrowthX Business Development:**
- Contract expansion path identified: Webstacks CFO requires clear value-add (discount, new services, extended roadmap) to move from flexible 3-month to annual term. Katya to propose roadmap and value metric by next conversation.
- Strong relationship signals: Jesse eager to solve technical issue and invest in AEO roadmap; team receptive to YouTube/Reddit experiments; recurring discovery calls planned for Q1.
- Reference/case study potential: post-resolution, Vercel sitemap fix and YouTube/Reddit AEO pilot can be documented as methodology.

---

## Overview

- **Traffic Drop Diagnosis:** A post-refresh traffic drop is linked to a Googlebot crawl issue (fewer requests, slower response times) and compounded by a sitemap update for 600+ articles.
- **Root Cause Hypothesis:** The issue may stem from Vercel build processes that trigger full sitemap updates on every change, causing excessive recrawl requests.
- **Strategic Shift:** The focus will shift from top-of-funnel organic traffic to high-quality, LLM-referred leads, using Check That and social listening to inform strategy.
- **Contract Discussion:** An annual contract requires a clear value-add (e.g., discount, new services) to secure CFO approval over the current flexible 3-month term.

---

## Key Topics

### Traffic Drop Diagnosis

  - A significant traffic drop followed the recent website refresh, accelerating in the last 1.5 weeks.
  - **Diagnosis:** Googlebot crawl data shows a sharp decline in crawl requests and a significant increase in response times.
      - This pattern is unusual and suggests a technical issue, not a content or 404 problem.
  - **Compounding Factor:** A sitemap update for 600+ articles occurred around the same time, likely sending a large, confusing signal to Google.
  - **Webstacks' Initial Fixes:**
      - Removed non-Webstacks scripts from the Sanity template \~1.5 weeks ago.
      - Noted a drop in bot traffic (via PostHog) that may be affecting impression data.
      - **Significance:** These fixes haven't resolved the core crawl issue, as response times continue to worsen.

### Root Cause Hypothesis

  - **Hypothesis:** The issue is a Vercel build process that triggers a full sitemap update on every page change.
      - **Impact:** This would force Google to recrawl the entire site repeatedly, overwhelming the server and causing the observed crawl performance degradation.
  - **Additional Finding:** An AI tool (Claude) was blocked by Cloudflare with a 403 error.
      - **Significance:** This suggests a potential issue with bot access that may also be affecting Googlebot.

### Content & Sanity Updates

  - **FAQ/TLDR Modules:**
      - **Request:** Add dedicated Sanity modules for FAQs and TLDRs to blog posts.
      - **Status:** The FAQ module exists for site pages but not blog posts. The TLDR can use the existing `excerpt` field.
      - **Action:** Jesse will investigate adding the FAQ module to the blog schema.

### Strategic Roadmap & AEO

  - **Goal:** Shift strategy from top-of-funnel organic traffic to high-quality, LLM-referred leads.
  - **Methodology:** Use Check That (GrowthX's new AI visibility tool) and social listening to inform a data-driven content strategy.
  - **Key Insight:** YouTube is currently the strongest signal for driving AEO (Answer Engine Optimization) visibility.
      - **Action:** Explore a strategy for YouTube and Reddit, where Webstacks has a limited presence.
  - **Process:** Establish a recurring cadence for sharing business context (e.g., Gong calls, customer patterns) to inform content themes.

### Contract Discussion

  - **GrowthX's Goal:** Transition to an annual contract.
  - **Webstacks' Requirement:** CFO approval requires a clear value-add to justify moving from the current flexible 3-month term.
      - **Examples:** A discount or new services.

---

## Action Items

**Katya Luscomb (GrowthX)**
- Email Jesse Check That demo by Feb 7
- Schedule next-week discovery call w/ Jesse + Kyle

**Jesse Schor (Webstacks)**
- Email Kyle PostHog bot traffic trends
- Investigate crawl response time w/ Nikan Shahidi; review Vercel logs
- Audit build/sitemap; fix noindex in sitemap; stop daily full rebuilds
- Confirm blog FAQ module in Sanity; implement if missing
- Email Katya + Kyle batch of recent Gong call recordings

**Kyle Gaudreau (GrowthX)**
- Email Jesse re: Cloudflare 403; propose access/eng support
- Email Jesse re: AEO/social listening tool recs

---

## Transcript
**Kyle Gaudreau:** Hi, how's it going?

**Kyle Gaudreau:** Good.

**Kyle Gaudreau:** All of that, it's like, okay.

**Kyle Gaudreau:** I feel like maybe getting sick again for, you know, it's been a while.

**Katya Luscomb:** Yeah.

**Kyle Gaudreau:** I hope it's nothing though.

**Kyle Gaudreau:** How about you?

**Katya Luscomb:** Mers crossed.

**Katya Luscomb:** Rolling along.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** Just some Thursdays are early morning.

**Katya Luscomb:** I have my, my first call at like 730.

**Katya Luscomb:** So my brain feels like it's been, been going for a minute.

**Kyle Gaudreau:** I guess moving that, uh, some of those accounts around there were only was a short-term fix for you there.

**Katya Luscomb:** Yeah, no, it's all good.

**Katya Luscomb:** I am, I've got one similar, like they've got a teammate far abroad, so make it work.

**Katya Luscomb:** Morning, Jesse.

**Jesse Schor:** How you doing?

**Katya Luscomb:** Good.

**Katya Luscomb:** How you doing?

**Jesse Schor:** Doing all right.

**Kyle Gaudreau:** Hey, long time to see.

**Jesse Schor:** Kyle.

**Jesse Schor:** Yeah, man, what's happening?

**Kyle Gaudreau:** You know, we're staying busy as usual.

**Kyle Gaudreau:** We just officially, Marcel literally just pinged the channel that we just officially launched Check That.

**Jesse Schor:** So pretty excited.

**Jesse Schor:** Nice.

**Jesse Schor:** What was that?

**Kyle Gaudreau:** Check That?

**Kyle Gaudreau:** Check That.

**Kyle Gaudreau:** It's our AI visibility tool that we just...

**Jesse Schor:** Oh.

**Katya Luscomb:** Yeah, I'm going to be sending you guys over a demo of your setup by the end of this week.

**Jesse Schor:** Nice.

**Kyle Gaudreau:** Yeah, we're super excited.

**Jesse Schor:** Get into the game.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** I snagged Kyle today because I wanted to dive in.

**Katya Luscomb:** I know I sent over that article on the content on the traffic drop.

**Katya Luscomb:** Let me pull up my screen really quick to share.

**Katya Luscomb:** Because he helps look into some of the performance that we were noticing and helped compile the recommended actions around the crawling issue that we noticed.

**Katya Luscomb:** So I to make sure...

**Katya Luscomb:** That you guys, that we could answer any questions that you guys might have around that.

**Kyle Gaudreau:** Yeah, it would be helpful for me to just like run through it real quick and then we can just go into questions from there.

**Jesse Schor:** do you guys feel like you have a pretty good sense of what's in there?

**Jesse Schor:** Yeah, let's run through it.

**Jesse Schor:** I might have a sense of some updates that like we've recently made.

**Kyle Gaudreau:** All right, cool.

**Kyle Gaudreau:** Okay, so basically a pretty notable drop, right?

**Kyle Gaudreau:** Like it seems like this was a little bit hard to spot in the initial weeks because it was a bit of like a slow burn.

**Kyle Gaudreau:** And I know this is like a lower seasonality period, but it precipitous in the past, you know, week and a half or so.

**Kyle Gaudreau:** It was a little bit hard, honestly, to spot exactly why this was happening.

**Kyle Gaudreau:** You know, you can see things in here like the queries and the pages that were dropping and things of that nature.

**Kyle Gaudreau:** But the why behind it was a little bit harder to find.

**Kyle Gaudreau:** I've looked into things like...

**Kyle Gaudreau:** I've

**Kyle Gaudreau:** You know, 404s popping up post the website refresh, like you had some, but they looked like they were all intentional and like it was like, you know, it wasn't a lot of traffic at all.

**Kyle Gaudreau:** So like that wasn't the impact.

**Kyle Gaudreau:** I was looking at your articles, you know, looking kind of back to the Wayback Machine a bit, didn't see anything like notable on the articles themselves.

**Kyle Gaudreau:** I would have like drastically changed internal linking or anything of that nature, like some tiles changed, but there's no way that would cause a drop.

**Kyle Gaudreau:** So anyways, like long story short, it was a little bit hard to kind of like spot, but once we dove into the crawl data, that's like really where it stuck out.

**Kyle Gaudreau:** And so as you can see here, it's just like crawl requests have plummeted and the response speed has gone up significantly.

**Kyle Gaudreau:** And then additionally, like some headwinds on like the smartphone, Google bot rendering specifically, and are doing those crawls.

**Kyle Gaudreau:** And because it's mobile first indexing, that's, you know, not amazing.

**Kyle Gaudreau:** And so, you know, you can see it happened right around.

**Kyle Gaudreau:** Around the time y'all did the website refresh, but it just took a little bit more time to then show.

**Kyle Gaudreau:** And then what seemed to have happened, this part's, you know, a little bit less definitive, but in your site map, you then communicated like a pretty wide scale, like change as well, where, you know, like 600 plus articles, like had a last modified date of around the time your traffic started dropping more.

**Kyle Gaudreau:** So I think it was just a lot of like compounding negative signal post the refresh.

**Kyle Gaudreau:** Why particularly your crawl requests?

**Kyle Gaudreau:** Hopefully that's kind of what you're alluding to, Jesse.

**Kyle Gaudreau:** You know, I'm hopeful that's something you all can help us understand because I don't have like the visibility to truly unpack like the why behind this trend specifically.

**Jesse Schor:** So, yeah, a couple things, like as of like last week, because I noticed this stuff as well and was like digging into it.

**Jesse Schor:** And thank you.

**Jesse Schor:** Something I noticed last week, a couple of things.

**Jesse Schor:** So one thing was there were quite a few like non-webstacks related like scripts that were on pages from like what we copied it over.

**Jesse Schor:** So like we have developed like this like sanity kind of like template, so to speak, that has a lot of the like back end of what we create over and over again across like the different like fields that are in sanity, et cetera, like for the components we put together.

**Jesse Schor:** Anyway, I noticed there were a bunch of different tags that like weren't ours or like I couldn't account for.

**Jesse Schor:** Uh, and we removed those.

**Jesse Schor:** We like realized they were from some like other project.

**Jesse Schor:** Um, so like remove those, um, and pull.

**Jesse Schor:** That off.

**Jesse Schor:** I don't know if that was like playing into it, but like there was a lot on there that like was would have been new.

**Jesse Schor:** So those were removed like as of a week and a half ago or so.

**Jesse Schor:** The other thing that like I noticed was like we were getting a bunch of this like bot traffic.

**Jesse Schor:** So like in we use PostHog and in PostHog over like the last six months or so, we've been getting like more international traffic.

**Jesse Schor:** And like there wasn't like a ton of weight I was really putting into it because nothing like really seemed to look super like weird about it.

**Jesse Schor:** But digging into PostHog, I still think that a lot of that bot traffic has like fallen off and that was like impacting or seems to be impacting a lot of the like impressions.

**Jesse Schor:** And traffic sources that we're having.

**Jesse Schor:** And I can share that with you, what that kind of looks like.

**Jesse Schor:** And so those were kind of two things that seemed like they were impacting our impressions.

**Jesse Schor:** Now, in terms of the response times that you put there, that I definitely want to dig into more because that seems, yeah, odd and new.

**Kyle Gaudreau:** And also, just to clarify, too, like, what you're talking about in terms of, like, bots or whatever, like, wouldn't necessarily apply to the crawl requests from a Googlebot perspective, for sure.

**Kyle Gaudreau:** But, like, there's a clear, like, right around when you did this.

**Kyle Gaudreau:** So, like, I don't know.

**Kyle Gaudreau:** Certainly, like, I'm not saying what you shared wouldn't have an influence here.

**Kyle Gaudreau:** But I would be surprised if it was something, like, if we, like, just boiled it down to, like, the number one real cause, if it wasn't related to this.

**Kyle Gaudreau:** I don't

**Kyle Gaudreau:** And primarily, those other things probably don't help or muddy the data in some way.

**Kyle Gaudreau:** But yeah, from what I can gather so far, and like when you dig into this too in GSC, like you can, you know, see all sorts of different reports.

**Kyle Gaudreau:** And like there's some, you know, common patterns in there of like some things were like relatively flat or other things like tanked.

**Kyle Gaudreau:** If helpful, I can like show you a couple of things.

**Jesse Schor:** What do you think could be causing that like response time?

**Jesse Schor:** Could that be the additional scripts that were on there or like?

**Kyle Gaudreau:** I mean, if we're playing off that like hypothesis of like that you, like when did you fix that?

**Jesse Schor:** Like a week and a half ago or so.

**Kyle Gaudreau:** Yeah, because I mean like look at the orange line, right?

**Jesse Schor:** That's what I'm seeing.

**Kyle Gaudreau:** It's trending up, right?

**Kyle Gaudreau:** So it's not, it's not improving.

**Kyle Gaudreau:** And so that's where it's like, it feels like, you know, varying things.

**Kyle Gaudreau:** Things were happening, but, like, maybe, you know, somewhat unrelated.

**Kyle Gaudreau:** Like, I'm happy to pull in, like, you know, we have some, like, you know, we have some folks who are both engineers and SEOs and can dig in deeper.

**Kyle Gaudreau:** This is where, like, it's hard for me to say specifically why this trend would happen.

**Kyle Gaudreau:** Um, but clearly there's something that's kind of happening, like, you know, on the hosting side or, you know, I don't know if you are all on, like, Cloudflare or whatever, but that is not performing how it was prior to this website launching.

**Jesse Schor:** Yeah, I'm wondering, yeah, I'm wondering, um, if something is up with our builds that is triggering something like this.

**Jesse Schor:** Um, so, yeah, I need to look into that more because even I was noticing...

**Jesse Schor:** Like Nikon created a page that was like no index, like no crawl, no index that was showing up in our sitemap.

**Jesse Schor:** And I didn't know how that could be, but it was also like showing up almost like immediately.

**Jesse Schor:** And I'm wondering if that is potentially creating some issues here.

**Jesse Schor:** If we're creating new pages or updating new pages and every time we're building, it is updating the sitemapper or editing the whole sitemap and then kind of triggering a recrawl.

**Jesse Schor:** That would be something that would continuously compound because we're basically just requesting a sitemap crawl every single day on everything, multiple times a day.

**Jesse Schor:** So I want to look into that because, yeah, that's significant.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** And I'm.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Trying to pull up the reports, but like there's definitely some things that we're kind of like hiding out too that were, like that's just the top level trend, but there were some that were standing out that were a bit worse.

**Kyle Gaudreau:** Yeah, we're awesome.

**Kyle Gaudreau:** What the hell?

**Kyle Gaudreau:** Sorry, technical difficulties over here.

**Katya Luscomb:** Kyle, while you're pulling that up, there's a few quick follow-ups related to like content production pieces in just to make the most use of our time.

**Katya Luscomb:** I think in December with talking about like refresh content and pieces, it had come up of adding in an element to do like a TLDR and FAQs and needing...

**Katya Luscomb:** A way to like put those elements into sanity.

**Katya Luscomb:** And I was curious if you guys had been able to implement that and with the new site, if there's considerations, because we've got a bunch of refresh content coming at you pretty soon.

**Jesse Schor:** So remind me, what was like the update to make from that?

**Katya Luscomb:** So I believe from when I was looking back at the context, it was adding a section to sanity to like put the TLDR and the FAQ in.

**Katya Luscomb:** And I can go back and like pull some talking points if that would be more helpful.

**Katya Luscomb:** Because I know sometimes we can just put them in as like a standard H3, but I think the idea was to have a separate block for the FAQ.

**Jesse Schor:** So like a schema for it or because we have it as its own component now.

**Katya Luscomb:** Oh, it is.

**Katya Luscomb:** OK, that wasn't something that that we had seen.

**Katya Luscomb:** So I will I'll share that back with our publishing team and make sure that they know that that's.

**Jesse Schor:** Yeah.

**Jesse Schor:** I'm sorry, Katya, are you saying on the blog?

**Katya Luscomb:** Yeah, on the blog posts when we go in to publish those posts.

**Jesse Schor:** Let me double check, actually, because we might not have the module set up for FAQs there.

**Katya Luscomb:** Okay.

**Jesse Schor:** We have it throughout the rest of our site pages.

**Jesse Schor:** Cool.

**Jesse Schor:** Yeah, I'll check on getting that.

**Katya Luscomb:** Awesome.

**Katya Luscomb:** And then I think we were also talking about a module for TLDR at the top of the article as well.

**Katya Luscomb:** So those two pieces.

**Jesse Schor:** That would be probably the excerpt would be like the best place for that.

**Katya Luscomb:** Okay, perfect.

**Jesse Schor:** Which we have, and that's separated as its own field.

**Jesse Schor:** And that like shows at like separately at the top of the blog, kind of in its own little box.

**Katya Luscomb:** Perfect.

**Jesse Schor:** Awesome.

**Jesse Schor:** Cool.

**Katya Luscomb:** Kyle, did you want to, do you want to jump back in?

**Kyle Gaudreau:** Thanks for- Yeah.

**Kyle Gaudreau:** Yeah.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** Yeah, sorry.

**Kyle Gaudreau:** I got it up at the moment.

**Kyle Gaudreau:** This might not be super helpful, Jesse, but just you might be like already quite familiar with this area in GSC, but wanted to show.

**Kyle Gaudreau:** So if you just go into settings and then get out of the way, zoom, come on, open report under crawl stats, then that's where we get this data.

**Kyle Gaudreau:** So that's the chart we were showing you, but then you can dig in deeper into different hosts.

**Kyle Gaudreau:** And so, you know, going into the primary, there's just a few different like cuts of data beyond what we showed.

**Kyle Gaudreau:** But honestly, I don't know if like this is really going to be informative for you and the team or not.

**Kyle Gaudreau:** But, you know, like these were just some of the things that stuck out was, you know, the crawl requests or like returning the 200 code certainly plummeted.

**Kyle Gaudreau:** This might be intentional, but like, because like looking at these URLs, it's like all this like monitoring page primarily.

**Kyle Gaudreau:** Um, but this is something that just like had a bunch of crawl requests in the past and then like is non-existent now.

**Jesse Schor:** I don't know if that one matters, but again, just trying to like, there could be things as you're digging in that could stand out, uh, in terms of usefulness where like, uh, So with something like that, like, that's what I'm wondering as well, because I noticed some of that on some of our ads recently too, where there were, I was getting all these notifications all of a sudden that like, where they're not able to like reach this page.

**Jesse Schor:** And it was a page like what you're showing there that like is not something that is actually like a page.

**Jesse Schor:** Um, some of it was even like our old site, like on S like a staging site, uh, that like was on like our Vercel.

**Jesse Schor:** Um, so like for something like this, like this monitoring, Yeah.

**Jesse Schor:** If we try to go to that, like URL.

**Jesse Schor:** Like, I'm not even sure what would show up here, right?

**Kyle Gaudreau:** Yeah.

**Jesse Schor:** I don't know what this would be or why it was, like, being crawled on here in the first place.

**Jesse Schor:** So, like, is that something that is, like, is this actually an issue?

**Kyle Gaudreau:** That's the thing.

**Kyle Gaudreau:** It's, like, I don't know if this is going to be truly an issue or not.

**Kyle Gaudreau:** I don't know what this page was in the past.

**Kyle Gaudreau:** This, I do believe, isn't going to show you every URL, but it is pretty consistent that it's just this URL.

**Kyle Gaudreau:** So, I don't know if I'd really, like, there probably is some noise in here of, like, things that you guys cut.

**Kyle Gaudreau:** But there's certainly, like, you know, just playing around with a few different things and see if there's anything you can correlate back to what you all did.

**Kyle Gaudreau:** But, yeah, I didn't see anything, like, massive changes in, like, 404s or anything like that.

**Kyle Gaudreau:** But it just looks like, you know, it truly just, like, it is struggling.

**Kyle Gaudreau:** to crawl your website efficiently as it was in the past.

**Kyle Gaudreau:** So, yeah, I can ask around for some other folks if, like, they see this pattern of, like, where could you focus your time?

**Kyle Gaudreau:** Because, I don't know, it feels like something that's probably happening, you know, related to, like, hosting side of what you guys have set up.

**Kyle Gaudreau:** Or maybe something is inadvertently getting blocked or, hard for me to say related to that ads thing you mentioned.

**Kyle Gaudreau:** mean, certainly there's a lot of false flags that can come from ads because they try to index old URLs all the time.

**Jesse Schor:** Yeah, yeah, that's, like, independent for sure.

**Jesse Schor:** But, like, that's, it required me, like, I was getting these notifications of these issues that I just had to, like, basically, like, tell our ads, like, ad words, like, ignore.

**Jesse Schor:** And, like, then it was all fine.

**Jesse Schor:** But there's definitely, like, yeah, it seems like something.

**Jesse Schor:** Something is off.

**Jesse Schor:** And like, I'm even noticing it just from like traffic in general.

**Jesse Schor:** But even like our form fails, like at first it was like, let's let this lie for a couple of weeks and like see if just like this is kind of the normal growth of doing like a full overhaul.

**Jesse Schor:** But that's why like last week when I was looking into it and kind of seeing some weird things happening, I wanted like pulled some updates to make, but we're definitely still working through it.

**Kyle Gaudreau:** So this is helpful.

**Kyle Gaudreau:** I'm not sure this really gets you to the root cause, but just one other thing to flag.

**Kyle Gaudreau:** As I was taking a lot of this data out, was running it through Cloud Cowork just to bring together like, you know, understand the trend a little bit more, see what's happening.

**Kyle Gaudreau:** Etc.

**Kyle Gaudreau:** And I was trying to get Claude to go through and basically audit some of your pages as well.

**Kyle Gaudreau:** It was hitting a four or three and getting

**Kyle Gaudreau:** Blocked from Cloudflare, it seems.

**Kyle Gaudreau:** So don't know if that's intentional.

**Kyle Gaudreau:** Don't, I mean, Claude obviously is going to be different than Googlebot, but it probably do want things like that crawling your website from an AEO perspective as well.

**Kyle Gaudreau:** So I don't know if they're going to be truly related, but that just one other thing that stood out as I was digging into this.

**Jesse Schor:** Okay.

**Jesse Schor:** Yeah.

**Jesse Schor:** Yeah, that's interesting.

**Jesse Schor:** Cause we're definitely still getting traffic from like LLMs and even like, like we got a great conversion this morning from an LLM.

**Jesse Schor:** But yeah, there's definitely something going on that.

**Jesse Schor:** Yeah.

**Jesse Schor:** We need to like look into.

**Kyle Gaudreau:** Well, we'll continue to dig in our end and see if there is anything we can uncover to help focus your, your attention.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** yeah, this is definitely.

**Kyle Gaudreau:** We Okay.

**Kyle Gaudreau:** A tricky one, not a super common pattern we see.

**Jesse Schor:** Yeah.

**Jesse Schor:** I'm going to take a look at, I just messaged Nikon, so we can take a look at like our Vercel and see if there's any like reports in there that can give us some more insight into what might be happening and then, yeah, go from there.

**Jesse Schor:** I might follow up and see if like your team can also like look into it and validate anything that we're seeing.

**Kyle Gaudreau:** Yeah, for sure.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** I'm happy to bring in whoever and if we can get the right access, et cetera, so let us know.

**Kyle Gaudreau:** But yeah, I want to make sure we get this resolved ASAP for y'all because like the thing that, you know, just not to lose sight of is like not only is it down, it's like last week was like quite a bit down versus the prior, so it's getting worse each week.

**Jesse Schor:** Okay, cool.

**Jesse Schor:** Yeah, thanks for flagging this.

**Kyle Gaudreau:** Of course.

**Kyle Gaudreau:** Yep.

**Kyle Gaudreau:** Thank you.

**Kyle Gaudreau:** you.

**Kyle Gaudreau:** Thank Thank Thank you.

**Kyle Gaudreau:** you.

**Katya Luscomb:** Yeah, glad we could help and potentially give some insight.

**Katya Luscomb:** I also wanted to chat because I know we had an email thread going around potential like pushing into annual contract.

**Katya Luscomb:** And I know we renewed for the three months for this upcoming cycle.

**Katya Luscomb:** Wanted to check in.

**Katya Luscomb:** One of the things that I had originally planned to talk about was kind of a roadmap beyond Q1.

**Katya Luscomb:** And then we put a lot of our time into looking at this traffic consideration.

**Katya Luscomb:** But I do just want to call it and kind of like keep the conversation going around moving to an annual contract.

**Katya Luscomb:** And, you know, looking, like I said, we can put together kind of a roadmap for like six months and beyond, which I know is something that you had called out previously as being helpful.

**Katya Luscomb:** And yeah, just wanting to be candid that that's something that's still really high on our radar to keep talking about and align on.

**Jesse Schor:** Cool.

**Jesse Schor:** Yeah, I kind of I was like trapped.

**Jesse Schor:** Traveling all kind of during that like back and forth that you had.

**Jesse Schor:** So I have not like hopped back into it with like my CFO and talked to them about it.

**Jesse Schor:** Yeah, ultimately, I think like the thing that like he's going to want to be able to see is like what changes for like benefit wise based off of like the contract that we have now.

**Jesse Schor:** If like I'm just being fully like transparent with you of like if we're going to sign on for like one year, like how does that impact things for us like one way or another to like warrant making that change in the first place?

**Jesse Schor:** Because what we have right now with like essentially the three months is just like from the business standpoint, greater protection.

**Jesse Schor:** Now, like we have a great relationship, obviously, with Marcel and with you guys in general.

**Jesse Schor:** I don't see any signs of us changing or splitting things up, but I know that's going to be.

**Jesse Schor:** The hurdle for me to get over in any conversations with him is like what is the benefit to us switching up the way like we're currently working now if like the three-month increments are, you know, part of the original scope and engagement that we have.

**Jesse Schor:** Um, so I don't know what that can look like or if there's additional like value add to be able to like plug in, uh, or like if there's like a longer term like discount type thing that can be like included, but like that would be like the type of thing that like gets the CFO, my CFO to just be like, yeah, sure.

**Jesse Schor:** Like this is worth us changing what we currently have.

**Jesse Schor:** Um, like I said, don't expect anything to change when it's like, this is all just like, what is the like contractual, like legal jargon of things?

**Jesse Schor:** And that's kind of how he operates.

**Jesse Schor:** Um, but as far as the...

**Jesse Schor:** I definitely think that would be great.

**Jesse Schor:** I want to solve this thing because I've had the hunch that this has been an issue for us and I was kind of letting it lie, letting it kind of show itself as fully being an issue so we could go and solve it.

**Jesse Schor:** But I definitely want to get this prioritized and solved as soon as possible.

**Jesse Schor:** January was a slower month for us, just lead-wise.

**Jesse Schor:** And when I'm looking at our numbers, I would be expecting them to be continuing to go up from a traffic perspective across our channels and they're just not.

**Jesse Schor:** So I think we're past seasonality.

**Jesse Schor:** Clearly, something's off.

**Katya Luscomb:** So I want to get this solved.

**Jesse Schor:** And then I would love to get into that cadence of the content updates.

**Jesse Schor:** One thing I want to flag, though, I think you guys resolved.

**Jesse Schor:** The API thing yesterday, but, and like, I think like, I had some like internal conversations about it that like, this was like testing something out and like, this isn't something that's going to like continue to occur.

**Jesse Schor:** That being said, like, if something like it happens again, then like the permissions are probably going to have to get updated to just be like edit only, not publish.

**Jesse Schor:** And then it'll require like manual, you know, publishing and going in and updating.

**Jesse Schor:** So just like whatever can be done to try to keep an eye on that and make sure that doesn't happen, you know, would be helpful for preventing that.

**Jesse Schor:** I'm all for efficiently.

**Katya Luscomb:** Yeah, yeah.

**Katya Luscomb:** And I can give a little more context around that step.

**Katya Luscomb:** Essentially, the pipeline is the step that it's supposed to pause for us to hit go and to stage the content broke.

**Katya Luscomb:** And so as that pipeline was running, it auto-published.

**Katya Luscomb:** We have addressed.

**Katya Luscomb:** That's like our engineering team already jumped in and revised that step.

**Katya Luscomb:** And we're definitely keeping a really close eye because, yeah, certainly don't want something like that to happen for you or for us again.

**Jesse Schor:** Definitely.

**Jesse Schor:** Appreciate that.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** No worries.

**Katya Luscomb:** I think we all spotted it right about the same time and we're digging in.

**Katya Luscomb:** So appreciate that you guys called it out as well.

**Jesse Schor:** Yeah.

**Jesse Schor:** And I think like when we're talking about like the roadmap, like hitting like this kind of cadence of these like different areas, like prioritizing sanity as a topic, like those are all like that I want to get into that cadence for sure.

**Jesse Schor:** And then I know you mentioned like the LLM visibility, but like if there's also like things that we can do to like prioritize the report, like from the reporting standpoint on like leads pipeline generated like that.

**Jesse Schor:** That's something that like is like still like kind of like a gray area or black box for us in relation to like our direct work.

**Jesse Schor:** And like it always kind of will be that like is clear, but even just like I don't know if you guys are moving away from Scrunchie, but some of the like prompts and things I was looking at like in Scrunchie, using that as like a way to set some of like our content strategy and direction I think like would be helpful because we're just getting like high quality leads from LLM referred traffic.

**Jesse Schor:** And like that seems like the easiest source for us versus focusing so much on just getting top of the funnel conversions from like even just like organic alone.

**Jesse Schor:** So as we kind of like think about those types of things, that would be great to kind of see in the roadmap, like how can we better utilize the monitoring and visibility that we have in there to like tie directly back?

**Katya Luscomb:** Yeah, absolutely.

**Katya Luscomb:** And that's actually one of the things in the Check That demo that I'm going to send over, because Check That is going to be a shift.

**Katya Luscomb:** It's got some added benefits that like sanity doesn't necessarily address.

**Katya Luscomb:** Kyle, I see you off.

**Katya Luscomb:** you want to pop in?

**Kyle Gaudreau:** Yeah, it's probably worth catching you up, Jesse, at some point of like, why we did the Check That launch.

**Kyle Gaudreau:** Because yes, like there's the things that we saw in AI visibility tools that led us to create this, you know, things like informing prompts in a different way, because it's kind of hard to prompt selection itself is a challenge.

**Kyle Gaudreau:** And so we introduced some elements for that.

**Kyle Gaudreau:** But the other pieces related to where it's going to go into tying into the content OS.

**Kyle Gaudreau:** And a lot of that is

**Kyle Gaudreau:** Flagging opportunities in a more systematic way that can enable us to kick off work for content that's informed by the signals that check that is capturing.

**Kyle Gaudreau:** Not that we have to wait for that to do what you're talking about, but that's a lot of like the same problem a lot of brands run into that we're building as well.

**Kyle Gaudreau:** And so I think there's certainly a lot of things we can unpack of, you know, what are the priority question patterns?

**Kyle Gaudreau:** I tend to think about like different themes, primary question patterns, and like, how can we layer that in with the content that we're doing?

**Kyle Gaudreau:** And then also be mindful of like, it's both an SEO and AEO play.

**Jesse Schor:** Yeah.

**Kyle Gaudreau:** And we're bringing this together.

**Kyle Gaudreau:** But, you know, there's a lot of different social signals we can leverage and just make sure that's informing the work and that it's not just prompts.

**Kyle Gaudreau:** It's not just keywords.

**Kyle Gaudreau:** And it's kind of the happy meeting between the two.

**Kyle Gaudreau:** Not that we can't do experiments outside of that and happy to, you know, make sure we're, you know, feeling better about like a roadmap around that of like, what is.

**Kyle Gaudreau:** Like a true more AEO based experiment, which certainly we've talked about with a few customers.

**Kyle Gaudreau:** I, you know, I'd say, I'd say that the, the challenge there is like, certainly there's things that we can do from an onsite perspective and they can move the needle, but also the offsite matters quite a bit as well.

**Kyle Gaudreau:** And so, you know, a lot of the talk recently has been the effect of YouTube being the strongest signal lately.

**Kyle Gaudreau:** And I'm seeing that from a lot of people lately.

**Kyle Gaudreau:** Um, and so anything you all are doing around videos, I think that would, if we really, really want to move the needle, yes, we can do all the stuff I mentioned before, but like, how can we collaborate with you on like thinking about how your videos take shape on YouTube?

**Kyle Gaudreau:** We can, uh, collaborate on like, what are those different like, um, themes we're going after those keywords and it needs to be user first.

**Kyle Gaudreau:** It needs to be useful for your audience, but also make sure it has some of those layers that is going to help add to your visibility as well.

**Kyle Gaudreau:** Um, cause that right now seems to be by far the, the biggest needle driver that folks are talking.

**Jesse Schor:** Yeah, definitely.

**Jesse Schor:** mean, between YouTube and Reddit, those are two areas where we don't have a strong presence.

**Jesse Schor:** And I'm fully game to do those things.

**Jesse Schor:** And Eric and I have spent a lot of time even just talking about Reddit and exploring, building out more content around that.

**Jesse Schor:** And so if that is a route that makes sense for us to go down, then we can take ownership of that.

**Jesse Schor:** But figuring out how does that best fit into the bigger picture of what we're doing, that would be helpful.

**Jesse Schor:** So any strategies you guys have around that, even if it's broad, but just things that you guys are seeing, that would be good for us to take into consideration.

**Jesse Schor:** That stuff would be helpful.

**Jesse Schor:** Because we're game to push into those things.

**Jesse Schor:** But it's just kind of like, what's the best way?

**Kyle Gaudreau:** And how does that best fit into the broader strategy that we have with our content?

**Jesse Schor:** How can we maximize the content that we have there?

**Jesse Schor:** And the other thing that Eric and I have been talking

**Jesse Schor:** Talking about lately too is just around like not only the like prompt keyword monitoring, but like just more social listening in general so that like we can insert ourselves into the conversations that are happening better.

**Jesse Schor:** Many times like we're having conversations even more like I would say like backdoor, like behind closed doors that are really interesting just because like we have a visibility into a lot of the websites that are feeling or impacting the trend.

**Jesse Schor:** Same way you guys see from like content, right?

**Jesse Schor:** Like you're kind of on the front line.

**Jesse Schor:** So like you're first responders in many ways.

**Jesse Schor:** And so a lot of that though just winds up like living in our gong or living in like separate places if we don't know that like there's something there for us to like do something with now.

**Jesse Schor:** And so having social like some kind of like social listening I think like allows for us to jump into conversations or even set conversations more and then monitor.

**Jesse Schor:** Whether or not those are impactful or sticky discussion points.

**Jesse Schor:** so, again, we don't really have a strong tool for that.

**Jesse Schor:** I'm open to adding tools for it.

**Jesse Schor:** If it's helpful, if you guys have tools that can help with that, or if the things that can come up in this LLM, like visibility tracking can be useful, then that's something else we're open to.

**Jesse Schor:** So any directional ideas, doesn't necessarily have to be like, this is the roadmap, this is what the next six months look like.

**Jesse Schor:** But even if it's like right now, if we're going to focus our efforts somewhere and point to a North Star, this should be it.

**Jesse Schor:** And this is how we should approach it and learn.

**Jesse Schor:** And then adapt from there.

**Jesse Schor:** That totally works.

**Kyle Gaudreau:** I think the other thing that, I mean, perhaps, you know, this has already been happening in some of the recent conversations, but where it can become even more powerful is like layering in the added business context you all have.

**Kyle Gaudreau:** And like what is driving, you know, the.

**Kyle Gaudreau:** Best deals for you at the moment, like hypothetically, like if you just give us some Gong calls, we could get aspects of that, but we're not going to like really get that view.

**Kyle Gaudreau:** But like, are, are there certain patterns of just like who makes a better customer of like their attributes, their, the CMSs, the challenges they care about, et cetera, to layer on, on top of like the frequency and the patterns we see from those sources.

**Kyle Gaudreau:** And so, you know, if we can just attack it from multiple angles, like get your Gong calls, see what we can get from the Reddits of the world, et cetera, get that qualitative insight from you of like, you know, the patterns you're seeing that can help us inform ultimately, like, where do we want to place a couple bets?

**Jesse Schor:** Think about those themes.

**Jesse Schor:** And then like, what are the varying sources to attack those themes from like a content standpoint?

**Jesse Schor:** Yeah, totally.

**Jesse Schor:** And like that, I'm open to doing that.

**Jesse Schor:** And maybe that makes sense for us to do next week, like as like separate, like, it's maybe been a while since like we've done like that level of like discovery call and maybe like Katja, like that's a good place for.

**Jesse Schor:** us to like at least earmark every quarter is like what are some of the like trends or things we're seeing or every month if we just want to like carve out some time I can share a lot of those things just anecdotally but then also like you know we have some of those things in Gong Call recordings that we can share it's just we're generating so much all the time right that like it's hard to know like what's actually valuable for you guys.

**Jesse Schor:** And also in many ways like we can go out and get things that we think are valuable so like if we can create this kind of two-way street where that context sharing is happening the things that like we're seeing are being implemented in the content we're putting together but also like we're listening and hearing for new things that like aren't even coming up then like I think it can be a lot more efficient and some of those things we're already trying to it's like with the sanity like we know the partnerships have such a big impact sanity has been such a huge partner for us and those are many of the conversations that we're having with folks.

**Jesse Schor:** Today, just because like it perfectly aligns with the like AI enablement that so many people are coming to us for.

**Jesse Schor:** So like we're already kind of trending towards some of those things.

**Jesse Schor:** But if there's ways that we can make that better or even increase the volume across the areas that that's happening on, then I'm totally game.

**Kyle Gaudreau:** Yeah, that makes sense.

**Kyle Gaudreau:** I think, yeah, you know, where we're going and layering in more lead data insights as well can just continue to help us evolve that.

**Kyle Gaudreau:** And yeah, I like the idea of like just making sure we have some sort of frequency.

**Kyle Gaudreau:** We're having those conversations because naturally it's going to shift over time and we have to just continue to adapt what we're doing.

**Kyle Gaudreau:** And for that to inform like that, that to me is like how you have a more meaningful roadmap of like what's coming next.

**Kyle Gaudreau:** Right.

**Kyle Gaudreau:** It's not just guessing.

**Kyle Gaudreau:** It's based off the signals we're getting from a variety of places.

**Jesse Schor:** Yeah.

**Kyle Gaudreau:** Cool.

**Kyle Gaudreau:** Well, happy to partner with Katya on some of that AEO stuff.

**Kyle Gaudreau:** I have a few ideas coming to mind.

**Kyle Gaudreau:** And.

**Kyle Gaudreau:** And, you know, getting access to Gong Calls would be amazing.

**Kyle Gaudreau:** Like, there's different ways, obviously, approaching that.

**Kyle Gaudreau:** But sorry if you've already done this with us and I'm just not aware.

**Kyle Gaudreau:** But if we could just, like, get, like, I don't know if you, like, organize them in some way of, like, the top hits or whatever that you can, like, export for us that we can just, like, run through.

**Kyle Gaudreau:** Because, yeah, between, again, like, the Reddit signals, the Gong Calls.

**Jesse Schor:** Yeah.

**Jesse Schor:** I that's a big batch over.

**Jesse Schor:** I mean, we send over now, like, more, like, intentional or driven ones that are related to the content we're talking about.

**Jesse Schor:** But if it's more helpful for you guys to just get, like, kind of a batch of some, like, good, like, recent sales calls or certain client calls, there's definitely some, like, consistent themes.

**Kyle Gaudreau:** Cool.

**Jesse Schor:** So, like, yeah, those are all things we're tracking for.

**Jesse Schor:** So I can send over kind of, like, a batch and then we can have that conversation as well based off, like, some of the things you guys take away and we can validate that.

**Kyle Gaudreau:** Sounds good.

**Katya Luscomb:** good.

**Katya Luscomb:** Yeah, that'd be great.

**Katya Luscomb:** Thank you, Jesse.

**Jesse Schor:** Cool.

**Katya Luscomb:** Awesome.

**Katya Luscomb:** Well, appreciate all the time and digging in.

**Katya Luscomb:** I know there was a lot of different aspects we covered.

**Katya Luscomb:** Was there anything else top of mind for you, Jesse and Eric, before we hop off?

**Jesse Schor:** No.

**Jesse Schor:** Yeah.

**Katya Luscomb:** Cool.

**Katya Luscomb:** All right.

**Katya Luscomb:** Well, thank you, guys.

**Katya Luscomb:** Appreciate the time.

**Jesse Schor:** See you, Bye-bye.

**Jesse Schor:** See you, guys.

**Jesse Schor:** Thanks.

**Jesse Schor:** Bye-bye.
