# Meeting w/George (Vivian Liu)

<metadata>
date: 2025-08-28
time: 21:03 UTC
duration: 65 minutes
organizer: george@growthx.ai
participants: George Haikal, Vivian Liu
fathom_recording_id: 83723706
fathom_url: https://fathom.video/calls/394804479
share_url: https://fathom.video/share/sbMExzD8ksniwWaMp1tbwpxTNqnaoTp_
source: fathom
enriched_on: 2025-03-03 00:15 UTC
</metadata>

---

## Summary

George and Vivian discussed Vivian's struggles with structuring AI prompt engineering for Mae's vehicle recommendation system, which uses wearables to capture customer conversations in dealerships. George shared GrowthX's step-by-step AI workflow approach, emphasizing that breaking down complex tasks into granular steps with individual prompts at each stage creates consistency and repeatability. Vivian committed to whiteboarding her entire process, and George will arrange an introduction with Daniel (GrowthX CTO) after the fundraising push to help Vivian refine her technical strategy.

---

## Context

Vivian Liu is building Mae (Making Auto Easy), a startup using AI-powered wearable devices in automotive dealerships to analyze customer conversations and recommend vehicles. George Haikal is at GrowthX during a major Series B fundraising push that has compressed timelines and created company-wide time pressure. The two have a pre-existing relationship—George has mentored Vivian on product strategy and GrowthX's AI methodology. Vivian is currently the expert on her own business domain (customer interactions, vehicle inventory, sales dynamics) but lacks depth in enterprise AI systems design, which is why she's seeking guidance from GrowthX's CTO Daniel. This is a peer-to-peer catch-up that evolved into technical advisory on a critical business problem.

---

## Relevance

**To GrowthX Delivery:**
- Vivian's challenge with prompt layering and step-by-step workflow design mirrors problems GrowthX solves for enterprise clients. Opportunity to document GrowthX methodology as a case study.
- George shared GrowthX's confidence scoring, self-evaluation loops, and multi-model orchestration (Claude, ChatGPT, Perplexity) as the core intellectual property. Mae could become a reference implementation.
- Inventory enrichment pattern (connecting customer psychology to product attributes) is directly applicable to other GrowthX workflows.

**To GrowthX Business Development:**
- Mae is early-stage and founder-led, post-wearable implementation but pre-product-market fit. Series A candidate if AI layer scales.
- Vivian is hiring a CTO and building a technical team; potential future consulting or platform engagement once fundraising closes.
- George's mentorship and Daniel's advisory could lead to deeper technical partnership or equity opportunity.

**To CheckThat:**
- Mae's vehicle recommendation system is a pure AEO use case: structured data + conversational AI + outcome optimization. Potential for CheckThat integration if Mae scales to multi-dealership networks.
- Wearable-captured transcripts are high-quality training data if Mae ever wants to build proprietary LLMs.

---

## Overview

- Vivian is struggling with structuring and refining AI prompts for vehicle recommendations
- George shared insights on GrowthX's AI workflow process, emphasizing a step-by-step approach
- Vivian plans to break down her process into more granular steps and possibly consult with Daniel (GrowthX CTO) for expert guidance

---

## Key Topics

### Mae's AI-Powered Vehicle Recommendation System

  - Vivian implementing wearable devices in dealerships to capture customer conversations
  - System analyzes transcripts, customer profiles, and inventory to recommend vehicles
  - Challenges in prompt engineering and result validation
  - Current process:
    1.  Gather input (transcript, guest sheet, inventory)
    2.  Generate customer summary with AI insights
    3.  Use large prompt to generate 5 vehicle recommendation scenarios
    4.  Manually review and iterate on results

### GrowthX's AI Workflow Process

  - Utilizes a step-by-step approach with individual prompts for each stage
  - Implements confidence scoring and self-evaluation loops
  - Uses various AI models (Claude, ChatGPT, Perplexity) for different tasks
  - Emphasizes the importance of breaking down complex tasks into smaller, manageable steps

### AI Tools and Best Practices

  - George recommends using Claude for document understanding and writing tasks
  - ChatGPT useful for structuring information and creating tables
  - Perplexity AI suggested for research tasks
  - Importance of providing context and examples in prompts
  - Continuous iteration and refinement of prompts based on output quality

### Fundraising Update

  - GrowthX pushing timeline for Series B
  - George involved in various aspects: documents, materials, scheduling meetings
  - Fundraising taking priority, causing general busyness in the company

---

## Action Items

**Vivian Liu (Mae)**
- Break down AI process into detailed steps. Whiteboard each stage (transcript analysis, inventory matching, recommendation generation). Create Excel/chart view of workflow. (00:46:49)

- Prep for potential call w/ Daniel (GrowthX CTO). List specific Qs, tech details. Determine abstraction level for discussion. Consider inviting Japheth. (01:02:10)


**George Haikal (GrowthX)**
- After fundraising (next week), arrange intro call between Vivian and Daniel (GrowthX CTO) re AI implementation strategies and system architecture. (01:01:15)

---

## Transcript
**Vivian Liu:** This meeting is being recorded.

**Vivian Liu:** Hey, I need like one second to send a text, okay?

**George Haikal:** Yeah, take your second.

**George Haikal:** It's a ghost.

**Vivian Liu:** Oh, how are you?

**George Haikal:** I'm good.

**George Haikal:** It's been crazy.

**George Haikal:** I'm Maya, but it sounds like with you too.

**Vivian Liu:** Yeah, I've been kind of having a crazy day today.

**George Haikal:** Why?

**Vivian Liu:** I accidentally lost my ring box that has both my wedding band and my...

**Vivian Liu:** And then, so I dropped it just outside of my friend's place.

**George Haikal:** Where were you holding it?

**Vivian Liu:** It was in my purse.

**Vivian Liu:** I was, like, leaving their place.

**Vivian Liu:** stayed overnight.

**Vivian Liu:** And then I was, like, moving things around.

**Vivian Liu:** And then in their video, you can see me, like, dropping it accidentally.

**Vivian Liu:** I didn't notice until I was, like, long gone.

**Vivian Liu:** And then they had someone come to the house.

**Vivian Liu:** That was pet sitting for them.

**Vivian Liu:** So then she finds it.

**Vivian Liu:** There's a video of her picking it up.

**Vivian Liu:** She's super hard to talk to.

**Vivian Liu:** She's, like, yeah, I have it.

**Vivian Liu:** Like, like, she texted saying, like, yeah, like, I was going to post it on whatever Lost and Found.

**Vivian Liu:** And then she, like, doesn't answer since 11 o'clock.

**Vivian Liu:** So it's been, like, almost three hours.

**Vivian Liu:** So she just messaged.

**Vivian Liu:** She took a ferry to, like, the mainland, which, so I missed my.

**Vivian Liu:** Ferry this morning, waiting for her to come back, maybe.

**Vivian Liu:** So now I have no idea where she is.

**Vivian Liu:** And she texts me.

**Vivian Liu:** She goes, hi, like, you're welcome.

**Vivian Liu:** Glad to find this owner.

**Vivian Liu:** I just got to the Schwartz Ferry.

**Vivian Liu:** I'm away for the weekend, but we'll get better back to you one way for another next week.

**George Haikal:** She's treating it way too casually.

**Vivian Liu:** Way too casually.

**Vivian Liu:** If this was a sweater, sure.

**George Haikal:** Like, this is, yeah.

**Vivian Liu:** Yeah.

**George Haikal:** Both extreme financial and sentimental value.

**Vivian Liu:** Like, she's treating it so casually.

**Vivian Liu:** Like, you couldn't have, I called multiple times.

**Vivian Liu:** You couldn't just be like, hey, like, I got it.

**Vivian Liu:** Like, I'm going here.

**George Haikal:** I'll be here. Yeah, that's frustrating.

**Vivian Liu:** Yeah.

**George Haikal:** Some people just operate differently, Viv.

**Vivian Liu:** I know, but what if she's just like, I'll bring it back to you, like, one way or another next week. Next week? Don't like. What if she sloughs the diamond?

**George Haikal:** Like, I'm panicking.

**George Haikal:** Sloughs the diamond?

**George Haikal:** I would not have thought about that in a hundred years.

**George Haikal:** That's a thing someone would do?

**George Haikal:** Do you, does your friend, is like, is she a reputable pet sitter?

**George Haikal:** Like, is she a friend of your friend?

**Vivian Liu:** No, it's not a trusted house sitter, so some random person.

**Vivian Liu:** I think it's verified through, like, the third party, but I creeped, I found, I found her last name, so, like, it fulfills I know who she is, but, like, there's no way for me to, like, yeah, I know, I'm probably overthinking it, but.

