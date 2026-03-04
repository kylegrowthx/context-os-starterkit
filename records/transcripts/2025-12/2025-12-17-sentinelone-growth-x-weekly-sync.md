# SentinelOne <> Growth X - Weekly Sync

<metadata>
date: 2025-12-17
time: 13:29 UTC
duration: 16 minutes
organizer: team@growthxlabs.com
participants: Bailey Seybolt, Marcus Derencius, Ankit Pahuja, Mansi Bhalothia, Ankit Pahuja, Mansi Bhalothia
fathom_recording_id: 109363805
fathom_url: https://fathom.video/calls/508366846
share_url: https://fathom.video/share/c5ZspxjZjJRrYM7HUHh2Vzu5yv26teZP
source: fathom
enriched_on: 2026-03-02 00:00 UTC
</metadata>

---

## Summary

GrowthX and SentinelOne reviewed a new CVE article generation pipeline that auto-generates articles from GitHub while enforcing writing guidelines for consistent quality and depth. GrowthX staged 250 articles for SentinelOne's review before proceeding with a full 750-article batch, and the teams aligned that SentinelOne will decide between prioritizing new content or refreshing existing articles after the review. Planning also kicked off for Q4 reporting in January and a 2025 strategic planning session in late January or February, pending SentinelOne's internal goal-setting completion.

---

## Context

GrowthX is delivering a B2B content marketing engagement for SentinelOne, focusing on CVE (security vulnerability) article generation as a major content initiative. The new pipeline is designed to address quality inconsistencies in the first batch of 750 manually created articles by automating generation from GitHub data while enforcing stricter adherence to writing guidelines. This meeting brought together SentinelOne's content leadership (Ankit Pahuja, Mansi Bhalothia) with GrowthX's delivery team (Bailey Seybolt, Marcus Derencius) to review improvements and align on next steps.

---

## Relevance

**To GrowthX Delivery:**
- SentinelOne must review 250 staged articles and writing guidelines before proceeding with the full 750-article batch to ensure quality standards are met
- Two competing priorities have been identified: generating new content or refreshing existing 750 articles with the new format; SentinelOne will decide after review
- New pipeline improvements include higher technical depth, more actionable guidance, and improved readability from a refined writing model
- SentinelOne product capabilities will not be integrated into CVE articles unless contextually relevant; "Key Takeaway" sections with CTAs will remain ad hoc
- Product description documentation is in progress (Ashley from PM/Prompt Engineering) and will be shared by Mansi once received

**To GrowthX Business Development:**
- Q4 performance review and content year-in-review scheduled for first two weeks of January, indicating strong account health and visibility
- 2025 strategic planning session deferred to late January or February due to SentinelOne's January financial year-end; timing dependent on their internal goal-setting completion
- SentinelOne remains engaged and collaborative on expansion opportunities (new product content, strategic alignment)

---

## Overview

- **New CVE Pipeline Ready:** A new pipeline auto-generates CVE articles from GitHub, enforcing writing guidelines for higher quality and consistency.
- **Review Required:** SentinelOne must review the first 250 staged articles and the new writing guidelines before the full 750-article batch is generated.
- **Strategic Decision Needed:** After review, SentinelOne must decide whether to prioritize new content or refresh the existing 750 articles with the new format.
- **Q4 Reporting & 2025 Planning:** January will feature a Q4 performance review and a 2025 strategic planning session, contingent on SentinelOne's internal goal-setting.

---

## Key Topics

### New CVE Article Pipeline

  - **Problem:** Inconsistent quality in the first batch of 750 CVE articles, which did not fully follow writing guidelines.
  - **Solution:** A new pipeline auto-generates articles from GitHub, enforcing guidelines for consistent quality.
  - **Key Improvements:**
      - Higher technical depth and more actionable guidance.
      - Improved readability from a refined writing model.
      - A process diagram explaining the data flow (GitHub → article generation).
  - **Staged for Review:** The first 250 articles from the new pipeline are in Contentstack for SentinelOne's review.

