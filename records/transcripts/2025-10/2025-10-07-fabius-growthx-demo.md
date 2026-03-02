# Fabius / GrowthX - Demo

<metadata>
date: 2025-10-07
time: 22:30 UTC
duration: 29 minutes
organizer: george@growthx.ai
participants: George Haikal, Andi Bailey, Neil Madsen
fathom_recording_id: 92563362
fathom_url: https://fathom.video/calls/432485656
share_url: https://fathom.video/share/yrmeEV_fUPyVSH4WsBUzG_wAoL1ystCa
source: fathom
enriched_on: 2025-03-02 02:45 UTC
</metadata>

---

## Summary

George and Andi saw a demo of Fabius, an AI-powered platform that automates customer analysis from calls, emails, and documents for sales qualification and account health tracking. Neil showed how GrowthX can configure analysis rules to score prospects based on their ICP framework (enthusiasm, decision-maker quality, fit) and flag churn risk in existing customer accounts. George committed to sharing GrowthX's sales process documentation, 2-3 prospect calls from Fathom, and 2-3 existing customer calls, with Neil analyzing the data in 1-3 days and following up mid-week.

---

## Context

GrowthX is evaluating Fabius as a tool to automate two key processes: (1) sales qualification of prospects through ICP scoring on intro calls, and (2) ongoing account health tracking of existing clients. George previously showed Neil's team a Notion document outlining GrowthX's framework—five scoring dimensions evaluated after initial client meetings before deep delivery work begins. Since that conversation, George and the team have developed V1 scoring criteria to quantify prospect enthusiasm and fit. Andi Bailey, GrowthX's head of customer operations, was added to this demo because she owns client-facing delivery and internal processes; automating health scoring would reduce the manual evaluation work currently consuming significant time. The demo showed Fabius's configuration interface for different customer journey stages, its ability to pull transcript data from Fathom recordings, and how it can surface churn risk alerts alongside recommended action plans.

---

## Relevance

**To GrowthX Delivery:**
- Potential to reduce Andi's manual work on account health evaluation by automating call analysis against GrowthX's rubric
- Can integrate Fathom call transcripts to track ICP scoring correlation with actual client performance and health over time
- Supports post-sales health tracking by analyzing implementation calls and detecting early churn signals (e.g., declining engagement or unfulfilled needs)
- Requires solving data integration challenge: GrowthX uses minimal HubSpot seats (one seat for existing clients) and relies on Slack for customer communication, limiting CRM fields available; Fabius could pull Fathom calls + custom Notion documentation

**To GrowthX Business Development:**
- Enables faster prospect qualification by automating ICP scoring on sales calls, helping sales team prioritize high-fit accounts
- Health score automation could surface at-risk accounts like Strappy (renewing in one month) before they become problems, with AI-suggested intervention strategies
- George wants to test the platform against real GrowthX data (Strappy, Clark, Outreach, WebStacks, and Galileo mentioned as test cases) to validate accuracy before rollout
- Follow-up meeting scheduled mid-week after Neil analyzes sample data from 2-3 prospects and 2-3 existing clients

---

## Overview

- Fabius centers on "analysis configurations" tied to specific customer journey stages, with AI-assisted creation of scoring rubrics and customizable analysis fields
- Can analyze transcripts, documents, CRM fields, and external data; supports chat interface for ad-hoc queries across multiple calls or accounts
- Includes churn risk detection: flags customers showing warning signals (poor engagement, unmet needs, escalation needed) and suggests recommended actions
- Key limitation: Slack data access restricted by contractual terms; Fabius will need Fathom transcripts + internal Notion docs to enable full analysis
- Next steps: George sends sales process docs, 2-3 prospect Fathom calls, and 2-3 existing customer calls; Neil analyzes in 1-3 days; follow-up mid-week

---

## Key Topics

