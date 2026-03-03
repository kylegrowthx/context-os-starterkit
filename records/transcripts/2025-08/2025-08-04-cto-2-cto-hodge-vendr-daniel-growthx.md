# CTO-2-CTO Hodge (Vendr) & Daniel (GrowthX)

<metadata>
date: 2025-08-04
time: 18:01 UTC
duration: 48 minutes
organizer: daniel@growthxlabs.com
participants: Matt Hodgson (Vendr), Yousef Hamade (Vendr), Daniel Lopes (GrowthX)
fathom_recording_id: 78321946
fathom_url: https://fathom.video/calls/369367023
share_url: https://fathom.video/share/cWAkd9theqGkyos1i_42PDZNVgZzxPkJ
source: fathom
enriched_on: 2026-03-03 09:30 UTC
</metadata>

---

## Summary

Matt Hodgson (Vendr CTO) and Daniel Lopes (GrowthX CTO) explored a strategic partnership where GrowthX would build AI-powered content generation and SEO optimization workflows for Vendr's marketplace. The core opportunity: leveraging Vendr's catalog data (suppliers, products, pricing) to generate FAQs, comparison pages, product cluster pages, and blog content that drive traffic to Vendr's pricing estimate widget—especially important as LLM-powered search results are cannibalizing traditional link-through rates. Daniel walked through GrowthX's workflow architecture (140+ reusable workflows, strategy sprints, weekly reporting on LLM citations/brand mentions), and Matt identified data integration (via Webflow CMS or custom database) and scaling content generation (18,000+ pages) as key technical questions. Next step: Marcel (GrowthX CEO) will meet with Matt to discuss content strategy and execution timeline.

---

## Context

Vendr operates a B2B SaaS marketplace (vendr.com) listing software suppliers, products, and pricing data—core IP that differentiates them from competitors like G2. The company monetizes through a pricing estimate widget, where prospects enter deal parameters and Vendr returns custom pricing for different vendors. Their challenge: generating high-quality content at scale that targets people searching for specific pricing and product comparisons (e.g., "SOC 2 compliance tools ranked by price") while driving them to the estimate tool rather than losing them to LLM-powered search answers (Claude, ChatGPT, Perplexity). Matt and Yousef (who introduced the partnership) connected with Daniel because GrowthX has proven success generating data-driven content at scale for clients like Augment, Ramp, and Fieldwire, with built-in measurement of LLM citations and brand mentions—a capability Vendr desperately needs. This was a CTO-to-CTO exploration of technical feasibility before Marcel engages on commercial terms.

---

## Relevance

**To GrowthX Delivery:**
- Validates the market-fit of GrowthX's AI workflow approach for API-driven catalog content; Vendr's 18,000+ supplier/product database parallels Ramp engagement. Daniel demonstrated how workflows integrate with existing CMS (Webflow) or custom databases—direct technical pattern-matching for scope.
- High-volume, deterministic content generation opportunity: Vendr needs 18,000+ programmatic product pages, FAQs, and comparison pages. This tests GrowthX's ability to operate at scale without custom per-client engineering (contrast: Augment required 140% custom development due to MCP server architecture).
- LLM citation and brand mention tracking is core value prop—Daniel's Scrunch tool (tracking in ChatGPT, Claude, Perplexity daily) positions GrowthX as the only vendor measuring AEO outcomes. Matt was explicit: this is the biggest gap Vendr has. Strategic bet: if GrowthX can quantify this for Vendr, it's a case study for market messaging.

**To CheckThat:**
- Real-time example of LLM search cannibalization affecting B2B business models. Matt's concern—"G2 is seeing massive downticks in click-through rates because Google just answers the question"—is CheckThat's thesis. Vendr's solution (ensuring content points to the pricing widget even in LLM answers) shows demand for visibility into LLM recommendations.
- Opportunity to integrate CheckThat into GrowthX's Scrunch-equivalent product. Currently GrowthX tracks brand mentions; integrating CheckThat's claim extraction and accuracy scoring would differentiate against competing AEO platforms.