### Review & Publication Plan

  - **SentinelOne's Review Process:**
    1.  Review the 250 staged articles and the new writing guidelines.
    2.  Provide feedback to GrowthX.
  - **Decision Point:** After review, SentinelOne must choose between two priorities:
      - **Option A:** Continue generating new content.
      - **Option B:** Refresh the existing 750 articles with the new format.
  - **Content Note:** Ankit requested that SentinelOne product capabilities not be integrated into CVE articles yet, unless contextually relevant.

### General Content Updates

  - **"Key Takeaway" Section:**
      - **Purpose:** A "good to have" section for articles directly related to SentinelOne products, used to include a CTA.
      - **Decision:** Will remain ad hoc, not a standard requirement.
  - **Airtable Status:** Mansi updated Airtable; GrowthX can now move published articles to the "Published" column.
  - **Product Description Doc:** Ashley (PM, Prompt Engineering) is creating the doc; Mansi will share it with GrowthX upon receipt.

### January Planning

  - **Q4 Performance Review:**
      - **Timing:** First two weeks of January.
      - **Scope:** Monthly reporting plus a "quarter-in-review" for all content efforts, including CVEs.
  - **2025 Strategic Planning:**
      - **Purpose:** Align GrowthX's work with SentinelOne's 2025 goals (e.g., new product launches, marketing strategy).
      - **Timing:** Late January or February.
      - **Contingency:** SentinelOne's financial year ends in January, so internal goal-setting may not be complete until then.

---

## Action Items

**Mansi Bhalothia**
- Review CVE writing guidelines; then review 250 staged CVEs in Contentstack and send feedback to Bailey/Marcus

**Bailey Seybolt**
- Share CVE materials (agenda, diagram, guidelines, staged CVEs) on Slack to Ankit/Mansi; confirm access
- Move articles marked 'to be published' in Airtable to Published
- Send async holiday content plan (in-progress/publish dates) to Ankit/Mansi
- Prepare Jan reporting deck incl. content year-in-review for Ankit/Mansi
- Schedule late-Jan check-in w/ Ankit/Mansi re: 2025 goals

---

## Transcript
**Bailey Seybolt:** This meeting is being recorded.

**Marcus Derencius:** Hello, how are you?

**Bailey Seybolt:** Good. I wasn't sure if you were coming today. Did you want to walk through the new pipeline to sort of talk them through how it works?

**Marcus Derencius:** Yeah, I can show you quickly because it's, actually, I need some feedback to analyze it because it gets the data, but I don't know the best way to, what to do. So it's simply getting the data, but nothing's happening because we have to define. So we have two pipelines, just to make sure we are talking about the one that gets new CVEs from GitHub.

**Bailey Seybolt:** Hi, Ankit.

**Ankit Pahuja:** Hey. How's it going?

**Bailey Seybolt:** Good. How are you doing?

**Ankit Pahuja:** I'm doing well. I'll just be off camera today.

**Bailey Seybolt:** Okay, no problem. Oh, I think she's here. Hi, Mansi.

**Mansi Bhalothia:** Hi, I'm sorry I'm a minute late.

**Bailey Seybolt:** Oh, no, no worries. Okay. I think it's just us, right? So maybe I'll just jump in and share the agenda. So I think the biggest thing is that now the code freeze is lifted. So we're back and able to publish the CVE pages again. And Marcus has been doing some work on our end to kind of revise what that article looks like and where it's pulling directly from GitHub. So I might let him just give a quick overview of the changes.

**Bailey Seybolt:** We included, I know you all wanted kind of a diagram to capture how the process will work. So we also included this and I can send the link to everything here after this meeting as well. So you can take a look, but we've uploaded the first 250 entries for you to review in kind of a slightly new format. So we figured it would be easier to start with a smaller batch in case there are kind of changes you want made or feedback you have. Those are staged.

**Bailey Seybolt:** Did you say something, Mansi?

