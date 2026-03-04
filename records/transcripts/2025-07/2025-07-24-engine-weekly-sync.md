# Engine Weekly Sync

<metadata>
date: 2025-07-24
time: 18:29 UTC
duration: 36 minutes
organizer: Jo Kaminska
participants: Jo Kaminska, Darrell Etherington, Carrie Chowske, James Winter, Joel Murphy, Kali Wootton
fathom_recording_id: 76334351
fathom_url: https://fathom.video/calls/360237586
share_url: https://fathom.video/share/ZrEkzLZmS3HixRqR5aC2xCg9aSGBi5Tm
source: fathom
enriched_on: 2025-07-24 19:45 UTC
</metadata>

---

## Summary

GrowthX and Hotel Engine aligned on strategy for 30,000+ programmatic SEO pages targeting "hotels good for [event] in [city]" patterns, with GrowthX agreeing to monitor indexation and diagnose performance issues while Hotel Engine improves page relevance. Key discussions covered content audits to free crawl budget, industry prioritization lists for targeted content development, analytics showing 50% impression gains with steady clicks, and a potential Cloudflare setting blocking LLM traffic that GrowthX will investigate—with next steps including establishing conversion event tracking and exploring collaborative LLM visibility measurement through tools like Peek.ai and Scrunch.

---

## Context

Hotel Engine is a B2B travel platform where GrowthX is executing a content strategy engagement. The relationship appears strategic—GrowthX handles all content creation and SEO optimization while Hotel Engine provides product guidance and approval workflows. This meeting is part of an ongoing weekly sync establishing after an initial kick-off call with Marcel; James Winter leads product/strategy decisions for Hotel Engine while Joel Murphy and Kali Wootton handle operational implementation. The programmatic SEO initiative represents a major strategic pivot for Hotel Engine, launching 30,000+ templated pages months into the engagement—a volume that surfaced concerns about best practices and potential risks, prompting closer collaboration on implementation strategy.

---

## Relevance

### To GrowthX Delivery
- Programmatic SEO at scale (30,000 pages) requires new monitoring and diagnostic processes—moving beyond traditional individual-page optimization to mass content strategy validation
- Content audit best practice highlighted: removing outdated content frees crawl budget, enabling better performance for new programmatic pages—directly applicable to other client engagements
- Multiple tool integrations needed: Peek.ai for LLM prompt tracking, Scrunch for unified LLM visibility, Amplitude for conversion influence analysis—establishing replicable analytics infrastructure

### To CheckThat
- Direct LLM visibility tracking opportunity: Hotel Engine is prioritizing collaboration on tracking specific AI prompts that drive traffic, offering real-world use case for monitoring LLM-generated traffic patterns
- Cloudflare blocking LLM traffic by default—potential common infrastructure issue affecting multiple B2B clients; GrowthX should document and share guidance

### To GrowthX Business Development
- Account health: Strong engagement signals—weekly syncs, collaborative problem-solving, client providing detailed industry data (revenue-sorted sub-industry lists), and expanding scope into analytics and LLM visibility
- Expansion opportunity: Charge card content on roadmap (1-2 weeks out); wedding vertical showing 100%+ click growth week-over-week suggests adjacent segment expansion potential
- Reference potential: Strong quality feedback ("kudos to you guys"), 50% impression growth within weeks suggests strong case study material for travel/hospitality B2B segment

---

## Overview

- Programmatic SEO pages (30k+) need indexation and performance analysis
- Content quality is good; industry prioritization list shared for future focus
- Analytics show 50% increase in impressions; clicks steady
- Potential Cloudflare issue blocking LLM traffic needs investigation

---

## Key Topics

