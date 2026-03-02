# Navan <> GrowthX Deep Dive (Nima Asrar Haghighi)

<metadata>
date: 2025-11-24
time: 22:04 UTC
duration: 58 minutes
organizer: erik@growthx.ai
participants: Erik O'Brien (GrowthX), Nikita Schaub (Navan), Nima Asrar Haghighi (Navan)
fathom_recording_id: 104026749
fathom_url: https://fathom.video/calls/483507423
share_url: https://fathom.video/share/DPPy6zuuYu_y8MBexvjNrQKifpd_jFeX
source: fathom
enriched_on: 2026-03-02 14:30 UTC
</metadata>

---

## Summary

Erik O'Brien and the GrowthX team conducted a deep technical dive with Navan's product team (Nikita Schaub and Nima Asrar Haghighi), exploring Navan's end-to-end travel and expense management platform — including personal travel, rail booking, admin dashboards, proactive expense controls, and group event management. The team discussed how Navan's "traffic light" policy system and actionable admin reporting differentiate the platform, and agreed to incorporate insights from the deep dive into GrowthX's content strategy, with Nikita committing to share documentation on Navan's payments functionality.

---

## Context

Navan is a modern travel and expense management platform competing in the fragmented TME (Travel and Expense) market dominated by legacy players like Concur. GrowthX is developing content strategy around Navan's platform capabilities as part of an ongoing engagement. This meeting was a scheduled deep dive to understand Navan's product positioning, technical architecture, and key differentiators — specifically how features like personal travel rewards, proactive expense controls, admin dashboards, and group event management create competitive advantage. Erik O'Brien led the session with support from the broader GrowthX content team, while Nikita Schaub (based in San Francisco, recently relocated from London) and Nima Asrar Haghighi represented Navan's product side. The session was part of ongoing collaboration to ensure GrowthX's content accurately reflects Navan's value proposition for AEO and broader awareness-building initiatives.

---

## Relevance

**To GrowthX Delivery:**
- Navan's "traffic light" policy system (Green: auto-approve, Orange: flag, Red: auto-decline) is a key messaging angle for proactive spend control at the point of swipe — eliminates retroactive expense workflows that are friction points for customers.
- Admin dashboard reporting (benchmarks, out-of-policy spend lists, live traveler map) demonstrates actionable data as a differentiator — content should emphasize how this enables proactive program management vs. reactive reporting.
- Rail booking aggregation (SNCF, Trenitalia, Amtrak coverage across US, Canada, Western Europe) is a lesser-known competitive advantage — content opportunity to highlight breadth vs. fragmented competitors like Concur.
- Personal travel rewards driving adoption and retention is a underappreciated retention lever — worth positioning as a user experience and value retention story.

**To CheckThat:**
- Navan's shift from SEO to LLM-optimized question-answer content formats (mentioned by Nima regarding query format changes between SEO and LLM results) aligns with AEO methodology — opportunity to apply CheckThat prompt testing and optimization to Navan use cases.
- Advanced analytics feature (ThoughtSpot integration for AI-powered report building, rolling out) represents emerging AI-driven features worth monitoring for competitive landscape analysis.

**To GrowthX Business Development:**
- Account health signal: Navan is investing in content strategy and deep dives with GrowthX, indicating commitment to brand/demand generation — positive indicator for engagement depth and expansion opportunity.
- Nikita Schaub (San Francisco-based, recently relocated from London) and Nima Asrar Haghighi are key product stakeholders — maintain relationships for ongoing insights and reference calls.
- Payments functionality (Nikita committed to sharing docs) is an underdeveloped content area — content opportunity and potential proof point for integrated platform narrative.

---

## Overview

- **Personal Travel as a Retention Driver:** Personal travel, funded by business rewards, boosts platform adoption and retention, enabling company savings by keeping bookings in-platform.
- **Actionable Admin Reporting:** The admin dashboard provides actionable data (e.g., out-of-policy spend, live traveler map) with benchmarks and direct user lists to enable proactive program management.
- **Proactive Expense Control:** The "traffic light" policy system (Green: auto-approve, Orange: flag, Red: auto-decline) provides real-time spend control at the point of swipe, eliminating retroactive expense reports.
- **Differentiated Group Travel:** The events tool simplifies complex logistics for large groups, including non-employees (e.g., interview candidates, board members), a key differentiator and source of high-value leads.

---

## Key Topics

### Personal Travel

  - **Path to Adoption:** Users typically discover personal travel via rewards earned from business bookings.
  - **Value Proposition:**
      - Fully private bookings, separate from company visibility.
      - Access to Navan's negotiated rates and deals.
      - Free 24/7 support for all personal travel.
  - **Booking Options:**
      - **Black Cars:** Premium car service, often used by delegates (EAs) for executives.
      - **Lodging Collection:** Navan's negotiated rates, offering savings and perks (e.g., late checkout, free breakfast).
      - **Company Negotiated:** Enterprise-specific rates loaded by the customer.
      - **Company Preferred:** Flagged hotels recommended by the company.

### Rail Booking

  - **Industry Problem:** Competitors (e.g., Concur) offer fragmented rail inventory, often restricted by country.
  - **Navan's Differentiator:** Offers the industry's broadest online rail inventory, accessible from anywhere.
      - **Coverage:** US (Amtrak), Canada, and most of Western Europe.
      - **Benefit:** Aggregating carriers (e.g., SNCF, Trenitalia, Wego) provides more options and significant savings.

### Admin & Reporting

  - **Core Function:** Enables admins to control spend, monitor compliance, and manage the travel program.
  - **Reporting Tiers:**
      - **Dashboard:** High-level metrics (spend, adoption, satisfaction).
      - **Analysis:** Pre-made dashboards for specific areas (flights, hotels, CO2).
      - **Reports:** Custom reports from 130+ data points per booking, with scheduling.
  - **Key Differentiators:**
      - **Actionable Data:** Provides context (e.g., benchmarks) and direct user lists (e.g., out-of-policy spenders) to enable proactive decisions.
      - **Advanced Analytics (ThoughtSpot):** Enables deep data slicing, custom alerts, and AI-powered report building (rolling out).
  - **Duty of Care:** The live map is a critical feature, as it only works if employees book in-platform. This enables real-time location tracking and communication during emergencies.

### Expense Management

  - **Core Principle:** Proactive spend control at the point of swipe, eliminating retroactive expense reports.
  - **"Traffic Light" Policy System:**
      - **Green:** Auto-approved (e.g., meals under $100).
      - **Orange:** Flagged for review (e.g., meals $101–$500).
      - **Red:** Auto-declined (e.g., meals over $500).
  - **Context Capture:** Captures rich transaction data (merchant, location, traveler status) and integrates with calendars to automatically add attendees to team meals, reducing manual entry.

### Group Travel & Events

  - **Functionality:** A dedicated tool for managing events of any size.
  - **Key Use Cases:**
      - Sales kickoffs and company conferences.
      - President's events and incentive trips.
      - Board meetings and sponsor/speaker travel.
  - **Non-Employee Travel:** A major differentiator, allowing companies to invite and manage travel for external guests (e.g., interview candidates, board members).

---

## Action Items

**Nikita Schaub (Navan)**
- Email Payments documentation to Nima Asrar Haghighi (Navan) and Erik O'Brien (GrowthX)

---

## Transcript
**Erik O'Brien:** Hey, Nima.

**Nima Asrar Haghighi:** Hi, Erik.

**Nima Asrar Haghighi:** Sorry, I'm all right.

**Nima Asrar Haghighi:** Yeah, no worries.

**Erik O'Brien:** Still waiting for Nikita.

**Nima Asrar Haghighi:** Yeah, he's having another meeting as well, so we should be closing it up in probably five minutes.

**Nima Asrar Haghighi:** In the meantime, how could I help until he joins us?

**Nima Asrar Haghighi:** Anything that outstanding that I could help you with?

**Erik O'Brien:** I don't believe.

**Erik O'Brien:** So I think just going through that content strategy that Ada presented this morning, I think the feedback we got there was pretty good, so we can incorporate that, plus the additional content you sent over the weekend.

**Erik O'Brien:** I think the team's just getting through some of that, mainly the S1 and the glossary.

**Erik O'Brien:** Any other kind of high-level thoughts or feedback so far?

**Nima Asrar Haghighi:** No, I think it was good.

**Nima Asrar Haghighi:** I liked some of the thinking that was going to examples of the keywords that she had there.

