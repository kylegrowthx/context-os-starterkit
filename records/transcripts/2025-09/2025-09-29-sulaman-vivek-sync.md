# Sulaman <> Vivek sync

<metadata>
date: 2025-09-29
time: 15:31 UTC
duration: 28 minutes
organizer: Vivek Shankar
participants: Vivek Shankar, Sulaman Ahmed
fathom_recording_id: 90479781
fathom_url: https://fathom.video/calls/425711668
share_url: https://fathom.video/share/vUAP-idADq1p39q_K2tJoUKyFa-7vzEj
source: fathom
enriched_on: 2026-03-03 12:45 UTC
</metadata>

---

## Summary

Vivek and Sulaman aligned on automating GA4 and GSC URL formatting using Apps Script to enable data blending for Looker dashboards across GrowthX client accounts. The team decided to implement full data refreshes rather than incremental appends, and reviewed multiple client-specific dashboard setup issues including Superhuman (tag/cluster fixes), Hockey Stack (template type correction), and Cash App (requiring further data gathering for a complex custom build). Sulaman committed to updating the Google Sheet script, adjusting Looker blends for proper URL joining, and testing the setup on Galileo before rolling out to all accounts.

---

## Context

GrowthX delivers analytics dashboards and reporting to B2B clients using Looker, with data sourced from Google Analytics 4 (GA4) and Google Search Console (GSC). Vivek leads the technical data infrastructure, while Sulaman owns the implementation and troubleshooting of dashboard builds. This sync focused on solving a critical data blending problem: GA4 and GSC use different URL formats for joining data, requiring separate automation logic. The team is testing this approach on Galileo before rolling out to all other accounts, and also working through a backlog of client-specific dashboard requests with varying complexity levels.

---

## Relevance

- **To GrowthX Delivery:**
  - Apps Script automation for URL formatting will reduce manual work and improve data accuracy for future client implementations
  - Clear distinction between GA4 URL format (everything after "/log") and GSC URL format (full published URL) is essential for correct data blending
  - Testing methodology for blends on a copy report before rollout prevents errors across all client accounts
  - Multiple client dashboards need fixes (Superhuman tag correction, Hockey Stack template type, Relay GSC updates)

- **To CheckThat:**
  - Google algorithm update on September 9 caused visible traffic spike/drop that needs to be flagged to clients
  - Current Google data reporting bug causing 2-3 day lag in GSC/GA4 data visibility affects CheckThat visibility insights

- **To GrowthX Business Development:**
  - Cash App deal flagged as requiring full custom build with missing data fields — potential scope/timeline discussion needed with client
  - Multiple accounts in active delivery phase with dashboard refinements (Superhuman, Logic, Relay, Diligent, SWOT)

---

## Overview

- The GA4 and GSC data blending process is ready for testing, with minor adjustments needed for URL joining
- Automation for URL formatting (GA4 vs GSC) will be implemented using Apps Script to reduce manual work
- Several client-specific Looker dashboard issues were reviewed and action items identified
- A complex custom build request for Cash App requires further discussion due to missing data fields

---

## Key Topics

### Data Blending and URL Formatting

  - Current automation script runs in \~10 seconds, capable of full data refresh
  - Decision made to stick with full updates rather than appending new data
  - Need to create separate columns for GA4 and GSC URL formats in the Google Sheet
  - Apps Script will be used to automate URL formatting, reducing manual work
  - Correct URL joining is crucial: GSC blend uses full URL, GA4 blend uses GA4-specific URL

### Looker Dashboard Testing and Updates

  - Test copy of Galileo Looker dashboard created to verify data blending
  - Process: Change data sources to test blends (GA4 and GSC) and verify data accuracy
  - Only change sources where GA4 or GSC is directly referenced, not for existing blends
  - Some charts (e.g., those already using blends) don't require source changes

### Client-Specific Issues

  - Superhuman: Incorrect tag and missing clusters identified; Sulaman to fix
  - Logic: Straightforward setup, quick review needed
  - Hockey Stack: Wrong task type (EPD instead of ANA) used; need to inform requester
  - Relay: Additional GSC-related changes requested
  - Diligent: Issue fixed
  - SWOT: Discrepancy in URL count explained (published vs receiving traffic)
  - Cash App: Complex custom build request with missing data fields; requires further discussion

### Google Algorithm and Data Reporting Issues

  - Spike drop observed around September 9th due to a Google algorithm update
  - Current bug in Google's reporting causing data to appear stuck a few days behind

---

## Action Items

