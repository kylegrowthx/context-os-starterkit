# Sunbit <> GrowthX - Weekly Sync

<metadata>
date: 2025-11-06
time: 17:01 UTC
duration: 18 minutes
organizer: team@growthxlabs.com
participants: Ehtisham Hussain (GrowthX), Kyle Gaudreau (GrowthX), Jason Beltran (Sunbit), Angel Kemper (Sunbit), Jenny Macrohon Dabon (GrowthX)
fathom_recording_id: 99768170
fathom_url: https://fathom.video/calls/464555722
share_url: https://fathom.video/share/MT7-b59gf9zQbL6U7AGbDUvNa-WKn-fy
source: fathom
enriched_on: 2026-03-02 00:00 UTC
</metadata>

---

## Summary

Ehtisham presented Sunbit's weekly traffic metrics, highlighting a suspicious spike (813 sessions vs. 400 avg) caused by ~400 bot-driven zero-second pages that didn't affect key conversion events. The team aligned on an LLM training strategy: create short Q&A pages for 4 personas (dental patient/clinic owner, auto repair customer/shop owner) to position Sunbit as an expert in LLM responses, with pages crawlable for SEO/AEO synergy and tracked via Scrunch. Jason approved an aggressive tone for the "Sunbit vs. Cherry" competitive positioning doc (Dental only; auto competitors are Dignify and Affirm) pending his written feedback.

---

## Context

This is a weekly sync between GrowthX (content and AEO strategist) and Sunbit (point-of-sale financing platform for dental and auto repair). GrowthX is delivering content marketing and LLM visibility work for Sunbit, addressing two core problems: (1) bot-driven traffic anomalies that distort performance metrics, and (2) the need to influence LLM responses to include Sunbit as a default answer for financing questions across target verticals. The meeting happens in the context of a content backlog approval and publishing pipeline that GrowthX is working through with Sunbit's legal team.

---

## Relevance

**To GrowthX Delivery:**
- LLM training strategy requires creating Q&A pages (~150-200 questions per persona, grouped across 4 personas) — substantial content production effort with tracking requirements via Scrunch
- SEO/AEO synergy: Pages will be crawlable by both search engines and LLMs, creating dual benefit for organic and LLM visibility
- Competitive positioning requires aggressive initial tone in drafts, then legal review/pullback — workflow impacts deadline and legal resource planning

**To CheckThat:**
- LLM prompt tracking opportunity: Scrunch can monitor how often Sunbit is mentioned in LLM responses for dental and auto repair financing topics
- AEO strategy live: This is a working example of AEO methodology (influencing LLM training data via expert positioning) vs. traditional SEO

**To GrowthX Business Development:**
- Traffic anomaly investigation shows data quality issue — important for future account health scoring (need to filter bot activity from real metrics)
- Backlog volume still substantial; content publishing cadence critical for momentum
- Client approval cadence is healthy (Jason actively reviewing docs, providing feedback)

---

## Overview

- **Traffic Anomaly:** A traffic spike (813 sessions vs. 400 avg) was caused by \~400 pages with 0-second sessions, likely a bot or internal crawler. Key events remained stable, confirming the anomaly.
- **LLM Content Strategy:** A new strategy will create Q\&A pages for 4 personas, embedding Sunbit as the expert to train LLMs. Pages will be crawlable for SEO and internal linking benefits.
- **Competitive Positioning:** The "Sunbit vs. Cherry" strategy will be aggressive, per Sunbit's "take the gloves off" directive. The scope is Dental only; auto competitors are Dignify and Affirm.

---

## Key Topics

### Traffic Anomaly Investigation

  - An unusual traffic spike was detected, prompting an investigation into its cause.
      - **Metrics:** Sessions doubled (813 vs. 400 avg); engagement time dropped (42s vs. 1:26 avg).
      - **Cause:** \~400 pages with 0-second sessions, likely a bot or internal crawler.
  - Key events were unaffected, validating the anomaly:
      - Shop directory views: 309
      - Become a partner form: 1 (suspected test)
      - Find Sunbit clicks: 4

### LLM Content Strategy

  - A new strategy was proposed to influence LLM responses by positioning Sunbit as the expert.
  - **Method:** Create short Q\&A pages (not full articles) for 4 personas:
      - Dental Patient & Clinic Owner
      - Auto Repair Customer & Shop Owner
  - **Execution:**
      - Group \~150-200 questions per persona into themed pages.
      - Embed Sunbit as the source (e.g., "according to experts at Sunbit").
      - Direct LLMs to crawl these pages via the `LLMS.pxt` file.
  - **Decision:** Make pages crawlable by search engines.
      - **Rationale:** Capture organic traffic and enable internal linking. Kyle (GrowthX) supports this for SEO/AEO synergy.

