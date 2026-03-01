# Pylon Demo | Growthx

<metadata>
date: 2026-01-13
time: 22:30 UTC
duration: 12 minutes
organizer: yousef@growthxlabs.com
participants:
  - name: Nano Schmidt
    email: nano@usepylon.com
    affiliation: Pylon
  - name: Yousef Hamade
    email: yousef@growthxlabs.com
    affiliation: GrowthX (Cybersecurity & IT)
fathom_recording_id: 114035401
fathom_url: https://fathom.video/calls/530257344
share_url: https://fathom.video/share/-2iq1NvU8xkzFikF6J-8asds-wwWqK_w
source: fathom
enriched_on: 2026-02-28 14:32 UTC
</metadata>

---

## Summary

Yousef from GrowthX's IT team asked Nano from Pylon whether Pylon can serve as a bridge for Teams-to-Slack federation with external partners. Nano clarified that Pylon is designed for internal channel consolidation across platforms, not external federation, and requires admin access to connect Teams accounts—a blocker for GrowthX's use case. Nano agreed to confirm the technical limitation with Pylon's product team.

---

## Context

GrowthX operates as a Slack-native organization but works with enterprise customers whose security policies mandate Microsoft Teams. Previously, several GrowthX colleagues (Leah, Andy, and William) evaluated Pylon in early December for a support platform use case, ultimately disqualifying it in favor of Intercom. This meeting is a follow-up with Yousef Hamade from GrowthX's Cybersecurity & IT team to explore whether Pylon could solve a different problem: enabling seamless cross-platform collaboration with external Teams-based customers without requiring either party to adopt the other's platform.

---

## Relevance

**Product-Market Fit**
- Pylon's core value proposition (internal consolidation of multi-platform conversations) doesn't match GrowthX's external federation need.
- The technical architecture (requiring admin access to connect Teams) creates a hard blocker for the intended use case.

**Competitive Context**
- GrowthX has already selected Intercom for support platforms.
- GrowthX is also evaluating conclude.io for similar federation or support workflows.

**Feedback Value**
- Nano is seeking feedback on why GrowthX chose Intercom over Pylon to inform product strategy and positioning.

---

## Overview

- **Mismatched Needs:** Growthx requires a Slack-Teams federation broker for external partners; Pylon is an internal tool for consolidating channels within a single organization.
- **Technical Blocker:** Pylon requires direct admin access to connect a Teams account, which is impossible for external partners.
- **Prior Disqualification:** Growthx previously disqualified Pylon for a support platform use case, selecting Intercom instead.
- **Action:** Nano will confirm the technical blocker and seek feedback on why Growthx chose Intercom, which helps Pylon's product evolution.

---

## Key Topics

### Growthx's Use Case: External Federation

  - **Goal:** Bridge communication with external partners whose security policies mandate Microsoft Teams.
  - **Requirement:** A federation broker to enable collaboration via shared channels/DMs without either party adopting the other's platform.
  - **Context:** This is a separate need from a support platform, for which Growthx selected Intercom.

### Pylon's Capability: Internal Consolidation

  - **Primary Value:** Consolidate internal conversations from multiple platforms (Slack, Teams, email, WhatsApp) into one dashboard.
  - **Technical Requirement:** Requires direct admin access to connect a Teams account.
  - **Limitation:** This requirement makes it unsuitable for external federation, as Growthx cannot get admin access to a partner's Teams instance.

### Prior Engagement & Feedback

  - **History:** Growthx colleagues (Leah, Andy, William) demoed Pylon in early December for a support platform use case.
  - **Outcome:** Growthx disqualified Pylon and selected Intercom.
  - **Pylon's Interest:** Nano requested feedback on the decision to inform product evolution.
  - **Competitor:** Growthx is also evaluating `conclude.io`.

---

## Action Items

**Nano Schmidt (Pylon)**
- Confirm with product team whether Teams-to-Slack federation with external Teams organizations is technically possible; provide update to Yousef
- Seek feedback from Yousef on why GrowthX selected Intercom over Pylon to inform product evolution

---

## Transcript

**Nano Schmidt:** So actually, I wanted to let you know that I had spoken with some of your colleagues earlier, I want to say like a month and a half ago, in December, early December.

**Yousef Hamade:** Okay. Who did you talk to?

**Nano Schmidt:** Pretty sure one of the folks was Leah, and then Andy, Bailey, and William Myers.

**Yousef Hamade:** Gotcha. Okay, so I didn't realize that Andy had reached out to you guys on this as well. And I can just give you some background on my side. So I am on our cybersecurity and IT team. And so folks like Andy and company would normally reach out to me for these types of things for me to handle. But it's completely possible they reached out directly as well.

