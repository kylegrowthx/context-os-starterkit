# Datagrid <> GrowthX - Weekly Sync

<metadata>
date: 2025-11-06
time: 20:00 UTC
duration: 43 minutes
organizer: mara@growthx.ai
participants: Mara Leighton, Vivek Shankar, Nika Narimanidze, Kaitlin Quimby, Miles Gordenker, Renato Ferro, Thiago da Costa
fathom_recording_id: 99852113
fathom_url: https://fathom.video/calls/465157226
share_url: https://fathom.video/share/FSVL1seV2zPsFftyqy5mtJeqPLbk6hQy
source: fathom
enriched_on: 2026-03-02 15:30 UTC
</metadata>

---

## Summary

GrowthX (Mara and Vivek's team) met with Miles Gordenker and Kaitlin Quimby from Datagrid to align on Datagrid's product messaging for marketing and sales. Miles demoed key Datagrid capabilities including hallucination-resistant citations, image processing for construction drawings, and video analysis—all positioning Datagrid as a tool for heavy industry, not cost optimization. The team identified three core personas: heavy industry users, product managers (integrated with Notion), and agent designers building white-label solutions. Key decisions included emphasizing quality and accuracy over token cost savings, and framing agent building as a skill for experienced managers (e.g., the 50-something welder who cut project evaluation from 3 days to 4 hours). Kaitlin will send the newsletter draft and update the welder customer story with more backstory for thought leadership.

---

## Context

GrowthX is working with Datagrid, an AI platform that builds agents for heavy industry and complex workflows. Datagrid has been operating for five years and recently pivoted from a pure data pipeline company to offering agent design and deployment tools. This meeting was part of ongoing marketing and sales alignment between GrowthX (which provides content marketing and B2B visibility services) and Datagrid. Mara Leighton and Vivek Shankar represent GrowthX's side; Kaitlin Quimby leads marketing at Datagrid (toric.com domain, which appears to be Datagrid's holding company), and Miles Gordenker is a product expert who handles most demos and customer conversations.

---

## Relevance

- **To GrowthX Delivery:** GrowthX is positioning content around Datagrid's adoption strategy and key differentiators. Focus areas: heavy industry targeting, hallucination resistance metrics (60% faster verification), human-in-the-loop preview features, and SOC2/FedRAMP compliance messaging. The welder story represents compelling thought leadership around democratizing agent building for experienced managers.

- **To GrowthX Business Development:** Datagrid is a strategic content marketing client aligned on three ICP segments (heavy industry, product managers, agent designers). The partnership directly supports a content narrative around AI adoption, security-first positioning, and use-case-specific value props—all areas where GrowthX's visibility and narrative work creates competitive advantage.

- **To CheckThat:** Datagrid's emphasis on hallucination resistance and verification efficiency via in-context citations relates to content quality and AI-generated content reliability—areas where CheckThat's visibility index provides differentiated insight for their customers.

---

## Overview

- **Target Heavy Industry:** Datagrid's core value is handling massive, complex datasets (e.g., construction drawings) that general-purpose AI tools "choke on."
- **Focus on Quality, Not Cost:** The value proposition is superior accuracy and sophisticated task completion, not lower token costs.
- **Highlight Verification:** Datagrid's in-context citations cut answer verification time by \~60% (e.g., 5 mins to 2 mins vs. Perplexity).
- **Empower Experts:** The key adoption strategy is enabling experienced managers, not just young tech graduates, to build agents.

---

## Key Topics

### Core Value Proposition: Heavy Industry

  - Datagrid's strength is processing large, complex datasets that general-purpose AI tools cannot handle.
  - **Hallucination Resistance:** In-context citations link directly to source data, enabling rapid verification.
      - **Metric:** Verification time cut by \~60% (e.g., 5 mins to 2 mins vs. Perplexity).
  - **Advanced Data Handling:**
      - **Image Processing:** Custom visual language models (VLMs) enable detailed analysis of complex diagrams (e.g., comparing construction drawing revisions).
      - **Video Analysis:** Extracts actions and details from job site videos for automated action.

### Product Manager (PM) Use Case

  - **Software Focus:** Currently integrates with Notion, not Jira.
  - **Value Prop:** Delivers better, more detailed outputs than a time-constrained PM could write manually.
  - **Workflow Automation:** Enables chained actions (e.g., Notion ticket → Slack notification) to eliminate context switching.
  - **Personalization:** Agents learn user preferences for ticket formatting, with user control to delete memories.

