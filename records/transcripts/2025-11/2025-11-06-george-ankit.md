# George / Ankit

<metadata>
date: 2025-11-06
time: 12:01 UTC
duration: 36 minutes
organizer: georgemaine@growthx.ai
participants: Georgemaine Lourens, Ankit Pahuja, Garima Nanda
fathom_recording_id: 99647305
fathom_url: https://fathom.video/calls/466666385
share_url: https://fathom.video/share/uPqnHsBiukrL1QnodF-tEnkuUrseAWof
source: fathom
enriched_on: 2026-03-02 18:45 UTC
</metadata>

---

## Summary

Georgemaine, Ankit, and Garima reviewed SentinelOne's CVE database QA sheet row-by-row, prioritizing critical bugs (filter reset issues, incorrect "View All" CTA logic, missing mobile hamburger close button) alongside UX refinements (filter menu interactions, sidebar content optimization). The team approved removing filter checkmarks in favor of color highlighting only, decided to keep the date range filter as month/year-only to simplify the UI, and agreed to defer the "Related CVEs" section (critical for SEO topical authority) until all critical bugs are fixed. Georgemaine will prioritize pushing fixes to staging, investigating the published date filter bug, and styling CVE detail page enhancements pending API support from Marcus.

---

## Context

Georgemaine Lourens (GrowthX) met with Ankit Pahuja and Garima Nanda from SentinelOne to review and prioritize their CVE (Common Vulnerabilities and Exposures) database quality assurance. Garima, a senior QA engineer at SentinelOne, has been leading QA efforts on the database and reported most of the findings in the QA sheet. This was the first time Georgemaine met Garima, though Ankit had coordinated the meeting. The session focused on working through a prioritized QA sheet row-by-row, verifying which bugs were critical, which were addressed, and which UX decisions needed team alignment before the next development push to staging.

---

## Relevance

**To GrowthX Delivery:**
- Gained firsthand QA insights on a large-scale CVE database project, including filter logic, mobile UX, and API dependencies that impact delivery timelines.
- Demonstrated effective prioritization methodology: working through QA sheets to distinguish critical bugs from nice-to-have refinements.
- Identified need for clearer "apply vs. dismiss" UX patterns when implementing complex multi-select filters — applicable to future GrowthX projects.

**To GrowthX Business Development:**
- SentinelOne's database project is progressing from QA review to staging deployment, indicating healthy project momentum and relationship building.
- Ankit is actively engaged as a strategic partner in design decisions (filter UX, date range simplification, sidebar content audits), suggesting high account investment.
- Garima's hands-on QA role and detailed issue reporting indicates SentinelOne's commitment to quality, which is a positive signal for renewal and expansion.

---

## Overview

- **Critical Bugs:** The "Published" date filter is broken, failing to reset and showing a misleading active state on page load. The "View All" CTAs also display incorrect results.
- **UX Decisions:** The team approved removing checkmarks from selected filters (color highlight is sufficient) and keeping the month/year-only date range filter to simplify the UI.
- **Filter Menu UX:** The current filter menu UX is confusing. The team will explore two solutions: adding an "Apply" button or making the menu background clickable to dismiss it.
- **Future Enhancements:** Key items on the roadmap include adding "Technical References" and "Vendor Resources" to CVE detail pages (pending API support) and making the CVE info table visible on mobile.

---

## Key Topics

### Critical Bugs & Fixes

  - **"Published" Date Filter (Rows 26-27)**
      - **Problem:** The filter fails to reset on the first click and shows an active state (earliest-to-latest range) on page load, even in incognito mode.
      - **Action:** George will investigate.
  - **"View All" CTA Logic (Row 10)**
      - **Problem:** "Top Scores" and "High Profile" CTAs incorrectly display all 250 CVEs instead of their filtered subsets.
      - **Action:** George has a fix locally and will push it to staging.
  - **Mobile Hamburger Menu (Row 18)**
      - **Problem:** The close button is missing from the mobile hamburger menu.
      - **Action:** George will investigate.

### UX/UI Refinements & Decisions

  - **Filter Menu UX (Row 23)**
      - **Problem:** The current UX is confusing; users must re-click the "Filter" button to apply selections.
      - **Solutions to explore:**
        1.  **"Apply" Button:** A clear action to confirm selections.
        2.  **Click-to-Dismiss:** Make the menu background clickable to close it.
  - **Date Range Filter (Row 13)**
      - **Decision:** Keep the filter as month/year-only, omitting the day selector to simplify the UI.
  - **Selected Filter Checkmarks (Row 14)**
      - **Decision:** Remove checkmarks; the color highlight is sufficient for indicating selection.
  - **Filter Names (Row 11)**
      - **Decision:** Use the long, Figma-approved names for now, despite potential readability issues.
  - **"View All" CTA Text (Row 1)**
      - **Problem:** Text color is black, not purple as per Figma.
      - **Action:** George will fix.
  - **Search Bar Copy (Row 23, SEO QA Tab)**
      - **Action:** George will update the placeholder text to Ankit's new copy.

