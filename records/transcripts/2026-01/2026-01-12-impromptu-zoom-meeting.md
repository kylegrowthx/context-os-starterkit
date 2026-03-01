# Impromptu Zoom Meeting

<metadata>
date: 2026-01-12
time: 21:31 UTC
duration: 16 minutes
organizer: matthew@growthx.ai
participants: Matthew Panzarino (GrowthX), Najam Ahmed (GrowthX)
fathom_recording_id: 113649991
fathom_url: https://fathom.video/calls/530361692
share_url: https://fathom.video/share/Q6FexChZQfTDP-pw2oxRy6MyCqm-1nnY
source: fathom
enriched_on: 2026-02-28, 14:29 UTC
</metadata>

---

## Summary

Matthew and Najam address a spike in pipeline executions (157 that day) caused by Airtable database cleanup, not new publishing. Matthew emphasizes that the Airtable must be updated with all published articles, dates, and live links as the single source of truth for client accountability. The team agrees on a policy: use automated publishing workflows exclusively, and file engineering tickets for all pipeline failures and systemic issues like broken links rather than applying manual workarounds.

---

## Context

This meeting follows workflow challenges on a client integration guides project. Najam has been managing end-to-end operations on content generation and enrichment, coordinating with the client (represented by Liz) on publishing and content scaling. The influx of pipeline executions raised questions about publishing velocity and data accuracy, prompting Matthew to clarify expectations around documentation, automation, and engineering escalation protocols.

The team is managing multiple workstreams: publishing integration guides (scaling to 5 articles/week), enriching existing pages with new content, and maintaining a use case guides repository. Data integrity issues in the Airtable (articles marked "published" with no live content, scattered documentation across sheets) were driving the cleanup work.

---

## Relevance

- **Publishing workflow standards**: Establishes that all pipeline work must be automated and logged in Airtable, with clear escalation paths for failures.
- **Client accountability**: The Airtable is the single source of truth for Matthew, Najam, and the client (Liz) to track published articles, dates, and live links.
- **Engineering escalation**: Broken links in generated articles (Webflow API endpoints) are a systemic pipeline issue requiring engineering investigation, not manual fixes.
- **Capacity management**: Documents recurring manual overhead (broken link fixes) that should be systematized or engineered away.
- **Data cleanup**: Explains the 157 pipeline executions as a one-time Airtable cleanup, not new publishing activity.

---

## Overview

- A surge in pipeline executions (157 today) is due to a cleanup of the Airtable database, not new publishing.
- The Airtable is the single source of truth for client accountability; it must be updated with all published articles, dates, and live links.
- Automated publishing is mandatory for scalability and visibility; manual workarounds are prohibited. File engineering tickets for all pipeline failures.
- A systemic issue with broken links in generated articles is a pipeline bug requiring an engineering fix, not a manual workaround.

---

## Key Topics

### Airtable Cleanup & Pipeline Surge

- **Problem:** A surge in pipeline executions (157 today) created confusion and a false impression of new publishing.
- **Cause:** A cleanup of the Airtable database to fix data integrity issues.
  - **Issue 1:** Articles marked "published" had live URLs but no content (e.g., `101Domain.com`).
  - **Issue 2:** No centralized folder for article documents; files were scattered across multiple sheets.
- **Solution:** Centralize all article documents in Google Docs, replacing the old sheet-based workflow.
- **Deadline:** Complete by end of day so Liz has visibility for her Wednesday meeting with Jason and can present accurate numbers to the client.

### Workflow Standardization & Accountability

- **Requirement:** The Airtable must be updated with all published articles, dates, and live links.
  - **Rationale:** This is the single source of truth for internal visibility and client accountability.
  - **Scope:** ~210 integration guides need to be logged in the Airtable for Liz's oversight.
- **Policy:** Use automated publishing workflows exclusively.
  - **Rationale:** Ensures scalability and provides clear visibility in Atlas for tracking completed work.
  - **Escalation:** File an engineering ticket or post in `#epd-help` for all pipeline failures; do not apply manual workarounds.
