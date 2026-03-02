# Alex <> Growth X - Weekly Sync

<metadata>
date: 2025-10-28
time: 17:30 UTC
duration: 33 minutes
organizer: Jo Kaminska
participants: Jo Kaminska, Megan Dickey, Donald Donckers
fathom_recording_id: 97394276
fathom_url: https://fathom.video/calls/454510139
share_url: https://fathom.video/share/VYREYpZySaoc6GM7rnm-qk1ypucnCKs1
source: fathom
enriched_on: 2026-03-02 10:15 UTC
</metadata>

---

## Summary

GrowthX and Alex aligned on strong SEO early signals: 156 organic sessions in 30 days with 78% top-ranking rate for the 23 prompts Alex appears for in AI overviews, demonstrating high-intent traffic despite low volume. The team planned a major website restructure—moving educational content to `/guides` and product announcements to `/announcements`—while implementing a Reddit and B2B review site strategy (G2, Gartner, Trustpilot) to build authority and backlinks. Donald will fix mobile formatting, implement code blocks in Webflow, and redesign blog intros as "Key Takeaways" sections to better serve AI search engines.

---

## Context

Alex is an AI recruitment platform that helps automate interview scheduling and candidate assessment. GrowthX has been working with Alex on SEO and AI visibility strategy since September, publishing educational content targeting recruitment keywords and building topical authority. This is a weekly check-in to review SEO performance metrics from Looker (combining Google Search Console and Google Analytics data), discuss content strategy adjustments, and align on website technical improvements. Alex CEO Donald is focused on building brand authority through multiple channels—content, PR, and community engagement (Reddit, review sites)—to improve visibility in both traditional search and LLM-based AI overviews.

---

## Relevance

**To GrowthX Delivery:**
- Blog content is the primary driver of high-intent LLM traffic for Alex; investing in educational content directly impacts AI visibility in addition to traditional SEO rankings.
- Content restructuring using `/guides` URLs with 301 redirects requires careful implementation to preserve existing SEO value while organizing the site architecture.
- "Key Takeaways" sections (replacing TLDR) serve both human readers and AI search engines, demonstrating how content formatting directly impacts AI discoverability.
- Webflow implementation of code blocks using pre-built components or custom development is a common client need; guidelines and scalable solutions are valuable.

**To CheckThat:**
- Alex's 78% top-rank rate in AI overviews for 23 tracked prompts demonstrates how CheckThat data (Scrunch) drives actionable SEO strategy—competitors can be identified and gap-filled.
- Blog content directly moves the needle on LLM visibility; content strategy needs to be as data-driven for AI overviews as it is for Google Search.
- Non-branded prompts (e.g., "interview automation platforms") are where Alex sees growth opportunity; branded vs. non-branded split matters for visibility strategy.

**To GrowthX Business Development:**
- Alex is building authority through content, PR, and community engagement—a multi-channel approach that positions this as a strong account with strong commitment to growth.
- Monthly cadence for performance reporting (vs. weekly) suggests maturing engagement and confidence in the partnership.
- Client is proactively planning Reddit and B2B review site strategy, showing ownership and strategic thinking on brand-building beyond content.

---

## Overview

- **Positive Early Traction:** New content is gaining traction, with 156 sessions in the last 30 days and a 78% top-rank rate for the 2% of AI prompts Alex appears for.
- **Content Strategy Pivot:** Educational articles will move to `/guides` (with 301 redirects) to preserve their SEO value, while the main blog will be repurposed for company announcements.
- **Authority Building:** A new Reddit/review site strategy will build brand authority and generate valuable backlinks, a key factor for improving AI visibility.
- **Website Fixes:** Donald will fix mobile formatting and implement a Webflow code block component, guided by GrowthX.

---

## Key Topics

### SEO Performance & AI Visibility

  - **Organic Traffic (Last 30 Days):**
      - Total Sessions: 156
      - Engaged Sessions: \>50%
      - Top Articles: "best AI recruiting tool," "bias article," "higher view alternatives"
  - **AI Visibility (Scrunch Data):**
      - Appears for 2% of tracked prompts (23 prompts).
      - Ranks in the top answer for 78% of those prompts.
      - **Insight:** High-intent traffic is low-volume but highly engaged.
  - **SERP Rankings (Google Search Console):**
      - Queries ranking \#1: 21 → 38
      - Queries ranking \#2–10: 32 → 177
      - **Insight:** Strong growth on the first SERP page.
  - **LLM Traffic (Looker Dashboard):**
      - Blog content is the primary driver of high-intent traffic from LLMs.
      - **Action:** GrowthX will add SEO opportunities from Alex's customer call summary doc to the content OS.

