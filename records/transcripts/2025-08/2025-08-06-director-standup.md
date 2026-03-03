# Director Standup

<metadata>
date: 2025-08-06
time: 19:01 UTC
duration: 29 minutes
organizer: andi@growthx.ai
participants: Andi Bailey, Darrell Etherington, Jakub Rudnik, Mara Leighton, Matthew Panzarino
fathom_recording_id: 78944501
fathom_url: https://fathom.video/calls/371975034
share_url: https://fathom.video/share/gjqxNSZR9PXZ91g5g2ZEmcyBzZikNWf1
source: fathom
enriched_on: 2025-03-03 14:23 UTC
speaker_note: "Golden Gate" (140 speaker labels) could not be identified against the participants list. This label appears to be a device/room name that the conversion script could not resolve to a real attendee. The person runs the meeting, leads discussions on article polish standards, and assigns action items. Dave Capone, Jason Gong, and Megan Dickey were invited but do not appear in the transcript.
</metadata>

---

## Summary

The GrowthX content delivery team aligned on article polish standards and quality review workflows, discovering that review intensity varies dramatically by client and content manager experience. Matthew Panzarino flagged critical pipeline issues with Metronome (scope creep causing low-quality artifacts and scope drift) and recommended reintroducing style adapters to pipelines as a lightweight guardrail for LLM-generated drafts. The team also discussed strategies for managing client expectations through clear visualization of work streams and priorities, and agreed that cleaner client-facing spaces (Notion, dashboards) would reduce scope creep and improve capacity communication.

---

## Context

This is a recurring GrowthX Delivery Directors standup where Matthew Panzarino, Jakub Rudnik, Darrell Etherington, Mara Leighton, and Andi Bailey meet to align on editorial processes, content quality, and client management. The meeting arose from a pattern across multiple accounts (Smith, School AI, Seat, Biologica, Monograph, Metronome, WebSec) where clients have very different expectations for article review and approval. Some clients trust GrowthX to publish without review, while others scrutinize every article before publishing. The core challenge: GrowthX has committed to managing wildly different volumes and quality standards across accounts, and the current manual review processes aren't sustainable. The discussion centers on defining baseline review processes, leveraging Grammarly, and improving pipeline quality so less human review is needed.

---

## Relevance

**To GrowthX Delivery:**
- Article review workflows vary by client trust level; define a tiered baseline (6 weeks director oversight, 12 weeks ME review, then autopilot) that can be adjusted per account to manage workload and maintain quality
- Reintroduce style adapters to post-process LLM article drafts — should be standard in all pipeline templates as lightweight guardrail to catch prompt adherence issues
- Metronome pipeline producing low-quality content due to poor artifact context and semantic segmentation; artifacts need clear section structure and human-readable context for LLM to succeed
- Grammarly account usage inconsistent across teams; audit needed to ensure adoption and include as standard editorial checklist

**To CheckThat / Content Generation:**
- LLM artifact quality directly impacts downstream generation; clear, well-structured artifacts with semantic context prevent scope drift and tangential content
- Style adapters catch writing guideline violations more efficiently than full human rewrites; prioritize building this post-processing step
- Ask.ai tool sidebar interface now available for line-editing tasks (reflow, name replacement); communicate update to teams using this tool

**To GrowthX Business Development:**
- Account health risk: Seat still requires review of every article despite years of engagement; signals trust or value communication gap
- Scope creep is major profitability risk (Augment Code, Metronome); visualizing work streams + prioritization system helps push back on requests exceeding capacity
- Client-facing spaces (Notion, dashboards) need professional polish to reduce perceived clutter and improve capacity conversations
- Implement Gary's task management app to give clients simple checkbox interface for deliverables, reducing friction and clarifying capacity limits

---

## Overview

- Polish levels vary by client, with some requiring more intensive review than others
- Most teams use Grammarly and have multi-layer review processes (CM, ME, Director)
- Client feedback loops and trust-building are crucial for reducing review intensity over time
- Organized task management and clear client-facing spaces are needed to manage workloads and expectations

---

## Key Topics

### Article Polish and Review Processes

  - Review intensity varies by client and content manager experience
  - Most teams use Grammarly for initial grammar checks
  - Multi-layer review process: CM → ME → Director (in some cases)
  - Some clients (e.g., Smith, School AI) review every piece before publishing
  - Others trust the team to publish without approval