**George Haikal:** Just send her, send her her address to her and be like, just make sure I get this back next week, okay?

**George Haikal:** That image of her home.

**Vivian Liu:** My gosh, then she'll disappear with it for good.

**George Haikal:** Yeah, wait, that's, okay, that changes things.

**George Haikal:** I thought it was a friend of your friend that was coming over to dog sit.

**Vivian Liu:** No, no, no, no.

**Vivian Liu:** If it was a friend of mine, I'd be fine.

**Vivian Liu:** Um, anyways, just  respond to me.

**Vivian Liu:** Um, fundraising.

**Vivian Liu:** What's your, that sounds fun.

**George Haikal:** It's crazy.

**George Haikal:** Yeah.

**George Haikal:** series B pushed the timeline up.

**George Haikal:** I was going to be, sorry, I'm just declining this call.

**Vivian Liu:** You can take it.

**George Haikal:** Sorry.

**George Haikal:** No, no, no, no.

**George Haikal:** My mother, she can wait a long time.

**Vivian Liu:** No.

**George Haikal:** Oh, you're back.

**George Haikal:** I'm at work.

**George Haikal:** It's so early in the day.

**George Haikal:** I don't know what she's doing.

**George Haikal:** Um, but yeah, it's crazy, but the number is really big and it's like a really big push and it's all looking good.

**George Haikal:** So it kind of, that just jumps to the top of the priority list of, um, everything kind of.

**George Haikal:** So everyone's rushing around this week and next, but all good things.

**Vivian Liu:** part to play for fundraising?

**George Haikal:** play Um, Um, Um, Um,

**George Haikal:** Yeah, little bit of everything.

**George Haikal:** Documents, materials, actually getting the meetings on the books.

**George Haikal:** Nothing like in terms of pitching in the room.

**George Haikal:** That's pretty much just the CEO and the CTO, Daniel, doing.

**George Haikal:** So everything around it, like a little model, presentation, all that stuff.

**George Haikal:** Deck, memo.

**Vivian Liu:** So that's nice.

**Vivian Liu:** Very cool.

**George Haikal:** Good exposure.

**George Haikal:** It's a cool experience.

**George Haikal:** Yeah, it's very cool.

**George Haikal:** Other than that, usual craziness.

**George Haikal:** It's just, it's all good things, but super busy.

**George Haikal:** Everything you're doing is new.

**George Haikal:** You know the drill.

**George Haikal:** So you're not great at everything when you first do it, but once you get a hang of it, learning a lot.

**George Haikal:** so now I have people who can help with some of the things that I've done.

**George Haikal:** So it's like a whole different problem is figuring out like how to actually essentially build a team.

**George Haikal:** Like that's so foreign to me.

**George Haikal:** So I get like where you're...

**George Haikal:** I know sometimes we would talk about drafted or whatever.

**George Haikal:** I completely get what you're saying now.

**George Haikal:** And I can't imagine how much more high stakes it is than it's like a co-founder.

**George Haikal:** It's crazy.

**George Haikal:** People are just difficult to navigate.

**Vivian Liu:** Yeah.

**Vivian Liu:** What are you building a team for?

**George Haikal:** Right now, it's all the stuff that I've just jumped in and helped with.

**George Haikal:** So, for example, when I first joined, we didn't have a super formal process right after we closed the deal.

**George Haikal:** It was like my first couple of weeks that when I joined, we came up with this like strategy sprint, eight-week onboarding of a client after we closed the deal.

**George Haikal:** Essentially, like a deep dive on every piece of their business, their audience, who they're actually serving, what their goals are for like our engagement.

**George Haikal:** So setting the expectations right.

**George Haikal:** And then driving the first eight weeks of that client to make sure after the eight weeks, we can hand it off and like everyone's in the right place.

**George Haikal:** We have everything we need and the machine's moving and working.

**George Haikal:** And so that was like a zero to one thing.

**George Haikal:** Now we do that for every new client.

**George Haikal:** And so it's putting the team in place to help with everything from the kickoff call to all the follow-ups to doing all the deep dives with the experts at these companies to then creating all of the content, materials, artifacts, writing guidelines, all the stuff that we build for each client.

**George Haikal:** So now there's a team and machine that's running it and just closing the little gaps of like, I'm on every kickoff call.

**George Haikal:** So now training someone to help fill that.

**George Haikal:** And then that's one example of one process or system that we've done here.

**George Haikal:** There's like five others off the top of my head now that I have like at least a part to plan it that could be helped with someone joining.

**Vivian Liu:** Okay.

**Vivian Liu:** Well, it's so exciting for you.

**George Haikal:** Yeah, it's good.

**George Haikal:** Yeah, it's crazy though.

**George Haikal:** How about you?

**George Haikal:** How's May?

**George Haikal:** How's Japnet?

**George Haikal:** How's...

**Vivian Liu:** Um, I mean, it's going well.

**Vivian Liu:** Um, it's just on a follow-up demo with Lithia.

**Vivian Liu:** Um, they have like over 300 dealerships.

**George Haikal:** How'd that go?

**Vivian Liu:** Good.

**Vivian Liu:** Um, they want me to do, they have a couple different regions.

**Vivian Liu:** So they're doing a big like meeting in November and they wanted to bring in like more tools to help with sales productivity.

**Vivian Liu:** So they want me to present in front of their 50 dealerships from Southeast.

**Vivian Liu:** And then she's going to bring me, she's going to get me to do a demo with the person who runs like Texas area.

**Vivian Liu:** And so, um, so basically I'd be going to Florida in November to do a presentation.

**Vivian Liu:** And then the following week, if I can get a demo with the person who runs Texas, that's 70 dealerships.

**Vivian Liu:** So it's good timing.

**Vivian Liu:** They do big buys like this like all the time.

**Vivian Liu:** So it's like ideal first candidate for like getting into the U.S.

**Vivian Liu:** It's good timing because we have wearables at the dealerships now.

**Vivian Liu:** So remember like our demo video where it was like listening?

**Vivian Liu:** We're already doing that now.

**Vivian Liu:** We've been testing that for like the last month, basically.

**George Haikal:** Sick.

**Vivian Liu:** We went from like little pucks on the desk to now actually wearables.

**Vivian Liu:** So we have like five of them floating around right now.

**George Haikal:** How's that working?

**Vivian Liu:** Well, it's wild.

**Vivian Liu:** I'm grateful that there's salespeople that are open to it.

**Vivian Liu:** There's definitely a few that are like, maybe I want to get in trouble at work.

**Vivian Liu:** I'm like, trust me, I don't care about your personal conversations. I don't want to store that. It's going to cost me money.

**Vivian Liu:** It's like what I was saying to them.

**George Haikal:** They're like, oh, okay.

**Vivian Liu:** But it's like we're testing if we can get through the wearables, like if everybody's comfortable with it.

**Vivian Liu:** And then the next thing is to take all the conversations.

**Vivian Liu:** conversations.

**Vivian Liu:** And then build, like, the dynamic interface that would support that conversation.

**Vivian Liu:** And this is the, like, unknown part that I'm dealing with right now.

**Vivian Liu:** Yeah.

**Vivian Liu:** So it's all fun, but, like...

**George Haikal:** The unknown is if, is, like, how it would support, or what's the unknown part?

**Vivian Liu:** Yeah, so we set up, like, a vector database for us to be able to test, like, having multiple agents be able to source information.

**Vivian Liu:** Um, so I have, like, this whole process of, like, putting a transcript in with a customer profile, the prompts that I've built, um, to...

**George Haikal:** Cleaning up the transcript.

**Vivian Liu:** Yeah, the, you know, the transcript's actually, like, clean, uh, shockingly.

**Vivian Liu:** Um, a couple of nuances here and there, but it's not, like, the most important thing right now.

**Vivian Liu:** The important thing is, like, based on this conversation, what are the three vehicles that are best to be shown to the customer, based on what's inventory is available?

**Vivian Liu:** And because every time I submit it, like, I have to learn how to do, like, post-training and eval.

**Vivian Liu:** And I have no way to do that.

**Vivian Liu:** And to, like, the team's been building, like, an environment for me to be able to do it and start to do that, like, autonomously.

**Vivian Liu:** So, yeah, I was kind of curious.

**George Haikal:** nuts.

**Vivian Liu:** It's crazy.

**Vivian Liu:** Like, I just discovered, like, the words of what I'm trying to do, like, yesterday.

**George Haikal:** That's a good way to put it.

**Vivian Liu:** That's a really good way to put it.

