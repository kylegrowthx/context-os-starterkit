# ICP & Sprint Pipeline Review

<metadata>
date: 2025-09-30
time: 21:01 UTC
duration: 65 minutes
organizer: Tyler Pavlas (tyler@growthx.ai)
participants: Tyler Pavlas, George Haikal, Bridget McGillivray, Andi Bailey, Jason Gong
fathom_recording_id: 90953176
fathom_url: https://fathom.video/calls/423531814
share_url: https://fathom.video/share/vMxZW1LMxmDns6tvxi4QLRDbXs5weexk
source: fathom
enriched_on: 2026-03-03 12:00 UTC
</metadata>

---

## Summary

GrowthX's sales and delivery teams aligned on a new ICP (Ideal Client Profile) framework with five key dimensions — DRI/champion, content complexity, audience clarity, technical depth, and company maturity — to better qualify inbound deals and prioritize the 70+ companies in the current pipeline. The team agreed to be more selective with early-stage companies, moving seed-stage prospects to a waitlist when misaligned on timelines or capabilities, while activating the Deal Desk channel for collaborative deal evaluation and refining messaging around qualification decisions to focus on results alignment rather than technical dismissals.

---

## Context

GrowthX's services team manages a large, complex sales pipeline—70+ active opportunities including Airbyte, Redis, Cresta, Brex, Zapier, and others—across different deal maturity stages and client profiles. The core tension: the team was making qualification decisions case-by-case without a consistent framework, leading to inconsistent outcomes and extended sales cycles. Meanwhile, delivery was struggling with clients outside the ideal profile (early-stage, very technical, misaligned on outcomes), draining resources and creating churn risk. George Haikal developed the ICP framework by surveying team members on their easiest and hardest clients, analyzing historical churn, and defining five dimensions that predict successful engagements. The meeting was called to socialize the framework, gather feedback from Tyler (sales/pipeline lead), Bridget (delivery lead), Andi (operations/resource planning), and Jason (technical feasibility expert) before finalizing materials for sales, kickoff, and delivery workflows.

---

## Relevance

- **To GrowthX Delivery:** The ICP framework creates guardrails for deal qualification, reducing downstream churn and misaligned expectations. Key delivery insight: clients with a clear DRI/champion, focused audience, and realistic outcome expectations close faster and stay longer. Non-starters include no existing blog/CMS (require education), extreme technical depth (Kubernetes-level), and seed-stage companies still defining their content strategy. The framework supports a tiered service model (discussed in parallel with role definition) to handle out-of-ICP clients more efficiently—e.g., editorial-only engagements or managed pods.

- **To GrowthX Business Development:** Seed-stage and early-stage companies are now pushed to a waitlist rather than onboarded, freeing deal slots for Series A+ opportunities with longer lifetime value and higher renewal likelihood. The Deal Desk channel activation enables faster, more collaborative go/no-go decisions. Waitlist/breakup messaging needs refinement to frame qualification as "results alignment" (realistic timelines and capability match) rather than technical dismissal—protecting brand perception while screening out poor fits.

- **To CheckThat:** The conversation touches on technical content evaluation—distinguishing "too technical" (Hacker News / DevRel-only) from "sweet spot" (cloud provider comparisons)—which informs prompt auditing and AI visibility research around industry-specific content complexity.

---

## Overview

- New ICP criteria and scoring matrix being developed to better qualify potential clients
- Agreement to be more selective with early-stage companies due to higher risk and misaligned expectations
- Deal Desk channel to be used more actively for collaborative deal evaluation
- Need for clearer, more decisive qualification criteria to streamline decision-making

---

## Key Topics

### Current Pipeline Review

  - Several deals in progress (Airbyte, Redis, Cresta, TrueLook, Magic, Tango, Obsidian, Norm, Zapier, Navon, Tavis, Brex)
  - Varying stages of engagement and alignment across deals
  - Some technical/procurement challenges being worked through
  - 70+ total deals in pipeline; 40+ could close with better prioritization

### ICP Criteria Development

  - George creating matrix with 5 key dimensions to identify ideal clients
  - Dimensions include: DRI/champion, content complexity, audience clarity, technical depth, company maturity
  - Scoring system and actionable materials for sales/delivery being developed
  - Team provided feedback on criteria and potential "non-starters"
  - Non-starters: no blog/CMS, extreme technical depth, rapidly pivoting business models

