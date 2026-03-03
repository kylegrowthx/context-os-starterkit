# Otto <> GrowthX | Product Deep Dive

<metadata>
date: 2025-09-12
time: 16:00 UTC
duration: 62 minutes
organizer: Erik O'Brien
participants: Erik O'Brien (GrowthX), Michael Gulmann (Otto), Jason Flateboe (Otto)
fathom_recording_id: 86925361
fathom_url: https://fathom.video/calls/407592149
share_url: https://fathom.video/share/9UgTdHNqQTJ-8qkiDDXy7ss2QXUUDe-Y
source: fathom
enriched_on: 2025-03-03 00:00 UTC
</metadata>

---

## Summary

GrowthX learned about Otto, an AI-powered travel booking assistant designed specifically for business travelers to simplify corporate travel booking through conversational interfaces across multiple channels (web, mobile, email, Slack). Michael Gulmann and Jason Flateboe from Otto demonstrated the desktop web interface, showing how Otto integrates corporate travel policies, handles multi-city itineraries, and manages mid-trip changes conversationally. Erik agreed to beta test Otto with five one-time access codes, and the conversation touched on competitive landscape with emerging players like Poke, which recently raised $15M but takes a text-message-only approach versus Otto's multi-platform strategy.

---

## Context

Erik O'Brien from GrowthX initiated a product deep dive call with Michael Gulmann (CEO) and Jason Flateboe (product) from Otto, an AI-powered corporate travel booking platform. Erik was exploring Otto's product approach to understand how it serves business travelers. GrowthX's client base is primarily B2B rather than B2C, which informed Erik's initial questioning about whether Otto should be demoed as a mobile app versus web interface.

Otto is positioned as an AI executive assistant for corporate travel rather than a consumer leisure travel product. The platform was built to handle business-critical use cases—like making a 2 p.m. client meeting in Chicago—rather than flexible searches for cheap flights to Hawaii. The timing of this call appears exploratory; Erik was gathering competitive landscape intelligence and considering Otto's approach in context of other emerging AI travel solutions like Poke (which raised $15M).

---

## Relevance

- **To GrowthX Delivery:** Otto's conversational interface design across multiple channels (web, mobile, email, Slack, SMS) demonstrates an approach to user experience that prioritizes natural language over rigid booking flows. The platform's ability to handle mid-trip changes, multi-city itineraries, and integrate corporate policy constraints shows sophisticated product requirements that B2B travel solutions must address.

- **To CheckThat / AEO:** Otto uses AI to surface company travel policies and preferences conversationally, creating a use case where AI visibility and understanding of policy documents could be valuable. The platform's voice recognition implementation (likely Whisper API) and planned voice output features represent ongoing AI infrastructure adoption in enterprise applications.

- **To GrowthX Business Development:** Otto's product philosophy—focused on business-critical use cases rather than leisure travel—aligns with B2B service positioning. The company's multi-platform distribution strategy (app, web, email, Slack) signals confidence in demand and suggests a potential partnership or content opportunity if Otto expands its education/onboarding content needs.

---

## Overview

- Otto is a conversational AI travel assistant accessible via multiple platforms (web, mobile, email, Slack, etc.)
- Offers hyper-personalized travel recommendations and bookings based on user preferences and company policies
- Simplifies the booking process with natural language interactions and efficient servicing capabilities
- Currently focuses on flights and hotels for individual business travelers, with plans to expand features

---

## Key Topics

### Otto's Core Functionality

  - Acts as an AI-powered executive assistant for travel booking
  - Accessible through multiple channels (web, mobile, email, Slack, SMS, etc.)
  - Learns user preferences over time for hyper-personalized recommendations
  - Simplifies booking process with conversational interface and natural language understanding
  - Handles complex multi-city trip planning and itinerary management

### User Experience and Interface

  - Web interface demonstrated, similar to mobile app experience
  - Users can interact via text or voice input (voice output coming soon)
  - No rigid booking flow; users can navigate freely between steps
  - Visual elements (e.g., airline logos) enhance the experience when available
  - Saves trip progress, allowing users to resume booking later

### Key Features

  - Integrates company travel policies, highlighting in-policy vs. out-of-policy options
  - Provides detailed flight and hotel recommendations with explanations
  - Handles mid-trip changes and servicing requests conversationally
  - Offers efficient rebooking and cancellation capabilities
  - Generates travel receipts formatted for easy expense management import

### Technical Capabilities

  - Uses AI to understand complex travel requests and preferences
  - Connects to multiple travel inventory sources for comprehensive options
  - Implements voice recognition (likely using Whisper API) for speech input
  - Plans to add voice output capabilities in the future

### Current Limitations

  - Focused on individual business travelers (no multi-traveler bookings yet)
  - Limited to flights and hotels (no car rentals, cruises, or restaurants currently)
  - No built-in expense management (but provides formatted receipts)
  - Lacks approval routing for out-of-policy bookings
  - Does not offer flexible date/destination searches for leisure travel

### Competitive Landscape

  - Few direct AI-powered travel booking competitors currently operational
  - Main competition from traditional corporate travel management companies (e.g., Amex GBT, Concur)
  - Some startups (e.g., Biztrip.ai, Skylink) in early stages or pivoting
  - Legacy players likely developing AI solutions but facing challenges with existing systems

---

## Action Items

**Jason Flateboe (Otto)**
- Send 5 one-time Otto beta access codes to Erik O'Brien (GrowthX), mark as used

---

## Transcript
**Erik O'Brien:** Hey, Jason.

**Jason Flateboe:** How you doing?

**Erik O'Brien:** Not too bad.

**Erik O'Brien:** Happy Friday.

**Jason Flateboe:** Yeah, that's always a good thing.

**Jason Flateboe:** Any plans this weekend?

**Erik O'Brien:** No, I'm going to just watch football, relax, take it easy.

**Erik O'Brien:** Nice.

**Erik O'Brien:** How about you?

**Jason Flateboe:** Gosh, no, not really much.

**Jason Flateboe:** My son has a soccer game, and that's about it, but I'll probably be watching football myself.

**Erik O'Brien:** What teams do you watch?

**Erik O'Brien:** I'm in fantasy, so I watch every team now, but I'm a Chiefs fan.

**Jason Flateboe:** Oh, really?

**Jason Flateboe:** Okay.

**Jason Flateboe:** Are you from that area?

**Erik O'Brien:** I grew up there for a short stint and went to my first NFL game there.

**Erik O'Brien:** So I've been a Chiefs fan before Mahomes kind of came as our savior.

**Michael Gulmann:** I was just going to make the joke.

**Erik O'Brien:** Hi, by the way.

**Erik O'Brien:** I was going to make the joke that he's just a huge Taylor Swift fan.

**Jason Flateboe:** That's my secret.

**Erik O'Brien:** That's my secret.

**Michael Gulmann:** They don't have to be mutually exclusive.

**Erik O'Brien:** Yeah, that's funny.

**Michael Gulmann:** Good morning.

**Erik O'Brien:** Yeah, absolutely.

**Erik O'Brien:** Good morning.

**Erik O'Brien:** Appreciate you guys taking the time to do this.

**Erik O'Brien:** So we typically run through these, and I guess for larger context, a lot of our clients aren't a B2C model.

**Erik O'Brien:** They're more of a B2B.

**Erik O'Brien:** And so we kind of have like sales demos to walk through, but I'm not sure if there's a way for you to share a mobile app screen or if we just want to talk through kind of product details.

**Jason Flateboe:** I was imagining just walking you through the desktop app, which I can certainly share.

**Jason Flateboe:** It's pretty much the exact same version.

**Jason Flateboe:** I can even narrow the screen if the mobile view matters to you, but that might be just easiest.

**Erik O'Brien:** Yeah, that works.

**Erik O'Brien:** Mobile view does not matter.

**Michael Gulmann:** Well, why don't I start here? One of the things I like to do is analyze questions people ask to try to figure out their conceptions and preconceptions.

**Michael Gulmann:** And so, Erik, by your question, I'm guessing you're thinking that it's mainly an app.

**Michael Gulmann:** And that's what I want to share. Otto in general, we think of it as the best executive assistant to help you book your travel.

**Michael Gulmann:** And so if you think about the model of an executive assistant, how do you talk to your executive assistant?

**Michael Gulmann:** Or if you ever talk to an office manager who's helping you out or something like that.

**Michael Gulmann:** And the answer is yes, right?

**Michael Gulmann:** There is no one way.

**Michael Gulmann:** And so what we designed Otto to be is completely independent of the form factor or the mechanism by which to talk to Otto.

**Michael Gulmann:** And so you definitely have an iOS app.

**Michael Gulmann:** You have an Android app if you prefer that.

**Michael Gulmann:** There is a website that you can go to, and that's what Jason is going to take you through.

