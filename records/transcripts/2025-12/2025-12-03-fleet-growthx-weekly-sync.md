# Fleet <> GrowthX - Weekly Sync

<metadata>
date: 2025-12-03
time: 20:30 UTC
duration: 33 minutes
organizer: Erik O'Brien
participants: Aida Knezevic, Erik O'Brien, Brock Walters, John Jeremiah, Irena Reedy, Ashish
fathom_recording_id: 106103265
fathom_url: https://fathom.video/calls/493316369
share_url: https://fathom.video/share/Jqc1HR_XZQUbXy5tFKyoNiLdHUt52t1z
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

GrowthX and Fleet aligned on content quality workflows and AI hallucination risks, with the decision to flag deeply flawed articles for complete rewrites rather than extensive manual editing (same-day/next-day turnaround). John Jeremiah and Brock Walters advocated strongly for proceeding with Phase 2, pending final approval from Ashish. The team also discussed GitHub draft visibility risk, public DNS issues, and long-term vision to build a comprehensive, SEO-rich MDM resource beyond Fleet-specific content.

---

## Context

Fleet is a major client of GrowthX, engaged in a multi-phase content generation and optimization program. The partnership centers on creating technical content around Fleet's mobile device management (MDM) platform. Week 8 of the engagement focused on content quality review processes and the decision to proceed with Phase 2. Brock Walters (Training & Enablement), John Jeremiah (Contributor), and Irena Reedy (Content Specialist) represent Fleet; Aida Knezevic leads GrowthX's content operations. GrowthX has built an in-house platform called Atlas to support the workflow: human editor research, assignment direction (SEO outline), AI-powered research and drafting, fact-checking, and final editorial review before delivery to Fleet.

---

## Relevance

**To GrowthX Delivery:**
- New workflow established for articles with major errors or incompleteness: flag for full rewrite rather than extensive manual editing, with same-day or next-day turnaround.
- GrowthX expects feedback to improve the process through GitHub PRs with inline comments, not just individual article fixes.
- Process improvement is iterative: content editors monitor review feedback and update inputs (assignment directions, writing guidelines) across all articles.

**To GrowthX Business Development:**
- Phase 2 decision due this week; strong internal support from Brock and John Jeremiah. Final approval authority is Ashish (Fleet).
- Erik O'Brien to connect with Ashish for Phase 2 go/no-go decision.
- Account demonstrates responsiveness and flexibility — positive renewal and expansion signal.

**To CheckThat / AI Visibility:**
- Technical SEO audit findings: newer LLMs appear multi-modal and can read JavaScript-rendered homepage (unexpected discovery). Erik to confirm and report findings.
- Other technical SEO issues from audit align with SEMrush data and require attention.
- Long-term vision: build comprehensive, SEO-rich MDM resource beyond Fleet-specific content — potential for broader AI visibility win.

---

## Overview

- **Process Shift:** For major AI errors (e.g., conflating "configuration as code" with "MDM configuration profiles"), the new workflow is to flag the draft for a full rewrite, not to perform extensive manual edits.
- **Phase 2 Decision:** The decision is due this week. John Jeremiah and Brock Walters strongly support continuing, citing the program's value and GrowthX's responsiveness. Ashish is the final approver.
- **Public Drafts Risk:** Publicly hosting unvetted drafts in the GitHub repo risks crawlers indexing incorrect information. The agreed solution is to delete any draft that will not be published.
- **Future Vision:** John Jeremiah proposed a long-term vision to build a comprehensive, SEO-rich resource on the broader topic of MDM, not just Fleet-specific content.

---

## Key Topics

### Content Quality & Review Process

  - **Problem:** AI-generated drafts sometimes contain "hallucinations"—confidently incorrect content that conflates distinct technical concepts (e.g., "configuration as code" vs. "MDM configuration profiles").
  - **Impact:** Correcting these errors requires extensive manual editing, which is time-consuming and risks undermining the article's SEO structure.
  - **New Workflow:** For drafts with major errors or incompleteness, the new process is to flag them for a full rewrite.
      - **Rationale:** GrowthX offers a fast (same-day/next-day) turnaround for revisions, making this more efficient than manual correction.
  - **Feedback Loop:** John Jeremiah emphasized that feedback must improve the *process*, not just the individual article.
      - **Method:** Use GitHub Pull Requests (PRs) for inline comments to provide specific, actionable feedback that helps GrowthX refine its AI inputs and human-editor guidelines.
      - **Goal:** Reduce review time by systematically improving the content generation process.

