# Hyperexponential Publishing

<metadata>
date: 2025-12-08
time: 18:00 UTC
duration: 27 minutes
organizer: bailey@growthx.ai
participants: Bailey Seybolt, Kirkland Gee, Rachel Pasche
fathom_recording_id: 107054337
fathom_url: https://fathom.video/calls/495497082
share_url: https://fathom.video/share/aG5_3i_KsM1MUzFEEoAw-Ysj-LADp3rn
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Bailey, Rachel, and Kirkland troubleshooted Atlas-to-Framer article publishing failures, identifying two root causes: the Framer MCP plugin must remain active during publishing, and a recent Framer site relaunch renamed the Blog collection from "Blog" to "Blog 📝," breaking the hard-coded Atlas workflow. They successfully tested a fix and confirmed that articles publish as drafts in Framer despite Atlas returning false failure messages. The team also scoped a potential Relay project for content-only work using Contentful CMS, with Bailey to clarify content volume and interactive element expectations.

---

## Context

This meeting was triggered by publishing failures in the Hyperexponential account, where articles Bailey was attempting to publish through Atlas to Framer were timing out and never appearing in the site. Kirkland built an automated publishing workflow via Atlas with a Framer MCP plugin integration to eliminate manual publishing. The workflow had been working initially but began failing in early December 2025 when Hyperexponential launched a new Framer site. Rachel recently gained Framer access and is the intended publisher going forward. The team needed to troubleshoot the issue before Rachel could take over publishing responsibilities.

---

## Relevance

**To GrowthX Delivery:**
- Atlas workflow requires active MCP plugin presence and user-specific URLs that must be updated per publisher; this creates friction and requires documentation for every team member who publishes.
- Framer's MCP server behavior is unreliable (false negatives on success status), and hard-coded collection names in workflows break on client site updates; workflows should parameterize collection names to avoid future failures.
- Rachel is now the primary Hyperexponential publisher; she needs MCP URL set as default in Atlas and clear runbooks for the publishing process.
- Hyperexponential still needs clarification on author handling and default author field values before full automation.

**To GrowthX Business Development:**
- Relay project scoping is advancing; a content-only engagement with Contentful CMS is technically viable if another vendor handles development.
- Key risks to clarify before committing: content volume scope and whether Relay expects interactive elements (quizzes, dynamic content) that would require custom development beyond static content placement.

---

## Overview

- **The Fix:** Publishing requires the Framer MCP plugin to be active and its unique URL pasted into Atlas. This enables the necessary local connection.
- **Root Cause:** A recent Framer site relaunch renamed the target collection from "Blog" to "Blog 📝," breaking the hard-coded Atlas workflow.
- **Known Issue:** Atlas will still report a "failed" status, but this is a false negative; articles publish successfully as drafts in Framer.
- **Relay Project:** A content-only scope (Contentful) is viable. Key risks to clarify are content volume and the client's expectations for interactive elements (e.g., quizzes).

---

## Key Topics

### Framer Publishing Failures

  - **Problem:** Atlas publishing jobs were running indefinitely and failing to create articles in Framer.
  - **Root Cause 1: MCP Plugin**
      - The Framer MCP plugin must be active to create a local connection that Atlas requires.
      - Each user's plugin generates a unique URL that must be pasted into the `Framer MCP URL` field in Atlas.
  - **Root Cause 2: Collection Name Mismatch**
      - A recent Framer site relaunch renamed the target collection, breaking the hard-coded Atlas workflow.
      - **Old Name:** `Blog`
      - **New Name:** `Blog 📝`
  - **Solution:**
      - Update the Atlas workflow's collection name to `Blog 📝`.
      - Ensure the MCP plugin is active and the correct URL is in Atlas before publishing.
  - **Result:** The test article published successfully as a draft in Framer.

### Relay Project Scoping

  - **Context:** Relay is considering a content-only project for micro-sites, with another vendor handling development.
  - **Technical Viability:** High, as the project uses Contentful, a familiar CMS.
  - **Key Risks to Clarify:**
      - **Content Volume:** Confirm it aligns with current capacity.
      - **Interactive Elements:** Clarify if the client expects us to build interactive features (e.g., quizzes) or just provide static content for templates built by the dev vendor.

---

## Action Items

**Kirkland Gee (GrowthX)**
- Update Atlas default Framer MCP URL to Rachel's in the Hyperexponential workflow

