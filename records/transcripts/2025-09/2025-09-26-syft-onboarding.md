# Syft onboarding

<metadata>
date: 2025-09-26
time: 20:01 UTC
duration: 58 minutes
organizer: Jason Gong (GrowthX)
participants: Imran Patel (Syft), Kyle Doherty (GrowthX), Claudia Ring (GrowthX), Jason Gong (GrowthX)
fathom_recording_id: 90237831
fathom_url: https://fathom.video/calls/424234092
share_url: https://fathom.video/share/Ur5KhjtMSrxmxcxx--hniV__b6zVy46L
source: fathom
enriched_on: 2026-03-03 12:45 UTC
</metadata>

---

## Summary

Imran Patel, CEO of Syft, walked Jason Gong, Kyle Doherty, and Claudia Ring through the Syft platform — a data integration tool that combines LinkedIn, HubSpot, and website visitor data to enable outbound engagement and pipeline analytics. The team configured LinkedIn engagement tracking, HubSpot integration with automated syncs to the timeline, and a Slack motion to capture identified website visitors. Planned next steps: Jason will experiment with motions to re-engage webinar attendees and track LinkedIn post performance, with a follow-up sync scheduled for late Wednesday.

---

## Context

Syft is a B2B revenue intelligence platform founded by Imran Patel that integrates LinkedIn, HubSpot, and website data into a unified account view. GrowthX is exploring Syft as a solution to solve the de-anonymization problem with website visitors — they've previously tried Common Room (which Imran and Kyle both agreed is bloated and expensive) and are looking for a leaner, more focused tool. Kyle Doherty leads RevOps for GrowthX on a contract basis, while Jason Gong appears to be leading the product/marketing initiatives, including upcoming webinars and community engagement efforts. The meeting was a live product walkthrough where Imran demonstrated the core platform features and helped the team configure their initial setup.

---

## Relevance

**To GrowthX Delivery:**
- New tool for web visitor de-anonymization and account-based outreach, addressing a known limitation (previous attempts with Common Room and Vector failed).
- Syft automatically creates ICP-matched lists and can filter by custom signals; team needs to refine ICP definitions based on customer data.
- Extension-based LinkedIn data collection (runs locally, no credential sharing) is a safer alternative to solutions that require password authentication.

