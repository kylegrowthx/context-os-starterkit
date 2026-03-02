# DG agenda creation  + Looker update overview

<metadata>
date: 2025-10-30
time: 17:25 UTC
duration: 36 minutes
organizer: nathan@growthx.ai
participants: Nathan Navidzadeh, Nika Narimanidze
fathom_recording_id: 98097791
fathom_url: https://fathom.video/calls/459457883
share_url: https://fathom.video/share/3ZafjxKVshzKbeewUBBVPu2GDUagmcrd
source: fathom
enriched_on: 2026-03-02 15:30 UTC
</metadata>

---

## Summary

Nika walked Nathan through the complete weekly agenda creation process for DataGrid, covering both Looker data source updates and Notion agenda population. The workflow starts with updating Looker's GA4 and Google Search Console data sources using regex formulas to capture newly published articles, then analyzing weekly performance metrics (Oct 20–26) to populate the agenda with key findings on traffic trends, keyword rankings, and content cluster performance. Nathan committed to completing the TLDR summary while Nika finalizes the full agenda for stakeholder review.

---

## Context

This is an internal GrowthX training session for the DataGrid content marketing workflow. Nika Narimanidze, who manages the weekly reporting and agenda creation process, is teaching Nathan Navidzadeh how to execute this task independently. The meeting captures a hands-on walkthrough using real Looker data and a live Notion agenda document. This is part of GrowthX's delivery process for DataGrid—a strategic client engagement focused on AI content and SEO visibility. The weekly agenda documents form the basis of sync meetings with stakeholders (Tiago and Caitlin) and require both technical precision in data pulls and clear communication of performance trends.

---

## Relevance

- **To GrowthX Delivery:** Formalizes the weekly agenda creation and DataGrid reporting process. Nathan now has a repeatable workflow for data pulls, analysis, and documentation. Future weeks will require only verification and minor template adjustments, freeing Nika for higher-level strategy work.

- **To GrowthX Business Development:** Shows strong operational maturity on DataGrid account. The sophisticated Looker setup and detailed weekly analytics position GrowthX as a data-driven partner. Weekly reporting rigor reinforces retention and expansion potential.

---

## Overview

- **Looker Update:** Add new article URLs to Looker's GA4 (slugs) and GSC (full URLs) data sources via regex to ensure accurate weekly reporting.
- **Weekly Reporting:** Analyze performance for the prior Monday–Sunday (Oct 20–26) to capture a full week of data, using only Organic & Referral traffic.
- **Key Findings:** Overall sessions declined slightly, driven by a drop in Google traffic. A key win was a +8 increase in \#1 non-branded keywords (to 273).
- **Content Strategy:** New clusters (e.g., AI at Scale) are attracting impressions, while some previously strong clusters (e.g., AI Agents for Healthcare) saw a decline, requiring further observation.

---

## Key Topics

### Looker Data Source Update

  - **Goal:** Add new article URLs to Looker's data sources to enable accurate weekly performance tracking.
  - **Process:**
    1.  Log in to Looker using Kim's account (required for access).
    2.  Navigate to the `DataGrid` space → `Edit` → `Manage Edit Data Sources`.
    3.  **GA4 Update:**
          - Edit the GA4 data source → find the field with the `fx` icon.
          - Generate regex for new article slugs and their `template category` using the Teams ChatGPT prompt: "This is a GA4 Regex formula, and I have to update more URLs and categorize, just like a ball."
          - Paste the regex into the field. Correct formatting is confirmed by the color-coding.
    4.  **GSC Update:**
          - Edit the GSC data source → find `URL List 5` with the `fx` icon.
          - Generate regex for the full URLs of new articles using the Teams ChatGPT prompt: "now we are doing this for GSC, and the format that I need here is URLs are the same."
          - Paste the regex into the field.

