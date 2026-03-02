# Hubspot Review

<metadata>
date: 2025-12-12
time: 18:00 UTC
duration: 32 minutes
organizer: andi@growthx.ai
participants: Andi Bailey, Kyle Doherty, Leah Myers
fathom_recording_id: 108435957
fathom_url: https://fathom.video/calls/495532405
share_url: https://fathom.video/share/p5gNA5ot_eEoY7fyBCi4yEco-P9sBT33
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Kyle walked Andi and Leah through GrowthX's HubSpot renewal automation: deals with "Growth Execution" SOWs auto-create renewal deals on "Closed Won," then auto-move to "Renewal Prep" at 90 days out with Slack notifications, followed by manual stage progression (Scope & Options → Proposal → Closed Won). Key issue: Slack alerts were failing because renewal deals had external channel references instead of internal channels (INT-customer-name format), which Kyle fixed. GrowthX also needs to clean up historical deals missing required fields like Contract End Date to ensure future renewals generate correctly.

---

## Context

GrowthX's operations team (Andi Bailey, Kyle Doherty, and Leah Myers) met to review HubSpot's renewal pipeline configuration. Kyle, who built the system, walked through the automation logic with Andi and Leah, who manage renewals operationally. Leah recently joined the team and needed to understand the process and start auditing historical deals. The meeting was triggered by outstanding issues: Slack notifications weren't firing for renewal milestones (90, 60, and 30 days out), and several renewal deals lacked required contract data, causing auto-generation failures.

---

## Relevance

- **To GrowthX Delivery:** Renewal management automation is foundational to predictable revenue tracking. Process requires discipline: Andi will document the renewal process in Notion, Kyle will verify required fields and fix broken associations, and Leah will audit all historical deals to backfill missing contract dates (start, end, term). Slack notifications are now tied to correct internal channels to trigger CSM engagement at 90, 60, and 30 days.

- **To GrowthX Business Development:** Renewal deals sit in pipeline for 12+ months; manual stage movement (after the initial 90-day automation) prevents false metrics on deals that haven't actually started conversations yet. Risk scoring is manual but dashboard-visible, allowing quick triage of at-risk renewals by quarter. Data Grid renewal failed to auto-create after July deal closed in November — Kyle will investigate to prevent future data loss.

- **To GrowthX Operations:** Line item pricing logic is complex due to mismatch between GrowthX's billing cycles and actual contract terms; Kyle offered a Loom walkthrough to clarify. HubSpot association labels ("Renews" vs. "Renewed By") are incorrectly set; Kyle will fix. The "30-day renewals" filtered view is broken and needs repair.

---

## Overview

- **Automated Renewal Creation:** HubSpot auto-creates a renewal deal for "Growth Execution" SOWs upon "Closed Won," tracking the new contract and serving as the opportunity for the next renewal.
- **90-Day Activation:** Deals auto-move to "Renewal Prep" 90 days out, triggering Slack alerts. Subsequent stage moves are manual to ensure data accuracy.
- **Data Integrity Fix:** Slack alerts failed because the `Slack channel internal` property was set to an external channel. The fix is to update this property to an internal channel (e.g., `INT-customer-name`).
- **Data Cleanup Required:** Leah will audit and update historical deals missing required fields (e.g., `Contract End Date`) to ensure future renewal deals are created correctly.

---

## Key Topics

### The Renewal Process: Automation & Pipeline

  - **Goal:** Automate renewal tracking and opportunity creation.
  - **Trigger:** "Closed Won" deals with an SOW of "Growth Execution."
      - *Rationale:* Excludes one-off "Strategy Sprints" that don't renew.
  - **Automation:**
      - **Creation:** A new renewal deal is auto-created.
      - **Naming:** `[Original Deal Name] - Renewal #[Number]`.
      - **Data Copy:** Key info from the original deal is copied (e.g., `Prior Amount`, `Prior ARR`) to provide context for the renewal.
      - **Activation:** At 90 days out, the deal auto-moves to "Renewal Prep," triggering a Slack alert.
  - **Pipeline Stages:**
      - **Renewal Prep:** 90+ days out (auto-triggered).
      - **Scope & Options:** 60–31 days out (manual).
      - **Proposal:** \<30 days out (manual).
      - **Closed Won:** Creates the *next* renewal deal.
      - **Closed Lost:** Requires a reason.
  - **Manual Stage Movement:** Prevents inaccurate data. A deal 12 days out might still be in "Renewal Prep," reflecting its true status.

