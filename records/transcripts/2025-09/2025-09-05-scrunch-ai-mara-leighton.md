# Scrunch AI (Mara Leighton)

<metadata>
date: 2025-09-05
time: 14:31 UTC
duration: 33 minutes
organizer: Vivek Shankar
participants: Mara Leighton, Andrew Sorensen, Vivek Shankar
fathom_recording_id: 85279377
fathom_url: https://fathom.video/calls/401061161
share_url: https://fathom.video/share/ucFyy3cvWU6bex3iKgrenifDxKU4C9Nw
source: fathom
enriched_on: 2026-03-02 18:45 UTC
</metadata>

---

## Summary

Vivek Shankar and Mara Leighton (GrowthX) met with Andrew Sorensen (Scrunch AI) to understand recent product updates and dashboard changes. Andrew clarified how competitive presence metrics are calculated and ordered by last 7-day activity, and explained the distinction between prompts and responses (seed prompts × platforms = total prompts). The team discussed API access, Looker Studio integration options, and product limitations, with plans for a follow-up meeting to explore Looker integration and address remaining questions about prompt categorization and condensation behavior.

---

## Context

Scrunch AI is an AI visibility index platform that GrowthX uses for client delivery. This meeting was triggered by Vivek Shankar, who works under Mara Leighton, accumulating questions about the platform while working with client dashboards. Mara coordinated directly with Andrew Sorensen, head of Scrunch AI product, to get authoritative answers rather than working through the normal support channel. The call was timely because Scrunch had just released significant product enhancements the previous day (September 4) that changed metric calculations, requiring clients to understand the shifts.

---

## Relevance

**To GrowthX Delivery:**
- Recent Scrunch AI product enhancements changed metric calculations and competitive presence ordering (now by last 7 days, with customizable timeframes coming); GrowthX must update client communication and dashboards accordingly.
- Competitive presence metrics are platform-specific, not aggregated across all responses, affecting how GrowthX explains competitive data to clients (e.g., Galileo client visibility).
- Scrunch API access is available to GrowthX at no additional cost, enabling potential custom reporting and Looker Studio integrations for enhanced client dashboards.

**To GrowthX Business Development:**
- Andrew Sorensen indicated GrowthX is a "super important client" for Scrunch, suggesting strong relationship and expansion potential.
- Scrunch platform has acknowledged reporting limitations but is actively developing improvements, positioning GrowthX to build custom solutions (Looker Studio) and stay ahead of client demands.
- Follow-up meeting planned for next week to explore Looker integration with Andrew's team, indicating deepening product partnership.

---

## Overview

- Recent product enhancements have changed some metric calculations and dashboard features
- Competitive presence metrics and prompt/response data interpretation require clarification
- API integration and improved data visualization options (e.g., Looker Studio) are available for enhanced reporting

---

## Key Topics

### Dashboard Updates and Metric Changes

  - Product enhancements rolled out recently, affecting metric calculations and dashboard features
  - New time frame filters added (e.g., last 4 weeks, 12 weeks), with custom date range coming soon
  - Prompt and response calculations explained: seed prompts × platforms = total prompts

### Competitive Presence and Citation Metrics

  - Competitive presence shows frequency of company mentions across all responses
  - Citations indicate specific references or attributions in responses
  - Competitors section shows presence per platform, not an aggregate of all responses
  - Suggestion made to replace percentage with platform logos for clarity

### Key Topics and Prompt Categorization

  - CSV upload takes precedence in assigning key topics to prompts
  - System attempts to categorize prompts without specified topics based on intent
  - Manual changes to categories may cause unexpected recategorization of prompts

### Prompt Design and Search Query Condensation

  - Platforms condense long-tail prompts into shorter search queries
  - Condensation patterns are not always predictable or consistent
  - Recommendation to continue using prompt variants until more platform guidance is available

### API and Reporting Features

  - API access available to GrowthX at no additional cost
  - Looker Studio integration possible for improved data visualization and client reporting
  - Current platform lacks robust reporting features, but improvements are in development

---

## Action Items

**Mara Leighton (GrowthX)**
- Share meeting insights with rest of team re: Scrunch AI dashboard updates, competitive presence calculation, prompt vs response distinctions

- Review other client dashboards to compare prompt numbers and platform usage for consistency

**Vivek Shankar (GrowthX)**
- Book follow-up meeting with Andrew Sorensen via Calendly for next week. Include Will in invite.

- Prepare questions about API integration with Looker for next meeting with Andrew

**Andrew Sorensen (Scrunch AI)**
- Confirm with engineering team about prompt recategorization behavior when categories are manually changed

---

## Transcript
**Mara Leighton:** A couple minute late here.

**Mara Leighton:** Hey, Andrew, how are you?

**Andrew Sorensen:** Hey, Mara, I'm good.

**Andrew Sorensen:** Vivek, I don't think we've met before today.

**Andrew Sorensen:** Is that right?

**Vivek Shankar:** You and I haven't, no.

**Mara Leighton:** But Vivek and I don't think you've met.

**Vivek Shankar:** Yeah, yeah.

**Andrew Sorensen:** Yeah, it's the first time.

**Vivek Shankar:** So basically, I work under Mara, and then basically, I was just digging into scrunch for our reporting, et cetera.

**Vivek Shankar:** I kept bombarding her with questions.

**Vivek Shankar:** She got sick of me.

**Vivek Shankar:** She's like, just ask Andrew.

**Andrew Sorensen:** So here we are.

**Andrew Sorensen:** No, it's just, we're cutting out the middleman here.

**Vivek Shankar:** I don't know.

**Vivek Shankar:** So, yeah, thank you so much for taking the time.

**Vivek Shankar:** I was wondering if I could just share my screen and just run through my questions real quick.