**Michael Gulmann:** You can email Otto, you know, in the very near future.

**Michael Gulmann:** And this is more just a decision of taking a couple of weeks to add it in, the infrastructure and the architecture is all set up for it.

**Michael Gulmann:** You can Slack Otto and ask Otto questions.

**Michael Gulmann:** You can use Teams to contact Otto.

**Michael Gulmann:** You can send Otto an SMS or a WhatsApp or an iMessage.

**Michael Gulmann:** And then at some point in the future, you know, you pick up the phone and you call Otto and you can talk to Otto.

**Michael Gulmann:** And so think of it more as Otto is a conversational agent that helps you book your travel.

**Michael Gulmann:** There's definitely some benefits when you have a web experience.

**Michael Gulmann:** And again, Jason will take you to this where you can show more visuals.

**Michael Gulmann:** You can show the logos of the airlines.

**Michael Gulmann:** You know, people are visual people and they see things that way.

**Michael Gulmann:** But that's something we take advantage of rather than that's the necessity of the product, if that makes sense.

**Erik O'Brien:** Yeah, absolutely.

**Erik O'Brien:** And just a quick follow before we jump in.

**Erik O'Brien:** And so we're kind of honing.

**Erik O'Brien:** And again, on personas, I know road warriors are kind of like top of mind, but would executive assistants themselves be able to use this for like multiple, like if they manage multiple executives?

**Michael Gulmann:** Yeah, we haven't added just for, I mean, this is more of a product decision for now.

**Michael Gulmann:** We haven't added the ability to impersonate the wrong word, to essentially be a second user on someone else's account.

**Michael Gulmann:** And so for now, that's not possible, but that's absolutely something that we're going to and will add.

**Michael Gulmann:** And so essentially, know, Otto will know that you are Erik O'Brien, but Otto will also know that you can come in and say, hey, Otto, I'm booking travel for Jason Flateboe, and then Otto will be able to know that you have a relationship.

**Michael Gulmann:** With Jason's account, and we'll go pull all of Jason's preferences, all of those things.

**Michael Gulmann:** So essentially, you're working within your account, and you're talking to Otto, no different than if you were an executive assistant, and you'd call someone and say, hey, I'm booking travel for my boss.

**Michael Gulmann:** But, you know, so as you can kind of hear by how I'm talking, that spec is built.

**Michael Gulmann:** That spec is well thought out.

**Michael Gulmann:** It's just a decision of, you know, we just haven't added it yet, because we're trying to narrow that go-to-market delivery.

**Erik O'Brien:** Yep, absolutely.

**Erik O'Brien:** Yeah, it was just something that we had kind of teed up as a potential persona, like the EA for an EA.

**Erik O'Brien:** But for now, we'll kind of remove that, and focus on more of the road warrior kind of executives.

**Michael Gulmann:** And Eric, expect this to be a two-way street as well.

**Michael Gulmann:** You know, if I jump fully into the GrowthX story that was shared with me initially by Marcel, is that, you know...

**Michael Gulmann:** Growthx becomes our product marketing and product content marketing team.

**Michael Gulmann:** Think of it as an in-house group.

**Michael Gulmann:** Then this is a two-way street.

**Michael Gulmann:** If you guys are going through and doing your research and you're seeing that there's a huge opportunity in the market for targeting that persona of the executive assistant, no different than if you were sitting in our office and you're working directly for our team, I'd expect you to say, hey, Michael, there's an opportunity here.

**Michael Gulmann:** If we build that in, that's a whole different segment that I can target.

**Michael Gulmann:** Think about that and let us know if you guys start uncovering some potential target audiences that we just haven't done yet.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Yeah, absolutely.

**Erik O'Brien:** I mean, I'm thinking of it very selfishly for ourselves.

**Erik O'Brien:** know, startups with multiple people that need to manage kind of travel.

**Erik O'Brien:** And if we have, you know, a couple office managers that are helping to manage that, if they...

**Erik O'Brien:** It would be able to be kind of power users.

**Erik O'Brien:** And so that's where the initial insight came from.

**Erik O'Brien:** But as we get into deeper research, we'll definitely let know kind of what we see as opportunities.

**Michael Gulmann:** Perfect.

**Jason Flateboe:** Thank you.

**Michael Gulmann:** All right.

**Michael Gulmann:** I'll turn it over to Jason to kind of take control and walk us through.

**Jason Flateboe:** Cool.

**Jason Flateboe:** All right.

**Jason Flateboe:** I'm going to share my screen.

**Jason Flateboe:** And I think it's worth actually just quickly starting on, like, if we imagine just sort of the full user journey.

**Jason Flateboe:** Let's take a moment to just sort of visit the web page, the landing page.

**Jason Flateboe:** Oh, great.

**Jason Flateboe:** I can't share my Zoom workspace on this new computer.

**Jason Flateboe:** I may have to sign out and give permission here and then come back in.

**Jason Flateboe:** Sorry, guys.

**Erik O'Brien:** Yeah, no worries.

**Jason Flateboe:** Yeah, it doesn't like this.

**Erik O'Brien:** actually not the first time it's happened this week.

**Jason Flateboe:** Yeah, I thought I already had this going.

**Michael Gulmann:** I actually found Mac is decently forgiving with not having to log out of Zoom, but it's last name very, I guess it varied.

**Michael Gulmann:** He's gone.

**Michael Gulmann:** So, Erik, reminder again, whereabouts are you based?

**Erik O'Brien:** I am currently in Iowa.

**Erik O'Brien:** I just moved here a couple months ago.

**Erik O'Brien:** was in Chicago for the last 15 years.

**Michael Gulmann:** That's a change.

**Erik O'Brien:** Quite a bit.

**Michael Gulmann:** Okay.

**Jason Flateboe:** All right, Jason, we'll get you back.

**Jason Flateboe:** You guys see this?

**Jason Flateboe:** Okay.

**Jason Flateboe:** So here's the current landing page we have.

**Jason Flateboe:** Obviously, there's a ton of changes coming to this in the next couple weeks as we open up the audience.

**Jason Flateboe:** We're going to have new content, new design, and all kinds of stuff here.

**Jason Flateboe:** But right now, this is the entry point for people to sign up and join the wait list.

**Jason Flateboe:** So essentially, they're popping their email in here.

**Jason Flateboe:** And then we, behind the scenes, are approving people sort of case by case and then letting them in after some amount of time.

**Michael Gulmann:** So, Michael, how long is this usually taking people before they get in?

**Michael Gulmann:** It's 100% my choice.

**Michael Gulmann:** It's, you know, it's kind of anywhere from six hours to three days.

**Michael Gulmann:** From six hours to three days, depending on kind of, you know, what traffic we're looking for and things like that.

**Jason Flateboe:** Yeah, yeah.

**Jason Flateboe:** So obviously that's our current state.

**Jason Flateboe:** We're going to be moving past that pretty quickly into a situation where people are getting in much, much quicker or even real time.

**Jason Flateboe:** So, but I just wanted to kind of start here.

**Jason Flateboe:** I know you guys have probably already looked through some of these screens, but this is where people are going to be coming from.

**Jason Flateboe:** And then when they land, obviously I am a user who already has used Otto, so you would not see this.

**Jason Flateboe:** But very quickly, we kind of talked through this.

**Jason Flateboe:** What Otto does when you get on is it's learning very quickly about your home airport, your preferences in terms of brands for both flights, hotels, what times you like to travel.

**Jason Flateboe:** We've kind of gone through all that stuff, but right away, you can start interacting with Otto to start planning a trip.

**Jason Flateboe:** And we actually have for new users, we have some sample trips where you can just.

**Jason Flateboe:** Click a button, and it's an example of, hey, want to go to Florida next Thursday, and right away, otter will just start bringing back flights.

**Jason Flateboe:** But in this case, I'm going to just ask for, this is a real trip I'm taking, I'm going to San Francisco, I think it's October 9th through 11th, and I only want Alaska Airlines.

**Jason Flateboe:** So, otter's going to start bringing back flights for me, it'll also, as I start picking my flights and making selections, it'll go into a hotel selection process, but it's basically going to plan my whole trip out around, not only these dates, but the preferences, and this is kind of a good example right here.

**Jason Flateboe:** Otter's telling me what it knows about me already, based on...

**Jason Flateboe:** And some travel preferences that have been collected on my previous flight.

**Jason Flateboe:** So as I'm using this more and more, Otto knows me better and better and is giving me more tailored trip selections.

**Jason Flateboe:** So here's my Alaska flights.

**Jason Flateboe:** I can see other parts.

**Jason Flateboe:** Let me just pause you on that, Jason.

**Michael Gulmann:** And, Erik, this is a big thing and probably one of the biggest differentiators and something I would expect quite a bit of content on if I was just writing it.

