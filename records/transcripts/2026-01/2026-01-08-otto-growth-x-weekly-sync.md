# Otto <> Growth X - Weekly Sync

<metadata>
date: 2026-01-08
time: 18:30 UTC
duration: 18 minutes
organizer: team@growthxlabs.com
speakers: Bailey Seybolt (GrowthX), Jason Flateboe (Otto)
participants: Jason Flateboe, Michael Gulmann, Erik O'Brien, Bailey Seybolt, Team GrowthX
fathom_recording_id: 112845186
fathom_url: https://fathom.video/calls/524334748
share_url: https://fathom.video/share/d7TZN6z7Uq4zyWsHHDvCmCx2adP_wS7v
source: fathom
enriched_on: 2026-02-28
enriched_time: 14:32 UTC
status: production
</metadata>

---

## Summary

Bailey and Jason discussed Otto's content strategy for 2026, addressing immediate content pipeline deliverables, a temporary FAQ schema fix, December reporting delays, and conversion tracking gaps on Otto's marketing site. The meeting established a shift to bi-weekly cadence focused on strategy and performance as the blog matures, with operational updates moving to asynchronous Slack communication.

---

## Context

This is a recurring weekly engagement between GrowthX (content marketing services) and Otto (travel planning AI startup). GrowthX provides content strategy, pipeline management, and performance reporting; Otto is responsible for site tracking, conversion metrics, and goal alignment. The meeting occurs post-holiday with both teams resetting workflows and planning alignment for 2026 initiatives. Otto's product exists as both a marketing site (Webflow, Google Analytics) and a core app (`app.ottotheagent.com`, Mixpanel tracking), creating a split tracking landscape that impacts reporting visibility.

The context for this sync includes: (1) recent content delivery ramping back up after the holiday pause, (2) discovery of a technical gap in FAQ schema generation that GrowthX is addressing manually while engineering automates it, (3) December reporting being low-signal for B2B decision-making, and (4) Jason flagging a critical gap in conversion tracking that prevents end-to-end funnel visibility from content to signup/login.

---

## Relevance

- **Immediate Content Delivery:** 5 articles queued for delivery this week; ongoing content pipeline velocity matters for blog performance tracking and user acquisition funnel.
- **FAQ Schema Fix:** Recent articles missing FAQ schema prevent search visibility; this is a critical technical debt in content publishing workflow that impacts SEO performance and needs engineering automation.
- **Conversion Tracking:** End-to-end funnel tracking gap is blocking attribution of signups/logins to content sources, preventing performance measurement of content effectiveness and 2026 strategy validation.
- **Cadence Shift:** Moving to bi-weekly cadence signals maturation of engagement and focus shift from tactical delivery to strategic performance analysis, suggesting the blog is delivering signal and warrants deeper analytics investment.
- **2026 Planning:** Alignment of content strategy with Otto's goals and KPIs is foundational for 2026 engagement effectiveness and competitive positioning.

---

## Overview

- **FAQ Schema Fix:** GrowthX is manually adding missing FAQ schema to recent articles, a temporary fix until engineering automates the process.
- **Reporting Delay:** December's performance report is delayed but will be sent async. Its data is expected to be low-signal due to typical B2B holiday traffic patterns.
- **Cadence Shift:** Meetings will move to a bi-weekly cadence to focus on strategy and performance. Project management updates will now be sent asynchronously via Slack.
- **Conversion Tracking Gap:** Jason identified a critical gap in Webflow conversion tracking (GA) and will investigate if existing Mixpanel data can fill it.

---

## Key Topics

### Content & Reporting

  - **Content Pipeline:** 5 articles are queued for delivery this week.
  - **FAQ Schema Issue:**
      - **Problem:** Recent articles are missing FAQ schema, preventing the content from appearing in search results.
      - **Cause:** A new, manual process for generating and adding the schema was missed during publishing.
      - **Solution:** GrowthX is manually updating all affected articles.
      - **Automation:** Engineering is working to automate this step by connecting the content pipeline directly to the CMS.
  - **December Performance Report:**
      - **Status:** Delayed; Bailey will send it async tomorrow.
      - **Insight:** December is a low-signal month for B2B traffic, making the data less actionable for strategic decisions.

