# Marcel Santilli

<metadata>
date: 2025-12-10
time: 23:02 UTC
duration: 41 minutes
organizer: stevie@growthx.ai
participants: Stevie Kim (GrowthX), Marcel Santilli (GrowthX)
fathom_recording_id: 107892639
fathom_url: https://fathom.video/calls/501042513
share_url: https://fathom.video/share/f3VjjpbYfysq8ssYxMyJw_bYk7e1xJjt
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Marcel and Stevie aligned on a new operating model for CheckThat over the next two months, moving from unstructured work to a "work lanes" framework. The team will focus on two launch-blocking initiatives: building a scalable CMS for organic growth and creating a complete sign-up and payment flow. Stevie will shift from coding small fixes to high-leverage product management—organizing work, shaping features, and improving the Shared Library—while Marcel focuses on prototyping public-facing pages and defining the CMS MVP.

---

## Context

CheckThat is GrowthX's B2B SaaS product for AI visibility and SEO auditing. The product is in active development with Marcel (Founder) and Stevie (Product/Engineering lead) driving the roadmap. The team is preparing for launch and needs to coordinate between multiple parallel workstreams while avoiding "busy but not effective" work. The lack of structure and written communication following Jose's departure has created misalignment around priorities, with the Linear backlog containing too many items at equal priority.

This call was scheduled to define an operating cadence that would bring focus and organization to the work for the next 8 weeks, ensuring the team moves toward launch milestones efficiently and with clear context on what each person is building and why.

---

## Relevance

**To CheckThat Product:**
- CheckThat is adopting a "work lanes" model with four focus areas: Organic Growth, Customer Validation, Data & Shared Library, and Experience & Infrastructure. This structure will drive all engineering and product decisions.
- Two launch-blocking initiatives: Organic Growth CMS (to enable scalable content creation with SEO controls) and Sign-up/Payment flow (to establish the monetization loop).
- Design partnership with external customers (e.g., Augment Code, Scrunch) is progressing; team is getting ahead of feature expectations and visibility metric discrepancies before launch.

**To GrowthX Operations:**
- Stevie's role is shifting from code contributor to product management, focusing on work organization, feature shaping, and data quality. This signals a maturity shift in how the product team structures work.
- Team is implementing weekly written updates (a practice from Jose) to improve async communication and reduce misalignment. First update due by end of Thursday.
- Shared Library quality is critical; team is auditing brand categorization and prompt quality to ensure data accuracy for customers like Scrunch.

---

## Overview

- **New Cadence:** Adopt a "work lanes" model to replace the current unstructured process. This provides focus and context, preventing "busy but not effective" work.
- **Top Priorities:** Focus on two launch-blocking initiatives: 1) building a scalable CMS for organic growth, and 2) creating a complete sign-up and payment flow.
- **Role Shift:** Stevie will shift from coding small fixes to high-leverage product management: organizing work, shaping features, and improving the Shared Library.
- **Immediate Action:** Marcel and Stevie will draft a team-wide update by EOD Thursday to introduce the new structure and align everyone on priorities.

---

## Key Topics

### Problem: Unstructured Work & Misaligned Priorities

  - The current Linear "milestones" are too broad to provide clear direction, leading to a feeling that "if everything's a priority, what's the priority?"
  - This unstructured process risks "busy but not effective" work, where tickets are closed without advancing key milestones.
  - The lack of written updates (a practice from Jose) has reduced team-wide context and alignment.

### Solution: A "Work Lanes" Operating Cadence

  - The team will adopt a "work lanes" model to provide focus and context for all work.
  - Each lane is a distinct workstream with clear validation goals.
  - **Proposed Lanes:**
      - Organic Growth (Goal: Clicks)
      - Customer Validation (Goal: Daily use)
      - Data & Shared Library (Goal: Quality & expansion)
      - Experience & Infrastructure

### Top Priorities: Unblocking Launch

  - Two initiatives are critical for launch and require immediate focus:
  - **1. Organic Growth CMS**
      - **Why:** To build a defensible lead in organic traffic before better-funded competitors can copy the strategy.
      - **Need:** A CMS to enable editors to scale content creation (e.g., brand pages) by managing SEO elements (H1s, meta titles) and connecting workflows.
      - **Goal:** Marcel to shape the MVP by EOD Friday for engineering prioritization next week.
  - **2. Sign-up & Payment Flow**
      - **Why:** To build the core monetization loop, which currently does not exist.
      - **Need:** A complete end-to-end experience from sign-up → payment → onboarding.
      - **Goal:** Marcel to focus on pricing/packaging; Stevie to research payment providers (e.g., Clerk vs. Stripe) to enable a quick, informed decision.

### Stevie's Role: High-Leverage PM

  - Stevie will shift from coding small fixes to high-leverage product management.
  - **Focus Areas:**
      - **Organizing Work:** Structuring the new "work lanes" and driving team-wide asynchronous updates.
      - **Feature Shaping:** Defining MVP requirements for key initiatives like the sign-up flow.
      - **Shared Library Improvement:**
          - **Why:** The library is critical for data quality and needs to reflect reality (e.g., Notion is a note-taker).
          - **Actions:** Correcting subcategory assignments and adding high-quality prompts.

---

## Action Items

