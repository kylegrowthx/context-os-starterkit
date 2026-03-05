# Q&A with GrowthX on data and tech SEO 

<metadata>
date: 2025-05-20
time: 12:01 UTC
duration: 52 minutes
organizer: Branko Kral (GrowthX)
participants: Branko Kral (GrowthX), Jess Scott (GrowthX), Carmel Schetrit (Siit.io)
fathom_recording_id: 63564491
fathom_url: https://fathom.video/calls/304059156
share_url: https://fathom.video/share/_aDZoe39SAxaBd9eBvz_a39U-pxrP56Y
source: fathom
enriched_on: 2026-03-04 12:00 UTC
</metadata>

---

## Summary

Branko and Jess conducted a deep-dive analytics audit with Siit.io CEO Carmel Schetrit, investigating PostHog and GA4 data to understand content-driven conversions. The key finding: Siit.io's analytics setup was mostly correct but underutilized—their top-converting content includes IT help desk, migration guides, and French blog content, with conversions driven by form submissions. The team agreed to prioritize content production and distribution over technical SEO micro-optimizations, with Branko committing to create a Loom video summary of GA, PostHog, and Google Ads insights, while Carmel will explore Reddit visibility and content distribution investment.

---

## Context

Siit.io (a SaaS company operating in the IT infrastructure/operations space) engaged GrowthX to help optimize their content strategy and understand content performance beyond surface-level metrics like traffic. Carmel Schetrit is based in Tel Aviv and manages Siit.io's marketing and product strategy. The relationship appears to be in the strategic advisory phase—this meeting was focused on auditing existing analytics implementation to uncover conversion drivers from their blog and glossary content. Siit.io has GA4 and PostHog set up but hadn't fully explored the conversion funnel data. The broader context: Siit.io had experienced a traffic spike from trade show attendance and an AI agent product launch, but Carmel wanted to understand which content pieces actually drive business outcomes rather than just impressions.

---

## Relevance

**To GrowthX Delivery:**
- Reinforced GrowthX's methodology: analytics-first content strategy, prioritizing content production and distribution over technical micro-optimizations. Branko demonstrated GA4's power when properly configured, countering the perception that GA4 is unusable.
- Identified that conversion tracking requires proper event setup in both GA4 and product analytics—Siit.io had the infrastructure but hadn't fully leveraged it for content strategy decisions.
- Monthly reporting cadence agreed upon to reduce over-analysis of short-term fluctuations and focus on strategic patterns.

**To CheckThat:**
- Discussed how AI visibility and AEO differ from traditional SEO; acknowledged schema markup's limited impact relative to content authority and distribution. Relevant for CheckThat positioning: building visibility through authoritative content and partnerships is more impactful than technical optimizations alone.

**To GrowthX Business Development:**
- Siit.io shows healthy engagement signals: they have the tools, they're thinking strategically about content ROI, and they're open to GrowthX's advisory on distribution (Reddit investment). Potential for expanded engagement if content production ramp yields results.
- Account health indicator: Carmel is asking the right questions (funnel attribution, content-to-conversion mapping), suggesting she's invested in optimizing the relationship and validating GrowthX's impact.

---

## Overview

- Siit.io's GA4 setup is solid; the key insight is that their best-performing landing pages for conversions are IT help desk, migration guides, and glossary—mixed top and bottom funnel content—validating a broad content strategy over narrow targeting.
- PostHog custom events need standardization (Carmel acknowledged inconsistencies), but the form submission tracking is reliable and matches GA4 data, enabling conversion analysis once properly configured.
- French blog content surprisingly outperformed in both traffic and conversions despite Siit.io not intentionally targeting French-speaking markets—unexplored opportunity for distribution.
- Google Ads is synergizing well with organic traffic; focus should be content production at scale and distribution partnerships (Reddit) rather than technical schema markup or AI engine optimization.
- Attribution models in GA4 need exploration—last-click attribution may undercount the impact of early-funnel content; Branko recommends testing alternative models.
- Monthly reporting prevents over-analysis of weekly fluctuations and enables strategic decision-making on content investment and distribution.

---

## Key Topics

### Analytics Setup and Conversion Tracking

  - Current setup: PostHog for granular data, Google Analytics 4 (GA4) for general trends
  - Key conversion events: "Sign up for free trial" and "Book a demo"
  - PostHog custom events and actions not properly capturing full conversion funnel
  - GA4 showing some conversion data, but potential setup issues identified
  - Action item: Branko to investigate and optimize PostHog/GA4 setup for accurate tracking

### Content Performance Analysis

  - Recent traffic spike attributed to trade show attendance and AI agent launch
  - Google Ads performance improving, with synergies between paid and organic traffic
  - Top-performing content includes IT help desk topics and migration-related articles
  - French blog content showing surprising performance
  - Need for better understanding of content-driven conversions and referral traffic

### SEO and AI Optimization Strategies

  - Focus on producing high-quality, authoritative content over technical optimizations
  - Prioritize content distribution and partnerships for exponential growth
  - Schema markup useful but not critical; focus on other authority signals
  - Explore distribution channels like Reddit for increased visibility
  - Utilize blog and glossary content as potential link magnets

### Reporting and Decision Making

  - GrowthX developing standardized Looker-based report across clients
  - Monthly reporting cadence agreed upon to avoid over-analysis of short-term fluctuations
  - Branko to create a Loom video summarizing GA, PostHog, and Google Ads insights for Carmel and Jess

---

## Action Items

**Branko Kral (GrowthX)**
- Investigate PostHog data for more conversion info. Record 5-10min Loom video on GA, PostHog, Google Ads data conclusions for Carmel and Jess

**Carmel Schetrit (Siit.io)**
- Continue discussions regarding Reddit visibility and investment for content distribution

---

## Transcript
**Carmel Schetrit:** Woke up in Paris.

**Carmel Schetrit:** On Wednesday, I woke up in London.

**Carmel Schetrit:** It was a lot.

**Carmel Schetrit:** How's your sleep when you travel?

**Branko Kral:** Not amazing.

**Carmel Schetrit:** So this weekend, I was very tired.

**Carmel Schetrit:** And then I flew back to Tel Aviv on Sunday.

**Carmel Schetrit:** It was great to sleep in my own bed.

**Branko Kral:** Oh, yeah.

**Branko Kral:** Own bed is a big deal.

**Branko Kral:** I've read about it.

**Branko Kral:** And I heard people talk about it a lot during COVID, especially people who would travel a lot.

**Branko Kral:** then they couldn't because nobody could really.

**Branko Kral:** And then there was a lot of talk about how healthy it is to sleep in your own bed and how your brain doesn't actually shut off when you're sleeping at a new place.

**Branko Kral:** It's so true.

**Branko Kral:** I would wake up at like 4 a.m.