### Operational Updates

  - **2026 Goals Planning Session:**
      - **Purpose:** Align content strategy with Otto's 2026 goals and KPIs.
      - **Timing:** To be scheduled in \~2 weeks to allow for internal goal-setting and to ensure Michael can attend.
  - **Meeting Cadence Shift:**
      - **New Cadence:** Bi-weekly meetings.
      - **Rationale:** Shift focus from project management to higher-level strategy, performance analysis, and conversion optimization as the blog matures.
      - **Asynchronous Updates:** Project management details will be sent via Slack every Monday.

### Conversion Tracking Gap

  - **Problem:** No end-to-end conversion tracking exists for the Webflow marketing site (GA), preventing attribution of sign-ups/logins to content sources.
  - **Context:**
      - **App Tracking:** The main app (`app.ottotheagent.com`) is tracked correctly in Mixpanel.
      - **Site Tracking:** The marketing site uses Google Analytics (GA).
      - **Ownership:** Jason will work with the original GA contractor to implement tracking, likely via Google Tag Manager (GTM).
  - **Potential Solution:** Investigate if Mixpanel, which tracks the entire domain, already captures the missing conversion data.
  - **GrowthX Support:** GrowthX can provide best practices or connect Jason with an internal expert if needed.

---

## Action Items

**Bailey Seybolt (GrowthX)**
- Send 5 queued articles to Jason for publishing this week
- Send December monthly performance report to Jason (async via email/Slack)
- Schedule 2026 goals planning session with Jason for ~2 weeks out; ensure Michael Gulmann can attend

**Jason Flateboe (Otto)**
- Set up GA4/Google Tag Manager conversion tracking for sign-up and login buttons with contractor; share configuration with Bailey once complete
- Investigate Mixpanel tracking coverage for Otto's marketing site (Webflow properties); determine if existing Mixpanel data already captures marketing site conversion events; share findings with Bailey

---

## Transcript
**Bailey Seybolt:** Happy New Year.

**Jason Flateboe:** Happy New Year.

**Bailey Seybolt:** How's it going?

**Bailey Seybolt:** Good.

**Jason Flateboe:** How are you doing?

**Jason Flateboe:** Good.

**Jason Flateboe:** How was your trip?

**Bailey Seybolt:** It was pretty amazing.

**Jason Flateboe:** How's that?

**Jason Flateboe:** Tell me about it.

**Bailey Seybolt:** You know, I don't even know if I knew what to expect from the Galapagos except tortoises.

**Bailey Seybolt:** And that everyone says it's really cool.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** But we went on a boat, which is really cool because they often sail while you're sleeping.

**Bailey Seybolt:** And so we kind of wake

**Bailey Seybolt:** Up in a new island every day, which is pretty incredible.

**Bailey Seybolt:** And they had naturalists on the boat with us.

**Bailey Seybolt:** And so I think one of the most amazing things is having that guide really kind of put everything into context for you to like understand what it is that makes the ecosystem unique to like help you understand what you're seeing.

**Bailey Seybolt:** So I think to me, like getting that deeper understanding was one of the coolest parts beyond just like, oh, my God, you're swimming with baby sea lions, which is like, oh, my God, that's cool.

**Jason Flateboe:** Yeah, I could imagine having that person kind of educating you in a social way is much better than having like your nose and like a guidebook the whole time trying to like figure stuff out because you want to be learning and understanding what you're seeing and stuff.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** And they're talking about, you know, how like the ocean, like learning how ocean currents work with the cold and warm air, which is like, or cold and warm water, which is how you get this kind of unique ecosystem.

**Bailey Seybolt:** So I felt like I was like living inside a National Geographic episode.

**Bailey Seybolt:** So it was very cool.

**Bailey Seybolt:** And then like being able to see that stuff in person.

**Bailey Seybolt:** I've never been a huge snorkeler. I get kind of like nervous around the big fish.

**Bailey Seybolt:** But for some reason, it felt like the sharks there were like friendly sharks. You're like swimming with sea lions and penguins, but also the sea turtles and all these like tropical parrotfish and stuff.

**Jason Flateboe:** That's cool.

**Jason Flateboe:** So how many islands are there?

**Bailey Seybolt:** We, I think we, they sort of, they often split it between like kind of the east and the west Galapagos.

**Bailey Seybolt:** And often you'll take a trip kind of on one or the other.

**Bailey Seybolt:** I'm not sure if one's like better than the other.

**Bailey Seybolt:** I think we were on the kind of eastern side and we mostly sailed around like, I think there was like four or five main islands.

**Bailey Seybolt:** And then there's a lot like smaller ones kind of off of there.

