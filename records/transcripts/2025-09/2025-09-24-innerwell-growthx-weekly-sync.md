# Innerwell <> GrowthX - Weekly Sync

<metadata>
date: 2025-09-24
time: 15:31 UTC
duration: 31 minutes
organizer: team@growthxlabs.com
participants: Jakub Rudnik (GrowthX), Akina Sundararaman (Innerwell)
fathom_recording_id: 89512330
fathom_url: https://fathom.video/calls/418855499
share_url: https://fathom.video/share/Kzn7GcwuxQZW1n6Xtw_auBpGinrhjKSF
source: fathom
enriched_on: 2026-03-03 00:45 UTC
speaker_note: Only two speakers in this meeting—Jakub from GrowthX and Akina from Innerwell. The "akina" display name in the transcript corresponds to Akina Sundararaman at akina@helloinnerwell.com based on participant data. All other participants (Andrew Berman, Andi Bailey, Noa Cornberg, Matthew Alves-Hill) were invited but did not speak during the recording.
</metadata>

---

## Summary

Jakub and Akina aligned on a major site restructuring plan for Innerwell to address cascading SEO issues from duplicate and orphaned pages. The team agreed to consolidate the URL structure into a hierarchical `/service/state/city` format (e.g., `/ketamine/california/los-angeles`) with proper breadcrumb navigation, and to redirect all legacy pages to the new structure in batches. Before executing the redirect strategy, Jakub needs Akina's confirmation that the dev team can support nested folder structures in the CMS, and Akina needs Jakub's final mental health page structure proposal by end of day.

---

## Context

Innerwell is an online mental health and ketamine therapy provider, and they're a key GrowthX client. This is a technical SEO deep-dive call focusing on Innerwell's site architecture, which has accumulated structural debt over time. Multiple rounds of content expansion—including ketamine therapy pages, mental health service pages, EMDR pages, and location-based variants—created a chaotic URL structure with heavy duplication and orphaned pages that don't link together. Jakub, GrowthX's SEO strategist, has been auditing the site and discovered that despite the poor structure, some newer pages are outperforming older ones, which validates the proposed redesign. Akina leads Innerwell's content and technical implementation; this meeting is where they align on the fix before executing the redirect strategy, which is a high-risk, high-impact operation.

---

## Relevance

- **To GrowthX Delivery:** Site restructuring and redirects represent a major execution project—requires mapping old URLs to new hierarchy, setting up 301 redirects in three batches, adding breadcrumbs, filling gaps with missing city pages, and potentially adding clinician modules to ketamine pages. Demonstrates GrowthX's ability to architect and execute complex programmatic SEO fixes at scale.

- **To GrowthX Business Development:** Innerwell's success with this restructure will likely generate positive results (traffic recovery, ranking improvements) in Q4, which strengthens the relationship and provides case study material for similar multi-location service clients. Akina's willingness to pause new development while sorting out structure signals strong engagement and trust.

- **To Delivery Quality:** Site structure issues teach hard lessons about the importance of URL architecture decisions early in content expansion—this is a preventable problem if planned correctly. Future rollouts with other clients can reference this project.

---

## Overview

- **Current site structure is messy with duplicated pages** - Multiple versions of state/city pages exist across different URL structures (availability, ketamine, EMDR, mental health), causing SEO problems and splitting crawl budget and keyword targeting across competing pages
- **New URL structure agreed upon**: `/service/state/city` format (e.g., `/ketamine/california/los-angeles`) with proper breadcrumb navigation and internal linking from service to state to city
- **Technical confirmation needed before execution**: Jakub needs Akina to confirm the dev team can support nested folder structures in the CMS—this is a prerequisite before mapping old URLs to redirects
- **Three-batch redirect strategy**: First batch redirects new state pages to their new homes; second batch merges old "availability" pages into the new structure; third batch handles city-level pages
- **Mental health as umbrella pages** - Mental health pages should list all available services and link to service-specific state pages; Jakub is refining the exact structure and will send proposal to Akina same-day
- **Filling gaps** - Not all cities are represented in the new structure yet; GrowthX will programmatically create missing city pages using the same PSEO approach
- **Clinician modules missing** - Ketamine state pages lack the clinician modules that appear on mental health pages; Akina flagged this needs to be added for conversion potential

