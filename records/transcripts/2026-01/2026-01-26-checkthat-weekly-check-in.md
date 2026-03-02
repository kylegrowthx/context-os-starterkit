# CheckThat Weekly Check In

<metadata>
date: 2026-01-26
time: 18:00 UTC
duration: 33 minutes
organizer: Stevie Kim (stevie@growthx.ai, GrowthX)
enriched_on: 2026-02-28 12:45 UTC
participants:
  - Marcel Santilli (marcel@growthxlabs.com, GrowthX Labs, CEO)
  - Daniel Lopes (daniel@growthxlabs.com, GrowthX Labs, Engineering)
  - Jason Gong (jason@growthx.ai, GrowthX, Product/GTM)
  - Pedro Steimbruch (pedro@growthx.ai, GrowthX, Product/Infrastructure)
  - Jose Farias (jose@growthx.ai, GrowthX, Engineering)
  - Estevão Mascarenhas (estevao@growthx.ai, GrowthX)
  - Jacopo (jacopo@growthx.ai, GrowthX)
  - Leonardo Carpenedo Steffen (leonardo@growthx.ai, GrowthX, Billing/Infrastructure)
  - Stevie Kim (stevie@growthx.ai, GrowthX, Product Operations)
fathom_recording_id: 117139387
fathom_url: https://fathom.video/calls/543288402
share_url: https://fathom.video/share/yLNUw-n2b94JbiPaa1W8YGrz7cQewyD1
source: fathom
</metadata>

---

## Summary

CheckThat's launch readiness review: finalized user invitation flow (invites tied to specific email to prevent security risks), locked down launch roles (Members can manage all content and invite others, but cannot access billing or delete workspace), and aligned on analytics and CRM strategy (Rudderstack as primary data pipeline, separate HubSpot instance for PLG vs. enterprise sales data).

---

## Context

CheckThat is in final sprint to launch (target: week of Jan 27). The team resolved critical decisions on user onboarding, permissions model, and go-to-market infrastructure stack. Marcel emphasized the need to keep launch scope ruthlessly minimal—adding only essential features, with fast-follow improvements queued for post-launch. Key tensions emerged around invitation UX (tying to specific email vs. letting users choose), user role granularity (single launch role vs. Owner/Member split), and CRM architecture (risk of data contamination between CheckThat's product-led growth model and GrowthX's enterprise sales operations). The team also discussed coverage: Nigel (new ADE) starting same week to drive sales engagement on CheckThat side, requiring separate reporting and HubSpot instance.

---

## Relevance

**Launch Blockers & Trade-offs**
- User invitation flow decided: invites tied to specific email (security, simplicity; flexibility deferred to account-picker fast-follow)
- Member role at launch with full permissions (maximizes engagement; friction from single invitation bottleneck mitigated by support-flow for workspace deletion)
- Workspace deletion requires support request (no self-serve delete to prevent accidents)

**Infrastructure & Integration**
- Rudderstack replaces Segment as primary data pipeline (open-source, self-hosting path, Twilio risk mitigation)
- Separate HubSpot instance for CheckThat (isolates PLG noise from enterprise sales data; integration coordination between two orgs required)
- Rogers Tech handles Rudderstack, Intercom, Customer.io, Google Tag Manager installation (Daniel owns)

**Product Decisions**
- No Owner role selection UI at launch; ownership tied to workspace creator; owner transfer available via support only
- Members cannot see billing, but can manage all content (prompts, context) and invite users
- Multi-owner capability deferred to fast-follow

**Go-to-Market**
- Nigel starting same week as launch; ADE reporting tied to separate CheckThat HubSpot (not GrowthX sales data)
- Event tracking via Rudderstack to Intercom/Customer.io for post-signup engagement and feature activation

---

## Overview

- **User Invitations:** To prevent security risks (e.g., invite forwarding) and simplify launch scope, invitations will be tied to the specific email address used for the invite.
- **User Roles:** All invited users will launch as "Members" with full content management permissions (prompts, context) and the ability to invite others. This maximizes early engagement and avoids friction.
- **Analytics Stack:** Rudderstack will be the primary data pipeline, replacing Segment. This choice mitigates risk from Twilio's lack of innovation and offers future self-hosting flexibility.
- **HubSpot Strategy:** CheckThat will use a separate HubSpot instance to prevent data contamination between its PLG model and GrowthX's enterprise sales data.

---

## Key Topics

### User Invitation Flow

  - **Problem:** Decide if users must accept invites with the exact email or can choose a different one.
  - **Rationale for Tying to Invite Email:**
      - **Security:** Prevents invite forwarding to unauthorized users.
      - **Admin Clarity:** Ensures admins see the expected user email (e.g., `user@company.com`), avoiding confusion or data breach concerns.
      - **Simplicity:** Matches the standard, secure flow of tools like Figma.
  - **Rationale Against Tying to Invite Email:**
      - **Flexibility:** Allows users to consolidate accounts, which is common for agencies or users tracking competitors in separate workspaces.
      - **User Experience:** Prevents login conflicts if a user is already logged in with a different email.
  - **Decision:** Tie invites to the specific email address. This is the simplest, most secure path for launch. An account picker can be added as a fast follow.

