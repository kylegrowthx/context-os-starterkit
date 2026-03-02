# Airbyte <> GrowthX - Weekly Sync

<metadata>
date: 2025-10-17
time: 15:30 UTC
duration: 24 minutes
organizer: carrie@growthx.ai
participants: Jakub Rudnik (GrowthX), Carrie Chowske (GrowthX), Tanmay Sarkar (Airbyte), Mario Moscatiello (Airbyte), Nithin M (Airbyte)
fathom_recording_id: 94998434
fathom_url: https://fathom.video/calls/444263825
share_url: https://fathom.video/share/ZdzmykfvyZyuz54shnUhaUuYipx9ogs4
source: fathom
enriched_on: 2026-03-02 18:45 UTC
</metadata>

---

## Summary

GrowthX and Airbyte finalized the industry pages template and confirmed connector selection logic — using only the first tab's master list, excluding items marked for removal. Carrie reported strong SEO momentum: Airbyte moved into top-10 average position despite lower impressions, with gains in security/privacy/compliance and cloud/hybrid architecture clusters; LLM visibility jumped significantly on Claude and Copilot, likely tied to Claude's 4.5 rollout and enterprise contract expansion. Tanmay introduced the ghost website concept for AI citations and will evaluate programmatic workflow tools (N8N, GAMLOOP) to scale content production for middle and bottom-of-funnel topics.

---

## Context

Airbyte is a data integration platform and a key GrowthX content client. This is a weekly sync between Airbyte's leadership (Tanmay, Mario, Nithin) and GrowthX's content and strategy team (Carrie, Jakub, Kyle). The relationship involves GrowthX producing content around Airbyte's connectors, data integration use cases, and industry-specific applications — with Airbyte providing feedback on performance, SEO data, and strategic direction. The meeting covers regular content pipeline updates, performance metrics from Search and LLM platforms, and emerging opportunities like industry pages and new website design patterns.

---

## Relevance

**To GrowthX Delivery:**
- Industry pages template finalized; pipeline engineering in progress. Strategy: prioritize healthcare, financial services, fintech, and regulated industries first
- Confirmed connector page selection logic (master list only, exclude marked items) — removes ambiguity, allows engineering to move fast
- Content strategy shift to MOF/BOF away from TOF driven by AEO research showing top-of-funnel content heavily substituted by AI
- New connector display page design in Figma aims to improve internal link structure across site

**To CheckThat & AEO:**
- Substantial LLM visibility gains across Claude, Copilot, and other AI platforms in past month — potential signal of growing AI-driven traffic
- Claude's 4.5 rollout and enterprise contract expansion driving increased citations; Mario noted standardization trend for regulated industries choosing single AI platform
- AI platforms showing citation share drop in research, but Airbyte's position improving on Scrunch
- Ghost website concept (programmatic content at scale) being evaluated with N8N/GAMLOOP to test AI citation pickup on new domains

**To GrowthX Business Development:**
- Airbyte moving into top-10 average SERP position on quality metrics; strong gains in security/compliance/cloud architecture clusters
- Account showing positive engagement on SEO performance and willingness to experiment (Wikipedia page live, ghost site in discovery)
- Atlas feature access timeline remains quarters out; positioning GrowthX for early-access testing opportunity when available

---

## Overview

- Content pipeline: 73 topics approved; industry pages template finalized
- SEO performance: Improved quality of traffic, higher average position in SERPs
- LLM visibility: Substantial increases across platforms, especially Claude
- New initiatives: Wikipedia page created, ghost website concept discussed

---

## Key Topics

### Content Production and Industry Pages

  - 73 topics in the pipeline for upcoming content
  - Industry pages template finalized; engineering team working on pipeline
  - Clarification on connectors: Use first tab of master list, excluding those marked for removal
  - Prioritizing industries: Healthcare, financial services, fintech, and tech-forward regulated industries

