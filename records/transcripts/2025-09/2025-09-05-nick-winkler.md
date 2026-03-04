# Nick Winkler

<metadata>
date: 2025-09-05
time: 18:31 UTC
duration: 30 minutes
organizer: kyle@growthxlabs.com
participants: Kyle Gaudreau (GrowthX), Nick Winkler (Okta)
fathom_recording_id: 85380330
fathom_url: https://fathom.video/calls/396692614
share_url: https://fathom.video/share/WxUKkM_CXo8N98tm4oWxvMkGKENFDgxd
source: fathom
enriched_on: 2026-03-02 10:15 UTC
</metadata>

---

## Summary

Kyle Gaudreau introduced GrowthX's AI-powered SDR manager gem to Nick Winkler at Okta, a tool designed to accelerate account research and personalized outreach by synthesizing research data and forcing critical thinking beyond surface-level data. Nick shared his current SDR workflow — managing 750-800 relevant accounts out of 1,500 in Salesforce, prioritizing by industry and financial health, researching with Sales Navigator and SimilarWeb — and highlighted three key feature requests: web search to catch real-time signals (e.g., new loyalty programs), automated signal updates without manual gem recreation, and scalability beyond retail to other industries like software. Kyle confirmed the team is exploring more programmatic approaches to make account list ingestion easier and is still refining the delivery model.

---

## Context

Nick Winkler is an SDR at Okta, where he's been piloting GrowthX's SDR manager gem as part of a content marketing engagement. Okta recently brought on their first external AE and is building out their outbound sales motion. Nick reached out to GrowthX (referred by Rachel) after seeing the Akamai retail motion — a campaign GrowthX has been running in the UK/Ireland region. He's been testing the gem with accounts like Cole Haan and appreciates the "manager" approach that forces SDRs to synthesize research and develop their own insights rather than just copying pre-written briefs. This first pilot call with Kyle was to gather feedback on the tool's delivery, brainstorm feature gaps, and discuss challenges with account list compilation and signal updates across Okta's large territory.

---

## Relevance

- **To GrowthX Delivery:** SDR manager gem is working for pilot users but needs web search integration and automated signal updates to scale. The "manager" forcing critical thinking is a key differentiator. Account brief structure (personas, pain points, leverage points, discovery questions) is resonating but needs refinement and customization by user feedback.

- **To GrowthX Business Development:** Nick is preparing a Wednesday presentation to the Okta SDR team showcasing how to use the gem — high leverage moment for buy-in. Okta has 1,500 accounts but only 750-800 are truly relevant; there's opportunity to expand beyond retail into software and finance verticals. Internal friction around account list compilation and gem updates could become a barrier if not addressed programmatically (e.g., Clay workflow integration). Kyle mentioned continuing to refine how briefs are generated and delivered.

- **To CheckThat / AEO:** Not directly discussed, but Nick's focus on real-time signal detection (loyalty program launches, login changes, traffic patterns) aligns with CheckThat's AI visibility value proposition for detecting emerging opportunities.

---

## Overview

- Nick is excited about the SDR manager gem's potential to streamline account research and personalized outreach
- Current pain points include account prioritization and efficient signal identification among numerous accounts
- Future improvements could include web search capabilities, automated signal updates, and scalability across industries

---

## Key Topics

### Current SDR Workflow and Challenges

- Nick manages 750-800 relevant accounts out of 1,500 in Salesforce
- Prioritizes accounts based on industry (retail, finance), financial health, and potential impact
- Time-consuming to manually research and identify signals for numerous accounts
- Uses tools like Sales Navigator and SimilarWeb for initial research

### AI-Powered SDR Manager Benefits

- Excited about the gem's ability to provide account breakdowns and leverage points
- Appreciates the "manager" approach, forcing critical thinking beyond just using provided research
- Potential to significantly speed up custom messaging at scale

### Desired Improvements and Questions

- Web search capabilities to find recent, relevant information (e.g., new loyalty program announcements)
- Automated signal updates to keep information current without manual intervention
- Scalability to apply the workflow beyond retail accounts
- Concerns about the time required for SDRs to compile account lists for the system

### Account Research Process Demo

- Demonstrated research process using Cole Haan as an example
- Checks Salesforce for customer type and past interactions
- Uses Sales Navigator to identify company priorities
- Examines login process for potential improvement areas
- Utilizes SimilarWeb for traffic data and user engagement metrics

### Collaboration with AEs

- Varies based on individual AE's experience and motivation
- Some AEs actively participate in outreach, while others are less aggressive with new business