### Competitive Positioning: Sunbit vs. Cherry

  - The "Sunbit vs. Cherry" strategy will be aggressive, per Sunbit's "take the gloves off" directive.
  - **Scope Correction:** The competitive focus is Dental only.
      - **Auto Competitors:** Dignify and Affirm.
  - **Action:** Jason will review the strategy document and provide feedback.

---

## Action Items

**Ehtisham Hussain (GrowthX)**
- Monitor traffic for abnormal spike next week; update Jason/Angel
- Collect LLM plan feedback from Jason/Angel; finalize w/ Kyle; start execution
- Update Sunbit vs Cherry doc: remove auto; add Dignify; adopt aggressive tone
- Add LLM persona questions to Scrunch prompt section

**Jason Beltran (Sunbit)**
- Review Sunbit vs Cherry doc; add comments; approve

---

## Transcript
**Jason Beltran:** This meeting is being recorded.

**Ehtisham Hussain:** Hi, Angel.

**Angel Kemper:** Hello.

**Ehtisham Hussain:** Let me see.

**Ehtisham Hussain:** We should wait for Kyle for a bit.

**Ehtisham Hussain:** So have you guys been, have you guys been publishing stuff recently?

**Ehtisham Hussain:** There's a lot of testing going on on the website.

**Ehtisham Hussain:** Because I saw, I saw like a major, major spike.

**Ehtisham Hussain:** I have that in my report.

**Ehtisham Hussain:** But that spike is kind of abnormal in traffic.

**Ehtisham Hussain:** And it shows like there's a lot of one session, new pages that are on there with zero seconds on the page.

**Jason Beltran:** No, not that.

**Jason Beltran:** I don't, yeah, I don't, I don't know what you're referring to.

**Ehtisham Hussain:** Yeah.

**Ehtisham Hussain:** Okay, I'll show it, I'll show it in my book.

**Ehtisham Hussain:** Okay, so we got Sunbit versus Cherry.

**Jason Beltran:** Yeah, and Angel keeps on going in and she's like updating what's been approved by our legal team in the Airtable.

**Jason Beltran:** And then we've published a few articles, but we're like trying to get, we just have that huge backlog that we're trying to get in order.

**Ehtisham Hussain:** Oh, yeah.

**Ehtisham Hussain:** Yeah, there's a lot of new approved articles.

**Ehtisham Hussain:** So I'm just going to get started.

**Jason Beltran:** All right.

**Ehtisham Hussain:** Okay, so this week's batch has been delivered of 25 articles.

**Ehtisham Hussain:** This is the spike that I saw, like while looking at the organic traffic.

**Ehtisham Hussain:** Let me quickly include the link here too.

**Ehtisham Hussain:** Okay.

**Ehtisham Hussain:** So as you can see, we usually get like 400, like sessions in 400, we get active users in 400 to 300, the last week was like, it was a major, major spike.

**Ehtisham Hussain:** Like it was 813 sessions, 777 active users, 720 new users, and the average engagement time went down drastically.

**Ehtisham Hussain:** Like it went from one minute and 26 seconds, one minute, a minute, and 23 seconds to just 42 seconds.

**Ehtisham Hussain:** The key events were kind of consistent because we get 325, 256, so we got 314, and out of those, 309 were shop directly used.

**Ehtisham Hussain:** And I feel like I pronounced this incorrectly, but I don't know. That's good.

**Ehtisham Hussain:** So these numbers, they weren't adding up for me.

**Ehtisham Hussain:** So when I looked into it, and you guys have access to this file too.

**Ehtisham Hussain:** So when I looked into it, these 813 sessions, the 777 active users, they're mostly coming from like a bunch of new pages that usually don't appear when I do this weekly report.

**Ehtisham Hussain:** But now they were like roughly 400 or so pages.

**Ehtisham Hussain:** I just pulled out 252 here, but there were 400 and so pages.

**Ehtisham Hussain:** And all of them just have one session, one active user, zero seconds on the page.

**Ehtisham Hussain:** So maybe a crawler got recorded as an organic visitor because I usually, what I do is I drill it down to organic traffic.

**Ehtisham Hussain:** So this is, this is amazing.

