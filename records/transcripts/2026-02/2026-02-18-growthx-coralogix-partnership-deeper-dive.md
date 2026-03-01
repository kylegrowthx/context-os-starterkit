# GrowthX <> Coralogix - Partnership Deeper-Dive

<metadata>
date: 2026-02-18
time: 21:00 UTC
duration: 34 minutes
organizer: tyler@growthx.ai
participants:
  - name: Tyler Pavlas
    company: GrowthX
    role: Founding Account Executive
  - name: Brian Mullen
    company: Coralogix
    role: Head of Marketing
  - name: Katie McCoole
    company: Coralogix
    role: Demand Gen Lead (NA/EMEA)
  - name: Emma Mock
    company: Coralogix
    role: Campaign Manager
  - name: Ishaan Bhardwaj
    company: Coralogix
    role: Analytics/Marketing Operations/Organic SEO
fireflies_id: 01KHMEW1SN5WGGWYGXFBVG9R87
source: fireflies
meeting_link: https://growthx-ai.zoom.us/j/4783917602?pwd=SaydcdMdj9OaMnVHpCiwZwIQfrIQxB.1
transcript_url: https://app.fireflies.ai/view/01KHMEW1SN5WGGWYGXFBVG9R87
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Tyler presented GrowthX's end-to-end content platform to Coralogix's demand gen and SEO team, covering workflow architecture, Temporal-based publishing pipelines, and CMS integration. Coralogix identified critical wins: 2–3 year old blog pages requiring refresh, schema gaps post-website rebuild, and insufficient internal SEO writing capacity. Decision expected Thursday next week; kickoff 3–4 weeks out; results projected Q2 2026.

---

## Context

Coralogix is a log analytics and observability platform (often competing with Datadog) evaluating GrowthX for an SEO/AEO content engagement. Brian Mullen (head of marketing) had an initial conversation with Marcel; this call was a deeper explainer for the demand gen and analytics team who would actually work with GrowthX day-to-day. Tyler ran the session solo. The Coralogix team includes Katie McCoole (Demand Gen NA/EMEA), Emma Mock (Campaign Manager), and Ishaan Bhardwaj (Analytics/MarOps/SEO — six months in, formerly on the agency side for three years).

---

## Relevance

**To GrowthX Services:**
- Deal in late evaluation stage; decision expected by Thursday next week
- Target kickoff: 3–4 weeks from decision; Q2 results expected
- GrowthX opening an additional kickoff slot to accommodate earlier start if needed
- Coralogix's high-traffic blog pages were last updated 2021–2022 — easy refresh opportunity identified
- SEO/AEO gap identified via Semrush AI visibility tracker; schema and meta tags were backfilled after June/July 2025 website launch
- Ishaan's key questions: legal review for comparative content (Datadog vs. Coralogix), self-serve platform timeline, CMS/WordPress publishing integration
- Tyler confirmed: multiple review rounds including legal vetting; separate site sections recommended for sensitive comparative content
- CMS integration: GrowthX connects directly to WordPress (or similar) for staging and automated publishing, including content refreshes
- Self-serve access: available in month 2–3 of a 12-month engagement
- GrowthX will scan Coralogix's website to generate V1 artifacts; additional resources from client help refine them
- Augment Code case study presented: 20K → 70K monthly organic visitors; near-zero paid ad spend
- Follow-up meeting with Marcel scheduled for next Thursday or Friday

**To CheckThat:**
- LLM monitoring platform mentioned briefly — Tyler noted GrowthX just launched it — but not the focus of the discussion

---

## Overview

- Partnership overview: GrowthX as a full-service content team extension; daily publishing and content refresh at scale
- Content refresh opportunity: Coralogix's highest-traffic blog pages are 2–3 years outdated — fast wins available
- Two-phase engagement model: strategy sprint (artifacts, keyword roadmap, personas) → scale (five articles/week calibrated to quality)
- AI workflow architecture: Temporal-based; research → drafting → review → CMS publish — all customizable per client
- CMS integration: direct WordPress staging and automated publishing, including existing content refresh
- Decision timeline: by Thursday next week; kickoff 3–4 weeks out; Q2 results target

---

## Key Topics

### Coralogix's Current Content Structure and Gaps

