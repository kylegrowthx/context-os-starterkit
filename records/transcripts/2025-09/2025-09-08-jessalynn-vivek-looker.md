# Jessalynn <> Vivek looker

<metadata>
date: 2025-09-08
time: 14:00 UTC
duration: 31 minutes
organizer: vivek@growthxlabs.com
participants: Jessalynn Jones, Vivek Shankar, Jakub Rudnik
fathom_recording_id: 85587966
fathom_url: https://fathom.video/calls/402516091
share_url: https://fathom.video/share/nPn8QXxPAfKoTvd9FJPGWWxyaxa_1D-L
source: fathom
enriched_on: 2026-03-02 12:00 UTC
</metadata>

---

## Summary

GrowthX planned HubSpot lead data integration into Looker for clients Tiro and Webstacks, with Vivek confirming that a manual weekly workflow (clients export to Google Sheets, Jessalynn tags GrowthX leads) is the only feasible approach due to Looker's data sampling limitations with direct API connections. The team finalized data requirements (create date, first page seen, GX lead indicator) and identified secondary Looker enhancements: fixing a 10-bar chart limit to show full historical data, adding monthly view options alongside weekly views, and adding content distribution counts by cohort.

---

## Context

GrowthX clients Tiro and Webstacks are seeking deeper visibility into the pipeline impact of GrowthX's content production work. Both companies want to integrate HubSpot lead data into their Looker reporting dashboards to track leads generated from GrowthX-produced content. Jessalynn Jones leads delivery coordination and requested this meeting with Vivek Shankar (Looker architect) and Jakub Rudnik (likely product or strategy input on client requirements) to clarify what's technically possible in Looker and define the data export and tagging workflow needed from the clients' HubSpot instances.

---

## Relevance

**To GrowthX Delivery:**
- HubSpot-to-Looker integration workflow requires manual weekly updates via Google Sheets (no direct API connection due to Looker data sampling issues). Jessalynn will manage the spreadsheets and lead tagging.
- VLOOKUP formulas in Google Sheets can automate GX lead identification if Airtable maintains an updated list of GrowthX-produced URLs. Suleiman may build an Airtable export script.
- Looker reports cannot perform complex data transformations; all pre-processing must happen in the spreadsheet before Looker ingests the data.

**To GrowthX Business Development:**
- Both Tiro and Webstacks are moving reporting emphasis from weekly to monthly cadence, indicating longer-term engagement and more strategic use of the reports.
- Webstacks blog generates low volume of GrowthX-specific leads, but Jessalynn is building a holistic story showing overall blog impact and volume to address reporting concerns.
- Tiro generates substantial leads from GrowthX-produced content (GrowthX has authored their entire blog), making them an ideal reference for pipeline impact reporting.

---

## Overview

- HubSpot data will be exported to a Google Sheet, which Looker can then access for reporting
- Manual tagging of GrowthX-produced content will be required, but can be aided by VLOOKUP formulas
- Additional visualizations requested: monthly view option and content distribution across cohorts
- Vivek will address the bar chart limitation and explore adding monthly data views

---

## Key Topics

### HubSpot Integration Process

  - Clients (Tiro and Webstacks) to export HubSpot data to a Google Sheet in the Teams folder
  - Sheet to include: create date, first page seen, and GX lead indication
  - GrowthX team to manually tag GX-produced content
  - Looker will read and display data from this sheet

### Data Visualization Requests

  - Extended historical data view (bar chart limitation fixed)
  - Monthly view option in addition to weekly
  - Content distribution across cohorts (simple column added to existing table)
  - Detailed landing page analysis with impressions, clicks, and position data (to be implemented in overall tab)

### Automation Limitations

  - Direct HubSpot to Looker integration not feasible due to data sampling issues
  - Some automation possible through Airtable exports and VLOOKUP formulas in Google Sheets
  - Looker unable to perform complex data transformations; pre-processing required

### Reporting Focus

  - Emphasis on total lead volume and leads from GrowthX-produced content
  - Monthly reporting becoming more important than weekly for most clients

---

## Action Items

**Jessalynn Jones**
- Create spreadsheets in Teams folder for Webstacks + Tiro HubSpot data. Include column for GX leads indication.

- Contact Webstacks + Tiro re HubSpot exports. Specify fields needed (create date, first page seen, GX lead indicator). Request auto-export to Teams folder spreadsheet.


**Vivek Shankar**
- Fix bar limit issue for all Looker reports to show full historical data.

