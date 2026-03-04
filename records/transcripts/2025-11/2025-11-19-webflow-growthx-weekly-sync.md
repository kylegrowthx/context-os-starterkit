# Webflow <> GrowthX - Weekly Sync

<metadata>
date: 2025-11-19
time: 19:01 UTC
duration: 33 minutes
organizer: liz@growthx.ai
participants: Jason Gong, Najam Ahmed, Sydney Go, Erik O'Brien, Liz Kushnereit, Colin Lateano, Vivian Hoang
fathom_recording_id: 102913599
fathom_url: https://fathom.video/calls/479040926
share_url: https://fathom.video/share/ph5AksWro4AJd5zqgsog69vhtBpSmiX5
source: fathom
enriched_on: 2026-03-02 12:15 UTC
</metadata>

---

## Summary

GrowthX and Webflow aligned on building a comprehensive Webflow code components library (300-400+ components) to provide developers with styled, production-ready alternatives to generic component libraries. The proof-of-concept successfully validated technical feasibility, with each component built as TypeScript + CSS + DevLink config. Webflow will own a central GitHub repo and NPM package to address security concerns around community-contributed code, while GrowthX will contribute components via pull requests. The gallery will adopt a "Made in Webflow" model, using iframes of live component pages to maximize SEO value from long-tail category pages rather than individual component pages.

---

## Context

Webflow's Developer Advocacy team, led by Colin Lateano, is exploring how to build a curated library of production-ready code components for developers. GrowthX is supporting the project from multiple angles: Jason Gong is evaluating technical feasibility and build capacity, Vivian Hoang is tracking SEO performance of related content (integration pages and use case guides), and the broader GrowthX team is handling content production. This is a strategic initiative at Webflow aimed at differentiating the platform by providing styled, web-standard components that work both within Webflow (via DevLink) and in the broader React ecosystem. Success depends on resolving open questions around distribution (GitHub/NPM security model), gallery presentation (iframe-based "Made in Webflow" approach), and build capacity (estimating whether 300-400+ components is feasible).

---

## Relevance

- **To GrowthX Delivery:** This is a major scope expansion for content production. GrowthX must estimate build capacity for 300-400+ components and determine whether to build the component gallery in Webflow (native to Webflow) or Next.js (native to GrowthX). Adopting the "Made in Webflow" model requires operationalizing the process of creating dedicated component pages and iframing them into a main gallery catalog. Integration pages and use case guides are performing well (driving both SEO and internal sales references), validating the content strategy, but GrowthX is currently shipping 5 use case guides/week and 30 aggregation pages/week with capacity concerns.
- **To GrowthX Business Development:** Webflow is investing in developer advocacy and component libraries as a strategic product differentiator. Success on this project could deepen the GrowthX-Webflow relationship, unlock additional work scope (full gallery builds, category page optimization), and position GrowthX as Webflow's content partner for enterprise developer initiatives.
- **To CheckThat / AEO:** The component library and gallery structure represent significant SEO opportunities. Long-tail category pages (e.g., "Webflow button component", "Webflow form component") are where most organic value will come from, not individual component pages. Vivian will track traffic and signup data from integration pages and use case guides via Snowflake, providing data to validate the content model before scaling to components.

---

## Overview

- The code components POC is a success, validating the technical feasibility of creating interactive components for Webflow.
- The project will adopt a "Made in Webflow" model for the component gallery, using iframes to showcase live demos. This strategy leverages a proven SEO driver and aligns with the "built on Webflow" principle.
- A Webflow-owned GitHub repo and NPM package will manage component distribution, providing a secure, curated library that addresses internal security concerns.
- The project will be scoped to 300–400+ components (core types + variants) to build a comprehensive library that goes beyond a simple ShadCN clone.

---

## Key Topics

### Code Components POC Review

  - **POC Success:** The proof of concept (POC) successfully validated the technical feasibility of creating interactive code components for Webflow.
  - **Component Structure:** Each component consists of a TypeScript file, a style file, and a DevLink config file for Webflow import.
  - **Access:** Colin requested access to the Webflow demo site workspace and the component GitHub repo for a full technical review.

### Distribution & Security Strategy

  - **Problem:** A key blocker was the security risk of promoting unvetted, community-contributed code.
  - **Solution:** Webflow will own a central GitHub repo and NPM package for all components.
      - **Rationale:** This model allows Webflow to review and approve all contributions, ensuring security and quality.
      - **Process:** GrowthX will contribute new components via pull requests to this repo.

