# Panther <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-04
time: 20:00 UTC
duration: 25 minutes 17 seconds
organizer: Aida Knezevic (GrowthX)
speakers: Aida Knezevic, Ana Milosavic, Katie Campisi, Shannon King
speakers_count: 4
participants: Aida Knezevic (GrowthX), Katie Campisi (Panther), Ana Milosavic (Panther), Shannon King (Panther)
fathom_recording_id: 119815874
fathom_url: https://fathom.video/calls/554059478
share_url: https://fathom.video/share/mvvy2SMbpsaQQrfLKAuttP6oMayz8M2v
source: fathom
enriched_on: 2026-02-27T14:30 UTC
</metadata>

---

## Summary

Aida (covering for Kathy) reviewed content production status: 3 articles delivered and approved. Discussed new custom CTAs for CRO (5 product angles built, 2 remaining), and demoed the Atlas platform—GrowthX's proprietary content generation system with modular artifacts, multi-agent pipeline, and fact-checking. Navigation update caused a week-long deployment freeze, blocking 17 approved articles from publication.

---

## Context

This is a weekly engagement sync between GrowthX (content marketing services) and Panther (security platform). Aida Knezevic covered the call while Kathy Lam was out, serving as engagement manager and strategist for Panther's B2B content program. Shannon King, recently joined Panther's team, needed onboarding to GrowthX processes and the Atlas platform. The meeting balanced operational updates (content delivery, deployment blockers) with a deep product demo to build confidence in GrowthX's quality control and production methodology.

---

## Relevance

- **Content Operations**: Weekly Airtable review process confirmed as primary workflow; live sync feedback is more efficient than async comments. 17 articles currently blocked by site navigation deployment freeze.
- **Platform Product**: Atlas demo shows GrowthX's competitive advantage: modular artifacts, multi-agent research/draft/fact-check/edit pipeline, and human oversight for quality control.
- **Lead Generation**: CRO strategy balances authority-building content (SEO signals) with commercial evaluation-stage pieces. Custom CTAs being built by Panther's web agency (Pixel 1).
- **Client Onboarding**: Shannon King needs access to Notion content strategy doc and artifact feedback workflow. Feedback loop: article comments → Notion doc → artifact updates → applies to all future content.

---

## Overview

- **New CTAs for CRO:** GrowthX is drafting new, customizable CTAs to improve blog conversion. Panther's web agency (Pixel 1) is building the editable modules.
- **Atlas Platform Demo:** GrowthX demoed its proprietary Atlas platform, explaining how it uses modular "artifacts" (e.g., personas, style guides) and a multi-agent pipeline to produce high-quality, fact-checked content.
- **Content Workflow:** The team confirmed the weekly Airtable review process, noting live syncs are more efficient for feedback than async comments.
- **Publishing Blocked:** A site-wide navigation update has caused a week of deployment freezes, delaying the publication of 17 approved articles.

---

## Key Topics

### Content Production & Workflow

  - **Recent Deliverables:** 3 articles were delivered last week; Katie will complete a detailed review today.
  - **Strategy:** The content plan balances two goals:
      - **Authority Building:** Expert content to signal expertise to Google and LLMs.
      - **Commercial Content:** Evaluation-stage pieces for lead generation.
  - **Workflow:** The weekly Airtable review process was confirmed.
      - **Process:** Panther reviews topics, flagging for approval, changes, or rejection.
      - **Efficiency:** Live syncs are more efficient for feedback than async Airtable comments.

### CRO & CTA Strategy

  - **Goal:** Improve blog conversion rate (CRO) via new, targeted CTAs.
  - **Implementation:**
      - **GrowthX:** Drafting CTAs with specific value props for key products (e.g., Panther AI, Detection & Alerting).
      - **Panther:** Pixel 1 (web agency) is building the editable CTA modules (light/dark versions) for easy customization.
  - **Status:** GrowthX will add CTAs for Security Data Lake and Hosting Options, then share the full list for feedback.

