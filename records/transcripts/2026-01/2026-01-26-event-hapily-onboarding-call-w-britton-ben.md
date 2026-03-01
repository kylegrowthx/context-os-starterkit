# event·hapily Onboarding Call w/ Britton + Ben

<metadata>
date: 2026-01-26
time: 19:00 UTC
duration: 33 minutes
organizer: jesus@growthx.ai
participants:
  - name: Ben Francis
    email: ben@hapily.com
    company: hapily
    role: Director of Customer Success
  - name: Jason Gong
    email: jason@growthx.ai
    company: GrowthX
    role: Operations
  - name: Britton Wright
    email: britton@hapily.com
    company: hapily
    role: Sales/Onboarding
  - name: Gloria Willis
    email: gloria@growthx.ai
    company: GrowthX
    role: Demand Generation
  - name: Jesus Yepez
    email: jesus@growthx.ai
    company: GrowthX
    role: CEO
fathom_recording_id: 117171241
fathom_url: https://fathom.video/calls/542873809
share_url: https://fathom.video/share/EoCNq8HSrQounnbfEK2TbTp7WT4syhg7
source: fathom
enriched_on: 2026-02-28 12:30 UTC
</metadata>

---

## Summary

GrowthX transitions from Britton Wright to Ben Francis as primary hapily contact. The team diagrams a 3-part Zapier integration to sync Luma registration data to HubSpot, enabling event attribution and post-event analysis through hapily's registrant data model. Previous implementation by Kyle was incomplete; Jason owns the build effort.

---

## Context

GrowthX's event engine relies on Luma for registration (front-end UX, audience messaging, low-friction signups) and hapily for backend tracking and deal attribution. The previous implementer, Kyle, started the integration but departed before completion, leaving Luma registration data unsynced to HubSpot. This blocks GrowthX's primary use case: understanding which events influenced closed deals and revenue. Ben Francis takes over as long-term support contact from Britton Wright, bringing deep HubSpot and hapily workflow expertise from his role as Director of Customer Success.

Luma is increasingly popular across GrowthX's ecosystem, and hapily acknowledges this but has not yet prioritized direct integration. The solution is a GrowthX-owned Zapier implementation that mirrors Luma's registration flow into hapily's custom objects (Event, Registrant, Contact, Session) in HubSpot, then leverages hapily's built-in deal attribution workflows to claim credit for won deals.

---

## Relevance

**Event Attribution & Revenue Impact**
- Hapily provides the infrastructure to track which events influenced closed deals
- Without Luma→HubSpot sync, this entire system is non-functional
- GrowthX holds all event data in Luma but cannot report on ROI

**Technical Ownership**
- Jason Gong owns the Zapier build and will be the point of contact for technical questions
- Britton and Ben will provide guidance on hapily workflows and HubSpot data model
- Support model is asynchronous (Loom videos, email) rather than real-time Slack

**Product Roadmap**
- Luma integration is on hapily's roadmap but not prioritized yet
- Multiple customers (Signify, others) have requested this; Luma is a California/venture ecosystem phenomenon
- Ben is exploring how to "make Luma less painful" for future customers

---

## Overview

- **Support Transition:** Britton is handing off as primary contact to Ben Francis, hapily's Director of Customer Success, who will be the long-term resource for reporting and advanced use cases.
- **Integration Gap:** GrowthX's Luma registration data is not syncing to HubSpot, blocking event attribution. This is because the previous setup was incomplete after the original implementer (Kyle) departed.
- **Solution Path:** A 3-part Zapier integration is required to sync Luma data to hapily's custom objects in HubSpot. This is a GrowthX-owned build, as hapily does not offer direct Luma integration.
- **Core Use Case:** GrowthX will use hapily as a backend system of record for post-event analysis and deal attribution, while Luma remains the front-end registration tool.

---

## Key Topics

### Problem: Incomplete Luma → HubSpot Integration

