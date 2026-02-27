# Production Team Weekly 

<metadata>
date: 2026-02-09
time: 15:59 UTC
duration: 34 minutes
organizer: Jenn Peters (jenn@growthxlabs.com)
primary_speaker: Matthew Panzarino (matthew@growthx.ai)
participants: Fatima, Simran Sethi, Aida Knezevic, Martha Martins, Ismail, Lawrence Neves, Victor, Ademilade Shodipe-dosunmu, Sucheta, Andi Bailey, Matthew Alves-Hill, Katya Luscomb, Marisol Smith, Hassan, Jessalynn, Liz Kushnereit, Oluwatimilehin Ademosu, Matthew Panzarino, Mariana Marins, Bailey Seybolt, Nathalie Schrans, Iana, Bisera, Ehtisham Hussain, Usman Adepoju, Megan Dickey, William Leborgne, Marcus Derencius, Felix Morgan, Nathan Navidzadeh, Gabrielle Brogan, Josip Sovar, Kyle Gaudreau, Carrie Chowske, Rachel, Saskia Wartnaby, Kirkland Gee, Usman Ghani, Ifeoluwa, Kalil, Sydney Go, Jenny Macrohon Dabon, Patricia, Will, Erik O'Brien, Kavishka Kanayake, Jo Kaminska, Leah Myers, Andrew, Pamela Weber, Igor, Sergey Kaplich
key_speakers: Matthew Panzarino (Lead), Sydney Go (New Team Lead - Sprint), Jenn Peters (New Team Lead - Production)
fathom_recording_id: 120810728
fathom_url: https://fathom.video/calls/559354799
share_url: https://fathom.video/share/CYfYSpExYZpVCd44gg8_zQxzcHorVXQF
source: fathom
enriched_on: 2026-02-27T00:00:00Z
</metadata>

---

## Summary

Matthew Panzarino conducted a production performance review, revealing that only 30% of clients meet quality, satisfaction, and time-to-delivery targets—the primary issue being high time-to-delivery (TTD) signaling cascading pipeline failures. Two new team leads, Jenn Peters and Sydney Go, were introduced to close the support gap between EMs and MEs, focusing on troubleshooting high-TTD accounts and fixing pipeline architecture rather than editing every piece. The team must proactively file tickets for accounts exceeding 2x average TTD, eliminate artifact conflicts, provide contextually complete instructions, and complete skills assessments to ensure better client assignments.

---

## Context

GrowthX's production layer faces a performance crisis rooted in pipeline inefficiency rather than individual editor capability. High TTD (currently averaging 1h 4m per deliverable across clients) creates a cascading failure: inefficient pipelines force marketing engineers (MEs) to spend disproportionate time on architectural work, leaving no capacity for performance-enhancing edits like SEO optimization and narrative refinement. This results in lower-quality content and reduced client satisfaction. The team has been categorized into three tiers: 30% "Good" (meeting all metrics), 30% "Striking Distance" (close on some), and 30% "Far Away" (significantly missing targets). Problem accounts include Relay, Diligent, Fieldguide, Rimkus, Cresta, and Navon.

To solve this, Jenn Peters and Sydney Go have been appointed as team leads with specific leverage-building mandates: troubleshoot high-TTD accounts, identify and fix root causes in pipeline architecture, and prevent downstream production issues. Their role is explicitly not to edit every piece of content but to eliminate structural obstacles. The root causes of high TTD have been identified as artifact conflicts (identified via the Convergence Report) and instructions lacking context—agents cannot execute based on external knowledge, so instructions must include concrete examples (e.g., "Write a CTA like this client-approved example"). Additionally, clients are inherently skeptical of AI-generated content and expect it to be bad; any error undermines confidence, making flawless execution the only way to build trust.

---

## Relevance

- **Operations & Delivery:** Production team members must file proactive tickets when TTD exceeds 2x average (>2 hours per deliverable); failure to raise hand results in escalation. Sydney Go now owns sprint pipeline quality before exit. Jenn Peters owns troubleshooting high-TTD production accounts.
- **Pipeline Architecture:** All new content type pipelines require unique, purpose-built artifacts; reusing standard artifacts for comparison, directory, or specialized content produces unusable output. The refresh pipeline is currently being rebuilt; improvements will benefit all downstream workflows.
- **Quality & Client Trust:** Clients are skeptical of AI content. Every error (even minor formatting like m-dashes) undermines confidence. Flawless execution is the differentiator. Artifact conflicts and context-poor instructions must be eliminated weekly using the Convergence Report.
- **ME Skill Development:** Complete the skills assessment form to enable better client-to-skill matching and more aligned work assignments.
- **Root Cause Diagnosis:** High TTD is a leading indicator of pipeline, process, or capacity issues—never an isolated editor problem. Interrelated factors (pipeline quality, input quality, process) must be diagnosed together.

---

## Overview