### Agent Designer Value Proposition

  - **Problem:** Building agents from scratch is slow due to the need to build data ingestion, enrichment, and tool frameworks.
  - **Solution:** Datagrid provides a 5-year-old data pipeline foundation and a library of pre-built tools, cutting years off development.
  - **Open API:** Allows full white-labeling and custom tool development, giving technical users control.

### Agent Evaluation & Quality Control

  - **Process:** Combines human review with "LLM as a judge."
      - **LLM as a judge:** An LLM compares agent outputs against a suite of \>1,000 industry-specific test cases to ensure quality at scale.
  - **Real-time Monitoring:** Agents self-score their performance after each action.
  - **Self-Correction:** Agents remember successful steps to improve speed on future runs.

### Key Differentiators & Messaging

  - **Human-in-the-Loop:** Shows a preview of agent actions before they are executed in connected systems, building trust and preventing errors.
  - **Security:** SOC2 compliant, working toward FedRAMP.
  - **Adoption Strategy:** Frame agent building as a skill for experienced managers, not just young tech graduates.
      - **Example:** A 50-something welder built an agent that cut project spec evaluation from 3 days to 4 hours.

---

## Action Items

**Kaitlin Quimby (Datagrid)**
- Email Mara with newsletter draft, deck/video status (cc Thiago da Costa), welder story update with more backstory, and benchmark stats

---

## Transcript
**Mara Leighton:** Hey, how's it going?

**Mara Leighton:** Oh, I just love the look today.

**Mara Leighton:** I think you're on mute, but like, but I get the vibe.

**Kaitlin Quimby:** I am on mute.

**Mara Leighton:** Thank you.

**Kaitlin Quimby:** No, just washed it and actually did it today.

**Mara Leighton:** Wonder.

**Kaitlin Quimby:** Yeah, it's like, people are like, oh, you know, and they're like, oh, it's like, is it freshly dyed?

**Mara Leighton:** Is this that?

**Mara Leighton:** It's like, wash and actually styling it.

**Mara Leighton:** Yeah.

**Mara Leighton:** Also, do you always have the glasses on?

**Kaitlin Quimby:** Maybe it's just like all of the match, but.

**Kaitlin Quimby:** Yeah, it does all match day, but I have been wearing them more.

**Kaitlin Quimby:** They're fairly new.

**Kaitlin Quimby:** So yeah, it's just trying to protect the eyeballs.

**Mara Leighton:** Totally.

**Mara Leighton:** I need a pair, prescription pair for the first time ever.

**Mara Leighton:** And I've just been prioritized doing it, but eyes are so tired at the end of the day.

**Kaitlin Quimby:** These are blue light ones because I was noticing.

**Kaitlin Quimby:** And like, it was just like, my eyes are draining.

**Mara Leighton:** Hi, Miles.

**Mara Leighton:** Hey, Miles.

**Mara Leighton:** Howdy.

**Mara Leighton:** How are you?

**Miles Gordenker:** Doing all right.

**Miles Gordenker:** I'm having a super busy day.

**Mara Leighton:** So if I seem a little cranky, it's me, not you.

**Mara Leighton:** Oh, totally.

**Kaitlin Quimby:** I get it.

**Kaitlin Quimby:** Well, I know I want to be conscious of your time, Miles.

**Kaitlin Quimby:** We want to do the product, like overview and demo stuff first, and then we can go into like any updates after.

**Kaitlin Quimby:** then Miles doesn't have to stay for the whole call.

**Mara Leighton:** Yeah, that'd be great.

**Kaitlin Quimby:** Okay.

**Kaitlin Quimby:** And help me contextualize this.

**Kaitlin Quimby:** Who are we advertising to?

**Miles Gordenker:** What prompted this demo?

**Miles Gordenker:** Any like particular personas that we're interested in or limitations?

**Mara Leighton:** What's the format?

**Mara Leighton:** Yeah.

**Mara Leighton:** Do you want me to jump in there?

**Mara Leighton:** Yeah.

**Mara Leighton:** I have some particular questions from the team.

**Mara Leighton:** This originated just so that we can talk about the most updated version of the DataGrid product accurately.

