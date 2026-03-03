# Town/GrowthX Weekly Sync

<metadata>
date: 2025-08-13
time: 18:01 UTC
duration: 21 minutes
organizer: darrell@growthx.ai
participants: Ehtisham Hussain (GrowthX), Darrell Etherington (GrowthX), Pier (Town), Ryan Johnson (Town)
fathom_recording_id: 80384871
fathom_url: https://fathom.video/calls/378315678
share_url: https://fathom.video/share/UjCKzay9qYi9ph_pmzCaHw7fhpbhwUps
source: fathom
enriched_on: 2026-03-03 14:32 UTC
</metadata>

---

## Summary

Ehtisham and Darrell synced with Pier and Ryan from Town on content production velocity and SEO optimization. Town is building a 5-article submission buffer (5 submitted this week, 5 more coming tomorrow) with a goal of publishing backlog by Friday. The team addressed an H1 tag duplication issue affecting SEO and discussed possible design changes to hero image layouts. Darrell flagged two experimental SEO tactics worth exploring: a hidden blog optimized for GEO (with Q&A structure) and an LLM.txt file for AI visibility; he committed to syncing with Dave on implementation options and comparing approaches.

---

## Context

Town is a financial services software company focused on tax and accounting workflows. GrowthX is executing a content strategy that aims to drive SEO visibility and lead generation through consistent blog publishing. This was a weekly operational sync to review content submission progress, debug technical SEO issues, and evaluate emerging SEO tactics (GEO and LLM.txt). The 21-minute call reflected momentum in content production but also highlighted the team's cautious approach to experimental tactics—eager to try high-upside strategies but grounded in data-driven prioritization.

---

## Relevance

**To GrowthX Delivery:**
- Town is successfully ramping up content production (5 articles submitted weekly, aim for 5-article rolling buffer). This execution model is replicable for similar clients.
- H1/title tag duplication is a common technical SEO issue in CMS-based sites; Darrell and Pier's solution (text on image overlaid with H1 tag) is a pattern worth documenting.
- GEO (Generative Engine Optimization) for Q&A content and LLM.txt file generation are emerging tactics GrowthX should track across the client base for effectiveness signals.

**To CheckThat:**
- Town is exploring LLM.txt approach and hidden blogs to improve AI visibility. This is direct evidence of demand for AEO/generative visibility strategies in SMB financial software space.
- Darrell mentioned Anthropic's own LLM.txt deployment—worth monitoring for LLM crawl patterns and indexing behavior that could inform CheckThat research.

**To GrowthX Business Development:**
- Town is receptive to new content formats (tax scenario templates, top-app lists, gated downloadable assets) and exploring community-led growth—signals of strong account health and expansion potential.
- Pier flagged regulatory concerns about tax advice implications of downloadable assets. This is a common constraint in tax/finance verticals; understanding legal guardrails early strengthens future proposals.

---

## Overview

- 5 articles submitted for review; 5 more lined up for tomorrow to build a content buffer
- H1 tag duplication issue addressed; design tweaks discussed to improve UX and SEO
- Exploring GEO blog strategy and LLM.txt implementation for potential SEO benefits
- Considering new content types (e.g., tax scenario templates, top app lists) for future implementation

---

## Key Topics

### Content Production and Review

  - 5 articles submitted for review; issue with Ludmilla's access resolved
  - 5 more articles lined up for tomorrow, building a hedge for future content
  - Aim: Publish backlog by Friday, new set early next week
  - Goal: Maintain a 5-article buffer submitted every Tuesday

### Blog Design and SEO Optimization

  - Addressed H1 tag duplication issue; revised H1s to differ from titles
  - Discussed moving graphical elements up, integrating text into hero image
  - Debated HTML structure for title, H1, and image placement
  - Action: Pier to discuss with Tony about implementing design changes and H1 tag solution

### Analytics and SEO Progress

  - Some impressions registered in Bing, but too early for significant position improvements
  - Need to continue publishing consistently to see meaningful results

### GEO Blog Strategy

  - Discussed creating a "hidden" blog for GEO optimization
  - Content structure: H2s as common questions, paragraphs as bullet-point answers
  - Darrell to explore implementation with Dave, comparing to current LLM.txt approach
  - Potential to generate parallel GEO Q\&A content for each blog post