### Fabius Platform Overview

  - Centered around configurable analysis for different customer journey stages
  - Can analyze transcripts, documents, CRM data, and other sources
  - AI-assisted creation of analysis prompts and scoring criteria
  - Chat interface for ad-hoc analysis of individual/multiple calls or accounts

### GrowthX's Current Process

  - Manual analysis of customer calls using ICP framework in Notion
  - Recently added V1 scoring criteria for pre-deep dive intro meetings
  - Tracking how ICP scoring correlates with overall health, delivery, and churn

### Customization for GrowthX

  - Demo showed sample analysis fields based on GrowthX's notion document
  - Scoring includes pros, cons, and suggestions for improvement
  - Can update rubrics and create custom views/reports

### Data Sources and Integration

  - Primary focus on call analysis from Fathom recordings
  - Potential challenges with Slack data due to contractual limitations
  - Interest in connecting various touchpoints (calls, docs) for comprehensive health tracking

### Health Scoring and Churn Risk Analysis

  - Ongoing customer health scoring based on recent interactions
  - Churn risk analysis using custom indicators and internal notes
  - Automated alerts for health score drops or identified risks
  - Challenge: Incorporating GrowthX's content performance metrics into health scoring

---

## Action Items

**George Haikal (GrowthX)**
- Send Neil sales process steps documentation, 2-3 prospect Fathom call recordings, 2-3 existing client Fathom call recordings, and "what good looks like" analysis documentation for both pre-sales and post-sales stages

**Neil Madsen (Fabius)**
- Analyze provided call data and documentation (1-3 days turnaround), setup follow-up meeting mid-week to review results and have team play around in the platform

---

## Transcript
**Neil Madsen:** Hey, George.

**George Haikal:** Neil, how's it going, man?

**Neil Madsen:** Good.

**Neil Madsen:** How about yourself?

**George Haikal:** Good.

**George Haikal:** It's catching up on my lunch.

**George Haikal:** So I pardon the eating during the meeting.

**Neil Madsen:** Oh, no worries.

**Neil Madsen:** I definitely, especially like working from home, I feel like my like lunch hours always at random times throughout the day.

**George Haikal:** So I definitely feel you there.

**George Haikal:** Yeah, man, home is easier, though, at least in my opinion, because you can just pop away quick in the office, like they're back to back.

**George Haikal:** So you're moving around a little bit.

**George Haikal:** I find it harder.

**George Haikal:** But I started doing this, this meal kit, which is like healthy prepared meals.

**George Haikal:** So, oh, nice.

**George Haikal:** Game changer for, for saving some time and still eating pretty healthy.

**Neil Madsen:** Yeah, yeah.

**Neil Madsen:** That's always nice in the office to make sure you actually get something that's good.

**George Haikal:** I know, right?

**George Haikal:** This is Andi, by the way, we chatted earlier, and she's like our head of customer ops and deals with everything.

**George Haikal:** Customer facing related and also all of our internal processes as it relates to customers.

**George Haikal:** So thought it'd be great for her to join here.

**George Haikal:** I know we focused our first conversation on basically using our ICP information to start quantifying and scoring all the information that we get on sales calls.

**George Haikal:** But I also mentioned once we actually onboard a client and deliver them, deliver for them, being able to track their client health, account health, all of that.

**George Haikal:** so Andi can add more info, but that's why she's here.

**George Haikal:** She's super into it.

**Neil Madsen:** Okay, awesome.

**Neil Madsen:** Great to meet you, Andi.

**Andi Bailey:** Likewise.

**Neil Madsen:** Awesome.

**Neil Madsen:** So yeah, to, to begin with, I'll just recap a little bit about what we talked about, George, and kind of let me know if there's anything else that you want to focus on as I kind of go, what will be the focus of the demo?

**Neil Madsen:** We'll probably spend, you know, 10 to 15 minutes just on that main piece.

**Neil Madsen:** And really kind of what I heard from you, right, is you have this framework today, right?

**Neil Madsen:** What you showed me.

