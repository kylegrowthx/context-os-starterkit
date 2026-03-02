# Vizcom <> Growth X - Weekly Syncs

<metadata>
date: 2026-01-13
time: 17:59 UTC
duration: 22 minutes
organizer: team@growthxlabs.com
participants:
  - name: Carly Piekos
    email: carly@growthx.ai
    company: GrowthX
  - name: Sophia Silver
    email: sophia.silver@vizcom.co
    company: Vizcom
  - name: Kim Lu
    email: kimberley.lu@vizcom.co
    company: Vizcom
  - name: Maura Kelly
    email: maura.kelly@vizcom.co
    company: Vizcom
  - name: Aida Knezevic
    email: aida@growthx.ai
    company: GrowthX
  - name: Andreina Coronado
    email: andreina.coronado@vizcom.co
    company: Vizcom
  - name: Emily Lonetto
    email: emily.lonetto@vizcom.co
    company: Vizcom
  - name: Chris
    email: chris@vizcom.co
    company: Vizcom
fathom_recording_id: 113917047
fathom_url: https://fathom.video/calls/529040934
share_url: https://fathom.video/share/wia2bBGfvRPnqVYoH39g3cMCPUNP_bts
source: fathom
enriched_on: 2026-02-28 00:00 UTC
</metadata>

---

## Summary

GrowthX and Vizcom reviewed critical post-launch SEO issues following Vizcom's site migration on January 8th, including GSC cleanup, meta description fixes, and crawl error resolution. The team finalized strategies for blocking UTM and 404 pages in robots.txt, addressed a 3-day analytics data gap, and discussed content publishing blockers (OG images) and new SEO initiatives (schema markup and alt text implementation).

---

## Context

