# SentinelOne <> Growth X - Weekly Sync

<metadata>
date: 2025-11-13
time: 15:00 UTC
duration: 33 minutes
organizer: team@growthxlabs.com
participants: Katya Luscomb, Marcus Derencius, Marisol Smith (GrowthX), Ankit Pahuja, Mansi Bhalothia (SentinelOne)
fathom_recording_id: 101404096
fathom_url: https://fathom.video/calls/472178087
share_url: https://fathom.video/share/9fEJyMtDKAf8oSu5nXGCisRY3UEQsRJC
source: fathom
enriched_on: 2026-03-02 14:32 UTC
</metadata>

---

## Summary

GrowthX and SentinelOne synced on CVE page strategy and CS101 content pipeline progress. The team confirmed a two-week code freeze for Algolia search implementation, which pauses CVE publishing but not content uploads—GrowthX will now push content to ContentStack in Monday batches for Tuesday publication by SentinelOne's web team. On CS101, three PMM-reviewed articles (Software Supply Chain Security, Malware vs. Virus, Infrastructure as a Service) are ready for Monday publication. The team expanded CS101 content pillars to Wayfinder services (Threat Hunting, MDR, Incident Response) and new acquisition offerings (Prompt Security, Observo) to create clear content lanes and avoid keyword cannibalization.

---

## Context

SentinelOne is a GrowthX client engaged in a multi-workstream content engagement covering both CVE (Common Vulnerabilities and Exposures) page strategy and CS101 (Cybersecurity 101) content production. The relationship involves close collaboration between SentinelOne's marketing team (led by Ankit Pahuja) and product/content teams with GrowthX's content strategy and production team (Katya Luscomb leading execution). The CVE initiative launched with 500+ pages and is scaling to thousands—requiring technical improvements (Algolia search implementation) and operational workflows (batch publishing via ContentStack). The CS101 content library is a high-volume strategic initiative where GrowthX supplies keyword research and content assignments with SentinelOne PMM review and publication. This sync focused on unblocking publishing workflows and expanding content opportunities as the team hits keyword saturation in narrow AI pillars.

---

## Relevance

**To GrowthX Delivery:**
- CVE workflow shift to batch publishing (200-entry batches Mondays for Tuesday release) reduces complexity on GrowthX's side and leverages new ContentStack automation—estimated 1-day lift from Marcus to build the Google Docs → ContentStack automation.
- CS101 pipeline evolution: moving PMM reviews to Google Docs (vs. ContentStack) feeds comments directly into GrowthX's agentic pipeline, improving iteration cycles and reducing approval friction.
- Content pillars expansion beyond narrow AI keywords (adding Wayfinder, Prompt Security, Observo) unblocks assignment approvals and increases publishing velocity—directly impacts client satisfaction and revenue per account.
- GitHub-Airtable integration (due next week) automates CVE deduplication and new entry ingestion, reducing manual data management across SEMrush/GitHub sources.

**To GrowthX Business Development:**
- SentinelOne expanded trust in GrowthX strategy layer: asking GrowthX to identify new content lanes (Wayfinder, acquisitions) vs. just executing existing pillars—signals strong account health and expansion opportunity.
- Volume and quality metrics trending positive: 500+ CVE pages live, Google Search Console indexed with early impressions, 3 CS101 articles ready this week—delivers visible proof of concept for further scope.
- Code freeze timing creates a forcing function for workflow optimization (batch publishing, automation) that GrowthX led—shows execution excellence under constraints.

**To CheckThat:**
- SentinelOne's search infrastructure challenge (thousands of CVEs, Algolia implementation) mirrors AEO/visibility concerns for large enterprise security vendors—potential product validation or case study angle for CheckThat.

---

## Overview

- **CVE publishing is paused for ~2 weeks** due to a code freeze for an Algolia search fix. Phase 2 will resume after the freeze is lifted.
- **CS101 strategy expands to new pillars** (Wayfinder services, Prompt Security, Observo) to create clear content lanes and avoid keyword cannibalization.
- **CS101 workflow streamlines** via Google Docs for PMM reviews, with automated final push to ContentStack (unaffected by the code freeze).
- **Three PMM-reviewed CS101 articles ready for Monday publication**: Software Supply Chain Security, Malware vs. Virus, and Infrastructure as a Service.

---

## Key Topics

### CVE Pages: Code Freeze & Publishing Pause