**Stevie Kim**
- Draft 101 doc on lanes/priorities/cadence; share w/ Marcel
- Research monetization (Clerk vs Stripe); then prototype sign-up/onboarding/billing
- Improve shared library: add subcategories, reassign brands, add missing prompts
- Post EOD update to team re: lanes/priorities/cadence

**Marcel Santilli**
- Prototype public-area pages; then shape MVP CMS for public pages

---

## Transcript

**Stevie Kim:** So, lots of things that I'm kind of doing in parallel.

**Stevie Kim:** So, trying to get the design partnership thought through a little bit.

**Stevie Kim:** But, um, I to, I talked to Liz, and then I want to talk to the other directors, because I want to kind of understand, like, for those that they're using, if they're, like, showing customers, certain customers, like, Augment Code, Scrunch, like, and they already have these ideas of what is working or not working for them, what, you know, is really important for them to see.

**Stevie Kim:** Um, documenting that so we can get ahead of it before, like, because I don't want them to, like, get access and then be, like...

**Stevie Kim:** Oh, well, this isn't, this visibility metric isn't here on the, like, overview, and that's missing, and that, you know, that's really important to us.

**Stevie Kim:** So basically, just trying to get ahead as much as we can with that.

**Marcel Santilli:** So, yeah, I'm kind of.

**Marcel Santilli:** And also making sure, like, if our visibility metrics are, like, orders to magnitude different than what Scrunch is reporting on the same prompt, right?

**Stevie Kim:** Yes.

**Stevie Kim:** Yeah, Liz, and I talked about that, too, which is a little bit, I mean, it's kind of.

**Stevie Kim:** It works in our favor that you can only select, like, one LLM provider at a time on Scrunch, because our filtering is a little different.

**Stevie Kim:** And so, you know, there's not a way to do apples to apples comparison on that data right now.

**Stevie Kim:** And I think that's good for the meantime.

**Stevie Kim:** So.

**Stevie Kim:** So, you know, iron out all of the potential wrinkles.

**Stevie Kim:** So, yeah, there's that.

**Stevie Kim:** And then just also making sure we have the functionality that they would expect.

**Marcel Santilli:** Okay.

**Marcel Santilli:** That sounds good.

**Marcel Santilli:** Yeah, think the thing I want to figure out with you is what's the right operating cadence for the next between now and end of January to, like, make sure we're driving, like, momentum towards getting to the milestones, improving out the things we need to prove as quickly as humanly possible, right?

**Stevie Kim:** Yeah, so another thing that is on my plate and it's mostly, like, as I see things and then in my head a little bit, putting, you know, that design partnership milestone.

**Stevie Kim:** I'm going to put on tickets that are blockers.

**Stevie Kim:** I'm going to just make sure that they're a part of that milestone and really make sure we're focusing on those.

**Stevie Kim:** That's part of it.

**Stevie Kim:** And then I think the one thing is a little bit hard for me is that we don't work in any kind of sprints or cycles or anything.

**Stevie Kim:** And so that's a little bit tough.

**Stevie Kim:** So there's not like this kind of, yeah, organized chunk of work that is happening in a, you know, given time frame.

**Stevie Kim:** But it seems like it's been working for y'all.

**Stevie Kim:** So I'm not going to change that.

**Stevie Kim:** I just need to make sure in my head that I'm, that I, you know, I've got the right things.

**Marcel Santilli:** Yeah, and that's what I'm saying.

**Marcel Santilli:** mean, we're, we're working towards these milestones, right?

**Stevie Kim:** head.

**Stevie Kim:** It's

**Marcel Santilli:** Validation, and we can almost look at those as, it's like, how do we organize the lanes and the work right now?

**Marcel Santilli:** And it can shift, you know, so maybe one work stream or lane is, like, organic growth, right?

**Marcel Santilli:** And there's very specific things we're trying to validate, which is, like, building towards, like, clicks, essentially, like, organic clicks.

**Marcel Santilli:** And so, for instance, like, that lane, every day, I am, like, refreshing this, right?

**Marcel Santilli:** So I'm looking at impressions, so I'm like, cool, all right, that's a good trend, right?

**Marcel Santilli:** I mean, 100 impressions is nothing, but it's like, that doesn't matter where we start, right?

**Marcel Santilli:** What matters is that every day is going up a little bit, right?

**Marcel Santilli:** I'm looking at the number of pages here, 37 pages, getting impressions, lovely, right?

**Marcel Santilli:** Once that validates, now I'm like, okay, cool.

**Marcel Santilli:** Now there's, like, clicks, okay, great.

**Marcel Santilli:** It clicks.

**Marcel Santilli:** It's not quite there.

**Marcel Santilli:** All right.

**Marcel Santilli:** We got to keep driving, Keep paying attention to it and then keep working towards the organic strategy I pulled together and unlocking things on the admin panel, right?

**Marcel Santilli:** Like, so maybe another work stream can be, you know, get this to be you, like, validated with every single customer we have and have them be excited to use this every day and turn from other tools and solutions, right?

**Marcel Santilli:** So that's the, like, essentially get our workspaces to be, you know, whatever we want to call, like, these work streams.

**Marcel Santilli:** And then there might be another one that can be, like, a data one, right?

