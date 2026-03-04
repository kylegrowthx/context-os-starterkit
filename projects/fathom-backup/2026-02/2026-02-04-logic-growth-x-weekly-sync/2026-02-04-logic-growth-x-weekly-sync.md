# Logic <> Growth X - Weekly Sync

<metadata>
date: 2026-02-04
time: 18:29 UTC
duration: 61 minutes
organizer: team@growthxlabs.com
participants: Azzam Aijazi (Logic), Bailey Seybolt (GrowthX), Steve Krenzel (Logic)
fathom_recording_id: 119774666
fathom_url: https://fathom.video/calls/554059457
share_url: https://fathom.video/share/s-j6AewsEyvEjWMv3eEHj7PLjVAcxo76
source: fathom
enriched_on: 2026-02-27 14:30 UTC
</metadata>

---

## Summary

New content pipeline is live with improved quality, delivering two articles this week; team set a 3-month refresh cadence to keep content current with Logic's fast-moving product. Early SEO signals are strong: "LangGraph Alternatives" already ranks #8, and new articles index within hours, validating the strategy and creating foundation for "How to Build an Agent" guide targeting top-ranking position.

---

## Context

Logic and GrowthX synced to review content strategy progress following a recent recalibration of the content pipeline. GrowthX's engineering team built a new version that delivers higher-quality articles with improved positioning for Logic's engineering-focused audience. This meeting assessed pipeline quality, discussed refresh cadence strategy, reviewed infrastructure integrations (Statsig, image generation API, Check That tool), and evaluated early SEO wins. A key strategic decision was prioritizing correct messaging and audience alignment over preserving outdated SEO rankings when refreshing existing articles.

The broader context is Logic's fast-moving product and industry landscape, which requires content to stay current. The team is balancing net-new article production with a strategic refresh cycle to ensure brand messaging stays consistent with Logic's current positioning, while capitalizing on early traffic wins from comparison and listicle-style posts.

---

## Relevance

- **Content Strategy**: New pipeline delivering measurably higher quality; refresh cadence (3-month SLA) established to keep content aligned with product positioning and market positioning
- **SEO & Traffic**: Early validation of strategy with "LangGraph Alternatives" ranking #8 and "Make.com Alternatives" at #14; fast indexing within hours signals strong content quality
- **LLM Visibility**: 0.5% visibility driven by blog citations and case studies; Check That tool provides more accurate contextual understanding than Scrunch
- **Attribution & Analytics**: Content-to-conversion tracking via Statsig and potential Looker integration; citation tracking for LLM visibility
- **Product Integration**: Image generation API, Statsig access, and Check That tool enable automated content scaling and better performance tracking
- **Long-form Content Strategy**: "How to Build an Agent" guide (ungated, premium asset) positions Logic as authority and drives high-intent traffic

---

## Overview

- **New Content Pipeline:** A new pipeline is live, delivering two articles this week with a "step change improvement" in quality.
- **Aggressive Refresh Cadence:** A 3-month refresh cadence was set for all articles to ensure content stays current with Logic's fast-moving product and industry.
- **Strong Early SEO Signals:** New articles are indexing in hours, and the "LangGraph Alternatives" post already ranks \#8, validating the new content strategy.
- **New Content Asset:** A long-form "How to Build an Agent" guide will be published as an ungated, premium asset to drive SEO and establish authority.

---

## Key Topics

### Content Pipeline & Quality

  - A new content pipeline is live, delivering two articles this week.
  - The first new article is due tomorrow; Rachel (Logic) noted a "step change improvement" in quality.
  - **Action:** Azzam to review \~5 articles in the old pipeline.
      - If quality is poor → flag for Rachel to rerun through the new pipeline.
      - Rationale → Avoid wasting time on granular edits for content that doesn't align with the new strategy.

### Content Refresh Strategy

  - This week's content will mix net-new articles with refreshes of high-performing pages.
  - **Goal:** Test the refresh pipeline's ability to update content with new positioning without hurting existing SEO rankings.
  - **Decision:** Prioritize correct messaging over preserving outdated SEO performance.
      - Rationale → The primary goal is to tell the right story, and these articles aren't direct conversion drivers.
  - **New SLA:** A 3-month refresh cadence was set for all articles.
      - Rationale → Logic's product and industry move too quickly for content to stay relevant longer.
      - Process → Airtable reminders will trigger the refresh cycle.
  - **SEO Tactic:** Update the `published_at` date in StoryBlock during refreshes to signal freshness to search engines.

