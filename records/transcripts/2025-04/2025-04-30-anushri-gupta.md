# Anushri Gupta

<metadata>
date: 2025-04-30
time: 19:31 UTC
duration: 39 minutes
organizer: Jason Gong
participants: Jason Gong (GrowthX), Anushri Gupta (Webflow), Vic Plummer (Webflow)
fathom_recording_id: 60126174
fathom_url: https://fathom.video/calls/288332999
share_url: https://fathom.video/share/xzEjusURiYSymGF17tCaNiJ94M2LRqWg
source: fathom
enriched_on: 2026-03-04 15:42 UTC
</metadata>

---

## Summary

GrowthX and Webflow discussed a comprehensive developer documentation strategy and visibility initiative. Jason outlined plans to improve Webflow's developer documentation through framework-specific guides, enhanced content architecture, and a new developer-focused publishing area (similar to Webflow University but for developers). Key focus areas include strengthening Designer API documentation, creating guides for MCP server use cases, and building a separate, developer-centric hub where users can discover both Webflow's APIs and general developer knowledge to establish Webflow as a technical authority.

---

## Context

This meeting brought together Jason Gong from GrowthX (a growth agency that works with companies on AI-powered content strategy and developer marketing) with Anushri Gupta and Vic Plummer from Webflow's developer relations team. Webflow is building out its developer offering beyond its core visual builder, expanding APIs (Data API, Designer API, Browser API) and marketplace. GrowthX was engaged to help drive developer awareness and improve how Webflow communicates with technical audiences. The conversation focused on understanding Webflow's current documentation structure and exploring content opportunities that could position Webflow as a developer-friendly platform while capturing search intent from developers researching CMS integration, headless architectures, and API use cases.

---

## Relevance

**To GrowthX Delivery:**
- Webflow operates three separate API documentation sites (Data, Designer, Browser) with distinct audiences: app marketplace builders, in-house dev teams, and front-end developers using custom code. Understanding this segmentation shapes content strategy.
- Designer API documentation is the biggest gap — currently reference-only, lacks framework-specific guides (React, Svelte, Vue), and has poor performance metrics. This represents the highest-impact opportunity for new content.
- Framework-specific permutations of generic guides can be generated at scale (e.g., "Sync CMS data with Airtable" becomes versions for React, Vue, Svelte, etc.), matching Webflow's current code-snippet approach.
- The integrations page is unmaintained with dead content and blank pages — presents both quick-win opportunity (redesign, consolidate) and ongoing maintenance responsibility.

**To CheckThat / AI Visibility:**
- Webflow recently launched MCP (Model Context Protocol) server integration and is tracking adoption; opportunity to create use case stories and documentation around how developers use Webflow + AI tools.
- Metrics tracked include time-to-hello-world (docs visit → successful API call) and API playground usage, suggesting interest in developer enablement analytics.
- Competitor benchmarking: Canva's developer docs praised for organization and content quality; GSAP and Figma plugins noted as reference models. Webflow's docs are seen as strong for Data API but weak for Designer API and cross-framework scenarios.

**To GrowthX Business Development:**
- Account health signals: Vic Plummer and Anushri Gupta are stakeholders in developer product and content; Rachel is driving a parallel headless CMS visibility initiative. This indicates multiple workstreams within Webflow marketing.
- Expansion opportunity: Current developer content serves Webflow users; new "Webflow for Developers" publication could target non-users researching CMS integration and headless architectures (competitor to Sanity, Contentful, Strapi).
- Timeline and commitment: Vic committed to providing a wishlist doc of Designer API improvements within the meeting; calibration article to be delivered within 2 weeks; follow-up meeting planned with prototype of new content area.

---

## Overview

- Webflow's developer docs focus on extending Webflow functionality, not headless CMS use cases
- Designer API documentation needs significant improvement and expansion
- New content ideas: framework-specific guides, MCP server examples, and a dedicated developer learning hub
- Opportunity to create a separate developer-focused content area, similar to Webflow University but for developers

---

## Key Topics

### Current Developer Documentation Structure

  - Separate APIs: Data API, Designer API, and Browser API
  - Documentation includes introductory information, technical structure, and API references
  - Guides section serves as a "kitchen sink" for use cases and examples
  - Marketplace documentation covers app development and optimization

### Developer Audience Segmentation

  - App builders creating marketplace apps for monetization
  - In-house teams building custom integrations for specific company needs
  - Front-end developers using custom code in Webflow
  - Developers creating custom integrations (e.g., syncing CMS data with Airtable)
  - App builders creating Webflow-specific apps or integrations (e.g., Make.com)

### Documentation Performance Metrics

  - Traffic and page views tracked in Amplitude and Snowflake
  - On-page feedback collected
  - Conversion rates for guide pages (users implementing guide instructions)
  - API playground usage monitored
  - Working towards "time to hello world" metric (from docs visit to successful API request)

### Areas for Improvement

  - Designer API documentation needs significant work
  - Lack of framework-specific examples (e.g., React, Svelte, Vue)
  - Limited guide content for Designer API
  - Opportunity to expand MCP server documentation and use cases
  - Need for a showcase or code snippet library

### Content Strategy Ideas

  - Generate framework-specific versions of generic documentation
  - Create a dedicated learning hub for developers (similar to Webflow University)
  - Develop a "developer blog" for more general topics and case studies
  - Improve SEO to capture developers researching CMS integration topics

