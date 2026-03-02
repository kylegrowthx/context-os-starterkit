# Hyperexponential <> Growth X - Weekly Sync

<metadata>
date: 2025-10-07
time: 18:01 UTC
duration: 30 minutes
organizer: team@growthxlabs.com
participants: David Spitz (Hyperexponential), Aida Knezevic (GrowthX), Bailey Seybolt (GrowthX), Erik O'Brien (GrowthX)
fathom_recording_id: 92476548
fathom_url: https://fathom.video/calls/432469867
share_url: https://fathom.video/share/F18G1txoe81a3zsJoJJ-aQShEge_z_r3
source: fathom
enriched_on: 2026-03-02 18:45 UTC
</metadata>

---

## Summary

GrowthX and Hyperexponential discussed deploying an agentic AI pipeline to improve content quality and reduce editing overhead, with the goal of reaching five articles per week. Bailey Seybolt (new managing editor) presented findings from the calibration blog — the standard pipeline gets content 70-80% there, but needs additional research supervision, question prioritization, and quality scoring. The team approved article topics around submission triage and underwriting workbench (a vague category that David positioned as distinct from full workflow management), but identified a need for more top-of-funnel keyword research and product positioning guidance from a marketer. David committed to sharing product training recordings and industry analyst content to generate more article ideas.

---

## Context

Hyperexponential (HX) is an insurance technology company offering decision intelligence for underwriting workflows — specifically AI-powered ingestion and recommendations (approve/deny/price), distinct from full workflow management systems. GrowthX is executing a content marketing engagement for HX, with Bailey recently joining as managing editor. The team has been iterating on article production, starting with a calibration blog to test the effectiveness of GrowthX's standard AI content pipeline. The calibration work revealed that while the initial pipeline produces decent raw content, Hyperexponential's specialized insurance domain (underwriting, triage, portfolio optimization, regulatory concepts like IFRS and solvency) requires deeper research and stricter quality control to avoid generic or misaligned positioning.

---

## Relevance

**To GrowthX Delivery:**
- Deploying agentic AI pipeline with research supervisor, quality scoring, and knowledge gap detection — a significant methodological advancement beyond the standard pipeline. Includes web scraping, API integration (Perplexity, others), and structured research prioritization.
- Bailey's 10 years of B2B SaaS content + recent AI services work directly applicable to specialized insurance domain.
- One article ready for review this week; three more by end of week. Publishing goal is 5 articles per week.
- Identified need for product marketer input on positioning (HX as decision intelligence, not workflow management) — may require adjusting engagement scope or adding resource.

**To CheckThat / AI Visibility:**
- Low-volume, high-intent keywords ("submission triage in insurance", ~20 searches/month) are good AEO targets — less competitive, higher ranking likelihood in LLM outputs.
- GrowthX is explicitly strategizing around LLM optimization (AEO/GEO) alongside traditional SEO for topical authority.

**To GrowthX Business Development:**
- Client is willing to invest in methodological improvements and product positioning work — signals confidence in partnership.
- David's mention of subscribed industry analyst group suggests HX has budget for premium research sources; potential to position GrowthX as aggregator/analyzer of that content for future clients.

---

## Overview

- GrowthX is implementing an agentic AI pipeline to improve content quality and reduce human editing needs
- One article ready for review today, with 3 more expected by end of week
- Need for additional keyword research to target top-of-funnel content
- David to provide product training recordings and industry analyst content to inform future articles

---

## Key Topics

### Team Introduction

  - Bailey Seybolt introduced as new managing editor leading content editing and generation
  - Bailey has 10 years of B2B SaaS content experience, including recent AI services work

### Content Production Updates

  - Calibration blog finalized based on previous feedback
  - Standard AI pipeline getting content 70-80% there, but needs improvement
  - Implementing agentic AI pipeline with additional steps:
      - Research supervisor workflow
      - Prioritized question generation
      - Multiple research APIs and web scraping
      - Research quality evaluation and scoring
      - Addressing knowledge gaps
  - Goal: Reduce repetitive information and improve content specificity

### Keyword and Content Strategy

  - Mix of low volume, high intent keywords (e.g., "submission triage in insurance")
  - Focusing on product feature-related content to build topical authority
  - Approved topics: submission triage, underwriting workbench
  - Need to balance definitional content with product positioning
  - Exploring underwriting workbench sub-topics (history, types, etc.)
  - Aim to target different funnel stages, with more focus on top-of-funnel content

