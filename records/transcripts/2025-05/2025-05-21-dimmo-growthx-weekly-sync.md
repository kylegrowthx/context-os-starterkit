# Dimmo <> GrowthX Weekly Sync

<metadata>
date: 2025-05-21
time: 19:02 UTC
duration: 25 minutes
organizer: Carrie Chowske (GrowthX)
participants: Prateek Gupta (GrowthX), Dave Capone (GrowthX), Troy Munson (Dimmo), Lucas Swartsenburg (Dimmo)
fathom_recording_id: 64000129
fathom_url: https://fathom.video/calls/306583843
share_url: https://fathom.video/share/GGypz5BX5m1Tsuyn8suuXrrfMkmZvhkX
source: fathom
enriched_on: 2026-03-04 15:32 UTC
</metadata>

---

## Summary

GrowthX delivered a strategic content and technical roadmap update for Dimmo's product reviews site. The team is 105 product reviews deep into a 129-product sales-focused content initiative, with 41 keywords ranking in Google's top 10—but click-through rates are underperforming despite high impressions (82k, up from 75k). Prateek outlined critical technical fixes needed (publication timeline optimization, sub-bullet UI fixes, internal linking, 301 redirects for duplicate content, subdomain cleanup) that will improve crawl efficiency and indexing. Dave Capone introduced himself as the strategic account lead and scheduled follow-up calls with Troy and Lucas to align on Dimmo's growth goals and content strategy direction.

---

## Context

Dimmo is a sales productivity software company focused on workflow automation and content management. GrowthX is managing a comprehensive content marketing engagement with them, building a high-volume product review and comparison content strategy to drive organic search visibility and traffic. This was a weekly operational sync between the GrowthX delivery team (Prateek Gupta leading hands-on execution with support from Dave Capone on strategy) and Dimmo's technical/product leads (Troy and Lucas). The engagement is generating strong rank positions but struggling with CTR optimization, indicating a pivot may be needed toward strategy refinement and technical infrastructure fixes before expanding content further.

---

## Relevance

**To GrowthX Delivery:**
- Content quality and ranking are decoupling from CTR—need to shift focus toward meta title optimization, SERP positioning, and content angle testing before adding more volume
- Publication timeline bottleneck (45 minutes per page) is a capacity constraint that compounds as content volume scales; technical fixes needed to automate formatting
- Duplicate content and indexation issues (product pages vs. blog pages competing for same keywords, subdomain de-indexation) are standard B2B SEO challenges; process improvements in content governance needed

**To GrowthX Business Development:**
- Client is evaluating effectiveness of current content strategy; Dave's strategic intake calls signal opportunity to expand scope beyond just content production into full SEO strategy partnership
- High keyword rank count (41 in top 10) shows execution capability; positioning for renewal/expansion based on CTR wins in next 2-4 weeks as meta title tests run

**To CheckThat:**
- Search functionality and internal linking fixes relate to AI visibility—well-structured internal link graph and clean indexation patterns improve CheckThat crawlability for future AI engine optimization work

---

## Overview

- Content strategy shift: 105/129 sales-related product reviews completed; considering new content buckets for better performance
- Technical fixes needed: publication timeline, UI issues, internal linking, 301 redirects, and search functionality
- SEO performance: 41 keywords in top 10, but click-through rates need improvement; meta title optimization planned

---

## Key Topics

### Content Strategy and Progress

  - 213 articles in pipeline, 105 product reviews completed
  - 129 sales-related products identified, 105 done
  - Considering shift to new content buckets after completing \~10 more product reviews
  - 41 keywords ranking in top 10, but click-through rates are low

### Technical Issues and Fixes

  - Publication timeline needs optimization (currently takes 45 minutes per page)
  - UI fixes required for sub-bullet points and formatting
  - Internal linking improvements needed
  - 301 redirects for blog pages to product pages (potential short-term ranking dip)
  - Subdomain launch.demo.io to be removed due to duplicate content
  - Search functionality not working properly, known issue being addressed

### SEO Performance and Optimization

  - 41 keywords in top 10, but low click-through rates
  - Impressions increased from 75k to 82k
  - Plan to optimize meta titles for top 40 keywords to improve click-through rates
  - Considering more clickbait-style titles and integrating Dimmo's tagline

### User Experience Improvements

  - Rename "Categories" to "Product Demos" or similar for better clarity
  - Update header navigation to include new overview pages

---

## Action Items

**Prateek Gupta (GrowthX)**
- Optimize meta titles for 40 top-ranking keywords focusing on high impression, low click CTR. Implement within 1-2 days to test impact on click-through rates.
- Create and share new content bucket suggestions (beyond product reviews) for next week to expand strategy beyond sales-focused products.

**Lucas Swartsenburg (Dimmo)**
- Update product page meta titles based on Prateek's non-truncated suggestions once received (current titles are truncated by Google, impacting SERP appearance).
- Fix search functionality issue between CMS and search engine (known blocking issue affecting user experience).
- Schedule 15-30 minute call with Dave Capone to discuss Dimmo's business goals and SEO/content strategy alignment.

