# Dimmo <> GrowthX Weekly Sync

<metadata>
date: 2025-04-30
time: 19:04 UTC
duration: 28 minutes
organizer: Prateek Gupta (GrowthX)
participants: Prateek Gupta (GrowthX), Lucas Swartsenburg (Dimmo)
fathom_recording_id: 60117349
fathom_url: https://fathom.video/calls/289114511
share_url: https://fathom.video/share/m5vyrFJUtwyv7NsSMF_J3Lzs4gHZzSsu
source: fathom
enriched_on: 2026-03-04 00:32 UTC
</metadata>

---

## Summary

GrowthX (Prateek) and Dimmo (Lucas) aligned on structural SEO improvements to the Dimmo website, including implementing "long short sections" for product pages, decoupling demo videos from product pages to prevent keyword cannibalization, and implementing 301 redirects from blog review pages to product pages. The website is gaining traffic with 260 clicks (up 24% from 210), impressions up 20% to 72,000, and 24 growth articles ranking—but click-through rates on those articles are underperforming, suggesting a CTR or content-targeting issue to investigate.

---

## Context

Dimmo is a B2B SaaS product comparison and review platform. GrowthX is handling their SEO strategy. This weekly sync is part of the ongoing delivery engagement where the GrowthX team (specifically Prateek) is advising on technical SEO, content structure, and keyword strategy to improve organic visibility and indexing. Dimmo's CMS now supports a new "long short sections" feature for organizing product page content, and the team is optimizing URL structure and redirects to improve crawlability and prevent cannibalization across review, product, feature, and video content.

---

## Relevance

**To GrowthX Delivery:**
- Implementing multi-layer internal linking strategy (same category + same product) across three content categories (best software, alternatives, features) — demonstrates scalable SEO methodology
- Decoupling video content from product pages using URL structure `/videos/[product-name]/[video-name]` to prevent keyword cannibalization and improve indexing — tactical SEO pattern applicable to other content-heavy clients
- 301 redirect strategy for legacy blog review content — standard content consolidation approach now in motion
- Prateek investigating Google's "watch page" detection issue for video pages — potential technical SEO blocker requiring markup/schema debugging

**To CheckThat:**
- Video content visibility issue: Dimmo's videos aren't showing up in Google's video results despite being video-focused pages — CheckThat could audit whether AI engines are properly indexing video content or if schema/structured data is missing

