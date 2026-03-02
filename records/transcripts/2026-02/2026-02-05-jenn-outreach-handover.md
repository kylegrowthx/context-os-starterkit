# Jenn - Outreach Handover

<metadata>
date: 2026-02-05
time: 20:15 UTC
duration: 16 minutes
organizer: usman.adepoju@growthx.ai
participants: Jenn Peters, Usman Adepoju
fathom_recording_id: 120189403
fathom_url: https://fathom.video/calls/558491562
share_url: https://fathom.video/share/TyGzsv24z6CuFMrVbuD-23DXd9TPvPeo
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Jenn Peters handed over the Outreach client account to Usman Adepoju, covering the article refresh workflow, publishing pipeline, and internal tools. Key process points: article refreshes use a yellow/strikethrough format (a cumbersome requirement worth advocating to change), the change document pipeline handles point-by-point edits, and post-processing in Claude ensures competitive completeness since the pipeline doesn't reliably evaluate all gaps. Jenn will review all of Usman's work next week before publishing, and emphasized starting with the operational manual and product context before Monday's handoff.

---

## Context

This is an internal handover between two GrowthX content strategists. Outreach is a GrowthX content marketing client with a significant account (~$200k+/year engagement). The client runs an editorial calendar in Asana, not Airtable, and publishes articles on their own cadence after GrowthX drafts them and stages them through Suleiman. The client is currently in a strategy shift and renewal period, which creates an opportunity to propose workflow improvements. Jenn Peters has been managing the account and is transitioning it to Usman Adepoju, who will start taking on article refreshes and publishing oversight beginning the following week.

---

## Relevance

**To GrowthX Delivery:**
- Article refresh workflow uses yellow/strikethrough format for client review—a time-consuming process on both sides. Usman should advocate for switching to net-new drafts, especially given the client's strategy shift and upcoming renewal.
- Post-processing in Claude is critical since the change document pipeline doesn't reliably identify competitive gaps or catch shoehorned stats. Usman must verify all statistics and their context before publishing.
- Client publishes on own cadence and often fails to update Airtable with published URLs. Usman must manually check the blog every few days to keep the OS current for Looker dashboard updates.

**To GrowthX Business Development:**
- Outreach client is in strategy shift with renewal coming up, creating favorable conditions to propose workflow improvements and demonstrate expanded capabilities.
- Jenn's willingness to review all early work and provide feedback signals confidence in account continuity and relationship strength.

---

## Overview

- **Article refreshes require a yellow/strikethrough format** for client review, a process Usman should advocate to change to net-new drafts.
- **Use the `change document` pipeline** for refreshes, but always post-process in Claude to ensure competitive completeness.
- **Manually update Airtable with published URLs** from the client's blog, as they use Asana and often miss this step.
- **Jenn will review all of Usman's work** next week to ensure quality and provide direct feedback.

---

## Key Topics

### Article Refresh Workflow

  - **Client Requirement:** Article refreshes must use a yellow/strikethrough format to show all edits for client review.
  - **Recommended Change:** Usman should advocate for net-new drafts.
      - **Rationale:** The current format is time-consuming for both teams and makes the final article difficult to visualize.
      - **Timing:** The client's strategy shift and upcoming renewal create a good opportunity to propose this change.
  - **Pipeline Process:**
      - Use the `change document` pipeline in Outreach Atlas.
      - It generates a point-by-point list of additions (highlight yellow), deletions (strikethrough), and rearrangements.
  - **Post-Processing in Claude:**
      - **Why:** The pipeline's output is not 100% reliable for competitive completeness.
      - **How:** Use the "Outreach, post-processing" project to compare the draft against top-ranking articles and identify gaps.
  - **Fact-Checking:**
      - **Why:** The pipeline can "shoehorn" stats, misinterpreting data to fit a narrative.
      - **Action:** Always verify stats and their context in the source article.

