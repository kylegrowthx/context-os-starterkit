# Datagrid <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-03
time: 17:30 UTC
duration: 29 minutes
organizer: team@growthxlabs.com
participants: Kaitlin Quimby, Liz Kushnereit, Thiago da Costa, Marcel Santilli
fireflies_id: 01KG0AWB9DZMSX0NNKVFCEJAZ5
transcript_url: https://app.fireflies.ai/view/01KG0AWB9DZMSX0NNKVFCEJAZ5
</metadata>

---

## Summary

GrowthX presented a major content strategy pivot for Datagrid (Procore) — moving from blog-led awareness to product-led discovery built around three lanes: agents as the discovery layer, connectors as a marketplace hub, and guides plus programmatic SEO as traffic engines. The team also aligned on a website redesign that will move the site out of Webflow.

---

## Context

Datagrid is a GrowthX client where Liz Kushnereit leads content strategy alongside client contacts Kaitlin Quimby and Thiago da Costa. This session presented the v1 of a new content strategy that fundamentally restructures how the website drives discovery and activation. The strategy treats the website as a knowledge graph, with agent-based content clusters replacing keyword-chasing blog content. Marcel joined late and added context on the website redesign approach, drawing on lessons from other GrowthX clients like Augment.

---

## Relevance

**To GrowthX Delivery:**
- Live example of GrowthX's evolving content strategy methodology
- Product-led content approach replacing traditional blog-led awareness
- Website redesign scope: migrate entire site out of Webflow, facelift (not rebrand)
- Lessons from Augment applied to Datagrid engagement

**To CheckThat:**
- Knowledge graph concept aligns with CheckThat's AI visibility framework
- Cross-linking and flat page structures optimized for both human buyers and AI agents

**To GrowthX Business Development:**
- Client engagement expanding from content to website infrastructure
- API integration and product embedding creating deeper client relationship
- Reference case: Webflow integration content engine producing 30 pages/week

---

## Overview

- Strategy pivot from blog-led awareness to product-led discovery across three lanes
- Agents become the canonical discovery layer with agent-based content clusters
- Connectors serve as a marketplace hub for enablement (modeled on Webflow success)
- Guides replace blogs as full-funnel SEO content linked to agents
- Programmatic SEO targets specific use cases at the agent level
- Website redesign moving from Webflow to code-based site for speed and maintainability
- API integration to embed Datagrid product experience directly on the website
- Knowledge graph approach: flat URL structure, strong cross-linking, dynamic page surfacing

---

## Key Topics

### Content Strategy Pivot
- Three lanes: agents (discovery), connectors (marketplace/enablement), guides + PSEO (traffic)
- Agent-based content clusters replace keyword-chasing strategy
- Content velocity driven by product rather than keyword research
- Full-funnel coverage: guides for informational, PSEO for high-intent, agents/connectors for product activation
- Internal linking, pre-configured workflows, deep links, and taxonomy keep everything interdependent

### Prototype & UX
- Landing page prototype for agents with deep search, chat, pre-configured workflows behind login wall
- Sidebar navigation for use-case-driven user journeys
- Connectors pages modeled on Webflow integration success (600 pages, 30/week output)
- Guides page replaces blog with new full-funnel SEO content
- Headless CMS consideration for better scalability

### Website Redesign
- Full site migration out of Webflow for speed and maintainability
- Design facelift, not rebrand — improving legibility and readability
- Augment cited as reference for design approach
- Once complete, any dev or designer can implement changes via the repo
- GrowthX scope: port and facelift content sections; not taking on product marketing or homepage redesigns

### API & Product Embedding
- Datagrid product as a "kit": knowledge, attachments, instructions, configuration
- API calls to programmatically create agents and push associated datasets
- Example: safety agent for California with OSHA standards pre-loaded
- Guides can hold compliance documents that agents pull from
- Goal: accelerate time to value, similar to Lovable's double-digit conversion rates from templates

---

## Action Items

