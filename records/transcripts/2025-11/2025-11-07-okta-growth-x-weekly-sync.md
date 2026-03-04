# Okta <> Growth X - Weekly Sync

<metadata>
date: 2025-11-07
time: 17:01 UTC
duration: 44 minutes
organizer: Kyle Gaudreau (kyle@growthxlabs.com)
participants: Kyle Gaudreau, Sydney Go, Emily Erdman, Rachael Tiow
fathom_recording_id: 100091943
fathom_url: https://fathom.video/calls/463482590
share_url: https://fathom.video/share/hCACxoVT1GeYw3Hsjj-GbsVvNh-SQmQh
source: fathom
enriched_on: 2026-03-02 00:00 UTC
</metadata>

---

## Summary

GrowthX and Okta aligned on prioritizing repeatability over scalability for AI-driven prospecting. The core problem is that 90% of Okta's revenue team lacks the business context to write effective outreach, resulting in generic, ineffective messages. Emily presented research on AI tooling showing a hybrid workflow—using NotebookLM to synthesize briefs and Gemini for creative outreach—is most effective. The team committed to a 1-hour deep-dive session the week of November 17 to finalize the strategy, with an initial focus on proving the model with a small group (John Parker's enterprise sales team) before scaling to 300+ SDRs.

---

## Context

Emily Erdman recently joined Okta's team and is working closely with Rachael Tiow on revenue enablement initiatives. The meeting is part of a regular weekly sync between GrowthX (Kyle Gaudreau and Sydney Go) and Okta (Emily, Rachael) to align on account-based marketing strategy and AI enablement for prospecting. Okta's revenue organization faces a critical challenge: the sales development and account executive teams lack the business and industry context needed to craft compelling, value-driven outreach. This results in generic pitches that fail to resonate. GrowthX's engagement involves enriching data in Clay and building detailed account briefs that sales teams can leverage. The conversation focuses on finding the right tool stack and process to make this repeatable before attempting to scale across hundreds of sales reps.

---

## Relevance

**To GrowthX Delivery:**
- AI brief synthesis is becoming core to GrowthX's service delivery; the hybrid workflow (NotebookLM for context, Gemini for creative output) is the validated approach for Okta's use case
- Account brief structure may need refinement to better guide Gemini's output; GrowthX should plan to optimize brief formatting based on Emily's documented test results
- The initial pilot will target John Parker's enterprise sales team, providing a bounded scope for testing and validation before broader rollout

**To GrowthX Business Development:**
- Strong account health signals: Emily is actively embedded, Rachael is highly engaged in strategy sessions, and the team is scheduling additional deep-dives. Emily and Rachael's international travel (Dublin, London) suggests escalating importance of the engagement.
- Risk: Adoption is lower than expected even with briefs in hand; GrowthX should be prepared to support enablement and change management efforts, not just deliverables
- Opportunity: Okta's revenue org has 300+ SDRs and ~150-200 AEs; proving repeatability with Parker's team creates a strong case for expanding GrowthX's scope

**To GrowthX Strategy:**
- This deal is proving the market demand for AI-powered prospecting briefs; Okta's challenges (generic messaging, lack of context) are likely universal across enterprise sales orgs
- The emphasis on repeatability before scalability aligns with GrowthX's core value prop: smart, targeted enablement beats brute-force automation

---

## Overview