### "How to Build an Agent" Guide

  - Logic is creating a long-form guide to establish authority and drive SEO.
  - **Format:** An ungated, premium asset (like the Aeroops report example) living outside the main blog.
  - **Goal:** Outrank the current \#1 Google result for the target keyword.
  - **Action:** GrowthX to review the guide and provide feedback on structure and SEO.

### Reporting & Integrations

  - **Statsig Access:** Azzam will add Bailey as a Statsig user to track content-to-conversion attribution.
  - **Image API:** Logic will provide an API key for the image generation service to automate content creation.
  - **Check That Tool:** A Loom walkthrough is coming this week, with logins next week.
      - Rationale → Check That's superior contextual understanding will provide more accurate LLM visibility scores than the previous tool (Scrunch).

### January Performance & SEO Signals

  - **Fast Indexing:** New articles are indexing within hours, a strong positive signal.
  - **Strong Keyword Rankings:**
      - "LangGraph Alternatives" → \#8
      - "Make.com Alternatives" → \#14
  - **LLM Visibility:** 0.5% visibility is driven by citations of specific blog posts (e.g., "e-commerce content moderation") and case studies.
  - **Key Insight:** "Alternatives" and listicle-style posts are driving outsized traffic and conversion lifts.

---

## Action Items

**Azzam Aijazi (Logic)**
- Review ~5 articles in current pipeline; flag off-topic pieces by commenting and tagging Rachel (Logic) for rerun through new pipeline
- Add Bailey (GrowthX) to Statsig for content-to-conversion attribution tracking; investigate Looker integration for automated reporting
- Enable and share image generation API key with Bailey (GrowthX); GrowthX to integrate via API or manual process

**Bailey Seybolt (GrowthX)**
- Set Airtable reminders for 3-month refresh SLA on all articles
- Review "How to Build an Agent" guide; provide SEO structure and positioning feedback to Azzam (Logic)
- Record and send async Loom walkthrough of Check That tool to Azzam (Logic); logins to be distributed next week
- Send LLM citation list (specific queries and article URLs) to Azzam (Logic) from Check That analysis
- Confirm Storyblok/Atlas `updated_at` workflow with Steve (Logic); then systematically update published dates on all refresh cycles

---

## Transcript

**Bailey Seybolt (GrowthX):** Well, a lot's going on. So I'll share our Notion. Is Steve joining today?

**Azzam Aijazi (Logic):** We can jump in, but he is joining.

**Bailey Seybolt (GrowthX):** Awesome. So, blog updates.

**Bailey Seybolt (GrowthX):** Our engineering team has built a new pipeline and we'll be delivering two new articles this week. I haven't seen them yet, but the first should be ready tomorrow.

**Azzam Aijazi (Logic):** Rachel's reviewed them and says it's a step change improvement.

**Bailey Seybolt (GrowthX):** What about those five articles currently in the pipeline for review?

**Azzam Aijazi (Logic):** There are about five articles in the queue for me to review, and we've been moving in the right direction overall.

**Bailey Seybolt (GrowthX):** Go ahead and review them—the more we can get published, the better. If something feels off-brand, just leave a comment and tag Rachel (Logic) specifically. She can run it through the new pipeline since it's designed to fix specific types of issues. Don't waste time on granular line edits; just flag problematic ones for rerun.

**Azzam Aijazi (Logic):** Cool.

**Bailey Seybolt (GrowthX):** I'm also proposing we do a mix this week—net new articles plus some refreshes. I want to test how the refresh pipeline handles our positioning change. Let's start with high-performing pages that already have organic traction, so we can see if the new positioning helps accelerate rankings and test whether the new angle connects with the target audience.

**Azzam Aijazi (Logic):** Okay, cool.

**Azzam Aijazi (Logic):** I have a few questions. First, I'm glad we're discussing refreshes—this was one of my top questions coming in. What should our general refresh strategy be? We've got a lot of articles that feel outdated. Do we have a timeline? Are we prioritizing high-performing articles first, or what's our approach? Also, these existing articles target keywords we wouldn't choose today given our new positioning. I want to update the messaging to be more engineering-focused. But won't pivoting messaging tank performance if we're no longer targeting people searching for "no-code automation"? How do these articles survive a messaging pivot?

