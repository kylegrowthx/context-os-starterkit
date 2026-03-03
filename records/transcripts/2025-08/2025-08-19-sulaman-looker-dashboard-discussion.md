# Sulaman - Looker Dashboard Discussion

<metadata>
date: 2025-08-19
time: 13:59 UTC
duration: 25 minutes
organizer: Vivek Shankar
participants: Sulaman Ahmed, Vivek Shankar
fathom_recording_id: 81417473
fathom_url: https://fathom.video/calls/384493354
share_url: https://fathom.video/share/MSTJRd1893vzqvLMyL61syHACGxq1bkx
source: fathom
enriched_on: 2026-03-03 18:45 UTC
</metadata>

---

## Summary

Vivek walked Sulaman through detailed Looker dashboard updates for the Seat client, including creating state-level and city-level page performance tabs, adding a glossary page cohort with control fields and GSC data tables, and updating the non-branded tab chart. Sulaman also reported severe workload spikes on Thursdays and Fridays (54 articles in 14 hours the previous Friday) and is exploring support options, while Vivek advised that due to team absences this week and next, Sulaman should send completed dashboards directly to Jacob for review and schedule calls rather than tagging Vivek on Linear.

---

## Context

This is an internal GrowthX delivery sync between Vivek Shankar (Account Lead) and Sulaman Ahmed (Delivery Specialist) for the Seat client, a major publishing account that produces large volumes of content across state and city pages. The meeting focuses on the second half of Sulaman's ongoing dashboard work: implementing advanced cohorts in Looker to track performance by page type and geography. Sulaman has been handling the dashboard development directly in Looker while managing concurrent publishing workflows. The team context is critical: this week and the following week are understaffed (Timmy, Nika, and Maram out of office), leaving only Vivek and Ismail to manage all accounts, which is why Vivek is setting expectations about review timelines and communication channels.

---

## Relevance

**To GrowthX Delivery:**
- Seat dashboard development demonstrates advanced Looker cohort logic (state-level and city-level cohorts using regex matching) with custom fields and control field dropdowns — reusable pattern for other clients with geographic or categorical segmentation
- Glossary page tracking is a new content segment that requires custom field maintenance as new pages are published; documentation and training videos will reduce future support tickets
- Heavy workload concentration on publishing days (Thursday/Friday) — Sulaman published 54 articles in 14 hours on one Friday — indicates need for process documentation and potential resource support on peak days; currently exploring security clearance for team member assistance

**To GrowthX Business Development:**
- Seat account health: strong engagement signal (client requesting multiple dashboard iterations with detailed specifications); high volume publishing activity indicates scaled content operations
- Renewal/expansion potential: client investment in analytics sophistication (multiple cohorts, detailed tracking) suggests content strategy is working and opportunity to upsell additional reporting or analysis services

---

## Overview

- Two new dashboard tabs needed: state-level and city-level page performance
- Glossary tab requires updates with specific charts and control fields
- Sulaman facing heavy workload on Thursdays/Fridays; seeking support options
- Vivek advised direct communication with Jacob for dashboard review due to team absences

---

## Key Topics

### Looker Dashboard Updates

  - Create two new tabs for state-level and city-level page performance
      - Replicate charts from overall tab for both new tabs
      - Use case statements to cohort URLs for state and city pages
      - Apply filters for non-growthx URLs and respective page types
  - Update Glossary tab:
      - Create custom field for glossary page cohort
      - Add control field dropdown (glossary/non-glossary)
      - Copy first chart from overall tab, adjust for glossary pages
      - Add table with sessions, gate sessions, deltas
      - Create new GSC data table (landing page, impressions, position, deltas)
      - Copy non-branded tab chart, remove filter, set control field
  - Instruct Jess on using new Glossary tab features and updating URLs

### Workload Management

  - Sulaman reported 14-hour workday (54 articles) last Friday
  - Discussed with Andy about workload distribution
  - Exploring options for additional support on heavy publishing days
  - Creating documentation and Notion page updates for improved processes

### Project Management

  - Vivek reminded about follow-up task for Monograph dashboard (keywords view)
  - Due to team absences, Vivek advised Sulaman to:
      - Send completed Looker updates directly to Jacob
      - Schedule call with Vivek for complex issues, rather than tagging on Linear

---

## Action Items

**Sulaman Ahmed**
- Update Seat Looker dashboard - 2 new tabs (state/city level pages), add conversion events filter, update glossary tab

- Monograph dashboard - Make keywords filter permanent (create custom view)

- Send completed Looker dashboards to Jacob (cc Jess) for review

---

## Transcript
**Sulaman Ahmed:** On which specific page they are asking us to place that filter?

**Sulaman Ahmed:** it like from- In conversion events.

