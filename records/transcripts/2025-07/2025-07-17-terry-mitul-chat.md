# Terry/Mitul - Chat

<metadata>
date: 2025-07-17
time: 17:30 UTC
duration: 17 minutes
organizer: Dave Capone (dave@growthx.ai)
participants: Dave Capone (GrowthX), Mitul Gandhi (seoClarity), Terry Maturo (seoClarity)
fathom_recording_id: 74879968
fathom_url: https://fathom.video/calls/355957133
share_url: https://fathom.video/share/LZ1hrKx1Auos7e43FKxH57QKTub29zS6
source: fathom
enriched_on: 2026-03-03 14:30 UTC
</metadata>

---

## Summary

Dave Capone from GrowthX discussed the current SEO tool situation with Terry Maturo and Mitul Gandhi from seoClarity, evaluating a potential transition from SEMrush to seoClarity. GrowthX is paying $72K annually for SEMrush's business plan (tracking 2,312 keywords with 40 users) plus another $167K monthly for API usage in their content creation workflow, while facing user limitations and sampling issues in their client reporting through Looker. seoClarity proposed offering 25K keywords (10x more), unlimited users, unsampled data, customizable dashboards, and API access—all for less than current spend if GrowthX keeps a minimal $350/month SEMrush account for existing API workflows. The team agreed to move forward with comparison documentation and API integration details before presenting to GrowthX leadership.

---

## Context

GrowthX is a B2B content marketing and SEO services company currently using SEMrush as their primary SEO intelligence tool. The relationship with seoClarity appears to be a new prospect evaluation initiated by the vendor (Terry and Mitul represent seoClarity). Dave Capone is GrowthX's head of operations and SEO infrastructure, handling tool decisions and architecture for both internal SEO work and client delivery. The timing for this conversation suggests GrowthX is actively re-evaluating their tool stack due to cost concerns and feature limitations—particularly around the ability to create client-ready reporting without data sampling issues. One complicating factor: a GrowthX investor sits on the SEMrush board, though this person is not actively influencing the evaluation or providing preferential treatment.

---

## Relevance

**To GrowthX Delivery:**
- Critical workflow dependency: GrowthX has built API integrations into their content creation pipeline, querying SEMrush for keyword data, search volume, and difficulty metrics—this is not easily replaced and requires feature parity for any tool transition
- Client reporting pain point: Looker dashboards with sampled data are unsuitable for client demos; seoClarity's unsampled data and pre-built, customizable dashboards could significantly improve client-facing analytics delivery
- Keyword tracking capacity: Moving from 2,312 to 25,000 keywords would allow deeper content strategy work, particularly for vertical expansion (Dave mentioned General Contracting and HVAC as current focus areas)

**To CheckThat:**
- Opportunity to evaluate seoClarity's AI visibility and AEO capabilities in their platform; Dave mentioned CheckThat's relevance to GrowthX's product line (implied by discussion of AI-powered workflows)

**To GrowthX Business Development:**
- Cost structure opportunity: Potential to cut or dramatically reduce SEMrush spend ($72K/year + $167K/month API costs) while adding unlimited users and superior features could improve margin structure on service delivery and allow reinvestment in product
- User licensing breakthrough: Unlimited users vs. SEMrush's per-user model removes a friction point for team scaling and reduces pressure to manage seat allocation across 40+ employees
- Partnership potential: seoClarity offering engineering support and product roadmap input suggests partnership depth beyond traditional vendor relationships

---

## Overview

- GrowthX.ai currently uses SEMrush's business plan (\~$72K/year) for keyword tracking and API usage, but faces limitations and high costs
- seoClarity offers a more comprehensive solution with 10x more keywords (25K vs 2.3K), unlimited users, and custom reporting capabilities
- GrowthX.ai's leadership requires a detailed comparison between SEMrush and seoClarity offerings to consider the switch

---

## Key Topics

### Current SEO Tool Usage

  - GrowthX.ai uses SEMrush business plan, paying \~$5-6K/month ($72K/year)
  - Tracking \~2,312 keywords
  - Heavy API usage for content creation workflow (costing \~$167K monthly)
  - 46 out of 50 user limit reached, causing login issues and extra costs