**Sulaman Ahmed**
- Update Google Sheet script - include GSC & GA4 URL formats, automate GA4 URL column

- Adjust Looker blends - ensure correct URL joining for GSC (published URL) & GA4 (GA4 URL)

- Update sources in Galileo Looker copy report - switch to new blends (testGA4 blend, testGSC blend)

- Fix superhuman Looker dashboard - correct tag, add missing topic clusters

- Contact Ada re: hockey stack Looker setup - inform about incorrect EPD format, request A board format

---

## Transcript

**Vivek Shankar:** You know, me going back and forth with this thing.

**Vivek Shankar:** Let me just open the, where is it, thing. So the automation, I saw the Looker that you linked to. It seems like the data is correct, right? It's matching like the GA4 versus the blend.

**Vivek Shankar:** Question about the export that you're doing. What is the easier way to do this? So basically, the Looker will pull from this sheet and it will then blend the data. Does that sheet need to pull in every single URL, published URL every single time? Or can it just pull in like the diff? So initial export, like whatever, 100, 200 URLs published. Second export, following week, only like five URLs extra. Like what is the easier way of doing it?

**Sulaman Ahmed:** I got it. Right, just give me one second on this one. So this is that sheet I shared with you. Now the speed of this script is, let's say I execute it right now, and it's done. So just like around 10 seconds. In 10 seconds it has the capability to bring back all of them. I can customize the script to get back all of them, find the difference, and just add the ones that are not already there. So that's totally an easy logic. That depends on how exactly we want it. At the moment it overrides all of them, brings the new data.

**Vivek Shankar:** But if you want it to append instead...

**Sulaman Ahmed:** We can easily do that. We can bring back and compare the difference, and the ones that would not be there, it will add them. So both options are available.

**Vivek Shankar:** OK, I don't think appending makes sense. If it's updating quickly then I think we can just stick with the full-on update, right?

**Sulaman Ahmed:** That makes sense, yeah.

**Vivek Shankar:** OK, so next step is the cohorts, right? We need to bring in the URLs as well as the URL cohorts. Basically the second column represents the cohorts.

**Sulaman Ahmed:** OK, so can you show me that sheet again?

**Vivek Shankar:** I know I took a look at it but I didn't pay attention to the second column.

**Sulaman Ahmed:** Yeah, blank rows.

**Vivek Shankar:** Yeah, fine, no worries. I'd like to test this on Galileo. So the copy of the Galileo Looker that you've created, right? I'm opening it right now.

**Vivek Shankar:** In the data sources we need to test it. Can I share my screen real quick? Yes, please. So this is a copy that you've created. And these charts have data sources. We need to change it to the testGA4 blend and see if it works the same way. So basically all these sources need to change everywhere. Every source will be the GA4 blend. And if it's GSC we need to change it to testGSC blend.

**Sulaman Ahmed:** OK, so we want to replace these sources, save, and see if that works.

**Vivek Shankar:** Yeah, because what I want to do is change the sources on this test report and then I'll compare it to the actual Galileo report and see if the data matches. If it matches then we can roll this out to every other account.

**Sulaman Ahmed:** Well 100%, that makes sense.

**Sulaman Ahmed:** I would like to highlight a few things. The first thing was on the line map we see on the first and second tab. On September 9 everyone saw a spike drop in that. That was something from Google's end, a new algorithm. Secondly there is a new bug from Google's side. It's stuck a few days back in the graph. The data is not up to date. And one more thing, can you go to the top where we have URL cohorts and the count? These numbers there, what are they supposed to mean?

**Vivek Shankar:** These are engaged sessions.

**Sulaman Ahmed:** Got it. So I was confused initially. I thought these were the number of pages. So for that dashboard I changed it to the number of pages because they were getting confused. They didn't think we were uploading that many pages. So I cleared that by explaining it's engaged sessions.

**Vivek Shankar:** So we don't let's stay away from regex because there's character limits. For now the only thing is this blend. I think the blend is ready to go, to be honest. Let's just do cohorted page data and remove the older stuff.

**Vivek Shankar:** You just copied this from the existing Galileo report, right? You didn't make any changes to the blend?

**Sulaman Ahmed:** No, I changed the data source to the new blend I created. I switched the data source, just the sheet.

**Vivek Shankar:** Yes, that is correct. But the join condition should be the same. Did you double check?

**Sulaman Ahmed:** Let me check.

**Vivek Shankar:** I was unable to find the sheet you created. Did you put it in your account?

**Sulaman Ahmed:** I think I put it in my account by mistake.

