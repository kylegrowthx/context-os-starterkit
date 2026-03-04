# Strapi <> Growth X -  Weekly Sync

<metadata>
date: 2025-12-17
time: 16:52 UTC
duration: 23 minutes
organizer: Vivek Shankar
participants: Vivek Shankar, Paul Bratslavsky, Theodore Kelechukwu Onyejiaku, Victor Coisne, Golzar Yaghoubpour, Usman
fathom_recording_id: 109458049
fathom_url: https://fathom.video/calls/508416574
share_url: https://fathom.video/share/vvz8J9CFDHBtGzMAwbTjzDC9wza-XRNu
source: fathom
enriched_on: 2026-03-02 00:00 UTC
</metadata>

---

## Summary

GrowthX and Strapi synced on accelerated content production during the holiday season, resolving critical technical blockers around comparison page publishing. The team aligned on 2026 strategy to position Strapi as the ideal backend for frontend developers by showcasing integration with various UI libraries. With Vivek out Dec 22–Jan 5 and Jan 12–16, GrowthX front-loaded 14 articles this week to create a content buffer while remaining available for emergencies via Slack.

---

## Context

GrowthX is a B2B content marketing agency delivering high-impact SEO and content strategy work for Strapi, a popular open-source headless CMS. This weekly sync covers content production progress, technical issues blocking page deployment, and alignment on 2026 marketing strategy. The meeting included Vivek Shankar (GrowthX lead), Paul Bratslavsky and Theodore Kelechukwu Onyejiaku (Strapi product team), and Victor Coisne and Golzar Yaghoubpour (Strapi leadership). The timing is significant due to holiday schedules and a critical bug in Strapi's Notum CMS blocking comparison page updates.

---

## Relevance

**To GrowthX Delivery:**
- Holiday schedule requires front-loading 14 articles this week (vs. typical 7) to create a content buffer while Vivek is out Dec 22–Jan 5 and Jan 12–16
- Usman available next week through Dec 25 and full-time in January; team remains responsive to Slack emergencies during OOO
- 2026 priorities locked in: integration pages, page refreshes, new agency-owner persona, continued developer persona focus

**To GrowthX Business Development:**
- Strong account health signals: Strapi holding #1 ranking for nearly all tracked queries with 92% sentiment
- Traffic remains strong despite December seasonality; LLM traffic slightly sluggish but within normal seasonal patterns
- Proactive auditing approach (Scrunch page audits) demonstrates value-add beyond standard reporting

**To Strategic Alignment:**
- Strapi's 2026 positioning (frontend-first, UI library flexibility) directly influences GrowthX content roadmap — integration pages and framework showcases align perfectly
- Critical blocker: Comparison page publishing blocked by missing CM field data; Growth X tasked with generation, timeline pushes to early January due to team OOO
- Notum CMS issues (preview, video insertion, publish failures) remain lower priority for Strapi but cascade into GrowthX's workflow

---

## Overview

- **Production Accelerated:** Delivering 14 articles this week to create a holiday buffer for Vivek's OOO dates (Dec 22–Jan 5, Jan 12–16).
- **Critical CMS Bug:** A bug in the Notum CMS is preventing comparison pages from publishing. The fix requires Growth X to generate missing `CM` field data, which is blocked until early January.
- **2026 Strategy Aligned:** Content will focus on Strapi's frontend flexibility (e.g., UI libraries) to position it as the ideal backend for frontend developers.
- **Performance Strong:** Overall traffic is healthy, though LLM-related traffic is slightly sluggish—a common trend this December. SEO rankings remain dominant.

---

## Key Topics

### Technical Issues & Blockers

  - **Notum CMS Bug:** Comparison pages fail to publish or update, causing page breaks.
      - **Root Cause:** Missing data in the `CM` field, which populates the page's technology breakdown.
      - **Resolution:** Growth X will generate the missing data.
      - **Timeline:** Blocked until early January due to the relevant team member's OOO schedule.
  - **Comparison Page Table:** The task to remove the table from comparison pages is a lower priority for Notum and is pending.

### Content Production & Holiday Schedule

  - **Production:** 7 articles delivered last week; 14 articles due this week.
  - **Rationale:** To create a content buffer for the holiday season.
  - **Growth X OOO Schedule:**
      - **Vivek:** Dec 22–Jan 5 & Jan 12–16 (available for emergencies via Slack).
      - **Usman:** Available next week (until Dec 25) and in January.

