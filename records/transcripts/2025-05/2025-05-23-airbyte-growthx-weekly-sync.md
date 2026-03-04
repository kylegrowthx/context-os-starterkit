# Airbyte <> GrowthX Weekly Sync

<metadata>
date: 2025-05-23
time: 18:59 UTC
duration: 20 minutes
organizer: nicolas@growthx.ai
participants: Jakub Rudnik (GrowthX), Nicolas Fernandez (GrowthX), Tanmay Sarkar (Airbyte), Mario Moscatiello (Airbyte)
fathom_recording_id: 64503119
fathom_url: https://fathom.video/calls/307603830
share_url: https://fathom.video/share/ps1MH38D87KQB-5oEo-RUGFzHHuECzPX
source: fathom
enriched_on: 2026-03-04 15:42 UTC
</metadata>

---

## Summary

Airbyte and GrowthX discussed content production progress, reporting improvements, and team transitions. GrowthX is delivering content 25% above typical volume with strong refresh coverage, and rolling out a new analytics dashboard by Tuesday that will include LLM traffic data and Profound AI visibility metrics. Nicolas Fernandez is departing, and GrowthX is onboarding new content managers to maintain quality on Airbyte's technical content, while the team shifted their weekly sync to Friday mornings to better accommodate schedules.

---

## Context

Airbyte is a data integration platform company that is a content client of GrowthX. They contracted GrowthX to manage their content strategy and production, focusing on technical content, refreshes, and SEO optimization. This is a core engagement between two service teams — Airbyte's content and data teams (including Mario, Tanmay, and others) work with GrowthX's content delivery team (Jakub, Nicolas, and supporting content managers) on a weekly cadence to review progress, align on strategy, and handle operational issues. The relationship involves tight collaboration around publishing workflows, analytics, and content recommendations.

---

## Relevance

**To GrowthX Delivery:**
- New publishing workflow automation needed for Webflow (multiple simultaneous logins causing session issues)
- Onboarding new content managers to replace departing Nicolas Fernandez; need to maintain quality on technical client work
- Implementing structured schema (FAQ, speakable, product) in article generation prompts to improve AI platform visibility
- Dashboard reporting expanding to include LLM traffic separation and week-over-week/month-over-month analysis

**To CheckThat:**
- Airbyte is using Profound AI visibility tool and seeing value in schema-based content; CheckThat can learn from schema implementation patterns
- LLM traffic attribution becoming central to Airbyte's measurement strategy alongside traditional GA4 conversion data
- AI visibility (impressions vs. clicks) emerging as key metric Airbyte wants to track and optimize for

**To GrowthX Business Development:**
- Airbyte is expanding reporting requirements and tool integrations (Profound, GA4, Webflow automation) — indicates growing sophistication and commitment to content ROI measurement
- Content volume 25% above baseline and sustained refresh pipeline suggests healthy engagement and utilization

---

## Overview

- Content volume and refresh efforts on track, exceeding typical output by 25%; publishing occasionally blocked by Webflow login issues when multiple users active
- New reporting dashboard launching Tuesday with LLM traffic data, content type separation (new vs. refresh), and week-over-week/month-over-month comparisons
- Airbyte integrating Profound AI visibility tool and implementing structured schema (FAQ, speakable, product) to improve AI platform visibility
- Nicolas Fernandez departing; experienced content managers from other GrowthX accounts supplementing new CM onboarding
- Weekly meeting moved to Friday mornings at 9 AM PT (6 PM Friday PT for David in Europe) to improve team availability and workflow
- Tanmay to complete article reviews by Monday to give two days for GrowthX publishing before Wednesday meetings

---

## Key Topics

### Content Production and Publishing

  - Currently above typical output by \~25%, including refreshes
  - Publishing occasionally faces Webflow login issues when multiple users active
  - Exploring automation options to streamline publishing process
  - New topics and refresh content pipeline set for next 30 days

### Reporting and Analytics

  - New dashboard coming Tuesday, will include:
      - LLM traffic data
      - Separation of new vs. refreshed content
      - Week-over-week and month-over-month comparisons
  - Integrating Profound AI visibility tool data
      - Adding schema (FAQ, speakable, product) to improve AI platform visibility
      - Jakub to be added to Profound for direct access

### Team Changes and Workflow

  - Nico's last day; new Content Managers (CMs) being onboarded
  - Experienced CMs may supplement during transition
  - Tanmay to complete article reviews by Monday for timely publishing
  - Weekly meeting time potentially moving to Friday 8:30 AM PT or Monday 10 AM PT

### Additional Projects

  - Jakub to provide:
      - Updated Looker dashboard
      - Programmatic SEO recommendations
      - Suggestions for combining/pruning existing articles

---

