# Aembit <> GrowthX Weekly Sync

<metadata>
date: 2025-06-18
time: 16:31 UTC
duration: 34 minutes
organizer: David Galic (GrowthX)
participants: Jakub Rudnik (GrowthX), David Galic (GrowthX), Dan Kaplan (Aembit)
fathom_recording_id: 69176323
fathom_url: https://fathom.video/calls/328432244
share_url: https://fathom.video/share/vEKXCPVG-csxp88q7CZsM2uyaF_oqegs
source: fathom
enriched_on: 2026-03-03 14:35 UTC
</metadata>

---

## Summary

GrowthX and Aembit discussed content quality improvements and publishing progress. Two articles have been published with two more (articles 3 and 5) pending final review. GrowthX shared refined workflows and artifacts to strengthen technical accuracy in depth articles, resulting in a 4,500-word SPIFFE piece and breadth articles on secret remediation and management. The team agreed to balance publishing higher-volume breadth content while perfecting deeper technical pieces, and Aembit committed to sharing Gartner reports and artifacts to inform ongoing content development.

---

## Context

Aembit is a security company working with GrowthX on a major content marketing engagement. This weekly sync is part of their ongoing collaboration to develop high-quality content around identity and access management (workload identity, non-human identity, SPIFFE, secrets management). Aembit has expressed concerns about technical accuracy in the content, particularly in deeper technical articles where LLM-generated content may lack specificity if source material is thin on the internet. GrowthX has responded by refining workflows and asking Aembit to contribute original artifacts (one-pagers, internal research, Gartner reports) to serve as authoritative source material for content generation.

---

## Relevance

