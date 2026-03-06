# Bryan Law <> Marcel Santilli

<metadata>
date: 2025-02-21
time: 22:38 UTC
duration: 26 minutes
organizer: alice@growthxlabs.com
participants: Marcel Santilli (GrowthX), Jimmy Pal (GrowthX), Drew Hoffman (SentinelOne), Bryan Law (SentinelOne)
fathom_recording_id: 48520183
fathom_url: https://fathom.video/calls/239039798
share_url: https://fathom.video/share/TJc7Vzkeft_2rpoHGRX7_UsEXDSya89t
source: fathom
enriched_on: 2025-03-05 18:40 UTC
</metadata>

---

## Summary

SentinelOne and GrowthX Labs explored a major content partnership to accelerate production and improve conversion on SentinelOne's 3,200+ page site. SentinelOne has achieved 172% traffic growth on their relaunched Cybersecurity 101 section and 42% YoY organic growth, but faces challenges scaling targeted, conversion-focused content beyond generic top-of-funnel material. GrowthX Labs proposed both editorial (custom strategy, $0.10/word) and programmatic (large-scale templated) content streams to help SentinelOne refresh existing content, create deeper insights, and expand into CISO-focused sections, with potential project start by March 24 pending procurement approval.

---

## Context

SentinelOne is an enterprise cybersecurity platform with a substantial organic content strategy. They've invested heavily in their Cybersecurity 101 educational content hub and operate a 3,200+ page site across blog, product guides, and educational sections. The company is led by Bryan Law (VP content/growth) and Drew Hoffman (head of content operations) and operates with formal IT and procurement processes. GrowthX Labs is a B2B content marketing services firm specializing in AI-powered content creation with human editorial oversight. Marcel Santilli (founder/CEO) and Jimmy Pal (cofounder) pitched the opportunity to help SentinelOne scale content production using workflow automation and editorial expertise. The meeting occurred as both companies approached end-of-quarter (SentinelOne's SCO was the following week), and GrowthX was booked through March 24, creating tight timing pressure.

---

## Relevance

**To GrowthX Delivery:**
- SentinelOne is 3,200+ pages deep with significant organic presence — opportunity for large-scale programmatic content refresh and existing page optimization (CTAs, cross-linking, internal references)
- Client challenges with manual refresh workflows and expensive content teams align with GrowthX's AI-human hybrid model value proposition
- Potential for CISO-focused content expansion represents new vertical/subsection work beyond current editorial model
- Timeline pressure: client needs decision/procurement approval within 3 weeks for March 24 start date

**To CheckThat:**
- Multiple mentions of AI-generated content concerns and Google's E-E-A-T signals — direct opportunity to surface CheckThat's AI visibility auditing for SentinelOne's own content evaluation
- Discussion of fact-checking workflows and prompt auditing suggests potential for CheckThat integration in GrowthX delivery process

**To GrowthX Business Development:**
- High-growth account (42% YoY, 172% on key section) with clear expansion appetite and budget awareness ($0.10/word editorial pricing discussed)
- Bryan Law flagged need to "double YoY" — strong signal for multi-phase engagement and upsell to conversion-focused content
- Reference potential: SentinelOne is established brand in security with measurable success metrics; results from partnership could drive future enterprise outreach
- Procurement friction (multi-week approval timeline) may delay start but validates serious buyer intent

---

## Overview

- SentinelOne achieved 172% traffic increase on Cybersecurity 101 section but struggles with conversion rates and deeper, more specific content at scale
- GrowthX Labs uses AI workflows with embedded editors to combine speed and quality, supported by proprietary research agents (Perplexity API, custom APIs for healthcare/verticals)
- Two pricing/delivery models: editorial ($0.10/word, custom strategy + dedicated editor) and programmatic (templated, volume-focused)
- Potential expansion: CISO-focused content section, 3,200-page refresh workflow, and cross-linking optimization to improve internal relevance and conversion

---

## Key Topics