**Neil Madsen:** From that notion document, the idea of what the ICP is, and you're going through and you're manually analyzing customer calls.

**Neil Madsen:** And what I want to show you in the demo is, hey, how can this become an automated living system that can actually sort of scale that analysis across all of your customers, give you better insights, allow you to answer the questions you need without diving into like very specific customer calls to do it manually.

**George Haikal:** That sounds great.

**George Haikal:** I would say two things.

**George Haikal:** The only thing we added since we last spoke was a V1 of a scoring criteria based on, so before we even meet with the client, here's five things we can score them on after an intro meeting that is not yet a deep dive on how our product actually helped them, but it's more like qualitative, how enthusiastic are they about this engagement, and a bunch of other factors like that.

**George Haikal:** Second stage, then third stage goes into scoring each one of the dimensions, which is that document I showed.

**George Haikal:** So not much change there, I guess just a little more on the scoring side, which is easy to solve for.

**George Haikal:** Then, yeah, again, I would just say basically of equal importance is seeing if this tool can do both, like everything we talked about and also Andi's needs, because I would like it to be as easy as possible for her to maintain this.

**George Haikal:** And like anyone going through this pre-qualification sprint process, ICP scoring, like we'd want to track how that holds up anyway to like their overall health or how we're delivering, or if they churn, like being able to see how they scored and then iterate based on that.

**Neil Madsen:** I think it's all connected.

**Neil Madsen:** Yeah, perfect.

**Neil Madsen:** Yeah, we can walk through that as well.

**Neil Madsen:** I can give you some kind of general demos on that, be a little bit less tailored just because, yeah.

**Neil Madsen:** Cool.

**Neil Madsen:** So let me just go ahead and quickly share my screen here.

**George Haikal:** Andy, Neil knows Bridget, by the way.

**Andi Bailey:** Excellent.

**Neil Madsen:** Thanks.

**Neil Madsen:** Yeah, I used to work at LiveRamp with Bridget.

**Neil Madsen:** And actually, my last role at LiveRamp was leading all of the technical client-facing teams.

**Neil Madsen:** So I was in charge of sales engineering, implementation, technical account management, support, kind of all of that.

**Andi Bailey:** Sounds like a headache.

**Neil Madsen:** Yeah.

**Neil Madsen:** And lived and breathed kind of this whole sales cycle of like, hey, how do you make a customer successful from, you know, kind of that first touchpoint and then kind of ongoing, especially with LiveRamp, so much of the sales motion was upsell on an ongoing basis and retention.

**George Haikal:** So that was a big focus for us.

**George Haikal:** What did Bridget do when you were there?

**Neil Madsen:** She did.

**Neil Madsen:** I mean, we were both there for a number of years and LiveRamp just allows you to do a bunch of stuff.

**Neil Madsen:** She was a BD person for a bit.

**Neil Madsen:** She was a salesperson for a bit.

**Neil Madsen:** She was a chief of staff, I believe, for the head of sales or maybe for one of the CEOs.

**Neil Madsen:** So, I mean, especially somebody like Bridget, they were basically like, hey, look, here's a bunch of hard things that we need help with.

**Neil Madsen:** Can you do these things?

**George Haikal:** Yeah.

**George Haikal:** Checks out.

**Neil Madsen:** Cool.

**Neil Madsen:** So let me quickly just start from a high level here.

**Neil Madsen:** So let me zoom a bit.

**Neil Madsen:** Can you see the UI pretty well?

**Andi Bailey:** Yes.

**Neil Madsen:** Okay, perfect.

**Neil Madsen:** So just to start, we kind of center everything around these analysis configurations.

**Neil Madsen:** You can think of this as a discrete type of analysis that you want to make for a given place in the customer journey.

**Neil Madsen:** So just like two quick examples, right?

**Neil Madsen:** Something could be discovery and scoping.

**Neil Madsen:** You could also just split these things out.

