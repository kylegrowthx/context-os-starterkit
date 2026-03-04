# Anything <> GrowthX - Weekly Sync

<metadata>
date: 2025-10-28
time: 17:30 UTC
duration: 35 minutes
organizer: team@growthxlabs.com
participants: Aida Knezevic (GrowthX), Nathalie Schrans (GrowthX), Dhruv Amin (Anything), Erik O'Brien (GrowthX)
fathom_recording_id: 97393828
fathom_url: https://fathom.video/calls/453994701
share_url: https://fathom.video/share/_f5CVmPySdt1sM_5PrTdv9W-Cdncy7Yo
source: fathom
enriched_on: 2026-03-02 12:00 UTC
</metadata>

---

## Summary

GrowthX and Anything finalized the blog platform build decision, with Dhruv committing to build a Sanity CMS blog that supports direct table embeds and UTM tracking. The team aligned on a streamlined content approval workflow: GrowthX will propose ~20 priority topics for quick approval instead of reviewing all 99 keyword ideas, and they'll publish articles first with minimal visuals, enriching high-performing posts later with graphics and product screenshots.

---

## Context

Anything is a digital product creation platform offering templates, tools, and guidance for non-technical creators. GrowthX has been engaged to build and scale a content strategy for Anything's blog. This meeting was a weekly sync to finalize technical infrastructure (blog platform choice) and align on content workflow to accelerate publishing velocity. Dhruv Amin (Anything's founder/CTO) needed the platform decision made so he could start building; Aida and Nathalie from GrowthX were managing content production and editorial workflow. The team had been deliberating between platform options and visual requirements, so the focus was on getting to first published post quickly and validating what actually drives growth before investing in heavy visual enrichment.

---

## Relevance

**To GrowthX Delivery:**
- Content workflow streamlining is a key efficiency lever: shifting from full-list review to curated priority lists (20 out of 99 topics) will accelerate time-to-publish and reduce approval bottlenecks.
- Publishing-first strategy (minimal initial visuals, enrich later) aligns with AEO/SEO best practices — indexing and ranking don't require images, so speed matters more than polish early.
- Direct table embed capability in Sanity CMS is a unique advantage for GrowthX's LLM-friendly content approach.

**To CheckThat / AEO:**
- Blog will use UTM-based attribution and GA4 exploration reports to track user journeys from blog posts to signups — useful signal for measuring content impact on awareness/consideration.
- Content mix includes both commercial and informational intent keywords, typical of AEO content strategy (serving both humans and LLMs).

**To GrowthX Business Development:**
- Early signal of healthy client relationship: Anything (Dhruv) is highly engaged, collaborative on trade-offs, and committed to moving fast.
- Potential reference value: if blog drives measurable signups/conversions, Anything becomes a strong case study for content-driven growth in the product space.

---

## Overview

- **Blog Build Approved:** Dhruv will build the Sanity CMS blog, enabling direct table embeds (a key SEO feature) and using abstract, text-free featured images to simplify content refreshes.
- **Content Workflow Streamlined:** GrowthX will now propose \~20 priority topics for Dhruv's quick approval, bypassing the slow review of the full 99-item list to accelerate publishing.
- **Publishing First, Enrich Later:** To prioritize speed, articles will launch with minimal visuals. High-performing posts will be enriched later with custom graphics and product screenshots.
- **Attribution Strategy Defined:** GA4 will track blog-driven signups via UTM codes on CTAs. This method is required because the server-side signup event is not visible to GA4.

---

## Key Topics

### Blog Platform Build

  - **Platform:** Sanity CMS, built by Dhruv.
  - **URL Structure:** `/blog/article-slug` or `/insights/article-slug`.
  - **Key Features:**
      - **Direct Table Embeds:** Enables simple copy-ppaste of tables, a key feature for LLM-friendly content, bypassing Webflow's complex HTML conversion.
      - **CTA Fields:** Dhruv will build the CTA component; Aida will provide copy examples.
      - **SEO Tagging:** Articles tagged "SEO" will appear in a dedicated section.
  - **Featured Images:**
      - **Style:** More abstract than the initial "flowery" AI-generated concepts.
      - **Format:** Text-free images only. This avoids manual re-creation when article titles are updated.

### Content Workflow & Strategy

  - **Topic Selection:**
      - **Problem:** Reviewing the 99-item keyword list was a bottleneck.
      - **Solution:** GrowthX will propose a curated list of \~20 priority topics (mixing commercial and informational intent) for Dhruv's quick approval.
  - **Visuals & Publishing:**
      - **Problem:** Callie requested more visuals (flowcharts, screenshots).
      - **Decision:** Prioritize publishing speed over initial visual enrichment.
          - **Rationale:** Images don't impact SEO ranking or indexing.
          - **Process:** Launch articles quickly, then enrich high-performing posts later.
      - **Resources:** Limited product screenshots are available at `createanything.com/brand`.

