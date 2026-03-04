# Website SEO Sync

<metadata>
date: 2025-06-30
time: 16:01 UTC
duration: 30 minutes
organizer: Megan Dickey (GrowthX)
participants: Jenn Peters (GrowthX), Megan Dickey (GrowthX), Cameron Brown (Firework), Ritesh Kewlani (Firework), Samrawit Stifanos Berhe (Firework), Abhishek Anjanappa (Firework)
fathom_recording_id: 71292122
fathom_url: https://fathom.video/calls/338688061
share_url: https://fathom.video/share/67qarEFA9ucio5wJJ7QFQmrHQ4H4JxXn
source: fathom
enriched_on: 2026-03-03 15:30 UTC
</metadata>

---

## Summary

GrowthX and Firework identified critical WordPress-to-Webflow migration issues blocking blog performance: since the October 2024 cutover, newly published content isn't getting indexed and no blogs from 2025 are generating leads, while pre-migration blogs continue to perform well. Cameron proposed reversing the site architecture to make Webflow the default with specific WordPress rules, and the team committed to accelerating the full migration and implementing granular blog performance reporting that breaks out individual blog metrics and monthly cohorts to guide optimization strategy.

---

## Context

Firework is a GrowthX client working through a major site migration. They moved from WordPress to Webflow starting in October 2024, and the team (Ritesh, Cameron, and infrastructure) is now realizing that this transition has created a cascading technical problem: new content isn't being indexed properly, which directly impacts lead generation from blog posts. Ritesh Kewlani from Firework flagged that they're seeing no leads from any blogs published in 2025, while older pre-migration content still attracts leads. On the GrowthX side, Megan Dickey (leading the reporting and article generation), Jenn Peters (SEO expert tracking indexing and Google Search Console data), and Cameron Brown from Firework's team are trying to solve the indexing problem while maintaining the blog strategy and translation roadmap. This call is a working session to diagnose the root cause and determine whether to accelerate the migration or patch the existing architecture.

---

## Relevance

**To GrowthX Delivery:**
- Technical site migrations require deeper SEO planning than typical content projects — indexing and canonicalization issues can tank performance for months even when content is solid
- Client blog reporting must become granular (individual blog metrics, monthly cohorts) not just aggregate numbers — Megan is implementing this for Thursday calls
- Need to flag migration timelines early with clients; Firework's blog strategy (translation project, content generation) is being undermined by infrastructure decisions made before SEO impact was understood
- Jenn developed a Google Search Console tracking methodology for indexing issues that should be documented and reused in future migrations

**To GrowthX Business Development:**
- Firework relationship is healthy and collaborative — Ritesh is directly engaged in strategic decision-making, infrastructure team (Abhishek) is looping in GrowthX on architecture choices
- Blog translation project is a growth signal (5 blogs to French by Thursday, potential for scaling to next 20) — indicates client expansion and confidence in content strategy
- Potential account expansion: Firework may need ongoing site optimization consultation beyond delivery scope, especially if CTA testing and architecture decisions require strategic advisory

**To CheckThat:**
- Firework's indexing challenge is a direct use case for AI visibility tools — flagging which content should be indexed and why, understanding crawl budget impact of duplicate canonicals and redirects
- Cameron is manually managing sitemaps and architecture decisions; CheckThat's visibility layer could help surface these issues faster in future migrations

---

## Overview

- Critical indexing issues from WordPress-to-Webflow migration (Oct 2024) are blocking lead generation — no blogs from 2025 are attracting leads, while pre-migration content continues to perform
- Team to accelerate full site migration: make Webflow the default with reverse-proxy rules for remaining WordPress pages, rather than maintaining dual architecture
- Implementing granular blog performance reporting to replace aggregate-only view — will track individual blog metrics, monthly cohorts (especially June blogs), and top 100 performers with publication dates
- Cameron has implemented CTA strategy: inline CTAs now default to "Free Trial" (higher value), with sidebar toggle between "Free Trial" (small business) and "Book a Demo" (enterprise messaging)