**Vivian Liu:** Yeah, like, I've been trying to do this thing.

**Vivian Liu:** And I'm like, well, like, if I have a result, how do I talk to the LLM to say, like, to ask why they got to this answer?

**Vivian Liu:** Like, I can't just get it, but I need to be able to have this conversation.

**Vivian Liu:** And I was listening to my favorite podcast is Lenny's podcast.

**Vivian Liu:** And literally every day, the podcast that comes on, it's like, it is like perfect timing.

**Vivian Liu:** Like, this is where I learned, like, the words, like, this is, this is eval, like, post-training.

**Vivian Liu:** Like, it's so important.

**Vivian Liu:** I'm like, oh, my gosh, it's literally what I'm trying to do.

**Vivian Liu:** How the  do I do this?

**Vivian Liu:** So, yeah.

**Vivian Liu:** And I remember you showed me something.

**Vivian Liu:** At the office and it was like creating the content pages for one of the companies in the portfolio that takes like their, their business and then compares it with a competitor and it builds like pages comparing their, their, like their advantages.

**Vivian Liu:** And it's kind of what I'm doing ish.

**Vivian Liu:** Like I'm basically what I did jobs again.

**Vivian Liu:** I went through a cycle with car buyers this time.

**Vivian Liu:** And what I was, yeah, it was like what I wanted to do kind of from the get go, but I knew I had to wait.

**Vivian Liu:** And I was trying to understand like what they were trying to, like, once they leave the dealership, they all go home, do more research.

**Vivian Liu:** And what were they hiring the information online or there are other sources for, like, what were they trying to overcome?

**Vivian Liu:** And if they have these hurdles in their brain that they need to get past in order to make a decision, can I not then condense all of that research and present it to them?

**Vivian Liu:** No.

**Vivian Liu:** I that they're going to do that anyway, so that they can make a decision.

**George Haikal:** Like, based on the transcript, the conversation this person had, like, what are the gaps they still have that they're going to go home and try to fill?

**George Haikal:** Yes and no.

**Vivian Liu:** Based on this person, what they said, like, I know that, like, safety is important because they have two kids, right?

**Vivian Liu:** And when they go home, what are they researching about this vehicle, even though they have all the information, supposedly?

**Vivian Liu:** Well, they're going on to, like, Reddit forums to find out how much people actually paid for this vehicle recently.

**Vivian Liu:** They're looking, when they talk about fuel economy, was like, well, like, what about fuel economy?

**Vivian Liu:** They're actually comparing fuel economy with their friends and their co-workers.

**Vivian Liu:** So, like, I'm trying to find those nuggets of what I can present to them, kind of like a recap or summary sheet of, like, here's what you have, like, you came for your visit, and I can summarize why this vehicle is better than the other ones.

**Vivian Liu:** And then, in theory, give them some sort of, you know, tool to work with that allows them to give us more information about what they really want.

**George Haikal:** That's super cool.

**Vivian Liu:** Yeah.

**George Haikal:** Very hard, though.

**George Haikal:** I know how difficult that actually is.

**Vivian Liu:** Yeah.

**Vivian Liu:** And I don't want to build all this and then find out I'm on the wrong path either.

**Vivian Liu:** So there's like two things.

**George Haikal:** in that round of interviews, like, was everyone saying the same?

**George Haikal:** Like, what was the biggest thing?

**George Haikal:** Was what you just told me?

**George Haikal:** The biggest thing that came out of it?

**Vivian Liu:** The understanding?

**Vivian Liu:** Yeah.

**Vivian Liu:** It was a combination of, like, then, like, okay, with this information, they would, literally, people would write notes on their phones, or they would, the dealerships are not, like, always consistently printing things for them to, like, take home.

**Vivian Liu:** And that's some of the feedback is, like, no one gave me anything.

**Vivian Liu:** And part of that problem is because dealerships don't want to give you something because they want, they think you're just going to, like, go shop it with somebody else.

**Vivian Liu:** But they're going to shop you anyway.

**Vivian Liu:** So they have a lot of questions more on people's, like, about the value of the vehicle after they use it.

**Vivian Liu:** And pricing, like negotiating was another, was a big piece.

**Vivian Liu:** So I'm trying to build value so that salespeople want to use it, but also consumers will want to participate and be like, listened to.

**Vivian Liu:** And then I've also been keeping a track of all the questions that people have in their conversations with the salesperson, because then that becomes the opportunity for what real time looks like.

**Vivian Liu:** If everybody has questions about trims, then I need to build something that can explain and visualize trims.

**Vivian Liu:** But that's a whole other problem, too.

**George Haikal:** Like, how do I get to the dynamic interface?

**George Haikal:** God damn.

**George Haikal:** It's good, though.

**George Haikal:** It's super interesting.

**George Haikal:** Yeah, yeah, yeah.

**George Haikal:** It's really, really cool.

**Vivian Liu:** Yeah, I'm not complaining.

**George Haikal:** How's all that going?

**Vivian Liu:** Sorry?

**George Haikal:** How's JapNet?

**Vivian Liu:** How's all that going?

**Vivian Liu:** It's a lot better.

**George Haikal:** That's good.

**Vivian Liu:** I sent her a podcast.

**Vivian Liu:** Um, from an autumn, I've been listening to like automotive podcasts too.

**Vivian Liu:** And there was a competitive company who essentially built their own, like, um, in like an ecosystem for sales people for sales managers to train their AI chatbots.

**Vivian Liu:** So as soon as she heard that, that's where she learned the terminology and she's like, Oh .

**Vivian Liu:** Like I've been, I gotta get the, yeah, I gotta do this.

**Vivian Liu:** Yeah.

**Vivian Liu:** So then she did a ton of research herself, which was great.

**Vivian Liu:** And then she got the whole team on it.

**Vivian Liu:** We have like an AI learning club on Fridays where everybody like brings in what research that they learned that we can like try.

**Vivian Liu:** So we're getting into that.

**Vivian Liu:** Um, but I think right now I'm the bottleneck because I'm the only person who can do the eval and I don't know how to do that properly.

**Vivian Liu:** And I find that it takes me so much.

**Vivian Liu:** Like there's so much mental energy required to sit down and be able to like assess the information on the, maybe with the new, like, um, the team.

**Vivian Liu:** Built me this Google Sheet that kind of pre-fills all the information that I'd be trying to compare side by side.

**Vivian Liu:** But it's still like, I think, like, I'm definitely the problem right now.

**George Haikal:** Really?

**George Haikal:** It's just getting through.

**George Haikal:** You're basically, I mean, what's the goal?

**George Haikal:** You're trying to, like, yeah, I guess, what's the goal?

**Vivian Liu:** I want the results from the prompts that we've built to be accurate enough that I can be confident we can build a product and let the results show to the, like, we can show the results to the customer.

**George Haikal:** And what are the prompts that you've built?

**Vivian Liu:** Like, what's...

**Vivian Liu:** Well, we have, like, it's mainly the recommendation prompt to identify the good, better, best.

**Vivian Liu:** So my prompt is because, so because there's so many different scenarios, I'm actually not asking it to give me the top three vehicles.

**Vivian Liu:** I'm asking it to give me the top three vehicles for each scenario.

**Vivian Liu:** So, like, different scenarios are, like, if it's, like, good, better, best of the same vehicle, different trims, different packages, like, different prices, basically.

**Vivian Liu:** Another one could be, like, stepping up into a luxury, so having two Nissans and an Infiniti, or is it having three different sizes of Nissans if they wanted to upgrade into a larger SUV?

**Vivian Liu:** Or is it that they can't afford it, so you actually have to remove some features in one of the good, better, best options to then help them make that trade-off?

**Vivian Liu:** Or is it showing them what the vehicle that they came in on and how much it would cost if they got everything that they wanted?

**Vivian Liu:** So there's just, like, there's multiple different scenarios, and I'm trying to take each combo from each scenario and then present it to the dealership and be like, here's what I think is the answer, which one do you think is the answer?

**Vivian Liu:** And then use that to then, like, that's the feedback loop that I think needs to happen.

**Vivian Liu:** And then I need to learn how the AI, the steps and the reasoning to be able to understand why they keep going.

**Vivian Liu:** It's definitely hallucinating too much still, and I need to understand how to combat that, and I've never had to do that before.

**George Haikal:** Yeah, you can put some, like, checks and balances in place or just, like, continue to ask it to, like, evaluate itself or, like, alongside an answer, like, have the model itself give, like, a confidence score based on whatever the criteria you want to set is.

**George Haikal:** Like, how confident are you in your own answer that it's correct?