**Neil Madsen:** And within discovery and scoping, you would then ask for a customer that's in discovery, these types of analyses on an ongoing basis.

**Neil Madsen:** And let's pull in this additional data, whether that's data from previous interactions, right?

**Neil Madsen:** So for implementation, it can be something like...

**Neil Madsen:** Hey, let's pull in all of the context of what the sales process would like, was like, and maybe like what's, you know, the, the implementation proposal we gave them was, and then as we go through implementation, let's actually look at how we're doing against that.

**Neil Madsen:** And so for a given, let me make sure that I'm putting around correctly, for a given configuration, you then have these analysis fields.

**Neil Madsen:** So George, put together basically just like a sample of four possible, like analysis fields that you could do.

**Neil Madsen:** And this would pull in basically transcript information.

**Neil Madsen:** sitting on top of the Zoom or Google Meet recordings, it can also pull in any documents or any external data that you have in your CRM.

**Neil Madsen:** So we also have customers that pull in, you know, firmographic data that pull in any third party data or other types of analyses that they've put in their CRM so that that can be analyzed as well during the process.

**Neil Madsen:** And then within sort of one of these fields, we focus a lot on giving you good tools to be able to actually like iterate and create this analysis over time.

**Neil Madsen:** Because ultimately the piece of this that makes something successful or not is can you define how you want the analysis to look?

**Neil Madsen:** And so a big thing that we focus on is basically, one, giving you the ability with an AI to basically help you like create these calls or things like that to say like, hey, look at these five previous calls.

**Neil Madsen:** What would you pull out as far as the jobs to be done?

**Neil Madsen:** Okay, could we now put them within these prompts themselves?

**Neil Madsen:** As well as we also have the idea of knowledge documents.

**Neil Madsen:** These can be things like case studies that you upload, any sort of internal best practices, anything like that, in order to also inform either the UI or the AI here that can help, or to actually inform the analysis as you're analyzing a given call.

**Neil Madsen:** And then basically you have the ability to select a bunch of calls and test it on an ongoing basis.

**Neil Madsen:** So here, you know, just put together like a quick idea of, let's say, like what the job could be done for something like this.

**Neil Madsen:** So it's like, hey, you know, I just had it basically write a sample call, had the AI write a sample call with, let's say, like you dive into deep dives that George mentioned.

**George Haikal:** When we first talked.

**George Haikal:** Yeah.

**Neil Madsen:** So I'm going to pause there.

**Neil Madsen:** So just to kind of recap, we have basically the configuration, which says, hey, for a given trigger, whether that's a call coming in, whether that's a change in an opportunity stage, whether that's just a given like cadence.

**Neil Madsen:** We also have the ability to say like, hey, analyze something for an account like every month, which is something that people look at, especially post-sales, to say, like, hey, look, if we're going through implementation, we may want to send, you know, a monthly update to the client saying like, hey, this is everything that we've worked together on and accomplished in the past month.

**George Haikal:** You can do that type of thing as well.

**Neil Madsen:** And then you have these fields.

**Neil Madsen:** And so for a given call, you can basically have any fields that you want to either be able to score things, which I'll show in a little bit, or something like that, where it's just a little bit more qualitative, or you can even have it just be something.

**Neil Madsen:** And it's, you know, one of 10 jobs to be done, literally just tell me which of these 10 it is and push it to the CRM.

**Neil Madsen:** You can do that as well.

**George Haikal:** Nice.

**George Haikal:** And basically, Andi, like every question we're trying to ask and dimension we're trying to solve for can be prompted to, prompted against all the transcripts and customer interactions that we have with the client.

**George Haikal:** And so that's kind of how.

**Neil Madsen:** They do all of this.

**Neil Madsen:** Yeah, just as an example, so like, I ran basically these scores.

**Neil Madsen:** So George, this was just based on kind of some of the notion stuff that you showed me.

