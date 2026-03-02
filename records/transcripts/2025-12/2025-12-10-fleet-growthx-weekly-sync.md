# Fleet <> GrowthX - Weekly Sync

<metadata>
date: 2025-12-10
time: 20:00 UTC
duration: 53 minutes
organizer: erik@growthx.ai
participants: Aida Knezevic, Brock Walters, Erik O'Brien, Irena, John Jeremiah
fathom_recording_id: 107837075
fathom_url: https://fathom.video/calls/500944993
share_url: https://fathom.video/share/GUBYu1Vuw-HG79LxrrLtzwHgYpYEqAnB
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

GrowthX and Fleet finalized a GitHub PR-based content review workflow for new articles, replacing an opaque issue-based process that lacked clear publishing triggers. John confirmed the workflow details with Mike T (Fleet's code owner), while Brock outlined the GitHub mechanics and emphasized the importance of accuracy for competitive comparison articles. The team approved ~20 article topics in Airtable to sustain GrowthX's 5 articles/week output through January, and discussed an upcoming "MDM Handbook" project to establish Fleet as a community authority ahead of MacAdmin podcast sponsorship.

---

## Context

Fleet is an open-source device management platform that GrowthX has been working with on content marketing. John (Fleet's content lead) attended this meeting from Gartner's annual conference, where he was in sessions and meetings with Mike T and others. GrowthX has been drafting content for Fleet's website on MDM topics and competitive comparisons, but the review and approval process was unclear—articles were tracked as GitHub issues without a defined publishing trigger. This meeting was called to align on a formalized GitHub PR workflow that integrates directly with Fleet's website publishing pipeline, clarify approval authority, and work through a large backlog of ~20 approved article topics to ensure GrowthX can sustain output through year-end and into January.

---

## Relevance

**To GrowthX Delivery:**
- GitHub PR workflow now replaces ad-hoc issue-based review, providing a clear publishing trigger and reducing ambiguity.
- Feedback loop via Atlas (company context, personas, writing guidelines) will improve future article quality over time as reviewers flag inaccuracies or ambiguous distinctions.
- 3-week sprint cycle for Fleet's reviewers could create bottleneck if GrowthX continues 5 articles/week cadence; team agreed to monitor queue and adjust as needed.
- Competitive comparison articles require high-scrutiny review for fairness and accuracy—Brock will provide Fleet's internal competitive battle cards to inform these pieces.

**To GrowthX Business Development:**
- Approval of ~20 article topics provides clear runway through January, de-risking content pipeline and reducing need for topic vetting meetings.
- MDM Handbook project is a curated, community-driven resource (not GrowthX-driven) to establish Fleet's authority, with MacAdmin podcast sponsorship as call-to-action.
- Gartner Endpoint Management Magic Quadrant (expected Jan 5) will be leveraged for SEO—GrowthX to create follow-up articles linking keywords/features back to report for credibility boost.

---

## Overview

- **New Review Process:** A GitHub PR workflow is approved for new articles, replacing the issue-based system. This makes the review process more transparent and directly integrates with the website's publishing pipeline.
- **Topic Backlog Cleared:** \~20 article topics were approved in Airtable, providing sufficient content for GrowthX to draft through the end of the year and into January.
- **Competitive Content Strategy:** Comparison articles (e.g., "Jamf vs. NinjaOne vs. Fleet") will be created to capture competitor-specific search traffic. These will undergo high-scrutiny review to ensure fairness and accuracy.
- **"MDM Handbook" Project:** A new, open-source-style "MDM Handbook" is planned to establish Fleet as a community authority. It will serve as a call-to-action for the upcoming MacAdmin podcast sponsorship.

---

## Key Topics

### Content Review Process

  - **Problem:** The current issue-based review process is opaque and lacks a clear publishing trigger.
  - **Solution:** A GitHub PR workflow for new articles was approved.
      - **Workflow:**
        1.  **Draft:** GrowthX creates a new branch and PR.
        2.  **Review:** Marketing assigns a reviewer (from Dale's or Alan's team).
        3.  **Refine:** GrowthX and the reviewer iterate on feedback.
        4.  **Publish:** An approved PR is merged, triggering automatic publication.
      - **Feedback Loop:** Reviewer feedback will be used to update GrowthX's "Atlas" tool (company context, personas, guidelines) to improve future drafts.
  - **Potential Bottleneck:** The 3-week sprint cycle for reviewers could create a backlog if GrowthX's 5 articles/week cadence is maintained. This will be monitored.
  - **Approval Authority:** John will ask Mike T if a dedicated "tone review" step is needed. Mike T previously indicated anyone can approve PRs, but John will seek formal clarification.

### Article Topic Backlog Review

  - **Goal:** Clear the Airtable backlog to ensure a steady pipeline of approved topics.
  - **MDM Fundamentals:** Several educational topics were approved to build topical authority.
      - **Approved:** Zero-touch deployment, device lifecycle, BYOD.
      - **Archived:** EMM/MAM (outdated), "MDM security" (too broad).
  - **Solution Evaluation & Alternatives:** Competitive comparison articles were approved to capture specific search traffic.
      - **Approved:** "15 best MDM providers," "Jamf alternative," "Jamf vs. NinjaOne," "Best MDM for Windows," "Best MDM for Mac."
      - **Archived:** "Apple Business Essentials alternative" (not a direct competitor).
  - **Competitive Content Accuracy:**
      - **Requirement:** These articles must be fair, honest, and avoid marketing fluff.
      - **Resource:** GrowthX will create a "Product Feature Matrix" artifact for these pieces.
      - **Action:** Brock will request access to Fleet's internal competitive battle cards to provide to GrowthX.

### Future Content Strategy

  - **Gartner Report Leverage:** Fleet will be mentioned favorably in Gartner's upcoming Endpoint Management Magic Quadrant (expected Jan 5).
      - **Plan:** Scan the report for keywords and features to create articles that link back to the report, boosting SEO and credibility.
  - **"MDM Handbook" Project:**
      - **Vision:** A curated, open-source-style resource on MDM best practices, hosted at `fleet.com/mdm-handbook`.
      - **Goal:** Establish Fleet as a neutral, authoritative expert in the MDM space, similar to the existing Fleet Handbook.
      - **Execution:** The handbook will be a curated project, not a GrowthX-driven initiative, to ensure quality and community contribution.
  - **MacAdmin Podcast Sponsorship:**
      - **Plan:** Use the "MDM Handbook" as a call-to-action in podcast ads, inviting listeners to contribute to the community resource.

---

## Action Items

**John Jeremiah (Fleet)**
- Convert existing article issues to PRs; assign reviewers
- Confirm with Mike T on dedicated tone/language review step; update workflow diagram

**Brock Walters (Fleet)**
- Brief Dale, Alex, and Alan on new PR review process
- Brief reviewers and start official PR reviews
- Confirm with Mike T on sharing internal competitive comparison matrix; then share with Erik
- Slack Erik the MDM handbook issue link

**Erik O'Brien (GrowthX)**
- Notify Suleiman of the new PR workflow
- Request Suleiman create branches/PRs for the 2-3 articles ready for publication
- Begin drafting ~5 newly approved article topics

---

## Transcript
**John Jeremiah:** Thank you.

**John Jeremiah:** Thank you.

**John Jeremiah:** Well, I'm at Gartner, so between going to some sessions and taking notes and coming back to my room for a couple of meetings and then, you know, the obligatory and the other extended time with Mike and Ashish and others, it's been, it's kind of crazy.

**John Jeremiah:** So, yeah, but I am, well, quick, a couple of updates.

**Erik O'Brien:** I don't know, what's on our agenda?

**Erik O'Brien:** Mainly just to cover off on the things I was paying about earlier this week, just kind of, how do we unblock reviews and then get some approved topics?

**John Jeremiah:** Yeah, I mean, the, are we waiting on anybody else?

**John Jeremiah:** I don't know, let me look at you, Brock.

**John Jeremiah:** Let me look at the camera and see what's.

**John Jeremiah:** Hey, Brock.

**Brock Walters:** Hey, Irena said she was going to join, but a little late, so.

**John Jeremiah:** Okay, we did, we just dive in.

**John Jeremiah:** From where I sit, I think the process of, and I have no doubt to Mike T, who's ultimately the quote-unquote code owner and the keeper of the tone, about the process we have for finalizing the reviews, I think the process of, I answered your, Erik, the question about pull requests.

**John Jeremiah:** Are there other concerns on your end about pull requests, Erik?


**Erik O'Brien:** I don't think so.

**Erik O'Brien:** I was checking with Suleiman, and he said that's completely fine with him as long as we understand the process.

**Brock Walters:** I mean, I think the only issue is that when a pull request is, in our public repo, to create a pull request, a branch has to be created first.

**Brock Walters:** That's not a big deal.

**Brock Walters:** It's just that I don't think you, you can create a new PR without creating a branch.

**Brock Walters:** Now, the thing that's maybe non-obvious.

**Brock Walters:** And please forgive me if you understand all the details of this and I'm telling you stuff you already know, but I'm just explaining it the way I know.

**Brock Walters:** When there's an article on the website that has that edit this article button, what that does is automatically creates a branch for you to do the edit.

**Brock Walters:** If we're going to be doing this from scratch, I think the only thing to know, without having a template that will automatically create a pull request for us, you would need to just know to create the branch first.

**John Jeremiah:** That's all.

**John Jeremiah:** Right.

**John Jeremiah:** Yeah, yeah.

**John Jeremiah:** Well, and as I see it, know, Suleiman creates a branch, names it growthx hyphen article, you know, some part of the article title.

**John Jeremiah:** Yep.

**John Jeremiah:** And this is a relatively, I mean, it's a standard kind of practice.

**John Jeremiah:** We're going to take it from master to have a short-lived branch for this one article.

**John Jeremiah:** It's a net new article.

**John Jeremiah:** There's no possibility of having any sort of merge conflicts when we get done.

**John Jeremiah:** And then when we're done.

**John Jeremiah:** And we merged and the branch gets deleted.

**Brock Walters:** Yeah, exactly right.

**John Jeremiah:** Yeah, this is – yeah, for me at least it's a standard – a very standard way of doing it and keep things as simple as we can.

**John Jeremiah:** I don't – yeah, I've wrestled enough with Git in the past that I don't want to make it anything more complicated.

**John Jeremiah:** But Git can – I mean having hundreds or thousands of branches is trivial.

**Brock Walters:** Oh, yeah, that's not the issue.

**Brock Walters:** The issue would just be do we want to see if George or Luke would do anything to create a template that would just do all of that rather than – Yeah, and for me at least let's get the process going today and we can add a template to improve the process as we go.

**John Jeremiah:** For the other thing – and one of the things I'm going to do, Erik, is the existing issues we need to – I want to get those into pull requests so we can – Yeah.

**John Jeremiah:** So we

**John Jeremiah:** So this to Mike to make sure that we're in sync.

**John Jeremiah:** If I can find it, I apologize, I didn't have it open.

**John Jeremiah:** There we go.

**John Jeremiah:** I'll find it this way faster.

**John Jeremiah:** There we go.

**John Jeremiah:** So conceptually, the flow would be marketing is going to prioritize and select topics.

**John Jeremiah:** And this is what I've written down.

**John Jeremiah:** I'm just doing it graphically to make sure we can sort of see the boxes.

**John Jeremiah:** GrowthX is going to draft the article, create a pull request, name it in branch and pull request appropriately.

**John Jeremiah:** I could include and create branch if we want.

**John Jeremiah:** So, and Brock, I'm including you in marketing kind of conceptually here.

**John Jeremiah:** So, collectively, from a marketing perspective, we're going to assign an author or reviewer or a team.

**John Jeremiah:** The reviewer then will take the pull request, provide feedback.

**John Jeremiah:** That feedback then with growthx gets into refinement, right?

**John Jeremiah:** And it could be a case where the author actually makes the edits or makes direct changes, or they could give feedback on a block of it, and it goes back to growthx.

**John Jeremiah:** So, when that step is done, we're back on to the blue with approving the article and then publishing the PR.

**John Jeremiah:** I've asked Mike T if he wants to add a deliberate step for tone review and language review.

**John Jeremiah:** I don't know if we need it, but conceptually we might.

**John Jeremiah:** And then I think the other part I want to make sure we're looking at clearly is a feedback loop that updates.


**John Jeremiah:** What do you guys call your tool, Erik?

**Erik O'Brien:** Atlas.

**John Jeremiah:** Atlas.

**John Jeremiah:** So I'm going to change update model to update Atlas.

**John Jeremiah:** So I think that there would be a step where Atlas gets smarter as we go forward.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Yeah, I think the artifacts that we store within Atlas, so like company context, personas, and writing guidelines, personas I don't think will change very often, if at all.

**Erik O'Brien:** But definitely company context, anytime that there's clarifications, so stuff like Brock pointed out today, if like, you know, MDM is not a third party software, it's, you know, created by Apple and kind of embedded into their systems, stuff like that, we'll want to pull out and then update just maybe products and services are kind of facts and features.

**Brock Walters:** And I think it's great that we capture all that stuff.

**Brock Walters:** And I

**Brock Walters:** Again, just want to caveat, I'm not meaning to be critical because these distinctions are very subtle.

**Brock Walters:** It's just if we get them wrong from the outset, they'll be wrong forever.

**Brock Walters:** So, yeah, I think it's important to capture them.

**Erik O'Brien:** Those are super helpful.

**Erik O'Brien:** Like, that's the type of feedback that we want to get so that we can both pass that along to the managing editor that kind of will refine the article and then be able to update the artifacts as necessary so that we can kind of get it.

**Erik O'Brien:** Update Atlas and the artifacts over time.

**Brock Walters:** And I just want to promise I'm not trying to be dumb about it.

**Brock Walters:** mean, like, but the distinction is, like, a Tesla doesn't have an engine.

**Brock Walters:** has a motor on the wheel, right?

**Brock Walters:** And that's, like, an important distinction.

**Brock Walters:** It's a subtle one.

**Brock Walters:** And to the layperson, nobody cares the difference between the engine and the motor.

**Brock Walters:** But if you're actually talking about electric cars, that distinction matters.

**Brock Walters:** So, I mean, we're at that level of technical detail.

**Brock Walters:** So, yeah.

**Brock Walters:** well.

**Brock Walters:** But I feel like it's important to fix all these things while we can.

**Erik O'Brien:** Yep.

**Erik O'Brien:** No, absolutely.

**John Jeremiah:** So this is what I'm reviewing with.

**John Jeremiah:** I want to get Mike T's last.

**John Jeremiah:** He's the last kind of check in this.

**John Jeremiah:** And I think Brock and Irena, what our next step is, we go back, we return to the conversation we had, what, last week?

**John Jeremiah:** Or it was last week.

**John Jeremiah:** We return with the kind of the update with Dale and Alex for the work we've done, or Alan, with kind of the process and the status and get their agreement.

**John Jeremiah:** We're going to continue.

**John Jeremiah:** And at that point, we're briefing reviewers and we start doing this officially.

**Brock Walters:** I will say, John, did you, sorry to interrupt.

**Brock Walters:** Did you see that Mike, I don't remember where it was.

**Brock Walters:** And of course, this is how it always goes with Mike because he's in Japan.

**Brock Walters:** So his commentary on some thread.

**Brock Walters:** Is maybe in the middle of the night and none of us see it, but there was a thread on which I had said, Mike T is the code owner for this approval.

**Brock Walters:** His response was, anybody can approve those.

**Brock Walters:** And I guess we're just going to have to figure out if that, no, I mean, that is true.

**Brock Walters:** mean, like, occasionally, I can approve something that he has put in as a pull request.

**Brock Walters:** I just think if someone else does it, you can't do your own.

**Brock Walters:** Right.

**Brock Walters:** That's the way our system is currently set up.

**Brock Walters:** So, and he's the default.

**Brock Walters:** That's, so that's what I meant.

**Brock Walters:** It's, it's not necessarily that everyone has to go through him.

**Brock Walters:** It's that he's the default when anyone other than him makes one.

**John Jeremiah:** Me and the point that we is that we have it configured.

**Brock Walters:** So you can't approve your own change.

**Brock Walters:** Correct.

**Brock Walters:** And I mean, the thing, I think that that's a good rule, generally.

**Brock Walters:** There are certain people at Fleet who can do that.

**Brock Walters:** The engineering managers, Luke, I believe, Alan, can approve his own pull requests in certain places.

**Brock Walters:** And maybe what I think you could do or should do is just kind of ask for that mojo.

**John Jeremiah:** I'm going to, I will.

**John Jeremiah:** I mean, for parts of, it's one thing to, for parts of the code, we need to do that.

**John Jeremiah:** But either way, I'll sort that out.

**John Jeremiah:** But I want to, I'm mainly asking, I want to know if Mike thinks we should have a dedicated step in this flow where we get a tone and a, you know, the tone check.

**Brock Walters:** I don't know how much you've spoken with Mike or worked with Mike yet, but I think what he was saying by saying that is, please don't make me do this.

**John Jeremiah:** He can say no.

**Brock Walters:** He can say no, I trust you.

**Brock Walters:** I don't think he was saying no.

**Brock Walters:** He was just saying.

**Brock Walters:** Like, I don't wanna.

**Brock Walters:** And it's like, especially if, like, I do think that the funny thing about him is if he read an article that was bad and it was on the website, then he would be upset about it.

**Brock Walters:** So maybe we should keep him in here as a contingency.

**Brock Walters:** But what he was saying in that thread, and I'm inferring this, is that he didn't need to be involved in this process, especially if there was people that were going to be editing the article before it got to him.

**John Jeremiah:** And that's fine.

**John Jeremiah:** If, and that's, so I, I've, I've tagged him in this issue and I've asked him that question specifically if he thinks we should update this or not.

**John Jeremiah:** Okay.

**John Jeremiah:** And, you know, it's one of those things.

**John Jeremiah:** I'm perfectly okay.

**John Jeremiah:** Look, I, being blunt, I'm gonna be really blunt.

**John Jeremiah:** I love blunt.

**John Jeremiah:** I think we're going way crazy on over indexing on this process.

**John Jeremiah:** I think we should publish this  as fast as we possibly can and fix it in production.

**John Jeremiah:** And if we see an article that we think it needs to get.

**John Jeremiah:** Fine.

**John Jeremiah:** We should fix it.

**John Jeremiah:** And no harm, no foul.

**John Jeremiah:** I mean, Google will, I mean, we're not going to break Google and most people aren't going to see it.

**John Jeremiah:** You know, the fact that we were doing a lot of this work, that we're polishing, we're putting this energy into polishing before it hits the website.

**John Jeremiah:** It would be different if we were casting it.

**Brock Walters:** So let me be blunt back.

**Brock Walters:** If it was your idea for them to be in my name, I wanted them to be in your name as articles written by the marketing department.

**Brock Walters:** I don't want these articles to go out this wrong written by Brock.

**John Jeremiah:** Sorry.

**Brock Walters:** Yeah, that's fine.

**John Jeremiah:** I won't.

**John Jeremiah:** Well, that's fine.

**John Jeremiah:** And the, but the point is, is that they can, they can't, because we're doing it on the website, we can change them quickly.

**John Jeremiah:** So, so it's one of those things that the power of being able to change it.

**John Jeremiah:** So this is fine.

**John Jeremiah:** I think having reviewers and having them in the reviewer's name is, is a benefit.

**John Jeremiah:** So I'm, I'm okay with the process.

**John Jeremiah:** The, but I want to make sure we get this going because.

**John Jeremiah:** The backlog we're building is going to be significant, and I think we have other core content we're going to want to build as we go, and that is going to require a lot more of your expertise, rather than, and we can let GrowthX run on this, and there's other things we're going to need to do.

**John Jeremiah:** So either way, but Eric, this is where we're at, and I think we're really close to kicking this off and going, is where I think we're at.

**Erik O'Brien:** Awesome.

**Erik O'Brien:** Is there, just thinking through this, is there a way once we have Suleiman create the pull requests to alert the assigned reviewer?

**Erik O'Brien:** Or would we need to let you guys know and then kick off a process?

**John Jeremiah:** So, so, so the, the flow of it will be is once we have the pull request, and we assign it to either Dale's team.

**John Jeremiah:** Alan's or Alan's team, it'll then go into their sprint planning and in their work queue, and they will either pick it up and run with it immediately, most likely it will go into the queue and wait for the next sprint.

**John Jeremiah:** So we're going to see this, what we're going to see is these reviews queuing up and sitting in their work to get reviewed as a part of their regular work, it's a sprint process, which is we're on a three-week cycle.

**Brock Walters:** And then if what happens with other issues happens, what I'm envisioning is that at the beginning of a sprint, there will be that bucket of issues, and it's like, okay, this person's going to do these two, and this person's going to do this one.

**Brock Walters:** So at the beginning of a sprint, they'll get assigned.

**Brock Walters:** Sometime during that sprint, they'll get completed or rejected.

**John Jeremiah:** Erik, that make sense to you?

**John Jeremiah:** Or do you see any issues with that?

**Erik O'Brien:** I guess with a three-week cycle, if it becomes later in the cycle and we continue to push out five articles per week, then that's when it could back up to, you know, 15 articles sitting in one sprint.

**Erik O'Brien:** Erik it's picked up immediately, or even put in the backlog for the next one, so...

**Brock Walters:** Erik Well, I'm to continue to pick them as they come, right?

**Brock Walters:** Erik So, I will do as much of that as I can, and I'm going to be able to go a lot faster than I've been going, I promise.

**Brock Walters:** Erik But, I don't know...







**Brock Walters:** I mean, that's the thing, is like, I don't think it makes any sense for GrowthX to be assigning work to someone on Dale's team.

**Brock Walters:** I think it makes sense for Dale to assign that work or have people picket themselves from a bucket.

**Brock Walters:** But maybe this is where the system breaks down.

**Brock Walters:** I don't know, Erik.

**Brock Walters:** Has this never been done in the past like this?

**Erik O'Brien:** We definitely do have, like, other clients that bring in, like, product marketers that are, you know, marketers, but also have the technical ends to do the reviews.

**Erik O'Brien:** But we don't have this kind of rigorous of a process.

**Erik O'Brien:** It's more of like they know that they're coming on a weekly basis.

**Erik O'Brien:** They usually review within two to three days, give us their feedback and edits, and then we'll do final edits before kind of pushing for final review.

**Erik O'Brien:** I don't, like, if this is the process that works for the team, then, like, we're totally flexible with it.

**Erik O'Brien:** I just want to be mindful of the number of pieces we produce creating a backlog that, you know, we keep moving.

**Erik O'Brien:** And I don't want it to seem, like, insurmountable for the team to be like, this is, you know, taking up half my week now, let's review articles.

**Brock Walters:** Yeah.

**John Jeremiah:** Yeah, and the challenge will be, I mean, if, as we go, I mean, we've got roughly 10 reviewers.

**John Jeremiah:** Yeah, we'll see how the, we'll see how this first batch goes through.

**John Jeremiah:** I mean, we'll know more once we get the first batch going through.

**John Jeremiah:** I think that's okay.

**John Jeremiah:** And, and for me, at least, the, the kind of the process question that I got to, I want to think through would be, what labels we put on the pull request, or the status that should be the same.

**John Jeremiah:** Labels as the flow we have, so I think it'll be visible, so when a pull request reaches the final, the approved status, approved to publish, or needs review, so that way, whoever's doing the review and is done with it, I don't know, that's the only process, only part of this I think that's not perfectly clear to me as to how, when, I mean, a good example is, you know, Brock, when, and you're doing this on issues today, on the issues we're working on, I don't know how Solomon knows to publish it.

**Brock Walters:** I mean, I've just been putting a comment in the bottom that said it's ready for published tag team.

**John Jeremiah:** Right.

**John Jeremiah:** And, yeah, and, and so, I don't know, that's the, and I don't know how, like, for one of them I saw earlier today, that was, the comments that approved, I don't know if it was actually published.

**Brock Walters:** I don't know either.

**John Jeremiah:** Yeah.

**John Jeremiah:** I mean, that's the, for me, that's the, to be able to look at this and say, yeah, these were done and published is not clear yet.

**John Jeremiah:** And I don't want to create an overhead where we're slacking back and forth.

**John Jeremiah:** Was this, did this get published?

**John Jeremiah:** Did this get published?

**John Jeremiah:** You know, that's going to be just noise and chaos that I'd like.

**John Jeremiah:** So that way we can look at this process and say, okay, these are all done and they're published.

**John Jeremiah:** Um, but the, the pieces are in place that that'll be a detail.

**John Jeremiah:** have to just sort out as we go.

**John Jeremiah:** Um, but I don't think we've, I don't think it's, for me, it's not clear.

**Brock Walters:** Well, I think the expectation was that we were going to use, I mean, Erik, and correct me if I'm wrong, and I'm not meaning to change the process by saying this.

**Brock Walters:** I'm just trying to figure it out that normally what you have people do is do this kind of no, go, no, go in air.

**Erik O'Brien:** Um, for most clients we have.

**Erik O'Brien:** We access directly to their content management system, and so we stage the article, have them do a final review, and then either one of us can hit publish.

**Erik O'Brien:** I would say the GitHub PR is, we've done it with like a couple clients, but it's not a standard practice that we do.

**Erik O'Brien:** Okay.

**Brock Walters:** I mean, theoretically, that should make it easier.

**Brock Walters:** I mean, an approved PR is going to get merged, and you know, the merge job runs all the time.

**Brock Walters:** So that really is no different than, I mean, that is our CMS.

**John Jeremiah:** Yeah, I mean, rather than, you know, WordPress or Webflow, this is it.

**John Jeremiah:** So, so we're, we're as close to it as we can be.

**Brock Walters:** That's why I wanted to move away from the issue.

**John Jeremiah:** Yeah.

**John Jeremiah:** So we got, so we're basically working on the actual article.

**John Jeremiah:** But yeah, that's, so that's where we're at.

**John Jeremiah:** going ahead need funny So, Now.

**John Jeremiah:** What other, we have the back, we need to look at, I think the backlog of, of article topics in the Airtable is the other action item we need to look at.

**Brock Walters:** Yep.

**Brock Walters:** I think I've commented on about, what, 25% of those haven't gone through the entire list.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** It's about 60 in the considering ideas to approve.

**Erik O'Brien:** Um, and again, like ideally we get some approved across multiple topic clusters, um, with the goal of, you once we get to publish, then we start to track those URLs and see like, what's working, what's not working.

**Erik O'Brien:** Um, and continue to kind of push, um, or where we see some success factors, some of it is, you know, more, we need to get, you know, fill some gaps for just keywords that we're not ranking for, um, just so we can build top.

**Erik O'Brien:** Um.

**Erik O'Brien:** So some of the kind of very broad topics that may seem like why do we care about this, it's really just building that topical authority and clusters on the page.

**Erik O'Brien:** So I'd say like MDM solution evaluation and alternatives is very much bottom of funnel kind of competitive content that does really well with LLMs and just overall search visibility.

**Erik O'Brien:** But the MDM fundamental stuff, I think that's where we need to be creating some content just to create some topical.

**Brock Walters:** I'm working on the one at the top of the list, Erik.

**Erik O'Brien:** But yeah, whenever you guys get the chance, I think going through this and approving, you know, as we're getting towards the holiday season, we'll be producing through the week of the 22nd, and then we have an off week, probably do you guys too, I assume, but probably get like...

**Erik O'Brien:** 10 to 15 of these approved, just so we have enough content to develop through into the new year.

**John Jeremiah:** What's in our current status of approved or unapproved?

**John Jeremiah:** Do you want to do it now?

**John Jeremiah:** Let's just do it now.

**Brock Walters:** Sure.

**John Jeremiah:** And I'm having conversations with Mike M and Ashish, and there's some campaign ideas we're thinking about.

**John Jeremiah:** The on-prem, we think that there's a on-prem play that we should go after.

**John Jeremiah:** So there's the idea, this is as of yesterday, and I don't know what they covered today at eStaff, but the idea around having content around on-prem DDM, which, you know, Jamf won't do.

**John Jeremiah:** Right.

**John Jeremiah:** And as being a topic area that if we can build a campaign with content and landing pages and, you know, things to draw...

**John Jeremiah:** So people into that.

**John Jeremiah:** Well, guess what?

**John Jeremiah:** That's a sweet spot for us.

**John Jeremiah:** I don't know how it aligns with what we have here.

**John Jeremiah:** But in my view, let's get stuff out of the considering and into the moving forward process.

**John Jeremiah:** And we can come back with campaign ideas in the next pass.

**John Jeremiah:** I don't think we have to do it right now.

**Brock Walters:** Erik, do you have way of sorting these by the ones that have already had comments put on them?

**Erik O'Brien:** Erik Let's see.

**Erik O'Brien:** I don't believe we can sort by comments.

**Brock Walters:** Okay.

**Brock Walters:** I mean, I haven't done anything other than put comments in.

**Brock Walters:** I haven't grouped them in or tried to move anything ever.

**Erik O'Brien:** Erik Yeah.

**Erik O'Brien:** I feel like...

**Erik O'Brien:** Erik Whichever group you want to start with.

**Erik O'Brien:** Yeah, let's start with MDM fundamentals.

**Brock Walters:** Erik That one's good go.

**Brock Walters:** I'm

**Brock Walters:** I'm about two minutes from being done, and I'll approve it as soon as we get off this call.

**John Jeremiah:** It's still in considering.

**Brock Walters:** Well, let's approve it then.

**Brock Walters:** I mean, zero-touch deployment seems like a good option.

**Brock Walters:** Sure.

**Brock Walters:** I don't know about that.

**Brock Walters:** I would like to have a different topic than that that seems very broad.

**Brock Walters:** I would like to have something more focused on software than that.

**Brock Walters:** Yep, I like that, device lifecycle.

**Brock Walters:** It's good.

**Brock Walters:** The only thing I would say about that is Fleet is not a hardware asset manager.

**Brock Walters:** So if the purpose of that article is to just generally talk about the topic because it's good for searching.

**Brock Walters:** Yes.

**Brock Walters:** Okay.

**John Jeremiah:** Yeah, mean, these don't have to be about Fleet.

**Brock Walters:** mean, these are- Oh, right.

**Brock Walters:** I mean, a lot of them are certainly a level above the actual product, for sure.

**John Jeremiah:** Yeah.

**John Jeremiah:** In fact, I think that in principle, a lot of this stuff, I mean, when we get into the comparison stuff, that becomes really obvious it is about Fleet.

**John Jeremiah:** But there's a level of this that, you know, we're educating people.

**John Jeremiah:** Yeah.

**John Jeremiah:** Because they're asking questions of LLMs, and LLMs are looking for authoritative answers.

**Brock Walters:** And if we provide that, then- I would like to archive this topic.

**Brock Walters:** E-M-M, M-A-M, I don't want to talk about that.

**Brock Walters:** That one's fine.

**Brock Walters:** The other thing I guess I would say, though, is what about repetition?

**Brock Walters:** The one that I'm working on is basically this exact same topic with a different name.

**Brock Walters:** Is that by design?

**Erik O'Brien:** What's the one you're working on right now?

**Brock Walters:** Six benefits of Apple MDM explained.

**Erik O'Brien:** Yeah, so that one's probably targeting Apple MDM benefits.

**Erik O'Brien:** So it's mainly keyword.

**Brock Walters:** this is fine then.

**Brock Walters:** MDM security.

**Brock Walters:** I don't know what that means.

**Brock Walters:** Does that mean the security of the MDM server itself?

**Brock Walters:** Or does it mean security settings that are set with MDM?

**Brock Walters:** That's too big.

**Brock Walters:** means.

**Brock Walters:** I I I I

**Brock Walters:** That's a good one, the BYOD.

**Brock Walters:** Interesting.

**Brock Walters:** Sure.

**Erik O'Brien:** All right.

**Erik O'Brien:** Look at us go.

**Brock Walters:** Look at us go.

**Brock Walters:** Um, 15 best MDM providers.

**Brock Walters:** So this is talking, this is like talking about competitors?

**Erik O'Brien:** Mm-hmm.

**Erik O'Brien:** Yeah, this entire cluster is mainly about like solution evaluation and alternatives.

**Brock Walters:** Okay.

**Brock Walters:** I think that's obvious, an obvious choice.

**Brock Walters:** Um, GM alternative.

**Brock Walters:** Sure.

**Brock Walters:** We all try Okay.

**Brock Walters:** Okay.

**Brock Walters:** Okay.

**Brock Walters:** Thank you.

**Brock Walters:** Now what does it mean if it has an X file?

**Erik O'Brien:** There'll be a number there.

**Erik O'Brien:** So like eight benefits or ten benefits.

**Brock Walters:** okay, okay, okay.

**Brock Walters:** It's not you guys are just using Roman numerals, I thought, maybe just to be different.

**Brock Walters:** Maybe there's some sort of optimizing the searching for Roman numerals.

**Brock Walters:** Okay.

**Brock Walters:** Benefits of using mobile device management software.

**Brock Walters:** Does that mean using a mobile device management solution?

**John Jeremiah:** Yeah.

**John Jeremiah:** Yeah, I think so.

**Erik O'Brien:** Okay.

**John Jeremiah:** Yeah.

**John Jeremiah:** It's the benefits of MDM.

**Brock Walters:** Why do you do MDM?

**Brock Walters:** I mean, it's exactly, again, this is the exact same article that I'm looking at today, but it's fine.

**John Jeremiah:** Yeah, there will certainly be some content that if one were to read it, this is an article that ideally you're thinking about the LLM is going to find it and looking for a list.

**John Jeremiah:** Interestingly, I talked

**John Jeremiah:** The CTO of Adagy today, who came out of a, who was sitting in a session with me here at Gardner.

**John Jeremiah:** Yeah.

**John Jeremiah:** We had a nice conversation.

**Brock Walters:** Jason, good guy.

**Brock Walters:** Jason Depthorne, he's a good guy.

**John Jeremiah:** Yeah, he's a good guy.

**Brock Walters:** I've had, and the, well, the guy that used to be the head of software engineering at Adagy was the head of software engineering at Jamf for many years.

**Brock Walters:** So, that's how I know Jason.

**Brock Walters:** Okay, sure, this one's good.

**John Jeremiah:** It's funny, I told him my story about the comparison pages I did at Traceable and the impact it had on SEO.

**John Jeremiah:** It's kind of fun to see that we're doing that now.

**Brock Walters:** Here.

**Brock Walters:** Sure.

**Brock Walters:** Is there some method to the madness of having Jamf and Adagy in one comparison and Ninja won by itself?

**Brock Walters:** Is that just random?

**Brock Walters:** What is, what is the reasoning for that?

**Erik O'Brien:** So, if we look at the keyword,

**Erik O'Brien:** There we go.

**Erik O'Brien:** JFPro versus Ninja1.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** And then we're just adding Fleet.

**Erik O'Brien:** So we're optimizing for people searching this, and it will show up alongside that result.

**Brock Walters:** I see.

**Brock Walters:** Okay, so there is some sort of tricksy game here being played that Brock is too stupid to understand.

**Brock Walters:** It's fine.

**John Jeremiah:** Yeah, I did this, when I did this at Traceable, I created comparison pages, Traceable versus, you know, Traceable versus Salt, Traceable.

**Brock Walters:** I did these one-to-one comparisons, head-to-heads.

**John Jeremiah:** And then those ranked so well, I did head-to-heads of competitor A versus competitor B.

**Brock Walters:** Without your product at all?

**John Jeremiah:** No, I included my product.

**John Jeremiah:** Oh, okay.

**John Jeremiah:** But the headline, the SEO was always formatted around, you know, A versus B, and I always included me as the third one, so they always would get a three-way.

**Brock Walters:** Gotcha.

**John Jeremiah:** you know, did the head-to-head, me versus them, because I had all the data.

**John Jeremiah:** Yeah.

**John Jeremiah:** And once I

**John Jeremiah:** started to create those pages, then anybody searching for those pages would hit.

**Brock Walters:** So yeah, this is a tactic I've done too.

**Brock Walters:** Okay.

**Brock Walters:** Sure.

**Brock Walters:** This one's good.

**Brock Walters:** Obviously this one's the same as the others.

**John Jeremiah:** I'll stop asking questions about that.

**John Jeremiah:** Erik, how are you guys qualified to do these?

**Erik O'Brien:** What you mean?

**John Jeremiah:** Just that.

**John Jeremiah:** I mean, these are deep product marketing kind of competitive analysis pieces that require deep insight into our tool versus their tool.

**John Jeremiah:** And you gotta understand both domains pretty well to come up with a reasonable product here.

**John Jeremiah:** How do you guys do that?

**Erik O'Brien:** Erik, most of it's done through that deep researcher that we walked through, or Marcel kind of previewed last week.

**Erik O'Brien:** So it will go to Jamf's or Ninja One's product pages, developer docs.

**Erik O'Brien:** up, So,

**John Jeremiah:** Kind of pull out the way that they look at those features, and then kind of do a feature-by-feature comparison.

**Brock Walters:** And also, Erik, did I provide you the battle card stuff from Adrian?

**Brock Walters:** I thought I did.

**Brock Walters:** If I didn't, I meant to.

**Erik O'Brien:** Let me...

**Brock Walters:** I thought the battle card stuff was part of what you guys had in the Notion doc.

**Erik O'Brien:** I believe we do have it.

**Erik O'Brien:** Yeah, there's like a Jamf fleet comparison.

**Brock Walters:** Yeah, and then there's also one that's kind of more generic.

**Brock Walters:** battle card.

**Brock Walters:** Yes, if you have anything called battle card, I probably gave you the main one.

**Brock Walters:** So John, and I don't know if you've seen those assets, but we did have a contractor kind of preparing.

**Brock Walters:** Based on case studies and interviews he's done with our customers, and based on his own analysis, who's created like some competitive analysis, Val.

**Brock Walters:** Yeah.

**John Jeremiah:** Yeah, I saw it.

**John Jeremiah:** I saw it.

**John Jeremiah:** I think he...

**Brock Walters:** I was pretty impressed with the work he did.

**John Jeremiah:** Yeah, he did some very good stuff, for sure.

**John Jeremiah:** I think, Erik, just to be clear, I expect these comparison pages, when we get into the head-to-heads, are going to go through more scrutiny than normal.

**Erik O'Brien:** Sure.

**Erik O'Brien:** I would expect, so, yeah.

**Brock Walters:** And I'm happy to help with that, John, as much as Yeah, well, I mean, I'm thinking up to and including Mike.

**John Jeremiah:** I mean, I think that when we start to do these things, these are going to be pages that we don't want, we absolutely don't want to overlook a capability that we have, or, you know, we want to be, my philosophy on these is they have to be fair, they have to be honest, they can't be marketing fluff.

**John Jeremiah:** Yep.

**John Jeremiah:** These have to be things that people can look at and go, it's a fair comparison.

**Brock Walters:** Yep, I totally agree.

**John Jeremiah:** So, yeah, but either way, that's fine.

**John Jeremiah:** We should, we should build them.

**Erik O'Brien:** Yep.

**John Jeremiah:** And if, and if you guys have the ability to build them like this, that's awesome.

**Erik O'Brien:** Yeah, we'll, um, we'll also create a

**Erik O'Brien:** New Artifact, specifically for these competitive pieces called a Product Feature Matrix.

**Erik O'Brien:** Okay.

**Erik O'Brien:** So we'll have basically a breakdown of Fleet and then Jamf, Intune, whoever we're going against, and just say like apples to apples.

**Erik O'Brien:** If we list a feature for Fleet, then we have to list it for the other company.

**Brock Walters:** And we already have that internally.

**Brock Walters:** If you don't have it, you probably should start with ours maybe.

**Erik O'Brien:** I don't know.

**Erik O'Brien:** Yeah, I would.

**Erik O'Brien:** Yeah, if it's not in these battle cards.

**Brock Walters:** I don't think it's been, I don't think it's been provided because it's like an internal thing, but I can, I can find out from Mike if it's okay to share with you guys and then you can definitely have it, yeah.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** Yeah, because I think that would speed up the development of that artifact that we can use for these pieces.

**Brock Walters:** And I mean, it's incomplete, but I, you know, I, this kind of analysis is, John, correct me if I'm wrong, but it's kind of never done, right?

**Brock Walters:** No, it's always ongoing.

**Brock Walters:** The features are always changing in every product.

**Brock Walters:** So it's a moving turn.

**John Jeremiah:** Yeah, yeah, yep.

**Brock Walters:** Okay.

**Brock Walters:** Best open source?

**Brock Walters:** Sure.

**Brock Walters:** Best MDM for Windows?

**Brock Walters:** Sure.

**Brock Walters:** That's a good one.

**Brock Walters:** That's a softball for Fleet.

**Brock Walters:** Best MDM for Mac?

**Brock Walters:** Sure.

**Brock Walters:** I thought we already had one like that, but I said I would not say anything more about that.

**Erik O'Brien:** Let's just repeat it until everybody knows.

**Erik O'Brien:** There's a champ versus X versus Fleet, but not a direct one-to-one.

**Brock Walters:** Go tell it out.

**Brock Walters:** Enterprise.

**Brock Walters:** Enterprise mobile device management.

**Brock Walters:** Sure.

**Brock Walters:** Yep.

**Brock Walters:** I guess we have to change the year on that one pretty good.

**Brock Walters:** quick, but.

**Erik O'Brien:** Done.

**Brock Walters:** Excellent.

**Brock Walters:** Sure.

**Brock Walters:** Although, well, hang on a second.

**Brock Walters:** So this is, I don't know about that.

**Brock Walters:** I really don't like that because what that does is, let's archive that one.

**Brock Walters:** What it does is fosters the narrative that Apple Business Essentials is a competitor to tools like Fleet and Jamf, and it's not.

**Brock Walters:** It's a completely different market.

**Brock Walters:** Top Ninja 1 alternative.

**Brock Walters:** Sure.

**Erik O'Brien:** And then Kanji will need to change.

**Erik O'Brien:** Change journey.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** What is it?

**Brock Walters:** It's something to do with the jellyfish.

**Brock Walters:** It's I-R-U.

**Brock Walters:** I-R-U.

**John Jeremiah:** And we'll probably.

**John Jeremiah:** I think we should still call him Kanji.

**Brock Walters:** Okay.

**John Jeremiah:** I mean, they're.

**John Jeremiah:** I I, I, I, I think referring to them with both would make sense for now.

**Brock Walters:** Yeah.

**Brock Walters:** We're kind of doing that same.

**Brock Walters:** Same thing with Workspace ONE.

**John Jeremiah:** They've had seven different names in the last year or so.

**John Jeremiah:** Yeah.

**John Jeremiah:** The Gartner, I just came from a Gartner session, and Brock, if you want to read the notes or the slides there, I put them in Slack.

**John Jeremiah:** That's just a little while ago.

**John Jeremiah:** Okay.

**John Jeremiah:** They are talking a lot about autonomous endpoint management.

**John Jeremiah:** And it's the intersection of endpoint management and digital experience management and using data as a feedback mechanism to drive things.

**John Jeremiah:** It actually was a pretty good talk that Tom just gave.

**John Jeremiah:** I literally just came out of it.

**Brock Walters:** That was a session I with Jason.

**John Jeremiah:** I think we should be paying attention to that and or maybe writing about it.

**John Jeremiah:** can, Erik, can talk about how we want to address the Gartner topics as we go forward.

**John Jeremiah:** But, and the other data point from Gartner is we're going to have a favorable mention in their upcoming Magic Quadrant.

**John Jeremiah:** Right.

**John Jeremiah:** job.

**John Jeremiah:** And maybe, maybe that's a topic we could add to this mix of writing about a Gartner report.

**Erik O'Brien:** Yeah.

**John Jeremiah:** Even though we're not going to pay you for it.

**John Jeremiah:** We're not going to license it.

**John Jeremiah:** I don't think we're going to license it, but at least acknowledging and running with it is going to be something we're going to want to do.

**Brock Walters:** Yeah.

**Brock Walters:** I mean, if it's, oh, sorry, Eric, go ahead.

**Erik O'Brien:** I would say we can kind of scan the report once it comes out.

**Erik O'Brien:** So look for how, you the features or how they kind of rank against other competitors.

**Erik O'Brien:** And it sees those keywords to create articles and kind of boast a link out to the article.

**John Jeremiah:** And we're going to get, there's going to be two artifacts that are going to come from Gartner.

**John Jeremiah:** Actually, there's going to be three.

**John Jeremiah:** The magic quadrant will be their judgment, their evaluation of the vendors.

**John Jeremiah:** They will also have a document, which is the requirements.

**John Jeremiah:** They call that critical capabilities.

**John Jeremiah:** That's the yardstick they used to grade everybody on.

**John Jeremiah:** And then.

**John Jeremiah:** And.

**John Jeremiah:** There will be a market guide that just talks about products in the market, but doesn't provide judgment.

**John Jeremiah:** So those three things are all coming out in early January.

**John Jeremiah:** January 5th is when I expect the Magic Quadrant, so we'll be watching for this.

**John Jeremiah:** And it's a totally new report.

**John Jeremiah:** They haven't done this one in four years.

**Brock Walters:** Wow.

**John Jeremiah:** The last time they did an endpoint management was universal endpoint management in 2022.

**John Jeremiah:** And then they retired it because there was nothing in the market.

**John Jeremiah:** I mean, that's...

**John Jeremiah:** There was nothing changing in the market.

**John Jeremiah:** The market was somewhat static.

**John Jeremiah:** And so now it's just...

**John Jeremiah:** Now it's endpoint management, not universal endpoint management.

**John Jeremiah:** So that way they're covering a broader set of solutions, so.

**Brock Walters:** Okay.

**Brock Walters:** Cool.

**Brock Walters:** Well, I know we're over, Erik.

**Erik O'Brien:** Yeah, I just noticed that.

**Erik O'Brien:** Sorry.

**Brock Walters:** We're so captivating that you just don't pay attention to time anymore.

**John Jeremiah:** That's right.

**Brock Walters:** Yeah, but I appreciate you going over, and hopefully that number of approvals gives you something to work with.

**Brock Walters:** I do agree with John that those comparisons are going to have to undergo more scrutiny, and I will see if I can dig up this comparison matrix and make sure that you guys are approved to access it.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** Yeah, I think as we get the current backlog through in the review process, we'll focus on more of the MDM fundamentals.

**Erik O'Brien:** just to give some breathing room to the reviews, and then we can kind of hit the new year with some of the competitive and alternative stuff.

**Erik O'Brien:** And once we get the matrix that you have, so we'll be equipped to create the artifacts that we need to make sure those are as accurate as possible.

**Brock Walters:** If the articles that we have currently in GitHub all get approved, would that be enough to get us through the end of the year, do you think?

**Brock Walters:** Yeah.

**Brock Walters:** Okay.

**Erik O'Brien:** So those will get approved, published.

**Erik O'Brien:** Okay.

**Erik O'Brien:** As soon as they're approved, and then we'll take probably five of the articles that we just approved and start working on those.

**Brock Walters:** Okay, and to John's point from earlier, does Suleiman know that there are two in there that are ready to go out?

**Erik O'Brien:** I don't believe so, but I will let him know.

**Brock Walters:** Okay, just check the comments for the ones that have approved.

**Erik O'Brien:** Okay.

**Erik O'Brien:** And then for that approval or publishing, does he just need to...

**Erik O'Brien:** I'm not familiar with GitHub.

**John Jeremiah:** He's going to have to create a pull request.

**Brock Walters:** create a branch and create a pull request.

**Brock Walters:** Yeah.

**Brock Walters:** And maybe I should be the one that's doing it.

**John Jeremiah:** Let's see if he can do it.

**John Jeremiah:** He should be able to do it.

**John Jeremiah:** I mean, if he can create an issue, mean, if he's...

**John Jeremiah:** this is not...

**John Jeremiah:** it shouldn't be hard.

**John Jeremiah:** Okay.

**John Jeremiah:** Create a branch, create a pull request, and we process it.

**Erik O'Brien:** Yep.

**Erik O'Brien:** He uses GitHub, I do not.

**Erik O'Brien:** Okay, cool.

**Brock Walters:** So first step, is just to look for the ones that have comment on them that say that they're approved, and in about five minutes, there will be three of those.

**John Jeremiah:** Cool.

**John Jeremiah:** The other thing, one last thing, Brock, just so you know, we're going to end up sponsoring, 99% positive, we're going to sponsor the MacAdmin podcast.

**John Jeremiah:** That's amazing.

**John Jeremiah:** And I intend to direct them to some of this content as being the call to action.

**John Jeremiah:** So as you're thinking about what we're doing here, just planting the seed as you're thinking about it, imagine if one of these podcast articles, podcast ads, says, hey, here's something that's useful, that might be useful to you from FleetDM, and direct them to that page, or to direct them to a landing page that will direct them to where that content is.

**Brock Walters:** So my goal is not to sell on MacAdmins, but to offer value, and this content is intended.

**Brock Walters:** I mean, I would, I guess what I would say in that regard is that those comparison ones would probably not be the best choice for that.

**Brock Walters:** wouldn't, I wouldn't put those on there.

**Brock Walters:** Yeah.

**Brock Walters:** But, but the other ones that are just like, Hey, this is what's what those, those are great value.

**John Jeremiah:** And in fact, there is an issue in, in the marketing board for a MDM handbook, meaning a handbook on the topic of MDM.

**Brock Walters:** Yeah.

**Brock Walters:** mean, Mike and I have talked about this in the past where it's like, he wants us to be experts in that and make it known to everyone.

**John Jeremiah:** And well, the intent, the intent behind that issue, you can go look it up.

**John Jeremiah:** It's, it's on the, it's on the marketing board, but the intent is to take the spirit of the fleet handbook and apply it to the MDM space.

**Brock Walters:** You could call it Wikipedia for MDM.

**John Jeremiah:** Sure.

**John Jeremiah:** But a no marketing, no vendor.

**John Jeremiah:** Let's teach the topics of what is good MDM.

**John Jeremiah:** This would exist under fleet.com slash MDM handbook, and it would be a section of content that's built out and curated in order to teach someone all about MDM.

**John Jeremiah:** Things like GitOps might be relevant sections of that, and I've got a whole issue outlined with structure and a proposed approach to it.

**John Jeremiah:** I'd love talk to you about that.

**John Jeremiah:** Well, go take a look at the issue, and you can throw comments on it, but this is – I think this is a direction we need to go as far as creating valuable content that stands on its own rather than – because today when we throw articles out there, we're just piling articles on top of articles, and there's no structure.

**John Jeremiah:** Yeah, that totally makes sense.

**John Jeremiah:** Yeah, take a look at the issue.

**Brock Walters:** It's there.

**Brock Walters:** I'll Slack you the issue.

**Brock Walters:** Awesome.

**John Jeremiah:** Thanks, guys.

**John Jeremiah:** Thank you.

**Brock Walters:** Take care, everybody.

**Brock Walters:** Oh, sorry, John.

**Brock Walters:** I didn't mean to cut you off.

**John Jeremiah:** Well, did this with Erik, too.

**John Jeremiah:** wanted Erik to hear kind of the conversation of thinking about structure, because it'll help us from an SEO perspective, too.

**Brock Walters:** Meaning that at some point, we'll kind of want maybe some of this auto-generated content to end up there, and how do we do that?

**John Jeremiah:** Potentially.

**John Jeremiah:** So here's the distinction I make.

**John Jeremiah:** Whether or not, you know, the Atlas, whether Atlas gave us the first draft, or whether Erik manually typed it, or whether or not you manually typed it, I'm less concerned about it.

**John Jeremiah:** If we're putting the effort into actually reviewing it and validating and vetting it and making it real and making it ours, then I'm less concerned about this.

**John Jeremiah:** I don't want to have us auto-generate and publish blindly.

**John Jeremiah:** Yeah.

**John Jeremiah:** So whatever ends up there has to be something that we're happy to stand behind.

**John Jeremiah:** But either way, that's my only two cents on it.

**John Jeremiah:** So might some of it...

**John Jeremiah:** Will things get repurposed and put there?

**John Jeremiah:** Absolutely.

**John Jeremiah:** But I don't want to turn it loose and make it a growthx project to say growthx populate this.

**John Jeremiah:** This has to be something we want to curate.

**John Jeremiah:** And, and in fact, I would expect the MDM handbook becomes something that just like we open people open the handbook for people to edit our pages and contribute to it.

**John Jeremiah:** I would expect the MDM handbook is exactly that spirit where anybody can contribute to it.

**Brock Walters:** Sure.

**John Jeremiah:** You know, so it's kind of an open source, like project of sorts.

**Brock Walters:** No, I like that idea.

**Brock Walters:** I think there's a lot of potential value there, not just for us, but for.

**John Jeremiah:** Well, and that's, and that was something I thought would be really cool to share with the Mac admins podcast and to invite people to contribute.

**John Jeremiah:** You know, once we get enough content there that there's, there's meat on the bone.

**John Jeremiah:** Yeah.

**John Jeremiah:** Would be the ads on Mac admin podcast would be, Hey, help us contribute to this.

**John Jeremiah:** We're.

**John Jeremiah:** Building this as a resource for all users, not just Macs, it says MDM across the board, and we could contribute across.

**Brock Walters:** It's a way to help the community.

**Brock Walters:** Yeah.

**Brock Walters:** I mean, I don't mean to drag this out, but I tend to haunt the Bash channel and the scripting channel in Mac Admin Slack, right?

**Brock Walters:** And if I had a nickel for every time someone is asked about, how do I do user context in a script, right?

**Brock Walters:** I'd have a lot of nickels.

**Brock Walters:** The answer is always the same.

**Brock Walters:** It's always a reference to the same article.

**Brock Walters:** It's just that there's 100 people who have never thought about it and never asked the question before.

**Brock Walters:** So, and there's never really been a good forum for like, it's, I mean, it's not, it's, it would be this handbook thing, I think would be bigger than a FAQ, but effectively it could perform the function of an FAQ for lots of things that get asked over and over again.

**John Jeremiah:** So, yeah, no, that's exactly the.

**John Jeremiah:** That's exactly the spirit of what...

**John Jeremiah:** Take a look at the issue.

**John Jeremiah:** mean, the issue, there's a lot went into it.

**John Jeremiah:** I put some thought into how could we structure and how could we set this up so that way it could take on a bit of a life of its own without it.

**John Jeremiah:** But it's part of Fleet.

**John Jeremiah:** It's part of us.

**John Jeremiah:** It's ours.

**John Jeremiah:** But it's something, it would be larger and would help us.

**John Jeremiah:** It could have a huge impact on SEO too.

**John Jeremiah:** But we got to go.

**John Jeremiah:** got an all-handsman you got to go too.

**John Jeremiah:** Thank you, Erik.

**Erik O'Brien:** Cheers.

**Erik O'Brien:** Bye-bye.

**Erik O'Brien:** Absolutely.

**Erik O'Brien:** See you guys.

**Erik O'Brien:** Bye-bye.