**George Haikal:** Like, make it a percentage and you can mark it on a bunch of different levels of criteria.

**George Haikal:** Like, that's what we have right now for one of our researchers.

**George Haikal:** It's a genetic switch just loops until it meets the criteria that we set.

**George Haikal:** And the criteria that we set, it ranges, but it's a...

**George Haikal:** Actually, I'm trying to think of like a crystal clear example.

**George Haikal:** It's an example is I have this piece of content that I have to write and I want to make sure it's always under a thousand words.

**George Haikal:** And so this is all in like a prompt, right?

**George Haikal:** Like I want it to be under a thousand words.

**George Haikal:** I want it to sound in this tone, you know, be educational and confident, nonjudgmental, whatever, like whatever the writing guidelines are as well.

**George Haikal:** The model is obviously hallucinating and it's not going to get it perfectly right each time.

**George Haikal:** And so it will just continue to loop content.

**George Haikal:** Here's the writing guidelines.

**George Haikal:** Here's the output.

**George Haikal:** Does this output meet the criteria of these writing guidelines?

**George Haikal:** No, this is 1200 words, not a thousand.

**George Haikal:** Rerun and rerun and rerun until it continues to hit that.

**George Haikal:** And that's just one criteria can be on however many that you set.

**George Haikal:** And so we have it on like four or five.

**George Haikal:** Different ones.

**George Haikal:** One is research.

**George Haikal:** like make sure the research that you're doing, the sources are highly vetted, that it's accurate and factual, and that it's relevant to the content and the business.

**George Haikal:** And so it'll go in and continue to loop and check on all those things, and it'll give it a confidence score on how grounded this article is.

**George Haikal:** So it's like adherence to the writing guidelines, how grounded the article is, and then a few more criteria that we set.

**George Haikal:** And so it just continues to go until it hits it.

**Vivian Liu:** So I'm assuming the work of like eval has already been done.

**Vivian Liu:** So like who, what, I guess like it was, maybe it was like Danny who was then looking at the results of the confidence score to then determine whether it was accurate or not.

**George Haikal:** Like who does that?

**George Haikal:** Who, like where is the feedback loop?

**George Haikal:** We have a human in the loop.

**George Haikal:** So like all the content has an editor or a content manager who like does a lot of the plugging in on the system, an editor, a managing editor who actually looks at the output of the content, and then a director who manages the whole process.

**George Haikal:** But it's either the content manager at the level when the run stopped, it's like, okay, is this output right?

**George Haikal:** Like, did this actually check?

**George Haikal:** And because we're running it in a loop, it will also tell you, hey, I'm not confident in this.

**George Haikal:** So it helps the human come and understand where they need to focus their attention.

**George Haikal:** Like, this research, I don't think was done well.

**George Haikal:** There wasn't enough for me to grab.

**George Haikal:** I don't like the sources that were available.

**George Haikal:** I need someone to come in and look at it.

**George Haikal:** It's essentially what it helps with.

**Vivian Liu:** So in this scenario where they realized there was something wrong and the output was not what they wanted, like, what happens after that?

**Vivian Liu:** Like, how do they then iterate in the system?

**George Haikal:** Yeah, then it's just another step.

**George Haikal:** So this is all, that is like one action that happens is that loop that I told you about, and then there's the output of it.

**George Haikal:** And then if they don't like the output of it, they just add in post-processing instructions, like what they want to change, right?

**George Haikal:** So, and then that's

**George Haikal:** Another prompt with this output, and then it goes through whatever the post-process instructions are, and then you evaluate it again to see if it meets it.

**George Haikal:** And that on its own, there'd still be a lot of hallucination, and you wouldn't be able to one-shot all the time, but because each step, we have the context of the entire business, the audience, the writing lines, the style and tone, all these artifacts that we pull on every time.

**George Haikal:** So it's as knowledgeable as possible on every part.

**George Haikal:** That's what helps it, like, make sense more as steps, and that's why it's like, you only need one or two revisions or instructions for it to go back and fix itself, because it still takes every other piece of context that we've done to date into account.

**Vivian Liu:** So the people that are doing this, they're, like, if it's, like, they're talking to what is, like, ChaiJPT through the GrowthX platform?

**George Haikal:** Yeah, I can show you.

**George Haikal:** Yeah, it's a model.

**George Haikal:** doesn't have to be ChaiJPT.

**George Haikal:** We have a bunch.

**Vivian Liu:** How does it work for, like, the bunch?

**Vivian Liu:** Like, do they just automatically run through all of them and then, like, another agent, like, assesses all the results?

**George Haikal:** Like, how does that work?

**George Haikal:** If it's a bunch, you mean?

**Vivian Liu:** Yeah.

**George Haikal:** Like, if it's multiple different, like, assignments that we're trying to do?

**Vivian Liu:** Well, you said, I said, Chachi Vutin, you said, well, there's a bunch, right?

**George Haikal:** There's, like, several.

**George Haikal:** Oh, yeah.

**George Haikal:** Yeah, reasons for itself on which one you want to use.

**George Haikal:** can also self-select which model you want to use based on whatever you're trying to do.

**George Haikal:** There's, like, a drop-down that you can select and the UI that we built.

**George Haikal:** Not, not, built that, Daniel, but watch.

**Vivian Liu:** I'll show you a little.

**Vivian Liu:** Okay.

**George Haikal:** Trying to find a good example of a workspace that's really good.

**George Haikal:** Engine.

**George Haikal:** Share my screen.

**George Haikal:** Hmm, hmm, hmm.

**George Haikal:** Hmm, hmm.

**George Haikal:** So these are the artifacts I'm talking about, all the pieces of context that constantly get called on, that this is what we do in the strategy sprint, is like we understand super deeply every audience and person you're speaking to, down to persona, but like who this person actually is, the biggest fears, uncertainties, motivations, all that stuff.

**George Haikal:** Let's do that for every different vertical and part of the industry that you're in, and want to be in. Then there's company context about your company—as much research as possible on your company—and then blah, blah, blah.

**George Haikal:** It's like this for everything, right?

**George Haikal:** And then pipelines.

**George Haikal:** These are all the things we do on behalf of this client, right?

**George Haikal:** And so we'll do, I'm going to show you this one, let's see if we've got anything done.

**George Haikal:** I just want to show you.

**George Haikal:** So, when you have a topic.

**George Haikal:** That you want to write about, right?

**George Haikal:** The keywords, whatever.

**George Haikal:** You put the topic in.

**George Haikal:** The domain to search for fact checking, which is the client summit.

**George Haikal:** And this is all the things that it does in continuous steps.

**George Haikal:** It creates an assignment brief.

**George Haikal:** I can inspect and show you too.

**George Haikal:** Let me re-login to flow.

**George Haikal:** Why is this?

**George Haikal:** Dude, I have so many  tabs.

**Vivian Liu:** Where are we at here?

**Vivian Liu:** I am the same.

**George Haikal:** I want to know why.

**George Haikal:** I'm getting this error, but I'm in flow studio here.

**George Haikal:** The ?

**George Haikal:** Whatever, mean, you can swag it.

**George Haikal:** So...

**George Haikal:** And then it comes up with a brief, pulling the context, this is the prompt, right?

**George Haikal:** And the context that we pulled in, let me minimize this  so I can scroll down, I I can't.

**George Haikal:** And then it does a bunch of research, pulls the executive summary and then the output of that.

**George Haikal:** It creates this overview, this assignment brief.

**George Haikal:** So before you write an article, you need to brief who the target audience is.

**George Haikal:** It does a keyword analysis, blah, blah, blah, blah, then it actually goes and does the research.

**George Haikal:** And it shows you the research that it did.

**George Haikal:** Then it comes up with the right research questions to ask based on the topic.

**Vivian Liu:** The only thing you're manually doing is the topic.

**Vivian Liu:** And then it does all of these steps, all the way down.

**Vivian Liu:** So then someone would review each one of the steps?

**George Haikal:** Basically, the review, yes, you can go in and review each one of the steps.

**George Haikal:** That's why they're here.

**George Haikal:** And there's like an AI editor here.

**Vivian Liu:** Okay.

**George Haikal:** It's Okay.

**George Haikal:** And Thank

**George Haikal:** Where you can go in and make edits and revisions and whatever you need.

**George Haikal:** And like these are the artifacts, you can call them or whatever.

**George Haikal:** You can strengthen the call to action, can realign with the writing guidelines that are based on the client.

**George Haikal:** But usually someone just looks at the output and sees if it's right.

**George Haikal:** And if not, they can go and dig in to each step.

**Vivian Liu:** So let's say that there's something wrong with the article draft.