- The previous setup, built by Kyle, was incomplete, leaving Luma registration data unsynced to HubSpot.
- This prevents GrowthX from using hapily for its primary goal: event attribution and ROI reporting.
- The team's focus is on using hapily as a backend system of record, not for its native registration pages.

### Solution: 3-Part Zapier Integration

A 3-part Zapier integration is required to sync Luma data to hapily's custom objects in HubSpot:

**Part 1: Event Sync**
- **Trigger:** New event in Luma.
- **Action:** Create/update `Event` object in HubSpot.

**Part 2: Registrant Creation**
- **Trigger:** New registration in Luma.
- **Action:**
  1. Find the corresponding `Event` object in HubSpot (match by event name).
  2. Get the HubSpot `record ID` for that event.
  3. Update the registrant's HubSpot `Contact` record by populating a webhook property with the event's `record ID`.
  4. This action automatically triggers hapily to create the `Registrant` object, linking the contact to the event instance.

**Part 3: Status Updates**
- **Trigger:** Status change in Luma (e.g., registered → attended).
- **Action:**
  1. Find the specific `Registrant` object in HubSpot (match by email AND event name).
  2. Update the `status` property on that `Registrant` record.
- **Status Mapping:** GrowthX must map Luma statuses (e.g., "approved," "waitlisted") to hapily's standard statuses ("registered," "attended," "canceled").

### hapily's Data Model & Attribution

Hapily's data model enables granular tracking and reporting:
- **`Event`:** The event itself.
- **`Contact`:** The individual.
- **`Registrant`:** The crucial link object. It represents a specific contact's registration for a specific event, storing status and attendance data. One-to-one relationship per event per contact.
- **`Session`:** A child object of `Event` for tracking attendance at individual sessions within a larger event (e.g., a conference).

**Deal Attribution:**
- The `Deal Attribution` workflow automatically links deals to events based on registrant status (e.g., "attended"), a defined look-back window, and optional filters (e.g., pipeline, deal owner).
- Workflows can filter by deal stage, pipeline, or deal owner to claim only relevant deals.
- A secondary workflow fires when a deal is won to mark the event as "influenced."

### Support & Roadmap

- **Support Channels:** Ben provides asynchronous support via Loom videos and email. Direct Slack integration is avoided to manage expectations around instant support.
- **Luma Integration:** Ben confirmed Luma is on hapily's roadmap for a potential direct integration, driven by growing adoption in venture/startup ecosystems. However, prioritization is TBD.

---

## Action Items

**Jason Gong (GrowthX)**
- Audit Luma fields vs HubSpot; map Luma statuses to Registrant Status
- Build 4 Luma→HubSpot Zaps (event create, event update, registrant create, status update)
- Test integration with Thursday's event

**Jason Gong (GrowthX)**
- Review deal attribution workflows in hapily
- Configure conditions (which pipelines, deal stages, or deal owners to include)

**Britton Wright (hapily)**
- Schedule working session with Jason Gong + Gloria Willis to review workflows and reporting options

---

## Transcript

**Jesus Yepez:** Nice, nice to hear that.

**Jesus Yepez:** This meeting is being recorded.

**Britton Wright:** Great to meet you.

**Britton Wright:** Yeah, I know I was working with Gloria and Kyle mostly doing the onboarding.

**Britton Wright:** So are you going to come in as well to help out with the event happily?

**Jesus Yepez:** Yeah, and I think Jason and Gloria should be coming as well.

**Ben Francis:** Great.

**Britton Wright:** Awesome.

**Ben Francis:** Is your team fully remote?

**Jesus Yepez:** Yep, but there's an office in San Francisco as well for San Francisco-based people.

**Britton Wright:** All right.

**Britton Wright:** Oh, awesome.

**Gloria Willis:** Hey there.

**Britton Wright:** Hey, Gloria.

**Gloria Willis:** Hello.

**Gloria Willis:** How are you?

**Britton Wright:** Good.

**Gloria Willis:** Good, good.

**Gloria Willis:** Hi, Ben.

**Ben Francis:** Nice to meet you.

