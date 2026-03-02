# Fleet <> GrowthX - Weekly Sync

<metadata>
date: 2025-11-26
time: 19:59 UTC
duration: 38 minutes
organizer: team@growthxlabs.com
participants: Aida Knezevic (GrowthX), Erik O'Brien (GrowthX), Brock Walters (FleetDM), Irena Reedy (FleetDM), John Jeremiah (FleetDM)
fathom_recording_id: 104663296
fathom_url: https://fathom.video/calls/486302107
share_url: https://fathom.video/share/9ve7wzxchp4bKszEsfzzzYsD7tL6sHzd
source: fathom
enriched_on: 2026-03-02 18:45 UTC
</metadata>

---

## Summary

GrowthX and Fleet aligned on a GitHub Issues-based content review process where Fleet's CS and SA teams will volunteer to review articles for factual accuracy and become published authors, replacing the unscalable Airtable/Google Docs workflow. John Jeremiah flagged a critical technical issue: the site's client-side rendering prevents LLMs from reading content, directly blocking the project's goal of influencing AI-driven search. Fleet confirmed proceeding to Phase 2 (12-month contract) pending signed agreement next week, while GrowthX will deliver the full technical audit and propose an LLMS.txt file as a temporary workaround for the CSR issue.

---

## Context

Fleet is a B2B device management platform working with GrowthX on a content strategy to influence AI-driven search and build authority in the endpoint security space. The project started as an 8-week strategy sprint (ending this week, November 26) with a decision point on proceeding to a 12-month Phase 2 engagement. GrowthX is producing 4-5 articles per week while Fleet reviews them for factual accuracy before publication. The relationship is active and collaborative, with clear alignment on goals but emerging technical blockers that may require architectural decisions about the website itself.

---

## Relevance

**To GrowthX Delivery:**
- New content review workflow using GitHub Issues as the single source of truth, replacing Airtable/Google Docs hybrid. Scaling review to 10+ people requires process discipline.
- Content pace target is 4-5 articles/week; review scope limited to factual accuracy and SEO preservation to prevent scope creep and missed deadlines.
- GrowthX must load all 9 pending articles into GitHub issues by next week to launch the new process at scale.

**To CheckThat & AEO Strategy:**
- Critical discovery: Fleet's website is not readable by LLMs (ChatGPT, Claude, Perplexity) due to client-side rendering. This directly blocks the project's core goal of influencing AI-driven search and content training.
- GrowthX's technical audit (due today/early next week) is expected to confirm CSR is pervasive across the site, not just article pages.
- LLMS.txt file proposed as temporary band-aid to give LLMs a static markdown summary of content until broader site architecture is resolved.

**To GrowthX Business Development:**
- Phase 2 decision point due next week; Fleet is signaling strong intent to proceed ("we're going to continue to phase 2") but needs signed contract.
- Erik will send current contract by end of week. John Jeremiah (key stakeholder on Fleet side) will review and return signed by next week.
- Account health is strong; internal alignment at Fleet on value (Brock and John aligned on quality-first approach), no renewal risk visible.

---

## Overview

- **New Content Review Process:** Fleet is adopting a scalable GitHub Issues workflow where internal teams (CS, SAs) volunteer to review articles for factual accuracy, becoming the published authors to ensure quality.
- **Critical Website Issue:** The site's client-side rendering (CSR) makes content unreadable to LLMs (e.g., ChatGPT), blocking the project's core goal of influencing AI-driven search.
- **Phase 2 Decision:** Fleet must decide by next week whether to proceed from the 8-week strategy sprint to a 12-month contract.
- **Interim Fix:** GrowthX proposed an `LLMS.txt` file as a temporary workaround for the CSR issue, providing a static content summary for LLMs.

---

## Key Topics

### Website Technical Audit

  - GrowthX's technical audit, due today or early next week, is expected to confirm a major issue: the site's client-side rendering (CSR).
  - **Impact:** CSR makes content unreadable to LLMs (e.g., ChatGPT, Claude), which cannot execute JavaScript. This blocks the project's goal of influencing AI-driven search results.
  - **Significance:** John Jeremiah stated this is a "much, much, much bigger problem" that could halt content production until resolved.
  - **Proposed Workaround:** GrowthX suggested an `LLMS.txt` file—a static Markdown summary at the root domain—as a temporary fix.

### New Content Review Process

  - **Problem:** The current Airtable/Google Docs workflow is unscalable for the target pace of 4–5 articles/week.
  - **Solution:** A new GitHub Issues workflow will be implemented.
      - **Reviewers:** Volunteers from Customer Success (CS) & Solution Architects (SAs).
      - **Incentive:** Reviewers become the article's published author, increasing investment in quality.
      - **Scope:** Review is limited to factual accuracy to preserve SEO keyword impact.
  - **Process Flow:**
    1.  GrowthX creates a GitHub Issue with the draft.
    2.  A Fleet reviewer claims the issue, makes edits directly, and approves.
    3.  GrowthX publishes the approved article.
  - **Future Automation:** Brock Walters will investigate automating new article creation via Pull Requests, mirroring the existing "Suggest an Edit" button.

### Project Phase 2 Decision

  - The 8-week strategy sprint is ending, requiring a decision on the 12-month Phase 2 contract by next week.
  - Erik O'Brien will send the current contract to John Jeremiah for review.

---

## Action Items

**John Jeremiah (FleetDM)**
- Align w/ CS + SA managers on reviewer pool; then set up GitHub board + statuses
- Test Fleet blog/article pages w/ JS disabled
- Review GrowthX contract and return signed by next week for Phase 2 decision

**Aida Knezevic (GrowthX)**
- Draft reviewer checklist; share w/ John, Brock, Irena
- Move 5 Airtable drafts to GitHub issues; move all 9 pending articles into GitHub for new process launch
- Create Airtable view for ready-to-publish articles