**Carmel Schetrit:** disoriented.

**Carmel Schetrit:** Yeah.

**Branko Kral:** For me, it's one of those things where once I've read about it, it bothers me even more.

**Carmel Schetrit:** Sorry.

**Carmel Schetrit:** I get that.

**Carmel Schetrit:** Yeah.

**Carmel Schetrit:** It's a great sleep in my own bed.

**Carmel Schetrit:** I need to go back to Paris at some point, but I just, with California, I don't know, I think you joined after Fathom, but I was in California for three weeks.

**Carmel Schetrit:** So with that, and then this, and I just, I need to be home.

**Jess Scott:** It's not that I'm going say that I'm to It's like every time I talk to you, in a different location.

**Jess Scott:** Yeah.

**Jess Scott:** So today I'm working from home.

**Carmel Schetrit:** But you have a U.S.

**Carmel Schetrit:** accent, right?

**Branko Kral:** So do you live there too, or you have?

**Branko Kral:** I am American.

**Branko Kral:** I'm from California.

**Carmel Schetrit:** I moved to Tel Aviv a year and a half ago.

**Carmel Schetrit:** So not that long ago, actually.

**Branko Kral:** I'm American too, and I've lived in California for eight years, but I don't have the accent.

**Carmel Schetrit:** I moved there when I was older.

**Branko Kral:** Where did you live?

**Branko Kral:** In Mammoth.

**Branko Kral:** Oh, sick.

**Carmel Schetrit:** Yeah, yeah, yeah.

**Carmel Schetrit:** I don't think I've ever met anyone that actually lived in Mammoth, only you guys camped in Mammoth.

**Branko Kral:** Yeah, yeah.

**Branko Kral:** I've lived there for a bit of a...

**Branko Kral:** Seven years.

**Branko Kral:** It's quite the gem.

**Branko Kral:** I live at a very similar place now, but Mamet is quite the gem.

**Branko Kral:** I just wanted to be closer to family for change.

**Branko Kral:** And with some life goals ahead of me, I really like it where I am now in Slovakia, but for like three years...

**Carmel Schetrit:** Beautiful.

**Carmel Schetrit:** It's on my list.

**Carmel Schetrit:** Yeah, my window here is like a painting.

**Branko Kral:** And yeah, there's actually a good amount of tourism here, too.

**Branko Kral:** And since you're in Israel, I'll tell you, there's a synagogue like 100 meters this way.

**Carmel Schetrit:** No, wait.

**Carmel Schetrit:** I didn't even know there was Jews there.

**Carmel Schetrit:** There's not many left.

**Branko Kral:** I didn't have any Jewish friends until I moved to the States because there's just not any Jews here, right?

**Branko Kral:** And then in the U.S.

**Branko Kral:** you just have Jewish friends because there's a lot of Jewish people.

**Branko Kral:** And it was such a mind opener to me to realize, oh, damn, okay, that's why I never met any Jewish people because there aren't any.

**Carmel Schetrit:** I mean, I didn't even know they existed there.

**Carmel Schetrit:** It's surprising there's a synagogue.

**Carmel Schetrit:** Well, there's a lot of Jewish history.

**Carmel Schetrit:** There's a lot of synagogues.

**Branko Kral:** They just don't get used that much.

**Branko Kral:** They're mostly used for events.

**Branko Kral:** I was actually at an event.

**Branko Kral:** It was a live chess game with...

**Branko Kral:** At a synagogue?

**Branko Kral:** Yeah, the figures were people in costumes.

**Branko Kral:** No way.

**Branko Kral:** And there were two people actually playing chess, and then the people in costumes were acting it out.

**Branko Kral:** But it was pretty entertaining.

**Branko Kral:** So that's how they get used more for concerts now and events.

**Carmel Schetrit:** Wow, that's so funny.

**Carmel Schetrit:** Yeah.

**Carmel Schetrit:** I'm going to tell my boyfriend that.

**Carmel Schetrit:** Yeah, we were there on Saturday.

**Carmel Schetrit:** It was pretty cool.

**Branko Kral:** Anyway, for the agenda, we put something in the calendar.

**Branko Kral:** I think it can be a tentative agenda still.

**Branko Kral:** We didn't update that word, because I'd just like to offer you the time and flow through it with you, answer questions.

**Branko Kral:** I put post hoc and GA data.

**Branko Kral:** You told us about some...

**Branko Kral:** For instance, we have the Google Ads data.

**Branko Kral:** I would definitely like to look at the Looker report.

**Branko Kral:** I like it a lot.

**Branko Kral:** There are also some things I could recommend you ask to maybe improve further.

**Branko Kral:** But it gives us some really good ideas for what report we could build.

**Branko Kral:** We'll be getting into that more and more.

**Branko Kral:** I'll comment on that in more detail.

**Branko Kral:** Then we can talk briefly about schema and maybe how to set up your team.

**Branko Kral:** Yeah, that would be awesome.

**Carmel Schetrit:** What I really wanted to do, well, honestly, thank God and the lucky stars and whoever that were starting to bounce back in traffic because my heart was sinking.

**Carmel Schetrit:** I mean, I think historically, I mean, it's really hard to say historicals because we're such a tiny company, but apparently historicals aren't great in April in general.

**Carmel Schetrit:** It was very bad timing for me because it was the time that I.

**Carmel Schetrit:** We took vacation and so it seemed very directly correlated.

**Carmel Schetrit:** But there's been a lot of traffic spiking back up.

**Carmel Schetrit:** I think especially what I mentioned on Slack from the show that we were at last week and also from the AI agent launch, which has been really good.

**Carmel Schetrit:** Plus, we've been getting I don't know exactly how Google algorithm works, but we've been getting once we started getting more traffic for our PPC or like the Google ads for our AI agent campaign, it started it started rolling like we started seeing more.

**Carmel Schetrit:** So last week was a really strong week, which is good news.

**Carmel Schetrit:** One of the things that wanted us to cover, in addition to what you said, was how can we, I think maybe on post hoc, but how can we look into referral traffic?

**Carmel Schetrit:** And understand the correlation between our different articles.

**Carmel Schetrit:** And this is maybe what I was trying to get out with the dashboard so that I can report back to the team what content is driving our traffic and maybe ultimately some conversions would be super helpful for our conversation as well.

**Branko Kral:** Okay.

**Branko Kral:** Okay.

**Branko Kral:** So I guess that's the first question.

**Branko Kral:** Uh-huh.

**Branko Kral:** Just going right in.

**Carmel Schetrit:** Yeah, yeah, yeah.

**Branko Kral:** That's a good thing.

**Branko Kral:** Well, let me start sharing the screen.

**Branko Kral:** So.

**Branko Kral:** GA with PostHog.

**Branko Kral:** I stopped looking at GA.