---

## Key Topics

### Site Migration and Indexing Issues

  - WordPress-to-Webflow migration (Oct 2024) causing significant indexing problems
  - Majority of high-performing blogs likely published pre-migration
  - No blogs from 2025 attracting leads, flagging potential issues
  - Cameron to initiate conversations with infrastructure team about reversing site architecture
  - Proposal: Make Webflow the default site, with specific rules for remaining WordPress pages
  - Team to review all non-migrated blogs and develop a strategy for quick migration

### Blog Performance Reporting

  - Current aggregate reporting doesn't reveal which individual blogs are performing or why
  - Ritesh identified a critical signal: no blogs from 2025 are generating leads, but pre-migration blogs perform well — suggesting indexing is the blocker
  - Megan to provide more granular data for Thursday calls:
      - Top 100 performing blogs with publication dates (currently only top 20)
      - Monthly cohort breakdown (e.g., how are June blogs performing vs. May/April)
      - Individual blog metrics (not just aggregate impressions/clicks/leads)
  - Jenn flagged that recent content needs time to mature, and manual indexing requests are rate-limited by Google; team to review April/May/June trends together

### Content Optimization Strategies

  - Cameron implemented changes to inline CTAs, now promoting free trials (more valuable than playbooks)
  - New feature: Ability to change sidebar CTA button between "Free Trial" and "Book a Demo"
  - Strategy: Use "Free Trial" CTA for small business-focused content, "Book a Demo" for enterprise-targeted blogs
  - Team to provide more recommendations on blog optimization (e.g., images, CTAs)

### Translation Project Update

  - Cameron plans to translate \~5 blogs by Thursday
  - Will unpublish English blogs on French site for better user experience
  - Translated blogs will have new URLs (e.g., /fr/blog/translated-slug)
  - Cameron to update shared spreadsheet with new translated blog URLs

---

## Action Items

**Megan Dickey (GrowthX)**
- Prepare detailed blog performance report including publish dates; focus on recently published content (especially June); provide top 100 performers and monthly breakdown for individual blogs (not just aggregates)
- Collaborate with Jenn (GrowthX) to develop specific recommendations for blog page optimization (CTAs, images, layout) that Cameron can implement; Jenn to share process for exporting data and identifying indexing issues

**Cameron Brown (Firework)**
- Initiate conversations with Abhishek (Firework) and infrastructure team to review timeline for accelerating WordPress-to-Webflow migration; propose reversing site architecture to make Webflow default with reverse-proxy rules for remaining WordPress pages
- Provide regular updates on migration progress and work with Jenn to verify that blog pages are getting indexed post-migration

---

## Transcript
[Small talk: Cameron and Jenn discuss weekend activities, Samrawit shares about weather in Edmonton, Alberta.]

**Megan Dickey:** Yeah, I mean, I don't have much for you, but yeah, just so, yeah, we're moving ahead on those articles that we spoke about in Slack, and I've also just started doing some article generation.

**Megan Dickey:** Yeah, so actually, just to clarify what that even means, they're, like, basically, like, my process is, like, I'll go through SEMrush, I'll run, I'll do some keyword research, and then our new platform, Atlas, like, has this assignment tool generator, so.

**Megan Dickey:** Based on those new topics, Ritesh, that you put into Slack, I did some research on that, and so now there's like, we have like 100 new potential ideas, but we'll kind of still, I won't throw them all at you at once, we'll kind of do this like week by week until like, okay, like this is what we're looking at this week.

**Megan Dickey:** But yeah, I think we have a good plan moving forward.

**Megan Dickey:** Yeah, I got the HubSpot data this morning. If you send it Monday morning, that gives me time to dive through it by Thursday.

**Megan Dickey:** Does anyone else have feedback? Cameron, I sent you the top 20 blog posts — was that helpful, or do you need them cut in any other way?