### Product Positioning and Content Creation

  - HX offers decision intelligence rather than full workflow management
  - Need for product marketing input to accurately position HX in relation to underwriting workbenches
  - Plan to create product feature matrix and competitor comparison tables
  - David to provide product training recordings for content team reference

### Content Publication and Design

  - Awaiting design team feedback on featured image examples
  - Exploring Framer integration requirements (MCP vs API)

### Expanding Content Ideas

  - Need for more article topics to meet 5/week goal
  - David to share industry analyst content for potential article ideas
  - New Airtable tab created for "David's Content Suggestions"

---

## Action Items

**Aida Knezevic (GrowthX)**
- Work with engineering team to set up agentic pipeline for HX content production

**Bailey Seybolt (GrowthX)**
- Conduct additional keyword research, factoring in Franki's comments regarding top-of-funnel content

**David Spitz (Hyperexponential)**
- Find and share product training recordings (including older ones) for GrowthX team
- Export titles from subscribed industry analyst group and add to "David's Content Suggestions" tab in Airtable

**Erik O'Brien (GrowthX)**
- Connect GrowthX team with Mark (HX designer/Framer expert) to discuss Framer MCP vs API requirement

---

## Transcript

**David Spitz:** I saw you sent a note somewhere, but, oh, was it in Notion?

**Aida Knezevic:** Yes, I put the agenda over Notion.

**David Spitz:** Okay, go.

**Aida Knezevic:** So I can actually share my screen as well.

**Aida Knezevic:** Yeah, so I wanted to introduce Bailey first.

**Aida Knezevic:** I mean, she introduced herself over Slack, but she's a new managing editor on our team, and she's leading the content editing and content generation process for Hyperexponential.

**Aida Knezevic:** Bailey, you want to do a quick intro as well?

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** Hi, it's really nice to meet you.

**Bailey Seybolt:** I'm happy to be here and on the GrowthX team.

**Bailey Seybolt:** Just to give you a little bit of background on me, I've worked in content in various forms as a copywriter, as an editor for mostly B2B SaaS companies for the last 10 years or so.

**Bailey Seybolt:** So companies like Greenhouse and a mix of in-house and also more agency-style writing.

**Bailey Seybolt:** So I worked at a content marketing agency.

**Bailey Seybolt:** And then most recently, I was running sales enablement content at an AI services agency.

**Bailey Seybolt:** So a mix of experience there.

**David Spitz:** And I'm very happy to be here today. You're based on the East Coast, right?

**Bailey Seybolt:** I am. I'm based in Vermont, actually.

**David Spitz:** I'm originally from New York City, but now I'm up in Vermont.

**David Spitz:** Oh, yeah.

**David Spitz:** Cool.

**David Spitz:** I'm from New York City also.

**Bailey Seybolt:** I'm Connecticut, so.

**David Spitz:** Oh, nice.

**Bailey Seybolt:** Are you having some, like, very summery weather, too?

**David Spitz:** It's, like, just gorgeous up here.

**David Spitz:** Yeah.

**David Spitz:** Yeah, definitely.

**David Spitz:** Did you go to the Exit 5 conference a couple weeks ago?

**Bailey Seybolt:** You know, I was traveling.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** It was, like, I think it was actually happening where I do my co-working, so I got, like, the last day, but I was out of town for most of it.

**David Spitz:** Okay.

**David Spitz:** Yeah.

**David Spitz:** Not too many conferences in Vermont.

**Bailey Seybolt:** No, there's not.

**David Spitz:** Yeah, great.

**Aida Knezevic:** Nice.

**Aida Knezevic:** All right.

**Aida Knezevic:** So, yeah, just to give you kind of a quick update, you we didn't meet last week.

**Aida Knezevic:** So, we spent last week sort of dialing in the calibration blog.

**Aida Knezevic:** You've given us your feedback there.

**Aida Knezevic:** And what we found last week while, especially while Bailey was editing the content, was that the standard article generation pipeline we have can get the content, like, 70 or 80%.

**Aida Knezevic:** But we still need like an additional push from the AI to not require as much like human editing so that we can really scale this to a level where you're like getting five articles per week.

**Aida Knezevic:** So because there's just, you know, the standards of your industry and also just the, you know, we want to be able to position the content in a way that aligns with the product messaging that we discussed in our last meeting.