### CVE Detail Page Enhancements

  - **Missing Sections (Row 15)**
      - **Problem:** "Technical References" and "Vendor Resources" are missing.
      - **Action:** George awaits API support from Marcus, then will style the sections.
  - **Sidebar Content Audit (Row 17)**
      - **Problem:** The sidebar is too long.
      - **Action:** George will implement a "show more" feature (hiding items \>3). Ankit suggested simplifying the date display to show only the "Discovery Date."
  - **CVE Info Table on Mobile (Row 25, SEO QA Tab)**
      - **Decision:** Make the table visible on mobile, placed after the hero section.

### SEO & Internal Linking

  - **"Related CVEs" Section (Row 24, SEO QA Tab)**
      - **Problem:** This section is critical for SEO's topical authority.
      - **Status:** On the roadmap, but deferred until critical bugs are fixed.

---

## Action Items

**Georgemaine Lourens**
- Fix 'View all' CTA color/text to match Figma
- Commit SEO QA row 23 copy update to stage
- Fix 'Top scores' View all to show only top-score CVEs
- Fix CVE sidebar: format/align items; set 'Discovery date' only
- Fix mobile hamburger close button
- Fix 'Published' filter reset; ensure page load has no pre-selected filters
- Implement filter menu UX (apply vs dismiss); prioritize after bugs
- Make CVE info table visible on mobile after hero

**Ankit Pahuja**
- Decide keep/remove vulnerability tables on mobile; inform George

---

## Transcript
**Garima Nanda:** It is evening.

**Georgemaine Lourens:** What is it?

**Georgemaine Lourens:** Oh, okay.

**Georgemaine Lourens:** Sorry?

**Garima Nanda:** What is there on your end?

**Garima Nanda:** Morning, evening?

**Georgemaine Lourens:** Afternoon.

**Garima Nanda:** It's 1 p.m.

**Garima Nanda:** Okay, here it is, 5.30 p.m.

**Georgemaine Lourens:** 5.30.

**Georgemaine Lourens:** Okay, so almost dinner time.

**Garima Nanda:** About to.

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** Hi, Ankit.

**Ankit Pahuja:** Hey, George.

**Ankit Pahuja:** Hey, garima.

**Ankit Pahuja:** Hi.

**Ankit Pahuja:** This is the first time you both are meeting, right?

**Garima Nanda:** Yeah.

**Georgemaine Lourens:** Yeah, it is.

**Georgemaine Lourens:** Should we do a quick intro?

**Ankit Pahuja:** Yeah, I think that should be helpful.

**Georgemaine Lourens:** Yeah, I can go first.

**Georgemaine Lourens:** So my name is Georgemaine, but you can call me George.

**Georgemaine Lourens:** I'm a design engineer at GrowthX, and I'm here to help you guys ship the database.

**Garima Nanda:** So shoot me all your books.

**Garima Nanda:** Yeah.

**Garima Nanda:** Okay.

**Garima Nanda:** So I am garima and I have, I am working as a senior QA for SentinelOne.

**Garima Nanda:** Okay.

**Garima Nanda:** Yeah.

**Garima Nanda:** So I can report all of the books and you can have my name and that.

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** Awesome.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** So should we start?

**Georgemaine Lourens:** What would be the best way?

**Georgemaine Lourens:** Like maybe we can go through the sheet together and then kind of like talk about the most important ones or did you have a different agenda in mind, Ankit?

**Ankit Pahuja:** Yeah, I think that should be the right approach.

**Ankit Pahuja:** So you're working on UX, UI, QA tab in the sheet and I have garima here so that, you know, she's the one who reported the most kind of managing this tab and all the findings.

**Ankit Pahuja:** So we can talk priorities.

**Ankit Pahuja:** So any of your findings, do you think we should talk about?

**Ankit Pahuja:** We could talk through.

**Ankit Pahuja:** Okay.

**Ankit Pahuja:** And grima is with us, too, just to help out on all things.

**Ankit Pahuja:** And also, I have two, three more from the other tab that I think you should know.

**Ankit Pahuja:** So I'd bring that up after we are done with this exercise.

**Georgemaine Lourens:** Okay, cool.

**Georgemaine Lourens:** Okay, let's just start top to bottom, I guess.

**Georgemaine Lourens:** I guess the first one was the view all CTA style.

**Garima Nanda:** I marked that as done.

**Georgemaine Lourens:** And you guys, too.

**Garima Nanda:** So I think we can skip that one.

**Garima Nanda:** No, George.

