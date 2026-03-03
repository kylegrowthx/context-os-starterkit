# Airbyte <> GrowthX Weekly Sync

<metadata>
date: 2025-07-02
time: 15:30 UTC
duration: 19 minutes
organizer: David Galic (GrowthX)
participants: Jakub Rudnik (GrowthX), David Galic (GrowthX), Mario Moscatiello (Airbyte), Nithin M (Airbyte)
speaker_note: Speaker "6 - Grand Canyon" identified as Nithin M based on technical discussion of Gong call analysis and BigQuery data infrastructure, consistent with engineering/data team role.
fathom_recording_id: 71834212
fathom_url: https://fathom.video/calls/340574539
share_url: https://fathom.video/share/SxQK8CsfxR6ytxnK9ywUCXBYx2iMy88z
source: fathom
enriched_on: 2026-03-03 14:32 UTC
</metadata>

---

## Summary

GrowthX and Airbyte aligned on a phased approach to scaling content production from 40 to 80-100 pieces/month, with a focus on two work streams at a time while Airbyte completes its website redesign (expected in 1-2 months). Key strategy shifts include balancing LLM-optimized content with traditional SEO/editorial, leveraging Airbyte's 7,000 Gong calls for topic research and content inspiration, and implementing visual content improvements (charts, graphs, flowcharts) to enhance readability and LLM comprehension. The team is also moving forward with integrating AI-generated visuals and optimizing image alt text for search performance.

---

## Context

GrowthX is running a content marketing engagement with Airbyte, a leading data integration platform. This weekly sync brings together Jakub Rudnik (GrowthX) with Airbyte's Mario Moscatiello and engineering/data team (Nithin M) to align on content strategy, production scaling, and resource planning. Airbyte is investing heavily in content as part of their growth strategy, with a major website redesign underway. The relationship is structured around GrowthX delivering scaled content production while Airbyte leverages its proprietary customer call data (Gong calls) and technical infrastructure to inform strategy and optimize for both traditional SEO and emerging AI/LLM visibility.

---

## Relevance

**To GrowthX Delivery:**
- Content production scaling methodology: phased two-stream approach reduces risk while managing editorial quality and team capacity during client transitions
- Integration of Gong call data as content ideation source: new playbook for turning customer conversation data into topic validation and long-tail keyword targeting
- Visual content systems development: frameworks for programmatic creation of charts, graphs, and flowcharts with AI assistance to improve both user experience and LLM comprehension
- Balancing programmatic/PSEO with traditional editorial: proven need for dual-track content strategy rather than pure AI-optimized focus

**To CheckThat:**
- LLM visibility strategy validation: live client case study of balancing traditional SEO with AI overview optimization, targeting long-tail keywords and commercial-adjacent content
- AEO implementation in practice: Gong call analysis as systematic method to identify prompt patterns and customer language for AEO targeting
- Content chunking and structure for LLMs: Airbyte's content being actively optimized for token efficiency and standalone chunk comprehension
- AI-generated visual content: testing ground for scaling visual content creation and assessing LLM utility for content ideation

**To GrowthX Business Development:**
- Account expansion signal: Airbyte planning to 2-3x content production (80-100 pieces/month), indicating strong engagement and confidence in GrowthX's delivery
- Website redesign creates content opportunity: 1-2 month timeline creates structured engagement for landing page and structural content work post-launch
- Technical sophistication: Airbyte's advanced data infrastructure (BigQuery, S3 integration, Airbyte connector for Gong) enables sophisticated content strategies and partner alignment
- Reference potential: Live demonstration of scaled content delivery with AEO/LLM focus positioning for similar SaaS buyers

---

## Overview

- Content production scaling from 40 to 80-100 pieces/month, but Airbyte can only execute two work streams simultaneously to avoid bottlenecks
- Website redesign (1-2 month timeline) is the top priority; landing page updates should be deferred until the new site is live to avoid rework
- Balance required between LLM-optimized content (prompt research, long-tail keywords) and traditional editorial/commercial content (lists, versus pages) — both remain valuable
- Gong call analysis (7,000+ calls) identified as the first strategic work stream to pursue, with infrastructure ready (BigQuery, S3, Airbyte connector) for data extraction
- Visual content improvements critical: charts, flowcharts, graphs, and tables enhance both user experience and LLM token efficiency when properly chunked
- 19 articles already published with 15 more in flight; recent formatting issues resolved and team aligned on content structure

