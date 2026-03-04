# Strategy Sprint Standup

<metadata>
date: 2025-10-23
time: 14:29 UTC
duration: 40 minutes
organizer: team@growthxlabs.com
participants: Aida Knezevic, Andi Bailey, Bailey Seybolt, Erik O'Brien, Hassan Rashid, Tamara Luza Jic, Will Ruzvidzo, Talal Syed
fathom_recording_id: 96285393
fathom_url: https://fathom.video/calls/449547992
share_url: https://fathom.video/share/aCny4g9yh_7GHj8neQ8yu2FsmkenGzkv
source: fathom
enriched_on: 2026-03-02 04:35 UTC
</metadata>

---

## Summary

GrowthX held a strategy sprint standup to review client deliverables across multiple concurrent engagements and resolve delivery blockers. The meeting revealed consistent patterns: writing guidelines with only sentence-level examples produce robotic AI output (affecting Anything and Hyper-Exponential), clients vary widely in their expectations and process scrutiny, and several infrastructure issues (Webflow table publishing, agentic pipeline accuracy) are blocking progress. The team aligned on fixes: paragraph-length writing examples, better deep researchers for the pipeline, and HTML/Webflow workarounds.

---

## Context

This is an internal GrowthX standup focused on multiple concurrent client strategy sprints. The meeting brought together the delivery team across content writers (Tamara, Aida), project leads (Andi, Erik), and specialist resources (Hassan, Sydney) to discuss progress on approximately 12 concurrent client engagements at various stages (u.com strategy, Fleet device management, Flight source, Hyper-Exponential, Anything, Bubble, Logic, Spectra Apps, Enable, Lovable, Base 10, Otto, Relay). The cadence is driven by weekly sprint cycles and tight client deadlines; most action items are due within 24-48 hours, indicating high-velocity delivery. Talal Syed from an external partner attended to review dashboard reporting infrastructure for one engagement.

---

## Relevance

### To GrowthX Delivery

- **Writing guidelines architecture matters:** Single-sentence examples in templates produce repetitive, robotic tone; switching to paragraph-length examples (as Aida did for "Writing like a Human" section) is already showing impact on output quality.
- **Pipeline accuracy is a bottleneck:** Heavy fact-checking required for Hyper-Exponential due to AI hallucinations and dead links; Flight source client catching minor details (manufacturers vs. companies); suggests current deep researcher or prompt engineering inadequate.
- **Webflow table publishing workaround:** Claude-generated HTML inserted into custom code blocks solves a blocking issue across multiple projects; training team on this unblocks Linear tickets.
- **Client personas and context documentation:** Fleet project shows AI's knowledge base is 2 years stale; content strategy depends on refreshing AI's understanding via fresh, accurate company context documentation.

### To CheckThat / AI Visibility

- **Writing style bias in AI training:** Observing that short examples teach AI to replicate a single "correct" style repetitively rather than learn style variation; longer contextual examples enable more natural variation.
- **AI accuracy on proprietary details:** Flight source client's exacting feedback (images, terminology precision) highlights where AI knowledge is incomplete or drift-prone; this is a prime testing ground for CheckThat's value proposition around real-time accuracy.

### To GrowthX Business Development

- **Account expansion:** Logic (backlinks/thought leadership inquiry) and Bubble (higher expectations for reporting/insights) signal upsell opportunities; pricing defined ($150–200/link for backlinks, $10–15k for thought leadership).
- **Client satisfaction risk on Bubble:** Higher expectations for insights beyond dashboards; mid-sprint check-in scheduled to reset alignment on scope and deliverables.
- **Flight source as reference/case study:** Andi flagged as a good demo case for Marcel's pipeline refinement; client is highly responsive despite demanding specs, making it valuable for testing process improvements.

---

## Overview

- **Writing Guidelines Need an Overhaul:** Use paragraph-length examples instead of single sentences. The current format produces robotic, repetitive AI output, as seen with Anything and Hyper-Exponential.
- **Client Expectations Vary Widely:** Some clients (e.g., Fleet, Flight source) require intense accuracy and process scrutiny, while others (e.g., Remkus) are highly collaborative. This requires a flexible, client-specific approach.
- **New Service Offerings Defined:** Backlinks are available via outsourcing (~$150–$200/link) but are de-emphasized due to low ROI. Thought leadership is a separate, high-touch engagement starting at $10–15k.
- **Webflow Table Publishing Solved:** A simple workaround exists: use Claude to convert tables to HTML, then paste the code into Webflow's custom code block. This unblocks several stalled Linear tickets.

