# Vizcom <> Growth X - Kaelan / Carly GSC Troubleshoot Session

<metadata>
date: 2026-01-09
time: 19:03 UTC
duration: 7 minutes
organizer: carly@growthx.ai
participants: Andreina Coronado, Kaelan Richards, Carly Piekos
fathom_recording_id: 113181669
fathom_url: https://fathom.video/calls/526030223
share_url: https://fathom.video/share/ru1XoZZPBxb79wm6bc-RpnbXKNF-oDGR
source: fathom
enriched_on: 2026-02-28T14:35:00Z
</metadata>

---

## Summary

Carly diagnosed and resolved a Google Search Console indexing issue for Vizcom's migrated site (Framer to Webflow). The migration changed the URL structure from `https://vizcom.com` to `https://www.vizcom.com`, causing GSC to report zero indexed pages. A live GSC URL Inspection forced Google to crawl the new URL, making the page "available on Google" and confirming the URL change was the root cause.

---

## Context

Vizcom recently migrated their website from Framer to Webflow and encountered an indexing issue that prevented the site from appearing in Google Search results. Carly identified that GSC was still tracking the old URL (without the www prefix) while the migrated site had changed to include www. During this troubleshooting session, Carly walked Kaelan through the GSC interface, confirming that 301 redirects were correctly implemented and demonstrating how a direct URL Inspection request immediately resolved the indexing status. The session concluded with Carly committing to contact Emily or Mara on the marketing team to verify that Webflow's indexing settings are configured correctly for all pages on the site.

---

## Relevance

- Client is Vizcom, an external company (vizcom.com domain)
- **Primary contact:** Kaelan Richards (Vizcom, kaelan@vizcom.com)
- **GrowthX side:** Carly Piekos (carly@growthx.ai, organizer)
- Related to SEO/AEO work and technical site migrations
- Demonstrates GrowthX's capability to troubleshoot and resolve indexing issues quickly
- Actionable outcomes for both Vizcom (confirm Webflow settings) and GrowthX (monitor GSC performance)

---

## Overview

- **Problem:** A site migration from Framer to Webflow broke Google indexing by changing the URL from `https://vizcom.com` to `https://www.vizcom.com`.
- **Solution:** A live GSC URL Inspection fixed the immediate issue by forcing Google to crawl the new URL, making the page "available on Google."
- **Action:** Carly will contact the marketing team (Emily/Mara) to confirm Webflow's indexing settings are correct for the entire site.

---

## Key Topics

### Problem: Site Migration Breaks Indexing

  - A site migration from Framer to Webflow broke Google indexing by changing the URL from `https://vizcom.com` to `https://www.vizcom.com`.
  - **Impact:** GSC reported zero indexed pages, preventing the site from appearing in search results.
  - **Positive:** The migration correctly implemented 301 redirects, preserving SEO value from old URLs.

### Solution: Live GSC URL Inspection

  - Carly's live GSC URL Inspection fixed the immediate issue by forcing Google to crawl the new URL.
  - **Outcome:** The page was successfully fetched and became "available on Google," confirming the URL change was the root cause.

---

## Action Items

**Carly Piekos (GrowthX)**
- Email Emily/Mara (Vizcom marketing team) to confirm Webflow indexing settings are correct for all pages
- Resubmit sitemap in Google Search Console on Monday to accelerate crawling
- Monitor performance data and report any new GSC issues to Kaelan

---

## Transcript
**Kaelan Richards:** Hello.

**Carly Piekos:** This meeting is being recorded.

**Kaelan Richards:** How's it going?

**Carly Piekos:** It's good.

**Carly Piekos:** How's everything going with you?

**Kaelan Richards:** Good.

**Kaelan Richards:** Sorry I have to be off camera.

**Kaelan Richards:** I'm on my phone right now, but yeah, nice to meet you.

**Carly Piekos:** Nice to meet you, too.

**Carly Piekos:** So I noticed something today when going on the vizcom site, the URL changed.

**Kaelan Richards:** Are you aware of this?

**Kaelan Richards:** From what?

**Carly Piekos:** From HTTPS to HTTPS www dot.

**Kaelan Richards:** Oh, interesting.

**Kaelan Richards:** We did just switch over our site yesterday.

**Carly Piekos:** Oh, you did.

**Kaelan Richards:** Okay.

**Carly Piekos:** Yeah.

**Carly Piekos:** So the Google search console wasn't picking up on it because it didn't have the www.

**Carly Piekos:** But now that it's the HTTPS, I believe it's...

**Carly Piekos:** Starting to pick up on some pages.

**Kaelan Richards:** Okay.

**Kaelan Richards:** Nice.

**Carly Piekos:** So that's good.

**Carly Piekos:** But I mean, obviously it was just yesterday.

**Kaelan Richards:** So hold on.

**Kaelan Richards:** Let me just make sure.

**Kaelan Richards:** Okay.

**Carly Piekos:** I'm just looking at.

