# Webstacks<>GrowthX Weekly Sync

<metadata>
date: 2025-03-13
time: 16:31 UTC
duration: 29 minutes
organizer: aida@growthxlabs.com
participants: Aida Knežević, Devon Wood, Jesse Schor
fathom_recording_id: 51770604
fathom_url: https://fathom.video/calls/251541804
share_url: https://fathom.video/share/qJcys_d1bx8wyRKdxZRpHW-SofnQyFvz
source: fathom
enriched_on: 2026-03-04 18:30 UTC
</metadata>

---

## Summary

Webstacks and GrowthX reviewed a new automated Looker Studio performance report that tracks weekly metrics in real-time using Google Search Console and GA4 data, with a new addition of LLM referral traffic tracking showing AI sources now as the top referral channel. The team discussed an upcoming new component for Sanity CMS — embedded pillar content on capabilities pages with 600-750 word Q&A sections designed to rank these pages higher than individual blog posts through internal linking. Key action items include Aida completing content enrichment using customizable conversion panels and setting up a redirect for a refreshed article that was published with the wrong URL slug.

---

## Context

Webstacks is a digital agency/technology partner working with GrowthX on content strategy and website optimization. This is a routine weekly sync between the Webstacks delivery team (Devon Wood and Jesse Schor) and Aida Knežević from GrowthX. The relationship involves ongoing content work, technical implementation, and performance reporting to support Webstacks' SEO and visibility goals. The site rebuild from late January to mid-February created a baseline for measuring new performance, which is now being tracked through the automated Looker Studio dashboard Aida built. The team is actively in a content refresh and rewrite cycle, with new strategic initiatives (pillar content components) being developed to boost mid-funnel page rankings.

---

## Relevance

**To GrowthX Delivery:**
- Automated performance reporting reduces manual work — new Looker Studio dashboard tracks weekly GSC and GA4 metrics with real-time updates and customizable date ranges, now including LLM referral traffic as a new tracking dimension
- Content management workflow clarified: conversion panels (non-shared modules) can be customized per page for copy, headline, and CTA, while shared CTAs can be reused to reduce redundant work
- New Sanity CMS component (embedded pillar content) requires 600-750 word Q&A sections on capabilities pages; Devon is building these out, but GrowthX needs to prepare content and potentially build new workflows in AirOps

**To CheckThat:**
- AI/LLM referral traffic is now the highest-performing referral channel for Webstacks, outperforming traditional referrals (guest blogs, etc.) — suggests strong AI visibility opportunity
- Profound agency (specializes in LLM rankings/AEO) was mentioned as a potential competitive or learning reference; Kyle Gaudreau indicated GrowthX could potentially build similar capabilities for clients
- LLM traffic isn't converting to direct sales yet, but provides strong top-of-funnel signal; opportunity to explore unique conversion experiences for AI-driven visitors

**To GrowthX Business Development:**
- Webstacks account showing positive momentum: site rebuild (weeks 2-7 of 2025) generated impressions/clicks growth, new reporting infrastructure now in place, and strategic content initiatives being planned
- Aida's work on conversion panels and pillar content is core value delivery; next week Webstacks' new Managing Director (Jacob) will join to explore additional content directions beyond standard blog pillars
- Risk flag: article published with wrong URL slug; redirect setup is simple but process needs tightening (Jesse handles redirects, but communication flow needs improvement)

---

## Overview

- New automated Looker Studio report implemented for real-time performance tracking, including LLM referral traffic
- Significant increase in traffic from AI/LLM sources, outperforming other referral channels
- Plans to create new pillar content for capabilities pages to boost rankings and internal linking
- Upcoming focus on content refreshes, rewrites, and potential new content directions

---

## Key Topics

### Automated Performance Reporting

  - New Looker Studio report automates weekly performance tracking
  - Includes data from Google Search Console and Google Analytics 4
  - Real-time updates with customizable date ranges
  - Added LLM referral traffic tracking for entire website
  - Perplex City driving traffic to their own page noted as interesting

### AI/LLM Referral Traffic

  - Significant increase in traffic from AI sources, outperforming other referrals
  - No direct conversion impact observed yet, but positive for overall traffic
  - Potential to explore optimization strategies for LLM visibility
  - Mentioned "Profound" agency specializing in LLM rankings (not currently engaged)

