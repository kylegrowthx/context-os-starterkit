# You.com <> GrowthX - Weekly Sync

<metadata>
date: 2025-11-05
time: 17:01 UTC
duration: 30 minutes
organizer: team@growthxlabs.com
participants: Aida Knezevic, Erik O'Brien, Ben Geller, Brooke Grief, Keya Gupta, Kady Srinivasan, Seher Dholakia, Alper Tekin, Justin Fink
fathom_recording_id: 99419338
fathom_url: https://fathom.video/calls/462832541
share_url: https://fathom.video/share/QjseyRrExTXy3xhgkbuhS1SY6a_oJ7Px
source: fathom
enriched_on: 2026-03-02 09:15 UTC
</metadata>

---

## Summary

Review content calibration and address SEO performance issues.

---

## Context

This is a weekly status sync between GrowthX (a content marketing agency) and You.com (a search and API platform company). Aida Knezevic leads content strategy and production for You.com at GrowthX, working closely with Brooke Grief (You.com's Head of Content Marketing) and Seher Dholakia (You.com's internal content team). The meeting focused on finalizing content calibration, addressing post-migration SEO issues, and launching the AI visibility tracking infrastructure via the Scrunch dashboard.

---

## Relevance

**To GrowthX Delivery:**
- Established human, conversational voice standard for You.com content, unblocking production pipeline
- Defined competitor strategy: direct comparisons permitted only in "vs." articles; best-of lists position You.com as top choice, competitors as niche alternatives
- Improving content production pipeline with agentic workflows and advanced fact-checking to reduce accuracy issues
- Webflow CMS access confirmed; featured image generation pipeline in development with brand asset integration

**To CheckThat:**
- Scrunch AI visibility dashboard live with 2% citation rate baseline (vs. 3% competitor average)
- Tracking 35+ base prompts across Claude, Gemini, ChatGPT; potential to expand to thousands of prompts
- LLM referral traffic measurement framework established via Looker dashboard integration with GA4 and GSC
- Data showing LLM citations drive significant traffic to blog posts, contradicting earlier industry predictions about blog obsolescence

**To GrowthX Business Development:**
- Account production timeline secured: 3 drafts week of Nov 10, 5 drafts week of Nov 17, calibration finalized next week
- Post-migration SEO audit required to resolve technical issue (2 ranking pages in SEMrush vs. 25 in GSC) from Oct 14 Webflow migration and redirect gap
- Looker dashboard reports being built for You.com internal use beyond content performance tracking
- Executive team presentation of full content strategy planned for next week, potential for strategy refinement feedback

---

## Overview

- **Content Calibration Finalized:** The "calibration blog" review set the voice (human, conversational) and competitor strategy (direct comparisons only), unblocking content production.
- **SEO Performance Issue Identified:** A post-migration (Oct 14) SEMrush data discrepancy (only 2 ranking blog pages vs. 25 in GSC) was traced to a 2–3 week redirect gap; GrowthX will perform a technical SEO audit to diagnose.
- **AI Visibility Tracking Launched:** The Scrunch dashboard is live, showing You.com's 2% citation rate (vs. 3% for competitors) and providing data to inform future topic selection.
- **Production Timeline Set:** After final calibration, GrowthX will deliver drafts for 3 articles next week, followed by 5 the week after.

---

## Key Topics

### SEO Performance & Technical Audit

  - **Problem:** A SEMrush data discrepancy shows only 2 ranking blog pages, while Google Search Console (GSC) shows 25.
  - **Root Cause:** The issue is linked to the blog's migration from HubSpot to Webflow on Oct 14, which created a 2–3 week redirect gap.
  - **Impact:** The redirect gap caused a significant drop in keyword rankings (especially top-10 positions) that coincided with a July Google Core update.
  - **Solution:** GrowthX will conduct a technical SEO audit to diagnose the issue and create a plan to recover lost rankings.

### Content Calibration & Strategy

  - **Voice & Tone:** The "calibration blog" review established a human, conversational voice.
  - **Competitor Strategy:**
      - **Direct Comparisons:** Permitted for "vs." articles (e.g., You.com vs. X).
      - **"Best of" Lists:** Position You.com as the "best overall" and competitors as niche alternatives.
      - **Rationale:** This strategy captures traffic, secures LLM citations, and proactively counters competitor messaging.
  - **Content Enhancements:**
      - **Customer Examples:** Add Rack and InSurf as API customer examples.
      - **Hackathon Tie-in:** Reference the winning hackathon project, which used the Search API.
      - **Internal Linking:** Add internal links to older content to help regain lost SEO authority.

