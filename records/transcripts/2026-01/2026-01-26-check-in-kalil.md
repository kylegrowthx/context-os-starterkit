# Check-in: Kalil

<metadata>
date: 2026-01-26
time: 19:07 UTC
duration: 24 minutes 20 seconds
organizer: kalil@growthx.ai
enriched_on: 2026-02-28 14:32 UTC
fathom_recording_id: 117172570
fathom_url: https://fathom.video/calls/542797092
share_url: https://fathom.video/share/TnymjxYeQfkjbYz-cu5vFYoYoMUKBG_R
source: fathom
participants:
  - name: Matthew Panzarino
    email: matthew@growthx.ai
    affiliation: GrowthX
    role: Leader
  - name: Kalil Magtoto
    email: kalil@growthx.ai
    affiliation: GrowthX
    role: Content Operator
</metadata>

---

## Summary

Matthew Panzarino checks in with Kalil Magtoto on pipeline efficiency, discovering Kalil achieves 15–45 minute edits per article—well within Q1 targets. The discussion pivots to systemic bottlenecks: AI-generated broken links, manual artifact maintenance across clients, and the strategic importance of aggressive ticket filing to unblock engineering. Matthew reframes high edit times (>1.5 hours) as signals of pipeline failure, not operator inadequacy, and outlines a future Atlas feature that automates context engineering to eliminate artifact juggling and enable operators to scale from 1–4+ clients.

---

## Context

Kalil operates content pipelines for multiple clients using Atlas, GrowthX's proprietary content generation and editing system. His role bridges content operations and product feedback—each edit and client request surfaces insights into how pipelines perform and where engineering can improve. Matthew, as a leader overseeing editorial quality and process, uses Time Doctor data to identify performance patterns across the team and coach operators toward efficiency. This meeting sits at a critical inflection: Kalil's documented workflow reveals the shift from "more manual effort" to "better pipeline design," and Matthew's scaling vision (4+ clients per operator) depends on automation of context engineering tasks that currently consume hours per week in manual artifact updates.

---

## Relevance

- **Pipeline Performance**: Kalil's 15–45 minute edit cycles benchmark strong performance. Substantive edits (reblocking, SEO, fact-check, link review) consume 50% of time; copy edit and final polish, 5–10%. This data informs Q1 efficiency targets and identifies where Atlas can automate.
- **Bottleneck Analysis**: Link hallucinations (Atlas generating broken URLs) force manual verification of every link and weekly manual repository updates. An automated SERP search function would save 10–15 minutes per slow cycle.
- **Scaling Model**: Matthew's vision of operators managing 4+ clients depends on Atlas automating "artifact juggling"—the current manual process of tracking client messaging updates across versions and propagating them into instructions and guidelines. This becomes the inflection point for product development.
- **Performance Tiers & Corrective Action**: Matthew establishes a clear diagnostic framework: <30 min = green/scalable; >1.5 hrs = red/pipeline failure. High edit times signal conflicting instructions or flawed artifacts, not editor inadequacy. The correct response is pipeline debugging (test variations, file tickets) not more manual effort.
- **Engineering Engagement**: Matthew emphasizes aggressive ticket filing—both for Kalil's immediate bottlenecks and for the product team's long-term roadmap. Many pipeline issues are either bug fixes or features that benefit the entire team, not just the filing operator.

---

## Overview

- **Kalil's workflow is efficient (15–45 min/article),** meeting the Q1 goal of \<30 mins. The main bottleneck is the substantive edit, which consumes \~50% of the time.
- **The primary issue is AI hallucinating broken links,** requiring manual verification. A future Atlas feature will automate this by using client edits to self-improve pipelines.
- **High edit times (\>1.5 hrs) signal a pipeline failure,** not a need for more manual effort. The correct action is to debug the pipeline (instructions, artifacts) or file an engineering ticket.
- **The long-term goal is for operators to manage 4+ clients,** enabled by Atlas automating context engineering to eliminate the current artifact-juggling bottleneck.

---

## Key Topics

### Pipeline Performance & Editing Workflow

  - **Current Performance:** Kalil's workflow is efficient, with edits taking 15–45 minutes per article.
      - **Substantive Edit (50% of time):** The main bottleneck.
          - **Process:** Reblocking → SEO check → Fact check → Manual review.
          - **Wait Time:** 5–10 minutes spent waiting for Atlas to process edits.
      - **Copy Edit (5–10% of time):** Quick final polish.
  - **Primary Bottleneck: Link Hallucinations**
      - **Problem:** Atlas generates broken links, requiring manual verification of every link.
      - **Current Fix:** Manually update an internal link repository weekly.
      - **Desired Fix:** An automated SERP search function to validate links.

