# Fossa <> GrowthX Weekly Syncs

<metadata>
date: 2025-04-24
time: 18:00 UTC
duration: 34 minutes
organizer: aida@growthxlabs.com
participants: Aida Knežević, Andy Drukarev, Jakub Rudnik
fathom_recording_id: 59065605
fathom_url: https://fathom.video/calls/283667803
share_url: https://fathom.video/share/3Unw1j3tP8y4SEqxeQPm2MssXPaysJep
source: fathom
enriched_on: 2026-03-04 09:00 UTC
</metadata>

---

## Summary

GrowthX and FOSSA aligned on CWE (Common Weakness Enumeration) content strategy, deciding to complete 10 articles (1 pillar + 6 cluster pages + 3 pending) before pausing, with Andy leading the setup of a dedicated subfolder structure. The team identified critical sitemap issues (only glossary URLs currently indexed) and agreed to prioritize fixes while researching best practices for building sitemaps without a CMS. On the programmatic front, Jakub will draft end-of-life data elements and structure to inform a separate property experiment, with Andy reviewing available data sources and planning to explore whether registry pages can rank for multiple intents (package name, vulnerabilities, end-of-life) simultaneously.

---

## Context

FOSSA is a software supply chain security platform and GrowthX's client for content marketing. This weekly sync is part of an ongoing engagement where GrowthX develops SEO-driven editorial content and programmatic strategies to increase FOSSA's organic visibility around software security topics. The relationship includes both tactical content creation (CWE articles, OWASP pages) and strategic planning (programmatic content for registry data, sitemap architecture). Jakub Rudnik is not a GrowthX employee but appears to be a consultant or contractor providing SEO expertise specifically for this engagement.

---

## Relevance

**To GrowthX Delivery:**
- CWE content approach (pillar + clusters) validated by keyword volume analysis (e.g., CSRF: ~1k searches/month, owned by Black Duck competitor). Demonstrates the value of GrowthX's editorial process and SEO-informed structure.
- Sitemap issue highlights critical deliverable oversight — GrowthX should review other client implementations for similar gaps.
- Programmatic content strategy debate (separate property vs. subfolder) shows evolving client needs; Jakub recommending pragmatic MVP approach (launch 500 registry pages, measure performance, iterate).

**To CheckThat:**
- Potential opportunity: FOSSA's hallucinated OWASP sections and broken internal links could be audit fodder for CheckThat AI visibility reports — shows where AI-generated content fails search and ranking health checks.

**To GrowthX Business Development:**
- Account health signal: FOSSA's engagement depth (weekly syncs, multi-month content build, programmatic experimentation) suggests strong relationship. Expansion opportunity to other product lines (e.g., license compliance, supply chain risk content).
- Reference potential: CWE strategy + sitemap fix + programmatic rollout plan could serve as case study for B2B SaaS clients with similar technical SEO needs.

---

## Overview

- 7 CWE articles ready for FOSSA review; 3 more to be completed by Monday
- Site map issues identified; only glossary URLs currently included
- Plans to explore programmatic content generation for end-of-life data
- Decision to create a separate property for end-of-life content initially

---

## Key Topics

### CWE Content Strategy

  - 7 CWE articles (1 pillar, 6 clusters) ready for FOSSA review
  - Code snippets reviewed by software developer, only missing language labels
  - Decision to complete 10 CWE articles total, then pause
  - Considering dedicated subfolder vs. blog for CWE content
  - Jakub recommends subfolder for long-term SEO benefits if expanding to 15-20+ articles

### Site Map Issues

  - Current site map only includes glossary URLs
  - Potential impact on indexing and crawl efficiency
  - Andy to prioritize fixing site map issues
  - Jakub to research best practices for site map creation without CMS

### OWASP Page Improvements

  - Some sections (e.g., "how FOSSA addresses issues") contain hallucinated content
  - Andy to work on de-indexing problematic sections
  - Potential to use editorial process to improve and optimize content

### Programmatic Content Generation

  - Discussing strategy for registry pages: package name, vulnerabilities, end-of-life date, licenses
  - Debating between separate properties vs. single domain with subfolders
  - Concerns about splitting search intent and potential keyword cannibalization
  - Decision to start with separate end-of-life property, can 301 redirect later if needed

### End-of-Life Content Experiment

  - Jakub to create draft of data elements needed for end-of-life keywords
  - Andy to review available data sources (public and FOSSA-specific)
  - Goal to combine best available data with SEO requirements

---

## Action Items