- **Problem:** The current search function is failing with the new volume of CVE pages.
- **Solution:** The web team is implementing Algolia search to support thousands of entries.
- **Impact → Code Freeze:** All publishing and website code changes are paused for ~2 weeks.
  - **Exception:** George can fix minor (P3/P4) design bugs.
- **Revised Phase 2 Plan:**
  - **Status:** Paused until the freeze is lifted.
  - **New Workflow:** GrowthX pushes content to ContentStack → SentinelOne web team publishes.
  - **Cadence:** GrowthX will push in batches of ~200 entries on Mondays for Tuesday publication.
  - **Action:** Ankit will identify a SentinelOne web team contact for publishing.

### CVE Pages: Process Improvements

- **GitHub → Airtable Integration:**
  - **Goal:** Automate pulling new CVEs from GitHub into Airtable.
  - **Action:** Katya to file a Linear ticket for Marcus to assist with the setup next week.
- **Airtable Enhancements:**
  - **Request:** Add columns for live URLs and publish dates.
  - **Action:** Katya will add columns and investigate automation to avoid manual entry.
- **New 2025 CVE Workflow:**
  - **Cadence:** Push new CVEs on Wednesdays to separate them from the backlog.
  - **Action:** Katya will update the Airtable plan with revised dates and volume projections.

### CS101: New Content Strategy

- **Problem:** Finding high-volume keywords for the current AI pillars without cannibalizing existing content is difficult.
- **Solution → Expand Content Pillars:** Ankit approved new content lanes to create clear opportunities.
  - **1. Wayfinder Services:** SentinelOne's rebranded services arm.
    - **Focus Areas:** Threat Hunting, MDR, Incident Readiness & Response.
  - **2. Acquisitions:** Create content on Prompt Security and Observo offerings.
    - **Rationale:** This content is currently missing from SentinelOne's site.
- **Content Refreshes:** The team will revisit a prior report on refresh opportunities.
  - **Action:** Katya to share the report with Ankit for review.

### CS101: Workflow & Content Updates

- **Workflow Improvement:**
  - **Decision:** Keep PMM reviews in Google Docs for better collaboration and to feed comments into the AI pipeline.
  - **Action:** Marcus to build an automation to push final content from Google Docs to ContentStack (est. 1-day effort).
- **Content Status:**
  - **New Content:** 4 revisions and new agentic pipeline articles are due by end of week.
  - **PMM-Reviewed Articles:** 3 articles are ready for publication by Monday.
    - Software Supply Chain Security
    - Malware vs. Virus
    - Infrastructure as a Service
  - **Action:** Mansi to resolve comments and publish. Katya to track URLs.

---

## Action Items

**Katya Luscomb (GrowthX)**
- File Linear ticket for GitHub↔Airtable integration; send requirements to Marcus
- File Linear ticket for CS101 ContentStack publish step; coordinate with Marcus to implement
- Update Looker to include new CVE entries
- Add Live URL and Published Date columns to CVE Airtable; investigate automation
- Email Ankit prior CS101 refresh analysis docs
- Research Prompt Security and Observo offerings for CS101 content topics

**Mansi Bhalothia (SentinelOne)**
- Resolve comments on Software Supply Chain Security, Malware vs. Virus, and Infrastructure as a Service articles
- Publish three reviewed articles by Monday
- Send published URLs to Katya

**Ankit Pahuja (SentinelOne)**
- Align with web team on CVE publishing point of contact; share name with Katya
- Add CVE UI/UX feedback to prioritization list
- Check in with web team regarding code freeze timeline
- Email Katya the Wayfinder landing page link

**Marcus Derencius (GrowthX)**
- Confirm with George regarding CVE P3/P4 design bug fixes during code freeze
- Build automation to push final CS101 content from Google Docs to ContentStack (~1 day effort)

---

## Transcript
**Marisol Smith:** This meeting is being recorded.

**Katya Luscomb:** Hi.

**Marisol Smith:** How are you?

**Katya Luscomb:** Good.

**Katya Luscomb:** How are you both doing?

**Marisol Smith:** Good.

**Marisol Smith:** Hi, Marcus.

**Marcus Derencius:** Hello, hello.

**Katya Luscomb:** I just got a message from OnKit.

**Katya Luscomb:** It sounds like at least a few of them are running like five minutes late.

**Katya Luscomb:** So we have a second.

**Katya Luscomb:** Nice.

**Katya Luscomb:** But kind of bummer timing on the code freeze.