**Vivian Liu:** Where are they going to update in the system?

**Vivian Liu:** Like they caught something and it's like every single time they should, like the prompt needs to change for that article draft section or that step.

**George Haikal:** With this?

**George Haikal:** The assignment brief?

**George Haikal:** Or like what do you mean the article draft, this output?

**Vivian Liu:** No, no, no.

**George Haikal:** So you see how there's like assignment brief, research outline, article draft.

**Vivian Liu:** Oh, here.

**Vivian Liu:** So let's say you got something wrong in one of the steps.

**Vivian Liu:** So they would like, how are they iterating?

**Vivian Liu:** Oh, guess if you scroll up, there's an input.

**Vivian Liu:** So then they would go.

**Vivian Liu:** I want to adjust the input, right?

**George Haikal:** Yeah, and so each step, so if you look, yeah, the short answer is yes, but if you look at it in like the pipeline view, here you can see all the steps.

**George Haikal:** So the draft here, so each one of these happens before the next one happens.

**George Haikal:** So you can either go back and see, it depends on what was wrong in the step, right?

**George Haikal:** Like if this sounds super off tone or like, yeah, very casual and it's not in line with the tone that we want, then you can go and look at your writing guideline artifacts where you have all the tone information and adjust it there.

**George Haikal:** Or you can just go like, I need to realign this to the Brandon voice, right?

**George Haikal:** So realign this sentence.

**George Haikal:** But usually if these are wrong, that's either because one had hallucinated or because like one of the foundational artifacts or one of these steps are super off.

**George Haikal:** But that's why each one of these isn't happening in a moment.

**George Haikal:** Or is happening individually as like small steps that then compound on each other.

**George Haikal:** Because if you tried in one shot to be like, hey, I need you to create an article based on this title, right, and this meta description.

**George Haikal:** And I needed to have all these things and I want you to go to research on the topics and I want you to take this outline to kind of all that was in one prompt.

**George Haikal:** Like it would never, ever, ever work.

**George Haikal:** It would take so much manual effort.

**Vivian Liu:** That's why it's all broken down into steps.

**Vivian Liu:** Okay.

**Vivian Liu:** I think like what I'm trying to figure out is like, this has obviously been perfected.

**Vivian Liu:** So like the step prior to when you're like figuring, like you can trust that each one is going to do its job.

**Vivian Liu:** Like I can, I definitely need to split things up.

**Vivian Liu:** And I definitely need to have the LM explained to me like the reasoning of how they're like for each one of these like steps for me to figure out like where it's going wrong.

**Vivian Liu:** But like.

**George Haikal:** But like.

**Vivian Liu:** Then I, for me, like, what I would do then is, like, okay, well, if I now figure out, like, this one thing that's wrong, I would have to update the prompt, and then I would just keep doing the tests with new transcripts that come in.

**Vivian Liu:** And it just feels very, like, it feels very messy for some reason.

**George Haikal:** Yeah, I get what you're saying.

**George Haikal:** Let me just pull this raw workflow and show you quick.

**George Haikal:** Like, article gen, because for some reason, like, that's the thing when you are doing it yourselves, like, it's so buggy.

**Vivian Liu:** Platform, article gen.

**George Haikal:** Jesus  Christ.

**George Haikal:** I actually do engine on the same example.

**George Haikal:** So, this is an example of, like, how one step is improved.

**George Haikal:** So,

**George Haikal:** This certain client needed a better outline.

**George Haikal:** And so you can see everything that it's doing, right?

**George Haikal:** It's validating the input.

**George Haikal:** It's creating a dossier category.

**George Haikal:** It's enhancing the article outline that already exists to make it better.

**George Haikal:** And it's returning.

**George Haikal:** so, like, let's see if you can use the rungs.

**George Haikal:** You can see that's what I want to show you.

**George Haikal:** Like, each step has, like, a super detailed prompt still.

**Vivian Liu:** Okay, yeah.

**Vivian Liu:** And then, is it someone's responsibility to update this prompt?

**Vivian Liu:** Like, how are they, like, how are they, because, like, you're getting, let's say for me, I have, like, a thousand conversations that come through each store a day, right?

**Vivian Liu:** I can't possibly, like, I know I need to build some sort of agent to do this autonomously, but while I can't do that just yet, because I don't know how to do that, but how do I then, like, what is the environment and the procedure for me to go through each thing?

**Vivian Liu:** And, like, it's that prompt.

**Vivian Liu:** So this is going back and forth that I haven't figured out.

**George Haikal:** Yeah, I don't know where your team is like, and I'll just show you like the simplest version of this.

**George Haikal:** Like, I don't know where your team is doing it now, but what I do myself, like when I, because I'm still new, I just go to Claude.

**George Haikal:** And like, this is never going to be as good as our own platform, but I have a Claude project that has everything that I need.

**George Haikal:** So like, if you think of a step, whatever step that you're doing right now, this example is, I have a kickoff meeting with every new client we have.

**George Haikal:** I have the same follow-up that I need to do.

**George Haikal:** So then I automate it.

**George Haikal:** How did I automate it?

**George Haikal:** I just created this project that has the context.

**George Haikal:** So it has examples of what good looks like from other clients we have.

**George Haikal:** These are documents, full notes, follow-ups from other clients that we had.

**George Haikal:** Then I pull in the company I just interviewed, but with a bunch of research, a description of the company.

**George Haikal:** The notes from the call that I had that I took live.

**George Haikal:** And then the notes from the transcript that I had, or, and then the raw transcript that I had.

**George Haikal:** And then in the instructions, I give it more info on the company.

**George Haikal:** And then all I, all I literally do for this step, and you'll obviously adjust it to what you need, is I just reuse the same prompt of what I wanted to do.

**George Haikal:** Just create this document for the company, use these things, which are already context in the project.

**George Haikal:** Then some, like, and this is a super simple prompt, but with the good context already, don't need the most in-depth prompt to start.

**George Haikal:** Refer to these examples of what good looks like.

**George Haikal:** So you give it examples of what good looks like, you give it direction on what to use, and then you can just iterate from there.

**George Haikal:** So, like, basically, these are all ones that I do, and it essentially almost one-shots them all.

**George Haikal:** I did the same thing, in a second, you created this super, like, really good document.

**George Haikal:** Super specific, it's pulling in quotes, like I asked it to, directly of the right people, and at the right point.

**George Haikal:** So that's, like, way to...

**George Haikal:** Have all the context, whatever you're doing needs, and then just adjust the prompt accordingly.

**George Haikal:** And you can test yourself in a cloud project to make it easier.

**George Haikal:** Because I don't know, like, what environment your team is using.

**George Haikal:** It sounds like they're just giving you, like, this easy interface to use when you said, like, Google Doc or something.

**George Haikal:** So that's how I test, like, if a prompt is working.

**George Haikal:** And then you can adjust.

**George Haikal:** You can add more context, see if the output works better, add less.

**George Haikal:** You can add different questions of it, see how it responds.

**Vivian Liu:** So I don't know if that is helpful, but it's, like, a way for you to test.

**Vivian Liu:** This is basically what I'm doing, except I asked them to see if they could build me something in the future that I can, like, we're using N8N to, for me to, like, upload documents, the inventory, things like that.

**Vivian Liu:** But ideally, I would like to keep all of my, I wanted to do all this research in N8N instead of taking everything out of, and putting it into, like, GBT.

**Vivian Liu:** So...

**Vivian Liu:** So...

**Vivian Liu:** So...

**Vivian Liu:** Um, I did just learn something is like, I need to break down the steps even more of like the logic of coming up with what the outcome is.

**Vivian Liu:** Um, and cause it's doing that on its own.

**Vivian Liu:** And anyways, what are the different, um, like AI sources?

**Vivian Liu:** Like what are all the elements that you use and for what?

**George Haikal:** Cause yeah.

**George Haikal:** So you just, yeah.

**Vivian Liu:** Like I, I've tried Claude, but I didn't, I found it like unnecessary.

**Vivian Liu:** Like I didn't see that big of a difference that like made me gravitate towards one or the other.

**Vivian Liu:** Meanwhile, like, like keep in mind that I'm not, I'm not like working on copy or anything like that.

**Vivian Liu:** Like I know that Claude's supposed to be better for that.

**Vivian Liu:** Um, but I'm curious, like, I'm also like, there's so much going on and I just want to figure out how to do this one thing before I go expand to do others.

**Vivian Liu:** So I'm not testing anything else, but I'm curious what you found is the difference.

