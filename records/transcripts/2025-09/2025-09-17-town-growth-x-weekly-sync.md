# Town <> Growth X - Weekly Sync

<metadata>
date: 2025-09-17
time: 18:01 UTC
duration: 31 minutes
organizer: Kyle Gaudreau
participants: Kyle Gaudreau, Ehtisham Hussain, Pier, Ryan Johnson
fathom_recording_id: 87968829
fathom_url: https://fathom.video/calls/412152338
share_url: https://fathom.video/share/rJgc22q6HmqSi2H9EqgTSocQNzYY1D_s
source: fathom
enriched_on: 2026-03-03 16:30 UTC
</metadata>

---

## Summary

GrowthX and Town reviewed blog traffic trends, event analytics, and content strategy alignment. Overall traffic is growing but remains volatile week-to-week; the team agreed building consistent traffic is priority one before optimizing for conversions. Immediate action items include setting up GA4 tracking for key conversion events (visits to app.town.com, sign-ups), giving GrowthX access to PostHog analytics, and experimenting with table of contents, author bios with booking links, and middle/bottom-funnel content (case studies, expert interviews) alongside high-volume keyword targeting for e-commerce and real estate verticals.

---

## Context

Town is a CPA + AI platform for tax and accounting services. GrowthX is running Town's content marketing strategy with a focus on organic traffic growth through blog content. This is a recurring weekly sync to review analytics, content performance, and strategy alignment. The relationship is service-based — GrowthX owns strategy and content production, while Town handles approval workflows, publication, and analytics integration from their platform side.

---

## Relevance

**To GrowthX Delivery:**
- Blog traffic growing but volatile — team prioritizing consistency before funnel optimization
- Event analysis approach (comparing week-to-week vs. 4-week rolling average) to account for Google's testing behavior
- Author attribution strategy to build topical authority (Google E-E-A-T signals) — tying blog content to expert bios
- UX experiments in flight: table of contents (low-hanging fruit for engagement/SEO), inline CTAs, author booking links
- New content format experiments: case studies, expert interviews, behind-the-scenes pieces (middle/bottom funnel)

**To GrowthX Business Development:**
- Town is actively tracking conversion funnel (form starts, sign-ups, onboarding completion) — signals engaged account health
- Analytics maturity growing: Town moving from Google Analytics only to integrating PostHog for downstream funnel tracking
- Expansion opportunity: Town planning higher-volume keyword experiments in e-commerce and real estate verticals
- Decision framework emerging: Town now defining ideal customer journey (from organic → site behavior → onboarding) — positions GrowthX for scope expansion

---

## Overview

- Blog traffic is growing but still volatile; building consistent traffic remains the top priority
- Event analysis shows good engagement (4 page views on average) but low click-through rates on CTAs
- Need to better define and track key conversion events (e.g., visits to app.town.com, sign-ups)
- Experimenting with middle/bottom funnel content and UX improvements planned alongside high-volume keyword targeting

---

## Key Topics

### Traffic and Engagement Analysis

  - Overall website traffic (impressions and clicks) is trending positively
  - Blog traffic shows alternating weeks of high engagement vs. broader reach
  - Good engagement metrics: 4 page views on average, high scroll rates
  - Low click-through rates on internal links and CTAs
  - Seed announcement article driving significant traffic, but may not be ideal audience

### Content Strategy and Experimentation

  - Continuing focus on building consistent traffic through informational content
  - Planning to experiment with middle/bottom funnel topics (case studies, expert interviews, behind-the-scenes content)
  - Considering UX improvements: table of contents, inline CTAs, author bios with booking options
  - Upcoming high-volume keyword topics for e-commerce and real estate verticals

### Analytics and Tracking

  - Current reliance on Google Analytics for website data
  - Need to integrate PostHog data for better insight into user journey and conversions
  - Goal: Track why users visit the site, what they do, and how many sign up
  - Action item: Set up GA tracking for key conversion events (e.g., visits to app.town.com, onboarding URL)

### Content Production Workflow

  - Two articles ready to publish, five more under review
  - New batch of topics coming this week, including middle/bottom funnel proposals
  - Shifting to discuss content production over Slack, focusing meetings on metrics and insights

---

## Action Items

**Ehtisham Hussain (GrowthX)**
- Propose middle/bottom funnel topics
- Investigate form start triggers in GA and how they work
- Implement table of contents for published blog posts