**Garima Nanda:** Actually, I validated this one.

**Garima Nanda:** The style is okay, but the CTA text is still different from the Figma design.

**Georgemaine Lourens:** So, yeah.

**Garima Nanda:** Okay.

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** So we can make it in same color.

**Georgemaine Lourens:** Okay, so we have purple here.

**Georgemaine Lourens:** we have Figma.

**Ankit Pahuja:** Okay.

**Georgemaine Lourens:** Here we go.

**Garima Nanda:** Oh, we have black here and purple here.

**Georgemaine Lourens:** So what I did was, I believe I stole it from the homepage.

**Georgemaine Lourens:** Oh, wait, you're right.

**Georgemaine Lourens:** Got it.

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** Let's not mark this as completed.

**Georgemaine Lourens:** Let me move the zoom controls out of the way.

**Georgemaine Lourens:** I'll just make this red for now.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** Second one, the top score CVE section is not present.

**Georgemaine Lourens:** I do think we fixed that.

**Garima Nanda:** Yeah, this is done.

**Garima Nanda:** I have added in the sheet as well.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** And how do you verify?

**Georgemaine Lourens:** Oh, like this.

**Georgemaine Lourens:** Verify looks fine, looks fine, looks fine, looks fine.

**Georgemaine Lourens:** So this one.

**Garima Nanda:** Yeah, this one I very much did.

**Georgemaine Lourens:** Okay, so this is about to search for this part, right?

**Garima Nanda:** Yeah.

**Georgemaine Lourens:** Let me see if I could fix that really quickly.

**Ankit Pahuja:** Yeah, on this one, I actually have a different suggestion that I also want to discuss.

**Ankit Pahuja:** Okay.

**Ankit Pahuja:** I did write in a copy that I could share with you that we could essentially replace while you are at it.

**Ankit Pahuja:** Why don't you?

**Ankit Pahuja:** So in the Zoom chat, I just shared this is the copy we could keep.

**Ankit Pahuja:** Reported this under SEO QA as a feedback, row number 23.

**Ankit Pahuja:** I just shared the copy that you would just use.

**Georgemaine Lourens:** Rule, sorry, where?

**Ankit Pahuja:** Can you go to the other tab?

**Georgemaine Lourens:** SEOQA, row number 23.

**Ankit Pahuja:** Yeah, 23.

**Georgemaine Lourens:** Oh, 23, sorry.

**Georgemaine Lourens:** Search.

**Ankit Pahuja:** Let's just use it.

**Georgemaine Lourens:** Let's go away with the zoom controls.

**Georgemaine Lourens:** Then we update it here too.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** Like this, right?

**Ankit Pahuja:** That's it, yeah.

**Georgemaine Lourens:** Okay, awesome.

**Georgemaine Lourens:** I'll commit that later.

**Georgemaine Lourens:** Okay, let me see if I can.

**Georgemaine Lourens:** can see

**Georgemaine Lourens:** Right, zoom controls, because, right, video panel, right, meeting controls.

**Georgemaine Lourens:** Okay, cool.

**Georgemaine Lourens:** Mark this, this is fine.

**Georgemaine Lourens:** And then the next issue was the name of the filters that they weren't matching.

**Georgemaine Lourens:** Yeah, so I changed them back to the ones that were in Figma, and also kind of like the ones that your competitor always uses.

**Georgemaine Lourens:** They're pretty long, so I need to make some changes here to the column widths.

**Georgemaine Lourens:** I personally don't mind, but my, I kind of find them to be very long, and I feel like usually filters are kind of like you scan something, and if you have them like this, you have to read it before you can.

**Georgemaine Lourens:** Actually scan it, and I feel like that usually causes a lot of overload.

**Georgemaine Lourens:** And then, but it's your choice.

**Georgemaine Lourens:** I'm fine with either.

**Georgemaine Lourens:** Do you guys have a preference?

**Garima Nanda:** We were actually following the Figma, right?

**Garima Nanda:** Ankit, because that was approved.

**Garima Nanda:** So, yeah, if we can change the design, then I think that is okay.

**Garima Nanda:** Otherwise, we have to, I think, make it similar, as per the Figma.

**Ankit Pahuja:** For now, we could just keep as per the Figma.

**Ankit Pahuja:** But I think you've already changed it, right, George?

**Georgemaine Lourens:** Yeah, it's changed there.

**Georgemaine Lourens:** It's just very long to read, just a lot of text.

**Ankit Pahuja:** Yeah, because they have Boolean values, so that kind of clears that up.

**Ankit Pahuja:** for now,

**Ankit Pahuja:** We'll just keep the long ones.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** Then I will mark this as complete for now, and I will push it later.

**Georgemaine Lourens:** The next one is clicking on view all shows all 250 results.