**Aida Knezevic:** Um, we are setting up an agentic pipeline for you, which, um, is similar to the pipeline that we have for you already, but it includes a couple of extra steps where the AI reviews its own work according to guardrails that we implement.

**Aida Knezevic:** So to show you one of the biggest aspects of the, uh, parts of the agentic pipeline is the researcher step.

**Aida Knezevic:** So, um, this is the standard researcher step, but

**Aida Knezevic:** Just wanted to show you so you have something to compare it again.

**Aida Knezevic:** So the standard research step, it follows the assignment brief, and it takes the assignment brief, and it generates targeted questions, it searches across specific domains, and then it combines the findings into a markdown document.

**Aida Knezevic:** And it uses perplexity usually for that purpose, it might use some other APIs, but it uses perplexity, and that's it.

**Aida Knezevic:** The research document is ready, and there are no extra steps after that, and this suffices, this is, like, good for clients that are really, not in a very, like, I mean, demanding, like, very specialized industry.

**Aida Knezevic:** For you, however, we found that it would be better to have an agentic researcher set up, so this is how it's different.

**Aida Knezevic:** So the research supervisor workflow, it first generates a research plan, so it has a list of prioritized

**Aida Knezevic:** questions based on the Claude model.

**Aida Knezevic:** And these questions are set up to make sure that it collects enough information about a specific topic.

**Aida Knezevic:** So it also includes like an audience analysis.

**Aida Knezevic:** And this is like the first step.

**Aida Knezevic:** And then it executes the research questions.

**Aida Knezevic:** So it's going to use web scraping, URL analysis.

**Aida Knezevic:** It's going to use different research-specific APIs like Perplexity.

**Aida Knezevic:** But there could be additional ones depending on need.

**Aida Knezevic:** And then it's going to synthesize those research results.

**Aida Knezevic:** And then it organizes them based on the priority and how confident it is in the quality of the research.

**Aida Knezevic:** So it's not just — not all research is the same, and it's not all of the same quality. This step makes sure that the research is actually graded according to the quality of the information. Then it goes back and evaluates the research quality according to the original instructions that our engineers implemented in the first step.

**Aida Knezevic:** And then it grades the research.

**Aida Knezevic:** And it generates a quality score from zero to one.

**Aida Knezevic:** And then it also asks questions, okay, are there any knowledge gaps in this research document based on who the initial audience is?

**Aida Knezevic:** And if there is, then it's going to go back, ask additional questions, generate additional research.

**Aida Knezevic:** Once the research objectives are met, then it's going to finalize the document and it stores the research in Atlas.

**Aida Knezevic:** So it's going to just give us more information to work with.

**Aida Knezevic:** One of the things that we've been finding that Bailey has been editing is just repetitive information that's been kind of cropping up in different sections.

**Aida Knezevic:** And we want to avoid that.

**Aida Knezevic:** And having this research step is going to help us avoid kind of providing repetitive information. Yeah, so this is something that we are working with our engineering team right now to set up for you, and as soon as it's set up, we're going to move the content production to this agentic pipeline, and we're going to share it with you when it's ready.

**David Spitz:** But in the meantime, Bailey, do you have any other content updates in terms of just what we're delivering this week?

**Bailey Seybolt:** Yeah, so one article we'll be ready for you to review today, and then just to give you sort of like a behind-the-scenes peek, we have run the other articles that you've approved.

**Bailey Seybolt:** We've been running them through the original pipeline, and like Aida said, some of what we're finding is that it gets it right for an insurance context, but like we talked about.

**Bailey Seybolt:** But in the calibration article, it doesn't always, like a general context, it doesn't always do a great job making it highly valuable to the specific audience.

**Bailey Seybolt:** So if it's about tools for actuaries, it really needs that extra research step to understand, I think, the specific actuary context or the specific underwriting and pricing context.

**Bailey Seybolt:** So the reason we haven't delivered those yet is because I think they're just, honestly, they're not ready, I think, at a valuable enough stage to show to you yet.

**Bailey Seybolt:** But it's been very useful for us to kind of pull out the patterns we're seeing and be able to build those into the agentic pipeline.

**Bailey Seybolt:** So we have one that will be ready today and then three more that are kind of in that pipeline that should be ready by the end of the week.

**Bailey Seybolt:** And then, yeah, and then the additional, I saw on next steps, we did capture the comments there on the additional keyword research and sort of the.