## Action Items

**Jakub Rudnik (GrowthX)**
- Update Looker dashboard with more detail using template from other managing editor
- Refresh keyword research
- Send new dashboard template to Tanmay and Mario early next week
- Provide programmatic SEO (PSEO) recommendations for article optimization
- Discuss Webflow publishing automation options next week

**Tanmay Sarkar (Airbyte)**
- Complete article reviews by Monday to allow two days for GrowthX publishing
- Add Jakub to Profound AI visibility tool (pending email ID)

---

## Transcript
**Jakub Rudnik:** It's a long story, but I was in Philly for two days to see a friend's graduation. We surprised him. None of us had ever visited him out there yet, so like six of us did. I'm actually sitting in Cleveland at a friend's house. Longer story, but the house next to him is available to purchase. We may move here now. It kind of happened all at once. So this week has been like just a very busy trying to work like at night, 5 a.m. on a plane, trying to catch up. I owe you a couple of things. I'm very sorry this week fell apart. So but yeah, I'm on my friend's couch on my hotspot because I can't figure out his Wi-Fi.

**Tanmay Sarkar:** So this is like remote work. Maybe that's worse, maybe it's better. I don't know which way. Yeah, travel and work is always fun.

**Jakub Rudnik:** And last week we had our vacation. So it was like this wasn't supposed to be like out of town. This is like doubling down. So I just feel behind. But this weekend, we've like canceled our other plans mostly. So we'll have some family time, but we can like catch up on some stuff. We both are like feeling behind in ways that we don't like to feel. This is Nico's last day.

**Nicolas Fernandez:** Yeah, hello, how are you doing?

**Jakub Rudnik:** So we're bummed about that, but excited for a good opportunity.

**Nicolas Fernandez:** Yeah, I'm actually sad about leaving. It's been a short time, but you're great. I mean, I already told you everything that I was involved in.

**Jakub Rudnik:** So right on. Yeah, Nico put together an agenda with all the what's published, what's in progress for us, what we are pitching for next. Those basics. I know I owe you updating the Looker dashboard. We have a template that I use with my other managing editor. So I'll just recreate that with more detail and update. So that's not done yet. It's one of those that's just like, I keep putting it off. I think I'll get to it this week. And then the PSEO stuff. And then we'll refresh some of the keyword research as well.

**Tanmay Sarkar:** So what I feel is I think there's some ready to publish articles, which I have already approved. So those, we need to just publish those. I think other than that, everything is going fine. Dashboard thing, I think, as you mentioned, we'll take care of it. We just want to keep a track of everything so that we know that whatever we are producing gives us enough output or whatever we are trying to measure those things like traffic increase or anything is decreasing, how we can tackle those. Also, I was chatting with one of the Profound guys, the AI visibility tool, and they were mentioning that if we use schema, AI platforms tend to grab those in a structured manner and like share more output accordingly. So they have shared one article with whatever schema they have used. So I can share that with you guys. You guys can have a look. I think if you can integrate those to your prompt that you would generate, once you generate those schema along with the article and we add those while publishing the article, I think those will help in terms of more search engine visibility and AI platforms visibility.

**Jakub Rudnik:** Yeah, that's a good nugget. We can do that for sure. Are you using them, or are you just discussing, like, kind of in more of that early stage, speaking with them?

**Tanmay Sarkar:** We are using Profound for our AI visibility, and there are multiple schema. They were showing me, like, FAQ schema, speakable schema, product schema. There are multiple schema that we use, and they have seen that those tend to give good results, and those tend to work better in AI platforms.

**Jakub Rudnik:** Okay, cool. Yeah, we'll do that. I think some of those are obvious in schema. I'm not sure if I've ever, like, seen someone say that, but it made sense to me that we should be doing that. So if we haven't, that's a miss, and we'll update that process. But then if there's other nuggets from them, feed them our way so we can implement it into the content. I think, I mean, just every week with three clients, someone's asking what a recommendation, what can we do? So both, like, for our general knowledge, but also, specifically, if they're seeing anything within your content. And I want to make those updates and improve that at that level. So that's useful. We were just having another conversation with a different client. And so the new dashboard will have some, we can write out LLM traffic too. And so we can kind of compare that with what you're seeing with Profound. And then I would love to be able to cross match that and see how much traffic is actually represented just from GA4. Because my guess is it's really low compared to the actual impressions of what someone would be seeing there.