### SEO Performance Update

  - Average position in search results moving into top 10
  - More keywords in top 20
  - Improved quality of traffic despite decreased impressions
  - Growth in security, privacy, compliance, and cloud/hybrid architecture clusters
  - Steady growth in homepage traffic
  - Maintaining click volume with improved quality

### LLM Visibility

  - Substantial increases across AI platforms
  - Copilot and Claude showing significant jumps
  - Potential correlation with Claude's enterprise contracts and 4.5 rollout

### Wikipedia and Ghost Website

  - Airbyte Wikipedia page created, awaiting Google indexing
  - Concept of ghost website discussed for AI citation purposes
  - Exploring workflow automation tools (N8N, GAMLOOP) for programmatic content creation

### New Connector Pages Design

  - Figma design shared for new connector display pages
  - Aims to improve internal link structure across the website

---

## Action Items

**Carrie Chowske**
- Email Jakub more content topic ideas
- Email Kyle O' (GrowthX) meeting recording re: connector pages; FYI Tanmay is POC
- Prioritize industry pages: Healthcare, Financial Services, Fintech
- Check Fivetran top-nav industries; share w/ Jakub
- Produce more MOF/BOF content; deprioritize TOF

**Jakub Rudnik**
- Follow up internally re: Atlas access timing; update Airbyte next week

**Tanmay Sarkar**
- Email Jakub ghost-site competitor example link
- Evaluate N8N/Gamloop for ghost-site programmatic publishing; share plan w/ Jakub

---

## Transcript
**Jakub Rudnik:** Hey, y'all.

**Nithin:** Hello.

**Nithin:** Hi.

**Jakub Rudnik:** Nithin, how are you doing?

**Nithin:** All good, Jakub.

**Jakub Rudnik:** How are you?

**Jakub Rudnik:** I'm all right.

**Jakub Rudnik:** It's getting cold.

**Jakub Rudnik:** It's getting chilly in the house.

**Jakub Rudnik:** Fall weather is coming in.

**Jakub Rudnik:** Where are my slippers?

**Jakub Rudnik:** I got a blanket on my lap.

**Nithin:** like, just changed quickly.

**Tanmay Sarkar:** Yeah, think it's the same in San Francisco.

**Tanmay Sarkar:** So last week it was raining and the weather is changing.

**Jakub Rudnik:** Yep.

**Jakub Rudnik:** Yep, yep, yep.

**Jakub Rudnik:** Week is coming.

**Jakub Rudnik:** I know.

**Jakub Rudnik:** Sad about it already.

**Tanmay Sarkar:** Yeah, that's a famous line from Game of Thrones if you have watched.

**Carrie Chowske:** Who gets the dragon, though?

**Tanmay Sarkar:** That's what I want to know.

**Tanmay Sarkar:** Of course.

**Tanmay Sarkar:** I think this next season is coming for House of Dragons.

**Tanmay Sarkar:** That's the prequel of Game of Thrones, yeah.

**Jakub Rudnik:** And they showed another screenshot from one of the other offshoots as well.

**Jakub Rudnik:** I saw like a early spoiler.

**Jakub Rudnik:** Oh, that one that was like, yeah, the one that was about the, what, the maester from the wall?

**Jakub Rudnik:** Yeah, yeah, yeah.

**Carrie Chowske:** When he was like younger, yeah.

**Carrie Chowske:** Might have read all the books, I don't know.

**Carrie Chowske:** Anyway, let me find, let me always have to find things on my screen.

**Carrie Chowske:** Ever since we went to like going to Zoom exclusively, I feel like I'm lost.

**Carrie Chowske:** It's like how I was when we first switched to Google.

**Carrie Chowske:** Anyway, so just to keep you updated on this regular content production, we just published, finished publishing this week's stuff today.

**Carrie Chowske:** And we've got, you know, another batch ready for next week.

**Carrie Chowske:** So, and with those topics that you approved, we've got about 73 in the pipeline.

**Carrie Chowske:** So we're good for a little while, but I'll probably send you some more topics.