### Atlas Platform Demo

  - Aida demoed Atlas, GrowthX's in-house content platform, to show how it ensures quality and accuracy.
  - **Core Components:**
      - **Artifacts:** Modular context for the AI.
          - `Customer Spotlights`: Case studies with URLs, problems, and outcomes for proof points.
          - `Writing Guidelines`: Broken into specific artifacts (e.g., competitor content) to prevent overwhelming the AI with conflicting instructions.
          - `Proofreader Checklists`: AI-driven checks at the end of the pipeline to enforce style and fix errors.
          - `AI-isms Editor`: Guidelines to eliminate common AI phrases and ensure a human tone.
      - **Pipeline:** A multi-agent workflow for article creation.
          - **Researcher (Tavilli/EXA):** Gathers in-depth info to prevent generic content.
          - **Fact Checker:** Verifies each paragraph against sources; rewrites unconfirmed info.
          - **Human Editor:** Performs a final top-to-bottom review for flow, tone, and link accuracy.
  - **Feedback Loop:** Panther provides feedback (e.g., "no M-dashes") in article comments. GrowthX adds this to a Notion doc to update the relevant Atlas artifact, ensuring the change is applied to all future content.

---

## Action Items

**Aida Knezevic (GrowthX)**
- Share Notion content strategy links in Slack for Shannon King (Panther)
- Post meeting recap in Slack with links for Shannon King (Panther)

---

## Transcript
**Aida Knezevic:** This meeting is being recorded.

**Ana Milosavic:** Hi, how's it going?

**Aida Knezevic:** Good, how are you?

**Ana Milosavic:** Pretty good.

**Aida Knezevic:** Great. I'm in SF this week, so I'm in a different time zone. And it took me like two days to adjust. So now today I'm feeling great. It takes time.

**Ana Milosavic:** Where are you based usually?

**Aida Knezevic:** I live in Sarajevo, Bosnia.

**Ana Milosavic:** Oh, nice.

**Ana Milosavic:** I'm also from that part of the world. I have family in Serbia, Croatia, and Bosnia. So I'm always just traveling to see them in the smaller places.

**Aida Knezevic:** Yeah, that's one of the things about being Balkan diaspora. You have family in like all of these random villages. And sometimes you have to give up part of your PTO to go to these places. Like you would rather maybe go on vacation somewhere else, but you have to go to Travnik.

**Ana Milosavic:** Yeah. I've never even been to Italy and we basically border Italy. And every time I have to spend time with family.

**Aida Knezevic:** Exactly the same. I have family in Austria and Germany. My sister's in Austria and she has to reserve part of her PTO to come home.

**Shannon King:** Sorry I'm losing my voice and was trying to eat a very fast lunch. So I was a little late. But I'm excited to chat more.

**Aida Knezevic:** No worries.

**Aida Knezevic:** Yeah, like I mentioned in the meeting agenda, I'm covering for Kathy while she's out this week and next week. My name is Aida. I'm an engagement manager and strategist at GrowthX. I've been here for over a year now. I joined when we were like 15 people. So I've seen GrowthX through different eras and phases. And right now I'm in SF and the team is really working hard improving our processes and making sure our platform and workflows are doing the best work. So part of today I wanted to show you Atlas, our in-house content platform.

**Shannon King:** So I ended up getting a bit of a demo earlier this week, but I don't know which parts I haven't seen yet. But I would love to see the latest and then be kind of a fly on the wall for Katie and Ana to do what they usually do. And I'm hoping down the road we have some really big repositioning messaging efforts underway. So we do kind of a project kickoff for those efforts in the coming weeks.

**Aida Knezevic:** Perfect. Yeah, we definitely want to keep things moving from the content production side. And any major changes that have to be done, we can always go back and make updates as needed. But just keep us in the loop. Any new docs that you create, just send them our way and we'll update everything on our end.

