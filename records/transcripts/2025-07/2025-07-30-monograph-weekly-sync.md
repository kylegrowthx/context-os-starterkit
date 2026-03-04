# Monograph Weekly Sync

<metadata>
date: 2025-07-30
time: 17:01 UTC
duration: 31 minutes
organizer: team@growthxlabs.com
participants: Aida Knezevic, Jo Kaminska, Matthew Panzarino, Chris Morgan, Robert Yuen, Gary DeBerry
fathom_recording_id: 77463761
fathom_url: https://fathom.video/calls/365528780
share_url: https://fathom.video/share/htWnJpGfAmdX_xEKnxka5CKszGWRkhnT
source: fathom
enriched_on: 2026-03-03 00:00 UTC
</metadata>

---

## Summary

GrowthX and Monograph aligned on content delivery, audience research, and LLM visibility tracking. Four blogs are ready to publish this week after incorporating feedback from Gary DeBerry; GrowthX gained access to Monograph's Gong call recordings to extract engineering-specific pain points and competitive insights. Matthew Panzarino joined the GrowthX team as Chief Content Officer and committed to optimizing workflows, while the team set up Scrunch dashboard tracking showing 23% LLM presence across ChatGPT, Claude, Gemini, and Perplexity. Monograph is shifting messaging toward "built by architects for architects" with more aggressive positioning against PE-owned competitors (BQE, Dell Tech), and GrowthX will create an LLM text file for better AI crawling and integrate Scrunch data into Looker for client visibility.

---

## Context

Monograph is a founder-led project management and operations tool built specifically for architects and engineers. GrowthX is in the delivery phase of a content marketing engagement, having completed a sprint to understand Monograph's business, products, and market positioning. This was a weekly sync check-in following Matthew Panzarino's recent joining of GrowthX as Chief Content Officer. Matthew previously spent 10 years leading TechCrunch editorial operations and was brought in to help productize GrowthX's content delivery pipeline and accelerate Monograph's publishing cadence. The meeting focused on executing content strategy, gathering audience insights, and tracking LLM visibility — a directional metric for how often Monograph appears in responses from AI models when architects and engineers ask relevant questions.

---

## Relevance

**To GrowthX Delivery:**
- Matthew Panzarino joining as Chief Content Officer signals deep investment in content quality and workflow optimization; he brings 10 years of TechCrunch editorial experience and explicit focus on "breaking down components of quality content" to enable faster, AI-assisted production at scale.
- Monograph has asked GrowthX to avoid mentioning specific details around onboarding and data migration processes in blogs, flagging that these are fluid and subject to change — requires artifact updates and editorial discipline across future pieces.
- GrowthX has access to Monograph's Gong call recordings for engineering-focused discovery calls, enabling persona development and audience research for more targeted positioning.
- Gary DeBerry (Monograph) is actively reviewing content in Google Docs and flagging specific feedback on spelling, competitor names, and phrasing — establish feedback loops in the workflow to ensure consistency before publishing.

**To CheckThat / AEO:**
- Scrunch LLM visibility dashboard shows Monograph at 23% presence across ChatGPT, Claude, Gemini, and Perplexity, with largely positive sentiment — Matthew emphasized this is early-stage directional intelligence, not precise tracking, and noted diminishing returns beyond ~12 Gong calls for pattern matching on pain points.
- GrowthX is creating an LLM text file (similar to a sitemap for LLMs) for upload to Monograph's Webflow site to improve AI crawling and visibility.
- Chris Morgan flagged interest in understanding which page types and content forms (customer quotes vs. brand narration) are most effective for LLM visibility, and whether Monograph appears in non-software business-related queries — potential expansion of Scrunch prompts and GA4 integration could provide that data.

**To GrowthX Business Development:**
- Monograph is preparing major messaging shift: moving from general positioning to "built by architects for architects" with aggressive comparisons against PE-owned incumbents (BQE, Dell Tech) following growing M&A activity in the space.
- Robert Yuen expects increased pipeline activity as the new narrative launches; success metric is seeing more competitor mentions (PE-backed vs. founder-led) in late-stage sales funnels.
- Account health strong: Monograph is pushing to increase content cadence and integrating Scrunch insights into Looker dashboard for internal analytics — signals of maturing engagement and scaling investment.

---

## Overview

- Four new blog posts to be published this week after incorporating feedback
- GrowthX team granted access to Monograph's Gong call recordings for deeper audience insights
- Scrunch dashboard set up to track Monograph's LLM visibility, showing 23% overall presence
- Monograph to refine positioning as "built by architects for architects" and highlight advantages over PE-owned competitors

---

## Key Topics

### Content Update and Feedback

  - Four new blogs delivered last week, to be published after incorporating feedback
  - Avoid mentioning specifics about onboarding or data migration processes in content
  - Gary provided detailed feedback in Google Docs, including spelling corrections for competitor names
  - Jo is handling the changes and incorporating feedback into artifacts

