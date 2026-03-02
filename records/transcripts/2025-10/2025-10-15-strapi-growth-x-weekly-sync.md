# Strapi <> Growth X -  Weekly Sync

<metadata>
date: 2025-10-15
time: 16:30 UTC
duration: 30 minutes
organizer: team@growthxlabs.com
participants: Mara Leighton, Vivek Shankar, Victor Coisne, Paul Bratslavsky, Theodore Kelechukwu Onyejiaku
fathom_recording_id: 94383308
fathom_url: https://fathom.video/calls/440500068
share_url: https://fathom.video/share/D4u7QZ9tDB3pMZmyKyUMU917ae8rNQMx
source: fathom
enriched_on: 2026-03-02 12:45 UTC
</metadata>

---

## Summary

Strapi and GrowthX aligned on content strategy priorities, with Mara and Victor scheduling a dedicated Friday meeting to discuss partnership renewal and engineering dependencies. The team confirmed 21 out of 128 comparison pages completed, 8 articles delivered last week with 7 more scheduled, and strong LLM visibility positioning Strapi ahead of Contentful, Sanity, and WordPress. Key blockers include engineering delays on the social workflow and Kappa content-gap integration, which the team plans to revisit in a few weeks, while Victor emphasized focusing on top-of-funnel content and pragmatically optimizing the five highest-traffic comparison pages first.

---

## Context

Strapi is a headless CMS platform and a key GrowthX client in their high-value services engagement ($200k+/year). This is their weekly sync to track content production, SEO performance, and feature releases. The partnership has been active for a year, and this meeting marks a milestone year discussion where Victor (Strapi's product/strategy lead) and Mara (GrowthX's delivery lead) plan to review next-year priorities and understand GrowthX's engineering dependencies. Strapi recently launched Strapi AI (automated content type building and media management) and content agents in October, which creates new content opportunities around AI SDKs and CMS relevance to developers building AI applications.

---

## Relevance

**To GrowthX Delivery:**
- Engineering bottleneck on social workflow and Kappa/Octolens integration is delaying content workflows; requires prioritization discussion during Friday renewal meeting to understand feasibility of fast-tracking integrations
- Medium workflow completed; CMS staging workflow has formatting issues but is largely automated; integration page meta update workflow executing well with completion expected by next day
- New weekly cadence: Vivek to send planned URLs to Theo/Paul starting this week for clearer delivery visibility and timeline management
- Action items tracking needs refresh; Victor flagged that delivery dates in tracker are outdated, creating visibility gap on actual project status

**To CheckThat/AEO:**
- Strapi maintains strong LLM visibility across tracked prompts, outperforming Contentful, Sanity, WordPress, and iGraph in ChatGPT citations
- Identified opportunity to map prompts where Strapi is absent (but competitors appear) to existing content for refresh and H2 enrichment to close LLM visibility gaps
- Victor emphasized Q4 AI content strategy opportunity around Vercel AI SDK, OpenAI App SDK, and CMS relevance for AI applications—aligned with Strapi AI launch and agent product releases

**To GrowthX Business Development:**
- Partnership renewal meeting Friday will discuss 2026 priorities, engineering dependencies, and resource allocation; strong account health signal given year-long engagement
- 21 of 128 comparison pages completed (16% progress); pragmatic approach to optimize top-5 traffic-driving pages first (Strapi vs WordPress, Strapi vs Contentful) before completing full set
- Content performance trending close to previous highs with non-branded impressions rising; most content pillars in top-10 positions; renewal timing creates natural expansion discussion point

---

## Overview

- Content pipeline is healthy, with focus on comparison pages and top-funnel content
- LLM visibility for Strapi is positive, outperforming competitors in tracked prompts
- AI-related content opportunities identified as a priority for Q4, aligning with Strapi's recent product launches
- Some engineering-dependent workflows (e.g., social, content gap analysis) are delayed due to prioritization

---

## Key Topics

### Partnership Renewal Discussion

  - Victor and Mara to have a separate meeting on Friday to discuss next year's partnership
  - Mara to share outline of discussion points in text format beforehand
  - Focus on aligning priorities and understanding engineering dependencies