### Early-Stage Company Challenges

  - Debate around working with seed-stage companies like BlackSoul
  - Concerns: higher churn risk, unrealistic expectations, pivoting business models
  - Agreement to be more selective and push early-stage to waitlist when possible
  - Focus on Series A+ deals where lifetime value and renewal rates are higher

### Deal Evaluation Process

  - Will use Deal Desk channel more actively to collaboratively evaluate deals
  - Plan to get technical (Jason) and delivery (Andi) input on feasibility and resource impact
  - Need for clearer go/no-go criteria to reduce "analysis paralysis"
  - 3/6/12-month outcome expectations assessment as core qualification step

### Client Expectations Management

  - Importance of aligning on 3/6/12 month goals and realistic timelines
  - Challenge of communicating typical ROI due to situational factors
  - Need to refine waitlist/breakup messaging to maintain professionalism
  - Shift messaging from "we can't do technical clients" to "we need results alignment on timelines"

---

## Action Items

**George Haikal (GrowthX)**
- Finish ICP matrix & scoring system, including examples of too-technical vs. sweet-spot content

- Create concise 1-pager summary of ICP criteria

- Develop sales materials with specific discovery questions tied to ICP dimensions (DRI/champion, audience, technical depth, maturity)


**Bridget McGillivray (GrowthX)**
- Ask Sean about his involvement/investment in BlackSoul and implications for qualification


**Tyler Pavlas (GrowthX)**
- Start posting deals in Deal Desk channel for team review and qualification

- Refine waitlist language to focus on results alignment and realistic timelines, not technical capability

- Deepen qualification for seed-stage companies: validate ICP fit, content POV, and 3/6/12-month expectations before committing deal slots

---

## Transcript

**George Haikal:** Hey, George.

**George Haikal:** This meeting is being recorded.

**George Haikal:** What's up, man?

**Tyler Pavlas:** Nothing much.

**Tyler Pavlas:** Sorry for yesterday.

**Tyler Pavlas:** I was a little all over the place, but feeling good today.

**George Haikal:** You're good, man.

**George Haikal:** Feeling good is good.

**Tyler Pavlas:** Yes, indeed.

**Tyler Pavlas:** Could have used one of those magic things yesterday, that's for sure.

**George Haikal:** I've stopped feeling the air effects, unfortunately.

**Tyler Pavlas:** It's just your natural state, all of those nootropics.

**George Haikal:** Something like that.

**Tyler Pavlas:** What's up, Jason?

**Jason Gong:** Been a minute. How are you?

**Tyler Pavlas:** You're still drowning in deals.

**Tyler Pavlas:** Drowning in deals, but feeling much better about it. I love that we're all working together to figure out how to prioritize, and think this meeting will be really helpful for a lot of the deals that are close to closing.

**Tyler Pavlas:** The work with Understory looks like it's been doing great for the community.

**Jason Gong:** They're starting. I don't know how much I'd attribute to them. They're just like, you know, agencies. I can't say they're very productive yet. It's easy stuff, but I'm seeing a lot of activity from my LinkedIn without me doing anything, so I'll take that.

**Jason Gong:** I think it'll help. It just gives you more followers, and then whenever you decide to post something, people will see it.

**Tyler Pavlas:** Did you see the response I got from a guy who I knew who was like, Tyler, are you spamming me now?

**Jason Gong:** Yeah, they're doing that with me, too. I messaged Kirkland. They're not very good at cleaning the lists.

**Tyler Pavlas:** That's funny. Yeah, I saw that Kirkland gotten the list. So will they send that to you for a review each week?

**Jason Gong:** I think they send it to somebody, like Claudia, maybe. I haven't reviewed the list they've sent. For the most part, the copy is relatively unoffensive, so I'll just let them run with it.

**Tyler Pavlas:** Yeah, I didn't have any problem with the message that was sent. Would just want to take out people that I know really well. Let me message Bridget. I was waiting for her to join here.

**George Haikal:** Andy, how were the first two days back?

**Andi Bailey:** We had a lot happen.

**George Haikal:** Did we? There's always a lot happening.

**Andi Bailey:** Well, when you're not here, it hits you all at once.

**George Haikal:** Do you feel recharged, at least?

**Andi Bailey:** No, I got sick at the end.

**George Haikal:** Oh, no.

**Tyler Pavlas:** Yeah. The exact conversation Andy and I had on Monday morning, asked the same question.

**Andi Bailey:** Kyle said welcome back to me in the director's meeting yesterday. And I was kicking out all the note-takers, and I accidentally kicked him out. I was like, you don't welcome me back.