**Katya Luscomb:** Thanks for that heads up, Marcus.

**Marcus Derencius:** I think it's related because now that it's live, the search function is failing. The search capability is needed for a large number of entries.

**Marcus Derencius:** Yeah, maybe it was a small concern initially, but it's become a big one.

**Katya Luscomb:** Yeah, the problem became more obvious once we had all those pages.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** Makes sense.

**Katya Luscomb:** Did they give an estimated timeline for the code freeze?

**Marcus Derencius:** Not yet.

**Marcus Derencius:** So it's couple of weeks.

**Katya Luscomb:** Okay.

**Katya Luscomb:** That's good to know.

**Katya Luscomb:** Cool.

**Katya Luscomb:** And then I, I know I messaged in the space about trying to hook up GitHub and Airtable.

**Katya Luscomb:** With this code freeze, I think we have a little bit of time to play with that.

**Katya Luscomb:** It's just slightly beyond my technical abilities.

**Katya Luscomb:** But Marcus, do you think you could support me with that maybe next week at some point?

**Marcus Derencius:** Yeah.

**Marcus Derencius:** Send me what, what do you, exactly what you need, what you have.

**Marcus Derencius:** I can, I can check what, we have some things.

**Marcus Derencius:** Yeah, we have some things in place already for GitHub and Airtable.

**Katya Luscomb:** Okay, cool, cool.

**Katya Luscomb:** I'll just file a linear ticket so that it's tracked with everything else.

**Marcus Derencius:** Thank you for all the help on this.

**Marcus Derencius:** I appreciate it.

**Katya Luscomb:** I get eager to try and do a lot, and then I get in over my head, and I'm like, I'm not using my time effectively.

**Marcus Derencius:** Yeah, but nowadays I use Cloud Code a lot, so it helps a lot, the bugging of those issues too.

**Marcus Derencius:** So, yeah, maybe like, you should try the Cloud Code, super fun.

**Katya Luscomb:** I've been playing a lot with like App Scripts and things to leverage that, at least in like Google Sheets.

**Katya Luscomb:** So, yeah, getting ChatGPT to help with that.

**Marcus Derencius:** Nice.

**Katya Luscomb:** Hi, Mansi.

**Mansi Bhalothia:** Hi, Kathia.

**Mansi Bhalothia:** Ankit and I are on another call.

**Katya Luscomb:** He's still occupied there.

**Katya Luscomb:** thought I can just come in and see updates on CS101.

**Katya Luscomb:** Yeah, no worries at all.

**Katya Luscomb:** I know he had sent a message.

**Katya Luscomb:** Yeah, we can jump into that section if you want to go ahead and get started.

**Katya Luscomb:** Did you have anything?

**Mansi Bhalothia:** I'm sorry, please go ahead.

**Katya Luscomb:** No, no, it's okay.

**Katya Luscomb:** I have quick updates on our new content pipeline. We're finalizing refinements to our new agentic pipeline. The new articles will be ready by the end of this week, and the four revisions you sent on Monday will be done today or first thing tomorrow morning.


**Mansi Bhalothia:** I have an update on PMM.

**Mansi Bhalothia:** we received three articles.

**Mansi Bhalothia:** I think there are in general five articles that are pending.

**Katya Luscomb:** I have seven, it looks like, but I do try and look over the CS101 page to see what's been published, but sometimes I think titles change, and so I miss a few things.

**Mansi Bhalothia:** So if you can see my screen, these are...

**Mansi Bhalothia:** I think out of these, I received three today, and I did send a reminder to other PMMs.

**Mansi Bhalothia:** I'm yet to hear back from them.

**Mansi Bhalothia:** So I think we'll be going live with those three articles, either by tomorrow or first thing Monday.

**Katya Luscomb:** Great.

**Katya Luscomb:** Do you know which three it was?

**Mansi Bhalothia:** I can just follow the...

**Mansi Bhalothia:** Just pulling up.

**Katya Luscomb:** Yeah, no worries.

**Katya Luscomb:** Helps me when I'm hunting on the page for the published URLs.

**Mansi Bhalothia:** I think he has left a lot of comments.

**Katya Luscomb:** I

**Mansi Bhalothia:** I need to resolve them. There's one article titled Software Supply Chain Security that came back from Camden. Then there's Malware vs. Virus. And then Infrastructure as a Service.

**Katya Luscomb:** Okay, cool.