### The Problem of High Edit Times

  - **Performance Tiers:**
      - **Green (\<30 min):** Efficient and scalable.
      - **Red (\>1.5 hrs):** Signals a pipeline failure.
  - **Why High Edit Times Are Inefficient:**
      - Editing poor LLM output is like untangling a "spaghetti mess" because the editor doesn't know the AI's logic.
      - This is less efficient than rewriting the article from scratch.
  - **Root Causes of High Edit Times:**
      - **Process Failure:** An operator edits poor output instead of debugging the pipeline.
      - **Architectural Failure:** Conflicting instructions or flawed artifacts.
  - **Corrective Action:**
      - **Test Pipeline Variations:** Run the pipeline with different instructions (detailed, stripped-down) to find the optimal configuration.
      - **File Engineering Tickets:** Aggressively report pipeline issues to improve the product for everyone.

### The Solution: Automated Context Engineering

  - **Current Bottleneck:** Manual "artifact juggling" (e.g., updating client messaging) is time-consuming and error-prone.
  - **Future Atlas Feature:** Automate context engineering.
      - **Mechanism:** Atlas will analyze client edits and feedback to automatically update pipeline artifacts (e.g., writing guidelines, company context).
      - **Benefit:** Eliminates manual artifact management, freeing operators to focus on higher-value work.

---

## Action Items

**Kalil Magtoto (GrowthX)**
- File Linear tickets for recurring pipeline issues; triage and prioritize (recurring patterns documented across 27+ articles).
- Collaborate with engineering on pipeline variations testing and artifact debugging.
- Scale toward 4+ client management as Atlas automates context engineering in future releases.

---

## Transcript

**Kalil Magtoto:** Good afternoon, or good morning for you still.

**Matthew Panzarino:** Good. Hey, give me just one moment—I'm going to refill my coffee. And sorry I'm late. I've just been back to backs. So give me just one second.

**Kalil Magtoto:** Thank you.

**Matthew Panzarino:** Okay. Hi. How are you doing?

**Kalil Magtoto:** Hello. I'm doing good. It's cold here in Canada. How are you?

**Matthew Panzarino:** Good. You know, it's about 65 degrees high today. So it's not quite as bad here.

**Kalil Magtoto:** Actually, I don't know what that means. 18—that's perfect. That's the best weather.

**Matthew Panzarino:** Yeah, I know. We feel a little bit... we don't really feel guilty about it, to be honest. It is what it is. We do pay a lot of taxes, so we figure.

**Kalil Magtoto:** We choose where we live.

**Matthew Panzarino:** Yeah, exactly. But cool. Yeah. I wanted to check in, see how things are going. You know, from the work that you do with your pipelines and how thoughtful you are, I don't have any super concerns. I think you're very proactive about it and take a good process-oriented approach. So no red flags from my end. I'm just really asking how are you doing? How are you feeling about the progress towards making your pipelines performant? If you have any clients or bloggers—things like that—I just wanted to kind of catch up in general.

**Kalil Magtoto:** My tools for my clients are going smooth every week. There's something to improve upon, but as expected. Ever since we made those major changes in the very beginning, everything has been great. It takes me 15 to, at the worst, 45 minutes to edit an article. And that's when, maybe, there's a section that's bloating the article, then I have to remove chunks, make things more concise, or review links. The thing is, I don't know what it is with AI, but it hallucinates links. There's no 404s that we found initially, and then I'll manually check each one, and I'm like, wow, half of these links don't exist. That's Perplexity crawled inside of Atlas, I think. So I don't think it's an us thing. I think it's AI getting confused along the way and creating stuff. I have a workaround—I manually update an internal link repo. Every week, we have five or seven new articles, refresh that. I find new articles that should be in there, so I add them in. It would be nice if at some point it could SERP—like, actually search what are the working links and then update that for me. That would be a big win. Save me maybe 10–15 minutes on the slow end.

