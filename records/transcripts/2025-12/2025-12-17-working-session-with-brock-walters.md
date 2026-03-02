# Working Session with Brock Walters

<metadata>
date: 2025-12-17
time: 15:30 UTC
duration: 20 minutes
organizer: erik@growthx.ai
participants: Erik O'Brien, Sulaman Ahmed, Brock Walters
fathom_recording_id: 109415783
fathom_url: https://fathom.video/calls/509836541
share_url: https://fathom.video/share/1Ucp55ykFTpWaXTVRF-y_GPZ1gBsjPkV
source: fathom
enriched_on: 2026-03-02 00:00 UTC
</metadata>

---

## Summary

Brock walked Sulaman and Erik through the new fork-based GitHub workflow for submitting article contributions to the Fleet repository. Instead of the old method of posting Markdown in GitHub issues, external contributors now create a personal fork, add their article file to the articles/ folder, and submit a Pull Request to the main repository—this enables Git diffs for easier review. Brock will investigate granting Sulaman limited organization access to add marketing labels and manage project board placement, but for now Brock, Irina, and John will handle label assignment.

---

## Context

Sulaman Ahmed is an external contributor working on Fleet documentation articles. The team previously used GitHub issues to propose new content, but the process was inefficient because it lacked Git diffs, making it impossible to track changes between versions and complicating editorial review. Erik and Brock met with Sulaman to teach him the new external contributor workflow, which aligns with how Fleet's open-source community submits contributions. This is a shift from internal-focused processes to a more scalable, community-standard approach.

---

## Relevance

- **To GrowthX Delivery:** New client content delivery workflow via GitHub PRs instead of manual issue posting. Demonstrates adoption of open-source contribution standards for collaborative content projects. Git diffs now enable detailed review and iteration tracking.
- **To Fleet Partnership:** Streamlined article submission process for external partners. Establishes clear, repeatable workflow for Sulaman's ongoing article contributions. Potential future automation via scoped org access if GitHub permissions allow.
- **To Operational Efficiency:** Reduces manual work for Brock, Irina, and John (review queue management, label assignment, board placement). Pending resolution: investigation of scoped org permissions for Sulaman to automate project board assignment.

---

## Overview

- **New Workflow:** Use a GitHub fork to submit Pull Requests (PRs) directly to the main `FleetDM` repository. This replaces the old issue-based method.
- **Why:** The fork-based PR workflow is the standard for external contributors and enables Git diffs, which are essential for efficient content review.
- **Critical Step:** CC Brock, Irina, and John in every PR description to ensure they receive immediate notifications for review.
- **Next Step:** Sulaman will submit the first article via PR for review. Brock will investigate granting Sulaman limited org access to add marketing labels, which automates board placement.

---

## Key Topics

### Problem: Old Workflow Inefficient

  - The previous method of pasting Markdown into GitHub issues was inefficient.
  - **Key Limitation:** It lacked Git diffs, making it impossible to track changes between content versions, which complicated the review process.

### Solution: Fork-Based Pull Request Workflow

  - This new workflow is the standard for external contributors and is designed to bypass branch protection rules that would otherwise block direct commits.
  - **Process:**
    1.  **Fork:** Create a personal fork of the `FleetDM` repository. This is a one-time setup.
    2.  **Create File:** In the fork, navigate to the `articles/` folder and click "Add file."
    3.  **Name File:** Use the convention `article-title-with-dashes.md`.
    4.  **Add Content:** Paste the article's Markdown text into the file.
    5.  **Commit & Create PR:** Commit the change. GitHub will automatically configure the PR to target the main `FleetDM` repository.
    6.  **Add Notifications:** In the PR description, CC Brock, Irina, and John to trigger notifications.

### Optional: Automating Project Board Placement

  - **Goal:** Automatically add new PRs to the "Help Marketing" project board for team visibility and assignment.
  - **Mechanism:** This requires adding the "help marketing" label to the PR.
  - **Access Issue:** Adding labels requires organization-level permissions, which Sulaman currently lacks.
  - **Proposed Solution:** Brock will investigate granting Sulaman limited access to the `fleet` organization, scoped only to the marketing project.
  - **Interim Process:** Until access is granted, Brock, Irina, or John will manually add the labels and move PRs to the board.

