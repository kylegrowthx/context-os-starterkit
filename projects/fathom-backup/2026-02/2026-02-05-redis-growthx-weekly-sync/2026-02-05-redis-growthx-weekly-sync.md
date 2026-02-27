# Redis <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-05
time: 17:29 UTC
duration: 33 minutes
organizer: team@growthxlabs.com
participants: Erik O'Brien (GrowthX), Alexis Ruiz-Pedregon (Redis), Reet Mand (Redis), Megan Boone (Redis), Rebekah Reddis (Redis), Fung-Lin Wu (Redis), Andy Varshneya (Redis), Allison Gregory (Redis), Claudia Di Martino (Redis), Regine Carreras (Redis)
fathom_recording_id: 120115074
fathom_url: https://fathom.video/calls/556077761
share_url: https://fathom.video/share/RrKfH8VbeoHfQoyeYHKcJQTKrc8ustrc
source: fathom
enriched_on: 2026-02-27T00:00:00Z
</metadata>

---

## Summary

GrowthX reported strong January results (18 articles, 1.7k+ sessions, 43 LLM referrals, 2 trial signups) and moved to an auto-publish workflow without PMM review, shifting focus toward hand-raiser conversions. Redis's AI visibility in LLM prompts reached 50% (up from 42%), with new tracking planned for Google Memory Store and access granted to GrowthX's proprietary competitor-to-Profound tool.

---

## Context