### Content & Website Strategy

  - **Content Structure:**
      - **Problem:** The "TLDR" section is repetitive and offers no new value.
      - **Solution:** Replace "TLDR" with a "Key Takeaways" section. Donald will provide an example intro to align on the new style.
  - **Website Architecture:**
      - **Initial Plan:** Move educational articles to `/guides` and use the main blog for product announcements.
      - **Revised Plan:** Create a new `/announcements` subfolder for company news.
          - **Rationale:** Preserves the SEO value of existing blog URLs, which are gaining traction.
          - **Action:** Implement 301 redirects from old blog URLs to new `/guides` URLs.
      - **Other Planned Changes:**
          - Add "Book a Demo" CTA to the top nav.
          - Add a "Platform" item to the nav with product overviews.
          - Move customer stories to dedicated pages.

### Technical & UX Issues

  - **Mobile Experience:**
      - **Issue:** Formatting problems (spacing, fonts) on mobile.
      - **Action:** Donald will fix; can use internal resources or external Webflow agency (Osomic).
  - **Code Blocks:**
      - **Issue:** Code blocks are not displaying correctly.
      - **Action:** GrowthX will provide Webflow implementation guidelines. Donald will attempt the fix, escalating to Osomic if needed.

---

## Action Items

**Donald Donckers (Alex)**
- Fix mobile formatting (spacing/fonts) on alex.com
- Draft and share intro/Key Takeaways example with Jo Kaminska; then GrowthX updates blog intros
- Verify GA4 form_start/form_submit tracking; confirm to Jo Kaminska
- Implement site structure: /guides + /announcements; move articles; set 301s; add nav CTAs

**Jo Kaminska (GrowthX)**
- Send Donald Donckers code block guidelines; Donald implements Webflow component or engages Osomic
- Import SEO topics from Donald's doc into Content OS; send to Donald for 'Approve to Start'
- Switch Looker performance reports to monthly cadence for Donald Donckers

---

## Transcript

**Jo Kaminska:** Hey, hey.

**Megan Dickey:** How you doing?

**Jo Kaminska:** I'm good, good. It's nice to be in the office, I think.

**Megan Dickey:** Yeah, for sure. So, yeah, I'll share my screen. First thing is that we checked your mobile experience and there are still some formatting issues we noticed around spacing and fonts.

**Jo Kaminska:** So flagging that for the dev team. And I wanted to ask about code blocks. We implemented them in the GDPR piece that got published and had issues with the implementation. Are there specific guidelines on how to set this up in Webflow?

**Donald Donckers:** I'm not sure what you mean exactly. What's the ask here?

**Jo Kaminska:** We'd like to implement this type of component on the website. Right now it's not properly displayed.

**Donald Donckers:** Okay, do you have experience with how we can set this up in Webflow?

**Jo Kaminska:** I think you need a component to embed it. It's pretty basic. Do you have Webflow developers, or what resources do you have?

**Donald Donckers:** So we work with a company called Osomic. But I have admin access and can make small changes myself. Just send me your needs and we can figure it out together.

**Jo Kaminska:** We can send guidelines and point you in the right direction. Every CMS is different, and Webflow usually has pre-built components we can leverage.

**Donald Donckers:** No, I think it should be fine. Let me look into it. I can figure this out.

**Jo Kaminska:** Great. So when it comes to content updates, we published several pieces last week. How did the reviews go?

**Donald Donckers:** Yeah, my only feedback was the TLDR section is repetitive. It's basically the same as the intro. I'd rather have the intro more clearly call out what you're getting out of it, maybe by bolding key points.

**Jo Kaminska:** What I see across blogs is a Key Takeaways section—bullets that summarize the whole content. This is how you present it to AI search engines, breaking content into digestible chunks.

**Donald Donckers:** Yeah, I like that. Key Takeaways are different from TLDR. That works better.