### Weekly Performance Analysis

  - **Goal:** Analyze Looker data to populate the weekly agenda document.
  - **Global Filters:**
      - **URL Cohorts:** Untick `non-growthx URLs` to focus on owned content.
      - **Date Range:** Prior Monday–Sunday (e.g., Oct 20–26) to capture a full week.
      - **Mediums:** Select `Organic` and `Referral`.
  - **Key Findings (Oct 20–26):**
      - **Overall Performance:** Slight session decline.
          - **Driver:** Reduced Google traffic.
          - **Counter-Trend:** ChatGPT traffic increased.
      - **Non-Branded Keywords:**
          - Impressions: Slightly down.
          - Clicks: Stable.
          - \#1 Rankings: **Increased by 8** to 273.
      - **Content Cluster Performance:**
          - **Declining:** AI Agents for Healthcare, Insurance, and Law.
              - **Significance:** This is the first decline after 4 weeks of growth.
              - **Action:** Observe for another week to confirm if it's a trend or anomaly.
          - **New Clusters Attracting Impressions:** AI at Scale, Customer Intelligence, Sales Acceleration, and Proposal & Project Management.
          - **Growing:** AI Agents for Marketing, Mining, Finance, and Transportation.
      - **LLM Traffic:**
          - **Growth:** ChatGPT and Perplexity.
          - **Decline:** Gemini.

---

## Action Items

**Nathan Navidzadeh (GrowthX)**
- Add TLDR to Sync 45 Notion agenda

**Nika Narimanidze (GrowthX)**
- Finalize Sync 45 Notion agenda: add LLM, proofread, send to Tiago + Caitlin

---

## Transcript
**Nathan Navidzadeh:** The week's been good.

**Nathan Navidzadeh:** It just feels like I was doing article generation through the Agentec pipeline thinking it was good, and then I started fact-checking and realizing there's a lot of issues with the research step, a lot of issues with the fact-checking step, and so the article's no good because it takes too much work to go in and check 20 different references.

**Nathan Navidzadeh:** So then I have to revisit, okay, how are we going to do this using Claude and the old pipeline and trying to improve that, and so I'm back to, it feels like I'm back to square one since this afternoon.

**Nika Narimanidze:** Yeah, the main issue right now is that it generates false facts through a research pipeline grid.

**Nathan Navidzadeh:** Yeah.

**Nika Narimanidze:** Okay, let's do this, Nathan.

**Nathan Navidzadeh:** So we're going to create the agenda, so the, I think it's the sync 45 that will be this time.

**Nathan Navidzadeh:** Notion, and then we're going to update Looker, or I don't know exactly what we have to do with Looker, but that was one step that you said we have to do, usually.

**Nika Narimanidze:** Yeah, that's the first thing that we should do when we are working on creating agendas, but let's go through the meeting files first.

**Nika Narimanidze:** Yes.

**Nika Narimanidze:** So you can just go here, duplicate this meeting.

**Nika Narimanidze:** Once it's duplicated, I suggest to delete the guests, because if you duplicate it, the invitations we're going to send.

**Nika Narimanidze:** But once you fill in everything, once we get final, applies to the document, then you can just type Tiago and Caitlin there.

**Nika Narimanidze:** Okay.

**Nika Narimanidze:** So basically, we should change this.

**Nika Narimanidze:** Let's call it 45, and let's just randomly pick.

**Nika Narimanidze:** The icon, not going to think too much, and then you can customize the color that you want.

**Nika Narimanidze:** So let's stick with this.

**Nika Narimanidze:** Then let's change the event time, and I think it should be tomorrow, right?

**Nika Narimanidze:** It's 31, Friday.

**Nika Narimanidze:** Okay, so once it's changed, then we will delete the old URL of Fathom recording.

**Nika Narimanidze:** And now let's.

**Nika Narimanidze:** Let's move to the Looker.

**Nika Narimanidze:** Basically, are logging in using the Kim's account.

**Nika Narimanidze:** Just note, because personal accounts, they do not have the accesses to Looker.

**Nika Narimanidze:** Let's go to the data grid.

**Nika Narimanidze:** This is the relevant space for us.

**Nika Narimanidze:** And the first thing that we should do is to go to edit button here.

**Nika Narimanidze:** Just click on this.

**Nika Narimanidze:** And once this floats, you should visit the region.

**Nika Narimanidze:** Resource here and click the first button, Manage Edit Data Sources.

**Nika Narimanidze:** This is the space where we centralize all our data.

**Nika Narimanidze:** So look, here is the data platform that unites data we have in Google Search Console and Analytics.

**Nika Narimanidze:** So we have GCS and Plus Analytics GA4 as well.

**Nika Narimanidze:** So let's head here.

**Nika Narimanidze:** And an important note is that once we update the base with newly published articles, we should update the GA and Search Console base as well.

