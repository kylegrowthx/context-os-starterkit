# Tech SEO for The Adventures Group

<metadata>
date: 2025-04-25
time: 20:01 UTC
duration: 25 minutes
organizer: mariana@growthxlabs.com
participants: Dave Capone, Isabel Luna, Mariana Montezzana, Carlos G Martínez
fathom_recording_id: 59324820
fathom_url: https://fathom.video/calls/284518574
share_url: https://fathom.video/share/8nsxkP6RrJSGBA417M_c8y6ynNVPvhbq
source: fathom
enriched_on: 2026-03-04 20:30 UTC
</metadata>

---

## Summary

GrowthX's Dave Capone, Mariana Montezzana, and Carlos G Martínez met with Isabel Luna (The Adventures Group) to plan technical SEO improvements focused on schema implementation for blog articles and fixing blog template issues. Carlos will create a technical spec for adding a schema dropdown field in Sanity CMS by end of day, and the team agreed to establish weekly Friday status meetings to track progress on the new schema workflow, H2 tag spacing fixes, and keyword optimization guidelines.

---

## Context

The Adventures Group is a travel and tourism content platform where GrowthX has been delivering content marketing and technical SEO services. Mariana Montezzana (managing editor, 3 months into engagement) leads editorial strategy and blog operations. This was an introductory meeting for Carlos G Martínez, a technical SEO specialist being brought onto the account to focus on tour page optimization and blog template improvements. Dave Capone, who brings 20+ years of SEO experience across travel, e-commerce, and editorial content, had recently joined to support the account's strategic direction.

---

## Relevance

- **To GrowthX Delivery:** Establishing structured schema implementation workflow in Sanity CMS for blog articles — custom input fields (preferred) vs. GTM conditioning. Need to fix blog template spacing issues (H2 tags implemented but spacing still broken). Opportunity to document keyword optimization best practices to prevent keyword stuffing in refreshed content.

- **To GrowthX Business Development:** Account health signal: client actively investing in technical SEO with regular Friday status meetings. Three GrowthX team members now engaged (Dave, Mariana, Carlos) suggests account expansion and deepening relationship. Potential to expand schema strategy to tour pages beyond blogs.

---

## Overview

- Carlos to create technical doc for adding schema dropdown to Sanity CMS blog section (due today 2025-04-25)
- Mariana to share schema list and page mockup with team for review
- Isabel to request staging access for the Adventures Group team from developers
- Team to establish weekly Friday status meetings for ongoing tech SEO collaboration
- Blog template improvements needed: H2 tags working, but spacing issues persist, schema integration required
- Carlos to provide keyword stuffing examples and optimization guidelines for content refresh process

---

## Key Topics

### Team Introductions and Project Overview

  - Mariana: Managing editor for Adventures Group (3 months)
  - Dave: 20+ years SEO experience (Attics, Adventures, TripAdvisor)
  - Carlos: SEO specialist, joining to assist with technical SEO
  - Current focus: Tour page optimization, editorial/blog improvements

### Schema Implementation for Blog Posts

  - Proposal to add schemas like "tourist attraction" to blog articles
  - Dave confirms adding schema to articles is beneficial for SERP treatment
  - Options for implementation:
    1.  Custom input in article head (preferred for flexibility)
    2.  Google Tag Manager (URL-based conditioning)
  - Team to create field in Sanity CMS for schema input during article creation

### Blog Template Improvements

  - H2 tags now implemented, but spacing issues persist
  - Need to align content review speed with publishing capabilities
  - Aim to streamline optimization process for older content
  - Carlos to provide guidelines on avoiding keyword stuffing

### Content Creation Process

  - Using multiple LLMs in workflow steps
  - Ability to customize prompts at article or client level
  - Carlos offered to suggest tested prompts for improved results

### Next Steps for Tech SEO Collaboration

  - Carlos to create staging access request for developers
  - Regular Friday status meetings to be established
  - Team to review schema implementation doc from Carlos

---

## Action Items

**Carlos G Martínez (GrowthX)**
- Create technical doc with instructions for Oscar — add schema field/dropdown to Sanity blog section. Share with team via email by end of day (2025-04-25).

**Isabel Luna (The Adventures Group)**
- Upload Carlos' schema implementation doc to dev task management tool after team approval. Request staging access from developer for Adventures Group team.

**Mariana Montezzana (GrowthX)**
- Share schema list screenshot and mockup page with team via email for review (note: mockup is brainstorming only, not finalized).
- Discuss with Alice regarding optimal Friday status meeting time and confirm with team.

---

## Transcript
**Mariana Montezzana:** I was telling Jess that it's so good to see the world outside every now and then.