---

## Key Topics

### Internal Process & Pipeline Improvements

  - **Writing Guidelines:**
      - **Problem:** Single-sentence examples in guidelines produce robotic, repetitive AI output.
      - **Solution:** Use paragraph-length examples to provide sufficient context for tone and style.
      - **Action:** Aida created a "Writing like a human" section for Anything's guidelines; this will serve as a template.
  - **Agentic Pipeline:**
      - **Problem:** The pipeline sometimes hallucinates facts or produces dead links, requiring heavy manual fact-checking (e.g., Hyper-Exponential).
      - **Action:** Andi will investigate specifying a better deep researcher within the pipeline to improve accuracy.
  - **Webflow Tables:**
      - **Problem:** Publishing articles with tables on Webflow is a known blocker, stalling several Linear tickets.
      - **Solution:** Convert tables to HTML using Claude, then paste the code into Webflow's custom code block. Suleiman is already familiar with this process.

### Client Updates

#### Fleet Device Management

  - **Strategy Presentation:**
      - **Feedback:** Client Brock approved the strategic approach but requested an additional content lane for OS updates.
      - **Action:** Aida will research the SEO value of an OS update lane.
  - **Artifacts:**
      - **Feedback:** Brock requested significant revisions to audience personas and company context.
      - **Action:** Erik has a line-by-line review with Brock tomorrow to ensure accuracy.
  - **Goal:** Use content to update AI's understanding of Fleet's current offerings, as its knowledge base is ~2 years old.

#### Flight source

  - **Feedback:** Client is highly responsive but has specific, challenging requests.
      - **Images:** Demands multiple images per article, citing a lack of images as a "clear sign of AI in 2025."
          - **Constraint:** This is not feasible; we can provide one simple image per article max.
      - **Accuracy:** Requires extreme precision, flagging minor details (e.g., "manufacturers" vs. "companies").
      - **Process:** Left feedback for the calibration article in Slack screenshots, complicating review.
  - **Action:** Andi will use this client as a demo case for Marcel to refine the agentic pipeline, testing its ability to meet such exacting standards.

#### Hyper-Exponential

  - **Pipeline Issues:**
      - **Fact-Checking:** Requires heavy manual fact-checking due to AI hallucinations and dead links.
      - **Tone:** Content sounds robotic, likely from the pipeline condensing long drafts (e.g., 4k words → 2k words).
  - **Staging:**
      - **Blocker:** 4 articles are ready for staging, but Suleiman is out today.
      - **Action:** Bailey will message Suleiman directly to prioritize the Linear ticket upon his return.

#### Anything

  - **Feedback:** Client Drew's primary concern is tone, not accuracy.
      - **Goal:** Write in a plain-spoken style like Stripe or OpenAI.
      - **Action:** Aida is updating the writing guidelines with a "Writing like a human" section and will regenerate the article.

#### Bubble

  - **Expectations:** Client seems to have higher expectations, requesting analytical reports beyond the Looker dashboard.
  - **Action:** Erik and Andi will meet with client Didi tomorrow for a mid-sprint check-in to align on expectations.

#### Logic

  - **New Service Inquiries:**
      - **Backlinks:** Client asked about backlink services.
          - **Response:** We offer it via outsourcing (~$150–$200/link) but de-emphasize it due to low ROI.
      - **Thought Leadership:** Client asked about thought leadership content.
          - **Response:** This is a separate, high-touch engagement starting at $10–15k.
  - **CMS Access:** Client will provide direct CMS access for self-staging.

