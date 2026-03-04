# Impromptu Google Meet Meeting

<metadata>
date: 2025-11-27
time: 15:51 UTC
duration: 17 minutes
organizer: matthew.alves-hill@growthx.ai
participants: Matthew Alves-Hill, Israel Beni
fathom_recording_id: 104823987
fathom_url: https://fathom.video/calls/489396342
share_url: https://fathom.video/share/3kvyn2Db-mkouKLahd6mo15wZzzKFVBr
source: fathom
enriched_on: 2026-03-02 09:32 UTC
</metadata>

---

## Summary

Matthew and Israel debugged a critical blocker preventing the Batch 1 redirect feature from working on InnoWorld's preview server — it functions correctly locally but fails when deployed. Israel cannot access server logs due to company deployment policies, so Matthew agreed to create a private Slack channel connecting Israel directly to Ilya (the backend engineer) to accelerate debugging without Matthew as an intermediary. The team is prioritizing this feature above all other technical work, including other misconfigured static redirects, to meet InnoWorld's key performance indicators.

---

## Context

This is an internal GrowthX call between Matthew Alves-Hill (GrowthX) and Israel Beni, an external development partner working on the InnoWorld website project. Israel has been tasked with implementing a Batch 1 redirect feature managed through Prismic (a headless CMS), which is critical to InnoWorld's current deliverables. The feature works correctly on Israel's local development server but fails mysteriously on the preview/staging server. Because InnoWorld has a company policy restricting deployment access to external partners for security reasons, Israel cannot directly access server logs to debug the issue. This has created a communication bottleneck where all technical details must flow through Matthew as an intermediary, slowing down the debugging process.

---

## Relevance

**To GrowthX Delivery:**
- Critical blocker on InnoWorld's top KPI: completing the Batch 1 redirect feature today or tomorrow
- Deployment access policies at client sites require process redesign (direct Slack channel) to unblock external partners
- Static redirect infrastructure on the site is misconfigured (e.g., /consult changed from 301 to 302), creating cache issues for end users — deferred pending Batch 1 completion

**To Account Health (InnoWorld):**
- Feature delivery is tracking to the promised deadline but with dependency on InnoWorld's backend engineer (Ilya) availability
- Matthew positioned other technical issues as out-of-scope until Batch 1 is complete, managing expectations effectively

---

## Overview

- **Blocker:** The Batch 1 redirect works on the local dev server but fails on the preview server.
- **Root Cause:** A company policy prevents direct deployment access, blocking Israel from debugging server logs.
- **Solution:** Matthew will create a direct Slack channel for Israel and Ilya to accelerate communication and unblock the task.
- **Priority:** Completing the Batch 1 redirect is the top KPI for InnoWorld; all other issues are deferred.

---

## Key Topics

### Batch 1 Redirect Blocker

  - **Goal:** Implement a redirect feature for "Batch 1" paths, managed via Prismic.
  - **Status:** The feature functions correctly on the local development server.
  - **Problem:** The redirect fails on the preview server, but the cause is unknown.
  - **Root Cause:** A company policy prevents direct deployment access for external partners.
  - **Impact:** This policy blocks Israel from accessing server logs, preventing debugging.
  - **Initial Proposal (Rejected):** A live screenshare with Ilya to debug the server together.
  - **Rationale for Rejection:** Matthew confirmed Ilya is already briefed on the high priority of this task.

### Solution: Direct Slack Channel

  - **Decision:** Matthew will create a private Slack channel for Israel and Ilya.
  - **Rationale:** This provides a direct communication path, bypassing Matthew as an intermediary and accelerating the debugging process.
  - **Scope:** The channel will be dedicated exclusively to completing the Batch 1 redirect.

### Other Redirect Issues (Deferred)

  - **Finding:** Israel discovered other static redirects are misconfigured.
  - **Example:** The `/consult` path was changed from a permanent (301) to a temporary (302) redirect.
  - **Impact:** Users who visited the old path before the change are still cached on the old destination (Calendly) and will not see the new one (HubSpot).
  - **Decision:** These issues are out of scope for now. The team must focus on the Batch 1 redirect to meet the primary KPI for InnoWorld.

---

## Action Items

**Matthew Alves-Hill (GrowthX)**
- Create private Slack channel with Israel Beni and Ilya; post intro message; request Israel's live-server debugging instructions

---

## Transcript

**Israel Beni:** Okay, so can I present my screen? Can you see my screen?

**Israel Beni:** All right, so real quick, I'm going to share about the Batch 1 redirect. Secondly, I'm going to give you a quick presentation of the feature from dev and how it's working.

**Israel Beni:** I'm currently running the development server. So for the purpose of this call, I've added this one here. When you go in Prismic, you have the redirect. This is where we're going to be adding any new batch in the future.

**Israel Beni:** Coming back to this batch, currently if I take this example here and copy this path, when I hit that, it's loading. Yeah, you can see there's redirecting back here. Perfect.

**Matthew Alves-Hill:** Yeah.