**Carmel Schetrit:** I mean, like, you know, I look at it a little bit, but I go mostly off of PostHog data because GA is a  show.

**Carmel Schetrit:** And I just feel like it's not as, as you said.

**Carmel Schetrit:** So maybe for the trend, but I just feel like I'm not getting the data that I need from there.

**Carmel Schetrit:** So I've been going mostly off of Fathom.

**Branko Kral:** Yeah, because you felt like it was the conversion data or the traffic data that you wouldn't trust in GA?

**Carmel Schetrit:** The conversion data you definitely can't trust in GA.

**Carmel Schetrit:** And even the traffic, it shows you a general direction.

**Carmel Schetrit:** It's something that I talked a lot about with Kyle, but it's not that granular.

**Carmel Schetrit:** And PostHog lets me get more granular and slice and dice the data better.

**Carmel Schetrit:** So that's why I've been going off of that.

**Carmel Schetrit:** Cool.

**Branko Kral:** Yeah, those charts are kind of similar, but I like PostHog a lot.

**Branko Kral:** You're right.

**Branko Kral:** So here I've filtered it a bit to all the traffic that goes to Glossary or Blog.

**Branko Kral:** right.

**Branko Kral:** So.

**Branko Kral:** This pipe character is the OR sign in regular expressions.

**Branko Kral:** It's just one way to define what I want to look at.

**Branko Kral:** The channel type would be organic search.

**Branko Kral:** And I excluded French since I don't believe we have worked on it, but should I put it back in there for you?

**Carmel Schetrit:** No, it's fine.

**Carmel Schetrit:** We're not doing, yeah, we're not working on it with growthx.

**Carmel Schetrit:** Yeah.

**Branko Kral:** And I did the last 90 days.

**Branko Kral:** Because sometimes we can do more.

**Branko Kral:** I think 90 is good.

**Carmel Schetrit:** Yeah, yeah, yeah.

**Branko Kral:** If you're mentioning that April could be a low month, sometimes you could do 13 or 14 months so that you do the full year and then you do the same month last year as well to see how it actually compares, whether the seasonality holds true or not.

**Branko Kral:** The thing is that I joined in December.

**Carmel Schetrit:** December, so that's the reason I don't really compare it to last year because there were.

**Carmel Schetrit:** No marketing efforts.

**Carmel Schetrit:** They just said that it's a low month in terms of trials and demos, but again, we're tiny, so no use.

**Branko Kral:** It could be a benchmark before and after of, hey, this is what you had before marketing, this is what you have since you started marketing.

**Carmel Schetrit:** Yeah, that's true.

**Branko Kral:** But that's easier.

**Branko Kral:** I could just switch that.

**Branko Kral:** What I'm looking at here now are those conversion numbers.

**Branko Kral:** So we have the traffic chart.

**Branko Kral:** Like you said, you had a strong week.

**Branko Kral:** I believe it actually, it was almost the strongest.

**Branko Kral:** So, yeah, it's looking up.

**Branko Kral:** And the thing I like the best is that for a couple of weeks in a row now, we have the rising trend.

**Branko Kral:** So when it's going down, which...

**Branko Kral:** We always like that up and to the right.

**Branko Kral:** There should be a song about it.

**Branko Kral:** From early March until mid to late April, it was going down even with this kind of a little...

**Branko Kral:** But it's still a downward trend to me.

**Branko Kral:** So at the end of April, it's stabilized, which is an early sign.

**Branko Kral:** So I would say for two to three weeks, it's been going up and to the right.

**Branko Kral:** Now, visitors views bounce rate.

**Branko Kral:** So this is just traffic, and I need to get to conversions.

**Branko Kral:** This is what I saved from when I was poking around.

**Branko Kral:** I didn't look at conversions here yet, but I'm getting offered.

**Carmel Schetrit:** I don't know that we have it set up super well, to be very honest with you.

**Carmel Schetrit:** I'm like, wear all hats for marketing operations, too.

**Carmel Schetrit:** And I don't know that we have it set up properly with HubSpot in terms of tracking conversions.

**Carmel Schetrit:** So it might not.

**Carmel Schetrit:** I put the snippet from HubSpot, but it might not be super accurate.

**Carmel Schetrit:** I'm not sure.

**Carmel Schetrit:** Yeah, yeah.

**Branko Kral:** So.

**Branko Kral:** On your side, which conversions do you care most about?

**Branko Kral:** Which conversions should I be trying to dig out in post hoc?

**Branko Kral:** So there's two.

**Carmel Schetrit:** There's the sign up for free trial.

**Carmel Schetrit:** That's one conversion.

**Carmel Schetrit:** And then the second one is book a demo.

**Carmel Schetrit:** Okay, makes sense.

**Carmel Schetrit:** And it's simple that you only have two?

**Carmel Schetrit:** Yeah.

**Branko Kral:** Okay, so I am tempted to go into GA, but let's see.

**Branko Kral:** If I don't find it real quick now, I'm just making a note.

**Branko Kral:** I have a notebook open on the side.

**Carmel Schetrit:** Like we have, so with the PPCI on his looker dashboard, there's still some discrepancies that we're seeing that he's trying to work through with HubSpot conversions.

**Carmel Schetrit:** But for the keywords, we have, he synced it with HubSpot.

**Carmel Schetrit:** So we have the trial.

**Carmel Schetrit:** a note.

**Carmel Schetrit:** be able to

**Carmel Schetrit:** Demo conversions, supposedly.

**Carmel Schetrit:** But here, I just don't think that PostHug is able to, or I don't think we have it set it up, optimized in a way that we can see all the conversions on PostHug.

**Carmel Schetrit:** Yeah.

**Carmel Schetrit:** Well, when I'm looking at the...

**Carmel Schetrit:** Can you click on the next, or maybe it's in his back console that he should need, that there were actual conversions.

**Carmel Schetrit:** If you click on the next, let's see.

**Carmel Schetrit:** Yeah, that tripped up.

**Carmel Schetrit:** So I think it's on our actual Google console.

**Carmel Schetrit:** Yeah, Google dashboard.

**Carmel Schetrit:** Yes, because it's an issue with the primary secondary conversion issue.

**Carmel Schetrit:** I don't know, something on Google's back end.

**Carmel Schetrit:** But it's on the, let me pull it up, I think it's on the Google ads dashboard.

**Carmel Schetrit:** I'm going take it just real quick.

**Branko Kral:** I could have anticipated this one.

**Branko Kral:** Let's see.

**Branko Kral:** Where did he, where did he see it?

**Carmel Schetrit:** May.

**Carmel Schetrit:** Apply.

**Carmel Schetrit:** Let's see.

**Carmel Schetrit:** Maybe it's on the campaign level itself.

**Carmel Schetrit:** Oh.

**Carmel Schetrit:** showing this to me yesterday.