### 2026 Content Strategy

  - **Goal:** Align content with Strapi's marketing initiatives.
  - **Paul's Focus (Strapify):** Showcase Strapi's flexibility with various UI libraries and frameworks.
      - **Rationale:** Position Strapi as the ideal backend for frontend developers, enabling them to build user-facing products without deep backend expertise.
      - **Alignment:** This focus is already reflected in the new list of integration pages.
  - **Growth X Priorities (Jan):**
      - Integration pages
      - Page refreshes
      - New persona: Agency owner
      - Continued focus: Developer persona

### Performance & SEO

  - **Traffic:** Strong session numbers, despite December being a typically slow month.
  - **LLM Traffic:** Slightly sluggish, but this is a common trend across many accounts this December.
      - **Action:** Running page audits in Scrunch to proactively check for issues, though none are expected.
  - **SEO:** No significant changes in Scrunch.
      - **Rankings:** Strapi holds \#1 position for nearly all tracked queries.
      - **Sentiment:** High at 92%.

---

## Action Items

**Vivek Shankar (GrowthX)**
- Queue approved integration pages for production
- Add to-do to generate CN (comparison) fields for all comparison pages — blocked until early January due to team member OOO
- Add agency-owner persona topics for review

**Paul Bratslavsky (Strapi)**
- Double-check comparison pages table removal status with Notum
- Follow up with Notum regarding preview, video insertion, and publishing issues

---

## Transcript

**Vivek Shankar:** Hey, Paul, how are you?

**Paul Bratslavsky:** Very good, very good.

**Vivek Shankar:** It's been a while, I feel like I haven't seen you in ages.

**Paul Bratslavsky:** Yeah, I've been missing just things come up or I'm either off or whatever.

**Paul Bratslavsky:** Yeah, so it seems like it's been forever.

**Vivek Shankar:** Yeah, no worries.

**Vivek Shankar:** Well, good to see you again.

**Paul Bratslavsky:** How have you been?

**Paul Bratslavsky:** Good, good.

**Paul Bratslavsky:** You know, it's in Vegas, it's getting chilly.

**Paul Bratslavsky:** I don't know how I feel about it.

**Paul Bratslavsky:** It's not that cold, competitively speaking, but it's still, I'm like, come on, man.

**Vivek Shankar:** Well, you're still about to complain.

**Paul Bratslavsky:** I mean, it's relatively chilly.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** It's all good.

**Vivek Shankar:** You see, it's a complaint.

**Paul Bratslavsky:** Yeah.

**Vivek Shankar:** Yeah, Lisbon has become pretty chilly as well.

**Paul Bratslavsky:** Yeah.

**Vivek Shankar:** We're having some storms and everything because we're right next to the Atlantic.

**Paul Bratslavsky:** Yeah.

**Paul Bratslavsky:** Yeah, Lisbon is amazing.

**Paul Bratslavsky:** Like, is there like a good time for people to come where it's like, like, like.

**Paul Bratslavsky:** It's going to sound counterintuitive when it's like the least touristy.

**Vivek Shankar:** Yeah, yeah.

**Vivek Shankar:** I don't know.

**Vivek Shankar:** Definitely.

**Vivek Shankar:** I mean, with overcrowding, I would say like late fall, you know, around November.

**Vivek Shankar:** I would say that is the best thing because it's so warm over here in November.

**Paul Bratslavsky:** Like it's not hot, but it's warm.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** And yeah, the tourists have left and everything's back to normal.

**Vivek Shankar:** So you can, you're not going to be met with like lines around the block for a good restaurant or something.

**Paul Bratslavsky:** Nice.

**Paul Bratslavsky:** Nice.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Hey, Theo, how are you?

**Theodore Kelechukwu Onyejiaku:** Yeah, I'm good.

**Paul Bratslavsky:** How are you doing?

**Vivek Shankar:** Doing good.

**Vivek Shankar:** Discussing the weather.

**Vivek Shankar:** So, yeah.

**Paul Bratslavsky:** Yeah.

**Paul Bratslavsky:** Yeah.

**Theodore Kelechukwu Onyejiaku:** You don't know if you live.

**Paul Bratslavsky:** I think it's in Lisbon.

**Paul Bratslavsky:** They have a bridge that looks like the Golden Gate Bridge.

**Vivek Shankar:** Yeah, it does.

**Paul Bratslavsky:** Yeah.