**Mara Leighton:** I'm dropping some questions from the team in the chat.

**Mara Leighton:** dropping some team.

**Mara Leighton:** team.

**Mara Leighton:** team.

**Mara Leighton:** might help structure it a little bit.

**Mara Leighton:** Vivek couldn't be here today because he's having surgery, so I am stepping in instead.

**Mara Leighton:** But typically, we are looking for how do you evaluate your agent's outputs?

**Mara Leighton:** What advantages would an AI agent designer receive by working with Datagrid instead of building this from scratch?

**Mara Leighton:** What specific features should we highlight when talking about Datagrid's agents that will instantly hook, like a product manager, for instance?

**Mara Leighton:** So that could be kind of the ICP that we chat through.

**Mara Leighton:** And then any technical examples of customization that is possible.

**Mara Leighton:** And then generally, how does Datagrid optimize agent running costs, token usage, et cetera, any of those other related cost savings.

**Miles Gordenker:** Okay, sounds good.

**Miles Gordenker:** Do you have that in written form as well?

**Mara Leighton:** So, yeah, I just dropped it into the, oh, you know what?

**Mara Leighton:** I dropped it into the note taker versus the.

**Mara Leighton:** Shared group chat, so I'll drop it right now.

**Mara Leighton:** And I'll also hit record just so we have a backup.

**Mara Leighton:** That looks like...

**Mara Leighton:** Is that sufficient, Miles?

**Miles Gordenker:** I just haven't gotten the write-up yet, but I was going to run through each of those in turn.

**Mara Leighton:** Yeah, totally.

**Mara Leighton:** I just dropped it into the group chat on Zoom.

**Miles Gordenker:** Oh, weird.

**Miles Gordenker:** Oh, I see.

**Miles Gordenker:** I was on...

**Miles Gordenker:** I see how you did that.

**Mara Leighton:** I was also on the chat with me.

**Mara Leighton:** Sorry that.

**Mara Leighton:** Yeah.

**Miles Gordenker:** I'm glad I asked.

**Miles Gordenker:** I wasn't sure.

**Mara Leighton:** that's not your fault.

**Mara Leighton:** Yeah, those are the questions.

**Mara Leighton:** But typically, like, if you're whatever your general demo might be, and then these would just be the particular areas of interest for like a product manager, for instance, or cost savings, any other kind of like points of differentiation that we can point out.

**Miles Gordenker:** Okay.

**Miles Gordenker:** I didn't know we were targeting product managers.

**Mara Leighton:** Is that new?

**Mara Leighton:** Yeah.

**Mara Leighton:** I mean, relatively new.

**Mara Leighton:** But yeah.

**Miles Gordenker:** Okay.

**Miles Gordenker:** Cool.

**Miles Gordenker:** So I think where we've landed with product managers right now is the key thing where the key like software we're supporting for them is Notion.

**Miles Gordenker:** I don't think we support like Jira or a lot of those other ones.

**Miles Gordenker:** So that'll limit the market that we can go to.

**Miles Gordenker:** And I'm not sure how granular your targeting can get.

**Miles Gordenker:** But folks who use Notion are definitely ideal for this.

**Miles Gordenker:** I'm going to spin up another browser as well.

**Miles Gordenker:** I was expecting to do a construction-related demo, so I'm in the wrong account right now.

**Mara Leighton:** Perfect.

**Mara Leighton:** Whatever your most typical version of this looks like will also be useful to us.

**Mara Leighton:** So, yeah, feel free to do your standard one, and we can follow up with any particular questions.

**Miles Gordenker:** Yeah, I think we'll have much better luck in general with heavy industry.

**Miles Gordenker:** So that's like any kind of industry where they're using a ton of documents.

**Miles Gordenker:** And I think what you can do here is just draw the contrast between ChatGPT and general-purpose tools and Datagrid.

**Miles Gordenker:** Like, they're going to – a general-purpose tool is going to, like, choke on the amount of data that they have to deal with.

**Miles Gordenker:** So, things like –

**Miles Gordenker:** A good one to highlight is the hallucination resistance in citations, because we'll back up, you know, where this information came from with links back to the specific part of the data set so people can verify quickly.

