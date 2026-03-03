# Webstacks <> GrowthX - Weekly Sync

<metadata>
date: 2025-09-18
time: 16:31 UTC
duration: 38 minutes
organizer: rachel@growthxlabs.com
participants: Jakub Rudnik (GrowthX), Rachel Pasche (GrowthX), Jessalynn Jones (GrowthX), Jesse Schor (Webstacks)
fathom_recording_id: 88253013
fathom_url: https://fathom.video/calls/413696372
share_url: https://fathom.video/share/TzYXsui1Bw4-qnn3gYsufyxSEznz_BFz
source: fathom
enriched_on: 2026-03-03 12:45 UTC
</metadata>

---

## Summary

GrowthX and Webstacks aligned on content strategy improvements, including a chapter-by-chapter analysis of spoke pieces to identify and address content cannibalization, launch of a new "Coffee Chats" blog series from existing Webstacks video content, and plans to add video snippets and thought leadership elements to articles. Jakub presented a draft experiment to test FAQ and TLDR sections on ~400 blog posts, with technical implementation details to be finalized async.

---

## Context

Webstacks is a design and content partner for GrowthX's blog strategy. This is a weekly sync to align on content production, SEO performance, and strategic direction for an ongoing hub-and-spoke content architecture. Webstacks designs graphics, manages CMS implementation, and handles video production (Gong recordings and "Coffee Chat" interviews with design experts like their head of design). GrowthX handles editorial planning and content writing. The team has completed pillars and sub-pillars for a major content initiative and is now optimizing spoke pieces by analyzing Google Search Console performance data to identify cannibalization. They're also exploring new content formats (video snippets via Descript, thought leadership pieces, FAQ/TLDR experiments) to increase engagement and distribution across channels.

---

## Relevance

**To GrowthX Delivery:**
- Spoke piece optimization using GSC data (impressions/clicks analysis) to identify cannibalization — actionable process for evaluating content performance before publication
- New workflow for image recommendations and video integration: GrowthX providing image tabs in Airtable docs, Webstacks adding video snippets via Descript post-publication
- Coffee Chats blog series reduces production friction by converting existing video transcripts to blog posts with light editing (1 per week target)
- Thought leadership content opportunities paired with educational pieces to differentiate and reduce cannibalization concerns