**Carmel Schetrit:** There are conversions happening, and I saw them yesterday, but this was the issue that he had.

**Carmel Schetrit:** Ported.

**Branko Kral:** Yeah, yeah.

**Branko Kral:** I can ask him where it is.

**Carmel Schetrit:** But anyways, for us to figure out, maybe we work backwards.

**Carmel Schetrit:** For us to get to a state where we can track conversions from blog, what we need to do, you're saying, is to make sure that HubSpot conversion data is properly feeding into PostHog?

**Carmel Schetrit:** Yeah, of course, yeah.

**Carmel Schetrit:** Yeah, yeah.

**Branko Kral:** And, you know, you could do two things, which, you know, when I look at Google Analytics, even though I'm also not a big fan of it, it's not fully cooked, you do have the key events in here, which are the conversions, and you also want to assign a value.

**Branko Kral:** So you probably have an estimate of the average value of each free sign-up.

**Branko Kral:** Yeah.

**Branko Kral:** I mean, there's a rate at which...

**Branko Kral:** They turn into a paid user.

**Branko Kral:** So for instance, when I was at SEMrush, we were measuring paid signups.

**Branko Kral:** And every paid signup had the value of about $125 to us.

**Branko Kral:** It was a big average of just a lot of data.

**Branko Kral:** So you probably have that too.

**Branko Kral:** So then at SEMrush, the free signup was one step higher up the funnel, like the free trial.

**Branko Kral:** And that had the value of $5 maybe, if I remember it right.

**Branko Kral:** So maybe you have the same.

**Branko Kral:** And if you can put that on here, then that makes it even better.

**Branko Kral:** Because I assume that booking a demo has maybe, I don't know, but they probably have a different value.

**Branko Kral:** I'm not sure which one would be bigger.

**Branko Kral:** Because if you're booking a demo with a human, maybe they actually have a value.

**Carmel Schetrit:** They're normally the same, our values.

**Carmel Schetrit:** They differ between outbound and inbound.

**Carmel Schetrit:** Outbound is clearly higher than inbound in terms of opportunities.

**Carmel Schetrit:** Trial and booking a demo, I think, I have to get the exact numbers, but I think they're generally close to being the same because even our trials end up getting on a call with sales.

**Carmel Schetrit:** It's like a sales-assisted trial.

**Carmel Schetrit:** So they talk to a human in the end.

**Carmel Schetrit:** Mm-hmm.

**Carmel Schetrit:** Mm-hmm.

**Branko Kral:** Okay.

**Branko Kral:** So you're saying then trying for free, the higher value, higher than booking a demo?

**Carmel Schetrit:** I'm saying that I'm pretty sure that they're quite similar figure, but I need to get the exact numbers.

**Carmel Schetrit:** I am seeing, though, he sent, if you, I can share my screen really fast just so you can see the weekly report.

**Carmel Schetrit:** right.

**Carmel Schetrit:** All All All All All Thank

**Carmel Schetrit:** He sent me, the PPC guy.

**Carmel Schetrit:** Let share one sec.

**Branko Kral:** And then I have a thought on the HubSpot connection, but you'll show me that first and I'll tell you more.

**Branko Kral:** Okay.

**Carmel Schetrit:** Can you see my Slack?

**Carmel Schetrit:** Yeah.

**Carmel Schetrit:** Okay.

**Carmel Schetrit:** So I can see this.

**Carmel Schetrit:** Or this is what he sent.

**Carmel Schetrit:** We generated six leads and 13 ads for form submit.

**Carmel Schetrit:** I think I, so for me, the, I think this, what he's counting, there's like, I don't know.

**Carmel Schetrit:** He's having an issue too with the HubSpot integration, but we got like 12 trials and demos booked last week from PPC.

**Carmel Schetrit:** Anyways, I, I just want.

**Carmel Schetrit:** Show you what he sent.

**Carmel Schetrit:** And I don't know if there's anything here.

**Carmel Schetrit:** What's the definition of a HubSpot lead?

**Branko Kral:** You said it's a trial or is it different?

**Carmel Schetrit:** Trial and demo.

**Carmel Schetrit:** Either.

**Carmel Schetrit:** Oh, here we go.

**Carmel Schetrit:** So this is the daily requests.

**Carmel Schetrit:** So this is for last week.

**Carmel Schetrit:** So, oh, this is still conversion zero because he's having a HubSpot.

**Carmel Schetrit:** Okay, never mind.

**Carmel Schetrit:** I thought I would be able to show you.

**Carmel Schetrit:** Um, yeah, this is the thing he's working on.

**Carmel Schetrit:** Okay.

**Carmel Schetrit:** Yeah.

**Branko Kral:** So what happens is that they book a demo or ask for a free trial and then HubSpot captures them in the CRM, right?

**Branko Kral:** Yeah.

**Branko Kral:** Yeah, yeah.

**Branko Kral:** But the action probably still happens on the website.

**Branko Kral:** So it should still be website data.

**Branko Kral:** So if there's a better link with...

**Branko Kral:** Google Analytics and Google Ads, that should work.

**Branko Kral:** So when you're connecting it with PostHog, if you have the PostHog tracking tags on the website, you might not even need the HubSpot CRM.

**Branko Kral:** But what you could do, since you're small...

**Carmel Schetrit:** we do.

**Carmel Schetrit:** We have the PostHog snippet on our website.

**Branko Kral:** Yeah, so there should be events in PostHog, and I'll try and dig them out after this.

**Branko Kral:** I'll try and see what PostHog can do in terms of conversion tracking here.

**Branko Kral:** I just need to learn it on the go, and it's sometimes hard to dig out something on a live call.

**Carmel Schetrit:** Of course, of course, of course.

**Branko Kral:** But yeah, think for tracking, for you to be able to connect it, you might not even need the HubSpot data, because I think what Google Ads is tracking anyway is that the lead was sent to HubSpot.

**Branko Kral:** But so the next level up would be that you could also connect your CRM with your website data, and then you could have the full detail of not just the average value,

**Branko Kral:** Of a free trial or a demo call, but what actually happened with that person.

**Branko Kral:** That's when analytics gets best by far.

**Branko Kral:** You probably know, Yep.

**Branko Kral:** You could then probably trace the history of each new customer or at least do much, much better analysis.

**Branko Kral:** Maybe isolate the ones with the higher value or more longevity or such.

**Branko Kral:** But I'll try and find it.

**Branko Kral:** In GA, it's actually there.

**Branko Kral:** I'll click around real quick in GA and then I'll share the screen again.

**Branko Kral:** And I'll show you some numbers at least for which pages convert.

**Branko Kral:** Now, you know, this is last click attribution.

**Branko Kral:** So if somebody comes to your site five times and they don't.

**Branko Kral:** know..

