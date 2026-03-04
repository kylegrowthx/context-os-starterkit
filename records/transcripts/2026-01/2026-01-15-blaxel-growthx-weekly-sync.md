# Blaxel <> GrowthX - Weekly Sync

<metadata>
date: 2026-01-15
time: 19:29 UTC
duration: 37 minutes
organizer: team@growthxlabs.com
participants: Paul Sinai (Blaxel), Aida Knezevic (GrowthX), Nicolas Lecomte (Blaxel), William Leborgne (GrowthX), Kathy Lam (GrowthX)
fathom_recording_id: 114677538
fathom_url: https://fathom.video/calls/532027556
share_url: https://fathom.video/share/xxJbX8viky8CXPSGK6K4cTzxWNnT4YYZ
source: fathom
enriched_on: 2026-02-28 16:45 UTC
</metadata>

---

## Summary

GrowthX and Blaxel refined their content review workflow to handle highly technical articles, updated the competitor strategy to distinguish between direct competitors and competing technologies (allowing discussion of Wasm, MicroVMs vs. containers for technical credibility and SEO), and reviewed performance metrics from the Looker dashboard. The team selected five new blog topics to balance technical and less-technical content, reducing review bottlenecks. PostHog integration will track blog performance as an alternative to GA4 due to Blaxel's legal constraints.

---

## Context

This is a recurring weekly sync between GrowthX's content operations team (Aida Knezevic, Kathy Lam, William Leborgne) and Blaxel's leadership (Paul Sinai, Nicolas Lecomte). The meeting addresses content production bottlenecks, editorial workflow optimization, and performance tracking for Blaxel's technical blog, which GrowthX is managing as part of their B2B content marketing engagement.

Key business context: Blaxel provides sandboxing technology (MicroVMs) for running untrusted code safely. GrowthX is generating in-depth technical articles to build domain authority and capture relevant search traffic. Articles require internal Blaxel review by subject matter experts (SMEs) before publication, creating a bottleneck as product development demands SME time.

---

## Relevance

This meeting is critical for managing deliverables and alignment between a client (Blaxel) and service provider (GrowthX). The decisions made directly impact:
- Content publication velocity (5 articles per week target)
- SEO performance and search positioning (initial post at position 18.6, target 1-10)
- Review process efficiency and team capacity planning
- Content strategy pivots (competing technologies vs. direct competitors)

The workflow changes discussed will inform how future content batches are staffed and scheduled. The technical depth discussion and SME review workflow have implications for Blaxel's ability to sustain the publishing cadence without degrading quality.

---

## Overview

- **Workflow Refined:** Blaxel and GrowthX implemented a new Airtable-based SME review status to clarify when technical articles require additional expert eyes. Blaxel can flag articles for "SME Review" and tag GrowthX with status updates via comments (Blaxel has read-only access to Airtable).
- **Content Mix Strategy:** Future batches will mix technical and less-technical articles to balance Blaxel's review load and reduce bottlenecks during product release cycles.
- **Competitor Strategy Updated:** The content workflow's "remove competitors" instruction was overcorrecting, omitting relevant competing technologies (e.g., Wasm, containers) that are essential for technical credibility and SEO. The workflow will now distinguish between direct company competitors (e.g., E2B, Modal) to exclude, and competing technologies to include in comparative analysis.
- **Performance Dashboard Live:** The Looker dashboard is pulling data from Google Search Console (GSC). One published article has 159 impressions with an average position of 18.6; the target is 1-10. GA4 is unavailable due to Blaxel's legal constraints.
- **PostHog Integration:** GrowthX will create a PostHog view to track performance of published blog URLs, with BigQuery export as a fallback if needed.
- **Five New Topics Selected:** Sandbox for AI agents, MCP vs. API, Modal vs. E2B (competitive analysis), How to build a sandbox with GPU support, and Serverless sandboxing. Kathy Lam noted the Webflow VP of Engineering reached out with technical questions that could inform a blog topic.

---

## Key Topics

### Content Review Bottleneck

- **Problem:** Blaxel's internal review process is a bottleneck for publishing technical articles.
  - **Cause:** Technical depth requires specific SMEs (developers), who are often unavailable due to other priorities like product releases.
- **Solution:** A new process will be implemented to improve review efficiency.
  - **Airtable Workflow:**
    - Blaxel will flag technical articles in Airtable.
    - GrowthX will add an "SME Review" status.
    - Blaxel will tag GrowthX in comments to request status changes, as their access is read-only.
  - **Content Mix:** Future article batches will mix technical and less technical topics to balance the review load.
  - **Revision Cycles:** GrowthX typically does up to two rounds of revisions per article. After the first round, if Paul or Nicolas request additional SME review, GrowthX will create the SME Review status in Airtable and wait for another round of feedback before marking ready to publish.

### Competitor & Technology Strategy

