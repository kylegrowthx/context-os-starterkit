# CheckThat Weekly Check In

<metadata>
date: 2026-01-20
time: 22:30 UTC
duration: 14 minutes 14 seconds
organizer: Stevie Kim (GrowthX)
participants:
  - name: Stevie Kim
    email: stevie@growthx.ai
    affiliation: GrowthX
    role: Product Manager / Lead
  - name: Jose Farias
    email: jose@growthx.ai
    affiliation: GrowthX
    role: Engineer
  - name: Leonardo Carpenedo Steffen
    email: leonardo@growthx.ai
    affiliation: GrowthX
    role: Engineer
  - name: Jason Gong
    email: jason@growthx.ai
    affiliation: GrowthX
    role: Engineer
  - name: Pedro Steimbruch
    email: pedro@growthx.ai
    affiliation: GrowthX
    role: Engineer
  - name: Estevão Mascarenhas
    email: estevao@growthx.ai
    affiliation: GrowthX
    role: Engineer
  - name: Jacopo
    email: jacopo@growthx.ai
    affiliation: GrowthX
    role: Engineer
  - name: Marcel Santilli
    email: marcel@growthxlabs.com
    affiliation: GrowthX Labs
    role: CEO
  - name: Daniel Lopes
    email: daniel@growthxlabs.com
    affiliation: GrowthX Labs
    role: (Not present)
fathom_recording_id: 115798373
fathom_url: https://fathom.video/calls/536979075
share_url: https://fathom.video/share/MsTEsVu4zkDmNx27DyeFikj55UGNCWN9
source: fathom
enriched_on: 2026-02-28 00:00 UTC
</metadata>

---

## Summary

The team aligned on launch readiness, particularly around admin access controls, data consistency workflows, and outstanding product decisions. Stevie confirmed the decision to keep EMs as non-admins while she and Carrie buffer workspace setup; Jose introduced the "backfill last 14 days" recovery for recategorization; and the group identified that user invitation and roles/permissions features remain incomplete and require clarification with Marcel before implementation.

---

## Context

CheckThat is approaching launch with an internal team working on product, payments, workspace management, and customer enablement. This weekly sync brings together the core engineering and product team to surface blockers, validate assumptions, and align on what must ship to launch. The team had covered significant ground earlier that morning, so this call focused on specific pain points: (1) whether to grant demo/onboarding partners (external engineers managing customer accounts) admin privileges in their workspaces, (2) a data consistency issue discovered during recategorization workflows, and (3) clarifying the scope of the "invite users to workspace" feature in relation to roles/billing/subscription logic that hasn't been fully defined with leadership.

---

## Relevance

**Product Management & Design**
- Workspace admin access policy and onboarding risk (EMs as non-admins vs full access)
- Post-signup user experience and permissions model (who can create/invite/edit within a workspace)
- Subscription-to-workspace linkage and multi-workspace support decisions

**Engineering & Development**
- Data backfill workflow for recategorization (now discoverable via "Backfill last 14 days" action)
- Roles and permissions system scope (estimated "couple days" if added before launch)
- User invitation ticket acceptance criteria and product assumptions

**Launch Readiness & Operations**
- PR review bandwidth and ticket clarification bottleneck (Stevie as blocker mitigation)
- Stripe account setup status and payment flow readiness
- Missing launch features: acceptance criteria, edge cases, scope clarity before hand-off to Marcel

---

## Overview

- **Admin access decision**: Keep EMs (external engineers helping customer accounts) as non-admins for now. Stevie and Carrie will buffer workspace setup/fixes to avoid public page corruption.
- **Recategorization fix**: Use "Backfill last 14 days" in the Workspace page after recats to repopulate charts (no charts auto-update on recat currently).
- **Roles/permissions**: Do not exist yet. Current model is GrowthX admins vs everyone else. Inviting users today grants full workspace access; adding roles ≈ couple days of work.
- **Product unknowns**: Subscription ↔ workspace 1:1? Multi-workspace capability? Who can invite? Must clarify with Marcel before finalizing "invite users" scope.

---

## Key Topics

### EM admin access and workspace stabilization

- EMs (sprint team) have been added to customer workspaces as non-admins; Stevie and Carrie handle manual fixes (subcategory corrections, UX polish) so the team can demo safely.
- Admins can break public pages; onboarding coverage is insufficient to grant all EMs admin access yet.
- Intent is to avoid "panic grant" of admin if workload spikes; Stevie to draft an access policy and consult Jason.

### Recategorization data consistency

- Issue: Recategorization via admin console does not auto-backfill historical charts.
- Resolution: Use Workspace page action "Backfill last 14 days" → wait ~1 min → metrics repopulate.
- Action: Stevie to run backfill on affected workspace(s) post-call.