**Mansi Bhalothia:** And it sounds like you said you still need to resolve the comments on those and then likely publish them.

**Mansi Bhalothia:** Yeah, I just, there are quite a few comments left there.

**Mansi Bhalothia:** So I'll resolve it by tomorrow and then we can publish it.

**Katya Luscomb:** Perfect.

**Katya Luscomb:** I'll update those three tomorrow then, and then check either tomorrow afternoon or Monday morning for those URLs.

**Mansi Bhalothia:** The final article will also come by the end of the week, so we can publish it by Monday.

**Katya Luscomb:** Perfect. I won't change the status yet since it's not quite ready for publication, but that's good to know.

**Mansi Bhalothia:** Okay.

**Mansi Bhalothia:** I also read your comment about PMM reviews in Google Docs. It would be easier for them to leave comments in Google Docs instead of ContentStack, and it would be better for us too since your algorithm incorporates those comments and I can resolve them more efficiently.

**Katya Luscomb:** Yeah, I just wanted to check because I know we had talked a little bit about updating our pipeline so that things get pushed to ContentStack.

**Katya Luscomb:** And so I just wanted to understand the flow of how those revisions would be applied and then at what point we would need to put it into ContentStack and send it to you all.

**Katya Luscomb:** So I think what we can look into doing is having a final step that doesn't run it until we approve it.

**Katya Luscomb:** And then we would wait for you to get all that feedback and finalize the article and then we could paste it in and send it.

**Mansi Bhalothia:** So it makes sense.

**Katya Luscomb:** Perfect.

**Katya Luscomb:** I do know, actually it's nice that you're on, Marcus, because I know there's the code freeze related to the CVE pages.

**Katya Luscomb:** Do you know if the code freeze would impact being able to adjust the current CS101 pipeline to send things to ContentStack?


**Katya Luscomb:** No worries.

**Marcus Derencius:** The code freeze is only on the website for CVE pages. We can still publish CS101 content to ContentStack—we just can't change the website itself. So publishing direct to ContentStack is possible.

**Katya Luscomb:** Cool, cool.

**Katya Luscomb:** I will, I'll file a linear ticket with some of the breakdown on what that might look like, and we can start playing with that a little bit.

**Katya Luscomb:** Perfect.

**Katya Luscomb:** Should we wait for Ankit, or can we dive into some strategy pieces? I wanted to discuss how we're generating assignments and some friction points we've noticed.

**Mansi Bhalothia:** Either way works for me.

**Katya Luscomb:** I can cover performance review when he joins. We are seeing some positive signs, which is nice. Anything else on CS101 before Ankit arrives?

**Mansi Bhalothia:** I'm going to work through the comments on the three docs that came back. There are some comments from others too, but nothing specific beyond those at the moment.

**Katya Luscomb:** No worries.

**Katya Luscomb:** I figured I'd check just in case, especially while we're playing with our new pipeline and fine-tuning it.

**Katya Luscomb:** I was curious, because my understanding is that there is another essay.

**Katya Luscomb:** SEO agency that's also doing content for CS101.

**Katya Luscomb:** I was curious if they have a specific lane, kind of like we've identified the AI three pillars that we've been working on.

**Katya Luscomb:** I was curious if they have a specific lane, because I know there's a risk of overlapping content, and that's part of the review process in the assignments.

**Katya Luscomb:** Do you know, or that might be, again, another better question for Ankit.

**Mansi Bhalothia:** We work with another agency on CS101 content, and they focus on different keyword lanes. We ensure the keywords don't overlap between our efforts and theirs.

**Katya Luscomb:** That makes sense.

**Katya Luscomb:** Hi, Ankit.

**Ankit Pahuja:** Hey, Katya.

**Ankit Pahuja:** Hey, Marisol.

**Ankit Pahuja:** Marcus.

**Ankit Pahuja:** How's everyone?

**Katya Luscomb:** Good.

**Katya Luscomb:** Good.

**Katya Luscomb:** How are you doing?

**Katya Luscomb:** Busy day?

**Ankit Pahuja:** Doing well, doing well.

**Ankit Pahuja:** Busy day.

**Ankit Pahuja:** just, we were together, Mansi, myself, and the team were in a QBR, and I was just listening to the final thoughts, so I got late.

**Katya Luscomb:** Sorry about that.

**Katya Luscomb:** No worries.

**Katya Luscomb:** And we covered some of the initial CS101 updates, so we can jump into some of the more meaty stuff.