**Michael Gulmann:** It is really two different concepts.

**Michael Gulmann:** The first is that Otto learns from your interactions and gets better with every single experience.

**Michael Gulmann:** You'll hear me keep coming back to the concept of the best ever executive assistant because that's really what every single time a question comes up internally with the engineering team, with design.

**Michael Gulmann:** Whatever question it is, I'll come back with, well, what would the best ever executive assistant do?

**Michael Gulmann:** Okay.

**Michael Gulmann:** And so as you're working with an EA, then you say, hey, I really like flying Delta, but actually really what the main thing I want is a nonstop flight, things like that.

**Michael Gulmann:** Or what you just do is your EA presents you with a bunch of hotel options.

**Michael Gulmann:** And then after you've basically picked the Bonvoy or Marriott hotel three times in a row, then your EA kind of goes, aha, I think I figured out this person really likes Marriott hotels.

**Michael Gulmann:** And so Otto will do the same thing.

**Michael Gulmann:** It's learning as you go along.

**Michael Gulmann:** And so it's getting a better and better understanding of, you know, does this person really like flying in the mornings?

**Michael Gulmann:** There's a person like flying in the evenings.

**Michael Gulmann:** And the great thing is we haven't set up a, you know, kind of a, your typical key variable type of a thing where here are the 10 things that Otto learns.

**Michael Gulmann:** It literally learned down to nuances of, you know.

**Michael Gulmann:** I think this person always likes sitting on the right-hand side of the plane by the window when they're flying east.

**Michael Gulmann:** Without us telling Otto, that's something to go look for.

**Michael Gulmann:** And so this is part of that learning.

**Michael Gulmann:** And when Jason says, oh, it knows that, you know, I don't want red-eye flights.

**Michael Gulmann:** I prefer the front of the plane.

**Michael Gulmann:** You can read there.

**Michael Gulmann:** Obviously, the Alaska Airlines was in the actual request.

**Michael Gulmann:** But those are the types of things that Otto learns.

**Michael Gulmann:** And so what we really are calling that, what I'm calling that to lots of folks is, you know, this is the first of, I think, a breed of apps and applications and usages that are really going into hyper-personalization, right?

**Michael Gulmann:** This isn't just personalization of, you know, the basics of it remembers your name, it remembers your login, and, you know, your frequent flyer number, things like that.

**Michael Gulmann:** It'll do all that, but it's really hyper-personalization in the sense that it'll start personalizing based on things.

**Michael Gulmann:** No one ever taught it to personalize on.

**Michael Gulmann:** No one ever instructed it to personalize on these things, down to the level of hotels.

**Michael Gulmann:** So we had a user the other day who very excitedly told me, and I kind of said, yeah, that's what I would expect.

**Michael Gulmann:** He very excitedly told me that he was like, yeah, you know, I know I've used Otto to go to Philadelphia three times.

**Michael Gulmann:** And if I'm correct, I think it's actually Century City, which is a little town or a city outside of Philadelphia.

**Michael Gulmann:** He said, I searched for Philadelphia hotels, and because I end up always booking in Century City, it's actually now figured out to find me hotels in Century City.

**Michael Gulmann:** And he goes, the first option, the one I was recommending was the hotel I've stayed at before.

**Michael Gulmann:** I'm like, yep, that's how it would work, right?

**Michael Gulmann:** That's what the best of executive assistant would do.

**Michael Gulmann:** And that's that level of personalization where your Otto by itself starts narrowing in and finding that particular hotel because it knows.

**Michael Gulmann:** That's the hotel.

**Michael Gulmann:** But even beyond that, you say, I want to go to Chicago.

**Michael Gulmann:** Well, actually, by Chicago, maybe this user actually means they want to go to Highland Park specifically because they're visiting a company and Otto knows that the headquarters of that company is out in Highland Park.

**Michael Gulmann:** And it's that type of thing.

**Michael Gulmann:** So pair the self-learning and preferences with that hyper-personalization and start getting this experience.

**Jason Flateboe:** And just to add to that personalization story that Michael's talking about, think there's another kind of angle to this, too, where Otto knows your travel policy for your company, right?

**Jason Flateboe:** So you can copy-paste or upload that, and Otto will understand that you can only spend $300 a night on a hotel or, like, in this case, only refundable flights, right?

**Jason Flateboe:** So although there's a $150 Sabre fare, I can see these other fares if I want, but Otto knows that...

**Jason Flateboe:** The one that it should recommend is this $300 refundable because that's really all I'm ever going to buy.

**Jason Flateboe:** So it's saving me a step of like filtering through a bunch of different fares and just cutting to like what my travel policy is really calling for.

**Jason Flateboe:** And you can actually, this is made up, but there's actually a place where you can go interact with the Otto and tell it, you know, like I said, copy, paste your travel policy.

**Jason Flateboe:** You can modify it.

**Jason Flateboe:** I could say, hey, when I go to New York, San Francisco, or LA, actually get to spend $100 more per night on hotels and like it'll learn all those rules and figure that out.

**Erik O'Brien:** Any other, because I know that you're a current user, any other kind of preference center or preference like questions that are asked on like a new user?

**Erik O'Brien:** Before they start jumping into the experience.

**Jason Flateboe:** It's so it's not.

**Jason Flateboe:** And it's not patterned necessarily.

**Jason Flateboe:** It's sort of like the questions vary on how you're interacting with Otto.

**Jason Flateboe:** And it's learning sort of behind the scenes as you go as well.

**Jason Flateboe:** So like I think Michael mentioned earlier, like we used to have an onboarding flow where it was like, hey, what's your favorite airline?

**Jason Flateboe:** What's your favorite this?

**Jason Flateboe:** What's your favorite that?

**Jason Flateboe:** And we moved away from that into more of just an organic collection and like over time learning about the user.

**Jason Flateboe:** But Otto does ask, like, you know, if it's not sure, you know, it's sort of like, I think the design principle is more like ask at the right time to clarify and learn.

**Jason Flateboe:** Anything to add to that, Michael?

**Michael Gulmann:** No, just do you want to go into the preferences and you can show what Otto knows about you?

**Jason Flateboe:** Yeah, let's do that.

**Jason Flateboe:** So under user profile, we've got loyalty, travel preferences here.

**Jason Flateboe:** Here's where you can see where it goes a little deeper into things that I've told it, right?

**Michael Gulmann:** If you click for view, save preferences, you can kind of see the detail there.

**Michael Gulmann:** So this is how it's figured out.

**Michael Gulmann:** Should buy luggage?

**Michael Gulmann:** Never.

**Michael Gulmann:** That's not a key value pair that we've entered in.

**Michael Gulmann:** That's Otto has decided that it needs to track whether or not Jason ever wants to buy luggage.

**Michael Gulmann:** Yeah, it'll give you a sense of it.

**Michael Gulmann:** And this can be amazingly long.

**Michael Gulmann:** It can be three short.

**Michael Gulmann:** It can go down to the level of, you know, I think that user who found the same hotel that they've stayed at before probably would have a preferred hotel in Century City near Philadelphia and then that hotel name.

**Jason Flateboe:** Yep.

**Jason Flateboe:** And as you can see, these are all editable.

**Jason Flateboe:** So if I disagree with any of this stuff, I can cancel it.

**Jason Flateboe:** can chat with Otto about my preferences and say, hey, actually, I don't care that much about, you know, being in the front of the plane.

**Jason Flateboe:** This is sort of always evolving.

**Jason Flateboe:** You can always give it feedback.

**Jason Flateboe:** So it's always learning about you.

**Jason Flateboe:** Okay, let me go back into the trip.

**Jason Flateboe:** Okay, and so this is my outbound flight.

**Jason Flateboe:** So I'm going to choose this one.

**Jason Flateboe:** Otto is then going to move on to figuring out my return trip.

**Michael Gulmann:** As that's loading, Erik, he clicked the button.

**Michael Gulmann:** And this is when I say that, you know, having a desktop or an app allows us to have those visual cues.

**Michael Gulmann:** And you can interact with it.

**Michael Gulmann:** If Jason had, and Jason, I'll ask you to do this on the next one.

**Michael Gulmann:** If Jason just says, you know, pick the 11, 24 a.m.

**Michael Gulmann:** departure or pick the first one, then Otto would do that as well.

**Michael Gulmann:** Gotcha.

**Michael Gulmann:** So the whole point is it's completely conversational except for when we have the ability to make it a more rich experience.

**Michael Gulmann:** Yep, more than we can do that.

**Jason Flateboe:** I I hope.

**Jason Flateboe:** Bought this.

**Jason Flateboe:** Flight 1169, which I see is the first one.

**Jason Flateboe:** And I won't go all the way into the booking flow.