**Miles Gordenker:** So I made, like, a LinkedIn post on this quite some time ago, but we did, like, a comparison between, like, how long it takes to verify an answer in Datagrid and how long it takes to verify an answer in, like, the standard ones, like perplexity.

**Miles Gordenker:** And all those.

**Miles Gordenker:** And, like, it's way faster in Datagrid, because, like, in the other softwares, when you click on one of these, it takes you to, like, directly to that website.

**Miles Gordenker:** But for us, we're popping it directly within context.

**Miles Gordenker:** So there's way less back and forth that has to happen.

**Miles Gordenker:** And that's been, like, a pain point that's kind of resonated with people quite a bit.

**Mara Leighton:** And what was the difference in, sorry if I'm just not noticing it, but what was the difference in time?

**Mara Leighton:** Or the.

**Mara Leighton:** Or the time savings between like a perplexity versus Datagrid?

**Miles Gordenker:** Like, you'd have to go like into the LinkedIn post I did.

**Miles Gordenker:** I don't have it off the top of my head.

**Miles Gordenker:** But I believe it was like two minutes versus five minutes.

**Mara Leighton:** Okay, cool.

**Miles Gordenker:** Okay.

**Miles Gordenker:** So specifically, another use case that's like very compelling to construction, a lot of these other ones, are just the idea of comparing revisions.

**Miles Gordenker:** Because we aren't using just like a vanilla model to do the image processing, we can handle like the detail on that a lot better.

**Miles Gordenker:** So this is a nice example of like, hey, compare these two drawing divisions and like...

**Miles Gordenker:** We can talk through, like, okay, it's seen as frequent updates.

**Miles Gordenker:** Like, here's the isCurrent one.

**Miles Gordenker:** This one wasn't a great example because it's been a while since I revisited this.

**Miles Gordenker:** But we can definitely, like, get you some good examples of us doing really detailed comparisons of drawings that other software would probably choke on because it looks like this and it's really complicated.

**Mara Leighton:** it does.

**Miles Gordenker:** I think another angle you can take is just around, like, the human in the loop element of all of this.

**Miles Gordenker:** So I'll back up and, like, go to some of the other stuff now.

**Miles Gordenker:** I think it's just easier for me to pull the slides for this.

**Mara Leighton:** I think it's just...

**Miles Gordenker:** Okay.

**Miles Gordenker:** So this one resonates a lot, speaking about how, hey, look, you can use the agents from anywhere, you can get the work done from your phone, people don't want to install yet another app, and we're still implementing the same kind of hallucination resistance within here.

**Miles Gordenker:** In this case, we deeply understood this diagram, and then we're also sending it back to the user's phone so they can verify.

**Miles Gordenker:** So that get work done on a go angle has been resonating quite well as well.

**Mara Leighton:** Yeah, I would imagine so.

**Mara Leighton:** And then, sorry if you already mentioned this, but do people typically ask follow-up questions about that, like how it actually works technically?

**Miles Gordenker:** Yeah, and then we tell them that we use a visual language model that's tuned for this type of task rather than like, yeah.

**Miles Gordenker:** Rather than, like, you know, one of the big ones, like ChatGPT, Gemini, et cetera.

**Miles Gordenker:** Video type stuff also resonates quite well in this one.

**Miles Gordenker:** Can you hear the sound, by the way?

**Mara Leighton:** I can't.

**Mara Leighton:** Okay.

**Mara Leighton:** Also, if you're able to share this with us, we can use the whole deck if that's something you'd be able to...

**Miles Gordenker:** I think that's a Tiago question.

**Miles Gordenker:** Okay.

**Mara Leighton:** Because I don't know whether this customer is given consent.

**Miles Gordenker:** Okay.

**Miles Gordenker:** But in it, he's talking through, like, you know, the guy is talking in, like, a really thick Southern accent.

**Miles Gordenker:** He's showing a video of something happening on the job site.

**Miles Gordenker:** And then Datagrid is going ahead and extracting everything from that video and taking action for him.

**Mara Leighton:** So that's a nice one as well.

**Miles Gordenker:** Thank Thank

**Miles Gordenker:** Okay.

**Miles Gordenker:** On the product manager side, did that give you enough ammunition for now?

**Mara Leighton:** Have you covered any of this before?

**Mara Leighton:** Yeah.

**Mara Leighton:** So the initial demo preceded me.