**Aida Knezevic:** From the content production side, we did share three articles from last week. And I was just wondering if you've had the chance to review them, if you had any high-level feedback.

**Katie Campisi:** Yes, I have been looking at them this morning and I haven't combed through with the fine-tooth comb, but these look really great. I think I'll just do that final detail scan, but looking at the topics and the sections, it looks really good.

**Aida Knezevic:** Okay, perfect. That's great. Shannon, these are for you to be aware of where you can find information easily. This is our content calendar. If you go to drafts for review, you can see what topics are currently in review, and these are the ones we're working on this week. So we're trying to do more commercial keywords that are really important for lead generation and pipeline health. So we want a healthy balance of authority building content, which is important for visibility and sending signals to both Google and LLMs that Panther is an expert in your industry, and then also these evaluation stage pieces.

**Shannon King:** Can I ask a quick basic question?

**Shannon King:** So Katie and Ana, you're going into the Airtable today. What's the workflow on our side?

**Katie Campisi:** Looking at the topic and then flagging any that we're good with, flagging any that we want changed or flagging any that we don't want to do.

**Shannon King:** And Katie, are you doing that on a weekly basis?

**Katie Campisi:** That's the plan.

**Ana Milosavic:** Whenever we have time in these meetings as well, we'll go through it. And that way we can provide more feedback. When we're going through it live without this meeting, you just can't provide as much feedback.

**Shannon King:** Okay, so it's harder to act on it through the Airtable interface, so you have to go through the GrowthX team to do that?

**Katie Campisi:** I can go in, I have access to the Airtable itself, so I can leave comments.

**Katie Campisi:** But yeah, it was, I think, was it last weekend that we went through with Kathy, like a ton live and it was way faster than when we were.

**Ana Milosavic:** Yeah, it's just easier to do it live, I think sometimes.

**Aida Knezevic:** Yeah, we have, I believe we have a ton that have been approved to start.

**Aida Knezevic:** Yeah, we have like 17.

**Aida Knezevic:** we ton that has

**Aida Knezevic:** That our team has been added to your channel where we can see when there's a publishing freeze.

**Aida Knezevic:** So we should be aware of when we can and can't publish.

**Katie Campisi:** We've also had an unusually high frequency and length of deployment freezes over the last week.

**Katie Campisi:** I feel like we have barely had any and then it's been almost entirely no deployment for a week.

**Katie Campisi:** But we're updating the navigation on the site.

**Katie Campisi:** So they've been working on that behind the scenes.

**Aida Knezevic:** Okay, okay, that makes sense.

**Aida Knezevic:** All right.

**Aida Knezevic:** And then another update. So last week we met with Ali to talk about how we're going to track blog performance and do attribution. And to improve CRO, we agreed that I would put together some CTAs that you can take to your agency that does web design and development. So I've prepared a list of CTAs. I still need to add CTAs for Security Data Lake and Hosting Options—those are the two that are missing. So I created CTAs for Demo, Panther AI, Ingestion, Search and Analytics, and Detection and Alerting. The idea is the headline is either a really big value prop or a pain point that your audience really wants to solve. The body goes into what Panther does, and then we have the CTA that takes them to the page we want them to visit. So the Demo obviously goes to the demo page, Panther AI and other pages link to different product pages that we want readers to explore. Feel free to leave comments if you want us to change something, or if there's an additional angle that you want us to highlight. Just leave a comment and we'll work it in.

**Ana Milosavic:** I did work with the Pixel 1 team to create these. The way they've created them is generic and editable. So we can go in and make edits to all of the text and the link. I think they should be live pretty soon. There's going to be two versions—a darker version and a lighter version—so you can choose whatever you think fits. You can just plug and play as you like.

**Aida Knezevic:** I love that. Okay, that's my favorite setup, where we can really customize these, because I'm sure that your website is also going to evolve and you're going to have additional pages. So it's great that we can add additional ones as needed for the content.