### Client Management and Expectations

  - Building trust over time allows for less intensive client reviews
  - Some clients (e.g., Seat) still provide feedback on every article despite long-term engagement
  - Strategies for managing client expectations:
      - Visualize all work streams and priorities
      - Use a prioritization system to focus efforts
      - Clearly communicate capacity limits and trade-offs

### Content Quality and Pipeline Issues

  - Metronome pipeline producing low-quality content, possibly due to scope creep and semantic issues
  - Suggestion to reintroduce style adapters in pipelines to reinforce writing guidelines
  - Importance of clear, contextual artifacts for LLM understanding

### Workflow and Tool Improvements

  - Ask.ai tool now has a sidebar interface for easier editing
  - Suggestion for a unified task list across clients for directors
  - Need for cleaner, more polished client-facing spaces (Content OS, Notion, dashboards)

---

## Action Items

**Jakub Rudnik (GrowthX)**
- Check if team is using Grammarly, report back to meeting lead

**Matthew Panzarino (GrowthX)**
- Review Metronome artifacts for quality issues, identify improvements
- File ticket with Engineering to get style adapter built for article draft post-processing
- Implement Gary's task management app for Biologica, Metronome, and Monograph teams

**[Unidentified Meeting Lead]**
- Update standard pipeline template to include style adapter workflow

---

## Transcript
**Mara Leighton:** Trying to teach Erisham how to use Figma.

**Darrell Etherington: It's a bit of a mess.

**Darrell Etherington: He thought it was more like Canva.

**Darrell Etherington: It's kind of like Canva.

**Darrell Etherington: But if you wanted to be very designery.

**Darrell Etherington: Okay.

**Andi Bailey:** Guys, I'm trying to figure out how to invite a room.

**Darrell Etherington: Oh.

**Darrell Etherington: But the keypad thing, like manually entering.

**Darrell Etherington: I've only ever manually entered the whole meeting ID.

**Andi Bailey:** Wow.

**Andi Bailey:** George did it a fancy way today.

**Andi Bailey:** Earlier today.

**Andi Bailey:** Is the participant in the meeting invite?

**Andi Bailey:** Oh, I can add them.

**Andi Bailey:** Good idea.

**Andi Bailey:** I'm here, thank you, Golden Gate. I'm doing all of this and we have a relatively short thing today. I wanted to talk about the details.

**Golden Gate:** And can you hear us?

**Mara Leighton:** Perfect.

**Golden Gate:** Great.

**Golden Gate:** Okay, I want to look back.

**Golden Gate:** About the polish for articles, this has come up for a couple of clients across the board, and I think everybody's doing something a little bit differently in terms of how you think about polish.

**Golden Gate:** So I wanted to, like, just have a conversation about, like, what level you're editing, how much you think your MEs are editing, and, like, not just for accuracy, but in terms of, like, grammatical stuff.

**Golden Gate:** We do have a Grammarly, like, a shared Team Grammarly account.

**Golden Gate:** Are people using it?

**Golden Gate:** Do we need more seeds?

**Golden Gate:** Just, like, across the board, polish before it goes out to clients.

**Golden Gate:** I also know, like, our clients are very, all think about it a little bit differently, but, yeah, I just kind of want to go around the room and hear how we're thinking about it.

**Golden Gate:** Yeah, guess I can just start, yeah, I think for me it depends on the client, like I was telling you, I feel like I'm definitely more involved with Smith, just to, this is where doing this like big website refresh for them, and the client definitely just is, can be particular about something, so like, I'm just sort of like, going through essentially like everything that is going up on the site, just to make sure it is like, fitting what the client wants, but I would imagine that like, at a certain point, I won't need to do that, but just because we're like, in the early stages of this refresh, like, I'm just really wanting to make sure that like, because we were like, just given permission, to just like, run wild and publish without approval, so I'm just wanting to make sure we don't, that doesn't get revoked, because that would be, that would get fortunate, so yeah.

**Golden Gate:** But then with other clients, I can be a little less hands-on with editing just because they're already in such a good flow. How many individual pieces would you say each client is reading every week? With Smith, it was everything before. Up until they had the specific refreshes, I think they had stopped reading all the blog posts. But because this is more forward-facing in terms of the website, Maddie was looking at everything. I would imagine she'd probably still be looking pretty closely, and I imagine she's looking after we've published them too.