**Liz Kushnereit**
- Present detailed content and UX strategy to Kaitlin for full knowledge transfer
- Prioritize agents for content cluster development as phase one
- Develop prototype enhancements for agents landing page UX
- Continue fleshing out connectors marketplace content based on Webflow success
- Conceptualize and prepare guides page as new full-funnel SEO engine

**Kaitlin Quimby**
- Ensure product and website agent content alignment
- Communicate content updates to product team as needed

**Marcel Santilli**
- Lead website redesign and migration planning away from Webflow
- Scope rapid facelift for legibility and readability improvements
- Coordinate design and dev team for parallel implementation
- Provide ongoing support for API and agent creation integration

**Thiago da Costa**
- Coordinate embedding of Datagrid product experience in new website structure
- Collaborate on API-driven agents content and knowledge graph implementation

---

## Transcript
**Kaitlin Quimby:** This meeting is being recorded.

**Kaitlin Quimby:** I don't know why it's not showing me.

**Kaitlin Quimby:** Hi.

**Kaitlin Quimby:** Oh, there we go.

**Liz Kushnereit:** How are you doing?

**Kaitlin Quimby:** I'm good.

**Kaitlin Quimby:** How are you?

**Liz Kushnereit:** I'm good.

**Liz Kushnereit:** Where are you based?

**Kaitlin Quimby:** I'm in Austin.

**Liz Kushnereit:** Okay.

**Liz Kushnereit:** I'm in Austin.

**Kaitlin Quimby:** Oh, wait, really?

**Liz Kushnereit:** Yeah.

**Kaitlin Quimby:** Oh, gosh.

**Liz Kushnereit:** I know.

**Liz Kushnereit:** I was.

**Liz Kushnereit:** I was.

**Kaitlin Quimby:** Obviously we should like meet up in person next time.

**Kaitlin Quimby:** Yeah.

**Liz Kushnereit:** Honestly, that would be fun.

**Kaitlin Quimby:** One of these.

**Kaitlin Quimby:** Yeah.

**Kaitlin Quimby:** Because I don't think.

**Kaitlin Quimby:** I think originally the plan was for Marcel and Tiago to join, but that has changed.

**Kaitlin Quimby:** I think they talked separately.

**Kaitlin Quimby:** But yeah, maybe I'm incorrect.

**Kaitlin Quimby:** If.

**Kaitlin Quimby:** Maybe Marcel's still joining.

**Liz Kushnereit:** Yeah.

**Liz Kushnereit:** Do you know if Tiago is not joining?

**Liz Kushnereit:** I'm sure Marcel probably isn't, but tbd.

**Kaitlin Quimby:** He'S in an in person meeting right now.

**Kaitlin Quimby:** Supposed to be done, but could be wrapping up.

**Kaitlin Quimby:** He's actually in Austin this week.

**Liz Kushnereit:** I think I gave Marcel a lot of context on Friday and then he had a conversation with Thiago over the weekend.

**Liz Kushnereit:** And then I think, yeah, we're kind of greenlit, but there's still a lot of information.

**Liz Kushnereit:** I.

**Liz Kushnereit:** Maybe I could still present it all to you because it's quite a lot.

**Kaitlin Quimby:** Yeah.

**Kaitlin Quimby:** Yes.

**Kaitlin Quimby:** Because I got like 30 second brief and he's like, this is what we're doing.

**Kaitlin Quimby:** I'm like, okay.

**Kaitlin Quimby:** He's like, but actually you need to find out more info.

**Kaitlin Quimby:** And I was like, okay.

**Liz Kushnereit:** Okay, great.

**Liz Kushnereit:** Oh, this is off.

**Liz Kushnereit:** I wish we'd done this in person then.

**Liz Kushnereit:** That would have been more fun.

**Kaitlin Quimby:** I know.

**Kaitlin Quimby:** Well, we'll have to.

**Kaitlin Quimby:** I'm sure with like some of the transition of stuff too.

**Kaitlin Quimby:** We can do one of these in person.