**George Haikal:** That's funny.

**Andi Bailey:** And then he couldn't rejoin, so we had to start a new meeting.

**Jason Gong:** That's really called for an AI.

**Andi Bailey:** Yeah, I was just like, you know, he was next to one.

**Tyler Pavlas:** All right, Bridget's here. Let's jump in. And so the goal today, I'm just going give you a quick overview of where we stand with current pipeline and priorities, and then we'll dive deeper and try to figure out who we want to prioritize for each slot after we go through a bunch of these pieces that I feel like if we discuss, we'll get closer to the answer faster.

**Tyler Pavlas:** So yeah, the deals that we've got going on right now. Kyle, I can see that Airbyte's progressing, but I don't have specifics. Doesn't look like anything's going the wrong direction. Like earlier conversations we had about making sure that we qualify the clients better, we're aligned on what kind of content they want us to create. We hadn't met with Redis in forever, and we're basically aligned on legal. So I set up a meeting with the main point of contact from the content team and also the head of marketing. And they added like a digital marketing manager. So one thing we can talk about a little bit is what information we want to get from Redis in my meeting tomorrow to validate that we want to move forward with them.

**Tyler Pavlas:** Cresta, Marcel responded to them and gave them an offer that was lower. They were pushing back on price. We had an early conversation with them when pricing was lower. He said $9K up front or $12K quarterly. I responded to that today to see if they would give us direction either way. This column, like, essentially ready to go. True Look, not getting back to me. Maybe not one that we're going to work with. Magic and Tango seem like really good fits. I'm really trying to make things happen with both. But it isn't clear if they're going to move forward yet. So I'm still trying to make sure that we win their business. Based on all the ICP conversations, they just seem like a great fit.

**Tyler Pavlas:** Obsidian, Marcel was on the first call. Seems like a good fit. Not as technical. Norm, always there if we need them. Zapier, we're scoping out the feasibility of the use case. I'm working with Kirkland and Stevie and the Zapier team. And Marcel gave me good guidance there. Navon, trying to reach alignment around some of their procurement stuff. But the good news is we don't have to get separate laptops or do all that ridiculousness they're proposing.

**Tyler Pavlas:** And then the last two. Tavis, reengaging with them tomorrow. They were super excited about working together. But based on their product and all the different AI avatars or whatever the heck it is that they have that you can make, I know the conversation was more like brainstorming less standard use cases, so I just need to make sure that one gets a little bit more on track.

**Tyler Pavlas:** Then Brex. Marcel really likes the content guy there. He even made a joke about trying to poach him from the team. And for them, it's like editorial and then this tools work stream, which Marcel built a prototype of in like 10 minutes. So I think that'll probably be like a 30K close because he wants to do all the procurement up front. But I'll continue talking to Marcel about that one to make sure we don't do anything out of our wheelhouse. That's the rundown on the closest deals. But I'll take any questions on like any of the deals and we'll talk about them again. So fire away if you got any.

**Tyler Pavlas:** Cool. We can keep it moving. Just mainly to catch y'all up to speed on some of these. George, I'll pass it to you if you could just maybe give the group an update on where the ICP work currently is.

**George Haikal:** Yeah, yeah, I definitely can. I'm just finishing adding one thing. I sent the link to you all here. So a few caveats, right? This will be ready tomorrow. But I wanted to get it to a point where it's still valuable for us to run through and get all of your feedback on. So let me share my screen.

**Tyler Pavlas:** Yeah, I'll stop. Sorry about that.

**George Haikal:** You got it. No, you're good.

**George Haikal:** So I'll explain quickly each piece of this and the work I've done so far and where I'm thinking it's lacking. And then we can go into like each one and where I want a lot of your input. Basically, as part of a project plan, I pulled seven of the team members. Andy was out, but I can pull you as well. Basically asked who was the easiest client for you to serve, who's the hardest, and why for both of those. And then who are the top three easiest and hardest and why.

**George Haikal:** So the way I'm approaching this ICP matrix is, how do we identify which clients are easiest for us to serve in the least amount of criteria or dimensions possible. Like what are the five things, if we get pretty much right, means we're going to have a successful engagement with the client. And so here you can look at the survey results from the polling and the similarities and what the top five dimensions from those results were. I also went through all of our churn, analyzed that, and then I pulled a job statement for each one. I've also gone through and spent a decent amount of time on it.

