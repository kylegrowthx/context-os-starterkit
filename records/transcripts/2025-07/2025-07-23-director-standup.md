# Director Standup

<metadata>
date: 2025-07-23
time: 19:00 UTC
duration: 27 minutes
organizer: Megan Dickey
participants: Andi Bailey, Dave Capone, Jakub Rudnik, Mara Leighton, Megan Dickey, Matthew Panzarino, Jason Gong, Darrell Etherington
speaker_note: "Golden Gate" appears 4 times in the transcript with no matched email. Unable to determine which participant this label refers to. Likely a Fathom transcription artifact or device name. Recommend cross-referencing with Fathom recording for clarification.
fathom_recording_id: 76059375
fathom_url: https://fathom.video/calls/359470326
share_url: https://fathom.video/share/4zQysQebfLh-XjAV38QBf36nrYv1zUeo
source: fathom
enriched_on: 2026-03-03 14:35 UTC
</metadata>

---

## Summary

GrowthX directors discussed team capacity management, client deliverables, and strategic AI visibility initiatives. Matthew Panzarino is taking over new clients from Strategy Sprint (Metronome, Monograph) as workflows mature. The team redirected manual publishing tasks to Suleman (EPD requests) and is shadowing Rachel and Jesselyn to identify bottlenecks. Directors reviewed Scrunch dashboard setup for clients and explored Airbyte's ChatGPT button feature to drive AI citations. The Galileo account remains a focus — with written memos on LLM strategy being prepared for Jason's questions about search traffic impact and content ROI.

---

## Context

This is a weekly Director Standup — GrowthX's internal leadership sync for the Geo/delivery team. Directors lead clients, manage capacity, and align on strategic initiatives. The call opened with personal updates before transitioning to business items: staffing changes, client-facing tool implementations (Scrunch dashboards), and a critical ongoing account discussion with Galileo (a design/architecture SaaS client). The team is in the thick of H2 planning with clients, scaling their SEO visibility (AEO/CheckThat) work, and troubleshooting bottlenecks in content publishing workflows.

---

## Relevance

**To GrowthX Delivery:**
- Workflow optimization underway: Rachel and Jesselyn are publishing manually; shifting tasks to Suleman (EPD) to reduce director overhead and bottlenecks
- UX study approach being piloted to identify patterns in publishing process, potentially feeding engineering requests
- Panzer/Matthew successfully customizing Strategy Sprint workflows; rolling out to Metronome and Monograph clients
- Scrunch dashboards rolling out as client-facing tool; editors now have access to refine prompts, ICP data, competitor data

**To CheckThat / AI Visibility:**
- Airbyte's ChatGPT button feature explored as potential lever for forcing AI citation (adds article to ChatGPT's history, increases future references)
- Dave flagged article on button benefits; next step is securing timeline/impact data from Airbyte
- Potential to embed additional context in prompts (article title, company name) to strengthen visibility signals

**To GrowthX Business Development:**
- Galileo account represents strategic challenge: Jason (CEO) skeptical of LLM content ROI, questioning search traffic impact
- Mara preparing written memo on Geo strategy + LLM impact to address board-level concerns
- V2 Scrunch prompts shifting from informational to direct product evaluation per client feedback
- Planned Scrunch walkthrough in 3 weeks to surface data + build trust; Jackson and Connor on PTO this week

---

## Overview

- New CM hiring in progress; Panzer taking over upcoming Strategy Sprint clients
- Scrunch dashboards set up for clients; opportunity to refine prompts and data
- Airbyte's ChatGPT button implementation discussed; potential for testing and implementation
- Galileo client case study: ongoing discussions about AI/LLM strategy and content visibility

---

## Key Topics

