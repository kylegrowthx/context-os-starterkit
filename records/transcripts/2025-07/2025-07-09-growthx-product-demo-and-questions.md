# (GrowthX) Product Demo and Questions

<metadata>
date: 2025-07-09
time: 19:00 UTC
duration: 38 minutes
organizer: nemanja@growthxlabs.com
participants: George Haikal (GrowthX), Nemanja Simic (GrowthX), Sydney Go (GrowthX), David Edoh-Bedi (Metronome)
fathom_recording_id: 73180473
fathom_url: https://fathom.video/calls/345265074
share_url: https://fathom.video/share/g5ga1BBxaRztGvHX9Urt2jygSxsTY1yz
source: fathom
enriched_on: 2026-03-03 08:15 UTC
</metadata>

---

## Summary

David Edoh-Bedi from Metronome walked the GrowthX content team through a comprehensive product demo covering Metronome's usage-based billing platform, using a fictional AI speech company called Vocalist as the example. Key differentiators highlighted were Metronome's centralized rate cards (allowing single-point pricing updates for all customers), modular architecture, and real-time alerting capabilities. The team scheduled a follow-up call for July 16 at 2pm Pacific to dive deeper into competitive positioning, PLG vs. SLG strategy, and case studies of superuser customers including OpenAI, Anthropic, Databricks, and Confluent.

---

## Context

GrowthX is engaged with Metronome on a content marketing engagement focused on developing content strategy, editorial plans, and a white paper. This meeting was the product deep-dive phase of the engagement. David Edoh-Bedi is a product leader at Metronome who came from Stripe and is heading up the product team. The GrowthX team attending — George Haikal, Nemanja Simic, and Sydney Go — are working to understand Metronome's actual customer problems and use cases so they can develop targeted, authentic content that resonates with both large-scale AI companies and smaller startups. The conversation reflects a standard content discovery phase where the vendor educates the agency on product nuance so the content can move beyond generic positioning.

---

## Relevance

**To GrowthX Delivery:**
- Metronome's product architecture is modular and technical — the content will need to address both technical audiences (engineers) and commercial decision-makers (finance, product) separately
- Rate cards and real-time alerting are core differentiators vs. Stripe; content should emphasize the operational simplification (single-point pricing updates vs. per-customer updates)
- Customer profiles vary dramatically (OpenAI vs. 20-person startups), suggesting the content strategy should include separate messaging lanes
- David flagged PLG (product-led growth) vs. SLG (sales-led growth) as a key conversation for next call — this will shape messaging about ease-of-use and self-serve onboarding

**To CheckThat:**
- Metronome processes millions of usage events and invoices monthly at high scale (OpenAI, Databricks, Confluent), which could be interesting for AI visibility / AEO positioning if Metronome is a platform used by major AI companies
- Real-time event processing and alerting mechanisms could inform CheckThat's understanding of usage-based pricing models in the AI space

**To GrowthX Business Development:**
- This is a $200k+ engagement with clear project momentum: content strategy and editorial plan due end of week, white paper strategy in progress
- Follow-up call scheduled for July 16; David is engaged and willing to provide case studies, customer profiles, usage metrics, and answer detailed questions in Notion async
- George framed the need for content precision around different customer segments (big scale vs. small startups), indicating this is a strategic engagement worth deeper investment

---

## Overview

- Metronome's core differentiators: centralized rate cards, real-time alerting, and modular architecture
- Key customers include OpenAI, Anthropic, Databricks, and Confluent
- Rate card feature allows centralized pricing updates, highly valued by customers
- GrowthX team working on content strategy, editorial plan, and white paper for Metronome

---

## Key Topics

### Metronome Platform Overview

  - Built with modular architecture: data platform, pricing engine, customer configuration
  - Real-time event processing and alerting capabilities
  - Integrations with invoicing, marketplaces, ERPs, and data warehouses
  - API and alerts module enables product decisions based on usage thresholds

### Metronome Data Model

  - Core building blocks: billable metrics, products, rate cards, and contracts
  - Rate cards centralize pricing, allowing easy updates across all customers
  - Contracts define commercial agreements with customers (e.g., monthly, pay-as-you-go, enterprise)