**Isabel Luna:** Why is it that you're working outside today?

**Mariana Montezzana:** Because I'm meeting some friends later, and then I was like, I want to go out a little bit.

**Mariana Montezzana:** Every now and then I come to this very same place, like for 40 years, whenever I need to go out of the house a little bit.

**Isabel Luna:** Super, super amazing.

**Isabel Luna:** Well, Carlos is about to join us. In the meantime, Dave, how are you?

**Dave Capone:** I'm doing well.

**Dave Capone:** Looking forward to the weekend.

**Dave Capone:** We're going up to the beach over here in North Carolina.

**Dave Capone:** So I've never been before.

**Isabel Luna:** Yeah.

**Dave Capone:** So hopefully it'll be fun.

**Dave Capone:** How far away from where you live?

**Dave Capone:** We're four hours from everything — four hours from the mountains, four hours from the beach, four hours to Atlanta. It's nice, you can jump in the car and be there within a couple hours.

**Dave Capone:** We're going to Jacksonville, North Carolina. We have some friends there and we all do couples trips together. We've gone to the Caribbean, a bunch of Sandals resorts, but haven't actually been to their place yet. So we're going there to hang out for a couple of days.

**Isabel Luna:** Ah, that's so cool.

**Isabel Luna:** So, um, and I have to say that I really like the mock-up you guys work on for our filler pages.

**Isabel Luna:** It looks top notch.

**Isabel Luna:** Love it.

**Dave Capone:** Yes.

**Mariana Montezzana:** We're excited to implement it.

**Isabel Luna:** Yes, definitely.

**Mariana Montezzana:** I told Dave that I asked you if it will be okay for you if you get a professional to log in to the production.

**Mariana Montezzana:** The the production, the stage, what is the name of the game?

**Mariana Montezzana:** staging area.

**Isabel Luna:** Yeah, please don't forget to share the mock-up with me so I can tell them, you know, like, present the project to everybody.

**Mariana Montezzana:** Dave was working on the list of variables — geography like Cancun, Puerto Vallarta, and Cabo. But we could do broader options like Riviera Maya or Yucatan Peninsula, not too granular. For example, Lovers Beach. I was talking to Dave about maybe creating a card for each destination. We have posts for Balandra Beach, Sea of Cortes, and others. Those could be cards, or we could optimize them and bring in any blog posts related to those destinations.

**Dave Capone:** Yeah.

**Dave Capone:** So right now I'm putting the requirements together for the project and how we're going to build the page.

**Dave Capone:** So essentially just like, you know, defining what, you know, the MVP looks like, what are things that we can build, how we're going to, how we're going to take in the content, like how we're on gesture product feed, how we're going to look at photos and apply, you know, tagging to those photos and figuring things out on how we're going to build this thing.

**Dave Capone:** So I should have that done probably Monday, and then I'll pass it to our engineering team to look at.

**Dave Capone:** We've got pretty much all the things so far to start moving forward.

**Dave Capone:** You know, once we get it in the hands of the engineers, it'll be interesting to see what their take is on it.

**Dave Capone:** But we are building similar types of experiences already.

**Dave Capone:** Hey, Carlos.

**Dave Capone:** Hola.

**Isabel Luna:** Hi, how are you?

**Carlos G Martínez:** Good. Hi. Sorry about the technical difficulties. No worries.

**Isabel Luna:** Well, Mariana and Dave, do you want to introduce yourselves?

**Mariana Montezzana:** Yes.

**Mariana Montezzana:** Hi, Carlos.

**Mariana Montezzana:** My name is Mariana.

**Mariana Montezzana:** I'm the managing editor for the Adventures Group accounts.

**Mariana Montezzana:** We've been working together for three months now.

**Mariana Montezzana:** And this is it.

**Mariana Montezzana:** We implemented a bunch of content.

**Mariana Montezzana:** I know if you had the chance to analyze.

**Mariana Montezzana:** So nice to meet you.

**Mariana Montezzana:** Happy to work with you.

**Isabel Luna:** Yeah, nice to meet you, too.

**Carlos G Martínez:** And Dave.

**Isabel Luna:** Dave is a recent addition to our account.

**Isabel Luna:** Yep.

**Isabel Luna:** So, Carlos, I'm the director on the account.

**Dave Capone:** I've been working in SEO for like a really long time, like over 20 years or so, working for brands like Attics, Adventures, and recently TripAdvisor.

**Dave Capone:** So I've been a lot of experience in both editorial SEO, e-commerce SEO, and travel.

**Dave Capone:** So it's a dream to be working on an account like this.