### Team Updates and Capacity Management

  - Panzer taking over new clients from Strategy Sprint (e.g., Metronome, Monograph)
  - Potential new CM hire, either for Panzer's team or Strategy Sprint
  - Addressing capacity issues for Rachel and Jesselyn:
      - Shadowing their process to identify improvement areas
      - Shifting manual publishing tasks to Suleman (EPD requests)
      - Considering UX study approach to identify patterns and engineering needs

### Scrunch Dashboard Implementation

  - Basic dashboards set up for clients; directors now have editor access
  - Opportunity to improve:
      - Upload more prompts
      - Refine ICP and competitor data
  - Mara working on V2 prompts for Galileo, focusing on direct product evaluation

### Airbyte's ChatGPT Button Feature

  - Dave highlighted Airbyte's "Summarize with ChatGPT" button
  - Potential benefits:
      - Forces ChatGPT to review the content
      - Adds to ChatGPT's history, potentially increasing future references
  - Considerations for testing:
      - Timing of implementation (possibly Monday)
      - Potential to add extra context in the prompt (e.g., article title, company name)
  - Custom-built by Airbyte, not an OpenAI embed

### Galileo Client Case Study

  - Key stakeholders: Connor, Jackson, and Jason (CEO)
  - Ongoing discussions about AI/LLM strategy and content visibility
  - Addressing Jason's concerns:
      - AI citations vs. mentions
      - Impact of LLMs on search traffic
      - Justification for continued content production
  - Next steps:
      - Scrunch walkthrough and data review in 3 weeks
      - Preparing written responses and memos for Jason
      - Balancing information sharing for trust vs. avoiding unnecessary complexities

---

## Action Items

**Dave Capone (GrowthX)**
- Check if any CMs publishing manually; redirect to EPD requests if so
- Share article about ChatGPT button benefits in Slack

**Mara Leighton (GrowthX)**
- Check if any CMs publishing manually; redirect to EPD requests if so
- Draft memo w/ written responses to Jason's (Galileo) questions on Geo strategy & LLMs
- Meet w/ Andrew from Scrunch re: V2 prompts for Galileo, incorporate Jason's feedback
- Share Scrunch prompts w/ Galileo + record Loom video explaining prompt selection rationale

**Megan Dickey (GrowthX)**
- Check if any CMs publishing manually; redirect to EPD requests if so

**Jakub Rudnik (GrowthX)**
- Check if any CMs publishing manually; redirect to EPD requests if so

---

## Transcript
**Megan Dickey:** Hey, Jakub.

**Jakub Rudnik:** What's up?

**Megan Dickey:** Is that a dog or a cat?

**Megan Dickey:** Doesn't it look like...

**Jakub Rudnik:** It's just my bag.

**Jakub Rudnik:** It's my laptop bag.

**Jakub Rudnik:** I'm going to move it now.

**Jakub Rudnik:** I thought it blurred in the background.

**Jakub Rudnik:** It did look very black cat-like.

**Megan Dickey:** Yeah.

**Megan Dickey:** Handy.

**Andi Bailey:** Hello.

**Megan Dickey:** Hello.

**Jakub Rudnik:** Excited to get this office all flipped around for staging.

**Jakub Rudnik:** All that, and there's no way I'm going to, like, redecorate or anything.

**Jakub Rudnik:** So I'm excited to get to a place where it's not, like, in a holding pattern.

**Jakub Rudnik:** You can do what I want again.

**Megan Dickey:** Wait, are you?

**Jakub Rudnik:** Because you haven't moved yet.

**Megan Dickey:** No, two months from now.

**Jakub Rudnik:** So we're having an offer.

**Jakub Rudnik:** It's accepted.

**Jakub Rudnik:** But they're doing all the instruction stuff.

**Megan Dickey:** Thank you.

**Jakub Rudnik:** But until that's, like, done and processed, then we won't change anything.

**Jakub Rudnik:** And then even then, it's not like I'm going to go put...

**Jakub Rudnik:** Thank you.

**Jakub Rudnik:** My stuff back up are just waiting, so weird.

**Megan Dickey:** Yeah, for sure.

