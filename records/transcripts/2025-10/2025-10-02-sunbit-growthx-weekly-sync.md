# Sunbit <> GrowthX - Weekly Sync

<metadata>
date: 2025-10-02
time: 16:02 UTC
duration: 16 minutes
organizer: team@growthxlabs.com
participants: Ehtisham Hussain, Jason Beltran, Angel Kemper
fathom_recording_id: 91452854
fathom_url: https://fathom.video/calls/427808769
share_url: https://fathom.video/share/pYcEcH8Yg1os8s6Uy9u3HsyK7Kp8myGr
source: fathom
enriched_on: 2026-03-02 14:35 UTC
</metadata>

---

## Summary

GrowthX's content delivery team met with Sunbit to review traffic performance, discuss technical issues affecting major traffic-driving articles, and align on a phased webhook-based content delivery approach. Active users declined from 390 to 324 over recent weeks, with two high-performing articles (clear aligner cost, dental tips) returning 404 errors due to a mid-August blog template update affecting pre-August post URLs. The team agreed to send articles in batches (5, then 10, then full) via webhook to Sunbit for Claude-assisted summarization, while Jason (Sunbit) investigates URL issues and the GrowthX team prepares to review and fix URLs for older blog posts from June-August.

---

## Context

Sunbit is a financing solutions provider for merchants in automotive repair and dental sectors. GrowthX is developing content marketing and SEO strategy for Sunbit's blog, focused on attracting shop owners and encouraging partnership adoption. Kyle Gaudreau (GrowthX's primary point person) was absent from this sync due to illness, so Ehtisham Hussain covered the traffic and strategy updates. The meeting happened as a routine weekly sync to review traffic metrics, address blockers in the content pipeline, and align on how to automate and scale article delivery. The relationship includes a technical integration point: GrowthX sends articles via webhook to Sunbit's platform for Claude-assisted summarization and enrichment before publication.

---

## Relevance

**To GrowthX Delivery:**
- Webhook-based content delivery system is ready; testing batch approach (5 articles, then 10, then full) before scaling to avoid operational overload
- Content pipeline automation (focus keywords, cluster, summary, key takeaways) owned by Sunbit's dev team; ETA 2 weeks — indicates vendor dependency risk and need for interim manual processes
- Template update infrastructure issues affecting blog URL structure suggest need for coordinated deployment practices (redirects must be in place during template migrations)
- B2B content strategy expansion (merchant adoption verticals for auto and dental) adds complexity to content planning; requires feedback loop discipline (comments in Word doc, tags)

**To GrowthX Business Development:**
- Sunbit partnership health signal: proactive, engaged reviews; identifying technical blockers early; organized feedback process indicates collaborative relationship
- Traffic decline trend (390 → 354 → 363 → 324 active users) suggests content performance issue beyond SEO; URL errors compounding organic visibility loss
- Shop directory views uptick (55 → 57) and engagement time slight increase are minor positive signals but insufficient to offset traffic decline
- Two articles returning 404 were "major traffic winners" per historical GA4 data — fixing these and older posts (Jun-Aug window) likely highest-leverage quick win

---

## Overview

- Traffic trend shows a slowdown in decline; shop directory views increased slightly
- Major traffic-driving articles (e.g., clear aligner cost) are 404ing due to URL structure changes
- New B2B content clusters for auto and dental merchant adoption are being developed
- GrowthX to start sending articles through webhook for Claude-assisted summarization

---

## Key Topics

### Content Pipeline and Delivery

  - Kyle (absent) out sick; Ehtisham covering report
  - Dev team working on automating focus keywords, cluster, summary, and key takeaways (ETA: 2 weeks)
  - Immediate plan: Send 5 articles via webhook, monitor, bug-bash, then scale up to 10, then full batch
  - Jason to use Claude for summaries and key points extraction

### Traffic and Analytics Update

  - Sessions and active users continued downward trend (390 → 354 → 363 → 324)
  - Shop directory views increased slightly (55 → 57)
  - Average engagement time saw a slight uptick
  - Major traffic winner (clear aligner cost article) now 404ing

