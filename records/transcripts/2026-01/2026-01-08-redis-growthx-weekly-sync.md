# Redis <> GrowthX - Weekly Sync

<metadata>
date: 2026-01-08
time: 17:30 UTC
duration: 19 minutes, 15 seconds
organizer: team@growthxlabs.com
participants:
  - Alexis Ruiz (Redis)
  - Reet Mand (Redis)
  - Fung-Lin Wu (Redis)
  - Régine Carreras (Redis)
  - Erik O'Brien (GrowthX)
fathom_recording_id: 112814349
fathom_url: https://fathom.video/calls/524334770
share_url: https://fathom.video/share/gMnMRb3LcicnT5Yx-m9xk4DTe-UGEzh_
source: fathom
enriched_on: 2026-02-28 22:45 UTC
</metadata>

---

## Summary

Redis and GrowthX discussed content publishing acceleration, early performance metrics from December, and operational improvements. The teams aligned on a fast-publish-then-review model for articles, with deeper reviews reserved for high-traffic pieces (100+ sessions/month). Key operational shifts include moving to biweekly syncs and adding regional performance tracking to reporting dashboards.

---

## Context

This meeting kicks off Redis's Q1 content production cycle with GrowthX following the strategy sprint and holiday break. Redis has a 17-article content backlog in active review, with 12 articles awaiting PMM review and 5 in brand review. GrowthX began publishing Redis content in early December, generating strong initial traffic signals despite the holiday period being historically weak for content metrics. The team is establishing publishing workflows including Sanity content management, Canva template access for self-service blog images, and GA4 event tracking. A key strategic decision is under consideration: moving from comprehensive multi-stage reviews to a rapid-publish model, conducting deeper technical reviews only for articles that gain significant traction (100+ sessions/month), mirroring Airbyte's approach.

---

## Relevance

- **Content Operations:** Sets publishing workflows, template access, and authorship metadata requirements for B2B content at scale
- **Performance Benchmarking:** Early December articles (138–118 sessions) establish baseline traffic metrics despite holiday seasonality
- **Publishing Model Evolution:** Tests rapid-publish model with post-publication reviews, reducing editorial friction while maintaining technical accuracy
- **Reporting & Analytics:** Establishes GA4 event naming conventions (OS-prefixed events) and adds regional performance tracking to inform content strategy
- **Cross-functional Alignment:** Clarifies team transitions (Ada to strategy sprint, Gabby as managing editor) and operational POCs (Erik for GrowthX, Fung-Lin for Redis)

---

## Overview

- **Review Process Overhaul:** To accelerate publishing, Redis will evaluate bypassing PMM/Brand reviews by end-of-month. The proposed model is to publish quickly, then conduct deep reviews only for articles exceeding a traffic threshold (e.g., 100 sessions/month).
- **Strong Early Performance:** December's initial articles showed healthy traffic (e.g., `ContextRot` → 138 sessions), a positive signal given the holiday period. All new content was indexed successfully.
- **Reporting & Ops Updates:** The sync cadence shifts to biweekly to focus on strategy. Reporting will be enhanced with regional performance data and conversion tracking for key GA4 events (e.g., `os_book_a_meeting`).
- **Publishing Process Refined:** GrowthX will self-serve blog images via shared Canva templates and retroactively add authors to all published articles, using the name of the PMM who conducted the review.

---

## Key Topics

### Content Review & Publishing Process

  - **Backlog:** 12 articles are in PMM review; 5 are in brand review.
  - **Goal:** Bypass PMM/Brand reviews by end-of-month to accelerate publishing.
  - **Proposed Model (based on Airbyte):**
      - Publish content quickly to gather performance data.
      - Conduct in-depth PMM reviews only for high-traffic articles (e.g., \>100 sessions/month) to ensure accuracy and optimize for conversion.
  - **Publishing Requirements:**
      - **Blog Images:** GrowthX will self-serve via shared Canva templates.
      - **Authorship:** Authors must be added to all articles in Sanity.
          - **Retroactive:** Use the PMM who reviewed the article.
          - **Future:** Use the assigned PMM/technical marketer.

### Performance & Reporting

  - **December Performance (Initial Articles):**
      - `ContextRot`: 138 sessions
      - `AI use case, financial services`: 118 sessions
      - **Significance:** Healthy initial traffic, especially for a holiday month.
  - **Reporting Enhancements:**
      - **Regional Performance:** Add a section to the dashboard to show international traffic.
      - **Conversion Tracking:** Focus on key GA4 events (e.g., `os_book_a_meeting`, `os_aws_trial`) to avoid double-counting.
  - **Team & Cadence:**
      - **POC Change:** Gabby is now the managing editor; Erik is the primary POC.
      - **Cadence:** Moving to biweekly syncs to focus on strategy and KPIs.

