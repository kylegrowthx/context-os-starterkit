# Vapi <> GrowthX Weekly Sync

<metadata>
date: 2025-04-24
time: 18:01 UTC
duration: 29 minutes
organizer: matthew@growthx.ai
participants: Marcel Santilli (GrowthX), Jordan Dearsley (Vapi), Richard Ou (Vapi), Matthew Panzarino (GrowthX), Branko Kral (GrowthX), Jason Gong (GrowthX)
fathom_recording_id: 59067930
fathom_url: https://fathom.video/calls/285125849
share_url: https://fathom.video/share/92tyUwhU5ak22tuvd9tmKSUMKW_cPmss
source: fathom
enriched_on: 2026-03-04 19:08 UTC
</metadata>

---

## Summary

GrowthX and Vapi aligned on a dual-track content strategy combining editorial and programmatic approaches to drive SEO and user acquisition. Marcel and his team will develop 30-40 high-intent assignments across four prioritized content clusters (model comparisons, STT/TTS guides, integration recipes, and voice agent guardrails) with the goal of publishing 1-2 articles per week starting next week. Simultaneously, Jason and the GrowthX design/dev team will prototype programmatic template pages modeled on Fathom's integration web, targeting both organic search intent and current user enablement through sample conversations and "hit play" demos.

---

## Context

Vapi is a voice AI infrastructure company building APIs and platforms for voice agents. GrowthX is a B2B content marketing firm recently engaged on a strategic content and SEO initiative. This weekly sync brought together Vapi's product and marketing team (Jordan Dearsley, Richard Ou) and GrowthX's core delivery team (Marcel Santilli, Matthew Panzarino, Branko Kral, Jason Gong) to calibrate content direction and prioritize work streams. The relationship is early stage but high-intent—Vapi wants comprehensive SEO coverage across voice AI topics while GrowthX is committed to delivering at scale through parallel editorial and programmatic tracks.

---

## Relevance

**To GrowthX Delivery:**
- Programmatic content architecture modeled after Fathom's integration web is working well for clients; Jason's Bardeen AI experience provides a proven playbook for template-based scaling
- "Sandwiching" strategy (high-intent technical deep dives paired with broader, higher-volume content) is core to topical authority building for AI/voice companies
- Content approach must flex per cluster: model comparisons and listicles differ structurally from technical guides and compliance content; rushing all five clusters simultaneously will dilute quality

**To CheckThat:**
- Voice agent guardrails and compliance topics (HIPAA, edge cases, safety) are emerging content needs with enterprise relevance; potential for CheckThat AI visibility insights
- Integration recipes (e.g., Twilio + 11Labs + DeepGram) are high-intent, low-volume searches where Vapi can establish deep authority; auditing where Vapi appears in AI-generated content is valuable

**To GrowthX Business Development:**
- Vapi is moving at startup velocity ("fast and furious"); willingness to spin up parallel workstreams and prototype weekly (even at risk of spilling into next week) signals healthy engagement and expansion potential
- Voice Library sample access and production usage data give GrowthX real product assets to work with (model samples, user templates); reduces content research friction
- Richard Ou's emphasis on voice agent guardrails and edge cases surfaces compliance as a potential expansion topic for follow-on engagement

**Technical/Operational:**
- Vapi uses KeyStatic CMS; GrowthX will need dev/design access ASAP; Airtable + Supabase stack preferred for scaling beyond static site limits
- GitHub repo setup is on Jordan's plate but Airtable/Supabase approach may avoid repo pagination bottleneck; decision pending internal alignment

---

## Overview

- Focusing on 3-4 key content clusters: model comparisons, STT/TTS guides, and integration recipes
- Aiming to publish 2+ articles next week, ramping up to regular weekly cadence
- Developing programmatic templates for voice agents and chatbots, inspired by successful examples
- Balancing high-intent technical content with broader, higher-volume topics to build authority

---

## Key Topics

### Content Strategy and Clusters

  - Identified 10 potential content clusters, prioritizing 3-4 to start:
      - Model comparisons (TTS, STT, LLMs)
      - STT and TTS guides (e.g., diarization, vocoders)
      - Voice-related apps and alternatives
      - Integration recipes (e.g., Twilio + 11labs + DeepGram)
  - Aim to develop 30-40 assignments per cluster for 3-4 months of content
  - Balancing technical, high-intent content with broader, higher-volume topics

