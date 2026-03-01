# Ifeoluwa / William - Turnstile content review

<metadata>
date: 2026-01-12
time: 15:29 UTC
duration: 32 minutes
organizer: William Leborgne (GrowthX)
participants:
  - Ifeoluwa Adekoya (GrowthX)
  - William Leborgne (GrowthX)
fathom_recording_id: 113470006
fathom_url: https://fathom.video/calls/528305493
share_url: https://fathom.video/share/MX5bemMBZwwXygxXKGWXsNQwzeAZ2Q7u
source: fathom
enriched_on: 2026-02-28T12:00:00 UTC
</metadata>

---

## Summary

William and Ifeoluwa diagnosed a systemic issue with Turnstile's content: feedback consistently targets perspective gaps, not just accuracy problems. They decided to pause production and consolidate client feedback into a shared POV document for Turnstile to validate, then build a "Turnstile Positioning Checker" step into the Atlas pipeline to prevent similar misalignments.

---

## Context

Turnstile is a B2B CPQ/Quote-to-Cash solution. GrowthX is producing their content strategy and writing, starting with nine articles across various Quote-to-Cash topics. Early feedback from Seema (Turnstile) and Jordan (likely their lead stakeholder) revealed that Turnstile's perspective on their positioning, industry nuances, and audience isn't being fully captured in the output. This isn't an Atlas pipeline failure—it's a knowledge gap at the input stage. The kickoff and product deep dive didn't surface all the nuanced perspective details needed for authentic, client-aligned content. William recently joined GrowthX with deep content strategy and LLM expertise, making this his first project. Ifeoluwa has been at GrowthX since August 2025 and has worked with accounts requiring deep market niche understanding (e.g., Hyper Exponential). Both recognized that continuing to iterate tactically on articles won't fix the underlying perspective misalignment.

---

## Relevance

- **Strategy Shift:** Demonstrates shift from rapid production to deliberate knowledge capture—critical for high-touch, high-POV clients like Turnstile.
- **Process Innovation:** Introduction of "Turnstile Positioning Checker" step reflects learnings on how Atlas workflows handle perspective-heavy content.
- **Collaboration Model:** Shows how senior content strategists (William) and dedicated execution leads (Ifeoluwa) align on client needs, avoiding siloed feedback loops.
- **Risk Mitigation:** Preventing repeated rework cycles by validating foundational perspective before scaling production.
- **Pipeline Evolution:** Testing new validation steps in Claude before proposing them to engineering—low-risk way to improve Atlas effectiveness.

---

## Overview

- **Problem:** Turnstile content consistently misses the client's POV, not just having accuracy issues. This requires a strategic fix, not just tactical edits.
- **Solution:** Pause production to "slow down to speed up." The immediate goal is to define the client's POV in a shared doc for their validation.
- **Long-Term Fix:** Once the POV is validated, create a "Turnstile Positioning Checker" step in the Atlas pipeline to hardcode their perspective and prevent future errors.
- **Immediate Action:** William will review all 9 articles and artifacts to provide a fresh perspective, while Ifeoluwa will consolidate all feedback into a single doc.

---

## Key Topics

### Problem: Content Misses Turnstile's POV

  - Turnstile's feedback, especially from Seema and Jordan, is highly specific to their perspective, not just grammar or accuracy.
  - This indicates a systemic issue with understanding their core POV, not a simple pipeline error.
  - **Example Feedback:**
      - "This is not our perspective."
      - "We are sacrificing depth for brevity."
      - "We are missing key distinctions and information."
  - **Root Cause:** The initial kickoff and product deep dive did not fully capture the client's nuanced perspective.

### Solution: Define & Validate POV

  - **Strategy:** Pause production to focus entirely on defining the client's POV.
  - **Process:**
    1.  **Consolidate Feedback:** Ifeoluwa will create a shared Google Doc with all feedback from the 9 articles.
    2.  **Analyze & Synthesize:** William will review all content and artifacts, then synthesize the client's POV into the shared doc.
    3.  **Client Validation:** Send the POV doc to Turnstile for review by EOD today.
          - **Goal:** Get explicit confirmation and push for more details to ensure a complete understanding.

### Long-Term Fix: "Turnstile Positioning Checker"

  - **Plan:** Once the POV is validated, create a new step in the Atlas pipeline.
  - **Step Name:** "Turnstile Positioning Checker"
  - **Function:** This step will validate generated content against the client's specific POV before SEO meta-tag generation.
  - **Implementation:**
    1.  **Test in Claude:** First, prototype the checker's logic using Claude to ensure it works.
    2.  **Propose to Engineering:** If successful, propose adding the step to the Atlas pipeline.

---

## Action Items

**William Leborgne (GrowthX)**
- Create shared Google Doc consolidating Turnstile POV; add notes; send to Seema/Jordan EOD Jan 12
- Review all 9 Turnstile articles and artifacts; rewatch Quote-to-Cash recording; synthesize POV insights into shared doc
- Schedule follow-up sync with Ifeoluwa for Jan 12 PM to finalize POV doc before client handoff

