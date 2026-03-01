# Augment Code <> GrowthX Weekly Sync

<metadata>
date: 2026-02-25
time: 18:00 UTC
duration: 24 minutes
organizer: Liz Kushnereit (liz@growthx.ai)
participants: Molisha Shah (Augment Code), Sylvain Giuliani (Augment Code CEO), Liz Kushnereit (GrowthX), George Haikal (GrowthX)
fathom_recording_id: 125332143
fathom_url: https://fathom.video/calls/578884393
share_url: https://fathom.video/share/xqsxwKZnBhszkMByakUQj_nxjBhpG8qG
source: fathom
enriched_on: 2026-02-27T12:30:00Z
</metadata>

---

## Summary

Sylvain and Liz aligned on Intent app as primary focus with 500 downloads/day OKR and 50k weekly organic traffic target. Key initiatives include implementing dynamic sidebar CTAs across the blog, launching a free Code Review trial to improve conversion, and leveraging PostTag data to prioritize high-performing content. GrowthX will focus on publishing bottom-of-funnel Intent content while ensuring proper tagging in Spectrum CMS.

---

## Context

This meeting represents a strategic realignment following the launch of Intent, Augment Code's new free AI-powered code analysis app. Sylvain Giuliani, CEO of Augment Code, and Liz Kushnereit, GrowthX's content and demand generation lead, discussed how GrowthX's SEO and content efforts will drive user acquisition for Intent.

The Intent app has shown strong product-market fit with an 18% conversion rate on the landing page, but top-of-funnel awareness is limited. GrowthX's role is to generate high-intent organic traffic through specialized content (particularly "alternatives" and comparative pieces) that drives downloads. This represents a shift from the previous focus on Code Review content, though that product remains strategically important with a planned free trial launch to improve its conversion funnel.

---

## Relevance

- **For GrowthX Content Team:** Focus on publishing bottom-of-funnel Intent content (e.g., alternatives, tool comparisons). Prioritize content with high search volume that targets intent seekers. Use PostTag data to identify top-performing content and replicate success patterns.
- **For GrowthX Operations:** Implement PostTag reporting system for Intent downloads by content type. Send weekly summaries to Sylvain for his Thursday CEO memo. Tag all Intent articles in Spectrum CMS with product metadata to enable dynamic CTA functionality.
- **For Augment Code:** Monitor Intent download velocity against 500/day target. Prepare weekly reporting for internal company memo. Coordinate with GrowthX on content roadmap and messaging (positioning doc from Roz).
- **For Blog & Product Integration:** Immediate action needed on CTA management. Sidebar CTAs must dynamically switch based on content type (Intent vs Code Review). Longer-term: Build component library for flexible CTA insertion based on Funnel and Product tags.

---

## Overview

- **Intent Downloads are the \#1 Priority:** The primary goal is driving 500 Intent downloads/day to build a community and accelerate growth.
- **New OKRs Set:** New targets are 500 Intent downloads/day and 50k weekly organic traffic (up from a 34k 4-week average).
- **Immediate CTA Pivot:** Blog CTAs will be updated to promote Intent, starting with a quick sidebar change and followed by a more robust, component-based solution.
- **Code Review Trial Launching:** A new free trial for the Code Review product is launching next week to improve its "garbage" conversion rate.

---

## Key Topics

### New OKRs & Growth Strategy

  - **Intent Downloads:** The top priority.
      - **Goal:** 500 downloads/day.
      - **Rationale:** Build a community and accelerate growth toward a 50k user target.
      - **Current Performance:** The Intent landing page converts at a high 18%, validating the product experience and shifting focus to top-of-funnel traffic.
  - **Organic Traffic:**
      - **Goal:** 50,000 weekly organic visitors.
      - **Baseline:** 34,000 weekly average over the last four weeks.
  - **Code Review:**
      - **Goal:** Improve the "garbage" conversion rate of Code Review content.
      - **Solution:** Launch a new free trial next week (e.g., 10-20 free pull requests) to provide a stronger CTA.