#### Other Client Updates

  - **u.com:** Strategy presented; client confirmed API prioritization. Keyword research starts Monday (Tamara).
  - **Spectra apps:** Assignments reviewed; Looker dashboard set up. Calibration blog due next week (Lawrence).
  - **Enable:** 3 topics approved. Lawrence is updating guidelines with the client's AI style guide.
  - **Remkus:** 5 blogs ready for client review. Aida is drafting a Phase 2 executive summary.
  - **Lovable:** 8 blogs published. Aida will write custom template descriptions while Atlas pipeline is built.
  - **Base 10:** 1 outline sent; awaiting feedback. 3 glossary outlines are ready to send.
  - **Relay:** 9 articles published after partner bank approval.

---

## Action Items

**Aida Knezevic (GrowthX)**
- Do Fleet device management keyword research next week
- Research OS updates as Fleet content lane; decide inclusion
- Send Spectra Apps Looker dashboard link to Talal
- Update Anything writing guidelines to 'Writing like a human'; regenerate article
- Send 5 Remkes blogs to client Oct 23
- Draft Remkes Phase 2 executive summary Oct 23
- Generate custom descriptions for 5–7 Lovable templates Oct 24

**Andi Bailey (GrowthX)**
- Check in w/ Lawrence re: Spectra Apps calibration blog; ensure outputs tested
- Request Marcel demo Flight Source pipeline refinement Oct 24
- File ticket to enable Flight Source artifacts in Agentic pipeline
- Create Otto transition doc; share w/ Tamara
- Identify and specify better deep researcher for Hyper-Exponential pipeline
- Send async Notion update to Relay

**Bailey Seybolt (GrowthX)**
- Ask Logic how many backlinks/thought-leadership pieces; request pricing
- Automate Hyper-Exponential content review via Zapier (Airtable↔Notion)
- Send Hyper-Exponential ideas Notion doc to Aida Oct 23
- DM Suleiman re: Hyper-Exponential staging priority
- Rerun Relay pipeline w/ new step; assess output

**Erik O'Brien (GrowthX)**
- Review Fleet artifacts w/ Brock Oct 24; update personas/company context
- Add Andi to Bubble mid-sprint check-in w/ Didi Oct 24

**Hassan Rashid (GrowthX)**
- Review artifacts feedback patterns; propose pipeline tweaks

**Sydney Arin Go (GrowthX)**
- Send 3 Base 10 glossary outlines to Neural Oct 23

**Tamara Luza Jic (GrowthX)**
- Start u.com keyword research Oct 27
- Send 4–5 Bubble blog options to Aida; write 2 after selection
- Tag Suleiman to stage 3 Otto articles; note tables
- Write 5 Otto articles next week

**Will Ruzvidzo (GrowthX)**
- (No action items assigned in this meeting)

**Talal Syed (External)**
- (Attendee; no action items assigned)

---

## Transcript

**Aida Knezevic:** Hi.

**Andi Bailey:** How's it going?

**Aida Knezevic:** What's going?

**Bailey Seybolt:** Morning.

**Andi Bailey:** Oh boy, what does that mean?

**Aida Knezevic:** I feel like I'm a pot that's about to boil over.

**Andi Bailey:** Oh god, okay.

**Aida Knezevic:** Well, let's figure out where the bubbles are.

**Aida Knezevic:** No, I'm good, I'm good. But it's just like, I think that I just have a lot of really small client requests that have added up at the same time. And as I'm trying to do them, additional ones keep coming up. So that's like those requests that are the most—you never know how long it's going to take for you to do that.

**Andi Bailey:** Yeah. I feel that deeply, that million little things. And let's figure out if we can get you some help or what we can take away or deprioritize. As we're going through these.

**Andi Bailey:** Okay, so Fleet. Hassan, did you get to the competitor docs in Notion and the keyword gaps in Airtable?

**Hassan Rashid:** Those are all done.

**Andi Bailey:** Okay. Amazing. So are artifacts ready to send to them with the competitor docs?

**Erik O'Brien:** I'm reviewing those today. And once I get a chance to do that, I will send them over.

**Andi Bailey:** Awesome. U.com.

**Aida Knezevic:** So we presented the strategy today. It was funny because halfway through the meeting, one of the stakeholders said like we might need to tweak the clusters so that there are different clusters depending on their business line. And then halfway through the call, Brooke, who I think leads content, she was like, "Oh no, no, no, it's changed. We're back to prioritizing the API." So things are moving very quickly internally and their product prioritization literally changed in the span of a couple of minutes. So the good thing is we don't really have to change the clusters too much, Erik, if I'm right.

