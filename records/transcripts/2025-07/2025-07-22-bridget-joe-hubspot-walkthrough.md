# Bridget / Joe - Hubspot Walkthrough

<metadata>
date: 2025-07-22
time: 17:01 UTC
duration: 60 minutes
organizer: Kyle Gaudreau
participants: Joe Lehr, Bridget McGillivray, Kyle Gaudreau
fathom_recording_id: 75718141
fathom_url: https://fathom.video/calls/355518023
share_url: https://fathom.video/share/Kxg5nEnDSWcGs3sxDgGV519q2-9r5MeT
source: fathom
enriched_on: 2026-03-03 14:30 UTC
</metadata>

---

## Summary

Joe led a detailed HubSpot configuration walkthrough for Bridget and Kyle, covering the Monday go-live when GrowthX stops using Adio. Key topics included deal structure setup (line items and associations for sprint + growth deals), field requirements and validation rules, data migration strategy, and reporting tools like Coefficient for Google Sheets integration. Joe committed to creating video enablement content by Monday and scheduling a 1-hour onboarding with Tyler, while the team finalized required fields, custom views, and Slack/Zapier workflow migrations.

---

## Context

GrowthX is executing a critical CRM migration from Adio to HubSpot, with a Monday go-live deadline. Joe Lehr is leading technical configuration, while Bridget McGillivray (GrowthX leadership/operations) and Kyle Gaudreau (GrowthX operations/sales) are key stakeholders. The team's core challenge is managing a complex deal structure: GrowthX sells "sprint" (3-month initial engagements) and "growth" (9-month follow-ups) deals, requiring sophisticated line items, deal associations, and automation to track relationships between linked deals. Prior to Monday, all team members must stop updating Adio and rely solely on HubSpot. Tyler is joining the team Monday, requiring both immediate enablement and ongoing support as a new HubSpot user.

---

## Relevance

To GrowthX Delivery:
- Deal structure (sprint + growth) requires HubSpot line items and associations; this pattern likely applies to all new GrowthX engagements. Joe's validation rule approach for conditional field requirements will set the baseline for quality control.
- Reporting challenge: Currently unclear how many active customers GrowthX has — Coefficient tool enables automated, accurate customer status tracking via Google Sheets. This directly impacts renewal forecasting and churn visibility.
- Required fields strategy (end date, start date, contract attachment, billing contact, etc.) will drive data entry discipline; custom views and stage-based field requirements will be rolling out post-launch.