**George Haikal:** We're solving different problems for different companies. And so the ideal state is we have these dimensions and then a job statement tied to it. So you'll know what problem we're actually solving for when you intake a client. And then you can tie it to the dimensions, but that's just kind of supporting work.

**George Haikal:** And here's where I got started on each one of the dimensions. All this is open to feedback, but how I was thinking about it was my high-level goal is identify our sweet spot where we can add the most value for clients, and it's the easiest for us to deliver on. We have custom stuff we're doing. We have programmatic stuff we're doing. We have editorial work streams. Simplifying that to what's easy for us to deliver on and what we can actually scale on top of. And I do think these five capture a lot, but it's not everything.

**George Haikal:** Basically, the way I thought about it was number one by far is having a strong bot and champion or DRI. That is, and for many reasons. For you all, I'd suggest just reading the "why this dimension matters" section. And then I compared it to what easy looks like and what difficult looks like. I derived this from our client examples, my experience with clients, and all the polling I did. And I started to come up with discovery questions we could ask to understand whether a client meets this particular dimension. So this is the beginning of something that would help on a sales call. And it's derived from the questions we ask on our kickoff calls to get to the root of this.

**George Haikal:** There's a lot of other materials that will come out of this. I want to show you how I'm thinking about it for each one. And then there's a matrix that we'll be able to score each client on based on these dimensions. Weighted heavier towards the DRI, which I put at 40% as a placeholder. I'm finishing the matrix and the numbers today and tomorrow.

**George Haikal:** I've also added potential exclusionary criteria. The caveat here is I'm not confident in saying there's one thing that if a client has or doesn't have, would exclude them from being a good or bad client. I put everything that was in my head, the feedback I've gotten, or my experience with working with clients here. The way I thought about scoring was, if they have one, let's dig deeper and make sure there are no other ones. If they have more than one, then we should think about excluding them. Sometimes it's only temporary exclusion until our product gets better to actually handle some extremely technical clients like Clark.

**Andi Bailey:** Okay, check back in at 5.30.

**Bridget McGillivray:** Comments? Oh, it's 5.30 for you? That sucks.

**Andi Bailey:** Oh, yeah. Sorry. I forgot.

**Bridget McGillivray:** We're not in the same time zone. 2 p.m. I'm just starting my afternoon.

**Tyler Pavlas:** This is great, George. Thanks for doing this.

**George Haikal:** Yeah, I appreciate it. It's not done. We'd love your input, and then it'll be in a better and much more usable spot tomorrow.

**Tyler Pavlas:** George, on internal survey results and insights, number five, audience complexity and ICP clarity. Easy to serve is focused, unidimensional audience. Do we prefer clients who don't sell to multiple personas, basically? Is that what that means?

**George Haikal:** So that was feedback, and I can pull up the raw feedback as well. For like two of the clients, I think it was Tiro, and I think it was another one. Let me just pull it up so I don't misspeak. But it was favoring like one main audience with a couple specific personas versus a company we just kicked off that has like four different business segments that speak to another three personas each.

**Tyler Pavlas:** Okay, so one main audience with a few main personas.

**George Haikal:** That's what their feedback was. It's making them easier to deliver on.

**Tyler Pavlas:** Gotcha. We need a few more minutes, y'all.

**Andi Bailey:** Should we start talking about the non-starters? I mean, I've left a few comments, but I think the one through five dimensions make a lot of sense to me.

**George Haikal:** Yeah, I didn't see too many comments on one through five that were against or super different opinions, so yeah, I'm fine starting with the non-starters.

**Tyler Pavlas:** Cool. Perfect.

**George Haikal:** All of these, I wouldn't say 100% yes to if someone doesn't have a CMS, but that's why we're all here talking about it. Biologica and Pound are examples of clients that we've had success with that maybe now they don't feel super ideal, but at the time we used them as company examples, and they're relatively easy. They didn't have a CMS, but I agree. I think more importantly, this should signal more questions that we have to ask. Like, if they don't have a blog, how are they thinking about content? What do they actually want? How empowered are they for GrowthX to take control and set the strategy?

**George Haikal:** But, I mean, if I had to choose one, this is why it's number one. Like, apples to apples, someone has a blog and a CMS, and someone doesn't. And it's a yes or no decision. Like, that makes it easier for me.