Product marketing managers handle written SEO content; DevRel team contributes technical blogs and videos (ghost-written by PMMs). The team uses AI to customize existing content but lacks hands-on SEO writers. Ishaan ran the site through Semrush's AI visibility tracker post-launch and identified schema gaps — meta tags and descriptions were backfilled using AI after the June/July 2025 website rebuild. Next priority: FAQ-style content for ChatGPT AI Overviews.

Ishaan flagged a key constraint: comparative content (e.g., "Datadog vs. Coralogix") requires legal review before publishing. Tyler confirmed GrowthX supports multiple rounds of review and recommends creating separate site sections (not the main blog) for this content to avoid cluttering navigation while still capturing SEO value.

### GrowthX Platform Walkthrough

Tyler walked through the full GrowthX methodology:

**Phase 1 — Strategy Sprint:**
- Deep keyword universe analysis (volume, AI search, difficulty)
- 3–6 month content roadmap at five articles per week
- Topic cluster mapping to build authority in target areas
- Persona artifacts: fears, motivations, trust factors — mapped per buyer title
- Writing guidelines: terminology, structure, good/bad examples
- All artifacts generated from website scan + client resources; V1 ready even without client input

**Phase 2 — Scale:**
- Five calibration articles reviewed with client to hit quality bar
- Then scale: workflows run autonomously with human review in the loop
- Editors use the platform to speed up, not replace, their judgment

**Workflow architecture:**
- Built on Temporal; AI coding agents + file system
- Steps: research plan → bibliography → first draft → cross-linking → metadata → fact-checking → image generation
- Models used: Claude, OpenAI, Gemini, Google; research tools: Exa and Tavily
- Workflows are client-specific — custom prompts at each step, constantly evolved
- CMS integration: direct WordPress staging and automated publishing; existing content can be refreshed via the same pipeline

### Case Studies Shared

- **Augment Code**: 20K → 70K monthly organic; near-zero paid spend; 130+ technical guides with code snippets; GrowthX created their guides, tools, and learn site sections
- **SentinelOne**: Custom vulnerability database — a page per CVE, optimized for search
- **Lovable**: Templates section with API-generated app previews
- **Ramp**: Vendor directory and per-diem calculator using internal spend data — programmatic, data-driven content

### Decision and Timeline

Brian expects the team to align on a decision by Thursday next week. Marcel and Tyler are traveling to Boston that week. Follow-up meeting with Marcel is tentatively Friday. Tyler offered one-on-one or small group sessions with Katie, Emma, and Ishaan before the Marcel meeting. GrowthX is opening an additional kickoff slot so Coralogix can start sooner if they decide quickly.

---

## Decisions & Commitments

**Partnership Decision:**
- Brian (Coralogix) to confirm partnership decision by Thursday next week
- Follow-up meeting with Marcel scheduled for Friday next week; Tyler and Marcel will be in Boston

**GrowthX Commitments:**
- Open additional kickoff slot to enable Coralogix to start sooner if they decide quickly
- Perform website scan and content audit to generate V1 strategy artifacts
- Support multiple review rounds including legal vetting for comparative content
- Configure direct WordPress CMS access for staging and automated publishing
- Self-serve platform access available month 2–3 of 12-month engagement

**Coralogix Commitments:**
- Provide website resources and documentation for artifact refinement
- Create separate site sections for legally-reviewed comparative content (e.g., "Datadog vs. Coralogix")
- Coordinate internal review process with legal team for sensitive comparative content

---

## Open Questions

- **FAQ-style content:** Coralogix priority is ChatGPT AI Overviews optimization via FAQ content
- **Developer relations integration:** How will DevRel team's technical blog contributions integrate into GrowthX publishing workflows?
- **Community content:** Coralogix interested in Reddit/community-led content; GrowthX focusing on owned channels (Coralogix website)
- **Self-serve timeline:** Exact feature set and timing for month 2–3 self-serve platform access to be clarified

---

## Action Items

**Brian Mullen (Coralogix)**
- Finalize partnership decision and confirm by Thursday next week

**Tyler Pavlas (GrowthX)**
- Schedule follow-up meeting with Marcel and Coralogix team for next Friday
- Offer one-on-one or group meetings with Katie, Emma, and Ishaan before the full-team call

