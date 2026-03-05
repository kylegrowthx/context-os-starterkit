# Yourco <> GrowthX Weekly Sync

<metadata>
date: 2025-03-12
time: 15:34 UTC
duration: 28 minutes
organizer: kyle@growthxlabs.com
participants: Jessica Yip (Yourco), Kyle Gaudreau (GrowthX), Sadira Sittampalam (GrowthX)
fathom_recording_id: 51508279
fathom_url: https://fathom.video/calls/250659351
share_url: https://fathom.video/share/CSkyEptJV2dNo7KCvXEgsFznm22rA6C2
source: fathom
enriched_on: 2025-03-04 18:30 UTC
</metadata>

---

## Summary

Yourco and GrowthX aligned on fixing UTM tracking issues and optimizing Yourco's analytics setup, with Kyle recommending Google Tag Manager event tracking instead of internal link UTMs to preserve accurate channel attribution. The team reviewed recent traffic patterns, noting that a refreshed translation cost article spiked temporarily before normalizing, and agreed to focus on consistent publishing of achievable, lower-volume keyword targets across new content clusters (enterprise, personal cell phone use, legal text messaging) and expanding translation-focused content to align with Yourco's multilingual team positioning. Jessica flagged potential keyword cannibalization between two non-desk employee communication articles, and the team committed to reviewing overlapping content and providing additional examples to Sadira for analysis.

---

## Context

Yourco is an external client working with GrowthX on content marketing and SEO strategy. This weekly sync is a recurring touchpoint between Yourco's content team (Jessica Yip) and GrowthX's SEO/strategy team (Kyle Gaudreau and Sadira Sittampalam) to track content performance, discuss technical implementation, and align on next steps. The engagement appears focused on content performance optimization, technical SEO (UTM tracking, GA4 access, CTR optimization), and keyword strategy including cannibalization avoidance.

---

## Relevance

**To GrowthX Delivery:**
- Identified critical UTM tracking mistake on internal links causing self-referring sessions and lost channel attribution data. Kyle shared best-practice recommendation to use Google Tag Manager event tracking instead (taxonomy: CTA button click > asset type > specific asset name). This is a common analytics implementation error that affects data accuracy.
- Discussed GA4 limitations vs. HubSpot for tracking and attribution, flagging that GA4 lacks page-level conversion path visibility — client considering HubSpot as supplementary tracking tool.
- Content cluster analysis framework: Yourco planning to present refreshed vs. new article performance by cluster in Looker Studio; Sadira to receive updated metrics by next week.

**To GrowthX Business Development:**
- Content refresh strategy is working: refreshed articles on translation costs spiked impressions/clicks, showing traction. Traffic normalized after initial spike, which Kyle noted as common Google experimentation pattern.
- Client is confident about three near-term topic clusters (enterprise-related, personal cell phone use, legal text messaging) and planning focused publishing to drive consistent growth rather than "home run" content bets.
- Potential upsell/expansion opportunity: translation/multilingual content cluster aligns with Yourco's ICP (multilingual teams). Jessica proposing multiple articles under this cluster with internal linking strategy to help Google rank Yourco higher.

**To CheckThat:**
- No direct mentions, but the discussion of GA4 limitations for conversion attribution and exploration of alternative tracking methods (HubSpot, event-based) reflects broader industry shift in analytics that CheckThat visibility work could inform.

---

## Overview

- UTM tracking on internal links can disrupt GA data; event tracking via GTM recommended instead
- Recent traffic spike from translation-related content normalized; focus on consistent growth and user engagement
- Potential keyword cannibalization identified; team to review and optimize overlapping content
- Experimenting with longer meta titles may improve CTR, but requires careful monitoring

---

## Key Topics

### UTM Tracking and Analytics Implementation

  - UTM parameters on internal links create self-referring sessions, disrupting Google Analytics data and overwriting original referrer information
  - Recommended solution: Use event tracking via Google Tag Manager for internal link clicks with a taxonomy approach (e.g., "CTA button click" > "white paper" > "specific white paper name")
  - Jessica to investigate GTM implementation for tracking banner and resource page interactions
  - Team to consider leveraging HubSpot for additional tracking capabilities and conversion path visibility beyond GA4

### Content Performance and SEO Strategy

  - Overall performance for refreshed content doubled; slight drop in new article performance (4 published last week)
  - One refreshed article on translation costs saw temporary spike in impressions/clicks, now normalizing (typical Google experimentation pattern)
  - Strategy for maintaining growth:
      - Focus on consistent publishing of new content
      - Improve user experience (CTAs, images)
      - Target achievable, lower-volume topics for steady momentum ("singles and doubles rather than home runs")
  - Planned content clusters: enterprise-related, personal cell phone use, legal text messaging
  - Explore expanding translation-related content to align with Yourco's multilingual team focus

### Keyword Cannibalization

  - Potential issue identified with two articles on non-desk employee communications: "Successful non-desk employee communications" and "Communication reaching non-desk employees"
  - Both articles ranking for overlapping keywords; one is a pillar article, the other is supporting content
  - Team to review and consider:
      - Expanding content to differentiate topics and target unique queries
      - Refreshing content to focus on unique aspects
      - Possibly redirecting one article to the other
  - Jessica to send list of other potentially cannibalizing articles for Sadira's review

### Meta Titles and URLs

  - Discussed optimizing meta titles (target ~70 characters) vs. emerging evidence that longer titles may improve CTR
  - Agreed to experiment with shorter titles while monitoring performance
  - Will adjust titles only, not URLs, to avoid unnecessary SEO friction and preserve accumulated domain authority

---

## Action Items

**Jessica Yip (Yourco)**
- Investigate using Google Tag Manager for event tracking instead of UTMs
- Check and provide GA4 access to Sadira
- Send list of articles with potential keyword cannibalization to Sadira

**Sadira Sittampalam (GrowthX)**
- Investigate keyword cannibalization for non-desk employee communication articles
- Review list of potentially cannibalizing articles provided by Jessica

---

## Transcript

**Jessica Yip:** or contact sales or private fee, then we will add two more add value like the white paper download and also like subscribe to our e-newsletter and then we'll send you you know upload the library so then you can just use it and then for the link we'll provide you the link clicked.

**Kyle Gaudreau:** Just to clarify on that part Jessica, when you say track on the link what particularly are you adding to the link?

**Kyle Gaudreau:** Oh it's just the UTM.

**Jessica Yip:** Yeah we should be careful with that.

**Kyle Gaudreau:** You can at some point do some workarounds with UTM but this is actually like a common mistake that I've seen over the years and me asking essentially what I've seen and you know, correct me if I'm thinking about this in the wrong way, but if you append on it a link that from someone that's already on your website and you append, say, source data such as like UTM source, UTM medium, when they click that link, it actually will kind of mess up Google Analytics and other tracking sources because it will then be read as a new referrer essentially.