**Bailey Seybolt (GrowthX):** For content that's already ranking well, the general guideline is: the less you change it, the better. You want to deepen context, ensure accuracy, and update links. But yes, rewriting from scratch can hurt performance. I wanted to test these high-ranking articles to find the balance—keeping rankings while ensuring relevance and accuracy.

We want to refresh everything so your blog speaks properly to your audience and correctly presents the product. Some of these articles were probably intended for a CEO/business persona that's now secondary. So for each keyword, assess the search intent: Should this be reframed for the engineering persona to capture that keyword from a different angle? Should it stay as a light refresh for the CEO persona? Or is it a complete rewrite?

Refreshes can be just as valuable as new articles, especially if they've already gained visibility. I'd propose a mix of net-new and refreshes each week. Once we understand how the refresh pipeline works, I can build a project plan for weekly capacity.

**Azzam Aijazi (Logic):** That needs a different framing. I'd rather have an SLA on article freshness: no article should be more than three months out of date. If something hits three months without refresh, we need to act. As our volume grows, "N refreshes per week" won't scale to keep everything fresh. Is a three-month SLA reasonable? Our product and industry move too fast—anyone reading messaging from three months ago has an outdated view of Logic. Correct messaging matters more than preserving outdated SEO performance.

**Bailey Seybolt (GrowthX):** Three months makes sense for a fast-moving industry. We can certainly do that. We usually set Airtable reminders based on publication date to trigger the refresh cycle.

**Azzam Aijazi (Logic):** Great.

**Bailey Seybolt (GrowthX):** Regarding the strategy work: I've brought in our directors to update the strategy, KPIs, and content priority plan. To validate the agentic cluster properly, I need expert technical support since search intent there requires deep engineering community knowledge. They're reviewing the strategy and we'll update all documentation and add more agentic keyword topics for review. I'll have an update this week. I'll also update Looker once this is finalized to reflect the new cluster organization going forward. The current monthly report is outdated pending this feedback.

On Statsig: I tried to sign in but it didn't work.

**Azzam Aijazi (Logic):** Let me add you as a direct Statsig user instead of a published sharing link. That should work better. The goal is to show you which articles lead to conversions, right? Not just impressions or clicks, but actual sign-up flows so we know where to invest.

**Bailey Seybolt (GrowthX):** Exactly. We want to connect content to conversion pipeline.

**Azzam Aijazi (Logic):** I'm still figuring out the full tracking on my end, but I'll keep you posted. We could start with manual exports if that's easier.

**Bailey Seybolt (GrowthX):** If you could export to Looker so everything's in one place, that would be ideal. But we can investigate once you have access.

**Azzam Aijazi (Logic):** The numbers are small enough that manual tracking monthly or weekly is fine for now. We can automate later if it proves valuable.

**Bailey Seybolt (GrowthX):** Great. For the image generation—if you want to expose it as an API, we can potentially integrate it directly into our pipeline. Otherwise, we can add images manually.

**Azzam Aijazi (Logic):** Either way works. Let me ask Steve: Can someone outside Logic's org call the Logic API for agents, or do they need to create it in their own org?

**Steve Krenzel (Logic):** If they're just calling the API, we can give them an API key from our org.

**Azzam Aijazi (Logic):** Perfect. I'll handle getting the image generation API set up on our end.

**Bailey Seybolt:** I think the other thing I wanted to make sure that we talk about before I chat through reporting and check that is the, I know you saw the how to build an agent guide.

**Bailey Seybolt:** I was wondering what kind of feedback kind of would be most useful for you or like if you have specific open questions or like how you're thinking about positioning the document strategically just to sort of give a little more context there.

**Azzam Aijazi:** I mean, I guess the things that I was hoping to hear from you, if anything, would be like, what might we do that might help this rank higher more effectively?

**Azzam Aijazi:** Like, is there anything that you see as a little hanging fruit?

**Azzam Aijazi:** Anything that you're seeing that's like, hey, this is like, this is way too long.

**Azzam Aijazi:** This is way too in the weeds.

