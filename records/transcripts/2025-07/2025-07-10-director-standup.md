# Director Standup

<metadata>
date: 2025-07-10
time: 19:00 UTC
duration: 30 minutes
organizer: Darrell Etherington (GrowthX)
participants: Andi Bailey (GrowthX), Darrell Etherington (GrowthX), Jakub Rudnik (GrowthX), Matthew Panzarino (GrowthX), Jason Gong (GrowthX)
fathom_recording_id: 73468703
fathom_url: https://fathom.video/calls/347843171
share_url: https://fathom.video/share/6uvucJkPWPJZNyZbdHhdx-CzzWV6pBCX
source: fathom
enriched_on: 2026-03-03 12:00 UTC
</metadata>

---

## Summary

GrowthX directors tackled the persistent challenge of defining the managing editor role that spans multiple skill areas—production, research, and strategy—across different pod structures. The team discussed workflow manipulation difficulties that are pushing some managing editors to resort to ChatGPT rewrites to meet quality standards, and explored systemic solutions like FAQ chatbots and knowledge-sharing formats. Three key client accounts need attention: York shows strong improvement and could be a case study, while Rapid and Galileo (both Mara's accounts) need focus before Monday's discussion with Marcel.

---

## Context

This is GrowthX's internal director standup—a weekly check-in among the delivery leadership team (Andi Bailey, Darrell Etherington, Jakub Rudnik, Matthew Panzarino, and Jason Gong) to align on operations, client health, and systemic improvements. The meeting happened just before a major Monday alignment call with Marcel about key accounts and strategy. The managing editor role definition discussion stemmed from the challenge of hiring for a position that spans three distinct skill buckets Marcel had outlined, with the team discovering that existing managing editors (Carrie and Edesham) excel in fundamentally different areas—production vs. research/project management—yet both struggle with workflow manipulation and ticket writing. The broader context reflects ongoing friction between GrowthX's desire for scalable knowledge transfer and the reality that education at the organization works best through high-touch, one-on-one training.

---

## Relevance

**To GrowthX Delivery:**
- Managing editor role definition remains ambiguous—requires clarity on whether the role requires all three skill areas (production, research, strategy) or if Marcel's "one of each per pod" model is the working standard. This impacts hiring and performance expectations.
- ChatGPT rewriting of Atlas workflow outputs is being used at scale (Edesham's case) to meet quality standards—flags that workflows need engineering fixes, not workarounds. Matthew Panzarino documenting these gaps with recorded CM one-on-ones to feed back to engineering.
- Ismail's custom style adapter hack for Rapid/Brandt (addressing ignored writing guidelines) shows individual solutions working in isolation. Risk: proliferation of unsystemized hacks that aren't productized or generalized.
- Ticket writing remains a universal blind spot—"communication back to ENG in a consumable, practical way" is a cross-team problem acknowledged by all directors including Matthew and Jason.
- Knowledge transfer formats are failing at scale. Looms, Notion docs, guides not being consumed unless presented at point-of-need. Matthew's one-on-one CM sessions and NotepicLM podcast repurposing may offer better formats than self-service documentation.

**To GrowthX Business Development:**
- York account showing strong improvement—Darrell suggests running a learning session to extract what's working and why (isolation of account from competing priorities may be a key factor). Potential reference case.
- Rapid and Galileo (Mara's accounts) flagged as needing immediate attention before Monday Marcel discussion. Suggests account health concerns.
- Webflow strategy setting in progress—Jakub planning deep-dive call with Jesse to finalize requirements and approach.

**To CheckThat:**
- None directly mentioned, though workflow/output quality issues could relate to prompt engineering and content generation consistency.

---

## Overview

- New managing editor job description created; role spans multiple skill areas
- Workflow improvements and knowledge sharing remain challenging; exploring solutions
- Client updates: York improving, Rapid and Galileo need attention, Webflow strategy in progress
- Need to improve ticket writing and knowledge transfer across the organization

---

## Key Topics

### Managing Editor Role Definition

  - Job description created for managing editor position
  - Role spans multiple skill areas defined by Marcel
  - Difficulty in finding candidates with all desired skills
  - Discussion on differences between existing MEs (e.g., Carrie production-oriented, Edesham project management-focused)

### Workflow and Output Quality Challenges

  - Inconsistent ability to manipulate workflows for desired outputs
  - Some MEs resorting to ChatGPT rewrites to meet quality standards
  - Need for better documentation and training on workflow inputs/outputs
  - Exploring solutions like FAQ chatbots, office hours, and incentive programs

### Client Updates and Strategy

  - York account showing improvement
  - Rapid and Galileo (Mara's clients) need attention in upcoming meeting
  - Webflow strategy setting in progress; Jakub to schedule follow-up call

### Knowledge Sharing and Training

  - Difficulty in effectively sharing knowledge across the team
  - Current documentation (Looms, Notion pages) not always consumed
  - One-on-one meetings and hands-on training more effective but less scalable
  - Exploring alternative formats (e.g., NotepicLM for audio consumption)

### Workflow Improvements and Hacks

  - Discussion on Ismail's success with Rapid and Brandt using custom style adapter
  - Concern about proliferation of individual hacks vs. systemic improvements
  - Need to balance sharing of learnings with proper engineering implementation

---

## Action Items

**Jakub Rudnik (GrowthX)**
- Schedule call with Jesse to dig deeper into Web Stacks strategy and requirements
- Ensure Linear tickets for publishers are up to date before next sprint
- Remind pod to fill out weekly publishing report

**Darrell Etherington (GrowthX)**
- Ensure Linear tickets for publishers are up to date before next sprint
- Remind pod to fill out weekly publishing report

---

## Transcript
**Andi Bailey:** I officially let her know that she's moving over because she was on in David's pod, but she was only covering one publisher.

**Darrell Etherington:** She was covering Airbite.

**Andi Bailey:** Yeah.

**Darrell Etherington:** As we chatted, I added her to the standup and then I'm going to have an intro call here next week and gave Carrie a heads up about her too.

**Andi Bailey:** Cool. Cause then you have another Sam. Um, and we need to figure out what we're doing with Saskia, but that's maybe not a conversation for today.

**Darrell Etherington:** Right.

**Andi Bailey:** Hi, Jakub.

**Jakub Rudnik:** What's up?

**Darrell Etherington:** Hello.

**Andi Bailey:** Do you have a long drive?

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** Two hours of meetings, then putting stuff away, and then we have to drive to Michigan. We're staying at my parents, doing all the calls tomorrow, going to open houses on Saturday. We had already planned this trip, but we're really under the gun to get it done this week so we could get out of town for both weekends.

**Andi Bailey:** Well, it's nice not to be there for the open house.

**Jakub Rudnik:** Yeah, it's nice. We just have to do those final touches.

**Darrell Etherington:** Did you stage, or did you just leave your stuff?

**Jakub Rudnik:** It's our stuff, but very much minimalized and a lot of it personalized.

**Darrell Etherington:** It looks pretty good. It's the emptiest and cleanest house I've been in in two years. I remember when we listed our last house, the realtor wanted us to move everything out and replace it all with their staging. We haven't done it yet because it was so arduous, but I'm tired of owning a 120-plus-year-old house. I'm actually buying a 100-year-old house instead, so I'll be on your side with the old houses.

**Andi Bailey:** It's got character. Well, when it gets cool again, maybe you'll forget you don't like it.

**Darrell Etherington:** Maybe. Okay, it's just us.

**Andi Bailey:** We don't have to take up much time, but I've prepared the managing editor role definition. We're hiring for a managing editor, so I'll show you the job description and we can discuss it. This also reflects what we've been talking about with Marcel. The clients we should focus on before Monday's call with Marcel are Rapid and Galileo—both Mara's—but York is improving really quickly.

**Andi Bailey:** Do you feel that way?

**Darrell Etherington:** Yeah, I do. That was a good one because no one had any reason to feel any kind of way about it. It was just running solo on an island, so we could be full and transparent.

**Andi Bailey:** So maybe we could do another learning session and talk about what you guys did and what made the difference. Are there any other accounts where you guys want input or want to have another discussion?

**Darrell Etherington:** No, I don't think so. On my end, everything is tentatively going all right at the moment.

**Andi Bailey:** Okay.

**Andi Bailey:** Jakub, do you want to talk about Web Stacks at all? It's a big account and we're setting strategy for them, so I didn't know if you wanted time to discuss on Monday.

**Jakub Rudnik:** I don't think so. I'm here Monday. I think we just need to get that call scheduled. I wanted to have another call with Jesse.

**Jakub Rudnik:** I feel like I understand most of what they want to do. He gave me the high-level overview, so we should dig in more. We've been doing ongoing syncs—he's probably the account I've been most in touch with and we've been very proactive on delivering extras and working towards an upsell. A lot will come out in that hour-long working session.

**Andi Bailey:** Cool. I might message Megan on Monday morning about that call and have her watch it. Okay, the managing editor role.

**Andi Bailey:** The difficulty here is that across the three roles Marcel defined, the managing editors fit into some buckets but not others—even directors like us fit into one bucket each. Marcel's take is that as long as you have one of each represented in a pod, you're okay, which makes it really difficult to define what the perfect person is. Darrell, maybe it would be useful to reiterate what you were talking to Marcel about—you have two good MEs but they're totally different.


**Darrell Etherington:** It's more about how they see their roles and what they tap me for—it's quite different between them.

**Darrell Etherington:** Carrie is very production-oriented. She's good at making sure things go out the door and is a good quality assurance layer. But she's much weaker on opportunity scoping and research. She has a strong appetite for strategy, but I don't think she has the development and training behind it. I end up having to course correct because I don't think she's always leading clients in the right direction or saying substantive things.

**Darrell Etherington:** Edesham is the consummate project manager. He's a really good planner and can articulate the plan top to bottom on how things should show up and go out. He's also a deep researcher and will back things up with stats and numbers. But he seems less high touch on the actual production and output quality.

**Andi Bailey:** Taste plays such a big part in it—being able to fix when a workflow doesn't put out the right thing or recognize when the tone is off is a huge skill set. But the input for that is so technical that doing one or the other doesn't necessarily get you all the way there, which is an interesting conundrum.

**Jason Gong:** For the ME, I would hope it's a person who knows what a good output looks like. But other than editing themselves, our workflows are built in a way where it's pretty unclear which input knob you have to turn to get it to look like what you want. It takes so long that people end up just taking their hands off the wheel and shipping something pretty bad.

**Darrell Etherington:** That's what's happening in both cases. Carrie has a deeper understanding because she's spent more time with the workflows and is able to adjust the knobs to get the required output. Edesham has a very good sense of what good quality looks like but isn't as good at manipulating the workflows. So he's doing it transparently—a lot of what we deliver to clients are ChatGPT rewrites of Atlas workflow outputs because I have to get them over the line in a scalable way. Part of it is he's not as familiar with which parts to tweak, but I've tried tweaking the workflow myself and haven't had much more success. The key is documenting what happens in the ChatGPT step so we can feed that back to engineering to fix these things systematically. Maybe it's just that he hasn't spent enough time with the flows—Carrie did a lot of hands-on production work, whereas Edesham is more of a project manager architect who directs CMs to do that work.

**Jason Gong:** For somebody with a project management background, is he doing certain things better than Carrie? Is he better at surfacing problems or writing clearer tickets?

**Darrell Etherington:** No, that's actually a shared blind spot. Communication back to engineering in a consumable, practical way that won't get lost in ticket mass is a universal problem. Neither of them is particularly good at it—and I'm not either, though I try.

**Matthew Panzarino:** I'm glad you brought that up.

**Jason Gong:** That deserves a couple of sessions. People don't know what's the artifact's fault, what's the CM's fault, and what's the workflow's fault. When that's unclear, bugging engineering is the last thing you try to do.

**Matthew Panzarino:** I find people conflating the inputs of one thing with the outputs of another. If you file a ticket that way, it'll get ignored. I'm trying to do validation through one-on-ones with CMs—asking what their exact problem is and helping them articulate it and write the ticket correctly. I'm not sure if that's scalable. But if problems are articulated better, we'd have more success fixing them.

**Jakub Rudnik:** Imagine a database: "If you have this problem, here are three or four potential sources." It would build over time. We'd need to surface what works to change so we can document it. But giving MEs, CMs, and MDs a guide like "when this happens, here are the potential spots" could help.

**Darrell Etherington:** It could be an internal-facing customer support flow that's rules-based, with a chatbot—basically an FAQ chatbot that guides people to solutions.

**Jason Gong:** The first step is figuring out if this is actually a finite list of things that can be articulated, not an endless list. If it's tone, it's probably the artifact. If it's internal linking, it's probably this step in the workflow.

**Darrell Etherington:** Fathom itself improved ticket quality by filtering out stuff that's totally not addressable before it even gets to triage.

**Jakub Rudnik:** A diagnostic guide could help with training—when you're learning big documentation, it saves tickets and shows you've done your due diligence and checked six boxes. If it's still not working, then it's ticket-worthy or something larger is going on.

**Matthew Panzarino:** I've created Looms and documents that walk people through all the inputs and outputs—what goes in at each step and what comes out. Maybe I'm bad at it or the documentation is bad, but something that says "here's what goes into this workflow, here's what comes out, so if you have a problem with these outputs, check these inputs"—I think that's one place to begin.

**Jakub Rudnik:** You could literally use AI to turn that into a one-pager: "Here's this problem, here's where Panzer suggested looking." We build on it over time. If I'm having a tone issue and I have a long Loom, I don't know if I'll actually jump in. But repurposing what you've already done and pulling in conversations from Slack and other places would make it much closer to the specific problem when you have it.

**Jason Gong:** Marcel mentioned something similar—"If only I'd read this three-page doc I wrote buried three layers in Notion, it would all be good." How do bigger companies solve this problem where knowledge sharing across a big team is hard? Is it a tool thing or a meeting thing?

**Andi Bailey:** Sadly, it's a meeting thing. People learn when something applies to what they need to do right then and they see how it affects them personally. If it's not that moment, we've missed the window. Maybe office hours would work—"Next time you're running a workflow, come share it and let's work through it together."

**Matthew Panzarino:** Here's what I've been doing—more focused learning. Since the Atlas transition, I started all-hands meetings every morning for CMs. We've moved that down to twice a week, then once a week. I'm wrapping up one-on-ones with every CM: "Bring me your troubles, bring me your fears, bring me your broken stuff." We fix it live or file a ticket. I have all those calls recorded and Nana's collating common themes so we'll have a database. I don't expect that to be digestible for CMs, but something more institutional could work—like, "Let's run your workflow together, let's hack on it." I learn new things every time—problems or weird solutions they've come up with that we should productize. It's great to get that ground-level feel, but something more institutionalized may be better.

**Andi Bailey:** I'm also thinking about incentivizing learning—best work for the month, best article of the week, something like that. We don't have to read all the content, but if you're proud of something, submit it and we'll give you something. I want there to be an incentive rather than fear, because everything we're doing right now is a little fear-based, which isn't healthy long-term. We want to show what good looks like. We should brainstorm something other than a cash prize.

**Jakub Rudnik:** I like that theme and the positivity. I'm interested in the workflow—how they've tested, how they're iterating within the workflows or artifacts. What comes out is important, but how they got there is interesting too. What problem did they solve? The client came with X and we hit a wall, so how'd they use what existed? I'd be interested in that creativity and process before the final output, but we'd need to know the problem and what they did to surface it.

**Matthew Panzarino:** Ismail is running Rapid and Brandt. He's getting it to a point where he spends five minutes per article at the end of the workflow, plus another 10 minutes at the brief. He's happy with the results and feedback from Ramp has declined a lot. He discovered Ramp had a laundry list of writing guidelines—don't use Oxford commas, specific style things—that weren't being applied by the writing guidelines step. He went to Kirkland, who added a style adapter after the article generation flow, basically like the old feedback step, that lets him put in a list of items to adapt and apply them. That's giving him really good results. He did that on his own, which is great.

**Matthew Panzarino:** This illustrates a couple of things. One is isolation of improvement—if you're quietly doing something and your clients benefit, other clients could too, but we're not exposing it. But the second thing is that it's a symptom, not a solution. I'm glad it works for him, but it's symptomatic of the fact that writing guidelines aren't being applied in the writing guidelines step where they should be. Maybe that step is getting exhausted or needs to happen elsewhere—that's a workflow improvement issue. The balance is: I want people sharing learnings, but we end up with hacks proliferating without getting systematized or built by engineers. And then everyone thinks their hack is the solution to all problems.

**Darrell Etherington:** That's where we get the most feedback—people sharing hacks they're excited about. There's an incentive because they figured out something unique and cool. But then it doesn't get productized. Ismail is an interesting example—he was doing Prophecy really well, then he passed it to Saskia saying "just do it this way," and she couldn't do it at all. She told me Ismail was doing it all outside the workflows. But looking at what he's generating for Ramp, the grid is full of output, so unless it's fake... I'm hearing from some MEs that people are doing all the work outside the tool and then putting it back in to make it look like they're using it. That's something to watch for because we're incentivizing use through punishment rather than incentive.

**Matthew Panzarino:** The way Ismail was talking about it, it didn't seem like that to me. And if Kirkland built that style adapter, it should address a lot of the problems people are hitting.

**Andi Bailey:** We didn't solve anything, but I want to keep developing—what are the things everybody has in common, and what are the things that are always going to be tricky? How do we start to close those gaps?

**Darrell Etherington:** The digestion problem is big—we have too much stuff and nobody's sure exactly how to digest it: Looms, Notion pages, guides, docs. At past organizations where education was successful, it wasn't self-service scalable. It was highly manual, one-on-one meetings and knowledge transfer. I don't know that's fixable. The NotepicLM hack is good—dump docs in it and use it as a podcast. CMs said, "I can't pay attention to a 20-minute video, but I can on a dog walk to a podcast." Maybe it's just making sure it's available in the format people will naturally use. AI makes it easier to distribute across any channel. Education is always a massive challenge.

**Andi Bailey:** We'll keep having this conversation and highlighting people doing good work and where people are struggling. Last thing: make sure your Linear tickets are in. We've got tickets filed, Webflow is up and running, Ramp is testing. Just keep putting in tickets for publishers. Sprint starts next week. Remind your pods to fill out the weekly publishing report and we'll do audits on those. I'm out tomorrow, but thank you guys.

**Andi Bailey:** All right, have a good weekend.

**Darrell Etherington:** You too.

**All:** Bye.