### Data Integrity & Reporting

  - **Required Fields:** Several fields are required to close a deal, ensuring data quality for automations.
      - `Deal Owner`, `Amount`, `Contract Start Date`, `Contract End Date`, `Term`, `Term (number of months)`, `SOW`.
  - **Historical Data Cleanup:**
      - **Problem:** Older deals lack required fields, causing issues like the "Lovable" renewal missing a `Contract End Date`.
      - **Solution:** Leah will audit and update these deals. Missing info can be found on the associated original deal or in the contract.
  - **Slack Notification Fix:**
      - **Problem:** Alerts for the 90/60/30-day milestones were not firing.
      - **Cause:** The `Slack channel internal` property was set to an external channel.
      - **Fix:** Update the property to an internal channel (e.g., `INT-customer-name`). The system is hard-coded to ignore external channels as a safeguard.
  - **Pipeline Visualization:**
      - **Deal Tags:** Auto-applied at 90, 60, 30 days out, and "Past Due" for at-a-glance status.
      - **Filtered Views:** Pre-built views (e.g., "30-day renewals") to focus on specific cohorts.
      - **Renewal Dashboard:** Provides a high-level summary of upcoming renewals by quarter, stage, and risk.

### Known Issues & Future Topics

  - **Data Grid Renewal Failure:** A renewal deal was not auto-created after the July deal was "Closed Won" in November. Kyle will investigate the workflow failure.
  - **Line Item Pricing:** Andi noted the logic is complex. Kyle explained it's due to a mismatch between GrowthX's billing cycles and the actual contract term. A follow-up call is available if needed.

---

## Action Items

**Andi Bailey (GrowthX)**
- Copy Kyle's renewals docs to GrowthX Notion; update stage activities/notes

**Kyle Doherty (GrowthX)**
- Verify required fields (incl. Close Lost Reason) and calculated close date; update docs
- Fix HubSpot association labels (Renews vs Renewed By)
- Fix 30-day renewals filtered view in HubSpot
- Investigate Data Grid renewal auto-creation failure; report findings to Andi
- Send line-item pricing Loom to Leah and Andi

**Leah Myers (GrowthX)**
- Clean up upcoming renewals in HubSpot per audit; backfill contract start/end/term from contracts

---

## Transcript
**Kyle Doherty:** What is that nearly in Wisconsin?

**Leah Myers:** It's actually closer to like Minneapolis, St.

**Kyle Doherty:** Paul, but just on the Wisconsin side of the border from Minnesota.

**Kyle Doherty:** Hey, Andi.

**Andi Bailey:** How's it going?

**Kyle Doherty:** Good. So just to confirm, let me make sure we're using our time the best we can.

**Kyle Doherty:** The point of this is you wanted to go over like the docs again, and then like how this all, how it all works.

**Andi Bailey:** Yeah, I think especially like renewals management helped Leah get up to speed on all that stuff.

**Andi Bailey:** And yeah, I think since the last time.

**Andi Bailey:** Yeah.

**Andi Bailey:** I talked, there are some outstanding pieces on the Slack automations, and I, like, saw that thread, but I'm not totally up to date on, like, what the decision was.

**Andi Bailey:** And then the, like, just required fields for closing.

**Andi Bailey:** And then I also want to, like, dive in on, I know you explained the line item pricing, but it's still very weird to me.

**Kyle Doherty:** Yeah, line item is weird.

**Andi Bailey:** And then the, like, the automating of when you close wanted a renewal deal, that it creates another one.

**Andi Bailey:** Like, I just don't, like, yeah, just show me what, where.