**Vivek Shankar:** Okay, yeah.

**Sulaman Ahmed:** And they just want to see those events?

**Sulaman Ahmed:** Yes. So that would be just a filter update to only show those events. That would be the first thing — can we just see if the events are showing up, like he's mentioned purchases.

**Vivek Shankar:** Can we see if events is, if purchases is there in the dropdown, like it should be showing up.

**Vivek Shankar:** So yeah, we just, just make sure we, so you see he's typed purchases, but the event name is purchase.

**Vivek Shankar:** Yep.

**Vivek Shankar:** So yeah, just verified what the actual event name is from the dropdown and then proceed.

**Sulaman Ahmed:** And what about this one? Create a new tab that shows state and city level page performance in aggregate.

**Vivek Shankar:** Yeah, I don't know what their pages are. So we need to look at the AirTable. Can we just go there real quick?

**Sulaman Ahmed:** Yes.

**Sulaman Ahmed:** The first one, OS.

**Vivek Shankar:** Okay, so it should be this one?

**Sulaman Ahmed:** No, he says state level and city level pages. They have different tabs for those.

**Vivek Shankar:** Okay, so they have a published URL. Can you go back to Linear real quick? State and city level page performance in aggregate. Okay, so basically, this is quite straightforward. They have — so we create cohorts in the backend for state pages and city pages.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** So if you go to the Airtable, you see all the published URLs over here. So this is state level pages, right? So in your case statement, you just say, if URL regex match this, then state level page. And then you do the same for city.

**Sulaman Ahmed:** I think we're already doing that city level and location, but ideally it would be working like this one, right?

**Vivek Shankar:** Well, it won't show up here. We'll have a separate tab for it because I think what he's saying is that on the main assignments tab in AirTable, they're using different cohorts. So if you go to their main tab — do you remember what it was?

**Sulaman Ahmed:** I think they have this divided into chunks. And this is what we did in the Looker, in the backend for the variables too — like city level, city level, city level, and so on.

**Vivek Shankar:** Okay, so where is city level showing up? Can you just search for that in their AirTable? Just control F "city level" because that's the name they're using, right?

**Sulaman Ahmed:** That is from here. So they are using these as keywords for the cohorts. So it's not specifically defined in one place.

**Vivek Shankar:** Where are the other cohorts then? I'm not seeing that. One was state level, one was city level. But city level is not showing up in our Looker, right? So where is location? Where is editorial?

**Sulaman Ahmed:** That's a good question.

**Sulaman Ahmed:** Where is editorial? Have they changed their table, or...? It seems like they have changed it, but let me just confirm that. Yes, you can see editorial and location.

**Vivek Shankar:** And where is it in the data? Yeah, just take one of those URLs. It's not in city level. Let's check here. Yep, here it is.

**Vivek Shankar:** Okay, so blog content is their main thing. And then can we scroll to the left or right? Which column did you use to cohort it? Do you remember?

**Sulaman Ahmed:** Grammatic. Editorial location. I think there were multiple tabs for these. Like, each one was representing a keyword. It was not just one. It was different compared to other ones we do.

**Vivek Shankar:** Okay. What is the first tab — condition hub or whatever? What is that called? The first tab?

**Vivek Shankar:** Obviously, this is not it. So, yeah, I don't know what's going on. The reason I'm asking all this is I'm trying to figure out whether we need to keep the old cohorts or remove them. Because if they're not using the old cohorts, we don't need that tab, basically. That's my concern. But anyway, for now, since they have separate tabs for state level and city level, we can just do it for those. So we create a case statement for city level pages and another case for state level. You will need to do it for GSC and GA. And then he's saying performance in aggregate for these pages. So basically, we need to do whatever's on the first page in the overall tab. We'll need to build all of that out for both of these groups. So on the first page, when you see these charts, right, we'll need to have all this done for the state level page and city level pages.

**Sulaman Ahmed:** So ideally I would replicate it once more and that would show both state level and city level, or state level will have a separate page and city level will have a separate page?

**Vivek Shankar:** Yeah, they'll have separate pages. So two new pages.

**Sulaman Ahmed:** Okay, so your URL cohorts for the state level page will just be non-GrowthX URLs and state level page.

**Vivek Shankar:** Got it. So like location and editorial can go.

**Sulaman Ahmed:** Okay, so I think this one is clear. Two new tabs for state and city with a copy of the overall one. And then a filter for those events. That was easy. No, the second one is where you even guided me on how to do that. But I was slightly confused with this one.

**Vivek Shankar:** So, yes, this is for Seat. Yeah, I forgot what this was about. So can you scroll down to Jess's comment? Yeah, just stop there, please. Do you need accessions or both?

**Sulaman Ahmed:** She needs both.

