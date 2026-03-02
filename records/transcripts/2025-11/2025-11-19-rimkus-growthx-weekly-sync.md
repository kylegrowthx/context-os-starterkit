# Rimkus <> GrowthX - Weekly Sync

<metadata>
date: 2025-11-19
time: 15:30 UTC
duration: 35 minutes
organizer: matthew.alves-hill@growthx.ai
participants: Matthew Alves-Hill, Jakub Rudnik, Jennifer Bulmash, Alishia Natiello
fathom_recording_id: 102802414
fathom_url: https://fathom.video/calls/478522555
share_url: https://fathom.video/share/uSEiLojTHZcHYMaxKDfAwygU_kv1e_zx
source: fathom
enriched_on: 2026-03-02 14:30 UTC
</metadata>

---

## Summary

GrowthX and Rimkus reviewed critical technical SEO issues (1,300+ 404 errors, 88 5xx errors, slow mobile speed, canonical tag problems) that are blocking full audits due to WordFence firewall restrictions—findings will be shared with their new web agency. The team confirmed a 5-article weekly publishing cadence starting next week (2 BES, 2 Forensics, 1 high-priority refresh) and aligned on process improvements, including Airtable automations and a workflow tutorial to resolve review delays between Rimkus's approvals and GrowthX's publishing schedule.

---

## Context

Rimkus is a GrowthX content marketing client where Matthew Alves-Hill leads the day-to-day delivery and Jakub Rudnik oversees technical strategy and editorial direction. This is a weekly sync covering content production progress (22 articles published with 12 generating traffic) and the technical health of Rimkus's website. The engagement includes a 73-item "Ready to Start" assignment pipeline, 31 high-priority refresh articles, and ongoing forensic keyword research. Rimkus is contracting a new web agency by year-end to address site-wide infrastructure issues, making the technical audit findings and workflow improvements critical to maintaining publishing velocity.

---

## Relevance

**To GrowthX Delivery:**
- WordFence firewall is blocking GrowthX's crawl tools (Screaming Frog, Ahrefs), forcing workarounds and limiting technical audit scope. Requires IP whitelisting to unblock full analysis.
- Process bottleneck identified: disconnect between Rimkus's review completions and GrowthX's publishing pipeline. Airtable automations and a workflow tutorial will resolve this.
- 5-article weekly publishing cadence now confirmed, with content mix locked for next week (2 BES, 2 Forensics, 1 refresh).

**To GrowthX Business Development:**
- 22 articles published with 12 already driving traffic signals healthy account momentum and content-market fit.
- Rimkus is investing in a new web agency by year-end to fix critical site infrastructure—GrowthX's technical findings position them as strategic advisor for the handoff.
- Large content pipeline (73 ready-to-start assignments, 31 refreshes) indicates strong expansion opportunity within the engagement.

---

## Overview

- **Critical Tech Issues:** Rimkus's site has major SEO problems (1,300 404s, 88 5xx errors, slow mobile speed) that are hurting performance and will be shared with their new web agency.
- **Audit Blocked:** GrowthX's technical audit is blocked by the WordFence firewall. Rimkus must whitelist Jakub's IP to enable a full analysis.
- **Content Cadence:** The weekly publishing goal is 5 articles. Starting next week, the mix will be 2 BES, 2 Forensics, and 1 high-priority refresh.
- **Process Fixes:** To resolve review delays, Matthew will create an Airtable Loom tutorial and set up notification automations.

---

## Key Topics

### Technical SEO Audit Findings

  - **Blocker:** The WordFence firewall blocks GrowthX's tools (e.g., Screaming Frog, Ahrefs), preventing a full technical analysis.
      - **Impact:** This causes false-positive errors and underreports page counts (e.g., Ahrefs sees \~280 pages vs. the actual \~1,000).
  - **Critical Issues Identified:**
      - **404 Errors (1,300+):** A massive number of dead pages, likely from a past migration (e.g., `experts` → `expert` URL changes).
      - **5xx Server Errors (88):** All from the `legacy.rimkus.com` subdomain, which was recently shuttered.
      - **Canonical Tag Issues:** WordPress is creating indexable duplicate pages from URL query strings, bloating the crawl budget.
      - **Slow Mobile Speed:** A site-wide issue with 11–12 second load times, significantly hurting mobile rankings.
      - **Underutilized Footer:** The footer lacks key architectural links, missing a major SEO opportunity.
  - **Context:** Alishia confirmed these issues are a key reason for contracting a new web agency by year-end.

### Content Production & Process

  - **Performance:** 22 articles are now published, with 12 already generating traffic.
  - **Pipeline:**
      - **New Content:** 73 approved assignments are in the "Ready to Start" bucket.
      - **Refreshes:** 31 high-priority articles are in Airtable's "Refresh" view.
      - **Forensics:** Keyword research is in progress for new forensic clusters.
  - **Review Process & Cadence:**
      - **Problem:** A disconnect between Rimkus's completed reviews and GrowthX's publishing status.
      - **Goal:** A 5-article weekly publishing cadence, with reviews completed by the Wednesday sync.
      - **Resolution:** Matthew will investigate the status of 6 reviewed articles and create an Airtable Loom tutorial to clarify the workflow.

---

## Action Items

**Alishia Natiello (Rimkus)**
- Email web agency Jakub's IP; request WordFence whitelist; notify Jakub to re-crawl
- Email Vitali Edrenkine Jakub's technical audit; discuss priorities
- Review remaining 6 articles in Airtable; greenlight for publish

