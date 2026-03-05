# Strapi Handoff

<metadata>
date: 2025-06-19
time: 16:31 UTC
duration: 32 minutes
organizer: sydney@growthx.ai
participants: Vivek Shankar, Sydney Go
fathom_recording_id: 69437383
fathom_url: https://fathom.video/calls/329319494
share_url: https://fathom.video/share/pP3XM9CLV2y6Cjv2SzF5yvgHEuZwgysk
source: fathom
enriched_on: 2026-03-03 16:45 UTC
</metadata>

---

## Summary

Sydney handed off the Strapi account to Vivek, covering content operations, publishing workflows, and account strategy. The team discussed Airtable structure for article tracking, Looker studio reporting dashboards that require weekly updates, and the major strategic pivot from new content development to auditing and refreshing over 1,000 existing blog pages due to exhausted content clusters and low CTR performance. Key deliverables include comparison pages, integration page refreshes (now with FAQs and formalized structure), and a full content refresh strategy addressing duplicate content issues and engagement challenges.

---

## Context

Strapi is a headless CMS company with a developer-focused product positioned against competitors like Contentful and Sanity. GrowthX provides B2B content marketing services to Strapi, creating in-depth technical articles targeting both back-end and front-end developers. Sydney Go had been managing the account for about 2.5 months when she handed it off to Vivek Shankar. The account is structured around two main content streams: editorial articles (published through Strapi CMS using Markdown) and integration page refreshes. The client team includes Victor (strategy-focused), Theo (technical developer), and Paul (technical developer), with day-to-day communication happening in Slack. A major challenge is catching all code errors in highly specialized technical content, which is being addressed through a fact-checking integration with Kappa.ai.

---

## Relevance

**To GrowthX Delivery:**
- Content strategy shifting from new clusters to refreshing existing content due to cluster exhaustion — impacts portfolio approach and messaging about pivots
- Kappa.ai integration for code fact-checking is now part of the workflow and differentiates GrowthX capability on technical accounts
- Airtable workflow needs cleaning and organization; unused tabs and legacy statuses from previous PM should be archived
- Weekly Looker studio reporting dashboard maintenance required — needs porting to Dave's template to include integration pages as separate category
- Client expectations are high on volume (legacy expectation of 10-12 editorial articles/month); opportunity to reframe around quality and optimization instead

**To CheckThat:**
- Comparison pages (Strapi vs. Contentful, Strapi vs. Sanity) present direct LLM citation opportunity — currently thin tables with no surrounding narrative
- Programmatic comparison page solution blocked by client hesitation; technical decision-makers (Theo/Paul) resist programmatic approaches despite business value
- LLM citations mentioned as recent focus area for Strapi strategy going forward

**To GrowthX Business Development:**
- Low CTR across entire Strapi website suggests engagement issues beyond content quality; legacy PM (Andre) minimally edited articles; opportunity to improve renewal perception through quality improvements
- Client willing to discuss scope expansion (social media repurposing, Reddit mining) but boundary-setting needed to avoid scope creep
- Account is receptive to upsells once framed as strategic additions; community mining potential exists but needs alignment with client's internal content creation process

---

## Overview

- Strapi targets both front-end and back-end developers, with a focus on technical, code-heavy content
- Content strategy shifting from new topics to refreshing existing content and comparison pages due to exhausted clusters
- Publishing workflow uses Markdown in Strapi CMS; fact-checking process involves Kappa.ai for code verification
- Client relationship requires balancing big-picture discussions with Victor and detailed technical input from Theo and Paul

---

## Key Topics

### Target Audience and Content Focus

  - Primary audience: Back-end developers, with some front-end developer content
  - Content type: In-depth, technical articles on coding and integration with Strapi
  - Occasional targeting of technical decision-makers, but rare

### Content Strategy and Management

  - Shifting focus from new content to refreshing existing articles
  - Auditing 1000+ blog pages for duplicate content and traffic performance
  - Planning to refresh comparison pages and add new ones
  - Challenges with thin content on existing comparison pages
  - Exploring programmatic solutions for comparison page updates (client hesitant)

### Workflow and Tools

  - Airtable used for content tracking and management
  - Looker studio dashboard for performance reporting (weekly updates required)
  - Publishing done through Strapi CMS using Markdown
  - Kappa.ai integration for fact-checking code in articles

### Client Relationship and Communication

  - Regular calls with client team (Victor, Theo, Paul)
  - Victor focuses on big-picture strategy
  - Theo and Paul provide detailed technical input
  - Slack channel used for day-to-day communication and updates

### Performance and Challenges

  - Low click-through rates (CTR) across the website
  - Engagement issues with existing content
  - Difficulty in catching all code errors due to highly specialized nature

### Competitor Tracking

  - Main competitors: Contentful and Sanity
  - Client often draws inspiration from competitor content