### Audience Insights Collection

  - GrowthX team granted access to Gong call recordings for engineering-specific insights
  - Chris to set up generic login for GrowthX team to access Gong system
  - Aim to analyze about a dozen calls for pain points and competitor comparisons

### Scrunch Dashboard Implementation

  - Dashboard tracks LLM visibility across ChatGPT, Claude, Gemini, and Perplexity
  - 380 prompts used so far, generating almost 2,000 responses
  - Monograph shows 23% overall presence, with largely positive sentiment
  - Plans to integrate Scrunch data with Looker dashboard for client access

### LLM Optimization Strategies

  - Creating LLM text file for improved website crawling by AI
  - Instructions for uploading the file to Webflow will be provided
  - Exploring integration with Google Analytics for more detailed page-level insights

### Future Content Direction

  - Upcoming narrative shift to position Monograph as "built by architects for architects"
  - More aggressive positioning against PE-owned competitors
  - Aim to increase visibility of Monograph in late-stage sales funnels
  - Maintain current messaging for engineering-focused content

---

## Action Items

**Chris Morgan (Monograph)**
- Set up generic Gong login for GrowthX team (matthew@growthx.ai, mariana.marins@growthx.ai, jo@growthx.ai, team@growthxlabs.com)
- Check Webflow SEO section for LLM text file upload capability, report back to GrowthX team

**Jo Kaminska (GrowthX)**
- Make adjustments to KPI software blog post based on Gary's comments, update artifacts

**Gary DeBerry (Monograph)**
- Share Google Doc about new narrative (architect-built, PE comparison) with GrowthX team

---

## Transcript
**Aida Knezevic:** There were notes.

**Aida Knezevic:** think Panzar got the notes, which was helpful at least, but yeah, it was disappointing for her.

**Aida Knezevic:** All right.

**Aida Knezevic:** I actually wanted to start the meeting off by introducing Matthew.

**Aida Knezevic:** He's our chief content officer, but he is very much concerned with content quality for our clients and also improving the existing workflows to make them work better for you.

**Robert Yuen:** Okay.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Yeah.

**Chris Morgan:** Great to meet you.

**Matthew Panzarino:** Nice to meet you.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** As Aida mentioned, like I'm all about the workflows, making sure that the pipelines are set up well.

**Matthew Panzarino:** You you folks are kind of coming out of the sprint process where we're like, hey, what do we want to do for you?

**Matthew Panzarino:** And trying to get an understanding of the company.

**Matthew Panzarino:** I have watched all those calls and read all of your documentation.

**Matthew Panzarino:** I am also familiar with the company.

**Matthew Panzarino:** I think we announced your series B on TechCrunch by 2021.

**Matthew Panzarino:** But I am Matthew Panzarino.

**Matthew Panzarino:** previously ran TechCrunch.

**Matthew Panzarino:** I was the editor-in-chief from 2013 to 2023.

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** For about 10 years, serving editorial operations there across, of course, our news gathering org, then TechCrunch Disrupt, Startup Battlefield, and dozens of other editorial products.

**Matthew Panzarino:** So I joined up at GrowthX because I got to talking with Daniel and Marcel, got connected with them, and we were thinking the same way about the atomization of content and how AI can sort of enable people to produce quality content at scale, thinking about the breaking down of the components that make up quality content, and understanding and articulating how we can enable people to do that faster and better with AI.

**Matthew Panzarino:** So that's why I'm here, and why I'm here with you is to kind of make sure that this pipeline that we've created gets productized well to smoothly deliver content for you.

**Matthew Panzarino:** I know you've talked a little bit about wanting to increase cadence of delivery, which we can do, which is to make sure that the wheels are oiled and running smoothly.

**Matthew Panzarino:** The gears are interlocked properly, and that's my job, so I'm going to be generating content for you, editing it.

**Matthew Panzarino:** I'm presenting it to you over the next couple of weeks and making sure that you're really happy with it and making sure any tweaks needed that are necessary get done.

**Matthew Panzarino:** So that's why I'm here.

**Robert Yuen:** Pleasure meet you.

**Aida Knezevic:** Nice.

**Aida Knezevic:** All right.

**Aida Knezevic:** Perfect.

**Aida Knezevic:** So I wanted to kick things off by just giving you a quick content update.

**Aida Knezevic:** So last week we delivered four new blogs.

**Aida Knezevic:** You have reviewed them.

**Aida Knezevic:** The plan is to resolve any outstanding comments, incorporate them into the artifacts, and then we're going to publish the four this week.

**Aida Knezevic:** Yesterday I had a really nice conversation with Ashish, your CPO.

**Aida Knezevic:** He gave me a lot of good insights on the engineering audience.

