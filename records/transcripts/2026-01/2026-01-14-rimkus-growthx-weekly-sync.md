# Rimkus <> GrowthX - Weekly Sync

<metadata>
date: 2026-01-14
time: 15:30 UTC
duration: 33 minutes
organizer: team@growthxlabs.com
participants: Matthew Alves-Hill (GrowthX), Jennifer Bulmash (Rimkus), Alishia Natiello (Rimkus), Vitali Edrenkine (Rimkus), Nohora Davila (Rimkus)
fathom_recording_id: 114197508
fathom_url: https://fathom.video/calls/530450877
share_url: https://fathom.video/share/tdMGdgaJ92cZ_egE3z_5aQyCQrvRn-ds
source: fathom
enriched_on: 2026-02-28 14:47 UTC
</metadata>

---

## Summary

GrowthX and Rimkus finalized the new high-level, informative editorial tone and confirmed strong post-holiday traffic recovery with articles ranking in Google AI Overviews. The team reviewed content review status (3 BES articles for Nohora, 2 Forensics articles for Jen), discussed improvements to weekly reporting and Looker dashboard tagging, investigated keyword tracking discrepancies between Profound and Scrunch, and proposed a new scalable "Building Codes by State" series to build topical authority and capture high-intent search volume.

---

## Context

This is an internal weekly check-in between GrowthX's content and analytics team and Rimkus's marketing leadership. Rimkus is a specialized building services and forensics consulting firm; GrowthX handles content marketing across their Building Envelope Services (BES) and Forensics verticals. The team meets weekly to review editorial direction, content performance metrics, and content strategy initiatives. In this call, they finalized a shift to a higher-level, more natural-language editorial tone and discussed data infrastructure improvements to better surface performance wins for Rimkus's internal stakeholder presentations.

---

## Relevance

This meeting directly impacts Rimkus's content marketing strategy and reporting cadence. The approval of the new editorial tone removes a major bottleneck and enables faster content production. The proposed "Building Codes by State" series represents a significant SEO and authority-building opportunity with low competition and high search volume. The infrastructure improvements (Looker tagging, weekly reporting automation) address real reporting friction for Rimkus's internal teams and will improve visibility into content performance across BES and Forensics. The keyword tracking alignment work ensures Rimkus and GrowthX are measuring the same KPIs.

---

## Overview

- **Editorial Direction Finalized:** The new high-level, informative tone is approved. Rimkus will review the final 7 articles written in this style to enable full adoption.
- **Strong Performance Confirmed:** Traffic is recovering post-holiday, and articles are ranking in Google's AI Overviews for high-intent keywords (`building condition assessment`), validating the SEO strategy.
- **New BES Content Strategy:** A programmatic series on "Building Codes by State" is proposed to build authority and capture high-intent traffic.
- **Reporting Improvements:** GrowthX will add BES/Forensics tags to the Looker dashboard and provide custom performance reports to support Rimkus's internal presentations.

---

## Key Topics

### Editorial Direction Finalized

  - **New Tone:** Approved as high-level, informative, and natural language, focusing on informational intent over deep technical detail.
  - **Implementation:** GrowthX's content pipelines are updated. The 7 articles currently in review are the final pieces written in the old style.
  - **Review Status:**
      - **BES:** 3 articles for Nohora.
      - **Forensics:** 2 articles for Jen.
  - **Process Improvement:** To avoid repetitive intros, new articles will vary their opening formats.

### Content Performance & Reporting

  - **Performance:** Traffic is recovering post-holiday, with weekly traffic already matching the previous week's volume.
  - **SEO Wins:** Articles are ranking in Google's AI Overviews for key terms, including:
      - `building condition assessment` (top source)
      - `electrical risk assessment` (top source)
  - **Reporting Needs:**
      - **Looker Dashboard:** Add BES/Forensics tags to the "Published" view for easier reporting.
      - **Custom Reports:** GrowthX will provide data for Rimkus's weekly internal presentations (e.g., high-level wins, new article links).
  - **Keyword Tracking Discrepancy:**
      - **Issue:** BES keyword performance in Rimkus's Profound tool appears inconsistent compared to Forensics.
      - **Cause:** Different keyword sets tracked by Profound vs. GrowthX's Scrunch tool.
      - **Resolution:** Nohora will share her keyword list to align tracking and enable a direct comparison.

### New Content Strategy: Building Codes by State

  - **Opportunity:** Keyword research shows high search volume and low competition for state-specific building codes.
  - **Goal:** Build topical authority and capture high-intent traffic by providing an accessible alternative to dense government resources.
  - **Proposed Format:** A programmatic series (one article per state) with a consistent, templated structure:
      - Code changes for the current year
      - High-level code structure and requirements
      - Governing agency and current edition
      - Specific local elements
      - Typical penalties and enforcement