**To GrowthX Business Development:**
- Potential webinar attendee engagement motion: identify registrants from Luma event (4,500+ people), create LinkedIn connection requests, and follow up with recording link or in-app messaging.
- LinkedIn post engagement tracking: Jason wants to monitor engagement on co-authored posts (e.g., Guy's webinar promotion) and send targeted outreach to commenters/likers.
- Account expansion signal: Syft can track all inbound website activity at the account level, giving early signals for bottom-up adoption before outbound outreach.

**To CheckThat / Product Development:**
- PostHog integration opens door to combining product signup events with outbound LinkedIn engagement — e.g., auto-connect with new community signups (Circle) or product beta users.
- Future SDK integration could allow GrowthX's own product (in development) to feed engagement signals into Syft, automating motion triggers based on product behavior.

---

## Overview

- Syft integrates with LinkedIn, HubSpot, and website data to provide enriched contact/company insights and engagement analytics
- Key features include LinkedIn activity tracking, automated workflows ("motions"), and detailed pipeline reporting
- GrowthX team plans to experiment with Syft for webinar attendee engagement and LinkedIn post analytics

---

## Key Topics

### Syft Platform Overview

  - Connects data from HubSpot, LinkedIn, website visitors
  - Chrome extension pulls LinkedIn data locally for security
  - UI shows enriched contact/company data with engagement context
  - Can create custom lists and automated workflows ("motions")
  - Pipeline reports provide detailed engagement analytics

### LinkedIn Integration Capabilities

  - Tracks post engagement (likes, comments) for specified profiles
  - Can automate connection requests and track DM activity
  - Adds tracking parameters to shared GrowthX links
  - Ad campaign data can be pulled in for analysis
  - Weekly connection request limit of \~150-200 enforced by LinkedIn

### HubSpot Integration

  - Syncs Syft data to HubSpot timeline
  - Can create new contacts/companies in HubSpot
  - Existing HubSpot lists visible in Syft interface

### Potential Use Cases for GrowthX

  - Engage webinar attendees via LinkedIn/email follow-ups
  - Analyze LinkedIn post performance and audience
  - Track ad campaign engagement
  - Enrich product analytics data (e.g. PostHog integration)

### Data Privacy and Security

  - Extension runs locally, Syft doesn't store LinkedIn credentials
  - No message content synced, only activity metadata
  - User has control over what profiles/data are tracked

---

## Action Items

**Jason Gong (GrowthX)**
- Play around with Syft tool, focusing on motions related to upcoming webinar engagement and LinkedIn post tracking
- Set up first motion for webinar attendee outreach via LinkedIn or email sequencer

**Imran Patel (Syft)**
- Send calendar invite for follow-up meeting for late Wednesday 4pm

**Kyle Doherty (GrowthX)**
- Review Syft integration and HubSpot field mapping, prepare questions for follow-up

---

## Transcript
**Imran Patel:** Yeah, sure.

**Kyle Doherty:** I do RevOps for GrowthX on a contract basis.

**Kyle Doherty:** And yeah, we've been trying to get de-anonymization for web visitors, first with CommaRoom, but CommaRoom just, yeah, I don't love CommaRoom.

**Kyle Doherty:** They're trying to do way too much.

**Kyle Doherty:** So we just got, I'm blanking on the name now, but yeah, so excited to hear about your tool because I've seen you on LinkedIn and think it's potentially a great tool, so.

**Kyle Doherty:** It's great.

**Kyle Doherty:** Well, thank you.

**Kyle Doherty:** Vector.

**Kyle Doherty:** Vector, yeah.

**Kyle Doherty:** But yeah, I'm tool agnostic.

**Kyle Doherty:** I care about what's going to get the job done, not the tool.

**Imran Patel:** It's always all about the data quality.

**Imran Patel:** Yeah, exactly.

**Kyle Doherty:** Well, I'm curious now, what do you not like about CommaRoom?

**Imran Patel:** I think they're trying to do way too much.

**Kyle Doherty:** And then the...

**Kyle Doherty:** And the reason they're charging so much is because they're angled towards larger sales teams where you can use Common Room as sort of this tool that's assisting their sales reps.

**Kyle Doherty:** And like GrowthX and most companies I work with, they don't need that.

**Kyle Doherty:** They have a very lean sales team.

**Kyle Doherty:** And the other thing is I think Common Room is just duplicating features of other tools that should be your source of truth.

**Kyle Doherty:** So you're just like, you have all the, then you're paying $800 a month for a tool that does the same thing as like HubSpot or like pick a sequencer or whatever.

**Kyle Doherty:** Yeah, yeah, yeah, yeah.

**Imran Patel:** Yeah.

**Imran Patel:** Well, they have a lot of money, so they kind of can, you know, keep on expanding their surface area.

**Imran Patel:** Yeah.

**Kyle Doherty:** They remind me of a segment back in like the mid-thesens when it was like promising to solve all your problems.

**Kyle Doherty:** But then when you actually got under the herd, it was like just a very simple tool that wasn't delivered.

**Kyle Doherty:** Yeah, yeah.

**Kyle Doherty:** Segment, I like Segment.

**Imran Patel:** I think they were doing a good job on the front end on the data collection side of it, but then I think they kind of instead overstretched themselves and went into like the braze.

**Kyle Doherty:** Yeah, I mean, they didn't, when I say they didn't deliver on their promise, I mean with personas, when they chugged in.

**Kyle Doherty:** Yeah, yeah.

**Kyle Doherty:** The identity part, yeah.

**Kyle Doherty:** Yeah, that was trash.

**Kyle Doherty:** Cool.

**Kyle Doherty:** It was why the developer that created that built this company high touch, so.

**Kyle Doherty:** Oh, okay.

**Kyle Doherty:** I see.

**Kyle Doherty:** Yeah, those people are nice.

**Imran Patel:** I met them.

**Imran Patel:** We were just doing introductions.

**Imran Patel:** I'm the, my name is Imran.

**Imran Patel:** I'm the co-founder and CEO of Syft.

**Imran Patel:** And me and Kyle were just talking about segment, common room, gardeners, like, you know, just like tools in general, I suppose.

**Imran Patel:** Cool.

**Imran Patel:** And you work in marketing, I think.

**Imran Patel:** Right.

**Imran Patel:** Okay.

**Imran Patel:** Awesome.

**Imran Patel:** Cool.

**Imran Patel:** Well, let's just get started.

**Imran Patel:** And so I saw that you set up the thing.

**Imran Patel:** mean, one of you can kind of just present the screen and it can kind of walk you through what the tool does that usually works out the best.

**Imran Patel:** So whoever wants to do the honors will kind of either Kyle or Claudia or Jason.

**Imran Patel:** Do I have any, Kyle?

**Jason Gong:** Yeah, everybody.

**Jason Gong:** It's like Oprah.

**Jason Gong:** Everybody gets seats.

**Jason Gong:** Oh, just clicked the sign up thing.

**Jason Gong:** Okay, sorry.

**Jason Gong:** didn't get a chance to do that.

**Jason Gong:** Do I just sign up for free?

**Jason Gong:** that?

**Jason Gong:** Yeah, just log in.

**Jason Gong:** If log in with your growthx thing, you should be in.

**Imran Patel:** Okay, it'll just pull me into the...

**Jason Gong:** Yeah, Imran, the one thing I wanted to ask you was I...

**Claudia Ring:** Yeah, sorry.

**Claudia Ring:** Do you want to present?

**Claudia Ring:** Sorry, Isaac.

**Imran Patel:** Sorry, go ahead.

**Imran Patel:** Yeah.

**Imran Patel:** I can.

**Imran Patel:** Yeah.

**Claudia Ring:** I threw in Marcel's LinkedIn on mine because I wasn't sure if it was supposed to be like for me, for everyone, for whatever, but I can obviously swap that out.

**Claudia Ring:** So, yeah.

**Claudia Ring:** Yeah, yeah.

**Imran Patel:** I saw that Marcel and Growthx company page also...

**Imran Patel:** That was added, correct?

**Imran Patel:** Yes.

**Imran Patel:** Yeah.

**Imran Patel:** So the way syftdata works is that what you track is different than who installs the extension, if that makes sense.

**Imran Patel:** So the extension is what is used for pulling the data.

**Imran Patel:** We'll get to it.

**Imran Patel:** So anyway, this is the main screen.

**Imran Patel:** I think HubSpot is connected.

**Imran Patel:** You can kind of see people kind of, and then if you click on show context on the top right, there is a toggle there, and that will show you all the accounts for which we have.

**Imran Patel:** we scroll down here, like, you know, somebody from FAL was there.

**Imran Patel:** Gorkum actually is coincidentally, I know Gorkum or somewhere connected.

**Imran Patel:** And yeah, so those will show you all the companies for which we do have people that we are kind of picking up.

**Imran Patel:** If you scroll up and toggle that thing off, then we kind of show you everyone.

**Imran Patel:** And so in this case, like, Felices, somebody came in.

**Imran Patel:** They were, like...

**Imran Patel:** We weren't able to figure out who that was.

**Imran Patel:** So if you click on that one contact under Felicis, it will show you exactly what was and go to visitors on the top right.

**Imran Patel:** That is a pill right next to that one.

**Imran Patel:** Then if you click on one session, it will kind of show you what happened there.

**Imran Patel:** Like, I think they just came to the website and bounced off.

**Imran Patel:** Oh, so we installed the pixel already?

**Jason Gong:** Yeah.

**Jason Gong:** She was quick.

**Imran Patel:** But yeah, so that's kind of what, so if you back out of here, you will kind of see, like, now, obviously, Felicis is not your target ICP.

**Imran Patel:** And so, like, Dialpad is, right?

**Imran Patel:** And so you can kind of see Dialpad is tagged with that B2B SaaS thing on it at the top.

**Imran Patel:** Well, this one right here.

**Imran Patel:** Okay.

**Claudia Ring:** Yeah.

**Imran Patel:** And so that is, so, and you can see all of the companies that match that ICP on the left-hand side under and they're, you

**Imran Patel:** Suggested lists, so we automatically created the list for you on the left hand side if you scroll like there, and so these are all the ones that match your ICP essentially, but then you can also look at since you connected HubSpot there are some other lists on the left as well like LostOps, Customers, OpenOps, so Zoopla is circling back, we don't have anybody with OpenOps, and then Customers, like DeepGram, guess.

**Imran Patel:** Is DeepGram a customer?

**Imran Patel:** I'm assuming DeepGram is a customer.

**Imran Patel:** Mm-hmm, yep.

**Imran Patel:** Yeah, I think DeepGram should, we sometimes, what we should do is we should probably add media, sometimes the classification is kind of off, but if you click on that plus media at the top, yeah, let's just add them to the ICP, so click on review there, and then just say add to ICP on the top.

**Claudia Ring:** Huh, and you can, can you tell why it wasn't falling?

**Imran Patel:** It's because I think it's just whatever data provider that we had, like, you know, classification, didn't have them under software.

**Imran Patel:** Sometimes they misclassify them.

**Imran Patel:** So that's just like, that's why we're going to just add media into it.

**Imran Patel:** So they'll get, yeah.

**Kyle Doherty:** Cool.

**Kyle Doherty:** Yeah.

**Kyle Doherty:** Industries is like notoriously bad data.

**Imran Patel:** It's always, you know, we're trying to actually fix it a little bit on our side by not even relying on industry classification anymore.

**Imran Patel:** It's always hit or miss, as Kyle said.

**Imran Patel:** Well, mostly three-levels.

**Imran Patel:** Sometimes it kind of gives you, it throws you off.

**Imran Patel:** Okay.

**Imran Patel:** So let's kind of do, finish the, so this is, this is like the general, like, sift kind of interface.

**Imran Patel:** If you go to all accounts, you can filter and create lists in your own kind of way.

**Imran Patel:** So you can kind of do, you know, based on ICP persona, signals, which we set up for you.

**Imran Patel:** So you can, and you can choose the signals that.

**Imran Patel:** Safal was looking at your pricing page.

**Imran Patel:** I came and looked at your pricing page like earlier in the morning, so I'm on there as well.

**Imran Patel:** But you can then create this list.

**Imran Patel:** And so like you can, there's a button that create list, I will create a list on the sidebar.

**Imran Patel:** LLM referrals also kind of a thing.

**Imran Patel:** So let's actually go and sort of set up a, there are a few analytics things that I'll show you in a bit, but click on settings now.

**Imran Patel:** Let's take care of the LinkedIn stuff because that's what Jason really wants.

**Imran Patel:** So if go to integrations, and I think it would be good if you all do it.

**Imran Patel:** And so if you just take this, let me just give you the URL.

**Imran Patel:** So if you click on install there, you see there is a LinkedIn engagement organic, click on that.

**Imran Patel:** There'll be a Chrome extension that is, it will ask you to install from the app store.

**Imran Patel:** So just do that.

**Imran Patel:** And then Jason and.

**Imran Patel:** And Kyle, if you want to, Jason, you should do it, Kyle, probably not.

**Imran Patel:** Yep, I think I'd just do it.

**Imran Patel:** Customers and doesn't want to tie his LinkedIn to growthx.

**Jason Gong:** Claudia, you work at growthx full-time, right?

**Imran Patel:** No.

**Imran Patel:** Oh, you're part-time as well, okay.

**Imran Patel:** Yep.

**Jason Gong:** Okay, I installed mine, I think.

**Jason Gong:** Okay, awesome.

**Imran Patel:** So, yeah, if you want to present your screen, Claudia, then we can go ahead and I can show you how to, right, and so, click on reload here, refresh this page.

**Imran Patel:** Oh, click on settings on the left, under, sorry, under LinkedIn engagement, organic, that card, yeah.

**Imran Patel:** So, we have Jason, we have Claudia, we have Marcel and growthx.

**Imran Patel:** Anybody else that we should track, Jason?

**Jason Gong:** I think we can probably keep that for now.

**Jason Gong:** mean, I'll look.

**Imran Patel:** The ones that are already there, if you click on configure sync, it will show you what it's actually writing and what it's kind of pulling, if you scroll down, 90% of the stuff is SIFT's properties, they're all prefixed with SIFT, so you will kind of, you know, know exactly, like, you know, it's not going to do anything, stomping or anything on something that exists, so that's, you can configure what gets written here, the field mapping, so to speak, Kyle.

**Imran Patel:** So, that is there, and so if you want to make it completely read-only, then you can just turn off that toggle, we strongly recommend to keep it, because it's mostly, it's fairly useful, and then.

**Claudia Ring:** Do to keep it on for now, Kyle, or do you want me to turn it off for now?

**Kyle Doherty:** I don't see a problem with turning, or keeping it on, Imran, when we did the connection, does it automatically create those SIFT properties?

**Kyle Doherty:** Yes.

**Kyle Doherty:** Okay, cool, yeah, then, I don't see a problem with it, because those are net new, like, shouldn't cause any issues.

**Imran Patel:** Yeah, and then you can see all the properties there as well, but Kyle, it's in the documentation.

**Imran Patel:** I'll just put a link on the sidebar.

**Imran Patel:** There's the documentation that you can always go check.

**Imran Patel:** And then Slack, I think we should connect as well.

**Imran Patel:** So whoever has the privileges, we should probably, I don't know if Claudia, you have it.

**Jason Gong:** Yeah, I can probably, I think actually, it'll probably just send a request to our IT guy, but let me try.

**Jason Gong:** Do have an IT guy?

**Jason Gong:** I he's also part-time.

**Jason Gong:** We have a lot of part-time people.

**Jason Gong:** Yeah, I just get the blocker of not being authorized, so.

**Claudia Ring:** This app is not approved by Slack, blah, blah, blah.

**Jason Gong:** And then what does this Slack thing do?

**Jason Gong:** Is that just for notifications to a channel or?

**Jason Gong:** Yes, Okay.

**Kyle Doherty:** I'm loud.

**Jason Gong:** Am I allowed to say what channels there's the access to?

**Imran Patel:** We only read content from the channels where we are inside that channel.

**Imran Patel:** Got it.

**Jason Gong:** Okay, I think I connected it.

**Jason Gong:** Yeah, Claudia, do you want to refresh the page?

**Claudia Ring:** Perfect.

**Imran Patel:** Okay, so now we are going to do some automation.

**Imran Patel:** So if you click on motions on the left, that's how we kind of do the, you know, do a bunch of interesting stuff.

**Imran Patel:** This is the orchestration layer.

**Imran Patel:** So there is already one which says post to HubSpot timeline.

**Imran Patel:** So that motion already was set, you know, was set up.

**Imran Patel:** So this is going to run an update and going to post, like, all the LinkedIn and other activities on to HubSpot as they happen, which I think one of the things that Jason kind of wanted.

**Imran Patel:** Jason, like, I think you also wanted the DMs to.

**Imran Patel:** Synchronize into HubSpot, in which case anybody who's DMs need to synchronize into HubSpot, we need to tell them to install a safe extension.

**Jason Gong:** And I guess this sync, like, is this like all your DMs?

**Jason Gong:** Can you select a subset somehow?

**Imran Patel:** We never copy the messages into HubSpot out of privacy reasons.

**Imran Patel:** So it will always say, like, Claudia messaged someone on the account, right?

**Jason Gong:** And so that way, like, let's say I, like, message, like, random people have nothing to do with work.

**Jason Gong:** Like, if those people aren't in HubSpot, is that just, like, nothing happens?

**Jason Gong:** Yeah, that doesn't matter.

**Jason Gong:** Yeah, yeah.

**Jason Gong:** But if they're in HubSpot, it will go there.

**Imran Patel:** But your actual message doesn't show up on the timeline.

**Imran Patel:** So at least it gives you a certain idea that, okay, well, this account was worked by someone, but, like, they can kind of fill you in.

**Imran Patel:** Yeah, it's always a very tricky privacy situation with, like, you know.

**Imran Patel:** LinkedIn generally, but this motion, so motions in SIFT always have three components, there's a trigger, which is like when should it fire, like typically on some activity, and then there is a filter, which is you scroll down, it will kind of, yeah, on the left hand side, if you scroll down, I'll just click on the edit again, sorry, I meant in the screen that you had to open, so just click on the post to HubSpot timeline title, Oh, sorry, my bad, no worries, and then click on edit on the top right, yeah, so here on the left hand side, so filters is very qualified, so filter is like how you filter out people that you, so you might only want to update for ICP companies, for example, so you can click on add new filter, and you can just kind of, there are a bunch of filters, you can do account filters, you know, so I wouldn't do it right now, but like, you know, just let everything, because it's just doing it for everything that exists in your HubSpot, and then the final thing is action, which is

**Imran Patel:** A nicer name, probably.

**Claudia Ring:** We can update this.

**Claudia Ring:** We'll just do it in a test channel for now and see and update it.

**Claudia Ring:** Okay.

**Imran Patel:** And before you do that, just click on apply motion to these past visitors and companies.

**Imran Patel:** At the bottom, you see there is a toggle right there.

**Imran Patel:** Yeah.

**Imran Patel:** And then just say create motion.

**Imran Patel:** So this should now start sending that data into that channel.

**Imran Patel:** Make sure that people who need to be, you know, they should be in that channel.

**Imran Patel:** And then the other thing that we can do is we can also set up, I guess it's up to Jason now.

**Imran Patel:** Like we have three or four plays that we can turn on.

**Imran Patel:** So right now the HubSpot update is going to go through the Slack you're going to get.

**Imran Patel:** Do you want to create contacts and companies as well that come in?

**Jason Gong:** Is there a place to just look at kind of the, I guess, what would you call it?

**Jason Gong:** Like the triggers or like the kind of information you're actually ingesting before we start?

**Jason Gong:** Pushing it out to HubSpot and Slack.

**Imran Patel:** You mean like what would be pushed?

**Imran Patel:** Like a dry run?

**Jason Gong:** Yeah, just like, well, I guess the parts that were interesting to me is like, you now know like everybody that's like engaging with our content or like, you know, like we're writing messages to.

**Jason Gong:** Is there anywhere that we could just browse that to see what that actually even looks like?

**Imran Patel:** Yeah, so what you can do is you can always come to the app and see what is going to happen.

**Imran Patel:** But we can also do a dry run channel, Slack channel as well.

**Kyle Doherty:** Or maybe I don't.

**Jason Gong:** You want to see what would be, what would be, what is the activity in general, right?

**Jason Gong:** Yeah, this is like, I guess, like, for example, one motion that maybe I want to do is like, like, both.

**Jason Gong:** Me and, like, this guy from Webflow, we did a post about a webinar we're doing, and just want to send everybody that added, or that commented, or liked that post, like, a link to the webinar.

**Jason Gong:** Like, would I be able to do that here?

**Jason Gong:** Yeah, and how would you send the link via DM?

**Jason Gong:** It's a good question.

**Jason Gong:** We could use, I guess we have PayReach, we have, could be an email, I guess, if we enrich that.

**Jason Gong:** So that, that would be HubSpot, or I think we use, once again, Instantly, or it could be Phantom Buster.

**Jason Gong:** I guess it could be any of those, but I guess, like, could I look at who those people even are before, like, hooking up that last mile of sending the message?

**Jason Gong:** So, yeah, yeah, yeah.

**Imran Patel:** So what you can do is, if you tap, Claudia, on LinkedIn Activity on the left-hand side, then you can now see, like, okay, so now we have started thinking you.

**Imran Patel:** Thank

**Imran Patel:** So now this is Marcel's birthday post, and if you click, so it's still processing, okay, so it's like if you click on that thing, file it, it will actually show you, it's probably opened in a new tab, yeah, so it will show you everybody who's kind of engaging with that post, right, from different companies and so on.

**Imran Patel:** So we could run a motion where the LinkedIn post is this, or whoever engages with this LinkedIn post is in your ICP and persona, and then just send them into a particular list in HubSpot, probably, so we could, we could do that as well.

**Imran Patel:** Okay, cool.

**Jason Gong:** That's really...

**Jason Gong:** Is that what you wanted?

**Imran Patel:** Yeah, yeah, but I guess right now it hasn't, it looks like, for some reason, yeah, yeah, I guess, yeah, was the post from you, or, so I can show you one other thing, like,

**Imran Patel:** If you present your screen, I'll show you one other trick.

**Imran Patel:** Yeah, sure.

**Imran Patel:** Because we are not tracking your profile yet, right?

**Imran Patel:** So, but I guess the post was from, was it from Guy or someone?

**Imran Patel:** Yeah, Guy did one, and then I just did one this morning.

**Jason Gong:** Yeah, so if go to LinkedIn and open Guy's post, not here, on LinkedIn, LinkedIn, yeah.

**Kyle Doherty:** And this one.

**Imran Patel:** Right, so that, yeah, just click on that button, the gray button, yeah.

**Imran Patel:** So this will start tracking his.

**Imran Patel:** Cool.

**Jason Gong:** And then you can go so that integration screen you showed.

**Jason Gong:** So there are two things, right?

**Imran Patel:** One is that there are profiles that we auto-track.

**Imran Patel:** So everything that comes out of growth hacks and marshals will just be pulled in, sift automatically, right?

**Imran Patel:** But then if there are these one-off things that you want to do that a lot of our customers will do it.

**Imran Patel:** Like, you know, like I come across Kyle's post and like, you know, he's like relevant.

**Jason Gong:** Does adding it here mean that it's tracked or do I still have to add myself?

**Jason Gong:** No, you have to add that stuff.

**Imran Patel:** The extension is just for pulling the data.

**Imran Patel:** has nothing to do with it.

**Imran Patel:** It's pulling your personal data, so to speak.

**Imran Patel:** Right?

**Imran Patel:** So if you want to pull DMs and other stuff, we need the extension.

**Imran Patel:** If you want to send connection requests on your behalf, we need that stuff.

**Imran Patel:** So.

**Imran Patel:** Okay, that's helpful.

**Jason Gong:** Yeah, it's there.

**Jason Gong:** You added.

**Jason Gong:** So this is like, I can add, it doesn't matter if they work for growthx or not.

**Jason Gong:** Yeah, yeah, Okay, cool.

**Jason Gong:** Some of our customers do it for competitor profiles.

**Jason Gong:** Yeah, We're trying to their ops, guys, for sure.

**Imran Patel:** Yeah, so and then if you click on view track post, it will start, you know, so now we can see like guys post is also in the queue now.

**Imran Patel:** So it will start, you know, so you should just bookmark that LinkedIn activity tab and then, or just like, you you can come to it.

**Imran Patel:** And then if you want to run the.

**Imran Patel:** Yeah.

**Imran Patel:** Yeah, yeah.

**Imran Patel:** Yeah.

**Imran Patel:** Yeah.

**Imran Patel:** Motion on that stuff, you can just go and say, like, I want to, you know, create a motion on the top, or, yeah, you can, there's a bunch of templates, so you can just tell the AI what you want.

**Jason Gong:** It's a trigger.

**Imran Patel:** New contact, yeah, and then go to filters, and identified by LinkedIn, actually, that's what you want, right, you don't want the website, people.

**Imran Patel:** So, and then add new filter, and then go to LinkedIn at the very bottom, yeah, and then organic engagement, and then you can choose engage post, and then you choose the one that you want.

**Jason Gong:** It's the bottom one, if you want the birthday post.

**Claudia Ring:** Yeah.

**Jason Gong:** He wants the guy one, I think.

**Jason Gong:** Isn't that the Webflow one, probably?

**Imran Patel:** Oh, this one's my post, okay, it looks like it pulled that in, too.

**Jason Gong:** Right, and then

**Imran Patel:** And can kind of send it to.

**Jason Gong:** Right, you can apply it, I think, Jason, you need to apply it.

**Jason Gong:** Yeah, I don't actually want to turn on.

**Jason Gong:** And you can go to LinkedIn.

**Imran Patel:** So you can close the loop here and by just saying send a connection request.

**Imran Patel:** We have a DM thing coming actually pretty soon.

**Imran Patel:** So you'll be able to send a DM.

**Imran Patel:** But if you click on connection request, then you can send out the connection request to them as well.

**Imran Patel:** And you can add a personalized message.

**Claudia Ring:** But then you said, like, we can also go back and just look at the list of the people from this particular motion that showed up.

**Claudia Ring:** Yeah, it looked like that was just here.

**Jason Gong:** Yeah, that was in that tab, yeah.

**Jason Gong:** Yeah, okay.

**Jason Gong:** Cool.

**Jason Gong:** Yeah, I I think setting this up, I can totally just do it.

**Jason Gong:** Yeah, so you could just probably, the way to do it would probably, the way I would do it is I would just put it into a smart lead sequence.

**Imran Patel:** Mm-hmm.

**Imran Patel:** I think...

**Imran Patel:** If you turn on SmartLead AI or whatever, or I would put it in clay if you want to do some more fancy stuff, but SmartLead, I think there's an add to sequence action there.

**Imran Patel:** Or you could put it into a spreadsheet if all of the fails, like, you know, that's kind of the other thing that you can always do.

**Imran Patel:** So you can always add it to a spreadsheet as well.

**Imran Patel:** That makes sense.

**Jason Gong:** And then are these people enriched already when they...

**Imran Patel:** Yeah, so we'll kind of, we'll enrich them, we'll pull the email, and then we'll send the entire record.

**Imran Patel:** Got it.

**Jason Gong:** Let me just do this just so you can visually see it.

**Jason Gong:** What do I click on?

**Jason Gong:** I click list?

**Jason Gong:** Yeah, that one, yeah.

**Jason Gong:** I don't know why Google is so...

**Imran Patel:** Oh, I should tell my CTO, like, why is this?

**Imran Patel:** Thank you.

**Jason Gong:** And then you can choose.

**Imran Patel:** It's okay.

**Imran Patel:** It's okay if you get our name wrong.

**Imran Patel:** That's fine.

**Jason Gong:** There's this app called Sifton that I used to use for social distancing.

**Jason Gong:** you used that?

**Jason Gong:** No, I actually didn't know there was a Sifton.

**Imran Patel:** I know other Sif that exist.

**Imran Patel:** Let's see.

**Jason Gong:** Okay.

**Imran Patel:** Yeah, and then what you can do is you can...

**Imran Patel:** Yeah, there you go.

**Jason Gong:** Yeah, it's going to send a whole bunch of stuff.

**Imran Patel:** Um, the scroll, um, yeah, in the motion, uh, you can, yeah, there is a LinkedIn, uh, if you search for LinkedIn, there is...

**Imran Patel:** Like a LinkedIn, there's a couple of columns of LinkedIn in there, LinkedIn like, post URL, and then it should also have the profile, the email, you can see the contact email address should be there as well, and then the LinkedIn profile should always, this is the post URL, but the LinkedIn, the URL should be under contact.

**Jason Gong:** Oh, I see it, it's over here.

**Jason Gong:** Yeah, this is the test one, right?

**Imran Patel:** You're just like, this is just the test thing that we sent.

**Jason Gong:** okay, so there's a contact, okay, this one, I guess.

**Jason Gong:** Yeah.

**Jason Gong:** LinkedIn contact.

**Jason Gong:** Okay, cool.

**Imran Patel:** And then if you go back to the safe thing, you can click on apply motion to pass visitors and contacts, and then create motion, and that should just, oh yeah, it needs a name.

**Imran Patel:** Okay.

**Imran Patel:** Cool.

**Imran Patel:** So now we have Slack, have HubSpot.

**Imran Patel:** One other thing I always recommend is connect with identified visitors.

**Imran Patel:** That one is very useful.

**Imran Patel:** I use it myself, the second template at the top, which is anytime somebody signs up on your website, just connect back with them on LinkedIn.

**Imran Patel:** Just keep everything as it is.

**Imran Patel:** And then you can just choose yourself, Jason.

**Imran Patel:** And then you can add a note as well saying, like, thanks for signing up or whatever.

**Imran Patel:** And it generally works very well.

**Jason Gong:** Yeah.

**Jason Gong:** Okay.

**Jason Gong:** I just want to think about stuff before I actually turn on.

**Imran Patel:** You know where to go.

**Imran Patel:** Makes sense.

**Imran Patel:** What do you guys do with, like, ads?

**Jason Gong:** Because, like, I mean, we really don't do much ads, but we just started, like, for example, we're promoting guys' posts right now.

**Jason Gong:** Is there anything we can do?

**Jason Gong:** So ads is actually, so what were you, like, you were doing a thought leadership ad on this stuff?

**Jason Gong:** So at Florida sometimes.

**Jason Gong:** Yeah.

**Jason Gong:** I mean, aren't

**Jason Gong:** Yeah, I'm really bad with ads, but like, here's what we're doing, we have...

**Jason Gong:** doesn't make it easy, man.

**Imran Patel:** It's like, I don't know, they haven't updated this thing in like, like, don't update it very frequently.

**Jason Gong:** Yeah, we're just, this is almost like a test, because I have no idea how to use this, so I'm just like, oh yeah, okay, this, but I'm promoting his post as a brand awareness.

**Jason Gong:** I don't know if this was the right goal to set.

**Jason Gong:** I haven't done it before, I know if this is the right one.

**Jason Gong:** Is there, yeah, is there anything you could do with this and stuff?

**Imran Patel:** So what you can do is you can, if you go back to SIFT, go to integrations, and then go to LinkedIn ads, connect.

**Imran Patel:** Yeah.

**Imran Patel:** Use the one that, yeah, use the one that has access to your campaign manager stuff.

**Jason Gong:** Use the one that, yeah, sure.

**Imran Patel:** And then here you choose the ones that you, you don't want the ones.

**Jason Gong:** I do a horrible job of like naming, so there's duplicates, let's see.

**Jason Gong:** I would just put both of them.

**Jason Gong:** Okay.

**Jason Gong:** One is on hold, this is hard to figure out, which one would be okay.

**Jason Gong:** Like, ah, , okay, I want to just do, okay, there's only one, okay, that's good.

**Jason Gong:** Is that right?

**Jason Gong:** Yep.

**Imran Patel:** Perfect.

**Imran Patel:** And so what this will do is, this will start pulling in LinkedIn accounts who engage with your ad.

**Imran Patel:** And so that way you can then now use those, and you can funnel those accounts into HubSpot as well.

**Imran Patel:** So, so that's kind of the other thing that.

**Imran Patel:** This is great.

**Jason Gong:** Wait, is there any custom connector you could do at all?

**Jason Gong:** No.

**Jason Gong:** No.

**Jason Gong:** I think, honestly, LinkedIn, our website, probably captured most of it.

**Jason Gong:** The only one left that we've had a little bit of trouble integrating into all of our emailing and stuff is just stuff in Luma.

**Jason Gong:** For example, we have like 4,500 people.

**Jason Gong:** I want to send these people some stuff.

**Imran Patel:** Is Luma now connected to HubSpot right now, Jason?

**Jason Gong:** It is through a Zapier connection.

**Kyle Doherty:** Say that again.

**Kyle Doherty:** It is through a Zapier connection.

**Kyle Doherty:** Oh, because they don't have their own integrations.

**Jason Gong:** Okay, sorry, go ahead.

**Jason Gong:** Oh, no, I guess I was just going to say, I guess if we are connected to Zapier, they'll get pulled into HubSpot, into a list, and then I guess we can pull that here.

**Jason Gong:** Yeah.

**Jason Gong:** I guess that would be the motion.

**Jason Gong:** What is the motion that you were thinking, Jason?

**Jason Gong:** Yeah, I guess it depends.

**Jason Gong:** I mean, this one, it'll be like...

**Jason Gong:** I think I promised people that joined the webinar, would send them a link to the recording of the last one.

**Jason Gong:** So it would be cool if I could add them on LinkedIn.

**Kyle Doherty:** Yeah, we have them for each one of those.

**Kyle Doherty:** So for the registrants in HubSpot, we have a list.

**Kyle Doherty:** And then you could pull that in to here.

**Kyle Doherty:** think, Imran, are you able to, when we pull in those lists we have on the side, like customers, you able to sync individual lists from HubSpot?

**Imran Patel:** Um, we don't currently have, it's coming where you can sync or take on HubSpot list, but I can show you there is one way, if you want to just blast, like if you want to connect with them, what you can do is you can go to motions and there is, uh, click on, um, see all here on the right hand side, there's a template called enrichment, just search for enrichment on the top, uh, uh, in the search templates bar.

**Imran Patel:** There is a, yeah, and what you can do is you can just.

**Imran Patel:** So if Kyle gives you that list of people from HubSpot, and then just click on that use template, and then just drop that list here, and at the bottom, you can just put LinkedIn as a destination URL, and then you will connect them through LinkedIn.

**Imran Patel:** And do you want to connect with those people?

**Jason Gong:** Like, what's the play?

**Jason Gong:** Yeah, I guess it'd be nice if I could connect with them, and then either it's a LinkedIn message or an email.

**Jason Gong:** Like I said, doesn't matter, and then in that message, I'll send them a link, especially to, like, here, where the recording of our last workshop is like this.

**Imran Patel:** Yeah, I think what you can do is probably, I'm assuming you get the email from Luma, right, Kyle?

**Imran Patel:** Yeah, we have everyone's in there.

**Imran Patel:** Yeah, so I think it might be, yeah, one of the things that you can do is probably, would, because LinkedIn has a connection request limit, Jason.

**Imran Patel:** So my, because you're going to be constrained.

**Imran Patel:** By that given, like, I don't know, how many did you have, like, as a registrant, lots of them, right?

**Jason Gong:** Yeah, the whole audience is pretty big, but I think it's like 150 so far.

**Jason Gong:** Right, 150.

**Imran Patel:** LinkedIn will do 150.

**Imran Patel:** My understanding is we think it's between 150 and 200 per week is the connection limit on LinkedIn.

**Imran Patel:** So you'll just get capped by that limit.

**Imran Patel:** My advice is to just send them into a smart click sequence.

**Imran Patel:** Yeah, you can, and then you can, in sift, can just say, like, okay, just blast them out into, like, there are more actions at the bottom where you can kind of do that.

**Jason Gong:** Yeah, well, I guess if I'm just exporting to CIP, I could just import that CSV into, I guess, like, the vehicle in here would just be, you're doing what, I guess, Clay would do or something.

**Jason Gong:** Exactly, yeah.

**Jason Gong:** I would just directly import it into.

**Jason Gong:** Or you could just fire it from HubSpot as well.

**Kyle Doherty:** Yeah, that's I going to say.

**Kyle Doherty:** Yeah, that's true.

**Jason Gong:** Yeah, that's what I would do.

**Imran Patel:** So, it's a more straightforward way of doing it.

**Imran Patel:** Okay.

**Jason Gong:** It's what I would like.

**Imran Patel:** I'm going to, yeah, play around with it, and then, like, you know, let's sync up probably in a week or so to see, like, how things are going.

**Imran Patel:** And we are on Slack anyway, so anytime you're confused, just let us know what, if it can help you.

**Jason Gong:** Got it.

**Jason Gong:** So, right now, I guess just thinking about the way people enter SIFT data, it's, like, engagement on LinkedIn, and then, I guess it's basically just all integrations.

**Jason Gong:** Website, ads, what would the Apollo integration be?

**Jason Gong:** Is that just more pushing to Apollo, or grab?

**Imran Patel:** Yeah, Apollo is more like you, yeah, it's like HubSpot, so we can figure out the status of the Apollo contact, but then we can also push stuff into Apollo.

**Imran Patel:** What's PostHog?

**Imran Patel:** PostHog, we can enrich your app analytics with SIFT data, so we can kind of just, and so PostHog has a user table, right?

**Imran Patel:** And then, like, we can just enrich.

**Imran Patel:** It's the user table with all the information.

**Jason Gong:** Okay, so it's not like, I can't do like, oh yeah, new signup, and then new signup gets pulled in here as a trigger to do, I mean, guess maybe there's no reason, but it's like, oh yeah, connect with all your new signups on LinkedIn, or something, like you wouldn't be able to.

**Jason Gong:** No, we can do that.

**Jason Gong:** You can do that, okay.

**Jason Gong:** Yeah, we can do that.

**Imran Patel:** So like, but do you have a product for signups, or like, where does the signup happen?

**Jason Gong:** No, but we kind of like, or I guess I'm looking into instrumenting, like, the community as a thing in post hoc.

**Jason Gong:** Which apparently you can do, so I was looking at it a lot.

**Jason Gong:** like this, and this AI-led growth is on Circle, right?

**Jason Gong:** It's on Circle, yeah, but like, apparently you can add post hoc, or at least we're trying to add it to post hoc, so then it's like, you know, we got a bunch of people sign up, and it's like, oh yeah, well, I just connected with all of them on LinkedIn, and like, a lot of them aren't paying yet, right?

**Jason Gong:** So it's like, how can I help you?

**Jason Gong:** I don't know, I mean, I think I'm just thinking of options.

**Jason Gong:** as well, Kyle, or no?

**Jason Gong:** No, they don't have a direct connection, so we're going to try.

**Kyle Doherty:** Try to get it just with like a CSV download, and then for like all the ones that exist, and then a simple Zapier connection, because they have a Zapier integration, but that's not set up yet.

**Kyle Doherty:** I see, I see.

**Imran Patel:** I think one way we can do it, I'll look into the Circle stuff.

**Imran Patel:** The way we do it, most of our customers will get product signals from their products through our SDK integration.

**Imran Patel:** And so I can, and I know you are working on a product as well, but like in the future, if you want to pull that signal into SIFT, you can do that as well, Jason.

**Imran Patel:** Let me just put that in the Slack.

**Imran Patel:** I'll share it with you in a bit, but yeah, I think this is, I'm going to go and think about how to get your Circle stuff into SIFT as well.

**Imran Patel:** But you can kind of just make it a cockpit so that it comes here, and then you can kind of send it someplace.

**Kyle Doherty:** I mean, if we could get into PostDog, that would be ideal, because then we could integrate PostDog.

**Kyle Doherty:** Right.

**Imran Patel:** The PostLog integration is pretty good.

**Imran Patel:** I think our friends at Haygen use it quite rigorously because they have lots of product analytics in PostLog as well.

**Imran Patel:** But yeah, the user table, there's documentation about it, so you can learn what it does.

**Imran Patel:** But yeah.

**Kyle Doherty:** Are there any concerns with LinkedIn cracking down on all the scraping stuff and all that?

**Imran Patel:** Yeah, I mean, LinkedIn cracks down on scraping depending on what you're scraping.

**Imran Patel:** I think if you're scraping profiles and sales now, they'll come after you.

**Imran Patel:** They went after Apollo and stuff.

**Imran Patel:** We kind of stick to like just getting scraping stuff that you technically own, right?

**Imran Patel:** Like it's your post, like your engagement.

**Imran Patel:** So like generally we think that that's kind of more or less stuff.

**Imran Patel:** And the way we do it is also somewhat like we only do it through your browser. Like we don't even involve our servers.

**Imran Patel:** It's pretty safe.

**Imran Patel:** We don't even have your tokens or anything.

**Imran Patel:** So, yeah.

**Imran Patel:** One last thing, Jason, you can look at is this pipeline reports.

**Imran Patel:** If you click on pipeline reports on there.

**Imran Patel:** So that's our analytics layer.

**Imran Patel:** If you click on site engagement, that's the one that is actually pretty, what happened here?

**Imran Patel:** Just reload it.

**Imran Patel:** I don't know what.

**Imran Patel:** Oh, yeah.

**Imran Patel:** Click on site engagement on the left.

**Imran Patel:** And that will kind of give you a good understanding of, like, where people are coming from for you.

**Imran Patel:** So, like, and slow on the first time.

**Imran Patel:** But it's nothing like this exists on the market.

**Imran Patel:** And it's like a beta feature right now.

**Imran Patel:** But on the left hand side, you will kind of see the metrics, like how many people coming in, how many accounts.

**Imran Patel:** On the right hand side, you will see the breakdowns of those metrics.

**Imran Patel:** So, like, 27 people came in.

**Imran Patel:** So now if just click on 20, the whole segment is going to slice into it.

**Imran Patel:** And then you can kind of see that.

**Imran Patel:** So if you choose, like, let's just say United States, that as you had, or like, yeah, the seven on pricing, then now you can kind of see the companies that, those seven companies that, like, clicked on pricing.

**Imran Patel:** Yeah, it's like, I'm just getting started, but there you go.

**Imran Patel:** So on the right-hand side, you will see, like, the seven that came in, including me, Deepka, Fowler, whatever.

**Imran Patel:** So, but the main thing is, like, it will help you understand your channel content segments.

**Imran Patel:** You can start your segmenting wherever you want, whatever.

**Imran Patel:** And then LinkedIn is similar.

**Imran Patel:** LinkedIn ads is similar.

**Imran Patel:** Like, the metrics are different there.

**Imran Patel:** So if do LinkedIn ads, it will show you the campaign that you had.

**Imran Patel:** Oh, because you don't have data yet.

**Imran Patel:** It will show up in a bit.

**Imran Patel:** We just connected it.

**Imran Patel:** And LinkedIn engagement, same idea.

**Imran Patel:** You will have, like, let's see.

**Imran Patel:** It will show you likes, comments, engagers, and so you'll see, like, which, like, just in general, what your audience looks like across those posts, right?

**Imran Patel:** And so, you go back, yeah, don't go there.

**Imran Patel:** Yeah, so, like, it's just on the right-hand side, it will show you who's, you know, what kind of industry is interacting with your content and so on.

**Imran Patel:** So it just, like, gives you that breakdown.

**Imran Patel:** Let it populate a little bit because it just started.

**Imran Patel:** Oh, I got it.

**Imran Patel:** Yeah.

**Jason Gong:** Yeah, I mean, yeah, you can do by dimensions.

**Imran Patel:** You can choose the metric on the right-hand side where it says showing post engagers. Yeah, just go where it says all dimensions on the top, and then next to it, choose your metric. So you can choose the metric that you want, and then it will slice that metric.

**Imran Patel:** We're still working on it, but it's pretty powerful in terms of what it will kind of tell you.

**Jason Gong:** Yeah.

**Jason Gong:** Cool.

**Jason Gong:** Let the data come in.

**Imran Patel:** And then the same with LinkedIn ads.

**Imran Patel:** The data will come in and you'll be able to slice and dice your audience or from an analytics point of view.

**Imran Patel:** Yep.

**Jason Gong:** Cool.

**Jason Gong:** All right.

**Jason Gong:** I think about what the first motion is, but this is great.

**Jason Gong:** Yeah.

**Jason Gong:** So like, if I'm monitoring, let's say like guys posts, like what is that?

**Jason Gong:** What exactly is happening?

**Jason Gong:** What's happening is that like, they're pulling everybody who likes or replies to guys posts.

**Imran Patel:** Like how is everybody's coming in into safe now?

**Imran Patel:** Like, how are you pulling that list?

**Jason Gong:** From the extension.

**Imran Patel:** So the extension, like what exactly does the extension to?

**Imran Patel:** What the extension is doing, it's doing two things, right?

**Imran Patel:** It's like, it's pulling the data for you.

**Imran Patel:** It can send the connection request on behalf on you, but then it's like, it does two jobs.

**Imran Patel:** It fetches the data for you, and it, behind the scenes, the system round robins, like, because you are tracking four profiles, so, you know, your extension will pull posts for two profiles and so on.

**Imran Patel:** There's just some internal way that we kind of...

**Jason Gong:** Right, but you're saying it's happening just here locally, or...?

**Jason Gong:** Yes, it's already happening locally.

**Jason Gong:** And how does that work?

**Jason Gong:** Like, is it just spawning, like, a little tab somewhere, or is it, like, there's a way to do that without even...

**Imran Patel:** Yeah, it's just, like, it's a background activity in a Chrome extension.

**Jason Gong:** And that happens, like, what if I just don't have my browser open and my computer's closed?

**Jason Gong:** Like, then it's just not working.

**Jason Gong:** Like, if my whole team has their computers kind of locked off, then...

**Imran Patel:** Yeah, so then it goes in an inactive mode, but generally almost everybody is on LinkedIn.

**Imran Patel:** So it's like, but if you go on a vacation, then what we'll do is if you go on a vacation, then other active extensions will pick up the Slack.

**Imran Patel:** Okay, got it.

**Jason Gong:** And it's like, I guess I have to have the tab open or not?

**Imran Patel:** You don't need the tab open.

**Jason Gong:** I'm just curious what it's doing.

**Jason Gong:** Because I guess like it is scary, like when I log in to HeyGen and give them access. I give them like literally my password or something. I mean HeyReach — I don't know how they do that.

**Imran Patel:** Our stuff, we have no access to your password.

**Imran Patel:** Like we can't log in into LinkedIn because the extension doesn't give us even the cookie or like the auth cookie.

**Imran Patel:** We don't have it.

**Imran Patel:** Um, so we have designed it to be very safe and secure.

**Imran Patel:** So even if we get hacked, like we don't have access to your LinkedIn.

**Imran Patel:** And from LinkedIn's perspective, what they see is like, oh, well, it's Jason's browser that's kind of doing some of this stuff, right?

**Imran Patel:** And so, like, it's just designed that way.

**Imran Patel:** That's, like, pretty, pretty reliable that way.

**Imran Patel:** Cool.

**Jason Gong:** All right.

**Jason Gong:** This is great.

**Imran Patel:** And you can also turn on the toggle if you want the DM to be synced.

**Imran Patel:** Yeah.

**Imran Patel:** One other thing that the extension will do is also when you send a growthx link in LinkedIn or Gmail, it will rewrite the link to include some tokens to add tracking. So when somebody clicks on that link and then they come to your website, you will know who came to your website. Very useful.

**Jason Gong:** Oh, like, only growthx links?

**Imran Patel:** Yeah, only growthx links, yeah.

**Imran Patel:** Yeah.

**Jason Gong:** Like, it's not an issue because our tag doesn't run on Luma, so we can't make the connection.

**Imran Patel:** Oh, I see.

**Jason Gong:** Okay, got it.

**Jason Gong:** Cool.

**Jason Gong:** All right.

**Imran Patel:** We want to sync up probably later next week, just to see how things are going, like quick 15-minute check-in, and like if you have any ideas for any crazy motions, I can help you set them up as well.

**Imran Patel:** Yep, that sounds good.

**Jason Gong:** Same time?

**Jason Gong:** Let's see, Friday.

**Jason Gong:** I'm off next Thursday, Friday, so maybe we could do like late Wednesday or the Monday after.

**Jason Gong:** Basically like everything I'm thinking of doing revolves around this next webinar, so I'll probably play around in this quite a bit. Yeah, late Wednesday or the Monday after.

**Jason Gong:** Yeah, late Wednesday, like 4 p.m.?

**Jason Gong:** Yeah.

**Jason Gong:** Okay, I'll send you an invite.

**Jason Gong:** Perfect.

**Jason Gong:** And Kyle, let me know if you have any questions.

**Jason Gong:** All right, thanks a lot.

**Jason Gong:** Bye.
