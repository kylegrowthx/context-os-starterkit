# DG & Ramp CMS Intro

<metadata>
date: 2025-05-19
time: 13:01 UTC
duration: 40 minutes
organizer: usman.adepoju@growthx.ai
participants: Usman Adepoju, Nika Narimanidze
fathom_recording_id: 63315577
fathom_url: https://fathom.video/calls/303432847
share_url: https://fathom.video/share/ASWSWs7hRnZraZxw7a1zyLsXygwfGjAy
source: fathom
enriched_on: 2026-03-04 12:30 UTC
</metadata>

---

## Summary

Nika trained Usman on publishing workflows for two key content properties: DataGrid (using Webflow CMS with manual, error-prone processes) and Ramp (using Sanity CMS with automated table integration). The team discussed the shift in publishing responsibilities — Nika currently handles all review and publishing for both properties, publishing ~5 DataGrid articles daily and managing Ramp vendor comparison pages, but is bringing Usman into the review process and will have Vivek cover during her absence. Publishing is paused for Galileo pending a CMS migration, but Nika outlined the inline CTA strategy for different content clusters (e-book CTAs first, then leaderboard CTAs for agent topics; podcast playlist CTAs for other topics).

---

## Context

Usman Adepoju recently joined GrowthX Labs after completing his onboarding (starting writing the week before this meeting). Nika Narimanidze, who works with GrowthX Labs, has been handling all publishing for two key content platforms: DataGrid (a content marketing tool using Webflow for blog publishing) and Ramp (a vendor comparison tool using Sanity CMS). The publishing workload has grown to unsustainable levels for Nika alone, so this meeting was scheduled to train Usman on both publishing processes and bring him into the workflow. The team is also working on automating DataGrid publishing through Airtable-to-Webflow integration to reduce manual input, though that work is still in progress. Additionally, Galileo (another content platform) is in the middle of a CMS migration, which is why publishing is currently on hold.

---

## Relevance

- **To GrowthX Delivery:** Publishing operations for DataGrid and Ramp are critical delivery components. Both platforms have significant CMS complexity and bugs (Webflow is unreliable; Sanity has preview functionality issues), requiring careful manual QA. Nika discovered that Ramp's "Pages" section now shows as "Structure," creating confusion around page preview workflows. Team needs to document these pain points and prioritize the Airtable-to-Webflow automation to reduce manual workload and human error.

- **To GrowthX Business Development:** DataGrid publishes ~5 articles daily, and Ramp has 9 articles in progress with 4 due immediately. Vivek is taking on coverage during Nika's absence, and Usman is ramping up on review responsibilities. Workload distribution is now shared across three team members (Nika, Usman, Vivek), which improves continuity and reduces single-person bottleneck risk.

- **To Galileo Growth:** Galileo CMS migration is underway. Once complete, the new publishing process will rely on inline CTAs (e-book first, then leaderboard for agent/Rang topics; podcast playlists for other content). Publishing is currently paused, but the team has a backlog of articles ready to go once migration completes. This represents a significant content volume opportunity (9 articles in progress).

---

## Overview

- DataGrid publishing uses Webflow CMS, requiring manual input and careful checking due to system bugs
- Ramp uses Sanity CMS for vendor comparison pages, with automated table integration
- Galileo is migrating to a new CMS; current focus is on implementing specific inline CTAs
- Publishing automation efforts are underway for DataGrid to reduce manual workload

---

## Key Topics

### DataGrid Publishing Process

  - Use Teams account to log into Webflow CMS
  - Create new blog posts following specific field guidelines from Airtable assignments
  - Manually input metadata, dates, categories, and images
  - Schedule posts and double-check all elements due to potential CMS glitches
  - Publish \~5 articles per day after review and approval

### Ramp CMS Publishing

  - Use Sanity CMS for vendor comparison pages
  - Automated table integration simplifies the process
  - Select parent and comparison vendors, input content sections
  - Insert vendor metrics and feature tables automatically
  - Currently experiencing issues with page preview functionality

### Galileo Inline CTAs

  - Specific CTAs required for different content clusters (e.g., multi-agents, Rang)
  - E-book CTA always comes first, followed by leaderboard CTA
  - Podcast playlist CTAs used for topics outside main clusters
  - Publishing on hold during CMS migration

### Content Review and Publishing Responsibilities

  - Nika currently handles review and publishing for DataGrid and Ramp
  - Usman to get involved in the review process
  - Vivek will cover during Nika's absence

---

## Action Items