**Mara Leighton:** So this is all new to me, but I'm assuming no, we haven't.

**Miles Gordenker:** Okay.

**Miles Gordenker:** I'll switch this.

**Mara Leighton:** .

**Miles Gordenker:** I'll let you do that.

**Miles Gordenker:** Yeah, you can keep on talking.

**Mara Leighton:** This is not a high brain power activity.

**Mara Leighton:** Okay.

**Mara Leighton:** Are there, so running through some of those other questions.

**Mara Leighton:** How does Datagrid optimize agent running costs, like token usage, etc.?

**Mara Leighton:** Idea being highlighting this expertise and implying cost savings.

**Miles Gordenker:** I don't think that's really the angle we want to take because we're going to be more expensive than most things.

**Miles Gordenker:** I think the angle we take is, hey, we can do more sophisticated tasks than competitors can, and we're more likely to get it right on the first run.

**Miles Gordenker:** And we can probably show some stats on how we did on benchmarks to back that up.

**Miles Gordenker:** But we're not going to use less tokens.

**Miles Gordenker:** If you really want to take that angle, you can mention that we're combining a lot of different models to arrive at the answer.

**Miles Gordenker:** So for certain tasks, it's running a cheap model.

**Miles Gordenker:** For other tasks, it's running a more expensive model because it needs it.

**Miles Gordenker:** And we're doing it that way.

**Miles Gordenker:** But that's, like, not super unique to us.

**Miles Gordenker:** A lot of companies.

**Mara Leighton:** Companies do that, so I don't know how much it's going to resonate.

**Mara Leighton:** Yeah, that makes sense.

**Mara Leighton:** And then just generally, how are you evaluating the outputs that agents are putting together?

**Mara Leighton:** Like the idea of being here to build trust that the agents are validated and robust?

**Mara Leighton:** What kind of metrics are you tracking?

**Miles Gordenker:** What processes are in place?

**Miles Gordenker:** We're using LLM as a judge combined with human review.

**Miles Gordenker:** Okay.

**Miles Gordenker:** So you can look that up and kind of see it later, but I'll kind of talk into it.

**Miles Gordenker:** Okay.

**Miles Gordenker:** First, like we'll do human reviews whenever someone thumbs downs something and feed that into improving it.

**Miles Gordenker:** LLM as a judge is basically when you say, when you have like a big suite of questions to ask the agent along with the data and then you have an expected answer and you use an LLM to compare the answer that you actually got with the expected answer.

**Miles Gordenker:** Right.

**Miles Gordenker:** right.

**Miles Gordenker:** And so

**Miles Gordenker:** But because we can run that, I think we've got like a few, at least a thousand of those test cases now.

**Miles Gordenker:** And a lot of them are very industry specific and we can run them at scale.

**Miles Gordenker:** Every time we make code changes, it lets us move a lot faster and ensure quality.

**Miles Gordenker:** And like, we can only do this because we have so many experts from heavy industry within the company.

**Miles Gordenker:** So they're able to like craft us evals that no one else has.

**Mara Leighton:** Okay, cool.

**Miles Gordenker:** And then also the agent is like reflecting after every action, after every turn of conversation and giving itself like a score on how it did.

**Miles Gordenker:** So we have access to that as well for like real-time monitoring.

**Miles Gordenker:** And then it'll remember the steps it took to get to a successful conclusion and answer the last time, which then makes it faster when it runs in the future.

**Mara Leighton:** Okay, cool.

**Miles Gordenker:** So for product managers, I think this one's a good one, like very basic.

**Miles Gordenker:** It prompt.

**Miles Gordenker:** All I did was attach a video, and it created two bug reports for me on my behalf, and it did a good job of correctly identifying everything.

**Miles Gordenker:** So the angle we take here is like, hey, look, not only is this thing going to save you time, but it's also going to give you better results because you're starting from a point where most of it's already written out.

**Miles Gordenker:** Like, in practice, when product managers are writing tickets, they end up getting lazy or time-constrained, and they don't put in this much detail.

**Miles Gordenker:** So we don't want to just say time savings.

**Mara Leighton:** We also want to say better output.

**Mara Leighton:** okay.

**Mara Leighton:** Understood.

**Miles Gordenker:** All of this is editable directly from within here.