### Phase 2 Decision

  - **Deadline:** The decision on whether to proceed with Phase 2 is due this week.
  - **Support:** John Jeremiah and Brock Walters strongly advocate for continuing.
      - **Rationale:** The program is a critical need, and GrowthX has been highly responsive to feedback.
  - **Ownership:** Ashish is the final decision-maker. John Jeremiah will connect Erik O'Brien with Ashish to discuss.

### Public Drafts in GitHub

  - **Concern:** Publicly hosting unvetted drafts in the GitHub repo creates a risk.
      - **Scenario:** If a draft with significant errors (like the "configuration" example) is never published, it could still be indexed by search engines and LLMs, creating a source of public misinformation.
  - **Solution:** Delete any draft from the public repo that will not be published.
      - **Rationale:** This prevents incorrect information from being indexed.
      - **Constraint:** This requires a process change for Fleet, which typically closes issues rather than deleting them.

### Technical SEO Audit

  - **LLM Input Test:** The audit's finding that LLMs can read the homepage was surprising, as it was expected they would be blind to JavaScript-rendered content.
      - **Hypothesis:** Newer LLMs may be multi-modal and can now process such pages.
      - **Action:** Erik O'Brien will investigate and report back.
  - **Other Findings:** The audit's other technical SEO issues align with data from SEMrush and require attention.

---

## Action Items

**Aida Knezevic (GrowthX)**
- Compare original vs Brock's edited draft; share diff with Brock

**Erik O'Brien (GrowthX)**
- Schedule sync with Ashish and John re: Phase 2 go/no-go decision
- Confirm LLM JS-rendering capability; update John with findings

**Brock Walters (Fleet)**
- Verify GitHub issue/PR deletion capability; report back to Aida

---

## Transcript
**Aida Knezevic:** Hi.

**Aida Knezevic:** Looks like John can't make it, he rejected the invite, but, okay, here's Brock.

**Aida Knezevic:** Hi!

**Brock Walters:** Hello.

**Brock Walters:** I really said she's running late, I believe, so.

**Aida Knezevic:** Okay.

**Brock Walters:** And I've never been on time to a meeting in my life, which I apologize for.

**Brock Walters:** Okay, so, yeah, I'm in the middle of another article right now.

**Brock Walters:** I did look at them before, but I hadn't really dug into them.

**Brock Walters:** They're long, and they've been hard to edit.

**Brock Walters:** it's I hope most ucz you know.

**Brock Walters:** You

**Brock Walters:** Also, I think I have some human understanding of the limitations of AI and language, and that there's statistical matching happening, and if we're using the word configuration in two different contexts, the robot doesn't necessarily have a way of discerning that, especially when whatever context is surrounding the word configuration that's being used to extrapolate and create the text is probably, would be confusing to a human reader, because there are subtle differences.

**Brock Walters:** The one that I did yesterday, I put a lot of edits in it, but there wasn't anything catastrophically, like systemically wrong.

**Brock Walters:** But the one that I worked on yesterday, it was just a total, like just your classic, what is described as.

**Brock Walters:** The AI hallucination, right?

**Brock Walters:** It's just completely destroying the context of how the word configuration is used in configuration as code and how the word configuration is used in the context of MDM and configuration profiles and just, what's the word?

**Brock Walters:** That I'm arbitrarily combining concepts from those two separate things in a way that made absolutely no sense.

**Brock Walters:** And just, these aren't complaints, I'm just telling you what happened.

**Brock Walters:** It made it very difficult to do, right?

**Brock Walters:** Because it's so sure about what it's written.

**Brock Walters:** It's so confidently wrong.

**Brock Walters:** It's very difficult to be like, wait a second.

**Brock Walters:** This like, does not, like, it just, it has no human context.

**Brock Walters:** So to undo it is a, without telling you my, the torture inside, I'm worried that fixing them will take longer than the people that I'm signing up to do this will be willing to spend.

