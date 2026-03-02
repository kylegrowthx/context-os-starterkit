# Katya / Bailey SentinelOne

<metadata>
date: 2025-12-03
time: 19:30 UTC
duration: 59 minutes
organizer: Bailey Seybolt (bailey@growthx.ai)
participants: Katya Luscomb, Bailey Seybolt
fathom_recording_id: 106078081
fathom_url: https://fathom.video/calls/493892074
share_url: https://fathom.video/share/8PzcRyXANWJgsnuQ4Arxtvk1yazgxGEf
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Katya handed over the SentinelOne account to Bailey, detailing critical strategic and operational challenges: the editorial CS101 content lane is blocked by extreme keyword cannibalization within SentinelOne's thorough existing content, making manual research inefficient and slow. The team will propose pivoting from editorial work to the scalable PSEO (CVE page) engine, which can produce 100–200 pages daily and scale to 1,000–1,500 per week once a GitHub sync is live. Bailey's immediate priorities include securing a December content runway by pushing for 20 topic approvals, investigating automation of the Airtable-to-Atlas CVE URL sync, and exploring Looker reporting solutions for high-volume CVE pages.

---

## Context

SentinelOne is a cybersecurity company and a GrowthX content marketing client. Katya joined the account approximately two months prior (early October) following a extended strategy sprint where SentinelOne pivoted away from requesting AI-generated blog content and redirected GrowthX to focus on CS101 (Cybersecurity 101) educational content. The relationship is complex: SentinelOne has published extremely thorough existing content across CS101 topics, leaving almost no keyword gaps for new editorial work. The account operates with high editorial involvement from multiple stakeholders (OnKit as lead SEO strategist, Mancy as hands-on reviewer, and Mahendra for topic approvals), resulting in long articles (2,000–3,200 words), frequent revisions, and slow topic approval cycles (typically 5 approvals at a time rather than the 20 needed for a stable calendar). Katya flagged the unsustainability of this approach and proposed a strategic pivot to PSEO (CVE pages), which SentinelOne had discussed in the strategy sprint but is not explicitly part of the current Statement of Work.

---

## Relevance

**To GrowthX Delivery:**
- Editorial work at SentinelOne is hitting a hard ceiling due to keyword cannibalization within their existing CS101 content. A manual, multi-step verification process (Google site: search + on-site search + SEMrush) is required to avoid client rejection, but still yields ~25% cannibalization rates on batches.
- The team should reframe SentinelOne conversations around templated, repeatable content patterns rather than line-by-line editorial edits to improve efficiency.
- New account management setup: OnKit (SEO strategist, directs strategy), Mancy (hands-on reviewer for all articles), Mahendra (topic approvals). Bailey needs to maintain async workflows and manage three-person approval cycles.
- Consider proposing a formal scope revision to clarify whether editorial CS101 work or PSEO is the primary focus, as the current SoW does not specify word counts or article commitments.

**To CheckThat:**
- PSEO/CVE page engine is proving effective with early promising traffic. A GitHub sync for real-time CVE updates could unlock 1,000–1,500 new pages/week, representing significant AEO opportunity.
- High-volume automated content creation at this scale requires new approaches to performance tracking and reporting (current Looker dashboard approach breaks down with 1,000+ individual clusters).

**To GrowthX Business Development:**
- Account health is mixed. Keyword cannibalization and slow approvals are creating execution friction, but the client's openness to PSEO pivot suggests strategic alignment potential.
- Expansion opportunity: if PSEO strategy is formalized in December, it could become the strategic focus and open discussion of revised pricing/scope for 1,000–1,500 page/week operations.
- SentinelOne leadership awareness: OnKit's strategic steering role suggests higher-level decision-making may be possible; flagged for future escalation if needed.

---

## Overview

- **Editorial work is unsustainable.** The "CS101" content lane is blocked by extreme keyword cannibalization, requiring a slow, manual research process. The team will propose pivoting to focus on the scalable PSEO engine.
- **PSEO is the future.** The automated CVE page engine is the clear strategic path forward, with plans to scale to 1,000+ pages/week once a GitHub sync is live.
- **Bailey's immediate priorities.** Secure a content runway for December by pushing for topic approvals and investigate automating the Airtable-to-Atlas URL sync for the CVE engine.

---

## Key Topics

### Challenge: Editorial Work is Unsustainable

  - **Blocker:** The "CS101" content lane is blocked by extreme keyword cannibalization.
      - **Root Cause:** SentinelOne's existing content is so thorough that finding unique, high-volume keywords is nearly impossible.
      - **Impact:** The manual research process is slow and yields few approved topics, creating a persistent scramble for assignments.
  - **Inefficient Process:**
      - **Research:** Requires a manual, multi-step check (Google `site:` search, on-site search) to validate gaps identified by SEMrush.
      - **Approvals:** Clients approve topics in small batches (e.g., 5 at a time), preventing creation of a stable content calendar.
      - **Revisions:** High-touch editorial involvement from multiple stakeholders (OnKit, Mancy, SMEs) leads to long articles (\~3,200 words) and significant revision cycles.
  - **Proposed Pivot:** The team will propose pausing editorial work to focus on the scalable PSEO engine.
      - **Rationale:** A recent audit confirmed refresh opportunities are too limited to justify the calibration effort.

### Solution: Pivot to PSEO (CVE Pages)

  - **Strategic Fit:** The automated CVE page engine is the ideal strategic fit for GrowthX's scalable model.
      - **Volume:** The engine can produce 100–200 new pages daily.
      - **Performance:** Early traffic from the pilot launch is promising.
  - **Scaling Plan:**
      - **Phase 1:** Publish 1,000 existing CVEs/week from the current Airtable.
      - **Phase 2:** Once the GitHub sync is live, publish a weekly batch of 1,000–1,500 new CVEs.
  - **Operational Challenges:**
      - **Looker Reporting:** The high volume of CVE pages makes adding them as individual clusters to the Looker dashboard impractical.
      - **URL Sync:** The client requires published URLs in the Airtable database, which currently requires a manual process.

### Operational Tools & Workflow

  - **Airtable Interface:** An Airtable interface provides a central, visual content calendar.
      - **Purpose:** To give both teams a clear overview of content status and production schedules.
      - **Client Adoption:** The client has started using it for topic approvals (Mahendra), but needs to use it for review status updates (Mancy) to enable auto-publishing.
  - **Auto-Publishing:** The goal is to automate publishing via Atlas.
      - **Trigger:** The client would update the Airtable status to "Ready to Publish."
      - **Benefit:** Eliminates manual Slack communication and reduces client workload.

---

## Action Items

**Katya Luscomb (GrowthX)**
- Send 1 editorial revision to Iana this week; rerun longer piece next week
- Follow up w/ OnKit/Mancy/Mahendra on CVE code freeze status
- Create and share Loom on SentinelOne cannibalization check workflow w/ Bailey
- Draft SentinelOne call agenda for Dec 4; include Bailey intro, approvals, CVE freeze, Looker, CVE URLs, long-tail, cadence
- Ask Vivek re: Looker CVE visibility; then propose approach to client
- Clean up ContentOS interface; remove 'Sent to client' and fix status field
- Add Mancy to ContentOS w/ review status edit permissions

**Bailey Seybolt (GrowthX)**
- Investigate Atlas→Airtable CVE URL sync; consult Carrie if needed; propose approach to client
- Find SentinelOne CMS in Notion; share w/ Katya

---

## Transcript
**Bailey Seybolt:** Moving the time.

**Bailey Seybolt:** It was one of those moments where I was like, This meeting is being recorded.

**Bailey Seybolt:** I'm definitely going to go over, so you can either like sit there waiting for me or I can just push it.

**Katya Luscomb:** Yeah, no, it worked.

**Katya Luscomb:** I had a ton of things I was juggling this morning.

**Katya Luscomb:** And so honestly, when you messaged me, I was like, great, I'm going take a brain break.

**Bailey Seybolt:** Oh, man, it's a week.

**Bailey Seybolt:** I feel like my brain is like being torn in half this week.

**Katya Luscomb:** Yeah, yeah.

**Katya Luscomb:** No, I was going to ask how you're doing with like, I would love for us to just like chat about the EM role.

**Katya Luscomb:** It doesn't have to be all the time.

**Katya Luscomb:** But like, I feel like often you say things in meetings that like I'm thinking and just haven't quite like managed to figure out how to ask yet.

**Bailey Seybolt:** And so I really appreciate how our perspectives seem to sink.

**Bailey Seybolt:** No, that'd be great.

**Bailey Seybolt:** We should we should just have like buddy time.

**Katya Luscomb:** Yeah, I would love that.

**Katya Luscomb:** I know this.

**Katya Luscomb:** I also just like, I feel so bad handing Sentinel one to you, not because they're like a terrible account, but it feels like they're kind of in a messy place.

**Katya Luscomb:** Um,