**Aida Knezevic:** And then for the Atlas walkthrough. So Atlas is our own in-house content generation platform that we launched last April. Before that, we were using Aerops. We have an entire team of in-house software engineers who built this platform and continue improving it, working closely with our content editorial team to make sure that the workflows work exactly as expected. It has evolved so much since it first launched and it's constantly being improved.

**Aida Knezevic:** So I want to show you where all of the different artifacts live. At the beginning of our engagement, we created artifacts like company context, products and services, audience personas, and writing guidelines. Those are the core artifacts that are really important for the articles to be accurate and in the tone that you want. However, we have also created custom artifacts like customer spotlights. This includes key case studies that we want to reference in your content. It contains URLs, the key problems, and the outcomes that Panther enabled. So every piece of content that we create includes proof points related to Panther that we can immediately reference. We also have different personas to make sure that when we're creating content for a specific persona, we are addressing the right fears and bringing up the right capabilities. And then we also have writing guidelines for competitor content. We're going to be creating listicles where we're comparing different solutions and versus articles. These types of guidelines only apply to those articles to make sure that this type of content follows very specific guidelines. And the reason why we break up these writing guidelines is because if you give LLMs too much context, the AI would just get overwhelmed. And it wouldn't follow maybe 50% of the writing guidelines because there's a token limit to how much information you can give an LLM. So these writing guidelines are only applied to the workflow where we're generating comparison or competitor content. And then we also have different proofreader checklists. The proofreader checklists are applied at the very end of the drafting stage. The AI reads the draft and then compares it to the writing guidelines and evaluates whether the content followed the writing guidelines. And if it didn't, it makes adjustments. This is because as we've been working with customers in different industries, we've noticed that sometimes the writing guidelines might be applied partially. Sometimes we're providing conflicting information to the LLM. So we might have one instruction that conflicts with another, and then the LLM doesn't know what to do. So we have this proofreader checklist at the end to make sure that we catch anything—whether that's punctuation, use of specific phrases that you don't want us to use, or specific sentence structure. The proofreader checklist catches that and makes fixes.

**Aida Knezevic:** We also have an AI-isms editor. In the sprints, we have a lead editor, her name's Sydney, and she's really an incredible editor. Her job is to make sure that this pipeline is working well and that the content doesn't read as written by AI. She uses this to eliminate those annoying phrases that come up in AI content. So we have connection phrases that the content has to use, bad examples, good examples. We read a lot of AI content every day, and we know what AI likes to do. So we try to create guidelines around that as well. We also have examples of good content here for the AI to reference, to understand what kind of content it should emulate. We have multiple pipelines here. We'll spin up test pipelines if we're experimenting with something. When we notice that something's not right with the content, we will create a test pipeline to try a different approach without impacting the primary pipeline. But the two main pipelines that we're using right now are agentic article generation for comparison and competitor articles, and then agentic article generation that covers general topics like how-to guides and topics that are more informational in nature.