**Kyle Doherty:** Let me go over the documentation, and we'll just go through it.

**Kyle Doherty:** So first, let me give you the link. I think this lives in a doc that Bridget and I had, but if there's documentation that you have for the renewals process, I think we should put it there.

**Kyle Doherty:** Because ultimately you should manage this going forward, right?

**Kyle Doherty:** So this is in like, this is like this renewal work doc that Bridget created.

**Kyle Doherty:** And then there's the HubSpot renewal documentation.

**Kyle Doherty:** So this is what I'm saying.

**Kyle Doherty:** Like this whole thing should probably live wherever you want the renewal documentation that you're in charge of.

**Kyle Doherty:** You can just copy this and put it there.

**Kyle Doherty:** Yeah.

**Andi Bailey:** I mean, we can start with that because we have just renewals data, but we don't have like a process documented yet.

**Kyle Doherty:** So yeah.

**Kyle Doherty:** Okay.

**Kyle Doherty:** Well, this is here.

**Kyle Doherty:** You clear.

**Kyle Doherty:** You have that.

**Kyle Doherty:** Well,

**Kyle Doherty:** The notion, so you'll have access to this, and you're both able to access this, right?

**Kyle Doherty:** Okay, cool.

**Kyle Doherty:** Yeah, so this just, this explains everything.

**Kyle Doherty:** It's pretty comprehensive, but, so there, let's start with the automatic renewal deal creation.

**Kyle Doherty:** So, well, for me, do I have, I don't, let me get HubSpot open, too, so we can kind of go back and forth, and so you can see, like, the context of what we're talking about, instead of just a doc.

**Kyle Doherty:** All right, so are you both familiar with HubSpot? You know it has deals and different pipelines?

**Kyle Doherty:** Okay, cool. So we have new business, which is obviously new business. There are different types basically by the SOW — you have strategy sprints and growth ones, and I forget exactly what they're called, but the growth ones are what we focus on.

**Kyle Doherty:** And we really, for renewals, we only care about the growth ones.

**Kyle Doherty:** So if those get to closed one, then what is automatically happening is we're creating a renewal deal for that.

**Kyle Doherty:** And the point of the renewal deal is because now you have like an active contract for that company, right?

**Kyle Doherty:** So let's say RAMP, we have a contract for RAMP, we closed them, let's say today.

**Kyle Doherty:** So then next year, we're going need to renew them on December 12th, 2026, right?

**Kyle Doherty:** And so this new renewal deal, it's in charge of like keeping track of that, like the contract information of like when it renews.

**Kyle Doherty:** And it also is acting as the deal, the opportunity of like closing that renewal business.

**Kyle Doherty:** So like getting a new contract, the second contract.

**Kyle Doherty:** So I'll just

**Kyle Doherty:** That's the point of that, and so that's what happens for new deals, but then if you renew them, so let's say December 12th, 2026, we renew RAMP, so we close win the renewal deal.

**Kyle Doherty:** So if we go to the renewal pipeline, and let's say we had a renewal deal for RAMP, and then we get to the 90-day mark, so we're doing renewal prep, then we scope, then we give them a proposal, and we close win it.

**Kyle Doherty:** Now we need another renewal deal, right?

**Kyle Doherty:** So it's like renewal deal two, to keep track of that new contract, and that we need to renew them.

**Kyle Doherty:** So that's high level what's going on there, but let me go back to the docs, and stop me if any of this doesn't make sense.

**Leah Myers:** I have a question about the nomenclature, so that old designation, is that going to carry over with the auto-creation of new growth execution renewals, like growth execution number two, would that be the name?

**Leah Myers:** It's a pedantic thing, but I'm curious.

**Kyle Doherty:** Yeah, no, no, that's a good question.

**Kyle Doherty:** Yeah, so whatever, like, the original is, it's just taking the original deal name, and then it's putting renewal number one.

**Kyle Doherty:** Or if it's the second time we're renewing them, it's renewal number two.

**Kyle Doherty:** If it's the third, renewal number three.

