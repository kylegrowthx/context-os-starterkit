# Webflow <> GrowthX Weekly Sync

<metadata>
date: 2025-09-03
time: 17:32 UTC
duration: 33 minutes
organizer: jason@growthx.ai
participants: Jason Gong, Sydney Go, Luke Stahl, Colin Lateano
fathom_recording_id: 84739710
fathom_url: https://fathom.video/calls/397678509
share_url: https://fathom.video/share/9PysbALrEDe_1rWkN4cCsf2sAyYqzu6Q
source: fathom
enriched_on: 2026-03-02 23:45 UTC
</metadata>

---

## Summary

GrowthX and Webflow aligned on prioritizing SEO articles and integration guides while deprioritizing competitive listicles due to quality review overhead. GrowthX shared progress on 75 published integration guides (10-15/week) with positive partner feedback, and Colin Lateano proposed exploring AI-generated code components and templates for Webflow Cloud and Code Components to accelerate developer adoption — Jason Gong agreed to scope the project and return with resource requirements and feasibility by the following week.

---

## Context

This is a recurring weekly sync between Webflow's product and DevRel leadership (Colin Lateano, Luke Stahl) and GrowthX's engagement team (Jason Gong, Sydney Go). The relationship began with an SEO content contract (~6,000 pieces/year) that has evolved into deeper technical collaboration. Over the past weeks, GrowthX shifted from generic SEO to targeted, high-quality integration guides that pair Webflow with partner platforms like Stripe. The guides are performing well and inspiring partners to author their own integration pages. Colin is now exploring how GrowthX can help extend developer adoption through more sophisticated code samples — moving from "What is X?" conceptual content to runnable code examples and React components for Webflow Cloud and Code Components.

---

## Relevance

**To GrowthX Delivery:**
- Integration guides are repeatable, high-quality, and performing well at scale (10-15/week, 75 published). The pattern is now validated and can be extended to code components and templates.
- New code component project requires scoping React generation capabilities and assessing lift vs. current capacity. This is adjacent to CheckThat and Bolt work GrowthX has done.
- Webflow's Airtable system for content approval (SEO, listicles, code components) is working. Colin can review and approve in batches.

**To GrowthX Business Development:**
- Account expansion opportunity: Original 6,000-piece/year contract unlikely to be hit due to quality focus, but multiple expansion lanes emerging (code components, marketplace seeding, template libraries).
- Partner enthusiasm signal: Two partners reached out asking to author their own integration pages — suggests content value and attachment.
- No timeline pressure on code components project gives GrowthX flexibility to scope and plan resource allocation strategically.

**To CheckThat:**
- Webflow's interest in AI-generated code samples creates potential testing ground for CheckThat capabilities around code quality, safety, and guardrails in generated output.

---

## Overview

- SEO content: 18 articles approved in Airtable; listicles deprioritized due to competitive nature and heavy review overhead (product marketing required for accuracy)
- Integration guides: 10-15 completed per week; 75 total published; Colin confirmed comfort with structure and behavior; two partners requesting to author their own pages
- New opportunity: Exploring hundreds of AI-generated code samples for Webflow Cloud and Code Components marketplace — Colin seeking pattern validation to inspire developer adoption
- Technical blocker: API key for publishing expired/invalid; Luke Stahl to generate new key; Sydney to confirm error details from engineer

---

## Key Topics

### SEO Content Strategy

- 18 SEO-focused articles approved in Airtable, ready to produce
- Listicles deprioritized due to competitive nature and extensive review requirements (require product marketing review for accuracy on each competitor comparison section)
- Focus on faster-to-produce, less competitive SEO content (e.g., "What is a webhook?")
- 75 pieces published so far; 15/week ongoing production rate

### Integration Guides

- 10-15 guides completed weekly; 75 total published to date
- Colin Lateano confirmed comfort with structure and behavior — guides are repeatable and scalable
- Two partners reached out in past week and a half requesting to author their own integration pages (positive adoption signal)
- Google Tag Manager implementation delayed until after Webflow conference; once live, will enable analytics data sharing to validate SEO performance
- Next step: Jason to pull SEO performance numbers for integration pages to share following week

### Webflow Cloud & Code Components