**Azzam Aijazi:** Like you need better structure.

**Azzam Aijazi:** Anything like that sort of advice would be really, really helpful.

**Azzam Aijazi:** Otherwise, it's I think it's more just a general like FYI.

**Azzam Aijazi:** I mean, if you have.

**Azzam Aijazi:** If you any particular, you know, concerns or questions, I'm happy to answer them.

**Bailey Seybolt:** How are you planning on sort of surfacing it or serving it?

**Bailey Seybolt:** I know it's going to be a lot longer than kind of just, you know, a standard blog post.

**Bailey Seybolt:** How are you planning on, like, is it going to be a download link on your website?

**Azzam Aijazi:** No, I wanted it to be an ungated, like, in my head, I've been calling it like a pseudo landing page.

**Azzam Aijazi:** I'll give you an example of one that I like, which is, like, this Aeroops report.

**Azzam Aijazi:** Hold on.

**Azzam Aijazi:** There you go.

**Azzam Aijazi:** I dropped it in the Zoom chat.

**Azzam Aijazi:** But it's just, like, an original piece of content that lives on its own somewhere.

**Azzam Aijazi:** It's findable by Google on Index.

**Azzam Aijazi:** It's nicely, like, visually laid out and designed.

**Azzam Aijazi:** Yeah.

**Azzam Aijazi:** Gets premium treatment.

**Azzam Aijazi:** It sort of looks and feels like a blog.

**Bailey Seybolt:** Yeah.

**Azzam Aijazi:** I think it's actually important that it not just live on our blog as a blog post, but feel more...

**Azzam Aijazi:** We might even want to add this to our website, footer as a separate primary asset that's linked from more places, but I want to pull out all the stops essentially to make this feel really special and high level and not gate this just so that it does its work on SEO and AEO and gets us as high ranking as possible.

**Azzam Aijazi:** I specifically wrote this looking at what was number one on Google today and trying to beat that just so we can get all the way up there.

**Bailey Seybolt:** No, I think that definitely makes sense.

**Bailey Seybolt:** And we can take a look at it thinking about that.

**Bailey Seybolt:** And I think some of it too is like making it a priority to link to it from blog posts so you get those internal links.

**Bailey Seybolt:** I'm wondering if you plan to do this on a regular basis, like if you want to create a new category under your resources.

**Azzam Aijazi:** Yeah, was thinking about that exact question.

**Azzam Aijazi:** So I think that...

**Azzam Aijazi:** I do want to do it on a regular basis.

**Azzam Aijazi:** I don't know what else, like what other topics we'd want to own that are this important.

**Azzam Aijazi:** I can't think of any other ones on top of my head.

**Azzam Aijazi:** But yeah, I think that there is value in there being like long form content living in some other place.

**Azzam Aijazi:** That probably ideally would have been called resources, but we're already using that for our blogs.

**Azzam Aijazi:** Maybe it's something, maybe it's like assets or something like that.

**Azzam Aijazi:** Guides, maybe it's guides, yeah, guides could work.

**Azzam Aijazi:** But yeah, I would love for that to look and feel in some way different and be somewhere different.

**Bailey Seybolt:** Yeah, I think that makes a lot of sense.

**Bailey Seybolt:** And especially if you plan on doing it on a more regular basis, having that more, those more in-depth pieces, hopefully like ones that can include, you know, more primary sources or, you know, quantitative and qualitative insights that are unique to your business.

**Bailey Seybolt:** Having those be stored somewhere separate, like under resources.

**Bailey Seybolt (GrowthX):** Having those stored separate with internal links from blog posts is good SEO strategy. I'll look at recommendations. We'd want long-form pieces with primary sources and unique insights linked as a priority from all blog posts.

**Azzam Aijazi (Logic):** That sounds great. Please do review. Now is the time to shape it. Any size feedback—small, medium, or large.

**Bailey Seybolt (GrowthX):** Will do. I'll send all three types of Goldilocks feedback.

**Bailey Seybolt (GrowthX):** Alright, we'll do that. On Check That: Our tool is rolling out this week, but it wasn't ready for a walkthrough this morning. I'll record an async Loom and send it over. I'll answer any questions, and we'll distribute logins next week.

