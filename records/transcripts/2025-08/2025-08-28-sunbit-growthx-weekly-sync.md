# Sunbit <> GrowthX Weekly Sync

<metadata>
date: 2025-08-28
time: 16:00 UTC
duration: 27 minutes
organizer: Kyle Gaudreau (GrowthX)
participants: Jason Beltran (Sunbit), Angel Kemper (Sunbit), Ehtisham Hussain (GrowthX), Kyle Gaudreau (GrowthX)
fathom_recording_id: 83603753
fathom_url: https://fathom.video/calls/392845088
share_url: https://fathom.video/share/VSCRqtM5KVjxUjHbpLmgiai3PgAdPLNM
source: fathom
enriched_on: 2026-03-03 09:05 UTC
</metadata>

---

## Summary

GrowthX and Sunbit reviewed progress on content delivery and performance metrics, with organic traffic showing strong growth from January to August across impressions (up to ~2,800), sessions (~1,800), and new users (~1,500). The team implemented social post instructions for 25 new articles (Facebook and Instagram) and discussed strategies for adapting content for LLM consumption, including potential Reddit-inspired tactics and experiments with the Monograph team. Key action items include retroactively adding delivery dates to published articles, providing priority key events list (B2B form fills, B2C shop directory and pre-qual links), setting up Tray webhook integration testing, and discussing Sunbit's Tray pricing concerns.

---

## Context

Sunbit is a fintech company providing point-of-sale financing solutions. GrowthX has been delivering a comprehensive content marketing engagement, building a knowledge center strategy that drives organic traffic. This weekly sync is the standing operational review between the Sunbit content and business teams (Jason Beltran, Angel Kemper) and the GrowthX delivery team (Ehtisham Hussain, Kyle Gaudreau) to track content publishing, performance metrics, integration updates, and strategic initiatives.

---

## Relevance

**To GrowthX Delivery:**
- Proven content strategy effectiveness: organic traffic metrics across 8 months show consistent growth (sessions 1K→1.8K, new users 949→1.5K), validating the knowledge center approach for B2B2C fintech positioning
- Social post implementation working within workflow; request for retroactive delivery dates indicates operational maturity and desire for better content tracking
- Publishing automation in progress with engineering; Tray webhook integration pending to enable automated posting workflows

**To CheckThat:**
- Sunbit exploring LLM-friendly content adaptations and Reddit-influenced tactics; GrowthX running parallel experiments with Monograph on subreddit strategies, providing research opportunity for AEO and LLM content patterns
- Discussion of content optimization for LLM consumption highlights growing client concern about AI overviews and search landscape changes

**To GrowthX Business Development:**
- Strong account health signal: consistent growth trajectory, expanding feature requests (retroactive dating, automation), and Sunbit's investment in integration complexity (Tray, webhook automation) indicates expansion potential
- Sunbit evaluating iPaaS tools and considering long-term automation capabilities; positioning GrowthX as strategic delivery partner managing complexity of content ops at scale
- Client openness to experimentation (Reddit tactics, LLM-friendly content) suggests room for strategic advisory expansion

---

## Overview

- Social post instructions implemented; new batch of 25 articles delivered with social posts included
- Organic traffic metrics show positive trends: impressions, sessions, and users all increasing
- Automation efforts ongoing for publishing content and integrating with Tray
- Discussion on adapting content strategy for LLMs and potential Reddit-inspired tactics

---

## Key Topics

### Social Media Content Implementation

  - New batch of 25 articles delivered with social posts for Facebook and Instagram
  - Request to retroactively add delivery dates to older content for better tracking
  - Action item: Add estimated delivery dates to "Ready to Publish" articles

### Performance Metrics Review

  - Organic traffic metrics showing positive trends from January to August:
      - Sessions increased from \~1,000 to \~1,800
      - New users up from 949 to \~1,500
      - Engagement time improved to 1 minute 27 seconds
  - Click-through rate remained steady at 0.3% despite increased impressions
  - Action item: Provide list of key events to prioritize in future reports (e.g., B2B form fills, B2C shop directory clicks)

### Content Strategy and LLM Considerations

  - Discussion on adapting content for LLM consumption
  - Potential experiments with Reddit-inspired content tactics
  - Consideration of creating Sunbit-specific subreddits or contributing to existing ones
  - GrowthX to share insights from ongoing experiment with Monograph team