---

## Action Items

**Fung-Lin Wu (Redis)**
- Assign 6 new articles to PMMs/technical marketers including post-holidays batch
- Send primary GA4 conversion event names to Erik (key events: `os_book_a_meeting`, `os_sign_up_payment`, `os_aws_trial`, `os_redis_insight`)

**Erik O'Brien (GrowthX)**
- Check with GrowthX analytics team regarding regional performance breakout in reporting dashboard
- Send Gabby's email to Régine; Régine to grant Canva access for blog image self-service
- Retroactively add PMM/technical marketer authors to ~40 articles in Sanity (use reviewing PMM name for historical articles, assigned PMM name for future pieces)

---

## Transcript
**Alexis Ruiz:** This meeting is being recorded.

**Alexis Ruiz:** Good.

**Alexis Ruiz:** How are you?

**Fung-Lin Wu:** Hi.

**Erik O'Brien:** Hey there.

**Erik O'Brien:** How are you?

**Fung-Lin Wu:** How are y'all?

**Erik O'Brien:** Well, Happy New Year.

**Fung-Lin Wu:** You too.

**Erik O'Brien:** Is this everybody for today?

**Fung-Lin Wu:** Do we know if Claudia is joining?

**Régine Carreras:** I'm actually not sure.

**Régine Carreras:** Yeah, I think Claudia might have had a conflict.

**Régine Carreras:** Ah, she says no.

**Régine Carreras:** Yeah, yeah, yeah.

**Fung-Lin Wu:** Yeah, I believe this is it.

**Fung-Lin Wu:** We might just be missing Reet, but I think we can get started.

**Erik O'Brien:** Okay, wonderful.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** So, got a quick agenda to get through.

**Fung-Lin Wu:** Yeah, and Erik, just a quick intro.

**Fung-Lin Wu:** We invited Régine.

**Fung-Lin Wu:** Régine, am I pronouncing her name right?

**Régine Carreras:** Yes, Régine.

**Fung-Lin Wu:** Régine, okay.

**Fung-Lin Wu:** I meant to have Régine and Claudia, who couldn't make it today, join this meeting because we've had a couple of transitions internally.

**Fung-Lin Wu:** They've been helping a lot with some of the publishing of articles on our website.

**Fung-Lin Wu:** They just want to be informed on how GrowthX is doing it on your end, because I think we usually require authorship and a blog image, so they just want to help inform the GrowthX process.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** Great to meet you, Régine.

**Régine Carreras:** Nice to meet you.

**Erik O'Brien:** All right.

**Erik O'Brien:** So quick updates.

**Erik O'Brien:** We did share five new articles for PMM review.

**Erik O'Brien:** So that puts us at about 12 that are in PMM review, and then we've got five that are in brand review.

**Erik O'Brien:** I did see that we have one article reviewed by PMM, so that should be shifting slightly to 11 and 6.

**Erik O'Brien:** But overall, we've got quite a backlog to get through here in January.

**Fung-Lin Wu:** Yeah, I'm going to assign them out today.

**Fung-Lin Wu:** I think there's about six that I haven't assigned out.

**Fung-Lin Wu:** If I remember, the one that you sent over after the holidays, I haven't gone through yet.

**Fung-Lin Wu:** So I will be assigning those out to our PMM and technical marketer today.

**Fung-Lin Wu:** And then, Erik, on our end, we are actually syncing up as a team internally this Thursday, oh, maybe it's today.

**Fung-Lin Wu:** We're actually syncing up internally, or next, sorry, next week.

**Fung-Lin Wu:** We're syncing up internally next week to see if we all feel good about the quality that GrowthX has been producing, we might be able to just bypass PMM and brand review, hopefully by the end of this month as the goal on our end.

**Erik O'Brien:** Okay, wonderful.

**Fung-Lin Wu:** Can I ask a quick question?

**Fung-Lin Wu:** With most of your clients, are there specific articles that you guys would always prefer the company to continue reviewing, like the super technical ones, or does GrowthX usually have a preference of just bypassing brand and PMM review and just launching on your own?

**Erik O'Brien:** So it varies just depending on overall preference from our clients.

**Erik O'Brien:** Like one client of mine is Airbyte, and they do a quick review.

