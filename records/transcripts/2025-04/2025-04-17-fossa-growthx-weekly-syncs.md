# Fossa <> GrowthX Weekly Syncs

<metadata>
date: 2025-04-17
time: 18:01 UTC
duration: 17 minutes
organizer: aida@growthxlabs.com
participants: Andy Drukarev, Aida Knežević, Jakub Rudnik
fathom_recording_id: 57941820
fathom_url: https://fathom.video/calls/278455474
share_url: https://fathom.video/share/z5M3QYfhxEP4s1KYVp4wbLsHpWfdLAmi
source: fathom
enriched_on: 2025-03-04 12:15 UTC
</metadata>

---

## Summary

GrowthX and FOSSA aligned on a narrowed content strategy for FOSSA's technical CWE blog series—shifting from publishing all 25 CWEs to focusing on the 4-5 most popular CWEs plus supplementary content like CWE vs CVE comparison articles, aiming for 10 editorial-style articles per week. The team discussed implementing a code review process to ensure technical accuracy of code snippets and error representations before publication, with options ranging from 15-20 minute manual reviews by engineers to automated fact-checking. After completing this initial cluster of 5 CWE articles by end of week, the team plans to pivot to PSEO (programmatic SEO) experiments, with Jakub to propose ideas for discussion next Thursday.

---

## Context

FOSSA is a major client in the security/software development space, engaged in a long-form content initiative with GrowthX to build technical authority through a series of blog posts focused on Common Weakness Enumerations (CWEs)—a standardized list of common security vulnerabilities. The engagement centers on creating in-depth, technically accurate articles that target security-conscious developers and organizations. GrowthX is responsible for content generation, editing, and delivery in markdown format for FOSSA's GitHub-based publishing workflow (pull requests rather than a traditional CMS). Quality and technical accuracy are paramount given FOSSA's position as a trusted resource in the security space; hallucinations or inaccuracies in code examples or vulnerability descriptions could damage credibility.

---

## Relevance

**To GrowthX Delivery:**
- Quality assurance is critical for technical content—GrowthX implementing fact-checking and code review workflows to catch AI hallucinations (fabricated statistics, made-up quotes, product misinformation)
- Narrowed scope (5 CWEs instead of 25) reduces delivery volume but increases editorial effort; GrowthX capable of delivering 10 editorial articles/week with full review cycles
- Factoring AI output accuracy into polishing instructions (jobs-to-be-done analysis) and enriching with source documentation significantly improves output quality
- Delivery model for FOSSA is markdown files via GitHub pull requests, not CMS integration—GrowthX handles export and handoff
- Code review process decision due by Tuesday next week; options include freelancer review (15-20 min per article) vs automated fact-checking

**To CheckThat:**
- Strong alignment opportunity: PSEO (programmatic SEO) experiments on FOSSA's domain after CWE cluster completion; CheckThat visibility could be tested on low-signal content or tool-based pages
- FOSSA is exploring AI-driven content at scale; programmatic approaches may include interactive tools or comparison pages where AI visibility is testable

**To GrowthX Business Development:**
- Account health strong: client actively collaborating on strategy refinement, clear decision-making (Andy Drukarev has clear technical vision), weekly cadence with senior GrowthX people (Jakub, Aida)
- Expansion potential into PSEO methodologies; early success with AI-powered tools mentioned by Andy—referenceable as case study
- Timeline pressure (5 articles by end of week) and fact-checking decision by Tuesday signal operational maturity and commitment

---

## Overview

- Shift from 25-CWE content plan to 4-5 most popular CWEs + supplementary topics (CWE vs CVE) for higher editorial quality
- Deliver at 10 editorial articles/week (vs 30/week for purely programmatic content) due to review and editing overhead
- Implement code review process for technical accuracy: either 15-20 minute manual review by engineer or automated fact-checking; decision due Tuesday
- Fact-checking layer added to AROP workflow to catch hallucinated statistics, fabricated quotes, and product misinformation
- Publish 5-article CWE cluster by end of next week, then transition to PSEO experiments
- GrowthX delivers markdown files via GitHub pull request workflow (not CMS)

---

## Key Topics

### Content Quality Assurance

Fathom AI-generated content commonly produces hallucinations—fabricated statistics, made-up quotes, and product misinformation—which Aida has encountered repeatedly across client work. The team discussed layering fact-checking into the AROP (content generation) workflow by adding a step before internal linking. Aida flagged that Daniel (developer) can implement this. Secondary strategy: enrich polishing instructions with jobs-to-be-done analysis (identifying what the product actually does and how people use it), which significantly reduces AI misrepresentation. For product-specific accuracy issues, Aida uses ChatGPT with direct product documentation URLs to rewrite sections with accurate information.