**Aida Knezevic:** I think with these types of cases and not to say that it just doesn't happen often, but there will be times when these types of articles like there's just a confusion and there's also I think might be a human element to it where someone, if it was being generated by a subject matter expert, they could provide like a direction saying hey like don't confuse these two types of concepts.

**Aida Knezevic:** I think in these types of cases where you literally start reading and you're like oh this is not right, like it's confusing, like our, what we would like you to do is just to tag us immediately and be like this isn't good, it's confusing.

**Aida Knezevic:** We need to rewrite it because of like, you can give us like two or three bullet points and we'll redo it and then send it to you because I don't, our expectations, like we do up to two revisions, like two rounds of edits on a draft.

**Aida Knezevic:** So it really is never our intention to have you like edit something.

**Aida Knezevic:** Of course not.

**Aida Knezevic:** I just wanted to kind of put that out there.

**Brock Walters:** I mean, I guess the only problem is I, I'm, it's hard to know at this stage where the, so John and I took a crack at creating a, like a, a little bit of a guidelines for people who might be doing this editing work.

**Brock Walters:** Um, and what you just said is interesting because at this, like, it's hard to know at this point, what it would, what's the threshold to say, like, you guys need to complete.

**Brock Walters:** Thank

**Brock Walters:** Completely redo this because it doesn't make any sense versus, okay, I'm fine with changing this and changing that.

**Brock Walters:** Like, I don't know that we have a clear threshold that says, like, yep, this has to go back in the oven.

**Aida Knezevic:** I think the case that you just talked about, that is one instance.

**Aida Knezevic:** That would be kind of the extreme end.

**Aida Knezevic:** And then I think another scenario would be when it's a topic where you think we are missing an important part of the story.

**Aida Knezevic:** So if you feel like an article is incomplete, there's something that we just have to add to make it comprehensive.

**Aida Knezevic:** In that case, you would also flag it to us.

**Aida Knezevic:** I can think of some more.

**Brock Walters:** I mean, so would it help you if I explain to you the specific subtle distinction that was...

**Brock Walters:** not being made?

**Brock Walters:** Or is it just better that I've rewritten the article and removed all of the problematic references and now you guys have that to use as a model?

**Brock Walters:** Like, which is more helpful to move forward?

**Aida Knezevic:** I think the team that generates the content, they would appreciate a quick explanation of just, but I think you did explain it in the beginning.

**Aida Knezevic:** You were saying it was conflating configuration as code with device configuration, right?

**Brock Walters:** Right, which is very reasonable because it's the same word.

**Brock Walters:** Yeah, yeah.

**Brock Walters:** So it's like, how do human beings keep a word that has two different meanings separate?

**Brock Walters:** Often they don't.

**Brock Walters:** And we have to write it down in a dictionary.

**Brock Walters:** And those meanings change over time.

**Brock Walters:** Uh, and sometimes words 300 years ago that meant one thing now mean completely the opposite thing.

**Brock Walters:** Uh, what's an example of that?

**Brock Walters:** The word concept.

**Brock Walters:** We used the word in concert to mean we're going to do something together.

**Brock Walters:** The original version of that word actually meant we're going to fight.

**Brock Walters:** So, like, if we haven't been able to figure this out with just writing down how we use language, I don't know how you expect your robot to figure it out, but I'm willing to keep trying.

**Brock Walters:** So, I guess we'll just keep on trucking.

**Brock Walters:** The article yesterday shook my confidence a little, and I guess what I'm looking for from you is I'm perfectly willing to edit these things and try to make them as close to what I would write as possible.

**Brock Walters:** That's just time-consuming.

**Brock Walters:** My fear is if I tell you, hey, these three things are problems, please write it again.

**Brock Walters:** That doesn't seem as efficient to me as as guess I'm pretty

**Brock Walters:** Me giving you an example of an article that doesn't have this conflation or doesn't have these mistakes, but then the edits that I've made may be somehow screwing up your formula for SEO, which defeats the whole purpose.

**Aida Knezevic:** Yeah, I think I get what you mean.

**Aida Knezevic:** So for us, we are very efficient when it comes to implementing revisions.

**Aida Knezevic:** So we do typically like either same day or next day turnaround, depending on like the scales, like the scope and the depth of revisions, but it's not going to set us back in the sense that's like you're going to have to wait for a week for us to redo something.

