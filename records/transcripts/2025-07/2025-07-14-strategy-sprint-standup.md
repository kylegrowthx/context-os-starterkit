# Strategy Sprint Standup

<metadata>
date: 2025-07-14
time: 15:31 UTC
duration: 21 minutes
organizer: Nemanja Simic
participants: Kyle Gaudreau, Andi Bailey, Aida Knezevic, Sydney Go, Dave Capone, Jo Kaminska, Nemanja Simic, Matthew Alves-Hill, George Haikal, Marisol Smith
fathom_recording_id: 73936490
fathom_url: https://fathom.video/calls/350561349
share_url: https://fathom.video/share/VbxSsmeBuGy7XbyfNWr55ehKTLLLvsvF
source: fathom
enriched_on: 2026-03-03 13:41 UTC
</metadata>

---

## Summary

The GrowthX delivery team held a strategy sprint standup covering multiple client projects and upcoming kickoffs. Key priorities included three new client onboardings (Sentinel-1, Diligent, and Okta/Auth0) with varying delivery models, ongoing content delivery across eight active clients (Metronome, Monograph, Airbyte, Interwild, Biologica, Hypergrowth, Enjin, Town, and Augment Code), and workflow optimizations to improve content generation quality and efficiency. The team discussed contract status, team capacity, and next-week sprint planning for new workflow builds and client deliverables.

---

## Context

This is an internal GrowthX delivery standup led by Andi Bailey, focusing on the delivery and operations side of the business. The meeting brought together GrowthX's content delivery team and supporting staff (Kyle Gaudreau on sales/partnerships, Sydney Go and Nemanja Simic on engineering/workflows). The standup runs through the delivery status and priorities across multiple concurrent client engagements, ranging from initial kickoffs to established relationships in their second-third month. The team tracks content production status, client approval cycles, workflow customization requests, and upcoming deliverables across multiple verticals and content types (blogs, white papers, case studies, social posts). The broader context: GrowthX has recently scaled from 2-3 concurrent clients to 8-9, with three new clients onboarding in the same week, requiring careful attention to delivery capacity, team allocation, and maintaining delivery quality while scaling operations.

---

## Relevance

**To GrowthX Delivery:**
- Workflow customization requests (Airbyte fact-checker, Monograph AROPS setup) indicate client needs diverging from standard playbooks; flagging strategic trade-offs (sharing backend code/processes vs. proprietary protection)
- Atlas workflow improvements (automated medical claim tagging for Biologica) are reducing manual QA load and enabling faster content scaling
- FAQ generator bug in Airbyte workflow is blocking 100 blog articles; needs immediate resolution
- Content approval cycles are extending client timelines; Metronome, Monograph, and Augment Code all waiting on client sign-off