**Kyle Doherty:** So it just says number, because sometimes deals are on a three, like, contracts are three months, sometimes they're six, sometimes a year, could be 24, whatever.

**Leah Myers:** Yep, yep.

**Kyle Doherty:** Yeah, and then also that way this future proves this.

**Kyle Doherty:** if we ever, like, and even you can see some of these before they standardize it to growth, the growth ones, you have all these content services and different names of the services being provided instead of growth execution.

**Kyle Doherty:** So there could be in the future where it's, like, growth execution, XYZ, like, maybe there's a different type of growth execution.

**Kyle Doherty:** So this will just handle it.

**Leah Myers:** Okay, so it'll just be the customer name.

**Leah Myers:** And then renewal.

**Kyle Doherty:** renewal.

**Kyle Doherty:** Perfect.

**Kyle Doherty:** And so when it's creating this, these are just sitting here because you can see this doesn't renew for 12.1 months.

**Kyle Doherty:** So when it's copying that data over to this new renewal deal, it's just taking a snapshot of the deal that closed one and pre-populating this deal to be a starting point for where, because the happy path would, or not the happy path, but one happy path would be, we just get them to renew the same thing they did.

**Kyle Doherty:** Like the ultimate happy path, obviously, is you expand them, right?

**Kyle Doherty:** Like you sell them more.

**Kyle Doherty:** But the point is like, let's just start with what they already bought and try to get them to buy that.

**Kyle Doherty:** Now, this might change.

**Kyle Doherty:** And so you would need to update this deal as needed once you get into probably like scope and options.

**Kyle Doherty:** But that's fine.

**Kyle Doherty:** So sort of call that out.

**Kyle Doherty:** So this is our like spells out all those details.

**Kyle Doherty:** So like I said, we only are doing this.

**Kyle Doherty:** For where the SOW equals growth execution, that is because you also have the strategy sprints, and those aren't actually renewing because they have to then convert to the growth execution before we would worry about renewing them.

**Kyle Doherty:** So that's what this is noting here.

**Kyle Doherty:** Then this notes, like what I was saying, so you are getting some contextual data about the deal that is closed one.

**Kyle Doherty:** So you have like prior amount, prior AR, prior MRR, those are locked in on the new renewal deal, just so you have that context.

**Kyle Doherty:** It also gives you like prior deal dates, like the renewal date, all that.

**Kyle Doherty:** So like I said, that's storing the information about like that new contract that got signed for that deal, that closed one.

**Kyle Doherty:** So this tries to map it out for you, so it's a bit more visual.

**Kyle Doherty:** So you have like prior deal information, which is getting copied over from, and this obviously isn't always a new business deal.

**Kyle Doherty:** I'm just using that as an example.

**Kyle Doherty:** It could be a renewal deal, technically.

**Kyle Doherty:** Yeah.

**Kyle Doherty:** But it's just copying over like what happened when you closed, what was the amount, what was the ARR, what was the contract end date, what's the renewal date.

**Kyle Doherty:** And then you also have just the normal deal information for that renewal deal, which is just the, it's basically just this up here.

**Kyle Doherty:** And like all, just the normal deal information you would have about any deal, right?

**Kyle Doherty:** Like what's the amount, what's the contract start date, the term deal and our company contacts, SoW.

**Kyle Doherty:** So really the only difference is that renewal deals are keeping track of like the contextual information from the deal that they are renewing, the deal that closed one that they are going to renew.

**Kyle Doherty:** And the reason they do that is so that they can sit in here and we can automatically move them over to renewal prep when it's 90 days out.

**Kyle Doherty:** And just so we can quickly see like, hey, what deals are supposed to renew and we just have them all here.

**Kyle Doherty:** So I already mentioned this, there's like the 90-day renewal activation, just meaning like at 90 days, that's when stuff, at least currently in the process, Andi, you could change this, this might change to like, I don't know, you might start doing check-ins earlier, and maybe like there's new stages that you need.

**Kyle Doherty:** But for now, it's at 90 days, this automatically moves, gets moved over to renewal prep, and the Slack notification gets fired.