This weekly sync between Redis's product marketing team (Alexis Ruiz-Pedregon, Reet Mand, Fung-Lin Wu) and GrowthX's head of content (Erik O'Brien) focused on month-one performance and operational improvements. GrowthX's content is now a primary driver of organic traffic and AI visibility for Redis—18 published articles generated 1.7k+ sessions and moved Redis to #1 visibility among vector database competitors in tracked LLM prompts. The team discussed workflow bottlenecks (PMM review latency) and surface-level signals (2 trial signups, but 0 hand-raiser conversions), setting February goals around 3,000 sessions and deeper analysis of decision-maker lead drivers. A new vendor-agnostic AI tracking tool launched today, offering 100k+ historical prompts instead of starting fresh with Profound or Scrunch.

---

## Relevance

- **Content Performance:** 7.8x week-over-week session growth validates topic selection and distribution; LLM traffic (43 referrals, ~70 tracked prompts) shows early ranking momentum.
- **Workflow Efficiency:** Auto-publish model removes PMM review bottleneck; weekly Slack summaries maintain visibility. Exception: Jim T. continues reviewing "vs." articles for accuracy.
- **Conversion Priority:** Hand raisers (decision makers) are primary goal; free trial signups (developers) secondary. Reverse-engineering hand-raiser content is now urgent.
- **AI Visibility & Tooling:** Redis at 50% visibility ahead of Pinecone and Weaviate; new GrowthX tool provides historical depth without retraining.
- **Regional & Topic Insights:** 83% US/APAC traffic aligns with paid channels. Industry Solutions cluster shows highest engagement; Agent cluster above-average despite nascent content.

---

## Overview

- **New Workflow:** GrowthX will auto-publish articles without PMM review. A weekly Slack summary will be sent for PMM visibility.
- **January Performance:** Strong start with 18 articles published, 1.7k+ sessions, and 43 LLM referrals. Two Free Cloud Trial signups occurred, a positive signal for month two.
- **Conversion Priority:** The primary goal is "Hand Raisers" (decision-maker leads), not "Free Cloud Trials" (developer signups). GrowthX will analyze past content to reverse-engineer Hand Raiser drivers.
- **AI Visibility:** Redis leads competitors (Pinecone, Weaviate) with 50% visibility in tracked LLM prompts, up from 42%. Google Memory Store will be added to tracking.

---

## Key Topics

### January Performance Review

  - **Content Output:** 18 articles published, 1.7k+ sessions, 43 LLM referrals.
  - **Traffic Growth:** Sessions grew 7.8x from week 2 (122) to week 4 (953).
  - **Regional Traffic:** 83% from US, Singapore, China, India, Canada.
      - This aligns with paid traffic data, validating the content's reach.
  - **Topic Cluster Performance:**
      - **LLM Optimization & App Speed:** Dominant (53% of traffic).
      - **Vector Database & RAG:** Tied for \#2 (14% each).
      - **Industry Solutions:** Highest engagement rate → signals value of vertical-specific content.
      - **Agent:** Above-average engagement → supports Redis's strategic shift from cache to AI agent infrastructure.
  - **Conversions:**
      - **Free Cloud Trials:** 2 signups from technical LLM content.
      - **Hand Raisers:** 0 signups.

### New Content Workflow

  - **Publishing Process:** GrowthX will auto-publish articles without PMM review.
      - **Exception:** Jim T. will continue to review "competitor vs." articles.
  - **PMM Visibility:** GrowthX will send a weekly Slack summary with links to all published articles.
  - **Performance Review Trigger:** GrowthX will flag articles reaching 150 views in one week for a thorough PMM review.
  - **Table Formatting:** GrowthX will ensure correct table formatting in Sanity, as simple copy-paste fails.
      - An engineering ticket is open to improve the native table component.

### PMM-Requested Content

  - **New Priority Blog:** A draft on a new Redis 8.6 feature will be prioritized over a previous request from Jim T.
  - **Author Assignment:** Alexis will provide a list of authors for each topic cluster to ensure consistency.

### AI Visibility & Tooling

  - **AI Visibility:** Redis leads competitors with 50% visibility in tracked LLM prompts (up from 42%).
  - **Competitor Tracking:** Google Memory Store will be added to the tracking list.
  - **New Tool Launch:** GrowthX is launching a competitor to Scrunch/Profound.
      - **Benefit:** Provides access to a historical library of 100k+ prompts, eliminating the need to start tracking from scratch.
      - **Access:** Redis team will receive direct access.

---

## Action Items

**Erik O’Brien (GrowthX)**
- Prioritize Jim’s Redis 8.6 blog; publish next week
- Slack Alexis weekly published-article links
- Ensure tables in blog posts render correctly in Sanity
- Monitor article views; ping Alexis/Reet at 150/wk for PMM review
- Remind Gabby of new publish-without-review process
- Update today’s articles to publish-without-review
- Add total rows to LLM referral tables in Looker
- Grant Reet Looker access; Slack dashboard link
- Analyze hand-raiser content; propose ideas to Alexis/Reet
- Add MemoryStore and ElastiCache to AI visibility tracking
- Schedule AI visibility tool demo w/ Alexis & Reet
- Share Jan performance deck in Marketing Private Slack

**Alexis Ruiz-Pedregon (Redis)**
- Confirm w/ Jim T review for vs articles; then inform Erik
- Slack Erik topic-cluster author assignments

---

## Transcript

**Alexis Ruiz:** Sorry about that. Got stuck in another meeting.

**Erik O'Brien:** No worries, I figured that much.

**Alexis Ruiz:** How are you? Good so far. Reet might join. Fung-Lin will be unable to join today, but I have a few things for you.

**Erik O'Brien:** Do you want to start?

**Alexis Ruiz:** Sure. First, Jim suggested another blog topic for us. I wanted to see what the process is since you have slated blogs weekly. This one's already drafted—a simple "what is" piece. What are your thoughts on handling PMM requests?

**Erik O'Brien:** Feel free to send them over. You can easily fit them into the schedule and prioritize since it's something they're interested in.

**Alexis Ruiz:** This one should actually be priority. It's about a new Redis 8.6 feature launching.

**Erik O'Brien:** Okay, we can do that next week then. I'll send it over via Slack.

**Alexis Ruiz:** So for articles moving forward, Fung-Lin said we can move forward with publishing without PMM review. But can you Slack us once a week with the articles published? Links too, so we can forward to the PMM team for visibility.

**Erik O'Brien:** Wonderful news. We're good to go.

**Alexis Ruiz:** Great. One more thing—make sure table formatting is correct. I don't have Sanity access, so I'm not sure how it works backend, but copy-paste doesn't seem to work.

**Erik O'Brien:** Right. Sanity doesn't auto-format tables. I shared the standard table component used across other blogs. I had a ticket out to engineering to see if we can update it to look friendlier. They're inundated with a product launch, but hopefully we'll get clarity in a week.

**Alexis Ruiz:** Thanks for checking on that. One last thing: when an article reaches 150 views in a week, can you ping us? That's when we'll have PMM do a thorough review.

**Erik O'Brien:** Absolutely. For the blogs I sent today, we're skipping PMM review.

**Alexis Ruiz:** Actually, I need to double-check with Fung-Lin. But we still might want Jim Tessier to review the "vs." competitor articles. He has the bandwidth.

**Erik O'Brien:** That works. I'm taking notes to remind Gabby of the new process.

**Alexis Ruiz:** Last thing: do you need authors for each topic cluster?

**Erik O'Brien:** It'd be great to have it in writing.

**Alexis Ruiz:** I'll send that via Slack after this.

**Erik O'Brien:** We published six articles this week—good momentum. But mainly I wanted to review January 26 performance. We got 18 articles published, over 1.7k sessions, 43 LLM referrals, and two Free Cloud Trial signups. This is great, especially this early. Usually, we don't see conversions until month three or four.

**Reet Mand:** What are LLM referrals exactly? Can you walk me through that?

**Erik O'Brien:** In our Looker dashboard, we track specific referrals from LLMs. Most referrals come from Google—over 80%. But LLM referral rate is typically 1-2% of total traffic. We track specifically if our content is cited in LLM chats and which platform it's coming from, so we can see which landing page was referred from which platform.

**Reet Mand:** This is tracked in Google Analytics too, but this is a summary view. If I'm looking at this dashboard, it says 17 sessions. Sessions are visits?

**Alexis Ruiz:** Visits, yes.

**Erik O'Brien:** And 8 engaged sessions—either 10 seconds on page or a scroll.

**Reet Mand:** This 16,000% increase—is that monthly or yearly?

**Erik O'Brien:** This is just January. We probably had six articles in December, so this is siloed to content we produce.

**Alexis Ruiz:** Right, just content GrowthX has produced for Redis. We've had lots of traffic from LLMs generally.

**Reet Mand:** Perfect. When you do your monthly review, Erik, could you also show what percent of sessions come from GrowthX content over time?

**Erik O'Brien:** Absolutely. Given compounding content efforts, I set a goal to hit over 100 sessions next month—doubling it. As we produce more, it compounds. Hopefully we continue getting picked up by LLM traffic. Quick ask: can you add a total row at the bottom of these tables so we easily see total numbers?

**Alexis Ruiz:** Sure. So we can easily see the 100 sessions from LLMs.

**Reet Mand:** Can you ping me this dashboard?

**Alexis Ruiz:** Yes, let me share it now. Actually, Erik, can you give Reet access? I don't see she has it.

**Erik O'Brien:** Absolutely. What's your email?

**Reet Mand:** Reet.mand at Redis.com.

**Erik O'Brien:** Got it.

**Reet Mand:** This is a really great dashboard, by the way. One of the cleaner reports I've seen.

**Erik O'Brien:** We simplified all the noise from Google Analytics to pull down what we want to track.

**Erik O'Brien:** So 20 articles delivered last month, 18 published. We're almost at parity—one delivered, one published. With reduced PMM review, we'll get more published. We'll try to get through the backlog to over 20 this month.

**Erik O'Brien:** Overall sessions: 7.8x growth from week 2 (122) to week 4 (953). Great momentum. This first week doesn't count—half week, holiday week, little content. We've already passed 1,000 sessions this week and it's only Thursday.

**Erik O'Brien:** Regional breakout: 67 countries reached, 83% from US, Singapore, China, India, Canada. About even split between Americas and APAC, with EMEA at 7%.

**Alexis Ruiz:** This aligns well with our paid traffic.

**Reet Mand:** Surprised to see Singapore.

**Alexis Ruiz:** We've been seeing lots of Singapore traffic from paid too. This is pretty aligned with paid.

**Erik O'Brien:** Overall cluster performance: LLM Optimization & App Speed dominates with 53% of traffic, almost 1,000 sessions. Average engagement across all clusters is 34%. Vector Database at number two with 14% traffic and huge growth. We published quite a bit in that cluster. It's more top-of-funnel fundamentals, so we expect lower engagement. We'll continue tracking and see if it improves. RAG Architecture tied at 14%, 235 sessions, a bit below average engagement but resonating with technical audiences. As RAG and agent spaces evolve, we'll expand content there. Industry Solutions shows highest engagement rate—signals vertical-specific content is valuable. We have a couple Industry Solutions articles this week. Agent content performs above average. We've published lots of agent content recently and want to keep expanding as Redis shifts from cache-only to AI agent infrastructure perception.

**Erik O'Brien:** Two trial signups is great this early. Usually month three or four. These came from technical implementation-focused LLM content—"Single vs. Multi-Agent Systems." Great signals. Larger question: we track about 5-6 conversion events in GA4. Do you track conversion events other ways or use other tools for attribution?

**Alexis Ruiz:** Mostly GA4, especially for web traffic and organic/paid. We have Salesforce, but that's for Free Cloud Trials or Hand Raisers already captured. Really, we go off GA4 data.

**Erik O'Brien:** It's the most accurate we've seen.

**Erik O'Brien:** Of these conversion events, which would you like to prioritize as most valuable?

**Alexis Ruiz:** Hand Raisers—that's actual users filling out a form to book a meeting. That's the ultimate goal. Free Cloud Trial Signups are second because it's easier entry. We do see lots of free trial signups because of lower barrier.

**Erik O'Brien:** Good to know.

**Reet Mand:** My question too. Do we have the ability to track hand-raiser quality?

**Alexis Ruiz:** Yes, we can track hand raisers and GA4 does. We work closely with Outshine to keep those events updated.

**Reet Mand:** So we just haven't had any hand raisers yet.

**Alexis Ruiz:** Exactly. We're seeing free trials first because they have lower barriers, like in paid campaigns.

**Reet Mand:** Erik, in your experience with other clients, do you think LLM traffic really converts better?

**Erik O'Brien:** True for the most part. It's not one-to-one, but if there's a free option, we see consistent conversion from engagement. Engagement rates are higher from LLM traffic—conversion is about 5-6X higher on LLM traffic with engaged sessions. We're tracking this across clients to get actual market numbers. For Redis, we have early signals. We got two trial signups in month two. In February, we hope to double or triple. If so, we're on the right track. I'll analyze content to identify hand-raiser drivers and reverse-engineer new ideas that lead to sales conversations.

**Alexis Ruiz:** That would be great. We've been discussing this internally. Free trial signups target practitioners and developers. Hand raisers target decision makers—the ones converting with Redis. Maybe content should be split that way: practitioner vs. decision maker?

**Erik O'Brien:** Industry Solutions is probably our closest decision maker content. I'll go through all your content and specifically look at hand raisers, see what blog or editorial content leads to more hand raisers than average.

**Reet Mand:** Our number one goal is hand raisers. Number two is free trial signups.

**Erik O'Brien:** AI visibility growth: 42% to over 50%. For 483 prompts tracked (about 70 per day), Redis shows up 50% of the time—number one ahead of Pinecone and Weaviate. We're seeing steady growth as we publish. Content is being cited. For prompts we're tracking, this mirrors your Profound data. When Cody was here, he gave me Profound access. I took those prompts and uploaded them here for parity.

**Alexis Ruiz:** Do we track Valkey, ElastiCache, Google Memory Store as competitors? I see Valkey, ElastiCache.

**Erik O'Brien:** Memory Store—I'll add those.

**Alexis Ruiz:** Google Memory Store is a main competitor after ElastiCache. They're naming us right there.

**Erik O'Brien:** I know you use Profound, which competes with Scrunch. Are these the same prompts?

**Alexis Ruiz:** Same prompts, yes.

**Erik O'Brien:** We're launching a competitor to Scrunch and Profound. You don't set it up from scratch. It looks at entire categories of buyer queries and sorts them. Redis is in multiple categories, database management systems mostly. This competitor view mirrors what you'll see in Scrunch. For prompts, we have over 100k prompts tracked since November. If you want new prompts from the shared library, you add them and get all historical data instead of starting from scratch. I'll do a deeper demo today—it's launch day, so expect bugs.

**Alexis Ruiz:** We'll get access too?

**Erik O'Brien:** You'll have direct access. No more screenshot reports.

**Reet Mand:** This is a really great update, really good progress, Erik. Thanks. Let's add this to Marketing Private channel.

**Alexis Ruiz:** Yes, definitely. Erik, can you share the deck?

**Erik O'Brien:** It's in the monthly report. Google Slides. I'll share it.

**Alexis Ruiz:** Can you Slack me the link after our call too?

**Erik O'Brien:** Absolutely. We'll also set some content goals. Try to hit 3,000 sessions—2x January. Drive trial conversions with better CTAs. Double LLM referral traffic as content compounds. Maintain steady state elsewhere with slight growth. Competitive AI visibility presence. Engagement at 34% or improve.

**Reet Mand:** Sounds good.

**Erik O'Brien:** Thanks for the time. I'll share links via Slack for easy access. Let me know if questions come up.

**Alexis Ruiz:** Thank you so much. I'm on the slide deck already.

**Erik O'Brien:** Thanks, team. Bye.