- Investigate adding monthly view option to Looker reports (overall + cohorts tabs). Consider single chart w/ toggle or separate charts.

- Add count of URLs per category in first table of cohorts tab for content distribution analysis.

---

## Transcript
**Jessalynn Jones:** Hey, good.

**Jessalynn Jones:** How are you?

**Jessalynn Jones:** Good, good.

**Vivek Shankar:** Thanks for taking the time to walk through this today.

**Jessalynn Jones:** I invited Jakub to this as well, so hopefully he can join us in a moment, because I feel like he maybe has a clearer idea of what he wants to get out of these reports. I was just seeing if he messaged me.

**Jessalynn Jones:** But kind of the big thing that we're looking for, which I'm sure you saw in Linear, was just that two of our clients, both Tiro and Webstacks, they really want to be able to see, like, the full pipeline impact of what we're doing, and namely integrating HubSpot is kind of, like, the first step for that.

**Jessalynn Jones:** So, what I'm hoping we can get from you, well, maybe

**Jessalynn Jones:** Maybe we can kind of describe what we're looking for, and then you can tell us what fields you need exported from HubSpot in order to integrate those into Looker, and or what's even possible in Looker, because I think that's like a little bit of an unknown for us too.

**Vivek Shankar:** Yeah, I think it might be faster if we just discuss the WebStacks issue, or not the issue, but the ticket, and then that sheet that you'd sent me, let me get my screen.

**Vivek Shankar:** So this sheet, this thing here, so I'm assuming GX produced blogs is not relevant for reporting purposes, and there's these three tabs, right?

**Vivek Shankar:** So my question was, and you know, just to give more context, the, I think your request was what, no, they just need to track all leads, basically.

**Vivek Shankar:** So, yeah.

**Vivek Shankar:** So the question was, do they want to track overall leads as well as GrowthX leads, right?

**Vivek Shankar:** I think that would be helpful, but Jakub, do you have a different perspective on that?

**Jakub Rudnik:** I think the GrowthX, the leads from GrowthX pages is what we really care about.

**Jakub Rudnik:** They can look at the overall leads in HubSpot thing, so that's where I would focus.

**Vivek Shankar:** All right, so my question was, this leads month on month.

**Vivek Shankar:** I thought this was a formula table, but it doesn't look like it.

**Vivek Shankar:** I mean, this is, yeah, like, does this need to go into reporting as well?

**Vivek Shankar:** Is this like overall, or is this, I don't think this is GrowthX, so do we need this at all?

**Jessalynn Jones:** Yeah, so this is overall leads because for Webstacks, we actually are not getting a ton of leads specific to our blogs, so I was reporting overall leads for them, too. Our other client, Tiro, they get a decent amount of leads, and we basically have produced their entire blog at this point, and so they're all from us, so it makes it a little bit easier. But with Webstacks, my concern is: if we are only reporting Webstacks leads, that's not a lot each month.

**Jessalynn Jones:** Like, we already are not getting a lot of leads directly from the blog, and then if we filter down even further to just leads from GrowthX blogs, it's not a lot, and so I wanted to try to, like, capture the value of just us creating volume on their blog, even if the leads are not coming specifically from our blogs.

**Jessalynn Jones:** I don't know if that makes sense, but I just, I'm concerned that if we show them zero leads, like, each month.

**Jessalynn Jones:** What that might look like.

**Jessalynn Jones:** Yeah, I think that's fair.

**Jakub Rudnik:** They, I mean, some of it's that they don't have any, I guess probably how they're tracking it, and they don't have any conversion points on most of those blogs, and there's just like a bunch of things.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** But I do think like having the same kind of functionality of the traffic, like cohorts of like leads, like a leads page with all Webstacks, Webstacks blog, Webstacks, GrowthX pages, or something like that makes sense.

**Jakub Rudnik:** So you can see the whole scope, because if they're, they don't have leads anywhere on their blog, like that's not just us either, that's a larger picture.

**Jakub Rudnik:** So it is, idea, it would help tell the bigger story regardless.

**Jakub Rudnik:** Okay, cool.

**Jakub Rudnik:** So basically, yeah, that should be easy.

**Vivek Shankar:** Like you're just combining these two tags essentially, and then cohorting in GrowthX versus non-GrowthX.

**Vivek Shankar:** I guess if I understand you correctly, Jessalynn, you're creating.

**Vivek Shankar:** Yeah, so this can be replicated in Looker pretty easily.