**Nima Asrar Haghighi:** I think there is a lot more of those ones that we could go about, so how do we know?

**Nima Asrar Haghighi:** How deep we should go and where, because, and then also the other thing that wasn't clear for me is that as we

**Nima Asrar Haghighi:** When move from the SEO to LLM results, right, the query format changes quite a bit, how do we think about creating the questions and answer kind of ideas, so that might be an output of the programs that we're going to be running, but that's, that was the only thing that was kind of making me think a little bit more.

**Nima Asrar Haghighi:** Yeah.

**Nima Asrar Haghighi:** Hey, Nikita.

**Nima Asrar Haghighi:** Hey, how's it going?

**Nima Asrar Haghighi:** Good, good.

**Nima Asrar Haghighi:** Thank you very much.

**Nima Asrar Haghighi:** Good.

**Nima Asrar Haghighi:** Sorry for being a bit behind.

**Nikita Schaub:** I am just, uh, candidly waiting for Gemini to analyze, uh, the lease agreement I just received to let me know if I can sign it.

**Nikita Schaub:** Sorry.

**Nikita Schaub:** It's a very busy rental market.

**Nikita Schaub:** In SF, and I'm just like, we got it now, and they were like, you sign it, or it goes.

**Nikita Schaub:** Yeah, if you have to jump, totally understand it.

**Nima Asrar Haghighi:** I know, SF, if you're two minutes late, it's gone.

**Nima Asrar Haghighi:** We applied already, we already have it.

**Nikita Schaub:** But now they were like, oh, we forgot to put the parking, and it's an extra fee, and we're like, but we don't want it.

**Nikita Schaub:** And then they're like, well, if you don't want it, somebody else does.

**Nikita Schaub:** So, like, okay, fine.

**Nikita Schaub:** So, Nima, if you want an empty parking in Kauho Low, let me know.

**Nima Asrar Haghighi:** Sure.

**Nima Asrar Haghighi:** Anytime.

**Nima Asrar Haghighi:** I'm sure I could use it.

**Nima Asrar Haghighi:** You could rent it out, too.

**Nima Asrar Haghighi:** No, we can't.

**Nima Asrar Haghighi:** They don't want to.

**Nima Asrar Haghighi:** Oh, they don't want to?

**Nima Asrar Haghighi:** Okay.

**Nima Asrar Haghighi:** Yeah.

**Nima Asrar Haghighi:** That's $300 a month, at least.

**Nikita Schaub:** Creative ideas for a parking spot to do something.

**Nikita Schaub:** Let me know.

**Nikita Schaub:** You know, a remote desk, storage, anything.

**Nikita Schaub:** Yeah.

**Nima Asrar Haghighi:** Pop-up store.

**Nikita Schaub:** Yeah.

**Nikita Schaub:** Yeah.

**Nikita Schaub:** Any.

**Nikita Schaub:** At this point, I mean, just going to, yeah, fun times.

**Nikita Schaub:** Yeah.

**Nima Asrar Haghighi:** Always.

**Nima Asrar Haghighi:** Did you go with two bedroom or one bedroom eventually?

**Nikita Schaub:** We went for one bed.

**Nima Asrar Haghighi:** Okay, smart choice. Let's set out the inn first, and then see whether you like the neighborhood.

**Nikita Schaub:** Yeah, that makes sense. Nikita just moved from London to San Francisco, so we're still getting settled.

**Nima Asrar Haghighi:** So let's get started.

**Nima Asrar Haghighi:** Absolutely.

**Erik O'Brien:** I believe we left off on hotel workflow, and then we were talking through just some of the rewards that you're able to gather if you're kind of booking hotels below policy.

**Erik O'Brien:** So if we can just pick up there, and then I think high level, just get through the rest of travel, and then some of the Expense, plus the Admin side.

**Nikita Schaub:** I'll just share my entire screen.

**Nikita Schaub:** See things.

**Nikita Schaub:** It's okay.

**Nikita Schaub:** All right.

**Nikita Schaub:** I think we had, yeah, we had done most of the...

**Nikita Schaub:** Hmm.

**Nikita Schaub:** I thought it was this guy.

**Nikita Schaub:** No.

**Nikita Schaub:** Oh, sorry.

**Nikita Schaub:** Is this...

**Nikita Schaub:** Wow, I feel...

**Nikita Schaub:** Can I just close this little window, or is it going to close you guys?

**Erik O'Brien:** I'm not sure. Let's see.

**Erik O'Brien:** You should be closer.

**Nima Asrar Haghighi:** Hey, what's the line?

**Nikita Schaub:** There we go.

**Nikita Schaub:** Okay, good stuff.

**Nikita Schaub:** Do you want to go more into the hotel workflow or do you feel like that was probably enough?

**Erik O'Brien:** I feel like we covered quite a bit there, at least enough for me to suggest.

**Nima Asrar Haghighi:** think, unless, Nikita, when is the best for extending to personal?

**Nima Asrar Haghighi:** Is that after hotel or is it after the flight or either?

**Nima Asrar Haghighi:** So I think it's a very valuable one to cover.

**Nima Asrar Haghighi:** Okay.

**Nima Asrar Haghighi:** Yeah, after hotel is actually good.

**Nikita Schaub:** I think the easiest segue we have, and you can see my screen, right?

**Nikita Schaub:** Yep.

**Nikita Schaub:** Great.

**Nikita Schaub:** The easiest segue to personal, at least in the demo, is via other rewards.

**Nikita Schaub:** Because even for users, that tends to be the path, which is, you know, you use Navan for business travel, which is like, there's no sign-up path for personal only today.

**Nikita Schaub:** And this does change in the past few weeks.

**Nikita Schaub:** but

**Nikita Schaub:** So you start because your company on board is Navan for their travel program, and you go around, and either by exploration or emails, you see that there's personal travel, and you're like, that's pretty sweet.

**Nikita Schaub:** Or usually the main path is by other rewards, which is also why it's a good driver for us, but also for companies to save.

**Nikita Schaub:** And you're going to see this notion of rewards starting to pop up, and you're like, oh, I can start actually saving money.

**Nikita Schaub:** What do I save it for?

**Nikita Schaub:** You save it for your personal travel.

**Nikita Schaub:** So this is the easiest segue.

**Nikita Schaub:** The second segue, which is a little less direct, but also pops up in the flow, is once you've actually booked something, you will start to get some nudges throughout the experience, as we saw last time in the trip section, for instance, where within your trip detail, it's going to be a little thing that says, hey, you could actually expand this for what we call pleasure, which is your own kind of little holiday while you're on your business journey.

**Nikita Schaub:** And you just stayed a weekend, for instance, right?

**Nikita Schaub:** So those little pop-ups appear.

**Nikita Schaub:** So I'm showing you the pop-up here.

**Nikita Schaub:** I'm going back to Steven's trip, which we saw last time.

**Nikita Schaub:** And you should see here, it's probably gonna be in the hotel side.

**Nikita Schaub:** Bam, extend your trip with top deals.

**Nikita Schaub:** So there's a few nudges, but this is the how they get to it.

**Nikita Schaub:** What the experience looks like in itself, I would say is very similar.

**Nikita Schaub:** You're going to go back to here and go back to business, add to personal.

**Nikita Schaub:** Similar interface, same content.

**Nikita Schaub:** You can actually see it, this is actually a kind of slightly review value proposition, but every booking that happens in the personal side is completely private.

**Nikita Schaub:** So my company obviously doesn't know where I go on holidays and what's going on, which is great.

**Nikita Schaub:** But at the same time, me as a traveler, I will still have access to all the content.

**Nikita Schaub:** next So to to the I'm

**Nikita Schaub:** That is available in Navan.

**Nikita Schaub:** I will have access to all the special deals that Navan has access to.

**Nikita Schaub:** And then when I manage my trip, same idea, that trip's view with all my bookings in one go, I have access to Navan support, which is actually great.

**Nikita Schaub:** I use it for personal travel myself.

**Nikita Schaub:** There's a few times where I need to change something.

**Nikita Schaub:** I just contact support.

**Nikita Schaub:** It's free.

**Nikita Schaub:** Somebody does it for me.

**Nikita Schaub:** I don't need to wait on the phone with the airline for hours, which can be quite annoying.

**Nikita Schaub:** If it takes too long, they're like, we'll call you back.

**Nikita Schaub:** They actually call you back.

**Nikita Schaub:** It's great.

**Nikita Schaub:** But peace of mind.

**Nikita Schaub:** It's the same idea.