**Andrew Sorensen:** Yeah, please do.

**Andrew Sorensen:** I was going to pull up mine as well, because I think these are all about Galileo.

**Andrew Sorensen:** Is that right?

**Vivek Shankar:** Some about Galileo, but some about just general metrics and how the dashboard is going.

**Andrew Sorensen:** And real quick, I just want to be real clear.

**Andrew Sorensen:** We did roll out a lot.

**Andrew Sorensen:** A lot of product enhancements just yesterday.

**Andrew Sorensen:** So there's some stuff in here around metrics and around the way things are calculated.

**Andrew Sorensen:** So that changed as of yesterday.

**Andrew Sorensen:** So happy to answer those.

**Andrew Sorensen:** Just understanding that it may, I'm just letting Mara know some of the way that we've explained it in the past may not be true as of yesterday.

**Andrew Sorensen:** Okay.

**Andrew Sorensen:** Okay, cool.

**Andrew Sorensen:** Thank you for the heads up.

**Mara Leighton:** I'm glad this is a perfectly timed conversation and we'll share this with the rest of the team as well.

**Mara Leighton:** And then also, just as a heads up, at the end, I have slightly more general, like kind of conceptual questions if we happen to have the time.

**Mara Leighton:** Cool.

**Mara Leighton:** Awesome.

**Andrew Sorensen:** Sounds good.

**Andrew Sorensen:** Great.

**Andrew Sorensen:** All right.

**Vivek Shankar:** So just, you know, caveat, I'm sorry if Mara has already asked these questions or you've answered them with Jason before, but I'm just going to run through it real quick.

**Vivek Shankar:** The first question I had was the competitive presence.

**Vivek Shankar:** So I'm looking at Galileo here.

**Vivek Shankar:** The competitive presence, like how is this ordered?

**Vivek Shankar:** Is it...

**Vivek Shankar:** Is it the client comes first, or is it like whoever has the highest presence comes on the left or something?

**Vivek Shankar:** That's it.

**Andrew Sorensen:** And the way that I've seen, if you hover over each of the, for Galileo AI, if you hover over those, you see we've got last 90 days and last seven days.

**Andrew Sorensen:** Historically, the way that it's been ordered has been by last seven days.

**Andrew Sorensen:** So that'll be the prioritization.

**Andrew Sorensen:** Whatever's the highest of the last seven days, they rank order them in that way.

**Andrew Sorensen:** And then, but you'll also see the last 90 days there as well.

**Andrew Sorensen:** And then, again, I do want to call out, if you look at the top, if you click on right underneath dashboard, where it says last 12 weeks, a little bit higher up.

**Andrew Sorensen:** Yep.

**Andrew Sorensen:** Yep.

**Andrew Sorensen:** Right there.

**Andrew Sorensen:** So now we've got some different filters.

**Andrew Sorensen:** If you hit on like last four weeks, then it's going to filter by the last four weeks.

**Andrew Sorensen:** And when we say 12 weeks, it's 90 days.

**Andrew Sorensen:** That's what it is.

**Andrew Sorensen:** Last four weeks is one month is what we're looking at there.

**Andrew Sorensen:** And then later today, hopefully, if not Monday, in addition to what you see there, you will also be able to specify time frame.

**Andrew Sorensen:** So you'll be able to go in and say, I want to see from June 1 to today.

**Andrew Sorensen:** So you'll also have that.

**Andrew Sorensen:** then it will rank order based off of whatever that filter is that you've put on there from a time frame.

**Andrew Sorensen:** Cool.

**Andrew Sorensen:** That sounds good.

**Vivek Shankar:** Yeah, go ahead.

**Vivek Shankar:** So sorry.

**Mara Leighton:** Just one really quick question since we're looking at this.

**Mara Leighton:** The prompts.

**Mara Leighton:** So it says 1,953 and then the responses a little bit over 5,600.

**Mara Leighton:** What is that calculating there?

**Mara Leighton:** Just because I've noticed that Galileo's is significantly higher than some of the other clients that we're tracking, but the same like general number of prompts.

**Mara Leighton:** But we've switched the prompts a few times.

**Mara Leighton:** So anyway, just curious for what that, what the reasoning might be.

**Andrew Sorensen:** And this is even non-branded prompts.

**Andrew Sorensen:** So this isn't all the prompts unless they're all non-branded.

**Andrew Sorensen:** So what the way that we calculated is you have what's called a seed prompt.

**Andrew Sorensen:** And then we, and then we run it across.

**Andrew Sorensen:** However, however,

**Andrew Sorensen:** Any different platforms you choose, whether it's the full seven, whether it's three, whatever it is, that's how you get to that prompts number, is the number of the base core prompts times the number of platforms that you run it across.

**Andrew Sorensen:** Okay.

**Andrew Sorensen:** Okay.

**Vivek Shankar:** So, okay.

**Vivek Shankar:** All right.

**Mara Leighton:** We can circle back there.

**Mara Leighton:** I'm just going to look at some of the other dashboards, just because I've noticed that they're, anyway.

**Vivek Shankar:** Yeah, I think here we're tracking all seven, so maybe that's like expanding the thing.

**Vivek Shankar:** Yeah, that will.

**Andrew Sorensen:** Yeah.

**Andrew Sorensen:** Cool.

**Vivek Shankar:** Yeah, the next question I had was, so we have the list and, you know, this, I'm just wondering, like, how all of this ties together.

**Vivek Shankar:** So, citations, like, I understand what citations are, you know, according to this data, competitors are not being mentioned, or slightly, little more than Galileo.

**Vivek Shankar:** So, my guess is our prompts are slightly off here.

**Vivek Shankar:** But when I come to...

**Vivek Shankar:** On to this list, it says like brain trust 86%, 81%, 67%, just wondering how does this pie chart or donut chart here correlate to these percentages?