**Miles Gordenker:** I can also tell it to edit certain parts of the...

**Miles Gordenker:** I can also...

**Miles Gordenker:** Tell it to use AI to rewrite parts of it for me.

**Miles Gordenker:** So that cycle of iteration is really fast, especially if product managers need to chain together multiple actions.

**Miles Gordenker:** Like, hey, I need to create a notion on this and then also send a Slack message or an email to make sure that the developers see it and hop on it right away because it's critical.

**Miles Gordenker:** Outlining that whole end-to-end journey would be particularly compelling for product managers because we spend so much time hopping around between different software.

**Mara Leighton:** Yeah.

**Mara Leighton:** And just knowing that it's creating itself, iterating each time and, like, what you're putting in, what kind of compound, and you'll get better responses in the future.

**Mara Leighton:** Does it remember, like, your preferences as well of, like, if you're a product manager and you typically prefer that your tickets look a certain way, will it learn your style and auto-apply it in the future?

**Mara Leighton:** Yeah.

**Miles Gordenker:** Cool.

**Miles Gordenker:** And users have control over that, too.

**Miles Gordenker:** So they can just delete those memories.

**Miles Gordenker:** If, like, they decide it's no longer serving them.

**Mara Leighton:** Cool.

**Miles Gordenker:** But also a pretty standard functionality.

**Mara Leighton:** I don't think it's going to, like, make any particular waves.

**Mara Leighton:** Yeah.

**Miles Gordenker:** Okay.

**Miles Gordenker:** What's the next question on the list?

**Mara Leighton:** Well, one of them is what advantages would an AI agent designer receive by working with Datagrid instead of building something like this from scratch?

**Mara Leighton:** Infra availability is one, but also from a design customization perspective.

**Miles Gordenker:** And define AI agent designer.

**Mara Leighton:** That's a great question.

**Mara Leighton:** I would imagine these questions are from Vivek, who is editing the content, but I would imagine anyone who might be able to build something like this for themselves versus just using Datagrid.

**Miles Gordenker:** Okay.

**Miles Gordenker:** Let me think about how best to position this.

**Miles Gordenker:** Okay.

**Miles Gordenker:** So I think a really common pain point that people experience is that, like, if you look at a lot of, like, the frameworks and stuff that's available for people today, they're not covering everything that you need end to end.

**Miles Gordenker:** So as an AI agent coder, just to, like, make the term a little bit more specific, you end up spending a lot of time, like, writing out the stuff to, like, prepare, ingest, and make available the data to the agents.

**Miles Gordenker:** So I think we can, like, potentially speak to, look, Datagrid's been around for five years.

**Miles Gordenker:** Like, at first, they were purely a data pipelines company.

**Miles Gordenker:** So we already have these 100...

**Miles Gordenker:** And we're not just shoving them into a vector database for you.

**Miles Gordenker:** We're enriching the data and making it easier to find for the AI just to simplify your entire process.

**Miles Gordenker:** And a lot of the magic from AI comes not so much from the AI itself.

**Miles Gordenker:** It comes more from the tools that you give the AI.

**Miles Gordenker:** So if I scroll through all of these tools, I already have a ton of tooling that someone who is building out an agent for themselves don't need to build from scratch anymore because they've got it all in here.

**Miles Gordenker:** And then we've built our API to play nicely with others as well.

**Miles Gordenker:** So one of our customers is calling the API 10,000 times a day.

**Miles Gordenker:** They're making the agent look like it's their own.

**Miles Gordenker:** They're not giving us any credit in any way.

**Miles Gordenker:** And that cut years off their development cycle.

**Miles Gordenker:** And we also have this really open philosophy.

**Miles Gordenker:** So if there's a gap in the functionality for the agent or someone needs to augment how it works, they have the ability to write their own tools and actions for it on the API.

**Miles Gordenker:** So kind of the net net of this is I think the messaging should be, look, we've already done a bunch of this hard work, so you don't have to.

**Miles Gordenker:** And if you're using our API, you're not beholden to us to build everything for you.

**Mara Leighton:** You can also self-serve if you're technical.

**Mara Leighton:** Okay, great.

**Mara Leighton:** That's perfect.

**Mara Leighton:** And then are there any technical examples of customization that you like typically show?

**Mara Leighton:** The example that Vivek left was, is there a way to create workflow templates that share common steps but might diverge at key points?