**To GrowthX Business Development:**
- Client-facing thought leadership examples (Nikan's AI/workflow efficiency video) demonstrating Webstacks' services — useful for case studies and reference conversations
- Growing content library (10-15+ Coffee Chat recordings in backlog) positions GrowthX as thought leader in design and workflow optimization
- Newsletter strategy identified as underutilized distribution channel for thought leadership and video content insights

**To Webstacks Partnership:**
- FAQ/TLDR experiment draft underway (Jakub + AI data science team) — test vector for measuring engagement impact across ~400 articles
- Video production scaling: Eric (Webstacks digital marketer) building 1-2 conversations per week; team exploring topics (visual branding, client dynamics, design thinking, enterprise vs. startup design)
- Social content flywheel: publish article → Eric auto-queues LinkedIn posts within 10 days; Coffee Chat blogs will plug directly into this existing workflow

---

## Overview

- New approach for spoke pieces: analyze by chapter, address cannibalization, merge/adjust as needed
- Launching "Coffee Chats" blog series using existing video content from internal discussions
- Experimenting with FAQ/TLDR sections in blog posts to test impact on engagement
- Enhancing articles with video snippets and thought leadership content for added value

---

## Key Topics

### Content Strategy for Spoke Pieces

- Chapter-by-chapter analysis of article performance using Google Search Console data (impressions and clicks)
- 0-0 entries (no impressions, no clicks) signal cannibalization — trigger for merging or replacing content
- Recently published articles given more time; articles 4-6 weeks old with no results warrant action
- Some articles can be quick fixes (adding thought leadership elements) rather than full merges
- Process: identify cannibalization signs in Chapter 1, decide whether to merge or adjust, then repeat chapter by chapter

### Thought Leadership and Video Enrichment

- Nikan's video example: AI-driven workflow efficiency (8-15 hours of work done in 30 minutes)
- Can create thought leadership posts paired with educational pieces; link from educational content to thought leadership
- LinkedIn posts and newsletter content from video recordings to extend reach
- Descript tool enables AI snippet extraction (70-75% hit rate) from video for article integration

### New "Coffee Chats" Blog Series

- 10-15+ existing recordings from Eric's conversations with Webstacks team members (design experts, engineers, etc.)
- Topics: visual branding, client dynamics, enterprise vs. startup design, understanding design thinking, AI workflows
- Workflow: GrowthX produces blogs from transcripts with light editing (1 per week), Webstacks adds video snippets via Descript post-publication
- Publish blogs first, then add video clips retroactively after Descript analysis
- Series branding: Webstacks designer (Philippines-based) to create series graphic; GrowthX to provide inspiration

### Image and Video Recommendations in Workflow

- GrowthX adding image recommendation tabs to Airtable documents (5-10 recommendations per article)
- Video recommendations to be flagged in Slack with opportunity notes rather than in document tabs
- Webstacks CMS has component blocks for easy video integration

### FAQ/TLDR Experiment

- Jakub drafted an experiment to test FAQ sections, TLDR sections, or combination on ~400 blog posts
- AI data science team refining logistics and experiment validity metrics
- Parameter unknown (possibly 50 of each blog type) — first draft, details TBD
- Jakub to provide refined version with implementation timeline next week; feedback async

### Social Content Flywheel

- Eric automatically queues LinkedIn posts based on published articles (10-day lag)
- Coffee Chat blog publication will trigger automatic social queuing without additional coordination
- Building a punch list of video opportunities to extract from existing content library

---

## Action Items

**Jessalynn Jones (GrowthX)**
- Create blog posts from coffee chat recordings. Use transcripts, light editing. Aim for 1 per week alongside spokes.
- Send inspo for coffee chat series graphic to Jesse by EOD. Include screenshots of similar series graphics.

**Jesse Schor (Webstacks)**
- Add coffee chat Gong recordings to Slack for GrowthX team access. Ensure public links work.
- Review FAQ/TLDR experiment draft from Jakub. Provide feedback on excitement/concerns async.

**Jakub Rudnik (GrowthX)**
- Run chapter-by-chapter analysis of spoke pieces using GSC data (impressions/clicks) to identify cannibalization candidates. Prioritize Chapter 1 first.
- Refine FAQ/TLDR experiment draft with input from AI data science team on logistics and test validity. Follow up async with refined parameters and timeline.

---

## Transcript

**Jakub Rudnik:** Hey, Rachel.

**Rachel Pasche:** Hi. Are you getting ready for the big move?

**Jakub Rudnik:** Yeah, packing three to five boxes a day. We did a lot over the weekend, so we're getting there.

**Rachel Pasche:** Did you guys do anything to the house you're moving into?

**Jakub Rudnik:** It's in good shape. It's old — all the houses in Cleveland are around 100 years old. We're moving into one of those, but the previous owners lived there for 25 years and the guy is very handy. He's actually sold me some tools and done a lot of projects to keep it in good shape. The bathrooms are a bit dated but it's more aesthetic at this point.

**Rachel Pasche:** I kind of like doing house projects. Our first project was painting the whole interior — it was this late 90s, early 2000s red that everyone had everywhere.

**Jakub Rudnik:** We had that in our condo. Someone had painted beautiful wooden built-ins red for no reason. We had to paint it all white because the red was impossible to remove.

**Rachel Pasche:** My parents had that red too.

**Jakub Rudnik:** Now we have millennial gray everywhere. The new house has 2000s beige, so we'll liven it up a bit. It's got good bones — the realtor said so.

**Rachel Pasche:** It's a beautiful house, though. I love all the crown molding.

**Jakub Rudnik:** Yeah, it's got good bones.

**Jesse Schor:** What's up, guys?

**Jakub Rudnik:** Hey, Jesse.

**Jesse Schor:** I'm on the East Coast right now visiting family between Philly and Jersey. Got my cheesesteak fixed yesterday. The houses here still have those old, preserved hardwood floors — the West Coast is so new everything.

**Jakub Rudnik:** Yeah, the West Coast is all new construction. Everything's gray and white. It's nice to have something unique to this house instead of every other house.

**Jesse Schor:** 100%. You don't get the character on the West Coast.

**Jakub Rudnik:** Okay, let's get into it. We have some stuff to chat through.

**Jessalynn Jones:** I can share the agenda. The big things today are talking through spoke pieces and thought leadership, now that we have the pillars and sub-pillars done. Jakub also has some recommendations for an FAQ and TLDR experiment.

**Jessalynn Jones:** Jakub, do you want to walk through the spoke analysis or should I?

**Jakub Rudnik:** You can talk through it. I think we're pretty aligned on the pillars. We did a deeper look at potential cannibalization based on how Google has treated the hubs. The topics you identified I feel pretty confident about. There's a lot of content on the site and Google is cannibalizing some things, so we've eliminated a couple because of potential cannibalization. There are spokes lined up if we want to continue. Your plan of merging a couple — like the timeline/composable piece — those specifically look like they could merge together into a stronger piece with no cannibalization. Some others can be tweaked slightly or we should wait a few weeks. I've seen pieces with no impressions just wake up one day and start working. So there are probably three different paths forward with about ten articles.

**Jesse Schor:** For recently published articles, we should give them more time. For anything published four to six weeks ago with no impressions, then we make the call. I think a chapter-by-chapter approach works best. If we look at Chapter 1 in GSC — anything with impressions and clicks, keep running with those. Anything with 0-0 (no impressions, no clicks) is our cannibalization trigger.

**Jakub Rudnik:** Exactly. For Chapter 1, run it through GSC. If anything has impressions or clicks, keep going. If there's 0-0, that's the cannibalization trigger — move it into a merge. Otherwise, we have enough spokes. A chapter-by-chapter approach works each week. Five articles including a hub or pillar per chapter. Some could be quick fixes rather than full merges. We could do an educational piece with thought leadership elements if it's targeting something slightly different. First step is identifying Chapter 1 items with cannibalization signs, then deciding if it's a merge or quick adjustment.

**Jesse Schor:** I like that. For articles with traction already, let's fold everything into them. I want to share a video of Nikan, our head of design, talking through a customer story and AI workflows. It's less technical and more about how AI took what normally takes 8-15 hours and does it in 30 minutes. Maybe there's a thought leadership angle we can take that's less keyword-driven but enriches existing articles. We could chop it up for video media or create it as a thought leadership post and incorporate it.

**Jessalynn Jones:** If that's the one you shared before, we actually pulled the transcript and added it to our workflow artifacts. We haven't done a true thought leadership piece based on it yet, so we can add that.

**Jakub Rudnik:** The Nikan example — if there's obvious opportunities or we're writing that article, we should definitely link from the educational side. That could solve our cannibalization issues if we change titles slightly but link from the educational piece. We could use the organic traffic from the educational piece and surface what Webstacks is doing with that tactic. And if he's got that type of recording, let's create the article, but also do some LinkedIn posting — very results and numbers-driven, probably video and post together. Clips from the video can be used on the blog and in the thought leadership piece. That's perfect newsletter content too. So there's a flywheel here even with potential cannibalization.

**Jesse Schor:** We're still pulling from your published content in our social. I want to keep that as the first line. Our social backlog is there. If we publish something and incorporate it into the article, it's less coordination — we just know it'll get queued up in our social content calendar.

**Jessalynn Jones:** Are you guys already doing a series with these coffee chat recordings? Like a blog wrap-up with the video?

**Jesse Schor:** We're not doing a series now. But there's a stockpile of these videos. Eric's been having one or two conversations per week building up content faster than we can use it.

**Jessalynn Jones:** If you have 10-15 recordings, that's a super easy quick win. Create a "Coffee Chats" blog series, pull the transcript with light editing. You already have the content, which is rare.

**Jesse Schor:** I like that. Right now we're building up conversations with Eric, getting reps in, finding topics people want to talk about. It's almost like we can't get them out fast enough. I have more I can share.

**Jessalynn Jones:** Do they need production or can we just take them and create a series?

**Jesse Schor:** We use Descript with an AI snippet tool — about 70-75% hit rate. If you guys take the transcript and put it together, we could do it in reverse: feed the full video and article to Descript and ask for the best snippets for each section.

**Jessalynn Jones:** Do you want us to produce the blog series?

**Jesse Schor:** I'm not opposed to handing them off. I just shared the ClickUp with the Gong recording links — they should be public.

**Jessalynn Jones:** That's a super easy quick win. You have the content stockpiled. How should we handle workflow — produce the blogs, send you a couple at a time, then you go back in and add video snippets?

**Jesse Schor:** Yeah. That's already our workflow. Eric doesn't interact with you guys — he sees what gets published and auto-queues LinkedIn posts at about a 10-day run rate. We do the same with Coffee Chats. Eric handles the Descript work. Right now the bottleneck is him chopping it up and trying to find articles to link to. If you guys start with the article and publish it, then we add the videos a week or two later and update.

**Jessalynn Jones:** So we produce the blogs, publish them, and you go back in and add video illustrations?

**Jesse Schor:** I think so. That helps us get Descript snippets easier — we feed the video plus the article with a prompt asking for the best snippets for each section. We can test with one next week.

**Jessalynn Jones:** If we're doing a series, could your designer mock up a graphic?

**Jesse Schor:** Great idea. Can you share some inspiration?

**Jessalynn Jones:** I can send screenshots by end of day.

**Jesse Schor:** My designer is in the Philippines — good English, always available. With some examples, that's the easiest way to get what we need.

**Jessalynn Jones:** I'm so excited for this. You already have the content stockpiled, which is super rare. This is a great opportunity to showcase expertise and build community.

**Jesse Schor:** That's my goal. I want more of these conversations, direction on what conversations to have. The more we build up, the more data we gather to share with you guys. Better content comes out.

**Jessalynn Jones:** For the next couple weeks, we'll do the spokes like we talked about, then weave in one Coffee Chat per week. Does that sound right?

**Jesse Schor:** I like it. Let me know early next week if you want me to look at anything ahead of time or if we should coordinate on getting the videos together.

**Jessalynn Jones:** Sounds good. Well, have a good rest of your day, all.

**Jakub Rudnik:** Great job.

**Jessalynn Jones:** See you guys. Bye.

---

## FAQ/TLDR Experiment Discussion

**Jakub Rudnik:** I can do a one-minute overview on the FAQ/TLDR experiment. I drafted an outline with ChatGPT for testing FAQ sections, TLDR sections, or a combination on ~400 blog posts. I'm working with my team on implementation. We have an AI data scientist working on experiment validity. Logistics and parameters aren't finalized yet. Feel free to read through and give feedback. I'll have more next week and follow up async.

**Jesse Schor:** I'll take a look through this. We can talk async.

**Jakub Rudnik:** It's still a work in progress. Let me know if anything stands out — whether it's very exciting or seems way off.