### AI Visibility Tracking (Scrunch)

  - **Purpose:** The Scrunch dashboard measures You.com's visibility in LLM responses against competitors.
  - **Current Metrics:**
      - **Citation Rate:** 2% (vs. 3% for competitors).
      - **Position:** Ranks \#1 in responses 50% of the time.
  - **Data Usage:** The data will inform topic selection, identifying high-performing areas to support and low-visibility areas to target.
  - **Looker Dashboard:** A 7-page Looker dashboard is in development to track content performance, including a page dedicated to LLM referral traffic.

---

## Action Items

**Aida Knezevic (GrowthX)**
- Revise calibration blog per Brooke’s edits; send to Brooke for review
- Upload 3 Webflow drafts (week of Nov 10); notify Brooke to publish
- Upload 5 Webflow drafts (week of Nov 17); notify Brooke to publish
- Share AI-generated featured image examples in Slack to Brooke
- Send weekly Scrunch PDF reports to Brooke + Seher
- Send Scrunch prompt list to Brooke + Seher

**Erik O’Brien (GrowthX)**
- Add technical SEO audit to Talal’s to-do; share findings w/ Brooke

**Brooke Grief (You.com)**
- Analyze top-3 ranking drops (Jul 2025); recommend content refresh to Aida

---

## Transcript
**Aida Knezevic:** This meeting is being recorded.

**Brooke Grief:** Hi.

**Brooke Grief:** Sorry, I joined like four wrong Zooms before I found the right link, but I'm here.

**Brooke Grief:** How's everyone doing?

**Aida Knezevic:** Good.

**Aida Knezevic:** How are you?

**Brooke Grief:** Good.

**Brooke Grief:** Good.

**Brooke Grief:** I just ran through that blog.

**Brooke Grief:** That's very exciting.

**Aida Knezevic:** What do you think?

**Brooke Grief:** I thought it was great.

**Brooke Grief:** I thought it was awesome.

**Brooke Grief:** I am curious, like, I saw all the stuff at the top, which is awesome, like meta description, URL, excellent.

**Brooke Grief:** I added the keyword in just so that I remember.

**Brooke Grief:** And then, like, if we have a sense of audience when we're doing these, it would be great to know just who we're targeting so that we keep them in mind.

**Brooke Grief:** But overall, I left some suggested edits in there, just ways to kind of make it sound more human.

**Brooke Grief:** No one will be shocked if we use AI to write content as an AI company, but I always like to add a little more touching touch in there.

**Brooke Grief:** But let me know what you think of the suggestions.

**Aida Knezevic:** We can work in the doc if that works for you, or we can run through it, whatever you have planned for today.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Cool.

**Aida Knezevic:** I think we can go through your comments really quickly.

**Aida Knezevic:** Let me just share my screen.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Yeah, can definitely add the, like, the audience here.

**Aida Knezevic:** That's actually something that we typically do, but it slipped my mind when I was delivering this.

**Aida Knezevic:** Okay, what is Rack?

**Aida Knezevic:** Sorry, I have to remove our faces so that I can see your comment.

**Brooke Grief:** Okay.

**Aida Knezevic:** Okay, so you don't, you're not sure if you can use this?

**Brooke Grief:** Yeah, I know we can use their logo, but I just have to confirm that we can actually speak to what they use us for specifically.

**Brooke Grief:** We can, but it's currently on the website too.

**Aida Knezevic:** Sweet.

**Brooke Grief:** Yeah.

**Brooke Grief:** So ignore me, we can use this.

**Aida Knezevic:** Okay, okay, cool.

**Aida Knezevic:** Yeah, it was, I was looking at the customer success stories on the site and all of them were for, like, the enterprise AI solution.

**Brooke Grief:** And this was the one that was mentioned on the API search page.

**Brooke Grief:** Okay, so yeah.

**Aida Knezevic:** I'll get in.

**Seher Dholakia:** If we need another, I think we could also use win.

**Seher Dholakia:** InSurf here, they're like another API customer that we could leverage.

**Brooke Grief:** Cool.

**Aida Knezevic:** Yeah, okay, that makes sense.

