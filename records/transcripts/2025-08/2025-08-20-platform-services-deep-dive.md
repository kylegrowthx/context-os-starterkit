# Platform/Services Deep Dive

<metadata>
date: 2025-08-20
time: 20:32 UTC
duration: 26 minutes
organizer: george@growthx.ai
participants: George Haikal (GrowthX), Alex Fine (Understory), Ali Yildirim (Understory)
fathom_recording_id: 81905166
fathom_url: https://fathom.video/calls/385924572
share_url: https://fathom.video/share/v_wicMBf7rqTzKPWCMJmzs7D7WeJk5-L
source: fathom
enriched_on: 2026-03-03 07:22 UTC
</metadata>

---

## Summary

George Haikal conducted a deep dive into Understory's platform capabilities and service delivery process, moving beyond the kickoff narrative to understand the specific systems, workflows, and team structure that power their paid media and go-to-market engineering services. Alex Fine and Ali Yildirim walked through their end-to-end client onboarding process, showed Clay workflows for audience targeting and data enrichment (including real examples like the Remofirst employer-of-record campaign and social content engagement scraping), and explained their reporting infrastructure across HubSpot, Looker, and Google Slides. The key insight: Understory's differentiation lies in blending paid media expertise with Clay-powered go-to-market engineering—a capability neither Understory's founders nor other agencies possess separately, enabling bespoke, data-driven campaigns that outperform traditional paid media approaches.

---

## Context

Understory is a boutique services agency co-founded by Ali Yildirim (Head of Paid Media) and Alex Fine (VP of Operations & Go-to-Market Engineering). They specialize in paid media and what Alex calls "go-to-market engineering"—using Clay to build automations that combine data enrichment, audience targeting, email sequencing, and workflow automation. The agency works with mid-market B2B companies, with a minimum ad spend requirement of $15-20K/month to achieve positive ROI. George is evaluating Understory as a potential partner or reference for GrowthX's content strategy and sales enablement work, particularly around how to articulate their own service delivery to buyers. This meeting served as a working session to understand the specific mechanics of what Understory sells—not just the pitch, but the actual processes, tools, dashboards, and team structures that buyers experience post-signature.

---

## Relevance

**To GrowthX Delivery:**
- Understory's approach to bespoke implementation without pre-canned templates mirrors GrowthX's own model (strategy first, then build). Their intake form process and collaborative strategy development offer a potential reference for how GrowthX positions custom delivery.
- Their use of Google Slides for weekly client decks and Looker dashboards for real-time reporting could be benchmarks for GrowthX's own client reporting structure, especially for managing multiple reporting surfaces (HubSpot for one channel, Looker for another).
- Team structure insight: dedicated specialists per channel with heads-of-channel oversight, plus an exec (Ali/Alex) coordinating cross-channel work. This could be a model for GrowthX's own delivery team scaling.

**To CheckThat / AEO:**
- Understory extensively uses Clay for LinkedIn data scraping, audience enrichment, and behavior-based targeting (e.g., scraping job postings to find companies hiring in new geographies, scraping LinkedIn to find people engaging with specific content). This validates the value of data enrichment and signal-based targeting for B2B—core to CheckThat's AEO thesis.
- The Remofirst use case (scraping Indeed job postings to identify EOR-service buyers) is a concrete example of how job posting data can signal buying intent—relevant to how GrowthX thinks about intent signals.

**To GrowthX Business Development:**
- Understory is managing multiple channels (paid media and go-to-market engineering), each with different tools, metrics, and team structures. This suggests their clients are sophisticated enough to fund multi-channel campaigns—potentially high-ACV, logo-worthy accounts.
- Key qualification criteria: minimum $15-20K/month ad spend, high enough ACV to sustain retainer + ad spend, audiences receptive to outbound (e.g., they avoid cybersecurity professionals because skepticism kills conversion). These are useful qualification filters for GrowthX when engaging potential clients.
- Account structure: Sunry is an example account with 50-60 demo requests/month from LinkedIn at ~$800 cost per lead. This is a strong reference case if Sunry agrees to be publicly named.

---

## Overview

- Understory uniquely blends paid media and go-to-market engineering for optimal results
- Process involves intake forms, strategy development, and bespoke implementation plans
- Team structure includes specialists for each channel and oversight from Alex and Ali
- Reporting done via HubSpot, Looker dashboards, Slack notifications, and Google Slides
- Clay used extensively for data enrichment, audience targeting, and workflow automation

---

## Key Topics