### Content Strategy and Website Performance

  - Positive growth in impressions and clicks since site changes (weeks 2-7 of 2025)
  - Current focus on content refreshes, rewrites, and enrichment
  - Plans to start new content creation after current refresh cycle
  - Exploring non-blog content formats for diversification

### New Website Feature: Embedded Pillar Content

  - New component for capabilities pages to boost rankings
  - FAQ-style rich text component with internal linking
  - Aims to rank capabilities pages higher than individual blog posts
  - Content length target: 600-750 words per pillar
  - Consultative, advisory tone for pillar content
  - Will be implemented across multiple capability pages

### Content Management in Sanity CMS

  - Demonstrated use of conversion panels and shared modules
  - Options for customizing copy, headlines, and CTAs in conversion panels
  - Various panel variants available (downloadable asset, client story, brand, internal, newsletter)
  - Shared CTAs can be used to simplify content creation process

---

## Action Items

**Aida Knežević (GrowthX)**
- Do content enrichment tomorrow using conversion panels (non-shared modules); customize copy, headline, and CTA for each page
- Send redirect link for old CMS article URL to Webstacks team via Slack

**Jesse Schor (Webstacks)**
- Set up redirect for old CMS article URL once Aida sends the link

---

## Transcript

**Aida Knežević:** How's it going?

**Aida Knežević:** Pretty good.

**Devon Wood:** We've had a really rainy week here, which is strange. But overall it's pretty good — I came down from the high of last week. I went to watch pro tennis in Palm Springs last week, and it was an incredible time. Really nice to be back in the swing of things.

**Aida Knežević:** Do you like tennis?

**Devon Wood:** Yeah, I play a lot and I've played since I was very young. So it was cool to see all the pro people that I've been watching on TV for years. All the big names were there.

**Aida Knežević:** Joe Covich is one of those players — it's kind of weird seeing someone from the Balkans make it big in pro sports. But I guess it's not unusual these days because a lot of NBA players are from there too. What countries are considered the Balkans?

**Aida Knežević:** Serbia — well, we're Western Balkans technically. It's more of a political term, but it's Serbia, Bosnia, Croatia, Montenegro, Kosovo, Bulgaria.

**Devon Wood:** I was going to say Bulgaria because Mateo Berrettini was there too, and he's from Bulgaria.

**Aida Knežević:** Yeah, but for example, Slovenia is technically also the Balkans, but they don't want to be grouped in with us. It's kind of like how they act a bit snooty about it.

**Aida Knežević:** Hey guys, what's happening?

**Jesse Schor:** Are you saying that about Luca because he's in LA now, or is that just how all Slovenians are?

**Aida Knežević:** That's how all Slovenians are. I don't follow basketball, but I see it on Instagram and stuff.

**Aida Knežević:** So I don't know if you already saw it in the agenda, but I was finally able to automate your reporting in Looker Studio. From this point forward, we're going to use this rolling performance report which updates in real time with data from Google Search Console and Google Analytics. It still tracks data the same way — it still follows a weekly cadence. So you can still see the same week-over-week performance in one place, and you can adjust the dates. Right now we're seeing data from the last week, from last Thursday to this Wednesday.

**Aida Knežević:** And then when you go to page two, this is your Google Analytics 4 data. It looks quite similar to the Google Search Console data on the previous page, but you can tell the difference because it shows sessions, bounce rate, and engagement rate. Since you're just viewing the report, you can't adjust the type of data that's shown here, but if there's something else that you want to see, you can let me know. And I can either give you permissions to edit the report yourselves, or I can do that for you. The queries are down here.

**Aida Knežević:** And then the last page of the report contains LLM referral traffic, which is something that some of our clients have been interested in. So we decided to include it here with your report. It basically uses GA4 data to see which LLMs are driving the most traffic to your site. It includes the entire website, so not just blog posts.

**Devon Wood:** That's awesome. Yeah, there's something we haven't really looked into before. So it's really interesting to see, even like Perplexity driving to their own page, is pretty neat.

**Aida Knežević:** Yeah, this is awesome.