**Miles Gordenker:** For what?

**Mara Leighton:** Customer persona?

**Mara Leighton:** For any customer persona.

**Mara Leighton:** I think the perspective would just be, how can you create that level of customization for someone technical?

**Mara Leighton:** Also fine if you don't have a response on hand for that.

**Miles Gordenker:** I have other questions, but I just want to make sure to get through all of this.

**Mara Leighton:** I do.

**Miles Gordenker:** Cool.

**Miles Gordenker:** Kaelin, are they under NDA?

**Miles Gordenker:** Can I demo you in the customer space?

**Kaitlin Quimby:** We should be.

**Kaitlin Quimby:** I mean, they have access to a lot of our things.

**Kaitlin Quimby:** And let double check.

**Miles Gordenker:** There should be an NDA.

**Miles Gordenker:** I'm just going to pause for a second just to minimize the amount of stuff that's on screen, but I can show a good example of this.

**Mara Leighton:** Cool.

**Kaitlin Quimby:** There is, yeah, in our contract.

**Kaitlin Quimby:** Thank you.

**Kaitlin Quimby:** There's an NDA as part of the agreement.

**Miles Gordenker:** Great.

**Miles Gordenker:** I will pull as much as I can off screen.

**Mara Leighton:** And then after that, I would just be curious if there are any other kind of, we went through a few, but any other aha moments if you're demoing to a potential customer that might be useful for us to include in content as well.

**Miles Gordenker:** Sounds good.

**Miles Gordenker:** So what you're looking at here is an agent template.

**Miles Gordenker:** I inherited the general settings from this from the parent, and then I made some edits to it.

**Miles Gordenker:** I just changed the hub ID and the project ID to be specific for this agent.

**Miles Gordenker:** So if you're targeting the agent builder persona, basically what can say is like, hey, look, especially if you're dealing with a large enterprise company, it's extremely important to keep the data secure.

**Miles Gordenker:** And to minimize the amount of overhead.

**Miles Gordenker:** So what they can do is they can automatically set up team spaces for every project.

**Miles Gordenker:** Maybe it's a construction site.

**Miles Gordenker:** Maybe it's a certain division within the company programmatically.

**Miles Gordenker:** They can set up the agents programmatically.

**Miles Gordenker:** They can make changes to the instructions of the agents programmatically.

**Miles Gordenker:** So they have full control on how they set all of this up.

**Miles Gordenker:** And, you know, even whether they want to show Datagrid or not.

**Miles Gordenker:** Like, for example, they could even just only use Datagrid to bring in the data and store it in a vector database.

**Miles Gordenker:** But not use our agent framework or, you know, chain our agents with their agents.

**Mara Leighton:** They have a lot of room to maneuver there.

**Mara Leighton:** Cool.

**Miles Gordenker:** Great.

**Mara Leighton:** I think the other big aha moment.

**Mara Leighton:** And then also any, like, questions that you feel like you're typically fielding?

**Mara Leighton:** Like any maybe areas for a little bit of education would also be helpful.

**Mara Leighton:** But I also do want to be mindful of your time.

**Mara Leighton:** So if you, we don't need to use the full 30 if you have somewhere else to be.

**Miles Gordenker:** Yeah, security is a big one.

**Miles Gordenker:** We're SOC2 compliant and working our way towards FedRAMP.

**Miles Gordenker:** And typically the way I'll explain that to customers is like, hey, this is the same security standard that banks have to go through and the same audit.

**Mara Leighton:** Which is somewhat impressive to them.

**Miles Gordenker:** Yeah.

**Miles Gordenker:** Other aha moment is like the human in the loop stuff where we show the user a nice preview of what the agent's going to do in the connected system before they actually do it.

**Miles Gordenker:** And that's valuable because people are used to MCPs.

**Miles Gordenker:** So they have to go through this really crappy cycle of, you know, multiple rounds of...

**Miles Gordenker:** Multiple rounds of, like, reprompting this to get the right content.

**Miles Gordenker:** And so having that ability to review it beforehand, especially being able to see that, is really valuable to them.

**Miles Gordenker:** You said questions and other aha moments?

**Mara Leighton:** Yeah, anything else that you feel like, yeah, either that is a differentiator that you feel like resonates with most of the people that you speak with, or areas of opportunity for education, like they, yeah, like the security thing is perfect, like compliance.