**Israel Beni:** Now, this works on my local server. As I said in the report that I shared, there is a difference in what I'm currently getting and what I'm seeing in the preview server. I couldn't see the log to get a hint at what exactly might be causing this discrepancy. Since they're not favorable to sharing the deployment — which is understandable, because anybody with deployment access could have security vulnerabilities. I understand that decision. I've led many projects and understand why they might take this decision.

**Matthew Alves-Hill:** Me too. It was a long shot. I didn't think they would give us access. I appreciate you saying that because we do need to move quickly, but I think this is as fast as we can move, unfortunately. I trust you, but I understand why the company doesn't want people with those kind of privileges.

**Israel Beni:** Yeah, I'm okay with that. So I'm proposing an alternative. We could have a live session so I can go over the server with you and see what's going on. I think that's the fastest way to go right now. Otherwise we revert back to what we were doing the past few days — I send a change, I wait for him when he's free, he answers and deploys.

**Matthew Alves-Hill:** Yeah, it's not ideal. We have company policy that there's only one mode of communication through external channels, and that's through me. So I know it's not ideal. But I think the approach we're doing is okay. If that's the fastest we can move, then that's the fastest we can move. If the company aren't going to give us deployment capabilities and we're reliant on Ilya being online, then that's as fast as we can go.

**Matthew Alves-Hill:** I saw in your message that you need more of his help today. What would be great is if you give me instructions for what you need from him, I will pass those messages along into the external channel. I think that's going to be the fastest way we can move.

**Israel Beni:** Okay. So let's just confirm — he's available, you are available, and I am available, so we can communicate faster this way. I know it's not ideal, but he is online right now and will be for a while. But he might be working on other stuff.

**Matthew Alves-Hill:** But it is an absolute priority for him as well. We've been very clear that we need to get this done. So he's on it.

**Israel Beni:** Okay.

**Israel Beni:** So I'm currently available.

**Israel Beni:** I have a meeting, another meeting two hours from now, so I'm currently here.

**Matthew Alves-Hill:** Okay, so if you can compose, like, can I just forward that message that you sent me?

**Matthew Alves-Hill:** Do you think I can just forward that through to Ilya?

**Matthew Alves-Hill:** Yeah, or would you want to write a new message to just explain, like, what we need to do?

**Matthew Alves-Hill:** What do you...

**Matthew Alves-Hill:** Basically, like, if you write messages like what you need from him, I will pass those on and make sure it's helping.

**Israel Beni:** Okay.

**Israel Beni:** I will send you a new message specifically for when he's live, so we can go over this together.

**Matthew Alves-Hill:** Cool.

**Israel Beni:** The other thing I mentioned is that I've seen there have been a couple of redirects that were done by their team. I need to go through the code history to see exactly who did that. But I've noted some of them here.

**Israel Beni:** There has been some redirect configuration that was set up on the website statically. An example would be the `/consult` path. When you hit that path now, it directs to a HubSpot page. But before it was directed to a Calendly page.

**Matthew Alves-Hill:** I'm wondering, one thing I could do is create a channel between you, me, and Ilya. Maybe that would help — we could have our own Slack channel.

**Israel Beni:** I don't know if it's worth the company policy, but let's see.

**Matthew Alves-Hill:** Okay, let me just ask about that.

**Israel Beni:** So I was saying that when you hit the `/consult` path, it used to direct to the Calendly page, but now it directs to the HubSpot page. Now, it was set as a permanent (301) redirect. But the way it was changed, it was changed as if it was a temporary (302) redirect. In my browser it works because I didn't hit this endpoint before the change occurred. But anybody who hit this endpoint before the redirect changed will still be cached on the old Calendly destination and won't see the new HubSpot page.

**Matthew Alves-Hill:** I see. Yeah, I think the website is a mess in general. There are lots of issues. But for us, we need to show progress in certain areas. We're being judged on solving the blogs and solving the batches. That's what InnoWorld asked of us. Other things outside that scope are helpful, but right now I want to focus on getting Batch 1 done — hopefully today, if not by tomorrow. That's our main KPI for InnoWorld. That's what they want to see from us. That's what we promised. So that's the key priority. I think other stuff is helpful and maybe this project will expand, but right now we need to show InnoWorld that we've figured this out. I know it's tough because we're relying on them helping, which makes things go slowly. I think we're moving as fast as we can. Let's get Batch 1 complete this week, and then we can talk about other issues next week.

**Israel Beni:** Okay. Do you have any questions for me?

**Matthew Alves-Hill:** No. I've been told I can create a private chat with you and Ilya. So that should hopefully make things go more quickly. I'll add you to that chat just now. It means you don't have to explain things to me so that I have to explain things to Ilya.

**Israel Beni:** Yeah. Okay, cool.

**Matthew Alves-Hill:** I really appreciate your help. This is super helpful work. Let me set up that channel and then I'll introduce you guys and we can get to work. Let's just keep this channel dedicated to this task at hand because he has been briefed that this is a top priority.

**Israel Beni:** Okay. So just as a wrap-up, regarding the other redirects that have similar issues — you can relate that to him later on after we have this done.

**Matthew Alves-Hill:** Yeah. Cool. Thanks, Israel.

**Israel Beni:** Thanks. Bye.