---

## Key Topics

### Current Website Issues

  - Multiple duplicated pages across states and cities, especially for ketamine therapy
  - No consistent URL structure across services (ketamine, mental health, EMDR)
  - Pages are "orphaned" with no internal linking between related content
  - Despite poor structure, newer formatted pages are performing better in SEO
  - Some pages missing clinician modules that could help with conversions
  - Current structure splits crawl budget and creates competing pages targeting same keywords

### Proposed URL Structure Solution

  - Implementation of hierarchical URL structure: `/service/state/city` (e.g., `helloinnerwell.com/ketamine/california/los-angeles`)
  - Mental health pages function as umbrella landing pages that list all available services and link down to service-specific state pages
  - Breadcrumbs on all pages to improve navigation and SEO (linking back: city → state → service)
  - Add clinician modules to ketamine therapy state pages (currently only on mental health pages)
  - Update footer and site navigation to reflect new hierarchical structure
  - Ensure internal linking from mental health state pages to their service counterparts

### Implementation Plan and Priorities

1.  Confirm technical feasibility of nested URL structure with dev team
2.  Map old URLs to new structure (focusing on state pages first)
3.  Set up 301 redirects in batches:
      - New state pages to their new URL homes
      - Redirect all "availability" format pages
      - Address city pages
4.  Fill gaps by creating missing city pages in new format
5.  Fix internal linking between pages
6.  Update footer with new site architecture

### Additional Concerns

  - "Conditions" pages (like ketamine for depression) get few organic clicks
  - Some city pages never indexed by Google
  - Need to reorganize how cities link from state pages
  - Many pages lack proper navigation and internal linking

---

## Action Items

**Jakub Rudnik (GrowthX)**
- Map out the final mental health page structure (including how it fits with the service pages) and send to Akina today

- Create and send the list of states with their new URLs for redirect batch step 1 (moving new state pages to their new homes)

**Akina Sundararaman (Innerwell)**
- Confirm with dev team that the CMS can support the nested folder structure (ability to place state pages under service parent pages)

- Check progress on adding breadcrumbs to city and state pages

- Once foldering is confirmed, prepare to execute three-batch redirect strategy for old pages to new URLs

---

## Transcript
**Akina Sundararaman:** Hi, Jakub.

**Akina Sundararaman:** I think you're on mute.

**Jakub Rudnik:** Zoom, the different settings in Google Meet. Can't go back. Like, switching back and forth. It's just killing me.

**Akina Sundararaman:** How are you? Good. How are you doing? I think it's just, it's me today.

**Jakub Rudnik:** No one's in Barcelona now. Oh, nice. Very good for her. Okay, I'm just going to throw a little bit at the end of the Slack, and I'll just share it here since it'll be one-on-one, but basically two things.

**Jakub Rudnik:** One, I move this weekend to a new state, so I'm like all over the place mentally. So bear with me. This is definitely a priority because the site structure is a mess. Two—stuff is very messy. I don't think that's a surprise to you, but as I was peeling back the onion even more, there's just a lot of layers of SEO and pages to work through. It's not end-of-the-world stuff though. Luckily, we have a lot of good traffic and signals despite doing a lot of things incorrectly. Some decisions are stressing me, but I think we can work through them and get things settled.

**Akina Sundararaman:** And we'll also see a huge lift once we get these things right.

**Jakub Rudnik:** It's not completely done, but I need your buy-in plus a couple technical confirmations before we can move forward. I have a plan to outline here. Let me get this on the screen. What are you doing, by the way? We're moving to Cleveland. And I'm in Chicago now. But just to say it—we bought the house next to some of our best friends and their three kids. The house went on sale and they joked, "If anyone wants to move next to us." The day before, me and my wife had been like, we should try something else. It was just like someone is telling us to do something. We thought about that for a few weeks and then pulled the trigger. Our other best friends—I lived with them after college—they were moving from Florida to Cleveland. After we pulled the trigger, they were planning to move to the Midwest. They just didn't know which city, but they wanted to be closer to his family and friends again. So they're like seven minutes from us and moving the week after we do. It all just happened—nobody planned any of this. We're all kind of getting back together.