**Ehtisham Hussain:** Sanitized version of the traffic.

**Ehtisham Hussain:** This does not have any direct hits or anything.

**Ehtisham Hussain:** And zero second sessions, they brought our average engagement down and they spiked the sessions and active users.

**Ehtisham Hussain:** But I added the normal looking numbers and they were still more than like 400.

**Ehtisham Hussain:** So we're fine on that front like when it comes to sessions and everything.

**Ehtisham Hussain:** I see that there was, when it comes to key events, let me see.

**Ehtisham Hussain:** So when it comes to key events, there were 309 shop directory views.

**Ehtisham Hussain:** One was a become a partner form, Sunbit, Submit option.

**Ehtisham Hussain:** And I think this may have been a test someone performed.

**Ehtisham Hussain:** And if no one was performing any tests, then someone filled out the form.

**Ehtisham Hussain:** And then we got four clicks on Find Sunbit as well.

**Ehtisham Hussain:** So now we're getting new activity when it comes to these key events.

**Jason Beltran:** Yeah, that's interesting.

**Jason Beltran:** Yeah, you know, but internally, we have a lot of, you know, we're pretty, we have a new, we've had a new structure this year where there's a bunch of disparate efforts.

**Jason Beltran:** And I don't, you know, there's, they're done in silos.

**Jason Beltran:** So I don't know if that's something that maybe was happening internally, or if externally, like what competitor was trying to like, scrape our site and using maybe even an agent, like an AI agent.

**Jason Beltran:** Yeah, they do that.

**Jason Beltran:** So then the AI agent is in an active browser.

**Jason Beltran:** So that looks like a user.

**Jason Beltran:** And they're just kind of like indexing, like our site, I really don't know.

**Jason Beltran:** That's interesting to know, and we can investigate it further.

**Ehtisham Hussain:** Yeah, so we'll keep an eye on this. I've recorded my notes on this over here as well.

**Ehtisham Hussain:** The item that I had, like, let's quickly look at the traffic for growthx articles, it's still holding, like, it's pretty much the same.

**Ehtisham Hussain:** I think because we haven't added a lot, we haven't been publishing that much.

**Ehtisham Hussain:** We have published, what, 10 more articles since we've met?

**Jason Beltran:** Yeah, yeah.

**Ehtisham Hussain:** So they, I need to, like, refine this report as well a little bit, but it's, it got me traffic up to October 29, and the trends are pretty similar.

**Ehtisham Hussain:** Their, their, uh, impressions are going up, links are going up.

**Jason Beltran:** No, that's good.

**Jason Beltran:** Yeah.

**Jason Beltran:** And overall, like, we're, we're trying to, Angel and I are trying to figure out, okay, what's the next steps?

**Jason Beltran:** And Angel's been doing a lot of work and, like, cleaning up the reviews, and then now we're working on the publishing.

**Jason Beltran:** Um, so, we'll get into a good group soon.

**Jason Beltran:** We're just, like, that backlog is, uh, it's taking us a minute to catch up.

**Ehtisham Hussain:** Yeah, it's, like, it's a big one.

**Ehtisham Hussain:** Uh, it's, I think, hundreds of.

**Ehtisham Hussain:** So then the really big item was the LLM plan.

**Ehtisham Hussain:** So Kyle will have more thoughts on this, but I will present you my version today.

**Ehtisham Hussain:** And then Kyle will also have some feedback on this and maybe he'll make some changes.

**Ehtisham Hussain:** I'll also get yours and Angel's feedback on this.

**Ehtisham Hussain:** And then we can like finalize it and put it into motion.

**Ehtisham Hussain:** So the general plan is that we address all the questions that our four primary personas go to ChatGPT or Gemini with.

**Ehtisham Hussain:** So the four primary personas are a dental patient and someone who owns a dental clinic, a dentist, someone who owns an auto repair shop and someone who may need auto repair.

**Ehtisham Hussain:** Right.

**Ehtisham Hussain:** So these four people, they may have, you know, we have to assume that they go to ChatGPT, they go to Gemini, they go to Claude and other AI tools like that.

**Ehtisham Hussain:** And they ask questions, they get there.

**Ehtisham Hussain:** And usually the answers don't really mention any brands unless it comes up, like unless they specifically ask, they recommend me some good companies for blah, blah, blah, you know, a company's name never really comes up.

**Ehtisham Hussain:** So what we want to do is we create thorough answers to all these questions, not full articles because LLMs are not really crawling whole websites and like 2,000 word or 3,000 word articles, just short answers, but not that short.

