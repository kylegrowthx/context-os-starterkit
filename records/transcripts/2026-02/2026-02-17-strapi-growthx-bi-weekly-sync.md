# Strapi <> GrowthX -  Bi-Weekly Sync

<metadata>
date: 2026-02-17
time: 17:29 UTC
duration: 27 minutes
organizer: team@growthxlabs.com
participants: Victor Coisne, Paul Bratslavsky, Theodore Kelechukwu Onyejiaku, Carrie Chowske
fathom_recording_id: 123038871
fathom_url: https://fathom.video/calls/568840574
share_url: https://fathom.video/share/uqK-VSsB6cszdfwYC6zt6UeJWjywTpFP
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

GrowthX and Strapi reviewed production status, AI visibility metrics, and automation improvements. Pipeline is healthy with 14 articles in review and 30+ approved topics, shifting focus to content refreshes to leverage existing high-intent assets. Strapi maintains 100% visibility on core headless CMS prompts across AI platforms, with Gemini showing strong growth in referral traffic. Theo is building an N8N workflow to automate Airtable/Slack updates on Strapi publication events, solving a key operational tracking challenge. Meeting cadence moves to bi-weekly (next: March 3) as the workflow has stabilized.

---

## Context

Strapi is a headless CMS platform and a GrowthX client for B2B content marketing services focused on driving AI visibility. This is a regularly-scheduled bi-weekly sync between GrowthX (Carrie Chowske managing delivery) and Strapi's engineering/product team. The relationship focuses on creating integration pages and optimized content to capture referral traffic from AI tools like ChatGPT, Perplexity, and Gemini. GrowthX uses CheckThat, their proprietary AI visibility index, to track Strapi's performance across AI platforms.

---

## Relevance

**To GrowthX Delivery:**
- Shifting from new content creation to content refresh strategy to leverage existing high-intent assets — demonstrates mature content pipeline management with 14 articles in review and 30+ approved topics.
- Airtable schema improvements underway to track refreshes vs. new content, showing evolving ops maturity.
- N8N workflow automation for publication tracking (Strapi → Airtable + Slack) eliminates manual tracking pain — model for process efficiency across other clients.

**To CheckThat:**
- Strapi has 100% visibility on core headless CMS prompts across 7-week tracking window, with ~45 new integration-related prompts added to the platform.
- Gemini and CoPilot are emerging as high-growth referral sources (alongside ChatGPT and Perplexity), driven by Google's mobile AI integration — valuable data for AEO strategy.
- Form embedding issues resolved by vendor (Notum); validation of portal IDs still pending technical review.

**To GrowthX Business Development:**
- Meeting cadence moving to bi-weekly reflects stable workflow and reduced operational friction — positive account health signal.
- Content OS launch timeline accelerated as a side-effect of CheckThat rollout, creating internal dependency alignment.
- Integration page performance shows strong user intent signals, supporting expansion opportunity into vertical-specific content strategy.

---

## Overview

- **Production Focus:** Shifting to content refreshes to leverage existing assets, as the pipeline is healthy with 14 articles in review and 30+ approved topics.
- **AI Performance:** Strapi has 100% visibility on core headless CMS prompts, with Gemini showing strong growth in referral traffic.
- **Process Automation:** Theo is building a N8N workflow to automate Airtable/Slack updates on content publication, solving a key tracking challenge.
- **Website Bug:** The comparison page display bug will not be fixed, as a new website launching in April will render the work redundant.

---

## Key Topics

### Content Production & Pipeline

  - **Pipeline Status:**
      - 14 articles in review
      - 17 approved topics
      - 13 integration pages ready
  - **New Focus → Content Refreshes:**
      - Rationale: Leverage existing high-intent content assets.
      - Tracking: Airtable is being updated to better track refresh projects.
  - **Form Embeds:**
      - Status: Fixed by Notum.
      - Action: Theo to confirm correct portal ID is used.