**Aida Knezevic:** And this is the workflow. We've broken up the article creation process into multiple chunks. It starts with the topic. We provide the article title with a short direction so that the AI knows what to focus on. We give it the target keyword because we want to rank in Google Search. And then the next step is the AI runs a research workflow. It takes the assignment direction and generates a list of questions that it has to research and gather information on in order to create a very comprehensive research document that it's going to use in the content generation process. I don't know if you've ever tried to create an article in Claude or ChatGPT without giving it a lot of information. You would notice the articles are very short and they just repeat the same information over and over again. And that's because it doesn't have enough research to go off of. So with this step, we really make sure that the content is not just informative, but also high quality. We use Tavilli as our researcher. They're really advanced. We also have EXA if we notice that Tavilli isn't doing very well. But the reason why our content can be so in-depth and provide the right amount of information for even very complex audiences is because of this researcher. It's incredibly important to have a good researcher in the mix. After the researcher is done, then the article draft takes our assignment direction and creates the first version of the article. After this, we add the internal links programmatically, but we also do this manually at the very end. We also add source links to any third-party references that we used. We also have the proofreader checklist. We make sure that the writing guidelines were applied and it fixes anything that wasn't applied. Then we create the meta tags for SEO. Keep in mind that sometimes we will modify this depending on what the article ends up covering. We use our own judgment here. We have the fact checker. The fact checker breaks up the article into different chunks and then verifies the accuracy of each chunk using the researcher workflow. So if there's a paragraph that says that 30% of security developers use this tool, it's going to search and scrape the internet to see if there's any information that confirms this. If it cannot confirm or find a valid source, it's going to rewrite that information. However, the fact checker is very much a safeguard. We have found that our researcher does a really good job, and the fact checker doesn't have to do much in terms of correcting the information. And we also have our human editors. So after we run the fact checker, our editor is going to read this and verify any third-party links that we have. If we notice any additional AI-isms or issues with flow, we will fix that manually. So every article that we send to you, we read it from top to bottom—that's really important for me to emphasize. And the cover image we generate at the end, and that's when we will send it to you for review.

**Aida Knezevic:** Any questions, anything that I can help with?

**Shannon King:** I have some basic questions. Where you were talking about the AI styling and the rules that you can put in, let's say we want to make sure it never does an M-dash, as an example. How does the workflow work for us making that change?

**Aida Knezevic:** So you will let us know, for example, in one of the articles. Like when Katie's reviewing, she can leave a comment and say never use an M-dash again, and then we will update the artifact. What we're starting to do is create a document in Notion that summarizes all of the feedback that you've given us so far so that any feedback that you've given us is not lost and we can always go back and reference it.

**Shannon King:** So that process is owned by you guys?

**Aida Knezevic:** Yeah. And we can always add additional artifacts. We have some clients who have published reports with unique statistics or insights. And we will take those PDF reports, extract just the text, and then turn it into a statistics artifact. So every time we write an article and we have a proof point, we can back it up with real solid data. For Panther, what we could do is find authoritative reports, but we just have to make sure it's not sponsored by one of your competitors. We want to make sure it's like an industry resource that is more or less objective.

**Shannon King:** Fair enough.

**Aida Knezevic:** Yeah. Sometimes I remember when I started out in content writing at a content marketing agency called Animals. And in my early days, I'd be so excited. I found this great stat I could use in this article. And then my editor would be like, did you check the source? Like this was sponsored by their direct competitor. So I want to make sure we're not doing that.

**Aida Knezevic:** All right. So those are all the updates that I had. Shannon, I know that you joined recently, so I'm sure you're going through a lot of things. But we have the content strategy doc in Notion, and I'll share links in our Slack. So if you have any questions, feel free to tag me and Kathy and we'll get back to you. It's just important for us. Since we're in this sprint phase, we want to make sure that we make any adjustments as quickly as possible so we don't have to pivot too late.

**Shannon King:** Sounds good. Thank you. And Kathy is out this week and all of next week and then she's back?

**Aida Knezevic:** Yes, exactly. So I will be sending you your updates. Feel free to tag me if you have any questions. I'll be here.

**Shannon King:** I'm in San Francisco this week. Next week I'm in Europe.

**Aida Knezevic:** All right. I think those are all the updates that I had. Is there anything else that you wanted to discuss?

**Katie Campisi:** I'll take a deeper look at those three articles this afternoon. But like I said, they look really good. So I don't expect to have many changes, if any.

**Aida Knezevic:** Perfect. I'm really glad to hear that. All right. I think if that's it, we can wrap this up a little early. I'll send a recap in our channel and I'll send over just a list of all the main links so that you can find them easily. We'll be in touch with the five new drafts this week, and we will also let you know when the new content has been published.

**Ana Milosavic:** Amazing.

**Katie Campisi:** Thank you.

**Aida Knezevic:** Thank you. I'll see you next week. Bye.