**Matthew Alves-Hill (GrowthX)**
- Set up Airtable automations to notify Alishia/Jen on review-ready articles
- Publish 1 BES article immediately; align with Lawrence on 5/week cadence
- Record and share Loom re: Airtable workflow with Alishia & Jen
- Send async update to Jen re: next week's progress

**Jakub Rudnik (GrowthX)**
- Rerun technical audit once IP is whitelisted; provide full report to Rimkus

---

## Transcript
**Matthew Alves-Hill:** Hello.

**Alishia Natiello:** Good afternoon to you.

**Matthew Alves-Hill:** Yeah, good very early morning to you.

**Matthew Alves-Hill:** Yeah.

**Matthew Alves-Hill:** this, half past seven?

**Alishia Natiello:** Yep, yep.

**Alishia Natiello:** Sun just came up like 30, 35 minutes ago.

**Matthew Alves-Hill:** Okay.

**Matthew Alves-Hill:** You're in early bed or?

**Alishia Natiello:** I can be, I can be, yeah.

**Alishia Natiello:** Okay.

**Alishia Natiello:** Like, when I need to be, it's like, yep, let's just get up and do it.

**Alishia Natiello:** The benefit is then I can leave a little earlier from work.

**Alishia Natiello:** Yeah, yeah.

**Matthew Alves-Hill:** Yeah.

**Matthew Alves-Hill:** That's like, we make a joke, I'm in Cape Town and Capetonians are always up early and then the rush hour is actually at like 2.30 in the afternoon.

**Alishia Natiello:** Everyone's like, yeah, come out there, go to the beach.

**Matthew Alves-Hill:** Hi, Jen.

**Jennifer Bulmash:** Hey, morning or afternoon or whatever time it is, wherever y'all are.

**Alishia Natiello:** We were just running through that then.

**Alishia Natiello:** Well, you know, I just picked up on what y'all are talking about.

**Alishia Natiello:** That's awesome.

**Matthew Alves-Hill:** Jen, you're in Texas, right?

**Jennifer Bulmash:** Yeah, yeah, I'm down in Houston.

**Matthew Alves-Hill:** Okay.

**Jennifer Bulmash:** But I'm not from here.

**Jennifer Bulmash:** I don't claim it.

**Matthew Alves-Hill:** Important distinction.

**Matthew Alves-Hill:** Okay.

**Matthew Alves-Hill:** Where are you from originally?

**Jennifer Bulmash:** The Kansas City area.

**Matthew Alves-Hill:** So, just a couple hours north.

**Matthew Alves-Hill:** Yeah.

**Jennifer Bulmash:** Okay, cool.

**Alishia Natiello:** We've all moved because, yeah, I'm not from California.

**Alishia Natiello:** I'm from, like, New Jersey, Pennsylvania area in the northeast.

**Matthew Alves-Hill:** Okay.

**Matthew Alves-Hill:** I actually grew up, I spent seven years in the States in Connecticut when I was a kid.

**Matthew Alves-Hill:** So, there's a bit of a twang.

**Matthew Alves-Hill:** I am English, but there's a bit of a weird twang, third culture kid.

**Matthew Alves-Hill:** Cool.

**Matthew Alves-Hill:** I wanted to introduce you guys to Jakub.

**Matthew Alves-Hill:** I don't think you've met yet.

**Jennifer Bulmash:** Hi, Jakub.

**Matthew Alves-Hill:** is managing director here.

**Matthew Alves-Hill:** He's been working on your technical stuff.

**Matthew Alves-Hill:** Jakub, you want to do a brief intro?

**Jakub Rudnik:** Yeah, for sure.

**Jakub Rudnik:** Jakub Rudnik, nice to meet you both.

**Jakub Rudnik:** I'm in Cleveland, Ohio.

**Jakub Rudnik:** Don't claim it.

**Jakub Rudnik:** Just moved here like six weeks ago.

**Jakub Rudnik:** I'm from Chicago and I've lived there for 14 years.

**Jakub Rudnik:** It's a longer story.

**Jakub Rudnik:** But yeah, I live in Cleveland now.

**Jakub Rudnik:** And yeah, I've been a managing director here since March.

**Jakub Rudnik:** It was our first one, actually.

**Jakub Rudnik:** And before that, we ran content at SEO at a lot of different software companies, primarily.

**Jakub Rudnik:** So kind of got my start as a journalist and went to G2, which was G2 Crowd at the time.

**Jakub Rudnik:** And like just saw a content SEO at a big enterprise scale there and a lot of big content team.

**Jakub Rudnik:** I've done that at a couple of different stops between here and there over the last decade.

**Jakub Rudnik:** So yeah, that's me as a, like, that's my credentials or whatever.

**Jakub Rudnik:** I'm to work on this.

**Jakub Rudnik:** think we're actually like.

**Jakub Rudnik:** In the mode of moving how we resource and things, but I think I'll be largely working, I'll be the director that you'll work with the most, but we're kind of pooling resources.

**Jakub Rudnik:** So my expertise, definitely content strategy, content, like in the editorial sense, which is a lot of what you're doing with us, but certainly go into the technical, have experience with link building, though that's less of what we do here.

**Jakub Rudnik:** But there will be other folks, like depending on what your projects are, what other marketing areas you have, you may see other directors with different skill sets, know, something on the brand side, we'd pull someone in from that perspective, or there was, I don't know, there's just different projects and we'll continue to build out where our strengths are, but that's where mine are.

