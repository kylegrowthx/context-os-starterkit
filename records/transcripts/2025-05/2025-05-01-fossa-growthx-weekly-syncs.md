# Fossa <> GrowthX Weekly Syncs

<metadata>
date: 2025-05-01
time: 18:01 UTC
duration: 31 minutes
organizer: aida@growthxlabs.com
participants: Aida Knežević, Jakub Rudnik, Andy Drukarev, Aaron Williams, Kevin Wang
fathom_recording_id: 60317354
fathom_url: https://fathom.video/calls/289315649
share_url: https://fathom.video/share/Ky8Kt_cy7DF8oyZ-xvhXMEW1dsfxss51
source: fathom
enriched_on: 2025-03-03 21:15 UTC
</metadata>

---

## Summary

GrowthX and FOSSA aligned on a major Registry page structure pivot: moving end-of-life content into a core package page with separate tab URLs for security vulnerabilities and version history, allowing them to target distinct keyword clusters (package vulnerabilities, end-of-life, and version history) while maintaining a unified user experience. Key blockers include redirect chain issues in SEMrush (likely from UTM parameter formatting and package observer URLs) and content publishing challenges without a CMS, though both teams agreed a headless CMS would dramatically improve workflow speed. Jakub committed to investigating the redirect patterns and creating a scoped version history outline by end of week, while Andy will continue publishing the CW series and develop concrete Registry implementation details for Kevin Wang's (FOSSA CEO) review.

---

## Context

FOSSA is an open-source security and license compliance platform; GrowthX is providing content marketing and SEO services for their Registry feature — a comprehensive database of software packages with security, version, and licensing information. This is an ongoing client engagement where GrowthX is helping FOSSA expand organic traffic by building programmatic SEO into the Registry. The relationship is collaborative: FOSSA (led by CEO Kevin Wang, with engineers Aaron Williams and Andy Drukarev leading the Registry work) owns the technical infrastructure and data, while GrowthX (represented by Jakub Rudnik on this call, with content support from Aida Knežević) handles content strategy and SEO optimization. This particular sync focused on the end-of-life content vertical — a competitor space dominated by endoflife.date (375,000 monthly visits) — and how to integrate it into FOSSA's existing Registry architecture without compromising performance or user experience.

---

## Relevance

**To GrowthX Delivery:**
- Programmatic SEO for Registry is working; FOSSA's main Registry page is indexed and gaining traction, but individual package pages need indexing investigation
- CMS implementation (headless CMS recommended) is critical bottleneck — Aida has client CMS expertise (WordPress, Framer, Sanity) that could directly inform FOSSA's technology choices
- Content publishing workflow is painful without CMS; temporary blog-post-and-redirect strategy (moving to subfolder later) is viable interim solution that Kevin Wang has used before
- End-of-life content vertical offers significant SEO opportunity (375,000 monthly visits at endoflife.date) and requires thoughtful information architecture (separate tabs/URLs) to avoid keyword cannibalization

**To GrowthX Business Development:**
- FOSSA relationship is expanding: moving beyond simple Registry SEO into strategic product architecture decisions (tab structure, URL hierarchy, data reuse patterns)
- Account health is strong — both teams working collaboratively, issues are tactical (redirect debugging, content publishing), not strategic
- Reference potential: FOSSA's Registry structure (core page + security + version tabs) is replicable for other B2B SaaS clients with large data sets; successful launch could become case study

**To CheckThat:**
- FOSSA is using programmatic SEO at scale (Registry has hundreds of package pages); opportunities to integrate CheckThat prompts into end-of-life and vulnerability content for AI visibility/ranking
- Jakub (GrowthX) is doing manual keyword analysis; could benchmark CheckThat's AEO capabilities against this process

---

## Overview

- Programmatic SEO for end-of-life content: opportunity analyzed against endoflife.date (375,000 monthly visits)
- New Registry page structure decided: core package page with separate tabs/URLs for security vulnerabilities and version history, targeting distinct keyword clusters
- Redirect chain issues identified in SEMrush (new issues on package observer and blog tags, likely UTM parameter formatting); Jakub to investigate
- CMS implementation critical need: content publishing currently blocked without CMS; headless CMS (e.g., Sanity) recommended for long-term scalability