**Vivek Shankar:** It doesn't.

**Vivek Shankar:** Those percentages would correlate with presence.

**Andrew Sorensen:** We're not saying that your competitors are cited in that response.

**Andrew Sorensen:** We're saying they show up in that response.

**Andrew Sorensen:** Presence, yeah, that's the number you'd want to compare to that.

**Andrew Sorensen:** then you can see here, and I'm not sure, it keeps moving.

**Andrew Sorensen:** I don't know if you guys saw that, but the number of topics.

**Andrew Sorensen:** Yeah, it keeps, that was my next question.

**Vivek Shankar:** It keeps sort of readjusting.

**Vivek Shankar:** Yeah, and I don't know if we're getting, yeah.

**Andrew Sorensen:** Can you do me a favor?

**Andrew Sorensen:** Instead of where it says by topic, where you're sorting by topic, can you drop that into by seed prompt?

**Andrew Sorensen:** I just want to look at a specific prompt, and I think it'll make more sense if we look at it that way.

**Andrew Sorensen:** Did we just add some prompts?

**Andrew Sorensen:** Is that what these are?

**Andrew Sorensen:** Yeah.

**Andrew Sorensen:** We just don't have very many.

**Andrew Sorensen:** I think we added some research.

**Mara Leighton:** this week, cleared the rest of the prompt, cleared the prompts that we were tracking previously, and then uploaded a new Fathom.

**Andrew Sorensen:** Got Yeah.

**Andrew Sorensen:** That makes sense.

**Andrew Sorensen:** Okay.

**Andrew Sorensen:** So if we just click into, so let me just read this from left to right for you.

**Andrew Sorensen:** So you've got a prompt.

**Andrew Sorensen:** Sorry.

**Andrew Sorensen:** Oh, no, you're good.

**Andrew Sorensen:** We've got a prompt.

**Andrew Sorensen:** And this is a seed prompt right here.

**Andrew Sorensen:** We've got, we're running across all seven platforms.

**Andrew Sorensen:** We've, we've received some responses.

**Andrew Sorensen:** We'll start to get some time data about presence, about over time, how that's going.

**Andrew Sorensen:** But if they're brand new prompts, that's why we're not seeing a, you know, kind of a chart there.

**Andrew Sorensen:** So that makes sense.

**Andrew Sorensen:** Right now, our presence, Galileo's presence is 25% in the responses.

**Andrew Sorensen:** They're being cited 29% of the time.

**Andrew Sorensen:** Vertex.ai is only, they're showing up more frequently across all the responses in here.

**Andrew Sorensen:** Nobody else is showing up.

**Andrew Sorensen:** But again, this is just, that's only saying that they are showing up in the response.

**Andrew Sorensen:** They have presence in the response.

**Andrew Sorensen:** It's not saying they're being cited.

**Andrew Sorensen:** If you do click into that prompt itself, then here is where we can go.

**Andrew Sorensen:** OK, now let's look at this seed.

**Andrew Sorensen:** We're going to look at every single variant of this.

**Andrew Sorensen:** So how are we showing up on ChatGPT?

**Andrew Sorensen:** So if you go down there and see ChatGPT, and let's actually go to where Vertex is showing up.

**Andrew Sorensen:** Let's go to perplexity.

**Andrew Sorensen:** Can you click on the one for perplexity?

**Andrew Sorensen:** Yeah, because Vertex is showing up in there.

**Andrew Sorensen:** And so you'll see here, if you scroll up a little bit higher, sorry, can you, yeah, yeah, there you go.

**Andrew Sorensen:** So this table right here is showing you who's showing up when.

**Andrew Sorensen:** So you can see here, we've got on September 2nd, when we collected the data, you can see this is where Galileo is showing up.

**Andrew Sorensen:** We didn't get any real sentiment information for those two.

**Andrew Sorensen:** And we didn't see any competitors on those first two.

**Andrew Sorensen:** It's just the most recent one from today, where we see, okay, now we're seeing, we do have some positive sentiment for Galileo, which we'd love to see.

**Andrew Sorensen:** But now.

**Andrew Sorensen:** We're seeing, there's more, I think we must have added to the competitor set, and Vertex is showing up in this response.

**Andrew Sorensen:** So now if you scroll down, you'll be able to see, okay, let's find out where are they showing up.

**Andrew Sorensen:** And yeah, you can read through that, and you'll see where Vertex does show up.

**Andrew Sorensen:** But then over on the right, you can see these are all the citations.

**Andrew Sorensen:** So you're asking about citations.

**Andrew Sorensen:** Over here on the right, these are the exact citations that Perplexity used to generate this response.

**Andrew Sorensen:** Okay.

**Andrew Sorensen:** Cool.

**Vivek Shankar:** So just going back to this performance chart.

**Vivek Shankar:** So here's, I guess the question I was asking is like, I was looking at citations, but I should be looking at competitive presence, because that's what this correlates to.

**Vivek Shankar:** So Galileo, 20%, you know, it's kind of showing like Galileo's ahead of the rest.

**Vivek Shankar:** But then I look at this and

**Vivek Shankar:** It says 42%, 67%, like if I just say, let's say, it's like 67, 42, you know, 33, et cetera.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Then you see, I can see it.

**Vivek Shankar:** Yeah, it's like by topic, I think it's a little more sort of clear.

**Vivek Shankar:** Like you can see here, brain trust, like 71, 90, whatever.

**Vivek Shankar:** They're like super numbers.

**Vivek Shankar:** But then here, it's like, you know, brain trust is 13% or lower.

**Vivek Shankar:** So I'm just wondering how it correlates here.

**Andrew Sorensen:** So the competitive presence is just taking across all of your responses.