---

## Action Items

**Nohora Davila (Rimkus)**
- Review 3 BES articles in Ready for Review; notify Matthew for publish
- Email Matthew: Scrunch/Profound screenshots + BES prompts/personas; then Matthew onboard to Scrunch
- Obtain WordPress API key from Alishia Natiello; share w/ Matthew for publishing automation

**Jennifer Bulmash (Rimkus)**
- Review 2 Forensics articles in Ready for Review; notify Matthew for publish
- Email Matthew: presentation wishlist + Forensics prompts/personas; then Matthew onboard to Scrunch

**Matthew Alves-Hill (GrowthX)**
- Add BES/Forensics tags to Published Blogs view in Looker
- Confirm GA4 engaged session threshold; update Jennifer and Nohora
- Fix BES vs Forensics cohorting logic in Looker; update Jennifer and Nohora
- Email Jennifer and Nohora: weekly roundup (new article links, traffic wins, Looker highlights, Google AI Overview placements)
- Email Nohora: Building Codes by State concept + draft template; scope keyword research for all 50 states

---

## Transcript

[Opening remarks omitted - technical check-in about background noise and personal updates.]

**Matthew Alves-Hill (GrowthX):** I feel like we're in a really good place on editorial. Jen, I appreciate you going back and forth on this, but I was much happier with the output after our last discussion. The key takeaway is the tone is now much more high-level and informative, more natural language—thinking about high-level informational intent instead of diving into rabbit holes.

**Jennifer Bulmash (Rimkus):** Agreed.

**Matthew Alves-Hill (GrowthX):** And Nora, I know the conversation was focused on Forensics, but I think the same approach works well for BES.

**Nohora Davila (Rimkus):** Absolutely, 100%.

**Matthew Alves-Hill (GrowthX):** We've created new content artifacts based on the updated editorial direction. The pipelines are updated and all the feedback from our last discussion has been incorporated. We had some content audited over Christmas that you re-approved, and those are published, but they're the last pieces in the old tone. I want to tie this off neatly. There are seven articles that we've reworked—five from last week and two from content audit. If you can spend five minutes reviewing and confirming they look good, we'll get them published straight away. From this week forward, everything will follow the new approach.

**Nohora Davila (Rimkus):** We have four articles to review. I have three for BES and Jen has two for Forensics. We'll get to those. Just so you know, my schedule is packed early in the week, so I'll probably start tackling them tomorrow afternoon and Friday.

**Matthew Alves-Hill (GrowthX):** Got it.

**Matthew Alves-Hill (GrowthX):** [Checking article status in shared doc] Some have moved to publish already. Jen, it looks like you reviewed a couple last night?

**Jennifer Bulmash (Rimkus):** Yes, I reviewed some the other night.

**Matthew Alves-Hill (GrowthX):** That explains the movement. So we have three BES topics for Nora, and two are quite fresh so those should be quick. But no rush—we're in a good publishing cadence right now, so there's no pressure. Whenever you can get to them is fine. Lawrence is handling the rest on our side.

**Jennifer Bulmash (Rimkus):** Two quick comments. First, I flagged the repetitive introductions to Lawrence and he's addressed it. A lot of the blog post intros were following the same format—something like "You get a call at 8 a.m." and the pattern becomes obvious when you see them all on the Rimkus blog preview. Nora was seeing this too. It's nothing wrong with the content itself, but at scale it's noticeable, so I'd love some variation in the opening formats.

**Matthew Alves-Hill (GrowthX):** Got it—it's a scale problem. Yeah, we can definitely add variation to the intros.

**Jennifer Bulmash (Rimkus):** Second thing: on the Ready for Review view, you have BES/Forensics tags. Would it be possible to add those same tags to the Published Blogs view going forward? It would help me at a glance when Nora and I are assembling materials for presentations.

**Nohora Davila (Rimkus):** That would be really helpful for quick reference.

**Matthew Alves-Hill (GrowthX):** Absolutely, I'll make sure those tags are added to the Published view.

**Matthew Alves-Hill (GrowthX):** I really appreciate you both going through this process with us. It's been methodical, but I think we're definitely in a good place now. Let me just pull up the performance data. [Chrome restarts briefly] Okay, so on the good news front: you mentioned last week about the new tone potentially impacting performance. I don't think it will be significant—actually, it might improve things. Natural language is always a good play. The data shows growth is solid. We had a dip over Christmas, which was expected, but we're already bouncing back nicely. We're only two days into the week and we're already on par with last week's traffic. So we haven't lost any performance. I would expect to see continued improvement. I'm going to use email as the primary comms channel for now, unless you want to switch back to Slack. I'll share the detailed data there, but I wanted to show you the highlights.