**Bailey Seybolt:** That's probably not your fault, so.

**Katya Luscomb:** Not entirely.

**Katya Luscomb:** They're tricky.

**Katya Luscomb:** I've been working a lot with Kyle and like the number of times we've been on calls and he's like, hmm, yeah, this is not ideal.

**Katya Luscomb:** In like, just like finding gaps in their CS101 content.

**Bailey Seybolt:** Has it been really hard to find keywords for them?

**Katya Luscomb:** It's been so hard.

**Katya Luscomb:** So like.

**Bailey Seybolt:** So why did they hire us?

**Bailey Seybolt:** Like, what's the context?

**Bailey Seybolt:** Like, why would they hire us if they don't, if they have so much stuff that there's like nothing for us to do?

**Katya Luscomb:** So it's shifted my understanding.

**Katya Luscomb:** So I came on to them like two months ago, I think.

**Bailey Seybolt:** Were they new or were you?

**Katya Luscomb:** Were they at a sprint?

**Katya Luscomb:** They were newer.

**Katya Luscomb:** So they were just coming out of the strategy sprint.

**Katya Luscomb:** Part of the issue is that coming out of the strategy sprint, they didn't have any additional keywords.

**Katya Luscomb:** So like a week into me starting here and taking them on, it was like, they need keywords.

**Katya Luscomb:** Go.

**Katya Luscomb:** I was like, okay.

**Katya Luscomb:** Okay.

**Katya Luscomb:** So I did a bunch of digging.

**Katya Luscomb:** It took me probably like 10 hours to do that initial batch of research because like I, context, like I come from a broader like writing background, not necessarily like marketing and SEO research specifically.

**Katya Luscomb:** So I'm like doing a deep dive and learning a lot of this as I go.

**Katya Luscomb:** Same.

**Katya Luscomb:** Cool.

**Katya Luscomb:** Glad to know I'm not alone there.

**Bailey Seybolt:** Did they mention, it's funny.

**Bailey Seybolt:** like what, after my first week or two at the job, I was like, you know what?

**Katya Luscomb:** We didn't even talk about SEO research in my interview.

**Katya Luscomb:** We didn't really talk about it either.

**Katya Luscomb:** Like I, I mentioned that I had like some basic familiarity with some like other web content that I had done.

**Katya Luscomb:** A lot of what I was doing was like AI editorial work.

**Katya Luscomb:** Um, it's like a third party contractor for a group that like worked for Google and we like graded all of those like AI responses and things, um, and then rewriting them.

**Katya Luscomb:** So they actually sounded human.

**Katya Luscomb:** Um, it was, it was my more recent shift, but yeah.

**Katya Luscomb:** Anyway, I like, I flagged.

**Katya Luscomb:** And pretty early on when I was working with SentinelOne, I was like, you know, like, I need some support here and some strategic guidance on, like, how to effectively do this because it's not working right now.

**Bailey Seybolt:** Yeah.

**Katya Luscomb:** And then the more Kyle dug in, like, we realized that it really is because they have a bulk of content on CS101.

**Katya Luscomb:** They are super sensitive to cannibalization risks.

**Katya Luscomb:** One of the early pieces of feedback they gave us, like, early, mid-October, they had shared that they really wanted us to focus on high-volume keywords that, like, didn't include AI in it, which most of that they've already covered.

**Bailey Seybolt:** So it left us with this, like, teeny-tiny silo.

**Bailey Seybolt:** Did they give you a sense of, like, why they wanted to focus on that?

**Katya Luscomb:** I think that has just been their tactic of, like, the mindset of high-volume keywords is going to equal, like, more likely traffic and more valuable opportunities to go for.

**Katya Luscomb:** Yeah.

**Bailey Seybolt:** Even if you don't rank for them, though, if they're all like, presumably those are also higher difficulty, most of them.

**Katya Luscomb:** For a lot of them, yeah.

**Katya Luscomb:** I mean, they do, they've got really good site authority.

**Bailey Seybolt:** So there's, there's that to leverage in part because they have so much content.

**Katya Luscomb:** So they feel bolder in going for a lot of that.

**Katya Luscomb:** And I think they were in this mindset of like, it takes a long time and a lot of people hours to generate content like this.

**Katya Luscomb:** Um, and so helping frame this idea of like, sort of that, that abundance mindset.

**Katya Luscomb:** But even then, um, there's still quite a lot of cannibalization risk within CS101.

**Bailey Seybolt:** Yeah.

**Katya Luscomb:** So I'll backpedal a little bit.

**Katya Luscomb:** Um, in the strategy sprint before I came on, there was initial discussion about doing like a couple different things within like an editorial lens.

**Katya Luscomb:** Um, cause they have a blog that is written by a lot of their like cybersecurity experts, and then they have the CS101 content.

**Katya Luscomb:** about it.

**Katya Luscomb:** Okay.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** Uh, cause

**Katya Luscomb:** And I want to say we got like three weeks into the strategy sprint and all of a sudden they're like, actually, we don't want any AI generated content on our blog.

**Katya Luscomb:** You guys can't produce there and we think that it would be better for you to do CS101.

**Katya Luscomb:** So coming into it, I don't think there was a lot of clarity in terms of like the lane that made sense for what our service really offers.

**Katya Luscomb:** And then they were in the strategy sprint for a really long time as well, in part because it took them a long time to like get back to us and get us context that we needed.

**Katya Luscomb:** And so when I got them, we had pivoted, we were doing CS101 content that was like, we had produced a fair amount.

**Katya Luscomb:** We hadn't gotten a ton of feedback yet.

**Katya Luscomb:** But I think we had published like three pages and there was a backlog of a bunch of stuff that still needed to be published.

**Katya Luscomb:** And the big focus was on their PSEO strategy, which was not original.

**Katya Luscomb:** in the scope of their SoW.

**Katya Luscomb:** Their SoW, it only mentions editorial work, but it doesn't have a strict word count or number of articles we're committed to delivering, which I know we were talking about a little bit last week.

**Katya Luscomb:** We have delivered something to them every week that I've been with them, in part because of like scrambles over weekends for me to like get keywords and things and like poking it, getting assignment approvals.

**Katya Luscomb:** And the articles get long.

**Katya Luscomb:** I think I'd flag that for you that like when like we'll send them content that's like about 2000 words and then they'll ask us to add like five different additional H2s in the table of contents.

**Katya Luscomb:** And even if you keep those super short, it just balloons.

**Bailey Seybolt:** But they're very editorially like involved.

**Katya Luscomb:** Very much so.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** So they are like high touch in terms of

**Katya Luscomb:** The, like the precision and language that they want in headers and things.

**Katya Luscomb:** So there's, there's a couple different things I think that like, you'll need to keep in mind with conversations going forward with them is some maybe better framing around like, how the models operate and that like, they're not necessarily doing line by line edits, but the more we can find repeatable patterns within how we're producing content, the more successful the content is going to be, which is a big part of what I've been trying to do.

**Bailey Seybolt:** Like create more templated content, you mean?

**Katya Luscomb:** Sort of, yeah.

**Katya Luscomb:** So, and a lot of the table of contents that they send us follow kind of a templated structure with some variation in like H3s and a few different H2s depending on the content.

**Katya Luscomb:** And so I've really tried to template that as much as I can.

**Katya Luscomb:** And it's been working with the exception of one piece I sent them last week and they're like, yeah, the table of contents.

**Katya Luscomb:** Didn't really make sense for this keyword.

**Katya Luscomb:** Okay.

**Katya Luscomb:** I haven't actually looked at that one yet.

**Katya Luscomb:** Just like, I don't want to deal with this right now.

**Katya Luscomb:** But I need to send that to Iana.

**Katya Luscomb:** And that would probably be a good thing for you guys.

**Katya Luscomb:** I think one of them, we can get to them this week.

**Katya Luscomb:** And then the other revision, that's going to be longer.

**Katya Luscomb:** We'll probably just need to rerun through the pipeline.

**Katya Luscomb:** So it can flag that we'll send that to them next week.

**Katya Luscomb:** And they're usually, so long as we proactively communicate, like when we're sending things, they're usually pretty understanding about it.

**Katya Luscomb:** And then I need to follow up on if the code freeze actually got lifted for the CVE pages.

**Bailey Seybolt:** And so in terms of like your pipeline, would you say that, like, are you delivering five?

**Bailey Seybolt:** Are you aiming to deliver five a week?

**Bailey Seybolt:** Or given the length and the complexity, are you just, and the fact that there's nothing in the SoW, are you like setting your bar a little bit lower?

**Katya Luscomb:** So I have been, so long as we have assignments, I've been aiming to deliver five.

**Katya Luscomb:** I think there's like two weeks that we've

**Katya Luscomb:** Only delivered like two or three, but pretty consistently we've been able to meet the five.

**Katya Luscomb:** There was one week I don't think we delivered any because they gave me like 10 pieces of content to revise.