### Performance & AI Visibility

  - **Overall Performance:** Sessions and engagement remain strong.
  - **Integration Pages:** High engagement confirms high user intent.
  - **AI Visibility (7-Week View):**
      - Core Headless CMS Prompts: Strapi mentioned 100% of the time.
      - Referral Traffic Sources:
          - Top 3: ChatGPT, Perplexity, Gemini.
          - Growth: Gemini and CoPilot are increasing, driven by Google's mobile AI integration.
  - **Check That Platform:**
      - Access: Theo and Victor have access.
      - New Prompts: \~45 integration-related prompts added to gather data.

### Process & Tooling

  - **Meeting Cadence:** Moving to bi-weekly (next: March 3) to reflect a stable workflow.
  - **Content OS:**
      - Goal: Replace Airtable for a unified workflow.
      - Timeline: Launch may be accelerated.
  - **Publication Automation:**
      - Problem: Manual tracking in Airtable and Slack is inefficient.
      - Solution: Theo is building an N8N workflow to automate updates on publication.

### Website Bug: Comparison Pages

  - **Issue:** Content cards on comparison pages are not displaying on the front end.
  - **Decision:** No fix will be implemented.
      - Rationale: A new website is launching in April, making a fix redundant.
      - Impact: This will delay the live publication of new comparison pages.

---

## Action Items

**Theodore Kelechukwu Onyejiaku (Strapi)**
- Share Spotify link of artist w/ Victor, Paul, Carrie
- Build N8N workflow: Strapi publish → Airtable + Slack
- Publish pending integration pages this week
- Investigate comparator page content visibility; report back to Victor

**Victor Coisne (Strapi)**
- Sync offline w/ Theo re: form embeds/portal IDs; confirm go-ahead

---

## Transcript
**Carrie Chowske:** This meeting is being recorded.

**Paul:** Hey, who are you?

**Carrie Chowske:** Love that background.

**Paul:** That's fun.

**Paul:** Oh, thanks.

**Paul:** Yeah, just mixing it up a little bit.

**Carrie Chowske:** Mine's still just my boring bookshelf.

**Paul:** Oh, The Danielle's character.

**Paul:** I need to get, like, some furniture with some, you know, cozy looking.

**Carrie Chowske:** You just look like you're getting ready to, like, drop, like, the latest podcast.

**Carrie Chowske:** I like it. I like this, but I can't, like I get, I'm backlit, but I have a really nice window right here.

**Paul:** I just can't open it.

**Paul:** Yeah, it's awesome.

**Paul:** I do want, like, my room to have more character. It's just, like, so unrealistic that I don't have enough stuff to put in the background.

**Carrie Chowske:** I hear that.

**Carrie Chowske:** How was your weekend?

**Carrie Chowske:** Did you have a long weekend for the U.S.

**Paul:** holiday?

**Paul:** Yeah, we did, we did.

**Paul:** Yeah, weekend was good.

**Paul:** How was yours?

**Carrie Chowske:** Good, same.

**Carrie Chowske:** We did a lot of thrifting this weekend.

**Carrie Chowske:** My husband and I are, like, on this mission.

**Carrie Chowske:** We just moved into our house two years ago, and it's totally different from our old, we have a 110-year-old house now.

**Carrie Chowske:** And so, like, I'm in this phase of, like, wanting to thrift everything.

**Paul:** I refuse to buy anything new.

**Paul:** Yeah.

**Carrie Chowske:** And, like, the desk that I'm using is from the 1950s, from Las Vegas high school. That a friend gave me. Like, just, it's stupid. It's so dumb. I just feel so bad.

**Paul:** Like, because for one thing, new stuff, the quality is not that great anyway.

**Paul:** And where are you based on it again?

**Carrie Chowske:** I'm north of Charlotte, North Carolina. I'm in Salisbury, which is about smack in the middle of the state.

**Paul:** Yeah, yeah.

**Paul:** I used to go to Charlotte a while back ago.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Hi, Victor.

**Victor Coisne:** Hey, how are you?

**Carrie Chowske:** Good.

**Carrie Chowske:** How are you?

**Victor Coisne:** Hey, Theo.

**Carrie Chowske:** We're We're just talking about our weekends.