- Colin proposed AI-generated code samples and templates for Webflow Cloud and Code Components to drive developer adoption
- Webflow Cloud: Application hosting service; would need pseudocode, command-line instructions, deployment guidance (similar to integration guides but more technical)
- Code Components: React components that can be embedded in Webflow; opportunity to generate hundreds of small, functional "micro apps" to inspire developers (store locators, stock price displays, etc.)
- Goal: Pre-seed marketplace with inspirational, high-quality examples; let community contribute additional components
- Precedent: GrowthX previously worked on similar projects for Bolt and Vapi (gallery/template marketplaces)
- Jason to scope feasibility, resource requirements, and timeline; no deadline from Webflow — flexible exploration of growth lever

### Content Generation Contract & Resource Planning

- Original yearly contract: 6,000 pieces of content
- Unlikely to hit this volume due to focus on quality and human-in-loop evaluation (similar to Surge peer-reviewed research approach)
- Colin prefers retainer model — allocate GrowthX team (Sydney, Jason, writers, engineers) to Webflow's evolving priorities rather than chase piece volume
- Current resource allocation: Sustainable at integration guide pace; code components project would require scoping and potentially shuffling priorities
- Path forward: Jason to propose scoping and resource planning once code components feasibility is assessed

---

## Action Items

**Colin Lateano (Webflow)**
- Review 'for consideration' SEO articles in Airtable and approve relevant ones for production queue

**Sydney Go (GrowthX)**
- Get specific error details from engineer regarding expired/invalid API key issue

**Jason Gong (GrowthX)**
- Scope code components project: deliverables, resource requirements, and feasibility assessment
- Pull SEO performance numbers for integration pages to share the following week

**Luke Stahl (Webflow)**
- Generate new API key for publishing and send to team

---

## Transcript

**Luke Stahl:** How are you doing?

**Colin Lateano:** I'm having a busy day.

**Jason Gong:** Yes, I know your Webflow conference is coming real soon.

**Jason Gong:** It certainly is.

**Jason Gong:** I can give a quick, or I'll just give our usual update.

**Jason Gong:** Let's see here.

**Jason Gong:** So I guess, like, changes from last week, we kind of got the SEO article approved.

**Jason Gong:** So we're doing more there.

**Jason Gong:** But for listicles, guess the feedback was, you know, in general, might be a little bit tough to publish those, because we'll get pretty deep.

**Jason Gong:** So maybe to deprioritize for now.

**Jason Gong:** I guess that was from the thread that you posted, Luke.

**Jason Gong:** I guess my question would just be, like, is this a temporary thing because Webflow is doing some deep work right now, and after we'll be able to get back to this, or is it a general policy?

**Luke Stahl:** It wasn't the pushback that we don't want to talk about competitors.

**Luke Stahl:** It's just that those listicles will generally be more competitive nature.

**Luke Stahl:** So they'll require more of a review.

**Luke Stahl:** So it will require then someone from product marketing probably to then do like a deep competitive analysis for each section to verify everything is accurate.

**Luke Stahl:** So it's like they won't be as quick to kind of produce versus those that are like, you know, what is a webhook and what are they kind of like what we did with this other one.

**Luke Stahl:** So that's why I called out those more SEO related ones in the air table and approved like 18 of them in there.

**Luke Stahl:** I think those will be faster to get out the gate versus the listicle one there where we discuss every single different platform from a CMS perspective.

**Luke Stahl:** And then I have to vet whether that's accurate and then vet how we're talking, add in how we're speaking about AI and all.

**Luke Stahl:** So it was like, it's definitely a good foundation, something that then could be taken and expanded upon, but then it's about bandwidth and who can support like really doing that deep dive on it.

**Luke Stahl:** And so definitely someone like Joe would want to have eyeballs on something like that.

**Luke Stahl:** And that was Mike's feedback too, from, or Michael's feedback too, from like the content side.

**Luke Stahl:** I see.

**Luke Stahl:** There's probably more that we could get after from those more SEO focused articles versus the listicles.

**Luke Stahl:** So prioritizing those over these.

**Jason Gong:** Yeah, that makes sense.

**Jason Gong:** I think for like one other client, not ours, we do this like thing before we write where we just assemble this like grid of kind of competitive comparison, like just like, you know, by price, feature, like different pricing tiers.

**Jason Gong:** And then we align on that first.

**Jason Gong:** So the raw materials, I guess, are like correct.

**Jason Gong:** And then we write.

**Jason Gong:** And And then we

**Jason Gong:** To make sure like, you know, it's like easier to kind of not say something that we're not supposed to.

**Jason Gong:** So, okay, maybe when we get to that, we can, we can do that.

**Jason Gong:** But at the moment, sounds like, again, the SEO content, we have some approved and the, now that we got you here, the integration guides, we can focus on those instead.