---

## Key Topics

### Content Production Scaling

- Potential increase from 40 to 80-100 pieces/month; Jakub and Mario evaluating resource capacity
- Bandwidth constraints: Airbyte cannot execute everything simultaneously due to competing priorities
- Mario's recommendation: focus on 2 work streams at a time to maintain quality and avoid team overload
- Airbyte has internal resources (Kusha, Mario) available to assist with content review and scaling editorial capacity

### Website Redesign

- Major priority: Airbyte rebuilding entire website with expected completion in 1-2 months (currently iterating on design and branding)
- Blog changes planned as primarily cosmetic initially, with deeper structural discussions deferred with Nithin and Mario
- Landing page updates should be deferred until new website launches to avoid duplicate work; Mario will prep content in advance for implementation post-launch

### Gong Call Analysis

- 7,000+ Gong calls available for customer conversation analysis and topic/prompt research
- Airbyte's data infrastructure ready: can export to S3, BigQuery, or Snowflake; currently stored in BigQuery
- Unique advantage: Airbyte can use its own Airbyte connector for Gong to manage data pipelines (eating own dog food)
- Current BigQuery formatting is suboptimal; Nithin suggests dumping calls in unstructured format and collaborating with GrowthX engineering to develop extraction and analysis processes

### Content Strategy and LLMs

- Dual-track strategy necessary: LLM-optimized content (targeting prompt research, long-tail keywords where AI can provide brand visibility) AND traditional editorial/commercial content (both remain valuable)
- Prompt research matters: target prompts about tools, software, and platforms where Airbyte brand can appear in LLM responses (versus generic "how-to" questions that rarely mention brands)
- Commercial and commercial-adjacent content still converts: software lists, alternatives, versus pages, and intentional topic clustering show real value
- Avoid glossaries and pure upper-funnel content: AI overviews dominating these categories; focus on a level or two below (supporting content for commercial pieces)
- Intentional content clustering and tight interlinking supports both SEO and LLM comprehension; supporting articles add credibility even without direct clicks

### Visual Content Improvements

- Visual content critical for both user experience and LLM token efficiency: charts, flowcharts, tables, and graphs are better than bullet points, which beat paragraphs
- AI-generated visuals in-article: featured images follow template; in-article images (graphs, charts) can leverage AI for faster creation
- Jakub shared inspiration from high-growth content creator using sophisticated visual layouts and chunking strategies
- Alt text optimization for keywords: images drive clicks from Google Image Search even without ranking improvements; strategic alt text amplifies this benefit
- Collaboration needed: David (GrowthX) and Jakub to develop systematic patterns for identifying which content types map to which visual elements, then execute at scale
- Repurposing internal assets: existing landing page visuals, competitor inspiration, and LLM ideation sessions to identify what can be visualized from article content

### Current Content Progress

- 19 articles already published and live
- 15 new articles in progress and being delivered (with a batch outstanding that the team is working through)
- Recent formatting issues resolved; team aligned on content structure and ready to continue steady output (daily or near-daily delivery)

---

## Action Items

**Jakub Rudnik (GrowthX)**
- Share meeting transcript with George to brief on Gong call analysis strategy and engineering team approach; coordinate order of operations for data extraction and processing

**Mario Moscatiello (Airbyte)**
- Review strategy document sent by George on Monday, provide feedback (pending completion due to short week and onboarding of new VP Finance)
- Discuss with Nithin which work stream to pick beyond usual article production, report back to team with prioritization recommendation

**Nithin M (Airbyte)**
- Review 3 new articles submitted by David Galic, provide feedback within one business day
- Have longer discussion with Mario about structural changes and editorial strategy for blog during website redesign

**David Galic (GrowthX)**
- Experiment with AI-generated charts and graphs for in-article visual content; develop repeatable process and patterns for identifying which content types require which visual formats

---

## Transcript

