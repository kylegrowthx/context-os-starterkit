# Clerk Kick Off

<metadata>
date: 2025-08-04
time: 18:00 UTC
duration: 66 minutes
organizer: Marcel Santilli
participants: Marcel Santilli, Kyle Gaudreau, George Haikal, Alex Rapp, Brian Morrison II, Nick Parsons
fathom_recording_id: 78316861
fathom_url: https://fathom.video/calls/369278957
share_url: https://fathom.video/share/8PGnLqzxbVzmBFgy1WK1Mu1dbJEgb7dA
source: fathom
enriched_on: 2026-03-03 04:08 UTC
speaker_note: "Board Room" device label in transcript refers to Marcel Santilli, the call organizer and GrowthX representative.
</metadata>

---

## Summary

Clerk (developer authentication/security platform) and GrowthX kicked off their engagement focused on content strategy and AI-driven growth. Clerk aims to increase signups attributed to AI engines from 1% to 10%+ and is tackling challenges around limited team bandwidth (4 people), proving blog ROI, and attribution in LLM-driven traffic. GrowthX will conduct a dense learning period analyzing Clerk's data, competitive landscape, customer personas, and content opportunities — with weekly syncs, product deep dives, and customer analysis planned.

---

## Context

Clerk is a developer-focused authentication and user management platform competing in a crowded space against Auth0, WorkOS, Stytch, FusionAuth, and Firebase. The company differentiates on developer experience (DX), pre-built components, and security, with particularly praised documentation. Alex Rapp leads growth marketing and recently reconnected with Marcel Santilli at GrowthX to explore how content and AI visibility initiatives could accelerate adoption. This kick-off call included Brian Morrison, Clerk's director of marketing and senior developer educator, who owns blog content and co-marketing partnerships with other developer tools. The meeting represented the start of a focused engagement to identify content gaps, competitive opportunities, and AI-driven growth tactics.

---

## Relevance

### To GrowthX Delivery
- Clerk's developer-first motion and DX focus align with CheckThat's AEO capabilities and AI visibility work
- Opportunity to apply GrowthX's content strategy and competitive analysis methodologies to a high-growth technical audience
- Four-person team at Clerk means content solutions must be efficient and directly tied to measurable growth

### To CheckThat
- Clerk is already experiencing meaningful inbound traffic from LLM/AI engines but struggling with conversion attribution — core CheckThat use case
- Testing opportunity for CheckThat to quantify LLM-driven signups and help Clerk optimize decision-maker vs. implementer messaging
- Competitive threat from open-source BetterAuth underscores importance of visibility in AI search results

### To GrowthX Business Development
- Well-positioned customer: Clerk is VC-backed, growth-focused, has budget for content and strategy work, and sees content/AEO as strategic
- Potential for expanding scope into customer/product research, YouTube/open-source partnership strategy, and ongoing performance tracking
- Strong reference potential — Clerk's growth marketing team is influential in DevTools ecosystem

---

## Overview

- Clerk seeks to leverage LLMs for growth, aiming to increase signups attributed to AI engines from 1% to 10%+
- Key challenges: limited bandwidth (4-person team), difficulty proving blog ROI, and attribution issues with LLM-driven traffic
- Focus areas: improving AEO/SEO, YouTube partnerships, open source collaborations, and B2B-focused content

---

## Key Topics

### Clerk's Current Growth Initiatives

  - Core channels: Organic search, YouTube partnerships, AEO, open source partnerships
  - Supplementary channels: Paid social, newsletters, events, co-marketing with DevTools
  - Recent test: B2B SaaS multi-tenancy content series (generic to Clerk-specific)
  - Docs praised for comprehensiveness and ease of navigation

### Competitive Landscape

  - Main competitors: Auth0, WorkOS, Stytch, FusionAuth, Firebase
  - Emerging threat: BetterAuth (open-source, growing "cult following")
  - Differentiation: DX/UX focus, pre-built components, security emphasis

### Customer Personas and Pain Points

  - Three core personas: Developers (React-focused), early-stage startups, AI builders
  - Pain points: Data ownership concerns, pricing objections, integration complexities
  - Strength: Positive developer experience, comprehensive documentation

### LLM Strategy and Challenges

  - Inbound LLM traffic growing rapidly, but conversions lag (1% of signups)
  - Hypothesis: Decision-makers research via LLMs, delegate implementation
  - Challenge: Proving ROI and attribution from LLM-driven traffic

### GrowthX Collaboration Approach

  - Weekly recurring calls, product deep dives, and customer analysis planned
  - GrowthX to access Clerk's data (BigQuery, Hex, Elastic) for insights
  - Focus on dense learning period to inform content strategy

---

## Action Items

**Alex Rapp (Clerk)**
- Send GrowthX team article about YouTube partnerships process (from Gonta)
- Share content backlog with GrowthX team
- Provide GrowthX access to relevant data (BigQuery/Hex exports, Elastic sample data)
- Send initial resources to GrowthX team before Thursday

**Marcel Santilli (GrowthX)**
- Set up weekly recurring calls with Clerk team starting next week
- Schedule product deep dive and customer deep dive meetings with Clerk team

---

## Transcript
**Marcel Santilli:** It's a short week for me, so.

**Marcel Santilli:** Oh, snap.

**Marcel Santilli:** What are you up to?

**Alex Rapp:** My wife and I are about to hit 10 years at the end of this month, and we're just taking a little staycation earlier in the month, so.

**Marcel Santilli:** Oh, that's awesome.

**Marcel Santilli:** You have kids, I see the drawing on the wall?

**Alex Rapp:** Yeah, that's what I was about to say.

**Alex Rapp:** Both kids go back to school next week, so trying to get it in before all that chaos.

**Marcel Santilli:** How old are your kids?

**Alex Rapp:** Four and six.

**Marcel Santilli:** Nice, nice.

**Marcel Santilli:** I have a two-year-old, so you're pro-level already, I know.

**Marcel Santilli:** Two kids, four and six.

**Alex Rapp:** Definitely not at a pro-level.

**Alex Rapp:** We'll just call it surviving.

**Marcel Santilli:** Yeah, yeah, pretty much.

**Marcel Santilli:** I feel like that's every parent, pretty much.

**Marcel Santilli:** Funny enough, my wife went out of town with...

**Marcel Santilli:** Our daughter to visit her family in Michigan, so I'm like solo for two weeks, and it's like really weird, you know, like working late every day, like, oh, what should I do now?

**Alex Rapp:** This is what life was like before kids.

**Marcel Santilli:** Yeah, exactly.

**Marcel Santilli:** yeah, exactly.

**Alex Rapp:** That's pretty weird.

**Marcel Santilli:** But Brian, good to see you.

**Marcel Santilli:** How's it going?

**Marcel Santilli:** Doing well.

**Brian Morrison II:** Pleased to meet the gentleman.

**Marcel Santilli:** Likewise, likewise.

**Marcel Santilli:** Likewise.

**Marcel Santilli:** Well, yeah, I invited Brian.

**Alex Rapp:** So Brian is our senior dev educator, or, you know, as he pointed out in some documentation somewhere else, that he's now the director of marketing and clerk.

**Alex Rapp:** But anyways, Brian does the heavy lifting on all the content that you see on our blog, you know, works with a lot of the other dev tools that we like to do co-marketing with, you know, helps create, you know, project templates.

**Alex Rapp:** It's, I mean, he doesn't.

**Alex Rapp:** That's a lot, but really, I figured it would be good to have him in these conversations so he can obviously contribute to any insights or due diligence questions that you guys have just in terms of really anything.

**Alex Rapp:** But I also think, you know, the output that you shared with Nick and I, the sample output, I think that would be of immense value for him to just to, you know, find opportunities for, you know, human, you know, continuing human authored work as well.

**Marcel Santilli:** Yeah, that's amazing.

**Marcel Santilli:** Well, with that, should we do just the super quick?

**Marcel Santilli:** I know some of us already met and whatnot, but Alex, you mind just doing a quick background intro and then Brian may be the same and then we can do a super quick one on our hand as well just to set context a little.

**Alex Rapp:** Yeah, yeah, no problem.

