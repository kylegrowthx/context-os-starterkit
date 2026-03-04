# GrowthX - S1 Web

<metadata>
date: 2025-11-13
time: 13:59 UTC
duration: 14 minutes
organizer: Georgemaine Lourens (GrowthX)
participants: Marcus Derencius (GrowthX), Georgemaine Lourens (GrowthX), Joery Van Druten (SentinelOne), Andrew VanNess (SentinelOne), Tim Lisiecki (SentinelOne), Ankit Pahuja (SentinelOne)
fathom_recording_id: 101376447
fathom_url: https://fathom.video/calls/473400600
share_url: https://fathom.video/share/ksLxDPjFGyJWzvQxa8qg4g2WgezBZerK
source: fathom
enriched_on: 2026-03-02 02:15 UTC
</metadata>

---

## Summary

GrowthX and SentinelOne agreed on a major refactor of SentinelOne's CVE database to address performance issues caused by fetching all entries on every page load. SentinelOne's Andrew VanNess will lead the refactor to integrate Algolia as the search index, update to Next.js best practices, and migrate from PageRouter to AppRouter in December. A code freeze is now active to prevent rework. Once SentinelOne delivers the refactored codebase, Marcus Derencius (GrowthX) will maintain the project, with SentinelOne handling P0/P1 bugs during refactor and GrowthX handling lower-priority fixes afterward.

---

## Context

GrowthX is providing ongoing development and maintenance services for SentinelOne's CVE (Common Vulnerabilities and Exposures) database, a searchable index of security vulnerabilities. Marcus Derencius from GrowthX has been maintaining the codebase, but the current architecture has fundamental performance problems: it fetches all database entries on every page load, causing slow search performance even with just 500 entries and preventing scaling to the planned 10,000+ entries. SentinelOne's product team (led by Joery Van Druten) recently completed a redesign and is now updating their technical infrastructure across all projects. To align the CVE database with SentinelOne's new standards, Andrew VanNess (Dev Lead) will take ownership of the refactor, implement Algolia for search indexing, update package versions, and migrate the codebase to Next.js AppRouter. After stabilization, the project will transfer back to Marcus for ongoing maintenance.

---

## Relevance

**To GrowthX Delivery:**
- CVE database project temporarily shifts to SentinelOne ownership during major refactor; Marcus will resume maintenance post-handoff
- Code freeze now active; P2/P3 bug fixes deferred until refactor completion to avoid rework
- SentinelOne driving architecture changes (Algolia integration, AppRouter migration) that will change the codebase significantly
- Content publishing (500 entries per batch) should pause until refactor stabilizes to prevent conflicts with Algolia migration scheduled for December

**To GrowthX Business Development:**
- SentinelOne treating CVE database as a strategic tool (investing in performance overhaul) — signals strong engagement with the project
- Monthly content batch publishing cadence (500 entries) shows planned long-term growth for the database; SentinelOne initially requested pause during refactor
- Regular sync cadence established between Andrew VanNess and Marcus to maintain communication and project visibility post-handoff

---

## Overview

- **Code Freeze:** A code freeze is active to prevent rework during SentinelOne's refactor of the CVE database.
- **Algolia Migration:** SentinelOne will migrate the database to Algolia to fix performance issues (e.g., slow search) caused by fetching all entries on every page load.
- **Ownership Handoff:** SentinelOne will own the refactor, then hand the project back to GrowthX for ongoing maintenance.
- **Bug Fixes:** SentinelOne will fix P0/P1 bugs during the refactor; GrowthX will handle lower-priority fixes post-handoff.

---

## Key Topics

### Problem: Performance & Scalability

  - The current architecture fetches all entries from the CMS on every page load, causing performance issues.
      - **Symptom:** Slow search, even with only 500 entries.
      - **Limitation:** Prevents scaling the database to the planned 10,000+ entries.

### Solution: Refactor & Migrate to Algolia

  - SentinelOne will refactor the project to use Algolia as the index for all posts.
      - **Benefit:** Algolia will handle search/filtering, simplifying the codebase and improving performance.
  - The refactor will also align the project with SentinelOne's new site architecture.
      - **Updates:** Package versions, Next.js best practices.
      - **Migration:** From Next.js PageRouter to AppRouter (scheduled for December).