**Bailey Seybolt (GrowthX)**
- Follow up with Hyperexponential regarding images and author handling, then update Atlas workflow defaults
- Confirm with Rachel: verify Framer category field is single-select only
- Email Relay: confirm CMS platform, content volume scope, and expectations for dynamic/interactive elements (e.g., quizzes)

---

## Transcript
**Bailey Seybolt:** Um, just realized, do you have access to Framer yet?

**Rachel Pasche:** Uh, yes.

**Bailey Seybolt:** So I didn't get in.

**Bailey Seybolt:** You were, okay.

**Rachel Pasche:** Yeah, Kirkland sent a link.

**Bailey Seybolt:** Okay, yeah.

**Bailey Seybolt:** I realized after all that and asking you to do it that I didn't actually add to that.

**Rachel Pasche:** Um, yeah, I was able to get in, thankfully.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** Um, they also just relaunched their new website, which I feel like always breaks something.

**Bailey Seybolt:** So we'll see.

**Bailey Seybolt:** Um.

**Rachel Pasche:** Oh.

**Rachel Pasche:** Great.

**Bailey Seybolt:** Yeah, exactly.

**Bailey Seybolt:** We'll see what happens.

**Rachel Pasche:** So you guys have been doing this manually?

**Rachel Pasche:** You haven't been using, like, SoWren?

**Bailey Seybolt:** Well, well, we created a way to do it through Atlas, like to auto-publish.

**Bailey Seybolt:** So theoretically, you can publish directly.

**Rachel Pasche:** So

**Bailey Seybolt:** Hi Kirkland.

**Kirkland Gee:** Hello.

**Kirkland Gee:** How's it going?

**Kirkland Gee:** are you guys?

**Rachel Pasche:** Good.

**Rachel Pasche:** Good.

**Bailey Seybolt:** I'm going to have a fire in the back.

**Bailey Seybolt:** That looks so cozy.

**Kirkland Gee:** Yeah, my office is in our basement and we don't have like central heat in our basement.

**Kirkland Gee:** It's just baseboards.

**Kirkland Gee:** And so it's way more cost effective to put a little gas fireplace than it was to like run radiator heat all winter.

**Kirkland Gee:** Uh, and there's, it's currently snowing and there's a couple of inches of snow on the ground.

**Kirkland Gee:** So I am freezing.

**Bailey Seybolt:** Yeah, I'm freezing too.

**Kirkland Gee:** I look like I'm dressed to go outside.

**Kirkland Gee:** That's I all listen.

**Kirkland Gee:** I, I am so cold all the time.

**Kirkland Gee:** My wife is always hot in our house.

**Kirkland Gee:** So just a never ending struggle.

**Kirkland Gee:** Um, cool.

**Kirkland Gee:** Thank you guys for just doing a quick meeting.

**Kirkland Gee:** I think we can try to figure this out because I've been having a hard time like reproducing the issues that you're running into.

**Kirkland Gee:** So I just kind of want to see like what you're doing to publish to framer so that I can.

**Kirkland Gee:** Try to work out, like, what's going wrong.

**Bailey Seybolt:** So when you publish it, have you tried publishing and it worked fine?

**Kirkland Gee:** Both from Atlas and from my machine, it all works fine.

**Bailey Seybolt:** Clearly I'm doing something wrong.

**Kirkland Gee:** So I don't know if you are, or if there's some difference in the MCP URLs, depending on who's logged in, or if there's some issue with, like, it just being super inconsistent because it's kind of a newer technology.

**Kirkland Gee:** So that's why I just want to, like, walk through what you are doing so I can understand it and then try to figure out what's going wrong.

**Kirkland Gee:** So if you're doing something new, I'm not so worried about this one that kind of already broke.

**Kirkland Gee:** I think we can try it again.

**Bailey Seybolt:** So I was just, this was the last one I tried to do.

**Bailey Seybolt:** And what I find is it's just, it's like running forever and then it's failing.

**Kirkland Gee:** And the article is not showing up in Framer when that happens.

**Bailey Seybolt:** No, and it's not showing up in Framer.

**Bailey Seybolt:** Because I...

**Bailey Seybolt:** Thank you.

**Bailey Seybolt:** The first couple times when you and I did it together, when we got started, it also failed, but I feel like then it would run for less than five minutes, and then it showed up.