**Aida Knezevic:** Like this is, yeah, we can make this like more conversational.

**Aida Knezevic:** Yeah, I do agree.

**Aida Knezevic:** Like we try to like strike a balance between like writing an active voice and kind of chunking information and then like actually like using transitions.

**Aida Knezevic:** So I do like gravitate more towards like the more human writing, but I did want to like provide you with like a different option.

**Aida Knezevic:** So I think we could just like, yeah, make this like more conversational and just connect the dots for the readers.

**Brooke Grief:** I think that would be make this section better.

**Brooke Grief:** Totally, same for like that, the intro, I usually do like at least a couple sentences just to make it look a little more structured.

**Aida Knezevic:** But yeah.

**Aida Knezevic:** Yeah, yeah, that makes sense.

**Aida Knezevic:** Okay, this is, like, it's important that we get, like, also, like, it's not just the calibration blog, it's not just for, like, the voice and the writing style, but it's also, like, to get the information right.

**Aida Knezevic:** So we do have a fact checker in our workflow.

**Aida Knezevic:** But if, you know, there's anything that's inaccurate, like, just flag it to us.

**Aida Knezevic:** We are working on improving the article generation pipeline.

**Aida Knezevic:** So we are, like, transitioning to an agentic pipeline, which has a, like, a more advanced fact checker that can actually, like, it generates a research document, and then it goes back in and, like, does additional rounds of, like, verification on the data so that it, and it ranks the data it collected.

**Aida Knezevic:** So it's, like, grades it on, like, a scale of one to five based on the accuracy and the relevance.

**Brooke Grief:** So, if there's anything here that you think is, like, maybe outdated or is just, like, missing context, you can flag it for us.

**Aida Knezevic:** Index.

**Aida Knezevic:** Feels like using the word in the definition.

**Aida Knezevic:** Oh, yeah, yeah.

**Brooke Grief:** Yeah, so it's, like, a different word for it or a clarify.

**Aida Knezevic:** Synonym, yeah.

**Brooke Grief:** I like the metaphor, similes.

**Brooke Grief:** It helps me at least understand this stuff better, so I'm assuming it would help.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Okay, yeah, that's great.

**Aida Knezevic:** I think we had, like, an earlier version of the writing guidelines that we were using this summer had, like, a whole section on metaphors and similes, and then, yeah, it kind of went overboard, and it was just using them in every other paragraph, so we had to cut them down significantly.

**Aida Knezevic:** So, they do appear from time to time, but we really had to kind of tone it down, because it was too much.

**Aida Knezevic:** And then, okay, lightweight example.

**Aida Knezevic:** Okay, we can provide an example here.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Oh, you don't want to mention competitors?

**Brooke Grief:** Okay.

**Brooke Grief:** Yeah, I would stay, unless it's, like, a direct eval of, like, how we're better, I would just stay away from Toss, and then that section about you.com is also in the conclusion, so.

**Aida Knezevic:** Okay, okay, that works.

**Aida Knezevic:** I think maybe we can see what else, like, maybe we can actually expand the you.com section.

**Aida Knezevic:** So, like, we have a conclusion that's, like, start building, it's, like, brief, we can, like, shorten it further to avoid repetition, but then we can turn this section into one that talks more about you.com's API and how it works.

**Aida Knezevic:** I think that would be, like, more valuable, and it, you know, provides, like, more information about the product, so.

**Brooke Grief:** Yeah, something we could do, too, that just happened is our hackathon ended.

**Brooke Grief:** Okay.

**Brooke Grief:** And our, the winner of the hackathon used our search API, so that could be something that just gets plugged.

**Aida Knezevic:** In here.

**Brooke Grief:** There's a blog post that was just published yesterday on the winning hack.

**Brooke Grief:** So that'd be a nice tie in.

**Brooke Grief:** But from like a length perspective, I think even if we cut that whole section out and didn't add anything in, I think it's still long enough.

**Aida Knezevic:** Like it's around 1000 words still, which is pretty good.

**Brooke Grief:** So I wouldn't like if we're just trying to fill to get length that I wouldn't worry about it too much.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Okay.

**Aida Knezevic:** I did see when it comes to just like general topic selection for the blog, there were some articles that we suggested that do mention your competitors explicitly.

**Aida Knezevic:** What are your thoughts on that?

**Brooke Grief:** If it's a direct like versus of like how we stack up, that's totally fine.