### Product Demo

  - Walked through creating billable metrics, products, and rate cards in the Metronome dashboard
  - Demonstrated ease of setup and configuration for usage-based billing
  - Showed how to assign contracts and simulate usage events

### Customer Insights

  - Super users include OpenAI, Anthropic, Databricks, Confluent
  - Rate card feature highly valued for simplifying pricing updates and experimentation
  - Alerting mechanism also receives positive feedback from customers

### GrowthX Content Strategy

  - Team working on content strategy, editorial plan, and white paper
  - Artifacts for style, tone, and competitor analysis pending review
  - First iteration of content strategy provided for editorial and white paper

---

## Action Items

**George Haikal (GrowthX)**
- Schedule 30min follow-up call w/ David for Wed 7/16 @ 2pm Pacific
- Review agenda for next meeting, extend time if necessary
- Prepare & send publication calibration doc to Metronome team

**Nemanja Simic (GrowthX)**
- Finalize & submit white paper content strategy draft

**David Edoh-Bedi (Metronome)**
- Send case studies, customer profiles, usage metrics to GrowthX team
- Answer GrowthX questions in Notion doc, tag George

---

## Transcript
**George Haikal:** Man, how's it going?

**Nemanja Simic:** What's happening, George?

**George Haikal:** Yes, sir. Doing what we can.

**Nemanja Simic:** Bro, you look exactly like one of my friends from high school. It's crazy. He's a Serbian guy. I don't know what your background is, but you guys are like identical.

**George Haikal:** Half Lebanese, half Panamanian.

**Nemanja Simic:** Half Panamanian and half Lebanese? I don't know where the mix is from, but you guys are weird, man. Throws me off.

**George Haikal:** What's his name?

**Nemanja Simic:** His name's Stefan.

**George Haikal:** Stefan. Nice.

**George Haikal:** So before David joins — he's a super nice guy. He's heading up product, or at least high up on the product team, and he came over from Stripe, which is interesting because they're really big and also kind of a competitor to Metronome. So he has some good insights there. What I'm trying to pull out of him is the biggest use cases, what are the biggest problems they're solving for customers, who the super users are, what the most requested features are — pretty basic stuff. Then we'll let him give us a demo and drill down into more specific questions, just flowing naturally as a conversation. I don't want to just pepper them with a ton of hyper-specific questions. It'll be fun.

**David Edoh-Bedi:** Hello, hello.

**George Haikal:** David, how are we?

**David Edoh-Bedi:** I am great.

**George Haikal:** How are you? Good.

**George Haikal:** You're traveling, you said, right?

**David Edoh-Bedi:** Conference time?

**David Edoh-Bedi:** Yeah, I am in Berlin for a conference, for a developer's conference starting tomorrow.

**David Edoh-Bedi:** So, yeah, just trying to get used to the jet lag and time zones and all that stuff.

**George Haikal:** Yeah, what was that?

**George Haikal:** How long was that flight?

**David Edoh-Bedi:** Oh man, I had two layovers. One in Minneapolis, one in Copenhagen, and then here. It was tough leaving Austin because of all the thunderstorms. The epicenter of the floods is not very far from where I live. So I didn't get the worst of it, but it was just kind of rough flying out of there. Yeah, a long few days.

**George Haikal:** As if travel isn't messy enough, you mix in thunderstorms and crazy weather. I can imagine.

**George Haikal:** Well, thanks for jumping on, man. I know we had to move it around a few times, but I really appreciate you meeting with us. This is Nam and Sydney. They're both on the account and they're amazing. So happy they're on the call here too, to meet them. They'll have some great questions for you on the product. The way I was thinking about this, David — let me know what's easier for you. If we can start with a general product demo, and then during it we can just ask questions casually. Maybe a deck? Yeah, that's perfect. And we'll just pepper in our questions as they become relevant. I think that's the best way to do this.