**Troy Munson (Dimmo)**
- Schedule 15-30 minute call with Dave Capone to discuss Dimmo's business goals and SEO/content strategy alignment.

---

## Transcript

**Prateek Gupta:** Managers like me work directly with clients. Ali leads a couple of content managers, and Dave leads at a more senior level, heading up a few pod leads.

**Troy Munson:** Hey, Troy, nice to meet you.

**Dave Capone:** Nice to meet you.

**Prateek Gupta:** Perfect. So a couple things, Troy—as we keep progressing, I wanted to help with the project with Dimmo in terms of our strategy and content. Carrie will help more operationally, but Dave will be more focused on the overall strategy level. Carrie and I will be working hands-on in terms of content and execution planning. I'll be supporting in the background going forward.

**Troy Munson:** Sweet, sounds good. I get it, growing company.

**Prateek Gupta:** Is Lucas joining us?

**Troy Munson:** He had a project come up, but said he could make it if he can. That's fine. We're going to hand over a lot of the technical tasks to Lev—he's amazing and can get things done quickly. Most technical work will go through Lev, though Lucas will definitely help too.

**Prateek Gupta:** Maybe we can use Slack to keep Lev updated on the list of things he needs to do.

**Troy Munson:** Yeah, that works. Lev does a great job with Fathom calls—Lucas and I will have strategy conversations, send them to Lev, and he goes through everything and knocks it out. If you explain things clearly, Lev can watch the demo and execute. If things need more detail, we can bring Lev or Lucas onto a call.

**Prateek Gupta:** Okay, so anything that helps Lev execute and fix all the tech issues—let's get on it.

**Prateek Gupta:** So just summarizing—we need help with publication timeline fixes. I'm facing almost 45 minutes to take one page live right now because of all the formatting and headings. I have to redo everything with bullet points. For listing pages, we created them and Lucas asked where we link them out. Generally we link in the footer, but our footer is vanilla with not many URLs. I'm thinking we could add it in the header under a Resources column.

**Troy Munson:** Okay, great. And this will be software alternatives, features, and so on.

**Prateek Gupta:** We need to still place a T01 on these URLs. These are 15 alternatives pages that were initially posted in the blog, then moved to a subcategory. We're waiting to place the T01 redirect on these 15 pages.

On the product UI side, the current system doesn't give us options for sub-bullet points. There's a bullet point and a sub-bullet point option in the CMS backend, but they're not displayed on the front end. We need UI fixes for that.

**Troy Munson:** So when you say sub-points, you mean nested bullets with a tab underneath the first bullet?

**Prateek Gupta:** Right. It exists in the CMS backend but doesn't show on the front end. I'll recheck that with Lucas's fix.

**Prateek Gupta:** Internal linking is something we've been discussing—we want to implement two different internal linking approaches. I've also prepared a list of product review blog pages that need 301 redirects. The issue is keyword cannibalization: pages like Nukes reviews exist in both the blog and product sections. We want to 301 from blog to product pages. I've checked which product pages are actually indexed by Google. About 5-6 product pages aren't indexed, so when we do the 301 redirect (like Aurum review from blog to product), we'll lose the blog page's ranking while the product page has almost no chance of ranking since it's not even indexed yet.

**Lucas Swartsenburg:** So these are new 301s? I didn't see this list shared before.

**Prateek Gupta:** No, I wanted to discuss it first because there are 6-7 product pages not indexed. The issue is duplicate content—both blog and product pages are trying to rank for the same keywords, so Google won't index the duplicates. That's why I'm requesting the 301 redirects. But I want to flag that this is a long-term solution. In the short term, we'll see a dip in clicks and impressions because those 5-6 pages aren't indexed yet.

**Lucas Swartsenburg:** Any idea why they're not indexed?

**Prateek Gupta:** Duplicate content. Both sets are competing for the same keywords.

**Lucas Swartsenburg:** Okay, that makes sense. That's fine then.

**Prateek Gupta:** There were two products I couldn't find product pages for: Phone Burner Review and Unitas AI review.

**Troy Munson:** Those should be gone. They shut down. I thought I removed them from the CMS, so the product page might be unpublished but the blog page is still live.

**Prateek Gupta:** Right. So for those two, let's place a 301 redirect to the homepage instead of letting them become 404s. That way we preserve any backlink value.

**Troy Munson:** Okay, I'll check on that.

**Prateek Gupta:** All clear on the 301 list, Troy and Lucas?

**Troy Munson:** Yeah, all good.

**Prateek Gupta:** One more thing: we have a subdomain, launch.demo.io, with duplicate pages. It's getting indexed but has zero search performance. Should we de-index the entire subdomain?

**Troy Munson:** Yeah, I can remove that.

**Prateek Gupta:** All these are crawl and indexation issues I'm identifying so we can optimize Google's crawl budget and improve indexing.

**Lucas Swartsenburg:** I noticed our videos are starting to get indexed on Google. I requested revalidation of a lot of pages because Google was saying videos weren't on video pages. I started that on the 10th, and Search Console validation is still running—seems really slow.