**Brooke Grief:** We love to do those.

**Brooke Grief:** If it's like a list of tools and we're one of many and the competitors are also on the list, I would stay away from that just because we want to be like the best.

**Aida Knezevic:** And the only choice and the top choice and all of that.

**Brooke Grief:** And yeah, so that's sort of how I would think about it.

**Brooke Grief:** But if there is a certain case where you think it would make more sense to list out competitors, let me know.

**Brooke Grief:** Obviously, we can examine on a case by case.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Yeah, I think what we can do in those types of like best of listicles, we can, we like to like, we can categorize them.

**Aida Knezevic:** So we could say like, best overall is you.com.

**Aida Knezevic:** And then we can mention other competitors and be like, okay, they work for this and this use case.

**Aida Knezevic:** But we don't have to, mean, typically, when we do publish them, the competitor sections are more, they're just, you know, shorter, you kind of, cover like the basic features and the functionalities.

**Aida Knezevic:** But we try to kind of not really talk about their advantages or really disadvantages because that can be a little bit tricky.

**Aida Knezevic:** Like depending on, um.

**Aida Knezevic:** You know, the company and if they really like, I've written content for companies that never wanted to mention any of their competitors cons because they were afraid of their legal departments.

**Aida Knezevic:** So that's just something to keep in mind.

**Aida Knezevic:** But I think for the best of listicles, I think that is kind of the structure that we take.

**Aida Knezevic:** And I do like to incorporate those types of articles in the content strategy, just because they do get traffic, they do get cited by LLMs, and your competitors are probably going to be publishing them as well.

**Aida Knezevic:** So you might as well be on the SERP.

**Brooke Grief:** And as they like come through, we can always look at them, you know, in draft form and see what we think.

**Brooke Grief:** And so keep in mind, too, is we will have, at some point, I know, Seher, we're working on the evals page, but we'll have a page that has updated numbers on how we compare to our competitors.

**Aida Knezevic:** And we can use that as a basis for a lot of these listicles.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** No, that's great.

**Aida Knezevic:** I love those.

**Aida Knezevic:** I mean, you know, the more resources you have on your site that we can point people to, the better.

**Aida Knezevic:** I know you already have like these versus articles on your site, which is great.

**Aida Knezevic:** But, you know, the more they show up, the better.

**Aida Knezevic:** We did an article for Lovable, published a lot of articles for Lovable recently for where we were just comparing them against their top competitors.

**Aida Knezevic:** And they're already being cited by ChatGPT.

**Aida Knezevic:** Like we just found like when we were doing research for a different article, it was cited and it was published like last week or two weeks ago.

**Aida Knezevic:** So the time to like visibility is very short.

**Aida Knezevic:** So yeah, that's kind of something that I did want to like, I think for a lot of these like verses, and I'm glad that you are publishing that type of content, because I do run into companies that just don't want to do it for whatever reason.

**Aida Knezevic:** And it is very valuable, in my opinion, at least for.

**Brooke Grief:** AI visibility.

**Brooke Grief:** Totally.

**Brooke Grief:** I know.

**Brooke Grief:** think we're in the ask for forgiveness mindset.

**Aida Knezevic:** Yeah, yeah, totally.

**Aida Knezevic:** And I mean, we had clients.

**Aida Knezevic:** There was one client where their competitor published like a blog post where they flat out said that our client was not an enterprise solution.

**Aida Knezevic:** And they put all this information out there that they're not suitable for enterprises.

**Aida Knezevic:** They don't work.

**Aida Knezevic:** And it was being picked up by all of these LLMs and like AI overviews.

**Aida Knezevic:** And they were kind of like in a panic, like, okay, what are we going to do about it?

**Aida Knezevic:** So like there are companies that really do use these types of blogs for just kind of like they're not very, not very fair.

**Aida Knezevic:** So you do want to get that messaging out there.

**Brooke Grief:** Totally.

**Brooke Grief:** That's a good point.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Okay, great.

**Aida Knezevic:** Did you have any other, I know you left some comments on the other topics in the content calendar.

**Aida Knezevic:** I did respond to them.

**Aida Knezevic:** But.

**Aida Knezevic:** We do have, like, I think a good batch approved to get us started.

**Aida Knezevic:** So our next step from here would be we're going to, like, incorporate your feedback in the calibration, send it to you for another review.

**Aida Knezevic:** And then next week we would do three blog posts and the following we would do five.