**Jakub Rudnik:** I think we're still finalizing what work streams to go after with the strategy sprint, and we can jump into the day-to-day, too, so I don't want to go out of sequence too much, but curious how, you know, if we're doubling our content production on our side, if that's, like, one of the big pushes, how do you see the bandwidth there, or maybe it's a breakdown where we're doing more programmatic and it needs less review?

**Jakub Rudnik:** Like, what, what's going to be your ideal state as I'm talking with George and Marcel, and then also, you know, trying to figure out resources on with David, you know, if it was 80 or 100 pieces of content a month instead of 40, what, how do you, how do you think about it?

**Nithin M:** Yeah, so, my take is, let's say, whatever we are doing, that's based on some prompt research where we want to showcase Airbyte, right?

**Nithin M:** And if you look at the data, if you type, like, how to do this and what to do this — obviously, your brand won't appear there in most of the cases, right?

**Nithin M:** So your question should be related to tools, software, platforms, and then only you can see your brands.

**Nithin M:** Other than that, if you have an article on a similar topic, that might get citations, but most of the cases don't mention your brand.

**Nithin M:** And if brand doesn't get mentioned, you're not getting visibility, right?

**Nithin M:** So, we need to go one step back and see what are the kind of prompts that people are asking.

**Nithin M:** There are tools to check some kind of data, but obviously there is nothing called search volume anymore in the platform thing, right? But yeah, from that trend, we can finalize some prompts.

**Nithin M:** Like topics and write those. Also, I feel like we have discussed this, like we have almost 7,000 Gong calls.

**Nithin M:** So customers talk about multiple things.

**Mario Moscatiello:** What are we talking about, sorry?

**Nithin M:** So this is about work streams, what we discussed with Marcel and George.

**Mario Moscatiello:** Maybe just taking a step back on that. I have one question: how do we balance the current engagement with the different work streams? Like before we get into anything, we can sort of...

**Jakub Rudnik:** Yeah. So that was really helpful context, Nithin. I think that goes into the topics we're doing on this side, but also... So Mario, I was kind of asking as people were coming on. My question for Nithin was about resources. As we're doing a lot of content right now, how are you thinking about resourcing that review or what ability to scale in that direction?

**Jakub Rudnik:** So Mario, I know we're still finalizing things with George, Marcel, and you trying to align those. Are there recommendations on the different work streams? Like, there's the Gong call analysis, there's some new editorial that would just scale, but also a few different programmatic pieces. We can also do landing pages. I'm trying to understand how much editorial scale can you all take on? Like, if it just looked like this current engagement but expanded, I'm just trying to understand what that is and make sure what we're recommending doesn't go beyond that capacity.

**Mario Moscatiello:** Yeah, I think we can't do everything at the same time. That's the one thing I would say, especially because we're still working through some changes internally. The main thing we're working on is rebuilding the entire website. You know how these things go — we've had to restart the project a couple of times with design changes and the brand not being ready. So I think for a bunch of that work, I wouldn't want to be investing in redoing all the landing pages and those work streams until we have the new website live. We could technically do it earlier, but it would just be a lot of double work in my opinion.

**Mario Moscatiello:** So that's one where I'm like, great, let's prep and have everything ready, then we can do it once the website is live. I think it's going to be in the next month or two, so that's one for sure.

**Mario Moscatiello:** In my mind, I think we can start adding a couple of things. We have other people on the team that can help me review the content — Kusha, myself. I can do a bit of review if needed. So we can scale, but we can't do four things at the same time. I think we want to keep it where we're doing two things at a time and building it like a roadmap, you know.

**Jakub Rudnik:** Yeah, so that was very helpful. Yeah, and a couple of things...

**Mario Moscatiello:** Yeah, for the Gong calls, we have a data team, so we can literally drop everything into an S3 bucket or BigQuery or Snowflake — wherever it needs to be, we're pretty advanced. And I think as part of the strategy sprint, we get input from you on the engineering side as well. So we can have our teams talk and figure out how to dump these calls. But we literally have an Airbyte connector for Gong. And so we can use our own technology to dump the calls wherever we need, which is kind of the advantage. We actually have them all in BigQuery already — I just think the formatting is terrible.

