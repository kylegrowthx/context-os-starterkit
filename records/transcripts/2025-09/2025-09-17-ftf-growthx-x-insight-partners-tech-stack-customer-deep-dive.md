# [FTF] GrowthX x Insight Partners — Tech Stack & Customer Deep Dive

<metadata>
date: 2025-09-17
time: 21:04 UTC
duration: 54 minutes
organizer: Marcel Santilli
participants: Julia Baldini, Richard Matus, Alexander Leibowitz, Daniel Lopes, Marcel Santilli
fathom_recording_id: 88040114
fathom_url: https://fathom.video/calls/414505728
share_url: https://fathom.video/share/wCoYfHq8F_Ky6bodGTozRMteSVd-XmN9
source: fathom
enriched_on: 2026-03-03 14:32 UTC
speaker_note: "Board Room" device label matched to Julia Baldini (Insight Partners) based on contextual references to enrolling Alex onto the team and work at Insight Partners.
</metadata>

---

## Summary

Marcel Santilli and Daniel Lopes (Co-Founder, Product) presented GrowthX's AI-powered content marketing platform and tech stack to Insight Partners partners Julia Baldini, Richard Matus, and Alexander Leibowitz. GrowthX has achieved strong traction with 10 deals closed and ~$2M in net new revenue, built a scalable hybrid model combining AI workflows with expert delivery, and is being selective about capital to maintain quality. Insight Partners recognized alignment with their investment thesis on tech-enabled services businesses that disrupt traditional industries, with potential portfolio company introductions (Augment, Airbyte, SKU.AI) and discussions around deeper partnership.

---

## Context

GrowthX is a ~12-month-old venture-backed B2B services company founded by Marcel Santilli that combines AI technology with expert human delivery to provide high-quality content marketing at scale. The company raised a Series A in March 2025 and has attracted operators from leading companies (Intercom, Coinbase, Stripe). Insight Partners is a growth-focused venture firm with a dedicated tech-enabled services practice led by Julia Baldini (and including Richard Matus and Alexander Leibowitz). This meeting occurred as part of Insight's investment evaluation process, with the goal of understanding GrowthX's business model, technology architecture, customer approach, and fit with their investment thesis around technology-disrupted professional services.

---

## Relevance

**To GrowthX Business Development:**
- Potential partnership/investment opportunity with Insight Partners, a growth-oriented VC with deep conviction around tech-enabled services
- Strong investor interest in GrowthX's hybrid model (AI + expert services) as validation of market opportunity
- Possible introductions to portfolio companies (Augment, Airbyte, SKU.AI) for partnership or go-to-market collaboration
- Insight Partners' 7 investments in 18 months across construction, security, data services validates GrowthX's potential to expand beyond content marketing
- Julia Baldini's conviction about TAM (budget, decision-making quantity) and ability to scale beyond traditional services constraints highly relevant to GrowthX's expansion strategy

**To GrowthX Delivery & Product:**
- Confirmed market validation of services + software hybrid model as critical to building TAM and attracting capital
- Explicit acknowledgment that tech-enabled services scale differently than pure SaaS (lumpier revenue, longer annual planning cycles) — important for unit economics and investor expectations
- Opportunity to optimize delivery engine for portfolio company integration if partnership moves forward
- Reinforcement that brand and team composition (ex-Intercom, Coinbase, Stripe talent) is a key differentiator

**To CheckThat:**
- Implicit validation of AI visibility/visibility products as ancillary revenue in tech-enabled services model
- CheckThat mentioned as example of productization potential within broader services business

---

## Overview

- GrowthX has built an AI-powered content marketing platform combining expert knowledge, context, and workflows to deliver high-quality outputs at scale
- The company is seeing strong traction (10 deals closed this month, \~$2M in net new revenue) but being cautious about scaling too quickly to maintain quality
- GrowthX's tech has broad potential beyond content marketing, but they're staying focused on that vertical for now
- Insight Partners sees alignment with their thesis on tech-enabled services businesses disrupting traditional services industries

---

## Key Topics

### Insight Partners' Investment Thesis

  - Focus on growth-oriented companies leveraging technology to disrupt traditional services industries
  - Looking for businesses that can scale more effectively than typical services companies
  - Have made \~7 investments in 18 months across diverse areas (security, construction, data services, etc.)

### GrowthX's Business Model & Approach

  - Combines AI technology with human expertise to deliver high-quality content marketing at scale
  - 8-week initial strategy sprint to calibrate and set up workflows, then ongoing execution
  - Pricing based on "lanes" or workstreams (e.g. organic growth, newsletter, sales enablement)
  - Currently focused on tech/software companies but see potential to expand to other verticals

### GrowthX's Technology Platform

  - Custom-built AI workflow engine and framework optimized for content marketing tasks
  - Integrates context, knowledge bases, and reusable workflow components
  - Combines multiple AI services (e.g. Claude, Anthropic, Perplexity) based on task requirements
  - Built-in tracing, evolving, and error handling capabilities

### Market Opportunity & Growth

  - Content marketing seen as foundational to broader marketing/knowledge work
  - Strong customer demand - not constrained by leads, focused on scaling quality
  - Potential to expand into additional marketing functions over time
  - Exploring productized offerings like CheckThat.ai for AI visibility

### Team & Funding

  - Founded \~12 months ago, raised Series A in March
  - Attracting top talent from companies like Intercom, Coinbase, Stripe
  - Capital efficient but considering additional funding to accelerate growth
  - Being selective about investors who understand the model

---

## Action Items

**Julia Baldini (Insight Partners)**
- Review GrowthX data room + deck
- Provide partnership feedback next week
- Introduce GrowthX to Insight Partners marketing team (Joey/Matthew Panzerino at TechCrunch)
- Consider introductions to portfolio companies: Augment, Airbyte, SKU.AI

**Daniel Lopes (GrowthX)**
- Attend breakfast meeting with Insight Partners
- Prepare for potential tech deep-dive discussion

---

## Transcript
**Julia Baldini:** Hey, can you hear us?

**Daniel Lopes:** Hey, yeah, can you hear me?

**Julia Baldini:** Yeah, yeah.

**Julia Baldini:** How's it going?

**Daniel Lopes:** Good.

**Daniel Lopes:** Sorry, guys.

**Daniel Lopes:** Sorry to not be in person today.

**Daniel Lopes:** I had a little bit of an unplanned scheduled this week.

**Daniel Lopes:** My wife had surgery this morning, so I have to be babysitting her here.

**Julia Baldini:** You're all good.

**Julia Baldini:** We think you've prioritized well.

**Julia Baldini:** not that hard to find, but it's good to see you.

**Julia Baldini:** Good to see you again.

**Daniel Lopes:** Nice to meet you.

**Julia Baldini:** Good to meet you for the first time.

**Julia Baldini:** Richard, I work with Alex closely.

**Julia Baldini:** Yeah, yeah.

**Julia Baldini:** I know today we were thinking maybe we could do a deep dive, also happy to whatever you think would be most helpful.

**Julia Baldini:** deck and a little bit of our conversation, Richard.

**Julia Baldini:** Maybe we could do a 10-minute overview of just kind of what growth is.

**Julia Baldini:** Yeah.

**Julia Baldini:** To make sure he's up to speed.

**Julia Baldini:** Than everything

**Julia Baldini:** We'd love to kind of do a deep dive on kind of customers, what you're doing for them, and let you guys kind of take the conversation to what you think we should know.

**Julia Baldini:** Yeah, that's perfect.

**Julia Baldini:** Yeah, that sounds great.

**Julia Baldini:** Ask me questions if I cover the wrong stuff, but Richard Mantu's been inside about five years, started working across all sorts of parts of our business, where the two things that have never changed on the inside is the focus on growth and the focus on technology.

**Julia Baldini:** And so we worked across kind of the bio part of our business, but also the early stage venture part of our business.

**Julia Baldini:** A couple of years ago, we kind of stared at the impact that ChatGPT woke us up to, that AI can have in a bunch of industries, and our founder, Jeff Horing, was sort of ripping the idea, like, wow, there could be other ways to invest around traditional services industries where you can go be the disruptor or the non-SaaS business model.

**Julia Baldini:** Like, there's all these different barriers to self-adoption, which are the reason why technology hasn't eaten up more of, kind of the broader, say, professional services and labor market.

**Julia Baldini:** Now you have an opportunity to solve that kind of onboarding problem or find different ways or meet the customer where they're at.

**Julia Baldini:** On their existing buying behavior, but driving technology into what you do to build what traditionally would have been the criticisms of a service and business, which is really hard to scale.

**Julia Baldini:** Which, by the way, I sort of disagree with Cognizant, that's pretty big.

