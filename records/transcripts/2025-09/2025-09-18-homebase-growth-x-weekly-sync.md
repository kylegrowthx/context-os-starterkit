# Homebase <> Growth X - Weekly Sync

<metadata>
date: 2025-09-18
time: 14:00 UTC
duration: 29 minutes
organizer: team@growthxlabs.com
participants: Jakub Rudnik (GrowthX), Matthew Alves-Hill (GrowthX), Sonia Urlando (Homebase)
fathom_recording_id: 88171272
fathom_url: https://fathom.video/calls/413513545
share_url: https://fathom.video/share/7QEUaxjYxwnn8dbqmSu8mvJfYj-kz54q
source: fathom
enriched_on: 2026-03-03 14:30 UTC
</metadata>

---

## Summary

GrowthX introduced Matthew Alves-Hill as Homebase's new managing editor, bringing Atlas workflow expertise and strategy sprint best practices to improve content quality. The team prioritized fixing input quality issues in TLDR and "How to Start a Business" content through new agentic pipelines in Atlas, conducting glossary quality reviews post-platform migration, and building out reporting in Looker to track content performance with metrics for individual URLs, keyword position movements, and internal linking data. Homebase committed to content refresh workflows while GrowthX identified key capability gaps in research process control and editorial oversight that the agentic pipeline would help address.

---

## Context

Homebase is a GrowthX content marketing client operating in the business/payroll/HR space. This is a weekly operational sync following Homebase's recent migration to Atlas, GrowthX's proprietary content generation platform. Matthew Alves-Hill, who previously led onboarding and strategy sprints for new clients at GrowthX, is transitioning into the role of managing editor for Homebase's account — a hands-on position overseeing content quality, artifact optimization, and workflow configuration. The relationship involves continuous improvement of Atlas outputs through better input curation and new agentic pipeline capabilities that provide finer control over research quality.

---

## Relevance

**To GrowthX Delivery:**
- New agentic pipelines in Atlas enabling tighter research control and editorial intervention — applicable across Homebase and other GrowthX clients in regulated/quality-sensitive verticals (legal, medical, financial services)
- Managing editor embedded in account operations improving iterative workflow optimization and client confidence in content process quality
- Content refresh infrastructure and triggers (6-12 month glossary refresh cycles, keyword position monitoring, orphan page detection) can be replicated across other accounts

**To GrowthX Business Development:**
- Homebase account showing strong glossary performance providing proof of concept for scaled programmatic content — foundation for future expansion and upsell opportunity
- Input quality focus and collaborative review processes signal mature client relationship with clear operational framework
- Quality improvements and reporting transparency building case study potential for CheckThat AI visibility angle (content ranking, position tracking, keyword movement analysis)

---

## Overview

- Matthew Alves-Hill introduced as new managing editor, bringing expertise from GrowthX's strategy sprint team and Atlas workflow optimization
- Identified input quality as root cause of TLDR and "How to Start a Business" content issues; new agentic pipelines in Atlas will enable more targeted research control and editorial intervention
- Glossary content performing well but requires quality review for recent articles post-Atlas migration; established 6-12 month refresh cycle threshold
- Looker reporting dashboard introduced with gaps; team to add glossary segmentation, individual URL tracking, keyword position movements, internal linking analysis, and traffic source filtering

---

## Key Topics

### Team Updates and Introductions

- Matthew Alves-Hill introduced as new managing editor from GrowthX, bringing 6+ months of strategy sprint experience onboarding new clients
- Started at GrowthX in March 2025 alongside Jakub; deep expertise in Atlas workflows and new agentic pipeline implementations
- Kerry McCreadie on vacation until Monday; Mark Velarga absent due to urgent project; Jess Scott not actively present in discussion

### Content Quality and Improvement Strategies

- Glossary content performing well overall but requires quality audit for articles published post-Atlas migration; editor currently 2+ months behind on review cycle
- TLDR content facing structural and content alignment issues: mismatched structure for top-of-funnel vs. middle-of-funnel content, TLDRs not referencing source article, quality degradation post-Atlas platform switch
- "How to Start a Business" programmatic content: errors in research quality, variation in output depth, need for editorial intervention and refined artifact curation
- New agentic pipelines in Atlas to be implemented: Linear ticket already created; provides tighter control over research process, more targeted instructions, and ability for editorial feedback loop mid-generation
- Strategy: improved input artifacts (research direction, sourcing instructions) + agentic control + editorial oversight = better scaling without sacrificing quality

### Reporting and Analytics

