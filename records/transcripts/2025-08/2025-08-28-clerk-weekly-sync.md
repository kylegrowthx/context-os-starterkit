# Clerk Weekly Sync

<metadata>
date: 2025-08-28
time: 16:00 UTC
duration: 30 minutes
organizer: team@growthxlabs.com
participants: Aida Knezevic, Jo Kaminska, Alex Rapp
fathom_recording_id: 83602058
fathom_url: https://fathom.video/calls/392419673
share_url: https://fathom.video/share/TMzi4F_Jmh6E7ccigaQGAECE4ytyARo8
source: fathom
enriched_on: 2026-03-03 02:15 UTC
</metadata>

---

## Summary

GrowthX and Clerk aligned on the SSO Best Practices blog post launching by end of day tomorrow, targeting indie hackers and solo developers with 2-3 depth-focused Clerk mentions and no Enterprise SSO coverage. Alex will review and approve remaining blog ideas in Airtable while GrowthX checks for content overlap; redundant topics will be refreshed rather than duplicated. An SEO audit identified minor fixes needed (footer nofollow causing 404s, thin changelog content, duplicate title tags), and a Looker dashboard was set up to track performance by non-branded traffic, GrowthX vs. Clerk content, and LLM referral sources, with initial posts rolling out unlisted but indexable to ensure quality meets Clerk's high standards.

---

## Context

This is a weekly sync between GrowthX's content delivery team and Clerk, a developer authentication platform. GrowthX is executing a content marketing engagement for Clerk, creating blog posts targeting mid-funnel developer audiences. Clerk is a B2B SaaS company with high content standards — they previously rejected a ghostwriter program as insufficiently polished. The meeting focused on publication workflow, content strategy alignment, and establishing performance tracking for GrowthX-authored content.

---

## Relevance

**To GrowthX Delivery:**
- Established publication workflow: Google Docs drafts → team channel review → unlisted/indexable posts → eventual public release pending quality validation
- Client enforces strict content review involving broader team initially, then streamlining — requires flexible revision cycles
- AEO best practices integrated into GrowthX writing (H2s formatted as questions, focusing on LLM discoverability)
- Looker dashboard setup demonstrates analytics maturity expected for SaaS engagements

**To CheckThat:**
- LLM referral tracking integrated into performance dashboard — identifies which LLMs send traffic and which pages get referenced
- AEO strategy explicit in content approach (depth over keyword frequency, unlisted-but-crawlable strategy for LLM training data)
- Kevin Indig AEO scorecard referenced as optimization framework by Clerk

**To GrowthX Business Development:**
- Clerk account shows strong collaboration patterns and process maturity (Airtable content OS, automated review workflows, structured analytics)
- Client balancing speed vs. quality, opting for unlisted strategy rather than forced timeline
- Opportunity for future work: changelog enrichment, content refresh cycles, technical SEO optimizations (internal linking strategy)

---

## Overview

- SSO Best Practices blog post nearly complete; delivery expected by end of day tomorrow
- SEO audit revealed minor issues (404 errors, thin content, duplicate titles) to be addressed
- Content review process to involve broader Clerk team initially, then streamline over time
- Looker dashboard set up to track content performance, including GrowthX vs. Clerk-authored content

---

## Key Topics

### Content Creation Progress

  - SSO Best Practices blog post chosen as first piece, focusing on indie hackers/solo coders
  - Blog post delivery expected by end of day tomorrow
  - Alex to review Airtable for additional blog ideas, approving or rejecting as needed
  - GrowthX to double-check for content overlap before proceeding with approved topics

### Content Strategy and SEO

  - Mid-funnel content approach for SSO Best Practices blog
  - 2-3 mentions of Clerk planned, focusing on depth rather than frequency
  - Enterprise SSO to be omitted from this piece
  - SEO best practices (e.g., H2s as questions) to be implemented in content

### SEO Audit Results

  - Main issue: Adding nofollow to footer link causing 404 errors
  - Thin content on changelog pages receiving backlinks
  - Some duplicate title tags identified
  - Broken links found on a few pages
  - Overall, fewer issues than typically seen on other websites

### Content Review and Publishing Process

  - Initial drafts to be stored in Google Docs
  - Alex to set up shared folder with global access for Clerk team
  - Content to be posted in team channel for broader review initially
  - Plan to streamline review process over time as team becomes comfortable with quality

### Performance Tracking

  - Looker dashboard set up, integrating Google Search Console and GA4 data
  - Dashboard includes non-branded traffic, GrowthX content performance, and LLM referral traffic
  - Airtable integration used to differentiate GrowthX vs. Clerk-authored content