### GrowthX Labs' Content Creation Process

  - Utilizes AI workflows with human editors for scalable, high-quality content production
  - Process includes:
      - Extensive research using multiple sources (e.g., Perplexity API, custom APIs)
      - AI-driven outline creation and content drafting
      - Human editor review and customization
      - Post-processing steps (e.g., style adaptation, cross-linking, SEO optimization, fact-checking)
  - Offers both editorial (custom strategy) and programmatic (large-scale templated) content streams
  - Pricing: \~$0.10/word for editorial content, with additional services included

### SentinelOne's Current Content Situation

  - Recently relaunched Cybersecurity 101 section, resulting in 172% traffic increase
  - Overall organic traffic growth of 42% YoY in Q4
  - Challenges:
      - Creating more specific, insightful content beyond general topics
      - Improving conversion rates from organic traffic
      - Scaling content production efficiently
  - Currently refreshing existing content manually, which is time-consuming and expensive

### Potential Collaboration Areas

  - Accelerating content production and refresh cycles
  - Developing more targeted, conversion-oriented content
  - Exploring new content sections (e.g., CISO-focused content)
  - Leveraging GrowthX Labs' AI workflows to reduce manual effort and costs

### Google and AI-Generated Content

  - Google doesn't explicitly penalize AI-assisted content
  - Focus on uniqueness, value-add, and E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness)
  - GrowthX Labs' approach emphasizes deep research and unique insights to meet Google's quality standards

---

## Action Items

**Marcel Santilli (GrowthX)**
- Send proposal + sample SLW to Bryan/Drew. Include project costs, structure details

- Initiate Slack Connect invite process for SentinelOne team

- Conduct deeper audit of SentinelOne site. Prepare insights on potential content strategies


**Bryan Law (SentinelOne)**
- Review procurement process timeline. Determine feasibility of starting project by March 24


**Drew Hoffman (SentinelOne)**
- Initiate IT request for Slack Connect approval with GrowthX Labs

---

## Transcript

**Jimmy Pal:** Traffic to like hundreds of thousands of people to the site.

**Jimmy Pal:** I started, I got the AI bug maybe two years ago, right when ChatGPT came along, as most of you did.

**Jimmy Pal:** And Marcel and I were building our own AI systems, separately attended one of his webinars.

**Jimmy Pal:** And I was probably the second person to join GrowthX and helping all clients, all things growth now.

**Jimmy Pal:** So yeah, when we started working together, we'll be helping you guys with all things that we are really good at.

**Marcel Santilli:** So excited to be on the call.

**Marcel Santilli:** Yeah, I'll just jump in to show you all a little bit of how we're thinking. I'll caveat on some of my background a little bit — I've been at different startups, but I would just mention our CTO Daniel and a lot of what we're building.

**Marcel Santilli:** He was leading product and engineering back in the day at a company called If This Then That.

**Drew Hoffman:** I remember that.

**Marcel Santilli:** So anyways, he built a lot of the distributed systems and everything that we're running — billions of runs and recipes and workflows. So that's a little bit of the background. When I show you a lot of what we're building, it's going to kind of click and make sense. My background early on was building these kind of organic growth engines and content engines for brands.

**Marcel Santilli:** At IBM, I built a site called SecurityTellers.com. Way back in the day, it was the first site outside of IBM.com that was allowed to be published. We grew that, became the biggest source of pipeline for the business. Then after that, I started building other content programs at HP — I built a contributor network. Every time it was the same thing: I'm hiring a managing editor, spinning up a whole team, producing content. And after six months or a year, things were growing quite fast, but it was a lot of work.

**Marcel Santilli:** So I'll fast forward a little bit. I started building these AI workflows and putting editors in the loop, just streamlining the whole process from engagement to publish. We published 30,000 pages, 24x'd traffic, company hit an awesome inflection curve. From there, I started doing workshops. That's kind of how Jim and I met and other folks in the company as well.

**Marcel Santilli:** A lot of people asked us to start doing that as a service because they needed both the strategy and the ability to adapt and build these AI workflows with humans in the loop to get all the work done and check the work. We started partnering with companies and seeing a lot of really awesome growth across the board. That's how GrowthX got started.