**Katya Luscomb:** And so I flagged for them.

**Katya Luscomb:** was like, hey, you know, this is a little bit more on the revision front.

**Katya Luscomb:** Like we're going to postpone publishing and give us a little bit of wiggle room for some assignments as well.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** So there's some of that that like, yeah, just the more proactive in planning.

**Katya Luscomb:** My goal with them has been like to get enough assignment approvals to like create more of a content calendar.

**Katya Luscomb:** And we've just never quite been able to get to the point where we have that that much of a backlog of keywords.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** Because even when I do send assignments, they'll approve like five at a time.

**Katya Luscomb:** We need like 20 of these approved.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** Or rejected immediately.

**Bailey Seybolt:** like has been the case this week too, where there's like six.

**Katya Luscomb:** Yeah.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** And are they good at it async?

**Bailey Seybolt:** Or like I have one client where I basically have to like sit with them live.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** They are.

**Bailey Seybolt:** They're pretty good.

**Katya Luscomb:** I need you to do this right now.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** Can we walk through these and like approve them?

**Katya Luscomb:** No, they're pretty good about doing things async.

**Katya Luscomb:** There's a lot of stakeholders involved.

**Katya Luscomb:** So my messages often tag three people.

**Katya Luscomb:** usually tag like OnKit and Mancy for anything editorial.

**Katya Luscomb:** And then now I'm also tagging Mahendra when it comes to approving topics.

**Katya Luscomb:** So OnKit is their like main SEO strategist.

**Katya Luscomb:** He's the most hands on when it comes to like directing content strategy largely on our weekly calls.

**Katya Luscomb:** There are other folks above him who I think would be good to involve at some point if we need to do like a really big strategic shift.

**Katya Luscomb:** And then Mancy does a lot of the hands on like she's in every article reviewing it.

**Katya Luscomb:** She responds when we have table of contents updated.

**Katya Luscomb:** She applies all of the edits that the subject matter experts put in.

**Katya Luscomb:** So we only have one cycle of review with them.

**Katya Luscomb:** Like she sends us table of contents, structural edits back.

**Katya Luscomb:** We apply those and then their subject matter experts go in and flag a bunch of things that she fixes.

**Bailey Seybolt:** And have you been delivering in Slack or do you have automation set up in air?

**Katya Luscomb:** So I deliver in Slack just because the timing of things has been funky.

**Katya Luscomb:** And they like sort of one singular roundup.

**Katya Luscomb:** I was thinking about trying to set up an automation where like every Friday it just had like, here's what's ready.

**Katya Luscomb:** And then sent it to them.

**Katya Luscomb:** Just did not quite get that put in place.

**Katya Luscomb:** In part because sometimes I didn't have things ready until like really late Friday.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** Well, I feel like that's easy enough to do.

**Bailey Seybolt:** And I'm sure it won't happen now because I'm not even sure like who's delivering in what way right now.

**Katya Luscomb:** Because it sounds like Panzer is going to be reviewing stuff.

**Katya Luscomb:** So I don't want anything automated since we don't have it on the Slack on our end.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** so in terms of like.

**Bailey Seybolt:** The keywords you have now, like, I'm wondering, so there's maybe 20 ideas for approval.

**Bailey Seybolt:** And then, you know, there is a huge list of like, you know, of these sort of other 350 keywords on the list.

**Katya Luscomb:** Are those all ones that have been so, oh, you're talking about like, yeah, yeah, like in your air table.

**Katya Luscomb:** I'm just wondering, like, are these all potential articles to extend the runway?

**Katya Luscomb:** Or are these ones like, have you probably not?

**Katya Luscomb:** So these came to me in the, from the strategy sprint.

**Katya Luscomb:** I flagged a lot of them as archived from what I could, like, I was, I was trying to clean this up a long time ago.

**Katya Luscomb:** And then I just kind of gave up halfway through because I needed to focus on like actually getting them assignments.

**Katya Luscomb:** I, let me share the keyword research doc that Kyle and I were working on.

**Bailey Seybolt:** And have you been like, yeah, I would also love to know.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** Like.

**Bailey Seybolt:** Say whether or not these 20 get approved, like how would you approach the next round of research for them?

**Bailey Seybolt:** And like, how do you loop in Kyle?

**Bailey Seybolt:** Like, how do you think about?

**Bailey Seybolt:** And then also understanding, given the huge database of content they have, how have you been checking?

**Bailey Seybolt:** Yeah.

**Katya Luscomb:** Manually.

**Bailey Seybolt:** Using what?

**Katya Luscomb:** I use, so I use their, both their website and Google.

**Katya Luscomb:** And I can make you a little loom on how I've been going about it.

**Katya Luscomb:** But I think I've got one that I started to prep.

**Katya Luscomb:** I'm trying to find, I've got, I had a couple different docs of keyword research.

**Katya Luscomb:** So what we ended up doing, oh my goodness, where is this?

**Katya Luscomb:** Sorry, I should have been way more prepared for this call.

**Katya Luscomb:** One second to pull this up from.

**Katya Luscomb:** So the first time I tried it, I basically like grabbed a bunch of keywords from SEMrush.

**Katya Luscomb:** And the keyword gap.

**Katya Luscomb:** Yep.

**Katya Luscomb:** The tricky thing with that is because of how Google changed the pages they show in their results.

**Katya Luscomb:** Like there's a lot of SentinelOne content that's not showing up.

**Bailey Seybolt:** And so it says it's a gap and it's not actually.

**Bailey Seybolt:** Right.

**Katya Luscomb:** So that was causing a big issue.

**Katya Luscomb:** Like the last batch of content that I sent them before this round, I think they rejected like 25% of them for cannibalization with content that already existed.

**Katya Luscomb:** was like, damn it.

**Katya Luscomb:** Because I had spent a lot of time trying to come through and checking for that.

**Katya Luscomb:** Let me share my screen really quick.

**Katya Luscomb:** So this document, if I'm sharing the right thing, and I'll link this to you.

**Katya Luscomb:** You're just running with my stream of consciousness here a little bit.

**Katya Luscomb:** Run.

**Katya Luscomb:** Run.

**Katya Luscomb:** So this is something that Kyle helped with together.

**Katya Luscomb:** Basically, he pulled one of these tabs is keywords from SentinelOne.

**Katya Luscomb:** Maybe these both are.

**Katya Luscomb:** So one is from SentinelOne and one is from CrowdStrike.

**Katya Luscomb:** And then he also imported keywords.

**Katya Luscomb:** Okay, so these are SentinelOne from GA4, I believe, over a couple of different periods.

**Katya Luscomb:** And then this tab shows, this is a SEMrush poll from a CrowdStrike keyword gap analysis.

**Katya Luscomb:** And basically what we've done here is we've got a formula comparing if this keyword is anywhere in the GAC data from SentinelOne.

**Katya Luscomb:** M어중, the can simply give So

**Katya Luscomb:** And flagging like what row number it is, which is really just an easy way to see if it exists or not.

**Katya Luscomb:** And then anything that's NA is like, let's check to see if they do actually have something published.

**Katya Luscomb:** So this is where the manual piece comes in.

**Katya Luscomb:** There's probably a way to play with it, potentially in Claude, maybe in Perplexity, depending on, yeah, I'm not sure which one's going to be better for that.

**Katya Luscomb:** But to potentially have them look for it.

**Katya Luscomb:** And so I do this a couple different ways where there's also like a lot of duplicate terms in part because CrowdStrike has their own cannibalization.

**Katya Luscomb:** And like, you know, one article might rank for honeypot and then the other might rank for like honeypot and, you know, that kind of thing.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** So there's a degree of going in here and like looking for that overlap.

**Katya Luscomb:** And then I managed to get 10 assignments from this.

**Katya Luscomb:** The other like 20 that I developed were using a different process that was a lot more painful.

**Katya Luscomb:** So.

**Katya Luscomb:** So I think this is the best way to go.

**Bailey Seybolt:** How many are there?

**Katya Luscomb:** Like, how many roses is this?

**Katya Luscomb:** It seems like there's a lot.

**Bailey Seybolt:** Oh, there's a ton.

**Bailey Seybolt:** There's...

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** And is there any way to check what you've already done?

**Katya Luscomb:** So anything that I've checked, it's all these NAs that I've colored.

**Katya Luscomb:** So anything that has a color is done.

**Katya Luscomb:** Okay.

**Katya Luscomb:** And then I added a little use column.

**Katya Luscomb:** And so anything that I found is an actual gap.

**Katya Luscomb:** I've got it pulling into this sheet.

**Katya Luscomb:** So those are some of them you've used before and some of them you haven't.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** I need to clean this up a little bit because I was combining a couple different sheets to upload easily into Airtable.

**Katya Luscomb:** But basically, this pulls in, like, these 10 keywords were the keywords that I checked from this sheet.