**To GrowthX Business Development:**
- High-profile account potential: Vendr is Series B, backed by top-tier VCs, and Matt indicated strong budget ("very light" approval bar—they'll experiment freely). Success here = strong reference for other SaaS marketplaces (Capterra, Gartner, AppFigures).
- Marcel meeting scheduled Thursday. Matt is optimistic about technical alignment (data via API/Webflow CMS); deal structure will depend on content volume pricing vs. fixed-cost sprint model. Daniel suggested starting with 20-article calibration phase—low-friction entry.
- Expansion flag: Yousef mentioned blog pages as Vendr's highest-traffic content; this signals opportunity beyond FAQ/comparison pages into full editorial strategy (20-50 articles/month range Daniel quoted).

---

## Overview

- GrowthX offers customizable AI-driven content creation and SEO optimization workflows
- Vendr aims to leverage its data to create targeted content that drives traffic to its pricing estimate tool
- Integration options include using Webflow CMS or creating a custom database solution
- GrowthX's approach combines automated workflows with human oversight for quality control

---

## Key Topics

### GrowthX's AI-Driven Content Creation System

  - Utilizes customizable workflows for content creation, research, and SEO optimization
  - Combines AI automation with human review for quality control
  - Offers flexibility in integration, from using existing CMS to custom API solutions
  - Tracks content performance, including LLM citations and brand mentions

### Vendr's Content Strategy Goals

  - Focus on driving targeted traffic to the pricing estimate tool
  - Need for content that answers specific questions about software pricing and comparisons
  - Interest in leveraging internal data to create unique, valuable insights
  - Aim to improve SEO performance and adapt to changes in search engine behavior (e.g., LLM-powered answers)

### Integration and Implementation Considerations

  - Potential use of Webflow CMS for content management
  - Option to create a custom database solution for content storage and retrieval
  - Need to determine the best method for sharing Vendr's internal data with GrowthX
  - Importance of aligning content creation with Vendr's existing catalog and data structure

### Content Types and Opportunities

  - FAQ pages for specific products and suppliers
  - Comparison ("versus") pages for multiple products
  - Product cluster pages highlighting top products in a category
  - Blog posts and buyer's guides (currently high-performing content for Vendr)
  - Refreshing and enriching existing content with new data and insights

### GrowthX's Workflow and Reporting Process

  - Initial strategy sprint to determine content approach and topics
  - Weekly or bi-weekly reporting on content performance and strategy adjustments
  - Continuous monitoring of LLM citations and brand mentions
  - Iterative approach to content creation, starting with short-form answers and expanding to full pages based on performance

---

## Action Items

- **Schedule meeting with Marcel (GrowthX)** — Matt Hodgson to meet with Marcel to discuss content strategy, execution timeline, and pricing/scope model. Daniel confirmed Thursday meeting was already set up. (Owner: Matt Hodgson - Vendr)
- **Determine data integration method** — Decide between Webflow CMS (for direct content publishing) vs. custom database (Airtable/Supabase) for syncing content back to Vendr's back-office. Daniel indicated both are viable; CMS is simpler if Webflow tier upgrade is acceptable. (Owner: Matt Hodgson - Vendr)
- **Calibration phase: 20 articles** — Daniel proposed starting with 20 test articles to validate GrowthX's approach (writing guidelines, personas, data consumption from Vendr's API) before full rollout. Vendr reviews and approves. (Owner: Matt Hodgson + Daniel Lopes)
- **Identify initial content clusters** — Work with Marcel to define which supplier/product categories to tackle first (e.g., SOC 2 compliance tools, CRM pricing comparisons) and which content types (FAQs, versus pages, cluster pages, blog). (Owner: Matt Hodgson - Vendr + Marcel/Daniel - GrowthX)
- **Explore Webflow CMS upgrade** — Matt to evaluate if upgrading Webflow tier is cost-effective vs. building custom database solution. Daniel noted API integration is simpler than CMS, but CMS reduces engineering overhead. (Owner: Matt Hodgson - Vendr)

---

## Transcript
**Matt Hodgson:** Hey, Daniel, what's up man?

**Daniel Lopes:** Nice to meet you.

**Yousef Hamade:** This meeting is being recorded.

**Matt Hodgson:** Yousef, you doing intros or what's the plan?

**Matt Hodgson:** You guys know each other?

**Yousef Hamade:** Daniel, Hodge, Hodge, Daniel.

**Yousef Hamade:** Hodge is the CTO over at Vendr and very, very hands-on CTO, very technical.

**Yousef Hamade:** I've known each other for like three, three and a half years at this point in time, right, Hodge?

**Matt Hodgson:** Yep.

**Matt Hodgson:** Yep.

**Yousef Hamade:** And all of that.

**Yousef Hamade:** Daniel is the CTO over at GrowthX.

**Yousef Hamade:** Daniel, we've known each other.

**Yousef Hamade:** I've a few months now, I would say, and, you know, I think, Hodgson, haven't officially been introduced to Marcel yet, but you guys are meeting on Thursday.

**Yousef Hamade:** So just quick intro to the effort.

**Yousef Hamade:** Daniel, Vendr has their marketplace.

**Yousef Hamade:** So if you just go on Vendr.com, they have a list of companies and, in some cases, products.

**Yousef Hamade:** They have a number of blog posts, all of that.

**Yousef Hamade:** They are looking to enrich, or we are looking to enrich all of the content there with additional stuff, a lot of which could be found through public information and all of that.

**Yousef Hamade:** And when I saw...

**Yousef Hamade:** What we were looking to add there, I immediately thought of GrowthX and all the cool stuff Marcel and you and the rest of the team do there, and think it could be somewhat synergistic to be able to leverage GrowthX to fluff out a lot of that content and start adding content in new places that we don't currently have it.

**Yousef Hamade:** And, you know, work together with the vendor team to get that content published, right?

**Yousef Hamade:** And then Vendr has built some variations of this, but, you know, my thought there is, you know, Fathom and the vendor engineering team are extremely capable people, but they're not content people, right?

**Yousef Hamade:** And so...