**Jakub Rudnik:** for something like your, you know, upfront strategy, like that was said in strategy sprints, but I come in and also look at things from that perspective and how we'll carry that out.

**Jakub Rudnik:** But then, you know, your technical audit, that would be something like I'll come in for and make those recommendations.

**Jakub Rudnik:** And we'll obviously talk about some of that today and continue to do that over the coming weeks as there's been hiccups.

**Jakub Rudnik:** But again, nice to meet you.

**Jakub Rudnik:** That's where I come in.

**Jakub Rudnik:** And yeah, it's definitely like Matt does a lot of the day-to-day, week-to-week, and organizes both like the editorial team and then connects to me.

**Jakub Rudnik:** when there's either something to flag or a new opportunity, you know, he'll typically file a ticket, we have a conversation, then you'll see me in those type of calls.

**Jennifer Bulmash:** Okay.

**Jennifer Bulmash:** Most importantly, who is behind you?

**Jakub Rudnik:** Oh, this is Penny, who's being really cute right now.

**Jakub Rudnik:** I hadn't even noticed.

**Jakub Rudnik:** I kind of like minimized the window.

**Jakub Rudnik:** She'll either sit like that or bark at a mailman.

**Jennifer Bulmash:** There's like basically no in-between.

**Jennifer Bulmash:** So very, she That's what I do all day too.

**Jakub Rudnik:** So yeah, I put the cushion, just trying to get her in here as we get this new office set up and it's working.

**Jennifer Bulmash:** It's good for the client calls for sure.

**Alishia Natiello:** Excellent.

**Jakub Rudnik:** Good vibes.

**Matthew Alves-Hill:** Yeah.

**Matthew Alves-Hill:** Awesome.

**Matthew Alves-Hill:** Cool.

**Matthew Alves-Hill:** So we'll dive into the agenda.

**Matthew Alves-Hill:** Let me just pull that up.

**Matthew Alves-Hill:** Too many desktops open here.

**Matthew Alves-Hill:** Cool.

**Matthew Alves-Hill:** Maybe this will be a little different from before, but largely we're going the same way.

**Matthew Alves-Hill:** So just like a quick recap from last week.

**Matthew Alves-Hill:** So we asked you guys to go through those forensic topics.

**Matthew Alves-Hill:** Jen, to help us with the clusters, super helpful.

**Matthew Alves-Hill:** Really appreciate that.

**Matthew Alves-Hill:** And then obviously the article review.

**Matthew Alves-Hill:** And then for us, on the editorial side anyway, it was, we wanted to get seven more published, which we have done.

**Matthew Alves-Hill:** So it's actually great.

**Matthew Alves-Hill:** We actually overpublished last week to catch up.

**Matthew Alves-Hill:** The keyword research piece for those forensic clusters that you shared.

**Matthew Alves-Hill:** And then the refresh sync was basically bringing all those high priority refresh opportunities that we'd identified into the Airtable so that everyone knows where everything is and it's all in one place.

**Matthew Alves-Hill:** Airtable can be a little bit fun.

**Matthew Alves-Hill:** So yeah, we have a clean, tidy air table.

**Matthew Alves-Hill:** Jakub, I put the technical audit up front.

**Matthew Alves-Hill:** I can go into editorial first, but Jen, guys, where do you want to start?

**Matthew Alves-Hill:** Because I know obviously technical audit is top of mind.

**Alishia Natiello:** Do you want to start there?

**Alishia Natiello:** Yeah, let's go with that.

**Matthew Alves-Hill:** Okay, cool.

**Matthew Alves-Hill:** Jakub, I'll let you take over the screen.

**Jakub Rudnik:** Okay, so this is linked in the agenda.

**Jakub Rudnik:** So I would use, I'll give you the high level here, ask questions, and then obviously, like, I want to talk through next steps because this is, I've identified a bunch of big things, but I can't get into a lot of the pieces I would normally be able to analyze and make recommendations on because of the firewall, essentially.

**Jakub Rudnik:** I've been able to do a decent amount, but even, we'll get into that.

**Jakub Rudnik:** So I'll start with that issue.

**Jakub Rudnik:** I'm even blocked from, like, a lot of me into your WordPress right now.

**Jakub Rudnik:** Everything is unblocked, rimkus, yeah, WordPress login, like, I can't even get in, the crawl, I can show you my screaming frog, just for, like, I run this, usually I can just run this overnight, and I come back and I can just get it done, and every time I run it, like, it runs, and there's a lot here, but you can see, like, status code 403, forbidden, all this has been blocked for me, and I've, like, turned down the settings as slow as possible.

**Jakub Rudnik:** It's, like, giving me all these false flags, this one's just giving me forbidden, last time I ran it, it was giving me all these server errors, so I had, like, started writing recommendations on, like, your server is crashing on all these pages, like, none of that was happening, we were just being blocked by the firewall, so I've had just, I've, I don't know, run four or five of these, and I use a couple different SEO tools, well, screaming frog on the technical side, but Ahrefs on, like, keyword research and things, and it, I'm noticing, like, there's just inconsistencies on what we have access to, and I think it's just because it blocks Ahrefs drop.

**Jakub Rudnik:** Other crawlers all the time, like it thinks you only have 280 pages, but in reality, you know, there's a thousand or so pages on the whole site.

**Jakub Rudnik:** So there's just things that the firewall is blocking.

