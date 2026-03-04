# Adrian | Dave

<metadata>
date: 2025-05-15
time: 21:02 UTC
duration: 26 minutes
organizer: Dave Capone (GrowthX)
participants: Adrian Machado (Zuplo), Dave Capone (GrowthX)
fathom_recording_id: 62967504
fathom_url: https://fathom.video/calls/302536006
share_url: https://fathom.video/share/r37rQcCKi-avmZ6v-q_RVjb_x1GzznQs
source: fathom
enriched_on: 2026-03-04 12:45 UTC
</metadata>

---

## Summary

Adrian (Zuplo) and Dave (GrowthX) aligned on ownership for an API directory project that will drive Zuplo's contract renewal decision. GrowthX will generate content, categorize APIs, retrieve logos, and handle P1 deliverables (summary, benefits, categorization, logo, OpenAPI spec), while Zuplo provides the initial dataset and handles P2 items like pricing pages and Postman collections. MVP target is 12 pages by end of May, with a full launch planned for early June before Zuplo's renewal decision.

---

## Context

Zuplo is an API management platform that GrowthX currently works with under a contract up for renewal in June. Adrian raised the API directory project as a test of GrowthX's PSEO (Programmatic SEO) capabilities at scale—specifically whether GrowthX can generate high-quality content pages for hundreds of APIs programmatically. This is a strategic bet: if the directory launches successfully with strong content quality, it becomes a key value prop in Zuplo's renewal decision. Adrian is focused on creating value beyond just traffic, including leveraging OpenAPI specs to upsell Zuplo's open-source projects. The project is ambitious but intentionally scoped to test GrowthX's content engine before committing to larger-scale PSEO workflows.

---

## Relevance

**To GrowthX Delivery:**
- New PSEO workflow scaling opportunity: the API directory tests whether GrowthX can generate consistent, taxonomy-driven content at scale (targeting 100+ pages long-term)
- Content engine must handle category selection from a taxonomy, competitor identification via domain scraping, and Brandfetch logo API integration—all novel requirements
- Early May deadline creates urgency for Dave to sync with Daniel on dev resource allocation and integrate new team members recently hired

**To CheckThat:**
- API specifications are a key downstream asset: Adrian plans to use OpenAPI specs to generate documentation, security scores, and mocks via Zuplo's open-source tools
- This strengthens the positioning that GrowthX/CheckThat can move beyond traditional content into technical asset generation

**To GrowthX Business Development:**
- Contract renewal hinge point: Adrian explicitly tied the API directory launch to Zuplo's June renewal decision; delivery by end of May is critical
- Upsell opportunity: if the project succeeds, GrowthX can pitch similar PSEO workflows to other developer-focused SaaS clients
- Reference potential: if the directory drives qualified traffic and conversions for Zuplo, it becomes a referenceable case study

---

## Overview

- Zuplo to provide initial API dataset (name, domain, docs URL)
- GrowthX to handle content generation, categorization, and logo retrieval
- MVP (P1) target: \~12 pages by end of May; full launch early June
- JSON export as deliverable for Zuplo to ingest and display

---

## Key Topics

### Project Scope and Responsibilities

  - Zuplo provides:
      - Initial API dataset (name, domain, external docs URL)
      - Category taxonomy for GrowthX to apply
      - OpenAPI specs and Postman collections (when available)
  - GrowthX handles:
      - Content generation using provided context
      - API categorization based on Zuplo's taxonomy
      - Logo retrieval (likely using Brandfetch API)
      - Scraping additional metadata when possible

### Priority Features

  - P1 (MVP): Summary, key benefits, categorization, logo, OpenAPI spec
  - P2: Alternatives, documentation images, pricing page, Postman collection
  - Future: Performance metrics, popularity scores (likely via partnerships)