**Kyle Doherty:** Now that you're asking, Andi, like what was going on with the Slack stuff, so I'll go over that real quick.

**Kyle Doherty:** So in this deal, and so when you're looking at a deal, like you have all this information on them, but you can also just go view all properties, and you can see everything.

**Kyle Doherty:** And so there's a Slack channel internal, and it's set to whatever the Slack channel is.

**Kyle Doherty:** The issue that was happening is all these were set to external, and the Zap was

**Kyle Doherty:** It won't send to, if it's, if it doesn't say INT dash, it won't send because that way it's safeguarding against someone accidentally puts an external one in here and we like send these notifications to an external one.

**Kyle Doherty:** Okay, so that's that.

**Kyle Doherty:** So, I'm actually going to delete this, it does not create a task.

**Kyle Doherty:** We were initially going to use Tasks, but you guys don't use HubSpot Tasks, so just send us a Slack notification.

**Kyle Doherty:** And at that point, like, the deal owner or Andy, whoever, whoever should be taking over that process would take that over.

**Kyle Doherty:** So, I guess that's a good stopping point.

**Kyle Doherty:** Like, is this accurate or should we update this or what?

**Andi Bailey:** I mean, it's fine for now since not everybody's in HubSpot, but at least then the owner, the, like, deal owner knows that they're, that they're on the clock and that they can.

**Andi Bailey:** And they should start their external phasing activities.

**Kyle Doherty:** Right.

**Kyle Doherty:** Cool.

**Kyle Doherty:** And then this is just trying to make it ultra clear.

**Kyle Doherty:** Wow, that's not helpful.

**Kyle Doherty:** Make it ultra clear that you have a new business.

**Kyle Doherty:** When it's closed one, it creates a new renewal deal.

**Kyle Doherty:** Then nine days out, it moves it to renewal prep.

**Kyle Doherty:** The CSM or whoever works the deal, if that's closed one, another renewal deal is created.

**Kyle Doherty:** And it could go on forever as long as we continue renewing the customer.

**Kyle Doherty:** Cool.

**Kyle Doherty:** So this is just documents, the renewal pipeline.

**Kyle Doherty:** So you have the stages, like you already saw that.

**Kyle Doherty:** But so it just says what the stage is, the description.

**Kyle Doherty:** These are just like, these are not based on anything.

**Kyle Doherty:** It's just like, I set these to this.

**Kyle Doherty:** As time goes on, you guys can change these in HubSpot so that you have like more accurate.

**Kyle Doherty:** Like, oh, we know that as soon as we get someone to scope and options, we have like a 70% close rate.

**Kyle Doherty:** And maybe it's like 80 or 90.

**Kyle Doherty:** You can update that.

**Kyle Doherty:** Yeah, and then the timing.

**Kyle Doherty:** So, like I said, renewal prep, it automatically moves it 90 days out.

**Kyle Doherty:** After that, you have to manually move them.

**Kyle Doherty:** But the idea here is scope and options would be between days 60 and 31.

**Kyle Doherty:** And proposal would be within, when you're 30 days or less, like you should be in the proposal phase.

**Kyle Doherty:** Again, these are what I just set with Bridget.

**Kyle Doherty:** She liked them, but Andi like obviously changed them as you see fit.

**Kyle Doherty:** These ones, I'm actually going to delete this because these are just placeholders.

**Kyle Doherty:** And I tried to get Bridget to update them or like somebody, but no one did.

**Kyle Doherty:** So this is just like whatever the key activities are for the stage.

**Kyle Doherty:** Ideally, they're documented so everyone knows what they should be doing.

**Kyle Doherty:** And these are just additional notes, like triggered by the 90 day automation.

**Kyle Doherty:** Again, these are just like things I put in here to be helpful, try to be helpful, but you guys should update these as you see, if you're like, this doesn't matter, get rid of it.

**Leah Myers:** For the closed lost, is lost reason required, like coded into the renewal program, and you can't close lost it without that reason?