**Prateek Gupta:** Search Console validation is like that—it's also very inaccurate. Many times the fix is already applied but it still shows as an error. There are lots of issues with that validation unfortunately. Let's give it time, but the fix should come through eventually.

**Lucas Swartsenburg:** Got it.

**Prateek Gupta:** There's also another list of 15 alternatives page 301s that I shared last week.

**Lucas Swartsenburg:** I'll make it work.

**Prateek Gupta:** We're in week 15 right now. We have 213 articles in the pipeline, with 105 pages completed on product reviews. We identified 129 sales-related products and have completed 105 of them. I have about 10 more sales-related products I can cover. But after that, we'll have covered all the sales-related products. So the question is: do you want me to continue with more product reviews, or should we change strategy? We've already done 105 articles—maybe we should evaluate their performance first and try new content buckets before jumping into more reviews.

**Troy Munson:** Do we know what's working best—reviews, alternatives, or other content types?

**Prateek Gupta:** Out of almost 150 articles published, we have 41 articles in the top 10 of Google. We have lots of features and alternatives content ranking in the top 10, but unfortunately the clicks aren't coming in for those tools. The rank positions are good, but the click volume we expected is definitely not happening.

**Troy Munson:** Yeah, that's the big concern right now—the clicks. We talked about clickbait-style titles, but we really need to figure out what drives clicks. How are other companies getting clicks when we're ranking decently well on some of these?

**Prateek Gupta:** We could try exploring other content topics outside of pure product focus—maybe some longer-tail, lower difficulty keywords where we can rank in AI overviews and Google's top 10 to see if we can drive more clicks.

**Troy Munson:** That's worth trying. I looked at the limbless features keyword—I see we're ranking, but when I typed it, all the other results say "limbless reviews," "limbless features setup and tips," and our title is "best limbless features for smarter sales outreach." Our title looks different, which could be good or bad. I always prefer our titles to stand out, but maybe we need to change our approach.

**Prateek Gupta:** Right, standing out gives users something different instead of reading the same meta titles. We have 41 keywords ranking in the top 10. Over the next week, I can redo meta titles for around 20 of those keywords—make them more clickbait-optimized and test the impact. But there's one issue: our current meta title "watch a free demo plus all you need to know" is getting truncated by Google. I've looked at 40-50 product reviews and most are truncated. We'll need to redo these completely.

**Troy Munson:** That makes sense. Maybe we could integrate our tagline, like "watch a limbless demo without a salesperson" or something.

**Lucas Swartsenburg:** If you come up with good suggestions, let me know and I'll make the updates.

**Prateek Gupta:** I'll Slack you the new suggestions.

Compared to last week, we had a small increase of seven clicks. Our impressions went up—we were stagnant around 75k for the last three weeks, now we're at 82k. So impressions improved but clicks remain the challenge despite good keyword rankings.

**Lucas Swartsenburg:** Also, there's a search functionality issue I'm working on—there's a problem between the CMS and the search engine.

**Prateek Gupta:** One more important point: your header says "Categories" but as a new visitor, that's confusing. The term doesn't give users context for what you're categorizing. Could we rename it to something clearer for user navigation?

**Dave Capone:** We could call it "Sales Demos" with a hover to provide context about what's available.

**Troy Munson:** Or "Product Demos" since there are more than just sales demos.

**Prateek Gupta:** So these are all the tech updates we need: publication timeline fixes, internal linking (which improves crawlability and indexation), removing the launch subdomain (which optimizes crawl budget), and other structural improvements. If we get these done, we'll improve crawling, indexing, and rankings.

**Lucas Swartsenburg:** Did you see that Lev created overview pages for the software alternatives and such?

**Troy Munson:** Did Lev create those overview pages for the software alternatives?

**Prateek Gupta:** I just checked—they're already in the header. So they're discoverable from the navigation.

**Lucas Swartsenburg:** Good, so nothing else needs to link to them. They're in the header now.

**Troy Munson:** Right, that's what we talked about early on—having those in the resources tab.

**Prateek Gupta:** So looking ahead at next week: I'll optimize the top 41 keywords ranking in the top 10, focusing on those with high impressions but zero clicks. I'll redo their meta titles to be more clickbait-optimized and implement by today or tomorrow so we have a week to see the impact. Second, I still have about 10 more sales products to cover to finish the sales-related product list. After that, I'll share new content bucket suggestions for next week.

**Lucas Swartsenburg:** The search functionality is a priority for me—I'll fix that. I'll also implement the meta title updates quickly once you send them.

**Prateek Gupta:** I'll get back to you on the meta titles since our current ones are getting truncated.

**Dave Capone:** Hey, Troy and Lucas, I'd love to put some time on the calendar—15 to 30 minutes—just to introduce myself and learn more about Dimmo and your goals. I have some documentation, but I'd rather do a quick client interview to understand what makes you tick and what you're excited about. This way we can start thinking through strategy together and help you get the growth you're looking for. I'll send a calendar link through Slack to find a time that works.

**Lucas Swartsenburg:** Thanks, everybody.

**Troy Munson:** Thank you.
