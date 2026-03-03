# Metronome Design Sync

<metadata>
date: 2025-09-22
time: 17:32 UTC
duration: 24 minutes
organizer: matthew@growthx.ai
participants: Matthew Panzarino, Renato Valdes Olmos, Chang Li, kris
fathom_recording_id: 88923417
fathom_url: https://fathom.video/calls/418720817
share_url: https://fathom.video/share/U3q8U4-JQSz_5FrVLVH5VD1z79-_Vzmu
source: fathom
enriched_on: 2026-03-03 18:42 UTC
</metadata>

---

## Summary

GrowthX and Metronome aligned on the ESEO project architecture: a hub-and-spoke pricing model directory with 100+ company pages built collaboratively. Metronome will handle design and Webflow implementation in-house using GrowthX's prototype as a guideline; GrowthX will build data pipelines for scraping, fact-checking, and analysis, with plans to start with 20 companies and scale to 120+. The team agreed to explore Webflow API options for scaling beyond manual CMS entry, and discussed potential downstream content (blog posts, data slicing, trend analysis) once the database reaches sufficient scale.

---

## Context

This meeting brought together GrowthX (a B2B content marketing and AI visibility company) and Metronome (a SaaS pricing analytics platform) to align on a major ESEO (enterprise SEO) project. The project centers on building a comprehensive pricing model directory for Metronome — a hub page with 100+ company cards and individual company pages with pricing data, historical analysis, and Metronome's proprietary insights. Matthew Panzarino (GrowthX) outlined the technical strategy, while Renato Valdes Olmos (GrowthX design lead) offered design flexibility, and kris (Metronome's technical lead) outlined their internal development preferences. Chang Li (Metronome) provided the company data and strategic direction. The meeting was focused on defining the division of labor, design approach, and data pipeline architecture needed to launch the directory with 20 companies initially, scaling to 120+ over time.

---

## Relevance

**To GrowthX Delivery:**
- Large-scale data pipeline project: 100-120 companies with pricing scraping, fact-checking, and analysis. 2-3 week development timeline for initial pipelines.
- Hybrid design/dev model: Metronome handling design/frontend in Webflow; GrowthX responsible for backend pipelines and content generation.
- Webflow integration complexity: Tables and complex data handling pose challenges; static table elements may be needed as workaround.
- Scalability strategy: Potential API integration for rapid publishing (5-10 companies/week); currently planning manual CMS entry for first 20.
- Knowledge base application: Project demonstrates GrowthX's capability to build proprietary knowledge bases and run RAG queries for client-specific insights.

**To CheckThat:**
- AI companies as primary focus: The directory targets AI model companies, video APIs, voice APIs — directly aligned with CheckThat's AEO and AI visibility positioning.
- Pricing model analysis as data moat: Metronome's proprietary pricing insights create an authoritative dataset that can supersede public information — reusable methodology for CheckThat.

**To GrowthX Business Development:**
- Metronome account expansion opportunity: Project scope includes blog post generation, data slicing, and trend analysis as stretch goals. "5-800 word analysis per company page" mentioned as possible expansion.
- Reference potential: Once 50+ companies complete, Metronome may use directory as public case study/marketing asset; strong reference for future AEO/ESEO projects.

---

## Overview

- Project scope: Hub page with 20+ company cards, categorized by industry; individual company pages with pricing data, analysis, and Metronome's take
- Design approach: Metronome to handle in-house design/development, adapting GrowthX's prototype
- Data pipeline: GrowthX to create for scraping, fact-checking, and generating analysis; aiming for 20 companies initially, scaling to 120+
- Webflow integration: Explore best practices for efficient content population and potential API usage for scalability

---

## Key Topics

### Project Overview and Design Approach

  - Hub page: Directory/index of company cards, categorized by industry (e.g., AI models, video companies, voice APIs)
  - Company subpages: Include pricing model snapshot, historical analysis, text segments on approach, and Metronome's perspective
  - Metronome to handle design in-house, using GrowthX's prototype as a guideline and applying Metronome's branding

### Data Pipeline and Content Generation

  - GrowthX to build pipeline(s) for:
      - Data scraping and fact-checking
      - Pricing model analysis
      - Editorial content generation using Metronome's knowledge base
  - Output: Mostly text files (MD or other formats) for CMS integration
  - Aim to start with 20 companies, potentially scaling to 120+ over time
  - Consider generating additional blog post content (500-800 words) for each company page

### Webflow Integration and Scaling Considerations

  - Explore Webflow's capabilities for handling tables and complex data
  - Investigate options for efficient content population:
      - Manual CMS entry for initial 20 companies
      - Potential API integration for scaling to 100+ companies
  - Discuss with Webflow developer (Jan) to determine best approach for large-scale additions