### Timeline and Deliverables

  - Target: \~12 pages by end of May
  - Full launch: Early June (before Zuplo's GrowthX contract renewal decision)
  - Deliverable: JSON file export for Zuplo to ingest and display
  - Iterative feedback process starting next week

### Strategic Value for Zuplo

  - Leverage OpenAPI specs to upsell Zuplo's open-source projects
  - Generate API documentation, security scores, and mocks
  - Warm leads for potential long-term conversion to Zuplo's ecosystem

### Data Sources and Scraping

  - Utilize provided API marketplaces for initial data and cross-referencing
  - Use domain as a "join key" between first-party and third-party information
  - Leverage existing data to shortcut manual processes where possible

---

## Action Items

**Adrian Machado**
- Allocate time for website build-out to showcase API pages

- Provide additional API list to Dave for project expansion


**Dave Capone**
- Add list of APIs provided by Adrian to project

- Export project data to JSON file for Zuplo ingestion

- Share initial content with Adrian early next week for review

- Sync with Daniel re project requirements & dev resource allocation

---

## Transcript

**Dave Capone:** This meeting is being recorded. So for this meeting, what I wanted to do was just go through the properties and really just define who the owner is.

**Adrian Machado:** I went through and I did a rough draft of it.

**Dave Capone:** I'll go ahead and share the screen of what I thought each could provide. And then we can just say, okay, yeah, that's true. Or no, I want you guys to take care of that. And we'll go from there. So do we want to just go through verbatim?

**Adrian Machado:** I think that's fine. We can start verbatim. Can you scroll to the sidebar? Because it's a little bit off center for me.

**Dave Capone:** Okay. I got a super ultra wide screen.

**Adrian Machado:** Oh, that's why it was clipping. Yeah. Because you have a ton of margin on one side. Yeah. Most sites don't handle it very well at all. I used to do an ultra wide, but it's just like so many webpages are just so ineffective. So now I do a dual monitor setup, which gets me a similar effect.

**Dave Capone:** Yeah, yeah. All right, so the API name, is that going to be on you to provide or on us to provide?

**Adrian Machado:** So I think the way we'll start with stuff at a high level—I think we can generate a good list of APIs for you to pursue. That would probably consist of the name of the API and the domain of that API. We'll start with a repository, and as we covered in the article, there are many other repositories out there that we can kind of clone to build essentially an initial dataset of APIs to generate. So yeah, I'm fine handling that. The three most pertinent properties are: the API name (good for titling the article), the domain (probably the most important because that's the primary source of information for how the content engine cites stuff), and the external API documentation. I don't want to say the content engine can't cite anything outside of that domain, but I would strongly encourage it to cite first-party information. In many cases, stuff found outside the domain might be out of date. If you're talking about Stripe's API, you should get it from the horse's mouth.

**Dave Capone:** So that's going to be on us then, right?

**Adrian Machado:** I would provide you with the domains. Yeah, exactly. I don't know how this gets fed into the content engine. That's opaque to me. But you need to make sure that the domain gets used for citations and data sources, whether that's through prompting the content engine or whatever. And the external API documentation—I mean we would provide the link to their specific API docs. The core thing is a page with a rendered version of the specification: endpoints, use cases, languages supported, SDKs. I'm fine providing that as well. It shouldn't be too much manual work on our side. Usually it's standard like, whatever-company.com/api or /docs/api. It's almost all schematized, so that's fine to provide.

**Dave Capone:** And then moving into, I think what makes sense is for me to cover the ones I think that we should handle first.

**Adrian Machado:** That's fine. Can you scroll a little bit further down so you can see more of the table? So the other stuff for us to cover here: API alternatives. I think that's probably going to be a combination between us in most cases. In terms of context clues, what competitor APIs would be relevant? Well, you already know the website. Let's say we're talking about Stripe here. Stripe has comparison pages to other platforms, right? So you can determine what companies are competitors. Then you can ask: do they have an API already in our dataset? If so, it's worth mentioning. So it's a little bit of a collaboration between us on that.

**Dave Capone:** So as we're gaining context of all these different APIs, GrowthX will provide competitors based off of the URL domain. We'll scrape and gain context via the domain.

**Adrian Machado:** Yep. So if we feel that isn't working out, then maybe I need to do it more manually in some cases. It really depends on the quality of the results here. Moving forward to categorization: I'm going to provide a taxonomy to use. When I say taxonomy, ideally it's a tree structure, but it might end up being flat. You know, categories like animals, payments, fintech—whatever it is, I'll provide all the categories. What I'd be interested to see is if the content engine is capable of picking the appropriate category from that list based on context clues. This is what we do with tagging in our regular blogs: I provide the content engine a list of tags with descriptions, and then you pick one to use.

