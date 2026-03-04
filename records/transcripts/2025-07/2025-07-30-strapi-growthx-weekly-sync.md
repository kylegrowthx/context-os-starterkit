# Strapi<>GrowthX Weekly Sync

<metadata>
date: 2025-07-30
time: 16:30 UTC
duration: 33 minutes
organizer: mara@growthx.ai
participants: Mara Leighton, Vivek Shankar, Oluwatimilehin Ademosu, Victor Coisne, Golzar Yaghoubpour, Paul Bratslavsky, Theodore Onyejiaku
fathom_recording_id: 77451339
fathom_url: https://fathom.video/calls/366636974
share_url: https://fathom.video/share/ozAo-pihmzgdPR1Gbo4Kx3nhyQgzafjD
source: fathom
enriched_on: 2026-03-03 20:18 UTC
</metadata>

---

## Summary

GrowthX and Strapi aligned on content production velocity, performance metrics, and optimization strategies for LLM discovery. Vivek reported steady traffic with 34% jump in "Talk to sales" conversions, while integration pages showed room for optimization. Victor confirmed Octave integration is ready to move forward — GrowthX will gain API access and platform access to begin integration work. The team prioritized three immediate needs: fixing code formatting issues in articles (backticks and syntax highlighters), generating image illustrations for new content, and increasing refresh velocity to maintain rankings as AI discovery becomes more critical.

---

## Context

Strapi is a headless CMS company and a strategic content marketing engagement for GrowthX. This is a weekly sync where the Strapi team (Victor Coisne, Golzar Yaghoubpour, Paul Bratslavsky, Theodore Onyejiaku) reviews content production status and performance with the GrowthX content team (Mara Leighton, Vivek Shankar, Oluwatimilehin Ademosu). Victor is currently traveling to Corsica and will be on vacation the following week. The meeting comes as GrowthX's content is shifting focus toward optimization for LLM discovery and citation, with existing content refreshes becoming a higher priority alongside new production. Strapi's engineering team is also preparing an integration with Octave, a platform they've been preparing content for.

---

## Relevance

- **To GrowthX Delivery:** Strapi engagement shows importance of addressing code formatting quality issues early (backticks, syntax highlighters) in markdown workflows to prevent rework by publishing teams. Image generation and design center partnership are emerging as standard content production requirements. Refresh prioritization strategy by traffic loss + outdated info is working; flow of running topics past product experts (Theo) one week ahead scales better than waiting for original authors.

- **To CheckThat / AI Visibility:** Integration pages underperforming in LLM traffic despite good HubSpot campaign results — suggests needed strategy shift from broad information architecture to semantic clustering of pain points + use cases + referral-worthy content. Scrunch tool access and detailed LLM query analysis is driving strategy (Mara to share Loom). Recency bias means refreshes directly improve LLM citation likelihood. Conversion event tracking shows 34% jump in "Talk to sales" CTAs, but attribution gap remains — may need custom GA4 events on GrowthX URLs to tie content to HubSpot pipeline.

- **To GrowthX Business Development:** Account stability signal — Victor investing in multi-week vacation planning, Strapi green-lighting Octave integration. Production velocity risk: team flagging content review bottlenecks in Airtable; Victor concerned refresh/comparison page/integration content streams are stalling. Headless CMS content showing volatility in performance — may indicate changing buyer research patterns.

---

## Overview

- 6 articles staged last week, 7 in progress this week; additional topics being added to queue
- Octave integration moving forward; Victor to provide API key and platform access
- Performance holding steady; slight dips in some areas, increases in conversion events
- Integration pages not receiving much LLM traffic; team to investigate optimization strategies
- Refreshes and image generation to be prioritized in upcoming content production

---

## Key Topics

