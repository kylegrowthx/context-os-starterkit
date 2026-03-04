# Airbyte <> GrowthX - Weekly Sync

<metadata>
date: 2025-11-14
time: 16:30 UTC
duration: 21 minutes
organizer: carrie@growthx.ai
participants: Carrie Chowske (GrowthX), Kyle Gaudreau (GrowthX), Tanmay Sarkar (Airbyte), Mario Moscatiello (Airbyte)
fathom_recording_id: 101785750
fathom_url: https://fathom.video/calls/474502520
share_url: https://fathom.video/share/4wxzshDHZDLzeyLBasu664VK9ED_MPKU
source: fathom
enriched_on: 2026-03-02 16:45 UTC
</metadata>

---

## Summary

GrowthX and Airbyte reviewed content performance and SEO strategy, with Airbyte's traffic holding steady despite a market-wide 31% drop in ChatGPT citations. The team will add TLDRs to all new content and test a high-risk, high-reward "AEO Glossary" experiment using dedicated Q&A pages instead of FAQ sections. Airbyte will also ramp up production to 36 pages/week (30 industry pages) to finish their industry page project by end of year, freeing engineering time for new use cases.

---

## Context

Airbyte is a data integration platform that GrowthX has been working with on content strategy and SEO. This is their weekly sync call covering content production, performance metrics, and SEO experiments. Carrie (GrowthX) and Kyle (GrowthX) align with Tanmay and Mario (Airbyte) on content roadmap, LLM traffic trends, and AEO (Answer Engine Optimization) testing. The relationship is a delivery partnership where GrowthX manages Airbyte's content pipeline and tests new AEO strategies to drive visibility in LLM outputs.

---

## Relevance

**To GrowthX Delivery:**
- TLDR experiment proved to be low-risk SEO win (mixed results for LLM traffic) — now rolling out to all new content across Airbyte
- AEO Glossary test (dedicated Q&A pages vs. FAQs) is higher-risk experiment with scaling potential; Kyle is building overview and scoping this test
- Production ramping to 36 pages/week; 30 pages/week on industry pages project through EOY 2025 — requires team capacity planning

**To CheckThat:**
- Market-wide 31% drop in ChatGPT citations over 3 weeks signals algorithm changes designed to keep users on-platform, reducing outbound links
- Airbyte outperforming competitors despite broader trends (up 6% vs. market down 31%); validates CheckThat's visibility advantage
- AEO Glossary test will generate insights on LLM-friendly content formats and question patterns (Reddit-sourced) applicable to other clients

**To GrowthX Business Development:**
- Airbyte account health is strong: steady growth in target clusters, outperforming competitors on LLM visibility, actively investing in AEO experiments
- Partnership demonstrates successful delivery of complex, evolving SEO strategy with appetite for testing and iteration
- Potential reference value for B2B SaaS platform growth stories

---

## Overview

- **Content Pipeline Shift:** The editorial focus will broaden from Airbyte Flex to general topics. Production will ramp to \~36 pages/week (30 industry pages) to finish the industry page project by EOY.
- **LLM Traffic Volatility:** A recent 31% drop in ChatGPT citations is a market-wide trend, likely due to algorithm changes designed to keep users on-platform. Airbyte's performance is strong relative to competitors.
- **New SEO Test Proposed:** An "AEO Glossary" test will create dedicated Q\&A pages (not in-article FAQs) to capture LLM traffic. This is a higher-risk, higher-reward experiment than the TLDR test.
- **TLDR Test Outcome:** The TLDR experiment yielded mixed results for LLM traffic but is a low-risk SEO win. The team will add TLDRs to all new content and consider a bulk update for the "Data Engineering Resources" section.

---

## Key Topics

### LLM Traffic & Market Context

  - **Problem:** LLM referral traffic growth has slowed, a trend confirmed by both GA4 and Scrunch data.
  - **Context:** This is a market-wide phenomenon. Profound research shows a 31% drop in ChatGPT citations for brands over the last three weeks.
  - **Cause:** Algorithm changes are likely designed to keep users on-platform, reducing outbound links.
  - **Airbyte Performance:** Airbyte is outperforming competitors in LLM citations, according to Scrunch data.

