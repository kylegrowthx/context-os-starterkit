# Blaxel <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-19
time: 19:58 UTC
duration: 36 minutes
organizer: team@growthxlabs.com
participants:
  - Paul Sinaï (Blaxel, Founder)
  - Aida Knezevic (GrowthX)
  - Nicolas Lecomte (Blaxel, Head of DevRel)
  - William Leborgne (GrowthX)
  - Kathy Lam (GrowthX)
  - Carly Piekos (GrowthX)
fathom_recording_id: 123855273
fathom_url: https://fathom.video/calls/571614109
share_url: https://fathom.video/share/EuPAEKEXunhzd-5gdv3Xaw-bj4Hc1yA3
source: fathom
enriched_on: 2026-02-27T18:45:00Z
</metadata>

---

## Summary

Weekly strategic sync between Blaxel and GrowthX on marketing and technical initiatives. Reviewed a new blog CTA component ready for deployment with requested enhancements (mid-page floating CTA, scroll-hide TLDR). Discussed technical SEO audit findings with critical fixes needed for search visibility, plus strategies for short-form content distribution and performance benchmarking using influencer partnerships.

---

## Context

This is a recurring strategic sync between Blaxel (an AI sandbox platform) and GrowthX (a content marketing agency). Blaxel is looking to improve marketing velocity through multiple channels: blog content, social media distribution, and third-party validation via benchmarks. GrowthX provides content strategy, SEO optimization, and partnership facilitation. The meeting focused on implementation timelines for blog CTA improvements, feasibility of short-form content creation (daily social posts), and alternative distribution strategies for performance benchmarks given challenges with maintaining existing open-source projects. Technical SEO issues on Blaxel's site are blocking search visibility and require immediate remediation including URL redirects and page renames.

---

## Relevance

**Content & SEO:** Critical technical SEO issues identified that must be fixed before content marketing efforts can achieve organic visibility; URL structure decisions (VM vs Sandbox rename) will affect authority and search rankings.

**Product Marketing:** CTA component implementation and short-form content strategy directly impact blog-to-awareness funnel and social amplification; benchmark content strategy is core to competitive positioning.

**Operations & Partnerships:** Decisions on content staffing (ghostwriter vs GrowthX team), influencer partnerships, and sponsorship budgets will drive resource planning; weekly sync cadence indicates active collaboration and fast iteration.

**Growth & Metrics:** Blog enhancements and daily social posts target increased audience engagement; benchmark distribution through influencers provides third-party validation and audience expansion.

---

## Overview

- **New Blog CTA:** A new CTA component is ready for use in blog posts. GrowthX will explore adding a mid-page floating version and investigate creating daily short-form content from long-form articles to match competitor cadence.
- **Benchmark Strategy:** Blaxel will create performance benchmarks (e.g., sandbox start times). GrowthX will explore using influencers for third-party validation and distribution, with Blaxel open to sponsorship.
- **Technical SEO Audit:** A Screaming Frog audit found critical issues (JS blocking, orphaned URLs, 404s). Blaxel will fix these to improve search visibility and is considering renaming the `/vm` page to `/sandbox` for clarity.

---

## Key Topics

### Technical SEO Audit

  - A Screaming Frog crawl identified critical technical SEO issues impacting search visibility.
  - **Key Issues to Fix:**
      - JavaScript blocking resources on specific pages.
      - Orphaned URLs in the sitemap.
      - Non-indexable URLs in the sitemap.
      - Canonicalized pages.
  - **Specific Problem:** The old `/sandbox` URL is a 404 error, likely linked from the CMS.
      - **Action:** Implement a 301 redirect to the current `/vm` page to preserve link authority and user flow.
  - **Potential Page Rename:** Blaxel is considering renaming the `/vm` page to `/sandbox` for better industry alignment.
      - **Concern:** Risk of losing SEO authority from the existing `/vm` URL.
      - **GrowthX Advice:** A 301 redirect from `/vm` to `/sandbox` would preserve authority, making the rename safe.