**Erik O'Brien:** But it's usually same-day and just get it out, and if there starts to be increased traffic and it's performing well, then we might go through and do another detailed PMM review and say, hey, can we check this just to see if there's anything we need to review or refine? As it's performing, we make sure technical accuracy is on point.

**Erik O'Brien:** And so it kind of leads to higher conversion rates.

**Erik O'Brien:** But yeah, I think for the most part, our thesis is really, you know, the more that we can get published, the quicker we can see signals of like which cohorts and topic clusters are performing well and be able to kind of adjust strategy as we see fit from that.

**Erik O'Brien:** But overall, I think, you know, if the goal is to get to like less reviews by end of month, given that we're, you know, I think just out of the strategy sprint, still kind of calibrating on technical accuracy.

**Erik O'Brien:** The first two months are usually the most in-depth, and then we probably get a little bit smoother sailing after that.

**Fung-Lin Wu:** Okay.

**Fung-Lin Wu:** Yeah.

**Fung-Lin Wu:** I kind of like the way that Airbyte does it. Assuming how the conversations internally go next week, I do like the idea that maybe GrowthX just launches on your own without any review.

**Fung-Lin Wu:** I think on the brand side, Allison is feeling pretty good about the brand guidelines to our voice.

**Fung-Lin Wu:** I think it's just a technical piece left that we just have to nail down.

**Fung-Lin Wu:** But I think once that's good, ideally soon, I do like the idea of like maybe if certain articles hit a certain amount of traffic, those are the ones we kind of go back and fine-tune and just make sure there's nothing alarming.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** And for Airbyte, we have some that even have code snippets.

**Erik O'Brien:** And so those are the ones that we will have like our engineering team review really quickly.

**Erik O'Brien:** Just like, is there anything blatantly that catches your eye?

**Erik O'Brien:** And if not, we kind of hit publish.

**Erik O'Brien:** And then, again, just if it hits a certain traffic threshold, like over 100 sessions in a month, then we go back and look at it to just make sure that everything's good and great.

**Erik O'Brien:** So as it continues to perform, there's no reason for people to kind of look at it as a bad piece of content.

**Fung-Lin Wu:** Got it.

**Erik O'Brien:** Awesome.

**Erik O'Brien:** So quick December snapshot of performance.

**Erik O'Brien:** So, you know, we just started publishing early December, but started to see really good traffic from initial pieces.

**Erik O'Brien:** So ContextRot drove 138 sessions, AI use case, and financial services 118.

**Erik O'Brien:** Overall, every new article that we published was automatically indexed.

**Erik O'Brien:** So no issues with, like, technical blockers for indexing.

**Erik O'Brien:** So everything looks pretty good for the initials, you know, three net new and three refreshes that we put out.

**Erik O'Brien:** So overall, early signals, but really good traction so far.

**Erik O'Brien:** Any questions there?

**Fung-Lin Wu:** I don't think so.

**Erik O'Brien:** Awesome.

**Erik O'Brien:** And we'll have, you know, as we continue to publish more content, we'll have a more detailed breakout to, like, how each topic cluster is performing.

**Erik O'Brien:** But right now, we just have, like, a single piece per cluster.

**Erik O'Brien:** So it's spread out pretty evenly.

**Fung-Lin Wu:** Yeah.

**Fung-Lin Wu:** mean, 118-ish feels pretty strong to me initially, like, as an initial.

**Fung-Lin Wu:** I'm curious, like, how you think of it.

**Fung-Lin Wu:** Like, is this a number that you see typically?

**Erik O'Brien:** Yeah.

**Erik O'Brien:** I mean, for December, it's healthy.

**Erik O'Brien:** December is usually, like, a terrible month to get, like, a baseline in place.

**Erik O'Brien:** So I think for December, like, seeing everything trend in the right direction prior to the holiday weeks.

**Erik O'Brien:** It's a great early signal for us.

**Erik O'Brien:** I'd love to get to like a full baseline in January to see where we're really at without the holiday traction kind of disrupting some of the traffic flow and be able to see which ones are starting to get picked up by LLMs as well.

**Erik O'Brien:** We did have a couple articles start to get LLM referrals, but it was like three, so I didn't put that in here today.

**Erik O'Brien:** But at least we are starting to get some citations for the content we're putting out.

**Erik O'Brien:** And then just from an operational standpoint, this last piece here, we were planning to move to a biweekly cadence.

**Erik O'Brien:** And so allow us to kind of focus more on getting production right and be able to kind of provide async updates on Mondays and then use our biweekly.