**Alex Rapp:** Alex Rapp, I lead growth marketing here.

**Alex Rapp:** I've been here for almost two years now.

**Alex Rapp:** And my main goal is basically finding initiatives, channels, experiments, however you want to label it, that essentially drive awareness and adoption slash acquisition of Clerk and ensuring that the audience that we bring is a qualified audience as well.

**Alex Rapp:** So those are my goals in AEO and content opportunities is something that is sort of paramount for us right now, which is why I reestablished comms with Marcel over here.

**Marcel Santilli:** I love it, man.

**Marcel Santilli:** I am so, so pumped.

**Marcel Santilli:** I've been looking forward to this day.

**Marcel Santilli:** Brian, I would love to hear a little bit on you as well, your journey, your background.

**Brian Morrison II:** Yeah, sure.

**Brian Morrison II:** My name is Brian Morrison.

**Brian Morrison II:** I'm senior dev ed at Clark.

**Brian Morrison II:** So my main responsibility at Clerk is producing content as well as finding other potential dev tool partner companies for us to partner with for content creation.

**Brian Morrison II:** I interact with a lot of our users on Twitter and different social media networks just to find what types of topics resonate with those people and ultimately produce the content.

**Brian Morrison II:** Before being in dev ed or dev marketing, I was a software developer.

**Brian Morrison II:** I've been infrastructure for a logistics company across the U.S.

**Brian Morrison II:** I've been in tech for about 15 years now, holding multiple different titles and roles and stuff across the way.

**Brian Morrison II:** Yeah, so that's a little background around me.

**Marcel Santilli:** Love it, man.

**Marcel Santilli:** I'll go super quick, but CEO here at GrowthX, been at a lot of different technical companies throughout my career, like IBM and HP Software.

**Marcel Santilli:** I was at HashiCorp as well, and so fairly familiar in terms of content and different initiatives for dev.

**Marcel Santilli:** so on so so

**Marcel Santilli:** So I feel like that because of my background in that area, I think I'm going to say more than half of our customers are technical audiences.

**Marcel Santilli:** So we keep getting better and better, I think, at it.

**Marcel Santilli:** And so always exciting to pick off a new one.

**Marcel Santilli:** And just a quick high level on growthx.

**Marcel Santilli:** Like we're almost at 50 customers.

**Marcel Santilli:** We're about 72 people right now.

**Marcel Santilli:** And our teams are split between build and delivery.

**Marcel Santilli:** So you have about like 40 or so people on the delivery side.

**Marcel Santilli:** And we're in the delivery side.

**Marcel Santilli:** have two different teams.

**Marcel Santilli:** And one is the strategy sprint teams, which, you know, we're part of.

**Marcel Santilli:** And then you have the rest of the delivery team.

**Marcel Santilli:** And they report up to our chief content officer who ran TechCrunch.

**Marcel Santilli:** And then you also have directors and managing editors.

**Marcel Santilli:** And so like all, like we have a lot of supporting functions, you know.

**Marcel Santilli:** And so this will hopefully feel like a white glove.

**Marcel Santilli:** We got no treatment, but we also try to move insanely fast, so buckle up, you know.

**Marcel Santilli:** Love it.

**Marcel Santilli:** We'll adapt to companies, you know.

**Marcel Santilli:** I think you'll probably be in the woods that move faster.

**Marcel Santilli:** So super excited, but I'll let George take a quick intro, too.

**Marcel Santilli:** Yeah, I'll be very quick.

**Marcel Santilli:** Good to be both.

**Marcel Santilli:** I'm the chief of staff here.

**Marcel Santilli:** Help with a bunch of different things, but with the strategy sprints, specifically every new client.

**Marcel Santilli:** And helping pull in all the people Marcel just mentioned we have on the delivery side, figuring out what you all need to be most successful, how we can help, and then pulling everyone and everything needed together to make that happen.

**Marcel Santilli:** So you'll be hearing from me a lot the first two or three weeks of this engagement to make sure, you know, both sides of all the materials, people, et cetera, and then I'll be here along the way, you know, forever, hopefully.

**Marcel Santilli:** So really good to meet you guys, and I'm excited to get this kicked off.

**Marcel Santilli:** So we can jump right in.

**Marcel Santilli:** George, if you don't mind sharing your...

**Marcel Santilli:** Yeah, I just sent the agenda in this chat as well.

**Marcel Santilli:** You both should have access to our notion to follow along, too.

**Marcel Santilli:** Cool.

**Marcel Santilli:** And we'll code drive here.

**Marcel Santilli:** George will ask a lot of the questions.

**Marcel Santilli:** I'll jump in as well.

**Marcel Santilli:** And so this is really kind of like free form.

**Marcel Santilli:** These questions are more just to guide us, but depending on kind of how it goes, when I double-click on certain areas, jump around a little bit, you know, so this is really us coming in and trying to figure out what we don't know and understand what's driving things.

**Marcel Santilli:** George?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** For sure.

**Marcel Santilli:** So before we jump in, I'll just do a quick little demo of the workspace.

**Marcel Santilli:** how we work is through Slack and Notion.

**Marcel Santilli:** We're happy to, you know, email any other way to get in touch with your team, but just a really quick high-level.

**Marcel Santilli:** Everything we do works out of this Notion workspace.

**Marcel Santilli:** So documents, any artifacts, documents we add, update, materials we get from you all.

**Marcel Santilli:** Anything pending review, ping you on Slack, but we'll also have it all updated here, so it's very easy to look at, review, leave comments on, and then every meeting we have will be logged here in this section, including the first one, our kickoff meeting.

**Marcel Santilli:** Any deep dives we want to do, which we love, like jumping in on the product, really getting an understanding of how that works, customer deep dive, et cetera, these will all be here with the agenda notes.

**Marcel Santilli:** So we try to make it as easy as possible to save you all the time and to have everything in one place.

**Alex Rapp:** Yeah, love it.

**Alex Rapp:** In terms of Slack, are we just going to use our existing channel, I'm assuming?

**Marcel Santilli:** Yeah.

**Alex Rapp:** Yeah, that makes the hard one.

**Alex Rapp:** Yep.

**Marcel Santilli:** Cool.

**Marcel Santilli:** Yeah, and think of it as like anything you want to throw over the fence, throw it over the fence on Slack, you know, not a problem, don't worry too much about where should I put this or that, like we'll process it, we'll put it in the right place, like the homework, put all the homework on us.

**Alex Rapp:** Sounds good.

**Marcel Santilli:** Amazing.

**Marcel Santilli:** So, I mean, before we start, like the way out.

**Marcel Santilli:** I like to think about this with clients the way we like to, is thinking of this next hour as, you know, we don't know what we don't know.

**Marcel Santilli:** And so we want to get all that information, the expertise, the context from you all.

**Marcel Santilli:** And like this call is not the only time we're going to be asking for that.

**Marcel Santilli:** The next one or two weeks, we're going to be diving, you know, experts at the company to really understand all the nuances to get our inputs right.

**Alex Rapp:** Yep.

**Marcel Santilli:** That ultimately leads to the output.

**Marcel Santilli:** So that's how we think about it.

**Marcel Santilli:** Some of the questions are broad by design, but we start there and then drill down.

**Alex Rapp:** Sounds good.

**Marcel Santilli:** Amazing.

**Marcel Santilli:** With that, help us understand, you know, what's driving this engagement now?

**Marcel Santilli:** What's pushing you towards this?

**Alex Rapp:** What keeps you up at night?

**Alex Rapp:** Yeah.

**Alex Rapp:** All right.

**Alex Rapp:** So engagement is sort of a open-ended word.

**Alex Rapp:** When you're asking what's driving engagement, are you saying what's driving, you know, our interest in GrowthX?

**Alex Rapp:** Or are you saying what's – okay, gotcha.

**Alex Rapp:** So we –

**Alex Rapp:** Obviously, as everybody else has, have identified, you know, the power that can be unlocked with LLMs as growth channels.

**Alex Rapp:** You know, we've seen, you know, companies that, you know, are widely admired across our entire org do it really well and put best practices in place.