- **Problem:** The content workflow's "remove competitors" instruction overcorrected, causing the AI to omit relevant competing *technologies* like Wasm.
- **Solution:** The workflow will be updated to distinguish between direct company competitors and competing technologies.
  - **Direct Competitors (Companies):** Continue to exclude (e.g., E2B, Modal).
  - **Competing Technologies (Concepts):** Allow for comparative discussion (e.g., Wasm, containers, MicroVMs).
    - **Rationale:** This is crucial for technical credibility and SEO. When users search "sandbox with containers" or "execute safely in the browser," Blaxel should appear in alternatives. Mentioning the technology first (Wasm, containers) makes Blaxel visible in those queries and positions MicroVMs as the superior alternative.
    - **Examples:** The "Browser Isolation" article should mention Wasm as the first technology created for safe browser execution, then position Blaxel's approach. MicroVMs vs. containers should compare both with balanced analysis.

### Performance Tracking & Reporting

- **Looker Dashboard:** The dashboard is live, pulling data from GSC.
  - **Initial Data:** One new post has 159 impressions with an average position of 18.6.
  - **Goal:** Achieve an average position of 1-10 for new content (1-10 is page 1 ranking; 10-20 is also good if the query has high search volume).
  - **Interpretation:** Every blog post ranks for many keywords. The average position of 18.6 means it's ranking on page 2 across its keyword mix, which is early-stage but acceptable for new content.
- **PostHog Integration:** GrowthX will integrate PostHog data to track blog performance, as GA4 is not an option due to Blaxel's legal constraints around adding new tracking providers.
  - **Action:** GrowthX will create a PostHog view with all published blog URLs to track blog performance separately from the main Looker dashboard.
  - **Support:** Blaxel will provide engineering support if needed. PostHog data can also be exported to BigQuery if additional analysis is required.

### New Blog Topics

Five new blog topics were selected to create a balanced review load:
1. Sandbox for AI agents (technical)
2. MCP vs. API (technical, emerging topic)
3. Modal vs. E2B (competitive analysis, technical)
4. How to build a sandbox with GPU support (technical, high search volume)
5. Serverless sandboxing (technical)

Paul also noted that the Webflow VP of Engineering asked him about competing sandboxing approaches from other platforms (Vercel, Cloudflare, Fly.io), suggesting there's demand for technical awareness content from engineering executives, not just developers.

---

## Action Items

**Aida Knezevic (GrowthX)**
- Block calendar to disable extra note-takers
- Email Looker dashboard access to Nicolas Lecomte & Paul Sinai

**Nicolas Lecomte (Blaxel)**
- Unpublish unreviewed blog post
- Apply Paul's edits in Strapi
- Correct publish date on "What is AI Sandbox" article

**Kathy Lam (GrowthX)**
- Update AI workflow to allow competing-technology mentions (e.g., Wasm, containers); clarify distinction from direct company competitors
- Fix Strapi schema-markup permissions; update schema markup for blog posts
- Create PostHog view for published blog URLs; share access with Nicolas & Paul
- Follow up with Nicolas regarding cloud-code prompts for Check That
- Draft next 5 articles: Sandbox for AI agents, MCP vs API, Modal vs E2B, How to build sandbox with GPU, Serverless sandboxing

**Paul Sinai (Blaxel)**
- Share Slack reply regarding Webflow VP of Engineering's questions about competing sandbox technologies (potential blog topic)

---

## Transcript

**Kathy Lam:** Hey Aida, how's it going?

**Aida Knezevic:** Good.

**Kathy Lam:** I can't believe we're outnumbered by the AI.

**Aida Knezevic:** Yeah, I know.

**Aida Knezevic:** Not the first time it's happening.

**Kathy Lam:** So I think after this week, think William will take over for Blaxel for the next couple weeks.

**Kathy Lam:** And then, does that sound right?

**Aida Knezevic:** Wait, so you're going to be out of office?

**Kathy Lam:** Yeah, yeah, that was the, not, so I think, yeah, let's chat afterwards.

**Nicolas Lecomte:** Heyo.

**Kathy Lam:** Hi.

**Kathy Lam:** Hi.

**Kathy Lam:** How are you doing?

**Nicolas Lecomte:** Hi, everyone.

**Nicolas Lecomte:** I'm good.

**Nicolas Lecomte:** How are you guys?

**Kathy Lam:** Pretty good.

**Kathy Lam:** How's your week been?

**Nicolas Lecomte:** Good.

**Nicolas Lecomte:** Intense.

**Nicolas Lecomte:** Lots of activity.

**Nicolas Lecomte:** It's good.

**Nicolas Lecomte:** I can feel everybody's back.

**Nicolas Lecomte:** So, yeah, no, it's pretty cool.

**Kathy Lam:** Yeah, yeah, definitely.

**Kathy Lam:** It's interesting.

**Kathy Lam:** Every time I message you, regardless of the timing, you're always on, so it's quite funny.

**Nicolas Lecomte:** Me too, yeah, because I forgot.

**Nicolas Lecomte:** You're probably saying.

**Nicolas Lecomte:** I at the beginning, but I forgot what time zone you were on.

**Nicolas Lecomte:** was, oh, I thought, because you're maybe northeast?

**Nicolas Lecomte:** West coast, yeah.

**Nicolas Lecomte:** Oh, you're west coast.

**Nicolas Lecomte:** Okay.

**Nicolas Lecomte:** Okay, okay.