### Programmatic Approach

  - Creating templates for voice agents and chatbots, similar to Fathom's integration web
  - Covering both organic search intent and enabling current users
  - Including benefits, options, and product integration paths on template pages
  - Considering adding sample conversations or "hit play" demos for engagement

### Content Development and Publishing

  - Calibrating content approach for each cluster due to differing formats
  - Aiming to publish 1-2 articles per week initially, across chosen clusters
  - Developing assignments further, e.g., comprehensive lists of open-source TTS/STT models
  - Exploring ways to include model samples or quick demos in articles

### Technical Implementation

  - Engaging designer and web developer for programmatic template prototyping
  - Considering Airtable + Supabase for content management as volume scales
  - Using existing static CMS (likely Gatsby) for initial implementation

---

## Action Items

**Marcel Santilli (GrowthX)**
- Send calibration piece to Vapi team for high-level notes
- Record and send Loom videos explaining content strategy by tomorrow
- Develop 30-40 assignments for each of the 4 prioritized content clusters
- Aim to publish 1-2 articles from prioritized clusters by end of next week
- Connect with Jason offline re: getting dev and design access to Vapi's CMS

**Jason Gong (GrowthX)**
- Create sample programmatic page for voice agent/chatbot use case by early next week

**Jordan Dearsley (Vapi)**
- Set up GitHub repo for GrowthX team to push content if needed

---

## Transcript

**Richard Ou:** I remember in New York. I actually have a cafe right now. It's like about lunch, sorry.

**Branko Kral:** Cool.

**Jordan Dearsley:** What's up, buddy? All right. Cool.

**Marcel Santilli:** That was cool. Thank you.

**Richard Ou:** Yeah, that was great.

**Jordan Dearsley:** You guys are killing it on social, man.

**Marcel Santilli:** I got to take some notes. That's great to hear. How long have you been committed to posting often, Jordan?

**Jordan Dearsley:** We have someone in-house who kind of goes right. Yeah. I personally have not written in a while.

**Marcel Santilli:** I figure, but it's like, how long have you been doing that? Probably about four months or so.

**Jordan Dearsley:** Four months? Okay, cool.

**Marcel Santilli:** I'm going through that process right now and finding ways to develop that for other people. You guys don't need it, but it's like, you know, so it's like trying to learn as much as possible, doing it for myself as well, but then like others, it's like the most common ask right now is like, people want to be like you, essentially, you know, it's like, hey, I want to do this and whatnot.

**Jordan Dearsley:** And so that's pretty cool. What did you guys want to do? Did you guys have an agenda for this?

**Marcel Santilli:** Jürgen, can you drop the link really quickly on the agenda? Oh, did we lose Jürgen?

**Jordan Dearsley:** Matthew's alive.

**Matthew Panzarino:** Oh no, I'm alive. I'm reading. Here, let me get you a link. Let's grab the agenda.

**Jordan Dearsley:** We have meeting notes. There we go.

**Matthew Panzarino:** All right. Perfect.

**Jordan Dearsley:** All right, cool.

**Marcel Santilli:** So really quickly, high level, I can jump in a little bit, but we did some work on, there's two parallel tracks here, right?

**Marcel Santilli:** Like the, think of it as like the programmatic side, we're shaping.

**Marcel Santilli:** The editorial side, we're aligning and calibrating, right?

**Marcel Santilli:** So then it's like, think of those two separate because we want to make sure like on the editorial side, like we can deliver faster.

**Marcel Santilli:** So on the editorial side, we did some work on the content OS as well as the calibration just to get feedback.

**Marcel Santilli:** And then we'll go through a little bit on the programmatic side, like some of the inspirations and a little bit of like the, the strategy and a demo.

**Marcel Santilli:** And so maybe we can start with the content OS.

**Marcel Santilli:** And so I'm going to share my screen here in a minute and then give you a little bit of the hype.

**Marcel Santilli:** Level, how we're thinking about it.

**Marcel Santilli:** This is still like a work in progress, but I think it will be pretty good.