### Client & Publishing Process

  - **Client Tooling:** The client uses Asana, not Airtable, for their editorial calendar and publishing.
  - **Publishing Flow:**
    1.  **Staging:** Articles sent to Suleiman for staging.
    2.  **Publishing:** Client publishes on their own cadence.
    3.  **Airtable Update:** Client often fails to add the published URL to our Airtable OS.
  - **Required Action:** Usman must manually check the client's blog every few days to find and add missing URLs to Airtable.
      - **Why:** This data is required for the weekly Looker dashboard update.
  - **Other Tools & Tasks:**
      - **`image only generator` pipeline:** Creates standalone images, useful for fixing incorrect titles or replacing low-quality visuals.
      - **Bottom-of-funnel CTA:** Add to all articles using the dedicated Claude project.
      - **Header Formatting:** Change all headers to sentence case, as many older articles use title case.

---

## Action Items

**Jenn Peters (GrowthX)**
- Set up Usman's edit-update automation so he receives updates on incoming article edits

**Usman Adepoju (GrowthX)**
- Review the operational manual and Timmy's video to understand the article formatting and staging workflow
- Read the product strategy, company context, and product matrix to prepare for account handoff starting Monday
- Send completed refreshes to Jenn for review and feedback before publishing during first week

---

## Transcript
**Jenn Peters:** Okay, so like if you look at this article, you'll see like there's yellow and then there's going to be like strikethroughs.

**Jenn Peters:** So Kimmy's video will explain, I'm not going to get into because it's not difficult, like but you will see it, it'll make more sense when you go through it yourself, that there is, there's like, you put all the new content in yellow and you put all the stuff that you are removing striked through because they want to see on their end, like what you're taking out and what you are at it, yeah, which is kind of annoying but it's like, you know, I can see the point as well.

**Jenn Peters:** Ideally, I've mentioned this to Joe once and I would suggest, I would suggest like kind of encouraging this in whatever way you can that it would be beneficial for both sides, for both you and for them, if you just created a net new.

**Jenn Peters:** You know, and maybe it's keeping the good stuff from the old article and maybe it's adding the new, but the pipeline is, you know, trying to do that.

**Jenn Peters:** So this business here with like, you have to, because you will wonder, you will ask yourself, how do I do this in the pipeline?

**Jenn Peters:** That is the question, right?

**Jenn Peters:** And I will say to you, it's a bit crazy because we used to do it, when Timmy was doing it, he did it in Claude, like a post-processing thing.

**Jenn Peters:** And then Claude would make a big list of like, add this, add this, take out this, take out this, da-da-da-da-da-da.

**Jenn Peters:** Panzer created all, like he added that to a new pipeline, all like that does it for us, that if you go into the outreach atlas, you'll see it's called change document.

**Jenn Peters:** So what you do is you just add it like any refresh and then it's going to give you like a point by point list of additions, like new content to insert and where to put it exactly.

**Jenn Peters:** Like insert this after here.

**Jenn Peters:** So then you would take this new content and you would insert it and you would highlight it in yellow.

**Jenn Peters:** And then after all the insertions, it will give you deletions and you do all that.

**Jenn Peters:** And then it will also tell you like content to rearrange.

**Jenn Peters:** I know what you're thinking.

**Jenn Peters:** This is crazy.

**Jenn Peters:** That's why I'm like, I, of course it takes more time.

**Jenn Peters:** Right.

**Jenn Peters:** So like I mentioned it to Joe, like, can you just talk to them and say like, do you like, because they have to review it that way too.

**Jenn Peters:** And it's like yellow strike through and you don't get a, like a picture of the new completed document, right?

**Jenn Peters:** Like you can't really conceive of like, what's going to word count be.

**Jenn Peters:** And like, what's, you know, so.

**Jenn Peters:** I think it'd be so much easier for them as well if we, and I do not know why it was like this.

**Jenn Peters:** This goes back to their strategy sprint and what they requested at the time.

**Jenn Peters:** And then it just stayed that way.

