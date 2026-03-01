# Webflow <> GrowthX - Weekly Sync

<metadata>
date: 2026-01-21
time: 19:00 UTC
duration: 56 minutes
organizer: team@growthxlabs.com
participants:
  - name: Colin Lateano
    company: Webflow
    email: colin.lateano@webflow.com
  - name: Zach Plata
    company: Webflow
    email: zach.plata@webflow.com
  - name: Jason Gong
    company: GrowthX
    email: jason@growthx.ai
  - name: Liz Kushnereit
    company: GrowthX
    email: liz@growthx.ai
  - name: Kirkland Gee
    company: GrowthX
    email: kirkland@growthx.ai
  - name: Kelly We
    company: Webflow
    email: kelly.we@webflow.com
  - name: Meg Murray
    company: Webflow
    email: meg.murray@webflow.com
  - name: Kirat Chhina
    company: Webflow
    email: kirat.chhina@webflow.com
  - name: Michael Huard
    company: Webflow
    email: michael.huard@webflow.com
  - name: Luke Stahl
    company: Webflow
    email: luke.stahl@webflow.com
  - name: Vivian Hoang
    company: Webflow
    email: vivian.hoang@webflow.com
  - name: Anushri Gupta
    company: Webflow
    email: anushri.gupta@webflow.com
  - name: Darin LaFramboise
    company: Webflow
    email: darin.laframboise@webflow.com
  - name: Rachel Wolan
    company: Webflow
    email: rachel.wolan@webflow.com
  - name: Vic Plummer
    company: Webflow
    email: victoria.plummer@webflow.com
  - name: Raymond Camden
    company: Webflow
    email: raymond.camden@webflow.com
fathom_recording_id: 116084032
fathom_url: https://fathom.video/calls/538013025
share_url: https://fathom.video/share/kLeNYFEAVeiFGPhn3TC7xzys75X4x6aL
source: fathom
enriched_on: 2026-02-28 18:35 UTC
</metadata>

---

## Summary

GrowthX and Webflow aligned on the scope and direction of a strategic initiative to build a Code Components library and example apps ("Cloud") that lower the barrier to entry for developers building on Webflow. The initiative has pivoted from a marketing-focused "AppGen" showcase to a practical, B2B-oriented developer resource featuring pre-built components and contextual use-case examples. Key blockers discussed include API access for automating workflows and scheduling challenges.

---

## Context

Webflow and GrowthX are collaborating to build developer-focused tooling that extends Webflow's capabilities. Colin Lateano (Webflow) originally proposed an "AppGen" initiative to showcase inspiring use cases, but this evolved into a more pragmatic approach: a library of pre-built Code Components and example applications that solve real-world B2B problems. The Code Components library addresses a core technical constraint: Webflow's live-rendering system ("Wooftle") limits standard frameworks like Tailwind, requiring custom component solutions. GrowthX, led by Liz Kushnereit and Kirkland Gee, is tasked with building and documenting these assets while unblocking infrastructure needs (API tokens, scheduling).

---

## Relevance

**Strategic & Product:**
- Reframes "AppGen" as a developer-first initiative, shifting from inspiration-driven marketing to practical B2B solutions
- Clarifies scope: Code Components (foundational) vs. example apps (iterative, open-ended)
- Defines Webflow's strategy to compete with lower-code barriers (vs. ShadCN, which Webflow can't directly integrate)

**GrowthX Delivery:**
- Guides engineering capacity planning and sprint roadmap for Kirkland's team
- Identifies infrastructure blockers (API tokens, deployment hosting patterns) that affect delivery pace
- Establishes recurring sync timing (to be rescheduled) as a critical coordination mechanism