**Megan Dickey:** Hey, Mara.

**Mara Leighton:** Hey, how's it going?

**Megan Dickey:** Pretty good.

**Mara Leighton:** How are you doing?

**Mara Leighton:** I have definitely complained about this before, but I haven't had a fridge for about a month.

**Andi Bailey:** A month?

**Mara Leighton:** A month.

**Mara Leighton:** What?

**Mara Leighton:** I could talk about this for, like, three hours, but the company, Big Mike's, who's supposed to come test, not even replace, but just test the fridge.

**Mara Leighton:** They have 1.5 stars, and they've come a few times.

**Mara Leighton:** Their number always goes to a full voicemail inbox.

**Mara Leighton:** No one ever picks up.

**Mara Leighton:** And they'll say they came when I was home all day, and they didn't.

**Mara Leighton:** So, anyway.

**Mara Leighton:** Today, I finally saw a person, and so I'm feeling good, but I'm like carrying a lot of stress energy from that experience.

**Andi Bailey:** So is Big Mike supposed to test your fridge before the landlord will buy you a new one?

**Andi Bailey:** Exactly how it works, yeah.

**Andi Bailey:** Big Mike the only one that tests refrigerators in New York?

**Mara Leighton:** Yes, Big Mike holds In all five boroughs?

**Mara Leighton:** Even though I was like, hey, the fridge is actually hot.

**Mara Leighton:** It's like retroactively cooking things. No one's eyes or the sense of touch could tell.

**Mara Leighton:** So anyway, that's my, thanks for asking though.

**Megan Dickey:** I don't understand, how does it need testing?

**Megan Dickey:** Like, isn't it, if your landlord just shows up? Yeah, and it seems pretty binary.

**Mara Leighton:** I'm like, you can tell if it's working or not. But yeah, everything goes through Big Mike, not cold testing.

**Mara Leighton:** Yeah, anyway, Big Mike's has a bit of a monopoly on it, so.

**Andi Bailey:** Oh my God.

**Andi Bailey:** God, maybe that's my next, like, going to business doing that, probably make a ton of money.

**Jakub Rudnik:** We're better at the whole advert.

**Jakub Rudnik:** Two stars is all it takes.

**Megan Dickey:** Yeah.

**Mara Leighton:** Not even.

**Mara Leighton:** Yeah.

**Andi Bailey:** And we answer the phone.

**Golden Gate:** Yeah, real.

**Andi Bailey:** Wow, that, what, did you like buy a Yeti or something?

**Mara Leighton:** What have you been doing?

**Mara Leighton:** No, it's a great question.

**Mara Leighton:** I've been eating a pretty crazy diet, and mostly, it's very European.

**Andi Bailey:** Fruits and nuts only.

**Mara Leighton:** European.

**Golden Gate:** No ice.

**Mara Leighton:** No ice.

**Megan Dickey:** Room temperature eggs.

**Mara Leighton:** Yep, room temperature eggs.

**Mara Leighton:** It's been a lot of, I'm being very vulnerable here to say, it's been a lot of rice and, like, tinned fish.

**Mara Leighton:** So, anyway, that's been the last 30 days post-move.

**Andi Bailey:** I mean, tinned fish is a fashionable diet.

**Golden Gate:** My nightmare.

**Mara Leighton:** That's exactly correct.

**Mara Leighton:** I'm doing a bit of a PR spin with like, it's European.

**Mara Leighton:** But the last thing I'll say on this, the good and bad thing is I have a cat.

**Mara Leighton:** And so anyway, now we have essentially the same diet.

**Andi Bailey:** I was going to say, 30 days.

**Mara Leighton:** She's like, oh, are we having tuna again?

**Megan Dickey:** And I'm like, yeah, we have to.

**Jakub Rudnik:** Watch out for early signs of scurvy, Mara.

**Golden Gate:** Yeah, I'll let you guys know.