**Branko Kral:** But they come for the sixth time, and they finally get a free trial, the sixth visit with the landing page of that visit will be the one counted as the landing page that brought the conversion.

**Branko Kral:** So it's still data you can use for decisions, but that you also need to play around with the attribution models.

**Branko Kral:** And in you can actually do that.

**Branko Kral:** In Postdoc, I'm not sure yet, but I would hope that you can.

**Branko Kral:** And journey tracking is always the best.

**Branko Kral:** There's some of it in GA.

**Branko Kral:** But yeah, let me finish something, though.

**Branko Kral:** So let's see here, key events.

**Branko Kral:** I'll broaden up the date range now, because I don't have a ton of data, especially for the conversions, I need to actually broaden the date range to the 14 months.

**Branko Kral:** I'll actually share the screen, can at least show you what I'm doing on this exploration.

**Branko Kral:** Okay, so I filtered it in landing pages in GA, just because I know how to find conversions here, and I filtered it to just the blog and the glossary again.

**Branko Kral:** The French is still there, but maybe that's of interest as well for now.

**Branko Kral:** And then I'll order it.

**Branko Kral:** By the key events.

**Branko Kral:** So I assume that's your analytics events.

**Branko Kral:** And I could look in the back end to see how they're defined in the admin.

**Branko Kral:** I wouldn't trust how they define because I didn't set them up and I think they were set up a really long time ago.

**Carmel Schetrit:** Okay.

**Branko Kral:** But so we'll look there in a minute just to make sure.

**Branko Kral:** Sometimes you'd be surprised.

**Branko Kral:** Sometimes at least they're helpful even if they're not great.

**Branko Kral:** And sometimes the fix can be pretty quick.

**Branko Kral:** So the most key events by far are for build an IT help desk in Slack.

**Branko Kral:** And then just overall blog, like the blog list page.

**Branko Kral:** Then your seed round.

**Branko Kral:** Nice.

**Branko Kral:** More help desk.

**Branko Kral:** All you need to know.

**Branko Kral:** And then an alternative that you can migrate from because they're shutting down.

**Branko Kral:** That's a good one.

**Branko Kral:** That's bottom funnel.

**Branko Kral:** Yeah.

**Carmel Schetrit:** That's the help is what Jira Service Management acquired, and that's when we got a lot of migration from them.

**Carmel Schetrit:** Nice.

**Branko Kral:** So I would say it's a pretty good mix of bottom funnel and top funnel, but let's do that.

**Branko Kral:** Let's look at how the conversions are defined, if I can see that.

**Branko Kral:** Key events.

**Branko Kral:** Oh, actually, it's form submit.

**Branko Kral:** Do you only have two forms?

**Branko Kral:** Are these two?

**Branko Kral:** Yeah, they're the only two.

**Branko Kral:** Okay, then these events are actually set up pretty well.

**Branko Kral:** So the report we just looked at is reliable, and your GA is not all that messed up.

**Branko Kral:** But yeah, you should be able to find it in post hoc as well.

**Branko Kral:** So, but yeah, again, this would be the report.

**Branko Kral:** I can send you the link on Slack.

**Branko Kral:** Do you want it, though, or do you dislike GA too much to want to look at this?

**Branko Kral:** Report.

**Carmel Schetrit:** No, no, yeah, send it to me, please.

**Carmel Schetrit:** Cool.

**Branko Kral:** Okay, I'll start a Slack note in our channel.

**Branko Kral:** It's nice to see how fairly clean your Slack is.

**Branko Kral:** Ours is super complex.

**Branko Kral:** We're having to organize, and it works.

**Branko Kral:** It's active.

**Branko Kral:** It's a good time in there.

**Branko Kral:** But holy moly, there's a lot of channels at our company.

**Branko Kral:** And yours is right here.

**Branko Kral:** Okay, I'll have that.

**Branko Kral:** Oh, yeah, remember, this is last.

**Branko Kral:** So, you know, the thing is, GA can work really well.

**Branko Kral:** I used to work as the director of client services at an analytics agency, and that's when GA4 was starting.

**Branko Kral:** And I'm still close with that team.

**Branko Kral:** I own a part of the company.

**Branko Kral:** And they do really, really cool GA4 implementations.

**Branko Kral:** You just need to do them well.

**Branko Kral:** So it's this tool where, sorry, they give you this promise of that you get analytics and, you know, it'll be Google Analytics.

**Branko Kral:** it's kind of industry standard.

**Branko Kral:** But then out of the box, it's a piece of crap.

**Branko Kral:** But then once you set it up well, it works because the concepts there work.

**Branko Kral:** You know, it's based on more event-based analytics.

**Branko Kral:** Before, analytics was based more on page views.

**Branko Kral:** And what happens is once you load a page.

**Branko Kral:** But because of different product and product analytics, the influence has been to measure everything based on.

**Branko Kral:** And every event, like every click, every screen, it doesn't have to be a full page.

**Branko Kral:** And website analytics has adapted.

**Branko Kral:** And so GA4 actually follows that.

**Branko Kral:** So I wouldn't dismiss it completely because it's just the industry norm is the most integrated tool out of all of them.

**Branko Kral:** Just because it's a hard UI is why I don't like it.

**Carmel Schetrit:** Yeah, yeah.

**Carmel Schetrit:** But I have the click set up in PostHog too.

**Carmel Schetrit:** Like all the different clicks that you can click on the page.

**Carmel Schetrit:** So I can slice data that way as well.

**Carmel Schetrit:** But yeah, ideally I want to, in order to create a better content strategy for us in general, I need to, I want to be able to see like a high level view of how our SEO content is performing.

**Carmel Schetrit:** And that, yeah.

**Carmel Schetrit:** That was more the thought behind all of this.

**Carmel Schetrit:** But okay, noted, I will try to figure out how I can get the conversion data properly set up with HubSpot in PostHog or whatever the snippet needs to be.

**Carmel Schetrit:** Yeah, yeah, yeah.

**Branko Kral:** And so that's the input that we're going to talk about for us as well, which is just the standard, I would say, that you want to look at the content that was produced for SEO, and you want to look at how it performs beyond just traffic.

**Branko Kral:** And now we know what events those are.

**Branko Kral:** Now we also know that you have them in GA and that you might have them in PostHog.

**Branko Kral:** I could ask you now, do you know how to get to that data in PostHog or like form submit data in PostHog?

**Carmel Schetrit:** So what I have set up on PostHog, but I haven't dug into it a ton.

**Carmel Schetrit:** Is, one sec, so I have a few things, so we have this, what's that?

**Branko Kral:** I see one time series chart at the bottom of this page, there's a time series chart with events.

**Carmel Schetrit:** So I have the conversion goal here, and then here in the custom events, I don't know that we standardized this really well, to be honest, because it's really hard.