**Tyler Pavlas:** Part of the challenge is that there'll be accounts that will have longer procurement processes. That will be targets because of the logo, because of the likelihood for the business to grow, to have more work for us to do, to renew. And like, we might identify that's like a seed stage company, and hasn't created a lot of content. And so if I put them in the spot, then I'm pushing back further and further and further the more strategic logos.

**Tyler Pavlas:** And in these situations, I'm definitely trying to do editorial only and be done with anything outside of that. But that's like the challenge. I think like, I want to use BlackSoul as like an example, because BlackSoul is a client that would pay us the $30K for editorial. They have the blog on Notion. They're having CMS conversations, and would transition to a new CMS. They'd set up a blog. The content that they want us to create is in our wheelhouse. They're super aligned. But it's a technical company. It's seed stage. So the decision for me becomes do I take that slot when I know that I could push harder on Magic and Tango instead, which I think are like much better fits.

**Tyler Pavlas:** I think like the reason I say we don't have to ever bring a seed stage company on again is because it would take the place of like a Series A, Series B plus opportunity. I have 70 deals that I'm working on right now. And I would say that like 40 plus of them we could get as close to closing if we just like try harder.

**George Haikal:** The point George is making about the exclusionary criteria is that they signal questions, not hard stops.

**Tyler Pavlas:** Yeah, I still can't look at blogs and know if it's too technical. I know that their blog isn't necessarily what we would be doing. But what I'd like to be able to do is look at that blog and know whether or not it's too technical. And I just don't feel like I can do that right now.

**Jason Gong:** Yeah, I remember Cast the Eye. I feel like this is a pretty easy comparison. Comparing cloud providers is easy. The ones I saw were more like DevRel type content. The difference is, if you read it and it sounds generic versus it sounds like something you read on Hacker News. If you read something on Hacker News, like, you just wouldn't be able to write it. But if you compare cloud provider A with cloud provider B, like, we can write stuff like that. So the question is, can we do more of what's on their blog?

**Tyler Pavlas:** I think, George, if you can continue to provide more specificity around what's too technical. Examples of what's too technical, examples of what's in a sweet spot. Like, just the word Kubernetes, I just see that and go, we don't want to do this.

**Jason Gong:** Let me open it and share my screen to look at Panther.

**Andi Bailey:** Link to Panther. Man, what a name.

**Jason Gong:** What are we naming things, these guys?

**Tyler Pavlas:** Yeah. Let me just ask George. So if I look at this Panther content, right, is this something we can reasonably do? Or is this too technical?

**George Haikal:** Yeah, looking at it, some of this is doable. Like, the first few paragraphs could work, but yeah, there's a lot here that gets beyond our wheelhouse. Like, okay, I think the way to frame this for George is like, if I compare the difficulty of this content to like, the difficulty of let's say, Panther's API docs or something like that, we're positioned closer to what they have than to their docs. So it's not like we can't do any of it. It's just that we'd need to scope it down and make sure we're clear on what we're doing versus what they're doing.

**Tyler Pavlas:** Yes. That's the distinction I needed. That's helpful.

**Tyler Pavlas:** Any other questions on anything?

**Tyler Pavlas:** Okay. So, we'll get into Deal Desk and qualification faster. But before we do that, Bridget, do you have any thoughts on like the overall ICP framework?

**Bridget McGillivray:** I think the DRI dimension is the biggest predictor of success. Like, we've seen that across our portfolio. When there's a clear DRI, projects are so much cleaner, faster, better outcomes. So yeah, I definitely think that's the right weight.

**Tyler Pavlas:** Yeah, the DRI is like the gateway. Like, everything else kind of falls into place if you have that.

**Tyler Pavlas:** Okay, so we'll talk a bit about the Deal Desk channel now. I want to keep things moving. We know we're struggling to make good qualification decisions on the fly. So the idea with Deal Desk is every deal that we're considering, we'll be posting in there.

**Tyler Pavlas:** That way, everyone can see it, everyone can think about it, everyone can add their expertise. And we can make faster and better go/no-go decisions on a deal without me being the sole arbiter of every single deal.

**Tyler Pavlas:** So what I'd like from each of you is just your expertise in the Deal Desk posts.

**Tyler Pavlas:** Like, Andi, I'd like to know, like, from a delivery and resource perspective, like, is this doable? And then, George and Jason, I'd like to know like, from a technical perspective, like, is this content too technical for us to create? And then, like, Bridget, I'd love to know from you like, does this fit the ICP, and is it a good fit for the team based on what we're trying to do?