**To GrowthX Delivery:**
- Workflow improvements using client artifacts as source-of-truth documents significantly improve content depth and accuracy. Original artifacts (Asher's one-pager on SPIFFE) elevated article quality from mediocre to strong.
- Content strategy shift: balance "depth" (4,500+ word technical articles with code) and "breadth" (2,000 word overview/definition articles). Breadth articles are faster to fact-check and publish while depth articles are refined.
- Identified workflow issue: forced inclusion of client-specific conversion content sometimes convolutes technical accuracy. Focus on clear topic boundaries first.

**To GrowthX Business Development:**
- Account health: Aembit is actively engaged and providing feedback. Two articles published, four in progress. Account producing consistent output.
- Expansion signal: Aembit considering updating/merging existing pillar content (Non-Human Identity guide) instead of creating new content to avoid cannibalization. Strategic planning underway.
- Reference potential: SPIFFE article resonating with Aembit's market. Gartner and industry analyst coverage indicate strong SEO/visibility opportunity.

**To CheckThat:**
- Content refresh patterns: Older content (8-10+ months) needs regular updates to maintain relevance for LLM scraping and search rankings. Dashboard tracking GSC performance to measure impact.

---

## Overview

- Two articles published, two more close to publication after final review
- New workflow improvements implemented, resulting in higher quality content
- Focus on balancing "depth" (technical) and "breadth" (overview) articles
- Leveraging industry sources (e.g., Gartner reports, LinkedIn posts) to inform content strategy

---

## Key Topics

### Content Quality Improvements

  - Issues with technical accuracy in "depth" articles addressed through:
      - Using specific artifacts/documents from Aembit as source material
      - Updating workflows to improve content generation
      - Avoiding forced inclusion of Aembit-specific content where not relevant

### Content Strategy

  - Balancing "depth" (technical, 4,500+ words) and "breadth" (overview, \~2,000 words) articles
  - Considering updating/merging existing pillar content instead of creating new, potentially cannibalizing articles
  - Expanding into adjacent topics (e.g., secrets management, identity federation) to attract relevant audience

### New Content Creation

  - Six new articles created, including a 4,500-word piece on SPIFFE
  - Two "breadth" articles on secret remediation and management best practices
  - Potential update/merge of existing "Guide to Non-Human Identity" content

### Industry Resources

  - Leveraging Gartner reports and former analyst's upcoming content series
  - Mining LinkedIn posts, podcasts, and other industry discussions for topic ideas and unique perspectives
  - Exploring Google Scholar for relevant academic research to inform content

### SEO and Performance

  - Need to regularly update older content (8-10+ months) to maintain relevance for LLMs and search engines
  - Creating a dashboard to track published content performance using Google Search Console data

---

## Action Items

**Dan Kaplan (Aembit)**
- Review articles 3 and 5 for final approval before publishing
- Review new SPIFFE article (4,500 words) and compare with existing Aembit SPIFFE content
- Review 2 new breadth articles on secret remediation and secret management best practices
- Send Gartner reports and internal artifacts to GrowthX team

**Jakub Rudnik (GrowthX)**
- Create dashboard for Aembit with published content links and Google Search Console access data for performance tracking

---

## Transcript

**Jakub Rudnik:** So just a lot of experimenting and getting up to speed, training, all that stuff. I mean, I think we were already seeing some things that are really good. Now it's just like ironing bugs and figuring out best practices and all that stuff that just takes time.

**Dan Kaplan:** That's awesome.

**Dan Kaplan:** So, yeah, I was away. I got back yesterday. So kind of catching up on some other things, including this, including progress here. I feel a little bit behind. I think Asher's out today. Anyway, so catch me up to date. I know we published a couple of things.

**Jakub Rudnik:** Well, that's what we're here for, to get you up to speed.

**Jakub Rudnik:** Yeah, I think where we left off last week was certainly kind of level setting on the technical depth and accuracy. By the way, I wasn't on last week's meeting. I was in England, so my life has been a blur for the last week. So, yeah, so we talked about issues we've had with some of the technical accuracy on some of the articles. We kind of broke those into two categories.

**Jakub Rudnik:** I don't think it's a perfect clean split, but in general, we've started using this term like the depth articles versus the breadth stuff. Depth articles are hyper-specific and narrow. That's where we've seen issues. When there's little specific information available on the internet, LLMs pull from mediocre content and we get mediocre output. One other issue is that often we're trying to force Aembit into the content for conversion purposes, but that creates accuracy issues. We're convoluting ideas and blurring lines that need to be more clearly defined. I want to push our team and workflows to get to that point, but I know your team's worry from the get-go was how much can truly be automated versus where expertise needs to be involved.

The breadth articles are more up-funnel — glossary level or definition posts. There's more accurate information online for those. The question is whether we scale those in the meantime as we iron out the depth articles. Maybe we do a little bit of both sides, iron on one side while seeing how far we can get on the other. For SPIFFE articles, that's 4,500 words with code and technical detail. Or in the meantime, can we publish more 2,000-word, higher-funnel, definition-based pieces that are easier to fact-check and automate?

So that was a lot of the conversation last week. We went back to our team — Panzer and another director, Daryl, who hadn't taken on clients yet. We're really focused on improving quality and figuring out workflows. They had more bandwidth than me, and we've also done some arrangements so me and David have more bandwidth. They jumped in to look at how we can use our workflows and artifacts from your side to improve. Some articles came out of that seem deeper or more accurate. I've highlighted those.

**Dan Kaplan:** What was shared last week that helped strengthen the workflow so dramatically? I saw Asher shared something on SPIFFE, right?

**Jakub Rudnik:** That PDF, that one-pager — there are gaps in what's available on the internet. Your specific, detailed nuance on a topic, whether it's original research or an internal one-pager, helps us inform an article. That's the original source material. Anywhere we have that across all clients, but particularly for technical content, everything just becomes better because our workflows point to those documents as the source of truth instead of something written by a content writer four years ago.

**Dan Kaplan:** Would that only inform SPIFFE-related content, or could what Asher shared benefit across the board?

**Jakub Rudnik:** That one was SPIFFE-specific, though I think there are pieces of Aembit in there. We can build a cluster on that and there might be details we can take elsewhere. If you had 100 one-pagers like that, we could go do those. But anything with that type of authority or detail, we can build a backlog of trusted documents and research. I was talking to the team earlier today — we should be looking through Google Scholar for similar things, not just Aembit-specific. Can we find documents that aren't getting scraped the same way but have that level of authority and depth? If we had more one-pagers like that, we could find clusters and not just do one article, but make one artifact into 10 articles. That type of document becomes a few articles and informs the larger content strategy.

**Jakub Rudnik:** So yeah, we have two articles published. There are two more articles, articles 3 and 5, that seem very close — just pending final review from the updates David made on those.

**David Galic:** I made clean versions for both of these. Articles 3 and 5 are good. The fourth one was the one that wasn't working and needed a lot of work, so we put that on the back burner. That's the Workload Access article.

**Dan Kaplan:** Okay, so three and five have been reviewed. We're close.

**Jakub Rudnik:** So once you get the okay, you'll publish those and continue the publishing?

**David Galic:** Correct. Yep.

**Jakub Rudnik:** And then there are four new articles that have been created. Article 6 is based on what Asher shared plus updates to the workflows from Daryl. I feel confident in this, with as much as I can be with some technical nuances. There's a lot of improvement on this article.

**Dan Kaplan:** This is 4,500 words. This is depth with custom code and things. Even with all the improvements, my expectation is this will take some time. But I think it's important — we've seen traction around that topic. Has anyone looked at it yet?

**Jakub Rudnik:** I didn't see any comments. This is us stress testing it for your use case. We really need to figure out if we can do these things technically if we have the right information on the back end. It's a good test case and will tell us what comes out of this. Your team's eyes on this one will be really important.

**Dan Kaplan:** The Guide to Non-Human Identity — was that one we had in the pipeline?

**David Galic:** No, I think it's just one that Daryl did based on topics for you. It came together after Daryl got involved. It looked more like a breadth topic.

**Jakub Rudnik:** So we wanted to give him one he could do off to the side as we expand your content footprint, but maybe slightly off. With the updates to the workflow, it seemed improved. It was off to the side but wanted to see what that would look like if we're expanding topics a little bit to be more up-funnel.

**Dan Kaplan:** I view this as a pillar piece — the all-encompassing guide to our discipline and domain. We've created a couple of these blog posts that do above average in terms of traffic. We actually built a 101 webinar off of one of them. I'm sure both of these could live together. It's not either-or. You could have multiple, more in-depth pieces around the general topic.

**Jakub Rudnik:** Yeah, it could cannibalize. So it's a good call. I wouldn't imagine we'd want both unless one has a slightly different angle and keyword coverage. If anything, it'd be updating and merging the two. So I put that in next steps — don't take that as the next step. We need to look at it before we go forward.

**Dan Kaplan:** The most recent article you shared is really good context. There's no competition, but there is traffic. I know that when I search "workload IAM," that article performs well. I think it's good we created it because Gartner, the major advisory firm, homes in on the workload identity and workload IAM term versus non-human IAM. If Gartner's leaning toward workload, it could increase visibility. So maybe it's good we have this, even if it's not NHI numbers. I'm glad we made the effort to create that larger piece because those are good to have.

**Jakub Rudnik:** On the workload article you sent, clicks have dropped even though impressions are growing. July 2023 is the published date. We should refresh that because LLMs aren't looking at content over 8 to 10 months old anymore. But if Gartner's talking about this and there were clicks in the past, refreshing, adding content, and changing the published date could be valuable and pick back up a lot of exposure. If we can find anything Gartner's written or reports, we can pull keywords, get topic ideas. There's a lot we can do with that.

**Dan Kaplan:** I can share the Gartner downloads with you. We have a couple of recent ones I can collect from Apurva. Also, there's a former Gartner analyst who's now independent — ran their identity and access management division. Today on LinkedIn he announced he's going to write an article a week on our space. He detests the NHI term but understands the marketing muscle behind it. I think funneling that content will be good as well.

**Jakub Rudnik:** This person sounds perfect. We can embed LinkedIn posts and it helps with time on page and authority with LLMs. I'm glad you're thinking that way. If there are others that come to mind, let us know.

**Dan Kaplan:** Yeah, when someone comes into a topic with a cynical approach, they breathe fresh air into it. It might funnel into our copy and make our stuff more relatable. I'll get you the Gartner stuff and put this analyst on your radar so you can watch for when he starts posting. He has a fairly big following.

**Dan Kaplan:** Thank you for sharing. This is helpful.

**Jakub Rudnik:** So the Non-Human Identity article — we need to pause and take another step. We should double check the intent and if it's worth having two SPIFFE articles. This might be a merge situation because the new one has a lot more depth. And also, the older SPIFFE article is from 2023 — everything needs to be updated much more regularly than it used to be. So we'll review this deeper piece and we can make that call.

**Dan Kaplan:** It might be worth publishing them in tandem, especially as SPIFFE comes up a lot for us and there are developments happening.

**Jakub Rudnik:** Yeah, really just an SEO look on our end at the intent and if they'll cannibalize. We can make that call pretty quickly. Even a LinkedIn post could be something to embed at the right spot and be a conversion driver. Just throw anything you see our way — drop it in Slack. Just grab the link, send it, don't think about it again.

**Jakub Rudnik:** There are two other articles — Guide to Secret Remediation Best Practices and Best Practices for Secret Management. These are breadth articles, slightly expanding what we've done. These are V1, David took a crack at those.

**David Galic:** Since you weren't at the last meeting, Apurva was talking about how if there's not a lot of stuff about what you're doing on the internet, there's a lot of adjacent content we can mine for good ideas. People who read that will be interested in what you do. The first topics that came to mind were secrets management — there's good content out there, especially from HashiCorp — and identity federation. We want to build articles that are well-written, well-informed, and in that ballpark but not specifically about Aembit. This is how we publish a lot and produce more content while calibrating the deeper technical stuff. We're not waiting — we're actually publishing and getting traffic.

**Dan Kaplan:** That makes total sense and aligns with our plan. I think we've done some of that, but maybe it wasn't calibrated well enough. Hopefully these will let us achieve that.

**Jakub Rudnik:** So we've got the two quick articles that are close — three and five. The SPIFFE article with a lot of depth might be the last one to go after this week. We'll compare that to what you have. The two new articles are shorter and hopefully less technical, so we can review and get publishing guidance.

**Jakub Rudnik:** The asks are: send over the Gartner reports and artifacts if you have them. For us, we'll create a dashboard with the published links and your GSC access so we can track progress. Using tools like Perplexity to surface Gartner reports and Google Scholar to find authoritative sources like academic analysis will help us mine content for topic ideas and quotes.

**Dan Kaplan:** Noted. I'll collect the Gartner stuff and get it to you. And I'll make sure you're on the radar for when that analyst starts posting.