**Marcel Santilli:** Continue to improve the data and the categories and the shared library, essentially.

**Marcel Santilli:** And another one can be the experience and another one, the infrastructure or something.

**Marcel Santilli:** Like, some way to, I don't know, I'm just brainstorming here, but, like, just to organize the lanes.

**Marcel Santilli:** So when people are doing something.

**Marcel Santilli:** It's like, why are you doing this thing right now for this?

**Marcel Santilli:** And as long as it fits in one of these priorities lanes, you know, then it'll be a little bit easier for us to, like, it doesn't need to be overly structured.

**Marcel Santilli:** I just don't want tickets to start flying around too much.

**Marcel Santilli:** And then next thing you know, people are just, like, you know, closing 20 tickets a day.

**Marcel Santilli:** And it's like, wait, nothing is fundamentally changing, you know.

**Stevie Kim:** For sure, for sure.

**Stevie Kim:** So I was just going based off of what you guys already have, like, oh, is it good at changing it?

**Stevie Kim:** You already have those milestones.

**Stevie Kim:** What isn't, and there's already tickets in them and new tickets I assigned to those milestones.

**Stevie Kim:** The only thing that I'm not clear on is, like, I guess when I think of milestones, I think of, you know, like the roadmap, right?

**Stevie Kim:** And those are different milestones in the roadmap, not everything running, these milestones running in parallel.

**Stevie Kim:** So the way you described it.

**Stevie Kim:** If, like, I'm thinking about it in, like, lanes, I think that makes way more sense.

**Stevie Kim:** But is there anything in those milestones that are currently in there that we shouldn't be focused on?

**Stevie Kim:** Because they're just, they're not really prioritized in a linear way, so.

**Marcel Santilli:** Yeah, like, I would think of it as, like, our job, your job, and my job is to get us to, like, validate these things as quickly as possible to then unblock us from going to market, right?

**Marcel Santilli:** Like, we're in a sprint as quickly as possible to be, like, launch ready, let's call it, right?

**Marcel Santilli:** And I think, like, maybe we just need to spend, like, a bit more time just planning those big bucket areas more.

**Marcel Santilli:** Like, I haven't had time this week.

**Marcel Santilli:** I was going to do the pricing, monetization, and overall, like, packaging strategy, right?

**Marcel Santilli:** But that's a big, big one, right?

**Marcel Santilli:** And then there's the feature priority with Scrunch, essentially, a.k.a.

**Marcel Santilli:** like our customers can use it and they're good.

**Marcel Santilli:** And our teams are using and they're happy with it.

**Marcel Santilli:** And once we give some of our customer users access, they're happy.

**Marcel Santilli:** There's nothing wrong with it.

**Marcel Santilli:** Cool.

**Marcel Santilli:** That's validated.

**Marcel Santilli:** And then the other big one is like the index, if you will, or the public area is growing and we have the right surface area to continue to grow.

**Marcel Santilli:** And we're seeing up to the right momentum, right?

**Marcel Santilli:** And the main reason for that is like if our organic strategy is not really solid, you're going to have and we haven't already like gotten far out into executing against it, then it's easy for anyone to copy.

**Marcel Santilli:** And our competitors have, you know, more zeros in the bank than we do.

**Marcel Santilli:** So then the goal is like we're too far out on that for them to like pivot super fast and it'll be a lot harder.

**Stevie Kim:** For them to copy, you know what mean?

**Stevie Kim:** Yeah, so it seems like, yeah, so it seems like those would be milestones.

**Stevie Kim:** We time box those till the end of January.

**Stevie Kim:** And then, yeah, we can have tickets associated with those and have engineering focus on those.

**Stevie Kim:** Because they are kind of all, it is all, as I said, the milestones are really more of like what I would think of as just like categories.

**Stevie Kim:** Like, you know, if it was in client ops, I would be using like labels instead of, you know, the way it is.

**Stevie Kim:** So, yeah, I'll think of the best way to organize that so it's not, so it's clear for us.

**Marcel Santilli:** lane would be the mentality would be a little bit different, right?

**Marcel Santilli:** Like, for instance, like in the organic growth one, right now, there's like multiple things that are blocked by me or by others, right?

**Marcel Santilli:** Like one of them is actually like finishing the design of some of the pages.

**Marcel Santilli:** that's let's And here's,

**Marcel Santilli:** The changes we're making.

**Marcel Santilli:** The other one is like the admin experience for being able to edit and create new pages, regardless of what that page is based on.

**Marcel Santilli:** Like, for example, a brand page is a page, and it's based on a brand, but it's a page.

**Marcel Santilli:** And right now, the H1 and title of those pages just say, you know, Salesforce, for example.

**Marcel Santilli:** And like, we need ability to change that or change it to meta title or description and things like that, right?

**Marcel Santilli:** So there's like, and then you need a CMS experience to do that.

**Marcel Santilli:** And then you need to connect workflows to those in order to scale the crap out of those, right?

**Marcel Santilli:** Like, and improve those.

**Marcel Santilli:** There's like a lot of those things that are going to be very like, they're not like a quick ticket, fix it, call it a day, next one.

**Marcel Santilli:** know, they're very much like someone thinking day in and day out as an engineer, plus design, plus product, plus like growth mindset towards that one.

