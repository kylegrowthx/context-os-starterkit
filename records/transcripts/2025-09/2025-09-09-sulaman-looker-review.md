# Sulaman - Looker Review

<metadata>
date: 2025-09-09
time: 14:59 UTC
duration: 29 minutes
organizer: vivek@growthxlabs.com
participants: Sulaman Ahmed, Vivek Shankar
fathom_recording_id: 85947897
fathom_url: https://fathom.video/calls/404546255
share_url: https://fathom.video/share/W6pzFCPkWyffaqNTGGia4v_-xfx2_YXD
source: fathom
enriched_on: 2026-03-02 12:45 UTC
</metadata>

---

## Summary

Vivek and Sulaman reviewed five major Looker dashboard projects: fixing a chart display limitation (7-8 bar constraint) across all client dashboards, updating the Abnormal (Mariana) dashboard to surface clicks/impressions/CTR/position metrics from GSC, building Web Stacks lead visualization with CSV data cohorted by GX-created vs. non-GX URLs, and designing a complex Outreach Lukas dashboard from raw Google Sheet data with lead/meeting counts, UTM distributions, and landing page analysis. Sulaman committed to completing bar chart fixes, Web Stacks visualization, Outreach Lukas dashboard, and a video tutorial on updating Looker data sources by early Friday.

---

## Context

Sulaman Ahmed is a Looker specialist (external partner/consultant) working with Vivek Shankar from GrowthX on various client dashboard projects. The team manages Looker instances for multiple clients including Abnormal (Mariana contact), Web Stacks (Jessalyn contact), Limes, and Outreach Lukas. This meeting was a tactical review of pending ticket work — dashboard updates, data integrations, and new visualizations needed across the client portfolio. Vivek serves as the primary stakeholder/approver and shared his screen to walkthrough specific Looker configurations, data source patterns, and implementation approaches that Sulaman would then execute.

---

## Relevance

**To GrowthX Delivery:**
- Looker dashboard standardization across clients — bar/point display fixes reduce support overhead and improve visual consistency
- CSV and Google Sheet integrations now standard pattern for client data visualization; Sulaman's Web Stacks and Outreach Lukas builds establish reusable templates
- Data integrity concerns surfaced on Outreach Lukas (duplicate rows, categorization inconsistencies) require client-side data cleanup; presentation approach prioritizes transparency over data scrubbing
- Time-period grouping feature (weekly/monthly/quarterly filters) deployed to one dashboard; strong candidate for rollout to entire Looker portfolio if clients respond positively

**To GrowthX Business Development:**
- Expanding dashboard capabilities and data source flexibility increases client stickiness and cross-sell potential for analytics upgrades
- Video tutorial on data source updating enables clients toward self-service maintenance, reducing support burden
- Abnormal (Mariana) project demonstrates responsiveness to client feedback; GSC source switch signals commitment to metric accuracy

---

## Overview

- Multiple client-specific Looker dashboard updates required, ranging from minor tweaks to complex data integrations
- New data source integration needed for Web Stacks client, involving CSV import and custom visualizations
- Outreach Lukas project requires extensive data visualization from a complex Google Sheet, including various charts and tables
- Importance of maintaining data integrity while creating flexible, updateable dashboards for clients

---

## Key Topics

### Abnormal (Mariana) Dashboard Update

- Client using report incorrectly; focus on clicks, impressions, CTR, and position
- Potential solution: Change data source from GFO to GSC for first page
- Update chart to display clicks and impressions
- Modify table to show clicks, impressions, CTR, and position

### Bar Chart Display Limitation Fix

- Issue: Some charts only show 7-8 bars
- Solution: Adjust 'Bars' setting in Style tab to 100-500 for all relevant charts across client dashboards
- Implementation: Change settings in background without notifying clients

### Web Stacks Data Visualization

- New data source: CSV file with lead information (name, email, creation date, page first seen)
- Jessalyn to update sheet with "GX lead" column (yes/no)
- Visualization requirements:
    - Number of leads month-on-month, cohorted by GX or non-GX URL
    - Group data by week or month
    - Challenges in date grouping to be addressed in Looker

### Limes Dashboard Update

- Add "count of landing page" column to cohorts tab
- Include in first and second tables of the cohorts tab

### Time Period Grouping Feature

- New filter added for weekly, monthly, or quarterly data grouping
- Custom parameter and field created for this feature
- Consider deploying to all dashboards if well-received

### Outreach Lukas Dashboard Additions