**Vivek Shankar:** The next question is, when they send the export, right?

**Vivek Shankar:** Because I'm trying to figure out how to minimize the work for you.

**Vivek Shankar:** When they send the export, does it come in separate tabs like this, lead than GX leads, or is it just one big data dump?

**Vivek Shankar:** It's just one big data dump.

**Jessalynn Jones:** So right now, this GX leads tab is basically a filtered list of the total leads tab.

**Jessalynn Jones:** So I basically just put in a formula that takes GX produced blogs and filters all the leads on the leads tab and then spits it out into the GX only leads.

**Jessalynn Jones:** Does that make sense?

**Vivek Shankar:** Okay, so you look at this first page scene.

**Vivek Shankar:** If it's a GX, if it's one of the blogs we produce, then it's a GX lead, basically.

**Vivek Shankar:** Yeah, exactly. So the process that I'm thinking of is basically, and they'll send this every week, right?

**Vivek Shankar:** And it'll be just, they'll just append it.

**Vivek Shankar:** So for next week or whatever, they'll just append it to this list, right?

**Jessalynn Jones:** So right now, I basically asked them if we could get export access to their HubSpot.

**Jessalynn Jones:** And they said for security reasons, they're not sure.

**Jessalynn Jones:** But they've set up a similar export for one of their other ad vendors.

**Jessalynn Jones:** And it's actually like a 24-hour renewal.

**Jessalynn Jones:** So basically, every 24 hours, it automatically pulls the new leads.

**Jessalynn Jones:** We can tell them what fields we want and in what format.

**Jessalynn Jones:** So I just...

**Jessalynn Jones:** Yeah, the fields and format is not an issue.

**Vivek Shankar:** We can always pull that in. My concern is more like, Looker doesn't do real-time data feeds very well. It'll just break. So we can't connect to HubSpot out of the box because we'll need a special third-party connector for that. That's out of scope.

**Vivek Shankar:** The only way to do this is for you to come in each week and just upload the sheet for that week. Whatever the export is, you just upload it and the Looker page will automatically pull data from whatever sheet you're uploading. Charts are set up and you'll have data presented the way you want it. The easiest way to do that would be for them to send you an export of this sheet with all these leads—basically, the entire list of leads from whatever date we started working together till the current date. And with these fields, or they can include any fields they want. It's fine. And then once the sheet comes in, you'll have to do the GX leads filtering. If this is a URL that we have produced, then maybe a column over here that says GX lead.

**Jessalynn Jones:** Okay, so we can't filter into another tab, you need it all in one tab. Am I hearing that correctly?

**Vivek Shankar:** Yes, correct.

**Jessalynn Jones:** So, I guess my question is, so, I hear you that we can't do a HubSpot direct integration with a live, live updates, necessarily.

**Jessalynn Jones:** But what, what our client was describing was basically, I think it's some kind of, like, API that basically auto-populates a spreadsheet.

**Jessalynn Jones:** So, it wouldn't be, like, direct, it wouldn't be a direct API to HubSpot to look up.

**Jessalynn Jones:** It would be basically some kind of API that basically connects HubSpot to a spreadsheet, and then we could connect the spreadsheet to Looker.

**Jessalynn Jones:** Does that work for live updates, if we have a spreadsheet that's live updated versus directly connecting?

**Jessalynn Jones:** Yeah, that can work.

**Jessalynn Jones:** Okay, so we could automate this as long as it's the same spreadsheet, and the spreadsheet is what's getting the auto-updates versus trying to connect HubSpot directly.

**Jessalynn Jones:** Correct, yes.

**Vivek Shankar:** Yes, and for the cohorts to work, we need this field filled out.

**Vivek Shankar:** They're just letting us know which is the growthx URL, because, yeah, like, we can't build this logic into Looker.

**Vivek Shankar:** Like, Looker is a very basic kind of a tool, and it breaks if you look at it the wrong way.

**Vivek Shankar:** So, yeah, the only thing is we need this column.

**Vivek Shankar:** Filled out.

**Vivek Shankar:** If it's not filled out, it's not a big deal.

**Vivek Shankar:** It'll just go under like a miscellaneous or whatever.

**Vivek Shankar:** So in terms of a process for you, I'm thinking like maybe have a sheet to which they export this HubSpot data to. It can live in the Teams GrowthX folder in Google Drive. They just keep updating it whenever. Reporting happens each week based on whenever you sync with the client. And then before you report, you just fill out whether it's a GX lead or not.