**Andrew Sorensen:** How often does Galileo show up and how often does everybody else show up?

**Andrew Sorensen:** So I see when you look at, when you're looking at, and maybe, maybe that we need to be more clear about the calculations and stuff like that.

**Andrew Sorensen:** So, you know, here for AI, well, and it keeps changing on me again.

**Andrew Sorensen:** I think it's updating data as we speak, but for AI model debugging and troubleshooting.

**Andrew Sorensen:** Nope.

**Andrew Sorensen:** Nope.

**Andrew Sorensen:** Okay.

**Andrew Sorensen:** can't pick him.

**Andrew Sorensen:** Whatever the one is that's showing up there at the top.

**Andrew Sorensen:** The way that you would read that is for competitors.

**Andrew Sorensen:** It's more based off of the prompts.

**Andrew Sorensen:** So it's just saying across those prompts, they show up.

**Andrew Sorensen:** Then the data up above is across responses.

**Mara Leighton:** So this is, you're saying like for AI agent evaluation, for this general topic, like for all of the prompts that are underneath this topic, this is the aggregate for which competitors are showing up.

**Andrew Sorensen:** Okay.

**Mara Leighton:** And, and then the competitive presence is the, is all of that combined.

**Andrew Sorensen:** It's saying it's taking all of the responses.

**Andrew Sorensen:** So it's, it's, yeah, it's, if I'm looking for true competitive presence across all the responses that we receive, that, that graph is accurate.

**Andrew Sorensen:** That's saying that across every single response, you show up 20% of the time, Vertex shows up 14% of the time that that's, that's accurate across all the responses.

**Andrew Sorensen:** When you aggregate the data here.

**Andrew Sorensen:** And again, we'd love feedback if that's.

**Andrew Sorensen:** If helpful or if that's not the way that you do it, let us know.

**Andrew Sorensen:** But this is just saying in this category across the prompts, this is how often these show up against prompts.

**Andrew Sorensen:** So it's one thing to show up because, again, you're running this across seven different platforms, right?

**Andrew Sorensen:** So you can show up for this calculation, this competitors on the right, you can show up in one of those seven or you can show up in six of those seven.

**Andrew Sorensen:** We're just saying, do you show up across that prompt?

**Andrew Sorensen:** If you show up in any of those seven, we say, yes, check the box.

**Andrew Sorensen:** Yes, we're going to calculate that as they do show up on the prompt.

**Andrew Sorensen:** Whereas, again, on the top left, when you look at competitive presence, we're just saying across all seven, how often do you show up?

**Andrew Sorensen:** And if you only show up one of those seven, that's your competitive presence.

**Andrew Sorensen:** Okay.

**Andrew Sorensen:** Yeah.

**Vivek Shankar:** So my question was really the roll-up, right?

**Vivek Shankar:** So irrespective of this change, if you just look at brain trust, like here's 73, 68, 63, 78, 86, whatever.

**Vivek Shankar:** Everything is like 70% plus, like over here, 100% across all of these.

**Vivek Shankar:** So this should roll up.

**Vivek Shankar:** So if I look at every single category and take the average of these numbers, that's how often brain trust should be showing up, right?

**Vivek Shankar:** And that should correlate.

**Vivek Shankar:** And that's what I was trying to explain.

**Vivek Shankar:** So maybe I didn't explain it very clearly.

**Andrew Sorensen:** So what for the competitors on the right?

**Andrew Sorensen:** Okay.

**Andrew Sorensen:** That's saying, just think of it on the prompt.

**Andrew Sorensen:** So whatever it is for these prompts, they are showing it.

**Andrew Sorensen:** That's how often you'll see them show up on a prompt.

**Andrew Sorensen:** Okay.

**Andrew Sorensen:** But every single prompt, we run across seven platforms.

**Andrew Sorensen:** So we're not saying that brain trust shows up on 86% of the responses.

**Andrew Sorensen:** There's a distinction between prompts versus responses is what I'm trying to say.

**Andrew Sorensen:** So here, and again, it just keeps changing.

**Andrew Sorensen:** So for AI.

**Andrew Sorensen:** Yeah.

**Vivek Shankar:** Can you just explain that a bit?

**Vivek Shankar:** Like prompts versus responses?

**Andrew Sorensen:** Yeah.

**Andrew Sorensen:** here, I'm saying, AI agent reliability, hopefully it doesn't leave me again, but there's 140 prompts in that one.-hmm.

**Andrew Sorensen:** 19.

**Andrew Sorensen:** 25 prompts in that one.

**Andrew Sorensen:** across those prompts, then that's how often they show up, okay?

**Andrew Sorensen:** And that means that if on that prompt, and we're running these across seven different platforms, okay?

**Andrew Sorensen:** But on the prompt, if they show up at least once in those seven, we're saying that they're present in that prompt, okay?

**Mara Leighton:** So this is tracking the prompt rather than the response.

**Mara Leighton:** Yes.

**Mara Leighton:** My question would be, and Vivek, I'm sorry, I hope I'm not like taking us in a different direction.

**Mara Leighton:** Please keep us in the tracks.

**Vivek Shankar:** We answer your question.

**Mara Leighton:** But what's the utility of tracking who shows up in the prompts versus the responses?

**Mara Leighton:** I could be just missing it, but wouldn't we only care about who shows up in the responses or?

**Mara Leighton:** Yes.

**Andrew Sorensen:** We've gotten feedback from both.

**Andrew Sorensen:** We've gotten feedback from customers who do want to see if they show up anywhere.

**Andrew Sorensen:** I want to know that they're showing up and how often they show up on the prompt.

**Andrew Sorensen:** We have a lot of customers that don't distinguish between prompt versus what we call prompt.