**Alex Rapp:** But I think the thing that is, you know, the biggest barrier for us is, you know, A, we only have, you one person writing content for us, Brian.

**Alex Rapp:** And, and B, you know, a lot of the, a lot of the tooling that we've, you know, looked at using to supplement a, you know, automated workflow for, you know, various pieces of the content generation lifecycle have faltered one way or another.

**Alex Rapp:** You know, you know, we've had lots of issues in, in errors and haven't received.

**Alex Rapp:** A lot of support from Aerofs in terms of being able to set up automated workflows that we feel are strong.

**Alex Rapp:** I'm still going to be pursuing that while we work with you all just so that we don't slow down and we can continue to put content out there and test it and see how it does.

**Alex Rapp:** But we know that we've seen the ability to grow with traffic coming from LLMs already.

**Alex Rapp:** In the first six months of the year, our signups grew by about close to 9% that were attributed to LLMs and inbound traffic grew by 4X.

**Alex Rapp:** But, you know, even more so recently, it has started to eclipse inbound traffic that we get from search engines as well.

**Alex Rapp:** So, you know, traditional SEO.

**Marcel Santilli:** Just to play it back with what just said, what we're saying is that...

**Marcel Santilli:** Total traffic 9% comes from LLMs, or sorry, total sign-ups 9% are from LLMs, or are you saying?

**Alex Rapp:** No, sorry.

**Alex Rapp:** No, yeah, from January to June, our monthly inbound traffic for coming from LLMs that we can attribute back to LLMs, that grew by, you know, anywhere from 3% to 4%, and the attributable sign-ups grew by 9%, still a very low number, I would say, which, you know, we have a hypothesis that there is a attribution.

**Alex Rapp:** Not issue, but, you know, there's an attribution, you know, aspect at play.

**Alex Rapp:** But, you know, at the same time, organic search has been, you know, one of our top growth levers.

**Alex Rapp:** You know, it's how a lot of users find us, and we can obviously see the value in pushing on, you know, AEO that also contributes to improved SEO.

**Alex Rapp:** You know, even while we...

**Alex Rapp:** You know, kind of take more of a traditional SEO approach, you know, in a completely different swim lane.

**Alex Rapp:** So, you know, that's what's really driving this engagement is increased velocity behind content for LLMs and also, you know, for human consumption as well.

**Alex Rapp:** And I think the other thing too is that, you know, we've gone down a number of different avenues to identify content opportunities, you know, whether they're gaps or underperforming content or, you know, I guess those are probably the two biggest new areas that we've really looked into to try to find a systematic approach for, you you know, driving, you know, content or, you know, other, other aspects that could inform, you know, our other growth channels or even improvements on our website.

**Alex Rapp:** So, you know,

**Alex Rapp:** Really what we see here is not so much an engine that can help drive LLM as a growth channel, but something that can inform all of our efforts across the other areas that we're pushing on.

**Marcel Santilli:** Yeah, that's perfect.

**Marcel Santilli:** By the way, I don't know if you saw, but I did a workshop on Friday.

**Alex Rapp:** I did.

**Alex Rapp:** I wanted to participate, but I didn't have the time on Friday.

**Marcel Santilli:** All good.

**Marcel Santilli:** We're just finishing editing.

**Alex Rapp:** It's two hours, and I'll send it to you guys.

**Marcel Santilli:** Awesome.

**Marcel Santilli:** Just in case, I promised it was super packed.

**Marcel Santilli:** It wasn't like two hours of BS.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And just because there's a lot of stuff that I'm tempted to jump in and show you and talk about, that is super relevant to everything you're saying.

**Marcel Santilli:** But I think like that, I'll send it over, but this resonates a lot, everything you're saying.

**Alex Rapp:** Cool.

**Marcel Santilli:** Please help me understand a little more.

**Marcel Santilli:** You said you're still...

**Marcel Santilli:** But then to be in and playing around with Aerobs, help me understand some of the things you were trying to do that weren't working with Aerobs and what you weren't super happy with and then the things that you're still going to continue to do in that.

**Alex Rapp:** Yeah, so basically what I did is I basically tried to replicate recurring workflows that we are running manually in-house right now and do so in a way that is obviously focused on our target personas and with a look and feel of our brand.

**Alex Rapp:** And, you know, just ensuring that there's brand fit, you know, things of that nature is cross channels.

**Alex Rapp:** You know, we're using it to, you know, help automate a lot of scouting that we're doing for external partners across various channels.

**Alex Rapp:** You know, we're taking a shot at using it for, you know, identifying, you

**Alex Rapp:** Content gaps in SEO improvements, we're using it for suggestions around, you know, upper funnel sponsored campaigns like paid social, newsletters, things of that nature.

**Alex Rapp:** And, you know, also using it just as a sort of a fact checking or a polishing mechanism for content that, you we may be producing in other automated areas, whether it's LLMs or, you know, we've also been exploring NAN as well.

**Alex Rapp:** So, you know, we're kind of using it across a very broad spectrum, using it to extract insights and opportunities, and also trying to, you know, expedite a lot of our manual trigger workflows, I think is the easiest way to sum it up.

**Marcel Santilli:** Respect sounds.

**Marcel Santilli:** And for that, I'm assuming you have a lot of instructions, documents, prompts, etc.

**Marcel Santilli:** Like, so when you say...

**Marcel Santilli:** Fact-checking and polishing, me, I hear like writing guidelines, style, tone, brand, audience, personas.

**Marcel Santilli:** Yeah.

**Alex Rapp:** Sorry, go ahead.

**Marcel Santilli:** I was going to say, would love any and all materials that you have.

**Alex Rapp:** Yeah, definitely.

**Marcel Santilli:** Yeah, the opposite time when we're getting to work, doing our research and then creating our own workflows and pipelines.

**Alex Rapp:** Yeah, think, you know, the biggest issue is I look back and realize I spent two weeks on, you know, trying to fine tune workflows and still wasn't happy with the output.

**Alex Rapp:** You know, whether it was technical issues in terms of specific blocks or steps, you know, such as iterations and, you know, exporting to, you know, our external tooling like Notion or even just Google Sheets we had issues with and, you know, we're still having issues there.

**Alex Rapp:** Or whether it was...

**Alex Rapp:** You know, just tone and perspective didn't really feel as though, you know, we were getting closer to, you know, sort of the degree of polish that our CEO, you know, expects of us in terms of anything that we put out there with the clerk label on it.

**Alex Rapp:** You know, after spending the weekend really, you know, kind of stepping back outside of the tooling and taking what I've learned, I've started to, you know, sort of piece together a, you know, what the blueprint of a workflow would be in my mind in terms of all the, you know, the inputs, the, you know, sort of the narration guidance, as well as the, you know, the editing aspects of it as well.

**Alex Rapp:** And then, you know, obviously we would then use that output to inject, you know, human elements into it just so it doesn't seem as though it, or it's not so apparent that it was, you know, written by LLM.

**Marcel Santilli:** So.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Sorry, selfishly, I feel like this is our bread and butter, so I'm getting super excited just hearing the pain points and the struggles because, you know, that's what the company was built off of in some degree, like right when it started.

**Alex Rapp:** So, yeah, I think that's the other driving factor around the engagement, too, is that we're a small team.

**Alex Rapp:** We're, you know, calling us a group of five is probably going out on a limb.

**Alex Rapp:** You know, there's really, you know, four core members.

**Alex Rapp:** We have one contract partner that's doing video content and then a design resource that sort of sits between us and design.

**Alex Rapp:** But outside of that, it's myself, Nick, who you met, Brian, and another growth marketing lead.

**Alex Rapp:** But we're hoping to add more heads to the team to allow us to be able to increase velocity of our own experimentation and initiative, so.

**Marcel Santilli:** What's your current output like?

**Marcel Santilli:** Like increased velocity from what and then, you know, to what?

**Alex Rapp:** Yeah, so we'd like to go deep.

**Alex Rapp:** We're on channels that we know, you know, we see a really strong signal from.

**Alex Rapp:** So there's a lot of additional exploration, tinkering, and support given to those existing channels.

**Alex Rapp:** And our aim is to ship at least two new data-driven or signal-driven experiments per week.

