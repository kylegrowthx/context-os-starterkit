# Lovable <> GrowthX Weekly Sync

<metadata>
date: 2026-02-25
time: 16:30 UTC
duration: 22 minutes
organizer: team@growthxlabs.com
participants: Megan Dickey, Georgemaine Lourens, Nicolas Castellanos, Sam Vinden, Vikas Bhagat
fathom_recording_id: 125284656
fathom_url: https://fathom.video/calls/578565745
share_url: https://fathom.video/share/PotjdqzQGxx4YrTq9gz2cLDAQ63HdJXH
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

GrowthX and Lovable refined their template creation process and launched new content initiatives. Vikas will provide quality examples across the complexity spectrum to establish consistent quality standards, while Megan will grant access to Notion and Airtable artifacts for feedback. The team will also automate integration doc generation using a 3-part source of truth (PRD, PMM brief, technical docs), with Vikas delivering sample documents by end of week and Nico estimating a 3-day build for the workflow. Content volume will decrease from 15 to 10 items per week starting in two weeks.

---

## Context

Lovable is a GrowthX client for whom the team is producing content (templates, guides, blog posts) and building workflows for automation. The relationship involves two GrowthX lead engineers (Georgemaine and Nicolas) who oversee template creation and workflow development, with Megan Dickey as the director leading the account and Sam Vinden as a PMM who recently joined Lovable. This weekly sync aligns GrowthX and Lovable leadership on content strategy, template quality standards, and automation priorities. The meeting occurred about one month after Sam Vinden's start date at Lovable.

---

## Relevance

**To GrowthX Delivery:**
- Template creation process standardization: lack of quality benchmarks across complexity spectrum requires Lovable input to set consistent bar
- Content volume adjustment from 15 to 10 items/week starting in two weeks affects sprint planning and resource allocation
- Automation opportunity: integration doc generation workflow requires 3-day build, with 3-5 integration packages from Lovable by EOW to start testing

**To GrowthX Business Development:**
- Lovable relationship expansion through automation: POC with integration docs could unlock new revenue stream if workflow proves reliable
- Account health indicator: low quality of Lovable's PRDs and PMM briefs creates risk for downstream content accuracy and could impact client satisfaction

---

## Overview

- **New Content Initiatives:** GrowthX will create content (blogs, guides) for Lovable's top 5–10 use cases and automate integration doc generation.
- **Template Process Refinement:** Vikas will provide quality examples to set a consistent standard for GrowthX's template creation, which currently lacks a benchmark.
- **Source of Truth:** Vikas will provide the 3-part source of truth for integration docs (PRD, PMM brief, technical docs) by EOW, enabling Nico to build the automation workflow.
- **Content Volume Adjustment:** The steady-state content volume will decrease from 15 to 10 items/week, starting in two weeks, to match a smaller remaining task list.

---

## Key Topics

### Template Creation Process Review

  - GrowthX's template creation process uses Atlas, an internal OS, to feed LLMs with artifacts (personas, research) to generate specs.
  - **Problem:** The process lacks a consistent quality benchmark for app templates, which vary widely in complexity.
  - **Solution:** Vikas will provide 2–3 examples across the complexity spectrum to establish a clear quality bar.
  - **Action:** Megan will share the Notion/Airtable source documents for these artifacts, allowing Vikas to review and provide feedback.

### New Content Initiative: Use Cases

  - **Goal:** Promote Lovable's top 5–10 use cases to showcase the platform's capabilities.
  - **Format:** Blog posts and guides.
  - **Action:** Vikas will send the project brief with the use case list.
  - **Strategy:** GrowthX will cross-reference the list with keyword research to prioritize content that aligns with user search intent.

### New Content Initiative: Integration Docs

  - **Goal:** Automate integration doc generation to scale production beyond the current manual process.
  - **Source of Truth:** Vikas defined a 3-part input for the automation workflow:
      - Product Requirements Doc (PRD)
      - PMM Brief (messaging, audience)
      - Technical Docs (product docs)
  - **Constraint:** The current quality of PRDs and PMM briefs is low, which could compromise the accuracy of the automated output.
  - **Action:** Vikas will provide a handful of these source documents by EOW for initial testing.
  - **Timeline:** Nico estimates a 3-day build for the workflow, followed by a calibration period to refine outputs.