**Brock Walters (FleetDM)**
- Align w/ CS + SA managers on reviewer pool (joint action with John)
- Finalize approval status on 4 existing articles in marketing board (clarify approved vs. pending)
- Consult George/Luke/Alan re: PR template + GitHub Actions for automating new article creation via Pull Requests
- Document GitHub Issues-based review process workflow and interface specs between GrowthX and Fleet teams

**Erik O'Brien (GrowthX)**
- Email John the current GrowthX contract for Phase 2 review
- Deliver full technical website audit report (expected today or early next week)
- Propose LLMS.txt file implementation as temporary workaround for client-side rendering issue

---

## Transcript
**Erik O'Brien:** This meeting is being recorded.

**John Jeremiah | FleetDM Contributor:** Eric, how are you?

**Erik O'Brien:** Doing all right.

**Erik O'Brien:** How's your week been?

**John Jeremiah | FleetDM Contributor:** Sure.

**John Jeremiah | FleetDM Contributor:** You know, look, tomorrow's a good break.

**Erik O'Brien:** Yeah, looking forward to it.

**John Jeremiah | FleetDM Contributor:** I'll probably take Friday.

**John Jeremiah | FleetDM Contributor:** I don't know if I'm going to work with someone Friday, but it'll be a quiet day.

**Erik O'Brien:** Told everyone I'm not working so I can get actual work done.

**John Jeremiah | FleetDM Contributor:** Yeah, that's the way a lot of people play it.

**John Jeremiah | FleetDM Contributor:** But yeah, I don't have any big plans.

**John Jeremiah | FleetDM Contributor:** We'll see.

**Irena Reedy | Content Specialist:** Hello!

**Erik O'Brien:** Hey there.

**Irena Reedy | Content Specialist:** How's it going?

**Erik O'Brien:** Good, how are you doing?

**Irena Reedy | Content Specialist:** I'm well, thank you.

**Aida Knezevic:** Hi.

**Irena Reedy | Content Specialist:** Hi.

**Irena Reedy | Content Specialist:** Hi.

**Aida Knezevic:** All right, I think we have everybody here, right?

**Erik O'Brien:** Yeah, we do.

**Brock Walters | Manager, Training & Enablement:** Let me fix my audio.

**Aida Knezevic:** Give me one second.

**Brock Walters | Manager, Training & Enablement:** All right.

**Brock Walters | Manager, Training & Enablement:** Hopefully that's better.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Mm-hmm.

**Aida Knezevic:** Okay, cool.

**Aida Knezevic:** All right.

**Aida Knezevic:** So I have added everyone to the agenda, so you should get it in your inbox from Notion.

**Aida Knezevic:** So to do a couple of quick content updates.

**Aida Knezevic:** On our end, so we shared three new blogs for your review, which brings the total number of articles that are currently being reviewed by Fleet to five, and there are four that are still, that are ready to publish, so we wanted to just see if there was anything that we can do to kind of help with the publishing.

**Brock Walters | Manager, Training & Enablement:** John, do you want to kind of speak to that, on what our plan is going to be going forward, or I can't repeat you?

**John Jeremiah | FleetDM Contributor:** No, I mean, I'll talk to it.

**John Jeremiah | FleetDM Contributor:** So, you know, recognizing that we're going to be publishing at a pace of probably four or five articles a week, you we've got to come up with a model that's scalable for us to review and to look at articles and make sure they're factually correct and aligned with what, you know, with what we think is, you know, you know, the right things to be saying in the market.

**John Jeremiah | FleetDM Contributor:** So what we're going to do is we're having conversations with a...

**John Jeremiah | FleetDM Contributor:** A team of, with two different teams, one on the customer success side of the house, another one on with Solution Architects.

**John Jeremiah | FleetDM Contributor:** And the idea will be is that we will create a GitHub board with, where we'll put each of the new articles as they come up.

**John Jeremiah | FleetDM Contributor:** We'll solicit volunteers from these two groups to do the review and to provide feedback and then move it forward to a status where it's approved for publishing.

**John Jeremiah | FleetDM Contributor:** So this will give us scalability and the ability to create multiple authors.

**John Jeremiah | FleetDM Contributor:** And then whoever the reviewer is will be the author and will be the byline.

**John Jeremiah | FleetDM Contributor:** So we'll solve a couple of problems by doing it this way.

**John Jeremiah | FleetDM Contributor:** But we still have to finalize, get final agreement alignment internally with the two different managers.

**John Jeremiah | FleetDM Contributor:** But I don't think it's going to be a heavy lift.

**John Jeremiah | FleetDM Contributor:** And my expectation is that 90% of the...

**John Jeremiah | FleetDM Contributor:** Articles are going to require little to no revision.

**John Jeremiah | FleetDM Contributor:** If that's wrong, if it turns out that the articles require a lot of revision, then we may have to revisit how we do this.

**Brock Walters | Manager, Training & Enablement:** And just to be piggyback on that, the difference in strategy, from my perspective, is that before John and Ashish joined, we'd started this project.

**Brock Walters | Manager, Training & Enablement:** The idea of me having to actually read every blog post for content, which I'm totally willing to do, and then half date having to edit them, it was daunting.

**Brock Walters | Manager, Training & Enablement:** And so my plan was going to be to make sure that we had the seating right, make sure that we had the robot pointing in the right direction.

**Brock Walters | Manager, Training & Enablement:** But I actually am totally aligned with John's vision for this.

**Brock Walters | Manager, Training & Enablement:** And I think at least to start, we have to have a human person that's looking at every one of these and being like, yes.

**Brock Walters | Manager, Training & Enablement:** And I know that that might slow our trajectory down a

**Brock Walters | Manager, Training & Enablement:** But I think everyone, at least from the fleet side, is not only concerned about the kind of SEO, whatever AI searching advantages we're going to get from this, but also making sure that we're actually creating something that is useful and is high quality.

