# GrowthX x Madrona – AI/Cloud Resource Access

<metadata>
date: 2025-06-20
time: 18:03 UTC
duration: 21 minutes
organizer: Marcel Santilli
participants: Marcel Santilli, Yousef Hamade, Katie Chiupka
fathom_recording_id: 69684169
fathom_url: https://fathom.video/calls/331284334
share_url: https://fathom.video/share/mBLWXXXFUyLiMQZzMqJ67RkQqZ91fycQ
source: fathom
enriched_on: 2026-03-03 21:15 UTC
</metadata>

---

## Summary

Marcel introduced GrowthX's AI-powered platform and its intensive compute requirements to Katie Chiupka at Madrona, focusing on rate-limit bottlenecks with Anthropic and OpenAI APIs. Katie committed to escalating access through Madrona's direct relationships with cloud providers and API vendors, starting with connecting GrowthX to Anthropic's VCBD team for Anthropic limits and helping establish OpenAI contacts. The team agreed to send Katie a comprehensive tech stack breakdown to unlock Perplexity credits ($5k), explore SEMrush partnerships, and investigate $600k+ in cloud provider credits through strategic stacking.

---

## Context

GrowthX is a Madrona portfolio company building an AI-powered workflow engine that enables complex knowledge work with human oversight. The platform is fundamentally different from traditional SaaS: it creates intelligent agents that execute intricate multi-step workflows using various APIs (Anthropic, OpenAI, Perplexity, SEMrush, SERP API) and AI models to automate specialized tasks like fact-checking, research, and content generation. This architecture is intentionally compute-heavy—the platform processed 832,000 activities in a single month—and quality is prioritized over cost efficiency since clients pay $25-30k/month contracts.

Katie Chiupka at Madrona supports portfolio companies with cloud and BD partnerships, providing access to direct relationships with major cloud providers and API vendors where she can escalate support issues and unlock free credits. This meeting focused on helping GrowthX address immediate rate-limit bottlenecks that are causing engineering overhead and preventing platform scaling, while also identifying medium and long-term opportunities for cost optimization through strategic partnerships.

---

## Relevance

**To GrowthX Delivery:**
- Anthropic API rate limits are the highest priority blocker—currently forcing engineering to implement queue systems and model-swapping logic, creating technical debt that delays customer-facing improvements
- Direct API access is non-negotiable for GrowthX due to time-to-market on new models; cloud provider abstractions (AWS Bedrock, GCP Vertex) create weeks of delay for model availability
- Monthly API costs span Anthropic, OpenAI, Perplexity, and SEMrush; securing credits and preferred pricing directly impacts platform economics at scale