**Kyle Gaudreau:** So it creates what's kind of called like a self referring session.

**Kyle Gaudreau:** Your website would be the referrer and it would drop the original referrer data.

**Kyle Gaudreau:** So meaning like you would struggle to accurately see, you know, if it was paid, organic, direct, wherever it actually came from, it would get overwritten essentially.

**Jessica Yip:** So what you're saying is basically like on our website, we would let the Google Analytics do the job.

**Jessica Yip:** And so then it's stick to the so they can able to identify the sources come from our website and that we can just look at the link click link by clicking and impressions of that specific link.

**Kyle Gaudreau:** Yeah, so there's a lot of ways to solving this.

**Kyle Gaudreau:** And I'm happy to, if you want to do a session where we just, particularly, at what you're trying to track, I've spent so much time doing this over the years on the web.

**Kyle Gaudreau:** But I'm happy to help work with that.

**Kyle Gaudreau:** So there's a few different things here, right?

**Kyle Gaudreau:** So how you handle refer data, and ultimately, I imagine you're trying to get this into your CRM, right?

**Kyle Gaudreau:** Not just Google it, because you're trying to get the refer data into the CRM.

**Kyle Gaudreau:** I mean, so I just want to have one objective.

**Jessica Yip:** The reason why I want to install UTM is I know that how many people click on this link on this banner, so how interactive and how engaging the banners are, so that we can do, like, maybe this banner works better, or this white paper, actually a lot more people click on it.

**Jessica Yip:** So then we have more data.

**Jessica Yip:** Otherwise, it was just right on, you know, the, let's say we, you know, to white paper, we don't know this white paper is like direct or come through the blog.

**Jessica Yip:** So there's no way that we can track, right?

**Kyle Gaudreau:** I didn't mean to cut you off. Yeah, go ahead.

**Kyle Gaudreau:** Not necessarily.

**Kyle Gaudreau:** It depends on what answers you're trying to get and where.

**Kyle Gaudreau:** You know, constraining this to Google Analytics specifically, the typical recommendation I would do in that case. Um, and as good even if you were, there's other things related to like tracking this in the round we could always talk about later, but is event tracking to the links.

**Kyle Gaudreau:** And so then coming up with essentially a taxonomy of, like, this can happen in different ways, right, like, there's different layers and events, and so, like, you could say, like, one broad bucket is, like, click the CTA button, and, like, so then you can see that in Google Analytics, and you can see all the CTA button clicks and where they're, and then as you double click into that, you can see the particular thing, and there are different ways of organizing, right, you could call that the white paper name, you could call that a white paper, usually there's three layers you can, if I recall correctly, you can add to this, so you could say, like, CTA button click, white paper, the particular white paper, and so it's use Google Tag Manager.

**Kyle Gaudreau:** Yeah, I do.

**Kyle Gaudreau:** It's pretty easy to do in Google Tag Manager nowadays, and so that's the most ideal because that's essentially how GA is, like, purpose-built to track kind of stuff is based off the events, and that's how they track a lot of the conversion data nowadays, too.

**Kyle Gaudreau:** Um, and so in this case, it's not a true conversion.

**Kyle Gaudreau:** You're just tracking behavior to a conversion.

**Kyle Gaudreau:** Yeah, that would be the most ideal because else, if you do it with UTMs, yeah, you're just going to start, like your data is going to start looking really weird and confusing.

**Kyle Gaudreau:** Uh, this is one that's like super, super common, like almost every stop of, you know, my in-house career when I would join in audit analytics almost every time my book kept something like this.

**Kyle Gaudreau:** So it's super common misconception.

**Jessica Yip:** Got it. Okay.

**Jessica Yip:** Let me look into it then.

**Jessica Yip:** Yeah, happy to share any detail.

**Kyle Gaudreau:** Um, but it's pretty easy to add for GT.

**Jessica Yip:** Yeah, we actually do have event conversions for all the call to actions, the three, but just looking to, like, is it able to where these call to action come from in which pages was the, you know, like the curve converting path.

**Jessica Yip:** I know in Google, there's a solutions path, but it's more based on channel.

**Jessica Yip:** It doesn't tell you which page that they go to.

**Kyle Gaudreau:** I mean, this is the problem nowadays with Google Analytics, GA4 specifically.

**Kyle Gaudreau:** It's not great.

**Kyle Gaudreau:** We actually stopped using it at home based on my previous stuff, like it was still on our website, but we barely used it for any of our reporting.

**Kyle Gaudreau:** But yeah, I think depending on the questions you're trying to answer, there's things you can do to make that easier to answer in GA4, but also you may want to consider, do you remember now, use HubSpot?

**Jessica Yip:** Yeah, we use HubSpot.

**Kyle Gaudreau:** Like some of those same questions that you have, we could theoretically do in HubSpot as well.

**Kyle Gaudreau:** But anyways, if it's helpful, yeah, I've been using UTM for GA4 and it has worked well in the past so I haven't seen any ref flags like how you mentioned it but definitely we'll look into it more.

**Jessica Yip:** Yeah yeah the last thing I'll just say on that it's not surprised because it actually can fly under the radar it's like you'd have to like segment your data in specific ways to find it but it did again the big challenges if like you won't get the accurate pulse on what your channels are doing yeah that's it and that's you know one of the key parts of what GA is trying to do but anyway sorry didn't want to be real less on that but that's got my attention to the here so is there anything else you want?

**Sadira Sittampalam:** Yeah yeah yeah there was also one article it was a resource page. I'm not really sure how to upload the image on that page like I don't know what type of slice to use because any of the options I had was just for text.

**Jessica Yip:** So if you could just double check on that and let me know how I can upload it to that page, that would be great.

**Sadira Sittampalam:** Yeah, I think, yeah, let me look into it.

**Jessica Yip:** I think for resources, the way we build it, there is no, actually, you can just track it.

**Jessica Yip:** Actually, I tried it last week because we're going to put banners in there, so I will do an example for you and send a link over after the call.

**Sadira Sittampalam:** All right, cool.

**Jessica Yip:** And yeah, going on to the performance.

**Jessica Yip:** I'm looking at the air table, you mentioned about the enterprise.

**Sadira Sittampalam:** They are considering in the cluster enterprise related.

**Sadira Sittampalam:** There should be around 30 words, I think.

**Jessica Yip:** Okay, so it's a status cluster that are to review.

**Jessica Yip:** It's under constraint.