**Yousef Hamade:** The difference between knowing what good engaging content is and not is kind of, I think, a potential gap there.

**Yousef Hamade:** And then just, you know, building and maintaining those pipelines for an extremely large catalog of vendors and products can be, you know, a challenge.

**Yousef Hamade:** Doing it once is hard.

**Yousef Hamade:** Doing it, you know, lots of times every day is much harder to keep the content fresh and, you know, keep SEO and GEO bots happy.

**Yousef Hamade:** So, that makes sense.

**Daniel Lopes:** Let me just, you know, you know, like, what would be the best way for me to, like, help you, Hodge?

**Matt Hodgson:** I have of questions I could just anchor around.

**Matt Hodgson:** I think, you know, we'll talk, I can talk to Marcel later, but about sort of more.

**Matt Hodgson:** Maybe like content strategy itself, but I was hoping to pick your brain a little bit about how to sort of dovetail from a technical architecture standpoint, like this sort of content strategy with some of the other core stuff that we do.

**Matt Hodgson:** So similar, like, did you work on the Ramp project?

**Daniel Lopes:** Like, were you there for that? I've followed it. Like one of the engineers did, but I'm pretty familiar with that.

**Matt Hodgson:** Okay, cool.

**Matt Hodgson:** So, like, I think what we're talking about is probably most similar to that, but we have a sort of the core fundamental part of our offering, this sort of basic catalog ontology for SaaS software.

**Matt Hodgson:** And so, like, you know, suppliers and products and that's very, like, critical to what we offer from, like, the API, like the pricing data that we sell, all of that stuff is, like, super critical.

**Matt Hodgson:** And so the content that we want to generate and have should...

**Matt Hodgson:** At least the ontology should be derived from that catalog, and then potentially some of the insights we could generate from our data would be part of the content.

**Matt Hodgson:** But obviously all that's part of our core system, what we call a back office, but our back office, like database and all of that.

**Matt Hodgson:** And then we have a front-end app that we thought was going to be like a marketplace where we really needed it to be its own like full-stack application, and that's this thing you're looking at now.

**Matt Hodgson:** Our website used to be in Webflow, though, right?

**Matt Hodgson:** So it was like much easier to do content generation.

**Matt Hodgson:** Like we could just, you know, people get, it was templates and CMS and all that stuff, and it was get plug and play.

**Matt Hodgson:** And then we like took half of it now, which is these pages, and this is its own web app now.

**Matt Hodgson:** And I think we're like in a position strategically now where we're...

**Matt Hodgson:** I'm thinking maybe we shouldn't have done that.

**Matt Hodgson:** But on the other hand, when it was like Webflow and CMS, it had a tendency to sort of get disconnected and stale from the real catalog.

**Matt Hodgson:** We still need to be able to embed these interactive widgets on the page.

**Matt Hodgson:** But ideally, me and my team don't have to custom build basically a CMS functionality so we can surface content and have what you guys do happening, right?

**Matt Hodgson:** And so I'm wondering if maybe you could help me understand like the best structure you've seen to sort of marry these two things.

**Daniel Lopes:** Yeah, I can walk you through some different clients and I can show you the behind the scenes and I can explain how we did it and like what's going on there too.

**Daniel Lopes:** Like maybe that will give you an idea.

**Daniel Lopes:** Because like what you're describing, like we have different ways of doing that.

**Daniel Lopes:** Like so like in the case of the catalog, with all the pricing data and everything, I'm assuming you guys would have an API or like something that could be consumed.

**Daniel Lopes:** So we could have like, because we have two kinds of problems when they're dealing with different clients.

**Daniel Lopes:** Like some folks who have like a large set of data that they want us to consume, like it's like PDF formats and stuff like that.

**Daniel Lopes:** So for that, we're building like a graph reg implementation with like Neo4j and the vectorization separate with VVA.

**Daniel Lopes:** And then we would be building the graph out of what they want.

**Daniel Lopes:** So that part of the project isn't ready.

**Daniel Lopes:** And I could say in progress, it would be ready like in a couple of weeks, I think.

**Daniel Lopes:** Before we had a traditional rag, and then we would just load everything in there.

**Daniel Lopes:** That still works.

**Daniel Lopes:** But if you have an API, it's even better because you don't have to use that part.

**Daniel Lopes:** It would be a pipeline that would start from there with public data.

**Daniel Lopes:** It's kind of what we do for a few clients.

**Daniel Lopes:** And maybe I can show you.

**Matt Hodgson:** I don't know.

**Matt Hodgson:** I it makes sense or not, but we also have an MCP server, which we found, obviously, it's just wrapping the API, but we've just found it's really cool to plug it right into the LLM and have it decide what data to get.

**Matt Hodgson:** We've had some success where we're like, wow, this actually generates pretty intelligent information.

**Daniel Lopes:** Yeah, let share my screen and I'll walk you through some of the clients.

**Yousef Hamade:** Yeah.

**Daniel Lopes:** So, we have, let's see, we have, this is the one for vendor, for vendor for rent.

**Daniel Lopes:** It's slightly this and it's simpler, but it has some sort of sanity.