**To CheckThat / AEO:**
- GrowthX is using AI agents extensively for research workflows (SEMrush API, SERP API, Replica's API for fact-checking)—insights from this platform scaling could inform CheckThat's own API strategy and model selection

**To GrowthX Business Development:**
- Strong signal that GrowthX is moving toward broader platform launch and scaling beyond current consulting engagements; rate-limit resolution is prerequisite for growth
- Madrona relationship represents capital-efficient path to cost reduction ($600k+ cloud credits possible), improving unit economics without dilution
- Potential co-marketing/partnership with SEMrush and Perplexity positions GrowthX as strategic AI customer rather than commodity user
- Google Workspace upgrade and Datadog adoption indicate team scaling (70+ users planned)

---

## Overview

- GrowthX's AI-powered workflow engine processed 832k activities this month and requires heavy compute resources, hitting rate limits with Anthropic API (highest priority blocker)
- Madrona can escalate API access and limit issues directly with Anthropic (VCBD team), OpenAI, Perplexity, SEMrush, and cloud providers via Katie's established relationships
- GrowthX strongly prefers direct API access over cloud provider abstractions (AWS Bedrock, GCP Vertex) due to time-to-market requirements for latest models
- Path to unlock $5k Perplexity credits, potential SEMrush co-marketing partnership, and up to $600k+ in cloud provider credits through strategic stacking (AWS $200k + follow-on rounds)

---

## Key Topics

### GrowthX Platform Overview

  - AI-powered workflow engine for complex knowledge work
  - Executes intricate plans using various APIs, services, and AI models
  - Compute-heavy processes (e.g., 832k activities this month)
  - High-quality output prioritized over cost-efficiency (e.g., $25k-30k/mo contracts)

### Current Resource Challenges

  - Hitting rate limits with Anthropic API (highest priority)
  - OpenAI unresponsive to public form submissions
  - Heavy users of Perplexity API (not yet rate-limited)
  - SEMrush as current top cost driver among "other" APIs

### Cloud Provider Considerations

  - Using Render for most infrastructure; some LangChain (considering alternatives)
  - Reluctant to use cloud provider AI services (e.g., AWS Bedrock) due to delayed model access
  - Need immediate access to latest models for competitive edge

### Partnership Opportunities

  - Anthropic: Katie to escalate via VCBD team (Danny Delaney)
  - OpenAI: Katie to help establish connection for limit increases
  - Perplexity: Potential for $5k in API credits via Madrona's startup ecosystem
  - SEMrush: Potential for co-marketing, non-competitive partnership
  - Cloud providers: Strategic engagement for maximum credits ($600k+ potential)

### Additional Resource Needs

  - Datadog for observability (credits/partnership inquiry)
  - Google Workspace upgrade (exploring preferred pricing via GCP connection)

---

## Action Items

**Katie Chiupka**
- Follow up w/ Anthropic (Danny Delaney) re. increasing API limits for GrowthX

- Escalate OpenAI situation, connect GrowthX w/ right people for API access

- Send info on Perplexity API credits ($5k) to GrowthX team

- Inquire about Google Workspace preferred pricing for Madrona portfolio cos


**Yousef Hamade**
- Send Katie details on Anthropic/OpenAI API usage, rate limits, bottlenecks


**Marcel Santilli**
- Prep summary w/ Yousef of tech stack, API providers, usage for Katie. Inc. Anthropic, OpenAI, Perplexity, SEMrush

---

## Transcript
**Marcel Santilli:** Hi, Katie.

**Katie Chiupka:** How's it going?

**Katie Chiupka:** Happy Friday.

**Katie Chiupka:** Good.

**Katie Chiupka:** How are you?

**Katie Chiupka:** Is this your fixer or mine?

**Marcel Santilli:** This one is mine.

**Marcel Santilli:** I haven't seen another one.

**Katie Chiupka:** okay.

**Katie Chiupka:** I guess mine isn't invited.

**Marcel Santilli:** We've just been testing it out.

**Marcel Santilli:** Yeah, yeah.

**Katie Chiupka:** I know.

**Marcel Santilli:** I've been testing it off since, like, Karon came by the office and they stopped by, too.

**Marcel Santilli:** So then I started testing it.

**Marcel Santilli:** The note taker is actually pretty good.

**Marcel Santilli:** It's so far better than Fathom.

**Marcel Santilli:** We hate Fathom.

**Katie Chiupka:** Okay.

**Katie Chiupka:** Which they're here, too.

**Katie Chiupka:** So nice to see Fathom.

**Marcel Santilli:** Yeah, yeah, exactly.

**Marcel Santilli:** But thanks for taking the time.

**Marcel Santilli:** I don't if Bridget is going to join or not, but I know you all have time, I think, next week, right, already?

**Katie Chiupka:** Yeah, I think we have time next Monday.

**Marcel Santilli:** Okay, perfect.

**Marcel Santilli:** And then just a little context.

**Marcel Santilli:** Yousef, do you want to do just a super, super quick intro on your end?

**Yousef Hamade:** Yeah.

**Yousef Hamade:** Hey, Katie.

**Yousef Hamade:** Nice to meet you.

**Yousef Hamade:** Just helping out here with cybersecurity and IT needs.

**Yousef Hamade:** So this is one of those things I'm trying to just help take off the CTO's plate and help out as I can.

**Katie Chiupka:** Sure, sure.

**Marcel Santilli:** Katie, do want to do just a quick intro and then happy to give you a context if you think would be helpful or wherever you think would be helpful to make the most sense?

**Katie Chiupka:** Yeah, for sure.

**Katie Chiupka:** So I'll do a quick intro.

**Katie Chiupka:** So at Madrona, I support our portfolio companies with cloud and BD partnerships.

**Katie Chiupka:** So it's basically, you can think of me like post-investment, like no capital is coming from me other than like free credits from cloud partners.

**Katie Chiupka:** And so if you're running into situations like you guys are right now, like I would be the right resource to come to because at Madrona, we have, we have specific level of contacts to all these large and small cloud providers and providers in general where we.

**Katie Chiupka:** It's escalate situation.

**Katie Chiupka:** So you are getting to the right people quicker and getting your answer quicker on what they can do to support.

**Katie Chiupka:** And so I work with, I just got off the call with AWS before this.

**Katie Chiupka:** And so I work closely with them.

**Katie Chiupka:** And then I also work with like our enterprise CXO network on business introductions that help accelerate the growth.

**Katie Chiupka:** So pretty much partnerships from like everything from like free credits to more strategic and then growth opportunities from like BD perspective as well.

**Marcel Santilli:** Awesome.

**Marcel Santilli:** Yeah, that is super, super helpful.

**Marcel Santilli:** Cool.

**Marcel Santilli:** Well, maybe it would be helpful to give you just a little bit of like high level so you kind of understand.

**Katie Chiupka:** Yeah, for sure.

**Marcel Santilli:** Because I think there's like a lot of areas of opportunity.

**Marcel Santilli:** So actually, now that you've described a little bit broader, maybe giving you a broader context and then I can share more things later.

**Marcel Santilli:** Sure.

**Marcel Santilli:** Cool.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Okay, cool.

**Marcel Santilli:** So let me just share maybe a little bit of like, this is our internal platform.

**Marcel Santilli:** And I think even Karon hasn't seen it.

**Marcel Santilli:** So you get to see before him.

**Marcel Santilli:** But just to kind of give you a little bit of the sense of a lot of what we do underneath the hood is as we're generating, think of it as like we're creating a platform that enables us to do really complex knowledge work with humans in the loop, right?

**Marcel Santilli:** And so what we build under the hood is a workflow engine that is essentially an AI coding agent that takes a plan from an expert.

**Marcel Santilli:** So let's say for you, you're like, hey, I want to research every single startup out there that provides compute resources to startups and AI, right?

**Marcel Santilli:** Like, how would you go about doing that?

**Marcel Santilli:** Like, you think through, okay, this is the criteria.

**Marcel Santilli:** This is how I would do it.

**Marcel Santilli:** This is how I would research.

**Marcel Santilli:** This is the context of how I would do it.

**Marcel Santilli:** And you would build, if you're trying to use AI, you would build a workflow and you go into some local tools and just like drag and drop and give it a prompt and it would be very, very hard.

**Marcel Santilli:** So essentially for us, we have a coding agent.

**Marcel Santilli:** You feed the plan, and it builds this very complex workflow.

**Marcel Santilli:** And then we have a runtime layer that then goes and executes these plans, right?

**Marcel Santilli:** And goes and uses different APIs, different services, you name it, right?

**Marcel Santilli:** So for instance, this one specifically, it goes through all of these steps, right?

**Marcel Santilli:** And this one is using SEMrush API.

**Marcel Santilli:** It's using SERP API.

**Marcel Santilli:** It's obviously using a bunch of different scraping services.

**Marcel Santilli:** It's also using a bunch of different models, right?

**Marcel Santilli:** And so, but because of that, like our processes are like really, really heavy.

**Marcel Santilli:** So I'll give you an example.

**Marcel Santilli:** Our fact checking step, it takes a piece of content that we produce, and it splits it into chunks.

**Marcel Santilli:** And then it goes and extracts each passage.

**Marcel Santilli:** And then it goes and researches each passage using the APIs, like Replica's API, for example.

**Marcel Santilli:** And then it verifies each one of them to see if it's false.

**Marcel Santilli:** Or not.

**Marcel Santilli:** So, and then based on that goes and uses different LLMs, rewrite it to based on if it was false or not.

**Marcel Santilli:** Right.

**Marcel Santilli:** So you can see it's pretty compute heavy.

**Marcel Santilli:** And so like we're using Temporal, for example, Temporal could be a great partner in another investment of Madrona.

**Katie Chiupka:** Yeah.

**Marcel Santilli:** So like if you just look like just across like this month alone, we've done 832,000 activities here.

**Katie Chiupka:** Yeah.

**Marcel Santilli:** You know, and so like, but because of that, because our processes are heavy and we want the latest and greatest, we run into limits a lot more often.

**Marcel Santilli:** But we're not so compute heavy because we don't have 10,000 users, right?

**Marcel Santilli:** Like what we do for the amount that we like of quote unquote users who are essentially our employees.

**Marcel Santilli:** Like we just consume an obscene amount, right?

**Marcel Santilli:** And, and like, we don't want to take shortcuts that will impact quality.

**Marcel Santilli:** In other words, like most companies, like when they're running a process, they need to have low latency, right?

**Marcel Santilli:** And they need to, for that process to cost pennies at most because they're only charging $20.

**Marcel Santilli:** For us, like we're charging, you know, Webflow, you know, 30 grand a month, like for, or abnormal security, $25,000 a month.

**Marcel Santilli:** Like we don't care if the process costs $10.

**Marcel Santilli:** Like for us, just want to achieve quality and it's directly replacing human time, which is more expensive than that.

**Katie Chiupka:** Anyways, right.

**Marcel Santilli:** So anyways, that's the context.

**Marcel Santilli:** So the context, we use a lot of APIs, for instance, like recraft, we use recrafts API, we use different like APIs around like stock images and around like different research.

**Marcel Santilli:** We have a lot of, for instance, this week, we kicked off with Joey, who is the founder of Allbirds and his new startup that is in women's health and a hormone supplement side, you know, and there's a lot.

**Marcel Santilli:** I'd like healthcare sources we're going to need to tap into.

**Marcel Santilli:** So that's that one side.

**Marcel Santilli:** The more immediate side of what we talked about, which is like going direct to the sources and making sure we were preparing ahead of launching our platform more broadly and to keep up with demand, essentially.

**Marcel Santilli:** So making sure we're not caught in a situation where it's just like we're opening this up and now all of sudden everything breaks and we're a month away from getting more capacity.

**Marcel Santilli:** You know, and then longer, longer term is seeing like the opportunities of like getting credits and, you know, maybe developing more strategic relationships with the cloud providers or the cloud players and things like that, you know?

**Katie Chiupka:** Yeah.

**Katie Chiupka:** So are you guys predominantly building with or like who are you built on?

**Katie Chiupka:** AWS, Anthro, did you say?

**Marcel Santilli:** We're actually using Render for most things.

**Marcel Santilli:** Yeah, Render, our stack's mostly like Render, Temporal, and then we're using LangChain for some things, but we might move off of it because it's pretty poor.

**Marcel Santilli:** Currently looking into evaluation platforms right now, and then we're pretty heavy with Perplexity.

**Katie Chiupka:** API is probably one of our biggest things.

**Marcel Santilli:** We're currently talking to you.com.

**Marcel Santilli:** They have a new CMO, and they want to be a customer, so we're seeing, but their API just got not better, you know, for a while.

**Marcel Santilli:** And then we're pretty bottleneck, obviously, with Anthropic, OpenAI, and haven't spent enough time, honestly, with Google's models, but we're not opposed to it.

**Marcel Santilli:** It's just one of those, just like, hasn't been worth our time, to be honest, you know.

**Katie Chiupka:** Okay, okay.

**Katie Chiupka:** So, super helpful.

**Marcel Santilli:** I'm going to show you some of this, where we're hitting bottlenecks, too.

**Katie Chiupka:** Yeah, okay, okay.

**Yousef Hamade:** As you can see, this week we were being rate-limited pretty hard on our Anthropic side, and that triggered this conversation.

**Yousef Hamade:** We have a direct rep with Anthropic that we've been trying to work through all week as well.

**Katie Chiupka:** Anthropic?

**Katie Chiupka:** Do you have a name?

**Yousef Hamade:** So it's Sophie is her first name.

**Yousef Hamade:** And give me just a second.

**Marcel Santilli:** She's like a college friend of Bridget, our VP of Ops.

**Yousef Hamade:** It's like a warm contact. I think she's an Account Executive.

**Yousef Hamade:** Her last name is Altchek.

**Yousef Hamade:** And, you know, we just, like, literally went on Anthropic's, you know, form and said, hey, help us out.

**Yousef Hamade:** Or, hey, give us a contact.

**Yousef Hamade:** And then, again, it just happened to be someone connected to a couple of people here.

**Yousef Hamade:** Open AI has kind of ghosted us at the moment, trying the same process.

**Yousef Hamade:** And so, you know, we haven't gotten a rep over at Open AI yet.

**Yousef Hamade:** Okay.

**Katie Chiupka:** Okay.

**Katie Chiupka:** Okay, so for Anthropic, it sounds like, so you guys aren't consuming, because I sent a note to AWS and I said, okay, that they're happy to chat with you guys to talk about Anthropic and the limits there and talk through it.

**Katie Chiupka:** It's a different team than I usually work with over there, but it sounds like you're not consuming Anthropic with it.

**Katie Chiupka:** I fear if we get you in the AWS cycle, they're going to try to sell you.

**Marcel Santilli:** Yeah, it's also like our CTO doesn't want to like go through, like essentially all the cloud providers make it way, way, way harder.

**Katie Chiupka:** Totally.

**Marcel Santilli:** And a new model comes out, it's not immediately available in Bedrock or something.

**Marcel Santilli:** Exactly. For us, time to the latest model is so, so, so much more important, because each run through essentially takes us up a notch.

**Katie Chiupka:** We're riding that wave as well.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** So it's like we need to be the latest immediately, essentially.

**Katie Chiupka:** Yeah, okay, so we have a direct relationship as well with Anthropic, their VCBD team.

**Katie Chiupka:** So Danny Delaney over there.

**Katie Chiupka:** I reached out to him and he said, he's looking, he's going to take a look at GrowthX and I'll get back to you.

**Katie Chiupka:** I can share that we connected and kind of what the issue is there and try to kind of escalate to get higher limits.

**Katie Chiupka:** I think going through Anthropic is probably going be the right thing than going through AWS through Anthropic right now because I know they're going to try to sell you on stuff.

**Katie Chiupka:** Because we've had this conversation with folks before.

**Yousef Hamade:** And Sophie suggested maybe we go through GCP with Vertex.

**Yousef Hamade:** And again, like...

**Katie Chiupka:** We have a great relationship with GCP as well.

**Yousef Hamade:** Yeah.

**Yousef Hamade:** And the challenge there is getting everything swung over from Anthropic Direct to GCP would be a pretty heavy lift.

**Yousef Hamade:** And we'd still be second class versus going direct through GCP or direct through Anthropic.

**Katie Chiupka:** Yeah, okay.

**Katie Chiupka:** Okay, so I think the priority one is just go direct through Anthropic and get you guys connected into the right folks for the right conversations on limit increases.

**Katie Chiupka:** As well as, I can help escalate, if you want to send me a note on where you're running into blockers at OpenAI, we have a team that we work with there as well.

**Marcel Santilli:** Larry, the lead, is actually out on paternity leave, but his backup has been super great and helpful, so I'm happy to escalate there too.

**Marcel Santilli:** That one is almost like start from scratch if we can go through.

**Katie Chiupka:** That's super disappointing, so provide that context to me because I will make sure that they pay attention because they're very good for companies that they know who have a relationship with tier one VCs in their mind, basically.

**Yousef Hamade:** Yeah, and so we just did the submit the request through their public forum.

**Katie Chiupka:** And, you know, crickets, so to yeah, send me a note, and I'll estimate that, too, to try to get you the right folks.

**Marcel Santilli:** Okay, so as a next step, Yousef, we'll send you all the details.

**Marcel Santilli:** I know you still have time with Bridget. I think it would be helpful to review that.

**Marcel Santilli:** Our biggest API expenses are Anthropic, OpenAI, Perplexity, and then SEMrush. Those are the four top ones.

**Katie Chiupka:** I believe Anna's on their board.

**Marcel Santilli:** We engaged with them and they came back with obscene prices—2x more than the offer they gave us six months ago. That one's lower tier compared to the top four, but the priority order is Anthropic, OpenAI, Perplexity, and then SEMrush as our biggest cost driver. Having an API partnership we can co-market with them makes sense since we're not competitive. It's cool because they're trying to be more in the AI space.

**Katie Chiupka:** We also have a relationship with Perplexity. We have access to their approved startup partners ecosystem—it's about $5k in API credits, which every bit helps. I can send that information to you guys. Send me a breakdown of those areas and I'll follow up. I'm talking with Perplexity on Monday.

**Marcel Santilli:** Here's what we'll do. We can work on unlocking Anthropic and OpenAI in parallel. We can include Perplexity if you want to start that relationship too, but we're not rate-limited on Perplexity yet.

**Yousef Hamade:** Yet.

**Marcel Santilli:** We used to switch everything to Perplexity from You.com, but You.com was difficult to work with—no API dashboard. We'd just get bills for $10k and couldn't see our usage breakdown. We'll also prepare a separate summary of your tech stack.

**Marcel Santilli:** We can share all the players we have relationships with or are using where intros would be helpful. We're also open to case studies, co-marketing, and talking about the cool work we're doing. If you have intros, great. If not, this is just our wish list.

**Katie Chiupka:** That makes complete sense. I'll send you a resource document showing what's available at Madrona. It's not comprehensive—OpenAI and Anthropic aren't on it—but it shows where the free credits are and acts as a resource library.

**Marcel Santilli:** So do you guys have anything with Datadog?

**Katie Chiupka:** We do have a relationship with Datadog, but they're not on this document for some reason.

**Marcel Santilli:** We're starting to use them for observability. We have principal engineers from X, Stripe, and Airbnb who've used Datadog before, so there might be credit opportunities there.

**Marcel Santilli:** For cloud providers, my CTO and I need to sit down and plan. The approach we've heard is to pick one provider a year, use up all their credits, then layer another one—you can stack credits across providers and get $600k+ for free.

**Katie Chiupka:** Right. There are unique things for each. AWS can give up to $200k, but you need to go to them first with your seed round.

**Katie Chiupka:** If you get a follow-on round with any of their preferred VC partners, you get another $100k. There are unique things with each provider that you can stack. Often we can get these credits extended. If you haven't burned through them in a year, we can sometimes get an extension.

**Marcel Santilli:** Perfect. This is super helpful. Thank you.

**Katie Chiupka:** Yeah.

**Yousef Hamade:** There is one other.

**Yousef Hamade:** So I know you guys have GCP on here.

**Yousef Hamade:** Google Workspace.

**Katie Chiupka:** Google Workspace, yeah.

**Yousef Hamade:** Do you do anything there?

**Yousef Hamade:** Or can you do anything there?

**Yousef Hamade:** We're on a business plan right now, but we need to upgrade. It's going to be extremely expensive with 70+ users. Are there any deals you can get through your GCP connections on Workspace?

**Katie Chiupka:** I'm sure we can, but let me ask our team.

**Yousef Hamade:** That would be great.

**Katie Chiupka:** I don't see why they wouldn't help—that's something they want to drive users to. I'm positive we can work with them on preferred pricing for Madrona portfolio companies for Google Workspace. We just haven't asked yet. I'll look for the summary and details on the Anthropic limits situation.

**Katie Chiupka:** Danny is looking into the Anthropic situation. Any additional context I can provide to him, plus the OpenAI escalation, I'll send once I have details from you in writing.

**Marcel Santilli:** To summarize, the Anthropic issue is most time-sensitive. We're already hitting the limit, causing engineering refactoring—we're building queue systems and swapping models just to avoid hitting the API limit. This creates a lot of work that we should be spending on customer value instead.

**Katie Chiupka:** Exactly. Send me those details and I'll get back to you today.

**Katie Chiupka:** Thank you so much. Nice to meet both of you.

**Marcel Santilli:** Nice to meet you too.

**Katie Chiupka:** Bye.
