# Goodcall <> GrowthX Weekly Sync

<metadata>
date: 2025-04-03
time: 17:02 UTC
duration: 35 minutes
organizer: Prateek Gupta (GrowthX)
participants: Kyle Gaudreau (GrowthX), Prateek Gupta (GrowthX), Bob Summers (GoodCall), Daniel Lannon (GoodCall)
fathom_recording_id: 55396861
fathom_url: https://fathom.video/calls/266914836
share_url: https://fathom.video/share/TzgiK2mBrge19z34JfjZ7Kkmy_RRtzBC
source: fathom
enriched_on: 2026-03-04 20:35 UTC
</metadata>

---

## Summary

GrowthX and GoodCall reviewed strong content performance gains — clicks jumped from 140 to 200 daily — and aligned on a strategy shift toward comprehensive internal linking via tagging systems within Webflow. The team prioritized keyword-level reporting via Google Search Console (moving away from unreliable SEMrush data) and committed to doubling down on the BPO call center content cluster from 25 topics toward 50, with Daniel building out the "related articles" CMS widget and Prateek developing the tagging structure to support automated interlinking across categories.

---

## Context

GoodCall is an AI-powered business software platform that GrowthX is serving as their SEO content partner. GrowthX built out a content publishing system (178 articles published, 150 indexed) focused on vertical content clusters — starting with BPO call center operations, answering services, salon management, and appointment scheduling software. This is the weekly sync to track SEO progress, troubleshoot technical issues, and align on strategy direction. The relationship is 4+ months in, and the team is shifting from a reporting-heavy cadence to a blocker-focused format while also building better internal tools for measurement (moving away from SEMrush toward Google Search Console + custom Looker Studio dashboards).

---

## Relevance

**To GrowthX Delivery:**
- Internal linking strategy (tagging + auto-linking) is becoming a core differentiator in content delivery — replicable across other clients
- Built internal dashboard/reporting framework using GA4 + GSC + Looker Studio to replace vendor tools (SEMrush unreliability is a wider industry challenge)
- Monthly keyword performance analysis + topic cluster reporting — shift from keyword tier lists to query-level attribution

**To GrowthX Business Development:**
- GoodCall account showing strong retention signals — team moving from skeptical to collaborative on methodology
- Client request for better measurement (keyword attribution, velocity tracking) demonstrates maturity and intent to invest longer-term
- Strong case study potential: 43% click increase in 4 months on organic-only, no paid, minimal brand signals

**To GrowthX Scaling:**
- Topic cluster / tagging approach scales to other verticals and clients — the "BPO call center model" is replicable
- Google's keyword privacy restrictions (70% of GSC data hidden) is forcing GrowthX toward smarter measurement — opportunity to build proprietary reporting tools

---

## Overview

- Content performance jumped to 200+ daily clicks (from 140) — 43% increase
- BPO call center cluster at 25 topics; doubling down to target 50+ topics for the next 1-2 weeks
- Implementing category-based internal linking: tagging system (Salon, Answering Services, BPO Call Center, Appointment Scheduling) with auto-related articles at bottom of each post
- Shifting meeting cadence from status-heavy to blocker-focused; pre-meeting Slack updates for keyword highlights + performance metrics
- Indexing pipeline: 150 of 178 articles indexed; manually submitting 10 articles/day to Google Search Console to accelerate indexing

---

## Key Topics

### Content Performance and Measurement Shift

- Clicks increased from 140 to 200 daily (43% gain)
- SEMrush showing fake "tank" — unreliable for GoodCall's use case
- Google Search Console is ground truth; keyword-level data still blocked by privacy (70% of queries not shown)
- Strategy: Build custom dashboard in Looker Studio using GA4 + GSC + topic cluster mappings
- New reporting approach: keyword analysis showing top 10 ranking opportunities + velocity indicators (up/down rank movement)

### Content Expansion and BPO Focus

- Current: 25 topics in BPO call center cluster; plan to expand to 50+ in next 1-2 weeks
- 178 articles published total; 150 currently indexed
- Recent category adds: Salon (6-7 clicks, 200K+ impressions), Answering Services (16 clicks, rising), Appointment Scheduling
- BPO cluster generating highest traffic: 45+ clicks last week, multiple articles on answering services driving impressions

### Internal Linking Architecture

- New CMS widget: "Related Articles" section at bottom of each post
- Multi-level tagging: category tags (e.g., Salon, BPO Call Center) + topic tags
- 5-10 related links per page, styled consistently; can expand to 50-100 articles per category via index pages
- Daniel building the CMS structure; Prateek developing the tag schema

### Indexing and Search Console Submission

- Manual submission workflow: 10 articles/day via Search Console
- 150 of 178 articles now indexed; some new URLs awaiting Google re-crawl after CMS migration
- Recent URL structure change causing temporary indexing lag; expected to resolve as Google recrawls

---

## Action Items

