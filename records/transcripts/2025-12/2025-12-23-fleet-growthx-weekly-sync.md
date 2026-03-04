# Fleet <> GrowthX - Weekly Sync

<metadata>
date: 2025-12-23
time: 19:58 UTC
duration: 44 minutes
organizer: team@growthxlabs.com
participants: Erik O'Brien (GrowthX), Brock Walters (Fleet), John Jeremiah (Fleet)
fathom_recording_id: 110736626
fathom_url: https://fathom.video/calls/514212474
share_url: https://fathom.video/share/jQcHkqSqxs6LMgso9v-Ms4jypsQhtwAM
source: fathom
enriched_on: 2026-03-02 00:00 UTC
</metadata>

---

## Summary

Fleet and GrowthX aligned on a GitHub-based workflow using labels (first draft, needs revision, updated draft, ok to publish) to track the status of hundreds of comparison articles in progress. Gabby from GrowthX will be onboarded to GitHub to directly edit PRs and see diffs, with Brock creating a Loom video to train her on the UI. GrowthX will synthesize Fleet's internal battle cards into 1,200–1,500 word long-form comparison articles (e.g., "Fleet vs. Jamf"), starting with standalone pages and leaving the door open for a hub-and-spoke model later; Brock flagged that AI-generated drafts contain redundancy and repetitive phrasing, which is critical feedback for GrowthX to tune its multi-agent pipeline to prevent context window exhaustion.

---

## Context

Fleet is a device management platform (open-source endpoint security and IT operations tool) that's engaged GrowthX to produce long-form content comparing Fleet to competitors like Jamf, Intune, and other device management solutions. This is a year-long engagement that started with 5 initial articles and is scaling to hundreds of comparisons. The collaboration involves converting Fleet's internal comparison matrices and battle cards (maintained by Brock in product/marketing) into SEO-optimized long-form articles. Erik O'Brien leads the GrowthX side of the engagement, working with Suleiman (publisher) and Gabby (managing editor). John Jeremiah (contributor on Fleet's side) handles process and technical implementation, while Brock manages the content review and provides feedback on Fleet's battle cards.

---

## Relevance

**To GrowthX Delivery:**
- GitHub-based label workflow (`first draft`, `needs revision`, `updated draft`, `ok to publish`) is now the de facto process for managing content reviews at scale (hundreds of articles). This is a generalizable pattern GrowthX can apply to other clients managing large content volumes.
- Gabby needs GitHub training; Brock will create a Loom showing the Markdown preview feature and diff viewing. This is a one-time setup that unblocks the entire workflow.
- AI-generated redundancy and repetitive phrasing are critical feedback signals for tuning GrowthX's multi-agent pipeline, particularly around context window exhaustion. This feedback should directly inform prompt engineering and pipeline design.

**To CheckThat:**
- Not directly relevant to this meeting. Mention of marketing automation (HubSpot, Salesforce, Zapier) is useful context for understanding Fleet's martech stack but doesn't intersect with AI visibility or AEO strategy.

**To GrowthX Business Development:**
- Fleet engagement is progressing well: 5 articles converted to PRs, ready for review. Scaling to "hundreds" of articles over the year indicates high confidence and potential expansion. No renewal risk signals.
- New articles paused Dec 29–Jan 2; resume Jan 7 (holiday break). Plan to track with weekly syncs.
- Standalone article strategy (rather than hub-and-spoke) simplifies initial execution and reduces GTM friction. Publishing strategy can be revisited if SEO performance warrants the hub-and-spoke model later.

---

## Overview

- **New Workflow:** A label-based GitHub workflow will replace comments for tracking content status, providing clear visibility and preventing items from getting lost in the review cycle.
- **Editor Onboarding:** Gabby (GrowthX) will be onboarded to GitHub to directly edit PRs, enabling her to see the diff and streamline the revision process.
- **Competitor Content:** GrowthX will write long-form comparison articles. The initial strategy is to publish them as standalone pages, with a future pivot to a "hub-and-spoke" model possible.
- **AI Tuning:** Feedback on AI-generated redundancy is critical for GrowthX to tune its multi-agent pipeline and prevent "context window exhaustion," which causes repetitive outputs.

---

## Key Topics

### GitHub Workflow & Visibility

  - **Problem:** The current comment-based review process is inefficient and lacks visibility, making it impossible to track content status.
  - **Solution:** A label-based workflow will be implemented to provide a consistent, at-a-glance status for each PR.
      - **Labels:** `first draft`, `needs revision`, `updated draft`, `ok to publish`.
      - **Rationale:** This system is necessary for managing hundreds of articles and provides a dedicated status for the GrowthX collaboration, distinct from general marketing project statuses.
  - **Blocker:** The GrowthX team (Suleiman) may lack the org-level permissions needed to add labels or move cards on the project board.

### Editor Onboarding & Process

  - **Problem:** Edits are currently flagged to Suleiman (publisher), but Gabby (managing editor) is the correct person to make revisions.
  - **Solution:** Gabby will be onboarded to GitHub to enable direct PR edits.
      - **Rationale:** Direct access to the diff is essential for efficient and accurate revisions.
      - **Training:** Brock will create a Loom video to train Gabby on the GitHub UI, focusing on the Markdown preview feature.