**Carrie Chowske:** And then as far as our pipeline for the industry pages, we finalized the template and the engineering team is working on the pipeline.

**Carrie Chowske:** We're still a little confused about the connectors thing and I am so sorry to ask you about this again, but you want us to just pull the ones from this page that say exists or keep.

**Tanmay Sarkar:** No, no.

**Tanmay Sarkar:** So if you go to the first tab, that is the master list.

**Tanmay Sarkar:** Out of that, if you go to coming soon, just go to the other page.

**Carrie Chowske:** Oh, yeah.

**Tanmay Sarkar:** So all these are also there in first tab.

**Tanmay Sarkar:** Out of those, only these three are available, which is exist and keep mention, like which will come.

**Tanmay Sarkar:** It's not there.

**Tanmay Sarkar:** It's coming soon and we want to keep those.

**Tanmay Sarkar:** Other ones on this page will be moved to draft, like we won't make those.

**Tanmay Sarkar:** Connectors, Pages on Website.

**Tanmay Sarkar:** So you can just follow the first tab without those names.

**Carrie Chowske:** Without any of the ones on here?

**Tanmay Sarkar:** Or you want us to delete these, these three?

**Tanmay Sarkar:** Other than these three.

**Tanmay Sarkar:** Other than these three, those will be there.

**Carrie Chowske:** Okay.

**Carrie Chowske:** Okay.

**Carrie Chowske:** Okay.

**Carrie Chowske:** That helps, I think.

**Tanmay Sarkar:** Yeah, it's confusing, yeah.

**Carrie Chowske:** I got another time.

**Carrie Chowske:** It's okay.

**Carrie Chowske:** It's all right.

**Carrie Chowske:** Because I thought it was one way, and then someone goes, well, doesn't it mean this?

**Carrie Chowske:** And then that's when I asked for clarification, and then I got that, and then I was like, well, I thought I knew, and now I'm confused.

**Carrie Chowske:** So, okay.

**Carrie Chowske:** I will relay that.

**Carrie Chowske:** I will give him this recording and say, here's exactly what it is.

**Carrie Chowske:** And any more questions, I will have him reach out directly to you, because I think you guys can work that out.

**Carrie Chowske:** But I think that's pretty clear.

**Tanmay Sarkar:** I'm not worried about it.

**Carrie Chowske:** And then I was just pulling up the list of industries so we can prioritize which ones we want to start with.

**Carrie Chowske:** I think that we had originally, the one we templated out, Jakub, was healthcare, was that right?

**Jakub Rudnik:** Yeah, I think that's the one that we did.

**Jakub Rudnik:** Yes.

**Carrie Chowske:** We definitely want that one in our first batch.

**Carrie Chowske:** What other ones do we, do you have any that you specifically want to make sure that are up there right away to test out?

**Carrie Chowske:** See how they, how they do on our first batch?

**Jakub Rudnik:** Yeah, for my end, doesn't, I'm not concerned necessarily.

**Jakub Rudnik:** think more of, yeah, what's.

**Mario:** Yeah, I think like healthcare, financial services, and also like most of like the, the actual verticals within those are like health tech or fintech or, you know, like wherever there is like a tech angle to those industries, we see that it's a great intersection because those are tech forward companies.

**Mario:** But they have data regulation and compliance needs.

**Mario:** And so that's kind of like the sweet spot for us.

**Mario:** Okay.

**Mario:** Or like anything, like, again, like any, basically any vertical software industry that serves regulated industries.

**Mario:** And then, of course, you can go healthcare, manufacturing, you know, financial services, and so on and so forth, biotech, and whatnot.

**Carrie Chowske:** Yeah, that's kind of what I was thinking. I was definitely thinking the financial services, fintech, and healthcare. So we'll start in that vein and kind of branch out. I can also look at what Fivetran has, because I think they've got the top-level nav categories. That tells you who you're going after. But we can start there, and that's not a problem.

**Carrie Chowske:** Okie doke.

**Carrie Chowske:** A quick little performance update then.