**Jakub Rudnik:** And so I think, very frankly, I've not had this level of issue with either client or internal because when I'm internal, I can just like avoid these things.

**Jakub Rudnik:** But I believe if you go into WordFence, which I'm not able to anymore, and add my IP, which is right here, even just for a few days, we should be able to, my understanding, that should alleviate things.

**Jakub Rudnik:** I've also had a couple feelings I'd be able to move forward and haven't been this week.

**Jakub Rudnik:** So I think this will work.

**Jakub Rudnik:** I will definitely have to test it.

**Jakub Rudnik:** We'll take next steps if needed.

**Jakub Rudnik:** But I believe if you can add this to WordFence, we should be able to complete things this week.

**Jakub Rudnik:** So sorry, a little bit of like a lot, showing you a lot there.

**Jakub Rudnik:** But that's what's blocked me from, like, having even more and some more details.

**Alishia Natiello:** The second piece is, like, it's a...

**Alishia Natiello:** Also, after this call, I'm hopping on with our...

**Alishia Natiello:** A website agency, so I will alert them right away so we can prioritize that.

**Jakub Rudnik:** Okay, thank you so much.

**Jakub Rudnik:** And I feel confident that that's not stopping, it's stopping SEO tools and stopping me, but it's not blocking crawlers from Google or from LOM, so that shouldn't be affecting.

**Jakub Rudnik:** Like, it's something that you do want, so someone like me that's not doing it for your good, like, who's trying to, like, you for other reasons.

**Jakub Rudnik:** So I totally understand why it's there.

**Jakub Rudnik:** It's just for this purposes, and, yeah, that's just blocking stuff.

**Jakub Rudnik:** So, again, apologies for it and thanks for the patience.

**Jakub Rudnik:** We are, there's still plenty to work through, and I don't want to call out, but I can't get into some of the nitty-gritty or have a ton of confidence on some things.

**Jakub Rudnik:** One of big issues, you have these 5xx errors, and there's a bunch of these have been, I've just linked the raw files down here.

**Jakub Rudnik:** I don't know your exact setup yet, just heard you have the web agency, and I don't know who will, like, be fixing this or who we'd be partnering with.

**Jakub Rudnik:** We wanted to get some of these alleviated, but we wanted to give the raw files for whoever would be doing that, while also giving the high-level overviews.

**Jakub Rudnik:** Here, each of these kind of opens into different sections and things, but basically there are server errors, and this one looks like it's coming from, sorry, a lot of tabs.

**Jakub Rudnik:** These 5XX errors from a legacy version of the site, they're all this legacy.rimkus.com, basically just have to set up a redirect, like a wildcard redirect to push these all to the live page.

**Jakub Rudnik:** These looked, I spot-checked, and they all look to have like a partner page, or like a matching pair that is live.

**Jakub Rudnik:** This is, you just don't want these server errors bogging down crawlers, sending Google these really negative signals.

**Jakub Rudnik:** This should be pretty easy.

**Jakub Rudnik:** looked like 88 total pages, but a big...

**Alishia Natiello:** And we did, we did just recently, like last week or the week before, completely shutter that page, the legacy page.

**Alishia Natiello:** We had kept it up from when we last published the new version of our site just about a year ago.

**Alishia Natiello:** But yeah, as you can see, it's now just been, we were like, we don't need it anymore.

**Alishia Natiello:** It's taking up space and causing these issues too.

**Jakub Rudnik:** Yeah, that makes sense.

**Jakub Rudnik:** That aligns with the signals that I've seen.

**Jakub Rudnik:** You know, some of it, I don't have the full history, but just basically redirect any of those pages to the non-Legacy version and then set a wild card for any stray pages.

**Jakub Rudnik:** So all legacy will just redirect to your rimkus homepage or whatever it is.

**Jakub Rudnik:** But just get these redirected so you don't have this type of, like, you don't want Google finding this and penalizing the whole site for something that's, you know, is already gone and you have a clear target to align to.

**Jakub Rudnik:** Yep.

**Jakub Rudnik:** There's a lot of 404.

**Jakub Rudnik:** It's like a thousand, if I'm remembering correctly.

**Jakub Rudnik:** Let's go back a

**Jakub Rudnik:** Page, and you'll see me using GSC more than some of these other tools.

**Jakub Rudnik:** Yeah, 4.4 is 1,300 pages, and so the 5XX were crawled less recently, but some of this is being crawled like this week, and Google is finding these variations of pages, and I think it's often like expert to expert.

**Jakub Rudnik:** It looks like folders or things were just changed slightly.

**Jakub Rudnik:** I'm not sure if I'll be able to recreate it based on the firewall stuff, so you'd have to go in.

**Jakub Rudnik:** I think can, doesn't matter, but these, yeah, there's like slight changes to URL structure, I believe, and just.

**Alishia Natiello:** they changed from previously like experts to expert, yeah, stuff like that with the site from a year ago, and then yeah, the language URL.

**Jakub Rudnik:** Yeah, and so we want to get those, we definitely do not want to.

**Jakub Rudnik:** Google's seeing this many pages that aren't, I hate doing like redirects of this magnitude too, but that happens when you make big migrations across tens of thousands of pages, but having this many pages that Google's finding is dead pages and potentially internal links as well.

**Jakub Rudnik:** That's what I can't give you a full report on, like I need Screaming Frog to do that piece, but you can still tell these aren't working and Google's finding them as of this week even.

**Jakub Rudnik:** And so a huge one there, probably my number one, maybe I should move this up as like the higher priority.