### Competitor Content Strategy

  - **Goal:** Synthesize internal battle cards into long-form comparison articles (1,200–1,500 words) for SEO.
  - **Initial Strategy: Standalone Articles**
      - **Plan:** Publish each comparison (e.g., "Fleet vs. Jamf") as a single, unified page combining the existing visual grid with the new long-form text.
      - **Rationale:** This avoids creating duplicate content and simplifies the initial implementation.
  - **Alternative Strategy: Hub-and-Spoke Model**
      - **Plan:** Use long-form articles for SEO traffic, linking to separate, more visual comparison pages.
      - **Rationale:** Allows for faster article updates and can drive higher conversion rates.
      - **SEO Concern:** Risk of cannibalizing traffic for the same keywords.
  - **Decision:** GrowthX will proceed with writing the long-form content. The final publishing strategy can be decided later, as the content itself is the primary asset.

### AI Pipeline & Content Quality

  - **Problem:** The AI-generated drafts contain "AI-isms" like redundancy and repetitive phrasing, which may stem from "context window exhaustion."
      - **Context Window Exhaustion:** A known LLM issue where long sessions cause the model to lose original context and produce repetitive, nonsensical, or hallucinated outputs.
  - **GrowthX's Pipeline:** A multi-agent system designed to manage context by injecting specific artifacts (company context, personas) at each step.
  - **Feedback Loop:** Brock's edits on redundancy are critical feedback for GrowthX to tune its pipeline and writing guidelines.

---

## Action Items

**Erik O'Brien (GrowthX)**
- Review Mike T comments on GrowthX PRs (00:03:57)
- Send John link to GrowthX PR example (00:05:22)
- Onboard Gabby to GitHub for direct PR editing; schedule time with Brock for Loom training
- Pause new article submissions for holiday break (Dec 29–Jan 2); resume Jan 7
- Ask Marcelo to deep-dive GrowthX pipeline in next education session (00:42:17)

**John Jeremiah (Fleet)**
- Confirm GrowthX GitHub permissions (specifically: can Suleiman add labels and move cards on the project board?) (00:16:08)
- Send specific permission asks to Erik and Suleiman; implement GrowthX labels (`first draft`, `needs revision`, `updated draft`, `ok to publish`)
- Update process documentation based on this meeting

**Brock Walters (Fleet)**
- Share latest competitor comparison matrix/battle cards with Erik (00:19:34)
- GrowthX to review Intune/Jamf PRs
- Create Loom video tutorial for Gabby on GitHub UI, focusing on Markdown preview and diff viewing (00:19:34)

---

## Transcript
**John Jeremiah:** Hey, hey.

**John Jeremiah:** I think it's just going be you and me.

**Erik O'Brien:** Alrighty.

**John Jeremiah:** What are you guys using for marketing automation?

**Erik O'Brien:** That's a great question.

**Erik O'Brien:** We actually engaged an agency.

**Erik O'Brien:** I believe their name is Understory.

**Erik O'Brien:** Yeah, understoryagency.com.

**Erik O'Brien:** They're an agency, but similar to how we've got workflows for content development, they've got workflows for B2B outbound.

**John Jeremiah:** Okay, so they're a digital, got it.

**Erik O'Brien:** Yeah, between that and then we've got some workflows that we've got set up through internal like Zapier, ZAPS.

**Erik O'Brien:** Um, but other than that, I'm not too deep on the latest on what we're doing for marketing.

**John Jeremiah:** So you guys are Salesforce plus Zapier and other stuff?

**Erik O'Brien:** Yeah, think HubSpot over.

**John Jeremiah:** Oh, you got HubSpot.

**John Jeremiah:** You have HubSpot though.

**John Jeremiah:** So HubSpot's doing the bulk of the, then I would assume HubSpot's doing your marketing automation.

**Erik O'Brien:** Yeah, it's, I think we've got that as like our central record of kind of content.

**Erik O'Brien:** And then we set up some automations for HubSpot.

**John Jeremiah:** Got it.

**John Jeremiah:** Yeah, so we're a Salesforce shop and the dilemma is, you know, what do you do for marketing automation and how do you keep lead and contact attribution along with opportunity attribution sorted?

**John Jeremiah:** If you're using HubSpot, most of that you're going to get for, I won't say for free, but a lot of that's kind of built into the platform.

**Erik O'Brien:** Yeah.

**John Jeremiah:** And because we're Salesforce and because we're using custom JavaScript on the website and Zapier and kind of other bespoke stuff to make things work, it means that we don't have a consistent way to do, to automate or manage or segment leads, et cetera, et cetera, et cetera.

**John Jeremiah:** So I am wrestling with how to solve that.

**John Jeremiah:** was just curious because I was literally just working on that as we came in.

**John Jeremiah:** All right.

**John Jeremiah:** So what do we want to cover?

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Hey, Brock.

**Erik O'Brien:** Just a few updates and kind of more discussion again today.

**Erik O'Brien:** So we did successfully convert the issues to pull requests.

**Erik O'Brien:** I've seen Mike T going through and adding comments in there.

**Erik O'Brien:** So I need to kind of go review in depth what's going on.

**Erik O'Brien:** Cool.

**John Jeremiah:** Five new articles that Suleiman will push either this week or next week whenever he's back.

**John Jeremiah:** So let's take, can you pull up one of the pull requests that you're looking at?

**John Jeremiah:** Yep.

**John Jeremiah:** Or reference one of them.

**John Jeremiah:** I just want to make sure that we're seeing them, that they're showing up here too.

**John Jeremiah:** Pick one, anyone.

**Brock Walters:** Yeah, they're not showing on the marketing board, John, if that's what you're looking for, because they don't have any project or labels assigned.

**John Jeremiah:** Yeah, we need to change.

**Brock Walters:** We need to, from a process perspective, need to check Well, I don't think that's nearly as important if I'm the one that's going to be reviewing all of them.

**Brock Walters:** I mean, I can do that, if Suleman would need organization-level permission to do that, because the projects only live at the organization level, not the repo level.

**John Jeremiah:** Can you send me a link to this one?