**Marcel Santilli:** Today, we're working with 35 different clients right now, and we have a huge list of folks that have come in recently in the last few months. But mostly it's because the alternative is — and you all might be running into this — what are the options? You can go with a really expensive agency that doesn't scale, or you're assembling teams, but a lot of us are really, really busy. And even if you go out and buy a lot of these tools to help streamline what you're doing, it's a lot of work. A lot of these companies are building tools to leverage AI, but as they're building, AI is evolving so fast that they're also falling behind.

**Marcel Santilli:** So the TLDR of what we're doing is we're signing up to do outcomes, right? It's not only a service, it's not only a tool. We're helping people. A lot of our engagements start with editorial content and programmatic SEO, but we're expanding around these different work streams.

**Marcel Santilli:** The idea is we start by understanding your market quite well. Our first 12 weeks, we do research on your company, your personas, and start to develop what opportunities matter in your domain area. Then we develop a content strategy with you within the first three weeks and get alignment. Hopefully by week three or four, we're calibrating on content quality and starting to publish for you. That's why a lot of companies partner with us — we can move super fast and scale things so we can learn from it.

**Marcel Santilli:** This is one that I showed Bryan in the meeting earlier this week — one of our research workflows. We did a ton of research on you all, understanding the context around your product, the use cases, the target personas, their motivations and interests. Our editors learn about you and your company, and that feeds downstream as we develop the content strategy. We do jobs-to-be-done analysis to understand your entire ecosystem. From there, we develop what we call the content OS, where we identify opportunities based on relevance to your business and how hard it would be to rank for them. We develop that content working closely with you, then start to publish.

**Marcel Santilli:** Our pipeline is the content OS. We work with you and say, "These are the opportunities we identify. This is how much potential volume there is here if we rank well for them. Should we go and start developing them?" We're constantly collaborating. Underneath the hood, we build a workflow engine that takes these workflows and runs it at huge scale.

**Marcel Santilli:** For research, just to do research for one topic, we're validating the topic, coming up with research questions, and finding tons and tons of sources around that topic. That's just one of many steps. As we're generating content, we do this across the board, inserting editors in the loop. They're directly assigned to you, working closely with you. That's how we're able to scale in a much more cost-efficient way while maintaining quality even with really technical topics.

**Marcel Santilli:** Hopefully that helps a bit of background.

**Drew Hoffman:** Can you walk me through this workflow?

**Marcel Santilli:** Yeah, absolutely. These are the steps of how we go from research to execution. We've done all this research for your company, came up with your content strategy, created assignments of potential content that we should be creating for you. Then this is how we execute. Let's take a topic — cloud security, for example.

**Marcel Santilli:** We break down that research into potential questions people might want to ask related to cloud security. We find hundreds of sources to answer those research questions, vet through them, and understand whether they're relevant to you and your business, and whether they're high-quality sources. If they are, we clean the content, process it, and put it into a vector database. Then we retrieve from that vector database and start to come up with an outline, using parallel processing with RAG. An editor reviews and tweaks that outline before we start producing the content.

**Marcel Santilli:** We take the topic, take some of the research, and understand what the top 10 search results are and the intent behind them. So we come up with a couple of different options for the angle for the article based on the outline. Then we draft, going through a bunch of steps to execute against the plan. After that, we do post-processing steps that are customized to each client — style adaptation based on your brand and voice, cross-linking steps, SEO optimization, fact-checking, editor feedback — all with editors in the loop. At the very end, an editor does a full final review. Then we create a cover image, anything else we need to do, stage it in the CMS, and publish. We have a similar process for refreshing content and other things.

**Bryan Law:** Something I thought was interesting was what we're generating right now. Traditionally, the AI model is creating a lot of very top-of-funnel generic content, and that's the stuff that's most quickly getting replaced and becomes irrelevant because it's just the easiest stuff for Google to answer. If we're really going to develop content, it needs to be more specified where we can leverage more insights that are ownable and harder to replicate. Having a more robust process would hopefully help us do that more effectively.