**Marcel Santilli:** And in order to unlock us putting like two editors on this and cranking, right?

**Stevie Kim:** Like.

**Marcel Santilli:** So then, like, I think for each one of those lanes, maybe you and I spend a little bit more time and then enough to shape it so that then you can go operationalize it, essentially, right?

**Stevie Kim:** Like, yeah, yeah, I start, so what I've been doing is going through and find, like, in the admin, finding areas that if, you know, a GrowthX user were to go in and do an oopsies, like, okay, is there, you know, is it irreversible?

**Stevie Kim:** And so there's a lot of those things.

**Stevie Kim:** A lot of them just, there's a lot of UX things that my local instance somehow got messed up.

**Stevie Kim:** And so I couldn't, yeah, like, I couldn't test my local changes.

**Stevie Kim:** So there's a lot of stuff that I can just fix, right?

**Stevie Kim:** A lot of little things that aren't going to, that aren't going to be quality of life, but it will help.

**Stevie Kim:** It'll put some guardrails up.

**Stevie Kim:** Yeah.

**Stevie Kim:** So people.

**Stevie Kim:** People don't screw up, basically, because I already did.

**Marcel Santilli:** I think right now, though, even if you can, I think what you can do that the engineers can't do, the rest of the engineers can't do right now, is help organize the work and help people kind of think through the lanes, you know what mean?

**Marcel Santilli:** So, and shape the stuff that's not even remotely shaped, that is way, and connect the business dots as well, that is way higher leverage, I think, right now.

**Marcel Santilli:** Because we're not yet in the phase where, I think we have just really good engineers that can move really fast, too, right?

**Marcel Santilli:** Like, and so even if you can, you feel like you can do the same, have the same amount of productivity as any other engineer, the engineers can't do what you can do as well on the product management side, you know, like shaping the lanes.

**Marcel Santilli:** Obviously, like getting there in order for you to, like, up and understand everything, you know, but.

**Marcel Santilli:** But in this phase, I think we have way more needs in, like, a PM rather than one more engineer, if you will.

**Stevie Kim:** That's fair, that's fair.

**Stevie Kim:** Yeah, it's hard because it's like when you see something, you're like, oh, I can just fix this, you know.

**Stevie Kim:** But yeah, no, I totally get what you're saying because it is context switching.

**Marcel Santilli:** Yeah, it is.

**Marcel Santilli:** It's very context switching.

**Marcel Santilli:** That's fair.

**Marcel Santilli:** Yeah, like, so, I mean, like, right now, the, there, maybe, okay, let's start, let's maybe start a doc.

**Stevie Kim:** Can we start a 101 doc or something?

**Stevie Kim:** Yeah, for sure.

**Stevie Kim:** And I did have some questions on some stuff that didn't feel intuitive to me, but I think I understand the reason, but stuff like when you go into...

**Stevie Kim:** Like, say, it's Augment Code.

**Stevie Kim:** You go into their overview.

**Stevie Kim:** I guess I would have expected to see the brand page there.

**Stevie Kim:** Like, I get why it's in the other, you know, the brand section.

**Stevie Kim:** That makes sense.

**Marcel Santilli:** Say that again.

**Stevie Kim:** So when you go to the workspace, say, your Augment Code, you go to the workspace, and there's the overview, and there's just that dashboard.

**Stevie Kim:** But there's a lot of also kind of interesting information in their brand page.

**Stevie Kim:** Like, that's where the AI answers are.

**Stevie Kim:** That's, you know, where they can kind of dig in.

**Stevie Kim:** And so, yeah, I was thinking, like, we don't have to, I know we wouldn't want to replicate that page under the workspace overview, but even just, like, giving them some awareness and linking to that brand awareness page, because it's not intuitive.

**Stevie Kim:** Like, if you go, if you sign in to your workspace, and you go into your little, you know, overview, and then there's, you know, a couple of other.

**Stevie Kim:** there are navigational items, it's not intuitive that you would find your brand information anywhere else.

**Marcel Santilli:** Does that make sense?

**Marcel Santilli:** Yeah, like, I think those things are, the context is important.

**Marcel Santilli:** Like, when you're logged in, I think a lot of the other experiences, like, you, like, it's either brand kit or context or something else, right?

**Marcel Santilli:** And so, like, that part is not, like, you know, it's, like, right there.

**Marcel Santilli:** And later on, I think we can optimize to see if people are truly not finding or whatever.

**Marcel Santilli:** But then later on, we are planning and want to do more insights where it's way less of, like, a data dashboard and it's way more about insights, right?

**Marcel Santilli:** Like, hey, your brand fell because of this, this, and this, and a new competitor entered the space that is being perceived better because of this, this, and this.

**Marcel Santilli:** Hey, there's a negative angle in some of these answers about this.

**Marcel Santilli:** It's being influenced by this one page.

**Marcel Santilli:** You should create a piece of content that counters this or whatever.

**Marcel Santilli:** You know what mean?

**Marcel Santilli:** That's part of what will come out of the study and other things and be a value add.

**Marcel Santilli:** It's just like right now that we got to get the end-to-end working.

**Marcel Santilli:** got to get compensation, conversions, the sign-up experience working, the public site indexing and getting traffic.

