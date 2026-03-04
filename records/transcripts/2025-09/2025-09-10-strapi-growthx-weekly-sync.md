# Strapi<>GrowthX Weekly Sync

<metadata>
date: 2025-09-10
time: 16:30 UTC
duration: 22 minutes
organizer: Vivek Shankar
participants: Vivek Shankar, Mara Leighton, Paul BRATSLAVSKY, Victor Coisne
fathom_recording_id: 86325733
fathom_url: https://fathom.video/calls/404546250
share_url: https://fathom.video/share/Q2zny6w2tLRyoe_YcBQe4B-tLTh-S7dE
source: fathom
enriched_on: 2026-03-03 14:45 UTC
</metadata>

---

## Summary

GrowthX is on track with Strapi content delivery despite Usman experiencing technical issues due to flooding — 5 articles delivered last week with 9 scheduled for this week, plus 2 refreshes completed and 7 more scheduled. Overall performance increased for the second straight week with blog pages leading; key metrics show demo clicks up and non-branded impressions slightly down (seasonal). Image generation workflow launching next week, with Medium distribution automation tested but needing bug fixes for folder organization and social meta descriptions exceeding character limits. Team agreed to wait until all comparison pages receive rich text updates before removing the redundant large table, focusing on the "at a glance" summary instead.

---

## Context

This is an ongoing weekly operational sync between GrowthX's content delivery team (Vivek, Mara, Usman) and Strapi's marketing leadership (Victor, Paul). GrowthX is executing a major content engagement for Strapi, creating and refreshing technical documentation and comparison pages. The relationship is a service delivery engagement where GrowthX manages content production at scale (9+ new articles weekly), performance tracking via tools like Looker and Scrunch, and workflow automation. This week's sync covered production status, technical challenges (Usman's flooding-related issues), new tooling rollouts (image generation, Medium distribution automation), and strategic decisions about content structure (comparison page table removal once all pages are updated).

---

## Relevance

**To GrowthX Delivery:**
- Workflow automation capability added this week: image generation (rolling out next week) and Medium distribution automation reduce manual effort at scale. Need to fix Medium folder bug and social meta description character limits.
- Team resilience: Usman experienced serious technical issues (flooding), but content pipeline maintained through Vivek and Mara. Two to three weeks of content scheduled ahead, reducing impact of single-person outages.
- Content refresh methodology working: Adding disclaimer callouts for outdated technical articles (e.g., "This covers Strapi v4, see v5 docs here") rather than full rewrites. Victor requested examples; Vivek to show samples in Airtable.

**To GrowthX Business Development:**
- Strapi expanding scope: asking for bulk meta title updates on integration pages (Paul to send list of VNI-generated pages to exclude) and exploring bulk image/meta description refresh on blog cohorts with high traffic but low images.
- Account expansion signals: Strapi investing in content velocity (9 new articles/week), LLM visibility (Perplexity traffic at new high, citations being analyzed), and cohort optimization. Ecosystem cohort at position 16 — room to improve with targeted refreshes.
- Citation performance gap: GrowthX capturing 4% vs competitors' 20% of citations. Team investigating whether low-value informational queries are skewing numbers. Important metric to unlock for Strapi's AEO strategy.

**To CheckThat:**
- LLM traffic data: Perplexity referrals driving new high in Strapi's LLM visibility; ChatGPT referrals steady. Citation attribution low but Scrunch access enabled for 12-week historical analysis (also 4-week and 7-day cohorts).
- Search query categorization: Team recognizing distinction between informational (low-value) and bottom-funnel product-recommendation prompts. Will help Strapi focus AEO efforts on high-intent queries.

---

## Overview

- Content delivery on track despite technical issues; 9 new articles and 7 refreshes scheduled for this week
- Overall performance increased for the second straight week, with blog pages performing best
- Image generation workflow nearly complete; to be rolled out for new articles and select refreshes
- Comparison pages to be updated: big table removed, keeping only "at a glance" summary

---

## Key Topics