**Nikita Schaub:** Same value prop as a business traveler, but a service for your personal travel.

**Nikita Schaub:** So it's pretty sweet.

**Nikita Schaub:** And obviously you book for yourself.

**Nikita Schaub:** You can book for a few people, right?

**Nikita Schaub:** So here, for instance, I could start booking a trip for myself and my wife, and maybe we're going to go, I don't know, SFO to Tahiti, which I spotted recently as a direct flight, which was pretty sweet.

**Nikita Schaub:** And there you

**Nikita Schaub:** You can start booking your trip.

**Nikita Schaub:** It's the same.

**Nikita Schaub:** That trip is tied to both users, which is, you know, same as you would go on an airline's website and book for two and all the benefits I mentioned before.

**Nikita Schaub:** In terms of what I can book, you might not have noticed, but there is one thing that's popped up here that was not in the business travel flow before, which is black cards.

**Nikita Schaub:** We have black cards for business travel, but it needs to be enabled by the company.

**Nikita Schaub:** And last time, I don't know if you remember, but Nima mentioned this user type called delegates.

**Nikita Schaub:** Delegates, you know, can be anything from a person booking for the entire office to something a bit more high-touch, which is the delegates that matter to us in travel programs, which is usually the EAs, the executive assistants, who book trips on behalf of the execs.

**Nikita Schaub:** For them, for instance, black cards is pretty nice, right?

**Nikita Schaub:** So it's really, I'm going to pre-book a very fancy Uber that's going to go pick them at the airport.

**Nikita Schaub:** and has one of those signs standing off, right?

**Nikita Schaub:** This is nice, the black cars bookings also track your flight details, so they know if you can arrive later and so on.

**Nikita Schaub:** So a really nice part of our offering that's online, that's also very few TMCs, if any actually, have brought online.

**Nikita Schaub:** But yeah, we just can't see it on the business travel side, because us as Navan employees, we're not allowed to book black cars for ourselves, which kind of makes sense.

**Erik O'Brien:** Yeah.

**Nikita Schaub:** All right, so the hotel I had selected before, we're going a bit of a mental gymnastics here, but let me know if I need more context before those switches, but we had a few hotels, this one had rewards, really cool.

**Nikita Schaub:** This one also has a little tag here called lodging collection.

**Nikita Schaub:** The lodging collection is essentially the own set of negotiated rates that we, Navan, as a company, have negotiated using the combined purchase power of our entire unit.

**Nikita Schaub:** The main benefit, of course, is usually savings, but sometimes there's additional benefits like, hey, this one will actually give you late checkout, or this property will give you preferential terms and conditions, aka you can cancel at the last minute, or they might give you free breakfast, right?

**Nikita Schaub:** So it's a series of perks that we bundle into some rates that are usually our most travel-to properties, and we can also work with customers if they're in a certain region or city where they're like, hey, I'm traveling there a lot.

**Nikita Schaub:** I personally don't have enough purchase power, but would you, Devon, be okay to maybe have a look at which hotel so you can negotiate rates out there?

**Nikita Schaub:** And we're like, yeah, sure, we'll do it.

**Nikita Schaub:** And then there's slowly but surely those kind of power point.

**Nikita Schaub:** I don't have the exact number of total properties we have there, but it's in the tens of thousands.

**Nikita Schaub:** And these are usually pretty, pretty nice deals.

**Nikita Schaub:** Again, I can find also the percentage of savings, but yeah, lodging collection usually.

**Nikita Schaub:** A good savings.

**Nikita Schaub:** The other kind of flags that you can put on hotels, there's two others.

**Nikita Schaub:** One is company negotiated.

**Nikita Schaub:** So this is particularly important for enterprise accounts.

**Nikita Schaub:** So if you think of a large company that travels very often in the same city, what they will start to be able to do with the total span they have is go to certain hotels and say, Hey, I'm spending, I don't know, a hundred bookings per year in this city.

**Nikita Schaub:** If I do them all at your property, what discounts can you give me?

**Nikita Schaub:** Right?

**Nikita Schaub:** And so those are such a pretty big component of large travel programs.

**Nikita Schaub:** And so if you have your own negotiated rates, you can load them in the platform.

**Nikita Schaub:** They will be tagged similarly with your company name and that says negotiated.

**Nikita Schaub:** So this is the second tag you can find.

**Nikita Schaub:** And the third tag you can find is company preferred, right?

**Nikita Schaub:** So for instance, here at Navan, we're NSF.

**Nikita Schaub:** Downtown, maybe we don't have negotiated rates with hotels nearby, but we might know that, I don't know, yeah, maybe this guy, the Union Square Hotel is great, and we want to flag it.

**Nikita Schaub:** We can have a tag that is just called preferred.

**Nikita Schaub:** So this is just to help the company give nudges to their users that this property is tried and tested.

**Nikita Schaub:** Let me know if I'm going too detailed, not detailed enough.

**Nikita Schaub:** You know, some of the fun stuff, like you can save a property, it will pop up at the top of your search results.

**Nikita Schaub:** The photos that we get access to is usually extensive.

**Nikita Schaub:** I could show you some other platforms and they would have maybe one or two pictures that are cropped and like very small resolution, like probably this size, but just stretched out.

**Nikita Schaub:** So pixels everywhere.

**Nikita Schaub:** You know, we can show you things like distance to your office or to your search point.

**Nikita Schaub:** Just a lot of things.

**Nikita Schaub:** Again, to make you make a decision faster and just build trust in the platform, right?

**Nikita Schaub:** And a lot of this, again, if you come from Booking.com, you're like, yeah, I've seen it.

**Nikita Schaub:** But if you come from any of a business travel tool, the complexity behind this is actually pretty big.

**Nikita Schaub:** Same thing in terms of rate.

**Nikita Schaub:** Like, those are direct rates.

**Nikita Schaub:** Some of the rates here are from Hotels.com.

**Nikita Schaub:** Some are for Priceline.

**Nikita Schaub:** To be able to match the direct rates with the Priceline one and the Hotel one to this room is actually a lot of work.

**Nikita Schaub:** But it looks great.

**Nikita Schaub:** And then you're like, oh, you can compare all the rates and see what you get and so on.

**Nikita Schaub:** so, yeah, this is a lot of work in the back.

**Nikita Schaub:** But overall, it looks very smooth.

**Nikita Schaub:** Get the little hotel reviews here as well.

**Nikita Schaub:** So we pull the hotel review number, the score.

**Nikita Schaub:** But we also give you actual reviews.

**Nikita Schaub:** These come directly from Priceline, by the way.

**Nikita Schaub:** Not that we need to mention it, but sometimes people ask.

**Nikita Schaub:** And, yeah, hotel booking platform is, I would say, see dazu Thank

**Nikita Schaub:** The market could be the best one.

**Nikita Schaub:** All right, cool.

**Nikita Schaub:** Let's go to the homepage.

**Nikita Schaub:** I'm not gonna go too much in detail today.

**Nikita Schaub:** We can do it at the end if we still have time, but on the rail platform or trains, the main call out here is that trains is a bit funny in business travel because at the same time, out of all those transport methods, it's the oldest one.

**Nikita Schaub:** It's also the least developed one in online booking tools.

**Nikita Schaub:** For whatever reason, the TMCs have not built it out too much.

**Nikita Schaub:** Well, actually, the main reason is probably that you don't make a lot of money on rail bookings, but it's probably this.

**Nikita Schaub:** And what you're gonna find very often is you're gonna find a tool, let's say, Concur, which is a very old tool.

**Nikita Schaub:** And you might have your users who are based in France, will get access to French rail, but they won't get access to German rail.

**Nikita Schaub:** And your users that are based in Germany will get access to German rail, but not French rail.

**Nikita Schaub:** For whatever technical reason, they make these restricted by country for the country, which is cool for some part of a user base.

**Nikita Schaub:** But realistically, your users are going to travel all over the place, and you want to be able to book a train in a country you're not yet in, right?

**Nikita Schaub:** Because you might be traveling to Canada tomorrow, and you know you need to go from Montreal to whichever city is two hours away.

**Nikita Schaub:** All right, so rail booking, a bit weird in the travel industry.

**Nikita Schaub:** We obviously, and thankfully, have a different approach where we unlock all those carriers to be accessible from anywhere.

**Nikita Schaub:** And so in terms of coverage, I think with the one we're unlocking this week, I think we can confidently say as a travel management company, we'll be able to offer the broadest online.

**Nikita Schaub:** Inventory.