### Inspiration from Competitors

  - Canva's docs praised for organization and content quality
  - GSAP documentation noted for guidance and learning resources
  - Figma's plugin API documentation structure similar to Webflow's

---

## Action Items

**Vic Plummer**
- Send wishlist doc of designer API docs improvements to Jason

**Jason Gong**
- Create/send content map of current + potential new topics after receiving Vic's wishlist
- Prepare nicer mockup of new developer-focused content area for next week's meeting
- Create calibration article for docs-related content for Vic's review (within next 2 weeks)
- Send recording of note-taker to Vic for both of today's calls

---

## Transcript

**Jason Gong:** Good.

**Jason Gong:** I'm eating melting ice cream.

**Vic Plummer:** That's great.

**Jason Gong:** Is it warm over there?

**Vic Plummer:** Yeah, where are you located?

**Jason Gong:** I'm in Oakland.

**Vic Plummer:** Oh, nice.

**Vic Plummer:** Oh, yeah.

**Vic Plummer:** Nice breezy.

**Jason Gong:** Yeah, it's not like, it doesn't get hot here. At least I've only been here like six months so far.

**Vic Plummer:** Oh, really?

**Vic Plummer:** Where were you before?

**Jason Gong:** But it's sunny. I've been in California for the last eight years, so we were in Mountain View before that. We were in L.A. before that.

**Vic Plummer:** Yeah, but the temperatures are so different in the Bay, depending on where you are, for sure. Super different, yeah.

**Jason Gong:** Whereabouts are you?

**Vic Plummer:** I'm in New York, but I'm in Jersey today.

**Anushri Gupta:** Hey, folks.

**Jason Gong:** I love New York.

**Vic Plummer:** Hello.

**Jason Gong:** Hello.

**Vic Plummer:** Are you late?

**Anushri Gupta:** No problem.

**Jason Gong:** Cool.

**Jason Gong:** So I guess I scheduled this. Let me give you some context on who I am and what I'm doing. Basically, we're GrowthX, a growth agency that uses AI and people to deliver outcomes in growth. Right now we're working with Anushri, Karat, and Rachel on developer awareness through various content forms.

One of the initial ideas was improving your doc site. You guys have a lot of snippets that show how developers use Webflow, and there's an idea of surfacing that content. There are also other ideas around the doc site, so I scheduled this to hear your vision for the docs and understand the structure you think makes the most sense for it. From there, we can figure out where to add new content.

**Anushri Gupta:** So Vic, do you want to go over the structure and how it's designed and why it was done that way?

**Anushri Gupta:** And then we can go from there.

**Anushri Gupta:** Sure.

**Anushri Gupta:** Let me just jump in and share my screen.

**Jason Gong:** Cool.

**Jason Gong:** That'd be awesome.

**Jason Gong:** And then just for background, I lead GoodMarket here.

**Jason Gong:** So I work with like a bunch of clients on one side and then I try to grow growthx on the other side.

**Jason Gong:** So it's a little bit of a dual kind of role.

**Jason Gong:** And then I've worked at a bunch of DevTools companies.

**Jason Gong:** I started a DevTools company.

**Jason Gong:** So I get the value and the importance of docs.

**Jason Gong:** Sorry.

**Vic Plummer:** Hold on one second.

**Vic Plummer:** Oh, my gosh.

**Vic Plummer:** Stop sharing.

**Vic Plummer:** Guys, hold on.

**Vic Plummer:** I'm not very used to Google Meet and it's yelling at me.

**Jason Gong:** I'm sorry. I should switch that for all my calls. There's probably a default somewhere I can toggle.

**Vic Plummer:** Yeah, I think Google is doing it. Okay, can you see my screen now?

**Jason Gong:** Yes, perfect.

**Vic Plummer:** I can't see my screen because there's a huge tab. There we go. Okay, so this is our developer doc site. Actually, this is an older version — we're trying to ship a newer version that shows our different APIs, which would be better to show you.

**Jason Gong:** Please, go ahead.

**Vic Plummer:** Okay, so here we have our developer docs. We're looking at Slack right now.

**Anushri Gupta:** Yeah.

**Vic Plummer:** So we have different APIs.

**Vic Plummer:** We have a data API, a designer API.

**Vic Plummer:** API and a browser API, and then we have references for all of that.

**Vic Plummer:** So here you can see some getting started information or some background information that's like technical structure of the API, as well as the REST endpoints with some organization.

**Vic Plummer:** And then our designer API, we have some introductory information as well, as well as a reference with different reference here.

**Vic Plummer:** We have a browser API that is nascent, and we're actually going to be launching another product that's a developer tool, not necessarily an API.

**Vic Plummer:** And so we're looking to chat about like use cases for that.

**Vic Plummer:** And then we have guides here that kind of put everything all together.

**Vic Plummer:** It's kind of the kitchen sink where we talk about use cases or using different parts.

**Vic Plummer:** So here you can see kind of working with the CMS.

**Vic Plummer:** And so I think these are pretty backed in, like technology specific.

**Vic Plummer:** So instead of saying like, oh, here's a use case of how to sync your CMS with Airtable, it's just like generically working with the CMS so that it can apply to many different use cases, right?

**Vic Plummer:** So it's like, depending on how, but there's a world in which both like from an SEO standpoint and like a use case specific or somebody's looking for it, we could have like, we can generate specific documentation for a tool based off of the general guidance that we have.

**Vic Plummer:** I think that's an area that is like interesting to me.