**Bailey Seybolt:** It said it failed, but it still showed up in Framer.

**Bailey Seybolt:** Here, it's running forever, and then I go and check in Framer.

**Bailey Seybolt:** It's not in Framer.

**Kirkland Gee:** Yeah, okay.

**Bailey Seybolt:** But I'm not really, I'm not sure, like in terms of walking through, I just, all I do is update the text here, and then publish to Framer.

**Kirkland Gee:** So if we go to the publish to Framer step.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** Can you just verify a couple of things for me?

**Kirkland Gee:** So go over to Framer.

**Bailey Seybolt:** Do you have the MCP server running in Framer when you click publish?

**Bailey Seybolt:** How do I check to see it?

**Kirkland Gee:** top left corner in Framer, just click that, and then there's a button for plug-in.

**Kirkland Gee:** It's for a toggle down towards the bottom.

**Kirkland Gee:** And then you can probably run recent, but just click browse all, because I don't know what the most recent one running was.

**Kirkland Gee:** And then MCP.

**Kirkland Gee:** And so you need to have this running with that little toggle window open whenever you go to publish.

**Bailey Seybolt:** If that's not open, Atlas cannot communicate with Framer at all.

**Bailey Seybolt:** So do I need to re...

**Bailey Seybolt:** Interesting.

**Bailey Seybolt:** Okay, so I just need to relaunch it every time then.

**Kirkland Gee:** So every single time you want to publish, that window in your browser has to be open, and this pop-up has to be open running the MCP plugin.

**Bailey Seybolt:** Okay, so that's just me being an idiot then, because I think it was just, I must have left it open for the first while, and so it wasn't an issue.

**Bailey Seybolt:** And then the first time I logged out and just shut it all down.

**Kirkland Gee:** you even just had a tab open, but like that tab went to sleep in Chrome, then this plugin may not be running.

**Kirkland Gee:** I hate this.

**Kirkland Gee:** It's so dumb.

**Kirkland Gee:** I don't know why Framer did it this way, but like...

**Kirkland Gee:** Like, this is what they require.

**Bailey Seybolt:** Like, this is not us.

**Bailey Seybolt:** This is just Fathom.

**Kirkland Gee:** The other thing is just to make sure that that URL right there, whoever is publishing, so whether it's you or Rachel or somebody else in the future, there's, if you go back to Atlas, there is an input to every row.

**Kirkland Gee:** So if you scroll up on the top left, and click, like, the top level input for this, and then scroll down to the bottom of the input, there is a, sorry, on the right side, you have to move your cursor, like, out of one of the boxes to get to the bottom.

**Bailey Seybolt:** Okay, there we go.

**Kirkland Gee:** Yeah, it's kind of, so that Framer MCP URL, there's a default, which right now, I believe, is set to yours.

**Kirkland Gee:** Um, but, for example, like, Rachel, if you go log in and run the plugin, and you try to publish with Bailey's URL, it's not going to authenticate, because they're authenticating this.

**Kirkland Gee:** This URL based on the user that's logged in with the plugin running at that time.

**Kirkland Gee:** So they need to line up.

**Rachel Pasche:** Does that make sense?

**Rachel Pasche:** So, like, if I were doing it, I might have to take the URL that shows up for me in Framer and go in and paste it here.

**Kirkland Gee:** Yes.

**Kirkland Gee:** So I'm going to say, like, whoever's going to be doing this primarily, we can just set that to the default for any new rows that get added.

**Kirkland Gee:** But if we change the default, it won't update all the rows that already exist, right?

**Kirkland Gee:** So if you go to do this, just double check, you know, in the input at the bottom, just paste in the URL that you have from Framer into that thing right there.

**Kirkland Gee:** And then you should be able to save that, run the publish again.

**Kirkland Gee:** And, again, this is just something going on with the MCP server.

**Kirkland Gee:** The publish step might fail in Atlas.

**Kirkland Gee:** But as long as it only takes a couple of minutes, it should.

**Kirkland Gee:** What's happening is, for some reason, the message that Framer is sending back to us to say, hey, we got the article.

**Kirkland Gee:** Atlas is not, like, read.

**Kirkland Gee:** It's probably my fault in the way I wrote the workflow, but it's just not reading that as a success.

**Kirkland Gee:** I've been trying to work that out, but MCP servers are just weird sometimes.