### Content Publication Strategy

  - Initial blog posts to be unlisted but indexable/crawlable
  - Approach aims to ensure quality meets Clerk's high standards before full public release
  - Internal linking to be implemented for crawler discoverability

---

## Action Items

**Aida Knezevic (GrowthX)**
- Deliver SSO Best Practices blog draft to shared folder by EOD tomorrow
- Review Clerk's website for content overlap with approved blog ideas; flag redundancies as refresh vs. new content
- Handle featured image selection (working with Katya, GrowthX designer) — provide 2-3 hero image options to Clerk

**Jo Kaminska (GrowthX)**
- Continue support on content delivery and process coordination

**Alex Rapp (Clerk)**
- Review & approve remaining blog ideas in Airtable content OS (complete by tomorrow due to Monday off)
- Send Next.js comparison article draft (Markdown) to GrowthX team for finishing
- Create shared Google Drive folder for content drafts; grant editing access to GrowthX team
- Pass SEO audit findings to Isaac (Clerk teammate) for technical remediation (404s, duplicate tags, broken links)
- Provide list of additional content reviewers beyond Brian for broader team involvement

---

## Transcript

**Jo Kaminska:** Hi, how are you?

**Aida Knezevic:** I'm good, pretty good.

**Jo Kaminska:** Feeling better?

**Aida Knezevic:** Yeah, I ate some really spicy chili peppers that are growing on my balcony, so that helped reset me.

**Jo Kaminska:** Yeah, I'm good. Just busy with editing — it's an editing day.

**Aida Knezevic:** Yeah, especially towards the end of the week it gets really crazy.

**Aida Knezevic:** Hi, Alex.

**Alex Rapp:** Hello, hello.

**Aida Knezevic:** How are you?

**Alex Rapp:** Oh, not too bad. Yeah, can't complain.

**Aida Knezevic:** I love the dog.

**Alex Rapp:** Yeah, he's on the mend. He just got fixed yesterday, so he's a little groggy, but he's doing better today.

**Aida Knezevic:** Oh, poor baby. My older brother has a golden retriever, and he wasn't fixed for most of his life.

**Aida Knezevic:** And then he had some health issues recently, and he's like 11 or 12 years old. The hospital in Germany took him there, and they said he needs to be fixed first. So he is now so food motivated — he's obsessed with food. It's gone to extremes as a result of that.

**Alex Rapp:** Yeah, he's a firecracker. He has so much energy. He just turned two recently, so we'll see if he calms down a little bit after all this. But yeah, he's fun.

**Aida Knezevic:** Okay, good to hear. So to give you an update on the progress: on Tuesday you approved a couple of blog ideas, and we've started. The blog is very close to being done. We couldn't get it ready in time for this meeting, but it'll be delivered by the end of the day. And then by end of day tomorrow, our goal is to get it to you for review.

**Alex Rapp:** Okay, sounds good. Yeah, just a heads up — we're off on Monday, so I may not get to it until Tuesday if you send it later in the day.

**Aida Knezevic:** Sounds good. Most of our team is also going to be out of office, but Jo and I are Europe-based, so we'll keep going.

**Jo Kaminska:** I was going to ask — I'm assuming you're in Germany, right?

**Aida Knezevic:** No, I'm in Bosnia, but I have a lot of family in Germany.

**Jo Kaminska:** I'm in Lisbon, Portugal — the capital.

**Alex Rapp:** Oh, cool. Fun fact, we did a full company offsite in Portugal last year. We stayed in Porto for a bit and then Lisbon for a day or two. Definitely want to go back.

**Jo Kaminska:** Lisbon is like a big version of Porto, right?

**Alex Rapp:** Yeah, walking around uphill everywhere was fun. It was a nice challenge.

**Jo Kaminska:** My watch tells me 10 floors done on a short walk, so usually daily is about 20 floors by default.

**Alex Rapp:** That's good. Nothing wrong with that.

**Alex Rapp:** So, do you know which blog you're going to run with first?

**Aida Knezevic:** We picked the SSO Best Practices one — that's what we want to calibrate on.

**Alex Rapp:** We have a big gap on SSO. I keep seeing that pop up anytime I dig into our SEO tooling.

**Jo Kaminska:** Quick alignment question: this blog will be angled as Best Practices, right? Besides the "what is" and "why is it important" sections, we're planning to include eight practices. Do you have a ballpark number for how many Clerk mentions you want? I thought two to three times to educate the developer audience rather than focus on the product.

**Alex Rapp:** From what I hear, this is mid-funnel content. I care less about the number of occurrences and more about the depth of those mentions. I think whatever feels natural based on the flow of the content is good.