**Andrew Sorensen:** Prompt variant, which means overall prompt is the prompt that we submit, but then we submit it to seven different, and we call them prompt variants, we submit it to seven different platforms.

**Andrew Sorensen:** So some of our customers have said, if they show up on any of those responses, I want to know, that's what I want to see there.

**Andrew Sorensen:** Others have said, no, I want to see a true, like, if they're not showing up on six of those platforms, I want to know that as well.

**Andrew Sorensen:** So we're trying to capture both, but it's not a roll-up, so that's what I'm trying to communicate.

**Andrew Sorensen:** If you look at these competitors, it's not a roll-up into the competitive presence.

**Andrew Sorensen:** They're measuring two different things.

**Mara Leighton:** So that's good to know, because I think, and I'm glad you asked that, because I think I was thinking of them as a roll-up as well, just based on the, like, terminology, and then was having trouble, like, squaring the high percentages for competitors versus, like, Galileo being the, getting, having a positive, or the most positive presence.

**Mara Leighton:** But Vivek, did that answer your question?

**Mara Leighton:** Sorry to jump in.

**Vivek Shankar:** Vivek, just...

**Vivek Shankar:** just want to double click on it.

**Vivek Shankar:** I'm still not clear.

**Vivek Shankar:** So when you say showing up for a prompt, what does that mean?

**Vivek Shankar:** So I have a prompt here.

**Vivek Shankar:** When you say Arise is showing up 67% of the time for this prompt, you're not saying that Arise is, okay, here we go.

**Vivek Shankar:** So you see here?

**Vivek Shankar:** So look at this.

**Andrew Sorensen:** What we're saying is on that, in this case, it's only ChatGPT.

**Andrew Sorensen:** For ChatGPT, if you look there, it shows up 67%.

**Andrew Sorensen:** So go back to the last screen.

**Andrew Sorensen:** Right here, it says Arise 67%.

**Andrew Sorensen:** Right there, you'll see it says Arise 67%.

**Andrew Sorensen:** So we're saying that across the prompt, then that's what we're saying.

**Andrew Sorensen:** But if you go into every, click back into that prompt, look at every single variant.

**Andrew Sorensen:** They don't show up on every single variant of this.

**Andrew Sorensen:** So if you take, and using this, we've got 21 responses here, it looks like.

**Andrew Sorensen:** Arise to go.

**Andrew Sorensen:** Going to the competitive presence, Kay, here, this will make it really easy for the math.

**Andrew Sorensen:** So here we know they're 67%.

**Andrew Sorensen:** So they show up in two of the three responses on ChatGPT, right?

**Vivek Shankar:** That's the 67%, two out of three.

**Vivek Shankar:** So they show up two out of three times on ChatGPT.

**Andrew Sorensen:** But if you, again, scroll down here, you see we've collected 21 responses.

**Andrew Sorensen:** They don't show up anywhere else.

**Andrew Sorensen:** So across all of these, they show up twice out of 21.

**Andrew Sorensen:** That's how, when you go to the competitive presence, you see 10%.

**Andrew Sorensen:** It's the two.

**Andrew Sorensen:** Does that make sense?

**Andrew Sorensen:** And again, if that doesn't, like, I understand exactly what you guys are saying, that it's not intuitive.

**Andrew Sorensen:** Like, it would be helpful to see those high out.

**Andrew Sorensen:** So let me, that's great feedback.

**Andrew Sorensen:** And I can share that with our team that, hey, maybe we want to rethink this.

**Andrew Sorensen:** But we've gotten feedback from other customers that they like the way that it shows up here because they can see prompt by prompt and they want to know, you know, is, you know, what's, anyways.

**Andrew Sorensen:** I think I, yeah.

**Vivek Shankar:** Sorry.

**Vivek Shankar:** So if I understand this correctly, when you say that this is for prompt, what you're saying is this is for a platform, really.

**Vivek Shankar:** That's a great, that's a good way to think about it.

**Vivek Shankar:** It's a platform.

**Andrew Sorensen:** Okay.

**Andrew Sorensen:** Okay.

**Andrew Sorensen:** That makes more sense to me.

**Andrew Sorensen:** Yeah.

**Andrew Sorensen:** Okay.

**Andrew Sorensen:** Good deal.

**Andrew Sorensen:** Okay.

**Andrew Sorensen:** Cool.

**Vivek Shankar:** And yeah, I think, yeah, personally, I don't know if, yeah, I don't know about the utility of this because I don't know any customer who says like, oh, we want to show up on chat GPT more than perplexity or something like that.

**Vivek Shankar:** So, yeah, I don't know.

**Vivek Shankar:** Maybe there's a different.

**Andrew Sorensen:** Real quick because like, and I don't know, again, volumes for all of my other customers, chat GPT is probably 80% plus of their volume of the referral traffic or the bot traffic that's hitting their site.

**Andrew Sorensen:** Chat GPT is about 80% of the overall traffic.

**Andrew Sorensen:** Perplexity is next, but it's a significantly smaller amount.

**Andrew Sorensen:** And then it's usually AI overviews.

**Andrew Sorensen:** I haven't seen our internal data about Gemini or AI.

**Andrew Sorensen:** I'm...

**Andrew Sorensen:** We just barely rolled them out.

**Andrew Sorensen:** we don't have the data sets yet, but so yeah, let me know.

**Andrew Sorensen:** That's really helpful feedback as well.

**Andrew Sorensen:** And I'll share that with our CTO for you.

**Andrew Sorensen:** Oh, sorry, go ahead.

**Andrew Sorensen:** If have a question, go ahead.

**Vivek Shankar:** No, I was just brainstorming here instead of 67%, since it's per platform, since the, I guess the intention is to communicate, the real value is to, as you said, like letting us know which platforms we're showing up on.

**Vivek Shankar:** So maybe replace the 67% with the logo of the, of where we're showing up.

