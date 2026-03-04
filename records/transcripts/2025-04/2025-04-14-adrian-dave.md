# Adrian | Dave

<metadata>
date: 2025-04-14
time: 19:03 UTC
duration: 32 minutes
organizer: dave@growthx.ai
participants: Adrian Machado (Zuplo), Dave Capone (GrowthX)
fathom_recording_id: 57200756
fathom_url: https://fathom.video/calls/274776302
share_url: https://fathom.video/share/5GzwDfMd8KjGCQQCRM2RrR7y-ZdjxSso
source: fathom
enriched_on: 2026-03-04 12:00 UTC
</metadata>

---

## Summary

Dave Capone introduced himself to Adrian Machado as GrowthX's newest team member, and the two discussed Zuplo's SEO growth strategy and initial successes working together for three months. The core opportunity: Zuplo wants to scale API documentation content programmatically, targeting 1,500 pages sourced from the API Guru repository, with GrowthX building a content generation pipeline. The main blocker is content accuracy—Adrian needs confidence that AI-generated API guides will be factually correct and stay current as APIs evolve—so the team is starting with 4 sample articles weekly to refine the prompt before full-scale production. Delivery format: CSV files with API identifiers and markdown content that Zuplo can ingest into their GitHub-based CMS.

---

## Context

Zuplo is a developer-focused API management platform competing in a crowded space dominated by AWS API Gateway, Google Apigee, and startups like Kong. Adrian Machado leads growth at Zuplo; he was previously at Facebook working on videos growth and SEO. He recently shifted from product work to GTM and brought GrowthX on board at the beginning of 2025 to accelerate signups and demos through SEO. The partnership is paying off—Zuplo has seen meaningful traffic growth in Google Search Console and increased signups/demos since September, though Adrian wants to prove quick wins to maintain budget and momentum with his leadership team. Dave Capone is relatively new to GrowthX and was meeting Adrian for the first time to understand Zuplo's business model, KPIs, and content strategy.

---

## Relevance

**To GrowthX Delivery:**
- Programmatic content generation at scale (1,500 API documentation pages) is a new service opportunity requiring a specialized prompt engineering and quality assurance workflow.
- Content accuracy and freshness are critical success factors—AI-generated API guides that are out of date or inaccurate damage client reputation and will require monthly refresh cycles.
- Delivery via CSV with markdown content is Zuplo's preferred format; integration points: API Guru repo (data source), Zuplo's GitHub-based CMS (distribution), and GrowthX's internal content knowledge base (for internal linking and deduplication).

**To CheckThat:**
- Adrian mentions AI-driven content generation as part of Zuplo's strategy—good signal for CheckThat's AI visibility positioning and opportunity to help Zuplo optimize for AI-generated search patterns.

**To GrowthX Business Development:**
- Zuplo values quick wins and measurable results; the 4-article/week pilot with quality gates is a low-risk path to demonstrating programmatic content ROI before scaling to 1,500 pieces.
- Account expansion signal: Adrian is focused on scaling signups and demos (10:1 value ratio). If this content initiative drives meaningful qualified traffic, there's potential to expand into other underperforming content areas or vertical deepening beyond API docs.

---

## Overview

- Zuplo aims to increase signups and demos through SEO, with a focus on differentiating in the API management space
- Current SEO efforts show promising results, with traffic and signups increasing since September
- Programmatic content generation for API documentation presents a scalable opportunity to create 1500+ pages
- Content accuracy and freshness are crucial concerns for the programmatic approach

---

## Key Topics

### Zuplo's Business and Growth Strategy

  - Zuplo operates in the API management space, competing with big cloud providers and startups
  - Differentiators: More flexible, developer-friendly platform; ability to write code at the API gateway
  - Growth focus: Increase signups and demos (valued 10:1 vs. regular signups)
  - SEO identified as a promising area for growth, started in September last year
  - Mix of content creation, technical SEO, and some programmatic/AI-driven approaches

### Current SEO Performance

  - Significant traffic increase visible in Google Search Console
  - Translating to increased signups and demos
  - Working with GrowthX for \~3 months, seeing "decent results"
  - Typical SEO timeline: 3 months for articles to reach maximum ranking potential
  - Cannibalization concerns addressed; multiple ranking pages for keywords generally healthy