---

## Action Items

**Brock Walters**
- Ask Sam about adding Sulaman to Fleet org with limited Marketing Project access; if approved, add him

**Sulaman Ahmed**
- Convert 1 article issue to PR in FleetDM/articles; CC Brock, Irina, John; then notify Erik to review

---

## Transcript
**Sulaman Ahmed:** Hey, greetings, Erik, how are you?

**Erik O'Brien:** Hey, Sulaman, doing great.

**Sulaman Ahmed:** How are you doing?

**Sulaman Ahmed:** Doing good so far.

**Sulaman Ahmed:** Good.

**Erik O'Brien:** Hopefully this will be less than an hour.

**Erik O'Brien:** I'm hoping about 30 minutes.

**Sulaman Ahmed:** Yes, this should be pretty quick.

**Sulaman Ahmed:** We just need to take access from them.

**Erik O'Brien:** That's it.

**Erik O'Brien:** Yeah, I think he's got a new process for us to do.

**Erik O'Brien:** So he's just going to walk us through what that new process is.

**Brock Walters:** Hi, guys.

**Brock Walters:** Sorry to keep you waiting.

**Erik O'Brien:** Hey, no worries.

**Brock Walters:** Hi, Sulaman.

**Brock Walters:** Have we been on a call?

**Brock Walters:** Have you been on a call with me before?

**Erik O'Brien:** Nope.

**Brock Walters:** Okay.

**Brock Walters:** I know your time schedule is way off of ours, so I appreciate you joining.

**Brock Walters:** So let's get into it.

**Brock Walters:** Let's see if I can remember how to do it.

**Brock Walters:** Oh, I closed my – yes, you can record.

**Brock Walters:** Okay.

**Brock Walters:** So I had an incognito window to do this, but then Chrome updated – Chrome updates every five minutes.

**Brock Walters:** Okay.

**Brock Walters:** So here's what I'm going to do.

**Brock Walters:** I'm going to log into GitHub with an account that is my account but has nothing to do with fleet.

**Brock Walters:** This is like slightly embarrassing.

**Brock Walters:** This is my Batman persona on the Internet.

**Brock Walters:** You know, like that XKCD cartoon where it's like someone is wrong on the Internet.

**Brock Walters:** This is the account that I use when I am performing in that role, which I try not to do.

**Brock Walters:** But, you know, you have to do it occasionally.

**Erik O'Brien:** So don't tell anyone.

**Erik O'Brien:** We'll keep it a secret.

**Brock Walters:** You guys have now been in the Batcave.

**Brock Walters:** Okay.

**Brock Walters:** So let me share.

**Brock Walters:** Can you see my screen?

**Sulaman Ahmed:** Yep.

**Sulaman Ahmed:** Yep.

**Brock Walters:** Okay.

**Brock Walters:** Excellent.

**Brock Walters:** So if I log in here, hopefully I will remember the password I used because I just did this last night.

**Brock Walters:** Okay, I don't have, so number one, this account is not associated with the Fleet.org.

**Brock Walters:** If I go and look at my actual GitHub account that I use, this is me.

**Brock Walters:** You can see all the repositories I have, and you can also see that I'm associated to the Fleet.org.

**Brock Walters:** Okay, what this means is that I have access beyond the branch protections.

**Brock Walters:** And this is the thing that I was kind of struggling to figure out.

**Brock Walters:** I assumed that you could make a branch, so I apologize for giving you one set of directions and now giving you another.

**Brock Walters:** What I'm going to walk you through is the way that we would tell a customer to contribute to the product.

**Brock Walters:** And customers do this all the time.

**Brock Walters:** It's an open source project.

**Brock Walters:** So we take customer contributions, this is the way they make them, okay?

**Brock Walters:** Okay.

**Brock Walters:** So this is the account that has nothing to do with Fleet.

**Brock Walters:** So if I go in here and I search for FleetDM, it probably is pulling up Fleet because I've visited it before with this account.

**Brock Walters:** This is what you would want to do first, just go to the Fleet Repo.

**Brock Walters:** Okay, and then some of the steps in the video still apply, right, because it's effectively the same concept.