**Marcel Santilli:** What's the bottleneck today with you all? From just a quick glance, you have about 3,200 pages published. That's quite a bit of pages. You have Cybersecurity 101, a lot of different things, blog obviously. What's working? Are there bottlenecks? What's important to help in this next phase for you all?

**Drew Hoffman:** We relaunched Cybersecurity 101 at the end of summer and infused a whole bunch of content into there. It was a huge undertaking — maybe less a bottleneck and more of a challenge we had to overcome, especially with the significant amount of content we launched.

**Drew Hoffman:** Some challenges we have is what Bryan mentioned — the content is very generalized, but the more we can create content with deeper insights and more human-centered content, the better it will rank. It was a very manual process, and we've tried creating AI workflows. The challenge is it takes more to bypass Google than it does to actually write the document itself.

**Drew Hoffman:** We've scaled content pretty heavily and seen a significant increase. Traffic rose 172% on that project. But now the question is, while we're getting traffic and hitting Google, is that engaging content that allows users to engage with us further? That's where we're at.

**Bryan Law:** Just a few more things to add — we've seen really impressive impression growth. Looking at Q4, we're at 42% year-over-year overall organic traffic to the website, which is awesome. But our boss wants us to double year-over-year, so we're not there. Also, where we saw great impressions to traffic, we're not seeing that traffic convert into conversions. The challenge is, how do we make sure content is a bit further down the funnel so it helps us get more pipeline? How do we accelerate and make it more relevant to hopefully help drive more revenue?

**Marcel Santilli:** Yeah, that makes sense. There are a couple things that are really interesting. Looking at an example in the security space, even in a topic like "exploiting bias in LLMs" or "AI bias," there's a lot of very specific content with cross-linking to very specific sources — actual papers on the topic, pages in their docs. For example, "Let's examine proven safeguards and explore how modern security in LLM and prompt injection vulnerabilities come into play for a robust framework." That's very specific.

**Marcel Santilli:** That's the content calibration piece — being able to put all that into the content versus just giving an answer that maybe sites your competitors, which you don't want. We have a way to blacklist domains you don't want to use — your competitors, for example. We programmatically cross-link to pages on your site. With 3,200 pages, no human is going to know exactly which pages cross-link perfectly across the board, but we can do it at massive scale. For example, can we go in and refresh that content and improve CTAs on those pages automatically?

**Drew Hoffman:** We're currently going through phase two of that project, but again, it's very manual. We're doing a refresh on those pages from a content perspective and overall experience to make them more engaging and lead people into the core site.

**Marcel Santilli:** Do you have an army of writers or how are you approaching that today?

**Drew Hoffman:** We have our always-on writers, but for that project specifically it was a small army of writers that we had to recruit, and it was very expensive.

**Marcel Santilli:** That's the key point. The good thing is we can recruit editors and writers who can be domain experts. But the idea is you don't want to just throw humans at it — you want to use AI for what it's best at. We have your custom knowledge base that we're constantly evolving. Then you want editors and writers to do the things they do better than our workflows. Over time, that evolves.

**Marcel Santilli:** The challenge with a mostly human approach is with 790+ Cybersecurity 101 pages, most writers charge per hour or by word count. Do the math. And managing to do 700 pages in a month would be really difficult unless you scale up writers like crazy.

**Bryan Law:** Outside of the timeline of the 12 steps, how does your model work?

**Marcel Santilli:** Great question. We have two primary work streams. One is editorial, and we're super transparent about it on our website. With editorial, we're developing the content strategy, the content OS, and identifying opportunities — whether existing blog content or articles or net new content we're publishing for you. It's based on a rough word count of 50,000 to 100,000 words, so it comes out to about 10 cents per word.

**Marcel Santilli:** But we're not only publishing content. We're developing the strategy, adapting workflows, and assigning you a strategist editor who meets with you every week and manages a team of editors, production assistants, and research assistants. Everything from staging content in your CMS, creating cover images, checking for broken links — all handled end to end.