**Ben Francis:** Great to meet you.

**Gloria Willis:** Yes, nice to meet you.

**Britton Wright:** Hi.

**Britton Wright:** Gloria, I was a little jealous of you. We got hit with an ice storm this weekend, and I know you're not that far down.

**Gloria Willis:** No, I'm based in Southern California, so it normally would have been fine, but I'm actually in Texas, so I got the full brunt of the storm. Oh, yeah, I was going to say, Dax had snow in his front yard, and Jonathan in Austin, who works on my team, he said it's a bit chilly where he is, too.

**Gloria Willis:** Yes, yeah, the ground is covered, so my flights were canceled. And now I'm still here, which is nice, I'm with family, but it's still rough, because it's crazy.

**Ben Francis:** Yeah.

**Britton Wright:** Awesome. Well, you know, really the point of this call is really a transition, but also to introduce you guys to Ben, right? So he's the main point of contact long-term. He's our director of customer success. He's the big brand that I go to anytime I don't have an answer to a question I need.

**Britton Wright:** But yeah, and Ben, like I mentioned on the call last time, Gloria, Ben is really going to be a great resource for reporting and things like that and making sure that, like, as you guys get more mature with your use of EventHappily, that you can leverage it even further.

**Ben Francis:** Yeah. Hey, guys. Great to meet you. I run everything post-sale here on the Happily side. So hopefully the transition from Britton to me won't be too jarring. I did teach him everything he knows about Happily. So in theory, I should know as much as he does.

**Ben Francis:** But yeah, so like any of those, how can I get the most value? What do other clients do? I mean, really any question as it relates to what you're trying to utilize Happily for. Happy to be that thought partner. I'll try to sprinkle some HubSpot magic on where I can. We've been in the Orange Playground for a good while now that we know a hack or two. So really excited to be supporting your team long term.

**Gloria Willis:** Great. Great. Well, I'm glad to hear that because Jason and I spent lots and lots of time last week kind of messing around in HubSpot and starting to play around with some of the like reports through EventHappily and walked away with lots of thoughts. So very interested to see what you all have and what you would recommend for like the best reporting options that we have, whether it's a nice dashboard or whatnot. But also, I don't know, Jason, if you'll have some questions on like the things that we were able to pull and finding out if there's a faster, easier way that EventHappily can do it.

**Jason Gong:** Or, you know, just trying to get everything in alignment so you're putting the best use of it. I think, I guess the context is like we had a robust person help us set it up, Kyle, and then he kind of left to pursue another full-time job. And then like everything's kind of like half built and we're not really using anything. And we're trying to pick up the pieces and figure out how to get it usable.

**Jason Gong:** And that's the context, so we're really looking for as much help as we can get right now.

**Britton Wright:** Yeah, maybe that's my misunderstanding. So to my understanding that when I was working with Kyle, that you guys are set up to host events, right? I think the main pain point that we were really dealing with was that Luma integration, right? Which he built via Zapier. So it was, and correct me if I'm like, this is going to be different how you guys want to use it moving forward. But to my understanding, was Luma would, you know, kind of control all the registration and things like that. But then via Zap, that would update HubSpot, you know, and EventHappily objects we have in there, the custom objects. And then you'd able to track and do your reporting on the HubSpot side. Is that not the case or is there, what's half built that's not missing?

**Jason Gong:** I think that's the plan. And I guess I'm trying to understand, like, what all these pieces do, too. Like, from my understanding, like, EventHappily, like, what you're really providing is, like, the scaffolding to track all this stuff. And then the objects themselves, like, connect to each other. But as far as, like, I guess in our case, using Luma, like, hooking that up to populate these objects, like, that is not, like, that is more for us to figure out. Is that correct?