Vizcom launched a redesigned website on January 8th, 2026, managed through Webflow. This is a weekly sync between Carly Piekos (GrowthX's SEO strategist) and the Vizcom team (Sophia Silver, Kim Lu, Maura Kelly, and Emily Lonetto) to monitor technical health, resolve post-launch issues, and coordinate content publishing. The launch uncovered several immediate issues: Webflow auto-scraped animated text into garbled meta descriptions, Google Search Console is reporting crawl errors for UTM-tagged URLs and 404 pages, and a 3-day analytics tracking gap occurred (likely from agency changes made over the weekend). In parallel, eight blog articles are blocked from publishing pending OG image finalization, and the team is implementing new SEO best practices (schema markup and alt text) to improve search visibility and accessibility.

This weekly cadence will continue until the migration stabilizes, after which the team plans to move to bi-weekly check-ins. GrowthX provides ongoing technical SEO guidance and content coordination, while Vizcom handles design implementation, image creation (via Jenny), and marketing workflow decisions.

---

## Relevance

**GrowthX Operations & Client Services**
- Demonstrates GrowthX's post-launch technical SEO support model for B2B content engagements
- Shows active coordination with clients on Google Search Console optimization
- Weekly syncs indicate hands-on account management and issue resolution cadence

**Technical SEO & Search Performance**
- Meta description auto-scraping from animated content is a Webflow-specific issue
- UTM crawl optimization and robots.txt configuration are foundational GSC health practices
- Analytics data gaps post-migration are common; restoration process documented

**Content Publishing Workflow**
- OG image inconsistency is a known bottleneck in content-to-launch processes
- Schema markup and alt text are emerging best practices for AEO/LLM model optimization
- Topic list cannibalization audit prevents redundant content and diluted search equity

**Client Collaboration**
- Weekly touchbase format works best during turbulent launch windows
- Clear role separation: GrowthX (SEO/strategy), Vizcom (design/implementation), external agency (initial build)
- Slack-based async updates complement synchronous syncs for continuity

---

## Overview

- **GSC Cleanup:** The `robots.txt` file will be updated to disallow UTMs (after confirming they're tracked elsewhere) and 404 pages, which are causing crawl errors.
- **Content Blocked:** 8 articles are ready for review, but publishing is blocked by the lack of Open Graph (OG) images.
- **New SEO Initiatives:** Vizcom will implement schema markup and alt text to improve search ranking and accessibility.
- **GA Data Gap:** A 3-day Google Analytics data gap (Jan 9–11) occurred post-launch, likely from agency work; tracking is now restored.

---

## Key Topics

### Technical SEO & GSC Cleanup

  - **Meta Description Fix:**
      - **Problem:** Webflow scraped the homepage's animated text, creating a garbled meta description.
      - **Action:** Vizcom manually updated the description in Webflow and submitted the URL to Google Search Console (GSC).
      - **Follow-up:** Carly will check for an update by Friday and resubmit if needed.
  - **GSC Crawl Errors:**
      - **Problem:** GSC is reporting crawl errors for UTMs and 404 pages.
      - **Action:** Vizcom will confirm if UTMs are tracked elsewhere. If so, Carly will update `robots.txt` to disallow crawling of URLs with a `?` (UTMs) and specific 404 pages (`/signup`, `/login`).
  - **`robots.txt` Review:**
      - **Action:** Carly will review Vizcom's new `robots.txt` file to ensure it's correctly configured.
  - **URL Structure:**
      - **Problem:** A `vizcom.com/resources/blog` structure was incorrectly implemented by the agency.
      - **Resolution:** The structure was corrected to `vizcom.com/blog`, and unnecessary redirects were removed.

### Content & Publishing

  - **Open Graph (OG) Images:**
      - **Blocker:** 8 ready-to-review articles cannot be published without OG images.
      - **Requirement:** Vizcom needs a consistent design language for both metadata (social sharing) and on-page thumbnails.
      - **Action:** Carly will follow up with Jenny on the status of these images.
  - **New Topic Pipeline:**
      - 5 new drafts are in progress.
      - Carly will audit the remaining topic list to prevent duplication and cannibalization before sending it to Vizcom for approval.

### New SEO Initiatives

  - **Schema Markup:**
      - **Rationale:** Improves search ranking by making content easier for bots to read.
      - **Action:** Carly will provide templates and recommendations for specific schema types (e.g., Organization for homepage, Article for blog posts).
  - **Alt Text:**
      - **Rationale:** Improves accessibility for users with disabilities.
      - **Action:** Vizcom will write descriptive alt text that avoids keyword stuffing.

---

## Action Items

**Carly Piekos (GrowthX)**
- Coordinate w/ Jenny on OG/thumbnail images; update Sophia/Kim in Slack
- Check meta descriptions in GSC; resubmit if not updated
- Annotate site launch date in analytics/reporting
- Audit topic list; send to Sophia/Kim for approval
- Send schema templates to Kim; prep walkthrough for next sync
- Send call summary to Sophia, Kim, Maura
- Send weekly Monday data updates + EOW publishing updates in Slack
- Set up next week's agenda; enable additions

**Kim Lu (Vizcom)**
- Audit robots.txt; confirm UTM tracking w/ Ritika/Jean; update Carly
- Disallow signup/login/support in robots.txt; redirect 404s

**Sophia Silver (Vizcom)**
- Confirm UTM tracking location with Ritika and new team member Jean
- Approve 8 ready-to-publish articles for release
- Approve new topic list (5 in-progress drafts) by next week

**Emily Lonetto (Vizcom)**
- Monitor site post-launch for any tracking or configuration issues

---

## Transcript

**Sophia Silver:** This meeting is being recorded.

**Carly Piekos:** Hi, Sophia. How are you?

**Sophia Silver:** I'm good. We had the site launch last week, so it was a busy one. But I'm just happy to have it out in the world.

**Carly Piekos:** Yeah, migrations are always challenging. I'm happy to help in any way I can. Let me get everyone situated here. Hi, Kim. Hi, Maura.

**Kim Lu:** Hi, everyone.

**Carly Piekos:** Is anyone else going to be joining the call today? Let's see if we have everyone.

**Sophia Silver:** I think we're good.

**Carly Piekos:** Perfect. So the updates for this week. Does anyone have anything top of mind that you want to add to the agenda?

**Sophia Silver:** I think my one thought was open graph images for the articles we published. I think we had questions about that from last week, Kim.

**Kim Lu:** Yes. Just finalizing the design language and making sure we can get those in so we can publish those blogs.

**Carly Piekos:** Okay, I'll add that to the next steps. I'll get in touch with Jenny. For clarification, is the OG image for the metadata or the thumbnail?

**Maura Kelly:** Just clarifying—are these different OG images for each blog, or the same ones?

**Sophia Silver:** For the metadata, I believe. But also the thumbnails for the cards when you're on the blog.

**Kim Lu:** And we need the core blog images for both the metadata and thumbnails. If they can be the same, that's fine.

**Carly Piekos:** All right. So core blog images for open graph—metadata and thumbnails. I'll check on that and get back to you in Slack.

**Kim Lu:** I also added a follow-up question about meta description updates that Emily submitted.

**Carly Piekos:** What happened with the meta descriptions?

**Kim Lu:** Since the homepage is heavily animated, Webflow scraped the animated text into a weird format for the meta description. Emily manually updated them on Webflow and submitted the URLs to Google Search Console for review.

**Carly Piekos:** If you published and submitted the URL to Google Search Console, that's pretty much all you can do. It shouldn't take long since you have a small site. I'll check by Friday and resubmit if it hasn't updated.

**Carly Piekos:** And you launched on the 8th, correct?

**Sophia Silver:** Yes, January 8th.

**Carly Piekos:** I want to make sure we annotate that in analytics so we know exactly when the new site went live. Now, for the technical issues—robots.txt. What do you need from me?

**Kim Lu:** It was already configured. We added some initial setup to allow the sitemap to be read.

**Carly Piekos:** I'll review it to do a sanity check. Now, I noticed some crawl errors in your Google Search Console. I want to make sure we're fixing the canonicals. In robots.txt, I'd disallow anything with a question mark to handle UTMs.

**Carly Piekos:** Are these UTMs being tracked elsewhere in your analytics?

**Kim Lu:** What would be a use case for tracking UTMs in Search Console?

**Carly Piekos:** If you're adding UTM codes to URLs from social media or Google Business Profile to track where traffic comes from, you'd track them. But if they're tracked elsewhere in your system, you don't need Google crawling them.

**Sophia Silver:** Yeah, we're using UTMs for feature launches and marketing materials. Let me check with Ritika and Jean—who just started this week—to see where we're tracking them currently. If they're tracked elsewhere, we don't need them in Search Console.

**Kim Lu:** Okay, we'll follow up on that. If we don't need them tracked in GSC, we'll disallow the question mark UTMs in robots.txt.

**Carly Piekos:** Right. Also, for the 404s—signup, login, support—you don't need Google crawling those. We should disallow them in robots.txt and make sure they redirect to the right place.

**Carly Piekos:** I did notice you're using Adobe's LLM checker extension. Good call on that. Everything is looking solid—you have your characters, descriptions, canonicals, and H1s in place.

**Sophia Silver:** That's really cool.

**Kim Lu:** Love that.

**Carly Piekos:** Now, the Google Analytics issue. I know Emily brought that up.

**Kim Lu:** We essentially lost tracking for a few days from the site, but it's working again now. We can see the data gap from the 8th through the 11th, and now it's coming back in.

**Sophia Silver:** I think the agency made some changes while finalizing the site, and they continued working over the weekend. That likely caused it. Emily undid some of those changes over the weekend, which got us back online.

**Carly Piekos:** Okay, so tracking is restored. The data should continue coming in now.

**Carly Piekos:** So we have eight drafts ready for review for next week. You're working on five new drafts—design productivity tools, behind-the-scenes design, AI rendering tools, design workflow optimization, and design automation tools. We're almost through the approved topic list.

**Carly Piekos:** I'll do a quick audit of the incoming topics to make sure there's no cannibalization or duplicates before you review them. If we can get those approved by next week, Jenny can start on the new topics for publishing.

**Carly Piekos:** That's everything from my side for now. We're waiting on data to come through from Search Console and Analytics. I'll have more information on your data next week.

**Kim Lu:** One more thing—we discussed adding schema markup and alt text. Is that something that will help us rank better?

**Carly Piekos:** Yes, absolutely. Structured data is a ranking factor, especially with LLMs. It makes content easier for bots to read. I'd definitely include schema markup on your blog pages and other pages. I have some templates we can use.

**Carly Piekos:** The best practice is using specific schema for different pages. So, Organization schema on the homepage, Article schema for blog posts. I'll put together a list, and we can walk through it next week.

**Kim Lu:** We'd love templates. We haven't done this before, so guidance on per-page structure would help.

**Carly Piekos:** I've done this many times. Schema markup varies by page type, and we don't want to overload pages. We'll go through the recommendations next week.

**Kim Lu:** Is alt text different from schema markup?

**Carly Piekos:** Yes, alt text is mainly for accessibility—helping users with disabilities. When writing alt text, focus on describing the image itself, not keyword stuffing. Just clear, specific descriptions.

**Carly Piekos:** I also noticed you added "resources" to the URL structure for the blog. Is that still active?

**Sophia Silver:** No, that got taken down. It should just be vizcom.com/blog. The agency had added redirects, but Emily removed them over the weekend. Everything should be direct now.

**Carly Piekos:** Good. That was likely blocking blog content from showing up. So for next week—schema markup, alt text, and structured data. I'll get an update on the OG images by end of day today. You just need to approve the five new drafts and I'll audit the topics to prevent cannibalization.

**Sophia Silver:** Awesome. We'll also check on our UTM tracking.

**Carly Piekos:** Perfect. I'll send a call summary after this so everyone has the priority list. Once the launch stabilizes and you're not troubleshooting every five minutes, we can move to bi-weekly meetings. But for now, weekly syncs make sense. I'll send Monday data updates and end-of-week publishing updates in Slack.

**Kim Lu:** I think we'd also like to track progress and impact of the pages we're setting up. Once we get into a better cadence, bi-weekly would make sense. But I'm liking the weekly syncs for now.

**Carly Piekos:** I agree. Weekly is better right now. I'll update you Mondays if there are issues and send end-of-week updates on what's been completed in the publishing pipeline. I'll set up next week's agenda so you can add items during the week as they come up.

**Sophia Silver:** Great. Thank you, Carly.

**Carly Piekos:** No problem. I'll be on Slack all week. Have a good week!

**Sophia Silver & Kim Lu:** Bye!
