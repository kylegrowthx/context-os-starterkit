# Siit <> GrowthX - Weekly Sync

<metadata>
date: 2026-01-22
time: 15:59 UTC
duration: 45 minutes
enriched_on: 2026-02-28 14:32 UTC
organizer: team@growthxlabs.com
participants:
  - name: Chalom Malka
    email: chalom@siit.io
    company: Siit
    role: null
  - name: Carmel Schetrit
    email: carmel@siit.io
    company: Siit
    role: Product/Marketing
  - name: Kyle Gaudreau
    email: kyle@growthxlabs.com
    company: GrowthX
    role: Advisor
  - name: Matthew Alves-Hill
    email: matthew.alves-hill@growthx.ai
    company: GrowthX
    role: Advisor
  - name: Team GrowthX
    email: team@growthxlabs.com
    company: GrowthX
    role: Team
fathom_recording_id: 116353403
fathom_url: https://fathom.video/calls/538013030
share_url: https://fathom.video/share/9NvGKzpnZxiqTDeU4ryD3tR-ygLxzd9C
source: fathom
</metadata>

---

## Summary

Siit and GrowthX aligned on Q1 conversion strategy to address critical attribution gaps (HubSpot misattributes 90% of MQLs to "direct" traffic) and low conversion rates despite 4x traffic growth. Teams committed to immediate CTA testing (swapping "Book a Demo" for "Free Trial"), technical website improvements, and new content focusing on product "aha moments" over high-friction ROI calculators.

---

## Context

Siit is preparing for Series A fundraising while facing a conversion bottleneck: website traffic has quadrupled through "Tools Pages" inspired by Ramp (organic SEO + thought leadership content), but the company is struggling to convert that traffic into quality MQLs. The core issues are twofold: (1) broken attribution in HubSpot making it impossible to measure which channels actually drive value, and (2) a high-friction "Book a Demo" CTA that doesn't resonate with Siit's technical IT buyer audience. GrowthX advisory team (Kyle Gaudreau, Matt Alves-Hill) and Siit's product/marketing leadership (Carmel Schetrit, Chalom Malka) met to diagnose root causes and execute quick-win tests before committing to larger strategic pivots like a website redesign launching in Q1.

---

## Relevance

- **Fundraising Impact:** Series A messaging and metrics depend on demonstrable channel ROI; broken attribution undermines investor confidence in unit economics and go-to-market repeatability.
- **Product Messaging:** Content strategy misalignment (ROI calculator positioning vs. technical "aha moment" narratives) is affecting conversion, not just the CTA choice.
- **Operational:** Website redesign launching in weeks will sunset the French site and shift messaging—timing is critical for minimizing SEO collateral damage and testing hypotheses before deployment.
- **Team Coordination:** GrowthX advises on analytics audits and SEO technical strategy; Siit owns execution on CTA testing, competitor page exploration, and content pivots.

---

## Overview

- **Attribution is broken:** HubSpot misattributes \~90% of MQLs to "direct" traffic, making it impossible to measure channel ROI and optimize spend.
- **High traffic, low conversion:** A "Tools Pages" strategy quadrupled traffic but yields few conversions, likely due to a mismatch between content intent and the current "Book a Demo" CTA.
- **Immediate test:** Replace the "Book a Demo" CTA on high-traffic blog and tools pages with a "Free Trial" option, which is a lower-friction ask for the technical IT audience.
- **New content strategy:** Pivot from a high-effort ROI calculator to creating assets that convey the product's "aha moment," such as recorded group demos or integration-specific landing pages.

---

## Key Topics

### The Problem: Broken Attribution & Low Conversion

  - **Context:** Website traffic has quadrupled, creating pressure to hit aggressive MQL goals for the upcoming Series A fundraising round.
  - **Attribution Failure:** HubSpot misattributes \~90% of MQLs to "direct" traffic, masking the true performance of channels like organic search.
  - **Low Conversion:** High-traffic "Tools Pages" (inspired by Ramp) generate traffic but few conversions.
      - **Hypothesis:** The "Book a Demo" CTA is a high-friction ask for the technical IT audience.
      - **Hypothesis:** The content attracts a broad audience, and Siit isn't effectively capturing the ICP within that traffic.

### The Solution: Immediate Tests & New Content Strategy

  - **Immediate Test:** Replace the "Book a Demo" CTA with a "Free Trial" CTA on high-traffic blog and tools pages.
      - **Rationale:** A trial is a lower-friction ask for a technical audience, allowing them to "touch and feel" the product first.
  - **New Content Strategy:** Pivot from a high-effort ROI calculator to assets that convey the product's "aha moment."
      - **Rationale:** The ROI calculator is high-effort, low-trust, and better suited for traffic generation than conversion.
      - **New Ideas:**
          - **Group Demos:** Host weekly, themed group demos (e.g., "Office Hours") to provide a lower-pressure alternative to a 1-on-1 demo.
          - **Integration-Specific Pages:** Create landing pages showing how Siit integrates with specific tools (e.g., Okta, JumpCloud).
          - **"How to Deploy X" Content:** Explore programmatic content for deploying specific apps, though feasibility is uncertain.