**Brock Walters | Manager, Training & Enablement:** And I'm not saying that it wouldn't be, but I, the reason I was maybe seemed less cautious about this before was because I didn't really have a choice.

**Brock Walters | Manager, Training & Enablement:** But, but I think my, I prefer the approach of having humans read all of them and give a rubber stamp on them if they're good.

**Brock Walters | Manager, Training & Enablement:** So I hope that doesn't put a wrench in what you guys are trying to do, but that's kind of what we want to do.

**Aida Knezevic:** Yeah, that's totally fine.

**Aida Knezevic:** I think for the vast majority of the companies that we work with, there are people that...

**Aida Knezevic:** That reading the content before publishing.

**Aida Knezevic:** Typically, takes a good couple of months before teams are like, okay, you can go ahead and publish, and we will take a look after you publish.

**Aida Knezevic:** So that's normal.

**Aida Knezevic:** I was just wondering if you wanted us to kind of provide a list of things or like a checklist for your internal team members so that they know what they're looking for, because different people might be looking at different things.

**Aida Knezevic:** might not have an idea, like, am I editing for style, for structure?

**Aida Knezevic:** Like, so we want to like set the expectation.

**Aida Knezevic:** Yeah.

**John Jeremiah | FleetDM Contributor:** Well, and I think that'll be a conversation we have, and I would love to have, if you guys have something, at least the way I see this, is it, the edit that I'm asking them to do, and if they want to go beyond this, I think they, I don't want to say they can, but they might, but I think the bare minimum, the simple action.

**John Jeremiah | FleetDM Contributor:** Ask is, is this factually correct?

**Brock Walters | Manager, Training & Enablement:** Yes, yes.

**John Jeremiah | FleetDM Contributor:** Is this, what's the word I would use?

**John Jeremiah | FleetDM Contributor:** Is it, yeah, is it something that we're not going to be embarrassed by because of, you know, errors or being misleading perhaps or omissions?

**Brock Walters | Manager, Training & Enablement:** Or just seeming naive, you know.

**John Jeremiah | FleetDM Contributor:** Well, I mean, there's some of these that I think because we need to be writing for basic audiences too, that there's different levels of this we have to write to.

**John Jeremiah | FleetDM Contributor:** But for me at least, it's something that I want to have a safety net in place to prevent us from publishing something that's going to show up on Twitter and where we're being made to look like fools.

**John Jeremiah | FleetDM Contributor:** Or grossly mistaken, you know what I mean?

**John Jeremiah | FleetDM Contributor:** So that's the...

**John Jeremiah | FleetDM Contributor:** The basic, I want someone to look at this, go, yeah, this is fine.

**John Jeremiah | FleetDM Contributor:** And by asking them to be the quote-unquote author next to it, you know, I think it gives them some latitude and some investment in the content.

**John Jeremiah | FleetDM Contributor:** So if they want to offer some suggestions or some improvements, then I think that's great.

**John Jeremiah | FleetDM Contributor:** The only caveat being we just don't want to lose the keyword impact or the impact we expect it to have on SEO and traffic.

**John Jeremiah | FleetDM Contributor:** So we don't want to take an article about a ham and cheese sandwich and turn it into a BLT by piecemeal changing it.

**John Jeremiah | FleetDM Contributor:** Which I've always wanted to do.

**John Jeremiah | FleetDM Contributor:** I wanted to go into a restaurant, order one thing, and then substitute it into something else just for fun.

**Brock Walters | Manager, Training & Enablement:** The classic example, right, is the one that they almost always do in the computer science class.

**Brock Walters | Manager, Training & Enablement:** It's how do you make a peanut butter sandwich?

**Brock Walters | Manager, Training & Enablement:** And it's, there's lots of ways of interpreting.

**Brock Walters | Manager, Training & Enablement:** So instructions, right?

**Brock Walters | Manager, Training & Enablement:** Do you press the peanuts?

**Brock Walters | Manager, Training & Enablement:** Do you buy a jar of peanut butter?

**Brock Walters | Manager, Training & Enablement:** So I'm just and just to be clear about the kind of process that I think we're outlining, I'm still planning on going through all the titles and rejecting them, the ones that I think are that we need to wait.

**Brock Walters | Manager, Training & Enablement:** So I don't think that we would ever even get to a spot potentially where we would have something really silly out there if I'm doing that part of it correctly.

**Brock Walters | Manager, Training & Enablement:** In other words, the pool of articles that we're going to have vetted by this group should already have gone through one layer of vetting where it's like, yeah, I don't know if that topic makes sense for us.

**Brock Walters | Manager, Training & Enablement:** So I'm still planning on doing that exercise.

**Brock Walters | Manager, Training & Enablement:** And then I really do like this idea of John's where it's like we're basically giving people authorship of these articles, which theoretically means they'll do a better job, making sure that it's true and it's good.

**Erik O'Brien:** Yep.

**Erik O'Brien:** And then for this process, is that, are you guys envisioning us sharing the way we've been sharing as like these Google Docs, or do you guys want us to submit via PR and then have the review or?

**Brock Walters | Manager, Training & Enablement:** I think that that makes the most sense for us.

**Brock Walters | Manager, Training & Enablement:** There was some question about like, if we just have a random PR, there's not necessarily going to be a specific person that's getting assigned to it.

**Brock Walters | Manager, Training & Enablement:** So how would like notifications work?

**Brock Walters | Manager, Training & Enablement:** But, but I guess my thought was that we would make everybody aware that there was a board in GitHub, where these things were stacking up, you know, new, new issues or whatever, and then you can just go into that bucket and pull however many of them you're interested in doing.

**Brock Walters | Manager, Training & Enablement:** So, so, I think the PR thing, or some kind of GitHub issue, regardless if it's an official PR or not, makes the most sense.