**Andi Bailey:** That is wild.

**Andi Bailey:** Also, like, what does the landlord think, like, that you're just trying to, like, I don't know, steal the fridge?

**Golden Gate:** Get a second fridge.

**Mara Leighton:** Yeah, get a second fridge.

**Mara Leighton:** Two fridge, better than one fridge.

**Mara Leighton:** Also, there have just been, like, leaks in every room.

**Andi Bailey:** It's been a lot.

**Andi Bailey:** But anyway, things are finally starting to get patched up.

**Mara Leighton:** So that's good.

**Mara Leighton:** And I've seen a human from Big Mike.

**Andi Bailey:** So I feel like it wasn't Big Mike.

**Mara Leighton:** It was not Big Mike.

**Andi Bailey:** Yeah.

**Andi Bailey:** They don't.

**Andi Bailey:** Send him out, I guess.

**Andi Bailey:** Because somebody would beat him up, probably.

**Megan Dickey:** for sure.

**Mara Leighton:** Maybe.

**Andi Bailey:** All right.

**Andi Bailey:** Wow.

**Mara Leighton:** That is a journey.

**Andi Bailey:** Now you really do have to update us all the time.

**Mara Leighton:** I will.

**Mara Leighton:** I'll let you guys know.

**Andi Bailey:** Okay.

**Andi Bailey:** We are on Wednesday, which is our normal Geo Day.

**Andi Bailey:** And we have a couple, I have a couple of things I want to talk about.

**Andi Bailey:** But first, FYI's, so the next few clients coming out of Strategy Sprint, Panzer is going to take over.

**Andi Bailey:** And because he's started to figure out, like, how to get the workflows customized in a way that works, he's gotten really to a good place.

**Andi Bailey:** So he is going to start on Metronome and Monograph, which are also coming out. So don't panic about everybody else getting anything new in the short term. And I think we're hiring, well, I think we're making an offer to a CM, at least on a contract basis, but she might go either to Panzer or the Strategy Sprint. So that's not good news for everyone, but it does mean we're looking for good people and we're trying to backfill.

**Golden Gate:** But it also means that the Sprint won't steal one of yours, or I won't steal one of them, so.

**Andi Bailey:** Yeah, yes.

**Andi Bailey:** Okay, so two other notes. Since we talked about capacity yesterday, we're chatting with Rachel and Jesselyn tomorrow about why they're so underwater. We're going to shadow their process and figure out what kind of requests we can put into EPD to lighten their load. But it came to my attention today that Rachel is manually publishing herself, which is obviously taking a lot of extra time.

**Andi Bailey:** We have Suleman officially now. If any of your CMs are publishing manually themselves, get that off their plate ASAP. Get them to put in EPD requests because that's something they shouldn't be doing anymore. Rachel also has a publishing pipeline request to automate that, but we know that takes time with engineering. So let's double-check that's not what's putting them underwater. If you do have people who are truly underwater in the publishing process like Jesselyn and Rachel, I want to start shadowing those people. We're going to do almost like a UX study, like you would do with external clients, where we film and see patterns, and submit those to the engineering team. So refer those people to me.

**Andi Bailey:** Okay, so those are the FYIs.

**Andi Bailey:** And then on Geo, you may have seen invites if you ever check your email because we don't get any emails.

**Andi Bailey:** It's like the weirdest thing.

**Andi Bailey:** This is the first company where I haven't ever gotten an email.

**Andi Bailey:** But if you do check your email, you might have gotten one that scrunch dashboards have been set up for your clients.

**Andi Bailey:** I'm not done with everyone, and they definitely need more help.

**Andi Bailey:** But I just like we set up the basics.

**Andi Bailey:** I tried to pull like audience information and context from your notion pages.

**Andi Bailey:** So like they should have like they should be okay in terms of their first output.

**Andi Bailey:** They

**Andi Bailey:** But there's an opportunity to upload more prompts and improve ICP competitor data, things like that.