### Technical & Strategic Considerations

  - **Website Redesign:** A full site rebuild is launching in a few weeks with new messaging.
      - **Risk:** Sunsetting the French site and redirecting it to the English site will likely cause a temporary drop in French-market rankings.
      - **Mitigation:** Ensure all URL changes (e.g., trailing slashes, www vs. non-www) are handled correctly with 301 redirects to minimize SEO impact.
  - **Competitor Pages:** Revisit the idea of creating dedicated competitor comparison pages, a strategy used by competitor Serval.
  - **LLM Traffic:** Analyze which articles are driving traffic from Large Language Models (LLMs) to inform future content strategy.

---

## Action Items

**Matthew Alves-Hill (GrowthX)**
- Audit GA4/Looker conversion tracking; fix dupes; validate trial/demo events

**Carmel Schetrit (Siit)**
- Swap blog/tools CTAs to trial; monitor lift; share results w/ Kyle
- Revisit competitor comparison pages (Serval model)

**Kyle Gaudreau (GrowthX)**
- Review French site sunset; recommend canonicals/redirects to Carmel
- Analyze LLM-influenced articles; share insights w/ Carmel

---

## Transcript

**Kyle Gaudreau:** This meeting is being recorded.

**Carmel Schetrit:** Oh, my God. Hi.

**Kyle Gaudreau:** Long time. talk.

**Carmel Schetrit:** Long time. How are you?

**Kyle Gaudreau:** I'm great. I'm trying to remember the last time. was probably like, I don't know, Q1, Q2 of last year-ish, since we had a chance to speak.

**Carmel Schetrit:** It's been, yeah, like almost a year? No, less than a year, but still.

**Kyle Gaudreau:** Wild, yeah. I have been here over a year now, which is crazy to think about.

**Carmel Schetrit:** How's it going? I heard you're doing great big things.

**Kyle Gaudreau:** know, keeping all of us very busy. I've worn a lot of different hats. I've done all sorts of different roles here. I was doing some stuff on the sales side a bit, getting away from Marcel doing founder-led, but now we have an AE. Helped fill a few other gaps for a bit, and now I lead what we kind of like, consider like a strategy SWAT team. So as things come up with our clients and we need extra support, that's where folks like Matt bring me into the fold.

**Carmel Schetrit:** next time. Yay. Well, I'm glad I get to see you again and pick your brain and use your expertise.

**Kyle Gaudreau:** Happy to help. Happy to help. Always. loved working with you. So excited to get the opportunity again.

**Carmel Schetrit:** Same.

**Matthew Alves-Hill:** Hi, Matt. Hello. Sorry I'm late. My computer decided to, Kanji decided to update all my apps. Forced me to, I just put it off. I put them off all day, all day, delay an hour, delay an hour, then it's like complete shutdown. and it always happens on a sync. How are you doing?

**Carmel Schetrit:** Good. It was just catching up with Kyle. I hadn't seen him in a long time.

**Matthew Alves-Hill:** cool. So let me just share my screen. Got a lot to cover. Carmel, the idea here, and really the main reason I wanted to pull Kyle in, is just to like, I think there are, we have a couple ideas like floating around. And I want to get, like, I want to get us aligned on where we should really be focusing. And especially to help you out, like we've chatted about conversions a couple of times. And I know that like, that's a key focus for you guys through Q1. And we've, there are some plays going on here. Like we've talked about CTAs, there's new website design, ROI calculator discussions, all these kinds of things. And I just want to, that's part of the reason I reached out to us, like, hey, how are you tracking? Because I think probably there was a little bit of a gap between what we're looking at and what you're looking at. So there's a couple of things, conversion tracking, ROI, CTA, ICP. Like I want to air those out and I want to help get Kyle up to speed on perhaps where we can help and offer some guidance, I guess, specifically. So I've, I've ordered them like this. We can start wherever you want, but I think a good place to start perhaps is on the conversion piece, because I know you have like some focus there.

**Carmel Schetrit:** Um, so do you want to be like, yeah, I can give some context. Let's do the conversion piece and the ICP piece. So Kyle, since we last spoke a long, long time ago, website traffic has quadrupled, which is phenomenal. We had a really good end of year last year. So Q4 ended, didn't start strong, but ended really strong. And we need to keep that momentum because we're starting fundraising for Series A right now. And of course, there's a lot of pressure on marketing per use. And we have some very aggressive MQL goals we need to hit now. In terms of conversion tracking, I mean, our conversion tracking is really  up, to be honest, like from every single channel. But the way we're calculating MQL. at the moment is trials, inbound trials, and demo, and inbound demos. And I kind of track them manually-ish. they're in HubSpot, but like, I have to go and make sure that none of them are like fake trials, you know, with fake emails and stuff like that. Now, that being said, so those are like the two big things, and we track those. We track our website traffic, our trials and demos. And our different sources in three different places. One is HubSpot. That's where we can see the trials and demos come in. And then in terms of like traffic, we can look at Google Analytics, and we have PostHog as well. So those are like the three things. Now, in terms of the traffic coming in, we've seen we've Tons of traffic coming to our blog, which I think is more of our ICP, but I can't confirm because we don't really see conversions happening from our blog. I think it's because it's very, you know, it's more top of funnel. Part of the tracking problem that we have is that HubSpot is calling a lot of our trials, for example, direct, even though it's probably not direct.