**Nicolas Lecomte:** But, yeah.

**Nicolas Lecomte:** I'm going to tell Paul that we're starting.

**Kathy Lam:** Okay, great.

**Kathy Lam:** And that was not the window I was trying to share.

**Kathy Lam:** I was just trying to share one window.

**Kathy Lam:** Let's try again.

**Kathy Lam:** Cool.

**Nicolas Lecomte:** Have you been able to make an opinion on the note takers?

**Kathy Lam:** Actually, that question's for Aida.

**Kathy Lam:** I know we were trying one other one, but are we going with Fireflies?

**Aida Knezevic:** with, yeah, Fireflies.

**Aida Knezevic:** But I first need to figure out how to stop all the other ones from joining my calls, which is an undertaking in itself.

**Aida Knezevic:** So, Aida.

**Kathy Lam:** Aida.

**Kathy Lam:** the

**Kathy Lam:** Set aside a calendar block to figure out how to do that.

**Nicolas Lecomte:** Cool, all the little minions.

**Nicolas Lecomte:** Somebody said, yesterday somebody told me that the Notion AI one had a very accurate transcript.

**Nicolas Lecomte:** Haven't tested it, but we were thinking, because Circleback is a bit annoying, like the local client is a bit funky sometimes.

**Nicolas Lecomte:** We were thinking maybe we would try at Notion.

**Nicolas Lecomte:** Apparently that the transcription is very accurate.

**Kathy Lam:** I've been using Notion a lot in, like, taking things from SEMrush and then creating tables.

**Kathy Lam:** It's very good, like, using AI to do that.

**Nicolas Lecomte:** So, It's surprisingly good for a company who's not primary focus, who's not AI.

**Nicolas Lecomte:** It's surprisingly good.

**Nicolas Lecomte:** Or Granola as well.

**Aida Knezevic:** I keep hearing it's a good one.

**Aida Knezevic:** I wonder who Notion is using on the back end.

**Aida Knezevic:** Like, is it DeepGram or they're using some type of speech-to-text API, but I wonder who it is.

**Nicolas Lecomte:** I don't know.

**Nicolas Lecomte:** I have no idea.

**Kathy Lam:** Cool.

**Kathy Lam:** With that, let's jump in.

**Nicolas Lecomte:** But before we begin, anything top of mind?

**Nicolas Lecomte:** No.

**Nicolas Lecomte:** Oh, hey, paul.

**Nicolas Lecomte:** We have the...

**Nicolas Lecomte:** You read the agenda before, so we did the article.

**Nicolas Lecomte:** Yeah.

**Nicolas Lecomte:** Okay.

**Kathy Lam:** No, nothing else that I think we won't cover.

**Nicolas Lecomte:** Okay.

**Kathy Lam:** Great.

**Kathy Lam:** I know we, right before this call, Natalie published two more blogs, just from the drafts that we've been working on.

**Kathy Lam:** I think there's one that has a few more...

**Nicolas Lecomte:** So I think, well, so that was, okay, so that was my question then.

**Nicolas Lecomte:** So I think this one...

**Nicolas Lecomte:** Which one?

**Nicolas Lecomte:** Sorry, the one on the left, I don't think it has been reviewed.

**Nicolas Lecomte:** That was my point.

**Kathy Lam:** Oh, okay.

**Nicolas Lecomte:** We can take that off.

**Nicolas Lecomte:** if you can, yeah, quickly unpublish this one, because I was sort of...

**Nicolas Lecomte:** used with your message, and then that's when we checked in with the team, just before the call, because I didn't know if somebody reviewed it, and I didn't know, but this one, I think, hasn't been reviewed.

**Nicolas Lecomte:** You're on mute, by the way.

**paul:** It happens all the time.

**paul:** Just this one is the one I asked Matisse to review, and he gave me that, but I was supposed to do a second round.

**paul:** And, um, and there is another one, which I think was ready for, um, maybe it was yours.

**Nicolas Lecomte:** This one, so this one here, the What is AI Sandbox, this one is, I read, or I, you know, read again the changes that you made.

**Nicolas Lecomte:** For me, that looks good.

**Nicolas Lecomte:** Um, I know that you hadn't read it, Paul, but for me, it was good, so, um.

**Kathy Lam:** You check.

**paul:** No, go ahead, although, you know, worst case, I can share it with you, minor updates.

**Nicolas Lecomte:** During the day, and Nicolas, you can directly apply them inside Strapi.

**Nicolas Lecomte:** I guess there's more, I don't know, there's something, I guess, wrong, because it says December 12th is the date, so I'll have to have a look at it.

**paul:** Maybe to share with Kathy and Aida, we were talking during our daily meeting with the teams this morning, how we're going to manage, we need to reorganize ourselves to manage the throughput of post review.

**paul:** So we annotate that we are not fast enough right now, so we are trying to find out what is the best way to work to, you know, increase the bandwidth in terms of reviewing.

**Nicolas Lecomte:** So it's just… Because some of them are technical, it's not just high level, some of them get pretty technical, so… Yeah, exactly.

**paul:** The more technical the post is, the longer it takes for us to review, depending on the subject, we have, like, several expertise inside the company.

