# CheckThat Weekly Check In

---
title: CheckThat Weekly Check In
date: 2026-01-26
duration: 37 minutes
participants:
  - name: Marcel Santilli
    role: CEO / Founder
    affiliation: GrowthX
  - name: Leonardo Carpenedo Steffen
    role: Engineer
    affiliation: CheckThat
  - name: Stevie Kim
    role: Product Manager
    affiliation: CheckThat
  - name: Jose Farias
    role: Engineer
    affiliation: CheckThat
  - name: Daniel Lopes
    role: Engineer
    affiliation: CheckThat
  - name: Pedro
    role: Engineer
    affiliation: CheckThat
  - name: Jason
    role: Product / Operations
    affiliation: CheckThat
organizer: Marcel Santilli (marcel@growthxlabs.com)
organizer_affiliation: GrowthX
meeting_type: Product weekly standup
source: fireflies
fireflies_id: 01KFESEHMP7ZNXXZQ8NQDSBT7T
transcript_url: https://app.fireflies.ai/view/01KFESEHMP7ZNXXZQ8NQDSBT7T
enriched_on: 2026-03-01 00:00 UTC
---

## Summary

CheckThat locked in three critical launch decisions: (1) workspace invitations tied to specific invited email addresses for security; (2) two-tier permissions with workspace owners controlling billing/invites and members managing prompts/content only; (3) RudderStack chosen as event tracking pipeline with Intercom and Customer.io for lifecycle messaging launching this week. All decisions trade flexibility for speed—future features (admin tier, multi-account linking, workspace deletion UIs) deferred as fast-follows.

## Context

Weekly product engineering standup for CheckThat, GrowthX's AI visibility index for B2B software companies. Team is one week from launch and operating in ruthless scope-cut mode: every feature decision is either "core to launch" or "fast-follow." This meeting focused on three blocking product questions that affect user onboarding, data integrity, and go-to-market readiness. The team has been iterating on permission models and analytics architecture for two weeks; today marked the inflection point where decisions shifted from exploratory to committed.

## Relevance to GrowthX

**Product & Launch:** CheckThat is GrowthX's strategic software bet. Launch is locked for week of Jan 26—these decisions determine whether the app is feature-complete and secure on day one. Permission model affects onboarding friction; workspace deletion workflow is table-stakes for user trust.

**Growth & Analytics:** RudderStack + Intercom integration directly impacts ability to measure acquisition, activation, and lifecycle metrics post-launch. URL-based attribution enables CAC/LTV analysis from day one. Without event tracking configured this week, CheckThat launches blind.

**Sales & Operations:** Separate HubSpot instance decision affects sales process design, reporting structure, and whether new AE can close CheckThat deals without contaminating GrowthX enterprise pipeline. Deferred to Jason this week but must resolve before scaling sales.

**Revenue:** Simplified permission model (no per-seat billing, admins optional at launch) reduces time-to-revenue but accelerates deployment of enterprise features in fast-follow phase. Reduces day-one support burden while preserving growth upside.

## Open Questions

1. **HubSpot integration:** Separate CheckThat instance or shared with GrowthX? This affects data quality, sales process, and cross-company insights. Requires decision + setup time before scaling AE hiring. (Assigned to Jason, may pull in Jeff Ignacio.)

2. **Workspace deletion UX:** Support ticket vs. in-app form vs. Intercom widget? Needs definition this week to unblock Daniel's Intercom setup. (Assigned to Daniel, Stevie to create ticket.)

3. **Admin tier urgency:** How soon do we need invite permissions decoupled from billing? Affects whether this is a week-1 fast-follow or deferred to week-2+. (Assigned to Marcel, impacts roadmap prioritization.)

## Decisions & Commitments

**DECISION: Invitations tied to specific email addresses.** Rationale: Prevents forwarded-invite security loopholes and reduces support burden at launch. Flexibility (multi-email logins, account merging) deferred to fast-follow phase. Committed by: Marcel, Daniel.

**DECISION: Two-tier permission model at launch (Owner / Member).** Workspace owners control billing and invites. Members manage all prompts/content but cannot invite or modify billing. No role-change UI at launch—support flips the boolean if needed. Future: Admin tier that allows invites without billing access. Committed by: Marcel, Pedro.