**Erik O'Brien:** Yep.

**John Jeremiah:** Yeah, but, Brock, from a management perspective, want to have visibility into these things, so I'm going to, we're doing this for a year.

**John Jeremiah:** You know, this is one of these things I want to be able to get visibility into how we're doing and where our process is at.

**John Jeremiah:** At the end of the day, I'd like to get it there.

**John Jeremiah:** So if I need to get Suleman access, then...

**Brock Walters:** Okay, I mean, I just don't know enough about it.

**Brock Walters:** What I don't know is if we can restrict his access to, for example, I don't think it would make any sense for him to have access to the confidential repo, and if we give him organization.

**John Jeremiah:** He doesn't need access to the confidential repo.

**John Jeremiah:** But as far as to be able to add it to the project, you know, can he add it to the project?

**John Jeremiah:** Can he add the labels to it?

**John Jeremiah:** Those are two questions I'm going to try to figure out.

**John Jeremiah:** So that's cool.

**John Jeremiah:** I mean, because otherwise, this whole thing is happening, you know, from a, it becomes something we just don't have good visibility into.

**John Jeremiah:** So let's keep going, though.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** So on that point, I think a couple things I wanted to clarify for process-wise with you guys.

**Erik O'Brien:** Either when Brock or Mike T are kind of reviewing these drafts and identify some edits that are needed, apparently you're tagging Sula.

**Erik O'Brien:** But he only handles, like, our submissions and pull requests, so he's basically a publisher.

**Erik O'Brien:** And so we need to be able to flag these to Gabby, who will kind of, as our managing editor, be the one to make any edits needed.

**Erik O'Brien:** And so wanted just to throw out there, is it easier to tag in Slack, or do you want her to get a GitHub handle and just be able to tag her in line there?

**Brock Walters:** I think that if Gabby doesn't have the ability to see the diff, and she's the one that's going to be doing changes, I think that would be, it would be ideal for her to see the actual diff and the understanding of what's changed.

**Brock Walters:** But that's just my opinion.

**Erik O'Brien:** I was kind of in the same boat, so I agree.

**Brock Walters:** Has Gabby used Markdown and GitHub before?

**Erik O'Brien:** No, she's a quick learner.

**Brock Walters:** Okay.

**Brock Walters:** I mean, it's not like it's just text.

**Brock Walters:** So at the end of the day, the Git diff, especially the GitHub UI can be a little, well, gross would be the first word that I would use, but it's functional, right?

**Brock Walters:** And the thing to understand, maybe what we should do is she and I can, if possible, maybe we can, or I can make a Loom video or something.

**Brock Walters:** Because the trick to it, if there is one, is just understanding that you can use that preview button to kind of, it's not going to be what it looks like on the website, but at least you get to see a human readable version of the article that shows...

**Brock Walters:** was the changed text, and then you can flip back to the Markdown to read the old text, and that's kind of the most useful thing.

**Erik O'Brien:** Yeah, she's out until next Wednesday or Thursday, but when she's back, I'll have her schedule some time with you, or we can do that loom.

**Erik O'Brien:** But yeah, just getting her up to speed on kind of the interface.

**Brock Walters:** Sounds good.

**Erik O'Brien:** Cool.

**Erik O'Brien:** And then for once, assuming all edits are made, and we get to the kind of approval, you know, good to go for publishing, is that easier for you to drop a note in Slack, or do you just want to do it straight from GitHub, too?

**John Jeremiah:** Well, we're going to be using labels to derive this, so this gets back to rather than doing these direct comments back and forth, because, again, it's not manageable.

**John Jeremiah:** Doing back and forth comments, we're going to lose them, so we're going to want to put labels on it for when it's done.

**John Jeremiah:** And I put

**John Jeremiah:** I don't know if you saw the issue earlier, Brock, or not, on the process.

**John Jeremiah:** I've been in the training session all day, so I haven't seen any.

**John Jeremiah:** Okay.

**John Jeremiah:** Yeah, I did it earlier this week, but let pull it up and then we can talk about it.

**John Jeremiah:** So from a, there's really three steps in the, let me get this open.

**John Jeremiah:** So, high level, this is the process we described earlier for when we were going to have multiple reviewers, but even with one reviewer, it works the same.

**John Jeremiah:** So it starts with, and I need to make sure the labels exist, be helpful if I spell label correctly too, but a first draft from GrowthX, followed by Brock, either you're saying it's okay, meaning we can publish it and move it forward into publishing it and merging it.

**John Jeremiah:** Or it needs revision, in which case it's going back to GrowthX for updates and revision, in which case the label to come back to us for a revisit would be updated draft.

**John Jeremiah:** I don't know if you've seen this.

**John Jeremiah:** updated this on Monday based upon our conversation last week.

**Brock Walters:** Is the expectation that adding these labels would move it through the board?

**John Jeremiah:** The expectation is the label tells us what state the issue is in, whether it's where it goes on the board.

**John Jeremiah:** It would move it on the board, but it tells us what state it's in.

**John Jeremiah:** I mean, at the end of the day, you know, one of these pull requests is either ready for first review.

**John Jeremiah:** So, you know, we're ready for, we have a first draft and it's ready for some form of review.

**John Jeremiah:** And then after that review, it goes one of two ways.

**John Jeremiah:** Either it's going back to growthx for feedback or it's okay for us to go forward.

**John Jeremiah:** Otherwise, the only way to look at one of these things and figure out where it's at is to read through the whole history of comments.

**John Jeremiah:** Which isn't terribly efficient.

**John Jeremiah:** So from an efficiency perspective, putting a label on it will make it easier for us to figure out where things are at.

