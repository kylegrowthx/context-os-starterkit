# Marcel <> Jason - Weekly

<metadata>
date: 2026-02-11
time: 22:30 UTC
duration: 80 minutes
organizer: marcel@growthxlabs.com
participants: Marcel Santilli, Jason Gong
fireflies_id: 01KGMQDN5GWC87WMB259452HGT
transcript_url: https://app.fireflies.ai/view/01KGMQDN5GWC87WMB259452HGT
</metadata>

---

## Summary

Marcel and Jason covered four main threads: the GrowthX AI Handbook (now live on GitHub as the company OS), event and community strategy, content production planning, and CheckThat's AI brand research product direction. Most important development: Marcel detailed a new AI brand measurement methodology — treating AI engines as digital twins of buyers, surveyed via structured prompts organized by taxonomy — which will become the core intellectual backbone of CheckThat. Jacob Cutter (ML/PhD) has verbally accepted to join as the data science hire.

---

## Context

This is the recurring weekly between Marcel (CEO) and Jason Gong (head of community/growth at GrowthX). Jason manages the IE LED community, workshops, webinars, and social content. These sessions serve as strategic alignment — Marcel sets direction, Jason executes. The meeting happened the week of Feb 9 during a period of heavy product development work on CheckThat and active GrowthX event programming.

---

## Relevance

**To GrowthX Services:**
- New GrowthX AI Handbook is live on GitHub — Marcel will post it in the company channel. Replaces Notion as the official company OS.
- Event strategy: VC co-hosting model is working well (rooms fill faster, better attendees). Need to scale beyond Bay Area to avoid saturation.
- Content: current output is scattered and inconsistent. Need a structured content cadence with multiple creators (Marcel, Jason, Danny, Will), anchored by a flagship lead magnet ($500 masterclass or equivalent).
- Operational gap: George has moved on, Dig is unmanaged. Context directory project aims to reduce reliance on direct communication.

**To CheckThat:**
- Core new product direction: AI brand research methodology based on brand recall, sentiment, and alignment metrics. AI engines are treated as "digital twins" of buyers surveyed via custom prompts.
- Taxonomy is the infrastructure: auto-tagging of prompts, prompt generation workflows, layered brand/market/buyer context.
- Phased rollout: taxonomy and auto-tagging first → onboarding for deeper research → dashboard redesign → scoring models and external analytics integration.
- Self-serve experience is broken — users sign up but rarely add custom prompts or upgrade to pro. Needs product attention.
- Jacob Cutter (PhD, Deepgram background) verbally accepted offer — will accelerate ML capabilities.

---

## Overview

- GrowthX AI Handbook now on GitHub — company OS replacing Notion.
- Event strategy: co-host with VCs, expand beyond Bay Area, balance dinners with scalable mixers/breakfasts.
- Content strategy: need consistent cadence with multiple voices, flagship lead magnet ($500 masterclass), landing pages on GrowthX and IE LED Growth.
- CheckThat product: AI brand research methodology — recall, sentiment, alignment measured via structured prompt taxonomy. AI engines as buyer digital twins.
- Phased product rollout starting with taxonomy and auto-tagging.
- Self-serve onboarding broken — users don't add prompts or upgrade.
- Jacob Cutter (ML/PhD) verbally accepted offer as data science hire.
- In-person content production session planned with Danny.

---

## Key Topics

### GrowthX AI Handbook

Marcel introduced the GrowthX AI Handbook — a GitHub-hosted company OS replacing Notion as the official handbook. Includes context files on brand research methodology, writing style, and company playbooks. Marcel will share the link in the company channel and send Jason the handbook repo and AI brand research files.

### Event and Community Strategy

The VC co-hosting model is working — rooms fill fast by association, better attendees. Marcel differentiates event types by scalability: curated dinners (least scalable) → mixers/breakfasts (more scalable). The community strategy needs to pivot from membership growth metrics to valuable workshops. Lead generation should come from simple, scalable offers (landing pages, $500 masterclass). Need to expand beyond Bay Area to avoid saturation. Jason managing calendars in Notion; Marcel suggested consolidating into Luma for shared access.

### Content Strategy

Current content is scattered — lacks cohesion to build audience. Marcel wants a content engine like successful influencers: videos, newsletters, playbooks, with multiple creators (Marcel, Jason, Danny, Will). Will set up recording at Marcel's home. Flagship lead magnet: a $500 masterclass with limited free access. Landing pages on both GrowthX and IE LED Growth platforms.

### CheckThat AI Brand Research Methodology

The key product direction discussed at length. Marcel's mental model: AI engines are digital twins of buyers. You survey them via prompts organized by taxonomy (brand evaluation prompts, solution exploration prompts, etc.). The output measures brand recall, sentiment, and messaging alignment — core brand health metrics. Layered context feeds the system: company positioning, competitors, market categories, buyer personas and decision processes. This taxonomy enables auto-tagging of prompts and automated prompt generation. The onboarding flow gets enriched with public page content (company descriptions, category definitions). Later phases include dashboard redesign, scoring models, audit workflows, and external analytics integration. Marcel emphasized protecting this methodology as proprietary IP.

### Product Self-Serve Gap

Jason reports users sign up but rarely add custom prompts or upgrade to pro plans. Marcel identifies this as a critical gap — the product experience needs attention to drive engagement and monetization. Taxonomy rollout, auto-tagging, and prompt generation workflows are the priority fixes.

### Hiring

Jacob Cutter (PhD, Deepgram background) verbally accepted offer as the first dedicated ML/data science hire. Will accelerate AI capabilities and product sophistication. Marcel plans to build out a data science team from this foundation.

---

## Action Items

**Marcel Santilli**
- Post GrowthX AI Handbook link in company channel
- Send Jason handbook repo link and AI brand research methodology files
- Assist Jason in shaping strategic planning sessions and provide context files
- Coordinate with Danny to plan a week-long in-person content production session
- Refine mental model for dashboard metrics and brand research visualization
- Lead coordination for upcoming webinars, workshops, and events
- Explore scalable lead generation landing pages on GrowthX and IE LED Growth platforms
- Onboard Jacob Cutter and integrate him into CheckThat product development

**Jason Gong**
- Send meeting document to Marcel
- Prepare to build prompt mapping skills based on Marcel's AI brand research structure
- Manage event calendars, confirm RSVPs, and increase warm outreach with Gloria to boost attendance
- Review and coordinate ongoing workshop promotions and co-hosted event scheduling in Notion
- Develop structured post types and consistent content production cadence
- Build automation for taxonomy, auto-tagging, and custom prompt workflows
- Support refinement of the self-serve product experience to improve engagement and upsell to pro plans
- Facilitate prompt sharing and prepare for next week's calls and prompt reviews

---

## Transcript

**Marcel Santilli:** It's.

**Marcel Santilli:** Yo.

**Jason Gong:** Sir.

**Jason Gong:** How are you?

**Marcel Santilli:** Good.

**Marcel Santilli:** We went to go get coffee with George and it started pouring, and it was a little.

**Marcel Santilli:** There was a massive line.

**Marcel Santilli:** We're like, let's not wait in line at Blue Bottle.

**Marcel Santilli:** There's this other coffee shop that's really good a block down and it wasn't raining.

**Marcel Santilli:** And then halfway through getting there, started pouring, and there's a massive line on that coffee shop that was bigger than the Blue Bottle one.

**Marcel Santilli:** So.

**Marcel Santilli:** But I got my coffee, and it's really good, so.

**Jason Gong:** Silver lining.

**Jason Gong:** All right, I'll send you the doc.

**Marcel Santilli:** All right.

**Marcel Santilli:** Let's do something we haven't done in a while.

**Marcel Santilli:** Personal, how you feeling?

**Marcel Santilli:** One to 10.

**Marcel Santilli:** One being like, hey, my life.

**Marcel Santilli:** On the personal side, 10 being perfect, in which case.

**Marcel Santilli:** And then on work, one being today, I'm quitting you.

**Marcel Santilli:** 10 being perfect.

**Marcel Santilli:** This company is.

**Marcel Santilli:** There's nothing to fix.

**Jason Gong:** Personal, like a seven.

**Jason Gong:** I mean, generally very happy.

**Jason Gong:** But I think Carrie's just not having a good time at her job.

**Jason Gong:** Yeah, he's really, really, really stressed.

**Jason Gong:** But Balin's healthy and, you know, everything else is good.

**Jason Gong:** So 7.

**Jason Gong:** And then growth X.

**Marcel Santilli:** Maybe.

**Jason Gong:** Six or seven.

**Jason Gong:** Not.

**Jason Gong:** Not because I'm not having a good time, but more just like, you know, I know we're pushing on a lot of different places and, yeah.

**Jason Gong:** Trying to do well, you know.

**Marcel Santilli:** Yeah.

**Jason Gong:** Cool.

**Marcel Santilli:** That's good.

**Marcel Santilli:** Man.

**Marcel Santilli:** On work side, what is one thing that is within my control or your control that would take you from a 6 or 7 to an 8 or 6 to 7?

**Jason Gong:** Not really sure.

**Jason Gong:** I think maybe just, like, spending more time together, shaping things that might be helpful.

**Jason Gong:** And I think we're getting closer.

**Jason Gong:** You know, we're not talking about activities anymore, which I think has been a good change.

**Jason Gong:** That's cool.

**Marcel Santilli:** Weeks.

**Jason Gong:** I think spending more time there would be helpful.

**Marcel Santilli:** And then.

**Jason Gong:** I mean, through that as well.

**Jason Gong:** Just kind of like understanding more of the vision, I think would also be helpful.

**Jason Gong:** I think I get bits and pieces, you know, especially about output.

**Jason Gong:** And, yeah, everything connects together.

**Jason Gong:** But it does feel like.

**Jason Gong:** Like, I know it's not intentional, but there are silos forming just in like.

**Jason Gong:** Like, check that is.

**Jason Gong:** Is one.

**Jason Gong:** Right.

**Jason Gong:** Growth X is one.

**Jason Gong:** And, you know, I guess through the conversations with Al and stuff, we can see how, like, you know, probably not doing the best job, kind of linking them together even if we do one.

**Marcel Santilli:** Yeah, yeah, that makes.

**Marcel Santilli:** That makes sense.

**Jason Gong:** So.

**Marcel Santilli:** Connecting the dots more across our layers and.