### Programmatic Content Generation for APIs

  - Proposal to create 1500+ pages of API documentation content
  - Data source: API Guru repository with 2,500+ APIs (pruned to \~1500)
  - Content structure: API name, authentication, available endpoints, competitors, etc.
  - Challenge: Ensuring content accuracy and freshness
  - Current pace: 4 articles/week to refine the content generation process
  - Delivery format: CSV with identifier and markdown content, organized by sections

### Content Refresh and Maintenance

  - Need for regular content updates due to frequent API changes
  - Exploring options for automated monthly refreshes
  - GrowthX to investigate refresh rates and options for maintaining content freshness

---

## Action Items

**Dave Capone**
- Create sample API content pieces using API Guru website as source. Research popular APIs, generate content, assess quality/accuracy.
- Follow up with Adrian re: content refresh rates. Pull old underperforming content into Looker for analysis.

---

## Transcript
**Dave Capone:** took the kids to a movie.

**Dave Capone:** This meeting is being recorded.

**Dave Capone:** That was it, took them to go see the new Minecraft movie, and that was it.

**Adrian Machado:** Oh nice, that was it.

**Dave Capone:** It was actually pretty good.

**Dave Capone:** I had to stop being a dad for about an hour and half because the theater was filled with kids and they were all screaming out the screen and throwing popcorn and having a good time and at first I was kind of like, oh I can't you know, I can't talk and you can't yell and all that other stuff and I was like whatever it's fine, just go do it.

**Adrian Machado:** Yeah, you had to like go at some point, right?

**Adrian Machado:** Awesome, awesome.

**Dave Capone:** So we should take about it.

**Dave Capone:** Yeah, so it's I just really wanted to spend some time and get to know you.

**Dave Capone:** I know that, you know, I'm relatively new, so I know you've been with the growth mix for a while.

**Dave Capone:** I really just wanted to like learn more about you and like the company and what their specific

**Dave Capone:** The goals that you're trying to meet and how we can help you or if there's like from a growth perspective is it signups really just trying to understand what your KPIs are and from a content perspective, how we can work with you to kind of you achieve those goals.

**Adrian Machado:** Yeah, absolutely.

**Adrian Machado:** So I'll kind of start from the top.

**Adrian Machado:** I guess I'd summarize my role is like growth at Zuplo over here.

**Adrian Machado:** I was previously at Facebook before this.

**Adrian Machado:** I was also doing kind of growth work for like the videos team over there, both like internal growth as well as a little bit of SEO while I was at Facebook.

**Adrian Machado:** So that's how I kind of picked up on some of this stuff and then switched over to Zuplo because one of the co-founders, Josh, he worked with me at Facebook and he just kind of pushed me over while I was getting bored.

**Adrian Machado:** So then it's a common story, I guess.

**Adrian Machado:** I was doing a lot of product work for a while at Zuko for about like two and a half years and then about like around the beginning, more so around.

**Adrian Machado:** At the middle of like last year, I kind of switched into more of a GTM type role, primarily helping to drive awareness of Zuplo and signups up, just developing our different motions around what a good SEO strategy should look like, who we should hire, our messaging, things like that.

**Adrian Machado:** And beginning of this year is when I decided to start working with Go with X, so we can start going hard on SEO.

**Adrian Machado:** The primary goal is to grow like signups and demos, I'd say of the product.

**Adrian Machado:** So a little bit about Zuplo is that we're in the API management space.

**Adrian Machado:** So some contemporaries in there include like big box solutions from like the matrix clouds.

**Adrian Machado:** So like AWS has like an API gateway, Google has like Apigee, Salesforce, so there are like some big box options, as well as some other startups in the space that are a little further along.

**Adrian Machado:** So like Kong and Tyke and

**Adrian Machado:** You can look at the sheet that I put together with the GrowthX team, and you can see some startup competitors there.

**Adrian Machado:** The way Zuplo differentiates ourselves is that, I'd say it's on two fronts.

**Adrian Machado:** One is like our platform is far more flexible and developer friendly than most other API management products out there.

**Adrian Machado:** You can, we have something called an API gateway, which essentially is sort of like a layer in front of most people's APIs.

**Adrian Machado:** And we're one the only gateways that you can actually write code at this gateway.

**Adrian Machado:** It's super fast and deploy, it's super simple.

**Adrian Machado:** We have a nice web UI, very much similar to this, traditional dev tools that people are used to, we're selling and things like that.

**Adrian Machado:** We try to bring that same experience back and development in APIs.

**Dave Capone:** It's similar to like a payment gateway where all transactions go through the payment gateway, and there's a gateway.