**Aida Knezevic:** And there's significant, like, there's some overlap, but it gave us a good overview into, like, some of the differences between the audiences, notably how engineers often deal with higher volumes of work than architects, so that's one thing that was a really big takeaway.

**Aida Knezevic:** He did mention that, you know, for more sort of granular insights, it would be helpful to speak to someone from sales, and I know that sales teams are usually really busy, but I was wondering if you're using Outreach or Gong or any type of other platform that has some recordings that you could share with us, or at least transcripts or summaries.

**Robert Yuen:** Yeah, we are using Gong, so there's a ton of call scripts.

**Aida Knezevic:** So it would be helpful to get a couple of good calls where we just can get a better understanding of the engineers' pain points and why they come to Monograph, and like, when they're talking to your sales team, like, what are the issues that they bring up, what are the problems that they want to solve, things like that.

**Robert Yuen:** Yeah.

**Aida Knezevic:** Or like, what's lacking in their currency?

**Aida Knezevic:** Like if they're using Google Sheets, we want to know why that doesn't work specifically.

**Robert Yuen:** Or if they're using a different tool, like we also want to understand like why they hate it.

**Robert Yuen:** Yeah.

**Robert Yuen:** Chris, can you do me a favor and just like ping Sam, Sam R, and grab any type of Gong recordings that are engineering specific and then pass that over?

**Chris Morgan:** Sure thing.

**Chris Morgan:** So how much is useful for you?

**Chris Morgan:** Are you thinking like three, because you listed spreadsheet and then like a competing tool.

**Chris Morgan:** Can you help us?

**Chris Morgan:** Because we can isolate down to segment and we can also isolate down potentially to competing solution.

**Chris Morgan:** But give me a sense for like, if you were to spec out what's the minimum you want to know, that's going to be insightful.

**Chris Morgan:** How would you describe it?

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Panzar, do you want to weigh in?

**Aida Knezevic:** I think you have probably a good idea of like the workflow and how much context it needs.

**Matthew Panzarino:** Yeah, I think in terms of pain points here, this would inform personas and.

**Matthew Panzarino:** And also the company context for us.

**Matthew Panzarino:** Those are the two primary artifacts that we're going to.

**Matthew Panzarino:** What we want to know is just keep things simple.

**Matthew Panzarino:** What are the top three things that in your top three solutions engineers are moving away from and towards Monograph?

**Matthew Panzarino:** In other words, what are the top three things they hate and don't like?

**Matthew Panzarino:** And whether that's the form of a solution or a major pain point, those are the insights we'd like to glean.

**Matthew Panzarino:** And we need to start there.

**Matthew Panzarino:** So as one example, do they live in Sheets and they hate it?

**Matthew Panzarino:** Or do they use an additional tool, but it doesn't do, for instance, like personnel time management, but it does do payments management.

**Matthew Panzarino:** And they like one solution for both.

**Matthew Panzarino:** That sort of thing.

**Chris Morgan:** So one thing we could do is like I could take all of our closed one engineering customers that I could take three that were spreadsheets and three that were competing tools.

**Chris Morgan:** And we could give you the SDR call and the disco call.

**Aida Knezevic:** Sounds good.

**Matthew Panzarino:** Yeah, that's perfect.

**Robert Yuen:** Just a quick question.

**Robert Yuen:** Chris, do we need to filter down?

**Robert Yuen:** Because I'm going to make an assumption here, Aida and Matthew, that whatever we give you, you're going to data dump it into some type of AI model to summarize those calls anyway.

**Robert Yuen:** So we should probably index on more versus pre-selecting out specific calls.

**Chris Morgan:** Yeah, I actually have API access, so we could try to hook up like a stream of filter, you know, by the segment.

**Matthew Panzarino:** That's a good question.

**Matthew Panzarino:** I haven't done this kind of thing.

**Matthew Panzarino:** Actually, you know, I have.

**Matthew Panzarino:** I have done this thing, this kind of thing at scale before and parsed about 150 or so.

**Matthew Panzarino:** So, like, I don't think there's any hard limit.

**Matthew Panzarino:** I would say out beyond a dozen, it's diminishing returns.

**Matthew Panzarino:** Like, because I think you'll find...

**Matthew Panzarino:** If a lot of pattern matching, I doubt that there's, you know, 150 different permutations of painting points.

**Matthew Panzarino:** It's most likely going to distill pretty quickly.

**Matthew Panzarino:** So I would say maybe a dozen, and you can just do 50-50.

**Matthew Panzarino:** know, 50% people are coming from manual raw labor solutions that they're doing.

**Matthew Panzarino:** You know, I built a spreadsheet in my basement.

**Matthew Panzarino:** And then the other 50% being, hey, we used a competitor's tools or combination of competing tools, and we didn't like them because of XYZ.

**Robert Yuen:** We do have this page.

**Chris Morgan:** Chris, are you aware?