- **Visibility:** Webflow logs provide external verification of published articles; the Airtable must align with what Webflow reports.

### Systemic Issue: Broken Links

- **Problem:** Generated articles frequently contain broken links (e.g., to Webflow API endpoints like `/feature/cms`, list endpoints, create endpoints).
- **Impact:** This requires manual checks and fixes on every article, creating a capacity bottleneck and slowing delivery.
- **Current workaround:** Najam manually identifies and fixes broken links (e.g., missing or malformed URLs to Webflow documentation).
- **Action:** File an engineering ticket with specific examples of broken links and affected runs.
  - **Rationale:** This is a pipeline bug requiring a systemic fix, not a manual workaround. If it happens across multiple pipelines or runs, it's a product issue, not a one-off instruction problem.
  - **Owner:** Matthew will escalate to engineering (Ange) with examples from Najam.

### Content Enrichment & Use Case Guides

- **Use Case Guides:** Scaling to 5 articles/week this week.
  - **Status:** Some articles are unlisted because they lack meta-images, which the client is responsible for providing.
  - **Client awareness:** The client (Liz) is aware of this and is okay with scaling while images are pending.
  - **Workstream:** Najam has coordinated feedback from the client's content person (Raymond) with Quirkland (engineering) to improve the publishing pipeline for these guides.
- **Content Enrichment:** A separate workstream for adding content to existing client pages that have placeholders or partial content.
  - **Coordination:** Najam meets weekly with Liz on Wednesdays; updates are logged in Notion.

---

## Action Items

**Najam Ahmed (GrowthX)**
- Update Airtable with publish dates and live links for all published articles; include approximately 210 integration guides so Liz has a complete view for her meeting with Jason.
- Document broken links and specific run examples; file an EPD engineering ticket (cc Matthew Panzarino) with details on which Webflow API endpoint links are breaking and in which article runs.

**Matthew Panzarino (GrowthX)**
- Monitor engineering ticket for broken links issue and coordinate with Ange to investigate systemic link issues across pipelines.

---

## Transcript

**Matthew Panzarino:** Like, there's been hundreds of articles run through today.

**Matthew Panzarino:** Why is that?

**Najam Ahmed:** Yeah, so two reasons.

**Najam Ahmed:** A whole bunch of articles that don't have a lot of code do get through the publisher very quickly.

**Najam Ahmed:** Most of the articles that you'll see don't have a lot of code.

**Najam Ahmed:** So once they're edited, I can run them directly.

**Najam Ahmed:** That's the reason why.

**Najam Ahmed:** Reason number two, you may see a bunch of articles that were generated in the pipeline as well.

**Najam Ahmed:** Those are for this week's articles.

**Matthew Panzarino:** Okay, because the pipeline executions here, I mean, there's like, what I don't understand is like, why there is suddenly 157 executions of the pipeline today.

**Najam Ahmed:** Not sure what you mean.

**Matthew Panzarino:** You're like, you've generated, you've run through like 157 generations in that pipeline today.

**Najam Ahmed:** Yeah, so...

**Najam Ahmed:** so...

**Najam Ahmed:** Thank

**Najam Ahmed:** When I started editing the Airtable, one of the things, and I mentioned this to Liz as well is, you mind if I quickly share my screen with you?

**Matthew Panzarino:** Sure.

**Najam Ahmed:** Okay.

**Najam Ahmed:** Right.

**Najam Ahmed:** So this is their Airtable, this is how it was set up.

**Najam Ahmed:** One of the things that I noticed when I started fixing this thing is some of the articles, for instance, take a look at this one, 101Domain.com.

**Najam Ahmed:** This was published, and it has a live page as well.

**Najam Ahmed:** So if you click on this live page, sorry, let me just open up the whole screen.

**Najam Ahmed:** Yeah.