### Content Production Update

  - 8 articles delivered last week, 7 scheduled for this week
  - SendGrid integration page to be published this week
  - Integration page meta information update workflow is progressing well

### Workflow Status

  - Medium workflow is completed and ready for use
  - CMS staging workflow has some formatting issues but is largely automated
  - Social workflow and content gap analysis tools integration delayed due to engineering priorities

### Comparison Pages Progress

  - 21 out of 128 comparison pages completed
  - Focus on optimizing top 5 traffic-driving pages (e.g., Strapi vs WordPress)
  - Team to take a pragmatic approach, enhancing high-traffic pages with recent case studies and updates

### Performance Report Highlights

  - Content performance close to previous highs
  - Non-branded impressions increased
  - Most content pillars in top 10 positions
  - Conversion events generally rose, with slight declines in pricing link clicks and contact sales

### LLM Visibility

  - Strapi maintains a competitive edge in LLM visibility across tracked prompts
  - Plan to address prompts where Strapi isn't showing up by mapping to existing content and refreshing

### AI Content Strategy

  - Q4 theme focuses on AI, aligning with Strapi's recent product launches (Strapi AI, content agents)
  - Opportunity identified for content around AI SDKs, plumbing for AI applications, and CMS relevance

---

## Action Items

**Mara Leighton (GrowthX)**
- Share renewal/priorities agenda with Victor today; schedule Friday renewal meeting via Victor's Calendly

**Vivek Shankar (GrowthX)**
- Send weekly planned URLs to Theodore and Paul starting this week
- Revisit social workflow with Jason and engineering team in a few weeks; update Victor
- Revisit content-gap integration with Kappa/Octolens with engineering team in a few weeks; update Victor
- Update project timeline and delivery dates in tracker
- Review image generation logo and data limits; update Victor; use infographics in articles
- Add LLM traffic charts to weekly report and recap
- Propose AI-themed listicle topics (Vercel AI SDK, OpenAI App SDK) to Victor

**Paul Bratslavsky (Strapi)**
- Investigate competitor-page reversion; confirm no scripts are overwriting GrowthX edits
- Optimize top-5 comparator pages (e.g., Strapi vs WordPress, Contentful)

**Theodore Kelechukwu Onyejiaku (Strapi)**
- Optimize top-5 comparator pages (e.g., Strapi vs WordPress, Contentful)

---

## Transcript
**Mara Leighton:** Probably a month out for the renewal. Meeting is being recorded. Heads up, she'll probably drop into the external channel today.

**Victor Coisne:** That sounds good.

**Victor Coisne:** Can't believe it's been a year already.

**Mara Leighton:** I know, that's wild.

**Mara Leighton:** I know, it doesn't feel like a year.

**Victor Coisne:** Yeah, I mean, it feels like there's this paradox of startup where it's weird.

**Mara Leighton:** You know, it feels like there's multiple years packed in one year, but at the same time, time is flying. I couldn't agree more. It's kind of what I said—this is totally stolen valor on my part because I'm not a parent, but I feel like it's what people say about raising kids: the days are long, but the years are short. That's how I feel.

**Victor Coisne:** That's exactly true.

**Victor Coisne:** You don't see yourself aging, but you see them growing.

**Victor Coisne:** Yeah.

**Mara Leighton:** Yeah.

**Mara Leighton:** Oh, that's a lovely way of thinking about it, actually.

**Victor Coisne:** Yeah.

**Mara Leighton:** Well, cool. I also have some renewal-related things for the next year of the partnership. I'd like to get your take on what your priorities are. I'd be happy to start with that and jump into performance, but let me know if you'd prefer a separate time. I'd love to get you things to consider by the end of the week.

**Victor Coisne:** Yeah, I think a separate meeting would be better. That way I can prepare more. If you want to send an agenda of what you're hoping to discuss—I want to understand the engineering team dependencies. It seems like that's a bit of a bottleneck in some cases. That way I can prepare and think about what we want to prioritize this year and how it aligns with our company strategy as we plan for 2026.

**Mara Leighton:** Yeah, that makes perfect sense. I'll share the outline of what I have in text today. If you have any feedback or want changes for later this week, I can definitely adjust. Do you have availability Thursday? If you have a Calendly, I can look at it.