---

## Action Items

**Nick Winkler (Okta)**
- Prepare presentation for Wednesday showcasing how to leverage the SDR manager gem — demonstrating value to Okta SDR team

- Check with Rachel & Eric regarding timeline for accessing his own accounts in the gem before Wednesday presentation


**Kyle Gaudreau (GrowthX)**
- Schedule follow-up meeting with Nick for further discussion and feedback on SDR manager tool

---

## Transcript

**Kyle Gaudreau:** Yeah, appreciate you being flexible. Sorry to have to move everything — it's been a weird week.

**Nick Winkler:** No problem. I appreciate it. We brought on our first AE and he was in town, had a big event yesterday, so my schedule got really weird yesterday, but all exciting things.

**Kyle Gaudreau:** So, real quick about me. I've been jumping into this engagement, which is kind of interesting. I've done a whole variety of things here at GrowthX. I was leading the client services side for most of my tenure. Then we needed to move away from founder-led sales, and I was helping stand up that side of the business. Now we have our first AE, so I can kind of get out of that a bit and actually dive into helping execute the work.

**Nick Winkler:** So my background is actually more in stuff like this. I've led groups at a variety of different places before this.

**Kyle Gaudreau:** And so, you know, we're continuing to kind of build this engine, build these experiments, figure out the right places and how this needs to be adapted.

**Nick Winkler:** How much background have you gotten so far from Rachel? I want to make sure we start in the right places.

**Kyle Gaudreau:** She was telling me about the retail motion that you guys have been doing within the UKI region.

**Nick Winkler:** I use AI in my job to help accelerate my workflow, honestly very similarly to what you guys have designed with the SDR manager, though not nearly as fleshed out. Rachel has explained to me how you're using hooks, where you're getting these signals from. I have a high-level understanding of what's happening on the back end so I can use Gemini effectively on the front end.

**Kyle Gaudreau:** Cool, got it. So part of my aim on this discussion is to get feedback from you, but I'm also happy to answer any key questions you have. We still have a few ADP refinements in this experiment itself, and I think there are likely doors for future experiments as well. But have you had a chance to see the briefs we created for some of your accounts yet?

**Nick Winkler:** I know we shared it with Eric. I'm taking a look at the UKI ones that were made because I was testing out the gem actually last week and this week, but no, I haven't seen anything in terms of the accounts that I'll be using.

**Kyle Gaudreau:** Got it. Let me go back and look at this thread to make sure I'm not making stuff up.

**Nick Winkler:** Eric and Rachel said mine might be expedited because I was helping pilot it.

**Kyle Gaudreau:** So these accounts here in this thread — are these your accounts?

**Nick Winkler:** Yes, those are all mine.

**Kyle Gaudreau:** Okay, cool. So let's take a look. We don't have to go through this slide, but I'm just curious as you dive into this. You may have already seen this structure, but right now the delivery is this account brief and then a cold outreach resource. The brief is synthesizing a lot of the different things you were mentioning — giving a summary, who are the key personas, what are some key pain points that could stand out, trying to find the intersection points between what you all do best and what could be unique, focusing on signal frequency, potential guidance and discovery questions.

**Nick Winkler:** One thing I loved about testing out the SDR manager was that before I realized my accounts weren't in there, I tried it with Cole Haan. And it gave me a decent breakdown even without that information. But what I really appreciated was that it's acting as a manager, asking things like "What sticks out to you as the best signal on this account? What's something that changed recently that you think is a good leverage point?" I love that. Something I'm guilty of is loving to use AI to accelerate my workflow, but what I love is that this forces me to take my own considerations into account, not just "here's account research, now I'll use that to create messaging." That was a huge highlight for me.

**Kyle Gaudreau:** Yeah, go ahead. What are your questions?

**Nick Winkler:** Well, I want to preface by saying some of this stuff I don't know if it's GrowthX doing on your side or Rachel. I know within the Gemini gem in particular, web search hasn't been something I've been able to do. I discovered that through testing Cole Haan — I wasn't able to pull other resources. I had an assumption that the amount of documents we're inserting into that gem might prevent it. But when it comes to updating signals, and Rachel and I talked about what that might look like, that's one of the main drivers for me — being able to have updated information without having to manually recreate or update that gem by hand. I know SDRs that might not be as cognizant of continuously updating and might just get stuck. And then there's replicability outside of retail. I think this is going to be a huge fan favorite among the SDRs and my team, and their number one question is going to be "How can I apply this to my next account or industry?" We'd have to address the fact that we're not pulling in leads and accounts and allowing GrowthX to build that out, but those are the things on my mind.

