# Sulaman - Looker Dashboard discussion

<metadata>
date: 2025-07-24
time: 16:59 UTC
duration: 76 minutes
organizer: Vivek Shankar
participants: Sulaman Ahmed, Vivek Shankar
fathom_recording_id: 76293839
fathom_url: https://fathom.video/calls/361114117
share_url: https://fathom.video/share/sKzRzq2R6WJgvxk9PCFZwhzFLsy_y2xL
source: fathom
enriched_on: 2026-03-03 15:30 UTC
</metadata>

---

## Summary

Vivek guided Sulaman through the Looker dashboard setup and migration process, focusing on data source switching, custom field configuration, and the current manual URL update workflow. The core issue with existing Looker dashboards is buggy data blending when joining Airtable data, so the team moved to reliable manual case statements. Sulaman committed to cloning the Flossom dashboard for his assigned client and exploring automation opportunities—particularly connecting Airtable to Looker via Google Apps Script—while ensuring the Managing Editors can still deliver reports on schedule.

---

## Context

Sulaman recently joined GrowthX's content operations team and is being onboarded on Looker dashboard management. Vivek, who has already built several Looker dashboards for GrowthX clients, is serving as his mentor through the onboarding process. Andy (likely the operations lead) requested this pairing because Sulaman needed hands-on guidance to understand the dashboard setup, migration, and maintenance workflows. The immediate context is that Sulaman needs to clone an existing Looker dashboard (Flossom) to a new client and learn the process for managing URL updates and data source switches. The broader context is that GrowthX's clients require weekly content performance dashboards, which depend on accurate data integration across GSC, GA4, and Airtable—and historical Looker configurations had data accuracy issues due to buggy blending logic.

---

## Relevance

**To GrowthX Delivery:**
- Looker dashboard reliability is critical for client reporting; data blending issues have created multiple support tickets in Linear that now need resolution.
- The manual case statement approach (replacing Airtable blending) has proven more reliable than automated joins and is now the standard pattern for new/updated dashboards.
- Training Sulaman on this process enables the team to scale dashboard work across multiple clients without degrading data quality.
- Managing Editors (MEs) need weekly reminders that they are responsible for the manual URL update workflow; this is a dependency on the content team's publishing process.

**To GrowthX Business Development:**
- Robust dashboard reporting is a retention lever for content marketing clients; demonstrating reliable, accurate performance metrics builds confidence in GrowthX's delivery.
- Sulaman's role in scaling dashboard setup supports account expansion—the more clients with working dashboards, the easier it is to upsell additional services.

**To Operational Efficiency:**
- Airtable-to-Looker automation (via Google Apps Script and API) could eliminate the manual weekly URL update process, reducing overhead and ME friction. Sulaman is exploring this as a secondary priority after ensuring immediate dashboard delivery.
- Bulk data source switching capabilities in Looker could streamline the cloning/migration process in the future.

---

## Overview

- Vivek guided Sulaman through Looker dashboard setup, focusing on data sources, custom fields, and filters
- The root cause of existing dashboard data issues is buggy Airtable blending in Looker; manual case statements are now the reliable solution
- Sulaman will clone the Flossom Looker dashboard and update it for his assigned client, including data source switches, custom field configuration, and filter updates
- Managing Editors require weekly reminders to manually update newly published URLs in the case statements
- Sulaman identified automation opportunities (Airtable-to-Looker via Google Apps Script) and will explore these after ensuring client dashboards are ready for next week's reporting cycle
- Andy's additional dashboard requirements are mostly achievable; GSC error reporting may require manual screenshots

---

## Key Topics

### Looker Dashboard Setup Process

- Change data sources from existing client (e.g. DataGrid) to new client (e.g. Flossom)
- Create custom fields for URL cohorts in both Google Search Console (GSC) and Google Analytics 4 (GA4)
- Update filters, especially for non-branded queries
- Ensure cross-filtering is enabled for interlinked chart updates
- Handle data blending carefully; use case statements rather than joins to avoid data duplication

### Current Manual Processes

- Weekly updates of newly published URLs required
- Process: copy URLs and categories from Airtable to Google Sheets
- Use Claude AI to format data into case statement syntax for custom fields
- Update custom fields in Looker with new URL data
- Managing Editors present the reports to clients

### Automation Opportunities

- Explore connecting Airtable directly to Looker or using Google Apps Script as an intermediary
- Leverage Airtable's API to pull URL data automatically
- Investigate bulk data source switching capabilities in Looker
- Potential to eliminate the manual weekly URL update step if automation is reliable

### Additional Dashboard Requirements

- Most requirements from Andy's ticket are achievable within current setup
- GSC error data not available via API; may require manual screenshots
- Content calendar integration possible through Airtable to Google Sheets export

### Team Structure and Responsibilities

- Content Managers (CMs) create content in Webflow
- Managing Editors (MEs) present reports to clients and update Looker dashboards (reluctant to do manual work)
- Directors and Leadership Committee oversee strategy

---

## Action Items