**Marcel Santilli:** So we need a second here.

**Marcel Santilli:** Hey, Jason. Thanks for joining us.

**Jason Gong:** Okay.

**Marcel Santilli:** So really quickly, so how we're thinking about our overall content strategy for you is we're starting to develop these clusters and what we want to calibrate with you. Inside these clusters are going to be assignments, right? So right now, think of this as giving you a taste of the kinds of assignments. This is not meant to be a definitive list—these are just to start. So for instance, the clusters here, these are 10. And so the goal would be, let's pick three to start to develop.

**Marcel Santilli:** So that's the strategy we've done with companies like Abnormal Security, right? When you have a lot of different topics, you can boil the ocean. But let's start by defining those 10 plus down to half a dozen, and then start to place bets in like three of them, right?

**Marcel Santilli:** And so these felt like the no-brainers for us to tackle.

**Marcel Santilli:** So essentially: model comparisons and alternatives around TTS models versus STT models; model comparisons and deeper dives into LLMs; decomposing AI voice agents—essentially taking voice agent architectures from first principles and defining every single aspect of it; model deep dives like, "Hey, Novo 3 came out, let's go deeper into it and be the first one to do that."

**Marcel Santilli:** And then STT and TTS top relevant topics, like for example diarization, right? Or like, what is a vocoder or what is voice cloning, you know?

**Marcel Santilli:** And then voice-related apps and alternatives. This is what 11 Labs does really well, and a lot of their traffic comes from this kind of stuff—breaking down what these discrete bets are, other features, benefits, and things like that. It's essentially, you know, the most popular voice-related apps are apps that have either voice functionality or text-to-speech or speech-to-text functionality, right? Maybe we stay away from text-only stuff, so it has to have some voice aspect to it. And this is where you're building topical authority around those apps, but it's not quite a programmatic play like we did with DeepGram, which was too broad for this.

**Marcel Santilli:** And then voice-related listicles—this is also where 11 Labs does a lot of this. It's mostly like "best [category] apps," "[competing things]," that sort of thing. And then if you look at Zapier, I think like 60% of their traffic is pretty much listicles of categories.

**Marcel Santilli:** And then compliance topics—we can develop more as we get into enterprise topics. Compliance is a big one, and we can start to develop deeper dives into clusters of topics. But I can pause here. Thoughts, reactions? Take any of these that you're like, "Hey, this is awesome, let's prioritize it."

**Jordan Dearsley:** Essentially anything that involves stuff that they would be searching for when building. So yeah, the models across the stack and model comparisons across the stack—that's great. I think we can also do other integrations, like telephony where Twilio has stuff, knowledge-based integration, people, AI workflows that are usually used like Langchain and Langfuse. I think that's more observability, but just various different tools, both on the interface side. WebRTC, telephony, all the different telephony providers, and knowledge-based providers as well. I have a set of articles that I put on the docs. I'm going to do some generative SEO myself, trying to find where they are that are decent.

**Jordan Dearsley:** Perfect.

**Marcel Santilli:** That's helpful.

**Marcel Santilli:** For the telephony providers, some of those—what is the intent behind it when they're searching for that first? We'll do research, but what exactly is the intent?

**Jordan Dearsley:** Like, telephony—they're trying to plug 11Labs into Twilio or something.

**Marcel Santilli:** So an example here on the telephony side might be an integration guide. Yeah, it's just the integration side.

**Jordan Dearsley:** So we only have Telmex in there, but there should be Twilio. We just forgot. And then different permutations of model providers that are being used in these guides—Deep Gram plus 11Labs plus Twilio, or Assembly plus, you know, whatever, those sorts of variations.

**Marcel Santilli:** So it's like the recipes, essentially. This is probably one of those that would be highly technical, highly specific. It would require a little bit more review to make sure we're getting it right. The volume would be low, but then the intent is extremely high, right?

**Marcel Santilli:** And I think those are important. If you think about that versus the more higher volume, slightly lower intent, but still highly relevant stuff. It would be good to have some of those in there.

**Richard Ou:** If you have compliance topics, I would say best practices—safeguards and guardrails.

**Jordan Dearsley:** Voice agent guardrails. Yeah.

**Marcel Santilli:** Are there examples related to this?