### Technical Issues

  - Multiple high-traffic articles (including dental tips) returning 404 errors
  - Likely cause: Blog template update affecting older posts' URL structures
  - Action: Team to review and fix URLs for posts from June-August, pre-dating new blog layout (mid-August)
  - Angel suggested using a path checker tool for efficiency

### New B2B Content Strategy

  - 2 new clusters: auto merchant adoption and dental clinic adoption
  - Article structure: Address industry challenges → Present statistics → Discuss financing benefits → Introduce Sunbit
  - Use case studies and third-party sources to build credibility
  - CTA: "Become a Sunbit partner"
  - Feedback process: Leave comments in Word doc, tag Ehtisham

### Content Mix and Publication

  - Will intersperse new B2B cluster content (5-10 articles/week) with existing auto part and dental cost topics
  - Ready-to-publish articles to be sent via webhook

---

## Action Items

**Jason Beltran (Sunbit)**
- Monitor webhook, bug bash, inform Ehtisham when to send more articles
- Investigate/fix 404 errors, especially "clear aligner cost" article
- Contact website agency to investigate potential causes of 404 errors
- Review new B2B cluster articles, comment in Word doc, tag Ehtisham
- Check and fix URLs for older blog posts (June-August) affected by template update

**Ehtisham Hussain (GrowthX)**
- Send 5 articles via webhook to Jason for testing

**Angel Kemper (Sunbit)**
- Review new B2B cluster articles, comment in Word doc, tag Ehtisham

---

## Transcript
**Angel Kemper:** This meeting is being recorded.

**Ehtisham Hussain:** So Kyle won't be joining us today, he's out sick.

**Angel Kemper:** Sounds good. Sorry to hear.

**Ehtisham Hussain:** Hi, Jason.

**Jason Beltran:** Hey, how are you?

**Ehtisham Hussain:** I'm good, good. So Kyle won't be joining us. I'll just continue with the report. Hopefully we can use today's meeting time to go over the new content from the new cluster.

**Jason Beltran:** Okay, perfect.

**Ehtisham Hussain:** One article — that's a B2B article encouraging automotive shop owners to become partners. Let me share my screen. Yep, you can see it. So I'm still going through all the articles for this batch. I'll be submitting articles in a couple of hours from now.

**Ehtisham Hussain:** About the ticket — the dev team is working on automating focus keywords, cluster, summary, and key takeaways before the article. They've put it in the current cycle. It's going to take them a couple of weeks. So I was thinking I'll just start sending articles to you via the webhook, as we discussed.

**Jason Beltran:** Yeah, totally. If you start sending them through now, I have everything set up where I'm using Claude to write the summary and extract key points.

**Ehtisham Hussain:** So should I be sending them in batches — batches of five, ten?

**Jason Beltran:** Yeah, I think so. If you can send five today, I'll monitor it, do some bug bashing, and Slack you to let you know when to continue. We can do five, then ten, then continue bug bashing. If we're feeling good in the next couple of days, you can send them all over.

**Ehtisham Hussain:** Sure. I've written that down, I'll send them over immediately after the meeting. I'll run the workflow and hopefully we can get five articles over to you.

**Ehtisham Hussain:** So, let's come to traffic.

**Ehtisham Hussain:** Last week I reported that sessions and active users went down, and there were a couple of articles that lost rankings. One was the "car won't start" article. Since Angel set up the redirect, that one is picking up traffic again. That's a good sign. But the downward trend has continued — it went from 390 to 354, 363, then 324 active users. Shop directory views went up from 55 to 57, which is positive. Average engagement time went up slightly. But now another major traffic winner — the "clear aligner cost" article — is returning a 404. That wasn't a 404 last week. This is a major traffic winner. According to historical Google Analytics data, this used to get a lot of organic traffic. I'll send it over on Slack.

**Ehtisham Hussain:** So is there something going on with the website? I see some fluctuation.

**Jason Beltran:** Yeah, I don't know what's going on there. I need to look and talk to our agency to see why those are changing. Maybe they're working on updating the blog structure.

**Angel Kemper:** But I don't think they're changing URLs, though, because surely if they are, they would be placing redirects while they do it.

**Jason Beltran:** Yeah, I don't know. It's interesting. I'm going to reach out to our website agency and see.