**Vic Plummer:** And we also like need to expand this because we only have guides right now really much for the data.

**Vic Plummer:** API, and we're working on a designer extension.

**Vic Plummer:** It's just we're shipping a lot of stuff every day.

**Vic Plummer:** We also have information on our marketplace.

**Vic Plummer:** And I think not only do we want to start providing content for how to get started, but then how to be successful, how to optimize to be seen on the marketplace, to get in front of customers, to design your app so that you have monitoring and observability so you understand what your users are doing.

**Vic Plummer:** We want to get to that point where we can be shepherds not only for how to get started with an API, but also just how to be successful and monetize your app since that's what you're usually here for.

**Vic Plummer:** Although we do have, and Jeremy back to the beginning of the beginning, we do have a couple of different audiences.

**Vic Plummer:** So we have an audience that builds apps for a marketplace that they plan on monetizing.

**Vic Plummer:** And then we have an audience of what we call in-house teams, which are people who probably sit in larger organizations who need to build custom integrations for the company they work in for the specific technology that they use or for the specific database that they have or something like that.

**Vic Plummer:** So we don't, like right now, all of our docs really talk to that because our mission when we started was to get apps off the ground as we really talk to those app developers.

**Vic Plummer:** We don't have a lot around those in-house teams, even though they're pretty valuable.

**Vic Plummer:** And then I will pause after this because I've been talking for a while.

**Vic Plummer:** But the last thing I would say is Webflow does have a blog.

**Vic Plummer:** And we do sometimes post content about apps here.

**Vic Plummer:** So let's see.

**Vic Plummer:** So here, this is a corroboration with one of our go-to-market partners.

**Vic Plummer:** And who, like, is saying how to be successful, like we were saying before, like, what does that success driven content look like?

**Vic Plummer:** And they have interviews and quotes from different app developers.

**Vic Plummer:** And we want to do more of this, like, spotlights on app developers and things like that.

**Vic Plummer:** I'm not sure how AI can help with that, because that kind of, like, is definitely more, like, person to person.

**Vic Plummer:** But that's kind of, like, the world of content that I'm thinking of right now.

**Vic Plummer:** But in terms of material to generate things off of, our doc site would be the place to start.

**Vic Plummer:** Yeah, that makes a lot of sense.

**Jason Gong:** I see a lot of, yeah, like, to your point, your concrete example of, like, generally, in your docs, you write generally.

**Jason Gong:** And it's, like, if you want all the permutations of a particular kind of, like, set of instructions, like, we can do that.

**Jason Gong:** Let me think.

**Jason Gong:** Like, so, do you have...

**Jason Gong:** Like, a set of, like, guidelines for, like, what would appear in the docs versus, like, on the blog or in the university, for example.

**Vic Plummer:** So the university, they really tried not to go into code that much.

**Vic Plummer:** And to be quite honest, like, we're going to be speaking to a larger developer audience by the end of the year that some of that is on the university.

**Vic Plummer:** So they really want to keep it simple and just talk to the designer audience and to, like, I guess the beginner audience.

**Vic Plummer:** They have some information on custom code, but, like, everything's caveated.

**Vic Plummer:** Like, hey, we can't help you.

**Vic Plummer:** We can't help you if you do something with custom code.

**Vic Plummer:** Because it's so, like, it's so open-ended that, like, it's not necessarily a troubleshooting Webflow product.

**Vic Plummer:** Now you're troubleshooting someone's specific code.

**Vic Plummer:** Right.

**Jason Gong:** Sure.

**Vic Plummer:** So they'll have, like, so, for example, like, getting a site token Webflow help.

**Vic Plummer:** Yeah.

**Vic Plummer:** Thank you.

**Vic Plummer:** And you guys also have help, and you have the forums as well.

**Jason Gong:** Yeah, I guess we do.

**Vic Plummer:** Okay, let's see.

**Vic Plummer:** So they have an intro.

**Vic Plummer:** They'll say, like, what can I do, how to create a token, how to create a webhook.

**Vic Plummer:** But anything more than that, they're like, go check out the developer documentation.

**Vic Plummer:** Go check out the developer documentation.

**Vic Plummer:** Like, that'll lead you to the developer documentation.

**Vic Plummer:** So somebody will probably see API or webhook in the product UI, no question.

**Vic Plummer:** So it's natural that they would come here instead of the developer go over docs.

**Jason Gong:** Yeah.

**Jason Gong:** So I guess the, like, separation is just like, hey, if I'm in the Visual Builder and I'm, like, not a developer, an app builder, somebody's trying to hook up to Webflow, it's like, I have a CMS or using data API.

**Jason Gong:** Like, I'm in the university and I'm, like...

**Jason Gong:** You know, the Help Center.

**Jason Gong:** But as soon as I, like, cross that into doing something a little bit more technical, I'm on developers.webhook.

**Jason Gong:** Yeah, that's exactly it.

**Vic Plummer:** That's a good differentiation.

**Anushri Gupta:** So like how to use the CMS in Webflow is a university article, but how to, you know, build an integration to take your CMS data into Airtable is more of a developer audience articles because you're not like kind of stepping outside the core designer and doing your writing code essentially.

**Anushri Gupta:** If you're writing code, you kind of get sent out from the university side of things.

**Jason Gong:** And then as far as like how you guys think about these properties, like, are there metrics you guys try to drive or is it more just general kind of paper helping?

