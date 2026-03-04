# Runpod <> GrowthX Weekly Sync

<metadata>
date: 2025-04-15
time: 17:01 UTC
duration: 36 minutes
organizer: sydney@growthx.ai
participants: Sydney Go (GrowthX), Jason Gong (GrowthX), Emmett Fear (RunPod)
fathom_recording_id: 57419704
fathom_url: https://fathom.video/calls/276776763
share_url: https://fathom.video/share/yPS8Y-JMhoqJFd4SP6yZHRyE6QayMfnk
source: fathom
enriched_on: 2026-03-04 17:50 UTC
</metadata>

---

## Summary

RunPod and GrowthX aligned on content production momentum—4 new articles generated this week with 11-16 more ideas needed to hit the 20-article goal. The team clarified GPU offerings (pods vs. serverless GPU) and finalized a programmatic approach to GPU-specific pages that includes benefits, specs, pricing, and FAQs for each card type, which Emmett and Jason will coordinate delivery format for. Most critically, RunPod's AI SEO revenue attribution jumped from 3% to 10% through targeted optimization, and the team is now testing Profound and Scrunch tools to optimize for AI-generated citations—targeting 15-20% citation rates by building out programmatic content around specific use cases (PyTorch, Stable Diffusion, ComfyUI).

---

## Context

RunPod is a cloud GPU rental and serverless GPU platform competing against Lambda Labs and Paperspace. GrowthX has been engaged in an ongoing content and SEO optimization engagement focused on ranking RunPod for technical GPU-related queries and maximizing AI engine citations. This weekly sync is a standing check-in between Sydney (GrowthX content lead), Jason (GrowthX engineering/programmatic SEO), and Emmett (RunPod growth engineering) to align on content production, track SEO performance, and test new AI visibility tools.

The partnership represents a significant strategic bet for GrowthX: the AI SEO revenue opportunity is compounding (3% to 10% attribution in a few weeks), and RunPod is aggressively pushing bare metal instant cluster offerings while simultaneously optimizing for AI-generated citation visibility—both areas where programmatic content and technical SEO directly impact revenue.

---

## Relevance

### To GrowthX Delivery
- **Programmatic SEO at scale**: The GPU page template (benefits, specs, pricing, FAQ) is replicable across 80+ SKUs in the backlog—significant leverage for future engagements.
- **Content production velocity**: 4 articles/week with 20-article weekly goal confirms GrowthX can sustain high-volume generation; content is shipping and indexing.
- **URL structure and SEO architecture**: Implementation of category-based URL hierarchy (articles/category/article-name) affects indexing and link-building strategy going forward.

### To CheckThat
- **AI visibility as revenue driver**: RunPod's 3%-to-10% AI SEO attribution in weeks validates CheckThat's core thesis. This is now a measurable client outcome worth studying.
- **Citation optimization tactics**: Profound and Scrunch are proving tools for finding citation gaps. Target of 15-20% citations shows market is moving beyond top-of-funnel ranking into direct attribution.
- **Persona-based prompts**: Scrunch's ability to test custom personas and specific questions (e.g., "best cloud GPU for PyTorch") aligns with CheckThat's positioning around high-intent AI queries.

### To GrowthX Business Development
- **Reference-worthy metrics**: 3x growth in AI SEO revenue attribution is a strong case study for pitching AI visibility services to other B2B SaaS clients.
- **Bare metal push alignment**: RunPod's high-priority initiative (bare metal instant cluster) is creating urgency for content. This signals account expansion opportunity if GrowthX can own the "bare metal GPU" content vertical.
- **Tool partnership leverage**: Access to Scrunch and Profound dashboards creates ongoing engagement and insight-sharing opportunities with RunPod team.

---

## Overview

- Content production is back on track with 4 new articles generated this week
- RunPod is implementing article categorization and URL structure changes
- GrowthX is developing a programmatic approach for GPU-specific content pages
- RunPod is seeing success in AI SEO efforts, with revenue attribution increasing from 3% to 10%
- The team is exploring AI tools (Profound, Scrunch) to optimize content for AI-generated responses

---

## Key Topics