**Sadira Sittampalam:** If you scroll up just a bit, Kyle, so yeah, there's like total performance for the refreshes, which has doubled from last week, and that's probably because we started focusing a bit more on refreshes, so we put six out, I think, last week, because there was some play in the flow before that, and we went on to the new articles, we're seeing a little bit of a drop, and we think this is also because we only published four new articles last week anyway, so that kind of makes up for and you also mentioned we would do like a cluster based analysis, for this we're going to be moving into Looker Studio to present all this data, but we'll have that right for you by next week.

**Sadira Sittampalam:** I also wanted to ask whether you could give us access to GA4, even though Kyle just mentioned it's unreliable, where I'm still going to probably use it for their reporting a little bit.

**Sadira Sittampalam:** But yeah.

**Jessica Yip:** I thought we had access to their GA4, but I could not remember that.

**Jessica Yip:** I think I don't think we're going to do that as access.

**Jessica Yip:** Yeah, I see it.

**Kyle Gaudreau:** Oh, I was looking for it, didn't show.

**Jessica Yip:** Yes, it's really weird.

**Kyle Gaudreau:** This actually happened to me as well.

**Kyle Gaudreau:** There is sometimes the view you're initially shown will cut off some accounts.

**Kyle Gaudreau:** I don't know why, but that did happen to me last where I didn't think I had access to their GA4 because it starts with why it's at the bottom of list.

**Kyle Gaudreau:** You might go back and then I'll show you the full list.

**Sadira Sittampalam:** I'll double check on that.

**Jessica Yip:** But yeah.

**Sadira Sittampalam:** I think that's all the updates we have.

**Sadira Sittampalam:** Do you have any questions?

**Kyle Gaudreau:** Yeah, you said you prepare a report in Looker.

**Jessica Yip:** And what kind of data point are you going to put into or investigate the drop?

**Jessica Yip:** I see on GA and also SEM right that impressions and click has dropped like 30 days compared to 30 days period.

**Sadira Sittampalam:** I think that is most because there was like one article of yours that we did that we refreshed and it got like a lot of impressions and clicks.

**Sadira Sittampalam:** I think now that is like fizzling out so the entire site is going down.

**Jessica Yip:** Why is the all of a sudden there is a search and click in that one article?

**Jessica Yip:** Like I said, we refreshed it I think a month ago.

**Sadira Sittampalam:** Or a few like very early on, it was something about translation costs, like a bunch multi will stand up, but I could be too long, but I think that was easy.

**Kyle Gaudreau:** So what you're saying is it spiked for like a short period of time and kind of was up but kind of normalized and came down?

**Sadira Sittampalam:** Yeah.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** From what I saw.

**Sadira Sittampalam:** We can clarify that.

**Kyle Gaudreau:** That's actually like a pretty common pattern.

**Kyle Gaudreau:** Like sometimes like Google's giving you a little bit of traction, it's trying to see how almost kind of like experimenting how you'll do with some of those queries and it's not unusual for that happen.

**Kyle Gaudreau:** So when that does happen, we typically want to like go back and see if we can optimize to some of what it was getting at.

**Kyle Gaudreau:** Yeah, I'm seeing that page now.

**Sadira Sittampalam:** It's, yeah, let me share the screen on that one.

**Kyle Gaudreau:** Okay, should be seeing GSC.

**Kyle Gaudreau:** So we had a bit of a spike for like a week and then it's kind of come down to what it was before.

**Kyle Gaudreau:** So here, this is day range.

**Kyle Gaudreau:** I want the state range to come up my rail, I have 17th.

**Kyle Gaudreau:** So we say, trying to see like a quick before and after the drop, this might not be perfect.

**Kyle Gaudreau:** I don't have to go farther, translation, it's translation, translation, prices.

**Kyle Gaudreau:** How much does a translator cost?

**Kyle Gaudreau:** I think that what I'm at least seeing by quick glance of what we were getting some impressions and clicks from, it's just very broad in terms of intent.

**Kyle Gaudreau:** So while we were able to show some traction, I would say we would probably, I mean, if we can consistently rank for this stuff, amazing, but it is quite broad in terms of intent from like an ERCO standpoint.

**Kyle Gaudreau:** If it had some sort of modifier that was closer to ERCO, I think we'd have a bit more traction.

**Kyle Gaudreau:** This wouldn't, based off the queries I'm seeing, this having a little bit of that up and down wouldn't necessarily surprise me.

**Kyle Gaudreau:** Right, I'm just looking at the by-ending page.

**Jessica Yip:** I don't see there's a big change in terms of traffic to the particular block, like, if we're talking about what is typical cost.

**Jessica Yip:** The professional translation services, if that is the article, I don't see a search and traffic in that page.

**Jessica Yip:** But I do see...

**Kyle Gaudreau:** Well, if we look, I mean, the view we were just looking at before this conversation shows it, right?

**Kyle Gaudreau:** So, like, if we look over time, you know, this is the spike, right?

**Kyle Gaudreau:** So, it's not a huge spike to be clear.

**Kyle Gaudreau:** It's not going to jump off the page when you're looking at old data.

**Kyle Gaudreau:** But, yeah, it's typically around like a few clicks a week.

**Kyle Gaudreau:** I mean, given this isn't a massive number, it's almost 20, but that's a little bit of the up and down.

**Kyle Gaudreau:** But in general, though, yeah, seeing some of those impressions up to the previous view we were looking at, let me get back to it.

**Kyle Gaudreau:** Switching between sharing on Google Meet, it's not very, yeah, especially when it's on different profiles, it's quite annoying.

**Kyle Gaudreau:** You know, we're at what, 60 here, 40 there.

**Kyle Gaudreau:** So that is actually, like, Sadira's point that it was roughly in the ballpark of a drop of 20, that it's kind of contributing.

**Kyle Gaudreau:** In general, like, we don't, we want to be seeing consistent up and to the right in terms of impressions and click growth, so certainly, I would say, like, continuing the momentum on publishing new is our most ideal, and then anything we can do that further, just improve user experience, the CTA's can be a part of it, uploading images can be part of it, just that they can help ensure people stay engaged, that would be my other kind of area of recommendation of focus.

**Kyle Gaudreau:** Outside of that, you know, I would say just like, making sure we have some good, like, you know, some good bets in terms of what we're going to do next in terms of topics.

**Kyle Gaudreau:** You know we talked about, you know, a few that we want to focus on next.

**Kyle Gaudreau:** What I think about when I see a trend like this is, like, instead of, you know, just going for, like, bigger swing type things, like, go for some things that, like, we're confident we can rank well on, and, and generate momentum even though it's like lower volume just to keep, like, positive growth going.

**Kyle Gaudreau:** And, you know, so I would, I would make sure we take a look at, like, what we are all lining on in terms of next steps in terms of topics to try to keep that momentum.