**Marcel Santilli:** And then doing more of, like a strategic planning.

**Marcel Santilli:** Shaping, forming together.

**Marcel Santilli:** Okay, cool.

**Marcel Santilli:** All right, well, let's do that.

**Marcel Santilli:** Let's see.

**Marcel Santilli:** I Damn.

**Marcel Santilli:** Monday's a holiday.

**Marcel Santilli:** I think.

**Marcel Santilli:** We can spend time, I think in person.

**Marcel Santilli:** My help more.

**Marcel Santilli:** Right.

**Marcel Santilli:** What do you think?

**Jason Gong:** Sorry, say that again.

**Marcel Santilli:** In person is better, right?

**Marcel Santilli:** You think for shaping?

**Jason Gong:** Yeah.

**Jason Gong:** Well, I guess it depends.

**Jason Gong:** What it's not that much better.

**Jason Gong:** Like zoom calls are fine.

**Jason Gong:** Okay, thank you.

**Marcel Santilli:** Okay, well let's go through today and then we can.

**Marcel Santilli:** I do have sometime Friday but I also like my headstone time has been so high leverage that it almost feels like, you know, like the more I do that then because I've been communicating the same thing again and again in different ways and then it just kind of like doesn't quite like make its way and it kind of like almost like doesn't click.

**Marcel Santilli:** So it's almost like here's my context files and here's one explanation of it.

**Jason Gong:** No, I mean I'm like I set up.

**Jason Gong:** I spent Saturday setting up cursor and like my life's changed now.

**Marcel Santilli:** Yeah, exactly.

**Marcel Santilli:** Okay.

**Marcel Santilli:** And then.

**Marcel Santilli:** And then I also launched Handbook Growth X AI password is AI LED growth altogether lower caps and actually let me post it in the channel right now before I forget.

**Jason Gong:** Yep.

**Jason Gong:** Let's see it.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Okay.

**Marcel Santilli:** So yeah, anyways, the.

**Marcel Santilli:** This is like V0 of it, right?

**Marcel Santilli:** The.

**Marcel Santilli:** The long term version here is like this is truly our handbook.

**Marcel Santilli:** It also has guides, it has SOPs, it has, you know, a lot of things and this is the source of truth.

**Marcel Santilli:** And only anyone that wants to make changes to it should do a pull request and make changes to it.

**Marcel Santilli:** Nah, you know, just go off and drift and.

**Marcel Santilli:** And then notion can be more like the reference this.

**Marcel Santilli:** But instead of having our handbook in notion, this would be a like notion will point to this as the source of truth for a lot of things for like the context of the company.

**Marcel Santilli:** And the notion is more like the day to day.

**Marcel Santilli:** And then later on I can figure out a way to keep the two in sync and lock the pages in notion and then people can make contributions over time to this one.

**Marcel Santilli:** But this is like more like truly like company, like operational, but it's also a GitHub project in our GitHub.

**Marcel Santilli:** So you can pull that context as long as you have access to our GitHub.

**Marcel Santilli:** You can pull this all the docs here anytime or do a sim link to it.

**Marcel Santilli:** So then this would be like also the place where we host our shared context, you know.

**Jason Gong:** So how do you plan to use it?

**Marcel Santilli:** I mean like right.

**Marcel Santilli:** Right now see an idea.

**Marcel Santilli:** You know, it's like we're like, right now, oh, shoot, I closed this.

**Marcel Santilli:** See.

**Jason Gong:** Okay.

**Marcel Santilli:** Anyways, but like, I wrote the entire thing by just taking all the context I already had and it's like translating it into docs.

**Marcel Santilli:** And, and so there is like also a context folder that is like, ignored by the.

**Marcel Santilli:** By the docs, but it's in the repo.

**Marcel Santilli:** So if you pull this repo, it should have like, some of the roles.

**Marcel Santilli:** I'll clean up the sources.

**Marcel Santilli:** It has some of the knowledge, you know, and then it has like, the voice.

**Marcel Santilli:** And then over times like this will have the context of how to write like, like us.

**Marcel Santilli:** Also the knowledge and some of the roles of like the, the CEO or whatever.

**Marcel Santilli:** Over time, I'm planning on putting like, my user guides, and everybody can have their user guides here.

**Marcel Santilli:** So if you're interacting with anyone, it also has like, cursor rules and you know, like, skills and anything else you need, you can start being.

**Marcel Santilli:** Putting here.

**Marcel Santilli:** And so anything that's like, worth.

**Marcel Santilli:** Worth sharing with everybody can all be.

**Marcel Santilli:** Be here, you know, ideally.

**Jason Gong:** So cool.

**Marcel Santilli:** But we'll see.

**Marcel Santilli:** It's an experiment.

**Marcel Santilli:** All right, well, let's run through.

**Marcel Santilli:** I think, like, for, for me, the, the.

**Marcel Santilli:** The big picture, Ray.

**Marcel Santilli:** Like, and I don't know if like, what would be.

**Marcel Santilli:** I think you have the 2026 kind of like, plan there, but it's like you have the, this model.

**Marcel Santilli:** But like, I think the connection there that I would like to see is how the programs and the lanes, you know, will build up to that.

**Marcel Santilli:** And so you kind of have the programs here.

**Marcel Santilli:** And so that's, that's good.

**Marcel Santilli:** And then now it's like, okay, how do we know if it's like, what are the bottlenecks in these programs?

**Marcel Santilli:** Are they being executing and what are the actual, like, plans for this?

**Marcel Santilli:** Like, a little bit more, right?

**Marcel Santilli:** Like, what is the strategy behind it?

**Marcel Santilli:** Like, so for, for instance, like, like Air Ops had GG on their latest webinar, right?

**Marcel Santilli:** Like, so it's like, hey, that's a leverage point.

**Marcel Santilli:** Or like, right now our bottleneck is like, I'm hitting up people, but, like, I don't have enough time to just like DM500 people and people are stuck are going to eventually stop responding with.

**Marcel Santilli:** To me because, like, we're.

**Marcel Santilli:** We're like using up me too much, right?

**Marcel Santilli:** And so then like, okay, so that's a bottleneck and we need to like, nurture other people, you know.

**Marcel Santilli:** But then it can't be Marcel talking to Caddy or Marcel talking to Carolou or Marcel, right?

**Marcel Santilli:** Like so then your team is doing it.

**Marcel Santilli:** But, you know, so there's like, identifying those bottlenecks and then figuring out, like, what is the plan to address those bottlenecks.

**Marcel Santilli:** So, so.

**Marcel Santilli:** So it's like, hey, there.

**Marcel Santilli:** This is like the program, let's say, like, events, right?

**Marcel Santilli:** And then it's like, okay, cast that out for the rest of the year.

**Marcel Santilli:** It's going to shift.

**Marcel Santilli:** And so, like, Q4, way lower confidence than Q3, way lower confidence than Q2 and Q1.

**Marcel Santilli:** But start, like, planning ahead.

**Marcel Santilli:** Like, today.

**Marcel Santilli:** I talked to G. He's going to be in town April 14th and 15th, and he's going to be in town July, wants to do events with us.

**Marcel Santilli:** Okay, awesome.

**Marcel Santilli:** Like, let's lock those in.

**Marcel Santilli:** No brainer.

**Marcel Santilli:** Mixer done.

**Marcel Santilli:** Okay, cool.

**Marcel Santilli:** And then, you know, like, so.

**Marcel Santilli:** So you have kind of, like, things that are shaping, things are forming, things that you're kind of like, nailing down.

**Marcel Santilli:** You know, you reach out to people like a Rachel, and you're like, hey, go get on a call, become best friends.

**Marcel Santilli:** Like, offer her to go to a game.

**Marcel Santilli:** And then be like, hey, now we're BFFs.

**Marcel Santilli:** Like, what do you want to do together?

**Marcel Santilli:** You know, like, CC is like, hey, let's do a meetup.

**Marcel Santilli:** But.

**Marcel Santilli:** But it's a lot easier when it's like, cast out the program and then you're solving kind of the bottlenecks, you know, a little bit.

**Marcel Santilli:** And I think, like, right now it's like, I don't know that the team sees it that way.

**Marcel Santilli:** And it's a lot harder to.

**Marcel Santilli:** Man, it's gonna be a lot harder for you to manage the team through, like, without that lens, right?

**Marcel Santilli:** Because it was going to be like, hey, so and so, go talk to this person and ask them to do this, this, and then do this thing and then that thing, right?

**Marcel Santilli:** Versus, like, kind of like, hey, here's.

**Marcel Santilli:** Here's the calendar.

**Marcel Santilli:** Here's the thing.

**Marcel Santilli:** Fill it in.

**Marcel Santilli:** And in order to attract people, here's where we're going to need.

**Marcel Santilli:** And then you figure out, like, where are the places where it's like, Marcel is absolutely necessary and how do we do it in a way that build leverage for him versus him?

**Marcel Santilli:** Copy and pasting.

**Marcel Santilli:** Like, Like, I spent, like, two hours sending dms and it's like, after two hours, like, this is so inefficient.

**Marcel Santilli:** Like, this.

**Marcel Santilli:** There's no way this is the way.

**Marcel Santilli:** You know, like, I was changing status in airtable, manually sending, copy and pasting, you know, And I was like, ah, this is like, insane.

**Marcel Santilli:** Like you know, this feels like.

**Jason Gong:** And so.

**Marcel Santilli:** But, but the, the good news is like events always going to be the least scalable on dinners is the least scalable, the hardest, most curated most.

**Marcel Santilli:** And you need more connectors.

**Marcel Santilli:** People are building relationships.

**Marcel Santilli:** DM bases, text message basis.

**Marcel Santilli:** Right.

**Marcel Santilli:** The like mixers are more blast.

**Marcel Santilli:** And you, if you do too many breakfasts, not enough mixers or not or too much dinners like then, then it's just like it loses the balance because like you need more entry ways to building the relationships that then you get them to come to the dinners and then you tap into their networks and then they refer people.

**Marcel Santilli:** Right.

**Marcel Santilli:** And you figure out what's in it for them, what do they care about.

**Marcel Santilli:** But then if you only do that and we don't do the like the workshops on riding the wave of what people want.

**Marcel Santilli:** Like AKA like me doing something on like what.

**Marcel Santilli:** Like how to use clock code.

**Marcel Santilli:** Like how I've 10x my daily.

