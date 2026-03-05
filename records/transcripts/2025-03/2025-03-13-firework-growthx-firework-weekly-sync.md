# [Firework] GrowthX <> Firework - Weekly Sync

<metadata>
date: 2025-03-13
time: 18:31 UTC
duration: 31 minutes
organizer: Prateek Gupta (GrowthX)
participants: Prateek Gupta (GrowthX), Ritesh Kewlani (Firework), Cameron Brown (Firework), Yi Jin (Firework)
fathom_recording_id: 51816335
fathom_url: https://fathom.video/calls/252310274
share_url: https://fathom.video/share/FgXEvUs-EGbMSj6zqmazVdm-NdMA5iwq
source: fathom
enriched_on: 2026-03-04 08:45 UTC
</metadata>

---

## Summary

GrowthX and Firework discussed content performance showing strong momentum with new beauty industry articles generating immediate clicks and impressions. The team reviewed lead generation data, identified tracking inconsistencies that inflated lead counts, and prioritized three initiatives: implementing dynamic CTAs based on blog categories (with fallback to beauty playbook), expanding content into fashion and grocery industries, and developing 10-15 articles on content creation pain points to position Firework's solution for brands. Cameron is finalizing category-based CTA logic in Webflow; content gaps and blog categorization remain the main blockers.

---

## Context

Firework is a video commerce platform for retail brands. GrowthX partners with Firework on content marketing to drive traffic and lead generation for the Firework website, which hosts 321 published articles across multiple industries. This weekly sync tracks performance against key metrics (traffic, leads, conversions) and coordinates next-week deliverables. The relationship is a joint GTM effort focused on SEO-driven content that positions Firework as the solution for brands struggling with content creation and personalization.

---

## Relevance

**To GrowthX Delivery:**
- Content strategy leveraging vertical specialization (beauty, fashion, grocery) is working: beauty articles indexed within one week and ranking on Google with meaningful click volume
- Lead magnet placement requires dynamic, category-specific CTAs rather than generic messaging; static approaches reduce relevance and conversion
- Blog categorization at scale is a roadblock: 75% of 321+ articles tagged as generic "Industry Insights"; automation needed to categorize existing content and support future lead magnet testing
- New positioning angle: content creation pain points (myths, leveraging user reviews, influencer-generated content) are higher-impact than features; consider adding to standard GrowthX content frameworks

**To CheckThat:**
- Firework's shoppable video content and dynamic personalization are core to positioning against competitors; understanding how their AI features drive engagement is valuable for market positioning
- Lead tracking and attribution inconsistencies (forms showing zero-click leads) signal broader challenges in conversion tracking that AI/AEO can help solve

**To GrowthX Business Development:**
- Account momentum is strong: expanded from 5 to 15 leads in Jan, stabilizing at 5-10/month base rate with upside from new content verticals
- Revenue expansion opportunity: Firework interested in testing lead magnet variations across top-performing articles; scope for additional services (A/B testing, landing page optimization) if conversions improve
- Renewal health: Prateek and Ritesh relationship is strong; proactive content planning and clear ownership of deliverables suggest high satisfaction

---

## Overview

- Content strategy showing positive results: New beauty industry articles generating good clicks/impressions
- Lead magnet implementation progressing: Cameron developing dynamic CTAs based on blog categories
- Tracking issues identified: Some lead submissions appear suspicious, internal testing may be skewing data
- Action items: Improve blog categorization, expand content for fashion/grocery, focus on content creation topics

---

## Key Topics

### Content Performance and Lead Generation

- 321 articles published, 13 ready for publishing
- 5 lead submissions last week (4 excluding internal submission)
- Monthly average of 5 leads, with spikes in Dec (10) and Jan (15)
- Potential tracking issues identified: Some leads don't correlate with click data
- Action: Remove internal users from lead reports to improve accuracy

### SEO and Traffic Analysis