**Ehtisham Hussain:** And we want to answer them and we want to kind of inject, that would be Sunbit's version of it.

**Ehtisham Hussain:** Like we will answer the question purely in an information, informative style, but we will mention Sunbit in there and we'll say according to experts at Sunbit or we'll say according to sunbit.com.

**Ehtisham Hussain:** So, so, so, we'll be kind of training those LLMs to, to.

**Ehtisham Hussain:** Mention Sunbit wherever relevant when it comes to those kinds of conversations.

**Ehtisham Hussain:** So what I did was I compiled a list of questions that these personas may have.

**Ehtisham Hussain:** So these are like, let's say auto repair financing questions.

**Ehtisham Hussain:** So they have general financing concerns.

**Ehtisham Hussain:** How can I increase?

**Ehtisham Hussain:** So this is an auto repair owner or shop owner who would want to increase their repair order and third-party financing, specifics, approval rates, customer access.

**Ehtisham Hussain:** So they may have a bunch of questions.

**Ehtisham Hussain:** we'd have like, and you guys have access to these documents as well.

**Ehtisham Hussain:** So we have 180 questions over here.

**Ehtisham Hussain:** Then we have...

**Ehtisham Hussain:** 150 questions over here and so on.

**Jason Beltran:** So these four documents...

**Ehtisham Hussain:** And they have close to 200 or 150, somewhere between 150 and 200 questions for each of these personas.

**Ehtisham Hussain:** What we want to do is if we start answering all of them in the same document, that's going to be a big e-book or something.

**Ehtisham Hussain:** That's not going to be a small page.

**Ehtisham Hussain:** So we are going to group them like this.

**Jason Beltran:** Like this is going to be one page.

**Ehtisham Hussain:** This is going to be the next page and so on.

**Ehtisham Hussain:** So each of this, like this document is going to give birth to a bunch of pages and we'll have answers in there and those will be Sunbit's answers to these questions.

**Ehtisham Hussain:** We'll then publish those pages.

**Ehtisham Hussain:** Those pages are just going to be question and answer format.

**Ehtisham Hussain:** Like there's not going to be an intro.

**Ehtisham Hussain:** There's not going to be conclusion.

**Ehtisham Hussain:** There's not going to be anything else in there.

**Ehtisham Hussain:** Just questions and answers.

**Ehtisham Hussain:** And then we're going to list them in your LLMS.pxt file so that we direct LLMS to crawl those pages.

**Ehtisham Hussain:** And then we're going to keep track of like we...

**Ehtisham Hussain:** We can keep track of these questions in scrunch, and we can see how much Sunbit's name is coming up.

**Ehtisham Hussain:** Yeah, yeah, I love it.

**Jason Beltran:** So then we'll have these, so we'll turn off, like, search engine crawl.

**Ehtisham Hussain:** That's up for debate.

**Ehtisham Hussain:** Like, so I was talking to Kyle about this.

**Ehtisham Hussain:** Kyle is of the opinion that since we, like, we have covered a lot of cost-related, we do a lot of cost-related articles anyway.

**Ehtisham Hussain:** And there's a massive opportunity here for internal linking, because there's a lot of cost-related questions in there.

**Ehtisham Hussain:** So that's still up for debate.

**Ehtisham Hussain:** Kyle is of the opinion that SEO and AEO should go hand in hand, and if we let search engines crawl it, there's no harm in it.

**Ehtisham Hussain:** Yeah.

**Ehtisham Hussain:** Because we are already mentioning these files in LLMS.pxt file.

**Ehtisham Hussain:** So we are directing those AI rules to crawl them.

**Ehtisham Hussain:** And then at the same time, we are giving ourselves a chance to get more organic.

**Ehtisham Hussain:** traffic through these pages, so that's why I put this point in there that we can either make them exclusive or we can let them be crawled, we are leaning towards letting them be crawled because why not, there's going to be internal linking, there's going to be organic traffic.

**Jason Beltran:** That makes sense, yeah.

**Ehtisham Hussain:** So this was my original plan, once Kyle weighs in as well, we can set this into motion.

**Jason Beltran:** Sounds good.

**Ehtisham Hussain:** So one action item from last week's meeting was Sunbit versus Cherry.

**Ehtisham Hussain:** So we did a bunch of research on it and so we have like a whole core positioning difference and this is going to need your approval.