**Kirkland Gee:** So it should still work as long as you have the plugin running when you click publish, which, again, is super annoying, but it's...

**Kirkland Gee:** It's what it is.

**Rachel Pasche:** I don't need to install that.

**Kirkland Gee:** That's just a plugin within Framer.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** So if you go back to Framer, basically, as long as you have a tab open...

**Kirkland Gee:** So also, if you just copy that URL, Bailey, I want to make sure that that is the right...

**Bailey Seybolt:** Go back to Atlas and replace it.

**Kirkland Gee:** I want to show you one thing you can check.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** I think it'll probably be Rachel going forward.

**Kirkland Gee:** So yeah, we should figure out how to get it with her.

**Kirkland Gee:** can change the default, Rachel.

**Kirkland Gee:** So if you just send me your URL in a Slack DM, once you log in...

**Kirkland Gee:** If get it, I can update that.

**Kirkland Gee:** But Bailey, really quick, we can just hit save and try to publish again.

**Kirkland Gee:** I'll show you something you can look at to verify if it's working.

**Kirkland Gee:** So once you click play, hopefully it'll just work.

**Kirkland Gee:** Cool.

**Kirkland Gee:** Now go back to Framer.

**Kirkland Gee:** You should be able to see that little circle turn green.

**Kirkland Gee:** Yeah.

**Bailey Seybolt:** So you see where it says right next to MCP.

**Kirkland Gee:** When that's green, that means you're connected.

**Kirkland Gee:** That means something is connected through your MCP URL.

**Kirkland Gee:** So right now Atlas is talking to Framer and working out how to publish everything.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** Again, Atlas is probably still going to return an error message, unfortunately.

**Kirkland Gee:** Okay.

**Kirkland Gee:** But it usually takes between two and 10 seconds.

**Kirkland Gee:** Can you just shoot me that URL?

**Kirkland Gee:** Because I could try to talk you through this, but I think I can.

**Bailey Seybolt:** Yeah, just so I don't have to go dig it up.

**Kirkland Gee:** I can check and see if it's on Framer, too.

**Kirkland Gee:** It's probably not.

**Bailey Seybolt:** Well, I guess it'll be on there because I added it before.

**Kirkland Gee:** Oh, if that one's already published, that might be why I returned an error.

**Bailey Seybolt:** I added it manually.

**Kirkland Gee:** This is hyper-exponential.

**Kirkland Gee:** Yeah, Bailey, if you can just shoot just the page, just the URL that you're on in the Zoom chat, so I can go take a look at why that failed.

**Bailey Seybolt:** Oh, sorry, I sent it to the note taker.

**Kirkland Gee:** Oh.

**Bailey Seybolt:** Like, every time, every time.

**Rachel Pasche:** Yeah, I do it.

**Rachel Pasche:** It's always annoying because it's, like, the separate tab, and, like, automatically defaults to the normal tab.

**Kirkland Gee:** I'm just going to share my screen while I look at this, just to try to figure out what happened.

**Bailey Seybolt:** So I did manually publish this one, so if, for some reason, that would cause an error.

**Kirkland Gee:** Yeah, I think it might.

**Kirkland Gee:** I mean, again, framers, it's not good.

**Kirkland Gee:** Like, this whole setup is so wonky, but I'm going to guess.

**Kirkland Gee:** Collection articles not found in project.

**Kirkland Gee:** Oh, did we change the name of something in Framer?

**Bailey Seybolt:** Well, just launched the site, like their new site, they just launched it on Framer on Saturday, so it's possible that something changed on there.

**Kirkland Gee:** so they added some, they renamed the collection, so that's the problem.

**Bailey Seybolt:** Blog, is this the one that we're using?

**Kirkland Gee:** Blog, yes, it was.

**Kirkland Gee:** Okay.

**Kirkland Gee:** So now...

**Kirkland Gee:** You do not have content editing rights.

**Bailey Seybolt:** What?

**Kirkland Gee:** What do you mean I don't have...

**Kirkland Gee:** Am I not?

**Kirkland Gee:** Who am I logged in as?

**Kirkland Gee:** What is happening?

**Kirkland Gee:** I guess they took away my content editing rights. So it should be blog.

**Bailey Seybolt:** Maybe I do, what is it, what do you want to copy?