**To GrowthX Business Development:**
- Account health signal: 24 growth articles ranking but underperforming CTR (72,000 impressions, low click conversion) — suggests potential follow-up work on content optimization, snippets, or meta descriptions
- Home page content (Troy's post) driving most new traffic — indicates blog/news feed strategy is working; could expand
- Steady progress on technical foundations (content structure, URL strategy, redirects) supports account retention and expansion opportunity

---

## Overview

- Product page content structure updated with new "long short sections" feature
- URL structure for demo videos to be decoupled from product pages for better SEO
- Blog review pages to be 301 redirected to corresponding product pages to avoid keyword cannibalization
- Website performance improved with 260 clicks (up from 210), but growth article clicks underperforming despite ranking

---

## Key Topics

### Product Page Content Structure

  - New "long short sections" feature added for content organization
  - Headings updated to H2s for better structure
  - Prateek to publish one page as a sample for Lucas to review before full implementation

### Internal Linking Strategy

  - Two-way internal linking implemented:
    1.  Same category: 5-10 links to other alternatives articles
    2.  Same product: Links to related pages (features, reviews) for the same product
  - To be implemented across all product categories (best software, alternatives, features)

### URL Structure for Demo Videos

  - Decision to decouple demo videos from product pages
  - [New structure: `/videos/[product-name]/[video-name]`](https://fathom.video/share/m5vyrFJUtwyv7NsSMF_J3Lzs4gHZzSsu?tab=summary&timestamp=621.0)
  - Each product will have its own subcategory of videos
  - Aims to improve indexing, ranking, and keyword targeting

### SEO Issues with Video Pages

  - Google not recognizing video pages as "watch pages"
  - Lucas seeking solution to get videos showing up in Google search results
  - Prateek to investigate and provide a solution

### Blog Review Pages Redirection

  - Existing blog review pages causing keyword cannibalization with product pages
  - Decision to 301 redirect blog review pages to corresponding product pages
  - Example: `/blogs/nooks-review` will redirect to `/products/nooks`

### Website Performance Update

  - Overall clicks increased from 210 to 260
  - Impressions up 20% (60,000 to 72,000)
  - 24 growth articles ranking in top positions
  - Click-through rate for ranking articles lower than expected

---

## Action Items

**Prateek Gupta (GrowthX)**
- Investigate why Google isn't recognizing video pages as watch pages. Debug the issue across video pages, evaluate scope, and provide solution to Lucas.

**Lucas Swartsenburg (Dimmo)**
- Implement 301 redirects from blog review pages to corresponding product pages (e.g., `/blogs/nooks-review` → `/products/nooks`). Remove duplicate content flagged in SEO audit.

---

## Transcript

**Prateek Gupta:** Okay, so we have lots of points to cover. Let me dig into the content structure updates. In terms of the product page improvements you shared, I'll need a screenshot or video showing how we publish the new pages. I have the content ready—just waiting for you to share the CMS updates so I can implement them. Can you show me how to make this as easy as possible?

**Lucas Swartsenburg:** So on the product page, you can now scroll down and there's a section called "long short sections."

**Lucas Swartsenburg:** You click the plus button and add a heading.

**Lucas Swartsenburg:** Then you add the short text, the short element text.

**Lucas Swartsenburg:** You can add the longer element text, and it will generate a heading and section for each one.

**Lucas Swartsenburg:** So for section two, you can create another heading.

**Lucas Swartsenburg:** These headings should be H2s. I'm not sure why they're not rendering correctly right now, but I think they should be H2s.

**Prateek Gupta:** Okay, let's confirm they're H2s and update them if they're not.

**Lucas Swartsenburg:** Right, so we should convert all of them to H2s.

**Lucas Swartsenburg:** Currently there's only one H1.

**Prateek Gupta:** Yep, one H1 and the rest should be H2s.

**Lucas Swartsenburg:** Okay, so should we update all of them to H2s?

**Lucas Swartsenburg:** Yes.

**Lucas Swartsenburg:** Easy.

**Lucas Swartsenburg:** Cool. Let me double-check the implementation. Okay, so we've got the long short section there. It's just tiles. Okay, so can you add an action item for me to update that?

**Prateek Gupta:** Yeah, I'll take care of it.

**Lucas Swartsenburg:** Okay.

**Prateek Gupta:** Let's go back to the Stappy product page where we were working.

**Lucas Swartsenburg:** Yeah, here you go.

**Prateek Gupta:** For the existing above section, nothing needs to be changed, right?

**Lucas Swartsenburg:** Nothing to be done. You can add new sections with these headings, and they'll appear above the above section.

**Prateek Gupta:** Okay. I'll remove the above section and work with the new structure.

**Lucas Swartsenburg:** Tell us what you want to do, and I'm happy to make adjustments.

**Prateek Gupta:** I'll publish one page as a sample and send it to you for approval. Then we can publish across all product pages.

**Lucas Swartsenburg:** That's perfect. I've already updated the headings now—they all show as H2s. I'll push this live right now.

**Prateek Gupta:** Great, I'll connect with the developer and pass them the recording so they understand the new structure.

**Lucas Swartsenburg:** Cool. And the updated page should be live in five to ten minutes.

**Prateek Gupta:** Perfect. Now let's move to the internal linking strategy. We have two-way internal linking: same category and same product links.

**Prateek Gupta:** If a page is about alternatives, include five to ten links to other alternative articles. If it's about a specific product like Pipedrive alternatives, add internal links to related Pipedrive pages like features, reviews, and product comparisons.

**Lucas Swartsenburg:** Got it. So this is internal linking across the alternatives section.

**Prateek Gupta:** Exactly. We're implementing this across three categories: best software, software alternatives, and software features.

**Lucas Swartsenburg:** Sounds good.

**Prateek Gupta:** No confusion with the two-way linking approach?

**Lucas Swartsenburg:** Nope, I've got it.

**Prateek Gupta:** Great. Now, let's discuss the URL structure for demo videos. Currently, demo videos are nested under product pages, but we should decouple them.

**Lucas Swartsenburg:** So you're saying decouple the videos from the products completely?

**Prateek Gupta:** Right. Here's why: each video will have its own transcript and keywords. If videos stay under product pages, they'll cannibalize keywords and make indexing worse. A separate `/videos/[product-name]/[video-name]` structure keeps each piece separate.

**Prateek Gupta:** From a user perspective, visitors either want to read an in-depth review or watch a demo video. Separate navigation for each improves UX. Plus, a pillar page listing all demo videos improves ranking and indexing across the whole video cluster.

**Lucas Swartsenburg:** Okay, so let's decouple the videos from the products. What should the structure be?

**Prateek Gupta:** It could be `/videos/[product-name]/[video-name]` or `/video/[product-name]/[video-number]`. Either works. The key is keeping video pages separate so each product has its own subcategory of videos.

**Lucas Swartsenburg:** So we could have `/videos/SendOS/` with a list of all five SendOS videos?

**Prateek Gupta:** Exactly. SendOS would list all its videos, whether that's five, ten, or more.

**Lucas Swartsenburg:** Got it. I can make that happen.

**Prateek Gupta:** Actually, before we move forward, can you show me something? The video pages still aren't being recognized as "watch pages" by Google.

**Lucas Swartsenburg:** Yeah, even with the video pages, Google's indexing report says they're not watch pages. I need a solution so they show up in Google's video results. What do I need to do to make these video pages recognized as watch pages?

**Prateek Gupta:** Not sure why that's happening. Let me debug this and check if it impacts all videos. I'll evaluate the scope and give you a proper solution.

**Lucas Swartsenburg:** Ideally, all our videos should show up in Google search results. If someone searches for "SendOS demo videos," we want them showing up in the video section, not as YouTube results.

**Prateek Gupta:** Yep, exactly. We should be competing there.

**Lucas Swartsenburg:** I'll keep the structure similar to what we discussed, and I'll think about the watch page issue.

**Prateek Gupta:** Good. So the structure would be `/videos/[product-name]` listing all that product's videos.

**Lucas Swartsenburg:** Yep, that works.

**Prateek Gupta:** Now, one more thing I wanted to discuss: the blog review pages. The previous agency created product review pages in the blog section, but we also have separate product pages. This is causing keyword cannibalization.

**Prateek Gupta:** For example, the "Nooks review" blog page and the product page are both targeting the same keywords. We should 301 redirect all blog review pages to their corresponding product pages. For example, `/blogs/nooks-review` redirects to `/products/nooks`.

**Lucas Swartsenburg:** So we're removing the content entirely?

**Prateek Gupta:** We're 301 redirecting the old review pages to product pages. Not deleting, redirecting. That way we consolidate authority and avoid duplicate content.

**Prateek Gupta:** This also improves indexing because we're not competing with ourselves.

**Lucas Swartsenburg:** That makes sense. I'll work on implementing that.

**Prateek Gupta:** Good. Now for performance: we improved significantly this week. Last week was 210 clicks; this week we hit 260 clicks. Impressions are up 20% from 60,000 to 72,000.

**Prateek Gupta:** The bump came mostly from the home page—Troy had a post that drove a lot of traffic.

**Prateek Gupta:** In terms of keyword rankings, we have 24 growth articles in top positions now. That's great. But here's the issue: even though they're ranking, they're not generating the clicks we expected. Impressions are up, but clicks are down.

**Lucas Swartsenburg:** Okay, sounds like an opportunity to look at title tags or CTR.

**Prateek Gupta:** Exactly. These are small numbers in the early days, but I wanted to check if there's seasonality or something else we should evaluate to understand why these keywords aren't converting to clicks.

**Lucas Swartsenburg:** Okay, sounds good. I'd really like to understand the video page issue—why Google isn't picking us up as a video source.

**Prateek Gupta:** As soon as I get answers on that, I'll let you know.

**Lucas Swartsenburg:** I'll get you that list of implementation items we discussed today.

**Prateek Gupta:** Perfect. I'll send you the technical items once we wrap up.

**Lucas Swartsenburg:** Got it, it's in the queue.

**Prateek Gupta:** Thank you, Lucas.

**Lucas Swartsenburg:** Thank you, Prateek.

**Prateek Gupta:** Bye.