**Matthew Panzarino:** Well, that's great. I mean, that's good. Iterative progress is great there. Plus, you're always going to have a little bit of the dice roll, the non-determinant aspect of how LLMs work. But I think sometimes the solution is to separate out the processes into finite chunks. If you're making progress every week, that's the good thing. If you had to characterize what your biggest chunk of time is, categorized by time, when it comes to fixing LLM drift or other issues—if you had to pie chart it, what's the biggest chunk?

**Kalil Magtoto:** So right now, all of my workflows go substantive edit, then copy edit, then final polish if needed. Sometimes the copy edit just catches everything, and then I read and I'm like, okay, this is good. So in a pie chart, 50% is substantive edit. I'm just waiting. And I tried this the other day where I was like, okay, while I'm waiting, let me do something else. But my brain just doesn't work well when it's trying to split across articles. I just want to get one done. So while I'm waiting—cup of coffee—the timer is still running. That's probably five to ten minutes where I'm just not really doing anything, staring at a screen. Then I'm looking at it, patching, flagging, whatever it's doing. But I want to stay on the article. The substantive edit is like 50% of the time, so anywhere from 15 to 20 minutes. First, I do reblocking if needed. And then I do an SEO check to see if we could win on any of these H2s, H3s. Then fact check. Once the fact check is complete, I get a thumbs up—hey, this is good for you, I'm flagging this for your review. Then I look manually one by one—okay, this is good, this is false. I remove that or fix the links, and then I move into copy edit phase. Copy edit takes about five minutes, maybe ten if it's really egregious. And then I copy all the metadata and I'm done. Then I move on to the next thing. Sometimes I'll take a break between edits, just because I'm turned on for half an hour.

**Matthew Panzarino:** Yeah, exactly.

**Kalil Magtoto:** Otherwise, that's my time.

**Matthew Panzarino:** Yeah, okay. Cool. I mean, all that sounds reasonable. You just bind your slivers as you go and chip away. It's definitely in light green territory as far as what I'm seeing from most people's edits. And certainly, half an hour or less is solid green territory. We're trying to trend everybody towards 30 minutes during Q1 and then less once we ship the new Atlas updates. Now I see Time Doctor data, which is what I needed. I can see where people are struggling and deploy assistance. On the low side, I see eight to twelve minutes per piece—that's awesome. And then on the high side, five or six hours. I apologize—I'm not bored by this conversation; it's just late morning. Five or six hours is like, you might as well write it manually and do the research and write the article. That's deep red territory. What happens is you end up in a worse problem because when you edit somebody else's work, you don't know the path they took or the logical choices they made to include or exclude things. I largely self-edited my content over 15 years.

**Matthew Panzarino:** I generally didn't work with a whole lot of editors, although I had wonderful copy editors who saved me many times every article. I'm not counting copy editing, but from a structural editing standpoint, I edited myself for the vast majority of my career. But most people cannot. The reason is because their thought processes are really clear to them. It's really hard for them to take the position of someone outside themselves and say, can somebody else understand how I got to this place from here?

**Matthew Panzarino:** And that is very, the flip side of that coin is extremely obvious when you edit an LLM's piece of content.

**Matthew Panzarino:** Because you're like, I.

**Matthew Panzarino:** I don't know what thought processes it used to link these things or to get this thing here from there.

**Matthew Panzarino:** And therefore, it is very hard for you to take something that is bad and edit it to be good because you don't know what to cut.

**Matthew Panzarino:** You're like, I can cut this narrative thread, you know, that appears here, here, and here because I remember it because I wrote it, right?

**Matthew Panzarino:** Like I remember these narrative pieces were all here.

**Matthew Panzarino:** And so it's very difficult to like rip those things out, like grab the end of them and pull them out and then have what's left still make coherent sense.

**Matthew Panzarino:** So when the edit times balloon to over an hour and a half, my gut instinct, which is usually correct, is that there are either a problem with the artifacts or instructions that we've given the pipeline.

**Matthew Panzarino:** Usually, because ipso facto, if one client can get delivery within eight minutes of pretty straightforward workman-like content, it's not like Tinker Toys children's content or anything.

**Matthew Panzarino:** It's solid.

**Matthew Panzarino:** If one pipeline can generate that within that amount of work and the client is happy and the content is performant, like it is trending upwards in traffic and is being cited by LLMs.

**Matthew Panzarino:** So it's not just like, we delivered it, we're free.

**Matthew Panzarino:** It's like, actually, it performs.

**Matthew Panzarino:** It is part of the whole positive feedback loop.