**Ifeoluwa Adekoya (GrowthX)**
- Consolidate feedback from all 9 Turnstile articles into shared Google Doc; prepare for William's analysis and synthesis
- Create Claude-based POV checker prompt; test effectiveness on Turnstile articles; if successful, propose "Turnstile Positioning Checker" step to engineering team
- Update Turnstile writing guidelines: standardize "Quote-to-Cash" formatting with en-dash; document keyword-title constraints; provide alternate title examples
- Schedule follow-up sync with William for Jan 12 PM to review finalized POV doc before client handoff

---

## Transcript
**Ifeoluwa Adekoya:** Hello!

**Ifeoluwa Adekoya:** Hi, William.

**William Leborgne:** How are you doing?

**Ifeoluwa Adekoya:** I'm not so good, but I'm alright.

**William Leborgne:** What's going on?

**William Leborgne:** Why are not so good?

**Ifeoluwa Adekoya:** Yeah, I'm at least so unwell.

**Ifeoluwa Adekoya:** I think I caught the flu or something.

**William Leborgne:** Oh, I'm sorry.

**William Leborgne:** Yeah, it's definitely coming around.

**William Leborgne:** I hear a lot of people having the flu at the moment.

**Ifeoluwa Adekoya:** Yeah.

**Ifeoluwa Adekoya:** Well, to be fair, I did come into contact with a couple of relatives that came from the U.S.

**Ifeoluwa Adekoya:** like last week or so.

**William Leborgne:** Got it.

**William Leborgne:** Okay.

**William Leborgne:** Sorry to hear that.

**Ifeoluwa Adekoya:** Transatlantic illness.

**William Leborgne:** Yeah, yeah, yeah.

**William Leborgne:** That'll hit you even harder because it's, you know, it's the viruses that you don't have and where you are.

**Ifeoluwa Adekoya:** By the way, where are you based?

**William Leborgne:** Nigeria.

**William Leborgne:** Nigeria.

**William Leborgne:** Amazing.

**William Leborgne:** Okay.

**William Leborgne:** Very cool.

**William Leborgne:** I lived for two years in Senegal.

**Ifeoluwa Adekoya:** Really?

**William Leborgne:** Yeah.

**Ifeoluwa Adekoya:** That's so cool.

**Ifeoluwa Adekoya:** I've never been.

**Ifeoluwa Adekoya:** I have a couple of friends living around there.

**William Leborgne:** Okay.

**Ifeoluwa Adekoya:** So in fact, can't remember what the African map looks like, but I think Uganda should be close to Senegal.

**Ifeoluwa Adekoya:** Okay.

**William Leborgne:** Yeah, yeah.

**William Leborgne:** Nice, nice.

**William Leborgne:** Well, I mean, as you know, Senegal is French-speaking, but right in the middle of Senegal is Gambia, and Gambia is English-speaking, so there's like a mixture.

**William Leborgne:** Yeah.

**William Leborgne:** Yeah, yeah.

**William Leborgne:** Interesting.

**William Leborgne:** I'd love to, just to kick things off, get to know you a little bit better.

**William Leborgne:** I'm also happy to share a little bit about myself.

**William Leborgne:** I feel like that's a good way to start since we're going to be working together on this project, and then we can go into the specifics of like the, you know, the writing and stuff.

**William Leborgne:** But yeah, if you don't mind, would you mind sharing a little bit about your background and anything you want to share?

**Ifeoluwa Adekoya:** Yeah, sure.

**Ifeoluwa Adekoya:** That sounds really good.

**Ifeoluwa Adekoya:** My name is Ifeoluwa, as you know.

**Ifeoluwa Adekoya:** You can call me.

**Ifeoluwa Adekoya:** My name translates to love of God.

**William Leborgne:** Oh, beautiful.

**Ifeoluwa Adekoya:** Yeah, Ife means love.

**Ifeoluwa Adekoya:** So every time you see Ife means love.

**William Leborgne:** Okay.

**Ifeoluwa Adekoya:** Yeah, like I mentioned, I live in Nigeria.

**Ifeoluwa Adekoya:** I've lived in Nigeria for like all my life.

**Ifeoluwa Adekoya:** I have about five, six years now of content experience.

**Ifeoluwa Adekoya:** I started out as a content writer in 2020, mostly doing freelance content of Fiverr and Upwork, stuff like that.

**Ifeoluwa Adekoya:** It wasn't until 2021, I transitioned into academic writing and really built my chops around research.

**William Leborgne:** Okay.

**Ifeoluwa Adekoya:** I really well.

**Ifeoluwa Adekoya:** Then in late 2020 and so on, I transitioned into marketing writing, that's SEO writing.

**Ifeoluwa Adekoya:** And I worked at the USAJT.

**Ifeoluwa Adekoya:** From late 2021 to mid-2023, we're now transitioned into tech marketing.

**Ifeoluwa Adekoya:** I worked with a personal finance, well, one of the biggest personal finance companies here in Nigeria and West Africa, to be fair.

**Ifeoluwa Adekoya:** I worked with them as an SEO strategist from 2023 to late 2025.

**Ifeoluwa Adekoya:** So right now, I still work with them, but mostly like on a consulting business.

