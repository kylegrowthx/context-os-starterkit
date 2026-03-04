# CMs Daily Standup – Atlas Sync

<metadata>
date: 2025-06-25
time: 15:31 UTC
duration: 26 minutes
organizer: Matthew Panzarino (matthew@growthx.ai)
participants: Matthew Panzarino, Mariana Marins, Tiandra Burns, Rachel Pasche, Ademilade Shodipe-Dosunmu, Jenn Peters, Moses Agbonmabi, Jürgen Linde, Saskia Wartnaby, Usman Ghani, Sydney Go, Carrie Chowske
fathom_recording_id: 70469563
fathom_url: https://fathom.video/calls/334901096
share_url: https://fathom.video/share/xZCa93qLzLGZGBcwe1MBJvYQCjwvrU3Q
source: fathom
enriched_on: 2026-03-03 00:32 UTC
</metadata>

---

## Summary

GrowthX's content management team discussed critical Atlas workflow bugs and optimization strategies during their daily standup. The engineering team is actively fixing the disappearing workflow outputs issue, and Matthew Panzarino provided guidance on reducing word count through outline adjustments, handling title case conversions via writing guidelines, and restructuring XML export workflows for client feedback cycles. The Ask AI feature is newly deployed (4 days old) and will improve in speed as feedback is gathered.

---

## Context

This is a daily standup for GrowthX's content management team using Atlas, the company's core content generation and workflow platform. Attendees include content creators, content strategists, and Matthew Panzarino (product lead). The meeting occurred on June 25, 2025, during active product development — the engineering team had deployed live updates that morning, which caused some system instability for users in Nigeria time zones. This meeting serves as a feedback loop: CMs report blockers, feature requests, and bugs; Matthew collects these and advocates to the engineering team for fixes or enhancements. The Ask AI feature mentioned is extremely new (deployed only 4 days prior), representing ongoing product iteration on the editing and feedback tooling within Atlas.

---

## Relevance

**To GrowthX Delivery:**
- Workflow bug (disappearing outputs) is a high-impact blocker affecting multiple CMs; engineering aware and actively fixing
- Word reduction workflow needs structural redesign at outline/guidelines stage, not post-processing with Ask AI — ask AI on finished drafts strips internal links
- Title case headers need to be enforced at writing guidelines level or custom pipeline level, not manually with Ask AI after generation
- Custom client pipelines coming soon (Kirkland building these) to handle rigid structural requirements without affecting standard workflows

**To GrowthX Product (Atlas):**
- Ask AI feature is alpha-stage (4 days old) and will improve on speed; users currently chunking documents and processing takes 1-2 minutes per full document
- Request for staging environment to test features before production deployment — currently causing user disruption during live updates
- Human review feature for publishing workflows has some remaining bugs but mostly fixed; monitoring needed
- XML export workflow needs documentation for clients requesting post-feedback export without full re-run