**Katya Luscomb:** As far as CD, I think we're all up to date that the code freezes happened.

**Katya Luscomb:** Excited that at least the first 500 pages went live.

**Katya Luscomb:** I know I was excited to say that we could start phase two this week and then had to revise that.

**Katya Luscomb:** So, one thing that I did want to clarify, as far as process goes, once that freeze is lifted, is for the publishing flow.

**Katya Luscomb:** Because I know that access to content stack, there's like some security limitations and considerations.

**Katya Luscomb:** And so, my understanding of the workflow is that we on the GrowthX side will push the

**Katya Luscomb:** Content2, ContentStack, let you guys know, and then you will actually hit publish, correct?

**Ankit Pahuja:** That's right.

**Ankit Pahuja:** So what does that mean in terms of effort?

**Ankit Pahuja:** Because my team has to do it because we have the association.

**Ankit Pahuja:** So there's some bandwidth to keep out.

**Katya Luscomb:** So that's the reason I asked this.

**Katya Luscomb:** Got it.

**Katya Luscomb:** So for us, it really is just a matter for that workflow.

**Katya Luscomb:** It's a matter of uploading the CVE entries.

**Katya Luscomb:** We'll probably do them in like batches of like 200 just to like catch if there's any like small blips as we're doing that.

**Katya Luscomb:** But upload those in small batches and then push those through likely on Monday so that those can get to you all in advance.

**Katya Luscomb:** So they're ready for Tuesday for you all to hit publish in ContentStack.

**Katya Luscomb:** Every once in a while, there's a CVE entry.

**Katya Luscomb:** I know we had one out of like the original 505 that...

**Katya Luscomb:** So anyway...

**Katya Luscomb:** um

**Katya Luscomb:** Was in SEMrush, but wasn't an actual published entry in GitHub.

**Katya Luscomb:** And so like we had to look and confirm why that one was having an error.

**Katya Luscomb:** And so there's some little things like that that require just a few minutes of our time looking into those pieces.

**Katya Luscomb:** But otherwise, the lift in terms of sending the content to you is fairly light.

**Katya Luscomb:** anticipate it take us maybe like an hour the first time as we're looking through some of those errors.

**Katya Luscomb:** I did want to know once we send those over, is there someone in particular that we should ping on your team that they've all been pushed for that visibility?

**Ankit Pahuja:** That's right.

**Ankit Pahuja:** So I think I'll have to set that alignment once with the web team because someone from the web team probably would do internally.

**Ankit Pahuja:** And I can get the name of the person who would help.

**Katya Luscomb:** Perfect.

**Katya Luscomb:** Great.

**Katya Luscomb:** And then just a couple other updates.

**Katya Luscomb:** I'm going to be working with Marcus on finalizing that link between GitHub and Airtable.

**Katya Luscomb:** It's slightly more technical than I was hoping it was going to be, so I'm looping him in.

**Katya Luscomb:** But we're planning on getting that done next week, and that's going to help just de-dupe the SEMrush entries that we've got and other things, and making sure that those new entries are getting added on a regular basis.

**Katya Luscomb:** And then I'm also going to have our team update Looker so that this new CV entries are considered as part of all our data.

**Ankit Pahuja:** Sounds good.

**Ankit Pahuja:** So while we are actually discussing CV, we wanted to chat through with Marcus as well.

**Ankit Pahuja:** Marcus, did you have that meeting with the web team prior?

**Marcus Derencius:** Yeah, I just, yeah, we had a meeting, so where they let me know that they are doing the code freeze, they're going to update the codes and fix the searching to use Algolia.

**Marcus Derencius:** So that's the final solution.

**Marcus Derencius:** So we can support thousands of entries.

**Ankit Pahuja:** joining Thank you you much.

**Ankit Pahuja:** so you much.

**Ankit Pahuja:** much.

**Ankit Pahuja:** Is this something that you are doing, they are doing, or what's it?

**Marcus Derencius:** Yeah, they are doing.

**Marcus Derencius:** So I stopped doing any, about fixes, P0s and P1s on the CV pages, why they are going to be doing that.

**Marcus Derencius:** And George even asked about the minor issues, P3, P4s, he might do some, but P1 and P0s, the web team is going to be doing, for a couple weeks.

**Ankit Pahuja:** Okay, got it.

**Ankit Pahuja:** Cool.

**Ankit Pahuja:** So, I didn't get the George, I mean, part.

