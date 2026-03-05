# Content Audit: Jess & Bisera

<metadata>
date: 2025-05-27
time: 15:16 UTC
duration: 24 minutes
organizer: Matthew Panzarino
participants: Bisera, Jess Scott, Matthew Panzarino
fathom_recording_id: 64842266
fathom_url: https://fathom.video/calls/310494231
share_url: https://fathom.video/share/mFF7HvPxTBsfXrhxGAiQQyGF7p2_FAFH
source: fathom
enriched_on: 2026-03-04 02:05 UTC
</metadata>

---

## Summary

Matthew Panzarino audited 40 pieces of GrowthX content across all current clients, finding roughly 30% great, 40% satisfactory, and 30% needing major improvement, with issues including overuse of the "blank blank: blank blank" headline template (in ~70% of content), unattributed LLM-generated statistics, and skeletal structures with back-to-back single-sentence H3s that damage readability. The team discussed how client requests (like Seat's demand for content under 1,000 words) drive some of these patterns, and agreed to pivot away from word-count-based Statements of Work toward article-based agreements, create custom workflows for each client during sprint operations, and develop detailed client-specific writing instructions to improve quality and reduce team burnout from meeting arbitrary metrics.

---

## Context

This is an internal GrowthX delivery meeting between Matthew Panzarino (recently hired VP of Editorial/Product), Jess Scott (delivery lead), and Bisera (content creator). Matthew conducted a systematic audit of GrowthX's current content production across multiple clients to identify systemic issues in output quality and workflow efficiency. The team has been operating under significant time pressure and word-count-based contractual obligations, which led to content that prioritizes volume over quality. Matthew's audit is part of a broader initiative to restructure delivery processes, transition off the AirOps platform by June 10th, and introduce sprint-based onboarding and custom client workflows to increase quality and team capacity.

---

## Relevance

**To GrowthX Delivery:**
- Content quality varies significantly (30/40/30 split) with common patterns in poor-performing pieces: "blank blank: blank blank" headlines in ~70% of content, LLM-hallucinated statistics, word-whiskers like "game-changer" and "robust," and skeletal structures with repetitive single-sentence H3s.
- Moving from word-count-based Statements of Work to article-based agreements will reduce perverse incentives and allow teams to prioritize quality and client-specific needs.
- New calibration process requires Matthew to review and edit all calibration articles before client presentation, establishing quality baseline and uncovering client-specific writing instructions (e.g., Aimbit case study yielded 98% generation accuracy after instructions were formalized).
- Retroactively creating custom client-specific writing instructions (collating feedback from Slack, Loom calls, Fathom calls, and all previous edits) will dramatically improve output quality for existing clients.

**To GrowthX Business Development:**
- Account health risk: Some clients have churned on calibration articles alone—quality in onboarding is now critical.
- Team capacity is limited by workflow friction and process debt (AirOps transition, broken workflow builds, ad-hoc sprint operations), creating renewal/expansion risk if delivery slows further.
- Matthew's role includes identifying "oxygen-stealing" commitments like Prismic integrations and CMS builds promised before development, freeing sprint groups to focus on delivering on core service contracts.

**To Operations/Platform:**
- June 10th AirOps sunset is hard deadline; this is consuming enormous engineering and leadership effort until then.
- New internal platform will offer workflow flexibility currently unavailable in AirOps (custom steps, more granular control, better debugging and rollback for broken builds).

---

## Overview

- Content quality varies: \~30% great, \~40% okay, \~30% needs improvement
- New client onboarding process to include custom workflows and detailed writing instructions
- Shifting focus from word count to article quality and client-specific needs
- Transitioning off AirOps by June 10th to gain more flexibility in workflow management

---

## Key Topics

### Content Audit Findings

  - \~30% of content across 40 pieces is high-quality with minor tweaks needed
  - \~40% is satisfactory
  - \~30% needs significant improvement or shouldn't be live
  - Common issues:
      - Overuse of "blank blank: blank blank" headline structure (in \~70% of content)
      - LLM-generated statistics without proper sourcing
      - Word whiskers specific to LLM outputs (e.g., "game-changer", "robust")
      - Skeletal structure with repetitive single-sentence H3s and bullet points

### Client-Specific Content Challenges

  - Seat example: Client requested concise, scannable content under 1,000 words
  - Push for brevity led to skeletal structure with multiple bullet lists
  - Highlights need for balancing client requests with content best practices

### Workflow Improvements

  - Moving away from word count-based SoWs to article-based agreements
  - Creating custom workflows for each client during sprint operations
  - Developing detailed, client-specific writing instructions (e.g., Aimbit case study)
  - Planning to incorporate client feedback and editor revisions into LLM training

### Platform Transition

  - Urgent need to transition off AirOps by June 10th
  - New platform will offer more flexibility in workflow design and implementation
  - Transition period may slow down some improvement initiatives temporarily

### Content Creation Process Enhancements

  - Matthew now reviewing and editing calibration articles before client presentation
  - Implementing custom workflows and writing instructions for new clients
  - Planning to retroactively create custom workflows for existing clients
  - Aiming to increase leverage through workflow improvements, allowing teams to handle more content with less stress

---

## Action Items

- **Matthew Panzarino (GrowthX):** Complete transition from AirOps to new platform by June 10th
- **Matthew Panzarino (GrowthX):** Develop and implement custom workflows for new and existing clients; retroactively collate client feedback (Slack, Loom, Fathom, editor revisions) into detailed client-specific writing instructions
- **Matthew Panzarino (GrowthX):** Identify and address "oxygen-stealing" commitments like CMS integrations and Prismic builds that slow delivery
- **Jess Scott (GrowthX):** Continue refining content creation process with emphasis on quality over word count; implement new article-based SoWs for clients
- **Bisera (GrowthX):** Leverage updated writing instructions and custom workflows in ongoing client delivery to reduce rework cycles

---

## Transcript

**Matthew Panzarino:** Oh, okay, so there are a couple of things I want to talk about.

**Matthew Panzarino:** I want to talk a little bit, and then I want to hear from you a little bit.

**Matthew Panzarino:** So, obviously, the one piece here, Bisera, most of your content is fantastic.

**Matthew Panzarino:** You know, I really, I think you do a great job, so I'm not—none of this is about, like, here's all the things I think are wrong.

**Matthew Panzarino:** You know, this is really more about, like, architecturally, how.

**Matthew Panzarino:** I'm thinking about these things, the things that we should be examining.

**Matthew Panzarino:** I looked at our content overall across about 40 different pieces of content across our current clients.

**Matthew Panzarino:** I would say about 30% of it is pretty great with some small tweaks here and there, which nothing is ever perfect, right?

**Matthew Panzarino:** Then a good chunk of it is all right.

**Matthew Panzarino:** And then there's about 30% of it that's like, eh, I really wish this wasn't live.

**Matthew Panzarino:** You know, this has not fallen to any of that.

**Matthew Panzarino:** There are a handful, only a handful of pieces really that I'm really regretful that are live currently.

**Matthew Panzarino:** But we'll get better.

**Matthew Panzarino:** The walkthrough of this stuff here—in this piece, I think there's only a handful of things that really need to call it out. Like the "how blank blank" heads or the "blank blank colon blank blank" heads.

**Matthew Panzarino:** We need to be really careful about those as much as possible. About 70% of our content has a "blank blank colon blank blank" structure, and a lot of them.

**Matthew Panzarino:** And of course the workflows are making these.

**Matthew Panzarino:** This is not humans writing it because nobody writes that way, right?

**Matthew Panzarino:** Like nobody specifically always loves a colon in a headline.

**Matthew Panzarino:** I don't know a single person who loves to do it.

**Matthew Panzarino:** You do it because you have to, because you must.

**Matthew Panzarino:** And sometimes you must.

**Matthew Panzarino:** Sometimes it's really just the best structure for it, especially if it's like a really in-depth guide or something.

**Matthew Panzarino:** It's like, you know, blah, blah, blah, the world's best guide, you know, or whatever it is.

**Matthew Panzarino:** That's okay.

**Matthew Panzarino:** But in general, try to avoid those.

**Matthew Panzarino:** Some scene-setting statistics are helpful here.

**Matthew Panzarino:** In general, these statistics are hallucinated by LLMs, right?

**Matthew Panzarino:** So you can't ask it for real ones.

**Matthew Panzarino:** You have to actually feed it real ones.

**Matthew Panzarino:** But I think this is, I just wanted to highlight this because I think this is a really good example of something that can be and should be in our new onboarding, client onboarding process.

**Matthew Panzarino:** It should be gathered during the sprint better.

**Matthew Panzarino:** I know we have always asked the client a little bit—like, "Oh, do you have anything for us? Do you have data? Do you have case studies? Do you have things that you can share?" Well, we need to get more robust about that.

**Matthew Panzarino:** We need to have an internal data store that has these documents on hand that we can feed to the LLM.

**Matthew Panzarino:** Say, hey, here's your repository.

**Matthew Panzarino:** Please only use data from this repository and add three statistics that support the thesis to this piece.

**Matthew Panzarino:** You know, there should be the ability to do that.

**Matthew Panzarino:** Right now, we don't have the ability to do that.

**Matthew Panzarino:** So I think that's good.

**Matthew Panzarino:** A handful of word whiskers in this piece that are LLM-centric—"game-changer," "robust"—you know, there's just a handful of things that are LLM whiskers that were in here.

**Matthew Panzarino:** This particular one is more of a theological thing that will not always apply, but I took this bullet point list and asked for a narrative version of it, and it worked fine. Like, the narrative aspect of taking a bullet point section and turning it into a narrative is a useful tool when we have back-to-back sections, which I found the vast majority of our pieces fall prey to.

**Matthew Panzarino:** And it's clearly the workflows or just LLM output, but you get this pattern: single-sentence H3, single-sentence bullet, single-sentence H3.

**Matthew Panzarino:** There's a lot of that, a lot of that in our pieces, and we need to be very intentional about allowing those things to remain.

**Matthew Panzarino:** It's not that they can never happen.

**Matthew Panzarino:** Sometimes it's just the best way to do it.

**Matthew Panzarino:** Sometimes it's just a brief list or a reminder or a quick recap or whatever, and that's just the best structure for that.

**Matthew Panzarino:** But if you have them back-to-back, the content ends up looking incredibly skeletal.

**Matthew Panzarino:** And, you know, from an SEO standpoint, it's nice to have those down there, especially if they're the core point of the article that you want to rank really well on.

**Matthew Panzarino:** But outside of that, be careful about how the texture of the piece looks.

**Matthew Panzarino:** It can look very skeletal if they're back-to-back.

**Matthew Panzarino:** Yeah, what's up, Jess?

**Jess Scott:** I just wanted to give you a little bit of context on Seat specifically because this client, I'm not surprised that this is the piece you pulled or, like, the content you pulled because it is so skeletal.

**Jess Scott:** And just for full context, just before you carry on—the client pushed back on this.

**Jess Scott:** So we gave them two calibrations with very narrative kind of similar to what you're pointing out here.

**Jess Scott:** And she was like, I want less than 1,000 words.

**Jess Scott:** I want it to be, you know, she was like, I want someone who's a dev or an engineer to be able to scan this and get the info they need.

**Jess Scott:** So that's why most of Seat's content is bullet list after bullet list. And we literally—I think it was last week's call—

**Jess Scott:** We were like, we need to do longer form content.

**Jess Scott:** This is, like, we've done what you wanted and now we need to kind of start revisiting this again.

**Jess Scott:** So I just, I did just want to add that of, like, these bullet lists were, like, they're not where we were trying to get the client to go.

**Matthew Panzarino:** Yeah, that's totally fine.

**Matthew Panzarino:** And that's why I said this is not like, here's what you did wrong, right?

**Matthew Panzarino:** It's like, are we thinking intentionally about this? Clearly, you are.

**Matthew Panzarino:** And this is a client piece of client calibration.

**Jess Scott:** Yeah.

**Matthew Panzarino:** I want this kind of thing.

**Matthew Panzarino:** And if they want it, great.

**Matthew Panzarino:** That's fine.

**Jess Scott:** You know, I just wanted to let you know that that was like, no, no, it's totally fine.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** There's going to be a lot of that across this content where it's like, hey, this is the way that I see this.

**Matthew Panzarino:** But if the client wants it a certain way and we've already enumerated our, you know, our concept of like, hey, you could do it this way too.

**Matthew Panzarino:** And they're like, no, no, no, we don't like that.

**Jess Scott:** Okay, cool.

**Jess Scott:** Yeah.

**Jess Scott:** She was like, "I'm not reading 2,000 words."

**Jess Scott:** So we sent her 1,500 and she was like, "It needs to be shorter." We were just like, "What do you want here?"

**Jess Scott:** And we don't have a word count on your SoW, yeah—exactly.

**Matthew Panzarino:** Well, I kind of agree with that.

**Matthew Panzarino:** And that's why I think we need to get away from word counts on SoWs.

**Matthew Panzarino:** Because I think it breeds weird content.

**Matthew Panzarino:** There's no reason that it needs to exist.

**Matthew Panzarino:** I don't think anybody really thinks that way.

**Matthew Panzarino:** It actually...

**Matthew Panzarino:** It's very difficult to tell whether or not anybody even understands what 1,000 words looks like.

**Jess Scott:** It adds a lot of stress from our side. Me and Bisera specifically have had moments of being like, "Well, their SoW is 50,000 words this month, and we've not gotten them there."

**Matthew Panzarino:** Yeah, the new SoWs are all article-based. Anything we sign from now on is not going to be based on words.

**Matthew Panzarino:** I don't think that that makes, and I expressed this, which is why it's different now, but I don't think it makes a lot of sense because words don't really matter.

**Matthew Panzarino:** You know, what matters is getting the point across, like getting your article across.

**Matthew Panzarino:** Now, that could be a double-edged sword.

**Matthew Panzarino:** It could end up biting you when a client's like, "Oh, we need all our articles to be essays."

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Okay, so now it's 2,000 words per article, right?

**Matthew Panzarino:** But in reality, it's usually never a problem to have an LLM give you more content. The real problem is where you're like, "Okay, make this more concise." The reason I wanted to call these out and I'm glad you're being intentional about it—it's client feedback.

**Jess Scott:** Yeah, sorry to interrupt.

**Matthew Panzarino:** No, no, that's okay.

**Matthew Panzarino:** The reason I wanted to call it out is because I doubt most of the content is that way because the client asked for it, right? I think the vast majority of it is because this is what the LLM spits out, and then people aren't just thinking critically about it and saying, "Okay, but what if we took this really skeletal body component and busted part of it out into a narrative?" So that at least there's some textual change.

**Matthew Panzarino:** Like—think of it as geometry, right? Like if you have this back-to-back and it's really skeletal, put some round shapes in there in addition to your columnar shapes, so that it has the appearance and feel and texture of quality to a human reader as well as to search engines, right?

**Matthew Panzarino:** Okay, so that's why I flagged it in here, but it gets it. I get it. You know, the client wants that. The reason it's in here is very straightforward: anytime you tell an LLM any word like—which I'm pretty sure is in our standard instructions—"clarity," "brevity," "concise"—it's like, "Cool, single sentences." It's like, "No, damn it, that's not what I meant."

**Matthew Panzarino:** But what I found was taking those chunks and feeding them back in and asking it very explicitly: "Give me these thoughts in two to five sentences per paragraph. Only use single sentences if you're emphasizing a key point."

**Matthew Panzarino:** And then it'll come back with something that's usually pretty good.

**Jess Scott:** Did you do that in AirOps?

**Matthew Panzarino:** So did you do that in AirOps?

**Matthew Panzarino:** Yeah, LLMs only. I didn't use AirOps for this exercise explicitly because my AirOps exercises are not going to be about, "Oh, what do we do inside the current operations to fix these issues?" It's how do we actually make better operations across the board.

**Jess Scott:** Yeah, I was going to say—that's the other thing about this specific piece.

**Jess Scott:** This client regenerates content in ChatGPT.

**Matthew Panzarino:** Okay, yeah, yeah.

**Matthew Panzarino:** And I think that's the case for some clients. A lot of Vivek's clients, as an example, were working really well out of the workflows—almost straight out of the workflows with some tweaking—and they look pretty solid. And then the workflows broke, and now we can't do that anymore. And then vice versa: some people generate a lot in ChatGPT, and it's like, maybe you could get this out of the workflows if it's properly prompted—maybe not.

**Matthew Panzarino:** But, like, that's why we're going through all of the content exercises and trying to get better about it.

**Matthew Panzarino:** The workflows are not where they need to be, like, let's just be honest, right?

**Matthew Panzarino:** But right now, a lot of engineering time is getting sucked up by the fact that we've got to get off of AirOps.

**Matthew Panzarino:** So that's, it's going to be a little slow for the next few weeks until we're off of that.

**Matthew Panzarino:** But then, you know, that's literally a good chunk of my job is to make sure that, you know, the feedback gets taken, we understand what's broken and what's not working.

**Matthew Panzarino:** We understand the differential between the reality of the day-to-day that you folks are seeing and what we think that the workflow should be capable of.

**Matthew Panzarino:** But there's a lot of fixes that can go in.

**Matthew Panzarino:** Kirkland just pushed one today, by the way, so let me know if any of that stuff improves or doesn't.

**Matthew Panzarino:** I'll be the sort of person that pushes all of those things, and that's going to be a good portion of my job, right?

**Matthew Panzarino:** Just making sure that those things actually do improve day-to-day.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** One of the things that I noticed, obviously we have some clients that have churned based on just calibration articles alone, which is not ideal.

**Matthew Panzarino:** Oh, really?

**Matthew Panzarino:** Yeah, so one of the things that I'm now doing is any new client, well, any new client is now going to go through our new sprint operation, right?

**Matthew Panzarino:** But one of the things I instituted for any new clients in the meantime is that I'm doing all of the calibration edits.

**Matthew Panzarino:** So we'll generate the calibration articles.

**Matthew Panzarino:** And then myself and the director will sit down with those calibration articles, maybe the Emmy as well, and edit them.

**Matthew Panzarino:** And then Emmy will, like, take those edits and apply them or push back or whatever.

**Matthew Panzarino:** And we knock them into shape before the client ever sees anything.

**Matthew Panzarino:** Because showing them something that we just generated is not a good look.

**Matthew Panzarino:** You know, because, A, they don't generate very well.

**Matthew Panzarino:** And, B, we need to offer them a vision for where they will be, not, like, a sketch of where they might be, right?

**Matthew Panzarino:** Because some people are okay with that, you know?

**Matthew Panzarino:** Some people are like, let's move fast and break things.

**Matthew Panzarino:** But the vast majority of clients are not going to be there.

**Matthew Panzarino:** Like, a CMO or a CEO, if we show them a piece of content that's really rough, they're going to be like, "Oh, they're too far off."

**Matthew Panzarino:** And we hired them to get work off of our plate, and it seems like a lot more work, you know, to get them even close to where we want to be, right?

**Matthew Panzarino:** So, as a part of that process, though, it helps us to kind of clarify that we need custom workflows for every client, not generic workflows.

**Matthew Panzarino:** And so the sprint group is going to be setting up custom workflows for each of the new clients that we kick off with.

**Matthew Panzarino:** So instead of just copying and pasting our workflow and then, you know, putting the outline in and hitting run or putting assignment in and hitting run, we're going to probably create something that's more custom along those lines.

**Matthew Panzarino:** One of the best exercises that came out of it is when Jacob and I did our pass on Aimbit's kickoff and calibration articles. David took that feedback—those edits along with the feedback Aimbit gave us—and created writing instructions for Aimbit specifically. Very detailed instructions that go beyond the company profile or current polishing instructions. I asked him to share this because I think it's really good.

**Matthew Panzarino:** And when we generated articles with this, it was like 98% good according to what Aimbit likes. He's generated a couple more based on these instructions after our first wave of calibration, and they're already better.

**Matthew Panzarino:** But exercises like that need to be done during the calibration phase. That's not currently done, right? The calibration phase is very rough right now—it's ad hoc and it needs to get a lot better.

**Matthew Panzarino:** The sprint groups will do a lot to change that so that by the time a working group like yourselves get a hold of a client, it will be in a much more steady state.

**Matthew Panzarino:** Like you will have a calibrated client that has a custom workflow, expectations already set.

**Matthew Panzarino:** Anything that we needed to custom build for that client has been built.

**Matthew Panzarino:** Like the poor folks on the StackBlitz account and the DAPI account are getting burned right now because clearly we needed to build a bunch of stuff before we promised them that we were going to deliver.

**Jess Scott:** Yes.

**Jess Scott:** How does that work for folks like us? Like we have three existing clients. Are we going backwards?

**Matthew Panzarino:** No, honestly, I don't know.

**Matthew Panzarino:** But nobody's really thought about how this will affect existing clients beyond my ad hoc thoughts about it, which is that if we improve workflows and create custom workflows for new clients, we should then do that exercise on our existing clients.

**Matthew Panzarino:** And an exercise that David did for Aimbit as an example, we should probably do that for all of our clients.

**Matthew Panzarino:** Like all of the feedback they've ever given you in the Slack channel or in all of the Loom calls and all of the Fathom calls or whatever, like all of that stuff should be collated.

**Matthew Panzarino:** And the LLMs are actually pretty good at turning that into specific instructions about what this client likes and what it doesn't like.

**Matthew Panzarino:** Because the missing link is, of course, all of the edits that you have done to get them into publishing shape for that particular client. Those should all be read into the model as well. And we don't even have that ability—it's not even built or even starting to be built yet, but everyone knows it needs to be, right?

**Matthew Panzarino:** So right now we're just trying to get the hell out of AirOps. That's consuming an enormous amount of engineering time between now and June 10th.

**Matthew Panzarino:** We've got to get off.

**Jess Scott:** You don't want to extend that deadline?

**Matthew Panzarino:** Yeah, that's the deadline. I've been hearing about getting off of AirOps, I've just never heard a date until now.

**Jess Scott:** Yeah, I know there's a deadline. I've been here a long time.

**Matthew Panzarino:** But yeah, once we get off AirOps and onto our own platform, there's a lot of flexibility that becomes available to us that's just not available in AirOps. You can only add so many steps in AirOps. And like, is this really a step or should it be more base-level built into our workflows that we have architected?

**Matthew Panzarino:** So there's improvements that need to be done there.

**Matthew Panzarino:** I'm literally still just onboarding. But after these exercises, I wanted to ingest as much as possible so I'm not talking out of my hat about what content we are making and what's possible.

**Matthew Panzarino:** And I understand where the pain points are and where we need to improve.

**Matthew Panzarino:** But we'll continue to have discussions about the way the workflows currently work versus how we want them to work, and we'll get more granular about all that. Like we have a delivery meeting later today where Jason and I know we need to get a tight loop on all this stuff, right?

**Matthew Panzarino:** And what we're telling clients we can do versus what we can't actually do, what the workflows are capable of, what they're not.

**Matthew Panzarino:** Like when a workflow breaks, that's a nightmare scenario. If we were a public-facing website, we would never push stuff to production without seeing whether it worked or not. And right now we just do—we make changes and then all of a sudden Vivek's entire world crumbles overnight, right?

**Matthew Panzarino:** And he has to rely on chat to you.

**Matthew Panzarino:** So that's not ideal.

**Matthew Panzarino:** Like there's a lot of process things we need to improve here.

**Jess Scott:** Cool.

**Jess Scott:** That makes sense.

**Jess Scott:** I mean, I'm glad there's – I mean, I told – it's funny because I told Kyle when they announced you joining.

**Jess Scott:** I was like – I looked at your LinkedIn.

**Jess Scott:** was like, this guy's a  artist.

**Jess Scott:** And now I'm like, no, this is actually what we need.

**Matthew Panzarino:** This is perfect.

**Matthew Panzarino:** You ask because there's no way somebody has done all the things you've done.

**Matthew Panzarino:** So I was like, there's no way.

**Jess Scott:** But, no, this is great.

**Jess Scott:** And now knowing that there's kind of like a timeline and like that we now have – like my team specifically has the capacity to think more critically about the content instead of just like – like I know we have Timmy's call in a minute.

**Jess Scott:** And like Timmy's article is like he put out 120 tribe articles last week or last week.

**Jess Scott:** like while also supporting three other accounts.

**Jess Scott:** So I'm like – I'm glad we finally have like actual breathing room for some of these folks to be able to think about it.

**Jess Scott:** not

**Jess Scott:** Just think about, like, I have to get X number of pieces out by end of week, but what are we actually providing the client?

**Matthew Panzarino:** Yeah, actually thinking about internal logic to what the client is getting and how can we improve and all that.

**Matthew Panzarino:** Yeah, just getting some breath in there.

**Matthew Panzarino:** I mean, the breath for us, the source of oxygen, the primary source, should really be, well, there's two things.

**Matthew Panzarino:** There should be a primary source of oxygen, which is improvements in the workforce.

**Matthew Panzarino:** The more that those are improved, the more that that will allow us to increase our leverage.

**Matthew Panzarino:** So each person can be responsible for more content or responsible for delivering content in a way that feels less harried and anxiety-ridden and behind the ball.

**Matthew Panzarino:** Then we also need to block oxygen-stealing elements like promising customers things that we have not built, right?

**Matthew Panzarino:** Stuff like that, right?

**Matthew Panzarino:** Like, those are oxygen-stealing bits of it.

**Matthew Panzarino:** Now, in a...

**Matthew Panzarino:** Startup, you are always going to do that, but what we're doing with creating these sprint groups is the ability to be like, hey, here's a high agency group of folks who have the ability and access to Daniel or Cell and the high level engine leadership, whatever, to like actually create these things and build them.

**Matthew Panzarino:** Not a build team who's like mid-stride with a bunch of clients trying to suddenly go, hey, who can build this thing that you promised them that we could do?

**Matthew Panzarino:** And like there's a lot of that, you know, there's, I mean, like the CMS integrations, like the Prismic thing and like, you know, all of these various integrations that we need to do for doing something as simple as publishing, you know, or building templates and all of that stuff.

**Matthew Panzarino:** You know, there's just more specificity that we need and we'll get there.

**Matthew Panzarino:** So there's oxygen giving, life giving, and then oxygen sealing stuff and we need to work on both ends.

**Jess Scott:** Yeah, but I think, I mean, yeah, like I said, like it's great.

**Jess Scott:** You've already felt the difference since you joining of being able to have better resources and have more clarity on like, it's not about the number or a word count.

**Jess Scott:** It's about the quality.

**Jess Scott:** And that's, you know, that's been something that we've been struggling, like, because when I came on, it was just Bisera and I in these five accounts.

**Jess Scott:** And before that, it was just Bisera in these five accounts, like fighting for her life and, you know, just trying to get everything out in time.

**Jess Scott:** So, no, I appreciate it.

**Jess Scott:** And yeah, my team—all I can speak for—we definitely have felt the difference.

**Matthew Panzarino:** Good.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** And look, one of the reasons I went through all of the content—I really sucked on the fire hose—is to understand the weaknesses in the outputs and workflows, and not to pick on anybody. It's not like, "Oh, you're bad at this."

**Matthew Panzarino:** No, I know the pressures everybody's under. I know the time crunch. I mean, we published 56 human-written stories a day at TechCrunch—every day, all day, globally.

**Matthew Panzarino:** So I can understand what a high-velocity newsroom feels like or high-velocity output in a writer's room.

**Matthew Panzarino:** And if we can enable the ability to do that at speed and at quality levels that we feel are acceptable, that's my dream scenario.

**Matthew Panzarino:** That's why I'm here.

**Matthew Panzarino:** I didn't want to join a place just to run an editorial team again. I've done that. I don't need to do that anymore. It's fine to do that work,

**Matthew Panzarino:** I'm happy to lend my skills in that way.

**Matthew Panzarino:** But the major reason I'm here is because I want to make sure that we can codify that and engineer that and make it a real thing. That's where my full attention will be.

**Jess Scott:** Bisera, did you have any questions?

**Jess Scott:** Because I know you watched the Loom and went through the article, and I just hijacked this whole call.

**Bisera:** Sorry.

**Bisera:** Yeah, no, I guess I agree with your edits.

**Bisera:** I see your point.

**Bisera:** It just, you know, it's what a client wants.

**Bisera:** It's what they're getting.

**Bisera:** Other than that, I hear you.

**Bisera:** Like, I agree fully.

**Bisera:** I love content.

**Bisera:** I'm very nitpicky when it comes to content and its quality, so yeah.

**Matthew Panzarino:** Yeah, yeah, no, that's totally fine.

**Matthew Panzarino:** I made these observations with an understanding of the rough Statement of Work, but certainly not with all the context of every conversation you have with a client.

**Matthew Panzarino:** So that's totally understood.

**Matthew Panzarino:** And I have to go into these in a first-principles manner. Because in a lot of cases, there's people who are like, "Hey, have you thought about this?" and they're like, "Oh, no, okay, cool, yeah, sounds good."

**Matthew Panzarino:** Great, I'm glad we talked about it. And that's the way to go about it. All right, we can jump to the next meeting. Thanks very much, Bisera. Thank you.

**Matthew Panzarino:** Bye.