**Coralogix (Katie McCoole, Emma Mock, Ishaan Bhardwaj)**
- Prepare and compile relevant website resources, documentation, and brand guidelines for artifact creation
- Coordinate with legal team on review process for comparative content

**GrowthX**
- Perform website scan and content audit to develop V1 strategy artifacts and keyword roadmap
- Configure WordPress CMS access for direct staging and automated publishing of refreshed and new content

---

## Transcript

**Tyler Pavlas:** This meeting is being recorded.

**Tyler Pavlas:** Hey, how's it going?

**Ishaan Bhardwaj:** Good. How's it going?

**Tyler Pavlas:** Yeah, it's going well. Ishaan, am I pronouncing your name okay?

**Ishaan Bhardwaj:** Yep.

**Tyler Pavlas:** Fantastic. And looks like you joined Coralogix not too long ago. About six months in.

**Ishaan Bhardwaj:** Yeah, about six months in, yeah.

**Tyler Pavlas:** Nice, nice. Have you been in like more of the technical space at your prior roles or is this a more technical company than the past?

**Ishaan Bhardwaj:** I've been on the agency side for almost three years prior to this.

**Tyler Pavlas:** Oh, amazing. Where were you helping them out on the agency side?

**Ishaan Bhardwaj:** Marketing operations, Revenue operations side.

**Tyler Pavlas:** Okay, nice. Are you a HubSpot or a Salesforce fan?

**Ishaan Bhardwaj:** Honestly, these days I don't know. HubSpot has become a weird AI first company, so it's like, I don't know where it's headed. Salesforce has always been, you know, pretty standard.

**Tyler Pavlas:** Yeah, for sure. I've used both in my career and it's like apples and oranges, right? As long as you can forecast your pipeline correctly, you don't get in too much trouble. Great to meet you, Emma. Katie, good to see you again. Brian, thanks for bringing the team together.

**Katie McCoole:** Nice to meet you.

**Emma Mock:** Good to meet you.

**Tyler Pavlas:** Yeah, you too. Great.

**Brian Mullen:** So I think we have everyone here, Tyler, just going to be you from your side.

**Tyler Pavlas:** Yeah, just going to be me from our side. But Marcel mentioned if we needed to do a follow up where the team could kind of go through some Q and A, we can definitely do that. Thought it would be helpful, you know, since this is the first call making sure that they had a good overview and introduction to everything we're doing here first.

**Brian Mullen:** Yeah, great. Well, let me give a little context for our meeting today. So this is more — I don't know if you guys already did intros, but we can do those in just a second if we haven't. I wanted to bring our demand and analytics and SEO team together. So this is it. We've got Katie and Emma and Ishaan and really I just wanted to kind of expand on the conversation I had with Marcel the other day and I'd love to have you guys just kind of give the team — or you, Tyler — give the team an overview of kind of what the purpose of GrowthX is and exactly kind of what you guys do in terms of surfacing Personas and behaviors and trends from our website so that can be used across, you know, put into other efforts that we have. So that was kind of like the gist of what I talked about with Marcel, which I thought was like a good framing for what you guys do and how it would be useful for us. So I'd love for the team — I was hoping you could just kind of walk through that and treat this as like an explainer meeting.

**Tyler Pavlas:** Yeah, that sounds perfect. We'll go super deep today. And as a quick intro, I'm the founding AE here at GrowthX. So I work hand in hand with our CEO Marcel, who Brian has had the chance to meet, and happy to bring him in on a later call, but would love to just do quick intros. Emma, Katie and Ishaan — with you and maybe like the thing you're most looking forward to learning over the next 27 minutes.

**Katie McCoole:** Perfect. I'm Katie, I've been with Coralogix for almost three years now running Demand Gen North America and some of EMEA with the digital marketing side of things. Have Emma here on my team managing North America. Well, I guess Emma, I should let you do a self intro so I can pass it over to you.

**Emma Mock:** I'm Emma, I've been at Coralogix about a year and a half and my role as a marketing campaign manager is a little bit field and a little bit digital and then working full time to move over to like full time campaign launch across all the different channels. So a little bit of this, a little bit of that and then we have the lovely Ishaan. I'll pass it over to you.