**Liz Kushnereit:** Okay, great.

**Liz Kushnereit:** Where's the office?

**Kaitlin Quimby:** So the procore office is located on sixth street in downtown.

**Kaitlin Quimby:** Oh, like six in Colorado, I think is the cross streets.

**Kaitlin Quimby:** Yeah.

**Liz Kushnereit:** Okay.

**Liz Kushnereit:** Well, I guess I'll screen share and then we'll see how this goes.

**Liz Kushnereit:** A lot less pressure, I guess, if it's just us, so that's nice.

**Kaitlin Quimby:** Okay.

**Liz Kushnereit:** Yeah.

**Liz Kushnereit:** Or we could wait one more minute.

**Kaitlin Quimby:** No, let's go ahead.

**Kaitlin Quimby:** I think there's a lot to cover and I know they've already covered some of it, so I would like to get a little more caught up.

**Liz Kushnereit:** Cool.

**Liz Kushnereit:** Okay.

**Liz Kushnereit:** So the TLDR is that it's a big pivot from blog LED awareness to product LED discovery surface and activation layer.

**Liz Kushnereit:** So there's a lot of moving pieces, but basically agents becomes our canonical discovery layer, Connectors becomes our marketplace style hub for enablement, and then guides and PSEO become our main traffic Engines and also like overlap into enablement especially for agents in our use case guides.

**Liz Kushnereit:** So what does that all mean?

**Liz Kushnereit:** This is basically three lanes of expansion.

**Liz Kushnereit:** So guides in PSEO is more of our like editorial content agents.

**Liz Kushnereit:** We will be taking over this page and optimizing for UX and content.

**Liz Kushnereit:** And then connector is basically the same story optimizing UX and the content.

**Liz Kushnereit:** And so I'll have a lot of like references especially on connections.

**Kaitlin Quimby:** And then just one thing on the agents, we just want to make sure that we have it.

**Kaitlin Quimby:** So like whatever we're doing there, updating or if we're changing, we want to reflect it on the product side too.

**Kaitlin Quimby:** So then the agent library on the product is just matches.

**Thiago da Costa – Datagridai:** That's.

**Kaitlin Quimby:** I mean obviously we can have more info on the website if we want but just FYI.

**Liz Kushnereit:** Yeah, I definitely think we'll need to know like that.

**Liz Kushnereit:** That is like not a.

**Kaitlin Quimby:** Right now.

**Kaitlin Quimby:** Yeah, yeah, no, like right now for example we have like a notion page and that's kind of our source of truth.

**Kaitlin Quimby:** So if we're updating it on there, I'll let like the product team know and like then they know to like go update in the product.

**Kaitlin Quimby:** So it's just all aligned.

**Liz Kushnereit:** Our next step is like the prioritization of agents and confirming which ones we want to move forward with, which is kind of segues into what the content strategy is, which is agent based clusters.

**Liz Kushnereit:** So, so building all of our content clusters at the agent level.

**Liz Kushnereit:** Right.

**Liz Kushnereit:** So I think there's like a lot of opportunity there and it moves the content strategy from chasing keywords to creating content velocity through product.

**Liz Kushnereit:** So that would be like our next phase here.

**Liz Kushnereit:** And so that's, this is kind of what that looks like.

**Liz Kushnereit:** Right.

**Liz Kushnereit:** So our editorial, our agent based cluster pages so guides pseo.

**Liz Kushnereit:** This is full funnel, especially guides.

**Liz Kushnereit:** This is where we're having more informational content.

**Liz Kushnereit:** We can't have like a mix of bofu, tofu.

**Liz Kushnereit:** PSEO gets a bit more into high intent and then we're still capturing some organic search into agents and connectors pages.

**Liz Kushnereit:** That will be much higher intent.

**Liz Kushnereit:** But we'll talk about what that looks like a little bit further down that taxonomy would look like this.

**Liz Kushnereit:** So and then of course these are all linked through internal linking, pre configured workflows, deep links as well as taxonomy.