**Golden Gate:** But with other clients, I don't really get the sense they're coming through everything with a fine-toothed comb, except for School AI. They do have a teacher who actually goes through every article before they're willing to publish it.

**Golden Gate:** And even though they really haven't found, like, any issues, like, they still want that, like, person on their side that they trust looking at every piece of content before it goes up.

**Golden Gate:** Yeah.

**Golden Gate:** Okay.

**Golden Gate:** Mara?

**Mara Leighton:** Yeah.

**Mara Leighton:** Yeah.

**Mara Leighton:** I would say for my pod, I would say the people who really do go through each individual piece or, like, spend a lot of time on them and have feedback from, like, a piece-by-piece level, it's definitely in the minority.

**Mara Leighton:** I would say most, either we've gotten to a point where they trust us enough and they're not reviewing or, you know, they just, like, prefer not to.

**Mara Leighton:** But I'd say, like, for now, it's kind of strappy and rapid.

**Mara Leighton:** And I think we're getting to a point with them where, like, in a bit, for instance, they just kind of gave us the green light where they're not going to be reviewing each individual piece.

**Mara Leighton:** Yeah.

**Mara Leighton:** And then to answer your question on Polish and who's using Grammarly in the level of editing, I know both Vivek and Mariana use Grammarly.

**Mara Leighton:** We, like, just chatted about it.

**Mara Leighton:** So I know that is part of their internal, like, checklist.

**Golden Gate:** Yeah.

**Golden Gate:** And then, like, I know Vivek has caught, like, a lot of little, or is, like, pretty good at catching the little things.

**Golden Gate:** So is that for Grammarly or is she literally reading everything?

**Mara Leighton:** No, think, like, that would be giving a once-over to every piece.

**Mara Leighton:** Like, when he's out of office, I do the same.

**Mara Leighton:** So I'll go in and, like, read each individual piece or just, like, give it a scan and make sure there's nothing, like, glaring or no, like, repositioning that needs to happen.

**Mara Leighton:** So I believe he reviews every piece before it goes out, but it's not, like, an intensive review.

**Mara Leighton:** And I think that it also just depends on the CM as well.

**Mara Leighton:** Like, you know, some folks have been on the account for months and months and, like, they generally have pretty...

**Mara Leighton:** Great editorial judgment, and then if someone's newer to the account, think, you know, naturally a little more intensive.

**Golden Gate:** Yeah, okay.

**Golden Gate:** Daryl?

**Darrell Etherington: Yeah, we haven't, we've only ever had the one issue, and it was with Tam.

**Darrell Etherington: Yeah.

**Darrell Etherington: And then when Adasham investigated that, he was like, oh yeah, this was like pre-existing.

**Darrell Etherington: So he didn't like throw her under the bus or whatever, but it was like something that Ada had published or whatever.

**Darrell Etherington: And I think he identified the root cause.

**Darrell Etherington: But we found that like, the reason that was so exceptional is because like the stuff comes out pretty copy clean from the AI generation flows, especially the Claude ones.

**Darrell Etherington: He reads them all, but in that case, was, after he did like his investigation into what it was, it was actually errors introduced in the transcription process when it was pulled.

**Darrell Etherington: Or like from our doc into their CMS, and then maybe from an older version of their CMS into a newer version CMS.

**Darrell Etherington: He looked at the edit history, and he was like, oh yeah, this was like human error, not actually AI error.

**Golden Gate:** Yeah.

**Golden Gate:** Okay.

**Golden Gate:** So that's like something flagged for CMS, watching out for CMS stuff.

**Darrell Etherington: Yeah.

**Darrell Etherington: Because there was also this weird artifacting, like it took the alt tag and turned it into a description, but it was because they switched their article format.

**Golden Gate:** Yeah.

**Golden Gate:** yeah.

**Darrell Etherington: Okay.

**Darrell Etherington: Yeah.

**Golden Gate:** Interesting.

**Darrell Etherington: otherwise, yeah, like Carrie reads everything for the final edit.

**Darrell Etherington: The volumes that we do, we don't have any like PSEO or pseudo-PSEO at the moment.

**Darrell Etherington: Yeah.

**Darrell Etherington: So they all get a final read before they go over to my side.