**Brock Walters:** I suppose.

**Brock Walters:** I guess the only thing I would point out is that when you have an issue in a project, the status is shown.

**Brock Walters:** And so the whole point of having that kind of Kanban-style thing where you're moving it through the board is that it has a visible status right there where it says Review QA.

**Brock Walters:** So it just seems a little redundant to have both labels and statuses.

**John Jeremiah:** Well, these will be the statuses on the board.

**John Jeremiah:** This will be the statuses we'll use on the board for GrowthX, for GrowthX articles, right?

**John Jeremiah:** For the GrowthX ones, we'll use this as a way to keep track of where they're at.

**John Jeremiah:** So we'll use some form of different, we'll different, we're going to update this based upon...

**John Jeremiah:** But we'll be able to at least to have a visual representation of where all their articles are at.

**John Jeremiah:** That's the goal.

**John Jeremiah:** The goal right now is to get to a place where this shows us the visual representation.

**John Jeremiah:** And the only way we're going to get there, I won't say the only way, but the way I'm trying to get there is by putting labels on these things as to where they're at.

**Brock Walters:** Right.

**Brock Walters:** I guess maybe I would need to see an example of one.

**Brock Walters:** So if you're looking at this plan, one in the plan column at the top of the plan column, that has a label on it that says help marketing.

**Brock Walters:** But if you, or you can go to any one of the, I guess I was, but it also has a status of new requests.

**Brock Walters:** So, I mean, I, we can use both labels and status.

**Brock Walters:** I guess it just seems a little fancy to do both.

**Brock Walters:** Like, why wouldn't we just.

**Brock Walters:** Is it because the GrowthX people can't currently move the cards from column to column?

**John Jeremiah:** Well, number one, they're not part of the project.

**John Jeremiah:** And from a new request, we would probably move this one.

**John Jeremiah:** This one probably should be in progress because we're actively working it.

**John Jeremiah:** But the labels tell us where it's at as far as going through this iteration with GrowthX.

**John Jeremiah:** So the labels is really how we keep track of where it's at with GrowthX.

**John Jeremiah:** And frankly, this one needs – we haven't implemented the process labels.

**John Jeremiah:** I wanted to get feedback on this before we got into this.

**John Jeremiah:** But the process labels, the intent of having the process labels is for us to be able to manage and to keep track of where they're at in the flow between Fleet and GrowthX.

**John Jeremiah:** Because we're going to be doing hundreds of these.

**John Jeremiah:** So we need to at have a way that we can put our finger on where they're at and not lose them.

**Brock Walters:** Yeah.

**Brock Walters:** Do you believe by having two systems?

**Brock Walters:** For tracking the status, that that will help that as opposed to having a single one.

**John Jeremiah:** Well, yeah, because this is a unique situation where we're going back and forth between us and GrowthX and deciding when we're going to publish it.

**Brock Walters:** And so the labels give us visibility that GrowthX has visibility into it without being part of the project.

**John Jeremiah:** Right, but they can't set labels either, I don't think.

**John Jeremiah:** Well, let's find out.

**John Jeremiah:** Let me find out.

**John Jeremiah:** I'll take a to-do on that and we'll figure out whether or not they can.

**Brock Walters:** Okay.

**Brock Walters:** I mean, I'm happy to use your system, John.

**Brock Walters:** I just don't quite understand it, but I'm happy to try.

**John Jeremiah:** Yeah, we just have to have some level where we have consistent visibility where they're at.

**John Jeremiah:** And what we're doing right now of tagging people and comments in it, guaranteed that we'll send up spending, I won't say hours, but we're going to be spending cycles going through, figuring out where stuff's at.

**John Jeremiah:** And frankly, it's not the most efficient use of our time.

**John Jeremiah:** So if we can have a process.

**Brock Walters:** The only point that I'm trying to make, and I'm not meaning to argue, I just want to say it one last time, is that if you scroll up on even this issue, there's a visible little pill right there that says Review QA that shows what bucket it's in on the board.

**Brock Walters:** And what you want is also a label that shows a different status as opposed to that.

**Brock Walters:** it's the GrowthX status, frankly.

**John Jeremiah:** Okay.

**John Jeremiah:** You know, and it's a status specifically for what we're doing with GrowthX.

**John Jeremiah:** As opposed to a status for a general marketing issue, which is how we're managing all of our work, GrowthX is a subset of that.

**John Jeremiah:** So in this case, you know, we would have this and this is what we'll be updating.

**John Jeremiah:** And these are labels, frankly, right?

**John Jeremiah:** These are the same as labels.

**John Jeremiah:** So let me, let me go through and try to update this to make sure we can implement this.

**John Jeremiah:** Solomon has access to it.

**John Jeremiah:** Okay.

**John Jeremiah:** I mean, it,

**John Jeremiah:** As I see it, the GrowthX team needs to be able to update these some, and I want to make sure they can.

**John Jeremiah:** So, let me work on that.

**Brock Walters:** as they have, I mean, I guess what I think is that the project level, sorry, the organization level is required for changing the project status.

**Brock Walters:** Sulemon probably does have access to just add an arbitrary, or to add a label currently.

**John Jeremiah:** Let me pull a string on it, but the goal will be to use that as a way for us to keep track of where they're at in the handoff between him initiating it, you reviewing it, goes back.

**John Jeremiah:** Dig's going to, is Dig going to be doing the review process?

**John Jeremiah:** Is that the way it's going to work?

**Erik O'Brien:** Gabby.

**John Jeremiah:** Gabby, okay, sorry.

**John Jeremiah:** So, Gabby's going to do the, kind of the next step in that process, or whoever, and then when it comes back, Brock, you'll see it, and then when it's all done, we'll worry about getting it merged.