**Bailey Seybolt:** Prioritization based on kind of where the keywords are in the funnel.

**Bailey Seybolt:** So we're going to go back and do some additional topics that sort of capture that more top of the funnel content as well and update that.

**David Spitz:** Yeah, I wasn't sure.

**David Spitz:** What was that asked?

**David Spitz:** I mean, think more broadly, let's see, what are we trying to, there's a lot of articles here that we could approve around triage.

**David Spitz:** Just what is submission triage, submission ingestion, they're all sort of variations of the same article.

**David Spitz:** So what would be the goal with that?

**David Spitz:** Are people searching, did we decide that people are searching for that term and we would be generating traffic?

**David Spitz:** Or is it more, you know, to influence the, you know, AEO, GEO that we mentioned?

**Aida Knezevic:** This is both. So to give you a little bit of context, the original keywords that we picked out.

**Aida Knezevic:** So there are a mix of very low volume, but very high intent search queries.

**Aida Knezevic:** Like, for example, submission triage and insurance that's very close to your target audience and your platform.

**Aida Knezevic:** And these are very, like, this is seemingly very low search volume.

**Aida Knezevic:** So it's estimated 20 per month, but it's valuable because it's closely connected to your platform.

**Aida Knezevic:** And we would most definitely rank very highly in search results for this keyword.

**Aida Knezevic:** And this is important.

**Aida Knezevic:** Having content around this would also, like, contribute to your topical authority in traditional SEO.

**Aida Knezevic:** Because Google looks at the totality of the content that you have on your site, especially when connected through internal links, to determine if hyperexponential is an authority on a specific subject.

**Aida Knezevic:** So the more, I always recommend to all clients, we need to have content on your website.

**Aida Knezevic:** that maps to different product features.

**Aida Knezevic:** Even if it's 10 searches per month, we should have content on the site that reflects those product features.

**David Spitz:** Okay, so let's approve those.

**David Spitz:** There's one or two of those.

**David Spitz:** Submission triage, there's another one that's pretty much the same.

**David Spitz:** A little further down, right?

**Aida Knezevic:** Oh, Automate Submission Triage.

**David Spitz:** Yeah, that's the same thing.

**David Spitz:** I mean, maybe that's a slightly different scope, but yeah, same idea.

**Aida Knezevic:** Yeah, different angle slightly.

**David Spitz:** And then there's one around underwriting workbench, a practical guide.

**Aida Knezevic:** Got it.

**David Spitz:** Okay, so now this one is going to be somewhat similar to IDP in the sense that we don't position ourselves as an underwriting workbench.

**David Spitz:** We don't position ourselves in IDP.

**David Spitz:** It's a well-known category.

**David Spitz:** Not well-known, but it's set.

**David Spitz:** but it's a pretty well-established category, so we have to make sure that...

**David Spitz:** Which is similar, where it's not, it has to be very definitional.

**David Spitz:** So with the IDP, I think where we were being too complimentary or too derogatory, I think that took us off course.

**David Spitz:** think just saying like, you know, the what is IDP, and then weaving in, you know, the evolution of the category at the end, is going in these directions without saying too much about, without suggesting that we are an IDP or a modern IDP or anything like that.

**David Spitz:** Under ID workbench is a little less fraught, but I think it's good for us to start to surround that category from a definitional sense.

**David Spitz:** I think you weren't on the call originally, Bailey, but when we talked about, that is one that we come across.

**David Spitz:** We don't come across IDP, it's a very old term, but I think people do search for it, so it was worthwhile doing.

**David Spitz:** We do come across underwriting workbench.

**David Spitz:** There's, I don't think there's ever been like a Gartner report on it, so it's one of these things that like everyone defines it differently, so you know, the sort of spin of the article is more like, you know, underwriting work means a million things to a million people.

**David Spitz:** It's kind of like if you ever came across, I used to work at Imparticle, and we wrote a lot of those things about customer data platforms, and like everyone defines it differently, there's 25 different flavors, and, you know, the interest in the conversation, the surrounding, it's okay that it's like a vague area, it's like a good position within that vague area of interest.

**David Spitz:** I don't know if that's helpful, but there might be more, there might be more articles, I'm saying, around underwriting workbench, that, than we have here, I think we only have one, I think it's a pretty, it's pretty big topic, so there, there might be more of those, more answers.

**David Spitz:** The history of the underwriting workbench, the seven different types of underwriting workbenches, I don't know.