**Jakub Rudnik:** It's a bigger lift to get right, but I would call that one a bigger priority.

**Jakub Rudnik:** There's some canonical stuff.

**Jakub Rudnik:** Let's find where the best thing to show off.

**Jakub Rudnik:** Like, so basically WordPress is using, there's a couple different strings that it adds to each of these pages, depending on like what the filter is or something.

**Jakub Rudnik:** And basically you wouldn't want to be creating new pages or definitely not indexable pages, pages.

**Jakub Rudnik:** Just for all this, it's just creating duplicates and it's like bloating your crawl budget to simplify.

**Jakub Rudnik:** And so all these are turning into like multiple pages depending on the variance.

**Jakub Rudnik:** And you don't need that.

**Jakub Rudnik:** You need either like a noindex or not turn this into a specific page.

**Jakub Rudnik:** So more detail here.

**Jakub Rudnik:** Yeah, I would not have a follow not index and canonical back to like the original page.

**Jakub Rudnik:** And this happens a lot.

**Jakub Rudnik:** I'll be able to give you a full overview here, but almost like so many of these pages have the, like, the question mark and the string afterwards.

**Jakub Rudnik:** And that's not necessarily a problem, but if they're all indexing and crawlable, you're just doing Google, like a lot of work to do on your site as it crawls.

**Jakub Rudnik:** And then sending a bunch of like false flags on what you want, indexed, crawled, et cetera.

**Jakub Rudnik:** So large, you'll see as you read in the details, I had to use, like, I had to really slow down the crawl and I got to 37 and 39%.

**Jakub Rudnik:** I was, like, re-uploading this as I was, like, doing that analysis.

**Jakub Rudnik:** So you'll see a couple different marks here.

**Jakub Rudnik:** So it's not full, but seeing a fairly big chunk of this, and it looks even bigger as I'm getting to some of the deeper parts of the site.

**Jakub Rudnik:** So canonicals there, mobile speed, this one to me, it's big, it'd be worse for a site that was less B2B than you are.

**Jakub Rudnik:** It's like only 22.5% of your traffic, but the site's really good on desktop.

**Jakub Rudnik:** There's like one issue that I would also fix on desktop or like focus on, but really like the mobile side is very slow and causing a lot of issues and will hurt your mobile rankings for mobile performance.

**Jakub Rudnik:** Like we're looking at, let's see, I guess 10 seconds on like first, yeah, 11, 12 seconds on first paint for mobile pages and seeing that across, you know, only checking a handful, but I was looking at blogs, looking at groups, like different areas of the site and seeing virtually the same score.

**Jakub Rudnik:** So telling me it's.

**Jakub Rudnik:** It's more of a site-level thing than, like, your blog's having an issue, but nothing over here.

**Jakub Rudnik:** So I want to confirm that this is universal, but seeing it, like, really, really big differences on desktop and mobile.

**Jakub Rudnik:** And because, like, if you were an e-commerce site all focused on mobile, like, this would be my number one thing.

**Jakub Rudnik:** It's going to take some dev work to fix a lot of these, but big core web vital pieces here that I want fixed.

**Jakub Rudnik:** And then SiteFooter, basically, you don't use your SiteFooter for very much, and especially with the scope of the site, I would want, like, this will have some high-level thoughts here, but you would really want a project on, like, how to redesign, make sure our most impactful pages in the site architecture are really shown to Google through the SiteFooter, or potentially even various SiteFooters, depending on the experience of the site.

**Jakub Rudnik:** And so not all that is included.

**Jakub Rudnik:** This is, like, the high-level.

**Jakub Rudnik:** You're missing these opportunities.

**Jakub Rudnik:** Then we would want to scope that.

**Jakub Rudnik:** And...

**Jakub Rudnik:** And do that design after, but really for this, like a site of your magnitude to just have a couple URLs, you're missing a lot of opportunities.

**Jakub Rudnik:** And I think like, you'll see like all these SiteFooter, Canonical, and the 404s, you just have like this massive, in Google's eyes, massive site, right?

**Jakub Rudnik:** 10,000 pages, but it can be like scoped down potentially and like focused and shown, even you can still have a big site, but show Google where to crawl and where to spend that budget.

**Jakub Rudnik:** That's where I think a lot of like technical issues are, and I think we'll even unravel more details underneath of that type of bucket.

**Jakub Rudnik:** That's one, and then the speed is another, and then 500, that's just that read around migration issue.

**Jakub Rudnik:** Some minor issues, like there's some no-index stuff that we want to work on.

**Jakub Rudnik:** I wouldn't even focus here, and I think I want to dive in as I get a deeper analysis.

**Jakub Rudnik:** This is kind of connected to the Canonicals.

**Jakub Rudnik:** There are a couple of redirect chains.

**Jakub Rudnik:** I want to see how extensive those

**Jakub Rudnik:** Those were, but it didn't look terrible, but sometimes I find this, especially with migration, so I'll need a full crawl to do this one.

**Jakub Rudnik:** The international variations and how we think about that, that's like, there's just a lot of versions of the site I can't see enough to give you a full piece, but I want to dig in deeper on like, is how necessary, do all page types need to be varied?

**Jakub Rudnik:** Because again, this is giving like this big bloat of a site that may not need it.

**Jakub Rudnik:** But we've done a blog audit, I just haven't dug in myself to confirm some of those findings.

**Jakub Rudnik:** feel fairly good at the high level, but want to double click into this.