**Nika Narimanidze:** So let's start with GA.

**Nika Narimanidze:** We should click on Edit.

**Nika Narimanidze:** And I know there's like tons of sections here, but you will need the one with FX on the right side.

**Nika Narimanidze:** This is a space where our URLs are centralized.

**Nika Narimanidze:** And basically, we should pick.

**Nika Narimanidze:** The latest one.

**Nika Narimanidze:** So you click on the fx icon, and you will see a bunch of URLs here, Nathan.

**Nika Narimanidze:** So our mission is to create the Regex formula and add newly published articles in database.

**Nathan Navidzadeh:** So these will be the articles that were published last Friday?

**Nika Narimanidze:** Yes, these will be articles that went live last week, last Friday.

**Nika Narimanidze:** So let's go to the air table and let's go to DataGrid.

**Nika Narimanidze:** And let's head on published pages.

**Nika Narimanidze:** Also important, even though these articles, refreshes, were published last week, we do not update this in Looker.

**Nika Narimanidze:** We only put the new URLs.

**Nika Narimanidze:** So this means that we need to make sure whenever you create the ticket to tell Suleman to update the URL field as well.

**Nika Narimanidze:** But basically, as mentioned last week, I will create the onboarding document for you where I'm going to go through the details that we would need.

**Nika Narimanidze:** So basically, we need to include the stack.

**Nika Narimanidze:** Let's copy all the editorials.

**Nika Narimanidze:** Check it just to make sure he didn't use a different slide by accident.

**Nika Narimanidze:** Yes, we can check it.

**Nika Narimanidze:** We also can check whether the URLs are live or not.

**Nika Narimanidze:** So let's find slugs.

**Nika Narimanidze:** Oh, it's better to open.

**Nika Narimanidze:** This in full screen mode.

**Nika Narimanidze:** So first is improve CRM data, improve CRM data, it's correct.

**Nika Narimanidze:** Six strategies, it's correct.

**Nika Narimanidze:** Simple guide customer lifetime value, it's correct.

**Nika Narimanidze:** I think all good, Nathan, do you notice something abnormal?

**Nathan Navidzadeh:** Yeah, it looks good.

**Nika Narimanidze:** Yeah, okay.

**Nika Narimanidze:** Let's copy this.

**Nika Narimanidze:** Maybe open the spreadsheet here.

**Nika Narimanidze:** Once I open the spreadsheet, I have to check the categories of these articles.

**Nika Narimanidze:** So I copy template categories.

**Nika Narimanidze:** Look, this field is called template category, and I copy the cluster data, and I put this in here.

**Nika Narimanidze:** Okay, so let's go to the chat GPT.

**Nika Narimanidze:** Then go here, and you see this chat, it mentions the code.

**Nathan Navidzadeh:** Is this just the Teams ChatGPT or PodA?

**Nika Narimanidze:** This is Teams ChatGPT.

**Nika Narimanidze:** And basically, we can copy the example that's correct.

**Nika Narimanidze:** I always try to give it the example again, because sometimes it loses the context and gives you wrong code.

**Nika Narimanidze:** So just say that this is GA for Regex formula, and I have to update more URLs and categorize, just like a ball.

**Nika Narimanidze:** And then you can basically copy this.

**Nika Narimanidze:** And paste it here.

**Nika Narimanidze:** Why is it so slow?

**Nika Narimanidze:** You do not have to validate from here whether the formatting is correct or not.

**Nika Narimanidze:** Just copy.

**Nika Narimanidze:** Go here and paste it.

**Nika Narimanidze:** If you see that the colors are matching, basically, it means that the formatting is correct.

**Nika Narimanidze:** If the formatting is off, then you're going to quickly notice because these ones won't be colored anymore.

**Nika Narimanidze:** So no need to double check manually.

**Nika Narimanidze:** Delete the blank space here and we can click on Update.

**Nika Narimanidze:** Okay.

**Nika Narimanidze:** We are set for the GA4 data.

**Nika Narimanidze:** Let's go back and then select Search Console.

**Nika Narimanidze:** This is Search Console.

**Nika Narimanidze:** I click on Edit.

**Nika Narimanidze:** and I go to URL List 5 and I click on FX.

**Nika Narimanidze:** Okay, so what we're going to do right now is I'm going to copy the Search Console format, and here we can say now we are doing this for GSC, and the format that I need here is full URLs.

