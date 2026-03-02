# Deepgram <> Growth X - Weekly Sync

<metadata>
date: 2025-12-10
time: 18:00 UTC
duration: 27 minutes
organizer: Erik O'Brien
participants: Erik O'Brien, Troy Blanchard, Jose Francisco, Hasan Jilani, Will Ruzvidzo
fathom_recording_id: 107779000
fathom_url: https://fathom.video/calls/500944999
share_url: https://fathom.video/share/zzMR6y3qBFzhXkegnuHsuATNy5G85G6v
source: fathom
enriched_on: 2026-03-01 00:00 UTC
speaker_note: Participants list includes calendar invitees (many Deepgram employees and GrowthX staff), but only Erik O'Brien (GrowthX), Troy Blanchard, Jose Francisco, Hasan Jilani (all Deepgram), and Will Ruzvidzo (GrowthX) actively participated in the discussion.
</metadata>

---

## Summary

Deepgram and GrowthX reviewed early content performance metrics using Dream Data analytics, revealing strong initial growth in LLM traffic and organic search. The team committed to a content strategy pivot: doubling down on the high-performing "Voice AI API Evaluation" topic cluster with ~20 new comparison articles while pruning low-performing, off-topic content to improve site authority. Publishing quality issues from a recent CMS migration to Sanity were identified and assigned for resolution.

---

## Context

Deepgram and GrowthX partner on content marketing focused on voice AI APIs and speech-to-text solutions. Deepgram is evaluating content ROI across multiple channels (LLM traffic, organic search, console signups) to inform 2026 strategy. GrowthX leads content production and strategy; Deepgram owns analytics, quality review, and strategic decisions. This weekly sync aligns on metrics, publication quality, and content priorities.

---

## Relevance

**To GrowthX Delivery:**
- New Dream Data reports enable deeper analytics on content ROI (console signups, traffic by source) — methodology applicable to future content clients
- CMS migration risks: broken links, table rendering issues, formatting problems — document lessons learned for other clients migrating away from legacy systems
- Content quality audit and pruning workflow: systematic approach to site authority and algorithm signals worth replicating

**To CheckThat:**
- Deepgram prioritizing LLM visibility metrics (who appears in ChatGPT, Claude, etc.) — validates CheckThat's core value proposition for B2B SaaS
- Growth in "organic search" from 0 to ~100 sessions/week suggests LLM and traditional SEO are complementary, not competing channels

**To GrowthX Business Development:**
- Deepgram showing strong product engagement signals: 8 articles ready for review, active content backlog, systematic A/B testing of topic clusters
- Holiday schedule decisions pending (week of Dec 22) — may affect engagement cadence and project delivery

---

## Overview

- New Dream Data reports provide deeper analytics on content performance, showing strong early growth in LLM traffic and organic search.
- The high-performing "Voice AI API Evaluation" topic cluster will be expanded with \~20 new comparison articles to double down on bottom-funnel content.
- A CMS migration to Sanity caused publishing bugs (broken links, tables, formatting); Jose will fix them, starting with the "Deepgram vs. Google" article.
- Low-performing, off-topic content will be pruned to focus site authority and improve algorithm signals.

---

## Key Topics

### Content Performance & Analytics

  - New Dream Data reports provide deeper analytics on content performance, focusing on console signups.
  - **Early Performance (8 weeks):**
      - **Traffic:** \~14 visits/article (monthly average).
      - **Organic Search:** Growing from 0 to nearly 100 sessions/week.
  - **Top-Performing Articles:**
      - "Speech-to-text benchmarks"
      - "Whisper comparison"
  - **Strategic Rationale:** The company is prioritizing LLM traffic, which is now back on a growth trend after a flat period.

### Strategy: Double Down & Prune

  - **Double Down:** Expand the high-performing "Voice AI API Evaluation" topic cluster.
      - **Why:** It drives strong traffic and shows early conversion signals.
      - **Action:** \~20 new comparison topics added to Airtable backlog.
  - **Prune:** Remove low-performing, off-topic content (e.g., "AI consumes water").
      - **Why:** To focus site authority and improve algorithm signals.
      - **Action:** Troy approved pruning; Erik will manage.
  - **Refresh:** Update high-value articles (e.g., "best speech to text APIs") in the new year.
      - **Why:** To send fresh signals to LLMs and maintain relevance.

