# SentinelOne Weekly Sync

<metadata>
date: 2025-09-10
time: 15:31 UTC
duration: 23 minutes
organizer: Marisol Smith
participants: Drew Hoffman, Mahati Rapol, Sydney Go, Ankit Pahuja, Mansi Bhalothia, Georgemaine Lourens, Marisol Smith
fathom_recording_id: 86296631
fathom_url: https://fathom.video/calls/405263794
share_url: https://fathom.video/share/xurR5ByxXWFAXiM7F_hWenYgqrxyb3_S
source: fathom
enriched_on: 2026-03-03 09:45 UTC
</metadata>

---

## Summary

GrowthX and SentinelOne discussed progress on three concurrent projects: CVE page design near finalization with all feedback implemented; CS101 content generation moving from calibration to ongoing production with 3 articles targeted for this week; and a vulnerability database project estimated at 2 weeks post-Content Stack access. Key decisions: adopting a filters approach for CVE page navigation instead of category pages, explicitly labeling CVSS scores on the directory, and requesting detailed feedback comments (not just suggested edits) to train the AI content generator for future articles.

---

## Context

GrowthX is delivering a content and design project for SentinelOne, a cybersecurity company. This weekly sync aligns the teams on three workstreams: CVE (Common Vulnerabilities and Exposures) page design and content publishing infrastructure; CS101 educational content generation using AI-powered tools; and a vulnerability database project that aggregates and displays security data. Sydney Go leads from the GrowthX side with support from Georgemaine (design) and Marisol (content strategy). Mahati and Ankit represent SentinelOne's product and security teams. The meeting reflects the transition from initial design/build phases into execution and optimization.

---

## Relevance

**To GrowthX Delivery:**
- CVE pages use a filters-based UX rather than category pages — this decision balances SEO benefit against user experience, worth capturing for future similar projects
- AI content generation system requires detailed feedback comments (not suggested edits) to train effectively; this is a workflow improvement for AI-generated content projects
- Looker dashboard tracking for client visibility on content performance — expanding monitoring and reporting capabilities

**To GrowthX Business Development:**
- SentinelOne CS101 content cadence accelerating from 3 to potentially 5 articles/week, signaling positive account health and expanded scope
- Vulnerability database project timeline depends on Content Stack access (currently blocked), creating a critical dependency worth tracking for account risk
- Client is actively involved in design decisions (fonts, CTAs, UI patterns) — strong engagement signal

**To CheckThat:**
- AI visibility and AEO: CS101 is educational content targeting technical audience; monitoring how these articles perform in search will show AI content effectiveness in B2B security
- Prompt injection attacks and "Prompt Hacking 101" content being developed with caution due to recent Prompt acquisition — relevant to competitive positioning and CheckThat's own security-focused content strategy

---

## Overview

- CVE page design is near finalization; feedback implemented, awaiting final review
- CS101 content generation is progressing well; 3 articles to be delivered this week
- Vulnerability database project timeline: \~2 weeks post-Content Stack access and design finalization
- Need to ensure proper code review and developer involvement in next meeting

---

## Key Topics

### CVE Page Design Progress

  - All previous feedback implemented in Figma
  - Awaiting licensed font files and color palette from SentinelOne
  - Drew to provide final feedback after team review
  - Agreed to use filters approach instead of category pages for better UX
  - CVSS score to be explicitly labeled on directory page
  - CTA to be provided by Ankit

### CS101 Content Generation

  - 2 articles in review process: 1 with PMM for final check, 1 with minor changes
  - Plan to deliver 3 articles this week, potentially increasing to 5 next week
  - AI training ongoing based on feedback; detailed comments requested for improvement
  - Caution noted regarding "Prompt Hacking 101" due to recent acquisition

### Vulnerability Database Project

  - Estimated 2-week development time once Content Stack access is granted
  - Mahati requested developer presence in next meeting for technical discussion
  - Proper code review process to be implemented

### Administrative Updates

  - Sydney awaiting Content Stack access; Mahati to follow up
  - Looker dashboard set up but currently empty; to be populated next week
  - Sydney completing required security trainings

---

## Action Items

**Mahati Rapol (SentinelOne)**
- Send licensed font files and color palette to shared Google Drive
- Follow up on Content Stack access for Sydney Go and Nicholas