### Client Onboarding Process

  - Intake form guides initial builds and strategy preparation
  - Paid Media: Set up ad accounts, prepare strategy based on client needs
  - Go-to-Market Engineering: Develop implementation plan with campaign ideas, segments, personalization variables, triggers, and signals
  - Strategy development heavily relies on team's extensive experience
  - Kickoff presentations created for both paid media and go-to-market engineering sides

### Service Delivery and Reporting

  - Paid Media: Uses Looker dashboards, Slack notifications for real-time lead gen tracking
  - Go-to-Market Engineering: Primarily uses HubSpot
  - Weekly update decks created in Google Slides for most clients
  - Working to streamline process for automatic deck creation from intake form data

### Team Structure

  - Paid Media: Channel-specific specialist + head of channel + Ali's oversight
  - Go-to-Market Engineering: Head of GTM engineering, GTM engineer, GTM ops person, RevOps manager + Alex's oversight
  - Expertise in both paid media and Clay usage sets Understory apart from competitors

### Clay Workflow Examples

  - Remofirst campaign: Scraping job postings to identify potential clients needing employer of record services
  - Social content engagement targeting: Scraping LinkedIn for prospects engaging with relevant content, enriching data, and automating outreach

### Client Qualification and Limitations

  - Disqualify clients with low ACV where positive ROI is unlikely
  - Advise against outbound campaigns for audiences not receptive (e.g., cybersecurity professionals)
  - Minimum ad spend of $15-20K/month recommended for effective testing

### Performance Tracking

  - Primary KPI for most clients: Demos booked
  - Track cost per lead, meeting request to booking rate, progression to opportunity stage, and closed-won deals
  - Example: Sunry client achieving 50-60 demo requests/month from LinkedIn ads at \~$800 cost per lead

---

## Action Items

**Ali Yildirim**
- Send George kickoff deck + any other relevant onboarding materials for paid media side


**Alex Fine**
- Send George go-to-market engineering deck when received from team + any other relevant onboarding materials

---

## Transcript

**Alex Fine:** Hey, how are you?

**George Haikal:** Doing well. Feels like it's been a week since Monday, but it's only two days ago that we met.

**Alex Fine:** Yeah. Things move fast.

**George Haikal:** Yeah, and you're on too, I'm assuming.

**Alex Fine:** Oh my God, yeah, it's crazy, actually. But no, all good.

**Alex Fine:** Oh, it looks like Ali got a fixer also. I didn't know Ali had it.

**George Haikal:** But I know, we have like an army of the, we have four note takers and three people in this meeting.

**Alex Fine:** Yeah, let me see if Ali's joining. She made the most ridiculous typo. I'm notorious, like I'm well known for typos. And I just said, are you joining for GrowthX? And I said, are you joining GTRoads?

**George Haikal:** Comes with fast typos.

**Alex Fine:** They just get worse and worse. Yeah, my typos are out of control.

**George Haikal:** That's funny, man. Here's Ali.

**Ali Yildirim:** Pretty good, guys.

**George Haikal:** How's it going? How are you doing? Good, man. Going well. I know we're all busy, so we can cut to the chase here. Essentially, the goal of this meeting, right, is we already heard a lot from you on the kickoff side. It was more general storytelling, a lot of really good information. But what I want to really better understand is the how of like how you're actually delivering for clients. Walking through like real client examples start to finish, end to end, like what services you're delivering and when and what that actually looks like. Like if we can go into a client workspace or a demo, essentially what you'd show a client who's about to sign—like not the intro sales call, but a few calls down the line when they're actually asking, okay, what should I be expecting? All that is going to help me better understand the business and add a ton of context for the team.

**Alex Fine:** So what exactly do you need? Do you need the intake form? What do you need, I guess?

**George Haikal:** So like a product deep dive, but however you're presenting to a client, right? Because you have an internal platform that you're using, or you're stringing together Clay and some other tools, right?

**Alex Fine:** Right, yeah.

**George Haikal:** So however you run it now, that would be helpful to see—the how of what you're actually doing. And then on the services side, how you're delivering to a client, what the communication looks like, what the dashboards look like. So essentially, if it was just pure software, it'd be a tech deep dive. But now we kind of have to figure out the how of how you're currently doing it.

**Alex Fine:** Got it.

**George Haikal:** And I have a bunch of guiding questions in this agenda. Honestly, what's better is if you have a usual deep dive or demo that you go through with clients to show them what they're actually buying, we can start there, or I can just start with my questions.