### Future Content Initiatives

  - Explored ideas from Ada: tax scenario templates, top app lists for SMBs
  - Darrell suggested prioritizing downloadable assets (potentially gated) for lead generation
  - Pier to consult legal team about form creation, especially regarding tax advice implications
  - Discussed possibility of community-led growth approach in the future

---

## Action Items

**Pier (Town)**
- Discuss with Tony about implementing H1 tag solution (remove duplicate H1, handle text overlay in graphics) and making graphic text customizable in CMS

**Darrell Etherington (GrowthX)**
- Sync with Dave on including Town in LLM.txt generation pipeline; share current approach and compare with hidden/shadow site strategy for GEO optimization

---

## Transcript

**Darrell Etherington:** Downloads install package at some intervals, even though it's already installed in my system, just in case you need another one.

**Pier:** I love that.

**Darrell Etherington:** Yeah, it's great.

**Pier:** Hey, Ryan.

**Ryan Johnson:** Thank you.

**Pier:** All right, I think we have quorum.

**Darrell Etherington:** All right, hi, Jean-Denis.

**Pier:** Hi, how are you?

**Pier:** I'm good, but busy, but it's a good place to be. Things are great. Let me pull up something on my side too. All right, let's do it.

**Ehtisham Hussain:** Yeah, I'll get started.

**Ehtisham Hussain:** So we submitted five more articles for review. There was a mix-up with Ludmilla not having access to them, but that's fixed. Plus I have five more lined up for tomorrow. This will help build up a hedge, and we'll be ahead. Hopefully we'll make up for the three days we didn't publish, and we'll have articles for the future as well.

**Pier:** So ideally, the existing five, we're going to try to do those as quickly as possible, hopefully by Friday. Then you have another five, which we'll get done by early next week—those are the ones that will be published next week. And then ideally, by every Tuesday, we have another five. So we're ahead and good for a while.

**Darrell Etherington:** Okay, cool.

**Ehtisham Hussain:** Yes, that's the plan.

**Pier:** All right, awesome.

**Ehtisham Hussain:** For the previously published blogs, we generated images in line with the new design. I addressed comments about the title and H1 repeating. As a short-term fix, I revised all the H1s so they're not verbatim the same as the title—they're a different take on it. Ideally, the title lives in the background in the page code for search engines, and the H1 is what's displayed at the top. Darrell has some design ideas, and I do too. It's not a shift in design. Let me quickly share what I was thinking.

**Pier:** Yeah, go for it.

**Ehtisham Hussain:** So here we have the title as HTML on the page, and then you have the H1. Ideally, we want just one. And you have pretty much the same text appearing in the image as well. I was thinking we move the graphical element up—the green part and logo—that can be the background. What if we make the text not part of the image and insert it manually over here, tagging it as the H1? This way we eliminate duplicate elements. We'll have a visual element in the hero area and the article starts right up. Right now I have to scroll to get to the article. So we move it up and remove the extra elements. That's one way to do it, but I know Darrell also has some ideas.

**Pier:** Can I ask you a question? I don't understand the title thing. Title is a head element, not a body element.

**Ehtisham Hussain:** Right, it's supposed to be in the head. Most blogs have the title in the background—if you view the page source, it's there and tells the search engine what the article is about. But the H1 is what's displayed on the page. Technically we can do that.

**Pier:** If you look at the HTML, they're both there in the head element. Looking at the page source, that top text "Fear the Compliance Guide for Real Fund"—if I inspect it, that's an H1 tag. So we have two H1 tags. We don't need two H1 tags.

**Darrell Etherington:** Yeah, that's right. We can just drop the first H1 if we're not sure why there are repeated ones.

**Pier:** I can ask our designer to figure out the HTML so we can insert an image and then write text on top of it. We'll give you cards from Figma that are empty with an H1 tag over the image. That's what you were suggesting, right?

**Darrell Etherington:** I think either solution works. The simpler approach is just dropping one H1 and having a static visual from Figma with a simplified broad category like "tax tips for real estate pros"—short, one or two words—and then the proper H1 that follows. Either way works. We agree we don't need two H1 tags.

**Pier:** I wish Tony were here. I'll talk to Tony after this and follow up with you on figuring out how to make it happen.

**Darrell Etherington:** You want to continue on the agenda?

**Ehtisham Hussain:** That's pretty much what I had.

**Pier:** Okay, great. How are we doing on analytics? Do you feel good about that progress?

**Darrell Etherington:** It's early for big conclusions, but go ahead, Ehtisham.