**George Haikal:** Yeah, it's hard because they change so quickly, and they're good for different things and use cases, but Claude, historically did all of any project work that I need to upload a bunch of documents, and I want it to really understand the documents and create good output from it.

**George Haikal:** I used Claude, but it's pretty much the same now as ChatGPT 5 for what I needed to do, which is like writing stuff, thinking through stuff, perplexity I use for research.

**George Haikal:** I use perplexity in ChatGPT, like I'll probably run the same prompt on each one and see what it gives me as research.

**George Haikal:** And yeah, tables and stuff, I use ChatGPT more, create tables, explain things to me in tables, help me break down my thoughts and everything here into like, a then I put that, the way it broke down into like a structured format presentation into like a different tool, like Gamma to make a presentation.

**George Haikal:** So ChatGPT, when I'm, want to break things down.

**George Haikal:** Steps.

**George Haikal:** Those are the main three.

**George Haikal:** mean, there's a bunch of other different ones, too, but those are the main three that are, like, probably the best for what you're going to need to do.

**Vivian Liu:** Okay.

**Vivian Liu:** That's cool.

**George Haikal:** Prophecy for research, too.

**George Haikal:** I use, like, all the time.

**Vivian Liu:** Yeah, I haven't asked to do any research yet because I wanted to take online sources to do research later, but there's, like, a whole host of problems because, like, how do you know, like, who's reliable and who's not, and people are just, like, upset online because they had their own mechanical issues.

**Vivian Liu:** So I don't want to, like, combine everything.

**George Haikal:** want to do, like, one variable at a time.

**George Haikal:** Yeah, no, that's a lot.

**George Haikal:** Yeah, I'm at more for, like, personal stuff, and you can always check the sources, too, you know, but that's a way, way future problem.

**George Haikal:** That's how I kind of use them.

**Vivian Liu:** And I guess I'm curious on the back end of things, like, like, I'm assuming that...

**Vivian Liu:** Um...

**Vivian Liu:** ...

**Vivian Liu:** ...

**Vivian Liu:** There's like some sort of confidence score that's being set.

**Vivian Liu:** Like is someone kind of is like someone just like tracking those to some degree or does that?

**George Haikal:** yeah.

**George Haikal:** I mean, that's like all day, every day.

**George Haikal:** The confidence score, it's like the person's reviewable check, but our engineering team is like constantly updating.

**George Haikal:** Like if we see something that's off, like we just tell them and they'll go and fix it.

**Vivian Liu:** But I'll show you a quick example.

**Vivian Liu:** What is the dashboard for that person supposed to look like?

**Vivian Liu:** This is a great distraction from me losing my reign.

**George Haikal:** I'm glad.

**George Haikal:** This is the research supervisor workflow.

**George Haikal:** I want to find the one that I ran.

**George Haikal:** It's basically just a better researcher.

**George Haikal:** That's funny.

**George Haikal:** didn't do it.

**George Haikal:** This was me.

**George Haikal:** It didn't do it that good job.

**George Haikal:** Oh, helping me plan my surf trip, but, um, what the , bro, I literally just had it, like one more, executions, I think it was like, uh, maybe the first one?

**George Haikal:** Okay, it was one more after the first one, I got it, this is, it'll be worth it, don't worry.

**George Haikal:** What the , hold on, I think was the third one.

**George Haikal:** I think everything's a V1, so it's like, whatever doesn't need to be perfect isn't.

**George Haikal:** Same put.

**George Haikal:** Whatever, this is fine.

**George Haikal:** And so...

**George Haikal:** So this can kind of show you what, like if something isn't working here, and like one of these steps fail, this is where I would go in and check the actual prompts or what happened or what didn't work and how each step is running.

**George Haikal:** But like from a high level, this shows you all the steps, all you're inputting is like the question you have.

**George Haikal:** To create a comprehensive brief for this company, blah, blah, blah, blah, blah, blah, and then the researcher generates a research plan, comes up with good questions, how deep it wants to research, what success looks like, so it'll loop until it hits this, right?

**George Haikal:** The source requirements, only using highly embedded sources, it's using properly deep research here, and it does this for all the different types of questions that it thinks are most relevant to ask based on the question.

**George Haikal:** Then it actually goes in and executes, and it synthesizes the results, and then it evaluates, like you said.

**George Haikal:** Here you can see confidence score and priority, and it'll explain this confidence score.

**George Haikal:** It's missing these leadership roles, no information found, research limitations, achieved approximately 25% of target goal because it didn't identify five to eight.

**George Haikal:** And so it'll continue to go in and assess itself on the criteria that you set, and then if anything goes wrong, then I go in here and figure out why.

**George Haikal:** So if one of these steps fails, by the way, this is when you're asked a question, it understands the question generates the persona, and then all of those eight or so other questions that it's asking based on your first one, these are all the individual research, deep research steps that are happening in parallel to go answer all those questions.

**George Haikal:** And then when it's like creating that executive summary and understanding, that's this, and this is the supervisor, so if any of these fail.

**George Haikal:** It'll loop until it hits it.

**George Haikal:** So this is like, you know, where it'll bounce back and continue to loop.

**George Haikal:** And then in each one of these, you can see what the input was.

**George Haikal:** It's funny, they're called workers.

**George Haikal:** And then what the result was for each one.

**Vivian Liu:** Okay.

**Vivian Liu:** Can you go back to, what is the, the top right hand, like buttons, like what is run workflow and the other workflow?

**George Haikal:** That's if I want to run a new one, I can choose this what you're asked, like which research tool we use.

**George Haikal:** These are the three different ones.

**George Haikal:** And then you can choose what model.

**George Haikal:** I mean, it's the same thing.

**George Haikal:** I think you can just do either or, and then you can ask the question and you can run it.

**George Haikal:** So I can show you, mean, let's see.

**George Haikal:** So let's

**George Haikal:** What's the question?

**George Haikal:** What's that good question that you have?

**Vivian Liu:** Um, that I have?

**George Haikal:** Doesn't...

**George Haikal:** I used to be in Vancouver.

**Vivian Liu:** That's it.

**George Haikal:** And you can see...

**George Haikal:** It's generating the research plan.

**George Haikal:** This is what you asked, right?

**George Haikal:** Like, what happens?

**George Haikal:** you just...

**George Haikal:** The input is the question.

**George Haikal:** And it's going to start running.

**George Haikal:** And you can see it all running.

**George Haikal:** You can see...

**George Haikal:** It's pretty insane, honestly.

**George Haikal:** And, like, I don't know  about this, honestly.

**George Haikal:** But it's now generating the plan.

**George Haikal:** The plan's done, right?

**George Haikal:** Here's the output of the plan.

**George Haikal:** It identifies the research objective.

**George Haikal:** It identifies the target audience.

**George Haikal:** And, like...

**George Haikal:** Queries that it should ask, and the success criteria.

**George Haikal:** So the answer to your question is, for us, it's coming up with what success looks like ourselves, and then going back and double-checking, right?

**George Haikal:** For you and the prompts that you're building, it's probably just going to be manually within those prompts to start, like what success looks like, or a separate prompt where you just run it after the first one happens, then it's like, make sure it hits these five things.

**Vivian Liu:** Yeah, I feel like I have steps on my end that's like, based on what the customer wants, are there vehicles that are a match to what they're looking for?

**Vivian Liu:** If there isn't, then they need to start problem-solving and like trying multiple different things.

**George Haikal:** But even that's like so vague, I feel.

**Vivian Liu:** It is, it is so vague.

**George Haikal:** Yeah, I think just break it down.

**George Haikal:** It's like every step that you would do to figure it out based on what that person told you in the conversation and like what you know, like whatever you're trying to get it to do, break it down into like all the steps and then you can understand how you did each step and then you can create a prompt for what you did and then you can test at each step instead of just trying.

**George Haikal:** I don't know if like you're trying to I don't know how you all are trying to do it now if I'm being honest like if it's one massive I don't even know like what you're prompting against you have the transcript and from the person and then what other information do you have and then you're running that that transcript running a prompt against that transcript and then trying to get something else out and then what are you doing with that thing you're getting out like that's the point I'm unclear on.

**Vivian Liu:** So we have the transcript there's there's two forms of the inputs from the conversation with the customer there's the actual guest sheet which is like a form that was filled out with by the salesperson.

**Vivian Liu:** The guest sheet that's currently out.

**Vivian Liu:** And then we have the transcripts.

**Vivian Liu:** So another thing that we could be putting in there is like, I have a separate prompt for assessing the transcript and then building essentially like a CRM entry for it.

**Vivian Liu:** Because there are certain things that you wouldn't capture through just a transcript itself.

