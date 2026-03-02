# Otto & Relay Content

<metadata>
date: 2025-12-01
time: 16:58 UTC
duration: 27 minutes
organizer: bailey@growthx.ai
participants: Bailey Seybolt, Fatima Tahir, Rachel Pasche, Kelvin Gitari
fathom_recording_id: 105264206
fathom_url: https://fathom.video/calls/490038783
share_url: https://fathom.video/share/ob1jhWndLEYA3MbZHeuk38ndZePKAS2-
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

GrowthX aligned the team on content delivery strategy for two clients—Otto (AI travel assistant) and Relay (small business banking platform)—following quality issues from a recent shift to agentic pipelines. Fatima takes over article generation while Rachel provides collaborative artifact updates; Kelvin closes out outstanding content and updates handoff documentation. The team identified root causes of poor output (artifacts written for brevity, missing product fact-checking, incorrect internal links) and established a process to improve pipeline quality through better artifact design and early feedback loops.

---

## Context

GrowthX is managing content delivery for Otto and Relay, two SaaS clients with different maturity levels and content needs. Otto is a newly launched AI travel assistant for business travelers; the product is new with limited content in market and a large runway of approved topics. Relay is a more established banking platform serving small businesses, particularly in home services accounting, and is expanding into "AI for small businesses" positioning. Both clients recently migrated to agentic content generation pipelines, which has created quality issues requiring immediate corrective action. Fatima Tahir just returned from 16-week maternity leave and is stepping into the article generation role; Rachel Pasche and Kelvin Gitari provide supporting functions. Bailey Seybolt leads the engagement and has direct client relationships.

---

## Relevance

### To GrowthX Delivery

- **Agentic pipeline quality requires artifact-first fixes, not post-processing workarounds.** The team recognized that choppy sentences, factual errors (invented product features), and irrelevant internal links stem from poorly written artifacts, not the pipeline itself. Updating artifacts in Atlas to use client voice/tone is the highest-leverage fix.
- **Internal link targeting must be restricted to blog subdirectories.** Agentic pipelines default to broad website links; narrowing to `auto.com/resources/blog` or equivalent, plus explicit "do not link to anything but this" instructions, significantly improves results.
- **Product fact-checking is a required QA step for new products.** Despite updated artifact data in Atlas for Otto's features, the pipeline still invents non-existent capabilities; manual Claude-based verification is needed until artifacts stabilize.
- **New team members returning from leave benefit from collaborative artifact updates, not solo post-processing.** Pairing Fatima and Rachel on artifact fixes accelerates onboarding and builds shared understanding of client voice/tone requirements for long-term ownership.

### To GrowthX Business Development

- **Relay is expanding into new verticals (accounting/bookkeeping cluster) and seeking small business audience positioning.** Bailey is conducting strategy research this week; keyword research and assignment generation are needed by end-of-week to maintain content velocity.
- **Both Otto and Relay accounts show velocity maintenance as a priority.** Kelvin is closing outstanding content from last week; Fatima will generate 1-2 articles per client weekly for Bailey review, establishing baseline cadence for agentic content in these accounts.

---

## Overview