**Jakub Rudnik:** So yeah, I've talked a lot, I'm sorry, probably going fast, I just wanted to be aware of time and make sure I got through some, but those are the initial like big findings, want to get your web agency, whoever else on some of those immediately and start to prioritize.

**Jakub Rudnik:** But there will be more and more granular pieces as we can get some of reports in.

**Alishia Natiello:** No, that's extremely helpful and something that we unfortunately have been like, I.

**Alishia Natiello:** appreciate all the detail because in our kind of like basic overviews, like we are aware, but we're actually going to partner with a new agency because of some of these reasons.

**Alishia Natiello:** Like we're meeting with them now and we'll probably contract with them by the end of the year, if not beginning of the year.

**Alishia Natiello:** So, yeah, it's just helpful to see that we're not the only ones who have noticed like, hey, what's going on here?

**Alishia Natiello:** doesn't seem like we're getting the best of what we thought we were.

**Alishia Natiello:** So, yeah, but thanks for the details.

**Alishia Natiello:** I'll make sure that Vitaly, our CMO, sees this and I'll talk through them with him.

**Jakub Rudnik:** Okay.

**Jakub Rudnik:** Let me know questions or other places to double click into.

**Jakub Rudnik:** There's so many places I can dive in, like giving these high level big issues I think is important, but there's so many, like we can't give you the checklist of like all those pieces once the Screaming Frog and some other audits are complete.

**Jakub Rudnik:** But those would be like.

**Jakub Rudnik:** Things I'd Fixed Right Now, they're holding you back.

**Jakub Rudnik:** There's still, like, plenty of organic success despite that, which gives you, like, a lot of enthusiasm that this can work.

**Jakub Rudnik:** But including this, you'll see really step changes for sure.

**Alishia Natiello:** Gotcha.

**Alishia Natiello:** And that's in this week's meeting notes on Notion?

**Jakub Rudnik:** Yes, it should be linked in the Notion.

**Jakub Rudnik:** then I put it into your documents section.

**Jakub Rudnik:** There's, like, an audits folder, like, drop down with a few different audits.

**Jakub Rudnik:** And so I've got that linked there so you can find it this week.

**Jakub Rudnik:** But then go to the documents.

**Jakub Rudnik:** It's, like, evergreen area.

**Alishia Natiello:** Awesome.

**Jakub Rudnik:** Thanks so much.

**Jakub Rudnik:** You're welcome.

**Matthew Alves-Hill:** Sorry.

**Matthew Alves-Hill:** lost the mute button there.

**Alishia Natiello:** Cool.

**Matthew Alves-Hill:** Yeah.

**Matthew Alves-Hill:** Good old Zoom.

**Matthew Alves-Hill:** Right.

**Matthew Alves-Hill:** So I'm going to give you guys some more information overload.

**Matthew Alves-Hill:** But it's good stuff.

**Matthew Alves-Hill:** Okay.

**Matthew Alves-Hill:** So quick.

**Matthew Alves-Hill:** So we're up to 22 publish, which was a good push from last thing.

**Matthew Alves-Hill:** Like we said, we've got seven more out.

**Matthew Alves-Hill:** This is encouraging.

**Matthew Alves-Hill:** Like we can see, this is just a screen grab from your looker, but you can see this is split by the clusters.

**Matthew Alves-Hill:** You can see good growth.

**Matthew Alves-Hill:** It's a good sign that content is seeing traffic early on.

**Matthew Alves-Hill:** So there's 12 blogs of traffic already.

**Matthew Alves-Hill:** That's great.

**Matthew Alves-Hill:** We do have now 73 assignments like in our ready to start.

**Matthew Alves-Hill:** So it means like we found them, you guys have looked at them, left your comments.

**Matthew Alves-Hill:** We've assigned where you've said high priority.

**Matthew Alves-Hill:** We put them into the ready to start bucket and we'll start folding the forensic stuff in.

**Matthew Alves-Hill:** With low priority, they're still under like considering and we'll come back to them as we go.

**Matthew Alves-Hill:** So this will like add on from the keyword research that we're doing around those, those clusters.

**Matthew Alves-Hill:** So the idea is like you.

**Matthew Alves-Hill:** Bryce have identified some that perhaps are a lower priority.

**Matthew Alves-Hill:** Our keyword research will come in on top.

**Matthew Alves-Hill:** We should be able to find some potentially better keywords to target off the bat, and then we'll kind of fold those in as we go.

**Matthew Alves-Hill:** So Lawrence, who's the managing editor on this account, he's doing the keyword research now based off all the help that Jen supplied.

**Matthew Alves-Hill:** So towards the end of the week, we'll have like an idea.

**Matthew Alves-Hill:** We'll have folded those into Airtable, and then we can start generating assignment titles as well from those.

**Matthew Alves-Hill:** And essentially, we'll give you guys a bit more work to have a look through some of the new assignments around the forensic clusters that we'll want you guys to take a look at.

**Matthew Alves-Hill:** Does that make sense?

**Matthew Alves-Hill:** Yep.

**Matthew Alves-Hill:** Cool.

**Matthew Alves-Hill:** Then, yes, so the refresh opportunities, like you guys have seen the refresh content audit.

**Matthew Alves-Hill:** The TLDR from that was like, we found 30, 31 straight off the bat that we were like, yep, we should go.

**Matthew Alves-Hill:** Go and refresh these straight away.

**Matthew Alves-Hill:** So the plan is to, I have now added those to the Airtable.