**Carrie Chowske:** Anybody else do anything fun?

**Paul:** I mean, I did.

**Paul:** My sister, she's like, you need to have more hobbies.

**Paul:** And she knows, like, I love music.

**Paul:** So she's like, you haven't been making music lately.

**Paul:** So I was like, you know what?

**Paul:** Let me do an impulse buy.

**Paul:** So I got a guitar.

**Carrie Chowske:** Oh, nice.

**Victor Coisne:** I did Scott headphones, so you could put, uh.

**Theodore Kelechukwu Onyejiaku:** Um, voice of the, I've forgotten the title, but he had a very great voice, like, like that of Michael Jackson.

**Theodore Kelechukwu Onyejiaku:** Oh, nice.

**Theodore Kelechukwu Onyejiaku:** So it was, it was really great for me.

**Victor Coisne:** That's awesome.

**Victor Coisne:** You should send us the link so we can, if they're on like Spotify or something, we can listen to them.

**Theodore Kelechukwu Onyejiaku:** Yeah, sure, I'll do that.

**Victor Coisne:** Awesome.

**Carrie Chowske:** Sounds like everybody had fun. All right, you guys want to get into this and we'll kind of catch up on what has been going on on our end?

**Carrie Chowske:** Um, I was out of office yesterday also.

**Carrie Chowske:** So, um, I just wanted to make sure that we kind of got, um, we're on the same page in terms of production.

**Carrie Chowske:** Um, there are 14 articles in review.

**Carrie Chowske:** Um, so there's probably still, there's probably just a few more than we had last week.

**Carrie Chowske:** Um, and we've currently got 17 topics approved and 13 integration, integration pages.

**Carrie Chowske:** So we're okay for a little while. I think next up we had talked about doing more refreshes. Is that still where we're at? I think that's probably still a good bet.

**Victor Coisne:** Yeah.

**Carrie Chowske:** And I'll show you why I think that in a second.

**Carrie Chowske:** But I did add some prompts to check that related to integrations.

**Carrie Chowske:** It's a lot of, like, best of things for this integration.

**Carrie Chowske:** And, you know, so there are a lot of those kinds of ones, but they're based on ones that we've created content for.

**Carrie Chowske:** So we'll be able to see if those are coming up, hopefully, in those answers.

**Carrie Chowske:** And then I'm still working on getting those refreshes updated.

**Carrie Chowske:** So, Usman was out last week.

**Carrie Chowske:** So I had, he was kind of, he was still checking his Slack, which I told him, he's like, you need to take some time off.

**Carrie Chowske:** But I was glad he didn't take it all off because he answered a lot of questions for me last week.

**Carrie Chowske:** And one of them was, we're just making some changes in Airtable so we can track what's a refresh and what's not a little bit better.

**Carrie Chowske:** So once we do that, then we'll have those, they'll have that fully fleshed out.

**Carrie Chowske:** But we do have some data.

**Carrie Chowske:** So that's at least good news. I think we're good here.

**Carrie Chowske:** Did we ever get the comparison page issues we were having fixed?

**Carrie Chowske:** I feel like we did.

**Carrie Chowske:** I don't think I ever updated this.

**Theodore Kelechukwu Onyejiaku:** Yeah, I am still following up on the preview, which I've created the issue.

**Theodore Kelechukwu Onyejiaku:** But, well, I think Victor has the best answer, because I was going to, like, ask Victor about it, considering the fact that we are making some migrations.

**Victor Coisne:** Yeah.

**Victor Coisne:** We're not trying to fix too many things on the website because we're working on, like, a new website.

**Victor Coisne:** So essentially, like, spending money to fix something that's going to get fixed no matter what.

**Victor Coisne:** So, yeah, I think this one we can just, you know, cancel because, like, it's going to get fixed, but it's just going to be a bit delayed.

**Victor Coisne:** I think we're still able to be live in April.

**Victor Coisne:** So that's...

**Theodore Kelechukwu Onyejiaku:** In that vein, I would like to ask about the embedded forms, the form embeds.

**Theodore Kelechukwu Onyejiaku:** Is this something we have to proceed with?