**Mario Moscatiello:** I bet you're seeing that. He's probably like, yep, we have that data. It's way different. But then we can get a better sense. It's just that GA4 doesn't have any visibility into view-through conversions. I put this as the way I think about it is sort of like the view-through conversions on LinkedIn. Because we can see the view-through conversions, because LinkedIn gives you the data on view-throughs, we use attribution tools. And we can see like basically in a bunch of cases, we're not going to see a conversion, but we can see the view-through conversion. From the company. And so I think in a way, the only way of knowing how many impressions you want at GPT is by integrating with them and getting the data from them, because otherwise you're not going to know. Because the one thing is like for somebody to search like four data platforms and say like, oh, Airbyte comes up, like, oh, what is the best data platform? Airbyte comes up, you look at it. And then maybe like two hours later, you just type Airbyte in Google, but that's going to come as an organic impression from Google, and you search and then probably you click on a brand ad. But that's, I think a lot of the way I think about AI search is that it's an impression game. That's the best way for me to explain that.

**Jakub Rudnik:** Yeah, definitely. If you have any data on your blogs or other different site sections, either from hockey stack or Profound, anything we can share?

**Mario Moscatiello:** Yeah, I'm happy to add you guys to any of these tools. I don't know if you guys have like an account that you use as a shared login, or if it's just you, but we should add someone.

**Tanmay Sarkar:** If you can share one email ID of yours, I can add that to Profound so that you can see. That would be good. And we are also trying to integrate our website with Profound, so that's still in the process with security. So once we integrate that, our website and GA4, I think we'll be getting more data inside Profound.

**Jakub Rudnik:** Yeah. As long as it doesn't cost you more, that'd be helpful. We used hockey stack at ActiveCampaign. It was really helpful for finding stuff that would appear in different parts of the journey and also some areas that we're attributing nothing to, but then once we got hockey stack data versus like normal conversion stuff, we were finding really good results and kind of duplicate that in different areas. So that will help me. I think we can run more like standard keyword research, but then supplement like where we're looking and, you know, kind of pattern match to the keyword strings and things like that. So it'll only help like improve the topic selection and our refresh selection as well. Okay, cool. And Mario, I know I owe you guys a couple of things still on the dashboard side. And then the one that I mentioned, the LLM stuff, we'll also be able to separate new content and refresh stuff. And then we can look at week over week, month over month. Eventually, we'll get to quarter over quarter and stuff. But there's another template that my other managing editor uses, and that one will be an improvement from what we had. So I'll have that to you early next week. And the same thing, PSEO is like, halfway started, so I just will get you that.

**Mario Moscatiello:** So I'll use some of this weekend and early next week. Yeah, last two weeks were crazy for us as well. I had a leadership retreat the week before, and then this week were QBRs and product cons, which we do once a quarter. So I've got zero work done for the past two weeks.

**Jakub Rudnik:** Right on. Yeah, so let's all catch up and like get our lives in order, because we had vacation straight into this. I feel like I haven't been in my home for a minute. So we have all those things. Nico's done after today, so we're going to be bringing in new CMs. It probably will be a couple people over the next couple weeks, as we're training a bunch of CMs really quickly. We need to get that quality to where they should be, especially on a more technical client like you all. But I think I can use experienced CMs from other parts of the company to supplement. So just generally, probably mostly to be aware on any content, like comments and back and forth, there will probably be a different mix. But our goal is to not use anybody before they're ready to support you. And Nico did a lot of off-boarding on what you guys look for and the nuances. So we should be pretty seamless, but just want to call that out because it'll be a little bit different.

**Mario Moscatiello:** Well, Nico, best of luck in whatever else you do next.

**Nicolas Fernandez:** Thank you very much. Yeah, and just for you to know, everything for the week is done, all the articles. I still have four publishings to do. One thing that I want you to know is that sometimes, I don't know if this is from Webflow or anything, it keeps logging me out for some reason. So that tends to complicate the publishing a little bit, but it's doable.

**Tanmay Sarkar:** That's why I couldn't reach the 15 articles for the week, but I'm trying really hard to do it for today. Yeah, so what happens is if someone else is also working on Webflow at the same time, from a single ID.

**Nicolas Fernandez:** I'm seeing that as well. Yeah.

**Tanmay Sarkar:** Yeah, so it says that we're floating. So I was taking advantage of my mornings to publish, yeah. Thank you so much.

**Jakub Rudnik:** It's obviously something we deal with across clients sometimes, depending on who's using. So there's some automation that we can build. I saw our eng team kind of put that into a public channel this week. It's one that I haven't dug into yet.

**Tanmay Sarkar:** I think it's something we can save that publishing time, and then it'll just keep that speed. Like, you can push everything via Webflow integration to Webflow directly. You don't have to manually publish. There is a way.

**Jakub Rudnik:** Yeah, so I'll chat through that probably next week when I get a better guess for what that means, but it should be something to help us. We did it in the past with Whalesync and Zapier. There are multiple ways to do it, basically.

**Tanmay Sarkar:** Okay, cool. But that'll be more, we'll talk soon on that.