**John Jeremiah:** And for me, the final steps in it is making sure we have the right CTAs and or any CTAs we want so we can hit publish.

**John Jeremiah:** We've already talked with Mike T about his role, so.

**Brock Walters:** Okay.

**John Jeremiah:** Which he doesn't want to be day-to-day in the weeds of it, so.

**John Jeremiah:** But let me do the next step and the final step of this and making sure.

**John Jeremiah:** But I wanted to make, but part of the reason why I wrote this issue was to make sure you could see it and we could, we could talk about it and if, if there is an issue.

**Brock Walters:** I'm happy to try whatever system you're proposing.

**John Jeremiah:** Okay.

**Erik O'Brien:** Right.

**Erik O'Brien:** Brock and Nose, a couple weeks ago, we were talking through the like battle cards and matrix that you might have internally.

**Erik O'Brien:** Could you share the latest one that you have with that?

**Brock Walters:** I can.

**Brock Walters:** No.

**Brock Walters:** Thank

**Brock Walters:** So there has been some internal discussion around whether or not we're duplicating effort by having you guys do this.

**Brock Walters:** John, don't know if you have an update from Ashish on that, but do we want to move forward with having GrowthX still working on that, or what do you think?

**John Jeremiah:** John, mean, GrowthX, I mean, Erik, confirm with me what's going to happen, is you guys are going to take our current comparison framework and battle cards, and you're going to synthesize that into long-form text.

**John Jeremiah:** Is that basically right?

**Erik O'Brien:** For each article?

**John Jeremiah:** Yeah, for the comparison pages, or the comparison content.

**Erik O'Brien:** Yeah, mean, we basically want to be as informational and comprehensive as possible, so that the reader actually gets value from the article.

**Erik O'Brien:** So...

**Erik O'Brien:** A lot of that is comparing feature by feature, like when should you choose Jamf, when should you choose Fleet, or any other competitor, and so we try to keep it fairly neutral, but do highlight like the key differences, and like when you should choose which platform.

**John Jeremiah:** At least the way I see it of using this content would be not in the form of an art, of a standalone article, but in the, as the content that would be part of a comparison page for that one competitor versus competitor.

**John Jeremiah:** Yep.

**John Jeremiah:** Right, so rather than creating a separate article that competes with comparison pages, which would have the comparison grid at the top, we would most likely consolidate all this content onto a single page, Fleet versus Jamf, whatever.

**John Jeremiah:** That makes sense to you?

**Erik O'Brien:** I mean, we've seen it played both ways, where you can have the competitor page, and then mean,

**Erik O'Brien:** The article, which is really meant for SEO traffic, can link to that page, so kind of a hub-and-spoke kind of cluster model.

**Erik O'Brien:** And that allows us to, you can update the articles and refresh them a lot more quickly than you can for, you know, a landing page, we assume.

**Erik O'Brien:** So, for us, it's kind of getting the competitor content out there, seeing how it performs, usually has higher click-through rate, higher kind of demo requests, you know, across most of our clients.

**Erik O'Brien:** And then, you know, as you guys make updates and releases, like being able to update those and refresh them, like on a quarterly basis.

**John Jeremiah:** Yeah, well, I mean, it's based upon our, but I mean, the point I'm getting to is it's, it's still based upon, we should talk about, I think we should talk about whether or not we want to do it like that, or.

**John Jeremiah:** I'm thinking.

**John Jeremiah:** I mean, when you think of landing page, you're thinking.

**John Jeremiah:** I of a, of a page that has, I mean, of a page that has the comparison grid.

**John Jeremiah:** I mean, I wasn't thinking of two separate pages.

**John Jeremiah:** was thinking of, of each of these are pages that have the comparison grid, the visual representation of the comparison along with text.

**Erik O'Brien:** Yeah, so similar, similar to the homepage where you guys have like just the dropdown to pick.

**John Jeremiah:** No, well, without the dropdown, with, with a, with a fixed grid, right?

**John Jeremiah:** I'd get rid of it.

**John Jeremiah:** I mean, the dropdown is, is a, is distracting.

**John Jeremiah:** I would want the, the comparison grid on each of these pages to be simply the comparison that the page is dedicated to.

**Erik O'Brien:** Yeah.

**John Jeremiah:** Right.

**John Jeremiah:** So the, the structure of the page would be this visual of this.

**John Jeremiah:** Of A versus B, along with the long-form text.

**John Jeremiah:** I'd put both of those together onto one page.

**John Jeremiah:** I would put both of those onto one page.

**John Jeremiah:** When you're thinking of hub and spoke, how would you separate them, though?

**John Jeremiah:** I mean, let's start off with, that's what I'm imagining is, you know, leveraging that content as a single grid, not a dynamic grid.

**John Jeremiah:** Were you thinking differently?

**Erik O'Brien:** I guess when I think of other comparison pages I've seen, most of them are highlighting kind of like a handful of features and maybe doing comparison of some of those kind of quality attributes of those features.

**Erik O'Brien:** But it's much more visual than text heavy.

**Erik O'Brien:** And so I think if that was just my assumption, if it was to be kind of more of a designed page with not, you know, not 1,200 to 1,500 words.

**Erik O'Brien:** And for anybody who wanted more of a deep dive, that's where we'd have the articles to kind of link out for like a side-by-side comparison of like when to choose which.

**John Jeremiah:** Let's do this.

**John Jeremiah:** mean, from where I sit, getting the long-form text written, as long as we're talking about something that's consistent and coherent with what our current analysis is as to that comparison, I think makes sense.

**John Jeremiah:** That's what I heard Ashish talk about, and Brock, you.