To GrowthX Business Development:
- Monday go-live removes data sync friction between Adio and HubSpot; confirms GrowthX is ready to onboard Tyler and scale account management.
- Bridget flagged time pressure on Joe; leadership aware of competing demands and has offered to distribute load (Jason's requests can be delegated).
- Renewal automation and churn tracking via Coefficient positions GrowthX to close renewals faster and forecast ARR more accurately.

To GrowthX Operations:
- Chrome extension, Gmail/Calendar integration, and HubSpot email sequences are now live. Kyle's onboarding walkthrough (Gmail, calendar, extension setup) becomes the template for new user enablement.
- Zapier workflow migrations (close-won, pipeline stage changes → Slack alerts) will complete by launch, reducing manual notifications.

---

## Overview

- HubSpot go-live planned for Monday; team to stop using Adio CRM on Sunday night
- Inbound lead flow, deal stages, and key fields have been implemented in HubSpot
- Line items and deal associations will be used to track complex deal structures (sprints + growth)
- Custom views and required fields will be set up to ensure data accuracy and ease of use

---

## Key Topics

### HubSpot Implementation Progress

  - Inbound lead flow has been moved from Adio to HubSpot with enhanced enrichment data
  - Deal stages have been imported, including a change from "meeting booked" to "engaged"
  - Key fields from Adio have been ported over, including SOW and contract type
  - Line items functionality will be used to track complex deal structures (e.g., 3-month sprint + 9-month growth)
  - Deal associations will be implemented to connect related deals (e.g., sprint and growth execution)

### Data Migration and Cleanup

  - All existing growth and sprint deal types (closed-won, closed-lost, open) have been imported to HubSpot
  - Priority for further imports: active open deals and closed-won (current customers)
  - Churned customers and historical closed-lost deals are lower priority for import
  - Backfilling of deals that don't match growth/sprint style still needed

### New Processes and Features

  - Calendar and Gmail integration set up for Kyle, to be done for other team members
  - HubSpot Chrome extension to be installed for easy data entry and activity tracking
  - Custom views to be created based on Kyle's feedback for most relevant fields
  - Required fields and validation rules to be implemented for data accuracy
  - Automation for renewal deal creation to be set up

### Reporting and Data Management

  - Coefficient tool ($100/month) recommended for advanced reporting and data syncing between HubSpot and Google Sheets
  - Discussion on how to handle contract changes (e.g., early cancellations) in the CRM
  - Slack notifications for deal stage changes and closed-won deals to be implemented in HubSpot

---

## Action Items

**Joe Lehr (GrowthX)**
- Implement final data import from Adio to HubSpot on Sunday night (00:03:13)
- Schedule 1-hour onboarding block with Tyler for Monday (00:09:25)
- Create video walkthrough for HubSpot processes (line items, deal association, conditional validation rules) by Monday (00:38:34)
- Port over close-won and pipeline change Zaps from Adio to HubSpot workflows (00:52:13)

**Bridget McGillivray (GrowthX)**
- Add Joe to PandaDoc for access to sales contracts (00:06:10)
- Sign up for Coefficient tool for Google Sheets integration with HubSpot (00:27:59)

**Kyle Gaudreau (GrowthX)**
- Provide feedback on HubSpot deal record layout preferences, including desired fields to see (00:36:46)
- Stop updating Adio CRM by Sunday night; ensure all data entry completed by Saturday (00:38:59)

---

## Transcript
**Joe Lehr:** I appreciate the time today. I have so much to cover with you both. It's going to be a bit of a cluster, but it'll be good stuff.

**Joe Lehr:** Ideally, I'd like to walk you quickly through integrating your calendar and Gmail so we can start tracking data. This is a soft launch where you'll begin updating fields to see how the flow works. I'll put together a video for enablement on a few things. Bridget, I want to make sure you know how to manage properties. I built out what you shared last night because it's really relevant to this conversation, and I'd love you to have a soft launch where you provide feedback.

**Joe Lehr:** The truth is, until Bruno and Tyler are in the platform, data syncs between Adio and HubSpot will cause issues. The official launch is Monday. Is that when Tyler starts?

**Kyle Gaudreau:** Yeah, Monday.

**Joe Lehr:** Okay. I'd love to get your feedback implemented starting Friday through the weekend, and then I'll have an hour onboarding block. I know Bridget said Tyler has already used HubSpot, so there shouldn't be anything crazy. But I'd love to have that unless you want to do Tuesday instead?

**Bridget McGillivray:** No, he's already got access to some stuff.

**Joe Lehr:** Okay, cool. So I want to...

**Bridget McGillivray:** So we have about eight deals we want to add today, or at least soon. Should we be able to test and add them after this?

**Joe Lehr:** I did import and manually update all existing growth and sprint deal types. So if they're closed-won, closed-lost, or open, I've brought them into HubSpot. The issue is if someone updated something today, that's not yet reflected in HubSpot. We could try building one to show you, but I'd say stick with Adio for right now. When we officially go live Monday, no one updates Adio and I'll have everything reflected. Sunday night, I'll do one final import of all the data and objects to make sure it's one-to-one.

**Bridget McGillivray:** That's perfect.

**Bridget McGillivray:** One other question.

**Bridget McGillivray:** I see Jason's asking you to do a bunch of stuff. Do you have time for all this? I will fight to the death to make sure we do HubSpot first.

**Joe Lehr:** HubSpot is critical. I'm not going to leave without having it in the right spot. Yes, I wish I was a little further along, but this is my priority. Some of the work Jason's talking about flows into this — like leveraging Luma to push data into HubSpot. I've already built 70% of that via Zapier. I just need to finalize it. I'm not doing that piece until I finish the main piece. There's also a list I need to build for him — that's 20 minutes when I have time to allocate. We need to go live. I need to have Tyler and Bruno in the platform Monday, updating things and collecting their questions and suggestions so I can implement fixes over the next week.

**Bridget McGillivray:** We probably don't need Bruno in there anymore, right? We can remove his seat and add Tyler.

**Joe Lehr:** That's really interesting and helpful, because then Tyler doesn't need onboarding enablement like Bruno would — that saves time. With Tyler, I can really just get into the nuance. And again, I'll have the video content. I don't expect you guys or Tyler to know how to do this right off the bat, but I'll walk you through it and share the video and you'll be good to go.

**Joe Lehr:** I don't want the backfill of those deals to fall by the wayside, Bridget. We talked about having Dig and a few other folks help, but I'd love to build out at least the eight you originally shared, plus a few more myself. I showed you the CSV. The difficulty is I don't have access to the contract folder. Some of these deals, the Notion doc doesn't have the contracts for all of them, so I get a little lost.

**Kyle Gaudreau:** Yeah, especially the newer ones.

**Bridget McGillivray:** I keep them all in a private area. I can add you to PandaDoc where they all live. Let me just check if we have a shared account there. We used to have a lot of other things in PandaDoc, but it should be just sales docs now.

**Joe Lehr:** I brought over about nine or ten closed deals that are part of the sprint and growth execution contract type, and I want to backfill those myself. Do you have access to that email for PandaDoc?

**Bridget McGillivray:** That email has access to PandaDoc. Let me figure out what kind of auth it is — Google auth or password?

**Kyle Gaudreau:** I'll just send you the password in Slack.

**Joe Lehr:** One question since there's so much to cover — is Bruno still updating deals, stages, or deal fields today?

**Kyle Gaudreau:** Not starting today, no.

**Joe Lehr:** So that's really interesting. I intentionally didn't import every field because I thought some were unique to his workflow and would be noisy if he wasn't there.

**Bridget McGillivray:** Yeah, don't bring in any of those custom enrichment fields.

**Joe Lehr:** That's really helpful. Kyle, if we go live Monday, I'll have the data backfilled Sunday night. Do you think we'd be doing any additional data fill in Adio Sunday night? I don't want to miss anything.

**Kyle Gaudreau:** I can work off of that. If I need to catch up on the weekend, I'll do it Saturday. Just send me a quick note when you're jumping into it Sunday night, just in case, but it should be absolutely fine.

**Joe Lehr:** I'll probably start at 9 p.m. Eastern Sunday night. We're just getting it all there. As you'll see, a lot of this is already in place. There's a few additional columns I want to bring in.

**Joe Lehr:** I want to call out a few high-level things. I definitely want to get your calendar and Gmail synced before we end this meeting. It's not critical, but I want to get it done. I'll get an hour with Tyler on Monday. Let me walk through what's been completed. The heaviest lift has been moving the default inbound flow from Adio into HubSpot. That's been completed. When someone submits the form now, it's been enhanced — we're including more enrichment data with a personalization layer. Instead of "hi there," we say "hi [first name]" and send it with the sales team CC'd. I incorporated the logic you both shared, and in a test run with a company that raised funding, I tested with $9,000 and was still able to see the meeting calendar. That flow has been brought over.

**Joe Lehr:** I want to share the inbound topic, and then move to deals. Let me get my screen up. I brought over your field for the opportunity idea of creating custom views, and I'll share how to do this over video. When I go to Joe Lehr contact, we have this tab here for inbound submissions. With inbound enrichment, we have additional fields like headcount, funding, traffic rank, location, et cetera. This is a much more streamlined process. The one thing I'm working on is hitting Clay to get additional data from SEMrush when someone submits the form. I've successfully pushed the email to Clay into a table, but their basic SEMrush enrichment wasn't working. I think it's just a bug I need to figure out.

**Joe Lehr:** From there, I'll be able to add in organic traffic and other interesting data points. I'm trying to give a lot more enrichment and context for the leads in the Slack messages.

**Kyle Gaudreau:** When you say other data points, the three that matter most would be traffic, domain authority, and number of organic pages.

**Joe Lehr:** The fields I've selected are organic search visits and paid search visits. I'm looking at what Clay is pulling from SEMrush. If you want, we could purchase a SEMrush API for more flexibility — I can make direct API calls from Clay. I could structure it as individual columns or one consolidated field. The key three you mentioned were organic traffic, domain authority, and number of organic pages. I've gotten organic data from SEMrush before, but I'm not sure why this isn't working right now. I'll look into it.

**Joe Lehr:** So inbound is live today. New contacts are being brought into HubSpot.

**Joe Lehr:** I'm keeping an eye on inbound — it takes hours to thoroughly test. I've replicated what I did before. It's been a slow day so I haven't seen many inbound submissions, but I feel good about how it's built. One other callout: I've added a Slack notification for Form 1 completions. If someone puts in their email but doesn't finish the second form, there's now a Slack notification in the disqualification channel saying they didn't complete form 2. I'm not automating that because many are Gmail addresses, but the notification includes enrichment data so if the person doesn't look promising, you can reach out.

**Kyle Gaudreau:** Yeah, that makes sense.

**Joe Lehr:** So that's the inbound piece.

**Joe Lehr:** There's a few additional fields I'm bringing over on the contact record, like people stage. I wasn't sure if you want to keep that.

**Kyle Gaudreau:** I think it's good to have. We haven't really been using it earnestly — it's been more based on deal stage. But as we add folks like Tyler and work on bigger strategic deals, I can see people stage becoming more important.

**Joe Lehr:** Great. It's here and I'll backfill it for anyone missing it. Okay, so next I wanted to talk about deals.

**Joe Lehr:** Bridget, you had a question in Slack about the form data field and meeting book via inbound flow. If you want to see when any meeting was booked, that would be like an engagement date or last meeting book date. You could leverage the HubSpot calendar instead of the default calendar — it tracks that data. If someone leverages the default calendar, it won't necessarily pick that up. But when Google calendars are synced, I'll stamp the data one way or another. I prefer to operate with stage dates. If someone books, the AE creates a deal and marks them as stage one.

**Bridget McGillivray:** So I can just use the stage one date or whatever.

**Joe Lehr:** I'm going to capture that as a standard field — the initial meeting date and most recent meeting date. I need to see how the Google Calendar sync looks. It requires Kyle and Tyler to create the deal, which should happen naturally.

**Joe Lehr:** Okay, so now to deals. This is where it gets nuanced. I'll start high level. There's some automation I want to do for updating fields. Kyle, I brought over your new stages — there's one change where "meeting booked" converts to "engaged." This was imported last night and I've associated them. This includes closed-won, closed-lost, and open deals where the SOW type is either sprint or growth execution. Before I dive into line items, have you used line items in HubSpot before?

**Kyle Gaudreau:** No, I'm more familiar with the marketing side.

**Joe Lehr:** Okay, I'll walk you through it. What we're doing will help Bridget with tracking and upfront agreements while I automate as many fields as I can. We're ensuring ARR tracking is as accurate as possible given the multiple deal types. There are still more deals to port over, but I'll show you a new tab where reps can update deal details directly. I've broken this down with descriptions for fields like decision authority. I can backfill this data from Google Sheets, but the goal is to have the information available as soon as possible.

**Kyle Gaudreau:** When we select all these fields, is there a roll-up so we can see a quality score for the pipeline overall?

**Joe Lehr:** That's a good question. I can build that out. You could use Zapier with a simple custom code block to sum up the scores since each field has a number. But every time a field updates, it would trigger.

**Bridget McGillivray:** I'd rather not do that yet. Let me export it and do it in a spreadsheet for now.

**Joe Lehr:** You could use Coefficient ($100/month) — it's an extension for Google Sheets. You could push data to Google Sheets on a recurring basis, then push back to HubSpot. You'd never have to touch it and could run it every couple hours. So you'd grab this data every couple hours, refresh it, and add it to a dashboard that refreshes every three hours. Coefficient also lets you pull all line items and deals and keeps them refreshed.

**Bridget McGillivray:** I'll just sign up for it now. I can start with a trial.

**Joe Lehr:** Great. Now let me shift focus back to deals. This is where I'm going to record a walkthrough. I want to talk about line items, associating two deals, and establishing relationships. HubSpot uses labels and tags to distinguish relationships, which helps with reporting. For example, if I look at Diligent, there are two deals associated with them — one growth and one sprint. We have a SOW field I ported over. We also have a contract type field. I'll update contract type based on SOW. It's another way of establishing the relationship between deals.

**Joe Lehr:** What's really critical for reporting is linking those two deals together. When you enter contract or proposal stage, you create the growth deal and establish the relationship between the sprint and growth deals. So if this is a sprint deal, I'll pair it with the growth deal. It takes a bit of muscle memory, but once I establish the relationship, it tags the record ID of the other associated deal. So on this sprint, it grabs the growth execution record ID and tags it here. If I went to the growth deal, it would show the sprint deal ID. This tagging runs an automation so Bridget can see which deals are connected in reporting. As Diligent grows and more deals come up, this deal-deal partnership relationship ensures we can connect the dots in a streamlined way. I'll backfill this work, especially where the names are the same, and when we export it, it's very clear how the deals are connected.

**Joe Lehr:** Now with line items, this gets a bit nuanced, but I'll keep it simple and include it in the video. Line items let us account for ramping MRR and other nuances. For a sprint, I'll add a sprint line item with billing frequency and duration. For example, three months at $1,000/month equals $3,000, then nine months at $3,000/month for $27,000 total. Line items tell the story with the data so Bridget can break down the total and map it to contract dates. Most growth deals are 12 months, so it's just one line item.

**Kyle Gaudreau:** This only applies if there's variability within the same deal, not across sprint and execution. We've had deals at 4k, 5k, 6k.

**Joe Lehr:** Exactly. Line item order matters — first three months, next nine months. Bridget can easily map it out. Line items are a validation field. When I save it, the deal amount updates, which is tied to TCV. You won't be able to close the deal without line items.

**Bridget McGillivray:** Joe's putting in a lot of rules.

**Joe Lehr:** Right. We have enforcement — you can't skip stages, you have to start at stage one, you can't move backwards. This is all tied to helping us track data for reporting. Eventually, you'll move to PandaDoc and it'll be more streamlined. But for now, this prevents problems and ensures we can report on ARR and MRR. You have to add line items at some point — if you go the enterprise route...

**Joe Lehr:** This enables us to export the deal with line items, the growth expansion related to it with its own items. Very easy to export and manipulate however you want. The automation handles mapping growth expansion to growth execution once I confirm which is which. You'll need this mapped to move to close-won stage. I'll hack that if needed.

**Joe Lehr:** Kyle, by end of week, can you tell me what custom deal view you need? When you start emailing folks, you'll want activities and webinar attendance on the timeline. I'm building that for you like I am for Jason. The goal is a custom view with the important fields — like inbound enrichment on contacts — so you and Tyler know exactly which fields matter and everything's in one view. That way Tyler doesn't have to learn all the fields; he just focuses on what's in that view.

**Kyle Gaudreau:** Yeah, I can get that feedback to you some time.

**Joe Lehr:** SEMrush data would be helpful. There are different ways to hit the SEMrush API — through Clay via Zapier or direct. Bridget, I'll use Zapier since the current HubSpot package doesn't have webhook access. Whether a deal is created from inbound or directly, we'll hit SEMrush and pull that data.

**Joe Lehr:** I'll pull that data onto the contact, deal, and company records so it's referenceable across those objects. You'd want to see it on the deal record and run reports against it — show me all closed-won deals and their traffic rank. The more context you provide on what you want to see, Kyle, the better. I'm going to create a video walkthrough by Monday on how to do line items and associations so I can share it when I onboard Tyler. There are a few other videos I'll make along the way.

**Bridget McGillivray:** When do you want us to stop touching Adio?

**Joe Lehr:** Sunday night. Create any new deals in Adio and I'll port them over on Sunday night.

**Bridget McGillivray:** Okay, so until then we'll use Adio, then we'll switch. On Monday we can start testing and creating deals. Right now Marcel is doing all these random calls and telling us to open deals for eight different companies.

**Joe Lehr:** Yeah, that's what you mentioned at the top. Create those in Adio and I'll port them over when I do the final import Sunday night.

**Joe Lehr:** I'll import the newest contacts and deals every few days to minimize work, and again Sunday night I'll do the final import of all new contacts, deals, and company records. The inbound flow helps create contacts and records automatically moving forward. To minimize manual data entry, I'm trying to get Luma data into HubSpot so it auto-creates contacts and company records. Kyle, let's set up your Gmail inbox. There's also the HubSpot Chrome extension for pushing data and creating records. Everyone you talk to should exist in HubSpot.

**Joe Lehr:** Bridget, I'll DM you about a few things. The backfill of deals that don't match the sprint/growth style — you shared the login with me so I can build those out. For renewals, we need to establish if they use the same pipeline stages as new business. We also need to handle renewal automation.

**Bridget McGillivray:** Anything sprint is already in HubSpot. Anything not sprint isn't in HubSpot. Older deals that weren't sprints aren't in there. We haven't really been creating renewals yet. Alice from my team can start chipping away at backfilling renewals, starting with the ones renewing soonest. When you create the renewal, is the start date one day after the end date?

**Joe Lehr:** Got it. Okay, let me set Kyle up with email and calendar integration. There's one more thing about the renewal — when I create it, is it exactly a year from the start date or end date, or plus one day?

**Bridget McGillivray:** Plus one day from the end date.

**Joe Lehr:** I'll put together a detailed walkthrough for backfilling other deal types. The data is in your Google Sheet already, so it's not top priority for HubSpot. Alice can manually create the old deals if needed. The priority is active and open deals, plus closed-won current customers. Everything else can come later.

**Bridget McGillivray:** I use two fields to track current customers: closed-one status and a subscription end date field. For churned customers, I update the subscription end date. For active customers, that field stays blank. That lets me track current customers.

**Joe Lehr:** Got it. Coefficient will help streamline the reporting since getting a list of current customers is difficult — you have deals past their end date that are still customers, and you need to understand churn and lapse of renewal status.

**Joe Lehr:** I do think the good thing is leveraging coefficient could help streamline that.

**Joe Lehr:** Instead of me trying to build out, like, some complicated formula field.

**Joe Lehr:** Because there are instances, like, where a big pain point for reporting that I used to have is, like, folks would ask, like, give me a list of our current customers.

**Joe Lehr:** And that's a really difficult thing to do because you're going to have deals that are customers that have gone over their end date but are still technically a customer.

**Joe Lehr:** But, you know, how do you reflect that?

**Joe Lehr:** So you're, like, lapse of renewal is something I used to put.

**Joe Lehr:** I literally don't know how many customers we have ever.

**Bridget McGillivray:** Every month, I'm counting random  in random places.

**Bridget McGillivray:** It's crazy.

**Bridget McGillivray:** There's only 40, and I can't get it right.

**Joe Lehr:** So hopefully with the Google Sheet piece, this is where it gets really easy because you'll have reference to all the deals.

**Joe Lehr:** And if there's not a churn deal, for this example I'll talk to you right now, for this customer, if it's an open renewal and you're outside of the current deal, start date, end date, the logic would be lapse and renewal.

**Joe Lehr:** So the beauty of having all this data on Google Sheets where it's easily accessible and interconnected through the relationships is that you could run this with coefficient.

**Joe Lehr:** So coefficient could run like twice a day, three times a day to update account status.

**Joe Lehr:** But what would be the trivia for that?

**Bridget McGillivray:** would be has closed one stage and is before the end date and doesn't have a renewal or something like So for like for lapse renewal, which is always.

**Joe Lehr:** Like the killer for me is like, oh, they're going back and forth over negotiation for the renewal or trying to expand them.

**Joe Lehr:** They don't want to expand.

**Joe Lehr:** You would see that it's not active.

**Joe Lehr:** You're no longer between the start date and end date of the most recent deal.

**Joe Lehr:** And now the next deal in line is not opened or it's not one or closed.

**Joe Lehr:** So you're looking at two different deal objects to understand the state of the company.

**Bridget McGillivray:** I think the hard part for me right now is, well, one, we don't have end dates on any deals.

**Bridget McGillivray:** I know, I'm having that.

**Bridget McGillivray:** So there's that.

**Bridget McGillivray:** But as soon as I know about churn, I go update.

**Bridget McGillivray:** I sent you the report in the chat.

**Bridget McGillivray:** I'm updating a subscription end date field for myself just so I can always pull the list of churns and when.

**Bridget McGillivray:** I remember you said Marcel doesn't like churn.

**Joe Lehr:** So I'm not pushing that.

**Joe Lehr:** But I am putting, obviously, I'm going to follow your lead here.

**Joe Lehr:** But, like, it is a need to fill in HubSpot end date.

**Joe Lehr:** I just changed the contract end date.

**Joe Lehr:** That would just be, like, the length.

**Joe Lehr:** Of the actual deal.

**Joe Lehr:** And then there could be like a new field called subscription end date, which is aka churn.

**Bridget McGillivray:** Well, I feel like, okay, but say we have a 12-month deal and someone cancels halfway through.

**Bridget McGillivray:** Usually what I do, yeah, is I just move the end date up.

**Bridget McGillivray:** I don't make it close, lost, or anything.

**Bridget McGillivray:** I just move the end date up.

**Joe Lehr:** It's up to your reporting style.

**Joe Lehr:** I would lean towards having the original data and then have the formulas living in Google Sheet to account for, hey, this is no longer 12 months.

**Joe Lehr:** It's actually six months.

**Joe Lehr:** But at least you could see that the AE closed a 12-month contract until like a six-month contract.

**Joe Lehr:** But then they go into CRM and it looks like it's a 12-month deal.

**Bridget McGillivray:** The other thing you could do is add another negative op or something.

**Bridget McGillivray:** Yeah, I mean, there's like so much nuance to this.

**Joe Lehr:** Like, to me, like, given it's small team and we need to ensure you're reporting correctly, I'll do whatever.

**Joe Lehr:** You want, but it's the fact of the matter.

**Joe Lehr:** like, we're giving you the data in Google Sheets for the most accurate reporting.

**Joe Lehr:** Like, amount is going to be a tricky thing.

**Joe Lehr:** We've talked about this.

**Joe Lehr:** If it's not like a 12-month contract, maybe it's a 14-month contract.

**Joe Lehr:** It gets a little tricky for, like, if you look at the ARR field in HubSpot, right?

**Joe Lehr:** It doesn't always reflect correctly.

**Joe Lehr:** So, I mean, I'll follow your lead here, but, like, yeah, for the subscription end date, that should live on the deal, though, then, right?

**Joe Lehr:** Or they should just update that.

**Joe Lehr:** A normal end date, basically.

**Joe Lehr:** Okay.

**Joe Lehr:** So, they would just update the contract end date, and you don't want there to be...

**Joe Lehr:** The only reason why I was looking to have end date is for the automation piece, for creating the renewal.

**Kyle Gaudreau:** Yeah, yeah.

**Bridget McGillivray:** I want to have end date, but end date can be automated.

**Bridget McGillivray:** Like, it's put the start date, and then look at the term length, and then create an end date.

**Bridget McGillivray:** Yeah.

**Bridget McGillivray:** And And then...

**Bridget McGillivray:** then...

**Bridget McGillivray:** Create a renewal one day post-end date with another whatever.

**Bridget McGillivray:** then if I need to change the end date, like say somebody canceled, I would go, I would change the end date and move it up and I would close lost the renewal.

**Bridget McGillivray:** Yeah.

**Joe Lehr:** That makes sense.

**Joe Lehr:** Is that not what you would do?

**Bridget McGillivray:** No, I would.

**Bridget McGillivray:** Yeah, definitely close lost the renewal.

**Bridget McGillivray:** So just need one end date.

**Joe Lehr:** Okay, yeah, the only difference, yeah, I mean, we captured like known churn date when I like in the past when I was at the CS platform.

**Joe Lehr:** But the way we looked at it's like the contract start date and end date were like locked in place.

**Joe Lehr:** But we knew that the expected churn date, the known churn date when they gave us formal notice that they're going to churn was, but this is different.

**Joe Lehr:** It's a different like use case to what you're talking to for tracking.

**Joe Lehr:** Yeah, I don't know.

**Joe Lehr:** Well, I'll follow your lead, obviously, on this.

**Joe Lehr:** It's like...

**Bridget McGillivray:** Like, Erickson, for example, needs to go and, like, know what – because you don't actually amend contracts when they just cancel.

**Bridget McGillivray:** So the contract still looks like it's 12 months, but we update the deal.

**Bridget McGillivray:** Like, when you get audited, you basically send them all your contracts and then an export of your CRM, and, like, there'll be some note in there, like – I don't know.

**Joe Lehr:** That's how Erickson and have done it in the past.

**Joe Lehr:** to do this a lot better than I do.

**Joe Lehr:** So this is not me, like, putting my foot in the ground thing.

**Joe Lehr:** Yeah.

**Bridget McGillivray:** No, it's just – but, like, we've done – we did all this stuff because we also had a massive data team, and we were putting everything in a warehouse, layering on a ton of DBT stuff, and spitting out metabase reports.

**Bridget McGillivray:** Like, we did not have to do crazy sheets.

**Bridget McGillivray:** So we were not building, like, the same way.

**Bridget McGillivray:** Yeah.

**Joe Lehr:** I mean, you're going to be doing –

**Joe Lehr:** Basically, what you're doing, you're turning Google Sheets into a many data warehouse, right?

**Joe Lehr:** Because you're going to be pulling and pushing data with Google.

**Joe Lehr:** But yeah, I totally get what you're saying.

**Joe Lehr:** It'll become a lot clearer when I just get it kind of like stood up.

**Joe Lehr:** And I think that's what I'll do.

**Joe Lehr:** That's something after Monday that I'll work with you on because I think that'll just be the purpose of getting the deal, Google Sheets stuff totally aligned.

**Joe Lehr:** The one other thing I didn't really talk about, just I need to like go through Zapier and just make sure like the close one Zap, right?

**Joe Lehr:** I just need to bring that over into, into HubSpot and whatnot.

**Joe Lehr:** That's not a challenging thing to do.

**Joe Lehr:** I just have to like spend the time looking through it.

**Joe Lehr:** Are there any other Zap that come to mind?

**Bridget McGillivray:** Just the close one and the pipeline.

**Joe Lehr:** I mean, the pipeline one, I remember we talked about early when I first started.

**Joe Lehr:** I can't remember what it is.

**Bridget McGillivray:** It's just any kind of stage changes, it's going to that like alerts pipeline channel.

**Bridget McGillivray:** Okay.

**Bridget McGillivray:** And you, do you want the, I know there's back and forth.

**Joe Lehr:** Do

**Joe Lehr:** Do want to keep it for all stages?

**Bridget McGillivray:** Yeah.

**Bridget McGillivray:** Okay.

**Joe Lehr:** This is done through Slack, HubSpot to Slack.

**Joe Lehr:** So it's not even like Zapier is going to play with this.

**Joe Lehr:** It's not like we're going to waste zaps anymore.

**Joe Lehr:** Because I'm just going to do the workflow internally for both of these two.

**Joe Lehr:** The disqualified inbound and did not book, I updated it's live.

**Joe Lehr:** That's going through Zapier.

**Joe Lehr:** Okay.

**Bridget McGillivray:** Whatever's easier.

**Bridget McGillivray:** mean, I don't mind.

**Bridget McGillivray:** Yeah, super easy.

**Joe Lehr:** I just missed the Adio one, by the way, while we were chatting earlier.

**Bridget McGillivray:** It was still sending like, you haven't filled in these fields.

**Bridget McGillivray:** Oh, God.

**Joe Lehr:** Sorry.

**Joe Lehr:** just turned it off.

**Joe Lehr:** Thank you.

**Joe Lehr:** I know you asked me, Tortha.

**Bridget McGillivray:** turned it You don't think we need that because we're not going to let them even close the deal without the fields.

**Bridget McGillivray:** Right.

**Joe Lehr:** It's going to be a little hacky, like just to call this out.

**Joe Lehr:** Like I'll share with you in video.

**Joe Lehr:** That's one thing I'll do.

**Joe Lehr:** Like it's very straightforward.

**Joe Lehr:** If you're like closed one, closed loss requires closed loss reason.

**Joe Lehr:** But when it gets a little bit more new.

**Joe Lehr:** Which is like, sprint deal, type equals sprint deal, requires associated growth ID.

**Joe Lehr:** So like, you'll see I kind of hack it together by like creating that new fields that kind of encapsulate all that logic, and then just like, this has to be true.

**Joe Lehr:** So I'll share it.

**Joe Lehr:** I don't know if that makes sense.

**Bridget McGillivray:** I don't know if you know Salesforce, but it's not like creating different, like there's this pretty drag and drop to create different like validation rules.

**Joe Lehr:** It's similar, but it's just the take into account, like there's like nuance between different pipelines.

**Joe Lehr:** You can't get to that level of like, if the pipeline is new business, require this field, versus if it's renewal, require this field.

**Bridget McGillivray:** Oh, no, but can't I just make multiple different ones?

**Joe Lehr:** You can across, I guess you can against across the pipelines, but we're using the same pipelines.

**Joe Lehr:** right.

**Joe Lehr:** comments.

**Joe Lehr:** I don't think we can.

**Joe Lehr:** Okay.

**Joe Lehr:** I'll walk you through it in the video.

**Joe Lehr:** Are there specific fields that come to mind that you want to have required besides the ones I've been talking to?

**Bridget McGillivray:** Honestly, just the basic stuff to start, like end date, start date, attach a contract, have the objects, not what am I calling it, the like line items filled out, billing contact, like there's probably 10.

**Bridget McGillivray:** Okay.

**Bridget McGillivray:** And then like I've always, like there's certain ones that certain, I don't think we need to get into this yet, but like at some point we'll have like can't even move it into contract if you don't have.

**Bridget McGillivray:** Yeah, that's really easy to do.

**Joe Lehr:** Like based on the pages, it's very simple.

**Joe Lehr:** It's just like when we get like very nuanced into like the different values, if this is a sprint deal versus a growth deal.

**Joe Lehr:** What's required.

**Joe Lehr:** But it's all doable.

**Joe Lehr:** That's like the truth.

**Joe Lehr:** Kyle, can you go five minutes over?

**Joe Lehr:** Do you have a call?

**Kyle Gaudreau:** I got to run, but I just connected my calendar.

**Kyle Gaudreau:** I got a jump ticket.

**Kyle Gaudreau:** Thank you, Joe.

**Kyle Gaudreau:** Thank you.

**Kyle Gaudreau:** I know I threw a lot at you guys.

**Joe Lehr:** I promise you this will be very detailed and a simple to digest document.

**Joe Lehr:** I'm over booking time with Tyler.

**Joe Lehr:** Yeah.

**Joe Lehr:** Okay.

**Joe Lehr:** Kyle, have to do your Gmail as well.

**Kyle Gaudreau:** So I did Gmail.

**Kyle Gaudreau:** Here, I'll just share my screen real quick.

**Kyle Gaudreau:** Let me know if I'm missing anything.

**Joe Lehr:** I apologize if this was not.

**Joe Lehr:** I wish I had more time to prepare for this meeting, but it's just been so focused on.

**Joe Lehr:** No, no, no.

**Joe Lehr:** You're good.

**Joe Lehr:** You're good.

**Kyle Gaudreau:** No stress, man.

**Kyle Gaudreau:** This is good.

**Joe Lehr:** All right.

**Kyle Gaudreau:** So I authenticated this.

**Kyle Gaudreau:** I'm still kind of going through the steps.

**Kyle Gaudreau:** I don't know if there's.

**Kyle Gaudreau:** Is that your correct calendar?

**Joe Lehr:** Is it GrowthX Labs or is it GrowthX.ai?

**Joe Lehr:** Yeah.

**Kyle Gaudreau:** Well, I have.

**Kyle Gaudreau:** Technically, this is the one I have a true account for, and I need to migrate eventually to the other.

**Joe Lehr:** If you scroll up, can you go to email as well?

**Joe Lehr:** Connect personal email, so you have to connect, add that.

**Joe Lehr:** Do I want this turned on?

**Kyle Gaudreau:** I don't know what that is.

**Joe Lehr:** It lets you send emails.

**Joe Lehr:** It lets you track if someone replies or not.

**Kyle Gaudreau:** So this is still my, I don't know why it's saying personal, but.

**Kyle Gaudreau:** Personal means like your actual inbox.

**Joe Lehr:** yeah.

**Joe Lehr:** Yeah, this is what everyone does, so no stress.

**Joe Lehr:** Yeah, yeah, cool.

**Kyle Gaudreau:** This is how you send sequences.

**Joe Lehr:** Got it, got it.

**Joe Lehr:** Sent through your Gmail.

**Joe Lehr:** Got it.

**Joe Lehr:** And the last thing you need to do is just like download the HubSpot Chrome XMPA.

**Joe Lehr:** You can click that, and that's nice to do it right there.

**Kyle Gaudreau:** Let's see.

**Kyle Gaudreau:** I don't use Chrome extensions anymore.

**Kyle Gaudreau:** Cool.

**Kyle Gaudreau:** All right.

**Kyle Gaudreau:** Kyle, you're all set.

**Kyle Gaudreau:** Okay.

**Kyle Gaudreau:** I think I'm good.

**Kyle Gaudreau:** Nice.

**Joe Lehr:** So that will start tracking emails now moving forward, and you'll see on there.

**Joe Lehr:** Now, if you like, oh, I know you have go in a second.

**Joe Lehr:** If you were to open up the Chrome extension, I think there's options in it for, like, create contact if not existing in HubSpot or stuff like that.

**Joe Lehr:** I can't recall.

**Kyle Gaudreau:** Browser notifications turned.

**Kyle Gaudreau:** I want to start seeing real-time activity.

**Kyle Gaudreau:** Oh, my God.

**Kyle Gaudreau:** I got to  authenticate again.

**Kyle Gaudreau:** Yeah.

**Joe Lehr:** It's all good.

**Kyle Gaudreau:** All right.

**Kyle Gaudreau:** I think, yeah, I think I got it.

**Kyle Gaudreau:** I

**Kyle Gaudreau:** Let me know if there's something else I'm missing, but yeah.

**Joe Lehr:** Whatever feedback you can provide as you're clicking around.

**Joe Lehr:** I think the biggest thing is I'm going to owe you some enablement content.

**Joe Lehr:** It'll be very clear.

**Joe Lehr:** I'll have it played out already before I turn on the video.

**Joe Lehr:** I think I just need to know what the layout is for the deal record and maybe even the contact.

**Joe Lehr:** Yeah, sounds good.

**Kyle Gaudreau:** Hopefully, you should have time on Friday.

**Joe Lehr:** Cool.

**Joe Lehr:** All right, dude.

**Joe Lehr:** Appreciate the time.

**Joe Lehr:** Thank you.

**Joe Lehr:** Bye.

**Joe Lehr:** See you.

**Joe Lehr:** Bye.