**DECISION: Everyone is a Member by default; all members can invite.** Override to original plan (owner-only invites) because per-seat pricing is not launching. Risk of "everyone invites" is lower than risk of "no one can invite." Committed by: Daniel, Marcel.

**DECISION: RudderStack for event tracking.** Open-source Segment alternative with same integrations. Integrates with HubSpot, Intercom, Customer.io, Google Tag Manager. Addresses Marcel's concern about Twilio (Segment parent) as stagnant company. Committed by: Daniel.

**COMMITMENT: Workspace deletion + billing management routed to support (no UI at launch).** Workaround: Help link or Intercom form in account settings directing users to support. Daniel owns implementation; Stevie creates ticket. Committed by: Daniel, Stevie.

**PENDING: HubSpot integration architecture.** Jason and team to investigate separate CheckThat instance vs. shared GrowthX instance. Marcel's instinct: separate (PLG data + enterprise data in one CRM = dirty data nightmare). May bring in Jeff Ignacio to help with setup. Decision deferred to this week.

## Overview

- **Invitations:** Tied to specific invited email addresses (not user-selectable) for security. Multi-email support deferred to fast-follow.
- **Permissions at launch:** Two-tier model—Workspace Owner (billing + invites) and Workspace Member (content management). All invited users start as Members; Members can invite others.
- **Account management:** Billing upgrades, workspace deletion routed to support (no UI). Help link or Intercom form in account settings directs users.
- **Event tracking:** RudderStack (open-source, Segment alternative) chosen for event pipeline. Integrates with Intercom, Customer.io, Google Tag Manager, and HubSpot. Launches this week with Intercom + Customer.io.
- **Attribution:** URL-based tracking for sign-up sources. User identification flows through RudderStack to all downstream tools after email capture.
- **Launch scope:** Ruthlessly cut. Fast-follows queued: admin tier (invites without billing), multi-account linking, workspace owner migration UIs, enhanced role-based access controls.
- **HubSpot decision:** Pending investigation (Jason). Separate CheckThat instance vs. shared GrowthX instance. Marcel's preference: separate (avoids PLG/enterprise data contamination). Decision needed before scaling AE team.

## Key Topics

### User Invitation Flow (Discussion: ~10 minutes)

**The Question:** Should workspace invitations be tied to the specific invited email, or should users have the flexibility to accept invites with a different email address (like in Slack, Notion, Linear)?

**Background:** Daniel advocated for flexibility (allows multi-email logins, useful for users managing multiple competitor workspaces). Marcel prioritized security and simplicity (prevents forwarded-invite breaches). Team compared behavior of Slack, Notion, Figma, Linear, Basecamp.

**Decision:** Tie invitations to the invited email address only. No user choice at acceptance time.

**Rationale:** Launched constraints outweigh flexibility edge cases. Security loophole risk (forwarded invites to unauthorized people) exceeds the pain of Pedro-like onboarding hiccups. Fallback: admin can re-invite if sent to wrong email. Future: multi-account linking and account merging deferred as fast-follow.

### User Roles and Permissions (Discussion: ~5 minutes)

**The Model:**
- **Workspace Owner:** Manages billing, invites users, can delete workspace.
- **Workspace Member:** Manages prompts and content; cannot invite, cannot modify billing.

**For Launch:** All invited users become Members. Only the workspace owner can initially invite others. No role-change UI—if someone needs to become owner, support updates the DB. No Viewer role yet.

**Future:** Admin tier (can invite without billing access) queued as week-2 fast-follow because free seats + non-monetized launch means "everyone invites everyone" is safe risk-taking.

### Analytics and MarTech Architecture (Discussion: ~8 minutes)

**Stack Decision:** RudderStack (open-source Segment alternative) as event pipeline. Replaces Segment/PostHog discussion because RudderStack has integrations with HubSpot, Intercom, Customer.io, Google Tag Manager.