**Najam Ahmed:** So if you click on the live page, this is how it appears.

**Najam Ahmed:** So on the face of it, the client would see that it's live, but in reality, it has no content.

**Najam Ahmed:** So that was also one of the reasons that I've been trying to fix.

**Najam Ahmed:** So I love this, adding content.

**Najam Ahmed:** So in there, making sure it's edited.

**Najam Ahmed:** Reason number two is there wasn't a centralized folder where all of the documents for these articles were being stored.

**Najam Ahmed:** All of the stuff moves from two sheets.

**Najam Ahmed:** So I'm essentially, what I've been trying to do is do away with the sheets altogether and just make sure that all of this works through Google Docs.

**Najam Ahmed:** So that's really it.

**Najam Ahmed:** Number two, which is use case guides.

**Najam Ahmed:** That also lives in here, except it's very basic.

**Najam Ahmed:** So part of that is also just me trying to expand on that, making sure this Airtable is on par with this one, has a V2 Enriched column.

**Najam Ahmed:** And then earlier in the day, what I was working on was, so we have another work, not really a work stream, another layer to what we're doing with them is enriching existing content.

**Najam Ahmed:** So not just the content.

**Najam Ahmed:** Content that has been generated, we're enriching them with, for them, so that's also what I've been doing for them today.

**Najam Ahmed:** They meet every Wednesday, so every, by every Tuesday, I have to give an update and fill out the Notion doc with all the stuff that's been done.

**Najam Ahmed:** So part of the reason why you're seeing such a flurry of activity today is just because I'm trying to make sure that this air table is done today before I log off.

**Najam Ahmed:** So by the time Liz goes in her meeting with Jason tomorrow, she has a pretty clear view, and then she can present it to them.

**Matthew Panzarino:** Okay, because it's like, you know, Liz sends a message, hey, where are these articles, and then basically it's like 300 things get triggered.

**Matthew Panzarino:** So it's like, to us, it's like, wait a minute, does this mean that nothing's been published?

**Matthew Panzarino:** So like, when, because if, frankly, if we go in there to Webflow, Webflow has the ability to look at their logs too.

**Matthew Panzarino:** So if we're publishing hundreds of articles that we didn't publish, they'll know.

**Matthew Panzarino:** And not only that, but...

**Matthew Panzarino:** So each week, you have published the articles each week, right?

**Najam Ahmed:** Like, if we look at the logs, we'll see those articles published, and you did it.

**Najam Ahmed:** I would say December 15th, 14th, somewhere around there.

**Najam Ahmed:** I can take a look and get you, like, a full list.

**Najam Ahmed:** That's exactly what I've been working on, whatever Andy said.

**Najam Ahmed:** So you have the live links, you have everything, you can check where all the stuff is.

**Najam Ahmed:** The count was a very novel way work was being done, in general, because Sydney has her very refined way of doing things through Excel.

**Najam Ahmed:** And it was a whole bunch of work right away, so I didn't really tweak her way of doing it.

**Najam Ahmed:** I'm pretty sure you already know how she does it, right?

**Matthew Panzarino:** With the app script and everything.

**Najam Ahmed:** So what I've done is, within that sheet only, so by day and today,

**Najam Ahmed:** Okay, we'll move away from the sheet.

**Najam Ahmed:** Essentially, what I've done is I've set up an app script.

**Najam Ahmed:** So whenever a new article is generated and combined, so the how to integrate section is separate, and the what you can build section is generated separately, and then put together.

**Najam Ahmed:** What will do is are being made.

**Matthew Panzarino:** To what?

**Najam Ahmed:** Edits to what?

**Najam Ahmed:** To the articles as well.

**Najam Ahmed:** So essentially, by the end, you will have, you can track changes for each of the articles if you so choose.

**Najam Ahmed:** Right now, for instance, all the edits are made in a Google Sheets cell, right?