**Britton Wright:** Yeah. So, yeah. So really what we're doing is sitting on top of your HubSpot, right? We're basically creating a faster, more simple way to track, like, attendees and registrants and stuff like that. When you do use something like Luma, that's out of our scope. So we would basically only be able to just use whatever data you're able to send back via that Zapier. So if you want it to appear on your Luma or you want to pull something from Luma, that's kind of on your side of things to own and create and then anything past that. But we do have, and I talked about this initially, right, we, with Kyle, we do have our own registration flows and things like that. I think the main concern, right, was the look.

**Ben Francis:** I think Luma just looked a little better. Maybe there's some functionality there.

**Jason Gong:** You guys are using, like, the front-end registration experience from Luma, I believe. Front-end registration. Registration. Then like, I, I mean, the real act of Luma is like, you know, with that, like we kind of hold that audience and it's super low friction and we can send as many emails as we want, you know, it's kind of hard to get that through another platform.

**Ben Francis:** Yeah. I think like Luma has like some more like the community messaging kind of functionality as well.

**Jason Gong:** A newsletter built in.

**Ben Francis:** Yeah. Yeah. Which is completely fine there. We've got, we've got clients that are collecting registration through outside systems, outside of HubSpot and still writing it back into HubSpot with the, you know, rather than just like the traditional setup outside of happily is like we try to associate contacts, like a custom object or something like that, which is great, but that doesn't really store the instance of that person signing up for that thing to remind them and to track their status and the attendance.

**Ben Francis:** And some of the other stuff that, which is why in our kind of data model, we link the contact to the event with this object, the registrant itself, which is. It's the instance of Jason registering for the happy hour event, which stores the details about the event and the status and the details about Jason and where to get a hold of him.

**Ben Francis:** And that way, in our data model, we can track how many events did Jason sign up for this year? How many did he actually show up for? It gives us kind of this more granular reporting, so you guys can trigger all kinds of interesting things.

**Jason Gong:** Yeah, I mean, that'll make sense. So I think we looked at last week and how all the objects, like, work with each other when it's set up, right? Like, you know, like, I can see it in the deals, I can see it in the companies, I can see it in the person objects. Like, that all makes sense. I think the gap right now is, like, I don't really know what pieces we're missing to get Luma to then work with EventHapply. Because it seems like there's, like, quite a lot there. Like, because right now, I guess basically everything that's happening in Luma is not, like, reflected.

**Jason Gong:** So I guess we need zaps for almost everything from like when we create an event that doesn't show up as an event, you know, when an event finishes, it doesn't like get captured, updates to the events, some get captured, like new registrants, some get captured. So I guess like all of those maybe need zaps. I think it would be, honestly, it would be really helpful as like, I don't know if you have customers who have like set this up with a tool that you don't like maybe directly integrate with, like, what are all the zaps I even need, you know, would be extremely helpful.

**Britton Wright:** Well, we have Signify, right? We have a customer that has used Luma directly. They use Zapier, I believe, to set up the connection. But, oh, Ben, I interrupted you.

**Ben Francis:** I were about to say something.

**Ben Francis:** No, you're all good.

**Britton Wright:** Yeah. Yeah. So we do have customers that have used that before, right?

**Ben Francis:** Obviously, there's a little out of scope for it because it's not something we directly integrate with. But the main piece, right, before you dive into that, is just understanding what all Luma has that isn't in HubSpot.

**Britton Wright:** I know we created a few custom objects, at least initially, to make sure that anything would sync over. So I think I would take maybe an audit of what's on that Zapier side, I'm sorry, that Luma side, to see what hasn't already been created on the HubSpot side.

**Ben Francis:** It's like from like a process perspective, whether the event in HubSpot exists first or the event in Luma exists first, obviously we need to synchronize those two instances. And then obviously from the Luma side, when someone takes action and registers, is, you know, it'd be interesting to see, like, I don't have access to your team's portal right now to go like look for myself. If Luma is posting a signal to the contact record that we can latch on to, to then create a registration in HubSpot, where we're essentially kind of mirroring the event to registration setup in Luma in HubSpot as well.