### Automation and Integration Updates

  - Publishing automation ticket with engineering team; awaiting implementation
  - Sunbit AI integration: Marcel informed and will set up ticket
  - Tray webhook integration pending; Jason requested notification when testing begins

### Tray Platform Discussion

  - Sunbit evaluating iPaaS options, likely to continue with Tray despite pricing concerns
  - Jason highlighted Tray's value in empowering business users to build their own agents
  - Shared success story: Tray integration saved $60,000 on Salesforce to NetSuite project

---

## Action Items

**Ehtisham Hussain (GrowthX)**
- Retroactively add estimated delivery dates to articles in "Ready to Publish" group (focus on early/mid/late month timeframe rather than exact dates)
- Notify Jason when engineering starts webhook testing for Tray integration (48-hour test window; Jason needs advance notice to capture logs for test data)

**Jason Beltran (Sunbit)**
- Provide list of priority key events for B2B (form fills) and B2C (shop directory, pre-qual links)

**Kyle Gaudreau (GrowthX)**
- Mention Sunbit's Tray pricing concerns to Niels at happy hour

---

## Transcript

**Kyle Gaudreau:** We have this weird thing with our Wi-Fi where it keeps trying to connect to a different endpoint. And so when you're in some of these rooms, it's trying to connect to the wrong one. It's very weird. Well, despite not having full bars, it looks like it's coming in decently.

**Ehtisham Hussain:** Hi, Jakub. Hey there.

**Angel Kemper:** How's it going?

**Ehtisham Hussain:** Good. So should we wait for Jason?

**Angel Kemper:** I think he should be coming. I was just talking to him a moment ago. I think we can get started. I didn't know what the agenda was, but if you want to start on the social post stuff, since I run that, we can talk about that first.

**Ehtisham Hussain:** So thank you for providing instructions for the social posts. We have included that in our workflow and all the social posts are now within the articles that we have prepared for you this week. To the best of our knowledge, they follow the instructions and everything. So you can check them and see if something's missing or something needs to change. And as per your instructions, they're only for Facebook and Instagram. The document was really helpful and pretty much sorted things out for us.

**Angel Kemper:** And how do I distinguish which ones are the newest 25? I see a date delivered column, but those dates are blank.

**Ehtisham Hussain:** The latest batch of 25 should have today's date on them. In the OS table, because there were a bunch of ready-to-reviews that were delivered previously, so that's why the date is blank on them. But for the previous batch, we have the date delivered, and for this batch too.

**Angel Kemper:** Is there not a way to retroactively apply the delivery date on the other blogs that are blank right now?

**Ehtisham Hussain:** It's going to be a little inaccurate. So is it up to a good degree of accuracy, which ones were delivered two weeks ago or three weeks ago? But there may be a couple of articles that get mixed up.

**Angel Kemper:** Going forward, obviously having the delivery date on the old ones would be helpful. What I mentioned last week is we're having to send these to legal and then wait for approval. And then once they approve, we're going through and manually posting those out. So I want to make sure that I am posting and updating in the right places. If it's just an estimated delivery date, that's fine. Really what I'm looking for is whether it's early in the month, mid-month, or later in the month. I don't need the exact date. The biggest part would be the ready to publish ones. Thanks for implementing that so quickly.

**Ehtisham Hussain:** We can prioritize that. Yeah, I've taken this down as an action item, so we can get it done fairly quickly.

**Angel Kemper:** And then I'll take a look at the newest 25 that you mentioned and can let you know of any feedback.

**Ehtisham Hussain:** So I'm going to share the full screen. So one more action item from last week was to include the looker report and data for all the articles that we've published.

**Ehtisham Hussain:** If we look at the data from a big picture perspective, everything is going up because we have been publishing so consistently. Impressions have gone up from May to August, which is what we want. We want lower figures at higher positions, meaning the top-ranking articles are ranking in the top 10. If you look at the GA4 data for organic sessions from January to August (August data pulled through today), this is organic sessions only for anything published in the knowledge center. This excludes referral traffic and social media traffic. Sessions went up across the board. Active users went from around 1,000 in January to 1,800 now. New users increased significantly from 949 to 1,500, and hopefully will reach 1,600-1,700 by end of month. Engagement time was showing zero for the first couple of months, but has gone up significantly to 1 minute and 27 seconds, which is really good. It means people are spending time on the page and engaging with the content. For key events, you have a lot set up there—anything from carousel clicks to form fills to any engagement. The count is around 314 last month, 303 this month and counting, improving from the 200s to 300.