**Brock Walters:** It's just that what we're doing is using a fork instead of using the actual Fleet Repo.

**Brock Walters:** The trick to this is that by using the fork, you are actually submitting the pull request to main, and you'll see that in a minute.

**Brock Walters:** The difference between, and you may know this, so forgive me for being pedantic, but the difference between a fork and a clone is that a clone is like a copy of the repository.

**Brock Walters:** That you're using for your own purposes, like I have a local copy, I have a cloud copy, and I'm making sure that those two are in sync, but really they're identical and they're in the repository that you're working in.

**Brock Walters:** A fork is a completely separate copy of the repository that operates separately, so when you make changes to the fork, it doesn't make changes to the thing that it's been forked from, unless you do this, which is using your fork to submit a pull request back to the actual main branch that's the real repository.

**Brock Walters:** I hope that makes sense.

**Brock Walters:** I'm saying it all just in case.

**Sulaman Ahmed:** Yep, that's clear.

**Brock Walters:** Okay.

**Brock Walters:** Okay, so if I go to this articles folder, and this is, I think we've decided that this is where they're going to live, to make a pull request, what you would do here is you create a new file.

**Brock Walters:** Now, you're going to see the very first time you do that, it's going to tell you to fork the repository.

**Brock Walters:** You want to click that.

**Brock Walters:** Okay, now whatever text you have, and this could be, you know, you have the articles that you've already created as issues in another tab, or you're writing them in here, it doesn't really matter where you're generating that text, as long as you can get to this point.

**Brock Walters:** And as I've said in the video, you're going to want to call these like article.md.

**Brock Walters:** The thing that I failed to mention is that if your article title has multiple words in it, I think the convention is to use dashes.

**Brock Walters:** So it would be like your great MDM article.md.

**Brock Walters:** Okay.

**Brock Walters:** And then you would paste some stuff here.

**Brock Walters:** Okay.

**Brock Walters:** And when I put a title in, number one, it's telling me you're making changes that I don't have right access to.

**Brock Walters:** Submitting a change will write it to a new branch in your fork.

**Brock Walters:** So you can send a pull request.

**Brock Walters:** That's exactly

**Brock Walters:** That's exactly what we want.

**Brock Walters:** So, I'm to commit this change.

**Brock Walters:** Okay, and this is the key to the whole thing right here.

**Brock Walters:** So, what this is saying is, okay, patch one, head repository is my fork, but the base is actually fleet.

**Brock Walters:** So, when I create this pull request, it's going to go to the main repo.

**Brock Walters:** It's not going to be isolated to just the fork.

**Brock Walters:** Okay?

**Brock Walters:** And so, if I do that, now I have this, I don't know why I added that twice.

**Brock Walters:** Maybe it adds the MD on there automatically.

**Brock Walters:** This is all boilerplate for an actual pull request for code.

**Brock Walters:** You could delete all that.

**Brock Walters:** You could put a summary of the article here if you wanted to.

**Brock Walters:** You could put a date.

**Brock Walters:** You don't have to put anything here, but I would maybe suggest at least putting something like the title, okay?

**Brock Walters:** But you could also put a summary and a date.

**Brock Walters:** Okay, create pull request.

**Brock Walters:** All right, now you'll notice that this pull request is 37405, okay?

**Brock Walters:** So if I go back to the actual fleet repository and I go to fleet, and I go to pull requests, there it is.

**Brock Walters:** So again, just to make the point perfectly clear, even though you're creating that in a fork, that pull request goes directly to the main repository, as long as you don't touch any of that stuff.

**Brock Walters:** Because the workflow is set up to do exactly this.

**Brock Walters:** And now this is ready to be assigned.

**Brock Walters:** And I think, well, it doesn't really matter if you can't go beyond this point, because what I'm going to be doing is looking for these.

**Brock Walters:** And maybe what you could always do in this comment would be, let's make this, whatever else you put in this comment block, make sure that you CC me.

**Brock Walters:** And, Irina, and John, okay, but that would be the one rule, is because that way we'll be notified for every single one of these that you submit.

**Brock Walters:** Okay, and then, cool, so that's in there, and just to show you, and you can try to do this, I just don't think you're going to be able to do it, because I think, again, this is a thing where you'd have to have privileges at the organization level.