**Richard Ou:** What we usually tell customers is, generally, when we're dealing with them, how can you make it feel like the AI agent says the right thing that you programmed it to, and can handle the edge cases.

**Marcel Santilli:** Okay.

**Marcel Santilli:** Like, yeah, edge cases.

**Marcel Santilli:** Cool.

**Marcel Santilli:** Yeah, like, so, like, the strategy that I would highly recommend, this is amazing feedback, by the way, so thank you.

**Marcel Santilli:** So the strategy that I'm recommending here is, like, building our way into topical authority from different parts of the stack, while also building it from, like, a, like, more, almost, like, not consumer level, but almost sandwiching it a little bit, right?

**Marcel Santilli:** So if there are people searching for Descript, that's great. You get the volume, you get some of the links, you start to establish yourself, and it's related to what you're doing in a way, but it's also starting to get you visibility.

**Marcel Santilli:** While at the same time, you're going a lot deeper into, for example, if someone is in the rabbit hole of looking into every single STT open source repo out there or framework or anything, you're doing deeper dives or you're at least curating a lot of stuff and becoming really valuable resources.

**Marcel Santilli:** And it's like we're trying to sandwich that because one is going to have low volume and it's going to be kind of harder, whereas the other is higher volume, lower intent, and more of a coolness factor to a broader audience. And then this, I think, will complement really well with the programmatic side, ideally.

**Jordan Dearsley:** Yeah, sounds good.

**Marcel Santilli:** I'll stop sharing here. But anything else—if you had to pick the top three clusters, what would you pick?

**Jordan Dearsley:** Yeah, the model comparisons are pretty good, and then the STT, TTS guides, I think, are probably the best. You can always get started on those, right? And then the rest of them we're still working on.

**Marcel Santilli:** Yeah, like, we'll still continue to develop the rest, and it doesn't mean that we can't plant a seed here and there in these other clusters.

**Marcel Santilli:** You know, it's just, like, some of these clusters are going to require us to do an entire calibration for just one piece and then get that one piece right.

**Marcel Santilli:** And it's going to look very, very different from, like, you know, a model comparison one.

**Marcel Santilli:** It's like, we need to calibrate, we need to get the formatting right, we need to get the, like, the outline right, if you will, right?

**Marcel Santilli:** And where we get the right inputs, they're going to be the highest quality.

**Marcel Santilli:** And that's going to look very different than a definitional.

**Marcel Santilli:** Posts, right, on a technical topic.

**Marcel Santilli:** And that's going to look extremely different from a listicle and it's going to look even more different from a deep dive into HIPAA compliance for voice agents.

**Marcel Santilli:** If we try to do all five at same time, we can, but then the quality might not be as bullseye target as you might want for the first version.

**Marcel Santilli:** Makes sense.

**Jordan Dearsley:** And it would be great to just do any open source models, especially like the newer ones on the GTS side.

**Jordan Dearsley:** I'm getting a lot of buzz recently.

**Jordan Dearsley:** Okay.

**Marcel Santilli:** Perfect.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Start here ASAP.

**Marcel Santilli:** All right.

**Marcel Santilli:** Sweet.

**Marcel Santilli:** That's super helpful.

**Marcel Santilli:** We do have a calibration piece that we can share offline and just get high-level notes.

**Marcel Santilli:** But I'd love to maybe pass it over to Jason to just kind of cover a little bit of like the programmatic side first.

**Marcel Santilli:** Cool.

**Marcel Santilli:** And then we'll record some looms by tomorrow and send it over as well just to make better use of this time.

**Jordan Dearsley:** Great.

**Jordan Dearsley:** you.

**Jordan Dearsley:** Thank

**Jordan Dearsley:** Cool.

**Jordan Dearsley:** Yeah, nice to meet you guys.

**Jordan Dearsley:** I know it's the first time.

**Jason Gong:** But I think, like, I'm going to talk about the integration pages because this is a nice segue.

**Jason Gong:** Like, I think the vision here is there's a nice web, kind of like what Fathom does, where, you know, you have integrations, you're going to have crazy authority for, like, any voice model connecting to any other tool that's relevant.

**Jason Gong:** And then in that same vein, under that structure, you're going to have all these, like, almost like recipes, templates.