### Component Gallery & SEO Strategy

  - **Challenge:** Define the gallery's technical foundation and SEO strategy to maximize organic reach.
  - **Decision: Adopt "Made in Webflow" Model**
      - **Method:** Each component will have a dedicated page on a Webflow site, which is then embedded as an iframe in the main gallery.
      - **Rationale:** This strategy leverages a proven SEO driver and aligns with the "built on Webflow" principle.
      - **SEO Focus:** The primary SEO value will come from long-tail category pages (e.g., "Webflow gallery component"), not individual component pages.
  - **Implementation:** Colin will propose this model to the Marketplace team.

### Project Scope & Future Vision

  - **Initial Scope:** The project will aim for 300–400+ components.
      - **Rationale:** This scope provides a comprehensive library by including core component types (e.g., ShadCN's 60) plus multiple variants for each.
  - **Future Vision: AI Integration**
      - The library could serve as a high-quality seed for AI tools like Cursor to generate styled, Webflow-compatible components.

### Integration Pages & Use Case Guides

  - **Performance:** Integration pages are performing well, driving both SEO and internal sales references.
  - **New Content:** GrowthX is now publishing use case guides (5/week) and aggregation pages (30/week).
  - **Data Request:** Vivian will pull traffic and sign-up data for these new content types from Snowflake to track performance.

---

## Action Items

**Jason Gong (GrowthX)**
- Email Ed to add Colin to GrowthX workspace and Webflow demo site
- Estimate component build capacity and catalog size; share estimate with Colin
- Email Colin with repo link and access to Webflow demo site

**Colin Lateano (Webflow)**
- Draft proposal: Webflow Components Library (GitHub/NPM + iframe catalog model); review with Marketplace team

**Vivian Hoang (Webflow)**
- Pull Snowflake traffic and signup data for integration pages and use-case guides; share with Colin and Jason

---

## Transcript
**Jason Gong:** Client day, all my calls I have get packed into this morning.

**Najam Ahmed:** Yeah, I mean, I see your calendar, and I'm like, huh.

**Jason Gong:** Mentally, just like the anchor point for every week.

**Jason Gong:** I just have to get through this morning.

**Jason Gong:** That's good.

**Jason Gong:** Do we have a dinner today?

**Jason Gong:** Rachel, there?

**Jason Gong:** Webflow's chief product officer, and also a guy.

**Jason Gong:** Hey, Vivian.

**Vivian Hoang:** Hey, how's it going?

**Jason Gong:** How's it going?

**Jason Gong:** Long time, I see.

**Jason Gong:** Yeah.

**Jason Gong:** How's everything been going on the marketing side of Webflow?

**Vivian Hoang:** It's good.

**Vivian Hoang:** A lot of, you know, AEO stuff going on.

**Jason Gong:** Yeah, no, I see your posts.

**Jason Gong:** I see Josh's posts.

**Jason Gong:** It's like it's going really well.

**Vivian Hoang:** Yeah.

**Jason Gong:** Do you work directly with Josh or you guys, like, how's the marketing side, like, structured?

**Vivian Hoang:** So I'm on the growth marketing team under Elliot who reports into Josh.

**Vivian Hoang:** Yeah, and Josh leads overall growth, which kind of oversees, like, marketing analytics, demand gen, and growth marketing.

**Jason Gong:** Wait for Colin.

**Jason Gong:** guess today we're mostly going to just chat about the code components project.

**Jason Gong:** Okay.

**Jason Gong:** We had a chat with Zach and Vic yesterday, so we, like, kind of hashed out some details so we can share more.

**Vivian Hoang:** Yeah, was just taking a peek at the notes.

**Jason Gong:** Saw some notes on like the integration pages.

**Vivian Hoang:** Those look like they're doing really well.

**Jason Gong:** Yeah, think so.

**Jason Gong:** Yeah, I think a lot of them are doing really well.

**Jason Gong:** It seems like even beyond SEO, a lot of just get kind of visited internally, which is interesting.

**Jason Gong:** I think Colin was saying some sales folks on your team were like, oh yeah, people were referencing these in the calls, which makes sense.

**Jason Gong:** Or like just starting to roll out the guides, which are like more deep dives into like, I guess more like use cases than like just like the broad integration umbrella.

**Jason Gong:** Yeah.

**Vivian Hoang:** Yeah, that makes sense since most people, once they're on Webflow, they're looking to extend their site integrations.

**Jason Gong:** Yeah, that must be like a pretty, I mean, do you guys...

**Jason Gong:** Kind of measure that journey at all of like, hey, I'm trying to figure out if I want to use Webflow or once I'm user of Webflow, like what the top things are that they like, that make people happy or make them churn, like as integrations in that list.

**Vivian Hoang:** I'm sure there's a team that probably looks at that, probably more on like the growth product side.

**Vivian Hoang:** Whereas I'm more focused on like the self-serve, like bringing in new signups and new customers.

**Jason Gong:** Has that, has that changed at all?

**Jason Gong:** Like I know, you know, like the lovables of the world are like kind of, you know, like flipping everything on its head, but like, how is that going?

**Vivian Hoang:** Yeah, we still see a lot of people looking for like CMS, website builder audience.

**Jason Gong:** So that's, hey, Colin.

**Vivian Hoang:** Hey, Colin.

**Jason Gong:** All right.

**Jason Gong:** right.

**Jason Gong:** I guess before I go.

**Jason Gong:** Has any of the stuff we shared so far made its way to you, or should I go into this, mostly, assuming you haven't read much about what we've been doing?

**Colin Lateano:** I looked at it, I played it on the site, I saw the screenshot, I was exploring things last night, there wasn't a way for me to import it, right?

**Jason Gong:** Or at least it wasn't shared.

**Colin Lateano:** Yeah, I think that repo, like, I actually don't even have access to, you probably shouldn't ask Ed to add all of this, but there's a repo with the components, then there's a Webflow, like, demo site, but again, I don't actually have I played with the Webflow demo site, I moved my mouse around, I didn't open the test page on Webflow, I played with the publish page, so I didn't actually see how it's constructed, so I, if I have access to that, I would able to check that out.

**Jason Gong:** Yeah, we, uh.

**Jason Gong:** to workspace that site?

**Jason Gong:** Yeah, gotta ask Ed to do that, I think he just forgot.

**Jason Gong:** Okay, cool.

**Jason Gong:** So I'll just run through everything.

**Jason Gong:** But we met with Vic and Zach yesterday.

**Jason Gong:** I guess mentally how I'm thinking through this is like, you know, opportunity, it's like, I think you guys are more thinking about it as kind of like a resource to help people get deeper into the platform kind of the same way as the integration pages.

**Jason Gong:** But I will say like, this compared to the integration pages just has like, you know, huge kind of organic awareness that we could try to go after.

**Jason Gong:** And then as far as like, can we do it like the two parts to it are like the first part of creating the component.

**Jason Gong:** I think the answer is definitely yes.

**Jason Gong:** So we have, and I'll share the repo so you can look at, you know, if the files all like make sense.

**Jason Gong:** But you know, we did a few demo lends.

**Jason Gong:** They all mostly just consist of like a TypeScript file and maybe a style file and the

**Jason Gong:** I can't remember the name of it, but like the thing that lets you kind of import it into Webflow.

**Jason Gong:** So like all of these are kind of added in here via DevLink, I think is the name right now.

**Jason Gong:** So that part, I think, I mean, there's going to be some components that I think are just going to be much more complicated, but like even these, like they're, you know, they're interactive, like there's like, they're not, you know, the simplest thing, like just the button.

**Jason Gong:** So I think like this, can already do, and then the part that's like a little bit fuzzier is like what the developer experience is to import it.

**Jason Gong:** That's the thing we probably spent more time on yesterday with Vic and Zach, just like our dev kind of had some thoughts around, you know, like creating a CLI utility of some sort.

**Jason Gong:** I think Vic mentioned, you guys were kind of thinking through the security implications of a lot of this stuff, but that's kind of the last model that we can't really fully understand.

**Jason Gong:** Like suggest anything, you know, concrete, but as far as creating the component, I think.

**Colin Lateano:** I can, I can talk about the, the CLI helper and the package for this, if we want to.

**Colin Lateano:** Okay.

**Colin Lateano:** My, my, my gut feeling is we, we create a package helper that allows you to import the targeted names of all of, of any given component that you include.

**Colin Lateano:** And that's tied up with a component library GitHub that, that we contribute to.

**Colin Lateano:** So yes, there is a security concern about allowing what the, there's a general blanket security concern about allowing, allowing people to import code components that we are promoting.

**Colin Lateano:** They're going to import code components anyway, but ones that we are promoting because can we trust the community to not have.

**Colin Lateano:** It's a negative implication, but if it's our GitHub repo, if it's in our package, and you're contributing to it, then we control what actually is showing up in that package.

**Colin Lateano:** And so I think I could navigate that security concern.

**Colin Lateano:** So in my mind, it's a fair concern because we don't want to present a world where people can change the package.

**Colin Lateano:** But if it's our package, if it's the Webflow developer advocacy components package with all the ones that we're pre-approving and reviewing and working with you on, I don't think there's a great concern in that domain.

**Colin Lateano:** So I agree to that method.

**Colin Lateano:** I think that's the right one, and I'm happy to propose it.

**Colin Lateano:** What that means, though, is that every new component you add would be a push to that GitHub repo, and we would need to find a way to also render and surface it in some sort of component catalog.

**Jason Gong:** Yeah, that's awesome.

**Jason Gong:** So the part that I think needs more thought if we want to move forward with this, because I think there's like different ways to build it out.

**Jason Gong:** I think if you care a little bit more about the kind of organic reach of it, there's like ways to build it out.

**Jason Gong:** I've been looking at stuff like, you know, this, for example.

**Jason Gong:** It's like, if you want to get in front of, you know, stuff like this, it like starts looking a little bit more content-y almost.

**Jason Gong:** Like, you know, whatever.

**Jason Gong:** Yeah, well, I mean, hopefully not as, you know, obnoxious, but, yeah, in that direction, having more kind of like contextual information.

**Colin Lateano:** When I got married in 2023, I always needed a great component.

**Colin Lateano:** I don't know how well we can capture hyper-competitive keywords with a utility tool like that.

**Colin Lateano:** I think the same way our integrations page targets it deeply, deeply long tail.

**Colin Lateano:** I would think this is people who would be searching for terms like Webflow, Webflow interesting gallery component.

**Colin Lateano:** And I think in that way, we already are going down a very deep long tail exploration.

**Colin Lateano:** Well, I don't think you're looking for Astro gallery component.

**Colin Lateano:** You're going to really, that'd be hard for us to rank.

**Jason Gong:** But I think the thing is, like, you could, I guess some of the inspiration we're looking at was, like, React bits.

**Jason Gong:** And, like, I mean, you guys already, like, these components, I guess, are interesting that, like, you don't have to necessarily use Webflow to use them.

**Jason Gong:** That's right.

**Jason Gong:** Like, if you just completely ignore the, like, Webflow dev link file.

**Jason Gong:** Yeah.

**Jason Gong:** So, I mean, my mind always goes there, but, like, totally understand.

**Colin Lateano:** So, I don't care at all.

**Colin Lateano:** And.

**Colin Lateano:** Yeah.

**Colin Lateano:** Yeah.

**Colin Lateano:** And if part, actually I'll say it oppositely, I care a lot.

**Colin Lateano:** I think any way that we can, any way that our contributions can improve the general web is a win on its own.

**Colin Lateano:** That is the nature of DevRel is, yes, we want you to think about Webflow as a major contributor to the open web.

**Colin Lateano:** We are helping build sites.

**Colin Lateano:** Here's a component library that we are investing and generating for you that you can play with and utilize in general React.

**Colin Lateano:** And if you want to use it on Webflow, here's an easy helper to do it.

**Colin Lateano:** But you can go take it somewhere else.

**Jason Gong:** I think that's a win.

**Jason Gong:** think.

**Jason Gong:** Okay.

**Jason Gong:** I mean, maybe, I guess we could dig into that a little bit.

**Jason Gong:** But, like, to me, it's like, like, if you just had a resource that just had the, like, base chatty and components, but you, like, styled it for a use case, you know, and added some stuff on top, like, that's just inherently useful.

**Colin Lateano:** Yeah, it is.

**Colin Lateano:** So when we're talking about what is the discoverability of it, we're also talking about what is the delivery mechanism that we want to service this in.

**Colin Lateano:** And this is where there is chatter happening on inside on DevRel.

**Colin Lateano:** How do we want to support this?

**Colin Lateano:** Do we take on methods to try to build a gallery page system within Fern?

**Colin Lateano:** we put it on the developer's dot?

**Colin Lateano:** Do we find a gallery component system on Webflow main?

**Colin Lateano:** Do we shove into our marketplace and call it a marketplace resource?

**Colin Lateano:** And my gut reaction is it's not a marketplace resource.

**Colin Lateano:** This is a community driven.

**Colin Lateano:** The inherent marketplace is an exchange for the implication of the creator is going to get some financial benefit at some point.

**Colin Lateano:** And this, I would love it if this method.

**Colin Lateano:** And we eventually do get, in the same way the integrations page is getting, people wanting to contribute to it.

**Colin Lateano:** I would love it if this has people wanting to contribute as well.

**Colin Lateano:** But they're knowing that they're contributing enough for financial benefit.

**Colin Lateano:** And so I am curious, has GrowthX built these gallery showcase listing pages before for other adjacent work you've done like this?

**Jason Gong:** Let's see.

**Jason Gong:** We definitely have, I would say like none of them are like extremely complicated.

**Jason Gong:** Like we do, like for example, like Lovable's template place, which is like super early.

**Jason Gong:** Like really, it's kind of just like a collection view.

**Jason Gong:** It's like not very fancy at all.

**Jason Gong:** So we can, I will say like our team is much better versed at building like Next.js websites and not really Webflow.

**Jason Gong:** So like if, you know, a part of this kind of lane.

**Jason Gong:** that.

**Jason Gong:** we're to to

**Jason Gong:** We're adding, like, hey, like, build this on Webflow, then I think I need to, like, go figure out if we can add that resource.

**Jason Gong:** Yeah, does that answer your question?

**Colin Lateano:** Yeah, it gets as close as I could ask today.

**Colin Lateano:** And then I need to ask internally, do we want to hand off this type of gallery catalog to growthx and have you build exactly, as what's ever native to you?

**Colin Lateano:** Knowing that that gets out the market faster, it gives you more control to deliver a discovery mechanism.

**Colin Lateano:** Or do we want to follow a principle that Webflow must be built on Webflow?

**Jason Gong:** Yeah, that would be good.

**Jason Gong:** Because I know, like, with the integration pages, like, at the beginning when that was, like, kind of unclear, we just, like, went out and found some, like, Webflow guide to build it in Webflow, but then it seemed like, like, I think getting something to the level that you guys...

**Jason Gong:** I mean, have a lot of kind of internal things you just need to do, like, probably would just take us a very long time, might not be productive if we could.

**Jason Gong:** So it feels ideal that, like, you know, maybe we don't do that just because we might get stuck in, like, however you guys work, you know, trying to get things rolled out or approved.

**Jason Gong:** But I'll say, like, the content itself, like, for sure, like, it seems relatively straightforward, like, at least for the a couple of components that we tried.

**Colin Lateano:** Yeah, so.

**Colin Lateano:** My, if we, so you're looking at made in Webflow.

**Colin Lateano:** Made in Webflow, I'll tell you exactly how it's constructed, and we could copy this exactly.

**Colin Lateano:** Every one of these sites is an iframe of Webflow.

**Colin Lateano:** So if you look at this, that's a Webflow page.

**Colin Lateano:** And so what, what is happening is actually, we...

**Colin Lateano:** We are taking the submission from the community of this Webflow site, and we are then cloning it to a sample site on our own internal workspace, and then creating every unique collection item off of every unique page.

**Colin Lateano:** So if we were to copy this methodology, what growthx would be doing is, every component created, you create a special page for that component, and then we would find a way to iframe that in using the same frameworks that we're talking about in the Maiden Webflow methodology.

**Colin Lateano:** Could we do that?

**Colin Lateano:** Definitely.

**Jason Gong:** Yeah, that makes sense.

**Jason Gong:** I think it's technically, it's really, like, I don't know how manual this, this part was.

**Jason Gong:** It's, I'm throwing it in here, but, I mean, yeah, like, this part, I feel like, can be operationalized, like, a fair amount.

**Colin Lateano:** Um, Vivian, how is the actual searchability of Maiden Webflow?

**Vivian Hoang:** Made in Webflow actually drives a ton of search for us.

**Colin Lateano:** But is the landing page of Made in Webflow or do the actual individual pages?

**Vivian Hoang:** actually long tail category pages.

**Vivian Hoang:** So, like, you have, if you click on animation at the top, we have, like, a bunch of these tag pages.

**Vivian Hoang:** So, I would say, like, it's probably one of our top SEO drivers.

**Vivian Hoang:** I guess we're playing a category game like we are with integration.

**Vivian Hoang:** Yeah.

**Vivian Hoang:** Although I will say that these pages aren't really maintained right now.

**Vivian Hoang:** And there's a lot of work that we're actually planning to do in Q4 to clean it up, to dedupe.

**Vivian Hoang:** There's a bunch of, like, duplication across the categories and tags.

**Vivian Hoang:** But, yeah, I kind of get what you're saying about, like, creating a showcase for components so much to this.

**Vivian Hoang:** And I think that's a great idea.

**Jason Gong:** Yes.

**Jason Gong:** Yeah, like, I feel like the, like, how it fits with this, I think it's, like, a question in my mind.

**Jason Gong:** Like, I think the component library that we've scoped out so far, I feel like it would go after the long tail of, like, honestly, very similar things, but just with, like, the word, the word React tag to the end, almost, you know?

**Jason Gong:** Like, when I look at keywords, that seems to be, like, where kind of a lot of those sites live at the moment in of the keyword intent.

**Jason Gong:** I don't know if that was the case, like, whether, you know, it's...

**Jason Gong:** somehow it's related to this or just as a completely separate thing, I feel like.

**Jason Gong:** Yeah, that's probably something to figure out.

**Colin Lateano:** I...

**Colin Lateano:** I...

**Colin Lateano:** I...

**Colin Lateano:** I'm not intimidated by this answer.

**Colin Lateano:** If we could operationalize the process to be efficient for growthlux.

**Jason Gong:** Mm-hmm.

**Jason Gong:** Okay, cool.

**Jason Gong:** I guess, okay, so I guess the answer is like the components themselves we can do.

**Jason Gong:** I think they're just like how do want them presented and where they live.

**Jason Gong:** That one seems a bit fuzzy to me.

**Jason Gong:** Like, you know, do you want us to own that versus like if you guys would own that, where would that be?

**Jason Gong:** Yeah, but I guess Colin, how do you?

**Jason Gong:** Are you thinking about all this?

**Jason Gong:** Because this will still require kind of like another lane to be added for us to like scale this up without deep priorities.

**Colin Lateano:** I understand that the scale of this is a scope increase for sure.

**Jason Gong:** Yeah.

**Colin Lateano:** I'm just trying to make sure there's clarity of what we're thinking about doing for this one.

**Colin Lateano:** And I do think a component library is really useful for a visual part of it.

**Colin Lateano:** As long as the Maiden Webflow structure that we're thinking about can also feature a link to the GitHub file and a name and declaring this is the npm call that you would need to make in order to actually import it into Webflow.

**Colin Lateano:** I don't see fundamentally what's bad about that.

**Colin Lateano:** We could probably change the style of Maiden Webflow to make it feel more dev at Webflow.

**Colin Lateano:** We make it a dark pattern instead of being a light pattern, but like, yeah, that seems interesting.

**Colin Lateano:** It's really interesting.

**Colin Lateano:** And if it does have a lot of crawlability, it feels like it then approaches the here's Webflow's suggested series of interesting components.

**Colin Lateano:** And we just have a bunch of shad components and other interesting ideas that we just, you can crawl through and pick and choose.

**Colin Lateano:** That feels like a win, a net win, honestly.

**Colin Lateano:** So what I have to do is I have to go draft this up and propose this as a where am I wrong talking to the Marketplace team on lifting and shifting the entirety of the Marketplace concept of main webflow and seeing if we can just use that?

**Colin Lateano:** What will the operational process be for GrowthX as a proposal?

**Colin Lateano:** But I mean, otherwise, the components seem neat.

**Colin Lateano:** So proving that you could do it is really cool.

**Colin Lateano:** Curious, what do you think at scale you could deliver components?

**Jason Gong:** How many there are?

**Jason Gong:** Is there, like, a number of, like, entities, I guess, within main webflow that seem to, like, be valuable?

**Vivian Hoang:** Like, is it in the hundreds?

**Vivian Hoang:** it in the thousands?

**Vivian Hoang:** Do you mean, clonables?

**Colin Lateano:** Just like, he's asking how many, how many different assets of main webflow become an actual value?

**Colin Lateano:** where then it starts to be a diminishing return of n plus one.

**Vivian Hoang:** Yeah, I have to look into that.

**Colin Lateano:** I'm not sure.

**Colin Lateano:** I don't think we've ever measured it at that.

**Jason Gong:** I feel like, I guess component, yeah, I guess, like, how many components can we create at what scale?

**Jason Gong:** Okay, I guess that's a question, because these first ones were, like, kind of very manually done, you know, the same as with all the other components, I think I can try to estimate it.

**Colin Lateano:** Yeah, if there was a world of asking, if we want to minimally copy the entirety of ShadCN, and then go beyond that and say, what other fun things can we do?

**Jason Gong:** Yeah, because I think base component-wise, like, there's maybe just, like, 5200, like, archetypes of components, but then once you get into the, like...

**Jason Gong:** Okay, let me go try to figure out, like, all the formats of buttons that are useful, you know, that's where, like, I'm not really sure, like, how many there are.

**Colin Lateano:** Yeah.

**Colin Lateano:** Well, probably close to infinite.

**Jason Gong:** Yeah, but, yeah, I guess so.

**Jason Gong:** I guess for SEO purposes, like, it wouldn't be infinite, but then for, like, hey, let me provide your resource with all these components seeded, yeah, I guess that would be relatively infinite.

**Jason Gong:** Let me just ask for, like, a blue button, you know, or something.

**Vivian Hoang:** I think for SEO purposes, you probably want to look at, like, the category types, which is what drives Medium Webflow, too.

**Jason Gong:** Yeah.

**Jason Gong:** Yeah, like, I don't imagine, like, you know, this individual want to be very SEO.

**Jason Gong:** Like, I'm sure some people try to game this and name their things, like, a little bit SEO focused to get traffic, but kind of, same with Canva, like, their category.

**Vivian Hoang:** Yeah.

**Vivian Hoang:** The same as templates, too.

**Vivian Hoang:** The category pages drive probably more than all of the template details pages.

**Jason Gong:** Yeah.

**Colin Lateano:** So, Shad has on their main components, they have 60 categories.

**Colin Lateano:** And then, and then they have, and then they have the registry directory of all their favorite friends, which looks like it's about 50.

**Colin Lateano:** I didn't actually count that one.

**Jason Gong:** I feel like themes of the components is kind of that, for sure.

**Jason Gong:** Sure, would have a pretty big one tail.

**Jason Gong:** Yeah.

**Jason Gong:** OK.

**Jason Gong:** Well, I guess the work on my end is just to see what the opportunity is a little bit.

**Jason Gong:** Because I don't know.

**Jason Gong:** I feel like very different if there's like a couple hundred versus like essentially infinite.

**Colin Lateano:** Yeah, absolutely.

**Colin Lateano:** And then we get down to a question also.

**Colin Lateano:** When do When do they reductive?

**Colin Lateano:** When are they just redundant?

**Colin Lateano:** The point of Shad's whole pitch is a high bar of taste saying this is everything we believe represents what the Shad world is.

**Colin Lateano:** The approach of this is let's blast and just do a lot.

**Colin Lateano:** So there is consideration on that.

**Colin Lateano:** But even with their selective group, they have 60 categories of components.

**Colin Lateano:** of The

**Colin Lateano:** They have 60 core components in Shad, I think.

**Colin Lateano:** Yeah.

**Colin Lateano:** And then they have variant themes on each of the core components.

**Colin Lateano:** So they have 60.

**Colin Lateano:** So we are saying there's 60 core components that represent things in Shad.

**Colin Lateano:** And then beyond that, then are there other variants that we'd want to approach of the same types of components in other versions?

**Colin Lateano:** I would say mainly this project is 300, 400 plus, because we'd want to have categories that are close to the core components of Shad and the different variants that could be imported for that same type of thing.

**Colin Lateano:** This is Shad's accordion.

**Colin Lateano:** This is Feld's core accordion.

**Colin Lateano:** Things like that.

**Jason Gong:** These guys do that.

**Jason Gong:** Yeah.

**Jason Gong:** That makes sense.

**Jason Gong:** Like one thing I think about is like, so minus the like SEO packaging of this, just like I'm a developer, like we're this.

**Jason Gong:** kind of goes of, like, I create a component.

**Jason Gong:** Because I guess right now, like, what would I do if I asked Cursor to, like, make me a component?

**Jason Gong:** guess it just kind of comes up with it.

**Jason Gong:** If I have ShadCN, it'll probably use that.

**Jason Gong:** But I wonder, like, do you think that's the future where, like, the seed that, like, the AI kind of uses to create the variant is kind of just this?

**Jason Gong:** Or do you think there's a future where I don't even know how that would work?

**Jason Gong:** It's, like, you have an MCP where it can just retrieve, like, good seed components that are a little bit more styled.

**Colin Lateano:** Oh, we're talking about future planning?

**Colin Lateano:** I have no idea.

**Colin Lateano:** I would have said you at least would start with, like, who are the most popular React libraries out there for components?

**Colin Lateano:** And can we spin up variants around those for different inspiration ranges, for different visual styles?

**Jason Gong:** Yeah, well, that's true.

**Jason Gong:** Right.

**Jason Gong:** I guess...

**Colin Lateano:** I also want to play a game of, I think if we copied Shad literally directly, we would probably be, it'd probably be worse for the web community.

**Colin Lateano:** It'd probably be one of the dumbest things Webflow could do, is probably just lift the entirety of Shad.cn, say here's how you can import Webflow components, and not just immediately say this is just how you import Shad.cn.

**Jason Gong:** Yeah, that probably makes sense.

**Jason Gong:** I think I'm just trying to think of like, will people, because like right now, if we build it up the way we're talking about, the experience we're thinking people will go through is like, building a website, like I need a button, and instead of like, asking Cursor, I would like, go to Google, I would go to like, Webflow's directory, to kind of like, like use the filters in the search to like, try to find that variant.

**Jason Gong:** I wonder, yeah, maybe I'm thinking a little too far ahead, like if that'll be the pattern, or in the future, somebody will just like, take Shad.

**Colin Lateano:** Oh, should we make an MC?

**Colin Lateano:** Of this component library and have it be a reference so that you can ask Cursor to generate Webflow components for me and this MCP can pull exactly that.

**Jason Gong:** I think that's an interesting idea.

**Jason Gong:** Yeah, like a little bit.

**Jason Gong:** I'm just trying to think of the future of like how developers will try to create like a variant of like one of the hundred, you know, base components that everybody uses.

**Jason Gong:** Like, I want like a special button with a certain animation.

**Jason Gong:** Will the pattern of like going to Google to search for like, Hey, I want a button that kind of pops off the page when I hover over it.

**Jason Gong:** Like, well, is that like a future proof thing people do or just to ask Cursor to kind of like animate the button, you know?

**Colin Lateano:** Yeah, that's a great question.

**Colin Lateano:** My first thought is most AO right now is still core SEO.

**Colin Lateano:** So if we were.

**Colin Lateano:** I think for the right use case that the, that, that the search tool is trying to find and we have the code available.

**Colin Lateano:** So it, pulling that would still be the major context of an agent would run on, but you're right.

**Jason Gong:** Yeah, I think that's right.

**Jason Gong:** Okay, cool.

**Jason Gong:** So I guess since we're on time, does this feel like, because I think like what we wanted to provide to you was like a proof of concept that was like in a way where you can kind of, you know, and you're having internal conversations, but whether to invest here, does this qualify?

**Jason Gong:** Is there anything we can do to kind of package it a little bit better?

**Colin Lateano:** Share with me the workspace or the site that you hosted on so I can show the range of settings.

**Jason Gong:** Workspace plus repo.

**Jason Gong:** We'll share this.

**Colin Lateano:** Yeah.

**Colin Lateano:** Otherwise, this accomplished the POC I was asking for.

**Jason Gong:** Cool.

**Jason Gong:** Okay.

**Jason Gong:** We'll do that.

**Jason Gong:** I know we did an upgrade on the integration pages, but I think there's not a ton there.

**Jason Gong:** We're currently doing like five use case guides a week.

**Jason Gong:** I think that's probably where we'll be for a little bit as we like work out the kinks.

**Colin Lateano:** But.

**Jason Gong:** But basically, we're always trying to be more efficient.

**Jason Gong:** But right now, it's like five there and then 30 on aggregations.

**Colin Lateano:** Vivian, are we tagging these in any way that I could aggregate the traffic that they're getting?

**Vivian Hoang:** I don't know.

**Vivian Hoang:** But I can probably pull that for you in Snowflake.

**Colin Lateano:** Okay.

**Colin Lateano:** As long as it's not just an incremental, we have to add.

**Vivian Hoang:** Mm-hmm.

**Colin Lateano:** Yeah.

**Colin Lateano:** But.

**Colin Lateano:** Okay.

**Colin Lateano:** Helpful.

**Colin Lateano:** So, yeah, Jason, I will add that to my tracker of visits and hits, and we can start seeing how that's going, too, as it gets indexed.

**Vivian Hoang:** I can pull signups, too, if that would be helpful.

**Colin Lateano:** That would be interesting.

**Colin Lateano:** Is that segment-related?

**Vivian Hoang:** Yeah.

**Colin Lateano:** Cool.

**Colin Lateano:** Yeah.

**Colin Lateano:** That'd be really cool.

**Colin Lateano:** Jason, we're to get more data for you.

**Jason Gong:** All right.

**Jason Gong:** Awesome.

**Jason Gong:** I'm just trying to iterate over here.

**Jason Gong:** All right.

**Jason Gong:** Well, thank you all for your time.

**Jason Gong:** Talk to all later.

**Vivian Hoang:** See you soon.

**Jason Gong:** Bye.
