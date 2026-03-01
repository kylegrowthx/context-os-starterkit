# SentinelOne <> Growth X - Weekly Sync

<metadata>
date: 2026-01-07
time: 13:29 UTC
duration: 20 minutes
organizer: Team GrowthX
participants:
  - name: Bailey Seybolt
    email: bailey@growthx.ai
    affiliation: GrowthX
  - name: Marcus Derencius
    email: marcus@growthx.ai
    affiliation: GrowthX
  - name: Ankit Pahuja
    email: ankit.pahuja@sentinelone.com
    affiliation: SentinelOne
  - name: Mansi Bhalothia
    email: mansi.bhalothia@sentinelone.com
    affiliation: SentinelOne
  - name: Drew Hoffman
    email: drewh@sentinelone.com
    affiliation: SentinelOne
  - name: Mahendra Desarda
    email: mahendra.desarda@sentinelone.com
    affiliation: SentinelOne
  - name: Mahati Rapol
    email: mahati.rapol@sentinelone.com
    affiliation: SentinelOne
  - name: Marisol Smith
    email: marisol@growthx.ai
    affiliation: GrowthX
fathom_recording_id: 112369753
fathom_url: https://fathom.video/calls/522936332
share_url: https://fathom.video/share/F297XKsPP_K-KJ2VyNY9PjnFCxEomXrU
source: fathom
enriched_on: 2026-02-28 04:32:00 UTC
</metadata>

---

## Summary

GrowthX and SentinelOne reviewed four critical issues on CVE pages pending publication, with Marcus committing to implement fixes by end of day. The team agreed to prioritize publishing new CVE content over updating existing pages, and Bailey will share the CS101 article template for SentinelOne to review and trim required sections to manage length. Both teams aligned on shifting to biweekly strategic meetings with daily progress updates via Slack.

---

## Context

This is a weekly operational sync between the GrowthX content team (Bailey, Marcus) and SentinelOne's product marketing team (Ankit, Mansi). GrowthX is a content marketing partner supporting SentinelOne's CheckThat product—an AI visibility index for B2B. The meeting occurred after the holiday break and focused on unblocking content publication and clarifying collaboration workflow. SentinelOne's content needs span CVE vulnerability pages and CS101 educational articles; both projects require iterative feedback and format standardization.

---

## Relevance

- **Content QA:** Critical bugs in staging CVE pages must be fixed before weekly publication can resume
- **Workflow alignment:** Clarification on publishing priority (new content first vs. updating existing pages)
- **Scope management:** CS101 article length creep (3,000+ words) requiring template review and section trimming
- **Reporting & automation:** Slack-based status updates replacing manual tracking
- **Strategic planning:** Early-February planning session to align on 2026 strategy and SentinelOne's internal FI27 fiscal planning

---

## Overview

- **CVE Fixes:** Four issues were identified on staging CVE pages (e.g., repetitive CVSS vectors, naked URLs). Marcus will fix them today, enabling new page publication this week.
- **CS101 Strategy:** Articles are too long (\~3k words), risking performance. GrowthX will share the template for SentinelOne to trim sections and will provide new topics next week to build a content runway.
- **Meeting Cadence:** The sync is shifting to biweekly to focus on strategic insights and reporting, with daily progress updates moving to Slack.

---

## Key Topics

### CVE Page Review & Fixes

  - **Context:** Marcus pushed three updated CVE pages to staging for review, addressing an initial visual bug.
  - **New Issues Identified:**
      - **Repetitive Content:** The CVSS vector string appears in both the sidebar and body text.
          - **Fix:** Remove from body text; keep in sidebar for readability.
      - **Ambiguous Links:** Multiple "Technical References" links have identical anchor text but lead to different URLs.
          - **Fix:** Add descriptive text to each link to clarify its destination.
      - **Naked URLs:** Raw, clickable URLs appear in the body content.
          - **Fix:** Hyperlink descriptive text instead of showing the full URL for better SEO hygiene.
      - **Incorrect Formatting:** "Detection Strategies" sections are sometimes unbulleted, despite being a list.
          - **Fix:** Ensure all list-like content in this section is bulleted.
  - **Path Forward:**
      - Marcus will implement fixes today.
      - GrowthX will publish new CVE pages this week.
      - **Priority:** Publish new pages first; update existing pages later.