**Kirkland Gee:** I just want to make sure I have the right code for whatever this emoji, the emojis actually might cause some problems, we'll find out in a minute, but can you just copy that, I think I can figure out which emoji that is, but it's like, if I'm even like, if it's not the exact same code, then it's probably go through an error.

**Kirkland Gee:** I think it's this one, so let's try this, input, so again, we have, so do I need, so they changed the categories, is that what you think the issue is?

**Kirkland Gee:** 100%, so and actually that's hard-coded into our workflow, which is super annoying.

**Kirkland Gee:** I don't know why I decided to do it that way, but I think I will need to, do I

**Kirkland Gee:** have an option to just pass something, election name, yes, I do, okay, so I'm not, just give me one second here, trying to see, where is that, oh, I bet I, okay.

**Kirkland Gee:** Sorry, I'm like, talking to myself, I did not, I think it's probably just here, election name, yeah, so, it's now called this, blog with this little emoji, okay, is there a space, hard to tell.

**Kirkland Gee:** I don't think there is, actually.

**Kirkland Gee:** Because it looks like that has a space and this doesn't, right?

**Kirkland Gee:** Yeah, I see what you're saying.

**Kirkland Gee:** We'll try it.

**Kirkland Gee:** I'm going to save that.

**Kirkland Gee:** And Bailey, you still have the plugin open?

**Bailey Seybolt:** Yes, I do.

**Kirkland Gee:** I'm just going to try this again. Let's see.

**Kirkland Gee:** So that's running, getting an error again, collection blog, not found, there is a space, I'm so annoyed, this little stuff is, again, it's just because like, this is how, it works a little bit better if you have like, if you're using like a cloud code or something, because it can like talk back and forth with the MCP versus in our workflow.

**Kirkland Gee:** I just want to make sure that, when you guys actually go to do this, that, it's not going to keep throwing errors for you.

**Kirkland Gee:** And then Rachel, I will go ahead and set that as the default input.

**Kirkland Gee:** So if you create a new row, it will default to yours.

**Kirkland Gee:** If you want to go back and like republish any of these that are already here, you'll just need to, that one failed to find out why.

**Kirkland Gee:** If that or something else, the collection "blog" might have been the issue. When I updated the default, it actually should have changed it for all rows.

**Kirkland Gee:** Thank you.

**Kirkland Gee:** Yeah, it looks like this just got edited.

**Kirkland Gee:** 6.13 p.m.

**Bailey Seybolt:** I don't know what time zone this is in.

**Bailey Seybolt:** They might be in the UK.

**Kirkland Gee:** That would actually be about right.

**Kirkland Gee:** Yeah, because this is what I was talking about.

**Kirkland Gee:** This step here is still running, but I think it's actually already done the thing.

**Bailey Seybolt:** But it's hard to know.

**Bailey Seybolt:** Oh, yeah, that's it, because it's in there twice, which would make sense, because I already manually have Ah, here we go.

**Bailey Seybolt:** So here's the draft, actually.

**Kirkland Gee:** Yes.

**Kirkland Gee:** Yeah, exactly.

**Kirkland Gee:** This is the one that just showed up.

**Kirkland Gee:** That makes more sense.

**Rachel Pasche:** Yeah.

**Kirkland Gee:** Yay.

**Kirkland Gee:** So it works.

**Bailey Seybolt:** I think there's still, like, a couple, like, the images we don't have from the pipeline right now.

**Bailey Seybolt:** Well, they don't, they haven't, we don't make images for them yet.

**Kirkland Gee:** Great.

**Kirkland Gee:** So that's not a, that's not a, that's a them problem.

**Kirkland Gee:** And then author, is.

**Kirkland Gee:** Isn't going over.

**Kirkland Gee:** Do they have like a default author on everything or are they choosing specific authors?

**Bailey Seybolt:** were choosing right now.

**Bailey Seybolt:** There was a lot of stuff that was on hold because they were figuring it out as they launched the website.

**Bailey Seybolt:** So there's some stuff I should follow up with them this week.

**Bailey Seybolt:** And that is one of them.

**Bailey Seybolt:** I can add them.

**Bailey Seybolt:** I think we were going to talk about images and I will also add author, how do I want to do that.

**Bailey Seybolt:** And so once we do that, is there an easy way to update the default?

**Kirkland Gee:** you can change the author at any time in the input to the pipeline.