**Kyle Gaudreau:** You're good, you're good. All of those things were top of mind. So, a clarifying question — can you give me an example of where web search is really helpful for you?

**Nick Winkler:** Yeah, it ties into updating signals too, and actually it ties into all of it. So, for one, I love the SDR manager and the workflow, but there might be an account in software that I really want to prospect into, but obviously we don't have that built out for anything outside of retail and the Akamai use case. When it comes to updating signals, Rachel has a timeline for V1, V2, V3. But let's say Cole Haan announces a loyalty program two weeks from now. That's not something we'd have the foresight to add right now. But if I were using the gem with Cole Haan again, it'd be awesome if it said "Actually, there's a recent announcement. Here's a new signal that they're entering the loyalty space. This is a great signal for us to go after."

**Kyle Gaudreau:** Yeah, that's interesting. There's kind of a social listening angle to it. If you're able to pick up on something timely, that's a compelling point of outreach.

**Nick Winkler:** And that's something I'm doing naturally. I'm not sure how familiar you are with the Altura product suite, but there are recent products where agentic AI use cases are huge, so I've been diving into that. When I think of how we can continue to update these signals and provide them into those documents, I'm lighting up with an agentic use case. I know enough tech to be dangerous to get someone in a meeting, but not enough to tell you how our tools work on the back end. But I'm imagining a way where we surf the internet with an agent and have it update our docs, which then automatically updates within the gem. We've got Auth0 workflows for that, so it seems possible, but that's why we're talking.

**Kyle Gaudreau:** Theoretically, for sure. There's complexity around what we read and write, and that's where gems come into play. Some of the things we're trying to think through with Rachel — we're taking a lo-fi version approach for now. How do we make that evolve through conversations like this? As we understand better, we can figure out if gems is the most ideal solution or what that looks like. I'll have this conversation with Rachel this week. It's not my favorite option when it comes to this.

**Nick Winkler:** But understandably, accessibility is why you leaned into it. I get that.

**Kyle Gaudreau:** So how many accounts do you have?

**Nick Winkler:** It's hard to answer because our Salesforce is a dumpster fire, in my opinion. At face value, I have 1,500. But I'd guess that number is closer to 750-800 in terms of accounts that are truly mine and should be mapped to us. The other reason is that OCTO and OCTO separated this year, which essentially doubled the number of accounts for everybody because now there's two people working each account.

**Kyle Gaudreau:** A lot of those accounts aren't worth using a workflow like this, no matter how fast. We've been talking about target accounts. How does that align with how you think about things within that 750?

**Nick Winkler:** For how I'm approaching my territory, I'm a huge believer in the 80/20 rule — 80% of your work comes from 20% of your accounts. A lot of that comes from industry. I've had calls with Spencer's — that grimy retail shop in the malls. I got on the phone with them and they had the use case. Their customer identity is weak. We could do a lot for them. But at the end of the day, everything they sell is a Chinese input and they've canceled every project. I look at: Does this company have money? Will this improve their business? But ultimately, industry is the first place I look. Retail is a perfect alignment. Finance and insurance is great. And when we have stuff like Akamai, where we know we have a place and a use case, we're diving in there.

**Kyle Gaudreau:** So how does account list compilation work? We've been thinking about the scale challenge.

**Nick Winkler:** I had the foresight to build out a system that made my life easier when it came to putting together my accounts and leads. Not everyone did that, and there was definitely a lot of friction for some of the SDRs just putting these lists together. I think to get buy-in internally from Okta, a big part will be how we approach this in a scalable way. I know some people probably spent 10 hours on it because they did it in the least practical way.

**Kyle Gaudreau:** What today do you feel like is your biggest time suck? If you could do X but Y is preventing you, what is that?

**Nick Winkler:** The vast number of accounts we have creates paralysis by analysis. I have so many accounts to go through, and I know the majority are going to be pretty bad. It's very difficult to find signals organically in our research, especially at the account level. That takes away a lot of my time. But what I'd love more time to do is exactly what this SDR manager gem creates — send out custom messaging at scale. I've already been able to do that faster building gems on my own, but with the SDR manager gem, that's what's getting me super excited. The output is improving a lot too.

**Kyle Gaudreau:** Love it. Not to put you on the spot, but could you show me some of that live? I'm just trying to find patterns that could give me some aha moments about how we could approach this.

