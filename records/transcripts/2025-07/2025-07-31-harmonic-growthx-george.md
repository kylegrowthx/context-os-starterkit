# Harmonic <> GrowthX (George)

<metadata>
date: 2025-07-31
time: 18:01 UTC
duration: 16 minutes
organizer: george@growthx.ai
participants: George Haikal (GrowthX), Jack Baylor (Harmonic)
fathom_recording_id: 77780843
fathom_url: https://fathom.video/calls/366937110
share_url: https://fathom.video/share/yL3eZN74uzsrc1yBCje2pV2scj2YWZr2
source: fathom
enriched_on: 2026-03-03 14:35 UTC
</metadata>

---

## Summary

George Haikal (Chief of Staff at GrowthX) and Jack Baylor (Harmonic) discussed Harmonic's platform for identifying early-stage and stealth startups. While Harmonic excels at pre-seed/stealth company identification with its 30 million company and 193 million person database, GrowthX's immediate need for native outreach capabilities makes Apollo a better current fit. Jack recommended GrowthX revisit Harmonic when the company has a tighter ICP and is scaling its sales team post-Series B, particularly for fundraising trigger signals like Series A and B rounds.

---

## Context

Harmonic is an AI-powered platform focused on the VC market, with deep expertise in identifying pre-seed and stealth companies. GrowthX (B2B content marketing and CheckThat software) is exploring tools to consolidate its CRM and prospecting workflow. George explained that GrowthX's founder Marcel currently manages VIP prospects across multiple channels (WhatsApp, email, LinkedIn) in a highly disjointed way, and George is working to centralize that in a CRM. GrowthX recently onboarded HubSpot for general sales and pipeline management. The company has a diverse client base ranging from public companies to stealth startups, all primarily needing marketing department support. GrowthX recently hired its first founding account executive and is transitioning from 100% inbound to building outbound sales capability.

---

## Relevance

- **To GrowthX Business Development:** Harmonic's strength in early-stage founder identification aligns with GrowthX's future sales expansion post-Series B. Once GrowthX tightens its ICP and scales a dedicated sales team, Harmonic's fundraising trigger signals (Series A/B raises) could be a valuable prospecting layer. Jack explicitly recommended reconnecting as GrowthX scales.

- **To GrowthX Delivery:** Harmonic's natural language search and founder background filtering could inform content strategy targeting. For now, GrowthX's immediate need is a CRM tool that also handles outbound outreach — for which Apollo is better positioned.

- **To Tools and Systems:** GrowthX needs a tool that consolidates inbound (WhatsApp, email, LinkedIn, etc.) into a single contact record and supports outreach. Harmonic lacks native outreach; Apollo covers both prospecting and outreach but doesn't go as deep on early-stage companies.

---

## Overview

- Harmonic excels at identifying early-stage (pre-seed/stealth) startups using AI-driven aggregation and filtering
- Platform limitations: no direct outreach capability, revenue data not scalable
- GrowthX's current needs align more closely with Apollo's features for outbound and prospect identification
- Harmonic's strength lies in VC use cases; expanding sales functionality is on their roadmap

---

## Key Topics

### GrowthX's Current Situation and Needs

  - Inbound leads from various channels (LinkedIn, email, WhatsApp)
  - CEO (Marcel) managing high-value prospects across multiple platforms
  - Recently onboarded HubSpot for general sales and pipeline management
  - Seeking consolidated CRM solution with outreach capabilities
  - Diverse client base ranging from public companies to stealth startups
  - Core client needs revolve around marketing departments

### Harmonic's Platform Capabilities

  - Database: 30 million companies, 193 million people
  - AI-powered aggregation from various sources (newsletters, TechCrunch, LinkedIn)
  - Natural language search for specific company criteria (e.g., "startups founded in past year by prior VC-backed founder")
  - Strong in identifying pre-seed and stealth companies
  - Email generation through API waterfall method (20 combinations)
  - Limited revenue data, collected on individual basis

### Harmonic's Limitations for GrowthX

  - No native outreach capabilities from the platform
  - Revenue data not scalable for comprehensive searches
  - Cannot currently enrich existing lists with additional data columns (on roadmap)
  - Better suited for VC use cases than sales outreach at present

### Harmonic Company Update

  - Current team size: 50 (grew from 25 in 18 months)
  - Double-digit ARR with 100% year-over-year growth
  - Focus on VC market (estimated $100M ARR potential)
  - Plans to expand into other verticals after solidifying VC market position

---

## Action Items

- GrowthX to consider Apollo for immediate outbound and prospecting needs
- Revisit Harmonic when GrowthX's ICP becomes more specific, particularly for Series A/B fundraising triggers
- Jack to keep George updated on Harmonic's development of sales functionality
- Potential reconnection as GrowthX scales and builds out their sales team

---

## Transcript