**William Leborgne:** Okay, got it.

**William Leborgne:** Cool.

**William Leborgne:** So as an SEO strategist, you really own the full experience from like what keywords you should be going after, what are the gaps, what are the competitors doing?

**William Leborgne:** You've done all that stuff.

**Ifeoluwa Adekoya:** Okay.

**Ifeoluwa Adekoya:** Yeah, yeah.

**William Leborgne:** And so it.

**William Leborgne:** Cool.

**William Leborgne:** And how long have you been with GrowthX?

**Ifeoluwa Adekoya:** I joined August, last year, late August.

**William Leborgne:** So that's six months?

**William Leborgne:** Yeah.

**William Leborgne:** Five, six months?

**William Leborgne:** Something like that.

**William Leborgne:** Okay, got it.

**William Leborgne:** Okay.

**William Leborgne:** And you weren't always doing sprints, right?

**Ifeoluwa Adekoya:** Or have you been with sprints the whole time?

**Ifeoluwa Adekoya:** Yeah, like from day one, I've been in sprints.

**William Leborgne:** With sprints?

**William Leborgne:** Okay.

**Ifeoluwa Adekoya:** I've been fortunate to always be assigned to really interesting accounts.

**Ifeoluwa Adekoya:** The first account I was assigned to is Hyper Exponential.

**Ifeoluwa Adekoya:** And I was even surprised.

**Ifeoluwa Adekoya:** They transitioned into like, they converted.

**Ifeoluwa Adekoya:** And I was really excited because the account was quite difficult.

**Ifeoluwa Adekoya:** Trying to know their USB and know their tone of voice.

**Ifeoluwa Adekoya:** And especially because they are very, very niche.

**Ifeoluwa Adekoya:** Very, very niche product, very niche audience, very, very niche positioning.

**Ifeoluwa Adekoya:** It shows a lot of things.

**Ifeoluwa Adekoya:** Yeah, we're to crack that.

**William Leborgne:** Okay, cool.

**William Leborgne:** Cool.

**William Leborgne:** Thanks for sharing all that.

**William Leborgne:** I will share a little bit about myself.

**William Leborgne:** I am half French, half American.

**William Leborgne:** My father is French.

**William Leborgne:** And I grew up kind of moving around.

**William Leborgne:** My whole life.

**William Leborgne:** So mostly in Europe, but also a little bit.

**William Leborgne:** Asia.

**William Leborgne:** And then when I started my career, I was living in Madrid, Spain, and I was working in brand management.

**William Leborgne:** And then I did the Peace Corps, which is how I ended up in Senegal for two years.

**William Leborgne:** And then I moved to the States.

**William Leborgne:** And so I only actually moved to the States when I was 28.

**William Leborgne:** So I was very late to moving out there, even though I'm half American, I'd never lived there before.

**William Leborgne:** And then I spent like 12 years, 11 or 12 years in the States.

**William Leborgne:** And at the time, was, you know, prior to that, was always kind of like playing around, seeing where I want to live and what experiences I want to have.

**William Leborgne:** My career kind of came second.

**William Leborgne:** I was very much more exploring, like, what interests me?

**William Leborgne:** Do I want to work in, you know, NGOs and more of that space, which is why I did the Peace Corps?

**William Leborgne:** Or do I want to work in this space?

**William Leborgne:** And I kept trying different things.

**William Leborgne:** So the last thing I tried was, yeah, when I was around 28, I worked.

**William Leborgne:** In the music industry in Los Angeles, I worked at a record label, and I did that for a couple years, and then I realized I really didn't like the bureaucracy, and I'm a big, big fan of music, and thought that that's what I wanted to do with my career, but then realized, no, this is not the right thing, and then I fell into technology, and then I never looked back.

**William Leborgne:** At that point, I was like, oh, I love this stuff, like the pace, how dynamic it is, it's really much more about meritocracy, you know, if you're good at something, they'll give you more stuff to do, versus kind of the hierarchy of older companies, so I really enjoyed that, and I've been working now for, yeah, over a decade across lots of different startups.

**William Leborgne:** I started my own boutique content agency as well, like six years ago, and was doing some work on the side, worked with clients like Credit Karma and TikTok, and then most of the time was always like trying to, you know, work out interesting.

**William Leborgne:** Companies.

**William Leborgne:** I was primarily the main SEO content marketing person in every company I worked at.

**William Leborgne:** So I would arrive and I would build a team of freelance writers, often on Upwork and Fiverr, and then build out systems and we would create content.

**William Leborgne:** And then in the last company I was at, I had a team of eight, most of which were freelancers.

**William Leborgne:** There was two full-time people, but most of them were freelancers.

**William Leborgne:** And we just produced lots of high-quality content for the company I was working at.

**William Leborgne:** And I discovered Aerofs back in December of last year, of the previous year, so 2023.

**William Leborgne:** And then in 2024, early 2024, I managed to convince my company to get Aerofs.

**William Leborgne:** And so I went really deep into the space.

**William Leborgne:** But I would say, broadly speaking, everything to do with ChadGBT or LLMs in general, as soon as it came out into the world, I was hooked.