**Aida Knezevic:** As soon as we finalize the calibration, we can, like, stage it on, I mean, draft it in your CMS and you can publish it or we can publish it.

**Aida Knezevic:** But typically, like, I think people like to take a look at the blog first to make sure that everything's, like, set properly before we publish.

**Aida Knezevic:** So that's what we can do as well.

**Brooke Grief:** Okay.

**Brooke Grief:** Yeah, I think that works.

**Brooke Grief:** Because if you all are okay uploading it, I can be the one that hits the publish.

**Brooke Grief:** So it's on our calendar for the right day.

**Brooke Grief:** But, yeah, that would be great.

**Brooke Grief:** And you have access to everything that you need.

**Brooke Grief:** How is that going?

**Brooke Grief:** is

**Aida Knezevic:** Erik, I do believe we have access to the CMS.

**Brooke Grief:** remember webflow, yeah.

**Brooke Grief:** Yeah.

**Brooke Grief:** Okay, cool.

**Aida Knezevic:** For the featured images, that is something that we can also build a pipeline for.

**Aida Knezevic:** So I can actually show you a couple of examples.

**Aida Knezevic:** I do see right now you're using, like, stock images with, like, an overlay.

**Brooke Grief:** Yep, that's me doing that, so.

**Aida Knezevic:** Okay, okay, yeah, yeah, okay.

**Brooke Grief:** I'm playing around, so there's no, we don't really have a hard and fast brand book yet.

**Brooke Grief:** The designers are working on it, but I think if it's close enough, it should be okay, and we can always swap it out later.

**Aida Knezevic:** Okay, yeah, I mean, I can, if you have any, I mean, the visual design assets, I think you did share them, and I sent them over to Katya, and she's...

**Aida Knezevic:** Going to work on them, so we can present you a couple of examples, but I did want to show you examples for another client, and this is just so you can kind of, you have a better idea of what the AI can do.

**Aida Knezevic:** So this is, like, they are, like, an app development platform, and this is, like, all in their brand colors, so it's, like, following, like, the colors that they're using, the fonts, and there are multiple options.

**Aida Knezevic:** So for each article we generate, this step comes at the end, and it uses the context from the article and the prompts that are uploaded by our designer to generate these images.

**Aida Knezevic:** So, like, you can see, like, there's code here, so we can, like, put, like, as soon as we have examples from Katya, I'm going to send them over on Slack so you can take a look.

**Aida Knezevic:** Yeah, so we can, like, publish with images that we generate.

**Brooke Grief:** Cool.

**Brooke Grief:** That sounds great.

**Brooke Grief:** And then all of this, I'm assuming, like, will live, the draft, the images, all of that will live in Airtable under each individual.

**Aida Knezevic:** Yeah, we're going to be tracking everything in Airtable.

**Aida Knezevic:** And then we're also setting up your Looker dashboard.

**Aida Knezevic:** So we do, I think we do have access to your GA4 and GSC account.

**Aida Knezevic:** And then we're going to connect that to a Looker dashboard.

**Aida Knezevic:** So it's like a seven-page report.

**Aida Knezevic:** And we're going to be using that to track, like, to track the performance of the content that we publish.

**Aida Knezevic:** But there are also many pages that are just cover, like, your whole website that you can just use, like, internally.

**Aida Knezevic:** And there's also one page in that report that just focuses on LLM referral traffic.

**Aida Knezevic:** So you can see which LLMs are driving the most traffic to your site, which pages are getting the most clicks from LLMs.

**Aida Knezevic:** And then we combined that data with data from Scrunch, which is like an AI visibility tool.

**Aida Knezevic:** And then you can actually kind of see your competitor's visibility as well.

**Brooke Grief:** It's very exciting.

**Brooke Grief:** And then do you all, do you use SEMrush?

**Brooke Grief:** Is that right?

**Aida Knezevic:** Yes, we do use SEMrush.

**Brooke Grief:** Okay.

**Brooke Grief:** I've been having some weird issues with our SEMrush.

**Brooke Grief:** I'm curious if you are seeing the same.

**Aida Knezevic:** What?

**Brooke Grief:** So for our keywords, when I look at all of our organic search rankings, we only have two pages that are resources that are ranking, which I've never seen before.

**Brooke Grief:** So I'm curious if it's just something that we need to fix on our end or if it's just our content, but I'm hoping it's not our content, but I'm not sure.