**Marcel Santilli:** Like my productivity with cloud code and cursor, you know and.

**Jason Gong:** Yeah.

**Marcel Santilli:** Or whatever, you know.

**Jason Gong:** Yeah, that makes sense.

**Jason Gong:** And that would be a good topic maybe with Kristen.

**Jason Gong:** We're I think we nailed down April 9th or something is the workshop with her.

**Jason Gong:** I know it's a month out, but working ionative you know, you guys seems like a good combo.

**Marcel Santilli:** Yeah, I think that's a good like one for you to like, like don't delegate that part.

**Marcel Santilli:** Right.

**Marcel Santilli:** Like, like, like okay, so like take Kristen, right.

**Marcel Santilli:** Like the more we have multiple bridges to people like that the better.

**Marcel Santilli:** You know, I'm like, and I think you've done that with some folks.

**Marcel Santilli:** Like some of the ones that came.

**Marcel Santilli:** I think it was like bao and a few others or you know, like I think it's through you.

**Marcel Santilli:** So that's great.

**Marcel Santilli:** So then what are other ways we can, you know, it's like yeah, like how do we bribe these people to be our friends?

**Marcel Santilli:** Kind of.

**Marcel Santilli:** It's like I don't know, like cinema warriors game.

**Marcel Santilli:** Like Michelin star dinners.

**Marcel Santilli:** Like who cares?

**Marcel Santilli:** Like you know, it's such high leverage.

**Marcel Santilli:** Tapping into people's network is the most high leverage thing we have.

**Marcel Santilli:** And you know, it's like a deal is worth five grand to us right now.

**Marcel Santilli:** Right.

**Marcel Santilli:** So then like you, you know that math in your head.

**Marcel Santilli:** So it's like okay, like hey, give me a referral.

**Marcel Santilli:** Right.

**Marcel Santilli:** Like, but that's too transactional.

**Marcel Santilli:** So then it's like how do you, you know.

**Jason Gong:** Yeah.

**Marcel Santilli:** Figure out what's in it for them?

**Jason Gong:** I think we have all the tools.

**Jason Gong:** It's like like that's how I'm thinking about the community now.

**Jason Gong:** I'm less so just trying to grow the membership and it's more of like a, like a thing to give people.

**Jason Gong:** Right.

**Jason Gong:** It's like if somebody likes our workshops, like hey, for your whole team, you know, here's, here's a year free.

**Jason Gong:** Here's six months free.

**Marcel Santilli:** Yeah, no, it's great.

**Marcel Santilli:** Don't worry about monetizing as much.

**Marcel Santilli:** But the, the thing we used to do well, right.

**Marcel Santilli:** I think is even before you join.

**Marcel Santilli:** Yeah, it was before you join.

**Marcel Santilli:** But I would just hit up like VCs and I would just hit up like you know, Dan or you know, somebody else.

**Marcel Santilli:** And it's like we're always doing things with other people, you know, and we're always like.

**Marcel Santilli:** And not individuals because like now what I'm finding with these individuals is like man, they're kind of flaky, they don't pull their weight, they're busy, they have a full time job.

**Marcel Santilli:** And so like you know, we can nurture like we could create like a directory by the way on the community where we list some of these fractional people and you know, we become like a little bit of the broker of these people could be interesting.

**Marcel Santilli:** But until we have deal flow or we have what they want, they're like Branko might be seems to be good, but I don't know, they don't seem to do a lot unless it's really something.

**Jason Gong:** What was the most impactful one you did today?

**Jason Gong:** That is what you're describing.

**Marcel Santilli:** Oh man.

**Marcel Santilli:** We did one with a vc.

**Marcel Santilli:** I forgot their name but that dinner was really good.

**Marcel Santilli:** We filled the room with like two or three with VCs and they were just like very like turnkey easy and they help fill the room.

**Marcel Santilli:** But most a little bit.

**Marcel Santilli:** But most importantly because you did it with the vc, everybody wants to network with the vc.

**Marcel Santilli:** So that was easy.

**Marcel Santilli:** I think the Lamar one was the great example, right.

**Marcel Santilli:** It's like we pulled it off in two weeks and we filled the room with like the best people.

**Marcel Santilli:** We wanted everybody.

**Jason Gong:** I mean Upside had a good network and they, I guess we hadn't done one in a while.

**Jason Gong:** Like do you think Madrona is the right person to do it because we tried doing that.

**Marcel Santilli:** No, no, like VCs is just like nothing to do with like, like the traditional.

**Marcel Santilli:** Like, like Norwest just reached out to me asking for a meeting.

**Marcel Santilli:** Right.

**Marcel Santilli:** It's like so, so I can use these VC calls, pretend like we're raising or something and, and like we can use it to our advantage.

**Marcel Santilli:** Like you know, and, and it's like whatever, you know.

**Jason Gong:** Okay.

**Jason Gong:** I mean if you find a good one center away, like especially if it's outside of the Bay Area.

**Jason Gong:** Because I think we're still like taxing this area out.

**Jason Gong:** So with HubSpot we're looking at a couple things.

**Jason Gong:** But I saw that list today.

**Jason Gong:** We'll, we'll work on it.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Okay.

**Marcel Santilli:** Yeah, The.

**Marcel Santilli:** And then like you need some that are like the consistent layer.

**Marcel Santilli:** Right.

**Marcel Santilli:** Like paid search tends to be that, like some gated content, you know, like that, that is usually like your, like that should be your no brainer, you know, spin up some quick nice landing pages.

**Marcel Santilli:** Do some, drive some people there, you know, do some gated stuff.

**Jason Gong:** Yeah.

**Jason Gong:** I mean it's not beautiful but like every week I think we get like 150 to 200 various sources.

**Jason Gong:** They're all in alg.

**Jason Gong:** They go in the newsletter.

**Jason Gong:** That flywheel is there.

**Jason Gong:** I think we need to make it better.

**Marcel Santilli:** We need like one asset.

**Marcel Santilli:** So I was thinking like, Like one thing that we just pack the out of it.

**Marcel Santilli:** You know, it's like, like I think it's the AO master class.

**Marcel Santilli:** But it's just like, hey, I don't know, it's just like let's just do the.

**Marcel Santilli:** Maybe it's the AO masterclass.

**Marcel Santilli:** It's like one time.

**Marcel Santilli:** It's going to be four hours.

**Marcel Santilli:** We're going to teach everybody everything.

**Marcel Santilli:** There's no about ao.

**Marcel Santilli:** And we're also going to have like a handbook that if you sign up for the workshop, you know, and we just say like we do a one time.

**Marcel Santilli:** It's like $500 but for one time like we're, we're giving away the first like a hundred or whatever.

**Marcel Santilli:** Like I, I don't know, like some, some something that like feels really meaty.

**Marcel Santilli:** But I, I do think like I want us to get like a, like our reference docs should be the thing that we give it away.

**Marcel Santilli:** You know what I mean?

**Marcel Santilli:** Like, like what is our reference doc of like the AEO strategy, how we think about it.

**Marcel Santilli:** Like which for me is it's like can we take the like a little bit of like kind of like it can be simple, you know, it doesn't need to be slides.

**Marcel Santilli:** It could be like you can turn this into like graphics and then put it into a nice page or PDF or something.

**Marcel Santilli:** But then also have a page.

**Marcel Santilli:** Like there's some unlock there.

**Marcel Santilli:** I think of like I had send the design team like something on which was a lot of here.

**Jason Gong:** Let's see.

**Marcel Santilli:** I said, oh, this is cool.

**Marcel Santilli:** Yeah, like this.

**Jason Gong:** Yeah, I saw this.

**Marcel Santilli:** You know, I don't know, maybe he's moving too fast to do something like this, but if you look at like the Sam from Mastra, like he's been.

**Marcel Santilli:** Like, he keeps promoting this one book, this, like, literally every time he posts, it's just like it blows up and he gives it away for free.

**Marcel Santilli:** So two levers we have, I think for like broader is like Alex Ortiz mentioned that in the dinner.

**Marcel Santilli:** He's like, you all are the, like, how to be more AI native.

**Marcel Santilli:** And so I think we need to double click on that and then we need to double click on like owning the AO space.

**Marcel Santilli:** And I have a really good angle that I think it's going to be like.

**Marcel Santilli:** I don't want to quite yet do a post about it because I want to shape up the product a bit more towards it.

**Marcel Santilli:** But I, I do think it's a better mental model and a way to think about the whole thing.

**Jason Gong:** Yeah, I mean, I guess the system this fits into for me is like the bottom layer of value is like the.

**Jason Gong:** The dinner is breakfast, virtual events and the AEO strategy session and then the top.

**Jason Gong:** We kind of need something a little bit more scalable and immediate.

**Jason Gong:** Yeah, that right now is kind of, you know, the workshop recordings, a few lead magnets.

**Jason Gong:** Is this where you think like, what you're describing?

**Jason Gong:** This kind of just like something interesting, right?

**Jason Gong:** It's like, oh, shit, I really want that.

**Jason Gong:** Like, is that where you think this, this fits in, like this book that you're showing?

**Marcel Santilli:** Yeah, it's just like we're.

**Marcel Santilli:** We have so many things that I think we'd be doing the Influencer game, you know, and, and, and I think like, like, let me give you an example.

**Marcel Santilli:** Those guys, like, master class here, right?

**Marcel Santilli:** Like, he's.

**Marcel Santilli:** For 10x, he's a guy that did the Morning Brew.

**Marcel Santilli:** And, and it's like he has this.

**Jason Gong:** Newsletter.

**Marcel Santilli:** That is good, right?

**Marcel Santilli:** And then call Ultrathink.

**Marcel Santilli:** You know, but it's like branded and it's like kind of like we have our newsletter, but.

**Marcel Santilli:** But it's like, you know, so it's.

**Marcel Santilli:** And then, and then he has playbooks.

**Marcel Santilli:** It's super simple, right?

**Marcel Santilli:** Like, but then it's like all the, like videos he's doing, he like turns them into a playbook, but then he also releases the, the thing as well.

**Marcel Santilli:** Right.

**Marcel Santilli:** But then the playbook is just like a process of the transcript, plus like some other things making more practical or whatever.

**Marcel Santilli:** You Know, like, but it's like a little bit more generic, and so ours can't be like a yo everywhere kind of, you know, like, our content everywhere has to be like, way, way more, and we just need more shots on goal and then we package it up maybe.