### Performance Tracking & Attribution

  - **Goal:** Attribute signups and subscriptions to specific blog posts.
  - **Challenge:** The server-side signup event is not visible to GA4.
  - **Solution:** Add UTM codes to all blog CTAs.
      - **Mechanism:** GA4 exploration reports will track user journeys from specific blog URLs.
      - **Implementation:** Dhruv will automate UTM code addition in the blog build.
  - **Next Step:** Aida will research best practices for UTM-based attribution from long-term clients.

---

## Action Items

**Dhruv Amin (Anything)**
- Build Sanity blog (SEO tag, tables, images-only); then stage 1st calibration post and add UTMs

**Aida Knezevic (GrowthX)**
- Draft CTA fields/copy; send to Dhruv for CTA mockups
- Update Katya re: featured images; request more abstract versions
- Email Callie: publish-first approach; enrich later
- Consult GrowthX team re: blog tracking; then propose approach to Dhruv

**Nathalie Schrans (GrowthX)**
- Send 20-topic priority list to Dhruv; then approve ideas and start production

---

## Transcript

**Aida Knezevic:** How's your week going?

**Nathalie Schrans:** It's good. We're making progress in the bulk of the roadmap work, which was very time-consuming. Most of that work is done now. I'm just creating a high-level version to present in the Augment Sync tomorrow.

**Aida Knezevic:** That's good. This week's a little easier. We're going to be out over Christmas and New Year's.

**Nathalie Schrans:** Everyone needs that.

**Aida Knezevic:** Honestly, most companies have people out, so it's a waste of time to be working.

**Nathalie Schrans:** Exactly. No point in stressing when you can be recovering and recharging.

**Erik O'Brien:** Hey, bye.

**Nathalie Schrans:** Cheers.

**Erik O'Brien:** Thought I would be late.

**Aida Knezevic:** We switched to daylight saving time on Sunday.

**Nathalie Schrans:** That's right. You guys are a week before us.

**Aida Knezevic:** It's already almost November.

**Nathalie Schrans:** It's wild how daylight saving time affects health and logistics. It's hard to change out of.

**Dhruv Amin:** What are we talking about?

**Aida Knezevic:** Daylight savings.

**Dhruv Amin:** Oh, okay. I haven't scarred you guys too much in three weeks?

**Aida Knezevic:** We're good. I'm going to share my screen to show the agenda. Just a quick check-in on updates.

**Dhruv Amin:** These are the updates we'll cover. Anything on your mind as a priority?

**Dhruv Amin:** I want to get to the first calibration blog ASAP. I know we're close. Once you get it up on the site, you'll probably see things that need fixing for ranking.

**Aida Knezevic:** Okay.

**Dhruv Amin:** For the URL structure, I'm thinking `/blog/article-slug` or `/insights/` — something that's still linkable from Google. In Sanity, CTAs are important because I'm building them. What fields does every CTA need? We can discuss async on Slack too. We'll tag articles as SEO, GEO so they show up in a separate blog section.

**Aida Knezevic:** That sounds good. I can help write CTAs for different use cases. I've done that for other clients. Usually there's a headline tag, a description, and a call-to-action button.

**Dhruv Amin:** If you have high-converting CTAs from other clients that look beautiful, I can have our design firm mock up a few versions and I'll build the front end. Anything else you want in the blog?

**Aida Knezevic:** Yes — Webflow has this annoying thing where tables have to be converted to HTML code. In Sanity, can we just copy and paste tables? LLMs love them, and we won't need converters.

**Dhruv Amin:** That should be built in. How do you handle internal linking?

**Aida Knezevic:** We have a step that adds links automatically, but you don't have much content yet. We'll do a lot of manual linking as we publish and go back to add links.

**Dhruv Amin:** We control everything here with Sanity, so whatever you think makes it perform better, let me know. I'll start building now so we can get it up.

**Aida Knezevic:** When it comes to publishing, Callie left comments I've resolved — adding screenshots and expanding sections. This calibration post can go into your CMS as soon as it's ready.

**Dhruv Amin:** Do you stage them manually or do you want an upload script?

**Aida Knezevic:** We stage manually, but we can do automated publishing. Sanity supports it, but I need to check with our dev team.

**Aida Knezevic:** For images, these are the featured images Katya created. She used your current blog as inspiration. Thoughts?

**Dhruv Amin:** It's a little flowery. We'd prefer something more abstract — one layer more. Do they look blurry to you?

**Aida Knezevic:** That's the style — high definition but intentionally blurry.

**Dhruv Amin:** Okay, fine. How is she making these?

**Aida Knezevic:** She has a prompt using GPT and designs it so she can tweak it back in.

**Dhruv Amin:** I'll let her know about the feedback and she can adjust.

**Dhruv Amin:** Do you want images just as images, or with text overlays of the title?

**Aida Knezevic:** Just images. When we refresh content and change titles, we don't want to remake images too.

**Dhruv Amin:** Makes sense. Thank you.

**Aida Knezevic:** Nathalie, content update?