**Ishaan Bhardwaj:** Thank you so much. Hi Tyler. So I've been with Coralogix for a little over six months now. I'm helping manage the analytics side of things, also kind of managing marketing operations, handling Marketo and then also managing the organic SEO side of things as well. So, you know, a little bit of here and there as well.

**Tyler Pavlas:** Perfect. Yeah, great, great to meet the team and high level, you know what we're doing at GrowthX — think of us as like an extension of your content team. So we are end to end as a partner. We'll help you identify the right strategy for SEO and AEO and then for all of our clients we're actually publishing or refreshing content on a daily basis. So that's I think one key piece — just this idea of how do I scale with quality? AI search needs more content, you need to keep that content nurtured and up to date. But a lot of times teams trying to use AI workflows — it just takes a super long time to get to quality. And what we can do is we can basically help you hit the ground running with your existing content and with new content. And the goal is that we're driving AI search visibility and seeing that all the way through to conversions. So we'll do all the LLM monitoring and visibility. We actually just launched our platform for all of that. And what I'd love to just quickly learn is like who are the content creators today? Do you work with external partners? Is it done in house? And I'm talking like SEO AEO content — think editorial on your blog typically or maybe other parts of the site.

**Katie McCoole:** So that would be our product marketing managers handle most of the written content. Sean and myself have written a few things but definitely need some more hands on writers to help support SEO in that sense.

**Emma Mock:** A touch of the developer advocates as well. Sometimes on the devrel side a lot are ghost written by the product marketers. But like one of our devrel just wrote an ebook so they sometimes also get involved.

**Brian Mullen:** And I would say looking forward, this hasn't happened yet, but we have a super strong devrel team and so I think our plan this year will be to do a lot more content, you know, some of which will be manufactured with some AI help but a lot of it will be personalized and we'll try to go quite deep on technical topics. And so we're going to lean heavily on the devrel team that's in place — both in the US and the UK — to write blog posts and also do technically oriented videos that'll be YouTube, a few minutes at a time, sometimes longer form. So they'll be increasingly the voice.

**Tyler Pavlas:** Makes sense. You're selling to developers at the end of the day so definitely want to resonate with the level of technical depth in the content that you're creating. Katie, is the team using any AI tools to create content or as part of the process currently?

**Katie McCoole:** From our side when Ishaan and I create it's mostly taking what we currently have on the website, customizing it using AI, but then really going back and customizing it from there to have more of the Coralogix brand tone. From the devrel's PMM side I assume they're probably leveraging AI and then going back and fixing it where it makes sense.

**Tyler Pavlas:** Okay, makes sense. And I guess when you split up the work — is it really like the less technical, more just search optimized content falls on you and Ishaan's plate and then higher technical bar is the devrel team and product marketing?

**Ishaan Bhardwaj:** To give you a little bit of background, the website that Coralogix has was updated somewhere last year in June or July. And then when the website was launched, some of the key things like meta tags, H1, H2 descriptions and all of that were kind of not there. So we leveraged AI to do a backfill of it. And then what I did was I ran the website through Semrush — they have that AI visibility tracker — and kind of established that these are the areas where we are missing. We are mentioned in search, especially AI overview searches, but not that often. So we started creating content using AI to specifically focus towards making sure we can fill out those content schemas that they're looking for now. Like the next evolution of that would be to have FAQ style content so that as you know, ChatGPT also consumes a lot of FAQ style of content. So basically creating that.

**Tyler Pavlas:** Nice. Yeah, I think what our partners really like — and I'll get into more of the examples and how the content's created next — but just really this idea that like the burden and the time intensive aspect of having to create so much content, we offload that from your team. A lot of times it's, you know, you're reviewing drafts, you're focused on more of those strategic pillar pieces of content, annual reports, ebooks, things of that nature. And I think when Marcel and I were looking just at the pages that are indexed from the blog today, there's already just some low hanging fruit when it comes to refreshing content. So all of the blog pages that are driving the most traffic — it looks like most of them were updated two, some three plus years ago. And just simply refreshing some of these pages could get some quick wins and would be easier for us to do right away, but we'll also do a lot of net new content creation. So just wanted to point out that there is actually a lot of easy refresh opportunities on the site which I'm sure you're probably aware of as well.

