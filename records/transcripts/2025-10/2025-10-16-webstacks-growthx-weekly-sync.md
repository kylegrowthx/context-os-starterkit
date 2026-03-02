# Webstacks <> GrowthX - Weekly Sync

<metadata>
date: 2025-10-16
time: 16:30 UTC
duration: 34 minutes
organizer: team@growthxlabs.com
participants: Rachel Pasche (GrowthX), Jakub Rudnik (GrowthX), Jesse Schor (Webstacks)
fathom_recording_id: 94714957
fathom_url: https://fathom.video/calls/441982282
share_url: https://fathom.video/share/WBoADuU9BRMoF8hXKy-KbJxuGi_csxsb
source: fathom
enriched_on: 2026-03-02 11:47 UTC
</metadata>

---

## Summary

Webstacks and GrowthX established a new content workflow centered on coffee chats: each conversation yields a 1,500-word article plus extraction of 2-3 related topics for additional content creation, with a target of 5-6 coffee chat pieces per week. Jakub completed several infrastructure updates—categorizing all uncategorized content in Looker, setting up AI content cohorts, and implementing Scrunch to track WebStacks' performance across LLMs (Claude, Gemini, Perplexity). The team also aligned on using WebStacks' existing ClickUp tag hierarchy as the source of truth for content categorization, and Jesse confirmed the community platform is live with an upcoming monthly "AI for web management" session launching next week.

---

## Context

WebStacks is an external client that GrowthX is working with on content strategy and AI visibility. This is a weekly operational sync between the GrowthX content team (Rachel handling creation, Jakub handling analytics and tool setup) and Jesse Schor from WebStacks. The relationship centers on building out WebStacks' content library and tracking how that content performs in AI search results—a critical strategic area for WebStacks. The team has moved from ad-hoc content creation to a more systematic workflow driven by WebStacks' coffee chat interviews, which serve as the source material for pillar pieces and related content refreshes. Recent progress on analytics infrastructure (Looker and Scrunch) now gives the team visibility into content performance, setting up for data-driven content decisions going forward.

---

## Relevance

**To GrowthX Delivery:**
- Refined content production system: 1,500-word coffee chat articles + 2-3 extracted topics per week creates a scalable template for client work. This workflow is portable to other clients doing thought leadership content.
- ClickUp + Airtable + Looker integration established a multi-tool content ops stack that GrowthX can replicate for future content production engagements.
- Content interlinking and refresh strategy (using existing library to enhance new pieces) improves SEO and topical authority for clients—key delivery lever.

**To CheckThat:**
- WebStacks is tracking content performance in Claude, Gemini, Perplexity, and other LLMs via Scrunch—direct validation of AI visibility importance to clients.
- Scrunch monitoring will show how WebStacks' content gets cited and positioned in AI overviews, providing real-world AEO data we can reference.
- Monthly community sessions with thought leaders and practitioners (starting with "AI for web management") create content soundbites that could feed CheckThat research and case studies.

**To GrowthX Business Development:**
- Account expansion signal: WebStacks is investing in infrastructure (Looker refresh, Scrunch setup, community launch) which indicates confidence in content strategy. Community platform suggests they're positioning as an authority—potential for expanded scope.
- Reference potential: WebStacks' AI visibility progress and community reach could make them a strong reference for other clients evaluating content + AEO services.
- Knowledge capture: Jakub's documentation of the coffee-chat-to-content workflow creates reusable IP that can accelerate future client engagements.

---

## Overview

- New content workflow: Coffee chats → topic extraction → content creation (1500-word articles + related pieces)
- Looker updates: Uncategorized content categorized, AI content cohorts added, custom clustering to be refined
- Scrunch LLM visibility tool set up to track WebStacks' content performance in AI search results
- WebStacks community launch and upcoming AI for web management session

---

## Key Topics

### Content Strategy Refinement

  - Reduce coffee chat articles to \~1500 words for more concise content
  - Extract 2-3 topics from each coffee chat for additional content creation
  - Integrate new content with existing library through refreshes and interlinking
  - Aim for 5-6 coffee chat articles per week, adjusting based on length and quality