**John Jeremiah:** I mean, we're all in alignment that we're creating a long-form content around this, so I don't know why we would pause.

**John Jeremiah:** The final publishing of it, we may go through a pivot on how we publish it.

**Erik O'Brien:** Yeah.

**John Jeremiah:** We may choose to design a page that, an article or a page that incorporates the graphic with the long-form text.

**John Jeremiah:** That's what I was thinking about doing.

**John Jeremiah:** Because we've already done the work on creating the matrix of the comparison.

**Brock Walters:** I don't really have an opinion.

**Brock Walters:** I just want to make sure that we're all pointed at the same goal and not duplicating effort, because, you know, there have been a number of attempts at this whole comparison thing.

**Brock Walters:** There's one that's live on the website currently.

**Brock Walters:** So I just want to make sure that, I guess, not make sure, I can't make anything sure, but that whatever effort is being expended results in the thing that everybody wants, and we're not working on two things that are the same thing in different places.

**Brock Walters:** That's what I'm worried about.

**Brock Walters:** So whatever we end up doing is fine with me.

**John Jeremiah:** I just want to make sure all the effort is targeted at one goal.

**John Jeremiah:** Yeah, and where I'm concerned, I guess, where I get worried about it a little bit is if Ashish has got Mike T spun up designing stuff, that's a parallel to this, because I don't want to have.

**John Jeremiah:** I two pages on the website that say, Jamf versus Fleet, I want one, and for me, the unified one is combining the comparison grid with the long form text that we're going to get from GrowthX.

**Brock Walters:** Yeah, I can see those things living in the same place, or at least having links to the articles that you wanted to read if you went to look at the comparison or whatever.

**John Jeremiah:** Yeah, that makes sense.

**John Jeremiah:** The real question would be, and I think the other thing about that is once we get to that is what the call to action is, and you know, it's probably get a demo, but how do we lead them to the next page, or does that page become a landing page, meaning having a form?

**John Jeremiah:** I don't know.

**John Jeremiah:** Erik, what's your take?

**John Jeremiah:** Should I put a, I mean, I don't know if I'd want to put a form on that page or not.

**Erik O'Brien:** Um, again, just kind of...

**Erik O'Brien:** kind of

**Erik O'Brien:** Basing my advice off of what I've seen historically, most of it is, especially with a kind of more technical audience, like letting them try it themselves.

**Erik O'Brien:** And so it's usually like, for one of my other clients, DeepGram, like console signups is the goal, those competitor contents.

**Erik O'Brien:** And so that's what we go after is just like, you know, to get started for free, there's credits, blah, blah, blah, and that works particularly well.

**John Jeremiah:** Do they have, in that situation, do they have a separate, are they using the hub and spoke model you're talking about?

**Erik O'Brien:** if so, how do they?

**Erik O'Brien:** so they, they were going through a website migration, so they couldn't stand up new pages.

**Erik O'Brien:** So a little bit nuanced, but they wanted to move fast on getting competitor content out.

**Erik O'Brien:** So we did the long form written pieces, which are doing fairly well.

**Erik O'Brien:** And now that they've migrated, they're going to build out specific pages.

**Erik O'Brien:** To help interlink between that content and that's, you know, already getting clicks and traffic, and then be able to link to those kind of more broad, less words, comparison pages.

**John Jeremiah:** Yeah, mean, the way I would think about it is if we wanted to do, I'm just thinking out loud now, a more complicated solution here would be what you're describing, which would be a, what's, I mean, if I hit the, long form text, the article, what's, what's, I guess, if I think about a call to action to go to the page with the graphics on it, that page with, I mean, you got to figure out how do you avoid competing with yourself from an SEO perspective on the same, exact same search term.

**John Jeremiah:** That's my biggest, where I get stuck on it.

**John Jeremiah:** So either the long form page is what you're driving for SEO, and then the short form is what you use for, you keep it non-index, I guess.

**Erik O'Brien:** Yeah, I mean, we could also play with which one drives more traffic.

**Erik O'Brien:** So like the, you know, fleet versus Jamf is one way to put it, or you could put Jamf alternatives as another headline to kind of, or an alternative to Jamf.

**Erik O'Brien:** So there's ways we can play with the title of the long form versus the title of the landing page, so that we're not cannibalizing the traffic for each other and just.

**John Jeremiah:** Yeah, either way, let's get these things going.

**John Jeremiah:** I mean, I think getting you guys to build the pages, build the content, and then when we implement, we can implement it a couple of different ways.

**John Jeremiah:** I just, I think stopping is.

**John Jeremiah:** I think the sooner we get these pages summarized, the better.

**John Jeremiah:** if we take the approach I'm thinking about, which is add the graphic to it, which is the graphic of the comparison, then you have a graphical element along with the long form all in one thing.

**John Jeremiah:** And then if we want to get more fancy and create a separate page, we can in the future.

**John Jeremiah:** That's what I'm thinking.

**Erik O'Brien:** Yeah, I mean, I think our goal, at least from the GrowthX side, is to get content published, start to get the signals, and then be able to make adjustments from there.

**John Jeremiah:** Yeah, I agree.

**John Jeremiah:** And this is a case where the sooner we get it, the better.

**John Jeremiah:** I mean, I've done these before.

**John Jeremiah:** I know how powerful.

**John Jeremiah:** I know how effective they can be if they're done.

**John Jeremiah:** And having the long form content will be much more SEO rich than the table.

**John Jeremiah:** And having the theرفom see of the PVS side here, stay risky.

**Erik O'Brien:** please share this business fromитанral.

**Erik O'Brien:** Hey, Ditard.SестоSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSumoSfelt Thank you.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** So, yeah, those are most of the things I had to talk through today.