**Carmel Schetrit:** Like, I had our Webflow developer who put this on, like, the snippet on our website create this, but I, yeah, I don't think that this is.

**Carmel Schetrit:** Standardized well, but, like, this is the clicks of, like, the nav trial clicked.

**Carmel Schetrit:** That means that they clicked the start of trial on the navigation bar.

**Carmel Schetrit:** Yeah.

**Carmel Schetrit:** And then in actions, we have the demo trial signup.

**Carmel Schetrit:** Okay.

**Carmel Schetrit:** Yeah.

**Branko Kral:** Okay, so it's right there.

**Branko Kral:** Okay, the last report I was on was the page reports, and I didn't have that, but the web analytics main one does.

**Carmel Schetrit:** Yeah, because page reports is new, so, like, it's, like, new, new.

**Carmel Schetrit:** So I don't know that it has all the stuff.

**Carmel Schetrit:** Yeah.

**Branko Kral:** Okay, so.

**Carmel Schetrit:** And then I can look at conversions.

**Carmel Schetrit:** There we go.

**Carmel Schetrit:** Here.

**Branko Kral:** Yeah.

**Branko Kral:** Yeah.

**Branko Kral:** Okay.

**Branko Kral:** Okay.

**Branko Kral:** Okay.

**Branko Kral:** That's getting good.

**Branko Kral:** So it's the some events that are working better.

**Branko Kral:** And that's the trial.

**Branko Kral:** So I guess we could look at a blog.

**Carmel Schetrit:** Yeah, you could filter it from there.

**Branko Kral:** Channel type equals do organic search.

**Branko Kral:** There we go.

**Branko Kral:** And then add another row for the filter.

**Branko Kral:** But that would be do page.

**Branko Kral:** Start typing page.

**Branko Kral:** Or a path.

**Carmel Schetrit:** I think that should be it.

**Branko Kral:** Do path name, please.








**Branko Kral:** Yeah, everything after the domain.

**Branko Kral:** Okay, so in the operator in the middle, instead of equals, try and see what's there.

**Branko Kral:** Do matches regex, please.

**Carmel Schetrit:** Okay.

**Branko Kral:** we'll do either, or do blog, and then the pipe character.

**Branko Kral:** So blog or glossary.

**Branko Kral:** So everything that contains either blog or glossary will be included now.

**Branko Kral:** And we have two conversions.

**Branko Kral:** This is the last 90 days, so not many.

**Carmel Schetrit:** And visitors down by 4% in the past 90 days.

**Carmel Schetrit:** And that compares you to the previous 90 days, right?

**Branko Kral:** No, compared to one week earlier, so we should change that.

**Carmel Schetrit:** Compared to previous period.

**Carmel Schetrit:** What's previous period, actually?

**Carmel Schetrit:** Would be previous 90 days, just previous whatever is defined in there.

**Carmel Schetrit:** Oops.

**Carmel Schetrit:** Okay, there we go.

**Carmel Schetrit:** That looks better.

**Carmel Schetrit:** But still two conversions.

**Carmel Schetrit:** Okay.

**Carmel Schetrit:** Yeah.

**Branko Kral:** And those are the next trial click.

**Branko Kral:** I wonder whether we have a conversion for the demos as well.

**Branko Kral:** And it looks like Postal lets you analyze for each one conversion only.

**Branko Kral:** So it is in actions.

**Carmel Schetrit:** Carmel, can you scroll down again?

**Jess Scott:** It's also a French blog as the top performer.

**Jess Scott:** Right?

**Carmel Schetrit:** Yeah.

**Carmel Schetrit:** What is build and run?

**Carmel Schetrit:** Build and run, like IT terms of how you build your actual infrastructure operations and then you run it.

**Jess Scott:** Translating what we're doing into French, right?

**Jess Scott:** No, this is what I built.

**Carmel Schetrit:** OG build and run.

**Carmel Schetrit:** Okay.

**Carmel Schetrit:** Cool, cool.

**Carmel Schetrit:** Yeah.

**Carmel Schetrit:** We'll

**Jess Scott:** Because a lot of these are the French blogs, so that's also worth noting.

**Branko Kral:** But hey, Kamal, we can add some more.

**Branko Kral:** I guess for demo and trial, it's the same.

**Carmel Schetrit:** Oh, I have nav trial clicked.

**Carmel Schetrit:** That's why.

**Carmel Schetrit:** So I should change it on the custom events.

**Carmel Schetrit:** Okay, we can just get rid of that for a second.

**Carmel Schetrit:** Add conversion goal demo.

**Carmel Schetrit:** Let's see.

**Carmel Schetrit:** I wonder what the difference is between custom events and actions.

**Branko Kral:** Oh, so this is not.

**Carmel Schetrit:** I have a feeling this isn't set up properly.

**Carmel Schetrit:** Because this doesn't show anything.

**Carmel Schetrit:** two conversions are only for the custom event, which is the click.

**Carmel Schetrit:** Let's see, for example.

**Carmel Schetrit:** Oh, no.

**Carmel Schetrit:** So it was from the navbar click trial.

**Carmel Schetrit:** But according to this, it didn't actually convert.

**Carmel Schetrit:** Conversion is just the nav trial conversion.

**Branko Kral:** In here, it's only the click, the click on the trial button, the try for free, which I wouldn't think there would only be two people who clicked it.

**Branko Kral:** if there are only two people who followed through and submitted the form all the way, that could be more believable.

**Carmel Schetrit:** But only two.

**Branko Kral:** And then when we don't see other events for the other conversions either, I think there's an issue here.

**Branko Kral:** Maybe there's something.

**Branko Kral:** Maybe there's too much filtering.

**Branko Kral:** Maybe there's something.

**Branko Kral:** Maybe the path cleaning is breaking it.

**Branko Kral:** I'll dig through it.

**Branko Kral:** So we're using time well.

**Branko Kral:** Once we get off the call, I'll stay in your data.

**Branko Kral:** I'll dig through it and see if I can find more.

**Branko Kral:** And

**Branko Kral:** And then to comment on what we were doing with reporting, we are trying to standardize our report across clients.

**Branko Kral:** Okay.

**Branko Kral:** We'll be in Looker.

**Branko Kral:** And so for now, we've been winging it, I have to admit.

**Branko Kral:** But yeah, there's a more standard report coming.

**Branko Kral:** We just want to make sure we get it right.

**Branko Kral:** And we want to make sure we have something that tells you enough about conversions as well.

**Branko Kral:** And it won't be super complicated, but we're also growing fast.

**Branko Kral:** We're experiencing some growing pains.

**Branko Kral:** So some things are taking us longer than they should.

**Branko Kral:** And we're trying to at least provide some value with calls like this or me, you know, getting into your tools and finding insights there in the interim.