**Marcus Derencius:** So, George has also fixed all the Yeah, George is fixing some bugs, so, yeah, that part was not super clear, George can still fix some bugs.

**Marcus Derencius:** Of the P3s and P4s related to design, why they are doing this.

**Marcus Derencius:** So apparently George can fix it, but I just have to double confirm because it's on a little bit fully clear.

**Ankit Pahuja:** Got it, got it.

**Ankit Pahuja:** So there were some feedbacks probably on the UI UX side that came from the team, and a few were logical as well.

**Ankit Pahuja:** So we might want to prioritize.

**Ankit Pahuja:** So that I will add to the list and probably initiate a discussion on what we might want to prioritize.

**Ankit Pahuja:** And yeah, rest looks good like we are live.

**Ankit Pahuja:** So that's a good thing.

**Ankit Pahuja:** We also submitted the sitemap to the Google Search Console.

**Ankit Pahuja:** A lot of pages are being indexed right now.

**Ankit Pahuja:** So I also see a few impressions already in the area.

**Ankit Pahuja:** So it's a good thing.

**Ankit Pahuja:** So, yeah, I think we are really looking forward to adding those.

**Ankit Pahuja:** And to echo on the plan, Katya, that you had laid out, totally aligned, let's do that as next steps for a few weeks, and then we can check again if we want to up the volume and however we'd like.

**Ankit Pahuja:** And, okay, I wanted to discuss something.

**Ankit Pahuja:** Could you open that plan, the table problem?

**Katya Luscomb:** Yes.

**Katya Luscomb:** Oh, I had it linked, and then I removed it.

**Katya Luscomb:** me just one second.

**Katya Luscomb:** I did want to clarify, because in the update that Marcus had shared with me earlier, it sounds like we are paused on sending new CVE entries through.

**Katya Luscomb:** Is that correct, Marcus?

**Katya Luscomb:** So it sounds like phase two, we won't actually be able to start next week, that we would need to postpone until the code freeze is lifted.

**Marcus Derencius:** week.

**Marcus Derencius:** Okay.

**Marcus Derencius:** So, okay.

**Marcus Derencius:** So, let's go.

**Marcus Derencius:** You

**Marcus Derencius:** Yeah, yeah, they said, even publishing to hold, because it can affect performance, so.

**Ankit Pahuja:** How much time did we plan, Marcus, in the meeting?

**Marcus Derencius:** Yeah, they didn't give, they said a couple weeks, so no clear date yet.

**Ankit Pahuja:** Okay, got it.

**Ankit Pahuja:** Cool, I can also probably check in once with the web team over the meeting, so.

**Ankit Pahuja:** Okay.

**Ankit Pahuja:** All right, then probably, yeah, that's right, we can't start with publishing.

**Katya Luscomb:** I know, it's such bummer timing.

**Ankit Pahuja:** Yep, that's right.

**Ankit Pahuja:** Cool, I think meanwhile, what we could do, or rather it's a question, so row number three, or rather four in the table, says new 2025 CVs, and then there's a TBD to it.

**Ankit Pahuja:** So, do we have a workflow for new CVs set?

**Ankit Pahuja:** I mean, it would work the same as we have previously.

**Katya Luscomb:** Yeah, so that is, that's one of the things that I'm working on with Marcus is connecting GitHub to Airtable.

**Katya Luscomb:** So it will pull those in and we can see the new CBE entries.

**Katya Luscomb:** And in my initial proposal, just so we don't conflate the current list with the new entries, I had proposed that we would push those on Wednesdays to you all, just so there's some clarity in terms of, and we don't overload our system either.

**Katya Luscomb:** Because my understanding is that right now, there can be anywhere between like, 50 to 200 CBEs added a day.

**Katya Luscomb:** And so if we're pushing those each week, that volume can get quite high.

**Katya Luscomb:** And so that'll keep us kind of within a workable range for uploading those to Atlas, making sure they're all going through and then pushing them on out to you guys.

**Katya Luscomb:** they're ready by Tuesday and Wednesday, respectively.

**Ankit Pahuja:** All right.

**Ankit Pahuja:** All right.

**Ankit Pahuja:** Yeah, makes sense.

**Ankit Pahuja:** I think this can be worked upon in parallel.

**Ankit Pahuja:** By the time we have that code freeze out.

**Katya Luscomb:** Yeah, so one of the things, next week once we get that connection in Airtable, I'll have a better view of how many new 2025 entries we have.