**Liz Kushnereit:** So that's also how we keep them all interdependent agents.

**Liz Kushnereit:** We'd keep the existing taxonomy connectors, we'd keep the existing.

**Liz Kushnereit:** Except like I think right now it moves into docs.

**Liz Kushnereit:** We would just move you Know, whatever.

**Liz Kushnereit:** Keep the URL structure moving into whatever the connector is.

**Liz Kushnereit:** Use case.

**Liz Kushnereit:** This is pseo.

**Liz Kushnereit:** So I know this is something that, like, programmatic SEO is something y' all talked about for a while, but this is like a different approach to it that we would take.

**Liz Kushnereit:** So that would be Agents four and then a very specific use case, and then we would build out that page.

**Liz Kushnereit:** Um, there's a lot that this could look like.

**Liz Kushnereit:** It could look like tool comparisons.

**Liz Kushnereit:** It could look like just very specific, like promoting one specific integration.

**Liz Kushnereit:** There's a lot we could do here.

**Liz Kushnereit:** But again, it would still link out to guides, workflows, everything like that to just keep the user, like moving through the system.

**Liz Kushnereit:** And then an entirely new page we'd need to stand up is guides.

**Liz Kushnereit:** So moving away from blogs and then just thinking about how guides relates to all of this and drives traffic.

**Liz Kushnereit:** But yeah, I'll stop.

**Liz Kushnereit:** Any questions so far about how they connect?

**Liz Kushnereit:** No.

**Kaitlin Quimby:** Cool.

**Liz Kushnereit:** Okay.

**Liz Kushnereit:** And then how we break this down.

**Thiago da Costa – Datagridai:** Can you.

**Liz Kushnereit:** Oh, so sorry.

**Thiago da Costa – Datagridai:** Hi, can you hear me?

**Liz Kushnereit:** Hi, Tiago.

**Thiago da Costa – Datagridai:** Yeah, hey.

**Thiago da Costa – Datagridai:** Sorry, I've been like a couple minutes late.

**Thiago da Costa – Datagridai:** I'm just kind of following.

**Thiago da Costa – Datagridai:** Pulling up here and seeing what you have.

**Thiago da Costa – Datagridai:** SEO pages, agent pages.

**Thiago da Costa – Datagridai:** Connect your pages.

**Thiago da Costa – Datagridai:** Yeah, that's cool.

**Thiago da Costa – Datagridai:** Okay.

**Liz Kushnereit:** Yeah, I can.

**Kaitlin Quimby:** I think.

**Liz Kushnereit:** Yeah, you just joined.

**Liz Kushnereit:** Okay.

**Liz Kushnereit:** Yeah.

**Liz Kushnereit:** So it's three lanes of expansion, Guides and PSEO agents and connectors improving through content and ux, especially on agents and connectors.

**Liz Kushnereit:** And so, yeah, this is what that interdependency looks like.

**Liz Kushnereit:** And that taxonomy, PSEO moves into form for specific use case at the agent level.

**Liz Kushnereit:** And then the content strategy is agent based, so each content cluster comes from a specific agent.

**Liz Kushnereit:** And then we build backwards into guides and then also sort of forward into our use case guides.

**Liz Kushnereit:** I think that's all cut up.

**Liz Kushnereit:** And the guide would be our new page that we would stand up.

**Liz Kushnereit:** And then.

**Liz Kushnereit:** So for what this looks like in terms of building it out, phase one is of course, agents.

**Liz Kushnereit:** So this, because this is sort of our, like, spine or the backbone of the entire content strategy, we'd want to think through the prioritization, what this page looks like in terms of, like, what the user would land on.

**Liz Kushnereit:** And so I have a prototype we can walk through.

**Liz Kushnereit:** And I think there's still some more work we can do in terms of ux, but that would be our primary focus just to ensure that we're prioritizing the correct agents and doing our content strategy prediction about, like, which agent we want to go after first or which 10, whatever.