**William Leborgne:** I was like, this is the sh**.

**William Leborgne:** That's that I love.

**William Leborgne:** Because I think I'm much more of a, generally speaking, I'm much more of a big picture person, more strategy, more structure, and less of like in the minutia.

**William Leborgne:** That's, I can do it, of course, like you have to, if you're going to be a content person, but it's not what I love the most.

**William Leborgne:** It's, in fact, why my wife and I get along really well, because she's very detailed, very researcher, and I'm much more like make decisions quickly, move fast, have momentum, you know.

**William Leborgne:** Yeah, yeah.

**William Leborgne:** So that's, so that's, that's basically my background.

**William Leborgne:** And like, I've only been at, at growthx a little less than a month.

**William Leborgne:** And I was hired in large part because of my background using air ops and sort of my, you know, my many years of content strategy work, working with lots of different companies.

**William Leborgne:** Yeah, that's, that's pretty much it.

**Ifeoluwa Adekoya:** Any questions?

**Ifeoluwa Adekoya:** That's, I was going to ask why you went to Senegal.

**Ifeoluwa Adekoya:** But when you mentioned that you had, like, French roots, I was like, oh, okay, no problem.

**Ifeoluwa Adekoya:** Because when you say French roots, so there's this joke that we always make, like, Australia, Nigeria, and West Africa, that when you say white man in, like, certain countries, you're like, oh, are you the CIA?

**William Leborgne:** Are you the CIA?

**William Leborgne:** Yeah, yeah, yeah.

**William Leborgne:** You're either CIA or you're Peace Corps.

**William Leborgne:** Yes, exactly.

**Ifeoluwa Adekoya:** I think that that's very impressive.

**Ifeoluwa Adekoya:** I know we've only, like, interacted a couple of times in Slack and, like, over meetings and stuff, but I think you're, I don't think, I know for the fact that your experience shines through, and I'm really, really excited to be working with you, like, hand-in-hand on Turnstile.

**Ifeoluwa Adekoya:** Surely because, you know, they are sending us, like, tons of feedback.

**Ifeoluwa Adekoya:** And I also like the fact that you understand that we are calibrating.

**Ifeoluwa Adekoya:** I remember when first went to GrowthX, I would get feedback from clients, I would be like, oh, my God, I'm doing really awful things.

**Ifeoluwa Adekoya:** Yeah, we don't get feedback.

**William Leborgne:** Exactly.

**William Leborgne:** And honestly, like, everyone's got the same feeling.

**William Leborgne:** When I saw SEMA's, you know, last comments, I was like, okay, you know, that doesn't feel good to see.

**William Leborgne:** But at the same time, like, exactly, that's exactly right.

**William Leborgne:** And that's what I also said in the beginning.

**William Leborgne:** was like, this is calibration.

**William Leborgne:** But what this does tell me, and every client is different, right?

**William Leborgne:** There was another client that started at the same time, BlackSoul, and they're totally the opposite, right?

**William Leborgne:** They're very technical, but they have no strong feelings about how content should be.

**William Leborgne:** Seema and Jordan have very strong feelings about how content should be.

**William Leborgne:** Not only that, but they have a very strong identity of what their perspective is supposed to be.

**William Leborgne:** And that's the hardest part, right?

**William Leborgne:** A lot of their comments are not, you know, this is poorly written.

**William Leborgne:** They're saying this is not our perspective.

**William Leborgne:** And that's extremely hard to do.

**William Leborgne:** So anyway, all to say, I think, and we can transition straight into this.

**William Leborgne:** I think the core element that we're going to need to do, or core philosophy, I think.

**William Leborgne:** For this week is we need to slow down in order to speed up.

**William Leborgne:** Like I know that the goal is to be at this point already doing a high level of production, but I don't think that helps us.

**William Leborgne:** And it certainly doesn't help us in the eyes of the client.

**William Leborgne:** I think what we do is we spend the rest of this week just focusing on the nine pieces that we've given them so far, the first three and the next six, just getting them to the best place possible.

**William Leborgne:** So that's where I think like you and I need to spend some time.

**William Leborgne:** I actually need to go in and like really read through all these pieces and all the comments myself.

**William Leborgne:** But broadly speaking, I'd love to know a little bit more about like, have you had a chance to read the comments already?

**Ifeoluwa Adekoya:** Yes, yes.

**Ifeoluwa Adekoya:** So whenever I get comments from them, I just duplicate the entire doc in case I like start working on the robot so I can compare both versions to see, okay, what are their comments like?

**Ifeoluwa Adekoya:** What can we basically improve?

**Ifeoluwa Adekoya:** And I noticed that what you mentioned before, where we're still a little off when it comes to their perspective.

**Ifeoluwa Adekoya:** I know we also have accuracy issues.

**Ifeoluwa Adekoya:** I know that accuracy issues can definitely be fixed, either with pipeline improvements or by maybe reducing the amount of instructions we're giving to the pipeline right now.

**Ifeoluwa Adekoya:** But for perspective, we need to go back and basically check out the aspects and make sure, okay, are we seeing the right things?