**Jo Kaminska:** Right — points where you could zoom into your solution and explain benefits, like around user management. Other best practices should be more general education.

**Alex Rapp:** That's perfect. Are you planning to mention Enterprise SSO at all?

**Jo Kaminska:** We wanted to focus on indie hackers and solo developers.

**Alex Rapp:** That's perfect. Yeah, let's omit any reference to Enterprise SSO.

**Aida Knezevic:** All right, nice.

**Aida Knezevic:** I wanted to talk about the blog ideas you reviewed in the content OS. You approved three — what did you think about the others?

**Alex Rapp:** The three I picked were the most compelling and fill known content gaps. The multi-tenancy articles, especially around architecture and multi-tenant versus single-tenant — we just did a bunch of those. I wanted to understand your position on redundancy: should we avoid duplicative content even if not a mirror image, or dance around existing content to fill gaps and strengthen our position?

**Aida Knezevic:** If something would rank for the same keyword with the same intent, we don't want to redo it. We might update it with sections to make it more SEO and LLM friendly. Looking at multi-tenancy — there's a top-of-funnel piece, and one on multi-tenant authentication that might overlap. But there are best practices angles.

**Alex Rapp:** There's opportunity to fill mid-funnel gaps. Anything that feels redundant to what you already have, I'm happy to refresh. We've got a 30, 60, 90 day review cycle built into our content process anyway. If you have suggestions based on your research, we're open to it.

**Aida Knezevic:** Here's the easiest workflow: you approve anything that sounds okay in Airtable, even if you think you might have content on that topic. Then I'll check your website for overlaps and flag each record as refresh or skip. I used SEMRush to identify keywords you're not ranking for — that's why I made these suggestions.

**Alex Rapp:** Got it. I can definitely go through this today. For anything without a status, I can archive or mark irrelevant. I know for a fact we don't have competitive content on our site, so that's fine.

**Jo Kaminska:** Before we start working on an assignment, we check what type of content ranks and what you already have. So based on that, we either refresh or produce new — mutually exclusive.

**Alex Rapp:** I'm trying to get my Next.js competitive comparison article over the finish line. I keep running it through Kevin Indig's AEO scorecard and it keeps getting worse even when I adjust for the recommendations. I'm stuck in a vicious cycle. The draft could be a nice candidate for you to take over from here instead of me chasing straws.

**Aida Knezevic:** Yeah, totally. Writing best practices are good for LLMs and AEO. I do small tweaks to make content more AEO friendly — like formatting H2s as questions, then answering immediately. But beyond that, you can lose a lot of time overthinking it.

**Alex Rapp:** Yeah, that's for sure. If I send it to you, can I just send it in Markdown?

**Aida Knezevic:** Yeah, that's fine.

**Alex Rapp:** All right, I'll get through that today for sure.

**Aida Knezevic:** Okay, perfect. We wanted to share an SEO audit of your website. I shared the spreadsheet link in the agenda and can send it in Slack. The biggest issue is adding nofollow to the footer link — it's causing 404 errors that impact crawl budget. We can share the spreadsheet with your web team. There are also recommendations for thin pages — changelog pages have low word counts but lots of backlinks. We could enrich them at some point, maybe as an internal project, and link to them in new content for internal linking.

**Alex Rapp:** Yeah, changelog entries are thin intentionally — that's standard practice. But if there's opportunity to beef them up slightly, that'd be interesting. I'd need to look at traffic post-release to see if there's value. My teammate Isaac is going through our Ahrefs audit right now, so this is timely and helpful.

**Aida Knezevic:** We also found a couple of pages with broken links and some duplicate title tags.

**Alex Rapp:** I don't know how duplicate titles got past our review. We can set up redirects for the broken links.

**Aida Knezevic:** Not that many issues overall. We've seen websites with hundreds of 404s, so this is actually pretty tame.

**Alex Rapp:** At least we're not the worst, but we definitely have room for improvement. I already passed this on to Isaac, so we're moving along.

**Aida Knezevic:** Thanks.

**Aida Knezevic:** Quick update on featured images: we looped in Katya, our designer, to come up with suggestions — two or three different versions for hero images. You can give feedback.

**Alex Rapp:** Sounds good.

**Aida Knezevic:** One last thing: the review and publishing process. I assume you and possibly Brian will review. We can automate reviews in Airtable and send you an email when articles are ready. Who else should be involved?

**Alex Rapp:** Let me think about that and get a list back to you. Where will drafts be stored?

**Aida Knezevic:** Google Docs initially.