**Liz Kushnereit:** But as soon as we have that.

**Liz Kushnereit:** We can just jump right into phase two, which is Guides and pseo.

**Liz Kushnereit:** So our guides pages would be the new ones.

**Liz Kushnereit:** This is our full funnel informational content.

**Liz Kushnereit:** So this can go, you know, across anything.

**Liz Kushnereit:** It can be something we can still relate to the agent, but it can be a much like higher volume keyword.

**Liz Kushnereit:** And then Programmatic SEO moves more into those use cases at the agent level.

**Liz Kushnereit:** And so we just start building out what that looks like in particular the template for Programmatic SEO and then finally our Connectors marketplace.

**Liz Kushnereit:** So this is needs a bit more fleshing out and so this is like that final enablement phase, like, okay, set up your integration and actually start using it.

**Liz Kushnereit:** I tagged webflow here because we do.

**Liz Kushnereit:** We did a really good job on this for webflow integrations.

**Liz Kushnereit:** It's a bit of a different business model, but we've seen a lot of traffic to these pages.

**Liz Kushnereit:** So up till now I think we've done like 600 pages for them and we're building out a big like interdependency structure for them as well.

**Liz Kushnereit:** But I think there's room to have more fleshed out kind of how to set up your integration content that still captures that high intent traffic.

**Liz Kushnereit:** So we're looking at doing that for connectors and then still having our internal links to move into pre configured workflows or whatever to drive to either guides agents.

**Liz Kushnereit:** Okay, any questions so far before I look at the prototype?

**Thiago da Costa – Datagridai:** No, this, this is exciting.

**Thiago da Costa – Datagridai:** Yeah, great.

**Liz Kushnereit:** Okay, so this is what we put together for agents.

**Liz Kushnereit:** So you'll forgive me because I do think we can build a bit better UX as we actually like if we do a headless cms, what that would look like and how we.

**Liz Kushnereit:** Because it's a bit less SEO and a bit more enablement at least at the agent level.

**Liz Kushnereit:** So this is the landing page for agents.

**Liz Kushnereit:** You click on your deep search agent, you have your chat, some more content about it.

**Liz Kushnereit:** Try this agent.

**Liz Kushnereit:** These can look like they're not clickable now in the prototype, but these can look like pre configured workflows going into, you know, already trying it.

**Liz Kushnereit:** These of course take you to the login wall.

**Liz Kushnereit:** So more content about the agent key capabilities.

**Liz Kushnereit:** I think what I'm hoping, hoping we can get is some kind of sidebar, some sort of stacking either that takes the user directly into their use case like for this use case and then maybe related guides we can still keep in this particular prototype is down here as well.

**Liz Kushnereit:** Common use cases.

**Liz Kushnereit:** This would be like our Programmatic SEO.

**Liz Kushnereit:** So I would probably just Bump this up when we actually launch this.

**Liz Kushnereit:** And then we also have our link into connectors.

**Liz Kushnereit:** So now we go to our connectors page, we take a look at procore.

**Liz Kushnereit:** This is like.

**Liz Kushnereit:** So as I just showed you our webflow integration content, we would look at something more like this.

**Liz Kushnereit:** So we've already developed the content engine for this.

**Liz Kushnereit:** We do like 30 a week output on this.

**Liz Kushnereit:** I don't know that we'll do the same here.

**Liz Kushnereit:** I don't know if that's even needed.

**Liz Kushnereit:** But similarly, we want to flesh out this content and do a bit more optimization about either like guides and more informational content about the usefulness of this integration or also working into use case guides.

**Liz Kushnereit:** These are also could potentially be those pre configured workflows that lead you back into the agent and then yeah, I think some more linking to agents, some set of requirements.

**Liz Kushnereit:** So this would be expanded into actual content and then linking to our related guides.

**Liz Kushnereit:** So in that way we.

**Liz Kushnereit:** And then I'll show you guides as well.