**Ifeoluwa Adekoya:** Because she's been mentioned, excuse me, Sima has mentioned so many things about it, the product positioning and their stance on certain parts of the product or the industry and even as regards to the audience.

**Ifeoluwa Adekoya:** So we need to make sure, where's the problem coming from?

**Ifeoluwa Adekoya:** Are we having clashes between artifacts?

**Ifeoluwa Adekoya:** Maybe the company context is different from what our target audience is saying.

**Ifeoluwa Adekoya:** Do we need to go deep into the writing guidelines?

**Ifeoluwa Adekoya:** And make sure things are all right.

**Ifeoluwa Adekoya:** So.

**Ifeoluwa Adekoya:** I'll say, I was going to suggest the same thing, that can we just go down a little, like, let's actually read these things to make sure we're looking good.

**Ifeoluwa Adekoya:** I can fix this right now.

**Ifeoluwa Adekoya:** We can use Claude or even Atlas to, like, fix the articles based on their comments, and they will look good.

**Ifeoluwa Adekoya:** But we're also having the same issues in the next round now.

**William Leborgne:** Exactly.

**Ifeoluwa Adekoya:** We're having the same issues again and again and again.

**William Leborgne:** Yeah, I remember one of the MEs saying, I don't remember who it was, but it was during one of the meetings, and she was like, yeah, I will spend three hours in Atlas fixing it when it would take me half an hour to fix the article.

**William Leborgne:** But she's like, the reason why is because of exactly what you said.

**William Leborgne:** So I have two questions.

**William Leborgne:** One is, what can I do to help facilitate this?

**William Leborgne:** Just, like, broadly speaking, would you like another set of eyes to review everything and share feedback?

**William Leborgne:** Do you want me to try and get into Atlas?

**William Leborgne:** Like, how can I help?

**Ifeoluwa Adekoya:** Yeah, I was going to actually, thank God, thank God you volunteered.

**Ifeoluwa Adekoya:** I was going to say, I just really need a fresh feel of eyes.

**Ifeoluwa Adekoya:** I think looking at all the artifacts day after day, I've become a little, like, slightly numb.

**Ifeoluwa Adekoya:** Yeah.

**Ifeoluwa Adekoya:** So I just would like for you to review, especially because their niche is, or their industry is core to cash.

**Ifeoluwa Adekoya:** If you can just check out the core to cash version of the CPQ piece, and also check out, like, a couple of the artifacts.

**Ifeoluwa Adekoya:** I know it might take a couple of, maybe an hour or two for you to just review.

**William Leborgne:** Yeah, yeah, that's fine.

**Ifeoluwa Adekoya:** Yeah, there's going to be a general article.

**William Leborgne:** So what I'm going to do is I'm going to review the turnstile articles and write down my own notes on it.

**Ifeoluwa Adekoya:** Yeah.

**William Leborgne:** My own notes.

**William Leborgne:** Maybe actually we should have a shared document with notes.

**Ifeoluwa Adekoya:** All right.

**William Leborgne:** Like, as we're looking at it, it might not be a bad idea just to have a Google Doc that we, that we, you both use, and we just put, like, thoughts and notes based off of the feedback.

**William Leborgne:** That way, I'm not repeating the same thing.

**William Leborgne:** And then the second thing you said is then review the artifacts, correct?

**Ifeoluwa Adekoya:** Yes.

**Ifeoluwa Adekoya:** I'm going to make a copy of the article now and just answer it.

**Ifeoluwa Adekoya:** So I'm going to retain the comments and suggestions.

**William Leborgne:** Because I also, I know that the, there were quite a lot of comments from Jordan in the last one, the, the, what is cash to, to, what was it?

**William Leborgne:** What is cash to quote article?

**Ifeoluwa Adekoya:** think it was.

**William Leborgne:** Quote to cash.

**William Leborgne:** Sorry.

**William Leborgne:** Cash to quote.

**William Leborgne:** So what is quote to cash article?

**William Leborgne:** was a lot of comments.

**William Leborgne:** And I remember you also saying, like leaving some comments, like asking, like, why, what, what's, you know, asking for further iteration, which I don't believe he's ever responded to, right?

**Ifeoluwa Adekoya:** No, he hasn't.

**Ifeoluwa Adekoya:** So he gave direction.

**Ifeoluwa Adekoya:** So he gave direction and I made the fixes, but I just wanted to confirm that, okay, this position that you mentioned, or are we doing it right?

**Ifeoluwa Adekoya:** Yeah.

**Ifeoluwa Adekoya:** But to be fair, the meeting that you had with the team last week did confirm that.

**Ifeoluwa Adekoya:** Um.

**Ifeoluwa Adekoya:** Where my fixes were right, were correct.

**William Leborgne:** Okay, great.

**William Leborgne:** Okay, so I think, I think what, because I almost feel like the Quote to Cash article is a little bit of like the Bible, or at least for part of it, it's the baseline, it's the foundation of what their perspective is.

**William Leborgne:** So I think what I'm also going to do is I'm going to rewatch parts of that recording as well to absorb more of it.

**William Leborgne:** Let me watch part of that.

**William Leborgne:** Okay, cool.