**Paul Bratslavsky:** And I think like they had like, they

**Paul Bratslavsky:** actually had like a pretty bad earthquake, right?

**Paul Bratslavsky:** Like a while ago in Lisbon, that demolished the majority of the city.

**Vivek Shankar:** Yeah, it was in the 1500s.

**Vivek Shankar:** And actually, a lot of people, historians say that that earthquake is what destroyed the Portuguese empire slash the imperialism or whatever.

**Vivek Shankar:** Yeah, it's that bad.

**Vivek Shankar:** So basically, they just never recovered.

**Paul Bratslavsky:** Yeah, it's insane.

**Paul Bratslavsky:** But yeah, but Lisbon is really awesome.

**Paul Bratslavsky:** It's funny because like, like I only been there once and it's just like, I instantly like fell in love.

**Paul Bratslavsky:** The food is amazing.

**Paul Bratslavsky:** It's just nice vibe, nice atmosphere.

**Vivek Shankar:** Yeah, it is.

**Vivek Shankar:** It is.

**Vivek Shankar:** It is very nice.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Well, I know Victor marked himself as a no on this.

**Paul Bratslavsky:** I think we can just get started.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Cool.

**Vivek Shankar:** So...

**Vivek Shankar:** Yeah, just some quick updates.

**Vivek Shankar:** We delivered seven articles last week, and we're delivering actually 14 this week.

**Vivek Shankar:** I'm very sorry, Theo.

**Vivek Shankar:** The main reason is that we are actually producing ahead of time to account for the holiday season, and I will be off the next two weeks and on Jan 12th to 16th.

**Vivek Shankar:** But I'll still be checking Slack for emergencies and questions, so there's no drop-off in coverage.

**Vivek Shankar:** Usman is going to be around in January when I'm off, as well as he is available next week until up to Christmas, basically.

**Vivek Shankar:** So we're still here.

**Vivek Shankar:** If there's any emergency, you can always tag one of us and we'll get back to you.

**Vivek Shankar:** But yeah, it's just that the content production is scheduled in bulk for this week.

**Vivek Shankar:** And for the new list of integration pages, Theo, I know you sent a message.

**Vivek Shankar:** I think you meant to send a link for the list of integration pages.

**Theodore Kelechukwu Onyejiaku:** didn't see it.

**Theodore Kelechukwu Onyejiaku:** Yeah.

**Theodore Kelechukwu Onyejiaku:** Yeah, you shared the list.

**Theodore Kelechukwu Onyejiaku:** So we've gone through them and we created a Google Sheet link, a Google Sheet so that you could see the ones we said yes to and the duplicates and the ones that are not going to approve now.

**Vivek Shankar:** Yeah, there was no link in your message.

**Theodore Kelechukwu Onyejiaku:** Oh, there was no link?

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Sorry about that.

**Vivek Shankar:** check.

**Vivek Shankar:** no worries.

**Theodore Kelechukwu Onyejiaku:** Yeah.

**Theodore Kelechukwu Onyejiaku:** I must have missed that.

**Theodore Kelechukwu Onyejiaku:** Oh, sorry.

**Vivek Shankar:** No worries.

**Theodore Kelechukwu Onyejiaku:** No worries.

**Theodore Kelechukwu Onyejiaku:** Yeah, I think this should be.

**Vivek Shankar:** There we go.

**Vivek Shankar:** Yeah, cool.

**Vivek Shankar:** Awesome.

**Vivek Shankar:** We will queue that up and get started with it.

**Vivek Shankar:** And then, yeah, this is more of a Victor thing, I guess.

**Vivek Shankar:** But, yeah, 2026 planning.

**Vivek Shankar:** So...

**Vivek Shankar:** The thing that I wanted to address in our first meeting in January is just to understand any internal initiatives that you're taking, either with the product or any other marketing initiatives.

**Vivek Shankar:** You know, Paul, I know Victor had mentioned that you were working on something, a Strapify initiative, something he mentioned.

**Vivek Shankar:** So the idea is just to, you know, align on what you're seeing from the marketing side on your end, so that we can align in terms of topics, goals, any competitor focus, et cetera.

**Vivek Shankar:** So, yeah, that's coming in January, but just wanted to see it right now.

**Paul Bratslavsky:** So, yeah, like, I mean, like, for me, like, one thing that I want to focus on is showcasing, you know, Strapify use with a wide variety of different UI libraries, you know, and frameworks.