**Matthew Alves-Hill (GrowthX):** Looking at the SEO wins, let me pull up building condition assessment. Google is drawing Rimkus as the top source in its AI Overview. This is an article we published in October, and Google is pulling directly from our content. Second example: electrical risk assessment—Google is pulling us again and we're top of the SERP. When I see articles like California balcony inspection with a thousand percent week-on-week growth in engaged sessions, that tells me Google's ranking us. The content is great, people are finding it, and they're staying on site.

**Jennifer Bulmash (Rimkus):** This is really encouraging.

**Matthew Alves-Hill (GrowthX):** You have access to the Scrunch report. I'll share the highlights in the email so you don't have to dig through all the details. Generally, when you see engaged session growth like that, it's a strong signal. We're doing all the SEO elements correctly. This has been super encouraging, and it's been helpful having this solid foundation while we've been recalibrating the editorial approach.

**Jennifer Bulmash (Rimkus):** Can I ask a couple of quick Looker questions? First, just to clarify for when we're sharing this data: sessions is basically people visiting the site, and engaged sessions means they stayed for a certain amount of time to actually read the content?

**Matthew Alves-Hill (GrowthX):** That's correct. Engaged is typically 10 seconds on site in GA4—I'll double-check that. The Looker report pulls from your GA4 data. The rankings shown are where we're ranking for specific keywords we're targeting. The bottom tier is position one on Google, and we're seeing a nice uptick there. When competing for position one it's the most competitive spot, but we want to see upward movement across the board. Vitaly requested we split traffic between BES and Forensics. I'm noticing an issue with how those cohorts are attributed, so I need to verify the logic.

**Jennifer Bulmash (Rimkus):** My second question is related: can we sort those landing pages by BES versus Forensics as well? Nora and I give separate presentations, and if we could filter and screenshot that view weekly, it would save us each an extra step. Anything that splits BES and Forensics would be helpful.

**Nohora Davila (Rimkus):** I also have a question about keyword tracking. We use Profound to track where we rank in certain areas, and we've set up goals between Forensics and BES. [Shares screen] The issue is BES looks very inconsistent compared to Forensics, which looks much cleaner. Are we doing something wrong with BES? Why isn't it consistent like Forensics?

**Matthew Alves-Hill (GrowthX):** Can you send me those screenshots? We don't use Profound—we use Scrunch. Each tool tracks different keywords depending on which prompts you're set up to track. All these tools have some degree of inconsistency. We're actually about to launch our own tool that's similar to Profound but with more control. If you share the prompts you're tracking, I can duplicate them in our tool. The fundamental issue is different prompt sets. If you share your keyword list and new prompts, we can align them in Scrunch and give you better visibility.

**Nohora Davila (Rimkus):** I have a full spreadsheet of new prompts we're going to implement, plus personas. I'll share that with you and we can compare apples to apples.

**Matthew Alves-Hill (GrowthX):** Please do. And Jen, the same for Forensics if you're documenting your prompts. We'll get you both into Scrunch, and when we roll out our own tool, you can be early users with full visibility.

**Jennifer Bulmash (Rimkus):** I'll put this in writing, but let me clarify our needs. Nora and I have a new internal marketing meeting where we present what we've accomplished together and what results we're seeing. For those meetings, we need high-level data on what GrowthX and Rimkus have done together. For other meetings, we need a list of new article links plus high-level wins. Our stakeholders don't need to know the process—just the outcomes. For example, "We're now second for building condition assessments" is the kind of win we want to share.

**Matthew Alves-Hill (GrowthX):** Got it. Send me a wish list of specific views and how you want to frame things. We can even automate it to send you the same views every week for your presentations.

**Nohora Davila (Rimkus):** I'll scope the keyword research further on the Building Codes by State series. That's the last thing—do either of you have a WordPress API key we can use to automate our publishing?

**Matthew Alves-Hill (GrowthX):** Great question. I've just messaged Alishia to get that. I'll follow up with Jen on the presentation wishlist, and we'll have everything you need. I need to jump off now though—my kid needs me. But let's touch base soon on all of this.

**Jennifer Bulmash (Rimkus):** Thanks, Matt. Nice to see you.

**Nohora Davila (Rimkus):** Bye, Matt.