**Andy Drukarev (FOSSA)**
- Work with Kevin Wang to create dedicated subfolder/page for CWE content, similar to OWASP page structure
- Review 7 CWE articles in Airtable labeled "ready for foster review" (1 pillar + 6 clusters, all code snippets already reviewed by software developer)
- Investigate and fix sitemap issues (currently only includes glossary URLs; only references glossary in sitemap.ts file)
- Prioritize sitemap fixes and consider de-indexing OWASP pages with hallucinated content (broken links, "how FOSSA addresses" section, real-world examples)

**Jakub Rudnik (GrowthX / SEO Consultant)**
- Research best practices for building sitemaps without a CMS, considering future expansion needs (particularly for 300k+ registry pages with 50k URL limit per sitemap)
- Create draft/sketch of end-of-life data elements and structure for programmatic pages based on keyword analysis; send to Andy for review before next call

---

## Transcript

**Jakub Rudnik:** There is a ritual, just hanging out to you there, I'll do one.

**Andy Drukarev:** Hello. How's going?

**Aida Knežević:** Is anybody else going to join us today?

**Andy Drukarev:** Okay. Give me one second.

**Aida Knežević:** Well, we can, I think, just get started. So, I guess we can get started with just a quick editorial update.

**Aida Knežević:** So, if you go to Airtable, you'll see that there are seven CWE articles that are ready for review. One of them is a pillar page and six of them are clusters. All of the code snippets were reviewed by a software developer and they were all pretty much correct. The only thing that was missing were some language labels, which are helpful when they're added in.

I know that you mentioned one thing — just to do these articles as part of the cluster and then move on with programmatic, which is totally fine, and I would love to get something set up programmatically very quickly. But in the future, even if you're doing it internally or maybe even if we do it, I do recommend completing the cluster just because the CWE keywords specifically are combined keyword, issue-based vulnerability, and are a lot higher in volume. Cross-site request forgery, for example, has around a thousand searches per month, and Black Duck owns the feature snippet. So, it's really a no-brainer in terms of content for the future.

All of the cluster pages follow a similar structure. Some of them might have an additional h2 if there's anything super specific for that vulnerability. I included that, but typically they are all quite similar because we want to keep them uniform.

I also just took a quick look at the OWASP pillar page and one of the cluster pages, and I know that you guys just set it up and published it to see what kind of results that you would get. When you do update them, I think there are a couple of pages that are top ranking for those targeted keywords that serve as good inspiration.

**Andy Drukarev:** If they go into more details, the OWASP page looks great. It might just need some more detail to cover what we discussed.

For the CWE cluster, I don't disagree on completing the cluster. I think it's a matter of how many cluster articles would get us to a point where we feel like it is complete. If the answer is we feel like it takes seven, then that's great. It's less than that? Also great.

**Aida Knežević:** I mean, it's just me being a little perfectionist, but I do want the 25. If it's a list of 25, I want the 25 on the site, but I understand that's a lot. We did a couple of them now, and one of the articles compares CWEs to OWASP, so we have a good cluster going right now.

**Andy Drukarev:** How many are ready for us to publish?

**Aida Knežević:** All of them are ready for you to review. If you review them and think they're good, you can publish them.

**Andy Drukarev:** How do you recommend we publish? Is it something that goes on the blog normally, or would you recommend something closer to what Kevin did with the OWASP page, where it's kind of its own sub property?

**Aida Knežević:** I think it's a good idea to have it on its own, like the OWASP. I don't know if Jakub disagrees. If you're going to turn it into a really big cluster, I think that would be helpful. But if it's not going to be that big, then maybe you might just keep it on the blog.

**Jakub Rudnik:** Yeah, I think if it's just a handful of articles, then it's not deserving of that larger folder. If you start to build out to maybe 10, 15, 20, then that fuller, more specific cluster makes sense — it's more intentional. With URLs and subfolder structuring, when you're standing something up, it's not as bad as with subdomains, but there's a little bit of restarting the clock. If you start something in that folder, it might be a little bit slower, but longer term it does show well. When you have that folder and all the slugs underneath, it seems to build more momentum over time, especially if it's done well and there's a lot of content. And if you're doing offsite backlinking, each link that comes into that subfolder powers that folder. So with 25 concentrated articles, I've found that works better than spreading across a blog with hundreds of articles.

You can put it on the blog too for ease, and it probably will be a little bit faster to rank and build right now, just because you've had blog success and you'd be starting a subfolder from scratch. But I don't think that would be too dramatic on the timelines.

**Andy Drukarev:** I guess the other consideration is, if we do all 25, they go on a dedicated page. If we only do seven, there's a place to work around it — you maybe have your pillar page and links that you click through for just seven of them. I guess I lean toward doing the page and giving it our best shot. Then we can chip away at the other 18 CWE articles over time as well.