**Erik O'Brien:** Like, I think the conclusion was that we should leave them as they are. Yeah, I think they were going to provide any additional feedback in the doc, assuming nothing else changed.

**Aida Knezevic:** Okay, that sounds good. So yeah, next week we're going to be doing keyword research. Tamara, I will—you can already take a look at the strategy, but I'll let you know when to get started. I think we can get started early next week.

**Tamara Luza Jic:** Sure, no problem. I can get started on Monday.

**Aida Knezevic:** Yeah, yeah, that works.

**Andi Bailey:** All right. Fleet device management.

**Aida Knezevic:** That was an interesting one. I think it went well. I just think that Brock has a lot of opinions, and he shares them.

**Erik O'Brien:** What do you think, Erik? Yeah, he's a very lively character.

**Aida Knezevic:** Yeah.

**Erik O'Brien:** He's been a prospect for Fleet and now works for Fleet. He's definitely got a lot of opinions and very educated in the field. So I think he's also got a different point of view of where they should go versus the CEO. So that's an interesting kind of dichotomy we'll have to navigate.

**Aida Knezevic:** Yeah. I'm going to do the keyword research for them next week. I think overall he liked the approach, but he was definitely asking a lot of questions. Like, why are we choosing this? Why did we do—why do we want to prioritize this? I was happy that he didn't push us in a more technical direction. Like, the clusters that we picked, he liked them. He's just wants to sanity check stuff and understand our process. Yeah, I think I have to tweak some of the clusters. I think he suggested one additional content lane around different OS updates, which makes sense, but I'm not sure if there's a lot of SEO value there, considering that's more product release content, and that's something that I don't think we can support. So I'll do some more research there.

**Erik O'Brien:** And then he had quite a bit of feedback on artifacts, mainly audience personas needs a lot of work, and then company context. I have time with him tomorrow just to kind of go through it line by line and make sure there's no inaccurate information.

**Andi Bailey:** Okay, Hassan, I know this is one you worked on, and since you're going to maybe keep working on artifacts, might be good just to take a look. I can see if there's any patterns as people start reviewing the artifacts. Like, are there things that we need to tweak in the pipeline? Are there things that it's just not doing in every client? Like, we're missing this.

**Hassan Rashid:** Gotcha. Yep, sounds good.

**Erik O'Brien:** Cool. For Fleet, I mean, they know it's a problem that AI has a very distinct story for them that's about two years old. And so that's something he's reiterated that we need to fix through our content is to kind of push the AI to update their understanding of what Fleet is and what they provide.

**Aida Knezevic:** Also, another note on the writing guidelines. I know that a lot of the good versus bad examples are just a sentence long. What I would prefer it to be are paragraphs. So we can have one good paragraph, one bad paragraph. The issue is that I was actually just working on Anything's writing guidelines, and every single one of the good examples is just one sentence or two sentences. So the AI doesn't have any additional context on what good looks like outside of those examples, and it leads to all sentences sounding the same, which leads to a very robotic flow. So I think if we could change the writing guidelines to provide more longer examples of text, I think that would be helpful. And I'm also going to give this update when we get to Anything. But yeah, that's just my one because I'm seeing issues come up repeatedly in the voice and tone, and I think it's because of the examples that we're providing.

**Andi Bailey:** Okay.

**Aida Knezevic:** I think we're doing a lot of telling, right, rather than showing in the writing guidelines.

**Andi Bailey:** Yeah, so I've started to see that we have like a writing guidelines and then we have like a checker doc. So writing guidelines might be more showing and then the checker can be more telling. Spectra apps.

**Aida Knezevic:** I reviewed their assignments today. They look good for the most part. So we're just meeting them later today. I'm going to present the assignment. Their Looker dashboard has also been set up. Yeah, I think next week we're just going to have to generate a calibration blog for them. So I think, yeah, Lawrence is also helping out with this.

**Erik O'Brien:** And we got the hygienic pipeline set up yesterday.

**Aida Knezevic:** Okay, good.

**Andi Bailey:** Yeah, Lawrence, probably good to—is he here this morning? I might have just added him.

