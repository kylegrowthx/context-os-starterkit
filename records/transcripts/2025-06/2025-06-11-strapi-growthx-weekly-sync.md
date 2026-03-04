# Strapi<>GrowthX Weekly Sync

<metadata>
date: 2025-06-11
time: 16:30 UTC
duration: 31 minutes
organizer: Jason Gong (GrowthX)
participants: Jason Gong (GrowthX), Sydney Go (GrowthX), Usman Ghani (GrowthX), Victor Coisne (Strapi), Paul BRATSLAVSKY (Strapi), Theodore ONYEJIAKU (Strapi)
fathom_recording_id: 67809285
fathom_url: https://fathom.video/calls/322534809
share_url: https://fathom.video/share/tBjTG9XQccLxUN4xXkkofFi58dWmzX1N
source: fathom
enriched_on: 2025-06-12 14:30 UTC
</metadata>

---

## Summary

Strapi and GrowthX aligned on content performance trends and AI optimization strategy. GrowthX reported continued upward momentum with listicles and comparison content performing best; they've loaded 9 articles into Strapi's CMS (with 10 more in the pipeline) and are prioritizing "how to build" use case articles. The team discussed prompt tracking across Perplexity, ChatGPT, and AI overviews (~300 prompts loaded), identifying freshness, structure, and authority as key ranking factors. Key action items include setting up API keys for Medium and Strapi CMS, reviewing use case articles, building a brand guideline scanner to flag outdated product references, and exploring new content areas: Vite coding, Generative Engine Optimization (GEO), and programmatic SEO.

---

## Context

Strapi is a headless CMS platform that powers content management and delivery for enterprise customers. This is a weekly sync between Strapi's product and content team and GrowthX's content marketing team, part of a broader engagement to optimize Strapi's content for both traditional search and AI-powered search engines. The relationship centers on content performance measurement, SEO strategy, and exploring emerging opportunities like AI optimization and programmatic SEO. Strapi has a large content library (1500+ blog posts) spanning multiple product versions, which creates both opportunity and complexity for optimization — balancing fresh, authoritative content with legacy version documentation.

---

## Relevance

**To GrowthX Delivery:**
- Listicles and comparison content are driving AI citation performance — GrowthX should template and systematize this content format for future clients exploring AI optimization
- Prompt tracking across ChatGPT, Perplexity, and AI Overviews provides measurable signals for content strategy — this could become a standard reporting/optimization metric for GrowthX services
- Authority and freshness signals (updated_at fields, source citations, product version accuracy) are critical for AI ranking — GrowthX should audit and update legacy content systematically

**To CheckThat:**
- Strapi's challenge with AI understanding their product mentions across 1500+ articles (spanning multiple versions) is a use case for CheckThat's brand consistency auditing — a "brand guideline scanner" would flag outdated product references automatically
- Prompt tracking reveals that Reddit threads and discussion forums are frequently cited in AI responses — understanding where Strapi appears in these sources could inform content repurposing strategy