**Neil Madsen:** And so, you know, it's something like, okay, hey, for, you know, champion or decision maker, this is a nine out of 10.

**Neil Madsen:** And it'll tell you the pros as well as the cons of what may be weak and then suggestions for how to strengthen in this area.

**George Haikal:** And this is all for one sample call?

**Neil Madsen:** Yeah, just had the AI so we can generate a hypothetical call.

**Neil Madsen:** Yeah, exactly.

**Neil Madsen:** And then, you know, we also do have basically these chat interfaces as well, where you can talk to either individual calls, or you can also talk at like the account level, or you can even, I mean, it's fairly common for like leadership and sales reps to do, just on an ad hoc basis.

**Neil Madsen:** Be like, hey, look, let me just pull up the last, you know, 50 discovery calls and have a conversation with it as I'm trying to figure out what analysis I may want to do.

**George Haikal:** Could you click into levels of review? I understand it's all test data in a test transcript, but could you show the rationale and the cons, please?

**Neil Madsen:** And just to, for example, go here, like, basically the rubric that we used was basically just taken from your, like, notion document that you shared to me.

**Neil Madsen:** And so I basically just plugged it in and had the AI make it kind of understandable from this perspective.

**Neil Madsen:** And so a big piece of this too is that all of this is available to you so that you know what the AI is doing and when it analyzes something in a certain way, it's not just like, hey, the AI has figured out what's best.

**George Haikal:** It's always following the instructions.

**George Haikal:** Exactly.

**George Haikal:** And how would this look at a high level?

**George Haikal:** So we've had 35 clients come through our pre-qualification sprint process already.

**George Haikal:** If I want to look at all the scores they've received to date and where they stand, aside from running a scheduled report, is there a table view here?

**Neil Madsen:** Actually, give me one second.

**Neil Madsen:** I'm going to switch over to something different that will have a couple more calls loaded into it to be able to show this.

**George Haikal:** Yes.

**George Haikal:** And then the second question is, that rubric makes sense and I know we can update it.

**George Haikal:** Can the scores of that rubric also be pulled into like a different view and like a table view so we can compare again and do our own analysis on?

**Neil Madsen:** Yeah.

**Neil Madsen:** Yes.

**Neil Madsen:** So a piece of this is basically, one, we generally just split it up by a person to begin with, but then we also basically allow you to kind of dive deeper.

**Neil Madsen:** So basically you can see, like, for a given person and then dive into details, and then also, you can basically download it as a CSV by month, or you can download multiple months, and this will just give you the score and everything like that.

**Neil Madsen:** And then the other piece that people use is basically for the chat itself, you can go into that and basically, like, analyze the fields themselves.

**Neil Madsen:** So you can say something like, hey, let me look at the decision makers, let me select the last 500 calls for those decision makers, and you can then chat with it sort of deeper as well to get more analytics on top of that.

**George Haikal:** I'll defer to Andi, she might have some other things to add.

**Andi Bailey:** Yeah, I mean, I think I am thinking about health, like health rubrics in general.

**Andi Bailey:** What else, like, can we go over what else I can pull in aside from my calls?

**Neil Madsen:** Yeah, so we basically organize things between calls, emails, and then what we call documents, as well as basically being able to pull in specific CRM fields.

**Neil Madsen:** So, like, the calls is obviously the ongoing calls, emails would be ongoing emails.

**Neil Madsen:** Because documents is a little bit more high-level or generalizable, such that, for example, when people have their customers fill out a form on the website in order to do the demo, a lot of times that will create a document and they'll have them analyze that if there's any sort of survey data.

**Neil Madsen:** If there's any third-party data, that's basically like anything else that we can pull in from the CRM or other types of sources.

**Neil Madsen:** We use that for the documents.

**Neil Madsen:** And then for the CRM fields, it's kind of any other type of data that would be on the accounts, on the opportunity, anything like that.