**Erik O'Brien:** Did he get included on these ones?

**Andi Bailey:** I know they're different invites. Oh, okay. Yeah, that's probably it. But, okay, I'll check in with him because if we're going to generate it for next week, then he should start playing around with the outputs this week and see what he can get. Oh, Talal, I saw you're here. So Aida, can you send the link to the Looker dashboard to Talal? It might be good to just take a look at this as the baseline Looker dashboard that we're using for reporting. So day zero, this is what it is. And if you have questions or suggestions, start compiling them.

**Talal Syed:** Yep, sounds good.

**Andi Bailey:** Cool. Enable.

**Aida Knezevic:** They approved three topics yesterday just to get us started. So I have reached out to Lawrence. I just sent him over the artifacts and also the AI style guide that they want us to use. So he's just going to update the writing guidelines with that style guide. And yeah, I think, yeah, he's working on that right now.

**Andi Bailey:** Bubble.

**Aida Knezevic:** So Tamara is working on one of their first blogs. Tamara, did you pick which ones you want to do?

**Tamara Luza Jic:** Yeah, sorry, I didn't have time. I'm working on Otto right now. So I will do that today and then we can choose one so I can write it tomorrow.

**Aida Knezevic:** Okay, okay. You can send me like four or five options, and then we can pick two. I'm a little concerned about Bubble, and I don't know if Erik feels the same way. It's just like the vibe that I'm getting is we'll give them the Looker dashboard, and they were like, "Well, we would like to get a report from you analyzing these findings and providing recommendations." And it just feels like we're not meeting these expectations that they have. I did share the refresh with them yesterday, and they were—I don't think they've reviewed it in close detail—but I did explain the different things that we changed and just told them to primarily focus on the sections where Bubble is described to make sure that we understand the new positioning. But yeah, I don't know what do you think, Erik?

**Erik O'Brien:** Yeah, I'm getting some kind of vibe from them of like they have higher expectations, but I have a check-in with Didi tomorrow, since we're at week four, just a mid-sprint check-in, so I'll chat with her and see kind of where their head's at.

**Andi Bailey:** Okay, Erik, do you maybe want to add me to that check-in? I can. Cool, yeah, thank you. Uh, Anything?

**Aida Knezevic:** So yeah, I'm updating their writing guidelines. Their big thing is what I noticed from the comments that they left was they just wanted to sound more like Stripe or OpenAI, which is very plain spoken. And I think that's what the writing guidelines were missing. So I played around a little bit and I've generated like an entire new section about "writing like a human" because I think that was Drew's big comment—that like humans don't talk this way. So I'm going to make those changes and then regenerate the article. And hopefully that's kind of closer to what they want to see.

**Andi Bailey:** Okay. So more tone than like factual or anything else.

**Aida Knezevic:** So yeah, I don't think they've had a lot of feedback on accuracy. It was more tone. And like some of the examples they wanted to replace, but I think that was about it.

**Andi Bailey:** Yeah. Flight source.

**Sydney Arin Go:** Oh, sorry, Aida.

**Aida Knezevic:** It's fine.

**Sydney Arin Go:** I just wanted to get some clarity. With Base 10, we haven't sent anything yet?

**Aida Knezevic:** We sent one outline. That outline was based on their format, and they're still reviewing it.

**Sydney Arin Go:** Okay, got it. Thanks.

**Andi Bailey:** So Flight source is—they're very responsive and they're willing to work with us, but they have, like, they have some very exacting standards. Like one thing is that they keep asking for multiple images per article, and they keep saying that a lack of images is a "clear sign of AI in 2025." But like, we can't provide five images per article. Like we can provide one, like a very simple image per article max. And they also are very particular about terminology. Like they'll flag things like we said "companies" and they wanted "manufacturers" or something very specific like that. And then they'll leave their feedback in Slack screenshots, which makes it hard for me to actually just like read it and process it all. And I think, you know, like, some of this is just the client's vibe. But I think they're also—it's a good case to use it like, Andi, I mean, Marcel, I will reach out to you about this and see if we can like use this as a demo of the agentic pipeline, testing its ability to hit these exacting standards.