**Alex Rapp:** I think it would be best to leave it open. I can grant access and share it in our company team channel. That's our standard practice — whoever has time reviews it. I'd like to do that at least for the first couple so everyone gets comfortable. Then I can pass suggestions back to you.

**Jo Kaminska:** We'll have a shared folder where we grant access to all your team members.

**Alex Rapp:** Sounds good. Alternatively, I'm happy to set one up on our side with global access for Clerk and then add permissions for your team.

**Aida Knezevic:** We'll set you up with editing access. For the first couple pieces, that's definitely a good approach. As we dial things in, it can be fewer people.

**Aida Knezevic:** Next week, we wanted to share, well, this also depends on, like, how quickly we can publish content.

**Aida Knezevic:** But we have set up a Looker dashboard for you, which integrates data from your Google Search Console and GA4.

**Aida Knezevic:** And it has, like, multiple pages.

**Aida Knezevic:** So it breaks down non-branded traffic to your site.

**Aida Knezevic:** One page focuses on GrowthX content so you can compare performance against what you're producing. And there's a page for LLM referral traffic.

**Aida Knezevic:** It pulls data from GA4 and breaks down which LLMs send the most visitors and which pages get referenced most in different LLMs. That should be helpful.

**Alex Rapp:** How do you split tracking for GrowthX versus Clerk authored?

**Aida Knezevic:** We integrate Airtable with Looker. Published URLs are fed into a Looker sheet from the published content view.

**Jo Kaminska:** We take it from the published content sheet view.

**Alex Rapp:** Got it. I assumed it had something to do with the URL slugs. Who generates the slug?

**Aida Knezevic:** We do. The slug is typically the primary keyword.

**Alex Rapp:** That makes sense. I just wanted to make sure we weren't on the hook for it. Nick mentioned you have a blog post template — is that helpful, or should I just reference existing posts for heading structure? I'm pretty sure we follow H1, H2, H3 best practices, but let me know if not.

**Alex Rapp:** One other thing: until we're confident in polish and tone, we're publishing posts unlisted but indexed/crawlable. We'll ensure Google and Bing index them. Will that obstruct your data collection and analysis?

**Alex Rapp:** At least for the, you know, until we get into a really confident place with, you know, polish and tone and, you know, all those things, we are going to have these posts be unlisted, but indexed or crawlable.

**Alex Rapp:** You know, we'll make sure that they're indexed with, you know, Google and Bing.

**Alex Rapp:** Any issue with that?

**Alex Rapp:** So they'll be, they'll be crawlable, but they just won't be, you wouldn't be able to, you know, navigate to the posts, you know, on your own if you were on the blog.

**Alex Rapp:** You know, the way, the way that I see it is that should be fine just because, you know, the goal here is to increase LLM traffic, right?

**Alex Rapp:** And that wouldn't, as far as I know.

**Alex Rapp:** So that's not a blocker for an agent crawler.

**Jo Kaminska:** How many pages?

**Jo Kaminska:** Yeah, like, could you give more context around it?

**Alex Rapp:** Yeah, so here, I'm going to show you an example.

**Alex Rapp:** So, you know, this is what, you know, obviously I was showing before, it's all the public posts.

**Alex Rapp:** An example of an unlisted one would be, this blog post is not up here in the index here visually, but it's still publicly accessible and, you know, we see traffic to it.

**Aida Knezevic:** If they're still crawlable, that's fine. We'll just need to add internal links so crawlers can find them. Hopefully we don't need that for all posts.

**Alex Rapp:** Right. Once everyone's comfortable with quality and technical depth, we'll post directly to the blog publicly. We tried ghostwriters before and our CEO shut it down — not meeting Clerk's quality bar. Content is heavily scrutinized across the board. If the unlisted posts gain momentum and volume, that's a much easier conversation for me to have.

**Aida Knezevic:** Yeah, I totally get it. It shouldn't hurt SEO short-term.

**Jo Kaminska:** We can also check what keywords each page should rank for, so if you want to expand and list them later, we have that mapped.

**Alex Rapp:** Cool.

**Aida Knezevic:** Sounds good. We'll be in touch on the blog. We're experimenting with content length internally — depending on your feedback, we might try different approaches. What's the ideal length and detail level?

**Alex Rapp:** We're also experimenting internally to see what length gets the best output. We'll get you the blog and adjust based on feedback.

**Aida Knezevic:** All right. Thanks. Have a great rest of your day. Hope your dog gets better soon.

**Alex Rapp:** Thank you. I'll go through the Airtable and the rest of the blog ideas.

**Aida Knezevic:** See you.

**Jo Kaminska:** See you next week.