**Andi Bailey:** Yeah, I mean, the CRM piece is interesting because we don't have much there — we have one HubSpot seat, so we're not using a CRM for existing clients.

**Andi Bailey:** We're thinking about whether there's an opportunity to use something else that's not 15 HubSpot seats, and so we're not storing a lot of this in the CRM.

**Andi Bailey:** We also communicate over Slack, so email doesn't get checked much.

**Andi Bailey:** Is there a way to download the transcripts and do analysis from that kind of engagement?

**Neil Madsen:** Yeah, we've, we've looked at that.

**Neil Madsen:** Slack and Salesforce have changed a lot of their data allowances recently.

**Neil Madsen:** And so the way that we can store that data, I think, is a little bit difficult.

**Neil Madsen:** But especially if you have something saved internally of the Slack records or anything like that, then yeah, we could absolutely take those as conversations internally.

**Neil Madsen:** But yeah, a lot of that is related to just the, basically, like, contractual terms that Salesforce and Slack put on third-party vendors.

**Andi Bailey:** I mean, we have a lot of calls with the clients, so I think call analysis would be good.

**Andi Bailey:** And thinking about touch points, are there indicators or alerts for health — if we're importing all that data and it's all connected, could it surface alerts for us rather than us doing an ongoing manual evaluation of saying, hey, these calls are getting tense or something's off?

**Neil Madsen:** Yeah, yeah, So let me, let me actually just pull up.

**Neil Madsen:** So the other thing that we're investing a lot in now and have deployed for a couple of clients is this idea of basically churn risk analysis.

**Neil Madsen:** So there's kind of two ways to look at health.

**Neil Madsen:** One is just giving the customer health score on an ongoing basis.

**Neil Madsen:** And that can be done using the existing framework of, hey, whenever we have a, you know, call with the customer, look at the last couple of touch points and tell us kind of like what the health is.

**Neil Madsen:** Right.

**Neil Madsen:** And then you can also alert on that.

**Neil Madsen:** So let's say you'd get an email for any customer that drops below a five out of 10.

**Neil Madsen:** But there's other churn risks.

**Neil Madsen:** So you have an understanding or you can get an understanding through things like chat of like, hey, what are the indicators of what somebody would do that would call us churn?

**Neil Madsen:** And then we sit on top of all of the calls, any other communication that happens, everything like that, as well as any internal notes that the team puts in.

**Neil Madsen:** And we basically flag the churn risks and then using your kind of standard operating procedures, also come up with basically a suggestion for the team of like, hey, look, you know, let's say the customer's not getting a lot of value out of this or they're not really making any sorts of like moves because we don't have top-down buy-in.

**Neil Madsen:** So, you know, basically the recommended action plan would be, let's say like, hey, escalate this appropriately, get top-down buy-in, everything like that.

**Neil Madsen:** We're also looking at how well the team handled it and kind of giving feedback around that as well, so that as a leader, you can get an understanding of, hey, look, when these issues happen, who on the team is doing a good job being strategic about it, who's just being reactive about it, who has way too much work on their plate and just isn't doing anything about some of these things.

**Neil Madsen:** And so, you know, getting an understanding of whether these churn risks are accurate, how much they actually align with our standard operating procedures, and what did the account manager or the team actually do about it.

**Andi Bailey:** Yeah, I mean, I think this does get to one piece of what we're looking at.

**Andi Bailey:** Our health rubric includes strength, quality of output, and performance of their content, but performance of their content is harder to pull into another tool.

**Andi Bailey:** So I think we need to figure out like what parts of the rubric this could contribute to and how much weight we're putting it on it against like the other pieces of evaluation for health.

**Neil Madsen:** Yeah, so you're saying the other pieces of evaluation for health are looking at basically like what the actual delivery of the service is.

**Neil Madsen:** Yeah, exactly.

**Neil Madsen:** So like, hey, if we're not actually driving conversions, then that's bad as well.

**Neil Madsen:** That kind of thing.