**Chris Morgan:** Yeah.

**Robert Yuen:** Because all the gone recordings are all here, but it looks like they're all demo calls.

**Robert Yuen:** So like, they're all essentially first call touches from an AE.

**Robert Yuen:** They're not like closing calls or anything else.

**Robert Yuen:** If you're just trying to get context of what an engineer might say or might talk about, this might give you enough without filtering down.

**Robert Yuen:** So like, well, what, what do they need to hear at the closing?

**Robert Yuen:** Um,

**Robert Yuen:** Typically, the closing calls are a demo call, so, like, they're all repetitive, we go through the product.

**Robert Yuen:** Discovery is more of a Q&A and, like, what you're paying, what you're trying to solve, talk a little bit about yourself.

**Matthew Panzarino:** Yeah, that's definitely where we'd find those insights, I think, because the closing is definitely going to be answering those questions, and so it would be more inference.

**Matthew Panzarino:** This comes from the horse's mouth, so I'd speak, so I think that's probably better.

**Robert Yuen:** Yeah, like, I think the easiest way without doing too much work is to just give you access to this page.

**Matthew Panzarino:** Okay, cool.

**Chris Morgan:** Yeah, and then if we could just have a, like, generic login, we'll ask Katie to maybe spin up a generic login for growthx that they can use to just download the transcript from gone.

**Robert Yuen:** Oh, gone calls.

**Robert Yuen:** Yeah.

**Matthew Panzarino:** Who do I invite?

**Matthew Panzarino:** Matthew at growthx is perfect.

**Matthew Panzarino:** TTHEW?

**Matthew Panzarino:** Yep, you got it.

**Matthew Panzarino:** Oh, and then, actually, if you wouldn't mind adding Mariana Marins.-S.

**Matthew Panzarino:** So, M-A-R-I-N

**Matthew Panzarino:** A-N-A?

**Matthew Panzarino:** Because Mariana would be helping me do the collation.

**Gary DeBerry:** A-N-A.

**Gary DeBerry:** A-N-A.

**Gary DeBerry:** There's an extra end in there.

**Gary DeBerry:** Two back.

**Matthew Panzarino:** M-A-R-I-A.

**Matthew Panzarino:** Perfect.

**Robert Yuen:** And this is growthx.com.

**Matthew Panzarino:** Let me validate that email for you, just since we're doing a fly.

**Robert Yuen:** Give me one sec.

**Robert Yuen:** Yeah, I'm not getting it.

**Matthew Panzarino:** It's not auto-populating, it's probably wrong, so give me one sec.

**Matthew Panzarino:** We don't email, we Slack.

**Matthew Panzarino:** It's actually first name dot last, so I'll paste it in the chat for you.

**Robert Yuen:** I'm trying to look for my Zoom bar.

**Matthew Panzarino:** Oh, yeah, sorry.

**Matthew Panzarino:** Mariana, M-A-R-I-A-N-A dot Marins.

**Matthew Panzarino:** It's M-A-R-I-N-S.

**Robert Yuen:** Let me go back to the screen.

**Robert Yuen:** M-A-R-I-N-A.

**Matthew Panzarino:** I-A-N-A dot M-A-R-I-N-S.

**Robert Yuen:** M-A-R-I-N-S.

**Robert Yuen:** Rollbacks.ai.

**Matthew Panzarino:** Perfect.

**Gary DeBerry:** There you go.

**Jo Kaminska:** Sweet.

**Jo Kaminska:** And you can add me as well, Jo, the same, Jo.

**Robert Yuen:** Oh, what was that?

**Jo Kaminska:** Jo at growthx.

**Jo Kaminska:** And the domain is the same.

**Jo Kaminska:** I think Aida pasted our emails in the conversation chat, if that's more helpful.

**Robert Yuen:** Got it.

**Aida Knezevic:** Thanks.

**Robert Yuen:** And then I think the only thing we need is to add a generic email into our gong user, so you can download.

**Robert Yuen:** So, Chris, that makes your job a lot easier of just getting that email into our gong system.

**Robert Yuen:** Yeah.

**Robert Yuen:** Or through Eben, or you can do it yourself.

**Chris Morgan:** Yeah.

**Aida Knezevic:** I think that could be our team email, right?

**Aida Knezevic:** Yep.

**Aida Knezevic:** Team GrowthX Labs.

**Aida Knezevic:** I think that works.

**Jo Kaminska:** Yeah, I think it's fun.

**Aida Knezevic:** Great.

**Robert Yuen:** Thanks, everyone.

**Robert Yuen:** I was just getting really worried that Chris was going to spend too much time digging through a whole bunch of gong calls.

**Robert Yuen:** Um, when it would be a lot easier if we just gave you all of them.

**Chris Morgan:** Uh, yeah.

**Robert Yuen:** Cool.

