# Deepgram <> Growth X - B-Weekly Sync

<metadata>
date: 2026-02-10
time: 17:57 UTC
duration: 29 minutes
organizer: team@growthxlabs.com
speakers: Erik O'Brien (GrowthX), Troy Blanchard (Deepgram), Hasan Jilani (Deepgram), Will Ruzvidzo (GrowthX)
participants: Praveen Rangnath (Deepgram), Sam Lee (Deepgram), Delano Fernando (Deepgram), Jose Francisco (Deepgram), Patricia Mitter (Deepgram), Nikko Lobato (Deepgram), Erik O'Brien (GrowthX), Hasan Jilani (Deepgram), Pippin Bongiovanni (Deepgram), Justin Epstein (Deepgram), Natalie Abeysena (Deepgram), Will Ruzvidzo (GrowthX), Troy Blanchard (Deepgram), Martine Katz (Deepgram), Team GrowthX
fathom_recording_id: 121269684
fathom_url: https://fathom.video/calls/561182207
share_url: https://fathom.video/share/t-iG9v-vtPAxzgJTjxFLbp-veE7yn1SG
source: fathom
enriched_on: 2026-02-27T00:00:00Z
</metadata>

---

## Summary

Deepgram and GrowthX aligned on a strategic pivot to boost TTS (text-to-speech) growth, which lags speech-to-text by 5x (~200 clicks/week vs. ~1,000). The team committed to a developer-focused content strategy targeting evaluation, latency, and integrations rather than voice quality, leveraging competitive "11 Labs Alternative" content and Hasan's TTS taxonomy to accelerate keyword research and production. They also identified a critical site migration issue causing 410 errors on high-traffic pages like LensGo and decided to implement 301 redirects to preserve SEO equity.

---

## Context