**Vic Plummer:** So we have, sorry, we have some stuff set up in Amplitude and in Snowflake and we get on page feedback.

**Vic Plummer:** And that's kind of how.

**Vic Plummer:** So.

**Vic Plummer:** We measure success here.

**Vic Plummer:** So we look at traffic.

**Vic Plummer:** We look at what people are looking at.

**Vic Plummer:** So our introduction, usually it's reference pages, but then like getting started, the guide pages and stuff.

**Vic Plummer:** And then we look at conversion to see, okay, if someone is, ooh, these are better numbers than last time I checked.

**Vic Plummer:** Okay.

**Vic Plummer:** But if someone read a guide, like did they go do with what the guide told them to do in the product, right?

**Vic Plummer:** So what's the considering rate for the guide?

**Vic Plummer:** So let's see.

**Vic Plummer:** And then like our other, the other thing that we look at is we have an API playground.

**Vic Plummer:** So you can play with the API directly from the docs.

**Vic Plummer:** So you just have to like authenticate really quickly and then it'll give you an API key and you can start making calls.

**Vic Plummer:** Another thing that we should be thinking about Anushri is MCP server.

**Vic Plummer:** And like, because we tell people like, oh, that's pretty easy to make calls from there.

**Vic Plummer:** So we do have some content around there, or like very limited, but could be more like use cases for that too.

**Vic Plummer:** This is taking a very long time.

**Vic Plummer:** But this would just show you like how many people are sending requests from those docs.

**Vic Plummer:** And then we're looking, like we're trying to get to a metric of time to hello world, which we don't have locked down yet.

**Vic Plummer:** mean, data support, but basically it's like, okay, from the time somebody visits the docs, like the time that they create an app or a site token to the time that they create, you know, a successful API request.

**Vic Plummer:** Like, what does that look like?

**Vic Plummer:** How do we make it shorter?

**Vic Plummer:** How many people drop off?

**Vic Plummer:** Like, what's that funnel look like?

**Vic Plummer:** That's where we're trying to get to in terms of measure success.

**Vic Plummer:** Would you agree, Anushri?

**Anushri Gupta:** Yep.

**Jason Gong:** That's all really helpful.

**Jason Gong:** I know I have a doc asking for access to all this, and I know that doesn't happen.

**Jason Gong:** Yeah, I actually forgot about it.

**Anushri Gupta:** Last week's been so busy.

**Anushri Gupta:** Oh, When I saw...

**Anushri Gupta:** And I think for this meeting, I was like, oh, there's this access request I forwarded.

**Jason Gong:** all good.

**Jason Gong:** I mean, I think all this can only help.

**Jason Gong:** So I appreciate that.

**Jason Gong:** So I guess one more question, and I can show you, like, maybe what we were thinking about doing.

**Jason Gong:** Like, when you guys say developers, like, what does that really mean in your head?

**Jason Gong:** Because, like, in App Builder, you're kind of extending, like, Webflow's capabilities, but mostly for the Visual Builder CMS audience, right?

**Jason Gong:** Like, yeah, that definition is actively changing as we speak.

**Vic Plummer:** So we really need to talk to all types of developers, from front-end developers who are using custom code in Webflow to create more advanced interactions, like using things like GSAP and adding, like, scripts and stuff that run on the page to people who are, like, Webflow data and sending it out.

**Vic Plummer:** And those custom integrations that we talked about before, like, hey, I'm sending my CMS data Airtable.

**Vic Plummer:** So I'm a four-person shop, and I...

**Vic Plummer:** I do this all the time, or I'm an agency and I do this for my customers, versus app builders who are building things from everything from a small app, or a Webflow-specific app like WhaleSync, to something like Make.com, where they're building integration to serve others and to serve the public.

**Jason Gong:** And lastly, wait, wait, sorry, just, I thought you were going list that last one, but like for Make.com, like, what are you referring to?

**Jason Gong:** Like their template marketplace or like their marketing website?

**Vic Plummer:** So, sorry, sorry, sorry, Make.com has an app integration with Webflow, so people can use Make.com to say, like, when my site is published, do this.

**Vic Plummer:** Want a new CMS?

**Jason Gong:** I see.

**Jason Gong:** Okay, got it.

**Jason Gong:** Got it.

**Jason Gong:** So, like, oh, go ahead.

**Anushri Gupta:** Some of their templates actually use our APIs, you know, their templates to do X with a collection item, and that's using our APIs.

**Anushri Gupta:** So very recently we launched a comments API.

**Anushri Gupta:** Anytime anyone in Webflow adds a new comment, Make has a template where you can say, template was created, what do you do?

**Anushri Gupta:** Comment was created, what do you do?

**Anushri Gupta:** was not.

**Anushri Gupta:** Somebody was mentioned in the comment, they didn't reply within 48 hours, and you can trigger another message, and so on.

**Anushri Gupta:** And so those templates themselves actually use our APIs to do things.

**Anushri Gupta:** Got it.

**Jason Gong:** So, I mean, those three audiences are very much about like extending Webflow's functionality.

**Jason Gong:** I think the audience that initially when you guys talked to developers, I thought you guys wanted to go after was like the same audience that thinks about sanity and contentful and strappy.

**Jason Gong:** Like, do you guys care about that audience at all?

**Jason Gong:** Like people using Webflow in that way?

**Anushri Gupta:** That's a separate workstream.

**Anushri Gupta:** For us, it's mostly around people.

**Anushri Gupta:** And then when we go into that headless CMS conversation, that's something that, you know, we're also interested in.