**Aida Knezevic:** All right.

**Aida Knezevic:** Perfect.

**Aida Knezevic:** Um, so this week, so we're, uh, we're going to be generating new content for you.

**Aida Knezevic:** I was curious to see if you had any, um, additional feedback on last week's batch.

**Aida Knezevic:** Um, any, any patterns that you're seeing emerge in the content that you would like to, um, fix with the artifacts.

**Aida Knezevic:** You know, any, any, anything that, um.

**Robert Yuen:** Uh, comes to mind.

**Robert Yuen:** There's only one that came out recently, and I would like to try to avoid any comments around how we run onboarding or data migration.

**Robert Yuen:** Okay.

**Robert Yuen:** just because that's so fluid and it's in constant change that whatever we put out in a blog post and we forget to go back and edit it, it's just going to cause a bunch of headaches.

**Robert Yuen:** Um, so if it has anything to do with, like, how we do onboarding or data migrations, um, or syncing with the product, anything that sounds like that, I would say leave out.

**Aida Knezevic:** Okay, great.

**Aida Knezevic:** I already removed that section from the first blog that we published, um, but we're going to fold this into the artifacts as well.

**Aida Knezevic:** Um, Gary, anything else, maybe?

**Gary DeBerry:** Yeah, um, as I was reviewing the blog post from last week, uh, what I've been doing is, uh.

**Gary DeBerry:** I've been making suggestions within Google Docs so that if there's any additional comments that I want to add in there for, you know, style changes or like the reasoning why I would have suggested something, I like to just drop those comments directly into the documents.

**Gary DeBerry:** I'm looking right now at the KPI software for architecture and engineering firms.

**Gary DeBerry:** There are a bunch of comments that are suggestions that are still live in there.

**Gary DeBerry:** Probably the biggest recurring one is spelling of competitor product names just to make sure that they're consistent and all of those.

**Gary DeBerry:** And it doesn't look like those have been accepted in there, but I just wanted to make sure that you make those changes before you get ready to publish.

**Aida Knezevic:** Yeah, yeah, yeah, yeah, we will.

**Jo Kaminska:** I'm on the changes right now. So I just checked your document, Gary, and I'll be making adjustments and also incorporating these into artifacts.

**Gary DeBerry:** Cool.

**Gary DeBerry:** Is that the preferred place for like if I do have comments on phrasing or that stuff, I'll drop them as comments into the document?

**Aida Knezevic:** Okay.

**Aida Knezevic:** Yeah, yeah.

**Aida Knezevic:** We might leave them open for longer if multiple people need to take a look at them.

**Aida Knezevic:** So we might not resolve them immediately, but we do handle them before we publish.

**Gary DeBerry:** Cool.

**Aida Knezevic:** Yeah.

**Chris Morgan:** And these, I know, so you have documents like Google Docs.

**Chris Morgan:** Are those linked on the Airtable?

**Aida Knezevic:** Mm-hmm.

**Chris Morgan:** Okay.

**Aida Knezevic:** Yeah, yeah.

**Aida Knezevic:** There's a Google Doc column where you should be able to see the links.

**Gary DeBerry:** Yep.

**Gary DeBerry:** I also like that you put the published URL after they have been published.

**Gary DeBerry:** Now I just have a one-stop shop.

**Aida Knezevic:** Yeah, yeah.

**Aida Knezevic:** Yeah, yeah.

**Aida Knezevic:** We also use that for our Looker dashboard.

**Aida Knezevic:** They're building it this week for you. And the way that it's automated, it automatically pulls the URLs from Airtable into Looker, so we don't have to manually add the published logs to Looker, it kind of happens automatically.

**Aida Knezevic:** Another thing that I wanted to show you this week is that we have set up your Scrunch dashboard.

**Aida Knezevic:** Scrunch, you probably have heard of it.

**Aida Knezevic:** It's a tool that tracks and measures LLM visibility of different brands in LLMs like ChatGPT, Claude, Gemini, Perplexity.

**Aida Knezevic:** So I'm going to share my screen and show you what it looks like.

**Aida Knezevic:** So this is your Monograph dashboard.

**Aida Knezevic:** The way Scrunch works is that it has a database of prompts, and we have uploaded some prompts for you, but you can also provide us with prompts.

**Aida Knezevic:** And these are the prompts that your...

**Aida Knezevic:** Audience, for example, an architect or an engineer would type into ChatGPT, Claude, whatever, to find out more about your solution or generally project management software.

**Aida Knezevic:** So we're trying to basically pretend like we're an engineer and an architect and we're doing research about different platforms and we're trying to assume the kind of questions that we would ask AI.

**Aida Knezevic:** And then Scrunch takes those prompts and it pings different LLMs and it analyzes those responses and then it provides all of that information in a dashboard like this.

**Aida Knezevic:** So we have 380 prompts so far.

