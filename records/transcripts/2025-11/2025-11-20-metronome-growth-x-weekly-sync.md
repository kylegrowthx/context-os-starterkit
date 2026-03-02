# Metronome <> Growth X - Weekly Sync

<metadata>
date: 2025-11-20
time: 20:01 UTC
duration: 33 minutes
organizer: matthew@growthx.ai
participants: Matthew Panzarino, Megan LaFlamme, Will Watters
fathom_recording_id: 103288545
fathom_url: https://fathom.video/calls/477563333
share_url: https://fathom.video/share/bfWqfGHrhCKJw47VUKNRTL6wYnppyZNS
source: fathom
enriched_on: 2026-03-02 00:00 UTC
</metadata>

---

## Summary

Growth X and Metronome aligned on four major refinements to Metronome's LLM pricing reference pages: flexible Webflow CMS tables to accommodate variable column structures (Perplexity has 7 columns, DeepSeek has 4), condensed "Key Features" into a 4-5 item summary focused on pricing-relevant capabilities, removal of negative "complaints" from "Customer Sentiment" to avoid alienating potential customers, and strengthening "Metronome's Take" to provide expert perspective beyond generic news summary. For complex multi-model companies like Base 10, Growth X will assess prevalence across the top 100 before defining a standardized approach. Will Watters committed to drafting improved "Metronome's Take" sections and adding detailed comments to sample pages. Matthew Panzarino will audit the top 100 for multi-model structures and create a Base 10 test draft, while Megan LaFlamme will grant raw code/markdown CMS access and confirm key features guidance.

---

## Context

Metronome is a pricing analytics and optimization platform that has partnered with Growth X to develop a library of LLM pricing reference pages. These pages are designed to help potential customers understand how different AI/LLM companies structure their pricing models. Matthew Panzarino leads the Growth X team on this project, which recently onboarded a new team member (Katia) to handle day-to-day operations. Will Watters, Metronome's product marketing lead, collaborated with Matthew and Megan LaFlamme (Metronome's product operations) to review content drafts and align on structural and editorial standards for the reference pages. The pages are built on Webflow CMS and aim to serve both LLM citations (supporting AI-generated answers) and organic search traffic from users researching pricing models.

---

## Relevance

**To GrowthX Delivery:**
- Established flexible table design pattern for Webflow CMS to handle variable pricing column structures without forcing standardization, reducing future content rework
- Confirmed need for raw markdown/code access to Webflow CMS (not rich text editor) to automate table generation at scale
- Defined "Key Features" as 4-5 pricing-relevant bullets plus summary paragraph, reducing content bloat and editing time
- New team member Katia will take over day-to-day delivery; Matthew remains available for strategy

**To Metronome Product & Marketing:**
- Multi-model companies (Base 10, OpenAI) require strategic assessment — prevalence check across top 100 will determine if custom solutions vs. standardized template needed
- "Metronome's Take" sections need stronger expert POV (current versions too generic); V2 roadmap includes pricing-to-best-practices mapping with "deploy to sandbox" CTA
- Customer sentiment quotes must be pricing-specific (clarity, value, limits) rather than general product praise; complaints removed to avoid alienating prospects
- Pages serve both LLM citations and organic search; collated pricing tables perform well in AI-generated answers

**To GrowthX Business Development:**
- Metronome partnership demonstrates expansion beyond core B2B content marketing services into specialized SaaS/product content
- Positive collaboration signal: Metronome willing to invest in process improvement (raw CMS access, instruction set refinement)

---

## Overview

- **Flexible Tables:** The "Pricing Snapshot" will use flexible Webflow CMS tables to accommodate variable data structures (e.g., Perplexity's 7 columns vs. DeepSeek's 4), avoiding a restrictive, standardized format.
- **Refined Content:** The "Key Features" section will be a summary paragraph of pricing-relevant features, and the "Customer Sentiment" section will remove negative "complaints" to avoid alienating potential customers.
- **Stronger POV:** The "Metronome's Take" section will be rewritten to provide a more distinct, expert perspective, moving beyond a simple summary of news.
- **Complex Models:** For companies with multiple models (e.g., Base 10), Growth X will first assess the prevalence of this structure across the top 100 companies before defining a standard approach.

