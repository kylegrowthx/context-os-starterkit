# Webstacks<>GrowthX Weekly Sync

<metadata>
date: 2025-02-06
time: 17:32 UTC
duration: 24 minutes
organizer: aida@growthxlabs.com
participants: Aida Knežević (GrowthX), Sadira Sittampalam (GrowthX), Kyle Gaudreau (GrowthX), Devon Wood (Webstacks), Jesse Schor (Webstacks)
fathom_recording_id: 45992986
fathom_url: https://fathom.video/calls/227063904
share_url: https://fathom.video/share/gB2GT12tHmzzinWtzzZvsVNNfbFMFeuu
source: fathom
enriched_on: 2026-03-05 14:32 UTC
</metadata>

---

## Summary

Webstacks and GrowthX reviewed strong organic search performance (nearly 500 weekly clicks driven by design-related content) and aligned on content strategy with 10-12 prioritized articles from a 30-topic cluster, while Webstacks navigated a CMS migration from Contentful to Sanity. The teams discussed AI content quality challenges, explored backlink exchange opportunities to boost Domain Rating in 2025, and agreed on supporting materials including brand guidelines and internal linking lists to improve AI-generated content adherence.

---

## Context

Webstacks is a web design agency and GrowthX services client using content marketing to drive organic search traffic. This is an ongoing weekly operational sync between Aida Knežević (GrowthX content lead managing the engagement) and Devon Wood (Webstacks technical/content leader). The relationship is focused on content generation, SEO performance monitoring, and website optimization. Webstacks is mid-redesign, transitioning from Contentful to Sanity CMS, which creates operational dependencies around publishing workflows that GrowthX needs to track.

---

## Relevance

**To GrowthX Delivery:**
- AI content generation quality remains a limiting factor — ChatGPT Premium outperforms Claude and Gemini for consistent adherence to brand guidelines and prompt instruction-following, suggesting potential workflow improvements
- Chunking/batching strategy matters significantly for prompt engineering; uploading multiple screenshots at once degrades output (breaks the AI)
- Internal linking automation through AirOps produces low-quality results that require manual cleanup; Devon requesting prioritized link lists suggests opportunity to document internal linking best practices

**To GrowthX Business Development:**
- Account showing positive momentum: 500+ weekly clicks, design-focused pages consistently outperforming, expecting major gains in 2 months as organic rankings mature
- Webstacks investing in CMS modernization (Sanity) signals confidence in long-term content strategy; GrowthX positioned to support transition
- Expansion opportunity: backlink exchange and automated outreach for link building could become 2025 differentiator for account; Devon explicitly seeking structured approach (Airtable tracking)

**To CheckThat:**
- Client actively using multiple AI models (ChatGPT, Claude, Gemini) and experiencing inconsistency across tools; suggests demand for AI visibility auditing and prompt optimization
- Domain Rating growth target (2025) indicates competitive SEO focus where CheckThat visibility data could inform content strategy

---

## Overview

- Performance report updated with GA4 data, showing a significant increase in weekly clicks (~500) driven by design-related pages
- 10 new articles being generated and staged this week; cluster research to be prioritized for future content
- Webstacks is transitioning from Contentful to Sanity CMS as part of their website redesign
- Both teams are open to exploring backlink exchanges and potential automated outreach for link building

---

## Key Topics

### Performance Report Updates

- GA4 data integrated into performance report, focusing on organic search metrics
- GrowthX content filtered using ChatGPT to separate from Webstacks content
- Significant increase in weekly clicks (nearly 500) observed
- Top-performing pages include bank website design and other design-related content
- Design-focused pages consistently perform well week-over-week

### Content Generation and AI Tools

- 10 new articles being generated and staged this week
- Challenges with AI-generated content:
  - Inconsistent adherence to brand guidelines
  - Forgetfulness in following specific instructions (e.g., describing design elements)
  - Need for careful prompt engineering and chunking of tasks
- Teams exploring various AI models:
  - Primary use of ChatGPT and Claude
  - Experimenting with Gemini in Google Docs for quick edits
  - Webstacks setting up Gemini account for custom use

### Content Cluster Research and Prioritization

- 30 potential topics identified in cluster research
- Plan to prioritize 10-12 topics for immediate focus
- Selection criteria:
  - Mix of high search volume topics
  - Bottom-of-funnel content for various marketing channels
- Devon to provide additional notes and resources to guide content creation

### Website Redesign and CMS Migration

- Webstacks transitioning from Contentful to Sanity CMS
- Redesign progress:
  - Homepage and solutions pages migrated
  - Client stories migration scheduled for tomorrow
  - Blog migration planned for next week
- Sanity CMS expected to be more organized and faster than Contentful
- Loom video walkthrough to be provided for GrowthX team on content publishing in Sanity

### Link Building and SEO Strategies

- Both teams interested in backlink exchanges with other accounts
- Webstacks aiming to increase Domain Rating (DR) in 2025
- Potential for automated outbound outreach for link building in the future
- Plan to track backlink information (websites, DR, linked pages) in Airtable