**Matthew Alves-Hill:** You can see them as a refresh view that just lists all of them.

**Matthew Alves-Hill:** You guys have seen it before.

**Matthew Alves-Hill:** It's also in Notion, but now it's an Airtable.

**Matthew Alves-Hill:** It's all clean.

**Matthew Alves-Hill:** And the idea is then from next week, I want to start folding those refreshes in.

**Matthew Alves-Hill:** We've got 30 to do.

**Matthew Alves-Hill:** So I'll start adding those in once a week.

**Matthew Alves-Hill:** Most of them are BES topics.

**Matthew Alves-Hill:** So we'll do like a, we'll do a two BES, two forensics, and then a refresh, and it will probably be BES as well.

**Matthew Alves-Hill:** Does that make sense?

**Matthew Alves-Hill:** Yeah.

**Matthew Alves-Hill:** Okay.

**Matthew Alves-Hill:** Yeah.

**Matthew Alves-Hill:** And then as we get through the refreshes, we can start to look at some of the medium priority and some of the ones that were lower down.

**Matthew Alves-Hill:** But I really want to tackle those high priority refreshes.

**Matthew Alves-Hill:** They're like, we've identified them as, you know, strong performing pages already, and we can go in and do, give it like a.

**Matthew Alves-Hill:** Good, like, you know, lick of paint there and, and try and capitalize on, on their performance already.

**Alishia Natiello:** Sounds good.

**Matthew Alves-Hill:** Cool.

**Matthew Alves-Hill:** The one alert I want to raise you guys is that seven articles waiting for review at the moment in the Airtable.

**Matthew Alves-Hill:** I am going to set up some automations in Airtable that basically notify you so that you like you, so it's clear in the external channel.

**Matthew Alves-Hill:** Hey, there's an article waiting for your review.

**Matthew Alves-Hill:** Like, it's here now.

**Matthew Alves-Hill:** It'll be, hopefully, little bit easier to track because I know with, like, the commenting in Airtable, it's not the easiest method.

**Matthew Alves-Hill:** So automation should help.

**Matthew Alves-Hill:** They'll tag you and say, hey, these are waiting for your review.

**Matthew Alves-Hill:** And it will also help us keep track of that we're delivering.

**Matthew Alves-Hill:** But I think the main point around these, I'm not, so one question first.

**Matthew Alves-Hill:** On the review process, how does that go?

**Matthew Alves-Hill:** Is it, are both of you guys?

**Alishia Natiello:** looking at that, or is it, is it, is it, is yeah, so, yeah, it'll be different, depending, as we're getting the forensics up and running, like, Jen will have a heavier review since that's new, I'm handling the review for the BES ones myself, got it, okay, and yeah, a question about the seven, or just, yeah, like, talking about the publishing, kind of schedule as well, so, I think, yeah, sometimes it's confusing for me, uh, once, like, I just commented a bunch last week, think Friday, Thursday, Friday, like, this is completed, this moves to Lawrence and team, so I saw on Monday, they published one, two, three, four, and so, um, that would have been, since we didn't publish any last week, like, you know, from last week's count, um,

**Alishia Natiello:** And then I think we want to keep the cadence to the five per week, like, by Friday.

**Alishia Natiello:** So I think I, yeah, I think I completed reviews for an additional seven on my, we have like a tracker on our side.

**Alishia Natiello:** So I just wanted to confirm, like, will all those be ready to publish this Friday, or at least like six, I guess, to kind of have the pen over the phone.

**Matthew Alves-Hill:** Yeah, yeah.

**Matthew Alves-Hill:** So to, so there's basically we sent four on Friday.

**Matthew Alves-Hill:** We sent a further three, I believe, on Monday morning.

**Matthew Alves-Hill:** So those have been, so we published, those are the seven.

**Matthew Alves-Hill:** And then the seven sitting and waiting for review.

**Matthew Alves-Hill:** Now I'll double check with Lawrence, but as I see in the air table, we haven't had a, we haven't had a comment from you guys saying like, good to go.

**Matthew Alves-Hill:** I may be missing something here as I take over.

**Alishia Natiello:** Is it?

**Matthew Alves-Hill:** Is

**Matthew Alves-Hill:** Are you guys commenting in the Airtable to say it's good to go, or are you commenting in the Google Doc?

**Alishia Natiello:** In the Airtable.

**Matthew Alves-Hill:** Okay.

**Alishia Natiello:** Okay.

**Alishia Natiello:** So, I have, I can, like, put the titles that I know I reviewed Friday that I haven't seen published yet in the chat.

**Alishia Natiello:** If that's helpful, if we could get those published this Friday.

**Alishia Natiello:** I don't know if there was any, like, outstanding questions, maybe.

**Matthew Alves-Hill:** Let me just, let me just.

**Alishia Natiello:** Oh, I did it again.

**Alishia Natiello:** I put it in the growthx.

**Alishia Natiello:** I always, like, go and do it to the wrong one.

**Matthew Alves-Hill:** Okay.

**Matthew Alves-Hill:** So, we've got, so, in Ready for Review, I see, uh, Completed Review and Edits.

**Matthew Alves-Hill:** Okay.

**Matthew Alves-Hill:** But this one should be gone.

**Matthew Alves-Hill:** This one.

**Matthew Alves-Hill:** It should be published.

**Matthew Alves-Hill:** And then you'll have six more waiting that I don't see.

**Matthew Alves-Hill:** Yeah.

**Matthew Alves-Hill:** Okay, cool.