**Anushri Gupta:** And that's going to be, I mean, maybe it gets merged into that, you know, other property that you were showing me.

**Anushri Gupta:** Maybe that's what happens here.

**Anushri Gupta:** But like for us, our main focus has been people who are extending Webflow.

**Anushri Gupta:** Oh, got it.

**Anushri Gupta:** That's actually really helpful.

**Jason Gong:** So, and then main focus, meaning like focus of the docs.

**Jason Gong:** Yes.

**Anushri Gupta:** And the focus of this team, to be honest, focus for my team.

**Anushri Gupta:** Oh, okay.

**Jason Gong:** That's actually really helpful.

**Jason Gong:** Then, I mean, could I just ask like the people that's thinking about using Webflow and promoting it more as a CMS, like what does that look like?

**Jason Gong:** Is it just like a completely separate team under product marketing?

**Jason Gong:** Oh, exactly?

**Jason Gong:** Yeah.

**Vic Plummer:** I couldn't tell you.

**Vic Plummer:** I'm sorry.

**Jason Gong:** I'm I can

**Anushri Gupta:** So I think that's just, that's one of the initiatives that Rachel's kind of doing.

**Anushri Gupta:** It will fall under this umbrella.

**Anushri Gupta:** So it'll be me working on it.

**Anushri Gupta:** I also don't have a lot of detail.

**Anushri Gupta:** I think it's just something she wants to do as part of this initiative to look like, you know, yeah.

**Jason Gong:** Yeah, because it was brought up at beginning.

**Jason Gong:** So I'm trying to like fit it all together.

**Jason Gong:** Because I guess the reason to schedule this call is just like, it's a lot of content and search intent to get in front of.

**Jason Gong:** And I want to avoid a situation where we're just like, putting content here and there, and then our dev site just becomes kind of like a mess.

**Jason Gong:** So just understanding kind of where things should be is helpful.

**Jason Gong:** Okay, so that makes sense.

**Jason Gong:** I'm trying to think if there's anything I want to ask.

**Jason Gong:** I mean, I can share like, just with you, Vic.

**Jason Gong:** I know you haven't been on the other calls.

**Jason Gong:** I'm not sure if you've watched them at all.

**Jason Gong:** But No, I haven't.

**Jason Gong:** Oh no, not at let me just show, I guess, what we're doing there, I'm sure I think we're safe, but I'm sorry, let me just show what we're doing, time screen, cool.

**Jason Gong:** So, yeah, I mean, I guess like you, like our scope is like fairly broad, like we're just trying to help drive developer awareness, I think what that has looked like currently is like we have this idea of just making the integration docs better, because right now they're, it's just like a heading with like two buttons, so like very low hanging fruit there, but also- Oh, yeah.

**Jason Gong:** Thank you.

**Jason Gong:** Thank you.

**Vic Plummer:** So much better, thank you.

**Vic Plummer:** This is the old integrations property.

**Vic Plummer:** Oh, yes, that integrations page that drives me nuts.

**Jason Gong:** What's your take on the integrations page?

**Jason Gong:** It's not actively managed, so there's a lot of dead content out there.

**Jason Gong:** There's no content, actually.

**Jason Gong:** I think a number of those pages are just blank.

**Vic Plummer:** So before we had an app marketplace, this is where we would say, hey, we don't officially support this integration, but you could try to put it together, or you could follow the other people's docs.

**Vic Plummer:** So there's a very dedicated group of people who would keep up to date about who supported things for Webflow.

**Vic Plummer:** Oh, and does that group still exist?

**Vic Plummer:** I think the person who did it still is at Webflow, but I don't think that's not part of their remit anymore at all.

**Vic Plummer:** So they might be able to give you context on how this came to be, but not necessarily on how it's managed.

**Vic Plummer:** Right now, I think that's

**Vic Plummer:** This is a great guard page.

**Vic Plummer:** Got it.

**Jason Gong:** Well, okay, we're bringing in some life.

**Anushri Gupta:** Yeah, it's a hot potato.

**Anushri Gupta:** People just pass it on.

**Anushri Gupta:** It's not mine, it's yours.

**Anushri Gupta:** It's not mine, it's yours.

**Anushri Gupta:** So I think, actually, that's good information, Vic.

**Anushri Gupta:** I'll ask you who it is.

**Anushri Gupta:** And starting, Jason, we could probably just build it in.

**Anushri Gupta:** I mean, it is built in Webflow, so it's probably managed with EMS, and it might just be a matter of adding more fields or reference.

**Anushri Gupta:** So we just work with that.

**Jason Gong:** For the sake of moving quickly, we have a designer, and we just come in and set it up and get your approval before we go live.

**Jason Gong:** Or if you guys have somebody, we'll be happy to do some.

**Jason Gong:** Cool, so that's thread one where it's very concrete.

**Jason Gong:** And then the other one is just kind of directional, like build more awareness with developers.

**Jason Gong:** Last week, I guess some of the ideas we've talked about, kind of the way.

**Jason Gong:** You mentioned, let's see, kind of like taking a generic documentation kind of like path or like area and then just doing it for all the most popular permutations of that, like whether it's integrate with a tool or like integrate with like a framework or use case.

**Jason Gong:** So that's one that we're doing, I guess, from this conversation.

**Jason Gong:** I guess I can sit.

**Jason Gong:** Oh, sorry.

**Jason Gong:** I was on mute.