**Kirkland Gee:** Like each row can have its own.

**Kirkland Gee:** Or I just have it because I think there was a marketing team author.

**Kirkland Gee:** I don't know if there still is.

**Kirkland Gee:** So I had set that to the default, but you guys could literally just click edit it up here and just change marketing team to whatever the author is.

**Kirkland Gee:** Make sure it's just kind of like the thing and anything like that.

**Kirkland Gee:** Otherwise, it might mess up if you're running the issue.

**Kirkland Gee:** Please let me know, but you should just be able to tweet that there, or if a specific piece needs a specific author, just put it in the input.

**Kirkland Gee:** And the same thing with categories, I think these, if I remember how I did this, need to, oh, close the window.

**Kirkland Gee:** But categories are going to be comma separated, ideally.

**Kirkland Gee:** So if you want to put multiple categories on something, I don't know if Framer even supports multiple, or if it's just the one.

**Kirkland Gee:** Um, because I...

**Bailey Seybolt:** I'll find out, Rachel, because I think they were also going to update that when they went to launch this blog.

**Kirkland Gee:** So I'll find out where they went with those.

**Kirkland Gee:** It looks like category is a single select now.

**Bailey Seybolt:** So you're just picking one.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** So whatever one category you want for the piece, just put it right here.

**Bailey Seybolt:** you could, you know, AI, whatever it might be.

**Kirkland Gee:** Uh, and then, yeah, as long as the URL is correct, and as long as...

**Kirkland Gee:** Your, you know, plug-ins, run recent, as long as that's running, URL, you should be good to go.

**Kirkland Gee:** Again, Atlas is still going to do this dumb thing where it just sort of like runs the workflow for a little bit.

**Kirkland Gee:** Eventually it will fail, but it's not, it's probably not actually failed as long as you have the server.

**Bailey Seybolt:** And Rachel, just, you know, we stage them, but they don't go live.

**Rachel Pasche:** So you don't need to be like too nervous when you do it because they want to publish themselves.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** And everything should go to draft from this workflow.

**Rachel Pasche:** You shouldn't have any like auto publishing or anything.

**Rachel Pasche:** Yeah.

**Rachel Pasche:** Cool.

**Kirkland Gee:** Awesome.

**Kirkland Gee:** If you guys need anything, if you're into any bugs, just let me know.

**Kirkland Gee:** But this is why I wanted to like do it together and make sure there wasn't like one piece missing somewhere.

**Bailey Seybolt:** Because I was like losing my mind.

**Kirkland Gee:** I'm like, why is this not working?

**Kirkland Gee:** What is wrong?

**Kirkland Gee:** But this makes a lot of sense.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** Awesome.

**Bailey Seybolt:** Um, uh, can I ask you about, since I have you on for another couple minutes, Rachel

**Bailey Seybolt:** Jill, if you have any other questions, you can drop.

**Bailey Seybolt:** I want to ask Kirkland about a different client.

**Rachel Pasche:** Sounds easier.

**Rachel Pasche:** Bye.

**Rachel Pasche:** Thank you.

**Kirkland Gee:** I'll read your questions.

**Rachel Pasche:** I had many.

**Rachel Pasche:** Bye.

**Bailey Seybolt:** Thanks, Rachel.

**Bailey Seybolt:** My question is, I think we, like, looped you in to that conversation about Relay because they wanted to do this, like, us to scope this custom project.

**Bailey Seybolt:** It was all built on Contentful.

**Bailey Seybolt:** I think what we decided is we don't have the internal, like, dev and design.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** I think particularly design is looking like a bigger bottleneck than anything.

**Bailey Seybolt:** So it sounds like they might be interested in us coming in to support just whatever, like, from an editorial content creation standpoint and have someone else, like, build out the micro sites.

**Bailey Seybolt:** So I'm going to get more information from them.

**Bailey Seybolt:** But I was just wondering, from your point of view, if there's any questions you'd want me to ask them, like, in terms of, yeah, just, like, trying to scope out what it means.

**Bailey Seybolt:** Because I imagine even if someone else is doing that dev work, there'll be.

**Bailey Seybolt:** A certain amount of coordination, they'll be like, I don't know if there's best practices, if there's anything you'd want me to find out from them before we kind of agree to jump in and handle the content piece of that.

**Kirkland Gee:** Yeah, I mean, if someone else is building it, you know, the only real complications could be around, like, if it's on Contentful, that's great.

