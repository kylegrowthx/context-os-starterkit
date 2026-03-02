# Webflow <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-18
time: 19:00 UTC
duration: 35 minutes
organizer: team@growthxlabs.com
participants: Liz Kushnereit, Kirkland Gee, Jason Gong, Paige Kehoe, Adam Lehman, Kelly We, Meg Murray, Kirat Chhina, Colin Lateano, Michael Huard, Luke Stahl, Vivian Hoang, Anushri Gupta, Darin LaFramboise, Rachel Wolan, Vic Plummer, Zach Plata, Raymond Camden
fathom_recording_id: 123452985
fathom_url: https://fathom.video/calls/570059849
share_url: https://fathom.video/share/DJnKKrycrYVxxR6XsWt2ecDag6pMwupG
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

GrowthX and Webflow aligned on the strategy, prioritization, and user experience for building a large-scale custom React code component library that solves real user problems (e-commerce, pricing calculators, application flows) rather than just filling feature gaps. Kirkland demonstrated AI-generated components with 90-95% accuracy, while Paige introduced user research from the AppGen release (18,000 prompts) to inform prioritization. The primary blocker is creating a scalable landing page process for individual components using Fern (docs-as-code), though non-technical user onboarding will be solved by a "Deploy to Webflow Cloud" API button currently in development.

---

## Context

This is a working session between GrowthX (content marketing agency, led by Liz Kushnereit) and Webflow's product and developer relations team (led by Paige Kehoe, PM for code components, and Kirkland Gee, who owns the code component library development). GrowthX is under an eight-week POC contract with Webflow that runs through late March 2026, focused on creating high-quality content and examples for Webflow's code component library. Adam Lehman joined late (having been added to the meeting without context) representing Webflow's platform perspective. The meeting was called to align on the strategy for creating a production-ready component library at scale, after Kirkland had achieved 90-95% accuracy in auto-generating components from specifications, and Paige had brought new user research from Webflow's AppGen release showing actual user needs and use cases.

---

## Relevance

**To GrowthX Delivery:**
- Component prioritization framework will now be grounded in AppGen user research (18,000 categorized prompts) showing actual use cases (e-commerce, pricing calculators, quote builders, application flows, mortgage flows) rather than relying solely on Discourse discussions and benchmarks
- GrowthX must create landing pages for each component at scale — the primary production bottleneck — likely using Fern (docs-as-code) requiring collaboration with Webflow's newly-hired technical writer and docs team
- Content strategy extends beyond components to create discovery-to-activation paths: jobs-to-be-done content → code components → integration pages, all targeting "beginner dev" or "vibe coder" audience
- Timeline: eight-week POC ends late March 2026, with expected rollover to annual contract coupled with existing content contract

**To CheckThat:**
- Code component landing pages and examples will be fed into CheckThat tool to track LLM visibility and create feedback loop for content adjustments
- Component examples and documentation must be optimized for LLM indexing (LLMs.txt, formatting, Fern structure) given large audience of "vibe coders" who rely on AI for code assistance

