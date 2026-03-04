# Otto <> Growth X - Weekly Sync

<metadata>
date: 2025-10-02
time: 16:30 UTC
duration: 34 minutes
organizer: team@growthxlabs.com
participants: Jason Flateboe, Aida Knezevic, Bailey Seybolt, Erik O'Brien, Michael Gulmann
fathom_recording_id: 91464062
fathom_url: https://fathom.video/calls/427808780
share_url: https://fathom.video/share/VE7ATRJnHzzY5deTCtptA8sZ8KM57Lt5
source: fathom
enriched_on: 2026-03-02 14:30 UTC
</metadata>

---

## Summary

GrowthX and Otto aligned on content production roadmap and website optimization. GrowthX will deliver 3 blog posts the following week, scaling to 5 per week, with the calibration post ready for Jason's feedback. The team agreed that adding a table of contents improves both user experience and SEO engagement, and discussed strategy for building domain authority through high-quality content compilations and travel blogger outreach. A Looker dashboard was set up to track website performance, content engagement, and organic search metrics.

---

## Context

Otto is an AI travel planning tool led by CEO Jason Flateboe. GrowthX is executing a content marketing and website strategy for Otto as part of a larger engagement. Bailey Seybolt recently joined the GrowthX team working on this account (as of early October 2025), bringing 10 years of SaaS and content marketing experience. The relationship is collaborative—Jason is hands-on strategically but delegating day-to-day execution to his operations lead. This was a working session to review the first draft content, align on production timelines, and set up reporting infrastructure for measuring content performance.

---

## Relevance

- **To GrowthX Delivery:** Bailey's joining the team brings fresh perspective on SaaS content approaches that complement GrowthX's existing content strategy. The team is testing shorter artifact outputs to improve LLM consistency—a finding that may inform future client recommendations. The Looker dashboard setup demonstrates GrowthX's ability to architect integrated reporting across GA4, GSC, and custom data sources.

- **To GrowthX Business Development:** Otto is planning a press launch within 4 weeks with tech and travel publications (TechCrunch, GeekWire, travel blogs). Strong potential for reference case study and organic authority building through high-domain-authority travel blogger partnerships. Initial traffic shows some LLM referral signals (ChatGPT, Perplexity) indicating emerging discovery channel.

- **To CheckThat:** The team identified AI search as an emerging discovery mechanism and discussed how content chunking and section-level clarity matters for AI search readability. This signals opportunity to demonstrate CheckThat's AI visibility capabilities for Otto as they scale organic traffic.

---

## Overview

- GrowthX to deliver 3 blog posts next week, ramping up to 5 per week thereafter
- Otto to implement table of contents on blog posts for improved user experience and SEO
- Looker Dashboard set up for Otto to track website performance and content effectiveness
- GrowthX to compile list of high-authority travel bloggers for Otto's outreach efforts

---

## Key Topics

### Content Strategy and Production

Calibration blog post is complete and ready for Jason's review. GrowthX has adjusted its artifact generation approach—findings from internal testing with the CTO showed that shorter, more concise documents produce better LLM outputs than longer, context-heavy ones. The team aims to publish 3 blog posts next week, ramping to 5 per week after that. The strategy emphasizes comprehensive, original content that genuinely serves user intent and builds domain authority. Industry statistics compilations are a high-potential tactic for generating organic backlinks, though they're more time-intensive because the team verifies all statistics against source reports.

### Website Development

Jason has implemented a basic blog template with title, author, breadcrumbs, and good readability. GrowthX recommended adding a table of contents for two reasons: user experience (helps readers jump to sections they care about, improving time-on-page) and SEO engagement metrics (longer dwell time reduces bounce rate). Given that blog posts are ~1,500–2,000 words, a TOC is essential. The team also discussed chunking content for AI search readability. Jason is also building a dedicated blog listing page to house all blog post entry points once the pipeline exceeds 3 posts.

### Analytics and Reporting

GrowthX set up a Looker dashboard integrated with Google Analytics 4 and Google Search Console. The dashboard includes session/engagement breakdowns by source, landing page performance, conversion events (custom and standard), organic search rankings, and LLM referral traffic. Content performance will be tracked via a cohort report comparing GrowthX blog posts to the rest of Otto's site. Currently, the site shows mostly branded search traffic and early LLM referral signals (ChatGPT, Perplexity), which is expected for a new product. Jason flagged that app user behavior (trip planning) is currently mixed into analytics with static website traffic; the team will separate these to focus reporting on marketing website performance.