**George Haikal:** They've been doing some big things. We have been moving and growing is how I like to put it. Yeah, man, a lot of stuff happening really fast. I guess the reason we're talking is kind of twofold. Like I have a bunch of use cases, a lot of things in my head, but I'm the chief of staff here at GrowthX. And so primarily, I understand this is a platform for VCs. We know that because our lead investor and like most of the VCs we know use Harmonic. Yeah, and we're talking for like a personal prospecting list and CRM of all the VIPs that the company has right now on our stage. The VIPs the company have are essentially VIPs that the founder has. And so the CEO, I'm trying to put that all in a CRM. It's super disjointed. The CEO, Marcel, has a lot of WhatsApp, a lot of email, a lot of LinkedIn — tying together, connecting the dots for these prospects. And he's closing all of it, but it's all inbound and disjointed. So that's one thing. And then the second is that a lot of the same signals that a VC looks for are the same ready-to-buy signals that we would be looking for in potential clients as well. So I would love to learn more about that during this call as well. Like the signals that we can track, how specific we can get for them, et cetera. So I have a lot of thoughts, a lot of notes, but I just wanted to give you some context. Hopefully that's helpful before we jump in.

**Jack Baylor:** Yeah, the latter topic we support really, really well. I've personally onboarded Amplitude and Vanta. We work with Brex, Notion, Ramp, Retool, all for the same use case of identifying basically the same signals that a VC would be looking for of like really high connectivity, but at a very, very early stage. And if we're trying to stuff our top of funnel with like the most qualified early, early stage companies, there's not really another platform out there that covers like super early stage founders as well as Harmonic. So definitely want to dive into that. And I've got a very good sense of how we could do that. And I could show you kind of how we've been set up at similar teams. But wanted to kind of dig into the first part, because that's definitely interesting. I'm not sure if we'd be able to support it natively, but there's some crazy implementations that we can use our API for. So just kind of, it sounds like, and let me make sure I'm rephrasing this problem correctly to you — you guys are getting inbound from a bunch of different channels, like WhatsApp, Signal, group chats, all that. And you're looking for a way to basically disambiguate where those sources are coming from, and then attribute them to companies. Is that correct?

**George Haikal:** No, so I could have been more clear. We're getting inbound primarily. I mean, the inbound comes from a variety of places, but it's primarily LinkedIn or email. But what I think is more important is like once someone becomes a contact that we're now speaking to, right, then Marcel will take it offline on WhatsApp and like move the ball forward. And so it's kind of like a contact, if I'm thinking of like traditional CRM stuff — a contact will have multiple touch points from WhatsApp or LinkedIn or Gmail. And like if we're able to consolidate that and send messages from the CRM out, that'd be super helpful. So it's less like aggregating the inbound and it's more keeping track of it all. But I think they're also kind of similar.

**Jack Baylor:** Yeah, that sounds like probably a better use case for Apollo. But what are you guys set up with tech stack-wise?

**George Haikal:** So we just onboarded HubSpot, which is good for tracking stuff. And email sequences — I've used it before, but it's not fantastic at that. And so I was wondering if you can connect to HubSpot and things like that too, but that's more for our general sales and pipeline stuff. But being able to connect to HubSpot would be important.

**Jack Baylor:** Cool. Let's dive into the platform. How familiar are you with Harmonic and what we do?

**George Haikal:** Outside of what I've spoken to people about and the website, not much.

**Jack Baylor:** Cool. So we leverage AI in two different directions — on the aggregation side, as well as on the filtering and sorting side. On the aggregation side, we are looking at a variety of sources to be able to identify startups at earliest formation. That's going to include thousands of different newsletters, TechCrunch articles, PR Newswire, like all of those kind of news sources. And then we're also scanning LinkedIn to identify anyone new that's popped up. The reason why Harmonic is able to do this early stage really, really well is because it's effectively two different databases. Let me get a new window queued up for the demo.

**George Haikal:** You're good, man.

**Jack Baylor:** So it's a database of 30 million companies and then 193 million people who work at those 30 million companies. So if you're thinking about it, it's basically two different tables that are intrinsically linked.

**George Haikal:** How many people was that? Sorry.

**Jack Baylor:** 193 million people. And then 30 million companies. So if we wanted to run a quick query — and this is just going to be like easy mode — but we could run a quick search for, let's say, startups founded in the past year by a prior VC-backed founder. We can just punch that in manually using natural language, and then it will go through and search the database for every single startup founded in the past year by a prior venture-backed founder. From here, I can modify the product that they're building, say, just genetic AI or just B2B SaaS. What I can also do is take this into the grid view, and then export it all.

**George Haikal:** Got it. Nice. I mean, how narrow can this go, right? If we're looking for companies who are over 5 million in revenue that are hiring for marketing positions — is that too narrow?

**Jack Baylor:** That's so we can't collect revenue in a scalable way. We can do it on an individual basis, so I can query against Eloquent AI and ask, like, what's their revenue? And this was actually already one that I ran, but Eloquent AI is estimated at like 500K ARR, and this was picked up in a YC mention.

**George Haikal:** Got it. So if I make a list of companies, can I then add another column and have that query run that column to enrich it with that search information?