### Programmatic SEO Pages

  - [30,000+ pages created for "hotels good for \[event\] in \[city\]"](https://fathom.video/share/ZrEkzLZmS3HixRqR5aC2xCg9aSGBi5Tm?tab=summary&timestamp=240.0)
  - Not currently indexed; team to analyze and advise on best practices
  - Concern about potential negative SEO impact
  - GrowthX to monitor, diagnose, and propose solutions
  - Hotel Engine to improve relevance of page content

### Content Audit and Deletion

  - Previous agency provided list of blog posts to delete
  - GrowthX to review list and conduct own audit
  - Goal: free up crawl budget for new programmatic pages
  - Potential traffic lift by removing outdated content

### Industry Prioritization for Content

  - James shared detailed industry/sub-industry list sorted by revenue
  - GrowthX to focus on broader industries (e.g., construction) while mentioning sub-categories
  - Need to consider variation within sub-industries for content relevance

### Content Approval Process

  - James prefers email and Slack notifications for approvals
  - Refreshed content doesn't need approval; GrowthX can lead on updates

### Charge Card and Octave API Updates

  - Charge card materials on hold; update expected in 1-2 weeks
  - Octave API: James to add GrowthX team to tool access
  - Potential collaboration between Octave team and GrowthX

### Analytics Overview

  - 50% increase in impressions, clicks holding steady
  - New pages (e.g., prepaid travel cards, weddings) showing growth
  - Updated/refreshed content seeing positive trends
  - Decrease in branded queries, indicating improved visibility

### LLM Visibility and Cloudflare Issue

  - GrowthX working on collaborative process for tracking LLM prompts
  - Potential Cloudflare default setting blocking LLM traffic
  - GrowthX to investigate and provide guidance

---

## Action Items

**Joel Murphy (Hotel Engine)**
- Share list of blog posts to delete w/ GrowthX team for review

- Provide GrowthX access to customer call database for AI querying

- Check w/ James re sharing Peek.ai prompt data w/ GrowthX team

- Set up & evaluate Amplitude influence chart for content performance, share if useful

**Jo Kaminska (GrowthX)**
- Implement Peek.ai prompts in Scrunch for comparison once received from Joel

- Research Cloudflare LLM traffic blocking, provide info to Joel early next week

---

## Transcript

*[Pre-meeting small talk — participants joining, discussing flights, venue quality, and family events — condensed for brevity]*

**Jo Kaminska:** So on the agenda, we wanted to talk about content quality, amount, priorities, and the production analysis. We'll also do a quick analytics overview from Carrie, and I wanted to ask about charge card materials and the Octave API. James is running late, so we can start with the product side.

**Kali Wootton:** Yeah, from our side, I don't have any info on the charge card yet—that's still in leadership approvals. But Joel and I wanted to flag something important: the programmatic SEO pages we added a couple months ago. There are tens of thousands of those pages, and launching this volume all at once without a delivery strategy has created some uncertainty. We'd love your advice on measuring what's been indexed, analyzing performance, and determining the best way forward. James suggested SCM tactics to help indexation, but we want a clearer picture first on what's indexed and what isn't.

**Jo Kaminska:** We can include it in our reporting. Could you give us more context on what was produced and what's been published?

**Kali Wootton:** Yeah, let me pull it up real quick.

**Joel Murphy:** Yeah, the pages are targeted at "hotels good for [event] in [city]"—like hotels best for family reunions in Fort Lauderdale. There are 30,000 of these created.

**James Winter:** Overall, I'm pretty happy with content quality. I found one article I thought was bad, but it turned out to be from a previous vendor, not from GrowthX. So kudos to you guys. Did you get the industry data I sent over?

**Jo Kaminska:** Yeah, we did. My question is whether we should prioritize the industries top to bottom for content updates.

**James Winter:** Let me pull it up. I sorted this by sub-industry, stack-ranked by revenue. So management consulting within business services is highest. Each section has primary and sub-industry options ranked best to worst.

**Jo Kaminska:** That makes sense. Given low keyword volumes, we won't tackle architecture, engineering, and design specifically. We'll focus on construction, energy, utilities, and mention sub-categories where it helps.

**James Winter:** Just be careful—some industries like construction are fairly uniform, but within business services, facilities management and advertising are wildly different, even though they're grouped together. You'll need to think about what makes sense for search terms and content consumption.

**Jo Kaminska:** Thanks for the list. It's very useful. Carrie, one quick thing on approvals—how would you prefer we notify you about content needing approval?

**Carrie Chowske:** Email and Slack is probably best. And like I mentioned, we don't need to approve refreshed content; you guys can take the lead on those updates.

**James Winter:** Sounds good. And on charge cards—we had a meeting this week. I'll have materials to share in 1-2 weeks.

**Jo Kaminska:** No problem. One more topic: Octave API. Who should I add to the tool?

**James Winter:** Email me a list and I can add your team. Marcel and the Octave CEO were supposed to meet, and I'll also ask the Octave team to chat with you directly about how to use it.

**Jo Kaminska:** Great. Before you run off, let me flag one more thing. We're working on making LLM visibility more collaborative. We want to agree on which prompts to track based on your priorities.

**Joel Murphy:** Yeah, James has set something up in Peek.ai—he's tracking specific prompts and measuring performance against them. I'm not using it directly, but I can help you get that data from him. We also have a database of sales calls that can be queried with AI to find common customer questions.

**Jo Kaminska:** Got it. Peek.ai sounds a lot like Scrunch, the tool we presented last week. We could pull the Peek.ai prompt data and re-implement it in Scrunch to compare. We could also incorporate your customer call database to identify more focused verticals and pain points.

**Joel Murphy:** I'll check with James on sharing that data. One technical question: I read that Cloudflare blocks LLM traffic by default. We're behind Cloudflare and want to make sure we're not blocking LLMs unknowingly. Is it just a checkbox or more complicated?

**Jo Kaminska:** I haven't heard about that, so I'd need to research it. But I'll get back to you early next week with information. It does sound like it's probably something toggleable if it's a default setting.

*[Carrie shares analytics overview]*

**Carrie Chowske:** Most new content is indexing fine. The PSEO pages aren't indexed yet—we can help with that. Comparing early June to early July, we're seeing about 50% increase in impressions with steady clicks. Over the last 28 days, same trend: impressions up significantly, clicks steady. The best-performing new pages are prepaid travel cards, which had 1,000% growth from the previous week—good signal for credit card content expansion. Weddings also showed strong growth. Branded queries are down, which is good for overall visibility. Construction and utilities refresh pieces are seeing good traffic too. Overall, the trend is moving in the right direction.

**Joel Murphy:** Nice. One analytics question: we're using Amplitude now instead of GA4. One feature they have is an influence chart that shows what events influenced a conversion. Could we set something like that up for your content work?

**Carrie Chowske:** I think that would be great. Amplitude's attribution models have gotten much better—they're not just using first-touch or last-touch anymore. It should give us better insights into content influence on conversions.

**Joel Murphy:** I'll explore it and bring results to the next sync. We're also working on setting up conversion events for form submissions, which will give us more granular tracking.

**Jo Kaminska:** In the meantime, we can set up funnel reporting in Google Analytics looking at blog post traffic to sign-up pages. That would show banner effectiveness. Once you have conversion events set up, we'll get even better data.

**Joel Murphy:** Amplitude will be our primary tool; we're moving away from GA4 as fast as we can.

**Jo Kaminska:** Got it. Anything else?

**Joel Murphy:** No, I'm good.

**Jo Kaminska:** Thanks, Joel, and thanks, Carrie. Talk to you soon.

**Joel Murphy:** See you guys. Bye.