**Drew Hoffman (SentinelOne)**
- Provide final feedback on CVE page design in Figma

**Ankit Pahuja (SentinelOne)**
- Send specific CTA copy for CVE pages

**Sydney Go (GrowthX)**
- Send shared Google Drive link for font files to team
- Finalize CVE page design after receiving Drew's feedback
- Add "excerpt" column (150-170 chars) to content tracking sheet
- Deliver 3 CS101 articles this week
- Set up Looker dashboard for next week's meeting

---

## Transcript
**Ankit Pahuja:** Yeah, all well.

**Ankit Pahuja:** How's it for you?

**Ankit Pahuja:** Doing good.

**Sydney Go:** Aida's out, so you have me again.

**Ankit Pahuja:** Hello.

**Ankit Pahuja:** I'm not sure if other folks are joining in.

**Sydney Go:** Okay.

**Ankit Pahuja:** I saw your comment around the Figma files.

**Ankit Pahuja:** I didn't get a chance to look at it, though.

**Ankit Pahuja:** Mm We could quickly walk through, maybe in this call.

**Sydney Go:** Yep.

**Sydney Go:** I can definitely do that.

**Sydney Go:** I do have that pulled up.

**Sydney Go:** I'm going to send you the agenda.

**Sydney Go:** My laptop's being really slow, so if I lag, do please let me know.

**Sydney Go:** And I'm apologizing in advance.

**Sydney Go:** I don't know why it's doing this.

**Sydney Go:** It's been doing it for the past few days, and it's been a struggle.

**Sydney Go:** Yeah.

**Sydney Go:** Do you need any help?

**Sydney Go:** Do you also have...

**Sydney Go:** So I actually just closed them, and I've kind of upgraded from 500 tabs to 500 windows, so that may be the issue.

**Sydney Go:** Okay, all right, I think we're all here and we can get started.

**Sydney Go:** Okay, so I'll share my screen for little bit.

**Sydney Go:** So both Georgemaine and Marisol are here because they're also working on your account.

**Sydney Go:** So just so that you can get more specific answers if you have any questions for us.

**Sydney Go:** Give me five seconds.

**Sydney Go:** I am attempting to share my screen.

**Sydney Go:** Free from my processing unit.

**Sydney Go:** Is it working?

**Sydney Go:** Yep.

**Sydney Go:** Okay, awesome.

**Sydney Go:** Okay, so what I've done to kind of make it a little bit easier for us to understand what's happening on your account is I've created work streams on top of every meeting note page that we have, basically, so that we know what's ongoing.

**Sydney Go:** Let me know if I missed something, but currently we have content creation for CS101, and this is currently calibrating.

**Sydney Go:** I'm hoping by next week I can shift this over to ongoing, which means it'll just be like an engine, and we'll just send you pieces, and we can do for review.

**Sydney Go:** The content generator is technically already built, but we do have to hook this up to content stack.

**Sydney Go:** We currently don't have access to content stack yet.

**Sydney Go:** I've been checking every day, but I know that Nicholas has already seen the email, so he's going to get access as soon as possible as well.

**Sydney Go:** And then on the front-end design, we're building it, but it's already in the finalization stage, so I know that you, Ankit, and Georgemaine, Marisol, and Ada were all working on this.

**Sydney Go:** So it is building, and currently what we're trying to do is finalize that front-end and make sure that we have all the information we need on the back-end, you know, coordinating with all that as well.

**Sydney Go:** And then on the generation front, the pipeline does work.

**Sydney Go:** It's just we need to hook it up to the front-end to make sure it auto-pub.

**Sydney Go:** publishes, and that all the data is being pulled in correctly.

**Sydney Go:** So the current priorities for now are to figure out how to hook up out the backend that we've created with the frontend we created on content stack and make that, you know, all kind of work together.

**Sydney Go:** Yeah.

**Sydney Go:** Okay.

**Sydney Go:** That was just a quick overview. I'll update this every week so that we have a clear understanding of what's going on. And if you have any questions, let me or Aida know, and we can field those.

**Sydney Go:** So for the CVE pages—you've already seen the Figma file. All the feedback has been implemented, and Georgemaine did have some asks for us. We need the licensed font files from you and the color palette. Before that, do you have any questions on the Figma file?