**Paul Bratslavsky:** So that way, you know, people have visibility that, like, you could literally build any framework you want with whatever.

**Paul Bratslavsky:** You are all you want using, you your Strapi backends.

**Paul Bratslavsky:** So that's the idea that, you know, just to show a lot of front-end kind of focused stuff.

**Paul Bratslavsky:** Because basically the problem that Strapi solves, that you are a front-end developer and you might not be like a really good back-end developer.

**Paul Bratslavsky:** Like you don't need to be, right?

**Paul Bratslavsky:** Strapi got you covered.

**Paul Bratslavsky:** And so you're more concerned building that end product, which is user-facing.

**Paul Bratslavsky:** And so that's where like pretty UI comes into place and like different, you know, component libraries.

**Paul Bratslavsky:** And I saw that on the list that you provided for the integration pages.

**Paul Bratslavsky:** You did mention like a good amount of the front-end UI libraries.

**Paul Bratslavsky:** So that's in alignment.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Cool.

**Vivek Shankar:** Yeah, so let me just run through the issue list real quick.

**Vivek Shankar:** I think most of these are pretty much settled.

**Vivek Shankar:** But yeah, there was this comparison page thing.

**Vivek Shankar:** I know Victor, like basically removing the table from...

**Vivek Shankar:** The top of the comparison pages, I know this was with Notum, I know, I think Victor was the one following up on this, but just want to check if there's been any progress here, or?

**Paul Bratslavsky:** I'll double check for that.

**Paul Bratslavsky:** Go ahead, Peter.

**Theodore Kelechukwu Onyejiaku:** Okay, about this, I'm not quite sure how it's been so far, the issue so far with Notum, like the one I shared recently, is about the issues you've been having with the preview, and the video insertion, and publishing.

**Paul Bratslavsky:** So, yeah.

**Paul Bratslavsky:** Yeah, no worries, I can follow up.

**Paul Bratslavsky:** Yeah, so the basic, I was going say, the basic guess is that they had, like, more pressing issues to deal with, and so kind of went down to this, and basically, right now, it's like, they'll get there when they get there, but there's some critical priority checks.

**Vivek Shankar:** Okay, no worries.

**Vivek Shankar:** Thanks.

**Vivek Shankar:** And then that was the one about adding the videos to the comparison pages.

**Vivek Shankar:** Theo, I think I sent you the list last week.

**Vivek Shankar:** was wondering if you need anything there.

**Theodore Kelechukwu Onyejiaku:** Yeah, similar to what I just said, I wanted to do this, although I've cleared out the blogs and the integration pages that were still outstanding.

**Theodore Kelechukwu Onyejiaku:** So what I noticed was that when I published some articles, they don't get to reflect on the live page.

**Theodore Kelechukwu Onyejiaku:** And any update as well tries to break the, what's it called, the page or the comparison page.

**Theodore Kelechukwu Onyejiaku:** And then I discovered, or they discovered as well, that we are not filling in the CM field, which is the comparison fields for the two technologies we are comparing.

**Theodore Kelechukwu Onyejiaku:** I just shared that on Slack.

**Theodore Kelechukwu Onyejiaku:** If you've gone through a draft, you would find a field called CN that gives you a breakdown of each technology on their page when you view them live.

**Theodore Kelechukwu Onyejiaku:** So some of them are missing because we don't already have them.

**Theodore Kelechukwu Onyejiaku:** So I requested if you could generate that for all the comparison pages you have created so that we can be able to add them and have it not break the server or the comparison.

**Theodore Kelechukwu Onyejiaku:** Yeah.

**Vivek Shankar:** Okay.

**Vivek Shankar:** I will enter this as a to-do task in the table after this meeting.

**Vivek Shankar:** And, yeah, just in terms of timelines, I think we will be ready to take this on in early Jan, just given the out-of-office, because we have a person who works in growthx, basically, who handles all the CMSs and the pages, et cetera.

**Vivek Shankar:** He is going out of office.

**Vivek Shankar:** So, yeah, it's just a resourcing question on our end, but it shouldn't be a big deal.

**Vivek Shankar:** Yeah, but that sounds kind of a little bit on the holiday free stuff, but mean, everybody's Yeah, and then the FAQs, these are pretty much done.

**Vivek Shankar:** From what I understand, we're just going through the final sort of reviews and changes.

**Vivek Shankar:** The issue that Usman had lagged regarding the previews, not sort of, we're not able to preview changes, which has gone to Notum, that is connected to this issue as well.