- Looker dashboard recently built and shared; pulls GSC data (clicks, impressions) segmented by content cohorts (Airtable-driven clusters)
- Current capabilities: non-branded traffic filter (removes Homebase branded keywords), cohort grouping by content type and time period
- Critical gaps identified:
  - Glossary vs. other content segmentation (internal distinction needed; cohort may not distinguish properly)
  - Traffic source filter missing (organic, direct, referral breakdown)
  - Individual URL tracking unavailable (need to see which specific pages drive clicks/impressions)
  - Keyword position movement tracking absent (need to monitor progression from page 2→1, or position improvements within page 1)
  - Internal linking analysis missing (identifying orphan/nearly-orphan pages for linking opportunities)
  - LM referral traffic breakdown (by cluster and URL) to be added next
- Jakub to create Linear ticket for data team; improvements targeted for next sync (2 weeks out)

### Content Refresh Strategy

- No systematic content refresh currently implemented for programmatic content (glossary, TLDRs, "How to Start a Business")
- Glossary content now entering 6-12 month refresh window; Jakub's analysis shows glossary articles still ranking strong with minimal keyword position degradation — not yet at refresh urgency stage
- Homebase maintaining separate manual refresh batch for "How to Start a Business" content while GrowthX stabilizes Atlas pipeline
- Next steps: build automated triggers and monthly reporting for keyword position movements and opportunity identification; support refresh workflows once base content quality and input artifacts are solid
- Timeline: refresh workflows can be ramped up once initial quality/reporting improvements complete

---

## Action Items

**Matthew Alves-Hill (GrowthX)**
- Set up new agentic pipeline in Atlas for Homebase (Linear ticket already created)

**Sonia Urlando (Homebase)**
- Review and quality check glossary articles published after switch to Atlas platform

**Jakub Rudnik (GrowthX)**
- Create Linear ticket for data team to update Looker dashboard (add glossary segmentation, traffic source filters, individual URLs, keyword position movements, internal linking data)

---

## Transcript
**Matthew Alves-Hill:** Thank you.

**Matthew Alves-Hill:** Hey, Jakub.

**Jakub Rudnik:** Hey, Matt.

**Jakub Rudnik:** How are you doing today?

**Matthew Alves-Hill:** Busy.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** Yeah, transitioning is always busy here, but taking on new stuff and getting onboarded is what it feels like.

**Matthew Alves-Hill:** And she's been able to jump in and take on some of the generation this week, which has been a huge help.

**Matthew Alves-Hill:** Yeah.

**Jakub Rudnik:** Make sure to say thank you to her. I didn't know how much room she had for that.

**Jakub Rudnik:** So that's great.

**Matthew Alves-Hill:** Yeah, that was a lifesaver.

**Jakub Rudnik:** So Sonia will be joining us today.

**Jakub Rudnik:** Hi, Sonia.

**Sonia Urlando:** Hello.

**Jakub Rudnik:** How are you doing today?

**Sonia Urlando:** Good. How are you both doing?

**Jakub Rudnik:** We're good. This is Matt.

**Matthew Alves-Hill:** Hi, Sonia. Nice to meet you.

**Sonia Urlando:** Thank you.

**Sonia Urlando:** Is Carrie still on vacation?

**Sonia Urlando:** Yeah, Carrie's out until Monday. Mark sent me a message this morning that he unfortunately has to miss this meeting just because he's got a rush project that came up. So it's just going to be a small meeting today.

**Jakub Rudnik:** Yeah, and we, well, and that's okay.

**Jakub Rudnik:** We'll just meet in two weeks and do things async and all that.

**Jakub Rudnik:** But as I said last week, I wanted to introduce you to Matt and so let him do an intro in a second.

**Jakub Rudnik:** But he's taking over that managing editor role.

**Jakub Rudnik:** So similar to what, how we're working with Jess, but I don't think much from like these type of calls will be that different there.

**Jakub Rudnik:** I think where I'm excited for Matt especially is that he's been real, he's been in our growth sprint team, which is how we've been onboarding clients for the last four months.

**Jakub Rudnik:** So it's not something that you experienced as like our first client, but it's something how we've changed and been really experimental on it, like the front of a lot of the things we're doing.

**Jakub Rudnik:** So he's been really deep into Atlas and our new workflows and even new iterations of those, what we're calling our agendic workflows.

**Jakub Rudnik:** And so he's actually bringing like things that I haven't seen yet on that front.

**Jakub Rudnik:** I know that that's when we kind of did a strategy reset a lot about you.

**Jakub Rudnik:** And Kerry, we're hoping to get more, like, see behind the scenes, have more constant iteration there.

**Jakub Rudnik:** And I think Matt is kind of the perfect Emmy to be coming in for that.