**Branko Kral:** And then we can actually keep doing that because this is a pretty good exercise in getting to know everything better.

**Branko Kral:** But we want to have something similar to what your Google Ads reports show you, but actually maybe a little simpler.

**Branko Kral:** Yeah, it doesn't have to be so boring.

**Carmel Schetrit:** boring.

**Carmel Schetrit:** that hasn't have But hasn't But the

**Carmel Schetrit:** Some kind of funnel.

**Carmel Schetrit:** Yeah.

**Branko Kral:** Yeah, yeah, yeah.

**Branko Kral:** But I also ask Morris to do, if I were you, would be in the keywords and conversions on the second page.

**Branko Kral:** I would ask him to also group it by ad groups so that it's easier to, and I'll actually share this now.

**Branko Kral:** It'll be more telling if it's organized.

**Branko Kral:** just a little different.

**Branko Kral:** There you see that.

**Branko Kral:** Yeah, you see the tab.

**Branko Kral:** I actually needed a different one.

**Branko Kral:** Sorry.

**Branko Kral:** I'll do a new share.

**Branko Kral:** Oh, it looks like I can stop sharing.

**Branko Kral:** Okay, here we go.

**Branko Kral:** So when I do a longer period, let's do 90 days here, two or so.

**Branko Kral:** So how do you see it now?

**Branko Kral:** And

**Branko Kral:** It does look like conversions just started trickling in or stopped trickling in at some point during the last month or two, but before that they were coming in.

**Branko Kral:** So if I organize it, for instance, per click, I see it organized per campaign and the search keyword.

**Branko Kral:** And I'm not sure how exactly these campaigns are set up, but usually you also have ad groups where the keywords are grouped and then it's easier to analyze.

**Branko Kral:** So maybe what I should be considering the ad group is IT managed services and then there are multiple keywords that we're targeting.

**Branko Kral:** Yeah.

**Branko Kral:** So they would tell me something, but it could maybe be even better if there's another column with the ad groups if it's still set up that way.

**Branko Kral:** Okay.

**Branko Kral:** But yeah, but this just, if you haven't looked at this report a lot yet, then we can also stay on and we have another call today too where this is getting pretty useful for us.

**Branko Kral:** At least for the number of clicks.

**Branko Kral:** And I'm also looking at the click-through rates.

**Branko Kral:** So this confirms that the bottom funnel converts the highs, right?

**Branko Kral:** Because you have a lot of impressions for some other terms, actually, like IT services USA.

**Carmel Schetrit:** Yeah, the click-through is low and it's so top of funnel.

**Carmel Schetrit:** Yes, which is why I wanted us to shift our strategy for growthx to bottom of the funnel.

**Carmel Schetrit:** I did want to ask you, I know we don't have that much time left.

**Carmel Schetrit:** I wanted to also talk to you about what we should be doing with the content schema stuff.

**Carmel Schetrit:** Because I saw this week, so like two weeks ago, I think I wrote in the channel, we got our first trial from ChadGPT.

**Carmel Schetrit:** And ever since then, we've been tracking it on HubSpot.

**Carmel Schetrit:** And this week, we didn't get any conversions, but we saw nine...

**Carmel Schetrit:** Impressions, think it was, or nine sessions where Siit came up in ChatGPT, according to HubSpot.

**Carmel Schetrit:** What do you think we should be doing to better rank on, I guess it's Bing?

**Carmel Schetrit:** I don't know.

**Carmel Schetrit:** I know ChatGPT loves peer review sites, so I'm trying to get us up to speed on Gartner and G2 Crowd.

**Carmel Schetrit:** But for the schema markup stuff, I'm wondering what pages you think we should start with, other than what we have already, which is the pricing page and the FAQ section on the migration page.

**Branko Kral:** I would even do your product and service pages first, because that's where you want to funnel people, and of course the blog articles.

**Branko Kral:** But, you know, it's more of a technicality in my mind.

**Branko Kral:** You can have a side ranking on a search engine or...

**Branko Kral:** An answer engine or a generative engine without the schema, right?

**Branko Kral:** But you couldn't rank anywhere without having a good volume of high-quality content and also a lot of different sources mentioning you.

**Branko Kral:** that goes first, right?

**Branko Kral:** whatever you can do in distribution of your content, whether that's with the email that you started doing or the social posts for repurposing, or if you need to add something to your scope about repurposing more for you so it's faster, just getting it out to more places where it works well.

**Branko Kral:** You don't have to cover all the different social networks, but you want to focus on a few and go really strong on there.

**Branko Kral:** And definitely backlinks, like by the end of this month, you'll see a sample of what we could deliver or what you could be trying for.

**Branko Kral:** Or you could publish link magnets.

**Branko Kral:** You could publish a tool.

**Branko Kral:** You could publish a checker of stories.

**Branko Kral:** You could publish an audit tool of sorts.

**Branko Kral:** You could publish something interactive that people would...

**Branko Kral:** Linking to because it'll be an interactive resource.

**Branko Kral:** That's another one for having a link magnet.

**Branko Kral:** And I don't think it's actually changed so much compared to before.

**Branko Kral:** The behavior of users has, but I think getting the visibility has not changed as much.

**Branko Kral:** I think the biggest change is that now you want to become the source for one of two or three citations.

**Carmel Schetrit:** It just, I've been surprised that people found us these past few weeks on ChatGPT because before, if you, I mean, I've tried a few times to type in, like, what is Siit.io or something like that, and it couldn't find us at all.

**Branko Kral:** Yeah, well, now you've had more and more content published.

**Branko Kral:** That helps, too.

**Branko Kral:** One of the signals of that you are an authority on a topic is that you have a volume of content.

**Branko Kral:** Okay.

**Branko Kral:** So what we're building for is the foundation.

**Branko Kral:** Right now, we need to bring more eyeballs to it.

**Branko Kral:** We know what we...

**Branko Kral:** Traditionally do would be publish great content that's written for SEO, and then SEO is the distribution method.

**Branko Kral:** And organic traffic from Google has been the biggest traffic source for most sites.

**Branko Kral:** So that's the biggest distribution method.

**Branko Kral:** Now the other distribution methods and your brand matter more than before AI.

**Branko Kral:** But the foundation of content is still just as important, and it is giving you the visibility and the authority.

**Branko Kral:** That you need.

**Carmel Schetrit:** Okay.

**Branko Kral:** But then, yeah, of course you want to have the schema on there, but I would say continue.

**Branko Kral:** saying it's not the most important thing.

**Branko Kral:** Yeah, I would say the other authority signals are more important, because what does schema do for you, right?

**Branko Kral:** Schema makes it easier for the crawlers to understand your content.

**Carmel Schetrit:** Right.

**Branko Kral:** they understand it anyway.

**Branko Kral:** The schema just makes it easier.

**Branko Kral:** Especially with AI, they understand it anyway.