### CS101 Content Strategy

  - **Status:** Four new articles are ready for review.
  - **Issue:** Articles are too long (\~3,000 words), which can negatively impact performance.
  - **Action:** GrowthX will share the article template for SentinelOne to review and trim required sections to manage length.
  - **Content Runway:** GrowthX will provide new article topics next week to ensure a consistent pipeline.

### Reporting & Planning

  - **Airtable Sync:** Mansi is updating Airtable statuses. GrowthX will create a Slack automation to notify the team of status changes in real-time.
  - **2026 Planning:** A strategy session is scheduled for early February, aligning with SentinelOne's internal FI27 planning.
  - **Reporting:** The December deep-dive report is delayed due to holiday schedules and will be shared next week.

---

## Action Items

**Marcus Derencius (GrowthX)**
- Fix CVE pages per Ankit: remove CVSS from body, hyperlink naked URLs, add refs labels, bullet Detection Strategies; then publish new CVEs
  - Timeline: Complete today (2026-01-07)
  - Status: Committed as "quick fixes"

**Bailey Seybolt (GrowthX)**
- Share CS101 template w/ Ankit & Mansi; then collect feedback
  - Goal: Reduce article length from 3,000+ words to manageable scope
- Set up Airtable→Slack automation for publish-status updates
  - Owned by Bailey; eliminates manual status messaging
- Schedule early Feb 2026 planning session w/ Ankit & Mansi
  - Aligns with SentinelOne's FI27 fiscal planning

---

## Transcript

### Holiday Greetings & Catch-Up (00:01–00:03)

**Bailey Seybolt:** Hi.

**Mansi Bhalothia:** How are you?

**Bailey Seybolt:** How was your vacation?

**Bailey Seybolt:** Oh, it was great. I went on a big trip to Ecuador, to the Galapagos with my family. So it was a very special holiday. How about you?

**Mansi Bhalothia:** I also had a special one. So I went on a bachelor's trip to Bali.

**Bailey Seybolt:** Oh, my God. So fun.

**Mansi Bhalothia:** Yeah, it was fun.

**Bailey Seybolt:** I haven't been, but I lived in Vietnam for a few years and traveled a little bit to Bali and Indonesia.

**Mansi Bhalothia:** And it was so stunning—the beaches and like the volcanoes rising from the ocean.

**Bailey Seybolt:** How fun. Hi, Marcus.

**Marcus Derencius:** Hello, hello.

**Bailey Seybolt:** Happy New Year. How was your holiday, Marcus? Did you go on a trip?

**Marcus Derencius:** Yeah, no, this time I just stayed home with my parents because they came to visit me. So they are in Brazil, then they came to Portugal to visit me. But now they are gone, and I'm traveling a little bit.

**Bailey Seybolt:** Oh, well, so it was a travel for them. But staying home during the holidays is pretty nice too sometimes.

**Marcus Derencius:** Yeah, and for that it was the first time seeing Christmas in the cold.

**Bailey Seybolt:** Yeah, it's true. I was in Ecuador this year with my kids and we live somewhere very cold and snowy.

**Marcus Derencius:** So they had the opposite. What's it feeling—is it still Christmas if you're somewhere on a beach with palm trees? Exactly.

**Bailey Seybolt:** Hi, Ankit.

**Ankit Pahuja:** Happy New Year.

**Bailey Seybolt:** Is it just us today? Should I jump in or do you think we're waiting? Okay, great. Well, Happy New Year, everybody. Welcome back. I know we have a few things to talk through today.

---

### CVE Page Review & Fixes (00:03–00:12)

**Bailey Seybolt:** And since we have Marcus, I was wondering if it maybe made sense to talk through the CVE updates. Actually, maybe I'll share the document that you left feedback on instead. Our editorial team went through and updated some of the three pages that she had left as an example in draft mode already. But I feel like maybe it would be helpful for your team to just talk through any of the issues you're still seeing. And maybe Marcus can speak to what we can kind of update in the pipeline to capture it, and then anything else I can kind of bring to our editorial team to make sure we can take care of that as well.

**Marcus Derencius:** Yeah, I addressed all the issues in our publishing workflow and sent three CVE entries to staging in draft mode for you to review and see if there's any remaining issue. So yeah, we are kind of waiting for feedback to decide how to move forward.

