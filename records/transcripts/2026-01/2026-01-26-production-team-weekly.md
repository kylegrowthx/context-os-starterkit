# Production Team Weekly

<metadata>
date: 2026-01-26
time: 16:00 UTC
duration: 24 minutes
enriched_on: 2026-02-28 12:00 UTC
organizer: Jenn Peters (jenn@growthxlabs.com) — GrowthX
participants_structured:
  - name: Matthew Panzarino
    email: matthew@growthx.ai
    affiliation: GrowthX — EPD Lead
    role: Session facilitator
  - name: Kirkland Gee
    email: kirkland@growthx.ai
    affiliation: GrowthX — EPD Engineering
    role: Internal linking & infrastructure
  - name: Sergey Kaplich
    email: sergey@growthx.ai
    affiliation: GrowthX — EPD Support
    role: Primary EPD support lead
  - name: Marcus Derencius
    email: marcus@growthx.ai
    affiliation: GrowthX — EPD Engineering
    role: Claude/API stability
  - name: Hassan Rashid
    email: hassan@growthx.ai
    affiliation: GrowthX
    role: Participant
  - name: Patrícia Contreiras
    email: patricia@growthx.ai
    affiliation: GrowthX
    role: Raised Claude.ai issues
  - name: Felix Morgan
    email: felix@growthx.ai
    affiliation: GrowthX
    role: Participant
  - name: Nathan Navidzadeh
    email: nathan@growthx.ai
    affiliation: GrowthX
    role: Participant
  - name: Kalil Magtoto
    email: kalil@growthx.ai
    affiliation: GrowthX
    role: Participant
  - name: Jenn Peters
    email: jenn@growthxlabs.com
    affiliation: GrowthX Labs — Organizer
    role: Recording organizer
  - name: Kyle Gaudreau
    email: kyle@growthxlabs.com
    affiliation: GrowthX Labs
    role: Participant
  - Additional 43 participants
fathom_recording_id: 117070698
fathom_url: https://fathom.video/calls/543227371
share_url: https://fathom.video/share/vbLbnhUsycUNCTWqU4D1ohzzN5q-DmLC
source: fathom
</metadata>

---

## Summary

Matthew Panzarino reviewed production workflows, quality standards, and EPD support structure. The team discussed Time Doctor tracking data revealing workflow bottlenecks, internal linking bug fixes, and the newly appointed primary EPD support lead, Sergey Kaplich. Claude.ai chat interface instability was addressed with recommendations for fallback tools and outage tracking.

---

## Context

This is the Production Team Weekly standup held on January 26, 2026, during winter weather disruptions in the Northeast US and Texas. The EPD (Enterprise Production Delivery) team operates Atlas, a content production pipeline. Matthew Panzarino leads the group's agenda. The session introduced Sergey Kaplich as the primary triage point for Linear support tickets, consolidating a previously distributed support model across the engineering team. Technical updates focused on internal linking reliability improvements and API-level stability of Claude models, distinguishing between Claude.ai chat interface outages and backend API performance.

---

## Relevance

**Operational & Process:**
- Time Doctor data is the foundation for proactive team support and workflow optimization
- Linear tickets are the single source of truth for all EPD issues and requests
- Atlas Learnings Slack channel is for peer review; production support flows through Linear
- Sergey Kaplich is the first point of contact for EPD support triaging

**Technical Infrastructure:**
- Internal linking now supports multiple target paths (comma-separated) for more flexible domain/section targeting
- Post-implementation 404 verification prevents LLM-induced link breakage
- Claude API remains stable; Claude.ai chat interface is the source of instability
- Google Gemini offers a viable fallback for post-processing tasks when Claude.ai is unavailable

**Quality Standards:**
- Production team maintains final quality gate before client delivery (read articles, verify links)
- Systemic issues in Atlas should be filed as detailed Linear tickets, not accepted as permanent workflow constraints
- Compressing errors in Claude.ai often stem from oversized context; breaking work into manageable chunks is recommended

---

---

## Overview

- **Time Doctor data shows clear workflow bottlenecks,** with task times varying from 10–20 minutes to several hours. The EPD team is using this data to proactively offer support.
- **Sergey Kaplich is now the primary EPD support lead,** triaging all Linear tickets to streamline the process.
- **Critical internal linking bugs are fixed,** including a SERP API issue and a new post-implementation 404 check. The `internal_link_target_site` input now supports multiple paths.
- **Claude.ai chat is unstable,** but the API is stable. A new Slack channel, `#is-claude-down`, will track outages, and Google's Gemini is a viable fallback for post-processing.

---