**Adrian Machado:** Yeah, exactly, same idea, but just purely for API requests so like anything can really go through the API.

**Adrian Machado:** Anyway, so it's kind of like a single pane of glass and there's a lot of cool stuff you can do with that. So, you know, that's just the API gateway. We consider ourselves an API management platform, which is like a broader layer. So what's included in API management? Things like logging and monitoring, authentication, infrastructure pieces like rate limiting quotas, as well as product-level features like monetization—being able to monetize your API requests on a usage-based or subscription-based model. And things like generating a full developer portal experience for users so they can browse documentation and interact with the API through a sandbox. A lot of different features kind of bucket under API management. So we're positioned a little bit higher compared to just gateways. In terms of our struggles to date, mostly around go-to-market.

**Adrian Machado:** If we have a lot of incumbents in the space, other startups in the space, how do we differentiate? How do we stand out? How do we gain attention and eyeballs, right?

**Adrian Machado:** We don't want to go fully open source. Based on companies in the space that have gone fully open source, it works out in the beginning, but then it peters out towards the end when you're trying to convert open source users to actual paying customers. A lot of them are sophisticated enough to just deploy your stuff themselves. So it makes it harder for us to move fast if we have to constantly update the open source community and manage breaking changes that way.

**Adrian Machado:** So, it makes it more difficult in terms of go-to-market, where we have to do developer relations and stuff like that. But we found that SEO is a promising area.

**Adrian Machado:** So it started working on September of the last year since doing some like a mix of things.

**Adrian Machado:** Creation of content, SEO technical best practices, a little bit of programmatic SEO, and some AI mixed in.

**Adrian Machado:** We've been able to create traffic quite substantially.

**Adrian Machado:** You can see it in Google Search Console.

**Adrian Machado:** And that's translated into real results—our signups have gone up over time, and so have demos.

**Adrian Machado:** I value demos at roughly 10 to 1 versus regular signups. Our signups and free users are great for awareness and word of mouth, but demos are the ones that could be actual enterprise deals.

**Adrian Machado:** Anyways, but yeah, like demos and signups have grown.

**Adrian Machado:** And that's why I started working with GrowthX to take this to the next level. Can we scale out this SEO? Can we produce AI-powered content, and down the road, programmatic SEO to really drive results up a notch?

**Adrian Machado:** What can we learn? Can we actually drive meaningful results? And we've been working with GrowthX for about three months now, and we've seen decent results. I know SEO is a lagging thing, right? We're putting out all this content and it probably takes a few days to get indexed, then a few weeks to get ranked, and then a few more weeks for our authority to push us high enough to actually rank well.

**Adrian Machado:** So we've seen some promise, but I'm just trying to do whatever I can to accelerate the process, get quick wins so it keeps justifying the costs to my leadership and keeps us investing in this.

**Dave Capone:** Yeah, that makes total sense.

**Dave Capone:** typically what I'd like to tell everybody is it's about three months before articles can start to rank.

**Dave Capone:** What you'll notice is typically when they get indexed, they start progressing through the index, you'll see them enter.

**Dave Capone:** and it'll be like on the last page, but then they'll start slowly creeping towards the first page.

**Dave Capone:** That's healthy and that's typically what we see with most of our clients is that when those articles are launched, there's a nice progression and you can watch as the rankings improve throughout time and then they usually get their maximum run right around three months.

**Dave Capone:** That typically is what the curve is of how we see growth for these and it's been like that for I don't know, last couple years that I've been in content marketing and editorial SEO, so that's been pretty standard across the board.

**Dave Capone:** The more links you get and sometimes if there's like inherent weakness and there's like a lack of a great answer for a specific query, sometimes they'll pop in quicker, which I've seen happen before as well, where this is like you've got a low KD kind of, if you were great, yeah, yeah.

**Dave Capone:** Or sometimes a high KD that just doesn't have like what Google's looking to,

**Dave Capone:** to differentiate in the SERPs, So like there's maybe an intent that the query's not hitting and then, you know, there's a transactional intent that's not being met.

**Dave Capone:** then all of a sudden, like you put a transactional page and boom, you rank it, right?

**Dave Capone:** So like those are some of the things that I've seen that would accelerate that growth.

**Dave Capone:** picking the right form of content or the right, like landing page to kind of do that would be helpful.

**Dave Capone:** And that's typically what the team is doing.