### Future Enhancements and Data Utilization

  - Landing page evolution: Start simple, expand with summary data and highlighted companies as database grows
  - Potential for data slicing and trend analysis once sufficient entries are available
  - Consider implementing tagging system (20+ tags per company) for easy categorization and filtering

---

## Action Items

**kris (Metronome)**
- Design hub page and company subpages using provided prototype, applying Metronome styles and branding

- Meet with Jan (Webflow developer) to discuss Webflow implementation options (API vs CMS) for company database

- Write summary of Webflow implementation plan in group chat after meeting with Jan

**Chang Li (Metronome)**
- Ensure complete list of ~120 companies is accessible to Matthew's team for processing

**Matthew Panzarino (GrowthX)**
- Begin parsing and categorizing Chang's data into knowledge base for company analysis

- Develop pipelines for data scraping, validation, fact-checking, and analysis (2-3 weeks)

- Create prototype content with generated data for initial review

---

## Transcript

**Matthew Panzarino:** Yes, so really quickly, we'll just dive right in.

**Matthew Panzarino:** Everybody's busy, I'm sure.

**Matthew Panzarino:** I just wanted to get this group together because we have this ESEO project, Ren, I think you looked at some of the internal docs, and Chris, maybe you got a chance to look at it, but the nut of it is, it's fairly straightforward from a breadcrumbs perspective.

**Matthew Panzarino:** It's a hub page that offers basically a directory or index that the directory or index could be represented as a series of cards, and then maybe, I had some thoughts on this, but maybe the categories represented as examples.

**Matthew Panzarino:** On that main page, categories being like general genre of company, like are these AI model companies?

**Matthew Panzarino:** Are they video companies?

**Matthew Panzarino:** Are they voice APIs?

**Matthew Panzarino:** That kind of thing.

**Matthew Panzarino:** Just to give a little bit of flavor there.

**Matthew Panzarino:** I guess I could screen share, but you can see the example in the meeting link.

**Matthew Panzarino:** But the designs here are very, very hand-wavy.

**Matthew Panzarino:** So do not, this is not, I'm not a designer.

**Matthew Panzarino:** This is basically a prototype to give us an idea of what's going on there.

**Matthew Panzarino:** So do not treat this as any sort of command.

**Matthew Panzarino:** It is basically to give an outline of where we stand with kind of what we need to accomplish with this.

**Matthew Panzarino:** And then the directory itself could be represented as cards on the hub page.

**Matthew Panzarino:** And then the sub page, single sub page only, as far as I can tell at this point is necessary, would be the company page.

**Matthew Panzarino:** And that company page would represent a handful of data sources as components on the page, including the usage pricing model (a snapshot of it), a historical analysis of it, a couple of text segments that would analyze its overall approach, and then give Metronome's take on that approach based on our parsing of Metronome's information that Chang has given us, to make sure that adheres to what Metronome actually thinks about these pricing models.

**Matthew Panzarino:** And then those would be collated together and then published, so to speak, as subpages to the hub page.

**Matthew Panzarino:** So that's the general outline.

**Matthew Panzarino:** Does that make sense to everyone, like, what we're looking at?

**kris:** Makes sense to me.

**Matthew Panzarino:** Okay, cool. And then on the design front, our job is just to figure out what you all need, what we would want to leverage, whether we divide and conquer or just take over designing the sub pages or the hub page itself. And then we can apportion resources accordingly. That's why Ren is here — he's our head of design and will help us figure out what we need to leverage on our side and what you want. So, kris, what do you think — how do you want to do it?

**Renato Valdes Olmos:** Yeah, to add to that — our capabilities are essentially that we can design and build anything in-house. But we also love to collaborate with in-house teams and resources, and we adapt to your ways of working. If you have a preferred method you'd like to adopt, we're all ears.

**kris:** Thanks for the context and the prototype — that definitely helps. I think we'd like to do a hybrid approach here. We'd prefer to pull in development and design on our side since we've built the platform and we can continue to iterate on it ourselves. That way, we don't have to worry about where things sit or who built them, and we can maintain control of the codebase.

**kris:** I do have some questions, though, as far as like the details inside of each company, whether they will be consistent across or, you know, like the next question is like, hey, we're going to build CMS for this.

**kris:** What do we need?

**kris:** And I'm curious on y'all's thoughts of like how there are alternative blocks for some of these or additional blocks for some of these that we have to think through so we can make sure that we build things accordingly.