---

## Action Items

**Vikas Bhagat (Lovable)**
- Send Megan use-case brief + top 5–7 list; then Megan cross-check keywords
- Send Georgemaine 2–3 template examples (simple–complex)
- Send Megan 3-doc integration packages for 3–5 integrations by end of week; then Nico build workflow

**Megan Dickey (GrowthX)**
- Grant Vikas Airtable/Notion access; point to artifacts; then Vikas review/comment

**Nicolas Castellanos (GrowthX)**
- Build integration doc generation workflow (estimated 3-day build); calibrate outputs after initial testing

---

## Transcript
**Megan Dickey:** This meeting is being recorded.

**Megan Dickey:** Or I think I was also out of town.

**Megan Dickey:** I think I was also traveling.

**Megan Dickey:** Yeah, first I was out of town and then I had my eye thing.

**Megan Dickey:** So, hello.

**Georgemaine Lourens:** What was the eye thing?

**Georgemaine Lourens:** Were you getting rid of the, were you doing like laser surgery or?

**Megan Dickey:** No, I mean, I still have my glasses.

**Georgemaine Lourens:** Yeah, I noticed the glasses.

**Megan Dickey:** Yeah, no, my, my cornea is thinning.

**Megan Dickey:** So they had to like do this procedure to like strengthen the cornea so that I like don't lose vision or lose further vision.

**Megan Dickey:** So, yeah.

**Megan Dickey:** Nico, is that what your vacay looked like?

**Nicolas Castellanos:** Hey, how's going?

**Nicolas Castellanos:** It was nice.

**Megan Dickey:** How are you doing?

**Megan Dickey:** I'm trying to get my fireflies to like join this meeting and it's really.

**Georgemaine Lourens:** Oh, yeah.

**Nicolas Castellanos:** I tried to install Fathom yesterday, but I couldn't find HAL.

**Megan Dickey:** Yeah.

**Georgemaine Lourens:** Yeah, I should do that too.

**Georgemaine Lourens:** I totally forgot.

**Megan Dickey:** But as long as there's at least one nit-taker in here, that is good.

**Georgemaine Lourens:** Hey, Nico, can I ask you something technical?

**Nicolas Castellanos:** Sure.

**Georgemaine Lourens:** So I created a workflow in Flow and committed it to Prod, and I then updated it again, but it kept throwing errors that I couldn't find, like, one of the old fields.

**Georgemaine Lourens:** And I fixed that, but now Claude tells me that I'm supposed to run a job in Atlas so that it can sync with the new catalog.

**Georgemaine Lourens:** Does that sound remotely true?

**Nicolas Castellanos:** No, that job.

**Nicolas Castellanos:** Yeah, can talk about this later.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** All right.

**Megan Dickey:** Cool.

**Megan Dickey:** Hey, Sam.

**Megan Dickey:** Sam.

**Megan Dickey:** Yeah, so this is, I don't know if you've met Georgemaine and Nico before, but they are our two lead engineers on the Lovable account.

**Megan Dickey:** Yeah, Nico is, he's often tasked with, like, building out the workflow.

**Megan Dickey:** So he's the one who's been working on the tools workflow.

**Megan Dickey:** So, and Georgemaine takes lead on the templates and making sure that those are all getting created and are looking good.

**Megan Dickey:** has a design background.

**Megan Dickey:** So, yeah.

**Megan Dickey:** Yeah, is Vicas, or I'm not sure how to pronounce his name or if that's correct.

**Megan Dickey:** Is he still joining us?

**Sam Vinden:** Yeah, Vicas.

**Megan Dickey:** Vicas, okay.

**Sam Vinden:** Yeah, he should be.

**Sam Vinden:** He should be.

**Sam Vinden:** He's got a sick kid.

**Sam Vinden:** So, yeah, maybe he's dealing with that.

**Megan Dickey:** Yeah, for sure.

**Megan Dickey:** Start winding back down to just the 10 steady states.

**Megan Dickey:** like beginning next week, we're doing 15 a week.

**Megan Dickey:** And the week after, we're doing 10 a week, just as we've kind of shrunk that list.

