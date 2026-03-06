# How We Audit a Brand

<metadata>
purpose: Internal operator's guide to GrowthX's end-to-end brand audit methodology — the steps, the reasoning, and the judgment calls
audience: Operators (EMs, strategists, analysts) and engineers building tools and automation
access: build-team
last_updated: 2026-03-05
</metadata>

---

Everything we do serves one outcome: help brands grow their visibility with search engines and AI so they get more traffic, more engagement, and more conversions.

That sounds simple. It's not.

The landscape shifted. Buyers now ask ChatGPT, Perplexity, and Google's AI Overviews which tools to use — and those engines build shortlists before a human sales rep ever gets involved. Traditional SEO still matters. But it's one layer. If AI doesn't recommend you when a buyer evaluates your category, you've lost before the conversation started.

So we built a methodology that covers both channels — search and AI — and maps the full competitive landscape across both. It's eight steps. Each one feeds the next. Skip a step and you're guessing downstream.

This guide explains what we do at each step, why it matters, what to watch for, and what comes out. It's written for the people who run audits and the engineers who build the tools that power them.

---

## Step 1: Know the brand

**What we do.** Deep research on the company. Products, business model, target personas, positioning, value props, go-to-market motion. We're building a complete picture of who they are and what they're trying to be.

**Why.** You can't score what you don't understand. Every judgment call downstream — which buying categories matter, which competitors are real threats, which content to audit, what "good" looks like — depends on understanding the business first.

This isn't a checkbox step. It's the foundation that prevents garbage-in-garbage-out in every subsequent step. An operator who doesn't understand the brand will miscategorize competitors, miss relevant markets, and draw wrong conclusions from the data. An engineer needs to know this because brand context feeds directly into CheckThat brand profiles, category tagging, and prompt design. If the context is thin, the AI measurement is unreliable.

**What to watch for.** Don't trust the company's own marketing copy at face value. Cross-reference with analyst coverage, customer reviews, and community discussion. What the brand says it does and what the market thinks it does are often different — and that gap is itself a finding.

**What comes out.** A brand context document that everyone on the team can reference. This becomes the answer key we check AI's narrative against later.

---

## Step 2: Map the ecosystem

**What we do.** Identify every market and buying category the brand competes in. Research what analysts, review sites, and reputable sources say about each category — how big it is, how mature, who the recognized players are, how the category is defined.

**Why.** Brands don't exist in one market. Vercel competes in frontend frameworks, deployment platforms, edge computing, and developer experience tools. Each category has different competitors, different buyer expectations, and different AI behavior. If you only audit one category, you miss the full picture.

The ecosystem map also determines which CheckThat categories we need. If we're going to measure AI visibility for this brand's competitive set, we need categories with evaluation-stage prompts, brand profiles, and active data collection. This step tells us what categories to build or match.

Look at Gartner Magic Quadrants, Forrester Waves, G2 category pages, industry reports, and analyst commentary. Some categories are mature and well-defined (CRM, project management). Others are emerging and messy (AI agents, vertical SaaS). Both are valuable — emerging categories are where the competitive landscape is most volatile and AI's recommendations shift the fastest.

**What to watch for.** Don't default to the brand's self-described category. A brand might call itself "an AI-powered collaboration platform" but analysts bucket it under project management. The categories that matter are the ones buyers actually search for and AI engines actually organize around.

Also look at how analysts and review sites define the boundaries of each category. Some brands sit at the intersection of multiple categories with significant overlap. Map all of them — the audit needs the full picture even if the final report focuses on a subset.

**What comes out.** An ecosystem map: a list of buying categories with market sizing, maturity assessment, and the key sources that define each one.

---

## Step 3: Find every player and rank them

**What we do.** For each buying category from Step 2, build a list of the top 50-100 players. Pull from analyst reports, review sites, community recommendations, and market signals. Score each one across 15 reputation dimensions and tier them.