**William Leborgne:** And we have 10 minutes left.

**William Leborgne:** Would you be open to just sharing your screen, opening your doc, and just starting to share some of your initial thoughts on this?

**William Leborgne:** Because this is all new to me.

**William Leborgne:** So, like, I mean, the process of growthx.

**William Leborgne:** So I would love to just, you can just talk through it as you're going.

**William Leborgne:** But if you were to look at a comment, for instance, and say, okay, I'm going to turn this into...

**William Leborgne:** into a prompt, or I'm going to update the prompt, like, this is how my, this is my thinking process, just so I can understand your process of how you absorb this stuff.

**Ifeoluwa Adekoya:** All right, so give me a sec.

**Ifeoluwa Adekoya:** Okay.

**Ifeoluwa Adekoya:** Nice.

**Ifeoluwa Adekoya:** So my process for fixing things is usually, I try to take all their comments and put it back into the pipeline, because the pipeline, Atlas learns from comments and interactions that we give to it.

**Ifeoluwa Adekoya:** So, for example, this wording that she mentioned is a little awkward, I wouldn't change this, mostly because this is, it's a keyword.

**Ifeoluwa Adekoya:** So I'll just, I'll just leave a note on it.

**Ifeoluwa Adekoya:** Okay, it's going to be a little awkward sometimes, surely in meta, in our metadata, and even in our H1, because we are trying to get the exact keyword match to rank search.

**Ifeoluwa Adekoya:** But for stuff that she mentioned about, maybe, like, grammar, those are like minor edits, those are fine.

**Ifeoluwa Adekoya:** And things like, oh, these are like stuff.

**Ifeoluwa Adekoya:** But the things I'm really, really concerned about is turnstiles POV.

**Ifeoluwa Adekoya:** Because we can fix accuracy, we can fix everything, but we need their feedback to make sure we're nearly positioned right.

**Ifeoluwa Adekoya:** So I'll the major issue I've noticed right now is that our positioning is still a bit tough.

**Ifeoluwa Adekoya:** For accuracy, we can always figure out about what, for POV, we're still a little off here.

**Ifeoluwa Adekoya:** We need to make sure, okay, who exactly are we speaking to?

**Ifeoluwa Adekoya:** The way, is there a turnstile approach to quote-to-cash that we're missing out on?

**Ifeoluwa Adekoya:** Because quote-to-cash is broad and the industry we're working in is very broad.

**Ifeoluwa Adekoya:** And it could be just with a very tiny niche or a very specific audience.

**Ifeoluwa Adekoya:** Another thing I'm going to note here is making sure we're not missing out on key metrics and trying to be SEO friendly.

**Ifeoluwa Adekoya:** So I did not...

**Ifeoluwa Adekoya:** She left like tons of comments on the table and said, okay, we mentioned things are overlapping and we are not explaining.

**Ifeoluwa Adekoya:** Are we sure that we're not missing out on like key distinctions and key information and also make sure we're not sacrificing, let's say, depth for brevity.

**William Leborgne:** Yes, yes, yes, yes.

**William Leborgne:** Yeah.

**William Leborgne:** Okay.

**William Leborgne:** I get you.

**Ifeoluwa Adekoya:** Uh-huh.

**Ifeoluwa Adekoya:** Yeah.

**Ifeoluwa Adekoya:** So what else?

**Ifeoluwa Adekoya:** What else?

**Ifeoluwa Adekoya:** So some AI wordings that she mentioned.

**Ifeoluwa Adekoya:** Again, those ones are not really big red flags like that.

**Ifeoluwa Adekoya:** They are things that we can always fix.

**Ifeoluwa Adekoya:** But I'll say the one thing I'm trying to make sure where it gets right is first and foremost, the positioning, POV, Tonstow's POV.

**Ifeoluwa Adekoya:** We want to make sure it's correct.

**Ifeoluwa Adekoya:** I also want to make sure that I wish that we have as much information as we need from them.

**Ifeoluwa Adekoya:** It could also be a situation where we've, the only thing we've mentioned is, okay, Tonstow is for B2B, sales like B2B.

**William Leborgne:** Mm-hmm.

**Ifeoluwa Adekoya:** But is there another angle that we are missing that is making our articles just seem a little bit off?

**Ifeoluwa Adekoya:** So I'll say that to make sure we're good.

**Ifeoluwa Adekoya:** And also, like, specifics when it comes to speaking about each topic we're writing around.

**Ifeoluwa Adekoya:** Like, are we, again, missing the mark when it comes to a blend of positioning and accuracy?

**Ifeoluwa Adekoya:** So, like you mentioned, it's not when it breaks down, it's when you haven't implemented a proper code to cache process.

**Ifeoluwa Adekoya:** So, is this an accuracy problem?

**Ifeoluwa Adekoya:** Is this a positioning problem?

**Ifeoluwa Adekoya:** Just like, investigate it.

**Ifeoluwa Adekoya:** So, that's why I mostly, whenever I get comments, I try to first check out everything before I start working on it.

**Ifeoluwa Adekoya:** Essentially, because whatever we do right now doing strategy sprints is going to impact what goes on if the client converts.