**Jason Gong:** Some are going to be the voice agents, and then some, I was poking around at it, your workflows, like, will be a little bit more kind of, like, workflow-based.

**Jason Gong:** So I think I mainly just want to cover the voice agents.

**Jason Gong:** I think you shared a lot of, like, really cool kind of ideas there.

**Jason Gong:** We have kind of, like, mocked up stuff.

**Jason Gong:** But just for inspiration, I think the intent you're going after, one, yes, is the voice agent stuff.

**Jason Gong:** I would say the intent for search on that is still, like, kind of nascent.

**Jason Gong:** It exists.

**Jason Gong:** It exists.

**Jason Gong:** It It It It

**Jason Gong:** But there's almost, like, nice tangential kind of, like, interest that I think could feel really nicely around chat that we can explore as well.

**Jason Gong:** Like, when somebody searches for, like, hey, I want an insurance agent chat bot, I won't know if that intent is super clear that they want purely text or, you know, they just want an AI.

**Jason Gong:** Fair.

**Jason Gong:** And honestly, we have lots of people who have implemented generative chat that want to use voice.

**Jordan Dearsley:** So there's something.

**Jordan Dearsley:** That's good validation.

**Jason Gong:** So I think how I'm thinking about it is, like, I think that's the universe we're going after is not necessarily voice agents, but it's kind of, like, all the things in there.

**Jordan Dearsley:** Got it.

**Jason Gong:** Yeah, so inspiration-wise, you know, there's lots of products that do templates, but this chat bot one actually has nice templates for chat, and I found this voice flow one where they're honestly kind of, like, eating your lunch, and they even have you guys in there.

**Jason Gong:** So it just kind of exists.

**Jordan Dearsley:** We definitely should publish here.

**Jordan Dearsley:** Yeah.

**Jason Gong:** As far as strategy, yeah, I mean, I said, like, I think at the beginning, let's do voice and chat, and then we'll dig deeper and figure out kind of.

**Jason Gong:** Where all the use case kind of interest is as far as keywords go.

**Jason Gong:** then what you shared was super great.

**Jason Gong:** Honestly, that prompt you wrote for creating.

**Jason Gong:** Yeah, it's you need.

**Jason Gong:** I mean, it literally, like, it is all you need.

**Jason Gong:** So this is just, you know, excuse the horrible design, but just more for, like, the concept.

**Jason Gong:** You know, I think, one, it's going to be really interesting to kind of use this and interlink between the integrations.

**Jason Gong:** And then as far as, like, what this page is trying to accomplish, I think it's actually two things.

**Jason Gong:** And it's really similar to what we're doing for Webflow.

**Jason Gong:** And it's like, like, half of this is to catch organic content.

**Jason Gong:** So people who have no idea, you know, what that be is searching about voice agents and chatbots.

**Jason Gong:** And how we cover that is, like, you know, when they search for that stuff, they're not necessarily looking for, like, a kind of ready-to-go template necessarily.

**Jason Gong:** Like, that's helpful information to have.

**Jason Gong:** They're more so thinking about, like, should I?

**Jason Gong:** You know, what are my options?

**Jason Gong:** What are the benefits?

**Jason Gong:** So on this page, we want to cover that.

**Jason Gong:** And then at the same time, we want to give them, you know, a path into your product.

**Jason Gong:** So this is, I think I just made one for like a, let's say you're doing like a, like somebody calls to file an insurance claim or something like that.

**Jason Gong:** This is like, you know, what you would then use, I guess, in Vapi, we'll have the CTAs there.

**Jason Gong:** You can call it on this page.

**Jason Gong:** So that's one half of the intent.

**Jason Gong:** And then the other half, I think, is like, more for enabling your users, which, like, I'd be interested to learn more there, like, what their usage patterns and journeys are.

**Jason Gong:** So like, if they use your product, you know, and they just want kind of not a cold start and to start with like something existing, like what their interests are there.

**Jason Gong:** Yeah.

**Jason Gong:** If we can mine that, I think that would be a nice set of things, set of pages as well.

**Jordan Dearsley:** Like you're saying, like, if we can use the current user data to inform.

**Jordan Dearsley:** like, I guess I wonder what that would be.

