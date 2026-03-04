# Lovable Templates Check-In

<metadata>
date: 2025-10-17
time: 16:16 UTC
duration: 59 minutes
organizer: Georgemaine Lourens
participants: George Haikal, Nicolas Castellanos, Georgemaine Lourens, Marcel Santilli
fathom_recording_id: 95022097
fathom_url: https://fathom.video/calls/443869905
share_url: https://fathom.video/share/7ELTQqoPeS8dTCfHcSMRqiGA6rKSsgaj
source: fathom
enriched_on: 2026-03-02 14:35 UTC
</metadata>

---

## Summary

GrowthX and Lovable confirmed client approval of the website experience and template designs, with Lovable serving as a happy customer reference. The team aligned on building a scalable pipeline for generating diverse blog templates using AI-powered generation with pre-selected components, targeting distinct visual styles while maintaining quality standards. Key deliverables include mobile gallery optimization (preview at top, sticky CTA bar), prompt-box integration for template remixing, and a component database categorized by style (professional, playful, minimal) with fonts, colors, and hero images to feed the generation pipeline.

---

## Context

Lovable is GrowthX's website template and builder client. The engagement started with GrowthX designing and delivering a custom website experience and initial template set that Lovable has now approved and deployed. This check-in focuses on expanding the template library and improving the gallery interface to drive user engagement and conversions. The team is moving from a manual template design phase into productization — building automated systems to generate templates at scale while maintaining quality standards. Lovable is positioned as a key reference customer for this new template generation capability.

---

## Relevance

**To GrowthX Delivery:**
- Template pipeline with AI-powered generation is now a core deliverable capability; documented and ready to share with Flow team
- Mobile-first design requirement confirmed: preview at top, sticky CTA elements critical for gallery conversion
- Component database approach (categorized by style: professional, playful, minimal) is scalable pattern for template customization
- Guides PR workflow established with Lovable team; reviews and merges proceeding smoothly

**To CheckThat:**
- Template generation pipeline requires prompt optimization and testing in Atlas; CheckThat visibility strategies may inform prompt engineering for landing-page demos
- AI quality control and prompt consistency across diverse template styles is a live use case

**To GrowthX Business Development:**
- Lovable is confirmed as happy customer and reference for website template services
- Expansion opportunity: template generation pipeline positions GrowthX to scale template delivery across multiple customers
- Deliverables (2-3 landing-page demo templates) due this cycle to validate pipeline output quality

---

## Overview

- Lovable approved the experience and templates; they're a happy customer
- Focus on diversifying blog templates while maintaining quality threshold
- Developing a pipeline for generating high-quality, diverse templates using AI and pre-selected components
- Gallery improvements needed: mobile optimization, sticky elements for conversion

---

## Key Topics

### Project Status Update

  - Lovable has approved the experience and templates
  - Team is working on productizing the gallery
  - PRs for guides are open and ready for review
  - Pipeline for template production is being developed

### Template Generation Strategy

  - Aim to diversify blog templates while maintaining quality
  - Develop a pipeline using AI to generate templates based on pre-selected components
  - Focus on creating distinct styles with tasteful output
  - Use Daniel's prompt as a starting point, but modify for Lovable's needs
  - Create a database of components (headers, fonts, colors) categorized by style (e.g., professional, playful)

### Gallery Improvements

  - Mobile optimization needed: preview should be at the top
  - Add sticky elements for better conversion (e.g., CTA bar at the top when scrolling)
  - Consider adding a prompt box for remixing templates directly in the gallery view

### AI-Powered Template Generation

  - Utilize Daniel's pipeline for generating brand concepts and mock data
  - Develop a system to select appropriate fonts, components, and styles based on the generated brand personality
  - Start with landing pages, then expand to other template types
  - Aim to demo high-quality templates by Wednesday

### Workflow and Tools

  - Use 21st.dev for inspiration and pre-made components
  - Explore Cloud browser extension for AI-assisted browsing
  - Balance between using AI for code generation and maintaining code quality standards

---

## Action Items

**Nicolas Castellanos (GrowthX)**
- Ping Lovable team re: Guides PRs; request reviews/merges
- Send template pipeline to Flow; start prompt-gen in Atlas; test micro-apps; deliver 2–3 landing-page demos
- Implement prompt-box in gallery embed; push to branch

**Georgemaine Lourens (GrowthX)**
- Finish gallery mobile fixes (preview top, sticky CTA); send updated link to George
- Curate 21st Dev heroes; share w/ Nico; then Nico categorize + integrate font/hero selection

---

## Transcript
**Georgemaine Lourens:** It's the weekend, and Lovable has approved the experience and the templates, and they're a happy customer.

**Georgemaine Lourens:** So, all good here.

**Georgemaine Lourens:** How are you?

**George Haikal:** Let's go.

**George Haikal:** I feel good as well.

**George Haikal:** Do you have any fun plans for the weekend?

**Georgemaine Lourens:** I believe I have to book a stay away, or however it's called, to Paris at the end of November with my partner.

**Georgemaine Lourens:** So that's going to be fun.

**Georgemaine Lourens:** It's going to be like Friday to Monday, because we've been together for 10 years at the end of this year.

**George Haikal:** Anniversary?

**George Haikal:** 10-year anniversary?

**Georgemaine Lourens:** Yeah, it is.

**Georgemaine Lourens:** But it's not the anniversary that you think it is.

**Georgemaine Lourens:** So, funny story.

**Georgemaine Lourens:** When me and my partner met on Tinder, and the first time that we met, she ghosted me on Facebook.

**Georgemaine Lourens:** She just gave me her Facebook, but ghosted me.

**Georgemaine Lourens:** So, at the end of this year,

**Georgemaine Lourens:** The year is going to be 10 years ago that she ghosted me.

**Georgemaine Lourens:** That's funny.

**Georgemaine Lourens:** And in January is going to be the official, official 10 years.

**George Haikal:** That's awesome.

**George Haikal:** Hey, you know, if you know, you know, right?

**George Haikal:** Persistence pays off.

**Georgemaine Lourens:** Exactly.

**George Haikal:** Just kept being nice about it, but showing her you cared.

**Georgemaine Lourens:** Exactly.

**Georgemaine Lourens:** How about you?

**Georgemaine Lourens:** Do you have any fun plans?

**George Haikal:** This weekend, no, I think just honestly catching up on some sleep and some rest.

**George Haikal:** That'll be nice.

**George Haikal:** Last weekend, I had like friends over in a housewarming, and so it hasn't been like a restful past couple weekends.

**George Haikal:** So this one, I'm looking forward to just, oh, I'm actually getting a sauna in, whatever, today.

**George Haikal:** And so now I have Cold Plunge right next to my sauna, and so I'll have this amazing, like, thing I can do every day.

**Georgemaine Lourens:** I'm excited for

**Georgemaine Lourens:** Ah, that's nice.

**Georgemaine Lourens:** I want to try that, the cold plunge.

**Georgemaine Lourens:** I've heard good things about it, but I've never tried it.

**George Haikal:** It's really good.

**George Haikal:** It's painful every single time, but you feel so good after, mental clarity-wise, and also inflammation, boosting metabolism, all that.

**George Haikal:** like no matter how tired you are when you wake up, you get in that cold plunge for two minutes, and you feel better.

**George Haikal:** You feel better.

**Georgemaine Lourens:** Yeah, I can imagine.

**George Haikal:** Hey, Nicolas.

**George Haikal:** What's up, Nico?

**George Haikal:** How are you doing, man?

**George Haikal:** Any big plans for the weekend, Nico?

**Nicolas Castellanos:** Yeah, I have like three, four hours of flight lessons this weekend.

**Nicolas Castellanos:** So, yeah, it's going to be nice.