**Ishaan Bhardwaj:** Yeah, yeah, we could use a refresh. A lot of these are from 2021, 2022, but they are getting indexed — it's just that anyone who lands on it would be like, they didn't update it?

**Tyler Pavlas:** Exactly, exactly. And so, you know, I told you a little bit about our partnership process, but one thing that differentiates us is that our founder and CEO Marcel has really been an organic content focused marketing leader at every stop in his career. So he's never had big paid ad budgets. He's got a story — and I'll let you watch a video where he explains it about the content engine — he stood up at each one of these organizations and the thing that's been great is that at every organization, the content engine had a huge impact on their pipeline, right, on their revenue goals. And so think about Hashicorp going through their hypergrowth phase, ServiceTitan, same thing, ScaleAI — he was the CMO as they were getting acquired by Meta. And then at Deepgram, what Marcel did was he experimented with building these workflows in AirOps to really figure out how fast could you accelerate the process, where can you actually automate and what do the dividends look like when you look at content performance — and they 24x'd their traffic over 18 months, they 4x'd their revenue. And GrowthX really started because Marcel was hosting these workshops explaining how he built the workflows and realized that people didn't need help learning how to build the workflows, they needed help actually having someone come in and build them. And so that's how GrowthX started — Marcel leaving his CMO job at Deepgram and really starting a team here that can take this on end to end so that you don't have to stitch together all these different tools, but that you can actually benefit from what we're building. So we're opening up our platform to our clients. We'll give you the ability to execute using our workflows. But we started off with everything as a service. That way before we launch products, we can learn across the 70 plus clients that we're working with and we can make sure that the pipelines — we call them pipelines for the workflows — are really optimized so that when they're in your hands, you're not having something that we're constantly making updates to on a weekly basis. Any questions? I'll get into some content examples next, but hopefully this gives you some good background.

**Ishaan Bhardwaj:** So in terms of community led content, like Reddit, for example — do you also support that kind of content play as well?

**Tyler Pavlas:** It's a great question. We're just super bullish on the channel that you can control, the owned channel where people are going to go to get more information. If you're showing up in answers as being the most important, doesn't mean we can't help out on Reddit, but the focus would definitely be your website.

**Ishaan Bhardwaj:** Got it.

**Tyler Pavlas:** And so getting into some specific examples here — Augment Code, it's probably one of my favorite examples to show. They're in the AI enterprise coding space. They compete against GitHub and Cursor. When they started working with us they were around 20K monthly organic and were spending quite a bit on paid. Now they are closer to 70K — so 3x that number — and almost tapered off paid ad spend. And so you know, this is on the traffic, the SEO side. But when you think about AI answers, this is the search that they care the most about: "What are the best AI coding tools for enterprises specifically?" And what I really like about this is we position them in the answer the way they want to be seen. We're the best for large complex code bases. We have this context window that can understand better than our competitors. And what I also like is you see a piece of content that we created cited as the answer next to GitHub and next to a few other competitors. And so how did we generate these types of results? The way that we go about that is we're super audience first and we split our engagements up into two phases. Phase one is the strategy sprint where we develop these artifacts to give our workflows the context necessary to be hyper personalized. And then phase two is when we actually scale out from articles that we calibrate on to make sure we're hitting that quality. So with Augment Code we've created over 130 different guides that are pretty technical — a lot of these will have code snippets in the content. We're cross-linking to the most relevant articles across their site. This is just a sample of what's driving that traffic and that visibility. For Augment, it's the guides, it's the tools section of the site that we created where we're doing comparisons and listicles, and then it's also this learn section where we're doing more thought leadership. And so this can really evolve in the partnership. We start off on editorial because it's an important foundation. But then for SentinelOne we actually created a vulnerability database where we built a custom pipeline and we even did the design and the development. So in that scenario, it's basically logging a page for every vulnerability and then we optimize it for search. Some other examples outside of editorial — we've built all the templates for Lovable where we use their API to actually go in and generate an app that a visitor could preview or remix. And then for Ramp, we had done their vendor directory and also a per-diem calculator that uses their internal spend data to populate pages programmatically. Any questions about use cases?

