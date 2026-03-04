# Prophecy <> GrowthX Weekly Syncs

<metadata>
date: 2025-04-02
time: 17:00 UTC
duration: 16 minutes
organizer: vivek@growthxlabs.com
participants: Vivek Shankar (GrowthX), Mara Leighton (GrowthX), Cody Carmen (Prophecy), Matt Turner (Prophecy)
fathom_recording_id: 55144764
fathom_url: https://fathom.video/calls/265892619
share_url: https://fathom.video/share/ySeeymRXjh6d3SAHh-DAcAqy7a3-6RZ5
source: fathom
enriched_on: 2026-03-04 09:00 UTC
</metadata>

---

## Summary

Prophecy and GrowthX reviewed content performance metrics, with impressions increasing significantly and clicks stabilizing at 10-15 per week. The team decided to consolidate competing ETL/ELT articles into pillar content to improve SEO performance, and discussed a repositioning strategy shift toward data engineering concepts (DEC) and non-technical audiences. Matt Turner flagged concerns about content attribution gaps in the Qualified/HubSpot integration, particularly for pre-registration engagement data.

---

## Context

Prophecy is a data integration platform that works with GrowthX on content marketing. This is a weekly check-in between the GrowthX delivery team (led by Vivek Shankar and Mara Leighton) and Prophecy's content/product stakeholders. The meeting focused on SEO performance metrics, content strategy adjustments, and analytics tracking challenges as they continue building out Prophecy's content library around data engineering topics.

---

## Relevance

**To GrowthX Delivery:**
- Content consolidation strategy (pillar content model) showing measurable impact on SEO metrics — 2 ETL articles will merge into 1, 1 ELT article becoming pillar post to reduce self-competition.
- GA4 event definition gaps with Evan (out of office) — follow-up required next week to align tracking with content strategy.
- Strong engagement metrics (50%+ sessions over 1 minute) validate top-of-funnel content approach even without conversion data.

**To GrowthX Business Development:**
- Account health positive: Prophecy proactively raising concerns about data attribution, showing engagement in optimization.
- Content is performing (data governance article jumped from 30s to top 10 ranking) — reference case for similar data engineering clients.
- Weekly sync cadence and active collaboration suggest healthy account relationship.

**To Prophecy Product/Strategy:**
- Repositioning toward DEC (data engineering concepts) and non-technical users will require JTBD article narrative shifts — impacts content roadmap.
- Pre-registration content consumption tracking gap in Qualified integration limits visibility into early-stage engagement — product team should evaluate workarounds.

---

## Overview

- Content performance: Impressions increased significantly, with clicks stabilizing at a higher level (10-15 range).
- Strategy shift: Consolidating ETL/ELT articles into pillar content to avoid self-competition and improve SEO.
- Metrics: 50%+ engaged sessions (1min+ or further exploration) indicate strong content quality.
- Repositioning: Shifting focus to DEC and non-technical users, impacting JTBD article approach.

---

## Key Topics

### Content Delivery and Publication Update

  - 3 articles delivered for review; 1 pending (Shadow ID)
  - 5 articles published last week
  - New article outline on "Original Pipeline Designed for BAs" posted in Airtable (includes webinar quotes)

### Analytics Tracking Challenges

  - GA4 event definitions: Follow-up needed with Evan (out of office)
  - Qualified/HubSpot integration limitations:
      - Content attribution tied to first email capture in a session
      - Pre-email content consumption not attributed
  - Matt raised concerns about missing data, citing previous funding announcement stats

### Content Performance

  - Impressions increased significantly
  - Clicks stabilized at 10-15 range (down from 15, but higher than previous baseline)
  - Standout articles:
      - Data governance article jumped from 30s to top 10
      - Data engineering skills article performing well
      - New ETL article showing promise