**Jason Gong:** think that's super interesting.

**Vic Plummer:** Right now, like we do all of my code snippets for like anything when I create like app examples and is in React and in Next.

**Vic Plummer:** And know that one of our engineer, our dev role engineer, Zach, he has like done some things in Astro, but we really kind of keep it framework-like because of like it's a small team and we have specific expertise in certain areas.

**Vic Plummer:** So I think that is actually something that would be incredibly helpful because.

**Vic Plummer:** So

**Vic Plummer:** Most of our code snippets are really just, like, we know a lot of people work in Svelte, and I don't have experience in Svelte.

**Vic Plummer:** I'm trying to ramp up on that.

**Vic Plummer:** So, like, that would be nice to provide.

**Vic Plummer:** So, yeah, I think the, is the localization one, does that have, maybe one more if you go down?

**Vic Plummer:** Yeah, so you'll see the code snippets there.

**Vic Plummer:** Oh, like these?

**Jason Gong:** Yeah.

**Jason Gong:** Hmm.

**Jason Gong:** I feel like they should be, like, use case.

**Jason Gong:** I guess it really depends on the type of snippet.

**Jason Gong:** like, okay.

**Jason Gong:** Oh, sorry, go ahead.

**Vic Plummer:** No, I think, like, if we could think of a different type of architecture for this site, because, like, Guides is really a kitchen sink right now.

**Vic Plummer:** But, like, I do like the idea of having, like, generic, like, here are the fundamentals and the basics of how this technology works or how this API works so that, like, you can understand the different quirks, the different errors that you might expect.

**Vic Plummer:** Although, with your technology, you'd be able to do that across all frameworks.

**Vic Plummer:** But I do think that there's like a benefit in having like a generic one that focuses on the technology itself versus like how that technology can be applied to different use cases.

**Vic Plummer:** But that is a different story.

**Jason Gong:** I think that's where my head's at.

**Jason Gong:** Just like, let's figure out all the homes for things.

**Jason Gong:** I think the like docs, I mean, reference, we probably won't really touch at all.

**Jason Gong:** But like within the guides, it feels like, you know, here's the reference, but like, here's some examples or here's like kind of the, how you would use, I guess, one of the endpoints.

**Vic Plummer:** I think our biggest opportunity, to be quite honest, like, I think people pretty, are pretty, are cooking with our data API.

**Vic Plummer:** I think our designer API needs the most work.

**Vic Plummer:** So if you click that top, if you click that and go to designer API.

**Vic Plummer:** So this is how people create designer extensions that run on top.

**Vic Plummer:** And I'm sorry, this happens.

**Anushri Gupta:** We're trying to fix this.

**Vic Plummer:** So guides are a kitchen.

**Vic Plummer:** They're for everything, but if you go to the reference, yeah, if you go to the reference, that'll be specific to the designer, and you can see here that these are specific for apps.

**Vic Plummer:** have to fix that button, but, like, these are the different methods that will run in Webflow, but then, like, you're going to, someone would create, like, a React or a Selt or a Vue app to, like, kind of house this, and it'll run, like, it'll run in the iframe, and then they'll use these methods that run in the browser to make the changes on the Webflow designer, and so that whole process, one, is, like, pretty abstract.

**Vic Plummer:** It's pretty hard.

**Vic Plummer:** I'm explaining it right now, but I need to kind of explain this better in the docs of, like, how A plus B equals C, but also, like, there's so many steps from, like, just creating an app to then applying, like, app and logic and stuff like that, and then applying the Webflow APIs on top of that, and I think that we, there's so much.

**Vic Plummer:** There's an opportunity.

**Vic Plummer:** It's actually like our docs, our data APIs perform really well.

**Vic Plummer:** Our designer API content does not perform that well.

**Vic Plummer:** And that's something that I would like to improve with the opportunity.

**Vic Plummer:** I see.

**Jason Gong:** And when you say perform well, meaning like people that read these generally don't like continue to like do the action that you want?

**Vic Plummer:** Honestly, I don't think like I don't even think I have conversion metrics for the designer API right now because it's mostly just.

**Vic Plummer:** Reference content at the moment.

**Vic Plummer:** There's not guide content yet because I just have not been able to get that out.

**Vic Plummer:** But so like I'm even saying that that's how standard and how much work is needed there is like I don't even have the guide content that I have for the data API.

**Vic Plummer:** And then on top of that, like there's a whole layer of, OK, well, what if you're using next?

**Vic Plummer:** What if you're using spell?

**Vic Plummer:** What if you're view or posture?

**Vic Plummer:** So like.

**Vic Plummer:** Well,

**Vic Plummer:** I think there's so many different permutations of what that could look like.

**Vic Plummer:** That's a place that I feel like it's a I think it would be really helpful if you had a wish list.

**Jason Gong:** I think it's mostly trapped in your mind.

**Jason Gong:** Or if you do have a doc, then just sharing that of things you've wanted to do for a while or ideas that you had but just not had the time.

**Vic Plummer:** I have a doc somewhere that I can pull out.

**Jason Gong:** That would be really helpful.

**Jason Gong:** Yeah, something I would have to send to you. I can pull that out later.

**Vic Plummer:** Yeah, and are you good?

**Anushri Gupta:** Sorry, Jason.

**Anushri Gupta:** I will add one more thing here.

**Anushri Gupta:** In addition to this, our MCP servers kind of gained some traction.

**Anushri Gupta:** We recently released it.