**Vivek Shankar:** At GBT?

**Vivek Shankar:** Yeah, yeah.

**Vivek Shankar:** No, that's a great call.

**Vivek Shankar:** All of these logos here, you know, like, cause that'll tell us like, okay, we're showing up, but, yeah.

**Mara Leighton:** I think too, even for our, in our experience of showing this to clients, I think that will make it a little bit more intuitive also just for someone who's even further removed, because if we screen share this, they're going to think that, you know, The numbers don't tie out, what's going on?

**Mara Leighton:** Yeah, I think that they're like massively under-

**Mara Leighton:** performing for some of these prompts if they're seeing a competitor at 67% versus, yeah, I think a logo is a great idea of, like, us being able to really quickly indicate, like, that's just, they're showing up for this platform, XYZ.

**Andrew Sorensen:** Okay, that's great.

**Andrew Sorensen:** That's great feedback.

**Andrew Sorensen:** Thank you for that.

**Vivek Shankar:** Cool.

**Vivek Shankar:** So, just real quick.

**Vivek Shankar:** Okay.

**Vivek Shankar:** So, I'm in the context tab now, and I just want to check, these key topics, right, let's say I come in here and I change this, because I changed this yesterday.

**Vivek Shankar:** Okay.

**Vivek Shankar:** Is that, and I noticed, like, the prompts kind of rearrange themselves within these.

**Vivek Shankar:** Does that affect, how, what are some of the side effects of that?

**Andrew Sorensen:** Yeah, so, real quick, because I thought, and Mara, correct me if I'm wrong.

**Andrew Sorensen:** I thought, did we just upload prompts or did we use the CSV file to upload the prompts?

**Andrew Sorensen:** We used the CSV file.

**Andrew Sorensen:** In that CSV file, did we assign key topics to prompts?

**Andrew Sorensen:** I believe so.

**Andrew Sorensen:** think that we did.

**Andrew Sorensen:** Yeah.

**Andrew Sorensen:** This would have happened after the CSV.

**Mara Leighton:** So we would have uploaded the CSV with those appropriate tags.

**Mara Leighton:** then Vivek, it sounds like you adjusted the key topics.

**Mara Leighton:** So that would have been like the chronological.

**Mara Leighton:** Okay.

**Andrew Sorensen:** So, so two things here, and this is how the system works.

**Andrew Sorensen:** Typically, when we upload a CSV file, then there is a category, there is a column there for key topics and we can assign the key topics.

**Andrew Sorensen:** That overrides the general way the platform functions.

**Andrew Sorensen:** Normally, if you just upload a prompt by itself and you don't specify the key topic, then our system on the backend goes and looks at it and tries to determine the intent.

**Andrew Sorensen:** And based off of the intent, the language of that looking at we're

**Andrew Sorensen:** prompt, it'll try to assign it into one of those different key topics.

**Andrew Sorensen:** So if it shouldn't change, like, again, the way that the logic works, the programming logic, is if we have a CSV file, that takes precedence above all else.

**Andrew Sorensen:** So let me know if you're, it should be rearranging, it should just follow exactly what we put in the CSV file.

**Andrew Sorensen:** Yeah, it seems largely fine.

**Vivek Shankar:** Like, I kind of, I added a bunch of new ones.

**Andrew Sorensen:** Yeah, if we change the other ones here, then the prompts that we have in the system right now shouldn't, and tell me if you see differently, but it shouldn't, like, anything that you added should be zero.

**Andrew Sorensen:** Like, it shouldn't have any prompts going to it, because they weren't specified in the original CSV file.

**Andrew Sorensen:** Does that make sense?

**Vivek Shankar:** And that's, I I think they do have, because, yeah, because I remember, like, yeah.

**Vivek Shankar:** Okay, it's changing on me, but LLM Reliability, LLM.

**Vivek Shankar:** Those are the ones you added?

**Andrew Sorensen:** I added a bunch of them.

**Vivek Shankar:** Like I added all of these, like AI Governance, for example, I added it yesterday.

**Vivek Shankar:** wasn't present before.

**Vivek Shankar:** And it has like 1,800 prompts.

**Vivek Shankar:** that was post-CSV file upload?

**Andrew Sorensen:** Post-CSV, yes.

**Andrew Sorensen:** Okay.

**Andrew Sorensen:** That's the way I've been told.

**Andrew Sorensen:** That's not the way it's supposed to work.

**Andrew Sorensen:** I'll go confirm that with my engineering team.

**Andrew Sorensen:** Because again, the way that it was explained to me was once we put up the CSV, that is the source of truth.

**Andrew Sorensen:** We override everything else.

**Andrew Sorensen:** So I will go ask them about that.

**Vivek Shankar:** just to sort of give you the full context on what I did, I actually deleted some of those CSV categories and I added these new ones.

**Vivek Shankar:** So maybe that's why the recategorizations happened, which is fine.

**Andrew Sorensen:** It's not an issue for us.

**Andrew Sorensen:** Yeah, no, I just want to know that because that's not the way it was explained to me how it works.

**Andrew Sorensen:** that?

**Andrew Sorensen:** Yeah.

**Andrew Sorensen:** Okay, good.

**Andrew Sorensen:** Thank you for letting me

**Mara Leighton:** While we're here, I think this relates to my question at the beginning of the seeing that really high number of prompts.

**Mara Leighton:** It's not something that I'm seeing across the other dashboards that we have.

**Mara Leighton:** If we're tracking typically like 200 or so prompts, typically like if I'm looking at like Prophecy or some of our other clients, those numbers are more like 20 prompts or 30 prompts versus like.

**Mara Leighton:** So I'm concerned that it's I don't know if this is feasible, but if it's still tracking the prompts that we've put in in the past and then deleted, Vivek, if you want to go to a different client's dashboard.