**paul:** And…

**paul:** So sometimes we just need to wait for a developer to become available to review a specific topic because they were working on this topic previously.

**paul:** This is a case of how to escape from a sandbox.

**paul:** One of our team members is doing this, not all the time, but very frequently trying to escape, you know, doing security tests.

**paul:** So yeah, it's just, yeah.

**Kathy Lam:** Yeah, and whenever we can incorporate that, it's good.

**Kathy Lam:** But then I also, what we could do is maybe as we're deciding on the next set of articles, what we could do is put a flag there and just know that there would be a long like revision cycle, but maybe also deprioritize that during times when your team is like, like furiously pushing for the next release or something.

**paul:** So absolutely.

**Nicolas Lecomte:** I think we'll always sort of be pushing.

**Kathy Lam:** That's the problem is we don't really have, like we'll always sort of have something going on.

**paul:** So, I mean.

**paul:** Yeah, exactly.

**paul:** I wish I could tell you.

**paul:** Yeah.

**paul:** This week we had a big release in production.

**Kathy Lam:** It's going to be the same in two weeks and three weeks.

**Kathy Lam:** we don't want to fool ourselves and we just want to find exactly the right process.

**paul:** Otherwise, it's great.

**paul:** I really like the output.

**paul:** I think it still requires more adjustments because it's very technical for some of them, much more technical than I expected at the beginning, which is great.

**paul:** Honestly, it's great.

**paul:** It's just it requires a bit more reviewing and probably a second cycle of generation.

**paul:** It's the case of the one where...

**paul:** The browser one.

**paul:** browser one, yeah.

**paul:** We showed a few...

**paul:** So one of my questions is what is the usual process when there is more extensive rewriting to do?

**Kathy Lam:** How does it work?

**Aida Knezevic:** Yeah.

**Aida Knezevic:** So what we typically do, so we do up to two rounds of revisions on a block.

**Aida Knezevic:** so what

**Aida Knezevic:** Post, so what, it really depends.

**Aida Knezevic:** So we can set up an Airtable automation so that whenever a draft is ready for your review, you get an email.

**Aida Knezevic:** And then, let's say, for example, you tell us, okay, this blog post needs an additional look by a developer or a subject matter expert.

**Aida Knezevic:** Then we will create a new status, an Airtable for, like, SME review.

**Aida Knezevic:** And then we will do that blog post there.

**Aida Knezevic:** And then we will know, okay, this blog post was reviewed by Nicolas, by Paul, but now we're waiting for another pair of eyes on it.

**Aida Knezevic:** I think also, the reason that the blogs are technical is because our researcher is pretty good at finding a lot of information.

**Aida Knezevic:** So, all of that information is incorporated into the articles.

**Aida Knezevic:** But yes, it does make the process a little bit longer.

**Aida Knezevic:** So yes, so we can do, I think you are probably the best to kind of decide, okay, which blog post needs to be reviewed by an SME.

**Aida Knezevic:** But I think would also be helpful ahead of time when you, you know, when we approve articles, you can also let us know, this is going to be, might be a little bit technical.

**paul:** Yeah, absolutely makes sense.

**paul:** I think it's, this first round really helped us to understand exactly what is the type of output we can get.

**paul:** And this is super useful.

**paul:** And again, like the quality is quite high, honestly.

**paul:** It's just because we are going deeper technically, at some point, like it's the case of the browser isolation.

**paul:** But for instance, we are not mentioning WASM, which is a technology, which is pretty, you know, it's, it's, it's.

**paul:** Part of the background, so I didn't know if the agent during the text didn't mention this because of the SEO, NGO optimization, or if it was intended to not mention Wasm or not.

**paul:** So it's where we say, okay, we put a lot of comments, and then what's the process?

**paul:** Like, it's someone reviewing this on your side?

**paul:** Yes.

**Nicolas Lecomte:** Which, on the topic of Wasm, just to emphasize on this, it's one of them that I flagged as competing technologies, so depending on how you adjust the prompts, I guess it's like, we don't want to recommend this technology, but it's okay to talk about it as in, like, this is, you know, in the landscape, people are doing this, and it's better for that reason, or it's not better for that reason, but it's in that use case, you can use it for that.

**Nicolas Lecomte:** But if you want to do things seriously, or if you want to do things better, whatever, you can do it with sandboxing, like, technology.

**Aida Knezevic:** I definitely know what happened here because our workflow has an instruction to remove mentions of competitors.

**Aida Knezevic:** So that's what happened in the whenever we because a lot of times if you if we generate content and we don't have that instruction, then the workflow might bring up your direct competitors and talk about them and we might probably don't want to talk about them.

**Aida Knezevic:** So I think this is one of the situations where it overcorrected.

**Aida Knezevic:** So it should have mentioned it just in passing, but it overcorrected and it removed.

**Aida Knezevic:** But yes, whenever you leave comments, a human editor is going through and accepting the changes.

**Aida Knezevic:** And then anything, any bigger comments that you leave, we update the artifacts, the workflow, sometimes one, not the other.

**Aida Knezevic:** But I know that right now we are also like really trying to like customize.

**Aida Knezevic:** this be one of the and in