**Jenn Peters:** So I did ask her to talk to them about it.

**Jenn Peters:** I think it got a little bit put to the back burner because of this new strategy and everything and renewal was coming up.

**Jenn Peters:** And it was like, maybe, I don't know, maybe she didn't want to ask because of the renewal coming up or whatever.

**Jenn Peters:** But this would be a perfect opportunity for you to also say like, hey, can we just like make a new document because this is crazy.

**Jenn Peters:** That being said, I did get used to it and like, it doesn't take that long.

**Jenn Peters:** However, even though the pipeline's job is to look at the top competing articles for this keyword and look at those top ranking articles and see what this current article is missing and what it needs to be, you know, added and everything.

**Jenn Peters:** I don't trust it 100%.

**Jenn Peters:** I don't think it always does a really great job.

**Jenn Peters:** And so I will do.

**Jenn Peters:** A second step in Claude and just say, once I have the articles done from here, I'll pop it into Claude and I'll, there's a project you can see there under Outreach, post-processing.

**Jenn Peters:** And I'll say like, hey, this is the keywords.

**Jenn Peters:** These are the top three ranking articles.

**Jenn Peters:** This is my current draft, which is a refresh of this document.

**Jenn Peters:** Does it have everything it needs in order to outrank this piece or is it still missing components or pieces of value, blah, blah, blah, blah, right?

**Jenn Peters:** And then sometimes it'll say like, oh yeah, you've missed some massive things that like, you know, um, and Claude's so dramatic.

**Jenn Peters:** So I just give you that caveat of just like, don't trust what this does exactly.

**Jenn Peters:** And then of course, you know, all the linking, you have to check with the stats and everything like any other pipeline, because, uh, it, it, I will say this, it, this pipeline, it doesn't hallucinate.

**Jenn Peters:** It's 404s or fake stats so much, but what I find that it does is it's the way it talks about it.

**Jenn Peters:** It will kind of like shoehorn a stat to meet what it's trying to say, but then when you go in and you read the stat, it's like, okay, well, is saying something drops 25%, but then the conclusion that the article makes after that is kind of like, yeah, you're kind of inferring what they meant by that when that wasn't really the topic of what they were talking about.

**Jenn Peters:** So you just have to, you know, it's like any of them.

**Jenn Peters:** You just have to kind of use your best judgment, but next week on your first week doing this, you can send each piece to me and I will check them before you ship them.

**Jenn Peters:** So don't worry about anything.

**Jenn Peters:** I will be here.

**Jenn Peters:** Joe is away the next two weeks, but I am here.

**Jenn Peters:** So next week, yeah, just like do those, go through them and then send them to me and then I will make sure they're like good before you send them.

**Jenn Peters:** And then if there's anything that's like a glaring thing that like, I'm like, oh yeah, like, don't forget this with them or whatever.

**Jenn Peters:** Cause I feel like there's a lot of little like finicky things with outreach, but you kind of have to learn it as you do it rather than, you know, if I just tell you like a ton of things out of context, it's not going to like really make much sense.

**Jenn Peters:** You know, like, I think the best thing you could do is like, if you want to prepare for Monday as like, read the strategy, read the company context and the, and the product matrix, try to get to know the product as much as possible.

**Jenn Peters:** Even like feed the product matrix into Claude and get it to like, explain it to you, like in a simpler way.

**Jenn Peters:** Um, and then just like dive in and then I'm sure it will be fine.

**Jenn Peters:** Like, I think, you know, like I said, these aren't like super complex topics.

**Jenn Peters:** They're just, it's just, it's just, we have to make sure we're factually accurate about the way it's talking about the product and that, and that like, yeah, links are all good and stuff like that.

**Jenn Peters:** But other than that, usually what I do is on Monday, I do the, I start my refreshes first because they are the most time consuming.

**Jenn Peters:** I do those at the beginning of the week.

**Jenn Peters:** They take the longest because of the stupid format that we're doing.

