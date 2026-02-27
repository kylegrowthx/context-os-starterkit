# Relay <> GrowthX - Bi-Weekly Sync

<metadata>
date: 2026-02-26
time: 16:00 UTC
duration: 28 minutes
organizer: bailey@growthx.ai
participants: Bailey Seybolt, Gavin Graham, Bethany Cantor, Dave White, Nick White
fathom_recording_id: 125647422
fathom_url: https://fathom.video/calls/580961064
share_url: https://fathom.video/share/BYWbEQ2dBU_ztXAE3sXU5siWbyg-p8yj
source: fathom
enriched_on: 2026-02-27 17:04 UTC
speaker_note: "06 - Oatmeal" in the original Fathom transcript is Gavin Graham (confirmed at 00:12:03 when Bethany addresses him by name). Dave White was likely on the same device/room and may account for some responses attributed to this speaker.
</metadata>

---

## Summary

GrowthX and Relay aligned on a major content strategy pivot — shifting from broad top-of-funnel content to deep-dive verticals, starting with General Contracting and HVAC. Bailey followed up on action items from Marcel's call with the Relay team the day before, including getting GA4 access for a GrowthX SEO expert, auditing CheckThat prompts for home services, and building a new Looker view for week-over-week page performance. Bethany flagged that approvals are still hard to attribute to specific pages, so the team agreed to focus on early-signal metrics before expecting conversion data.

---

## Context

Relay (relayfi.com) is an active GrowthX client. The day before this sync, Marcel met with Bethany and the Relay team to discuss strategic direction and surface concerns. Bailey, who manages the day-to-day engagement, caught up on the recording and used this bi-weekly sync to follow up on the resulting action items. The central challenge: Relay's organic traffic is flat despite rising AI visibility, because ~85% of their content is top-of-funnel and now appears in Google's zero-click AI Overviews. Gavin Graham presented a new strategy doc proposing a pivot to deep-dive verticals. This meeting was about aligning GrowthX's execution with that pivot.

---

## Relevance

**To GrowthX Delivery:**
- Live example of pivoting a client from broad ToFu content to vertical-specific deep dives
- Content pipeline restructuring: separate persona docs and pipelines per vertical, 1-2 calibration articles before scaling
- Internal linking artifact being developed with LLM-driven priority grouping
- Suleman (GrowthX SEO expert) may need individual GA4 access since shared team account was denied

**To CheckThat:**
- Relay explicitly discussed replacing Scrunch with CheckThat for AI visibility reporting
- Bailey to audit CheckThat prompts for home services vertical and share with Relay team
- Bethany asked for monthly AI visibility summaries — CheckThat is the delivery mechanism
- Prompt tagging by vertical cohort requested for more granular reporting