- **Fatima Tahir now owns article generation for Otto and Relay.** Rachel Pasche will provide collaborative support on artifact updates, not editing, to improve pipeline quality through early-stage refinement.
- **Top priority: Fix poor agentic pipeline output by improving artifacts.** The root cause is artifacts written for brevity (no transitions), which produce choppy sentences, factual errors (Otto's AI inventing non-existent features), and irrelevant internal links. Updated artifacts in the client's voice and tone dramatically improve output quality.
- **Kelvin will first deliver last week's outstanding content,** then update Notion handoff docs with current agentic pipeline details. Fatima will generate 1–2 articles per client weekly for Bailey to review, providing immediate feedback loops for artifact improvements.

---

## Key Topics

### Problem: Poor Agentic Pipeline Output

  - The recent shift to the agentic pipeline for Otto & Relay has degraded article quality, creating significant post-processing work.
  - **Root Cause:** Artifacts are written for brevity, not natural language. This produces choppy sentences and poor transitions in the final articles.
  - **Key Issues:**
      - **Factual Errors (Otto):** The AI invents non-existent product features, requiring a manual fact-checking step.
      - **Tone Mismatch (Relay):** The AI overuses conversational examples ("7 a.m. and your app is uploaded...") without providing context, resulting in "all tone, no substance."
      - **Irrelevant Internal Links:** Links often go to "mindshare competitors" (articles targeting the same keywords) or are contextually wrong.
          - **Fix:** Restrict the pipeline's link-target URL to the client's blog (e.g., `otto.com/resources/blog`) and add an explicit "do not link to anything but this" instruction.

### Solution: Collaborative Artifact Updates

  - **Rationale:** Improving artifact quality is the most effective way to fix the pipeline's output and reduce manual editing.
  - **Process:** Fatima and Rachel will collaborate on artifact updates early this week.
      - **Why:** Collaboration ensures a shared understanding of the process, which is more beneficial for long-term ownership than Rachel simply editing articles.
      - **Action:** Fatima will create a copy of the pipeline to safely test changes.
  - **Guidance:** Review the Notion meeting with Hassan, who confirmed that artifacts written in the client's actual voice and tone dramatically improve output quality.

### Client Context & Priorities

  - **Otto:** AI travel assistant for business travelers.
      - **Content Focus:** A new product with a large runway of approved topics.
      - **Priority:** Fact-checking all product features and links.
  - **Relay:** Banking platform for small businesses.
      - **Content Focus:** Home services accounting and "AI for small businesses" (to own this niche).
      - **New Project:** Bailey is researching a new "accounting and bookkeeping" cluster.
      - **Action:** Fatima will conduct keyword research and generate assignments for this new cluster once Bailey provides seed keywords.

### Team Roles & Weekly Plan

  - **Kelvin:**
      - **Priority 1:** Deliver all outstanding content from last week.
      - **Priority 2:** Update the handoff documents in Notion to reflect current agentic pipeline processes.
  - **Fatima:**
      - **Priority 1:** Collaborate with Rachel on artifact updates.
      - **Priority 2:** Generate 1–2 articles per client for Bailey's feedback.
      - **Priority 3:** Conduct keyword research for Relay's new cluster.
  - **Rachel:**
      - **Priority 1:** Collaborate with Fatima on artifact updates.
      - **Rationale:** This is feasible due to lighter workloads for Logic (paused Mon/Tues) and Hyper-Exponential (calibration articles only).
  - **Bailey:**
      - **Priority 1:** Provide feedback on Fatima's initial articles to guide artifact improvements.
      - **Priority 2:** Provide seed keywords to Fatima for Relay's new cluster.

---

## Action Items

**Kelvin Gitari (GrowthX)**
- Close out last week’s content; deliver to clients; resolve outstanding feedback
- Update Notion handoff docs w/ current agentic pipeline details

**Fatima Tahir (GrowthX)**
- Review client feedback/docs; sync w/ Kelvin on pipeline issues
- Watch Hassan artifacts video in Notion
- Create Atlas pipeline copies; update Otto/Relay artifacts w/ Rachel; then generate 1–2 articles for Bailey feedback

**Bailey Seybolt (GrowthX)**
- Research Relay accounting/bookkeeping cluster; share seed keywords w/ Fatima; then Fatima generate assignments

---

## Transcript
**Rachel Pasche:** Hello.

**Bailey Seybolt:** How's it going?

**Bailey Seybolt:** Rachel, were you just off for Thanksgiving?

**Fatima Tahir:** You're in the U.S., right?

**Rachel Pasche:** Right.

**Rachel Pasche:** Yeah.

**Bailey Seybolt:** Happy Thanksgiving.

**Rachel Pasche:** Yeah, I hope you have a nice, it's always like, I always come back from Thanksgiving wanting to just eat like just soup or something.

**Bailey Seybolt:** So everything's so heavy.

**Rachel Pasche:** Like a salad, a vegetable.

**Rachel Pasche:** Yeah, I need to just really keep it light for a little bit.

**Bailey Seybolt:** Hi, Fatima.

**Fatima Tahir:** It's nice to meet you.

**Fatima Tahir:** Hi, likewise.

**Fatima Tahir:** Where are you guys from?

**Bailey Seybolt:** I am based in the U.S.

**Bailey Seybolt:** on the East Coast.

**Bailey Seybolt:** I'm originally from New York City, but now I live in Vermont, which if you're not familiar with U.S. geography, most people haven't heard of it. But it's like a very rural kind of mountainous state up near the Canadian border.

**Fatima Tahir:** No, I actually did like the state-wise pages for Intervel, so I didn't know the state.

**Bailey Seybolt:** That's funny. Yeah. And Fatima, where are you based?

**Fatima Tahir:** I'm based in Pakistan.

**Bailey Seybolt:** Yep.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** And did you just, you just got back from maternity leave, right?

**Fatima Tahir:** Yeah.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** Congratulations, and welcome back.

**Rachel Pasche:** Thank you.

**Fatima Tahir:** Thank you.

**Bailey Seybolt:** All right.

**Rachel Pasche:** Just curious, does GrowthX have good maternity leave, or does it vary case-by-case? How does that work?

**Fatima Tahir:** It was a 16-week maternity leave. I wasn't expecting that long, but it was great. When I had to come back, I wish I could have gotten a bit more time off.

**Rachel Pasche:** Oh, that's pretty good. I feel like at startups or small companies, it varies so much.

**Rachel Pasche:** Yeah, the baby is still so small.

**Fatima Tahir:** Yeah.

**Bailey Seybolt:** Yeah, I know. It's so different. I was in Canada when I had one of my kids, and there it's like a year of leave.

**Fatima Tahir:** Yeah, that's wild.

**Bailey Seybolt:** Go, Canada.

**Bailey Seybolt:** Hi, Kelvin.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** So I wanted to have everyone here just to talk a little bit through both Relay and Otto, the clients, and then also kind of talking about roles and priorities for kind of this week and going forward.

**Bailey Seybolt:** Um, I think the plan is, um, for Fatima to take over, um, generating the articles.

**Bailey Seybolt:** Um, but I think, Rachel, because, uh, Tiro is churning, the hope is that at

**Bailey Seybolt:** the beginning, you would be sort of available to maybe help with some editing at the beginning, I think, was Andy's thought if Fatima needed support while she's kind of, like, getting up and running and used to the new systems, which is why I wanted you here, too, just so you have, like, a little bit more context on the clients in case you get pulled in to help.

**Bailey Seybolt:** And then Kelvin is going to help make sure the handoff documents are updated and close out.

**Bailey Seybolt:** We still have some content from last week that hadn't been delivered yet.

**Bailey Seybolt:** So he's going to also help close out all that content to make sure we're kind of maintaining our velocity here.

**Bailey Seybolt:** So my thought was I wanted to check in with Fatima and Rachel, with both of you, and see what your comfort was with things like...

**Bailey Seybolt:** Keyword research with updating the artifacts and, like, being, like, working within Atlas.

**Bailey Seybolt:** Fatima, I know it probably looks a lot different than, you know, 16 weeks ago.

**Bailey Seybolt:** I imagine the systems have changed a lot.

**Bailey Seybolt:** So I'm curious, what is your comfort with things like updating artifacts in Atlas?

**Fatima Tahir:** I haven't really worked on updating the artifacts yet. I would love to still sit back and see how it's done until I'm comfortable, because I don't want to mess things up for anyone. But I think that could be somewhere where we could pull in Rachel for a little bit of help, which might be more useful than even editing after.

**Bailey Seybolt:** You can create a copy of the pipeline, which is what a lot of people are doing. That way you don't have to worry about messing up the main version. The more you learn about the voice and tone and what's not working, you're really well-situated to make those updates. I'd also recommend talking to Kelvin about what he's been seeing in post-processing. And I sent you that chat we had with Hassan about artifact improvements. The biggest thing he found was that making sure the artifacts are written in the actual voice and tone that you want for that client produces a really big change in output quality.

**Bailey Seybolt:** Updating them to reflect that is where he's seen the biggest change. I'm flagging this because we're having a similar problem with Hyper-Exponential. Both Otto and Relay recently moved on to the agentic pipeline, and we've been getting not great results, especially for Otto. I think focusing on updating those artifacts at the beginning is going to save a lot of work later on.

**Bailey Seybolt:** So I think that that could be something that would be worthwhile working with Kelvin on this week to try to make a copy of that pipeline and work on updating those.

**Fatima Tahir:** Okay.

**Bailey Seybolt:** So in terms of Otto, just to give you sort of an overview of the clients, I sent you sort of the operating manual, but just to get a sense of them.

**Bailey Seybolt:** So Otto is a travel and AI travel assistant for business travels specifically.

**Bailey Seybolt:** So it's an app that can help business travelers who don't have sort of, who usually work at a startup or a small company where they're booking their own travel.

**Bailey Seybolt:** It will help them do their flights and their hotels.

**Bailey Seybolt:** It can integrate with their calendars so they can make sure they have enough buffer time between.

**Bailey Seybolt:** meetings.

**Bailey Seybolt:** And you can, it'll track their flights.

**Bailey Seybolt:** So if there's a delay, it can kind of help you rebook your flight all through a conversational interface.

**Bailey Seybolt:** So it kind of streamlines the whole business travel process.

**Bailey Seybolt:** It's very new.

**Bailey Seybolt:** So they haven't really had all of their blog content we've done for them.

**Bailey Seybolt:** So they're sort of still getting up and running.

**Bailey Seybolt:** And we have a good runway of content and their content OS of approved article topics.

**Bailey Seybolt:** So I think in terms of choosing article topics, that's something I can help you with.

**Bailey Seybolt:** But I think in general, just like choosing one, you know, hitting each of the topic clusters each week is basically what I have been doing.

**Bailey Seybolt:** And then sometimes the client will go in and they will leave a comment on them in the air table if there's something they want to like particularly prioritize next.

**Bailey Seybolt:** In terms of an overview of the pipeline, the things that aren't working are the choppy sentences. We're getting really choppy sentences, and I think updating the artifacts is the biggest thing, because most of the artifacts are written with very choppy sentences and no transitions between them to try and keep them short. But what we found out is that means we're getting articles with really choppy sentences that all need to be fixed in post-processing.

**Bailey Seybolt:** So I think that's definitely true here.

**Bailey Seybolt:** We're getting articles that need better transitions.

**Bailey Seybolt:** And I think the biggest things that I'm seeing that are of concern is we did build a product features artifact in Atlas, but it still seems to be making mistakes and making up new features for otto that don't exist.

**Bailey Seybolt:** So I think, A, that's something to think about in terms of we should be updating the artifacts, but I think for now, especially as you're less familiar with the product itself, I think it's worth making sure you do like a fact-checking step.

**Bailey Seybolt:** And Claude just confirming that the features exist, that they're kind of positioned in the correct way, because despite the artifact being up to date in Atlas, as of last week, we're still kind of getting mistakes there.

**Bailey Seybolt:** And then I think the other thing to check is I found with Otto, we're getting links to not competitors in terms of like competing products, but sort of mindshare competitors.

**Bailey Seybolt:** So it's linking to articles that are clearly like aiming for the same keyword.

**Bailey Seybolt:** So I think checking, making sure you check the links to make sure that they're kind of accurate.

**Bailey Seybolt:** And this is something I've seen across agentic pipelines is they're not always great at choosing what to link to.

**Bailey Seybolt:** So it's something worth asking around to see who's getting really good results.

**Bailey Seybolt:** Rachel, based on your pipelines, do you know how that internal link stage is controlled? With Otto and Relay, I think we're not getting awesome results there.

**Rachel Pasche:** Yeah, I usually add an internal link target in the agentic pipelines. If you make sure that's set to the blog and not just the website, it generally narrows things down. Most pipelines just link to the website, which gives you wide-spanning results. If you specifically set it to something like otto.com/resources/blog, it narrows it down. And then I always add explicit instructions saying "do not link to anything but this" because the pipeline still isn't great at choosing contextually relevant links.

**Bailey Seybolt:** Yeah, sometimes it'll do the internal linking but pick the wrong article that doesn't make sense.

**Rachel Pasche:** Exactly. You definitely have to manually go through and check everything. I don't know that anyone's found a perfect workaround yet. We're all kind of still spending 10 minutes manually checking everything.

**Bailey Seybolt:** Well, good to know. Thanks for that guidance.

**Bailey Seybolt:** Anyone have any questions about Otto specifically?

**Bailey Seybolt:** Otherwise, I'll just run through Relay as well quickly.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** And so Relay is a banking platform that is focused on banking for small businesses.

**Bailey Seybolt:** So they serve clients like right now, they're very focused on home services.

**Bailey Seybolt:** So like, we're doing a lot of blog, like accounting for like your plumbing business, how to like manage your cash flow for other small businesses.

**Bailey Seybolt:** And they're also kind of wanting to own the AI for small businesses space, like AI apps that small business owners can use to manage their small businesses, because I think they feel like there's not a lot of content focused on that audience.

**Bailey Seybolt:** And that's an audience that probably doesn't naturally gravitate towards AI tools that might be more resistant to trusting them.

**Bailey Seybolt:** So you'll see we have a lot of topic clusters for that one, I think, because we keep adding on, like we added on the AI for small businesses.

**Bailey Seybolt:** And this week, they've handed off some documentation, and I'm going to be doing strategy and research around this new accounting and bookkeeping cluster. There's a pretty good runway of content there, but they tend to approve smaller batches of articles, so I often have to go back and ask for more. But I think we've got their approving articles for this week, and then we're going to hand off these new keywords.

**Bailey Seybolt:** So I think one place I would need support this week is probably generating some new assignments based on the keyword research for this client.

**Bailey Seybolt:** So I haven't dug into the documentation they handed off.

**Bailey Seybolt:** I'll see how straightforward it is, whether I can just hand off the keywords themselves or if it seems like they might need more context.

**Bailey Seybolt:** So I wanted to know, Fatima, what's your sort of comfort with keyword research, with kind of like generating article topics and updating Airtable?

**Bailey Seybolt:** Is that something that you did before?

**Fatima Tahir:** Yeah, I've done both, so I'm like comfortable with whatever you're assigning me because I actually personally love keyword research.

**Bailey Seybolt:** Oh, great.

**Fatima Tahir:** Yeah.

**Bailey Seybolt:** Okay, well, that's great.

**Bailey Seybolt:** Well, then I'll see at the very least, I'm going to come up with.

**Bailey Seybolt:** Like seed keywords and some direction based on what they handed off.

**Bailey Seybolt:** But my thought, my thinking is based on my conversation with them that it's going to be an expansion of what we have rather than something totally different.

**Bailey Seybolt:** So I will dig into that hopefully today or tomorrow morning and then I can kind of just keep you updated based on that.

**Bailey Seybolt:** And in terms of how the pipeline, I think the relay pipeline in general is doing a better job on a more granular level.

**Bailey Seybolt:** I think it's sometimes repeating concepts.

**Bailey Seybolt:** I find it's going too far with voice and tone.

**Bailey Seybolt:** Like they like the sort of more conversational voice and tone, but it'll sort of go straight to these conversational examples without telling you what they're for.

**Bailey Seybolt:** Like it won't say, you know, the article is about accounting best practices.

**Bailey Seybolt:** It'll jump straight to like, it's 7 a.m.

**Bailey Seybolt:** and your app is uploaded for the fifth time, you know, and then it's like you get the same kind of like way to like.

**Bailey Seybolt:** It's like all tone with no substance, I would say.

**Bailey Seybolt:** So I think drawing it back a little bit sometimes in post-processing is something that we have been doing.

**Bailey Seybolt:** Same thing, I think sometimes the internal links are really like barely related, and that's something that the client has flagged for us before.

**Bailey Seybolt:** So just another one to make sure we're checking those kind of internal links as we go.

**Bailey Seybolt:** So, but otherwise, I think if you read through those handoff docs, Kelvin's going to help update anything that's changed with the agentic pipeline, but hopefully those will give you a good sense of where we are.

**Bailey Seybolt:** And then I think if you're generating for Otto and Relay this week, know, Kelvin will be available, and obviously I'll be available to, like, answer questions and leave feedback, too.

**Bailey Seybolt:** Awesome.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** So then in terms of...

**Bailey Seybolt:** My thought was, Kelvin, if you could focus on cleaning, like, just all that content from last week, making sure that all gets updated, delivered to the client, making sure that anything with outstanding feedback gets closed out on that kind of, like, bullet point list of stuff from last week, that that all gets closed out.

**Bailey Seybolt:** So, Fatima, if you want to start generating articles for Otto and Relay, and then, you know, you could do one or two for each client, and then I think we could either put time on our calendar with you and Kelvin or the three of us to kind of talk through anything that's not working or questions you have.

**Bailey Seybolt:** And then, thinking about how to update the artifacts—there's some stuff in Notion about it. I think it's worth watching that meeting with Hassan to see how he approaches it. It's going to be something worth doing in the next week or two as well.

**Fatima Tahir:** Okay.

**Bailey Seybolt:** And then, yeah, Rachel, I'm wondering—is updating the artifacts something you feel comfortable with? Were you working on that with your other clients, or was that mostly the ME handling it?

**Rachel Pasche:** It varied based on the different clients. I would usually handle one, or we'd alternate and update things as we went. So if you guys want help updating the artifacts, I can jump in and provide some guidance or help with the process.

**Rachel Pasche:** If I do jump in and help, I think it would be best if Fatima and I did it together. When somebody else updates something you're mostly working on, it can get messy. So I'd love to help out as a collaborative effort. I think that process is more beneficial for the next time you have to update the artifact.

**Bailey Seybolt:** Yeah. My thought is, Andy had mentioned you as editing support, but I actually think if we can get better results from the artifacts, then you'll be less of an editing resource. I feel like it'll just be better for everyone long-term.

**Rachel Pasche:** So I'm thinking if we pull you in to support this week, that might make more sense than just editing articles afterward.

**Bailey Seybolt:** Yeah, for sure. So maybe that makes sense.

**Bailey Seybolt:** And the question is, based on how you're working, what's your bandwidth like? I know you'll be working on Tiro this week, so you'll be pretty busy. It's really just a question of your bandwidth and availability.

**Rachel Pasche:** Yeah, I don't know exactly how much Logic and Hyper-Exponential will require, and we're wrapping up Tiro. So I can let you know as I get into it.

**Bailey Seybolt:** That makes sense. Let's figure out how to help you prioritize your workload.

**Bailey Seybolt:** Logic is going to be, I will update.

**Bailey Seybolt:** Basically, I'm meeting with them.

**Bailey Seybolt:** They're thinking about a shift in strategy.

**Bailey Seybolt:** So I think we're going to be on pause for them, at least for Monday and Tuesday.

**Bailey Seybolt:** So Wednesday, I'm going to sync up with them and figure out how they want to execute.

**Bailey Seybolt:** So I think whatever work we have for them this week will come at the end of the week.

**Bailey Seybolt:** And for hyper-exponential, I also have to share, I think, share some new article topics with them based on new research and documentation that we got last week.

**Bailey Seybolt:** So I have to close that out today.

**Bailey Seybolt:** So it might be worth you and I also syncing because I think what we'll do is they have this new stream of comparison content that might be worth us running, I think, one or two articles sort of as calibration because we're changing how we talk about their product.

**Bailey Seybolt:** So we may just be doing more calibration this week.

**Bailey Seybolt:** We may not be running the full five.

**Bailey Seybolt:** So it actually might be a good week for you, at least at the beginning of the week, too, if you have more availability to pop in and help with the artifacts.

**Rachel Pasche:** Yeah, yeah, that sounds good because I think if we're not doing much for those two, then all I've really got going is Tiro.

**Rachel Pasche:** So I could definitely pick up some other stuff and drop in.

**Bailey Seybolt:** Awesome.

**Bailey Seybolt:** Okay, so maybe then in terms of artifact generally, working on the artifacts, maybe you and Fatima could make some time earlier this week to take a look at those.

**Bailey Seybolt:** Does that make sense?

**Bailey Seybolt:** Yeah, for sure.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** Was there anything...

**Bailey Seybolt:** Kelvin, don't know, did you want to walk through your process for how you get articles set up for Otto and Relay or handle post-processing?

**Bailey Seybolt:** Or do you feel like that's all kind of pretty captured in the handoff documents?

**Kelvin Gitari:** Well, I think the handoff document hasn't changed much.

**Kelvin Gitari:** The process that used to be there is quite similar to what I'm doing right now.

**Kelvin Gitari:** But I can try to maybe add, as you said, what's different now in that document notion.

**Bailey Seybolt:** Okay.

**Kelvin Gitari:** That's okay.

**Bailey Seybolt:** Because I haven't looked at the documents yet today, so I wasn't sure how much you had updated them last week at the end of the week when I was off.

**Kelvin Gitari:** No, I didn't get time to do that, unfortunately, last week, but I was planning to do that.

**Kelvin Gitari:** They have to edit some content that was done last week, so I'm prioritizing that first. Then I'll get to updating the documents.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** Then maybe, since I don't want to block Fatima on creating new content this week, it's worth you just talking through your process at least.

**Bailey Seybolt:** Okay, so then Fatima, maybe today and tomorrow you could focus on updating the artifacts with Rachel, and then Kelvin can update those handoff documents after he's done delivering the content from last week.

**Fatima Tahir:** Okay.

**Fatima Tahir:** Yeah.

**Kelvin Gitari:** Okay.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** That makes sense.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** And did you guys, Fatima or Rachel, did you guys have any more questions for now?

**Bailey Seybolt:** I'm sure there'll be a lot of stuff that comes up and we'll just have to sort of, you know, I'm always happy to hop on and talk live or, you know, we can do stuff in Slack async too.

**Fatima Tahir:** Yeah.

**Fatima Tahir:** I'll go through everything now, like look at the client's feedback and all and talk to Kelvin about what's not working and then we'll see where it goes.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** And if you want to run one or two articles and have me go through and leave feedback on them, I'm happy to do that, especially at the beginning while you're getting up to speed. I think that can be very useful for updating the artifacts, too—it's helpful to have feedback to work with.

**Fatima Tahir:** Yeah, yeah, that would help.

**Bailey Seybolt:** Okay, that sounds good.

**Bailey Seybolt:** Well, then I'll give everyone the last few minutes of their time back.

**Bailey Seybolt:** All right.

**Bailey Seybolt:** Bye, everyone.

**Bailey Seybolt:** Thank you.

**Bailey Seybolt:** Bye.