**Aida Knezevic:** Pipeline to each client, depending on what your feedback is, so that, you know, the output is closer to, so that you just have to leave, like, fewer comments.

**Nicolas Lecomte:** No, that makes a lot of sense.

**Nicolas Lecomte:** so I think for the competitors, I think there are two things.

**Nicolas Lecomte:** There's the direct competitor, as in companies.

**Nicolas Lecomte:** So those are E2B, the one that we flagged in the intake.

**Nicolas Lecomte:** And then there are competing technologies, which is more, you when we get into the details of stuff, okay, know, MicroVM is the technology, generally speaking, that we use.

**Nicolas Lecomte:** containers is another example.

**Nicolas Lecomte:** And so Wasm, in that case, is more of a technology than they're not a company.

**Nicolas Lecomte:** It's not a company.

**Kathy Lam:** So it's a technology.

**Nicolas Lecomte:** So it's like a different level.

**Nicolas Lecomte:** So what I understand is, just going back to the lifestyle, the flow that we use, so, you know, we can use the air table, you guys flag us whenever, so we can flag ahead of time, if we think an article is going to be more technical than another, then you guys, you know, as soon as, I guess, the first generation has been done.

**Nicolas Lecomte:** of content, you flag us that it's ready for review, and then we dispatch, you know, either, you know, I can review myself, or we have to dispatch to somebody more technical, and then we flag it back, you know, if there are updates to do that, we can flag it back with another status inside of the art table to you guys to say, okay, either this one, I think, needs a bit more rework, or, okay, I think this one is ready for publication.

**paul:** Just a quick, a quick note here, just about the computing technology, I think it's really interesting, because for some blog posts, it's actually good to compare both technologies, and I'm more comfortable doing this, rather than comparing, you know, ads to head, YouTube with us, or, or things like that, so, and probably tell me, but probably for SEO and geo is also better, because if someone is talking about Soundbox and containers, we have a higher chance to be mentioned, and it's what we want, like, if people

**paul:** People are doing, hey, want to do some boxing with containers.

**Nicolas Lecomte:** I would like to be in the alternatives.

**paul:** Yeah, the article.

**Nicolas Lecomte:** Yeah.

**paul:** But at the same time, we just need to be careful.

**paul:** If we are talking about Blaxel, the technology of Blaxel is not containers, it's micrograms.

**Nicolas Lecomte:** So I guess, yeah, I guess it's okay to mention competing technologies, but just not say that they're the best thing on Earth.

**paul:** And sometimes we have to.

**paul:** It's the point of Matisse on the browser's unboxing, not talking about Wasm.

**paul:** At some point, in the example, the posts were saying that we need to execute safely and how it works inside the browsers right now.

**paul:** And the first technologies that have been created for exactly this use case was Wasm.

**paul:** So I feel like if we are going technical, we have to mention this technology.

**Nicolas Lecomte:** We cannot, you know, just ignore it because otherwise.

**Nicolas Lecomte:** Otherwise.

**paul:** Experts are going to say, yeah, guys, are you kidding?

**paul:** You are not even mentioning the number one which was used for that.

**Kathy Lam:** Great.

**Kathy Lam:** This is perfect.

**Kathy Lam:** We will update that, and then I'll let Natalie know.

**Kathy Lam:** We should be really good to go.

**Kathy Lam:** She did mention that she tried to edit the schema markup, but then didn't have permissions.

**Kathy Lam:** If there's any chance that can be updated, we'll go in and update the schema.

**Nicolas Lecomte:** Okay.

**Nicolas Lecomte:** Sounds good.

**Kathy Lam:** Sorry about that.

**Kathy Lam:** I'll have a look.

**Kathy Lam:** No worries.

**Kathy Lam:** I'll add that later on to next action items, but we should be good.

**Nicolas Lecomte:** Sorry to just go back.

**Nicolas Lecomte:** So on the status, there's a status in the article so that we can say, okay, come back to the, I didn't have a look, a close look at the article, but we can say, okay, it's back to production on your end or it's ready to publish.

**Kathy Lam:** Yes.

**Kathy Lam:** that right?

**Kathy Lam:** Yeah, so, um, Okay.

**Kathy Lam:** We'll make sure, I think you have access to this one.

**paul:** Okay, no, have access, because last time I checked, it didn't work, so I just want to be sure that it's safe.

**Aida Knezevic:** so the Airtable access, you have commenting access, and Airtable doesn't let you update the status with that level of access, so what you can do, you can leave, you see the comment icon, if you click there, can leave a comment tag, Kathy and Natalie, and let them know that, like, what you wanted to do.

**paul:** Okay, so we proceed with the comments, okay, okay, just to know, okay, that's good.

**Nicolas Lecomte:** Awesome, and then, and then, and then, so, one of last questions, so, we can do, said, it's, like, usually two rounds, so, like, you know, you give it to us for review, we have some changes that we request, so you guys do it, then you can go back to us, and then we can request additional changes, but then, you know, that's, like, the second and last time that you guys did it, okay.

**paul:** And we should...

**paul:** We plan for the different batch of posts, we should plan a mix of technical and less technical, because less technical will be faster, so if we have five article, five posts, we should not have like five technical posts during the same week.