**Alex Fine:** Honestly, I think throwing up your questions could be more productive because on those calls we kind of wing it. Like we don't really do a demo typically. We talk about our capabilities and then once the client signs, we go through the intake process and then everything is totally bespoke. We have SOPs for what we do when any new client onboards. Ali, maybe it's more buttoned up on the paid media side, but for us on the go-to-market engineering side, it's very much like we start building very bespoke workflows based on our customers' needs.

**George Haikal:** And look, that's totally fine. Whatever it is, it's beneficial for us to understand. We do the same thing for some clients—we build it out custom and we speak to it. So we can start with a real example of a client end-to-end, or just the general process from intake form to onboarding—what you need from the client and what you start delivering on.

**Alex Fine:** Yeah, so on both sides of the business, we have that intake form. The intake form guides us through the initial builds. On the paid media side, we get all the ad accounts set up the right way, make sure we're added to everything we need to be added to, and then we start preparing strategy. Same thing on the go-to-market engineering side. We start preparing strategy and an implementation plan—a bunch of different campaign ideas and segments we want to go after, with the variables, personalization, triggers, and signals we want to set up.

**George Haikal:** How do you come up with the strategy?

**Alex Fine:** It's just experience, to be honest with you. Our go-to-market engineers have worked with so many clients. They know what works for certain industries, what doesn't, what offers are going to resonate with audiences. And then they just start building—they basically build a plan and then reverse engineer the entire process in Clay.

**Alex Fine:** Ali, maybe it's helpful to talk about the paid media side and how we kick clients off.

**Ali Yildirim:** Yeah, for sure. We have that intake form that goes out in advance of our kickoff call. The expectation is the client fills that out in advance. And then we put together an initial onboarding presentation and plan. I'll show you the most recent one we did that was really good. They were very clear on what they wanted—MQL volume, enterprise deals coming through. So we looked at the channels that would be the best fit for them. Google Ads wouldn't be the biggest fit because they don't have a ton of keyword volume. We did keyword research on enterprise freight tracking—there's just not a lot of people searching for that. The job titles we want to go after are more easily targetable over LinkedIn. So that's why we went with this strategy. That initial intake process is really important, and then we map that to the campaign types we want to run.

**George Haikal:** This is great. So is there an example of what you build out for Clay for this client too?

**Alex Fine:** Yeah, give me one second. Yeah, there is.

**Ali Yildirim:** And we're trying to streamline this process so where we have the intake form and all these decks just get created automatically and we're just reviewing it—probably very similar to what you guys do.

**George Haikal:** Yeah, definitely. And this is already a lot more than I can get from the website. That's why it's so helpful—actually understanding the process that you run through. Yeah, and I can send you this kickoff deck if it's helpful.

**Alex Fine:** Yeah, I'm collecting one of these decks for go-to-market engineering.

**George Haikal:** Got it.

**George Haikal:** So it's kind of two parts, right? Someone signs on and if they want both, you pitch them a deck on the paid side and then on the go-to-market engineering side. Two decks?

**Alex Fine:** Well, it depends. If someone signs on for Allbound, then we'll do this together, right? But the problem is we've been disjointed in the past. It's now becoming more cohesive on the onboarding, but we don't have a good example of one of those yet.

**George Haikal:** But we do have examples in Silas. So where does all this live? Where does the client work live?

**Alex Fine:** It's in all the search consoles and everything you need access to, and then also in Clay.

**George Haikal:** And how are you reporting to clients and showing them progress and updates?

**Alex Fine:** Most things in HubSpot, to be honest. HubSpot and then on the paid media side, we have Looker dashboards.

**Ali Yildirim:** Yeah, we create dashboards for each client. We use Slack notifications because we run a lot of lead gen campaigns—that's just a real-time way of tracking things. And then we create decks for a lot of our clients. It's like a Google Slides deck where you can basically see week over week the new updates as you scroll through.

**George Haikal:** Got it. That's helpful. And then what's a typical team structure on an account? Obviously it ranges for a big logo. I'm assuming it's both of you most of the time. But what does that team breakdown look like internally at Understory?

**Alex Fine:** So if it's a paid media client, they'll get a specialist for whatever channel they're working. If it's paid search, they'll get a paid search specialist and head of paid search to oversee it. If it's paid social, same thing—a paid social specialist and our director of paid social. And then Ali to oversee the heads on the paid media side. And then on the go-to-market engineering side, you'll get the head of go-to-market engineering, a go-to-market engineer, a go-to-market operations person, a rev ops manager, and then myself to oversee that entire pod.

**George Haikal:** What's the most challenging or frustrating part in this system right now?