**David Edoh-Bedi:** Yeah, I think so. So I thought it'd be helpful to walk you through how we think about the product, then show you an example in the dashboard, and go from there.

**George Haikal:** Did you make this just for us, July 2025?

**David Edoh-Bedi:** Yeah, I did. It's something I've been working on, so it's the first time I shared externally. Feedback welcome. All right, cool. So yeah, let's start right in.

**David Edoh-Bedi:** So, here's what we're going to do.

**David Edoh-Bedi:** We'll do an overview of the Metronome platform.

**David Edoh-Bedi:** And then I have a fake company that I'm going to use just to help drive the concepts home, hopefully.

**David Edoh-Bedi:** We'll look at the Metronome data model, and then I'll show you a demo in the Metronome platform itself.

**George Haikal:** Sounds great.

**David Edoh-Bedi:** Cool.

**David Edoh-Bedi:** so with that, further ado, so I'm actually going to do the company overview first.

**David Edoh-Bedi:** My fictional company is Vocalist. They're an AI speech platform. Think of them as an Eleven Labs clone. They offer services like voice cloning and text-to-speech. They were originally founded as a subscription-based business, but now they want to add a usage-based component — which is very common for AI companies. Their product offerings are voice cloning and text-to-speech, and data access is important to them. They want to view usage patterns from their customers and iterate on pricing as needed. I wanted to set that up because we're going to keep coming back to it.

**David Edoh-Bedi:** So now let's talk about the Metronome platform itself. At Metronome, billing goes hand in hand with your product. We see billing as being pretty central to your product stack. This flywheel is supposed to represent that. I'll start with launch. Our goal is to help you launch as fast as possible — hours, days — processes that used to take weeks and teams of billing engineers. We really aim to condense that to a much shorter time period. Then there's connecting — billing to your product experience. We don't want them decoupled. We want billing to be central to your product experience. Lastly, we want to enable you to act on usage data as well. So think of this as taking data out of Metronome and building reports to react to customer usage patterns. The example I gave where Vocalist was doing subscriptions and now wants to do usage-based — that's an analogy here where companies tend to react quite a bit to what they see in the market. And of course, this is an iterative process. It's not a one-and-done. We aim to allow you to change pricing and experiment as often and as fast as possible.

**George Haikal:** Amazing. I'm assuming so these are broad categories, so I'm assuming Stripe or these other competitors cover Launch, Connect, and Act. But we're going to go niche and look deep in this product demo to kind of uncover the differentiators, yeah?

**David Edoh-Bedi:** Yeah. Cool. So I'm going to show the capabilities and you can ask questions as you go. This is an architectural overview of Metronome to help you understand how we're built. Core to the architecture is that we're built in a modular pattern with each module serving a very specific function. First is our data platform, which handles all the events. It's high throughput — we handle hundreds of thousands of events a day, I think millions of invoices a month. And it's used by very high-scale, high-compute customers. Some of our key logos are OpenAI, Databricks, and others — very, very high volumes, and we're able to support that without any issues. The second module is the pricing engine, where you define all the primitives for handling pricing. Then there's the customer configuration module — that's where you add all the customer information. And lastly, the whole thing is architected to be real-time. All your events are sent real-time, we process them real-time, you can export them real-time. That's the unifying theme here. The right side of this diagram shows the integrations — invoicing, marketplaces like AWS and Azure, ERPs, accounting. Quite a few integrations, all documented on our website. And data warehouses and big data providers like Databricks. Then the last thing I want to touch on is API and alerts, upper left here. The thing I really want to highlight is the alerts. It's a unique offering and a differentiator. We can alert on basically any field, which enables you to make product decisions. For instance, if you've configured a threshold for a customer's usage and they're reaching that threshold, you could set an alert to enable them to add credits. It's a mechanism for reacting to customer usage. And these modules are architected to decouple, so engineers handling data can work independently of finance handling pricing. That decoupling is very much in the spirit of allowing teams to work independently.

**George Haikal:** Got it. Question for me. Like an hour before this, my account ran out of limits, hit its limit, and I couldn't log back on until 11, and had to go upgrade to max. Is that notification from you all?