**Nika Narimanidze:** And just to make sure that nothing gets highlighted, let's just paste it.

**Nathan Navidzadeh:** Oh, no.

**Nika Narimanidze:** Well, it's weird. You copied the blank space for some reason. I have to restart to get the latest Mac update.

**Nathan Navidzadeh:** Okay, thank you.

**Nika Narimanidze:** Thank you. It had some weird issues until you restarted.

**Nathan Navidzadeh:** So now it should generate them in the new format for GSC.

**Nika Narimanidze:** Basically, the difference is that GA only includes slugs.

**Nika Narimanidze:** And the Search Console gives you the full URL. That's the only formatting difference you can quickly notice.

**Nika Narimanidze:** And as you see, everything looks good. You can click on Update. That works. Let's go back.

**Nika Narimanidze:** And just quickly, I'll open the agenda file.

**Nathan Navidzadeh:** So that's what you do for Looker?

**Nathan Navidzadeh:** That's it?

**Nathan Navidzadeh:** Or are we going to take a screenshot, something like that?

**Nathan Navidzadeh:** Or is that the stuff that...

**Nika Narimanidze:** But we then need to put the proper dates and check appropriate fields here to create the agenda.

**Nika Narimanidze:** Can you see it?

**Nika Narimanidze:** Or should I?

**Nika Narimanidze:** No, no, no.

**Nika Narimanidze:** It's too much.

**Nathan Navidzadeh:** I can't read it, but I can see it.

**Nika Narimanidze:** There we go.

**Nika Narimanidze:** That's good.

**Nika Narimanidze:** Okay, this is the overall performance field.

**Nika Narimanidze:** And here what we should do first is go to URL cohorts and make sure to untick non-growthx URLs because we only track the performance of the content that we produce.

**Nika Narimanidze:** We do not track this sidewise.

**Nika Narimanidze:** We do not include home page and everything.

**Nika Narimanidze:** So let's untick this.

**Nika Narimanidze:** Then change the dates.

**Nika Narimanidze:** The first interaction with DataGrid was in 2024, December 30.

**Nika Narimanidze:** And here, as the end date, we should choose the Sunday.

**Nika Narimanidze:** The latest Sunday of the week.

**Nathan Navidzadeh:** Okay, so we don't bring it all the way up to today.

**Nika Narimanidze:** No, no.

**Nathan Navidzadeh:** Okay.

**Nathan Navidzadeh:** It's only two days after publication.

**Nika Narimanidze:** Exactly.

**Nika Narimanidze:** And then we should click on Apply.

**Nika Narimanidze:** And when it comes to mediums, we should select Organic and Referral.

**Nika Narimanidze:** For DataGrid, just remember that it's Organic and Referral, because we also track the AI visits.

**Nika Narimanidze:** So everything is updated here, Nathan, and you can see the latest stats.

**Nika Narimanidze:** And this is basically the latest one.

**Nika Narimanidze:** From October 20 to October 6.

**Nika Narimanidze:** So the first thing that we notice is that the sessions has declined slightly.

**Nika Narimanidze:** We can use this point to include in the agenda, or even you can say that performance was within the expected range.

**Nika Narimanidze:** But I would rather say that it was a slight, slight decline.

**Nika Narimanidze:** So let's...

**Nika Narimanidze:** We should mention this point in performance update field here.

**Nika Narimanidze:** But before we go to performance update, let's go through the details here.

**Nika Narimanidze:** So as of general updates, we will say that article generation is going as planned, because I think I have provided the articles, Usman is on track, and you're also on track.

**Nika Narimanidze:** We have finished deleting the broken internal links.

**Nika Narimanidze:** So we can say that this...

**Nika Narimanidze:** task has been finished, so let's change this, and say we, you can later proof edit, like, and change the phrasing, but yeah, let's leave this like this, we claim broken internal links of current articles, then we are working on the newsletter outline and design templates, I don't know the status of this process, did anybody mention this in our chat, because Andy's handling it, and yeah, and she opened up a ticket, and they're waiting on something from them, but they are doing, we're doing something, I don't know, I guess she made a ticket, okay, okay, we can, we can keep this point, as it is, and then we mentioned data grid product demo, this should have happened last week, it didn't happen, and nobody has brought up anything, so I will delete this, but if there is some news, but it, maybe we'll be back with