---

## Key Topics

### Page Structure & Table Standardization

  - **Problem:** Inconsistent table structures across company pages (e.g., Perplexity has 7 columns, DeepSeek has 4) create a poor user experience.
  - **Solution:** Use flexible Webflow CMS tables that adapt to each company's specific data.
      - **Rationale:** This avoids a restrictive, standardized format that would force the removal of valuable, company-specific pricing details.
      - **Implementation:** Growth X requires raw code/markdown input access in the Webflow CMS (not a rich text editor) to automate table generation and ensure proper formatting.

### Content Refinements

  - **"Key Features" Section:**
      - **Problem:** The current bulleted list is too long and includes irrelevant, fast-changing details (e.g., enterprise security) that aren't core to pricing.
      - **Solution:** Replace the list with a summary paragraph focused on 4–5 key features directly relevant to the company's pricing model.
  - **"Customer Sentiment" Section:**
      - **Problem:** Including negative "complaints" creates a risk of alienating potential customers who may also be customers of the reviewed company.
      - **Solution:** Remove the "complaints" section entirely.
      - **Refinement:** Ensure remaining positive quotes are directly related to the pricing model (e.g., clarity, value) and not just general product praise.

### "Metronome's Take" Section

  - **Problem:** The current content is a generic summary of news, lacking a distinct, expert perspective from Metronome.
  - **Solution:** Will Watters will rewrite this section to provide a stronger, more impactful Metronome POV.
      - **V1 Goal:** A simplified, high-level perspective.
      - **Future Vision (V2):** Evolve into a deeper analysis that maps the company's pricing to Metronome's best practices, potentially including a "deploy to sandbox" CTA.

### Handling Complex Pricing Models (e.g., Base 10)

  - **Problem:** Companies like Base 10 offer multiple distinct models (e.g., GLM 4.6, Quen, Gini) with separate pricing on a single page, which breaks the standard page structure.
  - **Approach:**
    1.  **Assess Prevalence:** Growth X will first identify how many of the top 100 companies use this multi-model structure.
    2.  **Define Strategy:**
          - If rare → Use custom solutions.
          - If common → Develop a standardized template (e.g., a dedicated section with a table for each model).
    3.  **V1 Action:** Growth X will create a first draft for Base 10 to test a potential structure.

---

## Action Items

**Megan LaFlamme (Metronome)**
- Grant Growth X CMS access: provide raw markdown/code input capability in Webflow (not rich text editor only)
- Confirm with Chris: Key Features should be 4-5 pricing-relevant bullets plus summary paragraph

**Matthew Panzarino (GrowthX)**
- Audit top 100 companies for prevalence of multi-model pricing structures; propose standard handling approach if common, custom solutions if rare
- Draft Base 10 page structure as test case for how to handle companies with multiple distinct models (GLM 4.6, Quen, Gini)
- Remove negative "complaints" from Customer Sentiment sections; retain only 1-2 pricing-specific quotes (clarity, value, limits)
- Share finalized instruction set with Will Watters and Megan LaFlamme

**Will Watters (Metronome)**
- Add detailed comments to 1 sample doc (Perplexity) covering: section structure, pricing terminology consistency, CTA language, feature highlights, and sentiment quote selection
- Draft new "Metronome’s Take" sections with stronger expert perspective (V1: simplified high-level POV; V2: deeper analysis mapping pricing to best practices); share with Megan LaFlamme and CK for review

---

## Transcript
**Matthew Panzarino:** How are things? How's it going?

**Megan LaFlamme:** Good. How are you doing?

**Matthew Panzarino:** Very good. Hey, Will.

**Will Watters:** Hey, what's going on?