**Marcel Santilli:** But the cascade needs to start from something that works already.

**Marcel Santilli:** And I think we've had the things that worked before.

**Marcel Santilli:** And then there's ways to tap into other networks, right?

**Marcel Santilli:** It's like, dude, I can do, put me in any of these here.

**Marcel Santilli:** I, I can do this in my sleep.

**Marcel Santilli:** You know what I mean?

**Marcel Santilli:** Like, I can talk for.

**Marcel Santilli:** I almost guarantee you not to be arrogant, but like, I, I, I will do a better job than anyone here, right?

**Marcel Santilli:** But then like, look, this guy's the guy here, right?

**Marcel Santilli:** So then it's just like, yeah, fuck, like, why is this guy here, right?

**Marcel Santilli:** Like, so maybe like, there's a way for us to like, it's like, take this, create a better one and like, let's just go, right?

**Marcel Santilli:** Like, and so I like, but I also understand I've got so much going on.

**Marcel Santilli:** So things like, we got to structure in a way that's like, more repeatable.

**Marcel Santilli:** And, and it's all like, you know, like, there's so many videos, so many things, and, and like, I can record more.

**Marcel Santilli:** And I told Will to come and like, set up in my, my house because then I can just record because I'm doing so much right now.

**Marcel Santilli:** That will be high leverage, but gotta get that kind of like, like this engine going and build a cadence.

**Marcel Santilli:** But in order to have a cadence of publication, you got to figure out, hey, if it takes two weeks to produce a video, you know, from ideation to fully done, ready to publish, or four weeks, that means you need to have like four weeks worth of stuff ready to go already, right?

**Marcel Santilli:** And then you got to figure out what are your sources, like, who are the brains behind it?

**Marcel Santilli:** Is it Marcel?

**Marcel Santilli:** Is it you?

**Marcel Santilli:** Is it someone else?

**Marcel Santilli:** And how can you build diversity into it, you know?

**Marcel Santilli:** And like, what is the themes?

**Marcel Santilli:** It's like essentially the content strategy we do for all our clients, but we need to do like a legit one for us.

**Marcel Santilli:** You know that that is like, no, this is the content strategy.

**Marcel Santilli:** And that way we can be a little bit more than like this one masterclass for two months, right?

**Marcel Santilli:** That then it's just like, doesn't quite get traction.

**Marcel Santilli:** It's more like you find like the hooks, the angles, and it's just like, we just like, fuck it, don't depend on anybody.

**Marcel Santilli:** And then once you build enough audience and everybody's going to want to be part of it, you know?

**Marcel Santilli:** And then once you have enough cadence going, then you can start bringing in guests.

**Marcel Santilli:** And then each one of those videos or episodes or whatever, like, we just force ourselves to do it.

**Marcel Santilli:** And, Danny, you and others just, like, build enough, like, homework there or grab my calls or grab my things or whatever, right?

**Marcel Santilli:** Like, prepare it a little bit more.

**Marcel Santilli:** And.

**Marcel Santilli:** And then we have, like, design assets and everything.

**Marcel Santilli:** The episode launches.

**Marcel Santilli:** There's a newsletter.

**Marcel Santilli:** There's like an asset, a playbook or something, you know, and then we also do some live sessions as well, like, you know what I mean?

**Marcel Santilli:** Like, so.

**Marcel Santilli:** So maybe that's what we need to kind of, like, shape, because I feel like we're doing a lot of the right things.

**Marcel Santilli:** It's just, like.

**Marcel Santilli:** It hasn't quite connected to where it's just like, okay, it's going, right?

**Marcel Santilli:** Cause, like, when I.

**Marcel Santilli:** When I.

**Marcel Santilli:** Like when I spent all this time to just get, like, the.

**Marcel Santilli:** The.

**Marcel Santilli:** The.

**Marcel Santilli:** Like, one workshop going and the hook was really strong, everything else was so much easier, you know?

**Marcel Santilli:** And then the second one, I got 50 people to it, paying 500 bucks.

**Marcel Santilli:** I was like, like, you know?

**Marcel Santilli:** And.

**Marcel Santilli:** And so it's like, I feel like we got the muscles, we just kind of, like, narrow the aperture in a way that, like, unlocks more, you know?

**Jason Gong:** Yeah.

**Jason Gong:** I even get the core of it, right?

**Jason Gong:** Because we are doing a lot of the stuff, right?

**Jason Gong:** It's, like, cool.

**Jason Gong:** We have a page for lead magnets.

**Jason Gong:** We have, like, YouTube videos.

**Jason Gong:** We have all this stuff, but it doesn't feel as cohesive as, like, that Greg Eisen guy or this guy that you're showing me.

**Marcel Santilli:** Yeah, yeah.

**Marcel Santilli:** It's just not consistent enough.

**Marcel Santilli:** Right.

**Marcel Santilli:** So people don't know.

**Marcel Santilli:** You can't build an audience if you do, like, one time, Right.

**Marcel Santilli:** And so, like, for instance, like, it's great we did the stuff with Danny, but it's like, okay, cool.

**Marcel Santilli:** Like, what's the next one?

**Marcel Santilli:** Like, is it ready to go?

**Marcel Santilli:** Or.

**Marcel Santilli:** We're thinking about it right now.

**Marcel Santilli:** Like, and then it's like, how does this connect to the next thing?

**Marcel Santilli:** And was there an offer in this?

**Marcel Santilli:** Probably there was.

**Marcel Santilli:** And so then it's like, okay, cool.

**Marcel Santilli:** Like, and then everything kind of, like, connects, and then, like, we're validating.

**Marcel Santilli:** Okay.

**Marcel Santilli:** Is this, like.

**Marcel Santilli:** Like, it's almost like you need the flow to go into, like, tried and true things that have already been validated, you know?

**Marcel Santilli:** Because, like, if this hasn't been validated and it's not flying off the shelf.

**Marcel Santilli:** AKA you posted on LinkedIn and blew.

**Marcel Santilli:** Then it's not validated yet.

**Marcel Santilli:** So you should send people always to just like your highest value, most validated, no brainer value of like AKA get access to the community for free, you know, like.

**Marcel Santilli:** Or whatever the bundle of value is, you know, that is like the most like legit or like getting like the, you know, like get the flow.

**Marcel Santilli:** Right?

**Marcel Santilli:** I don't know.

**Jason Gong:** Yeah.

**Jason Gong:** Yeah.

**Jason Gong:** Okay.

**Jason Gong:** I mean I totally understand what you mean and I think the like maybe the good part is like the connection as far as like like the journey is there.

**Jason Gong:** The content just feels scattered.

**Jason Gong:** I need to think about how to.

**Jason Gong:** Yeah, I'm connected or anchor it in the right thing.

**Jason Gong:** I don't know.

**Marcel Santilli:** Yeah, I.

**Marcel Santilli:** Right now I think what works is like I. I'm decently compelling.

**Marcel Santilli:** Danny's awesome on camera.

**Marcel Santilli:** Will can do and is also super ag native.

**Marcel Santilli:** She should be on camera more too and do more content.

**Marcel Santilli:** Like more than the.

**Marcel Santilli:** You know.

**Marcel Santilli:** And we can do more sessions with like the.

**Marcel Santilli:** The three or four of us like just talking and being like showing things.

**Marcel Santilli:** And it's like we'll taking you know, you and Danny through or me and Danny through it or you know, Dan, you know, like, like what.

**Marcel Santilli:** Whatever combo it is.

**Marcel Santilli:** But it's just like you can bring in more, more guests.

**Marcel Santilli:** It could be me and Danny.

**Marcel Santilli:** It can be you and Danny can be me and you.

**Marcel Santilli:** It can be me and Will.

**Marcel Santilli:** It can be like any combination of things, you know, like we have like four people that can and should be.

**Jason Gong:** Able to do it.

**Marcel Santilli:** That would be like a.

**Marcel Santilli:** And.

**Marcel Santilli:** But then you have like the distribution piece and the distribution piece, I think where I gotta spend more time on my social.

**Marcel Santilli:** And then in the meantime though, like if like what is our best highest intent offer we have, can we brute force that?

**Marcel Santilli:** Can we do some landing pages like take.

**Marcel Santilli:** Take out campaigns on other agencies?

**Marcel Santilli:** Like dude, there's so many agencies.

**Marcel Santilli:** We had a lead come in, word of mouth referral that wants to pay us 18 grand a month upfront.

**Marcel Santilli:** Like or not front but like you know, 12 month contract.

**Marcel Santilli:** Tyler tried to DQ and the guy's like, it's our surgeon essentially.

**Marcel Santilli:** Like, you know I saw that email.

**Jason Gong:** Yeah.

**Marcel Santilli:** You know, it's like, dude, like there's so much business to be had out there that's just like way easier than trying to sell to like lovable or vercel, you know, like, like there's agency business to be had that are.

**Marcel Santilli:** There's so much man, there's like an insane amount, you know?

**Jason Gong:** Yeah.

**Jason Gong:** All right.

**Marcel Santilli:** I mean let's spend time can compete with that.

**Marcel Santilli:** They're not going to go pitch an agency pitch.

**Marcel Santilli:** We can go do an agency pitch, you know, go get that.

**Marcel Santilli:** Lane Darling I think can be a no brainer, you know, like pay search like directive.

**Marcel Santilli:** Like it's like I don't know, $50 million business, something like that.

**Jason Gong:** You know, like they're conductor.

**Jason Gong:** They're like really big too.

**Marcel Santilli:** They're like legit, you know, I mean they do a bunch of other stuff but like they, they do a lot of, a lot of stuff here, you know.

**Marcel Santilli:** So I think it's like we'll feel better the more we like do a few things.

**Marcel Santilli:** Also get our SEO game going really strong all in all places.

**Marcel Santilli:** And so then if we get like hey, I LED growth to get some really good at SEO and a yo, we get growth X to get some good SEO and I'll check that.

**Marcel Santilli:** It's like a massive engine, right?

**Marcel Santilli:** Like we get.

**Marcel Santilli:** We essentially have like three engines to control.

**Marcel Santilli:** That could be good too.

**Marcel Santilli:** Yeah, yeah, no that makes sense.

**Jason Gong:** I mean I think like, like I would almost like.

**Jason Gong:** I think you're right.