**Aida Knezevic:** Let's take a look, actually, right now.

**Aida Knezevic:** Yeah, those are all great suggestions, and we definitely do, so, like, the first initial batch of topic ideas is just to give you, like, an idea of all of the different ideas that we've come across, and then we refine them as, like, as we go.

**Aida Knezevic:** Okay, keyword overview?

**Aida Knezevic:** No, keyword magic.

**Aida Knezevic:** So, yeah, there's 36 keywords right now that are all related to underwriting workbench.

**Aida Knezevic:** Yeah, what is an underwriting workbench?

**Aida Knezevic:** Features, solutions, AI workbench underwriting.

**Aida Knezevic:** Okay, interesting.

**Aida Knezevic:** Yeah, there's just, there's, I mean, not a lot of, like, search volume, but...

**Aida Knezevic:** Anything with AI in it has a lot more search volume than it says here.

**Aida Knezevic:** that's just based on my experience.

**Aida Knezevic:** Over the past year, we've published a lot of content that targets AI-related keywords in different industries.

**Aida Knezevic:** And we always find that the search volume right now is a lot higher than what Semrush says because this is 12-month data.

**Aida Knezevic:** So it's a little off.

**David Spitz:** And yeah, I don't know how we give you, I'll do a search.

**David Spitz:** don't know that we have good positioning stuff around, we'll probably do somewhere, but our proposition has evolved a lot.

**David Spitz:** So some customers, know, because it's big term, do think of us in the underwriting workbench, but we don't do, yeah, we don't do 100% of what they do.

**David Spitz:** So, I don't know how I, this is the thing, like, you almost need a product marketer to sit alongside you and we're trying to, trying to work.

**David Spitz:** So what would you normally do?

**David Spitz:** you write it 70% and then we'd run it through some product marketing cycles?

**Aida Knezevic:** that how you would try to approach this?

**Aida Knezevic:** Something like underwriting workbench solutions.

**David Spitz:** Yeah, because I could imagine at the end of the article, we'd want to say, well, these things are evolving into XYZ direction, and you might need a product marketer to help you articulate that.

**Aida Knezevic:** Yeah, yeah, yeah.

**Aida Knezevic:** No, so typically, I mean, what we would like to have ideally for these types of blogs is a product feature matrix.

**Aida Knezevic:** So it's a Notion document, and it's quite similar to the artifacts that we have already.

**Aida Knezevic:** And it breaks down your platform and all of the key features that you need to highlight in the content.

**Aida Knezevic:** And then we would also have these different other underwriting workbench solutions with also another quick table overview.

**Aida Knezevic:** of their key features, and that would help us get probably 80 to 90% of the way there, and then you would review it, or someone from the product team would review it, and, you know, just point out maybe some nuances about, like, other solutions, and just generally the industry.

**David Spitz:** Okay.

**Aida Knezevic:** Yeah, so I think the best thing I have is to ask you directly — what products are kind of similar to the other workbenches that are out there?

**David Spitz:** Yeah, I mean, I think all of our products have an underwriter-facing component. The workbench is so ill-defined — it can mean so many different things. In the original definition, it was more like case management, or a CRM for an underwriter. They get a submission and track it through the life cycle: "I routed it to this guy. I put it in comments. He sent that. I routed it." What we offer is more decision intelligence. We focus on the AI ingestion and then giving a recommendation — approve, don't approve, price like this, price like that. But we don't do the workflow bits of routing to Eric or routing to Ava. We do the AI bits of the underwriting workflow, but not the workflow bits.

**Erik O'Brien:** Yeah, because I'm curious if it would make sense if there's a product marketer or product expert who could spend an hour with me to talk through it. We could then use that to create a first version of the matrix Aida was talking about.

**David Spitz:** Yeah, let me do that. I'm sure we have a lot of recordings.

**David Spitz:** I'm sure I could find you our recording somewhere.

**Erik O'Brien:** Okay, that works too.

**David Spitz:** Yeah.

**Aida Knezevic:** That's great.

**Aida Knezevic:** And then, yeah, to just to go back really quickly what you were asking about AI optimization or AEO, GEO, when we're doing, like, low volume keywords like this, this also helps with your AI visibility because low volume content tends to always be, or skews to be lower difficulty.

**Aida Knezevic:** So, there's not a lot of really good quality content out there that talks about these topics.