**Jason Gong:** So like one, I think you're, you're done.

**Jason Gong:** Search would be really nice to get access to.

**Jason Gong:** Well, GrowthX maybe not that interesting for use cases, but didn't we give you a sheet with the top use cases?

**Jordan Dearsley:** I think you guys put it in there, or Marcel did.

**Jordan Dearsley:** Yeah, yeah.

**Jordan Dearsley:** Okay, that's fair.

**Jason Gong:** And then I guess in here, I don't know if you guys do anything to see what voice agents people are already creating. There's a bunch of people creating the same thing we can make a template for, basically.

**Jordan Dearsley:** Yeah, I think it's in that sheet that I shared with Marcel. And that goes over all the users who have hit 1,000 minutes, and it gives you an idea of the more popular ones.

**Marcel Santilli:** And also what will be cool is later on, we can even add a third tab that is sample conversations or sample things. Because often people want to just see a quick sample. Like, one of the things we did with DeepGram was also provide sample queries, if you will, for those agents. So it's essentially like you just want to kind of hit play—you don't want to actually have the conversation.

**Jason Gong:** You could have like mock conversations and then throw it up on YouTube and then catch some of that SEO as well.

**Jason Gong:** Yeah, yeah, that's that's interesting.

**Jordan Dearsley:** We've seen those go decently viral on LinkedIn from some startups who want to make demos of real people talking to actual voice agents. I don't know if there's something generative to do there or just generate thousands.

**Marcel Santilli:** Like we should do a voice demo. I have a ton of ideas. But there's some good stuff we can do on that.

**Jordan Dearsley:** Perfect.

**Jordan Dearsley:** As as like other work streams go, like we're kind of piloting ghostwriting for founders.

**Jason Gong:** And once we have something there, run it by you guys. But I think you guys probably have some of the most viral content.

**Jordan Dearsley:** I'm glad to see some progress on the generative stuff or on the showcase page as well.

**Jordan Dearsley:** What are you guys thinking for the next week?

**Jordan Dearsley:** Like you said, we're going to have some articles ideally ready for review in a couple days.

**Jordan Dearsley:** What is it going to look like?

**Jordan Dearsley:** Yeah, so from here, there's, like I said, parallel tracks, right?

**Marcel Santilli:** Just a quick context on Jason that I think we missed a little bit here because we're just running fast and furious. So Jason had a growth role for Bardeen AI, and he put a catalog of recipes and such there, and it blew up and really helped them. He had so much knowledge already of a lot of the stuff. I wanted to get his help to just supercharge this so you kind of see our commitment to trying to help. We're throwing everything we can at you.

**Jordan Dearsley:** We move as fast as we can here. And so from here, three things.

**Marcel Santilli:** One, we already did the calibration. We'll send it to you. Just keep in mind, we'll do a light calibration version for each cluster because they might be very different. And now we're going to take those four clusters that we flagged and develop them further before we come back to the other clusters. So we can really double down and come up with at least 30 to 40 assignments per cluster. So now we'll essentially have the next three to four months worth of content for us to focus on. Not to say that's 100%, but we can do an 80-20 split. Some weeks it might be a 50-50. If there's something random we need to jump on, once we're in steady state, we can respond very quickly. Right now, it's better to just focus a little bit. So we'll start with that. But pretty quickly, we'll see one, two, or three articles per cluster per week. And then we'll start to watch the signals.

**Marcel Santilli:** And so my hope would be by end of next week, assuming we're not locked on publication and access to hitting publish and we're good on calibration, we can at least publish our first one if not two, right? And get that going on the editorial side. Then from there, we'll start the weekly cadence of, "Hey, these are the assignments we're working on this week." About four or five weeks from now, we can look back and be like, "Hey, we published 30, 40, 50 articles. Here's the signals we're seeing. Let's add another cluster or double down on this or that, right?" So we can kind of play with it.