**Cameron Brown:** No, I think you've done a great job, thank you, that's basically exactly what I was looking for.

**Cameron Brown:** Okay, perfect.

**Cameron Brown:** The translation hasn't really started yet, so I will...

**Cameron Brown:** Do my best because I'm, you know, considering it like medium to low priority, but yeah, I'll try and make a little bit of progress on it every week.

**Cameron Brown:** But the main thing I want to keep tabs on is the performance of those blogs as I translate them and how they compare. By Thursday I'll hopefully translate about five of them. It'll probably be too early to draw conclusions, but we'll monitor it.

**Cameron Brown:** The other thing I think that I'll do, unless you guys have any strong opinions, is when I start the translation of the blogs, I will unpublish all of the blogs that are in English on the French site, for example.

**Cameron Brown:** So when blogs are visible on the French site, it means they're translated. From a user experience perspective, if you're reading a blog in French, all related blogs should also be in French — you don't want to click to another page that's only in English. That's the strategy I'm planning on. I won't have major updates or real numbers for a couple of weeks, but if it goes well, I can see us rolling out the next batch of translations.

**Megan Dickey:** Yeah, that sounds good.

**Megan Dickey:** Once it's live in French, can you send me the link so we can track it on our end?

**Cameron Brown:** Sure. The URLs will change — the equivalent slug will be translated into the local language. It will be /fr/blog/translated-slug, not just /fr with the same URL. I'll update the shared spreadsheet with the new URLs as I translate them.

**Megan Dickey:** Awesome.

**Megan Dickey:** Cool.

**Ritesh Kewlani:** I had a couple things I wanted to chat about. I was talking to Abhishek and we had an interesting idea. Right now we're reporting numbers at an aggregate level — for June, we look at total impressions, clicks, and leads. But we need to go deeper and understand how much traffic the blogs we've published recently are generating. When I look at our top-performing blogs, a lot of those were published way back in August or September. The trend is that recent blogs haven't performed as well as the earlier ones.

**Ritesh Kewlani:** I liked that your report had the top 20 most performing blogs with publication dates. Can we expand that to top 100 so we can see which ones are performing well and when they were published? And on Thursday's call, can we look at individual blogs and monthly cohorts? For example, how are June-published blogs doing? A few are doing well, but most either yielded no leads or just one or two. We need to understand: what's working, what's not, and what will actually move the needle — aggregate numbers don't tell the complete story.

**Megan Dickey:** That makes perfect sense. We can break that out by cohort — looking at June-published blogs, how they're doing, while keeping the overall data as well.

**Ritesh Kewlani:** Yes, let's keep what you were doing but add individual blog and monthly data. I'm wishing I could join Thursday's call — there's been a lot going on the last few weeks. It would be great if we could all review the data together and figure out what's working, what's not, and what we should publish.

**Megan Dickey:** Sounds good, we'll have it ready for Thursday.

**Jenn Peters:** One thing to note — sometimes results take longer than the same month to roll in. Looking at June data in June might not be the most accurate picture of longer-term performance. But here's my question: Is anyone on your team tracking indexing to make sure everything's indexing quickly? I sent you a report of pages that are crawled but not indexed. There could be several reasons — lots of redirects from the migration, sitemapping issues. We want to make sure that if we're tracking leads on a page, it's actually indexed.

**Jenn Peters:** Is there anything we should know about that?

**Cameron Brown:** No one's tracking it actively. I'm looking at the spreadsheet you sent me — that's a long list. The core problem is that the sitemap exists on the WordPress site. I've worked with sitemaps before, and I asked Webflow's solutions architect if I could manually add Webflow-only pages to the sitemap. Technically yes, but the work involved might not yield results. I floated this around, but we concluded that manually patching the sitemap won't work. The better strategy — which is what we're already doing — is to complete the full migration to Webflow. Once everything's on Webflow, we can quickly build a robust sitemap using Webflow's tools and my expertise on what should and shouldn't be indexed. But we can't do this with our current split architecture.