### seoClarity Advantages

  - Offering 25K keywords (10x more than current SEMrush plan)
  - Unlimited users vs. SEMrush's per-user charging model
  - Custom dashboard creation without sampling issues
  - Cohort analysis by content type and search intent
  - API access for existing workflows
  - Potential for engineering support and product roadmap input

### Transition Considerations

  - Keep one SEMrush account ($350/month) for API usage during transition
  - Potential conflict: GrowthX.ai investor on SEMrush board (not actively helping)
  - Need for detailed comparison table: SEMrush vs. seoClarity offerings and pricing

### Reporting and Dashboard Requirements

  - Current use of Looker for client dashboards, facing sampling issues
  - Need for customizable, client-ready dashboards without data sampling
  - Request for sample dashboard showcasing out-of-the-box reporting capabilities

---

## Action Items

**Terry Maturo**
- Create SEMrush vs seoClarity comparison table (pricing, features, 25K keywords, unlimited users)

- Prepare sample seoClarity dashboard (H&M account or similar) showing out-of-box reporting


**Mitul Gandhi**
- Review Terry's comparison table before sending to Dave


**Dave Capone**
- Create Ocean doc for leadership w/ SEMrush vs seoClarity comparison (after receiving from Terry)

- Contact engineer for SEMrush API usage details; send to Terry/Mitul

---

## Transcript

**Dave Capone:** I'm crawling on a site, so let me pause it, make sure it's not eating up bandwidth there.

**Terry Maturo:** Okay.

**Mitul Gandhi:** You're still doing it the old-fashioned way?

**Dave Capone:** Screaming Frog, yeah.

**Mitul Gandhi:** How do they upgrade you to the cloud?

**Dave Capone:** I wish I had access to that. But if you can pick up Screaming Frog to the cloud, to AWS, we did that at TripAdvisor and ran through the cloud, which was fun, but I don't have that here.

**Mitul Gandhi:** I'm going to get you a real cloud system here pretty soon. How are things going?

**Dave Capone:** Pretty good. Yeah, we're rocking and rolling, doing a lot of business, so it's doing pretty well. So the company seems to be getting there, but I know we were talking API and that's baked into a bunch of our workflows. We have our own system that's basically querying SEMrush and using their API to pull back competitors. It's pulling back keyword data, search volume, keyword difficulty, things like that. So I was able to get Terry the last month or so of our usage with the API, and I just wanted to make sure that doesn't raise any flags on your end.

**Mitul Gandhi:** Yeah, I'd love to. I didn't see the total usage thing in there, but tell me a little bit more. So this is even your tracking in SEMrush that you're pulling out all this data for?

**Dave Capone:** No, so it's when we start writing content. We pick the topic or keyword, and then our workflow will go and research all that for us. It'll pull the keyword difficulty, search volume, put together a list of keywords based off of all that data and competition, and then say, "Okay, here's the brief with all the keywords and things that we want to put into this article," and then it goes and writes it.

**Terry Maturo:** That's like $167,000 monthly, right?

**Dave Capone:** Yeah, it's up there.

**Mitul Gandhi:** Why would you do that if Content Fusion already does the whole process and gives you the recommended keywords to use?

**Dave Capone:** Yeah, that's our current workflow.

**Mitul Gandhi:** I'd love to—if you have details on the API being used, I can make sure that we map those APIs and provide you an equivalent there. Let's make sure we circle that because that sounds like a critical workflow for you, and I'm glad that came up.

**Dave Capone:** Well, even if we just keep one account with SEMrush for the API usage, it's still cheaper than what they're trying to upgrade us to. Leadership asked me to put together a comparison table of SEMrush pricing and what we're currently paying versus what you offer with seoClarity. I think you have those details. Can you help me with that?

**Terry Maturo:** Yeah, absolutely.

**Mitul Gandhi:** It can be super easy because you get so much more with what we're talking about here. Were you looking at the base plan that they had, like the 66K one?

**Dave Capone:** We have their business plan right now. They're charging us almost 5 to 6K a month, so we're paying around 72K a year.

**Mitul Gandhi:** Yeah, that's also probably because they charge you for all the users, right? This is not the enterprise. They were pitching you the enterprise, but this is not it.

**Dave Capone:** Right. And the problem with enterprise is the same thing. They want to charge us 100K a year and then only give us two users. Guest users don't get enterprise access—they get regular access.

**Mitul Gandhi:** I did not know that. That's super helpful to know because the SEMrush business plan has the ranking stuff, the reporting stuff, but you're not using much of that. You're using it for the keyword data and the API workflows, right?