**Theodore Kelechukwu Onyejiaku:** Because Usman is asking for a go-ahead, so I don't know if that's...

**Victor Coisne:** Well, that one is fixed.

**Victor Coisne:** As far as I know, that one is completely fixed.

**Theodore Kelechukwu Onyejiaku:** Okay, okay.

**Theodore Kelechukwu Onyejiaku:** Because although I noticed the last one he did, I checked, it got removed, and the last update was made by you.

**Theodore Kelechukwu Onyejiaku:** But I noticed the one he shared with me, the ID, the portal ID was different from the one Goza created in the GitHub repo.

**Theodore Kelechukwu Onyejiaku:** But we could talk more about it.

**Theodore Kelechukwu Onyejiaku:** I just wanted...

**Victor Coisne:** Yeah, let's talk about that one offline.

**Victor Coisne:** yeah, so Notum did the work and now like embed form should work as expected.

**Victor Coisne:** So it's just a matter of like just using the newsletter as the...

**Carrie Chowske:** I said, Oh, my goodness.

**Carrie Chowske:** I worked with her at the last agency we both worked for.

**Carrie Chowske:** So anyway, it's very fun to see.

**Carrie Chowske:** She's really she does amazing work with case studies.

**Carrie Chowske:** So she's a lot of fun to talk to.

**Carrie Chowske:** And then we talked, I think we talked about going biweekly, I believe.

**Carrie Chowske:** So our next meeting will be March 3.

**Carrie Chowske:** I'm going to be kind of working half days next week because I've got family in town. But we're going to use that opportunity to take us to a regular biweekly cadence. That doesn't mean we can't meet more often if we need to.

**Carrie Chowske:** It's totally up to you.

**Carrie Chowske:** But just so that we're on a good cadence. I think we're in a good flow at this point.

**Carrie Chowske:** We don't have a lot of like week to week things that are that we aren't taking care of over Slack.

**Carrie Chowske:** So let me know if that doesn't sound good to you.

**Victor Coisne:** Yeah, I think that's fine.

**Victor Coisne:** For me, as long as we get the updates on Slack and you know, the big thing that we're really looking forward to is getting access to the content OS.

**Victor Coisne:** I think that's fine. We want to make sure we understand how the workflows are built and like we can build some ourselves without relying 100% on GrowthX. You know, it's what we used to have on AirOps that we know.

**Carrie Chowske:** My understanding last I heard, and this was just like last week or the week before, I think they're going to, it kind of happened a little bit by accident, but we're, that might be rolling out sooner than we, than I last told you, just because they, part of us rolling out, like launching Check That, we worked on the content OS side of it, like kind of in conjunction, Daniel was working on that.

**Carrie Chowske:** So it sounds like they've moved up that timeline a little bit better than we thought.

**Carrie Chowske:** So hopefully that's coming soon, but I'll keep you posted as soon as I hear anything.

**Carrie Chowske:** But I know we're all dying for it too, because it's going to replace Airtable for us and have us like, I'm not a fan of switching back and forth between different platforms all day long.

**Carrie Chowske:** So like I got excited today that we finally got, you know, access.

**Carrie Chowske:** That's the HubSpot rather than having to be like, hey, can you check HubSpot for me?

**Carrie Chowske:** So anyway, I get excited about these things.

**Carrie Chowske:** Don't judge.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** So for performance, I just went, I pulled us back to like a week-to-week view because I kind of wanted to see where we've been the last few weeks.

**Carrie Chowske:** It's overall looking pretty good in terms of sessions, engagements looking pretty strong, and especially on the integration pages, which makes sense.

**Carrie Chowske:** That kind of content tends to, people that get there tend to have high intent, so that makes, that gives us a good signal that it's useful and people are continuing to engage with it.

**Carrie Chowske:** And then I went and looked at like those integration pages just because I had the list of the ones you didn't want us to touch, and then the one, I have a list of ones we were doing just to kind of look and see.

