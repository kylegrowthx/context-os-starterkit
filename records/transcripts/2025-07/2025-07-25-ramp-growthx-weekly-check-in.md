# Ramp<>GrowthX Weekly Check-In

<metadata>
date: 2025-07-25
time: 14:00 UTC
duration: 18 minutes
organizer: vivek@growthxlabs.com
participants: Luke Tubinis (Ramp), Matt Angelosanto (Ramp), Victoria Naef (Ramp), Mara Leighton (GrowthX), Vivek Shankar (GrowthX)
fathom_recording_id: 76496475
fathom_url: https://fathom.video/calls/358815613
share_url: https://fathom.video/share/G8Zurju6HFRBs5TVYE7YyxfYzNgewmFR
source: fathom
enriched_on: 2026-03-03 15:45 UTC
</metadata>

---

## Summary

Ramp and GrowthX reviewed content performance across blog, per diem, vendor, and tuning pages, with Ramp's "versus" pages outperforming alternatives and blog sessions increasing for a second consecutive week. The team discussed expanding into industry-specific AI tool content and identified opportunities to enrich existing overview pages rather than launching new ones, while awaiting feedback on recent vendor pages and working through automation challenges for publishing. GrowthX committed to researching industry-specific content expansion, delivering data wrapper charts, and providing updates on publishing automation progress next week.

---

## Context