**Kyle Gaudreau:** It's kind of like using a sports analogy.

**Kyle Gaudreau:** It's like trying to, you know, get some singles and doubles rather than swinging for some home runs.

**Kyle Gaudreau:** So, you know, that would be typically what we'd want to do in a case like this.

**Jessica Yip:** Yeah, I think in terms of topic, we're quite confident for that.

**Jessica Yip:** Enterprise one and also like the personal cell phone or like um is text um legal those clusters we're quite confident that will drive quite bit of traffic but I think it would quite a bit more review from our side to make sure the position is correct um yeah and then like half of the content will be more of the water terms where we bring the impression up and just see early signal so we're pretty aligned on the topics going forward and these like uh yeah these two months okay cool yeah another thing that I was thinking about like if translation there's um a search in the volume and we want to continue to optimize the article translation this topic is actually very fitting to um our prospect and ICP because we do a lot of the workforce like multilingual team so even build a search inquiry to tend to broaden.

**Jessica Yip:** One thing that I was thinking about, like we can continue to maybe run a couple more articles that it's more closer to intent, like how do you manage?

**Jessica Yip:** I think we do also have a couple articles about multi-lingual teams, based on the search inquiry, maybe we can bring some, have two to three articles just to hopefully Google will help us to rank higher if we publish articles under that cluster.

**Kyle Gaudreau:** Agreed.

**Kyle Gaudreau:** And then similarly, making sure we're finding opportunities to, you mentioned some of the things you already have related to that content, like I know we create internal links as a part of our blogs that we're generating, but additionally we write those new translation angles you were talking about, looking at those existing internal linking into them as well and just continue to show that kind of like, you know, at a cluster relevance.

**Kyle Gaudreau:** So I think it's absolutely worth exploring.

**Kyle Gaudreau:** You know I do recall you mentioned on the early days that angle of translation.

**Kyle Gaudreau:** So I think we can find the right angle modifier on the searches, et cetera, that gets it just a slight bit closer at how cool it sounds worthwhile.

**Jessica Yip:** Yep.

**Jessica Yip:** And I think two things that I want to ask is keyword cannibalization.

**Jessica Yip:** As I was looking at the blocks that ranked pretty well, we, there's two articles that might potentially competing each other is no one desk.

**Jessica Yip:** Okay, let me share with you guys this two links.

**Jessica Yip:** Basically is successful non-desk employee communications and the communication reaching non-desk employees.

**Jessica Yip:** So I see that they both ranking the same keywords.

**Jessica Yip:** Competing.

**Kyle Gaudreau:** So in this case, what is the best practice to, because one is a pillar article, the other one is just supporting law?

**Kyle Gaudreau:** Yeah, so it depends to a degree of like, on a few different factors.

**Kyle Gaudreau:** Does one of them have more traction on a particular set of words and does that align with what you want to see and how you want to map intent on the website?

**Kyle Gaudreau:** Because those are, I was just checking up pages, you know, slightly different files of pages, right?

**Kyle Gaudreau:** One being in the resources, the other as well.

**Kyle Gaudreau:** So if there is something there, like where you want to essentially map that and push that ideally, you know, that's one angle to consider.

**Kyle Gaudreau:** If they are just like truly like, if most of the queries are the same across both of them, and one of them just does, you feel a better job of landing the intent based off what you know from like a qualitative perspective, we should probably explore starting to refresh the other one.

**Kyle Gaudreau:** Sometimes what can happen in this case is you'll have one to three pieces or something like that, while they have a lot of overlap, one of them still has some queries that are a little bit unique to that.

**Kyle Gaudreau:** So you can start to refresh that piece to focus more on those that are truly unique to that, and then take some of that content that maybe could be additive to the other piece and start to move it over there.

**Kyle Gaudreau:** There's lot of other flavors of this.

**Kyle Gaudreau:** We could also consider just killing one of the pieces and redirecting it to the other, but there's not necessarily just one specific playbook like we have to consider like a few different figures so we can dig into it look at like you know which queries are overlapping how we'd want to map that and and and make a recommendation um but uh yeah I think it's something definitely we should be exploring as long as as long as it's truly like you know um sometimes you might see some queries pop up and it's not a huge deal because it's like so long but if they are really starting to like if this isn't setting us up for success we should consider yeah I think there will be some of you guys can look into like I think I would go for the approach where we extend the key work so then it's not much overlapping because if you look at the title it's very it's basically going to the same cluster um right yeah so for the I would say resources would be the the first to rank non the sample ecommunication and the we can expand the content a little bit out, so then it's not competing.

**Jessica Yip:** Yeah, I see a couple of articles like that.

**Jessica Yip:** It's not a main concern, but something that I think we should start looking into it, especially for the really good performing articles.

**Kyle Gaudreau:** Yeah, I agree.

**Jessica Yip:** Yes, Eric, we just make that action item for us to take into and just if we can find anything else as well?

**Sadira Sittampalam:** If you have any, if you have a list of articles that you've already got, send them over.

**Jessica Yip:** Sure.

**Sadira Sittampalam:** Great.

**Jessica Yip:** Another thing is for long title text, and I, as I'm also looking at these articles, these tend to have long links, URL.

**Jessica Yip:** You suggest us to, like, trim it down and...

**Kyle Gaudreau:** You know, it's fine.

**Kyle Gaudreau:** Just do it.

**Kyle Gaudreau:** I've been seeing this one pop up recently in my LinkedIn feed and people have been experimenting around this.

**Kyle Gaudreau:** Historically, the recommendation is keeping to a very specific character length.

**Kyle Gaudreau:** I'm not spacing out what the number is.

**Kyle Gaudreau:** It's like 70.

**Jessica Yip:** Okay, I didn't know it.

**Kyle Gaudreau:** Should have trusted myself.

**Kyle Gaudreau:** But I've actually been seeing people like experiment and challenge with that because they've been finding that rule is still showing longer character lengths and they were getting higher click-through rates.

**Kyle Gaudreau:** Admittedly, I haven't started to like validate that across the board, but I haven't, I've seen it multiple times now in the past few months with different people talking about this.

**Kyle Gaudreau:** So generally, I would say yes, going with 70, typically some of the ways I would do that, like by quick glance, like at least picking out the pipe in your code.

**Kyle Gaudreau:** If you can fit that in great, but I typically index more towards landing the message.

**Kyle Gaudreau:** But what applications are safe for?

**Kyle Gaudreau:** Use for business-related communication.

**Kyle Gaudreau:** We can probably have a shorter version of that.

**Kyle Gaudreau:** Yeah.

**Jessica Yip:** Yeah.

**Jessica Yip:** We definitely can shorten it.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Like, like if we just said, you know, safe to you, and anyways, just moving those words around and cutting it somehow, yeah, no, worth checking out.