**Nicolas Castellanos:** Yeah, I'm flying to Colonia and back.

**Nicolas Castellanos:** It's like, I don't know, maybe 150 miles, like each way.

**George Haikal:** It's going to be like, I don't know, two and a half hours maybe, or three of flying.

**George Haikal:** way?

**George Haikal:** Or one and a half?

**Nicolas Castellanos:** Each way.

**Nicolas Castellanos:** Yeah, each way.

**Nicolas Castellanos:** Each like go.

**Nicolas Castellanos:** Oh, and back.

**Nicolas Castellanos:** It will be, I don't know, maybe 300 miles.

**George Haikal:** It's just you and a pilot, like pilot and a passenger.

**Nicolas Castellanos:** Is it a two-seater plane?

**Nicolas Castellanos:** Yeah, I am the pilot.

**Nicolas Castellanos:** And then on my right, there's going be my instructor.

**George Haikal:** Do they have controls too in front of them?

**Nicolas Castellanos:** Or how does it work?

**Nicolas Castellanos:** Yeah, they do.

**Nicolas Castellanos:** They do have like the same controls I have.

**Nicolas Castellanos:** There is like throttle and other inputs in the middle.

**George Haikal:** Do they have to intervene at all when you're doing it?

**Nicolas Castellanos:** Or like, you at a spot now where you kind of...

**Nicolas Castellanos:** Usually not, unless something like super weird happens.

**Nicolas Castellanos:** What they usually do, like, I don't think that's going to happen for like the navigation to there.

**Nicolas Castellanos:** But when I do like round trips around the airport, what they usually do is, hey, you go without power, like engine installed, and they like turn off the throttle, everything, to simulate an engine loss.

**Nicolas Castellanos:** And you need to handle the situation and be able to come without the engine.

**Nicolas Castellanos:** It's great.

**Georgemaine Lourens:** It's great, he says.

**Nicolas Castellanos:** I mean, they don't stall the engine, just simulation, like, without throttle, to simulate as if the engine was stall.

**George Haikal:** What's your goal?

**George Haikal:** Like, when's your goal to fly alone?

**George Haikal:** I'm assuming your goal is to, like, be able to pilot alone.

**Nicolas Castellanos:** Yeah, being able to basically fly alone, and then also being able to, like, fly bigger airplanes alone.

**Nicolas Castellanos:** So, like, not the commercial ones, because I don't care about those, but maybe, like, a twin engine airplanes and those kind of stuff.

**Nicolas Castellanos:** That would be nice.

**George Haikal:** Is it mainly for, like, you want to be able to travel and go wherever, or is it more, like, just the experience of flying in general?

**Nicolas Castellanos:** No, it's, like, fun.

**George Haikal:** That's awesome, That's so cool.

**George Haikal:** That's so cool.

**Nicolas Castellanos:** Nice.

**George Haikal:** I think this is going to be, like, an easy one.

**Georgemaine Lourens:** Yeah.

**George Haikal:** In terms of things for life.

**George Haikal:** I mean, Georgemaine and I caught up on kind of where we think we're at.

**George Haikal:** Nico, is there anything top of mind for you for Lovable?

**Nicolas Castellanos:** And then we can just run into like where everything's at.

**Nicolas Castellanos:** Yes, I don't know.

**Nicolas Castellanos:** I assume Next Steps is productize the gallery.

**Nicolas Castellanos:** And then I don't know where are we at guides because I got the PRs open.

**Nicolas Castellanos:** They haven't got any reviews, but I haven't asked for them either.

**Nicolas Castellanos:** They should just open in there for anyone to review.

**Nicolas Castellanos:** But I don't know design-wise if we are approved and ready to go, or are we waiting for anything?

**Georgemaine Lourens:** It's fine design-wise.

**Georgemaine Lourens:** I watched a video from Nat, and he basically said like it's not great, but it's their fault because they need to update the design.

**George Haikal:** So I think you're good on the guides.

**George Haikal:** Yeah, so then if we can like ping them on the PRs, like to just merge and approve them, then we'll be good there.

**George Haikal:** And then I guess they'll let us – so then we'll get three articles published, and then we'll stay updated.

**George Haikal:** get three articles we'll

**George Haikal:** On the next five that are in the pipeline, and then once those are done, we'll just have to re-ping them again.

**Nicolas Castellanos:** Yes.

**Nicolas Castellanos:** Cool.

**Nicolas Castellanos:** Cool.

**Nicolas Castellanos:** So, yeah, I'll ping them.

**Nicolas Castellanos:** And then on templates, I got a pipeline that will produce fair enough templates.

**Nicolas Castellanos:** So we'll be sending that to Flow today, because right now it's a separate code base.

**Nicolas Castellanos:** Georgemaine, I applied the feedback you gave me yesterday.

**Nicolas Castellanos:** It's good now.

**Nicolas Castellanos:** I removed the discovery I was doing on 21st Dev, because you were always discovering the same templates.

**Nicolas Castellanos:** For that, I think we will need to basically make, I don't know, the same thing you gave me for fonts.

**Nicolas Castellanos:** Do it for components.

**Nicolas Castellanos:** So we can't give it strict components to use, instead of just letting go on discovery.

**Nicolas Castellanos:** Because it was...

**Nicolas Castellanos:** Flow is discovering the same stuff.

**Nicolas Castellanos:** So it doesn't make sense.

**Georgemaine Lourens:** Yeah, I think that pipeline still needs some work.

**Georgemaine Lourens:** But I think if we connected to Flow, it will be a lot better because we can use the artifacts and kind of like make it better.

**Nicolas Castellanos:** I saw today you generated a perspective template.

**Nicolas Castellanos:** How did you get the prompt for that one?

**Nicolas Castellanos:** Because I used that into my pipeline and got this one.

**Georgemaine Lourens:** Yeah, sorry, George, I didn't want to derail the convo.

**Georgemaine Lourens:** But what I did is I used Daniel's prompt for Bolt.

**Georgemaine Lourens:** And I started tweaking it a little bit because I wanted to try out a hypothesis that I had for like diversifying all of the styles without overkilling it.

**Georgemaine Lourens:** I'll show it to you on Monday because there's some stuff that I want to do this weekend to make sure that it runs well.

**Georgemaine Lourens:** But basically, I

**Georgemaine Lourens:** I just want to make a couple of components and then kind of like get like a feel and have AI fill in the field, but also the contents, the generates the right sections instead of just going wild and doing whatever.

**Georgemaine Lourens:** So, but it's going to be easier to see when I just demo it to you and sort of just talking out loud.

**Nicolas Castellanos:** Cool.

**Georgemaine Lourens:** So, yeah, but I think like the two things that are top of mind for me is kind of like being able to prove to Sebastian that we can diversify the blog templates, but also still meet a quality threshold.

**Georgemaine Lourens:** And I think, Nico, I'll be done with, I think I'm almost done with all of the fixes for the gallery.

**Georgemaine Lourens:** And I think afterwards you kind of need to do a pass so that it's production ready because I've just been like designing with cloud code.

**Georgemaine Lourens:** And I think, yeah.

**Georgemaine Lourens:** It needs to be ready before we really have them review it.

**Georgemaine Lourens:** So I think those are the two things that we probably need to do.

**Georgemaine Lourens:** Those are simple.

**Georgemaine Lourens:** Is there anything else that you're worried about or that's top of mind for you, George, or what is kind of like your next target here for next week?

**George Haikal:** Yeah, there's a few things.

**George Haikal:** So this afternoon I'm finishing up the template strategy because like what Ada and the editorial team deliver just like is not like it's basically just keywords and general categories for templates, but there's no real strategy behind it or one that we can communicate outside of, hey, here's a search volume for like 40 different template categories, but also it's only 40 different template categories, right?