**Alex Rapp:** And we don't really have a target in mind in terms of actual, you know, growth activities that are out in the community.

**Alex Rapp:** But we know that we want to grow it by, we want to grow monthly volume by, you know, 25 to 50% each month throughout the end of the year.

**Alex Rapp:** And really just have a well-oiled machine that's always on.

**Marcel Santilli:** That's great, that's really helpful.

**Marcel Santilli:** Is there any pressures or any goals that I'm missing before we kind of put a pen in this for later?

**Alex Rapp:** I don't think so.

**Alex Rapp:** We've had really steady.

**Alex Rapp:** Growth in terms of acquisition, you know, month over month, we've hit a bit of a plateau in terms of, you know, step growth, but that's to be expected, especially at the stage that Clerk is at.

**Alex Rapp:** And, you know, I know, well, at least Marcel, know that, you know, Gonta, you know, we've had, he, you he's an advisor for us and, you know, somebody that is good friends with Nick, you know, he's, he's kind of tempered us and said, you know, it's extremely hard to achieve step growth, especially at the stage that you're at.

**Alex Rapp:** And, you know, the sort of what is being asked of us by our investment board, you know, is, is somewhat, you know, new frontier, I guess, is, is a good way to put it in terms of, you know, companies that are like us.

**Alex Rapp:** But it's not to say that we're not going to take a swing and try our best to get there.

**Alex Rapp:** So, you know, that, that's really.

**Alex Rapp:** Another core aspect of what's driving this is to, you know, get our acquisition averages or our baseline, you know, up to where I hope to be.

**Marcel Santilli:** Cool.

**Marcel Santilli:** Amazing.

**Marcel Santilli:** Okay, this is great.

**Marcel Santilli:** so what we do on the content side is, you know, speaking to the audience and their pains and their struggles.

**Marcel Santilli:** So help me understand, you know, if we talk to your three best customers, it doesn't have to be the biggest, just the best, whose problem you're solving the best.

**Marcel Santilli:** What are they going to say you're good at?

**Marcel Santilli:** What do they like about you?

**Alex Rapp:** How are you helping?

**Alex Rapp:** Sure.

**Alex Rapp:** Brian, feel free to chime in here as well.

**Alex Rapp:** You know, I think, you know, the core value propositions of Clerk are the, you know, the heavy focus on DX and UX.

**Alex Rapp:** You know, aside from speed and simplicity.

**Alex Rapp:** study.

**Alex Rapp:** We want to ensure that the developers that are using Clerk have a very positive experience.

**Alex Rapp:** If they run into roadblocks, they're easily solved through the variety of resources that we provide, including our docs, our support channels, and to a lesser degree in terms of where we focus is the community itself, leaning in and providing resources there.

**Alex Rapp:** You know, what really kind of helps set us apart from competitors is the fact that we have pre-built components for authentication, user management, billing, and, you know, even the individual user from that perspective, being able to manage their own profile and customize it, you know, based on, you know, their desired user experiences.

**Alex Rapp:** You know, that's one big thing.

**Alex Rapp:** The other...

**Alex Rapp:** Aspect of that as well is, you know, the fact that we don't focus just on authentication, you know, Colin, the RCO, his vision is really to make this, you know, down the road, a user-centric platform that solves issues for, you know, our core target personas, you know, with anything that has to do, or sorry, anything that has to do with the user itself.

**Alex Rapp:** You know, so while authentication was really the origin of Clerk, it, you know, Colin's vision is it's much further beyond authentication, you know, where authentication is, you know, can be more or less a necessary evil, obviously, you know, for anybody that's building an application that where they're going to have users, but, you know, it's not always the sexiest thing.

**Alex Rapp:** So, you know, so, that's why there's, there's prospecting into areas such as, you know, billing, e-commerce.

**Alex Rapp:** And other aspects of that.

**Alex Rapp:** So I don't know if you want to add anything to that, Brian.

**Brian Morrison II:** I would echo a lot of that, especially around the DX and the implementation side of things, since we are kind of an all-inclusive package when developers are first, especially when developers are first starting to get their applications up and running.

**Brian Morrison II:** One of the other things I'd say is we put a heavy emphasis on security and sensible defaults.

**Brian Morrison II:** So when we build our components, there's a lot of thought that goes into how these things should not only look and behave out of the box, but making sure that everything is built securely as best as possible, down to the point that we even support a method of pushing out security updates to our clients, even without requiring the developer to actually update the dependencies that they haven't implemented in their application.

**Brian Morrison II:** So security is a huge focus.

**Brian Morrison II:** And then I would say one of the phrases that I've heard tossed around, I can't remember when or where, but I've heard somebody say that Clerks' kind of ultimate goal is to

**Brian Morrison II:** Help founders build products better, faster, stronger.

**Brian Morrison II:** And that's, I would say, is probably the North Star of where the company is heading to.

**Brian Morrison II:** With, like Alex said, authentication was kind of just the first step to get in the door.

**Brian Morrison II:** And then beyond that, we will continue to grow into that vision.

**Alex Rapp:** Yeah, think the easiest way to sum that up is, you know, we're building this so that, you people that are building startups can just drop it in and not have to worry about authentication and user management.

**Alex Rapp:** So that way they can focus on actually building out their core application as opposed to, you know, the more utility aspects of their application.

**Marcel Santilli:** And kind of along those lines, right, like what, within the audience of your best customers, the times you all lose.

**Marcel Santilli:** Customers or lose prospects that don't become customers?

**Marcel Santilli:** Are there themes of SSL UI?

**Marcel Santilli:** Yep.

**Alex Rapp:** Let's see.

**Alex Rapp:** You know, so let me start by, you know, giving you insight into another area.

**Alex Rapp:** So we have three sort of pillars or, you know, buckets of core personas.

**Alex Rapp:** You know, the foundational one is developers, right?

**Alex Rapp:** Like, Clerk was specifically built for developers, you know, more specifically front-end or full-stack developers building with React.

**Alex Rapp:** You know, we have SDKs that support a number of different frameworks.

**Alex Rapp:** But, you know, at the end of the day, you know, React frameworks are the ones that we are most focused on because those are the ones that are most popular.

**Alex Rapp:** Those are the ones that, you know, most developers are building with.

**Alex Rapp:** The second cohort is the one that Brian mentioned.

**Alex Rapp:** It's early stages.

**Alex Rapp:** Startups, founders, could be CTOs, it could be a technical founder.

**Alex Rapp:** They're looking for solutions to allow them to ship faster and, like I said before, focus on core aspects of their application.

**Alex Rapp:** The third bucket should be no surprise, but it's AI builders.

**Alex Rapp:** And really, there's two different personas within that.

**Alex Rapp:** There is the developer, you know, the seasoned developer that is using AI tooling to, you know, increase their velocity or, you know, learn new aspects or skills that they are unfamiliar with or another variety of reasons.

**Alex Rapp:** I don't think we've dug deep enough to really understand, you know, how, you know, further how they're using AI tooling.

**Alex Rapp:** Maybe Brian has some thoughts on that, but the flip side of the AI builder is the vibe coder, the non-technical audience that may have really strong business acumen and they're using...

**Alex Rapp:** You know, the likes of Lovable, Bolt, or V0 to, you know, help them get over that hump and, you know, build the actual application, especially if they are non-technical or don't have technical resources.

**Alex Rapp:** So in terms of, you know, why we lose customers or, you know, why we don't win customers, I would say there's a lot of reasons.

**Alex Rapp:** You know, the individual developer crowd, you know, really likes to scream about, you just open source alternatives.

**Alex Rapp:** There's a big belief that, you know, authentication is not something that you should be paying for.

**Alex Rapp:** And that, you know, it's, you know, if you spend the time, it's quite, you know, it's easier to roll your own authentication and manage it.

**Alex Rapp:** There's a cohort that believe that.

**Alex Rapp:** There's also the cohort that believes, you know, that, like I said, you shouldn't pay for authentication.

**Alex Rapp:** So, you know, there's open source.

**Alex Rapp:** There were alternatives that kind of give you more or less the framework, and then you can kind of customize it as you need, but more maintenance, but no costs associated there.