**Daniel Lopes:** So, sanity is the CMS that they use.

**Daniel Lopes:** It's kind of a pain, yes.

**Daniel Lopes:** And they built a lot of the widgets in sanity.

**Daniel Lopes:** The interactable things you have, interactive things you have on your website, they built insanity as blocks.

**Daniel Lopes:** So, we had to do a lot of custom.

**Daniel Lopes:** Work to integrate with Sanity and know which blocks are usable or not.

**Daniel Lopes:** So we have a custom stack.

**Daniel Lopes:** But just to back up a little bit, we have two systems. We have a system that does the content creation part. And we have another system that's essentially a workflow orchestration—like an AI workflow orchestration—where you can create custom workflows or use some of the reusable workflows that we have internally.

**Daniel Lopes:** So we have a researcher—a deep researcher using Perplexity and Tavoli—and an agentic loop that will keep trying to find everything relevant. We also have one for drafting. The drafting can use the MCP you mentioned, taking in the direction and writing the article based on that direction with evals to check if it's writing in the direction you wanted. It can then trigger the MCP if needed.

**Daniel Lopes:** But let me show you.

**Daniel Lopes:** Let me show you the Fathom account we were just looking at yesterday. This is the internal interface the team uses. We have pipelines that start with a context artifact—a strategy document that defines which documents can be used throughout the process. These include things like: what products do you serve, how we write for your LLM generation, personas, your company context, and writing guidelines with good and bad examples. All of these inform the LLM creation process. Then we have the pipelines, where we stitch the AI workflows together. For simpler clients, we almost never have to do custom stuff. For more complicated ones—like some of the video cases—

**Daniel Lopes:** In the page for rent, we had to do the sanity stuff.

**Daniel Lopes:** Sometimes we have to create our own research, researcher for different data sources.

**Daniel Lopes:** That was the case for Augment, for example, we have this product that we built for them that is a collection of MCP servers.

**Daniel Lopes:** So we had to build a researcher to find the MCP servers and collect the data and store that in a database and then consume from there.

**Daniel Lopes:** Like that's the stuff that we did for Augment, for example.

**Daniel Lopes:** But that one was almost like all the steps in the pipeline were custom, but I'll show you the one for sound.

**Daniel Lopes:** The usual editorial workflow we have is something like this: you come in with a topic and it creates a good definition for an SEO-based article for that topic in your space, for the personas you have and the products you serve.

**Daniel Lopes:** From there, there's a deep researcher, outline generator, article draft, fact checker, then we add internal links from your system and create metadata. Each of these steps is essentially a micro-app or function—all code-based. They talk to each other in this pipeline format.

**Daniel Lopes:** For example, at the beginning, we have a parameterizable form defined in our internal language. It specifies what inputs we need—sometimes dropdowns, sometimes checkboxes, sometimes image uploads. In this case, text fields. The assignment generation takes six minutes because it makes many API calls to SEMrush, identifying competitors, ranking the top three, checking their articles, and coming up with a potential set of considerations for writing the article.

**Daniel Lopes:** So we generate the target audience, potential metadata, top organic competitors, and a proposed structure for the article. Our editor reviews and edits this. All steps have a human review option that pauses the workflow so people can edit, then press save and continue. After that, we execute the following steps without human intervention, but people can still go back and change things.

**Daniel Lopes:** We have an inspect mode that opens our workflow orchestration engine—where we store all the workflows. They're all in code. We have a library of about 140 workflows that do different things.

**Daniel Lopes:** They do research, SEO-specific content generation, image generation, internal linking, rewriting, and related tasks. The one we use here is part of the strategy process for SEO content—creating an assignment, as we call it.

**Daniel Lopes:** The input is JSON; the view is just for readability. Every workflow is essentially an API endpoint. This one takes the keywords, user content, personas document, and other documents to understand the context. If it takes a URL, it takes one approach; if it takes a keyword or topic—like this case—it takes a different approach.

**Daniel Lopes:** If it's a URL, we find which keywords are ranking for it. If it's a topic, we search Google to see the actual results, instead of relying on paid data from something like SEMrush.

**Daniel Lopes:** We then analyze search intent based on your personas documents and generate a brief with an outline. That outputs the document we saw in the pipeline. The person approves it, then moves to the next step.

**Daniel Lopes:** The draft is one of the steps. We have two modes: linear and agentic. The agentic approach looks like this. We're not using this with all clients yet; we're rewriting many workflows from linear to agentic based on evals and metrics the editorial team developed.

**Daniel Lopes:** For example, let's say the input was for a client doing tax software—an AI agent for tax consulting and advice. That's the topic we want to write about. It takes the research data and a direction input—a rough direction is here.

**Daniel Lopes:** It's "provide a useful, to-the-point, plain-spoken guide for non-tax professionals." Let's see if it did a good job.

**Daniel Lopes:** We take all this, generate the first draft—stored in the database, so we just output the database ID—and then run the evaluation.