**Najam Ahmed:** So, I just want to make sure that there are docs for anything.

**Najam Ahmed:** Liz and I had a pretty detailed discussion around this.

**Najam Ahmed:** She showed me data annotation, how they do it.

**Najam Ahmed:** She showed me Ishmael's workflow.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** All right.

**Matthew Panzarino:** So, yeah, I think having every

**Matthew Panzarino:** I mean, we obviously need the pieces, the live links to all the pieces in the Airtable that weren't there.

**Matthew Panzarino:** I think we also need the publish dates for those.

**Matthew Panzarino:** And that's pretty standard, obviously, in all the Airtables.

**Matthew Panzarino:** So we need those in there.

**Matthew Panzarino:** And then, yeah, I mean, it looks like, so you run the publishing workflow today 30 times.

**Matthew Panzarino:** Was that for this week's articles?

**Matthew Panzarino:** Yes.

**Matthew Panzarino:** Okay.

**Najam Ahmed:** And it works.

**Najam Ahmed:** wait, wait.

**Najam Ahmed:** There are also a bunch, like I showed you, a bunch of articles that are from before, which do appear published, but aren't actually published in, like I just showed you, right?

**Najam Ahmed:** So there are also those as well.

**Najam Ahmed:** So there's a whole bunch of content from before that hasn't, it says it's published, but nothing really appears on the sheet.

**Najam Ahmed:** So...

**Najam Ahmed:** So...

**Najam Ahmed:** So...

**Najam Ahmed:** Here's like this one, they are pages, we're just populating them with content, like all of these, GoDaddy, Domain Control, I think we did that a couple weeks ago, I believe.

**Najam Ahmed:** Yeah, so they are still pages, a whole bunch of them, but some might have content, some might not.

**Matthew Panzarino:** That's just something that you need to know.

**Matthew Panzarino:** Yeah, we are enriching the pages, right?

**Matthew Panzarino:** That's it, like for instance, this one, the integration exists, it just doesn't have any content on it, so we are putting the content on here, that's great.

**Matthew Panzarino:** And that's the, by we are, what do you mean, like that's our work stream?

**Matthew Panzarino:** That's what we do, yeah, for integration pages.

**Najam Ahmed:** Yeah, so it's an existing page and we're adding the content to the Some of them are existing pages and some of them are not, some of them are just original ideas, like base and entity.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Well, I think that it's important, obviously, that the air table gets updated.

**Matthew Panzarino:** That's how we maintain accountability across ourselves and a client.

**Matthew Panzarino:** So ensure that that's done.

**Matthew Panzarino:** If the publishing workflows are not functioning correctly, fix that.

**Matthew Panzarino:** Don't publish them manually, right?

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Because A, that's how you achieve scalability.

**Matthew Panzarino:** And then B, it's how we can tell whether things have been done or not, you know, in Atlas.

**Matthew Panzarino:** So if the publishing workflow is breaking or not functional in some way, then file a ticket for it, right?

**Matthew Panzarino:** Or raise your hand in EPD help, and we'll get an engineer to take a look at it so that you can run your publishing through there.

**Matthew Panzarino:** Because basically, if I look at it, it looks like something was published by Sydney in December, and then nothing was published until today.

**Najam Ahmed:** Right?

**Matthew Panzarino:** That's my view of it when I look at it.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** If that's not true, then the air table will be our next source of truth, and that's blank.

**Matthew Panzarino:** So you see where we're at here.

**Matthew Panzarino:** Like, it's...

**Matthew Panzarino:** No visibility.

**Matthew Panzarino:** Neither does Liz.

**Matthew Panzarino:** She gets on a call.

**Matthew Panzarino:** She doesn't have the ability to do that.

**Matthew Panzarino:** So please keep that updated.

**Najam Ahmed:** That's the expectation, right?

**Matthew Panzarino:** We've got to have that updated.

**Matthew Panzarino:** Otherwise, we have no visibility.

**Najam Ahmed:** 100%.

