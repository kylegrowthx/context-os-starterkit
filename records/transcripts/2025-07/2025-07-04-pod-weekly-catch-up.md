# Pod weekly catch up

<metadata>
date: 2025-07-04
time: 14:03 UTC
duration: 13 minutes
organizer: oluwatimilehin@growthx.ai
participants: Vivek Shankar, Nika Narimanidze, Oluwatimilehin Ademosu, Ismail Ajagbe
fathom_recording_id: 72301382
fathom_url: https://fathom.video/calls/342908166
share_url: https://fathom.video/share/r2RkgGqCXxAnjEjmydRJT8F9ANmYuM8H
source: fathom
enriched_on: 2026-03-03 14:35 UTC
</metadata>

---

## Summary

The GrowthX Labs content delivery team held a weekly sync to address quality issues, process improvements, and workload planning. Vivek emphasized raising questions early in the assignment stage rather than compounding errors through the generation and editing pipeline—a five-minute conversation upfront saves a full day of rework. The team discussed client-specific requirements (Rapid needs header subtitles, Strappy needs "in brief" bullets), introduced new Q3 pillar templates to streamline workflows, and coordinated next week's full data grid load with publishing responsibilities and Strapi automation needs.

---

## Context

This is an internal weekly operations sync for GrowthX Labs' content production pod—the team responsible for delivering client content (articles, comparison pages, data grids) to clients like Rapid, Strappy, and others. The pod works within an automated content generation pipeline (Atlas assignment flow → article generation → review → publishing). Vivek leads the team and owns the Q3 strategy and pipeline optimization; Nika and Oluwatimilehin are content operators; Ismail handles administrative tasks. The meeting happens amid a high-velocity delivery cycle (60-90 minute target per article) with process challenges around attention to detail, early problem identification, and publication timing. One participant (Mara) was invited but did not speak.

---

## Relevance

- **To GrowthX Delivery:**
  - Critical insight on error compounding: small mistakes at assignment stage magnify into full article rewrites by publishing (one day of lost time). Procedure change: raise high-level article approach for async review rather than discovering issues downstream.
  - Client-specific requirements vary and must be matched in assignment (Rapid: header subtitles; Strappy: "in brief" bullets). Missed requirements trigger edit cycles.
  - New templated approach for Q3 pillars eliminates manual assignment flow modification; Kirk is automating further.
  - Strapi publishing automation is a bottleneck—Vivek handling manually. Ticket needed.
  - Data grid formatting issue: Atlas is generating H1 titles in body text; Oluwatimilehin must strip these before publishing.

- **To GrowthX Business Development:**
  - Rapid and Strappy are active clients with multi-article workloads and tight formatting requirements.
  - Team confidence high despite operational friction; Vivek explicitly affirmed performance and encouraged psychological safety on asking clarifying questions.
  - Freelancer articles from two weeks prior are still in the publishing queue; workload management needed.

- **To GrowthX Ops:**
  - Time tracking shows actual hours vs. planned 60-90 minutes per article. Oluwatimilehin reported strategy errors (Galileo article overcomplicated as listicle). Process training on simplicity and early feedback loops needed.
  - Airtable compliance: All three operators must log delivered articles weekly for Andy (admin/analytics).

---

## Overview

- Need to improve attention to detail and client-specific requirements to minimize edits
- Emphasize early problem-solving: raise doubts at assignment stage to prevent compounding issues
- New Q3 pillar templates introduced to streamline assignment process
- Time management and strategy improvements needed to reduce overall time spent on articles

---

## Key Topics

### Quality Control and Client Requirements

  - Specific client needs must be met (e.g., Rapid needs subtitles, Strappy needs "in brief" bullets)
  - Attention to detail crucial to avoid wasted edits
  - Vivek encourages raising doubts early in the process to prevent compounding issues
  - Team should share high-level article approaches in chat for quick feedback

### Workflow Improvements

  - New templates for Q3 pillars introduced to streamline assignment process
  - Kirk working on automation for assignment flow
  - Strapi publishing automation needed; ticket to be created
  - Data grid process adjustments: Timmy to publish directly after fixing formatting issues

### Time Management and Efficiency

  - Goal: 60-90 minutes average time per article
  - Timmy reported spending more time than intended due to strategy mistakes
  - Nika faced challenges with Emicronia and data grid erasure
  - Team encouraged to be more conscious of potential issues early in the process

### Client-Specific Updates

  - Rapid: Subtitles needed for all headers, focus on pain points or benefits
  - Strappy: Two articles in progress, including e-commerce microservices architecture
  - Data grid: Full load expected for next week

### Article Review Process

  - Nika to spot-check 1-2 of Timmy's data grid articles
  - Vivek handling Strappy comparison pages for next week

---

## Action Items

**Nika Narimanidze (GrowthX Labs)**
- Review 1-2 of Oluwatimilehin's data grid articles for formatting issues (next week)
- Add subtitles for all headers in Rapid articles (focused on pain point or benefit-oriented subtitles)
- Fill out Andy's Airtable with names of delivered articles this week

**Oluwatimilehin Ademosu (GrowthX)**
- Remove H1 titles from body text in Atlas drafts for data grid articles before publishing
- Fill out Andy's Airtable with names of delivered articles this week

**Ismail Ajagbe (GrowthX Labs)**
- Fill out Andy's Airtable with names of delivered articles this week

---

## Transcript
**Vivek Shankar:** There's a lot of little things we're missing. I don't want to give any specific examples, but things I listed in the thread. Other things—some clients need certain specific information. For example, Rapid needs a subtitle for each article, Strappy needs "in brief" bullets. Let's just make sure it's all on point. Because if it's not, it's just a wasted round of edits.