1. Add session duration to overall tab data
2. Create chart showing sessions vs. views in overall tab
3. Integrate and visualize complex Google Sheet data:
    - Double bar graph: Count of leads and meetings booked per day
    - Raw data table (excluding final column)
    - Table of initial landing pages with count
    - Table of conversion landing pages with count
    - Table of leads and meetings booked per campaign
    - Pie charts for UTM source, medium, and campaign distributions

---

## Action Items

**Sulaman Ahmed**
- Update # of bars displayed in charts for all clients. Go to Style > Bars/Points > Set to 100-1000 across all bar and point charts. Can be done silently in background without notifying clients.

- Create Web Stacks lead data visualization. Upload CSV as data source. Build chart showing # leads month-on-month, cohorted by GX-created URL vs non-GX URL. Group by week or month (Sulaman to decide best approach based on date ranges).

- Outreach Lukas dashboard additions: Add session duration metric to overall tab data. Create second chart in overall tab showing sessions vs views comparison.

- ADA Outreach (Outreach Lukas complex Google Sheet) complete data visualization build. Upload Google Sheet as data source. Create: (1) double bar graph of leads/meetings booked per day, (2) raw data table with all columns except final source column, (3) table of initial landing pages with row count, (4) table of conversion landing pages with row count, (5) table of leads/meetings booked per UTM campaign, (6) pie charts for UTM source, UTM medium, and UTM campaign distributions.

- Create video tutorial showing clients how to update data sources in Looker: add new sheet as data source, delete old data source, update visualizations to reference new sheet.

---

## Transcript

**Sulaman Ahmed:** Okay, so these are the tickets I would like to go over.

**Vivek Shankar:** Abnormal. This is the Mariana one. She's just using the report all wrong. Basically, I responded to her. Did you read my response to her?

**Sulaman Ahmed:** It might be super recent then.

**Vivek Shankar:** I responded to it just an hour ago.

**Sulaman Ahmed:** Yeah, just saw it now. So it's good from our end, we're waiting for their response, right?

**Vivek Shankar:** Yeah, basically, my guess is what she'll come back and tell you is she seems to be only concerned with clicks and impressions and CTR position. So basically, the information that's in the first page, for overall time, I think we just need to change the source from GFO to GSC and display clicks and impressions in the chart. And then in the table, we can show clicks, impressions, CTR, and position. I think that should satisfy her, but let her respond. And then if she says yes, I only want to see this, I don't want to see GFO data, we can change those tables.

**Sulaman Ahmed:** Got it, got it.

**Vivek Shankar:** Okay, let me open the next one. Ah, yeah, this one. This one is pretty easy. So let me share my screen. I'm talking about this one, update the number of bars displayed. This was actually coming up like Jacob was the one who told me there's this limitation. He showed me the cohorts tab. Basically what happens is some of these charts, they only show like seven or eight bars. They don't show more than that. So the way to fix it really is to go and click on the chart and then you go to style. And then you see it will say bars 10, just make this 100 or make this 500. That's it.

**Sulaman Ahmed:** I have to do this for all the clients you have done this dashboard for?

**Vivek Shankar:** So every client, every chart, every bar chart exists. So even here in the style, sometimes you'll see number of points like this. In this case, 500 is fine, but yeah, in this chart, for example, we can see here it's a hundred. I would just make it a thousand just to be safe. So like this, basically every Looker just change it. You don't need to tell anybody, just do it in the background.

**Sulaman Ahmed:** Got it. Yeah. Okay, cool.

**Vivek Shankar:** That's done. The next one is this one, Web Stacks. So this is the Jessalyn one, right?

**Sulaman Ahmed:** Yep.

**Vivek Shankar:** Okay. This was a bit more complex. So basically, let me open this. So the issue here is that they have this CSV. She had included a CSV, right? Oh, it's here. So basically, what's happening is they're receiving this list, right? Just this tab, whatever is in this tab. They're receiving name, email, creation date, page first seen, and GX lead, yes or no. They just want to visualize this. That's it. So what the client is going to do is they'll keep updating this sheet. They will create the sheet in the team's Google Drive. And then they'll keep doing a live export to this each week. So it'll just keep adding rows over here each week. And what they want is they want to visualize. There is simple stuff like number of leads, leads based on month, broken down by date, et cetera. This is the confusing bit. They want to know whether the lead, this first page seen, they want to know if this URL is a GrowthX-created URL or not. So their export will only have these four columns. So what I told Jessalyn is this final column, GX lead, yes or no, she needs to fill it out herself.

**Sulaman Ahmed:** So she'll fill out yes, no, yes, no, whatever.

**Vivek Shankar:** And then we basically create a data source. Like we upload this sheet as a data source. And then we just use these charts. So that's what I'm saying. A client will send one sheet with all conversions data and live exported, right?