**Megan Dickey:** So now there are just like fewer of those assignments that we need to tackle as part of that sprint.

**Sam Vinden:** Yeah, okay, cool.

**Sam Vinden:** That sounds good.

**Sam Vinden:** Let's also talk through the stuff with the cast as well, because it might be we want to like swap some guides out.

**Sam Vinden:** for like other types of pages that we want to build.

**Sam Vinden:** Perfect.

**Megan Dickey:** Yeah.

**Megan Dickey:** Cool.

**Megan Dickey:** Hey, Vikas, how are you doing?

**Vikas Bhagat:** Good.

**Vikas Bhagat:** How are you?

**Megan Dickey:** Good.

**Megan Dickey:** Yeah, I'm Megan.

**Megan Dickey:** I'm a director here at GrowthX, kind of taking lead on the Lovable account.

**Megan Dickey:** So I've been working with Sam for, I guess, like the last like two or three months, ever since Sam's first day, I believe.

**Megan Dickey:** And then we have Georgemaine and Nico.

**Vikas Bhagat:** So there are two lead engineers on the Lovable

**Vikas Bhagat:** Awesome.

**Vikas Bhagat:** It's great to meet you all.

**Megan Dickey:** I just joined about a month ago to lead our product marketing team with Sam and have had experience with the GrowthX at Webflow as well, where I was for about five years.

**Megan Dickey:** Oh, okay.

**Vikas Bhagat:** Oh, wow.

**Megan Dickey:** Nice.

**Megan Dickey:** Awesome.

**Megan Dickey:** Cool.

**Megan Dickey:** Yeah.

**Megan Dickey:** So Sam had mentioned that you kind of had some thoughts on the templates creation process.

**Megan Dickey:** And so that's why I just wanted to bring on Georgemaine and Nico since they handle everything from the engineering perspective.

**Vikas Bhagat:** So I just wanted to make sure we're able to answer any questions that you have or can even just like talk through some things live.

**Vikas Bhagat:** Yeah.

**Vikas Bhagat:** So I think like I'll walk you through kind of like what I am hoping to get done and see if GrowthX could help support.

**Vikas Bhagat:** Right.

**Vikas Bhagat:** So we have a lot of use cases of Lovable that people just aren't really aware of.

**Vikas Bhagat:** Right.

**Vikas Bhagat:** So there's a lot of things you can build from an app perspective.

**Vikas Bhagat:** We have a list of like a top hundred use cases of with Lovable.

**Vikas Bhagat:** I've narrowed that down to like the top five to 10 use cases that I really want to kind of just get out there in the world.

**Vikas Bhagat:** Top 5 to 7 that are more of our core segment.

**Megan Dickey:** Okay.

**Megan Dickey:** Yeah, for sure.

**Megan Dickey:** Yeah, I mean, we can definitely do that.

**Megan Dickey:** And so I guess in terms of like, are you envisioning them as templates, as guides, or really you just want them as any type of...

**Vikas Bhagat:** I think like blog posts and guides would kind of be what I'm thinking.

**Megan Dickey:** Okay.

**Megan Dickey:** Okay.

**Megan Dickey:** Got it.

**Megan Dickey:** And would you just be able to send me that specific list just so we can also just match that up with some keyword research to make sure...

**Vikas Bhagat:** Sure.

**Megan Dickey:** ...we're targeting those.

**Megan Dickey:** Yeah, because I would imagine that we're already targeting some of those, but I can definitely kind of do like a cross check with what we already have done, but then also look for ways to expand upon those.

**Vikas Bhagat:** Yeah, that makes sense.

**Vikas Bhagat:** I can send you kind of the project brief with the list and so forth.

**Megan Dickey:** Okay.

**Megan Dickey:** Okay.

**Megan Dickey:** Great.

**Megan Dickey:** Perfect.

**Megan Dickey:** Okay.

**Megan Dickey:** And then, but then with regards to the templates, like where's there...

**Megan Dickey:** Did you have...

**Megan Dickey:** have...

**Sam Vinden:** To, like, see the product creation flow that GrowthX uses so that you can sort of, like, feedback back on it from your perspective of, like, what you would want to see different in terms of the output.