**Carly Piekos:** Are you going to be able to see my screen if I share?

**Kaelan Richards:** Yeah.

**Carly Piekos:** Okay, cool.

**Carly Piekos:** All right.

**Carly Piekos:** Can you see my screen?

**Carly Piekos:** Hold on one second.

**Carly Piekos:** There?

**Kaelan Richards:** Yes, I can see.

**Carly Piekos:** All right.

**Carly Piekos:** Perfect.

**Carly Piekos:** Okay.

**Carly Piekos:** So when I'm looking at the site, this is the vizcom site right now.

**Carly Piekos:** And I just want to do, and it looks like you redirected all the pages.

**Carly Piekos:** I'm is

**Carly Piekos:** Which is good if you changed the site yesterday.

**Carly Piekos:** So now it's the Make It Real site.

**Carly Piekos:** Okay.

**Carly Piekos:** So the issue was it was the www before.

**Carly Piekos:** But now the referring page, this is kind of odd that the referring page is whatever this is.

**Carly Piekos:** Is this the staging site?

**Kaelan Richards:** No, this is the real site.

**Kaelan Richards:** Maybe they forgot to fix something here.

**Carly Piekos:** Okay.

**Kaelan Richards:** Let's switch from framer to webflow.

**Carly Piekos:** Okay, got it.

**Carly Piekos:** If I'm looking at the pages, it's saying that none of the pages are indexed.

**Carly Piekos:** So this is one thing in order to be found, obviously, we have to do.

**Carly Piekos:** Maybe we need to resubmit the sitemap.

**Carly Piekos:** sitemap.

**Carly Piekos:** Okay.

**Carly Piekos:** We

**Carly Piekos:** It's not saying anything about Core Web Vitals.

**Carly Piekos:** Let's see if there's a performance.

**Carly Piekos:** Well, it's showing up.

**Carly Piekos:** At least this part is showing up.

**Carly Piekos:** So that's good.

**Carly Piekos:** You're not going to have any performance though because pages aren't indexing.

**Carly Piekos:** So I'm not sure if you can check on that and make sure that in Webflow that the pages are actually indexed.

**Carly Piekos:** Do you have, let me see the site.

**Carly Piekos:** Okay.

**Carly Piekos:** So I submitted this site map on January 5th.

**Carly Piekos:** The status is a success.

**Carly Piekos:** So that's good.

**Carly Piekos:** I didn't even realize it was going to change to this specifically.

**Carly Piekos:** So that's, I'm pretty happy that that is the case.

**Carly Piekos:** Let me just grab this real real fast.

**Carly Piekos:** Okay, so it's not indexing.

**Carly Piekos:** We're going to request indexing here.

**Carly Piekos:** And the page was able to be fetched, so that's good.

**Carly Piekos:** So this kind of fixed the problem that we made this call for anyway.

**Carly Piekos:** Okay.

**Kaelan Richards:** So my only suggestion would be to make sure that the pages are indexed.

**Kaelan Richards:** Yeah, I don't really have too much context with Webflow, so you might have to reach out to Emily for that.

**Carly Piekos:** Okay, got you.

**Carly Piekos:** And she might be...

**Carly Piekos:** She might be...

**Kaelan Richards:** Or, yeah, Emily or, you know, Mara or whoever else on the marketing team.

**Carly Piekos:** Okay.

**Carly Piekos:** What I'll do, I'll reach out to them to make sure that the pages are going to be indexed.

**Carly Piekos:** If I have any more issues with the Google Search Console or anything changes, I will let you know.

**Kaelan Richards:** Yeah, let me know.

**Carly Piekos:** I just got to make sure that these are being, ah, there you go.

**Kaelan Richards:** See?

**Carly Piekos:** You are now available on Google.

**Carly Piekos:** So hopefully we'll pick up some performance over the weekend.

**Carly Piekos:** Okay.

**Carly Piekos:** Let's just test.

**Carly Piekos:** I'll resubmit it on Monday and see.

**Carly Piekos:** The more we resubmit, the better.

**Carly Piekos:** So it'll just, it'll be crawled more.

**Carly Piekos:** So hopefully you'll see some of the information on Monday.

**Kaelan Richards:** Okay, awesome.

**Carly Piekos:** All right.

**Carly Piekos:** Do you have any questions for me while we're here?

**Kaelan Richards:** No.

**Kaelan Richards:** I think I'm all good.

**Kaelan Richards:** I'm glad that it was resolved even before the call.

**Carly Piekos:** So, yeah, I was able to get that done.

**Carly Piekos:** All right.

**Carly Piekos:** Wonderful.

**Carly Piekos:** If I have anything or anything pops up, I will reach out.

**Kaelan Richards:** Okay.

**Kaelan Richards:** Thank you so much.

**Kaelan Richards:** All right.

**Kaelan Richards:** Thank you.

**Kaelan Richards:** Have a good one.

**Kaelan Richards:** You too.

**Kaelan Richards:** Bye.

**Kaelan Richards:** Bye.
