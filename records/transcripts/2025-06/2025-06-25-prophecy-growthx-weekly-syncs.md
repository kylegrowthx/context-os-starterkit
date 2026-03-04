# Prophecy <> GrowthX Weekly Syncs

<metadata>
date: 2025-06-25
time: 17:00 UTC
duration: 19 minutes
organizer: ehtisham@growthx.ai
participants: Ehtisham Hussain (GrowthX), Vivek Shankar (GrowthX Labs), Darrell Etherington (GrowthX), Mara Leighton (GrowthX), Cody Carmen (Prophecy), Matt Turner (Prophecy)
fathom_recording_id: 70502064
fathom_url: https://fathom.video/calls/335216029
share_url: https://fathom.video/share/hAa9yajDMFVUeWMS-54ynr3Bxg_kQjPV
source: fathom
enriched_on: 2026-03-03 14:32 UTC
</metadata>

---

## Summary

GrowthX formally introduced two new content team members—Darrell Etherington (ex-journalist with Shopify and Apple content experience) and Ehtisham Hussain (13 years in content marketing across startups like Atlan and Pipe)—to the Prophecy team and outlined the transition plan for ongoing content delivery. Prophecy's content performance remains stable with 12 articles published last week; metrics show divergence between Google Search Console and GA4 but maintain positive trends, particularly for data engineering and ETL topic clusters. The teams agreed to expose topic cluster performance breakdowns in future reports, share GrowthX's Atlas content artifact management tool with Prophecy, and revisit knowledge base documentation post-Databricks Summit to incorporate new AI agent thought leadership.

---

## Context

This is a weekly operational sync between GrowthX's content delivery team and Prophecy, an AI data orchestration platform. Prophecy engaged GrowthX for content marketing services to drive organic visibility through targeted technical content around data engineering, ETL/ELT, and data orchestration workflows. With Prophecy's rapid product evolution and event activity (Databricks Summit), the partnership requires regular alignment on performance metrics, strategic priorities, and article handoffs between GrowthX's existing and newly onboarded teams. This particular meeting marks a formal transition point where two new GrowthX team members take delivery responsibility, necessitating knowledge transfer and process clarity to maintain continuity.

---

## Relevance

**To GrowthX Delivery:**
- Successful onboarding and transition of two new senior content team members (Darrell, Ehtisham) to Prophecy account requires continued partnership alignment and knowledge transfer sprints
- Atlas tool visibility and artifact documentation critical for maintaining Prophecy's confidence in deliverable consistency across team handoff
- Topic cluster performance breakdown request signals need for more granular analytics dashboards and category-level analysis in Looker

**To GrowthX Business Development:**
- Prophecy engagement remains active and healthy; client explicitly flagged willingness to continue collaborative topic selection beyond just execution
- Opportunity to expand Prophecy's content library post-Databricks Summit with fresh thought leadership synthesis into content pipeline
- Darrell and Ehtisham's complementary backgrounds (journalism + AI/SaaS product experience) position account for expansion into deeper technical and strategic positioning content

**To CheckThat:**
- Prophecy's platform focus on AI data orchestration and LLM reference traffic patterns provide ongoing reference data for CheckThat visibility research

---

## Overview

- Darrell Etherington and Ehtisham Hussain formally introduced as new GrowthX team members taking over Prophecy account delivery
- 12 articles published last week; sessions stable, views down slightly as expected; data engineering and Medallion architecture performing strongest
- Google Search Console shows increased clicks/impressions; GA4 data diverging but both metrics point to positive compounding effects
- Team to expose topic cluster performance breakdown by category to identify underperforming areas and inform strategic priorities
- GrowthX Atlas tool will be shared with Prophecy team via Loom for transparency on content artifact management and knowledge transfer
- Post-Databricks Summit thought leadership refresh and knowledge base gardening planned for next iteration

---

## Key Topics

### Team Introductions

  - Daryl: Ex-journalist, 1.5 months at GrowthX, experience in content production, organic search
  - Ehtisham: 13 years in content marketing, diverse roles (writer to product marketing), AI platform experience