**Adrian Machado:** So I think this is something you guys are probably already capable of.

**Dave Capone:** I think through the researcher it should be able to figure it out. Between context and researcher, I'm pretty sure you can figure out a category to put this in.

**Adrian Machado:** Exactly. Yeah, there's plenty of signals that you'll get to understand where it should go. Logo—I think this one will probably be the most difficult. I've spoken to Marcel about this. He used a tool called Brandfetch when he did DeepGram's AI index. Brandfetch is an API where you enter a company name and it pops out a logo for you. It's very nice, gives you PNG or SVG. So it might be worth using. As for who should own it: is this something you need to be using more regularly within other PSEO workflows for your other customers? Maybe that makes more sense for you guys to own it to take advantage of scale. Or maybe it makes sense for us to own it if no one else you're working with wants to do logos at scale.

**Dave Capone:** Yeah, I think we'll take that one because if there's an API, I want to build a workflow around it. If we're doing these programmatically, we should be able to build a workflow, hit Brandfetch for this variable which is the company, and then dynamically pull it in and grab it.

**Adrian Machado:** That should be fun. Yeah, I think that's immensely useful for other customers too, so it makes sense. What else is on here? The pricing page. That one, I think maybe you'll be able to scrape this, but it might need to be manual. Typically pricing is on the base domain with /pricing at the end. Sometimes APIs have their own pricing or aren't included in the package. I think Jen has been playing around with this on our current API articles, trying to figure out what's included. So I would maybe talk to her to see how well the content engine can handle this. In the worst case, it would probably be just the URL to their pricing page. But it seems like you guys are actually capable of this based on the current API articles you're producing.

**Dave Capone:** Got it. Can understand pricing?

**Adrian Machado:** Yeah, exactly. When it comes to the OpenAPI specification and Postman collection, this will actually be kind of difficult. I think scraping it should be doable in many cases, but I'm going to reverse this process. I'm going to provide you with specifications from an existing repository upfront to make this as easy as possible. For the first 100 articles or so, I can probably provide you with specs from an existing repository of known specifications. Postman collection is also going to be on us. You can potentially scrape this as well. But if you can't find it, I think we'll always be able to provide a fallback.

**Dave Capone:** Okay. So then these two seem like the most difficult: performance metrics and popularity.

**Adrian Machado:** Yeah, so those are going to be on us. I think these are going to be P2 as far as priority goes. I wanted to include them to illustrate the direction we want to go—these pages should be more than just informational. They should actually provide value to users. But this is very much going to start as a manual process where I'll have to sign up for these APIs and actually test them out. There are other pages we can scrape to get some of this information, but yeah, it's going to be manual and not super high priority.

**Dave Capone:** Cool. And I think you could back your way into a popularity score by tracking the number of visits to one of those landing pages and just apply it as popularity—most visited or something like that.

**Adrian Machado:** Yeah, exactly. Performance metrics is going to be tough. Don't expect that from you guys. What will most likely happen is if this becomes popular, we would partner with another company that does API performance metrics. They would give us an API to get the data directly so we can upsell the service. But you've got to crawl, walk, run.

**Dave Capone:** All right. So can we just go through priorities for P1 and P2? What will be MVP and what will be the version after that?

**Adrian Machado:** Yeah, exactly. Starting from the top here, I think P1 is the summary, key benefits, and getting started. Alternatives I would say P2, especially because it's going to be more difficult. Images of documentation I'd say P2. It's good to have some images, but the logo is probably more useful. Categorization is P1. If we don't start with taxonomy, it's very hard to retroactively apply. Logo, I want to feel like that's P1, but it depends on how Brandfetch works. Pricing page is P2. Specification is P1 for us, and I'll explain why.

**Dave Capone:** Postman Collection is P2.