**Bailey Seybolt:** And I was like, these are good to use.

**Katya Luscomb:** Okay.

**Bailey Seybolt:** If that makes sense.

**Bailey Seybolt:** So what about the ones that you've highlighted red?

**Katya Luscomb:** Does that just mean they're not good to use?

**Katya Luscomb:** Exactly.

**Katya Luscomb:** Exactly.

**Katya Luscomb:** Exactly.

**Katya Luscomb:** So it means that they're either like a duplicate of something that I flagged from this list to use or they exist on CrowdStrike or on Sentinel-1 already.

**Katya Luscomb:** And so my search for this, you can do site and then Sentinel Cybersecurity 101.

**Katya Luscomb:** And then for this keyword that I use here, I check a couple different ways.

**Katya Luscomb:** I'll look at this keyword and like Google to see if it pulls anything up.

**Katya Luscomb:** I also look to see what the main topic is of the CrowdStrike article because sometimes like there's overlap that like we have actually talked about that content.

**Katya Luscomb:** And so it doesn't necessarily make sense for us to try and target.

**Katya Luscomb:** Like I think they would still flag it as irrelevant or like, you know, tangential enough that they don't want a duplicate article.

**Katya Luscomb:** So then for this, like I would...

**Katya Luscomb:** Yeah.

**Katya Luscomb:** you.

**Katya Luscomb:** you.

**Katya Luscomb:** Thank

**Katya Luscomb:** So grab that and then paste it in here and see what showed up.

**Katya Luscomb:** Is this one that I had flagged to use?

**Katya Luscomb:** Yeah.

**Katya Luscomb:** And so because there's nothing that showed up here, it's like, okay, that keyword is probably a legitimate gap in their content versus something like, oh, yeah, like here, Internet Dark.

**Bailey Seybolt:** This is talking about like the dark web.

**Katya Luscomb:** I happen to know from hours of doing this that they have dark web content.

**Katya Luscomb:** So that didn't show up for that particular keyword.

**Katya Luscomb:** But then I will also go on to their actual Sentinel one page.

**Katya Luscomb:** And so it's like here.

**Katya Luscomb:** But because I know this relates to the dark web, then it's like, all right, they've got four articles on the dark web already.

**Katya Luscomb:** There's probably not an actual gap for us to talk here.

**Katya Luscomb:** They're knowing how thorough their content tends to be.

**Bailey Seybolt:** Does that make sense?

**Katya Luscomb:** So it is obnoxiously manual.

**Bailey Seybolt:** And especially if you're going through this and then they're like not still rejecting it.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** Like one thing if you are if it's this high touch and then you have 40 article topics and then that's your content runway for the next two months.

**Katya Luscomb:** But right.

**Katya Luscomb:** Right.

**Katya Luscomb:** But for like send them 40 topics and have them approve like 10.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** I think they will approve more that are on that list.

**Bailey Seybolt:** It just takes them a while.

**Katya Luscomb:** Like I do kind of have to keep poking at it of like, hey, like we need, you know, can you please take a look at the rest of this list?

**Katya Luscomb:** Blah, blah, blah.

**Katya Luscomb:** So I have had to do that.

**Katya Luscomb:** I will be following up with them on the call tomorrow to make sure that like they have a chance to actually go through all of those so that we actually like Iana knows what she's preparing each week.

**Bailey Seybolt:** Yeah.

**Katya Luscomb:** And I think especially with, I mean, we can say like the holidays are coming up and we need to get ahead to keep our velocity and, you know, etc.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** I do.

**Katya Luscomb:** I think that in a couple of weeks, there's going to be a point in which the conversation needs to like explicitly shift to like CS101 is not really a great lane for us to continue to execute on because of the way growthx.

**Katya Luscomb:** Like we just, the best place for us to be a strategic partner is areas that there is a lot of gap that we can like execute on rapidly at scale.

**Katya Luscomb:** CS101 has so much content and there's a few gaps, but the time it takes to identify those and the like limited repeatability within each of those topic clusters makes it really challenging for like our system to work well at scale within this realm.

**Bailey Seybolt:** Is that, is this something that you've flagged for like either your director or I'm like curious if this is something.

**Katya Luscomb:** Kyle is, Kyle is, is well aware of this.

**Katya Luscomb:** Um, and

**Katya Luscomb:** Andy's also well aware.

**Bailey Seybolt:** Have they talked to you at all about how they want to, like, manage that conversation?

**Katya Luscomb:** We don't have specific phrasing around it.

**Katya Luscomb:** I did flag for Andy that, like, it would probably be great for you to continue to, like, stay connected with a director on this account because of how challenging this is.

**Katya Luscomb:** And so the other layer of that, like, the most recent shift we tried was, like, hey, let's think about refresh opportunities.

**Katya Luscomb:** Like, maybe there's something there for us to find within CS101.

**Katya Luscomb:** Again, worked with Kyle a little bit this week.

**Katya Luscomb:** He had a couple different ways to, like, go about looking for that.

**Katya Luscomb:** His conclusion yesterday was not much.

**Katya Luscomb:** Again, like, we could probably get about a month of content runway out of refreshes.

**Bailey Seybolt:** But is it worth it?

**Bailey Seybolt:** But is it, exactly.

**Katya Luscomb:** Because, like, at that point, we're spending, we're probably spending a month calibrating what that refresh looks like.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** Only to, like, use those up in a month and then scramble again.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** And so his ultimate definition decision or like mindset was like CS1 was probably not the best lane for us to execute.

**Bailey Seybolt:** Do we have proposals for what might be a better lane for us to execute or is that something we're thinking about?

**Katya Luscomb:** that's something that we have just started to like explore with them.

**Katya Luscomb:** They have some very general ideas.

**Katya Luscomb:** They offered to connect us with their – he's not their head of product.

**Katya Luscomb:** I don't have his specific title, but to connect us with someone who does some of their product writing to like to potentially develop some content for their product pages.

**Katya Luscomb:** Again, I'm not sure that's going to be really repeatable long term.

**Katya Luscomb:** My gut feeling is that like this – it really might just be where we are developing a massive amount of PSEO content for them.

**Katya Luscomb:** And like that is our lane.

**Katya Luscomb:** That's been their priority zero since they decided that we could come on to that.

**Katya Luscomb:** So why are we trying so hard to do, make editorial work if PSEO is like their focus?

**Katya Luscomb:** Yeah, good question.

**Katya Luscomb:** Part of that is because it took so long for the PSEO content to actually be ready to publish.

**Katya Luscomb:** That strategy, I think, started like right at the tail end of their strategy sprint.

**Katya Luscomb:** So when I came in, Ada was still super hands-on in getting that off the ground.

**Katya Luscomb:** We just published the first phase, like the first pilot, November 5th, I think.

**Katya Luscomb:** And their original launch date for that was like early October.

**Katya Luscomb:** And it just kept getting delayed, mostly because of feedback and like QC processes on their end.

**Katya Luscomb:** Can I ask you where it is on their site?

**Katya Luscomb:** Because I was looking to try to find like what it looks like, but I wasn't sure where to look.

**Katya Luscomb:** Yeah, yeah, yeah.

**Katya Luscomb:** Sorry, I thought I had that one linked.

**Bailey Seybolt:** You probably do somewhere, but I don't

**Bailey Seybolt:** I'm lost in the documentation.

**Katya Luscomb:** And I wrote so much for you.

**Bailey Seybolt:** was like, this is probably overboard, but I want it somewhere other than my brain.

**Bailey Seybolt:** I think it's great to have because you can like stick it in a clod and help them find what you're looking for.

**Bailey Seybolt:** But then it also, like, I will be grateful that it's all there, but it's hard to scan.

**Katya Luscomb:** Totally.

**Katya Luscomb:** Okay, I see.

**Katya Luscomb:** I was trying to like make it so you could like collapse things easily.

**Bailey Seybolt:** You did a great job.

**Bailey Seybolt:** Thank you.

**Bailey Seybolt:** This is about me, not about you.

**Katya Luscomb:** No, no, it's the same way.

**Katya Luscomb:** Like, open those documents and I'm like, where do I start?

**Katya Luscomb:** So this is what it looks like on their page.

**Bailey Seybolt:** And how does that process, like, I know a lot of it's pretty automated.

**Bailey Seybolt:** I'd be curious to know, like, where you participate actively, kind of.

**Katya Luscomb:** So I personally have not actually participated much in the CVE generation.

**Katya Luscomb:** That has primarily, so Marcus and George Maine did a ton of work.

**Katya Luscomb:** Let's

**Katya Luscomb:** On the coding, they're still involved in debugging some like mild priority revisions that the Sentinel-1 team has requested.

**Katya Luscomb:** They have their own calls set up and are like, I've been pretty hands-off managing that because playing telephone between eng teams and dev teams sounds like a nightmare.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** So they have been mostly doing that.