**Ishaan Bhardwaj:** No, I think this looks good to me. I think one of the other areas — like for example when we create comparative docs like Datadog versus Coralogix and certain things like these, where we also need legal to step in and make sure it's within their framework and ensure we are not stepping on anything that could be IP of Datadog. So is there a process where content can be vetted before it goes live? Like, basically it's in draft mode that we can share with legal, get it checked, make those edits — or would it just go, the moment the AI kicks in, it'll just generate and publish the content?

**Tyler Pavlas:** Absolutely, is the short answer. All of our clients can have multiple rounds of review. We want to make sure it doesn't become a bottleneck to driving results. And not every piece of content we create is going to be the most technical content. Some is just going to be related to keywords and searches where we can win against your competition. And I think as well, sometimes what helps there is like with Augment Code, they reserve their blog for their technical writers, their product information, and company announcements. But then they set up these different sections in the site, in the footer, so that it's not congesting their main navigation, but it is getting all the benefits of content being indexed and showing up in searches.

**Ishaan Bhardwaj:** Got it. Yeah, that sounds like a good plan to have a separate section.

**Tyler Pavlas:** Yeah. And so getting a bit more tactical into our process in phase one. The first thing that we do is we're diving super deep into the keyword universe. So yes, AI search is a little different but always good to actually look into the search volume that we can quantify and where the keyword difficulty may be lower against competitor pages. And from here we're creating a roadmap of assignments, about three to six months of content at that five per week clip. And then we're connecting it all to different topic clusters where you want authority. And then as we start to get content approved, we prioritize based on one, either where we think is going to drive the most results or two, by collaborating with you to understand what the top content priorities might be. And from there we're sending over drafts. So it's really you get five drafts each week. We'll have weekly meetings and then we'll do feedback async and in sessions if helpful so that we can continue to optimize our engineering and what we're doing here. And this is also happening in week one. That's kind of the name of the game for us. We want to move super fast without breaking things. We create those artifacts. And so with Engine we created persona artifacts across all those different industries and we went super deep into everything that the titles they care about are thinking when it comes to business travel. So everything that you're seeing here, it's a business travel related fear or motivation or what's going to win their trust or lose their trust. And then we connect it back to the client and we do the same thing for the finance manager, the project manager. And this will feed into each piece of content that we create along with artifacts like the writing guidelines — good and bad examples, what terminology should we use or not use, how should we structure the content. What's great about this is that we have a point of view on the V1 for these artifacts. It's not something that you need to spend a ton of time finding the right examples for or thinking about how can we make this perfect before we start. We get a lot of that and then build it in through the feedback that you give us on those calibration articles. Katie, Ishaan, any questions about the context engineering?

**Katie McCoole:** Will you scan our website for this or do we have to upload everything into this engine?

**Tyler Pavlas:** Great question. There's a couple resources that we request ahead of the kickoff and then we also will scan your website and be able to generate a V1 of the artifacts with or without resources from you. They just help us refine the artifacts versus one shot with just looking at your website.

**Katie McCoole:** Okay, sounds good.

**Ishaan Bhardwaj:** Could we also self serve? Let's say there are certain pieces of content that I want to create for myself — could I self serve with the platform or can I just send it to you guys saying we need these five or six pieces of content?