### Workflow Improvements

  - GrowthX to access WebStacks' ClickUp for better content organization and topic tagging
  - Weekly content planning: Select coffee chat, extract topics, plan related articles
  - Jesse to export WebStacks' existing tag hierarchy for more accurate content categorization in Looker

### Analytics Updates

  - Looker: Uncategorized content now categorized, refreshes every 12 hours
  - AI content cohorts added for tracking performance (e.g., "AI for web dev", "chapters")
  - Custom clustering to be refined based on WebStacks' existing tag hierarchy

### LLM Visibility Tool Implementation

  - Scrunch set up to track WebStacks' content performance in AI search results
  - Monitors queries, position, sentiment, and citation frequency across various LLMs
  - Data population in progress; more insights expected in the coming weeks

### WebStacks Community Initiative

  - New community launched with Slack channel
  - Upcoming session on AI for web management, featuring technical CMS insights and content strategy discussion
  - Monthly sessions planned on various topics, providing potential content soundbites

---

## Action Items

**Jesse Schor (Webstacks)**
- Add Rachel & Jakub as ClickUp guests; tag coffee chats by topic
- Export tags JSON; send to Jakub for Airtable/Looker mapping

**Rachel Pasche (GrowthX)**
- Send coffee chat draft to Jakub via Slack for content analysis

**Jakub Rudnik (GrowthX)**
- Fix Looker impressions tracking; then add AI/chapters to non-branded cohort
- Send cohort segmentation proposal to Jesse; then implement after approval
- Confirm Scrunch client invites; then invite Jesse
- Document coffee-chat-led content workflow; share w/ Jesse, Rachel, Jessalynn

---

## Transcript

**Jakub Rudnik:** What's up, guys? Welcome to, welcome to gardening talk with Rachel.

**Jesse Schor:** Nice.

**Jakub Rudnik:** How are you doing?

**Jesse Schor:** Gardeners. Yeah, Rachel's just went to frost because she's up in the elevation. Yeah, we did some gardens, garden beds in Chicago, but there's no garden here, but there's plenty of backyard for it, so I'll have to start fresh. I like to cook, so I like having the fresh produce and the herbs especially, so I'll have to get everything going again.

**Jesse Schor:** Very nice. You're in Cincy now, right?

**Jakub Rudnik:** Cleveland, but yeah.

**Jesse Schor:** That's it. Nice.

**Jakub Rudnik:** Yeah, week three, almost in the books. My wife has been out of town for two of the weeks. Very fun to have moving, you know, being the single dad for half of each week, and so we're getting through, but it's good. Our friend's kid started in the same daycare room as our kid today, so he's got, like, his best friend. I mean, two-year-old best friends, but still, that's pretty cool.

**Jesse Schor:** The plan is coming together.

**Jakub Rudnik:** Yeah, for real.

**Jesse Schor:** What do you like to cook?

**Jakub Rudnik:** Yeah, I'll cook a little bit of everything. I've been trying to diversify, especially post-pandemic. I use the New York Times app a ton, and often I'll just go to the grocery store, see what's on sale, figure out what proteins are available, and then just throw that in. Especially when the garden's going, it's protein plus veggie and see what comes up. So just try to do a little bit of everything. It's about to be stew and soup season, so I'd not done anything like that before, like two years ago, so I've been trying to build out kind of my repertoire over there. I used to grill a ton—that was obviously my first thing—and got a smoker, but now I've been more into stews. They're hardier and more layered, longer cooking has been kind of my thing this last year or so. Different cuisines, different spices. My wife goes along for the ride usually, but she comes from a very bland food household, so she's had to learn to adapt to me.

**Jesse Schor:** Very nice. I love it.

**Jakub Rudnik:** Let's see. Jessalynn made up the agenda. I think mostly the stuff that we covered last week made progress on those things. Yeah, anything to add from your end before I jump in and go through?

**Jesse Schor:** Let me just bring that back up. I don't think so. Yeah, want to talk about the coffee chats and the new cohorts.

**Jakub Rudnik:** So that's perfect. I think we're good. Yeah, Rachel, what's this that I've been less into now in the coffee chats? I was more on the analytics and stuff side. Yeah, I guess that question probably is most of the talking point, but anything to add there and then let Webstacks answer?