### Content Strategy Adjustments

  - ETL/ELT articles competing against each other
  - Plan to consolidate:
      - 2 ETL articles into one comprehensive pillar content
      - 1 ELT article to become pillar post (Anya's byline)
  - New focus: "Enhancing ETL" deep-dive article
  - 3 articles marked for refresh in Airtable

### Referral Traffic and Engagement

  - Referral traffic stable week-over-week
  - 50%+ engaged sessions (1min+ or further site exploration)
  - Strong indicator of content quality, especially for top-funnel content

### Q1 Overview and SEO Progress

  - Established good base with positive signals
  - Top performers: Data engineering skills and data governance articles
  - Ranking improvements:
      - Top 5 for various data engineering-related searches
      - Data silos article showing promise
  - Keyword breakdown available in Looker dashboard (some URL click data discrepancies noted)

### Repositioning Strategy

  - Shift focus to DEC and non-technical users
  - Will impact JTBD articles approach and overall narrative
  - Core topics to remain consistent

---

## Action Items

**Matt Turner (Prophecy)**
- Email Evan re. stat about blog engagement from funding announcement; clarify Qualified's tracking capabilities pre-registration

**Vivek Shankar (GrowthX)**
- Follow up w/ Evan on email from Matt re. Qualified tracking capabilities when he returns next week

**Cody Carmen (Prophecy)**
- Move Shadow ID article feedback to Airtable, tag Vivek

---

## Transcript

**Vivek Shankar:** How are you? Good, going well. I love how we're always the first ones on our calls.

**Mara Leighton:** Yeah. Hey Cody, how are you doing?

**Vivek Shankar:** Hello, how are you guys?

**Cody Carmen:** Doing well. Our weather has really been back and forth the last couple of weeks, even for the Atlantic Coast in the Northeast. Yeah, this is one of the weirder springs I've ever had here.

**Mara Leighton:** I saw that it was the greatest sizable jump in temperature on Saturday in New York's history. Went from about 80 degrees to the 40s in an hour. It was wild.

**Cody Carmen:** It dropped hard enough that when I was telling my wife about the temperatures and we were planning to go meet friends, I had to tell her it's going to drop about 25 degrees from right now by the time we get there.

**Matt Turner:** It dropped about 20 degrees in 15 minutes. We were at a soccer game and it was like one breeze and then it got freezing. Everybody was in shorts and they were all freezing afterwards.

**Mara Leighton:** It felt biblical, like the skies got all dark.

**Vivek Shankar:** I started thinking in Celsius once I crossed the planet, so 80 to 40 means nothing to me.

**Vivek Shankar:** All right. So just a quick update since last week's call, we delivered three articles to review. I believe you've gone through them. There's just one on the Shadow ID that needs a review from your end. We published five articles last week.

The major news is tracking everything between GA4 and Qualified. Evan is out of office this week, so I haven't been able to follow up with him regarding the event definitions at GA4. Regarding Qualified, he responded before he left.

Cody and I were discussing this yesterday. It seems like based on what he's describing, there's no foolproof way of tracking how a prospect is consuming content before they become a lead. What's happening is that on the Qualified dashboard, it's pulling in data from HubSpot, so we're dependent on what HubSpot attributes as content consumption. When a prospect visits the website and gives their email, that email becomes the first touch for that session. If anyone consumes content in that session, it gets attributed. If anything is consumed before that, it's not attributed. So it's not perfect, but it is something.

**Matt Turner:** Can we stop for a second? I know Evan's out, so I didn't respond to that thread. But we had a stat from the funding announcement about blog engagement. I see that came from Qualified, which is talking about a blog where nobody had logged in, but it was using Qualified's understanding of company origins to identify people from our ICP. I think we're missing something because I do think we have something prior to registration — I've seen data from it. I want to make sure either I was misunderstanding that or we had misrepresented it. We were able to report out article engagement from people from our ICP.

**Vivek Shankar:** Great. I will follow up with Evan and send you an email.

**Matt Turner:** I'm going to do that right now. When is he back?

**Vivek Shankar:** I assumed he'd be back on Monday. He's out this week.

**Vivek Shankar:** All right, so regarding the articles this week, we're working on them. We just delivered one: "The Original Pipeline Designed for BAs." I posted an outline in Airtable. It's going to look a little weird because we're including quotes from these webinars, but it will give you a good idea of what's going to be in each section.

**Matt Turner:** Where is that?

**Vivek Shankar:** It's in Airtable. I tagged you on it.

**Matt Turner:** It's in writing, at least. It's just the outline, not the full article.

**Vivek Shankar:** Any other questions about all of that?

All right, so moving on to the performance. We're still seeing volatile metrics. We had a big jump, then clicks settled a bit from about 15 to 10, but it's still higher than our baseline. The most encouraging thing is that impressions really took off. A couple of articles started showing up a lot in searches. The data governance article continues to do very well — it went from the 30s to top 10. The data engineering skills article and the new ETL article are driving performance.

Since it's been two to three weeks, we have a decent amount of data to see what's doing well and what's not. When we initially wrote the ETL and ELT articles, we wanted to see which approach would work. What we're seeing is that all four articles — two on ETL, two on ELT — are competing against each other and having mediocre performance.

So we're consolidating the two ETL articles into one big pillar content piece. We're going to follow SEO boxes and add additional insights from your webinars to create one comprehensive resource so we're not cannibalizing clicks. The other article will look at how we can enhance ETL — a deeper dive — and we'll see if there's search volume in that cluster. It ties in well with Prophecy's product.

We're doing something similar with the ELT post. We're taking the one post that's doing reasonably well — I believe it's under Anya's byline — and turning that into one pillar post on ELT. The other post addresses a subtopic of ELT, so we'll give it time and see if there's another angle we could take.

These are the main refreshes for next week. I've listed them in Airtable under "Needs Refresh" — you'll see three articles. That's the priority for next week.

Regarding referral traffic, we didn't see a huge jump — it's pretty much the same as last week. Something that stands out is the number of engaged sessions on page 2 of Looker. Engagement is defined by GA4 as when a user spends at least a minute on page or clicks to explore further on Prophecy's website. We're seeing over 50% engaged sessions, which is a pretty good indicator for the kind of content we're producing. A lot of the content has been top-of-funnel, and we have a few that are geared toward job-to-be-done. The average positions and impressions in Looker give a good idea of how often these terms are being searched and where Prophecy is showing up.

**Vivek Shankar:** So, upcoming tasks, we're working on four articles and the bigger task is the repositioning strategy we discussed yesterday. We're conducting research on that. The core topics won't change, but the shift to DEC and non-technical users is going to impact how we approach the JTBD articles and the narrative within them.

As a broad Q1 overview, there are some good signals. We have a good base established. The best articles so far have been the data engineering skills article and the data governance article. We're in the top five for quite a few searches related to data engineering, data silos, data pipeline development, and others. A breakdown of keywords is on the first page of Looker. Generally speaking, the average positions and impressions will give a good idea.

Anything else I could clarify or answer? All right, looks like we're good. We'll wait for your feedback on the Shadow ID article and take it forward from there.

**Cody Carmen:** Vivek, I dropped off a couple of comments on that yesterday. I think I tagged you, but we're pretty much good unless there's another update.

**Vivek Shankar:** Usually we work through Airtable, so just tag me there and I'll move it.

**Cody Carmen:** Cool, I can do that.

**Vivek Shankar:** Thanks, everyone. Good to see you guys.

**Mara Leighton:** Bye. Good to see you.