**Andi Bailey:** So yeah, those should be up.

**Andi Bailey:** And you guys should be editors of the pages for your clients now.

**Andi Bailey:** So you should be able to go into the content section of Scrunch and make changes to all of the inputs that start tracking those prompts.

**Andi Bailey:** Any questions there?

**Andi Bailey:** Okay.

**Andi Bailey:** The next thing I wanted to talk about, and I'm putting people on the spot here, but they're chats that have been in Slack elsewhere.

**Andi Bailey:** Dave, you made a mention of a chat GPT button in Airbyte, and here, I'll share my screen.

**Andi Bailey:** I kind of want to talk to you about, like, how we might test that, what you...

**Andi Bailey:** You, like, it was a very broad comment, and so, like, let's talk about it here.

**Andi Bailey:** Airbyte has a page that has the summarize with ChatGPT button.

**Andi Bailey:** Like, that's interesting.

**Andi Bailey:** I think that that, like, forces ChatGPT to, like, look at your page.

**Andi Bailey:** Is that your hypothesis, Dave?

**Dave Capone:** Yeah, there's an entire article on this that I can share that gives more context.

**Dave Capone:** But the TLDR is that there's a lot of good signals from this.

**Dave Capone:** One, it forces ChatGPT to look at the article and check out your content.

**Dave Capone:** It also basically adds it to your history so that as it is a site that you've referenced before, the likelihood of them using it, you know, and synthesizing results will be increased.

**Dave Capone:** So there's a lot of good signals from this, and I'll link the article in a minute.

**Andi Bailey:** Yeah, so you mentioned having some open questions. If you want to test it in the thread, what do you think the first steps would be?

**Dave Capone:** Yeah, this is literally just putting a button on the page with a link that just adds it to chat GPT conversations.

**Dave Capone:** So it's super easy to add.

**Dave Capone:** So there really isn't any prep.

**Dave Capone:** I wanted to find out a few things from Airbyte if, like, when did they put this on the pages?

**Dave Capone:** And, like, what impact or potential impact they saw so that we can see if it's worth us trying it on other partners.

**Dave Capone:** So, yeah.

**Andi Bailey:** I wonder if the, like, if this is the first time they've done it, which would be, what, two days ago?

**Andi Bailey:** So Monday would be when they started.

**Jakub Rudnik:** Yeah, I hadn't seen it before. I don't know if that's Monday or sometime recently, but it's definitely new.

**Jakub Rudnik:** I would wonder, Dave, what your thoughts would be, like, it just opens to, like, read this article.

**Jakub Rudnik:** I wonder if there'd be any value in putting the title of the article, or maybe "Summarize this article about [topic] from [company]," or adding extra context on the click to help connect the brand or title to the prompt.

**Golden Gate:** I don't know.

**Dave Capone:** Yeah, we could potentially do that in the prompt because the prompt is part of the click. If you right-click and view the link, you can see how they constructed it. I need to read through the Airbyte documentation so I can ask them questions about it. I think we can probably add some additional context to the prompt.

**Andi Bailey:** Oh, that's funny.

**Andi Bailey:** It's a totally different answer.

**Andi Bailey:** This is the first time that I asked it, and this is the second time I asked it.

**Dave Capone:** Interesting.

**Dave Capone:** Yeah.

**Andi Bailey:** Megan, I feel like you'd be interested in knowing that this is an option, even if we don't know what it does yet.

**Golden Gate:** Who built that?

**Golden Gate:** Is that an OpenAI embed, or did they build that?

**Dave Capone:** They built that.

**Dave Capone:** Yeah, Airbyte built it.

**Golden Gate:** It's nothing affiliated with ChatGPT. Oh, interesting.

**Andi Bailey:** Yeah.

**Andi Bailey:** Okay, and so we should be tracking this. Dave, it sounds like you have an article that explains why people would do this?