## Key Topics

### Time Doctor Insights

  - Initial data shows clear workflow bottlenecks, with task times varying from 10–20 minutes to several hours.
  - The EPD team is using this data to proactively offer support where needed.
  - **Action:** Continue diligent time tracking. Contact Nana or Matthew for support.

### Quality Standards & Systemic Issues

  - **Directive:** Maintain quality standards (e.g., read articles, verify links) to act as the final quality gate before client delivery.
  - **Action:** File detailed Linear tickets for any systemic issues in Atlas.
      - **Rationale:** This provides the EPD team with the specific data needed to diagnose and fix problems, preventing the team from having to "live with" broken workflows.

### Internal Linking Updates

  - Kirkland detailed three key fixes to improve internal linking accuracy:
    1.  **SERP API Bug Fix:** Resolved an issue (Jan 12–last week) that prevented the API from fetching page data for linking.
    2.  **Post-Implementation 404 Check:** Added a check to ping all URLs *after* the LLM implements them.
          - **Rationale:** Fixes an issue where the LLM would sometimes change valid URLs, causing 404s.
    3.  **Multiple Path Support:** The `internal_link_target_site` input now accepts comma-separated paths (e.g., `domain.com/blogs,domain.com/docs`).
          - **Rationale:** Fixes an issue where the system would guess links if multiple paths were provided.

### EPD Support & Ticket Triage

  - Sergey Kaplich is now the primary EPD support lead, triaging all Linear tickets.
  - **Rationale:** This streamlines support by providing a single point of contact and better managing the EPD team's workload.
  - **Process:**
      - File all issues in Linear; it is the source of truth for tracking and resolution.
      - Use the `#atlas-learnings` Slack channel for peer review and discussion.

### Claude.ai Instability & Workarounds

  - **Problem:** The Claude.ai chat interface is experiencing frequent errors.
  - **Diagnosis:** The issue is with the chat interface, not the Claude API, which remains stable.
      - **Note:** The "compressing" error often occurs when feeding the model excessively large contexts.
  - **Workarounds:**
      - **Outage Tracking:** A new Slack channel, `#is-claude-down`, will track service outages.
      - **Fallback Interface:** Use Google's Gemini to call Claude models (e.g., Opus).
          - **Rationale:** This provides a stable alternative for post-processing tasks.
      - **Custom Interface (Advanced):** Build a personal interface to call any model, including local ones.

---

## Action Items

**Sergey Kaplich — GrowthX EPD Support**
- Join #atlas-learnings Slack channel for peer review and coordination

**Kirkland Gee — GrowthX EPD Engineering**
- Investigate Anthropic repository issues; fix if possible
- Create Slack channel #is-claude-down and route Claude service alerts to it

---

## Transcript

**Hassan Rashid:** Thank Kirkland, and anyone else on the East Coast, how did the storm treat you guys?

**Sergey Kaplich:** It's pretty bad. Everything is closed. The store was closed, and my daughter didn't go to daycare today. A lot of snow.

**Kalil Magtoto:** This is my first time shoveling. That was an experience.

**Kirkland Gee:** I'm down in Virginia. It's bad, but not as bad as some places. We had about five or six inches, but that still shuts down our entire city. The weather yesterday was almost like silica gel—just tiny little balls of ice.

**Nathan Navidzadeh:** I was lucky. Our daycare is open if you can make it. We have fluffy snow this time because it's so cold it's not heavy, wet snow.

**Felix Morgan:** In Austin, we got about two or three inches. It's just solid ice. Schools are shut down.

**Matthew Panzarino:** Sorry for being late. Winter connections are rough out here.

**Matthew Panzarino:** Let me check in on Time Doctor. We're seeing good tracking from everybody, so please be diligent about that this week. We're getting raw data that's interesting. We have clear patterns showing bottlenecks. Task times vary from 10 to 15 minutes on the bright side to hours and hours on the dark side. We're using this to proactively help those who need support. If you have any time tracking issues or need technical support, contact Nana or myself.

**Matthew Panzarino:** Regarding quality standards, remember to read articles before delivery and verify links. The EPD team found some linking issues in one of our workflows, and we're deploying fixes. Don't assume that manual labor like link checking is just your responsibility. You're the final quality gate, but if you find systemic issues in Atlas, file a detailed Linear ticket. That's how we improve.

**Matthew Panzarino:** Atlas may have issues, or you may be using it incorrectly, or the workflow needs tweaking. In any case, you don't have to live with problems. You can get training, update your process, or we can improve Atlas itself. The only way we know is through detailed tickets.