**Kyle Doherty:** Yes, I'll double check that, but yes.

**Kyle Doherty:** And that's for any deal, like if it's closed lost, you have to put in a reason.

**Leah Myers:** Great, I'll bet.

**Kyle Doherty:** Yep.

**Kyle Doherty:** This just reiterates the rules about that it will only move it automatically at 90 days, and then after that it needs to be manual.

**Kyle Doherty:** The reason for that is because a lot of companies will do it where it just automatically moves based on the days out.

**Kyle Doherty:** But you could be 12 days out and not even talk to them yet.

**Kyle Doherty:** So.

**Kyle Doherty:** But then you're getting really bad data on like what's actually happening.

**Kyle Doherty:** So yeah, that's why I would do that.

**Kyle Doherty:** These are like the required fields that we need.

**Kyle Doherty:** like, and generally you're always going to have this on a new deal or a renewal deal, deal on our amount, contract, start date, contract, end date, terms, the term number of months, SoW, like these are already required.

**Kyle Doherty:** So it's like, you have to have these, but it's just calling that out.

**Leah Myers:** So question — I've seen some renewals and opportunities without the calculated close date. Is there a date this requirement was deployed, like as a sanity check? Anything that might have happened before that date, we might have to move.

**Kyle Doherty:** Yeah, it was. I forget when it was, but back around October, September-October.

**Kyle Doherty:** I can go double check these to make sure they're required, but all new deals should have all this.

**Andi Bailey:** Yeah, but Leah, so to your point, all the upcoming renewals probably don't have all this.

**Kyle Doherty:** Most of them, yeah. We were trying to get all that in, and it was just such a slog that we finally had to create them and fill it in after.

**Leah Myers:** That sounds good. Yeah, I have a list from the audits I've been doing this week, so I'm happy to go in and get stuff cleaned up.

**Kyle Doherty:** You should be able to, because you have the original deal associated here. It has a label that it's renewed by this one.

**Kyle Doherty:** So you can click into the old one, and then any information you need, whether it's like, so you have like all the contract information here.

**Leah Myers:** Here's one, like a straight up example of lovable that doesn't have a contract end date, and then it renews a renewal.

**Andi Bailey:** So, lovable in here, the renewal.

**Kyle Doherty:** This one?

**Leah Myers:** Yep.

**Kyle Doherty:** And this was the, oh wait, no.

**Kyle Doherty:** So this is the original one?

**Leah Myers:** Yeah.

**Leah Myers:** Yeah.

**Leah Myers:** So for this one.

**Kyle Doherty:** So this is the original that got renewed by this one. Yeah, actually, this association label is weird. I'm going to check how that's getting set — this really should say "Renews," like this one renews that one. So we have the contract end date. We're probably missing terms. When we created the renewal, it didn't have terms, so the terms didn't get copied over. Yeah, this is just missing everything.

**Kyle Doherty:** Yeah this is just missing kind of everything.

**Kyle Doherty:** So what we would have to look at the contract.

**Leah Myers:** Yeah.

**Kyle Doherty:** Is that what you're trying to solve for?

**Leah Myers:** Yeah, just understanding what should be updated — I'm happy to chase down all the things. My understanding is we just go in, look at the contract, and update as required. HubSpot is set up so that when we get to renewal number two, it will be copy-paste of renewal number one if we have a nice clean one.

**Kyle Doherty:** Yeah, exactly. So if we have contract start date, contract end date, term, and all this, then it'll be good.

**Leah Myers:** Great cool.

**Kyle Doherty:** Oh, good.

**Kyle Doherty:** Cool.

**Kyle Doherty:** This gets into how to use the renewals pipeline.

**Kyle Doherty:** We don't move deals automatically by days, except at 90 days — then you have to move it yourself. But it's ideal to have the context of how many days till they renew, regardless of what stage they're in. So we add deal tags like "90" and "30" so you can quickly see, "Hey, this 30-day deal should be in proposals — what's wrong with this one?" It's faster than squinting at dates to figure out where things should be.