**Matthew Panzarino:** Then, if somebody is delivering something where they're like, it's taking me an hour and a half, there is either a process problem or an architectural problem.

**Matthew Panzarino:** It's one of the two, right?

**Matthew Panzarino:** Either you are holding yourself to a ridiculous standard and you could probably have let this content go half an hour ago, which is happening in some cases because people are just different editors.

**Matthew Panzarino:** They're more obsessive and it's like, hey, chill out.

**Matthew Panzarino:** Like, it's fine.

**Matthew Panzarino:** Let it go.

**Matthew Panzarino:** You know, like, let it go.

**Matthew Panzarino:** It's fine.

**Matthew Panzarino:** It's going to perform.

**Matthew Panzarino:** Clients are going to be happy.

**Matthew Panzarino:** We're good.

**Matthew Panzarino:** Right?

**Matthew Panzarino:** Like, don't worry about it.

**Matthew Panzarino:** Every piece can't be your magnum opus.

**Matthew Panzarino:** It's just not the way it works.

**Matthew Panzarino:** Or it's a process problem where it's like, okay, there's a blind spot in how they're interacting with the pipeline in that they aren't seeing that the instructions that they're giving it are causing it to go off into the wilderness in a way that is not just the normal LLM thing where it's going to take a different path, but it truly is like going off here.

**Matthew Panzarino:** And instead of saying, oh, you failed, right, to Atlas.

**Matthew Panzarino:** Like, you failed.

**Matthew Panzarino:** I need to give you different instructions or I need to have somebody come and help me engineer this pipeline or whatever.

**Matthew Panzarino:** They're just editing the piece.

**Matthew Panzarino:** And it's like, I think too many people think of it like, I ran it once and I'm just have to edit this output.

**Matthew Panzarino:** It's like, no, run it like five times, run it six different ways.

**Matthew Panzarino:** Like, give it a stripped down set of instructions.

**Matthew Panzarino:** Give it a really detailed set of instructions.

**Matthew Panzarino:** it a medium set of instructions.

**Matthew Panzarino:** You know, run it with these artifacts, change the artifacts, run it again, get six different versions of it, read, take a half hour to read those versions and go, oh, this one's so much closer to the ballpark.

**Matthew Panzarino:** Cool.

**Matthew Panzarino:** This is where I need to be, right?

**Matthew Panzarino:** Rather than just running it once, getting a mess and then trying to untangle the spaghetti mess for five hours.

**Matthew Panzarino:** You know, and it's like, don't do that.

**Matthew Panzarino:** That's not, that's not how the company works.

**Matthew Panzarino:** It's not how it's supposed to work.

**Matthew Panzarino:** So, in some cases, it's, hey, take more personal responsibility.

**Matthew Panzarino:** In some cases, it's like, take less personal responsibility almost.

**Matthew Panzarino:** Like, blame what's actually happening, which is that the pipeline is not producing something that's even in the realm of editable.

**Matthew Panzarino:** And if that's the case, now we need to retcon the pipeline, you know, adjust it, tweak it.

**Kalil Magtoto:** Yeah, we're not, I'm not yet there.

**Kalil Magtoto:** I, I, I always think back to the metronome example.

**Kalil Magtoto:** I'm so glad that you like.

**Kalil Magtoto:** flagged me to take a look at that.

**Kalil Magtoto:** And, like, three articles was enough for me to go, oh, so this is what I'm working towards.

**Kalil Magtoto:** I'd love to just, like, I should do this.

**Kalil Magtoto:** Just, like, talk to an engineer, like, in a meeting when they have time.

**Kalil Magtoto:** And then, like, pick their brain on an actual pipeline and say, like, honestly, this is every single time I've documented across 27 articles that I do this.

**Kalil Magtoto:** It's exact same thing.

**Kalil Magtoto:** How would you approach this issue so that, you know, like, I know I can file a ticket and get you to do this.

**Kalil Magtoto:** But I also want to be able to get to a point where, like, I'm doing this across 10 clients and fixing them.

**Kalil Magtoto:** Like, it would be cool if I could do that.

**Kalil Magtoto:** At least I'm personally interested in it.

**Kalil Magtoto:** That would be a good opportunity.