**To GrowthX Business Development:**
- Strapi is actively exploring thought leadership in GEO, Vite coding, and programmatic SEO — this signals growth appetite and budget availability for expanded content services
- Expansion of Kappa AI (Strapi's custom LLM) beyond documentation to support general user questions on the site indicates product evolution and potential for deeper content partnerships

---

## Overview

- Content performance trending upward with listicles and comparison content as top performers across both traditional search and AI-powered search
- ~300 prompts tracked across Perplexity, ChatGPT, and AI Overviews; listicles and content from competitors like HighGraph are frequently cited
- Freshness (updated_at fields), structure (well-organized content), and authority (expert citations) identified as key factors for AI rankings
- Building a brand guideline scanner to flag outdated Strapi product references in legacy articles across 1500+ blog posts
- Exploring GEO (Generative Engine Optimization), Vite coding optimization, and programmatic SEO as new thought leadership topics
- Considering expansion of Kappa AI beyond documentation to general user Q&A on website

---

## Key Topics

### Content Performance Update

  - Upward trend in content performance continues
  - Top-performing content: listicles (e.g., "Top 10 websites", "Best data security tools")
  - Refreshed integration pages showing early signs of improvement
  - 9 articles from last week loaded into CMS; 10 more planned for this week
  - Adding "how to build" use case articles; prioritizing based on goals

### Prompt Tracking and AI Optimization

  - \~300 prompts loaded across Perplexity, ChatGPT, and AI overviews
  - Listicles and comparison content frequently cited in AI responses
  - Freshness, structure, and authority identified as key factors for AI optimization
  - Potential need to update legacy content mentioning outdated Strapi features
  - Exploring creation of a "brand guideline scanner" to identify misaligned content

### Content Strategy and Thought Leadership

  - Vite coding and GEO (Generative Engine Optimization) identified as potential thought leadership topics
  - Opportunity to compare traditional SEO, headless CMS, and Vite coding approaches
  - Considering creation of content on building websites optimized for AI/LLMs
  - Exploring programmatic SEO as a potential topic, leveraging Strapi's CMS capabilities

### AI-Powered User Assistance

  - Discussion on expanding Kappa AI (Strapi's custom LLM) beyond documentation
  - Potential for creating a more general-purpose bot for answering user questions
  - Exploring integration of AI-powered FAQs or context-aware search within content

---

## Action Items

**Paul BRATSLAVSKY (Strapi)**
- Review list of use case articles from Sydney Go, confirm if they fit Strapi's use case and justify investment in content without clear search traffic

**Theodore ONYEJIAKU (Strapi)**
- Set up and share API keys for Medium and Strapi CMS next week

**Victor Coisne (Strapi)**
- Collaborate with Nuclas on product marketing prompts for Strapi functionality and cost research
- Draft internal piece comparing traditional SEO, headless CMS SEO, and Vite coding approaches for GEO

**Jason Gong (GrowthX)**
- Ingest user stories from Strapi website and G2 reviews as source material for content creation to establish authority

---

## Transcript

**Jason Gong:** Hey Paul, how's it going?

**Sydney Go:** Hi Theo, how are you?

**Paul BRATSLAVSKY:** Yeah, just bright out today. Too bright, if you ask me.

**Jason Gong:** I think you might be muted. We're still waiting for Victor, but we can start.

**Paul BRATSLAVSKY:** I have some stuff to show on prompt tracking. I'll leave that to the end since Victor will be excited about that part.

**Jason Gong:** Sounds good. Sydney, can you do the content update first?

**Sydney Go:** So content performance-wise, we're still on the upward trend. What we're working on now is looking at your content to see what's actually contributing to performance. The top performing content is still the same from last week — our top 10 websites, best data security tools, best collaboration tools — there's a lot of listicles. We might pivot some ideas for that. I'll double check after the content audit to see if that's consistent, but that's what's performing best.

**Sydney Go:** For our refreshed integration pages — these were refreshed last week — I don't think we'll see an immediate jump in traffic, but we can already see movement. We'll continue to monitor the impact on high-performing and lowest-performing pages. This week we plan to load 10 more articles. We've already loaded your first nine from last week into the CMS, with 10 more coming this week.

**Sydney Go:** We started adding "how to build" use case articles based on the goals you sent over. I couldn't find search traffic for some of them, but if you see value in other channels like Reddit, Twitter, or LinkedIn, we can still create those pieces. Let me resend the list so Paul can review which ones fit Strapi's use case.

**Paul BRATSLAVSKY:** Let me double check which ones make sense. We want to make sure they fit our use case if there's not much search traffic. But I'll review the list.

**Sydney Go:** Theo, we also saw your edits on the articles. We'll go through those this week and let you know when we've updated them so you can get those uploaded.

**Sydney Go:** For the API keys for both Medium and Strapi CMS — do you know where we can get those?

**Theodore ONYEJIAKU:** We'll probably set that up next week.

**Jason Gong:** Yeah, we can share those with you after the call. Now let me share some prompt tracking results. We got your list of prompts last week and loaded them all in — about 300 across Perplexity, ChatGPT, and AI Overviews. I'm creating a report you can review.

**Jason Gong:** Most of the prompts are at the awareness and evaluation stage of the funnel — comparing tools, asking "what's the best tool to do X." We're tracking what gets cited, what answers come back, and what links to the citations using tools like Scrunch.

**Jason Gong:** Some patterns we've already noticed: a lot of listicles are performing well. One competitor, HighGraph, has an article showing up in many prompts — it's a listicle comparing best CMSs. We haven't written that particular spin yet. We'll build a content backlog next week to determine whether to create new content, refresh existing content, or merge cannibalizing pieces.

**Jason Gong:** Different listicle variants seem valuable to invest in. Sydney already flagged that listicles are performing well in search. We're also seeing a lot of Reddit threads get cited. We could help you repurpose Reddit content as well.

**Jason Gong:** I see some good signs of your own content being pulled into AI responses. I'll get you a dashboard soon that you can click through. Any thoughts or questions so far?

**Paul BRATSLAVSKY:** Yeah, I have a question. Is there a way to understand how LLM search prioritizes which resources it pulls from? Like, how does it decide?

**Jason Gong:** The short answer is everyone's trying to figure it out. I've talked to the founders of Perplexity and others. To be honest, none of them are doing meaningful studies on it. Folks are now starting to release something, so we're pushing them and doing our own research. The thing is, LLM search isn't just positions one through five — they have an opinionated approach to which search results they use for citations. I haven't seen anyone unpack that yet. And it changes frequently.

**Jason Gong:** But basically, if content is ranking between pages 1 to 4, it has a better shot at being pulled. We should start by writing content we haven't even created yet. Once we learn what gets pulled, we can refresh and shape content accordingly.

**Paul BRATSLAVSKY:** So for V1 strategy, we're looking at competitors' content, creating a better version, and trying to rank it higher.

**Jason Gong:** Right. Then fine-tuning is: it's ranking well, but it's not getting pulled by AI — what's going on? We can figure that out next. A lot of content we need to write still. And note: content might show in Perplexity but not ChatGPT. For most people, ChatGPT drives the most, then Perplexity, then Claude is most common.

**Victor Coisne:** I was reading an article from AeroOps that identifies three criteria for AI optimization: freshness, structure, and authority. Freshness means having the updated_at field in Strapi to signal freshness. Authority means citing the right sources — when we write, we should quote thought leaders and resources they've created. Structure — you guys are already doing a great job there.

**Victor Coisne:** So we probably have room for improvement on authority and freshness.

**Jason Gong:** Do you guys do much surveying or thought leadership content of your own? For other customers, we try to weave that in if they do. Citing authoritative sources helps with freshness signals.

**Victor Coisne:** We probably should, but we don't.

**Jason Gong:** I've seen mixed results with freshness. Some people update a bunch of dates and it becomes a negative signal. But at minimum, content should have up-to-date information. A few weeks ago we found an example of legacy JavaScript framework references. Another thing that's important — every article mentions Strapi and how your product works. This shapes how LLMs think about your product. Your older articles probably describe the product differently than how it works now. We're trying to flag articles mentioning legacy Strapi features that don't work anymore. With 1500 blog posts, there are definitely pieces describing your product in outdated ways — we saw questions referencing "be to see you next time"

**Jason Gong:** Like forum posts from a long time ago. Sometimes questions come back with wrong answers — "Does Strapi support A or B?" when it actually does. It's usually version-specific behavior that changes.

**Paul BRATSLAVSKY:** So if you have Strapi 5 and Strapi 4 is moving to security-only support, does it make sense to remove content about Strapi v3? Is there a best practice for keeping information up-to-date?

**Jason Gong:** The answer depends. If an article says "Strapi 3 does X" and links to the right place, you don't need to worry. But when vague writing ranks well and gets cited, it throws things off. We're trying to build a brand guideline scanner that flags articles not describing the product correctly.

**Paul BRATSLAVSKY:** Some of those articles might not be written by your team — they could be from other authors. So we'd need to figure out who and how to update them.

**Jason Gong:** Right. In terms of fixing, we can potentially remove and rewrite paragraphs, but no promises. But scanning — we'll have that soon. Basically, we're trying to enforce proper product marketing across all the content you're creating.

**Jason Gong:** Listicles seem important. I've seen HighGraph pop up quite a bit. Next week during our strategy sprint, I want to see what content they're making and why it's doing so well in LLMs.

**Jason Gong:** V1 of prompt tracking is to help prioritize your content. For the future, we're thinking about how to help beyond vanilla link-building. We want to be smarter about getting Strapi mentioned on Reddit, Dev.to, TechRadar — places where you're not the only website talking about Strapi. That's partly PR, partly content placement.

**Victor Coisne:** If you have insights on which platforms we should target, a summary would be super helpful.

**Jason Gong:** I'm working on getting you a dashboard you can click through. Prices for this tracking are dropping, so in a month or two you can add more prompts. One category I haven't seen in our list is product marketing side — prompts like what customers ask when researching Strapi functionality and pricing. Those are worth tracking too.

**Victor Coisne:** That sounds good. Let's add that as an action item. I'll collaborate with Nuclas, who owns product marketing on our site.

**Jason Gong:** Once you give us API keys, we can help you publish cross-platform. Next week we're diving deep on strategy — figuring out what content to make and doing research we've been holding off on.

**Jason Gong:** On strategy, anything from your end? We talked about Vite coding a little. Maybe that's a cluster we start mapping next week?

**Victor Coisne:** Yeah. Vite coding and GEO — we want to be thought leaders in the SEO space too. SEO for websites is really important, and folks are having the same conversations we're having today. The more we can share transparently, the more it helps our audience. It's not just Vite coding, but also SEO. I've seen so many different terms — GEO (Generative Engine Optimization), AI Answers Optimization, AI SEO.

**Jason Gong:** I've seen all of those too.

**Victor Coisne:** Maybe we can compare them. There's a great AeroOps article, and they reference an Andreessen Horowitz piece on GEO. I think we should add that as a topic.

**Jason Gong:** Have you guys done much thinking on this? We're actually writing about this too — I have an hour-long interview with the Scrunch founder where we dive in. The interesting part for you is: if I'm building a website, how do I structure it to be accessible for AI?

**Victor Coisne:** And one thing — Vite coding doesn't follow best practices for GEO. That's an opinionated piece that could get attention. Headless CMS solves that — we've been doing that for years.

**Jason Gong:** Two sides to this. SEO-wise, we'll look at the Vite coding cluster. But there's actually no good information on how to build websites optimized for GEO. That's a piece of transparent, human-curated content worth creating.

**Victor Coisne:** We can create an internal piece comparing traditional SEO, traditional CMS, headless CMS with Next.js and modern frontend, versus Vite coding.

**Jason Gong:** GrowthX has production equipment for interviews. Since you're in SF, maybe we do something together at some point.

**Victor Coisne:** People definitely want to learn about this.

**Jason Gong:** Honestly, I don't know yet how you're supposed to start a website optimized for this. People are figuring it out. Some think the internet will be built for bots and crawlers, purely bot-optimized.

**Victor Coisne:** There's also programmatic SEO. Lots of folks are trying it — it's hot. CMS will be the best tool for that. We talked about a potential partner's search for a new CMS for programmatic SEO, so maybe we can learn from that.

**Jason Gong:** Cool. Theodore, do you have anything?

**Theodore ONYEJIAKU:** I wanted to add on content structure. If we could source code from your different use cases and add it to published content, that gives authority. And maybe with the workflows we have now — trained with prompts — we could have an AI agent where customers can ask questions from articles and get answers based on what we've fed the system.

**Jason Gong:** For the first point — what's the best resource for quotes on your website? User stories?

**Theodore ONYEJIAKU:** Yep.

**Jason Gong:** Okay, we'll definitely do that. We already do this for some clients.

**Victor Coisne:** You can also pull from G2 reviews. We haven't invested much in comparator pages, but there's content available there.

**Jason Gong:** Great. On the bot — most people we've seen do this have chatbots in the corner that index your site and answer questions. I'm not sure if we've built that for anyone before.

**Victor Coisne:** We have Kappa AI — that's our fact checker for workflows. It's our custom Strapi LLM. Maybe we make it more visible throughout the site. Right now it's only in docs and Discord.

**Jason Gong:** Kappa's a tool you use?

**Victor Coisne:** Yes, mostly for docs. But we could use it elsewhere.

**Paul BRATSLAVSKY:** Our Kappa AI bot is very tactical — specifically for developers. But this would be more general — answering "what's the best use case?" Like if someone asks "why should I use Strapi?" and we show them related articles. It's top-of-funnel, answering common ChatGPT questions about Strapi on our site with context-aware search.

**Theodore ONYEJIAKU:** Also for content itself — if readers have questions on a blog post we just wrote, beyond our FAQ section, they can ask. It's a suggestion.

**Jason Gong:** I've seen people try this. It can distract from CTAs, but I'd want to know what people ask. They should probably be in your content already. Could work in an FAQ section where the last question is "Ask Kappa."

**Paul BRATSLAVSKY:** I wouldn't build a separate agent.

**Victor Coisne:** Keep feeding Kappa with more things instead of building a separate one. Good idea. We can discuss internally. We could help pick which articles to index.

**Jason Gong:** I'm not sure how Kappa works, but you could put it in the FAQ section.

**Victor Coisne:** Kappa already takes our blog as a source. Mostly docs and YouTube. We should check how often they pull the latest from the sitemap.

**Jason Gong:** If you share what people ask, that would help us.

**Paul BRATSLAVSKY:** To keep Kappa up-to-date, I think it's using mostly OX docs, not articles. I'd double-check. I can give you access if you want.

**Victor Coisne:** That would be awesome. I'll ask Daniel — he has fact-trigger access.

**Jason Gong:** I think he has it. We can give you dashboard access with analytics.

**Jason Gong:** Okay. Next week we're focused on the strategy sprint. We'll figure out what content to make and do research we've been holding off on. Looking forward to it.

**Jason Gong:** Thanks everyone. Bye.

**Paul BRATSLAVSKY:** Bye.