---

## Key Topics

### Content Publishing Challenges

  - All GrowthX SEO content pieces ready for review; Daniel (FOSSA software developer) has code-reviewed them
  - Publishing on FOSSA site is bottleneck without CMS; current workflow is painful and manual
  - Temporary solution: post as blog content with pillar page, then migrate to folder structure later (Kevin Wang has done this before)
  - Headless CMS (Sanity Content, WordPress, or Framer) would dramatically accelerate publishing; Aida has hands-on experience with multiple CMS platforms used by GrowthX clients

### Redirect Chain Issues

  - SEMrush audit (Monday) still shows redirect chains and loops; manual audit initiated and still running
  - Root cause diagnosis in progress: SEMrush setup had issues on FOSSA's side, complicating investigation
  - New redirect issues emerging: many related to package observer URLs and blog tag structure
  - Suspected root cause: old UTM parameters lacked leading slash; new redirect rule adding slash may be creating chains for all UTM-parameterized URLs
  - Jakub to prioritize diagnosis (free day on Tuesday) and leverage GrowthX technical team's broader expertise for support

### Programmatic SEO for End-of-Life Content

  - Analyzed endoflife.date as dominant competitor (375,000 monthly visits, authority in space, extensive backlinks); opportunity to expand beyond their coverage
  - Jakub created detailed outline for FOSSA's end-of-life content strategy, mixing observed data structures from endoflife.date with FOSSA's own expertise
  - Key strategic question: should end-of-life data be standalone property or integrated into Registry? Team debated keyword fragmentation risk (Registry ranking #3 for end-of-life terms vs. dedicated site ranking #1)
  - Decision: integrate into core Registry page with separate tab URLs to target specific keyword clusters without cannibalizing traffic (core page for package info, security tab for vulnerabilities, version history tab for end-of-life)

### Registry Page Structure

  - Core page: `/registry/[package-name]` with base package information and description
  - Security tab: `/registry/[package-name]/vulnerabilities` with vulnerability data, targeting bootstrap/package-name + vulnerabilities keywords
  - Version history tab: `/registry/[package-name]/versions` (or end-of-life) with end-of-life, version release history, and sunset information, targeting end-of-life + version keywords
  - Content reuse strategy: core description and data shared across tabs but presented in tab-specific contexts to provide keyword-focused content clusters
  - SEO advantage: unified interface for users (tab experience) but separate URLs for search engines to target distinct keyword intents without keyword cannibalization

### Registry Indexing and Sitemap Issues

  - FOSSA Registry main page is indexed; unclear if individual package pages are indexed
  - Pending decision: subdomain vs. subfolder structure (was using subdomain, may migrate to subfolder)
  - Sitemap submission issues: using prositemaps.com for automated sitemap generation and submission, but sitemaps showing as "successfully submitted" in prositemaps dashboard while not appearing in Google Search Console
  - Needs investigation: Search Console property setup and sitemap configuration validation; possible DNS/verification issues

### New Redirect Issues

  - SEMrush showing multiple new redirect chains (identified in recent report)
  - Majority of new issues related to: (1) package observer URLs, (2) blog tag structure (Andy flagged these have been heavily modified)
  - Root cause hypothesis: UTM parameter formatting. Old UTM URLs lacked leading slash (e.g., `?platform=...`); new redirect rule adding slash is triggering redirects for all parameterized URLs
  - Package observer URLs will be deprecated; expected to be handled separately via bulk domain-level redirects
  - Action: Need to identify and fix UTM parameter redirect patterns before new redirect debt compounds

---

## Action Items

**Jakub Rudnik (GrowthX)**
- Investigate redirect issues in SEMrush report, focusing on UTM parameter patterns and package observer redirects; prioritize this (available Tuesday) and leverage GrowthX technical team for support
- Create new outline for version history/end-of-life page on registry, targeting relevant keywords and fitting alongside other main pages; scoped to what's immediately implementable

**Andy Drukarev (FOSSA)**
- Develop more concrete details and steps for registry improvements, including potential subdomain to subfolder migration; present proposal to Kevin Wang for review
- Continue work on publishing CW series content; resolve CMS bottleneck (blog post + pillar page interim approach acceptable)

---

## Transcript
**Aida Knežević:** But it's coming along.

**Aida Knežević:** How are you guys doing?

**Aida Knežević:** I can't do it.

**Andy Drukarev:** right.

**Andy Drukarev:** How are you?

**Andy Drukarev:** Yeah, all good.

**Jakub Rudnik:** Sun just came out after like 12 showers of rain.

**Jakub Rudnik:** So nice little after lunch surprise, I'll probably go take a walk after this.

**Jakub Rudnik:** I've been like had fresh air and a day and a half.

**Andy Drukarev:** So where are you located again, Jake Chicago?

**Jakub Rudnik:** So we're we're doing all the Midwest weather, April, two beautiful days, wearing shorts, and then you're going to get the winter code again and just when you think you put it away.

**Jakub Rudnik:** So fun stuff.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** How was that game?

**Jakub Rudnik:** I don't think we've talked since Clippers Warriors.

**Jakub Rudnik:** That was great.

**Aaron Williams:** That was great.

**Aaron Williams:** We lost, of course, but that's OK.

**Aaron Williams:** It was a fantastic game.

**Aaron Williams:** So we're trying to get asked for more than that.

**Aaron Williams:** My 18-month-old son and I were watching.

**Jakub Rudnik:** He's just obsessed with anything sports.

**Jakub Rudnik:** And so he was watching them and trying to bounce a ball on the carpet.

**Jakub Rudnik:** It didn't work.

**Jakub Rudnik:** And he's like, shoot.

**Jakub Rudnik:** And just throw a ball above his head.

**Aaron Williams:** I was thinking about you.

**Jakub Rudnik:** went to overtime and everything.

**Jakub Rudnik:** was like, man, would be a fun one to be at, so.

**Jakub Rudnik:** Yeah, pure luck.

**Aaron Williams:** bought those tickets at the beginning, well, not at the beginning, but kind of the middle of the year when it looked like the Warriors more kind of make the playoffs.

**Aaron Williams:** And so I thought the last game of the year, could probably get some cheap tickets for that one.

**Aaron Williams:** And I could.

**Aaron Williams:** And I just wanted to see the Clippers.

**Aaron Williams:** And it turned out it ended up being a very consequential game, which was.

**Aaron Williams:** Yeah, yeah, what a buy.

**Aaron Williams:** man.

**Aaron Williams:** Nice.

**Aida Knežević:** OK, so today we're mostly going to go over the programmatic SEO update.

**Aida Knežević:** Jake was going to share the end-of-life content that he's been working on.

**Aida Knežević:** Just a quick update from my end.

**Aida Knežević:** And so all of the SEO content pieces are pretty much ready to go for your review.

**Aida Knežević:** I had Daniel, he's a software developer, he looked over all of the code, he said it was okay, it's great to hear.

**Aida Knežević:** If you have any questions or comments, you can tag me directly in the docs.

**Andy Drukarev:** No, I appreciate that.

**Andy Drukarev:** The thing that I'm now wrestling with is just how to get everything published.

**Andy Drukarev:** It's a bit of a challenge considering we don't currently have a CMS.

**Andy Drukarev:** It would be very straightforward if we were hosting them as blogs, but because we're not hosting them as blogs, there's a bit of nuance there.

**Andy Drukarev:** I've already started working on it — the progress looks good.

**Andy Drukarev:** I will continue trying to work on it.

**Andy Drukarev:** If we get to a point where I hit a wall, I might have to post them as blogs and the main page is a pillar page which would all be easy to do, but let's see, I'll keep you posted there.

**Andy Drukarev:** Just a quick question.

**Aida Knežević:** Do you have plan to have a CMS in the future?

**Aida Knežević:** Oh, that's a good question.

**Andy Drukarev:** We've gone back and forth on it internally.

**Andy Drukarev:** I will say that with each passing day, I continue to spend way too much time wrestling with publishing workflows. Our CEO is 10 levels above the rest of the world when it comes to getting things done and being technical and moving fast. But the reality is that even if it takes us a few days to install a CMS, I think it ends up being a time saver in the end because our current process is painful and we're still wrestling with it.

**Andy Drukarev:** Yeah, yeah.

**Aida Knežević:** I mean, we typically do the publishing for our clients, so I'm familiar with a lot of CMS platforms — from traditional ones like WordPress and Framer, to headless ones like Sanity Content.

**Aida Knežević:** Headless CMSs are great — if you have developer bandwidth to set up the backend, it's super easy for the marketing team to publish content with individual components that you can set up.

**Aida Knežević:** I know a lot about this because one of my other accounts is a web development and web design agency, so I've written and edited a ton of content about CMS platforms. If you're spending this much time on publishing, a CMS is definitely a solution. It will be a lot faster.

**Andy Drukarev:** You're somewhat preaching to the choir.

**Aida Knežević:** But yeah, so we'll see where that goes.

**Andy Drukarev:** I think the other thing, Jakub — on the redirect chains and loops. The most recent audit we ran was Monday, and it was still showing all those issues.

**Andy Drukarev:** I just initiated another manual audit.

**Andy Drukarev:** Now it's still running, but we haven't made any changes to anything that would impact that since Monday.

**Andy Drukarev:** So my understanding is that those errors are still present.

**Jakub Rudnik:** Yeah, when that comes in, either email me the results or give me the URL. I want to spot check it and maybe run something duplicated. Thanks for the patience on it — getting my SEMrush setup connected with you has been tricky. There are some issues on how we set up SEMrush on our side.

**Jakub Rudnik:** But I'll take a look. We've set up a bigger channel at GrowthX that's much easier to share data on, and there's a lot more brain space and technical expertise there to help me diagnose this. So I'll prioritize that.

**Jakub Rudnik:** I was hoping to see some improvement, but if it's still there, there's definitely more to figure out. From the tools I'm typically using, it looks like the redirect from the blog side (the one without the leading slash) might be the issue, but nothing looked obviously wrong there. It's been stumping me.

**Andy Drukarev:** Yeah, I'll send a message there.

**Andy Drukarev:** I'll keep you posted.

**Andy Drukarev:** Okay, shifting gears to the programmatic SEO discussion. I talked to my team about what end-of-life sources we have. But with Aaron now on the call, I think there are probably two parts to this conversation: first, what data would we need to rank for end-of-life terms? What sources, what information would we display? Second, is this project part of Registry, or is it a standalone property? Aaron, I'd be curious for your take, but we can start with you, Jakub — what was on your mind and what investigation have you done?

**Jakub Rudnik:** Really, very quickly —

**Jakub Rudnik:** I just wanted to follow up on what you said about the non-blog option. If you have to post as blogs, we can always move that to a folder or subfolder in the future. Publishing and then redirecting a month or two later isn't a big deal. I just want to mention that before I lose track of it mentally. I know it's doable because Kevin did it with another content series.

**Andy Drukarev:** Right. Kevin's our CEO. There will be a fair amount of work in the weeds — asking tools to duplicate and tweak things — but it's doable. It'll just take a few days.

**Andy Drukarev:** Yeah.

**Jakub Rudnik:** We've already got redirect issues to tackle, so we're adding more technical debt there. Okay, so here's what I spent most of this week on: doing the outline for what end-of-life content would look like, analyzing existing content from endoflife.date, which has made a whole entity around this space. Generally speaking, they're covering so many of the keywords, while everything else is fragmented across blogs and other sites. But I think they've built a really good proof of concept with lots of backlinks. They've become the authority in the space, but there's so much more we can expand.

**Jakub Rudnik:** So I put together an outline with some bold points of what I would include — a mix of what I saw on existing pages, what I know from research, plus what you all can supplement since you have more expertise in the space. This isn't really my world; I'm more of a history major and journalist, so there's stuff in here that I'm sure needs tweaking. I was trying to understand what data could exist and what would be required, plus supplemental items. This outline is worth going through in depth to some extent.

**Andy Drukarev:** Do you have search volume data for a handful of these terms? I'm curious about the actual SEO opportunity here.

**Jakub Rudnik:** I should have put that in there. Using endoflife.date as a baseline, they're getting 375,000 monthly visits. Some of their pages aren't going to be relevant for us — like consumer stuff (iPad, etc.) — so those we can filter out. But basically, we could export their data and mark yes or no on each page for whether it's relevant to FOSSA. They rank number one or two on each of these terms.

**Andy Drukarev:** Like the Python page?

**Jakub Rudnik:** Right, the release calendar table. Most of it is custom-written content mixed with templated sections. Some sources like GitHub have specific documentation patterns, while others like Apache have different structures. It depends on what the source looks like. The bulk of their content is the table structure, and that's what people generally use. Our outline is much more extensive, but we don't need everything right away. We need the core pieces, with supplementary data added over time. We can do a V1 and continue adding sections as we scrape more data and it becomes available.

**Jakub Rudnik:** There are some variations in how end-of-life versions appear across different pages, but depending on the page, sometimes you get other long-tail stuff.

**Andy Drukarev:** Going back to your outline, there are several pieces that will be on Registry — the vulnerability stuff, definitely. Currently, Registry has capabilities but no versions. We definitely need versions and version release history. But the question is how to structure this. We could do it a few ways. You could have a core page with the package name in the URL, then `/vulnerabilities`, and another tab for `/end-of-life`, or you could put it all on one page. I lean toward having it all part of the same property. Do you have thoughts on that?

**Aaron Williams:** No, I would lean the same way.

**Aaron Williams:** The challenge we have is that these pages are generated through a fairly complex script. Just adding content into the pages won't be the long-term solution. It might get us content into the pages and be enough for us to test, which I'd be open to. But the real long-term fix is to add this as a new part of the script and regenerate all pages, rather than adding them page by page.

**Jakub Rudnik:** The hardest part for me is knowing what Registry will rank for. Registry is a catch-all page with tons of good information that should be valuable, with people coming in from different ways. But my concern is whether they'll actually come in from end-of-life search terms. Google might say that endoflife.date is so simple and so focused on end-of-life that it will still win. So we need to test whether adding more headers and specific information to Registry gives us the best chance of ranking for multiple things.

**Jakub Rudnik:** I know endoflife.date has done a dedicated property approach, but just because one company has done it doesn't mean we can't attack those keywords differently. We should test whether we can rank for end-of-life and longer-tail version terms on Registry, and not just rank, but rank on page one. If some terms don't work, we can reuse the data and create a separate page type. Data being valuable in multiple places is a good thing — it's less work and more bang for your buck. We just don't want cannibalization if we create two separate things. But if Registry is on page three for end-of-life queries and we want that traffic, we'd need something else.

**Andy Drukarev:** My gut is that we have a core page, then essentially three tabs with separate URLs. You have security, which gives all the vulnerability information with a separate URL targeting package name + vulnerabilities keywords. Then you have version history or versions, and the versions tab has all the end-of-life information with its own URL targeting end-of-life and version history keywords. Does that make sense?

**Jakub Rudnik:** It does. The version I have of Registry doesn't show the security tab, so I've been operating on something old. But I love this approach — it feels like you're on one page but with separated URLs. Even though there's some duplicate content, that's okay if the security section has so much extra content specific to that URL. It solves my concern about the catch-all problem. You have one frame but catching three different things in three targets, showing Google hyper-specificity while reusing the core description and data in a good way. It's context that's reusable.

**Jakub Rudnik:** So it was all makes sense to me.

**Jakub Rudnik:** And then the URL structuring, it's like creating little mini content clusters.

**Jakub Rudnik:** So the inner linking is really natural and you don't have to force that where often that happens on a page like this.

**Andy Drukarev:** So I think my ask will be, and I put a sample of a registry page in the Slack channel would be based on the content that currently exists.

**Andy Drukarev:** What a

**Andy Drukarev:** like version history kind of sub page would look like.

**Andy Drukarev:** What elements are there?

**Andy Drukarev:** What SEO metadata should be included to maximize our chances of ranking for the end of life keywords that do exist?

**Andy Drukarev:** I do think it's a little bit tricky.

**Andy Drukarev:** Most of the search volume is not like a name end of life.

**Andy Drukarev:** It's really about different versions of the stuff.

**Andy Drukarev:** So I think that's probably the next step is it relates to kind of your support of this project.

**Andy Drukarev:** think parallel on our side, like I need to go back to Kevin and Aaron and like put together like propose this essentially of like we have our core page that has like core package information.

**Andy Drukarev:** You know we have a vulnerabilities page which again it's like a tab but it does have its own URL.

**Andy Drukarev:** does have version history end of the page.

**Andy Drukarev:** Yeah.

**Jakub Rudnik:** We can take what we've pulled and sell

**Jakub Rudnik:** A lot of that kind of goes away because it's built into the registry page or the other tabs to reformat and build like kind of get into this tabular structure.

**Jakub Rudnik:** Yeah, that's easy to do.

**Jakub Rudnik:** Yeah, Aaron.

**Andy Drukarev:** Aaron, do you have any context on Registry progress over the past few weeks?

**Aaron Williams:** We've been spending time talking about snippets more than Registry. It hasn't really come up much in the past couple of weeks, but I can have a conversation about it. Are we indexed with these pages?

**Andy Drukarev:** I believe so. I know the FOSSA Registry main page is indexed, but I'm not sure if any of the individual package pages are.

**Jakub Rudnik:** Is this moving to a subfolder rather than a subdomain? Is that the latest?

**Andy Drukarev:** I believe that was the plan, but we need to have an internal discussion to figure out the right approach. The subdomain is what's currently indexing, but I thought I saw something on the subfolder side. It was the subdomain vs. subfolder conversation.

**Jakub Rudnik:** I can look quickly in Search Console.

**Andy Drukarev:** I'll need to add a property for it. I'm also having trouble with the sitemap submission. I'm using prositemaps.com, which gives you different submission options. It tells me the sitemaps have been submitted successfully, but they're not showing up in Search Console. Let me share the link with you.

**Jakub Rudnik:** So it's showing up under the subdomain in Search Console as indexed (main page), but you don't see any of the individual pages?

**Andy Drukarev:** Yeah, there's an internal conversation needed there.

**Andy Drukarev:** Okay, so next steps. Let me check what the SEMrush report is showing. I'm seeing even more redirect changes.

**Jakub Rudnik:** All of these are new?

**Andy Drukarev:** Yeah. So my top ask is to see what you can dig up on your end. You should have access to our SEMrush account.

**Jakub Rudnik:** Yes, I do. I can see this directly. This is interesting — if the top one is a tag URL and we don't have a CMS page anymore but the page still exists. I would not pay as much attention to the package observer ones because those are likely going away. We'll have to do bulk domain-level redirects for the rest. Do you have any guidance on what redirects to investigate?

**Andy Drukarev:** Yeah, see what you can find.

**Jakub Rudnik:** Okay, that'll be my priority. I've got a pretty free day tomorrow, so I'll try to get this done by end of week.

**Andy Drukarev:** Looks like the new ones are a lot of package observer URLs and blog tags. We've been playing around with the blog tagging stuff a lot. The old ones might be a mirage — was that UTM stuff?

**Jakub Rudnik:** Like if the old URLs had UTM parameters without a slash?

**Andy Drukarev:** Right. I think most of this is package observer and blog tags. My gut is it's mostly those, but I'm still interested in any guidance.

**Jakub Rudnik:** Look at the one you're hovering over. You've got `/platform?` with no slash before the question mark. The old way UTM parameters were set up didn't include the slash. Now that you've added a redirect to add a slash, you're instantly getting redirects on everything with a UTM parameter.

**Andy Drukarev:** I think that's right. I'll look for those patterns — there are probably a few different ones.

**Andy Drukarev:** Okay, so on your end, the two asks are: first, this redirect diagnosis, and second, a newly scoped version history/end-of-life outline that targets reachable keywords and fits alongside the other main pages on Registry. On my end, I'm working on publishing the CW series and getting more concrete details and steps around Registry.

**Jakub Rudnik:** Okay, that sounds good. I'll work on reformatting the data and the new structure for Registry.

**Andy Drukarev:** Aaron, anything else from your side?

**Aaron Williams:** No, we've got some things to discuss internally, but once you get some of these hammered out, there's so much potential. It's a lot of moving parts, but there's only opportunity.

**Jakub Rudnik:** Yeah, there's additional sections and so much to do beyond this.

**Aaron Williams:** That's alright.

**Aida Knežević:** Alright, guys.