**David Edoh-Bedi:** Yeah, if you're using the API, right?

**George Haikal:** Yep.

**David Edoh-Bedi:** Yeah, if you're using the API, that would be us.

**George Haikal:** Cool. Very cool.

**David Edoh-Bedi:** Okay, so now we're talking about the data model. Metronome is core to what we do, so it's important to understand this. These are the building blocks of Metronome. And I'm going to use a restaurant analogy here — I think it makes it easier to internalize. Going left to right, the first building block is what we call billable metrics. That's a consumption unit of measure. So think of a restaurant where you go for lobster and pay by weight. That's the unit of measure. Second are your products — what you sell. Pretty self-explanatory. With the restaurant analogy, that would be your actual dish: steak, salad, or lobster. Then there are rate cards, which is a big differentiator. We centralize all your prices. Think of it as your menu — your menu has all your prices. That's the way we built this. It's really powerful because it allows you to make changes to all customers using that rate card in one location. All at once. If you look at Stripe, they don't support this. Actually, they have two versions of usage-based billing now where they're trying to build a rate card as well. Then the last building block is contracts — the commercial agreement you have with your customers. Monthly, pay-as-you-go, or enterprise. And there's a lot of variety in those. Mapping that to dining arrangements: regular dining is pay-as-you-go, you show up, eat, and leave. Catering is akin to an enterprise agreement. And you can have custom contracts — catering a private event, for instance. Hopefully that analogy helps clarify the building blocks of Metronome.

**George Haikal:** Definitely.

**David Edoh-Bedi:** Okay, so next thing I wanted to cover is to map all those components to how they would look in Vocalist. We'll go top down. Usage events are what you actually send to the platform. I'll show you an example in a second. Billable metrics, as we apply them to Vocalist, is how much AI voice is used. That's your consumption unit of measure. Products are AI voice standard, AI voice premium, and voice cloning. And rate cards are your menu of products or prices. And then contracts are the agreements you have with your users.

**David Edoh-Bedi:** Excuse me for one second.

**George Haikal:** No problem. I'm going to get a drink of water.

**David Edoh-Bedi:** How do I pause this?

**George Haikal:** The meeting controls.

**David Edoh-Bedi:** All right, sorry about that. No problem. Sometimes I get dehydrated with all these time zone changes.

**David Edoh-Bedi:** All right, so here is an example of a usage event. This is what you would send to Metronome. This is how we track what your customers are actually doing. They follow a very specific schema. Event types are required, and then you can send custom tools in the properties. I'll show an example in a second. So yeah, that's it for my slide deck. I'm going to shift to showing you the actual dashboard.

**George Haikal:** Sweet. Thanks, that helps clarify things.

**David Edoh-Bedi:** Yeah, of course.

**David Edoh-Bedi:** Let just make sure I log in.

**David Edoh-Bedi:** Okay, cool. So this is the Metronome dashboard. Have any of you seen this?

**George Haikal:** No.

**David Edoh-Bedi:** Cool. Just real quick, there are two configurations to our platform — production and sandbox. I'm going into sandbox. In the menu, you have different sections with all the primitives you need when you interact with the platform. We're mainly going to be in the offerings today. And if you look here, these are the building blocks we were just talking about. I'll start with the billable metrics and show you the event type at the end. So billable metrics is your unit of consumption. And if you recall, for Vocalist, they had voice cloning, standard voice generation, and premium voice generation.

**David Edoh-Bedi:** So we're going to create a premium voice generation. There's no billable metric for that, so I'm going to duplicate voice because they're pretty similar and rename it to premium. Billable metrics are a unit of consumption, and the way they work is they basically filter all your events that come in. You can define two types of filters: basic, which is simple and straightforward, or SQL, where you can do more manipulations on the data. Let's say you're a service provider that does AWS and you want to charge not just based on region, but configuration with a group key of region, hardware, et cetera. You can have a SQL statement to configure that on your event. We're just going to look at basic filters today. The event type is voice generation. Let me go back real quick and show that in the deck. So yes, the event type — we saw there's a voice generation property.