**Sulaman Ahmed:** Got it. So we just want to utilize, out of all those leads, which are from GrowthX, which are not from GrowthX, and they will be grouped based on the weeks.

**Vivek Shankar:** Correct. Got it. I'll figure that out. So your x-axis will be grouped by week. That's the tricky bit because they're sending August 19th, August 1st. You can do it monthly, actually, or weekly. I'll leave it up to you. But basically, we kind of need to figure out, like, okay, all of these are in one week, right? All of these are in one week. This is another week. So this grouping needs to happen somehow.

**Sulaman Ahmed:** And we have to do this in Looker.

**Vivek Shankar:** Like, we can't do it in the sheet. Understood. So try playing around with this. My guess is this is going to be a little complex for you to figure out. One way of doing it is usually if you upload the sheet, you can usually create fields and parameters over here. To sort of group that. So for example, you have this date, right? We'll pull in this create date field, for example. So let's say this is create date. You can customize it over here. So you can say display, display format, and then you can say custom format or whatever. I'm trying to see if there's a better example I could show you, which isn't date. I don't have one right now, but play around with it. I think you can customize it.

**Sulaman Ahmed:** I understand.

**Vivek Shankar:** Cool. Next one. So this whole ticket was just regarding this grouping, right?

**Sulaman Ahmed:** Oh, sorry.

**Vivek Shankar:** Let me cover the list. Yeah, that was pretty much it. So there were others as well. This first one is just dealing with the sheet. The next one is the Abnormal sheet — detailed landing page analysis with impressions, clicks, position data. So yeah, basically replicate the main table in overall tabs, switch to GSC, add columns. So basically what we're doing for Mariana, same thing. But Jacob said, just put it under this table, under this chart.

**Sulaman Ahmed:** So the second table would be what we have mentioned there?

**Vivek Shankar:** The second chart will be what we've mentioned. Got it. And then this one is pretty straightforward. Limes wants to see number of URLs per cohort. So in the cohorts tab, add a column in the first and second table, count of landing page. So basically we go to the cohorts tab, this table and this table. You just add a column of landing page and then just a count.

**Sulaman Ahmed:** Got it.

**Vivek Shankar:** This non-GrowthX is 500 pages, et cetera. Actually, you know, I'll just do this here. It's pretty easy. So it says CTD next to landing page.

**Sulaman Ahmed:** Yep.

**Vivek Shankar:** So CTD means count, basically. There's something weird going on, non-GrowthX URL 500, non-GrowthX URL 482. Something is wrong with the way they're categorizing, I think. Because these things are not adding up. Website design 52, website design 27. I think what's happening is they're updating GA4, they're not updating GSC. Let me just respond to this. And this weekly, quarterly, monthly thing, I've already done it. Go to the first page. You see like now they can basically filter or group this data based on quarterly or monthly. So previously it used to show only weekly, right?

**Sulaman Ahmed:** It would show only weekly.

**Vivek Shankar:** Now you click this, they can switch to a month, cohorts by month, or quarter by quarter based on this data. So I've deployed it here. If they like it, I think we should deploy this to every dashboard because this is actually very useful.

**Sulaman Ahmed:** So it would be just on this new filter, and the tables would be the same?

**Vivek Shankar:** Well, no. It's a bit more complex. This thing requires some customization. So basically, what I did is I created this custom parameter, and then I created a custom field with a formula over here. So there's like two, three steps that we need to do for this. But anyway, I've deployed it to one dashboard. Any other questions about this?

**Sulaman Ahmed:** I think I'm good for it right now. I will give it a try and if I get stuck somewhere, I'll reach out to you.

**Vivek Shankar:** All right, next one. Additions to Outreach Lukas. Ah, yeah, this was the one. So the first two are pretty easy. So basically, add session duration to the data in the overall tab. So basically, this table just needs session duration over here under the metric. And then add a chart showing sessions versus views in the overall tab. So again, like how we're doing for the other client, we just need a second chart below this that shows sessions and views. What you can do is maybe remove Engaged Sessions and just use Sessions. And then the third one, this is a pain. So basically, they have a sheet, which is this one, right? So basically, they have this sheet over here and it has a lot of data. So it has name and a ton of stuff. But basically, we need to visualize all of this. So it's the same as the previous issue. But it's just that we have more data over here. So you can just follow the steps. Number one is basically telling you how to do number one. Number two is telling you how to do number two. Number two is done already. So you can ignore this. Number three is where it gets complex, and we have to come up with ways to visualize this. These are just some ideas I have. If you have other ideas, please let me know, and you can build it as well. But basically, we need a count of leads and meetings booked per day as a double bar graph. So basically, that same sessions and views chart, but it will show meetings and leads as two series. X-axis is the date. So if you look at the sheet, we have dates here. All of these are dates. And then we have meeting and lead booked. So if it is one, it means meeting booked. If it is zero, it's just a lead, right? But here's the thing. Every entry in the sheet is a lead. And meetings booked, only if this is one, then it's basically like a meeting booked. So in this instance, this row should show up in lead and meeting.