### TLDR Experiment Results

  - **Goal:** Test the impact of adding a "TLDR" (Too Long; Didn't Read) summary at the top of articles.
  - **Outcome:** The test yielded mixed results for LLM traffic across platforms (GA4 data).
      - **ChatGPT:** Showed a positive session increase.
      - **Other LLMs:** Results were inconsistent, with some showing wins but no net session increase.
  - **Decision:** The team will add TLDRs to all new content.
      - **Rationale:** It's a low-risk practice that doesn't harm user experience and provides a small, consistent SEO benefit.
      - **Consideration:** A bulk update for the "Data Engineering Resources" section (1k–2k articles) was discussed.

### Proposed "AEO Glossary" Experiment

  - **Proposal:** Test a new AEO (Answer Engine Optimization) strategy using dedicated Q\&A pages.
  - **Methodology:**
      - **Research:** Scrape Reddit to identify primary questions and related sub-questions on a topic.
      - **Execution:** Create a simple, Q\&A-style glossary page focused on a single theme.
      - **Rationale:** This format is designed for easy LLM ingestion, unlike FAQs buried at the bottom of articles.
  - **Risk:** Potential for SEO cannibalization with existing articles.
      - **Mitigation:** Use `no-index` tags or `robots.txt` to restrict the pages to LLM-only visibility.

### Content Production & Pipeline

  - **Production:** The team is now working one week ahead on content.
  - **Editorial Focus:**
      - The final batch of Airbyte Flex/hybrid deployment pages will be published next week.
      - The focus will then shift to a broader mix of general data topics.
  - **Industry Pages Project:**
      - Production will ramp to 30 pages/week.
      - **Goal:** Complete the project by EOY 2025.
      - **Significance:** This frees up engineering time for "use case one" setup and creates a content buffer for its launch.
  - **Thumbnails:** Final tweaks are complete; files will be delivered today.

---

## Action Items

**Mario Moscatiello (Airbyte)**
- Reschedule weekly sync to avoid Kyle's school drop-off

**Kyle Gaudreau (GrowthX)**
- Send FAQ/glossary overview to Airbyte team; then scope/launch AEO test

**Carrie Chowske (GrowthX)**
- Add TLDRs to all Data Engineering Resources pages (1,000–2,000 articles)

**Tanmay Sarkar (Airbyte)**
- Review scrunch prompts; send updates to Carrie

---

## Transcript
**Carrie Chowske:** Hello, how are you?

**Tanmay Sarkar:** Hey Carrie, I'm doing good, how are you?

**Carrie Chowske:** Not too bad, not too bad.

**Carrie Chowske:** It's Friday, it's always good.

**Tanmay Sarkar:** Yeah.

**Tanmay Sarkar:** For the other project, you will also be working on that, or Eric will be the main?

**Carrie Chowske:** I think, yeah, I think during the sprint it'll be Eric, but I think then after that it'll get handed off to us for regular production.

**Carrie Chowske:** So, yeah, I'm trying to stay up to date on it so that I know what's going on.

**Carrie Chowske:** But, yeah, I helped him review some of the artifacts for the pipeline and stuff.

**Carrie Chowske:** So, it's my understanding that it is coming to us, yes.

**Tanmay Sarkar:** Yeah.

**Carrie Chowske:** Make it easier.

**Tanmay Sarkar:** Yeah, I saw the artifacts and I have left some comments too, yeah.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Just specifically for you, I will have next week's content ready for you.

**Tanmay Sarkar:** Thanks, I'm working on it. I was working on it just now.

**Carrie Chowske:** And it's the last group of those.

**Carrie Chowske:** There might be a couple things in there with the hybrid architecture that were already in production before you sent me that other list.

**Carrie Chowske:** So those will be the last ones of that.

**Tanmay Sarkar:** And then next week, we're starting with some of the other content.

**Carrie Chowske:** I think we're waiting on, I don't think Jacob is coming, but I think we are waiting on Kyle, but we can get started if you want.

**Tanmay Sarkar:** Yeah, yeah.

**Tanmay Sarkar:** You can get started.

**Tanmay Sarkar:** Yeah.

**Carrie Chowske:** We usually do the bulk of the talking anyway.

**Carrie Chowske:** So yeah, for this week, we've got everything for this week.

**Mario:** I told Kyle and Jacob, I was like, why are you guys even showing up?

**Mario:** Carrie's amazing.

**Mario:** Aw, thank you.

**Carrie Chowske:** I try.

**Carrie Chowske:** Jacob's my backup just because early on, he had a lot of hand in the stuff that we were doing. I'm just saying you're amazing.

**Mario:** Thank you.

**Mario:** Thank you.

**Mario:** I'm friends with Kyle, so I can say that.

**Mario:** Yeah.

**Carrie Chowske:** Yeah, yeah, yeah.

**Carrie Chowske:** He was really excited to work with you again when you joined.

**Mario:** Kyle, I was telling Carrie that you're amazing and you can do it.

**Kyle Gaudreau:** Oh, I appreciate that.

**Mario:** Carrie is amazing.

**Mario:** That is great.

**Carrie Chowske:** Yeah, she's great.

**Kyle Gaudreau:** thank you.

**Kyle Gaudreau:** It's always an adventure this time for me, my son.

**Mario:** No, we'll move the call.

**Mario:** Tanmay, we need to find a better time for this call because Kyle has school drop-off around this time, so we'll figure a better time.

**Carrie Chowske:** Yeah, yeah.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Not a problem for me.

**Carrie Chowske:** Yeah, so the only thing we got started on, Tanmay, I was telling Tanmay that I had content for him to review and that we're working out a full week ahead, which is great.

**Carrie Chowske:** And then next week, we'll publish our last group of the...

**Carrie Chowske:** The pages for the editorial stuff for the hybrid deployments.

**Carrie Chowske:** And then we'll change in a slight little, like, I don't even say it's a right turn.

**Carrie Chowske:** We're just kind of going back towards center where it's not all Airbyte Flex related topics.

**Carrie Chowske:** So we'll have a little more variety in there again.

**Carrie Chowske:** And then at that point, we'll be doing probably roughly 36 pages per week for the next few weeks.

**Carrie Chowske:** And 30 of those will be the industry pages until we get those wrapped up.

**Carrie Chowske:** Right now, it's looking like we'll finish those before the end of the year.

**Carrie Chowske:** We're able to do quite a few at a time.

**Carrie Chowske:** And we might even be able to ramp that up a little bit more.

**Carrie Chowske:** And that'll give us, that'll be good because it'll give our engineering time to get the use case one set up.

**Carrie Chowske:** And then we should be able to start with that right away.

**Carrie Chowske:** So, yeah, that got me through all this stuff.

**Carrie Chowske:** Wow.

**Carrie Chowske:** Okay.

**Carrie Chowske:** Oh, and they're working on the final tweaks to the thumbnails that we discussed yesterday, Tame.

**Carrie Chowske:** So I should have that today.

**Carrie Chowske:** So you should be able to get them.

**Carrie Chowske:** And then that should be pretty much just business as usual going forward here on the industry pages.

**Tanmay Sarkar:** Yeah.

**Carrie Chowske:** Okay.

**Carrie Chowske:** Makes sense.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** And then performance-wise, I pulled just like last couple months to kind of give us a quick little, just a few little snapshots since we just went over a lot of this last week.

**Carrie Chowske:** But we're still showing steady growth overall for the last couple of months.

**Carrie Chowske:** And particularly in the clusters that we've been focusing in are showing the most growth, which is really solid.

**Carrie Chowske:** We want to see that.

**Carrie Chowske:** And then we should see more come back into this data integration and data pipeline, since that's a lot of the topics that we'll be pushing forward with in the coming weeks.

**Carrie Chowske:** For GEO, we're still seeing really steady growth with LLM referrals, although it seemed to slow down.

**Carrie Chowske:** I know, Kyle, we talked about like the volatility with the scrunch data, but I'm also seeing similar, a slightly similar.

**Carrie Chowske:** Pattern with what we're seeing from GA4 also, where we're still seeing growth, but it's slowed a little.

**Kyle Gaudreau:** I feel like this is a good case to, one, the scrunch data has definitely been wonky recently.

**Kyle Gaudreau:** It's been a little bit hard to trust that I've just seen in the same day, wildly different numbers, and just the past week and a half has been strange, but this is definitely a bit more extreme in the trends.

**Kyle Gaudreau:** Probably a place, Carrie, where we could test that FAQ idea, and I know you're not as much in the loop on that, but we're running an experiment across a variety of accounts that's like a play on like FAQ slash glossaries that we have high conviction on.

**Kyle Gaudreau:** So I think maybe some structured GEO focus tests for a bit would be interesting to see if we can reverse that trend.

**Mario:** Yeah, that'd be great.

**Mario:** And Tamme, two questions for Tamme, maybe.

**Mario:** Like, first, do you see anything different in Profound? And B, you were talking about GPT 5.1 reducing citations. I think it's going to be bumpy for a while.

**Tanmay Sarkar:** Totally.

**Tanmay Sarkar:** Yeah, so I mentioned this last week to Jakub also.

**Tanmay Sarkar:** So as per like recent profound research, they have seen chat GPT citations for brands are down by 31% in the last three weeks.

**Tanmay Sarkar:** It's like declining.

**Tanmay Sarkar:** So they changed their algorithms, how they show up brands.

**Tanmay Sarkar:** So maybe in next algorithm, they tend to again show up more and it will again bounce back.

**Kyle Gaudreau:** So it's just like how Google algorithm used to work.

**Kyle Gaudreau:** Sometimes when an algorithm comes, your traffic crashes.

**Kyle Gaudreau:** Yeah.

**Tanmay Sarkar:** Something like that.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Yeah, I'll say though, like this trend, quite a bit more extreme than we've seen.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** So.

**Tanmay Sarkar:** Um, anyways, uh, yeah, but we can, like, yeah, like what this platforms are trying basically not to like, once they show a brand, they know that you'll go to the brand website by doing Google search or just typing in the URL.

**Tanmay Sarkar:** So they are trying to make them stay and read inside them.

**Kyle Gaudreau:** So, yeah.

**Tanmay Sarkar:** Yeah.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Makes sense.

**Carrie Chowske:** It kind of, that's a good lead into what I was going to say about the experiment that Jacob was running with the TLDR at the top of the page.

**Carrie Chowske:** Um, if we're looking at, you know, SEO, like there's, it's clearly helping with SEO, ironically, not helping, uh, not seeing as much of the same, um, pattern with GEO.

**Carrie Chowske:** So for the LLMs, like, it's kind of a mixed bag of, I kind of went in and looked at, um, and there's another, there's another page in the Looker dashboard.

**Carrie Chowske:** Specific LLM traffic for the test, and it's really kind of mixed. What I've done here is highlighted in green which one was the clear winner of the two groups for that particular LLM, and then the yellow is where it's the winner, but it's not a positive increase — it's not an increase in sessions.

**Carrie Chowske:** And this is based on session data.

**Carrie Chowske:** So it's coming from GA4.

**Carrie Chowske:** And like you can see here, it's just like, depending on the platform, you know, it's, it's, yeah, anyway, we're seeing like, that, surprisingly, you're doing pretty well on ChatGPT across, you know, this.

**Carrie Chowske:** And even, even when we're looking at this data up here, same thing, like, if everyone else is seeing it go down like 30%, and you're just going up six, I'm happy with that.

**Tanmay Sarkar:** Yeah, in ChatGPT, we are way ahead from our main company.

**Carrie Chowske:** And that's kind of what I really think is good, too, when we look at the scrunch data.

**Carrie Chowske:** If we can rely on it at all, it is showing that you're getting quite a bit more traction across the board through, you know, LLM citations, presence, all of those factors.

**Carrie Chowske:** So even if it's way off, it's still saying that you're doing better than the others.

**Carrie Chowske:** I don't know.

**Carrie Chowske:** It be blowing smoke at you.

**Carrie Chowske:** I don't know.

**Carrie Chowske:** But that's what I'm seeing.

**Carrie Chowske:** don't know, Kyle, if you have any thoughts.

**Kyle Gaudreau:** No, no, nothing to add to that.

**Tanmay Sarkar:** Yeah, I think we're doing a small experiment with a block at the beginning of statistical articles to show how the results appear in Google AI search or Google AI overviews — like a snippet we're adding to listicle articles.

**Tanmay Sarkar:** So that's a test we are doing, experiment.

**Carrie Chowske:** And we have seen pretty good traction so far from that.

**Carrie Chowske:** So we are adding it to more and more pages.

**Carrie Chowske:** Okay.

**Carrie Chowske:** I think, because it just kind of leaves the question, I mean, we'll finish out, obviously, tracking through SEO testing for this experiment.

**Carrie Chowske:** I'm kind of, at the moment, I'm kind of of the mind of it's making, it's not going to hurt to have it in there.

**Carrie Chowske:** Just kind of, I think, comes down to one of the things that I've noticed with content, and this is my personal opinion.

**Carrie Chowske:** I obviously, and this is anecdotal entirely, but like if we're trying to long-term say still write for the person and then for the algorithm, one of the things that happens a lot of times when you see, like we've got a lot of things at the top of the page, a table of contents, a TLDR, all that, it takes the person a while to get to the actual content.

**Carrie Chowske:** So it kind of just depends on what the goal is with what we're creating.

**Mario:** Yeah, I think we should never sacrifice too much, at least on user experience, because it's good to have more traffic and so on and so forth.

**Mario:** But I also think we should start looking at session data and see, okay, we're running this experiment.

**Mario:** Is the bounce rate going up?

**Mario:** Is the session time decreasing?

**Mario:** so on and so forth.

**Mario:** Because those will eventually hurt us.

**Mario:** Because at the end of the day, we want the people to, yeah, of course, a lot of this is top of the funnel content.

**Mario:** But we want people to come in and find value into what we're saying and hopefully keep browsing the website and finding something relevant to them and hopefully drive a conversion.

**Mario:** And so to me, it's always like, yeah, striking a balance in between experience and optimization in a sense.

**Kyle Gaudreau:** Yeah, we're very aligned with that.

**Kyle Gaudreau:** Like, that's generally how we think about it.

**Kyle Gaudreau:** You know, I would say TLDR is like pretty low risk from that perspective, like it.

**Kyle Gaudreau:** It can just be helpful for a person, right?

**Kyle Gaudreau:** Whether it really moves the needle, think it's like a small, like, around the edges type of thing that, like, doesn't hurt, but it's not going to all of a sudden, like, you know, massively increase, you know, AI visibility.

**Kyle Gaudreau:** But, yeah, generally, I think, like, that seems to be kind of what it's showing.

**Kyle Gaudreau:** Like, it's a little bit up and down, like a bit of a mixed bag.

**Kyle Gaudreau:** It clearly doesn't hurt.

**Kyle Gaudreau:** It doesn't massively help.

**Kyle Gaudreau:** So it's probably a good practice to include, I'd say, more often than not, but generally think about, like, with most of our customers, like, what are types of articles that just suits better versus others?

**Mario:** And sometimes that's clearer for some customers than others.

**Mario:** Maybe we do something with that here.

**Kyle Gaudreau:** Great.

**Kyle Gaudreau:** Yeah.

**Carrie Chowske:** Yeah.

**Kyle Gaudreau:** Carrie, I realized I wasn't sure if you were in the loop on the FAQ thing, but clearly you are. I think this is something good to test with the Airbyte team.

**Kyle Gaudreau:** I can do a brief overview on it to socialize it later.

**Carrie Chowske:** Yeah, we've been doing kind of like similar to what we were doing with Engine.

**Carrie Chowske:** I think we've been doing FAQs at the bottom of our individual articles, but I don't think we've done anything more comprehensive than that.

**Kyle Gaudreau:** Yeah, this is a little bit different.

**Carrie Chowske:** So I think it's like one of those things that, you know, in the next month, I would say like it would be worthwhile to test.

**Kyle Gaudreau:** Oh, it cut out like right as you were speaking, Tanmay.

**Tanmay Sarkar:** Oh, I think my internet is like has something to do.

**Tanmay Sarkar:** In a little bit.

**Tanmay Sarkar:** Oh, so I was telling you, we already have FAQ on some pages, mostly all article pages, and we have added FAQ schema also on those articles.

**Tanmay Sarkar:** Yes.

**Tanmay Sarkar:** Yes.

**Tanmay Sarkar:** Yes.

**Kyle Gaudreau:** This is a little bit different.

**Tanmay Sarkar:** Yeah, we can definitely try.

**Tanmay Sarkar:** I'm open to try any experiment because this is new and evolving.

**Tanmay Sarkar:** People are trying multiple things.

**Tanmay Sarkar:** They don't know which will work out and which not.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** I don't want to derail Carrie, can I do a quick, like, two-minute here on it?

**Carrie Chowske:** On the glossary?

**Carrie Chowske:** Yeah, yeah.

**Kyle Gaudreau:** Do you want to take it or want me to?

**Kyle Gaudreau:** Yeah, yeah, I'll just share it real quick.

**Kyle Gaudreau:** I'll keep it fast.

**Kyle Gaudreau:** We can scope this out further, but I'll just loop you guys in what we're doing with the engine team.

**Kyle Gaudreau:** So, first, we did a bit of Reddit research.

**Kyle Gaudreau:** just scraped different threads feeding into artifacts, trying to find, basically, like, primary questions and then related questions to that and trying to, like, pair those together.

**Kyle Gaudreau:** And so, like, in this case, like, construction companies that are booking hotels.

**Kyle Gaudreau:** Hotels for crews is like a common use case for them.

**Kyle Gaudreau:** And so then what are the associated questions to that?

**Kyle Gaudreau:** And then we have this comprehensive list of all these different questions.

**Mario:** So just try and identify where there's patterns of frequent.

**Kyle Gaudreau:** What we do is a really light test.

**Kyle Gaudreau:** It's kind of like a play on a glossary, but it's more of an FAQ style approach.

**Kyle Gaudreau:** And so basically it is centered around the primary question and then the associated questions.

**Kyle Gaudreau:** And it's supposed to be like really simple, like keep it short, LLMs are lazy.

**Kyle Gaudreau:** So we want to like, you know, play around these question and answer pairs around this common theme and see, does that help with visibility?

**Kyle Gaudreau:** We have no idea if it works, but our point of contact there who just joined from Ramp — formerly their head of something there — was also our customer before. They had done something similar at Ramp and found a lot of success. Small world.

**Tanmay Sarkar:** Congrats. It's so funny.

**Kyle Gaudreau:** Yeah, yeah.

**Kyle Gaudreau:** Yeah, totally.

**Kyle Gaudreau:** Anyways, it's like one of those things, if it works, it's the kind of thing we can scale out really fast.

**Kyle Gaudreau:** And, you know, we're going to be working on this navigational page that all this is on.

**Kyle Gaudreau:** so it's a little bit different than putting FAQs at the bottom of a page and more of a test of, like, this should be at least good enough for the average user if they actually, of course, read it and can rank in SEO.

**Carrie Chowske:** This is kind of like the traditional glossary page, which is designed for SEO — pulling those keywords that people search for and helping them find you that way.

**Carrie Chowske:** This is like the GEO version of that.

**Carrie Chowske:** And it's in the question and answer format.

**Carrie Chowske:** So that's why we're calling it a glossary.

**Carrie Chowske:** But it really looks more like an FAQ to the human eye.

**Carrie Chowske:** So it's less product-focused than a traditional FAQ, which is just a general question, hopefully to grab some of those.

**Carrie Chowske:** Because if that's the reason why FAQs work for an LLM, this should, in theory, work as well, and then not continue cluttering up.

**Kyle Gaudreau:** And part of it, too, is a lot of times FAQs are added at the bottom of articles.

**Kyle Gaudreau:** You know, these LLMs are trying to, you know, be as efficient as possible.

**Kyle Gaudreau:** This is a way of theoretically surfacing that content in a way that is easier for them to ingest.

**Kyle Gaudreau:** And so whether that holds true, we'll see.

**Kyle Gaudreau:** But that's the test that we're running across a couple of customers right now.

**Kyle Gaudreau:** So something we could do down the line with you all, but, you know.

**Tanmay Sarkar:** Yeah, I was thinking, let's say, we have a topic, like normal article, and at the end, whatever we have added.

**Tanmay Sarkar:** And if we add questions related...

**Tanmay Sarkar:** To that thing as a separate this FAQ that you showed, will there be a cannibalization issue?

**Kyle Gaudreau:** Yeah, potentially if you want to be certainly careful of like duplication in that sense, but cannibalization from like an AEO perspective, I think I'm worrying a little bit less about at this point, although I can see how that could be something to be concerned about.

**Kyle Gaudreau:** So from an SEO perspective, we're worrying about cannibalization, especially with like good FAQ coverage, can always like no-index those pages, put them in your LLMs, TXT, and then like even more restricted as like an AEO-focused test to see if it drives visibility.

**Kyle Gaudreau:** There's different like permutations of like how to think about leveraging it, so.

**Tanmay Sarkar:** You got it.

**Carrie Chowske:** I just have a couple more things in the agenda I wanted to make sure that we touched base on, so we'll go back to that for just one second.

**Carrie Chowske:** So then I guess we kind of got a little sidetracked with this, but do we want to start adding?

**Carrie Chowske:** You

**Carrie Chowske:** Are the TLDRs to more pages, or do we want to wait until we're completely done with the SEO testing portion to do that?

**Carrie Chowske:** I think we've got two weeks left on that test.

**Tanmay Sarkar:** No, I think we have already added TLDR to certain pages, and you want to add it to all the other pages, right?

**Carrie Chowske:** So it sounds like we all agree to start adding TLDRs to all new content. It's fairly easy to implement on any editorial or programmatic editorial content.

**Tanmay Sarkar:** Yeah, absolutely. We can push it to all the data engineering resources pages.

**Carrie Chowske:** In data engineering resources, we have more than 1,000–2,000 articles.

**Tanmay Sarkar:** Yeah, okay.

**Carrie Chowske:** And then did you look at the scrunch prompts like you were going to?

**Tanmay Sarkar:** No, I haven't checked it yet. I will check and let you know.

**Carrie Chowske:** Not a problem, that's it, that's all I had.

**Carrie Chowske:** Do we have anything else we needed to go over?

**Tanmay Sarkar:** I know you have another meeting with the Sprint team about the Airbyte context stuff, so I don't want to take up your time.

**Carrie Chowske:** No, I'm good from my end. Kyle, do you have anything else?

**Kyle Gaudreau:** Nothing useful.

**Carrie Chowske:** Well, it was nice chatting with you guys.

**Mario:** Thank you, team. We'll see you next week.

**Carrie Chowske:** See you next week.

**Tanmay Sarkar:** Have a good weekend.

**Kyle Gaudreau:** Bye.