**Nikita Schaub:** So we have Canada is coming up this week, we have the US obviously already with Amtrak, and in Europe we have most of Western Europe, European countries, which is really solid coverage.

**Nikita Schaub:** All those are accessible from anywhere, and fully self-service.

**Nikita Schaub:** In a lot of scenarios, you can also book your seat, so reserve your rail seat online, which again, if you're used to booking your train directly on the rail provider's website, you're like, oh, this is pretty standard.

**Nikita Schaub:** But doing it at scale across so many carriers where possible is pretty big in terms of innovation and capability.

**Nikita Schaub:** So something we do like to promote, again, some people might be like, well, I don't care because my office is in the Midwest and I need to travel to the West Coast all the time.

**Nikita Schaub:** Cool.

**Nikita Schaub:** But for many large programs, it matters a lot.

**Nikita Schaub:** The best example I'd like to show here.

**Nikita Schaub:** Here is Lyon, Paris.

**Nikita Schaub:** This is a good example because you can show the breadth of content that we bring.

**Nikita Schaub:** You can see here we have SNCF, normal, the national French rail carrier.

**Nikita Schaub:** But then who do you see here?

**Nikita Schaub:** This is an Italian rail.

**Nikita Schaub:** is Vingtree in Italia.

**Nikita Schaub:** So we're able to bring Italian content because they also travel in France.

**Nikita Schaub:** Then you can see here, bam, this is a direct saving, right?

**Nikita Schaub:** You would have only usually 84 euros or 84 dollars.

**Nikita Schaub:** We bring you the Italian carrier that also is in France, bam, you can now pay 56.

**Nikita Schaub:** On top of this, we built a connection recently with Wego, which is a low cost carrier.

**Nikita Schaub:** So here you can really see the effect of having the additional sources of content in the platform.

**Nikita Schaub:** Effect number one is you just have more options, which is great, right?

**Nikita Schaub:** Some is probably fancier, some is probably a bit cheaper.

**Nikita Schaub:** But you have all those options so that you can depart anytime you want, but also no reason to get outside of the platform.

**Nikita Schaub:** And then it's the cost.

**Nikita Schaub:** Like here, you know, if you take 20 minutes away, you're gonna pay like less than half price.

**Nikita Schaub:** All right, so in savings, you can't do better than this.

**Nikita Schaub:** And again, no reason to book outside of the platform.

**Nikita Schaub:** This guy, you can probably go and book your rails, your seats and so on.

**Nikita Schaub:** But yeah, I'm not gonna go too deep there, but this is pretty cool.

**Nikita Schaub:** All right, sweet.

**Nikita Schaub:** Again, any questions, just stop.

**Nikita Schaub:** I don't see anyone, I just see my screen.

**Nikita Schaub:** Oh, we are not there anymore.

**Nima Asrar Haghighi:** We went home.

**Nima Asrar Haghighi:** Yeah, I like, maybe I'm just speaking to myself.

**Nima Asrar Haghighi:** Yeah, that's one of those issues with Google.

**Nima Asrar Haghighi:** Hopefully you're just all so captivated by the business travel industry now.

**Nima Asrar Haghighi:** Yeah, absolutely.

**Nikita Schaub:** All right, you wanted to see expenses.

**Nikita Schaub:** There's a few different paths in to expense.

**Nikita Schaub:** I'll do the one.

**Nima Asrar Haghighi:** Nikita, as we go, think one area I would love definitely to focus on is the advanced analytics integrations.

**Nima Asrar Haghighi:** I think there would be some really good keywords around those ones.

**Nima Asrar Haghighi:** Somehow, if you leave those two things in it as well, that would be great.

**Nima Asrar Haghighi:** Yeah.

**Nima Asrar Haghighi:** Did we sign an NDA?

**Nikita Schaub:** Yeah.

**Nima Asrar Haghighi:** Yes.

**Nima Asrar Haghighi:** Okay.

**Nima Asrar Haghighi:** Okay.

**Nikita Schaub:** Wait.

**Nikita Schaub:** Oh, no.

**Nikita Schaub:** Okay.

**Nikita Schaub:** It's here.

**Nikita Schaub:** I'm going to log into some accounts, just you not seeing anything, but that's fine.

**Nikita Schaub:** But yeah, I'll show you the capabilities from the point of view of someone who has access to it.

**Nikita Schaub:** I was going to go.

**Nikita Schaub:** go.

**Nikita Schaub:** So staging, which is our engineer's environment, but it actually doesn't look very nice.

**Nikita Schaub:** So I'll just go into a build account and show you what the admin section looks like there.

**Nikita Schaub:** they should be on experience.

**Nikita Schaub:** All right.

**Nikita Schaub:** So this is the same platform, but I'm now an admin.

**Nikita Schaub:** All right.

**Nikita Schaub:** So I do have access to all the fun company admin section here.

**Nikita Schaub:** And I think I picked an account that doesn't have experience.

**Nikita Schaub:** Oh, that's okay.

**Nikita Schaub:** All right.

**Nikita Schaub:** I will start with just a normal reports and then we can go into expense.

**Nikita Schaub:** I think that makes a bit more sense.

**Nikita Schaub:** Is that okay for you?

**Erik O'Brien:** That's sweet.

**Nikita Schaub:** You know, as an admin, you want to control spend.

**Nikita Schaub:** You want to see what's out of policy.

**Nikita Schaub:** You want to make sure there's no anomalies and then you want to manage your program.

**Nikita Schaub:** All right.

**Nikita Schaub:** So manage.

**Nikita Schaub:** Okay.

**Nikita Schaub:** So your program is things around safety, things around compliance, and then just see if there's any optimizations available, whatever those optimizations are.

**Nikita Schaub:** When it comes to visibility, we're at the top left here on the dashboard.

**Nikita Schaub:** Initially, there's three views that we provide.

**Nikita Schaub:** There's the dashboard page, which is your helicopter view on all the key metrics that matter, and this page, the metrics are set.

**Nikita Schaub:** If you want to go a level deeper, you have the analysis pages, where you can go a bit deeper on certain areas.

**Nikita Schaub:** Similar views, I would say, with pre-made dashboards, or just on specific areas, so total span, flights, hotels, CO2 emissions, well-being.

**Nikita Schaub:** If you want to go a level deeper, we have the reports.

**Nikita Schaub:** In the reports section, you have access to all the data points

**Nikita Schaub:** That we offer per booking, which is, I think, 130 data points captured per booking.

**Nikita Schaub:** And based on those data points, you can start and build a report of whatever you want.

**Nikita Schaub:** You can start to build a report of out-of-policy spend by the French sales team over a month, for instance.

**Nikita Schaub:** And then you can save and schedule it so that all those transactions are sent to someone in your company.

**Nikita Schaub:** So from very high level all the way to more granular.

**Nikita Schaub:** Now we have a fourth view, which is called Advanced Analytics, which I'm going to go into after.

**Nikita Schaub:** But I will go back to the dashboard first because it's the most visually easier to see and kind of understand.

**Nikita Schaub:** If you put it on the website or something, it's like, this is a cool view that speaks to everyone.

**Nikita Schaub:** Still nice to mention the other capabilities, but this one is more approachable.

**Nikita Schaub:** Top view is spanned over time.

**Nikita Schaub:** This is great.

**Nikita Schaub:** This might be normal.

**Nikita Schaub:** This might be very concerning that it changes per company.

**Nikita Schaub:** Business travel spanned is usually...

**Nikita Schaub:** Business usually...

**Nikita Schaub:** Cyclical.

**Nikita Schaub:** You'll have some quarters where you travel more.

**Nikita Schaub:** For instance, I don't know if you guys have a sales kickoff.

**Nikita Schaub:** Sales kickoffs are usually around February.

**Nikita Schaub:** This is a lot of people on the road.

**Nikita Schaub:** Sometimes it's September meetings.

**Nikita Schaub:** So it depends a lot on how your company travels.

**Nikita Schaub:** So this might be totally normal.

**Nikita Schaub:** This might be completely out of place.

**Nikita Schaub:** The admins will usually know very quickly.

**Nikita Schaub:** Here, a bunch of key metrics.

**Nikita Schaub:** I'm not going to go into all of them.

**Nikita Schaub:** But this is essentially what you need to know about your program.

**Nikita Schaub:** The way I'm going to start to call out a few things is at this section.

**Nikita Schaub:** So adoption is essentially the percentages of bookings that happen on your platform.

**Nikita Schaub:** Here we count it by registered users, mobile app users.