**Mario Moscatiello:** So I'd rather dump them in an unstructured way and then figure out with you guys how to extract the text and so on. For that to happen, I would work with our data team.

**Jakub Rudnik:** Yeah, for sure. That makes sense. I'll bring this — the transcript of this — which would be really helpful to bring to George and what he's working on with our engineering team on how they're thinking about that in the order of operations.

**Mario Moscatiello:** And I know George sent me the document on Monday where we have leadership team this week — onboarding a new VP Finance and stuff. So I'll get to it, but a couple days with a short week is just challenging, but yes.

**Jakub Rudnik:** Yeah, no problem at all. So let's do some of the week-to-week things. We'll have that, continue that conversation. I'll bring that over to George — he has even more context. So you can update anything coming out of that.

**Jakub Rudnik:** Yeah, we've pushed 19 different articles. We still have a batch outstanding, but the team is working on those updates to me. We'll keep those coming every day or so. David's working even — we were in the States working through Friday, so we'll see some of those. But I'm sure you all will be out Friday with the long weekend and delivering 15 new... I'm not sharing my screen, I just realized, so bear with me. Any questions on the content that's come in or any feedback before I jump to the next item?

**Nithin M:** Oh, I think David has already submitted three articles today, so I'll review those and share feedback by another day to him, yeah.

**Jakub Rudnik:** Awesome, thank you. Yeah, should all be pretty business as usual. Just get that batch reworked and the formatting. David, what do you have on the formatting progress? What do you want to talk through there?

**David Galic:** I just want to check in on whether everything's looking good. While I was on vacation, there was a little bit of a formatting problem, but it looks like everything's been ironed out. Just want to make sure we're good, everything's looking the way it should, and we can just move forward.

**Nithin M:** Yeah, I think the content structure is good right now. After the last big discussion, we're aligned on the same thing.

**David Galic:** Yeah, cool.

**Jakub Rudnik:** And then, where do you want to take the conversation on visuals, David?

**David Galic:** Yeah, I know Nam was telling me that he's trying to figure out something. I was just wondering what this is going to look like. Do we want graphics? What's the ask for these kinds of improvements in the visuals?

**Nithin M:** Okay, so for featured images, we already shared that template, right? And then for in-article images — graphs, charts — those I think we can use AI to create.

**David Galic:** Okay, then yeah, we'll check that out and see what it looks like.

**Nithin M:** See if we have support for that.

**Jakub Rudnik:** Yeah, I shared this with Nemanja last week, David — apologies I didn't pass it over your way. This is one of my friends who runs content. I use them for a lot of inspiration. They've grown every single year like crazy. But this is what I was envisioning, and for every piece of content, you have to understand the context — how to show something visually that makes sense for that article. We shouldn't force things in. A picture tells a thousand words, that's legitimate. A basic flowchart is so much better than bullet points, which are better than paragraphs. It's really good.

**Jakub Rudnik:** We spent a lot of time at the director onsite talking LLMs. You all are probably the most advanced client I'd speak to on this stuff, but Dave is working on a directive for GrowthX in general. He's experimenting with things, but one thing we're really bullish on is chunking content. If we're publishing 3,000-word articles, not every word is being scraped or examined. We need to make sure each chunk works on its own — the number of tokens LLMs use to go through content breaks into chunks and should understand each piece individually.

**Jakub Rudnik:** Images are a good example, but also how they bring in different snippets. We do some of that already, but we should continue with tables and other things. The goal is to repurpose content and really improve user experience and readability. That's stuff we should do anyway for the user, but it'll have the double purpose of being valuable for LLMs. David, that's how I'd think about it. I haven't experimented with execution yet, so we should collaborate on that, see what's in place, but build something as necessary.

**Jakub Rudnik:** There should be patterns we can recognize — this type of content typically turns into this type of images. We should use anything you already have on landing pages, or competitor inspiration. Even conversations with an LLM about what could be visualized from content can give inspiration. The number one thing is what actually adds value to that piece of content.

**Jakub Rudnik:** We should make sure our alt text and other things are optimized for keywords. With these images, you increase clicks from Google Image Search even if you don't improve rankings — that's where people come in looking for these things. They have value for LLMs, Google Image, time on page, and more.