**Donald Donckers:** Right—like the TLDR says "save recruiter time" but the first sentence is "recruiters spend the majority of their day in administrative tasks." You're just repeating yourself.

**Jo Kaminska:** Right, so if we do Key Takeaways, it should not be repetitive. Let me draft an example of what I think it should look like, then we can iterate.

**Jo Kaminska:** What I see across blogs is a Key Takeaways section—bullets that summarize the content. This is how you present it to AI search engines, in digestible chunks.

**Donald Donckers:** Yeah, I like that. Key Takeaways are different from TLDR. That works better.

**Jo Kaminska:** Great. So let me walk you through the SEO reporting. We pulled the doc you shared with customer call notes and found many SEO opportunities. We'll import these topics into the Content OS, and once the briefs are generated, I'll send them to you to move from "Considering" to "Approve to Start."

**Jo Kaminska:** Looking at your overall AI visibility—you don't have many topics covered yet, which is expected since we're building out the repository. Scrunch data shows Alex appeared for 2% of tracked prompts (about 23 prompts). Paradox by Workday and iReview are your main competitors in this space, so we're planning "Lever alternative" posts and more to position you head-to-head.

**Donald Donckers:** What can we do outside of creating content and posting on the website?

**Jo Kaminska:** Generally, appearing in AI overviews is about strengthening your brand. PR actions, CEO visibility at events, podcasts, and your backlink profile all indirectly strengthen your credibility. LLMs value that. We're treating AI visibility the same way we treat SEO—targeting specific prompts where competitors appear but you don't, then creating the content they're citing.

**Megan Dickey:** Exactly. We look at competitor content in those prompts and decide if we want to create it first for Alex. You need to approach both SEO and LLM visibility simultaneously.

**Jo Kaminska:** SEO and AI visibility are very similar—the bigger your content repository, the better your chances of appearing in AI overviews. Brands with massive content libraries are the top players in AI visibility. To improve authority, you need backlinks—high-quality industry links, PR mentions, maybe a "State of AI in Recruitment" report that other blogs cite for data.

**Donald Donckers:** What about Reddit backlinks?

**Jo Kaminska:** Good for visibility, but they're nofollow—they don't pass link equity. Still, they build authority. Now let me show you the Looker Dashboard data. This combines Google Search Console (impressions, clicks, position, CTR) and Google Analytics (session data). The LLM tab is particularly interesting—we filter referrers to show only LLM traffic. You can see which LLMs drive sessions and how engaged those sessions are. Blog is your key driver for LLM traffic, so educational content directly impacts AI visibility.

**Jo Kaminska:** Last 30 days: 156 total sessions, 50%+ engaged. Best-performing articles are "Best AI Recruiting Tool," "Bias Article," and "Higher View Alternatives." First position SERP rankings grew from 21 to 38 queries. Second to tenth position grew from 32 to 177. Very positive signals. Conversions are growing too—form submits are up compared to the previous 30-day period.

**Donald Donckers:** We have a full doc on site structure changes: adding a "Book a Demo" CTA to nav, adding a "Platform" nav item with product overviews, moving customer stories to dedicated pages. We want to move SEO articles to `/guides` to keep the blog for product and company announcements—right now the articles dominate it.

**Jo Kaminska:** 301 redirects are critical to preserve SEO value. But consider creating an `/announcements` subfolder instead, so product news doesn't cannibalize your blog traffic. Blog is the predictable place for educational content.

**Donald Donckers:** Yeah, `/announcements` makes sense. We avoid losing traffic while separating the hubs.

**Jo Kaminska:** Looking at content cohorts, AI Recruiting and Interview Automation are performing best. "Higher View Alternatives" and Recruiting Tech topics are picking up too. Overall, first signals are excellent.

**Donald Donckers:** We're also building a Reddit strategy, plus G2, Gartner GetApp, and Trustpilot presence to build authority and get backlinks.

**Megan Dickey:** Perfect. LLMs pull a lot of context from Reddit, so that'll help.

**Jo Kaminska:** That's a double win—visibility plus backlinks. We'll switch to monthly performance reports since we're doing monthly updates now. Your key action items are mobile fixes, code block implementation, and Key Takeaways intro format. Send us an example of how you'd like the intro shaped, and we'll implement it across all pieces.
