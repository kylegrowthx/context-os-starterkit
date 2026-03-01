# Alex <> Growth X - Weekly Sync

<metadata>
date: 2026-01-27
time: 18:30 UTC
duration: 25 minutes
organizer: Team GrowthX (team@growthxlabs.com)
participants:
  - Carly Piekos (carly@growthx.ai, GrowthX)
  - Donald Donckers (don@alex.com, Alex)
source: fathom
fathom_recording_id: 117535455
fathom_url: https://fathom.video/calls/544435737
share_url: https://fathom.video/share/ddKFzbiLUGoPaaP4Vm4zyhwUWaMeKAyR
enriched_on: 2026-02-28 00:00 UTC
</metadata>

---

## Summary

Carly presented urgent technical SEO audit findings and content publishing status. Critical issues blocking site growth include missing robots.txt configuration (currently using LLM.txt instead), schema implementation errors, and 404 redirects. To restore momentum, Donald must approve 11 ready-to-publish articles and fix five priority technical issues this week. Next meeting will feature a demo of the new "Check That" citation tracking tool.

---

## Context

Alex AI is competing in the AI recruiting space against well-established players like Eightfold and Paradox. Over the past quarter (October-December 2025), the site saw strong momentum with consistent publishing and branded keyword rankings (AI recruiter, Alex AI interviewer both now rank #1). However, publishing paused in December, causing visibility to drop from 15% to 13.9% for non-branded keywords. The team discovered that site health issues—particularly misconfigured robots.txt and schema markup—are preventing crawlers from properly indexing pages, which is directly hurting rankings. Fixing technical SEO is critical since Alex has lower domain authority than competitors and must optimize every ranking signal.

---

## Relevance

- **SEO Performance**: Tracking keyword visibility and competitive positioning (Alex at 3.2 vs. Eightfold and Paradox higher). Non-branded keyword drop from 15% to 13.9% correlates with publishing pause.
- **Technical SEO**: Screaming Frog audit identified five critical issues: robots.txt misconfiguration blocking JS/images, schema stuffing (Organization on all pages), 404s wasting crawl budget, non-indexable pages in sitemap, missing H1 tags and alt text.
- **Content Pipeline**: 11 articles queued for publication; Carrie already made requested revisions and added internal linking for target keywords. Approval needed to resume publishing rhythm.
- **Tooling**: CheckThat (internal CheckThat tool) will replace Scrunch reports for more granular LLM citation tracking with 45-day window.

---

## Overview

- **Urgent Technical Fixes:** Critical issues are blocking growth. The `robots.txt` file is missing (an `LLM.txt` is being used instead), causing crawlers to block essential site resources like JavaScript and images.
- **Content Stagnation:** Publishing paused in December, causing a growth slowdown. 11 ready-to-publish articles are awaiting review to restore momentum.
- **Keyword Progress:** Branded keywords are strong (`AI recruiter`, `Alex AI interviewer` rank #1), which is a key step toward ranking for high-volume, non-branded terms.
- **New Reporting Tool:** Next week, Carly will demo "Check That," a new tool for more granular LLM citation tracking, replacing the current "Scrunch" reports.

---

## Key Topics

### SEO Performance & Content Stagnation

- **Growth Slowdown:** Publishing paused in December, causing a growth slowdown and slight drop in non-branded keyword visibility (from 15% to 13.9%).
- **Branded Keyword Success:**
    - `AI recruiter` → Ranks #1
    - `Alex AI interviewer` → Ranks #1 (improved from ~50th)
- **Content Pipeline:** 11 articles are ready for review. Publishing them will restore growth momentum and build internal link authority for keywords like `AI recruiter` and `AI interview`.

### Urgent Technical SEO Audit (Screaming Frog)

- **Problem:** The site is using an `LLM.txt` file instead of a standard `robots.txt`.
- **Impact:** Crawlers are blocking essential resources (JS, images), which prevents proper page rendering and indexing.
- **Solution:** Create a standard `robots.txt` and separate the `LLM.txt` file.

### Other Technical Issues

- **Schema Implementation:**
    - `Organization` schema is incorrectly applied to all pages; it must be homepage-only.
    - `Product` schema must be specific to product pages.
- **404 Errors:** Numerous 404 pages are wasting crawl budget and must be redirected (301) to the main blog page.
- **Sitemap Issues:**
    - The auto-generated Webflow sitemap includes non-indexable URLs.
    - Carly will investigate how to remove them.
- **Non-Indexable Pages:** Staging, demo, and old homepage URLs are indexable and must be set to `noindex`.
- **Missing Elements:** Several pages are missing H1 tags and image alt text.

---

## Action Items

**Donald Donckers (Alex)**
- Fix robots.txt: separate LLM.txt, allow JS/CSS/images, add LLM.txt allow/disallow
- Review 11 articles; approve for publish
- Fix paid ad: stop sponsored homepage showing for product queries
- Implement 301s for 404s to blog
- Fix schema: remove Organization from non-homepage; apply Product on product pages
- Set noindex on old homepage, landing/demo, staging; then remove from sitemap

**Carly Piekos (GrowthX)**
- Investigate AI recruiter rank history; report to Donald
- Investigate Webflow sitemap control; advise Donald on removing non-indexable URLs
- Send Donald Screaming Frog 5-issue summary + fix steps
- Demo Check That tool next week

---

## Transcript

**Carly Piekos (GrowthX):** I'm good, how are you?

**Donald Donckers (Alex):** I'm doing good, I'm doing good.

**Carly Piekos:** All right, let me pull up the agenda.

**Carly Piekos:** I want to share my screen.

**Carly Piekos:** Can you see my screen?

**Donald Donckers:** Yes.

**Carly Piekos:** Okay, perfect.

**Carly Piekos:** So I took some screenshots of before and after.

**Carly Piekos:** We did it.

**Donald Donckers:** We did it.

**Donald Donckers:** Yeah, we did it.

**Carly Piekos:** Finally.

**Carly Piekos:** So I'm happy to have helped in whatever way I did.

**Carly Piekos:** So it is now consolidating all of the URLs, which is fabulous.

**Carly Piekos:** That means you are ranking for your brand officially.

**Carly Piekos:** This is going to help your overall visibility, and this will definitely help push towards that non-branded AI recruiter keyword.

**Carly Piekos:** So I'm very excited about that.

**Carly Piekos:** So I did the Screaming Frog technical audit.

**Carly Piekos:** So these are kind of urgent.

**Carly Piekos:** What I noticed in your robots is you have an LLM text file in lieu of a robots.txt file, and those need to be separate.

**Carly Piekos:** So we need a robots, and then we can connect an LLM text file, maybe within, like, allow to crawl, and then we have a separate LLM text file for that.

**Donald Donckers:** All right, right, right.

**Donald Donckers:** Okay, let me, let me, I updated the robots.txt file last night, actually.

**Donald Donckers:** So I'll take another look at it and get those two separated, the LLM text and the robots.txt file.

**Carly Piekos:** I mean, I have an outline for you, but I don't know, you already said you built it out?

**Donald Donckers:** Yesterday night, I, like, had it rewrote the robots.txt file, but I'd, like, I'll take another look at it.

**Donald Donckers:** It might not have been, I just had it updated based on what it, when did you do this Screaming Frog audit?

**Carly Piekos:** I did it on Friday.

**Donald Donckers:** Friday, okay.

**Donald Donckers:** Let me take a look at it.

**Donald Donckers:** It might be solved already.

**Carly Piekos:** Here, what I can do is, what I can do, I'll just rerun it right now.

**Carly Piekos:** They gave me access to the Screaming Frog, so I'm very excited about this.

**Carly Piekos:** Giving nerd energy.

**Carly Piekos:** So, I'll wait until it's crawled, and then it should be done by the end of this call.

**Carly Piekos:** So, we'll go over that in a second.

**Carly Piekos:** The schema issues, it wasn't implemented correctly, so I've created some schema templates for you to put on specific pages.

**Carly Piekos:** Just remember that organizational, and I'll put it in the notes here, organizational schema should only be on the homepage.

**Carly Piekos:** And then the schema, the product schema that you put on there should only be on product pages.

**Donald Donckers:** Got it.

**Donald Donckers:** Got it.

**Donald Donckers:** Got it.

**Donald Donckers:** Okay, perfect.

**Donald Donckers:** That's good to know.

**Carly Piekos:** Yeah.

**Carly Piekos:** So we just want to make sure that that is the case.

**Carly Piekos:** You have 11 articles ready for review.

**Donald Donckers:** Perfect.

**Donald Donckers:** I'll look at them tomorrow.

**Carly Piekos:** These need to just like a glance because Carrie already made the adjustments and she already put everything in and reran everything based on the information that you gave her a few weeks ago.

**Carly Piekos:** So they are ready to go.

**Carly Piekos:** All you have to do is take a glance and just make sure she did the things that she said she was going to do to the articles before I started.

**Carly Piekos:** And then just give them the go-ahead because the last time we published was in December and that is affecting the overall growth of the website.

**Carly Piekos:** But not only that, the internal links are really important for us to get in there.

**Carly Piekos:** She did rerun it to include those internal links for AI recruiter and AI interview.

**Carly Piekos:** So we just want to make sure that we are publishing regularly.

**Carly Piekos:** Otherwise, we're going to see drops like we saw this week.

**Donald Donckers:** Yeah, it's like stagnated because we're not publishing since December.

**Carly Piekos:** Right.

**Carly Piekos:** All right.

**Carly Piekos:** Yeah.

**Carly Piekos:** So it's kind of going down just a little bit.

**Carly Piekos:** So we want to make sure we keep the momentum, a rolling stone gathers moss type of thing.

**Carly Piekos:** So we, and your content by the pillars, they've gone down in engagement a little bit.

**Carly Piekos:** So we just want to make sure that we're continuing to publish within these pillars.

**Carly Piekos:** But you did see, you're still seeing growth.

**Carly Piekos:** You're just not seeing the amount of growth that you have been seeing since we started back in October and we were like consistently publishing.

**Carly Piekos:** So that is, but your positioning has gone up by 1% here.

**Carly Piekos:** So that's great.

**Carly Piekos:** Alex is actually at 3.2 as of January 19th.

**Carly Piekos:** So the average is 3, but you're at 3.2 right here with competitive performance.

**Donald Donckers:** I did see.

**Donald Donckers:** Can I see up there?

**Donald Donckers:** Yeah.

**Donald Donckers:** The other ones are growing much better, like Eightfold and Paradox.

**Carly Piekos:** Is this on the right date?

**Carly Piekos:** Hold on.

**Carly Piekos:** Just want to make sure.

**Carly Piekos:** Yes.

**Carly Piekos:** Okay.

**Carly Piekos:** 3.2.

**Carly Piekos:** 3.2.

**Carly Piekos:** There we go.

**Carly Piekos:** For that week.

**Donald Donckers:** Yeah.

**Donald Donckers:** Okay.

**Donald Donckers:** So the other, like, Eightfold and Paradox, you're really doing well.

**Carly Piekos:** Yes.

**Carly Piekos:** And one of the main reasons you have a bit lower visibility is because of these technical errors.

**Carly Piekos:** Okay.

**Carly Piekos:** So I it's almost done crawling, so I can kind of run through what this looks like on our end, like what's, what's wrong, how we fix it.

**Carly Piekos:** And if we can get that fixed this week, along with those articles published, I don't think that you'll have anything standing in your way to grow exponentially in the next couple of weeks.

**Carly Piekos:** Okay.

**Carly Piekos:** No one, no one really considers like how site health plays into this.

**Carly Piekos:** Yes, you can produce all the content you want, but if your site's not in at least like 90% health and all of your competitors have that, and I mean, I can technically check all of your competitors' site health too to see where they are at.

**Carly Piekos:** But I just want to make sure that we are doing the most, just because your brand has like a lower brand authority across the board than any of your competitors.

**Carly Piekos:** So we have to kind of make up for it in other ways.

**Carly Piekos:** These are for your non-branded prompts.

**Carly Piekos:** If I were to filter out of this and also include your branded prompts, you are growing from 12 and now you're at 13.9.

**Carly Piekos:** Last week, you were at 15, the week before you were at 15.

**Carly Piekos:** So the more we publish, the more it will grow and grow and grow.

**Carly Piekos:** So the positioning when you are considering branded, you're at 81, sentiment 96%.

**Carly Piekos:** So I'm not sure if you just want to look at non-branded always.

**Carly Piekos:** Next week, I'll be demoing our version of Scrunch.

**Carly Piekos:** It's called Check That.

**Carly Piekos:** So I'll be going through how we will, it's basically just like Scrunch.

**Carly Piekos:** But we are able to add more prompts.

**Carly Piekos:** We are able to, we have like a 45-day window, which we can report within.

**Carly Piekos:** And we're able to see more citations per LLM model.

**Carly Piekos:** It's just like a bit more visibility into everything.

**Carly Piekos:** So once we go through Check That this week.

**Carly Piekos:** Oh, that's not this one.

**Carly Piekos:** That is not the thing.

**Carly Piekos:** I will run through that next week with you.

**Carly Piekos:** Let me see this.

**Carly Piekos:** Okay.

**Carly Piekos:** So ranking number one, this is fabulous.

**Carly Piekos:** You're ranking number one for AI recruiter and Alex AI interviewer.

**Carly Piekos:** I have to put Alex.

**Carly Piekos:** So branded, you're ranking number one for both of those, which is really, really good.

**Carly Piekos:** That means that you are more likely to rank for these individually as a non-branded term.

**Carly Piekos:** So once we get the branded as that long tail keyword, we're more likely to rank for AI recruiter, AI interviewer in the long run.

**Carly Piekos:** So you will also have an AI overview and you're being cited right here.

**Carly Piekos:** And this is all just because of a few technical changes, a few meta descriptions and titles and H1s being changed over the past few weeks.

**Donald Donckers:** Weren't we ranking for Alex AI recruiter before?

**Donald Donckers:** I thought we were.

**Donald Donckers:** I thought it was just like AI recruiter.

**Carly Piekos:** That's the one that we care about.

**Carly Piekos:** You were not ranking number one for it.

**Carly Piekos:** You were ranking, let see, a few weeks ago.

**Carly Piekos:** Actually, I don't have that report up right now, but I can look into and tell you exactly where you were a few weeks ago.

**Carly Piekos:** I know that for AI interviewer, you went from 90 to 50.

**Carly Piekos:** 50 in, like, this two-week period.

**Carly Piekos:** Okay.

**Donald Donckers:** AI interviewer or AI recruiter?

**Carly Piekos:** AI interviewer.

**Donald Donckers:** Okay, perfect.

**Carly Piekos:** I'm looking into AI recruiter.

**Carly Piekos:** That's a little bit further back because it's a higher volume keyword.

**Carly Piekos:** So we just have to make sure that we're just keeping an eye on that.

**Carly Piekos:** But I am tracking the keywords to make sure that it's moving forward.

**Carly Piekos:** Do you have any questions for me?

**Donald Donckers:** No major questions, just, like, what are the changes?

**Donald Donckers:** So we made, we published a bunch of new pages yesterday and, like, some site updates yesterday as well.

**Donald Donckers:** And so there were some issues that I'd noticed yesterday with, like, these changes.

**Donald Donckers:** But I've already updated it and I submitted it to the search console.

**Donald Donckers:** So, we keep seeing, like, whenever I go into Search Console, certain pages, like our AI interviewer page and our coordinator or verify page, they don't show up in Search.

**Donald Donckers:** Like, whenever I put them in in Search Console, they say that they're not indexed by Google.

**Carly Piekos:** Okay, let me pull that up real fast.

**Carly Piekos:** Not it.

**Donald Donckers:** I can show you.

**Carly Piekos:** Yeah, if you want to, yeah, if you want to show me while I'm pulling this up.

**Carly Piekos:** Okay.

**Donald Donckers:** So okay.

**Donald Donckers:** So okay.

**Donald Donckers:** Okay.

**Donald Donckers:** So here you can see I put in alex.ai interviewer, right?

**Carly Piekos:** I don't know why this is showing.

**Carly Piekos:** Oh, that's a sponsored result.

**Carly Piekos:** That's also what I wanted to bring up.

**Carly Piekos:** That's a sponsored result.

**Carly Piekos:** So it's showing up differently because it's sponsored.

**Carly Piekos:** So whoever's in charge of the paid campaign just needs to make an adjustment.

**Donald Donckers:** Yeah.

**Donald Donckers:** I turned off the specific campaigns.

**Carly Piekos:** I'm not sure why this is still showing here.

**Donald Donckers:** So, yeah, this is just like the homepage, right?

**Donald Donckers:** It's not going to this page, which you would think it would be, right?

**Donald Donckers:** Like you would go to this page and then when I go in here and I type in interviews.

**Carly Piekos:** Oh, that's on Google.

**Donald Donckers:** Yeah.

**Donald Donckers:** Yesterday it wasn't.

**Donald Donckers:** Let me do this one.

**Donald Donckers:** Yes, yes, finally.

**Donald Donckers:** Yay, we were getting there. Yesterday it was not there.

**Donald Donckers:** Oh, my God, this took forever.

**Donald Donckers:** Yeah.

**Donald Donckers:** Yes.

**Donald Donckers:** What we did is, though, like, we have now on the homepage, I think, I wonder if this has to do with it.

**Donald Donckers:** I submitted, I turned off the sitemap and I resubmitted it.

**Donald Donckers:** And then I also, on the homepage, we now have these links that go to the individual products.

**Carly Piekos:** Okay, AI interviews, yep.

**Donald Donckers:** Perfect.

**Donald Donckers:** This channel, this is video, so this is Verify, Coordinator, and then Residence Greens.

**Donald Donckers:** That looks great.

**Donald Donckers:** All right.

**Carly Piekos:** That looks great.

**Donald Donckers:** Okay.

**Carly Piekos:** Okay.

**Carly Piekos:** Okay.

**Carly Piekos:** Good.

**Donald Donckers:** Good.

**Donald Donckers:** Getting there.

**Carly Piekos:** Let me share my screen real fast because the audit is reran.

**Carly Piekos:** Okay.

**Carly Piekos:** All right.

**Donald Donckers:** Can you see my screen?

**Carly Piekos:** Yes.

**Carly Piekos:** All right.

**Carly Piekos:** So these are the main issues right here.

**Carly Piekos:** These are the response codes.

**Carly Piekos:** And I can send you over a summary of what it is and how to fix it.

**Carly Piekos:** But these are all of the pages that have 404s.

**Carly Piekos:** We, if you do not want these pages to exist, we just need to redirect them back to the blog in general.

**Donald Donckers:** Okay.

**Carly Piekos:** We can do that.

**Carly Piekos:** So let's, yeah.

**Carly Piekos:** Just so we're not wasting your crawl budget.

**Carly Piekos:** And then we have the results.

**Donald Donckers:** I updated a sitemap, so they should get removed, right?

**Donald Donckers:** Or is that not enough?

**Carly Piekos:** No, you need to redirect the pages because even though they're not on the sitemap anymore.

**Carly Piekos:** Or any 404 you need to redirect to another type, just the blog page.

**Carly Piekos:** Then it'll be a 301 redirect and you'll be fine.

**Carly Piekos:** This right here are the pages that have the structured data.

**Carly Piekos:** Right now they have one error and one warning.

**Carly Piekos:** Unfortunately, I don't have what errors or warnings it has.

**Carly Piekos:** It just means that something's wrong with the way it was configured.

**Carly Piekos:** So you have your FAQ.

**Carly Piekos:** This one is on alex.com.

**Carly Piekos:** Perfect.

**Carly Piekos:** Breadcrumbs, answers, FAQs, image, object, list item.

**Donald Donckers:** You select one, is it also not showing?

**Carly Piekos:** Your organization.

**Carly Piekos:** So this one, we need to get rid of this on all of the pages.

**Donald Donckers:** It only should exist on the homepage.

**Donald Donckers:** This is the JSON issue.

**Donald Donckers:** Can you click on one so I can see what's in it?

**Donald Donckers:** Just click on one instead of selecting the entire list.

**Donald Donckers:** Hold on.

**Donald Donckers:** Can you go back to where you had the organization?

**Carly Piekos:** Yes.

**Donald Donckers:** There we go.

**Donald Donckers:** Click it.

**Donald Donckers:** So what's the issue?

**Carly Piekos:** The issue is there are this organization is not supposed to be on anything but the homepage and it's on Talent Match.

**Carly Piekos:** It's on all of the other pages.

**Carly Piekos:** So it's basically blanketing across the board.

**Donald Donckers:** So we only want to...

**Carly Piekos:** There's some dash LB file, right?

**Carly Piekos:** Yes.

**Carly Piekos:** So we just want to make sure that it's on, the organization's only on one page, that when we're doing, like, the, like, software app, or if we're doing, like, product schema, that it's only on those app pages, or product schema pages, because Google will ding you for not having the correct schema on those pages.

**Carly Piekos:** Got it.

**Carly Piekos:** Yeah, it's kind of like, I guess, I don't know.

**Carly Piekos:** Keyword stuffing, if you would, like, schema stuffing.

**Carly Piekos:** What else do we have?

**Carly Piekos:** We have security HTTPS.

**Carly Piekos:** That's fine.

**Carly Piekos:** Sitemaps, not indexable URLs in the sitemap.

**Carly Piekos:** So we just, if these are not supposed to be in the sitemap, we need to just remove them from this.

**Donald Donckers:** Okay.

**Donald Donckers:** The sitemap is auto-generated by Webflow right now.

**Donald Donckers:** So what do I do then?

**Donald Donckers:** Just like copy it and manually remove it, like copy the auto-generated sitemap and just remove these?

**Carly Piekos:** If it's auto-generated, should have, maybe it just adds, when you add a page.

**Carly Piekos:** Did you set up the auto-generation?

**Donald Donckers:** It's like by def, it's just Webflow.

**Donald Donckers:** It's like by default, it's just Webflow.

**Carly Piekos:** So Webflow just automatically, dynamically updates it?

**Donald Donckers:** Yeah, like based on the settings.

**Carly Piekos:** Okay.

**Carly Piekos:** I'll look into it and see how we can remove from the sitemap.

**Carly Piekos:** And then we just need to, this one's redirected.

**Carly Piekos:** This one is canonicalized, but this is your old homepage.

**Carly Piekos:** I would just redirect this.

**Donald Donckers:** Oh, I just got.

**Carly Piekos:** I'll just kill that.

**Carly Piekos:** And kill it.

**Carly Piekos:** Yeah, index.

**Carly Piekos:** Like, no index it.

**Donald Donckers:** And then this one, too.

**Donald Donckers:** Okay.

**Carly Piekos:** We don't want these to be indexable, right?

**Carly Piekos:** Not landing demo.

**Carly Piekos:** And definitely not this.

**Donald Donckers:** Correct?

**Donald Donckers:** Yeah, you can, like, not make that index.

**Donald Donckers:** I'll, I need to flag this with the engineers.

**Donald Donckers:** This is.

**Carly Piekos:** I'll print a report out for you.

**Carly Piekos:** So that way you have, like, a whole list of the things.

**Carly Piekos:** H1s are missing.

**Carly Piekos:** That's this one.

**Carly Piekos:** This page is also indexable.

**Carly Piekos:** We want to make sure that that's not.

**Carly Piekos:** Missing alt text.

**Carly Piekos:** It's all of these.

**Carly Piekos:** What do you think are just staging files?

**Carly Piekos:** Okay.

**Carly Piekos:** I'm missing...

**Carly Piekos:** Okay.

**Carly Piekos:** So that's low.

**Carly Piekos:** Warnings.

**Carly Piekos:** So this is JavaScript pages that are blocked resources.

**Carly Piekos:** If we click on...

**Donald Donckers:** What does that mean?

**Donald Donckers:** Blocked resources.

**Carly Piekos:** So like images, JavaScript, they're blocked by rendering from your robots.

**Carly Piekos:** So that's why we have to get your robots up to date, because right now it's crawling the LLM TXT instead of the robots TXT.

**Carly Piekos:** Okay.

**Carly Piekos:** So it's being blocked.

**Carly Piekos:** So like anything, any JavaScript you have on your site, images, they're being blocked from crawlers.

**Carly Piekos:** So there's a lot that are being no indexed.

**Carly Piekos:** Then you have these ones, which I don't think are index nofollow.

**Carly Piekos:** I think those are fine.

**Carly Piekos:** Or you want me to kind of, like, I haven't had a chance to, like, look through the articles since Carrie has written them.

**Carly Piekos:** So I'm happy to help in any way I can take some stuff off your plate.

**Donald Donckers:** Sounds good.

**Carly Piekos:** All right.

**Carly Piekos:** That's all I really had today.

**Carly Piekos:** So let me know if you need anything before our next meeting.

**Carly Piekos:** I'm going to send you an update on Monday.

**Carly Piekos:** We will be going through Check That.

**Carly Piekos:** And I will send over the Screaming Frog 5-issue summary.

**Carly Piekos:** Did you just want the main issues?

**Donald Donckers:** Just, like, the five main issues.

**Carly Piekos:** Yeah, exactly.

**Carly Piekos:** I'll send those over.

**Carly Piekos:** Okay.

**Carly Piekos:** Perfect.

**Carly Piekos:** All right.

**Carly Piekos:** All right, Don.

**Carly Piekos:** Have a great week.

**Donald Donckers:** Bye.

**Donald Donckers:** You too.

**Donald Donckers:** Have a good week.

**Donald Donckers:** Bye.