**Rachel Pasche:** No, I don't think so. I sent two, and then I think of the two, one, I'm wrapping up feedback, and so then I think one is pretty much ready to go, and then the other one, once I get to fixing the feedback on that one, both of those will be ready to publish, and then next week we'll probably have a few more as I wrap up the internal linking stuff.

**Jesse Schor:** What do you, what do you think is like a realistic pace on these?

**Jesse Schor:** I know this was like our first batch, but like.

**rachelpasche:** Yeah, I think we'll probably aim to like, I guess it depends on how you feel about the length of the first two.

**rachelpasche:** Like if they were long enough, or if you felt like they should have been longer or shorter, like if you like.

**rachelpasche:** The pace, then we'll probably aim for about five or six a week.

**rachelpasche:** And then if you want them to be shorter, we'd probably do more or longer.

**rachelpasche:** We'd probably do fewer just to kind of keep it within like the same ballpark of like words per week.

**Jesse Schor:** Cool. How many words were each of these?

**Rachel Pasche:** I think maybe like 2,500, something like that. Let me look. The one was almost 3,000. So it was like 2,900.

**Jesse Schor:** And I think the other one was a little less. I think it was like 25 or 24. I think we probably can cut it down a bit to be a little bit more succinct on it. I also think some conversations are just objectively better than others. Like we get more out of the discussion. And I think sometimes just naturally we're catching someone when they're maybe at their best versus someone that maybe is jumping from back-to-backs and is maybe not as clear on some of the responses for things, which I think is normal. So like I think we can probably reduce them a bit and then there might be some that we can send your way and be like this is a really good one, let's extract everything we can from it. I would rather that we're able to start layering some of these in.

**Jesse Schor:** I know we have like a pretty solid batch of probably like 10 conversations, we've done two so far there's like more we'll get through, but also realistically we don't always have week over week like a lot of these. What I would like us to start being able to do is saying almost kind of like ordering up a menu of like, okay, we're going to do like three of these 1500-word coffee chats because like we have them this week or maybe two of them this week. And then we're also from those coffee chats going to take some of these like topics that we discussed. And I think like we can kind of give that direction like when we share it and either add to content that exists already. So like I would ask like from your guys' end to do a little bit of research on like the content that we have. And maybe there's something that we can have that like we can use some of the coffee chat takeaways and like incorporate that into updating an article or writing something new that's like a relevant topic around it. And I think like layering those kind of pieces together will really help. One, like the perspective of, you know, Webstacks touching kind of all of these different articles, but then two, I think it'll help us kind of keep diversity rather than treating like, okay, this week we're just doing coffee chats, next week we're doing blogs, next week you know, and so on. And you can even see like some of the comments I left you, Rachel. I like made a note on one with the combo with enterprise websites. And then like, I just did like a quick search on like enterprise websites. And like, we have a lot of articles related to enterprise websites—best tech stack, design styles, you know, migrations. But like, that could even be like a perfect example of something that we could say, like, hey, let's do an enterprise websites pillar-style page, like what is an enterprise website? What makes an enterprise website enterprise? And I think like we can kind of build off of some of those things to influence the other content.

**Rachel Pasche:** Yeah, I think that sounds great. So do you see that as like sending over kind of like a brief for the week and being like, okay, this week we're going to do this coffee chat and then I want to expand on some of the concepts explored here into like a pillar piece, two refreshes, whatever?

**Jesse Schor:** Yeah, I would ask you guys in terms of like workflow, what makes the most sense in terms of info to like provide versus like what stuff you guys can also explore. My kind of baseline thinking is that like each time we meet, by the time we're ending this call, if we're clear on here's kind of the order for next week, then we can kind of go from there and we can even like provide some of that context to you guys on these calls. Like if we look at kind of almost like a backlog of coffee chats, if we have them recorded already or if like we just had some this past week and we like share those with you guys during this call or ahead of time on this call, we can give some context into like, what was the discussion even about? And yeah, I guess, is it easier for you guys or is it better for you guys to like have the detailed topics, outlines, things like that? Is it better to just like give you the coffee chat, let you guys go through it and that's kind of like the starting point for like what topics we might want to dive into and you guys can do your own research? What do you think is like the best?