**Vivek Shankar:** Speaking of edits, I'd like us to minimize the amount of back and forth next week. Generally, I think you need to be a little more aware of how problems expand. We're not writing things manually, so if we have a small mistake in the beginning, it compounds into entirely something else by the end of the process and the entire article goes off.

**Vivek Shankar:** So if you have any doubts at the assignment stage, bring them up to me. We can drop the high-level approach for your article in the chat, we'll take a look and solve it there. If we can stop that problem—which takes about five minutes at the assignment level—versus the article gen level or editing stage, we save one day. Because if the article is wrong, you're going to have to do the whole thing all over again.

**Vivek Shankar:** So please be very conscious in the beginning. If something is not clear, even just a little bit, bring it up. You'll save yourself a lot of heartache and we won't be sitting on a Friday trying to figure out how to publish articles. Generally, despite all that, I think we made some pretty good progress. Really happy with the way you guys executed everything. I know it's hectic, but thanks a lot.

**Vivek Shankar:** One more note. When you run your data grids next week—we're going to be on a full load—Nika, do you want to review the articles or can they just be published and staged in the CMS directory? I think the only issue was formatting.

**Nika Narimanidze:** If they fix it, it's okay, but I'll check one or two.

**Vivek Shankar:** Yeah, no worries. So, Timmy, regarding formatting—I'm sure Nika told you about this, but one thing: your articles still have the title in them. When we publish to Webflow in the body text, the title shows up. So delete that in your drafts. In Atlas. That's for data grid. Because I just published all your articles from the image gen and all of them had H1 titles in the body. Just delete that and we can push it in.

**Vivek Shankar:** Maybe next week on Monday, send a couple for Nika's review. If that works, just run everything all the way until published. For next week, we'll be starting on the Q3 pillars. I created specific templates, so you just have to copy-paste the template into the assignment flow. If you're seeing any errors, let me know. Basically I did that so we don't have to spend time manually modifying the assignment flow. Kirk is working on an automation for that. I don't know when it's available, but hopefully that makes life even easier.

**Vivek Shankar:** Strapi publishing, we need a ticket to automate that because it's a real pain. Oluwatimilehin, if you want to assign more articles to me, assign it. I see there's four more or however many left to publish. So just assign more to me.

**Vivek Shankar:** That was all I had. Floor is yours now. Is there anything you guys want to bring up? Any questions, any issues, general thoughts about how things went?

**Nika Narimanidze:** Is it okay if I ask about Rapid subtitles? That needs to be done for all headers, just double-checking, because I've seen some previous examples in Airtable and some were missing.

**Vivek Shankar:** Yeah, that Airtable is not a good example because the previous articles were different. We need a subtitle for all headers. The subtitle can be pain-point oriented or benefit-oriented. For the article I just did, I put "stop payment failures"—understand the style?

**Nika Narimanidze:** We'll do the same for the other article.

**Vivek Shankar:** Anything else? Anything about process or time spent on articles? Are you guys averaging 60 to 90 minutes or more?

**Oluwatimilehin Ademosu:** I think I did a pretty good job managing my time and allocating tasks. But when I checked the total time spent on edits, I spent a lot more than I should have. That was because of overall strategy mistakes. Next week I want to work on that because when you told me to redo some articles, it was really frustrating. That was my fault, so I want to avoid cases like that.

**Vivek Shankar:** That goes back to what I mentioned about bringing up doubts at the beginning. For those articles, if you had dropped the high-level direction in a thread, it would have been super easy. The Galileo article was a good example—we just needed a listicle, but you overcomplicated it. Feel free to do that for all your articles next week. I'm not evaluating you on that basis, so don't feel like asking questions is a bad job. Just be more conscious about where you have doubts. Even the smallest doubt will magnify into something else entirely by the time you finish. So don't ignore that in the beginning.

**Nika Narimanidze:** I think the week was okay generally. I had a few bumps with some tools and the data grid erasure issue, but I liked the distribution structure. Hopefully next week goes better.

**Vivek Shankar:** The data grid being erased was an issue. That's probably why your plate is full. You're almost done with articles and have one or two left with outlines already done. One was a Strappy article, right?

**Nika Narimanidze:** The second Strappy one is the e-commerce microservices architecture. We have a call to cover the heading process so I minimize my impact. There's also one Rapid Telegraph Transcripts article. I left some queue headers so it's not huge work. We'll be done shortly.

**Vivek Shankar:** The main thing left for you is the data grids from the freelancers from two weeks back and some articles I'm still running. There's three of those taking forever. But mostly it's the freelancer articles. If you need help staging them, let me know.

**Oluwatimilehin Ademosu:** Yeah, I wanted to ask about Strappy comparison pages. Am I going to be doing any next week?

**Vivek Shankar:** I'm thinking of doing all of them myself because they're pretty straightforward pages. We can put them into the assignment grid and it should return the information we need. I'm thinking of asking Kirk to build a flow as well because they're very templated pages. We can click a button and make sure it's all in place. So yeah, for next week, I'll handle those.

**Vivek Shankar:** Anything else you guys want to bring up? Hopefully everything is clear by this point. For next week, the cadence with updates, client communication, articles—we just want to make sure everything is in place. Good stuff, everyone. Nice work. And despite the hiccups, I think you guys did an awesome job. Thank you very much. Just keep asking those questions. I'm here to help out. So let me know.

**Vivek Shankar:** One last reminder—make sure you fill out Andy's Airtable. We need to fill out which articles we've delivered this week. She wants the article names and your name. Just fill it out. If you don't have time in the next few hours, let me know and I'll do it for you.

**Ismail Ajagbe:** Okay, I think I should get to it.

**Vivek Shankar:** Thanks a lot, everyone. Bye.