**Vivek Shankar:** So, basically, there's a lot with Notum, basically.

**Vivek Shankar:** And then the last one was, yeah, the comparison pages, which, again, I think we can maybe club a lot of these things into this one issue, basically.

**Vivek Shankar:** It's all around the same thing.

**Vivek Shankar:** So, that's pretty much the issues, and then moving quickly to the performance side of things.

**Vivek Shankar:** So, yeah,

**Vivek Shankar:** Our sessions are pretty strong, given that this is two weeks' worth of traffic, we're making pretty, you know, very good progress.

**Vivek Shankar:** December, we do expect it to be a slow month, because I think next week and the week after that is basically the holiday period, but still, momentum is strong.

**Vivek Shankar:** And yeah, I just wanted to address questions over here.

**Vivek Shankar:** I can always follow up with them in Slack as well.

**Vivek Shankar:** But generally, these were the five pages that were the top performance this past week.

**Vivek Shankar:** This is nowhere near a red flag, but just want to point out that LLM traffic has been a bit sluggish to the overall website.

**Vivek Shankar:** Victor's question was, you know, is this happening across a lot of accounts?

**Vivek Shankar:** But to be honest, it's a bit of a mixed bag.

**Vivek Shankar:** Generally, December is a bit sluggish, and even for LLM traffic, it has been a sluggish start for many accounts.

**Vivek Shankar:** There are exceptions, of course, but this doesn't mean that we should not dig into this.

**Vivek Shankar:** But...

**Vivek Shankar:** Thank

**Vivek Shankar:** We're not seeing any issues.

**Vivek Shankar:** One way we are trying to sort of figure this out is we can actually run page audits in Scrunch, so for the homepage and for other important pages.

**Vivek Shankar:** So we're running it for a few of those and just seeing if we can flag anything.

**Vivek Shankar:** I don't expect anything to come up because your website is generally in excellent condition, so it's still worth a shot.

**Vivek Shankar:** Speaking of Scrunch, there's not been much change in terms of the positioning for all the queries that we are tracking.

**Vivek Shankar:** Strapi is still in the first place for pretty much every category.

**Vivek Shankar:** The sentiment is very high at 92%, which is great.

**Vivek Shankar:** Positions mostly at the top.

**Vivek Shankar:** yeah, generally things are looking good.

**Vivek Shankar:** And, you know, in terms of looking ahead for January, we have our priorities because Victor already kind of gave us input into that.

**Vivek Shankar:** So we're prioritizing the integration pages.

**Vivek Shankar:** We've always been, sorry, we've always been prioritizing.

**Vivek Shankar:** We're refreshes as well, and we do have the new agency owner persona that Victor had pointed us to, so I'll be adding a few topics at the end of this week and early in January just for your review, and of course, we're doubling down on the developer persona.

**Vivek Shankar:** So, yeah, generally, you know, we've ended the year well, and yeah, we're in good shape heading into 2026.

**Paul Bratslavsky:** Yeah, sounds good.

**Vivek Shankar:** Cool.

**Vivek Shankar:** And yeah, that was pretty much all I had for today.

**Vivek Shankar:** And yeah, I guess there's nothing else.

**Vivek Shankar:** Happy holidays.

**Vivek Shankar:** you in the new year.

**Vivek Shankar:** And I am available on Slack, of course.

**Vivek Shankar:** So, yeah.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Sorry, Paul.

**Paul Bratslavsky:** I didn't mean to interrupt.

**Paul Bratslavsky:** Oh, no worries.

**Paul Bratslavsky:** I said, yeah, to you and your family.

**Paul Bratslavsky:** I hope you have a wonderful holiday in the year.

**Vivek Shankar:** Thank you.

**Vivek Shankar:** Thank you very much.

**Vivek Shankar:** All right.

**Vivek Shankar:** See you, everyone.

**Paul Bratslavsky:** Bye, everybody.

**Theodore Kelechukwu Onyejiaku:** See you.

**Theodore Kelechukwu Onyejiaku:** you.

**Theodore Kelechukwu Onyejiaku:** See

**Theodore Kelechukwu Onyejiaku:** Happy New Year in advance.

**Vivek Shankar:** Thanks to you.

**Paul Bratslavsky:** Bye.

**Paul Bratslavsky:** Bye.

**Theodore Kelechukwu Onyejiaku:** Bye.