**Ankit Pahuja:** Sounds good. Yeah, Marcus, go ahead. So yeah, Bailey, would you mind if I share my screen? I would be able to show that in staging and it should just get easier.

**Bailey Seybolt:** Yeah, that's perfect.

**Ankit Pahuja:** All right. So from the issues we reported, we reported five of them. Let's zoom this a bit. So, um, mostly content-specific things and some that were around formatting. So this one is fixed—the CVSS vector content was overlaying the other visual element. This is fixed. We confirm. And let's go for other issues one by one. So this is what you pushed probably. And I see the fixed version here. Okay. There's no overlay. And let's talk about other issues. So this is the staging environment. That's how we see.

**Ankit Pahuja:** And let's talk about this. So I think in the content under vulnerability analysis, we do refer to the CVSS vector again, which is on the sidebar as well. So we might want to take that out just for better readability. That's a content ask. Do you want to talk more about it, or do we agree on fixing this?

**Marcus Derencius:** Yeah.

**Bailey Seybolt:** Yeah, I agree, yes, sounds good. We're good, so we should leave that in the sidebar, just to be clear, and we'll—

**Marcus Derencius:** Take it out of the body text of the article.

**Ankit Pahuja:** That's right. Yeah. This one's fixed.

**Ankit Pahuja:** Technical references. So, like for this article, here we have multiple technical references. These are different pages, but they're different URLs. So we want to make this a bit more descriptive, maybe add a few pieces with this about what this is, or just add a label, because this feels like all these are the same link, you click on it, but you get to different pages. So given these are different pages, let's visually tell people that they're different.

**Marcus Derencius:** Yeah, okay. I see. I checked on the other and you should see that still remains on this one.

**Ankit Pahuja:** Okay, all right. Next one. So in the body content, we have naked URLs, and they are clickable. So we might want to hyperlink here and not leave naked URLs in the body content.

**Marcus Derencius:** Okay.

**Ankit Pahuja:** No, hyperlink on the text. Yeah. So basically, it's for good SEO hygiene where we don't want to leave naked URLs within the body content, especially when they are clickable. We want them clickable, but we want them on a hyperlink.

**Marcus Derencius:** Okay.

**Ankit Pahuja:** Okay, so there was another section, which is a Detection Strategies section. Okay, this is another CVE page. And yeah, in the detection strategies, it looks like this content should be bulleted. And this is not. So we might want to fix this type of issue on other pages as well.

**Marcus Derencius:** Okay, I'll check.

**Ankit Pahuja:** We can identify those sections to make them bulleted. Yeah, I think how we would have prompted for the tool to generate output might be always bulleted, because other pages that we have generated as well for CVEs were all bulleted in the previous examples. If they are non-bulleted but by the structure of content it reads like they are bulleted.

**Marcus Derencius:** Exactly.

**Ankit Pahuja:** Yeah. So I think we might just want to put everything, every pointer bulleted in detection strategies, if the prompt supports that too.

**Bailey Seybolt:** I think that makes sense, especially if it's the intro with the colon. It should be able to bullet what each of the detection strategies are coming out of it.

**Ankit Pahuja:** That's right. Yeah, I think from the list, one of five are fixed, the four remains. We might want to fix those before we publish next ones. And I think these to me read like quick fixes. If they look the same to you as well, we could probably push something this week live.

**Marcus Derencius:** Yeah. Okay. I work on that today. So hopefully they all look like simple fixes.

**Ankit Pahuja:** Yeah. All right.

**Bailey Seybolt:** All right. Great. Thank you all for such clear feedback.

**Marcus Derencius:** That'll make it a lot easier to make those updates.

**Bailey Seybolt:** Okay, great. So we will work on those and I'll follow up too when that's updated async and hopefully we can get the rest of those pages out this week.

**Ankit Pahuja:** All right. So just a quick comment on the publishing. After the fixes, of course, we might want to start putting those batches out on a frequency that we discussed. And we are wanting to generally put more pages out for CVE and make this database look like a database now.

**Bailey Seybolt:** Okay, that sounds great. Yeah, as soon as we kind of update that, we can get back to publishing on that updated release plan. And I also wanted to ask, do you want us also to go back and update the existing ones or just focus on publishing new content, new CVE entries for now?