**Brock Walters:** Sure.

**Brock Walters:** Okay.

**Aida Knezevic:** And I appreciate that.

**Brock Walters:** mean, I'm probably much less timely than you are.

**Aida Knezevic:** Yeah.

**Brock Walters:** And I think what you did with this article, since you like rewrote it and edited it heavily.

**Brock Walters:** I mean, it wasn't like a top to bottom rewrite.

**Aida Knezevic:** But I did have to remove sections that were just like, this does not make sense.

**Aida Knezevic:** Yeah, I think we can use that.

**Aida Knezevic:** So we can use the final draft and then the original, and then we can compare those two and see what was changed.

**Aida Knezevic:** And that's also helpful, but it's certainly, you know, we can do, like, we can do pretty quick turnarounds in terms of revision.

**Brock Walters:** Okay, cool.

**Brock Walters:** That's really all I had.

**Brock Walters:** I, you know, I think I'm just going to keep plugging away at it and use your guidance to make sure that whatever you're getting back from us is still going to be useful for the long-term goals of the project.

**Aida Knezevic:** Okay, got it.

**Aida Knezevic:** Erik, I don't know if you had any updates that you wanted to share.

**Erik O'Brien:** Mainly just the kind of recap I sent over last night.

**Erik O'Brien:** right.

**Erik O'Brien:** All Subtitling Thank Thank

**Erik O'Brien:** We are in week eight, so I think we've had the due date of Monday, I guess, for the SOW date, but for phase two decision.

**Erik O'Brien:** And so I know you guys wanted to look at the contract last week and have the kind of conversation internally, if it makes sense to move forward, but wasn't sure if you guys have a decision on that, but it is something we'll have to have finalized by this week.

**Erik O'Brien:** I you're out of mute, John.

**John Jeremiah:** God, hate the mute thing.

**John Jeremiah:** Sorry about that.

**John Jeremiah:** I am talking to Ashish about it.

**John Jeremiah:** We're working on clarity on the decision.

**John Jeremiah:** From where I said, I think this is a program we desperately need to do.

**John Jeremiah:** I see the, um, I've done these programs before with other people that do these.

**John Jeremiah:** think you guys are doing, from where I said, I think it's, it's as a if I say just, I

**John Jeremiah:** You know, it seems like we're already up and going, so I don't see any reason to change.

**John Jeremiah:** I think we need to execute.

**John Jeremiah:** So that's where my head is at.

**John Jeremiah:** And I have a question, a process question.

**John Jeremiah:** You guys have an editor involved.

**John Jeremiah:** I mean, I want to get clarity because when Brock talks about, well, we just have the robot doing this, we're not getting, this is not robotic LLM content that's just coming at us, right?

**Aida Knezevic:** No, no.

**Aida Knezevic:** So I can share my screen really quickly to kind of give you, because I don't think I showed this to Brock, and I'm sure that I never showed the platform to you, John.

**Aida Knezevic:** So this is Atlas, which is our content generation platform that we built in-house.

**Aida Knezevic:** It's about six months old.

**Aida Knezevic:** So we have a team of developers that built it and maintains it and also develop.

**Aida Knezevic:** So, this is your workspace.

**Aida Knezevic:** The artifacts that we're using, they live in this part of the platform, and we can update them as needed.

**Aida Knezevic:** And then for the actual article generation process, this is the workflow that we are using.

**Aida Knezevic:** So, the input is the topic, and along with the input, we provide, sorry, the scrolling thing is annoying.

**Aida Knezevic:** Okay, so with the input, we also provide an assignment direction, which is kind of the SEO outline skeleton of what we want the end article to be.

**Aida Knezevic:** And this is informed by a human editor who researches for the article from an SEO perspective.

**Aida Knezevic:** So they analyze the top-ranking content, do all of that.

**Aida Knezevic:** Stuff.

**Aida Knezevic:** So there is a human involved at every stage.

**Aida Knezevic:** The researcher is AI-powered.

**Aida Knezevic:** So let me just switch to the input.

**Aida Knezevic:** So once we give it an assignment direction in terms of a rough outline, it goes and it researches the topic in detail.

**Aida Knezevic:** It uses Taboli for research.

**Aida Knezevic:** Other researchers we used in the past are Perplexity.