**Marcel Santilli:** And a great example of this is like had we fixed some of the things we had that were blocking indexation, we would have been able to, like, four weeks ago, we would have already been getting a ton of traffic right now probably.

**Marcel Santilli:** Right?

**Marcel Santilli:** And so no one was looking at it.

**Marcel Santilli:** No one was paying attention.

**Marcel Santilli:** No, we fixed robots, blah, blah, blah.

**Marcel Santilli:** It's fine.

**Marcel Santilli:** And then it's like there was another blocking thing and then another one and then another one and then another.

**Marcel Santilli:** Then no one did this and, you know, things like that.

**Marcel Santilli:** And so, like, that's what we got to make sure we're getting through is, like, the end-to-end experience, right?

**Marcel Santilli:** Like, hey, someone finds the site organically, they click on an action, they then convert, create a dashboard, they get experience, they don't get stuck, and then they upgrade eventually, right?

**Marcel Santilli:** Like, that's the end-to-end, if you will.

**Marcel Santilli:** And it's okay that, like, the monetization piece maybe is working, but we're not fully validated because we've already validated with our customers that it works and things like that, you know?

**Marcel Santilli:** But, like, there's big pieces in that whole end-to-end that are not yet, like, fully validated, you know?

**Marcel Santilli:** But it's getting closer.

**Marcel Santilli:** It's just we have a lot of work in progress right now that we just need to, like, bring clarity.

**Marcel Santilli:** So, for me, what's keeping me up at night right now is, like, two things.

**Marcel Santilli:** One is that there's a massive surface area in order for us to really get the organic strategy going.

**Marcel Santilli:** And I need, we need to unlock a CMS that I can get two or three of our editors just cranking in there and generating the pages, right?

**Marcel Santilli:** Like that to me, I need to shape it.

**Marcel Santilli:** And that one's like a bit, a decent undertaking.

**Marcel Santilli:** And we need to be like reserving engineering capacity probably early next week to just go prioritize the F out of that for a whole week, right?

**Marcel Santilli:** And if I can get the shaping done by Friday, end of day, then I think we can get it to a really good place, right?

**Marcel Santilli:** And that's to like turn part of that organic strategy like into reality, right?

**Marcel Santilli:** And then the second piece is us figuring out the pricing and sign-up experience and onboarding experience, know, making that experience really good and how people can, you know, swipe a credit card for 200 bucks essentially, right?

**Marcel Santilli:** Or whatever it would be, right?

**Marcel Santilli:** Just an MVP end-to-end experience.

**Marcel Santilli:** And, like, I think those two things for me will...

**Marcel Santilli:** We'll probably uncover big things like, hey, do we need to have like workspace admin rights?

**Marcel Santilli:** Like, do we need different, you know, permissioning?

**Marcel Santilli:** Do we need like a way for people to easily invite users?

**Marcel Santilli:** Do we need to push that or not?

**Marcel Santilli:** Do we need to like, what is the experience of that?

**Marcel Santilli:** Like upgrading, like where do we manage like the pricing and plans?

**Marcel Santilli:** Like, you know, support, like there's going to probably be more things that are going to come out.

**Marcel Santilli:** And so I think that one, I can focus on probably, I was thinking like focusing more on like the pricing and plans and things like that.

**Marcel Santilli:** And then the more you can help like shape it a little bit on like features and things that we need to MVP.

**Marcel Santilli:** And then I can help a little bit on the design prototyping, you know, side.

**Stevie Kim:** Okay.

**Stevie Kim:** Yeah.

**Stevie Kim:** So, um, previously you guys were really focused on the, like last week when I was onboarding, it was like.

**Stevie Kim:** The prompt quality, you know, the subcategories, all that, making sure we had that quality piece there.

**Stevie Kim:** Is that something you still want me to focus on or should I just really focus on?

**Marcel Santilli:** Yeah, yeah.

**Marcel Santilli:** Sorry, I don't mean to, like, take away from that.

**Marcel Santilli:** It's more of, like, those are the organic growth.

**Marcel Santilli:** It's what we said on the onboarding, right?

**Marcel Santilli:** It's, like, the organic growth is one piece.

**Marcel Santilli:** The quality of the data of the shared library is another piece and how we manage that, right?

**Marcel Santilli:** Which we don't have the tooling to manage that.

**Marcel Santilli:** We have some but not a ton, right?

**Marcel Santilli:** And then there's, like, the actual from sign-up to paying experience of the whole thing.

**Marcel Santilli:** And then there is, like, improving.

**Marcel Santilli:** And then within all of those, it's, like, improving versus unblocking versus.

**Marcel Santilli:** Zero to one.

**Marcel Santilli:** It doesn't even exist, right?

**Marcel Santilli:** Like, right now, the concept of signing up doesn't exist, really, right?

**Marcel Santilli:** Like, the concept of, like, billing and pricing and, you know, monetization doesn't exist yet, right?

**Marcel Santilli:** So those, that's why they're keeping me up at night is because I would hate for us to get a gen first or something and be like, okay, cool, everything is good, let's go.

**Marcel Santilli:** And it's like, oh, wait, but how are people going to sign up and pay for it, right?

**Marcel Santilli:** It's mostly, like, the unknown unknowns, whereas, like, the data quality is a known, known, you know, a known thing to go improve, you know?