**Mansi Bhalothia:** No.

**Bailey Seybolt:** So yeah, once you take a look at those, we have kind of more ready to go, but we thought it made sense for you to approve and kind of publish first to make sure everything is all good. Marcus, did you want to give like a quick overview of anything or if you had any questions for the SentinelOne team?

**Marcus Derencius:** Yeah. While I was building the diagram, how we generate the whole article, I made also some improvements on the model that we are using to write the final article. So there might be some improvements on the text, how it's read. So those are the changes we listed there. Just to get, like, when you read the article, should read better now. And then we can get, like, just a final feedback on the writing of the CVE article. Yeah, the diagram explains the whole flow, how we get the data from GitHub, how we write the article, how we use the code examples. If you have any questions, yeah, after reading the diagram or anything, yeah, if you have any other questions. Just, the update is mainly the writing.

**Bailey Seybolt:** Should look better.

**Bailey Seybolt:** Yeah. And I sort of tried to capture kind of the key changes here, but you'll notice it's just generally kind of a greater technical depth, sort of like offers more actionable guidance and actually what to do with this information. And I also included the writing guidelines that we're using to create these articles. So once you take a look at the kind of updated examples, you can let us know if there are other things you'd like to change, like other sections you would like edited and we can make updates there as well. So I'm happy to kind of touch base with you separately or async, or we can just do it on Slack. But once you've had a chance to review, we can kind of circle back and see kind of what you think. And then I think we have two choices where we can either like continue to prioritize the new content, but also if you want us to go back and refresh the existing articles that we've already published with sort of this new, richer format. So once you sort of let me know about that, I can update our review and our release plan documents, just so it offers a more accurate timeline, since I know we paused for a few weeks, and then we can decide how to approach that.

**Ankit Pahuja:** All right. All this is helpful. Thank you. And key changes. I think I'm a bit, I mean, I'll, of course, we'll check with the team on the entries that are added to content stack, but for the point integrated SentinelOne capabilities. So with vulnerability database, plan is largely to not include capabilities just as of yet. So let us go through the entries that are added, and if it's contextual, we can, of course, come back and tell you, give you feedback on how we'd want to go about it. If not, probably we'd, of course, in either case talk about it. Other things look great. I think it would only improve content depth and quality, which is great. I think the next step on us is to look at a few entries from the lot that you have added and give feedback if there's a need for feedback or just go publish. Is that right?

**Bailey Seybolt:** Yep, that's right. So, yeah, you can look at the ones under review.

**Marcus Derencius:** Yeah, one of the key reasons of this update is because the articles were not following the writing guidelines fully on the first patch. So with this new update, we can enforce the writing guidelines. So if you want to remove any section or any instruction, the article is going to be more consistent. So that's the main goal of this. So if you auto-cut, they'll be consistently good. So before, there would be a chance of randomly being off the writing guidelines.

**Ankit Pahuja:** Got it. So basically, this review and the writing guidelines for CVE database is something that we should refer to once. And basis this, the output is generated. Would that be right to assume?

**Marcus Derencius:** The new, the 250 new ones, they are following this writing guidelines we have now. If there's something we want to change that we can regenerate it again until it's good, then we can regenerate it for all the 750 entries that we have now.

**Ankit Pahuja:** All right. Got it. So I think Mansi, this is one to do that we could do is review the guidelines, look at the existing pages and the new 250 items that we have, and then probably get back to the team on whether we need to revise something. If not, we publish, and then we could probably plan a refresh as we'd need to for earlier entries.

**Mansi Bhalothia:** Okay, Ankit, got it.

**Bailey Seybolt:** Great. Yeah, so just reach out if you have any other questions or you want to talk through any of it.

**Ankit Pahuja:** All right. Yeah, can you just make sure that we have access to all the newer documents here?

**Bailey Seybolt:** Yes, yes. I'll make sure you've accessed everything, and I'll share this on Slack. I'll just put this agenda page, too, because I linked everything from here just so you would have it easy to access.