- 25k impression growth (15% increase) compared to previous week
- Clicks relatively flat at ~120k average from Google
- New beauty industry articles performing well, generating clicks in first week
- Action: Monitor high-converting blogs to optimize traffic and keywords

### Blog Categorization and Lead Magnet Implementation

- Current categorization too broad (e.g., "Industry Insights")
- Cameron developing dynamic CTAs based on blog categories
- Action: Create more specific categories (e.g., beauty, fashion, grocery)
- Action: Cameron to develop script for automated blog categorization
- Interim solution: Ensure beauty playbook magnet on relevant blogs

### Content Creation Strategy

- Fashion articles ready for publishing, grocery industry focus next week
- Spring-related topics identified (e.g., spring sales, marketing tips)
- New focus on content creation pain points for brands
- Action: Develop articles on simplifying content creation/curation (e.g., myths, leveraging user reviews, influencers)

### Lead Magnet Optimization

- Consider A/B testing lead magnet designs and placements
- Explore more targeted lead magnets for specific topics (e.g., beauty engagement)
- Action: Create specific lead magnets for top 10-20 articles as a test
- Consider testing new industry report as a lead magnet

---

## Action Items

**Yi Jin (Firework)**
- Investigate Gmail submissions on magic button form to understand why business-email-only restriction is being bypassed; update form validation if needed

**Ritesh Kewlani (Firework)**
- Update lead report to exclude internal submissions and test data for accurate baseline

**Cameron Brown (Firework)**
- Finalize dynamic CTA logic in Webflow blog categories; deploy fallback to beauty playbook when lead magnets don't exist yet
- Create/update blog categories for specific industries (beauty, fashion, grocery, home, consumer electronics) to replace current generic "Industry Insights" tagging
- Send Prateek CSV of lead magnet download data by quarter/date range (similar format to overall leads report)
- Consider automating blog categorization using ChatGPT to analyze content and suggest category tags for existing ~650 articles

**Prateek Gupta (GrowthX)**
- Write & publish fashion industry articles (ready content ready for launch)
- Develop new grocery industry content for next week's launch
- Create 10-15 topics on simplifying content creation/curation (myths about video production, leveraging user reviews, influencer-generated content, store associate content) and write articles
- Identify top 10-20 performing articles for targeted lead magnet testing (instead of rolling out across all 321 articles)
- Set up internal linking from existing fashion articles to beauty playbook content

**Samrawit Stifanos Berhe (Firework)**
- Slack Cameron the list of content categories being built for ICP targeting
- Send Prateek the ICP list being built for content prioritization

---

## Transcript

**Yi Jin:** And because Vincent knows Billy's actual location, it's somewhere in New Jersey, you see a profile comes up, but it's not Billy. And it turns out it's a profile of his wife. So the technology is almost there but still cannot differentiate between the exact person in that location. If you get a lot of these matches, you probably get profiles of the wives of enterprise CEOs.

**Prateek Gupta:** I guess they had some of that anyway.

**Yi Jin:** And Vincent tries it himself and it turns out to be the other co-founder Jerry's profile that came up. So it's close, but not exact.

**Prateek Gupta:** Let's get started. I'm not sure whether Vincent will be able to join, but we can proceed. As part of our routine, we'll review what we discussed last week, go over the action items, then cover performance metrics for leads and clicks at both monthly and weekly levels, and finish with our next content plan.

**Prateek Gupta:** From last week's updates, we were working on ICP targeting, which we're close to completing today. For UTM tracking, that's already done for the blogs. Dynamic lead magnet assignment is something we've discussed extensively and requires significant effort, but we'll roll it out over the next couple of weeks.

**Ritesh Kewlani:** Cameron and I have been working on the lead magnet logic. We've categorized blogs into different categories, and for each category, we have a corresponding lead magnet. We have the basic mapping in place. Not all lead magnets have launched yet—the industry report will launch in the next two or three days. Cameron has built the logic, and we've agreed the fallback will be the beauty playbook to start, then we'll keep updating as we get more content.