**George Haikal:** Like we want to hit.

**George Haikal:** The long tail of each of the most of the highest intent and largest opportunities of templates.

**George Haikal:** like portfolio websites as a category, having 3000 search volume doesn't help us at all because we want to break out all the different types of portfolio templates that we can make.

**George Haikal:** Right.

**George Haikal:** And so like it's communicate, it's compiling all that and then putting it in Airtable and communicating in a way where it's like, here's the total massive opportunity in the market based on what all of our competitors are doing.

**George Haikal:** Right.

**George Haikal:** I want to narrow it down all the way to like, these are the categories we want to show on the actual template gallery to start with.

**George Haikal:** And so that like what you have is great on the experience, like the icons look great.

**George Haikal:** But I think those categories are going to be.

**George Haikal:** What's the word?

**George Haikal:** Iterated on for sure.

**Georgemaine Lourens:** No, I think that's fair.

**Georgemaine Lourens:** I think that what we have right now for me, like I'm not married to the way it looks or what patterns we use.

**Georgemaine Lourens:** It was just kind of like, can we.

**Georgemaine Lourens:** We get an okay from them so we can move to the next part.

**Georgemaine Lourens:** So, Phil, you have total freedom there.

**George Haikal:** Appreciate it.

**George Haikal:** It's super necessary to get it out and get their approval because now we have it, which is fantastic.

**George Haikal:** But it's more so like people are coming to build apps, build dashboards, like B2B SaaS as a category, while it's like maybe a keyword that has search volume, like it's not going to resonate that much or as much with people or Lovable's users specifically.

**George Haikal:** so we can simplify that a bit and that's – I'll make sure to do that.

**George Haikal:** But all good things, right?

**George Haikal:** It's not going to add too much work either.

**Georgemaine Lourens:** No, but kind of like where is your head at in terms of like what we're going to create?

**Georgemaine Lourens:** Because I feel like on the one hand, like portfolio websites is very designery, but also very tied to a CMS and kind of like putting content in there.

**Georgemaine Lourens:** And it kind of feels like Lovable is more of a thing for people that want the vibe code or just kind of like

**Georgemaine Lourens:** Like, figure out how an idea should work.

**Georgemaine Lourens:** So should it be more on the components slash microapp side or more of the full-on templates?

**George Haikal:** You're spot on.

**George Haikal:** Yeah, it's going to be both.

**George Haikal:** I think just we wanted to start with portfolio templates to get their bar for quality, honestly, because it was the easier lift for us to actually execute on, right?

**George Haikal:** And then we communicate to them that we're not going to, like, be building fully functional apps or app templates, right?

**George Haikal:** But the micro tools, the micro apps, like, that's all definitely part of the strategy.

**George Haikal:** And, like, once I finish it this afternoon, we'll understand, okay, what is the next category we want to go into and start building for?

**George Haikal:** But there is a ton of traffic for the websites piece as well.

**George Haikal:** So, like, it is easier lift and there is a good amount of traffic to capture, like, all the Wix's of the world and other competitors, like, there's a ton of traffic going there that we can eat.

**George Haikal:** Easily capture for lovable.

**George Haikal:** And then it's about the apps and people coming in and being able to remix them, et cetera.

**George Haikal:** So we're thinking about that as well.

**George Haikal:** Like probably next week we'll have a better direction on what we actually want to start building as like the next set of templates.

**George Haikal:** Right.

**George Haikal:** Because then obviously it's easier said than done because then we need to create workflows that help produce them and all that.

**George Haikal:** So I guess, Nico, how, so like, just to help me understand if today I said, like, how long would it take to have, you know, a workflow that can produce micro apps, like different, like calculator micro apps to calculate.

**Nicolas Castellanos:** Like how much functionality, like micro apps need to have, like a backend for example.

**Nicolas Castellanos:** Do they need, like, AI connection?

**Nicolas Castellanos:** Like, what are the kind of features we're thinking about to build there?

**Nicolas Castellanos:** Because one, right now, it's not, it's going to build the functionality, but on its own.

**Nicolas Castellanos:** What I was thinking as a strategy to build those kind of, like, more complex use cases is to maybe, like, buy code and hand build a couple templates of how to use, like, the lovable cloud, the AI gateway they are talking about, and then have the pipeline to use that as a base, so it doesn't need to go crazy and build something that end up being super buggy.

**Nicolas Castellanos:** I don't know if that makes sense.

**Georgemaine Lourens:** It does make sense.

**Georgemaine Lourens:** Yeah, it does.

**Nicolas Castellanos:** Unless we're thinking micro apps as, like, just the UI, I'm not the, the, the actual, I mean, ideally, like, the more it can do, the better, but I.

**George Haikal:** Also want, like, there's a trade-off.

**George Haikal:** Like, the more it can do, the longer it'll take for us to make, and the harder it will be.

**George Haikal:** And so, like, understanding what we're trading off is going to be important and what we want.

**George Haikal:** Like, it doesn't need to be the best working app ever.

**George Haikal:** It just needs to be good enough, and we need to get their team's approval for it, and then create them programmatically.

**George Haikal:** So, more so, whatever you're...

**Nicolas Castellanos:** I think for super simple micro-apps, I don't know, a QR generator, that's super easy for the AI to do.

**Nicolas Castellanos:** If we want to add some, like, AI use cases to those, that's when it might be helpful to have, like, a base for the AI.

**Georgemaine Lourens:** Here are some examples from the doc that Sebastian shared with us.

**Georgemaine Lourens:** Yep.

**Georgemaine Lourens:** And I think, like, these are the types of things that we probably should be able to do, right?

**George Haikal:** I mean, password generator, kind of, like, mind maps, flowcharts.

**Nicolas Castellanos:** Yeah, I think we can...

**Nicolas Castellanos:** can build those super easy.

**Nicolas Castellanos:** The question is how much ready for production they need to be.

**Nicolas Castellanos:** Like, do we need user login, registration, and those kind of stuff?

**Nicolas Castellanos:** I we should stay away from that.

**Georgemaine Lourens:** I think we should stay away from that.

**Georgemaine Lourens:** I think, like, their use case is kind of like proving a thesis, kind of like, okay, I'm working in a product team, and we need to, I want to push for getting this on the road map, and let me just kind of, like, vibe code it and show it to you.

**Georgemaine Lourens:** Or maybe some kind of, like, solopreneur who is just trying to get a business up or trying something out.

**Georgemaine Lourens:** think kind of, like, in that area, I think you'll get stuck if we try to get, like, user authentication in it.

**Georgemaine Lourens:** And it's, like, that was my thinking, too.

**Nicolas Castellanos:** Yeah, it's just something that works.

**Georgemaine Lourens:** And that's it.

**Nicolas Castellanos:** Yep.

**Georgemaine Lourens:** I'm not sure how good Lovable works with ChatCN, so we might have to...

**Nicolas Castellanos:** Oh, it does work with, I mean, it has some components pre-installed.

**Nicolas Castellanos:** When you set up a project in Lovable, it will pre-install ChatCN and Tailwind.

**Nicolas Castellanos:** So it does a good job using ChatCN.

**Nicolas Castellanos:** It's part of the stack.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** That's good to hear.

**George Haikal:** Okay, so then what are the questions you need to answer there, Nico, if any?

**Nicolas Castellanos:** No, I guess I got the answer, which is just have those microapps to work and not worry about being production-ready in the terms of being available for other users to use your microapp.

**Nicolas Castellanos:** Just we need to build something that you as a user can replicate and use for yourself, and that's it.

**George Haikal:** Yeah, that makes sense.

**George Haikal:** Cool.

**George Haikal:** All right.

**George Haikal:** Cool.