**Dave Capone:** So we're going through in the research pages and looking at these queries and seeing what the competition is doing, what types of formats are they using?

**Dave Capone:** Is it listable format?

**Dave Capone:** it even an interest story?

**Dave Capone:** it a data science piece or a white paper or something?

**Dave Capone:** then we figure out, okay, well, there's a lot of this in high correlation to ranking something that's, you know, little bit different by answers these and times.

**Dave Capone:** So definitely a lot of fun there.

**Dave Capone:** So looking at your clicks and I've put a new, I think one.

**Dave Capone:** The things that we were talking about was cannibalization.

**Dave Capone:** So I think you were pretty worried about URLs, articles cannibalizing some of the articles that you were writing.

**Dave Capone:** So I actually pulled together a dashboard and take a look at that view and share something real quick.

**Dave Capone:** what I've seen is like everything looks pretty healthy so far here.

**Dave Capone:** And we can set the screen.

**Adrian Machado:** Yeah, I can see it.

**Dave Capone:** Cool.

**Dave Capone:** So this view shows keywords by the number of landing pages ranking for each. I'm showing URLs that rank for the same keyword. Let me sort by clicks since that's your most important metric. This particular keyword has four different landing pages ranking, and we're looking at about 200 clicks total. When I click through, I'll show the average rankings of all pages for this keyword.

**Adrian Machado:** Now we got you.

**Dave Capone:** Now what you see is that everything's very consistent across rankings. Nothing has dropped out of the index, which is what you want to watch for. When you launched this JSON Merge Patch article, for example—

**Adrian Machado:** Yeah, yeah.

**Dave Capone:** If your top-ranking page (the blue one at 8.82) goes away once the new article ranks, that would be cannibalization. But instead, you've got multiple rankings for the same query, which is actually really nice.

**Adrian Machado:** That's good in a way, right? What I'm really tracking here is that blue line. The fact that it's kind of decreasing over time is actually improving—higher rankings are improving conversion potential.

**Adrian Machado:** The other ones might be ranking for similar keywords too.

**Dave Capone:** It's the same query—JSON Patch. Even the gold article is doing really well, but the other one is starting to peter off.

**Dave Capone:** So if anything, this the other one might be something that we can look into consolidating into another article.

**Adrian Machado:** The yellow one is related to keyword number three—JSON Patch versus JSON Merge Patch are two different standards with similar names, which is why there's slight cannibalization. But JSON Merge Patch now ranks at 2.7, so it's working as intended. It's just unfortunate naming.

**Adrian Machado:** OK, so.

**Adrian Machado:** But otherwise, it seems pretty low, like.

**Adrian Machado:** Cannibalization yeah, they're high-ranking articles.

**Dave Capone:** What I'd be worried about is the intended page being out-ranked by another page. Let me sort by impressions instead. If there's cannibalization, your clicks wouldn't be as high because you'd be occupying several positions for the same keyword.

**Adrian Machado:** Yeah, so there's only one landing page on this one.

**Dave Capone:** Yeah, so we're not really cannibalizing much except for Patch, which seems to be related. In that situation, here's what I'd typically do—

**Dave Capone:** If the blue one is your hub, I'd link out to these other pages to help them rank for related topics.

**Adrian Machado:** Yeah, that's kind of what I did with these—they all link to each other. I think that's why they've been able to rank: they're all interlinked, so Google crawls them frequently.

**Adrian Machado:** That's pretty good because I was worried about the monetization model article—there's some redundant content there and clicks are low. But it's moving in the right direction. Strategic API monetization is doing really well.

**Dave Capone:** The brown one is also doing good. The orange one started to fall off but came back. I'm not the biggest fan of Looker—I'd prefer Tableau or something, but this is what I've got to work with.

**Adrian Machado:** I know it's not the most robust tool, but I appreciate you making the best of it.

**Dave Capone:** But I think, uh, I've been, uh, I got to reset it, but I've been, uh, heavily influencing, uh, on my end, and like, we got to get our data warehouse, right?

**Dave Capone:** we've got to, you know, start building some good reporting and, yeah, like, I want to be able to show this stuff to clients, like, as we're, you know, going through client reviews weekly or biweekly.

**Dave Capone:** Um, and I wanted to get your feedback on that too.

**Dave Capone:** So currently we eat weekly, right?

**Adrian Machado:** Uh, yeah.

**Dave Capone:** week.

**Dave Capone:** So do you feel like that?

