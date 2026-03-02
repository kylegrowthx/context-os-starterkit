# Lovable <> GrowthX - Weekly Sync

<metadata>
date: 2025-10-08
time: 19:59 UTC
duration: 31 minutes
organizer: team@growthxlabs.com
participants: Marcel Santilli, George Haikal, Aida Knezevic, Nad Chishtie, Rachel Hepworth, Fern
fathom_recording_id: 92857310
fathom_url: https://fathom.video/calls/434042757
share_url: https://fathom.video/share/BjDP69B5owokST8u-tq4bUTAro93QjVy
source: fathom
enriched_on: 2026-03-02 14:35 UTC
</metadata>

---

## Summary

GrowthX and Lovable aligned on strategy for two parallel workstreams: SEO-optimized editorial content targeting publication next week, and a template library MVP featuring five production-ready samples demonstrating quality standards. The core tension centered on quality expectations—GrowthX seeks to generate hundreds of scalable templates per category (e.g., construction, landing pages) at 80% polish for remixing, while Lovable's design team (Nad) emphasized avoiding "slop" and ensuring a baseline quality threshold. The team resolved this by separating concerns: long-tail SEO templates (GrowthX's domain) and homepage-featured designs (Lovable's design bar), with Nad taking ownership of CMS scaffolding and GrowthX driving content creation. An engineering sync between Nad and George Main/Nico (GrowthX) was scheduled to unblock GitHub and backend access issues.

---

## Context

Lovable is an AI-powered platform for building web applications and websites. GrowthX is partnering with Lovable on a strategic multi-month engagement to deliver SEO-optimized editorial content and a template library. Rachel Hepworth (Lovable's key contact) had recently met with Lovable's exec team at an Excel investor board meeting, and Nad Chishtie (Lovable's head of design) joined this weekly sync to align on engineering workflows and design standards. This is week four of the engagement—a critical inflection point where the team needed to push through the "valley of despair" to demonstrate early wins and momentum. The stakes are high: successful execution could unlock both editorial SEO traffic and a scalable template library as a major feature for Lovable's platform.

---

## Relevance

**To GrowthX Delivery:**
- Established clear separation of concerns: GrowthX owns content creation and long-tail SEO strategy; Lovable design owns CMS scaffolding and quality bar for featured templates. This operational clarity should reduce friction.
- Confirmed commitment to publish editorial content by next week—tangible deliverable that can start generating indexed pages and SEO signals. This is the "momentum moment" Marcel flagged.
- Weekly sync cadence may shift to daily updates if blockers emerge, signaling high priority and rapid iteration expected.

**To GrowthX Business Development:**
- Strong engagement signal: Lovable's head of design (Nad) and Rachel (key stakeholder) both leaning in. Rachel running into Lovable exec team at Excel board meeting shows strategic alignment at leadership level.
- Account health positive: They've committed to 5 production-ready template samples within a week despite quality disagreements. Shows willingness to iterate and move fast.
- Expansion potential: Once editorial + templates prove the model works, opportunities to expand into other verticals or white-label this template system for other no-code platforms.

**To CheckThat / AEO:**
- Template library strategy is inherently SEO-focused: building thousands of indexable pages per category (construction, landing pages, etc.) to compete with Wix, Webflow, Base44 in long-tail search.
- This execution demonstrates the power of AI-generated, SEO-optimized content at scale—a core thesis of CheckThat's AI visibility work.

---

## Overview

- Engineering sync scheduled between Lovable engineers (TBD by Nad) and GrowthX's George Main & Nico to resolve GitHub repository access and backend setup required for template development
- Quality bar aligned: Long-tail SEO templates target 80% polish to enable remixing; homepage-featured designs held to higher creative standard—these are separate buckets with different constraints
- Dual publication targets for next week: (1) Editorial content goes live; (2) Template library MVP includes 5 production-ready representative samples showing achievable quality across categories
- Design ownership clarified: Nad to set up CMS scaffolding and templates; GrowthX to drive content creation and provide 10 representative examples for quality sign-off

---

## Key Topics

### Project Overview and Goals

  - Two main goals: publishing SEO-optimized editorial content and creating starter kit templates
  - Editorial content publishing targeted for next week
  - Template project aims for V1 MVP and agreement on page design by next week
  - Sebastian working on design-forward templates separately

### Template Library Strategy

  - Aim to create indexable pages for long-tail SEO benefit, unlike competitors
  - Balancing logged-in vs. logged-out experiences
  - Creating thousands of templates across categories (e.g., hundreds for construction websites)
  - Challenge: meeting high-quality bar while maintaining scalability

### Quality Expectations and Alignment

  - Differing perspectives on quality bar between GrowthX and Sebastian (Lovable)
  - Need to define "good enough" quality for SEO-focused templates vs. homepage features
  - Suggestion: Provide 10 representative examples for review and alignment
  - Current quality target: Better than community-generated, unique, and 80% there for easy remixing

### Engineering Setup and Workflow

  - GrowthX team received GitHub access but needs backend setup
  - Action: Schedule call between Lovable and GrowthX engineers to resolve setup issues
  - Nad to identify key engineering stakeholders on Lovable side

### Content Creation Process

  - Exploring various methods: one-shot generation, programmatic iteration, GitHub integration
  - Challenges with importing external designs (e.g., from Figma) into Lovable
  - Testing different tech stacks and integration methods

### Blog/Guides Section

  - Current blog design acknowledged as suboptimal; improvements planned
  - Suggestion to create a separate /guides section initially, mirroring current blog structure
  - Nad offered to take ownership of CMS scaffolding and templates

---

## Action Items

**Nad Chishtie (Lovable)**
- Identify 1–2 Lovable engineers to join engineering sync call with GrowthX team; determine key engineering stakeholder on Lovable side to sponsor this work
- Send follow-up messages to Rachel clarifying engineering involvement and GitHub/backend setup path forward

**George Haikal (GrowthX)**
- Schedule call between Lovable engineers (to be identified by Nad), George Main, and Nico to resolve GitHub access and backend setup blockers

**Rachel Hepworth (Lovable)**
- Hunt down internal examples of high-quality Lovable-built applications to establish concrete quality reference point for template library discussions

**Aida Knezevic (GrowthX)**
- Prepare and send list of content topic suggestions (mix of informational and commercial intent, varied search volumes) to Rachel via Slack for editorial pipeline

---

## Transcript
**Nad Chishtie:** This meeting is being recorded.

**Aida Knezevic:** Hi, good morning.

**Nad Chishtie:** Good to see you.

**Nad Chishtie:** Good, how are you?

**George Haikal:** Good, man.

**George Haikal:** Good to see new faces getting added to the project.

**Nad Chishtie:** Yeah, it's like snowballing, like every thread feels like there's more of people.

**Nad Chishtie:** But it's good.

**Nad Chishtie:** But Rachel, I was just chatting with Rachel and it became a good idea to join this call basically just to try.

**Nad Chishtie:** And figure out some of this like GitHub access stuff and try and figure out like what the right path forward is basically.

**Rachel Hepworth:** And Nad, did you intro yourself?

**Nad Chishtie:** No.

**Rachel Hepworth:** Nad's Lovable's head of design.

**Rachel Hepworth:** So a very helpful person to have in this call.

**George Haikal:** Amazing.

**George Haikal:** Amazing.

**George Haikal:** Love that.

**George Haikal:** How are you, Rachel?

**Rachel Hepworth:** I'm good.

**Rachel Hepworth:** Again, I'm at the Excel office, Lovable's investors, and I ran into the whole Lovable exec team here for a board meeting.

**Rachel Hepworth:** And that was pretty funny.

**Rachel Hepworth:** I didn't even know they were going to be here.

**Rachel Hepworth:** So that was fun to say hi to everybody.

**George Haikal:** Nice.

**George Haikal:** The nice random, random bumping.

**Rachel Hepworth:** Yeah, like worlds colliding.

**Rachel Hepworth:** Cece can't make it.

**Rachel Hepworth:** She is in a different meeting.

**Rachel Hepworth:** Are we waiting for Marcel or?

**George Haikal:** Yeah, we'll give him one minute.

**George Haikal:** Okay.

**George Haikal:** I know you guys are meeting running late.

**George Haikal:** And if not, we could just jump in.

**George Haikal:** Okay.

**George Haikal:** I think I started as well.

**George Haikal:** But quick update on my end from yesterday.

**George Haikal:** know we have been going, or actually before that, was CC able to fill you in on kind of the template stuff and Sebastian, how we were thinking about the project overall from yesterday?

**Rachel Hepworth:** Very briefly, but I think what might be helpful is to give like a two or three minute overview for NAD so he has some context.

**Rachel Hepworth:** And then I think the update about Sebastian will also be helpful for that.

**Rachel Hepworth:** And then we can kind of go from there.

**George Haikal:** Great.

**George Haikal:** I can start from there.

**George Haikal:** So, Nad and hey, Fern, good to kind of see you in person.

**George Haikal:** Right now, our main goal, and I'll just pull up the agenda while we're here.

**George Haikal:** It's going to make it easier.

**Rachel Hepworth:** Pull it up.

**George Haikal:** Hi, Marcel.

**George Haikal:** Welcome as well.

**Marcel Santilli:** What's up, team?

**Aida Knezevic:** How goes that?

**Rachel Hepworth:** Hi.

**George Haikal:** Perfect timing, Marcel.

**George Haikal:** Nad joined, who's their head of design, and was just about to give a high-level overview of the project.

**George Haikal:** For them, to give more context.

**Marcel Santilli:** All right.

**Marcel Santilli:** I love it.

**Marcel Santilli:** I feel like we keep adding more friends to the platform.

**Marcel Santilli:** That's what I said.

**Marcel Santilli:** I appreciate it.

**Rachel Hepworth:** This is important for Lovable.

**Marcel Santilli:** Yeah, yeah.

**George Haikal:** Amazing.

**George Haikal:** I'll keep it very quick and then Marcel will add anything that I might miss, but essentially we have two main goals.

**George Haikal:** One is publishing editorial content for you all, high quality, SEO optimized, and then the template project.

**George Haikal:** So we want to create these starter kits, starter kit templates, also optimized for SEO, but intent and retention data that we've gotten from your team.

**George Haikal:** That's the super, super high level goal, and there's a lot that goes into each one, which we use these meetings every week to run through progress against.

**George Haikal:** Ideally, we want to be publishing by next week on the editorial side and the templates have a V1 of the MVP and agree on what a really good page looks like.

**George Haikal:** By next week as well.

**George Haikal:** And then Sebastian.

**George Haikal:** In parallel is working on templates himself that are more design-forward, solving for UX, and less on the intent SEO search volume side.

**George Haikal:** So that is what we've been balancing the last week and what Rachel and I were speaking about from the meeting with CeCe yesterday.

**Rachel Hepworth:** Can you give, maybe can you show like the templates part to Nad, because he's probably going to be pretty interested in what that looks like and what you, and by the way, Nad, the plan is always to have design involved in this, so we're not going to publish anything that like, you guys haven't looked at.

**Rachel Hepworth:** We have discussed that.

**Marcel Santilli:** Yeah, maybe, Rachel, super, super quick, just like the TLDR here, and then we'll jump in super quick, as like, we're week four, I think we made decent progress, and week four, normally when companies want to move fast, it tends to be that week where it's like, it's kind of like the valley of despair a little bit.

**Marcel Santilli:** I don't mean to make that sound bad, but just the reality is there's ambiguity...

**Marcel Santilli:** They're like, wait, what are we doing here again?

**Marcel Santilli:** And that usually we have to kind of push through a little bit to make sure we get to something that can start showing signals and results.

**Marcel Santilli:** I think luckily we have two lanes and we are willing to do whatever it takes to make sure we're exceeding expectations.

**Marcel Santilli:** But also knowing that there's like a lot of really smart people with a ton of contacts here that are going to care about slightly different things, rightfully so.

**Marcel Santilli:** And so personally, like what I would encourage us is like on the editorial site, I think that's a lane that we can create a new section of the site, you know, that looks exactly like the blog to start that we will improve the experience over time.

**Marcel Santilli:** We've done a ton of work to align and calibrate on the content.

**Marcel Santilli:** Let's get some content out so we can start showing results and making sure those pages get indexed and, you know, the quality is good and start to kind of build momentum there, right?

**Marcel Santilli:** And then on the template library, we can align.

**Marcel Santilli:** And maybe try to separate, there's three lanes here, right?

**Marcel Santilli:** One lane is the actual MVP experience.

**Marcel Santilli:** And what is that minimum viable experience that still contributes to the perception of the brand, but also knowing that there's trade-offs there that we can make, but we're super flexible here.

**Marcel Santilli:** Then there's the strategy itself of why we're doing this to begin with.

**Marcel Santilli:** And then there's like the substance itself, which is like the content that goes to the page and the source code of the actual thing that we built, you know, that we're going to build, right?

**Marcel Santilli:** And I think like, well, let's dig in to those, but just like, just remember there's like three lanes essentially in the templates library.

**Marcel Santilli:** So the level of complexity is a little bit more complicated.

**Marcel Santilli:** So maybe we try to address them slightly one at a time if possible, but then it still might not all make complete sense.

**Rachel Hepworth:** Sorry.

**Rachel Hepworth:** I just want to make sure Nad gets up to speed so he can.

**Marcel Santilli:** Help, help as best as you can.

**Marcel Santilli:** Awesome.

**Marcel Santilli:** That sounds good.

**Marcel Santilli:** George, do you want to show the latest on the template library?

**Marcel Santilli:** And so, Nad, just to give you a little bit of context, right?

**Marcel Santilli:** Like, this is still a prototype, and what we're working on right now is lovable fine.

**Marcel Santilli:** So that it looks more aligned on brand and with the rest of the experience of at least the homepage, you know, but then, like, we're, this is, so this is, like, take this as a prototype with a little bit, like, a little bit more bells and whistles than probably the MVP experience would be, but that hopefully captures a little bit of the essence of what we're trying to do.

**Nad Chishtie:** By the way, just to, just to maybe frame from my side, like, I know you've already been speaking to Felix, and so I kind of know that this design feedback and process is in, is in flight.

**Nad Chishtie:** The reason why I joined today was mostly just to figure out workflow-wise, how you're working and see if I could help on this GitHub setup stuff to try and figure out who else to pull in from our side as well.

**Marcel Santilli:** Perfect, perfect.

**Marcel Santilli:** Yeah, and sorry, just to make sure I understand, like, on the getting access to GitHub and the workflow of, like, where would be best to give us input, is that a fair summary?

**Nad Chishtie:** Well, no, just there's two things.

**Nad Chishtie:** As far as I understand it, you have access to GitHub, so you've been able to set up the repo, but having the code base is only one half.

**Nad Chishtie:** You also need, like, you know, access to the backend that our client connects to, et cetera, et cetera, a bunch of stuff that can actually run.

**Nad Chishtie:** And so I just wanted to figure out, like, A, double-check who was setting you up so far from the engineering side, and then from there I can kind of figure out which blanks to fill in and we figure out the most pragmatic path forward.

**Marcel Santilli:** Perfect. I think we got access this morning. Sebastian was out, so it took a few more days, but I think now we're unblocked on that. I think what would be useful is to do a separate session between you and our engineering team—they'll be better at telling you what else we need to fill in the blanks.

**Nad Chishtie:** No, I'm just going to say like, I think like the simplest thing would be like, we should probably get one or two of our engineers just on a call with your engineers, like very specifically, and there's like four or five small things to hash out, and so, I mean, from my side, I can figure out like who is the main sponsor of this on the engineering side, and then if you know precisely who you, like who you need to have involved.

**Nad Chishtie:** Then I might not even need to attend the call myself, but I can at least get the right people in the room together.

**Marcel Santilli:** Perfect.

**Marcel Santilli:** Okay.

**Marcel Santilli:** Fantastic.

**George Haikal:** Yeah, we can get that set up.

**Marcel Santilli:** Sebastian's been interacting—have we engaged with anyone else on the engineering side, right, George?

**George Haikal:** Correct.

**George Haikal:** Yeah, Gustav today we just reached out to, but he said he doesn't have admin access to actually give to the team on the back end.

**George Haikal:** So we'll definitely connect you with George Main and Nico who are running this on our end.

**Rachel Hepworth:** Nad, is there anything you need to know to figure out who is the right person on the lovable side to be on the call?

**Nad Chishtie:** I just need, so I mean, just to clarify, like the kind of key stakeholders here are like yourself and Sebastian, right?

**Rachel Hepworth:** Is that correct?

**Nad Chishtie:** On the lovable side?

**Rachel Hepworth:** Yeah.

**Rachel Hepworth:** Yeah, I'd CC as well, but yes.

**Nad Chishtie:** Yeah, okay.

**Nad Chishtie:** But there's been no one else in engineering like sponsoring this so far?

**Rachel Hepworth:** No, no.

**Rachel Hepworth:** We've had some people come in and help with things, but like nobody deeply involved.

**Nad Chishtie:** Okay.

**Nad Chishtie:** Okay.

**Nad Chishtie:** That's enough for me.

**Nad Chishtie:** I'll send you a couple of messages just to clarify a few things and then I have an idea of who like the one or two people are on our side to get involved in this.

**Marcel Santilli:** Yeah, and just maybe give just a tiny little bit more context to where your competitors have gotten it wrong and where we're hoping to do it slightly different is that Base44, Bold, and a few others, how they handle the templates is pretty much within the app experience.

**Marcel Santilli:** And it doesn't, none of the actual templates and listing pages get indexed as actual pages, which then brings you no long tail benefit of like, you know, organic traffic beyond people that already love the brand, which is what we're trying to optimize for, you know, is like if you search for, like if you look at Wix or Webflow and a few others, like a lot of the listing pages themselves as well.

**Marcel Santilli:** Fern probably knows this well. And we're working closely with Rachel at her company on their templates too, but for a completely separate reason. The key insight is the listing pages—similar to an e-commerce site or TripAdvisor, where one of our SEO folks ran SEO. The listing pages themselves are the real gold mine.

**Marcel Santilli:** And so we just want to make sure that the way we're building it allows us to do that one, which we're confident in.

**Marcel Santilli:** But then balancing out the logged in versus logged out experience and how today you handle it or how you recommend us handling that part, right?

**Marcel Santilli:** Like, in other words, like if you go to your pricing page, you know, are there logged in states versus logged out states?

**Marcel Santilli:** And then there's little functionality that might not be needed in the MVP but enables remixing. It's about how we gain that context and integrate it into the experience. If we need to defer it to post-launch, at least having the context now means we won't back ourselves into a corner.

**Marcel Santilli:** I hope that was helpful.

**Nad Chishtie:** Makes sense.

**Marcel Santilli:** Perfect.

**Marcel Santilli:** And anything else on the template project that you think would be helpful, Rachel?

**Rachel Hepworth:** Well, I know there was a conversation. Cece caught me up a bit, but very briefly.

**Rachel Hepworth:** I guess my question is, other than making sure we have good, on the lovable side, ENG oversight, are there any other concerns based off the conversation with Sebastian or things that we need to work out that I can help with?

**Marcel Santilli:** I think that it's just different goals.

**Marcel Santilli:** And so, the way to think about it is, what we're best at is giving the strategy and hopefully accelerating the scaffolding of what this experience should look like.

**Marcel Santilli:** And then the words that go in there and, you know, creating an engine to create a foundation of like thousands and thousands of templates, right?

**Marcel Santilli:** It's not just like, for instance, like let's take a website template, like construction website templates.

**Marcel Santilli:** It's not one template.

**Marcel Santilli:** We're talking like hundreds of templates just within that category that we have to fill in, right?

**Marcel Santilli:** Whereas from what we heard from Sebastian is like he cares deeply, rightfully so, like on the homepage, what's showing up there.

**Marcel Santilli:** And it's the super ultra premium, beautifully built app.

**Marcel Santilli:** And we believe it's like a direct trade-off if we focus on building, you know, a food ordering app that's better than Uber Eats for launch.

**Marcel Santilli:** It's going to be the trade-off of one in exchange for maybe a thousand or a hundred, you know?

**Marcel Santilli:** And in our experience using lovable, like that's a pretty difficult bar to do programmatically with one shot or even two shots or three shots.

**Marcel Santilli:** And, you

**Marcel Santilli:** We were confident we could do it if it was pure code, but it would be really difficult to hit that bar programmatically for 3,000 pages.

**Rachel Hepworth:** So Sebastian's concern is you're going to programmatically create pages that include prompts, and the prompts are not going to create excellent apps, and that's the concern.

**Rachel Hepworth:** Is that the right story?

**Marcel Santilli:** The framing, the way I would think about it is, like, we are coming up with a bunch of different creative ways to, you know, Lovable obviously has strong opinions on the stack, right?

**Marcel Santilli:** Lovable mostly uses Tailwind and Bit, so there's a certain stack with current limitations. I think it's about 50K tokens of context you can feed it, and how the agent does the planning.

**Marcel Santilli:** We're creating different workflows to find the best one-shot approach. If that only gets us 70% of the way, we find more scalable techniques. Humans in the loop is fine—but having a human manually review and tweak each of 3,000 pages wouldn't scale.

**Marcel Santilli:** So we're trying to do it at a bigger scale.

**Marcel Santilli:** And so we're playing around with different options right now.

**Marcel Santilli:** Even our CTO has been helping me with this.

**Marcel Santilli:** But we feel really good that we'll get to a place where for both simple apps, simple landing pages, simple websites, and simple components, we can create a beautiful library that's actually substantially better than the community-driven versions of those, right?

**Marcel Santilli:** Like significantly better.

**Marcel Santilli:** And we'll have a landing page with great descriptions and a sample prompt.

**Marcel Santilli:** Obviously, that sample prompt won't get you exactly to what's shown. So they can remix it from there.

**Marcel Santilli:** Now, the bar that I think Sebastian was talking about from what I understood is even higher than that.

**Marcel Santilli:** He wants award-winning, beautiful apps fit for a design gallery on the front page—the featured apps, which is an amazing goal.

**Marcel Santilli:** And that's the area that if we can not focus on that and focus on everything else, that would help us.

**Marcel Santilli:** Because if we focus on hitting that bar from what we understood from him is, is like, we're going to be a pretty difficult bar to hit.

**Rachel Hepworth:** I think maybe what might be helpful here, and I don't have an instant way to do it, is to try to figure out what, like, what good looks like.

**Rachel Hepworth:** Because when I talked to Cece, the way she framed it was not quite that.

**Rachel Hepworth:** It was more like, Sebastian wants good quality, and he's worried that it will be slop, you know, versus like, amazing award-winning quality, and good is not good enough.

**Rachel Hepworth:** And, you know, we could talk about this ad nauseum, but if there's a way for us to have a way to judge of, like, we all agree this is good enough or not, that we can align, that'll help us more.

**Rachel Hepworth:** Otherwise, it's just a lot of words and debating, and I'm worried that we'll get stuck here with, like, different definitions.

**Marcel Santilli:** Is there a good way to figure this out and validate quality?

**Rachel Hepworth:** yeah.

**Marcel Santilli:** And so this is the example, one of the examples we showed, right, where this is like a getting things done to do app.

**Marcel Santilli:** And this is a one-shot app, given this one's an example we built for Bolt, right, like this is one-shot for Bolt, and we show this, and I think Sebastian was like, yeah, this is better, but like, I'm talking like way higher than this, even, you know, and I think like.

**Rachel Hepworth:** Because I want to separate out anything going on the homepage, which I think we can, like, that's obviously a very different bar from like the, the SEO.

**Rachel Hepworth:** And by the way, Nad, if you have any thoughts as you're listening to this, feel free to check in, I'd be very curious from your opinion.

**Rachel Hepworth:** But, yeah, my biggest thing is just like, how do we more concretely align around what the quality bar is, and then we can like hit it or not, or to, to scale a project.

**Marcel Santilli:** But, yeah, like, this is the bar of quality that we feel confident we can hit, and level of detail.

**Marcel Santilli:** It could be even improved from here, but I think like, you know, this is a bar that I think we can create good quality as a starting point base and then build from there.

**Marcel Santilli:** This example doesn't meet Sebastian's bar, I can confirm.

**Rachel Hepworth:** So he said this app is not good enough.

**Rachel Hepworth:** Nad, do you have any in the moment thoughts?

**Rachel Hepworth:** You're on mute.

**Nad Chishtie:** Yeah, okay.

**Nad Chishtie:** I'm going to give you a very unsatisfying answer: it completely depends on the goals. This looks fine for boilerplate—if it's one of many, not prominent, and about getting breadth out there, then okay. But if it's going to be the homepage saying "this is the future of software development," probably not. It depends on what the goals are, which I'm lacking exact context on.

**Rachel Hepworth:** For the SEO library, which we're trying to scale, it's about growth, awareness, scale and breadth.

**Rachel Hepworth:** Agree that for the homepage, there's obviously a different quality bar.

**Rachel Hepworth:** I don't believe anybody's disagreeing with that, though.

**Rachel Hepworth:** So that seems totally fine and not in conflict.

**Rachel Hepworth:** We could have a featured front page for the template library, and then the long tail. We did this in Notion—we had a curated front page of the best items, and then a long tail of varying quality including community-generated content. The featured items get 80+ percent of the traffic, and we make sure those are better quality.

**Rachel Hepworth:** But is there any reason we can't arrange that in this project?

**Rachel Hepworth:** We're like, obviously, my assumption was none of these were going to be on the homepage anyway.

**Rachel Hepworth:** So there's not a homepage issue.

**Rachel Hepworth:** And that we could designate what goes on, like, if there's a templates homepage, if we design it like that, that also gets a human.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** If, if we can align on that, that would be helpful, because like, then, then we know.

**Marcel Santilli:** What we're trying to, to hit, right?

**Marcel Santilli:** Like, and, and then like, we can solve for the specifics, like, and so, like, we're, we're testing out a of different paths.

**Marcel Santilli:** And we do think that single page lending pages is a great place to start because there's like a lot of potential there.

**Marcel Santilli:** And if you look today at even Bolt, Base44, and what's in your homepage, although the homepage is not necessarily what we're optimizing for, there is a lot of things that are like pretty poorly built and very buggy and kind of like, you know.

**Rachel Hepworth:** Yeah, I think current state is not the bar we want to have.

**Marcel Santilli:** Yeah, and so like my recommendation here is like, we, the only way we're going to get to the, the, like, Webflow and Framer level templates, let's just take websites, let's put apps aside for just a second, right?

**Marcel Santilli:** Like, but, but the only way you're going to get to a place where.

**Marcel Santilli:** Where like our website pages are going to get to this is going to be through like an evolution.

**Marcel Santilli:** Like I don't think you're going to, we're going to be able to one-shot this, right?

**Marcel Santilli:** And so I think we're going to be able to get things that like get incrementally closer and closer and they're already unique and pretty good and better than what the community has generated.

**Marcel Santilli:** And that allows people to express their creativity by building upon something that's already, you know, 80% there.

**Marcel Santilli:** I think it's a great starting point. If I come to something like this that's 80% there, I feel way more motivated to remix it versus starting from scratch. We're still in the trial period and need better icons and imagery, but this demonstrates the opportunity.

**Rachel Hepworth:** So are you guys blocked on something, or are you waiting on something right now? I'm trying to figure out where you are in the process—are you moving forward and just want to make sure nothing becomes a problem?

**Marcel Santilli:** We are, I think, pending just the engineering call just to make sure and then making sure we align on the experience itself.

**Marcel Santilli:** We are not blocked.

**Marcel Santilli:** The trade-off is: we can spend the next four weeks perfecting one or two app experiences to an insane level of quality, or we can spend that time creating workflows, content, and sample apps to start building out the full catalog.

**Rachel Hepworth:** I think what might be helpful.

**Rachel Hepworth:** Because I think perfection is the enemy of progress here is maybe to, when you guys feel you're ready, give us like 10 examples of like, these are 10 that we feel are representative of what this will look like.

**Rachel Hepworth:** Maybe that's one of the best ways.

**Rachel Hepworth:** And we can sort of be like, yes, no, this hits our bar.

**Rachel Hepworth:** If no, why, what is there to work on?

**Rachel Hepworth:** If yes, like, go forth and conquer.

**Rachel Hepworth:** And then just all chat with Cece and Sebastian just to make sure.

**Rachel Hepworth:** But also, you know, again, not for the homepage.

**Rachel Hepworth:** Like this is for long tail SEO.

**Rachel Hepworth:** This is not like marketed all across the homepage of our website.

**Marcel Santilli:** So the bar is lower and the risks are lower.

**Marcel Santilli:** Like, I think we will do that in parallel, if at all, like folks have any bar of things that were built in Lovable that they feel like.

**Marcel Santilli:** is really amazing.

**Marcel Santilli:** Even one example would be amazing because like you said, it's so hard for us to know.

**Marcel Santilli:** When people say we need quality, we need quality.

**Marcel Santilli:** It's like the bars that for websites, it's a little bit easier because we can just look at Framer, Webflow, Wix, and a few others and find templates that are good enough to be in the marketplace.

**Marcel Santilli:** And that's the bar we're trying to hit.

**Marcel Santilli:** Apps are trickier—the bar for a calendar app is Calendly, and reverse engineering that in one shot is a challenge. You can't just build an Uber Eats clone and call it done.


**Rachel Hepworth:** I'll see if I can, I'll see if I can hunt up some examples.

**Rachel Hepworth:** I think some of that is like asking internally and figuring out what people think is good is a useful exercise.

**Rachel Hepworth:** So I can take that action item.

**Marcel Santilli:** To recap our approach: we start with one-shot generation, then find ways to programmatically iterate on it.

**Marcel Santilli:** We're integrating the one-shot output with the GitHub repo, plugging into Cloud Code to get recommendations based on our framework and best practices, then cycling that back into Lovable.

**Marcel Santilli:** We've tested exporting fully-built Tailwind and Bit code and trying to import it into Lovable, but Lovable struggles with that—it breaks when you try to build on top of it.

**Marcel Santilli:** We're also testing the Builder.io integration with Figma designs, but Builder.io produces better results than Lovable. The challenge is hitting the quality bar with Lovable in a way that's replicable for others.

**Rachel Hepworth:** That makes sense.

**Rachel Hepworth:** Really quickly on the blog, because I know we're almost out of time.

**Rachel Hepworth:** Nad, did you have any concerns or questions there that you wanted to talk about?

**Nad Chishtie:** Not a concern, but just an FYI: the blog design needs work and we're going to improve it.

**Nad Chishtie:** But if you're just duplicating that for guides, we'll just figure out how to merge everything, basically.

**Nad Chishtie:** And they'll get better.

**Marcel Santilli:** Nad, we can share our thought process here. We did this with Augment Code: created a /guides section, reused their blog structure even though they weren't totally happy with it, and 10x'd their traffic. If there are things you'd like to highlight...

**Marcel Santilli:** And you're like, hey, this is what, this is an inspiration, or this is a reference point that we really like.

**Marcel Santilli:** It would be good for us to just keep that in mind, too, because our goal is not to, it's just to unblock publishing.

**Marcel Santilli:** But it's like, we also agree, like, it's not a great experience, you know, like, yeah.

**Nad Chishtie:** What would work well is if you share that Notion document you screen shared earlier. We could take ownership of setting up the CMS scaffolding and templates, and then you drive the content creation. That's a clean division of ownership.

**Marcel Santilli:** Great. We'll schedule the engineering deep dive and align separately with Nad on the MVP experience. Rachel, we're not blocked but we'd love your feedback—we did a comparison and sent some calibration samples. Can you just give us a thumbs up or down on whether we should keep going, or if there's feedback we're missing?

**Aida Knezevic:** I'll send over a list of content suggestions for the next couple of weeks in Slack—it's a mix of informational and commercial content with varied search volumes. You can give me a thumbs up or down.

**Marcel Santilli:** Well, we're excited.

**Marcel Santilli:** We're pushing hard. I apologize if things feel a bit messy—there are a lot of moving pieces and context to align on. For me, a collective win next week would be publishing editorial content, getting pages indexed, and seeing initial signals. The other win would be having five production-ready template samples that show the content and experience. Then we focus on scaling to production and cranking out the rest of the catalog in parallel. These are ambitious but achievable goals. We'll increase daily updates if we hit blockers or need feedback.

**Rachel Hepworth:** Sounds good.

**Marcel Santilli:** Awesome.

**Marcel Santilli:** Well, thanks, team.

**Rachel Hepworth:** I appreciate y'all.

**Rachel Hepworth:** Thanks, guys.

**Aida Knezevic:** Thank you. Bye.