**Katya Luscomb:** And then in terms of the actual production, my role and your role going forward is largely being in the CBE database, which this is likely to change.

**Katya Luscomb:** I think I tagged you in that linear ticket where we're trying to get this synced with GitHub.

**Katya Luscomb:** GitHub, yeah.

**Katya Luscomb:** And I can show you that in a second so that might have some clarity.

**Katya Luscomb:** But basically we want GitHub.

**Katya Luscomb:** It's just like a running updated list of CVE entries that it auto-updates every hour on GitHub because there's somewhere between like 100 to 200 CVE entries that are added daily, which is so like this content engine is basically never going to end.

**Bailey Seybolt:** Well, that's like ideal, right?

**Bailey Seybolt:** When you compare this to the editorial.

**Katya Luscomb:** Totally.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** This makes so much more sense as a place for us to execute and be a really strategic partner.

**Katya Luscomb:** They've already started to get some traffic from the CVE entries that they published in that first 500.

**Katya Luscomb:** Like, I think this makes the most sense as far as highly repeatable.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** Like our AI can do this way faster.

**Katya Luscomb:** Imagine a person taking five, like doing 500 of these would take forever.

**Katya Luscomb:** So what I've done here, I basically took all the CVE entries that they had initially said they wanted to prioritize.

**Katya Luscomb:** They pulled a lot of these from SEMrush.

**Katya Luscomb:** So some of them aren't actually CVE entries, which most fourth 12 in SEMrushге So Like,

**Katya Luscomb:** Atlas will, it'll throw an error if that's the case.

**Katya Luscomb:** And then if an error throws, Viana can just go in and look at, like, look at the GitHub files and see if it's on there.

**Bailey Seybolt:** So have they been delivering you the CV entries?

**Katya Luscomb:** This is not you going and finding them.

**Katya Luscomb:** So I initially went and found them because they asked us to.

**Bailey Seybolt:** And then they're like, actually, we have this whole list.

**Bailey Seybolt:** Why don't you just use this?

**Katya Luscomb:** Oh, okay.

**Katya Luscomb:** That would be easier.

**Katya Luscomb:** So then I just, I aligned the list that they shared that they had, like, prioritized.

**Katya Luscomb:** They tend to, this is actually something else good to know.

**Katya Luscomb:** They tend to ask us to do strategic thinking.

**Bailey Seybolt:** And then they're like, well, this is how we're thinking about it.

**Bailey Seybolt:** We really want you to use our strategy.

**Katya Luscomb:** So I would recommend, like, if they ask you to do that, I would poke a little bit and say, like, you know, we can.

**Katya Luscomb:** We can put a proposal together.

**Katya Luscomb:** And it'd be helpful, like, if you guys have any documentation where you've already thought about this.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** That would help us give us, like, point us in right.

**Katya Luscomb:** I didn't think about asking that because I thought that they just wanted us to like take the lead.

**Katya Luscomb:** So I did.

**Katya Luscomb:** And we haven't necessarily gotten bad feedback from that, but a lot of times they're like, oh, well, we were actually thinking about it in this context.

**Bailey Seybolt:** Yeah, in which case, if you've done all the work, it's like, ugh.

**Katya Luscomb:** Yeah, I'm like, I spent 10 hours on this last week.

**Katya Luscomb:** Thanks, guys.

**Katya Luscomb:** I didn't actually spend that much on this.

**Katya Luscomb:** But this content calendar is basically existing entries.

**Katya Luscomb:** So most of your time is going to be like managing the content calendar.

**Katya Luscomb:** I have it set for like a couple months out just because of the sheer number that they gave us.

**Katya Luscomb:** There is some adjustment that will be needed because part of the plan is to publish, like once we start publishing again, is to publish a thousand of these existing entries each week.

**Katya Luscomb:** And then once we get the CBE GitHub connection linked, so push these to their team on Tuesdays.

**Katya Luscomb:** And then on Thursdays, push a batch of between 1,000 to 500 new CVE entries from GitHub.

**Katya Luscomb:** So two different pushes there, which, like, that's an insane amount of content.

**Katya Luscomb:** Honestly, like, if we're doing that much for them, I don't think we need the editorial at that point.

**Katya Luscomb:** Yeah, so part of the reason, like, I kept pushing the editorials, because I wanted us to be able to publish something.

**Katya Luscomb:** Especially, like, we got really excited when it launched.

**Bailey Seybolt:** And then the very next week, they're like, we have a code freeze.

**Katya Luscomb:** Okay.

**Katya Luscomb:** So my, and that was part of why I did the additional assignments and pulled teeth to get a few more editorial pieces, just to, like, good faith, keep experimenting, like, look into refreshes, see what we're thinking through there.

**Katya Luscomb:** I need to spend a little bit of time thinking about how I'm going to frame the conversation tomorrow.

**Katya Luscomb:** Or basically say, like, hey, you know, our initial content audit that we had done during the strategy sprint.

**Katya Luscomb:** in next one.

**Katya Luscomb:** Made it seem like there was potentially a lot more refresh opportunity.

**Katya Luscomb:** They specifically told us they don't want us to focus on cannibalization because they recently did a cannibalization audit.

**Katya Luscomb:** It's like outside of cannibalization, there's not a ton of opportunity for us to execute on in a really repeatable way.

**Katya Luscomb:** We don't actually recommend continuing to go down that route.

**Katya Luscomb:** It would probably just like suck up a lot of your time and hours trying to figure out how that would actually work.

**Bailey Seybolt:** And I'm curious, like, it seems like they really don't like certain types of content.

**Katya Luscomb:** Like I saw, like, on, like, anything that looked like a listicle, there were sort of comments.

**Katya Luscomb:** Yeah, so they rejected, like, any sort of listicle variation they rejected.

**Katya Luscomb:** So I've avoided those or just, like, reframed if the assignment direction spits it out.

**Bailey Seybolt:** And what about comparison articles?

**Bailey Seybolt:** It also seems like there was, like, they didn't, I didn't see a lot of those.

**Katya Luscomb:** And those always seem like, like, you know, the starting place for the comparison articles, I think, in.

**Katya Luscomb:** Isn't there strategy documentation where we talk about that?

**Katya Luscomb:** I think that was from when we were thinking about putting content on the blog as far as, because there's not, there's some comparison articles on CS1.

**Katya Luscomb:** Yeah, it's true.

**Bailey Seybolt:** It's much more like competitor comparisons.

**Katya Luscomb:** Exactly.

**Katya Luscomb:** Yeah.

**Bailey Seybolt:** Um, yeah.

**Katya Luscomb:** Okay.

**Katya Luscomb:** So the, um, the comparisons on CS101 are allegedly like dark web versus deep web, which, yeah.

**Katya Luscomb:** Um, you know, is similar to the content that we're already producing.

**Katya Luscomb:** So, um, trying to think through other things.

**Bailey Seybolt:** Um, I'm curious that I saw like in the, the strategy in terms of like future priorities, they talked about autonomy.

**Bailey Seybolt:** about autonomous operations content and developing business impact content.

**Bailey Seybolt:** I'm curious if that's something that's come up as, I guess that's more blog content then though.

**Katya Luscomb:** It's, it's somewhat blog content.

**Katya Luscomb:** It.

**Katya Luscomb:** It of reflects, we've got this topic cluster on like behavioral AI and autonomous security.

**Katya Luscomb:** I flagged this for them a few weeks ago in kind of starting to push back around like some of their keyword restrictions that a lot of topics that relate to this don't have high rankings yet because it's a fairly new realm.

**Katya Luscomb:** Like if they haven't written about it, it's a topic with almost no search volume.

**Katya Luscomb:** And so we've only published six articles.

**Katya Luscomb:** Some of these could probably get recategorized into this topic cluster, honestly.

**Katya Luscomb:** Like there's some companies that have like a very clear like hub and spoke approach where there's some sort of like pillar landing page and the content branches off from that.

**Katya Luscomb:** That's not really how they do things.

**Katya Luscomb:** They just have these broad categories that they chunk things into on their blog page.

**Bailey Seybolt:** Do they care about LLM?

**Bailey Seybolt:** Visibility?

**Bailey Seybolt:** Because it seems weird that they'd be targeting only these high volume keywords when so much of the opportunity there are these more like long tail.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** So they are interested in AI.

**Katya Luscomb:** I think they really want their content to be optimized for both, ideally.

**Katya Luscomb:** And so like a lot of the assignment approvals that they look for, like they're still very much in an SEO lens, even though AI visibility is part of what they want us looking at.

**Katya Luscomb:** So I think what they've been doing is like picking keywords that relate to like high volume SEO and then angling queries within that to like AEO.

**Bailey Seybolt:** That makes sense why it's also long then.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** And this is just what I've gathered based on like shifts and things.

**Katya Luscomb:** They haven't ever explicitly said this.

**Katya Luscomb:** So another like great question to talk about with them.