**Dave Capone:** Yeah. We're tracking about 2,300 keywords—basic SEO tracking.

**Dave Capone:** Since I'm a power user, I can build cohorts using RegEx and track by cohort or topic. I'd love to build customized views and dashboards because right now I'm doing it through Looker and getting all sorts of sampling issues. My team doesn't have SQL or RegEx skills, so the only way to avoid sampling is to manually filter using RegEx, which doesn't automatically update. I'd rather build this through seoClarity where the data is unsampled.

**Mitul Gandhi:** We bring in the data completely unsampled, and you save it once—save a content type, save by intent—and then just use it everywhere. That's exactly it. We can outline a dozen things you get with seoClarity that don't exist in SEMrush: content types, cohorts, search intent analysis, customized dashboards.

**Dave Capone:** That'll be a definite big win if you can show how you're ingesting data through the API, warehousing it, and avoiding sampling. That's the main concern. We had a director meeting today—I created an advanced Looker dashboard, and they said it's too much for client demos. So we need a simple dashboard that directors and clients can access anytime without seeing sample data.

**Mitul Gandhi:** We already have half a dozen pre-built simple dashboards that are client-ready: cohort analysis by content type, cohort analysis by search intent, alerting capabilities, and API access to all the data for your workflows. We want to evaluate your existing API usage and make sure we can support it. If you have the ability to just keep one small account running with SEMrush at $350 a month to keep that API running, maybe that's not worth the retooling effort. But at some point, we want all of that to come over so there's no dependency on SEMrush.

**Dave Capone:** Right. Ideally we move quick—move it over, and we just keep one active, and then from there we can move. The only other hiccup I see is that apparently one of our investors is on the board for SEMrush, so that could potentially be problematic. But they're not giving us any deals and they're not doing anything to help us out. Right now they're not doing anything to try and sway us, and they keep cutting access to the platform because of suspicious activity flags when we have many folks logging in from different IPs. It's frustrating because they want to charge for every user.

**Mitul Gandhi:** Good for us. You don't have any limits for users, right? That should go on the main list of things—unlimited users. Your clients would get dashboard access, not necessarily the whole platform, right?

**Dave Capone:** Yeah, I give them Looker dashboard access, but I'd rather give them seoClarity access.

**Mitul Gandhi:** Exactly. We'll give them read-only access to the dashboard. The platform is for you to use, dashboards they can use. They can review it with your comments.

**Dave Capone:** Yeah, that's fine. So Terry, if you can put together that comparison table—is the 25K keyword package comparable to what the SEMrush plan is?

**Terry Maturo:** Yeah, absolutely. And just so we're doing apples to apples—you get 10x the keywords we're talking about, right?

**Mitul Gandhi:** Should we mention that as a differentiator? You're getting 10x the number of search queries with us. Let me double-check what you have for keywords.

**Dave Capone:** We have 2,312 keywords on our business plan, and API usage is so heavy that it breaks their web front-end. We're at 46 out of 50 users on the business plan.

**Mitul Gandhi:** You're getting 10x the number of search queries now. They're charging you $72K for 2,300 keywords plus $4,000 a month just for user access. That's incredible.

**Terry Maturo:** Even with our 25K keyword package at 6K a month, we're still cheaper. We'll highlight that in the comparison chart to help your case. Mitul and I will put it together, Mitul will get your feedback, and we can look at it before we send it over.

**Mitul Gandhi:** Another key item is product roadmap input. You're part of our team to help navigate product development. Whatever you need, you're going to have input into what we build.

**Dave Capone:** Yeah, I've submitted requests in the past and you've evaluated and built things for me. Could you send a sample dashboard—maybe the H&M account—showing what out-of-the-box reporting looks like? That would help make my case to leadership.

**Mitul Gandhi:** We have a great sample dashboard with a variety of widgets that we can throw in there. We'll make this fantastic and very helpful for you.

**Dave Capone:** Once I get that info from you, Terry, I'll put it into an Ocean doc for leadership to look over.

**Terry Maturo:** We'll send over the API information so we can dig into that. I'll put the comparison table together, and we'll get to work on our end.

**Dave Capone:** I'll reach out to one of our engineers and find out exactly how we're using the API, then send that over to you. We'll make this work.