**George Haikal:** Yeah, that makes sense.

**George Haikal:** That makes sense.

**George Haikal:** And then the last thing that I'm doing this week and then weekend is setting up their AI visibility dashboard.

**George Haikal:** Daniel did a bunch of work on like the check that category for basically AI coding for non coders and like a bunch of prompts there.

**George Haikal:** So I'm pulling those in and then building out their scrunch.

**George Haikal:** Because now we can, once we get articles published, we need to make sure they get indexed.

**George Haikal:** And then we need start seeing what signals we're getting on them, both in terms of like impressions, clicks, etc.

**George Haikal:** But also the AI visibility, citations, mentions, brand perception, all that.

**George Haikal:** So setting that up so we'll be able to track it once these articles go live.

**Georgemaine Lourens:** Okay, nice.

**Georgemaine Lourens:** Did you guys make any, did you guys set any dates yet or when the first template needs to be published?

**George Haikal:** No.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** All right.

**Nicolas Castellanos:** And I'm sorry.

**Georgemaine Lourens:** Okay.

**Nicolas Castellanos:** Then SEO-wise, do we have, like, a clear strategy for the templates?

**George Haikal:** For the templates?

**George Haikal:** Yeah.

**George Haikal:** I'm finishing out this afternoon.

**Nicolas Castellanos:** Great.

**George Haikal:** Yeah.

**George Haikal:** Yeah.

**George Haikal:** So we will.

**George Haikal:** Cool.

**George Haikal:** We're basically, mean, in my head, right?

**George Haikal:** We're in a good spot.

**George Haikal:** We're not blocked at all.

**George Haikal:** We got the design approval we need for everything.

**George Haikal:** And it's kind of on us to productize the gallery experience.

**George Haikal:** I'll work on the template strategy, the AEO visibility stuff.

**George Haikal:** Yeah.

**George Haikal:** I don't think we're missing anything, right?

**Georgemaine Lourens:** No.

**Georgemaine Lourens:** No.

**Georgemaine Lourens:** I think my only other question is slightly off topic, but when is, like, we work in the sprint, right?

**Georgemaine Lourens:** And I'm guessing we're nearing the end of the sprint.

**George Haikal:** Here's the sprint.

**George Haikal:** Three more weeks.

**Georgemaine Lourens:** Three more weeks.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** When is their renewal or their commitment period?

**George Haikal:** Yeah, at the end of eight weeks, every client can opt in or out.

**George Haikal:** It's a mutual opt-out on our end and their end.

**George Haikal:** So they can market when they would convert to the annual contract.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** So next week is kind of like the moment of truth.

**George Haikal:** Yeah, just got to get publishing and then, well, like, yes, we're putting this pressure on ourselves, which is good.

**George Haikal:** We should, but they love us.

**George Haikal:** As of now, like Marcel was with their CEO yesterday.

**George Haikal:** They got invited to like vibe code, some stuff with them.

**George Haikal:** Their team is like back channeling us, saying like how happy they are.

**George Haikal:** so now it's about let's get to publishing and let's track the signals and let's double down on what's working.

**George Haikal:** Like a cadence of volume that we're comfortable with.

**George Haikal:** then obviously I want to give you all the time back coming out of the sprint, right?

**George Haikal:** So set.

**George Haikal:** The workflows in a way where someone else can step in and take over and where it's not taking all of your time.

**George Haikal:** But right now it's the setup period, right?

**George Haikal:** That's why it's just taking a lot.

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** All right.

**Georgemaine Lourens:** Cool.

**Georgemaine Lourens:** All right.

**Georgemaine Lourens:** Yeah, I guess that's all for me.

**Georgemaine Lourens:** I'll make sure that you have a new link with the changes that an ad requested so you can share that if you want.

**Georgemaine Lourens:** Yeah.

**Nicolas Castellanos:** Yeah, I'll ping the team to review those PRs.

**Nicolas Castellanos:** And then, Georgemaine, if you have like 10 minutes to sync on the pipeline, show you the latest results I got.

**Nicolas Castellanos:** George, you're free to stay if you want to.

**Nicolas Castellanos:** Sure.

**Georgemaine Lourens:** I'll stick around.

**Nicolas Castellanos:** Cool.

**George Haikal:** Sweet.

**George Haikal:** Thanks, guys.

**George Haikal:** Hit me up with anything that comes up.

**Georgemaine Lourens:** Appreciate the help.

**Georgemaine Lourens:** Cool.

**Georgemaine Lourens:** Ciao.

**Georgemaine Lourens:** Have a good weekend.

**George Haikal:** Me too.

**George Haikal:** Bye.

**Georgemaine Lourens:** Okay.

**Nicolas Castellanos:** So I saw, I applied the feedback this morning.

**Nicolas Castellanos:** And when I was at it, I saw you created this.

**Nicolas Castellanos:** And I think this is the one that you were saying that got the idea from Bolt and tweaked it.

**Nicolas Castellanos:** So I basically copied your prompt, which looked great.

**Nicolas Castellanos:** And put it into my pipeline.

**Nicolas Castellanos:** And I got this one.

**Georgemaine Lourens:** Oh.

**Georgemaine Lourens:** Yeah, it's a bit basic on the branding side.

**Georgemaine Lourens:** But it's good.

**Georgemaine Lourens:** It just lacks a brand.

**Nicolas Castellanos:** It just lacks kind of...

**Nicolas Castellanos:** I think we can tweak that with that initial prompt.

**Nicolas Castellanos:** Because I think we're adding so much value here is that initial prompt.

**Nicolas Castellanos:** So if we have a great prompt to start with, then the pipeline can direct Lovable to do good things.

**Nicolas Castellanos:** Like we can add branding, components to use, fonts, whatever we need to that initial prompt.

**Nicolas Castellanos:** And then Lovable, the pipeline that talks to Lovable will just help Lovable build that.

**Georgemaine Lourens:** Yeah, yeah.

**Georgemaine Lourens:** So, yeah, I think you're right.

**Georgemaine Lourens:** I think like the way that I understood it from Daniel is that the prompt, it needs a couple of things to be really good.

**Georgemaine Lourens:** One is it needs clear directions on the sections that we need, like the header, the introduction, the featured article, a newsletter thing, like it needs that.

**Georgemaine Lourens:** But the.

**Georgemaine Lourens:** But it also needs mock data, right?

**Georgemaine Lourens:** Because then it can populate it and then it won't go wild and come up with a thousand different things.

**Georgemaine Lourens:** So that's very important.

**Georgemaine Lourens:** But I think the other part is also having components included into the prompt.

**Georgemaine Lourens:** And that's kind of like my thing that I was trying to figure out.

**Georgemaine Lourens:** Like, can I come up with different components?

**Georgemaine Lourens:** For example, like you have the newsletter, the stats here, which is great.

**Georgemaine Lourens:** But I think we need like some more standard ones.

**Georgemaine Lourens:** Yeah, I saw these.

**Nicolas Castellanos:** And also I want to try like have like a manual look to all these.

**Nicolas Castellanos:** Like have a list of, I don't know, 20 of these.

**Nicolas Castellanos:** And then have this into a prompt so we can tell the prompt, like, I don't know.

**Nicolas Castellanos:** I don't know.

**Nicolas Castellanos:** like, So, So, So, I

**Nicolas Castellanos:** Build this, use this component for a hero, use this for, I don't know, the cards, and all those directions, like, they're super, like, clear on, like, even how it should look and how the code should look.

**Nicolas Castellanos:** And if we can build that into that prompt, then the pipeline will take care of, like, helping lovable do things step by step.

**Nicolas Castellanos:** Because what the pipeline is doing here, it's just helping lovable do things step by step versus just lovable trying to do all at once.