**Daniel Lopes:** The evaluation is grounded on the research data with a score from zero to one and comments on why it wasn't happy. This might not work perfectly because the workflow doesn't have scraping as a tool, so you might not get the TurboTax reference another person wanted. But it's grounded on the research data, scoring 7.5. The weak points are making claims with back-and-forth contradictory language.

**Daniel Lopes:** We also check if it's following the writing guidelines we wrote for the company and if it's following the direction. The direction with TurboTax on will fail because of the scraping issue.

**Daniel Lopes:** The planner iterates on what has to be done after the evaluation and executes improvements. We use a system called Temporal that executes our workflows—all in code. We built our own framework for creating these workflows.

**Daniel Lopes:** It's similar to what I did at my previous job at IFTTT, where we had recipes. Every workflow is essentially a recipe with steps, prompts, and orchestration flow.

**Daniel Lopes:** If you have an API with MCP, we can create a custom workflow to consume the data and use other workflows in a pipeline.

**Daniel Lopes:** For example, with Airbyte, we scrape a ton of their pages and created a specific content checker to see if pages are broken before publishing to their Webflow CMS. The deep research is also customized for them because it's technical content we needed to specialize.

**Daniel Lopes:** Some clients want image generation in the mix. We do HTML generation converted to images to follow company guidelines. Freepik is a good example. This client has a specific style, so we have humans select which images the team wants to use when we generate them.

**Daniel Lopes:** But I hope that gives you a sense of what's behind this.

**Matt Hodgson:** No, totally.

**Matt Hodgson:** A few follow-on questions. We've had bad luck hiring or working with SEO consultants. We know what data we have and what insights it can generate, and we know there are people interested. But we lack the ability to bridge the gap between what people are searching for and what we can rank highly for.

**Matt Hodgson:** I know there are people searching for things like "which SOC 2 compliance tool is cheaper," but I don't know if making a page for that will help because I don't know what keywords people are actually searching for.

**Matt Hodgson:** I know there are tools out there, but how do I scale that to everything we have and identify gaps or weak spots in the market where we could build pages with unique, valuable insights?

**Daniel Lopes:** Marcel is the expert to talk about this. The challenge we deal with is clients sometimes requiring seven layers of approval for a page with five searches, or having complicated deployments like Prismatic or GitHub that require per-article deployment. That makes the process much more complicated than it should be. But for simpler clients like Airbyte who just want to refresh all pages and give us Webflow access, we build a couple of workflows first. The cost of covering long-tail keywords drops significantly. If we get personas and writing guidelines right, we hit 90% quality there.

**Daniel Lopes:** We can publish those fast. If those pages get the keyword searches we expect, we double down. We put a person on rewriting the article if necessary, designers on improving images, and iterate the workflow for more pages.

**Daniel Lopes:** The long-term play works if you have a system that produces work well enough—not someone spending a week writing each article. You can't just use cloud code to ask for an article; it'll be totally off.

**Daniel Lopes:** You need to find what's doable super fast without putting a person in front of each article for two hours. For the long-tail play of publishing a thousand pages, most people and most domains can't do that. The key is drawing the line: is there enough domain authority and gap in the market?

**Daniel Lopes:** If we tackle long-tail keywords, we can project X searches in a cluster. We take that cluster, adjust the researcher to point to the API you're confident about. These strategy-level decisions are critical. If we skip to implementation, we often get stuck with IT teams waiting two months for CMS access. That's why strategy comes first.

**Yousef Hamade:** In terms of getting data over: should we give GrowthX access to Webflow to publish directly? Or should we avoid giving direct access to our back office and instead have them put content in Airtable, which we ingest into our back-office system?

**Matt Hodgson:** Webflow has CMS built in—you could use that as the source of truth. We downgraded our tier when we stopped using it heavily, but we could upgrade. We don't have anyone internally approving content necessarily, so the bar is very low. We'd be comfortable experimenting. That sounds good.

**Daniel Lopes:** We should have a calibration phase—maybe 20 articles—where you review them to make sure they're correct. Then we go forward using your internal data. That helps a lot instead of just tapping the internet, which is full of SEO crap in the top 10 results.

**Daniel Lopes:** Using internal data is even better. We can use data from APIs, internal Airtables, or RAGs we load ourselves. For Augment, it's Supabase—a workflow scrapes GitHub, puts it in Supabase, then Airtable where editors review and clean it up. That Airtable feeds back to Supabase, which the app consumes. So the CMS was essentially Supabase.

**Matt Hodgson:** If we need a database, we can figure something out—that's not hard. Is this a good way to describe GrowthX? You seem fairly hands-on and able to customize and do a lot of work. That's different from tools like Surfer. You seem much better suited for teams that don't have an internal dedicated person for this.

**Daniel Lopes:** Yeah, that's our sweet spot. From a product perspective, we were defining our ideal customer profile a couple weeks ago—who are the easiest people to serve that we do really well for and they're happy.

**Daniel Lopes:** It's usually teams with a small marketing team that's overwhelmed and needs help. AI should boost their productivity, but they don't have time to learn all this stuff—we can do it for them.