**To GrowthX Business Development:**
- Clear expansion signal: Webflow is investing in developer relations and docs infrastructure (new technical writer, Fern revamp) which creates ongoing content partnership opportunity
- Success metrics still being defined (Liz seeking Webflow's input on adoption, SEO traffic, dev usage beyond conversion metrics), indicating collaborative approach to measuring impact

---

## Overview

- **Strategy Shift:** Prioritization will now align with user research from the AppGen release (18k prompts) to build components that solve high-level use cases (e.g., e-commerce, calculators), not just fill feature gaps.
- **Production Bottleneck:** GrowthX can auto-generate components at scale but is blocked by the lack of a scalable process for creating their landing pages.
- **User Onboarding:** The initial CLI-based install will be replaced by a "Deploy to Webflow Cloud" API button to simplify the process for non-technical users.
- **Success Metric:** The primary goal is creating high-quality content that enables the "beginner dev" audience, with secondary metrics like SEO traffic and LLM visibility.

---

## Key Topics

### Code Component Library Goal

  - **Objective:** Build a large library of custom React components for direct import into Webflow.
  - **Scope:** From simple UI elements (accordions, date pickers) to complex, API-driven applications (e.g., a Greenhouse job board).
  - **Production:** An AI workflow generates vanilla React/CSS components with \~90-95% accuracy, enabling high-volume production.
  - **User Experience:**
      - Components inherit site styles via predefined CSS variables (e.g., `text-primary`).
      - Each component includes a local dev server (`npm run dev`) for easy offline styling and testing.

### Prioritization & User Research

  - **Initial Framework:** GrowthX's framework used sources like Discourse, benchmarks, and Webflow's native component limitations.
  - **New Input:** Paige introduced user research from the AppGen release (18,000 categorized prompts).
  - **Strategic Rationale:** This data reveals high-level user goals (e.g., pricing calculators, application flows), ensuring components solve real-world problems, not just fill feature gaps.
  - **Action:** GrowthX will update its prioritization framework using this research.

### User Onboarding & Distribution

  - **Problem:** The current CLI-based install process is a barrier for non-technical users.
  - **Solution:** A "Deploy to Webflow Cloud" API button is in development to enable one-click installs.
  - **Interim Plan:** If the API is not ready for launch, the backup is extremely clear, copy-pasteable CLI documentation.
  - **Distribution:** Components will live in an open-source GitHub repo. A scalable process is needed to auto-generate landing pages for each component, likely using Fern (docs-as-code).

### Success Metrics & Content Strategy

  - **Primary Goal:** Enable the "beginner dev" audience with high-quality, non-slop content.
  - **Secondary Metrics:** SEO traffic, LLM visibility, and dev usage.
  - **GrowthX Strategy:** Code components are part of a larger content ecosystem designed to guide users from discovery to activation.
      - **Tool:** The proprietary "Check That" tool will monitor LLM visibility and create a feedback loop for content adjustments.

---

## Action Items

**Liz Kushnereit (GrowthX)**
- Email Adam meeting context re: code components
- Share Notion space w/ Adam
- Remove Zach from recurring meeting series
- Email Paige proposed success metrics for code components/Cloud Cookbook
- Email Paige list of GrowthX builders for Deploy to Cloud feature flag
- Post meeting notes in channel

**Paige Kehoe (Webflow)**
- Email Liz/Kirkland sanitized AppGen research + native components roadmap bullets
- Email Liz/Kirkland intro to docs/Fern team re: landing page template + LLM indexing

**Kirkland Gee (GrowthX)**
- Email Paige CLI install instructions for non-technical users

---

## Transcript
**Kirkland Gee:** This meeting is being recorded.

**Kirkland Gee:** I'm Kirkland.

**Liz Kushnereit:** How's it going?

**Kirkland Gee:** It's good.

**Kirkland Gee:** How are you?

**Liz Kushnereit:** Good.

**Kirkland Gee:** Cool, let's talk about launch and code components.

**Adam Lehman:** Oh, cool.

**Adam Lehman:** I was added to this meeting and I have no idea why, so.

**Liz Kushnereit:** Oh, no.

**Liz Kushnereit:** There's plenty of context I can share with you after the call, just so you feel more looped in.

**Adam Lehman:** Oh, all good.

**Adam Lehman:** It's all good.

**Adam Lehman:** This is basically my MO for almost all meetings right now.

**Liz Kushnereit:** Oh, yeah, I'm sure.

**Liz Kushnereit:** Hopefully a good experience, right?

**Liz Kushnereit:** We'll share the notion space with you right now.

**Liz Kushnereit:** Oh, hi, Paige.

**Liz Kushnereit:** Nice to meet you virtually.

**Liz Kushnereit:** Okay, cool.

**Liz Kushnereit:** I guess this is really all we need to get going on this.

**Liz Kushnereit:** I know Zach left, so I'll probably take him off the series.

**Liz Kushnereit:** So usually in these calls, we go over content strategy and like our other pieces of the content we're doing for Webflow.

**Liz Kushnereit:** So I won't get into that too much today since it's not too relevant to y'all.

**Liz Kushnereit:** But we also do integration pages and use case guides.

**Liz Kushnereit:** And then we have our 2026 content strategy we proposed in the QBR.

**Liz Kushnereit:** So there's quite a lot there.

**Liz Kushnereit:** That's more to sort of renew and compound all the different work streams we're doing for y'all.

**Liz Kushnereit:** And then I put in some new SoW language for Colin to review.

**Liz Kushnereit:** And there's just like how we're scraping topics for jobs to be done work.

**Liz Kushnereit:** It's all very like opinionated Webflow content and some examples of that.

**Liz Kushnereit:** So that's more just like an FYI to see how everything overall fits together. And it's useful for y'all — if you see something that doesn't align with the work we're doing on code components or the cloud cookbook, if there's something there that's alarming, please escalate.

**Liz Kushnereit:** And then we can see how all of that strategy still is pretty cohesive.

**Liz Kushnereit:** And then for today's call, it's really more of kind of a working session.

**Liz Kushnereit:** And so I appreciate that y'all don't have like maybe as much context about what's been built around code components.

**Liz Kushnereit:** So we're happy to add more color to that.

**Liz Kushnereit:** Any just like overview or high-level questions.

**Liz Kushnereit:** And then Kirkland, I'll give it over to him, but this is sort of the prioritization framework we started to work through.

**Liz Kushnereit:** And so there's quite a bit of open questions there.

**Liz Kushnereit:** And then for me, just I would also, if we have time, try to think through, if not today, but at some point, how we define success once we ship these, this type of content.

**Liz Kushnereit:** So is it like adoption, SEO traffic, dev usage, like what would for y'all's team be more of what we think of success?

**Liz Kushnereit:** And then we can make sure that fits in.

**Liz Kushnereit:** So yeah, I guess I'll hand it over to you, Kirkland, if that's okay.

**Kirkland Gee:** Yeah, sure.

**Kirkland Gee:** I'm going to go ahead and tell you guys my, I have a not quite two-year-old, and he basically didn't sleep last night.

**Kirkland Gee:** So if anything I say doesn't make sense, or you need me to repeat something, just bear with me for the next little bit.

**Kirkland Gee:** I feel like I'm working on like 30% of my normal brain power today.

**Kirkland Gee:** Okay.

**Kirkland Gee:** So there's a lot of stuff that I guess like what, sorry, also, I'm Kirkland.

**Kirkland Gee:** Nice to meet you guys.

**Kirkland Gee:** Where are you guys coming at this from?

**Kirkland Gee:** Where should I start?

**Kirkland Gee:** I don't know how much information you actually have about what we're trying to accomplish here.

**Kirkland Gee:** If none is the answer, that's also fine.

**Paige Kehoe:** I would say assume none, just because that's probably the safest way to make sure we all get on the same page.

**Kirkland Gee:** Yep.

**Kirkland Gee:** Okay.

**Kirkland Gee:** So basically, we've been just talking about essentially the end goal being really ramping up the library.

**Kirkland Gee:** of custom React code components that can import directly into Webflow, doing that at scale.

**Kirkland Gee:** Both simple components, so think things like accordions or date pickers or things that just aren't like super natively supported in Webflow or there aren't enough options or whatever that might be.

**Kirkland Gee:** And then ramping up to much, much bigger components, think something like a job board that directly connects to Greenhouse through an API key that will pull in your jobs and put those on your website as an example of like a component that's much bigger than just a button or an accordion or something like that.

**Kirkland Gee:** And so where we're at is I've spent a decent amount of time just like trying to essentially get us to like 90, 95% accuracy on one go in terms of like using an AI workflow to give it a spec and have it generate a component that I can import into Webflow and that basically works.

**Kirkland Gee:** So that we can do a hundred of these without it being like, you know, a huge lift.

**Kirkland Gee:** So open questions for us to try to get resolved from my side is, one, I want to show you guys sort of what I've been working on and make sure that we are generally aligned with like the direction of how this is all going to work and feel.

**Kirkland Gee:** And then two is thinking about what the end user experience of finding those components is, because one, they're going to live in the same GitHub repo where the current examples are.

**Kirkland Gee:** It's open source.

**Kirkland Gee:** It's all there.

**Kirkland Gee:** We can add more components and we can set up a pretty simple workflow to just check that GitHub repo and update or generate pages in Webflow based on each component in the repo.

**Kirkland Gee:** But it would be good to, like, have an understanding of what those landing pages might look like or how built out they're going to be, those sorts of things.

**Kirkland Gee:** Yes.

**Kirkland Gee:** It is, so basically I forked this and just kind of pulled it down and started working on some other examples, but this is just the base one that you guys run.

**Kirkland Gee:** There's nothing I added in this repo just yet, but I can show you just an example, and these are still a little messy because I didn't bother styling everything perfectly because I was just trying to make sure it would mostly work.

**Kirkland Gee:** But like this is the existing website.

**Kirkland Gee:** I use this like really stylized template as a good example of like, can I make a component that will just kind of feel like it belongs here on first try?

**Kirkland Gee:** And overall things went fairly well.

**Kirkland Gee:** like this is just like a little hero section, super simple.

**Kirkland Gee:** This is supposed to be a weather widget that does work, but I didn't sign up for an API key, so it doesn't load in this component.

**Kirkland Gee:** Better example down here is this job board from Greenhouse.

**Kirkland Gee:** Like this is actually pulling in, I think this is for Figma.

**Kirkland Gee:** I think is the one, because theirs is all public.

**Kirkland Gee:** And so like if I change this token to, I think like OpenAI is another one that just works.

**Kirkland Gee:** No.

**Kirkland Gee:** Okay.

**Kirkland Gee:** Maybe.

**Kirkland Gee:** Okay, I broke it.

**Kirkland Gee:** That's fine.

**Kirkland Gee:** Because that would just be static anyways.

**Kirkland Gee:** It works again now.

**Kirkland Gee:** Or like this is like a pricing table with little animations.

**Kirkland Gee:** And all of these are just components that I built locally, published into here.

**Kirkland Gee:** And all of them have the same set of predefined variables.

**Kirkland Gee:** So like for example, and we would just have this listed somewhere on the, like on the landing page.

**Kirkland Gee:** Like a readme of like, hey, here's how you style your components.

**Kirkland Gee:** I think it's text primary is the name of the example.

**Kirkland Gee:** So let's say we make that red.

**Kirkland Gee:** We should go back and all the text in those components will turn red, right?

**Kirkland Gee:** So, and there are a bunch of those.

**Kirkland Gee:** I don't remember what they all are right now.

**Kirkland Gee:** But.

**Kirkland Gee:** This looks whack, but this is all just like, did it load?

**Kirkland Gee:** And that was all I was worried about, and I wasn't going back and cleaning things up.

**Kirkland Gee:** And also, I didn't touch any of these components by hand, right?

**Kirkland Gee:** All of these were just auto-generated by workflow.

**Kirkland Gee:** And in the real world, when we actually push these, you know, there will be a human touch after that generation when we add it to the repo to make sure that everything feels good.

**Kirkland Gee:** Just to show you, hold on, an example of how I'm thinking about that.

**Kirkland Gee:** Let's see if we can pull this up.

**Kirkland Gee:** So for each component, I also had it generate a really simple dev view.

**Kirkland Gee:** So you can just npm run dev in whatever folder of the component that you're building.

**Kirkland Gee:** And it will show you a light mode, dark mode, a kind of custom brand mode, or you can customize any of the relevant variables to see, like, what that might look like on your site.

**Kirkland Gee:** And you can just do all this locally.

**Kirkland Gee:** Make any...

**Kirkland Gee:** Edits to the code, look at everything locally, and then push it up to your website, so that way you can kind of style it offline super, super easily.

**Kirkland Gee:** Someone doesn't have to like build up the dev server, like it's already configured, all that kind of stuff.

**Kirkland Gee:** And this is the same job work component that you saw.

**Kirkland Gee:** This is like the default, and then in Webflow, it ends up looking like this, just because of the styling that's already inherent on this site.

**Kirkland Gee:** That's a bunch of ramblings.

**Kirkland Gee:** Does that all make sense?

**Kirkland Gee:** Any questions, thoughts about any of this, anything that's like, hey, this is very clearly missing, or we really need to think about this other use case or anything like that that I'm not thinking about?

**Paige Kehoe:** I mean, I think this all makes sense.

**Paige Kehoe:** The bigger thing is, and this is probably outside of the growthx scope, for Adam and I to take off.

**Paige Kehoe:** It's more like how we're going to be promoting these and how we're going to make sure that folks are finding them, right?

**Paige Kehoe:** Because we can build the best components in the world, but if folks aren't aware that they exist, the whole effort is cool.

**Kirkland Gee:** Yeah, and I think the way that we're imagining that is like we already have like these here, like some of these examples with a live example.

**Paige Kehoe:** And this just links, think, to the repo.

**Paige Kehoe:** So it could start like they can all just get pulled into here, but then I'm imagining it would be good for each of them to have their own kind of landing page, right?

**Kirkland Gee:** Instead of just being linked here, like this little component being a part of another page that's on slash code components slash, you know, job board, pulls in a pretty brief description of how to implement it.

**Kirkland Gee:** But like, especially for people who are, like, I know these are designed for developers, but I'm also imagining a lot of people using these are going to be like vibe coders that kind of know what they're doing, not people that are like strictly front end devs.

**Kirkland Gee:** You know, they can change CSS, but they don't necessarily know everything.

**Kirkland Gee:** So you want to make that on-ramp super easy, right?

**Kirkland Gee:** That's kind of how I'm thinking about it.

**Paige Kehoe:** That makes sense.

**Paige Kehoe:** And then something I'm curious about would be, is there anything we can do from a formatting perspective or, like, guidance on the way we should either create this page or do, like, you know, an LLMs.txt or configure our docs to ensure that LLMs are picking this up?

**Paige Kehoe:** Because I feel like having these examples is great, making sure that they're indexed and viewed by LLMs.

**Paige Kehoe:** We do know a lot of our audience is vibe coding.

**Kirkland Gee:** Yes.

**Kirkland Gee:** And so I'm imagining, like, some of that is just in the way that we've built.

**Kirkland Gee:** So kind of the first question, like, what do we want to do with the landing page?

**Kirkland Gee:** Like, I'm sure I have some opinions.

**Kirkland Gee:** I'm sure Liz has some opinions.

**Kirkland Gee:** I'm sure Colin will have some opinions.

**Kirkland Gee:** And we can sort of, like, pull all those together and figure out, like, what content needs to be on that job board component page to make that as relevant as possible.

**Kirkland Gee:** And you guys, like, what's the best way to display those examples?

**Kirkland Gee:** I think everything else is relatively straightforward.

**Liz Kushnereit:** I think I can chime in a little bit also on, like, overall strategy.

**Liz Kushnereit:** So I'm to share my screen again.

**Liz Kushnereit:** Yeah, I'll shut up for a minute.

**Liz Kushnereit:** Yeah, just to kind of, for, like, that overall context, the idea is also, like, existing content.

**Liz Kushnereit:** And specifically, we've shipped integration pages for y'all, and those have done really well, and we produce those at a really large scale.

**Liz Kushnereit:** And so how do we create, like, a whole, not the full ecosystem, but almost the full ecosystem of enabling, like, a beginner dev or, like, a dangerous dev is a word that Colin uses a lot.

**Liz Kushnereit:** And so what's discovery, moving into jobs to be done content, that activation path, do we move into code components or dev docs, do we move through integrations?

**Liz Kushnereit:** And then, you know, the example in this diagram is building an e-commerce site, then how do you add, like, an add to cart button?

**Liz Kushnereit:** And that's, like, one way that we drive to code components besides.

**Liz Kushnereit:** It's just like fully letting them be indexed and found on their own.

**Liz Kushnereit:** And then in terms of LLM visibility, part of this process, we have a proprietary tool that's built into the renewal contract called Check That.

**Liz Kushnereit:** And so we would be feeding all of these topics into that as we're going.

**Liz Kushnereit:** So we'd be able to track that ourselves as we're moving through the production piece and like going through it and then establish a feedback loop so that we can adjust and change if we're seeing that that's not working.

**Liz Kushnereit:** But this is like the idea.

**Liz Kushnereit:** I hope that like kind of answers that question and provide some color to that, but of how we would make it all make sense together and then also develop a feedback loop for performance and adjust as needed.

**Liz Kushnereit:** Okay.

**Liz Kushnereit:** All right.

**Liz Kushnereit:** I'll give it back to you, Kirkland.

**Kirkland Gee:** Yeah, I mean, that's helpful context. Let me back up — I did forget to mention something helpful to this conversation: a lot of the jobs-to-be-done content actually informs our component prioritization.

**Liz Kushnereit:** Right. So this is our component prioritization framework.

**Liz Kushnereit:** So linked in the notes, and then I dropped it in the channel yesterday.

**Liz Kushnereit:** This is, I think, the way looking through discourse, like benchmarks on ChatCN, like native element implement limitations with Webflow native elements, and like maybe a list of what's roadmap for the next like 12 months so we don't, you know, duplicate effort.

**Liz Kushnereit:** And then B2B developer use case patterns are sort of the approach we're taking.

**Liz Kushnereit:** And then if you go through, there's a lot of content here, but sort of how we would approach like the top 20, everything like that.

**Liz Kushnereit:** Like there's a sliding scale here of how much y'all want like ownership and decision making around like what we do and don't build.

**Liz Kushnereit:** Or there, you know, you can give us like you can approve our framework and let us sort of move forward with it and just provide us with anything that might limit us.

**Liz Kushnereit:** But it's really up to y'all. It would obviously be helpful to take the time to read through this, but it's not a question you have to answer today.

**Paige Kehoe:** Yeah, I scanned this yesterday because I think you shared the agenda yesterday or this morning.

**Paige Kehoe:** And I know we have a bit more UXR from, so some context here is I'm taking over for the PM who owned code components.

**Paige Kehoe:** So relatively new to the like code component portion of our product, but have been owning all of Webflow Cloud before then.

**Paige Kehoe:** And so that focus was a lot more like high level use case versus the components to unlock them.

**Paige Kehoe:** And so what, what I had half of mine to do and happy to like riff on this or partner, however, this would make sense is we have a lot of, we have a lot of information, especially from AppGen being released around what folks were trying to do.

**Paige Kehoe:** I'm not sure if you saw some of that research or if that was shared with you, but we have the 18,000, 18,000.

**Paige Kehoe:** Prompts that people did categorized into each of the types of apps they were building.

**Paige Kehoe:** And so there was some thought here around making sure we're connecting the dot across this.

**Paige Kehoe:** Like, this is a very clearly defined initiative, but I want to make sure it's in service of kind of the whole offering of, you know, you can build your components, import them for someone to work with the designer, host them on cloud, all in service of a couple of these use cases.

**Paige Kehoe:** I know e-commerce was a big one, but other things we've seen was like pricing calculators.

**Paige Kehoe:** I'm not sure how much that's come up with you is like a huge thing is around more dynamic quote builders.

**Paige Kehoe:** We'll see like mortgage companies doing application flows, all of these slightly more complex flows that are semi-possible with Webflow, but really need some custom work around them.

**Paige Kehoe:** And so it would be, I think, helpful to bring that layer of knowledge in as well.

**Paige Kehoe:** So we have not only each.

**Paige Kehoe:** These little puzzle pieces, but in service of, and we have a couple of those examples already on the docs, but in service of all of those use cases, making sure we have some really well-worn paths.

**Liz Kushnereit:** Okay, cool.

**Liz Kushnereit:** Do you think y'all could share that research with us?

**Liz Kushnereit:** I think so.

**Liz Kushnereit:** Some version of it?

**Paige Kehoe:** Yeah, just something.

**Paige Kehoe:** Yeah, let me like double check that there's not any sort of, you know, confidential information in it.

**Paige Kehoe:** But it was really, I think, really illuminating into what people really want from our platform and what they're trying to do.

**Kirkland Gee:** Yeah, I think that's great.

**Kirkland Gee:** That would be super helpful.

**Liz Kushnereit:** And for our content would also be very helpful.

**Liz Kushnereit:** So it's not just code components, like also the SEO play, but yes.

**Liz Kushnereit:** Okay.

**Liz Kushnereit:** Um, yeah.

**Liz Kushnereit:** So the sooner we could get that, even if it's like just the super high level 10,000 feet view bill, we would update our prioritization framework and then we can sort of move forward.

**Liz Kushnereit:** Or based on that?

**Liz Kushnereit:** Does that sound good to you?

**Liz Kushnereit:** Cool.

**Liz Kushnereit:** Okay.

**Liz Kushnereit:** Okay.

**Liz Kushnereit:** me check.

**Liz Kushnereit:** Oh, yeah.

**Liz Kushnereit:** And so native integrations, I guess, or native components, is there, do y'all have a roadmap for that?

**Liz Kushnereit:** Or do you think you will?

**Paige Kehoe:** Or there is a roadmap for that.

**Paige Kehoe:** It is not currently owned by my team, so I need to go find it.

**Liz Kushnereit:** Okay.

**Paige Kehoe:** But that's something we can get as well.

**Liz Kushnereit:** Yeah, again, like even just bullet points is enough for us just so we don't duplicate.

**Liz Kushnereit:** And then the other open one, did we talk about this, Kirkland, technical constraints?

**Kirkland Gee:** Kind of.

**Kirkland Gee:** mean, there really aren't that many.

**Kirkland Gee:** Like it's, it's working, you know, the idea of generating these components works fairly well.

**Kirkland Gee:** It's just a matter of like figuring out what

**Kirkland Gee:** That landing page experience looks like I think is the biggest thing that's missing because I think at this point like you know if you gave me a list of 100 components like I'm not going to generate them in five minutes but like we could generate them right like it's not that it's not a big gap from that from here to there but if I have a repo full of components I don't currently have a way to be like okay let's go make 100 landing pages right so we have to figure out whoever's going to design that landing page template like I don't know if that's us or you guys.

**Paige Kehoe:** Have you have you worked much with our docs folks?

**Paige Kehoe:** How has that gone with growthx previously?

**Liz Kushnereit:** We have not worked with them at all to my knowledge yeah.

**Paige Kehoe:** Okay there's a little bit of change coming on that end as well we've just hired a new technical writer and we are kicking off kind of a re revamp of the IA of our doc structure but we're keeping with Fern if you're familiar with that and like we're going to be doing docs as code.

**Paige Kehoe:** So I would imagine I've I mean I've worked with Fern in previous lives and I'm

**Paige Kehoe:** I'm assuming you have, or now you will.

**Paige Kehoe:** We can figure out a way to scale that.

**Paige Kehoe:** We'll have to loop in the folks working on that side.

**Paige Kehoe:** The interesting thing is that part of this would be owned by marketing and part of this is owned by developer relations.

**Paige Kehoe:** So we hit, you know, the interesting parts of the Webflow or chart.

**Paige Kehoe:** The other part here from a technical constraints perspective is are there code components or libraries that you've been working with that actually are not working or that you've found issues with when you're generating these?

**Paige Kehoe:** Because I had heard a couple of things.

**Paige Kehoe:** I know my team pushed out a couple of fixes for, what was it, styled components.

**Paige Kehoe:** It looks like we're doing mostly shad CN.

**Paige Kehoe:** Are any of those sort of constraints something you've run into?

**Kirkland Gee:** So I had a long chat and a long read of all the documentation.

**Kirkland Gee:** so the components I'm generating are all like vanilla React and CSS.

**Kirkland Gee:** So we're not using like.

**Adam Lehman:** Can I ask some dumb questions now with the one minute left?

**Adam Lehman:** I'm pretty, I guess I have like high confidence in the tier one.

**Adam Lehman:** So I guess my first question is, is like, how much of that, how long is that going to take you guys to get through the tier one piece?

**Kirkland Gee:** If we're assuming we're going through those.

**Kirkland Gee:** They're simple enough that like the actual building the components, not super difficult.

**Kirkland Gee:** I think it will take much longer to like on the merchandising and figure out how to get it on the website than it would to actually generate the components, like by very, very large margin.

**Adam Lehman:** Gotcha.

**Adam Lehman:** I'm extrapolating that it seems like the original goal of this project is actually to fill in holes in Webflow proper.

**Adam Lehman:** And code components is more of just the tool that we're using to fill those holes in.

**Adam Lehman:** Does that sound right?

**Kirkland Gee:** From what I've heard from Colin, I think that's one way to think about it.

**Adam Lehman:** Yeah.

**Liz Kushnereit:** Let me reiterate our North Star. We're creating content for the beginner dev or enabling dev audience, and truly good content is our North Star.

**Liz Kushnereit:** Code components fall under that — how do you actually enable someone to learn how to build in Webflow. Our success is not hinging on conversion metrics. We want to see the chart go up and to the right, but more importantly, we want to create something that's actually good, not slop. Colin's been very clear on that expectation. But we'd also like to understand what success looks like for you and how we might measure that beyond LLM visibility.

**Adam Lehman:** Yeah, in a previous life, we've built something extremely similar.

**Adam Lehman:** Yeah.

**Adam Lehman:** And when we rolled this out, like say code components, one of the biggest struggles that we had was like sparking our user's imagination of what was possible.

**Adam Lehman:** And so these examples are kind of like, were kind of key to that because it's like, oh, you can do anything that code can do.

**Adam Lehman:** But if you're not a technical user, that's like, what does that actually mean?

**Adam Lehman:** Is that everything?

**Adam Lehman:** And so we had to kind of go through and say, well, look, we could build a carousel for you.

**Adam Lehman:** And then people like, it starts to like click, oh, I don't necessarily need a carousel, but if that's the type of thing you can build, then you might be able to build X as well.

**Adam Lehman:** It looks like we're pushing pretty far towards the, like, these should be usable out of the box.

**Adam Lehman:** And so that tells me this is also maybe for the non-developer audience, like the person who's looking for the carousel.

**Adam Lehman:** And this is more of a conversation with Paige offline, but like, what is our install experience?

**Adam Lehman:** Say I find this component, it looks awesome.

**Adam Lehman:** How does that non-technical user get that in?

**Adam Lehman:** Are we expecting them to like copy and paste from GitHub?

**Adam Lehman:** Is there a launch flow?

**Kirkland Gee:** Right now it's all done through the CLI.

**Kirkland Gee:** I can say that.

**Paige Kehoe:** Adam, I think some context here, and this is where the puzzle pieces are not yet connecting, and I do have to hop to another meeting, but something also for you to be aware of, GrowthX Team, is we are actually in the process of creating a Deploy to Webflow Cloud API button.

**Paige Kehoe:** Not sure if Collins mentioned that to you, and so some of my, like, higher level things on, okay, how can we get a batch of code components that is an example app that then we have this Deploy button in the ReadMe, so you can immediately say Deploy, and then I would say Tier 2 would be DevLink Import to import those code components, depending on your job to be done and your user persona, because there's a bit of a Venn diagram of these folks, um, lots to noodle on there at the negative tier.

**Kirkland Gee:** Yeah, that's, from what we were talking about with Colin, what I kind of gathered was that's, like, the end goal.

**Kirkland Gee:** If we are ready to launch this before that's...

**Kirkland Gee:** Ready, the kind of backup plan is like very, very clear documentation on like, hey, here's exactly what you copy paste in your terminal to get this up to Webflow.

**Kirkland Gee:** And, you know, I mean, that's kind of for you guys to decide like where we want to land on that.

**Paige Kehoe:** And then timeline wise, how long, I mean, I'm not going to hold you to this right now, but just because my team is building this API, we are close to a point where we can feature flag folks for at least deploying to cloud.

**Paige Kehoe:** The import is via CLI for now.

**Paige Kehoe:** So there's things we can do to let you test this out earlier as well.

**Kirkland Gee:** Yeah, mean, Liz, I'd kind of defer to you on that of like when, how, you know, what's our.

**Liz Kushnereit:** So we're, yeah, we're in a POC right now, an eight week POC, which I think ends at the end of March.

**Liz Kushnereit:** And so like, I guess it's just, ideally, we just move into whatever our typical annual contract that's sort of coupled with our existing content contract.

**Liz Kushnereit:** Correct.

**Liz Kushnereit:** So.

**Liz Kushnereit:** So.

**Liz Kushnereit:** Thank

**Liz Kushnereit:** I don't know.

**Liz Kushnereit:** I don't personally have an opinion on stalling anything. Work done should be utilized. At a minimum, if it's ready to be feature flagged, we can deploy components.

**Paige Kehoe:** Exactly. If it's ready to be feature flagged and you or someone else is building, we can let you deploy components.

**Kirkland Gee:** Okay, sounds good.

**Liz Kushnereit:** All right, I'll post follow-up notes. Thanks everyone, and we'll talk more later.

**Kirkland Gee:** It was good to meet you both. Thanks everyone.