**Jakub Rudnik:** So I'll stop doing the intro and gassing Matt up.

**Jakub Rudnik:** But Matt, if you would just say hi and, you know, what you've been doing before this and where you're from, all that stuff.

**Matthew Alves-Hill:** Yep.

**Matthew Alves-Hill:** So like Jakub said, I was in the strategy sprint.

**Matthew Alves-Hill:** I've been at GrowthX for, I think I started in March, just after Jacob, actually.

**Matthew Alves-Hill:** But in GrowthX years, like, it feels like five years now.

**Matthew Alves-Hill:** Before that, I, so I've been in content, SEO, et cetera, for a while.

**Matthew Alves-Hill:** And then before that, I was market research, various different things.

**Matthew Alves-Hill:** But yeah, I think I've been getting up to speed on what's going on on Homebase.

**Matthew Alves-Hill:** I've still got a bit more research to do, but, like, for the...

**Matthew Alves-Hill:** The early feel here is super excited to get stuck in.

**Matthew Alves-Hill:** Like Jakub said, in strategy sprint with onboarding customers, it's been basically a ramp.

**Matthew Alves-Hill:** And the idea is to set the accounts up to be handed off and with the best practices in place.

**Matthew Alves-Hill:** And that goes down to curating the artifacts that determine the Atlas output, testing new Atlas pipelines, new research functionality, all of that.

**Matthew Alves-Hill:** So from my brief reading up on what's going on in Homebase so far, I think fundamentally it's an input issue, I guess, on our end.

**Matthew Alves-Hill:** And we need to figure out how to leverage our tools.

**Matthew Alves-Hill:** They're improving kind of every week.

**Matthew Alves-Hill:** How to leverage them properly because the problems, you know, are effectively like, as with all AI, like the heavy upfront, the heavy upfront work so that it scales correctly.

**Matthew Alves-Hill:** So I really think, really keen to add value there.

**Matthew Alves-Hill:** Yeah, really excited to get stuck into what's been going on and see how we can improve the input and ultimately improve the output.

**Sonia Urlando:** I think of the projects we've been working on more recently, where we've seen a lot of success and performance has been with the glossary piece. I think that's been running really smoothly. And there are areas to improve that more and also build other processes from that. But yeah, I'm excited for you to get the lay of the land and share your experience and ideas with us.

**Matthew Alves-Hill:** For sure.

**Jakub Rudnik:** And I'm sure with Matt that, just as you said Sonia, the glossary is working pretty well. Obviously we'll continue publishing there, but getting the other two pieces across the line — they've been almost there, not quite right, going back and forth for too long. So that's where we're prioritizing right now. I think it's one of our priorities across the few accounts that Matt's jumping in on.

**Jakub Rudnik:** And so I don't know, Matt, if you have any immediate thoughts to add or otherwise we can do some of that async, but that's the things that is he's jumping in.

**Jakub Rudnik:** We really want to get across the line.

**Jakub Rudnik:** I mean, especially with TLDR — it's such a short amount of content, frankly. Some of the errors you all unearthed, I should have been more in tune with. Day-to-day we're not connecting our TLDR to the existing article and product. Some of that stuff is easy to fix on the upfront side. Matt bringing that expertise had some immediate ideas on where to fix that.

**Jakub Rudnik:** Like how to start a business content. When we were chatting through that, I could see the light bulbs going and ideas forming. I think we'll have really good progress in the next week, if not by the next call.

**Jakub Rudnik:** So yeah, that we know that's a priority.

**Jakub Rudnik:** Definitely feel that Matt's got that as like very clear marching orders here because the other pieces are working well.

**Jakub Rudnik:** Matt, anything you want to add?

**Matthew Alves-Hill:** Speaking of that.

**Matthew Alves-Hill:** Yeah, I can add a little. I'm just getting up to speed, but I watched the call from last week. I think it will be cool to grab some of Mark's time specifically to learn more about how you're tracking quality as the article is generated.

**Matthew Alves-Hill:** So, like, the first, I guess the first, like, major update there is that, like, we're running out new agentic pipelines in Atlas.

**Matthew Alves-Hill:** So the plan is to get that set up for Homebase. The Linear ticket's already in. What that means is we have a lot more control over the research process. We can be a lot more targeted and efficient in how the research is done and give it more instruction, which in the past was a bit of a black box.

**Matthew Alves-Hill:** So that's the thing — some of the things we've been doing in strategy sprint, especially when clients work in regulated spaces like legal or medical, where research quality is absolutely critical.

**Matthew Alves-Hill:** So the agentic pipeline has been like really handy for research quality on that front.