**Mara Leighton:** I can just show you right here.

**Andrew Sorensen:** So I see 244 rows at the bottom left.

**Andrew Sorensen:** I'm seeing 244 rows.

**Andrew Sorensen:** So that means we're filtering by seed prompt right now.

**Andrew Sorensen:** So 244 times seven should be.

**Andrew Sorensen:** Yeah, it's 1708.

**Vivek Shankar:** It should be that.

**Vivek Shankar:** All right.

**Vivek Shankar:** I don't know why it's so much lower.

**Mara Leighton:** Yeah, can we pull the different, can we pull the different, because I.

**Andrew Sorensen:** know you guys have lots of brands.

**Andrew Sorensen:** Do we want to pull up another brand and look at that?

**Mara Leighton:** So if you go to like, actually, Vivek, do you want to go to 123?

**Andrew Sorensen:** But if you look at the platforms, it's only one platform.

**Andrew Sorensen:** It's only ChatGPT.

**Andrew Sorensen:** Yeah, maybe go to, let me see.

**Mara Leighton:** It's loading.

**Mara Leighton:** Webflow has four.

**Vivek Shankar:** Four, 148 prompts.

**Andrew Sorensen:** But if you go down for that one, oh.

**Andrew Sorensen:** Yeah, change that.

**Andrew Sorensen:** Instead of the sort by topic, can you sort by seed prompt?

**Andrew Sorensen:** Yeah, and then let's scroll down.

**Andrew Sorensen:** So 74 prompts here, 74 seed prompts across four platforms, right?

**Andrew Sorensen:** Well, it says there's two variants, so I'm guessing it's only tracking.

**Vivek Shankar:** Oh, so it's only two platforms.

**Vivek Shankar:** I think, yeah, because the, if I remember, Mara, the Galileo sheet we sent.

**Vivek Shankar:** Yeah, 200, 300 rules or something.

**Mara Leighton:** It would have been probably like, I think around 230, if I'm remembering correctly.

**Mara Leighton:** So that makes sense.

**Mara Leighton:** It's just that that number seems so far off from some of the other dashboards.

**Mara Leighton:** But that makes sense if it's we're tracking across six or seven.

**Mara Leighton:** And then, yeah, so that makes sense to me.

**Mara Leighton:** It's just like I wasn't seeing it for any of the other dashboards.

**Mara Leighton:** Like, for exec, the prompts number is just 240.

**Mara Leighton:** And then we're doing, let's see, five LLMs.

**Mara Leighton:** And, yeah, if you want to go to.

**Mara Leighton:** So anyway, it was more like, so if someone's asking, like, why is this number so high?

**Mara Leighton:** I can just respond in a way that makes sense.

**Mara Leighton:** But, yeah, so this is what we're asking.

**Andrew Sorensen:** Responses by platforms.

**Andrew Sorensen:** Yeah.

**Andrew Sorensen:** Yeah.

**Andrew Sorensen:** Yep.

**Andrew Sorensen:** Okay.

**Mara Leighton:** Okay.

**Vivek Shankar:** All right.

**Vivek Shankar:** Sorry, we're almost at time.

**Vivek Shankar:** I'll try to get to my questions quickly.

**Vivek Shankar:** Potentially loaded question here.

**Vivek Shankar:** So on these prompts, right?

**Vivek Shankar:** So the variants are essentially variants.

**Vivek Shankar:** It's taking the same prompt across different platforms.

**Vivek Shankar:** I'm wondering when we design prompts, right?

**Vivek Shankar:** So it says here, for example, AI roleplay software that pulls from whatever, workday employee data, right?

**Vivek Shankar:** This is a very long tail, very specific thing.

**Vivek Shankar:** Should I be including broad match queries in here as well?

**Vivek Shankar:** Something like best AI roleplay software versus, or, you know, and another prompt would be best AI roleplay software for startup companies using workday.

**Vivek Shankar:** Are those two separate prompts?

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Or, okay, so I do need to include my broad match.

**Andrew Sorensen:** There is, just to be clear, and every platform works a little bit differently.

**Andrew Sorensen:** But let me show you specifically for chat GPT.

**Andrew Sorensen:** If you go to the end.

**Andrew Sorensen:** Insights tab, over on the left there, click on that, and then, well, we only have one, but competitive presence, hit that review now, and then hit optimize.

**Andrew Sorensen:** What this is, is this is, just so you guys may already know this, this is prompts where competitors show up, but Galileo does not, or whoever this is does not, okay?

**Andrew Sorensen:** So this is very helpful, but if you go to the top, you'll see the prompt where it says search query right below that.

**Andrew Sorensen:** That is how, that is how ChatGPT has condensed that prompt for it to submit it to its indexer.

**Andrew Sorensen:** In this case, it's almost identical.

**Andrew Sorensen:** Most of the time, you will see it condensed into a shorter search query, but this kind of gives you an idea of, like, you thematically, if you have a little bit of a difference, it will pick that up.

**Andrew Sorensen:** But, like, I have some, some clients that will do the slightest variations of.

**Andrew Sorensen:** This prompt, and the search query is the same.

**Andrew Sorensen:** So just something to keep in mind is that they do take the long tail prompt, but in almost all cases across the platforms, they do still condense it to some version of a search query.

**Mara Leighton:** That's the thing that I have the most questions about, because it seems like if we're really like drilling down into particular use cases pain points, sometimes if we're seeing that that prompt, which is highly specific and highly individualized, if it's getting like kind of crunched down into a really succinct search query that's like best CMS for XYZ, like what's, is there still a point in creating all of those different long tail versions?

**Mara Leighton:** And also is, do we need to, could we just be doing best CMS for XYZ as the prompt if that's how it's actually going to show up on the back end anyway?