**Matthew Panzarino:** How are you doing, sir?

**Will Watters:** Not too bad.

**Matthew Panzarino:** Agenda stuff is pretty straightforward. I just wanted to check in on review cycles, if you had a chance to get read in yet.

**Will Watters:** Sorry, let me just pull up the agenda real quick to make sure I'm covering everything.

**Matthew Panzarino:** I also have some notes.

**Will Watters:** So maybe it might be helpful if you want to share your screen and go through one of the docs. I have some structural questions I think will be helpful for the design team, for Chris. I also have questions about terminology consistency across the pages. Megan, I'm happy to discuss this with you, but I think there are a couple of areas we can remove for now and revisit in the future. Whichever page you want, let's just start with that.

**Matthew Panzarino:** Yeah, let's look at it from a Google Doc.

**Will Watters:** Yeah, the Google Doc would be great. I didn't make these comments in the doc because I knew we were going to talk live about it. I'm happy to put them in the doc itself if it's helpful.

**Matthew Panzarino:** You can absolutely treat the doc as your canvas for feedback and all that doesn't interfere with us. The way we work is if you're marking stuff up and recording it, we can then scrape those comments and parse them for updates to our instruction sets — basically new instructions for the model or new context we need to give to the model. That's always valuable.

**Will Watters:** And we will always take it. So if you go to the updated version, that's the one I should be reviewing?

**Matthew Panzarino:** Yeah, exactly.

**Will Watters:** Cool. So I think the pricing at a glance is fine. That makes sense.

**Matthew Panzarino:** So I'm just going to go section by section here if that's helpful.

**Will Watters:** So the pricing snapshot section.

**Will Watters:** So this all makes sense to me.

**Will Watters:** I think that, like, so if you look at, like, perplexity compared, like, perplexity is one of the know.

**Will Watters:** I think DeepSeek is another one where ideally we would have consistency within the table. The way I'm thinking about it, and we've discussed this in Slack conversations with Chris, is how do we create a consistent page flow on a customer-by-customer basis? These companies are different — their pricing metrics and how they present on pricing pages varies. Most fall within four or five columns, but Perplexity is the outlier with seven.

**Matthew Panzarino:** I think maybe there's another company that has eight.

**Will Watters:** Yeah, exactly. What are your thoughts on some level of standardization for this table? Is that possible?

**Matthew Panzarino:** The snapshot table will have high variability because the models differ significantly. The other tables — model analysis and evolution timeline — are pretty standardizable. This is the one we need to decide on. We can package the data however you want. We're not tied to any particular way to present the data. As far as formatting, width, height, how it looks on the page, I think there are two buckets: one standardized format that works for 90% of the pages, and custom-built tables for more complex ones. The onus is not on you to worry about that — if the CMS block supports tables, we can fill the data and make it look good in the publishing process. If you want standardization, we drive towards the minimum: model name, price, and unit. What's the minimum rubric needed? Then eliminate the variable ones for the complex cases. As long as they have those base units, we drive towards that. Those are the two major options.

**Megan LaFlamme:** That first option sounds desirable to me.

**Will Watters:** Yeah, I think that's ideal — as long as the CMS block can import whatever table. But I want to push back on a broader question: how much ownership does Metronome want to have over the narrative? Is this purely looking at Perplexity — "this is how Perplexity prices, just reading the news"? Or do we take a spin on every section? What I mean is the second option — where we say, "At Metronome, we think about pricing this way, and these are the critical things, and here's how Perplexity maps to those metrics."

**Matthew Panzarino:** Right, I see what you're saying.

**Will Watters:** They monetize based on these criteria, and we fit into the Metronome table versus the Perplexity table. Maybe that's a bridge too far though.

**Matthew Panzarino:** It makes some sense to do that.

**Megan LaFlamme:** I'm wondering if we'd get our bang for the buck for that effort. This feels like a reference page to me, so adding another filter to line it up doesn't seem necessary yet. But I think it's an important consideration for future evolution. Eventually we want to use these as landing pages with a call to action to deploy the model into our sandbox. That might be the time to add a translation layer between their pricing and what we deploy.

