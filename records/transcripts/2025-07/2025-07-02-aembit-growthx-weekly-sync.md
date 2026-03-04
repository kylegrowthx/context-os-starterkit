# Aembit <> GrowthX Weekly Sync

<metadata>
date: 2025-07-02
time: 16:31 UTC
duration: 34 minutes
organizer: David Galic (GrowthX)
participants: David Galic (GrowthX), Jakub Rudnik (GrowthX), Ashur Kanoon (Aembit), Dan Kaplan (Aembit)
fathom_recording_id: 71861720
fathom_url: https://fathom.video/calls/340574537
share_url: https://fathom.video/share/wft4Tsfi_4ZXAs1TsaSZzggcx3Cmbywy
source: fathom
enriched_on: 2026-03-03 14:32 UTC
</metadata>

---

## Summary

GrowthX and Aembit reviewed progress on content creation using Atlas (GrowthX's content operating system), with focus on improving draft accuracy to 80-90% through a comprehensive knowledge base incorporating Aembit's glossary, white papers, and voice memo feedback. The team is balancing precision in technical terminology and messaging with scalable content production, including testing a new approach to repurpose existing Aembit webinars and videos into blog posts. Key blockers include finalizing the knowledge base definitions and establishing performance tracking, with two articles ready for final review before publication.

---

## Context

Aembit is a cybersecurity/identity platform (appears to focus on workload/non-human identity and access management based on discussions of Machine IAM, identity credentials, and APIs). GrowthX was engaged to help scale Aembit's content marketing by creating blog articles, webinar repurposing, and educational content that establishes Aembit as a thought leader in identity security. This is an ongoing engagement in the "calibration" phase — GrowthX is testing workflows (using their content operating system, Atlas) to produce drafts that are accurate enough to require minimal revision, while incorporating Aembit's technical voice and unique perspective on confusing identity concepts. The main challenge is balancing precision (definitions vary across industry, creating "blurry lines") with scalability, so the team is building shared artifacts (glossaries, knowledge bases) to codify Aembit's positioning for reuse across all content.

---

## Relevance

**To GrowthX Delivery:**
- Atlas workflow is maturing with new artifacts (glossaries, knowledge bases, voice memo transcripts) to improve draft accuracy and consistency
- Calibration approach (80-90% accuracy target, then human editing) is working better than pure LLM generation, but requires building domain-specific context artifacts upfront
- Content repurposing (webinars → blog posts, white papers → articles) is emerging as a high-leverage scaling lever that GrowthX can offer other technical clients
- Voice memo feedback loops are being integrated directly into workflows rather than used for post-hoc editing, improving efficiency

**To GrowthX Business Development:**
- Aembit is an active, engaged client providing regular feedback and collaborating on workflow design — strong renewal/expansion signal
- Performance tracking and SEO metrics are missing from current handoff, representing an upsell/expansion opportunity (reporting dashboard, keyword growth analysis)
- Content repurposing strategy could be packaged as a distinct service (webinar-to-blog, video library mining) for similar technical/platform companies

**To CheckThat / AEO:**
- Aembit's technical precision challenges (identity credentials vs. workload identities, APIs vs. identities, "non-human entities") are classic AEO scenarios where AI visibility depends on conceptual clarity
- Building shared glossaries and definitions to improve AI model consistency maps to CheckThat's core mission around AI-generated content quality

---

## Overview

- GrowthX is refining their content creation process using Atlas, aiming to better capture Aembit's voice and technical accuracy
- New artifacts (glossary, knowledge base) are being incorporated to improve content quality and consistency
- Repurposing existing Aembit content (webinars, videos) is a promising avenue for scaling content production
- Performance tracking and SEO impact analysis need to be more prominently discussed in future meetings

---

## Key Topics

### Content Creation Workflow Improvements

  - GrowthX is using Atlas (their content operating system) to incorporate various LLMs and Aembit-specific knowledge
  - Voice memo feedback from Aembit team is being used to guide article creation, showing promising results
  - A comprehensive knowledge base is being built, incorporating Aembit's glossary and documentation
  - Goal is to achieve 80-90% accuracy in initial drafts, reducing need for manual edits

### Content Review and Feedback Process

  - Aembit team should continue providing feedback via comments rather than direct edits
  - GrowthX is incorporating all feedback into artifacts and workflows for continuous improvement
  - Two articles ready for final review: "How to Distinguish Between Human and Non-Human" and "Machine IAM"

### Repurposing Existing Content

  - GrowthX created a blog post from Ashur's webinar as a test case
  - Dan shared additional webinar/video content for potential repurposing
  - This approach could efficiently scale content production while maintaining Aembit's voice and expertise

### Performance Tracking and SEO Impact

  - GrowthX to provide a dashboard showing content performance metrics (impressions, keywords, clicks)
  - Future discussions to focus more on performance analysis, identifying successful themes and content types
  - Both micro (individual piece) and macro (overall growth) perspectives to be considered

### Content Standardization

  - David to adjust image colors for brand consistency
  - Deckhead length and other formatting elements to be standardized across articles

---

## Action Items

**David Galic (GrowthX)**
- Incorporate Aembit glossary & docs definitions into Atlas knowledge base
- Add voice message transcripts to highlighted article sections for context
- Update article image colors for variety; adjust deckhead length for uniformity across articles

**Ashur Kanoon (Aembit)**
- Review repurposed webinar article "10 Identity Security Trends" for accuracy & key points

**Jakub Rudnik (GrowthX)**
- Share missing performance report/dashboard showing content metrics (impressions, keywords, clicks)

---

## Transcript

**Dan Kaplan:** I'm watching some Wimbledon.

**David Galic:** Nice. Who's playing?

**Dan Kaplan:** Alcaraz is playing. I live in Serbia, so it's pretty obvious who I'm partial towards. Well, going for 25 this year.

**David Galic:** Great. Right now I'm in Cedar Knowles. I grew up around areas like Wanaque and Butler.

**Dan Kaplan:** I'm down the shore, Middletown officially, which is like northern Jersey Shore, Bruce Springsteen country. Yeah, I'm a Jersey boy, living in New York now. Is Jakub joining?

**David Galic:** Yeah, yeah, he's just running a couple minutes late.

**Dan Kaplan:** And Ashur, good morning to you.

**Ashur Kanoon:** Good morning, guys.

**David Galic:** Yeah, this is the first time I'm talking with you in the morning. It's usually like late for me, 7 or 8.

**Dan Kaplan:** It is usually late for you. Well, July, the holiday is a nice time to see family.

**David Galic:** Yeah, we're going to go see some fireworks. They have them today at the local park.

**Dan Kaplan:** Now as a dog parent, I have personal opinions on fireworks. I think about all the animals that they frighten, but whatever.

**David Galic:** I've never had fireworks before, meaning July 4th stuff. As a kid we would always go to Serbia for the summer vacation, so I missed all the American summer stuff.

**Dan Kaplan:** Yeah, well Red Bank, the town I grew up next to, has a really good display on July 3rd, although I'm not sure if they're doing them anymore. The unpredictable rogue fireworks and firecrackers are the issue — the show is only 20 minutes, but there are all these random explosions.

**Jakub Rudnik:** Yeah, that's my neighborhood. You go out on the deck and it's just everywhere, not that impressive, just annoying and loud. We're trying to figure out what to do with our almost two-year-old.

**Dan Kaplan:** This will be like a five or six day event. Apurva is in Missouri and there's this theme park city with a Wild West theme. I'm thinking of Branson, Missouri. It's a popular vacation destination in the Ozark Mountains, known for family-friendly attractions.

**Jakub Rudnik:** They have an 1880s-themed amusement park called Silver Dollar City and a Titanic museum attraction.

**Dan Kaplan:** Yeah, so he won't be joining us. That'll be our big update next week.

**Jakub Rudnik:** Well, we'll jump in. David, I'm missing my URL. Was there an official agenda prepared?

**Dan Kaplan:** There was, let me share it.

**Jakub Rudnik:** Thanks. So thanks for reviewing those things. I did the scrappy rewrite version, and then David's been working on taking those voice memos and doing that more officially via Atlas. I think the edits showed us that just going into Claude wouldn't be what we'd do scalably, but Atlas doesn't have a great rewrite function yet. So that's why I went outside to Claude to test what this would look like from scratch.

**Jakub Rudnik:** For us now, we're at about 80-90% there, but the positioning is off. There's that nuance — what's going to take us across that final level? We've spent a lot of time on this first three days of this week, continuing today and tomorrow. We pulled in Panzer, and he had ideas about creating different pipelines for different areas instead of convoluting a couple of ideas. There's so much nuance to these concepts.

**Jakub Rudnik:** David took the articles that seemed close and is using the workflows we already have with his manual editing, because we want to keep production and publishing going as we do experimentation. So two articles here: "How to Distinguish Between Human and Non-Human" and "Machine IAM". I would love a final review on those. If those changes bring us across that threshold, we would publish those this week.

**Dan Kaplan:** My primary comment on the distinguish article was that there was still something fundamental. I want to make sure we're getting the core concepts right, especially the difference between identities and credentials.

**David Galic:** We're constantly building artifacts that have really precise definitions of the words and terms we're using. We're going through all your stuff and edits, making sure we're capturing what you're talking about and correcting, then feeding it into the workflows. Over time it should solidify so every time we talk about a certain concept, it's in the exact same way, the correct way.

**Jakub Rudnik:** I pulled up a document that David built into Atlas — here's the Google Doc version. He's taken all the different pieces of feedback and definitions from white papers, YouTube channel, and other things, and built this this week. Now it's feeding as an artifact to every piece of content. Our goal is to improve content, but also to see if there's any nuance missing or anything slightly off.

**Jakub Rudnik:** We can do a single edit and Atlas will understand what we're referencing — how to talk about "non-human identity" consistently. This is a long document, about 35 pages. The most important terms to get correct, I'd love your eyes on the key definitions and examples for feedback.

**Ashur Kanoon:** Just FYI, I'm looking at the first one and I want to edit the first definition. When I looked at that, I just remembered we have a glossary. I've actually gone through and defined what all these things mean to us. I've done definitions for maybe more than 100 terms.

**David Galic:** It's really long, so it's hard to ingest and put it into a format that works for the workflow. But I've already seen the glossary and we're definitely going to try to use it as much as possible. We'll find a way to put it into a format that can be easily understood and processed by the workflow.

**Ashur Kanoon:** And then our docs section as well, right? That has some definitions.

**David Galic:** We took a lot of white papers and put them into various AI tools and asked them to extract the key concepts, plus the way you guys are talking about things. It's probably a work in progress still, but our goal is to have writing guidelines capturing the style, tone, "teach first, promote less" atmosphere, and glossaries creating precise definitions.

**Dan Kaplan:** The glossary is in the docs. Okay, that's great.

**Jakub Rudnik:** All right, David, let's connect on how to incorporate these two glossaries into the Atlas document.

**Dan Kaplan:** The steps of the docs, too, I think is probably useful.

**Ashur Kanoon:** Yeah, question on the editing and commenting. I've kind of just been leaving feedback, thinking the feedback will go back into tweaking the tool. I haven't done any direct edits. Is that still the idea?

**David Galic:** I think that's the best idea because that's how we're going to get it to work. It won't work if you're just giving manual edits. Give your general thoughts on things and particular concepts, and we're going to try to incorporate that. Hopefully over time it understands better.

**Jakub Rudnik:** Every one of those edits is going into these documents and artifacts. So I appreciate all those comments. We'll circle back on this knowledge base with the two different glossaries.

**Dan Kaplan:** I think last week there were like 10 new articles, and we divvied those up between me, Ashur, and Apurva. Ashur and Apurva left voice memos largely for those, maybe some text edits. I had two. So where are we on those?

**David Galic:** So those two that you left edits for, I've tried to make edits based on your feedback. For the ones that had voice messages, we wanted to try a new approach. We have this workflow part that has assignment descriptions giving not just the keyword being targeted, but what the topic should be about and what the focus should be. We found voice messages are really good for defining the key points.

**David Galic:** We have one example for you guys to look at. I highlighted a section where I feel the workflow understood the direction of the voice message and what it was conveying. I just want eyes on that once you have time — is that close to the idea conveyed through the voice message? By the end of today, I want to have all the ones with voice messages put through the workflow again so we can see if the results are getting closer to the messaging.

**Jakub Rudnik:** Can you show where in the document you've highlighted?

**David Galic:** So it's a section called "Why APIs Aren't Identities and Other Misconceptions."

**Jakub Rudnik:** Let me highlight it so I don't forget.

**David Galic:** This is my first time screen sharing on this computer.

**Jakub Rudnik:** Never mind. But this is the big piece of feedback from that voice memo. This is where we just need eyes. If we're at 80-90% of the way there, this is that direct feedback. We've done this with this one, felt really good with how the voice memo pulled into Atlas. Reviewing this article for that section, we want sign-off, then we'll take that exact flow and do it to the other articles. We didn't want to do it six times and have it fall flat again.

**Jakub Rudnik:** So if we get that feedback, we'll rework the additional ones with voice memos using Atlas rather than Claude. Then we'll send those by end of day. But pending the review of the workload identity versus workload access management rewrite.

**David Galic:** I think if you look at these two versions, the first one is probably better structured and easier to read. But we really want you to look at the second version, the pure workflow version where we didn't do a lot of manual editing before and after. We just want to see if the workflow with voice message stuff and the new artifacts is really getting it more correct than we have in previous trials.

**Jakub Rudnik:** Which one works best?

**David Galic:** So it's the one I shared.

**Dan Kaplan:** I just want to minimize where I don't want to send over too much.

**Jakub Rudnik:** We need to review one section to understand what that is.

**David Galic:** I'm going to send that document and review that one section in particular. Then if you have time, compare the two versions and see if the second version is meeting the voice better than we had in the past.

**Dan Kaplan:** Was this the one you left a comment on?

**Ashur Kanoon:** No.

**Dan Kaplan:** Cool. I'll review whoever commented.

**David Galic:** Also, I can add a link to the transcript for the voice message in that highlighted section so you have clarity.

**Dan Kaplan:** And when that voice feedback is given, the entire article is re-examined, reassessed, and revised, right? Not just a new section inserted?

**Jakub Rudnik:** Right. The reworks we sent over that still had feedback were reworked throughout. This one is starting from scratch the way we'd normally do a workflow, but we've added article instructions with voice memos, which we hadn't had before. So it's creating a brand new article. We had an old version, now we have this new one. We want to compare them, but especially look at the new section — that's where I think we're missing on flow. How does this actually connect to Aembit? What's Aembit's perspective?

**Jakub Rudnik:** People are talking about these ideas in different ways with blurry lines on the edges. We're trying to make sure we hit your perspective and nail that — it'll be the most accurate. But you're also carving out the space between categories, being that thought leader. We need to get that right, and both sides need to feel good about it.

**Ashur Kanoon:** Is Atlas your homegrown LLM?

**Jakub Rudnik:** Atlas is not, it's like our replacement for AirOps, our content operating system, but pulling in LLMs in different ways. We have your pipeline, artifacts feeding into Atlas, which uses different LLMs at different points of the content process. There are micro steps — Claude over here, other models there. So different LLMs for research, writing, knowledge base, personas, other things. It's not a single LLM, but all LLMs plus inputs from our end.

**Dan Kaplan:** It's like a calibration engine or workflow.

**Jakub Rudnik:** It's like a context engine. AirOps is a content operations platform, but we're doing that plus building on top of it. I think Marcel talked with Apurva on this, but we're using it internally for all these operations. That's what's happened in the last two weeks as we calibrate. We're still figuring out the limits and what gets the best results, especially on this technical client. Coming down the road, it'll be open for you to use for different content types and knowledge work. That'll be in a couple months.

**Ashur Kanoon:** That makes sense.

**Jakub Rudnik:** We can show you what's built once we have one workflow that works and explain why it's working. But as we're calibrating, we'll have those articles reformatted today or tomorrow depending on feedback from the workload identity article. On top of these two we'd like to publish, David created additional articles in a different format — test cases showing what GrowthX does well or where we can continue publishing and scaling.

**Jakub Rudnik:** One brand new one: Ashur, you took a webinar you did historically and we turned that into a blog post. You've got so much perspective baked into that webinar. The article is "10 Identity Security Trends." We wanted eyes on this format because we can do this to basically your whole YouTube library. We have a library that hasn't had content repurposed. We can do this from white papers too.

**Jakub Rudnik:** Repurposing content you already have and turning it into really good blog content would help us get the voice right while figuring out the other nuances. We haven't done a ton of this yet, but it's really scalable to supplement net new content from scratch. This could be a good addition.

**David Galic:** I've seen that Dan has already turned some webinars into blog posts. I think that's something we can do.

**Dan Kaplan:** We're posting a Snowflake one actually that we did. But I haven't really gone beyond that. Definitely wherever we can repurpose is great.

**David Galic:** We can check out all different kinds of things. If we can take the stuff you already have and repurpose it into really good blog content, it'll help us get the voice right and get everything right while we're figuring out the other nuances. Keep the needle moving.

**David Galic:** So Ashur, I'd be really interested if you take a look at this and see how much it understood what you were saying and your key points from the webinar. I think it was the one where you visited a conference and shared your thoughts and what you learned.

**Ashur Kanoon:** I'll take a look at it right after this meeting. So, going forward, what's our plan on performance and SEO? Is it collaborative between GrowthX and Aembit?

**Jakub Rudnik:** It is collaborative in some ways. We should have a dashboard showing the content we published, impressions, keywords, clicks. Building on that, we'll start building in conversion data. I'm not seeing that link, so I'll have to ensure it's been created. But we should have that accessible for both sides at all times. Beyond that, we're looking at micro and macro perspectives.

**Jakub Rudnik:** We should see keyword and traffic growth. In the short term, we're still newer for publishing and scaling, but should see clicks expand over time and rankings improve. We'll look at individual pieces — what articles, what themes, whether at cluster level or article type, are seeing performance. Where are we getting traction and doubling down on that with new publishing.

**Jakub Rudnik:** We'll do a lot of analysis and bring findings to you. Should be doing that each week. Typically beyond the calibration phase, we spend so much time getting that right that we haven't focused on those conversations. But as those move forward, we should talk about it each week. We'll send the performance report as soon as we can.

**Ashur Kanoon:** Good callout. Definitely part of this and what you should be providing.

**Dan Kaplan:** I dropped in a couple of videos from webinar sessions we did at an event. David sat on one, and there was another kind of Snowflake-Aembit discussion. When we have net new content creating outside of our walls, is that the right place to put it?

**Jakub Rudnik:** Yeah, please do. Let's just start repurposing those. It informs and pulls into Atlas in different ways. But we should look at the repurposing opportunity for every piece. Confirm with Aembit that you're not crossing streams, but build it into the plan.

**David Galic:** I downloaded the files yesterday, so I'm definitely going to see what we can do with it.

**Dan Kaplan:** And the other blogs with feedback are still in motion.

**David Galic:** Everything you've seen and left comments or voice messages on will be ready for another look by end of week. It's going to be a combo of seeing if we can put it in the workflow with voice message prompts, and the other ones will go through regular editing, ready for publishing as soon as possible.

**Dan Kaplan:** When the next thing gets published, David, can you adjust the image colors to vary them? And standardize the deckhead length across articles?

**David Galic:** Yes, I'll do that today. She's very strict with the aesthetics, but I can do that today.

**Dan Kaplan:** And I know I forwarded ideas about Copilot and Rapid API. I'd love to see those get done. It's worthwhile leaning into industry brand terms and how they relate to what we do.

**David Galic:** Yeah, it's all on our radar. The numbers may say other directions we're taking will be better. We'll take a look at what's live and go from there. It's a bunch of updates over the next couple days before you enjoy your 4th of July.

**Dan Kaplan:** Ashur, anything else?

**Ashur Kanoon:** No, I think we're good. Thank you both. We'll get those updates.

**Jakub Rudnik:** All right. Cheers, guys. Appreciate it.

---

*Note: First ~20 minutes of the meeting consisted of informal discussion about July 4th holiday plans and locations. Meeting content starts with discussion of Atlas workflow and article calibration.*