**Jason Flateboe:** actually don't have a real credit card in here, but it is worth talking about.

**Jason Flateboe:** So unlike, you know, every other travel site we've been on where there's a whole cart and a checkout flow and, you know, fill out this form and then are you sure?

**Jason Flateboe:** There's all those screens.

**Jason Flateboe:** So Otto knows this about me, but it doesn't know my payment details.

**Jason Flateboe:** So imagine I had already filled all this out.

**Jason Flateboe:** What I can do here is literally just say book it and it's done.

**Jason Flateboe:** So in the chat, I can say book that flight and just kind of amazingly, like, that's the end of it.

**Michael Gulmann:** So the idea is to kind of get rid of the whole checkout concept, right?

**Michael Gulmann:** Which is just like, you know.

**Michael Gulmann:** Get back to the best ever executive assistant.

**Michael Gulmann:** You're not going to worry about the credit card, what loyalty numbers you have.

**Michael Gulmann:** You're just like, yep, let's do the 6 o'clock flight out and then the 11 or whatever closest flight noon back from San Francisco.

**Michael Gulmann:** You know, my EA might say, well, you know, we can get you a much better seat if leave at 1 o'clock.

**Michael Gulmann:** I'm like, eh, don't worry about that.

**Michael Gulmann:** Let's get back at noon.

**Michael Gulmann:** And the EA would say, good.

**Michael Gulmann:** Right?

**Michael Gulmann:** And then they would handle all the payment details and all that.

**Erik O'Brien:** Yep.

**Jason Flateboe:** Okay, I'm going to ask it to do hotels.

**Jason Flateboe:** Actually, I'm not even going to tell it what city.

**Jason Flateboe:** I'm going to take a college tour at Stanford.

**Jason Flateboe:** See if Otto knows where that is.

**Jason Flateboe:** Just on that payment flow as well, too.

**Jason Flateboe:** Like, we don't ask users to fill out forms about their personal information or their credit card.

**Jason Flateboe:** Yeah, friend.

**Jason Flateboe:** smart.

**Jason Flateboe:** It's

**Jason Flateboe:** Until the right moment.

**Jason Flateboe:** So in that moment is when they're actually ready to make that first transaction.

**Jason Flateboe:** So again, I'm just trying to make like the setup process as light as possible and then make them do the work only when they need it at the right time.

**Jason Flateboe:** Okay, so hotels near Stanford University, it already has my dates, it knows my preferences, I'm gonna wanna marry on, refundable rates only, it knows my price limits.

**Jason Flateboe:** There may not be anything that's within my price limit, see.

**Michael Gulmann:** Jason, you have a policy set up for hotels?

**Jason Flateboe:** I do, it's kind of bogus stuff, I created it myself.

**Jason Flateboe:** It's not a real policy, but yeah, I can't remember what my limit was.

**Jason Flateboe:** Well, it'll tell me, this is kind of cool too, where, whoops.

**Michael Gulmann:** Not sure what happened.

**Michael Gulmann:** You clicked over to Tampa.

**Jason Flateboe:** Ah, ruined the demo here.

**Jason Flateboe:** Okay.

**Jason Flateboe:** So here's the hotels coming back.

**Jason Flateboe:** Okay.

**Jason Flateboe:** So this is kind of interesting too, where Otto's going to show me this is within policy and why.

**Jason Flateboe:** Oh, okay.

**Jason Flateboe:** There we go.

**Jason Flateboe:** There's my policy, 300 bucks.

**Jason Flateboe:** And it also shows me if it's, you know, if it's showing me something that it thinks I might be interested in, but it's slightly out of policy, it'll actually include that, but it'll call it out like it's out of policy and here's why.

**Jason Flateboe:** But, you know, in some cases, like you can't find something in policy.

**Jason Flateboe:** So it's kind of helpful to see those.

**Jason Flateboe:** Okay.

**Michael Gulmann:** The other key thing to highlight here, and we both want it to be front and center, but also not get in the user's way, is the why I recommend it.

**Michael Gulmann:** Right.

**Michael Gulmann:** So again, the same concept of the best service executive assistant, you know, sorry for that.

**Michael Gulmann:** But, you know, the EA would say, hey, I think I'll put you the residence in because it's the closest one to Stanford.

**Michael Gulmann:** And it's within company policy.

**Michael Gulmann:** And Jason, if you scroll up to the flights.

**Michael Gulmann:** And you'll also see that that is the recommendation there.

**Michael Gulmann:** You know, it's less clear, it's fully refundable.

**Michael Gulmann:** Morning departure, you get, you know, a longer business day in Seattle, and you also get your mileage plan accrual.

**Michael Gulmann:** And so depending on what you've asked, Otto, like if you do a super complicated, hey, I need to be at an 11 a.m.

**Michael Gulmann:** meeting in New York City, and then later I have to be in Boston for dinner, then part of the recommendation is why I recommend it is this is the only flight that will actually get you there for 11 a.m.

**Michael Gulmann:** meeting.

**Michael Gulmann:** And then, you know, and it pairs well with that, you know, flight up to Boston to get you to that dinner.

**Erik O'Brien:** Yep.

**Jason Flateboe:** Yep, that's a good call out.

**Jason Flateboe:** So I can see, you know, kind of the typical, if I want to see, you know, some of the images and all that kind of stuff, all the usual things that you would use to choose a hotel, we do that kind of table stakes stuff.

**Jason Flateboe:** But again, we're seeing more of the personalization here.

**Jason Flateboe:** All Bye-bye.

**Jason Flateboe:** Again, like why it's recommended, some amenities that are personalized to you that we know you care about, but I can go ahead and select that.

**Jason Flateboe:** And then the next thing I see is, so within the hotel that I selected, there's also a room type choice, right?

**Jason Flateboe:** And this has its own set of considerations, right?

**Jason Flateboe:** I might be able to, within policy, get the one-bedroom suite, but, you know, can I get the, or sorry, other way around.

**Jason Flateboe:** I can get the King Studio here, but, you know, the suite is not quite within policy.

**Jason Flateboe:** I can see why.

**Jason Flateboe:** But in some cases, there's trade-offs here that are interesting to travelers, right?

**Jason Flateboe:** Like for an extra 30 bucks, maybe within policy, I could get a junior suite or something like that.

**Jason Flateboe:** So we're really trying to help people maximize, like, the best thing that they can get for the trip.

**Erik O'Brien:** And sometimes they're not aware of those if they just choose the cheapest room.

**Michael Gulmann:** Just for  and grins, I have no idea what Otto's going to say, but let's imagine that Jason really wants to have a gym because he wants to work out, or the...

**Michael Gulmann:** Yeah.

**Michael Gulmann:** Really wants to have a tea kettle because he loves his ramen, so he can make his ramen, right?

**Michael Gulmann:** So you can ask here and say, which of these hotels can guarantee me a tea kettle?

**Michael Gulmann:** And maybe the answer is none of them, but Otto will actually go try to figure that out.

**Michael Gulmann:** His whole point is you can pretty much ask Otto anything, like, which of these is within walking distance of this building?

**Michael Gulmann:** Yeah, there you go.

**Michael Gulmann:** You know, but that's factual information.

**Michael Gulmann:** I've done this search before, and other hotels will say, yep, this hotel has a tea kettle in every room.

**Jason Flateboe:** And, Michael, I like the example that you've given before, too, which is the same case, but rooftop deck, right?

**Jason Flateboe:** Like, I'm going downtown, and I want to stay in a hotel where I can, you know, in the summer be out on a rooftop deck, and that's not an easy thing to find right now on a normal travel site, but Otto can find that for us.

**Jason Flateboe:** As can see, Be

**Jason Flateboe:** Okay, so I'm going to pick this hotel.

**Jason Flateboe:** So for this trip, really, a round-trip flight and a hotel for, I'm not sure what happened right there, round-trip hotel, or sorry, round-trip flight and a hotel is really the only components of this trip.

**Jason Flateboe:** You can imagine much more complex trips.

**Jason Flateboe:** We're building a trip planner view that'll help you sort of figure out a whole itinerary for a multi-city trip, like I'm going to New York.

**Jason Flateboe:** For a meeting on Tuesday at 11 a.m., and then I have a dinner in Boston the next night at 6 p.m., and then I want to fly home to Seattle.

**Jason Flateboe:** Otto can figure out that whole trip for me and figure out which flights are going to make the most sense in terms of times, how to get to Boston, whether I should take a red-eye or not.

**Jason Flateboe:** Obviously, it knows that I don't want to take a red-eye.

**Jason Flateboe:** So there's much more complicated trips than the one that I just showed you here that Otto really kind of excels at.

**Jason Flateboe:** I think that's an important thing to call out.

**Jason Flateboe:** Okay, just kind of thinking through.