**Julia Baldini:** But people would say, really hard to scale, it's going to be harder for you to move up those milestones, et Now it can be easier.

**Julia Baldini:** So before I worked at Insight and focused on growth and technology, I used to work with really traditional businesses.

**Julia Baldini:** Like, I was the board observer over at Lobster and learned the dark magic that Golden Gate Capital just down the street used to get a 70% IRR before they went bankrupt.

**Julia Baldini:** So I was like, okay, cool trick to learn from those guys.

**Julia Baldini:** It's necessarily my passion of how I want to invest.

**Julia Baldini:** Like, I'd much rather be growth-oriented, so that's why I shifted.

**Julia Baldini:** But I had experience looking at a lot of these services businesses, so I sort of raised my hand to Jeff and said, I'd love to leave this practice for us.

**Julia Baldini:** So I enrolled folks like Alex on the team.

**Julia Baldini:** We report directly to Jeff, the founder of Insight.

**Julia Baldini:** We're now one of the most active teams at Insight because we're finding this to be a really deep and opportunity-rich market.

**Julia Baldini:** We've done about seven investments in 18 months.

**Julia Baldini:** But it's really broad and diverse.

**Julia Baldini:** it's like everything from robot docs to patrol perimeters to managed physical security, all the way to data managed services for enterprises, all the way to accelerated construction permitting.

**Julia Baldini:** So just the facts.

**Julia Baldini:** That's cool.

**Julia Baldini:** It's a quick version.

**Julia Baldini:** But ask me if you have more questions.

**Julia Baldini:** We're going to open book.

**Julia Baldini:** Yeah.

**Julia Baldini:** I guess I'm really curious because it's so fascinating to do, especially people get it earlier than it becomes cool to get it, which is awesome.

**Julia Baldini:** It's like how many VCs write a certain word and that eventually becomes a theme for...

**Julia Baldini:** Well, we also did this thing where we started doing a tour where we go do a trip somewhere, like a set for whatever.

**Julia Baldini:** We go start reaching out to people who wrote blog posts about services.

**Julia Baldini:** We haven't written them, actually.

**Julia Baldini:** Yeah.

**Julia Baldini:** And then you realize, like, some of them, unfortunately, there really is no depth behind it.

**Julia Baldini:** They're just like, yeah, I wrote a blog.

**Julia Baldini:** I might do one deal.

**Julia Baldini:** I'm going to move on to the next thing.

**Julia Baldini:** we were like...

**Julia Baldini:** Oh, we're thinking about it totally differently.

**Julia Baldini:** We think this is like an enormous wave of pretty competitive.

**Julia Baldini:** We do have other folks, of course.

**Julia Baldini:** I have friends that other funds are one of these types of investments as well.

**Julia Baldini:** And like, so what I'm really curious, and I promise I won't ask you a bunch of questions.

**Julia Baldini:** It's just like, from before you did your first investment in some of these businesses to now, like, has there been any like, whoa, I didn't realize this?

**Julia Baldini:** Good or bad, you know?

**Julia Baldini:** Like, I'm just curious.

**Julia Baldini:** Okay, here's actually, we've been noodling on this recently.

**Julia Baldini:** When you go by a reasonably mature, meaning like over 20, 30 million ARR software business, and we invest in one of those, they deliver net new ARR, like it's a metronome, every single quarter.

**Julia Baldini:** And that often isn't true of both software businesses at the 4 to 5 million ARR phase, but also isn't true of tech-enabled services businesses in many cases.

**Julia Baldini:** Like, then that new momentum.

**Julia Baldini:** can be a little bit lumpier.

**Julia Baldini:** That's kind of in weeds, but that's been one observation we've sort of had.

**Julia Baldini:** But I personally sort of don't care because I'll take more than a quarter view and say, okay, as long as you're making the right progress against these milestones on an annual basis, that's the way to do it.

**Julia Baldini:** That's one.

**Julia Baldini:** Two, we found actually one thing we've said to every single tech and able services business we've partnered with is we're doing this because you're tech and able services.

**Julia Baldini:** We're not saying shut it down and become SaaS.

**Julia Baldini:** That defeats the whole point of where we think the market is, which other people may have, but we don't think that'll necessarily work.

**Julia Baldini:** We're kind of noodling with and a little bit pleasantly surprised with the fact that actually packaging a lot of IP up and selling it kind of like error-based software as a portion of the business can drive a lot of embedded value.

**Julia Baldini:** And we're starting to see early days versions of that actually working pretty well.

**Julia Baldini:** But I think we didn't come in saying we have to do that.

**Daniel Lopes:** We've said like, talk to customers.

**Julia Baldini:** Customers tried stuff with customers and got pulled into doing that, which we're like, well, that's actually kind of cool because now you can kind of delight all sorts of different investors.

**Julia Baldini:** you think about a longer time horizon for an exit, you're sort of like, well, we actually have real software too, but we have this, which pulls into all sorts of, you know, technical services, so on and so forth.

**Julia Baldini:** that's been, those have been kind of a couple of things, but I think that maybe the third is you get way bigger TAMs.

**Julia Baldini:** Like actually, I was just talking to someone.

**Julia Baldini:** We have one software business.

**Julia Baldini:** These things happen.

**Julia Baldini:** Like for a couple of quarters, they've sort of stalled in the marketing space.

**Julia Baldini:** I've all anonymized now who it is.

**Julia Baldini:** But, and they're actually like, they have a really smart executive on their team that's like, man, maybe we should enter the services adjacent market of what we do, because that's a way to go pick up bigger budget and go drive us through like kind of this like slower growth hump.

**Julia Baldini:** And I think that that also is a very interesting observation.

**Julia Baldini:** Like these TAMs are probably larger.

**Julia Baldini:** They could go attack in the budgets and the number of like decision at-bats you get is probably larger.

**Julia Baldini:** Yeah.

**Julia Baldini:** Yeah.

**Julia Baldini:** We have a lot.

**Julia Baldini:** Those are just like three things for the last six months we sort of started to learn and see and have other examples of.

**Julia Baldini:** And it's also a bit of a network.

**Julia Baldini:** Like a few of our CEOs are actually, we're hosting this like CEO event in Montauk right now across a lot of our portfolio companies, but we have a whole bunch of ours that are there right now.

**Julia Baldini:** And it's like fun to watch them like take, send me selfies of like them together.

**Julia Baldini:** I'm like, oh, you guys are probably comparing notes.

**Julia Baldini:** Yeah.

**Julia Baldini:** Yeah.

**Julia Baldini:** It's funny because like, um, we had a lot of some, yeah, like a lot of the insights, like, and it's, it's kind of like some of the trends we're also seeing, like founders and friends that are like, you know, I'm going to start doing this because we got stuck over here.

**Daniel Lopes:** Some of the stuff you said is just like something that we actually like went through ourselves.

**Daniel Lopes:** Like, at one point, like a few months ago, decided, okay, like we actually have to figure out the services process as much as we have to figure out the PMF of the SaaS.

**Daniel Lopes:** You know, you have to do both in parallel.

**Daniel Lopes:** So sometimes you have to pause to figure out how to recruit for the service and how to train them so they do the onboarding correctly on the new system and then vice versa.

**Daniel Lopes:** So it's like you're solving two things at once.

**Daniel Lopes:** So it's the revenue.

**Daniel Lopes:** It's not the traditional SaaS that goes like this.

**Daniel Lopes:** Like if you pause sales a little bit and then it's like what's just happened to us.

**Daniel Lopes:** Because you keep you going like less.

**Julia Baldini:** Like we did one portfolio company where they like are like really rockstar like services operators.

**Julia Baldini:** So like actually an interesting lever we're pulling with them is we're finding people who have really innovative like service offerings and IP offerings or like software offerings.

**Julia Baldini:** can plug in to the platform because there can be some really good entrepreneur that just can't scale past like 10, employees.

**Julia Baldini:** And so it's like, oh, okay, what you're doing is really cool.

**Julia Baldini:** We love it.

**Julia Baldini:** We can sell you on being part of something bigger.

**Julia Baldini:** It's a mutual win-win.

**Julia Baldini:** But the thing that our team has already figured out is like how to scale a service delivery engine, plug into existing distribution service delivery.

**Julia Baldini:** And so like that.

**Julia Baldini:** It's kind of like a solved problem with at least one of our core programs, right?

**Julia Baldini:** We have others that are like kind of the far opposite where they're like very software IP driven and like we'll figure out the marketing funnel and how to get them more at that.

**Julia Baldini:** anyway, like this will be heard out on my new order because we're like worse if someone doesn't give me any customer feedback, we and all of the resources and elements that kind of can't help.

**Julia Baldini:** Like that's like the most important thing.