**Dave Capone:** Yes, thank you.

**Isabel Luna:** Thank you so much.

**Carlos G Martínez:** Bueno.

**Isabel Luna:** And Carlos, do you want to briefly, briefly introduce yourself?

**Isabel Luna:** Yeah, for sure.

**Carlos G Martínez:** First, I was having trouble connecting, sorry about that. I'm really passionate about SEO. I got into it indirectly — I studied interactive design, then digital marketing and e-commerce. My first approach was with email marketing, then I fully started working with SEO. I've known about GrowthX for a couple of years. It's funny because I work with another consultancy and we had a client that invited us to a GrowthX event.

**Isabel Luna:** I know.

**Isabel Luna:** I'm happy to meet you and happy to meet you here.

**Isabel Luna:** Carlos, ¿sabes que se está cortando mucho la conexión?

**Isabel Luna:** ¿Será que quitamos el video?

**Isabel Luna:** Sí.

**Isabel Luna:** Perfecto.

**Isabel Luna:** Bueno, ok, very well.

**Isabel Luna:** So for this first meeting, my idea was, Carlos, would you want to quickly grow?

**Isabel Luna:** Go through the updates Oscar has made regarding technical SEO, or would you prefer Mariana first to show what she has in mind regarding new schemas and things like that to implement?

**Isabel Luna:** I think that that'll be best.

**Carlos G Martínez:** Okay.

**Mariana Montezzana:** Isabel, you mentioned that Carlos will be working with the Tech SEO for the tour pages, right?

**Mariana Montezzana:** And we'll be prioritizing what we need to do with the editorial pages, the blog template, right?

**Mariana Montezzana:** Yeah, that's right.

**Mariana Montezzana:** I was thinking about adding schemas like "tourist attraction" to articles. I have some terms I found, for example, "tourist attraction."

**Mariana Montezzana:** For example, for Balandra Beach, we could add "tourist attraction" schema. I found the schemas, but I wouldn't know how to add that.

**Mariana Montezzana:** For example, when Lucero is publishing, maybe we need to change the sanity template where we publish anything to have those fields.

**Mariana Montezzana:** I know, for example, for WordPress, like you can add those plugins where you manually add the terms for schema.

**Mariana Montezzana:** So I don't know what's the equivalent for sanity.

**Mariana Montezzana:** Okay, super.

**Isabel Luna:** Would you want to share your screen?

**Mariana Montezzana:** Yes.

**Isabel Luna:** Yeah, my idea, inviting Carlos to this one, to this meeting, is like he already has this relationship with our developer, like they understand their own terms.

**Isabel Luna:** So anything you need, it will be okay.

**Isabel Luna:** Thank you.

**Isabel Luna:** Because Hans to translate it into a tech doc, as he has done, and we will upload it to the pipeline platform we have with our developer so he can create it.

**Mariana Montezzana:** The first thing is, you confirmed that we now have H2 tags. Remember Dave mentioned they didn't have those, but now they've been added. And Lucero mentioned in our meeting yesterday that she tested the spacing, but it's not working as expected. We need to fix that. I think that's super important because we can do part of the publishing workflow here, especially with automatic image selections. And we could also align the speed of content review with the speed of publishing.

**Mariana Montezzana:** So we need improvement in blog templates, and at the same time, we could add schema modifications with terms like "tourist attraction" in editorial content.

**Isabel Luna:** Carlos, are you familiar with those schemas?

**Mariana Montezzana:** I'm not sure if these are best practices. That's why we need to align. These are brainstorming ideas. For example, I didn't know about this "geocoordinate" field, but it would make it easier to show results related to locations.

**Isabel Luna:** So that one, that one, for example, of geocoordinate, we...

**Isabel Luna:** We use it, for example, when talking about restaurants, like Cancun, like Vallarta Beach, like Lovers Beach.

**Mariana Montezzana:** Okay.

**Carlos G Martínez:** Sorry, I was on mute.

**Carlos G Martínez:** For the tourist pages, what we did is a comparison between actually TripAdvisor and us, and as a reference, the structured data that they have currently, and we replicate that exactly.

**Carlos G Martínez:** So right now, the tourist pages have the structured data as TripAdvisor DOS to enhance the visibility.

**Carlos G Martínez:** And I can definitely support including the structured data for some attractions.

**Carlos G Martínez:** you.

**Carlos G Martínez:** be right back.

**Carlos G Martínez:** But are you thinking to include those as part of the blog post, or would this be on just the two pages?

**Mariana Montezzana:** I was thinking we could also add Schema to the articles.

**Mariana Montezzana:** Do you think this is a good idea, Dave?