**Najam Ahmed:** Yeah.

**Najam Ahmed:** So remember in our last meeting, the weekly meeting that we do, one of the things you mentioned was around scalability.

**Najam Ahmed:** So when we started this new work stream, which essentially I've been owning end-to-end, I had a pretty detailed ticket file with Quirkland.

**Najam Ahmed:** We sorted everything out.

**Najam Ahmed:** So previously, a lot of the work was being done manually.

**Najam Ahmed:** don't know if you have any eyes on that.

**Najam Ahmed:** can show you if you want.

**Najam Ahmed:** But they have a person on their end, Raymond, who was editing every article very manually.

**Najam Ahmed:** So what we did is we took his feedback, put it into specific buckets, and then presented it to Quirkland, who tweaked the pipeline.

**Najam Ahmed:** And now I think we're in a very good place.

**Najam Ahmed:** So this week, we're also ramping that up.

**Najam Ahmed:** So there's going to be five articles published for the use case guides.

**Najam Ahmed:** That is in Airtable.

**Najam Ahmed:** You can take...

**Najam Ahmed:** It should be also updated today.

**Najam Ahmed:** They asked us to unlist some of the articles because they manage.

**Najam Ahmed:** Actually, that's also important because I'll just quickly show you just because I'm pretty sure it might eventually pop up on your radar now and then.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** So you're going to have like roughly 210 articles represented in Airtable today, right?

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** That have been published?

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** For the integration guides specifically, not just to the work stream.

**Najam Ahmed:** Yes.

**Najam Ahmed:** So some of them are also there.

**Najam Ahmed:** So if you take a look here, these are articles that we did.

**Najam Ahmed:** This is the next work stream, the other work stream that we deal with now.

**Najam Ahmed:** They're responsible for the meta issues, but these all have been unlisted, right?

**Najam Ahmed:** So you will have to search for them to find them.

**Najam Ahmed:** These are the ones that we tweak the feedback and everything with them.

**Matthew Panzarino:** Okay.

**Najam Ahmed:** Yeah, just showing that to you, just so you know that these were unlisted, they know about it.

**Matthew Panzarino:** We have published them.

**Najam Ahmed:** And they're okay to scale up to five, but yeah, that's really good.

**Najam Ahmed:** Because they don't have meta-images as yet, you can see it appears a bit awkward on there.

**Matthew Panzarino:** But we're not generating those.

**Najam Ahmed:** That's why they're unlisted.

**Matthew Panzarino:** But they have to.

**Najam Ahmed:** No, the images.

**Najam Ahmed:** No, we don't do the images.

**Najam Ahmed:** They have a content.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** All right.

**Matthew Panzarino:** Well, yeah, let's get the Airtable updated with the published dates and the live links and the status of those because I think that's something Liz needs right away.

**Matthew Panzarino:** So please do that.

**Matthew Panzarino:** And then if you encounter any issues where you're running up against capacity problems because of things like the automations for publishing not working or automations are being too awkward or you need to systematize something that is previously scripted, like Sidney's like, hey, I've got a script for this.

**Matthew Panzarino:** And you're like, oh, how can we systematize this?

**Matthew Panzarino:** Just be proactive about it.

**Matthew Panzarino:** We can do it.

**Matthew Panzarino:** Right?

**Matthew Panzarino:** We'll figure it out.

**Matthew Panzarino:** But if you're falling behind because of that.

**Najam Ahmed:** I downloaded them.

**Najam Ahmed:** They're great.

**Najam Ahmed:** They work fine.

**Najam Ahmed:** Except sometimes the links are broken.

**Najam Ahmed:** You have to check them manually.

**Najam Ahmed:** Could that be...

**Najam Ahmed:** I'm just trying to see.

**Najam Ahmed:** Have you encountered...

**Matthew Panzarino:** Which links are broken?

**Najam Ahmed:** The links to docs?

**Najam Ahmed:** The links to docs.