**Alex Rapp:** Another thing that we hear is the fact of data ownership, and I think this also goes back to the open source issue, is that, you know, Clerk manages the user data within our own database, but anybody that's using Clerk has the ability to download their data.

**Alex Rapp:** You know, we have really strong data privacy structure in place, so, you know, that's obviously a way to set their concerns at ease, but, you know, I think we all know and have heard about, you know, plenty of data security, data breach incidents where, you know, it just causes people to be more reluctant.

**Alex Rapp:** If they're not owning their own data, because obviously, if we have a data breach, they're going to be upset at us, but then all of their users are going to be upset at them in terms of that issue.

**Alex Rapp:** So other issues I would say, too, is we've had a lot of feedback around pricing, even though if you look at the competitive landscape, pricing is actually quite favorable in some respects to competitors.

**Alex Rapp:** We're going through a pricing rehaul now.

**Alex Rapp:** I don't really know the details of that just yet, but that is another reason that we see churn or migration.

**Marcel Santilli:** I would say it's less about integrations and the ability to sync with other tooling and whatnot, because we've been working furiously to ensure that we're able to integrate easily with...

**Marcel Santilli:** All that are popular dev tools out there.

**Alex Rapp:** And I would say those are some of the bigger ones.

**Alex Rapp:** Brian, am I missing anything?

**Brian Morrison II:** No, I don't think so.

**Brian Morrison II:** I mean, there's also the element of just general bias.

**Brian Morrison II:** Everyone has their favorite camps of whether it's they want to implement auth a certain way or if they prefer a specific product to handle auth.

**Brian Morrison II:** I would say even kind of tacking on to the integration side of things, we integrate with a lot of kind of back-end as a service providers, and many of them do offer auth out of the box.

**Brian Morrison II:** So there is also the question that comes up is, if I'm building an application with Supabase, why would I bother using Clerk when Supabase offers auth as well?

**Brian Morrison II:** That's one of the other kind of things that we see pushback on.

**Brian Morrison II:** The answer, you know, because we're familiar with this approach, is, you we offer a more complete tool set.

**Brian Morrison II:** But, you know, just surface level when people see this.

**Brian Morrison II:** know, know, see

**Brian Morrison II:** If thing offers off, why would I use you?

**Brian Morrison II:** Sometimes they've already written it off before even entertaining that idea.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** So in some ways, like, you kind of have these three personas, right?

**Marcel Santilli:** Like, the devs have a lot of bias.

**Marcel Santilli:** And then the bi-coders just go for the least friction all the time, right?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And so that's kind of interesting.

**Marcel Santilli:** We'll definitely dig in.

**Marcel Santilli:** Well, thing I wanted to kind of, just to show you a little bit, one of the things that we're learning as well.

**Marcel Santilli:** Actually, I'll stop sharing first.

**Marcel Santilli:** Yeah, let me just join really quickly.

**Marcel Santilli:** But one of the things we learned with augment code, give me just one quick second here.

**Marcel Santilli:** Sorry for background noise.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** hear a car went off in the background.

**Alex Rapp:** It's never done.

**Alex Rapp:** It like that car is, like, in the office right next to you.

**Alex Rapp:** That's a loud car.

**Marcel Santilli:** I really...

**Marcel Santilli:** I don't know why, but, okay, so, check this out, right?

**Marcel Santilli:** Like, one of the things that, like, this is just to give you an example.

**Marcel Santilli:** I'm going to start off, I'm trying to decide if should build my own auth slash user management or buy a tool slash platform and help me to decide.

**Alex Rapp:** Like, essentially trying to replicate a little bit, right?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And so, it's like, these are not horrible pros and cons, right?

**Marcel Santilli:** But then, top platforms, for whatever asking reason, we got to get to it, right?

**Alex Rapp:** I know.

**Marcel Santilli:** Yep.

**Alex Rapp:** Yeah, that is one area that I was, I actually have a draft that I'm trying to, you know, get across the finish line of comparing us against other auth providers, because we saw that as a gaping area of opportunity.

**Alex Rapp:** Yeah, I mean, to provide some more context there, we've, that was intentional, up in.

**Alex Rapp:** Until now, because we don't like to, you know, really, we run with a PLG motion here.

**Alex Rapp:** So we'd rather focus on, you know, improving the product experience versus, you know, comparing ourselves to other competitors.

**Alex Rapp:** But we're now seeing what type of, you know, when competitors create this type of content, how well it performs for them.

**Alex Rapp:** So, you know, we're kind of matching on to that.

**Marcel Santilli:** And just to show you a quick example here, this is in the workshop as well, but this is for Augment, right?

**Marcel Santilli:** And we published this on July 29th, right?

**Marcel Santilli:** So like five days ago, 13th asked the AI coding tools for complex enterprise code basis, right?

**Marcel Santilli:** Went through all the steps and whatnot, and within one, 24 hours, it started showing up.

**Alex Rapp:** Yeah, doesn't surprise me.

**Marcel Santilli:** And, but it's not just showing up for like direct comparisons, like how.

**Alex Rapp:** How do I get AI coding tools to understand my entire code base?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** And then, like, I don't know if you can see, but it's like, unlike traditional AI tools that focus on an immediate code context, code-based aware AI tools like Augment Code, they, like, literally mention Augment Code.

**Brian Morrison II:** Yeah.

**Marcel Santilli:** And the part that's, like, really insane is that in our research, the way we wrote it, it literally captures, like, the same language exactly, you know?

**Marcel Santilli:** And so it starts to recommend in full and use the same language you used.

**Marcel Santilli:** And so in a lot of ways, like, and part of our research process is, like, coming up with questions to answer in order to do the research that then informs the draft.

**Marcel Santilli:** And you can see if you take that same question and you put it in chat GPT, then, like, it starts to show up the same way, you know?

**Marcel Santilli:** Yeah, I think that's been another area of struggle for me is, you know, we find by using, like, a tool like Scrunch or Profound, um,

**Alex Rapp:** We find that there's a lot of common prompts where we don't have presence in, but, you know, I think the issue that we run into is, do we write, you know, four different articles, you know, one for each prompt, or do we try to, you know, find those common threads between some of the prompts and, you know, kill multiple birds with one stone?

**Marcel Santilli:** And, you know, that's been the tricky part, I would say, in some cases, too.

**Marcel Santilli:** Yeah, that makes sense.

**Marcel Santilli:** And we'll have a ton of recommendations.

**Marcel Santilli:** just wanted to kind of point some of those out.

**Marcel Santilli:** Cool.

**Marcel Santilli:** Do you all have more materials on the customer or someone we can do a deep dive with there, like pain points, struggling moments?

**Marcel Santilli:** Like, the more specific we can get here on who we're speaking to, the better everything is.

**Alex Rapp:** On the personas, on the individual personas, I would say the first...

**Alex Rapp:** Two, we would probably have the best insight into pain points or where we excel, things of that nature.

**Alex Rapp:** Admittedly, don't have, based on our team, we don't have a lot of dedication to kind of further defining and understanding these cohorts.

**Alex Rapp:** You know, just because we've obviously been, you know, more so focused on using surface level metric or surface level insights or, you know, directional insights to really help guide us in that area.

**Alex Rapp:** You know, just because we're trying to run with growth experience as opposed to, you know, data enrichment or anything like that.

**Alex Rapp:** I can definitely give you some resources and some insights across the board there.

**Alex Rapp:** That is actually something that I'm hoping to dig into this week is that...

**Alex Rapp:** ...

**Alex Rapp:** ...

**Alex Rapp:** ...

**Alex Rapp:** ...

**Alex Rapp:** Our support team recently created an easily navigatable database of all of our Discord support issues that we should be able to, you know.

**Marcel Santilli:** That would be literally a goldmine for us.

**Alex Rapp:** Yeah.

**Alex Rapp:** That's amazing.

**Alex Rapp:** Yeah.

**Alex Rapp:** So we can see what we can do with that.

**Alex Rapp:** But that should definitely help unlock, you know, general, you know, issues or areas of friction, as well as, you know, ones, you know, more related to, you know, B2B utilization of Clerk.