### User Roles & Permissions

  - **Problem:** Define user roles for launch, balancing security with the need for early engagement.
  - **Initial Proposal:**
      - **Workspace Owner:** Manages billing and invites.
      - **Workspace Member:** Manages content (prompts, context) but cannot invite users or touch billing.
  - **Revised Decision for Launch:**
      - **Role:** "Member" (no "Owner" role at launch).
      - **Permissions:** Full content management, ability to invite other users.
      - **Restrictions:** Cannot manage billing or delete the workspace.
  - **Rationale:** This approach maximizes early engagement by removing friction from the invitation process. It avoids the risk of users needing to contact support just to invite a colleague.
  - **Future State:** A more granular "Admin" role can be introduced later, potentially downgrading current "Members" to a more restricted role.

### Analytics & Marketing Tech Stack

  - **Problem:** Establish the analytics and marketing stack for launch.
  - **Data Pipeline:**
      - **Tool:** Rudderstack.
      - **Rationale:** A direct, open-source replacement for Segment that mitigates risk from Twilio's perceived lack of innovation and offers future self-hosting flexibility.
  - **Marketing & Support Tools:**
      - **Tools:** Intercom, Customer.io, Google Tag Manager.
      - **Implementation:** Daniel will install all tools via Rogers Tech this week.
  - **HubSpot Strategy:**
      - **Decision:** Create a separate HubSpot instance for CheckThat.
      - **Rationale:** Prevents data contamination between CheckThat's PLG model and GrowthX's enterprise sales data.
      - **Action:** Jason will prioritize this setup, potentially with help from Jeff Ignacio or Leah.

---

## Action Items

**Jose Farias (GrowthX, Engineering)**
- Enforce invite-email matching; update invite flow + UI
- Implement launch roles: Member can invite/manage prompts; block billing/delete; add owner tooltip; add support-only owner transfer

**Pedro Steimbruch (GrowthX, Product/Infrastructure)**
- Sync w/ Leonardo re: billing; then update Stevie's ticket + invite/permissions docs

**Unassigned**
- Create ticket for Member-to-Admin upgrade path (fast-follow: allow selected members to invite others without full owner access)

**Daniel Lopes (GrowthX Labs, Engineering)**
- Add support link/form for workspace deletion; route to support
- Install Rudderstack via Rogers Tech/GTM; send events to Intercom/Customer.io; add source tracking

**Jason Gong (GrowthX, Product/GTM)**
- Decide HubSpot setup (separate vs shared instance); prioritize with Jeff Ignacio or Leah; then configure Rudderstack→HubSpot integration

---

## Transcript

**Marcel Santilli:** Good morning, everyone, or happy Monday.

**Leonardo Carpenedo Steffen:** Happy Monday. How are you?

**Marcel Santilli:** Pretty good.

**[Small talk about Notion AI and Fathom notifications]**

**Stevie Kim:** This meeting is being recorded. We already had stand-up this morning, so we went through what we accomplished and what we're planning to do and blockers. We do need some feedback on one item. It's a Slack thread about workspace invitations—we'd love feedback from you, Marcel or Daniel.

**Marcel Santilli:** What's the context here? I understand invitations conceptually, but what specific input do we need?

**Stevie Kim:** During standup we discussed inviting users to workspaces and how much flexibility users should have in that flow. Jose can explain better.

**Leonardo Carpenedo Steffen:** I was trying to find a CheckThat workspace to join, but couldn't find one in my account.

**Jose Farias:** Please read the Slack thread. I put the decision doc in Notion and linked it in Zoom chat.

**Daniel Lopes:** I already read it. I think the second option is the only way to go.

**Marcel Santilli:** Is this about domains or agencies?

**Daniel Lopes:** Just email. When you invite someone, they get an invite. The question is: must they accept using the email you invited, or can they choose a different one? I think we should let people choose because customers often track competitors in separate workspaces. Sentinel-1 tracks four competitors; Airbyte has four different workspaces. Letting people choose which email is small lift and adds flexibility.

**Marcel Santilli:** Isn't it like every other system? You type in an email, click invite, they accept using that email. Then it's just permissioning.

**Daniel Lopes:** That's the question: tie to invited email, or let them choose a different one? I use GrowthX AI and GrowthX Labs with different logins. The risk is if someone is already logged into one account with a cookie, they click an invite link, it ties to the wrong account.

**Marcel Santilli:** I think tying to the email is a security loophole—if I forward an invite, someone else with a different email gets access. Every other tool locks it to the invited email (like Figma). If sent to the wrong email, they can contact whoever invited them.

**Jose Farias:** Actually, most tools let people choose. But to be clear, when you're already logged into one account and click an invite link for another email, you need an account-picker screen (like Google) to choose which one to use.