**Golden Gate:** Yeah, that's the difference in terms of editorial versus PSEO. With the volumes we're publishing for some of the smaller ones, I feel like people are reading them, so I want to make sure.

**Golden Gate:** Jacob, do you have a sense of, like, how much Jeff is reading versus, like, Lannick Becerra publish?

**Jakub Rudnik: I think hers is the, closer to what others have described, of, like, low, like, reading through or a final check, but not the deep, deep edits.

**Jakub Rudnik: Jessalyn, I think, is, like, spending probably too much time on every piece of content would be my instinct from our conversations.

**Jakub Rudnik: Like, I'm glad for the quality, obviously, but that's where so many of her, she has way more concerns and things come up, but then, like, Jess, we are talking about that much less.

**Jakub Rudnik:** But I think that's Jessalyn's perfectionism — much of the content is really deep. I think Jessalyn does maybe the most editing among MEs, based on what I've seen, but that might be consistent across the board from hearing these overviews.

**Jakub Rudnik: And then like Tiro reads, they read everything, WebSec's used to until the content manager left.

**Jakub Rudnik: So it's been a mixed bag.

**Jakub Rudnik: Like I have some clients that give feedback, Seat reads every single thing and there's feedback and conversations on every article.

**Jakub Rudnik: Others, like they don't care what we're doing, just go for it.

**Jakub Rudnik: So it's like, that's kind of the most of the board.

**Golden Gate:** Okay.

**Golden Gate:** And are you guys leveraging Grimorling?

**Jakub Rudnik: That's a good question.

**Golden Gate:** I don't know that answer.

**Jakub Rudnik: Right.

**Jakub Rudnik: I'll double check that.

**Golden Gate:** Panzar, as our resident editor.

**Matthew Panzarino:** Well, that's loaded.

**Matthew Panzarino:** Excuse me.

**Golden Gate:** Like, I don't know how we think about this holistically.

**Golden Gate:** It does does seem like.

**Golden Gate:** It's client to client, but I want, I would like us to be more aware, like, which ones are trying to combing it.

**Matthew Panzarino:** There's probably, like, an elastic process that we need to define that is the baseline that gets adjusted for clients, right?

**Matthew Panzarino:** So, like, what is the process?

**Matthew Panzarino:** Who does review stuff, you know?

**Matthew Panzarino:** And I think that, unfortunately, is relatively variable because the quality, I shouldn't say quality, I don't want to talk about humans like that, but, like, the abilities of the CMs and MEs vary greatly.

**Golden Gate:** So if you have somebody who's an ME that also just happens to be a really detail-oriented editor, then you could read next to zero, right, as a director.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Same thing with the CM, you know, the ME could be like, oh, why am even reading this?

**Matthew Panzarino:** This is great, right?

**Matthew Panzarino:** And, like, eventually you get used to that working relationship.

**Matthew Panzarino:** So it's hard to, like, define a static process, but something elastic that's like, hey, the expectation is for the, you know.

**Matthew Panzarino:** First six weeks of an engagement, director reviews every piece, and then for the next 12 weeks, it ME reviews every piece, and then you're on autopilot or whatever with the CEM kind of submitting and allowing the client to then review the piece, because the client side is up to them, right?

**Matthew Panzarino:** But then we can say, hey, it's coming out of our world in a shape where we feel comfortable with it.

**Matthew Panzarino:** From my personal perspective, so I obviously am reviewing every piece for now for all these clients, so it's about 18 pieces a week I'm doing close reads on.

**Matthew Panzarino:** I don't have a standard ME-CM layer, so it feels a little different to me.

**Matthew Panzarino:** My goal, of course, is to make my life manageable, so I'm trying to make sure that we have enough post-processing in place to get it to where 18 pieces a week is pretty straightforward for me to do in half a day.

**Matthew Panzarino:** It takes me right now about two hours to do two clients, and then we'll probably, I don't know what it's going to take for me to do on Metronome, but it'll most likely take my legs.

**Matthew Panzarino:** Six hours to do Metronome, because their deliverables are ridiculous.

**Matthew Panzarino:** So I can't calibrate to Metronome, but on Monograph and Biologica, Biologica is pre-launch, so there's some asterisks there.

**Matthew Panzarino:** But in general, they are getting to a place where they're coming out of the pipelines within striking distance of a post-polishing clod, and then me doing maybe 10 minutes of review per article.