**Stevie Kim:** And it's not like there is no data, essentially, you know?

**Stevie Kim:** Right.

**Stevie Kim:** Okay.

**Stevie Kim:** Writing my own notes, just in case the AI note taker is in here.

**Stevie Kim:** It's like, you don't realize how much you rely on those until they're gone.

**Marcel Santilli:** I know.

**Stevie Kim:** And then you're like, uh, I wrote like three bullet points down in my notepad.

**Marcel Santilli:** Yeah.

**Stevie Kim:** All right.

**Stevie Kim:** Yeah, that definitely narrows things down.

**Stevie Kim:** So, yeah, I mean, I'll continue to create tickets for usability stuff, but I won't focus on assigning or fixing those myself for now, just so we have them in the, the backlog when the time comes where we can make things, um, a lot more.

**Marcel Santilli:** Yeah.

**Stevie Kim:** Just clean them up a lot more.

**Stevie Kim:** So I'll just focus on the big pieces for now.

**Marcel Santilli:** One, two.

**Marcel Santilli:** Wow.

**Marcel Santilli:** Thank you.

**Marcel Santilli:** do...

**Marcel Santilli:** Thank Ready?

**Marcel Santilli:** Eight.

**Stevie Kim:** Bye.

**Stevie Kim:** Bye.

**Stevie Kim:** Bye.

**Stevie Kim:** Bye.

**Stevie Kim:** Bye.

**Stevie Kim:** Bye.

**Stevie Kim:** Yeah, because I did have some questions around that pricing stuff, because just thinking through, like, you know, as we onboard our current customers, are we giving them a discount?

**Stevie Kim:** Are we giving it to them for free for being a design partner?

**Stevie Kim:** Just thinking of, like, you know, I'm assuming we're wanting to do, you know, obviously we're trying to build internal champions, and get conversions, but from, like, their previous tools to our tool, but are we going to try to do any co-marketing or besides, you know, of course, getting future feedback?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** you.

**Marcel Santilli:** You

**Marcel Santilli:** Okay, yeah, and these docs, think that that's pretty much, yeah, those are the ones that, so it's, like, changes to, like, admin slash CMS to manage the public pages, the admin experience, continue to work on the admin experience, and adding users to it, right, like, add editors.

**Marcel Santilli:** Thank you.

**Marcel Santilli:** To work on it.

**Marcel Santilli:** The way I look at it is like every day that there is a category maybe or prompts that are not in there in the shared library or that we're tracking the wrong prompts, which I've seen a ton of that are like poorly written prompts.

**Marcel Santilli:** And no one is in there improving those prompts, changing those prompts, adding better ones.

**Marcel Santilli:** No one is enabled.

**Marcel Santilli:** There's no end to end.

**Marcel Santilli:** It's like a day that we're losing that data, which means every day that we don't have a data that's critical.

**Marcel Santilli:** It might be two weeks before we have enough data to be able to not look embarrassing, you know, or, and so that's, yeah, that's kind of how I would think about it.

**Stevie Kim:** Yeah, I've been trying to take some time to look through what we brought in from Scrunch, you know, kind of part of, yeah, I mean, some of it looks okay.

**Stevie Kim:** A lot of it doesn't.

**Stevie Kim:** That's custom library.

**Stevie Kim:** it's Okay.

**Stevie Kim:** Right?

**Stevie Kim:** So the shared library I haven't spent as much time on.

**Stevie Kim:** And so I'll look into the shared library.

**Stevie Kim:** The ones that I have seen in there are pretty basic.

**Stevie Kim:** And I, and I know that, you know, Daniel was talking about adding some, you know, like, subcategory context to the prompts.

**Stevie Kim:** And so maybe, like, the ones I saw in the shared library didn't have anything like that.

**Stevie Kim:** They were, like, super broad, super general.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Like, the, the shared library, the reason I, I'm like, if, if all our customers, we have the right prompts in there and we feel good about, we have all the most important prompts for all our customers, we are okay.

**Marcel Santilli:** Later on, we can always take some of those prompts and add it to the shared library and create a way to do that.

**Marcel Santilli:** Right?

**Marcel Santilli:** Okay.

**Marcel Santilli:** So essentially convert a workspace prompt into a shared prompt, and that's completely okay, it's all our data, no one is paying for this, no one has signed a contract saying you cannot use my prompts, it's all our data, no one is paying for this, it's all ours, we can do whatever we want.

**Marcel Santilli:** And so right now it's like add prompts in any way, shape, or form necessary, and right now we can almost convert aggressively, that's why I like my comments in Slack, I talked about the, like, there might be times where there might be prompts that are not necessarily attached to a group or a category or a tag, you know, they might just be prompts in our shared library that don't, don't have a home yet, you know, like, Brex might have added a hundred prompts, and only ten of those are from the shared library, and there's another 90 that don't, have not found a home yet, you know, and that's okay.

**Marcel Santilli:** We still want it to be part of the shared library and we just want to like systematically categorize them or manually categorize them if needed, you know?

**Stevie Kim:** Yeah.

**Stevie Kim:** Yeah.

**Stevie Kim:** I mean, looking at the subcategories and kind of trying to figure out a good way of adding more of those, because that's one of the things like I don't want to spend a bunch of time adding.