**Pier (Town)**
- Give GrowthX access to PostHog analytics
- Review 5 pending blog posts
- Review and approve author bios for publication
- Check with team members for approval to publish author bios
- Determine GA implementation method (Google Tag Manager vs hard-coded)

**Kyle Gaudreau (GrowthX)**
- Analyze search queries leading to seed announcement page

---

## Transcript

**Kyle Gaudreau:** You're well. How about yourself?

**Kyle Gaudreau:** Good, about yourselves, I should say?

**Pier:** Yeah, ourselves.

**Kyle Gaudreau:** This meeting is being recorded. I was having a little technical difficulties with Zoom, so we'll try to work through it. I don't know what's happening with Zoom today. All of a sudden it's giving us conflicting host things. Our same system we've used for weeks all of a sudden doesn't work today. So, always fun.

**Pier:** Okay, I'm glad it's not just me. I was having some trouble logging in, so you're making me feel a little better.

**Kyle Gaudreau:** Oh, okay. Maybe it is just a Zoom thing, then. Oh, there's Ehtisham.

**Pier:** Cool. I'm excited by this agenda.

**Kyle Gaudreau:** Glad to hear that. Yeah, we're working on continuing to try to make this better and better each and every week, so feedback is always welcome. To me, the thing that should never be done is to stop improving it, and just make sure we're sharing useful insights and getting useful feedback. Ehtisham, you want to dive in?

**Kyle Gaudreau:** Oh, looks like you're muted.

**Pier:** Oh, sorry, we can see your screen, but yeah, okay.

**Ehtisham Hussain:** I was talking this whole time. Okay, sorry about that. So let's get started.

**Ehtisham Hussain:** Like, we have a lot to cover today. So since we last met, we have published five more articles, and we have a lot more in the pipeline. Hopefully, we're going to catch up to the current date and then have multiple articles to publish in the bank. I need help with two shadow blogs. I shared the details on Slack. I created a shadow blog CMS the other day. I marked it as it's not going to appear on search engines or on the website, but I was really struggling with getting text to populate up there, and I need Tony's help with that. I also shared bio for Eht, so we can start attributing articles to one of our four experts. Every article should ideally be attributed to an expert to improve our rankings, because Google still checks for authority and we can build authority like that.

**Ehtisham Hussain:** One of the major action items from last week's meeting was to do an event count analysis because we have a lot of events set up in Google Analytics by default and we should analyze those. I'll quickly go over them. There are eight different events that are set up in Google Analytics: click, file download, first visit, form start, page view, scroll, and user engagement. Scroll is when someone scrolls to at least 90% of page depth. User engagement is staying on the page for more than 10 seconds or triggering different events.

**Ehtisham Hussain:** So when we look at the clicks, I took last week's numbers and compared them with the last four weeks' numbers. We don't get that many clicks on the blog. This is only exclusive to the blog, not for the whole website — just for the main blog page and all published blog posts. We don't get that many clicks, which means our internal links and CTAs at the end aren't getting clicked on much. We can encourage stronger and more visible CTAs, but this also ties into the intent of the user who has arrived at the blog. We do a lot of top-of-the-funnel informational content, and they're getting information right there. We're not asking them to click and go somewhere to get the information. There are two ways to look at it. One: it's working as designed. We're not asking them to click anything — we want them to go to the expertise page at the end, but they're not at that stage yet. Another: if we really want them to click and sign up for sessions with our experts, we can experiment with more visible CTAs.

**Ehtisham Hussain:** There are no file downloads, which is not a surprise. We don't have any files to download. We can experiment with branded checklists, but I don't think that's an immediate concern right now.

**Ehtisham Hussain:** We do get a bunch of first visits — 17 first visits last week, 71 if we look at the last four weeks. A lot of the first visits are coming through the seed announcement article, which is driving a lot of traffic on the blog. The detailed guides are creeping up and should overtake the seed announcement article in two to three weeks. The seed announcement seems to be something that people find of interest. We can experiment with that page — we know it's getting heavy traffic. We can put CTAs in there to encourage people to explore different articles or go to the expertise page, and hopefully divert that traffic to other pages where we want them to go.

**Kyle Gaudreau:** Just one quick clarification. The first visit number, I think, is a little bit lower than what we're seeing in terms of clicks, which is pretty normal with how many folks are blocking cookies. So I think in reality, the numbers are higher.