**Nika Narimanidze:** But I have not read anything in public channel.

**Nika Narimanidze:** Have you noticed any updates in public channel that needs to be mentioned here?

**Nika Narimanidze:** I didn't check the channel as much because I had plenty of time.

**Nathan Navidzadeh:** So we did, like, on Monday, the Monday updates.

**Nathan Navidzadeh:** All that we said was that we sent the updated contract with newsletter wording.

**Nathan Navidzadeh:** That's our weekly goal.

**Nathan Navidzadeh:** And then an update.

**Nathan Navidzadeh:** We published five editorial, six refreshes.

**Nika Narimanidze:** And then there was a bunch of action items.

**Nika Narimanidze:** And that was it.

**Nika Narimanidze:** Okay.

**Nika Narimanidze:** And Caitlin had some questions.

**Nika Narimanidze:** He has answered it.

**Nathan Navidzadeh:** And there was no follow-up conversation.

**Nika Narimanidze:** Okay.

**Nika Narimanidze:** Okay.

**Nika Narimanidze:** Maybe we keep this point and we squeeze it somewhere about the newsletter wording and updating the contract.

**Nika Narimanidze:** We have published five new editorials last week.

**Nika Narimanidze:** True.

**Nika Narimanidze:** We refreshed six articles last week.

**Nika Narimanidze:** How many was lined up for this week?

**Nika Narimanidze:** think it should be six because they...

**Nika Narimanidze:** Okay.

**Nika Narimanidze:** Let's leave it like it is.

**Nika Narimanidze:** Is there any progress about the PSCO from DataGrid?

**Nika Narimanidze:** I see that they didn't mention anything, so it just tastes as it is.

**Nika Narimanidze:** Okay.

**Nika Narimanidze:** Let's go to the performance update then.

**Nika Narimanidze:** Here we should say that they should limit the date to October 26th, because that's the date of the Sunday.

**Nika Narimanidze:** Yeah, yeah, yeah.

**Nika Narimanidze:** That's the Sunday.

**Nika Narimanidze:** And the first thing that we see here, we have the screenshot of overall performance.

**Nika Narimanidze:** So basically just, we will go there and take a screenshot of this.

**Nika Narimanidze:** Okay.

**Nika Narimanidze:** Okay.

**Nika Narimanidze:** Then delete the old image and list it here.

**Nika Narimanidze:** Okay.

**Nika Narimanidze:** That's a good one.

**Nika Narimanidze:** And the first point is that we've seen like slight decline compared to last week.

**Nika Narimanidze:** And then I say that it was primarily due to reduced performance from Google, though ChatGPT traffic increased.

**Nika Narimanidze:** So let's check the sources.

**Nika Narimanidze:** We can scroll down and you'll see sessions by referrer and we can quickly check that it's 527. Google traffic has declined and Bing traffic also slightly declined, but ChatGPT traffic has increased. So we can say the decline was primarily due to reduced performance on Google.

**Nika Narimanidze:** Okay, this point is set.

**Nika Narimanidze:** Then, as you see, we talked about non-branded impressions that are slightly down.

**Nika Narimanidze:** And then we say that we are ranking number one for this much of non-branded keywords.


**Nika Narimanidze:** Okay.

**Nika Narimanidze:** Let's go to the non-branded traffic.

**Nathan Navidzadeh:** Yeah, here.

**Nika Narimanidze:** This is the non-branded performance.

**Nika Narimanidze:** This is the time frame for us to look at.

**Nika Narimanidze:** And as you see, the impressions, non-branded impressions, also have been slightly declined.

**Nika Narimanidze:** And clicks, they are within the same range, like not much of difference.

**Nika Narimanidze:** So we can mention this in the sub-bullet.

**Nika Narimanidze:** But let's quickly go to this.

**Nika Narimanidze:** And here, Nathan, we have non-branded query ranking distribution.

**Nika Narimanidze:** And you can go to October 26, and we see that 273 keywords are ranking as number one.

**Nika Narimanidze:** Oh no, it has been improved.

**Nika Narimanidze:** So let's change this number.

**Nika Narimanidze:** Write this.

**Nika Narimanidze:** Yeah, this point.

**Nika Narimanidze:** Stays the same because it was a slight decline for non-branded impressions.

**Nika Narimanidze:** And Nathan, can we jump on content?