**Vivek Shankar:** Yeah it's here. I just exported the entire layer table. Let me add you just to be safe and send this to you.

**Sulaman Ahmed:** OK so I can access it now. But this does not have the required format we need.

**Vivek Shankar:** The problem is when we're joining on the URL for the GSC blend, that URL join needs to match the GSC URL. But the GA4 URL is different. I asked Ismail to create this GA4 URL column, right?

**Sulaman Ahmed:** If we're using a manual process there's a possibility for mistake. Instead of one column we can have two, one pattern for GA4 and one for the original GSC format. So if we do it on Google Sheets via Apps Script that would be automated.

**Vivek Shankar:** Exactly. Apps Script can do that. So I think that would be the first step. We take the Airtable export and create a new column that formats it based on GA4, just everything after the slash log. So two URL columns and then the third would be the cohort category.

**Vivek Shankar:** This join is actually incorrect. This should say published URL. When we're joining on GSC we need to join on the right URL column. Published URL in my sheet is the full URL, right? So this is a GSC join. If I go to GA4, I'm joining on the GA4 URL not the published URL. Am I making sense?

**Sulaman Ahmed:** So and this is correct. We were supposed to match by GA4 URL for the GA4 blend.

**Vivek Shankar:** Correct. So the two blends, the only change is the URL column changes and the join column changes. That's it. Landing page and GA4. And if you go to the GSC blend it will say published URL and landing page.

**Vivek Shankar:** Can we test it for one column to see if that works?

**Sulaman Ahmed:** I mean it already works, right? I tested the blend in this report and it worked. The data was correct.

**Sulaman Ahmed:** So let me first wrap up that Google Sheet part, extract the URLs in both formats GSC and GA4. And after that I can switch each table. If it's GA4 use the GA4 format. If it's GSC use the GSC format.

**Vivek Shankar:** You need to test it in this copy Galileo report. Fix the blend columns to match whatever is in the Galileo blend and make sure the correct URL is being joined on for GSC and GA4. Once that is done you change the sources to all the charts. If the data source is GA4 you just choose the GA4 blend.

**Vivek Shankar:** Do I need to change everything in this chart?

**Sulaman Ahmed:** You only change it wherever the source data is directly GA4 or directly GSC, not where it's already a blend.

**Vivek Shankar:** Right. So for this chart the data source is GA4, right? So you change it to test GA4 blend. And nothing in the bottom needs to be changed.

**Vivek Shankar:** The date filter has no data source so it's fine. The country filter again GA4. Just make sure the source is not GA4 or GSC as a blend. You don't need to change anything for blends.

**Sulaman Ahmed:** OK that makes sense. I'll start with it right away. Regarding the few of the tasks, can we just walk through them one by one?

**Vivek Shankar:** Yeah. Superhuman Looker dashboard. The data is wrong, we wanted to correct the superhuman block.

**Sulaman Ahmed:** That was a different tag. I didn't have the right tag initially so I used my judgment.

**Vivek Shankar:** And the clusters are missing.

**Sulaman Ahmed:** The topic clusters exist in the Airtable. So I'll fix that.

**Vivek Shankar:** Logic. This is straightforward, a quick review should be fine.

**Vivek Shankar:** Hockey Stack. Why is this an EPD?

**Sulaman Ahmed:** She might have used the wrong board type.

**Vivek Shankar:** Yeah, she's not following the template. Maybe just ping her and tell her it needs to be an A-board format or something.

**Vivek Shankar:** Relay. GSC changes. That's fine. Diligent, this is fixed.

**Vivek Shankar:** SWOT. We have 329 in GrowthX. We published 382. Did you have a chance to look at this?

**Sulaman Ahmed:** It might be an engaged sessions thing. She might be confusing engaged sessions.

**Vivek Shankar:** These are URL clicks. Yeah these are showing engaged sessions. They might not have received traffic so that's why there's a discrepancy. Let me explain that to her.

**Vivek Shankar:** Cash App. This is a complex custom build request. They want a complete redesign. What data are they asking for?

**Sulaman Ahmed:** They want kind of a complete redesign. But the sheet does not have the required tabs and fields that we need.

**Vivek Shankar:** Let me work through this. Contact lead data tab, Contact ID, create date, date added. Yeah we need these fields. They're not present unfortunately. This is a full-on custom build so we don't have the data either. Let me respond to her.

**Vivek Shankar:** OK I have to hop on another call. I'll take a look at this and get back to you yeah?

**Sulaman Ahmed:** All right thank you so much.

**Vivek Shankar:** Thanks Sulaman. Thanks, bye. Have a nice day.