**Ankit Pahuja:** I think we could publish new CVE entries for now and then we can update them.

**Bailey Seybolt:** Okay, sounds good. So we'll focus on that for now. Okay, great. So we'll get on those updates.

---

### CS101 Articles & Content Length (00:13–00:15)

**Bailey Seybolt:** For CS101, we have four new articles coming. I think we've updated the articles based on the existing feedback, so I'm not sure if you had anything else you want to touch base on there. I noticed that we're still okay on new article topics, but I think to get ahead, we'll have some new article topics for you to review and approve next week, so we can kind of build out a longer content runway for CS101.

**Bailey Seybolt:** In terms of article format and length, I did want to touch base on length to make sure you're okay with the length, because I know that some of them are pushing sort of 3,000 words and there's maybe one or two that have even gone over. I wanted to include the template here in case you wanted to take a look and make sure it still aligns with your requirements for this type of article and see if there's any standard sections that you'd want to trim. I'll share that with you and Mansi, and if you want to go in and take a look and let us know if there are any sections you want us to remove from the template, because I know that articles this long can sometimes affect performance.

**Ankit Pahuja:** Yeah, I think that should be good. We could revisit once.

**Bailey Seybolt:** Okay.

---

### Airtable Status Updates & Automation (00:15–00:16)

**Bailey Seybolt:** And then I also wanted to ask, I know I've been sort of offline over the holidays, if there was any new content that had been published that we should update on Airtable. And I just wanted to confirm, Mansi, when you publish, are you going in and updating the status on Airtable?

**Mansi Bhalothia:** I am. For more visibility, I can also put it on a group. As we will publish in the coming week, we haven't published anything since last December. PMMs were also on leave. But I am updating the Airtable status and for more visibility, I can just write down a message to you.

**Bailey Seybolt:** You don't have to do that. I can set up an automation so that when you update the status, it lets us know on Slack. I just want to confirm that you're doing that to make sure that we're updating our reporting in real time. So if you're doing it on Airtable, then I will just create an automation to let us know on Slack as soon as you do that.

**Mansi Bhalothia:** That makes sense.

---

### Strategic Planning & Meeting Cadence (00:16–00:19)

**Bailey Seybolt:** And then I did want to touch base briefly on planning. We're scheduling kind of sessions mostly in January to talk about your 2026 goals and check and see if we need to revisit any of our strategy. I know that you all were having some of these meetings internally as well. And so we had sort of talked about late January or early February. So I did just want to touch base and put something on the calendar and see what made the most sense for your team.

**Ankit Pahuja:** Early February would be better. And I think by then we'd also have clarities on how we'd want to approach and plan for FI27.

**Bailey Seybolt:** Okay. That sounds great. Well, I'll just put it on the calendar so that it's there and we can always adjust as necessary. And next week we'll be sharing also the kind of monthly deep dive reporting from December. I'm trying to get everything done, but obviously it's a little bit behind since we started this month on January 5th. So that will be coming.

**Bailey Seybolt:** And then the other planning thing is we are shifting our meeting cadence to biweekly, so every other week to have these meetings. And this is to allow us to focus the meeting time kind of more around strategic insights and content performance and less about project management. So the goal would be basically we would obviously still be available on Slack. We'd still be working at the same cadence, but we would sort of use weekly Slack updates to cover just the usual progress and then kind of use our meeting time more to focus on strategy, reporting insights, strategic recommendations, and any kind of feedback that we needed on content. So I just wanted to give you a heads up and make sure that that worked for you. But obviously we're still available. We can still meet as needed. For example, for things like the CVE pages, if we need to sync live on feedback, we're always still available for that as well. So any other questions or kind of feedback on any of this?

**Ankit Pahuja:** I think this looks fine. I think meetings as required would work better for us as well.

**Bailey Seybolt:** Yes, for sure. Okay, that sounds great. So we, for right now, we'll focus on those CVE pages and getting those up and running, and I will follow up on Slack with any progress or questions there.

**Ankit Pahuja:** All right, sounds good. All right, thank you all, and talk to you soon. Bye.

**Bailey Seybolt:** Bye, everyone. Bye.