**Aida Knezevic:** We've gotten almost 2,000 responses and you can see your competitive presence laid out.

**Aida Knezevic:** So you're pretty even when it comes to Dell Tech, BQE, and your overall presence is 23%.

**Aida Knezevic:** LLMs.

**Aida Knezevic:** The sentiment is largely positive, so that's a good thing.

**Aida Knezevic:** But if you want to see the prompts that we're using, we would go to prompts right here.

**Aida Knezevic:** And you can see, like, you do have a larger share of presence, but it's by 7%.

**Aida Knezevic:** So we can work to increase this in the coming weeks and months.

**Aida Knezevic:** These are the prompts that we're using.

**Aida Knezevic:** They're divided into different topics.

**Aida Knezevic:** For example, we have AI-driven automation and project management, and then we have prompts like these.

**Aida Knezevic:** Like I said, we can add new prompts to this list, and you can make suggestions, and we'll just import them.

**Robert Yuen:** How do we get access?

**Aida Knezevic:** So this is internal right now. I know that the team is working on getting Scrunch integrated with Looker Dashboard, so you will have access, but right now we're going to be sharing the reports with you in our weekly syncs.

**Robert Yuen:** And you'll share it, like, this, like, live, or would it be, like, a screenshot in, like, a presentation format?

**Aida Knezevic:** I mean, we'll share them live.

**Aida Knezevic:** I think we can also share it in, like, a screenshot and presentation format, whatever works best for you.

**Aida Knezevic:** I think we can pull, like, the most interesting information.

**Aida Knezevic:** We typically, like, when we're meeting clients every week, once you're kind of out of the sprint and you're publishing regularly, we dedicate a portion of the meeting to analyzing the performance.

**Robert Yuen:** So we're going to pull this data.

**Robert Yuen:** Got it.

**Chris Morgan:** Okay.

**Chris Morgan:** Some things I'd be really curious to know.

**Chris Morgan:** So first one is, like, page, like, where, when it is able to tell us.

**Chris Morgan:** let's see.

**Chris Morgan:** Yeah.

**Chris Morgan:** Uh, what are the types of pages it's pulling from?

**Chris Morgan:** Is it exclusive to blogs?

**Chris Morgan:** Is it pulling from, like, non-blog pages?

**Chris Morgan:** Um, I'm also curious, what is the sort of nature of the content inside the page that it's pulling from?

**Chris Morgan:** So is it, like, you know, I have a hunch that it can distill, like, if it's a customer quote versus, like, um, our narration.

**Chris Morgan:** I'm curious if, like, you can see if it has a preference for the nature of the content.

**Chris Morgan:** And then the last one that we would love to see, those are kind of, like, helping us optimize, uh, inputs.

**Chris Morgan:** But the other thing I'd be curious to see is sort of a lagging indicator is, um, how is Monograph showing up in questions that don't relate to software?

**Chris Morgan:** So if, uh, if someone has a question about their business.

**Chris Morgan:** Like a business situation that doesn't mention software, is Monograph somehow showing up as the solution to that because it enables a business practice?

**Chris Morgan:** I'd love to be getting more footprint in that way.

**Chris Morgan:** So anyways, those are like three areas that I'd love to know more about from this.

**Aida Knezevic:** Yeah, I think with the prompts that we have right here, we can expand them and include prompts that are more, that aren't software related specifically.

**Aida Knezevic:** So then we can start to measure that over time.

**Aida Knezevic:** We can, Scrunch can integrate with Google Analytics data.

**Aida Knezevic:** So that's something that we can consider, like we can look into setting this up for you.

**Aida Knezevic:** It depends, I think it might depend on the kind of permissions that we have in your GA4, but we can connect this data, then it'll be easier to kind of.

**Aida Knezevic:** See the pages that it's referencing and pulling from.

**Chris Morgan:** Great.

**Matthew Panzarino:** Cool.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** I'll just throw in a couple of observations there.

**Matthew Panzarino:** Robert, you had mentioned on a previous call about, hey, maybe we should look at Reddit and see what questions are being asked.

**Matthew Panzarino:** That's essentially what these prompts are, right?

**Matthew Panzarino:** So if you do have sources that we can do that work on that you know are authoritative, where engineers are collecting and asking questions, and you want to focus on those kinds of prompts that they're asking for, obviously architects too, but, you know, mentioned that engineering is a focus right now.

**Matthew Panzarino:** You can either give us the source and we can scrape those together or if you do any internal exercises that also feed into other motions like sales and you're trying to figure that out for yourself and you want to share those findings with us, please do, because we can add clusters of prompts here to track.

**Matthew Panzarino:** Same thing, as you mentioned, Chris, with the clusters of prompts that are about non-software questions or non-software topics.

**Matthew Panzarino:** We can just add those clusters here.