**Dave Capone:** Kate

**Adrian Machado:** where we can sort of generate articles, know, the house under like some sort of URL structures, like, you know, our website, whatever.com slash API slash, you know, API name or like some identifier for it.

**Adrian Machado:** And then like we would use AI and like a content workflow to sort of generate different aspects of the API.

**Adrian Machado:** So like, oh, here's like the documentation for it, here's like the website link.

**Adrian Machado:** Here's the like SDKs and libraries associated with this thing.

**Adrian Machado:** Here's like, I don't know, guess MCCP servers are like a big thing right now.

**Adrian Machado:** So if you're like, you know, and you know, we can generate a lot of that stuff ourselves.

**Adrian Machado:** We do any kind of like basic, like clean, like base data and then like a way to kind of plug into the content pipeline to actually generate like textually relevant content.

**Adrian Machado:** So we can have like a hub basis like, oh, you click into the OpenAI API.

**Adrian Machado:** This is exactly how the OpenAI API works.

**Adrian Machado:** It's like, you know, a few salient points, like how do you

**Adrian Machado:** get an API key, how, like, what APIs are available, what are the competitors, things like that.

**Adrian Machado:** know, the basic stuff people want answer, and here's our like some useful links.

**Adrian Machado:** And, you know, we're off to the races, right?

**Adrian Machado:** if we can do that at scale, you know, you can imagine there's like thousands and thousands of APIs in the web, right?

**Adrian Machado:** So, we can, you know, we don't have to rank number one for all of them, right?

**Adrian Machado:** But there's certainly many that like don't have like this information centralized.

**Adrian Machado:** So that's kind of like our, the programmatic aspect I want to approach.

**Dave Capone:** So, if you can make that data available, we could crunch all that data and spit out an entire glossary or like page like that, so we could set up a structure, can have everything set up and we can actually take that data and render it ourselves for you.

**Dave Capone:** So, like, yeah.

**Adrian Machado:** Can I take over the screen for a second?

**Dave Capone:** Yeah, go ahead.

**Adrian Machado:** So there's this API repository that has about 2,500 APIs.

**Adrian Machado:** Although I'd probably cut off like 500 of these because they're companies we'd avoid—like Microsoft—which has 500 APIs themselves and no one searches for each individual one. They have their own docs.

**Adrian Machado:** But anyway, this repository is nice because it's in structured format. The challenge is the site is out of date—no one's really maintaining it anymore. But there is structured data available.

**Adrian Machado:** If you're familiar with APIs, there's something called an API spec—a machine-readable description in JSON format. That's what we'd use as the core data for generating content. And there are URLs for each spec, which we can also push into the content pipeline.

**Dave Capone:** So you want to cross it and tell me mention a specific API you want to cross the link to the repository?

**Adrian Machado:** So what's nice is it includes docs for some APIs, and there are reference URLs. For example, this one is the Adafruit API with a reference to adafruit.com. You can use that as a source reference for research.

**Adrian Machado:** So I'd ask: can you generate a guide to this API? Cover the points I mentioned—how to authenticate, what endpoints are available, pricing, alternatives. Some of this is documented, but some is in textual format on the website.

**Adrian Machado:** If I go to the website, some information is spread across multiple pages. Can you extract that information and convert it from machine-readable format into a usable guide?

**Adrian Machado:** And can we do this at scale? All the data is there. What I need help with is the text generation. I can create all the URLs and scrape the data myself—the website is machine-readable.

**Adrian Machado:** It's all within a GitHub repository. That's the base idea. And what's really nice is that because this is an open format, I can use it for other things.

**Adrian Machado:** Like, "Use this API on Zuplo" with a quick start, or "View it in our open source docs." I can plug in different company touchpoints to make it more transactional.

**Dave Capone:** Like we can use this API on Zupo.

**Adrian Machado:** Yeah, yeah, exactly, right.

**Adrian Machado:** "Use this API now," or "Secure your access," or "Use Zuplo as an integration gateway." There are several CTAs I can add that would add value to us.

**Adrian Machado:** Ideally we'd skip large providers like AWS and Microsoft, but there are probably some good APIs in there worth researching. The challenge is they don't always have their house in order, so we'd need to manually review to avoid duplicates.

**Adrian Machado:** But anyway, that's one example of where to get started. After pruning, we're looking at about 1,500 APIs.