**Cameron Brown:** Quick question — in the spreadsheet you sent, is the second column the publishing date?

**Jenn Peters:** Yes, it's a straight export from Google Search Console. The newest stuff probably isn't the issue anyway.

**Cameron Brown:** Right. I think these problems are infrastructure-related, which is my concern. Firework has good instincts to push on this — your recent efforts should be yielding results. But this is the perfect storm.

**Jenn Peters:** It's a blocker. While we're tracking leads and trying to nail down which pieces are performing, we also have translations on that non-indexed list. We'll never see accurate reporting if we can't fix the indexing issues tied to the sitemap. It's all interconnected right now. I don't think we've had accurate reporting since the migration.

**Cameron Brown:** I can help answer that. The official cutover to Webflow happened in October 2024, just before I joined.

**Cameron Brown:** Blogs written before October 2024 would have existed on WordPress and been indexed in the WordPress sitemap. My theory — and this conversation supports it — is that all our top-performing blogs were written before October because they were already indexed.

**Jenn Peters:** When I started, Prateek flagged the big problem: no blogs from 2025 are generating leads. That was the first red flag. We can manually submit URLs for indexing on our end, but there are complications. If you look at the data, there are duplicate and canonical issues — Google might be pointing to the old WordPress version and getting confused. Plus Google Search Console only allows about 10 manual submission requests per day, and if you keep requesting too often, it restricts you further — I think it's flagging that as a bigger issue. It's a lot of work to unravel, and we need to think about it strategically. Obviously, we want content to perform well with accurate reporting, but this is a longer-term problem to solve.

**Cameron Brown:** Obviously, I don't want to say this is the only issue, and you should definitely continue writing great content. But this is the critical blocker on blog performance right now. I want to open a conversation about accelerating the migration timeline. We're at the end game anyway. Once we finish the Ava page, we should move the switch. Even if some industry pages aren't done, they get less than 50 views a week. Sacrificing a couple weeks on those low-traffic pages is worth it to fix the blog indexing problem. I'm advocating for retiring WordPress at our earliest possible convenience.

**Ritesh Kewlani:** Let's have a conversation with Abhishek to review all the blogs that haven't been migrated. We know they're barely getting traffic anyway. Even if we need to move them, we can figure out a way to do it without heavy design and content work, then update them later.

**Cameron Brown:** I'll also talk to the infrastructure team. Here's my idea for a best-of-both-worlds scenario: reverse the architecture so Webflow becomes the default site. For the few remaining WordPress URLs, we write specific rules — if someone requests /industry/automotive, point to WordPress. Right now 95% of pages are on Webflow anyway, so it doesn't make sense for WordPress to be the default when we're constantly diverting traffic to Webflow. I need to loop in Abhishek and infrastructure. This is critical, not just for dev reasons.

**Cameron Brown:** So, okay.

**Cameron Brown:** Yeah.

**Cameron Brown:** Sorry to add to that.

**Jenn Peters:** Sorry to keep bringing this into this big, massive thing.

**Jenn Peters:** But, but like, yeah, like the pages that I pulled for you were very limited in the scope of like the number of non-index pages.

**Jenn Peters:** you look at GSC as a whole, like that was literally just a list of just the blogs, just discovered, not indexed, or either just crawled, not indexed.

**Jenn Peters:** I can't remember.

**Jenn Peters:** I don't have it open just now.

**Jenn Peters:** It's crawled, but not indexed.

**Jenn Peters:** It's crawled.

**Jenn Peters:** Okay.

**Cameron Brown:** So that's just the blogs.

**Jenn Peters:** I've included all the other pages from different parts of the sitemap. In Google Search Console, you'll see some non-indexed pages are due to redirects, which are unavoidable. But redirects aren't ideal in Google's eyes either. For context, when you bring this to the larger team, flag that it's not just blogs — our landing pages have indexing issues too.

**Cameron Brown:** So it's a site-wide problem.