**Jesse Schor:** Thanks for putting this together, Aida. It's super helpful. Yeah, I was really interested in this referral traffic because I've been noticing a consistent uptake. I think I mentioned in one of our calls that we're seeing more and more traffic coming from these sources. Still not totally sure what optimization we can be doing to increase it, but whatever we're doing, it's clearly having an impact. It's probably a lot of just making sure we're doing the right things for on-page SEO and infrastructure data is properly set up. Devin's working on some on-page cleanup now, but yeah, I just find it super interesting. So many referrals that we're getting right now are coming from AI. And it's not even close in comparison — we have guest blogs on other sites, and yeah, so this is really interesting.

**Aida Knežević:** I actually asked ChatGPT to give me a list of the top 10 tools for a specific use case, and then I asked it what criteria it used to list them. It uses G2 mentions and a lot of trust signals that I think Google also uses in rankings. But there's another client that actually shared this agency with me. It's called Profound — it's an AEO agency and they help people show up in LLMs. I don't think you're working with them, but it's something you can look into to see what they're doing. If they're giving you a list of LLM rankings, they have to be pinging GPT and other LLMs a lot. So there are a lot of questions around how much they're using these LLMs and if they can handle that type of traffic, but it's an interesting thing to look into if you're interested.

**Jesse Schor:** Yeah, are you guys working with them, Devin? I came across them in January and sent it to you. But are you guys working with them, Aida?

**Aida Knežević:** No, we're not working with them. A client mentioned them yesterday, and then Kyle said that this is actually something that we technically could build for our clients. But we're not working with them.

**Jesse Schor:** Okay. Well, if you guys start to deconstruct what they're doing and are looking for test subjects, let us know. I'm super curious about it. The thing is, I'm not seeing a ton of conversions from it. It seems like a positive signal for traffic sources, not necessarily for driving direct conversions. Which probably makes sense — if you get these articles as sources, you're checking them out to make sure they're legit, but then you're continuing to work out of Perplexity and ChatGPT. Whatever tool you're actually using for your prompts. But I am curious to see if there's something we can test with on it.

**Aida Knežević:** Yeah, I mean, it all boils down to what kind of topics we're covering and how they align with your customers and what they're looking for. I think some of the content that we've published in the past was quite middle of the funnel, top of the funnel, so it's not going to get as many conversions as we would like.

**Jesse Schor:** If this is just a source of additional traffic for us, that's awesome, and clearly it is. But yeah, I think maybe some testing — even things we can do on our end to create unique experiences for people coming from these sources — that might be a good test for us. Quick question on the session. Is this an aggregate of week-over-week progression, or is it showing each week and we're seeing the trend line continue to go up?

**Aida Knežević:** Do you mean this page or the first page?

**Jesse Schor:** The first page — clicks and impressions.

**Aida Knežević:** So yeah, this is aggregating weekly data. It should be the same as before, but it's just populating automatically. This table shows a page breakdown of clicks using Google Search Console data.

**Jesse Schor:** So week three of 2025, week four of 2025, and so on — it would be interesting to see a binary breakdown of new versus previous traffic.

**Aida Knežević:** So the chart shows it — the graphs aren't building off each other. Each bar shows the data for a specific week only.

**Jesse Schor:** Okay, so this is already showing that. Awesome.

**Aida Knežević:** Yeah, I wanted to keep it very similar to what we were doing before, just better and faster.

**Jesse Schor:** Yeah, I think especially as we look at the end of January. We made the switch for our initial pieces of our new site around week two, and we completed it around week six or seven. So this is a very positive sign, especially in comparison to the latter half of 2024 in terms of overall impressions and growth.

**Aida Knežević:** Right now we're working on refreshes and rewrites, and in parallel I'm also doing enrichment. We talked before about personalizing conversion panels, but I was using shared modules. I'm not sure if I can personalize them — change the copy, headline, or CTA — because the way the shared modules are set up right now, I just add the existing, pre-made ones. I don't make any changes to them.

**Devon Wood:** So with shared modules, if you change one, it changes on every single page where it's used. So you have to use a conversion panel component instead. I can show you if you want.

**Jesse Schor:** Yeah, do you want to go to Sanity real quick? We can show you.

**Aida Knežević:** No, because the last time I tried to use conversion panels, they weren't working, and I just didn't want to do them again.

**Jesse Schor:** It should be working now, Aida. Do you want to go to Sanity? I can show you.

**Devon Wood:** Yeah, I can share my screen. My Sanity is a bit slow, but okay. So this one right here is a non-shared module. When you make one of these, it's one of one, so you can fill it out, copy it, and paste it elsewhere without having to do the same thing for a new conversion panel. You can do this instead of making a shared module.