**Matthew Panzarino:** Like that's about where those clients are right now.

**Matthew Panzarino:** So we did two weeks worth of content for both Biologica and Monograph, by we, I mean myself and Nana.

**Matthew Panzarino:** Nana handling like admin and generation and stuff like that, and not really doing any proofreading, right?

**Golden Gate:** I'm not asking her to proofread them at all.

**Matthew Panzarino:** I'm just giving her prompt libraries and frameworks that she then applies.

**Matthew Panzarino:** And so I did, I think I did Monographs, she did Biologicas, and then she gave them all to me, and then I did a human review of them.

**Matthew Panzarino:** And we were able to do that all on Monday morning for both of those clients.

**Matthew Panzarino:** And that way we had two weeks worth of content done at the beginning of this week.

**Matthew Panzarino:** And then we're going to do it again.

**Matthew Panzarino:** So we'll be four weeks ahead.

**Matthew Panzarino:** And then we're going to do it again because I want to be like three to four weeks ahead with some elasticity for both of those clients.

**Matthew Panzarino:** And then Metronome, hopefully we get a renegotiation of what we're going to do for them next week.

**Matthew Panzarino:** But my experience with the quality that's coming out of the pipelines is it's extremely bad for Metronome, like very bad.

**Matthew Panzarino:** Sydney, of course, Sydney has been basically having to write all of their articles.

**Matthew Panzarino:** For Monograph, I'm able to get something within the 80th percentile out of the pipeline.

**Matthew Panzarino:** It's actually not bad.

**Matthew Panzarino:** And then Claude post-process to get it where it needs to go.

**Matthew Panzarino:** So with Biologica, the post-process there is Claude and then Human.

**Matthew Panzarino:** I didn't even know we had a Grammarly account, so I'm not running any of that.

**Matthew Panzarino:** But it looks fine grammatically to me.

**Matthew Panzarino:** Like, I'm working with the raw copy, and it seems okay.

**Matthew Panzarino:** I would say with Biologica, we just integrated the knowledge base post-process that Pedro created to apply the ingredients, and, you know, that hopefully will be helpful to others that work.

**Matthew Panzarino:** I am very anxious, to be honest, to just start working with the agentic workflows, because I think that they will improve the quality a lot, just from my experience.

**Matthew Panzarino:** Which is, basically, I'm so sorry, it's a long way of saying, like, I think two of them, which have more standard editorial engagements, need only 10 to 15 minutes of human review per piece, and that is the way I am handling it currently.

**Golden Gate:** Okay.

**Golden Gate:** Why do you think the metronome pipeline is so much worse?

**Matthew Panzarino:** We promised them way too much, or started, the scope creep was the problem.

**Golden Gate:** Oh, you mean, why is the pipeline bad?

**Golden Gate:** Yeah.

**Matthew Panzarino:** I actually think that we ran into the same issue that Rachel ran into, where it's not obeying the...

**Golden Gate:** It's not listening to the, yeah.

**Matthew Panzarino:** Yeah, so we filed a ticket on it and flagged Marcus, because I think he needs to apply the same reinforcement there.

**Matthew Panzarino:** Because it's, yeah, it, like, Yana was running it, and she was like, wow, like, here's new stuff that I didn't ask for, and here's a tangent that I didn't ask for.

**Matthew Panzarino:** The standard stuff.

**Matthew Panzarino:** And then at the other end, I'd say the copy is, like, a little meandering, a little dense.

**Matthew Panzarino:** I need to do a full review of their artifacts.

**Matthew Panzarino:** Like, I didn't write these artifacts.

**Matthew Panzarino:** You know, Ada and Sydney did.

**Matthew Panzarino:** And I'm not casting aspersions, but I haven't read them yet.

**Golden Gate:** Unfortunately, I haven't had a chance to.

**Matthew Panzarino:** So I don't know if there's some foibles that are being pulled from there.

**Matthew Panzarino:** I've seen a handful of things that my gut tells me if I go into the writing guidelines and stuff.

**Matthew Panzarino:** I'm like, this is semantically causing you issues, you know.

**Matthew Panzarino:** So there's some of that.

**Matthew Panzarino:** But I think at the root of it is the semantics of the underlying segmentation prompt that creates the individual chunks of the article, which are later assembled.

