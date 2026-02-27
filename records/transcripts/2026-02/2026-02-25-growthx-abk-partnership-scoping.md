# GrowthX <> ABK - Partnership Scoping

<metadata>
date: 2026-02-25
time: 22:00 UTC
duration: 43 minutes
organizer: marcel@growthxlabs.com
participants: Marcel Santilli, Tyler Pavlas, Alexander Kehaya, Pontus Andersson
fireflies_id: 01KJ5HCT0YXXBPJ3RGTW4JBXZZ
transcript_url: https://app.fireflies.ai/view/01KJ5HCT0YXXBPJ3RGTW4JBXZZ
</metadata>

---

## Summary

The team is developing an agentic commerce platform designed for enterprise use, integrating governance, security, and payment capabilities to facilitate agent transactions. Current market activity is limited but there's potential for growth as enterprises begin deploying multiple agents. The company plans to generate initial revenue through design partnerships while transitioning to product monetization as adoption increases, emphasizing workflows as code and partial automation with human involvement.

---

## Action Items

**Alexander Kehaya**
- Follow up via email to schedule Marcel Santilli's appearance on the Index Podcast
- Explore attending Marcel's CEO OS workshop on March 20 and consider collaboration for a joint workshop
- Coordinate internally with CTO Alexander to clarify technical details of runtime and Interchange platform

**Marcel Santilli**
- Send Alexander and team a link and potentially a free code to AI growth workshops previously hosted
- Share details on upcoming March 20 CEO OS workshop and support potential joint workshop development
- Provide documentation and assist in exploring use cases and co-creating content/workshops for go-to-market validation and distribution

**Tyler Pavlas**
- Participate in follow-up discussions to develop workshop and podcast content with Alexander and Marcel

**Pontus Andersson**
- Support Alexander on internal integration and dogfooding of Interchange and coordination with external partners

---

## Transcript

**Tyler Pavlas:** I can't even use the kid excuse myself. So every time someone reminds me that they're also taking care of kiddos like Marcel with his 2 year old, it always is a good reality check that I need to stop complaining.

**Marcel Santilli:** Yep.

**Tyler Pavlas:** Thanks for bringing the recorders in. I think that'll be good context for us to have. And before Marcel gets here, would love maybe a quick intro from you, Pontus, for context on my side. I'm the founding AE at GrowthX and I work really closely with our CEO Marcel.

**Pontus Andersson:** Rock on.

**Tyler Pavlas:** Yeah, so Pontus been working with Alex and the rest of the gang over at ABK for quite a while. History goes back I think like almost five years this year, which is fun and lead kind of all the operations go to market and some strategy stuff here on a day to day basis for ABK.

**Alexander Kehaya:** Yeah, I mean that's kind of what we want to talk about here. We've got some stuff that I think is relevant to what you guys have already probably built in house. It's called Interchange, but it's that governance, policy, orchestration, security auditing layer that we think ties directly into the economic side where agents are starting to transact with each other and buy things online. That's been kind of where we started with payment rails, but we think this other aspect is needed to make this all get adoption at Enterprise.

**Marcel Santilli:** Can you guys hear me okay?

**Alexander Kehaya:** Yeah, I can hear you fine. Good to see you. I think we talked like a year or two ago, I can't remember, but through Peter Griggs.

**Marcel Santilli:** Yeah, yeah, I remember. He connected us and now he's in the Bay Area. But I've been meaning to catch up with him.

**Alexander Kehaya:** Yeah, he and I have been talking a lot lately. You know, I think you probably remember we kind of cut our teeth together as entrepreneurs at this place called Opus Logica in Santa Barbara, which my business partner was the original founder of that Brian Fox. And Brian's story goes way back to, like, the beginning of the Internet. He was one of the few people between MIT's AI lab, Carnegie Mellon, and Stanford University that started the open source movement. Like, he wrote Bash back in the day, authored the GPL licenses.

**Marcel Santilli:** That's awesome.

**Alexander Kehaya:** Really cool guy. I met him through a friend. I was looking at an AI company like, 15 years ago to invest in, and I didn't know anything about AI. I was just teaching myself how to write software, learning online, how to write code. And I met a guy at some random meetup, and I was like, I need somebody who knows about AI. This guy's name was Steve Bell. Steve was like, you should meet Brian. So I met Brian for coffee. And I was just a solo entrepreneur, literally, like, working out of coffee shops, barely making ends meet, bootstrapping my SaaS business. And Brian kind of took me under his wing.

**Tyler Pavlas:** Are you sure?

**Alexander Kehaya:** And we've been partners basically ever since. But that's how I met Griggs, because he and I were both kind of entrepreneurs and we were hacking together that whole time.

**Marcel Santilli:** Yeah, there's people like Griggs that are just meant to be entrepreneurs forever, you know?