**Ifeoluwa Adekoya:** So, I like to imagine that they get to work right now.

**Ifeoluwa Adekoya:** the team that thinks over is doing less work and they're doing better work, not to worry too much about.

**Ifeoluwa Adekoya:** Quality or position or anything else.

**Ifeoluwa Adekoya:** We just keep working with it.

**William Leborgne:** Yeah, yeah.

**Ifeoluwa Adekoya:** I'm with you.

**Ifeoluwa Adekoya:** Yeah, I'll say those are things I basically will check out.

**Ifeoluwa Adekoya:** And obviously she did mention, she also did mention a couple of things that definitely were not included in artifacts, but things that may be just specific to the clients.

**Ifeoluwa Adekoya:** Like, let's not admit this.

**Ifeoluwa Adekoya:** This is very valuable feedback.

**Ifeoluwa Adekoya:** But stuff like that.

**Ifeoluwa Adekoya:** So I'll say to be fair, CMS feedback has been really, really great, like really, and really, really appreciated.

**Ifeoluwa Adekoya:** But I still think it's just calm down, check everything over, get a fresh pair of eyes, like your pair of eyes, make sure that we are aligned and okay, try and figure things out.

**Ifeoluwa Adekoya:** Is it issues with the artifacts?

**Ifeoluwa Adekoya:** Do we need to expand the artifacts?

**Ifeoluwa Adekoya:** we need to correct stuff in the artifacts?

**Ifeoluwa Adekoya:** Or do we need to like maybe go back to the pipeline and make sure that the pipeline is working as it should?

**Ifeoluwa Adekoya:** Or it could also be like, should we give less directions or more directions to Atlas?

**William Leborgne:** Yeah.

**William Leborgne:** Okay.

**William Leborgne:** Okay, cool.

**William Leborgne:** All right.

**William Leborgne:** This is super helpful.

**William Leborgne:** So a couple of thoughts that came up for me.

**William Leborgne:** There's the baseline artifacts, which is your company context, your writing guidelines, and your audience information, right?

**William Leborgne:** Those are kind of the three big ones.

**William Leborgne:** And I know from my very, very limited knowledge, I just got a quick walkthrough from Sydney on like what Atlas looks like and studio looks like and how they interact.

**William Leborgne:** But my understanding is two things.

**William Leborgne:** One is there are many pieces to the flow with an Atlas, and you can add pieces that are kind of custom for that client.

**William Leborgne:** But, and this is the second thing I know, but you don't want it to be too long or too complex because then the thing breaks down, because then maybe...

**William Leborgne:** Maybe there's things that conflict with each other where it just overwhelms the system.

**William Leborgne:** So with that in mind, because unlike other clients, this client does have such a strong point of view that we need to figure out.

**William Leborgne:** I wonder, and you can tell me if this is off, but I wonder if we should create a step within the workflow, within the pipeline, that is a checker of their point of view.

**William Leborgne:** And in that thing, just on its own, we would put things like, quote-to-cash is something you should be thinking about from step number one.

**William Leborgne:** Not when you had three or four clients and 20 to 30 invoices, but it should be from step one.

**William Leborgne:** Second point of view thing would be like, it's not one person that's doing it.

**William Leborgne:** It could be multiple people in the company.

**William Leborgne:** It could be the CEO.

**William Leborgne:** It could be your chief finance officer.

**William Leborgne:** could be blah, blah, blah, blah, right?

**William Leborgne:** We start to build some building blocks of their point of view, based off of all this feedback that we got from Jordan last week and from SEMA also last week, and then build that into it and then had that be a part of the checker.

**William Leborgne:** That's where my mind is going, but if you think, no, actually it's better to put it in one of the existing ones, we could also do that.

**Ifeoluwa Adekoya:** I actually think that that will help because right now, okay, I'm going to show you what Atlas looks like for the editorial pipeline.

**Ifeoluwa Adekoya:** it searches, topic, drafts, ad school, ads, internal links, source links, validates writing guidelines, and then does fact checking to make sure things are really cool.

**Ifeoluwa Adekoya:** We could add an additional step afterwards that shows that, either afterwards or even before, that shows that we, we could also call it like a turnstile positioning checker.

**William Leborgne:** Yeah, there we go, turnstile positioning.

**William Leborgne:** And I think that's almost like it's, it's,

**William Leborgne:** After validating the writing guidelines, you know, like before the generate SEO meta titles, but literally right after the writing guidelines, then it looks at the point of view and it makes changes based off of that.

**Ifeoluwa Adekoya:** All right.

**Ifeoluwa Adekoya:** All right.

**Ifeoluwa Adekoya:** Okay.

**Ifeoluwa Adekoya:** No problem.

**Ifeoluwa Adekoya:** So what I'm going to do is this.

**Ifeoluwa Adekoya:** When I've gotten your feedback from the Aspect as well as the article I shared with you, you can comment as well.

**Ifeoluwa Adekoya:** I think I'd leave it for William.

**Ifeoluwa Adekoya:** Okay.

**Ifeoluwa Adekoya:** Yeah.

**Ifeoluwa Adekoya:** So you can just check that.