**Anushri Gupta:** So it would be really good to have some stories around that use case.

**Anushri Gupta:** And it will be nice to have some stories around, like, well, it needs some.

**Anushri Gupta:** Research, first of how are people using Webflow's MCP server, and then, like, just having, I mean, it's so early right now, just having some ideas for people to look at and use would be, and then maybe we do a series around that, too.

**Jason Gong:** Yeah.

**Jason Gong:** Yeah, really good.

**Jason Gong:** Do you know if there's, do you have any competitor that you think has kind of better docs in any one of these areas or resources?

**Vic Plummer:** Oh, I like Canva's docs content.

**Vic Plummer:** I don't love their structure.

**Vic Plummer:** Canva.dev.

**Vic Plummer:** I like them because they're closest to us because they have a canvas that they have to develop for.

**Vic Plummer:** Yeah.

**Vic Plummer:** I think it's good.

**Vic Plummer:** I think it's well-organized.

**Vic Plummer:** They did just launch an MCP server.

**Vic Plummer:** Yeah.

**Vic Plummer:** I think it's think

**Vic Plummer:** Shopify's docs are a lot.

**Vic Plummer:** The thing about them is that you can find what you need because they have so much content, but you're just searching for it.

**Vic Plummer:** You're not looking through an organizational structure or a learning path.

**Vic Plummer:** You're not going to go down each doc list or something like that and have a progressive learning journey.

**Vic Plummer:** You're just going to search for what you need when you run into an error.

**Vic Plummer:** So I like Canvas docs.

**Vic Plummer:** I'm not a big fan of Figma's docs, but people use it and they build a bunch of plug-ins, so it is working.

**Vic Plummer:** Oh, that's different.

**Vic Plummer:** It's funny their docs don't rank when you search for Figma's docs.

**Jason Gong:** I just felt to crush that because he always gets mad at me.

**Vic Plummer:** Okay, yeah, so you go to their plug-in API.

**Vic Plummer:** So they have a bunch of different things, yeah, and so this is their docs.

**Vic Plummer:** Yeah, the same architecture.

**Jason Gong:** So they have a guide, you have the reference, and then you have the blog.

**Vic Plummer:** So I would say I really like Canvas a lot.

**Vic Plummer:** I think they did a great job.

**Vic Plummer:** Yeah, it's really – that's what I looked at.

**Vic Plummer:** And I like GSAP docs as well.

**Vic Plummer:** And they're a Webflow company, which is nice.

**Vic Plummer:** So we can pull off of them.

**Vic Plummer:** But they are just – they're a completely different product.

**Vic Plummer:** So they are, like, they're an animation library that runs in the browser.

**Vic Plummer:** So it's not – they don't have API endpoints and stuff like that.

**Vic Plummer:** But they do have, like, a lot of guidance and learning.

**Vic Plummer:** It's nice.

**Jason Gong:** Okay, got it.

**Vic Plummer:** Yeah, and I think actually – and I know we're a little bit over.

**Vic Plummer:** But that is something that we – I really been longing for is, like, a showcase.

**Vic Plummer:** Or, like, – like, we have an app marketplace.

**Vic Plummer:** But, like, off interesting tidbits or pieces that people use.

**Vic Plummer:** It's hard because, like, with Meet and Webflow and Webflow.

**Vic Plummer:** People are publishing Webflow sites to do this.

**Vic Plummer:** But I think like what you were saying before about code snippets or exhibit library, I think that would be our version of that.

**Jason Gong:** I'm trying to think about the scope — how much of the front end can you show with just a snippet? It depends on the example.

**Vic Plummer:** I would say Wix.dev is a reference. Instead of a showcase of user-generated content, I think we'd have code snippets we created ourselves.

**Jason Gong:** Yeah, those are all really good. So as a next step, if you send that wishlist, I'll create a map of what we have today.

**Jason Gong:** And then like all the different topics we think we could add and what that structure would look like.

**Jason Gong:** Okay.

**Jason Gong:** Okay.

**Jason Gong:** Okay.

**Jason Gong:** Yeah, that's awesome.

**Jason Gong:** So that would be one.

**Jason Gong:** And then the other thing I brought up to Anushri on our call today was like, the docs make sense for things that are related to the docs specifically.

**Jason Gong:** But like, let's say you had a general topic, like, you know, the best way to migrate from A to B or something like something that relates to like your APIs.

**Jason Gong:** Where would that live?

**Jason Gong:** And today there is no home.

**Jason Gong:** So I think I proposed having a home for that here.

**Jason Gong:** I think what the URL is, that stuff that works out, but like slash learn or slash, you know, something.

**Vic Plummer:** Yeah, so that would be great.

**Vic Plummer:** Right now, like, I think if anything that we would add, like we'd have it on Webflow's blog, but we're already pushing the limits there.

**Vic Plummer:** So yeah, we would have a developer's blog.

**Vic Plummer:** We also do have an engineering blog.

**Vic Plummer:** That's actually a great, I like that on their documentation.

**Vic Plummer:** I didn't even see that.

**Vic Plummer:** But that's more of a recruiting strategy.

**Vic Plummer:** We don't, I haven't touched that in a while.

**Vic Plummer:** Is it this or is it a separate thing?

**Jason Gong:** No, that's an interesting blog, yeah.

**Vic Plummer:** it's separate.

**Jason Gong:** like a tag within their blog.

**Vic Plummer:** Yeah.