**Kyle Gaudreau:** It does that when it doesn't know. it's a pretty common, like, challenge attribution-wise. It's like that tends to be where most of your misattribution falls because it's just like, oh, we don't know what to do with this.

**Carmel Schetrit:** It's direct. It's direct, exactly. And, like, the 90% of our MQ balls are direct, which I do not believe. Even for organic search keywords, like, our HubSpot isn't able to tell, so it just says organic search keyword unknown or something like that. Mm-hmm.-hmm. Um, but we've seen a lot more website traffic and we have grown for sure since last year, um, revenue wise and marketing and yeah, like inbound wise in general. However, one of the things Matt and I have been talking about is first of all, we have very aggressive goals, um, for this quarter, especially because investors are looking to see that the momentum is continuing. And I, ICP wise, if I go to like that other bullet point, um, we launched this thing called the tools pages, which we kind of copied from ramps playbook of like driving the, I think you saw probably the review pages for tools and we're getting tons of traffic to that, which is cool. But I don't think all the traffic is our ICP and even if it is our ICP on some of the particular tools, we're not doing anything to capture and convert them. and I think think think that. That's where we need help is like, we're getting this type of funnel traffic, I guess we're not a thousand percent sure that it's the right ICP, but even if it, a portion of it is, we're not, and we're ranking on Google, which is amazing, and on ChatGPT and stuff, we're getting more referrals from LLMs, but we're not doing an amazing job at converting it.

**Kyle Gaudreau:** So I guess that's like to summarize for you where I see the problem. It's helpful. How should I think about that MQL challenge in relation to like other channels, like are you seeing like diverging trends from something like paid, and do you feel like you have a better pulse on attribution there? Just trying to understand like the full scope of like different influences here on the funnel.

**Carmel Schetrit:** it's a good question. So again, because I can't say that our source tracking is very... Accurate. I have a hard time saying what, like, I can see in HubSpot, you know, that the majority is direct. I think actually our organic content is performing best from all of our channels because we're more searchable. We're showing up in Reddit. We're showing up in LLMs. We're ranking pretty high for a bunch of really important keywords. So I feel like actually our content is performing the best from our different, like, more than paid, I would say, from our different channels at the moment. I think that there is a really big opportunity that we haven't flipped on yet, like we haven't figured out what it is on how we can better convert the traffic that we're getting.

**Kyle Gaudreau:** it makes sense. certainly, you know, there's things we can action. I think just the challenge of not to be, like, overly idealistic about it. The ability to say, oh, we did this thing, and then we can measure it, we've learned something from it, and then we feel like we can double down. That's the vulnerability of the tracking issue. I'm sure you know so well, and I'm preaching to the choir on that, but it puts us in a bit of a tough bind there. I also would say, there's a few angles to consider here. One would be, like, it's awesome that ToolsPlay helped us increase a lot of traffic. I would agree that, like, yeah, like, what are things that we can do to convert that better? But also, we should be looking at, and Matt, I don't know if we've done this so far, but we should dig into it, is, like, are we seeing notable ranking changes in, like, solution, use case-based type of content that's more, like, the core site, I would call it? Because generally, the way I think about it, and sometimes the flaw of how I would argue people think about SEO content, It's always in this one-to-one basis. It's like, you create this content, someone comes to it, do they convert on it? And that's something you should absolutely measure, but what we're also trying to do is build your authority over time, and so if we help build that authority to allow you to rank for the really strong demand capture things, when someone is searching that keyword you want to win on so badly because that's active intent and they're highly likely to convert, that may show up in a different space and not necessarily the tool page can influence But it isn't necessarily like, it was that visit. So anyways, some things we can dig into there, but, you know.

**Carmel Schetrit:** And I think generally what you're saying is why we've continued with the tools too, because we thought the same thing of like, well, even if no one's converting on it, at least it's helping us with authority.

**Kyle Gaudreau:** and that certainly should not be understated. And honestly, it just adds to the complexity, even if you had your conversion tracking in a really good place. Like I would say like, you know, whereas that previously at home. We had a pretty strong attribution system. There were some gaps. Even then, it was pretty hard to separate some of these things, and we had to look at it more in an aggregate and an investment standpoint rather than on a one-to-one. made this particular content investment on this particular page and what happened. But anyways, there's more to unpack here. I just want to note that piece. But the other is it comes down to, like, I tend to think of it as, like, the intent and momentum of someone who is coming into this content. what stage are they at? How much do they understand what Seed offers? You know, where are they at in their own buying cycle? And how does that relate to the offers that we bring forward to them? So that was, like, one of the reasons for, like, if we take that to the blogs, I had mentioned to Matt, like, the idea of more prominent newsletter, even knowing, like, There's some challenges there, but we don't have to dig in too deep to that now. But applying that logic to, say, demo compared to trial, at least when I've tested this at varying stops in the past, especially with more technical audiences, I found typically they were more apt to go a trial route. They just want to touch and feel and get in there. And sometimes we'll, like, be of this mindset, especially going back to the phase and understanding of, like, I'm still not sure who Siit is and what they do, or I'm not, they may be at, like, you want them at this level of intent and momentum, but they may be here. That may even mean they're a better fit for a trial at that point. And so, like, that could, I don't expect that necessarily to be, like, a game changer, but that just feels like low-hanging fruit to test, to just see, like, if trial.