### Community Engagement

  - Active Discord community and presence on dev.to
  - Potential for mining community discussions for content ideas (to be explored)

---

## Action Items

**Vivek Shankar (GrowthX)**
- Follow up w/ Timmy re tags in Strapi CMS; get update on Usman's instructions

- Port Strapi performance reporting to Dave's template; incl. integration pages as separate category

- Take over comparison pages project after receiving initial batch from Sydney; plan next steps


**Sydney Go (GrowthX)**
- Create & send handoff doc to Vivek; incl. sections on quick wins, Strapi publishing workflow

- Clean up Airtable; process all pending items before handoff to Vivek

---

## Transcript

**Vivek Shankar:** I sent that long thread on Slack. I think Usman kind of answered most of them by the looks of it. I was thinking I could just run through those and get any clarifications in real time from you.

**Vivek Shankar:** Which persona are we addressing? Mainly developers. Is there any nuance here? Any specific type of developer or?

**Sydney Go:** So Strapi targets two types of developers: front-end and back-end developers. We lean more towards back-end most of the time because of the headless CMS that they are. But they do sometimes write for front-end developers and they're talking about Node.js and all those front-end languages that you can integrate Strapi with. Those are the two main ones. And then sometimes they try to target technical decision-makers, but very rarely. Usually it's in-depth how to actually code something, how to create something, so it's very developer-focused.

**Vivek Shankar:** I noticed a column called tags in Airtable. Usman said we paste the article, generate tags in Strapi CMS. I think that's more of a thing for Timmy. So I will ask Timmy to get in touch with Usman and then I'll update myself with Timmy.

**Vivek Shankar:** The category column — is that effectively the content cluster or content pillars?

**Sydney Go:** In Strapi CMS, we have to set tags and the category. They've got a set number of categories, and then Airtable automatically buckets our content under whichever one is based on the content.

**Vivek Shankar:** But do we have any content pillars on our site for tracking?

**Sydney Go:** We don't currently. We used to have content pillars, but because we have exhausted most of the content pillars, now we're just doing one-offs.

**Vivek Shankar:** Is that column still in Airtable, or did you remove it because it wasn't serving any purpose anymore?

**Sydney Go:** No, it should still be in Airtable. The clusters are Development Technologies, Framework, Performance Optimization, Content Strategy and Management, and E-commerce and Conversion Optimization.

**Vivek Shankar:** Where can I find that?

**Sydney Go:** It's in my personal view, in the Cluster Column.

**Vivek Shankar:** I can take a look at that later. The status metadata — was there a status called metadata review or something?

**Sydney Go:** Yeah, that's a leftover from the last content manager, and this account was handed off to me about two and a half months ago.

**Vivek Shankar:** I think this is one of Marcel's legacy statuses. I'll delete those eventually.

**Vivek Shankar:** The tabs in Airtable — there's a ton of them.

**Sydney Go:** Yeah, the only ones we really use are Assignments and Integration Page Refresh. The Assignments tab is all the new articles. Integration Page Refresh is all of their integration pages and what status it's at. All of these are already with the customer, and they started uploading last week.

**Vivek Shankar:** And these refreshes — are there more to come or is it just the integration page?

**Sydney Go:** These are done. We just have to monitor performance basically. We added an FAQ and formalized the structure of the integration pages so they're not super thin. The last content manager started with a content refresh in their contract, but then they didn't like it and abandoned it. So the only one we really use is the integration page refresh.

**Vivek Shankar:** And all of these other tabs — do we still need them?

**Sydney Go:** I didn't want to delete anything just in case. I keep the GX integration pages because they sometimes add new integration page ideas there. But outside of that, I've never used metadata optimization or the other tabs.

**Vivek Shankar:** So the performance reporting — how are you handling this? Do you have your own Looker built out or is Dave building one?

**Sydney Go:** I built their Looker studio, and there's a little bit of maintenance that goes into it. Let me show you the reporting dashboard. I update this every week. It's not super hard to update. The only tabs I update are GSC data, keyword data, and Google Analytics data. It's a week-on-week review of what we've done.

**Sydney Go:** So this is the Strapi GrowthX Performance dashboard — the week-on-week review of our content. It tells us what articles were published last week based on what Theodore publishes and then the specific performance of each of our articles. So I usually organize it so you can see what's getting the most engagement. The biggest challenge with Strapi is that their CTR is not great, and it's like that across the company. The whole website is kind of low.

**Vivek Shankar:** So this makes sense. That's why Jason was mentioning the LLM performance. I'm going to port everything over to Dave's template when time comes. Since he works off the assignment tab, I'll move the integration page refresh URLs into the assignments tab but categorize it as integration pages so he can cohort it separately.

**Sydney Go:** We should probably keep those separate.

**Vivek Shankar:** Yeah, the Airtable doesn't have any publish dates? Is that hidden as well?