**Ankit Pahuja:** All right.

**Bailey Seybolt:** Sounds good. Okay. And then in terms of content, I know you left some feedback on previous content, so I think that should be delivered today. And then Thursday, we have the new articles that are coming as well. One thing that we noticed is that sort of in the table of contents, sometimes you're adding a key takeaway section and sometimes you're not. And I was wondering if this is something that you want to make a standard part of each article or if there's a reason you sort of are including it in some but not others.

**Mansi Bhalothia:** So for the articles that are directly related to S1 product, that is the area where we include the key takeaway section so that we can ideally put a CTA. But it's not a specific requirement for inclusion. It's like a good to have section sometimes.

**Bailey Seybolt:** Would you want us to add it as a standard or do you want to keep sort of adding it on sort of an ad hoc basis?

**Mansi Bhalothia:** Ad hoc basis. It's not, as I said, it's just a good to have section. So it's not something that must be included.

**Bailey Seybolt:** Okay.

**Mansi Bhalothia:** And then I have updated over the last two pointers for you. No new article has been published. I updated the Airtable. So for the marked as to be published, they are published. So you can just move them to the publish section. The rest of them are still in PMM review. The document for product description. So from the product engineering team, the product manager from Prompt Engineering, Ashley is working on the product description doc. She hasn't specified a date where she can send, but I think she will probably share it soon and then I can share it with you.

**Bailey Seybolt:** Okay, great. Thank you. That is great to know. Well, thank you for those updates. The last thing on mine was more sort of planning for January, but did your team have anything else they wanted to talk about when it comes to content or the CVE project?

**Ankit Pahuja:** I'm good.

**Bailey Seybolt:** Okay. And then just in terms of, I know we'll have a little bit of more async time over the holidays to touch base. So I just want to let you know, my plan is by this week on Friday, I'll send an async document just to let you know what's being worked on and what's being published when, so that your team has access to it. Because I know people tend to take time off at this time of year just to make sure there's somewhere where you can go and check and know what's happening, even if we're not meeting. And then looking forward to January, two things that'll come is usually we sort of do our monthly reporting sometime in the first two weeks of the month. So we'll sort of use one of these sessions to kind of do a deeper dive into reporting and look at performance and how things are going in general, just as like a check-in. Was there any kind of particular metrics or questions that your team had or focus areas to be aware of as we kind of prepare to do that once we're back in January?

**Ankit Pahuja:** I think this looks good. We could also include a project-in-review or a quarter-in-review kind of thing, like a general lead by year-in-review for, you could specifically do for content because all our efforts have been around that, inclusive of CVE. So I think that could be a good thing to look at.

**Bailey Seybolt:** Okay, that sounds good. And then the other thing is that we're trying to touch base with clients and set aside some time to kind of talk about your goals for 2025. So if you have any, that can be anything from new products launching, like new focus areas for your marketing strategy, just to make sure, you know, we're staying up to date with your company goals as well. So I just wanted to kind of put that on your radar as something that it would be great to kind of update us on. And so we can use that, we can like schedule a special time for that, or we can kind of use one of these sync meetings, and I can just come with some questions about that as well.

**Ankit Pahuja:** Absolutely. So I think anytime third week or later could be good in January for this, because I think to update you all, we need to be updated about what's really going on, or what's the plan. So just allow some time there. Essentially our year ends January, like the financial year. So I'm expecting these conversations to happen late January or February, but accordingly we could have this session.

**Bailey Seybolt:** Okay, that sounds good. I'll put a note on my calendars to check in at the end of January, and then we can figure out what works best for your team. Sounds good. Okay, that was it for my end.

**Ankit Pahuja:** Is there anything else from your end? Nothing else.

**Bailey Seybolt:** I'm good. All right. Then thank you, everybody. And I will be in touch.

**Ankit Pahuja:** Talk to you soon. Thank you.

**Mansi Bhalothia:** Bye. Thank you.
