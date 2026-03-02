# Redis <> GrowthX - Weekly Sync

<metadata>
date: 2025-12-04
time: 17:30 UTC
duration: 25 minutes
organizer: team@growthxlabs.com
participants: Aida Knezevic, Alexis Ruiz, Allison Gregory, Cody Henshaw, Erik O'Brien, Fung-Lin Wu, Tyler Pavlas
fathom_recording_id: 106364817
fathom_url: https://fathom.video/calls/494185688
share_url: https://fathom.video/share/E5XnALqxNr9abuzjRZ4tQdRsc2qxh87r
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

GrowthX and Redis reviewed four content drafts pending technical approval from Cody's team, with Allison noting the tone had improved but flagging one draft as too formal and correcting the product name to "Redis LangCache" (not "Redis Semantic Caching"). Aida walked through Atlas, GrowthX's content generation platform, demonstrating a multi-step AI pipeline (briefing, research, validation, fact-checking, human review) that ensures quality and can be customized with additional steps like product fact-checking. The team confirmed the refresh strategy targets articles with traffic loss or low CTR, excluding the top-performing "Vector Databases" report due to proprietary benchmark data, and agreed that Redis can refresh it internally; next week Aida will deliver a Phase 1 summary to trigger a formal partnership check-in on continuation.

---

## Context

Redis is a major content marketing client for GrowthX, engaged in an eight-week content production and optimization sprint (Week 6 at the time of this meeting). The partnership focuses on creating high-quality, AI-assisted blog content around Redis products and AI/vector database topics. Aida Knezevic leads the GrowthX side as the primary point of contact, working with Redis's content and product teams (Fung-Lin Wu, Alexis Ruiz, Allison Gregory serving as tone reviewer, and Cody Henshaw as technical approver) to ensure content accuracy and alignment with Redis's brand voice and product positioning.

---

## Relevance

**To GrowthX Delivery:**
- Atlas platform's multi-step AI pipeline (brief → research → draft validation → fact-check → human review) is working effectively and can be customized with product-specific fact-checking steps to address client feedback on product mentions and accuracy.
- Product naming and technical terminology require careful review — Redis LangCache was mislabeled in drafts, underscoring the need for technical review gates before client delivery.
- Tone calibration is critical: Allison flagged one draft as too formal, indicating the writing guideline validation step in Atlas is effective but human editorial judgment remains essential.

