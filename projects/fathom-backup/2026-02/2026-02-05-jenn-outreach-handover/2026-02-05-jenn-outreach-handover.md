# Jenn - Outreach Handover

<metadata>
date: 2026-02-05
time: 20:15 UTC
duration: 16 minutes
organizer: Usman Adepoju (usman.adepoju@growthx.ai)
participants: Jenn Peters (jenn@growthxlabs.com), Usman Adepoju (usman.adepoju@growthx.ai)
fathom_recording_id: 120189403
fathom_url: https://fathom.video/calls/558491562
share_url: https://fathom.video/share/TyGzsv24z6CuFMrVbuD-23DXd9TPvPeo
source: fathom
enriched_on: 2026-02-27T00:00:00Z
</metadata>

---

## Summary

Jenn Peters hands off Outreach client responsibilities to Usman Adepoju, covering article refresh workflows (yellow/strikethrough formatting with Claude post-processing), publishing operations with Asana-based client processes, and key tools for automating CTAs and header formatting. Jenn commits to reviewing Usman's first week of work to ensure consistency and catch edge cases.

---

## Context

This is an operational handover for GrowthX's Outreach engagement, a content marketing services client requiring article refreshes on a recurring cadence. The client operates their editorial workflow through Asana (not Airtable) and expects detailed change visibility through yellow/strikethrough formatting, though Jenn advocates for moving to net-new drafts to reduce overhead. The core workflow involves using the "change document" pipeline in Outreach Atlas to identify additions/deletions/rearrangements, post-processing those results in Claude to ensure competitive completeness, and manually tracking published URLs back to the company's Airtable operations system. Usman's first week will involve familiarizing himself with strategy docs, the operational manual, and Timmy's publishing video before taking over Monday-to-Friday article refresh and publishing coordination.

---

## Relevance

- **Outreach client operations:** Full workflow handover including article refresh cadence, publishing coordination, and compliance with client-specific formatting requirements.
- **Content quality assurance:** Claude post-processing step is mandatory to catch stats misuse and gaps in competitive coverage that the "change document" pipeline misses.
- **Systems integration:** Cross-functional touches with Suleiman (staging), Airtable OS (metrics tracking), Looker dashboards (weekly updates), and client Asana calendar.
- **Operational procedures:** Automation setup, Linear reminders transfer, and team knowledge transfer required to complete handover.

---

## Overview

- **Article refreshes require a yellow/strikethrough format** for client review, a process Usman should advocate to change to net-new drafts.
- **Use the `change document` pipeline** for refreshes, but always post-process in Claude to ensure competitive completeness.
- **Manually update Airtable with published URLs** from the client's blog, as they use Asana and often miss this step.
- **Jenn will review all of Usman's work** next week to ensure quality and provide direct feedback.

---

## Key Topics

### Article Refresh Workflow

  - **Client Requirement:** Article refreshes must use a yellow/strikethrough format to show all edits for client review.
  - **Recommended Change:** Usman should advocate for net-new drafts.
      - **Rationale:** The current format is time-consuming for both teams and makes the final article difficult to visualize.
      - **Timing:** The client's strategy shift and upcoming renewal create a good opportunity to propose this change.
  - **Pipeline Process:**
      - Use the `change document` pipeline in Outreach Atlas.
      - It generates a point-by-point list of additions (highlight yellow), deletions (strikethrough), and rearrangements.
  - **Post-Processing in Claude:**
      - **Why:** The pipeline's output is not 100% reliable for competitive completeness.
      - **How:** Use the "Outreach, post-processing" project to compare the draft against top-ranking articles and identify gaps.
  - **Fact-Checking:**
      - **Why:** The pipeline can "shoehorn" stats, misinterpreting data to fit a narrative.
      - **Action:** Always verify stats and their context in the source article.

### Client & Publishing Process

  - **Client Tooling:** The client uses Asana, not Airtable, for their editorial calendar and publishing.
  - **Publishing Flow:**
    1.  **Staging:** Articles sent to Suleiman for staging.
    2.  **Publishing:** Client publishes on their own cadence.
    3.  **Airtable Update:** Client often fails to add the published URL to our Airtable OS.
  - **Required Action:** Usman must manually check the client's blog every few days to find and add missing URLs to Airtable.
      - **Why:** This data is required for the weekly Looker dashboard update.
  - **Other Tools & Tasks:**
      - **`image only generator` pipeline:** Creates standalone images, useful for fixing incorrect titles or replacing low-quality visuals.
      - **Bottom-of-funnel CTA:** Add to all articles using the dedicated Claude project.
      - **Header Formatting:** Change all headers to sentence case, as many older articles use title case.