**Aida Knezevic:** We also use EXA.

**Aida Knezevic:** So it combines all this information, it drafts the article, and then we run it through all of these steps like adding source links, validating the writing guidelines.

**Aida Knezevic:** We also run a fact checker that uses the research document to ensure that all of the information, or like any stats, industry reports that are referred to in the drafts, that they also appear in the research document.

**Aida Knezevic:** And then it

**Aida Knezevic:** We do a final content review, which is when the editor will read the draft, edit it, and then we send it to you for review.

**Aida Knezevic:** So we spend a lot of time on the outline just for SEO purposes and to make sure that the piece is comprehensive, but we also spend a lot of time at the end polishing it.

**John Jeremiah:** So on the fact, I mean, part of my, Mike, the reason for my question is, as we give you feedback, in the case where happy really should be replaced with glad or, you know, their terms are, there's language or there's elements to our domain that are peculiar and require some refinement.

**John Jeremiah:** How does that get folded back into the model?

**Aida Knezevic:** So right now, it's not advanced enough to do this automatically, but we have the human editor, they will, if it's a, if.

**Aida Knezevic:** If it's a heavier edit in the sense of it's a stylistic choice, like, for example, you never want to use a specific phrase, or you never want to talk about Fleet in a specific way, or like use it in the same paragraph with another phrase, then we would add that to the writing guidelines, which you can find in Notion for things like...

**Brock Walters:** Just real quick, just so John knows, because I don't think he was part of this when we started, I did modify the original stuff that I've been describing generically as seeding, but they got a lot of stuff from the Fleet Handbook in terms of style and guidelines and stuff like that, and a lot of that stuff was edited by me before things started being generated.

**Brock Walters:** So, that also included some modifications to like, personas and like how the company is described.

**Brock Walters:** So, we have had, we've touched that stuff.

**Brock Walters:** don't know that we've completely touched everything that's being used, but it has been edited by me to make sure that we were starting in the right place.

**John Jeremiah:** Sorry.

**John Jeremiah:** Well, I just want to make sure that, you as we give feedback, you know, if, and, you know, I'm of the belief that we should be pushing if something's not right or if we have, and part of the reason I want to do these things in pull requests is so we can make comments in line into the document and say, these are issues.

**John Jeremiah:** deal with the please address.

**John Jeremiah:** I mean, what I don't want to do is be in a situation where, you know, this week we change happy to glad, next week we change happy to glad.

**John Jeremiah:** You know what I mean?

**John Jeremiah:** I want to try to make sure that we're iterating and improving too, that the feedback's ending up being a positive on the process.

**John Jeremiah:** And I get it.

**John Jeremiah:** The editor kind of depends on who the editor is.

**John Jeremiah:** I, you when I did this, when we built TechBeacon, here got so the audio.

**John Jeremiah:** The editors were very deep experts in their field and were professional journalists by trade and we were building the platform that way.

**John Jeremiah:** And again, it was all manually.

**John Jeremiah:** We didn't have AI writing it, but it was humans doing the, you know, they'd take a pitch and they would build a pitch.

**John Jeremiah:** Same concept, right?

**John Jeremiah:** We had the same concept of what keywords were we trying to build into the article and how do we want to impact SEO.

**John Jeremiah:** But I just want to, I mean, because one of the things that I want to make sure we do is that when we do give the feedback that it's not just to fix the article, it's to fix the process.

**Brock Walters:** Yeah, yeah.

**Aida Knezevic:** Yeah, yeah.

**Aida Knezevic:** That's why I am all for the pull request change.

**Aida Knezevic:** We do want to get that feedback and it's a practice that we do with every client.

**Aida Knezevic:** So if I told you that we have, I mean, I would be lying.

**Aida Knezevic:** If I told you we have a subject matter expert on device management, like we don't have somebody with experience in that specific area, but everybody, our content managers who generate and edit the content, they're also in charge of monitoring your reviews to each piece and then updating the inputs as needed.

**Aida Knezevic:** So we are, you know, our goal is for the reviews to get shorter and shorter.

**Aida Knezevic:** So it is part of the process.

**Aida Knezevic:** And yeah, it's, I'm going to teach you everything I know.

**Brock Walters:** You're going to just hate it by the end.