**Sulaman Ahmed (GrowthX)**
- Clone Flossom Looker dashboard and update data sources and filters for non-branded queries
- Request Airtable access from Andy for all client accounts
- Inform Andy about the meeting with Vivek regarding Looker dashboard guidance
- Review Engine ANA3 ticket to check if event click link is already tracked in Looker
- Investigate automation options for updating URL lists in Looker custom fields (secondary priority after ensuring client dashboards are ready)

**Vivek Shankar (GrowthX)**
- Ask Ismail to assign Sulaman for Galileo/Framer and Strapi publishing tasks

---

## Transcript

**Sulaman Ahmed:** Monday, the last Monday.

**Vivek Shankar:** Okay, okay.

**Vivek Shankar:** Where are you from?

**Vivek Shankar:** From Pakistan.

**Sulaman Ahmed:** Where you from?

**Vivek Shankar:** From Islamabad.

**Vivek Shankar:** I'm from India, I'm from South, but I've spent a little time in Delhi.

**Vivek Shankar:** That's nice.

**Sulaman Ahmed:** Yeah.

**Vivek Shankar:** Okay.

**Vivek Shankar:** So Andy messaged me and said I'm supposed to support you through your onboarding.

**Vivek Shankar:** Generally, if you have any questions about processes or anything else, you can just ping me.

**Vivek Shankar:** You can also feel free to set up a weekly call on my calendar if you need it.

**Vivek Shankar:** The last time I supported someone with this, she set up recurring weekly calls for a month, and that worked well.

**Vivek Shankar:** So I'm here to help you out in any way.

**Vivek Shankar:** Thank you so much.

**Sulaman Ahmed:** Yeah, so for now I'm focused on learning new things, like using the apps our company works with. If we need to create new tools, I'll figure that out.

**Sulaman Ahmed:** I just got a message from Jess to publish new articles for Homebase. I checked 1Password but didn't find the Homebase credentials, so I messaged her. She said they'd be under Workflow.

**Sulaman Ahmed:** Can I share my screen? Would you be able to guide me if I'm missing something about how to use 1Password?

**Sulaman Ahmed:** That would be really helpful.

**Vivek Shankar:** Sure, sure. You usually get access through the Teams account at GrowthX Labs with those emails.

**Vivek Shankar:** When you log into Webflow, take the password from the team's Gmail account in 1Password.

**Vivek Shankar:** You can share your screen. I'll show you real quick.

**Vivek Shankar:** Got it.

**Sulaman Ahmed:** I have my password with me currently.

**Vivek Shankar:** Okay, just tell me what you were doing.

**Sulaman Ahmed:** I need credentials for Webflow for the Homebase client. The login should be in 1Password under Webflow.

**Vivek Shankar:** Can you search for Homebase?

**Vivek Shankar:** I could help you look.

**Vivek Shankar:** There's nothing there.

**Vivek Shankar:** What I'd do is check the Teams Gmail first.

**Vivek Shankar:** Type in Teams Gmail.

**Vivek Shankar:** I have access to Teams Gmail on my desktop.

**Vivek Shankar:** Okay.

**Vivek Shankar:** Then you can go to Webflow directly and log in with Google SSO. See if it shows up there.

**Sulaman Ahmed:** I don't even have the URL for that company.

**Vivek Shankar:** Just go to webflow.com. It should say login.

**Vivek Shankar:** Use your Google SSO, click "Continue with Google" at the top.

**Vivek Shankar:** No, go back.

**Vivek Shankar:** Click "Continue with Google."

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Okay.

**Sulaman Ahmed:** I don't see Homebase.

**Vivek Shankar:** Try searching for it.

**Sulaman Ahmed:** Let me try searching.

**Vivek Shankar:** Or check if there's a different account.

**Vivek Shankar:** Maybe it's under a different Teams email.

**Sulaman Ahmed:** Hmm, it doesn't look like I have access to that one.

**Vivek Shankar:** Okay, let me check something on my end. I'll need to verify with Andy which account Homebase is under.

**Vivek Shankar:** In the meantime, you can start working on one of the other clients where you have clear access.

**Sulaman Ahmed:** Got it. Should I just ask Jess to clarify which account to use?

**Vivek Shankar:** Yeah, that's probably the best approach. Let her know you couldn't find it and ask her to confirm which Teams account it's under.

**Sulaman Ahmed:** Okay, will do.

**Vivek Shankar:** Great. Now let's talk about the Looker work, which is probably going to be your main focus.

**Vivek Shankar:** So Andy mentioned you to be my mentor on this because I've already been working on some Looker dashboards for our clients.

**Sulaman Ahmed:** Yeah, and I appreciate that. Have you worked with Looker before?

**Vivek Shankar:** Not extensively. I'm not an expert, but I can diagnose issues pretty well. I think it's a good fit.

**Sulaman Ahmed:** I don't have that much experience with Looker.

**Sulaman Ahmed:** I just spent quite a bit of time learning about Looker sources, web matrices, and how things work.

**Sulaman Ahmed:** So one thing I found was, let's say there's already a dashboard in place. When we need to migrate it to a different client, what's the best approach?

**Vivek Shankar:** Looker is pretty much self-taught. I wouldn't say I'm an expert, but I can diagnose issues well. I think it's a good fit for you.