**Carrie Chowske:** Really cool to see.

**Carrie Chowske:** A lot of this is kind of, there's a few things going on here.

**Carrie Chowske:** going to asterisk before I start, but of course the update to the algorithm that Google did, you guys did a site update, obviously, and then we started publishing in some of these clusters that I'm going to talk about.

**Carrie Chowske:** But those are, these are all good signs that we're going in the right direction, and there's some other stuff with LLM visibility, too, that I think is good.

**Carrie Chowske:** One notable thing is like average position, so in search results, you we're moving up into the top 10 just in the last month.

**Carrie Chowske:** A lot of that had to do with, as we saw that decrease in impressions, we saw clicks go up, and so it's because we got, we were getting more quality traffic, and we're seeing.

**Mario:** This is great.

**Carrie Chowske:** Yeah, and we're seeing a lot more keywords in the top 20, so you're really, it's a lot of, it actually helped, I think, and we're seeing that across the board.

**Carrie Chowske:** That change actually kind of eliminated some of that dead weight in impressions.

**Carrie Chowske:** So it looks bad at first, but then when you really look at the quality of what you're getting, it's a little bit better.

**Carrie Chowske:** And then these are two clusters that we started doing stuff in a few weeks ago.

**Carrie Chowske:** was kind of part of our strategy to kind of talk about topics that are specifically relevant to Enterprise Flex.

**Carrie Chowske:** And so that's the security, privacy, and compliance.

**Carrie Chowske:** That was pretty up in impressions and clicks as well.

**Carrie Chowske:** And same with cloud and hybrid architecture.

**Carrie Chowske:** Both of those grew pretty good the last month.

**Carrie Chowske:** So that's what we want to see for sure.

**Carrie Chowske:** And then, of course, still the general data engineering resources and data integration — those are still the best performers overall. But these were just the ones that I know we specifically targeted. That's where all the content we published recently has been clustered.

**Tanmay Sarkar:** And what is the date range of this?

**Carrie Chowske:** This is from August and September.

**Tanmay Sarkar:** August and September.

**Carrie Chowske:** So you're talking about 60 days?

**Carrie Chowske:** Mm-hmm.

**Tanmay Sarkar:** Cool.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** And then we're maintaining click volume more so than, like, growing it.

**Carrie Chowske:** It's gone up a little bit.

**Carrie Chowske:** But I think that, again, with the quality of those clicks going up, I think that's pretty good.

**Carrie Chowske:** I highlighted this just because it was interesting to see just still some steady growth.

**Carrie Chowske:** People are just coming to the homepage, which is probably coming up.

**Carrie Chowske:** You know, when you make major changes like that, it does boost traffic usually a little bit.

**Carrie Chowske:** So that was nice.

**Carrie Chowske:** And then also this cloud and hybrid architecture had an increase in sessions, which includes, you know, not just obviously SEO, but any visit to those, that content.

**Carrie Chowske:** So, and that's where we want them to go.

**Mario:** Yeah, that's great.

**Carrie Chowske:** Yeah, yeah.

**Carrie Chowske:** As far as LLM visibility, pretty similar to last month — pretty substantial increases across the board. We're seeing a lot more AI use. Copilot jumped on the scene for you guys a bit more, and Claude had a big jump across the board. I wonder if it's related to their 4.5 rollout.

**Mario:** It's also like Claude is, I mean, this is the interesting thing about Claude versus OpenAI.

**Mario:** think Claude is signing these massive enterprise contracts where even at AirBuy that are like in leadership, like we're thinking like, should we, I mean, we're probably not going to do it, but we're at the point where we're like, hey, should we standardize on a platform, especially as they add stuff like connectors and MCPs.

**Mario:** And so what Anthropic is doing is they're signing massive enterprise contracts where you have companies with thousands of employees who are only allowed to use Claude at work.

**Mario:** And so, like, I think what you're seeing is that there is more enterprise traffic coming from Cloud because of that.