**Andi Bailey:** Yeah. And I would add, from a resource perspective, like, do we have capacity? Like, what does it mean for the team if we take this deal?

**Tyler Pavlas:** And like, that kind of cascades down to a few other things I want to ask. What are the key qualifications we should be looking for? And from the qualification, like, I want to understand, like, what are the conversations we should be having with prospects? Like, what are the open questions that will help us understand if a prospect fits the ICP?

**George Haikal:** Key questions on Spect Ops or Redis. Anything to add other than just looking through the docs in detail, George, and making sure I cover as much of that as I can? I think we've talked this through. I sort of know what to do, but anything else I should have to talk about?

**George Haikal:** Just so my brain doesn't miss something. Is there anything that you all think would be most helpful for me to focus on outside of the matrix and the scoring system to make this more actionable? To get this to a better spot where it's more usable? I'm going to do a one-pager that's much more concise. It's going to be a matrix where we can actually score and easily see. And then it'll be materials. Once those are done, it'll be materials for sales, like a checklist of questions. And what are those questions getting at? And what answers are you looking for? And then same thing for kickoff and like delivery. All organized by workstream as well as client.

**Bridget McGillivray:** That's the main thing for me is collateral for Tyler. Like there's too many questions here almost. Like we need to just decide on the questions.

**Andi Bailey:** And then on my end, like what for existing clients, like helping us get to a decision on what does it mean for engineering when a client is outside of our ICP. What does it mean for design resources? Like what does it mean for our teams? Are we giving them something, or do we just have like a garbage pod where somebody manages like 17 clients and they get what they get when they get it?

**George Haikal:** Wouldn't we point them to our product eventually?

**Bridget McGillivray:** Well, I, the other thing we're doing in parallel, I think we'll have more clarity on that in a bit. Cause like the other thing we're doing in parallel is like role definition and like everyone filled out their jobs to be done. And the main takeaway from me is that we do like a ton of stuff for clients and some people are paying us $6,000 for like an entire marketing team of work. I think we will probably move to a world where we have like tiers of customers and probably like a la carte. So I think it's related to this combo as well. Like we might probably just have to hold on to these clients for now. And then like, yeah, we might put them in a different pod later that's scoped down. And then they're easier to serve for that reason.

**Andi Bailey:** You don't like my garbage pod label.

**Tyler Pavlas:** Garbage pod.

**Andi Bailey:** I really like that.

**Bridget McGillivray:** One thing like that, I think we also need to work on as an action item is just the, how we want to frame the waitlist and just like a little bit of process there. So sort of related to any source, but also Jean's email, like we don't want to come off that we can't do technical clients. Like that makes us look bad and that's not true. So we just need to maybe Tyler, can like iterate on some of the language.

**Andi Bailey:** Yeah, I would talk about like that results alignment of just like work. We want to make sure that we can like get to success within like the timeframe that you're looking for or something like that, like align on the goal.

**Tyler Pavlas:** Yeah, maybe that can be part of what I'd put in Deal Desk is what they tell me about, you know, where do you, like, what do you expect to see 12 months from now in terms of results from working with GrowthX, basically. And that answer can guide how realistic it can be.

**George Haikal:** I think even at 3, 6, and 12, like, you know, like, what are the early wins they're expecting, right? And how reasonable or unreasonable are they? And then long term, what are they expecting as well?

**Tyler Pavlas:** Yeah, the challenge is that, like, they always ask, like, well, what is the typical ROI that your clients see? And it's like situational, you know? Yeah, I've gotten better at answering that question by not answering it.

**Tyler Pavlas:** Okay, one more thing, if y'all wouldn't mind here. I think it would be helpful if I put this in the doc. But George, this might help you as you're making the new criteria and looking through the weights. Like just kind of seeing how the ones that score high, they're just very different from each other, right? With all these criteria, it would be a good thing to look through.

**Tyler Pavlas:** And you know, the reason that I say we don't have to ever bring a seed stage company on again is because it would take the place of a Series A, Series B plus opportunity. I have 70 deals that I'm working on right now. And I would say that like 40 plus of them we could get as close to closing if we just like try harder.

**Tyler Pavlas:** I'm not like not responding to them all the time, but I just think, and the context you gave, Jason, was super helpful in that thread, but I still can't like look at blogs and know if it's too technical.

**Jason Gong:** Yeah.

---

_Transcript cleaned: removed standalone filler lines, consolidated fragmented speaker turns, fixed obvious transcription errors. No substantive changes to speaker content._