### Launch readiness: PR reviews and acceptance criteria

- Team to review open PRs within 24–48h and comment/approve or request changes.
- Team to surface missing launch items or unclear acceptance criteria proactively; if short on time, DM Stevie to ticketize.
- Stevie to enrich tickets with user stories and acceptance criteria where helpful; acknowledge that pre-launch phase will see late changes, so don't over-invest in rigid AC.
- Process goal: Reduce reliance on Marcel's last-minute clarifications by writing intent upfront; Stevie to iterate pragmatically with Leo.

### Invitations, roles/permissions, and billing/workspace model

- **Current system**: Only two hierarchy levels → GrowthX admins (Marcel, Jason, Stevie, core team) vs everyone else; no roles within customer workspaces.
- **"Invite users to workspace" ticket implications**:
  - Straight path now: Invited users = full workspace access (no roles).
  - Roles/permissions (owner/admin/member, etc.) require designing a small system → "couple days" build + product decisions.
- **Open product questions with Marcel** (block scope):
  - Subscription linkage: 1 subscription = 1 workspace? Confirmed or changed?
  - Multi-workspace capability: Can a customer create additional workspaces/brands under a subscription?
  - Invitation authority: Who can invite? Any member vs owner/admin? Cross-workspace visibility rules?
  - Futureproofing: Minimal role set for launch (e.g., Owner vs Member) vs defer roles entirely?

### Payments/onboarding status

- Stripe account setup in progress (Stevie); some details pending; aim to avoid blocking launch-related billing flows.
- Onboarding flow: Customers submit domain → system creates workspace; need clarity on post-creation controls tied to billing and roles.

---

## Action Items

**Stevie Kim (GrowthX)**
- Backfill last 14 days of data for recategorized workspace(s) using the Workspace page button
- Clarify with Marcel: subscription ↔ workspace model, multi-workspace policy, invitation authority, minimal roles needed for launch
- Draft an initial access policy for EMs/admins; review with Jason
- Continue Stripe configuration; flag any blockers
- Add user stories and acceptance criteria detail to ambiguous launch tickets where it reduces confusion

**All Engineers (GrowthX)**
- Review open PRs within 24–48h; comment/approve or request changes
- Proactively list missing launch items or unclear acceptance criteria; if short on time, DM Stevie to ticketize

**Jose Farias (GrowthX)**
- None assigned; provided backfill guidance and roles implementation estimate; available for scope input once product decisions land

**Carrie (GrowthX)**
- Continue workspace content/UX fixes for EM demos; coordinate with Stevie on priority workspaces

---

## Transcript

**Jose Farias:** Hey, sorry, I'm here.

**Jose Farias:** This is funny. I was late joining the meeting because I felt guilty joining a call without having Claude do work in the background. This is so new.

**Stevie Kim:** Cool. So I know Marcel and I don't think Daniel can make it. And since we went over quite a bit this morning, I think we can probably go through things pretty quickly.

**Stevie Kim:** So if you didn't put your status update, I'll just throw any missing information on there.

**Stevie Kim:** Yeah, I'm just getting this Stripe account set up, and so still there's some details I need to add there. So, again, if anything's missing or if you need any information from me on that, let me know. I don't want to be the blocker there. I think the basics, at least, are set up.

**Stevie Kim:** Yeah, so the EMs are on the sprint team. They've been added to their customers' workspaces as non-admins, so we're getting some tickets from them that we're working on. But I've been trying to be the buffer there so you guys aren't seeing a lot of information coming from them. They have raised a lot of UX things, and so has Jason, so I need to go through some of those.

**Stevie Kim:** There's a lot of manual work that I'm trying to take care of for their particular workspaces, like fixing if something's in the wrong subcategory. The reason I bring that up is because most of them we haven't given admin access to, because admins can mess up the public pages. Jason and I have done some onboarding, but I don't think it's enough to give all these EMs admin access. I could be wrong, so I just wanted to get a sanity check. What do you all think about that?

**Stevie Kim:** Right now Carrie is helping me with some stuff and I'm doing work around getting those workspaces to where they can actually demo and show to customers comfortably. But yeah, what are your thoughts about who we're giving admin access to?

**Jose Farias:** I think ultimately it depends on who we're comfortable changing the public pages. In terms of recategorization, I don't think we're backfilling the charts. If anything looks funky after recategorizing, because that's going through the admin flow rather than a native workflow, we haven't paid much attention to it. But there is a button in the Workspace page where it says "backfill the last 14 days." So if you recategorize and click that, you just wait a minute and things should be populated.

**Stevie Kim:** Oh, that's great. I either didn't notice it or forgot about it.

