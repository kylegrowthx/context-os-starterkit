# Semrush AIO Chat (Cont) and Amber Hamilton

<metadata>
date: 2025-05-19
time: 16:31 UTC
duration: 42 minutes
organizer: Jason Gong (GrowthX)
participants: Jason Gong (GrowthX), Kirkland Gee (GrowthX), Kevin Batchelor (Semrush), Amber Hamilton (Semrush)
fathom_recording_id: 63395325
fathom_url: https://fathom.video/calls/303341329
share_url: https://fathom.video/share/yeVWUPe8beZV7vvyXbyQ8DMWPziffQQR
source: fathom
enriched_on: 2026-03-04 14:30 UTC
</metadata>

---

## Summary

Kevin Batchelor from Semrush demonstrated the AIO (AI Optimization) module within the Enterprise platform—a new tool designed to help agencies track how their clients appear across AI models like ChatGPT, Claude, Gemini, and Perplexity when people ask relevant prompts. The system connects to GSC data to identify keywords losing clicks to AI, then generates prompts around those topics and tracks share of voice and positioning across AI platforms, with daily updates and sentiment analysis. Kirkland probed the architecture of how Semrush generates and sources the prompts (clarifying it's similar to keyword magic but for AI), and the team aligned on a Thursday 11:30am PT demo of the Enterprise platform with emphasis on automated insights and workflows, with Kevin to provide clarification on data extraction methods and pricing options for Enterprise and standalone AIO by tomorrow.

---

## Context

GrowthX is exploring the Semrush AIO product as a potential new vertical within CheckThat or as a white-label offering. Semrush is the primary SEO/content platform that GrowthX has built workflows and APIs into, and Kevin Batchelor is the primary contact driving education and implementation. This is the continuation of a previous week's conversation where Jason (GrowthX) raised questions about the architecture—specifically whether the prompts are people-also-ask questions from Google SERPs or if Semrush generates them via some other methodology. This demo was scheduled to show how the AIO module works within the Enterprise platform and to begin evaluating whether it fits GrowthX's service delivery or product roadmap, and whether standalone pricing (coming July 2025) would be more attractive than the current bundled model.

---

## Relevance

**To CheckThat / AI Visibility:**
- Semrush AIO platform directly competes with or aligns with CheckThat's vision—tracks share of voice, positioning, and sentiment across AI models for a given set of prompts
- GrowthX is learning how Semrush sources/generates prompts at scale; this methodology is core to evaluating CheckThat's competitive edge and feature prioritization
- Sentiment analysis and source attribution features (which articles/content are referenced by AIO) are key differentiators Kirkland flagged as critical for client decisions
- Kirkland's questions about API-vs-UI differences, model versioning (GPT-4.0 vs. SearchGPT default), and web search grounding are foundational to how GrowthX should position CheckThat

**To GrowthX Delivery:**
- AIO could become a new delivery vertical or upsell within client engagements, especially for content clients concerned with AI displacement
- Kevin emphasized speed (reports in 5 minutes) and automation as the value prop over manual Core work; GrowthX's content workflows and Looker Studio reports currently serve a similar function with more customization
- Kirkland is not sure the time savings justify the cost given GrowthX's reliance on first-party data (GSC, Airtable) and custom Looker reporting; pricing structure (bundled to Enterprise at launch, standalone in July) will drive adoption decision
- No immediate impact to EPD, but if GrowthX pursues an AIO integration or white-label model, will need to clarify data extraction methods and ensure it complements existing delivery vs. creates redundancy

**To GrowthX Business Development:**
- Semrush is expanding AIO from Enterprise-only bundle to standalone product in July; pricing and packaging clarity needed before GrowthX can pitch to clients or decide on internal adoption
- Thursday demo of Enterprise platform focuses on automated insights and workflows; outcome will inform whether GrowthX pursues deeper partnership or pursues independent CheckThat path
- Kevin committed to follow-up on: prompt generation/selection methodology, data extraction from AI platforms, and pricing options for Enterprise vs. AIO (all seats vs. 10-15 seat tiers) by end of week

---

## Overview

- Kevin Batchelor walked through the Semrush Enterprise platform and its new AIO (AI Optimization) module, showing how to identify keywords losing clicks to AI and then track client positioning in AI-generated responses
- The AIO module uses GSC data + keyword analysis to flag search query topics impacted by AI, then generates or selects prompts around those topics and tracks daily share of voice, positioning, sentiment, and brand mentions across ChatGPT, Claude, Gemini, Perplexity, and other AI models
- Kevin explained how prompts are generated (similar to the Keyword Magic tool, pulling high-volume questions around topics, but the exact differentiation from "People Also Ask" questions needs internal clarification from Semrush)
- Kirkland extensively probed the technical architecture: Are prompts hand-curated or auto-generated? How does Semrush get positioning data from AI models (API calls vs. special deal with OpenAI/Google)? Does it differentiate web-search-enabled vs. raw LLM responses? How is sentiment analysis done?
- Kevin acknowledged many questions need internal clarification and committed to sending detailed follow-up this week and at the Thursday Enterprise demo
- The team discussed pricing: AIO is currently bundled only with Enterprise (~price of Core platform), but will be sold standalone starting July 2025
- Kirkland expressed skepticism about time savings vs. cost, given GrowthX already uses custom Looker reporting tied to GSC and Airtable; the main benefit would be to offer AIO as a service to clients, not to replace internal workflows
- Scheduled 45-minute Enterprise platform demo for Thursday 11:30am PT with focus on automated insights and workflows

---

## Key Topics

### Semrush Enterprise Platform Overview
Kevin demonstrated the Enterprise platform's What Happened Report (analyzing traffic changes to client websites over a time period, e.g., Abnormal AI's changes from March to May), content insights, and keyword prioritization features. The platform generates reports in 5 minutes vs. hours of manual work in Core. Enterprise also integrates GSC data for win/loss analysis to identify which keywords are losing clicks despite maintaining rank position—a signal that traffic is being diverted to AI-generated responses.

### AIO Module Architecture & Data Flow
The AIO module is designed for agencies to track how their clients appear across AI models (ChatGPT, Claude, Gemini, Perplexity, etc.) when real users ask prompts. The workflow: identify keywords losing clicks to AI (via GSC win/loss analysis) → convert those topics to prompts → run those prompts daily against AI models → track daily share of voice, positioning (rank in the AI response), sentiment (positive/negative/neutral mentions), and brand presence over time. Kirkland raised a critical question: how exactly are the prompts generated or sourced? Kevin said it's similar to the Keyword Magic tool (pulling high-volume questions around a topic), but acknowledged he needs clarification on whether there's an extra step (e.g., running questions through an AI to rephrase as natural prompts) or if they're pulled directly from existing sources.