**Matthew Alves-Hill:** So I think with the variation issues on "How to Start a Business" — yes, we want it programmatic, but that doesn't mean the text and copy should be programmatic. We want it deeper. Editorial intervention needs to happen more than it has been.

**Matthew Alves-Hill:** Once the research phase is locked in, the article generation comes after, so you're not getting any more input. As you're editing or trying to improve, your research is already done. The agentic pipeline should solve a lot of that.

**Matthew Alves-Hill:** So there are a couple of things — in terms of prioritization, we've been in a period of change with some projects a little stalled, and we're trying to get back on track with quality.

**Matthew Alves-Hill:** I think right now where we're at as well is like there's a couple of things even within the glossary.

**Sonia Urlando:** I think something we haven't done since switching into Atlas and resetting the platform is pull some of the glossary articles from that period and do a quality check.

**Sonia Urlando:** I'll admit it's something I haven't done deliberately. We have an editor who works on them after publishing, but usually she's a couple months behind. So I don't know if we've hit the point where she's working on recent articles and catching any quality changes.

**Sonia Urlando:** So at this point, I'd say let's make sure the workflows and artifacts are solid for what's already working. We've also been talking about reporting and refresh opportunities, and those have gotten a bit lost in the mix as we look at the glossary program that's been running well.

**Sonia Urlando:** We've surfaced a few times what recommendations we'd have for keeping these refreshed and what automations could flag when they need refreshing. So we're looking to reevaluate quality and make sure we have a good system for refreshing them.

**Sonia Urlando:** With rolling out programmatic pages, Mark has a batch of "How to Start a Business in X State" he's working through. We're going to parallel path this internally in the short term while we continue discussing how to get the artifacts up to speed.

**Sonia Urlando:** We have the hub and everything for those being built internally that we want to start getting live. I think it's good to chat with Mark before our next meeting. We'd want to have discussions and get transparency on the work stream, making sure those artifacts are in the shape we'd want to see before we start getting our hands on content.

**Sonia Urlando:** And we haven't been doing content refresh for you guys at all.

**Matthew Alves-Hill:** No, just the programmatic — glossary entries or TLDRs that we do systematically. We've been in a starting phase with "How to Start a Business in Different States" programmatic pages.

**Sonia Urlando:** And TLDR seems like fundamentally it's the same — an input issue.

**Matthew Alves-Hill:** I saw you mentioned the structure is too rigid when the content is top-of-funnel or middle-of-funnel.

**Matthew Alves-Hill:** That seems like something we should be able to fix straightforward. Our pipeline should recognize that. If the article is top-of-funnel, the TLDR workflow shouldn't have structure mismatches. But the fundamental problem is the TLDR is not referencing the content. We've had iterations around length and brand voice, and we got to a place where that worked.

**Matthew Alves-Hill:** Then with the switch to Atlas, we kind of lost some of that quality at the outset and it needs to be retrained.

**Sonia Urlando:** We kind of stalled in getting it back up. And even after a few back-and-forths, the content of the TLDR is not lining up — even though structure and brand voice look aligned. There's a mismatch, like in a middle-of-funnel piece where it lists "our top five picks of X software" but lists different software than is in the article body.

**Sonia Urlando:** And my comment in the artifact documents about, I think the structure that was laid out there looked a little bit more of that middle of funnel, which is useful to have and to like model off of other middle of funnel pieces where the TLDR is all structured.

**Sonia Urlando:** But I think if...

**Sonia Urlando:** If we try to fit a square peg into a round hole with top-of-funnel content, that's not going to serve it as well.

**Sonia Urlando:** So yeah, I think we should focus on getting these things up and running first.

**Matthew Alves-Hill:** ...

**Matthew Alves-Hill:** That's where we can definitely make improvements toward what you want to see — fixing obvious errors and content misses, which is really a research function not being instructed correctly.

**Matthew Alves-Hill:** That will be my main goal — to go through what's informing these workflows for Homebase. I'm happy to walk you through how we're changing them and set up a collaborative process where we can sense-check improvements iteratively.

**Matthew Alves-Hill:** The scale thing shouldn't be a problem. Whether it's programmatic, if the inputs are correct, that's where we can really ramp the scale. So I'm very keen to get stuck in.

**Matthew Alves-Hill:** Yeah, I think the artifacts are a good start. Let's work through those.

**Sonia Urlando:** I think that's a good call to put that in front, Matt. Thank you.

**Sonia Urlando:** On the reporting and refresh side, for glossaries specifically, we're at around six months in, and I think it's worth watching. We can build that into the Looker dashboard.

