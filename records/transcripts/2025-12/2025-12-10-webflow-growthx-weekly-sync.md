# Webflow <> GrowthX - Weekly Sync

<metadata>
date: 2025-12-10
time: 19:00 UTC
duration: 30 minutes
organizer: team@growthxlabs.com
participants: Jason Gong, Liz Kushnereit, Colin Lateano, Luke Stahl, Raymond Camden, Zach Plata, Kelly We, Meg Murray, Kirat Chhina, Michael Huard, Sydney Go, Vivian Hoang, Anushri Gupta, Darin LaFramboise, Rachel Wolan, Vic Plummer, Najam
fathom_recording_id: 107809754
fathom_url: https://fathom.video/calls/500566159
share_url: https://fathom.video/share/Q4d1mqZBo9ygVWh1sZdCme1_nxcVMJq5
source: fathom
enriched_on: 2026-03-02 00:00 UTC
</metadata>

---

## Summary

GrowthX and Webflow reviewed progress on three major content initiatives: pausing use case guides to implement feedback (adding JSON examples showing data transformation between APIs and Webflow's CMS), optimizing integration pages for SEO and CRO by analyzing top-performing pages, and planning a category refresh pending confirmation of 301 redirect implementation. The team also discussed a broader developer hub vision and confirmed that GrowthX is shifting to a project-based delivery model with specialized experts (dev marketing, AI workflows) to support faster iteration.

---

## Context

Webflow and GrowthX have an ongoing partnership focused on developer content and integration documentation. GrowthX handles strategy and production for use case guides and integration pages — how-to content that shows developers how to build with Webflow and external services (e.g., SoundCloud, Stripe, Notion). Webflow's Colin Lateano, Luke Stahl, and others oversee developer experience strategy; GrowthX's Jason Gong and Liz Kushnereit manage content production. Raymond Camden, a new DevRel hire at Webflow, recently reviewed early use case guide drafts and provided technical feedback. This meeting is a weekly sync to align on priorities, troubleshoot blockers, and plan next steps before the holiday break.

---

## Relevance

**To GrowthX Delivery:**
- **Use Case Guide Shift:** Feedback from Raymond and Colin clarified that guides must show the "shape of data" — JSON examples of how external APIs and Webflow's data structures differ — before publication. Removing repetitive generic advice (testing, rate limits) creates room for more technical value.
- **Team Model Change:** GrowthX is moving to a project-based staffing model, pulling in specialists (Kathy for dev marketing, Kirk for AI workflows) rather than centralizing delivery through Jason. Liz remains the constant. This will accelerate content cycles for both integration pages and use case guides.
- **RAG System Opportunity:** Liz flagged that limiting AI content generation to Webflow's `developer.webflow.com` (instead of broader crawls) could improve guide quality and reduce validation issues.

**To GrowthX Business Development:**
- **Webflow Account Health:** Strong engagement signals — Jason is bringing in specialized hires, the team continues weekly syncs, and they're still planning Q1 work through mid-January QBR. No renewal risk signals.
- **Reference Potential:** Use case guides and integration pages are designed to support sales engineering and organic/agentic search, suggesting potential for case study or testimonial leverage.

**To Webflow Product/Developer Experience:**
- **Developer Hub Vision:** Colin and Jason aligned that a cohesive developer hub — integrating blog, code components, and guides into a single destination — is the long-term goal. GrowthX will draft a proposal. Initial scope may need negotiation.
- **Category Refresh Blocker:** 301 redirect implementation is critical to preserve SEO value when reorganizing integration category URLs. Colin will confirm Webflow's API capabilities with Zach before proceeding.

---

## Overview

- **Use Case Guides Paused:** Production is paused to implement feedback, primarily adding JSON examples to show data transformation between Webflow and integrations. This is a pre-publication requirement to make the guides actionable.
- **Integration Page Strategy:** With production nearly complete, the focus shifts to optimization. The initial plan is to analyze SEO performance (using unpacked Search Console data) to prioritize pages for CRO and content improvements.
- **Category Refresh Blocked:** The planned refresh is blocked pending a 301 redirect strategy. This is critical to preserve SEO value from old URLs, which will be lost otherwise.
- **Developer Hub Vision:** GrowthX will draft a vision for a cohesive developer hub, integrating content streams like the blog and code components into a single destination.

---

## Key Topics

### Use Case Guides: Feedback & Strategy

  - **Problem:** Current guides lack the technical detail needed to be actionable for developers.
  - **Solution:** Add JSON examples showing data transformation between an integration's API and Webflow's CMS.
      - **Rationale:** This provides a concrete understanding of the work involved without requiring full code snippets.
  - **Content Scope:** Remove repetitive, generic advice (e.g., testing, rate limits) to make room for more valuable technical content.
  - **Publication Bar:** The new JSON examples are a pre-publication requirement.
      - **Rationale:** The guides must provide confidence in the implementation process to be valuable.
      - **Metrics:** Success will be measured anecdotally (e.g., sales engineering feedback), not by traffic.
  - **Workflow Improvement:** Explore using a RAG system with a single source of truth (e.g., Webflow's `developer.webflow.com` subdomain) to improve AI-generated content quality.

### Integration Pages: Optimization Strategy

  - **Context:** With \~200 pages left to produce, the focus shifts from production to optimization.
  - **Initial Analysis:** A review of top-performing pages (via Search Console) will inform optimization priorities.
      - **Clarification:** The average position metric (e.g., "12" for Google Tag Manager) is misleading. It averages performance across all keywords, including non-branded ones where the page may rank lower.
      - **Action:** Unpack this data to see performance for specific keywords (e.g., "Webflow Google Tag Manager integration" vs. "Google Tag Manager integration").
  - **Optimization Tactics:**
      - CRO best practices
      - Improved positioning
      - More detailed FAQs for search

### Category Refresh: Blocked

  - **Plan:** Reorganize integration categories and update URLs (e.g., `.../integration-type/x` → `.../assets/x`).
  - **Blocker:** The refresh is on hold pending a 301 redirect strategy.
      - **Rationale:** This is critical to preserve SEO value from the old URLs.
  - **Action:** Colin will consult Vivian (SEO) to confirm the redirect process.

### Developer Hub: Vision

  - **Goal:** Create a cohesive developer hub that ties together all developer-focused content streams.
  - **Scope:** This is a broader vision than the initial blog page suggestions.
  - **Action:** GrowthX will draft a proposal outlining this "dream state" vision for review.

### GrowthX Team & QBR

  - **Team Model:** GrowthX is shifting to a project-based model, pulling in specialized experts (e.g., Kathy for dev marketing, Kirk for AI workflows) as needed.
  - **QBR:** The next quarterly business review is planned for mid-January.
  - **Holiday Break:** This meeting is paused for the last two weeks of December.

---

## Action Items

**Jason Gong (GrowthX)**
- Send integration SEO breakdown (branded vs non-branded, comp domains) to Colin
- Draft Developer Hub vision; share w/ Colin
- Verify missing components on Code Components sample site; restore if needed

**Liz Kushnereit (GrowthX)**
- Pause use-case guide production; group Raymond’s feedback by theme (pre-publish vs V2)
- Confirm 301 API for Brand workspace; coordinate w/ Vivian; implement redirects for category refresh

**Zach Plata (Webflow)**
- Confirm 301 API for Brand workspace; coordinate w/ Vivian; implement redirects for category refresh

---

## Transcript
**Liz Kushnereit:** Drop the notes into the chat.

**Liz Kushnereit:** This meeting is being recorded.

**Luke Stahl:** How's everyone's week going?

**Jason Gong:** We're good.

**Jason Gong:** Yeah.

**Jason Gong:** What did we do this week?

**Jason Gong:** A little webinar.

**Jason Gong:** My in-laws are here, so it's been helpful for kids.

**Jason Gong:** How about you?

**Luke Stahl:** Good, good, busy.

**Luke Stahl:** Everything's crammed before holiday break.

**Jason Gong:** Do you guys usually have like the last two weeks people are off?

**Luke Stahl:** I think it's kind of like definitely the last week.

**Luke Stahl:** I think it bleeds into obviously the first week of January, but definitely the last week is off.

**Jason Gong:** So you're still here tomorrow, or sorry, next week, the week after you're gone.

**Jason Gong:** Then January, it depends.

**Jason Gong:** Yeah.

**Jason Gong:** You guys doing anything for the holidays?

**Luke Stahl:** Staying put, which is good.

**Jason Gong:** Same.

**Jason Gong:** I'm, uh, yeah, I think I'm doing the same.

**Jason Gong:** Or we might go to San Diego, just like we're in Oakland.

**Jason Gong:** It's not too far of a drive.

**Jason Gong:** Hey, Raymond.

**Raymond Camden:** Hello.

**Jason Gong:** How's it going?

**Jason Gong:** I saw you join the team recently on the DevRel side.

**Jason Gong:** That was your first weeks at Webflow, Or is it your first weeks?

**Raymond Camden:** It's, uh, about four weeks or so, so first month.

**Jason Gong:** Cool.

**Jason Gong:** I saw your, or Liz showed me your latest blog post on Cursor extension.

**Raymond Camden:** Glad you liked that.

**Raymond Camden:** I think everybody in this room already knew that stuff, but it was all new to me and it was all fun to learn.

**Jason Gong:** I think that storytelling is, like, really good.

**Jason Gong:** I mean, I also run marketing for, like, us, and, like, it's kind of our formula.

**Jason Gong:** It's like, we just, like, we do all this cool stuff for you guys with our other clients, and then we just kind of talk about it in as genuine a way as possible.

**Jason Gong:** You guys know if Colin's joining?

**Jason Gong:** I guess I was waiting for him before kicking things off, but I'm happy to give him another minute or two.

**Jason Gong:** And there he is, speaking of the devil.

**Jason Gong:** Cool.

**Jason Gong:** We got a lot of folks here today.

**Jason Gong:** Raymond, glad you joined.

**Jason Gong:** We do have, like, some stuff to share on the use case guides that you've been reviewing.

**Jason Gong:** So we can have, like, chat about that.

**Jason Gong:** Hey, Colin, how's it going?

**Jason Gong:** Cool.

**Jason Gong:** Okay.

**Jason Gong:** I will get started.

**Jason Gong:** So, today, we're going to go through a few things. We have quite a bit to talk about on the use case guides — there's a lot of feedback and I think we're trying to generalize it and see how we can improve how we write. There are some pieces of feedback that make sense to discuss. For example, we made a decision early on to try not to have code snippets because you've got to update them and pointing to the canonical source seemed easier and more useful. When you flagged that maybe it makes sense to have some kind of simple instructions, that's something we should discuss.

**Jason Gong:** There's a category refresh that Liz has been working on.

**Jason Gong:** And then we have the developer hub, which we don't have anything to share this week, but we're just going to give an update of how we're thinking about it.

**Jason Gong:** And then we're getting a lot of folks, not a lot, but like an increasing number of people like asking about the integration pages.

**Jason Gong:** And we want to put in a process that, you know, you can get people to get feedback and, you know, somebody, whether it's us or you guys, has the ability to go and update.

**Jason Gong:** So that's the day.

**Jason Gong:** I'll start with a work stream update and some things coming up since we're getting close to the end of the year.

**Jason Gong:** In recent weeks, I want to flag some of the stuff outside of normal content work streams — code components, integration pages, getting the use case guides out the door.

**Jason Gong:** And we have some plans for what V2 of the integration pages could look like.

**Jason Gong:** A change that we're going to make coming up, like, as we get into next year is we started hiring a lot more experts.

**Jason Gong:** And we want to go to a model where, like, depending on the project, Liz, who's kind of the constant here, pulls in the right person.

**Jason Gong:** So I've kind of held it down as a journalist, but we hired somebody much more specialized than I am — super deep in developer marketing. Their whole career has been at places like GitHub and Sentry.

**Jason Gong:** We have Kirk, who specializes in AI content workflows. His background is interesting — he used to be an SEO person, and then he saw the writing on the wall with AI and completely retrained himself as an engineer. He's kind of a unicorn that helps us build workflows with good taste.

**Jason Gong:** And then I'm here to support as a growth journalist. How that looks going forward: Liz and I are bringing in Kathy and Kirk on the integration pages and use case guides to move a lot faster with improving workflows.

**Jason Gong:** For code components, if we work on that, it's probably something I'll stay close to.

**Jason Gong:** The last QBR we had was mid-October, so we're roughly planning for sometime in January to review this quarter and think about what to work on next.

**Jason Gong:** And the last thing to note, we typically have these last two weeks as quiet weeks.

**Jason Gong:** We don't have this meeting.

**Jason Gong:** We'll still kind of work on things and update you async.

**Jason Gong:** And depending on the date, like, some of us are still here.

**Colin Lateano:** But before you join, Colin, was talking to Luke, and it seems like that line-slip of vacations.

**Colin Lateano:** you wanted to check in in that time period, I will be home doing nothing, so I can hang out.

**Colin Lateano:** But it's not required at all.

**Colin Lateano:** I want Webflow to be available during that time period.

**Jason Gong:** Okay.

**Jason Gong:** Depending on the combo today and next week, it seems like what we're doing is fairly structured. I'll hand it over to you, Liz.

**Liz Kushnereit:** So for integrations, basically, we're focusing on what that next step is in terms of optimization.

**Liz Kushnereit:** We have, at least in our list, about 200 left, so with 30 a week, we're going to run out very soon.

**Liz Kushnereit:** We're wanting to think what the next steps are, and then I just did a quick little analysis of SEO performance on top-performing pages.

**Liz Kushnereit:** So these would obviously be, like, what we'd want to tackle first, and then move down that list.

**Liz Kushnereit:** And this will also help us inform the category refreshes and, like, what we might want to feature or push up for top-performing traffic.

**Liz Kushnereit:** So it's just, like, a little add-on to the existing performance.

**Liz Kushnereit:** There's a lot of directions we can go with this, and so I made a list of them, and, you know, we can, like, engage with them at varying degrees.

**Liz Kushnereit:** Najam is handling production, but we're simultaneously building the strategy so we can pivot quickly to optimization. CRO practices, improved positioning, detailed FAQs for search. Any thoughts?

**Colin Lateano:** Which ones are on page one, top of fold?

**Colin Lateano:** If we have that top 10 list, then I assume we can get the full list.

**Colin Lateano:** I mean, you don't need to share with me right now, but just generally, it's interesting which ones we are top ranking for and which ones are making a position.

**Colin Lateano:** I'd love to see the competition on all these pages if there was a domain to look into that.

**Jason Gong:** Yeah, we can pull that together. We got this from Search Console. So for example, Google Tag Manager — the interesting thing is we definitely need to unpack it. The reason it says 12 is I'm mostly certain it ranks number one for Webflow Google Tag Manager integration, but because it's ranking for a bunch of other keywords, it's averaging across everything.

**Jason Gong:** Yeah, so I think it makes sense to unpack all of it. You're probably page one for almost all of the Webflow integration ones, and then for non-branded keywords — people just searching "Google Tag Manager integration" — the ranking is probably lower.

**Colin Lateano:** That makes sense. Seeing a Calendly Webflow position of 16 felt odd — I was wondering if that's really something people are searching for. This helps clarify how that number was calculated.

**Liz Kushnereit:** We can build that out in more detail and feed it back into the strategy. This is kind of a new world for us with integration pages.

**Liz Kushnereit:** Use case guides:

**Liz Kushnereit:** For Raymond, I started working on a conversation around what quality and expectations we want for these guides. This document isn't fully ready because I haven't reviewed all your feedback yet, but the first ones have been actioned and are being staged.

**Liz Kushnereit:** I had a question — are all Webflow docs public facing? Accessible on the internet?

**Liz Kushnereit:** Because our research agent builds out assignment details, but we're testing other workflows. With those workflows, having front-loaded thinking with a single source of truth is usually stronger. If we could build that in and move away from the research agent doing that work, we could address validation issues on the output.

**Colin Lateano:** What would the signals or the truth be in these scenarios?

**Liz Kushnereit:** Just one single doc — basically a RAG system. We'd look at that single doc on the integration instead of letting our agent decide what's on the internet. At scale, that could mean downloading those webpages and not allowing for the crawl step.

**Colin Lateano:** Are these integrations typically just one Webflow and one external source? I know the Stripe one involved Cloudflare, and we were looking at membership sites with Cloudflare or Firebase. Are we thinking about RAGing Webflow devdocs, Stripe devdocs, Cloudflare — and seeing how we could put it all together?

**Liz Kushnereit:** We could. It's more of a lift, but the quality would be much higher.

**Jason Gong:** I think we already do that to some degree. I've read through some of Raymond's comments. But I think we almost need to go even deeper. If we limit to Webflow.com, there's still a lot of noise — help docs, forum stuff, universities. They talk about roughly the same topic but aren't in sync, and the AI has trouble figuring out the best approach.

**Colin Lateano:** The dream state would be pulling from the developer's subdomain. A lot of Webflow content is for no-code, but for code implementations — which is what we're going for in these examples — I'd hope our dev docs are sufficient to guide an AI through best practice implementation. I don't know if that's true for the external party we'd want to cover.

**Jason Gong:** I think the answer depends on what the other integration is. But to reiterate what Liz said — we got a bunch of comments from Raymond. We're trying to generalize them into themes so we can tackle all of them at once. Right now we're addressing them one by one, which works but slows things down and makes it cumbersome for Raymond because he has to keep reviewing. We're trying to generalize and solve this at scale so you don't have to keep reviewing.

**Liz Kushnereit:** Raymond, do you have any feedback for us right now or priorities you'd like us to focus on?

**Raymond Camden:** When I first looked at these, I went in expecting a technical blog post, which maybe wasn't the intended audience. I expected more code, but I don't think we need to turn them into full technical blog posts — that would expand the work needed to build proof of concepts significantly.

**Raymond Camden:** What I think would help: since you're using this third-party X with data in this shape, and Webflow has data in this shape — show the transformation. Here's SoundCloud's JSON data, here's what Webflow expects, here's how you'd transform it to sync. It doesn't have to be real code — just show me the shape of the data so I understand the work involved.

**Jason Gong:** That was exactly the level we were aiming at — if you read this, you'd have a good idea of how much work it would take and what you'd need to do, but you wouldn't be able to just follow it and get it done.

**Colin Lateano:** That was the intention. The integration hub shows what's possible for inspiration. These guides are pseudo-code examples of here's what you can do and here's how. Ray's feedback is that pseudo-code showing the data shape would help people understand the approach they'd need to take. Not producing a whole app — that's something else we've discussed.

**Jason Gong:** That makes sense. The data shape pattern is super useful — the shape from the integration doesn't match Webflow's shape. We should split that out separately and make sure we do it right across all of these.

**Raymond Camden:** One more thing I'd mention that I didn't include in my comments: every single integration guide talks about rate limits, testing, and good housekeeping. It's like "brush your teeth every day" — good advice, but it gets repetitive and it's expected in any technical article. I'd suggest not worrying about that as much. If you're asking me to add more content, removing that generic stuff could make room for the valuable technical details.

**Jason Gong:** The way you framed that feedback is extremely helpful. If you have things like that, send them our way — super easy to address quickly.

**Jason Gong:** On our side, we have a workflow generating the format you're seeing. For integration pages, the model is: you say it's good enough, not perfect, but let's get it out the door and learn. That's working extremely well. Now we have signals where Liz prioritizes pages for more effort — add screenshots, improve positioning, etc.

**Jason Gong:** For use case guides, I'm not sure what the publication bar is. Is the data-shape section required before publishing so we get signal, or do we need to get it right first?

**Colin Lateano:** If the core goal is to provide value for both agentic searches and organic people — people who read and think "oh, I want to do that, how would I?" — then it should give them confidence in how they'd approach implementation. If Ray says he wants to understand the shape of how he'd approach the integration, that's the floor. I'm open to experimentation from there.

**Colin Lateano:** I'm not expecting massive traffic. The question is: does this help our sales engineering team? Does it get agentic search traffic? I don't know what metrics we'll track yet, but anecdotal feedback for the next couple of months as we launch.

**Jason Gong:** The ask for you, Raymond: when you give feedback or generalize themes, specify whether it's V2 (can add later) or pre-publication (needs to be right before we publish).

**Raymond Camden:** Right now the content is good for people new to Webflow. Seeing "you can integrate with SoundCloud" sparks interest. But the docs you're talking about are supposed to be one step deeper — beyond just what's possible, showing something you could actually do.

**Raymond Camden:** Then I think it needs a bit more work before it goes live.

**Colin Lateano:** We're very close though, Jason.

**Liz Kushnereit:** The next step is clear — these high-level expectations are pretty clear. We'll take this back to the content engine, pause production, and focus on getting the baseline correct before moving forward. We may need to work with engineering since the needs here are different than integration pages.

**Jason Gong:** If we could group Raymond's comments into themes, that would help visually. Some things might be heavier lifts for V2. That way I can get aligned with Colin faster.

**Liz Kushnereit:** Yep, we can do that. We'll group them by theme and calibrate simultaneously.

**Liz Kushnereit:** Quick category refresh update: we're ready to proceed. We've built out a 301 redirect plan and have CMS access.

**Colin Lateano:** I'm comfortable moving forward. Luke, just want to flag: we're reorganizing categories and changing URLs from `.../integration-type/x` to `.../assets/x`. We'll have some category page changes. I want to confirm we can 301 those with Michael and Vivian so we don't drop SEO value.

**Luke Stahl:** There should be a redirect for any URL changes we create.

**Colin Lateano:** Vivian would be the person to help execute the 301 plan. Zach, does Webflow have API flexibility for 301 redirects on owned sites?

**Zach Plata:** There's an API for it. Drop the workspace slug in chat and I'll confirm.

**Colin Lateano:** It's the Brand workspace. Let's give us a couple days to figure out the 301 plan, but I'm okay with the categories as proposed.

**Liz Kushnereit:** Update intake process is still on my plate. We'll set that up as we move into content updates and optimization. Open to ideas.

**Liz Kushnereit:** Developer Hub — I'll hand this to Jason since he's excited about it.

**Jason Gong:** We need a bit of time on the developer hub. Our first version was just suggestions for the developer blog page, but I want to tie it all together — where code components could live, how all the content streams could look more cohesive. Is that aligned with your thinking, Colin?

**Colin Lateano:** I was scoping it down to be achievable, but I'm open to seeing the dream state first and then figure out what we can junk or work with other teams on. Show me what you're thinking.

**Jason Gong:** We'll work on that over the next week or two.

**Liz Kushnereit:** That's about all we have. Our asks are clear. Anything else?

**Colin Lateano:** Some components disappeared on the Code Components sample site. Can you check that?

**Jason Gong:** I'll check that right after. I think I fixed it, but I'll double-check.

**Jason Gong:** Thanks, everyone!