**Katya Luscomb:** This call feels like me saying a

**Katya Luscomb:** I didn't do that, but I should have.

**Bailey Seybolt:** No, I think the only difference here is I'm keeping those clients I have.

**Bailey Seybolt:** That's ones that were like, I didn't do this, but I should have.

**Bailey Seybolt:** like, at least I'm not hitting this one off.

**Katya Luscomb:** I know.

**Katya Luscomb:** I was like, I was just kind of starting to like get into a groove of like pushing on them on a few things on this.

**Bailey Seybolt:** And then what's the other have you with now?

**Bailey Seybolt:** What did they shift you on to?

**Katya Luscomb:** Did you keep your other clients?

**Katya Luscomb:** So I kept, yeah, I kept my other two.

**Katya Luscomb:** The only reason I'm handing them off is because their call is at my 7 a.m.

**Katya Luscomb:** Oh, right.

**Katya Luscomb:** You said, yes.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** I mean, otherwise, otherwise, the plan was originally for me to keep them.

**Katya Luscomb:** I was like, actually, can I not start my day at 630 on Thursdays?

**Katya Luscomb:** I didn't realize that the call was restricted to being that early when I first got them.

**Katya Luscomb:** Otherwise, they would have flagged it.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** And they, most of their team that is on the call is in India.

**Katya Luscomb:** So there's some stickiness with timing there.

**Katya Luscomb:** So they will probably be very grateful to have someone who.

**Katya Luscomb:** were.

**Katya Luscomb:** go.

**Katya Luscomb:** then.

**Katya Luscomb:** Because it would be what, your 9 a.m.?

**Katya Luscomb:** 10 a.m.?

**Katya Luscomb:** Are on Eastern Time?

**Bailey Seybolt:** I'm Eastern Time.

**Katya Luscomb:** Okay.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** So it'll your 10 a.m.

**Katya Luscomb:** for that call.

**Katya Luscomb:** So you could even, if you wanted to, could bump it earlier.

**Katya Luscomb:** They would probably appreciate that.

**Katya Luscomb:** Because I think it's there like 8.30 at night.

**Bailey Seybolt:** Well, we can ask on the call this week if they, I'm happy, if they want to bump it an hour earlier.

**Katya Luscomb:** That's fine.

**Katya Luscomb:** Okay, cool.

**Bailey Seybolt:** Offer that as a Goodwill.

**Katya Luscomb:** Yeah, yeah, yeah.

**Katya Luscomb:** Well, that's part of how I want to frame your introduction, too, of like, you're great, like, read you into all of this.

**Katya Luscomb:** And, you know, hopefully this can bring some, some closer coordination and, like, real-time, yeah, real-time collaboration.

**Katya Luscomb:** Because a lot of, like, they'll send me things and then I respond to it when they're already asleep.

**Bailey Seybolt:** So, yeah.

**Katya Luscomb:** What else was I going to say?

**Bailey Seybolt:** Is there anything else on my list?

**Bailey Seybolt:** I don't think so.

**Bailey Seybolt:** Yeah, mean, it seems like there's a lot of questions.

**Bailey Seybolt:** Marks here, but this isn't the only account that's like that.

**Bailey Seybolt:** Everyone's aware of it, and it seems like Kyle has a lot of context, so I can reach out to him.

**Katya Luscomb:** Yeah, he's been super helpful.

**Katya Luscomb:** I'm going to do some thinking about, I feel like I've got a pretty good framing around the refreshes.

**Katya Luscomb:** I'm trying to decide if I want to give them any documentation on how we started to do the audit or not, because there's just not really much there.

**Bailey Seybolt:** What was the refreshes?

**Bailey Seybolt:** Was the lack of opportunity just that it was pretty good content that's ranking anyway and doesn't really need be updated?

**Katya Luscomb:** Basically, their content is already so thorough, and a lot of it's pretty new.

**Katya Luscomb:** One of the ways we were looking at it is...

**Katya Luscomb:** I'm to pull this up again.

**Katya Luscomb:** I have so many messages all of a sudden.

**Katya Luscomb:** So we're basically looking at word count as like a way to filter the, like how extensive things are.

**Katya Luscomb:** Pretty much every piece of content that they have published, like it's got an FAQ, it's got pretty robust headers, like clear CTAs, all of those things that like would make it, you know, potential for refreshing.

**Katya Luscomb:** And so the word counts were one of the ways that we were trying to go about, like how can we filter this to find some potential opportunities to like expand on, you know, that template that we've sort of created for a lot of our content.

**Katya Luscomb:** Like maybe there's some of that that we can build in, but there's just not a good way at this point to like find those repeatable opportunities.

**Bailey Seybolt:** It also just seems like as a company, we're moving away from like taking on clients where it's like this hard to find the opportunity when there's so many clients out there for whom it's like so obvious and so much easier to do this for.

**Katya Luscomb:** Exactly.

**Katya Luscomb:** So here I'm going to send you this.

**Katya Luscomb:** It's in the call chat.

**Katya Luscomb:** It's in the call chat and should be in the doc.

**Katya Luscomb:** I'm sure it is.

**Katya Luscomb:** Here, I'll just, this is going to kind of messy.

**Bailey Seybolt:** in the call chat.

**Bailey Seybolt:** Did you maybe send it to the note taker?

**Katya Luscomb:** I did.

**Bailey Seybolt:** I'm being done.

**Bailey Seybolt:** do it every time.

**Bailey Seybolt:** I don't know why that's like the default where it starts.

**Katya Luscomb:** Here, I'm just going to send it to you directly.

**Katya Luscomb:** Actually, and then it's, I'm going to put all these links.

**Katya Luscomb:** There you go.

**Katya Luscomb:** And that way you don't have to, I always, I don't know why I send it in the call either because it deletes everything.

**Katya Luscomb:** Um, so this was, this was basically an approach looking at, um, like pulling things from SEMrush and then, um.

**Katya Luscomb:** And Kyle helped with this because we don't have a platform that growthx pays for to crawl and grab word counts.

**Katya Luscomb:** So he had access to one.

**Katya Luscomb:** So he did this.

**Katya Luscomb:** And basically what we found is that like the number with like low word counts.

**Katya Luscomb:** Um, let's see exactly how he sent me a little loom on this, but, but basically that like, there's not really a lot of opportunity there opportunity to like for a year's worth of content.

**Katya Luscomb:** that's really the lens that we're kind of trying to look at opportunities with Sentinel one is like, what, what's going to set us up well for like six months of runway within this so that the calibration period makes sense for all of us to invest time in.

**Katya Luscomb:** I think that might be something that I framed for the team too.

**Katya Luscomb:** Like, we don't want to waste your time either.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** yeah.

**Katya Luscomb:** You know, the CVE content engine is like, it's, it stands to be a really strong one.

**Katya Luscomb:** We can certainly continue to talk about, like we can execute on these, these keywords that we have developed, like through December.

**Katya Luscomb:** And like, maybe there's some, I did suggest doing some more long tail keyword research.

**Katya Luscomb:** I have not started on that.

**Katya Luscomb:** So I think that would be something really good for you and Yana to work on.

**Bailey Seybolt:** Well, we can take their temperature too, because if we're not interested in things that are of like lower volume, then it may just be a non-starter too.

**Katya Luscomb:** So I did, I poked at that a couple of weeks ago and they, they were like, you know, actually, like we are, we're open to that.

**Katya Luscomb:** Like, we're curious to see what those opportunities might look like.

**Katya Luscomb:** So I think, I think the piling and initial report, and again, just like seeing what, what might be out there.

**Katya Luscomb:** And if there are opportunities that like could become repeatable for AEO growth and things like that.

**Katya Luscomb:** I think it's, it's worth spending a little bit of time exploring just in case we can keep a content engine going.

**Katya Luscomb:** And maybe it's not five articles a week.

**Katya Luscomb:** Maybe we go to like two or three of those articles a week with that, with the context of like how much compute power and things we're using for the CVE pages.

**Bailey Seybolt:** And also if the articles are like 3,000 words each, it's really like two articles anyway.

**Katya Luscomb:** Totally.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** I did.

**Katya Luscomb:** I flagged that in a comment for them.

**Katya Luscomb:** They sent me a whole bunch of edits for one and I replied back.

**Katya Luscomb:** It's like, you know, one, like one, there was some repetition between sections that I was noticing and like, and how they have the headers framed.

**Katya Luscomb:** And the overall link, it ended up with like 3,200 words.

**Katya Luscomb:** It's like, do you, do you actually want content that's this long?

**Katya Luscomb:** Because this doesn't seem like it's optimized for SEO at that point.

**Katya Luscomb:** There's a lot of good stuff in there, but I didn't actually get a response to that.

**Bailey Seybolt:** So that's good to know.

**Katya Luscomb:** Again, like I can ask that on the call too, flagging of like, you know, as we, as we play with things in December going forward.