### Marketing Operations

Social media shares do not directly impact domain authority (unlike 15–20 years ago), but are valuable for content distribution. The press launch strategy is more important: reaching out to TechCrunch, GeekWire, and travel/business travel publications for coverage will generate high-authority backlinks. GrowthX will compile a list of 20–30 high-domain-authority travel bloggers (Points Guy and similar) using Perplexity for discovery and SEMrush for DA validation. Jason noted that review platforms like G2 and Trustpilot require critical mass (roughly 1–2% response rate from ~10,000 users) to be worthwhile, so Otto will revisit these after scaling user base.

---

## Action Items

**Jason Flateboe**
- Review calibration blog post in Google Doc, leave comments on content, style, tone; add meta thoughts on positioning/voice at top

- Add table of contents to blog post template for improved UX and SEO

- Create page housing all blog post entry points for when >3 posts published


**Aida Knezevic**
- Consult Vivek re: separating app data from static website data in Looker dashboard

- Compile list of 20-30 high domain authority travel bloggers; use Perplexity for credibility, SEMrush for DA; send to Jason for outreach

---

## Transcript

**Erik O'Brien:** Yeah, we just got the image pipeline set up, but I can just let her know we want some color variants.

**Jason Flateboe:** Yeah, that'd be good. I see Bailey's there. How you doing?

**Aida Knezevic:** Hi.

**Bailey Seybolt:** Hi. Thanks to meet you.

**Jason Flateboe:** Good to meet you. Glad to be working together.

**Bailey Seybolt:** Me too.

**Aida Knezevic:** I'm sorry to be in a row, but it's so cold in my apartment. They haven't turned the heating on yet, and it's an unusually cold start to October, so it's like eight degrees Celsius, which is pretty close to 40 degrees Fahrenheit. So I'm bundled up.

**Jason Flateboe:** Go for it.

**Aida Knezevic:** It also doesn't help when you're sitting all day in front of a computer. It's just not good for circulation. Is Michael also joining today?

**Jason Flateboe:** Yeah, he is. It looks like he's moving this way.

**Aida Knezevic:** Are you all in an office space?

**Jason Flateboe:** Yeah, we have an office here in Seattle. We're in a little pod that looks very similar to Bailey's, I'm noticing.

**Bailey Seybolt:** I think we might be in matching pods right now.

**Jason Flateboe:** Yeah, I'm sure it's made by the same company.

**Bailey Seybolt:** Michael, nice to meet you. Hi, it's so nice to meet you.

**Jason Flateboe:** We've got two laptops in one room—that's the trick.

**Bailey Seybolt:** So whenever I talk, it'll look like it's coming from Jason.

**Aida Knezevic:** Okay.

**Jason Flateboe:** You guys know the two-laptop-in-a-room trick.

**Aida Knezevic:** Well, thanks for joining. Bailey, want to do a quick intro?

**Bailey Seybolt:** Yeah, I've worked in tech and startups for about 10 years on marketing and brand teams—a lot of SaaS companies like Greenhouse Hiring, SaaS-focused content marketing agencies, and most recently an AI services company. So a mix of SaaS and services and content. I'm very excited to be here, and I used to travel a lot for work, so I wish Otto had been around 10 years ago because it's a pretty exciting product.

**Jason Flateboe:** I was just at a conference a couple days ago with Marcel, and he said you guys were going to take good care of us.

**Aida Knezevic:** Yeah, we will, no worries. Bailey and I also worked at the same content marketing agency a few years ago, so it's fun to work with old co-workers.

All right, so I've already shared our agenda over email, but I'm going to share my screen. Quick update on the content side: we've generated the calibration blog for you. You should have received it in your email.

**Jason Flateboe:** I don't see anything in my inbox.

**Aida Knezevic:** No worries, let me double-check. If you go to the content OS in the Ready for Review view, you should be able to see the Google Doc column. All comments are helpful—you can leave them directly in the doc. If you have meta thoughts about positioning, voice, and tone, you can write a couple of paragraphs and put it at the top of the doc.