**Brooke Grief:** So I'm just curious if you all have seen that or if you do see it for our content.

**Aida Knezevic:** I can check with our team that works.

**Aida Knezevic:** With clients, like, on an ongoing basis that do, like, long-term performance monitoring, I do remember, and this was maybe a month ago, maybe two months ago, that Google changed the way they, yeah, track, like, pages.

**Aida Knezevic:** So they removed, like, individual pages from their index, which made it difficult for SEMrush and Ahrefs to track where the blogs are showing up.

**Aida Knezevic:** But that does sound weird.

**Aida Knezevic:** Actually, let me take a look right now and see what shows up.

**Brooke Grief:** So is it just the resource page on your site?

**Brooke Grief:** Yeah.

**Brooke Grief:** Our whole site does rank.

**Brooke Grief:** I think we have, like, 4,000 non-branded.

**Aida Knezevic:** Okay, yeah.

**Brooke Grief:** But a lot of the pages aren't, the inside pages aren't necessarily showing up on those, as well as our resources, so.

**Aida Knezevic:** Mm-hmm.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Yeah, so it's only ranking for two keywords.

**Aida Knezevic:** And, like, historically, there just hasn't been a lot of.

**Brooke Grief:** Which is just strange, and I don't know if it's just a SEMrush thing.

**Brooke Grief:** Google Search Console shows, like, 25.

**Brooke Grief:** Mm-hmm.

**Brooke Grief:** Maybe it's better.

**Aida Knezevic:** Erik, can you, I think this is, like, a technical SEO task for Talal's to-do list.

**Erik O'Brien:** Okay.

**Aida Knezevic:** We have someone right now in-house that does, like, technical SEO audits, so he can take a look and see, like, what's happening, because this isn't normal.

**Brooke Grief:** Like, this should be.

**Brooke Grief:** That's what I thought, too.

**Aida Knezevic:** I was like, what?

**Aida Knezevic:** Yeah, yeah, because your authority score is 56.

**Aida Knezevic:** So anything that you publish should rank very well, like, right off the bat.

**Brooke Grief:** Yeah.

**Aida Knezevic:** Unless you have issues on your site that are preventing, like, pages from being indexed.

**Aida Knezevic:** So, actually, let me take a look at the content OS because when I was, when I was doing your, when I was just developing your content strategy, we also do, like, a keyword analysis of, like, the keywords that you rank for already.

**Aida Knezevic:** And this was, like, three weeks ago.

**Aida Knezevic:** So maybe things were different back then.

**Brooke Grief:** Yeah.

**Brooke Grief:** So, Hair, what was, like, the actual hard date that we switched over to Webflow?

**Seher Dholakia:** For the blog, specifically?

**Brooke Grief:** Yeah.

**Brooke Grief:** I mean, the whole site, but then also the blog?

**Seher Dholakia:** The first migration was done on August 6th, but that was only, like, five pages.

**Seher Dholakia:** And that was, like, the first time we had brought pages over to Webflow.

**Seher Dholakia:** And then the second way, like, the second one.

**Seher Dholakia:** And where the blog was included was, I believe, October 14th.

**Aida Knezevic:** Okay.

**Aida Knezevic:** So it looks like all of the resources used to be under articles.

**Seher Dholakia:** Yes.

**Seher Dholakia:** And they've moved over to, like, slash resources.

**Brooke Grief:** Yep.

**Brooke Grief:** And we just set up redirects.

**Brooke Grief:** Yes.

**Brooke Grief:** So I'm hoping that that fixes some of this.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Here it is.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** So the keyword, like, this article subfolder.

**Aida Knezevic:** You can see all the keywords that are used to rank for.

**Aida Knezevic:** And it's still ranking.

**Brooke Grief:** For articles, though.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Yeah.

**Brooke Grief:** Yeah.

**Brooke Grief:** For articles.

**Brooke Grief:** For all pages are still ranking.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** So how long were the redirects not set up?

**Brooke Grief:** Like, probably two weeks.

**Brooke Grief:** three weeks?

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Well, it's good that they're set up.

**Seher Dholakia:** Yeah.

**Seher Dholakia:** Ida, over time, will we re-

**Seher Dholakia:** What we once had from the old links, like, will that happen?

**Seher Dholakia:** Or what else do we need to do on our side to kind of maintain?

**Aida Knezevic:** Yeah.