**Ehtisham Hussain:** Right, this is just what we can see in Google Analytics.

**Kyle Gaudreau:** Still hopefully this helps tell us some things directionally, but the numbers are likely going to be a bit lower than reality.

**Pier:** Okay. And these are all like out-of-the-box variables? Like, I don't think we've done any GA customization, right? So like form starts — I don't know if there's some out-of-the-box variables where we're pretty confident these are accurate.

**Kyle Gaudreau:** Like form starts — I don't know how confident we are. Like, do we know what that means?

**Ehtisham Hussain:** These are out of the box to the best of my knowledge, because we haven't done any customization.

**Pier:** Okay.

**Ehtisham Hussain:** All right. So with form starts — according to our last couple of conversations, that's the most important thing you guys want to track. People need to fill out forms and become leads. We don't get much of that — we got two form starts from the blog index in the last four weeks. It's almost no lead capturing, but it makes sense because we do a lot of top-of-the-funnel articles right now. We're just building traffic right now. We can experiment with middle-of-the-funnel and bottom-of-the-funnel topics, which I also mentioned at the bottom of this article and in the meeting agenda.

**Ehtisham Hussain:** While I was doing this, I got this idea: if you're going to add author bios, we can put the authors' calendars right there — like a calendar link where someone could sign up for a one-on-one session, if that's something you guys do. Someone's reading an article attributed to, say, Ludmilla, and they get useful information but have questions — they can directly sign up to talk to the author. That could increase form fills.

**Pier:** We have to talk about whether we want to try something like that. It's a really fair call-out. I think we're constantly having a conversation about how much we lean into the human element versus not, and that would be a decision point there. I don't even know where that data would go. Yeah, I think we should assume that data is bad — I'm not sure where it's going to — but the point around engagement and thinking about how we would leverage it is well taken.

**Ehtisham Hussain:** Yeah, and as Kyle said, these are indicators. Not going to be exact numbers, but indicators. I can take this as an action item and look into form starts — how they trigger and everything.

**Kyle Gaudreau:** I think the key thing here is we can start to work back a bit from where you all need to go in terms of your targets. What do you need from organic? We align on the key leading indicators, track them, and report back on what we're seeing from our content that connects to those targets. Depending on where we're at, how does that inform our strategy?

**Pier:** We'd love to build that more and more so it feels more connected to where you're all trying to go. Yeah, 100%. I think there's a bit of a back-solve here — we probably need to better define our ideal customer journey from campaign to what happens on the site to what we want to experiment with. And on the forecasting side, what's happening on our side is we're trying to figure out, as we hire humans to support the tax process, what that acquisition number should look like with the other committed deals we have. In the next one to two weeks, there might be more to share about what we'd want from organic.

**Kyle Gaudreau:** But I think this is good for us because it makes me realize we have some work to do to define even something like form starts. What's happening there?

**Kyle Gaudreau:** That makes sense.

**Pier:** We just want to layer in some other tests. We talked about some higher-volume tests and higher-volume keywords. We can sprint on some middle-funnel stuff.

**Kyle Gaudreau:** I'm just trying to connect the dots. We can certainly have runway to execute while you're all working on that forecast.

**Pier:** Yeah, just most of the actions so far make sense to me. The key thing from the users that we want to see is they go to app.town.com. If someone goes to app.town.com, they're either starting the onboarding flow or creating an account. That's where it gets interesting for us. I don't know if that's being tracked. And I don't even know if we're putting Google Analytics on app.town.com versus town.com. We may not even have it there. That's probably one thing we should do. And then the question is, do they actually complete through the sign-up flow? We have those analytics in PostHog. I don't know how we hook that up to your Looker or to GA.

**Kyle Gaudreau:** There's something to be done there so you get a better picture of who's actually activating. Is that something we could get access to, or like a limited dashboard?

**Pier:** Yeah, we can give you access to PostHog. Can you put that on the to-do list?

**Kyle Gaudreau:** Yep, no problem. Yeah, the better we can get a sense of that funnel, the better. At the very least, we should be able to track the initial event and configure it correctly. We can explore the right way of tracking and mapping this journey.

**Ehtisham Hussain:** Is it PostHog?

**Pier:** Yeah, PostHog.

**Kyle Gaudreau:** We have a few other customers who use that as well.

**Ehtisham Hussain:** All right, so page views — that's something we are doing really good at.