**Julia Baldini:** But if we start getting invited into like any sort of troubleshooting along the way, it's like, oh, yeah, we can like find you executives that have dealt with exactly that or could plug in or could like pinch hit for something.

**Julia Baldini:** Yeah.

**Julia Baldini:** And like the nerdy line on like how to help businesses grow up and like how to scale.

**Julia Baldini:** That's like what we want.

**Julia Baldini:** And I think like honestly, just to jump in and like give you maybe a little bit of context too.

**Julia Baldini:** And then like the way kind of we've seen in talking to investors too recently is like we are, I think most investors are not ready for this model and they don't understand how much bigger the TAM is.

**Julia Baldini:** Yeah.

**Julia Baldini:** Like they think they do.

**Julia Baldini:** But then they're, like, trying to find reasons to confirm their doubts, you know?

**Julia Baldini:** And I think it's, like, just because we've talked to so many people and we've, like, worked so closely with so many customers, like, our conviction is, like, really, really high.

**Julia Baldini:** And it's, like, I can feel your conviction is really high, too.

**Julia Baldini:** And it's just, like, and I think you can't teach that, you know?

**Julia Baldini:** Let's just sort of show their hand when, like, they get shown businesses side by side.

**Julia Baldini:** And, like, a lot of times they go for the, like, smaller revenue, fewer proof points.

**Julia Baldini:** But it's agentic AI.

**Julia Baldini:** you're, like, right.

**Julia Baldini:** But it was, like, really brittle.

**Julia Baldini:** But no one is using it, that good?

**Julia Baldini:** Like, I don't know.

**Julia Baldini:** Like, I'd much rather just be in the door and then go figure out what that agentic AI version of this is, right?

**Julia Baldini:** Like, that's exactly it.

**Julia Baldini:** And I think, like, the way...

**Julia Baldini:** Yeah, you're really...

**Julia Baldini:** And, like, the way, like, we kind of build the team and just to kind of talk about it on a high level, too, it's, like, a lot of operators, ex-CTOs, like, people that are, like...

**Julia Baldini:** Like, had been around and are hungry to build, you know, but they're hungry to build at a company that has legit revenue, legit customers, and legit, like, problems to solve and pain that people are willing to pay for.

**Julia Baldini:** And I think, like, it's like the example, like, ran our head of design, like, he had an offer to go be head of design at Intercom, and he came and worked with us, right?

**Julia Baldini:** Like, instead, and, a lot of these people that were, like, in early Coinbase, early Stripe, Airbnb, and stuff like that.

**Julia Baldini:** And then I think we're just, like, really good, like, a founder market fit, because, like, I have been doing a lot of this stuff that I'll tell you a little bit, but then, Daniel, maybe you can share a little bit on your background, too.

**Daniel Lopes:** Yeah, like, do you want just tell a little bit on just your background at Intercom?

**Daniel Lopes:** Yeah, yeah, yeah, yeah, so, like, I, like, I've been a programmer for the last 20-something years, but I have always switched between programming, as a programmer, like, different roles, like, engineering manager, whatever, and product manager.

**Daniel Lopes:** And the last 10 years, I led the product side of Iftis and that.

**Daniel Lopes:** that was one of the OG, I don't know if you guys remember that, but it's still around.

**Daniel Lopes:** Yeah, yeah.

**Daniel Lopes:** So that was one of the OG consumer-focused automation tools.

**Daniel Lopes:** Like we got to like 10 million users when I was there, took more than a billion runs a month and all that.

**Daniel Lopes:** I dealt with a lot of challenges like distributed systems and like the nature of APIs failing all the time and all that.

**Daniel Lopes:** And then I switched to take over one of the spin-offs from Basecamp when they hit like an inflection point in their business.

**Daniel Lopes:** They always done like the traditional, they essentially had like negative turn their whole life for the last 10 years.

**Daniel Lopes:** But it got to a point to where they crossed like nine figure with like a tiny team.

**Daniel Lopes:** they decided to just point everything at the Basecamp product instead of the other products.

**Daniel Lopes:** And I took one of the products that they had and I ran that for the last six years.

**Daniel Lopes:** Before meeting Marcel, and, like, right before meeting Marcel, was at that point where, like, okay, GPT, it was right before GPT-3 came out, and it was, the APIs were getting available, and it was very clear that things were going to change, but I didn't want to be, like, doing things, like, little features on top of existing tools.

**Daniel Lopes:** I wanted to do something that was not possible before, and so I spent, like, almost, like, a year just, like, reading as many papers about prompt engineering, especially, because I was interested in applied AI more than the research side of things, and that's when I met Marcel, and Marcel was, like, playing the giant sandbox, which is, like, marketing as a whole, and, like, okay, this is the perfect place to apply, to do applied AI properly, because you're not super near in, like, customer support, for example, or training, which is just much smaller, you know.

**Julia Baldini:** Yeah, and I think, like, the thing that really has made a difference in how we're approaching things from a lot of other businesses, I think, is, like, the fact that

**Julia Baldini:** Daniel had seen what a distributed infrastructure looked like to run workflows at the billions, right?

**Julia Baldini:** So then we approach the problem not as, oh, how do we build a shallow marketing agent, but rather as, like, how do we start with outcomes and work our way backwards into, like, what does it take in order to scale quality, but not from a perspective of AI only or experts only.

**Julia Baldini:** Like, so from day one, all our primitives are both, like, scalability, but also, like, that interaction between, like, the kind of the experts as well as, like, the workflows that I'll explain in a little bit.

**Julia Baldini:** Can ask you two questions?

**Julia Baldini:** The first one, for the team thing, how do you have those conversations around, hey, we're, you know, kind of this high margin, but a little bit service-oriented business?

**Julia Baldini:** Are you finding people, yes.

**Julia Baldini:** Are you finding them, like, we get it, or that's a bifurcation, or there's some selling there?

**Julia Baldini:** it's, like, there's definitely a couple of things, right?

**Julia Baldini:** Because what you're trying to figure out is, like, are they AI native or not?

**Julia Baldini:** You

**Julia Baldini:** And did they want to build or not?

**Julia Baldini:** So assuming they checked those two boxes, then a lot of it is more of like it might take them a little minute to just understand to go to market or understand marketing because maybe they're not familiar, especially on the build side with like marketing overall.

**Julia Baldini:** And they're like, oh, it's just content.

**Julia Baldini:** And then like when they start to understand how big of a thing this is, then it clicks for them.

**Julia Baldini:** And then the second like Daniel, like they pass some of the engineering interviews and they go in and Daniel kind of shows what we build.

**Daniel Lopes:** They're like, oh, , this is like legit infrastructure.

**Daniel Lopes:** Yeah, you have more context to there.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Like the way we're thinking is that like we kind of split the company into two.

**Daniel Lopes:** So we have growthx delivery team are the folks that are doing the services side of it.

**Daniel Lopes:** And they are the users of the growthx build team.

**Daniel Lopes:** So like the build team is like a traditional product team, but we have just one customer.

**Daniel Lopes:** And that one customer is all of our pods performing the services.

**Daniel Lopes:** So like the build team doesn't interact directly with the client.

**Daniel Lopes:** And they interact with the people's services.

**Daniel Lopes:** So that's kind of the setup we have.

**Daniel Lopes:** So they come in as just normal.

**Daniel Lopes:** I can show you the architecture later, but we split the team into three, the build team.

**Daniel Lopes:** So it's like a client ops folks, client ops engineers, our four deploy folks, adjusting our microagents or creating custom ones depending on the client.

**Daniel Lopes:** And then we have a runtime team that does a distributed system and the framework that we have under the hood.

**Daniel Lopes:** And then we have a product team that adjusts the platform for the UI, the vertical software for content marketing.

**Daniel Lopes:** So we have the two layers.

**Julia Baldini:** That makes sense.

**Julia Baldini:** By the way, you've at least five, maybe six or more of our portfolio companies just on this page alone.

**Julia Baldini:** So it's great that you're working on it.

**Julia Baldini:** You can upload that relationship too.

**Julia Baldini:** It's helpful.

**Julia Baldini:** Have you guys, like, this makes complete sense to start with this ICP because it's local to you.

**Julia Baldini:** They're going to be early adopters.

**Julia Baldini:** Some of these are large enterprises, but they are.

**Julia Baldini:** Yeah.

**Julia Baldini:** It's a much additional too.

**Julia Baldini:** Yeah, for sure.

**Julia Baldini:** Like a diligent software company.

**Julia Baldini:** Have you guys put thought into what's the right timing or when you'll start making the move outside of software, do you think that that's a good.

**Julia Baldini:** We'll think

**Julia Baldini:** So just stick with that.