- **The Core Problem:** 90% of the revenue team lacks the business context to write effective outreach, leading to generic, ineffective messages like the "OddZero" example shared.
- **The Solution:** Prioritize repeatability over scalability. Focus on creating a repeatable process for a small group of "right players" (e.g., John Parker's team) to prove the model before scaling.
- **AI Tooling Refined:** A hybrid workflow is the most effective: use NotebookLM for synthesizing briefs and Gemini for creative outreach. Gemini alone gets confused by dense briefs; NotebookLM alone is too sterile.
- **Next Steps:** Emily will share her AI tool research doc. The team will hold a 1-hour deep-dive session the week of Nov 17 to finalize the strategy.

---

## Key Topics

### The Core Problem: Lack of Business Context

  - The primary challenge is the revenue team's lack of business context, not a tooling or scalability issue.
  - **Goal:** Enable the team to understand customer challenges and connect them to Okta's solutions, moving from generic pitches to value-driven conversations.
  - **Rationale:** Repeatability must precede scalability. A repeatable process must be proven with a small group before scaling to 300+ SDRs and AEs.

### The Solution: A Repeatable Process

  - The strategy is to build a repeatable process for a small group of "right players" who are motivated to use it.
  - **Initial Target:** John Parker's enterprise sales team.
      - **Why:** Parker is a senior leader who understands pipe gen and is frustrated with the SDR org's current performance.
  - **Process:**
    1.  Rachael's guide in Clay identifies target accounts (e.g., retail with login boxes).
    2.  The team selects accounts from this list.
    3.  GrowthX enriches data in Clay and builds detailed account briefs.
    4.  Parker's team uses the briefs for outreach.

### AI Tooling Refinement

  - Emily's research compared NotebookLM and Gemini for prospecting.
  - **Findings:**
      - **NotebookLM:** Excels at synthesizing briefs but creates sterile outreach.
      - **Gemini:** Struggles with dense briefs, getting confused by the volume of information.
      - **Hybrid Workflow:** The most effective method is using NotebookLM to create a "how to break in" framework, then feeding that context into Gemini to generate creative outreach sequences.
  - **Rationale:** This workflow combines NotebookLM's RAG capabilities (for factual retrieval) with Gemini's creative synthesis.
  - **Next Step:** GrowthX will experiment with a threaded conversation in Gemini to see if it can replicate the hybrid workflow's success in a single tool.

### Market Intel & Tooling

  - **Common Room:** Kyle's contacts (Marcel from Airbyte, Mario) expressed general pessimism about the tool.
  - **Adobe Journey Optimizer:** Rachael is skeptical after a demo where the vendor couldn't explain its "signals."
      - **Why:** It appears to be a repackaged version of existing tools like Sixth Sense.
      - **Action:** Kyle will seek feedback from his network on its effectiveness.

---

## Action Items

**Emily Erdman (Okta)**
- Email Kyle and Sydney the prospecting test documentation and Loom video (if time permits)
- Find Okta Workforce Product Marketing Manager; pull Highspot case studies; share with Kyle and Sydney

**Kyle Gaudreau (GrowthX)**
- Analyze CIAM vs OCI overlaps/differences; share findings with Rachael
- Research Adobe Journey Optimizer from network contacts; share findings with Rachael

**Sydney Go (GrowthX)**
- Analyze CIAM vs OCI overlaps/differences; share findings with Rachael

**Rachael Tiow (Okta)**
- Schedule 1-hour working session with Kyle and Sydney for week of November 17
- Add Clay professional services discussion to November 17 agenda

---

## Transcript
**Emily Erdman:** Taking a Monday, Tuesday off, doing a nice long weekend, being with the family.

**Emily Erdman:** So looking forward to it.

**Emily Erdman:** Awesome.

**Emily Erdman:** Well, happy birthday.

**Kyle Gaudreau:** Is it today or like Sunday?

**Kyle Gaudreau:** It is on Sunday.

**Kyle Gaudreau:** Okay.

**Kyle Gaudreau:** So, yeah, mostly just relaxing, doing some good stuff in the city, trying to forget how old I'm getting, you know.

**Emily Erdman:** Yeah.

**Emily Erdman:** Well, that's awesome.

**Emily Erdman:** So I'm glad to hear you're taking some time away and going to celebrate it properly.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** How about you?

**Kyle Gaudreau:** How's things on your end now being a couple weeks into the new team there?

**Emily Erdman:** It's good.

**Emily Erdman:** Yes.

**Emily Erdman:** I feel like I've jumped right in and gotten some great insight into the programs that we've got going and there's a lot going on.

**Emily Erdman:** So starting to get my teeth in a few of them, which is good.

**Emily Erdman:** Still lots to learn, but yeah, learning so, so much from Rachel.

**Emily Erdman:** So it's been, it's been a lot of fun.

**Kyle Gaudreau:** Amazing.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** you.

**Kyle Gaudreau:** I assume quite the change of pace from what you were doing before there.

**Emily Erdman:** Yeah, yeah, yeah.

**Emily Erdman:** Very different kind of worlds.

**Emily Erdman:** But yeah, it's been awesome.

**Emily Erdman:** And Rachel and I are actually headed to Dublin.

**Emily Erdman:** Both of us are heading there today.

**Emily Erdman:** We're meeting with the team there and then heading over to London about midweek next week as well.

**Kyle Gaudreau:** So we'll be excited.

**Kyle Gaudreau:** it sounds exciting.

**Emily Erdman:** Rachel, you don't look too excited.

**Rachael Tiow:** I actually asked myself, what did I sign myself up for?

**Rachael Tiow:** This is the thing.

**Rachael Tiow:** I love to travel.

**Rachael Tiow:** I always daydream about if I get to travel, I want to spend a year in every continent.

**Rachael Tiow:** Like,  that two week thing.

**Rachael Tiow:** That's lame.

**Rachael Tiow:** That's for kids.

**Rachael Tiow:** I've not made that dream a reality yet.

**Rachael Tiow:** So I got it.

**Kyle Gaudreau:** There's There's time.

**Rachael Tiow:** Yes, yes, yes.

**Rachael Tiow:** There's time.

**Rachael Tiow:** But that's only with the assumption that we think we are immortal.

**Kyle Gaudreau:** Well, you never know.

**Kyle Gaudreau:** You may end up being in Dublin for a bit and wanting to stay for a year.

**Rachael Tiow:** mean, you know.

**Rachael Tiow:** And unlikely.

**Rachael Tiow:** The weather is too welcoming.

**Kyle Gaudreau:** Yeah, it wouldn't be my choice either.

**Rachael Tiow:** Although I've heard amazing things.

**Rachael Tiow:** I've always wanted to go to Ireland.

**Rachael Tiow:** You know what I really want to do is I want to tour all those Polynesian islands because you can't travel.

**Rachael Tiow:** can't fly into all of them.

**Rachael Tiow:** got to go like on a, I don't know, some dinghy boats from one island to the next.

**Rachael Tiow:** It's not a dinghy boat.

**Rachael Tiow:** Sounds fun.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Sounds fun.

**Rachael Tiow:** And they drink all the kava that they've got.

**Rachael Tiow:** Samoan kava, Fijian kava, Vanuatu.

**Kyle Gaudreau:** Oh, I didn't realize there was so many variants.

**Kyle Gaudreau:** You just continue to educate me on the world of kava.

**Rachael Tiow:** There's Hawaiian variety.

**Rachael Tiow:** There's so many.

**Rachael Tiow:** And then you can.

**Rachael Tiow:** Look at the stalks and he's like some that has dots on there.

**Rachael Tiow:** Some are purple, some are purple and green.

**Rachael Tiow:** A lot.

**Kyle Gaudreau:** Interesting.

**Kyle Gaudreau:** Very cool.

**Kyle Gaudreau:** Well, I know we always...

**Rachael Tiow:** Exciting things this week.

**Kyle Gaudreau:** Yeah.

**Rachael Tiow:** I don't have SaaS stuff for Sydney.

**Rachael Tiow:** No hospitality.

**Kyle Gaudreau:** All good.

**Rachael Tiow:** I'm trying to tackle a bunch of stuff this week.

**Rachael Tiow:** So I haven't gotten back to you guys on the SaaS part.

**Rachael Tiow:** Yeah.

**Kyle Gaudreau:** I think the thing that would be helpful, you know, to spend a little bit of time experimenting of what's possible in the ABM side.

**Kyle Gaudreau:** You know, obviously Okta has come up a couple of times.

**Kyle Gaudreau:** I know we've talked about priorities in different ways, but I think it would be helpful.

**Kyle Gaudreau:** And I'm not sure we will nail this today, but perhaps as a follow-up to next week.

**Kyle Gaudreau:** Or, you know, a deeper discussion.

**Kyle Gaudreau:** Maybe we need more than 30 minutes.

**Kyle Gaudreau:** But, like, just how should we think about our priorities through the end of the year?

**Kyle Gaudreau:** We've talked about a lot of broad opportunities, but I think it would be helpful to help us, like, start to focus in on, like, having a clear kind of, like, set of goals for us to support and think around.

**Kyle Gaudreau:** Because, you we've created a lot of different artifacts.

**Kyle Gaudreau:** You know, there's things with Okta we can create more artifacts, but then we haven't necessarily leveraged all the artifacts we've created.

**Kyle Gaudreau:** So that's one side in my mind that I'm trying to think through of, like, how to think about focusing the time where we can provide the most value.

**Kyle Gaudreau:** And then on the ABM enablement side, I spent some time kind of experimenting with what this could look and feel like and generally came to the conclusion that I think there's something here, but, like, a bit more focus on the problem we're trying to solve would probably make it easier for us to be more useful here.

**Kyle Gaudreau:** You know, that felt a little bit broad as well.

**Kyle Gaudreau:** I like, love, I think, approaching in that broad way.

**Kyle Gaudreau:** really

**Kyle Gaudreau:** I don't see is going to be like terribly effective.

**Kyle Gaudreau:** I'll say I'm not as comfortable in that as I am like other AI based tools, but like just from, you know, how it's built.

**Kyle Gaudreau:** So anyways, we can go into the details in that, but just a high level.

**Kyle Gaudreau:** That's like one of the things that really I think would be helpful for us as we as we think about wrapping the end of the year.

**Kyle Gaudreau:** I know we talked about like ramping up on artifacts and that was one of the milestones we had talked about recently.

**Kyle Gaudreau:** But now where to go from there?

**Rachael Tiow:** So Emily did some research and she can share more detail on the comparison between using GEM, Notebook LM for prospecting.

**Kyle Gaudreau:** Oh, yeah, I'd love to.

**Kyle Gaudreau:** Yeah, I think I was doing similar.

**Kyle Gaudreau:** So I would love to see what you came up with.

**Emily Erdman:** Yeah, so we did do a bit of research and I'll share it with you as well, Kyle and Sydney.

**Emily Erdman:** But looking to understand if we need to essentially have two tools that we're providing to the SDR.

**Emily Erdman:** To then, you know, take the account briefs and then go to market with them.

**Emily Erdman:** So the TLDR on that is the notebooks are super helpful for like kind of synthesizing and pulling out the big pieces and aligned messaging frameworks, if you will, on the signals from, for the internal folks, SDRs, AEs.

**Emily Erdman:** But it doesn't do a good enough job of actually going through and creating, using that context to then create good outreach sequences.

**Emily Erdman:** yeah, so the content was so sterile, but then if you're just using kind of a gem alone, tested a couple different things.

**Emily Erdman:** I tested actually uploading all of our Akamai briefs into one PDF and then giving that context to a gem.

**Emily Erdman:** And then the prospecting instructions as well as kind of the gem instructions.

**Emily Erdman:** And it got very confused.

**Emily Erdman:** It was like pulling things from different accounts.

**Emily Erdman:** And we ended up pulling another test, which is 10 individual accounts, briefs, and then the prospecting instructions.

**Emily Erdman:** And while it didn't get as confused, I found that actually when I ran a third test, which was uploading the 10 sample briefs and then asking the gem to put together a sequence in addition to giving context from notebook.lm on breaking into the account is when I had the best output with the best context and framework for actually putting together a sequence that had substance that pulled from the framework and also had a positive, like effective outreach sequence as well.

**Kyle Gaudreau:** Interesting.

**Kyle Gaudreau:** So,

**Kyle Gaudreau:** Some of that certainly not surprising, you know, especially like in a single file, potentially flooding context, although, you know, context window in a gem is pretty large.

**Kyle Gaudreau:** About 2x high, though, in notebook LLM.

**Kyle Gaudreau:** think notebook LLM is like 2 million tokens or something like that.

**Kyle Gaudreau:** So it's like pretty large, but.

**Emily Erdman:** Can you share more on that, Kyle?

**Kyle Gaudreau:** Kyle so think of it as like, it's unfortunate, too, because these systems won't necessarily like flag this for you.

**Kyle Gaudreau:** Like you have hit the context window.

**Emily Erdman:** I am now going to be less effective.

**Kyle Gaudreau:** It is more to understand, you know, different models have different context windows.

**Kyle Gaudreau:** One of the things that's nice about the Google models is they have the biggest context windows of the major players.

**Kyle Gaudreau:** So like a ChatGBT5, I actually don't recall what that is off the top of my head, but far smaller than the...

**Kyle Gaudreau:** The window that Gemini has, which is about a million, and the Notebook LM is about two million, but then there's also an important distinction between the Gemini gems and then Notebook LM.

**Kyle Gaudreau:** Notebook LM is more like a classic RAG model, and so it's going to be better at basically similar to kind of what you were talking about, like staying true to what we are feeding it from context and pulling out the details.

**Kyle Gaudreau:** It's going to be less good at taking that and synthesizing that and helping us think creatively.

**Kyle Gaudreau:** So that was part of what I was trying to experiment with is like, see like, how does it do with that?

**Kyle Gaudreau:** Maybe I'm like, you know, maybe I'm being too pessimistic about this and it does better than I think, and largely I was kind of underwhelmed of like, oh, can I like legitimately like come up with some like compelling webinar?

**Kyle Gaudreau:** I basically like I did like I retail test and I fed in like, you know, like all the necessary artifacts and anyways, long story short, it struggled there.

**Emily Erdman:** Yeah.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** The example that you shared about feeding in the how to break in from notebook LN, generate that, feed that into the gem, and then the outbound sequence, I think the experiment I would then think about there, maybe you already did this, to use like a very, this is not a great example, but like, um, so I, I, when we initially created this, this was like a little test we did in the gem, because it was like, mimicking how the SDR team was prompting, they were doing very basic prompts, so we were trying to see like, what would be outputted if we did that, similar as kind of what you mentioned, breaks down some details, I think from here though, it's, how does a, how a threaded, um, a threaded message do compared to what you had mentioned, right, and so, by starting in the gem,

**Kyle Gaudreau:** And saying, help me break into that, getting that details, and then moving on to whatever it was you prompted from outbound sequence within that.

**Kyle Gaudreau:** Like, how does that compare to the example that you had highlighted?

**Emily Erdman:** Because if it is, like, situation.

**Kyle Gaudreau:** So this is one of those things, it's like, there's not necessarily a right or wrong answer.

**Kyle Gaudreau:** It's like, you know, just how to make this more scalable.

**Kyle Gaudreau:** So I think there's an application, certainly, for Notebook LM.

**Emily Erdman:** I think it's probably going to be better in, like, education-based things.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Less good at, like, ideation, thinking creatively.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Which, you know, that ABX team will need in certain situations.

**Kyle Gaudreau:** So that's why I came back to, like, trying to think about, like, what is the ultimate, like, things we want to move the needle on.

**Kyle Gaudreau:** And you can say that, obviously, on the SDR side as well.

**Kyle Gaudreau:** But anyways, hopefully some of that was helpful.

**Kyle Gaudreau:** But, yeah, I think what you mentioned makes a lot of sense.

**Kyle Gaudreau:** And it'd be good to just continue to experiment with that to see what are the right ways of bringing these puzzle pieces together.

**Emily Erdman:** absolutely.

**Emily Erdman:** Are you aware of any tools that are good at doing both, right, that can help synthesize these briefs into digestible chunks for the internal sales teams, but then also content creation or outreach creation, for example?

**Kyle Gaudreau:** That's a good question.

**Kyle Gaudreau:** I would lean more towards Gemini for that, and so if it is lacking in one of those key steps from what you're seeing, like, it's helpful to get your take on, like, what particularly do you feel like it's missing the mark on?

**Kyle Gaudreau:** If we can then take that and understand those points of friction, we can try to think creatively, like, how would we maybe think about adapting the structure in the briefs to specifically address that?

**Kyle Gaudreau:** That doesn't mean it does, but...

**Kyle Gaudreau:** But just as an example of how that could be helpful for us to think about this, generally I would, like, my own work and like how I would do this is I would go to Claude typically for stuff like this.

**Kyle Gaudreau:** I'm a big fan of, especially with 4.5 of base things, it's similar to what Gems does, but it also has its pros and cons, like context window isn't as high, you can hit limits quickly.

**Kyle Gaudreau:** I was just going to say, think Gemini may be the best of all, you know, trying to weigh the varying factors, it's probably the best of the bunch.

**Emily Erdman:** Yeah, but I think that makes sense, Kyle, like, is there something that we can adjust in the brief itself so that it is one tool, Gemini, that the sales teams are using and uploading the briefs directly there versus going to notebook first to get that context.

**Emily Erdman:** And I can share a little bit more on what I was seeing.

**Emily Erdman:** Yeah, that would be great.

**Emily Erdman:** In general, yeah, I felt like the Gemini was getting just a little bit more confused of like the key pieces to pull in versus just the sheer amount of information on the brief, if that makes sense.

**Emily Erdman:** Like how to position, what is worth positioning versus what is maybe more of just like a detail of the account.

**Kyle Gaudreau:** Does that make sense?

**Kyle Gaudreau:** That's something also that could be addressed to the instructions in some degree.

**Kyle Gaudreau:** What may be helpful, I know you all are traveling, you know, I'm happy to like, if it even fits in your schedule, like have a time where we just jam and like do that live.

**Kyle Gaudreau:** Or alternatively, like, if you could like record as like a quick loom or something and just like, here's what I'm seeing, and then we can take that back and start to dig in ourselves.

**Emily Erdman:** Yeah, and I actually did, I documented some of these tests on just like a Word doc.

**Emily Erdman:** So...

**Emily Erdman:** So...

**Emily Erdman:** As a starting point, while we're traveling, I can get that over to you as well.

**Kyle Gaudreau:** Yeah, that sounds good.

**Kyle Gaudreau:** And yeah, as we can understand a little bit of how you're approaching it better, we'll do our own experimentation.

**Kyle Gaudreau:** But I do think there's, it's not going to be perfect, but no doubt I think there's enhancements we can make to this.

**Kyle Gaudreau:** We very much looked at like what we initially used like a V1, or we can get feedback on that.

**Kyle Gaudreau:** We can continue to be like, okay, here's an interesting problem.

**Kyle Gaudreau:** How do we, how do we tackle that?

**Kyle Gaudreau:** You know, we still have ultimately that other challenge of like scale eventually as well that we'll need to tackle.

**Kyle Gaudreau:** And that is another reason I was a little bit pessimistic to a degree with Notebook LM, because it does have some restrictions on scale.

**Kyle Gaudreau:** I was less aware of until researching a little bit deeper.

**Kyle Gaudreau:** So like your team could start to hit like usage limits.

**Kyle Gaudreau:** Okay.

**Kyle Gaudreau:** And like.

**Rachael Tiow:** I'm sure you have opinions on this, but is this a world that you're kind of open to us moving to adjusting the briefs to give more maybe context and directive in the actual brief itself so that we could have one solution be Gemini for everyone to be using in terms of outreach and things I think if we're talking about using Gemini or Gem just for the prospecting, I don't want to think about it from groups lens, right, because that will be very, very limiting.

**Rachael Tiow:** But if we're thinking about it from the lens of, it's for prospecting or pipe gen, then that makes sense.

**Rachael Tiow:** I still think it makes sense to also have notebook element there because I have used it, poked around it enough for it to help with ideation.

**Kyle Gaudreau:** Per account does not certainly feel scalable, so that's kind of one of the challenges we saw, nor is swapping out different, nor is swapping out, like, within a particular gem, like, okay, now I'm working on this, remove this brief, add a new one, so that's an example of some of the scalability things in our mind.

**Kyle Gaudreau:** So, it's a little, I don't know if we've really had a clear solution for that part yet, to be clear.

**Kyle Gaudreau:** You know, it just comes back to, like, you know, there's just going be pros and cons either way, there's going to be limitations of these systems.

**Kyle Gaudreau:** Notebook LM is certainly better for that, in that you can upload more, it does still have limitations in terms of number of files you can add, though, because if you consider number of accounts you all are really managing, you would definitely hit those limits.

**Kyle Gaudreau:** So, yeah.

**Kyle Gaudreau:** Sorry, my memory is failing me a little bit of where we last left that particularly because we haven't talked about that structure in a little bit.

**Rachael Tiow:** None of it is scalable, right?

**Rachael Tiow:** So I think we need to remove that from our thinking because Notebook LM is not, I treat Notebook LM more of a library and you can go in there, you can ask questions.

**Rachael Tiow:** It does a pretty good job with retrieving information and because a lot of the challenges that these companies go through are very, very similar.

**Rachael Tiow:** even if it blends like one company to the next, it's able to pull.

**Rachael Tiow:** I think what will be helpful is for me to share what I'm looking to solve for, right?

**Rachael Tiow:** I'm not looking to solve for scalability right now.

**Rachael Tiow:** I'm not looking to solve for having everything hooked up.

**Rachael Tiow:** So that it can work seamlessly.

**Rachael Tiow:** I'm solving for the fact that as a business unit, we as a company on the revenue team, 90% of us, do not understand what are the challenges that a company is going through.

**Rachael Tiow:** Therefore, we send out messages like this one that a buddy of mine sent me this morning and says, wow, this is your ABM.

**Rachael Tiow:** I'd love to tell you how OddZero can make your login box awesome.

**Rachael Tiow:** If you hop on a meeting with us, we'll also give you a free seven-piece cocktail set.

**Rachael Tiow:** Customer identity is a must-have for your business to create secure, delightful customer experiences and compete in today's digital age.

**Rachael Tiow:** That's why companies of all sizes have turned to OddZero.

**Kyle Gaudreau:** I don't know I like that, but it's not great.

**Rachael Tiow:** It's not, it's not marketing.

**Rachael Tiow:** It's not, it's not pipe gen, period.

**Rachael Tiow:** I don't care what fancy .

**Rachael Tiow:** It's terms we want to give it for different teams, like inbound, outbound, AVX, AVM, Dimension, global campaigns.

**Rachael Tiow:** Call it what you want.

**Rachael Tiow:** Sprinkling stuff on things that are not good does not make it great.

**Rachael Tiow:** So that's the goal of why we're building these.

**Rachael Tiow:** The goal is not for scalability.

**Rachael Tiow:** It's for people to easily consume the information in a way that helps understand, oh, these are the things that's happening.

**Rachael Tiow:** And in a lot of ways, the stuff that you're building from us enriching things in clay and then you're building out the briefs is really where the context is because the additional stuff that I add into the gem or the notebook element is the business narrative.

**Rachael Tiow:** If I don't know what problems I'm solving, knowing all this information is futile because they don't know how to connect the dots.

**Rachael Tiow:** So that's what I'm solving for.

**Rachael Tiow:** So I don't care if it's not scalable.

**Rachael Tiow:** I don't care that it's not plugged into stuff.

**Rachael Tiow:** I don't even care if it's manual.

**Rachael Tiow:** It's...

**Rachael Tiow:** Because scalability before repeatability is just also another recipe for disaster.

**Rachael Tiow:** Like I can't scale what's not repeatable and I don't know what's working, what's not.

**Rachael Tiow:** And the issue right now is a lot of people are not using it.

**Rachael Tiow:** So that's an area that Emily and I are working on.

**Rachael Tiow:** Predominantly, this is Emily's idea.

**Rachael Tiow:** Before we met in person and have a chat, she's like, hey, you know what?

**Rachael Tiow:** I've had some chats with folks in the office.

**Rachael Tiow:** I think we need to drive enablement and adoption for these growth engines.

**Rachael Tiow:** So that will be the first place to start.

**Rachael Tiow:** But then once we open up the floodgate, the areas where I'm trying to throttle myself, and which is why it's not been widely adopted, is once I open up the floodgates, the question is, can y'all give me account briefs for 60,000 accounts?

**Rachael Tiow:** You see?

**Rachael Tiow:** So that's where I'm trying to throttle too, where I'm like, this is not realistic.

**Rachael Tiow:** So I'm trying to throttle in a few ways.

**Rachael Tiow:** I have my guide.

**Rachael Tiow:** That is working out of clay for, firstly, for us to determine which account should we go after first and why.

**Rachael Tiow:** And then from there, they got to pick the accounts.

**Rachael Tiow:** And then from there, we'll have the detailed account briefs built.

**Rachael Tiow:** Otherwise, we build all these things.

**Rachael Tiow:** And Kyle, you know this.

**Rachael Tiow:** You've been at several companies as a CMO.

**Rachael Tiow:** There's always a shiny object syndrome.

**Rachael Tiow:** I can't even get 14 SDRs to use the tool that's going to put money in their pocket.

**Rachael Tiow:** I cannot imagine trying to run 300 SDRs and about maybe 150 to 200 AEs.

**Rachael Tiow:** I haven't figured out my solution yet.

**Rachael Tiow:** No.

**Rachael Tiow:** So those are some things that I'm coming up against.

**Rachael Tiow:** The other thing is I'm also trying to convey and compel and influence the executive team that we have all these signals and they're not sitting in a single unified view.

**Rachael Tiow:** And we have tools selling the executives that they got, 6x has got no signals, right?

**Rachael Tiow:** Adobe's got no signals, but they are using these as buzzwords to get the attention of the execs.

**Rachael Tiow:** And I'm trying to educate them on those are not signals.

**Rachael Tiow:** And they go, well, what do you mean?

**Rachael Tiow:** I'm like, signals are behavioral changes, whether it's market drivers, whether it's the business drivers within them.

**Rachael Tiow:** We used to call them triggers.

**Rachael Tiow:** What are the telltale signs that a company is having challenges?

**Rachael Tiow:** They do not measure those.

**Rachael Tiow:** They're just literally a black box looking at keywords scripted from some third-party website and have some algorithm to determine the intent that matches along with our first-party engagement data.

**Rachael Tiow:** That is not a signal.

**Rachael Tiow:** That's just first-party data engagement.

**Rachael Tiow:** So I'm struggling with that one too, right?

**Rachael Tiow:** I've got to tackle...

**Rachael Tiow:** All that piece, because for us to ensure that people are doing things, I've to measure it, and we don't have a way of measuring it right now.

**Rachael Tiow:** So we're doing this all in hacks, and I'm giving these as context to let you know why things are the way they are at the moment.

**Rachael Tiow:** It's super clunky and deeply frustrating, hence my look when I joined the call.

**Rachael Tiow:** So we'll just charge on ahead with what we've got and build them as minimal as it is right now, where it's like, hey, where are we at?

**Rachael Tiow:** Are there people using it?

**Kyle Gaudreau:** It's just so I can't quite figure out why.

**Kyle Gaudreau:** Yeah, certainly appreciate that, you know, my mindset generally coming into this is just to have, like, each and every week make sure we're building momentum and continue to build leverage and trying to figure out exactly where to put that focus to.

**Kyle Gaudreau:** But yeah, I understand there's some complexity to that.

**Kyle Gaudreau:** I don't know, it feels like a

**Kyle Gaudreau:** A piece of this is, like, no doubt there is specific account-based things that have useful context that can be better surfaced to the team, but it sounds like that's even a step down the line of the challenge of, you've kind of mentioned, they don't even understand the industry at a deep enough level.

**Kyle Gaudreau:** is that where we start first into how we're thinking about the, like, we have the artifacts, how is that leveraged in a way that helps start with solving that piece first, what is the piece of that, but it's less about how to break into that account and more education, but I don't know if that really moves the needle in a meaningful way.

**Rachael Tiow:** But then this is the thing, right, so this is where, in the beginning when we started working together, I was very, very repetitive.

**Kyle Gaudreau:** said, guys, everything starts at the business narrative level.

**Rachael Tiow:** Mm-hmm.

**Rachael Tiow:** It doesn't have to be company-specific.

**Rachael Tiow:** I just need to know broadly, what are we solving for for an industry?

**Rachael Tiow:** Now, then there will be all these offshoot industries that we don't do business with all the time, but there's a use case there.

**Rachael Tiow:** So there's a few ways we can think about it.

**Rachael Tiow:** Business narrative at an industry level, business narrative at a sort of market overview level.

**Rachael Tiow:** The reason why is for Okta workforce, let's not even use brands, from the world and the lens of identity and access management, the narrative is pretty straightforward.

**Rachael Tiow:** You got employees, got all varieties of employees from full-time, 1099, business partners.

**Rachael Tiow:** You have these different types of users.

**Rachael Tiow:** There are business users logging in.

**Rachael Tiow:** How do you ensure that there's lifecycle management on them, there's governance on them, you can update?

**Rachael Tiow:** Not only that, because they're also accessing multiple types users.

**Rachael Tiow:** Apps within one portal, how do you access, how do you govern their ability to access all these things from a full lifecycle management way, right?

**Rachael Tiow:** So it's a high-level overview.

**Rachael Tiow:** Then when we start to look at SIAM, Customer Identity Access Management, where Okta and OddsRare starts to differ is Okta does very well if it's highly regulated, most especially if it needs FedRAMP, because OddsRare is not FedRAMP certified.

**Rachael Tiow:** So this carves two paths for these both SIAM players.

**Rachael Tiow:** OddsRare does really well all in the realm of e-com and tech, so digital native companies.

**Rachael Tiow:** All the coin bases of the world, all the whoops of the world, wealth front of the world, that's where we dominate.

**Rachael Tiow:** All the Sephora's in the world, that's where we dominate.

**Rachael Tiow:** But then when it comes to Wells Fargo,

**Rachael Tiow:** Fargo, your local credit union, to life sciences like Fred Hutch and whatnot, that falls in the realm strongly for Okta.

**Rachael Tiow:** Siam, I'm just looking at Siam, I'm thinking of Brandtia.

**Rachael Tiow:** So that's where things are at right now, how I've kind of mapped things out.

**Rachael Tiow:** And I'm also hesitant to sort of do it that way because now it seems like I'm playing God, right?

**Rachael Tiow:** And these are things that they need to verify it.

**Rachael Tiow:** And I have data to support it, but I don't want that if anything breaks, it falls on my neck.

**Rachael Tiow:** So that's how we would think about it.

**Rachael Tiow:** And that's why I keep going back to the narrative.

**Rachael Tiow:** Like what problems do we solve for from a workforce perspective and from a customer and identity perspective?

**Rachael Tiow:** Then we can break them into groups.

**Rachael Tiow:** What do we solve it from the lens of all the industries for IAM?

**Rachael Tiow:** And then what do we solve for Siam in the highly regulated industries?

**Rachael Tiow:** And what do we solve Siam for in a...

**Rachael Tiow:** music weight?

**Rachael Tiow:** And so solve

**Rachael Tiow:** E-commerce, retail-heavy, and digital-native companies.

**Rachael Tiow:** That then we can feed accounts into it, right?

**Rachael Tiow:** Because that's where really then accounts, because accounts is really a detail in the macros of what I just described.

**Rachael Tiow:** So that is the latest way I've been thinking about how to enable the teams so that they understand it.

**Rachael Tiow:** I don't even have the time to go look for all these documents personally.

**Kyle Gaudreau:** Yeah, that kind of leads to my question, is this just a matter of that context is out there, and it's just not being surfaced in the right way, and that's where we can be helpful in trying to do that.

**Kyle Gaudreau:** Because if I try to think about how we help move the needle there, we'd be quite limited without that context, at least from what I understand.

**Rachael Tiow:** Yeah, I think a lot of the use cases will come from case studies, right?

**Rachael Tiow:** Like, the case studies usually go over why this company is using it.

**Rachael Tiow:** And I think you can gather from that.

**Rachael Tiow:** Maybe this is something that Emily can help tackle is figuring out who's the PMM working on the workforce side, and we can glean all that data from Highspot, and if they can share it the way Brad and all the other folks on the PMM on the odd zero side can help, that would be great.

**Rachael Tiow:** The other one is what would be helpful is because you guys have, the PMM that you guys have talked to so far works under the umbrella for, broadly speaking, CIAM, Odd Zero, and Okta OCI.

**Kyle Gaudreau:** Okta OCI stands for Okta Customer Identity.

**Rachael Tiow:** I would love for you guys to, like, as you guys are ingesting that data to see really where do they overlap, because nobody can tell me where they overlap and how they differ, how they differ, which is, I think, quite bizarre.

**Rachael Tiow:** Okta OCI.

**Rachael Tiow:** right?

**Rachael Tiow:** Yeah, I find it kind of strange, like, when I asked Brad, Brad's like, yeah, actually,

**Kyle Gaudreau:** That was similar to houses when I met with them.

**Kyle Gaudreau:** That was the vibe I got.

**Rachael Tiow:** was like, okay, I don't know.

**Kyle Gaudreau:** Yeah, which I think it's kind strange.

**Rachael Tiow:** So I have just pretty much done my own line in the sand that I've been telling Janice about, and she seems to agree, but.

**Rachael Tiow:** Yeah, so that's where things are at.

**Rachael Tiow:** I don't know where you can jump in and help at this point.

**Kyle Gaudreau:** I just have a lot of stuff going on in my head right now, and I'm trying to fight the battle that will have the strongest lift in our work while we move these pieces forward, yeah.

**Kyle Gaudreau:** Wouldn't it be helpful for us?

**Kyle Gaudreau:** I realize now you're jumping into this travel period you've been talking about for a while, and your schedule's going to be crazy.

**Rachael Tiow:** I make time for the equal places, and things are important, Kyle.

**Kyle Gaudreau:** It feels to me there is an opportunity for us to do a bit of like a deep dive session.

**Kyle Gaudreau:** It's hard for us to like...

**Kyle Gaudreau:** We get too deep into this in a 30-minute meeting, so, you know, over the next two weeks, whatever makes sense, it feels to me we needed a bit of a longer period of time just to start collaborating and talking through this and just having, working back to, like, what are our, what are the key bets we want to make?

**Rachael Tiow:** Yeah, because the thing that I struggle a lot, Kyle, speaking plainly, is if people don't know what they don't know, where do you even begin looking, right?

**Rachael Tiow:** Yeah.

**Rachael Tiow:** That's a big thing that I'm facing right now.

**Rachael Tiow:** Like, right now, Emily and I have been tag-teaming on Coca-Cola.

**Rachael Tiow:** That's why I ask for Coca-Cola.

**Rachael Tiow:** Coca-Cola, okay, you guys don't even have an identity background.

**Rachael Tiow:** Let me ask you this.

**Rachael Tiow:** Let's talk about common effing scents.

**Rachael Tiow:** If you're trying to go after a company through the lens of your GrowthX lab, and this company has bought a large, like, LLM model,

**Rachael Tiow:** And sign a billion dollar deal with OpenAI.

**Rachael Tiow:** Do you think you're going to win that contract by beating up OpenAI?

**Rachael Tiow:** Or do you think maybe, hey, where are the gaps in OpenAI that we can win?

**Rachael Tiow:** And maybe that's how we're going to enter that deal.

**Kyle Gaudreau:** Right?

**Kyle Gaudreau:** Yep.

**Rachael Tiow:** Generally how I've thought about it.

**Rachael Tiow:** Yeah.

**Rachael Tiow:** Like in Cantonese, have an expression, tiny streams of water can turn boulders into pebbles.

**Rachael Tiow:** That's the approach we need to have.

**Rachael Tiow:** And here we have these  nimwits trying to go in like, we've got to fight Microsoft.

**Rachael Tiow:** I don't know about you.

**Rachael Tiow:** I'm  fighting on a good day.

**Rachael Tiow:** I'm not going to go battle a giant.

**Kyle Gaudreau:** I'm not going to win.

**Kyle Gaudreau:** You know, I put my money on you.

**Kyle Gaudreau:** It's one thing I've learned.

**Kyle Gaudreau:** Even though we have never met in person, you get the words.

**Rachael Tiow:** I not die out here.

**Rachael Tiow:** But you know, it's like, that is a huge frustration of mine.

**Rachael Tiow:** And this is not just on one account.

**Rachael Tiow:** I see this pattern.

**Rachael Tiow:** And across, over, and over, and over, and it's extremely concerning for me.

**Rachael Tiow:** And so where do we begin?

**Rachael Tiow:** Where do we begin?

**Rachael Tiow:** This is something that comes into enablement.

**Rachael Tiow:** So now I'm pivoting my game a little bit here where I go.

**Rachael Tiow:** Okay, let's find the right players instead of trying to make it work for players.

**Rachael Tiow:** Let's find the right players.

**Rachael Tiow:** We will ship these briefs to the players, and I've brokered a deal with JP, John Parker, who leads enterprise sales for Odd Zero.

**Rachael Tiow:** He's a very senior enterprise leader between us all girls.

**Rachael Tiow:** Not sure why and how he didn't get the VP role, and he's the AVP.

**Rachael Tiow:** Maybe he didn't want it.

**Rachael Tiow:** But super senior enterprise leader, knows and understands PipeGen very, very well.

**Rachael Tiow:** And I told them, said, JP, let me get done with coming through this.

**Rachael Tiow:** time.

**Rachael Tiow:** see.

**Rachael Tiow:** Let's you.

**Rachael Tiow:** Retail list so that I know which ones has login boxes and loyalty programs.

**Rachael Tiow:** Once I have that, we'll be able to know which ones we want to focus on.

**Rachael Tiow:** Once we know that, then I'll continue to enrich things out of clay, and then we'll submit those enrichments over to you guys, and you guys can pull the account briefs.

**Rachael Tiow:** His team is probably going to use it because they're the AEs, and he's completely jaded with the SDR org.

**Rachael Tiow:** So I think finding the right players, the right player and the right leaders, this is also another issue we've got.

**Rachael Tiow:** When kids act out and they're misbehaving, chances are it's not them, it's the parents.

**Kyle Gaudreau:** It's a hit out because my son has not been acting well this week.

**Kyle Gaudreau:** I feel attacked.

**Kyle Gaudreau:** Ha, ha, ha, ha, ha.

**Rachael Tiow:** Just saying, you know, chances are, okay, granted that there's always an anomaly in the family, you know, but our leadership too is a problem.

**Rachael Tiow:** So I'm just sharing very openly about all these things that's like swimming in my head and giving me a lot of like headaches around like, wow, I've tried this route that didn't work.

**Rachael Tiow:** tried that route that didn't work, okay, I need to find a different route.

**Rachael Tiow:** Um, so y'all are just experiencing the, uh, sort of like the filtered end of the other stuff.

**Rachael Tiow:** Same.

**Rachael Tiow:** I have to hop to another call.

**Rachael Tiow:** Um, let's find time.

**Rachael Tiow:** Let's make time to meet.

**Rachael Tiow:** Let me give, give me a week to collect my thoughts.

**Rachael Tiow:** If you guys have any ideas based on what I've shared with you, happy to hear them.

**Rachael Tiow:** Another ask I have is, I'm also trying to figure out this, uh, contractor thing with this clay professional services.

**Rachael Tiow:** Um, I'll put that on the docket for us to talk about, but, yeah, let's, let's think in the week after next, I'll be in Munich, but I'll, I'll make time for us to connect for an hour and talk through some stuff that gives me a week to really gather my thoughts and, and, uh, figure out a clear path forward.

**Kyle Gaudreau:** you all will be traveling next week.

**Kyle Gaudreau:** We shouldn't meet next week is what I'm hearing.

**Kyle Gaudreau:** That's what I'm saying.

**Kyle Gaudreau:** Yep.

**Rachael Tiow:** Yep.

**Rachael Tiow:** Yep.

**Rachael Tiow:** Cause, um, I want to make sure that when we meet for an hour next week, maybe my, my brain gets cleared up by then, uh, and the clouds have parted, but, uh, You're going to have a long, a long flight to, I suppose.

**Rachael Tiow:** I know.

**Rachael Tiow:** I'm hoping to catch up on sleep there.

**Rachael Tiow:** And there is no wifi on the British airway.

**Kyle Gaudreau:** It's lame.

**Kyle Gaudreau:** None.

**Rachael Tiow:** That's why.

**Rachael Tiow:** I cried last time.

**Kyle Gaudreau:** I didn't get no, um, Sometimes you get on an unlucky flight, uh, that's happened to me where I'm like, oh my God, I'm going to get so much work done on this trip.

**Kyle Gaudreau:** And then nope.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** Uh, but.

**Kyle Gaudreau:** Yeah.

**Rachael Tiow:** Kyle, it's going to not be a workaholic here.

**Rachael Tiow:** Yeah, give me a week, let me gather my brains on my neurons, and then I can game plan, like, I'll have discussions with Emily, because you know what's fresh is because she's looking at this from a third person's view, that's not so true.

**Emily Erdman:** the trenches, yeah.

**Rachael Tiow:** Yeah, yeah, yeah, yeah, yeah, so I can see it from, I can see it from a beginner's mind, right, like, because I'm so in this all the time.

**Kyle Gaudreau:** Yeah.

**Rachael Tiow:** And then it doesn't help them, I'm already so frustrated, so if I can see it from the lens of a beginner's lens, I'm like, oh, okay.

**Rachael Tiow:** That can speak some sense into my head.

**Rachael Tiow:** So give me a week, and then we'll sync the week after next week, which will be November 17th.

**Kyle Gaudreau:** Sounds like a plan.

**Emily Erdman:** I'll add it to our list to talk about while we're chilling.

**Kyle Gaudreau:** Thank you, thank you.

**Rachael Tiow:** escape.

**Kyle Gaudreau:** By the way, Rachel, this is quick.

**Kyle Gaudreau:** I did have a chat with a few people around Common Room.

**Kyle Gaudreau:** I don't have anything, like, terribly...

**Kyle Gaudreau:** Like directly useful other than like general pessimism, like Marcel, headed growth from Airbyte Mario, I was with them both this week having lunch and we were talking them through it, and yeah, they just, yeah, I did not hear a lot of positives about leveraging common room, so I'm happy to connect you with Mario if you want to.

**Rachael Tiow:** to do so, I'll talk to him when it's midnight in Dublin.

**Rachael Tiow:** Do me a favor, Adobe Journey Optimizer.

**Kyle Gaudreau:** Adobe and their names.

**Rachael Tiow:** Sorry man, just the fact that it's Adobe, I was like, it's Buick trying to make electric cars.

**Kyle Gaudreau:** I mean, they've done some good things to be fair, but I think they've fallen behind quite a bit the past handful of years, but you know, they, I haven't used it, I can certainly see if others have.

**Rachael Tiow:** Yeah, please do, please do, I want to know, I was on a demo yesterday, I asked them about signals, they couldn't answer me, and they like fumbled around, and they.

**Rachael Tiow:** said, I think, and I just was already in the mood yesterday, so I said, wait, you think or you know, I think.

**Rachael Tiow:** I said, so that means you don't know.

**Rachael Tiow:** I  hate it, salespeople, fun and lie.

**Rachael Tiow:** You think I was born yesterday?

**Kyle Gaudreau:** I would have loved a minute if I fly on the wall for that one.

**Rachael Tiow:** I came in spicy.

**Rachael Tiow:** was like, high five out of five, please.

**Rachael Tiow:** Cool, if you can do me a favor, yeah, check it.

**Rachael Tiow:** I want to know, because they're trying to buy Adobe Journey Optimizer, thinking there'll be some ABX, PipeGen, Accelerator tool, yada, yada, yada.

**Rachael Tiow:** And when I saw that, the demo yesterday, I thought, okay, guys, this is no different than Sixth Sense.

**Rachael Tiow:** Like, if we were really using Sixth Sense, it does the same thing.

**Rachael Tiow:** So why, I don't know.

**Rachael Tiow:** But anyway, if you got some feedback, would greatly appreciate it.

**Kyle Gaudreau:** For sure, sounds cool.

**Rachael Tiow:** All right, thank you all so much.

**Rachael Tiow:** Sydney, matane.

**Rachael Tiow:** I don't know what it, what is, see you later in Tagalog.

**Rachael Tiow:** Oh, Malay is, hmm?

**Sydney Arin Go:** We just use English.

**Sydney Arin Go:** I feel like we're speaking like different languages at any given moment.

**Rachael Tiow:** I see.

**Rachael Tiow:** Okay, okay.

**Rachael Tiow:** Well, in Malay, it is Jumpa Lagi, so Jumpa Lagi.

**Sydney Arin Go:** It's just a point that Malay sounds a lot like Filipino.

**Rachael Tiow:** It does.

**Rachael Tiow:** It's actually, there's a word for that language, but they're very similar.

**Rachael Tiow:** Actually, it's really similar to it.

**Rachael Tiow:** Like, if you look at the Maori language, the Hawaiian language, and the Malay language, there's actually a lot of similarities.

**Rachael Tiow:** So the one that I know of at the moment is, elua is tu in Hawaiian.

**Rachael Tiow:** The word in Maori is actually very similar too, but in Malay is dua, elua, dua, sounds similar, right?

**Sydney Arin Go:** The loa for us.

**Sydney Arin Go:** if you look

**Sydney Arin Go:** This is very, very, very similar.

**Rachael Tiow:** world of the brown people.

**Kyle Gaudreau:** Well, safe travels.

**Rachael Tiow:** Thank you, guys.

**Kyle Gaudreau:** Hope you all have a fruitful journey.

**Rachael Tiow:** Thank you, thank you.

**Rachael Tiow:** We'll talk soon.

**Rachael Tiow:** Thanks, everyone.

**Kyle Gaudreau:** See ya.

**Sydney Arin Go:** Bye.

**Kyle Gaudreau:** Bye.