**Erik O'Brien:** touch points to really focus on performance KPIs and then really make sure that we're focused on kind of the strategic points of the relationship versus really content updates, which had been historically what we focused on during the strategy sprint.

**Fung-Lin Wu:** Yeah, I think that works for us.

**Fung-Lin Wu:** The one thing, if I can ask to add, is there a way to do like a month-end reporting?

**Fung-Lin Wu:** So, I know you mentioned like there's this every Monday Slack update, but maybe if that Monday happens to be like near the month-end, then it could be on a Tuesday.

**Fung-Lin Wu:** Like if the month-end is on a Monday, then instead of a Monday Slack update that week, it's a Tuesday with a month-end, like a full month performance update.

**Erik O'Brien:** Yep.

**Erik O'Brien:** So we typically do that month-over-month reporting usually towards the end or beginning of the month.

**Erik O'Brien:** But yeah, since we're just getting publishing in December and just getting a few pieces out, very little data to go off of.

**Erik O'Brien:** But, yeah, we'll have more kind of comprehensive reporting to go off of on a monthly rolling basis.

**Reet Mand:** Hi, team.

**Reet Mand:** I just have a question.

**Reet Mand:** Hello.

**Reet Mand:** Probably more for, like, us, though.

**Reet Mand:** As I was thinking about this, all the great work that we're doing, Fung-Lin, I was thinking, like, how do we factor in outside of the U.S.?

**Reet Mand:** Because this is probably, a lot of it is very U.S.

**Reet Mand:** influenced, but if there is, like, you know, do we expect the impact on this to be international?

**Reet Mand:** If so, like, how is that perspective being brought in here?

**Fung-Lin Wu:** I would imagine this is global, since this is the blog.

**Fung-Lin Wu:** But maybe what could be interesting is in the monthly reporting or in the reporting dashboard right now, if we can add in a section that includes regional performance.

**Reet Mand:** Yeah, I think, yeah, I like that.

**Fung-Lin Wu:** Yeah, maybe that would be, yeah, because I don't think it's in the current dashboard reporting, but maybe we can add that in.

**Erik O'Brien:** So, yeah, I'll check with our analytics group to see if that's something we can fold into the dashboard that we have.

**Reet Mand:** Yeah, thank you.

**Erik O'Brien:** I've also just requested, we have conversion events, which you guys have quite a few, about 40 conversion events across Google Analytics.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** So, I did request to update that conversion page so that we can see conversions by landing page and be able to filter by GrowthX content.

**Erik O'Brien:** So that'll be an update that we should have within the next week or so.

**Fung-Lin Wu:** Yeah, our conversion event in GA4 is a bit messy.

**Fung-Lin Wu:** Erik, I can probably send you the main ones. There are two main ones: book a meeting and sign up for a form.

**Fung-Lin Wu:** Those are probably the two main ones that we care about.

**Fung-Lin Wu:** I can send you the correct event name in GA.

**Fung-Lin Wu:** Perfect.

**Fung-Lin Wu:** Yeah, let me, sorry, let me write that down.

**Alexis Ruiz:** probably the Marketplace download trials and Redis Insight downloads too, I think.

**Alexis Ruiz:** And also probably the Marketplace download trials and Redis Insight downloads.

**Alexis Ruiz:** And sign up payment—it's `os_sign_up_payment`.

**Alexis Ruiz:** It's all the OS ones.

**Fung-Lin Wu:** All the events we care about are the ones with OS. It stands for Outshine, our advertising agency who set up GA4 for us.

**Fung-Lin Wu:** But the correct conversion ones are the ones prefixed with OS (e.g., `os_book_a_meeting`, `os_aws_trial`).

**Alexis Ruiz:** Like `os_aws_trial`, `os_redis_insight`—those are the clean ones.

**Fung-Lin Wu:** There's a bunch of events, and if you use all 40 of them, it's going to create a lot of overlap and quadruple-count conversions.

**Erik O'Brien:** Gotcha.

**Erik O'Brien:** So, yeah, if you can send me just the primary ones that we want to start looking at for content that we put out, that would be great, and then I can report on those.

**Fung-Lin Wu:** Okay.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** So, yeah, quick updates this week. We're getting back into the swing of things after the new year.

**Erik O'Brien:** So, I think really the primary goal is to get through some of these that are in the backlog, get some new content published, and hopefully see compounding traffic and have our efforts start to shine a little bit more once we get some new content out.