**Matthew Panzarino:** Hex is a new client. And what I'm about to tell you will be built into Atlas in the very near future. The good news is you don't have to build that yourself. It's coming. If a client makes suggestions, updates, and changes to a piece of content on Atlas, and Atlas is able to understand where that needs to be tweaked in the artifacts or what needs to be added to instructions to properly produce for that client in the future, then you don't have to collate across Google Docs or cloud projects, tracking consistent changes across clients. Instead, Atlas will flag those changes and engineering will implement them automatically.

**Kalil Magtoto:** Yeah, because artifact juggling hurts my brain. I spend time documenting version 2.1 to version 2.9, like, did I update this one? I'm keeping track, but it does take time. That'd be cool. One of my new clients, Hex, I'm about four weeks out from handoff. We're getting their times down, but they're still providing feedback after the sprint. It's drastically changed their artifact ecosystem. They have new messaging, and I'm wondering, is this always the case? When a client evolves and has new messaging, do we always need to overhaul the artifacts? How does that work?

**Matthew Panzarino:** That's how it's supposed to work. Yeah, I think it does. Context engineering is a whole separate skill set. And it's not really viable to do it at such a rapid pace without creating a bottleneck. So the system has to do it. That's why it's going to be built in. When tweaks and changes are made to a piece, Atlas needs to ask: where does this belong? Is it a post-processing instruction? Part of the writing guidelines? An overarching theme? A precise instruction for the post-processor? Or is it a company context problem? For example, you've changed positioning six times, but the company context states they position themselves in X way. Well, we probably need to update how they position themselves.

**Kalil Magtoto:** And then Atlas will handle this moving forward.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Right now that loop is only as short as you can make it in a given work week. You fix 12 problems, get client deliverables out, then set aside time to parse those issues, see if they're consistent, and affect changes in the artifacts. That's absolutely fine, and it's skill building. But we know it's not practicable because we have great editors who aren't necessarily context engineers. That's a skill set you have to build—it's a muscle. Some people have capacity for it, some don't. I view the production layer as an avatar for our virtual customers. Some are comfortable with a feedback loop where they update context and provide new information. Others just want us to write the article so they can edit it. Either way, it's better if we represent this internally first, because then we build the impetus to create new Atlas capacities. There are places where people can't update their artifacts, don't know how, or there's no feedback loop between edits. Every edit should trigger a question: why did you have to edit this? Was it the instructions? Your interpretation? Or did you never tell me you wanted this, which is probably the case most of the time—over nine times out of ten. When someone says their pipeline is bad, I find it's trying to rectify conflicting instructions that disagree with writing guidelines or other artifacts. Sometimes it's obvious, sometimes subtle and nuanced. It's hard work to untangle that knot—especially when instructions appear to agree on the surface but have semantic conflicts in how they're positioned. Something as subtle as providing an example that doesn't incorporate the writing guidelines can cause problems. And when you're doing all this client work with four or five artifacts across two, three, or four clients, it becomes a lot of juggling. So the system needs to do more of that.

**Kalil Magtoto:** Thank you.

**Matthew Panzarino:** I'm looking forward to that. It'll leave more headroom for you to do some of it, but you won't have to worry about suggestions falling out of the loop. If you've edited five pieces or the client has given feedback, all of those suggestions are taken into account.

**Kalil Magtoto:** Then I can take on four, five, six clients because Atlas took that on. Yeah, I get it.

**Matthew Panzarino:** Yeah, you build capacity for yourself and the team, and that's how we do it. When people get nervous about taking three or four clients—and four clients is the goal—they're usually people who haven't built capacity yet because their pipelines haven't been worked on enough by engineering or them, or a bit of both. I'm not expecting people to become pipeline engineers. It's not practicable. But the ENG team is there. Linear is there. File a ticket. Please be aggressive about it. They'll tell you no if they don't think it's a system problem. If it's you, that's okay—just file the ticket. Anything you clear off your plate to build efficiency helps you in the near term and helps the product long-term. A lot of these issues filed become bug fixes or new features. So it's additive, helps the whole team, and then helps you in the near term.

**Kalil Magtoto:** Awesome. Thank you very much. I look forward to this.

**Matthew Panzarino:** Great. Sounds good. We'll keep checking in. I think you're doing great. Your documentation is solid. Your process-oriented mindset is great. I don't have any red flags on how you're approaching things. You're approaching them well. Just continue building efficiencies for yourself.

**Kalil Magtoto:** I think you're going to be fine. Thank you very much. Yeah. Thanks, Kalil. Ciao. Have a good one.