**John Jeremiah:** Well, I mean, but, but, but Brock, if we don't give them that feedback, then you're, you're kind of stuck every time.

**Brock Walters:** No, I mean, I completely understand what you're saying.

**Brock Walters:** And I, uh, there's, there's, uh, if I could plug my, uh, something into my temple, that would be sweet.

**John Jeremiah:** But until then, we'll just, and to be quite honest, you know, one of the things we could think about doing would be, you know, if we were to.

**John Jeremiah:** So let's do this process, but I'm imagining a state where we end up creating our own ability to scan for correctness.

**John Jeremiah:** You know, heck, it's what Mike does when he reviews content before it gets published.

**John Jeremiah:** He has, I don't know what he's using, but he's got a model trained on the fleet language.

**John Jeremiah:** Mike Thomas.

**John Jeremiah:** Yeah.

**Brock Walters:** Yeah, he's using a combination of, like, Grammarly, and he's got some prompt that he's using that's, uh, that he's kind of standardizing.

**Irena Reedy:** He he's implemented a, something into his chat to make sure that everything is all, is that what you're saying?

**John Jeremiah:** Mm-hmm.

**John Jeremiah:** Yeah, we talked to, we talked to Mike, we talked to him last night, but, but I'm imagining as we go forward, if we, if we, as we mature, I could easily see us getting to a place where, you know, we take input into, and we have our own sort of fact engine or validation engine.

**John Jeremiah:** We could throw in front of it, too.

**Brock Walters:** AI.

**Brock Walters:** We've been wanting Brock AI for many, many years now.

**John Jeremiah:** Yeah.

**Brock Walters:** Yeah.

**Irena Reedy:** I'm ready.

**Brock Walters:** I'm ready.

**John Jeremiah:** Cool.

**Aida Knezevic:** Okay.

**Aida Knezevic:** All right.

**Aida Knezevic:** And then, yeah, I don't know if I had any other updates.

**Erik O'Brien:** Erik, what about you?

**Erik O'Brien:** No, nothing on my end.

**Erik O'Brien:** think, like I said, we're kind of eager to move forward in phase two, kind of continue to iron out these details and get your guys' feedback, get some things published that start to see some traction.

**Erik O'Brien:** So, yeah, I think the only thing we'll need this week is just that final kind of written decision.

**John Jeremiah:** Final go forward.

**John Jeremiah:** And Ashish is going be the guy that's going to have to give it.

**John Jeremiah:** You know, I think Mike initiated the engagement, and I'm going to look to Ashish to be the ultimate decider.

**John Jeremiah:** I think Mike's delegated it to Ashish anyway, and I've given Ashish input.

**John Jeremiah:** So,

**John Jeremiah:** If you want, we can grab some time offline and have a conversation with Ashish.

**John Jeremiah:** But he ultimately has to own this.

**Brock Walters:** Agreed.

**John Jeremiah:** I'm favor of going.

**Brock Walters:** Same.

**Brock Walters:** I'm 100% in agreement with you, John, that we absolutely have to do something.

**Brock Walters:** And I think you guys have been super responsive to how we've talked about this.

**Brock Walters:** And I feel like the process is as good as it can be for something like this.

**Brock Walters:** So I'm generally in favor of continuing it if my input has any impact.

**John Jeremiah:** No, it does.

**John Jeremiah:** It's valuable, Brock.

**John Jeremiah:** I mean, I've done this before where I've had armies of humans developing content, which behind the scenes, they may well be using some AI.

**John Jeremiah:** But I mean, a lot of times they're doing it because they want the byline.

**John Jeremiah:** But yeah, for me, at least, it's getting a scalable process up and running.

**John Jeremiah:** And separately, I'm hinting at this, but I have a...

**John Jeremiah:** At least a mental model of how we can take this to a much bigger next level.

**John Jeremiah:** You know, I think the work we've done to put a stake in the ground and start to build content, I think, is spot on.

**John Jeremiah:** But I'm actually flirting with a bigger idea for how can we produce more content around MDM writ large that's not about Fleet but about MDM, the topic.

**John Jeremiah:** Because, to be honest, we don't have a lot of good content that's SEO rich.