**Carrie Chowske:** They're basically kind of the same thing where I'm seeing more of a division in terms of engagement and sessions has more to do with the type of content. And then if you're looking at just the core headless CMS prompts, Strapi has mentioned 100% of the time.

**Carrie Chowske:** And this is just over a seven-week period, which is what I've kind of started doing for AI because I see it moving around so much that I like to just look at it week to week.

**Carrie Chowske:** And what we should continue to see is that we may not hit that 100% mark every week in terms of visibility, but that we see it kind of steadily.

**Carrie Chowske:** We're getting more and more traction in those areas so that you start to see citations grow and you see share of voice grow and that sort of thing.

**Carrie Chowske:** Top referrers are ChatGPT, which continues to be the big player. Perplexity is pretty strong for Strapi, and then Gemini. Claude and CoPilot make up a really small subset of that traffic. Most of it's coming from these three platforms.

**Victor Coisne:** Is that the same for you, some of your other customers?

**Carrie Chowske:** Pretty much.

**Carrie Chowske:** Everybody has ChatGPT as their top one.

**Carrie Chowske:** It just depends.

**Carrie Chowske:** Some have, you know, Gemini is number two.

**Carrie Chowske:** Some have Perplexity.

**Carrie Chowske:** A few have Claude.

**Carrie Chowske:** Almost nobody has Copilot as like a number two.

**Carrie Chowske:** But ChatGPT is the top one still for everybody.

**Carrie Chowske:** I'm seeing a lot of gain in, you know, Google in general, like whether it's AI overviews or their built-in.

**Carrie Chowske:** is that?

**Carrie Chowske:** Theirs is what?

**Carrie Chowske:** Gemini.

**Carrie Chowske:** Gemini, that I'm seeing that starting to gain a lot of traction and that's kind of holding true for, you know, across the board.

**Carrie Chowske:** Like if I look at, this is your referral traffic for the last 60 days, like you see that most of these are kind of, you know, holding fairly steady or dropping slightly.

**Carrie Chowske:** But Gemini is increasing along with like Copilot.

**Carrie Chowske:** Those are the two that I'm seeing grow right now.

**Carrie Chowske:** But particularly Gemini, because I don't know if you've used Google on mobile lately, but like it really kind of funnels you into their AI.

**Carrie Chowske:** Like, oh

**Carrie Chowske:** Almost forcing you into it, short of like actually just making you go there.

**Carrie Chowske:** But if you do read the AI overview, prompts you to like search using just Gemini.

**Victor Coisne:** Okay.

**Victor Coisne:** That's so cool.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Like I said, we're seeing this 100% visibility coming through all these core prompts.

**Carrie Chowske:** I just added about 45-ish on the integrations related stuff.

**Carrie Chowske:** So we should start getting some data on that this week.

**Carrie Chowske:** So we'll see more there as well.

**Carrie Chowske:** But just on this, this is really good.

**Carrie Chowske:** This is very strong, especially when you're looking at, you know, both branded and unbranded prompts in here.

**Carrie Chowske:** These are really good metrics to see.

**Carrie Chowske:** I tend to kind of like look at these a little holistically rather than looking strictly at citations or position or, you know, any of them.

**Carrie Chowske:** Because citations, obviously, aren't getting clicked on as much in AI responses as they were before. Okay, awesome.

**Carrie Chowske:** Let me know if you have any questions or if you're able to access the space we've created, that's the one that you should have the full access to.

**Carrie Chowske:** It probably asked you when you logged in to create a space.

**Carrie Chowske:** And then that's just so that you can have like a personal space that's unique to you versus like the company-wide, like everybody's got access to that platform.

**Carrie Chowske:** So you should have both.

**Carrie Chowske:** You should have a personal one and then the one we created for Strapi. Let me know if you can't easily access it and I'll add you.

**Theodore Kelechukwu Onyejiaku:** At first, I got my own space. Then I had to go back to the invitation, and I was asked to sign up. After I signed up, I went back to the invitation and accepted it, and then I saw the Strapi dashboard.