**Carmel Schetrit:** So we can swap this out.

**Kyle Gaudreau:** like, here, how does it show up on the tools pages?

**Carmel Schetrit:** I've looked at it, but now I can't.

**Matthew Alves-Hill:** I think it's same way.

**Carmel Schetrit:** On the right-hand side, I think. Sorry, what did you say the company was called that you were at before?

**Kyle Gaudreau:** Before, this was Homebase, but some of things I was mentioning for demo and trial was when I was at Tri, although I've tested that at other places. But Tri actually would sell into an IT audience in some senses, it tended to skew a bit more with RevOps, but we did a lot of testing around live demos, one-on-one demos, and trials.

**Carmel Schetrit:** And did you have, like, so our attribution, again, is kind of . So I can't really track, like, the first touch. I can see where they came in from, like, where it originated for the first time. I can't see, normally I can't see exactly what page they converted on, but I'm wondering if... Part, like, my intuition is that our blog is influencing, it's just, we can't, it doesn't track it in the same session, so, like, when they come back way later, we know, you know, that actually our blog influenced, and that was the first touch.

**Kyle Gaudreau:** I don't know. There's complexity to solving some of that, I mean, you know, I could try to take a look and see if there's anything I can pick up, but, like, I don't know if I'd have high confidence in, like, being able to easily help you solve it, but.

**Carmel Schetrit:** Well, I'm wondering if that's even important, or if it's, like, we have, we need, because ultimately the goal is, we need to increase the velocity of our MQLs at the moment. Agreed. But what are we going to double down on if we're not super smart on, like, exactly where people are coming from?

**Kyle Gaudreau:** it's one of those things, like, I would, I would want to action, and I'd be careful of, like, impact for effort on. At this point in time, yeah, focus on driving the MQLs as much as possible. But if you keep kicking that cane down the road, I feel like you're going to get stuck to being able to continually make the bets you want. That would be my concern and just advice on that.

**Carmel Schetrit:** Which is the big fight that I had with our CEO today. But to get some of this fixed with a contractor, and he's like, no, we need to do it in-house and hire. And I'm like, that's going to take time. And he's like, I don't care.

**Kyle Gaudreau:** well, so I think as a potential short-term somewhat stopgap, and maybe this is, it's almost like you knew where I was going with this, Matt. I'm not very intimately familiar with, like, how you have your event set up in NGA. But, like, if we can, one, validate it is accurate, or two, just tweak it so it is, we can at least get some pretty useful directional data there. Especially because... Because it won't help us understand maybe the quality side of it, certainly, but we would be able to track form submits.

**Matthew Alves-Hill:** so on that point, I've been testing it a little bit earlier this week on making sure that, Looker at least, what we're looking at is correct. So the book appointment is the free trial and then the request demo, these page view requests, sorry, everyone has different names for these. page view request demo and ads conversion appointment. These are our two like request demo or book appointment events, granted them, a couple of these might be me from last, from, from this week, but, um, we are, like, Trial sign up on the drop down.

**Carmel Schetrit:** In the event name, you're sure that it's not, oh, it's page view sign up, I see. Page view sign up, yeah.

**Matthew Alves-Hill:** So I did do some testing. These are the two. Does this, like, at first glance, like, okay, four from last week, does that stack up or are you like, I'm not seeing any of this on your side?

**Carmel Schetrit:** I'm trying to, so we have. And this is filtered for.

**Matthew Alves-Hill:** This is, sorry, this is filtered for just our URLs and just the blog here.

**Carmel Schetrit:** And how many, so there's different things I'm looking at here. I'm looking at the book appointment one, so the event counts four, which we mean, means we've got four trials from there.

**Matthew Alves-Hill:** Event count, so yeah, this is actually, this is since December 23rd, so this is tracked in three weeks. And the suggestion is this book appointments, so free book demo, no, sorry, free trial, is four of these over the last three weeks. From the specific page there.

**Carmel Schetrit:** So I could be. We have definitely, I mean, just last week we had like 16 trials, I think, or something like that. So numbers could be. I don't know about the lending page source, but it could be.

**Matthew Alves-Hill:** Now that I'm looking at this, actually, this may be duplicated.