**Rachel Pasche:** I'm kind of speaking for Jessalynn here, but I would guess that kind of just taking like whatever coffee chat, whether we just pick one from the list and go from there, I feel like it's probably easier to like plan it out in advance on our end just so that we can kind of work at the pace that makes sense. Because sometimes we're not always like exactly lined up week to week. Like we're more like by the month, if that makes sense. So then I think it makes the most sense to kind of organize like some pillars, like pillar pieces and refresh schedules and stuff around the topics that are in the coffee chat. So as long as we continue to get like a batch, you know, every so often of coffee chat articles, then I think we can kind of develop a content strategy around those. But I think that's probably what makes most sense.

**Jakub Rudnik:** I think that's right. We'd have to do a couple to understand like what the cadence, kind of what Rachel was saying there. But I think that's right. You send over this coffee chat that's really good. You know, like you're saying, there's some that are better than others. This one really works. Then we can go through it and like spending some time in your Looker. Obviously I know that you have an extensive content library, but I like refreshed myself on how deep it is and how many different things we've done. And so there'll be a ton of opportunity there. And these things can help to intersect pieces. There's refreshes or interlinking that we should be doing, not just with these new batches that we've done, but just across all your content, because we've just done so much over time. And there's always a need for freshness. So this gives us like the ability to kind of patch some holes with new topics. We'll just need a little bit of runway on each kind of cluster or whatever we want to call it.

**Jesse Schor:** Yeah, I think I'm following. The planning piece of things too, I think like we can do around like our core, like we know kind of like the core pillars that we have. And I'm almost wondering like maybe what we can do is, because you guys have access to our ClickUp right now, right? Like where we've been putting the coffee chats?

**Jakub Rudnik:** I don't use it. Rachel, do you use or have access to the ClickUp? I'm not sure if anyone does.

**Rachel Pasche:** I put them in, like from the Slack thread, just copied them and pasted them into Airtable and that's what I'm using.

**Jesse Schor:** Yeah, okay. Maybe we can get access. I'm trying to think of the best way to do this. We take all of them, and we kind of organize them by topic in our ClickUp. And so maybe we can just like, I can add you guys to that as like guests, even to that page. And then we can add some like tags just next to the coffee chats when we put the link up. And that can at least broadly and maybe like directionally give some context into what the conversation is about or what topics were discussed. And then we can kind of run what you're talking about, Rachel, from there. But like at least from like a high level, when like we have these meetings, we can kind of look at like a backlog of all of the recordings that we have kind of accumulated and get like a sense of like, do we have a coffee chat that would make sense to like layer in and then pad two or three topics from that. And then that way, like going into the next week, you are kind of clear on like, okay, I'm going to write 1500 words for this coffee chat. And I'm expecting to like extract some, you know, two to three topics or two to three other articles from this that are somewhat related to like these topics. Does that make sense?

**Jakub Rudnik:** Yeah, I think that makes sense to me. I think we'll see different scopes of like, you know, that two to three is like a good placeholder number. Sometimes we're going to open up like new veins where we're like, oh, this is perfect. There's 20, how far do we go? And I think we just scope it and bring it back to you and be like, here are the opportunities. And sometimes that will be, we've done a lot of content in this area, this is more on the refresh front. And sometimes this will be a brand new vein that we have tons of new content ideas from. Sometimes there'll be one or two. So I think that cadence will work. Like bring us, like we, you know, select that coffee chat or coffee chats. We come back with that research, like kind of approve it. And then the next week or two of content follows behind. So I think roughly that works. We just have to do it in practice and see what like order of operations happens.

**Jesse Schor:** Okay, cool. Well, I guess as like the takeaway from here, we can take a look at coffee chat. Do you already have any others, Rachel, in progress or just the two that you sent us?

**Rachel Pasche:** I've got the two so far. I was kind of waiting to see like how we felt about the length and stuff before I moved on. Just so I wasn't like having to work backwards.

**Jesse Schor:** Totally. So let me look at the coffee chats that we have and then maybe queue you guys up like after this call. So to just like share, okay, like let's focus on this one. These are the topics. It'll kind of be like a crude version of the process I just like shared. And then like next week, let's plan to like hit that plus, you know, two or three articles, whatever you think is doable for us to maintain like our word count. And by the time we meet, you know, a week from now, like the first dry run, so to speak.