**Will Watters:** That's where I was leaning. If eventually we want to click a button to deploy this model, we're going to need to do a mapping exercise one way or the other. We need to say, "This is what Perplexity is saying. This is what it means in Metronome, the product."

**Megan LaFlamme:** Right.

**Will Watters:** Is now the time to do that? Or is this V1, where we read the news, show it, and at the bottom in "Metronome's Take" we give perspective on how to do this in Metronome? That could be a bridge. What's missing more broadly from these pages is: we say "we're reading the news," then "Metronome's perspective on why this model fits and how to do this in Metronome." There's more cohesion there than just reading the news throughout. I'm not saying the current approach is bad, but eventually you have to make that shift.

**Will Watters:** Yeah.

**Will Watters:** Yeah.

**Will Watters:** Like eventually we can probably mold this into like a true insights page where it's like, hey, here is an expert opinion on how perplexity prices based upon their business model.

**Will Watters:** These are the billable metrics that make most sense for them to align value and blah, blah, blah, blah, blah, blah.

**Will Watters:** The way that we see this in best practice in Metronome is by setting it up and blah, blah, blah, blah, blah.

**Will Watters:** And once you do this, the output of this is blah, blah,

**Will Watters:** Blah, blah, blah, blah, then you hit send.

**Will Watters:** Hey, you want to do this?

**Will Watters:** Hit send, right?

**Will Watters:** That's the, I think, the ultimate version that we want.

**Will Watters:** But right now, I think it's a little bit more of like, let's just get the mindshare on the page.

**Will Watters:** Here's kind of their evolution.

**Will Watters:** And maybe it's also like we can probably bridge a little bit with like, maybe there's just some like generic copy that we put on the page.

**Will Watters:** So like we skip, you skip that to like the pricing evolution.

**Will Watters:** We could add boilerplate copy explaining why we discuss pricing evolution and a Metronome CTA like "Explore Your Options." I agree with Megan — the first option is our preference.

**Matthew Panzarino:** Can we do the CMS box where we can import the table? We need raw markdown or code input capability — not a rich text editor. What CMS are you using?

**Megan LaFlamme:** We use Webflow.

**Matthew Panzarino:** Great! We can automate this with Webflow for dozens of clients. We can update table formats and verify they look good.

**Will Watters:** Good, we're all set on that front.

**Matthew Panzarino:** They offer GLM 4.6, Quen, and Gini with different pricing. We can present this similar to how we're handling other cases, or by product with a table per product.

**Will Watters:** My initial thought is that we anchor on the product. The goal of the exercise is to examine a company's monetization structure. For example, OpenAI has two independent operating products — the API and something else. I don't have a strong opinion on the Base 10 structure right now. But these are all API products.

**Matthew Panzarino:** Yeah, exactly. Here's my approach: First, we look at the top 100 companies to see how many have this multi-model structure. Before we spend enormous CPU cycles, let's see if it's a couple of one-offs we can custom-solve, or something systemic. Second option: we could do an overarching section with clusters for each model (API model, DeepSeek cluster, Quen cluster, etc.) on the same page. The only complexity is that it affects the "Pricing at a Glance" section. If this structure is pervasive across the top 100, we need a standardized approach. If it's only three companies, we custom-solve it.

**Will Watters:** Large companies have individual business units with their own pricing structures, so I'd expect more. Maybe take a first pass at Base 10 to see how you'd organize it.

**Will Watters:** Instead of jumping into pricing, I want to make sure we start with the business model and product overview. Someone trying to price their product should first understand Perplexity's business model, then see how they price.

**Matthew Panzarino:** Right, that makes sense.

**Matthew Panzarino:** So something like the product pricing table, a version of this that appears up here.

**Will Watters:** I mean, that's kind of what I'm thinking, but I don't know, Megan, what do you think?