**Kyle Gaudreau:** We can dig into it. I think, you know, the more pressing matter is, like, what are we actually going to do? From a conversion standpoint, we can dig into, like, the tracking it, of course. so I think the, like, the trial thing, that's just, like, low-hanging fruit that we should test. hopefully we can, like, loosely see if there's lift and, you know, make an assumption that it's correlated to that. We can investigate, you know, if we're seeing anything or low-hanging fruit for some of your other pages that could, like, be capturing some of the demand capture. there's some optimizations we could recommend there that could raise their rankings, that could help. Outside of that, then it becomes, like, other types of CTAs we can introduce or move around or prioritize content that may be more bottom-funnel-based. The idea of the ROI calculator, I mean, you know, maybe Matt had shared this. I've been pushing back on it internally, but...

**Carmel Schetrit:** Tell me more. I'm not married to it.

**Kyle Gaudreau:** I would love to hear. I will caveat this with...

**Carmel Schetrit:** Be brutal.

**Kyle Gaudreau:** I will caveat this with, I've been wrong about tests many times before, so I don't pretend like I know everything on this. Uh, I will just say, at least in my experience, what I have seen is generally... ... ... And the impact for effort isn't there on these sorts of projects.

**Carmel Schetrit:** It's a lot of effort.

**Kyle Gaudreau:** It's a lot of  effort. exactly. when we did this when I was at Distilled Networks, which I think is the extreme end of this, oh my god, it took so long.

**Carmel Schetrit:** just me doing all the logic and all that, it's a lot of effort.

**Kyle Gaudreau:** and then there's, like, you know, the side of, like, how much trust is someone going to have in this, like, I think there's an inherent bias assumption on this, right? And that doesn't mean it can't work, but where I've seen it work more is as a traffic play, not a conversion play.

**Carmel Schetrit:** and what we're trying is the conversion play. I feel like, so one of the things that I've been struggling with, we're running this provisioning, application provisioning campaign right now, which is, like, us, basically. Reaching out to these different audiences based off of their tech stack and explaining that we can auto-provision access to tools, to different tools, instead of IT having to manually do it and jump through a million hoops and take forever to do it. One of the things in general I'm struggling with in our emails is that we actually have very good open rates. like, the email that I sent out this week had, like, a 25% open rate or something, which is pretty good. And then, like, a very, very specific one that was, like, to a small audience but that are using JumpCloud, which is, like, a specific tool, had, like, a 33% open rate. So that's good. Click-through rates are really low. And I'm struggling to, like, we have no assets, I feel like, that we're sharing. And that's where the ROI calculator came about. was, like, oh, well, maybe we could, you know, share this out and put this on different places. But, like, assets are a problem.

**Kyle Gaudreau:** Assets are a problem in terms of scarcity or that lack of buying?

**Carmel Schetrit:** we have, we have none.

**Kyle Gaudreau:** yeah, yeah, I noticed. that's.

**Carmel Schetrit:** And that's why I was trying to think if like GrowthX, if it's worth, you know, using you guys to like start creating other assets or if maybe that's a waste and we don't think they're actually going to convert.

**Kyle Gaudreau:** it's, it's a fair question. could we find ways of doing, you know, white papers or whatever.

**Carmel Schetrit:** like easier assets.

**Kyle Gaudreau:** Like probably. Do those move the needle enough? Like I, that I'm not certain of, but like we could certainly experiment with it for you.

**Carmel Schetrit:** Very fair question. And that was my question too. does it move, will it move the needle? And you're totally right. Like that. An ROI calculator is a ton of effort and like we don't even know that it's going to convert and maybe we should try something lower. I also don't know when the age of like in 2026, yeah, people might be reading emails. Are they necessarily clicking? Meh, I don't know.

**Kyle Gaudreau:** What do you feel like, I don't know if you get this from like calls or like gong calls or any sort of thing you use to record, seat recorder, whenever I see this on this meeting. What is the thing that gets people to like that like aha moment for you all? Like maybe they're not understanding because like the way I don't think this has to be just thought about like jumping just to the conversion point because like ultimately like I like how Marcel frames this like what is that right next best action for someone who's coming to this content? That may not be a conversion point. It's just about how do you continue. And that could be some sort of, like, page, if you don't have it today, that communicates something that helps get them to that aha moment without needing to talk to the sales team and that may give them more momentum to want to convert on, say, a trial. like, I used to think about that, again, going back to Trey, was, like, I did a ton of, like, interviews with, like, our SCR teams and, like, other folks, and I just realized it was, like, three of Three calls or whatever that they would get to that, like, moment if they did. And I was, like, wow, that's a problem. that's super inefficient. what things can we introduce into what we do? Very intentional to try to tackle that. And that ended up working quite well for us. And so there was a lot of experiments with that in mind. Some of them were presenting conversion things, but others were, like, how do we use chat to do some of that? How do we create other pages that do some of that and, like, layer that into the fold?

**Carmel Schetrit:** So I got to imagine there's something here. I just. Oh, 100%. I need to, I think, dig. there's a few moments that I think are aha moments that we probably don't do a good job of around like, so the premise of this like app provisioning campaign was that is a really good wedge for us. Like it's a really good foot in the door where people realize that that's like, or prospects realize that's a huge pain point for them and suddenly they're interested. But it's a lot around request management, around our integrations, around like the ease of automating common types of like low level requests. And I feel like the reason we've been pushing for book of demo, like definitely we get more trials, but when our product is not explained well, so that when someone gets on a demo, normally they're way more likely to convert than if they just play. And I think that gets to your point that, like, it's, we're not doing enough to get the value across.

