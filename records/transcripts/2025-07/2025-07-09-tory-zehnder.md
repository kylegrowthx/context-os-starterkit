# Tory Zehnder

<metadata>
date: 2025-07-09
time: 20:01 UTC
duration: 15 minutes
organizer: bianca@growthx.ai
participants: Bianca Nieves (GrowthX), Tory Zehnder (Hex)
fathom_recording_id: 73205852
fathom_url: https://fathom.video/calls/346302103
share_url: https://fathom.video/share/NCcYxgyqiL2gYWtZ15SS49HuwS5GiRh4
source: fathom
enriched_on: 2026-03-03 11:08 UTC
</metadata>

---

## Summary

Bianca Nieves (GrowthX's new Head of Growth) evaluated Hex with Tory Zehnder (Hex sales) to address GrowthX's lack of analytics infrastructure—they had no internal data tracking until recently implementing Google Analytics. GrowthX's core needs are multi-channel attribution across LinkedIn, email, podcasts, and in-person events, plus tracking product launch performance and customer retention signals. Tory clarified that Hex is a data analysis and visualization platform requiring a cloud data warehouse (Snowflake, Databricks, or Redshift), not an event tracking tool, which prompted Bianca to discuss alignment with her team on whether a data warehouse investment makes sense for their current stage.

---

## Context

Bianca Nieves joined GrowthX approximately 1.5 months prior to this call as Head of Growth, reporting to the VP of Go-to-Market. She owns all website-related functions including analytics, tracking, pixels, and CRM. GrowthX had zero internal analytics tracking before Bianca's arrival—the company previously only tracked analytics for its clients. Bianca recently implemented Google Analytics and explored GDPR-compliant alternatives like Plausible but found them insufficient for GrowthX's growing needs around campaign attribution and multi-channel measurement. The company is planning major product launches (including a podcast and video-first content) and uses data-driven decisions to validate high-level company bets.

---

## Relevance

- **To GrowthX Business Development:** Early-stage product fit question. GrowthX lacks data warehouse infrastructure (currently using manual CSV analysis), which is a hard requirement for Hex adoption. Deal outcome depends on whether team will invest in Snowflake/Databricks setup. Bianca committed to internal discussion by end of week (2025-07-13) to determine go/no-go.

- **To GrowthX Delivery:** GrowthX's own analytics infrastructure mirrors challenges their clients face—no unified multi-channel tracking, manual data pulls, fragmented tools. This is firsthand experience that could strengthen positioning in content marketing and measurement consulting.

- **To CheckThat:** Hex discussion highlights the gap between event tracking (Google Analytics, Amplitude, Mixpanel) and analysis tools. CheckThat's AI visibility and prompt quality assessment are orthogonal to Hex but relevant to GrowthX's multi-channel attribution needs if they use AI for content personalization or automated insights.

---

## Overview

- GrowthX lacks robust analytics tooling; recently implemented Google Analytics
- Primary needs: multi-channel attribution, user journey tracking, campaign performance analysis
- Hex's event tracking limitations and data warehouse requirements may not align with GrowthX's current setup
- Bianca to discuss internally and revert by end of week on potential fit

---

## Key Topics

### GrowthX's Current Analytics Landscape

  - Recently implemented Google Analytics (1.5 months into role)
  - No prior analytics tracking for GrowthX (only for clients)
  - Explored platforms like Plausible (GDPR compliant) but found unsuitable
  - Bianca leads growth, owns website-related analytics, tracking, CRM

### Analytics Needs and Use Cases

  - Track returning users and campaign performance (e.g., programmatic landing pages)
  - Measure success of upcoming product launches and publications (podcast, video)
  - Attribute traffic sources and identify high-converting locations
  - Analyze user retention and pipeline progression
  - Multi-channel attribution (LinkedIn, email, podcasts, in-person events)
  - Validate hypotheses and bets made at company level

### Current Challenges

  - Manual, scrappy approach to data analysis
  - Lack of consistent user tracking from first touch to close
  - No visibility into client content engagement or team website usage
  - Difficulty in identifying and addressing customer issues in the pipeline

### Hex Product Overview

  - Notebooking feature for SQL and Python-based data analysis
  - Visualization capabilities for sharing insights
  - Self-service features for deeper data exploration
  - AI assistance for SQL and Python query writing
  - Requires connection to a cloud-based data warehouse (e.g., Snowflake, Databricks, Redshift)

### Potential Limitations for GrowthX

  - Hex doesn't provide event tracking capabilities (unlike Amplitude or Mixpanel)
  - GrowthX currently lacks a data warehouse for storing analytics data
  - SQL knowledge required (Bianca has basic SQL skills from a course)

### Team and Usage

  - Initially for Bianca and head of customer ops (3 users to start)
  - Potential for expansion as the company grows

---

## Action Items

**Bianca Nieves (GrowthX)**
- Discuss with team regarding event tracking needs and data warehouse setup; report back to Tory by end of week (2025-07-13)

**Tory Zehnder (Hex)**
- Send async resources (product overview, demo, recordings, documentation, videos) to Bianca

---

## Transcript
**Tory Zehnder:** Hey, how are you?

**Tory Zehnder:** Oh you're on mute by the way.

**Bianca Nieves:** Hello, how are you?

**Tory Zehnder:** Good.

**Tory Zehnder:** Great to meet you.

**Bianca Nieves:** How's your day going so far?

**Bianca Nieves:** Good so far.

**Bianca Nieves:** I think you're probably with my last call or close to my last call, so we're getting there.

**Tory Zehnder:** How about you?

**Tory Zehnder:** Nice.

**Tory Zehnder:** Yeah, days going on so far.

**Bianca Nieves:** Are you on the East Coast?

**Bianca Nieves:** No, I'm in Scottsdale.

**Bianca Nieves:** I split between Scottsdale and San Francisco, so go back and forth, mostly West Coast.

**Tory Zehnder:** Nice.

**Tory Zehnder:** Scottsdale's so fun.

**Tory Zehnder:** I went there a couple years ago, and we had such a good time there.

**Bianca Nieves:** For sure, for sure.

**Tory Zehnder:** Definitely like a growing city.

**Tory Zehnder:** I'm surprised you're splitting Scottsdale during the summer.

**Bianca Nieves:** Yeah, yeah.

**Bianca Nieves:** It's like I was living in Seattle for the last three years, and so like I've got the rain and all of that's fair, and I've got a pool, so I go swimming at night.

**Tory Zehnder:** Oh my god, a night swim.

**Bianca Nieves:** There's nothing like that.

**Tory Zehnder:** Yeah, It's definitely too hot to go in the day.

**Tory Zehnder:** Yeah.

**Tory Zehnder:** Oh my god.

**Tory Zehnder:** So nice.

**Tory Zehnder:** Well, awesome.

**Tory Zehnder:** Well, great meeting you.

**Tory Zehnder:** So today, we'd just love to chat.

**Tory Zehnder:** A little bit more about your needs and use cases kind of driving you to look at Hex and consider software.

**Tory Zehnder:** So we'd love to just kick us off with quick round of intros, and then we'd love to hear from you.

**Tory Zehnder:** It'd be great to get a little background on the team, how you're doing with your current tooling, what your current tooling is, and some of the reasons that you're looking for a data analytics software.

**Tory Zehnder:** I'm happy to jump in and talk a little bit more about Hex and talk about some areas where I think we can be helpful.

**Tory Zehnder:** And if it sounds like a good fit for you, I would be happy to spend some time at the end talking about Next Steps.

**Tory Zehnder:** Does that sound good?

**Tory Zehnder:** And anything else you want to cover?

**Bianca Nieves:** Yeah, no, sounds like a plan.

**Tory Zehnder:** I think that's perfect.

**Tory Zehnder:** Awesome.

**Tory Zehnder:** Cool.

**Tory Zehnder:** Well, I can kick us off with intros.

**Tory Zehnder:** So I'm Tory.

**Tory Zehnder:** on the account team here.

**Tory Zehnder:** So we'll just be your point of contact going forward as far as any questions you have, evaluating Hex, and considering software.

**Bianca Nieves:** Awesome.

**Bianca Nieves:** Yeah, sounds good.

**Bianca Nieves:** I'm Bianca.

**Bianca Nieves:** I just joined GrowthX maybe a month and a half ago.

**Bianca Nieves:** Tooling is basically non-existent at the moment, specifically for analytics. I implemented Google Analytics yesterday. So up to this point, no analytics tracking of any kind. We track them for our clients, but not for us.

**Bianca Nieves:** So this would be probably the first time we actually make this a project and take it on. It's wide open. I think what we want to see at a high level is tracking from multiple sources. We've explored platforms like Plausible — they're like a GDPR compliant version of Google Analytics — but that was not a good fit for us. We're looking for something more powerful. And then we'd love to explore pricing to see if this is more like a self-service tool or something that we're going to go through multiple steps in the process for.

**Bianca Nieves:** Team-wise, I lead growth here at GrowthX. My boss is the head of Go-to-Market — he's focused on product and building out some of our next product launches. I own everything that's website related — analytics, tracking pixels, CRMs, all that stuff is my wheelhouse.

**Tory Zehnder:** Yeah, awesome.

**Tory Zehnder:** Thank you so much.

**Tory Zehnder:** That was great in-depth background and really appreciated hearing a little bit about what you're considering, I guess, in your next tool.

**Tory Zehnder:** Would love to kind of dive in a little bit deeper there.

**Tory Zehnder:** So in terms of an analytics tool, so I understand you implemented Google Analytics and, you know, I assume we'll like to track, you know, traction, like probably on your website or maybe even what users are doing.

**Tory Zehnder:** But talk to me about your analytics needs.

**Tory Zehnder:** Like, what are you hoping to track?

**Tory Zehnder:** Like, an ideal scenario when you have tooling in place?

**Tory Zehnder:** Like, what is the state of tracking analytics look like?

**Bianca Nieves:** Yeah, think being able to see when users are returning and tracking some of our campaigns, like, for programmatic landing pages.

**Bianca Nieves:** So we run some campaigns, like, we're going to start to run some campaigns that, you know, spin up hundreds of landing pages at once and then kind of, like, push that over a six to eight week period.

**Bianca Nieves:** And so I think being able to measure the success.

**Bianca Nieves:** So that would be pretty helpful.

**Bianca Nieves:** There's also a ton of product launches and kind of like publication launches that we're gearing up for the next couple of weeks.

**Bianca Nieves:** So a pretty big podcast publication, video first.

**Bianca Nieves:** We'd love to be able to return traffic and attribute that to something, which right now we kind of just get a little bit of signal from LinkedIn and casual conversations with the team.

**Bianca Nieves:** So I think a huge win just being able to like step in, push these campaigns, launch these products, launch these publications, and be able to say like, hey, like this, you know, San Francisco for some reason is converting at 4x New York City.

**Bianca Nieves:** Maybe we should just double down there, hire a field sales team there, and just, you know, drive that.

**Tory Zehnder:** I think that's how I'm thinking about it, but let me know.

**Tory Zehnder:** Yeah, nice.

**Tory Zehnder:** No, I love that.

**Tory Zehnder:** Definitely like very important analytics to track.

**Tory Zehnder:** And in terms of like what, so I guess there's, you know, one component of like having Google Analytics that actually like triggers the events.

**Tory Zehnder:** That's the data.

**Tory Zehnder:** Like, in terms of, like, where you intend to analyze this data, like, what tools have you used in the past to do that?

**Tory Zehnder:** And, like, what are you doing now if you're doing anything now?

**Bianca Nieves:** It sounds like you have no tooling.

**Bianca Nieves:** Yeah, yeah.

**Bianca Nieves:** I mean, I've done Google Analytics.

**Bianca Nieves:** I've done, like, mixed panels and amplitudes that are more on the product side.

**Bianca Nieves:** I've also done, like, you know, just manually, like, with CSVs, which is very, very scrappy, so don't want to go back there.

**Bianca Nieves:** In terms of, like, using this tool to, like, I guess go deeper, I'm not really sure.

**Bianca Nieves:** I'm not sure exactly where I'd start.

**Bianca Nieves:** I think right now the biggest bottleneck is, like, kind of retention.

**Bianca Nieves:** And so it would be really important for us to be able to, like, say, okay, this is a person that's stuck in pipeline or this is a customer that's stuck and they've got a fire alarm.

**Bianca Nieves:** How do we service that person and get back to them and kind of, like, bring them into the next step of their journey?

**Bianca Nieves:** Right now there's no tracking. We don't know what clients are looking at or what type of content engages them. We don't know if people from our team are even looking at the website — all those triggers we just don't have, which has been hard. I've also used ABM platforms like 6sense and Rollworks, but I don't think we're necessarily diving into ABM just yet. Having analytics just to get started would be huge.

**Tory Zehnder:** That was a good brain dump.

**Tory Zehnder:** No, that was very helpful.

**Tory Zehnder:** Yeah, no, that definitely makes a lot of sense.

**Tory Zehnder:** So it sounds like your priorities right now are getting the data and tracking it — you have Google Analytics in place. I'm curious what your priorities are in looking for a tool. Is it tracking capability like Amplitude or Mixpanel? Or are you looking for visualization tools or analysis tools? What's top of mind?

**Bianca Nieves:** Yeah, I think having custom tooling would be exciting. Can you repeat the end of your question? I want to make sure I answer it correctly.

**Tory Zehnder:** Yeah, definitely. I'm curious to know what types of things you're looking for in a tool. Some tools have tracking capabilities like Amplitude and Mixpanel. Some have visualization capabilities. Some have notebooking type features for deep analysis. What's top of mind for you?

**Bianca Nieves:** Multi-channel attribution is number one — being able to follow the same user from LinkedIn, email, to a podcast, to an in-person event, and track that consistently. That's the biggest thing right now. Being able to identify where people are dropping off in a digital way. Right now a lot of this is just hunches we have, but being able to validate our hypotheses is the primary objective. We made some company-level bets and we're driving towards them as fast as we can. But honestly, it's very manual and scrappy right now. We have to go into each tool, build lots of sheets, and when someone edits a sheet, everything breaks. Just being able to track a user from their first touch all the way through to close would be the highest priority.

**Tory Zehnder:** All right.

**Tory Zehnder:** Got it.

**Tory Zehnder:** Yeah.

**Tory Zehnder:** And I'm curious to know like how you found Hex and what jumped out to you about our tool.

**Bianca Nieves:** Yeah, sure thing. My team actually recommended you all. Our VP of Go-to-Market and our CEO are familiar with the software. I'm not familiar — I haven't seen the platform — but there are some posts internally. So I figured I'd just get on a conversation with you today to chat through it.

**Tory Zehnder:** Yeah, awesome.

**Tory Zehnder:** Okay.

**Tory Zehnder:** That's great to hear.

**Bianca Nieves:** Do you know if they've used Hex before?

**Bianca Nieves:** I don't think so.

**Tory Zehnder:** So, yeah.

**Tory Zehnder:** Oh, okay.

**Bianca Nieves:** Yeah, I don't think they get Big E's.

**Tory Zehnder:** Nice.

**Tory Zehnder:** Okay.

**Tory Zehnder:** Got it.

**Tory Zehnder:** Yeah.

**Tory Zehnder:** And in terms of like who would be using it at the company, like clearly you like to get into analytics and campaign tracking and all of that.

**Tory Zehnder:** I'm curious to know if you're looking for a tool just for yourself or if you're looking for a tool on behalf of other people in the company.

**Bianca Nieves:** Yeah, definitely for myself.

**Bianca Nieves:** We probably expanded to our head of customer ops.

**Bianca Nieves:** That would be also good for reference, especially through the lane of like retention and like updates to our clients.

**Bianca Nieves:** So, yeah, I think probably three people that would make use of it for now.

**Bianca Nieves:** I'm not sure how that would expand as things grow, but for now, I think that's how we would start out.

**Tory Zehnder:** Awesome.

**Tory Zehnder:** Okay.

**Tory Zehnder:** Yeah, that sounds great.

**Tory Zehnder:** So let me talk a bit about how Hex works. At a high level, we have a notebooking feature and a visualization feature. In the notebooking tool, you can work with SQL and Python to analyze your data and figure out things like drop-off rates. On the visualization side, you surface all that data and visualize it to share with the business. We also have self-service capabilities so people can dive deeper into the data apps. But have you worked with SQL and Python or notebooking style tools before?

**Bianca Nieves:** Yes, I took a SQL course, but I'm not a master — I can do basic SQL. Other than that, no other notebooking tools. I've used things like Clearbit early on for prospecting and Reveal, those kinds of tools.

**Tory Zehnder:** Okay. So with Hex, we're definitely SQL and Python based. A lot of the analysis you'll run in the tool involves working with SQL. We do have AI baked into the product to help write SQL and Python, which is very helpful. One thing I wanted to call out though — in terms of tracking events and putting together those events, tracking events like Amplitude, Mixpanel, or Google Analytics — that's not something baked into our product. Where we come into play is once you have that data. If Google Analytics is tracking events and you have that data living in a data warehouse, that's where we can connect to that data warehouse and you can start analyzing it within Hex. I wanted to call that nuance out to make sure it's not a deal breaker for you. How do you feel about that?

**Bianca Nieves:** Yeah, I got it. That makes sense. I think the team had a different vision, but I'll get back to them after our call.

**Tory Zehnder:** Got it. No worries. Curious if they have any information about what drew them to Hex. I'm happy to supplement anything or send resources if there's something they were interested in that I haven't covered. But if event tracking is a main deal breaker for the team, that's something we unfortunately don't assist with. Any data living in a data warehouse, we can connect to that and you can analyze it.

**Bianca Nieves:** So it's definitely meant for data analysis, just not for tracking. Got it.

**Tory Zehnder:** Okay. This makes sense. And do you have a data warehouse where you store data?

**Bianca Nieves:** As of right now, we don't. I've used Segment in the past and probably will implement something similar. But at the moment, we don't — only for our clients, not for GrowthX HQ.

**Tory Zehnder:** Got it. Okay.

**Tory Zehnder:** Yeah, just curious because to use Hex, you'll need a cloud-based data warehouse. Your data needs to live in Snowflake, Databricks, Redshift — something like that — so we can connect to it and have data to work with. Just wanted to call that out. In terms of next steps, I have a bunch of async resources — product overview, product demo, additional demo recordings, documentation, and videos. I can pass these along to you and your counterparts. But before you take next steps, I'd want you to check with the team on two things: whether event tracking is a deal breaker, and whether it's possible to get a data warehouse set up.

**Bianca Nieves:** Yeah, let me have that conversation with the team. I'll take this back, look at those async resources, and chat with them later today. I can probably get back to you by end of week. If we decide we're going to build this out eventually, we'll continue the conversation. If not, we'll pause and pick it back up when it's time.

**Tory Zehnder:** Yeah.

**Tory Zehnder:** Okay, that sounds great.

**Tory Zehnder:** Well, sounds good.

**Tory Zehnder:** Well, I'll send that over after this call, just so you have that.

**Tory Zehnder:** And you can kind of sit with that information and take that back to them.

**Bianca Nieves:** And yeah, looking forward to hearing from you later this week.

**Bianca Nieves:** Awesome.

**Bianca Nieves:** Awesome. Thanks so much for the time, Tory. This is great.

**Tory Zehnder:** Of course. Great meeting you.

**Bianca Nieves:** Same here.

**Tory Zehnder:** All right. Thanks. Bye.