**Victor Coisne:** Yeah, I have a Calendly at cal.com slash [my name]. I'll drop you the link. Friday would be better for me though.

**Mara Leighton:** Sure.

**Mara Leighton:** Paul, every time you join, it's a slightly different camera view.

**Victor Coisne:** It's exciting.

**Paul:** Was having small technical difficulties, but I'm good now.

**Theodore Kelechukwu Onyejiaku:** Hi, everyone.

**Paul:** That's actually my actual background. I like nice lights with my streaming setup.

**Vivek Shankar:** It's beautiful.

**Mara Leighton:** Well, thanks for sending your Calendly, Victor. I'll find some time, and then, Vivek, we can jump into the regular programming.

**Vivek Shankar:** Cool.

**Vivek Shankar:** Let me share my screen real quick.

**Vivek Shankar:** Okay, so just running through the updates, we delivered eight articles last week, and we have seven scheduled for this week, and one of those is the SendGrid integration page, so we'll have that out as well.

**Vivek Shankar:** Just walking through the outstanding issues, so the first one was the widening comparison page column.

**Vivek Shankar:** So I think last time we discussed, we were proceeding with the competitor versus competitor comparison pages, so I guess we can address this when those pages are done.

**Vivek Shankar:** The integration page workflow, updating the meta information for these pages, this workflow is done, so we're currently executing that workflow, just updating it for all pages.

**Vivek Shankar:** We expect it to be done by tomorrow, but generally the workflow works well, so there's no delays over there.

**Vivek Shankar:** And then the CMS staging workflow, we're still having.

**Vivek Shankar:** Some issues with the formatting, as Theo pointed out.

**Vivek Shankar:** We're working through it.

**Vivek Shankar:** It seems to be a bit inconsistent at times.

**Vivek Shankar:** But again, as I mentioned last week, this workflow is pretty much automated.

**Vivek Shankar:** It just needs a few finishing touches on our end just to make sure everything is going well.

**Vivek Shankar:** The medium workflow is done. Theo had provided feedback and clarified it in Slack, so we're pretty good to go. What we'll do is at the end of this week send over a list of URLs we're planning on publishing, and then you can let us know if there's any priority or timeline adjustments needed.

**Vivek Shankar:** The social workflow is a bit of a bottleneck right now given engineering priorities. There will be delays in creating this workflow for Strapi, so it might not serve your immediate needs, but we will definitely prioritize and revisit this. We'll keep you updated on when that bottleneck clears and we can start working on it.

**Vivek Shankar:** The next issue is the content-gap integration. Unfortunately, the messaging is the same here because it demands integration into Kappa and Octolens, which are tools specific to Strapi. There's a bottleneck in terms of the other workflows that engineering has prioritized. So we'll be revisiting this in a few weeks with engineering to see if there's any room to take it on.

**Paul:** What's specifically preventing you from integrating? I thought you guys already have access to Kappa AI. And in terms of Octolens, it's just a web service that gives you access to the data.

**Vivek Shankar:** Yeah, there's no technical difficulty. It's more that the engineering team has prioritized other workflows and product creation, so there's no room to take it on. Technically, I don't anticipate any issues, which is why we want to revisit this because it seems like something we can get done quickly.

**Mara Leighton:** Victor, that's something you and I should chat through on Friday. I need to understand what the likelihood is of the team having the capability to fast-track that. We can discuss how high a priority it is and if there's a way to factor that in to next year's work together.

**Victor Coisne:** Yeah.

**Victor Coisne:** Well, just for me, like, the, it seems like we, we've been kind of, like, um, Mm-hmm.nosticolelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelelele...

**Victor Coisne:** Moving a bit slowly on some of the other works—workflows and dependencies with the engineering team. We've been working on the image generation one for like six months, and the result isn't mind-blowing. We're getting there, but it took us a long time. I want to put things into perspective: it feels like we're adding a lot, but also a lot of stuff has been kind of stuck. Speaking of getting things stuck, I think it would be really good to update the timeline and delivery dates here because they're all in the past.

**Mara Leighton:** It's not helping us understand the true status of where things stand.