**Jenn Peters:** But it's, you know, it's totally up to you.

**Jenn Peters:** But yeah, I will, I'll be here and you can just ask me whatever questions you want.

**Jenn Peters:** It doesn't matter how many.

**Jenn Peters:** We can also meet again.

**Jenn Peters:** Yeah.

**Jenn Peters:** I have some other things I just want to make sure I cover it.

**Jenn Peters:** But do you have any questions about anything we've talked about so far?

**Usman Adepoju:** I feel like I would, like Joe asked the same question.

**Usman Adepoju:** I like, when I get to JIT, I'll have like more questions.

**Usman Adepoju:** Yeah, that's kind of what I think.

**Jenn Peters:** You need to see it and do it, right?

**Jenn Peters:** Like it's hard to.

**Jenn Peters:** You what's going to come up until you do it.

**Jenn Peters:** But I think I'm just looking at my list.

**Jenn Peters:** I think I covered, oh yeah, there's, you'll see in the work, in the pipeline, there's a, there's a, there's a pipeline for just creating just an image, like without an article, it will create a standalone image.

**Jenn Peters:** This is really useful for, sometimes it doesn't create the, like some, you know how sometimes like your, your title will change as you go through it.

**Jenn Peters:** Or like maybe you might remove a tool and now it's like six tools, but you're, now your image is wrong or whatever.

**Jenn Peters:** You can just go into that and make a new image.

**Jenn Peters:** Or if you don't, if the image didn't really look good or whatever, it's a really useful one that you can just, it's pretty quick.

**Jenn Peters:** Like, so like, if you're, sometimes on rare occasions, they will ask like, hey, can you make a better image that doesn't have as long of a title or something like that?

**Jenn Peters:** So yeah, you'll see it in there.

**Jenn Peters:** It says like image only generator.

**Jenn Peters:** It's pretty handy.

**Jenn Peters:** The other thing to mention is that so after Suleiman stages, they will, they use Asana.

**Jenn Peters:** So they use their own calendar.

**Jenn Peters:** They don't use Airtable at all.

**Jenn Peters:** So everything that we put into Airtable, they go and copy and put into their Asana with their own calendar and everything like that.

**Jenn Peters:** So after we send our stuff to Suleiman stage and he stages it, like they publish it on their own cadence as they want to.

**Jenn Peters:** However, they don't always remember to update our OS with the published URL.

**Jenn Peters:** So every couple of days, every day or so, I just go into the OS.

**Jenn Peters:** I check published.

**Jenn Peters:** Oh, yeah, they missed, they missed a URL.

**Jenn Peters:** I go into their blog.

**Jenn Peters:** I see where it was, where like make sure it was published.

**Jenn Peters:** And then it because on Mondays, you'll need to update the Looker dashboard.

**Jenn Peters:** And that's when I kind of tend to notice something's missing from there.

**Jenn Peters:** They just, I've asked them before.

**Jenn Peters:** I don't really want to have, like, they don't use Airtable, so they don't really care.

**Jenn Peters:** I don't think about updating our Airtable.

**Jenn Peters:** But Joe always wants the OS updated.

**Jenn Peters:** So just keep your eye on that.

**Jenn Peters:** I usually check every couple days.

**Jenn Peters:** Today, I'm going to set up the automation for you so that you get the updates about the edits.

**Jenn Peters:** But, yeah, basically, it's just kind of, like, that flow.

**Jenn Peters:** Like, you're making the articles.

**Jenn Peters:** Sometimes there's articles coming in from them that they reviewed to, that you're going to do final checks on and send to Suleiman.

**Jenn Peters:** And then, like, yeah, make a publishing ticket for him on, like, Thursdays, you know, or whatever, Wednesday, Thursday, depending on when stuff comes in.

**Jenn Peters:** Only once have they run out of stuff to publish, I think because of Christmas holidays. Usually it's just a steady flow of stuff getting staged that we check.