**Vivek Shankar:** Okay, impressions, positions. We don't need them in cohorts, we just need to see traffic trends in a table, and then a table showing each page's info similar to the cohorts tab. Okay, can you scroll up a little bit? No, to the request — all the way to the top, yeah. "I need support on Seat glossary tab." Okay, can we go to the Looker? Okay, so she has the glossary tab there at the end. I think that's the one where we need to change something.

**Sulaman Ahmed:** And if that is a question, we don't have that. Yeah, this is...

**Vivek Shankar:** This is not working at all. I think she's, yeah. So, okay, this is, we just need to cohort it again. So if you go back to the Linear ticket, if you just follow the steps, I think it'll tell you. So can you scroll down to my message? Yeah, so we need to create a custom field. That's basically your case statement. So you're cohorting all the glossary page URLs into a case regex match if match glossary page.

**Sulaman Ahmed:** So all the URLs and they will match to the keyword "glossary page."

**Vivek Shankar:** Yeah, so that's what the second step is. Case statement. Copy the first chart from the overall page. So the overall tab in Looker, the first page, you just copy that chart. So it should be this one.

**Sulaman Ahmed:** This one, yes.

**Vivek Shankar:** Got it. So this one you copy and then the source is the same. You just need to — the source is still GA4, but then you need to use a control field. Oh, I used the wrong word there. It's not a filter. You need to use that control field on top. So can you go back to the overall tab? So that content pillar is one where it says, right?

**Sulaman Ahmed:** Yeah.

**Vivek Shankar:** Instead of that, it needs to be the — it'll say glossary page or non-glossary page, basically.

**Vivek Shankar:** So your control field needs to be the glossary page custom field.

**Sulaman Ahmed:** So we will have two values in here — one would be glossary and one would be non-glossary?

**Vivek Shankar:** Yes, because you're creating that custom field, right? So you see how her control field right now is content pillars one on the right-hand side — that one. So instead of that, you'll have to put our custom field that you will create.

**Sulaman Ahmed:** So a new variable on the back-end that would be in here. And the if condition would be glossary page, else would be non-glossary — the way else was previously non-glossary.

**Vivek Shankar:** Yes, that's what the previous steps are doing, right, in my notes. So if you go back to Linear — just one thing: when I say create a filter and include page type custom field name, instead of filter, it should say control field. So just keep that in mind. Basically, the dropdown is what you need to add. And add a date control — that's pretty straightforward.

**Vivek Shankar:** And then add a table showing sessions and gate sessions with deltas and apply the glossary control. You just need to add that table. You can copy it literally.

**Sulaman Ahmed:** And now the filter you're having, in this case, it would be this one?

**Vivek Shankar:** No, it's still the control field. Control field — as long as you place it on top, it will control every single chart on the page.

**Sulaman Ahmed:** Got it.

**Vivek Shankar:** And then the next one is add the table. This one, you will have to create it. So you just add a new table with GSC data source and apply the control field. Yeah, again, it's your control field. I don't know why I kept saying filter. And then your columns are landing page, impressions, position, and deltas, basically.

**Sulaman Ahmed:** So this one we don't have already. This is something I will create a new table. And it would look something like this one?

**Vivek Shankar:** No, this is from GA4. For GSC, we don't have an equivalent GSC table. But just like the appearance of that table would look something like this, yeah.

**Sulaman Ahmed:** And then copy a chart from the non-branded tab.

**Vivek Shankar:** So yeah, the non-branded tab — that performance chart that you have, you take that. The first chart is clicks and impressions. So you basically copy this, and then you remove that filter. Let me go back to Linear real quick. Oh, okay, so this is just for GSC. So you just need to create a chart that quantifies GSC performance, like clicks and impressions, et cetera. So basically, you can follow the steps as I've written it here. So you take that chart, remove the filter, and then, can you show me the chart again?

**Vivek Shankar:** Sorry.

**Sulaman Ahmed:** Yes.

**Vivek Shankar:** This one — impression click, yeah, it's fine. We can use this. So you just need to remove that filter, the non-branded query filter. Just make sure you remove that when you copy it. Source is still GSC, and then make sure the control field is set to glossary page.

**Sulaman Ahmed:** Got it. So it will be just one new tab using the glossary one, add all the tables you mentioned, and there will be one control field on the top and a date range.

**Vivek Shankar:** Yep.

**Vivek Shankar:** And remember, you need to tell her what to do. Otherwise, she's going to come back and create more tickets for you. You need to tell her that in the Glossary tab, and please review this call again, because I know I'm saying a lot of things. In the Glossary tab, you need to tell her that to get the Glossary page performance, you need to select Glossary in the dropdown. Yeah, because this dropdown pillar over there — there'll be a dropdown on top of this page, right? So it'll say Glossary page, Non-Glossary page. You need to tell her that you have to check off the Glossary page and uncheck Non-Glossary page to see the performance for those pages.