**Victor Coisne:** Yeah. To just give you visibility on what I consider priority, there's some stuff that I feel is table stake—like the integration with Strapi. That's something we used to have with AirOps.

**Victor Coisne:** And I think when you guys moved to Atlas, we also, so there was like a bit of a step back.

**Victor Coisne:** So like also that one I consider as like, you know, kind of table stake and we've kind of been waiting on that to get fixed.

**Victor Coisne:** The medium is like, that's like a bonus.

**Victor Coisne:** Like that's like, I don't see that as strategic.

**Victor Coisne:** I think it's like a nice to have, you know, it's obviously saves time for Theo.

**Victor Coisne:** So I think, you know, that's why we, and I feel like we, it was a bit harder than anticipated, but I wouldn't spend more time on, on the medium workflow that again, not strategic.

**Victor Coisne:** I think at this point, like what strategic is, is really looking at the, in particular, the integration with Kappa.

**Victor Coisne:** I think that's more than Octolance.

**Victor Coisne:** Like I think that's, that's also nice to have, but I think Kappa is a very important tool in, in, in the workflow, a different step of the workflow and we already use it.

**Victor Coisne:** It's a fact-checker in the fact-checking step.

**Victor Coisne:** But I think now it's even more relevant to use it for the discovery step.

**Victor Coisne:** And so, yeah, I think to me that I see that definitely as strategic.

**Victor Coisne:** We should think about it as it's more going to be content that is middle of the funnel, as in it will be strapi-related, right?

**Victor Coisne:** Because there are the content gaps within strapi.

**Victor Coisne:** And we want to spend most of our time at the top of the funnel.

**Victor Coisne:** think about GrowthX as top-of-the-funnel acquisition, like in terms of impression is what matters, non-branded ranking.

**Victor Coisne:** And so I think I want to talk about how we think about the distribution between top-of-the-funnel content and middle-of-the-funnel content.

**Victor Coisne:** Which is not, I think we don't have a very clear guidance at this time on what's the ratio in terms of volume and where we spend our time.

**Victor Coisne:** Does help a little bit?

**Mara Leighton:** Yeah, it definitely does.

**Victor Coisne:** Okay.

**Vivek Shankar:** Regarding the image generation, we shared the initial output with you, Victor—company logos, data, etc. We're running into limitations of the LLM itself in terms of what images it can generate. We'll take that back to the team and share your feedback. For now, we'll use the image generation flow for infographics within articles. In terms of the social workflow, I followed up with Jason, and the engineering workload is a bit blocked at the moment, so we'll revisit that shortly to see if we can get it up and running. I'll update all the action item dates to reflect current timelines.

**Victor Coisne:** I want to make sure we're good on the comparator pages because I'm a bit confused with the different updates.

**Vivek Shankar:** FAQ is done. From our end, we've staged all the Strapi versus pages. There was an issue with the WordPress page—it kept reverting to old content. Usman checked it yesterday and reported the page was updated with new content. The elements are in place, and we've been adding FAQs to the pages as well. We're going ahead with the competitor versus competitor pages.

**Victor Coisne:** Theo, you should have FAQ available as a component, so that should no longer be a blocker. What's holding us up from a website standpoint?

**Victor Coisne:** When you say staging, what do you mean?

**Paul:** When you look in Strapi, there are six drafts that were staged. There's confusion between the word staging versus in queue. Staging to us means it's in the Strapi backend and ready for review and publish. There were six updated competitor posts in staging.

**Victor Coisne:** In draft. The issue with Strapi v4 is that you cannot have a draft version of a published entry, which creates URL mismanagement and duplicates requiring redirects. I think you're on v5 though, so you should be good.

**Paul:** The way we looked at it is by "updated by GrowthX." Any comparator page updated by the GrowthX team is marked by type and the update date. If we see it updated by Theo a year ago, we know it hasn't been touched yet. That's the update from our end.

**Victor Coisne:** We should really make sure there's no script running and pulling from this—especially if content is getting reverted back. I don't know exactly how it's done on the backend, but we need to ensure there's no script erasing GrowthX's work.