---

## Action Items

**Aida Knežević (GrowthX)**
- Generate Midjourney images for 10 new articles
- Edit, review, and publish 10 new articles on Webstacks site

**Devon Wood (Webstacks)**
- Send list of 10-12 prioritized articles from cluster research to Aida
- Send notes, brand guidelines, and website architecture info to Aida for article context
- Send list of key pages (blogs, assets, solutions, industries) for internal linking
- Update Aida on blog migration timeline to Sanity CMS next week
- Record Loom video walkthrough of content publishing in Sanity CMS

---

## Transcript

**Sadira Sittampalam:** Hey, I'm good. How are you?

**Aida Knežević:** Not bad. Haven't seen you in a WebEx call before.

**Sadira Sittampalam:** Yeah, I've completely cleared out all of the accounts I'd been assigned to. I hadn't really looked at them because I had so many before, but now that I'm getting freed up, I can actually contribute.

**Aida Knežević:** That's good. I think Kyle is also supposed to join.

**Kyle Gaudreau:** Hi Deva.

**Aida Knežević:** Hey guys, sorry for being a couple minutes late. Just getting to the office.

**Devon Wood:** No worries. And I think Jesse's a bit under the weather today, so not sure if he's going to do any of this.

**Devon Wood:** Oh man, it's been hitting all of us.

**Kyle Gaudreau:** I've been down with COVID the past couple weeks. I'm doing super good now.

**Devon Wood:** I was out two days last week because I couldn't handle it either, but trying to get through it. At least I had it last week because I'm visiting my family next week, so getting it out of the way.

**Aida Knežević:** I sent the agenda to our Slack, but as always we're going to go through it together. The big thing for this week is I've updated the performance report. Last week Jesse mentioned wanting to see data from Google Analytics in these reports, so I was able to pull all the blog performance data from GA4. This is organic search data by the way. If you want data from other channels, let me know.

**Aida Knežević:** I filtered out GrowthX content by uploading the list of URLs into ChatGPT and asking it to filter which are ours and which aren't. So you have the GrowthX content column, and active user sessions, engaged sessions, bounce rate — which is super important. Hopefully this will be more useful for you moving forward.

**Devon Wood:** This is pretty much exactly what we wanted. I appreciate you going through and digging up all this information. Separating the content and getting it in one view was really helpful.

**Aida Knežević:** Yeah, I thought of this approach while cooking dinner. The pages and queries tabs are still your Google Search Console data. So from last week to this week, we saw a nice uplift in weekly clicks — almost 500 clicks last week, driven by these top pages. The bank website design that we did a couple of weeks ago is doing really well, and design-related pages seem to be performing well week over week.

**Devon Wood:** Yeah, we've historically seen very good results from industry-type website design and the pages we did last week. I'm feeling very good about seeing major gains. I'd say probably in the next two months — historically things take about six weeks to reach peak, maybe a bit more depending on keyword difficulty — but usually within six to eight weeks we see full results.

**Devon Wood:** Overall, I know it's not the easiest working with these prompts and trying to get the content good, but I think so far we've done a pretty good job. Shout out to you for all that.

**Aida Knežević:** It was a really nice exercise for me too. It's fascinating to see how ChatGPT defaults to using a specific structure if you forget to add a specific note in the prompt.

**Devon Wood:** We're putting together our 2025 version of best B2B SaaS websites. We're human-writing part of it and then using ChatGPT. It's interesting how it forgets things very quickly. You have to do it in bits and pieces and keep reminding it. Working at scale is tough because that's what we're trying to do. It's definitely battling quality versus speed, and that's something it struggles with.

**Aida Knežević:** Sometimes it forgets to describe design elements and just describes product features instead. I even tried uploading five screenshots at a time to speed things up, but I almost broke it. So don't do that.

**Devon Wood:** Have you guys started using any other AI models, or are you just using ChatGPT? Have you tried DeepSeek or Gemini?

**Kyle Gaudreau:** To my knowledge, I'd be shocked if we were using DeepSeek in our existing workflows, but we definitely layer in a lot of different things based on what works better. Chunking is a huge part of what we're doing through various workflows. With ChatGPT, you can chunk things like let's start here, get that baseline, then progress. But what we're also doing is bringing in Claude for things it does better.

**Kyle Gaudreau:** We're mostly using U.com, Claude, and ChatGPT — U.com for research, ChatGPT more for article creation. We're building less of the sequential workflows straight in AirOps now; those are contained outside AirOps as APIs, giving us more flexibility. It's an interesting challenge because it always feels like a moving target. The team was sharing earlier that some outline outputs look different than expected.

**Aida Knežević:** Yeah, and I use Gemini in Google Docs sometimes if I need to edit a paragraph quickly. But you have to be very careful with the prompts. If a paragraph is too formal and I tell it to be slightly less formal, it does a good job. But if I tell it to be less formal, it goes crazy.

**Devon Wood:** We just set up our Gemini account this week. Jesse was creating custom Gems and feeding it our brand information. I haven't had a chance to play with it yet because we had some trouble setting it up, but I think Google fixed it now.