**Cameron Brown:** I'm putting the finishing touches on it right now, just sorting out what I think is the final bug. Essentially, in Webflow we have two CMS collections: the blog post collection where content is written, and a secondary blog categories collection. Each blog post is tagged with a category. What I've done is add fields to the blog category collection so each category now has a CTA associated with it. Depending on the blog category, it will show the corresponding CTA. The only thing I'm finishing is that some things we want to promote for certain categories haven't been launched yet, so I'm coding fallback logic to show the generic beauty playbook CTA if no category-specific CTA exists. I think I can get this ready in the next few minutes.

**Cameron Brown:** One update though: blogs might not be tagged properly during publishing because the developer tagging them hasn't been consistent. We'll probably have to redo the tagging. I noticed about 75% of the blogs are all marked as "Industry Insights," so we could create more granular categories. The more specific we get, the more powerful and tailored the CTAs can be.

**Prateek Gupta:** We've completed several action items. On monthly leads analysis, we have 321 articles published and 13 from last week ready to publish by tomorrow.

**Ritesh Kewlani:** We saw five lead submissions last week; one was internal, so we need to update the report to exclude internal submissions. I'm seeing Gmail submissions on the magic button form—for example, a lead from Pakistan submitted using Gmail when we require business email. Can you investigate how they bypassed the restriction?

**Yi Jin:** They might have come through the magic button page initially but submitted the demo request through a different form. Can you check the form source?

**Prateek Gupta:** Let me share my screen to show you.

**Yi Jin:** That would help us determine which form is allowing Gmail submissions.

**Ritesh Kewlani:** We need to take an action item to fix that form's email validation.

**Prateek Gupta:** On average, we generate about five leads monthly. December was 10 and January was 15—the two months where we saw significant uptick. The remaining months have been flat at five. I audited January's 15 leads by page to understand the spike. I categorized articles, then checked click trends to see if it was a behavioral change or if specific pages dropped in traffic. I noticed two articles—"Vertical Video" and "AI Demand Personalization"—both saw click drops compared to January and each generated one lead. Apart from those two, clicks have been flat from search. Our ranking for "AI Demand Personalization" actually improved from position 20 to position 11, but clicks dropped. Same with "Vertical Video"—position improved but clicks didn't follow. Some of the suspicious patterns: "E-commerce Trending Strategies" had only four clicks in January but showed as one lead. "Beyond Influencer Marketing Holiday Promotion" had zero clicks but still shows a lead. These things don't add up. I suspect dummy leads from internal testing, which is why the actual January number should be closer to eight to ten leads, not fifteen.

**Ritesh Kewlani:** What I'll do is remove our internal users from the report so any internal testing won't show up as leads.

**Prateek Gupta:** The tracking issues are clear. Articles with zero or minimal clicks shouldn't be generating leads unless the attribution is wrong. We need to look at which articles actually convert and double down on those. We generated 25k impression growth this week—that's a 15% increase compared to last week. Click volume is flatlined around 120k average from Google. The clicks we're getting are from new articles, particularly beauty content published last week. We published eight to ten beauty industry articles that indexed and ranked quickly, generating good click volume in the first week. Articles like "Beauty Brands Using AI Personalization" got eight clicks, "Video Trends for Beauty Industry" generated solid clicks in the first week. These are great indicators.

**Ritesh Kewlani:** I'm assuming all these beauty blogs are categorized under a beauty category, right?

**Cameron Brown:** Actually, there's no beauty-specific category. They're probably all marked as "Industry Insights."

**Ritesh Kewlani:** We need industry-specific categorization. Can we tag blogs internally so if we want to look at just beauty blogs, we can? And when we want to add a targeted lead magnet, how do we do it? Do we do it manually every time?