**Jakub Rudnik:** Yeah, let's do that. I can take a crack at that like crude version as you're saying of the strategy or that selection and analysis of our existing content. And then I document that so Rachel can do that going forward. So, Rachel, just send me over the coffee chat that you've worked on. I know it exists, but just if you would Slack me and then I'll carve out time. I think that will help us to cover new ground, but be really, I don't know, cover a lot of like the connections, the refresh, the make each new piece of content work with existing stuff. So I like the format. Okay, cool. The next thing.

**Jesse Schor:** I was going to ask about the Looker.

**Jakub Rudnik:** Yep. Looker is, well, I've got a couple of things here. We, I updated all of the uncategorized content that didn't have a cluster. I think this was more from like a previous contributor, but I've updated all this. And then just let me know that this refreshes every 12 hours. I just finished that this morning. So those cohorts will, that was one of our outstanding issues. From a new AI content, you come into cohorts with your Looker, and then do AI for web dev or anything that says chapters. Currently, that's the best way to look at the new content. So then select those chapters. It'll show us, at least from a traffic perspective, how that's pacing. So we're starting to see some growth last week, and this week looks like it's surpassing. So we can track this over time. I do still need to add that to our non-branded cohort. I do still need to fix some issues—the impressions tracking broke again. But we can at least do it at the clicks level, but we can't do it at impressions level. That should be ready early next week. And then the uncategorized again, that will divvy out those articles and we can get a little bit more granular.

**Jakub Rudnik:** You know, running through this kind of quickly, but I was looking through the different cohorts we have. There were some things I'll probably just send these async, but we had clusters already set up, right? We have these different chapters, and I think we should be reading this, but it's like web development and branding and UX/UI. There are some other things I think we should potentially segment these clusters. So like there's a little bit of security, there's localization, there's a ton of migrations. There's just a few other things I think we should possibly segment out. And we have like a decent number of cohorts already, but we just have so many articles that we can get a little bit more granular here. So, Jesse, I'll probably sync on like what's most important, whether that's like the persona or whether that's the industry. I just want to know what's the most valuable here on the cohorts, like what we did 12 months ago in cohorts. I think that doesn't necessarily reflect where we are now. And over something more succinct there was just a hard thing for me.

**Jesse Schor:** Are these like custom by you guys, or are these like pulling based off of our like tags?

**Jakub Rudnik:** It's our cluster. Yeah, cluster status. So we can change this anything we want. It's not on your backend, it's in our Looker. So it's this column here. We could update the same thing. I think that's where, again, we had 100 articles, this worked, and we did the chapters for these AI articles, but maybe those should even be one. And we just need to rethink how we're clustering this. There's a bit of path dependency that we're going to keep going down on what exists before, so.

**Jesse Schor:** Yeah, I almost wonder. So are your developers like pulling it from here in Airtable?

**Jakub Rudnik:** Yeah.

**Jesse Schor:** Okay. Yeah, I wonder if I can do like an export of our tags. And maybe we can upload that here. And then we can start using that. It would be cool to like be able to associate the tags that we're actually using with some of these things. And maybe the cluster is like our internal, like broadest category. But I mentioned that just because, like the kind of subtopic or subtagging that you're talking about. That I think already exists on like the tags that like we have on the site. We basically have like a hierarchy that's like cluster, more or less very broad, like web development, web design, SEO, like very broad. And then we have tags. So like each article can have one like cluster, one high level tag, and then as many tags as you would want underneath it. So I'm wondering if that, because I would love to like make this actionable, like any ideas that you have about the tags or the way to like differentiate them even more or like pull more out of it to categorize, I think would be helpful. And then we also have the same thing with like our segments. So like we have industries where it's relevant, we have technologies where it's relevant. And like those tags are separated, but like the intention is that they tie back to those like pillar pages that we have.

**Jakub Rudnik:** Yeah, yeah, yeah. If you can export that, that saves me a ton of headache. And also it keeps our data much cleaner because I'm sure my categorization, like, there's often choices I have to make here. When I was cleaning this up, something didn't fit easily. So I'd rather work with the data that we have and have one source of truth and use the tagging categorization we have it. But how we connect that over to Looker, I think most of it should fit cleanly, but the tags, we just have to work with our team on. So it'd be a little bit custom, but I don't see an issue there. So yeah, if you can export that, I'll put that as an action item for you all.