**Nathan Navidzadeh:** Should we say that in parentheses, that's, I don't know, what was it before?

**Nika Narimanidze:** We do not typically report this.

**Nika Narimanidze:** It was 85K, and now it's 82K.

**Nika Narimanidze:** But it's up to you.

**Nika Narimanidze:** But we do not usually put this.

**Nathan Navidzadeh:** Yeah, number one pages, I mean.

**Nathan Navidzadeh:** Because that's just, that looks like a good win.

**Nathan Navidzadeh:** So go back to the doc.

**Nathan Navidzadeh:** To the doc?

**Nika Narimanidze:** Yeah, to the notion.

**Nika Narimanidze:** And then just undo the 273.

**Nika Narimanidze:** Because what was it before 273?

**Nathan Navidzadeh:** This is non-branded keywords. Before it was 265, so it's increased by 8.

**Nathan Navidzadeh:** So we could say eight more compared to last week.

**Nika Narimanidze:** Of course, we can indicate like this.

**Nika Narimanidze:** Okay, and then you see we have the content categories, but I want to go through all the details here before we jump on content categories.

**Nika Narimanidze:** So here we have conversion events, and we do not track this.

**Nika Narimanidze:** So you can always ignore conversion events.

**Nika Narimanidze:** In case it changed, then we can go back to this.

**Nika Narimanidze:** Then we have cohorts, which are our content categories. So what we should do is go to the cohort section and untick non-growthx URLs.

**Nika Narimanidze:** And then here, as we mentioned, we need to select Organic and Referral, and then we have to set the timeframes.

**Nika Narimanidze:** Here, Nathan, I typically set a week timeframe, but even if you do not change this, you have this chart here for the last week.

**Nika Narimanidze:** But we need to update this, because when we scroll down, you'll see that this demonstrates the session change from periods to period.

**Nika Narimanidze:** So basically, I should go up and select October, and it will be from Monday to Sunday.

**Nika Narimanidze:** Then I click on Apply.

**Nika Narimanidze:** Once I do this, the period-over-period percentages will be correct.

**Nika Narimanidze:** So this is the important step, just to let you know.

**Nika Narimanidze:** And here you can see which clusters have been performing well.

**Nika Narimanidze:** You can quickly check from here or even scroll down.

**Nika Narimanidze:** Yeah.

**Nathan Navidzadeh:** That percent change, the delta there, is comparing October 20th to 26th to what?

**Nika Narimanidze:** It's comparing from last Monday to last Sunday.

**Nika Narimanidze:** Yes, but usually here we tend to track the click changes rather than sessions because it's comparative performance.

**Nika Narimanidze:** And here also we have the data of average position.

**Nika Narimanidze:** That's why we prefer to report on clusters.

**Nika Narimanidze:** And here we can see which clusters were performing well and which were not. We just have to go through the numbers. We can also download this data.

**Nika Narimanidze:** So let's click on export, go to Google Sheets.

**Nika Narimanidze:** We can quickly set the filters.

**Nathan Navidzadeh:** I want to see how you're doing it, so you exported it.

**Nika Narimanidze:** The menu section here above these metrics, I click there, then I click on export data and work on Google Sheets.

**Nika Narimanidze:** And we can sort this in descending order.

**Nika Narimanidze:** Basically, the data that you see here means that nothing has been changed, or it has insufficient data to track it.

**Nika Narimanidze:** But what we can see right now is that productivity tools and techniques had improved clicks, but this cluster is typically underperforming because it received six clicks, and it had this much improvement.

**Nika Narimanidze:** And then we can go through the data, non-growthx URLs.

**Nika Narimanidze:** And this has been declining.

**Nika Narimanidze:** For example, AI agents for healthcare and insurance were going on an upward trend for three or four consecutive weeks.

**Nika Narimanidze:** These articles that were performing well last week have declined.

**Nika Narimanidze:** We need another week to observe the trend because it might be seasonal or topic-dependent.

**Nathan Navidzadeh:** What would you update now in the Notion agenda?

**Nika Narimanidze:** AI agents for healthcare and insurance have declined, even though they were performing well previously. Government clusters continue to perform.

**Nathan Navidzadeh:** How do you choose what to include in the agenda?

**Nika Narimanidze:** These clusters are relatively new and started generating good numbers, but this is the first time after four weeks that they face a declining tendency.