**Megan LaFlamme:** That makes sense. I see these pages as a reference for people who already know Perplexity and want to understand how it charges. They're not looking for educational content on business models — more like LLM citations and collated pricing data.

**Matthew Panzarino:** Exactly. LLMs love collated data and can cite these pages quickly. The win condition is seeing Metronome logos in citations, signaling authority.

**Will Watters:** For V2, we could adjust the title from "Product Overviews" to "Business Model," but let's not overcomplicate V1. I'll provide suggestions on copy adjustments. You can mark up the docs and we'll talk through feedback.

**Will Watters:** On Key Features and Capabilities — Chris asked if we could do a summary paragraph instead of a bulleted list. There's not much room for 10 bullets on some pages. We should focus on top 4-5 features that are directly relevant to pricing. For example, if product A has additional security protocols that justify different pricing, that's relevant. But performance, infrastructure, enterprise security management — those are table stakes or change too fast.

**Matthew Panzarino:** Right, I agree. Let's focus on 4-5 pricing-relevant features and not make it choppy.

**Matthew Panzarino:** Yeah, yeah.

**Matthew Panzarino:** Chris had sent me this big amount that he had, you know, we had marked up a little bit and I think, okay, yeah.

**Matthew Panzarino:** So this is

**Matthew Panzarino:** We can absolutely summarize the bullets and make sure they're pricing-relevant, not random security features.

**Will Watters:** Good. We've got a few minutes left. The Pricing Model Analysis and Timeline are good. On Customer Sentiment: I think the quotes are good, but remove the complaints. We don't need radical transparency here. Quotes should be about the model and pricing clarity, not general product praise. For example: "I have clarity on my costs because I know what limit I need to hit." Those are more relevant than generic praise. Keep 1-2 pricing-relevant quotes, not more.

**Matthew Panzarino:** I agree. We can find plenty of pricing-relevant quotes. We'll eliminate the complaints.

**Will Watters:** Megan, you're cool with that?

**Megan LaFlamme:** Absolutely.

**Will Watters:** I'll go into the docs and reiterate these points in comments. On "Metronome's Take" — my feedback is we're reading the news too much. We need more perspective from Metronome, not from us reporting. I'll prioritize getting those done today for you, Megan, and CK to review. They'll be simplified to start.

**Matthew Panzarino:** We'll need Megan and CK's eyes on them.

**Will Watters:** They'll be simplified initially and we can explain the perspective as we refine.

**Matthew Panzarino:** Good. I'll look at how to share our instruction set. Metronome gave us internal documentation on how they think about pricing models. We parsed that into a contextual document for the pipeline. But we can easily update the data, tweak it, or change the instruction set. For example, if you want "Give us two simple sentences on a high-level take about this pricing model," we can do that. Don't assume we can only make fine adjustments — we can reset and do broad-strokes changes.

**Matthew Panzarino:** We can reset and do a little broad strokes adjustment to it and then kind of refine from there if you need to.

**Matthew Panzarino:** So take a look at them with that in mind.

**Will Watters:** Okay.

**Will Watters:** Yeah, sounds good.

**Will Watters:** And again, it's not anything that they were like bad.

**Will Watters:** I just think that like, this is a common product marketing thing where it's like, how do...

**Will Watters:** How do we deepen what we're saying?

**Will Watters:** Like, how do we make it more impactful or relevant, unique?

**Matthew Panzarino:** Yeah, all those things.

**Will Watters:** This has been good. I'm juggling other things, but I'll put in my prescriptive guide and comments on pages today, along with new "Metronome's Take" content for Megan and CK.

**Matthew Panzarino:** Hopefully we'll have that in the next couple days. Last item: we're bringing on Katia to handle day-to-day operations. I'll still be around for strategy, but she'll drive forward daily. We're well-tooled up and should be able to get where you need.

**Will Watters:** Cool. Appreciate the time.

**Matthew Panzarino:** Thanks, Will. Talk soon.