### Content Performance Update

  - 12 articles published last week, 2 in edit phase
  - Sessions stable, views decreased (expected after previous week's outlier)
  - Top performers: data engineering, ETL, ELT, Medallion architecture
  - GSC shows increased clicks/impressions; GA4 data diverging but overall positive trend
  - Return direct traffic volatile but average rising
  - LLM referrals stable; ChatGPT highest referral source

### Content Strategy Discussion

  - Need for breakdown by topic clusters to identify underperforming areas
  - Plan to expose backend Looker data for better category analysis
  - Goal: Inform decisions on content priorities, rewrites, or approach changes

### Transition and Knowledge Transfer

  - Articles split between current and new team for consistency
  - GrowthX to share "Atlas" tool walkthrough for content artifact visibility
  - Emphasis on maintaining partnership in topic selection and execution

### Content Refresh and Priorities

  - Recent events (Databricks Summit, AI agents) necessitate content updates
  - Plan to review and potentially refresh knowledge base docs
  - New thought leadership material to be distilled and incorporated

---

## Action Items

**Vivek Shankar (GrowthX Labs)**
- Add topic cluster performance breakdown to visible metrics in next week's report

**Cody Carmen (Prophecy)**
- Review goals/knowledge base for any critical info to pass to new GrowthX team members

**Darrell Etherington (GrowthX)**
- Create and share Loom video walkthrough of Atlas tool with Prophecy team

**Matt Turner (Prophecy)**
- Compile doc of new thought leadership content from Databricks AI Summit for GrowthX team

---

## Transcript
**Ehtisham Hussain:** Yeah, there we go.

**Cody Carmen:** Hey, Vivek.

**Vivek Shankar:** Hey, everyone.

**Vivek Shankar:** Sorry if I was on mute.

**Vivek Shankar:** Classic.

**Vivek Shankar:** How's it going?

**Cody Carmen:** Are we waiting on Matt or do you think he's joining?

**Vivek Shankar:** Matt and Mara will be here in a few minutes.

**Vivek Shankar:** They're all in our offices in San Francisco, so they're trying to figure out the meeting rooms.

**Cody Carmen:** It's harder to get into a meeting on time in person these days than virtual.

**Cody Carmen:** Well, there's Matt, or at least Matt's screen.

**Vivek Shankar:** I don't know if you've already started talking to Ehtisham. He's one of our team members who will be taking over, so super excited to introduce him.

**Vivek Shankar:** Oh, there they are.

**Cody Carmen:** Sorry, a couple of minutes late.

**Darrell Etherington:** We were just figuring out the technology.

**Darrell Etherington:** That is really in person.

**Darrell Etherington:** We could probably start with some intros.

**Darrell Etherington:** This is Darrell, and I can share some background. So I joined about a month and a half ago, and I was a journalist for most of my career. I worked for a publication based out of Toronto. After that, I did a couple different in-house content jobs. I worked for Apple doing some of their initiatives, and then also ran content for Canada. I also worked at Shopify in a huge content marketing organization there. Most recently, I worked for a large Canadian pension-backed venture firm, spinning up their content program. I have a lot of experience in organic and search, but not the technical side—more the content production side. I'm learning the technical ropes here, and there's lots of good in-house talent to support that. Ehtisham, do you want to share as well?

**Ehtisham Hussain:** Hi, I'm Ehtisham.

**Ehtisham Hussain:** I have almost 13 years of experience in content marketing. I started as a writer in 2011, 2012, and since then I've worked as a writer, editor, manager, project manager, product manager, and product marketing manager. I have plenty of agency experience as well as in-house experience. I've written for companies like Pipe, Atlan, and others in the data and AI space. I've been reading up on Prophecy, and I'm excited to take over this account.

**Darrell Etherington:** Prophecy team, we'll get to know each other as we go.

**Cody Carmen:** Amazing.

**Darrell Etherington:** Vivek, if you want to run through the performance metrics, and then we can address any questions at the end.

**Vivek Shankar:** Yep, let me share my screen.

**Vivek Shankar:** Okay, so we covered introductions. For this week, we're working on articles in approval. Three of these articles are being worked on by Darrell, Ehtisham, and their team as part of the transition plan to keep everything smooth. We published 12 articles last week and are addressing edits on two articles.

**Vivek Shankar:** Overall sessions held pretty much the same as last week. Views fell, which we expected after last week's outlier. The articles performing well continue to perform well—data engineering, ETL, ELT, Medallion architecture has been doing really well over the past few weeks.

**Vivek Shankar:** According to Google Search Console, we saw a big jump in clicks and impressions this week. GA4 is showing we're at about the same peak as last week. Generally positive signs, though there's some divergence between the two data sources. Big picture, both are showing that we're seeing compound results from earlier articles. We're starting to refresh some articles from three to four months ago.

**Vivek Shankar:** Return direct traffic is volatile, but the average is rising, which is a positive sign. LLM referrals remain stable, and ChatGPT continues to be the highest referral source. Any questions on the performance overview?

**Cody Carmen:** I'd like to get a breakdown by topic clusters. Are any of these entirely underperforming? Then we can discuss what to do about them—whether we keep doing it but prioritize it lower, or if we need to re-approach it. Data engineering will probably sit on top for a while, but I'm less concerned with the top than with what's in the middle and bottom.

**Vivek Shankar:** We're actually tracking this on the backend in Looker. I just haven't made it visible yet, so I'll expose that. The data engineering topic is technically a miscellaneous category, which is why I didn't show it before.

**Cody Carmen:** That makes sense. We'll figure out how to sort through the noise we don't want to use for decisions. That's a key addition to our agendas.

**Darrell Etherington:** Then we can chat through refresh and rewrite recommendations as we get that visibility.

**Vivek Shankar:** Upcoming tasks are working on the articles. There was also an open question about the quarterly dashboard from Evan.

**Darrell Etherington:** I pinged Ashley to figure out where we are on that request.

**Cody Carmen:** Evan was going to get to it last Friday, but he's out this week. We'll get it next week when he's back.

**Vivek Shankar:** Yeah, that's a quarterly dashboard he puts together.

**Cody Carmen:** Alright, that was the update.

**Mara Leighton:** Matt, Cody, Mitesh—do you have any questions about the transition or anything else you want to chat through while we're together?

**Darrell Etherington:** We split up articles between the current and new team to maintain consistency, but let us know if you notice anything out of place.

**Cody Carmen:** I'll take a close look at our goals and knowledge base to make sure nothing's been missed. We really trust the GrowthX team as partners in not just executing content, but in topic selection. We want to make sure knowledge base and continuity are carried through.

**Darrell Etherington:** We're all in the same room, so we can adjust quickly with feedback. We might also share a Loom walkthrough of our Atlas tool so you have full visibility into the content artifacts we have in place. Nothing slips through the gaps at an atomic level. Darrell and Ehtisham can edit directly if needed.

**Matt Turner:** I have a question about where you're picking up from the background documentation. We gave you a lot of docs and refreshed them a couple months ago when Cody came on board. Do you have questions about that? Also, we just went through the Databricks Summit and published a lot about AI agents. Things are moving quickly, and we want to make sure we're not staying behind. Maybe in the next couple weeks we should think about a potential refresh of the knowledge base with that new material.

**Darrell Etherington:** I think we're in a good state. You've been thorough with documentation. We should treat it as living, though. If you have new priorities or want to target something for a specific event or conference, we can create new artifacts for that. We'll expose what we're working with so you can see if you want significant changes. We should also do some gardening on the knowledge base—it doesn't have to be so complex.

**Matt Turner:** Yeah, from the Databricks AI Summit, we have new thought leadership that we haven't distilled down to easy five-point summaries. There's more raw material to get to you. We can talk about distilling it collaboratively. We should probably put knowledge base gardening on the agenda for the next couple weeks.

**Darrell Etherington:** We can output it as documents and work from there. That sounds good. We can put together a doc of new stuff—it can be raw, and we can help with the processing.

**Matt Turner:** Well, thanks so much everyone. We've enjoyed working with you, and I think you'll really enjoy working with Darrell and Ehtisham. Obviously, as Darrell mentioned, we're all on the same team, so feel free to ping any of us whenever you need.

**Cody Carmen:** Thanks so much. Keep us in the loop.

**Darrell Etherington:** Thanks. We'll see you guys soon. Thank you so much for your time.