### Data Extraction & API Methodology
Kevin stated that Semrush has special deals/APIs with OpenAI, Google, and other LLM providers to pull data directly (not by making API calls through the user's own accounts). Kirkland pressed on the details: How does Semrush determine positioning (rank) in the response if it's not making the API calls itself? Kevin acknowledged the data comes "from the platform" but couldn't fully explain the mechanics. Kirkland noted that the API vs. web-UI distinction matters because ChatGPT's default model changes, web-UI has system instructions and tool access that API doesn't have, and web search behavior differs. These details affect how to interpret AIO positioning data for clients.

### Sentiment Analysis & Source Attribution
Kevin mentioned that AIO tracks sentiment (positive/negative/neutral) about the brand in AI responses. Kirkland clarified that "sentiment" likely means analyzing the text of the AI response to detect positive/negative mentions (e.g., "Brand X is the best" vs. "Brand X has issues"), not actually tracking user behavior after they receive the response. The team discussed the brand strength metric (what are the positive and negative attributes frequently mentioned by AI about the brand). There was also discussion about source attribution—which specific articles or content pieces are being cited by AI in responses—which is important because it can show if old content is being referenced (a risk for product updates).

### Prompt Tracking & Model Selection
Kevin walked through the project setup where users select which AI models to track (SearchGPT, ChatGPT 4.0, Claude, DeepSeek, Gemini, Grok, Perplexity, etc.), input keywords or custom prompts, and group them by topic/category. The AIO platform then pulls daily data and tracks positioning and sentiment per model. Jason asked whether the platform differentiates between API-based responses (no web search) vs. web-search-enabled responses (SearchGPT, ChatGPT web search). Kirkland noted that if data comes via API, there should be no web search by default, and that's a methodological difference worth understanding. Kevin acknowledged it's a good question and said the early product is still evolving.

### Share of Voice & Competitive Analysis
AIO's primary metric is share of voice (SOV) across AI platforms and prompts. For example, if tracking "best security tools" prompts across ChatGPT and Perplexity, and the client's tool gets mentioned 18% of the time vs. competitors, that's an 18% share of voice. Market analysis features let you compare by brand, see competitor mention counts, and break down by model. Kirkland and Jason discussed how "share of voice" in AI differs from SEO (where you have a defined position on the SERP); here, brands can be mentioned first, last, or not at all, and the weighting of position is unclear.

### Pricing & Go-to-Market
Kevin shared that AIO is currently bundled only with Enterprise (same price point as Core for all seats). In July 2025, Semrush will sell AIO as a standalone product, likely at a different price and with flexible seat options (e.g., all seats vs. 10-15 designated seats). Kirkland noted that Semrush's time savings value prop (reports in 5 min vs. hours of manual work) doesn't apply to GrowthX as strongly because GrowthX uses custom Looker Studio reporting tied to GSC and Airtable, which is more customized and doesn't require third-party data from Semrush. However, GrowthX might offer AIO as a new service to clients. Kevin committed to sending pricing options for Enterprise and standalone AIO by end of week.

### Thursday Enterprise Demo & Next Steps
The team scheduled a 45-minute Enterprise platform demo for Thursday 11:30am PT (1:30pm CT / 2:30pm ET), with focus on automated insights and workflows. Amber Hamilton will source and send Enterprise demo videos and schedule the demo; Kevin will prepare an in-depth demo and get internal clarifications on prompt generation methodology and data extraction processes; Jason will coordinate final scheduling. Kevin will also send pricing and clarification documents by tomorrow (or latest by Thursday).

---

## Action Items

**Kevin Batchelor (Semrush)**
- Provide detailed clarification on prompt generation/selection process for AIO platform (are they pulled from Keyword Magic tool, "People Also Ask," or AI-rephrased questions?); email to Jason Gong and Kirkland Gee by end of day or tomorrow
- Get internal clarification on data extraction methodology from AI platforms (how does Semrush access positioning data—API calls, special deals, daily scraping?); email details to Kirkland Gee
- Prepare pricing options for Enterprise platform and standalone AIO (all seats vs. 10-15 seat tiers); email to Jason Gong
- Prep in-depth Enterprise platform demo for Thursday meeting; focus on automated insights, workflows, and how Enterprise reduces manual reporting time vs. Core

**Amber Hamilton (Semrush)**
- Source and send Enterprise platform demo videos to Jason Gong and Kirkland Gee
- Schedule 45-minute Enterprise demo for Thursday 11:30am PT (1:30pm CT / 2:30pm ET); send calendar invite with Abnormal AI as example company

**Jason Gong (GrowthX)**
- Coordinate final scheduling and confirm Thursday demo attendees and timing

**Kirkland Gee (GrowthX)**
- Review clarifications from Kevin on prompt sourcing and data extraction methodologies before Thursday demo
- Prepare list of additional technical questions on API methodology and sentiment analysis for Thursday demo

---

## Transcript
**Kevin Batchelor:** Hey Jason, how's it going?

**Jason Gong:** Pretty good.

**Jason Gong:** Just doing some launching this morning of our fundraise.

**Amber Hamilton:** Oh, nice.

**Jason Gong:** Working from home today.

**Jason Gong:** Sorry, what's up?

**Amber Hamilton:** I said working from home today.

**Jason Gong:** Yeah.

**Jason Gong:** Oh, Brett.

**Amber Hamilton:** Cool.

**Jason Gong:** Let's get started.

**Amber Hamilton:** want to take us off?

**Amber Hamilton:** Since you're kind of, we're continuing from last week's meeting, you kind of ran that one, so.

**Kevin Batchelor:** Yeah.

**Kevin Batchelor:** Yeah, that's fine.

**Kevin Batchelor:** We only have, I think, 30 minutes today, so we can just jump right into it.

**Kevin Batchelor:** Mainly, I wanted to tie our enterprise platform into the AIO Insights today.

**Kevin Batchelor:** I know we used the example you sent over to last time that we discussed abnormal AI.

**Kevin Batchelor:** So let me share my screen here and we can jump in.

**Kevin Batchelor:** One second.

**Jason Gong:** Can everybody see this?

**Amber Hamilton:** Yep.

**Kevin Batchelor:** Perfect.

**Kevin Batchelor:** So this is really kind of the first step that an agency would take within the plan.

**Kevin Batchelor:** This is has happened report.

**Kevin Batchelor:** And I know Abnormal AI, they just changed their website recently.

**Kevin Batchelor:** So I know they really kind of started capturing this traffic around March.

**Kevin Batchelor:** Now they're seeing a rise around May.

**Kevin Batchelor:** So that's kind of the time period we analyzed here.

**Kevin Batchelor:** Basically, whenever you generate this for a client, very simple, you just pick whatever time frame you want to analyze, and it'll tell you exactly what has occurred within that time frame.

**Kevin Batchelor:** So we get some high-level metrics here.

**Kevin Batchelor:** And then, of course, we can get some more details, like what keywords contributed to that traffic change, like what we need to really focus on, as we can see here.

**Kevin Batchelor:** And can see like a significant drop-off from like an uncensored AI, for example.

**Kevin Batchelor:** We can get like an analysis of specific parts of the website.

**Kevin Batchelor:** And then, of course, down here, I just like to point out, we can really kind of see it by like, for example, maybe a group of like weak keywords, or in this case, it's really just kind of flagging one that maybe we should adjust the content on.

**Kevin Batchelor:** Start maybe increasing those rankings.

**Kevin Batchelor:** Also, we can really take a list of keywords and forecast what that's going to do for the client over time, how much traffic they can gain, how much estimated revenue they can gain as a result.

**Kevin Batchelor:** If they have a heavy PPC approach, of course, we can also improve SEO value to that specific client.

**Kevin Batchelor:** Really, I mean, there's a lot we can do within here.

**Kevin Batchelor:** Like, Jason, I know we talked about last time, like, you know, what would maybe be the point of like an enterprise software like this compared to Core.

**Kevin Batchelor:** Really, I mean, like the main focus of this is it just generates these reports within five minutes.

**Kevin Batchelor:** It just gets straight to the point without having to do all of that research with the data within Core.

**Kevin Batchelor:** So it tends to save clients hours.

**Kevin Batchelor:** We also have like content insights, for example.

**Kevin Batchelor:** Like, I don't want to spend too long on this today because I know the main focus is AIO.

**Kevin Batchelor:** But we have like content insights.

**Kevin Batchelor:** You can write your...

**Kevin Batchelor:** Content for you, basically, tell you everything you need to include within the content.

**Kevin Batchelor:** But really, and of course, like prioritizing keywords, really where we're going to tie the software, though, into AIO is going to be when we connect our GSC.

**Kevin Batchelor:** So we didn't have access to abnormal AI's GSC.

**Kevin Batchelor:** So I'm just going to I'm going to use one of our custom examples within the platform here.

**Kevin Batchelor:** We have this win loss analysis.

**Kevin Batchelor:** So really, if you have a client that's interested in how these AI platforms or just AIO in general is impacting the traffic to the website, we can focus in on this one clicks versus lost clicks report, mainly the lost portion of it.

**Kevin Batchelor:** So what we can do here is we can filter by demand decrease.

**Kevin Batchelor:** And this is going to show us a list of keywords for our specific website with the connected GSC.

**Kevin Batchelor:** Where we kept the same position on.

**Kevin Batchelor:** Google, right?

**Kevin Batchelor:** Like our position has not changed, but we've lost clicks.

**Kevin Batchelor:** So they're not really visiting the website as much.

**Kevin Batchelor:** In this case, we can identify these keywords as they're mostly just getting their information from AIO or, you know, an AI platform.

**Kevin Batchelor:** So this is kind of somewhere you could start, like maybe take like, you know, the top 10 keywords here.

**Kevin Batchelor:** And that's when we tie it into our AIO platform here.

**Kevin Batchelor:** we have this, Jason, we covered a little bit of this last time.

**Kevin Batchelor:** Wait one second.

**Kevin Batchelor:** Let me just adjust this real quick.

**Kevin Batchelor:** All right.

**Kevin Batchelor:** We're good to go there.

**Kevin Batchelor:** Let me go AIO back into the AIO platform.

**Kevin Batchelor:** As you can kind of see, it's all under one umbrella here.

**Kevin Batchelor:** But that's when we can bring it into this prompt generation.

**Kevin Batchelor:** And once we set up these workflows here, we can basically like pick like, you know, the top topics or keywords.

**Kevin Batchelor:** You know, that are being impacted by AI, which we kind of really want to drill down on.

**Kevin Batchelor:** So once we bring in those specific topics or keywords, what it's going to do is it's going to bring in, it's going to treat those keywords as topics and it's going to bring in the top prompts on Google or these AI platforms around that specific topic.

**Kevin Batchelor:** So like, like that'll be really what you want to drill down on and write the content around these.

**Kirkland Gee:** Yeah, Kirkland, go ahead.

**Kirkland Gee:** Yeah, you said you bring in the prompts from Google or other AI platforms.

**Kirkland Gee:** Can you elaborate?

**Kirkland Gee:** Like, how are you generating the prompts that are used in a platform like this?

**Kevin Batchelor:** Really, I said like other AI platforms.

**Kevin Batchelor:** Really, it's going to be Google.

**Kirkland Gee:** I mean, that's going to be the main focus and it's going to be the top.

**Kirkland Gee:** So are these prompts just people also ask questions that you're just using as AI prompts?

**Kevin Batchelor:** Correct.

**Kevin Batchelor:** It's going to be the number one asked prompts, like questions around these specific keywords on Google.

**Kirkland Gee:** Sorry.

**Kirkland Gee:** I'm so sorry.

**Kirkland Gee:** Yeah, go ahead.

**Kirkland Gee:** Just for clarification, because like it is a different thing to see.

**Kirkland Gee:** Like, we're getting prompts that people are putting into an AI platform versus we're just pulling the people also ask questions from the SERP.

**Kirkland Gee:** And I'm trying to understand which one of them, because I don't know how you would pull prompts that people are inputting, right?

**Kevin Batchelor:** Yeah, no, no, sorry.

**Kevin Batchelor:** So, yeah, I should clarify on that.

**Kevin Batchelor:** It's not like what people also ask.

**Kevin Batchelor:** It's just taking the topic and we have something like similar to this with our like keyword magic tool where it's like, you know, we might take a topic.

**Kevin Batchelor:** Like if I do something quick here, loans, and just focus down on questions, like we would have just the top questions by volume around that specific keyword or in this case topic.

**Kevin Batchelor:** Now, this software, it's very new, so I can get clarification on that too.

**Kevin Batchelor:** That's just something I'm going to have to ask internally if there's kind of an extra step they take on top of keyword magic tool.

**Kirkland Gee:** That makes sense.

**Kirkland Gee:** Typically what we find is, you know, the types of things that people are traditionally searching.

**Kirkland Gee:** In Google, in a search engine versus what they're prompting an AI with are very different just in the amount of words, the way that they're phrasing them.

**Kevin Batchelor:** And it doesn't look like those are like straight up just questions that people search on Google.

**Kevin Batchelor:** I'm just curious, you know, are you running them through an AI to generate the prompts?

**Kevin Batchelor:** And that's what a lot of people do.

**Kevin Batchelor:** Or are they coming from some other source just because like the quality of the prompts?

**Kirkland Gee:** I mean, basically, you know, changing words and those are going to drastically affect whether or not you show up.

**Kirkland Gee:** So that methodology is super important for us to understand.

**Kevin Batchelor:** I see.

**Kevin Batchelor:** Yeah, let me get some clarification on that.

**Kevin Batchelor:** That's a really good question.

**Kevin Batchelor:** And again, like this is kind of a new software we have.

**Kevin Batchelor:** We're very focused on just AI in general at the moment and just tracking because we know it's kind of a big question a lot of our customers have.

**Kevin Batchelor:** So I'm still a bit new to this process.

**Kevin Batchelor:** So I could definitely get clarification on.

**Kirkland Gee:** Yeah, totally fine.

**Kevin Batchelor:** Yeah, specifically.

**Kevin Batchelor:** But yeah, I mean, so that's how we set this up.

**Kevin Batchelor:** And I did.

**Kevin Batchelor:** A project for abnormal.

**Kevin Batchelor:** Let me just go into project settings here.

**Kevin Batchelor:** So once you set these up, you can select the AI models you want to track, like search GBT.

**Kevin Batchelor:** That would be kind of the AIO function within Google.

**Kevin Batchelor:** When GBT 4.0, that would be more so chat GBT.

**Kevin Batchelor:** But we have Claude, we have Deep Seek, Gemini, Grok.

**Kevin Batchelor:** Actually, this would be the Google AIO overview here.

**Kevin Batchelor:** Perplexity.

**Kevin Batchelor:** And then that's where we can tie in those prompts and specifically like track them within groups.

**Kevin Batchelor:** You can cluster them in the specific categories by topics.

**Kevin Batchelor:** And then, of course, choose like, you know, which AI models you want to track certain prompts.

**Kevin Batchelor:** can all be the same or you can kind of just specify that yourself.

**Kevin Batchelor:** So that's the project setup.

**Kevin Batchelor:** You can also put in a list of competitors you want to track alongside of your client's domain.

**Kevin Batchelor:** But that's basically the project setup right here.

**Kevin Batchelor:** You know, we have the U.S.

**Kevin Batchelor:** here.

**Kevin Batchelor:** We have English.

**Kevin Batchelor:** But we've just added a lot of different...

**Kevin Batchelor:** Countries around the world.

**Kevin Batchelor:** So if you have some clients that kind of branch into some of those other markets, I could definitely send you over that list.

**Kevin Batchelor:** If it's primarily in the U.S., we could just kind of keep it this way here.

**Kirkland Gee:** If you're tracking in a different country, that would just be like the IP address that those prompts are getting tested from, basically?

**Kevin Batchelor:** yes.

**Kevin Batchelor:** Yeah, it would be in their language.

**Kirkland Gee:** So like, for example, we have Germany.

**Kevin Batchelor:** German, yeah.

**Kevin Batchelor:** And let me cut over to this overview here.

**Kevin Batchelor:** So really, this is the primary metric we're going to be tracking is share of voice across these AI platforms in the prompts we're tracking.

**Kevin Batchelor:** So in this case, Abnormal AI, you know, it is picking us up slightly, but they don't really have too much of a presence yet.

**Kevin Batchelor:** And I think it's because it's a newer website, but we see like, you know, 18%, like, you know, share of voice within the market there, across these AI platforms we're tracking.

**Kevin Batchelor:** So here I have it just focused down on ChatGPT.

**Kevin Batchelor:** If we were going to be tracking these prompts within ChatGPT there, we can also break down like the sentiment in which the brand is being talked about.

**Kevin Batchelor:** Oftentimes it's going to be more positive.

**Kevin Batchelor:** Otherwise, the AI platforms are not going to talk about you in general, sometimes neutral.

**Kevin Batchelor:** So that's kind of something we can drill down on.

**Kevin Batchelor:** And again, this is like this right here, it's a new project.

**Kevin Batchelor:** So we just started tracking this today.

**Kevin Batchelor:** But really, like every day you have this, it'll pull this data in just automatically and you'll be able to measure this over time.

**Kevin Batchelor:** Also, we can specifically track the prompts we're really drilling down on.

**Kevin Batchelor:** But in this case, picking up on a lot of competition because abnormal AI doesn't really have as much of a prompt presence.

**Kevin Batchelor:** It's around, you know, like specifically a brand.

**Kevin Batchelor:** And presence, since it's a newer website.

**Kevin Batchelor:** So as it builds up in time, it can capture.

**Jason Gong:** for that one, what does position mean?

**Kirkland Gee:** I was literally, yeah, I was going to ask the same thing.

**Kevin Batchelor:** Yeah, so this is basically just telling you those prompts and who's basically kind of picking up those positions from your competitors.

**Kevin Batchelor:** Now, normally, if you had a bigger presence across these AI platforms, and you will kind of build on that, again, as the website.

**Jason Gong:** But I mean, like, what does position mean here?

**Jason Gong:** Like, just the response of the prompt?

**Kevin Batchelor:** Like, we're listed as the 17th tool.

**Kevin Batchelor:** This right now, it's picking up on the competition.

**Kevin Batchelor:** So it's saying, like, Google, like, their product, the authenticator for this particular prompt is currently picking up number one when somebody asked that question within chat GVT.

**Kirkland Gee:** Yeah, the question is, what does number one mean in the context of a prompt?

**Kirkland Gee:** just the first one that's mentioned in a list?

**Kirkland Gee:** Like, if you click into one of those prompts, do you see the actual response from the model?

**Kevin Batchelor:** Or...

**Kevin Batchelor:** Yeah, so, mean, we can, like, jump right in here, but that would be the order, like, list in which if somebody asked that within ChatGPT, like, what order these specific brands and products would be talked about.

**Amber Hamilton:** Kind of like in the keyword, sorry, Kirkland, kind of like in the keyword tools where it shows you which position you are.

**Amber Hamilton:** So on the SERP, you know, below the paid ads, if you're number one, that's position one.

**Amber Hamilton:** And so it's kind of the same thing here, but since there's not enough data from, you since we just put it in, it's showing you for that prompt.

**Kirkland Gee:** And then when he clicked on it, showing you who's showing up first, second, and third, so you know who you're competing against.

**Kirkland Gee:** But you can't actually see what the raw text of what the AI model said back.

**Kirkland Gee:** You're just getting this, like, abstracted position of where you might have shown up in the response, right?

**Kevin Batchelor:** Like, I can't see what ChatGPT said to that prompt.

**Kevin Batchelor:** Okay.

**Kevin Batchelor:** Correct.

**Kevin Batchelor:** Yeah, we pull these on a daily basis just from these platforms.

**Kevin Batchelor:** So this is kind of what we're provided with.

**Kevin Batchelor:** You know, like in what order they would kind of come up in the results.

**Kevin Batchelor:** What do you say you're provided?

**Kirkland Gee:** Yeah, what do you mean?

**Kirkland Gee:** Because typically, so just for most other platforms we've talked to that do this kind of thing, I mean, what you're doing is you're running that prompt against these models, getting a response and doing something with the data.

**Kirkland Gee:** So you said that you guys don't do that, that you're like getting data directly from OpenAI or something like that?

**Kirkland Gee:** Or do you know how, is it like some sort of deal?

**Kevin Batchelor:** Yeah, so it's a deal we have with each of these platforms right here, like these LLMs, AI platforms.

**Kevin Batchelor:** And it's kind of just like an API that we use just to kind of pull this data right from the platform.

**Kevin Batchelor:** So I know it's just, it's a deal SEMrush has set up with each of these platforms here.

**Kevin Batchelor:** And I know it's kind of confusing because like when somebody asks like one of these prompts, they're just going to get one response.

**Kevin Batchelor:** But I can get some clarification on like if they're coming up ninth, that just might mean within their specific data.

**Kevin Batchelor:** don't know.

**Kevin Batchelor:** Like, that's kind of the order they would have, like, ranked of that specific problem, that specific brand and product.

**Kirkland Gee:** Can click on that, which tools are best for detecting phishing emails, one, towards the one, the one is 17.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** I'm just curious, like, so that means there are 17 different tools that were mentioned in the response.

**Kirkland Gee:** And this is going to show me, okay, this date, it was in that position.

**Kirkland Gee:** The next day, it's been the same.

**Kirkland Gee:** So basically, we got the same response these two days back and forth.

**Kevin Batchelor:** Correct.

**Kevin Batchelor:** Okay.

**Kevin Batchelor:** Yes, and this is going to pull every day, basically.

**Kevin Batchelor:** So you'll be able to check this on a daily basis and kind of see how that changes over time.

**Kevin Batchelor:** Yeah, but, like, yeah, right here we can see the problem.

**Kirkland Gee:** Yeah, So I can actually see the response.

**Kevin Batchelor:** Okay, great.

**Kirkland Gee:** Yeah.

**Kevin Batchelor:** Sorry, Kirk.

**Kirkland Gee:** I'm getting used to this, too.

**Kirkland Gee:** It's very No, you're totally fine.

**Kevin Batchelor:** I'm learning with you here, so.

**Amber Hamilton:** Yeah, and I think, so the 17th, that's, the 17th position was no before.

**Amber Hamilton:** So in the model, it's comparing, like, your competitors and the questions that are.

**Kirkland Gee:** Or the prompts that are coming up or that you've put in and tracking your competitor, you know, kind of like you do in your strategy builder or your position tracking in the core platform.

**Amber Hamilton:** And then because we just put it in, you see the position change that there's nothing on the third column.

**Amber Hamilton:** That's where you're tracking your own position as well.

**Amber Hamilton:** So, you know, instead of tracking, you know, what number you are on the SERP feature, it's tracking where you are in the response and the various AI.

**Kirkland Gee:** And then share of voice.

**Kirkland Gee:** I think I thought a little tool tip.

**Kirkland Gee:** That's both doing some calculation on both if you show up and what position you do show up, where you show up to get.

**Kevin Batchelor:** Oh, my gosh.

**Kirkland Gee:** I did not mean to make balloons.

**Kirkland Gee:** I got to turn those stupid reactions off.

**Amber Hamilton:** I have one hour talking about a funeral.

**Kirkland Gee:** Oh, that's no good.

**Kirkland Gee:** Yeah, if you can hover over the little I by share of voice.

**Kirkland Gee:** I just want to kind of understand.

**Kevin Batchelor:** Yeah.

**Kirkland Gee:** Yeah, 100% would mean you're mentioned first everywhere.

**Kirkland Gee:** Correct.

**Kevin Batchelor:** Okay.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** And brand new.

**Kirkland Gee:** Visibility is just if you show up at all regardless of position.

**Kevin Batchelor:** Yes.

**Kevin Batchelor:** Okay.

**Kevin Batchelor:** Yes.

**Kirkland Gee:** Perfect.

**Kevin Batchelor:** Yes.

**Kevin Batchelor:** I mean, we can track like all of the prompts, for example, with an AI ranking.

**Kevin Batchelor:** So you can factor in that full list.

**Kevin Batchelor:** I know also like there's a lot of brands that want to know like what specific articles are being sourced.

**Kevin Batchelor:** So once like abnormal AI, for example, really starts capturing these prompts and just kind of increase that share of voice.

**Kevin Batchelor:** We'll be able to see here, like specifically if they are being mentioned in these, like we have eight prompts, which we're tracking, for example, that, you know, are being referenced in this specific blog here.

**Kevin Batchelor:** So we can really see like whether or not it's old data.

**Kevin Batchelor:** Like, you know, we can see here it's from around like the end of last year.

**Kevin Batchelor:** So, you know, maybe they have some more up to date data, but especially if it's like more of like an e-commerce company and they've like, you know, kind of just like updated their products or in this case, like like abnormal AI, maybe they updated their software and it's referenced.

**Kevin Batchelor:** Like old information.

**Kevin Batchelor:** That's something I know a lot of companies just want to see, like, you know, what specific information is being referenced when people ask this question.

**Jason Gong:** And then in the prompt tracking, do you guys like differentiate what's a like reference from a search versus just it's just like an answer it gives you?

**Jason Gong:** You know what I mean?

**Jason Gong:** Like, for example, if I ask what's the best security tool, sometimes it'll just give me an answer without running search and giving me a citation, right?

**Kevin Batchelor:** Like, is there a way to differentiate those two?

**Kevin Batchelor:** I see.

**Kevin Batchelor:** So, like, specifically on, like, AIO, like just Google's AI overview or?

**Jason Gong:** No, just like if I type into ChatGPT, like, what's the best phishing, you know, protection security tool?

**Jason Gong:** Like, sometimes it'll run a Google in the background, right?

**Kevin Batchelor:** So it gives me an answer with citations.

**Jason Gong:** Research, mean, and then sometimes it'll just say, you know, Microsoft is the best and it won't cite anything.

**Kirkland Gee:** Would that be the difference between GPT-40 and SearchGPT?

**Kirkland Gee:** I guess SearchGPT is probably the product specifically.

**Kirkland Gee:** And Jason, don't think if they're doing it through the API, I think not.

**Kirkland Gee:** I mean, I don't think there's any cases where you would ask for a response from the AI model using the API and trigger a web search without like explicitly turning that on.

**Kirkland Gee:** So all of these would be just the raw LLM response without any sort of grounding or web search.

**Kirkland Gee:** Which it should be.

**Kevin Batchelor:** Yes.

**Jason Gong:** Yeah, would agree with that.

**Jason Gong:** That's actually kind of interesting because I guess like as a person, like whatever, 99% people, I'm opening ChatGPT, wherever the default is.

**Jason Gong:** So like over time, as the default model changes, like what are we actually doing in this platform?

**Jason Gong:** Like when you track prompt performance, is it per model?

**Kevin Batchelor:** Yeah, so it'll be per model.

**Kevin Batchelor:** Just like once you set up that project.

**Kevin Batchelor:** It's, you know, so I've only selected, like, you know, these two here, but, like, these are all you can add and track just, you know, across those workflows there.

**Kevin Batchelor:** So we have most of, like, the major ones, as you can see here.

**Kevin Batchelor:** Right.

**Jason Gong:** I mean, guess it's just, like, something for us to think.

**Jason Gong:** Like, I'm going to imagine 4.0 is going to be outdated in, like, six months, but all our history is for 4.0.

**Jason Gong:** And it's, like, what we really care about is, like, does default ChatGPT mention our brand more, right?

**Jason Gong:** Which, like, the model kind of changes underneath every few months.

**Kevin Batchelor:** Yeah.

**Kevin Batchelor:** Would that be, like, 0.1?

**Kevin Batchelor:** Like, ChatGPT, they have so many models that it's just, you know.

**Kirkland Gee:** No.

**Kirkland Gee:** I mean, all of the models, if you're using an API, like, you're getting data directly from the API, you're probably the only way you're getting a response.

**Kirkland Gee:** If you're doing something on ChatGPT.com, there's all these extra tools that AI can call.

**Kirkland Gee:** There are system instructions that aren't included when you use an API.

**Kirkland Gee:** Like, you're going to get different responses.

**Kirkland Gee:** It's just part

**Kirkland Gee:** of the game, so to speak.

**Kirkland Gee:** But I think all of the people doing this AI tracking, to your point, Jason, like it's an interesting question that I think affects everyone, you know, pretty much exactly the same.

**Amber Hamilton:** And, you know, though we are, you know, leaders in the field, you know, we still, there's still a lot of gray area that we, you know, we don't have, they don't tell us.

**Amber Hamilton:** Same thing with like trying to rank on Google, like we know, what we can know, and we research what we can research, but there's still, you know, unless we go hack Google, or we have an insider or something, you know, there's still gonna be that gray area.

**Amber Hamilton:** But I would say Kirkland, when you asked about, you know, the search, like the actual search rankings, the only thing that I would think that that wouldn't come into play is when they're searching in ChatGPT, they get an answer, and then they use those links below.

**Amber Hamilton:** That's going to go into your sentiment, and then how people are feeling about the brand, because they're trusting the, they're trusting ChatGP enough to get the answer, and then they're following through with your, your brand or your customer's brand.

**Kirkland Gee:** Yeah, can we look at the sentiment analysis?

**Kirkland Gee:** just want to understand, like, is this just doing a sentiment analysis on the text, or is there something else going on?

**Amber Hamilton:** So I'm searching through everything, basically, like all of the reviews, how people are interacting with that prompt, you know, are they continuing to go through and use, you know, ask more questions?

**Kirkland Gee:** Are they clicking the link?

**Kirkland Gee:** would you get that data?

**Kirkland Gee:** How would you know what users are doing after they input a prompt?

**Kevin Batchelor:** Yeah, so, I mean, that would, let me, let me get, these are great questions, Kirkland.

**Kevin Batchelor:** Let me get, let me get some clarification on that, too.

**Kevin Batchelor:** But yeah, I mean, again, I know it's like just a special integration they set up with these AI platforms.

**Kevin Batchelor:** I think I just, I need to get more clarification on kind of just what the red lines with that are, and exactly, like, you know, kind of how they're specifically pulling that, like, after the process.

**Kirkland Gee:** Yeah, I mean, when I say SEMrush,

**Kirkland Gee:** I'm assuming that that means it's doing what's called a sentiment analysis on the text of the response and being like, hey, is it talking about this brand in a positive or a negative or a neutral kind of way?

**Amber Hamilton:** you're right, Kirkland.

**Kirkland Gee:** I'm looking at a different tool that we have.

**Amber Hamilton:** It's kind of similar.

**Amber Hamilton:** And it says, you know, the brand strength, positives and negatives frequently mentioned by AI responding to your brand.

**Amber Hamilton:** So how does AI feel about your brand?

**Kirkland Gee:** Which I don't think I'm saying that out loud.

**Amber Hamilton:** That feels weird.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** So what are their feelings?

**Kirkland Gee:** Okay.

**Kirkland Gee:** Yeah, that's what I figured.

**Kirkland Gee:** I just wanted to clarify.

**Amber Hamilton:** Yeah.

**Amber Hamilton:** Sorry about the confusion.

**Kevin Batchelor:** All right.

**Kevin Batchelor:** Last thing I want to point out here is just like we have the market analysis.

**Kevin Batchelor:** So again, like when abnormal really starts, you know, kind of bring like have more of a presence across these AI platforms, we can track by brand performance.

**Kevin Batchelor:** Of course, we can see their current competitors and just like, you know, how many mentions they have versus like what the share of voice is.

**Kevin Batchelor:** And then, of course, we can break that out in a chart level, get all the main metrics from share of

**Kevin Batchelor:** Voice, average positions, and then, of course, like number of products or, you know, in this case, I guess, like security softwares, which they're tracking across these prompts.

**Kevin Batchelor:** We can also just compare by model, too.

**Kevin Batchelor:** So, you know, if you really like all the models were tracking, for example, like if you wanted to, in this case, in the project I set up, we're only tracking two.

**Kevin Batchelor:** But if you wanted to kind of bring them all in, you could see kind of just how you're performing for that entire list of prompts.

**Kevin Batchelor:** Just, again, from a mentions and share of voice perspective, just across, you know, all of those AI platforms there.

**Kevin Batchelor:** Now, I know eventually, again, this is kind of still in the early stages, so we're going to be building on this in the coming months.

**Kevin Batchelor:** And I think eventually, you know, they plan on, you know, kind of bringing in maybe some like content insights for the prompts specifically.

**Kevin Batchelor:** But like right now, it's more of just like a tracking perspective, again, how your clients are performing.

**Kevin Batchelor:** Across like AI in general, and then like what's being referenced, you know, we see it from like a market view.

**Kevin Batchelor:** And then of course, it's specific prompt tracking.

**Kevin Batchelor:** But as this industry grows, and we get more answers, I know they're going to be kind of just very up to date with adding those workflows.

**Kevin Batchelor:** Again, if we could bring in like content insights or something of that sort, maybe even these AI platforms will eventually be paid advertising.

**Kevin Batchelor:** I don't know.

**Kevin Batchelor:** That's not really the case now.

**Kevin Batchelor:** But it's definitely something we're staying on top of here at SEMrush.

**Kevin Batchelor:** We do, we are going to start.

**Kevin Batchelor:** So right now, this is specifically attached to our, you know, main like SEO enterprise software.

**Kevin Batchelor:** We will start selling this standalone too, probably around July.

**Kevin Batchelor:** So that's another thing we can kind of factor into.

**Jason Gong:** I'm good.

**Jason Gong:** You're saying, like, right now it's a part of Enterprise, but in July it won't be and we'll have to pay extra for it.

**Kevin Batchelor:** Correct, yeah.

**Kevin Batchelor:** So, yeah, right now it has to be, like, sold on top of Enterprise, but around July we can sell this product standalone.

**Kirkland Gee:** And either way, it's a separate cost from the Enterprise platform, right?

**Kirkland Gee:** Correct, yeah.

**Kirkland Gee:** It's an additional cost either way.

**Kevin Batchelor:** Correct, yes.

**Amber Hamilton:** Kevin, you need to plug your computer in.

**Kevin Batchelor:** I know, yeah.

**Kevin Batchelor:** I've been checking that at the top right here the whole time.

**Kirkland Gee:** It's, like, slowly going down.

**Kirkland Gee:** Every Chrome tab you open is another percent of your battery.

**Amber Hamilton:** Like, you're giving me anxiety.

**Kevin Batchelor:** So, Kirkland, I can also, just after the demo, like, this week, like, I can, again, just get more insights specifically on how we're pulling all of this out of these platforms.

**Kevin Batchelor:** I can definitely, we can send that over in my follow-up email.

**Kirkland Gee:** Yeah, I think my, you know, I don't want to assume, but, like, I've seen a lot of these platforms.

**Kirkland Gee:** We've thought about building one ourselves.

**Kirkland Gee:** Like, we...

**Kirkland Gee:** You kind of understand how this works typically.

**Kirkland Gee:** And so the things I'm most interested in are the prompts, like where are they being generated or created or pulled from?

**Kirkland Gee:** Like what if I put phishing in as a keyword, what determines what prompts are automatically created?

**Kevin Batchelor:** Because I would assume we can.

**Kevin Batchelor:** Can you input your own custom prompts that you want to track as well outside of those keywords?

**Kirkland Gee:** Yes, absolutely.

**Kirkland Gee:** So that's great.

**Kirkland Gee:** But I want to know, you know, if I put in a keyword, how much more work do I have to do to get through the list of prompts that I want to be tracking?

**Kirkland Gee:** And then from a model perspective, I think I would imagine you're just hitting the API with the prompt, getting the response.

**Kevin Batchelor:** I saw that in there.

**Kevin Batchelor:** So that makes sense.

**Kirkland Gee:** And then obviously pricing is a big piece of the puzzle for us too, right?

**Kirkland Gee:** Evaluating all of that.

**Kirkland Gee:** And I'd assume, so if it has to be on top of the enterprise platform right now, that probably, I mean, that would make it significantly more expensive than an alternative.

**Kevin Batchelor:** We're just doing this, right?

**Kevin Batchelor:** Yeah, we originally started talking about like the enterprise.

**Kevin Batchelor:** This platform, because again, like what you're paying currently just for the core platform, like all those seats and everything, it would kind of reach around a similar price as enterprise.

**Kevin Batchelor:** And again, everything here is just more automated.

**Kevin Batchelor:** just like to the point.

**Kevin Batchelor:** So you don't have to spend as much time in core, like, for example, like within a timeframe, identifying like what went wrong for a specific website or specifically what went well.

**Kevin Batchelor:** And then of course, like, you know, forecasting content insights.

**Kevin Batchelor:** Yeah.

**Kirkland Gee:** Kirkland, go ahead.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** I mean, a lot of that stuff we're doing either in Looker Studio, like we have custom Looker reports that are directly integrated with GSC with all of our Airtable data to be able to cohort our content by like ways that we've already decided ahead of time.

**Kirkland Gee:** We don't typically rely on third party data, like from SEMrush directly for any sort of reporting.

**Kirkland Gee:** It's more about like keyword research and the front end of the planning and the strategy before we have first party data.

**Kirkland Gee:** So, I mean, I'm not saying that there's not a benefit to having a platform like this, but I'm not sure the time savings for us.

**Kirkland Gee:** Would be as large as some other, you know, potential clients you guys might have.

**Kirkland Gee:** And then like the content side, I mean, that's like our whole product, right?

**Kevin Batchelor:** Like that's what we sell is content workflows.

**Kevin Batchelor:** Yeah.

**Kevin Batchelor:** know in the fall we talked with Marcel and that's kind of primarily what you were using the API for kind of just to build that.

**Kevin Batchelor:** I see.

**Kevin Batchelor:** To kind of build something like this just within your platform.

**Kevin Batchelor:** Yeah.

**Kirkland Gee:** I'm sorry.

**Kirkland Gee:** And also, I feel like I'm giving you guys a hard time and I apologize for that.

**Kevin Batchelor:** just feel like asking the questions we need answers to are the right way to keep the conversation moving.

**Kevin Batchelor:** Kirkland, Kirkland, it helps me because, again, like we're pretty early like in this process.

**Kevin Batchelor:** So when you ask these questions, I know I'm going to get these questions in the future and I can get these answers now and address those, you know.

**Kevin Batchelor:** Right.

**Kevin Batchelor:** 100%.

**Kevin Batchelor:** It helps me a lot.

**Kevin Batchelor:** Yeah.

**Amber Hamilton:** Well, and if you're asking the questions, you're not just messing around.

**Amber Hamilton:** Like, you know, you know what you're doing and you know you want the problem.

**Kevin Batchelor:** I need to know the ins and outs.

**Kirkland Gee:** Exactly.

**Kirkland Gee:** So Jason, don't know what else you're thinking about.

**Jason Gong:** I think it's like super hard to dig in all the little details.

**Jason Gong:** I mean, is this something we can play with, like this demo instance that you have here so we can click around?

**Jason Gong:** So that's one question.

**Jason Gong:** And then the other one is just like, how much is enterprise?

**Amber Hamilton:** How much is AIO?

**Amber Hamilton:** I think that's where we kind of left it off last meeting.

**Amber Hamilton:** Well, we don't have a trial of the tool.

**Amber Hamilton:** Is that what you're asking about?

**Jason Gong:** Yeah, trial or even just like the sandbox you have with like dummy data.

**Jason Gong:** Like just the ability to come in here so I can see like does it have all the charts that we need?

**Jason Gong:** Because we've had, you know, like we have trials for like the other platforms that can answer some of the more kind of detailed questions.

**Jason Gong:** Like especially, you know, Kirkland Landry is like getting into the API for all these as well.

**Kirkland Gee:** Like is that something you can take a look at?

**Kirkland Gee:** don't know.

**Kirkland Gee:** Is Is it?

**Kirkland Gee:** Is any of this AIO data available through the API, or is it all just in the UI and the platform?

**Kevin Batchelor:** It would all just be within the UI, but everything can be exported out via CSV, PDF.

**Kevin Batchelor:** I mean, in your case, it's probably going to be more like CSV is going to be more helpful if you're integrating that in your platform.

**Kevin Batchelor:** But yeah, I mean, there's no current API integration for any of this at the moment.

**Kirkland Gee:** It's all kind of just in platform, but it can be exported out.

**Kirkland Gee:** Makes sense.

**Amber Hamilton:** Okay, so we have our questions.

**Amber Hamilton:** Do you guys, I don't know if you asked last time, do you have a time frame when you're making decisions?

**Amber Hamilton:** You mentioned kind of other platforms that you're cheating on us with.

**Jason Gong:** I don't know.

**Jason Gong:** mean, basically, they said, so if you can give us pricing, like, I would like it right now, please.

**Kevin Batchelor:** Kevin, do you have an idea or ballpark?

**Kevin Batchelor:** Yeah, so, I mean, it tends to be very customized.

**Kevin Batchelor:** If I could...

**Kevin Batchelor:** Yeah, let me stop sharing for a sec.

**Kevin Batchelor:** I think we might have a Google Sheet.

**Kevin Batchelor:** One second.

**Amber Hamilton:** I mean, either way, we could get it over today on some sort of, not the exact pricing, because we'll need to make sure that we have everything that you need and want, but, you know, a roundabout figure.

**Jason Gong:** Yeah, and I imagine it's, yeah, I mean, just everything, like, is it based on prompts, which I imagine it is, or is it based on number of domains, even?

**Jason Gong:** And it's, like, how all this pricing works.

**Kevin Batchelor:** Yeah, so it breaks down to this right here.

**Kevin Batchelor:** So it would just be, like, for AI, this is AI specifically, and I can get to Enterprise in a second, but we have bronze, silver, and gold.

**Kevin Batchelor:** And then, of course, like, the projects, that would reflect just how many clients you'd be using for this.

**Kevin Batchelor:** And then we would have just a list of prompts you can track.

**Kevin Batchelor:** So it would just kind of be working out, like, how many limits you would need.

**Kevin Batchelor:** And then this is how the monthly versus annual pricing would work.

**Jason Gong:** Okay.

**Jason Gong:** And then a service, what's a service credit?

**Kevin Batchelor:** So service credits, like that's what you use to generate the specific workflows.

**Kevin Batchelor:** So service credit is spent kind of just like, like every time you use that.

**Kevin Batchelor:** I don't think that that's not as much like, you know, an AIO feature.

**Kevin Batchelor:** That's more just like enterprise and like the, has happened report.

**Kevin Batchelor:** So, um, yeah, the enterprise product, this is more of a, I don't really want to show this as much at the moment because this is kind of more of like a customized pricing.

**Kevin Batchelor:** Um, and we have like different pricing for, um, you know, various segments.

**Kevin Batchelor:** Um, so you still fall within S and B.

**Kevin Batchelor:** So I, I think that would be, you know, kind of just like a lower price range than this, what we have here, for example.

**Jason Gong:** Um, yeah, I mean, if you could just, I guess I see their seats there, but like, you know, take a look at how many seats we have.

**Jason Gong:** Let us know what Enterprise would look like.

**Amber Hamilton:** You would want a seat for everyone that you have in the core?

**Jason Gong:** I don't know.

**Jason Gong:** I mean, like, what would you suggest?

**Jason Gong:** Actually, I was kind of surprised how many seats we were using, so maybe that's something for me to look at.

**Jason Gong:** But, yeah, maybe just assume, like, everyone would have a seat for right now.

**Jason Gong:** We would have a seat for in Enterprise.

**Amber Hamilton:** Okay.

**Kevin Batchelor:** Yeah, and you can have, like, an unlimited amount of guest users within Enterprise and come and look at the reports and export those out.

**Kevin Batchelor:** Where the cost comes in is the admin users.

**Kevin Batchelor:** So they're the ones who can actually go in and, like, generate the projects.

**Kevin Batchelor:** But once they generate the projects, you can invite as many people as you want to come in.

**Kevin Batchelor:** Okay.

**Jason Gong:** I would say, yeah, I would say, like, more than half are probably guest users for us.

**Amber Hamilton:** Yeah, I mean, you want to have whoever's doing, like, the BDRs or something who are doing, like, the back-end research stuff.

**Amber Hamilton:** They could set up the projects and then, you know, the team comes in and they can just export it and use what they need.

**Amber Hamilton:** That's completely up to you.

**Amber Hamilton:** I don't think that everyone that's using Core would need a seat in this.

**Amber Hamilton:** I would say, you know, just a few admins to actually generate the projects and then put in the prompts and then it's there.

**Jason Gong:** Your team just goes in as guests and exports.

**Jason Gong:** Right.

**Jason Gong:** We could probably get by with what, just directors and maybe Emmys at that level?

**Jason Gong:** So you're probably looking at something closer to like 10, 15 seats.

**Amber Hamilton:** OK, so we'll do it with the pricing with everyone right now, and then we'll do a 10 to 15-ish pricing as well.

**Jason Gong:** And then just to clarify, like no sandbox that can click around for both AIO or Enterprise?

**Kevin Batchelor:** Yeah, no, that's something we've pushed on in the past, but they're very strict with like no sandbox.

**Kevin Batchelor:** Now, if you want to see more of it, we could generate like any client example you want and go back in and walk through all those workflows you want to see.

**Kevin Batchelor:** OK.

**Kevin Batchelor:** OK.

**Kevin Batchelor:** OK.

**Kevin Batchelor:** It's no, like, kind of just like, like sandbox.

**Kevin Batchelor:** can click around at the moment.

**Jason Gong:** Okay.

**Jason Gong:** Because it just looked like totally different almost than our SEMrush now.

**Amber Hamilton:** So yeah, at least have some time to use it.

**Amber Hamilton:** Like I don't even know what half the reports are.

**Amber Hamilton:** Yeah.

**Amber Hamilton:** And you would be assigned someone to actually to help you get it set up an actual onboarding person.

**Amber Hamilton:** That would be your, your customer success person.

**Amber Hamilton:** Um, but we might have some videos.

**Amber Hamilton:** I'm sure we have like demo videos that we could send if you want to, if that would be helpful.

**Amber Hamilton:** Like someone clicking through and talking about what each of the different enterprise things are.

**Kirkland Gee:** And to clarify, if you got, this is just something I may have probably talked about before, but I just missed.

**Kirkland Gee:** If we did SEMrush Enterprise, that changes how the average person in our company is going to interact with SEMrush.

**Kirkland Gee:** So rather than going through the traditional core experience, they're going to use enterprise.

**Amber Hamilton:** Or is that just like when they're doing this specific workflows, they're going to be in this version of the platform.

**Amber Hamilton:** Yeah.

**Amber Hamilton:** So it's like a different login.

**Amber Hamilton:** Okay.

**Amber Hamilton:** Yeah.

**Amber Hamilton:** Yeah.

**Amber Hamilton:** Like I have a log.

**Amber Hamilton:** And like four demos.

**Amber Hamilton:** then I have Enterprise four demos.

**Kirkland Gee:** So it's a completely different platform because you don't want everyone to have access to it.

**Kirkland Gee:** But yeah, so you'd still keep core if you wanted because there's a lot of value there still.

**Kirkland Gee:** And if we keep core, are we paying for both?

**Kevin Batchelor:** separate prices for core and enterprise?

**Kevin Batchelor:** So enterprise, it comes with core.

**Kirkland Gee:** comes with a business plan of core.

**Kevin Batchelor:** you wouldn't lose any of that.

**Kevin Batchelor:** Okay, got It's got to be an upgrade, more automated data.

**Kevin Batchelor:** Again, just taking all that core data and just reaching like that end insight.

**Kirkland Gee:** Okay.

**Jason Gong:** Yeah, I mean, as the next step, maybe give us some pricing.

**Jason Gong:** Like we need at least like one more session, even just on the enterprise.

**Jason Gong:** I feel like the AIO, a decent grasp of based on what you click through.

**Kevin Batchelor:** For enterprise, it's probably worth another session so we can spend a lot of Amber, we're going to like jump deeper into enterprise, we should schedule at least 45 minutes.

**Amber Hamilton:** weʻs won't.

**Amber Hamilton:** We should.

**Amber Hamilton:** There's there's so much within there.

**Amber Hamilton:** Yeah, your schedule is insane.

**Amber Hamilton:** So why don't you tell us what time you're available?

**Kevin Batchelor:** Because I try to look at his calendar and I'm like, I know what's happening.

**Kevin Batchelor:** Yeah, it's a nightmare.

**Kevin Batchelor:** Would you guys, this week's crazy.

**Kevin Batchelor:** Actually, I could probably do something maybe, maybe like Thursday.

**Kevin Batchelor:** I've got, I got to keep in mind you're on Pacific Coast time.

**Amber Hamilton:** Oh, I think his computer died.

**Kirkland Gee:** Well, we did.

**Jason Gong:** We did say that.

**Amber Hamilton:** He looks like he's at the same, like at his house.

**Jason Gong:** So I'm like, where's your plugin?

**Amber Hamilton:** Let's see.

**Amber Hamilton:** Let me see if I can see what he was talking about.

**Amber Hamilton:** Thursday.

**Amber Hamilton:** I think he was going to say something like 3 p.m.

**Amber Hamilton:** So was three hours behind me?

**Amber Hamilton:** Three hours behind?

**Jason Gong:** Okay.

**Amber Hamilton:** Let's see.

**Amber Hamilton:** Okay.

**Amber Hamilton:** Let me talk to him when he gets his computer going back again.

**Amber Hamilton:** But are you guys pretty open on Thursday?

**Jason Gong:** Let's see.

**Kirkland Gee:** For the most part, yeah.

**Kirkland Gee:** Okay.

**Kirkland Gee:** I am on East Coast time, but.

**Amber Hamilton:** Okay, so let's see.

**Amber Hamilton:** Jason's got to be different.

**Jason Gong:** He said Thursday, 3 p.m.

**Amber Hamilton:** I'm on Central, so.

**Amber Hamilton:** Well, I was just looking.

**Jason Gong:** Let's see here.

**Jason Gong:** I'm free, 2 p.m.

**Jason Gong:** Pacific.

**Jason Gong:** And 12 p.m.

**Jason Gong:** Pacific to 1.30.

**Amber Hamilton:** Was that when you were?

**Amber Hamilton:** He's messaging me on his phone, so.

**Amber Hamilton:** He has 10 a.m.

**Amber Hamilton:** Pacific time.

**Jason Gong:** 10 a.m.

**Jason Gong:** 1 p.m.

**Jason Gong:** Eastern.

**Jason Gong:** No, I can't do that.

**Jason Gong:** Or at least.

**Jason Gong:** What could do is 11.30.

**Jason Gong:** Does that work?

**Jason Gong:** They say I'm free, 11.30 to 1.30.

**Jason Gong:** That's it.

**Jason Gong:** And then 2 to 3.

**Jason Gong:** Yeah, we could probably just coordinate over email or something.

**Amber Hamilton:** Yeah.

**Amber Hamilton:** Kevin, did you find a plug?

**Kevin Batchelor:** I thought that was plugged in properly.

**Kevin Batchelor:** Apparently not.

**Kevin Batchelor:** I think today is just not my – it's not a great Monday.

**Kevin Batchelor:** But let me take a look at this.

**Kevin Batchelor:** So, Amber, you said 11.30 is the earliest.

**Amber Hamilton:** 11.30 to 1.30, he's open, and then 2 to 3.

**Jason Gong:** Yep.

**Kevin Batchelor:** 2 to 3.

**Amber Hamilton:** And those are Jason-specific times.

**Kevin Batchelor:** That's specific.

**Kevin Batchelor:** Okay, 1.30 Pacific should work.

**Kevin Batchelor:** Yeah, I'm good there.

**Kevin Batchelor:** Which would be 4.30.

**Jason Gong:** I'm sorry, I'm not free 1.30.

**Jason Gong:** Like 1.32, I'm not free.

**Jason Gong:** Like 2 to 3, 11.30 to 1.30.

**Kevin Batchelor:** Let me see.

**Kevin Batchelor:** 11.30.

**Kevin Batchelor:** All right, yeah, I could do 11.30 Pacific.

**Kevin Batchelor:** That works, so I just got to move something around.

**Kevin Batchelor:** So, Amber, let's just schedule 45 minutes there.

**Kevin Batchelor:** And then, Jason, does abnormal, does that example still work?

**Jason Gong:** Yeah, let's keep using that one.

**Kevin Batchelor:** All right, sounds good.

**Amber Hamilton:** All right, so 11.30 Pacific, 1.30 Central, 2.30 Eastern.

**Amber Hamilton:** For 45 minutes, it'll come across as 30 minutes, and then I'll edit it, and then we'll go.

**Amber Hamilton:** From there, we'll get you pricing and all those questions, hopefully later today, Kevin can get to it, but we'll get you answers by tomorrow, at least, and then we will discuss the rest on Thursday.

**Jason Gong:** All right, sounds good.

**Amber Hamilton:** All right, appreciate everyone, and we'll talk to you a few weeks.

**Jason Gong:** Bye.

**Amber Hamilton:** Bye.