**Ehtisham Hussain:** It's linked in the file and so we just want to make sure that we got this right.

**Jason Beltran:** So that doesn't apply can can So

**Ehtisham Hussain:** And then we have a bunch of perfect ideas in here as well.

**Jason Beltran:** Yep, we can look through that.

**Jason Beltran:** And I don't, it's, so the one that we're, the only one that we're competing on is Dental with them.

**Ehtisham Hussain:** And I just want to make sure, because I saw you had auto service.

**Ehtisham Hussain:** Yeah.

**Jason Beltran:** So they're only a Dental competitor.

**Jason Beltran:** So we can, you can remove the auto ones because those aren't relevant.

**Jason Beltran:** Yeah.

**Jason Beltran:** Yeah.

**Jason Beltran:** In auto, the competitor we have is called Dignify.

**Ehtisham Hussain:** All right.

**Jason Beltran:** But they're not, they're not a threat at all.

**Jason Beltran:** It's the, yeah, Dignify.

**Jason Beltran:** That one, if you want to put it in there, it's D-I-G-I-N-I.

**Jason Beltran:** Dignify.

**Jason Beltran:** It

**Jason Beltran:** And then there's also a firm, dignifying the firm in an auto.

**Ehtisham Hussain:** All right.

**Ehtisham Hussain:** Okay.

**Ehtisham Hussain:** So, but like we haven't done these yet.

**Ehtisham Hussain:** I wanted to know how you want to like go about it.

**Ehtisham Hussain:** Like, of course, you can go through this page and leave some comments in there if we got some numbers wrong or anything.

**Ehtisham Hussain:** yeah.

**Ehtisham Hussain:** And then about the tone, like how do we go about it?

**Ehtisham Hussain:** Do we, can we go a little aggressive and say that Cherry doesn't do X, Y, Z?

**Jason Beltran:** Yeah, yeah.

**Jason Beltran:** We definitely, we want to be aggressive.

**Jason Beltran:** And then, of course, our legal team will kind of like pull it back.

**Jason Beltran:** But we want to be, and we kind of like internally, we said we want to take the gloves off.

**Jason Beltran:** So we want to we want to hit them hard.

**Ehtisham Hussain:** Okay.

**Ehtisham Hussain:** So we got this.

**Ehtisham Hussain:** And then other than that, like, I'll keep an eye on this traffic situation.

**Ehtisham Hussain:** See what happens next week.

**Ehtisham Hussain:** Does it return back to normal or let's see if this continues like this.

**Ehtisham Hussain:** Sounds good.

**Ehtisham Hussain:** And then for the LLM thing, we'll get this into motion during this week.

**Ehtisham Hussain:** And then so it's just it's Friday tomorrow.

**Ehtisham Hussain:** So just one day and then early next week.

**Ehtisham Hussain:** And then Kyle is going to weigh in on this as well.

**Ehtisham Hussain:** And then we are going to go.

**Ehtisham Hussain:** Hopefully.

**Ehtisham Hussain:** Sounds good.

**Ehtisham Hussain:** Sounds good.

**Ehtisham Hussain:** All right.

**Ehtisham Hussain:** Yeah, this is all from my side.

**Ehtisham Hussain:** had like, we're keeping track.

**Ehtisham Hussain:** Back of scratch as well, but there was no major change in there.

**Ehtisham Hussain:** was still the same numbers, 97% positive, sentiment, and all that.

**Ehtisham Hussain:** Yeah.

**Ehtisham Hussain:** So I think this is going to change once we start with these LLM pages.

**Ehtisham Hussain:** I'm going to put all these questions in here as well, in the prompt section.

**Ehtisham Hussain:** Yep.

**Ehtisham Hussain:** So we have, like, hopefully close to 1,000 in here, and then we'll see what it returns.

**Jason Beltran:** Sounds good.

**Jason Beltran:** Yeah, I got to dig more into Scrunch as well, and I'm really interested in what's happening with, like, Cherry and Dental, specifically.

**Ehtisham Hussain:** All right.

**Jason Beltran:** Yeah.

**Jason Beltran:** Very good.

**Ehtisham Hussain:** All right.

**Ehtisham Hussain:** So that's all from my side.

**Ehtisham Hussain:** If anything comes up, reach out on Slack, and I'll do the same.

**Jason Beltran:** Sounds good.

**Ehtisham Hussain:** Okay.

**Jason Beltran:** Have a nice day, everyone.

**Jason Beltran:** You too.

**Jason Beltran:** Bye.