**Daniel Lopes:** Or teams with nobody—we do everything for them. They need a lot of content, not just five articles a month but 20-50. Or if it's programmatic content consuming a database, even more.

**Daniel Lopes:** You still want somebody reviewing all articles—our editorial team does that. Our typical setup is a strategy sprint that looks at your space: does it need a lot of data?

**Daniel Lopes:** How hard are the competitors? What can you get?

**Daniel Lopes:** We see if the client benefits from 20 pages a month or 10 pages a week of super high quality, or from catalog pages like we did for Ramp.

**Daniel Lopes:** Those have different complexities. For editorial content production, we can do much higher volume than typical companies because of our automations. But it's still a team of three people who spend a big chunk of their week manually reviewing articles, iterating with our scripts, and publishing.

**Daniel Lopes:** Sometimes they have a publisher who manually puts things in the CMS. We also have people looking at your Google Search Console, Looker Studio, or AEO data to see if the strategy is working.

**Daniel Lopes:** During the strategy phase, Marcel and I—as strategists—come up with clusters and decide how many pieces you should publish to move the needle.

**Daniel Lopes:** This part is super hands-on. We need your team engaged—especially you or your marketing folks—helping us think about topics and giving us access to personas, jobs-to-be-done, interviews, and internal stuff so we can write the artifacts that really influence content.

**Daniel Lopes:** After that, we come up with the roadmap and projects. If it's simpler, it's very deterministic—how much effort and cost. Then we have the team working for you, producing X pages on that timeline.

**Daniel Lopes:** If we need a custom app like we did for Augment, it becomes software dev consulting. Sometimes it's fixed timeline or fixed scope, depending on engineer availability. There's a custom aspect that feels like a dev shop, but we build a lot of reusable stuff.

**Yousef Hamade:** My understanding of the immediate need is to enrich and refresh back-office content with X pieces of data—like FAQs for each company or product, generated from public or internal data. It's a lot of programmatic content refresh.

**Yousef Hamade:** That's one area. Another is versus pages—like you did with Ramp—comparison pages or product cluster pages. Not just X versus Y, but X versus Y versus Z versus ABC. Or pages that list the top five products and cross-link to other pages.

**Yousef Hamade:** Third, blog posts and buyer's guides. From when Marcel met with Shaker, those blog pages are actually our highest-traffic pages. We need CTAs on them and to constantly refresh them to maintain PageRank.

**Matt Hodgson:** The overall strategy is to funnel the right traffic—people likely to use a pricing estimate tool. It's not just traffic quantity; it's getting the right people to our estimate experience, our pricing insight generator, so they enter what they're thinking about buying.

**Matt Hodgson:** They give us their email and we give them pricing data. We currently have supplier listing pages. I bet there's low-hanging fruit in product-level pages and versus pages. The core is getting people who will interact with the widget to those pages.

**Matt Hodgson:** That's the goal. It's not just growing traffic. Especially in the LLM world, companies like G2 are seeing massive click-through declines because Google and LLMs just answer the question from their content. That's not going to stop. But what we hope is when LLMs answer the question, they say "go to vendor.com to use the pricing widget for a personalized estimate."

**Matt Hodgson:** That way we still get click-throughs. Because there's no generic answer for "I need a personalized estimate for my specific use case." Once the content exists, they use it.

**Daniel Lopes:** Uh, yeah.

**Matt Hodgson:** Yeah.

**Matt Hodgson:** It's about making sure the content references "go to Vendor to get an estimate." That's the goal.

**Daniel Lopes:** It's that or you generate enough of the funnel so when they get the overview answered, but they still need specifics—"For X users, my SLA needs, how much is that?"—which points them to the widget.

**Daniel Lopes:** They get the LLM answer, then the widget reference. It's impressive how fast they index citations. We've seen Augment picks up in citations within one hour.

**Daniel Lopes:** Or in ChatGPT, with exact language we used. ChatGPT is doing it now too.

**Daniel Lopes:** Search "top coding agents" and Augment wasn't mentioned. We published a couple articles, and it picked up exactly our wording. We can't guarantee it happens always, but when it does, it's impactful.

**Matt Hodgson:** You're measuring that? You're seeing the LLM references too?

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So like we're building the tool internal in this platform where now we're using like every client that we sign up, we create a workspace for them in the tool called Scrunch.

**Daniel Lopes:** And then we'll, in that assignment creation process or during the strategy phase or during the creation of the article, come up with like, what are the prompts that people will try to look for this?

**Daniel Lopes:** And then we add just content and essentially we'll run them daily and track the citations and also brand mention.

**Daniel Lopes:** So even if it's not linking, if it's mentioned in your brand, they track that too.

**Daniel Lopes:** And then we keep an eye on that.

**Daniel Lopes:** So, and sometimes we'll try to create things specific for that.

**Daniel Lopes:** And we've seen that like FAQs, for example, do really well.

**Daniel Lopes:** Comparison pages do really well.

**Daniel Lopes:** Super up-to-date content does really well.

**Daniel Lopes:** It has...

**Daniel Lopes:** Fathom kind of makes sense because it's like you're probably just using a reg with a vector database and the closest you get to the prompt semantically, that's how people will probably search and judge it into your perplexity.