**Georgemaine Lourens:** That's good.

**Georgemaine Lourens:** I think that's good.

**Georgemaine Lourens:** I think the workflow that the pipeline has is really good in terms of, like, being able to talk to each other.

**Georgemaine Lourens:** think we just need to be very, I think we need to be more strict about what we tell lovable to do, and I'm trying to figure that part out.

**Georgemaine Lourens:** Because I think in an ideal world, we just let it iterate.

**Georgemaine Lourens:** We, you give them five hero sections and there are, we tell them specifically to be creative on how it styles those, right?

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** And I think there's so much freedom that we can do there.

**Georgemaine Lourens:** Like we have like, we could focus on image background overlays.

**Georgemaine Lourens:** We could focus on video background overlays, large text and shapes and all of that.

**Georgemaine Lourens:** Like I feel like that's kind of like the thing.

**Georgemaine Lourens:** But I need to prove that thesis first.

**Georgemaine Lourens:** And obviously in the end, like someone needs to just say like, hey, we're going to talk about this topic or we're going to focus on this keyword.

**Georgemaine Lourens:** And for that, you need to come up with a whole use case with the text.

**Georgemaine Lourens:** And I think our pipeline should also kind of like generate that and have it be meaningful.

**Georgemaine Lourens:** And that's what Daniel's pipeline already does.

**Georgemaine Lourens:** Like it, it came up with like.

**Georgemaine Lourens:** It's a lifestyle and travel blog or like perspective that gives you the mock content.

**Georgemaine Lourens:** So I think that's something that I want to figure out.

**Georgemaine Lourens:** And yeah, I can take a look at the 21st dev, but I also want to make sure that like the page structure is good.

**Georgemaine Lourens:** But I think 21st dev is more focused on like cool interactions and some assets, although I do think the shaders are very useful.

**Georgemaine Lourens:** I think those can be pretty cool.

**Georgemaine Lourens:** So, yeah, let me try out some stuff this weekend for fun.

**Georgemaine Lourens:** But in my ideal world, we will end up with a database with a couple of, let me think about it.

**Georgemaine Lourens:** But I think like we should have like a pipe.

**Georgemaine Lourens:** Line that's running for block template, and it has access to some components that we wrote.

**Georgemaine Lourens:** Yes.

**Georgemaine Lourens:** And then you just give it like a use case, and then it spits out a brand and talks to Lovable and kind of like styling that and making it unique.

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** High quality and making sure that like, hey, there are no bugs and all of that.

**Georgemaine Lourens:** And you can also give it, you should also be able to give it an image so they can interpret the personality and kind of like the color palette from that and then use that to style it.

**Georgemaine Lourens:** And if we don't, then it just does its own thing.

**Georgemaine Lourens:** I think that's kind of like how I picture this working.

**Nicolas Castellanos:** Yeah, I think that's it.

**Georgemaine Lourens:** But bear with me because this is also like my first time doing this.

**Nicolas Castellanos:** So, I'm also just kind of like figuring this out.

**Georgemaine Lourens:** It's not an easy problem.

**Georgemaine Lourens:** No, it's different.

**Georgemaine Lourens:** what I'm doing.

**Nicolas Castellanos:** But I think we have, I mean, it's not an easy problem, but it's also, I think, that piece, again, I think it's the piece we as a company are good at, which is generating the content.

**Georgemaine Lourens:** Yeah.

**Nicolas Castellanos:** So, yeah, I think that's the way, and I feel like we need to build that, like, basically tweak Daniel's pipeline, the one that he built for Vault, tweak into what you are describing, and then use the output of it into this other pipeline to just let Lovable do the work.

**Georgemaine Lourens:** Yeah, I think that could work, because Daniel's prompts work really well, like, they still work really well.

**Nicolas Castellanos:** Yeah, I mean, this is great for, like, a one-shot.

**Georgemaine Lourens:** Yeah, this is everything you kind of need, right?

**Georgemaine Lourens:** It has.

**Nicolas Castellanos:** Oh, I saw this is amazing.

**Georgemaine Lourens:** Yeah, I think the only thing that it kind of needs is styling and some creativity and maybe some more components because functionality-wise, it's very simple.

**Georgemaine Lourens:** But the way that I look at this prompt is quite straightforward.

**Georgemaine Lourens:** It's kind of like, here are the sections, here is the thing, the company and the brand that we're making content for.

**Georgemaine Lourens:** Here are the sections that we need, the requirements.

**Georgemaine Lourens:** Here are some mock data for it.

**Georgemaine Lourens:** And then at the end, there's kind of like a whole design system for Tailwind.

**Georgemaine Lourens:** Like, that's super clear and not difficult at all.

**Georgemaine Lourens:** So I think we should be able to do it.

**Georgemaine Lourens:** The only thing that I kind of want to try out is like, how can we give them design system options, some building blocks, right?

**Georgemaine Lourens:** Because I think like a header, we should have like five headers that we can iterate between because people figured that.

**Nicolas Castellanos:** Yeah.

**Nicolas Castellanos:** Yup.

**Nicolas Castellanos:** Yup.

**Nicolas Castellanos:** That's how like, instead of like the five headers have like a recipe per type of template we're building.

**Georgemaine Lourens:** What do you mean by recipe?

**Nicolas Castellanos:** Like, I don't know if you are built like four blogs, you, you can use, uh, these fonts based on like the, feeling and the topic, uh, this header, uh, these components for the cards, this, uh, uh, I don't know, this hero, like for a blog, maybe a video on the hero doesn't make sense, for example.

**Nicolas Castellanos:** Yeah.

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** I think that's the way to go because that, that's kind of what I liked about a Squarespace.

**Georgemaine Lourens:** Like what they do upfront is they ask you what your use cases, um, and then they.

**Georgemaine Lourens:** Kind of like going to what you're trying to achieve and trying to get like your brand personality.

**Georgemaine Lourens:** Like, are you professional or are you playful or are you kind of like very bold, right?

**Georgemaine Lourens:** And if once you have that, you can kind of like match all of those components to that.

**Georgemaine Lourens:** For example, like if you're bold, like I can obviously imagine that maybe you kind of want to get like large type or a certain tone of language in the components, but also like bold to me is kind of like throw in some videos and it's immersive, like stuff like that.

**Nicolas Castellanos:** something that e-bugs, yeah.

**Georgemaine Lourens:** So ideally we generate the brand personality or a personality based on the keyword and the use case.

**Georgemaine Lourens:** And once we have that, we're able to kind of like narrow down the components that we can use and kind of like pick if we can label them a little bit.

**Georgemaine Lourens:** Like I try.

**Georgemaine Lourens:** I tried doing that with the fonts, but it became overkill, became like such a large document.

**Georgemaine Lourens:** Like it should be simpler than that.

**Georgemaine Lourens:** Like maybe it should just have tags.

**Nicolas Castellanos:** Yeah.

**Nicolas Castellanos:** And I'm using your doc in here for the fonts.

**Nicolas Castellanos:** The interesting thing is, and it might be because all these are like blogs or newsletters, but I think it's always trying the same fonts.

**Nicolas Castellanos:** But that's probably because the feeling of what I'm trying to build is always the same.

**Georgemaine Lourens:** It's like a newsletter.

**Georgemaine Lourens:** Yeah, well, maybe that's an interesting starting point for you.

**Georgemaine Lourens:** Like can you take the concept slash brand generation from Daniel's pipeline?

**Georgemaine Lourens:** Can you take that piece and then feed it to your pipeline and then have it pick the right font pairing or font based on the stuff that you feed it?

**Georgemaine Lourens:** Maybe that's a good starting point.

**Georgemaine Lourens:** Maybe that's that...