**Bailey Seybolt (GrowthX):** January had some positive signals, though cluster changes will shift performance metrics. Articles are indexing within hours, which is excellent—no lingering in the queue. "LangGraph Alternatives" is already ranking at position #8, and "Make.com Alternatives" is at #14. That's an awesome early signal validating the new content approach. We'll monitor rankings in Looker once clusters are updated.

On LLM visibility: Numbers may differ from Scrunch because we're tracking slightly different prompts and organizing competitors differently. We'll discuss this once you're in the tool, but don't be surprised by the difference.

**Bailey Seybolt (GrowthX):** No surprise that we haven't seen major movement yet, but as new content indexes, we should see more. One good sign: Check That has much better contextual understanding of Logic than Scrunch. Scrunch sometimes picked up "Logic" the concept without semantic understanding. Check That filters that out, so visibility scores will be more accurate.

**Azzam Aijazi (Logic):** That's awesome. What's driving that 0.5% visibility? What queries are we appearing in? I'm surprised it's that high.

**Bailey Seybolt (GrowthX):** Once you're in the tool, you can see all prompts where you appear. Looking at citations specifically, we're seeing blog posts cited around content moderation, N8 alternatives, case studies like DroneSense, and zero-touch automation. Mostly original content and use cases. I can send you a detailed list after this.

**Azzam Aijazi (Logic):** So it's our blog posts being picked up, not Logic's homepage. That's great.

**Bailey Seybolt (GrowthX):** Exactly. I'll follow up with a detailed breakdown of what's being cited.

**Azzam Aijazi:** Yeah, I was poking through the numbers yesterday, and I had noticed that that LangGraph article was pulling in some traffic, it seems like the numbers that I'm seeing on StatsAger.

**Azzam Aijazi:** Yeah.

**Azzam Aijazi:** It

**Azzam Aijazi:** Ever so slightly different from what you're seeing, and I'm not sure why that might be, because I think you're tied into Google Analytics.

**Azzam Aijazi:** But regardless, from what I was seeing, it was our number one or two traffic sourcing blog posts already, which was surprising and good to see.

**Bailey Seybolt:** Yeah, well, makes sense why you're ranking at number eight already, which is...

**Azzam Aijazi:** Yeah, that's awesome.

**Azzam Aijazi:** And it could be, I was pulling data just from January 1st to 31st, so that also could be a reason if you're looking at a slightly different...

**Azzam Aijazi:** Yeah, I I was looking at the last, like, three days or so, so maybe that's...

**Bailey Seybolt:** Yeah, okay.

**Bailey Seybolt:** It could be that then that's skewing it.

**Azzam Aijazi (Logic):** Cool.

**Bailey Seybolt (GrowthX):** Beyond individual articles, we're seeing across accounts that comparison posts, alternative posts, and listicles have outsized impact on LLM visibility and traffic. Those drive high-intent traffic and conversion lifts. Definitely prioritize that content type. One more thing: articles need recent publish/update dates to rank well. When we refresh, we need to update the Storyblok date fields so articles always appear current on Google.

**Azzam Aijazi (Logic):** That's important. Recent dates signal freshness. When I'm researching what LangGraph does, I don't want a 2024 article—it's useless for something moving this fast.

**Steve Krenzel (Logic):** The published date is a Storyblok field we can set.

**Azzam Aijazi (Logic):** Could we just always set it to three weeks ago? I want to make sure nothing's ever more than three months old.

**Steve Krenzel (Logic):** We could program that, but Google might penalize artificial date manipulation.

**Azzam Aijazi (Logic):** Yeah, maybe don't do that. But let's ensure nothing goes more than three months without a refresh.

**Bailey Seybolt (GrowthX):** If we stick to the three-month refresh cadence and update dates with each refresh, Google will see fresh signals.

**Azzam Aijazi (Logic):** Perfect.

**Bailey Seybolt (GrowthX):** That was it for me. Anything else to discuss?

**Azzam Aijazi (Logic):** No, just looking forward to seeing the new articles tomorrow.

**Bailey Seybolt (GrowthX):** We'll get them to you tomorrow.

**Azzam Aijazi (Logic):** Thank you both.

**Steve Krenzel (Logic):** Thank you.

**Azzam Aijazi (Logic):** Thank you, Bailey.

**Bailey Seybolt (GrowthX):** Bye.