**Prateek Gupta (GrowthX)**
- Prepare keyword analysis for next report: focus on new clusters entering top 10, highlight standout keywords & their traffic impact (CTR, impressions, position velocity)
- Develop tagging system for articles to support new interlinking feature: create category tags (Salon, Answering Services, BPO Call Center, Appointment Scheduling) + topic tags
- Reach out to Daniel Lannon for assistance with publishing BPO call center articles and creating new category in Webflow CMS
- Add "Published vs Indexed" column to weekly reporting dashboard for next sync

**Daniel Lannon (GoodCall)**
- Implement "related articles" section in Webflow CMS with tagging system for auto-linking: include bottom nav with multiple groupings (e.g., 5-10 links per category), style consistently with site design

---

## Transcript

**Kyle Gaudreau:** Thanks for the update on automated ingestion, really appreciate that.

**Bob Summers:** That's an important piece which we think a lot of customers would want. You guys agree — use us as the guinea pigs because we want to move as fast as we can and help you guys push it too.

**Kyle Gaudreau:** Love it, awesome.

**Bob Summers:** So where are we at? I love that there's only one note-taker now instead of the 3-to-1 or 4-to-1 ratio of AI to humans we had before.

**Prateek Gupta:** Hey Bob, hey Danny. So in terms of the last week, we had this content missing error where content wasn't displaying even though it's in Webflow CMS. Danny, did you have a chance to look into it?

**Daniel Lannon:** Yeah, let's fix that.

**Prateek Gupta:** Okay. So in terms of content updates, we're doing 25 articles a week and we've introduced a new category: BPO call center. Overall, we have 178 articles, 150 currently indexed. The 25 new articles will be uploaded today, then we'll start generating content for them and have them published by next week.

**Bob Summers:** When you say they're published, does that also mean they've been indexed, or are they just sitting on the web?

**Prateek Gupta:** No, they're just being published initially. They have not been indexed. So what we do is manually submit articles to Google Search Console. You can submit about 10 articles per day max.

**Bob Summers:** I've written a script that does this — you can submit 11 but on the 12th one you get an error.

**Kyle Gaudreau:** It used to be possible through the API back in the day, but I think Google killed that.

**Prateek Gupta:** Yeah. So I check each article's indexing status and keep updating. Some recent articles haven't been indexed yet because we changed the URLs recently.

**Bob Summers:** So on the status side, I think a very useful cadence for us is: how many are published, how many are indexed. When I'm thinking about content, there's creation, there's publishing, and then there's indexing. Once it's indexed, I feel like the first phase is done and we're monitoring performance.

**Prateek Gupta:** Exactly. So I'll add a "Published vs Indexed" column to next week's report. I'll update it in the Slack channel automatically.

**Kyle Gaudreau:** We're also working on automating more of this. We're building a dashboard in Looker Studio to give us better visibility into the funnel. We should also be asking: are we seeing velocity change? Hopefully positive, but if it goes negative, we need to understand why.

**Bob Summers:** Thanks for clarifying. Individual page submissions seem to work better than sitemap refreshes — Google takes page submissions more seriously.

**Prateek Gupta:** Right. So looking at the actual data, right now we're generating 45 clicks from the BPO category, and answering services is generating 70 clicks weekly. Salon articles are generating 6-7 clicks and about 200K impressions. These numbers will keep improving.

**Bob Summers:** You've done a great job focusing impact and performance. I'd love to see which keywords are mapping and how they're trending. Where do we rank, what's the velocity? I'd love to see keyword analysis — what keywords are we getting that we weren't before, and what's their trajectory?

**Prateek Gupta:** The problem is SEMrush data is unreliable. It's showing a fake "tank" in traffic that doesn't match reality. I've been using SEMrush for 10 years, but as of today it's the most unreliable tool.

**Bob Summers:** Kyle, you remember four or five weeks ago I was freaking out? You showed me that traffic quality was actually going up. Once you showed me the real data, I got it. SEMrush used to be reliable.

**Kyle Gaudreau:** It's still got challenges. There's an interesting SEO industry problem here. Historically, I'd do heavy keyword reporting and tier them. But as Google's approach to topics got more complex, I've shifted to topic cluster reporting. We can look at query data from Google Search Console. We actually have a technical SEO person now who was running ClickUp's SEO program. He's shown us we need to be mindful of how data is sampled and filtered. You can export to BigQuery to get better data.

**Kyle Gaudreau:** The core problem is that Google's keyword privacy (70% of keywords removed) and GSC's sampling make this harder than it should be. But we can look at queries, average positions, relative quality, and roll up by topic clusters.

**Bob Summers:** Some of this is that we as a team want to know we're making material impact. Marcel showed us SEMrush numbers a year and a half ago. But as you point out, that data is crappy. The CMS move has been huge. I think we're seeing benefits, but we should track keywords driving traffic and their ranking velocity. That shouldn't be too hard — it takes an intentional view.

**Kyle Gaudreau:** By the way, we're working on reporting in Looker Studio. I met with Jason today to review some proposals. There's a gap in the market for better tools. We'll focus on using GA4, GSC, and our data in smarter ways over the next month.