**Nika Narimanidze:** And I think it is relevant for me to report this.

**Nika Narimanidze:** It's just understanding the context.

**Nika Narimanidze:** So AI agents for healthcare, insurance, and law that have been performing well show decline.

**Nika Narimanidze:** Okay, this is the updated point.

**Nika Narimanidze:** Let's bold this, and then we're gonna unbold.

**Nika Narimanidze:** The new editorial cluster for AI at scale has already started attracting sessions.

**Nika Narimanidze:** Okay, let's delete this.

**Nika Narimanidze:** And, you know, we have started, like, new editorial work streams for them.

**Nika Narimanidze:** So for us, it would be interesting to see whether these new clusters, have started to attract the traffic.

**Nika Narimanidze:** So just, let's go to, where was it?

**Nika Narimanidze:** The content pillars, and check sales acceleration.

**Nika Narimanidze:** You know, just a single click impression.

**Nika Narimanidze:** So it's a positive thing, because we had started to publish this two weeks ago.

**Nika Narimanidze:** So the timeframe here is very short.

**Nika Narimanidze:** So I would see this as a positive trend, and I would say that the new cluster, sales acceleration, has started to attract impressions.

**Nika Narimanidze:** Thank you.

**Nika Narimanidze:** But I won't mention clicks because it's useless, right?

**Nika Narimanidze:** It's just a single thing.

**Nika Narimanidze:** Then let's check proposal and project management.

**Nika Narimanidze:** Okay, it has 13 impressions.

**Nika Narimanidze:** But, you know, still technically it's a good thing.

**Nika Narimanidze:** Because if I see that all articles, all clusters started to attract impressions, that I would say that all new, like, clusters have been attracting impressions.

**Nika Narimanidze:** Just a highlighter point.

**Nika Narimanidze:** Let's check Hustor Intelligence.

**Nika Narimanidze:** Hustor Intelligence has 265 impressions.

**Nika Narimanidze:** So it's a good sign.

**Nika Narimanidze:** Let's check the AI at scale.

**Nika Narimanidze:** AI at scale has three clicks and look at the number of impressions.

**Nika Narimanidze:** It's good.

**Nika Narimanidze:** Newly generated clusters like AI at Scale, Customer Intelligence, Sales Acceleration, and Proposal and Project Management have started to attract impressions.

**Nika Narimanidze:** And basically, it's up to you whether you want to indicate the numbers.

**Nika Narimanidze:** But what I've seen with Vivek, he doesn't tend to micro-report stuff because they can go themselves into Looker and check.

**Nika Narimanidze:** But yeah, it's up to you guys.

**Nika Narimanidze:** Some of the older clusters that were previously performing show a slight decline. Our well-performing articles like AI Agents, AI-powered automation, software integrations, and construction are older clusters.

**Nika Narimanidze:** As an overall tendency, most of our older clusters that were underperforming last week started to stabilize.

**Nika Narimanidze:** AI agents for marketing, mining, finance, and transportation have been performing well this week. These are newer articles that weren't stable last week.

**Nathan Navidzadeh:** I have to jump to another meeting very soon.

**Nika Narimanidze:** Yeah, we'll do this very quick.

**Nika Narimanidze:** This is the LLM traffic chart here.

**Nika Narimanidze:** For the LLM traffic chart, we set the weekly filters for October. The LLM traffic has been improved compared to last week.

**Nika Narimanidze:** We have seen upward trends from ChatGPT and Perplexity, while Gemini declined.

**Nathan Navidzadeh:** Is that the last thing for the agenda?

**Nika Narimanidze:** Yes, and you should also create the TLDR message.

**Nathan Navidzadeh:** I have a call with another meeting I can't miss.

**Nika Narimanidze:** Of course.

**Nika Narimanidze:** I hope this was helpful.

**Nathan Navidzadeh:** Are you able to finish that agenda?

**Nika Narimanidze:** Yeah, I can include the last point about the LLM, but.

**Nathan Navidzadeh:** Yeah, I'll make sure to edit the language and create the TLDR. I'll look at the previous one as a template.

**Nika Narimanidze:** Yeah, yeah, in case you have some questions, please just ping me.

**Nika Narimanidze:** Sounds good. Thank you, Nathan, for your time.

**Nathan Navidzadeh:** Thank you, Nika.