**Nikita Schaub:** Doesn't matter.

**Nikita Schaub:** We give you a view of adoption.

**Nikita Schaub:** We also give you a view of satisfaction.

**Nikita Schaub:** So throughout the experience, we will send out little surveys to users that say, are you satisfied?

**Nikita Schaub:** Yes, no, and why?

**Nikita Schaub:** The main thing I will call out on our reporting.

**Nikita Schaub:** One thing is the actionability of the reporting.

**Nikita Schaub:** You're going to have many tools that just give you some key metrics with little context.

**Nikita Schaub:** And we go a little further than this.

**Nikita Schaub:** For instance, in the adoption metrics, we'll give you who is registered.

**Nikita Schaub:** You can also download the list of who's missing because this connects directly to your HR system.

**Nikita Schaub:** For the NPS score, we give you the score.

**Nikita Schaub:** You can also download a list of answers to the surveys to see actually who's unhappy and why.

**Nikita Schaub:** So this notion of actionability in the data is a differentiator.

**Nikita Schaub:** Same here.

**Nikita Schaub:** If I go a level below, now we start to look at key metrics.

**Nikita Schaub:** Cool.

**Nikita Schaub:** Do you know if the 1,632 average flight per price is high?

**Nikita Schaub:** Not really.

**Nikita Schaub:** But we give you a benchmark to tell you, holy , this is actually a lot of money.

**Nikita Schaub:** I don't know how they're spending that one.

**Nikita Schaub:** Okay, they're finding a lot of this in class.

**Nikita Schaub:** makes sense.

**Nikita Schaub:** But this is very high, right?

**Nikita Schaub:** Without a benchmark, you don't have a lot of context.

**Nikita Schaub:** And as a travel manager,

**Nikita Schaub:** You don't really know if, oh, maybe this is inflation, blah, blah, blah.

**Nikita Schaub:** In this case, it's not inflation.

**Nikita Schaub:** In this case, it's that they're flying a lot of business class, and they're flying it way more than other companies.

**Nikita Schaub:** If this is acceptable for them as a company, it's fine.

**Nikita Schaub:** But this is, for instance, one way to make those metrics speak to them a bit more and make it much more actionable.

**Nikita Schaub:** For instance, let's imagine this flight price is much higher.

**Nikita Schaub:** They fly as much economy as anyone else, but everybody books at the last minute.

**Nikita Schaub:** You exactly know why those flights are much more expensive.

**Nikita Schaub:** So already this combination of metrics and benchmarks helps you make more informed decisions.

**Nikita Schaub:** All right.

**Nikita Schaub:** A bunch more key metrics.

**Nikita Schaub:** The other fun dashboard to show is the compliance one.

**Nikita Schaub:** Compliance means essentially, have I booked in policy, right?

**Nikita Schaub:** Have I respected the guidelines that...

**Nikita Schaub:** My travel and expense and finance teams I've agreed to, which are usually around cost, usually around fare class, it's don't book, business class, supreme economy, and around lead time.

**Nikita Schaub:** Lead time is how early or late I'm booking, whatever I'm booking.

**Nikita Schaub:** All right, the compliance tab here tells you how much more you could have saved if people had booked in line with your policies.

**Nikita Schaub:** And it gives you a bit of a view of, hey, who have actually booked out of policy all the time?

**Nikita Schaub:** Our French sales rep would call this the bad boys list because people laugh and they're like, ah, it's fun, but it's memorable and it's actually true.

**Nikita Schaub:** You can see it all the name, you can even see the name of the individuals who have spent the most out of policy.

**Nikita Schaub:** All right, this is also great because it gives you perspective on, is this something you need to act on or not?

**Nikita Schaub:** Let me give you an example.

**Nikita Schaub:** And I refer a lot to the sales team in those demos, but people tend to relate to this.

**Nikita Schaub:** If my sales team books always out of policy, but they...

**Nikita Schaub:** Always do it because they book at the last minute, and that is the nature of my business, that might be okay.

**Nikita Schaub:** It might also tell me that I should change my travel policy to allow them to book at the last minute.

**Nikita Schaub:** But I know that this is not a red flag, right?

**Nikita Schaub:** But if my engineering team is always booking at the last minute and too expensive, I can send them a message and be like, guys, you don't need to book at the last minute.

**Nikita Schaub:** So either we put you on a harder approval flow where we block bookings, or you change your patterns.

**Nikita Schaub:** So there's a few things that it lets me think about.

**Nikita Schaub:** All right, I'm not going to go into all the detailed reports.

**Nikita Schaub:** Just the main thing we need to know is it's very actionable.

**Nikita Schaub:** You can slice and dice your data.

**Nikita Schaub:** You can pre-build reports and schedule them.

**Nikita Schaub:** Very cool.

**Nima Asrar Haghighi:** Nikita, I think if you want to, this is all great, but in context...

**Nima Asrar Haghighi:** Yeah.

**Nima Asrar Haghighi:** It's going to be more interesting.

**Nima Asrar Haghighi:** For example, if somebody who's on Concur wants to pull the same reports, how long does it take them to do something like that, right?

**Nima Asrar Haghighi:** Because if you could talk to that piece as well, that would be super helpful.

**Nima Asrar Haghighi:** Yeah.

**Nikita Schaub:** These two issues, if you're on Concur, and it's going to sound like a sales pitch, but it's not, it's true.

**Nikita Schaub:** The first issue, if you're on Concur, is that the percentage of bookings from your employees that happen on your tool is usually quite low.

**Nikita Schaub:** So any report you're going to be able to pull is missing a lot of data because the tool is so  that people just go and book direct and then they expense it.

**Nikita Schaub:** And this is a case for every company we speak to, you would be surprised.

**Nikita Schaub:** Sometimes we speak to enterprise, like companies who spend 20 million plus per year on travel.

**Nikita Schaub:** And they're like, oh yeah, my tool adoption is 20%.

**Nikita Schaub:** 80%, they have no idea where it goes.

**Nikita Schaub:** They only see it after the fact when it gets expense.

**Nikita Schaub:** So.

**Nikita Schaub:** This is just a level on, like, even if you had the tools, the data was not there.

**Nikita Schaub:** Doing this on Concur would be extremely painful because depending on how they set it up, you might only be able to view for a single country at the time.

**Nikita Schaub:** And this would probably take you a few days and you'd probably need to ask an account manager at some point to help you do it because it's just, crap.

**Nikita Schaub:** The value we try to give here is that the work a data analyst would normally do for you in a legacy tool, we enable you to do yourself.

**Nikita Schaub:** And the culmination of this is really this tool for Advanced Analytics, which makes everything you've seen even more actionable.

**Nikita Schaub:** And this is a partnership with Fathspot.

**Nikita Schaub:** I don't know if you know Fathspot, but they do BI that is extremely accessible.

**Nikita Schaub:** And here, this allows us to build new dashboards in a couple of hours and make them available to all customers.

**Nikita Schaub:** And it's a similar idea as before.

**Nikita Schaub:** Like, you might see, like, okay, these kind of look like similar graphs.

**Nikita Schaub:** But here, you can actually deep dive directly in each metric and slice and dice it as much as you want.

**Nikita Schaub:** You can set up alerts, which is pretty cool.

**Nikita Schaub:** So, like, hey, if my total travel span exceeds a million per month, let me know immediately.

**Nikita Schaub:** And this is a very high-level one.

**Nikita Schaub:** But you can set up alerts per team.

**Nikita Schaub:** Again, if the marketing team is based in San Francisco, books out of policy more than 5% of the time, send me an alert.

**Nikita Schaub:** Whichever metric you want an alert on, this is great, right?

**Nikita Schaub:** So you kind of automate a lot of the maintenance of your program up to your liking, and you can deep dive into those metrics.

**Nikita Schaub:** The action ability I'm showing you here, nobody has this.

**Nikita Schaub:** With ThoughtSpot, we also have this cool thing, which I wouldn't talk about broadly just yet, but it's AI search analytics where, you know, you just type to build reports.

**Nikita Schaub:** You just say, hey, show me real bookings last year per country, growth year over year, whatever you want.

**Nikita Schaub:** You're just chatting here with the AI, and it just builds the viz for you, which is pretty sweet.

**Nikita Schaub:** You said that's just rolling out?

**Nikita Schaub:** The AI chat is being rolled out.

**Nikita Schaub:** Yeah, we just need to finalize this queue, which might take a month to three months or five.

**Nikita Schaub:** I don't know when it's going to be.