Ramp is a spend management platform that GrowthX supports with content marketing. This is a recurring weekly check-in where Vivek Shankar (GrowthX's content lead) reviews SEO and traffic performance across Ramp's content properties, while Victoria Naef (Ramp's product/content counterpart) and the Ramp team provide direction on strategy and flag production blockers. The relationship is active and collaborative, with GrowthX delivering content updates weekly and Ramp iterating on strategy based on performance data. This particular week's check-in focused on the strong performance of vendor "versus" comparison pages and opportunities to move beyond their current keyword targeting into industry-specific content that accounts for different vertical needs.

---

## Relevance

**To GrowthX Delivery:**
- Vendor "versus" pages dramatically outperforming alternatives pages since June 30th, validating comparison-style content format for software tools
- Publishing automation facing data-saving and backend presentation issues; GrowthX targeted to deliver update next week
- New markdown-based table creation method will unblock content workflow and reduce manual edits for structured data
- Need for proprietary metrics/benchmarks when claiming model superiority for specific industries; enriching existing pages more viable than standalone new pages

**To CheckThat:**
- AI overviews now appearing mid-page instead of top for per diem searches, reducing visibility impact
- Ramp considering industry-specific AI tool comparison content ("best AI tools for marketing agencies"), which aligns with CheckThat's AEO positioning
- Lack of proprietary model benchmarking data is limiting competitive advantage in AI tool rankings

**To GrowthX Business Development:**
- Account health: Ramp team on-site in New York, strong engagement, weekly collaboration continuing
- Expansion signal: Victoria Naef exploring new keyword categories (pricing pages) and industry verticals, indicating deeper content scope
- Production velocity improving: blog sessions increased for second consecutive week; vendor page traffic building after June 30th pivot to "versus" format

---

## Overview

- Blog sessions increased for the second consecutive week, with AI expense management page performing well
- Per diem pages saw a slight drop in sessions, partly due to new .gov domains appearing in search results
- Vendor "versus" pages are outperforming alternatives pages; team considering industry-specific AI tool content
- Publishing automation for overview pages hit some snags but progress is being made

---

## Key Topics

### Content Performance Overview

  - Blog: Second consecutive week of increased sessions
      - AI expense management page received high traffic
      - Other top performers: cash budget, late fees on invoices, six forecasts, IRS receipt requirements
  - Per diem pages:
      - Slight drop in overall sessions over past 3 weeks
      - New York, DC, Oregon, Florida lost the most traffic
      - New .gov domains appearing in search results (e.g., defense travel management office, Florida ports)
      - AI overviews now appearing mid-page instead of top
  - Expense category pages: No major changes
  - Tuning pages: Assets and liabilities performed best
  - Treasury pages: Drop due to liquidity position report losing clicks
  - Vendor pages:
      - "Versus" pages performing best since June 30th
      - Shopify and Figma overview pages in top 20
      - Alternatives pages not attracting much traffic

### Content Strategy Discussion

  - Team considering capturing traffic from pricing and other keywords
  - Exploring industry-specific AI tool content (e.g., "best AI tools for marketing agencies")
  - Debate on creating new pages vs. enriching existing overview pages with industry-specific information
  - Challenge: Lack of proprietary metrics/benchmarks for industry-specific model comparisons

### Content Refresh Performance

  - 4-5 URLs separated from existing blog pages
  - July 7th publications (procurement challenges, e-invoicing) showing improved performance (20 and 12 sessions)
  - Other refreshed content showing slight improvement, needs more time to evaluate

### Production Updates

  - Awaiting feedback on latest vendor pages and content refreshes
  - Datadog overview page: Questions about cost relative to category
  - Victoria to create data wrapper charts for three new categories by Monday

### Publishing Automation Progress

  - Hit snags with automation for overview pages due to complexity
  - Issues with data saving and backend presentation
  - Testing publishing into Sanity instance with test vendor
  - Update expected next week

### Technical Updates

  - New method for creating tables using markdown in the workflow coming soon
  - Will address current table and chart creation limitations

---

## Action Items

**Vivek Shankar (GrowthX)**
- Research ways to expand/dive deeper into industry-specific content for existing overview pages; present findings to team
- Provide update on publishing automation progress next week

**Victoria Naef (Ramp)**
- Create data wrapper charts for 3 new categories by Monday

**Luke Tubinis (Ramp)**
- Update team on new markdown-based table creation method for content workflow

---

## Transcript

**Mara Leighton:** Weekend plans?

**Vivek Shankar:** Got some good stuff coming up. There's some good music festivals playing in the city right now, so probably go for one.

**Mara Leighton:** Anything fun coming up?

**Vivek Shankar:** My friend just texted me and she's like, yeah, let's go. So, yeah, it's a good time to be in Lisbon right now.

**Mara Leighton:** How long does the music season last?

**Vivek Shankar:** It starts in spring and goes on till the end of summer, which over here is early October. So it's a long season, yeah.

**Vivek Shankar:** Also, just mentioning right now, but I booked two weeks off in September. I'm going to Peru.

**Vivek Shankar:** Hey, Victoria, how are you? Happy Friday.

**Victoria Naef:** Happy Friday. This week we had the team here in New York, too. So thanks for the flexibility in pushing to today.

**Mara Leighton:** How did the on-site go?

**Victoria Naef:** It was great. It's good to have everyone in person.

**Mara Leighton:** Hey, Matt. Were you in New York as well for the week?

**Matt Angelosanto:** Yeah, I got back last night. My train got canceled yesterday, well Luke's too, so we had to find new ways home. It's nonstop, there's no time to recoup.

**Mara Leighton:** I hope over the next three weeks, in aggregate, you get back to your baseline.

**Vivek Shankar:** Okay, so we can get started. Quick run through the performance.

**Vivek Shankar:** For the blog, we had a second consecutive week where sessions increased. The AI expense management page received quite a lot of hits compared to last week. Basically, these four stood out: cash budget, late fees on invoices, six forecasts, and then the IRS receipt requirements, which we actually refreshed a few months ago. So generally good performance on the blogs there.

**Vivek Shankar:** For the per diem, we're seeing some interesting things. The past three weeks, we've had a slight drop in overall sessions. Generally, New York, DC, Oregon, and Florida have lost the most over the past three weeks, and these were our top performers. In New York's case, there's an additional .gov domain that appeared — a defense travel management office. And across Oregon and Florida, the Florida ports have opened per diem pages.

**Vivek Shankar:** So none of the drop is really attributable to competitive drops. It's more like .gov sites are picking up more space. And something else we've noticed is the AI overviews are not appearing on top of the page for these per diem searches. They're appearing in the middle of the page, so there's the .gov sites, the AI overview, and then the people also ask. The real estate there has kind of changed a bit.

**Vivek Shankar:** The expense category pages, we didn't see any major changes last week. For the tuning pages, assets and liabilities did the best. Audit trails and cash flow statement dropped a few clicks, but not a massive amount. In the second batch of tuning pages, quarterly taxes performed the best, and how to improve cash flow also received a good number.

**Vivek Shankar:** For the treasury pages, we saw a drop mostly due to the liquidity position report losing a ton of clicks. We don't have too many pages in this category, so even if one page drops, the entire performance kind of falls off.

**Vivek Shankar:** Regarding the vendor pages, we're seeing clicks build up. Generally, the versus pages are performing the best. Shopify and Figma overview pages are the only ones showing up in the top 20 since June 30th. So generally, versus pages are the way to go forward. The alternative pages don't seem to be attractive. For the AI batch, we can give it a few more weeks to see whether they do well. But in the older batches, alternatives have not been showing up much. The best performer is the ClickUp Alternatives page, but that's only received like eight hits, and we published that quite a while ago.

**Vivek Shankar:** I just want to stop there, because I know last week you had requested a deeper dive into some of these things. So I just want to check if there's any questions.

**Victoria Naef:** No questions. I think one other thing we've been thinking about is how could we capture traffic from pricing and other keywords, whether that's with the existing pages or maybe creating new pages, and getting more granular with the industry. So best AI tools for marketing agencies, for example.

**Vivek Shankar:** Yeah, with regards to the best models for industry verticals, we're seeing a lot of LLM evaluation companies publish those kinds of pages. They're using customer data, like what we're doing with spend data. But they're using usage data and applying model benchmarks. It might be good to launch that as an experiment, but since Google prioritizes subject matter expertise and relevance to the products, it might be a bit of a challenge to rank. But we can certainly launch it as an experiment.

**Victoria Naef:** And maybe we could test by taking two different categories and testing with specific pages, getting more granular, or adding content to the existing ones with sections for the industries. What do you think?

**Vivek Shankar:** I think we can do it for the overview pages. Maybe "this model is best for these particular industries." I think that might be one way to enrich current pages and see how they do, as opposed to launching brand new ones. What kind of data are you envisioning if we do launch standalone pages?

**Victoria Naef:** Similar to what we have, but getting specific for that industry. So just getting specific on the industry within the content and explaining, sharing context on those numbers for the industry.

**Vivek Shankar:** Yeah, so the pages that are already doing that, the ones I've seen, and some of our clients that are in that space, they use proprietary metrics and benchmarks to prove why that model is best for certain industry use cases. They have charts with actual numbers and graphs saying that based on these metrics, the accuracy or coherence, this is why this model is best for this industry. Unless we have something to that degree, which I don't think we have, we might be better off enriching the existing overview pages instead of launching new ones.

**Victoria Naef:** Makes sense, yeah. We can test it.

**Vivek Shankar:** Yeah. And we'll also look at, based on what you said, ways we can expand this, dive deeper, et cetera. We can do that research on our end and present something for you.

**Vivek Shankar:** Regarding the content refreshes, we're separating four or five URLs away from the existing blog pages. There were two published on July 7th and two more on July 16th. The ones that went on July 7th seem to be having improved performance. So procurement challenges and e-invoicing had about 20 and 12 sessions. The other ones are seeing slight improvement, but it's just going to take more time to see how they're going.

**Vivek Shankar:** That's the performance overview. Regarding the production side of things, we're waiting for your feedback on the latest vendor pages and the content refreshes. Victoria, Nika had some questions about the Datadog overview page. I don't know if there are any updates there.

**Victoria Naef:** What was that — the category, the cost relative to the category was too high? Yeah, I think so. So for those, we can just keep adding them to that tab on the sheet, and then I'll submit them together so we can update them. For now, we can just hold. And yeah, I know I need to create some data wrapper charts for the three new categories, so I'll have them ready on Monday.

**Vivek Shankar:** Okay, sounds good. And then just want to quickly give an update on the publishing automation. We hit some snags with the automation for the overview pages, mainly because they're the most complex ones, so we decided to tackle those first. There's an issue with the way the data is being saved and the way it's being presented on the backend. But we're almost done with it. I should have an update for you sometime next week. The main issue has just been little niggles here and there, nothing major. We have tested it, and we're testing publishing it into your Sanity instance with a test vendor. So we should have progress to report sometime next week.

**Mara Leighton:** Luke, I know you mentioned this in the chat. Just piggybacking off of the publishing, when I was chatting with Marcel about some of the other blockers, specifically, I think he remembered it as images, but we were talking about those tables and charts. And it sounds like we're not able to adjust the editing permissions, which might allow us to skip over that.

**Luke Tubinis:** I don't know if permissions is the issue. We're going to have a new way to do tables that will just be markdown. So I'm sure you can create those within the workflow. I'll keep moving on that, so you'd have something relatively soon.

**Mara Leighton:** Very exciting.

**Vivek Shankar:** Awesome. Okay, cool. I think that was pretty much it, so there's nothing else.

**Luke Tubinis:** All right. Thanks so much, everyone.

**Mara Leighton:** Hope you all enjoy a restful weekend after the on-site. Thank you. Have a good weekend.