**Sydney Go:** Yeah, it's hidden. I can see it. They do want a separate Looker tracking for their integration pages and soon to come comparison pages. So they want that to be separate from their blog articles because they want to see if the refresh is made.

**Vivek Shankar:** So you mentioned integration pages — what was the second one?

**Sydney Go:** Comparison pages, we've not started yet, but that will be in the content refresh. We're doing a full deep dive into their strategy. Basically we're going through all of their URLs because they have a lot of duplicate content. Like, how to build an e-commerce store and how to build an e-commerce website are basically the same thing, published two years apart. Same with Angular versus React content. So we're going through all of their content and assessing whether there are indeed duplicate content issues, and then going through all of their old content because they have over a thousand blog pages and seeing which ones are dropping in traffic and need to be refreshed. We'll give them a list of comparison pages that they need to refresh or enrich, and also a list of refresh pages. We might pause on new content because there's so much content that needs to be either consolidated or refreshed.

**Sydney Go:** Again, they have CTR problems and engagement problems.

**Vivek Shankar:** Why are we refreshing just the comparison pages then? If we're auditing every single page, why are they focusing on just the comparison ones?

**Sydney Go:** No, we're also auditing the other content. We're going to have two buckets of refreshes: their old content that's on their blog, which will be refreshed as well, and the comparison pages will also be refreshed and new ones added.

**Sydney Go:** The comparison pages are currently very thin — it's just like a table with nothing around it that tells you how we talk about Strapi in comparison to other products. This is a great opportunity for LLM citations. So we're going to add data around that. The challenge is that it all pulls from a Google sheet, so they don't really know how to build it so they can put words around it. They're asking for two things: one idea on what these should be, and content so they know how to format it. So we'll probably send them five in the first batch along with a strategy refresh, and then you're going to have to take it forward from there.

**Vivek Shankar:** This looks like a programmatic thing. Why can't we just tell them we'll build some engineering into these pages from their Excel sheet, and they just keep updating it with elements on page?

**Sydney Go:** We actually talked about it with them last time. I think it's because their content team — Victor, who is very happy with almost everything that we're doing all the time, and then there's Theo and Paul, who are more into content and very hesitant to do anything in the programmatic space. They're the ones pushing back on this. Maybe you can push the conversation further because you have more knowledge about the back end of all these things.

**Vivek Shankar:** Okay, so summarizing the refreshes, we're doing regular blogs and these pages are a part of it. I can get up to speed with what content you're sending when you send it over.

**Vivek Shankar:** When you mentioned exhausted content clusters, it seems like you're focusing more on refreshes as opposed to developing new clusters, right?

**Sydney Go:** Yes.

**Vivek Shankar:** The publishing workflow — Usman said he can show me during our meeting today. But high level, what is the workflow?

**Sydney Go:** No, we are doing it for them. Everything is in Markdown code and it's all in Strapi CMS, so I can just share the password and login.

**Vivek Shankar:** Yeah, so I will be sending you a handoff document. What will you be including?

**Sydney Go:** So here's the handoff document that I'll be sending you. It'll have information about the Strapi team, what they want, about each of the team members, deliverables, and reporting. For the deliverables, I'll tell you what the editorial pages are, integration pages, what we've done so far, the CTAs that we use because we have custom CTAs, the comparison pages, and then I'll also add the reporting artifacts and the results from the audit that we're going to do.

**Vivek Shankar:** And if you don't mind, can you add a section in there like quick wins — something that I can just do right away?

**Sydney Go:** Okay, so I'll do a quick wins section, and I'll also add publishing and Strapi publishing workflow.

**Vivek Shankar:** One more thing — one of the articles in Airtable classified as a tutorial is under review. It's how to set up multilanguage Strapi website with Next, and Paul said it should include a repo to an example project. What is he talking about? Is this GitHub stuff?

**Sydney Go:** Yeah, it's a GitHub repo. So we have a batch under review because those were supposed to go through the fact checker and just slipped through the cracks, sorry. I'm going to try to clean up the Airtable and get everything through before I hand them off to you. But one of the quirks of Strapi is that they're very strict with all the code, and because Theo and Paul are both developers, we just can't catch everything. So there are articles that are code heavy that we're testing with a fact checker, but it's still not quite there. I don't think it's possible for any one person to catch all these errors unless you're Theo, apparently, because he's just amazing. He knows so many languages and specialties as a developer. Even Jason goes through these and asks how he caught things.

**Sydney Go:** So one of the special tools that we use for Strapi is that they've got a fact checker that they've set up with Kappa.ai. We ported that over to our workflow. Every time we create an article with code, we run it through Kappa.ai. Kappa will tell us if the code is correct for the version that we're writing for. So if it's Strapi v5, it'll check for Strapi v5. It should catch all of the code errors. I'll ask about whether it's already in our Atlas grid, but that's one of the things the under-review articles are going through currently.