**Kyle Gaudreau:** But yeah, anything we do that we would change on these, I would want to just like check back on the quickly roots.

**Kyle Gaudreau:** So a little while later.

**Jessica Yip:** Yeah.

**Jessica Yip:** So it's so good to try it, you know, to experiment whether it's, and then when we change the URL, then we make sure that it's transferable, right?

**Jessica Yip:** Like the SEO score that being built in this link can transfer to the other one.

**Kyle Gaudreau:** Oh, in this case, I would advocate for not changing the URL, just the title.

**Jessica Yip:** Just the title.

**Kyle Gaudreau:** Yeah.

**Jessica Yip:** Yeah.

**Jessica Yip:** And then not to say there aren't times.

**Kyle Gaudreau:** That makes sense.

**Kyle Gaudreau:** It's just like, I think we'd create unnecessary friction from a SEO standpoint, if we did that.

**Jessica Yip:** On it.

**Kyle Gaudreau:** Yeah.

**Jessica Yip:** Yeah, I think we will dig into the cannibalization.

**Jessica Yip:** Anything else comes up trying wise, let me know.

**Kyle Gaudreau:** Happy to help wherever I can.

**Jessica Yip:** Cool.

**Jessica Yip:** Awesome.

**Jessica Yip:** Appreciate the time, Jessica.

**Kyle Gaudreau:** Thank you, Kyle.

**Jessica Yip:** It's enduro.

**Jessica Yip:** Alright.

**Jessica Yip:** You.

**Sadira Sittampalam:** See you.

---

## Overview

- UTM tracking on internal links can disrupt GA data; event tracking via GTM recommended instead
- Recent traffic spike from translation-related content normalized; focus on consistent growth and user engagement
- Potential keyword cannibalization identified; team to review and optimize overlapping content
- Experimenting with longer meta titles may improve CTR, but requires careful monitoring

---

## Key Topics

### UTM Tracking and Analytics Implementation

  - UTM parameters on internal links can create self-referring sessions, disrupting Google Analytics data
  - Recommended solution: Use event tracking via Google Tag Manager for internal link clicks
      - Create a taxonomy: e.g., "CTA button click" \> "white paper" \> "specific white paper name"
  - Jessica to investigate GTM implementation for tracking banner and resource page interactions
  - Team to consider leveraging HubSpot for additional tracking capabilities

### Content Performance and SEO Strategy

  - Overall performance for refreshed content doubled; slight drop in new article performance (4 published last week)
  - One refreshed article on translation costs saw temporary spike in impressions/clicks, now normalizing
  - Strategy for maintaining growth:
      - Focus on consistent publishing of new content
      - Improve user experience (CTAs, images)
      - Target achievable, lower-volume topics for steady momentum
  - Planned content clusters: enterprise-related, personal cell phone use, legal text messaging
  - Explore expanding translation-related content to align with Yourco's multilingual team focus

### Keyword Cannibalization

  - Potential issue identified with two articles on non-desk employee communications
  - Team to review and consider:
      - Expanding content to differentiate topics
      - Refreshing content to focus on unique queries
      - Possibly redirecting one article to the other
  - Jessica to send list of other potentially cannibalizing articles for review

### Meta Titles and URLs

  - Discussed optimizing long meta titles (aim for \~70 characters)
  - Recent industry discussions suggest longer titles may improve CTR in some cases
  - Agreed to experiment with shorter titles while monitoring performance
  - Will adjust titles only, not URLs, to avoid unnecessary SEO friction

---

## Action Items

**Jessica Yip**
- Investigate using Google Tag Manager for event tracking instead of UTMs
- Check and provide GA4 access to Sadira
- Send list of articles with potential keyword cannibalization to Sadira

**Sadira Sittampalam**
- Investigate keyword cannibalization for non-desk employee communication articles

---

## Transcript
**Jessica Yip:** or contact sales or private fee, then we will add two more add value like the white paper download and also like subscribe to our e-newsletter and then we'll send you you know upload the library so then you can just use it and then for the link we'll provide you the link clicked.

**Kyle Gaudreau:** Just to clarify on that part Jessica, when you say track on the link what particularly are you adding to the link?

**Kyle Gaudreau:** Oh it's just the UTM.

**Jessica Yip:** Yeah we should be careful with that.

**Kyle Gaudreau:** You can at some point do some workarounds with UTM but this is actually like a common mistake that I've seen over the years and me asking essentially what I've seen and

**Kyle Gaudreau:** you know, correct me if I'm thinking about this in the wrong way, but if you append on it a link that from someone that's already on your website and you append, say, source data such as like UTM source, UTM median, when they click that link, it actually will kind of mess up Google Analytics and other tracking sources because it will then be read as a new referrer essentially.

**Kyle Gaudreau:** So it creates what's kind of called like a self referring session.

**Kyle Gaudreau:** your website would be the referrer and it would drop the original referrer data.

**Kyle Gaudreau:** So meaning like you would struggle to accurately see, you know, if it was paid, organic, direct, wherever it actually came from, it would get overwritten essentially.

**Jessica Yip:** So what you're saying is basically like on our website, we would let the Google Analytics do the job.

**Jessica Yip:** And so then it's stick to the so they can able to identify the sources come from our website and that we can.

**Jessica Yip:** just look at the link, click link, by clicking and impressions of that specific link.

**Jessica Yip:** Yeah, so there's a lot of ways to solving this.

**Kyle Gaudreau:** And I'm happy to, if you want to do a session where we just, particularly, at what you're trying to track where, I've spent so much time doing this over the years on the web.

**Kyle Gaudreau:** But I'm happy to help work with that.

**Kyle Gaudreau:** So there's a few different things here, right?

**Kyle Gaudreau:** So how you handle refer data, and ultimately, I imagine you're trying to get this into your CRM, right?

**Kyle Gaudreau:** not just Google it, because you're trying to get the refer data into the CRM.

**Kyle Gaudreau:** I mean, so I just want to have one objective.

**Jessica Yip:** The reason why I want to install UTM is I know that how many people click on this link on this banner, so how interactive and how engaging the banners are, so that we can do, like, maybe this banner is work better, and we, or this

**Jessica Yip:** paper.

**Jessica Yip:** Actually, a lot more people click on it.

**Jessica Yip:** So then we have more data.

**Jessica Yip:** Otherwise, it was just right on, you know, the, let's say we, um, to white paper, we don't know.

**Jessica Yip:** This white paper is like direct or come through the, um, the block.

**Jessica Yip:** So there's no way that we can track, right?

**Jessica Yip:** Well, no, Sorry.

**Kyle Gaudreau:** I didn't mean to cut you off.