### Technical Accuracy and Code Review

Andy's primary concern is the technical correctness of code snippets, error representations (like GW-787 errors), and CWE-specific technical details—not marketing copy. The team landed on two viable approaches: (1) human review by an engineer with security/development background (15-20 minutes per article to validate code), or (2) a tech-enabled automated fact-checking process. Andy noted he's comfortable with either. Decision to be made by Tuesday next week. GrowthX mentioned potentially bringing on a freelancer for code review.

### Content Strategy Rationale

The original 25-CWE plan was too broad for the effort level. Andy prefers 4-5 most popular CWEs (which have higher search volume) plus supplementary topics like CWE vs CVE, which Aida will keyword-research. Publishing all 25 vs focusing on 5 makes minimal difference to overall search volume. After this cluster completes, the team will explore programmatic content and PSEO (programmatic SEO) experiments where AI-generated tools and comparison pages could generate volume without the heavy editorial lift.

### Publication Workflow

FOSSA doesn't use a CMS—everything lives in markdown files and GitHub pull requests on their master branch. GrowthX will export markdown files for FOSSA to integrate directly via PR. Aida initially asked about adding a team email to their CMS; when Andy clarified they're using Git-based workflow, the team confirmed markdown export works perfectly.

### Registry and Site Stability

Andy flagged that FOSSA is stabilizing the existing website and expects to make changes to their scripts in the coming week. Jakub offered to pull the GrowthX team in as needed for support.

---

## Action Items

**Aida Knežević (GrowthX)**
- Conduct additional keyword research around new CWE-related topics identified in meeting.
- Complete remaining CWE cluster articles (5 total). Focus on 4-5 most popular/common CWEs + new ideas (e.g. CWE vs CVE). Deliver by end of next week.
- Discuss code review process with Jakub; potentially bring on freelancer for code review if pursuing manual review option.

**Jakub Rudnik (GrowthX)**
- Prepare PSEO experiment ideas for FOSSA. Present options in next Thursday's meeting.

**Andy Drukarev (FOSSA)**
- Decide on fact-checking process (manual review by engineer vs automated) for CWE articles by Tuesday next week. Inform GrowthX of decision so publication can proceed.

---

## Transcript

**Andy Drukarev:** QA and technical correctness—the concepts here certainly fall within my technical knowledge. So I don't know if you have any general philosophies on that. We're working toward putting in some infrastructure where a piece gets a certain amount of traffic and that triggers a manual review, but until then there's a pretty low bar for publication. For some of your other more technical customers, how are they dealing with that sort of thing?

**Jakub Rudnik:** I mentioned last week that the general philosophy at GrowthX—never having worked in a purely technical company—is how I've approached it. We try to use broad internet sources, but the better source material we can get and feed into our systems, the better our output. We're looking for white papers and reports that really speak to the technical language and get these details right. We do a lot of upfront work on that.

The one piece specific here is that we have cybersecurity and adjacent clients that aren't direct competitors but are in the space. We're actively seeking editorial oversight—someone who can bring that expertise—because we have a cluster of clients facing this. There's potential future support here, though I don't want to promise it, but it's being actively searched. Otherwise, it's a lot of upfront work feeding the right material. Some clients have to route everything through legal and bank reviews for every single piece. For those situations, we automate all the parts we can and try to just get to that review stage.

**Aida Knežević:** One thing we can do as an extra layer of safety: we could add a fact-checking step to the AROP article generation workflow, right before internal linking. I can have Daniel add that in. As someone who's edited a lot of AI content across various clients, the errors usually come down to made-up statistics, fabricated quotes, or invented examples. I always remove those. With the content I delivered this week, all the real examples are actually real—I double-checked that they're happening and that the consequences the AI described actually occurred. Those are the major issues I've seen come up across the board.

**Andy Drukarev:** When our CEO Kevin built out the OOS series, the big issue was hallucinations around how certain products helped solve problems. There's not a ton of source material on that, so AI makes up its own narrative. What would the fact-checker be—what sort of tool would you use?