**Georgemaine Lourens:** Where you can already have the picking and the personality piece nailed down.

**Georgemaine Lourens:** And once you figure that out, then it's easy peasy because then we have the system and then we just need to extend it to different components.

**Georgemaine Lourens:** Maybe that's something that you can already try and figure out because it's really good what he does.

**Georgemaine Lourens:** Like he already has the name for the template.

**Nicolas Castellanos:** He has a description.

**Georgemaine Lourens:** it's great.

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** So it's good.

**Nicolas Castellanos:** Yeah.

**Nicolas Castellanos:** What I want to, I mean, the only thing I don't like about that pipeline is, and that works for, I think that works for Bolt, but it doesn't work quite well for Lovable.

**Nicolas Castellanos:** Are the directions on like styles and fonts and tailwind classes that it's giving it.

**Nicolas Castellanos:** Yeah.

**Georgemaine Lourens:** I don't think you need.

**Georgemaine Lourens:** Yeah, I'm correct.

**Georgemaine Lourens:** I agree with that.

**Georgemaine Lourens:** with I agree

**Georgemaine Lourens:** I feel like the prompts that he has on Notion are better than the prompts that he got from the pipeline.

**Georgemaine Lourens:** But I think the concepts, like, I think those are really good.

**Georgemaine Lourens:** And maybe you can just leave out the other stuff and just kind of, like, if you could figure out a way to get all of the mock data and just have to pick the right font, then that will be a simple, simple, simple mini workflow that you could create and then you can add it in.

**Georgemaine Lourens:** But I 100% agree that, like, the styles and all of that, that isn't good in this workflow.

**Georgemaine Lourens:** But I think if we could be able to pick the right fonts based on the concept that he, the brand that he spits out, then we'll be in a great spot.

**Georgemaine Lourens:** because

**Georgemaine Lourens:** Then we just need to move to components and styling.

**Nicolas Castellanos:** Yeah.

**Georgemaine Lourens:** But it also needs to be based on the personas that we have, and all of that stuff lives in Outlast.

**Nicolas Castellanos:** Yeah, no, that's, I think that's the easiest thing.

**Nicolas Castellanos:** I might try playing a little bit with Cloud projects to see if I can have like a chat in there that will, that will give me this, what we're, this we're talking about.

**Nicolas Castellanos:** And then I'll move it into, I'll move it into Cloud.

**Nicolas Castellanos:** But yeah.

**Georgemaine Lourens:** Let me, let me show you something.

**Georgemaine Lourens:** This was something very rough that I, it's like my own little document that I started writing for myself.

**Georgemaine Lourens:** But when, when Sebastian said like, hey, I like the templates.

**Georgemaine Lourens:** But that's just proof that we can kind of like diversify this into distinct styles with tasteful output.

**Georgemaine Lourens:** I started kind of like breaking it down for myself, like what does that mean, right?

**Georgemaine Lourens:** So I think like diversify means you make different things.

**Georgemaine Lourens:** And I think that different things are powered by components.

**Georgemaine Lourens:** It's done, but also kind of like the assets, right?

**Georgemaine Lourens:** And for example, and that's when I started kind of like finding like high quality assets, for example, this.

**Nicolas Castellanos:** This is kind of like.

**Georgemaine Lourens:** I'm not sharing.

**Georgemaine Lourens:** But for videos, this is good stuff, right?

**Nicolas Castellanos:** Like if you have like an ocean background.

**Georgemaine Lourens:** I'm So I'm not sharing.

**Georgemaine Lourens:** Oh, let me try again.

**Georgemaine Lourens:** Christina?

**Nicolas Castellanos:** Yes.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** So I started out with this document.

**Georgemaine Lourens:** This is what Sebastian said, like, can you make it different, but also very good.

**Georgemaine Lourens:** Just starting to think about what does that mean?

**Georgemaine Lourens:** How do you make things different on the website?

**Georgemaine Lourens:** Like the components is one thing, but also the assets, like the images, the videos, the fonts, but also like the site styles.

**Georgemaine Lourens:** And I think another thing is also kind of like looking at how, like making sure that the quality is high.

**Georgemaine Lourens:** That's also another piece.

**Georgemaine Lourens:** I looked at, for example, like what, I think this might be interesting for you right now.

**Georgemaine Lourens:** I looked at what Framer, like I've been friends with him for like 10 years, so I can pick his brain on this.

**Georgemaine Lourens:** But these are kind of like the guidelines that they use to make sure that their templates are high quality.

**Georgemaine Lourens:** I feel like this should be a step in our workflow, where we just say like,

**Georgemaine Lourens:** Make sure that everything is unique in interactions and layouts, and of course, make sure it's built around a clear use case.

**Georgemaine Lourens:** What does it mean to make it polished?

**Georgemaine Lourens:** Like, it's keeping styling consistent across all pages.

**Georgemaine Lourens:** It's using sharp and high-quality visuals and consistent text and color styles.

**Nicolas Castellanos:** Those are, like, simple things that we could tell a lot about.

**Nicolas Castellanos:** Yeah, I mean, like, I don't know.

**Nicolas Castellanos:** I don't think it's super broad.

**Nicolas Castellanos:** We might need to, like, put an element on it to make it, like, more descriptive.

**Nicolas Castellanos:** Yeah.

**Nicolas Castellanos:** But, yeah.

**Georgemaine Lourens:** Yeah, but I think, either way, like, I think this kind of stuff was kind of what I was thinking about.

**Georgemaine Lourens:** And that's kind of where I want to play with Daniel's prompt to try these things.

**Nicolas Castellanos:** So, yeah, and I think for, like, this, sorry?

**Nicolas Castellanos:** What I...

**Nicolas Castellanos:** I was thinking for that part of diversifying was, what if we have, I don't know, say 10 proved themes, and for themes, I mean documents that specify what header to use, what heroes, what colors, very strict, build it with this inspiration, this feeling, this way, and then just remix using that.

**Georgemaine Lourens:** Yeah, I think that's a good idea.

**Georgemaine Lourens:** Yeah, that is kind of where I want to go to as well.

**Georgemaine Lourens:** So maybe we can say, like, let's focus on two edges of the spectrum for now, professional and playful, and I'll make sure that I get a list of, like, if you're playful, use these and these and these headers, use these and these and these fonts.

**Georgemaine Lourens:** And use these and these and these colors.

**Georgemaine Lourens:** And maybe here are some good-looking images that you can use unless the user has specified something else.

**Georgemaine Lourens:** And then do the same for professional.

**Georgemaine Lourens:** I think you already have the font, so you can already kind of like start with that.

**Georgemaine Lourens:** But I think like if we can get like page headers for that, then that should be doable.

**Georgemaine Lourens:** I should have that by Monday so we can try that out.

**Georgemaine Lourens:** And the rest should be simple because then afterwards it's just kind of like button style.

**Georgemaine Lourens:** Should they be round or should they be square or should they be rounded?

**Nicolas Castellanos:** Should they be held?

**Nicolas Castellanos:** One thing I hate about Lovable is that it always tries, no matter what you do, it always tries to do those round cards with shades.

**Nicolas Castellanos:** Yeah.

**Nicolas Castellanos:** It's frustrating.

**Georgemaine Lourens:** Yeah, yeah, because but if we if we do that in code and then give it.

**Georgemaine Lourens:** get

**Georgemaine Lourens:** Code, then it will basically just implement that code.

**Georgemaine Lourens:** I think that's the hack.

**Nicolas Castellanos:** course, you use that, yeah.

**Georgemaine Lourens:** But the challenging part will be the styles because, yeah.

**Nicolas Castellanos:** Yeah, I think that's, I think there's where 21st dev can help a lot.

**Nicolas Castellanos:** But if, I haven't, I need to, I still need to try this.