**Julia Baldini:** Yeah, like, honestly, like, right now, it's like, we're getting a lot of demand, and we just hire a first salesperson.

**Julia Baldini:** And so right now, we're trying to have, like, an 80-20 mindset to everything of, like, 80-20, like, 80%, like, go serve, what's incoming, where we know how to serve, and things like that.

**Julia Baldini:** Also, the core use cases that we know we can be successful.

**Julia Baldini:** And 20% can be, like, let's try out frontiers, right?

**Julia Baldini:** Like, of a new use case, like, Okta Not Zero, like, sales enablement, prospecting, and it's, like, kind of a use case that we're, like, all right, let's see, right?

**Julia Baldini:** Like, or maybe, like, Rinkus is, like, very different models, like, traditional company they just signed up, like, week.

**Julia Baldini:** And it's, like, okay, let's see how we do there.

**Julia Baldini:** We have a couple of those.

**Julia Baldini:** They're a little bit more on the traditional side, you know?

**Julia Baldini:** And so, like, that's a way for us to not, like, distract too much, but also not stay still, you know?

**Daniel Lopes:** I would also add, I'm thinking I would add to the commercial.

**Daniel Lopes:** I just said, it's just like a lot of the things that the tech or like AI first or like early series B or like A to C, let's say, startups in the tech space go through, it's like a super high bar for achieving results compared to like a traditional non-tech company.

**Daniel Lopes:** So like if we cleared that hurdle, like a lot of stuff that we've done for like Lovable, for example, or for VAPI, or like the agents that we had to create for them, it's so much easier to apply them to like some more like more traditional non-tech.

**Julia Baldini:** makes completely sense to me.

**Julia Baldini:** Like higher technical bar, probably lower go-to-market like implementation handling bar than like a very traditional enterprise.

**Julia Baldini:** That's like, that makes sense.

**Julia Baldini:** So you solve the technical problem first, then you can go solve the problem.

**Julia Baldini:** Yeah, and like, and I won't spend too much time on like, because I want to show you like some of the stuff we built and whatnot.

**Julia Baldini:** I think like what we're seeing right now is kind of like this natural progression where as you achieve ROI, you

**Julia Baldini:** With some companies, then they're immediately like, hey, I don't want to hire teams, I don't want to hire more service providers, can you just do more?

**Julia Baldini:** They can ask for more lanes.

**Julia Baldini:** So all of these on the right are asking for additional lanes, essentially work streams, essentially what we call them, right?

**Julia Baldini:** And so like...

**Julia Baldini:** Would it just be worth touching on quickly, just in terms of the way you're pricing work streams versus kind of like work streams where you can see if you're doing TNF?

**Julia Baldini:** Yeah, so what we do is we do an eight-week strategy sprint.

**Julia Baldini:** And so think of the strategy sprint as like a crazy accelerated, setting the strategy, getting the right inputs, building the context, setting up the platform, and then getting to the definition of done and calibrating.

**Julia Baldini:** So I think I learned a lot from my time at Scale.ai, where essentially like you wouldn't take on a Waymo and be like, hey, you know, it's like you have to calibrate a queue.

**Julia Baldini:** And so a queue is like a work stream for us, right?

**Julia Baldini:** Like it's like, hey, it's like a campaign, it's like a project, not a project, but it's like a lane, right?

**Julia Baldini:** A lane that you're going to actually do, right?

**Julia Baldini:** Like exactly, like towards an outcome, like you want to improve the models in this way, right?

**Julia Baldini:** Like in our case, it's like, hey, I want to...

**Julia Baldini:** I organically through editorial.

**Julia Baldini:** want to grow organically through programmatic landing pages.

**Julia Baldini:** Hey, I want to launch, build my distribution through a newsletter.

**Julia Baldini:** Hey, I want to do, you know, sales enablement and prospecting for ABM.

**Julia Baldini:** Like, you know, like, so there's like specific lanes.

**Julia Baldini:** And so then like those eight weeks, we're able to get to high quality, align on expectations, because before it was like, hey, well, I can come to you and you can say, I want X or Y, but like in a sales call, you can't get to that.

**Julia Baldini:** So it's a way for us to get paid to essentially spread out things, you know.

**Julia Baldini:** And, and so what we're finding, like the time to value is pretty good.

**Julia Baldini:** And so we switched to that model June 1st.

**Julia Baldini:** And since then, we had 100% conversion rate.

**Julia Baldini:** So we're not in our projections, we're not assuming 100%, we're assuming 85%.

**Julia Baldini:** But it's like, so far, you know, it's been really, really strong.

**Julia Baldini:** And so, so that's, and then after that, what's the talent profile of the person that does that engagement?

**Julia Baldini:** Yeah.

**Julia Baldini:** So think of it as kind of like an account strategist.

**Julia Baldini:** So we're hiring them from like AI consulting.

**Julia Baldini:** Kind of motions and some of them have been promoted from within that were the best people that were forward deployed with clients.

**Julia Baldini:** And then there's a mix of also like managing editors, people that are like really good with words and communication and things.

**Julia Baldini:** They're kind of like behind the scenes supporting that access.

**Julia Baldini:** Yeah.

**Julia Baldini:** And then like, I will skip the founder journey, but I think that the TLDR here is that like all of this is like, like I haven't, content is not like a thing that I just started thinking about.

**Julia Baldini:** I was like, from day one of my career is what I built for all these companies, you know?

**Julia Baldini:** And so that.

**Julia Baldini:** What was your role at scale, for example?

**Julia Baldini:** I was their CMO.

**Julia Baldini:** Yeah.

**Julia Baldini:** Yeah.

**Julia Baldini:** So I was there for two years and I was head of growth at ServiceDine, head of growth at HashiCorp.

**Julia Baldini:** Yeah.

**Julia Baldini:** And then I built the first publication for IBM.

**Julia Baldini:** Yeah.

**Julia Baldini:** When you think about like people like growth oriented company as well, like it makes sense where you're finding your early kind of wedge in product market fit.

**Julia Baldini:** Like you are part of the trifecta of like what every company needs.

**Julia Baldini:** Yeah.

**Julia Baldini:** Usually they're starting with engineering and product and then they're going to start thinking.

**Julia Baldini:** Thinking about, like, how do I do growth marketing, and then how do I do selling, right?

**Julia Baldini:** And that's, like, it's a tryback though.

**Julia Baldini:** And, like, I promise you, I don't mean this in, like, a bad way, but, like, at the end of the day, people wish they could hire me, right?

**Julia Baldini:** In a lot of ways, people wish they could hire somebody like that, and they wish they had a Daniel on staff, right?

**Daniel Lopes:** Like, if you're a marketing...

**Julia Baldini:** On the marketing side, yeah.

**Julia Baldini:** And you wish engineering resources could be deployed against your marketing model.

**Julia Baldini:** Yeah, with, like, somebody with my mindset and execution and things like that, right?

**Julia Baldini:** Like, and so, like, at the end of the day, it's a lot easier to scale what we're doing by just saying, like, replicate me more, and, you know, and build the way Daniel has built things in an AI-native way.

**Julia Baldini:** And so, I think, like, and then there's just, like, all these, this perfect storm, you know, all these tailwinds of, like, paid is getting more expensive, like, AI Answers is completely shifting to distribution, and you can't put ads in AI Answers, right?

**Julia Baldini:** Like, agencies all  suck, and they're horrible.

**Julia Baldini:** I don't know of anyone that loves their agencies they're working with.

**Julia Baldini:** And then, like...

**Julia Baldini:** The tools are just like garbage, right?

**Julia Baldini:** And it's not that they're garbage.

**Julia Baldini:** They're like unmaintainable.

**Julia Baldini:** They're really hard.

**Julia Baldini:** They don't get easier to use over time and become smarter and harder.

**Daniel Lopes:** On the tool side, one thing I would say is that they were not meant for this.

**Daniel Lopes:** Like I saw that firsthand at F.

**Daniel Lopes:** So we had 10 million users.

**Daniel Lopes:** We essentially built a graph kind of way to stick KPIs together like before Zapier, and we just never rolled out for everybody because our goal was to be like D2C and be the easiest thing that you could use.

**Daniel Lopes:** And like just a tiny fraction, less than 1% of the active users converted to actually stitch together it, else loops and all that.

**Daniel Lopes:** And now it's like way worse because like the agents, it's the loops are unpredictable.

**Daniel Lopes:** And you want to be, and you want to make that part of the decision making.

**Daniel Lopes:** It's like, is the evaluation passing?

**Daniel Lopes:** Can I do another pass?

**Daniel Lopes:** Should I do another pass?

**Daniel Lopes:** All these things like they're not predictable anymore.

**Daniel Lopes:** So like we started like last...