**Akina Sundararaman:** Well, that's fun. That's like the dream—to live with your friends.

**Jakub Rudnik:** Seriously. So we're very excited. Moving sucks, but anyway, by next week we'll be back in business. Okay, to this:

**Jakub Rudnik:** As we unearthed last week, I knew the state and city level stuff was wonky, but I didn't realize how many duplicates exist at the state level. For ketamine, we have states and most cities, but we've got duplicates of most cities and all the states. Mental health, we have all the states but no cities. EMDR has a mix of old and new versions. It's not uniform at all. Some of the PSEO we set up in the spring just wasn't fully executed, so there are little nuances and complications across everything. I remember mapping some of this, so I don't know why it didn't happen—I'm sure it was more on our end and didn't get communicated. Let me share the URLs on screen. Thanks for bearing with my scatterbrain because it's just not clear and there's so many little pieces. But the pages we've created—like California-mental health or ketamine therapy California—these ones are doing better than the older versions like availability ketamine therapy California, from an SEO perspective. That gives me a lot of belief that we should move forward with these new versions of the pages.

**Jakub Rudnik:** But I typically prefer—especially when we're doing this programmatic and nested types of content—a URL structure like what you set up before we got involved. We should have service-level landing pages like ketamine, mental health, EMDR. These should be state agnostic, city agnostic—they list what Innerwell offers for each service. Then from these, there should be a way to jump over to state pages. That's not happening now. But state pages should nest under the service. Like, helloinnerwell.com/ketamine/california—that's the state-level page. We've essentially created hundreds of orphaned URLs right now because there's no connection between city and state, and no connection from state to service. I remember doing that as one of the first things I did with you, and I recommended it to our team. I'm sure it was lost on our side. Assuming we can do this technically, we could take the current California page and nest it under the Ketamine page. I don't know with your CMS, so we'd want to confirm that with your web team and do it once before we map all those redirects. Then, availability/ketamine-therapy/california would redirect to the new URL. Right now we're splitting crawl budget and SEO—we're targeting the same keyword with two pages. So I would merge all of these state-level pages.

**Akina Sundararaman:** So basically you'd redirect all the availability pages.

**Jakub Rudnik:** Yes. And in the short term, I wouldn't sunset every city-level page because there are some cities on the availability side that don't have a new version. So we'd need to fill that gap by publishing new versions using the same PSEO approach. Like, we have one for Chico, but we don't have all of your cities covered. So we'd need to identify gaps and build new versions. There are short-term risks—some availability pages get some traffic, though it's lower than others. A redirect from availability/ketamine-therapy/california to the new structure has fairly low risk, but anytime you redirect, something could drop as Google re-indexes. The pages aren't linked anyway—they're just findable through sitemap, which is actually why it's crazy that these pages perform better. We've done everything kind of wrong for them. There's definitely bad internal linking to sort out—random pages linking to wrong places. We'll need to clean that up.

**Akina Sundararaman:** So right now, what are the ways someone can get to this page?

**Jakub Rudnik:** To get to this page? That's a good question. The only way is through sitemap because they're not linked from the California page or the ketamine page or anywhere else. There's some weird internal linking—like California Mental Health pages linking to Ketamine Therapy California—but overall there's a lot of bad linking that needs to be fixed.

**Jakub Rudnik:** If I was starting from scratch, this is what I would do: service, state, city. There are nuances and inconsistencies, but at the scale we're trying to create content and with the obvious segments you have, this URL structure makes sense. Each page should have breadcrumbs linking back through the hierarchy. Your old versions did this well—we just need to add breadcrumbs to the new pages.

**Akina Sundararaman:** So these would all link to each other, obviously. And then the availability pages would redirect to which one?