**Katya Luscomb:** And I can come back and revisit these numbers and give a more accurate update in our next meeting as well.

**Katya Luscomb:** At least for the first couple weeks that we're pushing these out.

**Katya Luscomb:** Because I anticipate there's probably quite a few new 2025 entries from when SEMrush got pulled and entries that didn't initially have traffic in SEMrush.

**Katya Luscomb:** So keeping that in the back of my mind as well.

**Ankit Pahuja:** Right, right.

**Katya Luscomb:** I can also come in, since these dates are getting pushed, I can come in and update these dates as well to reflect a likely start.

**Katya Luscomb:** I guess it would be close to the end of November for Phase 2 starting.

**Ankit Pahuja:** Right, thank you.

**Katya Luscomb:** Any other questions here?

**Ankit Pahuja:** No, I think they're good.

**Ankit Pahuja:** For CV, I do have a request on the Airtable.

**Ankit Pahuja:** And if we could add the two columns with live URLs to a particular CV and the published date.

**Katya Luscomb:** Okay.

**Ankit Pahuja:** I think that way this table would be wholesome and like a go-to table for everything CV.

**Katya Luscomb:** Yep.

**Katya Luscomb:** Makes sense.

**Katya Luscomb:** I'm going to look into seeing if that is something that we can link potentially automate so that we're not pulling a thousand URLs every week manually.

**Katya Luscomb:** So that would be super time-consuming.

**Katya Luscomb:** I'll add those and then, yeah, we'll do some problem solving to pull that more efficiently.

**Ankit Pahuja:** Sounds good.

**Katya Luscomb:** Perfect.

**Katya Luscomb:** I'm just going to add a note that this is paused for publishing.

**Katya Luscomb:** Oops.

**Katya Luscomb:** I can't spell in the morning.

**Katya Luscomb:** All right.

**Katya Luscomb:** Are you ready to hop into?

**Katya Luscomb:** I did have a couple of discussion points on CS101 strategy and topics that we're targeting.

**Katya Luscomb:** Do you have any other questions on the CVE pages before we jump?

**Ankit Pahuja:** Nothing, I think I'm good.

**Katya Luscomb:** Okay.

**Katya Luscomb:** So one of the things was discussing a little bit with Mansi's workflow to connect.

**Katya Luscomb:** We had mentioned wanting to have Atlas be able to push the CS101 content to content stack.

**Katya Luscomb:** I think we've got a clear plan that all of the review would still happen in Google Docs.

**Katya Luscomb:** And then once we get a go ahead that something is finalized, we would upload it and then push it.

**Katya Luscomb:** So we'll start working on setting that up in our backend.

**Katya Luscomb:** It might take potentially a couple of weeks.

**Katya Luscomb:** Do you think, Marcus?

**Marcus Derencius:** No, it should be quicker.

**Marcus Derencius:** Like just the publishing part, it should be quick.

**Katya Luscomb:** Should be fairly quick.

**Marcus Derencius:** Okay.

**Marcus Derencius:** Yeah, yeah.

**Marcus Derencius:** Yeah, like one day or something.

**Katya Luscomb:** Okay, great.

**Katya Luscomb:** Even better.

**Katya Luscomb:** So we should be able to do that next week.

**Katya Luscomb:** We're just putting some final touches on our new agentic pipeline, and I want to make sure that's really polished, and then we can add that step in.

**Katya Luscomb:** As far as – so there's a friction point that I have been hitting with developing new assignments, particularly finding really high-volume keywords relevant to the three clusters that we had identified in the strategy sprint around those various AI topics, while also making sure they don't cannibalize other content, because you all have a really extensive CS101 page, which is great.

**Katya Luscomb:** One thing that helps us execute quickly is having a really clear lane where there's a lot of opportunity for us to kind of run and be able to do five at a time, because that builds up rather fast, as we've sort of seen.

**Katya Luscomb:** So I wanted to talk a little bit about some things that we can consider that might give us some more content opportunities to support with that would help with that publishing pace so we can get you guys more signals and potentially reduce time that we're all spending on those assignments and assignment approvals.

**Katya Luscomb:** I know in the initial phase one of sorry my brain morning brain gone in the strategy sprint we had talked about content refreshes and I wanted to circle back to that idea and see if you all had any specific strategy on refreshes that you're already executing on that we could maybe support with.