**Kyle Gaudreau:** Yeah, it's probably worthwhile for us to dig into the key events and figure out what we want to filter for, because some of those are definitely more valuable than others. Clicking on a carousel versus a form—Jason cares much more about form fills and things of that nature.

**Ehtisham Hussain:** So which one should I prioritize for the next meeting?

**Jason Beltran:** We'll provide a list, because there's differing key events based on the content. For B2B, we want form fills. For B2C, it's more the shop directory and pre-qual links. We have a very unique B2B2C model, which is challenging compared to strictly B2B clients.

**Ehtisham Hussain:** So one thing I noticed: this is a positive trend across pretty much all variables except click-through rate. Because impressions went up so drastically and we're getting a lot more impressions, traffic has kept increasing. But the click-through rate has remained around 0.3%, which you'd expect to increase. This is a common trend we're seeing with a lot of customers—impressions are going up while click-through rates stay the same or decline slightly.

**Jason Beltran:** I'm curious how you're calculating click-through rates. If we have increasing impressions, the denominator changes, which means it gets more challenging to get incremental gains for clicks. So if we're looking at pure volume, it's positive.

**Kyle Gaudreau:** The additional thing to keep in mind is AI overviews, but even before this was part of the landscape, this isn't an uncommon trend. As your proportion of non-brand traffic increases, it's just different metrics. It's going to change and normalize over time.

**Jason Beltran:** Yeah, with more adoption of LLMs, it's changing the entire landscape. In the future, is a website just to feed the LLMs? There's a lot of people hypothesizing that that is the future of the internet.

**Kyle Gaudreau:** It makes you think about best practices—the flow of a page, how it needs to look, what its intention is. We've talked with some folks who are pushing to experiment with a shadow version of their content that's more text-driven and LLM friendly.

**Jason Beltran:** I was thinking of that. Yeah, I'm not convinced that works either, especially if you're tagging your images properly. Although, one thing I've noticed is Reddit. LLMs love Reddit, which I think isn't a good thing, but Reddit's just a forum. Every time I'm looking into LLMs and what they're referencing, Reddit consistently comes up. Do you add a forum-like module to your site?

**Kyle Gaudreau:** I think that's probably a result of other signals and replicating that. But there's value to extract from that in different ways. One of the things we've been doing more and more that we can apply here is narrowing in on different personas—where would those personas live? How are you narrowing on certain subreddits? How do you look at recency of different topical things that are bubbling up in those subreddits?

**Kyle Gaudreau:** Long story short, you can work back off of prompts that are informed by the behaviors on those subreddits. Does that help you create content that's inspired by things that are getting picked up in another way?

**Jason Beltran:** Or do we actually start contributing to these subreddits or create our own subreddits?

**Kyle Gaudreau:** We're running an experiment there with the Monograph team. I'm happy to keep you in the loop. It's just kicking off. We're going to be posting on their account page specifically to the subreddits themselves to see if it gains traction. We have no idea if it's going to work, but let me know how that goes.

**Jason Beltran:** Yeah, we're definitely up for it. I think it's the Wild West right now. It's all about experimentation. Those who want to experiment and get ahead of it are going to be the winners.

**Kyle Gaudreau:** Totally. If we get some early signal, happy to bring that back.

**Jason Beltran:** Yeah. Maybe we'll start running our own tests simultaneously.

**Ehtisham Hussain:** Yeah, that was pretty much it. On the publishing front, we're trying to automate it. The ticket is with engineering and we expect it to go live soon. I don't have a date for it, but they're working on it. I'll update you async as soon as I learn something. And for Sunbit AI, Marcel has been informed and he will contact you and then set up a ticket.

**Jason Beltran:** One thing—the webhooks. Sending the data via the public URL for Tray so we can start automating the posting. Is your dev team testing that? And if so, can you let me know when that happens so I can look at the logs and build out the rest of the workflow?