**Jason Gong:** The core of what we're offering is like a bit all over the place and we're.

**Jason Gong:** There's like too many and none of them's really amazing.

**Jason Gong:** I think that like if we have something amazing, can we actually bring people to it?

**Jason Gong:** Like that part I'm almost a little bit more confident in.

**Jason Gong:** We have like a decent machine building there where I would want to do less like cool.

**Jason Gong:** A bunch of like YouTube videos on our own channel and just one like lead magnet that really you know, converts people because you can always buy eyeballs.

**Jason Gong:** Like I would much rather spend.

**Marcel Santilli:** Yeah, we can, but we have a lot of stuff out there.

**Marcel Santilli:** So it's like validate that you can get somebody to sign up that is like a good lead and figure out how much that costs.

**Marcel Santilli:** Right.

**Marcel Santilli:** Like and so get, get an offer in and I think right now given everything it would be a lot better to do like even like a guide plus a strategy session landing page on growth X.

**Marcel Santilli:** Right like with a bunch of proof and just like a really good thing like landing page.

**Marcel Santilli:** It's like an LP and open up a few channels and see like can you get conversion and good leads there?

**Marcel Santilli:** You know, like try like more of the like traditional demand gen stuff because if, if you get like two ops a week from there now it's like okay, you know what I mean?

**Marcel Santilli:** Like and then we get like the lightning sessions going again with just me as like, you know, you can get other people too, but it's just like.

**Marcel Santilli:** Like get a couple of those, like, really, really strong.

**Marcel Santilli:** Like get to a thousand people.

**Marcel Santilli:** And then like, so we always have like two we're planning, you know, one that's scheduled but we're not promoting, and one that we're promoting really hard.

**Marcel Santilli:** That's like four weeks out, you know, and.

**Marcel Santilli:** And then maybe we like, we reduce the weight on the.

**Marcel Santilli:** The workshops and make just them, like two hour lightning sessions, you know, like.

**Jason Gong:** Like that is the two we have now.

**Jason Gong:** So we have like one AO one which maybe could turn into this lightning one.

**Jason Gong:** And then we have a co hosted.

**Marcel Santilli:** One AO one is with Guy.

**Jason Gong:** Sorry, say that again.

**Marcel Santilli:** Which one is the AO one?

**Jason Gong:** The AO one is actually with us, just about Check that.

**Jason Gong:** I was thinking it could be about like running an audio audit.

**Jason Gong:** You can make that a lightning session.

**Jason Gong:** I'm gonna look at Maven right after this.

**Jason Gong:** And then the other one is with Fletch.

**Jason Gong:** And the whole playbook there is like, not really driving our audience to it.

**Jason Gong:** I'm just going after his audience and using it as the lead magnet.

**Jason Gong:** And it's like, I know it's only 20 people, but it's like 200 net new people.

**Jason Gong:** And it's kind of effective.

**Jason Gong:** We still have two weeks left to promote.

**Jason Gong:** So that's kind of the current cadence there.

**Marcel Santilli:** Where are you managing that calendar right now?

**Marcel Santilli:** Or how do we.

**Jason Gong:** Like, it's in notion.

**Jason Gong:** I can send you that.

**Jason Gong:** And it's also, I guess if you.

**Marcel Santilli:** Go into Luma, I think it's just like, It, like we gotta like, form and bring everybody along.

**Marcel Santilli:** And I think you might be doing that already with your team, but.

**Marcel Santilli:** But it's just like, we gotta form it and then like have like a beat.

**Marcel Santilli:** So.

**Marcel Santilli:** So.

**Marcel Santilli:** So maybe like, what would be more helpful is instead of these, like, let's spend the time like, form this, put it in a place that, like, it's all in one place so that we kind of see it and maybe it's already there, but it's like, you know, that we can kind of plan against it.

**Marcel Santilli:** And then our meeting should be like, the things that are driving up to that and what needs to happen.

**Marcel Santilli:** And it's like, one is like operational.

**Marcel Santilli:** The other side is like editorial.

**Marcel Santilli:** But the editorial is just like, you kind of have to have like, people pitching things, you know, like, okay, that's what I'm thinking, you know, like.

**Marcel Santilli:** And then you kind of like, bounce off of each other and.

**Marcel Santilli:** And then, like, form that a little bit, you know?

**Marcel Santilli:** But I think, like, the framing, I can.

**Marcel Santilli:** I can help with that of, like.

**Marcel Santilli:** Like a few of the.

**Marcel Santilli:** The, like, anchor pieces, you know, and see if you can get Danny to come.

**Marcel Santilli:** Does she have a visa?

**Jason Gong:** She's American.

**Jason Gong:** Yeah, she can come.

**Marcel Santilli:** Okay, perfect.

**Marcel Santilli:** So can we get Danny to see if she wants to fly out and.

**Marcel Santilli:** And spend, like, a week or so here?

**Marcel Santilli:** We'll get you.

**Marcel Santilli:** Me will.

**Marcel Santilli:** Gloria can come too.

**Marcel Santilli:** So.

**Marcel Santilli:** So we, like, just, like, spend a few days just, like, here, like, produce a bunch of stuff.

**Marcel Santilli:** Like, you know, like, let's just, like, plan ahead of that, too.

**Jason Gong:** Yeah, that's good.

**Jason Gong:** Let's see.

**Jason Gong:** Okay.

**Jason Gong:** Next couple weeks are all in town.

**Marcel Santilli:** Yes.

**Marcel Santilli:** I think the only thing I have is going to be.

**Marcel Santilli:** I think I'm taking the 12 and 13 off to go to Salt Lake City.

**Marcel Santilli:** But then I see a VIP dinner on the 12, but I think we moved that right on March or.

**Jason Gong:** No.

**Marcel Santilli:** I don't know where the source of truth is.

**Jason Gong:** I don't.

**Jason Gong:** It's not on my calendar.

**Marcel Santilli:** Yeah, somebody put something in my calendar.

**Marcel Santilli:** I'm gonna delete it.

**Marcel Santilli:** Dig.

**Jason Gong:** Put it there.

**Jason Gong:** But it's like.

**Marcel Santilli:** I don't know.

**Marcel Santilli:** It's actually there or not.

**Jason Gong:** Because it's.

**Marcel Santilli:** In my calendar, but not the marketing events calendar, so I'm assuming.

**Jason Gong:** Okay, cool.

**Jason Gong:** All right.

**Marcel Santilli:** And then I have the Madrona event on the 24th, and.

**Jason Gong:** And then we're in Seattle for that.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Tactically, I invited a bunch of people to the.

**Marcel Santilli:** The one next week, but, you know, I think we have okay RSVPs.

**Marcel Santilli:** But, like, how are you feeling?

**Jason Gong:** Talk to Gloria.

**Jason Gong:** Like, 17.

**Jason Gong:** I think we at least, like, seven or eight more.

**Jason Gong:** But I haven't talked to Gloria yet about that.

**Jason Gong:** It's mostly handling.

**Jason Gong:** I mean, we are offering it.

**Jason Gong:** Like, the thing I am doing is doing some warm outreach on, like, Clothes Lost and, like, warm people from the workshops.

**Jason Gong:** And I'm offering the dinner there, so I think that'll help fill a few seats.

**Jason Gong:** Okay.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** I think, like, with.

**Marcel Santilli:** What they think, like, some of these, like.

**Marcel Santilli:** Like that one is like, There's.

**Marcel Santilli:** We can kind of fill the room more aggressively on that one, you know, For the 19th.

**Marcel Santilli:** But then also, like, the breakfast, we can start going more, like, director level and more broad as well.

**Jason Gong:** Yeah, I mean, I feel like the breakfast is the one that needs more work in both of them.

**Jason Gong:** It's like, same day, so it's like.

**Jason Gong:** Yeah, I guess we're cutting our audience a little bit.

**Marcel Santilli:** Yeah.

**Jason Gong:** And then Guy actually is unresponsive.

**Jason Gong:** I flagged that in there.

**Jason Gong:** I don't know what's going on for the.

**Jason Gong:** For the breakfast, which I guess is fine, but I mean.

**Marcel Santilli:** Yeah, I mean, it's the day of the event.

**Marcel Santilli:** He's getting pulled into.

**Jason Gong:** Yeah.

**Jason Gong:** Same with.

**Marcel Santilli:** Is that why Caddy said she bailed out?

**Jason Gong:** I. I have no idea.

**Jason Gong:** To you and did she say anything to you?

**Jason Gong:** She basically just like, pinged the Slack channel and then Gloria followed up, but she was busy.

**Marcel Santilli:** Yeah.

**Jason Gong:** Yeah.

**Jason Gong:** Well, good.

**Marcel Santilli:** We just need to.

**Marcel Santilli:** We don't need anybody to like, create great content and get audience.

**Marcel Santilli:** Like, I know how to get a thousand people.

**Marcel Santilli:** It's just like.

**Marcel Santilli:** It's just mostly get the content right and the hook right.

**Marcel Santilli:** It's.

**Marcel Santilli:** It's there, but it's like, it's a lot of work, you know, it's like, yeah, getting it right.

**Marcel Santilli:** Just like even the announcement post was like, still like a solid two hours of uninterrupted time to try to get it right, you know, like.

**Jason Gong:** Yeah, that's what I'm like.

**Jason Gong:** I don't know what your thought is on the unlock there or if that can ever be unlocked of like, I.

**Marcel Santilli:** Think the comments is a good starting point because it triggers my brain and then like, I can just like whisper flow something and then process it through like.

**Marcel Santilli:** Like my.

**Marcel Santilli:** My cursor and skill.

**Jason Gong:** Yeah, that.

**Marcel Santilli:** So like, that.

**Marcel Santilli:** That part is not the hard part.

**Marcel Santilli:** I think what would be helpful is like, the things that's.

**Marcel Santilli:** Like, I start to form them.

**Marcel Santilli:** Like for instance, like the All Hands, you know, it's like there's no way.

**Marcel Santilli:** We can't get like that 15 minutes of me walking through the mental model and not have at least like four graphics and four good, like, form things, you know, out of it or hooks, you know, I. I built a workflow with output AI too, but I need to refine it a little bit more.

**Marcel Santilli:** It's like, there we go.

**Marcel Santilli:** Here it is.

**Jason Gong:** Like.

**Marcel Santilli:** So.

**Marcel Santilli:** So anyways, it's like, it's pretty.