**George Haikal:** Got it. Yep.

**David Edoh-Bedi:** So what you're doing is — Vocalist is sending all these events to Metronome, and as they come in, we're going to filter on voice generation and look for the voice type property. So we're going to look for voice type property and make sure those are premium. We also want to make sure there's a duration in the event, otherwise it's useless. If we don't have duration, we can't calculate the consumption, can't charge the user. So we want to make sure that exists. And all we're doing is summing the duration. So I'm going to save this. And now we have our billable metric.

**David Edoh-Bedi:** Okay. So if you recall, now we need a product. We'll generate a product using that little metric that we just defined — premium voice generation. We're not going to do any tags today, there's so much I could show you, but tags allow you to take actions on a product or a group of products. So imagine if you want to apply a discount — you could tag all the premium voice as "15% discount this month." It's a usage type of product, and I'm going to link it to the premium voice generation metric. And again, you get a sense of how easy it is to create these primitives in Metronome. Then let's create a rate card, which is your menu of prices. We're going to select these products and define pricing. I'm going to keep it simple — let's say it's a fixed amount. Yeah, you can get pretty fancy with this and add tiers. So if you want to charge three cents for the first thousand seconds, you can. We'll keep it simple for now. So that's it. We've defined a rate card that all customers on Vocalist can now have applied. And anytime we make a change to this, it gets propagated.

**George Haikal:** Nice. What's the favorite feature of your super users?

**David Edoh-Bedi:** I would say the rate card is very useful. We hear good things about the alerting mechanism as well, but rate card is a big differentiator because it really simplifies how you update pricing. You can experiment with pricing just by updating the rate card.

**Nemanja Simic:** That's powerful. So can you outline what the problem was before or if somebody doesn't have the rate card? Just a little bit more detail.

**David Edoh-Bedi:** Sure. We used to have plans. And if you look at plans, I mentioned earlier that Stripe has two offerings for usage-based billing. They had their old offering products and prices. Now they're implementing rate cards as well. The problem with our old plans and with Stripe's products and prices offering is you're essentially tying a customer to an individual record. So anytime you wanted to update a price, you would have to do it per customer. It's much more tedious and a lot more upkeep — error-prone than just having a centralized place where all the customer contracts are drawing from. So anytime you want to change pricing for your customers, you just do it in one place. That's the key difference.

**Nemanja Simic:** Okay. So before, to go back to that restaurant analogy, you would have to change the menu for each customer. Now you could just change the centralized menu that they're picking from.

**David Edoh-Bedi:** That's right. Yes, yep.

**George Haikal:** Who's the segment of super users that, if you got 100 or 1,000 more of them, you'd be over the moon about?

**David Edoh-Bedi:** I mentioned OpenAI, Databricks, and Anthropic earlier. Those are our marquee customers. We have Confluent as well. And we're pretty excited about some of our newer AI companies like Replicate and Flyer.io. The ones we talk about a lot — if you want to talk about scale — are OpenAI, Anthropic, Confluent, and Databricks. We have case studies I can share with you on how they use us and what they're doing.

**George Haikal:** Yeah, because kind of what I'm getting at — there's ideal users, right? But sometimes the companies have very different profiles. OpenAI is much different than a 20-person startup. And you could be solving slightly different problems for each. So us being able to dig into the nuance, the case studies, and the problems you're actually solving can help on the content side — who we're trying to write for and what we're writing about.

**David Edoh-Bedi:** Absolutely. Cool.

**David Edoh-Bedi:** I know we're almost at time, so I'll just real quick show you the last step here. We've defined the rate card, and now we're going to assign a contract to a user. As I mentioned, we assign them a rate card — the one we just created. There are a lot of things you can do. Let's say you want to give credit. You can say, okay, you just joined, I want to give you $10 in credit that will expire after a month. And the priority sets the order in which things get applied if you have a lot of credits and commitments. But you can apply credit. The credit will show up on your invoice as a negative value, and as you consume the services, it would be used up. So we're creating a very basic contract. I'm just going to create it. And you'll see that there's an invoice that gets generated pretty much right away. There's no usage yet, so the $10 credit would show up here.