**Liz Kushnereit:** And so this is what our new guides page would look like.

**Liz Kushnereit:** And then we have some CTAs taking us into the agents.

**Liz Kushnereit:** I think we can also explore what we want this to look like because again, it's a little bit more room to play since it's already moving into product enablement.

**Liz Kushnereit:** But yeah, so this is our kind of v1 of the strategy, the infra and then what the prototype UI UX would look like.

**Thiago da Costa – Datagridai:** Okay, cool.

**Marcel Santilli:** Hey Thiago.

**Marcel Santilli:** Sorry, a few minutes later.

**Liz Kushnereit:** Hi.

**Thiago da Costa – Datagridai:** This is great.

**Thiago da Costa – Datagridai:** Okay, look.

**Thiago da Costa – Datagridai:** What do you call a guide?

**Thiago da Costa – Datagridai:** There's a part in there I say like, well, it goes into a guide.

**Thiago da Costa – Datagridai:** What is a guide in that case?

**Liz Kushnereit:** Yeah.

**Liz Kushnereit:** So I would think of guides as basically like blog, but this would be a new page.

**Liz Kushnereit:** We would stand up for full funnel content that moves away from the existing blog page.

**Liz Kushnereit:** There's definitely an open question about what we do with the existing blog page.

**Liz Kushnereit:** Like do we maintain, optimize, refresh and keep that going?

**Liz Kushnereit:** But guides is basically just SEO content that we'd be pushing out based on our agent based content clusters.

**Liz Kushnereit:** Does that answer that?

**Thiago da Costa – Datagridai:** Okay.

**Thiago da Costa – Datagridai:** Okay.

**Thiago da Costa – Datagridai:** Yeah, yeah, yeah.

**Marcel Santilli:** And Tiago, I think like the, the most important thing is the navigational experience and how strongly we cross link things.

**Marcel Santilli:** Right.

**Marcel Santilli:** Is far more important.

**Marcel Santilli:** And also trying to keep a lot of pages relatively flat.

**Marcel Santilli:** And so instead of having slash guide category, slug something else, slash, the actual slug of the page, you keep everything flat and then everything is just like a tag.

**Marcel Santilli:** Right.

**Marcel Santilli:** And then you're dynamically surfacing pages in a Bunch of places.

**Marcel Santilli:** So you create kind of like a.

**Marcel Santilli:** It's really like we're trying to create like we're seeing websites as a knowledge graph for brands, right.

**Marcel Santilli:** And so which case, like, we still need to fill in the gaps of like, all the pages, all the questions people have, all the things that you want to kind of have to both influence the human buyers as well as agents.

**Marcel Santilli:** And training data on your brand is kind of like the mental model there.

**Marcel Santilli:** And then what some of the lessons we learned from like Augment code and a few others is like, creating these additional sections of the site opens up sometimes a lot of opportunities, especially once you kind of go really heavy towards one and you've done hundreds and hundreds and hundreds of pages.

**Marcel Santilli:** Sometimes, like, it helps.

**Marcel Santilli:** So for instance, with Augment, we did a slash tools section of the site, but the template is exactly the same.

**Marcel Santilli:** Yet, like, it.

**Marcel Santilli:** It kind of like really took off, you know, and so it's like a great, great way to kind of like think about it.

**Marcel Santilli:** It's just like opening up like additional places of opportunities, you know?

**Thiago da Costa – Datagridai:** Got it.

**Thiago da Costa – Datagridai:** Got great.

**Thiago da Costa – Datagridai:** Makes sense.

**Marcel Santilli:** And then the only other thing that.

**Thiago da Costa – Datagridai:** I talked about, I don't know.

**Thiago da Costa – Datagridai:** Let's do this.

**Marcel Santilli:** Oh, sorry, go ahead.

**Thiago da Costa – Datagridai:** Yeah, let's do this.

**Thiago da Costa – Datagridai:** I think the only thing I didn't see, or maybe it was in there, is like an uplift on the design of the site overall.