**Marcel Santilli:** Pretty decent.

**Marcel Santilli:** It's like it analyzed the all hands, you know, and then I built this UI just to visualize it.

**Marcel Santilli:** And then the output, it's like it did like three posts on it, but, you know, has the hook tab text.

**Marcel Santilli:** But it's okay.

**Marcel Santilli:** Like, it needs refining, but.

**Marcel Santilli:** But it's like the bones are there.

**Marcel Santilli:** It just needs more refining on the.

**Marcel Santilli:** On the prompts, you know, but.

**Marcel Santilli:** But it has like, hook quality, voice match structure, CTA quality, overall score.

**Jason Gong:** Do you think the like, version of this that you would find helpful is like, there's somebody in the loop.

**Jason Gong:** It's not you running this and maybe pre filtering it and then you just kind of load it and yeah, it's.

**Marcel Santilli:** Almost like, like fetching, you know, from, from like my calls or something and coming up with like good hooks or finding like even like examples of things historically that have done well in other people.

**Marcel Santilli:** It's just like, gosh, like, you know, just fetch ideas and then I can pattern match those ideas, you know, and then it's like.

**Marcel Santilli:** And then like a library of those that were refining, you know, there are more.

**Marcel Santilli:** Like, then I think then when I'm like it and also like a visual system because like I'm.

**Marcel Santilli:** I'm like a visual person.

**Marcel Santilli:** So if I have like this, like, you know, then okay, like, like I can write five posts on this now.

**Marcel Santilli:** Like, you know what I mean?

**Marcel Santilli:** Like, like and we just gotta find a style.

**Marcel Santilli:** Like, I like TL draw.

**Marcel Santilli:** Like, but maybe it's like something like this, you know, it's just kind of like, like, I don't know, something that becomes like our style.

**Marcel Santilli:** It's like my scribbles or something, you know, like mental models that looks nothing too fancy and you know, like, Like, I don't know.

**Marcel Santilli:** Can I. I'm.

**Marcel Santilli:** I haven't used like.

**Marcel Santilli:** What do you use, like Gemini to.

**Jason Gong:** Do images like Nano Banana.

**Jason Gong:** You gotta.

**Jason Gong:** You gotta go in.

**Marcel Santilli:** Like this guy.

**Marcel Santilli:** I mean, this is just like the lazy version, but maybe there's like something that we can do.

**Marcel Santilli:** Like just turn some of these, you know, like.

**Marcel Santilli:** And then from the, the mental model build thing with social is like, I. I know how to do, but I need a clear mind, you know, and.

**Marcel Santilli:** And I need to be able to throw my ideas over the fence and, and have a holding pattern to do that, you know, but then have other people there.

**Marcel Santilli:** So it's like, I don't know if like the air table or something or, you know, it's like, yeah, like, dude, this is pretty good.

**Marcel Santilli:** I mean, it can be better, but it's like, you know what I mean?

**Jason Gong:** Like, yeah, maybe it's like, I feel like we need to take more variables away.

**Jason Gong:** It's like there needs to be a very structured type of post and then we start there instead of trying to do too much, you know.

**Jason Gong:** So if.

**Jason Gong:** If that is.

**Jason Gong:** So this to me is like, okay, so an infographic, but like a framework, essentially.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** I mean, like, I have a lot of stuff.

**Marcel Santilli:** Like for instance, like, I have this like.

**Marcel Santilli:** Like hooks, like study guide for Example.

**Marcel Santilli:** And then that's like.

**Marcel Santilli:** Talks about like the, the different, like, ways to do hooks and you.

**Marcel Santilli:** But I haven't, I just haven't spent enough time like, trying to like, adapt it, you know.

**Marcel Santilli:** But, but I mean, like, the one you did on offers was really good.

**Marcel Santilli:** Your LinkedIn post on offers, like, just give me that, like, you know, tweak it a little if you want.

**Marcel Santilli:** But it's like that exact thing on offers was really good.

**Marcel Santilli:** So it's almost like, can we use yours as the training ground?

**Marcel Santilli:** Yours and Danny as your train as the training ground.

**Marcel Santilli:** So it's like, if you're unsure about me, like, go do it as it's you.

**Marcel Santilli:** And if it does, well, post it on my.

**Marcel Santilli:** On mine a week later.

**Marcel Santilli:** Who cares?

**Marcel Santilli:** You know, like, that's.

**Marcel Santilli:** That could be another way, you know.

**Jason Gong:** Okay.

**Jason Gong:** The.

**Jason Gong:** The common stuff feels okay.

**Jason Gong:** I know you met with, with Danny.

**Jason Gong:** I haven't caught up with her yet, but anything needed there, I haven't acted on it.

**Marcel Santilli:** It's.

**Marcel Santilli:** It's like right now I'm like, I need Dig.

**Marcel Santilli:** I need somebody to like, make Dig more like, high leverage for me, you know?

**Marcel Santilli:** And like, it's like I have nobody to delegate anything to right now because, like, George is on onto better, bigger things.

**Marcel Santilli:** Dig is unmanaged and.

**Marcel Santilli:** And we haven't found a chief of staff and so.

**Jason Gong:** Got it.

**Marcel Santilli:** I need to, like, that's why I'm building this like, context directory.

**Marcel Santilli:** Because then, like, it's a lot easier than talking about it.

**Marcel Santilli:** It's like, you know, could have just.

**Jason Gong:** Yeah, yeah.

**Jason Gong:** Okay, let's see the last thing before you drop.

**Jason Gong:** Uncheck that.

**Jason Gong:** Just because I feel like you're also working on pieces of it and I just want to know what parts of it.

**Jason Gong:** So like, yeah, top of funnel.

**Jason Gong:** I'm just going to call out a bunch of tickets.

**Jason Gong:** I mean, Stevie and Daniel are both aware and they're like, cool, we'll get to it this week now that the launch is over.

**Jason Gong:** But I'm just flagging that there's like a lot of extremely high leverage things that will, two, three, whatever X our growth there.

**Jason Gong:** They're just APD has no time.

**Jason Gong:** And then also flag that.

**Jason Gong:** Like, it feels like the product experience.

**Jason Gong:** Like, I know you're working on it, but just, you know, like, everyone's coming in, nobody's adding custom prompts and as a result nobody's upgrading to pro.

**Jason Gong:** And like, that needs attention, which I think you're.

**Jason Gong:** You're putting there.

**Marcel Santilli:** Unwear.

**Jason Gong:** Just uncheck that.

**Jason Gong:** Like, I feel like the self serve, like experience just is not like resonating, you know, Like I don't see people getting deeper.

**Jason Gong:** Like they.

**Jason Gong:** Yeah, they sign up, you know, and they drop off.

**Marcel Santilli:** Yeah, yeah, for sure.

**Jason Gong:** The strategy sessions were rolling.

**Jason Gong:** I mean, we have two books so far, but we're sending like a ton of emails.

**Marcel Santilli:** And yeah, like.

**Marcel Santilli:** The.

**Marcel Santilli:** There's like two big, big things that are then going to allow us to then do a few other things that will take it a step up.

**Marcel Santilli:** But the first one is like the taxonomy.

**Jason Gong:** So I don't know if you saw.

**Marcel Santilli:** The loom from Daniel on the taxonomy.

**Jason Gong:** Did you get.

**Marcel Santilli:** But he has a loom, like demoing what he built, but.

**Marcel Santilli:** And then Jose's taking to the finish line.

**Marcel Santilli:** But the taxonomy is like custom taxonomy on the business.

**Marcel Santilli:** And so like if you get the taxonomy right, the next thing is auto tag prompts and then in parallel to that is like a prompt generator, which is very similar to the workflow we have for generating prompts for the, for the categories.

**Marcel Santilli:** But this is like for an individual account.

**Marcel Santilli:** So then you have essentially like three really powerful workflows.

**Marcel Santilli:** Then you got to get it to a place where you know they're fast enough, good enough and not expensive enough.

**Marcel Santilli:** So that's a little bit of a minor challenge.

**Marcel Santilli:** But like, but it's all good and you nail those three and you essentially it is the strategy, the AO strategy in a lot of ways, right?

**Marcel Santilli:** Like, it's like kind of like your prompt strategy and, and kind of like why you're doing what you're doing.

**Marcel Santilli:** Then from there then it's about like more of the scoring and the views that today just don't click because it's just like, so what, I'm 30, 40, or what?

**Marcel Santilli:** Like sentiment means nothing.

**Marcel Santilli:** Like share of voice kind of means nothing.

**Marcel Santilli:** So, so it's like the visualization is not the issue, it's just that the metrics are not meaningful to people, right?

**Marcel Santilli:** It's like, okay, so what?

**Marcel Santilli:** Right?

**Marcel Santilli:** And so like that's the, the unlock of like the, the part that I have a, a strong hypothesis which is like ultimately like a way to kind of think about it is like the.

**Marcel Santilli:** Gosh, what is that?

**Marcel Santilli:** So, so the, the, the kind of like way to think about it is like you have like three like layers, the context, instruments and measurement.

**Marcel Santilli:** And I'm not calling instruments, but just like, just, just bear with me for a minute, right?

**Marcel Santilli:** Like in the mental models, like check that like you run a Super bowl ad.

**Marcel Santilli:** How do you know if the super bowl ads was Effective or not.

**Marcel Santilli:** Right.

**Marcel Santilli:** You survey consumers and you say, were you exposed to this?

**Marcel Santilli:** Yes or no?

**Marcel Santilli:** If you were exposed to this, first of all, if you weren't exposed, then it's like, okay, it's like there's no way it impacted you.

**Marcel Santilli:** But.

**Marcel Santilli:** But if you were exposed.

**Marcel Santilli:** Now we're trying to figure out what, if anything, was there a lift in terms of recall, sentiment, alignment.

**Marcel Santilli:** Right.

**Marcel Santilli:** And so.

**Marcel Santilli:** And you're trying to influence that and in degree to which the thing you did lifted those things or improved those things or tighter alignment.

**Marcel Santilli:** Right.

**Marcel Santilli:** And so visibility is more of like, it's a recall metric.

**Marcel Santilli:** You know, like, I don't know if I want to use the word sentiment, but like, sentiment is more like the attributes of how, like, your brand is perceived.

**Marcel Santilli:** And alignment is like, how close is what AI thinks of you aligned to, like, your actual context, which is your grounding.