**Bob Summers:** I'd like to see keyword analysis. Which keywords are entering the top 10 this week as a result of our work? Maybe what we do is just highlight some standout keywords from a keyword perspective in a Slack channel.

**Kyle Gaudreau:** I love that. Just map shots and insights.

**Bob Summers:** Yeah. And honestly, this meeting should be mostly about: what's blocking us, what do we need to unblock? The status can come ahead of time. I'd love to read that stuff before the meeting so we can just focus on problems.

**Prateek Gupta:** Got it. I'll do the page analysis plus keyword analysis. The issue is Google Search Console filters out lots of keywords for privacy. Almost 70% of keywords are removed. If I could see all the clicks at keyword level, I'd know which keyword ranked at which position and got which clicks. That would help me identify what's working.

**Kyle Gaudreau:** That's a huge pain point with early-stage accounts. You see aggregate clicks but when you drill into queries, nothing has clicks associated with it. This used to be available in GA, then they encrypted it. You went to GSC, and now GSC has sampling limits too.

**Bob Summers:** Yeah. I expect 100% attribution from organic clicks, but it's not coming through.

**Bob Summers:** In terms of content generation, where are we at next? I think we should continue doubling down on the BPO call center space. It's an incredibly important cluster and we're barely scratching the surface.

**Prateek Gupta:** Right. We have 25 topics on BPO call center now. The idea is to go to 50 more topics. Let me just give one example: we had 47 clicks between March 23-29 for one post, but when I look at keyword level, it only shows 4 clicks. That's the gap.

**Bob Summers:** I have a few friends in that space. If I run into them, I'll try to get some insight. Expectations are low that this moves quickly, but let me try.

**Bob Summers:** Great progress, by the way. The CMS move has been huge. I think we're seeing some real traction.

**Prateek Gupta:** Yeah. Everything's bearing fruit and not everything is even indexed yet, so we're just at the early stage. But I needed to ask: could we add related articles sections to each page? For example, all appointment scheduling software articles could appear at the conclusion of each post. We moved to CMS so we could add these kinds of widgets.

**Daniel Lannon:** Yeah, that's like an index. It's not difficult, easy to do. Just let me know how you want me to style it.

**Prateek Gupta:** We have an existing format, Danny.

**Bob Summers:** Don't we have something already at the bottom, like related articles or something? I thought we were looking at interlinking.

**Daniel Lannon:** I had something and we've gone through iterations but I'm not sure if we ever used it.

**Bob Summers:** How many things do you want to link from each page? All of them?

**Prateek Gupta:** Maybe 5-10, like a standard related articles section.

**Bob Summers:** We have that in business applications — related or top 10. I don't think it matters where on the page, we just need linking to other pages. Right now these are small documents, so we need interlinking. Maybe at the bottom for consistency. We're creating relationships inside our network.

**Bob Summers:** What do you think about the interlinking strategy? Should we add a module that links to the same 10?

**Prateek Gupta:** I'm looking at two tactics. One is an article, and one is an HTML index page. Like we have "Business Productivity AI" where it links out to all the articles we created. Same way, we could have one for Answering Services, Salon, and BPO Call Center.

**Bob Summers:** I'd rather do this at the start. This is the most important part of our meeting. If we need to change how content is created, that's more helpful than reviewing data. So Danny, the main list is easy — we've done that many times. So that would be full index pages of all articles, right? Then we need some strategy on rotating or related articles. You'd want some kind of tag system.

**Bob Summers:** If you set up a tag structure, then Prateek can tag articles and it would auto-link inside the side nav. That's probably the way to do it. You tag the articles and it pulls them.

**Prateek Gupta:** Let me share an example. We did this for a client. For "USA Visa Photo Requirements," all related articles are tagged. So we can do two levels of tagging: one is category (Salon, Answering Services) and then topic tags. Then "Related Posts for Answering Services" shows all answering services articles, and then salon-related articles.

**Bob Summers:** So our internal linking will be robust. I see why bottom nav is super valuable — you're adding multiple grouping types. Let's go with that. It makes more sense at the bottom because we might add more groupings. The styling is yours — we know how to style it. You're adding multiple groups, and those groups are sets of tags within the cluster.

**Prateek Gupta:** We can also create index pages by category. That way we can add 50-100 links per category instead of just 5-10 at the bottom.

**Daniel Lannon:** We have a search with tags but we'll figure something out.

**Prateek Gupta:** Exactly. This works perfectly.

**Prateek Gupta:** Next time, with any tech fixes, I'll discuss them first, then we'll jump into the numbers.

**Daniel Lannon:** Yeah, they come up even beforehand during the week, so I can knock them out pretty quickly.

**Prateek Gupta:** Perfect. I'll need help publishing BPO call center articles and creating new categories in CMS, so I'll reach out.

**Daniel Lannon:** Sounds good.

**Bob Summers:** Thanks, guys. See you. Bye.