**Daniel Lopes:** When we were bootstrapping, we were trying to avoid as much as possible coding, anything custom.

**Daniel Lopes:** So we used everything.

**Daniel Lopes:** We used NA10, we used AeroOps, used Zapier, we used everything that was off the shelf.

**Daniel Lopes:** And the sophistication level, needed to cross the last 10% for full efficiency in some things.

**Daniel Lopes:** It either would be, because of workflows, was like workflow calling each other, calling each other in multiple different subfolders in like a Zapier or an NA10.

**Daniel Lopes:** Or things just like taking forever to run because they're not meant for that level of capability.

**Daniel Lopes:** So we ended up like getting rid of that and just like code works.

**Daniel Lopes:** But is there room for creating a new way of coding that coding agents can, like today, like if you were to create something like Raios or Django or React with the goal of like code generation being core of it and creating workflows for this kind of environment, how do that look like?

**Julia Baldini:** So that's essentially what.

**Julia Baldini:** This something I've been thinking about to you, something like 9.8.9 is really meant for the user, it's not meant for the enterprise.

**Julia Baldini:** Like, a lot of users within an enterprise could get value for, like, whatever they were doing day-to-day, but it just doesn't scale across, like, lots of them, and it certainly doesn't impute, like, best practice.

**Julia Baldini:** So that's why you guys have them springing up from that, building it, one, closer to that, all closer to the code, imputing our best practice of, like, hey, we actually don't do this.

**Julia Baldini:** And they just, like, right now, like, I think content, high-quality content, which is the building block in the atomic unit for all of marketing, and gives you a right to earn, like, all the jobs to be done within marketing is what we believe, right?

**Julia Baldini:** An ad has content, has images, has copy, has context, has targeting, right?

**Julia Baldini:** Like, content is deceivingly hard to do, high-quality content.

**Julia Baldini:** And so, like, we're meeting the market where they are, which is why there's 32,000 agencies in the U.S.

**Julia Baldini:** alone that do content, like, agencies, and then over 300,000 freelancers that are doing

**Julia Baldini:** Doing editing and writing and content overall, like that's a ton of like fragmentation and pain right there, right?

**Julia Baldini:** Like, and so for us, like the market is, like you said, like where you said, you said two things, right?

**Julia Baldini:** Like the 10 is so much bigger and you got to meet the market where they are.

**Julia Baldini:** And it's like those things like literally like you read from our slide.

**Julia Baldini:** then you're converting it into like a solution, which means that what you're doing during that diagnostic phase is very effective.

**Julia Baldini:** So yeah, and all of it, would be like, well, even if we weren't doing the way we're delivering outcomes, it would be the process of building what we're building no matter what, right?

**Julia Baldini:** Like would you like start with the outcomes?

**Julia Baldini:** And then like now the system of records, like the Salesforce are becoming like useless more because it's like you're just dumping information that's outdated there, right?

**Julia Baldini:** And even systems of engagement are great, but like I think like a lot of what we're trying to figure out is like, what does the system of work look like when you need AI and experts to collaborate, learn and iterate so that

**Julia Baldini:** Every run, every output makes the next output better, faster, cheaper, you know?

**Julia Baldini:** And I think, like, that's what companies want.

**Julia Baldini:** Like, they're not buying Cursor, Augment Code, and others, you know, because, like, they're just, like, a system of record.

**Julia Baldini:** They're buying because, like, they're getting work done, right?

**Julia Baldini:** And so for us, like, that's what we built ultimately.

**Julia Baldini:** It was, like, starting with these sequences of, like, understanding the work, creating, like, a config file for the work, assembling the right tools, if you will, that I'll show you in a second, and observing the work, collaborating with experts, and then improving the outcomes.

**Julia Baldini:** But then, like, the most important thing is also, like, as we're doing that, it has to accelerate the outcomes that drive to the right ROI, and then people see ROI faster, right?

**Julia Baldini:** And then it's, like, a no-brainer.

**Julia Baldini:** Then it just becomes, like, okay, this is, like, a no-brainer.

**Julia Baldini:** So maybe, Daniel, I don't know if it makes sense.

**Daniel Lopes:** Yeah, yeah.

**Julia Baldini:** I can walk through the stuff, or you can share your screen and walk through.

**Daniel Lopes:** Yeah, yeah.

**Daniel Lopes:** I can't take it from here.

**Daniel Lopes:** Let me just open the same slide that you have on the internet.

**Julia Baldini:** Yeah, so, like, under the hood, as he's pulling up, like, a lot of what we built was, yeah, go ahead.

**Daniel Lopes:** Yeah, so what Marcel was showing, like, essentially, we're thinking in two parallel tracks, and, like, the under-the-hood track is we need full flexibility, and we need full flexibility in the sense of, like, last year, we started with sequential workflows, sequential LLM steps, mostly, because they were not good enough with reasoning.

**Daniel Lopes:** We didn't have reasoning models and all that, so we, like, were so many steps.

**Daniel Lopes:** But then over time, we want to use the same infrastructure to do, like, React agents and that kind of stuff.

**Daniel Lopes:** That, to expose that through the user interface is super hard, so what we end up creating is this lower-level runtime layer with our custom framework.

**Daniel Lopes:** Like, like, think of it, like, Rails or Django, that, what they did for.

**Daniel Lopes:** Web, what we're trying to do for under-deterministic applications that are built on the top of LL.

**Daniel Lopes:** So think of it like tracing is embedded, so we don't need something like length use of brain trust.

**Daniel Lopes:** Evolves are embedded, so you don't need to call different APIs for that.

**Daniel Lopes:** And all the functions for backing off when LL fail and wait for it to run again is already there.

**Daniel Lopes:** All the things for like dealing with prompts, like rendering the prompts and like prompt playground, all that stuff, it's part of the framework.

**Daniel Lopes:** The same way as like Rails will talk to the database, Django will talk to the database, they have admin UIs and all that embedded into the framework.

**Daniel Lopes:** So for us, like that's the in front of the hood.

**Daniel Lopes:** And as we deploy that with clients, what we realize is that we get so many things that are common across all of them.

**Daniel Lopes:** So we get things like, as we decompose the way like somebody like Marcel works or like some of like expert like.

**Daniel Lopes:** The strategists or writers, they almost always work the same way with variants in between, but like the core is the same.

**Daniel Lopes:** So for us, we ended up having like a drafting agent or a proofreader agent or an infographics agent or a research agent.

**Daniel Lopes:** And some of those would just like sit on top of a bunch of different APIs.

**Daniel Lopes:** Like our research agent, for example, if it's a content complexity on the higher end, then we use XAI.

**Daniel Lopes:** And something simpler, use Stably.

**Daniel Lopes:** And for something even simpler, we use Perplexity, for example, Perplexity Presearch.

**Daniel Lopes:** It's expensive to use XA, but for some clients that matters, the being always correct matters more.

**Daniel Lopes:** And so like those elements, like those reusable building blocks, if you look on the top right here, that's like we have about like 200 workflows, some are agentics, some are sequential.

**Daniel Lopes:** But for the client-specific ones, we have like just about 60.

**Daniel Lopes:** So this screenshot is from last week.

**Daniel Lopes:** Everything else is reusable.

**Daniel Lopes:** So essentially build this framework that you can build agents and you can use them as like SaaS features or you can call them directly as APIs.

**Daniel Lopes:** And that's the bottom layer.

**Daniel Lopes:** And then the second track that sits on top of this, like in our mind, like you can't just use a chat interface because you cannot enforce behavior in the chat interface.

**Daniel Lopes:** So many times you want to do things in volume.

**Daniel Lopes:** So like if I want to create 100 pages at the same time or trigger 100 researches on different topics, you need a way to enforce that to execute like in the same way, standardized for the workspace.

**Daniel Lopes:** So we have to build this custom user interface on top that is specific to that vertical of content.

**Daniel Lopes:** We're focusing on content marketing first and it's really focused on like a handful of types of content first.

**Daniel Lopes:** So that interface is specific to this space that we're trying to solve.

**Daniel Lopes:** And what that looks like in practice is two different apps.

**Daniel Lopes:** So we have Atlas.

**Daniel Lopes:** Those are all internal tools that we use now.

**Daniel Lopes:** And we're going to expose more and more to the client.

**Daniel Lopes:** So we'll start with the client just handling the oversight and the reporting, like looking at dashboards and our team performing the work.

**Daniel Lopes:** And then over time, we'll flip more and more to the client to do more of the work.

**Daniel Lopes:** But the business lives of all of our clients, and then if you look at augmented code, for example, we have all the activity feed, what's happening.

**Daniel Lopes:** We have a folder with all the documents that we come up with during the onboarding process.