- **Performance Gap:** Only \~30% of clients meet the target of high-quality content, client satisfaction, and \<30 min/deliverable time-to-delivery (TTD).
- **TTD as a Red Flag:** High TTD (avg. is 1h 4m) signals a cascading failure: inefficient pipelines force MEs to do architectural work, leaving no time for performance-enhancing edits.
- **New Team Leads:** Jen and Sydney will provide direct ME support, focusing on troubleshooting high-TTD accounts and improving pipeline architecture.
- **Pipeline Hygiene is Critical:** The top causes of high TTD are artifact conflicts and instructions lacking context. Use the Convergence Report and provide concrete examples (e.g., a client-approved CTA) to fix this.

---

## Key Topics

### Production Performance "Vibe Check"

  - Performance is categorized into three tiers:
      - **30% "Good":** Meets all targets (quality, satisfaction, TTD).
      - **30% "Striking Distance":** Close on some metrics.
      - **30% "Far Away":** Significantly misses targets.
  - The goal is to move all clients into the "Good" bucket.

### The TTD Problem: A Cascading Failure

  - High TTD is the primary indicator of account issues, as it reveals a cascading failure:
    1.  **Inefficient Pipelines:** Force MEs to do architectural work.
    2.  **No Time for Quality:** Leaves no time for performance-enhancing edits (SEO, narrative).
    3.  **Client Dissatisfaction:** Results from lower-quality content.
  - **Average TTD:** 1 hour, 4 minutes.
      - This figure is skewed by outliers; removing the top 5 accounts drops the average significantly.
  - **High-TTD Accounts:** Relay, Diligent, Fieldguide, Rimkus, Cresta, Navon.
  - **Proactive Action Required:** MEs with TTD \>2x the average must file tickets (ENG, Editorial) immediately to get support.

### Solution: New Team Leads

  - Jen and Sydney are the new Team Leads, filling a support gap between EMs and MEs.
  - **Primary Role:** Troubleshoot high-TTD accounts to build ME leverage.
  - **Focus:** Fix pipeline architecture to prevent recurring issues, not edit every piece of content.
  - **Sydney's Sprint Team Task:** Ensure pipelines are performant and calibrated before they exit Sprint, which prevents production issues downstream.

### Client Perception & The Need for Flawless Quality

  - Clients are inherently skeptical of AI-generated content, often expecting it to be bad.
  - **Impact:** Any error, even minor style choices (e.g., m-dashes), can undermine client confidence.
  - **Action:** Treat every deliverable as if it will be scrutinized. Flawless execution is the only way to build trust.

### Pipeline Hygiene: The Root Cause of High TTD

  - The top two causes of high TTD are:
    1.  **Artifact Conflicts:** Use the Convergence Report to identify and resolve.
    2.  **Instructions Lacking Context:** The agent cannot execute commands based on external knowledge.
          - **Ineffective:** "Write something funner than last time."
          - **Effective:** "Write a CTA like this example, which the client approved."
  - **Pipeline-Specific Artifacts:** Use unique artifacts for different content types (e.g., comparison articles) to prevent "mumbo-jumbo" output.

### Admin: Skills Assessment

  - Complete the skills assessment form to inform client assignments and align work with your experience.

---

## Action Items

**Matthew Panzarino (GrowthX)**
- Email Sydney Go and Jenn Peters: establish priorities for troubleshooting high-TTD accounts; clarify scope of work to exclude editing every piece of content
- Email production team: circulate meeting agenda and skills assessment form link for completion

**All MEs (GrowthX Production)**
- Proactively file tickets (ENG, Editorial) if TTD exceeds 2x average (>1h 4m per deliverable)
- Use Convergence Report weekly to identify and resolve artifact conflicts
- Ensure all pipeline instructions are contextually complete with concrete client-approved examples
- Complete skills assessment form to inform client assignment alignment

**Sydney Go (GrowthX - Sprint Team Lead)**
- Ensure sprint team pipelines are performant and properly calibrated before content exits Sprint phase
- Begin troubleshooting high-TTD sprint-related accounts alongside standard pipeline work

**Jenn Peters (GrowthX - Production Team Lead)**
- Begin troubleshooting high-TTD production accounts; diagnose root causes (pipeline, process, or capacity)
- Dive-bomb accounts with quality flags to identify whether issues stem from pipeline, process, or individual capacity

---

## Transcript

**Matthew Panzarino:**

Thank Well, who knows what's going on with my camera? Not me. You're going to get the studio display camera today.

So I apologize for the low fidelity scenario. I have fallbacks. I was moving stuff around this weekend underneath my desk, and apparently I unplugged something vital to my camera.

This is what cable management will get you. You should just not cable manage. That's the takeaway.

Okay. Yes. Hi.

Good morning. Hello, everyone. Welcome to this wonderful February week.

It is gray and cloudy out here for me. I know it is probably for many of you as well. And if it's not, then I am suitably jealous.