**Georgemaine Lourens:** Yes, that's correct.

**Georgemaine Lourens:** I think I have a fix for that.

**Georgemaine Lourens:** Because the filtering was incorrect, so the top scores should only show the ones that match the top scores.

**Georgemaine Lourens:** And the latest CVEs, that should show everything, but it should be sorted by date because the most recent should be at the top, which is correct.

**Georgemaine Lourens:** And the high profile ones, I think that was also part of the issue.

**Georgemaine Lourens:** see.

**Georgemaine Lourens:** see.

**Georgemaine Lourens:** That now correctly shows only the high-profile ones.

**Garima Nanda:** Yeah.

**Garima Nanda:** But, George, the last section where we are showing the, what is that?

**Georgemaine Lourens:** Yeah, top scores.

**Garima Nanda:** Yeah.

**Garima Nanda:** So when I validated this issue, I can see total 250 records again in top score.

**Garima Nanda:** Because top score CV section was not present in the initial phase, right?

**Georgemaine Lourens:** Yeah, that's correct.

**Garima Nanda:** But now when I'm checking view walls, CTA here, they're showing 250 records again, which is incorrect.

**Georgemaine Lourens:** Yeah, that's correct.

**Georgemaine Lourens:** So we're currently on my local host because I've been actively working on some of these.

**Georgemaine Lourens:** So some of these things might not be on your branch yet, but they will be later.

**Georgemaine Lourens:** I'm still fixing some stuff.

**Georgemaine Lourens:** So I will just update this sheet.

**Georgemaine Lourens:** as soon as I push it from my local branch to the stage environment.

**Garima Nanda:** Is that okay?

**Garima Nanda:** Yeah, that is fine.

**Georgemaine Lourens:** Okay, then let's maybe unclick the validated part.

**Garima Nanda:** This is very different, but the issue was for the top score series, which is kind of pending right now.

**Georgemaine Lourens:** Yeah, where was it again?

**Georgemaine Lourens:** There's so many rows here.

**Georgemaine Lourens:** No, number 10.

**Georgemaine Lourens:** 10.

**Georgemaine Lourens:** Okay, yeah.

**Georgemaine Lourens:** Let's unvalidate that one.

**Georgemaine Lourens:** Then we have 11 fields of the name are different.

**Georgemaine Lourens:** Yeah, we just checked that.

**Georgemaine Lourens:** That was about this one, the CESA and the known exploit.

**Georgemaine Lourens:** So I updated those, which was number 11.

**Georgemaine Lourens:** Okay, cool.

**Georgemaine Lourens:** And then 11, 1.

**Garima Nanda:** I'm currently working on this bug.

**Garima Nanda:** So you added the comment there, and I have also put my comment.

**Garima Nanda:** So if you need the clarity, I can explain.

**Georgemaine Lourens:** No, I understand the bug.

**Georgemaine Lourens:** I just need to find a solution.

**Georgemaine Lourens:** I'm working on this right now.

**Georgemaine Lourens:** This is on my radar.

**Georgemaine Lourens:** In the filter menu, there is no option to select the date range.

**Garima Nanda:** I believe that should be.

**Garima Nanda:** Yes, George.

**Garima Nanda:** So you have added the month and year range, right?

**Garima Nanda:** Yeah.

**Garima Nanda:** When I'm verifying it, I can see the date as well.

**Garima Nanda:** Which should be in the range.

**Garima Nanda:** Right now we are showing month and year.

**Georgemaine Lourens:** Yeah, wait, let me go to the link that you guys are using.

**Georgemaine Lourens:** SentinelOne, which is this one.

**Georgemaine Lourens:** I believe.

**Georgemaine Lourens:** So this is month, this is year, this is from, this is to, this is month, this is year.

**Georgemaine Lourens:** So in the Figma design, essentially, it was...

**Garima Nanda:** The date is also there.

**Georgemaine Lourens:** Yeah, but the date, do you guys really need the date?

**Georgemaine Lourens:** Because the date is kind of like not necessary, right?

**Ankit Pahuja:** Yeah, I also think so.

**Ankit Pahuja:** It should be fine if we have month in there.

**Garima Nanda:** Hmm, okay.

**Ankit Pahuja:** Yeah, just month in there should be fine.

**Garima Nanda:** Yeah.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** Okay, let's mark that one as complete.

**Georgemaine Lourens:** Yeah, we did.

**Georgemaine Lourens:** The next one is selected filters are not showing the right tick.

**Georgemaine Lourens:** Oh, you mean the check mark.

**Georgemaine Lourens:** Yeah, so I intentionally removed those because it was a lot of noise, but I'm happy to add them back if you guys feel very strongly about it.

**Georgemaine Lourens:** But it felt like the color was already making it quite obvious.