**Ben Francis:** But essentially, like, especially if they're taking the registration action in Luma, we need to make sure HubSpot catches that signal so we can then tell HubSpot to create a registration for that person so we can link them together in HubSpot. So whether we create the event in HubSpot first and then push it to Luma or vice versa, from that side doesn't really exist, but that's like the, you know, prerequisite step to obviously have a thing for them to sign up for.

**Ben Francis:** Then on the Luma side, we're listening for when a registration happens to then, you know, register them in the HubSpot equivalent type of setup.

**Jason Gong:** Okay. So, so are those mostly, let's see. So, so it's, it's a zap for, um, syncing events to like events in Luma to the event object in HubSpot. And then it's another zap for, I mean, that might be two steps, one for creation, one for updating. And then there's another zap for, uh, registrations and maybe like, like updates to the status there.

**Ben Francis:** Does the, does Luma, um, I guess the, the interesting thing there is it would almost. It's to be a third in that. So we create the trigger for creating a registration that's contact-based, which then initiates the creation of the registrant record. The registrant record is what hosts the status of, you know, did Jason show up to the thing or not. So if you want to then use Luma to update that, we'll have to find the registrant record in HubSpot to then update it, which is fine because you can use the same email address for that person. So, like, it would be a Zap, so it would be, like, an event-based Zap to synchronize, a contact registration Zap to just mirror what happened in Luma in HubSpot, and then there would be a third one to update the registrant status where you'd, you know, find, based on matching email, and then updating status there.

**Jason Gong:** That one, yeah, makes sense to say, I'm just, maybe it helps just to look at it. Yeah, for because I think we're close to that, maybe. We were kind of hacking around last week. Just because we were looking for deal attribution, but I guess, like, where are the objects again? These things, right? Events make sense, registrants are, I guess it's interesting, registrants and a contact, or they're almost there, like, one-to-one, almost.

**Ben Francis:** The registrant is the instance of a contact registering for that event. So we carry over information about the contact, like, the name, company, email, and then we carry over data about the event that they signed up for, kind of all in one aggregated object.

**Jason Gong:** Got it. So for a given contact per event, will have one of these.

**Ben Francis:** Correct. Yeah. There's a one-to-one relationship between the contact and the registrant for that event. And, like, we carry over the same email address, the same name, so, like, using a find to then go update in a, you know, update the status. It should be relatively simple.

**Jason Gong:** Right, I see. I guess the flow would be just like if we starting from the very beginning, so it's like when we create an event in Luma, we need something that creates the happily event object. So that's step one. Then I guess we need something that's like syncing the two. I we changed the date a lot, so that would be something that would go into this field. And then the next step is to like when somebody registers for an event, or we invite them to an event, then we need to create the registrant object.

**Ben Francis:** We essentially need to take the, like, we can create the registrant by essentially putting the ID of the event from HubSpot into a contact property. So like that makes it relatively simple. Like, you know, for the, how we create registrations on our side is we're just, we have a couple webhook contact properties that we're just listening for the record ID of the event. And that then creates the registrant and we put all the stuff in a registered record for you.

**Jason Gong:** Then I guess I would need record ID. I guess I would need some ID here that comes with the, like, Luma trigger for an event that I can then look up this and then I need to look up this and then I, I add this to the contact and that's how I create, from the registration zap or whatever tool you use from there.

**Ben Francis:** It's, you know, when the, when the registration happens in Luma, you do a find and you get the, and you essentially can match based off of the event name. Cause it would be an exact match event name, find the event name. And one of the return fields is the record ID for the event. And then you do an update contact, and you carry over that record ID onto that contact trigger property.

**Jason Gong:** Okay, got it. That is pretty, well, I guess, okay, so that's registering, but then, like, I guess we have different statuses. It's like you can be registered, you can be approved, you can be waitlisted for that to then get carried to this. Does this have a similar kind of property?

**Britton Wright:** Yeah, it should have a property called status for the registry. That'll be, like, attended, canceled, registered. Now, approved, I don't believe yet, one of the options. Registered. Attended. Okay, so we'll want to figure out, like, I guess, a mapping to this, because these, I imagine, are used in your workflows, like, yeah, I would recommend it, right?