**Mario Moscatiello:** No, just from how we feel about the volume that we're pushing through and because we're doing a lot of content refreshes, I know there was an effort on pruning some of the content. I know there was an effort on where are we with a bunch of those things, like just as a recap for me or where we are, what does next month look like? And Jakub, again, appreciate it that it's been active these past two weeks, but what do you think the next 30 days should look like?

**Jakub Rudnik:** Yeah, yeah. The volume we've, you know, from pure number of pieces, even if you like take down word count, like refreshes are, I would count them as like less because there's a lot of existing content, right? We're above what we typically do 25% or so from like most clients, so we're able to hit that, and from that piece, I think we are doing quite well. You know, if anything, it's like sometimes the publishing were just, that's where there's been problems, but we've hit those numbers. We've done more because we've done more of the refresh. So I think we should hit the same numbers and keep that continuing. Good reminder on the running, Tanmay, am I waiting on you on that as well?

**Tanmay Sarkar:** Like, I'm just waiting for programmatic SEO things, but other than that, I think I have shared everything. The new topics are already there, and refresh topics are also there in the pipeline. So I think we are good for next 30 days.

**Jakub Rudnik:** Yeah. That's like our meat and potatoes. So that's all good stuff. I think that additional pieces are some recommendations for me on existing articles, if there's anything to be combining or pruning. So all that, and then the programmatic recommendations on the new pages. So that's more of like additional technical stuff. So on my end, but the CM work is continuing. It's been good. And I think it's just the reporting where we are missing right now.

**Mario Moscatiello:** Okay. And sorry, I might have missed it at the beginning of the talk, but when can we get the new reporting?

**Jakub Rudnik:** By Tuesday.

**Mario Moscatiello:** Perfect. Yeah, sounds great.

**Tanmay Sarkar:** Oh, sorry.

**Tanmay Sarkar:** And also one thing I was thinking, once the new person is on boarded, I think our weekly meeting is generally on Wednesday, right? So I finished the article reviews by Monday so that you get two days time to publish those articles, right? Otherwise, if I finished by Tuesday or Wednesday, and sometimes there are back and forth because I review those, I share some comments, you can go and edit. So there are some backlogs.

**Mario Moscatiello:** I was actually thinking of moving these meetings to Fridays. I don't know if that's something that works for you guys, but just better on our end. It's the end of the week and we can all talk about the week and then plan for the next one. Also because, you know, selfishly, Tanmay and I don't need to be in the office together and I can really use the time to have other meetings that are in person. And so Fridays working from home, it's very easy for me to be way more focused than I normally am in the office. But again, it's up to you guys and if you have a preference.

**Jakub Rudnik:** No, no. I mean, we do like just from the company generally puts on Wednesday and Thursday. I have a wide open Friday and actually would love to move one out. And I think that's the way we can like be flexible to what works for everyone. I know David is in Europe. So for me, like for Tanmay and I, like 9 AM PT works. It's like I can be very flexible. I'm just realizing that within Wednesday and Thursday, most of our agency meetings and there's too much overlap. So, yeah, no problem.

**Mario Moscatiello:** So, yeah, with 9 AM Fridays going forward. That works for your time? Yeah, yeah, works for me. OK, perfect. So let's move that. And yeah, like it's just easier on my end. So we can do nine on Fridays. I think it's a decent time in Europe for David.

**Jakub Rudnik:** Yeah, he should be good there. Honestly, this one was a hard one for him because it was later. I am PT. It's 6 PM on a Friday, though. Tanmay, is 8:30 AM too early for you?

**Tanmay Sarkar:** 8:30 on Friday? Yeah, yeah, yeah, it's because I'll be at home.

**Mario Moscatiello:** I don't know if that's any better, but I don't want David to be at 6 PM on Friday. Or would Mondays be better?

**Jakub Rudnik:** Monday is an easy one for me as well. Okay, I moved it to Friday temporarily, but I'll ping David and see what he prefers.

**Mario Moscatiello:** Then we're pretty free on those two days, so I don't mind. I think Monday also works. Okay, Monday morning works for me as well. I could do it, but the issue with Mondays is that I have a 9 AM sending call, so I can only do 10 AM Pacific, which is 7 PM East time.

**Jakub Rudnik:** Cool. Yeah, I'll let David respond.

**Mario Moscatiello:** I'll put that in the chat, and then we'll just update it. Okay, sounds good. All right, awesome.

**Jakub Rudnik:** Thanks, guys. Have a good long weekend.

**Mario Moscatiello:** You too. Well, let us know how you get on with the new house.

**Jakub Rudnik:** Yeah, I will. Okay, bye.

**Nicolas Fernandez:** Bye, guys.