**John Jeremiah:** We do have some, it's funny, because Mike just, Mike McNeil just sent me a Slack with a link to some MDM content that, when they were meeting with NVIDIA, and he said, see, this is why it's on the website.

**John Jeremiah:** And it was, it was basically MDM commands.

**John Jeremiah:** And so, in alignment with that, think there's an opportunity for us to create a more holistic MDM resource.

**John Jeremiah:** And so rather than these being buried in an article structure, which doesn't have much structure, I think we could create a structure that gives this stuff all a home and it'll all make more sense.

**Brock Walters:** We could talk about that later.

**Brock Walters:** Yeah, I have some ideas about that as well, John, that we should probably – I would love to talk to you about that because this – we'll talk about it offline.

**John Jeremiah:** Yep.

**John Jeremiah:** Cool.

**John Jeremiah:** But nonetheless, Erik, I'll look to you.

**John Jeremiah:** If you want to shoot me a note, I'll – we need to just – let's get connected with Ashish and have a quick conversation.

**Erik O'Brien:** Yep.

**Erik O'Brien:** Okay.

**Erik O'Brien:** We can do that.

**John Jeremiah:** And then the last thing I had was the technical audit, painful as though it was to read.

**John Jeremiah:** I do – I am still not sure what to do with the LLM inputs because my crude testing – somehow the LLMs know.

**John Jeremiah:** Oh, can read our home page.

**Erik O'Brien:** Yeah, I asked our team to look at that because we've been doing that just quick test kind of for all clients as part of the technical SEO on it.

**Erik O'Brien:** And it appears that, you know, maybe the models after updates have become multi-models so they can read, you know, without rendering JavaScript.

**Erik O'Brien:** So I've asked for clarification on that and we'll get back to you kind of soon as you get back from that team.

**John Jeremiah:** Yeah, I'd appreciate that because I went back and tested some older models too.

**John Jeremiah:** I used Poe to do multi-model testing.

**John Jeremiah:** So a lot of them seem to be able to at least summarize the home page as opposed to being completely blind to it.

**John Jeremiah:** But having said that, the other part of it, the technical SEO side of it is, I think, more concerning.

**John Jeremiah:** it aligns with, I just signed up for SEMrush, it kind of loosely aligns with what SEMrush is showing me as well.

**John Jeremiah:** So we need to start chipping away at that.

**Brock Walters:** I was just reminded of a goofy question, and I might be the only person that's concerned about this.

**Brock Walters:** It was the thread that we had about whether or not these draft articles should be posted in the public repo or not.

**Brock Walters:** And, I mean, I suppose it's possible that if we're approving every title, then every draft is eventually going to be published on the website.

**Brock Walters:** But if there are some that get rejected, I guess it seems to me, maybe I'm imagining a world of efficiency that doesn't exist.

**Brock Walters:** But it seems to me that if we're having article topics or either complete drafts of articles that we're actually not going to publish, that we're working at cross-purposes if we have something that is effectively posted publicly in the repo that we're not going to use that could be crawled and added to the LLM somewhere.

**John Jeremiah:** I don't think so.

**John Jeremiah:** The, I'm not worried about, at least I'll jump on it.

**John Jeremiah:** mean, I'm working from an SEO perspective, whether or not, and again, I came from GitLab, so I, where we lived, you know, everything was public.

**John Jeremiah:** Everything's public, We would live stream meetings like this.

**John Jeremiah:** The, I don't, I mean, for me, at least if we have some content that doesn't make it through, we decide to discard, it sits on a branch in a repo, you know, and it's sitting out there.

**John Jeremiah:** I don't know, I'm inclined to just say, let it run, and that way we don't have to deal with being, things being confidential or not.

**John Jeremiah:** think it just makes things more complicated.

**John Jeremiah:** I'm not, and I'm also not terribly worried, because I don't think the engines, Erik, correct me, do you think there's a problem or a risk with Google or any of these tools surfing GitHub?

**Erik O'Brien:** No, I don't think they would start there to kind of get the most up-to-date information about your company.

**Erik O'Brien:** Even Even though.

**Brock Walters:** So that's where we post the most up-to-date information about our company?

**Erik O'Brien:** I think it's, they'll still start with your kind of public URL, FleetDM, and kind of start the crawl from there, versus go to like github.com slash FleetDM.