### Intent Content & CTA Pivot

  - **Content Strategy:**
      - **Focus:** Create bottom-of-funnel (BOFU) content (e.g., "alternatives" articles) to capture high-intent users.
      - **Guidance:** Use PostTag data to identify top-performing content and replicate its success.
  - **CTA Implementation:**
      - **Problem:** Current blog CTAs promote the main product, not the new Intent app.
      - **Immediate Fix:** Change the sidebar CTA on relevant articles to promote "Download Intent for free."
      - **Longer-Term Solution:** Build a component-based CTA library that dynamically updates based on article tags (e.g., `product: intent`).

---

## Action Items

**Liz Kushnereit (GrowthX)**
- Set up PostTag reporting for Intent downloads by content; then send weekly summary to Sylvain
- Send weekly Intent GrowthX update to Sylvain for Thu memo
- Publish high-SV BOFU Intent content (prioritize alternatives and tool comparison pieces)
- Implement dynamic sidebar CTA (Intent vs Code Review) across blog (quick fix: 5 minutes)
- Tag Intent articles in Spectrum; then update sidebar CTA to Intent

**Sylvain Giuliani (Augment Code)**
- Coordinate Intent positioning with Roz (draft positioning doc to be shared)
- Include GrowthX Intent content metrics in weekly company memo
- Prepare free Code Review trial launch (planned for following week)

---

## Transcript

**Liz Kushnereit:** Thank you.

**Sylvain Giuliani:** What's up, Liz? I'm back at your office. You know, I feel like you're the excuse I use to go to GrowthX—one of the people on this team to be at the office.

**Liz Kushnereit:** Yeah, okay. That's funny. I was watching some of your videos, which were also filmed at the office.

**Sylvain Giuliani:** It's a good backdrop, you know? Makes us look like a cool startup compared to an office in Palo Alto that looks like a 90s business park with yellow lights and drop ceiling.

**Liz Kushnereit:** Yeah, also the plants. I feel like the plants make the office look really good.

**Sylvain Giuliani:** Yeah, mid-century modern aesthetic. Repurposed firehouse kind of thing. Okay, I got some OKRs for you. I got a bunch of things to discuss, so we can go for it and discuss this at the end too.

**Liz Kushnereit:** Yeah, I'm building a lot right now. I put in some OKRs based on SEO baselines, which was mostly 10% month-over-month increase. We can adjust those if you have different targets. I need to establish AEO OKRs going forward, but that's a different process and requires more capacity.

Overall, things are still trending up with stronger Code Review ownership. The challenge is a lot of it's related to open source code review, so there's still room for a canonical piece that recommends Augment Code. I'm working on post-QBR planning with a big project plan. The component library is still P0, and I'm working through other workstreams.

**Liz Kushnereit:** For the Intent app, I've documented everything we're shipping and our product matrix.

**Sylvain Giuliani:** The focus is Intent, Intent, Intent. The OKR is basically: can we get SEO to drive 500 Intent downloads per day? That's our primary target right now because it's new and highly trackable.

The big picture is to pace as fast as possible toward 50,000 community members. Even getting to 3,000-4,000 downloads per day would be strong. GrowthX should carry its own share. I know it's a slow start, but that's the goal.

The landing page conversion is already strong at 18%—people who land on the Intent page download the app at that rate. We'll worry about sign-ups and longer-term metrics end of March or April. Right now I'm focused on asking: what did we do today to get more downloads? If people aren't downloading, they aren't aware and they aren't trying. That's the reasoning.

**Sylvain Giuliani:** On Code Review, I'm excited about what you showed me. Hopefully next week we'll have a nicer free trial—something like the first 10 or 20 free pull requests. That's a much better CTA for that traffic because right now the conversion rate is garbage because the rest of the flow is garbage.

With a good CTA and trial, we should see better conversion. That's a big focus alongside Intent.

The second OKR is increasing organic traffic. We're currently at 34,000 weekly average over the last four weeks. Can we get to 50,000? That's the high-level goal. We can add more as we progress.

**Liz Kushnereit:** The category ownership with the BOFU strategy should work, especially since Intent is easy to install.

**Sylvain Giuliani:** I'm talking to Roz today about the positioning. She sent me a draft positioning doc last night that should help clarify what Intent is and how it's different. We're shipping new versions constantly—at least twice a day. It's a straightforward story: free app, powered by Cloud Code, no sign-up required, just download and go.