**Cameron Brown:** Right now, all blogs show the same lead magnet, which is the beauty playbook. That's the exact problem we're solving. We're trying to show different lead magnets depending on category. I'd suggest we add more specific categories like "Beauty Industry Insights" and "Grocery Industry Insights" and tag our blogs more specifically by industry.

**Ritesh Kewlani:** Our strategy of creating blogs for each lead magnet is working. Beauty is getting good clicks and impressions. Can you do something similar for fashion and grocery? Both magnets are already live, so let's write articles for those industries too. Cameron, you can start tagging these blogs to specific industries.

**Cameron Brown:** With 650+ blogs, manual tagging would be tedious. I'm thinking I could write a script using ChatGPT to scrape all blogs, analyze content, suggest categories, and output a spreadsheet. That beats manually reviewing hundreds of blogs.

**Ritesh Kewlani:** Until that automation is ready, let's at least make sure the beauty blogs have the beauty playbook magnet. I'll post the dynamic CTA demo in the GrowthX channel when it's complete.

**Cameron Brown:** I won't launch it right now since some of what we want to promote doesn't exist yet. I can provide a demo branch showing it works. We should launch once the industry report and other assets are ready. We should also decide which categories we want. I'm imagining at least categories for all our major target industries: beauty, consumer electronics, home, grocery.

**Ritesh Kewlani:** Sam has a list of categories we're building content for. She can Slack you. Let's use that. We have about seven more minutes. Samrawit, if you could send the category list and the ICP list being built, that would help.

**Prateek Gupta:** Fashion articles are ready for publishing by tomorrow. We'll start grocery next week and publish before the next call. We'll also add internal links from existing fashion articles to the beauty playbook for an extra boost. I'm also working on spring topics: spring sales, e-commerce marketing strategies, spring cleaning checklist, email marketing tips, and video marketing. I'll publish these next week.

**Ritesh Kewlani:** Those ideas sound good. One thing we've learned internally is that content creation is a huge pain point for many brands. Saying we have an AI-powered solution and a toolkit isn't enough. We need content on how we simplify content creation, curation, and recommendations. Some article angles: myths about video content creation, how brands can create content leveraging user reviews, how to leverage influencers for content, how to leverage store associates. Samrawit has a playbook in progress with this information. If you feed the insights to AI, it'll generate topics.

**Prateek Gupta:** I'll consider this. For prioritization, fashion is ready to go live, so I'll focus on spring content first since that's timely. Then I'll work on grocery, and after that, the content creation topics.

**Ritesh Kewlani:** I think content creation topics should be prioritized. Let's think through 10 to 15 topics and write articles. That will cast a wider net and help us see how this messaging performs.

**Prateek Gupta:** Another consideration: in a week or two, we should test whether visitors to beauty articles are downloading the beauty playbook. If they're not, we need to experiment with lead magnet designs and placements—make it bigger, more prominent, or add exit-intent popups. We need to A/B test.

**Ritesh Kewlani:** We have a HubSpot report showing lead magnet downloads. I can share the link. Do you have access to filter by date range?

**Prateek Gupta:** Can you send me a CSV similar to the overall leads report you shared previously?

**Cameron Brown:** I can send the raw CSV data.

**Ritesh Kewlani:** Cool. Let's do that. One more suggestion: instead of rolling out lead magnets across all 650 blogs, let's focus on the top 10 to 20 performing articles. Create specific lead magnets just for those and test. That way we're hyper-focused, and if someone comes to a beauty article about engagement, they see a beauty engagement magnet, not a generic playbook. The conversion rates will be much higher because it's relevant.

**Ritesh Kewlani:** We also have the industry report that just launched, which is applicable across industries. We should test that too to see if it drives better conversions.

**Prateek Gupta:** That makes sense. I need to hop off now, but thanks for the sync. Send that lead magnet CSV after this.

**Ritesh Kewlani:** Thanks, this was great. Anything else?

**Yi Jin:** We're good.