**Kirkland Gee:** We can work with Contentful, that's fine.

**Kirkland Gee:** If they decided to go with some other CMS, like, making sure that we know what that is, that that's going to be workable.

**Kirkland Gee:** Because sometimes people use some weird one-off custom thing that, like, makes it work.

**Bailey Seybolt:** don't think so, because they are navigating their whole site onto Contentful right now, and that's, like, a new thing.

**Bailey Seybolt:** So I can't imagine that they would want to bring in, like, something else at this point.

**Kirkland Gee:** Yeah, yeah.

**Kirkland Gee:** So that makes sense.

**Kirkland Gee:** And then, you know, I think it's just, like, volume of content, as long as it's not falling outside of what we've, you know.

**Kirkland Gee:** Now, if they want some level of research or information that we've not...

**Kirkland Gee:** done in the past, then maybe we'd want to talk about that, but it didn't seem like it's anything all that crazy, at least on the content side.

**Kirkland Gee:** So I don't think so.

**Kirkland Gee:** mean, if we're just putting content on that website, I don't foresee any technical concerns, really.

**Bailey Seybolt:** Yeah, I think that's the way I'm envisioning it, is it's like they're building the containers now, and then we would be filling them with content.

**Kirkland Gee:** Right.

**Kirkland Gee:** The same way we do it.

**Kirkland Gee:** Like, that sounds like what we do for pretty much every editorial customer.

**Kirkland Gee:** So the only thing is, like, I don't know if they want us to do any, making sure they're not expecting, like, okay, some other dev builds, you know, one visual element, and then we get enough content, and now we need to, like, go duplicate and recreate work.

**Kirkland Gee:** That's the only thing I could maybe see coming up as, like, quizzes, right?

**Kirkland Gee:** Like, they build a template for a quiz, and now we actually have to go dev the experience for every quiz for new articles.

**Bailey Seybolt:** Like, are they expecting that?

**Kirkland Gee:** Yes.

**Kirkland Gee:** I doubt it, but it might be worth clarifying that.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** Yeah, I think I would clarify that, yeah, this is just either purely for editorial or just, like, static content.

**Bailey Seybolt:** Like, I'm sure they would want us to build up the content on whatever the landing page experience is for the Microsoft itself, but I assume that would be pretty templated and would be closer to, like, editorial or PSA.

**Kirkland Gee:** Yeah, that's what I'm thinking, too.

**Kirkland Gee:** Yeah.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** Okay, cool.

**Bailey Seybolt:** I just wanted to make sure there was no big flags that I'd be missing.

**Kirkland Gee:** Not that I can think of.

**Kirkland Gee:** Okay.

**Kirkland Gee:** That all sounds good.

**Bailey Seybolt:** Okay, sounds good.

**Bailey Seybolt:** Well, thank you for this.

**Bailey Seybolt:** Sorry, I just wasn't running the plug-in.

**Kirkland Gee:** You must get tired of having these conversations with non-technical people where you're just press the button.

**Kirkland Gee:** Not at all.

**Kirkland Gee:** Mostly because I used to be one of those.

**Kirkland Gee:** I mean, literally, I was SEO director in an agency for years before I ever got into engineering.

**Kirkland Gee:** And so I think I have a little more empathy for people who, like, don't spend all day writing code than a lot of engineers do.

**Kirkland Gee:** Because the last thing I ever want to make someone feel is, like, oh, my gosh, I can't believe I missed this.

**Kirkland Gee:** Because it's not a tiny little thing.

**Kirkland Gee:** Like, there's a lot of stuff to keep trying.

**Kirkland Gee:** trying.

**Kirkland Gee:** But sometimes it's just easier to, like, spend 15 minutes and figure it out and keep going back and forth for two weeks.

**Kirkland Gee:** So, no, don't feel bad at all.

**Kirkland Gee:** I assume that might have been the problem, but I also would not have been surprised if, like, the framer side of things was just a piece of .

**Kirkland Gee:** Because it kind of is hard.

**Kirkland Gee:** Well, thank you.

**Kirkland Gee:** I appreciate your patience.

**Kirkland Gee:** Anytime.

**Kirkland Gee:** Thanks, Bailey.

**Kirkland Gee:** Talk to you later.

**Kirkland Gee:** Bye.