**To GrowthX Business Development:**
- ArtsRapid client (handled by Rachel Pasche) requires XML outputs and complex feedback integration — potential expansion if custom pipeline tooling works well
- One custom client (Ademilade's account) has specific structural requirements that Kirkland is building a dedicated pipeline for — signals demand for flexible output formats

---

## Overview

- Engineering team is actively addressing the disappearing workflow outputs bug; performance has improved since the morning update
- Word count reduction should happen at outline and writing guidelines stage, not via Ask AI post-processing, which strips internal links
- Title case enforcement should happen via writing guidelines or custom pipelines, not manually with Ask AI on finished articles
- Ask AI feature is newly deployed (4 days old) and will become faster as it matures and receives feedback
- XML export workflows for clients requiring feedback before final delivery can be structured by pausing at the internal links step
- Staging environment for testing features is in progress but complex to set up; engineers are prioritizing production fixes first
- Human review feature for publishing workflows is mostly operational with minor remaining issues

---

## Key Topics

### Atlas Bug Fixes and Updates

  - Engineering team is addressing the issue of disappearing workflow outputs
  - Some users experienced difficulties during live updates, but performance has improved
  - Human review feature was added to workflows, particularly useful for publishing steps

### Workflow Optimization Strategies

  - For reducing word count, Matthew recommends tackling length at the outline and writing guidelines stage before generating the article draft:
      - Limit the number of H3 sections in the outline
      - Specify word count targets per section in the outline or guidelines
      - Remove spurious sections (compare/contrast, case studies, troubleshooting) that commonly balloon length
      - Do not use Ask AI for major word-count reduction on complete articles — it rewrites content and strips internal links
  - For title case to sentence case conversion on headers:
      - First approach: embed sentence case instructions into the brief structure or writing guidelines to enforce it during generation
      - Second approach: request a custom pipeline from Kirkland if the client requires rigid formatting on every article
      - Avoid post-processing entire articles with Ask AI, which is slow and breaks links

### Feature Requests and Improvements

  - Request for ability to reformat revised content into XML without re-running entire workflow
  - Suggestion to create a staging area for developers to test new features before deployment
  - Ask AI feature is expected to become faster as it's currently in an early implementation stage

### Client-Specific Workflow Adjustments

  - Custom pipelines are being created for clients with specific structural requirements
  - Kirkland is working on implementing templates for custom client needs

---

## Action Items

**Matthew Panzarino (GrowthX)**
- Investigate whether title case headers are hard-coded into brief/workflow generation backend
- Coordinate with Kirkland on custom pipeline for Ademilade's client requiring sentence case enforcement
- Work with engineers on Ask AI feature speed improvements and link preservation (low priority)
- Follow up with Timmy on staging environment feasibility for feature testing

**Ademilade Shodipe-Dosunmu (GrowthX)**
- Prompt an LLM to generate sentence case instruction block for writing guidelines (4-5 sentences of do/don't rules)
- Add generated instruction block to writing guidelines and test in regeneration
- Follow up with Kirkland on custom pipeline build, and ask if custom pipeline can enforce sentence case natively

---

## Transcript
**Matthew Panzarino:** Okay.

**Matthew Panzarino:** I am in the office in Lake Tahoe meeting room.

**Matthew Panzarino:** So hello, everyone.

**Matthew Panzarino:** This meeting is being recorded.

**Matthew Panzarino:** What's everybody seeing?

**Matthew Panzarino:** I noticed we had some bugs this morning.

**Matthew Panzarino:** The eng team has noticed the issue with workflows.

**Matthew Panzarino:** Um, or with the outputs disappearing.

**Matthew Panzarino:** So they're working on that.

**Matthew Panzarino:** Um, I noticed there's some tickets filed, but they're aware of it.

**Matthew Panzarino:** So, um, aside from that, happy to chat about anything.

**Matthew Panzarino:** Uh, what do you got going on?

**Mariana Marins:** We have a pretty recent question on our channel from Elvis.

**Mariana Marins:** Has anyone had to import from Atlas to Airtable yet? Not really sure how to map every column since Atlas output is just one text markdown block.

**Mariana Marins:** Nobody has answered.

**Mariana Marins:** It was like 15 minutes ago.

**Mariana Marins:** So guys, have you had to import this yet?

**Matthew Panzarino:** There's probably a couple of answers to that, by the way.

**Matthew Panzarino:** I mean, people can talk about how they're doing it now, but the Airtables all need to be adjusted anyway.

**Matthew Panzarino:** So, you know, we're probably going to have a new format for that pretty quickly here, which will allow us then to, you know, map it to whatever outputs we're getting in Atlas currently.

**Matthew Panzarino:** But as far as existing workflows, how people are dealing with those, happy to yield the floor.

**Rachel Pasche:** Yeah, I have one, like, kind of relevant question that I was going to maybe...

**Rachel Pasche:** Submit a ticket for it, but for one of my clients, want ArtsRapid, they want to convert all of their stuff into an XML file, but the problem is, right now, the way the workflow does is it runs everything through the workflow, and then it converts it to an XML file, which is fine, but the client always, always gives a ton of feedback.

**Rachel Pasche:** And there's no way to then take their feedback, like the new updated article that's been revised, and then paste that into the output, and then have an updated XML generation, if that makes sense.

**Matthew Panzarino:** Okay, so can we get, I mean, which version are we giving them to edit?

**Matthew Panzarino:** Are we giving them just a rich text version to edit?

**Rachel Pasche:** No, I mean, they're getting just like a normal, like, Google Doc.

**Matthew Panzarino:** Okay.

**Rachel Pasche:** And then they make a bunch of changes, and then I usually take those changes, and I would paste them into, like, the final output column and air table.

**Rachel Pasche:** But now what I'm doing is I'm re-running everything.

**Rachel Pasche:** Everything, just to see if I can, I don't know, figure out a way to make it work, but I didn't know if there was, like, if that was even an option to submit a ticket for it, it'd be like, I need to basically redo the output for every article.

**Matthew Panzarino:** Do you need to redo it, or do you need to just...

**Rachel Pasche:** Paste it.

**Matthew Panzarino:** Like, reformat it into XML?

**Rachel Pasche:** I just need to reformat their final revised version into XML, yeah.

**Rachel Pasche:** And the way that the workflow's configured right now, it doesn't really make sense, because it's just configuring the first draft into XML, which isn't super helpful.

**Matthew Panzarino:** Okay, so I guess there's two questions before I offer a solution.

**Matthew Panzarino:** So, the current workflow's first draft, article draft, is in XML?

**Matthew Panzarino:** Like, you can get an XML download of it?

**Rachel Pasche:** Yeah, like, it's at the very end of the pipeline.

**Matthew Panzarino:** Oh, the end, so the output is XML.

**Rachel Pasche:** Yeah.

**Matthew Panzarino:** Currently, in...

**Matthew Panzarino:** In Atlas.

**Matthew Panzarino:** Okay, and that is technically what you need to deliver to them, which is probably why that exists.

**Matthew Panzarino:** yeah, like on paper.

**Matthew Panzarino:** Right, but then you need to get feedback from them.

**Matthew Panzarino:** So you deliver them an XML for edits, or you deliver them something earlier from the pilot?

**Matthew Panzarino:** Okay, so you give them, what step do you give them?

**Rachel Pasche:** Let's see.

**Rachel Pasche:** This is more relevant.

**Rachel Pasche:** I don't know if Ishmael or Rebecca is on this call, because I'm handing it off to them, but I figured I would troubleshoot this.

**Rachel Pasche:** It's for them.

**Matthew Panzarino:** What client was it again?

**Rachel Pasche:** I'm so sorry.

**Rachel Pasche:** You mentioned it.

**Rachel Pasche:** Rapid.

**Matthew Panzarino:** Sorry.

**Matthew Panzarino:** Thank you.

**Rachel Pasche:** So I'm giving them, right now, I would give them the internal links step.

**Rachel Pasche:** would take that, I would copy it, I'd put it in a Google Doc.

**Rachel Pasche:** Okay.

**Rachel Pasche:** And then would send it to Rapid, and then they always have a bunch of feedback, and then I would need to then, I guess I could just pause it at internal links.

**Matthew Panzarino:** I'm sure I don't know how to do this.

**Matthew Panzarino:** Yeah, and then give the feedback.

**Matthew Panzarino:** there, don't let it go, and then just put it back in there.

**Matthew Panzarino:** Sorry.

**Matthew Panzarino:** I'm like.

**Matthew Panzarino:** Thinking out loud in the chat.

**Matthew Panzarino:** Yeah, I think that's one of the solutions I would offer.

**Matthew Panzarino:** So I think you already got there.

**Matthew Panzarino:** You can just offer them that output.

**Matthew Panzarino:** And then that's your process for Rapid.

**Matthew Panzarino:** You get feedback, they get it, you paste it in, and then you run the final output to get the deliverable, you know, the XML.

**Matthew Panzarino:** The other option would be if you give them that item and they make changes and you're like, I don't really need to do anything further.

**Matthew Panzarino:** Like, I don't need to paste it back into the workflow to get an XML.

**Rachel Pasche:** You can just have it reflowed as an XML using an external tool for now.

**Matthew Panzarino:** And then we can have a specific workflow that does the XML output.

**Matthew Panzarino:** But it sounds like that's what the output does.

**Rachel Pasche:** So I don't know that we need to do anything.

**Rachel Pasche:** It already exists, right?

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** So I would say your take is probably the right take.

**Matthew Panzarino:** Just go ahead and give them the feedback from that step.

**Matthew Panzarino:** Pause all your workflows at that step for your batch.

**Matthew Panzarino:** And then say, hey, here's the output.

**Matthew Panzarino:** You know, let us know if you have any feedback, whatever.

**Rachel Pasche:** Once it goes through that process, paste it back in.

**Rachel Pasche:** Run the final output and give it to them.

**Rachel Pasche:** Okay, cool.

**Rachel Pasche:** Sorry.

**Rachel Pasche:** Yeah, sometimes it takes talking it out to figure it out.

**Matthew Panzarino:** So it's all good.

**Rachel Pasche:** Thank you.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** All right.

**Matthew Panzarino:** Anyone else come up with anything or come across anything?

**Tiandra Burns:** I have a question.

**Tiandra Burns:** So I am running the workflow and it gives me so many words.

**Tiandra Burns:** So I use the ask AI function to like reduce the word count, but then I lose all of the links that have been interlinked in that original output.

**Tiandra Burns:** And then when I, I tried to go back and paste the reduced version into the add internal links and I'm not fine.

**Tiandra Burns:** It's, it's generating like regenerating the article again.

**Tiandra Burns:** Like it's not taking my, my input.

**Tiandra Burns:** So is there, maybe anyone has found a way to.

**Tiandra Burns:** Take a reduced input that doesn't have the links into the link section to get the relating?

**Matthew Panzarino:** Okay, so that's a two-parter, really.

**Matthew Panzarino:** One part is, like, how you're going about reducing the length, and then the second part is, okay, can we regenerate links, you know, based on input or to have an external input for the internal link generation workflow.

**Matthew Panzarino:** So, part one is really, I think, more important.

**Matthew Panzarino:** I think the links need to be reduced before you're generating your draft, or as you're generating your draft.

**Matthew Panzarino:** So, your article draft, you're already seeing that it's too long at that point, right?

**Matthew Panzarino:** It's not, like, magically getting longer between article draft and internal linking.

**Matthew Panzarino:** So, I would say your best bet is to make sure that you're nailing your draft length by adjusting either your writing guidelines or your outline.

**Matthew Panzarino:** And if you need help doing that, you know, personally, we can do that, right?

**Tiandra Burns:** We can get a working session.

**Matthew Panzarino:** We mess around with it.

**Matthew Panzarino:** But, um...

**Matthew Panzarino:** So there are ways to reduce that length by limiting the number of H3s used, by specifying word count in writing instructions, or specifically specifying word counts per section in outline.

**Matthew Panzarino:** You can do some work there.

**Tiandra Burns:** The major way to do it, though, is deleting unnecessary sections in the outline.

**Matthew Panzarino:** You know, sections that are just spurious that you're obviously reducing the length for some reason, right?

**Matthew Panzarino:** But LLFs do not work well when you ask them to sort of include a certain number of topics or sort of, you know, outline of, hey, you know, cover these subjects, right?

**Matthew Panzarino:** And then you tell it to reduce the length overall.

**Matthew Panzarino:** It tends to just absolutely crush context.

**Matthew Panzarino:** So it'll take, you know, mash things together and delete them.

**Matthew Panzarino:** And the reason the links go away is most likely because it's rewriting everything.

**Matthew Panzarino:** And then it's like the links are no longer either relevant or even if they were relevant, it's already rewritten that sentence.

**Matthew Panzarino:** So I'm not surprised that that's happening.

**Matthew Panzarino:** So I'm not shocked.

**Matthew Panzarino:** I'm like, wait, what?

**Matthew Panzarino:** That's supposed to work?

**Matthew Panzarino:** No.

**Matthew Panzarino:** Understandable, right?

**Matthew Panzarino:** However.

**Matthew Panzarino:** The second part of that, so the first part is, let's figure out how to get your length in the ballpark before you hit the internal linking step.

**Matthew Panzarino:** Because the internal linking step is really, I hesitate to use this term because we've used it before in other contexts, but it's really post-processing, right?

**Matthew Panzarino:** Like you're done writing the article.

**Tiandra Burns:** Yeah, exactly.

**Matthew Panzarino:** So I think that it's important to get the major structural changes done before that step.

**Matthew Panzarino:** And I think that's true forever.

**Matthew Panzarino:** Like I don't think that it's like, oh man, there's a bug or we should adjust this so that we can make quality changes and internal links will remain.

**Matthew Panzarino:** Because I actually think that's a much more complex recursive flow that's not really that necessary if we nail the link before we get there.

**Matthew Panzarino:** we nail the major structural issues.

**Matthew Panzarino:** And I'm not talking about like, hey, reflow these bullets in the narrative and then maybe you need to add a link to that.

**Matthew Panzarino:** You know, that's different.

**Matthew Panzarino:** But the second part of it is the part that you talked about where you use the tool and the links go away.

**Matthew Panzarino:** I think it is worth explaining.

**Matthew Panzarino:** at least the idea of asking whether that tool can preserve links.

**Matthew Panzarino:** I will talk to them about it, see what's up.

**Matthew Panzarino:** I don't have high hopes on that because of the things that I mentioned.

**Matthew Panzarino:** know, it'll be frozen.

**Matthew Panzarino:** It's unlikely to retain those, but we can, I'll see what's up.

**Tiandra Burns:** But yeah.

**Tiandra Burns:** did try, I did try quickly to see if it would just like ask AI, like, can you make this more concise and keep the links?

**Matthew Panzarino:** And it didn't do it, so.

**Tiandra Burns:** Yeah, I'm not, I'm not too shocked.

**Matthew Panzarino:** Yeah, that's a good, good attempt for sure, but I didn't do that.

**Matthew Panzarino:** Yeah, so I think we, we can concentrate on trying to nail the major length issues before it gets to a draft or out, the draft output.

**Matthew Panzarino:** Or when you get a draft output and you're like, holy cow, you know, this is double the length that needs to be.

**Matthew Panzarino:** We can figure out how to tackle that.

**Matthew Panzarino:** There are a handful of ways that I can help you with that.

**Matthew Panzarino:** There's, I've had some success using some prompting, which.

**Matthew Panzarino:** Go, obviously, into writing guidelines because those do get applied at draft.

**Matthew Panzarino:** But also the major successes are with just taking a tight rein on the outline to make sure that it doesn't include extraneous sections that can balloon the length of it.

**Matthew Panzarino:** It does a lot of, there's a lot of, like, compare and contrast, case studies, common troubleshooting.

**Matthew Panzarino:** Like, these sections it loves to put near the end, right before the conclusion, that you can usually get rid of without too much issue.

**Matthew Panzarino:** Depending on the client, what they exactly want.

**Matthew Panzarino:** But that, I feel, has had more success with that.

**Matthew Panzarino:** So we can experiment with that.

**Tiandra Burns:** Okay.

**Tiandra Burns:** Thank you.

**Ademilade Shodipe-Dosunmu:** Hi, Panza.

**Ademilade Shodipe-Dosunmu:** I actually ran into something similar that Tiandra ran into.

**Ademilade Shodipe-Dosunmu:** But in this case, I was just trying to change, like, title case.

**Ademilade Shodipe-Dosunmu:** I mean, change from title to sentence case across board.

**Ademilade Shodipe-Dosunmu:** And using the Ask AI feature.

**Ademilade Shodipe-Dosunmu:** And super.

**Ademilade Shodipe-Dosunmu:** That was when it took a while, like a minute or two to actually process.

**Ademilade Shodipe-Dosunmu:** And the second was that like after I processed, like all the links were taken out.

**Ademilade Shodipe-Dosunmu:** I mean, this is something I typically would do and just put it in an LLM or do it manually.

**Ademilade Shodipe-Dosunmu:** All right.

**Ademilade Shodipe-Dosunmu:** I need to process much faster.

**Ademilade Shodipe-Dosunmu:** And since we said that the Ask AI feature is essentially just making calls on LLM, I guess my question is that is it going to get faster?

**Ademilade Shodipe-Dosunmu:** Because now I just find myself taking the output because I spend most time editing the article brief and the outline.

**Ademilade Shodipe-Dosunmu:** So the final version is, you know, I would say maybe 70 to 80 percent there.

**Ademilade Shodipe-Dosunmu:** So I now spend most time, you know, just taking it outside of the grid and like just editing it manually or using Claude or something.

**Ademilade Shodipe-Dosunmu:** Right.

**Ademilade Shodipe-Dosunmu:** And I know that the Ask AI feature is supposed to be that feedback flow, right, so that we don't have to take work out of the grid.

**Ademilade Shodipe-Dosunmu:** So my question is, is that feature going to get faster?

**Ademilade Shodipe-Dosunmu:** Right.

**Ademilade Shodipe-Dosunmu:** Or is this sort of where it's peaking at?

**Matthew Panzarino:** Yeah, no, it will get faster.

**Matthew Panzarino:** I mean, this is a, I would basically say you're using an alpha version of the feature.

**Matthew Panzarino:** You know, that's kind of like, it's just, it literally got implemented four days ago, right?

**Matthew Panzarino:** So it will get better, for sure.

**Matthew Panzarino:** But it will take feedback, right?

**Matthew Panzarino:** Or I shouldn't say we, I'm saying we, the engineers will take feedback.

**Matthew Panzarino:** I have nothing to do with it.

**Matthew Panzarino:** But I mean, we will, my job is to like, service these things or encourage you to service them.

**Matthew Panzarino:** So I definitely would say, file a ticket on the speed.

**Matthew Panzarino:** Because I think it's, it's like, hey, this is a low priority ticket, but it takes a lot of time for it to do something very simple.

**Matthew Panzarino:** However, when you say it loses the links, you're reprocessing the entire document with it?

**Ademilade Shodipe-Dosunmu:** Is that what you're doing?

**Ademilade Shodipe-Dosunmu:** Yeah, I'm highlighting the entire document, hey, know, change all of this to sentence case and all the links are gone.

**Matthew Panzarino:** That's going to take a lot of time, always, because it's reprocessing an entire doc.

**Matthew Panzarino:** So what it does is it sends it out and chunks it into pieces, and then it works on each chunk and runs a pass on each one.

**Matthew Panzarino:** Each one's going to take 30 seconds or so, and so it adds up, right?

**Matthew Panzarino:** So I don't know that that's actually the best use case for that.

**Matthew Panzarino:** What are you specifically changing from title to sentence case?

**Ademilade Shodipe-Dosunmu:** That's pretty much headers, like, oh, hey, change over the headings to, you know, sentence case or something like that.

**Matthew Panzarino:** There's, okay, there's probably, this is probably best tackled at writing guidelines.

**Matthew Panzarino:** So let me take a look at that, or we can chop up on that and chat a little bit about changing your writing guidelines to a scenario that gives you those sentence case, H3s and H2s, instead of you having to change them afterwards.

**Matthew Panzarino:** Because anything you do over and over again really needs to be ingrained in the prompt, right?

**Matthew Panzarino:** The writing guidelines or the brief or the, you know, something earlier in the flow.

**Matthew Panzarino:** So if you have...

**Matthew Panzarino:** You do this in every article.

**Matthew Panzarino:** That's not ideal.

**Matthew Panzarino:** These feedback tools like the AI assist tool or any other tool that we implement really should be looked at as fixing edge cases or one-offs or, you know, little things that are just persistent that we can't get rid of yet.

**Matthew Panzarino:** We haven't figured out how to nail, you know, with the prompting.

**Matthew Panzarino:** So I would say let's go earlier in your flow and figure out how to get it to produce sentence case titles for you across the board using your brief or outline, you know, or at the worst case scenario, article draft and using the writing guidelines to do that.

**Matthew Panzarino:** So let me investigate that.

**Matthew Panzarino:** This may be a scenario where we need to, because I'm almost positive that title case H2s and H3s are like hard code, you know, into the brief and generation workflow behind the scenes.

**Matthew Panzarino:** So let me get with Kirkland and ask him about that and see whether they are, it's like forcing that function.

**Matthew Panzarino:** If it is, that's okay.

**Matthew Panzarino:** We can probably overwrite it still somehow.

**Matthew Panzarino:** But if it's not, then I think we need to concentrate on the prompting.

**Matthew Panzarino:** If it is, there's a couple of options.

**Matthew Panzarino:** There's like a couple of branching pathways.

**Matthew Panzarino:** Either we create a new workflow that's specifically for this client that is like a new pipeline or just your current pipeline in a way where we're patching your pipeline to say, hey, this client needs sentence case titles.

**Matthew Panzarino:** We're not applying this as a universal rule across all of our accounts.

**Matthew Panzarino:** But for this one, we need to make that adjustment.

**Matthew Panzarino:** Or we need to figure out like an additional step, which basically says like, hey, rip the H2s and H3s and then replace them with sentence case versions of them.

**Matthew Panzarino:** So let me investigate that.

**Matthew Panzarino:** We can dig in that a little bit.

**Matthew Panzarino:** For now, in a very quick thing you can do like right after this call or while you're waiting, I would say go into your writing instructions and embed.

**Matthew Panzarino:** that instruction.

**Matthew Panzarino:** Actually, don't just go write it in there.

**Matthew Panzarino:** Prompt an LLM to give you an instruction on how to tell an LLM to generate sentence case.

**Matthew Panzarino:** And then, you know, it will probably be a block of about four sentences of instruction.

**Matthew Panzarino:** Do this, don't do that.

**Matthew Panzarino:** You know, here's what I want you to do.

**Matthew Panzarino:** Do this, don't do that.

**Matthew Panzarino:** Please enforce this.

**Matthew Panzarino:** And then put that in your writing instructions and see and regenerate and see what happens.

**Matthew Panzarino:** that's what you can do right now and see, you know.

**Ademilade Shodipe-Dosunmu:** Okay, I would, I'll try that out.

**Ademilade Shodipe-Dosunmu:** I have found a bit of mixed success with putting that in like the brief.

**Ademilade Shodipe-Dosunmu:** Yeah.

**Ademilade Shodipe-Dosunmu:** Because I started like adding it to the brief like, oh, hey, you know, this is how it should be structured.

**Ademilade Shodipe-Dosunmu:** Because like I typically take out the entire proposed at school structure with my own.

**Ademilade Shodipe-Dosunmu:** And in that structure, all the headings are like in sentence case.

**Ademilade Shodipe-Dosunmu:** And it typically retains that information in the output flow.

**Ademilade Shodipe-Dosunmu:** So that's the only workaround I've found so far.

**Ademilade Shodipe-Dosunmu:** But I think I'll try putting it in the guidelines to see whether it retains that to our knowledge, know.

**Matthew Panzarino:** Yeah, I guess there's another question that just came up with what you said, which is that do you need a specific structure for every article you produce for them?

**Ademilade Shodipe-Dosunmu:** I mean, for one of my clients, yes, I do.

**Ademilade Shodipe-Dosunmu:** And I have filed a ticket for that.

**Ademilade Shodipe-Dosunmu:** I'm giving Kirkland all the templates that he needs for the custom pipeline.

**Ademilade Shodipe-Dosunmu:** So that's still a work in progress.

**Matthew Panzarino:** Okay, that's great.

**Matthew Panzarino:** And is that the same client that needs sentence case or no?

**Ademilade Shodipe-Dosunmu:** Yes, that one needs sentence case.

**Ademilade Shodipe-Dosunmu:** Because you might want to mention that to him.

**Matthew Panzarino:** I was going to say, you might want to mention that to him and say, like, hey, can you also force sentence case on this?

**Matthew Panzarino:** I don't know if he's able to do that in that step, but I just want to throw that out there since he's already kind of building you a custom structure and it has to be the same every time.

**Matthew Panzarino:** And, you know, sentence case has to be the same every time.

**Matthew Panzarino:** So you might want to see what's up there because and then he also that will also engage him on the question of whether or it's like sort of hard coded.

**Matthew Panzarino:** Like, oh, well, you know, our workflows basically force everything.

**Matthew Panzarino:** And that's okay if they do.

**Matthew Panzarino:** It just means the writing guidelines have to fix it, right?

**Matthew Panzarino:** They have to correct for it after the fact instead of it just coming out of the brief or outline step with those already in place.

**Matthew Panzarino:** So I would say concentrate on, like, updating with that and then concentrate on the writing guidelines for yourself to see if that can course correct.

**Ademilade Shodipe-Dosunmu:** Okay, thank you.

**Matthew Panzarino:** Yeah, yeah, but once again, with your scenario, reflowing the entire article with the tool is not really as intended.

**Matthew Panzarino:** It'll strip links, it'll do, you know, other things.

**Matthew Panzarino:** It's very rare that I think we should reflow the entire piece.

**Matthew Panzarino:** If we do, then we're going to need to figure out a solution for, like, re-adding those internal links and stuff like that.

**Matthew Panzarino:** But remember, you can use that tool at any step, which means you can use it before the internal linking as well, you know.

**Matthew Panzarino:** So if there's that's messing around with this, you can do it at the article draft before you run the internal linking flow, fix those major structural issues.

**Matthew Panzarino:** And DeAndre, this is also something like a hack, you know, you can just...

**Matthew Panzarino:** And...

**Matthew Panzarino:** If need to reflow the whole piece using that tool for some reason, do it at the draft before you run the internal linking, because the internal linking is really post-processing.

**Matthew Panzarino:** So, cool.

**Matthew Panzarino:** Yeah, thanks, Eddie.

**Ademilade Shodipe-Dosunmu:** Thanks.

**Matthew Panzarino:** Yeah, yeah.

**Matthew Panzarino:** Any other questions?

**Matthew Panzarino:** Stuff that's come up?

**Matthew Panzarino:** No?

**Matthew Panzarino:** Everything running so smooth, you can't believe it?

**Matthew Panzarino:** No issues at all?

**Jenn Peters:** It's amazing.

**Jenn Peters:** think feedback from one of my CMs who couldn't make this call today was just that last night was pretty rough, and there were a lot of, and, you know, I think that's when a lot of updates were happening, and I asked her to just, like, check in with me in the morning when she logged back on, like, her time, Nigeria time, and she said, things are so much better this morning, and that, obviously, a lot of the, like, delays and...

**Jenn Peters:** Troubles she was having were likely related to the updates they were doing live while she was trying to actually run stuff.

**Jenn Peters:** So today seems a lot better for her team so far.

**Matthew Panzarino:** Okay, good.

**Matthew Panzarino:** Yeah, I believe that's true.

**Matthew Panzarino:** The way that it works is that if they're working on the front end or anything that's you facing, they will ship it at some point and you can still use the old version.

**Matthew Panzarino:** And then when you refresh the page, it'll present you with a new interface and the new, you know, new features, so to speak.

**Matthew Panzarino:** But if they're working on something architectural in the back end, you won't even notice and stuff will start failing and stuff.

**Matthew Panzarino:** But that's just the way it goes.

**Matthew Panzarino:** she's getting all thrown in with weird, like, blank screens and stuff.

**Jenn Peters:** And I was like, I don't think this is a you, you know, situation.

**Jenn Peters:** Yeah, it's a lot better for her.

**Jenn Peters:** Okay, cool.

**Jenn Peters:** Yeah.

**Moses Agbonmabi:** The only issue I add, I already have tabled it in the Atlas channel, but I think it's really working fine right now.

**Moses Agbonmabi:** How's that?

**Moses Agbonmabi:** Not an issue with my workflows moving on to the next step, but it's working better now.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** The human review feature was one that Daniel added for a variety of reasons, not the least of which is that some of the publishing, some of the workflows have a publishing step, and we would want, you know, human intervention before we sent something to staging or to publishing.

**Matthew Panzarino:** And I think, I'm sure, rolling that out was probably like, oh, you know, I rolled it out and then need to issue some fixes, which I think he already did.

**Matthew Panzarino:** So if you see further issues with it, though, no.

**Matthew Panzarino:** All right.

**Matthew Panzarino:** Cool.

**Matthew Panzarino:** Well, I'm available.

**Matthew Panzarino:** Oh, yeah.

**Matthew Panzarino:** Timmy.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Go ahead.

**Matthew Panzarino:** Hello?

**Matthew Panzarino:** Yes.

**Matthew Panzarino:** I can hear you.

**Timmy:** Okay.

**Timmy:** Okay.

**Timmy:** Um, so I wanted to suggest a staging area or some sort of.

**Timmy:** demo area for developers to just kind of test new features because the other day I was working, I generated like a series of articles and then I just kind of lost the connection out of the version of change.

**Timmy:** So maybe they could have a vision area where they're just kind of testing versions of features and that would be really nice.

**Matthew Panzarino:** Yeah, no, I agree.

**Matthew Panzarino:** It's definitely something that I mentioned to them.

**Matthew Panzarino:** I'm advocating for it as well.

**Matthew Panzarino:** I think that there was just some complexity in getting a prod and staging environment set up while they were doing this transition because it basically had to spin up a complete copy of the developer environment and then run a pipeline, know, introduce a new pipeline.

**Matthew Panzarino:** It's like, okay, into prod, out of prod, or sorry, into testing, out of staging, into prod, and like they were just trying to get Atlas up and running.

**Matthew Panzarino:** But I think that that will exist.

**Matthew Panzarino:** But I will take that as well in my next kind of round of chats and make sure that we advocate for it again because I agree.

**Matthew Panzarino:** You know, if we're going to ship stuff, we should have it tested or have a staging environment that's like, hey, run your workload on stage and make sure everything works good.

**Matthew Panzarino:** And then we're going to ship it to prod tomorrow or whatever the case may be.

**Matthew Panzarino:** So I'll update you if they tell me they're going to do that or they say it's never going to happen.

**Matthew Panzarino:** I'll also give you that so you can build expectations.

**Matthew Panzarino:** But we'll hopefully get there.

**Matthew Panzarino:** But I think right now everybody's just trying to fix everything on the fly as fast as possible, which will result in some weirdness.

**Matthew Panzarino:** But yeah, sorry about the lost work on the grid.

**Matthew Panzarino:** But it hopefully won't happen too much.

**Matthew Panzarino:** All right.

**Matthew Panzarino:** Anything else going on?

**Matthew Panzarino:** All right.

**Matthew Panzarino:** All right.

**Matthew Panzarino:** Well, I'm around.

**Matthew Panzarino:** So let me know.

**Matthew Panzarino:** Keep going, plugging away.

**Matthew Panzarino:** If we have any issues or any updates that need to be done, I'm happy to help back it up or articulate or figure out whether it's something that we can fix, you know, in process instead of an eng, or if it's something that should be filed, a ticket should be filed and stuff.

**Matthew Panzarino:** okay.

**Matthew Panzarino:** Thanks, folks.

**Matthew Panzarino:** Thank you.

**Matthew Panzarino:** Ciao, ciao.