**Najam Ahmed:** Or even external links.

**Matthew Panzarino:** Okay.

**Najam Ahmed:** Like I can find the link.

**Najam Ahmed:** Usually it's like webflow.com slash feature slash CMS.

**Najam Ahmed:** Those are the ones that we use quite often.

**Najam Ahmed:** But sometimes it's either the list API, the create endpoint API, something like that.

**Najam Ahmed:** Those links are often broken.

**Najam Ahmed:** And I can fix them manually.

**Matthew Panzarino:** Sometimes it's absolutely fine.

**Matthew Panzarino:** Sometimes I don't even need to...

**Matthew Panzarino:** Well, if they're often broken, that's...

**Matthew Panzarino:** Let's file a ticket, right?

**Matthew Panzarino:** That's like, hey, these links are broken.

**Matthew Panzarino:** I'm not sure how to diagnose this issue.

**Matthew Panzarino:** Can Ange take a look at this pipeline and see if any improvements can be made here?

**Matthew Panzarino:** That's the simple way...

**Matthew Panzarino:** mean, simple approach to that.

**Matthew Panzarino:** I could probably look at this and...

**Matthew Panzarino:** I noticed it on a granular level, but why, right?

**Matthew Panzarino:** Like, ENG needs to know because if it's happening across multiple pipelines that you're dealing with, then it's more systemic than just like, oh, this one pipeline has bad instruction or something like that.

**Matthew Panzarino:** So now I just checked all of the links in this integration guide here.

**Matthew Panzarino:** The, which one is this?

**Matthew Panzarino:** The build SaaS platforms with usage-based billing.

**Matthew Panzarino:** And all of these seem to work.

**Najam Ahmed:** Yeah, I mean, sometimes they're all fine.

**Najam Ahmed:** Like I said, it's, I will make a note of the ones that are broken and then I will send you a bunch of links or maybe even just talk to engineering and see what's happening.

**Matthew Panzarino:** Yeah, I would either just ask an EPD help or just file a ticket straight out, right?

**Matthew Panzarino:** Because yes, if it's broken links repeated, it's a repeated issue with broken links.

**Matthew Panzarino:** You're like, hey, I have to manually fix these links.

**Matthew Panzarino:** Any detail you can give about which links are specifically breaking would be lovely because perhaps it is something to do with those links, right?

**Matthew Panzarino:** A quirk of those URLs or whatever.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** But regardless, if you are having to manually check those links for something as straightforward as literally a malformed link or incorrect link, that's an engineering problem, right?

**Matthew Panzarino:** That's not something you need to be doing manually or should be doing manually each time.

**Matthew Panzarino:** That's a capacity issue, right?

**Matthew Panzarino:** And you're like, hey, very clearly, this is getting in my way of time to delivery or slowing me down.

**Matthew Panzarino:** And it seems to be a relatively systemic issue.

**Matthew Panzarino:** It's happening across multiple pipelines or multiple runs.

**Matthew Panzarino:** Can you take a look at this and evaluate it and give specific run examples?

**Najam Ahmed:** Okay, yeah.

**Najam Ahmed:** I'll start making a note now.

**Matthew Panzarino:** right, thank you.

**Matthew Panzarino:** Yeah, but there's no reason that, yeah, broken links every time should be your, like, this is, I guess I got to live with this, you know?

**Matthew Panzarino:** We'll figure something out.

**Najam Ahmed:** Our engine team will figure something out there.

**Najam Ahmed:** Okay, all right.

**Najam Ahmed:** Thank you.

**Matthew Panzarino:** Okay, thank you, sir.

**Najam Ahmed:** Thanks, Fathom.

**Najam Ahmed:** I'll let you know as soon as I'm done, yeah?

**Matthew Panzarino:** Great, wonderful.

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** appreciate that.

**Matthew Panzarino:** Thanks, man.

**Matthew Panzarino:** Bye-bye.