**Neil Madsen:** Yeah, so we do have a form of this where basically we have customers today that they have those types of reports on actually the performance of the service that they're delivering.

**Neil Madsen:** And we may have it analyzed and sort of flagged if there is an issue as well.

**Andi Bailey:** Yeah.

**Andi Bailey:** Yeah.

**Andi Bailey:** And I mean, we have call agendas in Notion where we're highlighting that stuff, so at a high level, we can see it, but we'd be interested to know more about how other organizations are doing this with performance data integrated.

**Neil Madsen:** Okay, yeah, yeah, the big thing is basically, if there's a way for us to pull that in and tie it to the account, we can pull it from a number of different sources, and then essentially just have it be like anything else that gets analyzed, both in the context of itself and within the larger account. So we look at the past four weeks of performance plus the calls that we had, everything like that, and then it will flag an open risk if, based on the documentation that you have, this could actually put the account at risk.

**George Haikal:** Okay, cool.

**George Haikal:** This makes sense.

**George Haikal:** Right now, the way it's happening is super manual — either one-on-ones with the directors or the people running the weekly meetings, asking for weekly feedback.

**George Haikal:** And so if there's a way to just do the automated report against client health, that would be huge.

**George Haikal:** Because right now, it's just a ton of Andi's time.

**George Haikal:** So, yeah, what's, like, the, and we'll probably get to that at the end of the call, but I would love to be able to test against, like, some of our real documents and see how it performs.

**Neil Madsen:** Yeah, so as far as kind of the next steps there, so what we basically want to be able to look at is, like you've kind of seen, I've set up kind of an initial piece.

**Neil Madsen:** And then what we need to really show you what it would look like is first that documentation that you have in Notion, George, and any other documentation you've completed.

**Neil Madsen:** Let's say a V1 of what the analysis you'd want to do would look like.

**Neil Madsen:** And then the second piece is calls pulled out of Fathom.

**Neil Madsen:** And we'd probably just want to pull out both kind of a handful of calls as well as, you know, maybe for two to three customers pull out their last like five to 10 calls or something.

**Neil Madsen:** And basically we can ingest those and then show you both what it would look like for, you know, a given point in time of something like, hey, look, we've analyzed 10 discovery calls.

**Neil Madsen:** This is what it looked like.

**Neil Madsen:** This is how you get this feedback.

**Neil Madsen:** And then second would be, hey, for these customers where we have multiple things, you can see the customer journey over time and you can see the point in time where, you know, maybe difficulties have come up or maybe you've gotten wins or that type of thing.

**George Haikal:** This makes sense.

**George Haikal:** And then two to three Fathom calls for existing customers for the client health tracking stuff.

**George Haikal:** And then two to three Fathom calls for prospects that went through our formal sales process.

**George Haikal:** It'll be a mixture of sales calls and then a couple of onboarding calls that we had with them.

**Neil Madsen:** Yeah, exactly.

**Neil Madsen:** Because then you can kind of see at each step.

**Neil Madsen:** And then I think the third thing would just be like documentation on what your sales process looks like so that we can set up the configurations correctly to be like, okay, this is the discovery call.

**Neil Madsen:** This is the scoping call.

**Neil Madsen:** This is the proposal call, whatever it is there.

**George Haikal:** Amazing.

**George Haikal:** Just wrote that down.

**George Haikal:** What's the best way to send that all to you?

**George Haikal:** Like Fathom has links to video call recordings where you can then digest the summary and the transcripts.

**George Haikal:** We could send the raw transcripts over as well for each one of the calls.

**Neil Madsen:** Do you just want to share maybe with me right now a Fathom link and I'll see if I can access it and pull out the transcript?

**George Haikal:** Yeah, if we can do that, then we can just do the Fathom stuff.

**George Haikal:** I'm trying to think of who's a good, Andi, you have a client that's top of mind for you?

**Andi Bailey:** Strappy.