**Tyler Pavlas:** Definitely in the 12 month term that you guys would be signed up for — probably closer to like month two or month three. I know that's our number one priority right now, but right now we're just using what you're seeing here internally. We're creating and revising the artifacts and then we're standing up these different pipelines that are producing different types of content. So to get into one of the pipelines specifically — let's just use a simple example, we'll go with the guide from Lovable. We've created all these different guides across different topic clusters. So for this guide — "How to start a gym business" — what is happening is we have different steps in the process, from agentic research to drafting an article, cross-linking, optimizing the metadata, validating against writing guidelines and fact-checking. We also have image generation, so cover images, even in-content images or infographics. And so what we do is we leverage those inputs — the writing guidelines, the personas — and then we use some different tools. For deep research, we'll use Exa and Tavily in addition to the best models across Claude, OpenAI, Gemini, Google. And then in the background we've built all our workflows in code so we can actually customize them client by client or build in unique steps to the process. So for this researcher, it's generating a research plan first for the topic that we're writing about. It's creating an objective, a bunch of research questions to answer, success criteria, source requirements tailored to be more authoritative sources that have authority. And then it is executing the research, coming up with a full bibliography across all those different sources that we use, and then evaluating the quality so that if it doesn't hit a certain threshold, it will rerun the research. And then as we move into the next step, it's taking all of that research and the writing guidelines to draft V1 of this article, where our experts in the loop are making changes throughout the content before it ever hits your desk. They're using the platform to speed up the process to get more personalized. And what's great about this as well is that we've built the workflows to be client specific. So for Sentinel One, for Webflow — we've ingested all their docs to enhance their existing integrations pages. We can definitely do that for you in the partnership and we can think about where are those areas that we can fit in outside of blog content, editorial content — what's a programmatic use case we might be able to execute on? And for each step in the process we also have a very complicated prompt that's being used in tandem with those inputs. My goal here is — I know that AI can be a bit of a black box and especially agencies using it for content creation — I just want to highlight how each step in the process there is a workflow that has been tried and tested across our clients, that is constantly being evolved, that represents each step in the content creation process here. And the last thing I'll just kind of say — with Augment Code, we actually start with the draft or with a template first. So we have an artifact that basically puts the content into a template and then in the next step it's actually going to create the article but use the writing guidelines as a supplemental input. This is one where we actually publish directly to their CMS as part of the workflow after we've gone through the review process. Their image generation is also a bit more on brand and enhanced because of the work that we've done over time. So yeah, there's a lot to unpack here, but happy to answer any questions.

**Ishaan Bhardwaj:** So this links to CMS. So for example if we are on WordPress, can we link it and just push content directly to WordPress? And let's say — you showed towards the beginning of our meeting that one piece of content which was written in 2022 — if we were to refresh it, we could just take that into your system, refresh it and push it to the CMS and it'll get updated. Is that the flow that we can expect?

**Tyler Pavlas:** Absolutely. We prefer to just get access to your CMS so we can stage and publish for you. And then if we have that access, then we can automate the publishing step pretty easily as part of the workflow.

**Ishaan Bhardwaj:** Got it.

**Tyler Pavlas:** Brian, I'm sure you probably have to run pretty soon — in terms of just timeline, I want to make sure everyone feels super confident, but also balance our kickoff calendar. Help me just kind of understand, like, when you were thinking about the partnership making the most sense, if you decide to move forward.

**Brian Mullen:** Sorry. Just when we met in person — it sounds like it's about a four weeks out when you guys could start at any given time, right? Around that time, more or less.

**Tyler Pavlas:** We're opening up an additional kickoff slot. So I think that's going to help a lot if you want to move sooner rather than later.

**Brian Mullen:** So I think we're all getting together next week. I think this is definitely something we're talking about. And I think we also came to make some bets or do some experiments, particularly on the geo stuff. And so we probably need about another week or so to kind of decide how we want to go forward. So I'd say like, by, you know, call it Thursday next week, we'd probably have a good sense. And then from there we'd try to just adhere to whatever your timeline is. Like if that's three weeks out or four weeks out, whatever probably is workable for us. I think we'd get going quickly, but we'd probably be expecting it to start hitting in Q2 — like the actual results of it.

**Tyler Pavlas:** I think that's perfect. And why don't we throw a meeting on for next Thursday — I'll definitely make sure Marcel comes.

**Brian Mullen:** So we need one extra day. So Thursday is okay.

**Tyler Pavlas:** Could we do Friday?

**Brian Mullen:** How about Friday? Because we — this team is mostly in Boston, but Brian and I are traveling to Boston for like three days next week. So that's like Tuesday through Thursday. So if Thursday doesn't work, let's do Friday.

**Tyler Pavlas:** Okay, sounds good. I'll connect with Marcel and I'll send you some specific times. And before then, Katie, Emma, Ishaan, if you want to do a one on one, a group meeting, happy to do that before the Marcel meeting too.

**Katie McCoole:** Perfect. Thank you so much.

**Emma Mock:** Great.

**Tyler Pavlas:** Great to meet you all. Thanks team. Hope this was helpful. See ya.

**Ishaan Bhardwaj:** Thanks.

**Brian Mullen:** Thanks, Tyler.