**Matthew Panzarino:** I also wanted to point out or, like, I guess, expect...

**Matthew Panzarino:** This is like one step above tea leaves at the moment for everyone.

**Matthew Panzarino:** I just want to like put that out there.

**Matthew Panzarino:** We're using scrunch because it's an option for us right now to monitor in a raw way.

**Matthew Panzarino:** Hey, if we throw these prompts, which we are essentially guessing at, at the wall, what comes back?

**Matthew Panzarino:** And it can give us a directional tracking.

**Matthew Panzarino:** So don't go crazy, like looking at these numbers and worrying about like a day-to-day monitoring of these.

**Matthew Panzarino:** This is very much a directional thing at the moment.

**Matthew Panzarino:** I just wanted to put that out there because this is an insanely new science, you know, the geo tracking.

**Matthew Panzarino:** And there are a couple of companies out there, scrunch is one of them that are doing something.

**Matthew Panzarino:** And we want to offer you some visibility into this.

**Matthew Panzarino:** And we have found some success with it, which is great.

**Matthew Panzarino:** Like we do believe it for the most part.

**Matthew Panzarino:** But even the companies internally, like I know people inside these companies, inside Anthropic and at OpenAI.

**Matthew Panzarino:** And they are telling me, we don't actually know.

**Matthew Panzarino:** So if they don't know, you know, then it is an outside-in approach like scrunches is pretty much the best way you can go.

**Matthew Panzarino:** Okay, let's act like a person.

**Matthew Panzarino:** Let's ask the questions and let's see what kind of motion we get.

**Matthew Panzarino:** So we should see some directional intelligence here that will help.

**Matthew Panzarino:** I just wanted to put that out there.

**Matthew Panzarino:** It's not like a GA4 scenario where you're getting a trailing indicator.

**Matthew Panzarino:** You know somebody visited that page off of this search.

**Robert Yuen:** I'm fully aware.

**Robert Yuen:** I know the investors that invested in scrunch.

**Robert Yuen:** So I have enough context.

**Robert Yuen:** Totally get it.

**Aida Knezevic:** Okay, great.

**Robert Yuen:** Just to say context, so like you're looking at Monograph's entire marketing team.

**Robert Yuen:** So we aren't going to spend any energy on terms of like scraping Reddit to figure out like what people are asking.

**Robert Yuen:** I'm going to leave that to GrowthX as you guys optimize your workflows.

**Robert Yuen:** So if you see something like added.

**Robert Yuen:** Um,

**Robert Yuen:** Don't lean on us, because we're stretched thin as it is.

**Aida Knezevic:** Got it.

**Aida Knezevic:** All right.

**Aida Knezevic:** One update that we have for you is that we're working on creating that LLM text file.

**Aida Knezevic:** So once that's ready, we're going to send it over to you, and you'll just have to upload it to your site.

**Aida Knezevic:** I think Webflow has an instructor.

**Aida Knezevic:** They have, like, a tutorial for how you can do that.

**Jo Kaminska:** Am I right, Jo?

**Jo Kaminska:** Yeah, so it should be pretty straightforward in Webflow.

**Jo Kaminska:** In the SEO section, Chris, you can take a look if there is, like, a section that lets you upload the file, because this LLM text file is basically, like, a sitemap, but for LLMs to better read your website.

**Jo Kaminska:** So let us know if you can, like, upload it without any code.

**Jo Kaminska:** If not, we can figure out the other way.

**Jo Kaminska:** But as Ada said, we're working on this.

**Jo Kaminska:** Yes, and we should have more information in the upcoming week.

**Chris Morgan:** Yeah.

**Robert Yuen:** Is this file going into your domain provider or going into your Webflow?

**Robert Yuen:** Like, which host?

**Chris Morgan:** It is going into Webflow.

**Robert Yuen:** Webflow?

**Robert Yuen:** Okay.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** All right.

**Aida Knezevic:** Great.

**Aida Knezevic:** Do you have any questions or comments, anything that you think we should address today?

**Robert Yuen:** No.

**Robert Yuen:** No.

**Robert Yuen:** I'm excited that we got one out.

**Robert Yuen:** Four is coming out.

**Robert Yuen:** So it's time to step on the gas and continue to iterate.

**Robert Yuen:** So I'm excited.

**Gary DeBerry:** Yeah.

**Gary DeBerry:** Great.

**Gary DeBerry:** a heads up that I'm going to be out on vacation for the next week.

**Gary DeBerry:** I do want to review the blog post, the next wave of blog posts, and get into a rhythm of doing that early on in every week.

**Gary DeBerry:** Um, so-

**Gary DeBerry:** There will be a little bit of disruption, as I won't be able to do that immediately when those links come through, but I do want to get into that rhythm.

**Gary DeBerry:** So hopefully not too much of a hiccup with my lack of accountability, but we'll get there.