### Production & Quality Control

  - **Publishing Backlog:** 8 articles are ready for review.
  - **Airtable Status:** Jose needs to update the status of 4-5 published articles.
  - **CMS Migration Issues:** A recent migration from Datto to Sanity caused several bugs.
      - **Broken Links:** Appear as plain text in articles (e.g., "Deepgram vs. Google").
      - **Missing Tables:** Published as screenshots due to CMS limitations.
      - **Incorrect Formatting:** H2s appear as plain text.
      - **Missing Content:** The article "Choosing the best speech-to-text on-premise solution" is empty.

---

## Action Items

**Erik O'Brien (GrowthX)**
- Fix Dream Data SQL/SDR filters with Sam Lee; confirm conversion metric
- Prepare Dream Data channel report (LLM vs organic split) for next sync
- Bump Slack thread on language-page content/FAQ questions; schedule call with Patricia Mitter and engineer if needed
- Align next week on holiday schedule; decide whether to hold week-of-Dec-22 sync or pause

**Jose Francisco (Deepgram)**
- Update Airtable statuses for 8 published articles; mark as published
- Review 20 new Voice AI API topics in Airtable; suggest title tweaks
- Fix "Deepgram vs. Google" article: make URLs clickable hyperlinks, format H2s correctly, replace table screenshots with actual tables
- Fix other articles with table-screenshot issues
- Restore missing content on "Choosing the best speech-to-text on-premise solution"

**Hasan Jilani (Deepgram)**
- Review 20 new Voice AI API comparison topics in Airtable; suggest title tweaks
- Share new TTS (text-to-speech) topics list in GrowthX Slack channel
- Review Dec–Jan content list and send prioritized production order to Will Ruzvidzo

**Troy Blanchard (Deepgram)**
- Prune low-performing and off-topic articles from site; start with "AI consumes water"
- Align next week on holiday schedule; decide whether to hold week-of-Dec-22 sync or pause

---

## Transcript

**Erik O'Brien:** Hey, Troy.

**Troy Blanchard:** Hey, Erik. How's it going?

**Erik O'Brien:** Well, how's your week been?

**Troy Blanchard:** Oh, we are very much into our 2026 planning. And so, oh, Jose is in the call. Awesome. Hi, Jose. Yeah, so we are just trying to figure out how we are going to keep growing this business. And so, to that end, I'd really like to talk about what I'm seeing. We have this platform called Dream Data.io, if you've worked with it. And I've gone ahead. I know we have our analytics report, and that's all good. This gives us a little bit of a deeper dive into what the pattern is. Our sample size in terms of progress is still just eight weeks of published material, more or less. I'll go ahead and start sharing. What we're finding is I've created these reports in Dream Data that can really help us understand not just the traffic, but the signups, and these are all filtered for just the pages that you've created, and then we can see it grouped by landing page.

**Troy Blanchard:** This is a pages report, so I can really just see by the page, but I can filter by LLMs, organic search, and I can go all the way down to things like SQL. So if you were to look at actual conversions, there are 25. These are the visitor numbers. I'm not entirely sure the SQL count and SDR accepted metrics are correct. I'll need to go back and figure out why those filters aren't right. I'll talk to Sam about that.

**Troy Blanchard:** But this might be a little bit more accurate. From this page, we can see Enterprise, Voice, AI, Agents, and other companies that have played a role. If I look at companies that reached SQL accepted status, I get a better view. We can really dig down into the values and amounts here. Ultimately, I'm going to be primarily focused on console signups and trying to drive as many visitors as possible. So this is on a week-over-week basis. We want to be able to project what we can accomplish both from an organic search point of view and through our other channels as well.

**Troy Blanchard:** So really, I'm trying to look at this — it's a bit of a low sample size, but we need to see: if we publish X amount of articles, and we can see that "speech-to-text benchmarks" and "whisper comparison" are doing well, how does that content quantify in terms of sessions and conversions? How do we pace out how much we need to keep doing, and what type of content should we continue to build? If there's more we can put out on something that's doing well, it'll probably help us do even better. Right now, for each article we put out, we're seeing about 14 average site visits per article in the last month. From there, we need to understand: what does our output look like? How do we prioritize the content that's generating the most volume from both an SEO and LLM perspective?

**Troy Blanchard:** That's where I'm starting — figuring out how we take this and make it compound over time. On organic search, when we started, we had nothing, and now we're coming closer to 100 sessions a week. So we want to understand the growth rate, as certain articles get higher ranks over time. We need to understand what we're likely to contribute from both LLM and organic search channels. We're trying to put more science around what we're doing to guide us in the right direction. I'm not entirely clear on the Salesforce data filters, but the visitor data is solid. You can see that speech-to-text, ASR speech-to-text, and whisper versus deepgram comparisons are having the highest performance.