**Mara Leighton:** But yeah, any other use cases where you're like, people love learning that they can do this?

**Miles Gordenker:** Not so much a use case, because I covered the key ones with you just now.

**Miles Gordenker:** But a tactic that generally works for me is just telling stories.

**Miles Gordenker:** I think a lot of people come into this with like a lot of anxiety about, hey, is my team going to be able to use this?

**Miles Gordenker:** Are they going to be able to adopt it?

**Miles Gordenker:** Is it like too technical for them?

**Miles Gordenker:** And it's like, I like to.

**Miles Gordenker:** Tell the story of this 50-something-year-old welder I've been working with who had never even used ChatGPT in his life and was kind of intimidated by all this.

**Miles Gordenker:** But he built a really complicated agent that takes the time it takes to evaluate a massive project spec for a construction project and figure out whether the company can do it down from three days to four hours.

**Miles Gordenker:** And he was able to do this because he's just good at talking with people.

**Miles Gordenker:** He's managed people before he could train a human to do it, which means you can write the instructions for an agent to do it.

**Miles Gordenker:** So I think there's a lot of thought leadership-type pieces that could be built around that, around like, hey, all the other companies do this.

**Miles Gordenker:** They just, like, hand their AI program to, like, a fresh college graduate because they assume that, like, they're going to be good at tech.

**Miles Gordenker:** Yeah.

**Miles Gordenker:** The right way to do this is to, like, find experienced managers who, like...

**Miles Gordenker:** Know how to write good English well.

**Mara Leighton:** That's kind of been like resonating with a lot of the folks at these conferences.

**Mara Leighton:** I'm just curious.

**Mara Leighton:** Do you have any like sales materials that have that story with the welder on it or any other kind of like social proof with him?

**Mara Leighton:** Like a case study or anything?

**Kaitlin Quimby:** I think I just posted it.

**Kaitlin Quimby:** I mean, I've interviewed him and working on a customer story.

**Kaitlin Quimby:** I didn't go as much into like his backstory in what I've written up, but I can add it in there.

**Kaitlin Quimby:** It's fairly easy.

**Mara Leighton:** Yeah, because that's a great, I love the point of flipping it from the youngest people on staff are going to be the most tech savvy to that's the wrong way of thinking about it.

**Mara Leighton:** You need to reverse it and go with like who has the most expertise.

**Mara Leighton:** And then because data grid is so efficient and elegant, they'll kind of, you're just getting the.

**Mara Leighton:** Best information, and then let Datagrid make it usable, technical, versus doing it the other way around.

**Miles Gordenker:** Yeah.

**Miles Gordenker:** Yeah, found a couple of related ones, but not that specific one.

**Miles Gordenker:** But, yeah, I feel like he's a good person, and sounds like Caitlin's already been in touch with him.

**Kaitlin Quimby:** Yeah.

**Mara Leighton:** Yeah, Brad.

**Mara Leighton:** Yeah.

**Mara Leighton:** I know we're pretty much at time, and I want to be respectful of your time.

**Mara Leighton:** This is very helpful.

**Mara Leighton:** Thank you for, like, popcorning around with all the different questions that we have.

**Miles Gordenker:** I know that wasn't the most linear experience, but this will be really helpful for the team.

**Miles Gordenker:** So thank you.

**Miles Gordenker:** For sure.

**Miles Gordenker:** Just doing my job.

**Mara Leighton:** If it helps you, it helps us.

**Kaitlin Quimby:** Yeah, super helpful.

**Kaitlin Quimby:** And then for the other items, I know that there was, like, a version of the newsletter that was going to be shared.

**Mara Leighton:** Can you just, like, send it in the notes, and then I can review?

**Kaitlin Quimby:** Yeah, we can just do the rest async.

**Mara Leighton:** Yeah, for sure.

**Kaitlin Quimby:** We'll follow up async.

**Mara Leighton:** Yay.

**Mara Leighton:** Thanks so much, Caitlin.

**Mara Leighton:** Thanks, y'all.

**Mara Leighton:** I appreciate it.

**Mara Leighton:** course.

**Miles Gordenker:** All right.

**Mara Leighton:** everyone.

**Mara Leighton:** Bye.