**John Jeremiah | FleetDM Contributor:** I mean, the way I saw it in the marketing board right now, we've got four articles listed, I think, four or five of them.

**Aida Knezevic:** There are four that have been staged.

**John Jeremiah | FleetDM Contributor:** Yeah, I mean, I was thinking we would just use that model and we would just create a board for, we would create a board and have those then be routed through that board.

**John Jeremiah | FleetDM Contributor:** So just like we have today, we would, we would use this and assign it to one of the, not necessarily assign it, but one of the authors would, would take it, run with it, and then, then move it.

**Brock Walters | Manager, Training & Enablement:** Yep.

**Erik O'Brien:** Okay, I'm just curious of if we submit the PR and you guys have edits or like feedback.

**Erik O'Brien:** Okay.

**Erik O'Brien:** right.

**Erik O'Brien:** How would that, would you guys push it back to our team to make those edits?

**Brock Walters | Manager, Training & Enablement:** Well, I think that that's a good question.

**Brock Walters | Manager, Training & Enablement:** And we were kind of kicking around the idea of like, okay, if it's edits that, if everybody knows the purpose of these articles and they're not going to like over edit it to kind of destroy the SEO content, right?

**Brock Walters | Manager, Training & Enablement:** Okay, they're editing it up to a point.

**Brock Walters | Manager, Training & Enablement:** I think the thing that John kind of said, and I'm not meaning to speak for him, but it's like, if we're editing beyond that point, that would maybe mean, for some reason, it would have to go back to you guys.

**Brock Walters | Manager, Training & Enablement:** In other words, this isn't just something that is in progress.

**John Jeremiah | FleetDM Contributor:** It was something that's like rejected, that we're not going to publish for whatever reason.

**John Jeremiah | FleetDM Contributor:** And I think these, yeah, and I agree, I agree completely that there's a threshold that we'd want to teach people.

**Brock Walters | Manager, Training & Enablement:** It's as if this requires a significant rewrite.

**John Jeremiah | FleetDM Contributor:** We need to put it into a category and treat it differently because now there's a bigger issue going on.

**John Jeremiah | FleetDM Contributor:** If it's a simple, I'm going to edit some of this style or I want to add some things to it, I think having them add to it would be great.

**John Jeremiah | FleetDM Contributor:** As I see it, why wouldn't we, I mean, today I'm looking at the four that are sitting in our new requests in marketing.

**John Jeremiah | FleetDM Contributor:** I think it's the six benefits of MDM, iPad MDM, what is Apple Business Manager, and then the device enrollment program.

**John Jeremiah | FleetDM Contributor:** These are issues, not pull requests, right?

**Brock Walters | Manager, Training & Enablement:** Yeah, yeah.

**Brock Walters | Manager, Training & Enablement:** And so I...

**John Jeremiah | FleetDM Contributor:** Go ahead, Well, no, I'm just, I wanted to get precise as to whether we would be doing pull requests or just doing these issues.

**John Jeremiah | FleetDM Contributor:** I, I'm open to either if, if, which, whatever the process looks like, but I was imagining it hits this, it hits the board wherever we're going to put

**John Jeremiah | FleetDM Contributor:** And then the authors do their edits here.

**John Jeremiah | FleetDM Contributor:** then it goes back to you guys to actually push in and publish.

**Brock Walters | Manager, Training & Enablement:** Yeah.

**Brock Walters | Manager, Training & Enablement:** What I actually think is, so in the past, I've actually looked in and I started creating a pull request template for articles.

**Brock Walters | Manager, Training & Enablement:** And I kind of got stymied, not because it was hard to create the template or not because that isn't a thing you can do in GitHub, but because the way we have our GitHub Actions set up for pull requests is very focused on the engineering process.

**Brock Walters | Manager, Training & Enablement:** Currently, the way articles are, new articles are generated internally is with an issue, not a pull request.

**Brock Walters | Manager, Training & Enablement:** And that's why.

**Brock Walters | Manager, Training & Enablement:** So, I think maybe in this case, we could probably fix that, but that would probably require someone like Luke or George.

**Brock Walters | Manager, Training & Enablement:** To create a new pathway for us in GitHub, and I don't know if it's worth it.

**John Jeremiah | FleetDM Contributor:** Yeah, I just, for me at least, just to, I think, let's just leave it the way we're doing it with issues, and we'll manage the edit process through issues, and then once it's approved, it can move to the pull request and get published.

**Brock Walters | Manager, Training & Enablement:** Yeah, I think that makes sense.

**John Jeremiah | FleetDM Contributor:** Yeah, I mean, in a perfect world in the future, we would just start with the pull request, but I don't want to, I don't want to upset, I don't want to change this more than we have to right now to get it going.

**Brock Walters | Manager, Training & Enablement:** Yep, and maybe that's something that I can, now that we're actually officially doing stuff like this, maybe that's an action item that I can kind of take to talk to either George or Luke and be like, hey, or even Alan, like, what would it take for there to be a pull request template to create a new article?

**Brock Walters | Manager, Training & Enablement:** So, as opposed to it having to be an issue, and you're kind of doing all these manual steps, having it be a pull request would make it a lot better.

**Brock Walters | Manager, Training & Enablement:** But I think there is some process stuff that we have to figure out.

**Brock Walters | Manager, Training & Enablement:** On our end to make that work.

**John Jeremiah | FleetDM Contributor:** And I think the only problem with it being an issue, it's not really a problem.

**John Jeremiah | FleetDM Contributor:** I'm just trying to think about the mechanics of the air quote author or reviewer making edits or reviewing it.

**John Jeremiah | FleetDM Contributor:** It means they're editing the description, they're editing the body of it.

**Brock Walters | Manager, Training & Enablement:** Well, that is the way we do it now.

**Brock Walters | Manager, Training & Enablement:** mean, effectively, what you're doing is putting the markdown for the article in a comment.