**Jakub Rudnik:** That's the other thing — if we know we want to do some other experiments or spread across a couple of different things, we can still build it that way and then plug in articles over time and expand. That's what you're saying — it's an option. It's going to be a while before you see significant traffic unless you're promoting it elsewhere. So building out that cluster over time, you won't have readers for it to feel empty as it's starting to rank. It will still work better with the whole library of content, but we can do that over the coming weeks too.

**Andy Drukarev:** Okay, so that's the CWE plan. I will review the articles that are ready for review in Airtable, just to confirm all of those have been reviewed by a software developer.

**Aida Knežević:** Yeah, so there are seven labeled ready for FOSSA review, and those were reviewed by a software developer. I also want to finalize the three that are in article generation state — I've got them semi-done and just need to do a final draft review. Then the software developer has to review the code. I hope to have that done by Monday.

**Andy Drukarev:** Great. Let's do the 10 and then let's call it for now. We'll put a pause on it. The pillar page is the CWE list of 25, right?

**Aida Knežević:** Yeah, the pillar page is the CWE top 25.

**Andy Drukarev:** Right. I will work with Kevin on the OWASP-like template — that's something that takes a bit of creativity and some coding and stuff. So I will work with Kevin and we'll find a way to get those published. That feels logical.

**Aida Knežević:** Sounds good. Before Jakub jumps into the programmatic stuff, your sitemap — I don't know if that's an issue with the sitemap or if there's something wrong, but we use AirOps to generate content, and we pull URLs from your sitemap for internal linking. When I fed your sitemap into AirOps, it only pulled URLs from the software supply chain glossary. It couldn't find anything else. So it might be that the sitemap doesn't include all of the pages on your site, but I just wanted to flag that in case you weren't aware of it.

**Andy Drukarev:** It shouldn't be happening. Since you're not using a CMS, how is that sitemap being built and submitted to Google Search Console? I'm looking at our repo now, and I see a sitemap.ts file that only references the glossary. That's not great. I also noticed some things in Google Search Console that weren't looking normal, which would align with the sitemap issue.

**Jakub Rudnik:** The broken sitemap isn't impacting ranking yet, but what is the role of the sitemap? I know it's important, but in what specific ways is it important for search?

**Andy Drukarev:** It's going to help show Google your site structure and show new pages, speeding up time to indexing. I'm wondering if this is affecting the registry indexing. The glossary is indexed, but is there another issue we're missing? Google still crawls your site even without a sitemap, but...

**Jakub Rudnik:** But if there's something that's not linked from your homepage or header/footer, it becomes an orphan page — much more difficult to find. A sitemap can solve that. It helps with crawl depth. Of course, you want to build that into your website architecture anyway, but a sitemap solves a bunch of those problems.

You can trigger Google to reindex the sitemap when a new page is published. When I launch a big batch of content, I'll ask Google Search Console to re-index the sitemap. If we're launching 500 registry pages, that's what I would want to crawl. It speeds up everything and makes sure things don't get missed.

**Andy Drukarev:** Are there any best practices for building out the sitemap that we should be mindful of?

**Jakub Rudnik:** Let me follow up on that research because I've never done it without a CMS. I usually have something auto-built. So I've had a big crutch. I'm curious about best practices here, especially with your various site sections and thinking about how you want to map things down the road. If you're going to expand programmatically, you'll need to future-proof the sitemap because you'll need multiple sitemaps for the amount of pages you have already, and definitely in the near future as you launch more.

**Jakub Rudnik:** A sitemap has a max limit of around 50,000 URLs uncompressed. So if you're launching 300,000 registry pages, we'd want to break that into more manageable chunks. If we could cluster or theme the registry pages in some way, that could help 300,000 pages be broken into smaller sitemaps that make sense together.

**Andy Drukarev:** Okay, that's all cool. We will prioritize this right now. For the OWASP pages, I knew about the broken links. But there's another issue — the "how FOSSA addresses or helps fix this issue" sections are hallucinated, and the real-world examples are also hallucinated. So I'm going to see if we can get those de-indexed because they're way off right now.

**Jakub Rudnik:** They're not generating significant ranking risk right now, but there's an opportunity here. The sections visually make sense and have the structure you'd need. This could be something we do as we continue to explore programmatic pages. Should we use our editorial process to update and publish, take some of that framework but use the new fact-checker and really improve the content, optimize, and do the interlinking more properly? That could be something we do in the next stage as well. It could kill two birds with one stone.

**Andy Drukarev:** On the programmatic side, I'd like your perspective. With the registry, there are potentially three things we'd want each page to rank for: one is package name, one is package name plus vulnerabilities, and one is package name plus end-of-life date. You could also add a fourth — package name plus licenses. The question is, there are probably two ways to do it. One is to have a separate property for the registry focused on package name and vulnerabilities, with a separate property that focuses on end-of-life. The other way is to have each package get a root page with slash vulnerabilities and slash obsolescence (EOL). Do you have a perspective on the right approach?

