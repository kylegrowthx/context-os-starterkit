# Engine <> Growth X - Weekly Sync

<metadata>
date: 2026-02-19
time: 19:28 UTC
duration: 33 minutes
organizer: team@growthxlabs.com
participants: Carly Piekos, Joel Murphy
fathom_recording_id: 123844035
fathom_url: https://fathom.video/calls/571614095
share_url: https://fathom.video/share/Cd-sX1fGXsryNzDeHEzX-nrxzvwE4LD-
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Carly and Joel synced on Nginx content approval status: 4 of 7 articles are with Legal, 3 pending final edits (due EOD that day), and none submitted to the bank yet. Weekly Amplitude metrics show consistent growth across all topic clusters (LLM visibility score up 2% to 16%), validating Engine's content strategy. Joel flagged AI output issues (out-of-context quotes, repetitive language on "direct bill") and proposed structured feedback tables (A → B format) to improve system prompts instead of scattered Google Doc comments. Carly committed to consulting the team on survey prompt for ChatGPT-referred traffic and defining a structured feedback process template.

---

## Context

Engine is a financial services/payments platform that GrowthX has been working with on content marketing for Nginx — a complex financial product feature. This is a GrowthX client engagement where Carly (GrowthX content strategist) is helping Joel (Engine) develop and approve content for bank-related topics. Engine uses Amplitude for performance tracking, Airtable for content management, and needs approvals from their bank before publishing financial content. The engagement includes both content creation (via AI assistance managed by GrowthX) and performance analysis. Joel has limited bandwidth for content work (it's not his primary focus), so he values having GrowthX handle the heavy lifting of research, drafting, and feedback synthesis.

---

## Relevance

**To GrowthX Delivery:**
- Structured feedback process (A → B tables in Google Sheets) replacing scattered Google Doc comments — operationalizes Joel's feedback loop and makes it easier to scale as Engine adds a dedicated growth lead.
- Bank approval timeline is ~1 week; 4 Nginx articles already submitted, 3 more expected that day — staying on track.
- Airtable overwrite strategy (single "biblical" source of truth) clarifies content ownership and prevents version confusion.

**To CheckThat & AEO:**
- Engine is building a ChatGPT survey (triggered on UTM parameter) to capture original prompts driving traffic — direct signal on high-intent search queries that CheckThat could reference in future AEO research.
- Amplitude data shows Engine gaining 4-5 metric points weekly per topic cluster; LLM visibility score now 16% — validates AEO/content strategy effectiveness.

**To GrowthX Business Development:**
- Engine renewal cycle begins in ~3 months; Joel expressed satisfaction with the partnership and value of offloading content work. Incoming growth lead may have different requirements but no churn signals flagged.
- AI output quality feedback (out-of-context quotes, over-correcting on "direct bill" language) is a product improvement opportunity for future AI system prompts — impacts how well GrowthX can serve similar financial services clients.

---

## Overview

- **Nginx Content Advancing:** 4 of 7 Nginx articles are with Legal; the remaining 3 will follow today. Joel will overwrite Airtable with final, approved versions to create a single source of truth.
- **Performance Growing:** Key metrics are up 4–5 points weekly (e.g., visibility score for LLM models +2% to 16%), validating the content strategy.
- **Process Refinement:** To improve AI output, Joel will provide structured feedback (e.g., "A → B" tables) for system prompt updates, replacing scattered Google Doc comments.
- **New Survey Planned:** A survey on ChatGPT-referred traffic will ask users for their original prompt, aiming to uncover high-intent search queries.

---

## Key Topics

### Nginx Content Approvals

  - Joel self-edited Nginx content to expedite the process, finding only minor tweaks were needed (e.g., "digital card" → "virtual card").
  - The team will not implement a formal approval workflow, keeping the process lean.
  - **Current Status:**
      - 4 articles with Legal.
      - 3 articles pending final internal edits (deadline: EOD today).
      - No articles submitted to the bank yet.
  - **Process Improvement:** To streamline reviews, Joel will create a single, "biblical" source of truth by overwriting the original Airtable docs with the final, approved versions.

### Performance & Data

  - Amplitude data shows consistent weekly growth across all topic clusters.
  - **Weekly Metric Comparison:**
      - Visibility Score: 14% → 16% (LLM models)
      - Other Metrics: 74→80, 93→98, 34→36
  - **New Data Initiative:** Joel's team is building a survey to capture the original ChatGPT prompt that led users to Engine's site.
      - **Goal:** Uncover high-intent search queries to better inform content strategy.
      - **Method:** Trigger survey on traffic with the ChatGPT UTM parameter.

### Process & AI Output Feedback

  - Joel's primary value from the partnership is offloading content work, as it is not his main focus.
  - **AI Output Issues Identified:**
      - **Out-of-Context Quotes:** Inserting irrelevant quotes (e.g., a FlexPro quote in an Nginx article) that break the narrative.
      - **Overly Repetitive Language:** Over-correcting on feedback, such as stating "requires credit approval" every time "direct bill" is mentioned.
  - **Proposed Solution:** Replace scattered Google Doc comments with structured feedback (e.g., "A → B" tables) to enable direct updates to the AI system prompt.

---

## Action Items

**Joel Murphy**
- Send Nginx edits table to Carly via Slack
- Overwrite Airtable original w/ approved Nginx content; Slack Carly link

**Carly Piekos**
- Review Ready to Publish items
- Move all pending items to Client Review
- Consult team re: LLM survey prompt/trigger; share guidance w/ Joel
- Define and share structured feedback process/template w/ Joel

---

## Transcript
**Carly Piekos:** Hello.

**Carly Piekos:** How are you doing today?

**Joel Murphy:** Oh, I am running around with a chicken with no head.

**Carly Piekos:** Yeah, I feel very similar, Joel.

**Carly Piekos:** I can relate on that level.

**Carly Piekos:** Did you end up hiring?

**Carly Piekos:** Anybody to help you yet?

**Joel Murphy:** Yeah, so I got a new guy on my team started last Monday.

**Carly Piekos:** Awesome.

**Joel Murphy:** Got a couple strong candidates pretty far in the process now.

**Joel Murphy:** So, yeah, looking promising.

**Carly Piekos:** Awesome.

**Carly Piekos:** Your house is so cool.

**Carly Piekos:** Every time I see you, you're in a different room.

**Carly Piekos:** I'm at my mom's house.

**Carly Piekos:** I was going to say, I'm like, what, like a tour, please.

**Joel Murphy:** Yeah, no, no, this is my mom's house.

**Joel Murphy:** She had hip replacement surgery on Monday.

**Joel Murphy:** So I've been here this week to just kind of make sure that goes fine.

**Carly Piekos:** No wonder you're stressed out.

**Carly Piekos:** All right.

**Carly Piekos:** Well, we don't have to take very long with today's session.

**Carly Piekos:** I just kind of wanted to go through a couple of things.

**Carly Piekos:** Did you end up looking through that document I sent over right after our meeting yesterday?

**Joel Murphy:** Yeah, I looked through it yesterday. I did, and it was helpful.

**Joel Murphy:** It's funny.

**Joel Murphy:** So I took all of our Nginx content.

**Joel Murphy:** I made edits myself just to speed things up.

**Carly Piekos:** I told you guys I was going to do that based on things I was finding in our GTM docs and our Slack bot and whatever.

**Carly Piekos:** Yeah.

**Joel Murphy:** The product team, like they made it sound like, oh, we're going to have all these edits and blah, blah, blah.

**Joel Murphy:** It really was not that much.

**Joel Murphy:** Um, so I'm glad we did it.

**Joel Murphy:** I did get a few things I'm going to feed back to you guys about Nginx, but it's not like really, like we weren't that far off.

**Joel Murphy:** We're just like little things like digital card has to be virtual card, you know, stuff like that.

**Carly Piekos:** Oh, okay.

**Carly Piekos:** Okay.

**Joel Murphy:** So I have that stuff to send. And I don't think we're going to do that whole approval flow, not long-term and probably not in short order either.

**Carly Piekos:** So with the statuses, here's what I did. I set up pending product approval, pending bank approval, and all approval signed in there. Is that what you were thinking?

**Joel Murphy:** Yep.

**Joel Murphy:** Yeah.

**Joel Murphy:** So I've got, let me see.

**Joel Murphy:** I've got four with product approval.

**Joel Murphy:** I've got three that had some pending edits that I made, and I'm going to give them until the end of today to like further comment.

**Joel Murphy:** And if they don't, I'm moving those to product approval.

**Joel Murphy:** I have submitted the four of those seven to legal.

**Joel Murphy:** And then I'll submit the other three to legal.

**Joel Murphy:** And we have not submitted any of this content yet to the bank.

**Joel Murphy:** We've submitted landing page stuff, and it took about a week.

**Joel Murphy:** So I'm not sure if that will be faster or slower with this stuff.

**Joel Murphy:** In all the articles I've highlighted everywhere Nginx is mentioned.

**Joel Murphy:** So they hopefully will comb through that stuff.

**Joel Murphy:** And not have to, like, read everything top to bottom.

**Carly Piekos:** Okay.

**Joel Murphy:** And then one other thing on this, like, because I had to make edits and make copies of docs so the bank can read them.

**Joel Murphy:** So I'm going to go back to the original doc that you guys have in Airtable.

**Joel Murphy:** I'm just going to overwrite it with everything that's approved.

**Joel Murphy:** So there'll be no question when you guys take it, it's the biblical version of the content.

**Carly Piekos:** Okay.

**Carly Piekos:** Perfect.

**Joel Murphy:** Got them to sign off for it.

**Joel Murphy:** So I'll just pass that one to you through Slack, I guess.

**Carly Piekos:** Okay.

**Carly Piekos:** I will figure out what these, the ones that she marked pending bank approval.

**Carly Piekos:** And then I will get back to you on that.

**Carly Piekos:** For the revisions, we have, this is pending approval.

**Carly Piekos:** Yes, that's what you marked.

**Carly Piekos:** Just pending approval or under review.

**Carly Piekos:** I put under the priorities.

**Carly Piekos:** I don't know if that's confusing though.

**Carly Piekos:** So I just want to make sure that we have under review pending approval.

**Carly Piekos:** you want me to get rid of pending approval and just put under review?

**Joel Murphy:** No, let's leave it because I can use under review as like an analog for our internal review.

**Joel Murphy:** And then pending approval will be.

**Carly Piekos:** I can change the color though, just so it's not as.

**Carly Piekos:** I'm trying to be as.

**Carly Piekos:** I'm

**Carly Piekos:** What is it called?

**Joel Murphy:** Organized as possible.

**Joel Murphy:** Why isn't this?

**Joel Murphy:** I'm eagerly the color.

**Joel Murphy:** It's all good. I'll use pending approval when we're waiting on final approval from the bank.

**Carly Piekos:** Okay, I'll change the colors to match and organize everything. Now that we have that sorted, we'll figure out how to organize the ones that automatically shifted.

**Carly Piekos:** For new topics to approve, we have none. We have one ready to publish. I'm behind on reviewing stuff, but I'll pick up anything that's in there tomorrow. I think I need to move all of these to client review.

**Carly Piekos:** That's good news.

**Carly Piekos:** When I looked at your Amplitude data, it's the same theme — you're going up by like four or five in each category every single week across each topic cluster. Everything is looking on the up and up. Your visibility score for LLM models specifically went up 2% over the past week, from 14% to 16%, which is something to celebrate.

**Carly Piekos:** So yeah, 74, 93, and 34 was last week.

**Carly Piekos:** And this week is 80, 98, and 36.

**Carly Piekos:** So a few percentages, but still, like, anywhere up is up.

**Carly Piekos:** So I am always happy to see it.

**Joel Murphy:** Cool. I've got somebody on my team working on a way for us to collect survey responses. I want to run it on traffic that comes from LLMs, and I want to ask what they were talking to the LLM about that sent them here. I'm not expecting an absolute deluge of responses, but when we have that in place, I'll definitely share it to give us some signal.

**Carly Piekos:** That's a really good idea. I think you would probably either use the word "question" or "prompt," right? Question might be a bit more universal. It's like, "What question did you use to get to this answer?"

**Joel Murphy:** Yeah, I haven't really figured that out. I don't want to lead the witness, so to speak — I don't know if I want to send a question because it might not be a question. I kind of want to say, "Hey, we noticed you came from ChatGPT. What were you talking to ChatGPT about?" and just let them fill it in. ChatGPT sends a UTM parameter with referred traffic, so it's pretty easy to pick up. I'm not sure about the others, but ChatGPT is the biggest one anyway. We're definitely going to do that.

**Carly Piekos:** I'll talk with the team and see if anybody else has come across this situation and how they managed it. So basically the goal is to confirm what they were talking and chatting with ChatGPT about, so you can cater towards that specific prompt set.

**Joel Murphy:** Yeah, essentially. The idea came from when I was at Deal — Deal's not free, so the pricing page is more important than at Engine. It was the second most popular page on our website, and we ran a survey with Hotjar that asked, "Was there anything you found confusing about our pricing?" You inevitably get a bunch of noise, but for every 10 responses, three gave you some useful idea. We'd wait 10-20 seconds after someone was on the page, and then the survey would pop up.

**Carly Piekos:** Yeah, that's a really efficient way to go about it. Please keep me updated on that. I'll also check with the team and see if anybody else has come across this, and we can collaborate and talk about it next week.

**Carly Piekos:** But yeah, I think that's all I have for today. Is there anything else you want me to run through or discuss?

**Joel Murphy:** Yeah, the conversion data. Can you remind me what all that entails? I can't remember the details. Nginx won't be done until next week, but I just want to make sure I'm not forgetting that.

**Carly Piekos:** Yeah, so the conversion data is in a drop-down. Kyle put it all there under the strategy. It'll give you the why we're doing this, the setup, and the data requirements. There's also a link to the Google Drive and sheets.

**Joel Murphy:** Okay, I have a note for this already.

**Carly Piekos:** Okay, cool. That way we can get more accurate reporting.

**Carly Piekos:** So how are you feeling about the partnership overall? I know you just signed the renewal. Is there anything that you feel like could be improved moving forward, or anything that would guarantee renewal in the next five months? We have to start the renewal process three months before your renewal date, so we're almost up on renewal again.

**Joel Murphy:** Yeah, renewal is coming up in about a month. It's hard for me to say because this is only part of what I do on the Engine website — it's not my focus. But I value the relationship because you guys do a lot of this work and make decisions that I just don't have the space for. Someone coming in as the growth lead might have a different, more specific answer. Their sole focus would be this type of work, so their perspective might be different.

**Joel Murphy:** I don't know if a new growth lead would feel differently — it could be good, bad, or indifferent. But for me, I'm happy to have you guys here to give us a hand. That said, there are things we could do better.

**Joel Murphy:** We talked about this in the last couple of weeks. With the AI output, there are some tweaks we could make. I made a request late last year to start bringing customer quotes into the content, and the AI is so eager to do that it's inserting them outside of context. For example, there was an Nginx piece that had a FlexPro quote when Nginx and FlexPro aren't really related — it just feels completely out of context when you're reading it. Then there's also the angle of inserting the wrong quote entirely. We're talking about direct bill and we have quotes about direct bill, but the AI stuck a FlexPro one in there.

**Carly Piekos:** Got it.

**Joel Murphy:** Those kinds of things would be helpful to solve. The other issue is with direct bill. We initially described the features as if they were a default part of Engine, so I requested that we specify you need credit approval to use direct bill. But then the AI got really eager with that — every time we mentioned direct bill, it automatically added "requires credit approval." We don't need to say it literally every time. It's a nuance: we need to be careful about not making direct bill features sound like a day-one sign-up, but without inserting fine print every time we say the words.

**Carly Piekos:** Okay.

**Carly Piekos:** Is there anything else that I can bring back to the team and solve any other problems that we could possibly solve for you?

**Joel Murphy:** The intention is there, but maybe the way we're doing it isn't perfect. I'm thinking there's a way for me to be more explicit in documenting feedback. If you guys can tell me, "Hey, if we inserted something exactly like this in our system prompt, it would make a difference" — tell me what X is, and I can write X and share it with you.

**Carly Piekos:** Okay, so I think the disconnect could be when you're reviewing the articles. Let me think through this out loud. Essentially, any issues that come up in the articles, we'd make a quick comment in Google Docs and then get those adjusted immediately. With this new person coming in, they'd be in charge of reading and making those comments for specific products, but they'll need training and time to catch those things. But if I'm trying to think of an easy way that doesn't put more on your plate...

**Joel Murphy:** I don't mind more on my plate if it means I have to read less — reading is my least favorite thing in my entire job.

**Joel Murphy:** Reading helped in the beginning to understand all the Engine ins and outs, but at this point it's just painful. So I'm wondering if my comments can stay, still feedback what needs to change in a specific piece. But maybe I can catalog my feedback in a structured way — like when I share the Nginx changes, I copied the original blurb and the updated blurb, showing what changed from A to B. That's more actionable than the scattered comments and docs we have now.

**Joel Murphy:** Yeah. With a Google Sheet or something like that — a rundown of specific changes. So next week when I'm reviewing new content, hopefully nothing from that sheet is still a problem. But if it is, I can flag it specifically instead of making another scattered comment. It's more formalized and easier to see in aggregate than tons of separate comments.

**Carly Piekos:** Yeah, agreed. I have to hop to another call, but I'm going to think about a more efficient way to do this. I'll get feedback from the content managers on how to set it up and format it, so I can explain it better next time.

**Joel Murphy:** Okay.

**Joel Murphy:** Sounds good.

**Carly Piekos:** All right.

**Carly Piekos:** Perfect.

**Carly Piekos:** I hope you have a good rest of your week and I hope your mom gets better soon.

**Joel Murphy:** Oh, she's doing great. She's walking around three hours after having her hip replaced — it's unbelievable.

**Carly Piekos:** That's amazing. Well, thank you.

**Joel Murphy:** I appreciate that. I'll see you.

**Carly Piekos:** Bye.