**Kyle Gaudreau:** I mean, certainly, like, a trial just standalone, you all have introduced things into it, but, like, yeah, like, it needs things to, like, pull them through. But, like, you know, okay, you have, like, a platform overview.

**Carmel Schetrit:** And we're doing, we're going through a rebrand and, like, I completely redid our entire website, which should be live in a couple weeks. So hopefully our new, yes, and it will look a lot better, but hopefully bigger than, like, looks-wise, our messaging positioning will be a lot more sharp and, like, very clear on what we do. And, like, try to distill it down to, like, you build your workflows and your system and your playbooks for your agents, you deploy them, everything runs. Smooth and seamlessly across IT and across all your internal operations and then you can measure and the measurement and the analytics part is big too because it shows your efficiency but it also shows you where your bottlenecks are so that you can improve even more and like that's kind of like the whole premise of how we want to position ourselves.

**Kyle Gaudreau:** Makes sense, makes sense.

**Matthew Alves-Hill:** Kyle, just adding on the, like, on that stepping stone point, like Carmel has already, that's in play with the new site so the idea is that there will be landing pages that, for specific provisioning, so the jump clouds, octas, et cetera, that will show in like, in a slide, in a real, in a slideshow essentially like how this, how easy this is. like, out of a tool page, like, hey, this is how it integrates with those identity providers. So there is that stepping stone coming with the new site, and I think that is perhaps a more powerful, like, hey, this is the next step, especially out of the tools pages. So yeah, I just wanted, I think I had shown you to that, but that kind of thing is there coming, too.

**Kyle Gaudreau:** because just, you know, framing a little bit of, like, there's different ways of doing this, but, you know, giving a bit more context of, like, how it works, the challenges it solves that may not be coming through our content can sometimes be directing people into those pages. If you direct them into that kind of content, and it also has very clear paths to conversion, you know, options to convert, you know, that can work well. But that sounds like that's a little bit down the road. a couple weeks, but I know every week counts for you right now.

**Carmel Schetrit:** Yes, every week counts. Do you have, like, an idea, bank, from your past life of, like, the types of things you were trying out? To better convey your value prop or your aha moment, like I'd love to just take a look and be like, oh, maybe I can do something like that.

**Kyle Gaudreau:** I don't know how much this is applicable to you all, but I, you know, this, like, this approach to the demo you have now, I think you framed it as like a live demo. It seems like it's more of a one-on-one style. The thing that worked really well for us at Trey was actually doing more like group style, like weekly demos. And what we did was initially for a while, like at least six plus months, we did it as like just like broad.

**Carmel Schetrit:** And sometimes we would, it's not like we would. Where did you promote it? LinkedIn. On email?

**Kyle Gaudreau:** LinkedIn. It was across the website. It was pretty course. Like we actually would offer multiple CTAs. And that was kind of like counter to like some best practices, but it worked really well. And the philosophy was basically like, different people are going to be at different phases, want to learn different ways. Let's give them options. And if we want to optimize that for a variety of reasons later on, we can. But essentially what we would do through that is just like walkthroughs of like the trade platform, solving particular challenges that would help get people to those aha moments. And then we would take those videos and we would also repurpose them.

**Carmel Schetrit:** We would get them later on.

**Kyle Gaudreau:** So it just gave us all this, like this different, these different things we could do. So I know like getting something like that going is not the easiest, but that was probably.

**Carmel Schetrit:** think that's interesting. That's a cool idea.

**Kyle Gaudreau:** And then eventually we started to like promote them on a clear theme ahead of time.

**Carmel Schetrit:** Like we're going to talk about this particular subject. So it's like an office hours vibe.

**Kyle Gaudreau:** Well, like there was Q&A and things of that nature. We're on. Average, we would have, like, actually, now I'm forgetting. It wasn't a huge amount of people that would attend. It ended up getting into, like, the low hundreds, I think. But in the early days, it was probably, like. That's huge for us. No, for sure. But, like, it took us time to build it out, to be clear. it was a lot of effort. It was probably closer to, like, the 20s, 40s in the early days. And then what was really cool is sometimes people would come multiple times to these and then eventually convert. And I remember there was some huge deal we had. I can't remember the company, but they had attended, like, five of these weekly demos and then converted to, like, one of our biggest deals ever.

**Carmel Schetrit:** And it was just, like, this, like, time and attention.

**Kyle Gaudreau:** Basically, what we would do is we had a marketer who would be, like, the emcee who would be leading it and just kind of organizing everything. And then we had, like, an essay, basically, who would come in and just, like, you know, do some walkthroughs who were, like, good to, like, show some of this and, you know, show off the things that they needed would be compelling for that audience. And so, I don't know if there's this play here that could work, but that was one of the biggest things. That's interesting.