**Jessalynn Jones:** So there will still be manual tagging of what blogs are ours, but otherwise it'll be at least somewhat automated?

**Vivek Shankar:** Yeah.

**Jessalynn Jones:** And Jakub, is there anything else that you want to get out of this besides just straight-up leads from HubSpot?

**Jakub Rudnik:** I mean, leads is like the one that they've asked for, and I have no experience building into Looker, just like the way we have to do it.

**Jakub Rudnik:** I don't know who this question is for, or maybe it's just an idea, just something for us to like look into, but I feel like some of that could be automated in like with Zapier or something.

**Jakub Rudnik:** So like, I don't know what, as we figure out what that process is, potentially we can remove some of that manual work.

**Jakub Rudnik:** I don't know exactly how to do this.

**Jakub Rudnik:** just like, we could do like a VLOOKUP formula that would populate like GX leads or not.

**Jessalynn Jones:** I think, Vivek, do you know, like, is Looker okay with formula fields?

**Jessalynn Jones:** Like, for example, if we have like a lookup.

**Jessalynn Jones:** A formula that basically would mark whether it's a GX blog or not in that field.

**Jessalynn Jones:** Would it read the formula or would it read the output?

**Jessalynn Jones:** Like is Looker able to differentiate?

**Vivek Shankar:** It won't work, Looker, unfortunately.

**Vivek Shankar:** Okay.

**Vivek Shankar:** It just literally takes what you already have and just displays it.

**Jessalynn Jones:** That's it.

**Vivek Shankar:** What you could do maybe is, so I think Suleiman can help this.

**Vivek Shankar:** And this was like, I don't know, Suleiman and I were going to get to this in whatever the next stage is once we're done with these initial requests, but they just keep coming.

**Vivek Shankar:** So what we were thinking of doing was, so to your process, right, you have your Airtable, you have this sheet that's being updated constantly live.

**Vivek Shankar:** You can have a second tab over here, which is GX produced blogs.

**Vivek Shankar:** This can be connected to Airtable.

**Vivek Shankar:** So you can have a script that just pulls it from Airtable.

**Vivek Shankar:** So if.

**Vivek Shankar:** Maintains the latest list of published logs over here, right, in this tab.

**Vivek Shankar:** And then over here, you can have a formula VLOOKUP or an index or whatever.

**Vivek Shankar:** And then, you know, you could run a script, basically, that just updates this URL field at certain predefined timelines.

**Vivek Shankar:** That's how the automation would work.

**Vivek Shankar:** And Looker is just reading this data and showing it as a chart or whatever.

**Vivek Shankar:** I don't know if that makes sense.

**Vivek Shankar:** I can explain it again.

**Jessalynn Jones:** So, I think maybe my original question, maybe I didn't explain it very well.

**Jessalynn Jones:** So we can do VLOOKUP formulas here in the spreadsheet, and Looker will be able to understand the outputs. You're just saying we can't do VLOOKUPs in Looker. So whether it's automation that automatically populates it from Airtable, or whether it's us manually updating that list and then the VLOOKUP formula pulling it, Looker would be able to read that.

**Jessalynn Jones:** So that leads me to another question. We're still manually updating these new Looker reports with formulas. Is there any way of automating that? I'm assuming you guys have already looked into that.

**Vivek Shankar:** Yeah, we did. The problem is that's the reason why the previous Lookers were failing—because if we automate it, we'll need to blend the data.

**Vivek Shankar:** Looker calls it a data blend. It's basically combining the data from Airtable with GSC and GA4, essentially telling Looker that this is the entire world of analytics data that we have, but we only care about these URLs from Airtable, and then it joins them.

**Vivek Shankar:** When we do that join, Looker goes absolutely nuts, and it starts sampling data from GSC and GA4.

**Vivek Shankar:** It doesn't show the absolute numbers, so the numbers are all wrong, which was why the original reports didn't really work.

**Vivek Shankar:** So that's why we had to remove that automation, unfortunately.

**Vivek Shankar:** The closest automation we can have is maybe automating the case statement generation for you, but that's not really much of an addition. It takes us two minutes to generate those things anyway. So unfortunately, no.

**Jessalynn Jones:** Okay, yeah, that makes sense. So when you're talking about automating the list of URLs getting pulled into this spreadsheet from Airtable—

**Jessalynn Jones:** What tool do you use for that?