**To GrowthX Business Development:**
- Client retention signal: Relay investing in new strategy despite flat traffic — relationship is healthy
- Marcel's direct engagement with Relay leadership reinforces account depth
- Attribution gap (can't track content to approvals) is a recurring client pain point — worth tracking as a pattern across accounts
- Bethany wants cross-account insights from GrowthX — opportunity to formalize benchmarking

---

## Overview

- Pivot from broad top-of-funnel content to deep-dive vertical strategy, starting with General Contracting and HVAC
- ~85% of current content is ToFu, now appearing in Google's zero-click AI Overviews, causing flat organic traffic despite rising AI visibility
- Approvals are hard to attribute to specific pages — multi-touch attribution still in progress at Relay
- GrowthX needs GA4 access for SEO expert to build custom conversion-path reports
- CheckThat replacing Scrunch for AI visibility reporting — Bailey to audit prompts for home services
- New Looker view planned for week-over-week page movers and shakers
- Vertical sequencing may shift after 2-3 months (e.g., e-commerce), with each vertical treated as a performance cohort
- GrowthX building a new internal linking artifact that groups priority links by theme for LLM-driven optimization

---

## Key Topics

### Problem: Flat Traffic & Unclear ROI

- ~85% of content is top-of-funnel (ToFu), which now appears in Google's zero-click AI Overviews, causing flat organic traffic despite rising AI visibility
- Approvals are hard to track to specific pages, obscuring content ROI
- Goal: find early signals of success (e.g., traffic growth, citations) to prove the new strategy is working before approvals can be attributed

### Solution: Deep-Dive Vertical Strategy

- Pivot from broad ToFu content to deep dives within specific verticals
- Initial focus: General Contracting and HVAC
- The plan may shift to a different vertical (e.g., e-commerce) after 2-3 months
- Each vertical will be treated as a cohort to track performance over time

### Execution & Reporting Plan

- **Content Pipeline:**
    - GrowthX will create persona docs and separate content pipelines for each vertical
    - 1-2 calibration articles per vertical will ensure quality before scaling
- **Reporting Tools:**
    - **GA4:** GrowthX needs access for a technical expert to build custom reports tracking organic touchpoints before conversion
    - **CheckThat:** Replacing Scrunch for AI visibility reporting. GrowthX will audit prompts for home services and add vertical-specific tags.
    - **Looker:** A new view will be built to highlight top "movers and shakers" (pages with significant week-over-week growth)
- **Internal Linking:**
    - GrowthX is building a new artifact to improve LLM-driven internal linking
    - Dependency: a list of top-performing pages by approvals is needed to inform this artifact

---

## Action Items

**Gavin Graham (Relay)**
- Send availability next week to Bailey for meeting with Jen and Panzer (editorial quality concerns)
- Confirm first 2 verticals to Bailey (expected by end of day or next morning)

**Dave White (Relay)**
- Pull list of top-performing pages by approvals and share with Bailey (working with Joseph on this)

**Bailey Seybolt (GrowthX)**
- Email Bethany/Dave for GA4 access for GrowthX SEO expert; set up custom GA4 views
- Audit CheckThat prompts for home services; share spreadsheet with Dave/Bethany
- Build Looker page for week-over-week page movers
- Discuss with editorial: separate pipelines per vertical; plan 1-2 calibration articles
- Read strategy doc; post questions in Slack to Dave/Bethany
- Once verticals confirmed, build out Airtable plan and persona docs

**Bethany Cantor (Relay)**
- Define and share early-signal metrics with Bailey

---

## Transcript
**Bailey Seybolt:** Here we go.

**Bailey Seybolt:** Yeah, so I did, maybe before we jump into the strategy updates, based on kind of the call, I know there was a couple things that were discussed.

**Bailey Seybolt:** I just wanted to make sure I followed up on them.

**Bailey Seybolt:** One was I know, Dave, we had talked about you getting time with kind of the Jen and Panzer from the editorial team just to talk through some of the concerns around quality since they're the ones kind of building and operating the pipeline.

**Bailey Seybolt:** I think they'll have the best insight into ways to address that.

**Bailey Seybolt:** So if you want to just send me some times you're free next week, I'm happy to take a look at their calendars and make that happen.

**Gavin Graham:** Okay, cool.

**Gavin Graham:** Yeah, I'll do that.

**Bailey Seybolt:** And then the other thing on one of the things that came up that I know we've talked about before is the linking.

**Bailey Seybolt:** And one of the things I'm working with the editorial team on is a new artifact that would essentially kind of group the priority links by themes and kind of have a step that gives the LLM a little more detail on what to pull and when.

**Bailey Seybolt:** And I would love to, you know, I think we have visibility into what's performing in terms of traffic, in terms of clicks, but not visibility into the approvals pipeline.

**Bailey Seybolt:** So if something that you could share with me is just, I think if you have like a list of what are the top performing pages on the site by approvals, I think it would be great to make sure we're kind of capturing that in the priority list as well.

**Gavin Graham:** Yeah.

**Gavin Graham:** And I actually have to figure out how to even pull that list.

**Gavin Graham:** Yeah, I was talking to Joseph about that yesterday.

**Gavin Graham:** I was going to try to pull something for you to identify that.

**Gavin Graham:** So that's in the works.

**Gavin Graham:** So we'll get that to you as soon as we can.

**Bailey Seybolt:** Yeah, and I won't let that block us from making the incremental improvements.

**Bailey Seybolt:** I think it would just be great to, I know that's the North Star we're building towards, so to kind of capture that in as many places as possible.

**Bailey Seybolt:** And then the other thing that I, and maybe this is a question for Bethany, that they talked about with Nick and Bethany on the call was just getting...

**Bailey Seybolt:** Oh, she's on.

**Bailey Seybolt:** Oh, just in time.

**Bethany Cantor:** Sorry, I have back-to-back meetings for the next four and a half hours, so I'm just bumping around.

**Bailey Seybolt:** Thursday's that day for me, too.

**Bailey Seybolt:** My calendar just like looks blue when you look at it.

**Bailey Seybolt:** We were just kind of, before we jumped into the strategy updates, I was just following up on some of the to-do's that came out of the meeting with Marcel yesterday, because I was able to catch up on the recording.

**Bethany Cantor:** Which was also rushed.

**Bethany Cantor:** Yeah, so feel free to ask questions.

**Bethany Cantor:** I feel like we didn't get done completely before we both had to jump.

**Bailey Seybolt:** I feel like we captured a lot.

**Bailey Seybolt:** And I think what he's looking for on those is a sense of outside of the day-to-day of how things are going and where we can improve as a new company and making sure that we're kind of addressing all your concerns and the things you care about the most.

**Bailey Seybolt:** So I think a lot of great stuff came out of that for me as someone who's just watching the recording.

**Bailey Seybolt:** So one of the things I was touching base with, I know you had talked about with him about just getting us access to GA4 and I don't know if you used PostHog or FullStory and letting us kind of just poke around to see how your conversion, your approvals pipeline is like currently set up, making sure that if there are ways we can plug it directly even into Looker.

**Bailey Seybolt:** I know we've done that or set up kind of custom reports in GA4 to give us that visibility.

**Bailey Seybolt:** So I just wanted to make sure I followed up on the best next steps to kind of get that access.

**Bethany Cantor:** So...

**Bethany Cantor:** Oh, go ahead.

**Gavin Graham:** No, I was just going to say, I thought you guys already had access to our GA4, and that's what's plugging into the Looker.

**Bailey Seybolt:** We do to GA4, but I think we don't to any other tools.

**Gavin Graham:** I see, I see.

**Gavin Graham:** Yeah, so you should have access to Search Console now, at the minimum, yeah.

**Bailey Seybolt:** Yes, yeah, so I have GSC.

**Bailey Seybolt:** I'll check and see.

**Bailey Seybolt:** I know, I think Suleman, who set up the Looker, has access to GA4.

**Bailey Seybolt:** I think there was a concern about giving the shared Teams account access, so we may need you to give another individual access. I would like our technical SEO expert to be in there helping set that up, so I'll find out if he's the right person and give you a more specific email.

**Gavin Graham:** Okay, and based on how quickly they gave you access to Search Console, I think that shouldn't be an issue.

**Bailey Seybolt:** Should be able to get that set up pretty quickly.

**Bailey Seybolt:** Yep, that was great.

**Gavin Graham:** That's kind of a blanket approval on other things.

**Bailey Seybolt:** Yeah, so then I think it would just be knowing if there's other tools or places you're collecting data that would help us kind of round out that story or if it's really just GA4.

**Bethany Cantor:** So here's the difficulty — I'm looking at your top performing content stuff.

**Bethany Cantor:** Approvals right now for us are hard to track to pages.

**Bethany Cantor:** We're still working on our multi-touch attribution.

**Bethany Cantor:** So that's probably — I think GA4 and Console are probably the best places to live for now.

**Bethany Cantor:** I'm trying to think of other tools that we use on a regular basis, like Ahrefs and SEMrush.

**Bethany Cantor:** We obviously have access, which we could bring you the reporting on a week-by-week basis.

**Bailey Seybolt:** Like that's enough to go on, but I think that would be helpful.

**Bethany Cantor:** Okay, cool.

**Bailey Seybolt:** Cause yeah, we've definitely set up custom views for customers before in GA4, even just looking at those trigger events, like how many organic touch points they had before, what were those touch points, and being able to kind of find some signals that way too.

**Bailey Seybolt:** So I'm thinking like at the very least, that would be a good place to start connecting those dots.

**Bethany Cantor:** Okay.

**Bailey Seybolt:** Okay, in terms of reporting, I know you all need it this week.

**Gavin Graham:** So that should come at the end of the day, by the end of the day today, or like first thing tomorrow morning.

**Bailey Seybolt:** And then I also am going to, given the shift in strategy, I would like to also take a look and just audit the prompts that we're checking and tracking on CheckThat and make sure we're capturing the full picture on home services.

**Bailey Seybolt:** So I'm going to go through and do a first pass on that and then I'm going to just pull them into a spreadsheet to share with your team to take a look at as well.

**Bailey Seybolt:** So we can make sure that those look good and we're kind of tracking the full story around home services especially so we can start collecting data there as well.

**Bailey Seybolt:** And then the last thing I wanted to ask about before we jump into the strategy is just I'm working on building out some of the additional views in Looker to give you kind of a more granular look into performance.

**Bailey Seybolt:** And I know we had talked about just getting a better article-by-article view of what the top performing posts are.

**Bailey Seybolt:** And this is kind of a good question for either Dave or Bethany in terms of — are there specific metrics you're most interested in?

**Bethany Cantor:** Maybe like week over week, if there are big movers and shakers in terms of pages that are getting cited or growing, that's probably the most interesting for now, because usually I'm just looking for the cause week over week of the peaks and valleys.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** Well, that's definitely something I think we could build as a page in Looker just so it's easier for you to see it with that filter.

**Bethany Cantor:** And then, yeah, think about it and let me know if there's anything else.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** So, I would love to — like I said, I didn't have time to dive deep into the strategy doc you shared this morning because I was in a meeting, but I would love to have you just kind of walk me through it.

**Bailey Seybolt:** I think I got the general gist of where we're going and it totally makes sense and it's definitely something I think we can successfully execute on.

**Bailey Seybolt:** And I think we've done a lot of the initial validation and keyword research when we dug into that home services strategy.

**Bailey Seybolt:** So I also think it's something that we can pivot towards pretty quickly, which is great.

**Bailey Seybolt:** But I would love for you to just walk me through it, if that works.

**Gavin Graham:** Yeah, let me find the doc then.

**Gavin Graham:** Unless you have it open.

**Bethany Cantor:** Well, Gavin, do you want to start with the background?

**Gavin Graham:** There's a bunch of background and context in there that I think is just generally known.

**Gavin Graham:** It's kind of teeing up why we're choosing the trades, but it's digging into the content that we have, particularly with AEO — about 85% of what's surfacing is very informational, very top of funnel content.

**Gavin Graham:** So I don't know if that's necessarily — I mean, it's probably just the mix that we have on the site right now, there's an over-concentration of top of funnel content.

**Gavin Graham:** We don't want to dismiss the importance of that content for the sake of brand building, but it's low conversion, and what's happening is it's appearing in Google's AI Overviews.

**Gavin Graham:** Our visibility in Google's AI Overviews has spiked over the past couple of months, which is great, except they're zero-click results.

**Gavin Graham:** So our organic traffic is flat and declining a little bit.

**Gavin Graham:** So the content plan is kind of what we talked about before, just going deeper into specific topics.

**Gavin Graham:** So a high level of specificity, and then moving from one topic to another, but going deep rather than broad.

**Gavin Graham:** And the strategy in here is really just kind of the specifics of that — what we want to target first and second and in what order.

**Gavin Graham:** So that's really the only change, I think, in what we've talked about previously — the order of operations and how we want to tackle things.

**Gavin Graham:** We're digging into vertical sequencing a little bit more right now, so we may insert other topics in between so that it's not just the trades over the next five to six months. So maybe do General Contracting and HVAC and pivot to — I'm totally making this up — but like pivot to real estate for example and then back to a different trade, just to add a little bit of variety. But we should know probably later today, if not a more fully fleshed out list and order that we want to tackle things in.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** Yeah, that sounds great.

**Bailey Seybolt:** It seems really clear.

**Bailey Seybolt:** I think the next step on us is just to build this out in Airtable in a way that makes it clear what we're actioning on.

**Bailey Seybolt:** I know Dave is feeling like we want to have kind of a content prioritization plan, in addition to just a big list of topics.

**Bailey Seybolt:** So I think that's what I would take away as my action items in terms of executing on this.

**Bailey Seybolt:** And it sounds like if your list is changing, maybe we just focus on the General Contracting and HVAC keywords and topics for now, and build that out, if that makes the most sense.

**Gavin Graham:** Yeah, I'm pretty confident that those two will remain at the top.

**Gavin Graham:** So we'll know for sure, like I said, probably later today, but latest tomorrow.

**Bailey Seybolt:** Yeah.

**Gavin Graham:** So it might make sense to kind of hold off even just for the half day, and we can let you know for sure.

**Gavin Graham:** But I'm quite confident those will be the top two.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** Yeah, I mean, we can certainly hold off.

**Bailey Seybolt:** My only goal would be to get it built out enough this week that we can start executing on it next week.

**Bailey Seybolt:** But that can be as simple as aligning on what we want to work on next week.

**Gavin Graham:** Okay.

**Bailey Seybolt:** So if we don't have the next three months fully mapped out, that's fine.

**Bailey Seybolt:** So yeah, if you just want to ping me when you feel like it's ready and you're kind of aligned on that, we can pick it up from there.

**Gavin Graham:** Sounds good.

**Bethany Cantor:** Yeah.

**Bethany Cantor:** And we are taking, just to be clear, like the full volume.

**Bethany Cantor:** So it's going to be a pretty big shift.

**Bethany Cantor:** I also think there's a possibility that after the first two months we switch to a different vertical, potentially, depending on how leadership feels, like e-com or another vertical for us.

**Gavin Graham:** I think it's more likely than not, yeah.

**Bethany Cantor:** Which is fine.

**Bethany Cantor:** Because then I think we can just let those first two cook and kind of see what the results are.

**Bethany Cantor:** So definitely also maybe with our reporting as the rest of the year goes on, want to keep an eye on these as though they were cohorts. Like when we went deep on this, here's what happened, this is building traction, maybe this cohort not so much.

**Bethany Cantor:** So yeah, I think this is, for the foreseeable, this will be the new way of doing things.

**Bailey Seybolt:** Yeah, and I think the thing I also want to touch base on with our editorial team is just from an execution perspective, just to give you visibility into what will happen there — talking to them about whether we should be treating these as separate personas and building out separate pipelines for each of these.

**Bailey Seybolt:** At the very least, we'll definitely be creating specific persona documentation for each one.

**Bailey Seybolt:** And I'll also talk to them about building out a separate pipeline as well.

**Bailey Seybolt:** I think once we've defined what those first verticals are, it may make sense to run a couple articles as calibrations to make sure we're nailing each of those personas, so that we're able to pivot quickly and don't have a ramp-up time for each one.

**Bailey Seybolt:** So all to say, I think it totally makes sense to focus it in this way, but at the very beginning, we just want to make sure that we're able to calibrate for each of the personas with one or two articles.

**Bailey Seybolt:** So you don't see a dip in quality every time we shift because we're starting from scratch again.

**Gavin Graham:** Cool.

**Gavin Graham:** Yeah, that makes sense.

**Bailey Seybolt:** Sounds good.

**Bailey Seybolt:** Yeah, but otherwise, I think the timeline makes sense.

**Bailey Seybolt:** My only other question would be in terms of reporting.

**Bailey Seybolt:** The benchmarks that you sent totally make sense and feel realistic in terms of the timeline and when you're going to be looking for signals versus results.

**Bailey Seybolt:** So just knowing that we're looking for signal especially in these early months, if there are specific metrics that you care about and feel like success — when we're probably not going to be marching towards approvals in quite the same way we had talked about before — just letting us know what those metrics are so we can make sure we're reporting on the right things in these early stages.

**Bethany Cantor:** Yeah, that's fine.

**Bethany Cantor:** And we'll think on that.

**Bethany Cantor:** I did say to Marcel yesterday, I think we're also curious to learn from you all — like how your other companies are showing this growth.

**Bailey Seybolt:** Some of it depends on whether it's a net-new content program in the first six months versus an existing publication with domain authority.

**Bailey Seybolt:** So some of it is, you know, happy to pull in learnings as much as possible.

**Bailey Seybolt:** And I know that was something you talked about with Marcel — getting more of those cross-account insights.

**Bailey Seybolt:** And I think that's an area where we're letting it inform our strategy and operations, but probably not doing as good a job as we could sharing that with you all.

**Bailey Seybolt:** So that's definitely a learning to take from that call and something I'd love to take away and talk to the team about.

**Bailey Seybolt:** Even just reporting monthly on the insights we're seeing across accounts would be a great thing to share.

**Bailey Seybolt:** And one of the benefits of working with a company like GrowthX.

**Bethany Cantor:** Great.

**Bethany Cantor:** I mean, it's a new discipline.

**Bethany Cantor:** Everybody's trying to figure out how to talk about it, right?

**Bailey Seybolt:** So we can put our heads together a little bit more.

**Bethany Cantor:** And we'll try to get a little clearer on our end.

**Bethany Cantor:** I think the reason it's still feeling a little wishy-washy from our side is like, we are still figuring out how to connect all of this data to actual results.

**Bethany Cantor:** It's just a weird moment because we can see the flatness in the traffic, but the AI conversions are climbing and it's hard to know what's doing it.

**Gavin Graham:** Like, is it because we are generally showing up more, which I think we are because our word of mouth numbers are growing?

**Bethany Cantor:** Yeah.

**Bethany Cantor:** But like, where are we showing up?

**Bethany Cantor:** We're trying to pull some data from SEMrush about the platforms we're showing up on from an AI perspective.

**Bethany Cantor:** But I think the more you can tell us from your AI visibility data — I haven't had a chance to dive into it, but what are the articles that are getting pulled in?

**Bethany Cantor:** What can we go into our meetings and say in terms of — this is the content that's getting cited with a link.

**Bethany Cantor:** So we're doing more of that — just positive momentum around what's working and what we learned.

**Bethany Cantor:** But we're struggling to figure out what is working.

**Bethany Cantor:** And I think, I mean, I'm really glad Gavin had this insight about the zero-click stuff, because that does explain a lot of the flatness. Looking at GA4, you can see that it's coming from Google.

**Bethany Cantor:** So that also makes double sense.

**Bethany Cantor:** But yeah, it would just be good to know when stuff is getting cited, what is getting cited.

**Bethany Cantor:** And I know the missing link for everyone is — we don't know who's asking the questions. We don't know if it's our ICP that's in ChatGPT or Claude asking.

**Bethany Cantor:** We know what's happening, but we don't know how often.

**Bailey Seybolt:** Yeah, 100%.

**Bailey Seybolt:** And I think once you get into CheckThat, that is a great way to dig into some of that more granular visibility, because you can see what your top-cited content is.

**Bailey Seybolt:** But then you can also go into the prompts themselves and see not just an overview of your visibility, but also where you're appearing across the platforms — which is really helpful if you're seeing growth on one platform, or higher converting traffic coming from one platform.

**Bailey Seybolt:** And I think we can also — we already have your prompts grouped by buyer stage, but we can also add tags, especially as we're shifting towards home services, so you'll be able to see insights for prompts for these cohorts specifically. Which makes it easier to report on and find signal than some of the other tools we've used, like Scrunch, where you get some of that overall visibility but it's hard to dig in and identify trends.

**Bethany Cantor:** So, are you guys going to be doing, now that you have this, kind of a monthly summary from this tool as well?

**Bailey Seybolt:** Yeah, so the goal is to move off of Scrunch and move on to this entirely.

**Bailey Seybolt:** We were just giving it a little bit of time as we launched, and it's new, to work out the bugs and the kinks before we shifted entirely.

**Bailey Seybolt:** But yes, this will be what we'll be using for reporting on those trends on a monthly basis now.

**Bailey Seybolt:** And then the goal of getting you all onboarded so you have access is that, for your own reporting, you'll be able to go in and see at the level of granularity what's going on with prompts and be able to do your own filters as well.

**Bethany Cantor:** Cool.

**Bethany Cantor:** Okay.

**Bailey Seybolt:** Okay, great.

**Bailey Seybolt:** Well, I think a lot of action items on our end, but I don't have any other questions.

**Bailey Seybolt:** I'll read through that document more thoroughly today and then drop any questions I have in Slack, if that works.

**Gavin Graham:** Sounds good.

**Bailey Seybolt:** And then, yeah, just let me know when it's updated, and we can action on that and get it all set up in Airtable on our end.

**Gavin Graham:** Will do.

**Bethany Cantor:** Sounds good.

**Gavin Graham:** Cool.

**Bailey Seybolt:** All right.

**Bailey Seybolt:** Is there anything else?

**Gavin Graham:** All right.

**Bailey Seybolt:** Thanks, everyone.

**Bethany Cantor:** Bye.

**Gavin Graham:** Thanks.