**Vivian Liu:** There's like nuances that I've taught it to like, to look out for.

**Vivian Liu:** So between those two or three things, and then it's got access to the inventory.

**Vivian Liu:** And the, like all the features in the inventory.

**Vivian Liu:** And then the output is like, basically give me the top three vehicles for each scenario.

**Vivian Liu:** And then what I was doing was, I was going through each scenario to decide like, does it make sense or not?

**Vivian Liu:** So one of the problems was, if you, if I looked at your transcript from like a month ago, I, and I was looking at inventory that we have today.

**Vivian Liu:** It, that's not, it won't be accurate.

**Vivian Liu:** Because like, how do I know which.

**Vivian Liu:** this

**Vivian Liu:** Like if I validate the answers with what actually happened, so like the salesperson showed them this vehicle, was that vehicle in the results that we gave?

**Vivian Liu:** And if it's not, then why isn't it?

**Vivian Liu:** Or is there a good reason for it to not be there?

**Vivian Liu:** And if I, I was running into the problem where like I was comparing the, I was giving them the top three vehicles that we have today, not when the customer was in the store.

**Vivian Liu:** So then I'm, then I'm like, I'm, I'm purely guessing whether this is like a good combination to show or not.

**Vivian Liu:** So the team has built me something where I can run it based off of, I can run the workflow based off of the inventory that was available that day.

**Vivian Liu:** But like, there should be a process where I'm doing this like every day, essentially, and going through with the salesperson or the managers and say like, you had this customer come in yesterday, here are the vehicles that you have in inventory, which ones would you have shown?

**Vivian Liu:** Is this combination of the good, the good, better, best that we presented, like the right combination?

**George Haikal:** I get that, but how do you even know, like, what are you doing with the transcript to actually help the model understand what is good, better, or best for the person, besides their raw words?

**George Haikal:** Like, are you doing anything from the transcript to when you're asking things to call in the transcript and use it?

**George Haikal:** Like, are you helping synthesize what that person said into what, like, into characteristics or, like, a more organized and concrete set of, like, criteria or data or information on the person?

**Vivian Liu:** Yes and no.

**Vivian Liu:** Like, it's breaking down the information of, like, what their motivators are, like, what are the things that they have, like, things that they're, like, indifferent about.

**Vivian Liu:** And, like, that's basically, it's not, like, it's not at the point where I can assess to be, like, oh, this customer clearly preferred this thing over that one through just, like, the tone of voice or anything like that, like.

**George Haikal:** But you're at least.

**Vivian Liu:** Why don't I show you?

**George Haikal:** Pull it up.

**Vivian Liu:** Okay.

**Vivian Liu:** So.

**George Haikal:** Nanaimo.

**Vivian Liu:** Yeah, that's where I'm stuck right now.

**Vivian Liu:** Okay, so here's the transcript that goes into a summary.

**George Haikal:** Why is it Chinese?

**Vivian Liu:** Because the customer is Chinese.

**George Haikal:** That's cool.

**Vivian Liu:** Yeah.

**Vivian Liu:** It's kind of wild.

**Vivian Liu:** So, for example, we have a prompt that builds whenever it loads.

**Vivian Liu:** Maybe.

**Vivian Liu:** Okay.

**Vivian Liu:** Like this.

**Vivian Liu:** So, this is the new version of the gesheet.

**Vivian Liu:** So, here, anything that's written, like, bigger trunk spaces through the form itself, that, like, this is gesheet.

**Vivian Liu:** gesheet.

**Vivian Liu:** And the AI insight is through the prompt that we've given to assess the transcript.

**Vivian Liu:** you click into the prompt or no?

**Vivian Liu:** No, I can pull it up though.

**Vivian Liu:** I have like a full notion, like I'm tracking the different prompts and like the different versions that we have.

**Vivian Liu:** I'm comparing it to see like, am I correct or not?

**Vivian Liu:** Like one, for example, like the wife works for the attorney general's office.

**Vivian Liu:** They have a preference for this vehicle.

**Vivian Liu:** And even though they put this into the quiz, the next version, I want to, I don't want them to input anything.

**Vivian Liu:** I want to make sure that what they're saying gets captured correctly.

**Vivian Liu:** So then it's like, okay, they want a bigger vehicle than their current Nissan Qashqai.

**Vivian Liu:** They talked about these vehicles.

**Vivian Liu:** Like this is interesting where they said it's 600 to 700.

**Vivian Liu:** So it's 30 to bi-weekly.

**Vivian Liu:** This is monthly.

**Vivian Liu:** That's why.

**Vivian Liu:** So then it would take.

**Vivian Liu:** All of the AI insights along with the actual answers from the form.

**Vivian Liu:** And it would, I would take the transcript, put it into this RAG workflow.

**Vivian Liu:** It would pull from inventory.

**Vivian Liu:** It would then, in my prompt for the recommendation engine, and it would spit out this output.

**Vivian Liu:** So, let me see if can find, are you following me so far?

**George Haikal:** Sorry.

**George Haikal:** Yeah, yeah, yeah, no, I'll interrupt if I don't.

**George Haikal:** Will it make sense?

**George Haikal:** So the My bad, I never asked if you were following me or not.

**George Haikal:** Sorry?

**George Haikal:** My bad, never asked if you were following me or not.

**George Haikal:** Oh, no, no, no, I'm going to keep it.

**Vivian Liu:** So, I'm trying to, like, again, like, so you can see I don't have, like, steps broken down.

**Vivian Liu:** But I will take, if this is the output of, sorry.

**Vivian Liu:** right.

**Vivian Liu:** This is the summary of the customer, and this is the output from the prompt that I gave it.

**Vivian Liu:** So what I was trying to do is, like, here's the scenario.

**Vivian Liu:** I asked for, like, up to five different combinations of good, better, best, so that I can assess, like, how it's thinking about it to then determine why it's wrong.

**Vivian Liu:** So one of my tests, like, it was pulling a vehicle that doesn't even exist, or it was skipping a vehicle because it thought that the customer really wanted Nissan's when they, in fact, didn't care.

**Vivian Liu:** So, like, I'm trying to find out, like, where it could go wrong to then put that into the prompt.

**George Haikal:** That makes sense.

**Vivian Liu:** That's my current process.

**George Haikal:** So, so the quiz and transcript, so that's, the quiz and transcript summary is the form they're filling out, plus the AI insights from the transcript, yeah?

**George Haikal:** And it's a summary of that.

**George Haikal:** And then the retrieved documents, this is from the inventory, I'm assuming.

**Vivian Liu:** Yeah.

**George Haikal:** And then what's the prompt that's calling on these two things to provide the recommendation?

**Vivian Liu:** It's this massive prompt that I have here.

**Vivian Liu:** I don't know if I can expand it.

**Vivian Liu:** So I'm asking for five scenarios that would be most relevant for this customer.

**Vivian Liu:** And the one that I narrowed down for the different scenario options is like a trim ladder showing like the going from one, like a low trim to a higher trim.

**Vivian Liu:** Moving up in size, it could be like moving down in size, looking at a comparable, someone says Toyota, maybe we show them a Honda showing comparable brands.

**Vivian Liu:** If they said the fuel economy is important to show vehicles similar in fuel economy, trade-offs.

**Vivian Liu:** that's it.

**Vivian Liu:** scenarios where they have to give up features or comparing a used version to the new version.

**Vivian Liu:** So those are the ones in my head that come up the most.

**Vivian Liu:** And when you said like going through the steps of like trying to figure it out, those are technically the steps.

**Vivian Liu:** It's I just don't know like what necessarily in what order.

**Vivian Liu:** So then it gives me in a table three vehicles.

**Vivian Liu:** And I also ask it to explain why.

**Vivian Liu:** So I've just been going through them.

**Vivian Liu:** And I'm finding like where it's going wrong.

**George Haikal:** Yeah, I think that makes sense.

**George Haikal:** Like that's all it is, back and forth iteration.

**George Haikal:** Like if you never want something added to happen again, you add it and like reinforce that in the prompt.

**George Haikal:** It's like don't ever do this thing or always make sure you do this thing.

**George Haikal:** And then I guess the only other question I'd have is like in the inventory of the actual vehicles.

**George Haikal:** Like what you had there was price and like some stat.

**George Haikal:** Like is there anything you could enrich the inventory with that would help?

**George Haikal:** I'm going Thanks.

**George Haikal:** Thank

**George Haikal:** The model connect the dots between the person, what's important to the person, why it matters, and like why this vehicle in this inventory could make more sense.

**George Haikal:** It sounded like you already did some of that.

**Vivian Liu:** I am.