**Mahati Rapol:** All the feedback has been incorporated, and we have a final design. I wanted to get Drew's final take on it before we start working on development.

**Drew Hoffman:** I have some feedback, but I haven't implemented it. I need to make sure it has a proper review for the rest of the team.

**Sydney Go:** So these are the pages we currently have. All the feedback that you left, Georgemaine has already implemented. We need the font for this, but we'll do that as well. How would you like that delivered?

**Drew Hoffman:** Do you have a shared Google Drive?

**Sydney Go:** We do have a shared Google Drive. I could create a doc for you to deliver feedback, or you can just leave feedback on Figma—whatever is easiest.

**Drew Hoffman:** I meant, how would you like the font delivered?

**Sydney Go:** Just sending it via shared Google Drive is fine.

**Sydney Go:** Mahati, can you send that my way?

**Drew Hoffman:** I'll add the link to our shared channel.

**Sydney Go:** We've addressed all the feedback. We also added a "generated by AI" tab like you requested. We removed some sections based on Phil's feedback and removed the Sentinel Labs logo. Georgemaine is on the call, so if you have any specific questions or urgent feedback, we can address that. The one question is: are these all the sources and information we want per row, or do we want to add more metadata?

**Sydney Go:** Score, technology, component, aim, exploit, fix, and date found. That's what we found on the Wiz page and competitors—it seems to be working for them on the SEO front. If there's anything specific you want us to add to these columns on the index page, we could do that.

**Sydney Go:** The other question we had: are we okay with the search bar? The Content Stack team said we could hook it up to Algolia, but we could also do a simpler filter by feature or tag approach.

**Ankit Pahuja:** No issue for me.

**Sydney Go:** So the third column here says "score" on the directory page.

**Ankit Pahuja:** Is this the CVSS score?

**Sydney Go:** Yes. We might just want to call it "CVSS score."

**Georgemaine Lourens:** In the Figma file, you left a comment about the filters—a sidebar experience similar to a competitor. We originally started on the index page with tabs and categories at the top. What's the ideal pattern we're going for? Would you rather have the Wiz experience with filters and categories at the top, or the list on the left with all the filters?

**Ankit Pahuja:** Speaking to security folks, the general expectation is they want to filter on technologies. A dropdown view that filters on technologies is ideal, and other filters are helpful. Where would these open up? Would we have a category page for each, or would the body below filter down on clicking filters?

**Georgemaine Lourens:** That's a great question. When I first modeled this, I based it after Wiz. They have a subcategory route that opens the same page but fills the search field with the category. There might be SEO benefit to having more index pages, but it comes at a user experience cost since you constantly navigate back and forth. It's a matter of what we're prioritizing.

**Ankit Pahuja:** I think a filters approach would suit better.

**Sydney Go:** Ankit, do you have a specific CTA in mind that you can send over?

**Ankit Pahuja:** I'll send it over.

**Sydney Go:** On the CVE pages, is there anything else you want to discuss?

**Ankit Pahuja:** I'm good.

**Mahati Rapol:** On the content end, I wanted to make sure Mansi is aligned on the content generation project.

**Drew Hoffman:** Do we have example articles we can send to Phil, or have we done that already?

**Mahati Rapol:** We showed them and shared with him. Phil came into the Figma and added comments. Once those are incorporated, we want to make sure we all review the final Figma.

**Sydney Go:** There are currently five articles in here for review. Basically, once we hook everything up to the front-end and back-end, it'll all look like this. We'll update the sidebar as needed. This is the initial mock-up, but most data should stay the same. We've confirmed on the back-end that we're pulling the correct data.

**Sydney Go:** The next thing I think you wanted to talk about is CS101 content. Is that correct?

**Mahati Rapol:** That's right. I wanted to make sure Mansi is in the loop and can review and work with you together.

**Marisol Smith:** With these two articles, I reviewed them. One was approved and is with the PMM for final check. The other, I made a few changes to, and I'll pass it over for final review so we can publish.

**Sydney Go:** Do you want me to tag Ankit for SEO reviewer and Mansi for content reviewer?

**Marisol Smith:** I can fill those up. We're missing the "excerpt" section. Apart from meta description, there's supposed to be another column that gives an excerpt of the whole article.

**Sydney Go:** So you want an excerpt?