Let's look at the PostTag data. We should be able to see which content drives Intent downloads and analyze conversion rates by content type. For example, "Guides" should drive downloads. I notice 31 people who visited Guides wandered around and ended up downloading Intent—who are those people? That's the insight we need. Let's slice the data to see which specific content drives the most downloads.

**Liz Kushnereit:** Yes, that makes sense.

**Sylvain Giuliani:** So which piece do you think drives the most? The "Code Review vs AugmentCode" comparison piece drives 81 conversions—people find us through that and then download Intent. Even 10 people from one piece end up downloading. We can slice that data quickly to see patterns.

**Liz Kushnereit:** Yeah, I can prioritize those top performers in our content roadmap.

**Sylvain Giuliani:** Here's important context: every Thursday I write an internal memo to the company covering goals and progress. What I need from you is visibility into: what is GrowthX doing this week to drive more Intent downloads?

Your update should be straightforward: we're writing more content, optimizing content. I'll use PostTag as the data source to report: what's changing, what's driving downloads? For example, "GrowthX is publishing 20 alternatives and tooling comparison pieces."

As long as you keep me updated, we can make this work. I know this week is just the first week doing this—we're laying groundwork for impact next week. I don't need perfection, just visibility. Tell me: what did we do this week to drive growth? This week it might be "we're publishing content," next week we'll see the lift.

**Liz Kushnereit:** Yeah, we're going to publish a bunch of content.

**Sylvain Giuliani:** That's the update I need. For Intent specifically, since we're still shipping new features.

**Sylvain Giuliani:** For other workstreams, keep the machine running. But for Intent, I'm sending memos tracking downloads and DAUs. Example: "Liz published 10 blog posts this week. SEO takes time, but look at last week's content starting to rank. YouTube colleague created five tutorial videos." That's what I'm reporting to the company.

**Liz Kushnereit:** I'll get you a summary. I'll prioritize high search volume BOFU content since we're not targeting paid traffic. Intent is the priority and we'll shift capacity to focus there.

**Sylvain Giuliani:** Easy.

**Liz Kushnereit:** I'm nervous, but it'll be fine. With Code Review, we owned the category but weren't the fully recommended choice. Now we have the chance to apply all those learnings and actually become the recommended choice with Intent. There's a real opportunity to do it really well.

**Sylvain Giuliani:** We're still doing Code Review—we're not giving up on that. But let's commit to Intent. All hands. We're also writing pillar content and leadership pieces around Intent. That anchors backlinks and seeds ideas for other SEO work.

We're shipping a RALF loop feature this week or next. Once it ships, let's update the Intent CTA to reflect it. CTA management is P0, so let's prioritize that.

**Liz Kushnereit:** Heard. I'll get that done tomorrow.

**Sylvain Giuliani:** Do you have a plan for the CTA implementation?

**Liz Kushnereit:** I was planning a complex variable library, but that would take 2-3 days. We could improve how we're using the current component. Editors are doing inline CTAs, so we could optimize that approach. It's in the project plan, but I need to think it through.

**Sylvain Giuliani:** Let me ask: do we tag content with product metadata?

**Liz Kushnereit:** We're tagging with Funnel and Product. That can inform which CTA displays based on tags.

**Sylvain Giuliani:** Here's the quick fix: just change the sidebar CTA to promote Intent based on blog category. That's a five-minute job. The CTA on Intent articles should say "Download Intent for free," not "Install Augment." Right now Intent is buried—nobody sees it. We'll reuse the same download component from the Intent product page, and it changes based on whether the article is tagged `product: intent`.

**Liz Kushnereit:** Got it. Articles need to be tagged in Spectrum. We haven't tagged any as Intent yet, so we need to go back and update them. We can use the tagging agent—it works really well.

**Sylvain Giuliani:** Perfect. It works?

**Liz Kushnereit:** Yeah, it works really well. I can try it and batch update that field.

**Sylvain Giuliani:** Great. Let's test it on one article as a proof of concept to see how it performs. Let's use this one.

**Liz Kushnereit:** Good. All right, let's shift gears. Team break?

**Sylvain Giuliani:** Yeah, thanks for the time.

**Liz Kushnereit:** Okay, bye.
