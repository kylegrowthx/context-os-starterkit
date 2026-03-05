# Training - Article gen grid walkthrough

<metadata>
date: 2025-06-05
time: 14:59 UTC
duration: 54 minutes
organizer: usman.adepoju@growthx.ai
participants: Vivek Shankar, Nika Narimanidze, Usman Adepoju
fathom_recording_id: 66704280
fathom_url: https://fathom.video/calls/317918124
share_url: https://fathom.video/share/XmR4EzSuso51jzpAy99roy_jzBRUYuU_
source: fathom
enriched_on: 2026-03-03 02:45 UTC
</metadata>

---

## Summary

Vivek Shankar trained Nika and Usman on GrowthX's article generation grid process, covering the complete workflow from assignment brief through feedback and fact-checking. The training emphasized connecting audience pain points to product solutions via Claude-generated outlines, and introduced a new Galileo/Prophecy workflow that enriches outlines with insights from podcast and webinar transcripts before grid input. The team identified a critical engineering defect: H3 headers are not properly formatted in the grid's article generation output, requiring a workaround using Claude for immediate article generation while engineering addresses the issue.

---

## Context

This is a training session led by Vivek Shankar (GrowthX) for Nika Narimanidze and Usman Adepoju, both from GrowthX Labs (the Galileo/Prophecy arm). The meeting demonstrates GrowthX's content production system—specifically the data grid workflow that powers article generation for clients like Galileo, Prophecy, and DataGrid. The GrowthX Labs team is new to the full process and needs to implement it consistently across their clients. Vivek walks through the complete grid architecture, the strategic importance of assignment briefs and Claude-based outline generation, and a newly-introduced enrichment step using podcast/webinar transcripts for clients with proprietary knowledge sources. The session also flags a major technical problem: the grid's article generation output is dropping H3 headers, forcing the team to use Claude as a workaround.

---

## Relevance

- **To GrowthX Delivery:** Establishes standardized SOP for article grid workflow—pain-point-driven outline generation with Claude, assignment brief as the foundation, and feedback loops for polishing. New enrichment step using podcast/webinar transcripts adds depth for Galileo and Prophecy articles. Updated internal documentation reflects new process as the authoritative SOP.

- **To GrowthX Business Development:** Demonstrates consistent, repeatable content production across multiple clients (Galileo, Prophecy, DataGrid). Highlights team capacity to scale: Nika and Usman now trained on full grid workflow, reducing dependency on Vivek for individual article reviews. Identifies engineering gap (H3 formatting defect) that impacts output quality and requires engineering bandwidth.