**Jesse Schor:** But that would be ideal. Pretty sure I can. It might just be like the JSON, but then we can kind of figure it out from there. Or I'm sure you could hand off the JSON file to like your developers and they would be able to match.

**Jakub Rudnik:** Yeah, agreed. Yeah. Send that over when you get a chance, but that solves a lot of problems and that's a way smarter way to do it. So good. Good shout there. That will populate here. Then we'll bring those into cohorts. I would imagine we have like two different views, one with the categories, one with the tags, but just a matter of aligning that to the data. And then I know we're close, but I just want to show, I did set up Scrunch, which is the LLM visibility tool. It's not a referral traffic thing. We'll still be in Looker in the LLM tab, but Scrunch will be the queries that we put in and how often they're showing up in Claude, Gemini, UI, AI, overviews, et cetera. I just finished this yesterday. So it only has one, two days of data, but each day, this is pinging all of these different LLMs with the queries that we've inputted and tracking like position, sentiment, how often you're cited. I took competitors that were automated, and then I took competitors that you gave us some of the research stages. A lot of them there's overlap, but these are starting to populate as well. You can export some of this, but they recommend prompts. And then, as I mentioned last week, I took the AI cluster that we've done over the last six weeks or so, and I moved those in manually as well. So it's a lot of like what you'd expect—things like B2B website design best practices and some of your higher level keywords that we've done historically, and those were all automated. And then I've built in like using AI in different areas, and then like AI accessibility, AI and QA automation, those things that we wrote articles on more recently. And so we're just getting some of this data. I think we'll have a lot more to show off next week. We'd have a week's worth of data, but we're starting to see some of this come in as we also get insights on like how to update our pages or recommendations from Scrunch on specific queries and pages where we might not have done optimization or what they're seeing from the content that is coming in. This is just trickling in, but so I'm going to give you a first view that this has been set up because that was one of the action items for last week. It just will take time to populate this data and give us more. We certainly don't have trends at this point, but set up and starting to run.

**Jesse Schor:** Can you invite us to this?

**Jakub Rudnik:** I believe so. We've done that with a couple clients, I believe. So I'll confirm that that isn't an issue, but I believe I can.

**Jesse Schor:** Okay, cool. Yeah, let me know. Otherwise, I'm wondering if like we should just get something like this ourselves.

**Jakub Rudnik:** Yeah, I think I'm pretty sure I can, but again, let me confirm because we haven't done that with everybody. It's like a closed, you know, clients that we work with. So I'll just make sure I'm allowed to do that before I confirm that.

**Jesse Schor:** Okay, cool. Yeah, let me know. If not, I'll just get our own account, but that looks pretty cool.

**Jesse Schor:** Well, awesome. I feel like a lot got done this past week and I'm really excited for this new workflow. So, yeah, Jakub, if you can put together kind of some documentation on like the process we talked about here, if you could drop that into the chat, something else just to like put on your guys' radar. I'm doing like the community that I was telling you guys about that we've been working on has launched and like we have the Slack channel and stuff going, but we're doing a kind of session on AI for web management. I kind of come at it from both a technical perspective, some of the things we're doing within the CMS. Nikan's going to be speaking to some of those things. And then I'm going to be talking about a lot of the things we've been working on. And so things like that are super helpful. But I anticipate that, and that's next week, that I'm going to be having that presentation, walkthrough discussion with that group. But some really interesting stuff. And we're going to be doing that once a month around varying different topics. So I think we'll have some really good soundbites from that that we'll be able to build off of too.

**Jakub Rudnik:** Nice. Yeah, I would love to see what that looks like either live or afterwards. But thanks for raising that flag. Yeah, I'll do that documentation tomorrow and send that over so we can review and then have Jessalynn and Rachel test that B1 afterwards. But I think it should all be good.

**Jesse Schor:** Cool. Sounds good.

**Jakub Rudnik:** Thanks, guys. Have a good rest of the week.

**Jesse Schor:** Bye.