**Brock Walters | Manager, Training & Enablement:** And then you're adding the metadata to that.

**Brock Walters | Manager, Training & Enablement:** And I think Mike Thomas probably is just manually adding those to a, turning that into a markdown file that goes into the static site generator.

**Brock Walters | Manager, Training & Enablement:** That's the part that would be nice to be automated so that he didn't have to do that.

**Brock Walters | Manager, Training & Enablement:** In other words, if you go to one of the existing articles on...

**Brock Walters | Manager, Training & Enablement:** And there's a button there that says, edit this article, that automatically generates a pull request.

**Brock Walters | Manager, Training & Enablement:** And you can start editing the markdown, and that pull request goes directly to Mike Thomas.

**Brock Walters | Manager, Training & Enablement:** If you want to start a new article, you have to create an issue.

**Brock Walters | Manager, Training & Enablement:** And it would be nice if we could just make the new article process exactly like editing an existing article.

**John Jeremiah | FleetDM Contributor:** Yeah, I'm with you.

**John Jeremiah | FleetDM Contributor:** And I guess here, I'm going to share my scene really fast and show you what I'm thinking.

**John Jeremiah | FleetDM Contributor:** So if I take this example, and if I was the, and you can see I edited this recently, but you don't necessarily, although I did an innocuous edit.

**John Jeremiah | FleetDM Contributor:** So what you're saying, Brock, is that when somebody, if we wanted to edit this, right, if we wanted to suggest a change.

**Brock Walters | Manager, Training & Enablement:** I mean, it would probably just be going in and actually just like clicking edit where you actually have this posted, yeah, because anybody can do that and just changing it and then making a comment that said, hey, I updated blah, blah, blah, you know, like, that's literally the way this happens with new articles.

**John Jeremiah | FleetDM Contributor:** So, so in this case, and I'll change this back in a second.

**John Jeremiah | FleetDM Contributor:** Yeah.

**John Jeremiah | FleetDM Contributor:** But the, in this case, you know, I've, I've gone in and added a new sentence or a new line.

**John Jeremiah | FleetDM Contributor:** What's disappointing is we can't see the, the thread here.

**John Jeremiah | FleetDM Contributor:** So that means you have to do two things.

**John Jeremiah | FleetDM Contributor:** Yes, that's correct.

**John Jeremiah | FleetDM Contributor:** If you are, if you are at a pull request, you can edit it.

**John Jeremiah | FleetDM Contributor:** The collaboration is more obvious.

**Brock Walters | Manager, Training & Enablement:** Yeah.

**Brock Walters | Manager, Training & Enablement:** And go ahead, like, um, since you're sharing already, go to fleet.

**Brock Walters | Manager, Training & Enablement:** Fathom.com, just so you can see what I'm talking about, and I know this is probably very inside baseball for the growthx people, sorry, I just want, I kind of want you guys to see it too.

**Brock Walters | Manager, Training & Enablement:** If you go to docs or guides, and just search for CrowdStrike in that search bar.

**Brock Walters | Manager, Training & Enablement:** Yeah.

**Brock Walters | Manager, Training & Enablement:** So you can see that button, says Suggest and Edit.

**Brock Walters | Manager, Training & Enablement:** Mm-hmm.

**Brock Walters | Manager, Training & Enablement:** So click on that.

**John Jeremiah | FleetDM Contributor:** Yep.

**Brock Walters | Manager, Training & Enablement:** Yeah.

**Brock Walters | Manager, Training & Enablement:** That just creates the pull request, and then you can see, this is exactly how the new article process should be.

**John Jeremiah | FleetDM Contributor:** Yep.

**John Jeremiah | FleetDM Contributor:** No, no, I'm very, I'm pretty, pretty, pretty with you.

**Brock Walters | Manager, Training & Enablement:** Totally with Okay.

**Brock Walters | Manager, Training & Enablement:** So, um, I guess I'm going to take on the responsibility of making sure that this.

**Brock Walters | Manager, Training & Enablement:** Okay.

**Brock Walters | Manager, Training & Enablement:** Thank

**Brock Walters | Manager, Training & Enablement:** I didn't realize that we actually had four on the marketing board, and Aida, you're saying there's five total, or is it seven total that you guys are ready to have us look at?

**Aida Knezevic:** Um, so there are five in total that are ready for you to look at, um, I assume that in this new process, we would, like, we would draft the articles, then immediately put them in GitHub, and then you would, like, your team would review them, and then publish, like, there wouldn't be that intermediary step of us tagging you and John and Irina, um, with the Google Docs.

**Brock Walters | Manager, Training & Enablement:** Well, for now, your team is, is Brock, but, but eventually what we're going to be doing is expanding the group of people that are hopefully willing to do that work.

**Brock Walters | Manager, Training & Enablement:** So, for now, I don't think we need to change anything with what you guys are doing.

**Brock Walters | Manager, Training & Enablement:** I just need to know where to find them.

**Brock Walters | Manager, Training & Enablement:** To read them, and I'm assuming that you want our approvals in Airtable somewhere, or is that, how does that work for you guys, at least for the time being?

**Aida Knezevic:** Um, you can, uh, you can leave, um, a comment here, like, approved, and you can tag me and Erik.

**Aida Knezevic:** Like, you left this comment when you approved it for the first time, like, as the blog idea.

**Aida Knezevic:** Right.

**Aida Knezevic:** And then you can, like, leave an additional comment and say, like, good to publish, or needs revisions.

**Brock Walters | Manager, Training & Enablement:** Okay.

**Brock Walters | Manager, Training & Enablement:** And, and the five that are ready are in, how are they grouped in Airtable currently?

**Aida Knezevic:** Are they?

**Aida Knezevic:** Uh, so you can find them, uh, when you open Airtable, if you go to the view called Fleet Reviewing Drafts.

**Aida Knezevic:** Okay, perfect.

**Aida Knezevic:** find them, yeah.