**Daniel Lopes:** during that time that Marcel was talking about the deploy of the team, we spent a lot of time, like, what are the products that they serve and how do they talk about it?

**Daniel Lopes:** What are the personas that they serve?

**Daniel Lopes:** What's the factual context about the company?

**Daniel Lopes:** When was the founder?

**Daniel Lopes:** Who are the founders?

**Daniel Lopes:** kind of stuff.

**Daniel Lopes:** Also, like, what are the things that matters to them?

**Daniel Lopes:** Like, for example, for augmented code, they have, like, we have a to-do list that has to pass on the provider agent performance.

**Julia Baldini:** Forming these checks, like, they hate them dashes, for example.

**Daniel Lopes:** They, like, when you, yeah, so, like, there's, there's all these different things, like, the way that every business is closed.

**Julia Baldini:** Well, there are various experts that you're starting there, but every single person.

**Julia Baldini:** This is the point I always make when I meet, because they don't solve any business problem, and then you can just start to be, like, okay, like, what are all the people doing?

**Julia Baldini:** What do you care about?

**Daniel Lopes:** How do you measure success?

**Daniel Lopes:** And then when you, like, codify that and start building agents around it, like, that's the Exactly, yeah.

**Julia Baldini:** We're just starting with what you know.

**Julia Baldini:** We've had, like, PE firm, like, about six months ago, we were already, and it didn't make sense at the time.

**Julia Baldini:** They're, like, hey, can you do this for sales use cases and, like, across, like, all our 80 companies?

**Julia Baldini:** Right.

**Julia Baldini:** Because it's, like, every company does the same  thing.

**Julia Baldini:** Like, so if you do it one, I can just do it two times 80.

**Julia Baldini:** And we're, like, yeah.

**Julia Baldini:** Yeah.

**Julia Baldini:** And I think, like, the context piece is so important, and, like, that's why context engineers, is almost more important.

**Julia Baldini:** And then they even prompt engineering some ways.

**Julia Baldini:** Because these companies don't, you ask SentinelOne, a public company, you're like, hey, can you give me a written doc of your persona?

**Julia Baldini:** I was like, nope.

**Julia Baldini:** Do you have a doc that explains all your products and all your features?

**Julia Baldini:** Nope.

**Julia Baldini:** So you can't have a success.

**Julia Baldini:** We've had the several ones.

**Julia Baldini:** Yeah, Brian is great.

**Julia Baldini:** Like a wild, wild.

**Julia Baldini:** Yeah, yeah.

**Julia Baldini:** I'm really interested in that.

**Julia Baldini:** Yeah, yeah.

**Julia Baldini:** He's sent to several customers already.

**Julia Baldini:** So it's cool that one of your customers are doing this.

**Julia Baldini:** I like bringing it to the house.

**Julia Baldini:** Oh, We've got a company that's a higher marketing.

**Julia Baldini:** Oh, 100%.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So like, so like, so let's just like explain everything like real quick.

**Daniel Lopes:** One thing is context.

**Daniel Lopes:** Another thing is knowledge.

**Daniel Lopes:** And knowledge, like, every, like every company has like internal things that they care about.

**Daniel Lopes:** So in the case of Clark, for example, they really don't want to make any claims that are wrong about the SDK.

**Daniel Lopes:** Or we don't want to write anything that's wrong about that.

**Daniel Lopes:** Potential vulnerabilities in their space of authentication.

**Daniel Lopes:** But for that, we ingested, like, we did a large research and ingested everything about authentication vulnerabilities that we could find.

**Daniel Lopes:** And that you have something like, in this case, we have, like, three sources.

**Daniel Lopes:** The SDK is one of the sources.

**Daniel Lopes:** Then you're going to have, like, a knowledge base that looks like this that has, like, a thousand plus entities.

**Daniel Lopes:** And they will cover all the little nuance for, like, OWASP or, like, authentication problems with, like, different kinds of providers.

**Daniel Lopes:** And then we run that, those two sources of truth we have now, like, the context plus the knowledge, can be used throughout the whole process.

**Daniel Lopes:** And some of the other things we have, like, we have analytics that will, like, track your Google search console and your Google Assistant.

**Daniel Lopes:** GrowthClerk is not set up.

**Daniel Lopes:** But just going back to everything here.

**Daniel Lopes:** We also like to take stock of everything that you have, like, your pages and find opportunities.

**Julia Baldini:** What the folks are doing, but the bulk of the work happens is such things you get.

**Julia Baldini:** And opportunities in inventory is just like over time, you know, we might be tracking like a Reddit thread that and then come up with different opportunities of things you should be talking about or things you should be doing.

**Julia Baldini:** But also your website is like a goldmine of  you go, you should go fix or improve or change.

**Julia Baldini:** Right.

**Julia Baldini:** And that's based on both like the analytics and signals and things like that, but also the substance of the content and how people are finding that as well.

**Julia Baldini:** So it's like this, this system of work can sit on top of that, right?

**Julia Baldini:** Like, and do so much, you know.

**Julia Baldini:** Yeah, you're combining like deep research with the actual kind of output.

**Julia Baldini:** Yeah, exactly.

**Julia Baldini:** And so, yeah, Daniel will show you some of the execution plan plans.

**Daniel Lopes:** Yeah, so like all the features that I showed you in this platform, Atlas, that's our vertical for content marketing.

**Daniel Lopes:** Like, everything that's AI enabled here, let's say if I select this and I want to, like,

**Daniel Lopes:** We have an experience with a cursor where you can do shortcuts that are based on content focusing, that make it more concise, improve caliphany, and all that.

**Daniel Lopes:** But it's staking in those context documents from the space.

**Daniel Lopes:** And you can see them loaded here on the right already.

**Daniel Lopes:** So all these things are going to the same runtime that we use for the agents as well.

**Daniel Lopes:** So it's all being performed in the same way.

**Daniel Lopes:** And then the other thing we have, if you look here on the left side, have workflow projects.

**Daniel Lopes:** And that's how we build the pipelines of anything that we want to scale and execute with multiple agents doing the work.

**Daniel Lopes:** And in the case of Augment, for example, their editorial pipeline, we might have topics like prompt engineering for agentic AI swarms, for example.

**Daniel Lopes:** If you click on this, you have each one of those steps.

**Daniel Lopes:** Those are the columns from those rows that I was showing you before.

**Daniel Lopes:** Each one of those columns are different, either agentic workflows or...

**Daniel Lopes:** Sequential Workflows.

**Daniel Lopes:** In the case of our research topic here, it's going to take like 10 minutes because it will make many different questions to XAI.

**Daniel Lopes:** First, we'll come up with a plan for the execution.

**Daniel Lopes:** So the execution here, the plan would be something like, I'm just actually using Table.

**Daniel Lopes:** Table is okay.

**Daniel Lopes:** X is more impressive.

**Daniel Lopes:** But the research plan, first to come up with a research plan, the research plan will look something like this.

**Daniel Lopes:** It changes how the AI engineers define the role.

**Daniel Lopes:** Success criteria.

**Daniel Lopes:** criteria.

**Daniel Lopes:** That's the priority.

**Daniel Lopes:** Like, if the priority is high, it cannot stop until it crosses that or reaches the maximum number of iterations.

**Daniel Lopes:** And you pass all that parameterization if you want.

**Daniel Lopes:** So at the end, you end up with like, it will perform this and it will perform all these questions in parallel.

**Daniel Lopes:** So it's taking 10 minutes, but it's taking 10 minutes because it's running 20 in parallel.

**Daniel Lopes:** I like to run sequential like most of the AI workflow tools will do.

**Daniel Lopes:** We'll be like, I'll

**Julia Baldini:** So now just to pause for a second, take a step back, imagine trying to build all this stuff in a low-code tool and then having a marketer go and explore different APIs like Exa, AI, Tavly, Perplexity, stitching it all together and then have a marketer try to learn how to do evals and then try to figure out how to do agentic evals and loops and then do all of that.

**Julia Baldini:** Only to have to copy and paste this thing over to a Google Doc and send it to another human to evaluate that and then based on the evaluation of a human, if it passes or not, figure out how to take that feedback and improve the workflows and the evals and the outputs, right?

**Julia Baldini:** Like there's no way you need a system of work that kind of connects all those things in a loop so that one thing improves the other.

**Julia Baldini:** Yeah.

**Julia Baldini:** We're also just dependent on quality of the marketers versus getting the skill of the cost.

**Julia Baldini:** Yeah, and also if you have the wrong person in the loop, then they  up everything.

**Julia Baldini:** You know, we've seen that one before.

**Julia Baldini:** Yeah, Joey was the founder of Allbirds, and him and his wife was the supplement once, was our first one in healthcare.