**Garima Nanda:** Yeah.

**Garima Nanda:** What do you think, Ankit?

**Ankit Pahuja:** I'm fine by that, too, because I was also in the notion that if you have a color highlighted, we should.

**Ankit Pahuja:** Yeah, measure the light, yeah.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** Then let's mark this as purple.

**Georgemaine Lourens:** Okay, getting somewhere on the details page, technical references and vendor resources are missing.

**Georgemaine Lourens:** That is correct.

**Georgemaine Lourens:** I asked Marcus to include that in the API.

**Georgemaine Lourens:** And as soon as he wakes up, he's going to look into it and then he will provide.

**Georgemaine Lourens:** And then I will style it.

**Georgemaine Lourens:** So this one, we're aware of this.

**Georgemaine Lourens:** The heading text, such as vulnerability, details, blah, blah, blah.

**Georgemaine Lourens:** We're talking about these things, right?

**Garima Nanda:** Yeah.

**Garima Nanda:** So this was done.

**Garima Nanda:** I verified it.

**Garima Nanda:** But the two fields I think are missing there, which I mentioned in the previous work.

**Garima Nanda:** So when you will add the...

**Georgemaine Lourens:** These two, Yeah.

**Garima Nanda:** Whenever you would be adding technical references and vendor resources, you can make these two bold as well.

**Garima Nanda:** So this would fix.

**Georgemaine Lourens:** Okay, cool.

**Georgemaine Lourens:** Then I am going to mark this.

**Georgemaine Lourens:** Text alignment is not present for text at the right hand.

**Georgemaine Lourens:** I believe this is about these, right?

**Garima Nanda:** Mm-hmm.

**Georgemaine Lourens:** Okay, I think I have fixed that locally.

**Georgemaine Lourens:** Let me see if I have one of these pages open.

**Georgemaine Lourens:** No, this is not the right one.

**Georgemaine Lourens:** Is this a better one?

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** So some of this data was just unformatted, so I made a list out of it.

**Georgemaine Lourens:** But some of these can be quite long, so I added a check that looks if there's more than three, then it hides the rest and then only shows three.

**Georgemaine Lourens:** And if you click it, then you show more, which is pretty similar to how Wiz handles it as well.

**Georgemaine Lourens:** But what I also realized is that we're showing quite a bit of information in this sidebar.

**Georgemaine Lourens:** I would love it if you guys could review, do an audit on everything.

**Georgemaine Lourens:** Everything that we show in this bar and kind of like make sure that everything that needs to be here is here and everything that doesn't need to be here shouldn't, so that we can remove it, because otherwise it's going to be quite long.

**Ankit Pahuja:** Yep, I do have put in suggestions around the first three, where we have dates and then last updated date and then month and year.

**Ankit Pahuja:** So probably we need to have just a discovery date here and have had the suggestion inside of SEO QA that Marcus can look at.

**Georgemaine Lourens:** Okay, let me write that down before I forget it.

**Georgemaine Lourens:** Only show discovery.

**Georgemaine Lourens:** Sorry.

**Georgemaine Lourens:** Discovery date.

**Georgemaine Lourens:** Remove.

**Georgemaine Lourens:** Published.

**Georgemaine Lourens:** Published is to discovery date, right?

**Ankit Pahuja:** Yeah, that should be great.

**Ankit Pahuja:** I think, yeah, published date is 20.

**Ankit Pahuja:** 24, so probably yes, yeah.

**Ankit Pahuja:** It should be the CV discovery date, essentially, yeah.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** All right, that's two.

**Georgemaine Lourens:** But I think the question still remains.

**Georgemaine Lourens:** It's not super high priority.

**Georgemaine Lourens:** I think the first thing that I will do is make sure that everything is styled and formatted correctly.

**Georgemaine Lourens:** But I think it will be nice at some point to kind of, like, look at it because a lot of this information, it's going to be a lot.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** Let's go to number 19.

**Georgemaine Lourens:** Or actually, we were on number 18.

**Georgemaine Lourens:** On mobile devices, the close button is missing from the hamburger menu.

**Georgemaine Lourens:** Yeah, I saw that.

**Georgemaine Lourens:** I am not sure what happened there because I didn't touch the global navigation, but I will look in.

**Georgemaine Lourens:** To it, I'm aware of it.

**Georgemaine Lourens:** You should be able to see all of the vulnerability tables.

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** Did you guys read my comment on this?

**Garima Nanda:** Yes, I did.

**Garima Nanda:** I did.

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** Any thoughts on that?

**Georgemaine Lourens:** I don't have a, well, I do have a strong opinion on this, but I will leave the final call with you guys.

**Garima Nanda:** But I would advise against it.

**Ankit Pahuja:** I'd get back to you on this.

**Ankit Pahuja:** I'll just take a few more opinions here.