That's awesome for you. I want to talk through a handful of things this week, for this week ahead. Some of it retroactive, some of it forward looking, and then we can open the floor a little bit and just have a little bit of a chat.

Overall, production wise, just want to give you, I'm going start doing a little bit of vibe checking. so everybody kind of knows how I feel about the production layer too. I know I haven't done a ton of that, because, you know, frankly, it's, it's still all over the You know, feel really good about some accounts and then, you know, sort of iffy about others.

And of course, that means that I probably have already spoken to you and that's cool. But I just want to give everybody kind of an overall assessment. So the way I look at it right now is we have about 30% of clients that are hitting our rough target of like good quality content.

It is actually performing, the client is happy, and we are close to our time to delivery metric, which is under 30 minutes per deliverable. So there are plenty of clients for where like one or more of those is true. Hopefully, in most cases, the clients are satisfied at the very least, and we're getting some performance out, which does happen.

That's closer to like 60 or 70% of clients, which is wonderful. Those that aren't are already aware and, you know, we're working on it. But in terms of like how good are we doing for all of our most important metrics, I just want you to all be aware.

Like it's about a... A third of the clients. And that's, I mean, obviously not ideal.

And there are numerous reasons for that that we have spoken about before and will continue to speak about. It's not doom and gloom because there's also like a good third that are probably within striking distance. But then there's also a third, that's three out of three, that are like far away, very far away for one reason or another.

And the far away parts can be and usually are related. In other words, if we don't have like a pretty solid time to delivery or within good striking distance, it is probably true that the pipelines are not in great shape or that they are not delivering something that the client expects. So, of course, like the ME has to do a lot more work to get them where they need to go.

And then if you cascade from there, it is very likely that the client is not getting the best quality content we can produce because the ME is spending a ton of time doing sort of like big architecture. They're not spending the time on the things that actually are going to make it performant, like, you know, SEO specifics, you know, clear narrative structure, and just making their own, you know, gut instinctual editorial changes to those things that they know tactically will support the strategy that we have proposed to the client, right? So, like, that's, it's a cascading series of effects.

The efficiencies don't, you can't, can't be absorbed at the human layer infinitely. There is just a finite amount of stuff that you can figure out, right? So, like, the mission going forward, obviously, is to get everybody in the good bucket, but in the very near term, there's going to be some hyper-focus on those of you that have long time to delivery, because that is, as I mentioned before, part of the picture.

and I don't, and the reason I'm... Laid it out for you is because I don't want it to seem like, oh, this person's taking a long time, we're going to pick on you. It's like, no, you have to understand, like, this is a part of, like, an interlocking series of things that occur.

And even if you personally are like, yeah, it takes me a long time, but I get it there, wonderful, that's great. But I guarantee you, you're probably missing things that you would catch otherwise. Because people don't have infinite amounts of attention, focus, you know, effort, ability, time, etc., right?

And I definitely don't want anybody, you know, editing stuff at 11.59 p.m. on Friday to try and get it out because they feel like they want to get out for clients. Because I guarantee you, you're not doing your best work at a metaphorical 11.59 p.m.

I know we're all in different time zones, but you know what I mean. Like, that's kind of the way it works. So, what are we doing about it?

Well, first of all, like, I can see the clients, right? So, like, I know how long it's taking. If you are erroring in your time tracking by, you know.

Tens or dozens of hours, then let me know, but otherwise, I could see that there are some clients that are taking a heck of a long time, you know, Relay, Diligent, Fieldguide, Rimkus, Cresta, Navon, you know, there's like a bunch of these ones that are just taking an enormous amount of time per piece of deliverable to edit, and I'm, once again, not picking on UMEs, so don't panic if you've heard a client that you're working on, because it is multi-factor, right? the number one thing, of course, when I go to, like, what am I going to do about it? first step is, have you filed a ticket?

Have you raised your voice? Is everybody aware of the scenario? Is your ME aware?

And then is, is the ENG team aware? Is AD aware? Am I aware?

Like, are there issues with it? I will, will pick on one client, Rimkus, which Matt has spoken to me about, and, you know, Lawrence and I have talked, and Lawrence and, you know, Nana have talked, etc. Like, we know Rimkus is sort of, like, an issue.

It's kind of hard enough to crack. Because that's like a legal review thing. And also that's related to the pipeline.

It's like, hey, they have a lot of hyper-specific desires and needs and wants. So like we are aware of that scenario. Like we're aware of that situation that needs to happen to like make them happy.

And the cascading series of things that go from there are like, okay, now how do we engage those resources? How do we get them on the same page as us? All of that stuff, right?

So in that case, like we are aware of like what's going on. If you are looking at your time to delivery and it is like, wow, man, I'm hovering at like, you know, one and a half to two hours, two and a half hours per piece of deliverable. And you have not proactively spoken up, raised your hand, rattled the cans, like asked for eng help, asked for editorial layer help, et cetera.

You need to do so ASAP. Because otherwise I'll be coming to you. And then...

