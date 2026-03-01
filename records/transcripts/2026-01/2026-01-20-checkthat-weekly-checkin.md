# CheckThat Weekly Check In

---
title: CheckThat Weekly Check In
date: 2026-01-20
duration: 19 minutes
participants:
  - Jose Farias (CheckThat — Engineering)
  - Stevie Kim (GrowthX — CheckThat Product Lead)
host: Stevie Kim
attendees:
  - Jose Farias
  - Stevie Kim
source: fireflies
transcript_id: 01KF9PN6FJW8ZWPR4CY8BNW08Y
transcript_url: https://app.fireflies.ai/view/01KF9PN6FJW8ZWPR4CY8BNW08Y
enriched_on: 2026-03-01 00:00 UTC
---

## Summary

Stevie and Jose aligned on three blockers for CheckThat's launch: (1) admin access policies — limiting who can modify public pages while supporting EMS team workspace setup; (2) missing roles and permissions system — currently only GrowthX admins vs. everyone else, needs design; (3) workspace ownership UX — unclear how users create additional workspaces, how invitations tie to billing, and what controls owners have. Jose flagged the tension between detailed acceptance criteria and rapid product iteration. Stevie will clarify workspace permissions with Marcel and discuss admin access policies with Jason.

## Context

Weekly CheckThat product sync between Stevie Kim (GrowthX product lead) and Jose Farias (CheckThat engineering). Marcel and Daniel were absent, so Stevie kept the meeting focused on operational blockers. CheckThat is in pre-launch phase; Stevie is supporting the EMS (engagement management) team's workspace setup for client demos while managing the engineering team's availability. The team is experiencing the classic tension between wanting detailed specs and the reality of rapid product iteration before launch. Key context: GrowthX's EMS team will demo CheckThat to clients, so workspace setup and user experience directly affect sales readiness.

## Relevance to GrowthX

**CheckThat Launch & Sales Readiness:**
- Admin access and permissions policies determine how quickly EMS can prep client-facing demo workspaces
- Missing roles/permissions system is a launch blocker if GrowthX plans to invite clients or EMS users with restricted access
- Workspace ownership UX directly affects sales positioning — unclear if CheckThat supports multi-workspace customers