**Mario:** Because, for instance, like, our engineers are not, like, for security and stuff because we have a special, you know, contract with OpenAI where our data, whatever, like, they're not using anything else.

**Mario:** And so, like, I think there is a bit of that with Cloud.

**Jakub Rudnik:** Sure.

**Jakub Rudnik:** That's super interesting.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** That's a good shot, Mario.

**Mario:** I think, yeah, I think, you know, Jakub, this is interesting for you guys as well because, like, yes, companies, we know because, I mean, we're building products with AI agents and stuff.

**Mario:** And what we're seeing is that companies tend to standardize so that they know that their data is under the same regulations and whatnot.


**Jakub Rudnik:** Yeah, really good point.

**Jakub Rudnik:** That's a good note across clients.

**Carrie Chowske:** Thank you.

**Carrie Chowske:** My husband came home from work last week and he works in IT for the city that we live in.

**Carrie Chowske:** And he came home and he goes, you know, last week I said to, I said, he said to the head of ITs,

**Mario:** Like, we really ought to have, like, an AI policy in place.

**Carrie Chowske:** And he brought up the one from, like, city of Raleigh.

**Carrie Chowske:** And he's like, here, I think we should kind of follow what they're doing.

**Carrie Chowske:** And he's like, ah, we don't need to worry about that.

**Mario:** And then the next week he comes back to him and he's like, oh, I heard from the top that we got to do this.

**Carrie Chowske:** And I'm like, god, you might want to handle that.

**Mario:** Like, jeez.

**Mario:** Anyway.

**Mario:** Great.

**Mario:** Thank you.

**Mario:** I have to jump, but thank you for the update.

**Mario:** I'll let Tanmay stay.

**Carrie Chowske:** Okay, thank you.

**Carrie Chowske:** Okay, thanks, Mario.

**Carrie Chowske:** And then from Scrunch, just looking at this, too, we saw a little more growth in citations and position again this week, which is nice.

**Carrie Chowske:** You've got a very strong competitive presence when looking at it.

**Tanmay Sarkar:** Yeah, I was also checking Scrunch the other day.

**Carrie Chowske:** Did you check the prompts that we're using?

**Tanmay Sarkar:** Yeah, I see.

**Tanmay Sarkar:** Yeah.

**Carrie Chowske:** Okay, cool.

**Carrie Chowske:** Well, then I won't go deep into that one for you.

**Carrie Chowske:** I think it's pretty steady from last week — about the same.

**Tanmay Sarkar:** Yeah, so as per some research, the AI has dropped, like these AI platforms have dropped citations share in last two months.

**Tanmay Sarkar:** So people have seen a decline in terms of direct traffic from these AI platforms.

**Tanmay Sarkar:** But in terms of visibility, those are still there — it's about whether they're still mentioning your brand. My take is you really can't generate demand and traffic anymore for top-of-funnel content because those questions are easily answered by AI — whether that's AI overviews or ChatGPT.

**Tanmay Sarkar:** So people won't come to your website to consume those content anymore because they're getting those answers there.

**Tanmay Sarkar:** So we need to produce more middle of the funnel and bottom of the funnel.

**Tanmay Sarkar:** Where they can take some actions or there will be some insights or metrics, something like those kind of content.

**Tanmay Sarkar:** Basically, not top of the funnel content with some definition and all.

**Carrie Chowske:** can get it to there.

**Carrie Chowske:** And hopefully that's where we're going with some of the topics that I sent.

**Carrie Chowske:** We're trying to go more with things that are specific to industries or related specifically to how Airbyte functions, that stuff.

**Carrie Chowske:** In terms of the direct traffic, this chart here, the referrer's breakdown, that is direct traffic to your site because that's pulling from GA4.

**Tanmay Sarkar:** Correct.

**Tanmay Sarkar:** You can see in the last two weeks, there is a decline, right?

**Carrie Chowske:** Yep.

**Tanmay Sarkar:** So there has been a change, but some companies are seeing some different things.