**Jakub Rudnik:** At that stage, typically we're not even thinking refresh — a lot of content is still ranking well. It's good to build triggers and reports though. While you all were talking, I was spot-checking and not seeing degradation.

**Jakub Rudnik:** We're not seeing pages losing keyword positions, which is where you'd start refreshes. There might be quality issues, but ranking-wise and from a refresh cadence perspective, we're starting to approach the six-to-12 month range threshold.

**Jakub Rudnik:** So it makes sense why we haven't done refreshes yet. However, you have a team doing small batches of refreshes each month. As we figure out workflows and improve quality, there's lots of content to refresh. When we set things up properly and outputs are good, we can scale refresh support.

**Jakub Rudnik:** Have we shown you our Looker dashboard?

**Sonia Urlando:** Not yet.

**Jakub Rudnik:** I think it was still in progress last time. Yeah, we had a screenshot in the agenda, but team transition meant that got lost. This has been built though, and there are still additions to be made.

**Sonia Urlando:** Right now I can't segment just glossary versus other things we've done.

**Jakub Rudnik:** There are things I want to add, but this is already an improvement. Let me walk through this quickly since we haven't shown you. There are pieces we should be adding. We can get a ticket with our team, but overall, here's what we have.

**Jakub Rudnik:** We have two or three dropdowns on each page and I want to add another one. Cohorts are set up in Airtable and represent different content clusters. That's where we should add glossary versus blog segmentation. The first thing I do when looking for our client impact is check off the non-branded URL filter.

**Jakub Rudnik:** That filters everything else on your site, so we're just looking at our content. It's broken up across topical areas with an obvious date range filter. We also need to add a traffic source filter — organic, direct, referral, etc. We're primarily looking at organic, but that filter would be useful. I'll follow up with the team. Overall, the dashboard shows clicks.

**Jakub Rudnik:** Impressions — this is all pulling from GSC data for weeks and months. We can look at just our content, which is more useful than raw GSC.

**Jakub Rudnik:** Non-branded removes branded search. There's a filter pulling out Homebase keywords specifically, so it's all traffic beyond that. Honestly, it doesn't look too different most of the time, but sometimes branded content shows up here.

**Jakub Rudnik:** Cohorts is where I spend my time — traffic over weeks by content clusters. That gives the best macro-level visibility into what's working by cluster and how we're growing. This is mostly glossary, and that's where we've seen traffic acceleration. We can see the breakdown by time period compared to previous. What I'd like to add is individual URLs.

**Jakub Rudnik:** That's where we can see what's growing and what's successful, but also what's falling — where are refresh opportunities? There needs to be a second check because sometimes content gets hurt by AI overviews, not by ranking issues, but we should still add it.

**Jakub Rudnik:** I don't know if we can add this to the dashboard or just stay in communication, but we're trying to shift and expand metrics beyond impressions and clicks — overall keyword volume, keywords on page 1, keywords that moved from page 2 to 1.

**Sonia Urlando:** Or into the top three positions.

**Sonia Urlando:** What might also be tangible is internal linking — which pages don't have links, how many links they have. Adding those layers, either in the dashboard or conversations, is where we want to go for thinking about refreshes and next steps with each piece of content.

**Jakub Rudnik:** Some of those keyword position movements can be built in here.

**Sonia Urlando:** Queries has some of that information, though some parts need updating. I often do ad-hoc analysis in SEMrush or Ahrefs.

**Jakub Rudnik:** There are a couple things missing, but we should get a Linear ticket to the data team with improvements. We can typically show LM referral traffic broken down by cluster and URL as well.

**Jakub Rudnik:** That's another tab we'll have by our next call. When we have those cleaned up, we'll get your eyes on it again in two weeks. We also need to add keyword movements. On internal linking, I need to build a process doc and run a report to find orphan or nearly-orphan pages so we can guide links to them. We can make these repeatable — monthly reports on keyword movements, internal linking as a one-off project with recommendations.

**Sonia Urlando:** Yeah, that makes sense. The reporting has been a gap for a while and we want to close that quickly.

**Jakub Rudnik:** Excited to see more functionality get added there.

**Sonia Urlando:** Thanks for being here.

**Jakub Rudnik:** Next time I'll do a walkthrough on digging into Atlas and the changes we've been making. I'll ping you or Mark in Slack if I have specific questions.

**Matthew Alves-Hill:** As I get more context, maybe I'll schedule time outside our weekly syncs, but only if I really need to.

**Sonia Urlando:** Let us know.

**Matthew Alves-Hill:** Thank you both. Have a good rest of the day.

**Sonia Urlando:** Bye.