### Blog CTA Implementation

  - A new CTA component is ready for use in blog posts.
  - [**Implementation:** Add a simple `[CTA variant_name]` shortcode directly in the CMS.](https://fathom.video/share/EuPAEKEXunhzd-5gdv3Xaw-bj4Hc1yA3?tab=summary&timestamp=644.0)
  - **Enhancements Requested:**
      - A mid-page floating CTA to capture attention in long-form articles.
      - A TLDR section that disappears on scroll to reduce visual clutter.

### Short-Form Content Strategy

  - Blaxel wants to create daily short-form content (e.g., tweets) from long-form articles to match competitor cadence (2–3 posts/day).
  - **Inspiration:** The Twitter profile of Ivan, founder of Daytona.
  - **Challenge:** GrowthX has a policy against posting as founders to avoid misrepresenting their personality.
  - **Path Forward:** GrowthX will investigate two options:
    1.  **Company Account Posts:** Create short-form content linking to Blaxel's blog from the company social media account.
    2.  **External Resource:** Refer a trusted social media expert for Blaxel to hire directly.

### Benchmark Content Strategy

  - **Goal:** Create and distribute performance benchmarks (e.g., sandbox start times) to showcase Blaxel's advantages.
  - **Distribution Channels:** Social media, dedicated landing pages, blog posts.
  - **Challenge:** An existing open-source benchmark project is unmaintained (last updated ~1 year ago), making a contribution impractical.
  - **Proposed Solution:** Use social media influencers to create or validate benchmarks.
      - **Benefit:** Provides third-party validation and reaches a relevant audience.
      - **Blaxel:** Open to sponsorship, depending on cost.

---

## Action Items

**Nicolas Lecomte** (Blaxel)
- Implement mid-page floating CTA component with TLDR that disappears on scroll; share working demo with Carly & Kathy by next week
- Email Carly additional examples of short-form social content from competitors (reference: Ivan @ Daytona Twitter profile as inspiration)
- Set 301 redirect from /sandbox to /vm; then rename /vm to /sandbox and update all internal links

**Carly Piekos** (GrowthX)
- Consult GrowthX team on feasibility of daily short-form social content strategy; update Nicolas this week; add discussion to next strategy session agenda
- Email Nicolas technical audit summary document with prioritized fixes (JavaScript blocking, orphaned URLs, non-indexable URLs, canonicalization issues)
- Research potential social media influencers/experts in the DevRel space who could partner with Blaxel for benchmark content distribution (discuss sponsorship budget with Nico)

**Kathy Lam** (GrowthX)
- Reach out to existing influencer contacts to gauge interest in independent benchmark reviews for Blaxel; clarify sponsorship expectations

---

## Transcript

### Blog CTA Implementation

**Nicolas Lecomte (Blaxel):** I've sent documentation on how to use the CTA component. There's a default version and you can override with configurations I provided. We can try a live demo so you have a recorded version for your team.

**Nicolas Lecomte:** The CTA component is implemented simply using shortcodes in brackets within the blog post body. There are four variants available, and the text inside the code is easily editable. The design is bare bones right now, but I can iterate on the visual design side once you give feedback.

**Kathy Lam (GrowthX):** I like it. One suggestion: since we're creating longer articles, would you consider adding a mid-page floating CTA right below the TLDR? And when people scroll down, could the TLDR disappear to reduce visual clutter? I don't want to add too much engineering burden though.

**Nicolas Lecomte:** A floating CTA is a good idea, and making the TLDR disappear on scroll is doable.

### Short-Form Social Content Strategy

**Nicolas Lecomte:** We want to create daily short-form content (tweets) from our long-form articles to match competitor cadence—2-3 posts per day. I sent Ivan from Daytona's Twitter profile as inspiration. He posts multiple times daily about sandboxes, code, agents, hiring, fundraising—thought leadership mixed with product context.

**Carly Piekos (GrowthX):** I don't have direct experience with this at GrowthX, but I've worked with other clients on open graph images and social CTAs paired with blog articles. I can ask our team if we can create daily short-form content or recommend someone who specializes in social media for hire.

**Nicolas Lecomte:** So essentially, for every blog post we write, you'd generate short-form versions we can tweet about?

**Carly Piekos:** Yes, we could create open graph images, thumbnails, and mini blurbs for social platforms integrated into the blog pipeline. I'll ask our team and get back to you this week, then we can discuss at the next strategy session.

**Nicolas Lecomte:** We've considered hiring a ghostwriter because generating this content takes time. But you already have the pipeline, context, knowledge, and industry expertise. It would be optimized to reuse all that and produce different content formats.

**Kathy Lam:** Nico, I should clarify something. I asked our team if we could post as founders, and the answer is no. We don't want to misrepresent founder personalities. But posting links to your content on the GrowthX company account might be more doable. Carly will double-click on what's specifically possible.

**Nicolas Lecomte:** Is that only for blog posts, or does it apply to any founder posts?

**Carly Piekos:** I'll also research social media experts in the industry who might take on this work. We have lots of connections, so maybe we can find someone really good.

### Benchmark Content Strategy

**Nicolas Lecomte:** Benchmarks perform really well on Twitter. Something like: "We tested 100 sandboxes—what's the median time to start? Here's how every provider ranks." People love specific competitive benchmarks. This is end-to-end work: building the benchmark code, distributing the output, deciding where to post (blog, landing pages, social).

**Kathy Lam:** I saw an open-source GitHub project with someone from Claude involved. Would your team consider contributing to include Blaxel?

**Nicolas Lecomte:** We tried. The problem is that benchmark project is about a year old with no maintenance signals. There's no guarantee anyone would review or merge a pull request. If it was recent, we'd do it.

**Kathy Lam:** Alternative: work with social media influencers who do benchmark reviews. We've done this with other clients. They do the review, you sponsor it, and they reach their audience. If their audience matches Blaxel's target market, everyone wins.

**Nicolas Lecomte:** That could be part of the distribution strategy. We wouldn't manipulate results—just ask if they'd independently review and compare us fairly.

**Kathy Lam:** Let me reach out to influencers I know. But I need to know: would you budget for sponsorships?

**Nicolas Lecomte:** It depends on the sponsorship amount, but we're open to the idea.

### Technical SEO Audit

**Carly Piekos:** I ran a Screaming Frog crawl to audit your site. I want to review URLs in your sitemap, orphaned URLs, and non-indexable pages—these block bot crawling and hurt visibility.

**Carly Piekos:** Major issues found: JavaScript blocking resources on specific pages, canonicalized pages (not great), and various URL problems. I'm sending a detailed summary after this call with descriptions and fixes. You're technical, so shouldn't take long to resolve.

**Nicolas Lecomte:** Is the old `/sandbox` URL even supposed to exist?

**Carly Piekos:** Screaming Frog flagged it as a 404—one of the worst things for a site. We need to redirect `/sandbox` to `/vm` so bots don't get blocked.

**Nicolas Lecomte:** The product used to be called "VM" and now we're considering renaming it to `/sandbox` for clarity. Does renaming `/vm` to `/sandbox` hurt SEO authority?

**Carly Piekos:** Use a 301 redirect from `/vm` to `/sandbox`. That preserves authority and keeps the bot flow intact.

**Nicolas Lecomte:** The `/sandbox` link is somewhere in the CMS. I'm jumping to another call, but I want to make sure renaming won't cost us authority.

**Carly Piekos:** A 301 redirect will preserve everything. Just set it up, rename the page, update internal links, and you're good.