**Kirkland Gee:** I have an update on internal links. We found a bug in the SERP API that ran from January 12th until last week. When the system tried to fetch page data for linking, sometimes it wouldn't get any data because of a bug introduced from a previous fix. That's fixed now.

**Kirkland Gee:** Second, we added a post-implementation 404 check. The system now pings all URLs after the LLM implements them. Previously, it would verify the URL before giving it to the LLM, but the LLM would sometimes change the URL for no reason. Now we check again after implementation.

**Kirkland Gee:** Third, the internal_link_target_site input now supports multiple paths. It used to only allow one domain. If you put in augmentcode.com and augmentcode.com/guides as comma-separated strings, it now respects multiple paths instead of guessing. This is theory tested on a handful of cases, so if it doesn't work as intended, let us know.

**Matthew Panzarino:** Great. Thank you.

**Matthew Panzarino:** Now I'm introducing our new EPD support lead, Sergey. Sergey, introduce yourself.

**Sergey Kaplich:** I've worked at GrowthX for almost two months. I'm an engineer with almost four years of experience. Before that, I had a seven-year career in content marketing, from copywriter to head of content. I understand what you all struggle with, and I'm happy to help. Everything organizational stays the same—create Linear tickets, and I, Kirkland, or Marcus handle them. I'll be the primary person triaging them.

**Kirkland Gee:** Do you have anything to add?

**Kirkland Gee:** Yeah. There are four or five of us, depending on who's on projects. It's challenging to handle all the work and triage linear tickets. Sergey has onboarded really well and has already helped many of you. He's going to step up as the primary triage lead with me. If you file a ticket, Sergey will be the first to respond. If he doesn't have capacity, he'll pass it off. In the future, we'll have more people, but bear with us for now.

**Matthew Panzarino:** There's only a few of us, but we're trying our best. Sergey, you should join the #atlas-learnings Slack channel for peer review. That's separate from client support and Linear tickets. Linear is the source of truth. Don't assume EPD team members are reading Slack peer review. File detailed tickets so we have the information we need to action them. That's it for me this morning. Continue being the quality gate between good and bad work going to the client. I'm happy to hear about blockers or patterns you're seeing.

**Matthew Panzarino:** Anyone got something happening?

**Patrícia Contreiras:** We've been having tons of problems with Claude recently. We raised it in the tools channel, but still having tons of trouble post-processing everything outside of Atlas.

**Matthew Panzarino:** It's good to call out. Unfortunately, these problems are unrelated to us. It's the problem of working with dependencies. We get hit by the issues that dependencies have. However, there's a channel dedicated to Claude outages and service issues. Having visibility there helps you sanity check whether it's a service issue or a personal problem. If it's a service issue, move on to other work until it stabilizes.

**Kirkland Gee:** Marcus, do you remember what that channel is called?

**Marcus Derencius:** We have a bot that sends Claude alerts in the alerts channel, but maybe we should move these to #atlas-learnings so people see them.

**Matthew Panzarino:** Those affordances probably need to be in the UI of Atlas. For now, the near-term fix is a Slack channel where people can see service outages or degradations.

**Kirkland Gee:** I'm just going to make a new channel called #is-claude-down and link the alerts to that.

**Matthew Panzarino:** Perfect. Marcus mentioned using Google Gemini as a fallback that also serves Anthropic models. Let me clarify for those who don't understand. When Claude.ai has issues, that's different from Claude API issues. If the API has problems, Atlas is affected. If Claude.ai chat is down, you can use alternatives. Many pipelines use Opus. If you're in a bind post-processing, you could use Gemini with Opus. The downside is your projects aren't set up there. For production, use your standard Claude projects. Other providers also serve Anthropic models. Technically, you could build a custom interface that calls any model, including local ones. But for production work, use Claude projects. If you hit a wall, reach out in #atlas-learnings.

**Marcus Derencius:** The Claude API and Claude Code have been stable. It's just Claude.ai that's been failing.

**Matthew Panzarino:** I'm not sure what's going on.

**Patrícia Contreiras:** We try to start conversations, and it gives a compressing error or something, and we can't continue.

**Matthew Panzarino:** The compressor has limits. If it's regularly compressing, you're probably feeding it enormous context. Better to work in manageable chunks per conversation. You could also experiment with Claude Code or Cursor—they tend to work pretty well. Try breaking work into smaller chunks or use an alternate interface if needed.

**Patrícia Contreiras:** Thank you.

**Matthew Panzarino:** Any other questions, comments, or issues? That's all I have for this morning. Continue being the quality gate. Let's go do work. By next Monday, I'll have more to talk about. Thanks, folks.