**Jack Baylor:** That's on the roadmap. It's not there yet.

**George Haikal:** Okay, no, that's fine.

**Jack Baylor:** I'm just giving you everything right now and just seeing what is possible.

**George Haikal:** Totally, that's completely fair.

**Jack Baylor:** So for that, what we would want to narrow down on is either background of the founders or funding. So if we're thinking they're already at 5 million in ARR, they've probably raised some degree of capital. And so if we're looking at just those that have raised in the past year and have been founded in the past year by a prior venture-backed founder, then we could also do those founded and raised this year, not prior venture-backed founder. There's a bunch of different ways to slice and dice off of funding, who works there, and what's their background. So we can include specific companies and then what they're actually building.

**George Haikal:** Got it. Yeah.

**Jack Baylor:** The next thing here is that we cover stealth and pre-seed companies really well. So if we want to narrow down to pre-seed or stealth companies that have that kind of founder persona that you guys do really well with, it's a great fit. Is your core ICP going to be a minimum cutoff of 5 mil ARR?

**George Haikal:** That was more a number I threw out. Our clients right now are ranging from public companies to startups and stealth. And so it's kind of all over the place, but like their core needs are around their marketing department. They need a certain amount of revenue to be able to pay us monthly too. That's stuff I'm concerned about. I guess the other thing — so are you able to send outreach from here?

**Jack Baylor:** Not directly from here. Basically the way that you would want to do it is export this, put it into a Google sheet, and then have one of the many different outreach tools ingest the Google sheet and then reach out to them systematically.

**George Haikal:** Got it. And then this pulls contact info?

**Jack Baylor:** Yeah. So we'll have some stored. We'll have like emails here. But like this company, looks like we don't have any emails for them yet. We can go in and generate emails. So I can go to individual founders and then get their email. If we don't have it yet, what we do is basically do a waterfall, pinging the NeverBounce API like 20 different times with 20 different combinations until we get one.

**George Haikal:** Got it. Okay, sweet. And so I guess just to be transparent, like the couple non-starters for a tool are the sending the outreach one. I do like the signal tracking and like the history of emails and WhatsApp and other touchpoints. So that would have to happen outside of this.

**Jack Baylor:** Yeah, I would say candidly, and this is me being an honest sales rep, but Apollo sounds like the tool that you guys want. Just in terms of because it does both — you can run a search and then also email people. It doesn't go as in-depth with their search criteria, like you can't build as advanced of a search. And it really only covers companies that are like Series A and beyond. Where we start to really become a value add is when stealth and pre-seed companies are like a critical gap. So it's a good tool for sales, but there's definitely tools out there that are better suited for like outbounding and prospect identification. It's where all of those tools universally fall short is at the earliest of stages.

**George Haikal:** Yeah. Okay. That's super interesting to know. I just want to be respectful of your time. That is super interesting to know. It makes sense why it's so heavily used.

**Jack Baylor:** So like for context, for like Vanta, they want to find people as close to incorporation as possible to get them to do all of their SOC 2 stuff. So for them, it's like, okay, the second someone's in stealth, let's hit them up because we don't know if they've registered yet. And we need to get our top of funnel filled with all of those net new guys.

**George Haikal:** That makes sense. Okay, man. Again, want to be respectful of the time. That's kind of why I wanted to lay out all the context beforehand. I've been in the same spot, and I don't like when people waste my time either. I don't think this is the perfect tool for us right now, but everything you gave was super helpful. And like, I think when we get more specific on our ICP and start doubling down after our Series B, I think the fundraising triggers — like Series A raises and Series B — maybe even Series B raises will be like a massive focal point, especially when we start like really scaling and building a sales force around it. Because right now, like we're not even hunting. We just onboarded our first founding account executive that is now just beginning to hunt. Because like I said, it's all been inbound. So appreciate the info and like, we'll definitely be in touch. The tool is awesome. We've only heard fantastic things. You already know how well it works for VCs.

**Jack Baylor:** Thank you. Hopefully, we'll build out more sales functionality as we continue to kind of solidify around the 100 million ARR or so that we think exists within the VC space. And then from there, once we have like the most robust company database, then it's pretty manageable to then launch into other verticals.

**George Haikal:** Yeah, I guess, how's the company doing? Like, I didn't have time to do a ton of research outside of like how it's used, but like fundraising-wise and team size-wise, how are you all doing?

**Jack Baylor:** Yeah, I mean, I joined 18 months ago. I was like the 25th hire. We're now at 50. I mean, double-digit ARR with 100% year-over-year growth. So it's a fun time.

**George Haikal:** That's good stuff, man. That's good stuff. I'm happy for you. Well, for what it's worth, it was a good meeting, Jack. I appreciate it. Super good info.

**Jack Baylor:** Sweet. Hey, George, if you ever want to hop back in, let me know.

**George Haikal:** Always happy to connect. Have your email, man.

**Jack Baylor:** I will. I appreciate it. All right. Cheers. Peace.