**Aida Knezevic:** So, if someone does look up something regarding, like, submission treatment,

**Aida Knezevic:** And insurance and chat GPT or perplexity, your blog post is much more likely to appear rather than, you know, if it's a keyword that has a lot of like monthly, you know, just has like hundreds of searches per month, it's way more competitive.

**Aida Knezevic:** So we, that's another way that we can like improve your LLM optimization and yeah, scale it from there.

**Aida Knezevic:** And it's just, you know, we do try to target like different stages of the funnel with these keywords, but Bailey's going to do another round of keyword research, just factoring in Frankie's comments.

**Aida Knezevic:** And then, yeah, we'll share those assignments as well.

**Aida Knezevic:** and yeah, I think anything like from a, that you can share, doesn't have to be super polished.

**Aida Knezevic:** So a meeting transcript, like, like a sales, not a sales deck, I mean, just like a slide deck would be helpful for us.

**Aida Knezevic:** And we can find a way to incorporate that and just build like a Notion doc that we're going to use for, for this type of.

**David Spitz:** Content that's more commercial.

**David Spitz:** Yeah.

**David Spitz:** What was Frankie's comment?

**David Spitz:** wasn't.

**David Spitz:** There's something about upper funnel.

**Erik O'Brien:** Yeah, she sent me an email today.

**Erik O'Brien:** I had her just look through the backlog because she said she was going to miss today's sync.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** And so she just had a point that she's flagged as depth that we lack currently on some of the higher level topics and keywords.

**Erik O'Brien:** And then some of the other down funnel content ideas like IFRS and solvency should be more phase two focus.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** So she just wants to see more, just like more top of the funnel, what is content alongside this more like bottom of the funnel content.

**David Spitz:** Yeah.

**David Spitz:** I think there is some value.

**David Spitz:** Weren't we going to work into about all the funnel content, like comparing this to that?

**Aida Knezevic:** Mm-hmm.

**David Spitz:** Yeah.

**David Spitz:** Again, you need a lot of product marketing input there.

**David Spitz:** But I think the...

**David Spitz:** Yeah.

**David Spitz:** I can download a lot of product training sessions.

**David Spitz:** What you'll have to do is, because the training sessions are all a year old, so they predate some of the newer products, but you have the artifacts on the newer products.

**David Spitz:** So are you able to somehow blend some of what you're learning about the category, like Underwriter Workbench, as sort of, that's your market knowledge.

**David Spitz:** And then you can blend that with our new portfolio of things and talk about how HX supplements your underwriting workbench, as an example.

**David Spitz:** So if I dig deep, what I'm saying is I'll find a lot of stuff, but it won't mention triage or portfolio optimization, which are our two newer products.

**Erik O'Brien:** Yeah, so we'll probably just do the download of the recording that you'd send, and then we'll kind of take the newer stuff and just ask it to update based off that.

**Erik O'Brien:** And we should get pretty close.

**David Spitz:** I think it'll get close.

**Erik O'Brien:** Yeah.

**David Spitz:** Yes.

**David Spitz:** And I just put in the chat — there's content around triage we're going to address now. Data ingestion is sort of like IDP, but it's more the job to be done as opposed to the technology. Triage is what you do after ingestion. And then there's portfolio optimization — once you have a bunch of policies in your portfolio, you want to optimize around those things. That's maybe a less crowded area. I just did a Google search and came up with a little podcast, but maybe there's more stuff from McKinsey or Deloitte about insurance portfolio steering and optimization at a very executive level.

**Aida Knezevic:** Yeah, yeah.

**David Spitz:** I don't know we researched that.

**Aida Knezevic:** Yeah, yeah, for sure.

**Aida Knezevic:** We did some initial research around portfolio optimization.

**Aida Knezevic:** And the search intent around those specific keywords is more investment related rather than insurance related.

**Aida Knezevic:** But I think, Bailey, maybe we could brainstorm some synonyms or try to come at it from a different angle.

**Aida Knezevic:** I think these types of reports that David shared, I think they could be helpful to try to extract related topics and themes that come up.

**Aida Knezevic:** And then we can try to find keywords there.

**Aida Knezevic:** Because I think from what I've seen, portfolio optimization is just dominated by investment content.

**Aida Knezevic:** Not to say that we can't publish this type of content, but it's probably not going to rank very highly for these types of keywords.

**Aida Knezevic:** Because Google is prioritizing content that focuses on investment.