**George Haikal:** Strappy?

**George Haikal:** Nice.

**George Haikal:** Did you have a dream about Strappy last night or put out a fire today or what?

**Andi Bailey:** They're renewing in a month and they want a million things from us, but they don't want to pay us more money.

**George Haikal:** Just another day.

**George Haikal:** Boom, boom, boom.

**George Haikal:** Cool.

**George Haikal:** Wow, we've had 56 syncs with them.

**George Haikal:** That is crazy.

**George Haikal:** There's no recording in here.

**George Haikal:** There's one in here.

**George Haikal:** Okay.

**George Haikal:** Cool.

**George Haikal:** I just dropped the link in here.

**George Haikal:** Neil, let me know if you can access that.

**Neil Madsen:** Okay, let me pull it up.

**Neil Madsen:** I'm good.

**Neil Madsen:** It's asking me to sign in. Let me see if I can sign in so I can see it.

**George Haikal:** I'm going to check the permissions right now for this client.

**Neil Madsen:** So it looks like I have to request access to this. Should I click request access? Is there a way to make it client-facing?

**George Haikal:** Yeah, click request access, and then let me see that quickly. If not, I can send it to you.

**Neil Madsen:** Okay, says request sent.

**George Haikal:** Cool, I can figure this out with Fathom — I'll go get admin access and then approve you.

**Neil Madsen:** Okay, so yeah, I think that's probably the easiest way. I'll pull the transcripts and import them into our platform that way.

**Neil Madsen:** That's a pretty common approach, just taking it from the existing transcription.

**Neil Madsen:** And then, yeah, basically I'll put this in and then I'll just follow up with an email.

**Neil Madsen:** So as I mentioned, I'll really need three things from you.

**Neil Madsen:** One is understanding the steps of your sales process and getting the calls labeled by what stage of the sales process they're in.

**Neil Madsen:** And then second is documentation on what good looks like at each step, including what kind of analysis you'd want to do, both for pre-sales and post-sales.

**Neil Madsen:** And that doesn't have to be really structured because it's going to be basically made understandable to the AI by another AI.

**Neil Madsen:** So really just like giving anything you have internally is perfect.

**George Haikal:** Sweet, and that totally makes sense.

**George Haikal:** Andi, are there any other ones top of mind for you?

**George Haikal:** For me, on the prospect side, I want to do Clark and ClickUp.

**George Haikal:** And then Outreach as a good example — complicated with some stakeholder challenges, but it actually turned out pretty good for us.

**George Haikal:** Do you have any two other ones you want on more of the stabilized delivery side?

**Andi Bailey:** Maybe like web stacks.

**Andi Bailey:** They're like super engaged.

**Andi Bailey:** And then Galileo who just renewed or like kind of very middle of the road.

**George Haikal:** This is helpful.

**George Haikal:** Cool.

**George Haikal:** This is great.

**George Haikal:** No, appreciate it.

**George Haikal:** Very clear on the next steps.

**George Haikal:** We can get back to you within the next day or so with all of that.

**George Haikal:** And then we'll go from there.

**Neil Madsen:** Yeah, perfect.

**Neil Madsen:** The analysis will probably take one to three days.

**Neil Madsen:** And then we can set up time probably mid-week to go through the results together.

**George Haikal:** Sweet.

**George Haikal:** I'm assuming after that we can play around ourselves in the tool once everything is loaded up.

**Neil Madsen:** Yeah, absolutely.

**Andi Bailey:** I'm good.

**Andi Bailey:** Yeah, no, I'm just interested to see how it works.

**Andi Bailey:** Thanks for offering to show us so much.

**Neil Madsen:** Yeah, of course.

**George Haikal:** Looking forward to it.

**George Haikal:** Great to meet you, Neil.

**Neil Madsen:** Good to see you, George.

**Neil Madsen:** Talk to you later.

**Neil Madsen:** Bye.