**Ehtisham Hussain:** Like once the users come in, they explore on average four pages, which is really solid. We don't want people to come in and leave within a few seconds. It means they're spending more time and exploring more pages. If we want to improve that, we can enhance internal linking. But I don't see this as a big concern right now because we're already doing a bunch of internal linking and doing well. Plus, they're exploring on their own — going back to the blog and exploring different articles, spending more time on the page.

**Ehtisham Hussain:** Scroll rates on the guides suggest light-skimming rather than deep read-throughs, but that's expected. In a really long-form article with 30 e-commerce topics, not everyone's going to read every subheading. People usually look for specific information, so light-skimming is normal. But here's an interesting idea: we can start including a table of contents with clickable headings at the top after the introduction. That's a really low-hanging fruit — I can do it for all published blogs immediately. People can click on the subheading they want and read the information there.

**Kyle Gaudreau:** I'd say the best thing to do here is let's run some experiments around different formats of this. Yes, it can help with general engagement and SEO, but some of these principles can work well for AEO as well. Let's pick a couple of articles and test it — hopefully not much from a web dev standpoint. We can weigh impact for effort here.

**Ehtisham Hussain:** All right. And then for session starts — the blog hub, the main town.com/blog, that's bringing in a lot of traffic as an entry point. I don't recommend doing anything extra there because it's working as intended. People are going there, exploring, clicking on the articles they want. And then engagement-wise, we're doing well. Once someone visits the page or any articles or the blog hub, they stay and explore multiple pages. That's something you'll see in the traffic analysis as well.

**Ehtisham Hussain:** So the next immediate steps are what we discussed above. These are possible ideas — we're not going to do all of these at the same time immediately, but we can experiment with table of contents, middle and bottom-funnel topics, and inline CTAs.

**Ehtisham Hussain:** That was the event analysis, which gives us a view of what users are doing as they visit the website. Overall traffic is positive — this is not just blog traffic, this is overall website traffic. Impressions and clicks are compounding and getting up. We're getting traffic — people are coming to the website. When we dive deeper into blog traffic, there's an interesting trend: every alternate week, Google tests the website with different audiences. Some weeks we get fewer views but highly engaged visitors. Other weeks we get more views but less engagement. Right now, organic traffic on the blog is volatile, but as we publish more, we'll build toward stability.

**Ehtisham Hussain:** Building traffic still remains priority number one. Kyle and I discussed this before the meeting, and we agreed that building traffic is priority one right now, not going directly for MQLs and signups.

**Kyle Gaudreau:** Yeah, basically, it's not either/or — it's doing some of this in parallel. I just want to be sure we're not trying to go too far down funnel when we still haven't cracked consistent traffic. I think we can experiment with middle and bottom funnel, but I'd love to explore how we get some higher-volume experiments going. We focused on lower-difficulty, lower-volume keywords, which is giving us something. If we continue to improve engagement there, it should compound. But I don't want to assume we can't win at more difficult things.

**Pier:** And that could be valuable on the AEO side as well. I'm looking at the weeks where we have less active engagement but more top-of-funnel. Is that where active users are 35% of the total versus 40-50%? It doesn't seem that different to me.

**Kyle Gaudreau:** I think at this phase, it's normal week-to-week fluctuation. Google's testing the website, seeing what the engagement is, and naturally seeing some fluctuations. At the end of the day, it's about the trajectory being consistently up and to the right. If we're on that trajectory, I care less about week-to-week and more about the overall direction. There are certainly some things building from an impression standpoint. My hunch is we need to play slightly more aggressive bets to get traction.

**Pier:** Okay.

**Ehtisham Hussain:** And to add to that, we're working off a small data set right now, so even five or ten users will throw off the entire analysis by a big percentage.

**Pier:** Okay.

**Ehtisham Hussain:** All right, covered the traffic. So the next items are some UX items I discussed: inline CTAs, putting author bios, maybe giving readers the ability to book a one-on-one session. And then another experiment we want to run in parallel to the high-volume keyword topics coming your way. We've already covered some — we've sent you the e-commerce titles batch, and real estate ones are up next. I'm going to ask for approval on those topics on Slack, and then we can experiment with case studies, expert interviews, and a behind-the-scenes of Town's CPA + AI model. We'll need your in-house resources. We can do async or one-on-one interviews, record those, and turn them into articles.