**Branko Kral:** The The schema started when...

**Branko Kral:** It was harder for search engines to parse out what your content is about.

**Branko Kral:** And a part of why it still lives is that sometimes you need your data to be structured like for Google Shopping ads.

**Branko Kral:** It's a very schematic markup as well for the feeds that you put into shopping ads and such.

**Branko Kral:** So it still has its purpose, but I don't think it's priority.

**Branko Kral:** think other authority signals are more important.

**Branko Kral:** Schema is not even an authority signal.

**Branko Kral:** It's just about the ease of understanding for the machines while your distribution, for instance, is.

**Branko Kral:** And then, you know, there's tools coming out for AI optimization where, you know, before we would have tools for search engine optimization.

**Carmel Schetrit:** I know I was tempted to, someone recommended some site or like some tool for AI optimization for your content on your website.

**Carmel Schetrit:** But I was like, how far down this rabbit hole can I go?

**Carmel Schetrit:** know.

**Carmel Schetrit:** I know.

**Branko Kral:** Yeah, I mean, if you used one, it could be good, and it'll probably be similar to an SEO optimization, you know, search engine optimization tool.

**Branko Kral:** But, yeah, focus on the...

**Branko Kral:** put it in your list of...

**Carmel Schetrit:** I mean, like, think about the fact that we're a seed-funded startup, and there's only so much marketing...

**Carmel Schetrit:** I mean, I'm the only full-time marketer, and there's only so much budget-slash-effort I can put into initiatives.

**Carmel Schetrit:** Do you think that that would be something that I should prioritize against, you know, a million other things?

**Branko Kral:** Yes, especially if it can be through partnerships with real people.

**Branko Kral:** If you can have other experts in the field talking about you, maybe...

**Carmel Schetrit:** I'm yes, but I mean, like, should I go to an agency to have them optimize our site for GPTs?

**Branko Kral:** No, no, I would focus on creating content and distributing it really well.

**Branko Kral:** And you can always optimize.

**Branko Kral:** The optimization is something that usually gives you something like, you know, a 10 to 20% boost in my experience.

**Branko Kral:** While if you want to go exponential, that's going to be either through content production or distribution or ideally both.

**Branko Kral:** I would even, if you're thinking budget allocation, I would maybe do it a half and half production and distribution for the optimal.

**Branko Kral:** Because I do believe that distribution is just as important as production, but not more.

**Branko Kral:** So whether that's the budget you put into content repurposing for social posts or for paying someone who's really good at creating those posts, maybe a LinkedIn person, maybe a Reddit person, that would be something else to consider before the technical.

**Branko Kral:** And what I think is also that how exactly to optimize for AI is going to be changing quite a bit.

**Branko Kral:** You know, you if you want to go do stuff similar to an.

**Branko Kral:** Your meta title and meta description and internal links and such.

**Branko Kral:** I think all of those qualities will still matter because even AI tools take from search engines and they scrape search engine result pages, whether that's Bing or Google and usually both.

**Branko Kral:** So I would keep optimizing for SEO, keep producing content and maybe do more for distribution, especially through partnerships with people with faces.

**Branko Kral:** Okay.

**Carmel Schetrit:** Okay.

**Carmel Schetrit:** That's good input.

**Carmel Schetrit:** I'm talking to someone who can help us get more visibility on Reddit and potentially invest in there.

**Carmel Schetrit:** So that helps on the distribution part.

**Carmel Schetrit:** Yeah.

**Branko Kral:** And we'll just keep working on serving up the content that you can use for all that.

**Branko Kral:** Because, you know, the

**Branko Kral:** The blog or the glossary, I think the glossary especially can be link magnets.

**Branko Kral:** know, when people link to something that's a resource because it explains something really well, that could be something worth citing or linking to.

**Branko Kral:** Especially your full glossary collection could be like, okay, you are looking into ITSM, use this as your dictionary.

**Branko Kral:** I can see people wanting to link to that.

**Branko Kral:** There's also something that should be fairly easy down the line for us to get your links to.

**Branko Kral:** And then the repurposing will be huge because the blog is like the hub, right?

**Branko Kral:** Like you can take one article and slice it up into, as you would know, five or ten sometimes social posts.

**Branko Kral:** Yeah.

**Branko Kral:** And that will get you more value for the money you're paying us.

**Branko Kral:** We love value.

**Carmel Schetrit:** And conversions.

**Branko Kral:** And conversions.

**Branko Kral:** We love conversions more.

**Branko Kral:** So after this now, since we're on time, I'm going to pause the hog.

**Carmel Schetrit:** And me know if you need me to share any info from the HubSpot side of things.

**Carmel Schetrit:** I'm happy to dig around in there as well.

**Carmel Schetrit:** Cool.

**Carmel Schetrit:** That'll be the next step.

**Branko Kral:** I'll start here.

**Branko Kral:** Because then HubSpot data might not have enough data about what happened on the website for the lead.

**Branko Kral:** It depends.

**Branko Kral:** Maybe it does, but it depends on what integrations you have and which tier and all that.

**Branko Kral:** But I'll start.

**Branko Kral:** Hopefully I'll find more.

**Branko Kral:** I'll record a loom about GA and postdoc and also about some conclusions we can make from the Google Ads data.

**Branko Kral:** And I'll make it so that it's for both of you, Carmel and Jess.

**Branko Kral:** So we can all use it for content decisions.

**Branko Kral:** And I think it'll be just, I don't know, five to 10 minutes.

**Branko Kral:** Because the digging around will probably take more than just showing you.

**Branko Kral:** Hopefully I can just show you a few charts and tell you a few things.

**Branko Kral:** And then we can make that.

**Branko Kral:** We were routine, and then they'll inform the reporting we are going to build for you as well, or just the routine we have for reporting.

**Branko Kral:** Maybe we do like a monthly thing, right?

**Branko Kral:** Sometimes looking week by week.

**Carmel Schetrit:** Yeah, can be a little too granular.

**Carmel Schetrit:** think monthly is fine too.

**Carmel Schetrit:** Yeah, yeah.

**Branko Kral:** Sometimes it can even be too tempting and too deceiving to look too often, like when you look at your account and it can tempt you to make decisions too early, but monthly at least.

**Carmel Schetrit:** Okay.

**Carmel Schetrit:** Sounds like a plan.

**Carmel Schetrit:** Cool.

**Carmel Schetrit:** Thanks so much.

**Branko Kral:** Yeah, yeah.

**Branko Kral:** See you tomorrow.

**Carmel Schetrit:** Yeah.

**Carmel Schetrit:** Bye.

**Carmel Schetrit:** Thanks.

**Jess Scott:** Bye.

**Jess Scott:** Bye.

**Jess Scott:** Bye.

**Jess Scott:** Bye.