**Marcel Santilli:** And so that has to be your grounding.

**Marcel Santilli:** Right.

**Marcel Santilli:** You need to ground on something.

**Marcel Santilli:** AKA if like you say I, my platform does X, Y and Z, and this thing over here says your platform does X and this other competitor does Y and you don't, and you're really bad at Y, then like, that's misaligned.

**Marcel Santilli:** Right?

**Marcel Santilli:** And so, so then there's a.

**Marcel Santilli:** And then there's different ways for you to, like, measure these things.

**Marcel Santilli:** So like, recall is a lot of what we're doing, and it's recall with an evaluation.

**Marcel Santilli:** Right?

**Marcel Santilli:** Because if in a comparison, it's like, you already know, like, who you're comparing to.

**Marcel Santilli:** Right?

**Marcel Santilli:** And in other stages, you're not really looking for anybody.

**Jason Gong:** Right.

**Marcel Santilli:** And if you're looking for alternatives to you, then that means you're already looking for.

**Marcel Santilli:** You don't want you.

**Marcel Santilli:** Right.

**Marcel Santilli:** Like, so that's a different challenge.

**Marcel Santilli:** But like, within, like, a lot of what we're doing is like, recall, then.

**Marcel Santilli:** Then sentiment is about, like, these attributes of, like, how people, like, perceive you.

**Marcel Santilli:** Almost kind of like, you know, so I got to spend a little bit more time there.

**Marcel Santilli:** But it's ultimately like when, you know, like, describe ramp, like the.

**Marcel Santilli:** The.

**Marcel Santilli:** Or.

**Marcel Santilli:** Or like, it's.

**Marcel Santilli:** It's kind of like, is ramp expensive?

**Marcel Santilli:** Or like, you know, it's kind of.

**Marcel Santilli:** And then alignment is mostly like, is the saying the right things, yes or no, and then lift.

**Marcel Santilli:** Right on all of these.

**Marcel Santilli:** It's like about like the thing that influences that.

**Marcel Santilli:** A citation.

**Marcel Santilli:** Sure.

**Marcel Santilli:** There's often many things that influences.

**Marcel Santilli:** And we have.

**Marcel Santilli:** I've seen brands already in our dashboard that like, will have like a 1% citation rate, but then like a 80% visibility.

**Marcel Santilli:** And that means like they're just truly like a market leader or they're, they're like synonymous.

**Marcel Santilli:** Synonymous, like with the space.

**Marcel Santilli:** Like QuickBooks, for example, right?

**Marcel Santilli:** Like where.

**Marcel Santilli:** And they're mentioned by everybody already.

**Marcel Santilli:** And so, so it's like that they're, they're, they're going to be there whether you're cited or not.

**Marcel Santilli:** So then citation is about like controlling the alignment and the sentiment more than anything, right.

**Marcel Santilli:** Rather than, you know, improving the recall only.

**Marcel Santilli:** Right.

**Marcel Santilli:** And so then it's just like there is like the context of the brand, right?

**Marcel Santilli:** You need to understand company products, positioning, pricing, Personas and buyers, competitors, differentiators.

**Marcel Santilli:** Like all those things are important, which by the way is all the context we do anyways to create public pages.

**Marcel Santilli:** And it's the context we need to have in their space and the taxonomy around their business.

**Marcel Santilli:** Right.

**Marcel Santilli:** And then the market context is like the, Think of it as, it's like, it's the, like it's the context of the market, the category, the buying categories, the market categories, the players, the category dynamics and adjacent categories, how it's like all correlated.

**Marcel Santilli:** And this should also be content that we do.

**Marcel Santilli:** Right?

**Marcel Santilli:** And then you have the buyer context.

**Marcel Santilli:** So now that's like us defining these buyers, right?

**Marcel Santilli:** How the buyers in these categories think they search, they decide, right.

**Marcel Santilli:** Like, we haven't spent a lot of time here.

**Marcel Santilli:** We mostly do this within the lens of that company, right?

**Marcel Santilli:** Like, and so then you have all that.

**Marcel Santilli:** So you have brand context, you know, and brand context on all the competitors.

**Marcel Santilli:** Then you have market context, buyer context, and then like the, the, the prompts, you know, so then the, the instruments are the probes that we use to survey AI engines, right?

**Marcel Santilli:** So, so the mental model here is like the probing and model, you know, it's not really a model, it's a service, right.

**Marcel Santilli:** Like you're probing a service at the end of the day in a lot of ways.

**Marcel Santilli:** And they're not random.

**Marcel Santilli:** They are a research instrument.

**Jason Gong:** Right?

**Marcel Santilli:** And it's built from the context you have.

**Marcel Santilli:** And, and so what you're trying to do, the analogy here is like brand research.

**Marcel Santilli:** You're surveying the population, survey questions, sample size, you know, survey wave, survey panel, control group, test group, right?

**Marcel Santilli:** So it's like almost a perfect analogy to like brand survey research, you know, and, and I think that's the unlock of like, if we position ourselves as like coming up with these new methodology, new mental model, new approach to it and how we're thinking about it, we become the default and it makes so much more sense when you do that because it's based on like actual brand research that has been done for, for years.

**Marcel Santilli:** And you're creating essentially like a digital twin of your buyer of your buyers.

**Marcel Santilli:** And you're doing, creating context on your company and your space and all your competitors.

**Marcel Santilli:** And then you're using AI as like, you know, almost kind of like this digital twin that you're like surveying in order to know how these services are going to like their opinions of your brand, right?

**Marcel Santilli:** Or recall.

**Marcel Santilli:** So then, so then you have like prompts, patterns, right?

**Marcel Santilli:** So then you have like the patterns of the prompts like best for whatever.

**Marcel Santilli:** You have prompt instances, which is like the actual instance of that prompt.

**Marcel Santilli:** And then you have clusters of prompts.

**Marcel Santilli:** And then you also have prompt sequences which is like the multi turn stuff, right, that you need to do.

**Marcel Santilli:** And then there's like these axis if you will for classifying prompts.

**Marcel Santilli:** And so the classification of the prompts will determine how you use that data, right?

**Marcel Santilli:** And so you have market like where you have intent to learn, explore, compare, validate or act.

**Marcel Santilli:** You have buyer stage, which we're already doing.

**Marcel Santilli:** You have question type, right?

**Marcel Santilli:** Like problem definition, category, evaluation, decision types, there's a bunch of other things.

**Marcel Santilli:** And then you have like modifiers.

**Marcel Santilli:** So then the modifiers are about like exploring that within a certain context, right?

**Marcel Santilli:** Like by, by industry, company size, buyer role.

**Marcel Santilli:** So it's like what is the best corporate card for SMB for startups, for a VP of marketing at a startup or whatever, right?

**Marcel Santilli:** Like and this has to be driven by your context.

**Marcel Santilli:** So these are like more, more advanced, right?

**Marcel Santilli:** And then it's like the purpose, like why is this right?

**Marcel Santilli:** So if you do ramp pros and cons or is ramp worth it or is ramp worth it for startups, that is sentiment.

**Marcel Santilli:** If you do what is ramp or what is ramp spicing?

**Marcel Santilli:** It's about alignment.

**Marcel Santilli:** If you do ramp versus Brax or alternative to Brax, like it's about like competitive position.

**Marcel Santilli:** And then recall is about best expense management tools, right?

**Marcel Santilli:** And then for the prompt structure types you have like simple Persona injected generated knowledge and multi turn and different layers of complexity, you know, and, and so then it's like this should form like your entire like prompt strategy.

**Marcel Santilli:** And if you do right then there's like the recall stuff.

**Marcel Santilli:** You're measuring more often, right?

**Marcel Santilli:** And, and then everything else is like less often but needed in order to take like surveys, like one off waves of surveys, like weekly surveys of your brand, like weekly surveys of like alignment, you know, to Your context and things like that.

**Marcel Santilli:** And then in all of this you have Share library versus custom.

**Marcel Santilli:** And we're constantly trying to upgrade the custom ones into the share library or add it to the share library programmatically.

**Marcel Santilli:** And then I need to tweak this a little bit more, but there's four core metrics.

**Marcel Santilli:** It's like recall.

**Marcel Santilli:** Does AI remember us?

**Marcel Santilli:** How does AI describe us?

**Marcel Santilli:** Does AI match our truth and is it getting better?

**Marcel Santilli:** And then we got to come up with unique names for all of these things and composite scores, which is like AI Brand health score, AI Recommendation score and competitive Positioning Score map.

**Marcel Santilli:** And then this is the full thing.

**Marcel Santilli:** And so this is the methodology that I came up with.

**Marcel Santilli:** Um, that I think it's like it unlocked in my head when I, when I clicked, I was like, fuck, this is it.

**Marcel Santilli:** Like, this is good.

**Marcel Santilli:** Like, I think.

**Jason Gong:** But no, I mean, I like the structure.

**Jason Gong:** Like, everything right now is just like a pool of prompts.

**Jason Gong:** Like, I don't know if I have too many of one or too many of another.

**Jason Gong:** It's just like all sitting in the soup.

**Jason Gong:** And I think this is like, if.

**Marcel Santilli:** I give this away tomorrow, the product is not there.

**Marcel Santilli:** And so it's kind of like we need to start like building this structure in parallel to building the product around it.

**Marcel Santilli:** But the probing structure is already there.

**Marcel Santilli:** So then the taxonomy is going to be needed for all of this.

**Marcel Santilli:** The auto tagging is going to be needed and the prompt generation, generating workflow and flow is going to be needed no matter what.

**Marcel Santilli:** Right?

**Marcel Santilli:** And so those are there and then the rest just becomes like, things you do for, like enabling these more complex modifiers.

**Marcel Santilli:** And, and all these modifiers have to be based on the context of your brand, right?

**Marcel Santilli:** And what market you assigned this brand to and you know, and the competitors.

**Marcel Santilli:** And then it's like, how much information do you pull from the competitors?

**Jason Gong:** Right?

**Marcel Santilli:** Like, so, I mean, all that info.

**Jason Gong:** Is going to be like, so critical to like now when you write a piece of content.

**Jason Gong:** I mean, like you, you've shown more artifacts than I think we have in Atlas right now.

**Jason Gong:** You know, if you have that info, you could write a much better whatever content that you want to write.