**Vikas Bhagat:** Sure.

**Vikas Bhagat:** Makes sense.

**Megan Dickey:** Georgemaine, I was going to throw to you anyway, but you have your hand up.

**Georgemaine Lourens:** So I have a question for you guys.

**Georgemaine Lourens:** You mentioned that some of the people internally are working on, like, the top 100 use cases templates.

**Georgemaine Lourens:** And if we're going to produce those, I'm going to assume that there are some of those will be apps and also tools.

**Georgemaine Lourens:** Do you have kind of, like, quality bar examples that you kind of want to share that we can kind of, like, aim to hit in terms of apps?

**Georgemaine Lourens:** Because they can be feature-rich, right?

**Vikas Bhagat:** I don't think we have a consistent example of, like, what best-in-class high quality is.

**Vikas Bhagat:** could probably get you a sense of kind of, like, three or four.

**Vikas Bhagat:** Or versions of what the apps that people are building, the templates that people are building, but they do range in terms of maturity and like power behind the app, basically.

**Vikas Bhagat:** Some of them are very, very lightweight, whereas some of them are really, really robust.

**Vikas Bhagat:** Why don't I source like maybe two or three examples that are like kind of across that entire gamut and I can share it with you all.

**Georgemaine Lourens:** Yeah, that will be perfect.

**Vikas Bhagat:** Yeah, I can take that as an action item.

**Megan Dickey:** Okay, great.

**Megan Dickey:** Yeah, and then Georgemaine and Nico, yeah, if you just wanted to maybe like quickly kind of walk, walk through our like process of template creation, maybe just kind of starting at the, maybe at like the prompt engineering phase or wherever you feel like might be like a good, a good starting point.

**Megan Dickey:** It's like, it's after we've done like the keyword research, and I've decided what to target, then how that actually makes its way into, into lovable.

**Georgemaine Lourens:** Sure, I can.

**Georgemaine Lourens:** Then I can share some stuff.

**Georgemaine Lourens:** So where we basically started with the list of keywords.

**Georgemaine Lourens:** I think these have been handpicked by you guys.

**Georgemaine Lourens:** And based on this, we just start generating stuff.

**Georgemaine Lourens:** So maybe I can quickly tell you how.

**Georgemaine Lourens:** So this is Atlas.

**Georgemaine Lourens:** It's kind of like our OS.

**Georgemaine Lourens:** And in here, we basically have gathered quite a few things about your company, kind of like contacts, research, products, services, and also kind of like the personas.

**Georgemaine Lourens:** And all of these things are kind of like artifacts that we use to feed to the LLM.

**Georgemaine Lourens:** And depending on the keyword, what I would do is I would either start with our assistant and kind of like go through some use cases that would be usable for your personas.

**Georgemaine Lourens:** And then I'll get some ideas.

**Georgemaine Lourens:** And based on those.

**Georgemaine Lourens:** Those ideas and the complexity of the template and with complexity, mean, kind of like if it's kind of like a template for like a photographer or maybe for like a music artist, those are kind of like very simple and very photography heavy.

**Georgemaine Lourens:** So if it's something like that, then I would generate kind of like a spec.

**Georgemaine Lourens:** How that would go is we just make a new task here, kind of describe what we want to build based on what the AI assistant gave us as a use case and kind of like give it some detail.

**Georgemaine Lourens:** And then add some more stuff, like a category and the primary keyword and the text tag that Lovable uses.

**Georgemaine Lourens:** And from there on, we would just have a job that we can run and the output of that would be a spec that we can feed to Lovable.

**Georgemaine Lourens:** And maybe I can give an example or something.

**Georgemaine Lourens:** The personas that we have right now can be tailored more to what you guys have identified so far.

**Georgemaine Lourens:** Maybe we can make some updates there.

**Georgemaine Lourens:** I think by updating these artifacts, the outputs will be way better.

**Vikas Bhagat:** Can I easily access these inputs that you guys are using?

**Vikas Bhagat:** Is there like a doc on our side, Sam, that I can look at or sort of export this or something like that?

**Georgemaine Lourens:** I think we can definitely do an export and a share.

**Georgemaine Lourens:** I'm not sure if we, it's kind of like an internal tool, so I don't know if we have shared access there.