**Jakub Rudnik:** My answer is evolving based on research over the last week and discussions about your space and the different search intents behind each query. The first way we normally think about this — both editorial and programmatic — is: what is the query and what content is needed to answer it? Then, what else can we add that competitors have or that would be really useful?

The registry does that, but I'm nervous about splitting search intent — trying to do three things at once. If competitors have done the micro search better, there's a risk the registry ranks 13th for all three but never at the top for one. That's my worry.

But looking at sites like Snyk, they're not ranking for end-of-life stuff because they're not trying to. The hard part is we're trying to take what Snyk did and build upon it. There's not enough competition in end-of-life. There are a few registry-ish things, and I can't say definitively that if we added the right information and made it readable, the registry couldn't also rank for end-of-life. So we could build a separate end-of-life database that's focused and clear, but there aren't many competitors there. Could the registry do all three? Maybe. That's the problem with SEO — we won't know until it goes live.

I think some of the early optimizations we suggested have come through, but definitely want to follow through and take what we've learned and build it in. Let's launch 500 registry pages and then see if we're picking up end-of-life keywords. We can have the end-of-life date on a registry page, and if it's not ranking for end-of-life keywords, then we build out that end-of-life

**Jakub Rudnik:** database. There are ways to roll it out in V1 where we hope for everything, and then build on top of other areas programmatically. I don't know if that's a great answer, but it's a way to not do three things when only one is necessary.

I'd be worried if you need 300,000 registry pages, plus each with 10 vulnerabilities, that's 10 pages each. Suddenly you're looking at a crawl budget in the millions of pages. Maybe that works, but it's a long-term build. Even if done perfectly, it will take a long time. So those are my thoughts on this.

**Andy Drukarev:** If we do build it as a separate property and we ultimately decide we want a dedicated subfolder within the registry, we can always 301 redirect it. Not ideal, but something we could do.

**Jakub Rudnik:** G2 is my best programmatic experience. We built product pages and category pages, and over time realized we definitely wanted comparison pages. Some was on the page, but we built dedicated comparison pages because they weren't ranking well enough. When you build a new page type, it's because the original pages weren't ranking enough. You see traffic even shift. So you can build one way and redirect if you wanted to.

I'm on the side of doing one thing really well, seeing what happens, and building on top. I would want to look at the URL structure and think about what we'd do to future-proof it. We need a plan in place if we add vulnerability pages or end-of-life pages. I don't think that would change anything too dramatically — I just want to give some thought to it.

**Andy Drukarev:** Do we have any risk of keyword cannibalization by building a separate property that prominently mentions the package alongside end-of-life against the registry?

**Jakub Rudnik:** If you make it so specific and strictly end-of-life, you should have different enough intents from what I'm seeing in the SERPs. The intents look different enough — when you search any of those three things, you get completely different results for each section. The cannibalization isn't there. G2 ranks for "Salesforce," "Salesforce alternative," and "Salesforce versus HubSpot" because it has different pages for each. Though they're so close, they're more like a cluster. It makes sense to have one page for each because they answer different queries.

**Andy Drukarev:** What would the next steps look like if we do want to run an end-of-life programmatic experiment?

**Jakub Rudnik:** The biggest thing I need to understand is what data you have proprietary and where you pull the data from. Then I want to scope the domain that's focused on end-of-life — how are competitors structuring it? What do they have? What information is there? Pull any good sources from end-of-life, whether blogs or pages, and take the best of those. Wireframe what information needs to be in each page. How does the data come in? Where do we supplement if we need information you don't have? Can we launch a V1 without it and pull over time?

The right first step is if you could sketch out what data should be on each page based on your keyword and search volume analysis. What would put your best foot forward? If you can build that out, I can then go see what public data exists and what you have at FOSSA.

**Andy Drukarev:** I think the good thing about this is that for now I think it's right to have the separate property. But even if we end up combining this onto the registry page, we'll need to do this anyway. So I think that's the right starting point.

**Jakub Rudnik:** Yeah, I'll do that this week and send you something ahead of our next call. That makes sense on what's in there, and then we can supplement with whatever is on your end.

**Andy Drukarev:** Great. So next steps, I will review the seven CWE articles in the cluster. Once I get through all of them, we'll start building that out as a subfolder on the site. Then we'll look forward to the draft of what data and what elements would help us write for end-of-life keywords.

**Jakub Rudnik:** Sounds good. I like it.

**Aida Knežević:** Great, we have a plan. See you next week.

**Jakub Rudnik:** See you.

**Aida Knežević:** Bye.