**Jason Flateboe:** I haven't actually booked anything.

**Jason Flateboe:** I would be seeing all of my bookings here if I had real trips that I had paid for.

**Jason Flateboe:** You can see over here I have all these different flights or trips.

**Michael Gulmann:** Why don't I take over to share real quick and I'll show a book trip as well.

**Jason Flateboe:** Okay.

**Michael Gulmann:** All right.

**Michael Gulmann:** So here's kind of in my upcoming flights.

**Michael Gulmann:** This one's actually canceled, but I'll show you the whole flow here.

**Michael Gulmann:** So I started off, this was just two days ago, and this is a pretty unique example of a book, a specific hotel, Mercer Hotel in New York City for next week or for Wednesday of next week, one night.

**Michael Gulmann:** And then it goes and finds it.

**Michael Gulmann:** It finds it.

**Michael Gulmann:** That hotel, and then I say, book the cheapest room.

**Michael Gulmann:** All right, again, I never actually selected the hotel.

**Michael Gulmann:** never selected the room type with two very simple instructions.

**Michael Gulmann:** Book the Mercer hotel, book the cheapest room.

**Michael Gulmann:** It summarizes everything and says, here's the price.

**Michael Gulmann:** Do you want to confirm that?

**Michael Gulmann:** I say, yes, book it.

**Michael Gulmann:** So, I mean, this is about the shortest that you can do on any travel, anything to actually get it.

**Michael Gulmann:** And it books it.

**Michael Gulmann:** And here's my reservation number.

**Michael Gulmann:** And it added it to my calendar.

**Michael Gulmann:** And then the next morning, I went in and said, cancel my hotel room because it's $1,100.

**Jason Flateboe:** And I'm not staying in an $1,100 hotel.

**Michael Gulmann:** But for demo purposes, one of our investors really likes the Mercer hotel.

**Michael Gulmann:** And so I wanted to use that as an example.

**Michael Gulmann:** But cancel it.

**Michael Gulmann:** And then it says, hey, yeah, you can get a free cancellation until September 13th.

**Michael Gulmann:** So what was in that?

**Michael Gulmann:** Do you want to cancel?

**Michael Gulmann:** Yes.

**Michael Gulmann:** Cancel.

**Michael Gulmann:** Let me know if you need to cancel any other bookings.

**Michael Gulmann:** Yes.

**Michael Gulmann:** I Ah.

**Michael Gulmann:** Yes.

**Michael Gulmann:** Similarly, I can go into my itineraries, my upcoming here, I've got a trip out to New York next week, JFK, staying at the Pod Times Square Hotel, and then back on the 18th.

**Michael Gulmann:** So kind of a quick trip, and then down to San Diego and back.

**Michael Gulmann:** If I click in on this one as an example, I can see my itinerary here, load up and see all the details of that itinerary.

**Michael Gulmann:** You know, again, I can click change trip.

**Michael Gulmann:** I'll show you what I mean by we use buttons to do what really is language type things.

**Michael Gulmann:** If I click change trip, all it's going to do is jump to that conversation and automatically put in as if it was me saying, please change my trip.

**Michael Gulmann:** Right, so again, the whole point of Otto and almost everything we do is that it's fully conversational.

**Michael Gulmann:** Yep.

**Michael Gulmann:** But that's an example of a booked flight.

**Michael Gulmann:** Here's my flight that I booked.

**Michael Gulmann:** Not that exciting.

**Michael Gulmann:** You know, I did ask it how much more is premium economy.

**Michael Gulmann:** It tells me that.

**Michael Gulmann:** You know, I asked it if I can pick a seat, recap all my details, checking exit row availability, looks for an exit row for me.

**Michael Gulmann:** But, you know, if you say, I hate bulkheads, I want an aisle, which seat has the, you know, the most room within coach?

**Michael Gulmann:** I'll say exit row.

**Michael Gulmann:** How much is exit row?

**Michael Gulmann:** You say, you know, Otto will tell you, that's going to cost an extra $79.

**Michael Gulmann:** say, great, add that in, and Otto will handle all those things.

**Jason Flateboe:** Michael, this is maybe a good time to talk about, like, mid-trip, too.

**Jason Flateboe:** So, if you're already, you know, maybe you're halfway through your trip or you're just about to take your trip and something happens, your flight gets changed or canceled, like, we won't.

**Jason Flateboe:** How to handle those scenarios as well?

**Michael Gulmann:** Yeah, so booking a flight and booking a hotel is kind of the boring first bit.

**Michael Gulmann:** People have been able to do that online for a long time.

**Michael Gulmann:** Servicing a trip, especially for business travelers, is actually one of the biggest pain points.

**Michael Gulmann:** I remember from working at Egencia, which is one of the big corporate travel companies that's now a part of Amex GBT.

**Michael Gulmann:** One of the things there was that when something goes wrong or a user needs to change something, 80% to 90% of people call in.

**Michael Gulmann:** They're just not able to do it online, and the online systems aren't set up for it.

**Michael Gulmann:** With Otto, you can just go to Otto and say, hey, I'm not going to be able to make my flight back.

**Michael Gulmann:** Move it to the next day.

**Michael Gulmann:** Auto will confirm the change of your flight to the next day.

**Michael Gulmann:** And then realize that you have a hotel room booked as well.

**Michael Gulmann:** And then we'll ask if it needs to extend your hotel room.

**Michael Gulmann:** You say yes.

**Michael Gulmann:** And so little things like that, it's the servicing aspect that's one of the biggest pain points.

**Michael Gulmann:** People have to spend hours and hours on the phone with either the airline, the hotel, or call in to whatever travel company they booked it through.

**Michael Gulmann:** And now with Otto, you can just ask Otto, and they'll handle things for you.

**Michael Gulmann:** Since I'm not mid-trip, I can't show you an example of that.

**Michael Gulmann:** But maybe on this trip to New York, I'll just kind of fake do that and move my trip to the next day and just record it just so we have it.

**Erik O'Brien:** That'd be wonderful.

**Michael Gulmann:** So that's kind of it.

**Michael Gulmann:** I mean, it's brilliant in its simplicity is kind of the point.

**Michael Gulmann:** We're trying to figure out how do we put together product videos, and part of that is what things are going to pop out and what things are going

**Michael Gulmann:** Are going to showcase well.

**Michael Gulmann:** But the reality is, it's kind of like, you know, how do you show the Uber app?

**Michael Gulmann:** Well, you say, I need to go here.

**Michael Gulmann:** And then it says, you get a car coming.

**Michael Gulmann:** It's like, the whole point is really complicated stuff happens behind the scenes, but to the end user, it should just be simple.

**Michael Gulmann:** And you shouldn't have to be a travel expert in order to book your business travel.

**Michael Gulmann:** You shouldn't have to know all about that city.

**Michael Gulmann:** You shouldn't have to know where the headquarters of something is.

**Michael Gulmann:** Actually, speaking of which, let me see if I can go back and show one other here.

**Michael Gulmann:** Yeah, so here's an example of just kind of, you know, Otto knowing more than even a human, if you call him, talk to travel agent.

**Michael Gulmann:** And said, I'm heading to the Focusrite Conference in San Diego in November.

**Michael Gulmann:** Already have a hotel.

**Michael Gulmann:** I'll just need flights.

**Michael Gulmann:** So Otto starts going through this whole thinking process, which it minimizes after it's done.

**Michael Gulmann:** And you've probably experienced something like this in chat GPT, where it says, okay, you know, the focus for conference is scheduled November 18th through 20th.

**Michael Gulmann:** It's at the Manchester Grand Heights, San Diego.

**Michael Gulmann:** That means the person needs to get into San Diego International Airport.

**Michael Gulmann:** Here's their preferred airlines.

**Michael Gulmann:** Here's their hotel, but they've already got a hotel.

**Michael Gulmann:** So don't worry about that.

**Michael Gulmann:** Apparently, it decides to figure out what the weather is.

**Michael Gulmann:** I don't know why it's doing that, but this is the joy of working with an AI.

**Michael Gulmann:** And so it's got it.

**Michael Gulmann:** You're set for the Focusrite Conference.

**Michael Gulmann:** I found you flights.

**Michael Gulmann:** I say, actually, I prefer Delta on this trip.

**Michael Gulmann:** You know, and let's get in the evening.

**Michael Gulmann:** So then it says, okay, well, if you want to get an evening in Delta, here's pretty much your only flight.

**Michael Gulmann:** It's a good example of it doesn't show you extraneous stuff.

**Michael Gulmann:** And then I say, sounds good.

**Michael Gulmann:** And I select that, pick the flight back.

**Michael Gulmann:** And then this is where my preferences for seats is the most forward aisle seat in premium economy.