**Georgemaine Lourens:** But I can follow up with this by the next meeting.

**Megan Dickey:** Yeah, we do have this, so all this information in Notion.

**Megan Dickey:** So like, it's like everything that we have in Notion, like we've kind of already have those artifacts and we've moved those in to Atlas.

**Megan Dickey:** But because I can share with you, let me make sure you have access to this.

**Megan Dickey:** do I'm

**Megan Dickey:** Airtable.

**Megan Dickey:** And then I can also just point you to those like specific artifacts in there.

**Megan Dickey:** you can, yeah, check them out.

**Megan Dickey:** You can also like leave comments.

**Megan Dickey:** And then from there, then we can update it in Atlas.

**Vikas Bhagat:** That's perfect.

**Vikas Bhagat:** That sounds fantastic.

**Megan Dickey:** Okay, cool.

**Megan Dickey:** Okay.

**Megan Dickey:** Great.

**Megan Dickey:** Let me just find my agenda again.

**Megan Dickey:** Okay.

**Megan Dickey:** Well, then let's see.

**Megan Dickey:** That honestly might have been, oh, actually, let's chat integration docs.

**Megan Dickey:** Yes.

**Megan Dickey:** Yeah.

**Megan Dickey:** Vikas, yeah.

**Megan Dickey:** Have you been, Sam kind of brought you up to speed on what we're thinking about in terms of like integration docs and like maybe pursuing, pursuing that as a, as a work stream?

**Vikas Bhagat:** I think at a very high level, but like not details.

**Megan Dickey:** Okay, for sure.

**Megan Dickey:** Yeah.

**Megan Dickey:** I mean, essentially like, yeah, our understanding is.

**Megan Dickey:** Some folks on your team have been doing it manually, these integration docs, and we're looking to actually use our workflows to create more of them more quickly.

**Megan Dickey:** And so I know, I think like the main question though, from our side is like, what is the source of truth for those docs?

**Megan Dickey:** Like, are there already internal docs at Lovable that you're sort of like using this as that like source of truth?

**Megan Dickey:** Or like, it's like, what should we rely on?

**Megan Dickey:** Should we rely on like public API docs or like what would be, how can we ensure that our work is accurate?

**Vikas Bhagat:** I think there's three docs that I'm trying to get better at.

**Vikas Bhagat:** There's the product requirements doc, which is kind of like the bare bones product source of truth.

**Vikas Bhagat:** There's a PMM kind of on top, PMM brief that sits on top of that, which is the messaging, the audience, the pain points, the value props, et cetera.

**Vikas Bhagat:** And then the third input would be like what I call like technical docs, like actual product docs that are for like our, our.

**Vikas Bhagat:** The combination of those three feel like the right inputs to potentially use for the integration kind of content that needs to get spun up.

**Vikas Bhagat:** I will be honest with you all, the quality of the PRDs and the PMM briefs are pretty low right now, so I'm trying to get those to a higher bar.

**Vikas Bhagat:** So the input that we provide is actually accurate.

**Vikas Bhagat:** It's the right altitude.

**Vikas Bhagat:** It's the right depth from a technical.

**Vikas Bhagat:** Limitations is a great example of this.

**Megan Dickey:** We would want to make sure we are very clear about our limitations in any kind of document.

**Megan Dickey:** Right.

**Vikas Bhagat:** Have we documented that in one single place?

**Vikas Bhagat:** No.

**Vikas Bhagat:** So I'm trying to get to that point.

**Megan Dickey:** Yeah.

**Vikas Bhagat:** think those three feel like the right inputs.

**Vikas Bhagat:** Does that resonate?

**Vikas Bhagat:** Does that?

**Vikas Bhagat:** Yeah.

**Megan Dickey:** Yeah, yeah, for sure.

**Megan Dickey:** Yeah.

**Megan Dickey:** And then maybe I'll, yeah, Nico, because I think you would, well, yeah, you or then also maybe like Kirkland, who's also on our team, would probably be tasked with sort of building out that workflow.

**Megan Dickey:** And like, does that, does that all sound like manageable and like doable in terms of you, like those being the right, okay, cool.

**Megan Dickey:** Awesome.