**Aida Knezevic:** And then the ones that are right now in your GitHub.

**Aida Knezevic:** where find them your GitHub.

**Aida Knezevic:** They are in Ready to Publish, so we separated them.

**Brock Walters | Manager, Training & Enablement:** Okay, and from your perspective, what's the difference between the ones that are here and the ones that are in the other place right now?

**Aida Knezevic:** So these four were submitted a couple of weeks back, and I believe you read them, and you said they look good, and we decided to go and put them in GitHub, yeah.

**Brock Walters | Manager, Training & Enablement:** Okay, cool.

**John Jeremiah | FleetDM Contributor:** Yeah.

**John Jeremiah | FleetDM Contributor:** So, hang on, now that confuses me a little bit.

**John Jeremiah | FleetDM Contributor:** Same.

**John Jeremiah | FleetDM Contributor:** from a process perspective, the drafts need to show up in GitHub in an issue.

**John Jeremiah | FleetDM Contributor:** From a flow, so the starting, so this is interesting, right?

**John Jeremiah | FleetDM Contributor:** Because Brock, you've already read these.

**John Jeremiah | FleetDM Contributor:** These five that are in GitHub today, you've already read.

**Brock Walters | Manager, Training & Enablement:** Very, very briefly.

**Brock Walters | Manager, Training & Enablement:** Like, I'm not sure that I've given them the...

**Brock Walters | Manager, Training & Enablement:** Full approval, but I did look at them, yes.

**Brock Walters | Manager, Training & Enablement:** They're tagged ready to publish.

**Brock Walters | Manager, Training & Enablement:** know.

**John Jeremiah | FleetDM Contributor:** But backing up, and this is, I think, trying to make sure I get to the process right here, because at least what I was imagining, and this is where I could be, you know, I probably am wrong on this process, is that when we have an article that's ready for us to review, it would show up.

**John Jeremiah | FleetDM Contributor:** And I'm not providing requirements, I'm describing how I imagine it works, so just to be clear with what I'm about to say.

**John Jeremiah | FleetDM Contributor:** So my thinking was that the draft article would be loaded up in a GitHub issue, that would be the trigger for GitLab, there you go again, for Fleet to execute a review and approval of that article.

**John Jeremiah | FleetDM Contributor:** Airtable GitHub issues, and then once it was done and approved, it would then go on into the publishing process, meaning the reviewer would not be using Airtable.

**Brock Walters | Manager, Training & Enablement:** I mean, that would be awesome.

**Brock Walters | Manager, Training & Enablement:** I'm not trying to dictate a process either.

**Brock Walters | Manager, Training & Enablement:** I think Mike McNeil, a couple weeks back, did have some questions about how are we going to do this, and he said pretty bluntly, you know, we don't use these other tools, we use GitHub and dah, dah, dah, So, I think, yeah, we, like, the way we've done it with these four blogs, it's our standard process with everyone, but if we want to change it to using GitHub issues, so when we are finished with a draft, we load it up in GitHub issues, and then you review it, that's fine, like, so we can change it.

**John Jeremiah | FleetDM Contributor:** Yeah, I mean...

**John Jeremiah | FleetDM Contributor:** And I appreciate you using Airtable to keep track of your process.

**John Jeremiah | FleetDM Contributor:** Totally get it.

**John Jeremiah | FleetDM Contributor:** I respect that.

**John Jeremiah | FleetDM Contributor:** I'm just trying to think about for us to manage the review process in the most natural way for the team, this broader team that we're going to have doing it.

**John Jeremiah | FleetDM Contributor:** If we only had one person doing the reviews, then doing Airtable would make sense.

**John Jeremiah | FleetDM Contributor:** It would be simple.

**John Jeremiah | FleetDM Contributor:** But if we're going to have 10 or 50, many people involved in this because we want to spread the love, then I think doing it via the issue will make more sense.

**John Jeremiah | FleetDM Contributor:** It's also how we're going to know who the author is and how it's approved.

**John Jeremiah | FleetDM Contributor:** And so let's do this for sake of closing on this.

**John Jeremiah | FleetDM Contributor:** Brock and I are going to, and Irena, we're going to have a conversation with the two managers internally.

**John Jeremiah | FleetDM Contributor:** We'll document how we're going to handle review process using GitHub Issues.

**John Jeremiah | FleetDM Contributor:** And then we can come back with y'all and nail down the kind of the interface between what happens before the issue gets created and then what happens after the issue's moved into an appointment.

**John Jeremiah | FleetDM Contributor:** And status or into a rework status.

**John Jeremiah | FleetDM Contributor:** Okay, that works?

**Aida Knezevic:** Okay.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** We will, so for the five that are in this batch, do you also want us to load them into GitHub issues or?

**Aida Knezevic:** Yes, please.

**Aida Knezevic:** Okay.

**John Jeremiah | FleetDM Contributor:** Yeah.

**John Jeremiah | FleetDM Contributor:** Yes, please.

**John Jeremiah | FleetDM Contributor:** And we will use that as a way to queue it up and as a way to start this process.

**John Jeremiah | FleetDM Contributor:** because we're going to define the boards and the status, the board and the statuses to manage this process, and we'll be kicking this off later.

**Brock Walters | Manager, Training & Enablement:** So just so I'm clear, the five that are in client review are going to be moved into the marketing board, and there's already four there.

**Brock Walters | Manager, Training & Enablement:** Is that correct, Ada?

**Aida Knezevic:** Okay.

**John Jeremiah | FleetDM Contributor:** Yes.

**Aida Knezevic:** Correct.

**John Jeremiah | FleetDM Contributor:** And I think the other reality is that the four that are there are pending approval.

**Brock Walters | Manager, Training & Enablement:** We'd probably need to reset those statuses.

**Brock Walters | Manager, Training & Enablement:** Well, I mean, let's just pretend that.