**Tanmay Sarkar:** But overall, research shows there's been a massive citations drop across the board.

**Tanmay Sarkar:** We have also created our Wikipedia page.

**Tanmay Sarkar:** It's live.

**Tanmay Sarkar:** It's not yet indexed in Google, but it will take time to show up in search.

**Tanmay Sarkar:** So, we recently created it last week.

**Tanmay Sarkar:** So, yeah, probably we'll see some good things where AI is pulling data from Wikipedia on AirBite and also whatever peer we do like from, let's say, TechCrunch, peer news error, later.

**Tanmay Sarkar:** However, we can easily link those to Wikipedia, because whatever we write on the AirBite page, that needs to be cited from a third-party, reliable source.

**Tanmay Sarkar:** So, yeah.

**Jakub Rudnik:** I saw the agenda item for the experimentation.

**Jakub Rudnik:** I just didn't push that off another week.

**Jakub Rudnik:** I didn't realize we had Monday off, and then two of my team members were out.

**Jakub Rudnik:** The deep work got pushed to Monday and Tuesday.

**Jakub Rudnik:** So just bear with me.

**Jakub Rudnik:** Thanks for the patience on that one.

**Tanmay Sarkar:** And is there a deadline when you guys are like opening Atlas for all the clients?

**Jakub Rudnik:** No, it's kind of the same answer — it's in the future.

**Jakub Rudnik:** Generally speaking, I think you all would be right up at the front of that line, given our relationship with you all and, you know, SOW and all that.

**Jakub Rudnik:** But that's been one that I've not heard an update, like, company-wide, even internally.

**Jakub Rudnik:** But the general sense is, like, it's just being, there are other priorities at the moment on where the product is going and the improvements.

**Jakub Rudnik:** They've been more on, like, pipeline improvements and other work streams.

**Jakub Rudnik:** So I'll keep you in the loop and I'll poke around and see if I can learn anything by next week.

**Jakub Rudnik:** But that was, generally speaking, like, a couple quarters out was my impression.

**Jakub Rudnik:** It's been deprioritized internally.

**Carrie Chowske:** Definitely keep throwing airbite in whenever they're asking for test cases.

**Carrie Chowske:** Because we're learning, we can learn so much from things we're doing either for your content or from you sharing data so they can run the analytics tool.

**Carrie Chowske:** So I keep mentioning like, hey, Airbyte really wants access.

**Carrie Chowske:** So they're going to get sick of me, but I keep bringing it up.

**Tanmay Sarkar:** Yeah, because we are planning to create a ghost website.

**Tanmay Sarkar:** I'm not sure, Jakub, if you have heard about this concept.

**Tanmay Sarkar:** So you can see this.

**Tanmay Sarkar:** I shared a link.

**Tanmay Sarkar:** One of our competitors has created something like this.

**Tanmay Sarkar:** Like how you can send signals to AI from different domains.

**Tanmay Sarkar:** Okay.

**Tanmay Sarkar:** And it doesn't always matter that that domain has to be very high authority because I have seen AI tend to cite a domain which is very new and has a domain authority of 8, 9.

**Tanmay Sarkar:** Right.

**Tanmay Sarkar:** If we're building a ghost website like this, I don't want to take so much of our manually written or optimized editorial content and reuse it because that would take too much time.

**Tanmay Sarkar:** Only way to scale those websites is by a programmatic approach.

**Tanmay Sarkar:** So a tools like, let's say, how AirOps does all these things.

**Tanmay Sarkar:** If we can get access to a tool platform like this, we can automate everything towards that ghost website.

**Jakub Rudnik:** Yep.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** Can you send me the example from the competitor? I don't see it in Slack or here.

**Tanmay Sarkar:** No, no, not Slack in this chat.

**Jakub Rudnik:** Oh, I wonder if you sent it to the, uh, one of the note takers.

**Jakub Rudnik:** I often do that.

**Jakub Rudnik:** Okay.

**Jakub Rudnik:** This is great.