**Dave Capone:** I'm happy to do some of that pruning. One thing we're working on is a repository of all content written for a client, so when we generate new articles we can reference existing ones for quotes and internal linking. Daniel's working on that now, so we should have it ready soon. That'll be huge for knowing what's been written and enabling smart internal linking.

**Dave Capone:** So when we go and go ahead and do the 1500 pieces of API content Yeah, and then reference that in all the articles that we write Yeah, exactly.

**Adrian Machado:** The main thing I'm worried about is accuracy. If someone bounces off inaccurate content, it hurts our reputation. So I need confidence that the content engine produces accurate articles. We've been doing some examples—like the OpenAI API guide. We're currently at about 4 articles per week as a pace.

**Adrian Machado:** We're doing 4 per week while I refine the prompts. I manually inspect each one—checking if it's out of date, if code samples are still relevant, if it's citing unofficial sources. Once I nail the prompt, we can scale.

**Adrian Machado:** Because if we scale out with the wrong prompt, we'd have to redo all 1,500 articles, which is a massive waste of resources. That's why I'm focused on getting confidence in the prompt first.

**Adrian Machado:** What I've learned is that we need to constrain the content engine with domain rules—only look at GitHub and the official API owner's URL. A rules engine with blocklisting helps, though sometimes it still escapes the rules because it's not formally built in.

**Adrian Machado:** The main blocker is just designing the site, which is trivial for me as an engineer. You'd generate the text content and I'd download it on the fly and populate it into pages.

**Adrian Machado:** It's not a hard project. I just need confidence in the content engine. The critical part is ensuring accuracy, freshness, and the ability to do automated content refreshes.

**Adrian Machado:** We'd need a way to rerun the job monthly because APIs change frequently.

**Dave Capone:** If you're handling page layout, we could just supply content as a CSV that you load into a database or headless CMS to pull the data.

**Adrian Machado:** Exactly. We use GitHub as our CMS—we host markdown pages there. If you generate a CSV with two columns—an identifier and the markdown content—that's all I need.

**Dave Capone:** That's all I would really need.

**Dave Capone:** That's it.

**Dave Capone:** And then, like, the content.

**Adrian Machado:** And ideally, maybe a column for section names so the content can be organized on the page accordingly.

**Adrian Machado:** Headings would be like "Alternatives," "How to Get Started," etc. You'd send an agent to research each section and come back with results.

**Dave Capone:** And that would be a different thing.

**Dave Capone:** Oh, of these.

**Adrian Machado:** Anyway, I'm not sure what bandwidth your team has.

**Adrian Machado:** I'm happy to support and build this out. I just need to make sure you guys are ready to do this at scale with confidence in the accuracy.

**Dave Capone:** For us, the content will go through a manual review process. We'll pull in the keyword and API and do the research on it.

**Dave Capone:** It should go quicker since we're not updating existing articles. These will be 500 words or less.

**Adrian Machado:** It'll probably be 500 to 1,000 words. The example I sent you is about the right size. It covers pricing, alternatives, available APIs, and code samples. We need to find a way to scale this on your side.

**Dave Capone:** Okay, we can definitely do that. I'll have the team pick a couple from the API Guru repository.

**Adrian Machado:** Let me send you that link.

**Dave Capone:** I've got it—API Guru.

**Dave Capone:** We'll grab some popular ones, do research, and see how it turns out.

**Adrian Machado:** If you can grab from that repo and generate something good, that would be amazing.

**Adrian Machado:** We could eventually generate 1,000-plus pages. Google will take a long time to index them all, even with sitemaps.

**Adrian Machado:** But I need to start now so they have time to index.

**Dave Capone:** If we start now, they'll probably start ranking in July. It depends on how obscure the topic is—if it's not competitive, they could rank sooner. But it depends on the difficulty of each keyword.

**Dave Capone:** But the majority of the batch should hit peak rankings in the third month.

**Adrian Machado:** Sounds good.

**Adrian Machado:** Okay, I got to hop off.

**Adrian Machado:** I have another meeting after this, but it was a good time of chatting with you to give you something to noodle on.

**Adrian Machado:** And let me know if you have any questions or, you know, you can hit me up on Slack and what was available.

**Dave Capone:** I'll hit you up on Slack about refresh rates. We can pull underperforming content into Looker for analysis.

**Adrian Machado:** Sounds good.

**Adrian Machado:** We'll come up with options. Thanks, talk soon.

**Dave Capone:** Sounds good, bye.

**Adrian Machado:** Bye.