**Usman Adepoju**
- Review DataGrid publishing process video. Prepare to assist with publishing 5 articles/day from "approved for publishing" status in Airtable.
- Access shared document with Galileo inline CTA details. Familiarize with CTA clusters and usage guidelines for different article types.

**Nika Narimanidze**
- Investigate issue with RAMP CMS "Pages" section now showing as "Structure". Update Usman on findings and how to preview pages.
- If DataGrid automation completed before time off, record explanatory video for Usman on new process.

---

## Transcript
**Nika Narimanidze:** No, not so good. It's a bit laggy. Is it my connection or is it just audio?

**Usman Adepoju:** I can hear it better now.

**Nika Narimanidze:** Yeah, so basically we're going to talk about publishings of RAMP DataGrid and discuss the inline CTAs of Galileo.

**Nika Narimanidze:** That's the plan of our meeting.

**Nika Narimanidze:** If you want to add anything, ask a question in the end, feel free to do it.

**Nika Narimanidze:** Okay.

**Nika Narimanidze:** Let's just start. So I've created a document that unites everything that will be valuable for you. I pulled it from the internal channel bookmarks and I'm going to send it to you — I think it'll be useful. The DataGrid stuff is a little bit more complex, so let's start with that.

**Nika Narimanidze:** This is the CMS link here, and you log in with the Teams account. Do you have access to Teams GrowthX Labs? Once we log in, we click the icon here and go to Blogs — that's where we create the blog posts. The first step is to click on "New Blogs," then follow the fields in the Airtable assignments. I've picked one at random to test and go through the process. Vivek will also review this to cover when I'm out this week.

**Nika Narimanidze:** So the first thing we do is open the Google Docs document. This goes into the first field. You'll see the slug is auto-generated, but we don't need that — we'll delete it and go back to the Airtable assignment to find the appropriate slug. We copy it from there and paste it. There's a message about auto-generated unique titles at the end, which you can ignore — it's just metadata.

**Usman Adepoju:** Nika, you should zoom in on your screen. Should I zoom too?

**Nika Narimanidze:** Yes, yes. Good now.

**Nika Narimanidze:** Good. After the slug is generated, we click the copy button here. I'm going to zoom in a bit more. Here's the copy button. I'll click it and paste it into the canonical URL field.

**Nika Narimanidze:** Once it's generated, we manually change HTTP to HTTPS. If we leave it as HTTP, Google will see it as a separate URL and give errors in Search Console and SEMrush. So remember to add the S manually. Next step, you can ignore — it's not useful for publishing. Then we have the date field.

**Nika Narimanidze:** In the Airtable assignments, you'll see two dates: delivery date (when the writer finishes) and publish date (what we use). The publish date is in European format, so we need to convert it to US format — month first. The section below with "blog use case" and "blog industry" is tricky. We only use blog use case and blog industry; ignore blog categories and main category — those fields will be reorganized and deleted anyway. To choose the right fields, go to Airtable and find the use case. For this example, it's Finance — copy it and paste it here in the field.

**Nika Narimanidze:** If there's a use case not in the dropdown (like "Content Writing"), click the plus icon, type it, click "Create and Save as Draft," and it will be automatically selected. I'm not doing that now because "Marketing and Content" already exists. We discard changes. Next, we find the blog industry — in this case, it's Financial Services. The template category field below is for freelancers to organize content by templates in Drive — not for publishing, so you can ignore it. We copy the industry from Airtable and paste it here in the CMS: Financial Services.

**Nika Narimanidze:** The thumbnail image and main image are the same. Download the picture and select it in the CMS — pretty straightforward. But Webflow CMS is often laggy and won't receive the image no matter what you try. If that happens, just redo the process. Webflow is a tricky CMS full of bugs. If it says the file size is too large, it's hallucinating — try again and it might work. When this happens, I usually upload the image first to avoid double work.

**Usman Adepoju:** Okay, so I understand.

**Nika Narimanidze:** We always select "DataGrid Team" as the author. Then we have the intro text — it's the same as the meta description from the metadata, so copy and paste it here. Then comes the PostBody. When working on PostBody, ignore the H1 since we already added it. Copy the whole document. Again, Webflow is laggy and adds extra spaces even when the source document doesn't have them. I quickly scan for those issues. For example, you can see there's an extra space here. We make sure those don't slip through. You can check against the docs too, but Webflow isn't reliable, so I always scan to avoid inconsistencies. It's not always a pain-free process. You can ignore the excerpt field — it's not useful. The featured blog field is set as default.