**Katya Luscomb:** I know initially we had put together a report on some opportunities, but it's been a while since we talked about any of that.

**Ankit Pahuja:** So it was my first piece that I wanted to discuss a little bit as potential.

**Ankit Pahuja:** That's right.

**Ankit Pahuja:** keep talking about it.

**Ankit Pahuja:** In a meeting that I was in yesterday, we were talking about the kind of sits on blog directory right now.

**Ankit Pahuja:** But would it be possible for you to circle me back with the documents that you mentioned that we have discussed earlier?

**Ankit Pahuja:** Or probably prior me getting into the picture.

**Ankit Pahuja:** It might be possible that those discussions were with Drew or someone in the team Mahathir herself.

**Ankit Pahuja:** That might be pre you, pre me.

**Katya Luscomb:** I think so.

**Katya Luscomb:** Perfect.

**Katya Luscomb:** Yeah, I will loop you into those and then potentially see what opportunity there is, if that's something to explore.

**Katya Luscomb:** And then one of the other pieces that I wanted to think about, because we do have those three pillars.

**Katya Luscomb:** Others are all quite focused on AI-heavy content.

**Katya Luscomb:** I know one of the pieces of feedback was to exclude AI from the keyword because that can limit volume.

**Katya Luscomb:** So it was curious if there's potentially another pillar or two, like content areas where you all really want to win and get more traffic and more recognition that we could potentially sort of own as our primary focus.

**Katya Luscomb:** And that might help direct our keyword research and other efforts.

**Katya Luscomb:** So we have a less risk of cannibalization and it might make, like I said, all those assignments and things more efficient in the approval process.

**Ankit Pahuja:** So AI cybersecurity is number one.

**Katya Luscomb:** That's all we shared with you.

**Ankit Pahuja:** We launched, not launched, but renamed the services lane of the business to Wayfinder.

**Ankit Pahuja:** I'll probably be able to give you the link to the landing page.

**Ankit Pahuja:** That probably can be a good starting point.

**Ankit Pahuja:** So

**Ankit Pahuja:** So we are calling it VFinder Threat Detection and Response to the landing page.

**Ankit Pahuja:** So you might want to check this and services within what's there to offer by us.

**Ankit Pahuja:** So that would be a good starting point.

**Ankit Pahuja:** But to give you a chance, it would be Threat Hunting, MDR, and Incident Readiness and Response.

**Ankit Pahuja:** I can copy that for you.

**Katya Luscomb:** That would be great.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** I can only type so fast.

**Ankit Pahuja:** Perfect.

**Katya Luscomb:** And then what was the second one?

**Katya Luscomb:** MDR.

**Katya Luscomb:** Thank you.

**Ankit Pahuja:** Wayfinder is our recently rebranded services division. It's a trademark. That's where we want to focus for this new content lane.

**Katya Luscomb:** Yeah.

**Ankit Pahuja:** So this generally is not picked up in Cybersecurity 101 as well, especially the incident response, threat hunting side of Okay.

**Katya Luscomb:** Yeah, no, that's actually super helpful.

**Katya Luscomb:** We can start to dig into this a little bit more and see if we can find some ample opportunities here to run with over the next couple weeks.

**Katya Luscomb:** It'd be great.

**Katya Luscomb:** Are there other than...

**Ankit Pahuja:** Oh, go ahead.

**Ankit Pahuja:** Yeah.

**Ankit Pahuja:** We also acquired Prompt Security and Observo to expand our platform capabilities in AI and automation. Their content isn't yet on the SentinelOne site, but you can research their offerings from their websites. Both are focused on AI, cybersecurity, and automation—areas where we don't have coverage yet. I've got approval to create content in these spaces and use them as new content lanes.

**Katya Luscomb:** Perfect.

**Katya Luscomb:** Perfect.

**Katya Luscomb:** This gives us a great starting point. I'm already familiar with Prompt Security and we've woven some of their services into tangentially related articles. Beyond these three pillars, is there anything else you'd like to explore? We've had clients with five or six content categories running in parallel, so we have bandwidth to cover multiple lanes.

**Ankit Pahuja:** I think we're just about out of time. I'll check in with the web team on the code freeze timeline.

**Katya Luscomb:** Thank you all. I have content performance data if you want to review it later, but I won't dive in now since we're at time.

**Ankit Pahuja:** Thanks, everyone.

**Katya Luscomb:** Have a good one.

**Mansi Bhalothia:** Thank you.