**Ehtisham Hussain:** Yeah, so there could be something going on over there. This was the "clear aligner cost" article — a major traffic winner. It's one of our top traffic drivers that went 404.

**Angel Kemper:** I wonder if we can get a quick report to proactively check for additional 404s. There might be more we don't even know about that are traffic drivers. We're posting this content on social, so we want to catch broken links.

**Jason Beltran:** Yeah. So what's happening is the slug and title in those two articles were updated. The slug is what assigns the overall URL. Whenever that gets updated to the article title, everything breaks. So far it seems like just those two, but I'm going to see if there are any others. I've also reached out to our agency to see if there's something that caused this.

**Angel Kemper:** Seems like a template update would be my guess — if they were updating the blog template.

**Jason Beltran:** Yeah. And it may have been for some of those older posts that weren't on the new blog template before we updated it. Maybe we can look at some of those older posts.

**Ehtisham Hussain:** And then the next thing on my agenda is to review the B2B content. We came up with two new B2B clusters — one for auto merchant adoption, one for dental clinic adoption. Articles like "How auto repair shops can boost revenue with financing solutions." In the main title, we mention Sunbit. Some initial drafts were too much like an ad for Sunbit, so I've toned that down. We're first talking about the challenges auto repair shops face, then statistics about how people are more likely to get repair work done if financing is available. We're linking to third-party articles about Sunbit and case studies from their website. We're mostly talking to shop owners about the benefits of financing, then bringing in Sunbit. All links are Sunbit-related, internal and external. The main focus is on offering financing options, and then we connect it to Sunbit. The CTA at the end says "Become a Sunbit partner" and explains how. That's the general structure. Once you guys read it, you'll have feedback for me.

**Angel Kemper:** Yeah, that sounds great. Where would you like us to provide feedback — directly in the doc, in Slack, or in the OS table?

**Ehtisham Hussain:** The best place is to just leave a comment in the Word document. That way I immediately get notified. If you see something that's too salesy, or if we're linking to something we shouldn't, just leave a comment.

**Angel Kemper:** Should we tag you?

**Ehtisham Hussain:** Yeah, if you tag me, that's better.

**Angel Kemper:** We can do that.

**Angel Kemper:** Also, I noticed the slug doesn't look like the same slug. It looks like it's auto-updating the slug to the entire block title, which isn't how it was.

**Jason Beltran:** Yeah, so what's happening is the slug and title in those two articles were updated. The slug is what assigns the overall URL. Whenever that gets updated to the article title, everything breaks. So far it seems like just those two, but I'm going to see if there are any others.

**Ehtisham Hussain:** Yes, because I'm only catching the ones that used to bring in a lot of traffic.

**Jason Beltran:** There may be a lot more. Yeah, I'm going to look at our older dental tips. That's exactly what happened. So we're going to have to go into our older dental tips and auto tips too, probably. This doesn't look like a slug we would have put in. So we're going to have to go back to the Airtable and make sure the URLs match.

**Angel Kemper:** Good thing we've been logging those URLs in Airtable. I think there's a path checker tool we could use — maybe there's an easier way to do this without having to cross-check manually.

**Jason Beltran:** Isadora's team can do that, but I don't want to wait. I think it's easier for us to just go through anything done in June, July, or August and double-check them. Since we launched the new blog layout mid-August, anything before that we probably have to revise.

**Angel Kemper:** Okay.

**Jason Beltran:** I don't think it's going to be a large amount, which is nice.

**Ehtisham Hussain:** All right, so I'll get to sending you the ready-to-publish blog posts and articles via webhook. That's it — do you guys want to discuss anything else?

**Jason Beltran:** No, I think we're good. As long as you send over those ready-to-publish articles through the webhook, I think we're good. And then we'll review those articles you were bringing up — the new finance cluster articles.

**Ehtisham Hussain:** The new cluster. We're going to mix it up. It's not going to be just that cluster. We're going to continue with the auto part costs and dental costs, but put five or ten of the new B2B articles in there every week.

**Jason Beltran:** Perfect.

**Ehtisham Hussain:** Sounds good. All right, have a nice day, everyone.

**Jason Beltran:** All right. I'm going to go in and fix all these URLs now with the rest of our time. Okay, bye.