**Daniel Lopes:** Right. The issue is we need a screen asking which account to use, because if you're logged into Canopy and receive an invite on your GrowthX email, your cookie ties it to Canopy unless we show a picker.

**Marcel Santilli:** That makes sense. But if Sentinel-1 invites you, they see only the email they invited, not your other emails. That's more important than flexibility for the edge case of managing multiple companies.

**Daniel Lopes:** The solution is letting the workspace admin add another email later. For launch, tying to the invited email is simplest. We can add account-picker and multi-account linking as fast-follow.

**Jose Farias:** Auth is complex. Tying to email exists, customer choice exists, account merging exists, account pickers exist. They're all valid approaches. For launch, let's do the simplest thing and iterate.

**Marcel Santilli:** Notion does it right. You have one email, you see all workspaces tied to it. Later, you add another account and sign in with the other login. Both show up as separate, with permissions attached.

**Jose Farias:** Notion actually lets people choose, not tying to invited email. Pedro accepted a Notion invite with his personal email and had to be told to use the right one.

**Marcel Santilli:** That's only when using invite links. If I add a specific email in the UI, you can't accept from a different one. Invite links are lazy—we shouldn't use them.

**Jose Farias:** Agreed. Let's move forward tying to the specific invited email.

**Marcel Santilli:** So everyone is admin by default, or is there a role concept?

**Pedro Steimbruch:** We have Workspace Owner and Workspace Member. Members cannot invite other users.

**Marcel Santilli:** That's the main difference. Can Members delete content?

**Pedro Steimbruch:** They can delete prompts, but not other users.

**Marcel Santilli:** Can they delete everything?

**Daniel Lopes:** Yes. It's simple: Owner can change billing and invite; Member can manage all content but not invite or touch billing. Later we add Workspace Viewer.

**Daniel Lopes:** For launch simplicity, don't allow changing Owner in UI. Whoever signs up is the Owner and controls billing. Add a tooltip saying Owner can invite and manage users. If someone needs to change Owner, they contact support and we flip it in the backend.

**Marcel Santilli:** So only the Owner can invite Members, and Members can't see billing. Only one person can invite until we add multiple Owners as a fast-follow. If an IT person signs up but the company wants to invite others, they ask the Owner?

**Daniel Lopes:** Exactly. Talk to your Owner. That's how Figma and others do it.

**Stevie Kim:** Pedro, can you update my original ticket to reflect this decision?

**Daniel Lopes:** We need a ruthless cut. This is the last week—let's not add anything. We can always add fast-follow.

**Marcel Santilli:** Right. This should be fast-follow if it does well.

**Daniel Lopes:** Here's the risk: if we don't let other people invite, engagement dies. Let me propose: don't restrict invites. Let everyone invite everyone. Only block truly destructive actions: delete workspace and change billing.

**Marcel Santilli:** But then when we add Admin tier later, we'd downgrade everyone else?

**Daniel Lopes:** Yes. Like we did with Canopy. That pattern is safe.

**Marcel Santilli:** Okay. So for launch: everyone invited is a Member. Members can invite others, manage all content (prompts, context), but can't touch billing or delete workspace. Once we add Admin tier, Members get downgraded. The benefit: we'll see engagement and people inviting. The risk is managed.

**Daniel Lopes:** That's right. Maximizes engagement at launch.

**Daniel Lopes:** We also need a support link for workspace deletion. Don't build self-serve—just route to support via help link or Intercom form.

**Marcel Santilli:** Intercom for launch. Is that on your plate?

**Daniel Lopes:** Yes. This week I'm finishing the output migration and then installing all the marketing tech: Rogers Tech, Google Tag Manager, Customer.io, Intercom. All events trigger activations.

**Marcel Santilli:** What about tracking where people come from? UTMs or tags?

**Daniel Lopes:** All page-based. We can track everything through events.

**Jason Gong:** Once you implement that, we need to identify people post-signup with their email.

**Daniel Lopes:** Rudderstack handles that. It's a direct Segment replacement.

**Marcel Santilli:** Does Rudderstack integrate with HubSpot?

**Daniel Lopes:** Yes, and everything else. It's open-source too—we can self-host eventually.

**Marcel Santilli:** Good. Twilio (who owns Segment) has zero innovation. I prefer Rudderstack.

**Marcel Santilli:** Now the big question: do we pipe CheckThat activity into a separate HubSpot instance or mix it with GrowthX enterprise data?

**Daniel Lopes:** Separate. Every company that mixes PLG and enterprise in the same HubSpot has a nightmare of dirty data.

**Marcel Santilli:** Agreed. Plus Nigel (new ADE) is starting this week to run CheckThat sales. He needs separate reporting. Jason, you've looked into this before?

**Jason Gong:** Yes, but our Ops person left and we haven't backfilled. We kind of punted.

**Marcel Santilli:** Let's prioritize this week. Can Jeff Ignacio help? Maybe Leah? We have an ADE now, so a week or two to get it set up.

**Marcel Santilli:** Thanks, team.

**Daniel Lopes:** Thank you.

**[Call ends]**