**Matthew Panzarino:** Yeah, as of now, the spec as written should encompass all of the goals.

**Matthew Panzarino:** for this.

**Matthew Panzarino:** It has the spec doc that I shared.

**Matthew Panzarino:** It has the pages and subpages sort of outlined there, like what the various data components of the subpages are.

**Matthew Panzarino:** And I have not altered my thinking on those at all.

**Matthew Panzarino:** So as far as what it is right now, that's consistent.

**Matthew Panzarino:** I don't think there will be a variety of different elements per page.

**Matthew Panzarino:** Although as we get deeper into the longer tail, like certainly not for the first 20 companies or so.

**Matthew Panzarino:** I think this is exactly what we're seeing.

**Matthew Panzarino:** If we get into the longer tail of companies and all of a sudden it becomes evident that like, oh, for this group of companies, we really need an additional block or something.

**Matthew Panzarino:** I don't think any of it would be more elaborate than another component of the same type, like another text block or another field block.

**Matthew Panzarino:** I don't foresee it right now, anything.

**Matthew Panzarino:** So I think what it is, is what it should be currently.

**Matthew Panzarino:** Although, you know, Chong, if you have any input about other things that you think.

**Matthew Panzarino:** You can always let us know, but I'm pretty sure that this will encompass everything we need.

**Matthew Panzarino:** And then from a CMS perspective, we deliver for clients in a lot of different ways.

**Matthew Panzarino:** So we can, we can like stage stuff for you.

**Matthew Panzarino:** We can ship it to GitHub.

**Matthew Panzarino:** We can upload it to an FTP.

**Matthew Panzarino:** We can publish in a CMS.

**Matthew Panzarino:** Like we do it a lot of different ways for a lot of different clients.

**Matthew Panzarino:** So we're pretty flexible from, from that perspective.

**Matthew Panzarino:** So whatever works easiest for you, right?

**Matthew Panzarino:** If you're like, Hey, here's a, a template, an HTML template.

**Matthew Panzarino:** Can you fill this out with the appropriate information and then stage it or upload it to our GitHub?

**Matthew Panzarino:** Well, you can do that, you know, whatever it is, we can automate it.

**Matthew Panzarino:** So we'll make, make your, make your life as easy as possible.

**Matthew Panzarino:** don't need to like fire up a separate sanity instance for this or, or whatever, if you don't need to, you know?

**Matthew Panzarino:** But we are more than happy to do so.

**Matthew Panzarino:** If it is a CMS, of course, please do.

**Matthew Panzarino:** I doubt you wouldn't, but make it a headless one.

**Matthew Panzarino:** And, and give us an API because we can use.

**Matthew Panzarino:** that for our content managers for delivery.

**Matthew Panzarino:** So eventually, once we get this into a steady state, and we're delivering, say, like 10 new companies a week, or whatever we are, those CMs can like vet the information, do the edits, know, run the pipeline, all that, and then release it to the CMS, and either in staging form, if that's what your, you know, Chung prefers, or publishing team prefers, or we can just publish it direct, you know, once we achieve some confidence.

**Matthew Panzarino:** And once again, we do both for clients.

**kris:** Yeah, well, I think we'll probably have to talk through that, like, what, what, hey, it's done, what, how do we populate this?

**kris:** I, you know, we use Webflow, and as you all, you all have done some stuff, like on the blog and stuff in the past, but, yeah, maybe we can talk about, like, you know, is there a hundred, or is there a 10?

**Matthew Panzarino:** Like, there's just a different delivery method there.

**kris:** So, all ears there, and I'm sure you all have done some stuff in Webflow, and some other delivery things, too.

**kris:** So, I think what we could probably do on this side is like, I can design, I'll probably use yours as a pretty type.

**kris:** guideline, and then I'll just apply our styles on top of it.

**kris:** It's pretty straightforward, and then I'll just brand it out a little bit more.

**kris:** But actually, it did a pretty decent job pulling our colors and stuff like that.

**Matthew Panzarino:** Well, that was me.

**kris:** I went and grabbed the color codes from your site.

**Matthew Panzarino:** Oh, nice.

**Matthew Panzarino:** I expected your element to grab the color codes, and I was like, hey, lovable, stop using whatever green this is and use this one.

**kris:** But yeah, it did a pretty good job overall, I thought.

**kris:** It was pretty decent.

**kris:** Yeah, I started to mess with this stuff not that long ago, too.

**kris:** It's actually, it's not that bad.

**Matthew Panzarino:** Yeah, exactly.