### Content Production and Strategy

  - 4 new articles generated this week, awaiting editing
  - Need 11-16 more content ideas approved for the coming week
  - Implementing article categorization (e.g., articles/category/article-name)
  - Exploring programmatic content generation for GPU-specific pages
  - Focus on creating content around popular use cases: PyTorch, Stable Diffusion, Comfy UI

### SEO Performance and Tracking

  - First published article showing positive signals: 1.57% CTR, 5.94 average position
  - New Looker Studio Dashboard created for tracking article performance
  - RunPod x GrowthX performance tab added for weekly updates
  - Overall article dashboard shows keyword rankings and top queries

### AI SEO Optimization

  - RunPod's AI SEO revenue attribution increased from 3% to 10%
  - Using tools like Profound and Scrunch to optimize for AI-generated responses
  - Focus on ranking for more technical, niche questions (e.g., "best cloud GPU provider for PyTorch")
  - Exploring ways to increase citation rates in AI-generated responses (target: 15-20%)

### Bare Metal and Serverless GPU Offerings

  - Major push for bare metal instant cluster offerings
  - Clarification on differences between GPU pods (on-demand) and serverless GPUs (flexible, managed scaling)

### AI Optimization Tools

  - Profound: Provides insights but has limitations in prompt variety and contract terms
  - Scrunch: More flexible, allows custom prompts and persona creation, offers content optimization suggestions

---

## Action Items

**Emmett Fear (RunPod)**
- Review/feedback on GPU pods + serverless pods articles—clarify differences between offerings
- Approve 11-16 more content ideas for next week's articles (targeting 20 total)
- Provide static pricing info for GPU rental pages
- Review shared GPU rental page format, provide feedback
- Provide info on top frameworks/use cases for RunPod beyond PyTorch, Stable Diffusion, ComfyUI
- Change Scrunch password and share access with Jason Gong and Sydney Go

**Jason Gong (GrowthX)**
- Start Slack thread to align on best format for delivering GPU rental page content (JSON, CSV, Google Sheet, etc.)

---

## Transcript

**Jason Gong:** I just wanted to show some of the progress on the programmatic content generation that we're doing, but maybe we can go through the editorial first.

**Sydney Go:** Give me five seconds, I'm losing windows here.

**Emmett Fear:** You mentioned you work late hours, right? I'm currently in the Philippines.

**Sydney Go:** Okay, so I'm happy to report we're back on track with content. This week we've already got our first four articles generated—they just need to be edited.

**Emmett Fear:** Fantastic.

**Sydney Go:** I sent these articles over and I did notice you've published some articles already. I'll get to those. But I wanted to ask about GPU pods vs. serverless pods. The difference is GPU pods are persistent, right?

**Emmett Fear:** Yeah, so serverless GPU is persistent and GPU pods are on-demand. Let me clarify: serverless works by being flexible—depending on your workload, it can increase or decrease automatically.

**Emmett Fear:** With serverless, we control the DevOps side—we increase or decrease automatically. With normal pods, you spin one up or multiple pods, and you're the one responsible for tearing them down. It's not going to automatically adjust the amounts for you.

**Emmett Fear:** Okay, that makes sense.

**Sydney Go:** It does make sense, but I'll be the first to tell you I'm not an expert in this.

**Jason Gong:** So, so, especially, like, like, serverless, like, like, Lambda is right, like, from a BS and then the pods, like, does everyone use that terminology?

**Jason Gong:** So how does this terminology position the product for other people?

**Emmett Fear:** Other providers just call it GPU Cloud. The assumption is you manage it yourself. That's how the industry works.

**Sydney Go:** So I asked for clarification, and also these articles are very similar—the language is very similar too. I tried my best to differentiate them, but could you review and give me feedback on which ones are for serverless vs. GPU pods? That would be very helpful.

**Emmett Fear:** I'll double check on the GPU pod and serverless GPU articles and provide feedback.

**Sydney Go:** Thanks. So the articles I've generated this week are these four: "How to Use Serverless GPUs for Real-Time Inference," "API Hosted," and "Generative AI." I changed some of the wording so it doesn't sound as awkward. I tried to vary the titles so they don't look spammy. For this week, we need about 11 to 16 more ideas.

**Sydney Go:** One of the examples in the Content OS is the GPU rental ones. Jason, do you want to talk about that, or should I talk about it last?