**Aida Knezevic:** So I think the thing is that this was in, when did the migration take place?

**Seher Dholakia:** August?

**Seher Dholakia:** the interesting part is, is it looks like it went down from July to August, but the blog actually remained in HubSpot up until October.

**Aida Knezevic:** Okay, so this is the Google Core update then.

**Brooke Grief:** Yeah.

**Aida Knezevic:** Okay.

**Aida Knezevic:** I think it's not going to be, since the redirect is there, any, like, it's, these, like, articles are going to be ranked.

**Aida Knezevic:** I think just adding internal links to the previous content is going to help.

**Aida Knezevic:** So that's going to be helpful.

**Aida Knezevic:** But to, like, regain these rankings, we do have to, like, do an analysis and see what we should refresh, particularly, like, the...

**Aida Knezevic:** Ones that dropped from the top three in July, 2025, because, yeah, I mean, it's not that bad, but you did lose a lot of, like, keywords in the top 10.

**Brooke Grief:** bottom, yeah, and, like, the the bottom dropped out of that funnel, which, yeah, yeah, I think I can look into this, but I think Talal can also do, like, a more technical SEO audit, just because of the migration, and there are always things that come up in a migration that affect technical SEO.

**Brooke Grief:** So, yeah, cool, that would be awesome.

**Aida Knezevic:** Great, all right, and then, did I show you your Scrunch dashboard?

**Aida Knezevic:** I don't think I did.

**Brooke Grief:** Not today, no.

**Aida Knezevic:** No, okay, yeah, so we do have this set up for you, and this is something that is accessible just to GrowthX email, but I can share PDF versions of the report with you on a weekly basis, so you'll have access to the data.

**Aida Knezevic:** So, Scrunch is very similar to tools like Profound, and it basically, how it works.

**Aida Knezevic:** We give it a description of your company, we give it a description of your target audience, and then we provide a list of the top competitors, and then it will automatically generate 35 base prompts to track.

**Aida Knezevic:** And then each of those base prompts gets adapted to different LLMs, like Claude, Gemini, ChatGPT, and then it sends those prompts to those LLMs, collects the responses, analyzes them, and then breaks down your visibility.

**Aida Knezevic:** However, we can upload many more prompts here, I've seen, like, accounts that are tracking thousands of prompts, so we can use AI to generate additional prompts that we think your audience would be using when, you know, in different LLMs, or you can provide us, like, a list of questions that come up pretty frequently from your customers.

**Aida Knezevic:** I mean, we did talk about this, Brooke, I think, last time you did say that...

**Aida Knezevic:** Sometimes there's, you know, they're not aware that your customers might not be aware that they might need this type of, what do you say, like this type of solution.

**Aida Knezevic:** They have like a very specific problem, but they don't know that the solution exists.

**Aida Knezevic:** But for example, for the Search API product, we could definitely like use those prompts.

**Aida Knezevic:** So, yeah, it breaks down your competitive presence overall.

**Aida Knezevic:** So, like compared to the competitors that we have uploaded, we can also add additional ones as needed.

**Aida Knezevic:** Your citations are around 2%.

**Aida Knezevic:** This is fairly standard.

**Aida Knezevic:** The average citation rate is around 5%.

**Aida Knezevic:** Companies with really huge content repositories, like thousands of blog posts, they might see citation rates of around 10%.

**Aida Knezevic:** But yeah, this is like fairly, fairly standard.

**Aida Knezevic:** Your competitors are at around 3%.

**Aida Knezevic:** So, it's pretty normal.

**Aida Knezevic:** we're if

**Aida Knezevic:** And then it also ranks your overall position in the responses that the LLMs generate.

**Aida Knezevic:** And then for the specific prompts.

**Aida Knezevic:** Okay.

**Aida Knezevic:** So the prompts are automatically grouped into topics.

**Aida Knezevic:** And then we can also kind of see how individual topics are performing.

**Aida Knezevic:** And if we go, for example, to like this one, we can actually see the seed prompts.

**Aida Knezevic:** And then when we click on the prompt, we can see, okay, like what is the LLM specific data that we're seeing?

**Aida Knezevic:** So like there are many responses where you don't have a presence, but also your competitors also didn't show up.

**Brooke Grief:** So are these.

**Brooke Grief:** are these.

**Brooke Grief:** these.