**Kyle Gaudreau:** Yeah, go ahead.

**Kyle Gaudreau:** Not necessarily.

**Kyle Gaudreau:** It depends on what answers you're trying to get and where.

**Kyle Gaudreau:** Um, so, you know, constraining this to Google Analytics specifically, the typical recommendation I would do in that case.

**Kyle Gaudreau:** Um, and as good even if you were, there's other things related to like tracking this in the round we could always talk about later, but, um, is, uh, event tracking to the, to the links.

**Kyle Gaudreau:** And so then coming up with, um,

**Kyle Gaudreau:** essentially a taxonomy of, like, this can happen in different ways, right, like, there's different layers and events, and so, like, you could say, like, one broad bucket is, like, click the CTA button, and, like, so then you can see that in Google Analytics, and you can see all the CTA button clicks and where they're, and then as you double click into that, you can see the particular thing, and there are different ways of organizing, right, you could call that the white paper name, you could call that a white paper, usually there's three layers you can, if I recall correctly, you can add to this, so you could say, like, CTA button click, white paper, the particular white paper, and so, it's, use Google Tag Manager.

**Kyle Gaudreau:** Yeah, I do.

**Kyle Gaudreau:** it's pretty easy to do in Google Tag Manager nowadays, and so that's the most ideal because that's, that's essentially how GA is, like, purpose-built to track kind of stuff is based off the events, and that's how they track a lot of the conversion data nowadays, too.

**Kyle Gaudreau:** Um, and so in this case, it's not a true conversion.

**Kyle Gaudreau:** You're just tracking behavior to a conversion.

**Kyle Gaudreau:** Um, uh, yeah, that would be the most ideal because else, if you do it with UTMs, yeah, you're just going to start, like your data is going to start looking really weird and confusing.

**Kyle Gaudreau:** Uh, this is one that's like super, super common, like almost every stop of, you know, my in-house career when I would join in audit analytics almost every time my book kept something like this.

**Kyle Gaudreau:** So it's super common misconception.

**Kyle Gaudreau:** Got it.

**Jessica Yip:** Okay.

**Jessica Yip:** Let me look into it then.

**Jessica Yip:** Yeah, happy to share, uh, any detail.

**Kyle Gaudreau:** Um, but it's pretty easy to, to add for GT.

**Jessica Yip:** Yeah, we, we actually do have event conversions for all the, uh, call to actions, the three, but just looking to, like, is it able to wear these, um, call to action, come from in which pages was the, you know, like the curve converting path.

**Jessica Yip:** I know in Google, there's a,

**Jessica Yip:** solutions path, but it's more based on channel.

**Jessica Yip:** It doesn't tell you which page that they go to.

**Kyle Gaudreau:** I mean, this is the problem nowadays with Google Analytics, GA4 specifically.

**Kyle Gaudreau:** It's not great.

**Kyle Gaudreau:** We actually stopped using it at home based on my previous stuff, like it was still on our website, but we barely used it for any of our reporting.

**Kyle Gaudreau:** But yeah, I think depending on the questions you're trying to answer, there's things you can do to make that easier to answer in GA4, but also you may want to consider, do you remember now, use HubSpot?

**Kyle Gaudreau:** Yeah, we use HubSpot.

**Kyle Gaudreau:** like some of those same questions that you have, we could theoretically do in HubSpot as well.

**Kyle Gaudreau:** But anyways, if it's helpful, yeah, I've been using like UTM.

**Kyle Gaudreau:** then 4GA4 and it has worked well in the past so I haven't like see any ref flags like how you mentioned it but definitely we'll look into it more yeah yeah the last thing I'll just say on that it's not surprised because it actually can fly under the radar it's like you'd have to like segment your data in specific ways to find it but it did again the big challenges if like you won't get the accurate pulse on what your channels are doing yeah that's it and that's you know one of the key parts of what GA is trying to do but anyway sorry didn't want to be real less on that but that's got my attention to the here so there anything else you want yeah yeah yeah there was also one article it was a resource page uh i'm not really sure how to upload the image on that page like I don't know what type of slice so whatever to use because any of the options I had was just for text.

**Sadira Sittampalam:** So if you could just double check on that and let me know how I can upload it to that page, that would be great.

**Sadira Sittampalam:** Yeah, I think, yeah, let me look into it.

**Jessica Yip:** think for resources, the way we build it, there is no, actually, you can just track it.

**Jessica Yip:** Actually, I tried it last week because we're going to put banners in there, so I will do an example for you and send a link over after the call.

**Jessica Yip:** All right, cool.

**Jessica Yip:** And yeah, going on to the performance.

**Jessica Yip:** I'm looking at the air table, you mentioned about the enterprise.

**Jessica Yip:** I don't see where exactly.

**Sadira Sittampalam:** They are considering in the cluster enterprise related.

**Sadira Sittampalam:** There should be around 30 words, I think.

**Jessica Yip:** Okay, so it's a status cluster that are to review.

**Jessica Yip:** It's under constraint.

**Sadira Sittampalam:** If you scroll up just a bit, Kyle, so yeah, there's like total performance for the refreshes, which has doubled from last week, and that's probably because we started focusing a bit more on refreshes, so we put six out, I think, last week, because there was some play in the flow before that, and we went on to the new articles, we're seeing a little bit of a drop, and we think this is also because we only published four new articles last week anyway, so that kind of makes up for and you also mentioned we would do like a cluster based analysis, for this we're going to be

**Sadira Sittampalam:** moving into Lucas Studio Studio to present all this data, but we'll have that right for you by next week.

**Sadira Sittampalam:** I also wanted to ask whether you could give us access to GA4, even though Kyle just mentioned it's unreliable, where I'm still going to probably use it for their reporting a little bit.

**Sadira Sittampalam:** But yeah.

**Sadira Sittampalam:** I thought we had access to their GA4, but I could not remember that.

**Jessica Yip:** I think I don't think we're going to do that as access.

**Jessica Yip:** Yeah, I see it.

**Kyle Gaudreau:** Oh, I was looking for it, didn't show.

**Jessica Yip:** Yes, it's really weird.

**Kyle Gaudreau:** This actually happened to me as well.

**Kyle Gaudreau:** there is sometimes the view you're initially shown will cut off some accounts.

**Kyle Gaudreau:** I don't know why, but that did happen to me last, where I didn't think I had access to their GA4, because it starts with why it's at the bottom of list.

**Kyle Gaudreau:** you might go back and then I'll show you the full list.

**Kyle Gaudreau:** I'll double check on that.

**Sadira Sittampalam:** But yeah.

**Sadira Sittampalam:** I think that's all the updates we have.

**Sadira Sittampalam:** Do you have any questions?

**Sadira Sittampalam:** Yeah, you said you prepare a report in LOKER.