**Carmel Schetrit:** like. brand I don't don't don't And I feel like it's maybe lower pressure than booking a demo, like a 30-minute demo yourself.

**Kyle Gaudreau:** Because honestly, like the way I think about live demo, or sorry, book a one-on-one demo is back to that concept of like momentum. They're going to, what is going to go through their mind is like, oh, I'm going to have to talk to a salesperson. And like, are they ready? Do they, like, it's sometimes, like, this isn't true for everyone, but for some people, it's like, ugh, am I really going to get enough value from this?

**Carmel Schetrit:** I'm super busy. especially for an IT audience, I feel like they don't, they don't love that.

**Kyle Gaudreau:** So I would say, you know, we can work through, if we, if we can like swap that demo and the blogs and tools pages for trial for now, I think that's a worthwhile test. that may not work, but that could be like one of your quickest wins.

**Carmel Schetrit:** I'm going to try it.

**Kyle Gaudreau:** We can explore what's happening, if there's any quick win optimizations on the solution pages for more demand capture. I'm sure some of that will change with the redesign, but maybe there's things we can bring forward into that. The other is like, you know, I know we've explored varying like programmatic opportunities with you and different ideas for like landing pages. Have we like dug in, I was thinking about it this morning because I was looking at your app access campaign doc really briefly. Have we done anything around like how to deploy X, like how to deploy Zoom, how to deploy blah, blah, blah. I don't know if there's, I know that isn't exactly what you, you're a piece of helping them with that, but I wonder if there's some things to.

**Carmel Schetrit:** How to deploy specific tools with app access? No, but we could do for the like specific IDPs we integrate with. So there's for the Google, Microsoft, Okta, JumpCloud. We could do a how to. I don't know how easy it is to talk about the, like, full setup you need for that, to be honest.

**Kyle Gaudreau:** That was the thing I was a little less certain about. It wasn't one that I had, like, high conviction on yet, but I was just trying to see if there was a potential for, like, a long tail of going after different apps there, but it sounds like it might be more limited.

**Carmel Schetrit:** No, but I was thinking that for the tools pages, we don't really talk, like, yeah, there's, like, a small section that's like, this is how Seat integrates. But maybe there is potential there on either, like, embedding a demo video of how, because our integrations are, like, a really powerful piece of the product. And some of the tools pages that we have, like, we integrate with whatever tool that is. And we have a small section, like, how this integrates with Seat, but not, you know, maybe there's more we could do there.

**Kyle Gaudreau:** yeah. How does chat do for you all? Do you get much out of it?

**Carmel Schetrit:** I see you have it. I I you. Um, we get, we, there's some activity, people ask about pricing, sometimes it's spam, sometimes it's like features, I wouldn't say it's like blowing up, but we have some activity on it.

**Kyle Gaudreau:** Um, and as far as like the, the redesign, uh, is there anything that would be helpful? Are we too late in the game to help with anything there or, you know, um, I, I was going to ask you a non-related question.

**Carmel Schetrit:** Um, and maybe the redesign will give us more opportunity to, you know, create more pages that we think would convert better. I saw, I don't know if you, you're in the bay. Serval is our big competitor that raised a  ton of money with Sequoia. Um. And they're doing like the competitor landing pages, which you and I had talked about a really long time ago. But maybe it's worth bringing that idea back because we did the tool review pages, but we didn't do like competitor pages. But non-related, I was going to ask you, so we're doing a full rebuild of our site because the way it was built before is like really problematic on Webflow. And there's going to be 301 redirects for everything, but, and we're going to sunset the French website.

**Kyle Gaudreau:** We decided that. Oh, I remember that whole.

**Carmel Schetrit:** that whole thing. We don't maintain it. And like, it's whatever. But I'm still scared at the bottom of my heart that it's going to mess up all of our traffic and like indexing and stuff. And I need you to tell me it's going to be okay if we do it properly.

**Kyle Gaudreau:** so before the French part of this, what is the. Impetus for everything needing to be 301 redirected?

**Carmel Schetrit:** Because it's, well, not everything. Like old pages that will, new pages will be 301 redirected.

**Kyle Gaudreau:** It's not a lot, actually. got it, got it. I wasn't sure if you were, it was like, because like, for example, this is a pain when we were at Homebase. When we went to Webflow, we had to redirect the whole site because they didn't handle like a trailing slash in their CMS, which is like super dumb. And so like, that's actually like a small thing that like can mess up migration. So always be mindful of things like, do URLs default to dub, dub, dub, no dub, dub, dub? Do you have a trailing slash or do you not have a trailing slash? Each of the, any of those things changing is a new URL in Google's eyes, right? And so sometimes these are like the small things like teams miss when they're doing migrations.

**Carmel Schetrit:** And then we're still, we're in Webflow now and we're staying in Webflow.

**Kyle Gaudreau:** We just have. so you should be fine. Different container. The French part of this, I would noodle on this one a little bit. there's an argument that some make, and we're literally going through this with another client now and their own migration. They're very interesting, complex migration. have three domains, active and live, at the same time.

**Carmel Schetrit:** I'm just like, why?