**Katya Luscomb:** Um.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** I think, and that's something I can flag too.

**Bailey Seybolt:** I feel like the, it would be great for you to raise the articles and like, just knowing that December is a holiday and, you know, it would be great to feel like we had a runway to get to January of topics and to know, like, basically, I don't want them to like sit on that and then approve nothing next week and then we're scrambling.

**Katya Luscomb:** Totally.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** If I poke at that on the call, I think they will, they'll work with us there or they'll tell us that all the topics are baloney and restart.

**Katya Luscomb:** Right.

**Katya Luscomb:** And that might be a really good lead way into like, yeah, you know, we're, we're kind of seeing this, this pattern where we're like repeatedly getting stuck here.

**Katya Luscomb:** Um, so I guess other question, like how, how much of the conversation do you want to jump into, or are you kind of wanting just to be introduced and then take it on more next week?

**Bailey Seybolt:** Yeah, that's the way I've sort of been doing it with the newer clients is sort of like being introduced, giving my background, you know, just.

**Bailey Seybolt:** Saying we're working together right now, you know, getting up to speed, whatever.

**Bailey Seybolt:** And then I've been jumping in with questions sometimes, but mostly letting the other person take the lead.

**Katya Luscomb:** Perfect.

**Katya Luscomb:** That's kind of what I figured.

**Bailey Seybolt:** That's how mine have mostly gone to.

**Katya Luscomb:** But yeah, just in case.

**Bailey Seybolt:** Unless there's anything you want me to like poke them on as the new person or be useful to like pretend that I don't know and ask the question again.

**Katya Luscomb:** I think next week it might be good.

**Katya Luscomb:** But I have tried to poke at like getting hard performance goals that they're trying to meet with content of like, you know, what are your what are your Q1 and Q2 like KPIs that you're trying to measure?

**Katya Luscomb:** What does that look like?

**Katya Luscomb:** That would probably be something really good for you to chat about.

**Bailey Seybolt:** That totally makes sense.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** Andy and I were talking about this like with a couple of my other clients, just like build rapport and goodwill and all that good stuff.

**Katya Luscomb:** I thought it was a great approach.

**Katya Luscomb:** Cool.

**Katya Luscomb:** I'm going to work on their agenda today.

**Katya Luscomb:** Today, I'm probably not going to write a ton of detail in it.

**Bailey Seybolt:** I think I'm going to make it more conversation-based.

**Bailey Seybolt:** That's fine.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** For me, from my point of view, since I'm really along for the ride this week.

**Katya Luscomb:** I appreciate it.

**Katya Luscomb:** I really appreciate how flexible and inquisitive you've been with this account because they're an odd duck.

**Bailey Seybolt:** Well, you know, I have a different account that's difficult in similar ways.

**Katya Luscomb:** So I feel your pain here.

**Katya Luscomb:** Yeah, the struggle.

**Katya Luscomb:** Yeah.

**Bailey Seybolt:** I should have pretended to be in a different time zone so that I could end it off.

**Bailey Seybolt:** Oh, funny.

**Katya Luscomb:** Just kidding.

**Bailey Seybolt:** I they, I got, I handed this one off and then they handed me Biologica, who's a challenge for a lot of different reasons.

**Bailey Seybolt:** So I'm like, well, you know, trade off.

**Bailey Seybolt:** I think it seems fair.

**Bailey Seybolt:** Like we all have to have some that are tricky and some that are easy.

**Bailey Seybolt:** Totally.

**Bailey Seybolt:** Like got only the tricky ones.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** 100%.

**Katya Luscomb:** And hopefully the tricky ones we got like match our respective strengths and areas to work.

**Katya Luscomb:** So, um, yeah, well, and they got getting their strategy ready was funky.

**Katya Luscomb:** Um, I, the CM who was working on this with me got pulled and promoted.

**Katya Luscomb:** And then the other gal who was supposed to jump in as a CM, um, like we were told that she was going to jump in as a CM.

**Katya Luscomb:** then like the very next week, like, actually we're doing this big restructure.

**Katya Luscomb:** And she's like, do I still learn and produce this content?

**Katya Luscomb:** was like, and I was, I was getting her up to speed on another account as well.

**Katya Luscomb:** I was like, just do those two and I will produce this one.

**Bailey Seybolt:** That part has been tricky.

**Bailey Seybolt:** I've had, I've had accounts where like, they haven't had the same CM on them for like more than two weeks.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** I've had only one account that was stable and otherwise people have quit.

**Bailey Seybolt:** People have gotten switched around and it's been like really hard to, to manage them.

**Bailey Seybolt:** Cause it's just like, it feels like you're getting someone up to speed, but you can never do the, like strategy, like the.

**Katya Luscomb:** Improvement of the artifacts and because you're just like not getting the right insight.

**Katya Luscomb:** So yeah, that part is tough.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** No, I was just starting to dig into like more of the Sentinel one, like pipeline and things.

**Katya Luscomb:** And I know I handed it to Yana.

**Katya Luscomb:** I like, it's not great.

**Katya Luscomb:** It's getting there.

**Bailey Seybolt:** It's not great.

**Bailey Seybolt:** I don't think any, like, I don't know.

**Bailey Seybolt:** I'm sure there are some.

**Bailey Seybolt:** I have like one or two where the like CM was just like a rock star and like really good at figuring it out.

**Katya Luscomb:** And then I have a bunch that are like a mess.

**Katya Luscomb:** Wow.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** Well, like Marisol was the CM on this for a long time and she was wonderful and did, she did a lot, but she was also pulled in a million different directions with other accounts too, because she was so good.

**Katya Luscomb:** So anyway, I've been chatting quite a long time.

**Katya Luscomb:** I want to make sure that you don't have any other big.

**Bailey Seybolt:** No, I feel like I have a much better.

**Bailey Seybolt:** I feel like the first time we talked, I hadn't even had a chance to like read through the documentation yet.

**Bailey Seybolt:** So now I feel like I actually had some questions and like a basic understanding of what they do and what.

**Bailey Seybolt:** The challenges are.

**Bailey Seybolt:** And so, yeah, I feel like we're in as good a place as we're going to be given the where we are.

**Bailey Seybolt:** Yeah, given everything.

**Bailey Seybolt:** So hopefully they'll approve some more topics and we'll get through this like December crunch and then we'll have like more opportunities to like think about strategy and the plan going forward in January.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** And I do think that like if we if we frame the conversation in the right way around pausing editorial content, like especially once CVE is really up and going, I think they'll be receptive to it.

**Katya Luscomb:** But we also talked about on the call, I had flagged for them initially that we were going to look into incorporating CVE into Looker, but it sounds like I know Yana flagged that like the number of lists that we would need to create for that would be pretty bonkers.

**Katya Luscomb:** And so probably better just to pull that from GA4, I think we were saying.

**Katya Luscomb:** So I wanted to make sure that was also on your radar.

**Katya Luscomb:** I will flag that for them on the call as well.

**Bailey Seybolt:** It won't be in their Looker dashboard, yeah.

**Katya Luscomb:** Yeah, we won't have it as a distinct cluster.

**Katya Luscomb:** It'll probably end up getting sorted into the non-growthx URLs.

**Katya Luscomb:** That might be something actually for you to look into.

**Bailey Seybolt:** Vivek might be a good person to ask.

**Katya Luscomb:** Yeah, I can ask him if there's a way to reflect them in Looker.

**Katya Luscomb:** Yeah, without having to create a bajillion lists for every single one.

**Katya Luscomb:** And then, oh, the other tricky thing.

**Katya Luscomb:** This will be more on Yana, but something for you to probably help figure out.

**Katya Luscomb:** One thing that they wanted within the CVE database is the link to the actual Sentinel-1 page.

**Katya Luscomb:** Page once it's published.

**Katya Luscomb:** I don't know if this is something that we can connect between Atlas and Airtable.

**Katya Luscomb:** I'm not sure if that's an option or I don't know the best way to systematize that.

**Bailey Seybolt:** I'll just ask.

**Bailey Seybolt:** I'll find out if it's possible and if it's not possible, we may just have to say we can't do it at the scale.

**Katya Luscomb:** Yeah.

**Bailey Seybolt:** I sort of feel like if it was possible, would they be doing it for all?

**Bailey Seybolt:** That's such a manual job that the CMS have to do right now.

**Bailey Seybolt:** I sort of feel like if it was possible, why wouldn't we be just doing it across accounts?

**Katya Luscomb:** My thought is maybe since we're auto-publishing from Atlas or auto-staging that the URL path might be easier to pull in bulk.

**Katya Luscomb:** Or maybe there's a way for us to export.

**Katya Luscomb:** Export batches?

**Bailey Seybolt:** Yeah.

**Katya Luscomb:** If we like export the batch and then like get that into a spreadsheet and then like somehow upload.

**Bailey Seybolt:** The tricky thing is like.