**Sulaman Ahmed:** In the third row, we can see it's the same person that we have got against the leads, like seven or eight leads. And one of them is meeting booked. But it's the same person, like Zubair Chaudhary, from five up to 16.

**Vivek Shankar:** Yeah, I don't really know what's going on here. Date is the same. All of these are the same. Yeah, it seems like every data is the same, but for some reason, the rows are being duplicated.

**Sulaman Ahmed:** Got it. Then shall we remove duplicates first?

**Vivek Shankar:** No, because basically what I want to give them is like every week the GrowthX team can just upload the sheet and that's it. Like they don't need to do any customization because I don't think the pod in charge of this team will be able to do all this.

**Sulaman Ahmed:** Got it. Yeah.

**Vivek Shankar:** This is more of a data quality thing. So basically, yeah, leads and meetings, x-axis date, y-axis is a count, count of all rows and meetings per day. So then below that, a table of the raw data, which is just the sheet. So every column in the sheet, this is where they can know that, okay, their data is corrupt. I think all their leads are just one guy. It's a data quality issue on their end.

**Sulaman Ahmed:** I understand.

**Vivek Shankar:** So the raw table includes date, session duration, name, email, initial landing page, conversion page, website URL visited, UTM source, UTM medium, and UTM campaign. The final column we don't need. So then the third one is a table of initial landing page and count of rows. Yeah, so this is basically showing which landing page is the most popular. So we show this initial landing page column, number of rows per landing page. So it's just a count of these rows.

**Sulaman Ahmed:** Right.

**Vivek Shankar:** And then table of conversion landing page, count of rows. So it's the conversion page URL. Just URLs and count. And we want a count of them, not a bar graph.

**Sulaman Ahmed:** Correct. It's a table. So two columns.

**Vivek Shankar:** Got it. And then a table showing number of leads and meetings booked per campaign. So again, table, you have campaign ID, they have a field here, this UTM campaign name, number of leads, which is a count of rows, and meetings booked will be wherever there's a one. So first column, campaign name, second column, count of leads, third column, number of meetings booked. And then pie charts, UTM source distributions. So UTM source is this one, yeah. This is a simple thing, it was just a pie chart. Basically, Google and whatever, just a distribution of all the values. My guess is this is going to be counted as a separate source, but can't help it. And then same thing for the medium and same thing for the campaign. So three pie charts — one for the source, one for the medium, and one for the campaign. And that's it. So if we do it like this, we don't need any custom fields, and the team can just upload the sheet as is. We can have a date control field on top.

**Sulaman Ahmed:** Shall I upload that sheet to a Google Drive and link that Google Sheet with our local dashboard so that they can update that Google Sheet? Or where do you want them to update?

**Vivek Shankar:** No. They will receive a Google Sheet. So each week, whenever they receive it, they'll go to manage data sources. They'll just add the new sheet as a source.

**Sulaman Ahmed:** Got it, got it. And then they would know the pattern in which the sheet should be, based on the sheet we will be using. And they can then follow the same pattern of that sheet.

**Vivek Shankar:** Yeah, their exports will be in exactly this pattern. Got it, got it. And when you finish this task, please include a video that shows how to update the data source.

**Sulaman Ahmed:** Got it, got it, we'll definitely do that.

**Vivek Shankar:** Yeah, so their data source, there'll be a sheet over here. You need to tell them like, okay, first of all, add a data source, add the Google Sheet, right, and then delete the old data source. That is important. They need to delete it.

**Sulaman Ahmed:** Got it.

**Vivek Shankar:** And then if they do it the right way, it should pick up the new sheet automatically as a data source. But well, actually, they'll need to change the data source, I think. So whenever you've created the new tab, they will need to hit edit and change the data source to the new sheet. Anyway, just include it in your tutorial.

**Sulaman Ahmed:** Got it. I think that's it. Yeah, that should be helpful. All right.

**Vivek Shankar:** Cool.

**Sulaman Ahmed:** Thank you so much, Vivek. I will start with this, and I'll let you know in case I need some guidance.

**Vivek Shankar:** Yeah. Just let me know by early Friday because I'm off.

**Sulaman Ahmed:** I'm here. Sure. Okay. Thank you so much for the guidance. Have a nice day.

**Vivek Shankar:** Bye now.

**Sulaman Ahmed:** Bye.