**Golden Gate:** I think that's the root of many of the issues, like the bullet points problem.

**Golden Gate:** Are there patterns that you've seen so far from rewriting artifacts in terms of semantic organization that we should be telling everybody not to do when they're generating artifacts even?

**Golden Gate:** It needs to be clean copy.

**Matthew Panzarino:** I think that's one thing.

**Matthew Panzarino:** People paste a bunch of random sentences in without context a lot.

**Matthew Panzarino:** I see that.

**Matthew Panzarino:** That's an issue.

**Matthew Panzarino:** needs to actually be, like imagine if you were reading it.

**Matthew Panzarino:** Could you understand what the hell you're saying, right?

**Matthew Panzarino:** Don't expect the LLM to understand because it needs the same context that a human would, roughly.

**Matthew Panzarino:** It just does it faster.

**Matthew Panzarino:** It doesn't do it any better.

**Matthew Panzarino:** In fact, it does it worse, right?

**Matthew Panzarino:** So I think it's just like, hey, H3 or H2 of what you actually wanted to do and then your supporting structure for what that wants to do.

**Matthew Panzarino:** And either a series of headers underneath that with...

**Matthew Panzarino:** Supporting do's and don'ts, that's the rough structure, I think that's good.

**Matthew Panzarino:** I don't think this varies too much from what the good examples have been that are out there, like DataGrader, Gitpod, or frankly, like the ones that we've done, you know, that we've refreshed.

**Matthew Panzarino:** So I'm not saying anything revelatory here, but I have noticed looking at people's artifacts when they ask me questions, one of the first things I do is look at the artifacts.

**Matthew Panzarino:** They're like, oh, this is bad.

**Matthew Panzarino:** I'm like, okay, cool.

**Matthew Panzarino:** Let me look at the artifacts. You know, like, I can't even understand what this artifact is.

**Matthew Panzarino:** Like, I think that's probably one of the major issues.

**Matthew Panzarino:** And then every once in while, I'm still seeing artifacts that are maybe 250 words long.

**Matthew Panzarino:** And I'm like, whoa, no wonder you're having trouble.

**Matthew Panzarino:** So, I mean, the fact is, is that the token window is 4,000 tokens.

**Matthew Panzarino:** That's huge, right?

**Matthew Panzarino:** We can stuff it full of a bunch of stuff.

**Matthew Panzarino:** And yeah, you know, you may need to reinforce it now and then.

**Matthew Panzarino:** And right now we're doing that with Claude.

**Matthew Panzarino:** But I think it's, it's actually straightforward to file a ticket with Eng to get a style adapter built to go after the article draft.

**Matthew Panzarino:** I would recommend that for a lot of people.

**Matthew Panzarino:** And basically what that means is it applies the writing guidelines again.

**Matthew Panzarino:** It just says, are you sure?

**Matthew Panzarino:** You know, you adhered to these?

**Matthew Panzarino:** And that's probably a few minutes worth of work for the Inge team.

**Matthew Panzarino:** I'd recommend it in, I think, a lot of cases.

**Matthew Panzarino:** I think we did away with that when we got out of AirOps.

**Matthew Panzarino:** Because remember, AirOps, applied it twice.

**Matthew Panzarino:** And we were like, why?

**Matthew Panzarino:** And in some ways, that was true.

**Matthew Panzarino:** But I think it's probably best that we add it back.

**Golden Gate:** Should we add it back to the templated workflow rather than having them add it back every time they build the pipeline?

**Matthew Panzarino:** Well, the standard pipeline template, which is somewhere.

**Matthew Panzarino:** I actually don't even know where that lives.

**Matthew Panzarino:** But that standard one, the article generation standard, that I think should just be updated to add that.

**Matthew Panzarino:** But you will need to add it to the existing pipelines.

**Matthew Panzarino:** But it is in the prompt library, right?

**Matthew Panzarino:** Or in the workflow library.

**Matthew Panzarino:** So you can just grab that workflow name and then add it.

**Matthew Panzarino:** It's only a few minutes worth of work in the workflow.

**Matthew Panzarino:** GAML, but I wouldn't want CMs or most MEs to be doing that.

**Matthew Panzarino:** that's We need to handle it at this level.

**Golden Gate:** Right.