**Kyle Doherty:** So there's 90, 60, 30, and past due tags. And there are also filtered views — so if you only want to look at 30-day renewals, there's a view for that.

**Leah Myers:** You've got lovable in the search bar.

**Kyle Doherty:** Oh, thank you. I might have to look into that. But ideally, the filtered view only shows 30-day, 60-day, or 90-day deals so you can get rid of the clutter.

**Kyle Doherty:** To access the views, they show up for me because I've already added them. Anytime you want a new view, you can add it by looking for the one you want — for you it would be under "created by others" instead of "created by me." You'd find it and add it.

**Kyle Doherty:** There's also a renewal dashboard. It breaks down renewals by 90 days out, and by risk. The risk property — yellow, green — you have to set manually. It auto-sets to green when created, and shows up on the card. You can update it in table view by adding it as a column. You also see upcoming renewals for 180 days — what quarter, how many coming up, by stage, and by risk. It's a quick snapshot if you don't want to sit in the pipeline view.

**Leah Myers:** Is the Slack notification just when the renewal opportunity is created, or does it ping the internal Slack channel at the milestone dates?

**Kyle Doherty:** When it hits 90 days out, the deal gets moved and a Zap fires a message saying "this renews in 90 days." Same thing happens at 60 and 30 days. This one is at 88 days — when it hit 90, it should have moved and sent a notification, but it probably had the external Slack channel set, so it didn't send. Now that it's internal, it will.

**Leah Myers:** Okay.

**Kyle Doherty:** And only if they're open, That's the only, like, issue is that if it doesn't have the internal Slack channel set, when it hits those milestones, it won't send.

**Leah Myers:** Let's say we have a unicorn customer that loves us so much that they decide.

**Leah Myers:** Okay.

**Leah Myers:** Okay.

**Leah Myers:** All right.

**Leah Myers:** Thank

**Leah Myers:** To, you know, close out their renewal, they're going to sign with us at, like, day 88.

**Leah Myers:** Like, if that's an opportunity that's closed one, are those Zapps still going to fire?

**Kyle Doherty:** So, sorry, they close at 88.

**Kyle Doherty:** You close one of them at 88?

**Kyle Doherty:** Yeah.

**Leah Myers:** So the renewal deal gets closed, and it's...

**Leah Myers:** Like, super early.

**Kyle Doherty:** Yeah, it's not going to fire, because it has to be an open deal.

**Leah Myers:** Yep.

**Leah Myers:** Sanity check.

**Kyle Doherty:** Thanks.

**Andi Bailey:** Can I ask you about the Data Grid one? I don't see a renewal for them. We had a deal from July — they renewed then on six-month terms, but they signed again in December on a shorter cycle. That renewal didn't come through after the deal got closed.

**Kyle Doherty:** When did that close?

**Andi Bailey:** November.

**Kyle Doherty:** Yeah, that's strange. The workflow should have picked it up as soon as it got set to closed one. Let me add that to my to-dos.

**Kyle Doherty:** There are other examples to look into. This gets into technical details — all the properties are documented here with what shows on the deal card view and the workflows that make it all work. You're welcome to read through that. We're at time, so I have to jump. Andi, I think you had a question about line items.

**Andi Bailey:** I know how to do it, but it really doesn't make sense. I guess it doesn't matter as long as the amount is the same.

**Kyle Doherty:** Even when I've explained it in the Loom, it doesn't make sense. It ultimately comes down to the fact that we bill differently than the actual contract term. That's why the logic is complex. We could set up another call if you want.

**Andi Bailey:** No, it's fine. I think we'll sort it out.

**Kyle Doherty:** Okay. I need to look into that Data Grid renewal issue. Are there any other things you specifically want me to look into?

**Leah Myers:** Not at this time. I'm pretty self-sufficient. I'll take a deep dive into the documentation and review any Looms you send over, and then follow up if there's anything else.

**Kyle Doherty:** Sounds good.

**Leah Myers:** Thank you so much.

**Andi Bailey:** Yeah, thank you.

**Kyle Doherty:** Thanks, guys. Bye.