**Marisol Smith:** That's correct. That's the same as meta description: 150 to 170 characters. It will show on your blog as the title with a little snippet below.

**Sydney Go:** I've been treating the introduction as similar to that. If you want, I can copy it over. Does this have any character limits?

**Sydney Go:** And then on the blog, sometimes we go straight into the H2 with no introduction. That's fine, right?

**Marisol Smith:** We directly answer the main H1 header. That's the strategy we're following.

**Sydney Go:** That makes total sense. We did the exact same thing at SoundRush Network with really good results.

**Sydney Go:** This week on the CS101 front, we plan to deliver three articles. But if you're happy with the way the CS101 content is looking, I'll switch this over to ongoing, and next week we can start delivering five. Does that sound good?

**Mahati Rapol:** All right. As we make changes and updates based on feedback, can we train the AI content tool to follow the same layout, structure, and style going forward?

**Sydney Go:** Every time you leave feedback, I add it back into our backend. My ask for you, especially for these calibration articles: leave as many comments as you can. Even if you don't like a specific word, leave a comment so I can feed it back to the AI generator. Comments are much better than suggested edits because suggested edits don't show up when we export to HTML. Fewer reviews down the line, and you get the messaging right from the start.

**Drew Hoffman:** I have a callout on "Prompt Hacking 101." We just went through an acquisition of a company called Prompt, so we need to make sure it doesn't impact any of that. There should be some monitoring there.

**Sydney Go:** I'll make a note of that. One of the things we wanted to work on this week related to prompt hacking was prompt injection attacks. Are we still okay to move forward with that?

**Drew Hoffman:** Yeah, I just want extra eyes on anything "prompt"-related.

**Sydney Go:** Moving forward, has Aida shown you what your Looker dashboard will look like yet?

**Sydney Go:** That will be a project for next week because we don't have uploaded articles yet. The Looker dashboard is set up, but it's completely empty. We'll populate it this week so by next week we can start tracking everything.

**Sydney Go:** I've been monitoring my email every day for Content Stack access, and I don't have it yet. So I can't stage the articles. Ankit, has anyone staged the first article we sent over?

**Ankit Pahuja:** It's under PMM review. Once we get approval, we stage it.

**Sydney Go:** Hopefully I'll get access before that so I can stage it and save you time.

**Mahati Rapol:** Sydney, do you have Okta access to SentinelOne?

**Sydney Go:** I do have Okta access. I've already done the security training.

**Sydney Go:** I'm about to do the security trainings. I know they're required.

**Mahati Rapol:** I'll work with John on CMS access for you. You should have it based on my previous actions.

**Sydney Go:** I saw on a thread that on Wednesday, September 3rd, John messaged that he'd get us CMS access as soon as Nicholas's Okta account is set up.

**Mahati Rapol:** I'll follow up on that and tag you in the thread so we can continue the conversation.

**Sydney Go:** So the next steps for us are to deliver three CS101 articles, finalize the CVE page design, and send over the shared drive link.

**Sydney Go:** Am I missing anything?

**Sydney Go:** I think this is all we chatted about.

**Ankit Pahuja:** Just a quick one. For the vulnerability database project, could you talk through and think about a go-live date we could put together?

**Sydney Go:** If everything goes smoothly, the engineering team should need about two weeks to hook it all up. But that's after the page is finalized and we get Content Stack access. Really, it depends on when Nicholas can get access. As soon as we have a timeline, I'll get you an estimate.

**Mahati Rapol:** I don't know who on the team is the developer working on this, but once we start development on the vulnerability database, I'd like to talk to them on the next meeting.

**Sydney Go:** He's actually out sick today. But John, Jory, Ankit, and Aida had a call with Nicholas recently on how to hook everything up.

**Ankit Pahuja:** It was an alignment call between the two web teams so they could get started.

**Mahati Rapol:** On the next call, I definitely want to be on it to make sure of the code questions. Is there going to be proper code review?

**Drew Hoffman:** Yes.

**Sydney Go:** If that's all, I can give you back seven minutes of your time.

**Mahati Rapol:** Thank you, team. I'll keep everyone updated on everything going on and send everything over within the next few minutes.

**Mahati Rapol:** Thank you so much. Bye-bye.

**Sydney Go:** Bye.