**Ehtisham Hussain:** We did see some impressions registered in Bing. We're not seeing any major improvement in position yet, but as Darrell said, it's too early.

**Pier:** OK, so we just need to keep publishing.

**Ryan Johnson:** All right.

**Pier:** I have a couple of things to talk about. One is about a GEO blog. We heard from a few companies doing this—they're creating hidden blogs blocked by robots.txt but included in the sitemap and LLM.txt. The H2s are questions people ask about tax or Town on ChatGPT, and the paragraphs are bullet-point answers. People say it's helping with GEO. We obviously don't have enough SEO visibility to be picked up yet, so maybe it's early. But I'd love your thoughts on it and what it would take to implement. Since we're building content anyway, we might generate parallel GEO Q&A for each blog post. I don't need an answer now, but I'd like to discuss it in the next few weeks. Second: I talked to Ada about other content beyond the blog—things like template forms for different tax scenarios, top app lists for SMBs where we list ourselves as a top-three tax app. I'd like to know which of those we'd want to implement by year-end so we can plan what we need to enable it.

**Darrell Etherington:** Sure, yeah. We do have work we're doing with the LLM.txt approach already with some other clients, and we can include you. It's very early. We're doing a version that takes the top content existing on your site and encapsulates it in a single file.

**Pier:** Yeah.

**Darrell Etherington:** It's formatted in markdown—the format LLMs want to read. It's like a user guide. All the LLM.txt stuff is very experimental, and I find the shadow site approach interesting too. I'm going to talk to Dave on our team about that. Generally, people are trying this because it seems like we should try it, but there's not comprehensive information yet about whether it's productive. Definitely worth trying.

**Pier:** The reason we heard the hidden blog works is because people are seeing those pages indexed by foundational apps. The thesis is that if you have bullet-point answers to questions that people are asking, that's what matters. That's why we're testing them—we want to see what results we get.

**Darrell Etherington:** That's right, and I think that's a good theory.

**Darrell Etherington:** We have the benefit of seeing across clients, so we have a better sample set of what's working or not.

**Pier:** Also, the stakes are lower for wrong information—humans aren't going to Google their way onto it. And since we're already generating the content, if it's within your automation capabilities, the cost is probably minimal.

**Darrell Etherington:** Right, we wouldn't have to review anything else. What we've been doing is directing to existing content or providing truncated summaries of top-performing content in one large text document, rather than recreating a shadow site structure. But I'm going to bring that back because it's worth trying. Especially when you're at the starting point like you are, it's easier to get a good sample than trying to regenerate thousands of pages in parallel. I'm very interested in this. I have academic interest in whether it's anything. LLMs do index everything—they're voracious, omnivorous monsters. But whether they make use of that is different. I can see them hitting it, but not how they use it. Anthropic put their own LLM.txt on their domain, which suggests they're thinking about how to ingest it. Definitely worth experimenting. I'll talk to Dave and get you into our generation pipeline that's supposed to do exactly this. We'll show you our current state and compare it to your shadow site idea, and we'll work that out.

**Darrell Etherington:** On the second point: Ada's right that all of those are useful, especially for engagement. The form idea is interesting for you because gated downloadable assets make sense for driving leads with your customer. That's probably the thing to address first. The question from your perspective is: how comfortable are we with these from a tax official standpoint? They wouldn't constitute tax advice, but they are actionable takeaways people might use. That's definitely your call. We'd want to make sure there are no flags around that. That's how I'd order these by efficacy. We could also explore community-led growth, which we do with various clients. We help stand up sites designed to build community around specific content or utility content adjacent to the brand. That's something we could explore if you're interested, but it's probably further out from a staging perspective.

**Pier:** That's interesting. I'd be interested eventually, but let me first look at the forms and talk to legal. Some forms are just templates for tracking, like a spreadsheet you fill out. Others calculate for you, which is more dangerous. Let me think about it and talk to counsel. Maybe we can get going on that in a month.

**Darrell Etherington:** Sounds good.

**Pier:** For next meeting, let's definitely talk about the GEO blog and LLM.txt stuff, depending on what you think. I'll follow up with Tony about the H1 tag issue and making the text in the graphic customizable in the CMS.

**Darrell Etherington:** I think the best solution is layering body text on the graphic, but the Figma option with a simplified one-to-two-word phrase works too.

**Pier:** We'll figure out how to do one of the two.

**Darrell Etherington:** Sounds good.

**Pier:** All right, thanks, guys. Take care.

**Pier:** Bye.