**Nikita Schaub:** But what I'm showing you here, this is out.

**Nikita Schaub:** Okay.

**Nikita Schaub:** Yeah, this is out.

**Nikita Schaub:** And you can go much deeper on all the reports you need.

**Nikita Schaub:** And if customers want a certain report, they just tell us and we can build it, which is pretty cool.

**Nikita Schaub:** Gotcha.

**Nikita Schaub:** Other fun stuff to show on

**Nikita Schaub:** The travel side is the live map.

**Nikita Schaub:** People love the live map.

**Nikita Schaub:** It's like, hey, here's everybody that's traveling in your company right now.

**Nikita Schaub:** Here's where they're at.

**Nikita Schaub:** Yeah, this is usually nice.

**Nikita Schaub:** And this is kind of a nice culmination of the talk track around adoption, which is like, Judy of Care is table stakes.

**Nikita Schaub:** Now, the features are not always super differentiated, but you need to have features on Judy of Care.

**Nikita Schaub:** And if people do not book travel in your travel tool, you have no clue where they are.

**Nikita Schaub:** So if half of your bookings are outside of Navan or Concur or wherever, and there is a security incident, you have no clue where people are in real time.

**Nikita Schaub:** And this is your libel as a company.

**Nikita Schaub:** So this talk track is actually really important, especially for large companies.

**Nikita Schaub:** And here, you know, we show you who people are traveling, which flight they were on.

**Nikita Schaub:** If you want to call them, you can.

**Nikita Schaub:** And if you want to send a push notification to their mobile phone, you can do it, too, right?

**Nikita Schaub:** So this is very actionable.

**Nikita Schaub:** is very actionable.

**Nikita Schaub:** When I joined, there were a few actual real examples of like, hey, we had an attack in this city, and we had people there, and immediately we could get in touch with all of them and tell them, hey, you got to get in touch.

**Nikita Schaub:** So this is the episode that lets you do it, that many other tools pretend to, but there's no adoption, so they actually can't do it.

**Nikita Schaub:** Travel impact dashboard, again, if there's like upcoming notification of disruptions that we know might happen, we might notice a strike in Brussels.

**Nikita Schaub:** This week, which is actually the case, you can see who, what's happening, and the potential number of impacted travelers in your company, right?

**Nikita Schaub:** this is, you want to be a bit more proactive.

**Nikita Schaub:** I'll stop here for the travel reports, and I might go into expense, if that's okay.

**Nikita Schaub:** Yep.

**Nikita Schaub:** Sweet.

**Nikita Schaub:** Do they have expense on?

**Nikita Schaub:** Oh, they do, sweet, okay.

**Nikita Schaub:** Okay.

**Nikita Schaub:** So there's a few paths to get to the expense section.

**Nikita Schaub:** I will actually start with a travel booking.

**Nikita Schaub:** Reason being, my charger.

**Nikita Schaub:** So when you want expense, essentially you want to start controlling transactions that employees are making on your behalf when they are traveling.

**Nikita Schaub:** And it's quite similar to when you're controlling a flight booking, right?

**Nikita Schaub:** The flight booking is also a transaction that your employee is making on your behalf.

**Nikita Schaub:** It's just if they do it in Navan, the flight price is cheaper and, you know, they can change it, cancel it themselves, et cetera.

**Nikita Schaub:** But it's actually the same.

**Nikita Schaub:** So let's say you've booked a hotel in Navan.

**Nikita Schaub:** This initially, immediately opens and creates a new transaction in your transaction report on the expense side, right?

**Nikita Schaub:** So you can see here that this transaction was a hotel in Amsterdam.

**Nikita Schaub:** There's something called the GL code.

**Nikita Schaub:** code.

**Nikita Schaub:** I don't know how familiar you are of accounting, but every single transaction needs its own GL code that then maps into your ERP to whatever that transaction type is.

**Nikita Schaub:** GL code here was automated because we booked it in Navan.

**Nikita Schaub:** We know it's a hotel.

**Nikita Schaub:** Now for expenses, we're going to do the same thing.

**Nikita Schaub:** We are going to code that expense on your behalf.

**Nikita Schaub:** I'll show you how after.

**Nikita Schaub:** All the additional fields that is tied to my profile, my department, my cost center, my region, blah, blah, blah, automatically filled.

**Nikita Schaub:** Bam.

**Nikita Schaub:** The expense is done.

**Nikita Schaub:** All right.

**Nikita Schaub:** So this, the concept is very similar to a spend you're going to do in your corporate card.

**Nikita Schaub:** It's this idea of collecting all the data that is needed to know what it is, and then verifying that you are allowed to make that transaction based on your policy.

**Nikita Schaub:** All right.

**Nikita Schaub:** So you've seen the mechanisms.

**Nikita Schaub:** And then the policy of the expense card is really going to be the heart of the expense product.

**Nikita Schaub:** And I need to find where we've put it now.

**Nikita Schaub:** right back.

**Nikita Schaub:** We'll we'll

**Nikita Schaub:** We've just changed this.

**Nikita Schaub:** There we go.

**Nikita Schaub:** I'll go to the most famous one.

**Nikita Schaub:** Meals for myself.

**Nikita Schaub:** Okay.

**Nikita Schaub:** They've actually not launched the expense product yet.

**Nikita Schaub:** So I'm not going to go too much into this, but I assume you travel for work, right?

**Nikita Schaub:** Maybe the easiest is like, what is your current way of expensing?

**Nikita Schaub:** Retroactive.

**Nikita Schaub:** Retroactive.

**Nikita Schaub:** Submit it all through the portal.

**Nikita Schaub:** All right.

**Nikita Schaub:** So what we want to do is automate this, which has two benefits.

**Nikita Schaub:** It saves you a lot of frigging time.

**Nikita Schaub:** And also your admin knows what you're spending in real time, as opposed to whenever you submit it through the portal, which might be on a monthly basis.

**Nikita Schaub:** Or if you're like me, I'd best on a quarterly basis because it really frustrates me to do it.

**Nikita Schaub:** So what the admin is going to do when you're on board the expense product is set up your...

**Nikita Schaub:** Policy, and you can set up a policy for pretty much anything, but the easiest one is traveling, meals for myself as a traveler.

**Nikita Schaub:** And so the way our policy works, and I'm not going to set up this because I'm afraid it's going to mess stuff up, but you're essentially going to set thresholds, and the way you need to think about this is a traffic light system.

**Nikita Schaub:** So you're going to set a threshold, which is green, which is the amount up until which everything is automatically approved.

**Nikita Schaub:** So in this case, it would be $100, which is pretty high, but let's go with it.

**Nikita Schaub:** So when you are traveling, everything up to $100 will be approved.

**Nikita Schaub:** So your total amount.

**Nikita Schaub:** So you can go to Starbucks for $10, you can to McDonald's for $15, I'm giving you a genius example here, but whatever.

**Nikita Schaub:** You can go have lunch for $25, right?

**Nikita Schaub:** As long as this total stays below $100, everything is automatically approved.

**Nikita Schaub:** Then you're going to set an orange category, which is...

**Nikita Schaub:** The transaction will still go through, but you will flag it for approval.

**Nikita Schaub:** So here it's up to $500, right?

**Nikita Schaub:** So this is a very generous policy.

**Nikita Schaub:** Anything that as soon as you start to spend above $100, everything above will be flagged for your admin.

**Nikita Schaub:** Because that's what your admin wants to see, and that's what they want more information on.

**Nikita Schaub:** So we need that orange zone.

**Nikita Schaub:** And then you will set a threshold above where it's red.

**Nikita Schaub:** You're like, screw this, everything above $500 automatically declined.

**Nikita Schaub:** There is no way in hell that we'll approve this, right?

**Nikita Schaub:** So when you start to set up that traffic light system for each type of transaction, food, Uber, fuel, internet access on the plane, then you've set up essentially what you are allowing to automate the approval of, and what you as an admin want to see and get more information on to make sure you will allow it.

**Nikita Schaub:** Does that make sense?

**Nikita Schaub:** Yep.

**Erik O'Brien:** Sweet.

**Nikita Schaub:** All right, so this is, for me, the heart of the expense product.

**Nikita Schaub:** And once you understand this, then you can understand everything else, which is the rest is very easy.

**Nikita Schaub:** There's a few ways for you as an individual to expense.

**Nikita Schaub:** Our preferred way is we issue you a Navan card.

**Nikita Schaub:** This Navan card is connected, obviously, to the card network system.