This is a bi-weekly alignment call between Deepgram's product and marketing team (Troy Blanchard, Hasan Jilani leading) and GrowthX's content marketing team (Erik O'Brien leading). Deepgram is the AI audio platform offering both STT and TTS capabilities; GrowthX is their content marketing partner producing SEO-driven developer content. The meeting focused on TTS growth because executive stakeholders were concerned about the gap in organic traffic between TTS (~200 clicks/week) and STT (~1,000 clicks/week), despite TTS being a core product offering. The team had 70 content ideas in backlog and about 15 drafts ready for review. Performance data showed January as a strong month (2,500 sessions total), with competitive comparison content ("11 Labs Alternative") and "Voice AI" topic clusters driving 40% and 34% of traffic respectively. LLM referrals were growing (151 sessions, 2% of total traffic) with higher engagement rates, indicating middle-funnel quality users doing active evaluation.

---

## Relevance

- **Content Strategy**: Shift from voice quality to developer-centric pillars (TTS evaluation in production, latency/concurrency, integrations/API usage); leverage competitive positioning against 11 Labs as proven traffic driver.
- **SEO & Traffic**: Address site migration errors (410s instead of 301 redirects) costing ~400 clicks/day on high-value pages; monitor Gemini LLM traffic growth (20% increase) as faster indexing opportunity.
- **Production & Planning**: Use Hasan's TTS mind map to accelerate keyword research and unlock faster content production; clear 15-draft backlog while scaling TTS ideas.
- **Partner Alignment**: GrowthX confirmed capacity to run TTS keyword research and check feasibility of 301 redirect implementation; fallback to Weeplash if capacity unavailable.

---

## Overview

- **New Focus: TTS Growth.** TTS organic traffic (\~200 clicks/wk) lags STT (\~1k clicks/wk), prompting a strategic pivot to developer-focused content on topics like TTS evaluation, latency, and integrations.
- **January Performance Strong.** Content-driven sessions grew to 2,500, with competitive content (e.g., "11 Labs Alternative") and the "Voice AI" cluster driving the most traffic.
- **Critical Site Error.** A recent site migration created 410 errors for high-traffic pages (e.g., LensGo, \~400 clicks/day), causing significant traffic loss. 301 redirects will be implemented to fix this.

---

## Key Topics

### TTS Growth Strategy

  - **Problem:** TTS organic traffic (\~200 clicks/wk) is significantly lower than STT (\~1,000 clicks/wk), raising executive concern.
  - **Solution:** Shift content strategy from voice quality to developer-centric topics.
      - **New Content Pillars:**
          - TTS evaluation in production
          - TTS latency & concurrency
          - Integrations & API usage
  - **Competitive Angle:** Target the "builder" (developer) market, where technical specs (latency, concurrency) are critical, rather than competing directly with 11 Labs for the "creator" market.
  - **Tactics:**
      - Continue creating "11 Labs Alternative" content, a proven traffic driver.
      - Use Hasan's mind map to accelerate keyword research and content production.

### January Performance Review

  - **Overall Growth:** Sessions increased to 2,500, beating the prior month.
  - **Top Content Drivers:**
      - Competitive content (e.g., "11 Labs Alternative"): \~40% of traffic.
      - "Voice AI" topic cluster: \~34% of traffic.
  - **LLM Referrals:**
      - Grew to 151 sessions, with ChatGPT at 64%.
      - "11 Labs Alternative" article drove 44 sessions with 80% engagement.
      - **Insight:** LLM traffic is middle-funnel (active evaluation) and has higher engagement but low volume (\~2% of total traffic).
      - **Opportunity:** Monitor Gemini, which grew 20% last month and indexes content faster than ChatGPT.

### Site Migration Error

  - **Issue:** A recent migration from `AI apps` to `Voice AI apps` created 410 errors for old URLs instead of using 301 redirects.
  - **Impact:** Significant traffic loss from high-value pages, including LensGo (\~400 clicks/day).
  - **Rationale:** The Sanity team argued 301s to a less relevant page would be a "soft 404" to Google.
  - **Decision:** The team agreed to implement 301 redirects, as a relevant redirect is superior to a dead page for both UX and SEO.

---

## Action Items

**Hasan Jilani (Deepgram)**
- Send TTS mind map to Erik O'Brien to guide keyword research and content production

**Erik O'Brien (GrowthX)**
- Run TTS keyword research using the mind map; draft dev-focused TTS content plan with focus on evaluation, latency, and integrations
- Confirm GrowthX capacity for implementing 301 redirects on AI apps → Voice AI apps migration; if not available, escalate to Weeplash

**Troy Blanchard (Deepgram)**
- Share TTS performance report with Erik to inform content strategy
- Review and publish backlog of ~15 drafted articles and 70 content ideas to maintain publishing cadence

---

## Transcript

**Erik O'Brien:** This meeting is being recorded.

**Will Ruzvidzo:** Hey, Erik. How's it going?

**Erik O'Brien:** Good, good.

**Troy Blanchard:** Hey, how's it going, man? I've been in meetings since 8:30. Long day so far. I know Hasan is back though—he really got hit hard by the flu. And I know we have a significant backlog to review. We have about a dozen articles ready to look at, plus we've got quite a few in the ideas section.

**Erik O'Brien:** Yeah, we probably have around 70 content ideas in backlog. And that doesn't include the TTS expansion we talked about last week.

**Troy Blanchard:** Right. We have some TTS ideas in the backlog, but that's really where I think the energy needs to be focused. When I look at our TTS growth versus STT, STT is having a nice pickup now, but TTS is not growing as much. From our executives' perspective, the concern is why aren't we growing TTS as well? What are we failing to talk about? I think it's about how we organize around it. STT is the core business, so it's not surprising STT leads. But we have a struggle here to figure out what the right angle is on TTS. The data shows we're only getting about 200 page clicks per week from organic search for TTS, which is just not enough. That's about a fifth of what we're seeing from speech-to-text at 1,000 clicks per week. So I'd love to get this moving in the right direction.

I think the developer angle is key—not so much voice quality, but integrations, making apps work, concurrency, latency. That's where we win versus 11 Labs.

**Hasan Jilani:** Yeah, there's one topic that's relatively unexplored but companies are struggling with: TTS evaluation—making sure TTS is actually working in production. That's one subtopic. TTS latency is another. And just getting away from voice quality by itself.

**Troy Blanchard:** Right. Let's get this going on the TTS side. I can share the TTS performance report with you, Erik.

**Erik O'Brien:** That would be super helpful. I'll definitely do some keyword research on our end to see what opportunities exist specific to TTS. But if you guys have ideas or a mind map, that would definitely expedite things and get us into production quicker.

**Hasan Jilani:** I could provide a mind map of TTS topics. That would help guide your keyword research.

**Troy Blanchard:** There's definitely stuff here that could be expanded into more use case blog posts. I think we have a good direction from this data. We're seeing the "11 Labs Alternative" content do really well—that's been a proven traffic driver.

**Hasan Jilani:** I think we should continue comparing ourselves to 11 Labs because that's been a growth source for us in content.

**Troy Blanchard:** Yeah, that evaluation and quality angle is exactly it. We continue to see growing traffic from your publishing, and we're seeing an uptick in activations overall. Traffic trends for the company are going in the right direction. I think if we nail this TTS thing, we can really put some solid content out there. Also thinking about how we expand the product page—hopefully we get the pricing page done and then move to those.

**Erik O'Brien:** Awesome. I prepared a quick view of January performance. We've been looking at it almost weekly, so no big surprises, but overall good session growth. We reached 2,500 sessions in January, beating December month-over-month. Traffic is going in the right direction and very in line with our publishing cadence.

Competitive comparison content drove the most sessions, about 40% of traffic, with really good engagement rates. The "Voice AI" topic cluster we pushed in December is also driving about 34% of traffic. Overall, when we have a focal point and produce content on it, we see traffic uptick. So with this new TTS focus, we'll get the right keywords and intent alignment to drive meaningful traffic.

For LLM referrals, we saw good month-over-month growth with 151 sessions in January. ChatGPT is leading at 64%. The "11 Labs Alternative" article drove 44 sessions with 80% engagement. LLM traffic is middle-funnel—people actively evaluating—and has higher engagement but only about 2% of total traffic. However, we should monitor Gemini, which grew 20% last month and indexes articles faster than ChatGPT.

**Troy Blanchard:** It's a nice diversity. ChatGPT is keeping going down though, which is interesting. We're getting a new pricing page and revised the FAQ based on what people are asking. When people do comparisons—Deepgram versus 11 Labs, for speech-to-text—the revised FAQ can link to relevant articles and help drive more traffic. We're trying to build a network across the site to drive LLM engagement. People have realized it's not a sales lead machine like LinkedIn or Google, but it's good middle-funnel signal.

**Erik O'Brien:** Exactly. Middle-funnel people doing active evaluation. There's data showing higher conversion rates from LLM traffic. With overall traffic at 2% compared to organic and referral, if we convert at 0.3%, it's still a pretty small number compared to other traffic sources. But as active decision-makers use LLMs for research, we should keep tracking to make sure they're finding the right pages and alternatives. We want our presence proportional to LLM usage growth and benchmarks.

**Troy Blanchard:** We don't need to dominate chat GPT or stop everything. 2% isn't a driver. Even if we doubled it to 4%, it's not a game changer. But it's a good signal.

One other thing I wanted to bring up: we recently migrated AI apps to Voice AI apps.

**Erik O'Brien:** Yeah, I noticed you guys migrated from AI apps to Voice AI apps. We would have probably recommended implementing 301 redirects from those old pages. LensGo was generating about 400 clicks per day, and now it's showing a hard 410 error.

**Hasan Jilani:** That was something I recommended to the Sanity team. I suggested 301 redirects for pages we're sunsetting to a relevant page. But they said Google would treat a non-relevant redirect as a soft 404. I'm not sure if there's a difference of opinion.

**Erik O'Brien:** There might be. If there's a high bounce rate after the redirect, Google might treat it as a soft 404. But the point is you have equity in the traffic you've already developed, and people are still clicking these links. Introducing them to the Voice AI apps page would at least be better than a 410.

**Hasan Jilani:** Yeah, that was my original logic. I wanted to preserve the link equity and backlinks, but the Sanity team thought a 410 would be cleaner for some reason. But the UX is worse with a 410 than just redirecting to the AI apps page.

**Erik O'Brien:** Right. From a user experience perspective, a relevant redirect is better than a dead page.

**Hasan Jilani:** I personally agree. We have the old URLs still. We could introduce a 301 redirect. But Troy, I'll defer to you.

**Troy Blanchard:** I was just following what the Sanity team told me. Let me think about both sides here. Ultimately, we want the old AI apps to fade away, but we need to preserve traffic equity where we have Voice apps. We should do it. We should just do it. Yeah, I think it's fine.

**Hasan Jilani:** The Sanity team has ended their migration, so they're not touching it anymore. Erik, is this something your team could programmatically handle, or should we go back to Weeplash?

**Erik O'Brien:** Let me double-check if we have capacity to do this. If not, we can escalate to Weeplash. Our original recommendation would have been the 301 redirect to preserve equity. This was just something we wanted to call out for discussion.

**Troy Blanchard:** I appreciate it. Thanks for the diligence. Let's keep the focus on TTS. Thank you, everyone.

**Erik O'Brien:** Thanks to you.

**Hasan Jilani:** Bye.