**Brooke Grief:** Prompts, were these taken into account in those initial topic suggestions, or is that how these are being used?

**Aida Knezevic:** So these are more, so this is more for optimizing the topic selection.

**Aida Knezevic:** So once we do like upload more prompts here, we have enough data, we can actually see, okay, if you're doing really well in a specific topic, and you start like dropping, your visibility starts to drop, then we can see how we can support that topic with more content.

**Aida Knezevic:** Or if there's a specific topic where your AI visibility is like really, really low, we can use that to inform topic selection.

**Aida Knezevic:** The initial clusters were really informed by like a content gap analysis, and then analyzing, okay, what are your goals?

**Aida Knezevic:** Like, who are you trying to serve?

**Aida Knezevic:** And then we also analyze like your audience's pain points to try to map the content to those pain points.

**Aida Knezevic:** That really, like, naturally kind of impacts AI visibility as well.

**Brooke Grief:** Got it.

**Brooke Grief:** And then is there a way to see which of our pages are showing up as answers or no?

**Aida Knezevic:** They don't report on that yet.

**Aida Knezevic:** Unfortunately, no.

**Aida Knezevic:** No, they don't provide that data.

**Aida Knezevic:** You can see, I mean, that's where the Looker dashboard is helpful because you can use it to actually see, okay, these are the blogs or these are the web pages that are getting the most traffic from LLMs.

**Aida Knezevic:** From what I've seen so far, just from other clients, a surprising number of blog posts get a lot of traffic from LLMs.

**Aida Knezevic:** So it's not just, I think a couple of months ago, there was a lot of talk, especially on LinkedIn.

**Aida Knezevic:** If you follow, like, the content marketing conversations, everybody was saying, like, blogs are going to die because, you know, everybody can find answers on ChatGPT.

**Aida Knezevic:** But what I'm seeing is that, like, the vast majority of LLM referral traffic for a lot of our clients goes directly to blog posts.

**Aida Knezevic:** Because people do, like, click on the citations to actually find out more about a specific topic.

**Aida Knezevic:** So it's not as grim as people thought it would be.

**Brooke Grief:** Right.

**Brooke Grief:** So we would just see that show up as, like, a referral from ChatGPT or...

**Aida Knezevic:** Yeah, exactly.

**Brooke Grief:** Cool.

**Brooke Grief:** That's exciting.

**Brooke Grief:** Yeah, a PDF of this weekly would be great if possible.

**Aida Knezevic:** Yeah, yeah.

**Aida Knezevic:** We can also send you a list of the prompts so you can take a look.

**Brooke Grief:** That would be great.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Okay, cool.

**Aida Knezevic:** I think I also wanted to discuss the internal content strategy development, but we can do that next week.

**Aida Knezevic:** It's not like a, you know, it wasn't, like, a huge priority for me.

**Aida Knezevic:** was more important to get the calibration reviewed.

**Brooke Grief:** Cool.

**Brooke Grief:** Yeah, I was going to ask, Seher, do you also want a copy of that Scrunch report?

**Brooke Grief:** Would that be helpful for the site at all?

**Brooke Grief:** You're on mute.

**Brooke Grief:** I'll see you in the next week.

**Brooke Grief:** Thank

**Brooke Grief:** Muted, did you say something?

**Seher Dholakia:** Thank you.

**Seher Dholakia:** Yeah, it would be great to have it.

**Seher Dholakia:** I was just going to ask, like, is the frequency weekly?

**Seher Dholakia:** Yeah.

**Seher Dholakia:** Yeah, it would be great to have it.

**Seher Dholakia:** Thank you.

**Aida Knezevic:** Yeah, sure.

**Brooke Grief:** But yeah, the content strategy, I am going to be presenting that to the exec team to get their feedback on it.

**Brooke Grief:** So it's actually good if we get to that next week.

**Brooke Grief:** Hopefully, I'll present to them between now and then, and then I'll be able to give you guys a more concise version of it.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Okay, perfect.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** All right.

**Aida Knezevic:** Well, we're at time, so I'm going to let you go, but let me know on Slack if you have any questions.

**Aida Knezevic:** And yeah, we'll be in touch with the three articles as soon as they're ready.

**Brooke Grief:** Awesome.

**Brooke Grief:** Thank you so much.

**Brooke Grief:** Thank you.

**Brooke Grief:** See you.

**Brooke Grief:** Bye.

**Brooke Grief:** Bye.