**Britton Wright:** I mean, we do have other fields that come. So if you look at the top right corner, says registered contact. So association labels between objects. There's also a pending registration between there. So there might be better ways to kind of register an event.

**Jason Gong:** Okay, cool. And then, okay, so let me need some way of updating this field. Okay, so the registering I get, because we just have to write the ID in. So let's say it goes from registered to approved or attended. And that's still from Luma. Like, I know there's some connection with Zoom if it's over a virtual call, I guess we can get into, but let's say that. How would then I update this record?

**Ben Francis:** Yeah, so based on the status of that person attending or whatever the status change in Luma is, you would do a find, happily registrant, and I would match based off of email, and then you could update and there's a status property.

**Jason Gong:** No, but then if they've come to multiple events. So you would, but that, in the find, it would be specifically for that event name. So you could find and match on, and event name is a property on the registrant as well. So you can scope to find that specific registrant for that specific event, rather than all registrants stack to be, hey, find this, find this registrant, if they have multiple, then filter based off of event name, matching, whatever the event name is. And then the action is update status.

**Jason Gong:** Got it. Okay, so we probably should stop changing event names after people have registered.

**Ben Francis:** It's an interesting use case that your team is, you know, using hapily kind of more as a back-end synchronization in HubSpot than really anything as a As it relates to the front-end experience for your event registration or content.

**Jason Gong:** So I guess, like, most of your customers would just happily be, like, the registration page. Is that how that works?

**Ben Francis:** Well, even if we're not collecting registrations through, like, a HubSpot landing page, we're using some sort of form, whether it's hosted by HubSpot or not, but we're then still collecting that registration action inside of HubSpot to then trigger the creation of a registration.

**Ben Francis:** And, you know, what most of our clients are doing is letting HubSpot be the driving force for the workflow automation, the event communications and reporting side of things. So, like, whether the registration action is hosted on a page or form that is owned by HubSpot or not, it's still, from that point on, everything stays typically within HubSpot to time the send the confirmation or remind your emails and do the check-in page. And everything kind of stays within HubSpot.

**Gloria Willis:** I see, and I have always been looking at EventHappily as a way to track results, like attribution and all that fun stuff on the back end. That's always been my main focus for why we were going to be using you all. So getting this part figured out with how we're going to get them everything connected, unless we're going to do, like, manual pushover of all of the registrations from Luma, which was going to have to be like our, you know, in between until this was all figured out. That's really what I was looking at event happily to be was like my dashboard to be able to see what kind of results are coming out of these events all in one place. Not necessarily tracking registrations because I can do that anywhere, but tracking results that are coming from registrations.

**Ben Francis:** The team's primary focus is happily being that system of record and magnifying glass for things that have already happened. And, you know, the event registration, communication side of things is done outside of happily. That's fine. You're not trying to push you into a use case that doesn't actually fit. I'm just pointing out, like, it's a bit uncommon for how our clients are typically structured. And so some of the connectors that we have to do to synchronize the data back into HubSpot is a little, just a little different.

**Ben Francis:** Ultimately, team can run the front end and even facilitate the event on Luma directly and happily can essentially have an event and we can bulk import registrations and attendees after the event happened if you don't want to have to synchronize stuff ahead of time. You guys can, you know, run your events with Luma and then as an action, we create the event record here, we import all of the, and you can do it in bulk, of course, for the registrations for who showed up, who just registered, to then allow the deal attribution workflow and some of the post-event analysis to still take place in HubSpot.

**Jason Gong:** Right. But I guess just from the stuff we're talking about, if we, you know, it's like a pain in the butt, but like if we get those kind of like triggers and syncs to work, then we don't have to do this like batch after the event.

**Ben Francis:** If we want to, if we want to use like, you know, middleware to then synchronize the, the event that happens from Luma into HubSpot and they register. And then synchronize the status, that's completely fine.

**Jason Gong:** Got it. Okay, I think it kind of all works out. What's the session?