**Stevie Kim:** prompts from the shared library to a subcategory like ML Platforms is so broad, you know, where they should go under like AI observability.

**Stevie Kim:** So I like I added that as a subcategory, AI observability and monitoring.

**Stevie Kim:** So there's, I think like, as I do that a couple times, I'll figure out.

**Stevie Kim:** You're like, okay, can this be automated some way or do we just need, because like if you look at a subcategory and it has 300 brands in it, it's probably too broad.

**Stevie Kim:** You know, so there's, there's, you know, rules that we can kind of say, okay, you know, here's some educational material for internal growthx users.

**Marcel Santilli:** If, like right now though, it's like, I agree with that.

**Marcel Santilli:** And like, you just need some basic editorial comments, like human common sense, like notetaker, Evernote is on top and Notion doesn't exist in there.

**Marcel Santilli:** I'm like, wait, there's something wrong here.

**Marcel Santilli:** Like, what the ?

**Marcel Santilli:** Like, that's insane.

**Marcel Santilli:** Like Notion is not part of notetaking.

**Marcel Santilli:** Like that is insane.

**Marcel Santilli:** Come on.

**Marcel Santilli:** Like that, that's like Google Doc and, and Evernote or, and, or Google Doc and Notion are not in the same bucket as Evernote, Evernote.

**Marcel Santilli:** Like, you know, like that's just, this is a match reality, you know?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** It has to match reality.

**Stevie Kim:** Oh, 100%.

**Stevie Kim:** Like, like a rise in, is in DevOps.

**Marcel Santilli:** Yeah.

**Stevie Kim:** Yeah.

**Stevie Kim:** So, so.

**Marcel Santilli:** So we need to, like, figure out, like, and that's the, like, so really quickly, I got to run, but, like, what I would love for you to kind of think about is, like, the operating cadence of all this.

**Marcel Santilli:** And then for us to be focused more, you and I at lanes and priorities and resource allocation, you know, and I think, like, and having, like, notes and things or, like, written that we're working against so that, like, these meetings, like, you know, we can kind of tackle and get the most out of them and the most out of my brain and yours and things like that, you know.

**Marcel Santilli:** Like, meaning, you know, what, what should we tell us that I want to focus on tomorrow or Monday or whatever, right?

**Marcel Santilli:** Like, and so, and then for me, uh,

**Marcel Santilli:** Priorities are going to be to shape additional public areas, plus prototype by end of the week, and then the, like, MVP, CMS, for public pages.

**Marcel Santilli:** And then for you, I think it should be the admin experience for us to improve the prompt and shared library, right?

**Marcel Santilli:** And then maybe some discovery on just, like, how we should do the, like, monetization piece, right?

**Marcel Santilli:** Are we using Clerk?

**Marcel Santilli:** Are we using Straight Stripe?

**Marcel Santilli:** What are the pros and cons, you know?

**Marcel Santilli:** and then there's, like, it.

**Marcel Santilli:** There's a couple of these that are like super meaty.

**Marcel Santilli:** Some of these are very design-based, then some like are, ideally, we don't want like our engineers to go spend like a week reading up if we choose Clerc, Stripe, or something else.

**Marcel Santilli:** It's just like we should just go for the tried and true and talk about the pros and cons of the approach and, you know, and then like go quickly, you know.

**Marcel Santilli:** And so, what do you think?

**Stevie Kim:** Yeah, no, that sounds good.

**Stevie Kim:** Should, yeah.

**Stevie Kim:** So should I, so I should continue on the things that I've been working on, but ditch doing any small fixes, not worry about usability stuff right now.

**Stevie Kim:** Just focus on these four things, plus like the, sorry if you can hear my dog squeezing squeaky balls, really loud.

**Stevie Kim:** Lisa's loud in my ear.

**Stevie Kim:** I'm still focusing on that, you know.

**Stevie Kim:** I'm

**Stevie Kim:** Prompt quality in it, but focus it on the shared library, not the custom, and making sure the subcategories and the brand allocation to those, brand association with those makes sense.

**Stevie Kim:** And then really focusing on just getting, you know, really just the visibility and the organization of these buckets, you know, of these different lanes.

**Marcel Santilli:** Yeah, like right now, I feel like everything is kind of floating.

**Marcel Santilli:** No one is doing written updates since Jose left, and now he's back.

**Marcel Santilli:** And before, it was like, here's the lanes, like, here's what we're working towards the lanes, here's the priorities of each lane, here's what, like, here's what is blocking, here's what we're working towards, and here's what we're going to prioritize next week, you know.

**Stevie Kim:** Uh-huh, yeah, yeah.

**Marcel Santilli:** Like, no one is doing that organization, and so everybody's just free-floating and doing whatever, and, you know, or picking from the backlog, and, like, no one's bringing it together, and, like, in a cohesive way, or writing things down.

**Marcel Santilli:** And so, like, I think...

**Marcel Santilli:** It be good to use, like, this Friday as, like, hey, doing a recap, forcing everyone to communicate a bit more on, like, hey, today, this is my plan for today, right?

**Marcel Santilli:** Like, or whatever, maybe dailies too frequent or at least, like, beginning of the week or something like that.