**Alex Rapp:** Vibe coding, AI building, not quite sure, you know, just because it is, you know, newer just in terms of use cases.

**Alex Rapp:** But, you I'm sure that opens up a whole new host of issues that people are encountering.

**Marcel Santilli:** Definitely.

**Marcel Santilli:** Just two quick things there.

**Marcel Santilli:** when you mentioned the database of Discord support issues, our eyes lit up because, like, we love playing around with that.

**Marcel Santilli:** An example is one of our clients, one of our private clients.

**Marcel Santilli:** We analyzed their entire prompt sessions.

**Marcel Santilli:** so through the analysis, we understood what people were going to the tool for, what they were trying to build, when they stopped building, when they came back, and what they built when they came back.

**Marcel Santilli:** So we understood why people are churning, what are the tough things they're building, and what are they struggling with.

**Marcel Santilli:** All through this kind of broad data that their team hadn't even done a full analysis on yet because there's just so much information.

**Marcel Santilli:** So we love kind of getting in the weeds there and then trying to provide value.

**Marcel Santilli:** Yeah, and if we need to build, like, a custom workflow, like, that is exactly why we did the strategist print, you know, to help understand things like that.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** We think there's a lot of value there.

**Alex Rapp:** Yeah, let me see what granting, you know, some degree of access to, whether it's, you know, a raw data output or if it's access.

**Alex Rapp:** So right now, you know, I don't know the exact inner workings of it, but the support issues feed into our...

**Alex Rapp:** database and then feed into a tool called Elastic, which is more or less like a, you know, kind of consider it like another BI layer where we can write queries or just drag and drop, things like that, and segment that way.

**Alex Rapp:** So I can definitely see what it would look like to get you access to the information at, you know, even at just the bare bones level.

**Brian Morrison II:** Anything for Marcel on customer before we come on?

**Marcel Santilli:** No, no, I just want to make sure we have enough time to remember the competitors as well.

**Marcel Santilli:** There's a lot of different players in this space.

**Marcel Santilli:** Who are most concerned about, competitors?

**Alex Rapp:** Oh, man, that definitely has changed since I first started here.

**Alex Rapp:** I'll list out the competitors, then I'll kind of give you my perspective.

**Alex Rapp:** I definitely want to hear Brian's perspective on this as well.

**Alex Rapp:** know.

**Alex Rapp:** I

**Alex Rapp:** Just because he is, you know, a bit more active in the community.

**Alex Rapp:** So I would say main competitors, Auth0, WorkOS, Stitch, S-T-Y-T-C-H, Fusion Auth, Firebase, and then, you know, there's open source alternatives.

**Alex Rapp:** You know, Better Off is one that's, that's kind of emerging, but still doesn't have the volume, but there is kind of a cult following to it.

**Alex Rapp:** And then, what would the left one call?

**Alex Rapp:** Better Off.

**Marcel Santilli:** Oh, Better Off.

**Alex Rapp:** Okay.

**Alex Rapp:** Yeah.

**Alex Rapp:** Oh, yeah.

**Alex Rapp:** And then looking at your list here.

**Alex Rapp:** Yeah.

**Alex Rapp:** You know, I, I would say that's a, probably a pretty good list.

**Alex Rapp:** You know, some of those may be more fringe competitors, but I don't know, Nick, or Brian, what do you think?

**Brian Morrison II:** Yeah.

**Brian Morrison II:** Um, so I do kind of keep an eye on the social discourse on Twitter as far as like, you know, what people are talking about and what people are building with as relates to Clerk.

**Brian Morrison II:** And I would say far, far away from the rest of them, Better Off shows up more than almost any of these other competitors.

**Brian Morrison II:** Work OS used to show up more often, although I get the feeling that they might have shifted a little bit towards more of that like B2B side.

**Brian Morrison II:** So I don't, I don't necessarily think they're less of a competitor now.

**Brian Morrison II:** I just don't think I get, I see them being talked about as much since they've shifted more that way.

**Brian Morrison II:** Um, Auth0 comes up occasionally.

**Brian Morrison II:** Firebase comes up occasionally.

**Brian Morrison II:** Kind I've seen come up occasionally.

**Brian Morrison II:** Um, but again, this is, this is all just based on my, you know, my napkin analysis of what I see on Twitter.

**Brian Morrison II:** Um, but like, like Alex was saying, Better Off really does seem to have some, something of a cult following.

**Brian Morrison II:** I mean, people that like Better Off, they really like Better Off.

**Brian Morrison II:** and part of me thinks that's.

**Brian Morrison II:** Just because it's the new kid on the block that everybody's having fun with right now.

**Brian Morrison II:** But I do see it a lot.

**Alex Rapp:** And that one is open source too.

**Alex Rapp:** So that's why we get kind of aired side by side a lot.

**Brian Morrison II:** And going back to some of the issues, like some of the objections we see about our product.

**Brian Morrison II:** One of the things that I see all the time with BetterAuth is with BetterAuth, could store customer records in your own database, which is not something Clerk supports out of the box.

**Brian Morrison II:** It's not, we don't stop you from doing it, but it does take a little more effort.

**Brian Morrison II:** So that's one of the reasons why it pops up a lot.

**Marcel Santilli:** Yeah.

**Alex Rapp:** And then just to paint a more complete picture too with Auth0 and WorkOS.

**Alex Rapp:** So Brian's right.

**Alex Rapp:** You know, WorkOS used to be almost like a direct competitor.

**Alex Rapp:** You know, that's kind of the sentiment that I got when I first joined Clark.

**Alex Rapp:** But they are, I think they moved upstream and are focused more so on stealing share from Auth0.

**Alex Rapp:** So they're more enterprise focused.

**Alex Rapp:** Whereas, you know, when we look for, you know, B2B, you know, or when we go out and target B2B, it's-

**Alex Rapp:** More so earlier stage, right?

**Alex Rapp:** It's more so trying to get in early so that Clerk becomes a core component of their overall tech stack and that we grow with them as they scale as well.

**Alex Rapp:** And then Auth0 is obviously, when people switch from Auth0 to Clerk, it's generally because of cost, the degree of support that they're getting, or something that is just easier to work with, I would say.

**Alex Rapp:** You know, to kind of simplify it.

**Alex Rapp:** Yeah, so, you know, it's kind of nice in the sense that, you know, we are not as distracted by competition nowadays because, you we do have a kind of nice footing in the area that we want to be.

**Marcel Santilli:** Yep.

**Marcel Santilli:** That makes sense.

**Marcel Santilli:** That's, yeah, I think one of the things is, like, I'll

**Marcel Santilli:** Although Hot Zero is probably not investing as much in content the same way you all are, they just had so much brand recognition and authority that with LLabs, you kind of have to play the game in order to insert yourself in there in a bunch of different ways.

**Marcel Santilli:** But I think it's really cool.

**Marcel Santilli:** One of the things that could be really interesting, Brian, is just like, not this week or next, is just to understand kind of like your process for reaching out to folks.

**Marcel Santilli:** Because what we're finding is like the LLMs have like zero filter for quality on listicles and citations.

**Marcel Santilli:** And it's just like, they're just citing URLs are just not great places, you know, but they also happen to be URLs that are not impossible to get mentioned and influencing that.

**Marcel Santilli:** But these are not going to be like the people you probably follow on Twitter.

**Marcel Santilli:** These might be more like, you know.

**Marcel Santilli:** So more random sites, if you will, but if there's a really high volume type of query where there's a citation where they're mentioning your competitors and not mentioning you or not mentioning you high up enough, then, you know, there might be an opportunity to influence those things as well, you know, in case there's like some categories that we want to try to go for like some quick wins as well.

**Brian Morrison II:** Yeah, mean, could even, quick 30 second overview of my process.

**Brian Morrison II:** I have a, I have a, whatever they call it, a TweetDeck board.

**Brian Morrison II:** It's X Pro now or whatever it is.

**Brian Morrison II:** I have an X Pro board that looks at every mention of Clerk, Clerk Off, or mentions Clerk directly.

**Brian Morrison II:** And I just skim through that once a day, once every other day and see what people are looking at, what they're up to, what they're talking about, stuff like that.