### Content Production Update

  - 6 articles staged last week (one existing content, didn't need creation)
  - 7 articles in progress this week from approved list
  - Additional opportunities being added to Airtable queue
  - Two-week rolling basis for topic planning

### Octave Integration

  - Victor to provide API key and add GrowthX team to Octave platform
  - Engineering team starting to game out integration
  - Team to review Octave content to ensure alignment with artifacts

### Performance Report

  - Overall traffic steady; slight dip in referrer traffic
  - Non-branded impressions fell slightly in integration and use case clusters
  - Conversion events saw a jump: 34% increase in "Talk to sales" CTA
  - Headless CMS content showing volatility in performance
  - GSC data shows 48% average position drop to 10.2; investigating causes
  - LLM referrals declined slightly from previous high

### Integration Pages and LLM Traffic

  - Integration pages getting fair traffic in HubSpot campaign
  - Team to investigate optimizing integration pages for LLM discoverability
  - Strategies include focusing on referrals/mentions, combining pain points/use cases
  - Potential adjustments: formatting, chunking information, adding overview sections

### Content Feedback and Improvements

  - Theodore noted issues with code formatting (backticks, syntax highlighting)
  - Team to follow up on specific examples and potential workflow updates

### Visual Content Generation

  - Discussion on generating image illustrations for articles
  - Team to prioritize implementing this in the workflow
  - Possibility of leveraging GrowthX design center for specific image requests

### Content Refreshes

  - Prioritizing refreshes based on traffic loss and outdated information
  - Process involves running topics by Theo for approval
  - Victor emphasized importance of speed and not waiting for original authors

---

## Action Items

**Mara Leighton (GrowthX)**
- Create/share Loom video walkthrough of Scrunch insights — focus on LLM queries and problems that are performing well (shared timestamp 00:07:39)

- Analyze integration pages for LLM optimization; share specific formatting and structural suggestions with Strapi team (shared timestamp 00:13:55)

**Vivek Shankar (GrowthX)**
- Follow up with Theodore in Slack with specific code formatting issue examples from recent articles (backticks, syntax highlighters, HTML entity encoding) (shared timestamp 00:20:46)

- Start process of generating image illustrations for this week's articles; coordinate with GrowthX design center per Oluwatimilehin's note about capacity and waiting list (shared timestamp 00:21:35)

- Send Theodore the list of articles prioritized for refresh via Slack; ensure Airtable list visibility so Theodore can identify which ones are too technical for external refresh (shared timestamp 00:31:22)

**Victor Coisne (Strapi)** [pending confirmation]
- Provide Octave API key and add GrowthX team to Octave platform to begin integration work

---

## Transcript
**Mara Leighton:** Well, hopefully, Victor, you feel 100% the next time that we talk to you.

**Mara Leighton:** That is a week away.

**Mara Leighton:** So if it isn't the case, that's awful.

**Victor Coisne:** I'm going to be on vacation next week.

**Victor Coisne:** Oh, great.

**Victor Coisne:** Where are you headed?

**Victor Coisne:** I'm in Corsica at the moment.

**Victor Coisne:** So this week I'm working.

**Victor Coisne:** Next week I'll be off.

**Victor Coisne:** And the following week as well.

**Victor Coisne:** So I actually won't see you until the end of August.

**Victor Coisne:** Wow.

**Victor Coisne:** Okay, great.

**Victor Coisne:** I hope you enjoy your August.

**Victor Coisne:** That sounds lovely.

**Victor Coisne:** Yeah, I will.

**Mara Leighton:** I guess if I had to be sick, I don't know.

**Mara Leighton:** I might prefer to do it while I was already working.

**Mara Leighton:** And then you get to just enjoy your vacation time.

**Victor Coisne:** Timing is not great.

**Victor Coisne:** I have so many things to finish before heading to vacation.

**Victor Coisne:** But yeah, it is what it is.

**Victor Coisne:** Yeah.

**Vivek Shankar:** Hey, everybody.

**Vivek Shankar:** Hey, team.

**Victor Coisne:** Hi.

**Golzar Yaghoubpour:** Hello.

**Golzar Yaghoubpour:** I guess we can get started.

**Vivek Shankar:** I think we're just waiting on Theo.

**Vivek Shankar:** Yes.

**Victor Coisne:** It's okay.

**Victor Coisne:** Yeah, we can get started.

**Victor Coisne:** Cool.

**Victor Coisne:** We can back up if he has any particular questions.

**Vivek Shankar:** Yes.

**Vivek Shankar:** So, yeah, just a quick update on production, et cetera.

**Vivek Shankar:** We staged six articles last week.

**Vivek Shankar:** It was six because one of the articles was a, there was already existing strapi content on it, so it didn't need creation.

**Vivek Shankar:** We're working on seven articles this week from the approved list.

**Vivek Shankar:** Also, we, this is more of a placeholder, just as a reminder, we've identified additional opportunities, and every week, we'll just be adding it to the queue in Airtable.

**Vivek Shankar:** For now, we're good for topics for the next couple of weeks, so just slowly keep adding topics in there, and then, you know, we can just keep working on a two-week rolling basis.

**Vivek Shankar:** The Octave integration, I think we had decided to sort of cut over to this.

**Vivek Shankar:** Yes, regarding this at the end of last week.

**Vivek Shankar:** I was just wondering, is there any update there from Strapi's end?

**Mara Leighton:** Yeah, I can jump in there for a second, Vivek, and just give Victor a brief update. Victor, I don't believe you were on our sync last week.

**Mara Leighton:** I know we had chatted about waiting until Strapi had, like, finalized all of those documents or all the information within Octave.

**Mara Leighton:** I did sync with Mateo just, like, over Slack really quickly and put in a ticket for our engineering team to just start gaming out an integration.

**Mara Leighton:** I would imagine we'll just need, like, the API key.

**Mara Leighton:** But, anyway, that's what's happened on our end.

**Mara Leighton:** And then back to Vivek's question of, is everything finalized within Octave, or are you still kind of tapering?

**Victor Coisne:** No, it is.

**Victor Coisne:** I can either give you the API key right now.

**Victor Coisne:** Yeah.

**Victor Coisne:** Or I can add you to the platform.

**Mara Leighton:** Yeah, that would be, if you don't mind double-dipping a bit, adding us to the platform, we can get started looking around now and make sure that everything maps to our artifacts, just so that there isn't a lag, and then the API key would be great.

**Mara Leighton:** I'll give that to the engineering team, and they can work on the integration simultaneously.

**Mara Leighton:** What email should I use?

**Victor Coisne:** For probably team at — I'll drop it in the chat here, I'll give you our team account.

**Mara Leighton:** Okay, and Mara, I'm sending you the API key via DM.

**Victor Coisne:** Thank you.

**Victor Coisne:** Okay, and so let me know when you receive the email.

**Victor Coisne:** You could also receive the email at team at growthxlabs.

**Mara Leighton:** Perfect.

**Mara Leighton:** Okay, great.

**Mara Leighton:** Cool?

**Victor Coisne:** Cool.

**Mara Leighton:** I got the Slack message, and then I'll keep you posted on when I see the email come through for the team account.

**Mara Leighton:** Perfect.

**Victor Coisne:** Okay.

**Victor Coisne:** Just a reminder regarding the competitor comparison pages.

**Vivek Shankar:** We've listed five of them for your review. Timmy and I will follow up in Slack with that thread in case you missed it. But yeah, if you could just review that real quick, and then let us know what you think, we can make changes and get started on that patch quickly.

**Vivek Shankar:** So, regarding the performance report — we pretty much held the same level as last week, no major changes over there.

**Vivek Shankar:** Traffic from Google was pretty much at the same spot.

**Vivek Shankar:** It was traffic from the other referrers that fell a little bit, which explains the slight dip.

**Vivek Shankar:** Non-branded impressions also fell a bit last week.

**Vivek Shankar:** Not a major fall, but a slight fall within the integration and use case stage clusters.

**Vivek Shankar:** Conversion events, however, we saw a bit of a jump.

**Vivek Shankar:** Talk to sales, CTA, saw a 34% jump compared to a couple weeks ago.

**Vivek Shankar:** And the clicks on pricing dipped a little bit, but the clicks on contact sales jumped a little bit.

**Vivek Shankar:** In terms of cohorts, the headless CMS content is seeing some volatility — we're seeing good performance one week, then it dips the next.

**Vivek Shankar:** The GSC data I won't fully trust at this point because of the variations it shows — it seems a bit extreme. Still, it shows a 48% average position drop to 10.2, so it's not like a bad position to be in terms of averages. Still, a 48% drop warrants investigation. We're looking into which pages suffered this drop and why it happened. It could be seasonal, but given the size of the drop, it does merit some investigation.

**Vivek Shankar:** The integration pages didn't drop in positions, there was a slight click loss, so we're thinking this is seasonal at this point, we'll wait and see for another week if this persists, and then we'll jump into that.

**Vivek Shankar:** In terms of LLM referrals, we declined a little bit from a previous high — ChatGPT referrals fell and Gemini as well. This wasn't a major drop-off, just a slight decline from last week's high. Generally speaking, LLM referrals are a small percentage of overall traffic when we look at the sessions for the pages that GrowthX has created.

**Vivek Shankar:** One of the reasons is the integration pages are not receiving a lot of referrals from LLMs, but the blog pages are receiving a healthy number.

**Vivek Shankar:** We don't think this is a major issue in terms of the integration pages not receiving a lot of traffic from LLMs, but just pointing out in case you do a comparative analysis.

**Vivek Shankar:** So those are any questions I can answer about the performance side of things.

**Victor Coisne:** Yeah, I've got a couple of questions. Go ahead, Golzar.

**Golzar Yaghoubpour:** No, no, you go first, Victor.

**Victor Coisne:** Okay, yeah.

**Victor Coisne:** So for LLMs, I missed last week and I didn't get a chance to watch the recording.

**Victor Coisne:** Did we get access to Scrunch?

**Mara Leighton:** We do have yes, we do have Scrunch. We didn't walk through it last week.

**Mara Leighton:** What we've typically been doing is sharing...

**Mara Leighton:** What

**Mara Leighton:** Like reports and screenshots from Scrunch because the interface is still a little bit hard to use.

**Mara Leighton:** So I can give you direct access, or I can walk you through it, but I can also just share a Loom of the parts that we think are most important to pay attention to and the insights we would glean from it. Would that be most useful?

**Victor Coisne:** Yeah, I think that'd be useful. I mean, what I'm trying to understand is: what are the queries, what are the problems that are doing well?

**Victor Coisne:** Like, just one level down from what you just shared, Vivek, like, if traffic is declining, have we lost ranking on a specific query?

**Victor Coisne:** So we can try to see if we need to do something about it.

**Mara Leighton:** Sure thing. Yeah, absolutely. I'll share a Loom either today or first thing tomorrow.

**Victor Coisne:** Sounds good. And the second question — if you go back to the Notion for a second. I was wondering about the conversion events.

**Victor Coisne:** Are we able to tie this back in Looker to the increase to either a specific content, like piece of content that could perform better?

**Victor Coisne:** Or if overall traffic is down, the conversion event is up?

**Victor Coisne:** I'm just trying to understand what that means.

**Vivek Shankar:** Yeah, so the thing with conversion events the way GA4 reports it — this is for organic traffic throughout the website. The traffic we are reporting on this page and overall is basically for the URLs that GrowthX has created. So it's not exactly apples to apples. When I say traffic remains steady, I'm reporting only the GrowthX-created pages. If we're talking about the entire website, we can filter it and see it's kind of the same across the whole site. It's a limitation of GA4 — we're not able to figure out if a conversion came exactly from a GrowthX URL.

**Vivek Shankar:** Was it a direct visit to the page, et cetera?

**Vivek Shankar:** We don't know.

**Vivek Shankar:** All we can track is how often these events were fired, and are they increasing in lockstep with what we're producing?

**Victor Coisne:** Yeah, I mean, maybe at some point, like, it means that we need to create, like, growthx-specific GA events, you know, that maybe that's the way to narrow down, like, attribution.

**Victor Coisne:** We have some visibility through HubSpot, which we can share, like, you know, impact on revenue.

**Victor Coisne:** Yes.

**Victor Coisne:** Or, like, lower, like, bottom-of-the-funnel impact.

**Victor Coisne:** But anyway, that's fine.

**Victor Coisne:** a topic fun of the day.

**Vivek Shankar:** Yeah, yeah, if you can send us the HubSpot data, that'd be great.

**Vivek Shankar:** If that is not enough.

**Vivek Shankar:** Then I guess, yes, creating a custom event and placing it on our pages would be the best way.

**Mara Leighton:** Okay, so moving on.

**Vivek Shankar:** Yeah, just a reminder again for the comparison pages and if you could let us know about that.

**Vivek Shankar:** And yeah, we'll keep adding more topics for your review.

**Vivek Shankar:** And Timmy or I will ping Paul and Theo in the channel to get feedback on new topics.

**Victor Coisne:** So, Theo, like anything you need from us on the comparison pages?

**Victor Coisne:** Maybe you can give a quick status update on this.

**Theodore ONYEJIAKU:** Yeah, for the comparison pages, well, I actually haven't taken a look at it.

**Theodore ONYEJIAKU:** So, I definitely will check it out today or tomorrow.

**Theodore ONYEJIAKU:** Okay, that sounds good.

**Victor Coisne:** And so for the topics, I did check a little bit — I think there were only four topics for review.

**Vivek Shankar:** That was because Paul and Theo got through the list last week.

**Vivek Shankar:** So we're actually good for the next two weeks, but then, you know, I'll keep, we'll keep adding more topics to that list.

**Vivek Shankar:** And as they come up, once we get to seven or eight or so, I'll ping in the internal channel.

**Victor Coisne:** Okay, I also had a quick follow-up question.

**Paul BRATSLAVSKY:** I know the list that you presented, I also sent a list of topics that I thought might be good.

**Paul BRATSLAVSKY:** Is that helpful for you?

**Paul BRATSLAVSKY:** Is there any feedback on that?

**Paul BRATSLAVSKY:** Yeah, it's super helpful.

**Vivek Shankar:** We will add it in.

**Vivek Shankar:** We're just doing some SEO research on those topics.

**Vivek Shankar:** It's just to see if there are any keywords we can connect to it, or if there's any repetition with what we've already suggested.

**Vivek Shankar:** Once that's done, you will see that in there over the next couple of days.

**Paul BRATSLAVSKY:** Yeah, no worries. I just wanted to make sure that Theo and I are still able to contribute topics — not just letting you guys focus on finding topics, but we're also recommending stuff that makes sense for the business.

**Vivek Shankar:** Yeah, yeah, that was definitely helpful. So yeah, thank you. I appreciate you doing that.

**Mara Leighton:** Also, if you're ever hearing anything from sales that you think is interesting, feel free to just drop it in the channel and we'll figure out a way to integrate it into the content.

**Mara Leighton:** Perfect.

**Mara Leighton:** Sounds good.

**Golzar Yaghoubpour:** I had a question about the integration pages. So, in the HubSpot campaign, they're getting a fair amount of traffic. Obviously, in HubSpot, I can't see exactly where the traffic is coming from. I wanted to know from your perspective — how do we position the integration pages so they start showing up in LLM traffic? Is there a science behind it yet, or is it still the Wild West?

**Mara Leighton:** That's a great question.

**Mara Leighton:** And the answer is a little bit of both.

**Mara Leighton:** I would say probably primarily Wild West, but we're starting to glean hard and fast best practices.

**Mara Leighton:** And then the value, obviously, of monitoring the content will be being able to glean what maybe hasn't bubbled up into popular wisdom just yet, but seems like a relatively good play for us to take advantage of.

**Mara Leighton:** So to answer your first question, and then the second, we can take a deeper look and see if maybe there are, you know, some adjustments that we could make with formatting, you know, if we want to like play around with where we're, where we're chunking certain information, if there's a way to optimize there.

**Mara Leighton:** But typically it would be formatting — the topic itself shouldn't really change. When we think about positioning ourselves to show up in AI, we're really looking for referrals and mentions. Even more so than citations, because citations are more difficult to get.

**Mara Leighton:** Fewer AI sources are actually going to give citations and also referrals mean that someone actually lands on the site, which is really nice for us.

**Mara Leighton:** And typically the way we'd track those would be combining pain points or use cases — something a bit more actionable for your audience. Referrals mean someone actually lands on the site, which is really valuable for you. So the TLDR is we'll take a deeper look and see what we should be tweaking in the integration pages. Broadly, for the AI play right now — which is Wild West but with emerging best practices — we want to "flood the zone" with ownership of the topics you want to be associated with. It's really about semantics. When an AI crawls the internet trying to be unbiased, are we showing up in the places it prioritizes? Are we showing up in enough places to be the obvious answer? From what we're seeing in Scrunch, Strapi is very well positioned right now. But we'll continue to monitor and adjust. That might include adding an overview section at the top of the page that's easier for AI to crawl. Anyway, for the integration pages in particular, we can do a deeper dive and share specific suggestions.

**Golzar Yaghoubpour:** And no worries about the monologue. I think it would be interesting to test redoing the layout of that page.

**Golzar Yaghoubpour:** Because the main thing that we changed on that page was where the CTA is.

**Golzar Yaghoubpour:** In the last six months, that's been the major change.

**Golzar Yaghoubpour:** So if there's additional things we can be doing to be discoverable by AI, then that's, I look forward to the work implementing those.

**Golzar Yaghoubpour:** Yeah, certainly.

**Mara Leighton:** And also, as we're doing refreshes, that's a pretty, that's win-win scenario for us if we're updating the formatting.

**Mara Leighton:** Because that's obviously also a really important part of showing up with AI.

**Mara Leighton:** There is a recency bias.

**Mara Leighton:** So sometimes, like, if you look on the back end of, like, if you start with the natural language prompt and then it gets kind of siphoned down into something that looks more like a keyword search on the back end, most of those will add in, like, 2025 or something.

**Mara Leighton:** So refreshes will work very well for us.

**Mara Leighton:** But yeah, certainly that is a to-do item.

**Vivek Shankar:** All right.

**Vivek Shankar:** That was it.

**Vivek Shankar:** If there's any other questions we can answer.

**Vivek Shankar:** Awesome.

**Mara Leighton:** Yeah.

**Theodore ONYEJIAKU:** I just have a few comments on the recent articles I reviewed.

**Theodore ONYEJIAKU:** They were good.

**Theodore ONYEJIAKU:** Just that I would want us to kind of focus more on the comments I formats like applying the backticks where they should be.

**Theodore ONYEJIAKU:** When you find a code word and the language for the syntax highlighter.

**Theodore ONYEJIAKU:** So it will reduce more time on my own.

**Theodore ONYEJIAKU:** And so I could do other things.

**Theodore ONYEJIAKU:** Yeah.

**Theodore ONYEJIAKU:** But it's great.

**Theodore ONYEJIAKU:** Like the contents are very great.

**Theodore ONYEJIAKU:** Thank you.

**Theodore ONYEJIAKU:** I just want to ask about the backticks.

**Vivek Shankar:** I think we tend to lose those because we download the doc as markdown and then paste it into the CMS. I think during that process, when we paste it into Strapi, we lose some of those backticks.

**Vivek Shankar:** Are you seeing backticks consistently not being present across every single instance, or is it just in a few places here and there?

**Theodore ONYEJIAKU:** In the last article I reviewed, some code blocks had backticks and some didn't, so I had to add them myself. For the language highlighter, same issue — some code blocks have it, some don't. I also noticed the code is using HTML entity encoding instead of literal symbols. For example, instead of using `<` and `>` symbols, it uses the HTML entity codes. For React code that renders components, the `<` and `>` get encoded to HTML format. These are things I could overlook except they take too long to fix manually. I don't think I've seen this before — maybe you guys updated your content workflow?

**Theodore ONYEJIAKU:** Okay.

**Vivek Shankar:** We'll follow up in Slack with specific examples, and then we'll take it to our team to see if there's any workflow updates needed. Yeah, thank you for pointing that out. We'll look into that for sure.

**Victor Coisne:** Okay, go ahead.

**Victor Coisne:** Go ahead.

**Victor Coisne:** Okay.

**Victor Coisne:** Yeah.

**Victor Coisne:** Just two quick questions. We didn't mention visuals — there's been a topic for some time about generating image illustrations or assets based on the ones you provided. Is there an update on this? I haven't seen it in the latest articles. Is that something we're able to do now?

**Vivek Shankar:** We can generate inline images for sure.

**Vivek Shankar:** We're doing that for other clients as well.

**Vivek Shankar:** What we've done in the past is generate them manually first and run them past you for approval. Then, if the style and idea look good, we go ahead and automate it.

**Vivek Shankar:** During that manual process, we can't get your exact brand colors or whatever spot on, but the idea is just so that you review that, okay, this kind of image, this idea looks good, this sort of style of graphic looks good.

**Vivek Shankar:** We can certainly do that with, you know, this week's articles and the next, and then sort of run past you.

**Vivek Shankar:** If it's good, we can then automate that within our flows.

**Vivek Shankar:** Does that kind of sound like something you have in mind?

**Vivek Shankar:** Yeah.

**Victor Coisne:** I'm surprised this isn't automated already — we had a lot of back-and-forth on this, so I'm a bit surprised it's not part of the workflow yet, to be honest.

**Vivek Shankar:** We can certainly get it in there quickly. Yeah, we'll run this past you, get on it, and see how soon we can have it in place.

**Mara Leighton:** Also, Victor, was that something that preceded Vivek and I joining the team?

**Victor Coisne:** Yeah, it started way before, yeah.

**Victor Coisne:** Okay, well, that completely makes sense.

**Mara Leighton:** Thank you again for mentioning it so that we can get it integrated and start moving on it really quickly.

**Mara Leighton:** So apologies for that.

**Mara Leighton:** Also, it's possible that we're missing context, so we should check, Vivek, and just make sure that the engineering team isn't already working on that because it's possible that maybe that got lost in translation.

**Mara Leighton:** If it isn't, we'll mark it as high priority, and we'll start doing it from this week onward.

**Mara Leighton:** So sorry for the delay.

**Mara Leighton:** Thank you for mentioning it.

**Mara Leighton:** We'll make sure that from this point onward, we're working on it.

**Victor Coisne:** That sounds great.

**Victor Coisne:** Timmy, yeah.

**Victor Coisne:** Go ahead, Timmy.

**Oluwatimilehin Ademosu:** Okay, hi. So I wanted to ask if you could send a written memo in Slack listing some of the things going wrong in the code. When editing, I haven't touched any of the code, so I don't know if it's a parsing issue or something we need to investigate more closely. That way I can flag it to engineering to prevent future issues. And about the images — I was speaking to Panza, our chief content officer, and he said if we need specific kinds of images like inline headers, we can drop a request to the design center. They're hiring fast and helping us with these things, but there's a waiting list based on how many clients they're supporting. But yeah, that's something we could explore.

**Mara Leighton:** Well, lovely. I know we're pretty much at time.

**Victor Coisne:** Yeah, there's one last topic. So refreshes — we all know refreshes are a big part of ranking in LLMs. Can somebody refresh my memory on the latest strategy for prioritizing refreshes? Obviously we're looking at the ones that used to get a bunch of traffic but don't anymore. What I'd like to see — and this is a bit missing from the agenda — is looking at different work streams separately so we can understand where we're at. There's the blog, the integrations, comparison pages, and refreshes. If we categorize the different work streams, we can better understand and make sure we keep on track for all of them.

**Vivek Shankar:** Yeah, definitely. I can give you an update on the refreshes.

**Vivek Shankar:** We have been prioritizing them over the past couple of weeks.

**Vivek Shankar:** This week, we have only new content, but from next week onwards, we will have refreshes in there as well.

**Vivek Shankar:** We have a pretty good flow sorted out.

**Vivek Shankar:** We prioritize refresh topics based on traffic loss, outdated information, versioning problems, and similar issues. We run the topics past Theo the week before to determine if it needs a full refresh or if he should handle it internally — some were written by specific people and need deep product knowledge. Once that's decided, we create the refreshes the following week. That's what we've been doing for the past couple of weeks now.

**Vivek Shankar:** And yeah, so we do.

**Vivek Shankar:** We'll just keep continuing to do that, for sure.

**Victor Coisne:** Okay, that makes sense. Theo, a lot of the feedback on the Strapi side lands on you, and I know you have a lot going on separately. I want to make sure you feel supported and comfortable. If we need to jump in and review articles in Airtable to approve them, we can do that. I want to make sure we don't get stuck because a lot of our success with GrowthX depends on volume, speed, and velocity getting content out and refreshed. It feels like sometimes we're stalling. Theo, if you need help or feel like you're running behind, just let us know.

**Theodore ONYEJIAKU:** Yeah, sure. I think this week I sent a couple of topics that are still being worked on.

**Theodore ONYEJIAKU:** And I'm hoping it will be ready as soon as possible so I could publish them.

**Theodore ONYEJIAKU:** The team also shared a couple of topics that Paul and I checked and gave feedback on. Right now, I'm waiting on the comparison pages and new articles to review and publish, and hoping the feedback I gave gets incorporated. If I need help, I'll let you and the team know. For refreshes, the one I was asked about was very technical — it didn't need a full rewrite, just an internal update. The one we were presented was different new content on the same topic. So I thought we could either update it internally or ask the original author to do the refresh.

**Victor Coisne:** I think the issue is if we wait for the author to get back, we waste another couple weeks per article. That doesn't scale. I really think we should move away from asking authors to do updates and owning the refresh. Yeah, we might not do as good a job as the original author, but I think speed and freshness matter more than waiting for them. It just won't scale, and it'll slow us down.

**Theodore ONYEJIAKU:** Yeah, I'll add that feedback. Yeah.

**Victor Coisne:** So maybe a note for the team — reviewing Airtable together might help. Just screen sharing and checking that none of the work streams have a ton of items stuck in review. That might speed things up strategically.

**Mara Leighton:** We can also include a note in our weekly memos flagging any bottlenecks we notice, so we're helping you see them as well.

**Victor Coisne:** That sounds good.

**Victor Coisne:** Great.

**Victor Coisne:** All right.

**Victor Coisne:** Well,

**Mara Leighton:** Oh, sorry.

**Mara Leighton:** Go ahead.

**Theodore ONYEJIAKU:** I would love us to have a list of the articles we want for refresh.

**Theodore ONYEJIAKU:** Like I mentioned, for very technical articles, we don't need to rewrite them completely because the one we saw was rewritten and lost the technical depth. So if it's a technical refresh, you could ping me or create a list on Airtable so I know which ones I'm updating myself.

**Vivek Shankar:** Yeah, we do have that list on Airtable. I'll send it to you in Slack so you can take a look at it.

**Theodore ONYEJIAKU:** Awesome.

**Vivek Shankar:** Well, thanks so much, everyone, for your time.

**Mara Leighton:** Really appreciate it.

**Mara Leighton:** If anything else pops up, you know where to find us.

**Mara Leighton:** Happy to sync whenever.

**Mara Leighton:** Victor, hope you feel better and enjoy your vacation next week.

**Mara Leighton:** We have a couple of action items to get back to you on, so we'll follow up shortly.

**Victor Coisne:** Great. All right, well —

**Mara Leighton:** Oh, sorry. Go ahead.

**Vivek Shankar:** Well, thanks so much, everyone, for your time. Really appreciate it. If anything else comes up, you know where to find us. Happy to sync whenever. Victor, hope you feel better and enjoy your vacation next week. We have a couple of action items to get back to you on, so we'll follow up shortly.

**Victor Coisne:** Great. Appreciate it.

**Mara Leighton:** Thanks, everyone.

**Paul BRATSLAVSKY:** Thank you. Bye.

**Paul BRATSLAVSKY:** Thank you.

**Paul BRATSLAVSKY:** Bye.

**Paul BRATSLAVSKY:** Thank you.