**Troy Blanchard:** This gives us more granularity to inform decision-making. It's definitely growing, and this is the hot topic. For next time, I'll do a channel report to show the split between LLMs and organic search. Even though the weekly volume isn't huge, we can say we're anticipating this level of growth from LLMs and qualified traffic, and hopefully we'll see conversions. It's the hottest topic with the sales reps — are we showing up when people search for "what is the best?" in prompts? We're looking at both LLM and SEO angles. Over time, as people come back and re-engage, we'll get a better sense of what's working. I'll clean up the filters for a better view. Ideally, we'll have better data-informed insights on what's really working and where people are spending the most time on site. We're in a good position to understand our performance, though we'll need a few more weeks outside the holidays. "Speech-to-text benchmarks" has barely been out 30 days, so in 90 days we can have realistic expectations. We should think about backlinking and optimization strategies too. The key is understanding what's working to the deepest level.

**Erik O'Brien:** Yeah, absolutely. The views we have on Looker are organized around the topic clusters we defined in the strategy. The "Voice AI API Evaluation" cohort is continuously performing well and growing over the last month. If you look at the URL cohorts, we can see which topic clusters are driving impressions and traffic, and then we can start looking at conversions. We got the update on the conversion events page. Based on what we're seeing as patterns, we decide where to double down. Will did keyword research and came up with about 20 new topics for that Voice AI API evaluation cluster, and we uploaded those into Airtable. If you go to the backlog grouped by cluster, you'll see them there. In that last cluster, that's where we added about 20 new ones.

**Troy Blanchard:** Got it. Oh, perfect. Yeah. No, this is perfect. Yeah, I think you're way ahead of us. This comparison is really going to be key. Awesome.

**Troy Blanchard:** Jose, you there, buddy?

**Jose Francisco:** Yeah, I'm here. There's eight blogs ready for review. I have four or five that are already published. I wish I could change the status on them myself, but right now I'm view only.

**Erik O'Brien:** Yeah, I just updated your permissions.

**Jose Francisco:** Awesome. Yeah, I'll update those. The first eight were the latest ones that needed updating. Four of them are already published, potentially five. One was scheduled for today — I'm not sure if it's out yet.

**Troy Blanchard:** And so we'll take a look through those topics. Does that work for you, Jose and Hasan, in terms of the new ones? Are there any title corrections or suggestions? Like, if we want "Deepgram vs. Azure" instead of something else — you guys know best how to position this without making enemies of our frenemies.

**Jose Francisco:** Yeah, I haven't published the Tortoise one yet, just in case we needed to talk about that today.

**Hasan Jilani:** The existing ones all look good. And I have some new TTS topics coming. I'll share a list in the GrowthX channel.

**Erik O'Brien:** Wonderful.

**Troy Blanchard:** Awesome. That's where we want to get to — here's why we're doing this, and here's the compounding growth we expect. I think we'll look for more places on the website to place these links and content to build more SEO strength. And then, Jose, thinking about the ones that work as potential video topics as well to have that content across multiple formats.

**Troy Blanchard:** I'm feeling pretty good about where we're moving as long as we keep the content production going. The numbers aren't the largest at this point, but we're definitely growing on LLMs again. From 2024 to 2025, LLM traffic grew 10X overall. This year it was looking a little flat, but now we're actually seeing growth again — it's early days, but we're back on the growth trend. We have a really strong story: we know what we're doing, we're analyzing the data, and we're seeing real growth. Obviously, SEO is super important too. As an AI company, we're focusing our investment on LLM searches, and so far, this is really doing well. I'm in the midst of our 2026 projection planning, so I'm pretty bogged down with that. But do we have anything else to review?

**Erik O'Brien:** Just a couple more things. Let me share my screen.

**Erik O'Brien:** Hasan, I know you were out last week, but I have some outstanding questions about those language pages. We got some questions from our engineer around content and FAQ sections. I tagged you in the Slack channel. If it's easier, I can schedule a call with you, Patricia, and the engineer to talk through it all.

**Hasan Jilani:** Yeah, I think so. If it's content-specific, I can answer it. But if it's CMS-related, Patricia can better answer that.

**Erik O'Brien:** Okay. I'll bump that to the top of your notifications and see what we can get answered asynchronously. If we need to, we'll schedule a call to dive deeper on open items.

**Hasan Jilani:** Yeah, that works.

**Erik O'Brien:** Wonderful. One of the articles that was posted last month, "Deepgram vs. Google," has a few issues we'd like to clean up on the publishing side. The URLs are showing up as plain text wrapped in parentheses instead of clickable hyperlinks.