**Jason Gong:** Let me show you the programmatic approach we're building. So far we have the standard article bucket—just going through AirTable and picking ideas. But this is the first programmatic bucket we're creating. I'm working on GPU-specific pages with benefits, specs, pricing, and FAQs. Right now it's in nested JSON format with all the individual fields. Would you prefer it as a table, JSON, CSV, or Google Sheet? That would be helpful to know before I generate the full set.

**Jason Gong:** So this A100 page has a much more relevant header with specific benefits of using the A100, the detailed specs, and a FAQ section. Right now the existing pages are mostly boilerplate—having these sections is what will help you rank. The pricing is mostly static, right?

**Emmett Fear:** Yes, I can get you those numbers.

**Jason Gong:** Great. We can keep it static for now. We can start a Slack thread to align on the best format—JSON, CSV, or Google Sheet—since you're loading this into your headless CMS.

**Emmett Fear:** Got it. First impressions on what you've shown me so far—I think it looks great.

**Jason Gong:** I'll send you a link to review. Are there any tweaks we should make? We have about 80 pages in the backlog, so once we settle on format, we can go to town.

**Emmett Fear:** I definitely think we can pursue these moving forward. It makes sense. I'd love it if you included this link in the Slack thread so we can figure out how to deliver it to the website.

**Jason Gong:** How is your team structured?

**Emmett Fear:** We have a full engineering team that works with product, and on my side we have growth engineering with three engineers. I'm the one spinning up the article work. We're releasing categorization today so the URL will be articles/category/article-name. I submitted the PR and we're updating all the URLs and indexing them today.

**Emmett Fear:** I also wanted to share the list of existing GPU rental articles we've already spun up. I want to make sure you have the full list. We should add FAQs to all these existing articles. Adding a FAQ section at the bottom would make sense.

**Jason Gong:** What if we merge the two approaches—the programmatic pages with the existing articles?

**Emmett Fear:** Merging them makes sense. I talked to one of my engineers about this.

**Emmett Fear:** We could create a template and set it up as a table in Supabase, then just drop content into different sections that populate on the page.

**Jason Gong:** If that's where you want the data, we can send it there. I like the PyTorch section approach. We can add columns for all the other data.

**Emmett Fear:** Right now, for Sydney's articles, I'm exporting them to markdown and pasting the content in—it populates as she built it in Google Docs. With these GPU pages, there's more nuance with tables and images, so we'll have to experiment with the layout.

**Jason Gong:** So on your end, let me know what format works—before I generate all 80, I want to know the best delivery method.

**Emmett Fear:** That totally makes sense. Once we agree on format, we can start generating.

**Jason Gong:** Hopefully we can get some done this week.

**Emmett Fear:** All right, Sydney, let's hear from you.

**Sydney Go:** Thanks. I added some competitor comparison ideas to the Content OS—Lambda Labs, Paperspace, and others we don't have content for yet. I also added editorial ideas based on articles I wanted to link to but didn't find. My only ask this week is to approve 11-16 more ideas so we can hit 20 total articles this week.

**Sydney Go:** For publishing, we have two articles live but one isn't indexed yet. I checked Google Search Console—should I request indexing?

**Emmett Fear:** Yes, please do. The URLs are about to change today due to categorization, so they'll be articles/category/article-name. That's why I haven't indexed yet—I'll set up the redirects.

**Jason Gong:** Is the folder structure already set up, or are you building redirects too?

**Emmett Fear:** We'll set up redirects.

**Sydney Go:** Great. So we're seeing good signals on the first article—1.57% CTR, 5.94 average position. I've built your Looker Studio Dashboard.

**Sydney Go:** This is your article performance dashboard showing overall views, clicks, and CTR. Conversions are ready to add once we define what metrics you want. I've set it to update daily. We're also tracking the RunPod x GrowthX performance tab—I update that weekly. Currently we have 292 impressions, 4 clicks, 1.37% CTR on the recently indexed article. That's strong signals. The bare metal article had some page views and indexing issues, but overall these dashboards will update daily. I'll add monthly and quarterly views later. The main RunPod dashboard shows all articles with keyword rankings and average positions.

**Emmett Fear:** That's good.

**Sydney Go:** I'll share that link in a more visible channel. That's it from me.

**Jason Gong:** So the main thing is we need you to approve 11-16 more content ideas. And for the GPU rental content, we need your input.