**Michael Gulmann:** And so it finds 10D and then 10C.

**Michael Gulmann:** It says continue it.

**Michael Gulmann:** And then I see save it for now.

**Michael Gulmann:** And so this is where we now got this save trip where it saved all the contacts for it.

**Michael Gulmann:** So I can say, now this was from a couple of days ago.

**Michael Gulmann:** I've gone and confirmed everything with my boss that, yep, I can go on this trip.

**Michael Gulmann:** And then Otto just goes now and confirms all the flight selections, makes sure that price is still valid.

**Michael Gulmann:** And we'll say, great, you're all set.

**Michael Gulmann:** Do you want to book it?

**Michael Gulmann:** And I can just say yes.

**Michael Gulmann:** So it just confirmed everything.

**Michael Gulmann:** I'll actually just book it.

**Michael Gulmann:** So I say, yep.

**Jason Flateboe:** Michael, you mentioned weather in there.

**Jason Flateboe:** It got me thinking, like, I could imagine Otto being smart enough to proactively say things like, hey, it just started snowing in Chicago.

**Michael Gulmann:** Like, there's something you don't want to go through Chicago.

**Jason Flateboe:** It's going to happen.

**Jason Flateboe:** Like, do you want me to rebook it through some other city?

**Jason Flateboe:** Like, that's not out of the realm of possibility.

**Erik O'Brien:** Are there any edge cases you guys have run into where it just hasn't been able to do something?

**Michael Gulmann:** Things that we know it can't do and things we haven't set it up for.

**Michael Gulmann:** You know, we've got a bunch of users.

**Michael Gulmann:** I think this was just some of the either TikTok or Instagram, you know, reels we were running.

**Michael Gulmann:** People, we had this slew of customers for about two weeks who would all come in and ask Otto to find the best cruise for them.

**Michael Gulmann:** And Otto's like, I don't do cruises.

**Erik O'Brien:** Um, so you'll have random things like that.

**Michael Gulmann:** Random things like that.

**Michael Gulmann:** Um, day of, if you're already checked into your flight, then the airline has taken control of your ticket, which means Otto, neither Otto nor any travel agency can actually touch that.

**Michael Gulmann:** Um, in which case, you know, Otto will spit you out and say, Hey, you need to call this number, uh, so someone can get ahold of the airline.

**Michael Gulmann:** Right.

**Michael Gulmann:** So we have not yet built Otto to be able to make a phone call to the airline.

**Michael Gulmann:** Um, and so we'll spit it out for human, um, human kind of takeover in that case.

**Michael Gulmann:** Um, but what Otto could do in that case as well is say, Hey, your, your, your flight's going to be severely delayed.

**Michael Gulmann:** I'll just book you a backup flight.

**Michael Gulmann:** It doesn't need to cancel out your original, um, even though you're checked in.

**Michael Gulmann:** And then if you take that other flight, then it can kick you off to human to say.

**Michael Gulmann:** Okay, go cancel my original.

**Michael Gulmann:** But anyway, here's my flight.

**Michael Gulmann:** It says it's confirmed.

**Michael Gulmann:** This is a real ticket.

**Michael Gulmann:** can go on Delta right now and look at that.

**Michael Gulmann:** And this is an example of where preferred cabin premium economy is actually not in my preferences.

**Michael Gulmann:** And so it just figured out, hey, looks like Michael's booked premium economy a couple times.

**Michael Gulmann:** This whole preferred seat, I'll seat as far forward as possible and comfort plus your premium economy.

**Michael Gulmann:** It's not too sure about that, so it's not pre-checked.

**Michael Gulmann:** I can check it.

**Michael Gulmann:** I'll leave it unchecked and I say, yep, add to preferences.

**Michael Gulmann:** So now, next time I do a search, it'll start finding new premium economies.

**Michael Gulmann:** But this is where it's kind of that, you know, it's learned by itself, but it's not going to just add it.

**Michael Gulmann:** In the future, once we have more signal, Audible will probably start adding some things by itself that it's over a certain percentage, you know, pretty sure about.

**Michael Gulmann:** But in this case, it asked me.

**Michael Gulmann:** But there's an example of literally, I did a search a couple days

**Michael Gulmann:** Days ago for, you know, flights down to San Diego.

**Michael Gulmann:** And then I said, hey, I'm not ready to book yet, but thanks for finding me on my flights.

**Michael Gulmann:** And I actually just thought of this.

**Michael Gulmann:** That's why I went into it.

**Michael Gulmann:** But, Erik, we were able to demo for you here that, you know, just went straight into that saved trip and say, yep, I'm ready to book it.

**Michael Gulmann:** And how many words did I use today?

**Michael Gulmann:** Five there, and then the word yes.

**Michael Gulmann:** So six words to basically say, yeah, just finish this booking.

**Michael Gulmann:** And we now have a booking.

**Michael Gulmann:** So now, because now I have two flights down to San Diego.

**Michael Gulmann:** I'm going to ask it to cancel right away, which you'll do and refund me since we were within 24 hours.

**Michael Gulmann:** So I don't get stuck with two flights.

**Jason Flateboe:** Michael, have you ever been stuck paying for something through your testing that you didn't actually want?

**Jason Flateboe:** I can imagine myself forgetting about something.

**Michael Gulmann:** One of our engineers booked a $1,200 hotel and didn't realize that they were booking it for that same day in New York.

**Michael Gulmann:** And so I was like, it's all good, but can you please call the hotel right now and ask them to cancel it?

**Michael Gulmann:** Because it was a non-cancelable.

**Michael Gulmann:** And so the hotel was like, oh, yeah, I see it here.

**Michael Gulmann:** We'll cancel right away because it just came into their system like 10 minutes before.

**Michael Gulmann:** But the joys of building a travel company.-life testing.

**Michael Gulmann:** So there you go.

**Michael Gulmann:** So now it's, oh, it's asking if I want to cancel it.

**Michael Gulmann:** Yes, I do.

**Michael Gulmann:** It always kind of just confirms saying, hey, you're going to get your money back.

**Erik O'Brien:** And then you mentioned, and this is more just my personal curiosity, you mentioned kind of multimodal being able to use calls or just talk to it.

**Erik O'Brien:** What are you guys using for like voice APIs?

**Michael Gulmann:** I think we're using Whisper, which is OpenAI's voice API.

**Michael Gulmann:** But honestly, we've been playing around with a couple of different ones.

**Michael Gulmann:** We're working with DeepGram.

**Michael Gulmann:** Oh, DeepGram, okay.

**Michael Gulmann:** For now, you can talk to Otto.

**Michael Gulmann:** Otto doesn't talk back yet.

**Michael Gulmann:** And again, these are more just proc decisions based on what we feel like we need to get ready.

**Michael Gulmann:** But yeah, so you kind of see the little talk down here.

**Michael Gulmann:** It'll just record what I'm saying and then translate that.

**Michael Gulmann:** But I think it was about two months ago, we had a little test demo where you were just literally just talking back and forth, just like you would with ChatGT and others.

**Michael Gulmann:** But I think we looked at DeepGram as well.

**Erik O'Brien:** But yeah.

**Erik O'Brien:** Yeah, they're, I think GPT real time.

**Erik O'Brien:** And it's really good for back and forth, like voice.

**Erik O'Brien:** And then there's 11 labs, which are like more expressive voices, but it's mainly for like creators and media agencies.

**Erik O'Brien:** So, but yeah, DeepGram, think at least they beat everyone on cost for both speech-to-text and text-to-speech.

**Erik O'Brien:** And then they have their own voice AI API that they're just rolled out a couple months ago.

**Erik O'Brien:** So, but yeah, between...

**Michael Gulmann:** If you're chatting with them and they want to do some sort of a joint marketing, joint demo, I'm happy to quickly implement DeepGram and then we could do something joint.

**Michael Gulmann:** think it'd be, you know, given the fact that every single AI company, or at least, you know, ChattyBT, Perplexity, Claude, whenever they release new models, they always give an example of finding a hotel, even though they never show the booking, never show the transaction because they can't...

**Michael Gulmann:** If they always use travel as an example, that may be an interesting thing for DeepRam to do if they want to kind of showcase how a travel company like Otto is doing that, and then we can boost each other.

**Erik O'Brien:** Absolutely.

**Erik O'Brien:** Yeah, we just kicked off with them a couple weeks ago, so we're still in the kind of calibration phase as well, but as soon as we get into those.

**Michael Gulmann:** As you're chatting with them, if they want an intro or they're interested, then just let me know, and I'll be happy to reach out.

**Erik O'Brien:** Wonderful.

**Michael Gulmann:** What else can we tell you?

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Who, if any, are direct competitors to you guys?

**Erik O'Brien:** Because I know there's people doing it on Expedia and businessbooking.com, but are there any other, like, direct, direct competitors you guys have seen out in the market?