**Jason Gong:** Yeah.

**Luke Stahl:** And I think it's when we discussed those listicle ones again, it was like, when we just, we were talking about where we were pulling from sources.

**Luke Stahl:** It's like, is it pulling things from like G2 versus like the actual company's platform or actual site?

**Luke Stahl:** And is it pulling from Reddit and all those other things?

**Luke Stahl:** Because then like, is it actually accurate?

**Luke Stahl:** Or is it pulling from third-party sources that might be giving us the wrong information?

**Luke Stahl:** Is it accurate?

**Luke Stahl:** Is it up to date?

**Jason Gong:** I mean, I do think that's like a nice muscle to build there.

**Jason Gong:** Like, I don't know how other companies do it because people like dump these kinds of articles out because they do great for SEO.

**Jason Gong:** Understandably, Webflow's bar is really high, so if we figure out a machine to do that, it'll be pretty advantageous.

**Jason Gong:** So, okay, I guess I'll put that on the back burner for now then, but yeah, I think to move that forward, just being really accurate on what we can say about each product seems to be the main thing, so I'll try to propose something there so that it just doesn't get stuck.

**Jason Gong:** Like, you know, like every single article has to go, like, through a deep kind of product marketing review, I feel like that'll probably slow everything down.

**Luke Stahl:** Yeah, well, and now you also have some information that relates to our headless source of truth and how we speak to us from, like, a headless perspective, so that should help with some of the how we classify us as a CMS, which would kind of benefit a lot of these articles.

**Luke Stahl:** But yeah, I think there's a good chunk of them that's already in the air table that we could start applying, and then I tagged you, Colin, earlier today about, like...

**Luke Stahl:** Even more of them in there that you might have a particular interest in, and if you want to add them into the queue that I put in what I thought would be acceptable, you could also go in there and review and see if there's any of them you'd put in the queue as well.

**Colin Lateano:** This is the queue in editing and review, or this is any editorial content, or is this ready for review?

**Luke Stahl:** Yeah, well, you see how there's a section that says ID approved, there's a whole section below for consideration, which that's where I think if you want to take a look at any of those considering, and if any of them sound like good articles for you, then just add them to the, you know, approved area.

**Colin Lateano:** I'm, okay, sure, I can do that.

**Colin Lateano:** At the end of the day, is this GrowthX generated, or is this going to be very human in the loop?

**Luke Stahl:** This is GrowthX generated.

**Jason Gong:** For everything we do, the main thing for you is: does it pass the bar? For almost everything, there's definitely a human in the loop. The question is how much human and what type?

**Colin Lateano:** I'm trying to comprehend how much human in the loop we're approaching with this. I'm happy to review ideas.

**Jason Gong:** These ones — the SEO grade ones.

**Luke Stahl:** So that's why I figured it'd be easier to pump this stuff out versus some of the other ones that are going to have more eyeballs on it.

**Luke Stahl:** When like those listicles, when you're comparing us to 15 other CMS platforms, there's going to definitely be more eyeballs on something like that.

**Luke Stahl:** Okay.

**Luke Stahl:** That's actually a good call.

**Jason Gong:** Maybe we should create a different category for listicles and product evaluation content, because we've currently bucketed everything under SEO for our other customers — they don't care, they just publish. But here we care. So it sounds like you have a bunch of stuff approved. That unblocks us. We're going to get spun up and rolling. Sydney, is that everything you needed?

**Jason Gong:** The main thing was just getting approvals.

**Sydney Go:** And then the API key for publishing — the one we got didn't work.

**Jason Gong:** Did you ask the engineer what the error was?

**Sydney Go:** I'll ask again. He just said there was an error.

**Jason Gong:** I've provisioned these before. It usually just makes you check a bunch of boxes to figure out what access it needs. We're probably just missing something.

**Sydney Go:** Yeah, let's get the details.

**Jason Gong:** For integrations, nothing really to call out. We've published 75 so far. We split out ones that are published but you haven't looked at yet. We have a bunch going through edits, still doing about 15 a week. Colin, anything on integration guides?

**Colin Lateano:** I liked it last week, liked it the week before. The last one I see is still v1. The only comment I had is the conclusion felt very AI written, but that's the last version I see.

**Colin Lateano:** And so everything else on here, I'm absolutely comfortable with the behavior and the structure of this.

**Colin Lateano:** I think this is pseudo guidance, so I think that's right.

**Jason Gong:** Cool. So the last thing — Webflow Cloud and code components. Can you share a bit more on what you're thinking?