**Daniel Lopes:** And the recency makes sense too.

**Daniel Lopes:** It does all think that we're trying to reverse engineer from seeing the ones that do the best.

**Matt Hodgson:** That's really, I mean, that's the biggest thing for me is like, how do we figure out what those questions are?

**Matt Hodgson:** I mean, we can all guess, right?

**Matt Hodgson:** But like, how do we figure out exactly what those questions are that we can then generate the FAQs for?

**Matt Hodgson:** Because I do think there's a large set of questions that we can answer where we're like, would be the best information.

**Daniel Lopes:** You're good to business on all of that.

**Matt Hodgson:** Yeah.

**Daniel Lopes:** Your business is perfect for it.

**Matt Hodgson:** Yeah, so we can actually answer a lot of questions.

**Matt Hodgson:** It's just like, well, what questions should we do?

**Matt Hodgson:** Should we do?

**Matt Hodgson:** So...

**Yousef Hamade:** So, yeah, I mean, it'd be fun to tackle it, I think.

**Yousef Hamade:** And Daniel, from what Marcel said, the question stuff comes out of the strategy sprints, right?

**Yousef Hamade:** And the reporting is part of the, like, weekly or bi-weekly reporting that the team does back to Vendr.

**Daniel Lopes:** Yeah, usually the way the team does that, like, they will come up with, like, rough topics, like, the cluster of things you want to cover, and then they will come up with, like, on traditional SEO, will be coming up with, like, and URLs that rank well.

**Daniel Lopes:** And for GEO, we're thinking, like, what are the prompts?

**Daniel Lopes:** We will come up with lists and then create the content out of that and see, and then have people monitor on a weekly basis to see if it's moving to it or not.

**Matt Hodgson:** And today we do, like, you, like, generate those prompts.

**Matt Hodgson:** I mean, they're almost always going to be like supplier or product specific in our case.

**Matt Hodgson:** And you generate them and then you stand them up as like FAQs.

**Matt Hodgson:** And then if you're seeing that that specific prompt is like referencing it a lot, then you stand up like a whole page answering that question or something like that, right?

**Daniel Lopes:** Yeah, yeah, yeah.

**Matt Hodgson:** Go from, use that as a guide to go from kind of short form to long form.

**Daniel Lopes:** Yep, yeah, exactly.

**Daniel Lopes:** We can see like in Scrunch, it's not great.

**Daniel Lopes:** That's why we're building our own version of it.

**Daniel Lopes:** But it's enough to see what the LLM answered.

**Daniel Lopes:** So like they will store the result.

**Daniel Lopes:** And then we'll look at that as, okay, that could be a page.

**Daniel Lopes:** The intent of this answer is not precisely what that article that was linked to does.

**Daniel Lopes:** Let's create a page specific to that.

**Daniel Lopes:** So like we're creating pages of how we see the LLM's answer to the questions.

**Daniel Lopes:** So this should point better on that intent.

**Daniel Lopes:** Because the intent of the page...

**Daniel Lopes:** And so usually the page has just one intent, ideally, instead of having like multiple.

**Daniel Lopes:** And that really helps to build a lens.

**Daniel Lopes:** So that's how we're thinking.

**Daniel Lopes:** But we're essentially building the Scrunch to be fully integrated with the whole process.

**Daniel Lopes:** Build our own version of Scrunch and bringing all the stuff in-house.

**Daniel Lopes:** And maybe by the end of the year, all the clients would get access to all the stuff aggregated in one place.

**Daniel Lopes:** And they can see you could follow your own analytics for SEO and GEO in one place combined and have also your vault of data where you can ask questions yourself.

**Daniel Lopes:** And that's kind of what we're building now to the end of the year.

**Daniel Lopes:** But yeah, I know we do a lot of like the team does a lot of manual checks and they are set up for like every week.

**Daniel Lopes:** One of the folks on the editorial team will look at your looker, look at the GEO analytics, cross-reference with our strategy, see if it makes sense, report back to the...

**Daniel Lopes:** To you and to the director of the account and see if the roadmap is still going the right path.

**Daniel Lopes:** So it's kind of the gist of the process.

**Daniel Lopes:** Marcel will do a much better job at explaining it.

**Matt Hodgson:** No, that's fine.

**Matt Hodgson:** I'll talk to him, too.

**Matt Hodgson:** I kind of just wanted to make sure I understood where you guys kind of played and from a technical standpoint, how we might integrate or work together.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Oh, yeah.

**Matt Hodgson:** Just explain the technical.

**Daniel Lopes:** We technical team as well.

**Daniel Lopes:** So we have a client ops engineering team that creates the workflows.

**Daniel Lopes:** And then we decide how much allocation that team will be to each client based on whatever the strategy team comes up with.

**Daniel Lopes:** This is the best way to get these folks to grow.

**Daniel Lopes:** So we have this cycle.

**Daniel Lopes:** have almost three guys just doing Webflow and CMS integration.

**Daniel Lopes:** The cycle before it was all like workflow creation for different use cases.