**Michael Gulmann:** Um...

**Michael Gulmann:** I mean, the answer is, I'm sure there is.

**Michael Gulmann:** And I'm sure there's probably 10 other companies working on something similar.

**Michael Gulmann:** I haven't seen any yet that are as far along as we are.

**Michael Gulmann:** I'm trying to think of...

**Erik O'Brien:** I know Swifty is one out of the UK.

**Michael Gulmann:** Yeah, Swifty, I've talked to them.

**Jason Flateboe:** They've shut down.

**Erik O'Brien:** Yeah.

**Michael Gulmann:** They actually, well, I won't say too much more, but they 100% confirmed or shut down.

**Michael Gulmann:** No.

**Michael Gulmann:** They couldn't raise money.

**Michael Gulmann:** And part of it was, this is what I'm saying, was very, very limited.

**Michael Gulmann:** As an example, that example I showed you, or Jason just did, of finding a flight to San Francisco, it would give back one flight on American Airlines.

**Michael Gulmann:** And so I asked...

**Michael Gulmann:** The CEO, I'm like, why are only doing one flight?

**Michael Gulmann:** He's like, oh, because we couldn't get the connections into all the airlines.

**Michael Gulmann:** And so it's things like that, that, you know, they're super nice guys, but they just couldn't make it go.

**Michael Gulmann:** Let me look for...

**Jason Flateboe:** I think that's just calling out, Michael, like how much work and effort and time it took just to do the transactional piece and get real flight hotel results and bookings.

**Michael Gulmann:** This is complicated stuff.

**Jason Flateboe:** Yeah, like nobody else is really going to be able to just slam that in and like put it out.

**Michael Gulmann:** Like it's not the idea, it's the implementation.

**Michael Gulmann:** Biztrip.ai, B-I-Z, like business, but short and cool.

**Michael Gulmann:** Biztrip.ai came out with a big announcement.

**Michael Gulmann:** But everything we can read or try to find out.

**Michael Gulmann:** can't.

**Michael Gulmann:** it

**Michael Gulmann:** It's not actually up and running.

**Michael Gulmann:** It's more of a, we assembled some great founders and some money, we're going to tackle this space.

**Erik O'Brien:** They've got Andrew Ng on there, co-founder.

**Michael Gulmann:** They do.

**Michael Gulmann:** So that's what I'm saying.

**Michael Gulmann:** So some big names and things like that.

**Michael Gulmann:** They don't have a ton of folks in the travel industry.

**Michael Gulmann:** They have some.

**Michael Gulmann:** but, but like I said, from when they announced in end of July to now, they're just, it's been, it's been pretty silent.

**Michael Gulmann:** Um, and then the other one is Skylink, S-K-Y-L-I-N-K.

**Michael Gulmann:** And I think best we can tell is that they pivoted because they couldn't get a whole lot of traction.

**Michael Gulmann:** They pivoted to try to be more of a back office operations.

**Michael Gulmann:** And travel AI.

**Michael Gulmann:** So when a human travel agent is answering a phone or needs to do some things, then Skylink will help with some of the back office operations.

**Michael Gulmann:** That's what I think that they've moved to now.

**Michael Gulmann:** They're really highlighting a partnership with Cornerstone, which is kind of a back office travel provider.

**Michael Gulmann:** But they were in there as well.

**Michael Gulmann:** Again, Skylink.

**Michael Gulmann:** Those are kind of the two with Swifty, kind of the three that are in there.

**Michael Gulmann:** Swifty's gone.

**Michael Gulmann:** Skylink looks like it's pivoting.

**Michael Gulmann:** And BizTrip.ai hasn't really launched.

**Erik O'Brien:** And then kind of more mindshare competitors.

**Erik O'Brien:** Is that the typical kind of retail?

**Michael Gulmann:** Well, it's, no, so you would have in there Navon Trip Actions.

**Erik O'Brien:** Navon Trip Actions, yep.

**Michael Gulmann:** Yeah, no, it was the same company, but whenever you, their rebrand was so bad that everybody in the industry still calls them Navon Trip Actions because most people know them as Trip Actions.

**Michael Gulmann:** And so if you use their new name, Navon, everyone's like, what's that?

**Michael Gulmann:** You go, that's Trip Actions.

**Michael Gulmann:** And they go, oh, that's right.

**Michael Gulmann:** So, but they, listen, they're fantastic at marketing.

**Michael Gulmann:** They put themselves out there as the newfangled.

**Michael Gulmann:** They're the new breed of corporate travel.

**Michael Gulmann:** But again, they haven't really released anything.

**Michael Gulmann:** I think their last demo that I saw was about a year and a half ago on AI.

**Michael Gulmann:** And it was, think of it as a, a, a, a, a single input window or a single input field where you would type in, I need to go on a business trip to XYZ.

**Michael Gulmann:** And then it would.

**Michael Gulmann:** Pre-fill-in to their homepage wizard, and then you have to click the button, and you're back in the regular flow.

**Michael Gulmann:** So nothing really conversational.

**Michael Gulmann:** Now, I don't doubt the fact that they're...

**Michael Gulmann:** Exactly.

**Michael Gulmann:** It helps you fill out the form field faster, but I'm sure that they are working on stuff.

**Michael Gulmann:** They'd be insane not to.

**Michael Gulmann:** The problem is always the legacy code they have.

**Michael Gulmann:** They've already got a flow built in.

**Michael Gulmann:** So are they going to...

**Michael Gulmann:** If you notice, with Otto, there is no specific flow.

**Michael Gulmann:** There's no step one, step two, step three.

**Michael Gulmann:** At any given point, you can go from step three back to step one.

**Michael Gulmann:** You can save your progress and then come back three days later and pick it back up.

**Michael Gulmann:** There's no kind of...

**Michael Gulmann:** There's no one through X type of a flow.

**Michael Gulmann:** So for a lot of these companies, that's the difficult thing for them is to kind of use their APIs.

**Michael Gulmann:** They're on internal APIs to...

**Michael Gulmann:** To try to create that new experience.

**Michael Gulmann:** So, Navon, TripActions.

**Michael Gulmann:** AmexGBT is probably the largest travel management company out there.

**Michael Gulmann:** They just recently got approved to purchase CWT, Carlson Wagon Leap.

**Michael Gulmann:** That was sitting in the regulators for about a year and a half, so that was just approved.

**Michael Gulmann:** I haven't heard, nor do I really know what they're working on, but I'd imagine that they have to be working on stuff as well.

**Michael Gulmann:** And then the other big legacy technology player is Concur.

**Michael Gulmann:** And Concur, you know, founded in the late 90s or mid-90s, mainly as an expense company, went on to create what they call the online booking tool.

**Michael Gulmann:** And so they've been licensed and sold that online booking tool to all of these travel agencies.

**Michael Gulmann:** These are...

**Michael Gulmann:** Corporate travel agencies that didn't have technology departments.

**Michael Gulmann:** And so if you're a legacy player in the year 2002, and you have, you know, thousand people sitting in a call center who are all answering phones, 1-800 number phones, and then Concur came along and said, we'll give you a web front end that integrates into your existing workflows.

**Michael Gulmann:** All these companies said, yes, please.

**Michael Gulmann:** And so Concur became almost the de facto front end for corporate travel.

**Michael Gulmann:** Steve Singh, who's the co-founder of Concur, is the biggest investor through Madrona in Otto and is, yeah, I'll leave it at that, and is our chairman.

**Michael Gulmann:** And so, you know, he clearly believes in Otto over the company that he founded some 20 plus years ago.

**Michael Gulmann:** So, but at the same time, you

**Michael Gulmann:** If I'm sitting at Concur, this is definitely part of my board meeting.

**Michael Gulmann:** This is definitely part of my conversations every single day is how do we build out a conversational AI?

**Michael Gulmann:** So I would hope for their sake that they're building this.

**Michael Gulmann:** And frankly, part of the fact that the legacy players are all trying to do this, if they announce that they're trying to, and then we can double down on that and say, yeah, but we're actually doing it.

**Michael Gulmann:** I think it builds the story quite a bit.

**Michael Gulmann:** So that's why I'm not, I guess part of that, I'm not afraid of those legacy players because I don't think they're as nimble or can move as fast, but it validates the story.

**Michael Gulmann:** But if I was, you know, building out keywords and building out stories, it's how does Otto compare against Concur?

**Michael Gulmann:** How does Otto compare against Navon trip actions?

**Michael Gulmann:** How does Otto compare against Amex GBT?

**Michael Gulmann:** You know, I'd probably, I'm not sure if I would go into biz trip.

**Michael Gulmann:** can see it.

**Michael Gulmann:** So