**Alex Fine:** I don't feel like it's that frustrating. To be honest, I feel like we've got that pretty buttoned up at this point. It's more so just having the same reporting on the go-to-market engineering side that we do on the paid media side. And the paid media side has historically done a much better job at presenting decks. So the lack of consistency across both teams has been a pain point. But from a team structure perspective, we pretty much have all our bases covered.

**George Haikal:** That makes sense. Ali, what would you say?

**Ali Yildirim:** Yeah, I agree. One thing I'm thinking about lately is because there's different pillars of the campaigns we're running, sometimes one isn't performing the best. So how do we debug and figure out what's wrong with that one initiative? That's one thing I'm thinking about.

**George Haikal:** When someone is trying to do this themselves, what about blending both these channels goes wrong that they're coming to you for?

**Alex Fine:** Can you ask that question one more time?

**George Haikal:** Yeah, so if a company's trying to do this themselves and they've failed at this before, trying to run paid and do all the go-to-market engineering, what about that process doesn't work for them?

**Ali Yildirim:** Because we have experts for every channel, it's not one generalist trying to learn everything. With paid media, you don't just know how to run paid campaigns. You can watch YouTube, but you need to actually spend a bunch of money to successfully run a campaign. There's a steep learning curve because you need access to capital, and not everybody has that experience. Same thing for email—you're going to burn your reputation, burn inboxes. If you haven't had the reps in, it's going to be hard to get off the ground in a successful way.

**Alex Fine:** Yeah, and paid media requires capital to test, capital to play. You need to get that experience, and it takes time. The reason we're great at it is because Ali has eight years of experience doing it, and everyone else on our team is also pretty senior with that experience. And on the go-to-market engineering side, it's brand new. Email deliverability is a moving target. What works in different copywriting strategies is a moving target. Signals and triggers that identify whether someone's in market—it's all a moving target. So being able to have your ear to the ground because this is your sole focus, that kind of experience makes it extremely impactful to work with someone like us.

**George Haikal:** Totally makes sense. Is there a Clay workspace example I can look at?

**Alex Fine:** Yeah, got plenty. I literally got thousands at this point.

**George Haikal:** I don't even know where to start. You're preaching to the choir—the amount of LLM projects and Notion and pipelines we have is semi-gross at this point.

**Alex Fine:** Yeah, let me look around.

**George Haikal:** And while you're pulling that up, you mentioned experience, but other agencies have experience too, right? So how are you handling that objection?

**Alex Fine:** They don't have experience doing what we do—blending paid media and go-to-market engineering to create the best results across both channels. No other agencies are doing it the way we're doing it. For example, on paid media, when you're uploading custom lists and custom audiences on LinkedIn ads, most people use native platform targeting. They want to go after a thousand people, they get 600 because of a 60% match rate. It's inefficient ad spend. Versus if you do what we do with Clay and have our level of expertise, you can enrich the data and build those segments before uploading them. You're going after the perfect ICP, perfect companies based on firmographic, technographic data. You've validated and enriched the data. You get a much higher match rate. There's pretty much no waste. No other paid media agencies are doing that.

**Alex Fine:** Also, go-to-market engineering is brand new. We were early on it. The way our business started is Ali was doing freelance paid media work. We started to work together. I came in on the business side. Then we added cold email as a service. Then from cold email, it evolved into go-to-market engineering through Clay. We were like, how can we blend these together? We put our brains together and came up with a process that's worked. That's how we've scaled our entire business. No one else is doing it because we have both of us. Ali is a paid media expert who now also knows Clay. I'm a Clay expert who's more well-versed in paid media than any other Clay expert. So when you bring us together, you get a two-headed creature that comes together as a superpower.

**George Haikal:** I love it. Super compelling. Do you want to pull up that workspace?

**Alex Fine:** Oh yeah, let me. I didn't build this one, so I can't talk through it as well, but this is one we're using right now that's getting great results. We're using Appify to scrape Indeed to find companies. This is for Remofirst—they compete with Remote and Deal for employer of record services for companies hiring in other countries. We're scraping job postings where they're hiring in other countries, identifying whether or not they're based in the U.S. or any other country where they're not hiring. So if they're based in India but hiring in Singapore, they might need an employer of record. If they're based in the U.S. but hiring in India, same thing. We're finding those companies, finding their domains, and enriching them with job title, the country they're hiring in, their location. We find the actual job LinkedIn URL, the job posting. An example: someone responded saying they're not hiring in Canada. Our go-to-market engineer responded with a job posting saying they are, and the guy replied, oh man, my bad, we are hiring there. That's what this workflow does—it finds companies hiring in other locations where we couldn't find an office on their website. So they likely don't have an employer of record in that country, and we're offering that service to help them hire legally.