**Marcel Santilli:** The other stream is programmatic. It's based on page count and customized based on whether you're refreshing existing content or creating new pages. We've done hundreds of pages around comparisons, expense categories, landlord laws, DUI, etc. It can be almost anything. You could say, "Anytime there's a zero-day vulnerability, we want a page that describes it well." We stand up the program, create the cluster, and start producing at scale. All with humans in the loop.

**Marcel Santilli:** Think of editorial as custom outline, custom research, different content types. Programmatic is building a knowledge base, templatizing it more, doing it at much broader scale.

**Drew Hoffman:** How do you bypass Google signaling that content is AI-generated? Is the human element how you do that?

**Marcel Santilli:** Google doesn't actually punish AI-assisted content. It's trying to understand uniqueness and how much value is added. It's measuring E-E-A-T — Experience, Expertise, Authoritativeness, Trustworthiness. If there's no value, if it's just reshaping content that exists somewhere else, that's a danger if you use tools like Copy AI without going deeper. That's why we put so much effort into our research agent. We're not relying on just Google search results. We use Perplexity API, U.com API, custom APIs in healthcare, process PDFs, and go into hundreds of sources, vetting them ourselves. So the content we create is well-cited, unique, authoritative, and trustworthy.

**Marcel Santilli:** And if you have internal sources of knowledge, we layer that on top, which is even better.

**Jimmy Pal:** To add to Marcel's point, we have the collective intelligence of all the best writers and editors from our clients. We gather feedback from all these folks and keep embedding it into our workflows. That's the added advantage of what we're learning. You get the best of everything we have to offer. We apply what we learn from other clients' workflows to yours, and we build on top of that. Our system has recently started learning this, and we're super excited to keep implementing it.

**Marcel Santilli:** For instance, Galileo AI and Strapub, a headless CMS, needed a fact-checker to make sure content never mentioned a feature that doesn't actually exist in their products. We built the fact-checker and now that's pretty standard in a lot of our workflow. Fact-checking is one of the post-processing steps to ensure nothing inaccurate is in there.

**Marcel Santilli:** I know it's end of day for all of us, but Brian, happy to keep the conversation going and send a proposal out. We're booked out until March 24 — we just finished signing clients for March 17. But obviously, we'd love to find ways to work together. I love the security space, and it would be really cool to supercharge what you guys have already accomplished.

**Bryan Law:** This is super interesting. A great next step would be to get a bit more on what a project could look like from a cost perspective and how it would function. Practically, our procurement process isn't that fast, but as part of you sending things over — whatever you would traditionally do if starting something — we can see if we want to actually try and get it in the system. It normally takes a few weeks anyway.

**Marcel Santilli:** That sounds good. Are you guys using Slack? Is it hard to get on Slack Connect?

**Drew Hoffman:** We just have to go through our IT. Very much a Slack organization.

**Marcel Santilli:** Perfect. We usually add everyone to a Slack Connect so it's super easy to ping back and forth. I personally hate email, but I doubt you have a random love for it either. We'll make it easier. I'll send you a sample SLW — not because you need to sign it right away. You guys have your process, but it's where we have all the language and what an engagement looks like. Just so you have it in front of you. We can plan to spend more time next week and I'll do a bit more of an audit on your site and come with more insights on potential things we could be doing.

**Drew Hoffman:** I've been tossing around the idea of opening up another section specifically targeted at CISOs or a very hyper-targeted audience. That might be an area where we could ramp up content — just an idea right now.

**Marcel Santilli:** We can dive into that.

**Bryan Law:** From a timing perspective, next week we're at our SCO, so we're pretty sidetracked, but same for you. Congrats and thank you for taking us as you're closing down.

**Marcel Santilli:** Thanks, thanks. This is super exciting because I love the security space — I've been in it for so long and have a lot of personal insight into it. It would be really cool to work together.

**Bryan Law:** Thanks guys, we really appreciate it. Enjoy the offline next week. See you guys.