**Aida Knežević:** So these are our best-performing pages, the ones with the biggest increases in week-over-week clicks. In terms of content updates, we're generating and staging 10 articles this week. Am I going to generate Midjourney images, or are you going to share some?

**Devon Wood:** If you can do Midjourney, that would be great.

**Aida Knežević:** And on cluster research — I wanted to review that with you. I don't know if you had a chance to look at it if you were out of office.

**Devon Wood:** I looked at it yesterday before I logged off. Overall it looks really good. I think we can prioritize 10 to 12 of these.

**Aida Knežević:** I can give you a list by the end of today and then the rest we can keep in the backlog. There might be a different pillar we want to build 10 to 12 for next week. But I think these are all very good to keep on a radar for the future.

**Aida Knežević:** There were like 30 assignments here. Maybe we can prioritize some with slightly higher search volumes and then do the rest as more bottom-of-funnel content.

**Devon Wood:** Yeah, definitely. We want a mix of high-search-volume ones and bottom-funnel ones — useful for email marketing and other funnels we're running. Maybe I'll look through them again and see if I should provide notes for each one, or send brand guidelines and website architecture to help you and the AI get a better sense of the style and how we want to approach these topics.

**Aida Knežević:** The most important thing is having a rough idea of what you want the article to be about or the focal point. That's helpful for the outline. Anything else you want to provide, you can just add it to a notes column.

**Devon Wood:** Could I put together a document with your website and use ChatGPT to analyze it, then put that in AirOps?

**Kyle Gaudreau:** We do store site notes in AirOps as part of research, and that tends to be more relevant for internal linking. We've been evolving fast and Daniel, our CTO, has been pulled into these things, so I don't know the latest. But it's theoretically possible. The question is how much added effort it would take and what the reward is at this point.

**Devon Wood:** Maybe we can just approach it by having you provide the pages we want to be linking to — blogs, assets, solutions pages, industries — and feed that to you or put it in the notes. That can be our general theme of what we want to relate these topics back to.

**Aida Knežević:** Yeah, definitely. There's a column in AirOps for research guidance and we can input stuff there like which concepts you want the article to reference. That can help form the outline.

**Aida Knežević:** This is all I have in terms of updates. I'll generate Midjourney images tomorrow or maybe later tonight, and the articles should be done tomorrow. I'll edit, review, and publish them. On internal links — last week you said some articles didn't have enough internal links. The current workflow adds them automatically, but there's no way for me to control it. It pulls from the site map and adds weak sentences that don't make sense, so I delete them and add manually.

**Aida Knežević:** If you have up to 10 internal links you want to prioritize, I can add them manually or tell the freelance writer to add them. But I can't tell it to use a specific list right now. It's not a big deal.

**Devon Wood:** Yeah, that's not a big deal. The main thing is making sure they're all linking back to the pillar we're writing about. If there are ones we want to link to, I can give you a list and put them in the notes — like five or so links we want to hit in each article.

**Devon Wood:** One other thing — we're having an issue where external links aren't opening in a new tab. But the website redesign is in progress. Our home page is done as well as all our solutions pages. We're migrating client stories tomorrow and the blog next week. I'll keep you updated on the timeline so you know whether you need to publish in Contentful or Sanity. We can do a workshop with your team or create Looms to help you understand how Sanity works.

**Aida Knežević:** If you could record a Loom walkthrough of how content is published, that'd be helpful.

**Devon Wood:** I've already started one, and it's very similar to Contentful. So there's not much of a learning curve, and hopefully it's more organized and faster than Contentful. The Contentful instance is from 2020 and has some technical debt built up. Sanity is a fresh start.

**Aida Knežević:** Sanity is similar to Contentful, right? It's one of the closest alternatives. This is my first time using a headless CMS. I have a website using WordPress and had no idea WordPress was that bad. I don't have time for migration though.

**Devon Wood:** I love Contentful, and Sanity is great too. Headless CMS is easy. Nothing but good to say about Sanity so far. We'll make sure to provide plenty of Looms and everything else you need.

**Devon Wood:** For next steps, you can let me know which assignments to prioritize next week. Just leave notes in the column and I'll assign them.

**Devon Wood:** One other thing — are you guys doing backlinks with other clients? Is there any way we can do backlink exchanges?

**Kyle Gaudreau:** We've definitely been doing that for some accounts. I can't recall if we've recently, but we've started to build that process. Yeah, that's something we can explore.

**Devon Wood:** Great. We'd be open to link exchanges for any relevant content. We could record that info in an Airtable with website URLs, their DR, the pages we're linking to, whatever. In 2025, we want to increase our Domain Rating.

**Kyle Gaudreau:** Yeah, there are other things we could explore too. We have automated outbound outreach for link building that we continue to refine. It's become more complex with domain changes, but we've figured it out. Let's keep that in the back pocket and get initial traction with backlink exchanges.

**Aida Knežević:** Thanks guys. We'll be in touch with Devon on Slack and see you next week.