**Ben Francis:** Is that a word? The session is a, sorry.

**Ben Francis:** Yeah, no worries.

**Britton Wright:** It's your call, sorry. Yeah, no worries, no worries. And what I was going to say, if y'all want to go a little longer, I'm more than happy to stay on. I think Ben has a hop, but I'm more than happy to stay on in, like, you know, just actually flesh this out, right? And give you guys a little bit more of an understanding fully of everything in here.

**Britton Wright:** But to quickly, like a conference, right? You're going to a conference and you might have multiple sessions or events, sub events, right, throughout that day you go to. And so sessions were really born out of that idea to create a way to track people, you know, with what they register for, should they want to register for, like, this session and skip another one or anything like that. So that's the primary use case. I don't think you guys are using it much. I didn't think you were going to run at it.

**Jason Gong:** Yeah, it doesn't look like we've tested it at all.

**Ben Francis:** It's a child object of the event itself. If you want to able to, if you need to track registration and attendance independent of the master event that they're going to, we allow that as an object to be able to track, hey, I want to go to session one, two, and five, and whether or not I attended each of those sessions independent of one another.

**Jason Gong:** Cool. Okay, I think I know what to attempt to build here. But you're right, like, it does feel like we're using it as, like, the backend. But it's like, if we didn't use it as a backend, we would still need to create this structure somehow, which seems daunting. Because I see all the, like, workflows you have, but I don't really know what they all do, but I assume that, like, it's the wiring that connects all these objects together.

**Britton Wright:** So if you go over to the far right, yeah, or you guys sorted by them, awesome. So they should all be organized. There's kind of a mixture there, right? So anything with, like, that halfway webhook, right, you don't have to touch. That's just a behind-the-scenes wiring that we created by default. Most of everything else, I would say, actually, everything else is needed. So this may make sense for us to have a separate call just, like, the three of us to dive into, you know, exactly what each workflow is doing, how you feel comfortable on it and, like, if it's needed or not.

**Jason Gong:** But I'm more than happy to do that, too. I think it's pretty clear. I mean, maybe what we could do is, like, try to build this and then, um, do you guys, like, work in Slack at all? Like, I'd love to be able to just ask some questions without having to set up another call. How do you all typically work with your customers?

**Ben Francis:** Slack is a challenging one in that we find that it becomes very quickly because runaway train with support and expectation of support being instant. We do have, I mean, ultimately, we have a variety of both direct contact through, like, you know, either personal email as well as, like, you know, chatting with our team through our knowledge base when you need it. So, I try to not get into customer Slack instances if at all possible just because the expectation of instantaneous support is, is just challenging.

**Jason Gong:** Okay, um, I guess just, like, breaking down what I'm thinking of doing, it's like, I guess in my head there's, like, four connectors. The things here, there's the, like, creating event, updating event, when a person registers, and when a person's status with an event updates, and all of those kind of, like, update event here, and then, I guess if we get those right, everything else should just automatically connect, is that fair?

**Ben Francis:** We built the deal attribution workflow to be essentially listening based off of that, that registrant status, and that, if you actually want to know that one, I'm not exactly sure if you want know, but yes, let's take a look at it. Yep. That's the standard one. Okay, cool.

**Ben Francis:** So, like, you know, from the, you know, system of record side, like, how do we know when we should attribute a deal? This is actually super helpful. So, let's go ahead and click on the action itself. So, give you a couple different levers to pull for, like, when we should go look for an associated deal with that, with that person who engaged with your brand at an event.

**Ben Francis:** Okay. How far back in time should we look for when that person attended your event to then see, does this person have any deals associated and should we go attribute the deal to the event itself? And we can even zoom out and say, does this person's company have any open deals that we should attribute to the event itself? And so, you know, with the labels here, you can target anyone who registers for an event. We can then associate their, like, if they have any deals to associate that to the event itself, or only people who show up, and then whether or not we can go look for the company itself and attribute all deals with that company, all in the context of, you know, whatever time parameter we put here.