**Erik O'Brien:** But, yeah, Brock, if you can send over that matrix that you have.

**Erik O'Brien:** I know we've sent over, I believe, Fleet versus Intune, first Jamf.

**Brock Walters:** Oh, you mean, like, in GitHub?

**Erik O'Brien:** There's already a thing?

**Erik O'Brien:** Yeah, of the pull requests from last week.

**Erik O'Brien:** And then this week we'll have Fleet versus Jamf comparison guide.

**Brock Walters:** So those two will definitely want Some of those were incomplete from Adrian's, from the person that created them, they were incomplete from his perspective.

**Brock Walters:** So I'll be interested to see what's in there.

**Brock Walters:** But I think, you know, anything is better than, there wasn't anything in there that was bad.

**Brock Walters:** It was more that it wasn't, like, exhaustive.

**Brock Walters:** So I think any starting place will be good, but I'll definitely check them out.

**Erik O'Brien:** So, let's go.

**Erik O'Brien:** Cool.

**Erik O'Brien:** And the next week is our quiet week.

**Erik O'Brien:** It's the one week per year we take off.

**Erik O'Brien:** So no new articles next week.

**Erik O'Brien:** We'll let you guys work through the backlog.

**Erik O'Brien:** And then we will pick up on the 7th.

**Brock Walters:** Awesome.

**Brock Walters:** The robots party on New Year's Eve.

**Erik O'Brien:** Yeah.

**Brock Walters:** We're going to Times Square to see the ball drop.

**Erik O'Brien:** We'll probably have a lower AI bill for that week.

**Erik O'Brien:** No tokens being eaten up.

**John Jeremiah:** Right.

**John Jeremiah:** Yeah.

**John Jeremiah:** Hey, what do you do?

**John Jeremiah:** I've got a question, specific question about your context window and how you manage that.

**John Jeremiah:** Yeah.

**John Jeremiah:** well, my experience of using...

**John Jeremiah:** And doing very long sessions, whether I'm vibe coding or doing other things with any one of the models, is after I've gone too long in a specific session and the context window starts to overlap with, you know, and I start losing original context of what happened, it gets weird.

**John Jeremiah:** And I'll get really weird results.

**John Jeremiah:** And repetitive, it'll just, it'll get really weird.

**John Jeremiah:** How do you manage that?

**John Jeremiah:** And the only reason I know it happens is because I'm paying attention to it and it gets weird, and then I have to basically start a new session.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** So we have, we inject context, depending on what step it's in.

**Erik O'Brien:** So like the research step, all that's provided is company context.

**Erik O'Brien:** Yep.

**Erik O'Brien:** The document we worked on, Brock, and then audience personas.

**Erik O'Brien:** And so we try to keep those articles or artifacts.

**Erik O'Brien:** Um.

**Erik O'Brien:** It's short in token length because we don't want to flood the window, but if it has company in the audience, it was the only context piece to be put into it, and then like a little brief of like, what's this article supposed to be about?

**Erik O'Brien:** And so it goes off and does the research there, and then once it comes back and does another draft piece, that's when it has additional context.

**Erik O'Brien:** It'll pull in of like, what are we looking for, for best practices for drafting?

**Erik O'Brien:** So it's a multi-step approach, and it's a Gentic pipeline, so it can send off multiple different kind of agents, sub-agents to go do work independently with their own context and then come back to like master agent and then provide all the updates to that one before it goes to the next step.

**Erik O'Brien:** So fairly advanced architecture set up on the backend allows us to kind of pull in the appropriate context.

**Brock Walters:** This workflow is attempting to account for that, the thing that John is talking about, right?

**John Jeremiah:** Yeah.

**Erik O'Brien:** Well, yeah, because we've definitely had instances.

**John Jeremiah:** Each one of these is a sync session, right?

**Erik O'Brien:** Yeah.

**Erik O'Brien:** But it does multiple loops back onto itself of like...

**John Jeremiah:** Onto the same session?

**Erik O'Brien:** Researching, uh-huh, until it gets to like a...

**Erik O'Brien:** So that's where the possible...

**Erik O'Brien:** Until it gets to the confidence level of...

**John Jeremiah:** Yeah, that's where the possibility, I think, of overrunning the context window, is if we're continuing to go back to the same LLM, the same session, you know, because we're effectively, every time you prompt an LLM, you're adding to that session's context as you're going on and on and on, and eventually, it starts to run over.

**John Jeremiah:** So I don't know, it'll be interesting as we kind of iterate on this to see whether or not, because I know Brock...

**John Jeremiah:** Some of the issues you saw where it was, I think there were issues that you commented that you thought were just not.

**John Jeremiah:** Complaining as code versus device configuration.

**John Jeremiah:** Yeah, and as I read that, as I read those comments and thought about it, I thought, gee, this feels an awful lot like situations I've been in where in VibeCoding it, the signal, the trigger for me was whenever the agent, the platform I was working with says, you're encountering a race condition.

**John Jeremiah:** It's like, no, I'm not, you know?

**John Jeremiah:** But as soon as it started and it would repeat the same feedback over and over and over again, I realized very quickly that I effectively would...

**Brock Walters:** I mean, I think I'm seeing evidence of that too.

**Brock Walters:** Again, without knowing what the secret code is, I'm assuming there's a certain amount of redundancy built in on purpose.

**Brock Walters:** For the way the article is structured, but there are certain places where I have corrected for what I felt was like the very, very high levels of redundancy, you know, where there would be a paragraph where it was literally exactly the same paragraph after next.

**Erik O'Brien:** Yeah, and that's the type of feedback we need to get so that we can tune our artifacts.