**Product & Engineering:**
- Tension between detailed specs and rapid iteration affects how the team captures requirements
- Backfill feature (Jose's 14-day retroactive data fix) unblocks data consistency issues for recategorization workflows

## Key Decisions

- **Admin Access Policy:** Stevie will hold on granting full admin access to EMS team members for now; instead, she'll continue acting as a buffer to manage workspace setup, preventing accidental public page modifications.
- **Acceptance Criteria Approach:** Jose noted this is an "amorphous product development phase" — detailed specs are impractical when things change last-minute. Stevie acknowledged the tension but will try to get ahead of Marcel's expectations by writing user stories.
- **Roles System:** No roles/permissions hierarchy exists yet. Current structure: GrowthX admins (Marcel, Jason, Stevie) vs. everyone else. Adding roles would take a few days of design and development work.

## Open Questions

- How many workspaces can a single user/organization create?
- How do workspace invitations tie to billing (one workspace per subscription)?
- What controls should workspace owners have vs. regular users?
- What level of admin access should EMS have to safely prep demo workspaces?
- How does Marcel want the workspace ownership UX to work?

## Key Topics

### Workspace Access and Admin Permissions
Stevie is managing EMS workspace setup manually (content prep, fixing categorization) while acting as a buffer between EMS requests and the engineering team. Admin access is restricted because admins can modify public pages, which could break the product. Only Jason and Marcel currently have admin rights. Jose mentioned a new "backfill last 14 days" feature that retroactively fixes chart data after recategorization — this unblocks the manual workaround.

### Stripe and SaaS Setup
Stevie is completing Stripe account setup. Some SaaS subscription details are still missing. This is foundational for billing and workspace-to-subscription mapping.

### Acceptance Criteria and Specs
Stevie wants to write user stories and acceptance criteria upfront to better align with Marcel's vision. Jose pushes back, noting the product is in a "fluid development phase" where specs become obsolete quickly — Marcel often rewrites requirements last-minute. The team agreed there's tension here, but Stevie believes being proactive could help avoid surprises.

### User Roles and Permissions System
Critical gap: the system currently has only two permission levels — GrowthX admins vs. everyone else. There's no concept of customer admins, workspace owners, or read-only users. Inviting a user currently means giving them full product access. Adding a roles system would require design work and a few days of engineering effort.

### Workspace Ownership and Multi-Workspace Strategy
Unclear how the product should handle workspace creation and ownership. Key unknowns: Can users create multiple workspaces? Is it one workspace per subscription? How do invitations and billing interact? What controls do workspace owners have? Stevie needs clarity from Marcel before the team can design the user experience.

## Action Items

### Stevie Kim (GrowthX)
- Complete Stripe account setup and add missing SaaS subscription details
- Use the "backfill last 14 days" feature to retroactively fix chart data after recategorization
- Continue supporting EMS team with manual workspace content preparation for client demos
- Create launch tickets with user stories and acceptance criteria for missing items
- Clarify with Marcel the intended user experience for workspace ownership, invitations, billing, and multi-workspace support
- Discuss admin access policies with Jason to determine safe permission levels for EMS team

### Jose Farias (CheckThat — Engineering)
- Review pull requests from the team
- Provide feedback on admin access restrictions and roles/permissions system design
- Flag any unclear acceptance criteria or blocking requirements on assigned tickets

## Full Transcript

**Stevie Kim:** Cool. So I know Marcel and Daniel can't make it, and since we covered quite a bit this morning, we can probably move through things pretty quickly.

**Stevie Kim:** I'm just getting the Stripe account set up and still need to add some details. Let me know if anything's missing or if you need information from me on that. I don't want to be the blocker there. I think the basics are at least set up.

**Stevie Kim:** So the EMS team has been added to their customer workspaces. We're getting some tickets from them that you're already working on. I've been trying to be the buffer there so you guys aren't seeing a lot of information coming from them, but they have raised a lot of UX things, and so has Jason. I need to go through some of those.

**Stevie Kim:** There's a lot of manual work that I'm trying to take care of for their particular workspaces, like fixing if it's in the wrong subcategory, etc.

**Stevie Kim:** The reason I bring that up is because most of them we haven't given admin access to, because of the ability for admins to mess up the public pages. Jason and I have done some onboarding, but I don't think it's enough to just give all of these admin access. I could be wrong. So I just wanted to get a sanity check on what you thought about that.

**Stevie Kim:** Right now, Carrie is helping me out with some stuff, and I'm doing work around getting those workspaces content to where they can actually demo and feel comfortable showing to customers. What are your thoughts about who we're giving admin access to?

**Jose Farias:** I think it ultimately depends on who we're comfortable changing the public pages like you said. When we recategorize, I don't think we're backfilling the charts if anything looks funky after recategorizing, because that's not a native flow. That's like going through the admin. We haven't paid much attention to it. There is a button in the workspace page that says "backfill the last 14 days." So if you recategorize and click that, you just wait a minute and things should be populated.

**Stevie Kim:** Oh, that's great. I either didn't notice that or forgot about it.

**Jose Farias:** It's new.

**Stevie Kim:** Okay, cool. I will do that after this call. That's perfect. Okay, great.

**Stevie Kim:** So that's the only thing I wanted to bring up. And then another thing — if anybody has time to review any pull requests sitting there or if any tickets need clarification. But also, if you think about things that are missing from our launch plan, I feel like there's just going to be things we totally forgot about.

**Stevie Kim:** So if anybody thinks of things, please bring them to my attention, even if you don't have time to create the ticket. I'll try to create the ticket with some user stories and acceptance criteria. I was talking to Leo about that and I want to get better about it. For one, it helps me understand what is expected. And also I think it'll help us align better with what is in Marcel's head and his expectations. We can confirm with that written down instead of kind of the ambiguity we've been trying to shape into something more defined.

**Jose Farias:** I definitely think it's helpful. For what it's worth, I think it's worth calling out that we are in a very amorphous phase of product development getting ready to launch. So I think it's only natural that things change last minute and it's hard to capture everything. Any one of us captures our own impression of how things should work, and then Marcel comes in and completely rewrites things. That's usually how this part of things goes.

**Jose Farias:** So I would say, for myself, I would be comfortable with not necessarily having all the fleshed out acceptance criteria. I understand that's suboptimal, but also at this stage, things change.

**Stevie Kim:** Yeah, I was just thinking that it might be a way to get ahead of that. I'll think a little bit more on that because I'm trying to get us in a more proactive state where we're not just waiting for Marcel to catch things, but know what he wants ahead of time. But yeah, it's probably not the best time to try to do that.

**Jose Farias:** I think there's going to be some tension there, but if you find the time, that's great. That's definitely helpful.

**Stevie Kim:** Does anybody have anything on their mind that's not on their update? As far as the launch plan and blockers we have to ship, is there anything anyone is confused about or doesn't really know the acceptance criteria for? Because I can try to get that information for you.

**Jose Farias:** Yes. One thing — the ticket for "workspace owner should be able to invite users to workspace." Usually that comes bundled with different assumptions from the engineering team versus product. The point of tension is roles. People expect that if you're implementing invitations, you're obviously implementing roles as well. And that's a whole other system.

**Stevie Kim:** Yeah, it is a whole thing. When I originally had that, I was thinking about something else that I didn't realize was already there. So it kind of needs to be thought out and fleshed out more.

**Stevie Kim:** I think that's one of the biggest things missing from my mind — the user experience within the workspace. So they submit their domain and we create a workspace based on that. And then what control and power do they have from then on? Do they have the power to create another workspace with a different brand? I don't know how that's supposed to work. Can they invite users to their workspace?

**Stevie Kim:** It's tied to the billing stuff too. I think Marcel had one workspace per subscription. So there's some stuff that's not fleshed out at all, but I wanted to confirm that. Like you said, roles and permissions, we haven't thought through any of that experience.

**Jose Farias:** I just want to call out that there is no system for roles currently. The one level of hierarchy we handle currently is just GrowthX admins — you, Jason, Marcel, and us — and then everyone else. Those are the two things we support currently.

**Jose Farias:** So the fast, straight shot would be simply inviting users means any new user can do everything. That's a straight shot. If you want to add roles on top of that, that's not super complex, but it is a system we need to design. So a couple days work.

**Stevie Kim:** Okay, I'll make sure I understand what Marcel has in mind for what we want to allow users to do and not do, because it has changed so much. Every time I think I know, it's not that way. I misremember things based on past conversations. So I'll spend some time on that, and any outstanding questions I'll ping Marcel on.

**Jose Farias:** So that's good. That was the one thing for me.

**Stevie Kim:** Anything else on anybody's mind?

**Jose Farias:** No.

**Stevie Kim:** All right, well, those are the only things I wanted to cover to make sure I wasn't blocking anybody and just sharing my thoughts on setting up and helping out the EMS with their workspaces. Right now it's doable and manageable and I think it'll be okay.

**Stevie Kim:** So I don't think we need to do anything on our end as far as giving everybody admin access. But I don't want to go into panic mode because I'm getting overrun and giving everyone admin access because I can't help them with their workspaces. That's what I'm trying to avoid.

**Stevie Kim:** So I'll think a little bit more about that and talk to maybe Jason and others about what we want to give to whom. All right, well, if nobody has anything else, we can get some time back.

**Jose Farias:** Yep, sounds good.

**Stevie Kim:** All right, thanks, y'all.

**Jose Farias:** Thank you.