**Vivek Shankar:** The issue with our current Lookers is that all the tickets in Linear show Looker issues because the dashboards were designed in a way that creates problems.

**Vivek Shankar:** Data is completely incorrect because those Lookers pull data from Airtable.

**Vivek Shankar:** In Looker, they call it a "blend," but it's actually a join. When you try to join on a field that doesn't have a perfect one-to-one relationship, it causes data duplication.

**Vivek Shankar:** So the data showing up is completely incorrect because it's introducing duplicates.

**Sulaman Ahmed:** So the join condition within Looker itself isn't working well?

**Vivek Shankar:** Exactly. Blending in Looker is usually buggy. My solution was to remove that automation from Airtable and manually create case statements instead.

**Sulaman Ahmed:** I see. So there's no automation, but there's that manual URL updating?

**Vivek Shankar:** Right. We manually update URLs, which is a bit of overhead for Managing Editors.

**Sulaman Ahmed:** Understood. So basically we'd be replacing the Airtable blend with a manual case statement approach?

**Vivek Shankar:** Exactly. That's the approach that works reliably.

**Sulaman Ahmed:** Got it. What are the specific steps for cloning a dashboard and updating it for a new client?

**Vivek Shankar:** So first, you go into Looker and find the dashboard you want to clone. You'll see an option to duplicate it.

**Vivek Shankar:** Once you've duplicated it, you need to update the data source from the old client to the new one. For example, change from DataGrid to Flossom.

**Vivek Shankar:** Then you need to update the filters, especially for non-branded queries. That's a critical step.

**Vivek Shankar:** You also need to create custom fields for URL cohorts in both Google Search Console and GA4, which requires setting up the proper mappings.

**Vivek Shankar:** And make sure cross-filtering is enabled so that when you click on one chart, the others update automatically.

**Sulaman Ahmed:** Okay, that makes sense. And what about the custom fields in GSC and GA4?

**Vivek Shankar:** You need to create URL cohorts that match your categories. This involves setting up case statements that map URLs to their respective categories.

**Vivek Shankar:** In GA4, it's similar. You create custom fields that organize URLs by the categories you're tracking.

**Vivek Shankar:** Once those are set up in the data sources, you can reference them in Looker.

**Sulaman Ahmed:** And then we manually update those case statements each week when new content is published?

**Vivek Shankar:** Yes, exactly. Every week, when new URLs are published, you need to add them to the case statements.

**Vivek Shankar:** The process right now is copy URLs and categories from Airtable to Google Sheets, then format them into case statements using Claude AI, then update the custom fields in Looker.

**Sulaman Ahmed:** So we use Claude to help format the data into case statement syntax?

**Vivek Shankar:** Right. It's a bit manual, but it ensures the data is accurate and there are no join issues.

**Sulaman Ahmed:** I see. That actually makes sense. It's more reliable than trying to automate something that's inherently buggy in Looker.

**Vivek Shankar:** Exactly. And the MEs can still present clean reports to clients.

**Sulaman Ahmed:** Understood. So after we get the Looker setup sorted, what about Andy's additional requirements? Were there other things she wanted?

**Vivek Shankar:** Yeah, she had a ticket with several requests. Most of them are achievable within the current setup.

**Vivek Shankar:** One issue is that GSC errors aren't available via API, so we might need to handle that manually with screenshots.

**Vivek Shankar:** But the content calendar integration is possible. We can pull data from Airtable to Google Sheets and display it in the dashboard.

**Sulaman Ahmed:** Okay, that's good to know. So the main tasks for me are to clone the Flossom dashboard and update it for the client I'm assigned to?

**Vivek Shankar:** Right. That's the immediate priority. Then you can look into the automation opportunities we discussed.

**Sulaman Ahmed:** Definitely. And you mentioned earlier that I should request Airtable access from Andy?

**Vivek Shankar:** Yes. You'll need access to all the client Airtable bases so you can pull the URL data when updating the Looker dashboards.

**Sulaman Ahmed:** Got it. I'll reach out to Andy about that.

**Vivek Shankar:** Perfect. And one more thing - once you update the Lookers, you still have to tell the MEs that they need to do the weekly process of manually updating newly published URLs.

**Sulaman Ahmed:** I reckon before doing that, I'll try to spend some time figuring out if there's a way to automate it.

**Sulaman Ahmed:** I might create a connection with Airtable. Since they're fields, they should definitely be accessible via API.

**Sulaman Ahmed:** So I might involve Google Apps Script to see if that can work out.

**Sulaman Ahmed:** Other than that, it's working fine for now.

**Vivek Shankar:** Okay, that sounds good.

**Vivek Shankar:** I'll let you take a call on that. But just keep in mind, it's already Thursday, and they'll need to create reports next week.

**Vivek Shankar:** So maybe you won't have time for the full automation. If you run out of time, just tell them the manual process needs to happen for one more week.

**Sulaman Ahmed:** Got it, got it.

**Sulaman Ahmed:** Thank you so much for your time, Vivek.

**Sulaman Ahmed:** Have a nice day.

**Sulaman Ahmed:** Bye now.

**Vivek Shankar:** Thanks a lot. Bye.