**Golden Gate:** Yeah, is there a reason why we got rid of the articles' feedback?

**Golden Gate:** Where you could, like, those in Aerox where we did that?

**Matthew Panzarino:** Yeah, Ask.ai, that's why.

**Matthew Panzarino:** The Ask.ai tool is supposed to be doing that.

**Matthew Panzarino:** Because remember the feedback one?

**Matthew Panzarino:** If that wasn't about applying writing guidelines, that was about basically line editing.

**Matthew Panzarino:** It is what now the Ask.ai tool would be doing, like, reflow this into bullets, remove all instances of the name, you know, Coca-Cola and replaced with Pepsi.

**Matthew Panzarino:** So, for that, by the way, you may have noticed that they enabled the sidebar for Ask.ai.

**Matthew Panzarino:** You may have seen that.

**Matthew Panzarino:** If not, you can go look at it, which is, I think, a much nicer.

**Matthew Panzarino:** I mean, it's what people are used to, right?

**Matthew Panzarino:** At least it's only an interface change.

**Matthew Panzarino:** The functionality, I think, is roughly the same.

**Matthew Panzarino:** But I think it's much nicer because you can kind of get a little bit of a context.

**Matthew Panzarino:** So, if you pop into any of your editors and then....ai tool.

**Matthew Panzarino:** ...

**Matthew Panzarino:** ...

**Matthew Panzarino:** ...

**Matthew Panzarino:** Invoke your editor, you'll see it pop into a sidebar, and the ASCII tool hovers there now.

**Golden Gate:** Okay.

**Matthew Panzarino:** But that should, you know, there's arguments for that to work differently.

**Golden Gate:** It's just undecided how it should work.

**Golden Gate:** Yeah.

**Matthew Panzarino:** Right.

**Matthew Panzarino:** But that's where the feedback workflow went.

**Golden Gate:** All right, cool. Do you have any thoughts on Polished?

**Golden Gate:** I mean, Sydney's really good, so she spends a lot of time thinking about it.

**Golden Gate:** Yeah, she spends a ton of time.

**Golden Gate:** And I guess with, like, Webflow, I shouldn't share my screen.

**Golden Gate:** I think, so two things on Polished, and then the other one just on, like, I know this isn't a super element, just, like, how you push back, I guess, for clients that ask for more and more, because we've got that for, not necessarily for Webflow, but, like, for Augment, and then Webflow unintentionally, they just kind of push us.

**Golden Gate:** But we've been doing stuff where we separate out everything we're doing into pieces. For clients that are purely on editorial, it's much more helpful to let's get definition articles right and not have everything mixed together, because that makes MEs' lives easier. Should we document that in the director chat?

**Golden Gate:** And it's helpful for Webflow, and then, I don't know if anyone has, like, a crazy client, like, for example, for, like, augment code.

**Golden Gate:** Like, they're doing so many random things, or, like, if we didn't have this, they just keep asking for more, and then we lose track, and there's no way to say, like, all right, we can only prioritize one thing here, like, which one should it be?

**Golden Gate:** Yeah.

**Golden Gate:** And do you have, like, a deprioritized tag for those, too?

**Golden Gate:** Not really, I think.

**Golden Gate:** Or, like, a time that it takes?

**Golden Gate:** I was thinking about that. It might help to weight effort on items — make this a three in terms of effort. I think it's meant to roughly shape the conversation.

**Golden Gate:** Yeah.

**Golden Gate:** And then in terms of polish, I don't know, for all of them, like I think I've had the benefit of having a different workflow for Webflow integration pages.

**Golden Gate:** So I don't know if it's as relevant, but like I went from reviewing every article with the client, even like one article to now we do 15 a week and Sydney does all of them.

**Golden Gate:** But like that took probably like three or four weeks of like just hammering like one article.

**Golden Gate:** Yeah.

**Golden Gate:** Which is kind of crazy.

**Golden Gate:** Like don't know if we have that.

**Golden Gate:** Well, I mean, I'm curious like for clients like Seat, where they've been on client for so long and they're still going back and forth, like what are we missing that they need to, that they still don't have the trust, you know?

**Golden Gate:** So that's another question. I can change the workflow, so we have the benefit of it eventually getting fixed. I don't know if that works for editorial, where the calibration is always stuck in whether the ME or CM followed the instructions — it's much harder to iterate that forward and make sure it doesn't roll backwards compared to a workflow.