---

## Action Items

**Jenn Peters (GrowthX)**
- Set up Usman's edit-update automation to notify him of client changes

**Usman Adepoju (GrowthX)**
- Review Outreach Operational Manual and Timmy's publishing video
- Study Outreach client strategy, company context, and product matrix
- Begin article refreshes on Monday and send all drafts to Jenn for QA review

**Joe (GrowthX)**
- Transfer Linear reminders (Looker updates, publishing tickets) to Usman

---

## Transcript

**Jenn Peters:** If you look at this article, you'll see yellow and strikethroughs. Timmy's video will explain—you put all the new content in yellow and anything you're removing you strikethrough. It's annoying, but the client wants to see what's being added and removed.

**Jenn Peters:** Ideally, I'd suggest encouraging them to switch to net-new drafts. It would benefit both sides. When Timmy was doing this, he'd post-process in Claude and generate a big list of additions and deletions. Panzer created a pipeline called "change document" in Outreach Atlas that automates this. You add any refresh and it gives you a point-by-point list with exact placement instructions, then deletions, then rearrangements.

**Jenn Peters:** This sounds insane because it takes more time, but I mentioned to Joe that they should ask the client if they'd prefer net-new docs instead. Yellow/strikethrough doesn't show them the final completed document or the word count or overall flow. This dates back to their original strategy sprint, but their strategy shift and renewal coming up is a perfect opportunity to propose changing it.

**Jenn Peters:** I've gotten used to it, though. But the pipeline doesn't always do a great job of identifying what's missing competitively. So I do a second step in Claude using the "Outreach, post-processing" project. I ask: here are the keywords, here are the top three ranking articles, here's my draft—does it have everything it needs to outrank this piece?

**Jenn Peters:** The pipeline doesn't hallucinate or generate fake stats, but it does shoehorn stats to fit a narrative. For example, it'll say something dropped 25 percent, but the source's conclusion doesn't actually support that interpretation. You have to use your best judgment and verify stats against their original context.

**Jenn Peters:** Next week, send each piece to me before you ship it. Don't worry—I'll be here. Joe is away the next two weeks, but I'm available. There are finicky things with Outreach that you'll learn by doing rather than from me listing them all at once. The best prep for Monday is to read the strategy, company context, and product matrix. Even feed the product matrix into Claude and ask it to explain it more simply. These topics aren't super complex—we just need to be factually accurate about the product and make sure all the links work.

**Usman Adepoju:** I feel like I'll have more questions once I get into it.

**Jenn Peters:** Right—you need to see it and do it. It's hard to know what'll come up until you actually do it. There's a pipeline for creating a standalone image without an article. This is useful if your title changes or you remove a tool and need to regenerate the image. It's called "image only generator."

**Jenn Peters:** After Suleiman stages the articles, they publish on their own cadence. But they don't always remember to update our Airtable OS with the published URL. Every couple of days I check the OS against their blog to find missing URLs. This is important because on Mondays you'll need to update the Looker dashboard. The client uses Asana, not Airtable—they don't think about updating our OS. But Joe always wants it current.

**Jenn Peters:** The flow is: you're making the articles. Sometimes they send you articles they've reviewed for final checks before you send them to Suleiman. Create a publishing ticket for him on Wednesday or Thursday. We usually have enough of a buffer that things flow smoothly. Today I'm setting up automation so you get notified about client edit updates. Joe is transferring the Linear reminders that were set to me over to you—things like the Looker update reminder.

**Jenn Peters:** Published articles are in the OS for reference. Notice that newer headers are in sentence case, but some older ones we're refreshing are still in title case—you need to change those. Every piece has a bottom-of-funnel CTA section. Timmy made a Claude project that generates that—just feed the content in and it produces the eyebrow copy, paragraph, and CTA.

**Usman Adepoju:** For Timmy's video—is that in the Operational Manual?

**Jenn Peters:** Yes, go to the Operational Manual. It has all the publishing stuff and videos. Timmy breaks down how to copy article content from the published page, put it into a Google Doc, and format it so it goes back into a normal editable view instead of chunky graphic blocks. He makes it really clear. And I'm always here if you need me to show you something.

**Jenn Peters:** I think the timing of this transition is good because of their strategy shift, the renewal coming up, and new content on the horizon. I'm sure the client won't notice any change or difference. I'm excited for you. Just don't hesitate to reach out with questions. Talk to you soon.