**David Spitz:** So.

**David Spitz:** So.

**David Spitz:** All right.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Okay.

**Aida Knezevic:** And then to give you an idea of what we're also working towards.

**Aida Knezevic:** we would like to start publishing soon.

**Aida Knezevic:** I mean, as soon as we get the sign-off on the calibration blog, we would like to get it published on the site.

**Aida Knezevic:** Did you hear anything from your design team about the featured image examples that we sent over?

**David Spitz:** Who's going to send some feedback?

**David Spitz:** But you're also going to talk to him.

**Erik O'Brien:** Frankie's going to send that over.

**Erik O'Brien:** Yeah.

**David Spitz:** Yep.

**Erik O'Brien:** So our team is looking into the new requirement that Framer has suggested of using an MCP versus their API.

**Erik O'Brien:** So it was new for our team to hear about that.

**Erik O'Brien:** And so they're looking into it.

**Erik O'Brien:** But once I hear back from them, we'll connect them directly with Mark.

**Erik O'Brien:** So two Framer wizards can figure it out.

**David Spitz:** Yeah.

**David Spitz:** So it's funny, like the same guy who is our designer is also sort of our...

**David Spitz:** So when you get them on the call to talk about that, you can often talk about the feedback on the images.

**David Spitz:** Is that right?

**David Spitz:** Could you get the right person on both the people on the call?

**Erik O'Brien:** Yeah, yeah, for sure.

**Erik O'Brien:** And then Frankie mentioned in her update this morning that she was going to pass along Mark's feedback.

**Erik O'Brien:** So we'll at least get some interstitial feedback, but we'll also mention it when we're on the call with him.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Okay, sounds good.

**Aida Knezevic:** All right, I think that's everything I have on the agenda for today.

**David Spitz:** Is there anything else you wanted to discuss?

**David Spitz:** No, I think we just need like more keywords, right?

**David Spitz:** Because we need to have, you know, five a week, you know, so we need more article titles to, you know, target.

**David Spitz:** So I'm trying to think for you what those.

**David Spitz:** Yeah.

**David Spitz:** Areas would be portfolio, pricing transformation.

**David Spitz:** You know what?

**David Spitz:** I just got a subscription to an industry analyst group for the industry.

**David Spitz:** So they'll have a lot of content and maybe there's some way I run that through an LLM to generate article ideas or something.

**Aida Knezevic:** Yeah, sure.

**Aida Knezevic:** I think we can also add a tab in Airtable with just a couple of like columns or you could just drop like a link to those resources or just the title and that could start us off.

**Aida Knezevic:** But we're going to do additional keyword research on our end.

**Aida Knezevic:** So, you know, we're going to come back with like an additional batch for you to go through.

**David Spitz:** Okay, that's what I should do is I should just export almost all the titles that they have.

**David Spitz:** And then we can see if, because this is paid like gated content, so no one can access it.

**David Spitz:** But if we.

**David Spitz:** Do free versions of these articles could be pretty useful.

**Aida Knezevic:** Yeah, I'm just adding a new tab.

**David Spitz:** It's called David's Content Suggestions.

**David Spitz:** Okay.

**David Spitz:** I don't want it to be just my suggestion. I mean, you also need to weigh in if there's any traffic and if it's the right part of the funnel. But at least it'll come from what industry analysts are writing about this niche.

**Aida Knezevic:** Yeah, yeah, for sure.

**Aida Knezevic:** No, that would be very helpful.

**Aida Knezevic:** And we've done this before with other clients.

**Aida Knezevic:** If they're like subscribed to any interesting newsletters, they'll just drop like a link to an article or just like copy paste a section and just be like, okay, can you look up and see if there's something interesting around this topic?

**David Spitz:** And sometimes we can find something.

**David Spitz:** Other times there's nothing there, but it serves at least it's like an interesting data point that we can reference in content.

**Aida Knezevic:** So it's always helpful.

**David Spitz:** Yeah.

**David Spitz:** Okay, perfect. Let's crack on.

**Aida Knezevic:** All right.

**David Spitz:** Talk to you soon.

**Erik O'Brien:** All right.

**Aida Knezevic:** Amazing.

**David Spitz:** We'll keep you in touch.

**David Spitz:** Thanks.

**Aida Knezevic:** Bye.

**Erik O'Brien:** Bye-bye.

**Erik O'Brien:** Thanks, David.