**Nithin M:** Yeah, that totally makes sense.

**Jakub Rudnik:** David, let's work through what that looks like and see what we can repurpose internally already, then figure out next steps if we need them.

**Jakub Rudnik:** Anything else on the image side from anyone?

**Nithin M:** No, I think we're good here. So next step: I'll review the already written articles today, and Nithin and I will chat about which work stream we can pick other than our usual articles. Then we can get back and chat with you too.

**Jakub Rudnik:** Okay, perfect. Those are the big things.

**Mario Moscatiello:** Yeah, my main question is — maybe it's for George — how many things do you recommend we do at the same time? I need to understand the structure better. But I think the Gong calls analysis would be the first thing we want to tackle because I think that's going to give us a lot of answers for a lot of the content.

**Mario Moscatiello:** Another question: I understand the push for LLM visibility, but at the same time, I still think we should write normal content, right? How do we want to balance that?

**Jakub Rudnik:** Yeah, I agree. Both sides are true. Answer the right questions and target long-tail where there's not good content already, and people are having deeper conversations with LLMs — that tracks. It's similar to how we think about zero-search-volume stuff. If we find something in Gong calls or hear from customers or see conversations on social, even without the exact keywords, we should create that content because people are having that real conversation. They're looking but might not know the exact term. I'm a proponent of that — I've seen it work really well. It converts, not just drives traffic, but drives conversions because you're creating it intentionally.

**Jakub Rudnik:** We're still seeing clicks and volume, though it's going down. Commercial and commercial-adjacent is where I want to go — software lists, alternatives, versus pages. Those work. We did things at Scribe with no search volume but where people were calling it a tool, and we got more clicks that converted. It's a pairing of those two things.

**Jakub Rudnik:** I wouldn't recommend glossaries to clients anymore because AI overviews are destroying those. But a level or two below the glossary feeling, there's still clicks. AI overviews haven't taken over yet — there's good value. What I want to revisit is clustering and being intentional with content. A lot of that's in place, but making sure we're tight because supporting articles provide credibility above commercial pieces, tightly interlinked. Even if clicks aren't there and it's just a citation, not a click-through, there's support for other articles and credibility. It's a bit of both — almost everything with SEO — but it's about intentionality.

**Mario Moscatiello:** We shouldn't discount that people browse our website. We want content that's... we don't have an internal content team. Yes, we do leadership content, but there's always a balance — 70/30, 80/20. This is why I originally picked the editorial work stream versus PSEO specifically. I think we can balance both, but keep it in mind for strategy moving forward.

**Jakub Rudnik:** Yeah, that makes sense. One question — on the website redesign or restructure, anything you're thinking about changing on the editorial or blog front? Anything to be aware of?

**Mario Moscatiello:** On the blog, it'll be mainly cosmetic for now. Then Nithin and I are going to have a longer discussion on what structural changes we want to make.

**Jakub Rudnik:** Okay, sounds good. Pull me and the team in at any point. I'm sure you would anyway, just call that out.

**Mario Moscatiello:** Sure, that's a good point.

**Jakub Rudnik:** Okay, so I'll send this over to George and connect, and then...

**David Galic:** Just want to give my two cents on the new stuff we've been doing. I was a little skeptical with just a question being the whole thing, but so far so good. The output has been pretty interesting. I was afraid it might be short and not as involved, but I'm really looking forward to you checking out the three I've put together. I think it's pretty good. It gives us an opportunity to answer questions and we can put everybody into there as well. It came out better than I expected.

**Nithin M:** Yeah, yeah.

**Mario Moscatiello:** That's great to know. And yeah, as I said, I think it's a great structure, but at the same time, let's still push some content that's normal.

**Jakub Rudnik:** Okay, cool. Right on.

**Nithin M:** Talk soon. A calendar is a good mix of content — some for LLM, some for technical and normal.

**Mario Moscatiello:** Buzz. Yeah.

**David Galic:** Cool.

**Mario Moscatiello:** Awesome. Thanks.

**Jakub Rudnik:** Thanks. Have a good one.

**Mario Moscatiello:** Thank you.

**Jakub Rudnik:** Bye.