**Jesse Schor:** You can go to another blog post and paste it and it will still work. If you click on that conversion panel, Aida, and click on the CTAs here, you can pull in a shared CTA for any use case — like downloadable assets or booking an intro call. There's a client stories variant too. So you can build a custom conversion panel with a new header and sub copy, then use a shared CTA. You don't have to use a shared CTA — you can create a new button — but shared buttons help simplify the process. You have autonomy to customize the copy of the conversion panel and bring in a shared CTA to save yourself work.

**Devon Wood:** We don't have them all built out for client stories and technology pages yet. I'm planning to build out some of those this week by going through our top blogs. So you might see them here, but I can also show you how to build one from scratch if you want. Say we have a blog on Contentful and we don't have a technology conversion panel yet — you can go in and build one easily.

**Jesse Schor:** Yeah, import those in if we think we're going to use them. Yeah, so you have those options. And if you click on the variant here, Devin, this changes the fields available to you. We have a few different versions of the conversion panel depending on the use case. For client story, you can pull in a testimonial from one of our clients and search if you're looking for something particular. Downloadable asset and client story are pretty straightforward. Brand is more of a sales CTA for pushing to the sales page. Internal is for internal pages or capabilities pages. And newsletter is for newsletter subscribe. You can technically use any of them the way you want, but it gives you the optionality.

**Aida Knežević:** Okay, this is good. It was a good refresher because I'm gonna do some enrichment tomorrow. I'm gonna use that. One other thing — is it easy for you guys to set up a redirect? One of the articles I refreshed was comparing Webflow and HubSpot, but the URL slug was content management systems. Someone published it live without telling me, and now we need to set up a redirect from the old URL, which is showing an error now.

**Jesse Schor:** Yeah, if you want to send over the old URL, you won't be able to access the redirects with your permissions. But it's really easy for us to set up. Just send over the link and we'll set it up. Sounds good. So next week we're doing additional refreshes and rewrites, and after that we can start working on new content. I know you mentioned working on additional pillar pages, but if you want us to look in a different direction, we can definitely do that. Last week, a new Managing Director joined — his name is Jacob. He's double-booked so he couldn't join this meeting, but next week he's supposed to be here. He's worked at G2 before and at Active Campaign, so he can definitely help us find additional content avenues if you don't have specific pillars that need support.

**Devon Wood:** Yep, that sounds good. I'm sure there are a couple other topics, but there's definitely a desire to create something other than blogs.

**Jesse Schor:** Devin, can you bring up the Contentful embed pillar? Ada, one of the things I want to loop you into that we're working on — Devin's working through this — basically we have this new component. Let me show you an example of it. If you scroll down to the bottom of this page, this is what it's based on. It's basically a rich text component where we can do some internal linking and have additional pillar content that exists on one of our capabilities pages. The intention is to try to get these mid-funnel pages ranking higher than one of our blog pages alone. With these beta pillars, we answer more specific questions. This is for our Contentful Agency page, and we have questions about the Contentful platform — how do I know it's right for the business, how does it integrate with my tech stack. These headers are based on keyword opportunities we might already have blogs for. We're pulling this content into the capabilities page, and it'll exist in the footer. Devon's building this out for the Contentful technology page, but then we'd love to get some other pages you want to add this to. The content is much shorter than blog posts — we're shooting for around 600 to 750 words total. The perspective is intended to be more consultative and advisory depending on the page. This would hopefully be a way to boost rankings of these capabilities pages while using them as pillars for content on our blog, using internal linking to link out to other pages on the blog, and then linking back from those blogs via internal link or conversion panel. So it's a way to bolster up the capabilities pages.

**Aida Knežević:** Yeah, yeah, that sounds like something we can definitely do. We don't think we have specific workflows for it in AirOps, but we can build them. I have a hard stop right now — I have a meeting after this. But we can talk about this in Slack. You can share any additional resources you have, and let me know how many pages you're planning for this type of project. We can plan that for not next week, but a week after.

**Jesse Schor:** All right, sounds good. So I'll send you the redirect links. And yeah, everything else is in the agenda, so you can take a look at it when you have time.

**Devon Wood:** All right, thank you guys.

**Aida Knežević:** I'll see you next week.

**Devon Wood:** Bye.