**Brock Walters | Manager, Training & Enablement:** I never said I read them.

**Brock Walters | Manager, Training & Enablement:** I mean, I did.

**Brock Walters | Manager, Training & Enablement:** But let's just, I didn't really like, none of this was happening at that point, right?

**Brock Walters | Manager, Training & Enablement:** So, I think it's good.

**Brock Walters | Manager, Training & Enablement:** Exactly.

**John Jeremiah | FleetDM Contributor:** You validated that it used words in English.

**Brock Walters | Manager, Training & Enablement:** They did use, seemed to have words and letters that I understood some of, yes.

**Brock Walters | Manager, Training & Enablement:** So, cool.

**Brock Walters | Manager, Training & Enablement:** And I will make sure that, just so we can get going, those are either fully approved or not.

**Brock Walters | Manager, Training & Enablement:** And then we will, the next step, what we need to provide for you guys is a solidified process of what we're going to do on our end so that you guys know where to put them and how it's going to look when we approve or not.

**Brock Walters | Manager, Training & Enablement:** Hope that makes sense.

**John Jeremiah | FleetDM Contributor:** And I don't want to make promises or commitment, but I'm pretty convinced we're going to be able to speed this up.

**Brock Walters | Manager, Training & Enablement:** This will become much more efficient as we wrap up.

**Brock Walters | Manager, Training & Enablement:** Totally.

**Brock Walters | Manager, Training & Enablement:** Totally.

**Brock Walters | Manager, Training & Enablement:** Right now, the only reason it's blocked is because John is new.

**Brock Walters | Manager, Training & Enablement:** The project was new to the folks in marketing to start.

**Brock Walters | Manager, Training & Enablement:** It was very new when they came on board.

**Brock Walters | Manager, Training & Enablement:** So apologies for the delay, but I think it's going to be good, and we will definitely make it work like a well-oiled machine once everybody knows how.

**Erik O'Brien:** Okay.

**Aida Knezevic:** Awesome.

**Aida Knezevic:** I'm going to create another view here just so we can see what is ready to publish, but I'll do that later.

**Aida Knezevic:** All right.

**John Jeremiah | FleetDM Contributor:** Yeah.

**John Jeremiah | FleetDM Contributor:** I apologize for slowing you guys down.

**Aida Knezevic:** No worries.

**Aida Knezevic:** I'm happy to, happy to adjust to whatever workflow works for you.

**Aida Knezevic:** Um, Erik, is there anything else that we needed to cover today beyond the publishing?

**Aida Knezevic:** C anytime you can return to Um Um,

**Erik O'Brien:** So we are in week seven, which makes it kind of a, we have our process set up is to opt in or opt out of phase two.

**Erik O'Brien:** So that is just a kind of formal decision we need from the fleet team by next week.

**Erik O'Brien:** From what I heard today, it sounds like we are going to continue to phase two, but just calling that out as a decision point that we need in writing.

**John Jeremiah | FleetDM Contributor:** Okay.

**John Jeremiah | FleetDM Contributor:** Other than that.

**John Jeremiah | FleetDM Contributor:** send a, for just for sake of arguing, can you shoot me the copy of our current contract?

**Erik O'Brien:** Yep.

**John Jeremiah | FleetDM Contributor:** I'll, I mean, Irena, Brock, don't know who owns it, but Mike was the one that initiated it.

**Brock Walters | Manager, Training & Enablement:** Well, was Mike that initiated it, but I think he fully expects to delegate this to you guys.

**Brock Walters | Manager, Training & Enablement:** Yeah.

**Brock Walters | Manager, Training & Enablement:** Um, so, uh, at this point, you know, we, we certainly, I certainly haven't been slow.

**Brock Walters | Manager, Training & Enablement:** Yeah.

**Brock Walters | Manager, Training & Enablement:** Overrolling it to somehow get to that decision point and then decide not to do it.

**Brock Walters | Manager, Training & Enablement:** mean, I think, what does the next phase look like, Erik?

**Brock Walters | Manager, Training & Enablement:** Is there another similar opt-out point, or is this kind of the first, there's like a trial, and then once you're past the trial, you're kind of in it?

**Erik O'Brien:** Yeah, so the initial eight weeks is the strategy sprint, and that's where we kind of have the opt-in, opt-out decision.

**Erik O'Brien:** And then from there, we go to a 12-month contract.

**Erik O'Brien:** So I will send the existing contract over for you guys to look at, and then we can just make sure we've got a decision by next week.

**Brock Walters | Manager, Training & Enablement:** Okay.

**Erik O'Brien:** Other than that, John, I know you were asking about the, I see it, like, technical side of the website review.

**Erik O'Brien:** Our team is supposed to have that done today, like the full technical audit, so I'm hoping to get that to share with you.

**Erik O'Brien:** Let's it.

**Erik O'Brien:** If not, we'll have it for you early next week.

**Erik O'Brien:** The one thing that I was talking about, I believe last week, was the client-side rendering that the site does.

**Erik O'Brien:** So we disabled JavaScript.

**Erik O'Brien:** This is basically what an LLM sees of your site.

**Brock Walters | Manager, Training & Enablement:** Yeah.

**Erik O'Brien:** So that's one of the big issues we, I'm expecting to see, um, in the technical audit.

**John Jeremiah | FleetDM Contributor:** Cool.

**Erik O'Brien:** But we won't have much more details to share once we get the full report.

**John Jeremiah | FleetDM Contributor:** Okay.

**John Jeremiah | FleetDM Contributor:** No, no, that's important because we can do all the work in the world.

**John Jeremiah | FleetDM Contributor:** And if the website, does that, yeah, I'll be interested.

**John Jeremiah | FleetDM Contributor:** I'm going to do that on some of the articles and blog pages and see if that's...

**Erik O'Brien:** It's pervasive across the site.

**Erik O'Brien:** I believe it is.