**Dave Capone:** Yeah, I think it's a great idea to add Schema to the articles.

**Dave Capone:** Schema will help Google figure out what the page is about and supply some additional facts, hopefully some different treatments in the SERPs with these, which is what we're trying to do.

**Dave Capone:** So, yeah, I think it's definitely something we should do.

**Mariana Montezzana:** Is there a way to add a tool that would make these schema injections, for example when Lucero publishes, or could we do this when uploading a new article? Could we fill a field with the terms?

**Dave Capone:** It would have to be done in HTML. If we have a way to upload via HTML, or if they build something when uploading a new article with a field for this, then yes. We could create all of this on our end, we'd just need a place — a field that would put it into the page code.

**Isabel Luna:** Exactly. That was Mariana's suggestion too — to have a dropdown for HTML.

**Mariana Montezzana:** Yeah, in WordPress there's a plugin for this. When creating an article, just like Yoast SEO, you have a place to fill in schema information.

**Isabel Luna:** Carlos, would you like to translate that idea into a document for Oscar?

**Carlos G Martínez:** Sí, seguro (Yes, sure).

**Carlos G Martínez:** I'm thinking of two alternatives. We could have a custom input field in the head of the article page that would give us freedom to customize it as needed. If that's not possible, the other alternative is Google Tag Manager — you can condition code injection based on specific URLs. But I need to double-check with Oscar.

**Mariana Montezzana:** Okay.

**Mariana Montezzana:** Besides schema, are there other ways we can improve our SEO efforts with Carlos?

**Isabel Luna:** Who's that question for?

**Mariana Montezzana:** Other initiatives besides schema implementation.

**Isabel Luna:** Well, so far, Carlos hasn't gone through the blog articles yet, right, Carlos?

**Isabel Luna:** You only have focused on the two pages.

**Carlos G Martínez:** Yeah, just the tour pages so far, but I've seen opportunities to optimize older blog pieces. I've noticed some keyword stuffing in some cases. Is there a way we could streamline the optimization of blog articles to identify keyword stuffing and get a more natural-sounding tone?

**Isabel Luna:** There's a lot of noise coming through.

**Mariana Montezzana:** I'm not sure which articles you're referring to — whether it's older content or more recent. We're creating new articles and now starting to refresh old ones, focusing on keywords that could drive traffic. We could establish best practices to avoid keyword stuffing. The workflow can add more keywords than natural flow, then we manually adjust. If you give us guidelines for future content, that would help.

**Carlos G Martínez:** Yeah, for sure. My guess is those are old materials — it's noticeable which ones are recent. I can definitely share examples. I'm curious about the content creation process. Does it rely on a specific LLM, or are you using multiple LLMs?

**Mariana Montezzana:** Multiple.

**Mariana Montezzana:** The workflows have many steps, and we can use multiple LLMs per step, or specify which LLM to use for each step. We have fields for article briefing and feedback where we can manually add instructions. If you have tested prompts or specific instructions, we can add those at the article level or client level.

**Carlos G Martínez:** Awesome. I've been testing prompts and seeing the difference. I could suggest tested approaches if that would help.

**Mariana Montezzana:** The next deliverable is adapting the interface where we publish articles to add these schemas.

**Isabel Luna:** Carlos, can you create a technical document with instructions for Oscar on how to add a schema field/dropdown to Sanity for the blog section where we can choose which schema to use for each article?

**Carlos G Martínez:** Yeah, for sure. I can have it done by today.

**Isabel Luna:** Ah, amazing!

**Isabel Luna:** Once that's done, you can share it via email with Dave and Mariana so they can review and add feedback. Once we have approval, I'll upload it to the task management tool we use with the developer.

**Isabel Luna:** Going forward, we'll have a regular status meeting on Fridays. Carlos can be a listener, and if you have something to add, you're welcome. It'll be a mix of brainstorming topics and status updates. I think it'll be useful to have everyone on the same page.

**Mariana Montezzana:** I'll need to confirm the time works with Alice and will follow up with her.

**Isabel Luna:** Alright, thank you all. Carlos, it was nice to meet you. Mariana, would you share the schemas screenshot and the page mockup we just discussed?

**Mariana Montezzana:** Yes, I'll send both. The mockup is brainstorming-level, not finalized. We can add more or change it as needed.

**Isabel Luna:** I'll request staging access from the developer so you all can work directly on it. If they decline, they'll create it for us.

**Isabel Luna:** Have a great weekend.

**Mariana Montezzana:** Happy weekend, everyone.

**Isabel Luna:** Nice to meet you, Carlos.

**Carlos G Martínez:** Likewise. Bye, everybody.