**Vivek Shankar:** I think you can do it in Airtable. You can have it export to a particular CSV. I think Suleiman can build that script. So if you need that, we can create a separate ticket for it and ask Suleiman about it.

**Jessalynn Jones:** So basically, if we create a spreadsheet in the Teams folder and have them export to that with a column for GX leads indication, that should be enough for you guys to hook this up?

**Vivek Shankar:** You don't even need to have them create the GX leads column. You can create it yourself and just update it as the data comes in.

**Jessalynn Jones:** All right.

**Jessalynn Jones:** Well, sounds good.

**Jessalynn Jones:** And then just like create date and first page scene, and then whether it's a GX lead or not is probably enough.

**Jessalynn Jones:** We probably don't need like name and email even for those leads.

**Vivek Shankar:** It's up to you.

**Vivek Shankar:** If you wish to see the list of people and their emails in Looker, it doesn't make any difference to Looker. Jakub, do you have any instinct on what you would like to see in terms of names, emails, company data, or is it strictly volume?

**Jakub Rudnik:** I just want totals, like we have for what you've exported for Tiro with that graph. That's the simplest form to show month over month so we can see how it's changing and growing. You have those tables at the bottom for other pages. I don't look at the individual URLs there as much, but if we did, I'd have to see the details.

**Jakub Rudnik:** Yeah, I wouldn't care about the, for our purposes, names, industries, it's really just volume.

**Jakub Rudnik:** Maybe if there's some sort of like more macro piece of data in there that we could pull, like if we had fleets by industry stacked, but it doesn't sound like we have the volume to justify like figuring out how to do that at this point.

**Jessalynn Jones:** But that's like the type of thing that I would want.

**Jakub Rudnik:** It's like, they should look at the individual lead more specifically, or just trying to report like blog traffic turned into lead somewhere.

**Jakub Rudnik:** So it's simpler than like Webstacks would use, but for our purposes.

**Vivek Shankar:** If you don't care about the name and email, I would ask them to send us an export from HubSpot for this exact report. We don't need to do any data transformation. HubSpot can easily roll up that data and present it to us.

**Jakub Rudnik:** Yeah, the only thing we would care about is the URL, like the first touch URL. That would be the macro view, then the table below would show all the URLs with the total number and the date, and if that had the cohort like we do with blog traffic, we could add the cohort of GrowthX created content.

**Vivek Shankar:** Okay, in that case, I think their export would contain this, because this is the, like, this is the unique key, basically.

**Vivek Shankar:** So, okay, it's not a big deal either way, I mean, you don't have to display it, so yeah.

**Jessalynn Jones:** So the export might include name and email, but we don't need that in Looker. The takeaway is we want GX versus non-GX cohort views.

**Vivek Shankar:** And at some point, if you want to add fields to this, that's not a problem. You just let us know and we'll add it into the code.

**Jessalynn Jones:** Awesome. Great.

**Jessalynn Jones:** Well, I'll reach out to our clients. For Tiro, I still need to reach out about the export. Webstacks is waiting to hear from us what we want exported, so I'll reach out to them today.

**Jessalynn Jones:** I'll reach out to both of them today and then get you spreadsheet links in the next couple days as soon as they get back to me.

**Jessalynn Jones:** Cool.

**Vivek Shankar:** Sounds good.

**Jakub Rudnik:** All right.

**Jakub Rudnik:** Awesome.

**Jakub Rudnik:** Thanks, Could I pause really quickly before we hang up?

**Jakub Rudnik:** Jesse asked for one other thing.

**Jakub Rudnik:** Do you remember what that was?

**Jakub Rudnik:** I'm, like, in there.

**Jakub Rudnik:** Sorry.

**Jakub Rudnik:** I should probably look this up. There's one other thing I wanted to ask about regarding the cohorts tab.

**Jakub Rudnik:** It's like the old Webstacks rolling report, which is super wide. You can look at a big chunk of time. But here, we're very limited. We can look at maybe six or seven weeks at best, then we can't push any further. It looks like it maxes out at about 10 weeks. When we're looking at all of 2025, it's much easier to tell a story with that scope. I would love to have a tab up here that lets you toggle between week and month. That would help a lot.

**Vivek Shankar:** Actually, I just fixed the bar issue. Can you check it? Try going back to January or something.

**Jakub Rudnik:** Yes, it should work now.

**Vivek Shankar:** I'm looking at it now. It's showing stuff all the way back to November and beyond. It should be good.