**Bailey Seybolt:** But it's such a wild landscape because some of it is so new because the volcanic activity is so active.

**Bailey Seybolt:** So there was one island that I think was only like, the part we were on was only like 100 years old or something.

**Bailey Seybolt:** So it looks like just this black volcanic, honestly, you look like you're on another planet, this kind of like wasteland.

**Bailey Seybolt:** And then you have other islands that are kind of much more established, you know, old volcanoes.

**Bailey Seybolt:** But I think because it's active, you know, it's like there would be volcanoes, islands that were separate islands, but then they became one island.

**Bailey Seybolt:** So you have these unique populations of birds and stuff on either side of the island.

**Bailey Seybolt:** So you can understand why Darwin showed up and felt like he had finally like found the place to study his theories.

**Bailey Seybolt:** But yeah, that part is a, it is pretty crazy.

**Bailey Seybolt:** Like there was some event, I think, like in the last hundred years where because of that volcanic activity, I guess the seabed actually rose like 30 feet.

**Bailey Seybolt:** And so this whole coral reef just lifted up and it was so fast that I guess someone showed up to the island and there were like dead sharks and dead fish all over it because they hadn't been able to escape this event.

**Bailey Seybolt:** So it is just like, it's such a wild, wild landscape.

**Bailey Seybolt:** So if you ever get the opportunity.

**Jason Flateboe:** I would like to.

**Jason Flateboe:** I imagine that took quite a while just in transit, right?

**Bailey Seybolt:** Do you have to go to Ecuador?

**Bailey Seybolt:** Oh God, yeah.

**Bailey Seybolt:** Like getting there, I feel like it took, I feel like it was a journey.

**Bailey Seybolt:** And especially on the way, the way home was right after our, the U.S.

**Bailey Seybolt:** activity in Venezuela.

**Bailey Seybolt:** So I think we like woke up that morning and were supposed to leave to the news.

**Bailey Seybolt:** And so I think travel everywhere was kind of messed up that day.

**Bailey Seybolt:** But yeah, you have to, you have to get to Ecuador.

**Bailey Seybolt:** I'm sure if you don't live in like small town Vermont, it's a lot easier to get to.

**Jason Flateboe:** Oh my gosh, that's yeah.

**Jason Flateboe:** Like from Seattle, I'm 15 minutes away from the major airport.

**Bailey Seybolt:** Yeah, I think you'd probably, it's probably not.

**Bailey Seybolt:** Quite as much of a journey as everything is a journey for us.

**Jason Flateboe:** Wow.

**Jason Flateboe:** Very cool.

**Bailey Seybolt:** Bia, how was your holiday?

**Jason Flateboe:** It was good.

**Jason Flateboe:** It was pretty mellow.

**Jason Flateboe:** We just hung out here and took some time off and we had some family come in and stay with us and stuff.

**Jason Flateboe:** So it was just chill.

**Bailey Seybolt:** I appreciate the holiday chill.

**Bailey Seybolt:** That's usually what our holidays look like.

**Bailey Seybolt:** And actually, there's some things that feel more kind of refreshing, I think, about not trying to accomplish a lot.

**Bailey Seybolt:** I'm just like enjoying the time with friends and family that feels restorative in a very different way.

**Bailey Seybolt:** Yeah, I think it's always the grass is always greener.

**Jason Flateboe:** And, you know, I came away going, oh, maybe I want to travel next year.

**Jason Flateboe:** Because there's just so much of like sitting around at home and not to complain, but sometimes you just want to mix it up a little bit.

**Bailey Seybolt:** But like, yeah, it is true.

**Bailey Seybolt:** The grass is always greener.

**Jason Flateboe:** Yeah.

**Bailey Seybolt:** Let me jump in and we can.

**Bailey Seybolt:** And remember who we are.

**Jason Flateboe:** Yeah, totally.

**Bailey Seybolt:** So I think you have, we've got five articles queued up coming your way today or tomorrow for this week.

**Bailey Seybolt:** We've still got a good runway of topics.

**Bailey Seybolt:** One thing I will note, there was a few articles being published that are missing the FAQ.

**Bailey Seybolt:** We're making some manual updates to that schema.

**Bailey Seybolt:** So if you see a few that are missing, we're on it and we're updating it now. Basically, until we automate publishing, which we're in the process of doing, there are some manual updates we need to make to add that schema.

**Jason Flateboe:** So just to understand that.

**Jason Flateboe:** So the FAQ content was written and included in the post, but it just wasn't showing up because of the technical thing.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** Exactly.