**Ehtisham Hussain:** If we have case studies where Town helped a real estate investor or dental practice, and they're happy to go public with their names and face, they'll get a backlink and we get a good story. It could also be good for your sales organization and distribution. These three types of assets can help you get leads.

**Pier:** I also wonder if that's part of why people are visiting the seed announcement — we don't say who we are or our point of view on the market anywhere else on the site. How are they finding the seed announcement?

**Ehtisham Hussain:** They're mostly coming directly to the seed announcement through Google. A lot of people are directly coming to the blog through Google as well. All the traffic I analyzed was narrowed down to organic traffic, so it doesn't contain direct or referral traffic.

**Kyle Gaudreau:** They're coming through Google. Are you familiar with the queries? Like, are people searching for broad Town-related searches?

**Ehtisham Hussain:** I haven't looked into the keywords yet.

**Kyle Gaudreau:** Yeah, we should dig into that. That's an interesting hypothesis.

**Ryan Johnson:** Yeah, I see it all the time. I go to our pricing page and google "town.com pricing," which gives the pricing link at the top, but the very second result is our seed announcement blog.

**Kyle Gaudreau:** Yeah, there's probably something to dig into. What are the subtopics bubbling up that might be better suited with more directly relevant content targeting that intent? We can dig in to see if we find some patterns.

**Pier:** The problem is that page is probably driven by VCs and people who heard about the fundraise. We should look at the search terms because it might just be terrible traffic for us.

**Kyle Gaudreau:** Could be. I'm just curious if there's anything else bubbling up that could be more directly relevant traffic. But we can validate that.

**Pier:** Thank you. In the remaining time we have, could we look at the action items and next steps, and on the content cycle — Sean, I remember last week you said you'd keep reviewing one a day. Is that still the cadence?

**Ehtisham Hussain:** I'm not doing it daily, but there are two ready to publish. Those are the shadow blogs we need.

**Pier:** And then I have five more to review over the next few days. That gets us to five published. We have enough topics approved to start, though we're getting a little thin.

**Ehtisham Hussain:** Yeah, but I'm going to populate that this week. We'll get a bunch of new topics. I'm going to explain why we want to do them. And then I'm going to propose some middle and bottom-of-funnel topics as well.

**Pier:** All the middle and bottom-of-funnel topics are things we can definitely use in the field. It's just a matter of prioritizing them with the tax team's time. And then we owe you guys the author bio reviews. I think we should be able to do that. I also need to check with people if they're okay with that happening.

**Pier:** Is there anything else from the GrowthX side? It sounds like post review, the shadow blog topic, and author bio reviews are the immediate things you need from us.

**Ehtisham Hussain:** Yeah, that's right. If we can get the shadow blog up and running, then we can start doing one or two articles every week and track them.

**Pier:** Okay. Guys, I appreciate the pivot to some analysis and giving us a sense of where we are in the growth journey. That's very helpful. I'd love to keep this framing as we look at the content input-output cycle.

**Kyle Gaudreau:** Yeah, great.

**Ehtisham Hussain:** What we want to do is handle production over Slack — here's the next batch and we published the previous batch. We don't talk about production as much in this meeting and focus on the numbers and what we learned.

**Pier:** Okay. Well, I know we're almost at time. One thing I forgot to mention is we also need to give you access to PostHog. That's the other thing we need to do.

**Kyle Gaudreau:** One of the things I found helpful is thinking through what questions we want to be answering week to week and aligning on that. Then we can look at our data sources to see if we're enabled to do that today. Is there a gap we're missing? There are things we called out today we can run with, but that may help us assess whether this is a PostHog thing, a GA thing, or something else.

**Pier:** Yeah, for me it's pretty easy. We should find out why people are coming to the website, what they're doing, and how many end up signing up. I think we should add tracking to GA for when they go to the dashboard URL or onboarding URL. That's enough for now because it'll show us if content clusters get people to sign up. But right now there's a risk that we're tracking people who never sign up.

**Kyle Gaudreau:** Then that's where we spend more time. Do you all have Google Tag Manager, or is it hard-coded?

**Pier:** I don't remember. We use Framer for the website, so it's however Framer does it. My guess is hard-coded, but I don't know.

**Kyle Gaudreau:** Cool.

**Pier:** Thank you, guys. Appreciate the work.

**Ehtisham Hussain:** Appreciate it.

**Kyle Gaudreau:** Bye.