**Brock Walters:** In GitHub, projects exist at the organization level, not at the repository level.

**Brock Walters:** So this is the fleet repo.

**Brock Walters:** This is the fleet org where all of the fleet repos live.

**Brock Walters:** If I go to projects, you will see that there is a help marketing project.

**Brock Walters:** Okay?

**Brock Walters:** What should happen, and we may have to do this, is that once we are notified that you've submitted one of these things, but you can try doing some of this stuff.

**Brock Walters:** I just don't know what access you'll have to do it.

**Brock Walters:** If I go to this pull request, and I add a label for marketing, the help marketing label, another thing I can do is add it to the marketing project.

**Brock Walters:** And what...

**Brock Walters:** Doing these two things will cause this to show up on the marketing board.

**Brock Walters:** What we're going to do from there, but the thing is, we may never actually have these hit this.

**Brock Walters:** I'm just showing you, this is how we segregate issues from one team to another.

**Brock Walters:** So what I will suggest to John is that because these things are going to be crowdsourced with the customer success team and the solutions consulting team, they also have their own project boards.

**Brock Walters:** So we could just start distributing these pull requests in a kind of round-robin way to those boards, rather than having them hit the help marketing board.

**Brock Walters:** But it also might be a task for Irina to go, okay, every one of these pull requests hits the help marketing board, and she's going to divvy them up between whoever's going to edit them.

**Brock Walters:** But the whole workflow that I just showed you, that's it.

**Brock Walters:** So you need the account, you need to go to...

**Brock Walters:** To the fleet repository, you need to go to the articles folder.

**Brock Walters:** Click add file.

**Brock Walters:** When you do that the first time, it's going to ask you to fork the repository.

**Brock Walters:** I think you can continue to use that fork to do this in an ongoing way.

**Brock Walters:** You shouldn't have to do that every time.

**Brock Walters:** And then, once you've created, pasted in the text for the article, you'll have a button that says create pull request.

**Brock Walters:** And as long as you don't touch any of those workflow buttons for the branching, that pull request will actually show up in the main repository for us to further action.

**Brock Walters:** Cool?

**Sulaman Ahmed:** Got it.

**Sulaman Ahmed:** That seems pretty clear.

**Brock Walters:** Just one question.

**Sulaman Ahmed:** If I have the capability to add a tag, obviously, I will see if I have the permissions for that or not.

**Sulaman Ahmed:** But if I have, shall I place in these marketing tags, the project and the labels?

**Sulaman Ahmed:** Or is that something that Irene would do?

**Brock Walters:** I would just say try it.

**Brock Walters:** What I think is that...

**Brock Walters:** The more that I'm talking about it out loud is I think you would have to have permissions at the org level.

**Brock Walters:** So we could probably add you to the organization and let you do that.

**Brock Walters:** I don't know if we can add you to the organization in a limited capacity, like let's say just for one project.

**Brock Walters:** I think if we do that, that would be the best way is to say that, yes, Sulaman is a member of the fleet organization, but he only has access to the marketing project.

**Brock Walters:** And the reason for that is to allow him to add the help marketing label to his pull request so that Irina can spread the love.

**Sulaman Ahmed:** Maybe if you can just add me as a contributor, just for that project, that will limit my access for one scope instead of the organization.

**Brock Walters:** Yep.

**Brock Walters:** I will look into that.

**Brock Walters:** For now, let's just assume that me or John or Irina will put things on boards, but I will ask Sam if that's possible, and then that would be great if you could do that step as well.

**Sulaman Ahmed:** All right.

**Sulaman Ahmed:** Perfect.

**Sulaman Ahmed:** That's pretty clear for me now.

**Sulaman Ahmed:** Actually, the thing I was missing was before I had in mind for the cloning, if I do it like locally, I would clone the whole project and that was quite big.

**Sulaman Ahmed:** And now I understand I just don't need to do that.

**Sulaman Ahmed:** Whole thing can be done with inside the GitHub UI and a direct fork would be sufficient enough for this one.

**Sulaman Ahmed:** So I was confused with the GitHub UI.

**Brock Walters:** It's super confusing.