**Erik O'Brien:** I think I checked.

**Brock Walters | Manager, Training & Enablement:** I mean, it very well could be by design.

**John Jeremiah | FleetDM Contributor:** Yeah, I mean, I know that some things work.

**John Jeremiah | FleetDM Contributor:** I mean, I know that we are being indexed because I got the – we fixed the problem with the handbook not being indexed.

**John Jeremiah | FleetDM Contributor:** now what you can do, custom search against the website and against the handbook.

**John Jeremiah | FleetDM Contributor:** So that's fixed.

**John Jeremiah | FleetDM Contributor:** But, yeah, because if it was all JavaScript, it wouldn't – that wouldn't work either.

**Erik O'Brien:** Yeah, the Googlebot is obviously – they've spent, you millions of dollars to make sure that it can read.

**Erik O'Brien:** Right.

**Erik O'Brien:** And register JavaScript.

**Erik O'Brien:** But the, you know, ChatGPT, Claude, Perplexity, they are still very nascent compared to Google's crawler.

**Erik O'Brien:** And so they just don't have the ability to render JavaScript.

**Brock Walters | Manager, Training & Enablement:** It's really funny to me that that's the case because it seems like the obvious solution to that would be to tell Claude.

**Brock Walters | Manager, Training & Enablement:** To use a Chrome headless browser and then just get everything through that.

**Brock Walters | Manager, Training & Enablement:** And the headless browser would then run the JavaScript to see whatever it needed to see.

**Brock Walters | Manager, Training & Enablement:** But maybe I don't know.

**Brock Walters | Manager, Training & Enablement:** Maybe those people know more than I do.

**Brock Walters | Manager, Training & Enablement:** Seems like a Chrome headless browser would solve the problem in every case like that.

**Erik O'Brien:** Yeah, it seems like we just moved backwards in web technology.

**Brock Walters | Manager, Training & Enablement:** Maybe.

**Erik O'Brien:** It does.

**John Jeremiah | FleetDM Contributor:** All right.

**John Jeremiah | FleetDM Contributor:** But that helps.

**John Jeremiah | FleetDM Contributor:** That's useful.

**John Jeremiah | FleetDM Contributor:** And I think that technical analysis is going to help us a lot to understand where we need to go.

**John Jeremiah | FleetDM Contributor:** And to be quite honest, you know, I kind of would have thought we would have uncovered some of these issues earlier.

**John Jeremiah | FleetDM Contributor:** Because the JavaScript issue of client-side rendering is if it's pervasive like it is, then we have a much, much, much, much, much bigger problem.

**Erik O'Brien:** let's

**Erik O'Brien:** Yeah, because that's, you know, trying to fix the narrative in which LLMs have been trained on the corpus of the internet, and if we're trying to change that with the content we generate, and they're not able to see it, then it's really hard to change that narrative.

**John Jeremiah | FleetDM Contributor:** Yeah, What's the point of generating content if the LLM's not going to be able to read it?

**Erik O'Brien:** Yep.

**John Jeremiah | FleetDM Contributor:** Right.

**John Jeremiah | FleetDM Contributor:** I mean, that does lead to that.

**John Jeremiah | FleetDM Contributor:** I mean, I'll be really blunt.

**John Jeremiah | FleetDM Contributor:** If we are facing a problem where everything we publish on our website is not going to be readable by an LLM, then we probably don't want to proceed.

**John Jeremiah | FleetDM Contributor:** We probably need to hit the brakes and think about how we architect the website or how we solve that problem first before we start producing content.

**John Jeremiah | FleetDM Contributor:** Maybe.

**John Jeremiah | FleetDM Contributor:** I mean, I'm just thinking out loud.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Yeah, I mean, it's still, you guys are definitely being indexed.

**Erik O'Brien:** Like, so it's not an issue with Google.

**Erik O'Brien:** It's just the LLMs themselves.

**Erik O'Brien:** So you'll still be indexed.

**Erik O'Brien:** You'll still register and kind of show up.

**Erik O'Brien:** For SEO purposes, it's just the GEO and AEO, like you say, the IEOs, is definitely basically a blind spot for them to be able to read the site.

**Erik O'Brien:** There is a kind of experiment we do with some clients, building a markdown file, it's called LLMS.txt, and that basically just puts everything in a markdown file at the root domain and tells the LLMS what they should know about your company, what pages they should be looking at.

**Erik O'Brien:** So it's definitely something we can put together is, you know, if we continue to move forward, it's like an experiment to see if that's able to be a kind of band-aid solution until we figure out the broader kind of client-side rendering.

**Brock Walters | Manager, Training & Enablement:** Okay, that makes sense to me, and I was actually going to suggest something like that, but I'm not surprised that you already have a kind of a workaround solution for that.

**Brock Walters | Manager, Training & Enablement:** um, but if...

**Brock Walters | Manager, Training & Enablement:** If there was a way we could give you a different view of this data on the site, it seems like it would also solve that problem.

**Brock Walters | Manager, Training & Enablement:** So, it looks like you've already got that.

**John Jeremiah | FleetDM Contributor:** Very cool.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** Well, I will get you guys a copy of that contract and then send over the technical audit as soon as that's ready to go.

**Erik O'Brien:** And then I hope you guys have a good Thanksgiving break and we will catch up with you all next week.

**John Jeremiah | FleetDM Contributor:** Awesome.

**John Jeremiah | FleetDM Contributor:** Thank you, y'all.

**John Jeremiah | FleetDM Contributor:** Thank you very much.

**Erik O'Brien:** Have a happy Thanksgiving.

**Erik O'Brien:** Thanks.

**John Jeremiah | FleetDM Contributor:** You too.

**John Jeremiah | FleetDM Contributor:** All right.

**John Jeremiah | FleetDM Contributor:** Cheers.

**John Jeremiah | FleetDM Contributor:** Bye-bye.