**Nicolas Castellanos:** But I'll try to send this, like the workflow as it is right now to Flow so we can use it on Atlas.

**Nicolas Castellanos:** And start working on this pipeline for generating the prompt.

**Nicolas Castellanos:** And I want to try, like, handpicking components from 21st dev and have the prompt use them and see if it came out, if it can realize.

**Nicolas Castellanos:** I'll send handpicking And I'll from from dev.

**Nicolas Castellanos:** then, like, from dev.

**Nicolas Castellanos:** like, from

**Nicolas Castellanos:** What kind of design are you aiming for using those components?

**Nicolas Castellanos:** Because those components already have everything on them, like styling, feeling, everything.

**Georgemaine Lourens:** Let me have a look, because let's have a look together.

**Nicolas Castellanos:** Maybe we can pick a few good ones.

**Georgemaine Lourens:** Because when I looked, it didn't feel, this is good.

**Georgemaine Lourens:** is kind of like a default header.

**Georgemaine Lourens:** I think this is good too.

**Georgemaine Lourens:** But what I would want is kind of like, I have this header, give me five different versions of it, right?

**Georgemaine Lourens:** Like this is good with like...

**Nicolas Castellanos:** Yeah, that stuff, for example.

**Nicolas Castellanos:** Like say we have like a kind of template that builds those things.

**Nicolas Castellanos:** But that is, good for like a certain given, like I don't know, a micro-opil.

**Nicolas Castellanos:** That does stuff with AI.

**Georgemaine Lourens:** Is this all it has?

**Georgemaine Lourens:** Oh, wait, it has kind of like more, so I can tilt it.

**Nicolas Castellanos:** Yeah, you can even search.

**Georgemaine Lourens:** Well, maybe this is a good place to start.

**Georgemaine Lourens:** Maybe you can just start with like, this is basically a lovable animation.

**Nicolas Castellanos:** Yeah.

**Nicolas Castellanos:** I think if you click on themes, lovable is listed on one of them.

**Nicolas Castellanos:** So, I was taking a look.

**Nicolas Castellanos:** Yeah, one of those is lovable, I think.

**Georgemaine Lourens:** Lovable doesn't even have like a theme.

**Georgemaine Lourens:** They have like badge.

**Nicolas Castellanos:** Maybe it wasn't screens and having themes.

**Georgemaine Lourens:** Yeah, like honestly.

**Georgemaine Lourens:** But this is also like, these themes are good.

**Georgemaine Lourens:** Like maybe we need to, maybe I need to be more open to using this kind of stuff.

**Georgemaine Lourens:** Right.

**Georgemaine Lourens:** Because this is, this is.

**Georgemaine Lourens:** lot of stuff that we can use, right?

**Nicolas Castellanos:** Yeah, I think a good thing about this is that we, we're using this, we don't need the AI to get creative, which kind of doesn't work for a lot of the because you don't always try to do the same kind of stuff.

**Nicolas Castellanos:** Like, we can give it stuff that we can't pick from here, then we don't need it to be created, we just tell it, go build this with this template, this component, this theme, get it done.

**Georgemaine Lourens:** Yeah, okay, I think this one's good.

**Georgemaine Lourens:** It's kind of like a basic header, so we should use this.

**Georgemaine Lourens:** Will it help if I just kind of, like, pick a few that I feel like are really good?

**Nicolas Castellanos:** Yeah, totally.

**Nicolas Castellanos:** Yeah, yeah, that was my plan, but I hadn't had the time.

**Nicolas Castellanos:** I wanted to finish that workflow, and then was going to focus on that initial prompt.

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** I'll do that.

**Georgemaine Lourens:** I'll just pick a lot of these that I feel like are good, and then I'll share them with you.

**Georgemaine Lourens:** And do you want me to give them a feeling, or did you mention that they already had that?

**Nicolas Castellanos:** I think they already have a feeling.

**Nicolas Castellanos:** Like, if you look at the, I mean, not in the prompt, I mean the high feeling on the design.

**Nicolas Castellanos:** Like, you look at it, and you know the feeling.

**Nicolas Castellanos:** That's professional.

**Georgemaine Lourens:** That's, like...

**Georgemaine Lourens:** Yeah, but I think we need to document it.

**Nicolas Castellanos:** So I think we need to be very strict.

**Nicolas Castellanos:** Okay.

**Nicolas Castellanos:** I was thinking to have an AI, like, analyze it and come up with it, but if you think...

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** Like, maybe you can start with doing that, and then just share it with me for review, and then I'll...

**Nicolas Castellanos:** Okay.

**Georgemaine Lourens:** I'll give it some feedback, and then we can go from there.

**Georgemaine Lourens:** But I think this...

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** Yeah, maybe this...

**Georgemaine Lourens:** This will save us some time.

**Georgemaine Lourens:** I'll just pick up a bunch of these, and then I'll share that link with you.

**Georgemaine Lourens:** OK?

**Nicolas Castellanos:** Cool.

**Nicolas Castellanos:** Thanks.

**Nicolas Castellanos:** And then anything you need from me on the stuff you're doing?

**Georgemaine Lourens:** No.

**Georgemaine Lourens:** I think if I just give you a link of all of these heroes, then you can try out if we can kind of, like, pick the right ones based on the brand that we come up with from the pipeline.

**Georgemaine Lourens:** And then we just test until that works, and then we move to the next piece.

**Georgemaine Lourens:** And then the next piece, and then the next piece, and hopefully we'll be able to do a page.

**Nicolas Castellanos:** Yep.

**Georgemaine Lourens:** Cool.

**Georgemaine Lourens:** And then I think if we can demo that by showing a few high-quality templates by Wednesday, then I think we'll be in a great spot.

**Nicolas Castellanos:** Yeah.

**Nicolas Castellanos:** I mean, if we can do that, then we can have the pipeline running 500 templates with no problem.

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** But I think like, to me, it's a bit unclear on what, yeah, I guess George is going to work on the keywords this week, this today.

**Georgemaine Lourens:** But to me, we need to, like, we can't focus on portfolio websites and on landing page.

**Georgemaine Lourens:** Like, we need one.

**Georgemaine Lourens:** Let's start with one, and then move to the next.

**Nicolas Castellanos:** Yeah.

**Nicolas Castellanos:** Yeah, true.

**Nicolas Castellanos:** I mean, having a couple, I think will give us, like, the examples we need to make these, like, scalable.

**Nicolas Castellanos:** And then the way I see it, it's just, we just run it for whatever they want.

**Nicolas Castellanos:** And then, I mean, there's always going to need a manual review process.

**Nicolas Castellanos:** So then, then we can, we can have that review process.

**Georgemaine Lourens:** Yeah.

**Nicolas Castellanos:** We decide what goes and what doesn't.

**Georgemaine Lourens:** Yeah, maybe we just start with the landing pages and then just assume that it's going to be for everything.

**Georgemaine Lourens:** But for now, that's just nil landing pages.

**Nicolas Castellanos:** Yeah, I might try microapps this weekend too, just to make sure the workflow can handle them fine.

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** Let's do that.

**Georgemaine Lourens:** I'll start picking a few out and I'll make a list and then I'll share that doc with you.

**Georgemaine Lourens:** then you can run the categorization over it and then share that with me and then I'll give that a review.

**Nicolas Castellanos:** Awesome.

**Nicolas Castellanos:** And then for the gallery, how...

**Nicolas Castellanos:** And then I'll do that.

**Nicolas Castellanos:** Thank you.

**Nicolas Castellanos:** What else do we need to do there?

**Nicolas Castellanos:** I know you're basically applying all the feedback NAD gave.

**Nicolas Castellanos:** Is there anything else?