**To GrowthX Business Development:**
- Three new client kickoffs in one week (Sentinel-1, Diligent, Okta) indicates successful pipeline conversion but tight delivery capacity
- Okta/Auth0 deal is custom and non-standard (created due to Rachel's relationship with Marcel), demonstrating willingness to be flexible on deal structure for strategic relationships
- Augment Code (week 7 of 6-week engagement) likely to extend beyond contract; ROI calculator in progress for CEO conversation signals expansion opportunity
- Biologica website launch in September provides known checkpoint for content roadmap planning
- Hypergrowth deal structure unclear; team providing free podcast-to-content work but unsure if custom workflows are included in scope, indicating potential scope-creep risk

**To CheckThat:**
- Airbyte project emphasizes fact-checking gaps in AI-generated content, highlighting demand for content verification capabilities
- Biologica's medical claim tagging requirement shows healthcare verticals have unique regulatory/compliance content needs

---

## Overview

- New client kickoffs (Sentinel-1, Diligent, Okta) upcoming; each with unique content refresh/creation needs
- Multiple projects (Metronome, Monograph, Airbyte) progressing with content generation and workflow improvements
- Handoffs and transitions occurring for Biologica, Enjin, and potentially Augment Code projects
- Need to clarify deliverables and expectations for newer clients (e.g., Hypergrowth, Town)

---

## Key Topics

### New Client Kickoffs

  - Sentinel-1 & Diligent: Content refresh opportunities, addressing organic traffic downturn
  - Okta (Auth0): Custom workflows for outbound growth, unique deal due to existing relationship
  - Initial artifacts set up in Notion, to be updated post-kickoffs

### Ongoing Project Updates

  - Metronome: White paper strategy shared, awaiting approval; goal to generate approved content this week
  - Monograph: Reviewing artifacts; exploring AROPS setup request (need to clarify scope and strategic implications)
  - Airbyte: Refresh workflow facing technical issues; SEMrush blogs (100) ready for generation once bug is fixed
  - Interwild: New content structure deliverables on track; 250 ketamine pieces nearly ready for publishing
  - Biologica: Handoff in progress; Atlas workflow updated for medical claim tagging; website launch in September
  - Hypergrowth: Blog and social post generation from podcast transcript; need to clarify publication strategy
  - Enjin: 9 articles in production; new pipelines for each vertical set up in Atlas
  - Town: 4 new blogs planned; need to set up Looker dashboard

### Project Transitions and Contracts

  - Augment Code: In week 7, likely to extend; 4 new blogs reviewed, 1 ready for publishing
  - Contract sent on Friday, awaiting response; ROI calculator being prepared for CEO discussion

### Workflow and Process Improvements

  - Airbyte: Customizing workflow, adding fact-checker for statistics
  - Monograph: Exploring AROPS setup, considering strategic implications of sharing backend processes
  - Biologica: Atlas workflow updated to automate medical claim tagging

---

## Action Items

**Aida Knezevic (GrowthX)**
- File Linear ticket for Monograph AROPS request. Get detailed requirements from client.
- Deliver 1 more blog for Biologica EOD today
- Generate blog + social post for GE (Hypergrowth) by Wed
- Set up Looker dashboard for Town this week

**Nemanja Simic (GrowthX)**
- Create Linear ticket for FAQ generator issue in Airbyte workflow

**Andi Bailey (GrowthX)**
- Create Linear ticket to pull back feedback step in Airbyte workflow

**Dave Capone (GrowthX)**
- Deliver new content structure deliverables for Interwild EOD tomorrow
- Create Linear ticket for Town Looker dashboard setup

**Jo Kaminska (GrowthX)**
- Invite Daryl to weekly Enjin call. Analyze + prepare first signals report for James.

---

## Transcript
**Andi Bailey:** Alright, do we have most of the people?

**Andi Bailey:** Not yet.

**Andi Bailey:** Give it another minute.

**Andi Bailey:** We have two kick-ups today, is that right?

**Aida Knezevic:** Yep.

**Andi Bailey:** Sentinel-1 and then one tomorrow.

**Andi Bailey:** Maybe we'll do a just quick check on how we feel about those kick-offs.

**Andi Bailey:** And Kyle, I think you gave us some context on Thursday, so if there's anything else that we need to note on Sentinel-1 and then Diligent.

**Kyle Gaudreau:** Sorry, I don't think I caught the complete comment.

**Andi Bailey:** Was there any particular questions?

**Andi Bailey:** No, just if there's any, like, I think you gave us like a little bit of a...

**Andi Bailey:** A high level of what they're looking for, but if there's anything else that you want us to keep in mind, know, did you share the notes here?

**Kyle Gaudreau:** Sentinel-1, yeah, they're in the client workspaces, so there's sales handoff notes for each.

**Kyle Gaudreau:** Sentinel-1, you know, there's going to be probably a bit more refresh opportunity there.

**Kyle Gaudreau:** They have a decent amount of content, MET's editorial, Diligent's going to be pretty similar, in that they have a decent amount of content, probably some refreshes, and as well as, like, Diligent, just as a reminder, they're PE-backed, and they've also been seeing, like, when they were first talking to us, like, a downturn in organic traffic, and so I think they hypothesized some of that is because of AI overviews, and GEO, but it would be good for us to, like, validate that, so a good place to find some quick wins, for sure.

**Kyle Gaudreau:** Okta is going to be very custom.

**Kyle Gaudreau:** This is like, you know, us creating custom workflows for Rachel to help with getting, to be clear, like the Auth0 brand, which sits under Okta, getting their growth motions back on track and mainly focused on the outbound side of things.

**Kyle Gaudreau:** There could be opportunities beyond that.

**Kyle Gaudreau:** Rachel has a variety of different experiments she wants to run.

**Kyle Gaudreau:** She also goes way back with Marcel, so that's why we were willing to take on something that was a bit more custom.

**Kyle Gaudreau:** So, yeah, that one's a bit of a unique one, not one we would, not a type of deal we would typically sign up for, but just because we know Rachel.

**Kyle Gaudreau:** So, we're willing to be flexible.

**Andi Bailey:** Okay.

**Andi Bailey:** Cool.

**Andi Bailey:** Thank you.

**Andi Bailey:** And it looks like we've got initial artifacts set up.

**Aida Knezevic:** Yeah, created something just to have it in Notion, but we'll update it after the kickoffs.

**Andi Bailey:** Cool, awesome.

**Andi Bailey:** Metronome, how are we doing?

**Aida Knezevic:** Yeah, I'm meeting with Nem and Sydney a little later just to discuss what we're going to do this week.

**Aida Knezevic:** But a quick update is that on Friday we shared the white paper kickoff strategy doc with them.

**Aida Knezevic:** They are going to have a meeting today and get back to us.

**Aida Knezevic:** The goal for this week, but I still have to align with Sydney and them on this, is basically we need them to approve artifacts.

**Aida Knezevic:** And we want to generate at least like one piece of content that they're happy with.

**Aida Knezevic:** And then next week, we want to just hopefully go full steam ahead with the white paper content.

**Aida Knezevic:** We have already generated.

**Aida Knezevic:** Some, like, three pieces for them, like, in the first week after their kickoff, but hopefully, like, they'll approve the white paper strategy, and this week we can already start, like, generating some of that content.

**Andi Bailey:** Okay.

**Andi Bailey:** Is that, those three pieces related to the white paper stuff?

**Aida Knezevic:** I think so.

**Aida Knezevic:** Sydney, can you confirm?

**Aida Knezevic:** I think they were.

**Sydney Go:** Yeah, some of them are related to the white paper stuff, but the SEO strategy is closely tied to the white paper strategy.

**Andi Bailey:** Great.

**Andi Bailey:** Okay.

**Andi Bailey:** Monograph?

**Aida Knezevic:** Okay.

**Aida Knezevic:** So, I sent them, they're still sort of reviewing their artifacts.

**Aida Knezevic:** I'm going to send them a reminder today.

**Aida Knezevic:** Today, I want to get back to them regarding their AROPS request.

**Aida Knezevic:** I don't know if you saw that, Andy, but basically, they want someone on our team to set up their AROPS.

**Aida Knezevic:** It seems like Daniel's all for it.

**Aida Knezevic:** I don't know if I should wait for Marisol to weigh in before I get back to them, but I just want to make sure that we have at least an idea of who could take this on from the dev team and how big of a lift, because I really have no idea how big of a lift that is for someone on the dev team, so that's what we need to find out.

**Andi Bailey:** Okay, so that's what they would be generating content kind of like alongside us for the air ops?

**Aida Knezevic:** Yeah, yeah, it's something that they would like be using internally.

**Aida Knezevic:** We are still, I mean, this week, we're going to present like the assignments during the meeting, some initial assignments that we found.

**Aida Knezevic:** And the goal is by the end of this week, to have one piece of content to send them for review.

**Aida Knezevic:** And then hopefully next week, we can kind of, you know, start to scale.

**Andi Bailey:** Okay, yeah, that's an interesting tension. I think I'd be interested to know how much of the content they're going to be generating and what kind of content they're going to be generating. That's probably a strategic question, and Kyle, you probably know this better than I do about whether we want to keep linking our back-end code in Airbyte in that way, because I think that's something we want to get away from. We could set up their Airbyte, but there's probably something we don't want to surface — like, what we're doing on the back-end for them.

**Aida Knezevic:** Yeah, yeah, I mean, they want to generate case studies, just as a note, yeah.

**Kyle Gaudreau:** Yeah, I mean, I'm not sure exactly how Daniel would set it up. In the case you're mentioning, we wouldn't necessarily just be — if we were still running our workflows and customizing them, we'd just be doing that largely through the API. So they wouldn't get anything. I don't know if Daniel would just try to set up something custom, I'm guessing not.

**Kyle Gaudreau:** It could be worth trying to unpack what they're trying to do. I heard case studies, but is Airbyte really necessary?

**Kyle Gaudreau:** Maybe they already have it and they're dabbling in it.

**Kyle Gaudreau:** One thing we've talked about in the past of like, how would we get customers set up to run workflows on their own if we wanted to?

**Kyle Gaudreau:** One thing we kicked around, which we never did, but theoretically is possible is setting them up with N8N and just like getting that set up there, similarly like leveraging our workflows.

**Kyle Gaudreau:** So, I don't know, I'm sure Daniel's thinking about all that anyways and so, but as far as like risk of them like trying to run content that would be comparable, I wouldn't worry about that at this point.

**Andi Bailey:** Okay.

**Andi Bailey:** Yeah.

**Andi Bailey:** Let me think about where we asked the question to get you an answer, Aida.

**Andi Bailey:** Is there a ticket for it?

**Andi Bailey:** Like, do you have a linear ticket?

**Aida Knezevic:** I haven't added it to linear yet because I just wanted to share it in the internal channel first to see if that's something we can do. Daniel seems to think that it's fairly simple.

**Aida Knezevic:** Okay.

**Andi Bailey:** If you can file a linear ticket — they have their weekly sprint planning meeting tomorrow, and that will be a good place for them to discuss the trade-offs from an engineering perspective and the level of effort. Then we can also have a separate discussion on whether strategically we have any concerns. But try and get as much detail as you can from them about what they're wanting to do, which you'll need anyway for the linear ticket.

**Aida Knezevic:** Okay.

**Andi Bailey:** Yep.

**Andi Bailey:** Okay.

**Andi Bailey:** Cool.

**Andi Bailey:** Thank you.

**Andi Bailey:** All right.

**Andi Bailey:** Airbyte, do we have anybody to talk through Airbyte?

**Andi Bailey:** I know so much is happening in person with them.

**Andi Bailey:** Okay.

**Andi Bailey:** Looks like no.

**Nemanja Simic:** The only update is I'm running the refreshes right now.

**Nemanja Simic:** And it's getting to the end to the FAQ generator, but stopping.

**Nemanja Simic:** So I'll probably just put up a ticket in for that right after this call just to get it done because it was working last week.

**Nemanja Simic:** And I have 100 of them in here ready to go.

**Andi Bailey:** Okay.

**Andi Bailey:** And then did you, you and Matthew think about SEMrush?

**Nemanja Simic:** Oh yeah.

**Nemanja Simic:** Yeah.

**Nemanja Simic:** We got all those blogs picked and everything. I have a hundred of them stuck on the last stage in Atlas right now, not generating for the last hour or so. Once that bug is sorted out, I think we should be good to go. And for automated publishing, I have a meeting with Ben tomorrow to make sure it goes well.

**Nemanja Simic:** And assuming all that goes well, we should be in a good place.

**Andi Bailey:** Okay.

**Andi Bailey:** And then I think the other question was we wanted to make this workflow more customized.

**Nemanja Simic:** Do we know in what ways we're looking to do that yet?

**Nemanja Simic:** Well, I spoke with George on Friday, and one thing that we could really use in the workflow is a fact checker to make sure stats are working. Right now, the way I have the refresh instructions set up, I'm avoiding new statistics but still referencing external sources, which it does well but not for actual numbers. I'm keeping external sources and it's been doing a fairly good job with that. I'll probably have to go into each blog and adjust a couple things, but it's in a much better place than it was.

**Andi Bailey:** Yeah.

**Andi Bailey:** Okay.

**Andi Bailey:** Cool.

**Andi Bailey:** And I still owe a linear ticket for making sure that we can pull back the feedback step in that we used to have, too.

**Andi Bailey:** I don't know if that was for this, but I'll make sure that linear ticket's in for tomorrow.

**Kyle Gaudreau:** We also sent them out the amendment last week, by the way.

**Andi Bailey:** Oh, awesome.

**Andi Bailey:** Do we have a timeline on when we'll get it back?

**Kyle Gaudreau:** Not really.

**Kyle Gaudreau:** He didn't respond, so I'll probably just follow up with him at some point today.

**Nemanja Simic:** There's a call with him right now as we speak, so.

**Kyle Gaudreau:** Oh.

**Kyle Gaudreau:** So maybe he comes up during the call.

**Andi Bailey:** Okay, got it.

**Andi Bailey:** All right.

**Andi Bailey:** Cool.

**Andi Bailey:** Interwild.

**Andi Bailey:** Dave, how are we doing on the new format, or the new content structure deliverables?

**Dave Capone:** Yeah, I'm on target to deliver all that by end of day tomorrow.

**Dave Capone:** They shared the blog post template on Friday.

**Dave Capone:** I gave a round of feedback.

**Dave Capone:** And then on this morning, I went through it again and gave another round of feedback on that.

**Dave Capone:** So, so far, so good.

**Dave Capone:** I'll have those deliverables ready to go.

**Andi Bailey:** Cool.

**Andi Bailey:** And I think it sounds like we're just waiting on one thing to get publishing those 25 ketamine, 250 ketamine pieces, right?

**Dave Capone:** Like for the connection with Kirkland.

**Dave Capone:** Yeah, Kirkland this morning tagged me on here for the ticket for all of that.

**Dave Capone:** But I'll go through and review just to double check on

**Dave Capone:** I'll review it to double-check as well, but that does look pretty good.

**Andi Bailey:** Okay.

**Andi Bailey:** Biologica, how are we feeling on the handoff for this one?

**Aida Knezevic:** I'm meeting Jess and Jacob today to discuss the handoff, and then I added Jacob to the meeting tomorrow.

**Aida Knezevic:** So, yeah, I mean, we have everything set up.

**Aida Knezevic:** Like, Atlas should be fully ready to go now.

**Aida Knezevic:** There was just one small tweak that the dev team had to make.

**Aida Knezevic:** To spare you the details, basically, Biologica's team would like to see all of the medical claims that the fact checker checked. They want them to be tagged with MD or something. That was the last update that the dev team had to do to the workflow, to just automate that process so we don't have to make those tags manually.

**Aida Knezevic:** And yeah, I'm going to deliver them one more blog by end of day, hopefully, because I wasn't able to do two yet on Friday.

**Andi Bailey:** Cool.

**Andi Bailey:** And then what are we publishing?

**Andi Bailey:** Like, what's the, like, ongoing speed of publishing that they're expecting?

**Aida Knezevic:** Do we know?

**Aida Knezevic:** They don't have a website yet, so they're launching in September.

**Aida Knezevic:** They're going to, once that, once they have a website built, we're going to plan around that.

**Andi Bailey:** Okay, cool.

**Andi Bailey:** Hyper Growth.

**Aida Knezevic:** George sent me the podcast transcript that they did with GE last week. I'm going to try to generate a blog and a social post for GE tomorrow or Wednesday. My one thing is that during our last meeting, Marcel pitched a publication for the output, and I want to clear up whether that's something they would want or if they want to publish it on Hypergrowth's website. The dev team is going to add Hypergrowth's custom workflows to the new sprint they're starting, so hopefully we'll have those built out sooner rather than later.

**Andi Bailey:** Okay.

**Andi Bailey:** Yeah, we need to figure out if that's actually part of the deliverables, because we're doing all this work for free, so it sounds like that might be an extra piece of work we would be adding on.

**Andi Bailey:** All right, Enjin, how are we feeling about the handoff?

**Jo Kaminska:** I'm in touch with Daryl and Carrie. I had a meeting with them on Friday. I'm wondering if I should invite Daryl to the weekly call. I'll make an intro today and we'll manage this.

**Jo Kaminska:** Besides, like, we are pretty good with content production.

**Jo Kaminska:** James reviewed our articles and he accepted all of them.

**Jo Kaminska:** And we have nine articles in production for this week.

**Jo Kaminska:** So, we are good on this end.

**Jo Kaminska:** And this week I'm diving into analytics, like, first signals, et cetera, because James wanted to see this.

**Jo Kaminska:** And...

**Jo Kaminska:** I think that's pretty much it.

**Jo Kaminska:** One more thing.

**Jo Kaminska:** We have new pipelines for each vertical already in Atlas, and they are probably mapped to each persona, so we are pretty much prepared for any topic that the customer may accept.

**Andi Bailey:** Oh, amazing.

**Andi Bailey:** That's really cool.

**Jo Kaminska:** So, yeah, we're in this one, generally.

**Andi Bailey:** Great.

**Andi Bailey:** Town?

**Aida Knezevic:** Yeah, so I synced with Daryl on Friday.

**Aida Knezevic:** We're doing four new blogs for them this week, and Daryl is also going to join the weekly sync on Wednesday.

**Aida Knezevic:** I'm just waiting on Town to finalize their internal review process for the content, so they should get back to us by tomorrow, I think.

**Aida Knezevic:** And then we do need to set up a Looker dashboard for them this week. I'm not sure who can help out with that, but they're a brand new website.

**Aida Knezevic:** We have access to their GSC, their GA4.

**Aida Knezevic:** So, yeah, that's one thing that's left over to do.

**Andi Bailey:** Okay.

**Andi Bailey:** Dave, yeah, I see you've got a thumbs up there.

**Andi Bailey:** Do you have a linear dashboard set up yet so we can start to see timeline and stuff on this?

**Dave Capone:** I do not yet.

**Dave Capone:** This would be the perfect case to add one.

**Dave Capone:** So this will be the first ticket that goes on to that.

**Andi Bailey:** Awesome.

**Andi Bailey:** All right.

**Andi Bailey:** And then augment code.

**Andi Bailey:** We're in week seven with them, but it sounds like we're probably going to go past that.

**Andi Bailey:** I don't know if we have anybody on the call that can speak to that.

**Aida Knezevic:** I reviewed four blogs for them this morning that Marisol created. We have one that they've reviewed that we could publish, and then we have four new ones coming up. We should figure out if we want to start publishing this week. I just wanted to flag that we probably do want to start publishing this week.

**Andi Bailey:** Okay.

**Andi Bailey:** Did we get their approval on, like, high-level strategy?

**Andi Bailey:** Kyle, you know anything about where we are with contracting or anything like that?

**Kyle Gaudreau:** We sent the contract out on Friday. No word back yet. George sent it out and we packaged the varying ideas. George has been discussing with them and was also working on sending an ROI calculator, because I think this is going to have to be a discussion with their CEO.

**Andi Bailey:** All right, well, let's hope we can keep this going.

**Andi Bailey:** All right, that is everything.

**Andi Bailey:** Any other pieces, open questions people want to talk about in the stand-up?

**Andi Bailey:** Awesome.

**Andi Bailey:** Have some time back.

**Aida Knezevic:** Thanks, guys.

**Aida Knezevic:** Thank you.

**Aida Knezevic:** Bye.

**Aida Knezevic:** Bye.