### Content Production Updates

  - Refreshes: 2 delivered last week, 7 scheduled this week
  - New content: 5 articles delivered last week, 9 scheduled this week (including comparison pages)
  - Delays due to technical issues (flooding) affecting Usman's work
  - Comparison pages: 4 older samples staged, 3 new pages this week

### Workflow Improvements

  - Image generation workflow nearly complete, expected next week
  - Medium distribution and publishing automation tested; minor bugs identified:
      - Medium articles saving in unexpected folders
      - Social meta descriptions exceeding character limits
  - Bulk update of meta titles for integration pages possible; team to provide list of pages

### Performance Metrics

  - Overall performance increased for second straight week
  - Top performing pages: all from the blog
  - Non-branded impressions slightly down (likely seasonal)
  - Conversion events increased slightly week-over-week
      - Demo clicks increased most
      - Pricing link clicks saw slight dip
  - Monthly performance at similar levels to previous month
  - Cohort performance:
      - Ecosystem tutorials and features saw higher traffic
      - Click performance mostly positive
      - Average position mixed; room for improvement (e.g., ecosystem at position 16)

### LLM Traffic

  - New high in LLM traffic, mainly from Perplexity referrals
  - ChatGPT referrals steady
  - Citations low (4% vs competitors' 20%); team investigating

### Comparison Pages Update

  - Decision to remove large comparison table
  - Keep only "at a glance" summary table
  - Implementation: wait until all pages are updated with rich text before removing table

### Image Generation Workflow

  - To be implemented for new articles initially
  - For refreshes:
      - Applied to GrowthX-created content
      - Not applicable to pages with only summary updates

### Meta Descriptions Update

  - Proposal to update meta descriptions in bulk for Strapi blog
  - Team to investigate feasibility of bulk image generation

---

## Action Items

**Paul BRATSLAVSKY (Strapi)**
- Send list of VNI-generated integration pages to exclude from meta title bulk update

**Vivek Shankar (GrowthX)**
- Follow up on comparison page table implementation decision with Strapi once all pages are updated with rich text
- Share Airtable examples with Victor showing content refresh callout format and disclaimer placement

---

## Transcript
**Vivek Shankar:** I've been in Paul's literally back-to-back.

**Paul BRATSLAVSKY:** Hello.

**Vivek Shankar:** Hey, Paul. How are you?

**Paul BRATSLAVSKY:** Pretty good. How's everybody doing?

**Mara Leighton:** I love whenever anyone's outside. It feels like I get angry.

**Paul BRATSLAVSKY:** I'm such an introvert that part of my routine, I'm like, I have to go outside and be around something green and people.

**Paul BRATSLAVSKY:** You know, otherwise I'll just never go anywhere.

**Mara Leighton:** I've been trying to work at, like, a coffee shop or something a couple days a week for a similar reason of just, like, I also just find that it makes things, the change in environment makes me feel more, like, productive and alert.

**Mara Leighton:** So anyway, you're reminding me that I should be doing that more. The change in environment makes me feel more productive and alert.

**Paul BRATSLAVSKY:** I'm such an introvert that part of my routine is I have to go outside and be around something green and people.

**Vivek Shankar:** It's autumn, so the weather is really good right now.

**Paul BRATSLAVSKY:** Hey, Victor. How are you doing?

**Mara Leighton:** I was getting FOMO seeing the pictures from the happy hour. It looked really fun.

**Victor Coisne:** I was very busy, but you guys really know how to organize events.

**Victor Coisne:** I heard you're doing well on the fundraising side too.

**Mara Leighton:** Thanks. We can go ahead and start when you're ready. Theo said he won't be joining.

**Vivek Shankar:** So, okay, just walking through the updates.

**Vivek Shankar:** For the refreshes, we delivered two last week and seven scheduled for this week.

**Vivek Shankar:** The reason the numbers are lower is because Usman experienced serious technical issues — there's a lot of flooding where he's located. We pushed some refreshes to this week, but we'll get them out this week without any hitch.

**Vivek Shankar:** For new content, we delivered five articles last week and have nine scheduled for this week. This week's numbers include the comparison pages — we've staged four older samples and have three new pages this week. We'll start pushing them out over the following weeks.

**Vivek Shankar:** On the workflow side, our image generation workflow is almost done and should be ready next week. We tested Medium distribution and publishing automation and found a few small bugs. Articles are getting staged in Medium but saving in unexpected folders and not appearing where you'd normally find them in the queue. Also, the social meta descriptions for Facebook and Twitter are exceeding character limits. We'll iron these out.

**Vivek Shankar:** Theodore asked last week if we could update meta titles for integration pages in bulk. We can do that if you send us a list.

**Victor Coisne:** Why don't we do it for all the integration pages?

**Paul BRATSLAVSKY:** Yeah, just exclude the list I sent you of VNI-generated content — we already set the SEO on those. But for all the others, a meta title revamp would be great.

**Vivek Shankar:** Yeah, we can get that done.

**Vivek Shankar:** Not an issue.

**Vivek Shankar:** Moving to performance, we split integration pages we created from Strapi-created ones. Overall performance increased for the second straight week, and even including Strapi's integration pages shows upward trends — it's great to see us breaking out of the plateau we've been in.

**Vivek Shankar:** The best-performing pages are from the blog. Non-branded impressions fell slightly, but we think it's seasonal. Conversion events increased week over week with demo clicks up most and pricing clicks slightly down. Monthly performance is similar to last month, maybe slightly higher, with steady improvement. Ecosystem tutorials and features saw higher traffic, and click performance was mostly positive. Average position is mixed — ecosystem is at position 16, which we can improve. We have refresh articles coming over the next few weeks targeting use cases.

**Vivek Shankar:** On LLM traffic, we hit a new high — mainly from Perplexity referrals while ChatGPT referrals stayed steady. Our presence is increasing compared to competitors over the past few weeks. Citations are lower than we'd like — competitors draw about 20% while we're at 4%. We're investigating that now. We've given you access to Scrunch, so you can explore the data. Any questions?

**Victor Coisne:** Yeah, I have a question, Vivek.

**Victor Coisne:** But when we say, like, use cases and some of the other pages that I've seen in Looker, when we have to keep check, like, for instance, yeah, use cases and features, for instance, like, we're talking about blog posts.

**Victor Coisne:** We're not talking about the feature pages.

**Victor Coisne:** We're talking about blog that cover use cases or cover features, right?

**Victor Coisne:** Yes, these are the blogs that Glowtex has created, yes.

**Victor Coisne:** Okay, got it.

**Victor Coisne:** Okay, just making sure we're not...

**Victor Coisne:** Tracking things, pages that are outside of, makes sense.

**Vivek Shankar:** Cool, cool.

**Victor Coisne:** Yeah, that's really insightful.

**Victor Coisne:** Thank you for that.

**Victor Coisne:** And so for Scrunch, there's historical data.

**Victor Coisne:** How far back can we go?

**Victor Coisne:** I haven't looked too much into it yet, but is there like...

**Vivek Shankar:** think we can go back to 12 weeks.

**Vivek Shankar:** That's the longest.

**Vivek Shankar:** And I think we uploaded your queries within that period.

**Vivek Shankar:** So basically, it's 12 weeks.

**Vivek Shankar:** You can cohort by 12 weeks, 4 weeks, or 7 days.

**Victor Coisne:** So you're digging into the low citation numbers and will share more information when you have it?

**Vivek Shankar:** Right. The numbers depend a lot on what queries we're tracking. The overall citation number appears low, but we need to verify how many are informational queries versus bottom-funnel product-recommendation searches. Informational citations don't drive buying decisions, so we're focusing on bottom-funnel queries.

**Vivek Shankar:** On the comparison pages, I had a question — we're not seeing the big table in the CMS. Is that something you want us to remove?

**Paul BRATSLAVSKY:** I thought we were moving the table below the content, or do you want to remove it completely?

**Victor Coisne:** We discussed this on Slack — the big table is redundant since we summarize it in the "at a glance" table. We don't have bandwidth to update it as it changes constantly. I recommend removing the big table and keeping just the "at a glance."

**Paul BRATSLAVSKY:** Got it. I'll update the issue to remove the table completely.

**Paul BRATSLAVSKY:** All right.

**Vivek Shankar:** So, yeah, is that something, like, how do we do that in the CMS?

**Vivek Shankar:** Because we didn't see an element for that.

**Vivek Shankar:** So that is not in the CMS.

**Paul BRATSLAVSKY:** The table is on the frontend, pulling from a Google data table. We just need to remove the reference and all content will come from the Strapi CMS rich text block.

**Vivek Shankar:** We'll set that and ping you. Quick note — I'm out of office next week and the week after. But Mara and Usman are here, so there's no coverage gap. We have everything scheduled for the next two to three weeks.

**Victor Coisne:** Great.

**Victor Coisne:** I'm excited about the image generation workflow. What's the rollout plan? We can use it on net new articles first for quality assurance, then apply to refreshes?

**Vivek Shankar:** We can do it for net new. For pages we created and are refreshing, we can include generated images. For other refreshes where we're just adding a summary, it doesn't make sense since we're not updating the content itself.

**Victor Coisne:** So for content you didn't create, you're just adding a summary at the top?

**Vivek Shankar:** Correct. Since we're not updating the text, older software versions still show in the content. But we add a disclaimer at the top — like "This covers Strapi v4, see v5 documentation here."

**Vivek Shankar:** Our process identifies which parts need updating for software versions and adds disclaimers like "This refers to Strapi v4, check v5 documentation here" for any mentioned software.

**Victor Coisne:** Where can I find an example in Airtable?

**Vivek Shankar:** Go to Published in Airtable and I can show you examples.

**Victor Coisne:** We're mainly a Notion company, so Airtable is still new to me.

**Mara Leighton:** Yes, there's a lot going on in a single Airtable view.

**Mara Leighton:** To give some context — we want fresh updated content, but some pieces would require too much effort from Strapi's team to fully revise. This disclaimer approach is a middle ground. We're also working on identifying the top 10 performing technical articles to recruit community members to help update them.

**Victor Coisne:** That's a good compromise. I'd like to see an example of a refreshed article to understand how the disclaimer stands out. The goal is to make sure people don't waste time on outdated content.

**Vivek Shankar:** In Airtable, you can view this in the Assignments tab under Refresh — you'll see the URLs. I can show you an older refresh and a newer one to see what the disclaimer callout looks like. There's also a Refresh Candidates view with different statuses showing which articles we've already refreshed, which are in queue, and which ones Theodore and Paul identified as GrowthX or Strapi responsibility.

**Victor Coisne:** Once the image workflow is ready, I'm also thinking — why not do bulk meta descriptions for the Strapi blog too? We can pull a report of missing meta descriptions and find cohorts with high traffic but low image ratios to refresh on both images and meta descriptions.

**Vivek Shankar:** We can do meta descriptions that way. For images, we need to check with engineering if it works at scale — generating images is time-consuming, especially running 100 URLs at once. We'll check internally.

**Victor Coisne:** We can do it progressively — start with net new, then refreshes, and eventually scale to more articles. It seems like a low-effort, high-impact opportunity.

**Vivek Shankar:** Absolutely.

**Paul BRATSLAVSKY:** Coming back to the comparison pages — we can't remove the table right away since not all articles have been updated with rich text. If we remove the table, non-updated articles would be blank. We could add a toggle in Strapi CMS to control whether the table shows, or we wait until all pages are updated with rich text and then remove it.

**Victor Coisne:** Let's keep the table for now. I'll update all the pages with rich text, then we remove the table when everything's done.

**Paul BRATSLAVSKY:** Those pages get minimal traffic anyway, so it's not urgent.

**Vivek Shankar:** Sounds good. We'll follow up on everything in Slack this week. Enjoy my vacation! Thanks, everyone.

**Victor Coisne:** Thanks, have a great trip.