**Matthew Panzarino:** It's really helpful when you're going into a conversation and you're trying to be like, okay, and then there's this thing, you know, it's just much easier to be like, hey, this is what I was thinking, you know.

**Matthew Panzarino:** And it can help, honestly, like highlight oddities in your thinking.

**Matthew Panzarino:** You're like, oh, I was thinking this would look good, but it does not.

**Matthew Panzarino:** So we need to do it a different way.

**Matthew Panzarino:** But the way this works for us as a data project is we're going to build a pipeline or series of pipelines. We're still wrapping our heads around it internally. The pipeline grabs the necessary data, fact-checks it, and puts it into whatever format we need for export or assembly.

**Matthew Panzarino:** And then it does that for, obviously, the data scraping from a pricing perspective.

**Matthew Panzarino:** It needs to understand what the model is, the pricing model the company is using, scrapes that data, and then formats it.

**Matthew Panzarino:** So that's where you're seeing the tables.

**Matthew Panzarino:** Then it also is going to be one or more editorial pipelines that do the analysis thing.

**Matthew Panzarino:** So the analysis will be like a rough analysis of it from an industry perspective, like what is it using and where does that fit?

**Matthew Panzarino:** And then the metronome's take is based off of data that Chung has given us at any data we may get in the future.

**Matthew Panzarino:** We parse that and put a knowledge base together, and then the pipeline basically checks the knowledge base.

**Matthew Panzarino:** Instead of using generic research and doing a researcher perplexity or XR or whatever to do a public research, it pulls from the knowledge base and says, hey, this is what you think.

**Matthew Panzarino:** Of all these different pricing models, please synthesize an analysis for us for this particular pricing model and write a paragraph basically about that, right?

**Matthew Panzarino:** And then that's where that data comes from.

**Matthew Panzarino:** So it's either scraped data, collated data, historical data, or editorial data that we are creating with the pipelines.

**Matthew Panzarino:** And then the output of those is largely text, right?

**Matthew Panzarino:** Like most of those are just text files.

**Matthew Panzarino:** So we can put them into MD or whatever formats and then shove them into the appropriate fields in a CMS via API or, you know, package them in whatever way is necessary for you folks.

**kris:** I'm a bit worried about Webflow's handling of tables — it's tough to work with.

**Matthew Panzarino:** We can create static table elements and ship those. We've worked extensively with Webflow on a handful of clients, so I'm confident we can figure it out. Yes, it can be finicky.

**kris:** Yeah.

**kris:** I mean, we'll just have to explore here and sort of see what the best method is.

**kris:** I mean, what are we looking to launch with?

**kris:** Like, how many companies are we looking to start with?

**kris:** Do we know that?

**Matthew Panzarino:** Chang and I were talking about this, and I think we want to start with between 10 and 20.

**Matthew Panzarino:** I want to shoot for, like, 20 because it gives us a chance to, like, like, 20 is put some reps in the tank, you know, to make sure we're confident with everything.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** And we can, as far as you folks launching it publicly, that's up to you.

**Matthew Panzarino:** You know, you tell me, Chang can decide, we can figure that out.

**Matthew Panzarino:** I would say minimum 20 to launch. You could do more — maybe 100 — which would give us time to iterate, stage it, look at it on pre-prod, and figure out if we love it. That's your call from a strategic perspective. I'd say minimum 20 to launch anything.

**Matthew Panzarino:** Otherwise, it's like, why do we even care about this?

**Matthew Panzarino:** From a public's perspective, not from you, but from the public's perspective.

**Matthew Panzarino:** If you want to make some sort of deal about it and build some motion around it, you're probably going need some corpus on there rather than just like, hey, here's five companies.

**Matthew Panzarino:** Okay.

**kris:** Yeah.

**Chang Li:** Yeah.

**Chang Li:** I think we'll probably do like start with 20 and by that time, it's better.

**Chang Li:** We already have some minimum database, like this type of design versus individual blog.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Sounds good.

**Matthew Panzarino:** And over that, I was thinking about this too, Chang Li, like over the course of developing the 20 companies, I want to like explore, I think it'll, it'll come clear in my head once we start actually like putting these together.

**Matthew Panzarino:** But I think there's some editorial motion we can do for you around.

**Matthew Panzarino:** So I'm thinking about it.

**Matthew Panzarino:** I don't want to promise a bunch of additional work on top of this.

**Matthew Panzarino:** I don't want to talk myself into additional work, but I really do feel like there's easy editorial motions we can do around each company, right?

**Matthew Panzarino:** So as we ship the database, you could also say, hey, here's a blog post that does a deeper analysis of each of these.