**Golden Gate:** So your tip though, for if a client is sort of like pushing for more, it's essentially kind of show them.

**Golden Gate:** I think what's helpful is to like, roughly shape what you're doing for them, and even for augment, like we'll lay out things like strategy, like if we're doing A, E, T, O, and SEO, we're helping you build the website.

**Golden Gate:** Just like remind them, like here's everything we're doing.

**Golden Gate:** Yeah, and I've found like, if you have this up, and then you say, like, we're like really hitting the limit of like, you know, hard time.

**Golden Gate:** Here in our budget, like not budget, but like our capacity, or what we decree, like, you know, I understand like we want social posts, right, or something, like this to be fixed, but like what that means, like, is there, can we shift the prioritization around here, like, do you think social posts are more important than us getting listicles to a good place, you know, we were like, um.

**Golden Gate:** Okay, I really like that approach.

**Matthew Panzarino:** I think this speaks into something, which is like all of the client facing spaces that we have, just need to be cleaner, right, like there's just if they're really muddy right now, that goes from content OS to notion to dashboards, like everything just needs to be really crispy, because we just default to share, which is fine, you know, it's all good.

**Matthew Panzarino:** But I think that it creates clarity about conversations like workload, as Jason was mentioning here, or work streams that we're for him.

**Matthew Panzarino:** Just a thought, and it's not a quick solve, but I think all the client-facing spaces need to be, I think, more polished.

**Golden Gate:** Yeah.

**Golden Gate:** Are any of you guys as a team implementing what Gary showed the other day in terms of having an app for task management?

**Matthew Panzarino:** Yeah, I want to. I've just been trying to get up to speed on everything, but I've already had it in our list of to-dos.

**Golden Gate:** I think it's a great way to handle it.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Clients should just be ticking boxes.

**Matthew Panzarino:** Now, some clients may want more, and I'm happy to have them access to more, but I want one view, which, like, you know, which is what I want internally.

**Matthew Panzarino:** Like, honestly, internally, for me, like, I tell Nana, it's like, I don't want to go, like, to figure out what we're trying to do this week.

**Matthew Panzarino:** I honestly just want one long list of deliverables.

**Matthew Panzarino:** I don't care what client is for.

**Matthew Panzarino:** Like, you can context switch on me every other line.

**Matthew Panzarino:** But if I can see a tick box of...

**Matthew Panzarino:** Everything that we have due this week, and we can tick it off, like, that's how my brain works.

**Matthew Panzarino:** I don't know how you guys work, but, like, I don't want, like, oh, we have this for them, and that for them.

**Matthew Panzarino:** Okay, cool.

**Matthew Panzarino:** Do I need to go to their space to look at that, and their space to look at that?

**Matthew Panzarino:** Which I think is more of, like, an atlas thing.

**Matthew Panzarino:** Like, we should be able to, as a team, say, hey, I am on team Biologica, Metronome, and Monograph, and I need to know all my deliverables, and we've defined those deliverables, and then we have assigned those deliverables, and then I just get a list.

**Matthew Panzarino:** Now, I'm not saying this is something we are going to build tomorrow, but eventually, I'm just throwing it out there.

**Matthew Panzarino:** It needs to happen.

**Matthew Panzarino:** Right now, we can build it in linear, obviously, and where I can go into a linear task and just see everything, right?

**Matthew Panzarino:** And I'm a box ticker, right?

**Matthew Panzarino:** If I could tick all my boxes, and I'll blast through tasks, right?

**Matthew Panzarino:** I'll get them done in a day.

**Matthew Panzarino:** But if they're all over the place, I'll do two, and then somebody will say something, and I'll be like, and then, you know, and then I'll come back, and I'm like, where the hell am I?

**Matthew Panzarino:** You know, so just a thought.

**Matthew Panzarino:** It's probably something that Atlas needs.

**Matthew Panzarino:** And I'm almost positive.

**Matthew Panzarino:** Daniel has mentioned something about like a task manager or something, but just throwing it out there.

**Golden Gate:** He wants to pull their apps and outlets, but that's not the priority right now. We want to give visibility into how people are managing that stuff. For clients pushing for extra work streams, Gary's task management app seems like a great solution.

**Golden Gate:** Thanks, guys. Have a good one.