**Sulaman Ahmed:** Got it.

**Vivek Shankar:** You also have to tell her that as Glossary pages are added, she needs to update that. Whenever they're published, whenever new ones are published, she has to do it. You can't send her that same video because it will confuse her — it will say URL list one, URL category, but that's not the one, right? So you need to tell her that the custom field that you have created, called glossary page or whatever you call it, that needs updating.

**Sulaman Ahmed:** Understood, got it. You're correct, that could be confusing, but I got it. Okay, thank you so much. That was comprehensive. I think I'm good to start with it.

**Sulaman Ahmed:** Actually, I'm not super good with Looker — it involves a lot of SQL terminologies and technical field definitions, but I think I'm good to start with it. Other than that, last week was good except for Friday. I was off on Thursday, and on Friday there was a ton of articles that needed to be published — 54 articles to be exact. That took 14 hours. This week I requested to meet with Andy earlier — she had scheduled a meeting for Wednesday but I asked if we could make it yesterday instead. I informed her about the workload situation. Normally on each working day, the load is manageable — I have some publishing tasks, some dashboard work, and other stuff. But on Thursday and Friday, especially Friday, the tasks pile up and that takes quite a lot of time. Previously, my teammate and I would work on tasks together and we were fine with that. But Andy mentioned that we have client contracts and without security clearance, my teammate can't work on those. So I asked if it's possible to have my teammate work along with me on Fridays after getting security clearance, rather than hiring another freelancer. The issue with a freelancer is it's not a fixed arrangement — it would be ad-hoc, and they wouldn't have the background on how to publish properly. Plus, we get client feedback on what needs to be done differently each time. Training videos don't cover that. Right now I'm creating documentation and I've requested from our team to share the Notion pages where they keep notes so I can keep those updated. So far, everything else is going well.

**Vivek Shankar:** Okay, that's good to know. Just one more reminder about the Looker dashboard in Monograph. There was a follow-up task for you this week. We did a temporary hack on one of those dashboards, but we need to make it permanent. We applied a filter, but we need to make it a custom view.

**Sulaman Ahmed:** Exactly, the keywords one. I will definitely have a look at that. For these Seat dashboards, I gave myself a deadline of Wednesday. I'm confident I'll be able to do that today along with the publishing work. So yes, definitely I'll have a look. I understood the requirements with the Looker dashboard work, but I needed some clarification. I think I'm good with it now.

**Vivek Shankar:** Okay, no worries.

**Vivek Shankar:** Just to give you some further context — this week and next week is absolutely crazy because Timmy and Nika are both out of office, and Maram's also out of office. So basically it's just Ismail and me managing all accounts together. So once you're done with the Lookers, just go ahead and send it to Jacob and ask him to review it. If you ask me to review it, then I'm going to become a bottleneck for you. I'll probably only be able to review on Friday or something like that. So just send it to Jacob and Jess. And then if they come back with weird questions or issues, pull me in and we can discuss. Actually, I would prefer if you book a call with me rather than tagging me on Linear. If you tag me on Linear, I probably won't prioritize it. But if it's on my calendar, then I'll know for sure that we can get through all the issues in that half hour.

**Sulaman Ahmed:** So Jacob is a director? I thought he was a managing editor.

**Vivek Shankar:** He's a director. Jess reports to him.

**Sulaman Ahmed:** Got it. So I'll send this to his director to review the dashboard. If he thinks it's good, that's good. If he has any questions, I can list them out and schedule a call with you to discuss if it's something complicated.

**Vivek Shankar:** Got it. I think the reason I said Jacob is because I think Jacob is the one who created that ticket that you just showed me.

**Sulaman Ahmed:** Actually, it was Jess and Jacob was cc'd in the ticket.

**Vivek Shankar:** Cc'd, yeah, okay. So fine, just cc them back. Got it, perfect.

**Sulaman Ahmed:** This is the case where both the dashboards have Jacob cc'd in them.

**Vivek Shankar:** Yeah, got it. All right. Thanks.

**Sulaman Ahmed:** Thank you so much. By the way, I assume this meeting is being recorded on Fathom.

**Vivek Shankar:** Yes, I think my recorder is on here. Do you have a recorder as well, or do you want me to share the recording?

**Sulaman Ahmed:** I've done Google Doc calls in meetings before and it creates a mess with multiple recorders. Would it be possible for you to share?

**Vivek Shankar:** Yeah, I'll send it to you.

**Sulaman Ahmed:** Thank you so much.

**Vivek Shankar:** Thank you so much. Have a nice day.

**Sulaman Ahmed:** Bye now.

**Vivek Shankar:** All right. Bye.