**Kathy Lam:** I was thinking exactly that.

**Kathy Lam:** Great.

**Kathy Lam:** Okay, let me go back.

**Kathy Lam:** think we did like hook up the local dashboard, but we'll need like, I think actually GA4 access, so that we can like get the specific search volume, not search volume, but like impression volume.

**Kathy Lam:** We have been able to look at, let me see, we have been able to look at like how many impressions this one, so it's currently a hundred and

**Kathy Lam:** 59 questions, and the average position is 18.6.

**Kathy Lam:** So hopefully as more and more queries come in, we can get more clicks on this, but this is fairly early.

**Kathy Lam:** Any, Nico, I wanted to, you look concerned, so I wanted to.

**Nicolas Lecomte:** So because we are aiming to be one, 18.6 is supposed to become one.

**Aida Knezevic:** That's for the average position.

**Aida Knezevic:** So typically, 1 through 10 is on page 1, and you are ranking, every blog post ranks for many different keywords.

**Aida Knezevic:** So for many of them, you will rank for maybe like on page 3.

**Aida Knezevic:** So we're looking for an average between 1 to 10.

**Aida Knezevic:** That's the ideal sweet spot.

**Aida Knezevic:** But also, like, between 10 and 20 is also good, because if one of those queries.

**Aida Knezevic:** has like 200 searches and you're in position two, then we're in a great spot.

**Aida Knezevic:** So it's the average of all of the rankings.

**Aida Knezevic:** I did want to show you, you mind, Kathy, if I share my screen really quickly.

**Aida Knezevic:** So yeah, the Looker dashboard that Kathy just shared, this is typically more expanded with GA4 data because we don't have GA4 data right now.

**Aida Knezevic:** We were just able to create like a smaller version of this report.

**Aida Knezevic:** So right now, we will email you access to this report, but right now you can see an overview of non-branded clicks and impressions to your website.

**Aida Knezevic:** And this is just data from Google Search Console, which means that this is organic search traffic.

**Aida Knezevic:** You can also see...

**Aida Knezevic:** see...

**Aida Knezevic:** Different landing pages, the performance of different landing pages, and this is basically when you open Google Search Console, this is the first report that you see, so it shows the average clicks, impressions, click-through rate, and average position over a period of time.

**Aida Knezevic:** You can also switch the dates here, and then you can also see what are all the landing pages that are getting organic traffic for the time period that you selected.

**Aida Knezevic:** And then the queries report allows you to see what are all of the queries or keywords that are driving users to your website.

**Aida Knezevic:** So, typically, there's going to be a lot of branded keywords here, but again, once we start really publishing content at scale, there are going to be many more non-branded queries here, and you can also...

**Aida Knezevic:** So you see kind of the query distribution, which are like the top keywords that you're ranking for, obviously.

**Aida Knezevic:** A lot of branded stuff in here.

**Aida Knezevic:** One thing we do want to pull in here, and this is just an additional page that we are going to create.

**Aida Knezevic:** It's just a small report that includes the organic search performance of the content that GrowthX publishes.

**Aida Knezevic:** So you will be able to see, you don't have to go into Google Search Console, like filter all of the pages.

**Aida Knezevic:** The data will be filtered here, so you can log in and see, okay, how many clicks did we get?

**Aida Knezevic:** Like what pages are getting the most traffic?

**Aida Knezevic:** What's the average position?

**Aida Knezevic:** Just to make it easier for you.

**Aida Knezevic:** So that's just the one report that we have to add in.

**Aida Knezevic:** Typically, it also is combined with GA4 data, but we don't really need it for this purpose.

**paul:** GSC is going to do just fine.

**paul:** Okay.

**paul:** Okay.

**paul:** And, and, um,

**paul:** Do we have the data on PostHog, too, for the blog itself?

**paul:** Did you successfully connect to PostHog and get the data?

**Kathy Lam:** I was able to get into PostHog, but I think I wasn't able to get the data yet.

**Kathy Lam:** So is it possible at all for you to add GA4 to your site, or is that...

**Aida Knezevic:** It's just for, we have to change the privacy policies, and it's...

**paul:** Yeah, yeah, yeah, that's not...

**paul:** It's just a lot of legal stuff for us to add a new provider, so if it's possible to stick with them.

**paul:** But if you have issues, we can ask one of the engineers to look at it and check if there is something missing on the blog.

**Aida Knezevic:** Yeah, I think all that we need to do really in PostHog is create, like, a view that's going to have all of the URLs of the pages.

**Aida Knezevic:** to to have...

**Aida Knezevic:** We're We're to to this.

**Aida Knezevic:** that we published where we can track the performance.

**Aida Knezevic:** So it should be fairly easy to set up.

**paul:** Yeah, sure.

**paul:** Yeah, and then we can help you with that.

**paul:** Another thing that we can do is also export data to BigQuery from Postdoc.

**paul:** There is exporter directly integrated inside Postdoc.

**paul:** So if at some point it also makes things easier for you, it's another thing that we can do.

**Kathy Lam:** Cool.