**Nika Narimanidze:** When you publish it, it will appear on the main page. Then comes the Meta Title and Meta Description. Copy them from the Airtable — Meta Title goes in Meta Title, and Meta Description is the same as the intro text. After everything is filled in, click Create. We schedule the article before publishing. To schedule, click here, select the date from the Airtable (in this case, May 16th), and then click Schedule.

**Nika Narimanidze:** Once it's scheduled, we don't trust Webflow and double-check that everything is present. When I started, it all looked correct, but when I went back, the images were gone and there were extra spaces. These issues happen sometimes but not always, so I quickly scan to make sure everything is good. Then I continue with the next article. Sometimes Webflow kicks you out of the session, but we're trying to fix this. We're integrating Airtable to Webflow to automate publishing — the automation is still failing, so I'm not sure when it'll be ready. But this is the manual process for now, and that's what I'm doing. Do you have any questions about Webflow?

**Usman Adepoju:** No questions. Except for the Webflow problems you mentioned, everything is straightforward. Yeah, it's pretty simple.

**Nika Narimanidze:** Just make sure no errors slip through. That's it. Let's move to the next client — Ramp. Ramp has vendor comparison pages — they compare different types of tools, like Airtable vs. Asana. We help them publish because the volume is too high. There's the Ramp CMS link, and I've included Loom videos from their team as well, so you can see the process from both sides. Sanity CMS is also full of bugs — it's a newer CMS, unlike WordPress, and they all have issues.

**Nika Narimanidze:** I'm going to talk about the issues I've faced. Let me visit the Ramp Airtable. It's not available from here directly, so let me access it another way. Here are the articles we produce for them — Smartsheet, Asana, and other comparison and overview texts. The good news, Usman, is you don't have to create the tables manually. They have a system where you put the vendor name and everything displays for you. It's fine to have this many tables. When we have vendor comparison articles, we go to the vendor comparison section, and there are the published articles.

**Nika Narimanidze:** If you visit this article, you see we indicate the parent vendor first. The parent vendor is Smartsheet because it's listed first. The logic is simple — click here, type Smartsheet, and click Save. It's already published, but let's create a draft. Say we write Notion. Notion is the main vendor because that's the page structure — we have a page about Notion and then related sections like "Notion vs. Asana." After we indicate this, we move to the comparison part. We select the first vendor (Notion again) and add items. The tables are automatically placed on the page — we integrate the vendor table database to avoid manual work. The slug is auto-generated, so we just move to the next section.

**Nika Narimanidze:** Then comes the hero title — the H1. In this case: "Smartsheet vs. Asana: Data-backed Comparison." Next is the hero body — the intro sentence below the H1. Copy it and paste here. Then comes the content. We don't copy-paste everything at once — it's not a single click. We copy everything up to the first table. Looking at the doc, the first table is about metrics. We go back to the content body, click the three dots, choose "Vendor Metrics Table," add items, and select the vendors. The table data automatically integrates into the text. Next, we handle the Smartsheet overview — copy the text until the first table and the header. Click three dots, select "Features Table," and type the vendor name (Asana or whatever). Do the same for the Asana overview — copy text until the table, paste it, insert another feature element, and write Asana. Then comes the use case scenarios section — there are no more tables after that, so we copy and paste it directly.

**Nika Narimanidze:** The body text is ready. Then we move to the Hub Topic field and type "Vendor Management," and for the Publishing Team, indicate "SEO." Everything is set up now. The page is drafted. After drafting, we can see how it looks on the blog. But here's the tricky part — even if everything looks correct and placements are right, the website might not display correctly and you have to redo it. This happened 4 out of 13 articles. So be careful and check every time to catch errors. Let me show you the preview. The main thing is to import the tables correctly and ensure you type the right vendors and table types as indicated in the CMS. I've included explanation videos from Victoria, the client, showing how to check article previews on the blog and how to adjust text length if it's too long or too short. I've never had that issue because they did pre-work, but it's good for you to check it. Do you have any questions about Ramp?

**Usman Adepoju:** Can you show me the presentation? I want to check what it looks like on the blog for Ramp.

**Nika Narimanidze:** Yes, I'll load it. Just a sec — I'll open it on another screen. Meanwhile, how's your onboarding going? Is everything good?

**Usman Adepoju:** I started writing last week, so I'm fully in. My onboarding ended last week.

**Nika Narimanidze:** My connection is bad — I think I need to rejoin. I lose you all the time and can't keep up. Just give me two minutes.

[Audio issues during reconnect]