**Thiago da Costa – Datagridai:** Not like a complete change, but iterate on that and improve.

**Thiago da Costa – Datagridai:** You had some criticism on this, so I assume you had an opinion.

**Thiago da Costa – Datagridai:** So would love for you guys to take over some of that.

**Marcel Santilli:** Yeah, for sure.

**Marcel Santilli:** And like, just to kind of show you a little bit, like with Augment, right.

**Marcel Santilli:** Like, this is not how it looked when we first started, you know, and, and so, like, there's a lot of improvements I think we can make on the individual page.

**Marcel Santilli:** And Augment is a great example of like, they started out as like, you know, dark mode everywhere, but overall I think there's ways for us to still keep like a dark feeling in places, but then the core content, like, improve the legibility and readability of the content itself, you know, and so we have like several, like, kind of examples of that.

**Marcel Santilli:** And so anyways, like, that's what we talked about.

**Marcel Santilli:** I gave the team a heads up and we're pulling in our design and dev to quickly scope it out.

**Marcel Santilli:** But the main lift here is, which is what I would recommend is we create the surface area in the fastest way possible to start getting those sections created.

**Marcel Santilli:** Right.

**Marcel Santilli:** And the content calibrated and things Kind of start to get indexed and then in parallel with the additional work stream, we take over and redo the website outside of webflow because then that will really, really ad speed.

**Marcel Santilli:** Like, I mean, we can spin up sites in, you know, once we agree on like the look and feel and design.

**Marcel Santilli:** And as long as we're not rebranding the company, obviously, right?

**Marcel Santilli:** Like, it's not a rebrand, it's like a facelift, if you will, an improvement overall to the experience.

**Marcel Santilli:** Like, we can move really, really, really fast and it would be way easier for us to maintain with coding agents and design engineers in the loop than us, you know, dragging and dropping shit in webflow like we talked about.

**Marcel Santilli:** So.

**Marcel Santilli:** So as long as you're cool with that in parallel, we'll start that work.

**Marcel Santilli:** But we didn't want to block that way for defining that work and adding a tiny little bit of scope there and going through whatever pro course process is from the team just starting to deliver value immediately.

**Thiago da Costa – Datagridai:** Awesome.

**Thiago da Costa – Datagridai:** Okay, so if you guys can repeat what the.

**Thiago da Costa – Datagridai:** Just summarize, what's the.

**Thiago da Costa – Datagridai:** How much work are you taking off workplace you're building?

**Thiago da Costa – Datagridai:** You're basically taking over most of the website, right?

**Marcel Santilli:** The what we're proposing taking over and redesigning the.

**Marcel Santilli:** Or refreshing the entire website out of webflow.

**Marcel Santilli:** Refactoring the entire website out of webflow and in that process redesigning essentially the pages to be best practices.

**Marcel Santilli:** And so like, and then at that point you have a repo that anyone else can do changes to.

**Marcel Santilli:** Right?

**Marcel Santilli:** Like, but where ideally drawing the line here is that we're not taking on product marketing work and we're not taking on like, hey, update our homepage after that.

**Marcel Santilli:** Like, we're porting everything over to a better place and facelifting the sections of the content that we're going to own.

**Marcel Santilli:** And then that will set you up for then any dev and any designers which we can recommend them to to then like spend weeks with you redesigning the homepage if you want or you know, creating a more a cooler animation for your product pages.

**Marcel Santilli:** Like that's the work you can't take on, you know, just because it's like a, it's a black box.

**Marcel Santilli:** And then you never know people, you know, there might be millions of iterations and things like that and then just like a huge suck for us, but at least we're going to unlock you to in the future.

**Marcel Santilli:** You know, any design can be implemented way easier and you can prototype directly in cursor or whatever you're using, you know, and it Just makes it super easy for you to use our components however you want to, you know.

**Thiago da Costa – Datagridai:** Great.

**Thiago da Costa – Datagridai:** Awesome.

**Thiago da Costa – Datagridai:** Okay.