**Ifeoluwa Adekoya:** I'll leave as many comments as possible.

**Ifeoluwa Adekoya:** I'll work with Claude to see if I can whip something out.

**Ifeoluwa Adekoya:** So it will either be maybe based on a special artifact that will only be pulled at that step.

**Ifeoluwa Adekoya:** We could just create a quick artifact that will be pulled at that step.

**Ifeoluwa Adekoya:** The turnstile positioning, check, checking step.

**Ifeoluwa Adekoya:** Just make sure that, okay, the Aspect has been created.

**Ifeoluwa Adekoya:** Does it make sense?

**Ifeoluwa Adekoya:** Does it actually tick all the boxes I wanted to tick before it now goes to generate SEO tags and fact check?

**Ifeoluwa Adekoya:** make sense?

**Ifeoluwa Adekoya:** But for now, we can just work on it in Cloud, and then if it works very well in Cloud, we can suggest an improvement to the pipeline, to the engineering team.

**William Leborgne:** I think, yeah, I think we're jumping ahead.

**William Leborgne:** I think what we need to do, like we were saying at the beginning, like slow down to speed up.

**William Leborgne:** I think the first step is just, I have, let me just check my day.

**William Leborgne:** Yeah, I have some meetings.

**William Leborgne:** I have a kickoff call in a couple minutes, and then another kickoff call.

**William Leborgne:** But after that, the rest of my afternoon is free.

**William Leborgne:** So what I think we should do is really just absorb all this information, put it into like a separate shared Google Doc, where we're just writing our perspective, like what we think is their point of view.

**William Leborgne:** And put it, put it in there based off of all the comments in this document and in Jordan's ones before.

**William Leborgne:** And then once we've added a lot of these point of views, then we, then we share that with their, with their team.

**William Leborgne:** And we say, listen,

**William Leborgne:** It looks like what we're really missing is your core perspective.

**William Leborgne:** And I think what we need to do here is make sure that we're really getting this locked in.

**William Leborgne:** Based off of all the feedback we've gotten, here's some turnstile-specific point of view that I think we need to integrate into our workflow.

**William Leborgne:** Can you confirm or deny or change any of the things that Ife and I have put together for you guys?

**William Leborgne:** And we send this to them by end of day today.

**William Leborgne:** And then tomorrow, hopefully, they give us the feedback.

**William Leborgne:** And if they say, yep, this looks good, da-da-da-da-da, or I would change this, or I would add these things.

**William Leborgne:** And I'll definitely push them.

**William Leborgne:** I'll say, please add as many things into the perspective.

**William Leborgne:** And I'll be honest.

**William Leborgne:** I'll be like, listen, the kickoff and the product deep dive was helpful, but it's not the whole package.

**William Leborgne:** We're not getting everything from your brains into our brains.

**William Leborgne:** We need a second step where we're getting more information from your brains into our brains.

**William Leborgne:** And then back in

**William Leborgne:** then to get translated into the pipeline.

**William Leborgne:** So I think before you make any edits on this and send them another copy, I think we do this first step.

**William Leborgne:** And just make sure that we're, for me also, it shows to them that we're listening.

**William Leborgne:** That we're saying, okay, this is what we're understanding based off of this.

**William Leborgne:** What do you think?

**Ifeoluwa Adekoya:** Yeah, to be fair, I think that's just brilliant.

**Ifeoluwa Adekoya:** I think that, yeah, that would definitely make things easier.

**William Leborgne:** Yeah.

**William Leborgne:** Okay.

**William Leborgne:** So let's do that.

**William Leborgne:** And then the other thing that I just noted down was, I got to jump, but yeah, there was a couple of things that you showed me that were like, for me, like reframing that do maybe go into the writing guidelines.

**William Leborgne:** Oh yeah, like the simple things like the quote to cash with the dash.

**William Leborgne:** Yeah, I can tell them like that , don't worry about it.

**William Leborgne:** We'll learn and we'll put that into the writing guidelines.

**William Leborgne:** That's simple.

**William Leborgne:** We can do.

**Ifeoluwa Adekoya:** We

**William Leborgne:** I'm sorry, the very, very top, the title, so that kind of thing.

**William Leborgne:** I think in the comments, we can say this has to be in there because it's the primary keyword, but what we could always do is we can still change the title, where instead of the title is quote cash versus CPQ dash, what's the difference, right?

**William Leborgne:** Or something like that.

**William Leborgne:** If she's saying it sounds awkward, which I understand, but I think we can also educate them, although I don't know how much SEMA needs education, but anyway, to educate them and say, hey, we have to keep this, but here's an alternative.

**William Leborgne:** And so we can put that into the comment and say, here's the alternative, you know?

**William Leborgne:** And again, that way that she feels like, oh, we're listening, we're engaging, et cetera.

**William Leborgne:** I got to jump.

**William Leborgne:** I'm so sorry, but let's talk again later this afternoon, yeah?

**William Leborgne:** All right.

**William Leborgne:** Yeah, sure.

**William Leborgne:** Thank you so much, William.

**William Leborgne:** All right.

**William Leborgne:** Thanks.

**William Leborgne:** Bye.