- **To CheckThat / AEO:** Grid workflow applies pain-point-driven content strategy as core methodology. Podcast/webinar enrichment step leverages proprietary knowledge (Prophecy's webinars) to strengthen topical authority and AI visibility positioning. Updated process creates repeatable framework for high-quality, authority-focused content across clients.

---

## Overview

- The article generation process emphasizes connecting audience pain points to the topic and product solution
- Outline creation should involve using AI tools (like Claude) strategically to develop targeted, audience-specific content structures
- New step added for Galileo/Prophecy: Enriching outlines with insights from podcast/webinar transcripts before grid input
- Major grid defect identified: H3 headers not being properly formatted/included in article generation output

---

## Key Topics

### Article Generation Grid Overview

  - Key columns: keyword/title, company context, assignment brief, research, outline, title gen, article gen, polishing instructions
  - Assignment brief is crucial - spend most time here as it's the foundation for the outline
  - Outline should be viewed/edited in code, not markdown
  - Polishing instructions incorporate style guide and client-specific requirements

### Strategic Outline Development Process

  - Use Perplexity for initial research on existing content
  - Leverage Claude for creative outline development:
      - Specify audience (e.g. AI architects in mid-size to enterprise companies)
      - Define Claude's role as experienced content strategist
      - Identify key audience pain points related to the topic
      - Generate outline addressing pain points and connecting to product solution
  - Aim for \~5 main sections in a 1500-2000 word article

### Podcast/Webinar Insight Integration

  - New step for Galileo/Prophecy: Analyze relevant podcast/webinar transcripts
  - Use Claude to identify opportunities to enrich outline with transcript insights
  - Add relevant points as writer instructions in the assignment brief

### Grid Defect and Workaround

  - Major issue: H3 headers not properly formatted/included in article generation
  - Temporary solution: Generate article in Claude, to be reviewed later
  - Urgently flagged to engineering team for resolution

---

## Action Items

**Nika Narimanidze (GrowthX Labs)**
- Flag H3 formatting issue in grid as urgent defect to engineering team
- Generate DataGrid article in Claude due to grid H3 formatting issue

**Vivek Shankar (GrowthX)**
- Update internal SOP documentation with new article gen process (including podcast enrichment step)
- Drop link to training video in internal board channel and delete older SOP video

**Usman Adepoju (GrowthX Labs)**
- Practice new article gen process with existing Galileo data and podcasts; follow Vivek's exact process
- Work with Ismail on podcast transcription grid training (Ismail to share details separately)

---

## Transcript
**Vivek Shankar:** So obviously, both of you guys, you kind of know how the grid works.

**Vivek Shankar:** Usman, you know, hopefully you reviewed Jess's call where she kind of explained what each column does.

**Vivek Shankar:** So I thought I'll first run over the way the grid is and just give a quick overview on what each column does.

**Vivek Shankar:** And then we can maybe run through a sample article and you guys can just stop me for questions and what not along the way.

**Vivek Shankar:** So I'm using data grid over here as an example.

**Vivek Shankar:** I think it's one of the latest grids.

**Vivek Shankar:** So that's the reason.

**Vivek Shankar:** So the first column, keyword, company name, company context is pretty straightforward.

**Vivek Shankar:** Name, the context, we get it from Notion.

**Vivek Shankar:** The keyword, it says keyword, but you can also put in the article title over here, as you guys know.

**Vivek Shankar:** So then we run the assignment brief.

**Vivek Shankar:** The Brief is maybe the most important part of this whole thing.

**Vivek Shankar:** This is where we want to be spending the most of our time.

**Vivek Shankar:** And the Assignment Brief is the base from which the outline is created.

**Vivek Shankar:** The whole document is editable.

**Vivek Shankar:** So you can go in and type whatever you want and do all of that.

**Vivek Shankar:** So the Research Domain Blacklist, if there's any websites you don't want, the flows referring to, you can put them in here.

**Vivek Shankar:** I usually put Wikipedia and stuff like that.

**Vivek Shankar:** But generally, you can leave it blank as well.

**Vivek Shankar:** It's fine.

**Vivek Shankar:** And then the Research Gen is basically whatever you have specified in the Assignment Brief.

**Vivek Shankar:** The Research Flow will research only that.

**Vivek Shankar:** So for example, we have this material over here.

**Vivek Shankar:** The Research Flow will take all of this.

**Vivek Shankar:** It will find other articles that talk about this or any other information.

**Vivek Shankar:** And it will focus only on what you've specified.

**Vivek Shankar:** And then once that is done, you run the outline.

**Vivek Shankar:** And the outline basically blows up the assignment brief that we had.

**Vivek Shankar:** Something important is you always want to view this in code, not in markdown.

**Vivek Shankar:** And again, this is editable, but we only want to edit it in code.

**Vivek Shankar:** Some of the other pods, what they do is create an outline in GPT or Claude, and then they paste it into this.

**Vivek Shankar:** I advise against doing that because we should not be creating our outlines outside of the grids.

**Vivek Shankar:** It just increases the complexity needlessly.

**Vivek Shankar:** If you want to make changes to the outline, if your outline is incorrect at whatever point, go back to the assignment stage and something has gone wrong there.

**Vivek Shankar:** So just create a new row and then run the whole thing again and then come back to your outline.

**Vivek Shankar:** So we just make sure we review it.

**Vivek Shankar:** Outline.

**Vivek Shankar:** One thing to note is this word count always needs to be changed in the introduction.

**Vivek Shankar:** It usually puts like 200 words in the intro.

**Vivek Shankar:** just want to be something like that.

**Vivek Shankar:** And we'll just run through it, just make sure everything is fine.

**Vivek Shankar:** This final CTA section, don't pay too much attention to it.

**Vivek Shankar:** I'll just demonstrate in the process.

**Vivek Shankar:** I think I'll show you guys this, but I'll just demonstrate.

**Vivek Shankar:** We can just copy-paste some of the assignment flow directly into the article.

**Vivek Shankar:** So we don't need to pay too much attention to this.

**Vivek Shankar:** The next thing is the title gen.

**Vivek Shankar:** So when you run the title gen workflow, it gives you a choice of five titles.

**Vivek Shankar:** Personally, I don't pay much attention to it.

**Vivek Shankar:** I just pick any one of those and I worry about defining titles later.

**Vivek Shankar:** So just pick one and make sure that it's in here.

**Vivek Shankar:** Then there's the article gen.

**Vivek Shankar:** Usman, you've probably never seen this before, but this is how the grid is supposed to run.

**Vivek Shankar:** You run the article, it sort of writes.

**Vivek Shankar:** article for you.

**Vivek Shankar:** And this first output is not the finished product, right?

**Vivek Shankar:** We have a new column here, polishing instructions.

**Vivek Shankar:** These polishing instructions are basically what we will use to define the article to make sure that it fits the client's style guidelines, right?

**Vivek Shankar:** So, Nika, have no idea where you got this from, but it looks good.

**Vivek Shankar:** So, yeah, nice work there.

**Vivek Shankar:** you.

**Vivek Shankar:** Yeah, have no idea where you brought this from.

**Vivek Shankar:** Like, I don't think we have this in Notion.

**Vivek Shankar:** So, I think...

**Vivek Shankar:** No, we don't have this.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** We didn't have this before, yeah.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Can you put this in Notion as well, please?

**Vivek Shankar:** Because just for future reference.

**Vivek Shankar:** You said to put this in Notion, right?

**Nika Narimanidze:** I lost you.

**Vivek Shankar:** Yeah, yeah.

**Vivek Shankar:** No worries, yeah.

**Vivek Shankar:** So, anyway, so this is where we put in the style guide and, like, it just says what kind of tone we should be using, what kind of language we should be using.

**Vivek Shankar:** What

**Vivek Shankar:** These kinds of examples that we're giving, this is really helpful, you know, for the flows generally.

**Vivek Shankar:** Some of the other pods, what they do is they list a little table, they say, do this, do not do this, like good example, bad example, you can do that as well.

**Vivek Shankar:** But generally over here, we want to be pasting the style guide instructions and any additional instructions that the client may have given us.

**Vivek Shankar:** For our clients, we don't have this, but for some of the other pods, okay, so a of a context.

**Vivek Shankar:** Galileo has a style guide, so we can just post that, we can just copy paste that in here.

**Vivek Shankar:** The style guide is in motion.

**Vivek Shankar:** So just a bit of context, some of the other pods, when you hear them talking about the polishing instructions, or even when Matthew Panzarino talks about polishing instructions.

**Vivek Shankar:** That's of So using you can mean, mean, I'm sure.

**Vivek Shankar:** I

**Vivek Shankar:** He'll, I think he's mentioned this on calls.

**Vivek Shankar:** Usman, he hasn't had a call with you as yet, but basically he'll mention this on call and he'll say something like, take all the instructions that you've given to indie LLMs about editing your articles so far and combine that into polishing instructions.

**Vivek Shankar:** That advice I don't think applies to us because what happened is during the calibration phase and when initially the clients were making edits to our articles, I was updating the style guides in Notion to make sure that we always had a source of truth in there.

**Vivek Shankar:** So there's nothing outside of Notion that we need to add, right?

**Vivek Shankar:** So anything that you need to add for polishing instructions, everything is already there in Notion.

**Vivek Shankar:** You don't need to sort of go anywhere else to sort of copy-paste stuff.

**Vivek Shankar:** And the advice applies to you.

**Vivek Shankar:** As well, as and when you notice client edits coming in, please notice what the edits are like, and then we can update Notion as well, the style guide, so that our polishing instructions are always updated.

**Vivek Shankar:** Notion, anybody can come in and just run the grid, that's the idea.

**Vivek Shankar:** We don't want specialized content sitting somewhere in Slack or some such thing.

**Vivek Shankar:** So anyway, so once you give the polishing instructions, the post-processing takes polishing instructions into account.

**Vivek Shankar:** It also takes this into account, all this information, which is the company context, into account.

**Vivek Shankar:** It just makes sure that the information we're writing is sensible.

**Vivek Shankar:** And then it'll give you this meta description, meta title.

**Vivek Shankar:** Again, personally, I don't pay attention to these, because we just need to modify them afterwards.

**Vivek Shankar:** So then you'll get the final article, and this is where the, I would say, the next important step begins.

**Vivek Shankar:** You need to read through this article, right?

**Vivek Shankar:** So everybody has different ways of doing this.

**Vivek Shankar:** Personally, what I do is I read this article right in here.

**Vivek Shankar:** So if I say like, okay, I see this.

**Vivek Shankar:** I don't really like what this looks like.

**Vivek Shankar:** I then go into the feedback and I just, oh, wow.

**Vivek Shankar:** I just sort of type in, right?

**Vivek Shankar:** Like I'm just going to give an example over here.

**Vivek Shankar:** And again, this is a text column.

**Vivek Shankar:** So you can just say, why is it not editing?

**Nika Narimanidze:** That's odd.

**Vivek Shankar:** Oh, it's weird.

**Vivek Shankar:** Oh, there you go.

**Vivek Shankar:** Okay.

**Vivek Shankar:** So, yeah.

**Vivek Shankar:** So you can just type in like, you know, change the header name, whatever, XYZ, to, I don't know, PQR, right?

**Vivek Shankar:** So these instructions that you give is literally like an LLL.

**Vivek Shankar:** So imagine you're looking at the article in Claude or GPT, and you're telling it, listen, change this, change that, etc.

**Vivek Shankar:** So you can see Nika has given a bunch of sort of examples over here.

**Vivek Shankar:** I can see you've provided the polishing instructions all over again.

**Nika Narimanidze:** because I felt that he didn't follow the polishing instructions and just copy-pasted it.

**Nika Narimanidze:** Okay, no worries.

**Vivek Shankar:** Just a reminder, if we give things like cut the word count to 1,800, LLMs cannot count, right?

**Vivek Shankar:** Yeah, it has not done it.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** So generally, the word count, if you want to reduce things in feedback section, if you feel like it's far too long, the best option, I would say, is either cut information yourself manually.

**Vivek Shankar:** If you feel that the tone is off or that the article is not good, just do a rewrite.

**Vivek Shankar:** Like, just read.

**Vivek Shankar:** Menderate the article.

**Vivek Shankar:** Because from the feedback flow, the idea is, and I don't know if Jess mentioned this on her call, but the idea of the feedback flow is to reduce and to make small changes.

**Vivek Shankar:** It is not to rewrite the entire article.

**Vivek Shankar:** It does not do that well, right?

**Vivek Shankar:** So if you think of it this way, if you want to expand something, you do it in the assignment flow.

**Vivek Shankar:** If you want to reduce or make small changes, you do it in the feedback flow, right?

**Vivek Shankar:** So mass deletion of a section, changing the header format from sentence case to title case or title to sentence, these kinds of things it does well.

**Vivek Shankar:** It will change individual sentences well.

**Vivek Shankar:** But if you tell it, rewrite the entire article in this one, it won't do a good job of that.

**Vivek Shankar:** So what I'm saying is generally, if you feel like it hasn't followed these things correctly, something has gone wrong in the polishing side of things.

**Vivek Shankar:** Thank you.

**Vivek Shankar:** And that is a fault in the grid that we need to flag to the engineering team, right?

**Nika Narimanidze:** Vivek, sorry for jumping in.

**Nika Narimanidze:** This means that we have to run the new row and start the process again, right?

**Nika Narimanidze:** Or just use Claude, just identify what's overextended or what just cut short and run on it?

**Nika Narimanidze:** I would just rewrite it.

**Vivek Shankar:** So you can rewrite it either using a new row.

**Vivek Shankar:** In this case, since you felt that the grid did not follow polishing instructions well, that is a defect.

**Vivek Shankar:** And you have to let the engineering team know.

**Vivek Shankar:** And you can tell them, like, in this grid, in this particular row, you know, these are the polishing instructions.

**Vivek Shankar:** It's not followed it.

**Vivek Shankar:** And you can give them a few examples of how it's not followed it.

**Vivek Shankar:** Like, yeah, what I've done in this case, I used Claude just to make it more...

**Nika Narimanidze:** You're good.

**Nika Narimanidze:** Yeah.

**Vivek Shankar:** You can take a call as to how you want to fix it.

**Vivek Shankar:** But generally, my point is, my broader point here, is that anything that goes wrong with the grid is a defect.

**Vivek Shankar:** And we have to log defects.

**Vivek Shankar:** I'm not a fan of going into Cloud and doing things because we need to treat this as a product.

**Vivek Shankar:** So do let the engineering team know at the very least.

**Vivek Shankar:** So, yeah.

**Vivek Shankar:** And then, so that's basically the feedback, right?

**Vivek Shankar:** So just keep in mind that we don't, if you tell the feedback flow to rewrite this article in this zone or something like that, it won't do a good job of it.

**Vivek Shankar:** It will mess it up.

**Vivek Shankar:** So you have to just, it's a defect, log it, right?

**Vivek Shankar:** So the next thing is, you run the feedback flow and it gives you the...

**Vivek Shankar:** Final with Feedback, and then this is where you kind of look at it and sort of go through it, right?

**Vivek Shankar:** So just read through the whole thing, just make sure that it makes sense.

**Vivek Shankar:** Then after that, you run the internal linking flow.

**Vivek Shankar:** I think in this, there's a database ID.

**Vivek Shankar:** I don't think we need to map that anymore.

**Vivek Shankar:** Yeah, this is a new one.

**Vivek Shankar:** So these ones will be automatically link, run linking to, you know, the pages for the client itself.

**Vivek Shankar:** And then there's a fact checker flow.

**Vivek Shankar:** The fact checker, I mean, it sort of verifies whether we're saying the right things.

**Vivek Shankar:** It makes sure there's no hallucinations in here and that sort of thing.

**Vivek Shankar:** So that's what the fact checker does.

**Vivek Shankar:** Any questions about all of this?

**Vivek Shankar:** Any doubts?

**Vivek Shankar:** Any questions about all of this?

**Usman Adepoju:** Any questions?

**Usman Adepoju:** Any questions?

**Usman Adepoju:** But I think Jess mentioned that at the beginning, what she wants to do is make sure that the article is that bulky so that you can review the contents and like the feedback.

**Usman Adepoju:** So she said that don't review the word count or don't specify what counts when you're still like in the video and the assignment based on the outline.

**Usman Adepoju:** But just let it go as far as it can go first and it can have condenses.

**Usman Adepoju:** I think she also shared the prompts for the condenses that she said David came up with or something.

**Vivek Shankar:** Yeah, mean, I do agree with the notion that we should limit the assignment brief.

**Vivek Shankar:** Like in the assignment brief over here, we don't want to be giving word counts or setting any sort of limit.

**Vivek Shankar:** Instead, what the problem is that sometimes what happens is if you you have to impose a limit at some point.

**Vivek Shankar:** Because if you go to the LLM and say, you know, let's say you're at the outline stage.

**Vivek Shankar:** I think that by the outline stage, you have to absolutely impose some sort of word count.

**Vivek Shankar:** So the way the LLM works is it doesn't count.

**Vivek Shankar:** Let me go to the code view.

**Vivek Shankar:** It won't count to 120 words, right?

**Vivek Shankar:** What it does is it estimates this word count.

**Vivek Shankar:** It knows for sure that 120 words is less than 300.

**Vivek Shankar:** So it kind of approximates and it says that, okay, this thing needs to be about, I don't know, 10 sentences or whatever.

**Vivek Shankar:** Right.

**Vivek Shankar:** So if you don't put this limit on the introduction, you're going to increase the burden on yourself for editing.

**Vivek Shankar:** And what happens is I can give it the LLM, this same instruction, and I can say word count 120 and I can say word count 12,000.

**Vivek Shankar:** It will still generate text for both.

**Vivek Shankar:** For 12,000, it will follow all of this and it will just generate like, I don't know, a thousand paragraphs.

**Vivek Shankar:** Something like that.

**Vivek Shankar:** And the result is you'll have a lot of fluff, which you cannot manually edit.

**Vivek Shankar:** So at the assignment brief level, don't impose any word counts or whatever, but by the time you reach the outline, definitely have word counts, because you also have to keep the final product in mind, right?

**Vivek Shankar:** Like you cannot have a massive, you know, we had this problem in the past, whereas the grid would generate like, I don't know, 4,000 words or whatever, right?

**Vivek Shankar:** And we'd have to edit those 4,000 words down to like 1,200 words.

**Vivek Shankar:** It's impossible to do that because, you know, even in an LLM, even if you put it in Claude, it's impossible.

**Vivek Shankar:** It takes more time to edit those articles than to generate a new one, right?

**Vivek Shankar:** So think about it in that way.

**Vivek Shankar:** And generally though, I will say the sentiment applies, that at the assignment stage, want to blow it up at the feed.

**Vivek Shankar:** XH, you want to reduce.

**Vivek Shankar:** So that's how it goes.

**Vivek Shankar:** Does that answer your question, Gaurd?

**Vivek Shankar:** Yeah, it does.

**Nika Narimanidze:** Thank you.

**Nika Narimanidze:** Vivek, just a quick question about word count.

**Nika Narimanidze:** Like, I know it depends on specific article, but what's the minimal word count that we want to make in terms of SEO?

**Nika Narimanidze:** Because sometimes these topics are too narrow and too niche specific.

**Nika Narimanidze:** So that's why I'm asking.

**Nika Narimanidze:** Let them be as long as they need to be.

**Vivek Shankar:** If they're too niche specific, let it be as big as it needs to be.

**Vivek Shankar:** For most SEO content that actually has keywords.

**Vivek Shankar:** And I think neither of you is writing content that actually has keywords.

**Vivek Shankar:** But if we have specific keywords, take a look at competitor articles and we get an idea of what the word should be.

**Vivek Shankar:** General rule of thumb is between 1500-2000 words is a sweet spot.

**Vivek Shankar:** So now you can go to 2100-2200 words, but you

**Vivek Shankar:** You don't want to be hitting like 2,500 and 3,000 words.

**Vivek Shankar:** That's too much, right?

**Vivek Shankar:** Yeah, of course.

**Nika Narimanidze:** And when it comes to like non-keyword specific blocks, let's say 1,000 to 1,200, is it okay?

**Vivek Shankar:** That's fine.

**Vivek Shankar:** If the topic is covered well, and if we're not missing anything, it's fine.

**Nika Narimanidze:** Yeah, okay.

**Nika Narimanidze:** Got it.

**Nika Narimanidze:** Thanks.

**Nika Narimanidze:** All right.

**Vivek Shankar:** So let's just quickly run through this one article here, which is this one, curate, don't create.

**Vivek Shankar:** It's the first row.

**Vivek Shankar:** So it's kind of, this is one of those articles that does not have a, you know, a keyword or anything of that sort.

**Vivek Shankar:** So that's why, you know, it's a good test to like use perplexity, use Claude and see how we can build something.

**Vivek Shankar:** So basically put this in here and then the first step is, you know, you just run the assignment brief, just let it run.

**Vivek Shankar:** there's no need need to.

**Vivek Shankar:** to go.

**Vivek Shankar:** Interfere.

**Vivek Shankar:** Meanwhile, we go into perplexity.

**Vivek Shankar:** This is what I usually do in here, you know, and this is your prompt.

**Vivek Shankar:** I'm writing an article about this.

**Vivek Shankar:** My audience is this.

**Vivek Shankar:** Definitely always mention the audience.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Give me an outline.

**Vivek Shankar:** Right.

**Vivek Shankar:** The way perplexity works is it is a research engine to see what is already being written.

**Vivek Shankar:** Right.

**Vivek Shankar:** So the perplexity outline only gives you what's already existing.

**Vivek Shankar:** Our job is to improve on this.

**Vivek Shankar:** We cannot copy paste this outline.

**Vivek Shankar:** Right.

**Vivek Shankar:** So as a first step, just digest it.

**Vivek Shankar:** Right.

**Vivek Shankar:** So the idea here is you want to learn something.

**Vivek Shankar:** You don't have to become an expert on the topic, but learn something about the topic.

**Vivek Shankar:** Right.

**Vivek Shankar:** So it says that, okay, introduction, brief overview of knowledge management challenge, knowledge management dilemma.

**Vivek Shankar:** Okay.

**Vivek Shankar:** So this tells me there's a bit of a pain point here.

**Vivek Shankar:** Knowledge management is a bit of an issue.

**Vivek Shankar:** Right.

**Vivek Shankar:** Then it says, Curate, Don't Create, the Strategic Shift, how AI agents benefit from curated knowledge, how to build a curated knowledge base, how to maintain common pitfalls, case studies, actionable, blah, blah, blah, whatever.

**Vivek Shankar:** So you can see just from the titles itself, there's a bit of a flow to this.

**Vivek Shankar:** It introduces me to the pain point, and then it gives me the solution, which Curate, Don't Create.

**Vivek Shankar:** Then it says, the impact of it, or the benefits of curated knowledge for AI agents.

**Vivek Shankar:** Then it says, how to build, then it says, how to maintain common pitfalls, how to avoid, and then conclusion, right?

**Vivek Shankar:** So I have a bit of an idea here.

**Vivek Shankar:** Now, you can go and cloud, and then you can sort of, I would say, play around with cloud a bit, because it's a bit more creative than perplexity, obviously.

**Vivek Shankar:** So what I did is, you know, I did the same thing as in perplexity, right?

**Vivek Shankar:** Same prompt.

**Vivek Shankar:** And it just gave me pretty much the same

**Vivek Shankar:** Same outline as perplexity.

**Vivek Shankar:** It added this extra stuff, implementation, patterns, strategic knowledge, but basically it's the same thing, right?

**Vivek Shankar:** What you actually want to be doing is you want to tell Claude to evaluate your outlines like an experienced content strategist.

**Vivek Shankar:** Most importantly, make sure you tell it to think objectively and tell you where the outline is weak, right?

**Vivek Shankar:** So what I have done in this instance is I've broken up multiple steps into different prompts.

**Vivek Shankar:** What I suggest you guys do is go into Claude, tell it your audience, tell it the role it should play, right?

**Vivek Shankar:** So the audience in this case is AI architects in, you could say, I don't know, data grids, target, company sizes, you know, mid-sized companies, I would say mid-sized to enterprise companies.

**Vivek Shankar:** The AI agent architects in mid-size two enterprise companies, which is actually a very big audience, but anyway, the role the LLM must play is that of an experienced content strategist, it can think strategically, and it can think objectively, right?

**Vivek Shankar:** It should not agree with you just for the sake of it.

**Vivek Shankar:** So make sure you say those things.

**Vivek Shankar:** If you do not say these things, it will just make some  up, right?

**Vivek Shankar:** And it will just keep confirming your biases.

**Vivek Shankar:** So you want it to think for you, right?

**Vivek Shankar:** So make sure you tell it all of that, and then ask it to give you an output, right?

**Vivek Shankar:** So we can actually put that to the test here.

**Vivek Shankar:** So what I can say is, like, you know, my, or no, I can say, I take an article about, you can just take this thing here.

**Vivek Shankar:** they don't don't create whatever.

**Vivek Shankar:** All

**Vivek Shankar:** My audio series.

**Vivek Shankar:** So the first step is really we want to make sure that we capture the pain point for this audience, right?

**Vivek Shankar:** So what I would say is give me a few in points of this audience that tie to this topic, right?

**Vivek Shankar:** Let's see what it gives us.

**Vivek Shankar:** The reason we go after pain points is because, as I said, in the process, in the internal pod channel, it really helps you find.

**Vivek Shankar:** It avoids a situation where you're writing 3,000, 5,000 word e-books, right, in the name of the plot.

**Vivek Shankar:** So it says, like, you know, it's giving us all of these things, like there's all these pain points that these people face.

**Vivek Shankar:** Usually, you know, it's given us like six pain points, which is a lot.

**Vivek Shankar:** So you can ask it, like, what is the most pressing pain point?

**Vivek Shankar:** Right.

**Vivek Shankar:** Go ahead.

**Vivek Shankar:** If you think something, and hopefully it gives us just, like, one result.

**Vivek Shankar:** Okay.

**Vivek Shankar:** So it says a knowledge, accuracy, accountability trap, right?

**Vivek Shankar:** Here's why it's a personal risk, no escape route, whatever.

**Vivek Shankar:** Read all of this because it's important.

**Vivek Shankar:** It'll also help you understand how to connect the topic to the audience, right?

**Vivek Shankar:** So now, using this pain point, we want to structure.

**Vivek Shankar:** So the article should basically provide a solution to this pain point, and insert data grid, which is our product, as a solution.

**Vivek Shankar:** So we're connecting three things here.

**Vivek Shankar:** So the way to do it is, would say, so given this pain point, and your role as, you know, And I'm repeating this, experienced content strategist who can think objectively.

**Vivek Shankar:** Can you guys see my prompt, or typing, or is it too, okay.

**Vivek Shankar:** Yes, yes, we can see it.

**Vivek Shankar:** The reason I'm repeating this role as experienced content strategist is because sometimes it forgets it, right.

**Vivek Shankar:** So I'm saying, given this pain point and your role, give me an outline for this topic, right.

**Vivek Shankar:** For this audience, just making sure.

**Vivek Shankar:** Let's see what it does.

**Vivek Shankar:** So you can see it's changed the title to something pain point related.

**Vivek Shankar:** And this is actually a good title because if it shows up in that search engine results page, you can imagine like, okay, I'm an AI agent architect.

**Vivek Shankar:** I'm searching for something.

**Vivek Shankar:** I want to see something that relates to my problems.

**Vivek Shankar:** Right.

**Vivek Shankar:** So he's us all of this, the accuracy, accountability crisis, and you know, whatever.

**Vivek Shankar:** Why custom knowledge creation makes you the expert.

**Vivek Shankar:** These are good ideas.

**Usman Adepoju:** Sorry.

**Usman Adepoju:** ofase, sure.

**Vivek Shankar:** So… … That's

**Vivek Shankar:** Early, nice ideas, very specific.

**Usman Adepoju:** Yeah.

**Vivek Shankar:** So then curated knowledge, accountability, shield, whatever, architect's guide, building your liability, protections, selling to leadership.

**Vivek Shankar:** This is a very nice section.

**Vivek Shankar:** This is, again, a pain point that, you know, they daily face.

**Vivek Shankar:** Implementation playbook, long-term career protection.

**Vivek Shankar:** Again, this is maintenance, basically.

**Vivek Shankar:** So you can see, like, when we go back to this complexity outline, right, it's the same sections that even Claude is proposing.

**Vivek Shankar:** But you can see how the angle has changed.

**Vivek Shankar:** And the angle is everything, right?

**Vivek Shankar:** Why custom knowledge expert makes you the expert versus curate don't create the strategic shift, right?

**Vivek Shankar:** Like, this particular heading, or section as it's proposed, it's very general.

**Vivek Shankar:** It can apply to anybody.

**Vivek Shankar:** I don't know who this applies to, but if I look at this, I've given it, you know, audience knowledge.

**Vivek Shankar:** I've given it, like, I've basically told it, this is the pain point.

**Vivek Shankar:** This is what I'm trying to solve.

**Vivek Shankar:** You can see how much more specific these things are, like the curated knowledge, accountability shield.

**Vivek Shankar:** Some of these names are a little over the top, but whatever.

**Vivek Shankar:** You know, defensible knowledge sourcing and all this stuff, like, you know, building a curated...

**Vivek Shankar:** That is this section, building a curated knowledge base for AI agents, right?

**Vivek Shankar:** That is this section right here.

**Vivek Shankar:** Building your liability protection architecture, all this stuff, right?

**Vivek Shankar:** So you can see how far we've come from the premise, right?

**Vivek Shankar:** We've come from curate, don't create.

**Vivek Shankar:** That is Aerox.

**Vivek Shankar:** We've come from curate, don't create, how to build knowledge for your AI agents, to...

**Vivek Shankar:** Oh, AI.

**Vivek Shankar:** And, you know, avoid career-ending, knowledge liability, and all this.

**Vivek Shankar:** And it is still the same topic.

**Vivek Shankar:** So the last step in building this is just saying, you know, what you want to do is like, we don't want to give the, what's it called?

**Vivek Shankar:** Well, so my issues with this outline, so, okay, let me take a few steps back.

**Vivek Shankar:** So as good as this outline is, my feeling is it's still a little too long.

**Vivek Shankar:** It has like eight sections, right?

**Vivek Shankar:** We're targeting between, say, around 2,000 words max.

**Vivek Shankar:** Eight sections is a bit much, right?

**Vivek Shankar:** So you can say, like, my article is going to be between 1,500 2,000 words long.

**Vivek Shankar:** So...

**Vivek Shankar:** Say, like, this outline for an article that length, something else I would say is like, replace the bullets in each section with paragraphs containing the guidelines, yeah.

**Vivek Shankar:** Because I think the R flows kind of read this better, it's just, it's just something that, it's a feeling.

**Vivek Shankar:** I don't have any data to back this up.

**Vivek Shankar:** But you can see it's giving you writing, like, open with a specific visceral, whatever, shift, right?

**Vivek Shankar:** And it's mentioning the word count as well.

**Vivek Shankar:** So, you can see, like, 300, 400, that's 7.

**Vivek Shankar:** This is, this brings us to 1,200.

**Vivek Shankar:** This is 16.

**Vivek Shankar:** This is 18 to 19, and then after this we'll have the data grid call out section.

**Vivek Shankar:** So basically we have five sections now, right?

**Vivek Shankar:** And again, personally, I don't think building long-term career protection is the right angle here.

**Vivek Shankar:** Personally, I would change this because it's getting a little too scary, right?

**Vivek Shankar:** So I would probably change this to just be like, you know, how to maintain your implementation or how to maintain your, you know, custom knowledge base.

**Vivek Shankar:** So the point again is you need to still think, you can't just outsource everything to the AI.

**Vivek Shankar:** So basically this is a decent outline.

**Vivek Shankar:** What I would do is I would take all of this and then paste it into Aerox over here, right?

**Vivek Shankar:** Thanks.

**Vivek Shankar:** Thanks.

**Vivek Shankar:** Thanks.

**Vivek Shankar:** So in our assignment brief, first thing again, just a reminder, as Nika has correctly done here, we need to change the target audience, first and foremost.

**Vivek Shankar:** The target keyword, you know, for data grid and all this, like, I don't think it's that big of a deal, but for clients like Prophecy and Ramp, we do have target keywords.

**Vivek Shankar:** So just make sure that the keywords are kind of present.

**Vivek Shankar:** If you want to add extra keywords, just add it as bullets.

**Vivek Shankar:** You don't have to add all the search volume competition, whatever.

**Vivek Shankar:** Just add it in here.

**Vivek Shankar:** And then for this proposed content structure, basically, I'll replace this whole thing, right, with what was in the cloud with this stuff.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Oh, Nika left for some reason.

**Vivek Shankar:** So, um, oh, he's back.

**Nika Narimanidze:** Yes.

**Nika Narimanidze:** No worries.

**Vivek Shankar:** Um, so basically what we need to now do...

**Vivek Shankar:** This creates this particular CTA section.

**Vivek Shankar:** This is pretty straightforward, but I think both of you know how to do this.

**Vivek Shankar:** Usman, did I cover this with you?

**Vivek Shankar:** Yes, yes, we did.

**Vivek Shankar:** Okay.

**Vivek Shankar:** Do either of you want me to cover this again?

**Vivek Shankar:** I think we directly covered this.

**Nika Narimanidze:** Okay, cool.

**Vivek Shankar:** Both of you are good with it.

**Vivek Shankar:** So, awesome.

**Vivek Shankar:** So then obviously the rest of the steps, we just do it.

**Vivek Shankar:** Make sure you review the outline, make sure it's correct, et cetera.

**Vivek Shankar:** And then, you know, you just go on.

**Vivek Shankar:** And just a reminder, if the final article before the feedback gen is not to your liking, it means something is wrong in the grid.

**Vivek Shankar:** So, like that, right?

**Vivek Shankar:** We want to avoid manually doing things in Florida as much as possible, right?

**Nika Narimanidze:** Yeah, of course.

**Vivek Shankar:** So, that was pretty much it.

**Vivek Shankar:** That's the process.

**Vivek Shankar:** The main takeaways is that I wanted...

**Vivek Shankar:** I emphasize was how to think through building the article itself.

**Vivek Shankar:** I just followed the process that I sent you guys in the internal channel.

**Vivek Shankar:** Think about the pain points, think about how to connect it to the audience, and think about how you can position the product as a solution at the end, which is actually pretty simple.

**Nika Narimanidze:** And just to let you know, Usman, if you tried this today, the flow has some problems right now.

**Nika Narimanidze:** So, the flow is failing.

**Nika Narimanidze:** It appears to have error, but the tech team can see the output, and Clint has manually copied the output of assignment brief, but when I run the research, it still fails.

**Nika Narimanidze:** I don't know where to just copy, paste this from.

**Nika Narimanidze:** So, it's bit laggy and takes a while.

**Nika Narimanidze:** Yeah.

**Nika Narimanidze:** Okay.

**Usman Adepoju:** So, I think my question is, when the flow fails, when we fail for all the clients, we have to initial process.

**Usman Adepoju:** are haven't we-based want don't do that so.

**Usman Adepoju:** We don't a

**Vivek Shankar:** Well, it is technically should, but sometimes it doesn't, because each grid is kind of customized for each client.

**Vivek Shankar:** In our case, they're not super customized, but there are some programmatic grids that are very customized.

**Vivek Shankar:** Usually it's grid dependent, but generally, if you are running into an error or an issue, don't worry about what's happening for anybody else.

**Vivek Shankar:** It's just easy, just like it.

**Nika Narimanidze:** Vivek, if we finish this, like when we finish this, do you have like extra two minutes to stay?

**Nika Narimanidze:** I just wanted to share something with you.

**Nika Narimanidze:** Yeah, yeah, I can stay on.

**Nika Narimanidze:** All right.

**Vivek Shankar:** So, yeah, just reiterating again.

**Vivek Shankar:** What I just demonstrated was that process that I sent you guys at the internal channel.

**Vivek Shankar:** very much.

**Vivek Shankar:** It's very important that we start connecting pain points, right, because that gives you the entire focus.

**Vivek Shankar:** So that was pretty much it.

**Vivek Shankar:** I will drop a link to this in our internal board channel.

**Vivek Shankar:** Just make this as our article gen SOP from now on.

**Vivek Shankar:** And I'll delete the older video because I don't think it applies anymore.

**Vivek Shankar:** So, yes, any questions, any doubts or anything of that sort?

**Nika Narimanidze:** I think the process is clear.

**Usman Adepoju:** I think it's like generic by myself.

**Usman Adepoju:** Then I'll be secure, like, if there are no choice coming in my mind.

**Usman Adepoju:** But for now, nothing.

**Vivek Shankar:** Yeah, I mean, what I would do is maybe take some time today and tomorrow.

**Vivek Shankar:** Just try rerunning one of your older, one of the Galileo's that you've already submitted, right?

**Vivek Shankar:** Just try rerunning it in one of the grids in Galileo.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** So that way you...

**Vivek Shankar:** Kind of see what the difference is, and we get used to editing as well.

**Vivek Shankar:** So that's an important thing.

**Vivek Shankar:** Now that you guys are comfortable with this, there is an additional step that I would like to add, which is podcast insertion.

**Vivek Shankar:** So this is not applicable to DataGrid, but Galileo and Prophecy, they have their own podcasts, and they have their own internal source material.

**Vivek Shankar:** So we're already doing this for Prophecy, right?

**Vivek Shankar:** The way to do it is once we have this outline from Claude, what we need to do is we need to basically take...

**Vivek Shankar:** I'm trying to think how to demonstrate this to you guys.

**Vivek Shankar:** I can show you Prophecy real quick.

**Vivek Shankar:** to I can show you.

**Vivek Shankar:** you.

**Vivek Shankar:** So Usman, tomorrow I've asked Ismail to, I think he's already sent you an invite, he will go over the podcast transcription grid with you, and he'll kind of show you how to transcribe those podcasts, right, and basically for Prophecy, what we've done is Prophecy has a bunch of webinars, and these webinars have a lot of proprietary knowledge, right, so what we did is we actually scraped all of these webinars using our grids, and this is a transcript right here, right, so what you can do is, let's say I'm writing something for Prophecy, I can look at these topic names, and I can kind of figure out like, okay, this particular webinar maybe talks about those ofnature what we well, People

**Vivek Shankar:** This topic, right?

**Vivek Shankar:** So let's look at some prophecy articles to see if We can find some examples So I go into article gen.

**Vivek Shankar:** So these are the sort of topics for this week like data domains, completeness, stewardship, whatever, right?

**Vivek Shankar:** Usually, you know, Ismail has his own process which we're still kind of experimenting with in Gemini but the simple process is basically look at the titles of these webinars or podcasts and paste, say like, okay, this particular thing here which is, I don't know, self-service, future of data transformation I think this webinar will have some good information

**Vivek Shankar:** To enrich my existing article, right?

**Vivek Shankar:** So you click on it, open this, and then you can just search for like, self-service, okay, here.

**Vivek Shankar:** So what I do is, I just copy, paste the entire transcript.

**Vivek Shankar:** I don't know, it continues.

**Vivek Shankar:** So let's say I take this entire transcript, right?

**Vivek Shankar:** And then I come back to Claude, and I would say, analyze this webinar transcript.

**Vivek Shankar:** Tell me if there's any opportunities to enrich the above outline with the information in this init, right?

**Vivek Shankar:** All

**Vivek Shankar:** So let's say, I mean, in this case, I don't think it will find anything, but because we're using Prophecy, Webinar, and DataGrid article, let's paste it, and let's see what it says, right?

**Vivek Shankar:** So usually, if there is a fit, it will tell you that for this particular topic, we can enrich it with this quote, we can enrich it with this information, etc., etc.

**Vivek Shankar:** If there's no match, it will just tell you there's no match whatsoever.

**Vivek Shankar:** So that's what I'm expecting in this case.

**Vivek Shankar:** Okay.

**Vivek Shankar:** So you can see, like, it says there are many opportunities.

**Vivek Shankar:** I see several valuable opportunities.

**Vivek Shankar:** This is a good example of how the LLM bullshits you, right?

**Vivek Shankar:** And the reason it's bullshitting me right now is because I did not specify in this prompt that it needs...

**Vivek Shankar:** Think critically.

**Vivek Shankar:** It's just kind of agreeing with me, right?

**Vivek Shankar:** It thinks that I want to make a connection, so therefore it will make a connection at any cost.

**Vivek Shankar:** So now let me change the prompt, and let me say, think like, an experience.

**Vivek Shankar:** You just think objectively, do not agree with me, just for the sake of it, right?

**Vivek Shankar:** Let's see what it gives us now.

**Vivek Shankar:** The idea here is, we just want to enrich the outline with insights from the podcast itself, right?

**Vivek Shankar:** So if there are some use, you can see how it's changed, right?

**Vivek Shankar:** Exactly.

**Vivek Shankar:** Thanks.

**Vivek Shankar:** Thanks.

**Vivek Shankar:** Thank

**Vivek Shankar:** So I told it to think objectively.

**Vivek Shankar:** Useful, tactical, but no major opportunities.

**Vivek Shankar:** So that's correct.

**Vivek Shankar:** It's not there.

**Vivek Shankar:** If it was there, it would have told you where it is, right?

**Vivek Shankar:** So it would have told you like useful, tactical to consider.

**Vivek Shankar:** Let's assume that these are actually valid, right?

**Vivek Shankar:** You say Angela's point about blah, blah, blah.

**Vivek Shankar:** You can add this as a concrete example of why architects did blame for wrong information, right?

**Vivek Shankar:** So it's giving all this.

**Vivek Shankar:** So it says recommendation, don't significantly change.

**Vivek Shankar:** Add this, add this, and add this.

**Vivek Shankar:** So you can, in your next prompt, you can tell it.

**Vivek Shankar:** So add these, or you can say, add your recommendations to the outline as writer instructions.

**Vivek Shankar:** Assume, assume writer does not.

**Vivek Shankar:** I have access to the JavaScript.

**Vivek Shankar:** Explain the information for you.

**Vivek Shankar:** I'm kind of making things up at this point.

**Vivek Shankar:** Let's see what it comes to.

**Vivek Shankar:** But the idea, you get the idea.

**Vivek Shankar:** It's like, it'll give you what the insertion points is, and then you just tell it, okay, great.

**Vivek Shankar:** Give me these points.

**Vivek Shankar:** Now enrich my thing, right?

**Vivek Shankar:** So you can say it's including this multiple version of TruthSync, right, as a writer instruction.

**Vivek Shankar:** And it's giving this entire context over here.

**Vivek Shankar:** So this is kind of what we want.

**Vivek Shankar:** Because our research flow does not have access to the webinar transcripts.

**Vivek Shankar:** So we need to give full context over here.

**Vivek Shankar:** Right.

**Vivek Shankar:** And I think, Usman, this is what we need to start doing for Galileo.

**Vivek Shankar:** all their podcasts, we need to put, you know, we already have articles about

**Vivek Shankar:** Their podcasts, we need to basically put all of that into one Google Doc or repository or whatever, and every article that we're creating for next week onwards, we need to start including those insights from the podcast into these articles.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** And this is the process.

**Usman Adepoju:** So I think I've done for about 20 articles.

**Usman Adepoju:** Your what?

**Vivek Shankar:** I've done this for about 20 articles already.

**Vivek Shankar:** Yeah, those were podcast quote insertion, but those were existing articles, right?

**Vivek Shankar:** So this is a new article, and this is how your outline will finally, or not your outline, your assignment brief will kind of look like this, and you need to put this into the grid for a new article, right?

**Usman Adepoju:** Yes, instead of doing it, it's after the process.

**Usman Adepoju:** Exactly.

**Vivek Shankar:** So we do it at the beginning instead of at the end.

**Vivek Shankar:** So this is something something that...

**Vivek Shankar:** We should be doing, if we have those resources, and for Galileo, we have a ton of resources, we have like external YouTube channels, we have podcasts, their own podcasts, have external podcasts, that's what I was talking to them about last week, or this week, the previous call, that if they can help us narrow down those sources, we can enrich content using this process, right, so Nika for you, this is not applicable, because NAMP and DataGrid don't have these podcasts, whatever, but, Yeah, yeah, of course.

**Vivek Shankar:** So, that's it, any questions about any of this?

**Nika Narimanidze:** Yeah, just want to circle back to the usual process that we discussed, you know, in assignment briefs, we format headers as in H2s and H3s, and then we generate the outline, after the research, right, and in the outline, H3s are not formatted, So, Thank

**Nika Narimanidze:** Is this the fault of the grid?

**Nika Narimanidze:** Should we like this?

**Nika Narimanidze:** I know you can like easily use code and to follow this formatting and everything, but trees are not formatted.

**Vivek Shankar:** Where am I?

**Nika Narimanidze:** You can check this on DataGrid Editorial, second or third row, whatever you wish.

**Nika Narimanidze:** Not the first one.

**Nika Narimanidze:** think on the first it has followed.

**Nika Narimanidze:** And I've missed this yesterday that the formatting was not on here.

**Nika Narimanidze:** Okay, so these three hashes that it's putting in, yeah, this is a fault of the grid.

**Vivek Shankar:** We need to bring it up.

**Vivek Shankar:** Because the three hashes means this is an H3.

**Vivek Shankar:** So it needs to, yeah.

**Vivek Shankar:** Is it still considering it as an H3 though?

**Vivek Shankar:** Like when it generates the article?

**Vivek Shankar:** Is it still putting it as an H3?

**Vivek Shankar:** No Vivek, it does not.

**Nika Narimanidze:** You can check the article gen output of the second row and you see that it's just missing.

**Nika Narimanidze:** Look, it's only H2s.

**Nika Narimanidze:** Okay.

**Vivek Shankar:** All right.

**Vivek Shankar:** Yeah, I would flag this immediately.

**Vivek Shankar:** This is a big defect.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Okay.

**Nika Narimanidze:** I rerun this on the third row, but the same thing happened.

**Nika Narimanidze:** So it's a flow issue, but it wasn't just like one specific example.

**Nika Narimanidze:** Yeah, this is a bit frustrating, but okay.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** In this case, it's not even included any H3.

**Vivek Shankar:** It's just kind of...

**Vivek Shankar:** No, no, it has not.

**Nika Narimanidze:** But I will flag this, but I will just use quote because I have to deliver the article.

**Nika Narimanidze:** Is it okay?

**Nika Narimanidze:** Okay.

**Nika Narimanidze:** I think it's not a big reason just to stop at the moment.

**Nika Narimanidze:** I'm trying to think.

**Vivek Shankar:** We have two days, so I would say go ahead and generate in Claude.

**Vivek Shankar:** I'll review when I'm back on Tuesday and we'll submit it then.

**Nika Narimanidze:** Yes, go ahead and do it on Claude.

**Vivek Shankar:** I will review it when I'm back.

**Vivek Shankar:** Okay.

**Vivek Shankar:** But, yeah, let's just flag this with urgency because we can't use the grid.

**Vivek Shankar:** Okay, I'll flag this up.

**Nika Narimanidze:** Yeah, this is a big issue.

**Vivek Shankar:** We cannot use the grid if this is happening because it's missing H3s.

**Vivek Shankar:** So, yeah.

**Nika Narimanidze:** All right.

**Usman Adepoju:** I think my next question, sorry, Nika, would be, so for the sessions, we don't want to use direct quotes from podcasts, right?

**Usman Adepoju:** Oh, yeah, I'll leave it up to you.

**Vivek Shankar:** Generally, I'm...

**Vivek Shankar:** Hmm.

**Vivek Shankar:** Hmm.

**Vivek Shankar:** I'm trying to think how to best answer this.

**Vivek Shankar:** I don't have an opinion either way.

**Vivek Shankar:** I think, though, in content, given what we're trying to do, it's better to not use quotes.

**Vivek Shankar:** We can link to the podcast that we're taking the information from.

**Vivek Shankar:** But if you do find quotes in there, that's fine too.

**Vivek Shankar:** It's not a deal breaker.

**Vivek Shankar:** Just make sure the quote is, you know, in context and that it reads well.

**Vivek Shankar:** If you're in doubt, just don't use quotes.

**Usman Adepoju:** Thanks.

**Vivek Shankar:** All right.

**Vivek Shankar:** Any other questions?

**Usman Adepoju:** No, not regarding this topic.

**Nika Narimanidze:** Okay, awesome.

**Vivek Shankar:** I guess Nika and I can stay on and

**Vivek Shankar:** Yeah, Usman, do you have any questions?

**Vivek Shankar:** Drop it in the channel, send a video, whatever.

**Vivek Shankar:** And yeah, just practice with the existing data that you've sent.

**Vivek Shankar:** that, you know, and try practicing with some of the podcasts.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Like, you can, in Galileo itself, you can go to the grid.

**Vivek Shankar:** You can go to podcast article generation, this grid, here.

**Vivek Shankar:** And if you go to the, where is it?

**Vivek Shankar:** Oh, it's this one.

**Vivek Shankar:** sorry.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Transcription, this column.

**Vivek Shankar:** So this is the transcript for the podcast itself.

**Vivek Shankar:** Right.

**Vivek Shankar:** So you can practice with some of these things.

**Vivek Shankar:** So let's say you're writing something about multi-agent, you know, you can talk about challenges, can talk about psychological safety, rise of agentic systems, multimodal capabilities, talk about this, right?

**Vivek Shankar:** So try to see if there's any sort of overlap, you know, understanding multi-agent systems and orchestration.

**Vivek Shankar:** You can take this as well, right?

**Vivek Shankar:** So try practicing with this.

**Vivek Shankar:** Just go through the process, understand how the prompts work, and yeah, just play around with it.

**Vivek Shankar:** But I would say stick to the process I showed you.

**Vivek Shankar:** Once you're comfortable with the process, then you can improvise and you can change.

**Vivek Shankar:** But initially when running it, please stick to the process exactly as I've showed you.

**Nika Narimanidze:** It'll save you a lot of problems.

**Vivek Shankar:** Once you're, you know, kind of, you're

**Vivek Shankar:** Master it, then do your own thing.

**Vivek Shankar:** I have no issues.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Okay.

**Usman Adepoju:** Thanks.

**Usman Adepoju:** Okay.

**Vivek Shankar:** Thanks, Usman.

**Vivek Shankar:** Bye, Nika.

**Usman Adepoju:** Bye, Usman.

**Nika Narimanidze:** All right.

**Vivek Shankar:** Just hang on.

**Vivek Shankar:** Let me take out the motor because we need this for the SOP.

**Nika Narimanidze:** Bye,