**Jason Gong:** Interesting.

**Jason Gong:** Yeah, I mean, I...

**Anushri Gupta:** Well, and I were talking this morning about how, I think, was striked our task.

**Anushri Gupta:** Yeah, like...

**Jason Gong:** Go ahead.

**Jason Gong:** No, sorry, I'm so sorry, I keep cutting you up.

**Jason Gong:** No, no, no.

**Jason Gong:** Oh, you go ahead.

**Jason Gong:** Yeah, but basically, I guess my take from the high-level, like, marketing, product marketing side of this is, like, your content today is not for developers.

**Jason Gong:** Like, when I land on glossary, blog, or university, it's crystal clear to me this is written for people using the visual builder, not for developers. And I think even Stripe has this problem — you'd assume their content is for developers, but they also need a place where if I'm a developer, I land on it and immediately trust it's for me.

**Jason Gong:** And I think for Webflow, similar to, I mean, looks like Cam already has the right idea.

**Jason Gong:** Like we need to have that, I think.

**Jason Gong:** And then that's where you build like non-brand awareness for some of these concepts that you guys are trying to push.

**Jason Gong:** Like some of these ways of using Webflow.

**Jason Gong:** So again, when somebody searches for something general, like right now, if they search for Webflow, you know, connect with Next.js or something, like they're going to land on your property because they search for Webflow.

**Jason Gong:** But like, if I'm just researching, like, you know, as a developer, what are the best ways to like integrate a CMS with my like Next.js website?

**Jason Gong:** They're not going to land on your website, you know, and they probably don't want to land on your blog because like as soon as you land on it, you can tell.

**Jason Gong:** So it's like, yeah.

**Jason Gong:** Yeah.

**Jason Gong:** Yeah.

**Jason Gong:** you.

**Jason Gong:** So, yeah, so that's what we're thinking.

**Jason Gong:** And then next week, I vibe-coded something very ugly, which I'll just show you.

**Jason Gong:** But I think I'm almost thinking about it as, like, a publication.

**Jason Gong:** Can you see Miller?

**Jason Gong:** Yeah.

**Jason Gong:** Okay.

**Jason Gong:** Again, very ugly.

**Jason Gong:** But, like, you know, similar to Stripe.

**Jason Gong:** Like, I think that's what I'm imagining.

**Jason Gong:** Next week, I'll show something a little nicer.

**Jason Gong:** I just wanted to, like, see if this was an idea you guys were on board for.

**Jason Gong:** And with Karat, I think a lot of what we're doing is about enablement. The integrations piece assumes I'm already a Webflow user.

**Vic Plummer:** Absolutely.

**Vic Plummer:** Same with the docs.

**Jason Gong:** But then we want to make it more organic.

**Jason Gong:** Like, let's capture people that aren't even using Webflow, you know, or thinking about Webflow.

**Jason Gong:** And they're just researching some topic that you want to be an authority in, basically.

**Vic Plummer:** I mean, that's how universities started and got huge, right?

**Vic Plummer:** Like, they taught people the basics of web development.

**Vic Plummer:** And then how to apply those concepts to Webflow.

**Vic Plummer:** So, yeah, we definitely think about it from that end of the spectrum.

**Jason Gong:** Yeah, so basically university, but for developers.

**Jason Gong:** Yeah, so I think that's something, and I think that covers all the topics I can think of.

**Jason Gong:** Like, if it's docs-related, it's on the docs.

**Jason Gong:** If it's more general, it'll live on slash learn or whatever we come up with.

**Jason Gong:** I think we can even do our developer stories here.

**Anushri Gupta:** I mean, we have trouble getting it on the Webflow blog.

**Anushri Gupta:** They're so busy, they have so much more content, and then, you know, we can do some features here, too.

**Jason Gong:** Yeah, for sure.

**Jason Gong:** And we have, like, I can't remember what the question was, but, like, we do have kind of workflows for that.

**Jason Gong:** Like, we don't generate stories out of thin air, but essentially what you would do is, like, do a Zoom call.

**Jason Gong:** We do like-

**Jason Gong:** We would have a list of questions, and then we would take that at the base, and then we would create a case study, developer story with it, essentially.

**Jason Gong:** Okay, cool.

**Jason Gong:** I think that was really helpful.

**Jason Gong:** I can't think of any other questions at the moment, but it sounds like anything docs-related.

**Jason Gong:** So just for our process, we'll do a calibration article at the beginning just to show you guys and set the bar for quality.

**Jason Gong:** So it sounds like for anything doc-related, that'll be you, Vic. Is that accurate?

**Vic Plummer:** Yeah, yeah.

**Jason Gong:** Cool. So expect that in the next two weeks.

**Vic Plummer:** Awesome. I'll send you the wishlist stuff.

**Jason Gong:** Yeah, that'll be awesome.

**Vic Plummer:** Would you mind sending me a recording of the note-taker?

**Vic Plummer:** We cover a lot.

**Vic Plummer:** I just want to make sure I remember.

**Jason Gong:** Sounds good.

**Jason Gong:** I'll do that for both calls today.

**Jason Gong:** Thank you.

**Jason Gong:** Amazing.

**Vic Plummer:** All right.

**Vic Plummer:** Awesome.

**Jason Gong:** Well, have a good rest of your Wednesday. I'll see you all soon.

**Vic Plummer:** All right, thanks.

**Jason Gong:** Have a good one.

**Anushri Gupta:** Bye-bye.