**Paul:** The only automatic thing is table data from Excel/Google Sheets on the front end. I'll double-check on competitors. Whenever the page gets published or updated, whoever is logged in determines what's reflected on the site.

**Victor Coisne:** It would be worth getting clarity here because you're saying six, but Vivek, you're saying you did a lot more. It's been a while since we talked about those comparative pages. I'd really like to close this and remove the big table, which we've been waiting to do until everything is published.

**Paul:** Let me clarify. If we search by all the entries, we have about 21 items. The total is 128, so we have 21 out of 128.

**Victor Coisne:** Okay.

**Vivek Shankar:** I think the rest are competitor versus competitor pages, which will come in the next few weeks. Strapi versus should be all done.

**Victor Coisne:** We should take a pragmatic approach—look at the top five pages by traffic. It's probably Strapi vs WordPress, Strapi vs Contentful, and make sure we can make those as good as possible. I manually added some stuff to WordPress yesterday because we just shipped a new case study about people moving from WordPress to Strapi and a really nice video. That's context the GrowthX team might not have. Let's optimize what's already in the top five—keep investing in making those pages better since they're getting the bulk of the traffic. Does that make sense?

**Paul:** Yeah, that makes sense.

**Victor Coisne:** Cool.

**Vivek Shankar:** We're almost at time, so I'll run through the performance report quickly. We're pretty close to previous highs in terms of GrowthX-created content. Usually we have integration pages in the top five, but this week it's a mix. Non-branded impressions rose, which is good—Google seems to have fixed the errors from recent weeks. Most of our pillars are in the top 10. The refreshes we've been targeting expand keywords rather than doing complete overhauls. Overall, we're doing well in positions and clicks. Conversion events this past week rose across the board except for slight declines in pricing link clicks and contact sales. New contact generation through HubSpot is holding steady, and sessions are ahead of HubSpot goals. We'd like to do better with new contacts since the April peak, but we're heading in the right direction.

**Vivek Shankar:** Looking at LLM visibility, Scrunch changed their charts, so we now have a line chart instead of a bar chart. Strapi's presence is highly competitive and positive across all tracked prompts. Strapi is in first position ahead of Contentful, Sanity, WordPress, and iGraph. Citations have increased. Scrunch identified prompts where Strapi doesn't show up but competitors do in ChatGPT. Our action plan is to map those questions to existing content and include them in refreshes or content enrichment as H2s to improve ChatGPT mentions. Any questions?

**Victor Coisne:** Vivek, it would be really nice to look at LLM traffic charts in the weekly report—over time, how it's moving. We have it in Looker, but adding it to the report every week would be great.

**Vivek Shankar:** I'll add that in. Looker's being slow right now, otherwise I'd show it live. I'll include it in the post-call recap moving forward.

**Victor Coisne:** How are we doing on the backlog of topics in Airtable? We submitted some ideas, and you've been providing some too?

**Vivek Shankar:** The content priorities are comparison pages—about two to three a week. Based on our research of competition and audience, we have topics primed and ready. Most are top funnel with strong keyword correlations. Some explain how to do things with Strapi, which we're treating as mid to bottom funnel. The content pipeline is pretty healthy. If you see gaps in your research, send them over—we're happy to include them. But we're researching on our own too, so things look good.

**Victor Coisne:** At a high level, our Q4 theme is AI—we released Strapi AI in early October with automated content type building and media management, translation is coming, and we have content agents coming to Strapi. We're launching a new product that could benefit from AI content. I'm thinking we should look at what's trending, not just what's showing in data yet. People are using the Vercel AI SDK and OpenAI released the App SDK. There's a lot happening with the plumbing to build AI applications. Listicles around what's available, what's doing well, and how it relates to CMSs could help us get ahead of the curve. This might not show in data yet, but we know that's where the industry is going.

**Vivek Shankar:** Yeah, for sure. We'll look into that and propose some topics. We're totally on board.

**Victor Coisne:** Cool.

**Vivek Shankar:** That was pretty much it. We'll follow up in Slack. Thanks, everyone.

**Victor Coisne:** Awesome.

**Mara Leighton:** Thank you.

**Paul:** Thank you, everyone.

**Victor Coisne:** Bye.