**Nathalie Schrans:** We got Callie's feedback on two outlines and we're starting drafts for "digital products ideas" and "how college students make money." The "lovable alternatives" article still needs review. Once we get that, we'll move to draft. Callie also requested more visuals — flowcharts, income timelines, product screenshots — which we'd need from you. We're already adding visual elements like bullet lists and tables, but adding more visuals would require reworking the workflow.

**Dhruv Amin:** What do other clients do, and does it actually impact growth? That's what we care about.

**Aida Knezevic:** Imagery comes second. Publishing is number one. Images don't impact indexing or ranking, though they can affect time on page. We treat images as enrichments. If a post does really well, we go back and add screenshots or custom graphics. Images shouldn't hold up publishing because they don't impact indexing or ranking.

**Dhruv Amin:** Exactly. That's my fear — we do tons of work on beautiful posts and then nobody cares, Google doesn't rank them, and we wasted time. Plus, we don't even know if LLMs read images.

**Nathalie Schrans:** Yeah, and even if they can, do they actually account for them when citing or showing information?

**Dhruv Amin:** You have resources at `createanything.com/brand`. There are product screenshots there. Not a ton, but there are some. Callie is also organizing a board for more assets for social. You can use these if needed. For articles, the image would only be useful if it's illustrative, like "five ways to make money." Let's tell Callie we're publishing first and enriching high-performers later.

**Aida Knezevic:** Okay. Good approach.

**Aida Knezevic:** For content approvals, we have 99 keyword ideas. Should we bring those all to you?

**Dhruv Amin:** Here's my thought: shouldn't you just tell us what you think are the best? You're looking at this more than I am. I don't want to review all 99. I'm looking at keyword volume, difficulty, and whether it overlaps with existing content. Like, do we need "15 ways to make money with AI as a florist" if we're already doing "15 ways to make money with AI"? Can you just pick the top ones and I'll tell you if any don't work for us?

**Aida Knezevic:** Yeah, we can put together a list of about 20 topics we recommend prioritizing. Most clients want to do approvals themselves, so that's what we default to. But Nathalie can pull together recommended keywords and we'll go from there.

**Dhruv Amin:** That works. I can review 20 and flag any that won't work for us or where we don't have good examples. Looking through 99 is too much. What are your top suggestions?

**Aida Knezevic:** We want a mix of commercial and informational intent, both important. Things like "lovable alternatives" have low volume but matter for LLM. So we'll balance educational and commercial. You'll see a list of 20, you flag any that won't work, and that's faster than going through 90.

**Dhruv Amin:** "How to develop an app" — that's ambitious but cool. Mobile app designs, patterns... these all seem great. The hard part is keeping it from sounding too generic.

**Aida Knezevic:** We'll curate the list. Anything else?

**Aida Knezevic:** If you have questions about the Looker dashboard, let me know. I hope that video was helpful.

**Dhruv Amin:** It was. For context, you're using Google Analytics 4 for client-side events, right?

**Aida Knezevic:** Yes, everything GA4 can collect.

**Dhruv Amin:** What do you typically do for event tracking on blog frontends? Do we need to add events for blog links? How do we track signups from posts?

**Aida Knezevic:** We had one client add UTM codes to CTAs and track them in HubSpot. In GA4, we create exploration reports that track users from a blog post and what they do next. That's helpful when you have case studies — knowing where people go after reading a post.

**Dhruv Amin:** We can do that with URLs, right?

**Aida Knezevic:** Yeah, we'd use URLs.

**Dhruv Amin:** And GA4 can see authenticated URLs too? It doesn't distinguish between auth and unauth users?

**Aida Knezevic:** Right. It tracks anybody on the site.

**Dhruv Amin:** Okay, you have what you need from a page view perspective. The events we care about are signups. There's a server-side event, but GA4 won't capture it. There are client-side events, but there are a million signup flows. I could set up UTM codes on blog links automatically. The other event is subscriptions, but for now, signups are the proxy.

**Aida Knezevic:** I can ask the team what they do with long-term clients and what works best. I'll get back to you this week.

**Dhruv Amin:** Okay.

**Aida Knezevic:** Nathalie, anything else?

**Nathalie Schrans:** No. I'll approve ideas and start the production process. Dhruv, should we keep sharing outlines for you and Callie to review?

**Dhruv Amin:** Yes, that's great. My goal right now is to be involved up front. I'm busy, so I can't be as involved as I am now long-term. My ambition is to get out of your way eventually. But right now, I want to be hands-on. Just loop me in up front so we nail voice, tone, and concepts all the way to our first successful post. Then I'll hand it off to Callie for scaling and ongoing success. For now, while we're getting the technical setup right and want to get the first indexed post, I should be paying attention.

**Nathalie Schrans:** That makes sense. We want to get it right before scaling so we don't have to go back and change things.

**Nathalie Schrans:** I'll let you and Callie know when we have new outlines to review.

**Dhruv Amin:** Thank you.

**Nathalie Schrans:** Thanks, Dhruv. See you next week.