**Colin Lateano:** Are there other topics you want to cover first?

**Jason Gong:** No, I think pausing listicles is the main thing.

**Colin Lateano:** So, on the DevRel side, we provide code samples and guides on how to get started with a lot of behaviors.

**Colin Lateano:** I can show you an example.

**Colin Lateano:** If you look at our getting started guide on Webflow Cloud, we provide a sample set of code and how to use.

**Colin Lateano:** I'll provide the actual link here too.

**Colin Lateano:** More or less, Webflow Cloud is incredibly complicated.

**Colin Lateano:** It's a hosting service.

**Colin Lateano:** It's more or less a very weak terraform.

**Colin Lateano:** And so what we do on highly technical documents is make a bunch of samples with different methods — hey, if you want to do X, Y, and Z in code, here's how.

**Colin Lateano:** But we push a lot of samples out, and you can find that in the example section here.

**Colin Lateano:** So where I'm going with this is, I believe really great companies for getting started to use their highly technical products, make much deeper investments in a range of code samples.

**Colin Lateano:** Now I know GrowthX, our original contract was SEO. I really enjoyed the integration guides you've been working on. And so I'm curious how much we can explore in terms of creating code samples or template examples of what's needed code-wise to take certain actions. Let me show you what I mean. So for instance, if you wanted to run an action on Vercel and didn't know how to start, you'd say, well, how do I actually start using a blog starter kit on Vercel?

**Colin Lateano:** I want to host a blog on Vercel.

**Colin Lateano:** This is actually just basic pseudocode of here's what you would need to do in order to actually do this on Vercel.

**Colin Lateano:** it's honestly just, this is as close as we did to the integrations pages.

**Colin Lateano:** I would make an argument that our code templates are a little more complex because they're full end-to-end, here's full code.

**Colin Lateano:** But to run on a Vercel example or make a bunch of templates here, honestly, this is already what you're doing in integrations.

**Colin Lateano:** And so I am curious if there's a world that can start going down to Vercel cloud templates.

**Colin Lateano:** But if you want to do this on Vercel cloud, here's what you would need to use.

**Colin Lateano:** Here are the different.

**Colin Lateano:** And actions you would need to run on your command line, here's how you would need to host it, here's how you would deploy it with Webflow Cloud.

**Jason Gong:** And then, I guess for Webflow Cloud, like, what is the universe of things there?

**Jason Gong:** Like, is it more functional components and less so, like, styling?

**Jason Gong:** Yes, it is.

**Colin Lateano:** Webflow is offering a constrained app hosting service in the same way that Purcell exists.

**Colin Lateano:** We are literally offering a style of Purcell.

**Colin Lateano:** And it is for hosting apps on Webflow, hosting your site on Webflow, or some integration between hosting your database.

**Colin Lateano:** Hosting it through Webflow, so we can then take part of the hosting fees, but also then it makes integration across site easier because now you have an app on Webflow and host it in Webflow, so you make the connection much cleaner because your site's also on that same host.

**Colin Lateano:** CodeComponents is more or less a React app that you can host on Webflow and embed custom React code.

**Colin Lateano:** Again, a bunch of code samples of, hey, here's a, you want to see what a React app is, here's one that could show your store's location based on the user's browser, or here's a domain of like, here's what the current price of our stock is.

**Colin Lateano:** Like, there's a bunch of random things we could do.

**Colin Lateano:** And basically, I think that would be, if we could get the pattern right, I think it would be easy to generate hundreds of getting started samples.

**Colin Lateano:** And why I think about that.

**Colin Lateano:** So, I'm marrying two things in the same time I talk.

**Colin Lateano:** Cloud is, is pseudocode, what command line to run to host your app and embed the files of your app in Webflow Cloud for hosting.

**Colin Lateano:** Dating code components.

**Colin Lateano:** It happens.

**Colin Lateano:** is a bunch of examples I guess I heard about how to make a good component and what you could think about in doing that behavior.

**Colin Lateano:** But why I think about that a lot is one of our best growth levers at Webflow is this.

**Colin Lateano:** Made in Webflow where community members submit sites they've made in Webflow to inspire users.

**Colin Lateano:** And you see them and you say, wow, I can't believe Webflow can do this.

**Colin Lateano:** And from that point, we have a whole list of, hey, do you want to go get a template?

**Colin Lateano:** You want to copy a template?

**Colin Lateano:** Do you want to use it?

**Colin Lateano:** I believe that we could have hundreds of code component examples.