**Sydney Go:** I think I should add that to a different use case cluster. I'll change the description.

**Emmett Fear:** Stable Diffusion, PyTorch, and ComfyUI are the top three frameworks people use with RunPod. Those should definitely be leverage points for content.


**Jason Gong:** Can you give us more frameworks beyond those top three?

**Emmett Fear:** Totally. PyTorch is extremely popular. We also have Stable Diffusion, ComfyUI being heavily used. Those are the Docker containers most frequently deployed, so we should definitely build content around them.

**Jason Gong:** Great. We could knock out articles on those. We have a good backlog, though I'd like to explore the use-case specific GPU pages cluster more. If we generate those now and they ingest your platform docs, we could show how to run different frameworks on RunPod cohesively.

**Sydney Go:** We have a cluster for use-case specific GPU pages already. The approach is to do GPU rental articles first, then move to the next cluster.

**Jason Gong:** I'd like to test the quality if we generate those now. It would be helpful to see how well the content works when we reference your actual platform documentation.

**Jason Gong:** That's it on my side. Keep us updated.

**Jason Gong:** So what are your top company initiatives right now? What are your main pain points?

**Emmett Fear:** Bare metal instant cluster offerings have been a huge push—that's why I asked for those articles immediately. We have competitors doing the same, so we need content. And we're optimizing for AI SEO as hard as we can. It's working really well. AI SEO started at 3% of revenue and now it's at 10%—almost 3x growth. Programmatic SEO and AI SEO are closely intertwined. We've started ranking high for general terms like "top GPU provider" or "top serverless GPU provider," and we show up in most AI-generated responses. Now we're targeting more technical questions like "best cloud GPU provider for PyTorch" or "best cloud GPU provider for Stable Diffusion." Those are the niche queries where we want to appear.

**Jason Gong:** That's interesting because we've been looking at AI citation optimization. For SEO, you want L1 mentions, but no one has really gone deep into vendor attribution. That's where the value is.

**Emmett Fear:** Let me show you two tools we're using. This is Profound. They start at $3k/month and want a year-long contract, but we got a trial period. The pricing is steep for the volume of prompts we need. We gave them six high-level topic areas, and they generated prompts from those. But we've pivoted to Scrunch. Scrunch lets you create custom prompts for $500/month with no contract—you get 300 prompts per month. I'm testing edge cases to find what ranks. The key difference is Scrunch shows lower numbers, which I think is more realistic than Profound. We're not getting mentioned as much as Profound claims. Scrunch helps you figure out where to optimize. Our top serverless GPU article shows up 3% of the time. We want 15-20% citations—that comes from strong programmatic SEO presence. For price point, Scrunch is easier to start with.

**Jason Gong:** With the 33k number I saw, does that mean you're tracking 33,000 different permutations? How many permutations do you actually need?

**Emmett Fear:** Those aren't 33k different prompts. For ChatGPT specifically, they only run six prompts 10 times a day. So you're getting data from six prompts, run 10 times daily. That changes maybe once a month, not weekly. You see fluctuations, but some of that's just noise from running it too many times. The nice thing about Scrunch is you can spin up personas—optimize for different customer types.

**Jason Gong:** Would you be comfortable letting us poke around in Scrunch and help optimize it? We could feed data back into what we're generating.

**Emmett Fear:** That works. The Scrunch account currently has two users. I can change the password and give you access. I'd love any optimization insights you can add. One cool feature is the Optimize tool. If you input a URL, it shows how the crawler treats that page and what content optimizations would help. It's like a sandbox where you can test changes against real AI crawler behavior.

**Emmett Fear:** And so as you can see like search perform website found and then website considered no.

**Emmett Fear:** There are specific things the article needs to change. We're new to Scrunch—only used it a week—but you can plug in any URL and test changes to see if ChatGPT would consider it. That tells you if it's optimized for AI as well as traditional SEO.

**Jason Gong:** This is interesting. We're thinking about building something similar, but honestly, we'd just use Profound. Either way, if you could let us poke around in Scrunch, that would be great.

**Emmett Fear:** Happy to do that. I'll get you credentials this week.

**Sydney Go:** I think that's it from me.

**Emmett Fear:** Thanks everyone. Appreciate your time.