**Michael Gulmann:** Or Skylink, just because they're, you know, BizTrip will probably get traction because of the names attached.

**Michael Gulmann:** Skylink hasn't really.

**Michael Gulmann:** One of the things they announced was that they're now part of the, I forget what travel company, but they're part of some marketplace.

**Michael Gulmann:** But it's no different than being in the app store.

**Michael Gulmann:** if nobody downloads it, it doesn't do anything kind of a thing.

**Michael Gulmann:** But you'll see an announcement out there for, that they, that they joined some marketplace.

**Michael Gulmann:** I think it's BDC, BD something.

**Michael Gulmann:** Skylink, Ordner, Marketplace.

**Michael Gulmann:** BCD Travel.

**Erik O'Brien:** BCD Travel.

**Michael Gulmann:** So BCD Travel said that Skylink is now in the.

**Michael Gulmann:** BCD Marketplace, which I think we can become if we pay them $1,000 as well.

**Michael Gulmann:** I just don't see that as a go-to-market strategy, but yeah.

**Michael Gulmann:** That's about as much of a dump as I can give you on competition.

**Erik O'Brien:** Yeah, no, that's super helpful.

**Erik O'Brien:** Anything else I didn't ask that you guys want to mention for Product Deep Dive?

**Michael Gulmann:** Yeah, think we covered a lot.

**Michael Gulmann:** Travel policy is in there, so that certainly exists.

**Michael Gulmann:** Oh, so important thing with travel policy.

**Michael Gulmann:** Also, what we do not do versus what we do do, especially as you're writing our content to make sure it's accurate.

**Michael Gulmann:** ...

**Michael Gulmann:** ...

**Michael Gulmann:** ...

**Michael Gulmann:** ...

**Michael Gulmann:** ...

**Michael Gulmann:** We don't do approval routing.

**Michael Gulmann:** So that's a process that I think about.

**Michael Gulmann:** If you look at the legacy travel management companies, and you'll have like a Microsoft and small companies and mid-sized companies sign up with these travel management companies.

**Michael Gulmann:** They're called TMCs, right?

**Michael Gulmann:** For these TMCs, about 20% of the ones who have a travel policy, and almost all of them have travel policies, about 20%, will require approval routing.

**Michael Gulmann:** That can either be because you're trying to book a hotel that's over policy, and then you click a button and an email goes to your boss to click another button that says, yes, I approve this.

**Michael Gulmann:** Or some companies are so locked down that the approval routing has to happen in order to even approve you going on the business trip.

**Michael Gulmann:** So some of these big companies, they really want to lock down costs.

**Michael Gulmann:** They're like, yeah, your manager needs to approve for you to go visit that client.

**Michael Gulmann:** up.

**Michael Gulmann:** Thank you.

**Michael Gulmann:** So managers are clicking accept every single day because obviously they want their people to travel, but they've set that in.

**Michael Gulmann:** We do not do any approval router.

**Michael Gulmann:** So what you saw Jason showed is that this is in policy, this is out of policy.

**Michael Gulmann:** That's a guide and a helpful thing for the users of Otto.

**Michael Gulmann:** But at the end of the day, they can book whatever they want.

**Michael Gulmann:** So again, and this is mainly because we're not trying to go compete in that space.

**Michael Gulmann:** We really just want to be the best ever executive assistant.

**Michael Gulmann:** And the best ever executive assistant is going to tell me, hey, Michael, you know, I know you need to be in London, but the only seat available is in premium economy.

**Michael Gulmann:** There's no more coach seats and our policy is to fly coach.

**Michael Gulmann:** I'd say, how much more is it?

**Michael Gulmann:** She'd be like, eh, it's $300 more.

**Michael Gulmann:** I go, yeah, go ahead and book it anyway.

**Michael Gulmann:** Right.

**Michael Gulmann:** So I've gotten the feedback on, is it in policy or not?

**Michael Gulmann:** And I've decided that I'm going to book it anywhere.

**Michael Gulmann:** And that's the experience we want.

**Michael Gulmann:** So, but that's something we do.

**Michael Gulmann:** Not to do is that kind of email routing of approval.

**Michael Gulmann:** We don't do cars, car rentals.

**Michael Gulmann:** We don't do cruises.

**Michael Gulmann:** We don't do restaurant reservations.

**Michael Gulmann:** Those are all things to come.

**Michael Gulmann:** It's flight and hotel for now, which is the two major components of your trip.

**Michael Gulmann:** All the servicing around it.

**Michael Gulmann:** And then you said, Expense management is coming later.

**Michael Gulmann:** Expense management is later.

**Michael Gulmann:** Also don't do that yet.

**Michael Gulmann:** We have full receipts, and those receipts are formatted in a way that they can very easily be imported into an expense management tool.

**Michael Gulmann:** So you can just download the PDF, and it'll get sent to you as well, and then that automatically routes to your expense management system.

**Michael Gulmann:** So in some ways, we are connected through, but we don't have the one-click or automatic feed over to an expense management

**Jason Flateboe:** We only do one travel, right?

**Jason Flateboe:** Like, if you want to bring your wife, you can't book two tickets.

**Jason Flateboe:** If you want to book for your whole team, you can't do that right now.

**Michael Gulmann:** It's like one traveler.

**Michael Gulmann:** That's more narrowing the scope.

**Michael Gulmann:** That's us forcing the narrowing of the scope versus, you know, long-term capabilities.

**Michael Gulmann:** Yep.

**Jason Flateboe:** We're not helping.

**Jason Flateboe:** We're not doing flexible search, Like, if people say, hey, find me the cheapest flight next month, like, that's not what we're doing.

**Michael Gulmann:** You need to know.

**Michael Gulmann:** Yeah, so very much, Erik, you know, you think of a business traveler, right?

**Michael Gulmann:** They're going to a conference.

**Michael Gulmann:** They're going to go meet with the client.

**Michael Gulmann:** They're going to go do whatever.

**Michael Gulmann:** That client meeting is set for 2 p.m.

**Michael Gulmann:** in Chicago.

**Michael Gulmann:** Like, you know, the use case is I need to get to that meeting.

**Jason Flateboe:** It's not what's the best time to go to Hawaii.

**Michael Gulmann:** What's the cheapest flight to Hawaii in August?

**Michael Gulmann:** That's great.

**Michael Gulmann:** If someone's building that, I'll probably go use it, but that's not what Otto's built for.

**Erik O'Brien:** Yeah, I saw an interesting one.

**Erik O'Brien:** Poke by Interaction.

**Erik O'Brien:** They came out with one.

**Michael Gulmann:** Poke as in Poke someone?

**Erik O'Brien:** Yep, P-O-K-E.

**Erik O'Brien:** Interested to see where that goes.

**Erik O'Brien:** They just launched their kind of teaser film last week.

**Michael Gulmann:** Wow, and a $15 million seed round.

**Erik O'Brien:** Yeah.

**Michael Gulmann:** That's not small.

**Erik O'Brien:** No.

**Erik O'Brien:** So they've made a lot of promises, and it looks like it's just interacting through text message versus having another interface or app to download.

**Michael Gulmann:** It's...

**Erik O'Brien:** Interesting.

**Erik O'Brien:** I've got a lot of questions about it.

**Erik O'Brien:** It's iOS only.

**Jason Flateboe:** I'm an Android guy, so...

**Jason Flateboe:** Mm-hmm.

**Michael Gulmann:** Oh, so iMessage only, it looks like.

**Erik O'Brien:** It's interesting.

**Erik O'Brien:** Yeah.

**Michael Gulmann:** I'll go take a look at them after this.

**Jason Flateboe:** Yeah, check it out.

**Erik O'Brien:** All right.

**Erik O'Brien:** Awesome.

**Michael Gulmann:** Again, appreciate the time and all details.

**Michael Gulmann:** Yeah, as you keep going, and Jason, I don't know if you can set up Erik and a few others with, or maybe just send across some one-time codes, and then you can just log in by yourself and start playing.

**Michael Gulmann:** Yeah.

**Michael Gulmann:** If you go to, if you go to ottotheagent.com, and then top, just click log in.

**Michael Gulmann:** If you just put in your email address, it'll say, hey, I don't find this, I didn't find this user or this email.

**Michael Gulmann:** Do you have a one-time code to get into the beta?

**Michael Gulmann:** And then the codes Jason's going to send, Jason, if you want to send like five across, just mark them all as used.

**Jason Flateboe:** Okay, great.

**Erik O'Brien:** Cool.

**Michael Gulmann:** Thanks, Erik.

**Jason Flateboe:** Thanks, Jason.

**Erik O'Brien:** Yeah, thank you.

**Erik O'Brien:** Thanks, guys.

**Jason Flateboe:** Have a good weekend.

**Jason Flateboe:** Yeah.