**Erik O'Brien:** So those are stuff in the writing guidelines or the post process checklist that we can refine.

**Brock Walters:** Yeah.

**John Jeremiah:** Yeah, and that's a question is how do you test for that?

**John Jeremiah:** Because for me at least the test for it was I sensed it.

**John Jeremiah:** You know, it's like putting your toe in the bathtub whether the water is too hot or too cold.

**John Jeremiah:** You know, can, you, I kind of knew it was happening.

**John Jeremiah:** But in this situation because Yeah.

**John Jeremiah:** Is that you guys have the framework built with the different agents doing the work somewhat autonomously?

**Erik O'Brien:** I just don't know how you catch it.

**Erik O'Brien:** Yeah, a lot of it comes down to the managing editor, like being able to spot these like AI-isms of like, you know, when we ask for it to do bottom line up front, like just state the end goal or the end fact and then back up why that's a fact with evidence.

**Erik O'Brien:** It'll sometimes just create a bottom line up front fact that then it doesn't back up at all, or it's just like more, it's common sense and it's like, this isn't informative to the reader whatsoever.

**Erik O'Brien:** And so those things like we tend to catch as the editor goes through and starts reading it of like, no , Sherlock, this is something anybody would know.

**Erik O'Brien:** So like it's bottom line up front, it's a little overstated here.

**John Jeremiah:** Yeah, there's a, and I don't know for sure.

**John Jeremiah:** mean, I've experienced this person, you know, on for kind of personally, and I kind of have a sense for what I was when it would happen.

**John Jeremiah:** I don't know the technical answer to how you solve it, though.

**John Jeremiah:** Big picture.

**John Jeremiah:** But either way, we'll keep going.

**John Jeremiah:** I was curious how you handle that because it's not a typical hallucination where it just makes  up.

**John Jeremiah:** It starts making stuff up when you've exhausted its memory.

**John Jeremiah:** You've kind of pushed it outside.

**John Jeremiah:** For me, at least, it would happen when I did that, when I've gone so far that I start overwriting it.

**Erik O'Brien:** That's where we're starting to get into, like, reviews of the pipelines where we're looking at, like, if it's an identic workflow and it's double-checking its work and it needs to pass a certain confidence level before it can move on to the next step, do we need the fact checker in there?

**Erik O'Brien:** Because the fact checker pipeline runs off Excel or Tably, which are fairly expensive tools.

**Erik O'Brien:** So we're, like, finding stuff just last week where, like, we don't need the fact checker in here because it actually starts to, like...

**Erik O'Brien:** He said, just starts to use up all the memory of going back and forth because the fact checker finds something that the agent's pretty positive is true.

**Erik O'Brien:** And they're using different source files of like where they get this information from.

**Erik O'Brien:** So a lot of engineering work that we're doing in the background to kind of make the standard pipelines that we use more efficient and less burdensome on kind of the review processes, but still a work in progress.

**John Jeremiah:** No, I get it.

**John Jeremiah:** And it's one of those things that all of the review feedback will never fix, in my view, won't necessarily fix it because, well, maybe it will.

**John Jeremiah:** It kind of depends on how you reset the, you know, for me at least, I think the simple answer is that, you know, after a period of time where you detect when you've reached the edge of the context window on the session and you say, okay, we're going to start again.

**Erik O'Brien:** Yeah, that's why sometimes the pipeline.

**Erik O'Brien:** And we have to rerun it because it does run out of, and then we go back and like, well, what step failed?

**Erik O'Brien:** And then start to look at why did it fail?

**Erik O'Brien:** And then some of it, yeah, it's like it just ran out of, it's been running for two hours.

**John Jeremiah:** Yeah, I mean, because if you get to, right, I mean, it's one of those things that it's like they have a short attention span.

**John Jeremiah:** And once you get past that, they lose you.

**John Jeremiah:** But either way, we could go on.

**Erik O'Brien:** And this is a session, it's a different conversation.

**Erik O'Brien:** I'm just curious from them.

**John Jeremiah:** Yeah.

**Erik O'Brien:** Marcelo will go through it in our education session.

**Erik O'Brien:** He'll, I'll tell him to do a deep dive into the pipeline.

**John Jeremiah:** And we'll do, we're, we're going to do that too.

**John Jeremiah:** So, all right, let me, let me do some work on this.

**John Jeremiah:** I'll send over some specific asks and we can pass it to Solomon and, and we'll see if you guys can make the changes.

**John Jeremiah:** And if not, we'll figure out, I'll figure out how we can, how we can overcome it.

**Erik O'Brien:** All right.

**Erik O'Brien:** Sounds like a plan.

**John Jeremiah:** So, cool.

**Erik O'Brien:** All right.

**Erik O'Brien:** All right, guys.

**John Jeremiah:** Appreciate it.

**John Jeremiah:** Merry Christmas, Brock.

**Brock Walters:** Merry Christmas.

**John Jeremiah:** Eric, have a Merry Christmas.

**John Jeremiah:** I won't be, I won't be.

**John Jeremiah:** See you guys until that, and I don't know, we meeting next week?

**Erik O'Brien:** No, we're not meeting next week.

**John Jeremiah:** Not meeting next week, no.

**John Jeremiah:** We're not.

**John Jeremiah:** So happy New Year, too.

**Erik O'Brien:** Yeah, happy New Year.

**Erik O'Brien:** Yeah.

**John Jeremiah:** We'll see you guys.

**John Jeremiah:** Thanks, everybody.

**Brock Walters:** Thanks.

**John Jeremiah:** Thanks.

**John Jeremiah:** Cheers.

**John Jeremiah:** Bye-bye.