**Jenn Peters:** And then like I had already sent it to Suleiman and I was like, hey, like, can you do this today or whatever?

**Jenn Peters:** And then it was, you know, he did it right away.

**Jenn Peters:** But usually it's kind of like there's always a bit of a buffer on our end and their end that it kind of just flows like that.

**Jenn Peters:** And yeah, they're super cool and understanding and stuff.

**Jenn Peters:** So update the OS, daily checks, automations—that's pretty much it, I think, for now.

**Jenn Peters:** I think, like you said, like everything else we can talk through next week as you like dive into it.

**Jenn Peters:** I think Joe is setting up the like linear reminders that were set to me to change to you, I think.

**Jenn Peters:** So like she usually has one for like updating Looker.

**Jenn Peters:** I'm sure it's the same for the clients you've been working like.

**Jenn Peters:** So yeah, you should be getting those.

**Jenn Peters:** But yeah, I'm here, so anytime you want to ask anything, just ask.

**Jenn Peters:** And, of course, there's all the published articles that are in the OS that you can take a look at to be like, hey, does this look kind of like how it should?

**Jenn Peters:** And how do it actually start?

**Jenn Peters:** Just like what they should look at.

**Jenn Peters:** Like, yeah, all their headers are in sentence case, but, like, some of their older ones that were refreshing are in title case, so you have to change that.

**Jenn Peters:** And you'll just kind of get to know all those little things.

**Jenn Peters:** But I think definitely, like, looking at some published pieces on the site and also, like, looking at some of our docs, like, published Google Docs will just give you a general idea of, like, ah, this is kind of, like, oh, yeah, that's another thing.

**Jenn Peters:** Yeah, this is, like, how they should look.

**Jenn Peters:** Like, for example, you'll see, like, at the bottom of each piece, they have kind of this bottom of funnel, like, like a CTA kind of thing.

**Jenn Peters:** Yeah, like, it'll.

**Jenn Peters:** Yeah, there's a, there's a Claude project that will write that for you.

**Jenn Peters:** So, so some of the older articles that you're refreshing won't have that, but we put that in every piece and Timmy made some kind of project in Claude that will, you can just like put the content in and it will say like the part that says at the bottom, like eyebrow copy, paragraph, CTA, we put that into every piece.

**Jenn Peters:** So, uh, but yeah, I'll be here.

**Jenn Peters:** So if you can't find something next week, then just, just ask and I will show you where to find it.

**Jenn Peters:** All right, no problem.

**Usman Adepoju:** But like for now, I think I'll find, so the Timmy's video that you're referring to, is it like in the, is it in the shot?

**Usman Adepoju:** Yep.

**Jenn Peters:** So if you'd go to like, yeah, basically like your first thing you could do is like go through the, what is that called?

**Jenn Peters:** Manual thing?

**Jenn Peters:** Operational manual.

**Jenn Peters:** Yes, that thing operation manual.

**Jenn Peters:** And then, um, it's got all the publishing stuff there pretty much and the videos and everything.

**Jenn Peters:** So, um, he.

**Jenn Peters:** He breaks down like how you copy the article content from the published page and then put it into a Google Doc and how you format it so that it will go back into like a normal view so that you can actually start to edit it and not just be like all like chunky graphic blocks and stuff.

**Jenn Peters:** Yeah, he makes it really clear.

**Jenn Peters:** But yeah, also I'm here so I can always jump in and show you something.

**Jenn Peters:** Thank you.

**Usman Adepoju:** Thank you.

**Jenn Peters:** I think it's good timing if we were to shift Outreach, because of their strategy shift, renewal, and new content coming up. I'm sure they won't notice any change or difference and it'll be all good.

**Jenn Peters:** So yeah, awesome, I'm excited for you. Don't hesitate to reach out and ask for anything.

**Jenn Peters:** Okay.

**Jenn Peters:** Talk to you soon.

**Jenn Peters:** Bye.