**Ben Francis:** So, like, you're not the whole, like, and I recommend, too, like, this, we pre-install this workflow in this way, it's just an easy way to get the action in a workflow, different deal attribution workflow actions based on really what makes sense for your team around, hey, only deals that are in a specific pipeline or specific stage do we then want to go attribute to an event record or only deals owned by a specific marketer, whatever the conditions are there to say these are the deals that we care about, that we want to say we're influenced by the event that that person engaged with our brand.

**Ben Francis:** Yep, and Britton looks like we created a couple other deal attribution workflows, which is great. So yeah, hey, when a deal is won, we then, you know, claim that because that deal was associated with an event, we then set that trigger that, hey, there was an influenced event that closed, or an influenced deal that closed on the event itself.

**Jason Gong:** Yeah. Okay. Well, we'll take a pass out of it. Yep. Maybe look. Later in the week, we'll find some time, see if it worked, we're doing a bunch of invites for an event next week, and then we have an event Thursday, which I guess we'll have actual attended.

**Ben Francis:** Is your team managing the invitation for events in Luma as well?

**Jason Gong:** Yeah, we are.

**Ben Francis:** Yeah, we're looking at external platforms like Luma and some of the other kind of systems that exist out there to connect to. We've only had a couple people ask about Luma so far. It's gaining traction. I'm trying to figure out, like, how do we better play with Luma as kind of the front-end experience for managing your event directly. So it's not that it will never be supported.

**Ben Francis:** We're just trying to figure out where does it fit in our priority for our roadmap.

**Jason Gong:** Yeah, that makes sense. I'm just really surprised there's nothing here already. I mean, I guess it is somewhat. But like almost every dinner I go to, every happy hour, you know, or workshop is in Luma now. Like said, if it's coming from like a slightly newer company, I guess like if I join a Fathom workshop, I'm still filling out their form. I mean.

**Ben Francis:** Like between this and like Partiful. With certain verticals, we're seeing Luma get more popular. Um, yeah, it's definitely a, uh, California Valley kind of oriented distribution so far. So it also might be the, uh, it might be the ecosystem that we're registering for events for. Um, so we're, we're looking into how we, how we can play nicely with that with Luma to make the need for building four different zaps or connectors, uh, not as, uh, not as painful for your team.

**Jason Gong:** Right. And do you guys help with that or no?

**Ben Francis:** We're to build that ourselves. That is, it's a little bit beyond us so we can. Speak to how, like, the data that needs to land in HubSpot to then tie it all together. But, like, the facilitation of building the zaps or the connections directly, it's, I mean, we don't have access to your credentials to build them anyways, and you don't want us to. So, that's a, we can provide guidance, but we're not hands-on building it.

**Jason Gong:** Cool. I think that's all the questions I have.

**Jason Gong:** Yeah, cool. Appreciate it.

**Ben Francis:** Well, like, I think, you know, Britton, you're going to connect with the team later this week still?

**Britton Wright:** Yeah, I think that'd be good. At least, I'll touch base with you guys after you get finished, like, building things out, testing it out, and then we can have, like, a working session to iron out any other kinks on call, and then, you know, you guys can keep using Ben as your main point of contact.

**Ben Francis:** Great. Yeah, so, you know, Britton was down for about a week or so, and then I will, I'll take over. I mean, ultimately, if Britton has any questions or you need to pull me in, I'm here as your resource permanently at Happily.

**Britton Wright:** So, what can be done, what should be done?

**Ben Francis:** And how I would try to solve that same puzzle, honestly, Jason's your point earlier about how to best work together. We do a lot of looms back and forth to clients. I'll go try to build something in my demo portal and kind of show you, here's how I would click through that, or if I have access, I'll try to build it in yours. Just to try to help you solve those puzzles asynchronously as well.

**Jason Gong:** Cool. Thanks so much, team.

**Jason Gong:** Thank you.

**Jason Gong:** You all.

**Jason Gong:** All right.