**Jessica Yip:** And what kind of data point are you going to put into or investigate the drop?

**Jessica Yip:** I see on GA and also SEM right that impressions and click has dropped like 30 days compared to 30 days period.

**Sadira Sittampalam:** I think that is most because there was like one article of yours that we did that we refreshed and it got like a lot of impressions and clicks.

**Sadira Sittampalam:** I think now that is like fizzling out so the entire site is going down.

**Jessica Yip:** Why is the all of a sudden there is a search and click in that one article?

**Jessica Yip:** Like I said, we refreshed it I think a month ago.

**Sadira Sittampalam:** or a few like very early on, it was something about translation costs, like a bunch multi will stand up, but I could be too long, but I think that was easy.

**Kyle Gaudreau:** So what you're saying is it spiked for like a short period of time and kind of was up but kind of normalized and came down?

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** From what I saw.

**Sadira Sittampalam:** We can clarify that.

**Kyle Gaudreau:** That's actually like a pretty common pattern.

**Kyle Gaudreau:** Like sometimes like Google's giving you a little bit of attraction, it's trying to see how almost kind of like experimenting how you'll do with some of those queries and it's not unusual for that happen.

**Kyle Gaudreau:** So when that does happen, we typically want to like go back and see if we can optimize to some of what it was getting at.

**Kyle Gaudreau:** Yeah, I'm seeing that page now.

**Sadira Sittampalam:** It's, yeah, let me share the screen on that one.

**Kyle Gaudreau:** Okay, should be seeing GSC.

**Kyle Gaudreau:** So we had a bit of a spike for like a week and then it's kind of come down to what it was before.

**Kyle Gaudreau:** So here, this is day range.

**Kyle Gaudreau:** I want the state range to come up my rail, I have 17th.

**Kyle Gaudreau:** So we say, trying to see like a quick before and after the drop, this might not be perfect.

**Kyle Gaudreau:** I don't have to go farther, translation, it's translation, translation, prices.

**Kyle Gaudreau:** How much does a translator cost?

**Kyle Gaudreau:** I think that what I'm at least seeing by quick glance of what we were getting some impressions and clicks from, it's just very broad in terms of intent.

**Kyle Gaudreau:** So while we were able to show some traction, I would say we would probably, I mean, if we can consistently rank for this stuff, amazing, but it is quite broad in terms of intent from like a ERCO standpoint.

**Kyle Gaudreau:** If it had some sort of modifier that was closer to ERCO, I think we'd have a bit more traction.

**Kyle Gaudreau:** This wouldn't, based off the queries I'm seeing, this having a little bit of that up and down wouldn't necessarily surprise me.

**Kyle Gaudreau:** Right, I'm just looking at the by-ending page.

**Jessica Yip:** I don't see there's a big change in terms of traffic to the particular block, like, if we're talking about what is typical cost.

**Jessica Yip:** the professional translation services, if that is the article, I don't see a search and traffic in that page.

**Jessica Yip:** But I do see...

**Jessica Yip:** Well, if we look, I mean, the view we were just looking at before this conversation shows it, right?

**Kyle Gaudreau:** So, like, if we look over time, you know, this is the spike, right?

**Kyle Gaudreau:** So, it's not a huge spike to be clear.

**Kyle Gaudreau:** It's not going to jump off the page when you're looking at old data.

**Kyle Gaudreau:** But, yeah, it's typically around like a few clicks a week.

**Kyle Gaudreau:** I mean, given this isn't a massive number, it's almost 20, but that's a little bit of the up and down.

**Kyle Gaudreau:** But in general, though, yeah, seeing some of those impressions up to the previous view we were looking at, let me get back to it.

**Kyle Gaudreau:** Switching between sharing on Google Meet, it's not very, yeah, especially when it's on different profiles, it's quite annoying.

**Kyle Gaudreau:** You know, we're at what, 60 here, 40 there.

**Kyle Gaudreau:** So that is actually, like, the Sedera's point that it was roughly in the ballpark of a drop of 20, that it's kind of contributing.

**Kyle Gaudreau:** In general, like, we don't, we want to be seeing consistent up and to the right in terms of impressions and click growth, so certainly, I would say, like, continuing the momentum on publishing new is our most ideal, and then anything we can do that further, just improve user experience, the CTA's can be a part of it, uploading images can be part of it, just that they can help ensure people stay engaged, that would be my other kind of area of recommendation of focus.

**Kyle Gaudreau:** Outside of that, you know, I would say just like,

**Kyle Gaudreau:** Making sure we have some good, like, you know, some good bets in terms of what we're going to do next in terms of topics.

**Kyle Gaudreau:** know we talked about, you know, a few that we want to focus on next.

**Kyle Gaudreau:** what I think about when I see a trend like this is, like, instead of, you know, just going for, like, bigger swing type things, like, go for some things that, like, we're confident we can rank well on, and, and generate momentum even though it's like lower volume just to keep, like, positive growth going.

**Kyle Gaudreau:** And, you know, so I would, I would make sure we take a look at, like, what we are all lining on in terms of next steps in terms of topics to try to keep that momentum.

**Kyle Gaudreau:** It's kind of like using a sports analogy.

**Kyle Gaudreau:** It's like trying to, you know, get some singles and doubles rather than swinging for some home runs.

**Kyle Gaudreau:** So, you know, that would be typically what we'd want to do in a case like this.

**Jessica Yip:** Yeah, I think in terms of topic, we're quite confident for that.

**Jessica Yip:** enterprise one and also like the personal cell phone or like um is text um legal those clusters we're quite confident that will drive quite bit of traffic but I think it would quite a bit more review from our side to make sure the position is correct um yeah and then like half of the content will be more of the water terms where we bring the impression up and just see early signal so we're pretty aligned on the topics going forward and these like uh yeah these two months okay cool yeah another thing that I was thinking about like if translation there's um a search in the volume and we want to continue to optimize the article translation this topic is actually very fitting to um our prospect and iCP because we do a lot of the workforce like multilingual team so even

**Jessica Yip:** build a search inquiry to tend to broaden.

**Jessica Yip:** One thing that I was thinking about, like we can continue to maybe run a couple more articles that it's more closer to intent, like how do you manage?

**Jessica Yip:** I think we do also have a couple articles about multi-lingual teams, based on the search inquiry, maybe we can bring some, have two to three articles just to hopefully Google will help us to rank higher if we publish articles under that cluster.

**Jessica Yip:** Agreed.

**Kyle Gaudreau:** And then similarly, making sure we're finding opportunities to, you mentioned some of the things you already have related to that content, like I know we create internal links as a part of our blogs that we're generating, but additionally we write those new translation angles you were talking about, looking at those existing internal linking into them as well and just continue to show that kind of like, you know.