**Marcel Santilli:** So then I think we can start to create the content for this.

**Marcel Santilli:** We can formulate it.

**Marcel Santilli:** I need to do a little bit more of the 0 to 1 to kind of structure how the metrics will be calculated and what the experience needs to look like on the dashboard.

**Marcel Santilli:** And so then it's just like taxonomy, auto tag, prompt generation, and then it's like onboarding V2 to do more deep research.

**Marcel Santilli:** And I connect all these things and have more of a wow experience in parallel to like enriching, more aggressively enriching the public pages and the catalog of brands and categories and continue to make those better.

**Marcel Santilli:** Because like only 172 categories.

**Marcel Santilli:** We need more categories.

**Marcel Santilli:** We need like, you know, more robust.

**Marcel Santilli:** We need better explanations of those categories, better contacts, which are all public pages anyways to pull because you need context, like market category context more, you know, and, and you also need more content around like how the dynamics of the category, the alternatives.

**Marcel Santilli:** All, all of the public content is context actually, you know, like.

**Jason Gong:** So it's great.

**Jason Gong:** Yeah.

**Marcel Santilli:** And, and then, then it's like rethinking the entire dashboard experience to be based on this, like reframing the whole thing based on this and then starting to like build the audits and reports, you know, so, so those are like the, the graders, the audits, the, you know, like the one off insights, the what to do about it a little bit.

**Marcel Santilli:** And they're, they're like one off snapshots of like ingesting all this information, which now will be way more.

**Marcel Santilli:** Because now you have context to the brands and things like that.

**Marcel Santilli:** So if like there's like, hey, this competitor green ground on you, then you can go pull the context of that competitor and then understand the dynamic of the market and, and then look at the data and then the report can give you like, oh, okay, I get it.

**Marcel Santilli:** You know, like this is what we're doing about it, you know, and then the last piece there is the analytics, like start to pull like GSC start to pull like, you know, basic page audits, you know, and, and then that's where we kind of draw the line of like create a brief or create an assignment, you know, then it can bridge to a legion to os, you know, but like we, we essentially do the whole.

**Marcel Santilli:** This is a brand research tool, you know, in database and in market context insight, where, you know, and so it's like a, A brand survey.

**Jason Gong:** Yeah, I mean, I guess, like tactically, can you share any of this?

**Jason Gong:** Because we do have calls next week and we got to like pull the prompts and see if the workspaces.

**Jason Gong:** I know you were working on it like last week, but I imagine yes.

**Marcel Santilli:** So this file should be.

**Marcel Santilli:** It is in the handbook now.

**Marcel Santilli:** Okay.

**Marcel Santilli:** Yeah, it's.

**Marcel Santilli:** It's in the handbook repo.

**Marcel Santilli:** So let me show you.

**Marcel Santilli:** Send it here.

**Marcel Santilli:** You have access to our GitHub, right?

**Jason Gong:** I do have access to our GitHub Let me see if I have access to that repo.

**Jason Gong:** You should.

**Marcel Santilli:** It's open to the whole company's call handbook.

**Jason Gong:** Does not look like I've accessed.

**Jason Gong:** Let's see.

**Jason Gong:** Oh no, I got it.

**Jason Gong:** Yep, got it.

**Jason Gong:** You got it.

**Jason Gong:** Okay, cool.

**Marcel Santilli:** Okay, so if you go to Context Knowledge and the aeo, I'll send you a link.

**Marcel Santilli:** There you go.

**Jason Gong:** All right, awesome.

**Marcel Santilli:** So if you can try to help me take this and then build like, like build this out a bit more, you know.

**Jason Gong:** Yeah, I'm looking to it.

**Jason Gong:** I mean, I guess the most immediate thing I'm going to build is just like some sort of skill that kind of takes this structure and just like maps out prompts just because we need to do that immediately once somebody books a call and then.

**Marcel Santilli:** But explaining it is going to be important, you know, but just like as well.

**Marcel Santilli:** But don't go to.

**Marcel Santilli:** Just don't give away too much, you know, yet.

**Jason Gong:** Yeah.

**Marcel Santilli:** Assume people you're talking to are going to turn around, send their recording to and don't let any recorders in other than ours.

**Jason Gong:** Okay.

**Marcel Santilli:** Like this is truly like if this clicks and profound gets a hold of it, they can match pretty quickly.

**Jason Gong:** Right.

**Marcel Santilli:** Like the, the thought process, like we have to be the first ones to like be like tada.

**Marcel Santilli:** This is how to think about it folks.

**Marcel Santilli:** Like, and there's like all these startups that raised a ton of money.

**Marcel Santilli:** They're doing like essentially like AI user research tools, you know, like Outset is a good one.

**Marcel Santilli:** Like synthetic users like Maze and then they're, they're all like it's a research platform, right?

**Marcel Santilli:** Qualitative research, quantitative speed, you know.

**Marcel Santilli:** And so they're creating essentially like digital twins of like their audience and then essentially surveying their digital twins of like, You know, it's like essentially creating like synthetic consumers to then go and survey them about what they think about something, you know, instead of actually like spending a fuck ton of money like actually doing surveys.

**Marcel Santilli:** It's mostly a consumer stuff, you know, AI driven synthesis case study, you know, Testis is most innovative product concepts.

**Marcel Santilli:** So then they're testing concepts and whatever, you know, like.

**Marcel Santilli:** So there's a lot of like parallels to kind of like this, you know, like user research, except the user is AI engines.

**Jason Gong:** Yeah.

**Marcel Santilli:** But you can see it's like if you look at this, it's like openness or whatever agreeable.

**Marcel Santilli:** There's almost later on a qualitative part of this that we're going to do which is just qualitatively showing this mind map of in an index of qualities.

**Marcel Santilli:** And then it's just like a map of the space of niche players versus who are considered the leaders.

**Marcel Santilli:** And, and you know the good news, a lot of the stuff is just snapshots.

**Marcel Santilli:** They're not like, you don't need to probe every single day and like show a trend towards it.

**Marcel Santilli:** You know, it's more like snapshots in time and if it's improving or not.

**Jason Gong:** You know, or you like, like is this gonna feel like a, like, hey, everyone is kind of getting around this is what AI visibility should be.

**Jason Gong:** Or are we even gonna call it something else?

**Jason Gong:** Because these guys aren't talking AI visibility.

**Marcel Santilli:** It's more like this is not what we're building.

**Marcel Santilli:** This is just like a parallel of like a way to think about it, right?

**Marcel Santilli:** Like, which is like you're survey, like you have three buyers now you have your human buyer, A agents and training bots.

**Marcel Santilli:** Right.

**Marcel Santilli:** And training bots is the most lagging of all of those.

**Marcel Santilli:** Like it might be six months before the data they collect actually is in a model.

**Marcel Santilli:** And so it's the most lagging one, but you're the most prominent permanent one, right?

**Marcel Santilli:** That's going to be important.

**Marcel Santilli:** Long term agents is like the, the real time factor that are influencing buyers, but buyers also go direct, right?

**Marcel Santilli:** And, and so like, so what you're trying to do is survey these services to understand the, the three parameters of like recall, sentiment and alignment.

**Marcel Santilli:** Right?

**Marcel Santilli:** And so you're serving a person.

**Marcel Santilli:** You're serving and that person is like a service.

**Marcel Santilli:** You're serving a service essential.

**Jason Gong:** Yeah, yeah.

**Marcel Santilli:** And so it's changing the market's mindset of infinite probing on prompts and whatever.

**Marcel Santilli:** Just prompt visibility.

**Marcel Santilli:** What is it like, why do I care about it?

**Marcel Santilli:** And it's more like this is a survey research.

**Marcel Santilli:** Like it's an AI survey.

**Marcel Santilli:** You're surveying AI and you're surveying AI in order to understand these three things and then understand the lift.

**Marcel Santilli:** And then in parallel we are building like these predictive models on understanding the impact that a citation and the kind of citation can and will have on how likely it is that the work you do will get cited and how a citation influences an answer and influences it in the right way you care about.

**Marcel Santilli:** AKA for instance, does word count matter?

**Marcel Santilli:** Well, the CMO of HubSpot said pretty confidently on a podcast that you should write really long fucking posts and chunk the fuck out of them.

**Marcel Santilli:** Like 6,7000 word posts and chunk the crap out of them.

**Marcel Santilli:** Is that true or not?

**Marcel Santilli:** I don't know, but I don't think there's conclusive evidence of that, but it's like, well, we should figure out.

**Marcel Santilli:** So then it's just like, hey, you got to compare answers.

**Marcel Santilli:** And then for each model is completely different.

**Marcel Santilli:** Like Perplexity and chatgpt versus Claude versus Gemini are very, very, very different.

**Marcel Santilli:** So then now it's like you're trying to like reverse engineer.

**Marcel Santilli:** But the good news is we have the most badass data science ML person ever that just accepted today.

**Marcel Santilli:** And I worked with him at Deepgram and since then he's like, incredible.

**Marcel Santilli:** So we, we also have somebody that's going to be able to help and hire a team as well.

**Marcel Santilli:** So.

**Jason Gong:** Excited.

**Jason Gong:** Is he, is he here or is.

**Marcel Santilli:** He at a. Yeah, he's, he's just moving to Fremont from San.

**Marcel Santilli:** Actually, Sorry.

**Marcel Santilli:** He's moving from Fremont to Castro Valley, but he's local.

**Jason Gong:** All right, I'm excited to meet him.

**Marcel Santilli:** Yeah, never mind.

**Marcel Santilli:** He hasn't signed, but he gave a verbal in person today and a handshake, so I will take that.

**Marcel Santilli:** And I, I, I worked with him at, at Deepram.

**Marcel Santilli:** He's really, really freaking good.

**Marcel Santilli:** His name is Jacob Cutter.

**Marcel Santilli:** How send the t. Anyways, he does have a PhD.

**Marcel Santilli:** It's a pretty smart guy, but it's really awesome to work with.

**Marcel Santilli:** All right, man, I'm going to run.

**Jason Gong:** Okay, talk to you later.

**Marcel Santilli:** Let's figure out time to then get the, like, the whole map and plenty of.

**Jason Gong:** Bye.

**Marcel Santilli:** See you, man.

**Jason Gong:** Good.

**Jason Gong:** I'll grab time.

**Jason Gong:** All right.

**Marcel Santilli:** See it.