**Yousef Hamade:** But essentially, what we're trying to do is some of our customers are Teams shops, and we are a Slack shop. And for whatever reasons, from a policy perspective, they can't use Slack, right? Their security policies say, hey, look, Teams is our standard. Communications platform, Slack is ours, and that makes it difficult.

**Yousef Hamade:** Now, sometimes we've been able to work around that by just setting up guests in our Slack. But we've had various degrees of success. Ideally, we'd like a way to invite these external organizations to collaborate through a shared Slack channel or shared DM infrastructure. We don't want to set up Teams on our side. Ideally, they don't want to set up Slack on their side. But can you guys act as that bridge in between?

**Yousef Hamade:** And so if this is the same use case that Leah and Andy had reached out to you for, my apologies for running this by you again. But hopefully that scenario makes sense.

**Nano Schmidt:** Yeah, so in all honesty, I think they actually kind of disqualified Pylon, which is what I was going to talk about today. I asked for feedback, and they hadn't given it to me yet, so maybe you can mention that.

**Nano Schmidt:** But in terms of answering your question, you can act as the bridge between Slack and Teams. You can set that up to connect the two or create a channel, and if there's someone messaging from Teams, it would go to your Slack channel or your Pylon dashboard, and then you can respond from either end. It would, of course, relate back to your Teams message for the customer.

**Yousef Hamade:** Okay, and since we don't control the Teams organization that we're linking to, how do they link to Pylon on their side?

**Nano Schmidt:** Yeah, so that might be an issue there. Because you would need to connect a Teams account to Pylon. I believe you need to have admin access to actually have anything in there.

**Yousef Hamade:** So that sounds like it's more for like, you know, if you just went through an M&A and half the users are in Teams and half the users are on Slack, and you own both sides of that.

**Nano Schmidt:** Yeah, it might not be the greatest fit. It's more to just consolidate all these channels. So if you were working out of Teams, but then you're also working out of Slack and email and WhatsApp and whatever else. And you're like, why can't this just be on one platform? That's the primary value add.

**Yousef Hamade:** Yeah, that's not really what we're looking for here. For us, it's more along the lines of Slack Connect where you can collaborate with different organizations. I know Teams has a similar sort of federation model. We're more looking for a service that would allow Teams-to-Slack federation for outside entities.

**Nano Schmidt:** Yeah, I mean, it tells me maybe not. I don't have a definitive answer for you right now, but I'll have to figure that out for you. But yeah, I'd say, is it like you need a support or success platform?

**Nano Schmidt:** She did tell me they were going with another competitor and disqualified us. But I did want to know why.

**Yousef Hamade:** Yeah, so that's a different thing. I'm not actually sure why we chose Intercom instead of something else from a support perspective. But ultimately, I don't need a support platform. I literally just need a Slack-to-Teams federation broker.

**Nano Schmidt:** There's nothing out there?

**Yousef Hamade:** I think there would be something out there. I reached out to you guys and someone else. There's Plane, which is another help desk or ticketing tool. Their integrations with Slack are actually better than Intercom's in my opinion. Zendesk is a huge company, but they didn't offer a solution for Slack communication. That's why I'm curious what specifically Intercom offered more than Pylon.

**Nano Schmidt:** Right, that's helpful context for us.

**Yousef Hamade:** Yeah, so I'm not really privy as to why we selected Intercom versus another. I do see that we did do a demo with you guys back in early December from a support perspective though.

**Nano Schmidt:** That's okay.

**Yousef Hamade:** So it sounds like your connector is really targeted at integration within your ticketing platform and not really targeted at the use case we're looking for.

**Nano Schmidt:** No, yeah. The fundamental part of Pylon is that you need to have these conversations within some sort of shared channel, whether it's Slack or Teams. That's what we're built around.

**Yousef Hamade:** Yeah, that's it. Well, it looks like we were able to work through this pretty quickly.

**Nano Schmidt:** I mean, maybe I don't think the answer is going to change, but I'll ask and try to see if it's possible. But I believe not, especially if you're not connecting to Microsoft Teams and there's no way. If for some reason you do get information and hear why for Intercom, I would love to know the feedback just because it helps us evolve as a company.

**Yousef Hamade:** All right, sounds good. I think the other folks we're talking to is conclude.io.

**Nano Schmidt:** I haven't heard of conclude. It's like Microsoft Teams streaming and cross-company federation. Sounds like it might be something you'd explore.

**Yousef Hamade:** Yeah.

**Nano Schmidt:** Well, if anything changes, let me know.

**Yousef Hamade:** All right.

**Nano Schmidt:** Thanks for your time.