The goal is to get your thoughts on content depth, writing style, and tone so we can update our writing guidelines. We've adapted the way we generate artifacts for clients. Our artifacts are now shorter than before because testing with our CTO showed shorter artifacts produce much better results. The more context you give an LLM, the less consistent it becomes. So we keep them shorter—key points are still there, just less additional context. We'll update artifacts as your feedback comes in.

Our goal for next week is to create three blogs for you, and then we'll go to five per week. Jason just shared the website, which I'm looking at for the first time. It looks good—I love the title, author name, and breadcrumbs.

**Jason Flateboe:** This is all very much placeholder, just a test page template.

**Aida Knezevic:** This is good. It's similar to what we set up for other clients—a news outlet-based template. It's very easy to read.

**Jason Flateboe:** I'm curious if there's anything missing. One thing I consciously left out was a table of contents on the left. Depending on how long the content is, it felt unnecessary.

**Aida Knezevic:** All of our content is around 1,500 words. The calibration blog has five sections, so some posts could be 2,000 words. I'd recommend having a table of contents here so people can click through to what they want.

**Jason Flateboe:** Is the benefit for the user or for ranking and SEO?

**Aida Knezevic:** Bailey, correct me if I'm wrong, but I haven't read about tables of contents as a direct SEO factor. What I do know is engagement rate—how long users stay on your page—matters for SEO. Google measures bounce rate. A table of contents makes it easier for people to find what they're looking for and stay on your site longer than 10 seconds, which counts as an engaged session. So it's both user experience and SEO.

**Bailey Seybolt:** And if we're chunking the content more, it's useful for scanning because of how it appears in AI search. Each paragraph and section needs to stand on its own. I think it's useful from a user perspective, and it also feeds into SEO.

**Jason Flateboe:** Okay, that's all helpful. I'll look at adding that in.

**Aida Knezevic:** Perfect. We're hoping to publish the calibration next week, so this timing is right.

**Jason Flateboe:** Three is the perfect number to start with. I'd add three blog post entry points to our homepage, and then when we go beyond three, we'll launch a dedicated blog page. Two-step rollout.

**Aida Knezevic:** Yeah, that sounds good.

**Jason Flateboe:** For marketing operations, do you have recommendations on how to get more authority? Should I push a snippet on LinkedIn that links directly to the blog?

**Aida Knezevic:** Social shares don't have a direct impact on website authority—they used to 15–20 years ago when SEO was new, but people abused it in forums. Social shares are helpful as distribution, but not for authority. Authority comes from comprehensiveness and originality of content that serves search intent, plus backlinks. You can create content likely to attract organic backlinks—for example, industry statistics compilations. When someone writes a blog post, they're always looking up statistics and they link to roundup posts. These are more time-consuming because we verify all stats against source reports. We find industry reports, download PDFs, use an LLM to extract stats, and compile them into a blog post with narrative. Then we link to those reports at the end, referencing sources. This attracts links and ensures we're not regurgitating old, unverified stats that other sites copy.

Press launches matter too. When you officially go live, more media coverage and launch announcements mean more backlinks to your site, which helps overall website authority that carries over to your blog.

**Jason Flateboe:** We have press mentions on our site linking to other websites. I'm building a page that links out to all of those.

**Aida Knezevic:** Yes, it's helpful to link to trustworthy websites. When publishing content, we avoid external linking. If we do add external links, it's to authoritative resources—industry papers, e-marketer stats, that kind of thing. But really, original, insightful content with unique data gets referenced a lot by other websites and drives authority.

**Jason Flateboe:** Do you have other questions about the website?

**Jason Flateboe:** Not at this moment. My next step is creating that page that houses all blog post entry points.

**Aida Knezevic:** I'll share a test page shortly. In terms of content, we'll wait for your feedback, revise the blog, prep it for publishing, and get started on the three new blogs.

Another thing we prepared is your Looker Dashboard. You should find a link in our Notion workspace. This is your Looker report, and you both have editing access. You can change data sources here. Right now it's displaying session mediums from Google Analytics. You can toggle to see sessions from different sources—paid social, email, organic social.

This chart breaks down sessions versus engaged sessions. An engaged session is longer than 10 seconds and includes a page scroll. Your ratio is currently low, which is normal for a brand new website without much content. Once you build out your site and we publish more content, this will increase.