**Ehtisham Hussain:** Yeah, we'll do that. It's with engineering and they'll inform me hopefully today or tomorrow, and then I'll let you know the date.

**Jason Beltran:** Just let me know. We have a 48-hour test window in Tray because we're pretty strict with security. So as soon as they start pushing tests, let me know so I can capture data and use it for testing.

**Kyle Gaudreau:** Just so happens I'm seeing some Tray folks tonight at a happy hour. If there's anything I can put a bug in their ear to help you out with, just let me know.

**Jason Beltran:** Yeah, we were working with Max, an AE there for six or seven years. Now we got transferred to Bud. We signed up with them six years ago. That was all me building it out. Now our IT team is really interested in what an iPaaS can do for the rest of the organization. But we're evaluating other tools. Tray is the one everyone likes so far, but the pricing is a little bit high for what we want to do. I actually think we'll end up going with Tray, continuing, because the switching costs would be really high. But maybe you can let them know our concerns.

**Kyle Gaudreau:** I'll definitely put some bugs in their ears. I'll be seeing Niels, who's a Tray power user who's been there forever. He has a lot of influence there.

**Jason Beltran:** That's great. What our team is trying to do is really tap into the agentic aspects of what Tray is doing. We've learned that developing everything in-house isn't feasible. We want to empower all of our business users to build their own agents, or at least give them the tools to do that. That's where Tray is really going to come into play.

**Jason Beltran:** It's really nice because I'm the only one who's been using it for the past five years. My role has extended beyond what I normally do. I've hooked up our accounting systems and a bunch of other things. It's really nice that we're getting greater involvement.

**Kyle Gaudreau:** He sounds like a very similar profile. He was using Tray at New Relic and was a power user there, and just started doing all sorts of things.

**Jason Beltran:** Yeah, I'll give you a quick story. We were moving to NetSuite and a consulting firm quoted us $60,000 to do an integration from Salesforce to NetSuite. I did it in about four hours with Tray, no cost. It's been up and running for the past three years.

**Kyle Gaudreau:** It's pretty impressive what you can do with it. One thing that stood out when I worked with Niels—we stripped out all the logic of Marketo and built it all in Tray. All the lead management, scoring, routing was done in Tray. Anytime we had to do anything different, like when a lead hits a score, send to enterprise AE—usually that takes multiple weeks. He would do it in a matter of, "I can get that done today."

**Jason Beltran:** Yeah, I just onboarded one of our Salesforce system admins to Tray and he loves it and is really taking off with it.

**Kyle Gaudreau:** It's wild that a lot of folks haven't been exposed to it and don't understand what's possible.

**Jason Beltran:** People want no code, low code, but you still have to think like an engineer and that intimidates folks. Zapier makes it super easy, but it's so lightweight that if you're more advanced, you run into walls. Tray unlocks all that, but for the normal user, it's intimidating. Some folks on my team thought they were pretty technical, but once they got introduced to Tray, they froze and never logged in again.

**Kyle Gaudreau:** Interesting. Well, we could nerd out about this all day, but yeah, we'd love to continue hearing anything cool you're building over there.

**Jason Beltran:** Yeah, Angel's really deep in Tray. She built out our request workflow—anything that comes in goes to creative and legal teams, and we store attestations. She built it out using Monday.com, Google Business Suite, and Tray. It's pretty cool.

**Angel Kemper:** Yeah, it's been super helpful, and I love Tray. I'm definitely intimidated by it, but I think it's really rad. Every time Jason and I have sessions, I'm like, yeah, this is cool. I want to learn more about it. It's fun to build those repeatable engines. When it actually works, it's just amazing.

**Angel Kemper:** Sometimes we're like, is this working? Then we go back and look at the logs and we're like, hell yeah, it's working. This is really dope, and people need to appreciate it.

**Kyle Gaudreau:** And the ability to put in your own custom JavaScript. It's wild.

**Jason Beltran:** Oh, yeah. It's always been amazing, but now with Claude and GPT-5, I don't have to write anything. I just prompt, "write me the script," plug it in. Wish I had that back then.

**Kyle Gaudreau:** Well, good chatting with you all.

**Ehtisham Hussain:** No, everything is covered.

**Jason Beltran:** All right, thanks, everyone.