**Adrian Machado:** Got it. So as for why the specification is so important for us: we actually use that specification to help upsell our open-source projects. This is what I mean by actually gaining value from these pages other than just traffic. API specifications are large YAML or JSON files that include a machine-readable way of understanding an API's capabilities—endpoints, features, etc. We take that format and use it to generate API documentation using our own open-source API documentation tool. We generate scores for those APIs based on security and other factors, and we would want to put these scores and links into the page itself. I'm able to handle that because I've already created APIs for doing all of these things. We just need the specification to generate that stuff, plus mocks for those APIs. So it's very much about upselling different open-source services that Zuplo already offers. Once we get them into our ecosystem, they become warmer to the Zuplo brand, and I think that could potentially lead to long-term conversion. That's my whole strategy here—rather than just purely upselling Zuplo, I want to approach it from different angles.

**Dave Capone:** Provide value. Got it.

**Dave Capone:** All right. So my next question is: what's your deadline on when you want this project to go live?

**Adrian Machado:** Yeah, I feel like we would want to get the first set of pages out by the beginning of next month. Let's say a dozen pages. Why the beginning of next month? Our GrowthX renewal is coming up in June. I think we need to decide then. This project is going to be pertinent to our renewal decision. I mean, one of the first reasons we started working with GrowthX was talking to Marcel about the concept of PSEO and scaling it out. The challenge has been getting the content engine in great enough shape to actually execute on this idea. It's not infrastructure we want to own—generating these pages with the content engine. So for continued success, we see the PSEO API directory as one of the key value props of our continued relationship with GrowthX. So if you can deliver by end of May, that would be crazy good. Let's say it isn't great and we're like, "Oh man, this is super sucky with what Dave produced." Then we would be able to give you guys a 30-day notice. But ideally, end of May would be the best time to have a dozen pages. Will they be indexed by then? I don't know. That's going to be tough. But I can certainly allocate time for building out the website and stuff like that. I can probably do that in a few days.

**Dave Capone:** I just need the metadata. So I will add to this the list of APIs that you gave me today. So the export of this is going to be a JSON file. We're going to take all of this and export it to JSON so you can ingest and paint it on your pages, or throw it in a database, however you're going to utilize it.

**Adrian Machado:** Yeah, exactly. That sounds great to me.

**Dave Capone:** Okay, deliverable JSON file. And then we'll have iterations because I'll start sharing content with you soon. I'll go through early next week, figure out if we're on the right page or not and get them to a point where we feel good about them.

**Adrian Machado:** And we'll go from there.

**Dave Capone:** So I'll start working on this and getting it ready to go.

**Adrian Machado:** Cool. Yeah, perfect. Any other questions that you have for me?

**Dave Capone:** Not at this time. I'm going to sync up with Daniel and go over the requirements for this and building things out. We've been hiring a bunch of devs, so we should have the bandwidth to take this on pretty soon.

**Adrian Machado:** Yeah, cool. OK, perfect. One last thing: if you scroll to the bottom of the page, you see the different sources. I've kind of tagged these with metadata that you might find on these pages. Some of them might have logos—like the API Layer Marketplace has logos for different APIs. That might be a way for you to shortcut. I know your developer time is valuable, so maybe it makes sense to scrape pages over reinventing it yourself sometimes, just to get more context clues. I've tagged all the metadata that you can find per page.

**Dave Capone:** So if I were to scrape the API Layer Marketplace page, these are not their own API logos, right?

**Adrian Machado:** These are their first-party APIs. If you scroll further down, maybe there'll be some other ones like Adobe. It's going to really depend. The domain matters most because that's how you do a join. Click on Asana for example—they have their own page, but you'll be able to find the domain somewhere on that page. You see developers.asana.com. So now you have that docs URL. The base URL is asana.com. So your developers can essentially form a table: we scraped this page and got the docs and pricing URL. We didn't need to generate that ourselves. Think of the domain as a join key between first-party information and third-party existing information. When you find a match, that's how you get it. This is just a way for you to shortcut and get that. It did the work for us.

**Dave Capone:** So we might as well leverage it.

**Adrian Machado:** Yeah, that makes total sense.

**Dave Capone:** Yeah, so I'm good here. If I have any questions, I'll ping you. And if I don't talk to you tomorrow, have a great weekend.

**Adrian Machado:** Likewise. Catch you later.