**Jose Francisco:** Yes, that was an old bug that was recently fixed. I'll check that out today. Same thing with the tables — in three or four articles, I had to publish screenshots of the tables rather than the tables themselves because our CMS had issues. I did that as a quick shortcut to get the articles out, but I'll fix those today as well.

**Erik O'Brien:** And some of the H2s need to be formatted as H2s instead of plain text.

**Jose Francisco:** Yeah, and the table issue isn't just for "Deepgram vs. Google." There are a couple of others too. I'll fix those as well, but I'll prioritize the Deepgram vs. Google article now since you brought it up.

**Erik O'Brien:** Great. And I tagged you in another one — an article showing no content at all.

**Jose Francisco:** I apologize for that. We recently migrated to a different CMS. We were working with Datto, our old content management system, and migrated to Sanity. To be honest, Sanity isn't my favorite, and I'm not sure why we switched. That's why these bugs are coming up. We'll fix those right away. And thank you for keeping an eye on them. It means a lot that you're also checking quality after publication. I'll look at those and update the tables.

**Erik O'Brien:** Awesome. I appreciate it. During our quick audit of published articles, we found those issues, but I figured the migration might have caused them, so good to confirm.

**Erik O'Brien:** I know you have an in-depth view with Dream Data. Just to recap expectations — as we talked about last week, we added conversion events by URL cohorts to the Looker dashboard. Most of them are console signups, and we can see which specific landing page articles are driving those.

**Jose Francisco:** Really briefly — can you tell me the title of the article with no content again?

**Erik O'Brien:** "Choosing the best speech-to-text on-premise solution."

**Jose Francisco:** Got it.

**Erik O'Brien:** So those are most of our updates for today. We have updates to the Voice AI API topic cluster so we can prioritize pushing out bottom-funnel content that's working well for traffic and showing early conversion signs. We're tracking what's working, what's not, and doubling down on areas with growth.

**Will Ruzvidzo:** I have a quick question. A couple of weeks ago, Hasan approved a bunch of content for me to work on for December and January. Now that we've added these comparison article ideas to the backlog today, how do you want me to mix the content? Like two comparison articles a week plus other content, or vice versa?

**Hasan Jilani:** I'd have to look at the full list again. I think it was around 15 or so, right, Will?

**Will Ruzvidzo:** Yeah, it was like 18.

**Hasan Jilani:** I can look at the list and see if there's a specific order we want to do them in. That'd be my guidance.

**Will Ruzvidzo:** And what about the ratio? Like one or two comparison articles per week mixed with the 18 you already approved?

**Hasan Jilani:** Yeah, I think we can mix and match — do some comparison, do some of the other thought leadership content.

**Will Ruzvidzo:** Okay, sounds good.

**Erik O'Brien:** Cool. And then one topic we discussed weeks ago — we did a full audit of the site for refresh and pruning opportunities. Articles like "how AI consumes water" and others that are off-topic are dragging down crawlability and confusing Google about what Deepgram really stands for. We want to prioritize some refreshes based on which ones are driving the most marketing qualified leads — like the "best speech to text APIs" article, which was last touched in April or May. As we continue to optimize for bottom-funnel content that LLMs prefer, articles like that are seeing more LLM traffic. And freshness leads to more LLM pickups.

**Troy Blanchard:** I'm fine with pruning them unless Jose or Hasan has an issue. The "AI water" article got a spike in traffic, then disappeared. I agree with you, Erik. We need to ensure the website doesn't have unrelated content that throws off the algorithm. We want to reduce that level of content and produce more of what's working.

**Jose Francisco:** The "AI water" article spiked because Hank Green, this big YouTuber, spoke about AI and water. And there were a couple of podcasts that mentioned it too, so it was being Googled heavily.

**Troy Blanchard:** Yeah, the algorithm is getting more sensitive. I think we can go ahead with pruning. I'll take that on.

**Erik O'Brien:** Cool. As far as refreshes, we can work those in when we get into the new year to send fresh signals for content that's already performing well.

**Troy Blanchard:** Yes, absolutely.

**Erik O'Brien:** Anything else top of mind? Any questions?

**Troy Blanchard:** No, I think we're doing good. I like it.

**Erik O'Brien:** Awesome. We'll check in next week and see what your holiday schedule looks like. We'll be around the week of December 22nd, but the week after is usually quiet for the company. We can align on whether to move our meeting earlier in that week or take a couple weeks off. We'll chat through that next week.

**Troy Blanchard:** Sounds good. We'll talk about that. All good.

**Erik O'Brien:** Wonderful. All right, team. Really appreciate it. Chat next week.

**Will Ruzvidzo:** Bye, y'all.