**Jakub Rudnik:** This is one of those things that might get delayed with other experimental work. I think we have a couple of clients that either wanted to do this or tried it.

**Jakub Rudnik:** So I'll have to go back to the team.

**Jakub Rudnik:** But we've been looking for examples of this.

**Jakub Rudnik:** We understand the concept — it's a big lift.

**Jakub Rudnik:** And I think that's why we don't often push it.

**Jakub Rudnik:** But if it can be done, it seems to have an impact.

**Jakub Rudnik:** So we'll take a look.

**Jakub Rudnik:** And I would want to use this as a use case.

**Jakub Rudnik:** But understand what you're trying to do there.

**Jakub Rudnik:** And it would be more programmatic and automated.

**Jakub Rudnik:** Yeah, it's something we could consider with like all the work streams we're doing just.

**Jakub Rudnik:** But yeah, I understand that if we open it up, you would just be able to run that as well.

**Jakub Rudnik:** So I don't have an answer on like, how we would execute that immediately.

**Jakub Rudnik:** But I understand and can go back to the team with that.

**Jakub Rudnik:** I'll loop in Kyle on this too.

**Tanmay Sarkar:** I'm evaluating workflow automation tools like N8N and GAMLOOP where we can build a workflow to directly push content programmatically to the ghost website.

**Tanmay Sarkar:** I don't want to buy AirOps because it's expensive. I'll spend time on N8N and GAMLOOP to build a workflow for the ghost website to produce content in bulk for middle and bottom-of-funnel topics.

**Jakub Rudnik:** Okay.

**Jakub Rudnik:** I shared this with the team and sent it to Kyle so we can discuss how to best support this initiative.

**Tanmay Sarkar:** Cool, makes sense.

**Carrie Chowske:** My number one goal is to get that pipeline set up so we can start publishing those industry pages. I need to stay on the engineering team and make sure we get their questions answered.

**Tanmay Sarkar:** So I appreciate you getting that list so quickly.

**Tanmay Sarkar:** I'm also showing a first draft design of another programmatic page. Can you see the Figma design I shared?

**Tanmay Sarkar:** Or let me share my screen.

**Tanmay Sarkar:** Can you see?

**Jakub Rudnik:** Oh, got it, yeah, just a second to look.

**Tanmay Sarkar:** Yeah, so it's not yet like the top nav bar and footer and all those will change, but this will be a page for connectors.

**Tanmay Sarkar:** A different kind of pages.

**Carrie Chowske:** Okay.

**Carrie Chowske:** Well, once we get this first, like, pipeline set up, too, like, we can easily, because we hadn't updated the connectors pages yet anyway, so once we get that pipeline, it'll easily be able to, you know, like, transfer to doing this as our next round of updates.

**Tanmay Sarkar:** This can be handled by our team and pushed via our web developer. It's a connector display page that will interlink with industry pages and create a strong internal link structure across the site.

**Carrie Chowske:** Cool. I like it.

**Carrie Chowske:** All right.

**Carrie Chowske:** Do we have anything else that we want to go over?

**Tanmay Sarkar:** Do you have any questions?

**Carrie Chowske:** I'm good.

**Carrie Chowske:** Okay.

**Carrie Chowske:** All right.

**Carrie Chowske:** I think we're good on all the data sources now. I've also grabbed quotes from case studies so we can rotate through those.

**Carrie Chowske:** So that's all, that's all set to go.

**Carrie Chowske:** So hopefully it'll be, it'll be quick once we start, actually, once we have the pipeline, hopefully it'll start quickly.

**Tanmay Sarkar:** Yep.

**Carrie Chowske:** Yep.

**Carrie Chowske:** All right.

**Carrie Chowske:** Well, y have a nice weekend.

**Carrie Chowske:** I'll talk next week.

**Tanmay Sarkar:** Thanks, Dean.

**Tanmay Sarkar:** Thanks, y'all.

**Jakub Rudnik:** Bye-bye.