**Jakub Rudnik:** I have a question about the mental health pages. Someone really wanted those pages two months ago. Is that still a focus? And is mental health like an umbrella above the other services?

**Akina Sundararaman:** So mental health lists out ketamine, psychiatry, all the other services.

**Jakub Rudnik:** Okay, I need to think about how this fits with the service/state/city structure. If you have a mental health Minnesota page, those should all link to the other services. But I hadn't fully worked through the mental health piece. Let me suggest something: mental health could be a separate service with its own state pages. Like `/mental-health/minnesota`, and from there you can link to other services. But I'm not sure if that doubles up on the directory.

**Akina Sundararaman:** What if we did mental health as a service, but then underneath it, the service folder? Like `/mental-health/ketamine/california`? That way we don't need to folder mental health twice.

**Jakub Rudnik:** Yeah, yeah. Like mental health and then ketamine underneath it and then state. I think that's right. The mental health structure isn't fully worked out yet, but that solves the duplication problem. I just don't want to lose track of these pages. Let me work through this and get you the structure proposal.

**Jakub Rudnik:** If we're in agreement on the ideal structure with the mental health caveat, can your team handle this technically? We already have a ketamine page. Can we put California underneath it with a slash, and then Los Angeles under that? We've done this historically with the availability pages. I would think most CMSs can handle nested folders, but I've had issues before.

**Akina Sundararaman:** Are the redirects 301s?

**Jakub Rudnik:** I'm pretty sure it's 301. Yes, once we confirm the technical setup and they set it up on the backend, I'm 98% sure it's 301. There might be some different codes, but 301 would be the bulk. This is the one we can't answer in this call—we need to confirm with someone on your team. But if we can do this, the new formats are already performing better despite not being findable yet. Not all cities exist in the new structure, so we'd need to programmatically create those and fill gaps. The new state pages also need breadcrumbs—we should link from state pages down to cities. Also, the ketamine state pages don't have the clinician module that appears on mental health pages. That should be added from a conversion standpoint. We can help advise on where to place that module. I also noticed the condition pages—like "ketamine for depression"—get very few organic clicks. That's more educational top-of-funnel content. I'd put that under the blog and noindex the service pages so they're only accessible from a footer or for pushing conversions. Lower priority. Now that I know how mental health fits in, I can send you the structure proposal today. If you can confirm your dev team can handle nested folders before we start mapping, we can move forward. We'd map old to new for both cities and states, then set up three batches of redirects simultaneously. We'd also need to fill gaps with missing city pages and review unindexed pages in GSC to see if they can be rescued or should be removed.

**Akina Sundararaman:** Okay, and these are in order of most impact, right?

**Jakub Rudnik:** Yeah, these first are just agreement and confirmation, then I'd work down from there.

**Akina Sundararaman:** Sounds good. I'll confirm the foldering setup with the team. You'll let me know on the mental health structure, right?

**Jakub Rudnik:** Yeah, the page structure. Once you confirm the technical piece, I'll send you the mental health structure and a list of the states with their new URLs. That's the first batch. Once we have that, we can start redirecting all the availability pages.

**Akina Sundararaman:** And we're still building new city pages this month?

**Jakub Rudnik:** Yeah, we've been semi-paused figuring out the site structure, but we have bandwidth to build those landing pages. I'd focus on stopping blogs and just filling in city page gaps until we're caught up basically in October. Then state-level pages depending on the service.

**Akina Sundararaman:** I asked the team to add breadcrumbs on the cities for the state pages, so check in on that.

**Jakub Rudnik:** Okay, if you get that confirmed, I'll get the mental health proposal over today. Please let me know if there's any ambiguity or questions—I'd rather talk through them.

**Akina Sundararaman:** No, I agree. Let's just have everything pause on new development and sort this stuff out first.

**Jakub Rudnik:** I'll keep an eye on Slack. Good luck with the move. Talk soon.

**Akina Sundararaman:** Thanks, Jakub. Thank you very much.

**Jakub Rudnik:** Bye.