**Ankit Pahuja:** I don't want people coming back to us later and asking for it.

**Ankit Pahuja:** So I'll just take opinions here.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** Let's leave that open then.

**Georgemaine Lourens:** Let's move to number 20, if you will.

**Georgemaine Lourens:** number Let's 24.

**Georgemaine Lourens:** go.

**Georgemaine Lourens:** Are we spaced?

**Georgemaine Lourens:** Yeah, I saw that.

**Georgemaine Lourens:** I'm aware of it.

**Georgemaine Lourens:** To be honest, like all of these issues, I think we can go one by one, but I didn't work on them yet.

**Georgemaine Lourens:** Except for this.

**Ankit Pahuja:** We can then keep them for tomorrow, once we have.

**Ankit Pahuja:** Yeah.

**Georgemaine Lourens:** Is there any issue in here specifically that you would like to discuss from the ones that we didn't go through yet?

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** Maybe.

**Garima Nanda:** There is an issue with the filters on the, it is now, I think it is because of some cache issue, but I tried the same by opening it in private window, but still it is coming up.

**Garima Nanda:** So you can see.

**Garima Nanda:** I think it is at the bottom of the sheet.

**Georgemaine Lourens:** The bottom of the sheet?

**Garima Nanda:** This one?

**Georgemaine Lourens:** Or is it this one?

**Garima Nanda:** This is row number 26 and 27.

**Georgemaine Lourens:** The publish filter does not reset.

**Garima Nanda:** So what is happening?

**Garima Nanda:** For example, if I have put the filter for published for the first time and it is showing the result.

**Garima Nanda:** And if I try to reset this filter, it doesn't do at the first click.

**Garima Nanda:** And I have to, you know, click it for the multiple times.

**Garima Nanda:** Sometimes it reset in the second click and sometimes it doesn't.

**Garima Nanda:** And the other issue is it is happening on all the devices on my end.

**Georgemaine Lourens:** Okay, so if I click here, and then I reset.

**Georgemaine Lourens:** This is fine.

**Garima Nanda:** It is fine for us.

**Garima Nanda:** Just the issue with the published one.

**Georgemaine Lourens:** Oh, with the published one.

**Georgemaine Lourens:** Okay, so this one doesn't reset.

**Garima Nanda:** Yes.

**Georgemaine Lourens:** Okay, so right now there's no results.

**Georgemaine Lourens:** There's all results.

**Georgemaine Lourens:** Yeah, you don't see it if you look at this.

**Georgemaine Lourens:** Let's see.

**Georgemaine Lourens:** I want all from 2025.

**Georgemaine Lourens:** It shows me 213 results, and then it flares.

**Georgemaine Lourens:** Okay, and this happens for you on mobile.

**Georgemaine Lourens:** On all the devices.

**Garima Nanda:** Yeah, on all the devices.

**Garima Nanda:** And if I take the URL for this, and try the same in the other device, it still shows me the...

**Georgemaine Lourens:** Results with the filter selected.

**Georgemaine Lourens:** We have one second.

**Georgemaine Lourens:** One second, I'm sorry.

**Georgemaine Lourens:** Okay, vandoor.

**Georgemaine Lourens:** Okay, vandoor.

**Georgemaine Lourens:** Volsma, ja, topi.

**Georgemaine Lourens:** Fijn dag, dankjewel.

**Georgemaine Lourens:** I'm so sorry about that.

**Georgemaine Lourens:** Okay, I'm opening it now on my mobile device.

**Georgemaine Lourens:** So, let's see.

**Georgemaine Lourens:** I want to track everything from October 2025 to November.

**Georgemaine Lourens:** And then I'll try reset.

**Georgemaine Lourens:** It is working on my end, but I will try it on some other devices to see if I can reproduce it.

**Georgemaine Lourens:** Can you stably reproduce it on your end?

**Garima Nanda:** Yes, yes, I am.

**Georgemaine Lourens:** I enjoy it.

**Georgemaine Lourens:** Can you share?

**Garima Nanda:** Yeah, I would.

**Georgemaine Lourens:** Let me see if I can get my Zoom controls back because I hit them.

**Georgemaine Lourens:** Stop sharing.

**Georgemaine Lourens:** Ah, there we go.

**Georgemaine Lourens:** Can you share?

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** And Zoom.

**Garima Nanda:** Can you see it is, I just opened this, and it is showing me the reset one, right?

**Garima Nanda:** And if I go here and check in the published, it is still taking the published filters that values that we gave, right?

**Georgemaine Lourens:** Oh, yeah.

**Georgemaine Lourens:** Oh, yeah.

**Georgemaine Lourens:** No, I understand that.

**Georgemaine Lourens:** I had a choice.