**To GrowthX Business Development:**
- Redis is Week 6 of an 8-week engagement and has signaled a partnership continuation decision pending next week's Phase 1 summary, indicating potential for Phase 2 expansion.
- Refresh strategy (targeting traffic loss and low CTR) is data-driven and excludes proprietary content, showing sophisticated approach to content optimization that could become a repeatable service offering.
- Strong collaboration between GrowthX and Redis teams (Allison's editorial involvement, Cody's technical gate, Aida's strategic demo of Atlas) signals good account health and engagement depth.

---

## Overview

- **Drafts Pending Approval:** Four drafts await final technical review from Cody's team. Allison has approved the tone, but flagged one draft as too formal and corrected a product name.
- **Atlas Workflow Explained:** Aida demoed Atlas, GrowthX's platform, to show how a multi-step AI pipeline (briefing, research, fact-checking) ensures quality and can be customized to address specific feedback.
- **Refresh Strategy Confirmed:** The refresh list in Airtable targets articles with traffic loss or low CTR. The top-performing "Vector Databases" report is excluded due to its proprietary data.
- **Partnership Check-in:** Aida will deliver a Phase 1 summary next week, triggering a formal check-in on the partnership's future.

---

## Key Topics

### Content Drafts: Review & Approval

  - **Status:** Four drafts are pending final technical review from Cody's team.
      - **Allison's Feedback:** Tone is good overall. One draft ("agentic rag") is too formal; comments were added to adjust.
      - **Product Naming Correction:** The product name is "Redis LangCache," not "Redis Semantic Caching."
  - **Approval Process:**
      - Cody's team must provide final technical approval.
      - **Action:** Cody's team to comment "review done" in the Google Doc or Airtable, tagging Aida.
  - **Review Cadence:** Product marketer review is expected for the first \~5–6 articles to establish a baseline.

### Atlas Workflow: Ensuring Content Quality

  - Aida demoed Atlas to show how a multi-step AI pipeline ensures content quality and can be customized.
  - **Workflow Steps:**
    1.  **Briefing:** Manual outline creation and research direction to ensure comprehensiveness.
    2.  **Research:** AI uses Tavali (or EXA for complex topics) to build a detailed research document, preventing thin content.
    3.  **Drafting & Validation:** AI generates a draft, then a separate step validates it against writing guidelines (e.g., removing banned words, improving readability).
    4.  **Fact-Checking:** An AI fact-checker (powered by Tavali) verifies claims.
          - **Process:** It extracts passages, researches them, and flags unverified stats for human review.
    5.  **Human Review:** Editors perform a final manual check of all links and stats before delivery.
  - **Customization:** The workflow can be tailored to address specific feedback.
      - **Example:** A "product fact-checker" step could be added to verify product mentions for accuracy and relevance.

### Content Refresh Strategy

  - **Refresh List:** The list in Airtable targets articles with significant traffic loss or low CTR over the last six months.
  - **Manual Selection:** The list also includes recent, underperforming articles (e.g., "agentic rag," "rag accuracy") that are not yet flagged by traffic metrics.
  - **"Vector Databases" Report:**
      - **Decision:** Excluded from GrowthX's refresh scope.
      - **Rationale:** The article contains proprietary benchmark data that GrowthX cannot update.
      - **Alternative:** Redis can refresh it internally by adding new, general sections.

### Partnership Check-in

  - **Timeline:** The engagement is in Week 6 of an 8-week sprint.
  - **Next Week:** Aida will deliver a Phase 1 summary, which triggers a formal check-in on the partnership's future.

---

## Action Items

**Fung-Lin Wu (Redis)**
- Confirm with Cody: primary approver; review 'What is an AI agent' draft; have him comment 'review done' in Google Doc or Airtable and tag Aida; confirm 2 refreshes

**Aida Knezevic (GrowthX)**
- Send 5 new article drafts to Alexis/Fung-Lin/Allison by December 5
- Send Phase 1 summary + Phase 2 plan to Alexis/Fung-Lin/Allison next week; request partnership continuation decision
- Update 'Agentic RAG' draft per Allison feedback: match tone, use 'Redis LangCache' (not 'Redis Semantic Caching')

---

## Transcript
**Alexis Ruiz:** Hello.

**Aida Knezevic:** This meeting is being recorded.

**Alexis Ruiz:** How are you?

**Aida Knezevic:** I'm good.

**Alexis Ruiz:** How are you?

**Alexis Ruiz:** I'm good.

**Alexis Ruiz:** It's Thursday.

**Aida Knezevic:** The week's almost over.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Do you guys have like a holiday break or something?

**Alexis Ruiz:** So we just had Thanksgiving last week and then the next one is just Christmas, New Year's holiday.

**Alexis Ruiz:** So yeah, I'll probably take honestly like a couple of weeks off.

**Aida Knezevic:** We can have a couple of weeks.

**Aida Knezevic:** We'll see.

**Aida Knezevic:** Yeah.

**Alexis Ruiz:** So that's the next one.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** We have a client that is going to get like they do two weeks off like everybody and they're not working over Christmas.

**Aida Knezevic:** Nice.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** So that's that's pretty it's pretty cool.

**Aida Knezevic:** I know some companies do it, but it's always like December is always just it's busy, but it's also like slow because people are out.

**Alexis Ruiz:** So, yeah, exactly.

**Alexis Ruiz:** And I feel like the beginning, like right now, everyone.

**Alexis Ruiz:** It's like scrambling to finish things because before the holidays start, so.

**Aida Knezevic:** Yeah, yeah.

**Aida Knezevic:** Hi, Allison.

**Fung-Lin Wu:** Hi, Fung-Lin.

**Fung-Lin Wu:** Hi, how are you?

**Aida Knezevic:** Good.

**Aida Knezevic:** How are y'all?

**Fung-Lin Wu:** Good.

**Allison Gregory:** Hello.

**Aida Knezevic:** All right.

**Aida Knezevic:** Let me check our calendar.

**Aida Knezevic:** I think we have everybody, right?

**Aida Knezevic:** I don't think anybody else is going to join.

**Fung-Lin Wu:** I don't think so.

**Fung-Lin Wu:** I actually, yeah.

**Fung-Lin Wu:** We have a lot of people at reInvent, and it looks like Cody's a maybe.

**Fung-Lin Wu:** I know Reed's at reInvent, so I don't think she'll be joining.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Got it.

**Aida Knezevic:** All right.

**Aida Knezevic:** Great.

**Aida Knezevic:** Well, I shared our agenda in Slack, but I'm going to share my screen over here as well.

**Aida Knezevic:** So before we begin, I wanted to ask if there's anything that's top of mind for you all in terms of the content that you've been reviewing for the past, for this week and last week, or anything else that you wanted to discuss.

**Fung-Lin Wu:** Let me ask Cody, since I believe, I think he should be the primary, like the main approver of these drafts.

**Fung-Lin Wu:** So I'll select Cody right now.

**Aida Knezevic:** Okay, okay.

**Aida Knezevic:** That works.

**Aida Knezevic:** No, yeah, because the, yeah, there are four drafts that are currently being reviewed.

**Aida Knezevic:** This one has been reviewed by Allison.

**Aida Knezevic:** The remaining three, I think, are being simultaneously reviewed by Cody's team and Allison unless, yeah, I think.

**Allison Gregory:** Yeah, I, on my end, I did a quick scan of the three that were shared earlier this week.

**Allison Gregory:** If there's four, I may have missed one, but tone-wise, so feeling really good.

**Allison Gregory:** It's a lot more kind of tonally direct and conversational than some of the first examples I had reacted to.

**Allison Gregory:** So all good on my end.

**Aida Knezevic:** Looks great.

**Aida Knezevic:** Okay, perfect.

**Aida Knezevic:** Happy to hear that.

**Aida Knezevic:** Thank

**Fung-Lin Wu:** Um, all right, so then we'll be on the look at how it works.

**Fung-Lin Wu:** Like, once we approve of these four, or is GrowthX, I can go ahead and just publish it for us?

**Fung-Lin Wu:** Yeah.

**Fung-Lin Wu:** Correctly?

**Fung-Lin Wu:** Okay, okay, got it.

**Fung-Lin Wu:** Um, I'll check with Cody, but I actually believe the refreshes, I think there's a chance if Allison's good with the two refreshes, then those two of these could move forward.

**Fung-Lin Wu:** But I'll, I'll confirm.

**Allison Gregory:** I'll confirm with Cody right now.

**Allison Gregory:** I just slacked him.

**Aida Knezevic:** Yeah, I think I would say make sure there's technical review.

**Fung-Lin Wu:** Don't let me be the final.

**Fung-Lin Wu:** Okay, yeah.

**Fung-Lin Wu:** Okay, yeah, yeah.

**Fung-Lin Wu:** Okay, I would check with, uh, I just slacked Cody.

**Aida Knezevic:** I'll let you know once I hear back.

**Aida Knezevic:** Awesome, thank you.

**Aida Knezevic:** Now, I think it's totally, we're, you know, happy to do these, like, product reviews.

**Aida Knezevic:** They do slow us down a little bit, but it's important to get it right earlier rather than later.

**Aida Knezevic:** Um, and I think anything that comes up, um, during their review, we can work it into Atlas.

**Aida Knezevic:** Um, I can actually show you, because I don't believe that I've shown you how Atlas works.

**Aida Knezevic:** This So this is just a placeholder.

**Aida Knezevic:** It's not actual data.

**Aida Knezevic:** It's going to have data at some point.

**Aida Knezevic:** So this is your workspace in Atlas.

**Aida Knezevic:** is our content generation platform that we built a couple of months ago.

**Aida Knezevic:** And sort of the editorial process is created, like we create your articles in the agentic article generation pipeline.

**Aida Knezevic:** We have a couple of like other test pipelines set up because our content editors, like we, just as a company, we like to like run experiments and see what's going to get us the best output in the fastest amount of time.

**Aida Knezevic:** So this is the one that we're using right now.

**Aida Knezevic:** And it has like, the production process is broken up into multiple steps.

**Aida Knezevic:** Typically, it starts with like the topic, which can be a primary keyword, but we usually.

**Aida Knezevic:** We a whole title because it gives more direction to the workflow.

**Aida Knezevic:** And then we provide an assignment direction, which includes the primary persona.

**Aida Knezevic:** And this is connected to the artifacts that we have that you guys have reviewed already.

**Aida Knezevic:** We give it some content requirements in terms of what is old information, what is new information.

**Aida Knezevic:** How to identify quality sources, where to, like, you know, how to link out to websites.

**Aida Knezevic:** But most importantly, we give it an assignment direction in the sense that we tell it, we do our own manual research on what's ranking, you know, in search.

**Aida Knezevic:** And also, like, just what kind of information we need to provide to make sure that this article is comprehensive.

**Aida Knezevic:** And we already provided, like, a recommended article structure.

**Aida Knezevic:** So, the AI...

**Aida Knezevic:** isn't doing this process end-to-end.

**Aida Knezevic:** We kind of manipulate the outline right off the bat.

**Aida Knezevic:** And then once we are happy with this kind of brief, we run the researcher.

**Aida Knezevic:** And then this researcher, which uses Tavali, we use perplexity in the past.

**Aida Knezevic:** Now we use Tavali more often.

**Aida Knezevic:** And we use EXA when it's like a really difficult subject matter.

**Aida Knezevic:** And we need to like really find like high-quality information that might not be readily available everywhere.

**Aida Knezevic:** But Tavali is a really good researcher that we've been testing pretty heavily.

**Aida Knezevic:** And then the researcher will take a look at the brief in the first step.

**Aida Knezevic:** And then it will ask different questions that it needs to answer in order to generate a research document that the AI is going to use to generate the article.

**Aida Knezevic:** So this allows us to avoid creating thin content.

**Aida Knezevic:** I know if you've ever tried to generate an article in Claude or ChatGPT and you didn't provide it a lot of information, you would notice that it just keeps kind of repeating the same point over and over again.

**Aida Knezevic:** And it's because it doesn't have enough research to go off of.

**Aida Knezevic:** So this is how we prevent that from happening.

**Aida Knezevic:** And the research document it creates, it's pretty extensive.

**Aida Knezevic:** And once the research is over, then we generate the draft.

**Aida Knezevic:** And then we add internal links, source links.

**Aida Knezevic:** We validate the writing guidelines.

**Aida Knezevic:** And this step is really important for different reasons.

**Aida Knezevic:** So we have the writing guidelines and the writing guidelines are applied at the draft stage.

**Aida Knezevic:** However, AI, just by nature of, you know, being an LLM, sometimes follows some instructions, but ignores others.

**Aida Knezevic:** Because sometimes, like, just, we might provide.

**Aida Knezevic:** And without realizing, we might give conflicting advice to an LLM.

**Aida Knezevic:** And to a human, it sounds completely reasonable, but an LLM interprets it in a way that, like, oh, these two, like, instructions are at odds with each other, so it doesn't do either, or it follows one but ignores the other.

**Aida Knezevic:** So we added this extra step, which basically checks the draft against the writing guidelines that we have.

**Aida Knezevic:** So it might, it grades it on a scale of one to zero, and it basically just, like, evaluates the draft against the writing guidelines.

**Aida Knezevic:** And it, for example, in this draft, which I believe is just, like, a test draft that we did for you, so it's not an article that we're working on right now, but it summarizes the changes.

**Aida Knezevic:** So, for example, like, fixed, banned language by removing leverage, enable, utilize, it's, like, removed em dashes, shortened links, it added bullet points to improve readability.

**Aida Knezevic:** So these are just some of the changes.

**Aida Knezevic:** Changes that it might make, it depends on the draft, obviously, but we do have this extra step in here.

**Aida Knezevic:** After we validate the writing guidelines, we generate the SEO tags, and then we run the fact checker.

**Aida Knezevic:** This fact checker, I can actually show you how it works.

**Aida Knezevic:** So the fact checker takes the draft, and then the first thing it does, it splits the article into different chunks that it detects as needing fact checking.

**Aida Knezevic:** And then it's going to extract the passages.

**Aida Knezevic:** For example, like Gartner found that 58% of finance functions already use AI.

**Aida Knezevic:** It explains why it extracted this passage, and then it has these questions that it has to answer in order to fact check.

**Aida Knezevic:** And then it does this for all of the passages that it's extracted.

**Aida Knezevic:** And then at the end, it's going to research the different passages.

**Aida Knezevic:** And if there is an incorrect piece of information, it's going to remove it.

**Aida Knezevic:** So it's going to be deleted from the draft and replaced with an accurate one.

**Aida Knezevic:** If it cannot find a specific source to back up a claim, it's going to let us know by saying, while there is no industry source that confirms that the majority of companies use AI, it, like, there are some claims and that that's typically the way we know, okay, like the fact checker couldn't find, couldn't verify a specific stat.

**Aida Knezevic:** And it replaced the stat with like a broad kind of explanation.

**Aida Knezevic:** And then we will remove it.

**Aida Knezevic:** So it's just a sign.

**Aida Knezevic:** And for us to know that there was a piece of data there that it was originally provided, and then the fact checker couldn't verify that information.

**Aida Knezevic:** So it replaced it with a vague explanation, and then we will remove it from the final draft.

**Aida Knezevic:** And then after the fact checker is ready, we will read the final draft and do additional fact checking of our own.

**Aida Knezevic:** So we check all of the links, including internal and external links.

**Aida Knezevic:** We verify all of the stats once again.

**Aida Knezevic:** The fact checker is more like for to speed things up, but it doesn't mean that we don't do it ourselves.

**Aida Knezevic:** And then we, you know, if there are any stats that we need to replace, we will replace them or remove them.

**Aida Knezevic:** And then once it's ready, we send it over to you in a Google Doc.

**Aida Knezevic:** The point is, while I walked you through this, is that we can add additional steps here.

**Aida Knezevic:** So we have a dev team.

**Aida Knezevic:** And if it's...

**Aida Knezevic:** It turns out that your product team comes to us with feedback and says, hey, you know, we don't like the way the product is being mentioned, or there are some details that are missing.

**Aida Knezevic:** We need to make sure the explanations are more detailed, like more context-rich.

**Aida Knezevic:** We can provide an extra step here.

**Aida Knezevic:** We can work with our dev team, and we can add an extra step that's like product fact-checker, and we will provide an additional artifact that just covers all the different, you know, details about your product that is super in-depth, even more than the company context.

**Aida Knezevic:** And then at the last stage, we would run that workflow, and the fact-checker for the product would read the draft and confirm that all of the product mentions are accurate and relevant.

**Aida Knezevic:** We could also add a step that adds additional product mentions.

**Aida Knezevic:** We have a client where they just wanted us to include more product mentions in the draft, so we decided to automate.

**Aida Knezevic:** By building an extra step where the AI identifies suitable sections where we could incorporate one of their product mentions in an organic way, and it inserts it automatically.

**Aida Knezevic:** So, yeah, this is certainly like a very malleable workflow that we can customize and tailor as the, you know, as things come up.

**Fung-Lin Wu:** Thank you.

**Fung-Lin Wu:** This is, like, actually helpful to actually understand how you guys are doing the fact-checking, because I, honestly, on our, at least for me, I wasn't entirely sure what that, what that process looked like on your end.

**Aida Knezevic:** Yeah, yeah, we have a, we have a fact-checker, and, yeah, it's a, it's, you know, it has evolved a lot.

**Aida Knezevic:** I can tell you, like, when I started working at GrowthX, I've been here for, like, a year and a couple of days, and when we first started out, we were using Exa, and we've always had a fact-checker, but it has just changed so much.

**Aida Knezevic:** We were, like, using different search APIs and, you know, the approach, the dev team's approach to how they run the fact checker has also evolved.

**Aida Knezevic:** So this is the latest iteration, but, you know, as issues come up, yeah.

**Fung-Lin Wu:** What is running the fact checking?

**Fung-Lin Wu:** Is it Tavali or...?

**Aida Knezevic:** Tavali.

**Fung-Lin Wu:** Oh, it is.

**Fung-Lin Wu:** Okay.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** So, yeah, that's kind of the process end-to-end.

**Aida Knezevic:** And, yeah, and then for another update that we have is that we moved all of the glossary and blog refresh opportunities to Airtable.

**Aida Knezevic:** So when you go to the content OS, you can find the main refresh opportunities from the blog and also from the glossary.

**Aida Knezevic:** These are based on traffic loss primarily.

**Aida Knezevic:** So any glossary?

**Aida Knezevic:** Entries or blog posts that lost significant clicks over the past six months or engagement, or they have a super low click-through rate, those are the ones that are surfaced in this list.

**Aida Knezevic:** However, there are also some blog posts that were published relatively recently, like a couple of months ago, that we're kind of identifying manually, and we are also refreshing them.

**Aida Knezevic:** So the last, for example, the two refreshes that we were working on last week, targeting agentic rag and rag accuracy, those are blogs that were published a couple of months ago, but they're not performing well in search in the sense that they don't rank for a lot of keywords, and if they do, it's on page like three or four.

**Aida Knezevic:** So we can just get a lot more out of

**Aida Knezevic:** These blog posts, if we just optimize them right, and if we just, like, you know, obviously, like, not, you know, maybe rewrite it from scratch, but just, like, hit all of those SEO and AEO checks to make sure that they're, like, working for you, because they're really important for the company.

**Aida Knezevic:** And these are not, like, based on traffic, because they were published, like, in the past four or five months.

**Alexis Ruiz:** Thank you so much.

**Alexis Ruiz:** A lot, you know, like, almost, like, 90%, but this is our best-performing one.

**Alexis Ruiz:** So I was wondering if we could maybe update this one and optimize for it since it is like the best, best one for AI right now.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** This one was actually originally here.

**Aida Knezevic:** the reason why I didn't market as suitable for refresh was just one reason was because the data here is like proprietary.

**Fung-Lin Wu:** Yeah.

**Fung-Lin Wu:** I was going say, I don't know if we would want to.

**Fung-Lin Wu:** Because this is actual data.

**Fung-Lin Wu:** Yeah.

**Fung-Lin Wu:** This is actual, an actual benchmark report.

**Aida Knezevic:** What we can do is we can add like more general, like we can analyze this blog post and kind of try to come up with like additional sections we could add that maybe cover, like talk about vector databases in general and try to add to it.

**Aida Knezevic:** But in terms of updating the data, that is like, we would not touch the data.

**Alexis Ruiz:** That's the.

**Aida Knezevic:** Got it.

**Alexis Ruiz:** Yeah, yeah.

**Fung-Lin Wu:** Okay.

**Fung-Lin Wu:** I also wonder.

**Fung-Lin Wu:** I also wonder.

**Fung-Lin Wu:** I also I

**Fung-Lin Wu:** I also wonder if the sessions dropped because we used to do heavy promotion on it, and I don't know if that's...

**Fung-Lin Wu:** Yeah, maybe.

**Fung-Lin Wu:** If there's like the ad fatigue, yeah, yeah, I'm not sure, but yeah, I figured some articles, it's better to leave it as fully human, and this might be one of, like a benchmark report, like, yeah.

**Alexis Ruiz:** Okay, got it.

**Alexis Ruiz:** No, that makes sense.

**Alexis Ruiz:** It was one of Katie's questions, but yeah, makes total sense.

**Alexis Ruiz:** The, like, average sessions and engagement rates are up, but maybe because we also have less sessions, but I guess the people that are going on there are reading, like, average session is, like, over two minutes, two and a half minutes.

**Alexis Ruiz:** And engagement rate has risen, like, 53%, but the sessions, number of sessions have gone down overall, so that's the way I think she was asking, Fung-Lin.

**Alexis Ruiz:** But yeah, we can definitely leave this, definitely understand why.

**Aida Knezevic:** Yeah, I think if you want to, like, refresh it internally, just maybe, like...

**Aida Knezevic:** Like, add, like, just a little bit of, like, more updated information or just, like, have one of your, like, I don't, you know, I don't know who on internally, like, who you typically tap to write blog posts, but maybe you could have someone on your team just, like, write a couple of additional sections just to kind of refresh it and signal that it's been optimized.

**Alexis Ruiz:** Not optimized, but that it's been, like, updated.

**Aida Knezevic:** I think that could work as well.

**Aida Knezevic:** Yeah.

**Alexis Ruiz:** Okay.

**Alexis Ruiz:** Okay.

**Aida Knezevic:** Got it.

**Aida Knezevic:** Thank you so much.

**Aida Knezevic:** No worries.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Great.

**Aida Knezevic:** So, yeah, I mean, the ones that we really, like, that I kind of selected as suitable for refresh are those that are, I could see, like, okay, this was originally an SEO article.

**Aida Knezevic:** So, refreshing it is not, you know, we avoided anything that's, like, product-related or, like, just, it was clearly, like, written by a subject matter expert and it has, like, a high degree of...

**Aida Knezevic:** Just like, you know, narrative driven, like, you know, content that it's, it would just be weird if we were to just like insert like some SEO sections in there.

**Aida Knezevic:** All right.

**Aida Knezevic:** So that, that would be the update on the refreshes.

**Aida Knezevic:** And yeah, so I think once we get feedback from Cody's team, then we can, you can go ahead and stage these in your CMS.

**Aida Knezevic:** We will also send over five new articles by the end of the week.

**Aida Knezevic:** So these are the five that we are working on right now.

**Aida Knezevic:** I have a few questions about, sorry, Cody, because Cody just responded.

**Fung-Lin Wu:** One, actually, Aida, what's your experience in terms of like, is it a goal for our product marketer to always be reviewing every content or?

**Fung-Lin Wu:** Or is it just like for the first eight weeks and then hopefully eventually they could also be more hands-off?

**Aida Knezevic:** Yeah.

**Aida Knezevic:** So, I mean, not even maybe the first eight weeks, but maybe like just the first like maybe five or six articles, it would be, it's totally fine.

**Fung-Lin Wu:** I think that gives us enough data to go off of.

**Fung-Lin Wu:** Okay.

**Fung-Lin Wu:** And then I guess my other question is for Cody to respond, is there a way you want him to respond if he's done reviewing and the status of it?

**Fung-Lin Wu:** Because I'm in the, I'm in the draft for review in Irritable and I can't edit the status.

**Fung-Lin Wu:** So I didn't know if like, do you want him to just comment on it?

**Aida Knezevic:** Yeah, you can comment on it and tag me and let me know that it's done or you can comment in the Google Doc and just say that the review is done.

**Fung-Lin Wu:** Okay.

**Fung-Lin Wu:** Because I believe there's actually a couple that he's done.

**Fung-Lin Wu:** So I will tell him to you to comment.

**Fung-Lin Wu:** Okay.

**Fung-Lin Wu:** Comment on Google Doc or in the, okay.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Thank you.

**Aida Knezevic:** Thank you.

**Aida Knezevic:** Okay, great.

**Aida Knezevic:** Happy to hear that they're already kind of were able to go through some of those.

**Fung-Lin Wu:** Yeah, he was also only aware of the three, but I told him there might be there's a fourth one now to review too.

**Fung-Lin Wu:** So I'll have them add to that long.

**Aida Knezevic:** Yeah, it's the first one.

**Aida Knezevic:** It's the what is an AI agent one.

**Aida Knezevic:** I think that they missed that one.

**Aida Knezevic:** Okay, awesome.

**Aida Knezevic:** And then to give you an update.

**Aida Knezevic:** So right now we are in week six of our eight week sprint.

**Aida Knezevic:** So we are going to share next week, we're going to share like a phase one summary, just kind of like wrap, you know, just kind of summarizing everything that we've done so far and what are our plans for phase two.

**Aida Knezevic:** And in phase two, I mean, in the next week, we would also love to hear your feedback on the partnership so far and also get, you know, just a notification from you whether you intend to continue or not.

**Fung-Lin Wu:** Yeah.

**Fung-Lin Wu:** Okay.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Okay, awesome.

**Aida Knezevic:** I think those are all of the updates that I had.

**Fung-Lin Wu:** Anything else on your end?

**Fung-Lin Wu:** I don't think so, I'm on my end.

**Allison Gregory:** All good for me.

**Allison Gregory:** I did just, I was multitasking a little bit to make sure I got you a thorough review here.

**Allison Gregory:** But tonally, think overall, we're feeling really good.

**Allison Gregory:** The agentic rag one in particular feels a little bit more formal than the other two.

**Allison Gregory:** Okay.

**Allison Gregory:** So I just left a couple comments in there just to kind of match tone.

**Allison Gregory:** And then there was just one term edit for Redis LangCache where we were saying that it was via LangChain.

**Allison Gregory:** And we're calling it Redis Semantic Caching, which is not what we call it.

**Allison Gregory:** We just use that as a sentence case term, but LangCache is the name.

**Allison Gregory:** Okay.

**Allison Gregory:** So just to give a little context to the comments I just added.

**Aida Knezevic:** But overall, we're looking really good.

**Aida Knezevic:** Okay, great.

**Aida Knezevic:** That's great to hear.

**Aida Knezevic:** Um, all right.

**Aida Knezevic:** Well, I'll be in touch with the five new drafts.

**Aida Knezevic:** Um, and yeah, as soon as we get Cody's approval, we can, um, and then we resolve also your feedback, Allison, we can go ahead and stage these in your CMS.

**Aida Knezevic:** Um, who should I tag when they've been staged in your CMS to publish?

**Fung-Lin Wu:** I would tag Cody.

**Fung-Lin Wu:** Okay.

**Fung-Lin Wu:** Right, Allison, unless you feel, yeah, yeah, think Cody, yeah.

**Aida Knezevic:** Okay, great.

**Aida Knezevic:** Um, all right.

**Aida Knezevic:** Well, thank you so much for your time.

**Aida Knezevic:** Um, I'll be in touch with all the links and yeah, I'll see you next week.

**Alexis Ruiz:** Thank you.

**Aida Knezevic:** Thank you.

**Aida Knezevic:** Thank you.

**Fung-Lin Wu:** Bye.

**Fung-Lin Wu:** Bye.