**Matthew Alves-Hill:** So this one should be out.

**Matthew Alves-Hill:** We'll just get this, like, we'll get this one published straight away.

**Matthew Alves-Hill:** And then that means that there are six left for your review, basically.

**Alishia Natiello:** And we want to try and publish those by Friday.

**Matthew Alves-Hill:** Yeah.

**Alishia Natiello:** I guess my question is I just put in a chat where I don't know where these are now in the edit view status, but all these I commented, like, completed review for.

**Alishia Natiello:** Which, yeah, so then I'm like, are they in a different status?

**Matthew Alves-Hill:** I see.

**Matthew Alves-Hill:** Okay, let me just check.

**Matthew Alves-Hill:** Okay, cool.

**Matthew Alves-Hill:** So they are, I'll double check this offline, but I believe these have all been sent for publishing.

**Matthew Alves-Hill:** They were sent on Friday.

**Matthew Alves-Hill:** I'll also, what I'll do is I've changed some things around in Airtable.

**Matthew Alves-Hill:** So basically, like, when you click on a view now, you can see exactly what's, it makes it easier, I think, for everyone to track these things without having to, like, do your own filters.

**Matthew Alves-Hill:** Let me just show you what I'm talking about here.

**Matthew Alves-Hill:** Yeah, so this will look a little bit different from last time, forensics, I'm going to move out.

**Matthew Alves-Hill:** But basically, like, now you can go in here and you can just, don't need to filter anything.

**Matthew Alves-Hill:** You can just see, like, okay, ready for review.

**Matthew Alves-Hill:** Like, in the end of class.

**Matthew Alves-Hill:** These are the page, these are the views that you need to worry about, I suppose.

**Matthew Alves-Hill:** What do you need to review and what have we published, right?

**Matthew Alves-Hill:** It's all here.

**Matthew Alves-Hill:** And then on the editor side, it's like, okay, prove to start.

**Matthew Alves-Hill:** These are the ones that you guys have signed off.

**Matthew Alves-Hill:** We're ready to go on.

**Matthew Alves-Hill:** These are the ones this week that are in production.

**Matthew Alves-Hill:** Let me get rid of the grouping.

**Matthew Alves-Hill:** And then it'll be like ready to publish and then publish.

**Matthew Alves-Hill:** So leave that with me.

**Matthew Alves-Hill:** Let me record a loom just so you guys are clear on everything that's going on.

**Matthew Alves-Hill:** I don't want you guys to be uncertain about what's happening.

**Matthew Alves-Hill:** I see we're going over.

**Matthew Alves-Hill:** So just a couple more things.

**Matthew Alves-Hill:** So the keyword research Lawrence is working on, we'll share a little bit of that towards the end of the week.

**Matthew Alves-Hill:** The idea is to build out clusters, more assignments, and then next week we'll share some more assignments with you and we can start adding to the roadmap.

**Matthew Alves-Hill:** But we have a good roadmap right now.-bye.

**Matthew Alves-Hill:** Bye Thank

**Matthew Alves-Hill:** We have stuff to work from.

**Matthew Alves-Hill:** So that's great.

**Matthew Alves-Hill:** The forensic personas document—the stuff you guys shared—we've folded that into the existing audience personas document.

**Matthew Alves-Hill:** I want to keep the workflow inputs as concise and tight as possible. When they start to creep, editorial quality drops because there's too much conflicting information.

**Matthew Alves-Hill:** Starting next week, when we add forensic articles, we can calibrate on the forensics pieces and make sure we're hitting the mark. We'll see if folding them in properly nails the intent in the persona, or if we need to build out the forensic personas more specifically to get even closer.

**Matthew Alves-Hill:** My gut tells me this approach will work, but we'll have a little calibration on the forensics since we haven't done that yet.

**Matthew Alves-Hill:** So basically, we have our marching orders. We know what we're working on this week. Next week, we'll start folding in the refreshes, and I'll shoot over a loom explaining what's going on in the Airtable, because it's a lot.

**Matthew Alves-Hill:** Yeah, that's helpful.

**Alishia Natiello:** But I will make sure, too, on my end to look through those reviews or review those items that you said are in ready to review.

**Alishia Natiello:** And I'll be able to do that before the day, my day today.

**Matthew Alves-Hill:** Yeah, ideally on Friday, you get the articles we've worked on. By the next sync, if you have time, we get your green light, and then we send for publishing so they're published within the week. That's the ideal cadence for me.

**Matthew Alves-Hill:** So we're on the same page there for sure.

**Alishia Natiello:** Um, great.

**Matthew Alves-Hill:** One last thing—I know it's Thanksgiving next week. Are we good on next week's Wednesday sync? Are you both working Wednesday?

**Alishia Natiello:** I'll be working.

**Jennifer Bulmash:** I'm off that day, but I'll be eyeballing things. I'll check in with you ahead of time and give you details, or I can join for a few minutes.

**Matthew Alves-Hill:** Cool. I'll make sure to drop an async update for you, Jen, just so you're linked in. But yeah, we know what we're doing, and everything's looking good.

**Alishia Natiello:** Great. It's been really helpful.

**Jakub Rudnik:** And if you're able to get my IP added, just let me know when that goes so I can restart and give you additional information.

**Alishia Natiello:** Will do. Thanks.

**Matthew Alves-Hill:** Okay, see you guys.

**Jennifer Bulmash:** Sounds good.

**Alishia Natiello:** Bye, y'all.