### Execution & Handoff

  - **Code Freeze:** Active immediately to prevent rework.
  - **Refactor Ownership:** SentinelOne's Andrew VanNess (Dev Lead) will lead the refactor.
  - **Bug Fixes:**
      - **SentinelOne:** Will fix P0/P1 bugs during the refactor.
      - **GrowthX:** Will handle lower-priority (P2/P3) fixes post-handoff.
  - **Handoff:** SentinelOne will return the project to GrowthX for ongoing maintenance.
  - **Communication:** Andrew will maintain a regular sync cadence to keep GrowthX informed.

### Content Publishing Coordination

  - **GrowthX:** Will inform the content team about the refactor to coordinate the publishing of new entry batches.
  - **SentinelOne:** Requested a temporary pause on new content publishing until the refactor is stable.

---

## Action Items

**Andrew VanNess (SentinelOne)**
- Enforce CVE database code freeze; defer P2/P3 fixes until handoff to Marcus
- Refactor CVE database to Algolia; fix P0/P1 bugs; hand off to Marcus
- Schedule recurring syncs w/ Marcus and Georgemaine regarding refactor updates

**Tim Lisiecki (SentinelOne)**
- Refactor CVE homepage to fetch fewer entries; investigate 1-entry section flag

**Marcus Derencius (GrowthX)**
- Confirm next CVE batch timeline; notify SentinelOne; coordinate with content team on publishing pause during refactor

---

## Transcript
**Marcus Derencius:** Thank you.

**Marcus Derencius:** Hello, Tim.

**Tim Lisiecki:** How you doing?

**Marcus Derencius:** I didn't do.

**Tim Lisiecki:** Good.

**Joery Van Druten:** Morning.

**Marcus Derencius:** Morning.

**Joery Van Druten:** I'm staying off camera at this time.

**Joery Van Druten:** Thank you.

**Marcus Derencius:** Oh, we need your face.

**Joery Van Druten:** Got the whole team here, Marcus.

**Marcus Derencius:** I'm in your face.

**Joery Van Druten:** I don't want to intimidate you.

**Marcus Derencius:** It is a little bit.

**Joery Van Druten:** Thank you for meeting.

**Joery Van Druten:** Congrats on the launch yesterday.

**Marcus Derencius:** Nice, yeah.

**Joery Van Druten:** Thank you.

**Joery Van Druten:** Yeah, I wanted to follow up because the team looked into the code, and what we wanted to introduce is if you want to step on the brakes a little bit?

**Marcus Derencius:** Okay.

**Joery Van Druten:** Because we need to refactor. Some things have to change because the way that we are going to do things on our end is also going to change.

**Joery Van Druten:** That's why we wanted to meet so that we are all aligned and that we're not going to do any throwaway work.

**Joery Van Druten:** So one of the things is like, yeah, we wanted to see if we can introduce a code freeze.

**Marcus Derencius:** Okay.

**Joery Van Druten:** And that we are going to do some refactoring first before we are going to move on those bug fixes.

**Joery Van Druten:** But I'm going to give it to Andrew.

**Joery Van Druten:** I don't know if you met Andrew before his paternity leave, but he's our dev lead.

**Joery Van Druten:** And he's going to take over this meeting and then can tell you a little bit more about the details.

**Andrew VanNess:** Yeah.

**Andrew VanNess:** Nice to meet you, Marcus.

**Andrew VanNess:** Yeah, excellent work with the project.

**Andrew VanNess:** We were looking through that readme, you included, with some potential problems.

**Andrew VanNess:** There are limitations on how many entries we could have, using server-side props so that we're fetching from the CMS every page load.

**Andrew VanNess:** And both of those problems will go away if we switch to using Algolia as the index for all the posts.

**Andrew VanNess:** We're using Algolia for everything else on our end going forward.

**Andrew VanNess:** So it makes sense that we will update your code to use that.

**Andrew VanNess:** That will solve basically all the issues that you are aware of and that we're aware of with the CVE database project.

**Andrew VanNess:** So we're going to spend a few weeks refactoring, updating that.

**Andrew VanNess:** And then we will give it back to you to support for the remainder of your contract with us.

**Andrew VanNess:** And we'll let you know about the changes, what we're doing, what we did.

**Andrew VanNess:** It's not going to completely overhaul the project, but there will be some pretty significant changes to the search and filters system.

**Andrew VanNess:** It should be a little simpler.

**Andrew VanNess:** Most of that logic will be in Algolia, so you won't have to worry about it in the code base.