**Vivek Shankar:** So it's all built into the article gen grid.

**Sydney Go:** It's not like a separate thing.

**Vivek Shankar:** I noticed there were two published articles that don't have a URL. It's 15 Advanced ChatGPT Prompts and Five Types of Relationships in SQL, Why They Matter. Just those two.

**Sydney Go:** Yeah, that should be in there because that's in my tracking doc.

**Vivek Shankar:** Who are their main competitors?

**Sydney Go:** They focus on Contentful and Sanity mostly as where they get their content ideas from. There was one more recently, but then I think they took one article from them and decided it's fine. So Contentful and Sanity are the main ones. When Theo sends ideas, they're usually in form of titles. So if you just copy them and search in Google, you can see what the inspiration article is from.

**Vivek Shankar:** They have a community. I haven't gone into Discord yet, but on their website there's content like how to populate a dynamic zone with media. Are we mining this or is there value in that?

**Sydney Go:** You can join if you want, but what they do is they take out our articles and share them with all their communities. They have one on dev.to, they've got a Medium page, and they've got a Discord group community. What we're trying to do currently is set up an API so that when they publish to their blog, it also publishes to Medium and dev.to as well.

**Vivek Shankar:** Are we treating their community like Reddit? Is there any value in that?

**Sydney Go:** We may be able to, but you'll have to talk to Theo and Paul about that, because they do create content side by side with us, and I think they take ideas from the community, so there might be some overlap. That's a conversation we haven't brought up recently, so it could be something to explore.

**Vivek Shankar:** Do they have a podcast or given us resources about where their community hangs out?

**Sydney Go:** No, but we link a lot to their Discord community. They've got Strapi open office hours. They publish regularly to Dev.to. If you look up both Paul and the CEO, they've got pretty extensive GitHub repos where they post Strapi examples with full code.

**Vivek Shankar:** Anything else I missed? Any mines I'm heading into?

**Sydney Go:** No, Strapi is pretty easy. The way I communicate with their team is pretty straightforward. You start the call with usually top-level ideas, and Victor is very happy with that. Like tell them this is what's moving forward, this is what's not. Recently it's been a lot of LLM citations — just the big picture of what we're doing and what we want to get into. Sometimes Paul or Theo will chime in with the more granular way of implementing that strategy, and they'll tell you what they want. Usually with Paul and Theo, it's very prescriptive and detailed, and then Victor is very big picture.

**Sydney Go:** Most of the small picture chats come into the Slack channel. They're treating us basically as part of their team, and Theo will give his updates for the week on publishing in the Slack channel along with his questions and feedback. As long as you keep talking about the big picture and telling Victor what's happening and where we're moving forward, he's generally very happy with all the efforts. The thing you have to look out for is that they will keep asking and asking for things. One recurring conversation is maybe we can repurpose content for social media and Reddit, which could be an upsell. But they're not quite ready, I think they just want us to do it. And we've been pushing back on extra requests. If we subtly tell them something could be an upsell, they pull back. So they're actually very good about it.

**Vivek Shankar:** One of the things I do want to push back on is the number of articles we're sending. It seems like too much. But yeah, with the refreshes, there's a good base over there.

**Sydney Go:** One tactic that maybe you could employ is to push for doing the comparison pages because it will help with LLM citations, branding Strapi as you want LLMs to talk about Strapi both as just the product and in comparison to other products. That might help you push the conversation of comparison pages forward. I don't even know what their work streams are, to be completely honest. It was mature and then we kind of put in free stuff. Any time I try to lower the number of editorial articles we're delivering, Farrokh and Osman have been trying to get everything through, but they are really hard to write for. Every time I try to push back on the number of editorial articles, they go back to oh, but the last PM was giving us 10 to 12 editorial. The last content manager was just too much work, and our workflows weren't there. He was not editing, like he was very minimally editing all the articles. And when I went through the articles, a lot of them weren't optimized very well. They weren't structured very well and they didn't really talk to the target audience, which is probably part of the reason why we're having the CTR and engagement issues. So maybe you can focus on telling them we're pulling it back so we improve quality.

**Vivek Shankar:** So this was one of Andre's legacy accounts.

**Sydney Go:** Oh, yeah. He had like 10 accounts and he was managing all of them. I remember he and Prateek were the only ones kind of running 10 accounts or something.

**Vivek Shankar:** Actually, I actually spoke to him recently. He's taking a sabbatical. He's like GrowthX kind of burnt him out.

**Sydney Go:** Thanks for getting on this call. It's pretty helpful for organizing things.

**Vivek Shankar:** Thank you, Sydney. I appreciate the handoff talk as well. I'll hop on a call with Usman now.

**Sydney Go:** Bye. Thank you.