**Bailey Seybolt:** It wasn't showing up because right now we have to manually generate the schema and then add that.

**Bailey Seybolt:** When we staged the post and that step got just missed on our end because it was a new process.

**Bailey Seybolt:** So I think we should, we're hoping our engineering team is working on having that just automatically generate when we kind of connect our pipeline directly to your CMS.

**Bailey Seybolt:** But right for the interim, the plan is to just manually do that.

**Bailey Seybolt:** And so we just didn't do that.

**Bailey Seybolt:** So we need to go back and update that.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** And then also I know we owe you sort of our monthly reporting.

**Bailey Seybolt:** We're a little behind this week just because of everything.

**Bailey Seybolt:** So I'm going to send that to you async tomorrow.

**Bailey Seybolt:** And then if you have any questions, we're happy to answer on Slack or we can kind of walk through it next week instead.

**Bailey Seybolt:** But honestly, December is such a weird month for website traffic that it's kind of like a bad month to base any insights.

**Bailey Seybolt:** Unless you like, you know, you're a B to C.

**Jason Flateboe:** Yeah.

**Jason Flateboe:** The-commerce company selling something that people are buying for Christmas.

**Jason Flateboe:** Which we are not.

**Bailey Seybolt:** Yeah, exactly.

**Bailey Seybolt:** For B2B, I feel like it's a bad traffic month.

**Bailey Seybolt:** Yeah, nobody's booking their business trip.

**Bailey Seybolt:** Yeah, exactly.

**Bailey Seybolt:** Christmas.

**Bailey Seybolt:** If you sell toys, then you had a great month.

**Bailey Seybolt:** Then just in terms of a couple ops things, one, I think I mentioned this before, but we're sort of scheduling out these 2026 goals planning sessions, ideally around when you're having these conversations internally.

**Bailey Seybolt:** And just to give us a better sense, it's a good time to take a look at our strategy, kind of take a look at your goals and your KPIs, and just look and make sure that the strategy is still sound, especially for you as you've launched, like if you have other insights and other things we should be thinking about.

**Bailey Seybolt:** It's just, I think...

**Bailey Seybolt:** For everyone, you know, January is a good time to sort of think big picture about some of these.

**Bailey Seybolt:** So we'd love to, when you're ready and around when you're having these conversations internally, just kind of put a planning session on the calendar to talk through how we can support your goals.

**Jason Flateboe:** Okay.

**Bailey Seybolt:** Yeah, sounds good.

**Bailey Seybolt:** Oh, and then one other ops things where we, I think I might've mentioned this before we went, but I think we're, we're planning to shift our meeting cadence to more of a bi-weekly cadence and to try to focus that time more around, you know, strategy insights, like content performance, especially as your blog gains more traffic, then we kind of move from early signals into hopefully planning how we can like talk more about conversion and other goals that you have and how we can kind of support that from a strategy perspective.

**Bailey Seybolt:** So the, the new cadence would sort of.

**Bailey Seybolt:** Still, we're obviously available on Slack, and the plan would be to send an update every Monday with sort of more of the project management things that this covers in terms of what content we're working on, what we're doing this week, any action items, and then also send a recap after meetings.

**Bailey Seybolt:** So hopefully the goal is that a lot of that more project management stuff can happen async and on Slack so we can use this time for our strategy.

**Bailey Seybolt:** And as we go, if we find we want fewer but longer meetings, too, we can expand those to accommodate.

**Jason Flateboe:** Great.

**Jason Flateboe:** Yeah, that all makes sense.

**Bailey Seybolt:** Sounds good.

**Bailey Seybolt:** Great.

**Bailey Seybolt:** Well, that was kind of everything I had on my side.

**Jason Flateboe:** Was there anything else on your mind?

**Jason Flateboe:** Um, no, not really.

**Jason Flateboe:** Um, you know, one, one thing that just, I, I, as an FYI, I should probably throw past you for, for, uh, metrics and reporting.

**Jason Flateboe:** We don't have things set up kind of end-to-end on the funnel for the conversion clicks, like on the button for, you know, logging in, signing up, et cetera, which is obviously problematic.

**Jason Flateboe:** Like, we want to get more of a view of, like, of those people who are actually signing up and logging in, like, where are they coming from and, you know, just kind of 101 stuff.