**Vivian Liu:** I just feel like I'm doing all of this.

**Vivian Liu:** I'm coming up with all of this and like lumping it together and not putting it like what you said, enriching the inventory.

**Vivian Liu:** Like I feel like I'm not updating the prompts in the right place and I just feel very scattered.

**George Haikal:** Yeah, mean talk to Japheth about it because I don't know how it's like your thing, your system's working in the, in the back end, but like the more you can break it into steps and have as detailed of a prompt that you had for like your master system prompt that you showed me for the recommendation, that you can have that much detail in a step or like at each step.

**George Haikal:** Yeah.

**George Haikal:** And so it's like, here's the transcript.

**George Haikal:** Here's what I want to make sure you got out of the transcript and then how well you understand this person and like what they care about that then it moves on to the next step then.

**George Haikal:** It's like, okay, use the inventory, everything you know about the inventory, and match that to these certain things with what you understand from the person so far.

**George Haikal:** Then the output of that is an expert.

**George Haikal:** Then you can just keep refining each step, and then you'll still get to the same output.

**George Haikal:** It will just be better, because you have a prompt at each step, and you're the expert, so you'll know what you need at each step and how to tweak the prompts.

**George Haikal:** And then that's what makes it more repeatable and consistent and reliable.

**Vivian Liu:** Yeah, I think that's it.

**Vivian Liu:** I think it's the breaking down the steps that need to just, like, whiteboard it.

**George Haikal:** Yeah, and it's helpful, like, to actually break down the steps in, like, a chart or Excel view, right?

**George Haikal:** Because that's how, like, our pipelines are.

**George Haikal:** Like, what I showed you was the cells and the boxes, and, like, each column was a workflow.

**George Haikal:** So you know, like, what the goal is of each one of these steps.

**George Haikal:** Each step is associated with a prompt and an action, either a genetic or a continuous thing.

**George Haikal:** Or just one thing.

**George Haikal:** It's like, hey, enrich this with all the most relevant keywords from Sunrush.

**George Haikal:** Okay, done.

**George Haikal:** Now, next step, use these keywords and the output from this last step, and then generate topics for articles that make the most sense based on the company's business.

**George Haikal:** And that artifact that I'm referencing the company's business, that can be the same thing as your inventory.

**George Haikal:** It's like whatever is like a source of truth, a knowledge base that you have, you can continue to refer to that in each one of your steps, in each one of your prompts.

**George Haikal:** Because it's like the same thing as the cloud project.

**George Haikal:** You can put stuff in it and have each step refer to it.

**George Haikal:** Like you could do each step in a cloud project itself, or like in a tool like AirOps or Airtable.

**George Haikal:** Don't use AirOps because they're our competitor.

**Vivian Liu:** AirOps?

**Vivian Liu:** Never heard of it.

**George Haikal:** Don't worry about it.

**Vivian Liu:** Never heard it.

**Vivian Liu:** Okay, got it.

**George Haikal:** But it is complicated and it's like frustrating because it's so much back and forth and testing, but it'll save you.

**George Haikal:** And like it's the only way it gets repeatable.

**George Haikal:** Yeah.

**Vivian Liu:** No, that's really helpful.

**Vivian Liu:** I just need to, like, hunker down and do nothing else except for this.

**Vivian Liu:** I think I was, like, trying to split my time between, like, sales and wanting to get all the wearables done properly and then trying to figure this out.

**George Haikal:** I just wasn't doing any of it properly.

**George Haikal:** Yeah.

**George Haikal:** You also need someone who's, like, knows this .

**George Haikal:** Like, I do not know this .

**George Haikal:** There's people who, like, live and breathe this every day.

**George Haikal:** Yeah.

**George Haikal:** And, like, they'll be able to help you way more because you know, like I said, what we do, we still use experts because they require the important steps and they know what good looks like and they know how to go iterate and essentially what they change the prompts to.

**George Haikal:** Right?

**George Haikal:** You're that expert and, like, you know, you can get in the weeds too and create the prompts with, like, someone can help make the process work smoother for you as well.

**George Haikal:** And Javid probably, I mean, I don't know how much he knows about this stuff, but.

**Vivian Liu:** I think she's getting to it, but I think it's up to me to tell her, like, how it needs to be structured, and that's where...

**George Haikal:** That's nuts.

**George Haikal:** That's nuts.

**Vivian Liu:** Is she the CTO?

**Vivian Liu:** Yeah.

**George Haikal:** She should be on top, inside and out of this.

**George Haikal:** Like, it's insane.

**Vivian Liu:** Yeah, I know.

**Vivian Liu:** I know you said, like, I should talk to Danny, but you guys are fundraising, so I don't want to bother him.

**George Haikal:** Yeah, but we'll be done, hopefully, at the next week.

**Vivian Liu:** Okay, cool.

**Vivian Liu:** Hopefully.

**Vivian Liu:** Yeah, hopefully, you guys will crush it.

**Vivian Liu:** If you...

**Vivian Liu:** Do you think he'd be open to having a chat?

**George Haikal:** know, like, there's no good time.

**Vivian Liu:** sure.

**George Haikal:** So...

**George Haikal:** Yeah, yeah, yeah.

**George Haikal:** Once he...

**George Haikal:** I mean, he hasn't even showed up for, like, a month, because this guy's cranking in the office.

**George Haikal:** We don't mess with Daniel when he's not showing up, because this guy...

**George Haikal:** You never have to worry about the work with him.

**George Haikal:** You just let him cook.

**George Haikal:** But, yeah, once he...

**George Haikal:** Once we close the round, I think everyone's going to take, like...

**George Haikal:** There, too, to take a deep breath.

**Vivian Liu:** Yeah.

**George Haikal:** Okay.

**George Haikal:** Definitely.

**George Haikal:** Hopefully I can figure this stuff out before then, too.

**George Haikal:** I will say he understands everything.

**George Haikal:** The business, kind of how to speak to non-technical people, and then obviously he's an expert in the technical stuff.

**George Haikal:** I will say to make the conversation most worth it, he is super technical.

**George Haikal:** So, like, make sure you know what level you want to speak to him at, what level of abstraction you want to speak to him at.

**George Haikal:** And make sure to tell him to dumb things down as well, because otherwise he'll just go super deep, or he'll miss.

**Vivian Liu:** Do you think it's worthwhile to have Janet on the call?

**George Haikal:** If she's well-versed, it probably wouldn't hurt.

**Vivian Liu:** I mean, she's more well-versed than I am, but I think there's just a disconnect.

**George Haikal:** And for her to see how an actual AI-powered CTO operates, yeah.

**Vivian Liu:** Yeah.

**Vivian Liu:** Yeah.

**Vivian Liu:** I think that would be good.

**Vivian Liu:** Okay.

**Vivian Liu:** All right.

**Vivian Liu:** I'm going to go call this person and hopefully they have my ring and she's willing to come.

**Vivian Liu:** that's so crazy.

**George Haikal:** Thank you so much for the time catching up.

**George Haikal:** Yeah, was good catching up.

**George Haikal:** This was awesome.

**George Haikal:** This was awesome.

**George Haikal:** I miss you.

**George Haikal:** So it was good to catch up on everything that you're doing.

**Vivian Liu:** Yeah.

**Vivian Liu:** I had a friend offer me to let her or let me stay at her place for September.

**Vivian Liu:** I'm like, oof, maybe.

**George Haikal:** In SF?

**Vivian Liu:** Yeah.

**George Haikal:** That's hype.

**George Haikal:** That's hype.

**George Haikal:** Yeah, I caught up with Encore last week and then talked to Carlo like one or two weeks before.

**George Haikal:** think him, Alex, want to do a trip to the States at some point, but probably on the East Coast, which is more essential for everyone.

**George Haikal:** You come to SF whenever you can, please.

**George Haikal:** have a great time.

**George Haikal:** You can come hang in the office.

**George Haikal:** There's so much to learn.

**George Haikal:** It's absolutely unbelievable.

**Vivian Liu:** So you'd love it.

**Vivian Liu:** I might take you up on that.

**Vivian Liu:** Maybe that's the environment that I need is like, I need a, if this is like.

**Vivian Liu:** If thing and it's the only thing that I need to like really propel us, then maybe I need to be around some experts.

**George Haikal:** Yeah, it wouldn't hurt for sure.

**George Haikal:** It definitely wouldn't hurt.

**George Haikal:** Cool.

**George Haikal:** This was great.

**Vivian Liu:** We'll talk soon, yeah?

**Vivian Liu:** Yeah, sounds good.

**Vivian Liu:** Have a good day.