**Brock Walters:** Yeah, and I guess the point, I'm not meaning to argue, I guess the point that I'm trying to make is that for Fleet, the distance between the repo and what's on the website is shorter than probably for most organizations.

**Brock Walters:** They're the same.

**Brock Walters:** And if they're somehow in conflict, is that going to break something?

**Aida Knezevic:** I would like to think that all of the articles that were published, like, that do end up in the repo, even if we decide not to publish anything, none of that content is going to talk about Fleet in a way that you'd be like, this is completely wrong, we don't do this.

**Aida Knezevic:** Like, the product description, the product messaging has to be accurate.

**Aida Knezevic:** Like, we...

**Aida Knezevic:** Absolutely, as a company, we have to get that right.

**Brock Walters:** Right, but I guess my point is, if I use the example that I was working on yesterday, if that existed as a draft in the repo, it would be public and wrong.

**Brock Walters:** So help me understand how that's not a problem.

**Aida Knezevic:** Right, I think in that case, because it can be indexed by Google, I think, I mean, I'm not like a GitHub expert.

**Brock Walters:** Those things.

**Brock Walters:** Well, all I'm saying is that there's text on the internet somewhere.

**Brock Walters:** Forget that it's in GitHub.

**Brock Walters:** You know, it's the same text that we would publish on the website, but it's in Markdown.

**Brock Walters:** I'm assuming that the robot, the crawlers are sophisticated enough to extract Markdown to make it, you know, useful as training data.

**Brock Walters:** So all I'm saying is I don't think we should have a public version of the article that's wrong, that's not going to be edited, if we're not going to use it.

**Brock Walters:** But maybe I'm overthinking it.

**Aida Knezevic:** really dumb question.

**Aida Knezevic:** Can we delete something from a public repo in GitHub?

**Brock Walters:** Yeah.

**Brock Walters:** Yes.

**Aida Knezevic:** So in that case, I recommend deleting it, even though it's not your domain.

**Aida Knezevic:** probably like a GitHub, GitHub really only, I think, ranks in Google for very specific, like complex technical queries.

**Brock Walters:** Right.

**Brock Walters:** That's just not how we use it.

**Aida Knezevic:** We use it for everything.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** So I don't think the content would rank for those specific keywords, but it being publicly available on Google, I would still prefer to just take it down.

**Aida Knezevic:** If we're not going to publish it, we'll just make a note of it in Airtable and we can take it down.

**Brock Walters:** Okay.

**Brock Walters:** I mean, I'll have to check and see if that is actually, I mean, typically we don't delete issues.

**Brock Walters:** We close issues.

**Brock Walters:** Um, they can be deleted, but I, I don't necessarily have the mojo to do that, but that's precise.

**Brock Walters:** Okay.

**Brock Walters:** So

**Brock Walters:** That's basically why I'm asking about it, is because if they can't be deleted, then what?

**Erik O'Brien:** Right?

**Brock Walters:** And maybe I'm making a bigger deal out of this than it needs to be, but it doesn't make any sense to me that we would effectively be publicly publishing content that we're not going to use.

**Brock Walters:** And I realize that it's Fleet's way of doing things that is the cause of this problem.

**Brock Walters:** I'm not saying you guys are.

**Brock Walters:** It's we do everything in the open.

**Brock Walters:** So if we keep our drafts in the open, how does that fit with your system?

**Brock Walters:** That's really what I'm asking about.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Because the alternative is just using Google Docs.

**Brock Walters:** Yeah.

**Brock Walters:** Ugh.

**Brock Walters:** Oh my God.

**Brock Walters:** Okay.

**Brock Walters:** You just said my two least favorite words in the whole universe.

**Brock Walters:** I hate Google Docs almost more than anything.

**Brock Walters:** Okay.

**Brock Walters:** Thank you so much, you guys.

**Brock Walters:** I will keep working on this and I'm sorry.

**Brock Walters:** Sorry for being so particular, but I really do think this is working well, and I think we're going to get it to a place where it's more automated and working great.

**Aida Knezevic:** So looking forward to continuing.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Thank you, Brock.

**Aida Knezevic:** We'll see you next week.

**Erik O'Brien:** Bye.

**Erik O'Brien:** Thanks, Brock.

**Erik O'Brien:** Bye.