**Brian Morrison II:** So there's not, there's not a real science to it, if you will.

**Brian Morrison II:** It's, it's just me looking through it, finding people who might be interested in different features of Clerk and might be having trouble getting them implemented, offering to help them out or support them, celebrating wins that they have when using Clerk.

**Marcel Santilli:** Stuff like that.

**Marcel Santilli:** Got it.

**Marcel Santilli:** That's super helpful.

**Marcel Santilli:** That's great.

**Marcel Santilli:** If we can go into growth.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** No, I think we covered a lot of the customer.

**Marcel Santilli:** We can dive deeper later, but we have 15 minutes here.

**Marcel Santilli:** So, okay.

**Marcel Santilli:** Tell us a little more about what your lean, your mean and lean team of four are currently doing.

**Alex Rapp:** Um, some of the biggest challenges and blockers are, uh, biggest challenges and blockers.

**Alex Rapp:** That's easy.

**Alex Rapp:** Uh, bandwidth is the biggest challenge and blocker.

**Alex Rapp:** We have a backlog of so many things that we want to do and we just don't have the, uh, the manpower for it.

**Alex Rapp:** Um, you know, the, you know, in terms of, you know, where our best leads come from, um, we have core, uh, what, what I call our core four channels.

**Alex Rapp:** Okay.

**Alex Rapp:** No.

**Alex Rapp:** Organic search is obviously a big one, but we all know that that is a melting pot of a number of different channels, as well as just traditional SEO.

**Alex Rapp:** For instance, one of our second core growth channels is YouTube Partnerships.

**Alex Rapp:** We know that YouTube Partnerships drive a lot of organic interest in inbound traffic.

**Alex Rapp:** And YouTube Partnerships, they're not ad roles or anything like that.

**Alex Rapp:** We find channel owners that are obviously good fits for Clerk's audience, and we work with them to basically provide ideas based on the types of tutorials that they're building.

**Alex Rapp:** Generally, they're building clones of popular apps or apps that serve a purpose of interest for development.

**Alex Rapp:** Developers that are looking to create side hustles, things of that nature.

**Alex Rapp:** And so that's been a really strong, you know, sort of evergreen growth channel for us.

**Alex Rapp:** The third one is AEO.

**Alex Rapp:** Obviously, you know, that's an area where we've seen really strong growth in terms of, you a dedicated channel.

**Alex Rapp:** And then lastly would be open source partnerships.

**Alex Rapp:** You know, that could be a whole host of things.

**Alex Rapp:** It could be, you know, finding GitHub repos, reaching out to their maintainers, especially ones that either don't have auth in their project or, you know, ones that are using alternatives to Clerk.

**Alex Rapp:** And we, you know, try to give them an incentive to essentially swap out whatever they have or plug Clerk in.

**Alex Rapp:** But that is more of a low volume but high intent channel.

**Alex Rapp:** So, you know, we're looking to add to that.

**Alex Rapp:** Snowball.

**Alex Rapp:** And then we have other channels as well that sort of layer on top of that to help fill the top of our funnel and push people closer to acquisition.

**Alex Rapp:** That could be paid social.

**Alex Rapp:** could be newsletters.

**Alex Rapp:** It could be events.

**Alex Rapp:** It could be...

**Alex Rapp:** What else am I missing here?

**Alex Rapp:** It could be, you know, co-marketing with other DevTools.

**Alex Rapp:** It could be, you know, just integrations or documentation on, you know, another DevTools site or, you know, other inbound traffic that we see from, you know, third-party sites.

**Alex Rapp:** But those are the areas that we're most focused in.

**Marcel Santilli:** Fantastic.

**Marcel Santilli:** It's really helpful.

**Marcel Santilli:** Yeah, we're doing a lot on the Exploratory side with other clients.

**Marcel Santilli:** You know, they have these main channels, but then things like newsletters, events, that's coming up a lot as well.

**Marcel Santilli:** So, you know, creating databases or just understanding the space better and then helping them strategize where they want to hit or actually running a newsletter.

**Marcel Santilli:** And really quickly on the YouTube partnerships, like, are you reaching out via email?

**Marcel Santilli:** Do you have kind of like a SDR-like motion outbound to people?

**Marcel Santilli:** Same thing with like the open source partnerships.

**Marcel Santilli:** Like, how are you reaching out to them when you identify them?

**Alex Rapp:** For the sake of time, I will send you guys an article that we did with Ganto that answers all your questions about that.

**Marcel Santilli:** There you go.

**Marcel Santilli:** I love it.

**Marcel Santilli:** Okay, sweet.

**Marcel Santilli:** That's super helpful.

**Marcel Santilli:** Got it.

**Marcel Santilli:** Marcel, anything else before we just kind of wrap with what they want?

**Marcel Santilli:** No, think the main thing super quickly would just be what are some of the things you've done around content or any additional, not just specific examples, but also like any big bets that you have done that have worked or seen signs that worked or things you're thinking about.

**Marcel Santilli:** Because I know you mentioned you have a huge backlog, so sometimes it's helpful to know.

**Marcel Santilli:** you.

**Marcel Santilli:** go.

**Marcel Santilli:** There's few that maybe we can try to focus on right away as well.

**Alex Rapp:** Yeah.

**Alex Rapp:** In terms of the three best pieces of content, the one that keeps floating to the top of my brain there is really our docs, to be quite honest with you.

**Alex Rapp:** A lot of developers and clear customers rave about the comprehensive nature, the ease of navigation, the resources that we provide within our docs in general.

**Alex Rapp:** That, again, feeds back to the desire to have the best DX of not even just auth tools out there, but anybody in the dev space.

**Alex Rapp:** That's what we strive for.

**Alex Rapp:** You know, in terms of other content areas, you know, I think that there's a lot of unanswered questions there.

**Alex Rapp:** You know, we...

**Alex Rapp:** Don't really have a strong or confident sense of how our blog contributes to acquisition.

**Alex Rapp:** We know that it does, at least directionally, but it's been really hard to prove that just in terms of the ability to stitch together a really strong attribution model that works with that.

**Alex Rapp:** But one thing that I pointed out to Brian last week was that most of our content on the blog is very specific to Clerk, and we don't really cast a wide net in terms of trying to bring in other audiences.

**Alex Rapp:** And, you know, we don't, we don't write, you know, we generally don't tend to write blog posts that are more, you know, kind of educational, upper funnel of, of the sense of just covering a topic more generically versus, you know, how it fits with, within Clerk's.

**Alex Rapp:** We just ran, I know Brian's working on the last couple posts, we ran a content test around B2B SaaS multi-tenancy in our organization's feature to help identify whether or not that approach is working, where we kind of start with content that is very generic, not really plugging Clerk at any point in time through that content.

**Alex Rapp:** And then as we work through the series of additional blog posts, we get closer and closer to content that's more specific to Clerk itself, in a sense, creating our own user journey as it relates to multi-tenancy and B2B SaaS.

**Alex Rapp:** But I think it's too early to tell how that's performing, especially since we're still working to push out that content.

**Marcel Santilli:** Send us your backlog, by the way, I don't where it lives, but that'd be fantastic, so we can dig in and see how we can help.

**Marcel Santilli:** And up in the background, we're going to be doing research.

**Marcel Santilli:** Search, creating topic clusters, finding some gaps and opportunities.

**Marcel Santilli:** so to be able to include some of your existing backlog in that, plus our ideas and what we found.

**Marcel Santilli:** Cool.

**Marcel Santilli:** Yeah, I can definitely do that.

**Marcel Santilli:** Amazing.

**Marcel Santilli:** Amazing.

**Marcel Santilli:** Cool.

**Marcel Santilli:** mean, four minutes left.

**Marcel Santilli:** We'd like to end with, you know, in six months from now, like, what would be a home run from this?

**Alex Rapp:** Yeah, so I have this overarching goal from the beginning, you know, to go ahead and know it out of Vercel's playbook.

**Alex Rapp:** Ideally, answer engines become a consistent, you know, 10% or above of total signups within a given week or time period.

**Alex Rapp:** My goal is to get it there.

**Alex Rapp:** You know, right now, it's been hanging at 1%, even though our inbound traffic has been, you know, from, sorry, even though our inbound