**Georgemaine Lourens:** So, basically, you could look at this page in two ways.

**Georgemaine Lourens:** Either you show all of the CVEs, and that means that you are filtering on the earliest to the latest, or you could just leave the values empty and just show everything.

**Georgemaine Lourens:** But then you, in order to filter, you kind of need to select two dates.

**Georgemaine Lourens:** And I thought that maybe it would be easier to start with showing a date range from the earliest to the latest.

**Georgemaine Lourens:** But that does mean that there's a filter active, which is technically correct, but not really.

**Garima Nanda:** I thought initially it is because of the cache issue.

**Garima Nanda:** So I tried the same URL in the incognito, in the private window as well.

**Garima Nanda:** There also, I can see the filter is already selected.

**Garima Nanda:** You can see it, right?

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** So what would you expect to see here?

**Garima Nanda:** No filters active.

**Garima Nanda:** No

**Garima Nanda:** Yeah, if I open the URL again in any of the devices or even in the incognito or private window, right, we should not have the property selected.

**Garima Nanda:** Okay.

**Garima Nanda:** You can see if I click on this reset for the ones, it doesn't, right, it did not.

**Garima Nanda:** And if I click on it again, then it works.

**Garima Nanda:** That is what the two issues are about.

**Georgemaine Lourens:** Okay, I think I understand it.

**Georgemaine Lourens:** Okay, all right.

**Georgemaine Lourens:** I will look into that.

**Garima Nanda:** Yeah.

**Georgemaine Lourens:** Okay, is there another issue that you wanted to discuss?

**Garima Nanda:** Let see.

**Ankit Pahuja:** I do have two issues from that list, but I'd let Karima complete.

**Garima Nanda:** I'm done, Ankit, you can.

**Ankit Pahuja:** Can we look?

**Ankit Pahuja:** Okay.

**Ankit Pahuja:** At 23, row number 23.

**Georgemaine Lourens:** 23, yes.

**Ankit Pahuja:** So it's more like a feedback.

**Ankit Pahuja:** Also wanted your opinion.

**Ankit Pahuja:** So once we start filtering, say we have selected options, filter options.

**Ankit Pahuja:** So we have to go back and click filter again to close this window.

**Georgemaine Lourens:** Or to apply filters.

**Ankit Pahuja:** Clicking anywhere else doesn't auto apply or there's no apply button.

**Ankit Pahuja:** So just I was just thinking if it's a good UX practice or just will be clear for all users who just come here, they click on filter, select their options.

**Ankit Pahuja:** And the last step is to go back to filter and click that again to apply those filters.

**Georgemaine Lourens:** So should we have an applied budget?

**Ankit Pahuja:** Yeah.

**Ankit Pahuja:** Or...

**Ankit Pahuja:** Yeah.

**Ankit Pahuja:** Should we just allow clicking anywhere, applies the filters, or what would be the good UX word?

**Georgemaine Lourens:** Right.

**Georgemaine Lourens:** Okay, that's a good question.

**Georgemaine Lourens:** So the way that it works right now is that because you can select multiple ones, usually you would select one and then it automatically closes, but then you would constantly have to open it again.

**Georgemaine Lourens:** And so that's why clicking the options doesn't close it.

**Georgemaine Lourens:** And I think the options that I have to close it are either you click this, or you click the same label, or you click outside of the menu.

**Georgemaine Lourens:** But this isn't very visible, I guess.

**Georgemaine Lourens:** But inside of the menu, everything is, doesn't dismiss it.

**Georgemaine Lourens:** I think there's a couple of things that we can

**Georgemaine Lourens:** Could do.

**Georgemaine Lourens:** I think what we could do is anywhere that isn't an option.

**Georgemaine Lourens:** So let's say, let me make this red to make it a bit more obvious.

**Georgemaine Lourens:** Background red.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** So I think what we could do is say everything that is red and is not an option.

**Georgemaine Lourens:** If we click that, then it closes.

**Georgemaine Lourens:** That way it's very close to your mouse, right?

**Georgemaine Lourens:** So I click here and I'm done and I just click here and then it closes, right?

**Georgemaine Lourens:** I think that could be an option.

**Georgemaine Lourens:** Another option would be you have to select everything and then we add a save button somewhere, but then you have to drag your mouse all the way there.

**Georgemaine Lourens:** And I think if you then close and it's not applied, it might.

**Georgemaine Lourens:** So either we add more ways to close it, or we only add a button to apply, and then apply closes it, which basically means that you add a close button, right?

**Ankit Pahuja:** A close and safe button.

**Ankit Pahuja:** To me, intuitively, I prefer an apply button, so that it's really clear.

**Ankit Pahuja:** Select options, click on apply, you get a filter results.

**Georgemaine Lourens:** And what would you, so if the user then selects all of these and then closes, then nothing is applied.