**Fung-Lin Wu:** Same.

**Fung-Lin Wu:** And Régine, I don't know if you want to cover real quick about the publishing aspect in Sanity.

**Fung-Lin Wu:** Do you guys have access back already?

**Erik O'Brien:** Yes, we should.

**Régine Carreras:** Yes, because I think Scott, it was something that the way it was set up, I think it was like split in some way, but I think they fixed that on Sanity.

**Régine Carreras:** And then I also wanted to see if we could maybe give someone on your team access to our Canva templates for our blog images, just so that you're able to self-serve in that way.

**Régine Carreras:** Because I think when I was talking to our project manager about it, she said, if you had any emails that we could just add to our Canva instance, that would make it so that you don't necessarily have to come to us for anything.

**Régine Carreras:** You just use the templates.

**Régine Carreras:** But yeah, I mean, if you have anything or any emails that we can just add or you can email those later, but.

**Erik O'Brien:** Yeah, I will send those over right after this.

**Erik O'Brien:** It's going to be our managing editor, Gabby, who was pinging about the access issue.

**Erik O'Brien:** So I will send her email over to you, and then we can include those.

**Erik O'Brien:** Great.

**Régine Carreras:** I'm not quite familiar with where this is in Sanity, but I do know that some of the blogs might have been missing authors.

**Régine Carreras:** So in addition to the blog image, we just want to make sure that authors are input on every blog that goes out.

**Régine Carreras:** But other than that, from a web standpoint, that's what we want to make sure we have on every blog that goes out.

**Erik O'Brien:** Yes, absolutely.

**Erik O'Brien:** Is there, like, a group of authors that we want to use or rotate between, or is there, like, a consistent author we want to use?

**Fung-Lin Wu:** For now, the author will just be whichever PMM or technical marketer is reviewing it. So Jim Allen Wallace, Talon, or Rini—whoever is reviewing.

**Erik O'Brien:** Now we're going back, and it's like 40-some articles we have to update.

**Fung-Lin Wu:** Yeah.

**Fung-Lin Wu:** Just put it all under my name.

**Erik O'Brien:** There you go.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** So I will send over that email for Canva, and then we will go and retroactively add those authors to whichever PMM was doing their review.

**Fung-Lin Wu:** I owe you the new assignments of the new articles that came in this week, and then I also owe you the conversion names.

**Fung-Lin Wu:** Yes.

**Erik O'Brien:** Perfect.

**Erik O'Brien:** And I will check into that regional performance breakout, see if we can add that.

**Alexis Ruiz:** And Erik, I just slacked you two articles that were done, reviewed by Finance, with a couple of overall comments that I pasted in. Other than that, she said they were great.

**Alexis Ruiz:** And I think I saw someone on your team was already responding to her comments on the docs, but just wanted to put that.

**Alexis Ruiz:** Because I see that they're still in PMM review status.

**Erik O'Brien:** I saw Gabby was looking at the, I think, database performance optimization one.

**Alexis Ruiz:** Yes.

**Erik O'Brien:** Wonderful.

**Fung-Lin Wu:** Is Ada, is she on vacation?

**Erik O'Brien:** No, so Ada is with the strategy sprint team.

**Erik O'Brien:** Ah.

**Erik O'Brien:** So she gets you guys through the strategy sprint, and then Gabby is now the managing editor full-time.

**Fung-Lin Wu:** Ah, okay.

**Fung-Lin Wu:** Helpful to know.

**Fung-Lin Wu:** I was like, did she just drop us?

**Erik O'Brien:** No, she just moved to the strategy sprint team.

**Fung-Lin Wu:** So it's mostly Gabby now.

**Erik O'Brien:** Gabby will be the editor, and then I will be your point of contact for pretty much everything.

**Fung-Lin Wu:** Ah, got it.

**Fung-Lin Wu:** Okay, nice to know.

**Fung-Lin Wu:** Well, tell Ada we said thanks for everything.

**Erik O'Brien:** I will.

**Erik O'Brien:** She'll appreciate that.

**Fung-Lin Wu:** Thank you.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** Any other questions or anything top of mind for you guys?

**Fung-Lin Wu:** I don't think so.

**Fung-Lin Wu:** All right.

**Erik O'Brien:** Well, again, Happy New Year.

**Erik O'Brien:** Hope you guys' holiday was great.

**Erik O'Brien:** And then we'll look forward to seeing you guys in a couple weeks.

**Fung-Lin Wu:** Yeah, you too.

**Fung-Lin Wu:** Thank you.