**Kyle Gaudreau:** at a cluster relevance.

**Kyle Gaudreau:** So I think it's absolutely worth exploring.

**Kyle Gaudreau:** do recall you mentioned on the early days that angle of translation.

**Kyle Gaudreau:** So I think we can find the right angle modifier on the searches, et cetera, that gets it just a slight bit closer at how cool it sounds worthwhile.

**Jessica Yip:** Yep.

**Jessica Yip:** And I think two things that I want to ask is keyword cannibalization.

**Jessica Yip:** As I was looking at the blocks that ranked pretty well, we, there's two articles that might potentially competing each other is no one desk.

**Jessica Yip:** Okay, let me share with you guys this two links.

**Jessica Yip:** Basically is successful non-desk employee communications and the communication reaching non-desk employees.

**Jessica Yip:** So I see that they both ranking the same keywords.

**Jessica Yip:** competing.

**Jessica Yip:** So in this case, what is the best practice to, because one is a pillar article, the other one is just supporting law.

**Jessica Yip:** So yeah, what is the best practice to go about it?

**Kyle Gaudreau:** Yeah, so it depends to a degree of like, on a few different factors.

**Kyle Gaudreau:** Does one of them have more traction on a particular set of words and does that align with what you want to see and how you want to map intent on the website?

**Kyle Gaudreau:** Because those are, I was just checking up pages, know, slightly different files of pages, right?

**Kyle Gaudreau:** One being in the resources, the other as well.

**Kyle Gaudreau:** so if there is something there, like where you want to essentially map that and push that ideally, you know, that's one angle to consider.

**Kyle Gaudreau:** If they are just like truly like, if most of the queries are the same across both of them, and one of them just does, you feel a better job of landing the intent based off what you know from like a qualitative perspective, we should probably explore starting to refresh the other one.

**Kyle Gaudreau:** Sometimes what can happen in this case is you'll have one to three pieces or something like that, while they have a lot of overlap, one of them still has some queries that are a little bit unique to that.

**Kyle Gaudreau:** So you can start to refresh that piece to focus more on those that are truly unique to that, and then take some of that content that maybe could be additive to the other piece and start to move it over there.

**Kyle Gaudreau:** There's lot of other flavors of this.

**Kyle Gaudreau:** We could also consider just killing one of the pieces and redirecting it to the other, but there's not necessarily...

**Kyle Gaudreau:** like just one specific playbook like we have to consider like a few different figures so we can dig into it look at like you know which queries are overlapping how we'd want to map that and and and make a recommendation um but uh yeah I think it's something definitely we should be exploring as long as as long as it's truly like you know um sometimes you might see some queries pop up and it's not a huge deal because it's like so long but if they are really starting to like if this isn't setting us up for success we should consider yeah I think there will be some of you guys can look into like I think I would go for the approach where we extend the key work so then it's not much overlapping because if you look at the title it's very it's basically going to the same cluster um right yeah so for the I would say resources would be the the first to rank non the sample ecommunication and the

**Jessica Yip:** we can expand the content a little bit out, so then it's not competing.

**Jessica Yip:** yeah, I see a couple of articles like that.

**Jessica Yip:** It's not a main concern, but something that I think we should start looking into it, especially for the really good performing articles.

**Jessica Yip:** Yeah, I agree.

**Kyle Gaudreau:** Yes, Eric, we just make that action item for us to take into and just if we can find anything else as well?

**Sadira Sittampalam:** If you have any, if you have a list of articles that you've already got, send them over.

**Sadira Sittampalam:** Sure.

**Sadira Sittampalam:** Great.

**Jessica Yip:** Another thing is for long title text, and I, as I'm also looking at these articles, these tend to have long links, URL.

**Jessica Yip:** you suggest us to, like, trim it down and...

**Kyle Gaudreau:** You know, it's fine.

**Kyle Gaudreau:** just do it.

**Kyle Gaudreau:** I've been seeing this one pop up recently in my LinkedIn feed and people have been experimenting around this.

**Kyle Gaudreau:** Historically, the recommendation is keeping to a very specific character length.

**Kyle Gaudreau:** I'm now spacing out what the number is.

**Kyle Gaudreau:** It's like 70.

**Kyle Gaudreau:** Okay, I didn't know it.

**Kyle Gaudreau:** should have trusted myself.

**Kyle Gaudreau:** But I've actually been seeing people like experiment and challenge with that because they've been finding that rule is still showing longer character lengths and they were getting higher click-through rates.

**Kyle Gaudreau:** Admittedly, I haven't started to like validate that across the board, but I haven't, I've seen it multiple times now in the past few months with different people talking about this.

**Kyle Gaudreau:** So generally, I would say yes, going with 70, typically some of the ways I would do that, like by quick glance, like at least picking out the pipe in your code.

**Kyle Gaudreau:** If you can fit that in great, but I typically index more towards landing the message.

**Kyle Gaudreau:** But what applications are safe for?

**Kyle Gaudreau:** Use for business-related communication.

**Kyle Gaudreau:** We can probably have a shorter version of that.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Yeah.

**Jessica Yip:** Yeah.

**Jessica Yip:** We definitely can shorten it.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Like, like if we just said, you know, safe to you, and anyways, just moving those words around and cutting it somehow, yeah, no, worth checking out.

**Kyle Gaudreau:** But yeah, anything we do that we would change on these, I would want to just like check back on the quickly roots.

**Kyle Gaudreau:** So a little while later.

**Kyle Gaudreau:** Yeah.

**Jessica Yip:** So it's so good to try it, know, to experiment whether it's, and then when we change the URL, then we make sure that it's transferable, right?

**Jessica Yip:** Like the SEO score that being built in this link can transfer to the other one.

**Jessica Yip:** Oh, in this case, I would advocate for not changing the URL, just the title.

**Kyle Gaudreau:** Just the title.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Yeah.

**Jessica Yip:** And then not to say there aren't times.

**Kyle Gaudreau:** That makes sense.

**Kyle Gaudreau:** It's just like, I think we'd create unnecessary friction from a SEO standpoint, if we did that.

**Kyle Gaudreau:** On it.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Yeah, I think we will dig into the cannibalization.

**Jessica Yip:** Anything else comes up trying wise, let me know.

**Kyle Gaudreau:** Happy to help wherever I can.

**Jessica Yip:** Cool.

**Jessica Yip:** Awesome.

**Jessica Yip:** Appreciate the time, Jessica.

**Kyle Gaudreau:** Thank you, Kyle.

**Jessica Yip:** It's enduro.

**Jessica Yip:** Alright.

**Jessica Yip:** you.

**Sadira Sittampalam:** See you.