**Colin Lateano:** We can create a new marketplace item here, a new template guide for code components.

**Colin Lateano:** And we can pre-seed a whole marketplace of here's a bunch of cool examples you can use.

**Colin Lateano:** And then ideally we can get the community inspired to keep doing it too.

**Colin Lateano:** But our biggest concerns are the attach rate of these products, because it's more technically involved than the average Webflow user. But we know the user is out there and wants to engage.

**Jason Gong:** Not every template component is attached to something. But when I look through template marketplaces, there's a bunch of things that are almost extensions of integration work.

**Colin Lateano:** That's why I thought this was so adjacent.

**Jason Gong:** We've gone from API docs and general use cases to the use case itself and getting deeper. This is probably as close as we get to runnable code that actually works.

**Colin Lateano:** Your integration guides are pseudo-code. This is still pseudo because it's basically command libraries you'd want to install and run on Vercel with guidance. That's close to what your Stripe example was. The real depth is with code components — can you generate actual React to run a component? I don't know if that's in your wheelhouse or if your models can do that.

**Jason Gong:** Yeah, we did this for Bolt — a design tool with a template marketplace. The code that comes out isn't super deterministic, so slightly different, but we've definitely done work in that domain. Lanes-wise, we're probably at our limit from our other three clients. This one seems more involved. Let me scope it and figure out if we can do it.

**Jason Gong:** And if it means shuffling priorities or expanding what we're doing for you guys, we can talk about that. I think the Bolt project is probably the closest precedent.

**Jason Gong:** We also did it for Vapi, but those were more around prompts. It would be something like this — maybe more akin to Made in Webflow than what you're describing.

**Colin Lateano:** Cloud is our hosting service; code components are a way you can import your own React code into Webflow. If we could generate a hundred interesting React applets and host them in Webflow Code Components, that's already a very interesting pre-seeded marketplace and template library. I was jumping around — cloud is for hosting, code components is importable code you can put on your site.

**Jason Gong:** Got it.


**Colin Lateano:** We need to be developer-assistive in our designer. Code components is literally, in the simplest way, import your React or JavaScript. If you have models and experience making clean code examples — like galleries you're doing for Bolt — we can see what we can do quickly. Our DevRel team produces one or two a week. These are really just simple micro apps on React.

**Jason Gong:** Definitely doable.

**Colin Lateano:** This is where we have them right now because we're only making a couple. These are really intensive.

**Colin Lateano:** This is an end-to-end.

**Colin Lateano:** The one you saw at the Careers Playground is what we used as demos.

**Colin Lateano:** Here's everything you could do.

**Colin Lateano:** It is end-to-end database, unique API structure, calls, all those functions.

**Colin Lateano:** I don't recommend.

**Colin Lateano:** That's not what we're trying to copy here.

**Colin Lateano:** But if we could figure out.

**Colin Lateano:** The closest you would see is like our template libraries in Webflow.

**Jason Gong:** Yeah.

**Colin Lateano:** And what I would do is I would actually spin up a new product SKU.

**Colin Lateano:** In our libraries for code components.

**Colin Lateano:** This is the template?

**Jason Gong:** No, this is like the full website.

**Jason Gong:** maiden Webflow for inspiration.

**Colin Lateano:** If you go to the marketplace, this is a thing we're trying to fix after Webflow conference.

**Colin Lateano:** If you go to the marketplace here, I'll send the link for you.

**Colin Lateano:** Very fraught.

**Colin Lateano:** If you're frustrated, imagine me.

**Colin Lateano:** Check the link on that.

**Colin Lateano:** This is the library of, hey, you can import all these interesting components.

**Colin Lateano:** We would pretty much be offering the same type of treatment, except there'd be a code component with the embedded code that you've created.

**Jason Gong:** Okay, I guess these are more like packs, but you'd be able to find just a singular thing over here.

**Colin Lateano:** The evolution of this would be, this is one individual component that you could import and clone.

**Colin Lateano:** And this is...

**Colin Lateano:** So this would be the same treatment.

**Colin Lateano:** I'd be creating a completely new marketplace listing structure for code components.

**Jason Gong:** Okay, cool.

**Jason Gong:** mean, yeah, I mean, fully doable.

**Jason Gong:** I think as far as what the lift is, let me get back to you on that.

**Jason Gong:** Let me poke around just like what the structure of it would actually be.

**Jason Gong:** Let's see.

**Jason Gong:** And then like any, I guess, timelines on your side where it's like, oh, if we can't do it in the next, you know, X number of weeks, like it's not worth it.