**Bailey Seybolt:** If the rows are mismatched at all.

**Katya Luscomb:** Exactly.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** So you'd have to have some sort of match between the CVE ID.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** There's probably, Carrie might be a really good person to ask about that as far as like building that into Airtable.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** Sorry, you're getting my problem-solving brain.

**Bailey Seybolt:** No, no.

**Bailey Seybolt:** That totally makes sense.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** I feel like maybe I'll find out if it's possible.

**Bailey Seybolt:** I don't even know if Airtable can pull from Atlas.

**Bailey Seybolt:** I don't either.

**Bailey Seybolt:** So I'll find that out first.

**Katya Luscomb:** And if not, it seems like getting it exported to a CVE and then we can figure out the best way to make sure it's accurate.

**Katya Luscomb:** That seems like it would be possible.

**Katya Luscomb:** Because I, yeah, I know we should definitely be able to export those when we produce them.

**Katya Luscomb:** And the URL should be, I think they're in Atlas already.

**Katya Luscomb:** I would assume so.

**Bailey Seybolt:** I think they have to be if we're public, if we're staging.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** I would assume the URL path is there.

**Bailey Seybolt:** You know what their, what CMS they're

**Katya Luscomb:** Oh gosh, which one do they use?

**Katya Luscomb:** They've talked about it in the calls.

**Katya Luscomb:** I feel like I'm starting to get a sense of which ones are a pain in the , even the ones that, without having used them directly.

**Katya Luscomb:** they mention it in the calls.

**Katya Luscomb:** I don't think it's specifically written in our documentation.

**Bailey Seybolt:** I will see if I can dig that up.

**Bailey Seybolt:** It's probably, it's got to be in Notion somewhere.

**Bailey Seybolt:** It'll be in Notion somewhere.

**Katya Luscomb:** They'll do a CMS walkthrough.

**Katya Luscomb:** Yeah, I think so.

**Katya Luscomb:** Well, I don't know if we do, because we don't actually do the publishing.

**Katya Luscomb:** Atlas, it's really tricky.

**Katya Luscomb:** So they've got all sorts of security measures, like for us to get access to their CMS was a real pain.

**Katya Luscomb:** like, you have to basically go through their employee onboarding.

**Katya Luscomb:** So I think Marcus and George Maine did that.

**Katya Luscomb:** So like, they could be in connecting Atlas and the CMS.

**Katya Luscomb:** But for anyone else, we're just, we're not in there.

**Bailey Seybolt:** So for editorial, do you do the same?

**Katya Luscomb:** stage it from Atlet?

**Katya Luscomb:** So they're interested in us looking into that.

**Katya Luscomb:** And we told them that we could look into setting it up.

**Katya Luscomb:** And that meeting happened, I think that was earlier, mid-October, where I was clarifying.

**Katya Luscomb:** was like, you know, with your review process, like basically we would still give you a Google Doc and then you would review it.

**Katya Luscomb:** And like, you know, we'd pass edits back and forth.

**Katya Luscomb:** And then they would still need to tell us when it's ready after PMM review.

**Katya Luscomb:** And that usually, like, they don't usually flag that.

**Katya Luscomb:** Like, I have to chase up every call of like, what got published this week?

**Bailey Seybolt:** What's the list for us to update?

**Katya Luscomb:** So that would, it would take a big lift off their shoulders, but we would really need to push for better communication around when things are ready.

**Katya Luscomb:** And I have this interface.

**Katya Luscomb:** case, I finally started to get Mahendra to use it for the approvals.

**Katya Luscomb:** because I'm Yeah.

**Katya Luscomb:** I'm I I I'm cool.

**Katya Luscomb:** I I'm I'm

**Katya Luscomb:** Before he was going and like commenting individually on those, it took forever to sort.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** Oh, we got some more approvals, it looks like, maybe.

**Katya Luscomb:** Maybe?

**Katya Luscomb:** Am I making it?

**Bailey Seybolt:** We do.

**Katya Luscomb:** We got a few more.

**Katya Luscomb:** So you could go through and play with the ContentOS here as well, if you wanted to take a look at that.

**Katya Luscomb:** And they are at least starting to like give some targets, like this one, I think I updated.

**Katya Luscomb:** Oh, no, I need to.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** update.

**Katya Luscomb:** So here, like I just make whatever changes and then I move it to like approve to start.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** And then what I, what I had, so this, this basically shows, oh, I don't want this sent to client in there.

**Katya Luscomb:** Oh, I'll update this later, but basically my idea was in, in our data, you can set in a content calendar row, like which week you want.

**Katya Luscomb:** Content produced.

**Katya Luscomb:** You or Yana, honestly, depending on how you guys want to shake that out.

**Katya Luscomb:** And then it shows up here so that they and we have a really clear view of where things are at.

**Katya Luscomb:** And this is supposed to be status.

**Katya Luscomb:** I just need to tidy this up.

**Katya Luscomb:** When I first go at prepping one of these, but this just gives a really nice overview.

**Katya Luscomb:** And then if you haven't already poked through their interface, I would recommend it because it's got a lot of different features in there.

**Katya Luscomb:** But the one other aspect that I would love to get them revising rather than like updating us in Slack is this review status here, which is editable.

**Katya Luscomb:** So I largely mark as it's pending SentinelOne review, which is their first pass of edits.

**Katya Luscomb:** And then once Mansi tells me that things have gone to their subject matter experts, that's this PMM review.

**Katya Luscomb:** And then...

**Katya Luscomb:** From there, it goes to publication with them.

**Katya Luscomb:** So if we add auto-publishing, we would need to know, like, they would need to change this to publication.

**Katya Luscomb:** I think that's the easiest way by far.

**Katya Luscomb:** So they're not, like, specifically having to, like, copy and paste titles to us all the time.

**Katya Luscomb:** And then we can just look and be like, ready to publish?

**Bailey Seybolt:** Great.

**Bailey Seybolt:** We'll push it through Atlas.

**Katya Luscomb:** Yeah.

**Bailey Seybolt:** Yeah, that's what I've done with other clients as well.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** And I think it makes it a lot easier.

**Katya Luscomb:** I do, I need to make sure that they can, I think Nancy would need added access here to be able to update that.

**Katya Luscomb:** Because this is, this is right now me going in and changing all these.

**Katya Luscomb:** So there is that.

**Katya Luscomb:** And then I have the CVE content calendar separated out here as well.

**Katya Luscomb:** Yeah.

**Bailey Seybolt:** That's great.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** So I was really proud of this when I said it.

**Bailey Seybolt:** look, I also, I was not much of an Airtable user.

**Bailey Seybolt:** And had to create a few interfaces.

**Bailey Seybolt:** And.

**Bailey Seybolt:** felt very proud of myself.

**Katya Luscomb:** Most of my clients that I'm taking over don't have one.

**Katya Luscomb:** I'm like, all right, project for mid-December, quiet week, maybe.

**Katya Luscomb:** I can hold these up for people.

**Bailey Seybolt:** Cool.

**Bailey Seybolt:** All right.

**Bailey Seybolt:** Well, thank you so much.

**Bailey Seybolt:** This was great.

**Bailey Seybolt:** I feel like I have a much better sense of where we stand in terms of personalities and content and strategy.

**Bailey Seybolt:** So thank you for putting so much work into getting us on the speed.

**Katya Luscomb:** I will probably still be slacking you with questions, but.

**Katya Luscomb:** Totally.

**Katya Luscomb:** Okay.

**Katya Luscomb:** I will provide as much clarity as I can.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** And then happy to be resourced.

**Katya Luscomb:** I'll be on the call this week and I will, unless it moves to like 5 a.m.

**Katya Luscomb:** or something crazy next week, I'll plan on joining next week just in case there's follow-up.

**Bailey Seybolt:** But I figure you'll probably leave that one and prep it and all that good stuff.

**Bailey Seybolt:** Yes.

**Katya Luscomb:** I think that makes sense.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** I can also, if you don't want to join, I can follow up with you async if there's anything.

**Katya Luscomb:** Either way.

**Bailey Seybolt:** Details on.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** I can let you know, see how, how swamped I am.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** Um, heads up for you.

**Katya Luscomb:** I am out Friday.

**Katya Luscomb:** Um, okay.

**Katya Luscomb:** But I, I don't anticipate anything wild happening.

**Katya Luscomb:** Um, but just in case there's questions that come up and I don't answer, that's why.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** So I'll be here.

**Bailey Seybolt:** I'll be on Slack.

**Bailey Seybolt:** Sounds good.

**Bailey Seybolt:** Well, enjoy the rest of your day.

**Bailey Seybolt:** Um, good luck with the rest of your week and I will see you bright and early tomorrow.

**Bailey Seybolt:** Tomorrow.

**Bailey Seybolt:** All right.

**Bailey Seybolt:** Bye.

**Bailey Seybolt:** Bye.