**Carrie Chowske:** Perfect. It's a known UX issue that we have right now. It's good that we're getting feedback. They know about it and they're working on it. It's a bit of a barrier. I did the same thing, Theo. I would have thought to do that, but not a lot of people are thinking to do that.

**Carrie Chowske:** So we want to make sure that they easily get access if we invite them.

**Carrie Chowske:** So any other questions about Check That or AI visibility?

**Victor Coisne:** No, I have access now, so I'll also look a little bit, spend a bit more time on the platform.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Let me know if you have any questions. Happy to answer them.

**Carrie Chowske:** I got to work really closely with the product team when we were starting on SEO content for the site. I have a little bit more insider knowledge than most, but I still often have to ask them questions. I'm really feeling positive about what we're seeing. Not just the metrics, but the usability of it is really strong and it's getting better all the time. That's pretty good.

**Carrie Chowske:** Theodore, were you able to use that webhook? Were you able to get that going?

**Theodore Kelechukwu Onyejiaku:** To add it to the Strapi code would require Notum to accept my pull request. So I decided to use N8N instead, and I already got access today.

**Carrie Chowske:** Okay.

**Theodore Kelechukwu Onyejiaku:** So I'll create workflow that we trigger using the Strapi webhook so that when I publish one, it gets updated on Airtable and possibly a message on Slack.

**Carrie Chowske:** Amazing. Thank you. I love that.

**Carrie Chowske:** Usman and I were talking this morning. You work with somebody and people track what they're doing in different ways. We need to find a system that works for both of us because I keep having to ask him questions about what he's working on. So we'll have visibility on what's being done.

**Carrie Chowske:** So that'll help us a lot, Theo.

**Carrie Chowske:** I appreciate that.

**Carrie Chowske:** Anything else that we need to go over?

**Carrie Chowske:** Did I miss anything?

**Carrie Chowske:** Anything that I didn't bring up?

**Victor Coisne:** One quick question is more for Theo, but like on the, I think on our end, says like there's about 15, if remember correctly, the number of things that are pending, like publishing.

**Victor Coisne:** Do, on the integration page, like do you confirm like it's pretty like low lift for you to, to publish and you don't have to do too much of a review?

**Victor Coisne:** For blog posts, I think it makes sense to do a more extensive review. For integration pages, I think we agreed it's less intensive.

**Theodore Kelechukwu Onyejiaku:** The last time I was able to publish them. So for this week, I'll check the list and publish them as well.

**Theodore Kelechukwu Onyejiaku:** And is it the same link you shared with me before, Carrie?

**Theodore Kelechukwu Onyejiaku:** Or is there a new one showing the new integration pages that we're adding?

**Carrie Chowske:** It should be the same one.

**Carrie Chowske:** Yeah, it should be dynamic.

**Carrie Chowske:** It should update whenever we update Airtable.

**Carrie Chowske:** Usman just put those in either late Friday or early yesterday. So they're new and haven't been sitting there very long.

**Theodore Kelechukwu Onyejiaku:** Oh, okay.

**Theodore Kelechukwu Onyejiaku:** Thank you.

**Carrie Chowske:** Yeah, you're welcome.

**Victor Coisne:** Sweet.

**Victor Coisne:** And for the comparator pages, it's the same, right?

**Victor Coisne:** Like we should be able to kind of batch, like ideally, like we don't even need to do that much of a review because I think like...

**Theodore Kelechukwu Onyejiaku:** Yeah, I also published the last ones. The issue is that the content is not being displayed on the front end.

**Theodore Kelechukwu Onyejiaku:** I was asking if I should create an issue. I think I've brought this up before. So I will definitely check back on that because that was the bug I was experiencing.

**Victor Coisne:** Okay.

**Victor Coisne:** I didn't realize the content wasn't updating. I guess I'm not following why it's not visible. If it's added in the admin panel, it should be visible live.

**Theodore Kelechukwu Onyejiaku:** Yeah. The content cards list, which has the different sections of each comparator page, is not being displayed. I'll create a new issue for Notom and get back to you.

**Victor Coisne:** Okay, sounds good. I'll have a closer look, but I'm trying to make sure we don't defocus the Notom team.