The 15 dimensions: trust, innovation, ease of use, value, support quality, security, scalability, integration, domain expertise, thought leadership, product quality, speed, transparency, customer-centricity, modernity. Each scored 1-10 with a rationale. (Details in the [competitor brief methodology](https://handbook.growthx.ai/guides/skills/competitor-brief).)

Beyond the 15 dimensions, gather business signals: revenue momentum, headcount and headcount growth, public vs private, funding or valuation (or market cap if public). These signals show which companies are real and growing versus which are stagnating or zombie-walking.

Tier them:
- **Leaders** — Recognized by analysts and review sites, strong market presence, real revenue
- **Established** — Solid players with meaningful adoption but not top-of-mind
- **Emerging / Low Presence** — Growing or new, some traction, not yet widely recognized
- **Off the Map** — Exist but barely register with analysts, reviews, or community

**Why.** We're building the universe of competitors before we measure anything. This prevents selection bias — the tendency to pick only the obvious five names and miss the emerging threat that's gaining ground fast.

Scoring across 15 dimensions now, even roughly, makes it much easier to track changes over time. When we re-run this in 90 days, we can see which brands moved and in which dimensions.

For engineers: this data structure is the foundation of the competitive set. Every subsequent measurement — SEO traffic, AI visibility, citation analysis — maps back to this list. Build for updates, not snapshots.

**What to watch for.** Companies with multiple brands and domains. Mailchimp is part of Intuit. HubSpot acquired Clearbit. Brands rebrand. Products merge. You need a way to group entities while tracking at the domain level — domain is always the unique ID.

Don't confuse "presence on review sites" with "market significance." Some companies game G2 with review campaigns but have tiny real adoption. Others have massive enterprise deployments but few public reviews. Use the business signals (revenue, headcount, funding) to calibrate.

**What comes out.** A tiered competitor list with reputation scores per category. This is the competitive universe we'll measure everything against.

---

## Step 4: Size up their web presence

**What we do.** Quick SEMRush pull on every player from Step 3. Domain authority score, estimated organic traffic, total pages indexed, number of ranking keywords, traffic trend (growing/declining/stable). This is a scan, not an audit.

**Why.** This is triage. We need to know who's a traffic giant (2M+ organic visits/month) and who's barely visible (500 visits/month). A company that analysts rank highly but has almost no web presence is a very different competitive threat than one that dominates search results.

This step also starts revealing mismatches — and mismatches are diagnostic. A brand with strong analyst recognition but weak organic traffic has a content or SEO problem. A brand with massive traffic but mediocre reviews might be riding a few high-volume pages that don't convert. A brand with explosive traffic growth is worth watching regardless of its current tier.

By now, you're also naturally filtering out players that don't belong: dead companies, irrelevant products that analysts grouped into the category incorrectly, tiny niche tools that don't actually compete.

**What to watch for.** Traffic estimates are estimates. SEMRush and DataForSEO can disagree by 2-3x on the same domain. Use them for relative comparison (who's bigger than who) rather than absolute numbers. The ranking within the set is more useful than any individual number.

Also watch for domains with artificially inflated traffic. A brand with 500K visits/month but 80% of traffic going to a single "free calculator" page is not the same as one with 500K visits spread across product and educational content.

**What comes out.** A competitive traffic scorecard appended to the tier list. Now each competitor has reputation scores and web presence data side by side.

---

## Step 5: Map the AI visibility landscape

**What we do.** Match each buying category from Step 2 to a CheckThat category. If one doesn't exist and should, escalate — we need to create it with evaluation-stage prompts, build brand profiles for every relevant player, and start collecting data. The goal: every vendor we discovered in Step 3 that's still in business should have a CheckThat profile and be tagged to the right categories.

Create a workspace in CheckThat with all competitors from the tier list. Then for every player, pull:

- **AI Presence score** — 30-day average plus the range (min, median, max)
- **Citation share** — what percentage of AI responses in this category cite their domain
- **Mention metrics** — total mentions, average rank position, percentage in top 3, percentage in top 5, full rank distribution

Four CheckThat scores provide the full picture:
- **Presence** — Does AI recommend you when buyers ask about your category? (The unaided awareness test for AI.)
- **Reputation** — What does the world think, independent of AI? Reviews, press, community, analysts.
- **Perception** — What story does AI actually tell about you? Six attributes: capability, usability, value, trust, support, innovation.
- **Influence** — How much control do you have over what AI says? Which sources drive the narrative?

(Scoring details and formulas live in the [CheckThat handbook](https://handbook.growthx.ai/products/checkthat/metrics). This guide is about what the scores mean for the audit, not how they're calculated.)

**Why.** This is where we answer the question no one else can: when a buyer asks AI for recommendations in this category, who shows up? That question didn't exist three years ago. Now it's one of the most important questions a brand can answer.

The AI visibility data layered on top of the reputation and SEO data from earlier steps creates a picture that's genuinely new. You see things like:

- A category leader with 80+ reputation that AI barely mentions (crawlability or content structure problem)
- An emerging player with modest reviews but 40%+ AI presence rate (they optimized for AI before anyone noticed)
- A brand that shows up in AI but with zero citations from their own domain (their presence is fragile — built entirely on what others say about them)

Each of these patterns has a different diagnosis and a different fix. That's what makes the methodology work.

**What to watch for.** Many players will be zero or near-zero in AI visibility. That's expected. Most B2B brands today are invisible to AI during evaluation — only about 30% maintain stable AI visibility. Zero is itself a finding.

Watch for the gap between Reputation (Step 3) and Presence (this step). High reputation + low presence is a specific diagnosis: the market loves them but AI doesn't surface them. That usually points to a technical or content structure problem, not a brand problem.

Also watch for brands with AI presence built entirely on third-party content (high presence, low source control). That's fragile — one G2 profile update or one Reddit thread fading from recency could change their visibility overnight.

For engineers: category-to-workspace mapping and competitor tagging are things we should automate. Ideally, when we define a competitive set in Step 3, the CheckThat workspace populates automatically.

**What comes out.** An AI visibility scorecard for the full competitive set. Now every competitor has reputation, web presence, and AI visibility data.

---

## Step 6: Pull it all together

**What we do.** Combine market positioning (Steps 2-3), reputation tiers (Step 3), search visibility (Step 4), and AI visibility (Step 5) into one competitive landscape view.

**Why.** No single dataset tells the story. A brand can be a category leader by analyst opinion, have decent organic traffic, and still be invisible to AI. Or the opposite — strong AI presence built on thin third-party content that could evaporate next month.

The synthesis reveals the real competitive position and the real threats. It also reveals opportunities — categories where the brand has room to grow, competitors whose AI visibility outstrips their actual product quality, gaps in the market where no one has strong AI presence yet.

Present this as a landscape, not a spreadsheet. The audience — whether internal team or client — needs to see the shape of their market. Where do they sit? Who's above them? Who's closing the gap? Where are the openings?

**What to watch for.** Resist the temptation to present every data point. The synthesis should tell a story with a handful of clear themes. "You're strong in search but invisible to AI." "You're the analyst favorite but your web presence doesn't match." "Three competitors are rising fast in AI visibility — here's why." The data supports the themes; it doesn't replace them.

**What comes out.** A competitive landscape report with the brand's position mapped across market presence, reputation, search visibility, and AI visibility.

---

## Step 7: Go deep on the brand's website

Now we turn inward. Everything up to this point was about the brand's position in the market. This step is about what's actually on their website and how it's performing.

Two layers.

### 7a. Site structure audit

**What we do.** Pull the full sitemap and map every page on the site. Classify each page by section and purpose:

- **Brand** — homepage, about, careers, press
- **Transactional** — pricing, signup, contact, demo request
- **Ecosystem** — integrations, partners, marketplace
- **Documentation** — docs, API reference, guides, tutorials
- **Educational** — blog, resource center, webinars, reports, case studies

Apply this taxonomy based on what we learned in Steps 1-2 about the business and its ecosystem. A developer tools company will have a huge docs section that matters. A marketing SaaS might have almost no docs but a massive blog. The taxonomy should match the business, not a template.

For each section, measure:
- Total pages
- Pages with zero organic traffic (dead weight)
- Total organic traffic for the section
- Traffic per page
- Number of ranking keywords
- Traffic per keyword
- Share of pages vs share of traffic

**Why.** You can't audit content if you don't know what's on the site or how it's organized. Most sites have large sections that are invisible — hundreds of pages generating zero traffic — and small sections that carry all the SEO weight. A blog with 400 posts where 50 drive 90% of traffic looks very different from a blog with 100 posts evenly distributed.

The share-of-pages vs share-of-traffic metric is particularly revealing. If a section has 40% of the site's pages but only 5% of traffic, that's dead weight dragging down the whole domain. If a section has 10% of pages but 60% of traffic, that's where the value lives — and probably where we should focus.

For engineers: page classification is something we want to automate. Given a URL and the brand context from Step 1, we should be able to classify most pages programmatically. Edge cases need human judgment, but the bulk should be machine-labeled.

**What to watch for.** Don't trust the sitemap alone. Many sites have pages not in the sitemap, or sitemaps that include pages that shouldn't be indexed. Cross-reference with SEMRush's indexed pages to get the real picture.

Also watch for sections that look healthy in aggregate but are propped up by one or two outlier pages. A blog section with 50K visits/month sounds good until you realize one viral post from 2023 accounts for 40K of it and everything else is declining.

**What comes out.** A site structure map with traffic data per section.

### 7b. Content and SEO audit

**What we do.** For selected sections — usually content and educational pages, sometimes docs — go page by page. For each page, pull:

- 12-15 months of organic traffic history
- Full keyword ranking data (current and historical)
- Traffic trajectory classification: **freefall** (>50% decline), **declining** (10-50% decline), **stable** (within +/- 10%), **growing** (10-50% growth), **surging** (>50% growth)
- Page health score (0-100) — technical vitals: load speed, mobile-friendliness, accessibility, structured data
- Content quality score (0-100) — a snapshot assessment, not a diagnostic deep-dive

Data comes from SEMRush and DataForSEO for traffic and keywords, PageSpeed and accessibility tools for page health.

**Why.** The trajectory classification is more useful than a point-in-time snapshot. A page with 500 visits/month that's declining 20% month-over-month is a very different situation than one with 500 visits/month that's growing. One needs rescue. The other needs fuel.

Trajectory also reveals the overall health of the content program. If 60% of pages are declining or in freefall, the content engine is broken regardless of what total traffic looks like today. If 40% are growing or surging, there's momentum to build on.

We keep this as a snapshot assessment — we're forming a picture of what's working and what's not. The detailed diagnostic ("here's exactly what's wrong with this page and how to fix it") comes later if they become a client. At this stage, we want to know the shape of the problem, not every crack in the foundation.

**What to watch for.** Don't score every page on the site. Focus on the sections that matter for the brand's growth — usually content/educational and sometimes product pages. Scoring 1,000 documentation pages that serve existing customers isn't useful at this stage.

Content quality scoring at scale is inherently rough. Flag obvious problems (thin content, missing meta data, no internal links, duplicate content) but don't pretend a 0-100 score captures everything. It's a triage tool, not a diagnosis.

**What comes out.** A content and SEO audit with trajectory classifications, health scores, and quality scores for the selected sections.

---

## Step 8: Form a hypothesis and recommend a plan

**What we do.** Take everything from Steps 1-7 and turn it into a story. What's really going on? Where are the biggest opportunities? What should this brand focus on for the next several months?

This is high-level and example-driven. Not a task list. Not a detailed export. The brand should walk away knowing what to focus on and why — the granular execution plan comes later.

An example hypothesis: "Your AI visibility is low despite strong market reputation because your content strategy was built for search engines circa 2020. Your pages rank for keywords but don't answer buyer questions directly — which is what AI engines need to cite you. Meanwhile, three competitors have restructured their content for AI citation and are showing up in 40%+ of evaluation prompts. Here's what we'd focus on for the next six months."

**Why.** Data without interpretation is noise. The audit generates a massive amount of information — competitive tiers, reputation scores, traffic data, AI visibility metrics, page-by-page health scores. None of it means anything until someone connects the dots.

The hypothesis is where the methodology earns its value. It's the moment where all the measurement becomes a recommendation. And it only works because we did the first seven steps in order — we understand the brand, we know the ecosystem, we've measured both search and AI visibility, we've gone deep on the website. The hypothesis is informed by all of it, not just one slice.

**What to watch for.** Don't try to cover everything. Pick the 3-5 most impactful themes and make them sharp. A recommendation that says "improve your content" is useless. A recommendation that says "your blog has 300 posts but only 40 drive traffic — consolidate the dead weight and redirect the equity to your top performers, then restructure those top pages for AI citation" is actionable.

Keep the recommendations proportional to the brand's resources. A startup with a three-person marketing team can't execute the same plan as an enterprise with 50 people in content. The hypothesis should fit the situation.

**What comes out.** A strategic recommendations document. High-level themes, supported by evidence from the audit, with enough examples to make the direction clear.

---

## How this compounds

Each step makes the next one smarter.

Brand context shapes ecosystem mapping. Ecosystem mapping defines the competitor universe. Competitor ranking reveals who matters. SEO sizing separates real threats from paper ones. AI visibility shows the new battlefield. The synthesis reveals the true competitive position. The website audit shows what's working and what's broken. And the hypothesis ties it all together into action.

When we re-run this 90 days later, every layer updates. We can see which competitors gained ground. Which AI visibility scores shifted. Whether the brand's content trajectory improved. Whether the hypothesis was right.

That's the point of a methodology instead of a one-off audit. The framework stays the same. The data refreshes. And every cycle, the picture gets sharper.