**Dave Capone:** I'll drop it in the chat in a second.

**Andi Bailey:** You'll have to find it.

**Andi Bailey:** Okay, and then I wanted to highlight a client who keeps coming back with data and geo questions. Mara, I know you've been going back and forth with Galileo, and I think Jason has been helping advise you on some of that stuff.

**Andi Bailey:** So I was wondering if we could just do, like, a timeline of what they've been asking, what we've been giving them, like, where they're skeptical and where they're, like, leaning in to what we're telling them.

**Mara Leighton:** Yeah, for sure.

**Mara Leighton:** I think, so Jason and I haven't talked about this.

**Mara Leighton:** I think they're, so let me answer your questions.

**Mara Leighton:** First would be kind of like the general setting.

**Mara Leighton:** Connor and Jackson are the two stakeholders who we speak with most of the time.

**Mara Leighton:** They attend the meetings.

**Mara Leighton:** They're the people that we have the primary relationship with.

**Mara Leighton:** We've discussed Scrunch with them over the last couple of weeks, and we knew that would be something post-Connor going on PTO. So we would want to all walk through it together. Jason tends to drop questions into the chat that he has.

**Mara Leighton:** Sometimes they're not necessarily like an accurate reading of the dashboards that we have.

**Mara Leighton:** So a lot of it is kind of like adding context and then going back and forth on sort of what he's looking at and what trends we're seeing.

**Mara Leighton:** So he dropped a question on AI citations and was concerned that maybe we didn't have the correct strategy in place for LLMs.

**Mara Leighton:** Mostly because I think he's going to be having a conversation with like, I would imagine the board at some point.

**Mara Leighton:** And it's just trying to get ahead of the things that he doesn't understand just yet.

**Mara Leighton:** So he asked us about Scrunch because he knew we'd discussed getting it up and running for them. I think his interpretation of the thread was that we had already showed Scrunch to Galileo and that we had mentioned citations versus mentions as the core metric for AI, which thankfully was not the case.

**Mara Leighton:** But this week, I should also say I messaged our Jason over the weekend when Jason from Galileo shared a message on Saturday wanting to go through things in more depth.

**Mara Leighton:** I shared it with Jason Gong in a message just saying like, Hey, I know people, I don't know if I gave him this context, but I know directors have been pulling in Marcel for like an Atlas walkthrough.

**Mara Leighton:** I was like, this is just one of our most skeptical, skeptical clients.

**Mara Leighton:** If you're available, I could see it being valuable for you to join and we can talk through things.

**Mara Leighton:** Otherwise, can I share a few talking points with you to ensure I'm capturing everything?

**Mara Leighton:** Um, if you have any like concerns or anything, you can let me know.

**Mara Leighton:** And I didn't hear back on that.

**Mara Leighton:** So I just kind of had the conversation with Jason and Vivek.

**Mara Leighton:** And we talked through Scrunch generally, just sort of some of the things that we will be tracking for them with the caveat that like, we're still nailing down the prompts.

**Mara Leighton:** Jason had feedback there as well, which was very helpful.

**Mara Leighton:** And so anyway, I didn't want to show them prompts that I didn't feel fully confident about.

**Mara Leighton:** So I walked them through generally Scrunch.

**Mara Leighton:** We talked about our general positioning on Geo.

**Mara Leighton:** We had the conversation around like focusing on citations versus mentions.

**Mara Leighton:** And knowing Jason's personality at Galileo, we have to reiterate the same things over and over.

**Mara Leighton:** So I figured it would be helpful to have written responses as well.

**Mara Leighton:** I've shared all the memos and the output piece that we have on Geo with him.

**Mara Leighton:** And then they'll also attend the webinar, but it's on my to-do list this week to write responses to the questions he was asking. We covered them live, but I think he'd feel more comfortable with a written memo he could use in conversations with people further removed from the industry.

**Mara Leighton:** But I think he said it himself:

**Mara Leighton:** He was like, I think I'm just a little paranoid that all of this search is going away and what's the use of producing more content.

**Mara Leighton:** And if everything is going to be showing up as competitor content, what's the use in doing any other type of content?

**Mara Leighton:** And so we talked a little bit about that, then I booked a session with him for three weeks from now, when we'll have the data from Scrunch and can actually start drawing insights.

**Mara Leighton:** He feels like it's not, you know, vanishing into thin air.

**Mara Leighton:** And I have a meeting with someone from Scrunch, I think it's Andrew, immediately after this call to go through the V2 of the prompts.

**Mara Leighton:** And based on Jason's feedback and the feedback we've chatted through on prompts.

**Mara Leighton:** Basically, I removed all the informational elements and replaced them with direct product evaluation.

**Mara Leighton:** So I think it should be in a better position. Andrew and I will chat through it together, and I'll share any learnings we have.

**Mara Leighton:** And then in terms of Galileo, the conversation is ongoing.

**Mara Leighton:** I also mentioned to them that I could share the prompts with them and share a Loom video contextualizing why we picked them, so they feel like they have visibility into the process.

**Mara Leighton:** This will be a test-and-learn situation — figuring out how much information is useful for buy-in and trust, versus what leads us into rabbit holes that aren't directly related and are difficult to get out of.

**Mara Leighton:** So, I know that was a monologue, but there's an executive summary we'll be doing for Jason, and we'll pull him in three weeks from now to discuss Scrunch.

**Mara Leighton:** And on the day-to-day level, we have a good rapport with Jackson and Connor, and we'll keep talking with them. Both of them are on PTO this week and next week.

**Mara Leighton:** So, anyway, I can pause there, but that's kind of the general gist.

**Andi Bailey:** No, that's perfect.

**Andi Bailey:** I asked you to do a monologue, so thank you for doing a monologue.

**Mara Leighton:** Well, I'm glad. It's a lot. But something I'll share — Jason's mannerisms and how he communicates in our external channel could be misconstrued as antagonistic.

**Mara Leighton:** He is very direct, which is great because it gives us an opportunity to respond.

**Mara Leighton:** There are challenges where sometimes I don't think we're on the same page with the data we're looking at. But when we're on a call with him, he's much more collaborative and warmer.

**Golden Gate:** Yeah, Vivek's responses were well done. He's providing quantitative information that we can counter with or at the very least contextualize. Direct is good also — don't dissemble. Tell us what you think.

**Mara Leighton:** And I responded to him over the weekend. Jason and I had a back and forth, and I essentially just reiterated our position on Geo.

**Mara Leighton:** I shared a couple of studies from Ahrefs with him — one from June of this year and one from February — showing the general trajectory of overall site traffic impact from LLMs.

**Mara Leighton:** And what we're seeing currently for Galileo is very positive, but it makes sense this is going to be a continual conversation. He's naturally fixated on it, and that's where we are.

**Andi Bailey:** Are you thinking about setting any shared goals with them? I know it's weird stuff to track, but are they setting goals, telling you about them, and are we able to help shape or discourage them?

**Andi Bailey:** Yeah, that's a good question.

**Mara Leighton:** Nothing explicit yet. We talked about which prompts would be most important to be visible in. From Jason's perspective, it's focusing on showing up in competitor content and making sure Galileo is continually part of the conversation. Once I have a better handle on what I can comfortably promise them, I can help guide that conversation. But nothing extremely explicit yet.

**Andi Bailey:** Okay, yeah.

**Andi Bailey:** I mean, I think right now, it seems like a lot of our clients are doing H2 planning and setting goals.

**Andi Bailey:** So we should just be trying to figure out if they're setting goals that we're supposed to be influencing.

**Andi Bailey:** And if he's talking to the executives about showing up in LLMs, I'm sure somebody has a number somewhere. Anybody have anything else? All right. Thanks, guys.