Below is your landing page performance breakdown. This includes traffic from all sources—referral, email, paid social, everything. You can see engagement rates by page and comparisons to previous periods. This is tracking month over month.

**Jason Flateboe:** Is this for Webflow pages only, or the app too?

**Aida Knezevic:** Anything accessible to the Google Analytics tag shows up here.

**Jason Flateboe:** I think it'll be helpful to separate app data from static website data.

**Aida Knezevic:** Maybe that's a step we can take later. We created this in-house, so our managing editor can look into how to separate that. Google Analytics 4 can capture app data, so it will appear in the dashboard.

**Jason Flateboe:** Just for our purposes, we should focus on the static website, not what users do when planning trips.

**Aida Knezevic:** Yeah, totally. We have filters in the report to focus on static pages. The last chart breaks down sessions by referrers—Google, Facebook, LinkedIn. The non-branded page shows traffic from keywords without your brand name—informational queries. This is Google Search Console data, so you're seeing URL clicks and impressions. It also shows ranking breakdowns by position: how many queries you rank for in position one, page one, page two, three, etc.

Conversion events come from your Google Analytics 4 account. You can set which are most important to track. Some are custom—customer conversion, virtual page view—so let us know which matter most.

The cohort report is super important. We measure your content performance against the rest of your site. Right now we haven't published anything, so we only see non-GrowthX URLs. When we do publish, we'll see our numbers alongside the rest. Content pillar comparative performance shows where topic clusters appear. Looker is connected to Airtable, so when we start publishing, we'll categorize URLs by cluster and see which perform better. Then we'll see individual URL performance—Google Search Console data, organic traffic only.

The landing page report pulls data from Google Search Console, showing URL clicks, impressions, click-through rate, and average position. The queries report shows all keywords you rank for—currently all branded, which is expected. Once we publish and ramp up, you'll see non-branded keywords.

One important thing: Google Search Console takes two to three days to finalize data. If you check on Saturday, come back Monday and it might be different.

For the LLM referral report, this comes from Google Analytics and shows traffic from different LLMs. Right now you're seeing ChatGPT and Perplexity. The filtering might need tweaking. People copying URLs from ChatGPT and pasting them is probably why ChatGPT shows up as a source. I'll check with Vivek on this.

**Jason Flateboe:** Well, I'm just looking forward to this chart going exponentially up and to the right.

**Aida Knezevic:** Don't worry, it will. Impressions usually come in within a week or two of publishing a blog post, then clicks follow. As you publish, results compound. Especially with a brand new site with no organic presence, you see intense growth—six to twelve months in, it's often 200% growth.

**Jason Flateboe:** I told Marcel I'm looking forward to being a case study.

**Aida Knezevic:** Nice. I think that's everything for today.

**Jason Flateboe:** Do you have any other questions? Nope, all good. How can I support beyond day-to-day pushing? We're planning a press launch in the next four weeks—reaching out to TechCrunch, GeekWire, travel sites. We'll aim to have everything under embargo and launch coordinated. Are there other things we can do besides diligently doing our tasks?

**Aida Knezevic:** Industry bloggers, especially business travel bloggers, could write reviews or mentions. They usually come at a fee, but help if they have high domain authority. Leverage high domain authority bloggers in travel.

**Jason Flateboe:** Do you guys have tools to research that? The Points Guy is a good example—road warriors and travel geeks who care about getting hotel points and status. Is there a special way you research this?

**Aida Knezevic:** We can do a deep Perplexity search to find credible ones—that helps us see which ones AI thinks are important. Then we check domain authority in SEMrush so you're not reaching out to low-authority blogs. We could definitely put together a list of 20–30 people.

I also think sites like G2 and Trustpilot are helpful for authority building because AI references them when people look for recommendations. But you probably need one to two percent response on review requests, so with 10,000 active users, you'd get around 100 reviews. You're probably not there yet.

**Jason Flateboe:** We can prep the list of bloggers for you.

**Aida Knezevic:** That'd be fantastic. Let us know what you think of the blog. In the meantime, we'll get to work on the other content.

**Jason Flateboe:** Thank you. Thanks a lot.

**Aida Knezevic:** Bye-bye.