**David Edoh-Bedi:** And real quick, it's going to simulate usage. I'm going to send a matching event for standard. You can see the example of the event payload here — voice type standard, the duration. I'll also send a voice cloning matching event. This is great because you can test within the dashboard without having to send actual API calls. And then if I go back to my customer, I'll see the usage events. Oh, that's premium voice. What happened? Something went wrong. Let me look at my contract again. Oh, okay. I see what happened. My contract — I sent the events before my contract actually started. So let's try that again. Okay, created at July 11th. Let's do that as well. Premium. Okay. So now it should show up. Still nothing. Okay. That's good.

**George Haikal:** No problem. I think we got the gist of it.

**David Edoh-Bedi:** Yeah. But anyway, that's the gist of it. Of course, it's going to show up in my invoice as usage. So yeah, I wanted to show you how things work. I think that's always helpful. I know you had other questions around our competitors and PLG versus SLG. I thought maybe we can schedule another call to cover that because 30 minutes is not a lot of time to cover these things. So if that sounds good, we can proceed that way.

**George Haikal:** Yeah, thanks for sharing those questions. I'll address some of them directly in the document too. So when we have the follow-up call, we can just talk about any remaining questions. No problem. I know we're jumping around a lot. Do you have a better time that works for you? I'm assuming you're at the conference through the end of the week, but next week, you have a time that works?

**David Edoh-Bedi:** Yeah, would a week from today work? That would be next Wednesday the 16th?

**George Haikal:** Yeah, same time?

**David Edoh-Bedi:** Let's do later in the day if that's okay. How about 2pm Pacific?

**George Haikal:** Does that work with you all, Sydney and Nemanja?

**Nemanja Simic:** Yeah, it's open for me.

**George Haikal:** Cool. Let's do it. I think 30 minutes will be enough if we just run through those questions. If we add stuff to the agenda, then I'll increase the time limit. You've been jumping around, David, so it was good for us to get into the product. It's pretty refreshing how simple it is.

**David Edoh-Bedi:** Yeah, I mean, of course, everything I showed you can also do through the API, but obviously I think it's easier to illustrate looking at the UI. So yeah, please feel free to Slack me if you have questions. And yeah, hopefully this was helpful.

**George Haikal:** Yeah, in the meantime, if you can send over any case studies or anything deeper about the customers or usage metrics or anything like that, we'd love to take it all in, ingest it, and have it inform our strategy.

**David Edoh-Bedi:** Okay, sounds good. And then what are the next steps? When do you think you'll actually start creating content?

**George Haikal:** Yeah, so we're in the weeds on this. The short answer is as soon as possible. There's two different lanes — the content strategy and editorial, and then there's the white paper. We're working on both simultaneously, but hopefully by end of week, we'll have more clarity on our pitch — what we want to do by when and where we want to go by end of sprint. Friday, we should have more clarity on the actual plan and what we're doing to execute. But in the meantime, we've generated and sent over a ton of documents that are pending review from your team. On our side, we have all the artifacts we're going to use to get the content right — the style and tone, competitor analysis. So we've been working in the background and we'll get to production as soon as we get sign-off on those artifacts and then send over a publication calibration as well.

**Nemanja Simic:** To add to that, we also provided the first iteration of the content strategy on the editorial side. And right after this call, we're going to get something put together for the white paper side as well. So all that is pending review.

**David Edoh-Bedi:** Cool. Yeah, I'll catch up on what's going on. I missed a bunch of messages over the last couple of days. And yeah, we'll chat next week. I'll just answer your questions directly in that Notion and tag you. If you have any questions, just tag me or message me.

**George Haikal:** Appreciate it. Async works. If anything's too specific questions-wise, you can keep the answer general. And then we'll ping you or re-dig in if we need more.

**David Edoh-Bedi:** Sounds good.

**George Haikal:** Thanks, David. Enjoy Berlin.

**David Edoh-Bedi:** Yeah, we'll do. See you.