**Aida Knežević:** I'd have to ask Daniel how it runs in the background—that's the developers' work. One thing I can show you on product hallucinations: we get around that in the polishing instructions by adding jobs-to-be-done analysis—just thinking through the main things your product does and how people use it. We can enrich this with additional company information. When I'm editing content and FOSSA or another company is mentioned, I paste the specific URL of a product page and ask the AI to redo that section using accurate information from that page. It gives me much more control and better results.

**Andy Drukarev:** I'm less concerned about that for these posts because I'll be able to manually correct anything. My bigger concern is that the technical details—code snippets, error representations like GW-787 errors—are actually representative. There should be some fact-checking: either a security person or just developers looking at the code to make sure it's coherent. That would be good.

**Aida Knežević:** I'll have to discuss this with Jakub. I might know someone we could bring on as a freelancer to do the code review of these articles.

**Andy Drukarev:** Looking through the CWE-787 example you shared, it seems right. I don't see obvious concerns. I think the real decision is just what our process is for fact-checking. Either a human from your team with an engineering background doing a 15-20 minute review of the code snippets, or some sort of tech-enabled, automated process—either is fine. After we settle that, I'd be comfortable moving forward to publication.

**Jakub Rudnik:** Sounds good.

**Aida Knežević:** The cluster we have in Airtable right now is based on the 25 CWEs. We can expand with additional ideas like CWE vs CVE and others. I need to double-check that there are actual keywords we could target with this type of content, but these would enrich the pillar.

**Andy Drukarev:** I like that, especially CWE versus CVE. That one has search volume. Yeah, the first two especially. I'd be comfortable adding those to the list.

**Aida Knežević:** I could do additional keyword research around these topics. Another thing: when it comes to publication, we usually handle publishing for our clients. If you want, we can add our team email to your CMS.

**Andy Drukarev:** We don't currently have a CMS. Everything is done via pull request and markdown files added to our master branch. We just need you to export markdown files and we'll take it from there.

**Aida Knežević:** Good to know. I wanted to double-check since we haven't talked about the CMS yet.

**Andy Drukarev:** It's still something we're discussing internally, but we don't have one right now.

**Aida Knežević:** In terms of the type of content—we call it editorial. It requires more editing and drafting on our end. If we were doing purely programmatic content, we could do 30 pages per week because it's much more automated. But because these are more traditional articles and blog posts, we're limited. I'll try to do at least 10 per week. It takes drafting the outline, editing it, reviewing the content—just more of a lift.

**Andy Drukarev:** I don't think we need to get through all 25 CWEs. I think there's a world where we focus on the 4-5 most popular, most common, plus a few of the other ideas you had—like CWE versus CVE—and build a good pillar page. Given the overall search volume, the difference between five cluster articles and 25 isn't that much. I'd rather have us get through the first batch and then maybe consider other paths. But I'm also curious if there are some programmatic ideas that come to mind.

**Jakub Rudnik:** Thanks for setting that up, Aida. Andy, your perspective is really helpful. We're discussing this as one of those clusters with depth, and it feels good there. We want to make sure we're aligned on where we are, how much lift is left, and what's next. This is all part of the calibration process, especially with the migration and registry work. We do have these other clusters, whether they're truly programmatic or not.

**Andy Drukarev:** Once we get through those five, let's shift gears to PSEO experiments. In general, I'm much more optimistic about the possibility of AI for PSEO than long-form editorial, especially domains where there isn't great source material. We've had a lot of early success using AI to build different tools. That's super interesting to me. Let's get through the five in the next few days, and then let's talk early next week. I'd love if you could come to us with a few suggestions of PSEO options.

**Jakub Rudnik:** We'll send those over next week so we can discuss at this call. I'm focused on publishing that five-article batch.

**Aida Knežević:** I just need to get in touch with the freelancer about code reviews to make sure we can publish these knowing they're correct.

**Andy Drukarev:** Thanks.

**Jakub Rudnik:** Anything else? I want to get a status on the registry. Any updates on that end?

**Andy Drukarev:** Hopefully we'll be able to make some changes to those scripts next week. We're trying to get the site stable with the existing website, but yeah, we're working on it.

**Jakub Rudnik:** Just pull us in whenever and keep us in the loop. If there's anything on the stability front, whether that's me or I can throw it to a large team of experts—we have folks across the board who can help. Appreciate it.

**Andy Drukarev:** We'll look forward to getting the remaining articles in this CWE cluster by the end of next week. At some point early next week, we need to come to a conclusion on whether we'll do manual review or automated fact-checking. Ultimately, let's pick one by Tuesday and then during our Thursday call, you can share those PSEO ideas.

**Aida Knežević:** All right. Perfect.