**Jose Farias:** It's new.

**Stevie Kim:** Okay, cool. Yeah, no, that's great. I will do that after this call for the one that I have. It's kind of ad-hoc me getting to the things I need to do for that ticket. But yeah, no, that's perfect. Okay, great.

**Stevie Kim:** So that's the only thing I kind of wanted to bring up. And then another thing is, if anybody has time to review any pull requests that are sitting there or if any tickets need clarification, please speak up. But also if you think about things that are missing from our launch plan, I feel like there's just going to be things we totally forgot about.

**Stevie Kim:** So yeah, if anybody thinks of things, please bring it to my attention, and even if you don't have time to create the ticket, I'll try to create it with user stories and acceptance criteria. I was talking to Leo about that and I want to get better about it. It helps me understand what is expected, and I think it'll help us align better with what is in Marcel's head and what his expectations are. So we can confirm that in writing instead of dealing with ambiguity.

**Jose Farias:** I definitely think it's helpful. For what it's worth, I think we're at a very amorphous phase of product development right now—getting ready to launch. So it's natural that things change last minute and it's hard to capture everything. Then any one of us captures their own impression of how things should work, and then Marcel comes in and completely rewrites things. That's how this usually goes. So I would say, speaking for myself, I'd be comfortable without necessarily having all the fleshed-out acceptance criteria. I understand that's suboptimal, but at this stage things change last minute.

**Stevie Kim:** Yeah, yeah. I was just thinking it might be a way to get ahead of that. But I'll think a little bit more because I'm trying to get this into a more proactive state where we're not just waiting for Marcel to catch things—like we know what he wants ahead of time. But yeah, it's probably not the best time to try to do that.

**Jose Farias:** I think there's going to be some tension there. But if you find the time that's great—that's definitely helpful.

**Stevie Kim:** So does anybody have anything on their mind that's not on their update or anything about the launch plan or blockers we need to ship? Is there anything anyone is confused about or doesn't really know the acceptance criteria for? Because I can try to get that information for you in the background.

**Jose Farias:** Yes. One thing for me. I just thought about this. So the ticket for "a workspace owner should be able to invite users to workspace"—usually that comes bundled with different assumptions from the engineering team versus product. Usually the point of attention there is roles. Like usually people expect "oh, you're implementing invitations." Obviously we're implementing roles as well, and that's a whole other system.

**Stevie Kim:** Right. Yeah, yeah. Yeah. It is a whole thing. Well, when I originally had that ticket, it was for something else that I didn't realize was already there. So it kind of needs to be thought out and fleshed out more.

**Stevie Kim:** And I think one of the biggest things missing from my mind is the user experience within the workspace. So they submit their domain through onboarding, we create a workspace based on that, and then what control and power do they have from then on? Like do they have the power to create another workspace with a different brand? I don't know how any of that is supposed to work. And can they invite users to their workspace? We've got this tied to the billing stuff too. One workspace per subscription, I think is what Marcel had. So yeah, there's some stuff that's not fleshed out at all. But I wanted to confirm that because maybe it is. Rules and permissions—we haven't thought through any of that.

**Jose Farias:** So yeah, I just want to call out: there is no system for roles currently. The one level of hierarchy we handle currently is just GrowthX admins—you, Jason, Marcel, and us—and then everyone else. Those are the two things we support currently. So the straight shot would be just inviting users means any new user can do everything, right? That's the straight path. If you want to add roles on top of that, that's not super complex but it is a system that we need to design. So a couple days of work.

**Stevie Kim:** Okay. I'll make sure I understand what Marcel has in mind as far as what we want to allow users to do and not do, because it has changed so much and every time I think I know it's not that way. Then I misremember things based on past conversations. So yeah, I'll spend some time on that and really think through it, and if I have any outstanding questions, I'll ping Marcel.

**Jose Farias:** That's good. That was the one thing for me.

**Stevie Kim:** Anything on anybody else's mind?

**Stevie Kim:** Cool. All right. Well, those are the only things I wanted to cover to make sure I wasn't blocking anybody and to share my thoughts on setting up and helping out the EMs with their workspaces. Right now it's doable and manageable, and I think it'll be okay. So I don't think we need to do anything on our end as far as giving everybody admin access. But we'll see. I just don't want to go into panic mode because I'm getting overrun and end up giving everyone admin access because I can't help them with their workspaces. That's what I'm trying to avoid. So I'll think a little bit more and talk to maybe Jason and others about what we want to give to who.

**Stevie Kim:** All right. Well, if nobody has anything else, we can get some time back.

**Leonardo Carpenedo Steffen:** Okay. Thanks, y'all. Thank you. Thank you.

**Stevie Kim:** Bye. Bye.