**Julia Baldini:** We got an inbound from him and hers as well, you know, so I think there's, we've talked to, like, really scale, like, pharma marketing roll-ups, where then, like, this AI hacker paired up with, like, a really good, like, PECO.

**Julia Baldini:** So the PECO focuses on, like, the roles that you guys have, like, that's a really good, sticky vertical, and then you just need some number of pages to brag about in sales pitch, but then, you know, you can kind of quantify all the work that they do.

**Julia Baldini:** Yeah, and then, like, there's so much more, too.

**Julia Baldini:** Maybe just for a matter of time, like, just know that there's, like, a lot of things beyond that, like, around, like, this one's, like, around medical recommendations, you know, and expert.

**Julia Baldini:** There's, like, there's, bunch more that we can go deeper as well on, but it's, like, also there's, like, cover images and imagery, and, like, this can be applied.

**Julia Baldini:** Video, anything that has an API, anything that has an MCB server, anything that requires context plus knowledge plus workflows plus human intervention, this can be applied to.

**Julia Baldini:** It's just like we're staying really focused because content is not only the atomic unit for marketing, but content is language, and language is the interface to AI, technically is the programming language of the future.

**Julia Baldini:** And so if you get good at content, you get good at everything related to knowledge work, pretty much.

**Daniel Lopes:** Yeah, just to give you a little bit of the roadmap, it's two minutes, like overview of how we're thinking the whole problem, and how we can make this, how we're thinking that we can make this service part of service and software really scalable.

**Daniel Lopes:** The approach that we're taking is like I said, like we have the vertical tool that was showing you, that was the grid and the context artifacts and the knowledge.

**Daniel Lopes:** The knowledge phase, that's like specific to content marketing.

**Daniel Lopes:** From that we can extract a bunch of self-serving products.

**Daniel Lopes:** we're working on this one called CheckThat.ai.

**Daniel Lopes:** We're going to launch that in October.

**Julia Baldini:** It's essentially a G2 crowd for AI visibility, and you can see your company, how you're doing.

**Julia Baldini:** A lot of your brand is ranking for everything.

**Daniel Lopes:** Yeah, that's a good lead done.

**Daniel Lopes:** So that came out of our needs of, like, monitoring how our clients are doing.

**Daniel Lopes:** So that's, like, all content marketing-related, all marketing-related.

**Daniel Lopes:** We're to start eating more and more of the functions and jobs should be done at the marketing department.

**Daniel Lopes:** And then we have the AI workflow engine under the hood.

**Daniel Lopes:** We're thinking about releasing our framework, and then we're going to release the web UI that they are showing you that you can inspect the work as well.

**Daniel Lopes:** And over time, we might let you host things for you, and we can learn from all the executions.

**Daniel Lopes:** It's all in code, but the way we're thinking is, like, we control the data you have.

**Daniel Lopes:** All the data from the runs, from the human reviews, it's all part of the output of the framework, and it's like the framework has that.

**Daniel Lopes:** And another thing we're working on is the actors and having them work with the client and all that, you delegate that to like a marketplace, but you have to figure out the definition of what's during the onboarding.

**Julia Baldini:** That's kind of like how we're thinking.

**Julia Baldini:** Yeah, and then like maybe just to kind of wrap things up and then happy to kind of dig in further or do other deep dives, but like to what Daniel was saying, right, like the goal is like expand into every marketing job to be done sequentially, you know, and as we're getting the goal from customers.

**Julia Baldini:** But as you can see, this has like so much lookability way beyond, it's just like we're staying focused in and under the hood, what we're building can really be repurposed to a lot of different things.

**Julia Baldini:** And, but like the, the 10 is still large that, you know.

**Julia Baldini:** So there's no point of trying to go fetch additional lanes right now.

**Julia Baldini:** Like, it's just insane, you know.

**Julia Baldini:** We've got a pretty incredible amount of salesperson.

**Julia Baldini:** Yeah, yeah.

**Julia Baldini:** So our unit account is really good.

**Julia Baldini:** We closed 10 deals this month already.

**Julia Baldini:** It's almost 2 million in net.

**Julia Baldini:** And obviously, like, they have kickoffs.

**Julia Baldini:** So the way to think about it, like, we're closing it, but we're doing two kickoffs a week.

**Julia Baldini:** So we're both through October now.

**Julia Baldini:** And then, like, we'll air in a third kickoff.

**Julia Baldini:** And, you know, as we don't feel, like, confidence that we can continue to scale with quality.

**Julia Baldini:** constraint is, like, the scope and you're trying to keep working with that.

**Julia Baldini:** The constraint is not just that.

**Julia Baldini:** It's just, like, we, like, we're a 12-month-old-ish company, right?

**Julia Baldini:** So we've been in this 12 months.

**Julia Baldini:** Everything you see that we built, like, we raised our first dollars in March.

**Julia Baldini:** Like, so it's only been five months since our Series A.

**Julia Baldini:** The engineering team has been fully in place since, like, April, May, right?

**Julia Baldini:** Like, so we're moving really fast.

**Julia Baldini:** But we also don't want to make it seem like we're this, like, you know, CRC company, like, you know.

**Julia Baldini:** They've been around for 10 years that pivoted five times, you know, and so for us, like, our revenue is probably ahead of, like, where we are in full transparency as far as, like, how we're building things.

**Julia Baldini:** And so we also don't want to get too far ahead because the revenue is already, like, going really fast.

**Julia Baldini:** We don't want to, like, get ahead of ourselves either, you know, because, like, reputation is really important here.

**Julia Baldini:** And so that's what we're protecting.

**Julia Baldini:** We don't need to 10x, like, every month, you know, like, but we're, like, we're also are going to win.

**Julia Baldini:** And we're not doing this to be, like, you know, be happy at 50 million a year, like, at all.

**Julia Baldini:** Like, we want this to, yeah, like, we're, and hopefully, like, what we've done in 12 months is indicative of our emissions as well.

**Julia Baldini:** Like, we're not, like, we could, we could have just gone from, you know, one to five, you know.

**Julia Baldini:** we could just make a five dollars.

**Julia Baldini:** Yeah.

**Julia Baldini:** Yeah.

**Julia Baldini:** No, that's enough money for most people.

**Julia Baldini:** We were making a lot of cash last year, like, in profit.

**Julia Baldini:** So it's, like, you know, that's not the path we chose.

**Julia Baldini:** I mean, we're going to be profitable very soon.

**Julia Baldini:** Again, you know, but that's not what we're optimizing for, you know.

**Julia Baldini:** The agencies do run, like, surprisingly high profit markets.

**Julia Baldini:** I mean, we've seen them buy.

**Julia Baldini:** Their markets are , but they do have, like, you know, 20% EBITDA on average.

**Julia Baldini:** But then I think one of the challenges they have is that it's one or two founders taking all the profits and underpaying the  out of people.

**Julia Baldini:** And then they have a lot of, yeah.

**Julia Baldini:** It's a talent-sharing platform.

**Julia Baldini:** Yeah, yeah, exactly.

**Julia Baldini:** But they do take all.

**Julia Baldini:** But hopefully, like, this gives, like, a little bit of a view off, like, you know, like, so just to give a little bit of an on, like, kind of, like, how we're thinking about things.

**Julia Baldini:** We weren't looking to raise.

**Julia Baldini:** I think we got a lot of inbound, and we've been really, really selective on who we're talking to just because we know that 99% of investors are just not going to get it, you know.

**Julia Baldini:** And we're okay with that.

**Julia Baldini:** Like, we actually kind of somewhat prefer.

**Julia Baldini:** And we've been a little bit protective of, like, not opening up too much too fast because then it's just, like, it's almost like we're in on a secret.

**Julia Baldini:** And, like, everybody else is, like, wait, why is nobody else doing this?

**Julia Baldini:** You know, thank you.

**Julia Baldini:** And then kind of the feeling I got from how you were talking about it, too, you know.

**Julia Baldini:** And so we're capital efficient, but one of the reasons we're considering, like, partnering with someone at this stage versus, like, next year or not raising again ever is because, like, this is a big, like, footprint to go build against in the right way.

**Julia Baldini:** And also, like, I just think we would be really dumb to not just double down because we're not demand constrained and the TAM is massive and the urgency is insane.

**Julia Baldini:** And this is, like, the most tailwinds you can possibly get at the same time, you know.

**Julia Baldini:** And so that's kind of what we're thinking about it.

**Julia Baldini:** But we're also not, like, don't want to, like, oversell that we're, like, this crazy thing or whatever, you know.

**Julia Baldini:** We're focused.

**Julia Baldini:** We're seasoned operators.

**Julia Baldini:** Like, we attract the best talent in the planet.

**Julia Baldini:** And I think we're building from the right primitives and we're working with the top brands in the planet.