**Aida Knezevic:** Yeah, no problem.

**Aida Knezevic:** I'm going be out of office next week as well, with the exception of Monday, but Joe and Matthew are going to be here.

**Robert Yuen:** There is one thing, just so everyone has at least a little bit of context.

**Robert Yuen:** I told Chris and Gary on Monday, one, there's a growing M&A activity within our space.

**Robert Yuen:** A few of the smaller companies are coming together.

**Robert Yuen:** The bigger incumbents, like the BQEs and the Dell Techs, are already 100% owned by PE.

**Robert Yuen:** So we'll be pushing out in the coming future a narrative where we're built by architects for architects, truly.

**Robert Yuen:** And starting to position us in a more aggressive.

**Robert Yuen:** position against PE-owned competitors.

**Robert Yuen:** So there will be campaigns that will start to either want to compare us and might lean a little bit more negative towards PE.

**Robert Yuen:** There's a couple objectives I want.

**Robert Yuen:** One, like, obviously we want to grow, but I think a lot of our prospects and customers aren't asking questions like, is the company truly built by architects for architects?

**Robert Yuen:** How's the support team?

**Robert Yuen:** What's the product roadmap look like?

**Robert Yuen:** And what's the vision for the business?

**Robert Yuen:** And I want to make sure that we want to highlight and bring that question more into light.

**Robert Yuen:** I know we will be doing a good job if we're seeing more competition within our late-stage sales funnels.

**Robert Yuen:** Right now, we see a little bit, but I would like to increase that.

**Robert Yuen:** So that's a broad take in terms of, like, what some of the future narratives might come out from our, from content.

**Robert Yuen:** that

**Jo Kaminska:** One question here, because we already incorporated this, and when I was editing the content, I saw mentions that this software is built by architects for architects, but I was wondering more about engineering topics.

**Jo Kaminska:** Should we still position the tool in the same way, or would you like to have a little bit of a different message?

**Jo Kaminska:** And basically, I don't know, on the editing stage, for example, we should remove these type of phrases from specifically engineering content.

**Robert Yuen:** No, I think currently the motion that we're doing right now works.

**Robert Yuen:** And I would like to see a few of it go out into the world and get a better gauge of the reaction from the market.

**Robert Yuen:** So on engineering content, don't change anything.

**Robert Yuen:** On, let's say, venture-backed, founder-led versus PE-backed, EBITDA-focus, that's just a refinement of focus that's going to happen.

**Matthew Panzarino:** Incoming weeks.

**Matthew Panzarino:** Yeah, great.

**Matthew Panzarino:** That's great that you flagged it, too, because we can incorporate that into the company context.

**Matthew Panzarino:** Because positioning of the company is what the artifact is about, and then it informs, obviously, directionality of the articles.

**Robert Yuen:** Matthew, what will help you?

**Robert Yuen:** Do you need, like, a bullet point one-pager from us?

**Robert Yuen:** Do you need, let's say, the PRs that were pushed out recently on these M&A actions?

**Robert Yuen:** What would help GrowthX continue to iron out the persona profiles on Monograph?

**Matthew Panzarino:** Yeah, one-pager.

**Matthew Panzarino:** One-pager is fine.

**Matthew Panzarino:** I think that'll probably provide enough articulation.

**Matthew Panzarino:** If I look at it and determine that it's unable to parse it properly, I'll ask for more.

**Matthew Panzarino:** But let's not put any additional labor on you.

**Matthew Panzarino:** Just shoot us over the one-pager.

**Matthew Panzarino:** Same way you'd be briefing, like, a marketing partner or something like that.

**Matthew Panzarino:** And then we can take a look at it.

**Robert Yuen:** But we're refunding the email that we want to push out that Gary started.

**Gary DeBerry:** So maybe, Gary, just share the Google Doc on that mic.

**Gary DeBerry:** I'm on enough contacts.

**Gary DeBerry:** Sure thing.

**Gary DeBerry:** Yep.

**Gary DeBerry:** Can I share that with the team at GrowthX?

**Gary DeBerry:** Okay.

**Gary DeBerry:** And then you'll all have access to it?

**Aida Knezevic:** Mm-hmm.

**Aida Knezevic:** Yep.

**Aida Knezevic:** All right.

**Aida Knezevic:** Well, we're at time, but thanks so much for today.

**Aida Knezevic:** We'll get the new articles to you by the end of the week, and we'll also publish the new ones as well by the end of the week.

**Robert Yuen:** Awesome.

**Robert Yuen:** Thank you, everyone.

**Robert Yuen:** Thank you.

**Robert Yuen:** Welcome to the team, Matthew.

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** Appreciate it.

**Matthew Panzarino:** Glad to be here.

**Matthew Panzarino:** Have a good one.

**Aida Knezevic:** Cheers, everybody.

**Jo Kaminska:** Cheers, everybody.