**Georgemaine Lourens:** And basically all of this is reset again, right?

**Ankit Pahuja:** Yeah, I think that, yeah.

**Georgemaine Lourens:** I think that would make it more clicks.

**Georgemaine Lourens:** But, up to you.

**Georgemaine Lourens:** Do you have a strong opinion?

**Ankit Pahuja:** I think I don't have a strong opinion on that.

**Ankit Pahuja:** I'm just wanting to solve this confusion that after selecting, right now, it's not really clear that, okay, I have to go back to, the first time I was using, I, I, wasn't clear to me that I have to go back to filters, click on it, and kind of, yeah, even I, I, found that, yeah.

**Garima Nanda:** Okay.

**Garima Nanda:** That was how to proceed further.

**Georgemaine Lourens:** Let me think about this one.

**Georgemaine Lourens:** I think, I think I will tackle this one last, because I think there are some more important ones, like real bugs, but I think, an easy fix would just be, make it more obvious that the background's here.

**Georgemaine Lourens:** It's clickable, and just click anywhere to dismiss it.

**Georgemaine Lourens:** I think adding a button would just make it more complex, but we can also try that.

**Georgemaine Lourens:** I'll just write that down.

**Ankit Pahuja:** If you think just adding a button, say, apply, clicking on that just closes it, that also just could be fine, and we could avoid the other rule that you mentioned, and clicking it anywhere else resets.

**Ankit Pahuja:** Essentially, somebody is on the filter button to apply filters, right?

**Ankit Pahuja:** So we could avoid the resetting by clicking anywhere else, but we could just have an apply button that essentially does what other buttons are doing, just closing it, closing the filter menu.

**Georgemaine Lourens:** Yeah.

**Ankit Pahuja:** I made an alt here.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** Anything else?

**Georgemaine Lourens:** Anything else?

**Georgemaine Lourens:** But we need to go over, or should I just?

**Ankit Pahuja:** Yeah, I think the last one, row number 25, on the web design, we have the table on the right for individual pages, but on the mobile devices, we don't have the CV information table.

**Georgemaine Lourens:** Yeah, I took a look at how you guys are handling that on the cybersecurity page, and just kind of went with that.

**Georgemaine Lourens:** So kind of here, you have like the contents, and then the content, and then whenever it goes to mobile, it just kind of disappears.

**Georgemaine Lourens:** So I reuse that behavior, but I think we can totally just keep it visible.

**Georgemaine Lourens:** On mobile, it just makes the page a bit longer to scroll, but I guess essentially like the sidebar is a summary of the whole articles.

**Georgemaine Lourens:** So, maybe it makes sense to keep it visible.

**Ankit Pahuja:** I'm fine with that.

**Ankit Pahuja:** We'd make it visible, and we'd keep it right after the hero section.

**Georgemaine Lourens:** Yeah, sure.

**Georgemaine Lourens:** Let's call that a feature request, then.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** All right.

**Georgemaine Lourens:** Cool.

**Georgemaine Lourens:** Then, I think I will just continue to try to fix as many as the bugs as I can.

**Georgemaine Lourens:** I will prioritize the P0s first, and then move downwards.

**Ankit Pahuja:** All right.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** Anything else that I should be aware of, or Marcus should be aware of, before we wrap this up?

**Ankit Pahuja:** This is something I discussed with Marcus, sorry.

**Ankit Pahuja:** The last one, again.

**Georgemaine Lourens:** Yesterday.

**Ankit Pahuja:** Something that sits on Figma, but I thought I'd also discuss with you so that we are all on the same page.

**Ankit Pahuja:** This is under SEO QA, row number 24, that talks about deleted section on individuals.

**Georgemaine Lourens:** Yeah, I saw that one.

**Georgemaine Lourens:** I brought it up with John in Jury.

**Georgemaine Lourens:** I hope I'm not butchering his name.

**Georgemaine Lourens:** And he mentioned that we could add it, but he wants to wait with fixing all of the bugs first and then add them as last.

**Georgemaine Lourens:** So it's on the radar.

**Ankit Pahuja:** It's just at the bottom of the list.

**Ankit Pahuja:** I just wanted this to be taken care of because for SEO, internal linking is super important just to keep the topical authority and tie everything back.

**Ankit Pahuja:** So I just wanted to keep this on the radar.

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** It's on the radar.

**Georgemaine Lourens:** It's the radar.

**Ankit Pahuja:** Thank you.

**Georgemaine Lourens:** All right.

**Ankit Pahuja:** All right, thank you guys for going over time, and I will report back as soon as most of the bugs have been fixed.

**Georgemaine Lourens:** Thanks, George.

**Georgemaine Lourens:** Thanks, garima.

**Georgemaine Lourens:** All right, ciao.