**Marcel Santilli:** And then on the programmatic side, we've already engaged a designer and web dev. We wanted to just conceptually get some of these ideas in front of you with an actual prototype rather than full-on detailed design and delaying it. So it sounds like we're in a good ballpark. We can create one sample page for early next week. And then assuming we get the content approved, we can do a more fine-tuned design and implement the template on your site. But my guess is it would be a little aggressive if we get all of that done next week—design, prototype, content, template live on the website. So most likely we'll spill over into next week. But once we get that, it really accelerates from there, right? We don't want to go so fast that we misstep. So the editorial work is hopefully buying us time to get this right, and to slow down before we speed up.

**Jordan Dearsley:** Pretty good on my end. So you're saying for next week, we're hoping to get the first couple of articles out?

**Marcel Santilli:** Yeah, exactly. Do at least two articles.

**Marcel Santilli:** And then from there, every week we'll post articles for the different clusters, those four clusters that we'll develop further.

**Marcel Santilli:** But then we're also developing the assignments further.

**Marcel Santilli:** Right.

**Marcel Santilli:** So now that we have the right direction and we understand which clusters will focus, now we'll go come up with like, let's go find every single open source TTS model, every single open source STT model.

**Marcel Santilli:** Let's go like do every single combo of one to one of every single one of them and then like develop the entire cluster further.

**Marcel Santilli:** And then select the ones that are the most most critical.

**Marcel Santilli:** So most likely like will be like you mentioned, TTS open source ones are getting a lot of hype online right now.

**Jordan Dearsley:** Cool.

**Jordan Dearsley:** Yeah, that sounds good.

**Jordan Dearsley:** If there's anything that we can do on our end, if you want to try to upload anything, feel free. Our priority is just moving quickly. You don't even have to wait to put a bunch of stuff together. If you just want to send what you have as just-in-time production, that's good with us.

**Marcel Santilli:** Quick question: do you all have any way to sample these models already available on the platform? So for example, if people want to just hit play, if not, we can find different ways later to sign up for 11Labs and create some samples. But if you already have stuff like that, that would be helpful.

**Jordan Dearsley:** Yeah, there are.

**Jordan Dearsley:** If you can log into our platform or go to Voice Library, you should find samples for every voice or at least for most of them. And they're just downloadable via a URL from the API if you just want to embed them when you click play. I think that will be helpful. We'll work on that on our end.

**Marcel Santilli:** It might not be phase one, but phase two of enrichment in these articles. The more we can deep dive into 11Labs, or whatever voice, with samples—so people are finding examples and have that intent—and then they have all the samples there, I think that will help, or at least a way to fast-forward through them.

**Jordan Dearsley:** And then when it comes to the programmatic side, is that going to be hosted?

**Jordan Dearsley:** You guys have a GitHub repo you're going to share with us? Should we set something up so you guys can start pushing there?

**Marcel Santilli:** Let me talk internally. What I found works really well is using something like Airtable and then syncing that with Supabase and then querying Supabase dynamically. That will probably work better than the repo because we can't paginate and query repos the same way you could a database. Once it gets into the thousands, for now it's not an issue. But when you're into 10,000 or 5,000 pages, you need a way to manage it better. Right now we can literally put the final content anywhere. So if that gets us to live faster, done. But if you want to just do markdown files in a repo and pull from that, I have no particular preference.

**Jordan Dearsley:** You guys know what can make it rank and be invisible on SEO. So just do it. Whatever you guys recommend, we'll roll with it.

**Marcel Santilli:** For the blog, are you guys using a CMS or don't have one yet?

**Jordan Dearsley:** We're using KeyStatic. Yeah, I think we gave you access. Henry can confirm.

**Marcel Santilli:** If we can use that same approach for this phase—whatever we're doing for blogs and articles, we can do that for the programmatic side. Let me know if you need access.

**Jordan Dearsley:** I think we should have given it to you in the onboarding doc. Sounds good.

**Marcel Santilli:** Jason, you and I can connect offline on getting dev and design access ASAP to develop the pages.

**Jordan Dearsley:** All right. We're moving fast. Fast and furious. I'm excited.

**Marcel Santilli:** I can't wait to get this thing live so we can start talking about it, sharing, and developing fun ones too. Richard, do you have anything to add?

**Richard Ou:** Sounds good. We'll share more stuff too by tomorrow.

**Marcel Santilli:** Perfect. Thank you.

**Jason Gong:** Thanks, everyone. Talk soon.

**Jordan Dearsley:** We'll see you next week.