**Mara Leighton:** Does that question make sense?

**Mara Leighton:** It totally does.

**Andrew Sorensen:** The only thing I haven't, and I look at these all day long.

**Andrew Sorensen:** I'm in with clients talking and looking at these all day long.

**Andrew Sorensen:** I can't figure out the pattern.

**Andrew Sorensen:** There's just times when, and this is just ChatGPT, there's times when the search query makes perfect sense.

**Andrew Sorensen:** But like this one, I would have thought this would have got condensed more.

**Andrew Sorensen:** Yeah, I'm kind of surprised.

**Andrew Sorensen:** Yeah.

**Andrew Sorensen:** Yeah.

**Andrew Sorensen:** So like, that's the thing.

**Andrew Sorensen:** I can't figure out the pattern yet.

**Andrew Sorensen:** And I look at these all day long.

**Andrew Sorensen:** So that's why I recommend to my clients, use the different variants, but like, don't get like too, like, you don't have to get super, super crazy granular.

**Andrew Sorensen:** But like, as opposed to like, help real estate agents practice objection handling with purchasers, you're not going to get a different, like, it's going to be about the same thing.

**Andrew Sorensen:** So I try to, I think there's a balance there.

**Andrew Sorensen:** do think that, again, until we get better insights directly from the platforms about how they operate, how they are doing this, we still have to keep playing with it and figuring out that.

**Andrew Sorensen:** Because, again, I can't figure out what the patterns are.

**Andrew Sorensen:** It just seems to be not random, but it just seems to be, again, like I said, it's.

**Andrew Sorensen:** I can't figure out what, why, I can't, I can't give you with 100% certainty of what that level is of where you're like, okay, now you don't have to go any further.

**Andrew Sorensen:** Now you can just leave it at this.

**Andrew Sorensen:** So I recommend continuing to do that until we start to figure out more of the patterns and we get more guidance from the platforms.

**Andrew Sorensen:** Yeah.

**Andrew Sorensen:** Okay.

**Mara Leighton:** I have more questions that I'm sure you do as well, but I know that we're at time.

**Mara Leighton:** Would it be helpful?

**Mara Leighton:** Should we just like book and Andrew, thank you for being so generous with your time.

**Mara Leighton:** We'll try and like really efficient with it and circulate this to the rest of the teams.

**Mara Leighton:** So that, you know, their questions get answered as well, but should we just not abuse your Calendly, but maybe book some more time next week for the access questions?

**Mara Leighton:** I'm assuming you probably have a busy day and like have other things to get to.

**Mara Leighton:** Yeah, no, please do.

**Mara Leighton:** I do have a meeting right now.

**Andrew Sorensen:** got to bounce to, but please like you just use my Calendly.

**Andrew Sorensen:** mean, that's what it's for.

**Andrew Sorensen:** You guys are, I know, you know this, you're a super important client for us.

**Andrew Sorensen:** So I want to make sure that we're answering your questions and supporting you and helping.

**Andrew Sorensen:** The only question that I had before we, before we jump is.

**Andrew Sorensen:** Do you know, are you guys linked into our API?

**Andrew Sorensen:** I don't know.

**Andrew Sorensen:** Okay.

**Andrew Sorensen:** I don't think we are.

**Andrew Sorensen:** Yeah, I would imagine not.

**Andrew Sorensen:** As an agency, you have access to it.

**Andrew Sorensen:** Like, it's not an add-on.

**Andrew Sorensen:** It's not an additional cost at all.

**Andrew Sorensen:** And I don't know if you have additional BI tools internally that you're using in support of clients and stuff like that.

**Andrew Sorensen:** But two things.

**Andrew Sorensen:** So if we don't, we can definitely talk about getting you guys hooked up with the API.

**Andrew Sorensen:** If you have a tool internally that you use, if that's helpful for when you're talking with clients.

**Andrew Sorensen:** The second thing is, I just had a guy on my team create a looker studio that is surfacing a lot of client information that I think is cool.

**Andrew Sorensen:** So I'd like to, if you have time next week, I would love to, if you set up time on my calendar, I'd like to bring him on too.

**Andrew Sorensen:** And I'd like to show you what he's working on from a visualization and surfacing data for clients that might be helpful as well.

**Andrew Sorensen:** That would be helpful.

**Andrew Sorensen:** think the visualization element in terms of.

**Mara Leighton:** Like, client relations is always the most important part of just, like, how do we communicate this quickly, positively?

**Mara Leighton:** Yeah.

**Mara Leighton:** Yeah.

**Andrew Sorensen:** And just candidly, like, report the, we don't have a robust reporting feature on the platform right now.

**Andrew Sorensen:** We know that we're working on it, but that's the reality of it.

**Andrew Sorensen:** This, I think, helps to bridge the gap a little bit.

**Andrew Sorensen:** Okay, cool.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** So, yeah, I'll add Will, and we'll share that with you.

**Andrew Sorensen:** Great.

**Vivek Shankar:** Yep.

**Vivek Shankar:** Cool.

**Vivek Shankar:** I'm sorry, does the API go into Looker directly?

**Vivek Shankar:** that's what we use.

**Vivek Shankar:** It can.

**Andrew Sorensen:** Yeah, if you're using Looker, it does, yeah.

**Andrew Sorensen:** Yeah, okay.

**Andrew Sorensen:** Great.

**Andrew Sorensen:** That would be super helpful, yeah.

**Andrew Sorensen:** Yeah, let's talk about that next week.

**Andrew Sorensen:** Okay, thank you both.

**Andrew Sorensen:** Have a good week.

**Andrew Sorensen:** Thank you, you too.

**Andrew Sorensen:** Bye-bye.

**Andrew Sorensen:** Bye-bye.