**Kathy Lam:** We'll try this on the Postdoc side to see if I can create that page.

**paul:** then if I need some help, I'll pick you guys.

**paul:** Sure, yeah, let me know, OK?

**Kathy Lam:** Excellent.

**Kathy Lam:** Cool.

**Kathy Lam:** Let me see.

**Kathy Lam:** I think we're nearing time, but I wanted to cover a couple more topics.

**Kathy Lam:** I've been adding some additional prompts to check that.

**Kathy Lam:** Right now, we just set up your page on Check That.

**Kathy Lam:** There's no data in it, so it's kind of not as beneficial to share.

**Kathy Lam:** But I've added the following.

**Kathy Lam:** We prompts in the different, like, buy stages, so awareness, evaluation, comparison, decision, and post-process, post-purchase, let me make sure you all have access, yup, if there are additional ones that you'd like us to add, feel free to either send them that my way, you don't actually need to send it here, you can, yeah, sure, yeah, I think, I think, Nico, we can add cloud code, you know, there is a, yeah, there's a few that I can think of.

**Kathy Lam:** Perfect, yeah, maybe I'll follow up with you, like, after online to make sure we can get that info, but I think the other thing I wanted to focus on was just figuring out if you have any, like, preferences on the next set of five.

**Kathy Lam:** I know we're working on the current, the previous set of five, we should have drafts for you soon, I think, what delayed it was, we were focusing on, what is it, making sure we

**Kathy Lam:** We had all the feedback, but if there's like any in this like group that calls out to you specifically, we can like set them up, and then we'll also pick a few that are not technical as well, and then send them out.

**Kathy Lam:** So do you need me to ask me, I think like, I think there's one is how to build.

**paul:** I like the fifth one, the Soundbox for AI agents, where it's made it like cycles and everything, and I think it's this one.

**Kathy Lam:** Yeah.

**paul:** looks good.

**Kathy Lam:** Yeah.

**Kathy Lam:** Right.

**Kathy Lam:** We, I just shared it with, you know, code only.

**Nicolas Lecomte:** So, you could do the MCP versus API.

**Nicolas Lecomte:** It's been a topic lately.

**paul:** Okay.

**Nicolas Lecomte:** And there is a competitive article, like, between, like, Modal or E2B.

**Nicolas Lecomte:** Maybe Modal, yeah.

**Nicolas Lecomte:** Maybe a little article on Modal.

**Kathy Lam:** It could be nice.

**Nicolas Lecomte:** one?

**Nicolas Lecomte:** Or which one is it?

**Nicolas Lecomte:** The first one, that one.

**Kathy Lam:** perfect.

**Nicolas Lecomte:** So that's three.

**paul:** You need two more?

**paul:** Yes.

**Kathy Lam:** Okay, okay.

**Kathy Lam:** The first one, the one that had, I think, a huge volume.

**Kathy Lam:** Yes.

**Nicolas Lecomte:** How to build this one?

**paul:** Yeah, yeah.

**paul:** Yeah.

**paul:** Yeah.

**Nicolas Lecomte:** this can't have GPU supports.

**paul:** Interesting.

**paul:** The 20th serverless of Tuesday, KT Dusting, I think.

**paul:** It's not a big volume.

**paul:** Maybe you are looking for something bigger.

**Kathy Lam:** you

**Kathy Lam:** I think this actually is very, very relevant to what you're doing.

**paul:** while it's like high volume, I think it's important.

**paul:** sense.

**Kathy Lam:** Okay.

**Nicolas Lecomte:** Yeah.

**Nicolas Lecomte:** Let's do it.

**Nicolas Lecomte:** Okay.

**Nicolas Lecomte:** Yeah.

**Kathy Lam:** I think have a good mix.

**Kathy Lam:** Yeah.

**Kathy Lam:** I think, let me see.

**Kathy Lam:** This should be the ones that I think, let me group them again.

**Kathy Lam:** Filter on.

**Kathy Lam:** Yeah.

**Kathy Lam:** So these should be the ones that we're working on that are in production.

**Kathy Lam:** Let me see.

**Kathy Lam:** Let me choose this one instead.

**Kathy Lam:** Filter by status is in production.

**Kathy Lam:** Yeah.

**Kathy Lam:** So there should be about 10 in here that we should.

**Kathy Lam:** Okay.

**Kathy Lam:** Excellent.

**Kathy Lam:** Yeah.

**Kathy Lam:** I think that should be the subject.

**Kathy Lam:** That should be all the topics we want.

**Kathy Lam:** Let me just make sure we have everything.

**Kathy Lam:** Oh, I think Nelly also made sure we updated the image so that it's a little bit more technical.

**Kathy Lam:** And then going forward, more and more of the images will be skewing more technical and more like it.

**Kathy Lam:** No, I think it was good.

**Kathy Lam:** Awesome.

**Kathy Lam:** I think, yeah, I think that's pretty much it.

**Kathy Lam:** Any, yeah, like, how are you guys feeling right now?

**Nicolas Lecomte:** I'm very good.

**Nicolas Lecomte:** Honestly, I'm pretty excited.

**paul:** I'm more, you know, not worried, but concerned on our side that we need to be more organized to really...