**Alexander Kehaya:** Yeah.

**Alexander Kehaya:** Yeah, but that's awesome. Well, great. Great to reconnect or chat live. Tyler, I don't know, sorry to join a minute or so late. Did you do intros yet or...

**Alexander Kehaya:** Yeah, we did a quick round. Pontus is my chief of staff. We've been working together across multiple companies now for about five years. We started our company ABK like two years ago. I was an early employee at Solana Labs and then the Solana Foundation. I was one of the first people to transition over when they started that. I've been in crypto mostly since 2016. I have a podcast called the Index Podcast where we talk about the future of the Internet. We'd love to have you on at some point. We cover everything AI to crypto. I've got about 120,000 subs on YouTube.

**Alexander Kehaya:** This is important because on my show about a year ago last April, the head of developer relations at Coinbase came on my show and told me about this thing called HTTP 402 that they were launching. No one had heard about it really yet. Essentially it's payments over HTTP. 402 is a response code for payment required. Back when Tim Berners Lee invented HTTP, they thought maybe people want to make payments server to server, we should have a response code for this. But at the time they had no technology to do that. Well, blockchain technology happens to be a perfect way to facilitate this.

**Tyler Pavlas:** So this is HTTP 402, the standard?

**Alexander Kehaya:** Right. So Coinbase acquired Earn.com, which my friend Lily ran and turned around with Balaji, and she actually was looking at 402 and that idea got absorbed into Coinbase. And then somebody picked up the ball finally like last year, and they made an open source specification for it.

**Marcel Santilli:** So what's the vision for this?

**Alexander Kehaya:** So the vision is that agents can now pay each other to use tools and services. If you have multiple agents working within an enterprise, they can discover new APIs and services, and instead of having a human approve and manage every interaction, agents can autonomously transact with each other. And the governance and security layer that Pontus and I are building is what manages this.

**Marcel Santilli:** That's fascinating. So you're essentially building the operating system for agent commerce?

**Alexander Kehaya:** Exactly. We call it the Interchange. It's modular, open-source, and chain-agnostic. The idea is enterprises adopt it as the orchestration layer for their agent teams.

**Marcel Santilli:** I love this. It aligns with what we've been thinking about workflows as code and runtime infrastructure. In my work with agents, I've found that full autonomy without guardrails is dangerous. You need policy enforcement, identity, auditing. It sounds like that's what you're building.

**Alexander Kehaya:** Absolutely. That's the core. And we're currently dogfooding internally to validate use cases.

**Marcel Santilli:** How far along are you in the product?

**Alexander Kehaya:** We're in prototype stage. Limited multi-agent orchestration so far. But we're seeing real value in simple agent "skills" for CEO-level productivity improvements. The long-term vision is enterprises running teams of agents that automate complex workflows.

**Tyler Pavlas:** What's the go-to-market strategy?

**Alexander Kehaya:** We're starting with design partners who can use Interchange internally to solve enterprise workflow problems. This validates product-market fit and builds credibility through real customer success. Eventually we transition to product monetization through agent wallet transactions and API marketplace access.

**Marcel Santilli:** That's a solid approach. I'd actually recommend adding workshops to that mix. Based on my experience at Scale AI and HashiCorp, workshops are a powerful way to validate demand, build community, and generate early revenue before scaling SaaS.

**Alexander Kehaya:** I like that. We could do paid workshops to introduce the platform and build early adopters.

**Marcel Santilli:** Exactly. And it gives you a distribution channel to reach enterprises interested in agent workflows. I'm actually hosting a CEO OS workshop on March 20 that's been really successful. You should come check it out.

**Alexander Kehaya:** Absolutely. I'd love to attend and explore doing a joint workshop with you.

**Marcel Santilli:** I think there's real synergy here. Your podcast plus my workshop platform could reach a lot of people interested in this space.

**Alexander Kehaya:** Yeah, we'd definitely love to have you on the Index Podcast to talk about agent workflows and AI-driven go-to-market.

**Tyler Pavlas:** That sounds great. This could be a real partnership.

**Marcel Santilli:** I'm going to send you some resources on the workshops. And maybe we can dive deeper on use cases next week.

**Alexander Kehaya:** Perfect. I'll follow up with you on scheduling the podcast appearance too.

**Pontus Andersson:** And from our side, we'll get our engineering team to clarify some technical details on the Interchange runtime that might be relevant to your framework.

**Marcel Santilli:** That would be great. I think there's real opportunity here to collaborate and advance the space.

**Alexander Kehaya:** Agreed. Let's stay in touch and keep this momentum going.

**Tyler Pavlas:** Thanks so much for the conversation. This has been really valuable.

**Pontus Andersson:** Yeah, excited about the possibilities.

**Marcel Santilli:** Me too. Talk soon, everyone.