**Jason Flateboe:** We had some tracking set up prior, before I kind of exploded the forms and the buttons, so it's kind of on me. I've changed things, but we had a different guy who sort of set up all of the GA stuff. So I need to make sure that that is set up properly, and I'm going to have to work with him, but that's top of mind for me so that we can actually get a full view, kind of end-to-end.

**Bailey Seybolt:** That makes sense.

**Jason Flateboe:** So we have Mixpanel for our actual app, right? So that's all configured. So when people actually start using Otto and they're planning trips and they're doing all the things, that's showing up in Mixpanel and we have a good view of that.

**Jason Flateboe:** But that is a separate site from the Webflow, right?

**Jason Flateboe:** So Webflow, we're using Google Analytics and that's where the work needs to happen.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** Well, that's useful to know.

**Bailey Seybolt:** And I think once you've sort of streamlined that, it for sure I think makes sense to, I think, walk us through it to make sure.

**Bailey Seybolt:** I mean, I think anything in our look or anything updates you make in Google Analytics should be automatically reflected.

**Bailey Seybolt:** But just to make sure we're kind of tracking the right metrics there and giving you, I think, the right visibility.

**Bailey Seybolt:** And then, yeah, in terms of conversion and...

**Bailey Seybolt:** And those journeys, I too, I think that, yeah, understanding what you're looking at and what your goals are and any visibility we can give you in terms of how content is sort of affecting that journey.

**Bailey Seybolt:** I think once that's all set up, that's probably a good time to bring us back in and just kind of take a look at all of that again.

**Jason Flateboe:** Yeah, yeah, that makes sense.

**Jason Flateboe:** And I guess from your perspective, just let me know if you're seeing holes in the metrics and reporting. Other than the one that I just identified, let me know and we can work through those together.

**Bailey Seybolt:** Yes, for sure.

**Jason Flateboe:** My plan was, and I'm by no means an expert in setting this up, but I think what I need to do is go into Google Tag Manager and set up, like, custom tags to, for those buttons and links.

**Jason Flateboe:** And so that was my plan there.

**Bailey Seybolt:** I'm also by no means a master at setting them up, but I'm sure we have someone on our side who does have more experience in that. So if you have questions around that or best practices, let me know. I might not be the right person to talk to, but I bet we have that person somewhere at GrowthX, and I'm always happy to track down more info for you.

**Jason Flateboe:** Got it.

**Jason Flateboe:** You know, I'm just rethinking what I said earlier and I should add clarification. The Webflow site is separate and different from our app, but they both live on the same domain. Our actual product is app.ottotheagent.com. So as I'm thinking about this, we probably do have static website, marketing website, landing page stuff that might be in Mixpanel.

**Bailey Seybolt:** I should look at that because we might actually be capturing some of that.

**Bailey Seybolt:** I mean, I don't exactly know how they talk to each other, but this feels like it must be a pretty common question for people, and there must be a way to get greater visibility and to kind of use your journeys across that.

**Jason Flateboe:** Yeah, and because they're on the same domain, I don't see any reason why it wouldn't be available altogether.

**Jason Flateboe:** So I'll poke at that a little bit.

**Bailey Seybolt:** Okay, all right, that sounds good.

**Bailey Seybolt:** And yeah, just let me know if you have questions around best practices or around setting that up to give better visibility into those.

**Jason Flateboe:** Yeah, and I'll work with him. I haven't had this conversation yet with my team. He's a third-party contractor, but I'll try to figure it out on our side before I flag anything for your side.

**Bailey Seybolt:** All right, that sounds good.

**Jason Flateboe:** Yeah.

**Bailey Seybolt:** All right.

**Jason Flateboe:** Well, that was it for me. Anything else?

**Bailey Seybolt:** Okay, yeah, that's all I have.

**Bailey Seybolt:** Okay, that sounds good. Oh, and then yeah, just let me know if you'd like me to set up this planning session. I'm happy to put something on the calendar.

**Bailey Seybolt:** Or if you want to kind of wait and have those conversations more internally, we can revisit it in a couple of weeks, too.

**Jason Flateboe:** Why don't we go ahead and put something on the calendar in a couple of weeks?

**Jason Flateboe:** I think that would be good.

**Jason Flateboe:** And that'll give Michael enough time to make sure he can attend.

**Bailey Seybolt:** That sounds great. All right.

**Jason Flateboe:** All right.

**Bailey Seybolt:** Thanks very much.

**Jason Flateboe:** Talk to you soon.

**Bailey Seybolt:** See you later.

**Jason Flateboe:** Bye.