**Matthew Panzarino:** I just don't want to promise anything until I see how our analysis pipeline works.

**Matthew Panzarino:** And if it's like good enough, then we could ship like, you know, five to 800 words of additional analysis as a blog post that attaches to each of those pages.

**Matthew Panzarino:** Stuff like that is an easy win, in my opinion, from a footprint perspective and ability to like, you know, get targets onto the database and all that stuff, link building.

**Chang Li:** I think once we hit a certain number, there's a lot we can do with how we slice and dice the data. We can look at top 30 companies, stats, trends — but let's get the data out first.

**Matthew Panzarino:** Yeah.

**Chang Li:** Yeah.

**Chang Li:** The landing page could evolve quickly, kris. For now, keep it bare minimum — just show the cards of different companies. But once we hit 50, we can make it a summary page with different sections and highlighted companies. The possibilities are endless.

**kris:** Yeah, I agree. We could add a hero section or carousel once we have actual data entries.

**Matthew Panzarino:** Exactly. The possibilities are endless once we have data.

**Matthew Panzarino:** Data slicing is a great example. Once we get enough data, we can make bold statements like: 30% of top AI model companies have shifted from this pricing model to that one. We'll build a database on our side that we can query, so the data doesn't end up in silos. We're also doing this as part of our knowledge base project internally. When we develop content, it becomes its own corpus that can be queried. This gives Metronome a more authoritative take than public sources. If we just run a generic researcher on it, we'd get a mishmash of Metronome's perspective and public information. By building a knowledge base, once you have 200 companies, if you want to slice the data a certain way, I can work up a pipeline you can query without additional labor on your end.

**Chang Li:** That's a really good point. Kris, can we get high-level breakdowns if we do better labeling in Webflow? For example, if we tag companies by category or pricing model, can we auto-generate basic stats? I think we should keep that in mind during design, if Webflow can provide that capability. I don't want to do everything manually. What's the best way to structure the database to pull data from Webflow?

**Matthew Panzarino:** We have a workflow currently that creates SEO data for pages — tags, URL slugs, and all that to match keywords we're shipping. We could modify it to pull, say, 15 pieces of data about each company and ship those as Webflow tags. You'd get basic data like industry category, company name, pricing model — which of the two dozen pricing models is it, things like that. This feeds into the home page where you can filter by category. If we generate 20+ tags per company page and ship them as Webflow tags, we can do rough slicing. LLMs are extremely good at generating those kinds of tags authoritatively. We'll think through how many would be helpful.

**Chang Li:** Oh, yep.

**Matthew Panzarino:** Sweet.

**kris:** I'll do some designing using the styles from your prototype. I have a meeting with Jan, our Webflow developer, tomorrow to figure out whether we should use the API route or just CMS. I'll write up a summary of that conversation and share it with the group.

**Matthew Panzarino:** Good. Let me do some research too and we'll circle back on that.

**Matthew Panzarino:** From a scale perspective, starting with 20, we can do those manually or semi-automated. For the longer tail, 5-10 companies per week. Chang, what's the total number of companies you gave us?

**Chang Li:** Around 120.

**Matthew Panzarino:** 120 doesn't warrant an enormous engineering process. An API is helpful for publishing cadence — if you want to publish 50 at once for a big marketing motion, no problem. But 50 in two weeks is tough to do manually with quality control. There are dozens more AI companies every day, so this will probably grow beyond 120 eventually.

**kris:** That helps a lot. So, timeline-wise, are we just getting going on this? Are you gathering data and content yet?

**Matthew Panzarino:** We just got data from Chang, which we'll start parsing, categorizing, and putting into a knowledge base this week. Building out the pipelines will take 2-3 weeks. We'll have prototype content for you to play with soon. I may even take our prototype and replace it with the data we generate to make sure it feels right. My main concern is the analysis portions — Metronome's take. Whether we can authoritatively generate that based on Metronome's internal docs and the info you've given us. That's what I really care about. The rest — data scraping, validation, fact-checking — we can do.

**kris:** I was hoping you were going to say, "We have all the data now, we're launching tomorrow."

**Matthew Panzarino:** It's going to take us a minute because we want to make sure it's done right.

**kris:** Okay.

**kris:** Sweet.

**kris:** Works for me.

**Matthew Panzarino:** Great. Any other questions?

**Renato Valdes Olmos:** Not on my end.

**Matthew Panzarino:** Awesome. Thanks, everyone.

**Renato Valdes Olmos:** Thanks, folks.

**kris:** Thanks. Good meeting with you all.

**Matthew Panzarino:** Thanks, kris. Catch you later.

**kris:** Bye.