**Marcel Santilli:** But, like, ideally, like, hey, these are the lanes we're working towards, like, fit into these lanes, right?

**Marcel Santilli:** So that then, like, everything is contextualized against these lanes.

**Marcel Santilli:** And if there's, like, surprises above and beyond that, then we can, you know, kind of work against it.

**Marcel Santilli:** Because the risk here we're trying to mitigate is busy and not effective, you know?

**Stevie Kim:** Yeah.

**Stevie Kim:** Yeah.

**Stevie Kim:** So, I mean, it's definitely felt, the way you described it, it's felt like that to me that I thought that it had been working that way till now.

**Stevie Kim:** You know, I thought it had been effective.

**Stevie Kim:** Would it be worth kind of organizing it similar to, you know, client ops where, you know, like, we don't have to do actual cycles, but we.

**Stevie Kim:** do have that, you know, like kind of kickoff.

**Stevie Kim:** This is the theme.

**Stevie Kim:** This is what we're focusing on for, you know, we can time chunk it two weeks or whatever, just to keep people focused.

**Stevie Kim:** It needs to be time box to me because otherwise there's just no end to it.

**Stevie Kim:** And then people, it just gives us like, is this, you know, this is never ending or it makes it easier to get sidetracked and pull on to other things.

**Stevie Kim:** Because if you're working on this lane and it's never ending and, you know, does that make sense?

**Marcel Santilli:** But we can solve for that, right?

**Marcel Santilli:** Like solving for what is the right iteration cycle or right cycle length or whatever, that's different, like, and important.

**Marcel Santilli:** But, like, I think as you're coming up to speed, you know, doing even like, start with the Friday update, right?

**Marcel Santilli:** Like, and first let's organize even our meeting, like you and I.

**Marcel Santilli:** And the lanes so that like we're on the same page in the lanes and how we communicate the lanes and then like and how we're doing in each lane, what the priorities are for each lane.

**Marcel Santilli:** And then next week we can try to get like everybody to update it a little bit more and us to like use that as a way to communicate with everyone because we're in these check-in meetings on Monday and it's just like just no structure to it, right?

**Marcel Santilli:** And then no longer like go back and try to find like the updates from Jose.

**Stevie Kim:** Yeah, there was there, you know, on the linear overview of the project, he had created the updates, he used that.

**Marcel Santilli:** Perfect.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Like I, those were like really, really, really, really helpful, you know?

**Marcel Santilli:** And so like I think us doing a version of that, so maybe you and I work on like a draft for that on...

**Stevie Kim:** I'm out on Friday.

**Marcel Santilli:** have a funeral to go to this weekend.

**Marcel Santilli:** No worries.

**Marcel Santilli:** It can be, like, Monday or whatever.

**Marcel Santilli:** But the goal is to hopefully, like, some update.

**Marcel Santilli:** Are you out tomorrow?

**Stevie Kim:** No, just Friday.

**Marcel Santilli:** Maybe we do it as, like, a tomorrow-by-end-of-day update, you know, of just, like, hey, just want to regroup us, you know, on where we are, state of things, you know.

**Marcel Santilli:** And then that will kind of help set, like, a little bit more context and framing for everybody else, you know.

**Marcel Santilli:** What do you think?

**Stevie Kim:** Yeah, no, that would help me a lot, too, because, yeah, trying to ramp up on something where it's just, like, you have all these milestones.

**Stevie Kim:** But it's not organized in any way.

**Stevie Kim:** And it's, like, all running in parallel.

**Stevie Kim:** And when you have so many.

**Stevie Kim:** It, you really, yeah, it's like, what is the focus?

**Stevie Kim:** If everything's a priority, what's the priority?

**Marcel Santilli:** And, and like, I need your help of bringing like that focus and organization to, to the chaos, right?

**Marcel Santilli:** And I think that starts with both like our meetings, as well as the weekly meetings, as well as forcing everyone to do really good asynchronous communication and organizations and writing.

**Marcel Santilli:** And that has to start with us as well, you know?

**Marcel Santilli:** So then like, the more we do that, the more people are going to have like more and more clarity on, on like what they're focusing on and why.

**Stevie Kim:** Yeah, that makes sense.

**Stevie Kim:** Cool.

**Stevie Kim:** I'm going to, for now, keep things in linear as it makes sense.

**Stevie Kim:** Longer form stuff, I'll keep in Notion.

**Marcel Santilli:** Cool.

**Marcel Santilli:** Cool.

**Marcel Santilli:** Sounds good.

**Marcel Santilli:** Awesome.

**Marcel Santilli:** I will spend a little more time on finishing this presentation for HubSpot.

**Marcel Santilli:** And then like tomorrow, it's going to be most of my, my, my focus is the stuff on check that.

**Stevie Kim:** Okay.

**Stevie Kim:** And I tend to work later, so you'll find, you know, so yeah, if you have anything that you want me to focus on or whatever, you'll find me at 8 p.m., more than 8 a.m., we'll just say that.

**Stevie Kim:** All good.

**Stevie Kim:** Sounds good.

**Stevie Kim:** Awesome.

**Stevie Kim:** Thanks, Stevie.

**Stevie Kim:** Talk soon.

**Stevie Kim:** Bye.