**Nicolas Lecomte:** I would need to make sure that we make a review in time.

**paul:** We are not slowing.

**paul:** We don't want to slow down the publication.

**paul:** So it's...

**paul:** But I...

**paul:** We're We're Here Thank

**paul:** I guess for us, it's just a question of organization.

**paul:** So we're going to fix this just to make this things faster.

**paul:** But yeah, so far, so far, pretty exciting and looking forward to see the results.

**Nicolas Lecomte:** I actually have a dumb question, maybe, because you guys do five articles per week, I think, right?

**Nicolas Lecomte:** So if we have one day delay, then we don't have room for catching up.

**Nicolas Lecomte:** Or do we publish on weekends then?

**Nicolas Lecomte:** Or do we do two posts a day?

**Nicolas Lecomte:** Like, what do people do usually when we need to catch up?

**Aida Knezevic:** It's really, I mean, we say five, we try to deliver five blogs per week and publish five blogs per week.

**Aida Knezevic:** But if it doesn't happen, like, let's say, you know, we don't have one article ready to go on Friday, we'll publish it on Monday.

**Aida Knezevic:** Like, it's not, you know, we don't try to schedule it very, very rigidly.

**Aida Knezevic:** We will publish them as they're ready.

**Aida Knezevic:** So what's important is that the content production is...

**Aida Knezevic:** will...

**Aida Knezevic:** More or less steady, but the publishing is steady.

**Aida Knezevic:** But also, paul, to your point, you know, if you, we can very easily do additional keyword research and topic generation to pivot to topics that aren't as technical.

**Aida Knezevic:** So we can very much adapt, you know, if you feel like, okay, listen, this is taking too much time and resources for us to edit.

**Aida Knezevic:** Like, we could just be like, okay, we will pivot and do like more commercial intent and just try to cover things maybe like at a higher level.

**paul:** No, I think, I think it's, it's because the quality is here so far, like we don't, it really depends.

**paul:** Maybe in two weeks or three weeks, I will tell you, yeah, maybe there is too much review.

**paul:** Like, it's, it's not just reading it, there is too much back and forth that we have to do to, to make this really accurate and relevant.

**paul:** Maybe there, then we will adjust, but because of our persona and who we are targeting, I.

**paul:** I think it's right.

**paul:** Right.

**paul:** Let's give us maybe two weeks to see how it goes, and then we can decide maybe add a little bit more posts which are less technical, maybe for more executive audience.

**paul:** But I think we are not that far.

**paul:** For instance, the VP of engineering of Webflow, he asked me in a direct channel a lot of technical questions about competitions, like what is the sandbox from Versa or for Cloudflare are doing?

**paul:** What do you think about this blog post from Fly.io?

**paul:** So they need some kind of awareness, but technical awareness.

**Aida Knezevic:** They need education.

**paul:** So I think it's good to also have technical content, even for our main personnel that we are targeting with you.

**Kathy Lam:** Yeah, absolutely.

**Kathy Lam:** Oh, sorry.

**Aida Knezevic:** Go ahead, Aida.

**Aida Knezevic:** No, don't worry.

**Kathy Lam:** I was going to ask, is that discussion recorded and based on...

**Kathy Lam:** On the information that you said on that call, would it make a good topic for a blog?

**paul:** It's a Slack discussion, but I could potentially share my reply.

**paul:** It's usually short, it's not a huge one, but it's still some, so yeah, I could share if you want, yeah, of course.

**Kathy Lam:** Yeah, if you wouldn't mind.

**paul:** Great.

**paul:** Sounds good.

**Kathy Lam:** Great, so look forward to next week.

**Kathy Lam:** There, I will be flying to Asia, so there will be a few days where, like, where I think someone will be covering, but I'll make sure that when I'm still online to make sure everything's still going.

**Aida Knezevic:** Yeah, I'll be here as well, so any questions, feel free to tag me in the external channel as well.

**paul:** Aida, you are based in Europe?

**Aida Knezevic:** Yes, I am based in Sarajevo.

**paul:** Oh, nice.

**paul:** Nice.

**paul:** Super nice.

**paul:** Okay.

**paul:** Yeah, because I was, it's during the night, right, behind you?

**Nicolas Lecomte:** I know it's winter.

**Nicolas Lecomte:** Dark outside.

**paul:** Okay.

**paul:** Okay.

**Nicolas Lecomte:** And Katie, you are in the U.S.

**Nicolas Lecomte:** or you are somewhere else?

**Kathy Lam:** Yeah, I'm in California.

**Kathy Lam:** But next week, after Thursday, I'll be in Hong Kong.

**paul:** Okay.

**Nicolas Lecomte:** Okay.

**paul:** Nice.

**paul:** So if I don't talk to you, then safe travel.

**paul:** And again, we really enjoy working with you so far.

**Kathy Lam:** So that's good to you.

**Kathy Lam:** Excellent.

**Aida Knezevic:** Great.

**Aida Knezevic:** Thank you.

**Aida Knezevic:** Thanks for the feedback.

**paul:** Thank you.

**paul:** Thank you.

**Nicolas Lecomte:** Thank you, guys.