**Kyle Gaudreau:** Oh, wow. I'm trying to help them through that. But what we're doing with them is actually more of like starting with doing canonicals and like leaving that content up and then communicating this is the canonical correct page for this. And that helps to like somewhat de-risk losing of rankings. It's not a guarantee. It's not like doing three or ones is going to guarantee you lose rankings. But I could take a look at like, could that be the move for you all? That makes sense. But I'm guessing with, when you're flipping this switch for the, for this read. is there any world where it would make sense or you could even keep the French website live at any point?

**Carmel Schetrit:** Not that I'm pushing for it, but. No, I mean, not really, because we didn't design the way, the way Webflow does, like, the, a different language. we tried, they offer a localization tool and it's , so you have to translate everything one for one. And we have all, I, like, completely redid the messaging architecture for our website, so, like, all the messaging is new.

**Kyle Gaudreau:** like. it's tough.

**Carmel Schetrit:** And I don't want to.

**Kyle Gaudreau:** It probably doesn't make sense.

**Carmel Schetrit:** I pull the bandaid off and be like, you know what, we'll redirect the French to the English, which we already kind of do for most stuff. We don't create any new content in French. I was just worried that since it's completely going to be redirected to English, that it's going to hurt our rankings in France, which it probably will.

**Kyle Gaudreau:** But, you know. It will.

**Carmel Schetrit:** But, I mean, I think, like, I'm trying to remember. But we're French. If we were doing this in the U.S.

**Kyle Gaudreau:** I'd be like, okay, this is the big deal.

**Carmel Schetrit:** We're already French, you know, like, I don't know.

**Kyle Gaudreau:** I can't recall all the different things I had picked up from my analysis when we looked at this last year, but like.

**Carmel Schetrit:** You were like, for a while, you were like, well, it's driving some traffic, but our traffic was so low. Now I think you'd be like, well, you know.

**Kyle Gaudreau:** it's probably flipped, I'm guessing. it should probably, like, you could theoretically have a hit for sure. But, yeah, I got to imagine it's not a huge proportion of your traffic at this point. You could reclaim some of that. The thing, like, how much of that traffic was, like, actually, like, English intent traffic. Because I do recall there was, like, a mixed bag of some of that. was like, yes, the French website's ranking, but it was actually for, like, English intent searches. And so, hypothetically.

**Carmel Schetrit:** Which it could be now, too, because we don't do any new French content at all. I think.

**Kyle Gaudreau:** But clearly a lot, you're balancing, not being able to attribute, doing all this, this is, it sounds like a lot.

**Carmel Schetrit:** I was so frustrated today. it's tough. And I'm going on maternity leave and I actually didn't tell Matt.

**Kyle Gaudreau:** Congratulations. Amazing.

**Carmel Schetrit:** you.

**Kyle Gaudreau:** When's that happened?

**Carmel Schetrit:** May 1st. So I'm also trying to hire for someone to like, you know, join the team so that they're not left with no forgetting about me.

**Kyle Gaudreau:** I'm trying to remember. Is this baby number one or?

**Carmel Schetrit:** Baby number one. Wow. Baby boy number one.

**Kyle Gaudreau:** Amazing.

**Carmel Schetrit:** Amazing. So there's that too. So I'm like, I have all these things and I'm on a time crunch.

**Kyle Gaudreau:** I'm like, okay. Hey, it's a good motivator. That's really cool. Um, well, yeah, it's certainly empathize having been in-house marketing. I've for many, many years.

**Carmel Schetrit:** I know the pressure is all too low.

**Kyle Gaudreau:** My lordy. So I will continue to noodle on this.

**Carmel Schetrit:** think like. Let me try the few things that you said too and like check back in with you also. And like, you know, just get your feedback as well. Like async, but yeah, noodle.

**Kyle Gaudreau:** And if you think of something else, let me know.

**Carmel Schetrit:** I think Matt logged off, but I think one of the things that would be super helpful for us is to also understand like, to better understand in terms of the articles that we're publishing, which ones lately do we see that are influencing LLMs and that we're getting more traffic to just to like also see what the lay of the land is, which I don't think we have a great read on right now.

**Kyle Gaudreau:** Fair enough. I will communicate that back. It's an interesting complexity now with like where AEO is of like the different layers of like what to build into our reporting.

**Carmel Schetrit:** you know, you know, know,

**Kyle Gaudreau:** And of course, welcome your feedback of like, it's this balance of like, you don't want to show a ton of data and like communicate the key points, but then there's like meaningful things that we need to And so I think that's worthwhile digging into for sure. By the way, as well, feel free to tag me in the channel.

**Carmel Schetrit:** I'm still in there.

**Kyle Gaudreau:** don't be shy to ask me questions. Great. awesome. Amazing catching up.

**Carmel Schetrit:** Congratulations again. great catching up. Thank you. Always good to see you. And yeah, I'll, I'll, um, I'll keep you in the loop when I need your brain picking.

**Kyle Gaudreau:** Sounds good. All right. Enjoy the evening.

**Carmel Schetrit:** for the late call. Of course. Anytime. Bye.