**Marcus Derencius:** Yeah, because even in development, I was having trouble with all the search of just 500 entries.

**Marcus Derencius:** I was having trouble already, so.

**Andrew VanNess:** Yeah, yeah, so this will make it easier for everyone.

**Andrew VanNess:** It's not, we don't have to take the site down or anything, you know, it's not that big of a deal, but we just want everything to be standard for our site.

**Andrew VanNess:** So yeah, it's not a huge problem or anything.

**Marcus Derencius:** Yeah, I'm completely fine with that and that's the way forward.

**Marcus Derencius:** So thanks for helping.

**Andrew VanNess:** Of course.

**Andrew VanNess:** Yeah.

**Andrew VanNess:** I don't have a ton more if we want to, I don't know if we want to dig into all the issues specifically or just kind of keep it brief and that we code freeze now.

**Andrew VanNess:** We're going to work on it and we'll let you know what's ready for you to take over for, there's going to be some design changes they want and some bug fixes.

**Andrew VanNess:** Anything critical that we notice with bugs, we will fix while we're in there.

**Marcus Derencius:** Perfect.

**Andrew VanNess:** But I'm sure there will be some work once we're done to get the design up to sensor one standards.

**Marcus Derencius:** Yeah.

**Marcus Derencius:** I don't have a question.

**Marcus Derencius:** I'm happy for you to take over because it was a concern to build it in a way that's similar to the patterns you have, so it fits well. So it's good to have a refactor and moving forward.

**Marcus Derencius:** From here, it's publishing more content, so not changing the code.

**Marcus Derencius:** So that's why I'm happy you're helping.

**Marcus Derencius:** And maybe I just, the question would be, if you're going to be publishing more content, we should wait for this refactoring because probably we are planning to publish many more entries, but not many changes in the code.

**Andrew VanNess:** Yeah, actually, do you know the timeline on adding more entries?

**Marcus Derencius:** Is that...

**Marcus Derencius:** Yeah, I don't have it top of my mind, but yeah, there is a...

**Marcus Derencius:** Yeah, I don't have it on top of my mind, but it'll be soon.

**Marcus Derencius:** So there'll be a cadence of 500 each couple weeks, but I don't have it now.

**Andrew VanNess:** Got it.

**Andrew VanNess:** Yeah, hopefully that can wait until things are a little more stable.

**Andrew VanNess:** Tim just reminded me that we are making some architecture changes to the site.

**Andrew VanNess:** be...

**Andrew VanNess:** So improvements, updating package versions and everything to align more closely with best practices for Next.js.

**Andrew VanNess:** And then in December, we're going to migrate to AppRouter from PageRouter, if you're familiar with that, Marcus.

**Andrew VanNess:** So there will be some changes to the code base along with the refactor, but we will keep you abreast of all that and in the loop.

**Andrew VanNess:** And I'm hoping I can keep you a little more up-to-date and we can meet in some kind of cadence, just so you're aware of what we're doing and we're aware of what you're doing, if there's any new updates to the CV database.

**Marcus Derencius:** Yeah, for me, it sounds good.

**Marcus Derencius:** So I wait for when you say it's ready, then I read that thing and try to continue the patterns, the new architecture.

**Andrew VanNess:** Awesome.

**Andrew VanNess:** Tim and John, do you have anything to add?

**Andrew VanNess:** That I glossed over?

**Tim Lisiecki:** Nothing immediate.

**Tim Lisiecki:** I'm working on a quick refactor to get into the new architecture.

**Tim Lisiecki:** I pulled it down into our dev environment, which has the new architecture.

**Tim Lisiecki:** So I might reach out if there's any questions.

**Tim Lisiecki:** But basically, it seems pretty straightforward for the most part on the homepage.

**Tim Lisiecki:** I love the VOLN database homepage.

**Tim Lisiecki:** And then the entry page, too, seems pretty straightforward as well.

**Marcus Derencius:** Yeah.

**Marcus Derencius:** Nice.

**Marcus Derencius:** Thank you.

**Tim Lisiecki:** I did have a quick question, though, actually, now that think of it, for the homepage.

**Tim Lisiecki:** I'm just going to share.

**Tim Lisiecki:** So all CVEs are getting fetched for this index page, but then it's only used for, I think, nine entries. Do you mind if I refactor that so we're not fetching all?