**Nikita Schaub:** So every time you swipe the card, we know immediately what type of transaction you're trying to make, because we have the merchant code, we know if you're traveling, we know who you are as an employee, we know which team you're on.

**Nikita Schaub:** We have all this additional information that we will collect by default because we know who you are and what the card is and so on.

**Nikita Schaub:** And then we verify it immediately against your policy.

**Nikita Schaub:** And so the verification, what we say is like control span before it happens because at the point of swipe, we can either authorize, flag, or decline the transaction.

**Nikita Schaub:** Thank you.

**Nikita Schaub:** No need to fill manual reports to say, hey, my name is Jack, I'm in the marketing team, and I have been on this trip.

**Nikita Schaub:** This is all automated, right?

**Nikita Schaub:** So all the filling of the expense is automated.

**Nikita Schaub:** And for your admin as well, they don't need to verify, okay, this guy was on the trip, he was doing this.

**Nikita Schaub:** It's just automatically done.

**Nikita Schaub:** And they will see essentially what they want to see, which is the flagged transactions.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Yeah, so expense is pretty sweet.

**Nikita Schaub:** Now, a lot of the immediate, you know, flags here, like policies, is usually around cost, right?

**Nikita Schaub:** And it's usually a total per day or a total per week or per month.

**Nikita Schaub:** The other thing you can do is you can allow certain things to happen if you're on a trip or not.

**Nikita Schaub:** So most of our users, employees at least, if they are traveling, their card will work.

**Nikita Schaub:** If they're not traveling, their card doesn't work.

**Nikita Schaub:** Everything is declined.

**Nikita Schaub:** So having travel and expense together here makes a lot of sense.

**Nikita Schaub:** You can be a bit more flexible than this if you want.

**Nikita Schaub:** What you can also do is you can have flags beyond just the costs.

**Nikita Schaub:** So this is quite new.

**Nikita Schaub:** It's something called Flag Management where we've created actually a lot of other reasons to flag a transaction.

**Nikita Schaub:** Oh, this person paid for a meal on a weekend.

**Nikita Schaub:** Okay, a little suspicious.

**Nikita Schaub:** Maybe they had a reason to travel on the weekend, but maybe not.

**Nikita Schaub:** Or, oh, they tipped excessively, right?

**Nikita Schaub:** Maybe you're like, hey, you tip above 25%, this should not be on my company.

**Nikita Schaub:** That could make sense, right?

**Nikita Schaub:** So there's a whole bunch of things here that you can flag for.

**Nikita Schaub:** And so these will be flagged to your admin as, hey, you might want to look into this.

**Nikita Schaub:** And look into this mean you can just send a message to Nima and be like, Hey, Nima, I saw you went to Starbucks on Sunday.

**Nikita Schaub:** Okay.

**Nikita Schaub:** Hey.

**Nikita Schaub:** Hey.

**Nikita Schaub:** What's up?

**Nikita Schaub:** All right, like this is maybe not normal.

**Nikita Schaub:** Maybe Nima is like, yeah, I actually flew to London, Sunday I landed late at night and I wanted, I don't know, a croissant, whatever.

**Nikita Schaub:** All right, so you can start to see what the amounts did, the transactions that you want to see.

**Nima Asrar Haghighi:** True story.

**Nikita Schaub:** A late night croissant.

**Nikita Schaub:** Oh, I landed in San Francisco at 1 a.m.

**Nima Asrar Haghighi:** and I was so hungry, so I got one.

**Nikita Schaub:** And all those policies, they can also change based on your level, right?

**Nikita Schaub:** So what I'm allowed to spend and what Nima is allowed to spend could be different, right?

**Nikita Schaub:** Because Nima has a team.

**Nikita Schaub:** So maybe in my policy, I will say Nima is allowed to pay for a team dinner.

**Nikita Schaub:** But if he pays for a team dinner, I will ask for the receipt, for instance, right?

**Nikita Schaub:** So you get to build really, it's this hyper-customized policy builder.

**Nikita Schaub:** That will fit your company policy today, or, you know, at least as close to it as possible.

**Nikita Schaub:** But it allows you to control spend the way you want.

**Nikita Schaub:** A lot of competitors will go around, you know, like automating finance and so on.

**Nikita Schaub:** Like for us, it's like finance needs to see the stuff that matters.

**Nikita Schaub:** You're going to automate 80% and the 20% that you really want to spend time on, this allows them to exactly do that.

**Nikita Schaub:** Now, I'm going to go back to my own.

**Nikita Schaub:** I've shown you the admin side, right, in practice.

**Nikita Schaub:** Oh, I actually think I have rejected transactions to show you.

**Nikita Schaub:** So this is a good example.

**Nikita Schaub:** In practice, for me as a traveler, I want to go into expanse.

**Nikita Schaub:** And here you can see all my transactions.

**Nikita Schaub:** You can see a lot.

**Nikita Schaub:** Here that I need to do more, like as a policy, as a company, we actually request a receipt if the transaction is above, I think, $65, just out of security.

**Nikita Schaub:** So I need to add a bunch of receipts here.

**Nikita Schaub:** You can see here, this is all my transactions.

**Nikita Schaub:** You know, I took an Uber when I landed in SFO.

**Nikita Schaub:** I need to add that receipt because it was about $65.

**Nikita Schaub:** Error load.

**Nikita Schaub:** This is my eSIM, Uber, a bunch of other stuff here, right?

**Nikita Schaub:** So this is all my transactions.

**Nikita Schaub:** You can see this.

**Nikita Schaub:** I didn't have to enter anything.

**Nikita Schaub:** I went to Starbucks.

**Nikita Schaub:** I sought my card.

**Nikita Schaub:** The tool knew I was at Starbucks, how much I spent.

**Nikita Schaub:** I was on a trip in New York, categorized everything, applied it to the expense type, which is traveling meals for myself, so that I was still allowed to spend money on this that day.

**Nikita Schaub:** Automatically approved.

**Nikita Schaub:** Done.

**Nikita Schaub:** I literally just wiped it off.

**Nikita Schaub:** Okay.

**Nikita Schaub:** The Uber, you know, this is now flagged as an action required because it's within that orange amount, which is like, yep, we allowed you to just, we let the transactions go through, but you need to add more information now because it's like orange, right?

**Nikita Schaub:** So this gives you a bit of action of approved versus needs more information.

**Nikita Schaub:** All right.

**Nikita Schaub:** I don't know if there's any part you want me to go over more in detail, so something you want to see more of, or I can show you some other cool stuff.

**Nima Asrar Haghighi:** If you don't mind talking a little bit about the policy, the dynamic policy.

**Nima Asrar Haghighi:** For example, Ramp CTO just had a content, so I could just drop the link here.

**Nima Asrar Haghighi:** So for example, they are thinking, I don't if that link is clear.

**Nima Asrar Haghighi:** applicable?

**Nima Asrar Haghighi:** No?

**Nima Asrar Haghighi:** Okay.

**Nima Asrar Haghighi:** Let me see if I could find it somewhere else.

**Nima Asrar Haghighi:** Let me remove the UTM so that you could access it easier.

**Nima Asrar Haghighi:** Try this link to see if it works.

**Nima Asrar Haghighi:** Yeah, so for example, they don't have any of our capabilities and this is an example of they kind of tooting the horn of their AI agents.

**Nima Asrar Haghighi:** Whereas, and then their support, so I don't know if this is something that we want to call out as well.

**Nima Asrar Haghighi:** If it's, I know maybe Nikita you need more time to review this one, but these are the sort of things that they are doing a better job of talking about their capabilities even though.

**Nima Asrar Haghighi:** It doesn't exist.

**Nima Asrar Haghighi:** Yeah.

**Nima Asrar Haghighi:** Okay.

**Nima Asrar Haghighi:** Yeah.

**Nikita Schaub:** Okay.

**Nikita Schaub:** I'll give you the honest perspective and the what we should do perspective.

**Nikita Schaub:** Yeah.

**Nikita Schaub:** None of this is AI.

**Nikita Schaub:** All right.

**Nikita Schaub:** This is just APIs.

**Nikita Schaub:** This is an API connection to the calendar, which we have.

**Nikita Schaub:** Same with the email.

**Nikita Schaub:** The expense policy is hard-coded or self-coded, but it's hard in the back.

**Nikita Schaub:** The context comes in, is applied to the written guardrails.

**Nikita Schaub:** Yes.

**Nikita Schaub:** No.

**Nikita Schaub:** Maybe.