**George Haikal:** This sounds like a more niche case, right?

**Alex Fine:** Yeah, everything's totally bespoke. But I'll show you something we build for a lot of clients.

**George Haikal:** Insanely cool. We do this on our end just a little bit.

**Alex Fine:** Yeah, so here's one I'm running from my own LinkedIn profile. It's called Triggerfy—scraping social content. It grabs anybody engaging with posts mentioning go-to-market engineering, LinkedIn ads, Google ads, outbound, RevOps, Reddit ads, and go-to-market strategy. If a post mentions those things and people engaging have specific titles, I grab them. If they're not in Bangladesh, India, Pakistan, excluding competitors and junior roles (SDR, intern, etc.), every week it pulls a fresh batch of prospects meeting my criteria. VP of sales, head of sales development, their company, LinkedIn profile. We match them against HubSpot to make sure we don't have an existing deal or they're not already a client. You can see this one—run condition not met because we have a conditional formula that won't add them. But if they don't meet exclusion criteria and it's a good fit matching our ICP, we send them to a reach campaign that sequences them on LinkedIn. We build things like this for clients but switch up the flow to match their needs.

**George Haikal:** This one is for you guys. It makes sense for you. This is great. Two more questions. What's an example of a time a client asked for something you couldn't do? Where are your limits?

**Alex Fine:** On paid media, it's easy to disqualify people. If they don't have high enough ACV where we don't think they'll see positive ROI, we tell them straight up: I don't think it's responsible for us to take you on because you're not going to see positive ROI. You need to spend a minimum of $15-20K/month to do the right amount of testing. To be ROI positive given your ACV, you'd have to close this many deals. It's just not a good fit—our retainer on top of the ad spend just won't work out for you financially. On the go-to-market engineering side, if they have an audience that doesn't do well with outbound messaging and they want outbound, we tell them: very unlikely you'll see success doing this. If they want to reach out to cybersecurity professionals, they're extremely skeptical of any message. They always think they're being attacked. So outbound is not going to be a great fit.

**George Haikal:** That makes sense. On the paid side, how are you tracking against benchmarks? Obviously clients come with different goals, but what are you showing them in terms of progress?

**Ali Yildirim:** Yeah, the number one KPI clients care about is demos booked. A lot of our clients are sales-led on the paid media side, so they're really looking for meetings booked with their sales team. For one of our clients, Sunry, they're getting between 50 to 60 demo requests from LinkedIn ads a month. We measure against cost per lead—around $800. We look at meeting request to actual booking rate, what progresses to the opportunity stage, and eventually close-won deals. That's the ultimate metric—pipeline and close-won. But we start top of funnel and work from there.

**George Haikal:** This makes sense. If you can send over that deck, Ali, that'd be fantastic. Any of the materials would be helpful for the team.

**Alex Fine:** So what's this session designed to create? What are the deliverables for us?

**George Haikal:** I'll give you an example. For Augment Code, we met with them, they're a Cursor competitor and AI coding agent. On the kickoff call, you can't go as deep on actual differentiators or what makes them different beyond the narrative. So we have to go deep on the context engine, how they're much better for large codebases. That's the point of these details—to really understand the how. Whether it's content or the sales tool database, we understand that. But we're trying to understand how you're solving problems in as many ways as possible, what you can do, what you can't do. We're going to speak to all that and use this as a foundational artifact in everything we do moving forward. Your blending of go-to-market with the traditional way sounds fantastic, and I understand it now, but most people don't. So the purpose of these deep dives is for us to be crystal clear on it so we can inform all the content we write and the strategy behind the database. There has to be paragraphs of words and copy under each tool. Who are we speaking to? What's their intent? What problems are they looking to solve? These are all the pieces that downstream inform that.

**Alex Fine:** Makes sense.

**George Haikal:** Awesome. Appreciate the time, guys. We're getting the discovery calls and deep dives out of the way in the first week or two because we want to be cognizant and respectful of your time. The team will update you on progress this week. I think we're all talking next week for the kickoff, right?

**Alex Fine:** Yeah, for the kickoff with us.

**George Haikal:** Jason from your team just booked some time. That's exciting because I'm doing a lot of CRM enrichment stuff and thinking as well. This is a great place—we've got a ton of good information. We'll keep you updated on the artifacts we create and the strategy we're putting together.

**Alex Fine:** Yeah, of course.

**George Haikal:** Have a good one.

**Alex Fine:** You too.