**Daniel Lopes:** Some stuff around image.

**Daniel Lopes:** And then with augment, we have almost like one person dedicated to that for the next couple of months.

**Daniel Lopes:** We have this small group of people that are super familiar with prompting, with LLM chains, and agents, and evaluations, and all that.

**Daniel Lopes:** And they're the ones creating the workflows that I've shown you.

**Daniel Lopes:** And then we have the platform team that is building this Python that I'm showing you, and that environment that you can see the workflows running.

**Daniel Lopes:** So, yeah.

**Daniel Lopes:** So it's a 12 people effort so far.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Awesome.

**Matt Hodgson:** Pretty cool.

**Matt Hodgson:** I mean, it seems like you're landing some nice accounts for sure.

**Matt Hodgson:** So that's exciting.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Each account is a little bit of a different challenge because you have the edges.

**Daniel Lopes:** The edges are the challenge user.

**Daniel Lopes:** Like in your case, the edge would be like getting the data from your APIs.

**Daniel Lopes:** Or some other accounts, the edges, they are CMS.

**Matt Hodgson:** But you can always figure that out.

**Matt Hodgson:** I think that'll be, I think it'll be pretty easy for us.

**Matt Hodgson:** So, yeah.

**Yousef Hamade:** In terms of, like, building these pipelines, because it seems like each pipeline is intended for, like, one piece of content being generated, right?

**Yousef Hamade:** In the case of, like, you know, the need to generate, like, I don't know, 18,000, you know, company profile refreshes or something like that.

**Yousef Hamade:** Is it really 18,000 workflows, or is it one workflow that would just pull in, you know, the data and just iterate 18,000 times?

**Yousef Hamade:** Like, how's that going to work?

**Daniel Lopes:** Yeah, the pipeline, we have the, the workflows are the units, and the pipeline is how we stitch them together.

**Daniel Lopes:** So that grid that I was showing you, it's the pipelines, would probably have, in that case, it would be probably one custom.

**Daniel Lopes:** Workflow at the beginning to get the data, and then the other steps might be the same.

**Daniel Lopes:** And like in this case, we have like a workflow that is templated article generator that will take in, let's see, some of the runs here, the executions.

**Daniel Lopes:** That will take in something, like this is for a company that does ticketing, and they have like the template here, let me just switch to raw.

**Daniel Lopes:** So this is the complex of the company, the template in this case is, another research data is PI and past as well, but their template at the end here will be a markdown with like whatever format that they need.

**Daniel Lopes:** They usually be a comparison table.

**Daniel Lopes:** So it's a tool name and alternatives, some predefined with some guideline in between, and a table with the comparison, and then it will populate.

**Daniel Lopes:** The template with the, it's not going to render here, but it does render on the other side.

**Daniel Lopes:** We'll populate the template with that research data that we've had.

**Daniel Lopes:** That's how we handle sometimes, but sometimes they will have a very specific way of generating a page with a very different HTML structure or something like that.

**Daniel Lopes:** Then we might create a custom one instead of just using our general templated article generator.

**Daniel Lopes:** So happy path, like we can use all of our existing 100 different workflows we have, and we just stitch them together with custom documents and custom knowledge base, and then we're good.

**Daniel Lopes:** Worst case scenario, we have to create a bunch of custom workflows, and that takes a little longer.

**Daniel Lopes:** Workflows are usually super fast to create, so we created our own framework for that, and we have an agent for creating workflows, and the team is essentially orchestrating that.

**Matt Hodgson:** You've got a workflow for creating workflows?

**Daniel Lopes:** Yep.

**Daniel Lopes:** Yep.

**Daniel Lopes:** Okay.

**Daniel Lopes:** Exactly.

**Matt Hodgson:** Makes sense.

**Matt Hodgson:** Cool.

**Daniel Lopes:** All right, man.

**Matt Hodgson:** Well, thanks, I appreciate you taking the time.

**Daniel Lopes:** For sure.

**Matt Hodgson:** I feel like we should definitely push forward here and really dig in.

**Daniel Lopes:** I'm excited to see how we can help.

**Daniel Lopes:** You guys are the perfect, in my mind, the type of company that actually has the data, has benefits from this kind of work.

**Daniel Lopes:** Sometimes people will be like, oh, I need to do this, and you're like, you're just like, called leadership.

**Daniel Lopes:** It's just your CEO writing it, you know?

**Daniel Lopes:** But in your guys' case, like, it's a catalog of data, and you guys have all the answers for things.

**Daniel Lopes:** It really is aligned with the product.

**Daniel Lopes:** That's the best.

**Matt Hodgson:** Nice.

**Daniel Lopes:** Cool.

**Matt Hodgson:** I'm excited.

**Matt Hodgson:** All right.

**Matt Hodgson:** Thanks, man.

**Matt Hodgson:** All right.

**Matt Hodgson:** Thank you.

**Matt Hodgson:** Have a good one.

**Matt Hodgson:** Talk to you soon.

**Matt Hodgson:** See you soon.

**Matt Hodgson:** All right,