**Nicolas Castellanos:** Apart, like, of course, for me to, like, productize it and make it work.

**Georgemaine Lourens:** So the last thing that I'm doing right now is on mobile, it's .

**Georgemaine Lourens:** So this preview should be at the top.

**Georgemaine Lourens:** And it's not.

**Georgemaine Lourens:** So I need to do that.

**Georgemaine Lourens:** And I think another thing that would be great is, like, now when you scroll, like, nothing's sticky.

**Georgemaine Lourens:** So it's hard to kind of, like, convert.

**Nicolas Castellanos:** And I think that will hurt conversion.

**Nicolas Castellanos:** Yeah, maybe that's right.

**Georgemaine Lourens:** Yeah, something that they do really well work for us is whenever you scroll at the top, you kind of get, like, this little bar at the bottom with, like, the CTAs.

**Georgemaine Lourens:** I wouldn't put it at the bottom because I think people might confuse it with...

**Georgemaine Lourens:** It comes like a cookie banner, but I do think like if we have something at the top, then that would be good, but that's a nice tab.

**Nicolas Castellanos:** Do you know what's something I think will be awesome to have here and might help a lot with conversion?

**Nicolas Castellanos:** The prompt box.

**Nicolas Castellanos:** Like, the remix, instead of being a button, being something you can write on.

**Georgemaine Lourens:** Oh, yeah.

**Nicolas Castellanos:** Yeah, you mentioned that.

**Nicolas Castellanos:** That will help a lot because that's powerful because, yeah, maybe you have like a pre-made prompt in there.

**Nicolas Castellanos:** I don't know, make this this other way that you just have the text ready for you to just click or you can edit it and do it your way.

**Georgemaine Lourens:** Yeah, if you can get something in this embed experience, that would be great.

**Nicolas Castellanos:** maybe...

**Nicolas Castellanos:** Oh, how do you mean, what are the pictures?

**Georgemaine Lourens:** So...

**Georgemaine Lourens:** So...

**Georgemaine Lourens:** If we get something, if we can put a chat bar here.

**Nicolas Castellanos:** Okay.

**Georgemaine Lourens:** Yeah, we can do that.

**Nicolas Castellanos:** I think that would make a lot of sense, or maybe it needs to be in between this, but I feel like as soon as you...

**Nicolas Castellanos:** My my only concern with that is hiding part of the page with the prompt, which is sort of, because it's already like a small window.

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** Yeah, maybe it needs to be here.

**Georgemaine Lourens:** I don't know.

**Nicolas Castellanos:** That could also be...

**Nicolas Castellanos:** I actually like the idea of hanging on the embed, because it's more like, it's more inviting to use it.

**Georgemaine Lourens:** It's more engaging, I guess.

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** Let me see what does, what do they do?

**Georgemaine Lourens:** They just do nothing.

**Nicolas Castellanos:** They have like a preview here, and then you pick some stuff.

**Nicolas Castellanos:** Yeah, that's not too engaging.

**Nicolas Castellanos:** Like, it's on the side.

**Nicolas Castellanos:** It's not...

**Nicolas Castellanos:** Like, it doesn't...

**Nicolas Castellanos:** Like, it will, like, I think browse for you and do some stuff, but it doesn't really, I think, it didn't analyze the page the way I wanted.

**Nicolas Castellanos:** What I'm using now, which I got the preview, like, a couple days ago, it's a browser extension for cloud.

**Georgemaine Lourens:** Ah, okay.

**Nicolas Castellanos:** That one is great.

**Georgemaine Lourens:** Yeah, for me, like, I tried it, I like the design, but I'm, I think in the end, for me, I like having my browser on my phone and the browser on my desktop to be in sync and basically be the same.

**Georgemaine Lourens:** And this just isn't it.

**Nicolas Castellanos:** And, yeah, I get the AI part, but on the other end, I'm also kind of like, yeah, I can use cloud code or GPT, so.

**Nicolas Castellanos:** Yeah, I don't know about this, I tried it, didn't like it.

**Georgemaine Lourens:** Yeah, but.

**Georgemaine Lourens:** I like them for inspiration.

**Georgemaine Lourens:** They're doing interesting things.

**Georgemaine Lourens:** I think that's cool.

**Georgemaine Lourens:** Okay, sorry, I derailed.

**Georgemaine Lourens:** Yeah, I think it's a good idea.

**Nicolas Castellanos:** If you want, you can just push it to the branch.

**Nicolas Castellanos:** Yeah, I'll try.

**Georgemaine Lourens:** I don't know how much time you have.

**Nicolas Castellanos:** But if you want to do something else.

**Nicolas Castellanos:** still have the entire day of today.

**Georgemaine Lourens:** And I'll, maybe not tomorrow, but I'll have some time on Sunday too.

**Georgemaine Lourens:** Yeah, well, just, if you get it in, then I'll try to make it a little bit better, because I don't know how to do that.

**Georgemaine Lourens:** I can ask Cloud, but it's probably ShitCloud, so.

**Nicolas Castellanos:** I mean, I'm going to do ShitCloud too, so it's the same.

**Georgemaine Lourens:** Yeah, I feel like everyone uses Cloud, but I, yeah, for me, it's kind of like, there are some areas that I just don't have any clue about.

**Georgemaine Lourens:** Like, it will kind of work, but I don't know if it's supposed to work like that.

**Georgemaine Lourens:** Like, for example, like if I ask him.

**Georgemaine Lourens:** To do backend stuff in Atlas, yeah, it works, but I'm also kind of like, yeah, probably if Daniel sees it, I probably  up the whole data.

**Nicolas Castellanos:** I think that's something that I love about this company.

**Nicolas Castellanos:** It's like we are like 100%, I think, about like things working and not that much about it needs to be like perfect in terms of like how the code looks.

**Nicolas Castellanos:** And that kind of stuff.

**Nicolas Castellanos:** So, yeah, if you do stuff on flow, for example, it doesn't matter if it's not great because it only needs for like one single workflow.

**Georgemaine Lourens:** Yeah, no, that's true, but like for Atlas, it's a bit stricter.

**Georgemaine Lourens:** Like I remember the whole reason that we got the front-end guidelines and stuff like that was because I was doing a lot of freestyling.

**Nicolas Castellanos:** Oh, you mean Atlas, like the UI of Atlas?

**Georgemaine Lourens:** Yeah, exactly.

**Nicolas Castellanos:** yeah, that's on the product side of the house, and they are a little bit bigger than we at ClientOps.

**Nicolas Castellanos:** So, yeah, true.

**Georgemaine Lourens:** True.

**Georgemaine Lourens:** But anyway, so to summarize, I will pick a few heroes for you, and I'll share those with you.

**Georgemaine Lourens:** And then you can run your categorization on it, and then you share that with me, and I'll review it.

**Georgemaine Lourens:** And then you can try seeing if we can get slow to pick it based on the right feeling.

**Georgemaine Lourens:** And then we can also try it on fonts, and if that works, then whoop, whoop, and that's awesome.

**Nicolas Castellanos:** You're there.

**Georgemaine Lourens:** But first, I got to finish the gallery, and then I want to drink a red wine and eat.

**Nicolas Castellanos:** Yeah, yeah.

**Nicolas Castellanos:** How about wait a weekend, man?

**Georgemaine Lourens:** You too.

**Georgemaine Lourens:** Enjoy the flights.

**Nicolas Castellanos:** Yeah.

**Georgemaine Lourens:** It's really cool.

**Georgemaine Lourens:** Thank you.

**Nicolas Castellanos:** guys.

**Nicolas Castellanos:** Yeah, it's nice.

**Georgemaine Lourens:** All right.

**Nicolas Castellanos:** See you.

**Nicolas Castellanos:** Ciao.