**Usman Adepoju:** Thank you.

**Nika Narimanidze:** Can you hear me?

**Usman Adepoju:** Yes, I can hear you now.

**Nika Narimanidze:** Okay, sorry for the issue. I'm back in the Ramp CMS. I'm going to share the screen with you.

**Nika Narimanidze:** The tricky thing is that we should have a "Pages" section here, but now it shows "Structure." I tested this before and there was a "Pages" section, but now it's "Structure" — weird. Let me try logging in again. Still "Structure." Let me try to see the preview. No, we can't see the preview here. I'm honestly not sure what happened. We have "Structure" now, but before it was "Pages." Maybe they're changing something in the backend. Once I understand what's going on, I'll update you. No worries. Meanwhile, we're also working on DataGrid automation. If it's ready before my time off, I'll record a video for you explaining it — that'll be much easier than the manual process. Let's move to the Galileo account.

**Nika Narimanidze:** Galileo is migrating to a new CMS — the website will be completely new. What we need to discuss is inline CTAs — these are CTAs embedded in the article body text that redirect when clicked. I have a table that will help you understand the CTA clusters and which articles need specific CTAs. For example, if you're writing about multi-agents or agents in general, include two inline CTAs in the article. The table has all the details, including images (which you download) and captions. The important thing is the CTA order — always insert the e-book CTA first, then the leaderboard CTA. If you're writing for the "Rang" cluster, use those CTAs. For topics outside "agents" and "Rang," use podcast CTAs instead. Galileo has a YouTube channel with podcasts, and we include the playlist links with a banner and caption alongside the inline CTA. That's basically it. Ask questions if you need clarification.

**Usman Adepoju:** I think I saw this last week. Can you share this document? I went through some of the articles to check how they implement it. The implementation looks right. I went through some articles just to check how they're posting them, and I think I'm good on this. But if I need help, I'll reach out. Also, we're not publishing until they migrate, right?

**Nika Narimanidze:** Yes, the process will change. Publishing is on hold — we're collecting a backlog of articles. Just remember: use the CTAs for those clusters, and for everything outside those clusters, use the podcast playlist CTA. I'll share this document with you too. To show you where everything lives, in Ramp go to Bookmarks and you'll see the CMS link with videos on publishing vendor pages. The page preview is important, but it's currently not working — I'll update you on that today. The same setup applies to DataGrid — go to Bookmarks, access the Content folder, then the SOPs section. You'll see the Article Generation SOP video (shared with VAs), a template folder for coordinating, and an Image Generation SOP (also for VAs). Product information is there too, but Notion is more convenient. That's basically it.

**Usman Adepoju:** Thank you very much, Nika.

**Nika Narimanidze:** If you have some additional questions, after the meeting, please ping me in the channel, and I can help you with everything that you need in terms of publishing, and maybe to find the valuable links as well.

**Usman Adepoju:** Okay. When does publishing start? At least for DataGrid?

**Nika Narimanidze:** DataGrid publishing occurs every day. The Airtable is the place to track that. When you visit the Airtable and see articles in different statuses, articles in "Client Review" — when I review and approve them, I move them to "Approved for Publishing." That way, we can see which articles are ready to go out. Everything under "Approved for Publishing" should be published. Our VAs create the content, I finalize them, and then we can split the load. We typically publish five articles per day. You can review the call recording, follow the DataGrid instructions, and then we can coordinate and make sure you're doing it right.

**Usman Adepoju:** So I'll be responsible for reviewing and publishing the articles?

**Nika Narimanidze:** Well, for some period, yes — I'm handling Ramp and DataGrid alone right now and sometimes it gets overwhelming. Vivek mentioned you should get involved. The freelance VAs create the articles, and I review and publish them. We used to have a dedicated publisher, but we're working on automating this to reduce the load.

**Usman Adepoju:** Okay, no problem. And while I'm away for a week, you can chip in and help Vivek, who will cover during that time.

**Nika Narimanidze:** During my absence, help Vivek, because he'll be taking care of it as well.

**Usman Adepoju:** There's nothing in publishing to do for Galileo yet, right?

**Nika Narimanidze:** Not yet, but we'll have it soon. Nine articles are being created right now. Four of them are due today.

**Usman Adepoju:** Okay.

**Nika Narimanidze:** Just feel free to ping me about anything you need. If you have additional questions after the call, reach out and I can help with everything publishing-related and find valuable links.

**Usman Adepoju:** Thank you very much, Nika. Bye, have a great day.

**Nika Narimanidze:** Thanks.