**Brock Walters:** It's super confusing, especially like, you know, I know enough about GitLab and GitHub because I used them when I worked.

**Brock Walters:** Apple and but I'm certainly no expert.

**Brock Walters:** And it's very confusing to the difference between a fork and a clone is is counterintuitive because the clone seems like it would be the thing that you would want, but it isn't because in order to use a clone, you have to have the same permissions to both the local folder and the GitHub repository on a fork.

**Brock Walters:** You basically own the whole thing because because Because...

**Brock Walters:** Whatever changes you make to the fork are isolated, unless you make a pull request back to me.

**Sulaman Ahmed:** Got it.

**Sulaman Ahmed:** Got it.

**Sulaman Ahmed:** Yes, you're 100% right.

**Sulaman Ahmed:** That is the correct explanation.

**Sulaman Ahmed:** Perfect.

**Sulaman Ahmed:** I think we are good to start that, if that's the case.

**Sulaman Ahmed:** However, I do have one question, Erik.

**Sulaman Ahmed:** Sure.

**Sulaman Ahmed:** Since we are changing the process, previously what I used to do was there was a generate ticket process.

**Sulaman Ahmed:** I directly use that as editor, like paste in the MD format, see the preview from there, see if image looks correct.

**Sulaman Ahmed:** Does that part would come on a local system now?

**Sulaman Ahmed:** Like I will see the preview of MD on a local system, or would we just create them as issues?

**Sulaman Ahmed:** Would we still create them as issues?

**Sulaman Ahmed:** I think we are dropping that approach, right?

**Brock Walters:** Yeah, you don't need to make them as issues.

**Brock Walters:** The only reason I was mentioning the issues is because you might have to convert the ones you've already created as issues.

**Brock Walters:** And the way to do that would just be to go to your issue, click the edit button, copy the markdown, and then paste that into a new pull request.

**Sulaman Ahmed:** Got it.

**Sulaman Ahmed:** And now, since I already have a structure for the article from the issues, I can, going forward, can just replicate them in my local system and just copy the direct MD from local to the GitHub UI.

**Brock Walters:** Got it.

**Brock Walters:** And there's one other thing I guess I want to mention about this, which is part of the reason that John wanted to go in this direction, is that, and he's, frankly, he's right about this, is that the, when you have just the markdown in a comment block, you don't get, doesn't give you any options for, you don't get any of the get diff capability.

**Brock Walters:** But when we're submitting these as pull requests, what you will get is the diff between the original content and whatever changes are made.

**Brock Walters:** And that will help, I think, us and you guys going forward to make the editing process better.

**Sulaman Ahmed:** A hundred percent, you are right.

**Sulaman Ahmed:** Perfect.

**Sulaman Ahmed:** I think I'm super clear with the process now, and hopefully.

**Sulaman Ahmed:** By today, I will publish some articles, and the first article would be the one that would be decisive, and going forward, I think this should be a smooth process.

**Brock Walters:** Okay, awesome.

**Brock Walters:** And if you don't want to go back, I can convert the ones you already have as issues if you don't get to it.

**Sulaman Ahmed:** No issues at all.

**Sulaman Ahmed:** I will actually start from there.

**Sulaman Ahmed:** I have already the links of those issues, so I'll start from there.

**Sulaman Ahmed:** I'll inform Erik, after the first article is done, maybe you can review and see if the process was done according to requirement, and then if that's good enough, I will do that same thing with the remaining articles.

**Brock Walters:** Cool.

**Brock Walters:** I mean, the only criteria we have is if the pull request shows up in main for a new article, you've done it correctly.

**Sulaman Ahmed:** 100% right.

**Sulaman Ahmed:** Got it.

**Brock Walters:** Awesome.

**Brock Walters:** Thanks, guys.

**Brock Walters:** I think that's it.

**Sulaman Ahmed:** Wonderful.

**Sulaman Ahmed:** I think we're good enough.

**Erik O'Brien:** All right.

**Sulaman Ahmed:** Appreciate it, Brock.

**Sulaman Ahmed:** Thanks, guys.

**Sulaman Ahmed:** Thank you so much, Brock.

**Sulaman Ahmed:** Have a nice day.

**Sulaman Ahmed:** Have a nice day,