**Megan Dickey:** Okay.

**Megan Dickey:** Great.

**Megan Dickey:** So I guess then, I guess in terms of timing, like, I guess, when do you think you might be able to get us those, those documents?

**Megan Dickey:** So that we can start.

**Vikas Bhagat:** The case here for integrations.

**Megan Dickey:** For integrations.

**Vikas Bhagat:** I think it depends on which integrations we want to focus on first.

**Vikas Bhagat:** Let me do some like homework on my side, but let's aim for end of this week.

**Vikas Bhagat:** Let's aim for end of this week for at least a handful of them, and then we can see if they are the right flavor, and then we can figure out what's working, what's not, and we can iterate from there.

**Megan Dickey:** Let's aim for end of this week.

**Megan Dickey:** Okay.

**Megan Dickey:** Great.

**Megan Dickey:** Yeah.

**Megan Dickey:** And then we can sort of, yeah, it'll take us, yeah, I guess, Nico, like, how long might it take us to sort of build out that type of workflow and get to a point where we're able to begin testing?

**Nicolas Castellanos:** Say, I don't three days, and then it might take some time to calibrate and, and.

**Nicolas Castellanos:** And refine the outputs.

**Vikas Bhagat:** It works.

**Megan Dickey:** Okay, cool.

**Megan Dickey:** Great.

**Megan Dickey:** Okay, awesome.

**Megan Dickey:** Well, yeah, well, then we'll be on the lookout for that for later this week.

**Megan Dickey:** Yeah, and then if you could get us the most popular, lovable use cases, that would also be helpful.

**Megan Dickey:** And quick question on that.

**Megan Dickey:** So they're, so they're the most popular use cases.

**Megan Dickey:** And I'm curious, like, are they also use cases that are requiring people to buy additional credits?

**Megan Dickey:** Or do you know if there's like any sort of like, any sort of like conversion data like tied to those use cases?

**Vikas Bhagat:** No, I mean, I honestly think it's like more of like, here's what's the art of the possible with lovable.

**Vikas Bhagat:** Here's some examples that are more complex than others would require like more internal tooling and more tokens, etc.

**Vikas Bhagat:** Where some of them are like so lightweight, where it's like, you don't need anything, you can just literally do it in lovable.

**Vikas Bhagat:** Others like you database.

**Vikas Bhagat:** You need authentication.

**Vikas Bhagat:** You need blah, blah, blah, blah, blah, blah, So I think, like, I can, I'll send you over, like, the full list, but I think we can pick and choose which ones make the most sense.

**Vikas Bhagat:** And we can track, I love cross-tragging with, like, the keyword search as well, right?

**Megan Dickey:** Like, what are people actually searching for?

**Megan Dickey:** And then we can prioritize those.

**Megan Dickey:** Okay, perfect.

**Megan Dickey:** That sounds good.

**Megan Dickey:** Okay, awesome.

**Megan Dickey:** Yeah, well, then I'll be on the lookout for that.

**Megan Dickey:** And then, yeah, we can sort of, yeah, I can re, I can integrate those into our current content plan, and then I'll circle back with you all on the, on the recommended next steps.

**Megan Dickey:** Okay, I think that is all for me, but, yeah, yeah, Sam, did you have anything else that you needed to check in on, or?

**Sam Vinden:** No, nothing from my side.

**Megan Dickey:** Okay, okay, great.

**Megan Dickey:** Um, perfect.

**Megan Dickey:** Okay, all good.

**Megan Dickey:** Thanks, Vikas.

**Vikas Bhagat:** got a job, guys.

**Vikas Bhagat:** Thank you.

**Vikas Bhagat:** I'll send the doc over to you later today.

**Megan Dickey:** Okay.

**Megan Dickey:** Perfect.

**Megan Dickey:** Yeah, and thanks, Georgemaine and Nico, for joining us.

**Megan Dickey:** I appreciate it.

**Megan Dickey:** And, yeah, and okay, then, I guess we will chat next time.

**Megan Dickey:** Cool.

**Megan Dickey:** Thanks, everyone.

**Megan Dickey:** All right.

**Megan Dickey:** Thank you.

**Megan Dickey:** Okay.

**Megan Dickey:** Bye.