**Thiago da Costa – Datagridai:** It makes a ton of sense.

**Thiago da Costa – Datagridai:** One of the things we're going to want to do is to connect our product to this experience or like embed our product in some degree.

**Thiago da Costa – Datagridai:** So that's something we are working on that I think will be, will be, will be cool to do here because I saw you have some, you know, some like input boxes and so on.

**Thiago da Costa – Datagridai:** We'd like it to be just like the data grid app at that point that gets embedded.

**Thiago da Costa – Datagridai:** And so it's like always the same design system, always the same look, you know, integrating the page, but like really the app piece and how we talked.

**Marcel Santilli:** About was we are using our API to programmatically create agents.

**Marcel Santilli:** And agents are, you know, contact instructions, potentially data sets and tools, right?

**Thiago da Costa – Datagridai:** Yeah.

**Marcel Santilli:** And then from there like it's essentially almost like a package.

**Marcel Santilli:** So if someone is in an experience, you are using the API and then if they click on anything, it essentially will create the environment and use the API to add that agent to their environment, essentially fork that agent, right?

**Marcel Santilli:** Is that like.

**Marcel Santilli:** That's how I remember, but I could be wrong because we talked about a lot of things, no, yeah, exactly.

**Thiago da Costa – Datagridai:** It's like a kit, right?

**Thiago da Costa – Datagridai:** Like you have like knowledge, some attachments, a bunch of instructions, the configuration of the agent, what's on, what's off, the planning instructions, and you can call the API to create that object and push all the associated data sets and knowledge so that the user can get started with something.

**Thiago da Costa – Datagridai:** So like one example would be like a safety agent for California and it would be like OSHA safety standards, right?

**Thiago da Costa – Datagridai:** And like there's a document in there, there's like the OSHA safety standards that are already like PDF attached or whatever.

**Thiago da Costa – Datagridai:** So you know, things like this that will kick it off quickly.

**Marcel Santilli:** Liz, what we can do, perfect, the guides or one of the sections can hold a lot of the quote unquote files, you know, like.

**Marcel Santilli:** So for instance, like a guide to like OSHA compliance in California or whatever, like whatever Safety compliance in California, for example.

**Marcel Santilli:** And that's like truly an in depth guide.

**Marcel Santilli:** And there could even be like files from there and then the agents will not only relate to that, but can also pull from, from that maybe like we'll think through it, but that way everything like, like we're, we're approaching it truly like a knowledge graph that we're building that will also accelerate time to value for your actual users, right?

**Marcel Santilli:** Tiago?

**Marcel Santilli:** So it's not only a way to capture a ton of traffic and AI visibility and get mentioned but.

**Marcel Santilli:** But it's also like a way for, to accelerate the time to value and that's what we're seeing with like lovable.

**Marcel Santilli:** The templates like they have double digit conversions, you know, and activations from.

**Marcel Santilli:** From that because it's just like it's what they were thinking of building anyways, you know.

**Thiago da Costa – Datagridai:** Yeah.

**Marcel Santilli:** Awesome Liz.

**Marcel Santilli:** Amazing work.

**Marcel Santilli:** Liz and team worked their butts off to like.

**Marcel Santilli:** I know it's like we didn't even cover the whole thing but it was like really, really thoughtful and in depth and you know, and so we care deeply and I told the team like Liz is our best so it's like whatever we need to do to knock it out of the park for you all.

**Kaitlin Quimby:** Yeah, it looks great.

**Marcel Santilli:** Awesome.

**Marcel Santilli:** Cool.

**Marcel Santilli:** Thanks team.

**Marcel Santilli:** We'll follow up soon.

**Kaitlin Quimby:** Thanks a lot.

**Kaitlin Quimby:** Okay, great.

**Liz Kushnereit:** Thank you.

**Kaitlin Quimby:** Bye all.

**Thiago da Costa – Datagridai:** Thank you.

**Kaitlin Quimby:** The recording has stopped.