**Nikita Schaub:** This is funny because they have rebranded a lot of it as AI, which, hey, don't hate the player, hate the game, whatever.

**Nikita Schaub:** But none of it is AI, but I guess, yes, there's a chance to lean more into it and do similarly.

**Nikita Schaub:** And I feel like this is the direction things are going.

**Nikita Schaub:** Yeah.

**Nikita Schaub:** It pains me, but it's true.

**Nikita Schaub:** So I think we can do, we can definitely do a better job at doing something.

**Nikita Schaub:** anything.

**Nikita Schaub:** Thank

**Nikita Schaub:** Similar, or actually much better, but yeah, this is the decision tree, so yes, no answer, and it flags automatically.

**Nikita Schaub:** Yeah, this is a good job of describing it.

**Nikita Schaub:** This essentially is kind of this slide here.

**Nikita Schaub:** And I can share this deck at some point.

**Nikita Schaub:** When it's finished, I just need to wrap up a few things.

**Nikita Schaub:** But on the expense side, you see on the right side, this is what is promoted as AI on the other side.

**Nikita Schaub:** But it's essentially with this card, you can capture all those transactions.

**Nikita Schaub:** You can capture what, purchase, where, because we...

**Nikita Schaub:** We where you are.

**Nikita Schaub:** Also, we have the merchant code, so we know where the shop is, for instance, who you are, you know if you're on a trip or not.

**Nikita Schaub:** We know who you're with because of your calendar integration.

**Nikita Schaub:** So if Nima has a team dinner, he most likely has it in his Gmail calendar.

**Nikita Schaub:** We have the calendar integration, so we will fetch the name of everybody in that calendar and buy it and add it to the transaction detail, and then we see if it's done with the policy.

**Nikita Schaub:** Yeah, all that context capture, I think we're going in a world where it will be more and more, say this from AI.

**Nikita Schaub:** Wow.

**Nikita Schaub:** Oh, my God, this is new.

**Nikita Schaub:** Do you guys see this?

**Nikita Schaub:** Yeah.

**Nikita Schaub:** Is it good?

**Nikita Schaub:** I haven't tried it yet.

**Erik O'Brien:** Is this Nano Banana?

**Nikita Schaub:** It looks like it.

**Nikita Schaub:** Oh, .

**Nikita Schaub:** Oh.

**Nikita Schaub:** I'm to have a green after.

**Nikita Schaub:** And they got it on the right there, too.

**Nikita Schaub:** Yeah.

**Nikita Schaub:** Wow.

**Nikita Schaub:** Yeah.

**Nikita Schaub:** That is where we really are.

**Nikita Schaub:** So you can say, yeah, with AI, we're actually able to collect more, more context.

**Nikita Schaub:** So there's something called L3 transaction data, which is much deeper level of transaction.

**Nikita Schaub:** We're able to collect this.

**Nikita Schaub:** actually had another slide, which I thought we were going to open.

**Nikita Schaub:** But yeah, we can say AI allows you to collect even more context on every transaction.

**Nikita Schaub:** And this is essentially what accounting wants and what employees want as well, because it's something that employees don't have to manually add.

**Nikita Schaub:** And accounting has all that information available to verify that it was compliant and then, you know, push it into the ERP.

**Nikita Schaub:** So it's really a win, right?

**Nikita Schaub:** We have some other smaller cool features, like the reporting I've shown you.

**Nikita Schaub:** We have a lighter version for managers.

**Nikita Schaub:** All right, so as a manager, I can see all the team, all the transactions that took place in my...

**Nikita Schaub:** Over time, I can see the safety dashboards for my direct reports and their direct reports too.

**Nikita Schaub:** You can see here nobody's traveling at the moment, so it makes sense that it's empty.

**Nikita Schaub:** I can approve the bookings directly from my team.

**Nikita Schaub:** You can see there's nothing happening, but this is just a pretty neat view.

**Nikita Schaub:** We have an entire product integrated into the tool for group travel.

**Nikita Schaub:** Group travel is very painful, usually very manual.

**Nikita Schaub:** And here in this, actually in the events tab, you can set up and manage events of any size.

**Nikita Schaub:** And this is, you can invite, you know, some people invite thousands of travelers to any given conference using Navan.

**Nikita Schaub:** And so here you can set up the guardrails to say, you need to arrive between that day and that day.

**Nikita Schaub:** And that will allow you to book a flight, but not a hotel or vice versa.

**Nikita Schaub:** You really set up all the guardrails.

**Nikita Schaub:** the Craigs stars.

**Nikita Schaub:** YouSte

**Nikita Schaub:** And then people just go and vote themselves.

**Nikita Schaub:** And we have some very, very large events being planned this way.

**Nikita Schaub:** Like you can see here, somehow I was the de facto planner of the event setup in the platform because I know it for our EMEA kickoff at the beginning of the year.

**Nikita Schaub:** So I also do part-time travel logistics.

**Nikita Schaub:** And here you can see, like, you know, we invited all those participants.

**Nikita Schaub:** We had an actual cost versus an estimated cost.

**Nikita Schaub:** And this was just everybody booked by themselves.

**Nikita Schaub:** I just set up all the parameters and let them book.

**Nikita Schaub:** And then you can manage, spend, and control the bookings here.

**Nikita Schaub:** So this is a really cool offering.

**Nikita Schaub:** It is really differentiated.

**Nikita Schaub:** We can talk about this for 30 minutes.

**Nikita Schaub:** But at some point, somewhere, it's worth talking about because I think from an SEO perspective, at least in the past, we had some really good success on keywords related to this.

**Nikita Schaub:** Yeah.

**Nima Asrar Haghighi:** So, for example, it could be a sales kickoff.

**Nima Asrar Haghighi:** It could be a company.

**Nima Asrar Haghighi:** It

**Nima Asrar Haghighi:** Any annual kickoff or in some cases, or it could be like Nikita planning the next trip to Davos, right?

**Nima Asrar Haghighi:** Any of those ones could be potential use cases.

**Nima Asrar Haghighi:** Yeah, we have this.

**Nikita Schaub:** And then this also allows you to invite non-employee travelers.

**Nikita Schaub:** Oh, yeah, that's a big one.

**Nima Asrar Haghighi:** Which is also a big one.

**Nikita Schaub:** It could be because you interview a lot of people.

**Nikita Schaub:** And as part of your interviews, you need to bring them on site.

**Nikita Schaub:** This was the case for a very large enterprise customer we signed who spent like probably $40 million a year.

**Nikita Schaub:** But this was the door of entry into their program.

**Nikita Schaub:** Or you could have your board travel.

**Nikita Schaub:** And so this is how you invite them to book.

**Nikita Schaub:** Or maybe you have some very big events and you want to invite all your sponsors and your speakers.

**Nikita Schaub:** So non-employee travel, and there's probably a few keywords around this.

**Nikita Schaub:** So it can be a big part of programs, and it's something we do really, really well.

**Nima Asrar Haghighi:** Yeah.

**Nima Asrar Haghighi:** Or for

**Nima Asrar Haghighi:** For example, there is a president's event, annual, that people take the top performers to a luxury hotel and they want to have the plus ones there, right?

**Nima Asrar Haghighi:** Yeah.

**Nikita Schaub:** Yeah.

**Nikita Schaub:** All right.

**Nikita Schaub:** Okay.

**Nima Asrar Haghighi:** Hopefully that was good, Erik, and thank you, Nikita, for walking us through it.

**Nima Asrar Haghighi:** So, let us know if you need more information, but hopefully this should give you a good starting point.

**Erik O'Brien:** Yeah, I think you got a pretty good foundation here across travel expense and the admin side.

**Erik O'Brien:** So, yeah, if I have any other questions, I'll be sure to reach out, but I appreciate the walkthrough.

**Nima Asrar Haghighi:** The part that we didn't talk much about was the payments.

**Nima Asrar Haghighi:** I don't know, Nikita, is there any documentation that you could share with the team on that front?

**Nikita Schaub:** Yeah, I can share some documents.

**Nikita Schaub:** Yes.

**Nikita Schaub:** Okay.

**Nima Asrar Haghighi:** Cool.

**Nima Asrar Haghighi:** Good stuff.

**Nima Asrar Haghighi:** Thank you much, team.

**Nima Asrar Haghighi:** appreciate it.

**Nima Asrar Haghighi:** Thank you.

**Nima Asrar Haghighi:** Bye.

**Nima Asrar Haghighi:** Bye.