**Jakub Rudnik:** That's great! This helps tremendously. There was a 10-bar limit on the chart that was blocking the view. And then having month versus week toggling would be an awesome addition too.

**Jessalynn Jones:** Sorry, can you expand on that?

**Vivek Shankar:** Month as in grouping the bars by month instead of week.

**Jakub Rudnik:** Yeah, exactly. Right now these are all weeks. I would love to see July, June—monthly views. We could even do quarters eventually, but for now month and week would be enough. The thing is, with Webstacks, when we've been sharing the reports we did on Friday, I'm struggling to tell them how much we've grown month over month, and that's what they're looking at.

**Vivek Shankar:** The way Looker works, we can't build a monthly view into the same chart. It won't automatically refilter or reorganize the data by month. It needs to be a separate chart. So if you want monthly, we can duplicate this chart and change the grouping to monthly.

**Jakub Rudnik:** Yeah, so we'd have a weekly and a monthly. Week and month would be enough. If I had this exact same thing duplicated but with months instead, I would want that across the overall and cohorts tabs. I think that would be useful for everyone. Otherwise, this helps tremendously already, but having the month view would be a great next step.

**Vivek Shankar:** And just to understand, you want this only in the cohorts tab, or in overall and everything else?

**Jakub Rudnik:** Both overall and cohorts. We do some reporting at the weekly level, but with Jessalynn's new reporting approach, we're trying to move to monthly level reporting.

**Vivek Shankar:** Okay, let me look into whether we can do it in one chart with a toggle or if we need separate charts.

**Vivek Shankar:** That might be clean. Otherwise we'd end up with massive reports with every single thing.

**Jakub Rudnik:** The date extension solves a lot of this anyway. I wouldn't prioritize the month toggle tremendously, but I think it would be a really good addition. Not completely backlog, but not urgent either.

**Vivek Shankar:** Okay, I'll wait for you with the sheet inputs and so forth. I'll look into the monthly view and fix the bar limit for all the Looker reports. I'll tell Suleiman about it. One more thing—I'm out of office for the next two weeks, so if you have any other requests, especially custom ones like we discussed today, throw them in Linear. I'll spec them out before sending to Suleiman since he knows Looker but not the presentation side. I'll get on this and let you know how it goes.

**Jessalynn Jones:** Thank you so much.

**Jessalynn Jones:** Jakub pulled up our Fathom recording from the meeting last week. It looks like what was requested was adding content distribution across cohorts and a more detailed landing page analysis with impressions, clicks, and position data.

**Jakub Rudnik:** So content distribution across cohorts is the number of articles produced? A pie chart would work, or even a table. We have four or five cohorts, and we can see we've done more website and design content.

**Vivek Shankar:** So in the first table, we could just add a count of the number of URLs in each category. Would that help?

**Jakub Rudnik:** Yeah, that would do it. Smart solution.

**Vivek Shankar:** The second request is for per-URL data. In the overall tab, instead of just sessions and engaged sessions, you'd want clicks, impressions, CTR, and position data—the same table structure but with different columns, right?

**Jessalynn Jones:** Yes, that's what was listed in the chat: conversion tracking from GA4 events and detailed landing page analysis with impressions, clicks, and position data.

**Vivek Shankar:** Okay, let me go through these. The conversion tracking is already there in the GA4 events. Usually when I see that request, clients want to see conversion events from your produced URLs. Is that what was meant?

**Jakub Rudnik:** Yeah, we're talking about adding HubSpot conversions. I think we've already covered that one with the HubSpot integration we just discussed.

**Jessalynn Jones:** Yeah, we were good there.

**Vivek Shankar:** LLM referral tracking by source is in the LLM tab. And for content distribution, we can add a simple column instead of a pie chart to show the count.

**Jakub Rudnik:** Yeah, the main ones I was remembering were the pie chart for content distribution and the extended date range, which we just fixed. The detailed landing page stuff—I think we've covered the key additional requests.

**Jessalynn Jones:** Thank you for pulling that. Really helpful. Well, I'll touch base with our clients again and get those spreadsheets over to you, and I'll send them in Linear.

**Vivek Shankar:** Sounds good.

**Vivek Shankar:** All right.

**Vivek Shankar:** Thank for the time.

**Vivek Shankar:** Thank you.

**Vivek Shankar:** Bye.

**Jessalynn Jones:** Bye.

**Jessalynn Jones:** Bye.