**Implementation (Daniel's Week):**
1. Output migration (nearly done; downtime scheduled before 6pm tomorrow for workflow updates)
2. RudderStack + Intercom + Customer.io + Google Tag Manager integration
3. Event tracking for all user actions (add prompt, remove prompt, invite, etc.)
4. URL-based sign-up attribution (tie users to source page/button)
5. User identification: After email capture → RudderStack → all downstream tools

**Why RudderStack over Segment:** Open source means self-hosting option if CheckThat scales. Twilio (Segment parent) is stagnant; RudderStack is actively developed.

### HubSpot Integration Strategy (Discussion: ~4 minutes)

**The Dilemma:** Should CheckThat data (PLG users, signups, AI visibility metadata) pipe into the existing GrowthX HubSpot instance (with enterprise deals, contracts, AE pipeline) or into a separate CheckThat instance?

**Marcel's Position:** Separate instance. Mixing PLG and enterprise sales data in one CRM creates dirty data and reporting confusion. Every company that tries it regrets it. Keep them separate, decide on integrations later.

**Status:** Deferred to Jason + team for investigation this week. May involve Jeff Ignacio (setup expertise). Decision needed before hiring new AE for CheckThat (need clean data model).

## Action Items

### Marcel Santilli (GrowthX)
- Work with design/comms to define how permission changes (Owner vs. Member) and role differences are communicated on invite page and invite-acceptance UI
- Finalize messaging on admin/member tier roadmap (when to launch, how to communicate to early users)

### Jose Farias (CheckThat)
- Update original Slack ticket to reflect final decision: invitations are tied to specific invited email address (not user-selectable)

### Pedro (CheckThat)
- Sync with Stefan on billing implementation details (Clerk integration, upgrade/downgrade UX)
- Update product ticket with final role and permission specs for workspace owner and workspace member

### Daniel Lopes (CheckThat)
- Complete output migration and schedule downtime for workflow updates (deadline: before 6pm tomorrow)
- Implement MarTech stack: RudderStack pipeline, Intercom integration, Customer.io integration, Google Tag Manager
- Add event tracking for all user actions (add/remove prompt, invite, etc.)
- Configure URL-based attribution for sign-up sources
- Coordinate with Jason on HubSpot integration (provide technical requirements)

### Stevie Kim (CheckThat)
- Create ticket for workspace deletion workflow: define whether it's support-only, in-app form, or Intercom widget

### Leonardo Carpenedo Steffen (CheckThat)
- Provide feedback on workspace invitation flow from async Slack discussion (already read thread)

### Jason (CheckThat / Product Ops)
- Investigate HubSpot integration architecture: separate CheckThat instance vs. shared GrowthX instance
- Recommend approach based on data quality, sales process, and reporting needs
- Explore bringing in Jeff Ignacio for setup if moving forward with separate instance

---

## Full Transcript

**Marcel Santilli:** Good morning, everyone. Or happy Monday.

**Leonardo Carpenedo Steffen:** Happy Monday. How you?

**Marcel Santilli:** Pretty good.

**Stevie Kim:** Hey y'all. So this meeting is being recorded. We already had standup this morning where we went through what we accomplished, what we're planning to do, and any blockers. But we did need some feedback on one of those items. It was posted in Slack and in the Notion doc—I shared it in the Zoom chat as well. Essentially it's feedback on workspace invitations. We'd love your feedback, Marcel and Daniel. If you have a second to check out that Slack thread, that would be great.

**Marcel Santilli:** What's the context here?

**Stevie Kim:** During standup we had a discussion on inviting users to workspaces and how much flexibility the user should have. Jose can explain it better. We wanted to get feedback from you guys to make sure we're on the right path.

**Marcel Santilli:** I understand the concept of invitations. Can somebody give me an actual question that requires input? I feel like you're just talking as opposed to saying what input we need specifically.

**Stevie Kim:** Yeah, I was going to have Jose take that on. The message is in Slack. I put the link in the Notion doc and linked it in the Zoom chat so everybody should have access.

**Daniel Lopes:** I think the second option is the only way to go. I already read everything and can explain why.

**Marcel Santilli:** I think this is related to inviting entire domains or agencies?

**Daniel Lopes:** No, this is about email. When you add somebody, you type their email. They get the invite and see that email is the only one they can use and it's tied to that specific workspace. The question is: do they get to choose which email they want to use? I think we need to let people choose because we only have one brand per workspace. It will be very common to have users tracking competitors with another workspace. Sentinel One tracks four competitors across different workspaces. AirByte does the same. So multiple workspaces will be common. We can't assume folks have just one workspace. Letting people control which email they use with that workspace opens up flexibility without much extra effort.

**Marcel Santilli:** I understand. Isn't it just like every other system where there's a members or users section, you type in an email, select permissions, click Invite, and then they have to accept using that email only? Everything else is just permissioning.

**Daniel Lopes:** The decision is: do we tie to that specific email or let them pick another? I use both GrowthX AI and GrowthX Labs—I can't use Google login with GrowthX AI because of this.

**Marcel Santilli:** That's a huge security loophole. If I invite you and you forward the email, someone else with a different email gets access to my dashboard. That's huge. When I send invites to the wrong email in Figma, sure, it happens, but the organization hasn't swapped domains. Keep it simple: whatever email you invite, that's the only email they can use. If it's wrong, they talk to the person who invited them and get re-invited to the right email.

**Jose Farias:** My impression is that's not how most tools work.

**Marcel Santilli:** Most?

**Jose Farias:** Most tools let you choose.

**Daniel Lopes:** Yeah.

**Marcel Santilli:** So if I invite Jose at Growth Hacks AI in Figma, you're saying he can pick any email on the planet? That's how Slack works?

**Daniel Lopes:** That's how Slack, Linear, and Basecamp work. You log in with that email, accept the invite with that email, so it means you came from that email. Then you can add another one if you want.

**Jose Farias:** One clarification: you're never really asked which email you want to choose. If I'm already logged into Figma and you invite me, I click the link—I'm already logged in—so I'm not asked which email I'd like to choose. It's just accept invite.

**Marcel Santilli:** So if I type this email and click Invite, what would show here if they choose a different email?

**Jose Farias:** It would show what you invited. But once they create an account, the invitation stops appearing. Then there's a different screen for users.

**Marcel Santilli:** As an admin, if I'm a security company (Sentinel One) and I invite marcelsentinel1.com, but then I see marcelmail.com in the system, I'd think it's a data breach. I'm trying to understand where we need that flexibility.

**Daniel Lopes:** We need to do the same thing as everyone else. The point is I don't think we're understanding how login works. If you're already logged in with another email, you cannot accept the invitation on that other email. You need a screen that says "do you want to use this email?" It has to match. Let the person choose, because otherwise you're tying the invitation to another domain. That's the real risk.

**Marcel Santilli:** I just don't understand: if you can only use work emails, how can someone use a different email? Other than agencies like us that changed domains early?

**Daniel Lopes:** This is more technical. I have two accounts: Canopy and GrowthX. I have two logins. I'm logged in with Canopy. I receive an invite on my GrowthX email. I click the link—my browser is logged in as Canopy. So it's going to tie the invitation to Canopy. We need a screen before that that says "pick your right one" or "you're not using the same account." It's what Google does—Google says switch accounts because this invite came from another account, then you see the dropdown.

**Marcel Santilli:** That makes sense. But if Yusuf sends an invite to a new employee, that employee can't accept it and log in as their Gmail. They have to switch between accounts—that's common in Notion. I can see all accounts and add another account. So I add another sign-in and both are tied together. But if I'm Sentinel One and I invited you, I only ever see the person I invited—not your other email. That's more important in a context where people manage multiple companies on behalf of those companies, not people working at those companies.

**Daniel Lopes:** Yeah.

**Marcel Santilli:** There's also a launch thing. For now, yes, it's a pain if you're in an edge case with multiple workspaces. But the solution is the workspace admin adds whatever. I'd only have my Sentinel One email and GrowthX email. I have 50 workspaces added to it. Later we can connect workspaces as a feature.

**Daniel Lopes:** Yeah, that makes sense. And also domain allow lists for domains.

**Marcel Santilli:** Yeah.

**Jose Farias:** We're touching on something important. Auth is complicated and we're not reinventing the wheel. Tying it to a specific email address exists, letting the customer choose exists, merging accounts exists, account pickers exist. They're all different ways to approach this. In the interest of moving forward, I think we need to make a decision and do the simplest thing possible, even if it underwhelms certain use cases. Building the ideal experience will take too long.

**Leonardo Carpenedo Steffen:** If you can revert it later or merge accounts later, then doing the simplest thing in the interest of time makes sense. What do you guys think?

**Jose Farias:** We're at a point where either approach takes practically the same amount of time. Let's go with tying it to a specific email address. Though I'm hesitant because Daniel's instinct at the beginning was the opposite—letting the recipient choose.

**Marcel Santilli:** Yeah.

**Daniel Lopes:** Tying is better because you can add flexibility later. And time-wise you're constrained.

**Marcel Santilli:** Yeah. Notion has it right. It's the simplest: I have this email, these are all the workspaces I have access to. That's it for now. Later we add another account.

**Jose Farias:** For what it's worth, Notion does letting people choose, not tying it. It happened to Pedro when onboarding at GrowthX. He accepted the invitation with his personal email because he uses Notion personally. Then Yusuf had to reach out and ask him to accept with the right email. That's what Notion does.

**Marcel Santilli:** Back and forth because that's what Notion does. If you send an invite link—which is lazy and what we do sometimes but shouldn't—and you accept it, that's what happens. But it would show up as a different thing. It wouldn't be associated to this email. So right now if you check, it's only this option. Later you can add another account and sign in with that login. Then both would show up as different organizations with their own group of workspaces attached. That sounds good.

**Jose Farias:** Okay, then we can move forward with tying it to the specific email address that was invited.

**Marcel Santilli:** Sounds good. For now, is everyone admin by default? Or is there a view-only concept? Not trying to add scope, just understand.

**Jose Farias:** Was that part of it, Pedro?

**Pedro:** We have the admin group (CheckThat admin). Then workspace owner and workspace member. Workspace member cannot invite other workspace users. That's the main difference.

**Marcel Santilli:** But they can delete the whole thing?

**Pedro:** No, they can only delete workspace users.

**Marcel Santilli:** But they can go in and delete every prompt if they want, right?

**Pedro:** Yeah.

**Daniel Lopes:** It's easy to add defense later because you already have the owner concept. That's the only addition.

**Pedro:** We have the workspace member role, which can be owner and member. We can build authorization on top of that.

**Marcel Santilli:** So for now it's owner or member. Owner can change billing and invite users. Member can manage everything—prompts, contacts—but can't invite or touch billing. Later we add a workspace viewer (view-only). Okay, cool.

**Pedro:** Yeah, I still need to sync with Stefan about billing, but that's how it will work.

**Marcel Santilli:** We need to figure out how to communicate this on the invite page. How do we say workspace owners vs. members and what they can't change? Usually it's where the role is shown.

**Daniel Lopes:** For simplicity, let's not allow changing the owner. If you can't change the owner, you don't have to explain much. Whoever buys it controls billing. Whoever can invite. We just say "owner" in the table with a tooltip saying "can invite and change people." If anyone needs to change the owner, they message support and we flip it in the backend.

**Leonardo Carpenedo Steffen:** Just communicate that this change is coming soon. If you're adding new features, tell people they'll be able to change user permissions soon. Communicate it simply.

**Marcel Santilli:** Just to be clear: you can only invite members, not owners. Members can't see billing or request upgrades or invite others. So until we change that, only one person can invite team members. If an IT person signed up but the team wants to invite others, what happens?

**Daniel Lopes:** They talk to their owner and ask the owner to invite. That's what Figma and others do. We'll add multiple owners later.

**Marcel Santilli:** Okay.

**Stevie Kim:** Pedro, if you could update my original ticket to reflect this?

**Marcel Santilli:** If it's not too much trouble.

**Daniel Lopes:** We need a ruthless cut. This is the last week. Let's not add anything.

**Marcel Santilli:** We can always add after. If this does really well, letting other people invite should be a fast follow.

**Daniel Lopes:** Yeah, it should be fast-follow. We need to prioritize it.

**Stevie Kim:** Everything around billing and user management will be super fast-follow that handles more of what you'd normally expect.

**Marcel Santilli:** As a fast follow, can someone create a ticket for an admin tier? You can invite admins, and admins can invite others but not change billing. We want people inviting each other—more people, more growth.

**Daniel Lopes:** Another option: just let people invite anybody. No restrictions.

**Marcel Santilli:** I prefer that because we don't have per-seat pricing. The tradeoff is how quickly we build another tier. The only thing we need to block is really destructive: delete workspace and change billing. Since we don't charge per seat, let people invite whoever they want.

**Marcel Santilli:** Later, when we add an admin tier or someone who can manage prompts and delete prompts, do we downgrade everybody to member so they can't invite?

**Daniel Lopes:** That's how Canopy does it. It's all pretty safe—nobody complains.

**Marcel Santilli:** So right now everyone is a member. Members can invite and delete/manage any prompt. Once we add an admin tier, admins will only be able to do some actions. For now, every invite is a member, and members can do everything except touch billing or delete the workspace. That's better because we'll see if people are inviting. Yeah.

**Daniel Lopes:** There's a real engagement risk if people can't get others invited. Stevie, we need a ticket: we need a place in account settings for users to request to cancel their account or delete their workspace. We don't need to build the feature—just a link or form.

**Marcel Santilli:** Is workspace deletion in the manage account section? Is that managed by Clerk?

**Jose Farias:** No, accounts are managed by us. Users are managed by Clerk.

**Marcel Santilli:** So this view is managed by us?

**Daniel Lopes:** Correct.

**Marcel Santilli:** So where would a user cancel? In a billing section?

**Pedro:** Right there.

**Daniel Lopes:** Clerk has a billing option, but billing is different from "delete my account." You can't put that there.

**Marcel Santilli:** So there should be something clearly visible saying "request to delete this account."

**Daniel Lopes:** People can come through support. You might not even need a form. But we need something for account deletion and workspace deletion.

**Marcel Santilli:** A help link with a form. Not an email, just a form.

**Daniel Lopes:** Yeah.

**Marcel Santilli:** Or an Intercom form. Just checking: is the goal to have Intercom for launch?

**Daniel Lopes:** Yeah, for launch. What's on my plate this week: finish the output migration (almost done with the workflow), then schedule downtime before 6pm tomorrow for workflow updates. Then MarTech and support integration: RudderStack, Google Tag Manager, Customer.io, and Intercom.

**Marcel Santilli:** Okay.

**Daniel Lopes:** All events too—adding prompts, removing prompts, inviting people. All trigger events. Activity feeds in Intercom and Customer.io are installed through RudderStack.

**Marcel Santilli:** Got it. One thing: we need URL tags or something to track where people come from at sign-up. If they click the top button vs. bottom button vs. a link. We need to track what they interacted with that led to the event. Either trigger an event or pass it as a URL parameter. If we don't pass events to GA or analytics, we lose tracking. We need to track the source and what action led to conversion.

**Daniel Lopes:** We can do everything URL-based because everything is page-based. Sounds good.

**Marcel Santilli:** Also, identifying people after we get their email is critical—probably our biggest gap. RudderStack handles that?

**Daniel Lopes:** RudderStack, yeah. It's a one-to-one replacement for Segment. It's Segment's biggest threat.

**Marcel Santilli:** So we don't need GA pixels? Everything goes through the RudderStack pixel?

**Daniel Lopes:** Yeah, exactly like Segment. I was going to use Segment, but RudderStack is taken care of.

**Marcel Santilli:** Jason, check if RudderStack integrates with HubSpot. We need to decide whether to use our current HubSpot instance or create a separate one for CheckThat. Both have pros and cons—it's complicated.

**Daniel Lopes:** RudderStack is also open source, so if you scale you can self-host. And it has everything—including HubSpot and Intercom.

**Marcel Santilli:** I'd avoid Segment because Twilio (parent company) has zero innovation. RudderStack looks better. The HubSpot decision: separate instance vs. shared. Mixing PLG and enterprise in one CRM is a nightmare—dirty data from account signups and deal cycles get tangled. Every company that tries it regrets it. My instinct: keep them separate and figure out integrations later. Jason, you've looked at this before? We have an AE starting soon, so we need a clean data model. Can Jeff Ignacio help with setup? Maybe Leah too. Let's prioritize this week. Thanks team.

**Daniel Lopes:** Thank you.

**Marcel Santilli:** See ya. Bye.