**Cameron Brown:** When you say GSC, you mean Google Search Console?

**Jenn Peters:** Yes, Google Search Console.

**Cameron Brown:** I'm not an expert in GSC, so after we flip the switch and do this migration, I'd like to piggyback on your expertise. After the migration, are the blog pages now indexed? And beyond your deliverables, can you verify that our landing pages are getting indexed too?

**Cameron Brown:** No problem.

**Jenn Peters:** It all comes out in the export — I just filter to get the blogs. I'm not an expert either, especially on sitemapping, but I'm happy to show you what I know and Megan can help too. If you confirm that what we want indexed is actually indexed, that would be great. I can show you how to export the reports and run the checks in two seconds.

**Cameron Brown:** Thank you for that. I'll have an update as soon as I can. This is going to be work, but it's clearly in everyone's best interest. We want to help your team so we can all succeed together. This should be top priority — we can't do our best unless it's resolved.

**Jenn Peters:** I didn't realize how big this was until I looked at the indexing reports. Obviously, it's the WordPress issue. We want to put our best foot forward.

**Cameron Brown:** It's not a small task, but it's the lowest-hanging fruit for improving performance. We're aligned, and I'll provide regular updates.

**Jenn Peters:** It's a work-in-progress, and it'll take time.

**Cameron Brown:** If I could do it independently, I would. The biggest challenge is we're not ready to move over without a redirecting strategy or at least finishing the Ava product page.

**Cameron Brown:** Ava is one of our four core products, but it's new and the marketing team isn't sure how to message it. The product team has lots of opinions, so it's been a back-and-forth conversation. I don't have complete control, but I'll provide updates as things move forward.

**Ritesh Kewlani:** Let's take this offline and discuss with Abhishek. We'll make whatever decisions need to be made.

**Cameron Brown:** Sounds great. Thank you, Ritesh.

**Ritesh Kewlani:** Jenn made a really valid point — when we look at monthly data, it takes time for blogs to get indexed. We might not see June results in June, but May and April blogs should show results by now. Let's start reviewing that data from Thursday onwards, watching May and April trends to see how things are maturing over time.

**Ritesh Kewlani:** One more thing — we talked last Thursday about optimizing blog pages for conversions. We've discussed where to use free trial vs. book a demo, but we need more support from you, Megan and Jenn, on next steps. Cameron can implement things quickly, so we're not lacking on execution. We need strategic leadership: should we add more images? More CTAs? Update existing CTAs? If you and Cameron can work together and come up with recommendations, that would be really helpful. Let's make it an action item to track this week.

**Megan Dickey:** Sounds good, we can do that.

**Cameron Brown:** I have some quick updates on CTAs. Late last week, I changed the inline CTA fallback from promoting a playbook to promoting a free trial — free trials are more valuable. I also implemented a feature to toggle the sidebar CTA between "Free Trial" and "Book a Demo." I need to evaluate the performance, but the strategic idea is: use "Free Trial" for small business content, "Book a Demo" for enterprise messaging. For example, our top performing blog on short-form video statistics performs well with enterprise customers like Lowe's and Nike. As you get to know the market better, you'll understand which messaging for different audiences. Use "Free Trial" for small business, "Book a Demo" for enterprise.

**Jenn Peters:** Is that a CMS toggle?

**Cameron Brown:** In the blog CMS, there's a dropdown called "Sidebar CTA" — you can pick "Book a Demo" or "Free Trial."

**Cameron Brown:** That should be simple.

**Jenn Peters:** I'll post screenshots in the GrowthX channel.

**Megan Dickey:** Thanks, everyone. We'll chat on Thursday. Quick flag: I'll be out next week, but Jenn will be around and I'll still be on Thursday's call. I'll keep everyone looped in.

**Ritesh Kewlani:** Sounds good.

**Jenn Peters:** Thanks, everyone.

**Megan Dickey:** Bye.

**Cameron Brown:** Bye.