**Marcus Derencius:** Yep, go ahead.

**Tim Lisiecki:** Is there a reason why we need all entries fetched?

**Marcus Derencius:** So if it does scale to like 10,000, we're not fetching all. Yeah, it's more for the filtering. So as soon as we have Algolia, we can get just the top ones because in case we change or publish again. So it's more for the filtering.

**Marcus Derencius:** So Algolia is going to fix that, so.

**Tim Lisiecki:** Sounds good. And then there's nine here, nine here, and then there's only one there. Is there a reason there's only one?

**Marcus Derencius:** Oh yeah, I have to check what the top score is. Yeah, there's a flag there, there's a boolean for this. So maybe it's just a boolean check on the data that should get published there.

**Tim Lisiecki:** Cool, okay, nice. I'll look into it more, but I just wanted to make sure if there's nine that gets populated here, there's no big major changes if there's only one.

**Tim Lisiecki:** Thank you.

**Tim Lisiecki:** And then I'm just going to click into this, and this should be pretty straightforward.

**Tim Lisiecki:** It is.

**Tim Lisiecki:** And then the search page seems pretty straightforward.

**Tim Lisiecki:** This will be handled by Algolia for the most part, so I won't change much here.

**Tim Lisiecki:** But cool.

**Marcus Derencius:** Thank you.

**Marcus Derencius:** Nice.

**Marcus Derencius:** Okay.

**Marcus Derencius:** Looks simple.

**Andrew VanNess:** Any other questions for us, Marcus?

**Marcus Derencius:** No.

**Marcus Derencius:** I'll just wait. I will check on the timeline for the next batch of entries so we can plan accordingly with the refactoring. I'll let the content team know since they're dealing with all the entries we're going to publish. They need to be aware of this refactoring so we can coordinate planning.

**Marcus Derencius:** No, no more questions.

**Andrew VanNess:** Okay.

**Georgemaine Lourens:** I have a question.

**Georgemaine Lourens:** Well, I just want to clarify something.

**Georgemaine Lourens:** So just to be sure, some of Ankit and some of the other people on the team, they requested a couple of bug fixes in an Excel sheet.

**Georgemaine Lourens:** And they were kind of like P2s and P3s, which aren't like very significant, but you just mentioned that there was going to be a code freeze until the refactoring is done.

**Georgemaine Lourens:** So I just assume that those can be handled on the SentinelOne site and until the code freeze is done.

**Andrew VanNess:** Anything, if there, you know, if there's a P0 or P1, we'll definitely take care of that.

**Andrew VanNess:** We don't want the site to be broken while we're responsible for it.

**Andrew VanNess:** If there's something low.

**Andrew VanNess:** For priority, it can probably wait until we give it back to Marcus.

**Andrew VanNess:** We can discuss if they're specific, if OnKit needs something now, we could do that.

**Andrew VanNess:** But we'd like Marcus to take it back over once we're done.

**Andrew VanNess:** This is just kind of an upgrade temporarily.

**Andrew VanNess:** We don't want to take sole responsibility, and we don't want Marcus to be unaware of how to maintain it.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** All right.

**Georgemaine Lourens:** Clear to me.

**Andrew VanNess:** Thanks for clarifying.

**Andrew VanNess:** Yeah.

**Andrew VanNess:** And just so you know, OnKit is aware of what we're doing, so he will understand if things are a little late for a few weeks.

**Andrew VanNess:** And we're in touch with OnKit, so if he needs something now, we will get it for him.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** Awesome.

**Georgemaine Lourens:** That's wonderful to hear.

**Georgemaine Lourens:** Thank you.

**Andrew VanNess:** Of course.

**Andrew VanNess:** Yeah, you guys won't take the blame for things being late right now.

**Georgemaine Lourens:** Okay.

**Marcus Derencius:** Okay.

**Marcus Derencius:** Okay.

**Andrew VanNess:** Cool.

**Andrew VanNess:** Thank you.

**Andrew VanNess:** Thank you very much for meeting with us on short notice.

**Andrew VanNess:** And yeah, we'll be in touch about this.

**Georgemaine Lourens:** All right.

**Marcus Derencius:** Okay.

**Marcus Derencius:** Thank you.

**Georgemaine Lourens:** All right.

**Tim Lisiecki:** Thanks all.

**Joery Van Druten:** Bye.

**Joery Van Druten:** Bye.