**Nick Winkler:** I'll use Cole Haan because why not? So, first thing I'll do is check their status in Salesforce — are they a workforce customer or customer identity? They're a workforce customer. Next, I check if we've had a conversation with them around customer identity. We haven't. Then I look them up in Sales Navigator to see what matters to them right now. I try to pull something that could be Auth0-related, something we can help on the customer identity side. I'll see things like their main driver is customer experience, which excites me. I take that with a grain of salt though — something like "quality of footwear" isn't great for me.

**Kyle Gaudreau:** Do you find that typically accurate?

**Nick Winkler:** Typically, I take it with a grain of salt. Then I check what their login looks like. I'm a snob when it comes to customer identity. I see they're still using username and password, which blows my mind. So then I think, okay, what am I seeing where Auth0 could make this better and provide a business use case? I notice they have username and password, then you try to join and there's a second page with a registration form. In my head, that feels like the beginning of a loyalty program. How can I position us as a loyalty program builder? Working with Rachel, I know about cookie permission changes and how our ability to gather first-party data is a major use case once those cookies change. So I keep notes like "no social login, pretty extensive registration experience." And one last thing I usually do is use SimilarWeb, which tells me their users and rough estimate. I see 3.9 million visits last month. That doesn't line up perfectly with our business model, but I'm looking for whether they have enough users accessing their website that they'd invest and there's value for us. For Cole Haan, I typically take 25-30% of that number as unique visits, though for retail it's probably higher. When I see that, I'm like yeah, that's acceptable for us. I also look at bounce rate — if it's high, that's a huge login use case. High bounce rate means their logins are frustrating users so they don't want to spend time and just go to Amazon instead. And a red flag for Cole Haan is that almost every engagement we've had has been through a partner, so that factors into my ability to get in contact with them directly. I've pushed to get in contact with our SHI rep, but my account executives haven't been as aggressive on it as I have.

**Kyle Gaudreau:** How does coordination work with the AE typically?

**Nick Winkler:** It depends. One of my buddies has a rep who just got promoted and is still early in his career, so he's still very hungry. When they plan for the week, he's doing outreach too. If my friend brings in an idea to get in touch with a partner, the AE will be aggressive with it. I'm in a place where most of my AEs later in their career have been very successful and are not quite as hungry or aggressive in pursuit of new business. We had a good quarter so we still had business to bring in. But outside of current customers, a lot of our reps later in their career are less aggressive in bringing new business.

**Kyle Gaudreau:** Understandable. Some human nature behind that. Well, this was really helpful. Is there anything else on your mind?

**Nick Winkler:** I'll have some follow-ups, so I'd love to pick your brain another time. The only thing I'm really thinking of is timeline on getting access to test the gem with my own accounts before I present on Wednesday.

**Kyle Gaudreau:** That might be a question for Eric and Rachel. I'm not as dialed in on how they're operationalizing that. The key is making this more programmatic. Our focus has been on dialing in the briefs and getting the right content, refining it, and exploring where this should live. Right now the team comes to us and says "I want you to run these accounts," which probably isn't ideal. I'd love to be at a place where you can dump in a list within Clay, configure endpoints into our workflows, define inputs and accounts and context, the workflow runs and spits out the brief, then that lives in your Octosphere and plugs into other systems like gems.

**Nick Winkler:** We haven't quite gotten there yet, but yeah, if we're always operating manually, I don't think this will have as much value as what's possible. But I loved hearing that because being able to replicate this outside of just the accounts we're starting with sounds like a step in the right direction. I have access to the drive Rachel has for this, so I'll keep an eye out. I was looking at it earlier but didn't see them. Knowing Rachel and Eric have them now, I'll go bark up that tree and see if they can get me going.

**Kyle Gaudreau:** Cool. Let us know if you run into friction or misalignment. We're clearly still trying to refine and make this more repeatable.

**Nick Winkler:** Yeah, super appreciate you taking the time.

**Kyle Gaudreau:** You have us in the channel. If anything comes up, hit us up.

**Nick Winkler:** Awesome. Yeah, we can figure it out offline, but if you want to throw time on with that link, maybe just message me and we can figure something out.

**Kyle Gaudreau:** Yeah, I'm happy to help. I'm really excited to be a part of it.

**Nick Winkler:** Yeah, please. Sounds like a plan.

**Kyle Gaudreau:** All right, dude. Well, enjoy the weekend and chat again soon.

**Nick Winkler:** Sounds good. Take care. Have a good weekend.