**Julia Baldini:** But it's also, like, ours to lose.

**Julia Baldini:** So we're going to move fast no matter what.

**Julia Baldini:** It's just a matter, like, how aggressive do we want to double down and have capital leverage as well to do it, you know.

**Julia Baldini:** Congrats to you both.

**Julia Baldini:** mean, it's awesome.

**Julia Baldini:** If you're open to sharing the deck, we can get you, like, have the feedback.

**Julia Baldini:** Oh, yeah.

**Julia Baldini:** Oh, deck, we have data.

**Julia Baldini:** Oh, perfect.

**Julia Baldini:** Yeah.

**Julia Baldini:** We can get pretty good feedback.

**Julia Baldini:** Cool.

**Julia Baldini:** We'll be at the breakfast tomorrow, for sure.

**Julia Baldini:** This was very helpful, and it was, like, helpful to make the Dutch one in person.

**Julia Baldini:** Yeah, yeah.

**Julia Baldini:** I understand how you guys think about the business, but we won't stop much of your path.

**Julia Baldini:** Like, I think what you guys are building is awesome, and we'll just give you feedback on, like, can we partner now, or should we just stay in touch?

**Julia Baldini:** Perfect.

**Julia Baldini:** Yeah, that sounds good.

**Julia Baldini:** Yeah, I think we should be have everything we need, and we can get you an answer probably next week.

**Julia Baldini:** Yeah, that sounds good, and we're super flexible.

**Julia Baldini:** If you guys want to double-click on anything, you know, tech or otherwise.

**Julia Baldini:** We're excited for tomorrow.

**Julia Baldini:** I know, yeah.

**Julia Baldini:** Which of the portfolio, I guess you don't know about our portfolio, but, like, of, like, what did I say in that?

**Julia Baldini:** School AI, diligent, uh...

**Julia Baldini:** And move it.

**Julia Baldini:** Move it as a customer.

**Julia Baldini:** Okay.

**Julia Baldini:** There were more on that page.

**Julia Baldini:** Is there someone that we should talk to do you is, like, a really...

**Julia Baldini:** Yeah, did we send you, I think it was on the list of people that we can make intros that, I mean, can make answers to anyone, it's just like a list of people that they know we're talking to investors.

**Julia Baldini:** I'll double click on Yeah, but Augment is great, I think Airbyte is great as well, there's several on the list, SKU.AI definitely, they're awesome.

**Julia Baldini:** And we owe you an intro to our marketing people.

**Julia Baldini:** Actually, I talked to Neil Berry, I think it was Neil, because we work with Matthew Panzerino, our chief content officer, over at TechCrunch, he runs your publications, right?

**Julia Baldini:** Different, that, you're Joey TechCrunch guy?

**Julia Baldini:** Yep, yep.

**Julia Baldini:** Joey runs our media.

**Julia Baldini:** Yeah, okay, that's who I talked to.

**Julia Baldini:** Yeah, that's a good person, but I'll introduce you to that kind of marketing.

**Julia Baldini:** Yeah, so let's just say, like, that side of your business, like, I really want to work on that, because, like, it would be sick, like, you guys are, essentially.

**Julia Baldini:** You, like, have, as you think.

**Julia Baldini:** We think about our own business and deep, think deeper most in our platform to create an advantage for our companies for free, basically.

**Julia Baldini:** And some of the bets we've placed, we have a media bet, we have a talent bet, we have an investment for our partners, we're product engineering.

**Julia Baldini:** But yeah, Joey and the media team.

**Julia Baldini:** I mean, this is going be really cool.

**Julia Baldini:** think we have over a thousand people applying a day and we run them through different workflows as well.

**Julia Baldini:** So there's so many things that I think with the right partner, that's one of the things that I think inside.

**Julia Baldini:** It's really unique because we all have like the PE side, the media side, you have like, you know, so many different farms and extension.

**Julia Baldini:** Obviously, like, it's not the only reason we, like, we're excited to partner, but it definitely, like, makes things, like, where you can accelerate, you know, the feedback in a very safe way, if you will.

**Julia Baldini:** Just like, hey, what if we try this over here, you know, but, but yeah, tons of, but on the data room, there should be a link, but I'll double check after this too.

**Julia Baldini:** I have access to deck and, um, for five.

**Julia Baldini:** I don't know if we ever got one.

**Julia Baldini:** Okay, cool.

**Julia Baldini:** I can send you like a couple more things.

**Julia Baldini:** Yeah, yeah.

**Julia Baldini:** But that sounds good.

**Julia Baldini:** Yeah, there's one to be more than a person.

**Julia Baldini:** Yeah, through it.

**Julia Baldini:** Yeah, yeah.

**Julia Baldini:** And you're around tomorrow.

**Julia Baldini:** You're excited to come in?

**Julia Baldini:** Yeah, we're going to come to breakfast.

**Julia Baldini:** I'd go out.

**Julia Baldini:** fine.

**Julia Baldini:** Yeah, yeah.

**Julia Baldini:** It's fine.

**Julia Baldini:** Oh, sweet.

**Julia Baldini:** Perfect.

**Julia Baldini:** Yeah, yeah.

**Julia Baldini:** Yeah, we got a good mix.

**Julia Baldini:** Normally, it's mostly like CMOs and marketing leaders.

**Julia Baldini:** This time, it's going to be a good mix between that.

**Julia Baldini:** Like rev-offs.

**Julia Baldini:** Yeah, like rev-offs.

**Julia Baldini:** Some people building like into the sales kind of thing, you know.

**Julia Baldini:** Yeah.

**Julia Baldini:** Click conference.

**Julia Baldini:** don't know if you stopped by there.

**Julia Baldini:** No, no.

**Julia Baldini:** I was surprised.

**Julia Baldini:** What do you think of playing and stuff like that?

**Julia Baldini:** You guys just start like, eh?

**Julia Baldini:** Or you're like, oh, no.

**Julia Baldini:** they're building something next time.

**Julia Baldini:** I think like their use cases are like...

**Julia Baldini:** We're invested in it.

**Julia Baldini:** Yeah, no, no.

**Julia Baldini:** It's like they figure a way to like distribute after building it for what?

**Julia Baldini:** Seven, eight years.

**Julia Baldini:** And so that's great.

**Julia Baldini:** And...

**Julia Baldini:** And it's kind of like Airtable eventually got to a point where it's just like, oh, okay, like they figure out like how to make it useful and enough people learn enough.

**Julia Baldini:** And I think the hard thing is just like they are also cornered though in the way they built the platform.

**Julia Baldini:** Yeah.

**Julia Baldini:** So they can't like build in a way that has human interventions built in and you have coding agents that rebuild the workflows.

**Julia Baldini:** And so a lot of it is like, but there's still plenty of use cases, like spreadsheets still exist.

**Julia Baldini:** And so it's not like spreadsheets, you know.

**Julia Baldini:** Yeah, like is Google Sheets going to cease to exist because of AI?

**Julia Baldini:** Maybe not, probably not.

**Julia Baldini:** it's also like.

**Julia Baldini:** Is it the  thing with like, is that where you want to place your bets for like the most 10 people find that?

**Julia Baldini:** Yeah, what it seems like one out of maybe 5,000 practitioners will know how to use clay.

**Julia Baldini:** And so that's just not like a, you know, that's bottlenecking too much access to how powerful AI can be, you know.

**Julia Baldini:** So then it's like, how do you actually like.

**Julia Baldini:** I think going to market tech has to be one of the hardest areas to invest in right now.

**Julia Baldini:** It is.

**Julia Baldini:** Yeah.

**Julia Baldini:** Because.

**Julia Baldini:** Because.

**Julia Baldini:** Because.

**Julia Baldini:** Because.

**Julia Baldini:** Folks like you guys will just figure out what are the best things and then where is someone else's product and margin , you can rebuild it pretty quickly.

**Julia Baldini:** It's a very outcome-oriented division.

**Julia Baldini:** Yeah, yeah.

**Julia Baldini:** But we're really, really excited.

**Julia Baldini:** appreciate you guys taking the time.

**Julia Baldini:** Thanks so much.

**Julia Baldini:** Yeah.

**Julia Baldini:** Thank you, guys.

**Julia Baldini:** Daniel, are you here tomorrow?

**Daniel Lopes:** Oh, yeah, I'm there tomorrow.

**Julia Baldini:** Thanks, man.

**Julia Baldini:** I don't have any.

**Julia Baldini:** You'll see Daniel in person.

**Julia Baldini:** Awesome.

**Julia Baldini:** Oh, cool.

**Julia Baldini:** See ya.

**Daniel Lopes:** See you guys.

**Daniel Lopes:** Thank you.