**Alex Rapp:** On traffic from answer engines has been, you know, growing rapidly.

**Alex Rapp:** And, you know, when we keep an eye in scrunch, you know, we see that our presence and visibility scoring is, you know, hockey stick growth now.

**Alex Rapp:** But, you know, we, you know, to kind of harken back to something I teased earlier, when we were talking to Ganto about this, he was saying that he has this hypothesis that a lot of the decision makers are the ones doing the research, you know, on LLMs.

**Alex Rapp:** And then, you know, they're handing it off to a more, you know, technical team member who is actually, you know, going through and installing Clerk.

**Alex Rapp:** But it's hard for me to believe that just based on what we know about our audience.

**Alex Rapp:** You know, I can't imagine that there's, you know, thousands of CTOs that are happening upon Clerk, you know, through, you know, LLM queries and then handing it off to, you know, somebody more technical and, you

**Alex Rapp:** They're coming in directly or via organic search.

**Alex Rapp:** I still have not yet been able to unlock that specific insight to actually validate the fact that the lack of direct conversion from LLMs is due to that.

**Alex Rapp:** There could be a whole host of reasons that they're still conducting the research and we don't have enough content that's more at the decision stage or at the consideration stage or enough content that's really going to convince you to pull the trigger with Clerk.

**Alex Rapp:** There's obviously not a significant barrier to entry because the majority of signups that we get come in through our free tier and then they build their way up to the pro tier, which is really the biggest incentive to moving from the free tier to the pro tier is essentially volume on the user side.

**Alex Rapp:** But, you know, that's the biggest trigger, you know, some of the add on features.

**Alex Rapp:** That we have on the pro tier, you know, they're more so designed to be there for when you actually need those features as opposed to, you know, sort of this shiny object that, you know, am I really going to pay for it just to get this, you know, one feature?

**Alex Rapp:** You know, I guess you could make that case with, you know, in terms of our, you know, add-ons, there's, you know, you have the access to MFA, you have the access to user impersonation, which could still be helpful at, you know, a lower monthly average user threshold.

**Alex Rapp:** But, you know, I think that's part of the reason why we're going through this pricing revamp exercise is to, you know, make it, you know, a bit more compelling to move to a paid tier, especially as we focus more and more on those B2B prospects.

**Marcel Santilli:** That's really interesting.

**Marcel Santilli:** One thing I will say, I know it's a really, really tough ask, but I will know it's

**Marcel Santilli:** So, you know, it might be worth even every now and then for like, let's say a week, if you can insert anything in the signup flow or you ask how to hear about us, we have a customer that did that.

**Marcel Santilli:** And it turns out like about 40% of all their leads are coming from LLMs.

**Alex Rapp:** So that has been proposed before and it was quickly dismissed as an option.

**Alex Rapp:** However, I know that we're good friends with the head of growth over at Sentry and that's essentially how they're running an attribution.

**Alex Rapp:** They're not relying on UTM parameters as much.

**Alex Rapp:** They're more so relying on the, how did you hear about us for him?

**Alex Rapp:** And, you know, I was surprised to hear the amount of, or the percentage of engagement with that element, you know, compared to what my expectations would be of, you know, most people just kind of.

**Alex Rapp:** And, you know, brushing or sidestepping it, so.

**Marcel Santilli:** Yeah, yeah, there's a very, very strong correlation between how people remember that they heard about you and their intent, you know, in addition to being able to get better attribution, you know, but we got to wrap up, but this is super helpful.

**Marcel Santilli:** So we're going to follow up with a bunch of things, but also feel free to flood us with as much context and information as humanly possible, and then we'll follow up with a bunch of deep dives and then just schedule some of our recurring stuff as well.

**Alex Rapp:** Okay.

**Alex Rapp:** In terms of, you know, transferring data in files or anything like that, you know, if there's something that we need to give you access to that's, you know, too big for Slack, how should we go about that?

**Marcel Santilli:** Yeah, like, usually either we can do a shared Google Drive, or you can share with us in whatever drive you have, right?

**Marcel Santilli:** Like, whether it's a Dropbox or.

**Marcel Santilli:** Google Drive, or we can create a Google Drive on our end and give you access to be able to upload as well.

**Marcel Santilli:** It's like a massive file, you know, but most people are already hosting it somewhere, and so they'll either duplicate a folder or something and then share access to that if they don't want it to give us access to the same folder that, let's say, there's hundreds of employees that have access to, or you can upload it to whatever we send you if there's massive files, you know.

**Alex Rapp:** Yeah, I mean, just really quickly, so our main infrastructure just around, you know, marketing data, it's BigQuery, and that sits on top of Hex, or sits underneath Hex, which is our BI tool, our BI and reporting tool.

**Alex Rapp:** I mentioned Elastic, I can see about getting you guys access to that versus, you know, just doing a data export of, you know, some sample data.

**Alex Rapp:** Those are, you know, really the, I would say, the biggest.

**Alex Rapp:** You know, sort of gateways to, you know, data that you'd probably care about.

**Alex Rapp:** And I'm sure there'll be other things I think about afterwards, but do any of those, you know, do you guys have existing, you know, accounts or connections or any of those for your other customers?

**Marcel Santilli:** Off the top of my head, know Engine uses, like, we've used BigQuery before, but...

**Marcel Santilli:** Yeah, normally, like, whatever you have, like, we can plug in.

**Alex Rapp:** We just have a shared team account.

**Marcel Santilli:** That makes it a lot easier for us to, like, manage, like, that access and things like that.

**Marcel Santilli:** So we'll send you that, and then we'll go from there.

**Alex Rapp:** Okay.

**Alex Rapp:** Yeah, sounds like most people just give you, you know, either samples or exports.

**Marcel Santilli:** You know, is that fair?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Yeah, yeah.

**Marcel Santilli:** It's usually preferred by their security teams, you know.

**Marcel Santilli:** Yeah, I can imagine.

**Marcel Santilli:** Yeah, yeah.

**Marcel Santilli:** It's just a little bit easier to manage.

**Alex Rapp:** Okay, cool.

**Alex Rapp:** Last question, then I'll let you guys go.

**Alex Rapp:** So I'll be out of office Thursday and Friday and obviously try to get you some resources before then.

**Alex Rapp:** In terms of scheduling, is there anything that I just need to be aware of in terms of next steps or will it mostly be async and then we'll figure out another time to meet up?

**Alex Rapp:** Marcel, I remember you mentioning something about, you know, kind of a regular and, you know, for lack of better terms, in-person schedule.

**Marcel Santilli:** Yeah, so weekly recurring calls moving forward starting next week.

**Marcel Santilli:** In-person if you're close, grade two, even most.

**Alex Rapp:** I meant like, yeah, this, just.

**Marcel Santilli:** Oh, okay.

**Marcel Santilli:** I mean, we like you a lot.

**Alex Rapp:** I don't know about every week, you know.

**Marcel Santilli:** Yeah, yeah.

**Marcel Santilli:** And then product deep dives, nothing that's going to be blocked by you being out Thursday or Friday.

**Marcel Santilli:** We'll figure out a product one, maybe at a deeper customer home, but we'll get those scheduled for when you're back.

**Marcel Santilli:** Yeah, we try to do as many deep dives this week, and if some of it goes over to next week, great.

**Marcel Santilli:** It's just that the more dense we have all the learnings packed up, then that unblocks us to start to really kind of firm up the content strategy and a lot of the artifacts will generate.

**Alex Rapp:** Right.

**Alex Rapp:** Yeah, my schedule shouldn't be an issue.

**Alex Rapp:** I've been trying to keep it much more, you know, I've been reducing the amount of meetings that I'm accepting.

**Alex Rapp:** So, you know, even this week, you know, if we need to hop on again, it should be fun.

**Marcel Santilli:** Sounds great.

**Marcel Santilli:** Thanks, We'll talk about it.

**Alex Rapp:** Yeah, thanks.

**Brian Morrison II:** See you.

**Brian Morrison II:** Nice meeting you.

**Brian Morrison II:** Bye.

**Brian Morrison II:** Bye.
