# Impromptu Google Meet Meeting

<metadata>
date: 2025-12-03
time: 11:33 UTC
duration: 64 minutes
organizer: matthew.alves-hill@growthx.ai
participants: Matthew Alves-Hill, Israel Beni
fathom_recording_id: 105868273
fathom_url: https://fathom.video/calls/495068324
share_url: https://fathom.video/share/zzmRVMUY6qGoEygT66sa_EbSHLGxrsuM
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Diagnose and plan a fix for the Inner World blog's broken URL structure.

---

## Context

Matthew Alves-Hill (GrowthX) met with Israel Beni, an external SEO specialist, to diagnose critical indexing failures on Inner World's blog. Inner World is a GrowthX client paying for organic traffic performance. The meeting was prompted by Matthew's discovery that none of the blog articles published in the past month are being indexed by Google, despite GrowthX staging and optimizing the content. Matthew needed expert SEO perspective to understand the root cause and develop a fix strategy before presenting recommendations to Jacob (Inner World's technical contact) and the Inner World leadership team later that day.

---

## Relevance

**To GrowthX Delivery:**
- Inner World's developer (Ilya) implemented an outdated categorization feature (Aug/Sep plan) without coordinating with the new URL strategy agreed to in October. This lack of internal communication at the client has directly caused the blog indexing failure, suggesting GrowthX needs clearer communication protocols with clients about technical dependencies.
- The Prismic routing feature creates duplicate URLs (`/reflections/[slug]` and `/[category]/[slug]`), requiring a code-level fix, not a redirect solution. This is a lesson in reviewing client infrastructure for SEO compliance before staging content.
- The outdated sitemap is not synced with the live site structure. Updating the sitemap alone won't fix the routing issue but will minimize indexing damage by signaling URL changes to Google.

**To GrowthX Business Development:**
- Inner World's account health is at risk. The client is paying for organic performance but receiving none due to self-inflicted technical damage. This is a critical renewal conversation requiring clear accountability and a technical fix timeline.
- Three articles staged by GrowthX on Oct 31 were never published by Inner World, indicating additional miscommunication and process gaps on the client side. Matthew is tracking this to separate GrowthX's delivery from client execution failures.
- The technical complexity of the fix (code change vs. redirect) and the client's apparent lack of technical oversight (developer implementing outdated plans) may require GrowthX to be more hands-on in validation before staging content.

---

## Overview

- **Broken URLs Block Indexing:** A Prismic routing feature creates two URLs for each blog (e.g., `/reflections/title` and `/category/title`), confusing Google and preventing new articles from indexing.
- **Outdated Sitemap Compounds Damage:** The sitemap is not synced with the live site, failing to signal URL changes and further delaying Google's discovery of new content.
- **Immediate Fix:** The Prismic routing logic must be removed. This requires a code change, not a manual redirect, as the issue is in the application's routing layer.
- **Client Communication Failure:** Inner World's internal communication failure between the SEO team and developer Ilya caused this issue. The developer implemented an outdated plan (from Aug/Sep) despite a new, simpler URL structure being agreed upon in October.

---

## Key Topics

### Problem: Broken Blog URLs & Indexing

  - **Root Cause:** A Prismic feature, implemented by developer Ilya, automatically adds a category slug to blog URLs.
  - **Result:** This creates two live URLs for every article, breaking the intended `/reflections/blog-title` structure.
  - **Impact:** Google is confused by the multiple paths and has stopped indexing new articles published in the last month.
  - **Compounding Factor:** An outdated sitemap fails to signal URL changes to Google, further delaying discovery and indexing.

### Diagnosis: Routing Logic & Indexing Behavior

  - **Mechanism:** The site's codebase contains two active routes for blog articles:
      - [`/reflections/[slug]` → The correct, intended path.](https://fathom.video/share/zzmRVMUY6qGoEygT66sa_EbSHLGxrsuM?tab=summary&timestamp=1085.0)
      - [`/[category]/[slug]` → The incorrect path created by the Prismic feature.](https://fathom.video/share/zzmRVMUY6qGoEygT66sa_EbSHLGxrsuM?tab=summary&timestamp=1228.0)
  - **Google's Behavior:**
      - Older articles (e.g., from Oct 31) were eventually indexed under the incorrect `/category/slug` path.
      - Newer articles (from Nov) are not indexing at all, likely due to the sitemap's failure to signal their existence or URL changes.
  - **Unpublished Articles:** Three articles staged by GrowthX on Oct 31 were never published by Inner World, explaining why they were not found in Google Search Console.

### Solution: Fix Routing & Sync Sitemap

  - **Priority 1: Fix Routing Logic**
      - **Action:** Remove the Prismic feature that adds the category slug.
      - **Method:** This is a code change to the application's routing logic, not a manual redirect.
      - **Rationale:** This eliminates the duplicate URLs and establishes a single, canonical path.
  - **Priority 2: Sync Sitemap**
      - **Action:** Update the sitemap to reflect the live site's correct URL structure.
      - **Rationale:** An accurate sitemap is critical for signaling changes to Google and accelerating the indexing of new content.

---

## Action Items

**Israel Beni (External SEO Specialist)**
- Review SEO standards, canonical tags, sitemap, and robots.txt configuration for Inner World's site
- Post a summary to Matthew via Slack with recommendations on: (1) fixing the Prismic routing feature, (2) updating the sitemap, and (3) any other SEO standards issues
- Matthew will then sync Jacob (Inner World's technical lead) with the findings and brief Inner World leadership (NOL) on the required technical fixes

---

## Transcript

**Matthew Alves-Hill:** Hey, Israel.

**Israel Beni:** Hello.

**Matthew Alves-Hill:** How are you doing?

**Israel Beni:** I'm good.

**Matthew Alves-Hill:** Another day, another NOL.

**Matthew Alves-Hill:** You don't have context here, but basically there was discussion, like, back in August and September around foldering the site in this way, the way that, like, the categorization makes sense.

**Matthew Alves-Hill:** So that's why that thing was implemented in the first place.

**Matthew Alves-Hill:** Although what's interesting is that discussion happened in early September, but it's only gone live in the middle of October, you're saying?

**Matthew Alves-Hill:** Yeah.

**Israel Beni:** Okay.

**Matthew Alves-Hill:** So that's weird, but I'm not surprised.

**Matthew Alves-Hill:** It seems like the InnoWorld team cannot communicate very well at all.

**Matthew Alves-Hill:** So initially that was the plan, and then we've changed it in recent months to be like, it just needs to be reflections and the blog title.

**Matthew Alves-Hill:** It's much more simple.

**Matthew Alves-Hill:** I have a question for you, like SEO-wise, I guess.

**Matthew Alves-Hill:** Okay.

**Matthew Alves-Hill:** This feature that adds the category and changes the URL, surely that would affect the ability for like the page to index if the URL is changed, right?

**Matthew Alves-Hill:** So...

**Israel Beni:** So...

**Matthew Alves-Hill:** Go on.

**Israel Beni:** Well, that's one point, but the damage in terms of issue could have been minimized if the sitemap is up-to-date, synced, right?

**Israel Beni:** As I pointed in, like, a couple of weeks ago in some of the findings with you, the sitemap is not up-to-date.

**Israel Beni:** And these are one of the tags that I will say those are priority.

**Israel Beni:** We have the sitemap is number one, and then we have the table, right?

**Israel Beni:** Because the sitemap that we have right now is telling a totally different story to Google, and Google on the website has totally different, you know, URL structures.

**Israel Beni:** Yeah.

**Matthew Alves-Hill:** Yeah, that makes sense.

**Matthew Alves-Hill:** So, can you...

**Matthew Alves-Hill:** Explain to me, like, again, like I'm five years old, why, like, if the sitemap was updated, why would this, I still don't understand that, like, how it could possibly work that the, that it would change the URL, because we're, like, we're publishing under one URL.

**Matthew Alves-Hill:** So if the sitemap is up to date, like, why does that fix this problem?

**Matthew Alves-Hill:** I don't really understand that.

**Israel Beni:** No, no, I'm not saying that, that we'll fix the problem.

**Israel Beni:** I'm saying it will minimize the damage, because at least it will reflect this page, the URL has been changed to this, because in the sitemap, we indicate, okay, the date, this page has been modified, you know, so Google can have an idea, okay, ah, all right, say this page was on this URL before, but now it's.

**Israel Beni:** On this URL, this change has happened at this moment, which is not synced in the sitemap as of now.

**Matthew Alves-Hill:** Right.

**Matthew Alves-Hill:** But even if the sitemap was up to date, we continue publishing with the `/reflections/[title]` structure, and then Prismic changes the URL by adding the category. It's always doing that — every time we publish new pages, we're going to always have this problem, right?

**Israel Beni:** To be honest, this fix is not a hard issue to fix. There's a logic in the routing pattern that he implemented for the blog cards on the blog page. The ones without `/reflections` in the URL are the affected ones. This affects articles published back in October, but I've even seen articles from June that have been affected by this code base change. Any articles that have a category field present will be affected.

**Matthew Alves-Hill:** Yeah, okay, what I'm trying to understand is whether this feature was implemented without any thought of SEO. Would that be fair?

**Israel Beni:** No, I don't want to judge people here.

**Matthew Alves-Hill:** I understand, but I do need to understand what damage they've done themselves here. This is a tricky relationship — we have done some stuff wrong for them in the past. But fundamentally, Inner World is paying us for organic performance. We've seen this before with other clients where they changed URLs and traffic disappeared. That's red flag number one to me. So with this categorization issue they've implemented, I need to understand if their developer understands SEO at all.

**Israel Beni:** Yeah, I told you last time — it's all good.

**Matthew Alves-Hill:** Yeah, so my hypothesis is that Ilya is making changes on the site that are affecting SEO performance as a whole. The Inner World team doesn't realize that's happening, and I think Ilya also doesn't realize these changes are really negative for the website.

**Israel Beni:** Well, I don't know how the communication goes internally at Inner World, but it depends. If you have a performance-oriented approach to your work, even when told to implement changes, you might say "this could cause this issue" and push back. But if there's no discussion and you're just told to implement it, developers dive in and implement it regardless of the outcomes.

**Israel Beni:** I don't know about that.

**Israel Beni:** One thing that was odd to me was yesterday during staging tests, he suggested retiring the availability folder — any URL with "availability" in it. I could do that since we're redirecting, but I didn't implement it because I think we need to make sure all availability pages are migrated first before we retire the folder. So this might hint that he's not well-informed about the migration we've been doing.

**Matthew Alves-Hill:** No, no, like, it's helpful.

**Matthew Alves-Hill:** I know, like, I appreciate that you don't want to say anything because we don't know.

**Matthew Alves-Hill:** But like, it affects our ability to work within a world if they're not communicating properly on their side.

**Matthew Alves-Hill:** And, like, for example, they're asking, like, how is our blog performing, right?

**Matthew Alves-Hill:** Since, like, I want to give them a performance report on the last month.

**Matthew Alves-Hill:** Thank

**Matthew Alves-Hill:** And when I go in and look, that's why I raised it today, because I go and look in Google Search Console, and I realize that, like, none of these blogs that we published in the last month are indexed by Google, right?

**Matthew Alves-Hill:** And fundamentally, they're not indexed because of this categorization issue in Prismic that is messing with the URLs and signaling to Google, like, And I think, to be honest, like, the site has been such a mess anyway, that it's going to take longer for our pages to index, and Google's, like, going to give us a harder time.

**Matthew Alves-Hill:** But, like, this, a month ago, we explained to Innerworld we are changing the blog path to reflections-the blog title.

**Matthew Alves-Hill:** And...

**Israel Beni:** And...

**Matthew Alves-Hill:** They haven't communicated internally to tell Ilya, hey, this is the new path, like, we need to remove this categorization feature.

**Matthew Alves-Hill:** And yes, we could have, like, spotted that issue earlier, but if there was some internal communication happening at InnoWell, they would, like, be aware of these.

**Israel Beni:** No, what is the thing is, as I said, I was not there, so I don't know what was discussion I preceded that, but my understanding was that if you are doing the categorization for block, that means reflection.

**Israel Beni:** So that will imply that after reflection, we have the category sludge, and then the article sludge.

**Israel Beni:** But the, what we have right now is getting rid of the reflection section totally.

**Israel Beni:** So just becoming...

**Israel Beni:** Like just a service or like a city.

**Israel Beni:** Yeah, I know what you mean. It's like a state page.

**Matthew Alves-Hill:** So in the blog right now, we go to `/reflections`. That's correct. This is the homepage. But when we click on a category like ketamine therapy, it changes the URL. And then when we click on the actual article, reflections disappears and it changes to the category path. It's dropping reflections and grouping it under the category. So we've made a load of redirects for these blogs, which from the outside looks good, but there's something going on with Prismic's routing.

**Israel Beni:** To be honest, when implementing any page routing structure while already live, you shouldn't move things to production until the sitemap is updated and the robots.txt is also updated if necessary. I highly doubt that was done when they migrated to the new structure. It looks like a very old sitemap has been kept, so every change still uses that old one. When you change a new URL structure, you need to reflect that in the sitemap so everything is in sync. URL changes don't only depend on changing the routing in the code — there are other aspects like the sitemap and robots.txt that need to be updated as part of the process.

**Matthew Alves-Hill:** Oh, gosh, this project is killing me. So in terms of recommendations, because we're meeting with Inner World leadership today, can we just remove the category feature? I'm trying to understand the order of how to fix this. I'm hearing that the sitemap needs to be updated, but we're also in the middle of redirects and new URLs. I don't really know what I'm talking about with sitemaps. So is that the right thing to do first? And the category piece is blocking our ability to index new blogs — we keep publishing new blogs, but they won't index because of this categorization issue.

**Israel Beni:** Okay, so my question is: what's the intended URL structure that Google should be indexing for the blogs?

**Matthew Alves-Hill:** The structure should just be `/reflections/[blog-title]`.

**Israel Beni:** Okay, is that what you want Google to index?

**Matthew Alves-Hill:** Exactly, yes.

**Israel Beni:** Okay, in that case, that can be fixed today. The sitemap we can update separately.

**Israel Beni:** So we can fix the URL structure of the blog first — add `/reflections` back and drop the category stuff. Then we focus on updating the sitemap.

**Matthew Alves-Hill:** That's what I would recommend.

**Matthew Alves-Hill:** Yeah, so I want to show you one more thing I'm confused about. When we look at last week's blogs — these are the blogs we staged last week, right?

**Israel Beni:** Yeah.

**Matthew Alves-Hill:** And that's how they're staged.

**Israel Beni:** You can access them with that URL. In Prismic, I just need to fill the handle, which is the URL slug. Yeah, so the routing is done in the code.

**Matthew Alves-Hill:** Ah, okay.

**Matthew Alves-Hill:** And the routing right now, because of this feature that Ilya added, is going ketamine therapy.

**Matthew Alves-Hill:** That's what the routing is doing.

**Israel Beni:** Yeah, it's doing that for the articles — the cards on the blog page.

**Israel Beni:** So we have two routes in the code base that are routing to the same page. For heaven's sakes, that's crazy. We have many paths for the same page. Usually for SEO purposes, you have to indicate a canonical URL.

**Matthew Alves-Hill:** Yeah, so, like, this opioid addiction thing, which is this one.

**Matthew Alves-Hill:** Your point is like this card is showing the categorization issue. So this published URL — they put these in, right?

**Israel Beni:** I did.

**Matthew Alves-Hill:** Wait, you put that in?

**Israel Beni:** That's how I understood the route we were going to be.

**Matthew Alves-Hill:** Okay, so what's weird is I saw some of these working. These ones are not working. Why does this one work?

**Israel Beni:** I did not add that one. Let me look at this. I'm confused here. This doesn't have reflections. I highly doubt I did that.

**Matthew Alves-Hill:** Yeah, I don't think that was you either. So if we look at the last batch we published — reflections, reflections, reflections — these are all correct.

**Israel Beni:** Yeah, I can confirm I had those. The ones we thought were wrong might have been a mistake on my part, or someone changed them.

**Matthew Alves-Hill:** Okay, so why does this one work?

**Israel Beni:** This one doesn't. The thing is, we have the base URL which is innerworld.com/reflections, and then the handle of the URL. So the routing is done in the code.

**Matthew Alves-Hill:** I see. So this is what we're publishing under, and this is working. But if you navigate to it, you get a different URL. So can you explain why they both work?

**Israel Beni:** Okay, so basically there is a route to handle `/reflections/[slug]` in the code base, and there is also another route handling all defaults — the catch-all routes we can have on the website. So we have two routes that are handling the same thing. To fix this, we just need to change the code in the blog page routing to direct to `/reflections/[slug]`. The issue is in the code base, not the individual articles.

**Matthew Alves-Hill:** So we have to change that manually?

**Israel Beni:** No, we need to change that in the code base, because that's where it was introduced.

**Israel Beni:** Okay.

**Matthew Alves-Hill:** So out of interest here, what I do want to understand is, like, is this...

**Matthew Alves-Hill:** I just want to check what Google is seeing.

**Matthew Alves-Hill:** ...

**Matthew Alves-Hill:** Thank you.

**Matthew Alves-Hill:** You

**Israel Beni:** Part of some of the issues, there are lot of issues on the website, and most of them are things that are due to the fact that they are using JavaScript.

**Israel Beni:** If you remember, I did inform you that any website that has JavaScript as there on the languages, you know, it's just a time bomb in production.

**Israel Beni:** So now there are going to be issues appearing.

**Matthew Alves-Hill:** Okay, so this is an older blog, 31st of October.

**Matthew Alves-Hill:** You staged this, I think.

**Matthew Alves-Hill:** I think by now, yeah, this would have been you.

**Matthew Alves-Hill:** First thing is, like, this H1 is wrong.

**Matthew Alves-Hill:** I don't know how that happened, but...

**Matthew Alves-Hill:** ...

**Matthew Alves-Hill:** ...

**Matthew Alves-Hill:** But that's not really the point.

**Israel Beni:** Yeah, that's, it's actually just that.

**Matthew Alves-Hill:** But the point is, like, this, Google has indexed this page under this pathway.

**Matthew Alves-Hill:** It's here.

**Matthew Alves-Hill:** Or it isn't, is.

**Matthew Alves-Hill:** Okay.

**Israel Beni:** Mm-hmm.-hmm.

**Israel Beni:** Mm-hmm.

**Israel Beni:** Mm-hmm.-hmm.

**Matthew Alves-Hill:** Right, so let's just check something from the 17th dementia.

**Matthew Alves-Hill:** Wow.

**Matthew Alves-Hill:** Okay, so that's not, So then is this, Okay.

**Matthew Alves-Hill:** So Google is indexing based on the categorization path, but it's not indexing more recent blogs. This must be a site health issue.

**Israel Beni:** The one that you checked that it was indexed, what time it was published?

**Israel Beni:** When was that published?

**Matthew Alves-Hill:** The 31st of October.

**Matthew Alves-Hill:** Okay, I see.

**Israel Beni:** So obviously Google takes some time to index a page. That might be one reason the October 31st article finally got indexed. One factor that accelerates the time for Google to index your pages is having an up-to-date sitemap. It moves things faster. That's why for newer articles, we don't have that acceleration — the sitemap is probably not reflecting those articles either.

**Matthew Alves-Hill:** This is weird though, because the article "at-home ketamine versus infusion" was published on November 10th, but it's not showing in Search Console. And the one from the 17th is there, but I can't find these other two articles.

**Israel Beni:** Can you share those with me?

**Israel Beni:** I'm checking. I can see the first one — "Fathom and Therapy gets you high" — let me share my screen.

**Matthew Alves-Hill:** Yeah, go ahead.

**Israel Beni:** The first thing you shared with me — is it this one?

**Matthew Alves-Hill:** No, sorry, I sent you the wrong two.

**Israel Beni:** I see. It looks like these have not been published. There are three articles that have not been published: "at-home ketamine versus infusion," "key benefits of vitamin D," and "ketamine therapy for dementia." But the dementia article is on the site.

**Matthew Alves-Hill:** I've seen it. So there must be draft changes that haven't been pushed.

**Israel Beni:** Let me check. You're right — there's been a draft change, but it's not published.

**Matthew Alves-Hill:** Okay, so let me just check if Inner World actually published these.

**Israel Beni:** If you want, I can publish them.

**Matthew Alves-Hill:** No, they asked us not to do anything.

**Israel Beni:** Right, because you remember we changed the image.

**Matthew Alves-Hill:** Yes, I remember. So this was on Friday, the 31st of October — you would have staged those. Looking at the dates, it looks like you staged them on Monday the 10th of November. So those should have been published. I think that's their problem — they haven't published the articles we staged. We told them they were staged on the 31st of October, and then we staged more on the 10th of November. They just didn't publish them.

**Matthew Alves-Hill:** So this is crazy. I think I need to speak to Jacob to get his technical input. So it looks like Google is indexing the URLs that Inner World's Prismic system categorizes — that's how Google is indexing them, but it's taking a long time. So if Google is indexing them, then in theory we could keep the categorization that Prismic is doing?

**Israel Beni:** Well, if that's the right URL you guys intended to have, yes. But if it's not the case, we need to change that. The main issue is that there's a missing `/reflections` in the URL path.

**Matthew Alves-Hill:** Right.

**Matthew Alves-Hill:** So there's like no canonical tag.

**Israel Beni:** There's no canonical stuff. I can also check what's going on with the other SEO standards. Do you have that documentation?

**Matthew Alves-Hill:** Yes.

**Matthew Alves-Hill:** Israel, I'm going to hop off — I need to go. Can you do me a favor? Once you've had a look through this, can you drop me a message with a summary of what we need to fix here from your perspective, in order of priority at a high level? I'm going to sync with Jacob, and some of these problems I don't fully understand yet, so your help would be super useful.

**Israel Beni:** Yeah, so the first thing is to confirm the path that you want. A lot of the work we currently have does not follow the URL structure you want. So we need to first confirm the URL structure you want, then update everything to that right URL structure, and then the sitemap needs to be synced up with the current structure of the website.

**Matthew Alves-Hill:** Would we have to do a whole other batch of redirects if we remove the categorization piece?

**Israel Beni:** No, we wouldn't do any redirect for that since it's mainly in the code base routing. Changing the routing in the code base will work directly. The difference is with the availability pages — those pages have routing dictated by Prismic. In that case, we'd need a redirection. But for this, we have two routes handling the same thing. We just need to eliminate the additional route and keep the canonical URL.

**Matthew Alves-Hill:** But if Google is indexing on the categories and we want it looking at `/reflections/[slug]`, then is it a redirect issue?

**Israel Beni:** In that case, yes, we can do a redirection in addition to changing the routing. This will keep up Google indexing while we're transitioning.

**Matthew Alves-Hill:** Can you just drop a message in Slack summarizing from your perspective? I need your take for when I meet with Jacob. I want what we discussed, your priorities, and what we need to do so I can convey that to Inner World leadership, since we're meeting them today. That would really help me.

**Israel Beni:** I wanted to show you the fix, but I have so many things going on right now and my system is lagging. Unfortunately, I can't show you right now. We'll put a pin in it and come back to it.

**Matthew Alves-Hill:** All right.

**Israel Beni:** Talk to you in a bit.

**Matthew Alves-Hill:** Thanks, Israel. Bye.