**Andi Bailey:** Yeah, I think that's a good idea. I'll request a demo with Marcel for Oct 24.

**Aida Knezevic:** I think Andi also said that—oh, wait, actually, let me—okay, so on the writing—oh wait, I'm sorry.

**Andi Bailey:** No, you're good. Let me get to Hyper-Exponential quickly, because there's some stuff there that's time-sensitive.

**Aida Knezevic:** So the issue with Hyper-Exponential is like, they're very thorough and everything sounds robotic. And because the articles are being condensed from like 4,000 words to 2,000 words, and like, I feel like that might be robotic sounding because they're like, they're pulled from the middle of these bigger documents. So it's missing context sometimes and then fact-checking is like super heavy because like there are dead links and hallucinations in there. And so it takes me a long time to just like fact-check these.

**Andi Bailey:** Yeah. So we have four articles that are ready for staging, but Suleiman is out today. Bailey, can you message him and see if he can prioritize the Linear ticket for staging when he gets back?

**Bailey Seybolt:** Yeah, I can DM him.

**Andi Bailey:** Thanks. Yeah. And then for the agentic pipeline, I think, yeah, Andi—actually, I think we should specify who our deep researcher is. And I think that might improve the output. So Andi, do you think you could like, take a look at and see if there's like a better deep researcher option that we could specify?

**Andi Bailey:** Yeah, I can check that out.

**Aida Knezevic:** Okay, cool. And also Bailey, can you send that Notion doc with the ideas to Aida so she can see what's in there?

**Bailey Seybolt:** Yeah, I'll send that over.

**Aida Knezevic:** And then Bailey, there was that Zapier automation you were talking about, like, Airtable to Notion. Can we set that up?

**Bailey Seybolt:** Yeah, I think we can automate that review flow with Zapier. I'll set that up.

**Aida Knezevic:** Cool. Otto. Actually, Suleiman was supposed to be on this, but since he's out, let me just give you the quick update. So we have three articles that are ready for staging, and they have tables in them, which is part of why we're a little stuck. Tamara, can you tag Suleiman on the Linear ticket and just note that tables are in there?

**Tamara Luza Jic:** Yeah, will do.

**Aida Knezevic:** And then Tamara, you're going to write five more Otto articles next week, right?

**Tamara Luza Jic:** Yeah, yeah, absolutely. And Andi, can you, like, send me a transition doc or something so I understand how we're moving from one stage to the next with the articles?

**Andi Bailey:** Yeah, I can write that up and send it to you.

**Aida Knezevic:** Cool. Okay. Logic.

**Andi Bailey:** So Logic reached out and asked about backlinks. They were interested in backlinks and thought leadership. So we said that backlinks are available via outsourcing at like $150 to $200 per link, but we kind of de-emphasize it because the ROI is pretty low. And for thought leadership, that's kind of a separate engagement. It's kind of high touch, and it starts at like $10k to $15k. And then they're going to provide CMS access so we can stage directly.

**Bailey Seybolt:** I can reach out to them about backlinks and thought leadership and get a sense of how many pieces they want and get the pricing all set up.

**Andi Bailey:** Perfect. Okay. So other clients really quick. Remkus—Aida, you're sending five blogs today?

**Aida Knezevic:** Yeah, yeah. And then I'm also drafting their Phase 2 executive summary today.

**Andi Bailey:** Okay. Lovable, we've published eight. Aida, you're generating template descriptions?

**Aida Knezevic:** Yeah, I'm generating custom descriptions for five to seven Lovable templates tomorrow while the Atlas pipeline is being built.

**Andi Bailey:** Cool. Relay, we're at nine articles published after the partner bank approval. Bailey, you're going to rerun the pipeline with the new step?

**Bailey Seybolt:** Yeah, I'll rerun it and then assess the output.

**Andi Bailey:** Perfect. And Andi, can you send an async Notion update to Relay?

**Andi Bailey:** Yeah, I can do that.

**Andi Bailey:** Cool. All right, I think that's it. I think we crushed it today. Let's keep moving.

---

## Speaker Notes

No significant ambiguity in speaker identification. All speakers were correctly matched to their email addresses via Fathom's speaker detection. The meeting was well-structured with clear topic sequencing and action item capture.