**Jason Gong:** Not at all.

**Colin Lateano:** This is, I'm currently exploring how do we supplement our growth lever.

**Colin Lateano:** And I know developer adoption comes first from inspiration.

**Colin Lateano:** So I have no timeline on this.

**Colin Lateano:** I'm just looking to find out how I can lever the resources I have available to me.

**Colin Lateano:** Cool.

**Colin Lateano:** Here we can look it it up.

**Jason Gong:** up.

**Jason Gong:** up.

**Colin Lateano:** I've really enjoyed having GrowthX on the integrations part of our hub. Leaning technical with GrowthX is a very interesting angle we didn't predict.

**Colin Lateano:** I'm happy with that shift from just SEO to actual value add. I'm trying to figure out how we can keep that going. I don't foresee us hitting our current yearly contract of 6,000 pieces of content. I don't predict we'll pull that off now that we're focused on quality and human-in-the-loop evaluation.

**Jason Gong:** I should probably look at that. Generally, that's how we work. For Surge, the data labeling guys, we're doing peer-reviewed research posts, and there's no way we do one a month. This isn't that, but we'll adapt to what you need.

**Jason Gong:** We could back into article counts per month if needed. Generally we allocate resources — you've got Sydney, a chunk of my time, writers, engineering time. It's just what we focus on.

**Colin Lateano:** So if it's more retainer, and we just quantified at first by 6,000 what the general retainer would cover in a year, then I'd love to see what we're able to do with the talent we have on the table.

**Colin Lateano:** Yeah.

**Colin Lateano:** But yeah, there's no timeline for, oh, if this isn't possible, drop it.

**Colin Lateano:** I would say no matter what my dream state answer is, we seed our template library.

**Colin Lateano:** .

**Colin Lateano:** With AI generative examples that we believe are high code quality, that are clean code, that it can be readable, understandable, how it behaves.

**Colin Lateano:** Whatever it takes to get there, I think is interesting.

**Colin Lateano:** Okay.

**Colin Lateano:** I mean, that is our bar.

**Jason Gong:** just like, it has to be useful and valuable.

**Jason Gong:** know, it doesn't matter if it's made by AI.

**Jason Gong:** At least that's my take.

**Jason Gong:** Let me get back to you next week. I'll scope it out, see what we need to do, talk through resource trade-offs, and then we can move forward.

**Colin Lateano:** With that in mind, on the integration cadence — is the Airtable still up-to-date on the integration pages?

**Sydney Go:** Sorry, I was muted.

**Sydney Go:** Yeah.

**Sydney Go:** So, I, I...

**Colin Lateano:** What I'm seeing of Integration Pages, I'm seeing only 10 completed on the Airtable.

**Colin Lateano:** Is that the correct number?

**Sydney Go:** Those are completed and reviewed, but then if you see that Ready for Client Review is also published.

**Sydney Go:** Okay, got it.

**Colin Lateano:** So if I'm just eyeballing, we are doing about 10 a week, or is it more than that?

**Colin Lateano:** About 10 to 15 a week.

**Sydney Go:** Cool.

**Colin Lateano:** If we're comfortable with the guide drafts, is this repeatable at scale? Can I see a few more examples?

**Jason Gong:** The first one wasn't a full machine — more a proof of concept. My work now is figuring out how to make it repeatable, and then I'll get you more to review.

**Colin Lateano:** And for analytics purposes, the team is trying to implement Google Tag Manager and was delayed until after Webflow conference.

**Colin Lateano:** Once we have Google Tag Manager, we can then start sharing analytics data.

**Colin Lateano:** I'll give you a heuristic though — two partners in the last week and a half reached out asking if they can author their own integration page. They think it's worth their time. Eventually they'll send drafts and we'll figure out implementation.

**Jason Gong:** I looked at the SEO performance and they're getting indexed and growing. Next week we'll pull actual numbers.

**Colin Lateano:** That'd be great — I'd share those internally to show this investment is working.

**Jason Gong:** So for us: continue integrations, build out the generation machine, do some SEO work, and scope the code components project. Let's see what we can help with.

**Sydney Go:** On the API key — the engineer said it's expired or invalid. We just need a new one.

**Luke Stahl:** I'll go get a new one.

**Sydney Go:** Got it.

**Colin Lateano:** Appreciate your time.

**Colin Lateano:** I'll chat with you guys later.

**Jason Gong:** Sounds good.

**Luke Stahl:** Bye, everyone.