**Webflow Partnership:**
- Clarifies the distinction between "AppGen" (Webflow's internal agent) and "Cloud" (the showcase initiative)
- Establishes that the library is *not* Marketplace-bound, avoiding a marketplace distribution conflict
- Identifies key decision-makers: Colin (Code Components strategy), Zach (API + infrastructure)

---

## Overview

- **Strategic Pivot:** The initiative shifts from a marketing-focused "AppGen" showcase to a practical "Cloud" library of Code Components and example apps.
- **Core Goal:** Provide a library of pre-built Code Components (e.g., sliders, accordions) to fill gaps in Webflow's native library and lower the barrier to entry for new users.
- **Technical Constraint:** Webflow's live-rendering system ("Wooftle") limits standard frameworks like Tailwind. This necessitates a custom library of components modified to fit these rules.
- **Phased Approach:** Prioritize the Code Components library first, then build example apps that combine these components with Webflow Cloud services (e.g., a Greenhouse careers page).

---

## Key Topics

### Strategic Pivot: From "AppGen" to "Cloud"

  - The initiative's focus has shifted from a marketing-driven "AppGen" showcase to a practical "Cloud" library.
  - **Rationale:** The original "fun inspiration" approach lacked clear ROI and failed to resonate with developers, who need useful, B2B-focused tools.
  - **New Focus:** A library of pre-built Code Components and example apps that solve real-world problems, such as a middleware service for an ABM campaign.

### Code Components: The Core Library

  - **Goal:** A library of pre-built components (e.g., sliders, accordions) to fill gaps in Webflow's native library and lower the barrier to entry.
  - **Technical Constraint:** Webflow's live-rendering system ("Wooftle") limits standard frameworks like Tailwind.
      - **Impact:** This constraint prevents simply importing existing libraries like ShadCN, making a custom library essential.
  - **Design Strategy:**
      - Offer multiple styles for each component to provide variety without imposing a single design system.
      - Prioritize adaptability: components should integrate with a user's existing site styles (colors, fonts) via a clear class-naming convention.
  - **Distribution:**
      - **Repo:** A GitHub repository for engineers to clone and fork.
      - **UI:** A CMS-driven showcase page with live iframes and documentation.
      - **CLI:** Future integration with the Webflow CLI for direct import.

### Example Apps: Building with Cloud

  - **Goal:** A "cookbook" of \~100 example apps demonstrating practical uses for Webflow Cloud services.
  - **Integration:** Apps will combine Code Components with backend services (e.g., Node, Astro).
      - **Example:** A Greenhouse integration app that uses a custom Code Component slider to display job listings.
  - **Showcase:** Apps will be displayed in live iframes on the showcase page.
      - **Challenge:** Creating meaningful visual demos for non-visual apps (e.g., middleware).

### Admin & Logistics

  - **API Access:** Liz requested updated API access (CMS + assets write) to automate image uploads for integration pages, unblocking a manual workflow.
  - **Meeting Time:** The recurring sync time conflicts with Colin's schedule; Liz will coordinate a new time.

---

## Action Items

**Liz Kushnereit (GrowthX)**
- Post channel poll to reschedule weekly sync (Colin Lateano conflicts with current time)
- Schedule scoping meeting with Code Components/DevLink PM + Colin Lateano

**Kirkland Gee (GrowthX)**
- Draft Code Components/Cloud scope document; share with Liz + Colin

**Zach Plata (Webflow)**
- Provide Liz with updated API token (CMS + assets write permissions) by end of day

---

## Transcript

**Liz Kushnereit:** This meeting is being recorded. Good morning.

**Kirkland Gee:** Hello.

**Liz Kushnereit:** Thanks for joining, Kirkland. We're still waiting on a few people.

**Kirkland Gee:** Yeah, sure thing. I'm going to be doing a couple of things until we get into it, but I'm here.

[Meeting opens with brief updates on secondary topics, then main participants arrive]

**Liz Kushnereit:** So Jason's running late, but Raymond, I can give you an update on use case guides. We're looking at five a week, at least for now, until we can scale up. We're monitoring these for traffic and performance because it's a bit of a black box with this approach, and we don't want to compete with our existing integration pages.

**Liz Kushnereit:** Zach, do you happen to know if Colin's attending?

**Zach Plata:** I think so. I'll give him a ping.

**Liz Kushnereit:** Thanks. My update for you: Zach is still working on the partner update systems, hopefully something by end of month. But we also need API access—I pinged Colin earlier today. We want to add image components to automate icon uploads so we're not doing that manually in the CMS with our high output.

**Zach Plata:** Just like a site token with CMS access?

**Liz Kushnereit:** Yes, and we need assets write permissions too.

**Zach Plata:** I think I can generate that. We can get it to you today. And just to mention to Colin if you do, since I also asked him for it.

[Colin joins the call]

**Colin Lateano:** Good afternoon. Was there a lively conversation, or is everyone waiting for me?

**Jason Gong:** Honestly, the last couple of minutes was just awkwardly waiting for you.

**Colin Lateano:** That's terrible. Can we move this time? I'm triple booked with a couple of different partners.

**Liz Kushnereit:** Yeah, I'll put that in the channel. Well, we mostly wanted you to help us talk about the scope piece of the expansion. So first, let's talk through code components. That's why I brought Jason and Kirkland. And then also the app gen piece, where we've done less scoping and prototyping.

**Jason Gong:** Context is that we brought Kirkland, who drives the engineering work on these engagements. The more we know about what you're signing up for, the more we can figure out how to schedule and manage capacity. Code components seem more scoped because we actually built a bunch of them. App gen was the more vague ask. Maybe start with what you're trying to accomplish and how you envision this marketplace of templates.

**Colin Lateano:** I want to be careful of the word "marketplace" because this won't live on Webflow's branded marketplace—that's user-generated content for agencies. This will live in a new universe, like "Made in Webflow," with some sort of canned templating. Code Components is our escape hatch for things you want to build that Webflow's opinionated Wooftle system can't support. It's how we support React and Tailwind effectively in Webflow. We want to offer a series of pre-made components you can import because lower-code or new technical users need that. Getting started is the hardest blocker to building on Webflow. So we want a large-scale library of components: sliders, accordions, lists, grids, movable objects, and other cool features we see in the wild that people can import.

**Jason Gong:** So the original discussion with Aaron seemed anchored more on AppGen?

**Colin Lateano:** Yeah, that was anchored on AppGen, but if you notice it fell off, there wasn't a reason for it. It was very marketing-focused—"have a big list of cool things so people say, cool idea, let's build." It was about inspiration, like Figma Make with a piano you can play. But that didn't have any legs in terms of ROI. We came back to: what's the ROI and value here? These are B2B sites. They want to build components, attribution models, and structures to make their site easier to manage. I moved from "how do you have a Game Boy on your site" to "how do you have a really nice scroll bar." Single-shot prompts don't really deliver the app you want. You need skills, guiding light, refinement. That's not what our developers are looking for. They're not looking for fun inspiration or designer content. DevRel isn't promoting this to designers—we're saying "isn't this useful?" "Don't you want to use this?" The biggest gap our partners ask about is contextual examples of iterative use cases for Cloud. They're looking for examples of why you'd have a Node app or Astro app to help accomplish marketing goals. It's less "here's a cool player piano" and more "here's how to build a middleware service that scrapes your CRM and feeds data to code components for an ABM campaign."

**Jason Gong:** So practically, it's like website templates that run on Webflow Cloud?

**Colin Lateano:** Mostly, yeah. Some part of the site operates off Webflow Cloud. It's not all middleware—that's just one example of a cloud service you might want to run.

**Kirkland Gee:** Could I repeat back what I'm hearing? The end goal is a ShadCN-style experience with basic components like buttons and sliders, in a documented place, easy to understand the code, with a button to import into your Webflow site. Then, larger components like micro apps—a pricing calculator, for example—useful in various business cases.

**Colin Lateano:** Yes, exactly. Where things get muddy is the breadth of use cases. Our most used example is a mid-layer that pulls from Greenhouse and pushes data to a code components data access layer, so you can have your own styled careers page that's up to date with Greenhouse listings. That's an app. Pricing calculator tied to your ERP, a translation service, an AI chat—the domain range is wide. We want 100 examples of interesting apps to inspire people on what they could build. The repo lives on its own so engineers can clone and fork, with a CMS representation explaining what they're looking at, maybe an iframe showing a live example on a Webflow project. This is for engineering engagement tied to our doc site.

**Kirkland Gee:** The ideal experience is seeing a live example. With a button component, fine. But with middleware and a Greenhouse connection, we need deployment—maybe the repo connects to Vercel or Render with subdomains.

**Colin Lateano:** There's going to be iteration on how we show this. I'm comfortable with hosted examples. Dummy data is fine. On Made in Webflow, we iframe Webflow sites as visual reps. We'd carve out a special project, and each true app would have its own site or page, iframed with explainers. Our challenge is making meaningful visual representations. Some apps aren't visual. My goal is 100 examples of interesting apps. Maybe they get the code repo and throw it into Cursor. The ShadCN approach is what I'm getting at: what are interesting components? This could be a hybridization.

**Kirkland Gee:** That's the easier part—opinionated button and slider designs, a library of components used in the apps.

**Colin Lateano:** Ideally, yes. Especially things like a slider feed to your Instagram page so you get up-to-date polls from Instagram. That uses a slider component we created.

**Kirkland Gee:** Maybe the only big question is: do we have strong opinions about the visual design of these components already, or is that still to be determined?

**Colin Lateano:** We don't have strong opinions because Webflow's philosophy is being the platform for designers to figure things out. We're not creating one design system. We're creating a series of components with multiple styles and renderings to appeal to different design systems. ShadCN introduced "this is how good sites look," but we aren't that. Maybe we create taxonomical series names—"this is one style we created; here's another design system style." You can download and import these. We're wider than ShadCN because we don't have one opinion. My goal is designers and technically savvy people see these libraries and say, "I want to import that and build my own code components" or "I want to use this to guide a component missing from Webflow's native library." It's supplementing Webflow core componentry. We're not talking about a button div; we're talking about components that don't exist in Webflow native—sliders with special interactions, galleries, etc. The hard part is making things unique and visually distinct without being too off-the-wall.

**Kirkland Gee:** Do you have like five different categories or styles we could work with? Not copying ShadCN, but as a model: they have "New York" and "London." If you pick all "New York," they look one way; all "London," another. You define a couple of archetypes manually—what that style needs to look and feel like, what emotion it evokes—and apply that to the component set, making four or five versions of each. It's not a huge ask if the core functionality is the same and it's mostly Tailwind.

**Colin Lateano:** That's a wonderful idea. But here's the challenge: no one on DevRel is a designer. We're all engineers. We don't have the form factor considerations for unique styles and branding. We might have to loop back and get a designer.

**Zach Plata:** I don't think that's important.

**Kirkland Gee:** Yeah, because the more we talk, I think you want this component to come in and adapt to whatever your website already looks like. That's the better differentiator. You add this component, it has the functionality you don't have, but it takes the naming or changes, boom, now it fits.

**Colin Lateano:** That's the dream state. It's the escape hatch to add componentry that doesn't exist in our WYSIWYG, but then you can apply WYSIWYG parts and drag it around. In our library display, toggling between style sheets would be slick—"here's how things can be, here are the style controls, here are the classes that can be introduced."

**Kirkland Gee:** If you think about that up front, it's not that complicated if you're thinking about it from the beginning.

**Colin Lateano:** I'd rather focus on the code component part first and add cool app examples as we progress. I don't think they have to run in parallel.

**Kirkland Gee:** What needs to happen now to get closer? Does our team sit down and think? Are there other people we need meetings with on your side?

**Colin Lateano:** I want to bring in the new PM lead who owns the official Code Components / DevLink effort. She's very open to this and excited about us building an example set and demo for adoption. Maybe their engineering lead, but this is primarily a DevRel thing.

**Kirkland Gee:** On our side, we're comfortable. There's not a crazy amount of engineering outside of writing the components.

**Colin Lateano:** Good afternoon.

**Liz Kushnereit:** Hello.

**Colin Lateano:** I hope everyone was there.

**Colin Lateano:** Was there a lively conversation?

**Colin Lateano:** We were in a lull, or is everyone waiting for me?

**Jason Gong:** I'm not going to lie, last couple of minutes was just awkwardly waiting for you.

**Colin Lateano:** That's terrible.

**Colin Lateano:** Can we move this time?

**Colin Lateano:** This is a conflict I have with a couple of different partners.

**Colin Lateano:** I'm triple booked.

**Liz Kushnereit:** Yeah.

**Liz Kushnereit:** Okay.

**Liz Kushnereit:** Yeah, I'll put that in the channel.

**Liz Kushnereit:** If you have an EA or anything, too, we can work with them.

**Colin Lateano:** Oh, I'm not that high level here.

**Liz Kushnereit:** I'm just busy.

**Liz Kushnereit:** Okay.

**Liz Kushnereit:** Well, yeah, we just wanted you mostly to help us talk about the scope piece of the expansion.

**Colin Lateano:** So, super wonderful.

**Liz Kushnereit:** For that, but wanting to scope out that sprint so we can hit the ground running once we get there.

**Liz Kushnereit:** So first and foremost, talk through code components.

**Liz Kushnereit:** That's why I brought Jason and Kirkland into this call.

**Liz Kushnereit:** And then also the app gen piece.

**Liz Kushnereit:** We've done much less scoping and prototyping on that piece and just wanted to clarify, like, what we're building towards or if we need to talk to another team potentially.

**Liz Kushnereit:** Okay.

**Liz Kushnereit:** Yeah.

**Colin Lateano:** Do you want me to do any recap of these things or just talk about exact questions we have?

**Liz Kushnereit:** So I don't think we need...

**Liz Kushnereit:** Yeah, sorry.

**Jason Gong:** Yeah.

**Jason Gong:** I was going to say, I guess context is like we brought Kirkland who drives a lot of the engineering work on these engagements.

**Jason Gong:** And it's like the more we know, the more they know, I guess, about what they're signing up for, the more we can figure out how to schedule this in and how to manage capacity.

**Jason Gong:** So I think from my end, I mean, would love Kirkland to drive, but like from my end, the code components.

**Jason Gong:** seem more scoped out because we actually did a bunch of them.

**Jason Gong:** The app gen was the more vague kind of ask.

**Jason Gong:** Yep.

**Jason Gong:** So, yeah, maybe just starting with, like, high level what you're trying to accomplish, how you envision this marketplace of templates.

**Colin Lateano:** Okay.

**Colin Lateano:** I want to be careful of the word marketplace because I do not believe any of will live on Webflow's branded marketplace simply because the way the marketplace exists today, is user-generated content as part of growing their business for agency.

**Colin Lateano:** That's just a taxonomy consideration.

**Colin Lateano:** This will likely live in a new universe where we have some sort of canned templating like we do with the term made in Webflow.

**Colin Lateano:** So Code Components is our escape valve, escape hatch for all of the things you want to build on your website that Webflow's opinionated wooftle system can't support.

**Colin Lateano:** It is how we support React effectively and Sunday Tailwind in Webflow.

**Colin Lateano:** And part of that focus is we want to be able to offer a series of great pre-made components that you can import into your Webflow site because lower code users or new technical users will want to have some capacity to import things in and get started.

**Colin Lateano:** We know getting started is the hardest blocker to building on Webflow.

**Colin Lateano:** So the hope there is we generate a large-scale library of different components that you would want to have on a site.

**Colin Lateano:** So granular sliders, accordions, things like that, lists, grids, movable objects, and a strong opinion of that, but also a growing opinion of cool features that we see in the wild that we can just keep growing on so that people can import whatever they want.

**Colin Lateano:** I want fun.

**Colin Lateano:** Thank you.

**Colin Lateano:** If your package proposal of that, I want to chase that one down.

**Jason Gong:** That is...

**Jason Gong:** And does this, just because this was, a lot of this was anchored on that first discussion Marcel had with the other, with Aaron on your team, which none of us were in the room for, but it seemed like that one was a little bit more anchored on AppGen, so like...

**Colin Lateano:** Yeah, it was anchored on AppGen, and I, if you notice that fell off, it is because there wasn't a, there wasn't a reason for it.

**Colin Lateano:** It was very much, at that point, it was marketing-y.

**Colin Lateano:** It was, let's have a big list of cool things, so people say, cool idea, let's go and build.

**Colin Lateano:** And it was focused on inspiration, and it was focused on the way, like, Figma Make has a library of cool, fun things, like a piano that you can...

**Colin Lateano:** And truth be told, that is fun, but if that fell off as a marketing push, because it just didn't have any legs of, like, how much it would cost to do that, and build.

**Colin Lateano:** Thank Thank Thank

**Colin Lateano:** And so we came back to what is the ROI, what is the value add we want to do here, and I'm a much more boring person.

**Colin Lateano:** And my response is, end of the day, these are B2B sites, and they want to get started on building components and attribution models and structures to actually make their site easier to manage and get going.

**Colin Lateano:** So I walked away from how do you have a Game Boy on your site, and more towards how do you have a really nice scroll bar on your site.

**Colin Lateano:** But it's a shift, because Aaron on the Marketplace team was tasked with a marketing launch for AppGen of how can we show off all these fun-generated apps to get people inspired in single-shot prompts.

**Colin Lateano:** What we also learned is that single-shot prompts don't really deliver the app you want anyway, so it wasn't that easy to put together a single-shot prompt and have a cool app available.

**Colin Lateano:** You need a bunch of sense.

**Colin Lateano:** Skills, needed a bunch of guiding light, you still need to refine things.

**Colin Lateano:** I'm not saying walk away from that vision, but I am saying that that's not really the use case that we see resonate with our developers.

**Colin Lateano:** They're not looking for fun inspiration.

**Colin Lateano:** They're not designers.

**Colin Lateano:** We're not promoting this.

**Colin Lateano:** If it's a DevRel-run project, it's not promoting to designers saying, isn't this cool?

**Colin Lateano:** Don't you wish you could have a fun part of your site?

**Colin Lateano:** We're saying, isn't this useful?

**Colin Lateano:** Don't you like the style of this one?

**Colin Lateano:** Don't you want to use this?

**Colin Lateano:** And so that then leads to the app part of it too, is the apps is a, what we are seeing as the biggest gaps of our partners asking us like what to use cloud for is they're looking for contextual examples of actually iterative use cases that help explain why you have a Node app.

**Colin Lateano:** Why have an Astro app, why have these apps?

**Colin Lateano:** apps on your site to help accomplish your site business marketing goals.

**Colin Lateano:** And they don't know what they don't know of how to get started and what to build.

**Colin Lateano:** So it's less about, here's a cool way to have a player piano that when you click on can play different songs from 1920.

**Colin Lateano:** It's more, here's how have a middleware service that can scrape across multiple parts of your CRM and have available data layer for your code components to actually render data for an ABM campaign.

**Colin Lateano:** Like, it's more use case focused apps that helps set a stage for different parts of your marketing journey and site management as templates that you can then look at and configure and say, I like that.

**Colin Lateano:** want to use that to help steer how, what I can build on my site.

**Jason Gong:** Yeah.

**Jason Gong:** So I guess practically it's like a bunch of websites, essentially website templates that run on Webflow Cloud.

**Colin Lateano:** Have some part of the site operate off of Webflow Cloud or some novel.

**Colin Lateano:** That operates off of Webflow Cloud.

**Colin Lateano:** It's not all middleware.

**Colin Lateano:** That's just one example set of a type of cloud service that would want to be run.

**Jason Gong:** But, yes.

**Jason Gong:** I think that's a bit more clear.

**Jason Gong:** mean, I'll leave it to Kirkland, but originally, I guess we were thinking, was there some restriction to like, okay, cool, these websites had to have been made with AppGen, you know, or something like that.

**Colin Lateano:** But it sounds like that's not the case.

**Colin Lateano:** It's not the case.

**Colin Lateano:** And it's, the app, the app, and also the AppGen part of it is, it's not, does this have to, AppGen is the name of our, our code, our, our code writing agent.

**Colin Lateano:** And you're not using it.

**Colin Lateano:** We're not offering hooks right now to have your agents call our agents.

**Colin Lateano:** It's like, making this part of AppGen in any capacity is a total misrepresentation.

**Colin Lateano:** I would rather have this...

**Colin Lateano:** The nicely documented, clean code of interesting apps that you could potentially import or configure or make some modifications that help solve an example of what people want to do as you would see on any really, really great developer-first documentation site of here's an example of a use case or here's a cookbook of really interesting things that you could make and style and design your way to meet your integration needs or your site needs.

**Kirkland Gee:** Could I just try to kind of repeat back what I'm hearing and make sure I understand?

**Kirkland Gee:** Because I'm coming into this, you know, with some context, but then hearing what you're saying.

**Kirkland Gee:** So we're thinking sort of the end goal of this sort of initiative is, and I'm going to oversimplify this, but to have sort of a ShadCN style experience in terms of basic components, things like buttons, sliders, that kind of stuff, in some sort of documented place, easy to use, easy to

**Kirkland Gee:** It's to understand the actual code there.

**Kirkland Gee:** Also probably a button that you can click and import into your Webflow site to add it there.

**Kirkland Gee:** And then on top of that, similar UI, but also have larger than just button components, you know, maybe little micro apps like a pricing calculator or something like that that might be useful in, you know, various business cases.

**Kirkland Gee:** Yes.

**Kirkland Gee:** Is that right?

**Colin Lateano:** Am I understanding that correctly?

**Colin Lateano:** Yes.

**Colin Lateano:** Yes, where the horizon gets a little bit muddy is how bigger and the variety of use cases.

**Colin Lateano:** Our most used app example right now on our doc site is a mid-layer that takes in batch pulls from greenhouse and pushes that data to a data access layer for code components.

**Colin Lateano:** So you can have your own styled careers page.

**Colin Lateano:** That's up to date with your greenhouse listings.

**Colin Lateano:** That's a really cool app.

**Colin Lateano:** Mm-hmm.

**Colin Lateano:** It's utilized in a lot of integration styles with the enterprise team for builds.

**Colin Lateano:** That's an app in my mind.

**Colin Lateano:** And things like that are where the ideation is going to go wide of, yeah, pricing calculator might make sense, tie it up to your ERP.

**Colin Lateano:** Or a translative service between things or running your own MCP server or little AI chat service on that.

**Colin Lateano:** The domain range is wide of what you would want to have an app do in assistance to your site.

**Colin Lateano:** And so that's where we're going to have a lot of back and forth.

**Colin Lateano:** Like, are these good ideas?

**Colin Lateano:** How do we run in this example set?

**Colin Lateano:** But the end use case is we want to have a repo and we want to have an example page of a cookbook of ideas to get started on cloud and what you can use cloud for to help get going on the needs of your marketing site.

**Colin Lateano:** That's the general area of what was once called AppGen initiative, but it's not AppGen anymore.

**Colin Lateano:** It's just cloud.

**Kirkland Gee:** And then in terms of where that stuff lives, we're going to have a repository where there's like a folder or whatever for each use case, each app.

**Kirkland Gee:** This isn't living in like a Webflow CMS where we need to track all or we have the repo over here, but then the landing page is in the CMS with like the content that goes there.

**Colin Lateano:** I think it's the repo lives on its own so that you can have engineers actually do regular engineering behaviors, clone and fork with a CMS representation that explains what you're looking at.

**Colin Lateano:** Maybe an iframe if it has some sort of visible part of it on a Webflow project that you can then look at and see with some explainers of what's going on.

**Colin Lateano:** But we want this to be for engineering engagement with an exploration tied to our doc site in some meaningful way.

**Kirkland Gee:** Okay, that is making sense.

**Kirkland Gee:** I'm just spinning my, I'm just thinking about, maybe I get into logistics too quickly, but thinking about.

**Kirkland Gee:** How that all sort of connects together.

**Kirkland Gee:** Because in theory, the ideal experience is someone goes to, you know, that careers page example, let's just say.

**Kirkland Gee:** And they can either on that page directly or in a modal, like, see an example of what that looks like live, right?

**Kirkland Gee:** Like, that seems pretty essential to any of this.

**Kirkland Gee:** And with, like, a button, that's fine.

**Kirkland Gee:** You just render it on the page.

**Kirkland Gee:** But if it's, like, something involving middleware and a greenhouse connection, like, that's, we need some way of, whether that's, like, deployed through that repo, like, that repo's connected to Vercel or Render or whatever, and all those live as, like, subpages on some other subdomain or something.

**Kirkland Gee:** Maybe it's that.

**Colin Lateano:** I think there's going to, depending on the ideas that we come up with, it's going to be a lot of iteration of how we actually have this be shown.

**Colin Lateano:** And I'm comfortable with these host examples.

**Colin Lateano:** We don't have to have any.

**Colin Lateano:** I'm a reason for how we get the data into the app or where that data lives.

**Colin Lateano:** It could all be dummy if you wanted, but I do think it's going to be, there's going to be some creativity per app until we have a common pattern established of things.

**Colin Lateano:** On the example set, we have a pattern established under the Made in Webflow universe where we do have a visual, we do have Webflow sites that are more or less iframed as a visual rep.

**Colin Lateano:** So, like, if you want to see the Webflow conference site, this is an iframe of the Webflow project page.

**Colin Lateano:** So, if we want to host the app in a novel way on a, I believe we would carve out a special project for this program, and every app, like, true app, would be...

**Colin Lateano:** It would have its own site, or at least a page of a sample site that is then iframed into this example.

**Colin Lateano:** so we explain, hey, this is the Webflow app to greenhouse render, and open the, open, here's the example of it, and go see it in GitHub or something like that.

**Colin Lateano:** But we have common patterns of a framework to iframe things, and I could show you where, how this is iframed with Webflow sites.

**Colin Lateano:** That's not my challenge.

**Colin Lateano:** Our challenge is going to be, how do you actually have a meaningful representation of the app in this iframe?

**Colin Lateano:** It's going to be the challenge that you might want.

**Colin Lateano:** And maybe some apps are not visual.

**Kirkland Gee:** I have no idea.

**Colin Lateano:** It's amorphous.

**Colin Lateano:** And so I don't really know how to, I don't have a good plan of how we execute on that app part of it.

**Colin Lateano:** But I just know what the goal is, is we have 100 examples of interesting apps to inspire someone to go, and how they use those apps.

**Colin Lateano:** Perhaps it's going to be up to them to actually configure, rearrange.

**Colin Lateano:** Maybe they get the code repo and they shove it into Cursor and they say, go figure  out.

**Kirkland Gee:** I don't know.

**Kirkland Gee:** Yeah, okay.

**Colin Lateano:** The ShadCN example of code components is exactly what I'm getting at, is what are interesting components.

**Colin Lateano:** And it could be a bit of ShadCN too.

**Colin Lateano:** It could be a hybridization of combinations, say this is how you make a really good slider.

**Kirkland Gee:** Yeah, because that's like the more easy part, right?

**Kirkland Gee:** Is come up with some opinionated way we want to design buttons and sliders and whatever else and build that library of things.

**Kirkland Gee:** And then ideally use those components in the apps that we're generating, the apps, whatever you want to call them, as well.

**Colin Lateano:** That would, ideally, yes.

**Colin Lateano:** Yeah.

**Colin Lateano:** Ideally, yes.

**Colin Lateano:** Especially in things like, I'm going to...

**Colin Lateano:** keep saying slider.

**Colin Lateano:** A slider feed to your Instagram page so that you get up-to-date polls from Instagram.

**Colin Lateano:** That would be an app that points to a slider component that we created of some sort of gallery.

**Kirkland Gee:** Yep, right.

**Colin Lateano:** Really cool combination of how these things are used across the board.

**Kirkland Gee:** Maybe the only big question, I mean, there are going be a million questions, but like, it seems like it needs just some like tinkering and sort of work to really like get at the rough edges.

**Kirkland Gee:** But like visual design of these components, do we have like strong opinions about that already, or is that still to be determined?

**Colin Lateano:** I will say, I know we don't, because that's been Webflow's opinion for interactive Webflow is, we are the platform for designers to figure these things out.

**Colin Lateano:** And so, it is not so much are we creating a design system, it is we are creating a series of components, and probably with most

**Colin Lateano:** Multiple styles and renderings to appeal to different design systems.

**Colin Lateano:** So ShadCN introduced a model of this is how good sites look.

**Colin Lateano:** And now a lot of sites look the same.

**Colin Lateano:** But we aren't making one library.

**Colin Lateano:** We're making a series of things and you can search for.

**Colin Lateano:** Maybe we even create, I don't know what you want to call it, taxonical series names of like, this is one style that we created.

**Colin Lateano:** Here's another design system style we created.

**Colin Lateano:** You can download and import these.

**Colin Lateano:** I don't know how you want to frame those things, but this is going to be wider than ShadCN because we don't have an opinion and we want to offer a range to get inspired to pull things in.

**Kirkland Gee:** Okay.

**Colin Lateano:** I think now I'm going to ask as a agency partner, do you think that's a good strategy?

**Colin Lateano:** Because the end goal I have is...

**Colin Lateano:** Is I want designers and technically dangerous people to look at these libraries and say, I want to import that and build my own code components, or I want to use this to guide a component that is missing from Webflow native component library.

**Kirkland Gee:** Yeah, because that's the thing.

**Kirkland Gee:** For the most part, you really don't care if someone's using a button, right?

**Kirkland Gee:** There's a hundred ways to make a button in the Webflow UI, right?

**Kirkland Gee:** It's more about building on top of, or filling in the gaps.

**Kirkland Gee:** Yeah, that's an interesting one.

**Colin Lateano:** And this is supplementing Webflow core componentry.

**Colin Lateano:** We have button div.

**Colin Lateano:** It is, this is a button that when you press has a dimple or something like that.

**Colin Lateano:** Like we're talking about like what are interesting components that don't exist in Webflow native that you can then import and solve problems because you're looking for more things to, looking for more inspiration.

**Colin Lateano:** A lot of what happens on Maiden Webflow, the reason we have Maiden Webflow is we make a

**Colin Lateano:** A bunch of sites, and then people say, that's really cool.

**Colin Lateano:** I want to take this site and review it and use it for my own purposes because the hardest part about getting started on Webflow is getting started.

**Colin Lateano:** And so our end goal with this is to have a massive component library so you can find things that, oh, want to use these things in my component system.

**Colin Lateano:** And one part that I want to make sure that, yeah, this is going to get convoluted, is we have this library concept where you can import.

**Colin Lateano:** People have already made huge libraries of interesting buttons and functionality and componentry.

**Colin Lateano:** This uses Webflow native componentry, and it's just a style library on top of these.

**Colin Lateano:** The novelty of this code component initiative is you don't have to use Webflow opinionated componentry.

**Colin Lateano:** We can design our own that have new opinionated approaches to things.

**Colin Lateano:** That's the gap that we're trying to solve here, is you might go through all of this, and you might say, none of these libraries that are available in Webflow's library service has a native gallery scroll, and I really want one.

**Colin Lateano:** That's where we have, well, now here's a list of interesting components that you can import that have these features that aren't available in Webflow today.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** Because that, I think, is maybe the hardest part, is, like, making things unique, making them, like, visually distinct without being, like, too off-the-wall, you know?

**Colin Lateano:** Like, you can make it distinct, it doesn't make it good.

**Colin Lateano:** Sure, yeah.

**Kirkland Gee:** So, that's something to maybe think about.

**Colin Lateano:** Off-the-wall isn't necessarily bad, as long as not all of them are off-the

**Kirkland Gee:** Right.

**Kirkland Gee:** And it's like, you know, do you just have, you know, literally just talking out loud, but like, do you just pick a thing, right?

**Kirkland Gee:** Let's call it a calendar, right?

**Kirkland Gee:** You want like an embeddable calendar widget of some kind.

**Kirkland Gee:** And you want just have maybe two different LLMs do 10 different variations with like varying prompts and like look at all the outputs and like, you know, how do you do that at scale is like the thing to figure out, I think.

**Kirkland Gee:** And do we have some sort of like, are there five different categories of things, different styles that we could like, you know, not to bring Shad's hand again, but like they do have like a couple of, I forget what they're called.

**Colin Lateano:** It's like New York and London and whatever else.

**Colin Lateano:** Yeah, you're right.

**Kirkland Gee:** They, I forgot they have a matrix of things.

**Kirkland Gee:** So if you're using, you know, their components, and again, we're not really copying them at all, but just like as a mental model, like if you're using their buttons and their sliders and their whatevers.

**Kirkland Gee:** there are you

**Kirkland Gee:** If you pick them all to be New York, they're going to look one way.

**Kirkland Gee:** Pick them all to be London, they're going to look a little bit different.

**Kirkland Gee:** They all still kind of look the same, to be honest.

**Colin Lateano:** It's mostly like slight color variations and that kind of thing.

**Kirkland Gee:** But like maybe you pick a couple of archetypes that we can just like think a little bit manually about what that archetype needs to look and feel like, what emotion it evokes, blah, blah, blah, blah, blah.

**Kirkland Gee:** And then you apply that to whatever set of components and you make four or five different versions of every component.

**Kirkland Gee:** Like that's not a big ask.

**Kirkland Gee:** Obviously, it does expand the number of things you're doing.

**Kirkland Gee:** But if it's the same core functionality and all that really is is Tailwind, right, and maybe like a few little changes or CSS, whatever.

**Kirkland Gee:** Although I remember earlier you said Webflow, like these code components for React, they're not, they don't support Tailwind?

**Kirkland Gee:** Or would you just do like, I guess, how does CSS work with these components?

**Kirkland Gee:** it CSS?

**Kirkland Gee:** On the Webflow side, like once it's imported, maybe this is a dumb question, but.

**Colin Lateano:** It's not a dumb question.

**Colin Lateano:** You can apply CSS uniquely to the component on its own import.

**Colin Lateano:** You have to import libraries for the CSS to be loaded in the component system.

**Colin Lateano:** It is then live rendered onto the site, and then you can apply additional styles from your style library onto those components additionally.

**Colin Lateano:** Zach, what happens on the collisions of that?

**Zach Plata:** We haven't seen much on collisions, but I know there are some difficulties with some libraries like Tailwind.

**Zach Plata:** For example, it doesn't directly import all of Tailwind's native variables, and so you'd have to re-import those.

**Zach Plata:** But in general, with the code components, like Colin mentioned, you're importing a global CSS file.

**Zach Plata:** Like, it's injected, it's all in Capilet.

**Zach Plata:** Capsulated into the Shadow DOM.

**Zach Plata:** But I know there's been some instances where folks have been using some named Webflow variables when they're referencing certain styles inside the actual code component.

**Kirkland Gee:** So some styles do propagate there.

**Kirkland Gee:** Right.

**Kirkland Gee:** That actually almost seems essential, right?

**Kirkland Gee:** Like if someone, well, I mean, depends on what your audience is, but if the audience is someone who has a Webflow site they've started and now they're trying to build on top of it, like the component kind of needs to take things like colors or fonts or, you know, spacing requirements.

**Kirkland Gee:** They've already set up for other things in their Webflow site.

**Kirkland Gee:** Like if this comes in with a new set of colors as a simple example and it just doesn't mesh at all, like that feels like a bad experience.

**Kirkland Gee:** But maybe it doesn't matter.

**Kirkland Gee:** I don't know.

**Kirkland Gee:** Because I don't know how logistically you make that all make sense.

**Colin Lateano:** You would have to go through, this is not for the rudimentary user.

**Colin Lateano:** Right.

**Colin Lateano:** On some import, you would have to change either your class naming or have style imports.

**Colin Lateano:** And maybe we can even deliver.

**Colin Lateano:** If we have five sample styles that we want or we know the class names that we are determining so we can have in our own documentation that always expect form field to be called form underscore field underscore A, like we can define the classes and the structures of it and just say it's your job to change these things.

**Colin Lateano:** Because the big part about why the importing tailwind or importing any real CSS structure or going off of standard React, our code component system does not follow those things to a T.

**Colin Lateano:** Because we are live rendering within the render of Wooftle, we cut things off at edges.

**Colin Lateano:** And so there are patterns that are in standard web frontend now that are still not rendered, which is why supplying this library.

**Colin Lateano:** You things that accomplish what you want to accomplish, but modified to fit our code component rules is why this is such an interesting thing that I'm willing to invest the cost of the scope in.

**Kirkland Gee:** Because if we could have just imported ShadCN, we would have.

**Kirkland Gee:** Right.

**Kirkland Gee:** This is extremely, thank you, so helpful to me in thinking and planning what this is going to look like.

**Colin Lateano:** It's helpful to me, too, because this is a quarter million dollar project, so I would, I'm happy to have the conversation that we're not going to do it right.

**Colin Lateano:** Yeah.

**Colin Lateano:** So this is the domain that we're trying to play into, is like, this is, we want to have a library, and I do think it's bigger than just that ShadCN, which is the atomic components.

**Colin Lateano:** I think there are going to be some combination components that we want to introduce that combine things and say, here's cool combinations that you can import as well.

**Kirkland Gee:** Mm-hmm.

**Colin Lateano:** And then to do that at scale is where the AI part comes in.

**Colin Lateano:** If we have five opinions or five styles, I think that's a wonderful idea.

**Colin Lateano:** What you're going to run into here is no one on DevRel are designers.

**Colin Lateano:** We're all engineers.

**Colin Lateano:** And so we don't have the form factor considerations of what are the very unique styles and branding we'd want to introduce in this coverage.

**Colin Lateano:** So we might have to loop back and go get a designer to have some opinion of this.

**Kirkland Gee:** And then I'm almost wondering, yeah, it's like, do you even want to do that?

**Colin Lateano:** Like, is that really?

**Zach Plata:** I don't think that's important.

**Kirkland Gee:** Yeah, because like the more we're talking about it, I'm like, really, you just want this component to come in.

**Kirkland Gee:** And in theory, like adapt to whatever your website kind of already looks like.

**Kirkland Gee:** That would be the better differentiator, right?

**Kirkland Gee:** It's like, hey, you add this component, it has the functionality you don't have, but it takes, if you just add these names or you make this change, whatever, boom, now it fits in.

**Kirkland Gee:** And I don't have all the details of how to make that work, but I think that makes more sense.

**Colin Lateano:** That's what the dream state was of this, is this is the escape hatch to add componentry that doesn't have native in our WYSIWYG builder, but then you can apply the WYSIWYG parts to it, and can drag it around on site.

**Colin Lateano:** And so, yes, but in our library display, I think toggling between style sheets would be a really slick way to say, look, this is how things can be, here's the style controls you have, here are the classes that can be introduced in this.

**Kirkland Gee:** And if we think about that enough up front, that doesn't be, that's not difficult, right?

**Kirkland Gee:** You do it once really, really well, you make sure all the components follow whatever guidelines, like in theory, not saying it's easy, but like it's not incredibly complicated to do that if you're thinking about that from the beginning versus trying to add something like that in halfway through.

**Kirkland Gee:** Yeah.

**Colin Lateano:** If we were to focus on this, because I know it's a limited amount of people, I would...

**Colin Lateano:** I'd rather focus on this code component part of it, and as we progress, occasionally what's a really cool app example of using these things, but I don't think they have to run in parallel streams.

**Colin Lateano:** I think getting this part done is great, and then bridging together.

**Kirkland Gee:** Okay, so maybe Liz, if you can help me think, be like, what, I guess what needs to happen now for us to get closer, right?

**Kirkland Gee:** Is it something, is it like, does our team need to kind of sit down and do some thinking about this?

**Kirkland Gee:** Are there other people we need to have a meeting with on your side, Colin, to like talk through some of the specifics?

**Kirkland Gee:** Like, what would be the most helpful, like, next thing?

**Colin Lateano:** I think one of the first, I think a couple of the first meetings of actually talking about how we're going to approach this, I want to bring in the new PM lead who is owning the official part of code component and what we're calling DevLink.

**Colin Lateano:** She's very open to this world.

**Colin Lateano:** She's very excited about us building an example set and demo.

**Colin Lateano:** That a good adoption.

**Colin Lateano:** And maybe, maybe they're engineering lead, but honestly, this is primarily a DevRel thing.

**Kirkland Gee:** So I think on our side, we're comfortable.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** There's not like a crazy amount of engineering that kind of needs to happen outside of like writing the components.

**Colin Lateano:** Correct.

**Colin Lateano:** Unless there is capability features that we want to introduce on the import, because part of this, I think, was a very clever idea.

**Colin Lateano:** If we have a, we do have a Webflow CLI.

**Colin Lateano:** So if there is a way to have this, if it, if these components are stored in the repo that is tied to our package, then it would be really slick to be able to do any bash import Webflow CLI of the components you want to import.

**Colin Lateano:** Right.

**Colin Lateano:** And so making sure all that plays together is going to be where there is some engineering on our side to actually engage on.

**Kirkland Gee:** Right.

**Kirkland Gee:** That makes sense.

**Kirkland Gee:** I think that.

**Kirkland Gee:** In my mind, it's like there's quite a few steps before we get there, right, that we could do in the meantime.

**Colin Lateano:** Correct, correct.

**Colin Lateano:** But making sure they're informed is where I'd like to have it kick off once we are ready to start moving on this with them so everyone's aware of all the different moving parts because they might tell us to make that work on their package set, they need to be a month ahead of us.

**Kirkland Gee:** Yeah, right.

**Kirkland Gee:** Okay, I can at least, Liz, like sometime before the end of this week, just like, I don't know, probably just yell at Claude for 30 minutes about all the things that I'm thinking and then try to consolidate that down into like a some, like at least a document of questions to answer at the minimum.

**Kirkland Gee:** And maybe some ideas and opinions and things and that can at least give us something to talk about the next time.

**Liz Kushnereit:** Yeah, we can get this on paper, reschedule this call, get a call scheduled with that PM and then ideally I'd want this all scoped so that by the time we actually kick off the sprint we all know what our tasks are so those are like those.

**Liz Kushnereit:** Things happening before that date.

**Liz Kushnereit:** So no block on that, but I'll follow up async for those pieces.

**Liz Kushnereit:** Yeah.

**Liz Kushnereit:** Great.

**Liz Kushnereit:** Right.

**Liz Kushnereit:** I guess that's it.

**Kirkland Gee:** Cool.

**Kirkland Gee:** Thanks.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** Thanks very much, Colin.

**Kirkland Gee:** Great to meet you guys.

**Kirkland Gee:** Thank you.
