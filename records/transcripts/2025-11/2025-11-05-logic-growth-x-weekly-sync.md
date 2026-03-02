# Logic <> Growth X - Weekly Sync

<metadata>
date: 2025-11-05
time: 18:30 UTC
duration: 29 minutes
organizer: bailey@growthx.ai
participants: Bailey Seybolt (GrowthX), Jakub Rudnik (GrowthX), Steve Krenzel (Logic)
fathom_recording_id: 99466689
fathom_url: https://fathom.video/calls/463300431
share_url: https://fathom.video/share/7KLeKaJP_5LMyQBuastkaprhR4DNwXZ2
source: fathom
enriched_on: 2026-03-02 18:45 UTC
</metadata>

---

## Summary

Sync on content progress and plan for embedding workflows.

---

## Context

GrowthX is delivering content marketing and editorial services to Logic, a workflow automation platform. Logic has embedded interactive workflows into their blog as a key conversion strategy, with GrowthX responsible for identifying strategic placement and publishing articles. This weekly sync aligns the teams on content progress, technical implementation of workflow embedding, and analytics setup for tracking performance across topic clusters.

---

## Relevance

**To GrowthX Delivery:**
- Workflow embedding is now live on Logic's platform, enabling GrowthX to embed interactive product demos directly in blog content. This creates a new content model combining educational articles with conversion-driving workflows.
- Content pipeline is stalled with 5 articles in review and 5 in production waiting for approvals from Logic. GrowthX needs to tag articles in Airtable going forward and manually identify placement for workflows before engineering can automate the process.
- Analytics misalignment: Looker cohorts don't map to Logic's four strategic topic clusters, preventing accurate performance tracking. Bailey must coordinate with Ada to fix the cohort mapping.

**To CheckThat:**
- Logic is using interactive workflows to demonstrate product value within educational content — a potential use case for CheckThat's AI visibility workflows if Logic becomes interested.

**To GrowthX Business Development:**
- Logic's signup flow is being overhauled from WorkOS to an in-house property, creating an opportunity to propose UX/conversion optimization (Jakub shared the blurred product screenshot tactic as an experiment).
- Two demo bookings generated through Logic's website CTA (marketing automation and logistics/trucking spaces), indicating the content-to-demo pipeline is working. Logic is seeing promising engagement on Looker.
- Strong partnership signal: Logic consistently ships product updates, and GrowthX is delivering weekly progress. This momentum indicates healthy account health and expansion potential.

---

## Overview

- [**Workflow embedding is live:** The technical capability to embed interactive workflows is now live, using a simple `{{logic-workflow slug="[slug]" caption="[caption]"}}` string in Storyblok.](https://fathom.video/share/7KLeKaJP_5LMyQBuastkaprhR4DNwXZ2?tab=summary&timestamp=848.0)
- **Pilot will use vetted workflows:** The initial pilot will use Logic's 36 high-quality, industry-specific workflows, leveraging existing assets to test the process quickly.
- **Looker reporting requires a fix:** The Looker dashboard is misconfigured, showing too many cohorts. Bailey will remap them to the four strategic topic clusters for accurate performance tracking.
- **Manual publishing continues for now:** Logic will continue manually publishing articles for 1-2 weeks to ensure image and workflow integration is smooth before automating the process.

---

## Key Topics

### Content & Site Updates

  - **New Features:** Logic shipped two key features for the blog:
      - Table of Contents (ToC)
      - Blog Categories/Tags
  - **Content Pipeline:** The pipeline is temporarily stalled due to a lack of article approvals from HX.
      - **In Review:** 5 articles
      - **In Production:** 5 articles

### Strategy: Embedding Workflows

  - **Goal:** Embed interactive workflows directly into blog content to demonstrate product value and drive conversion.
  - **Technical Implementation:**
      - [The system uses a simple string in Storyblok to trigger an embed: `{{logic-workflow slug="[slug]" caption="[caption]"}}`](https://fathom.video/share/7KLeKaJP_5LMyQBuastkaprhR4DNwXZ2?tab=summary&timestamp=848.0)
      - This method is familiar to GrowthX (similar to Webflow CTAs) and simplifies engineering.
  - **Pilot Plan:**
      - **Asset Selection:** Use the 36 vetted workflows from Logic's industry pages.
      - **Rationale:** This leverages existing, high-quality assets to test the process quickly and efficiently.
      - **Process:** GrowthX will manually identify the best placement for workflows in upcoming and existing articles. This manual test will validate the editorial process before building automation.

### Strategy: Aligning Analytics & Content

  - **Problem:** The Looker dashboard is misconfigured, showing too many cohorts instead of the four strategic topic clusters defined in the content OS.
  - **Impact:** This prevents accurate performance analysis of content clusters (e.g., traffic, conversions) and hinders strategic decision-making.
  - **Proposed Solution:** Bailey will investigate the Looker setup and remap the cohorts to the correct topic clusters.
  - **Related Action:** Bailey will also review blog categories to align them more closely with the topic clusters for better UX and tracking.

### Opportunity: Signup Page Optimization

  - **Suggestion:** Add a blurred product screenshot to the signup page background.
  - **Rationale:** This tactic has been shown to significantly lift conversion rates by providing visual context for the product.
  - **Context:** The suggestion is highly relevant as Logic is currently overhauling its signup flow, bringing it back onto its own property from WorkOS.

---

## Action Items

**Bailey Seybolt (GrowthX)**
- Add blog tags to Airtable for future staging
- Prioritize articles matching industry-page workflows; embed 1–3 per article using slug/caption
- Review blog categories vs topic clusters; propose alignment to Jakub
- Fix Looker cohort mapping to align w/ topic clusters; coordinate w/ Ada

**Steve Krenzel (Logic)**
- Consult Azzam re: auto-publish vs manual; then decide after 1–2 weeks
- Sync workflow spreadsheet w/ current list; share w/ Bailey

**Jakub Rudnik (GrowthX)**
- Document and share signup-page CTA/blur experiment idea w/ Steve

---

## Transcript
**Jakub Rudnik:** How's your week going?

**Bailey Seybolt:** Oh, okay.

**Bailey Seybolt:** It's going.

**Bailey Seybolt:** HX never got back to us with any articles to approve, so I feel a little bit like a parent who keeps, like, trying to get their kid to, like, do the assignment.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** Then they get all the feedback on why it's the wrong assignment or, you know, how the teacher's wrong, but it doesn't do the very basic part.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** Yep.

**Jakub Rudnik:** Yep.

**Jakub Rudnik:** Not the rarest thing, but not fun.

**Bailey Seybolt:** How about you?

**Jakub Rudnik:** It's pretty productive, but just a lot of little things to work through.

**Jakub Rudnik:** And I think I like pinched a nerve or something on my back.

**Jakub Rudnik:** Oh, man.

**Jakub Rudnik:** My wife like didn't like one of the pillows and gave it to me.

**Jakub Rudnik:** And that pillow feels weird not to put this on her.

**Jakub Rudnik:** But I woke up the next day.

**Jakub Rudnik:** I was like, I can barely turn my neck.

**Jakub Rudnik:** And this is day two.

**Jakub Rudnik:** It's gone up and down.

**Jakub Rudnik:** But I'm doing a lot of like eating pad.

**Bailey Seybolt:** It happened to be last year.

**Bailey Seybolt:** I call them sleep injuries.

**Bailey Seybolt:** It's like you hit your 30s.

**Bailey Seybolt:** And then suddenly you like injure yourself doing nothing.

**Jakub Rudnik:** Very real.

**Jakub Rudnik:** I've got like a sports-related back injury that I'm like actively dealing with, too.

**Jakub Rudnik:** So I'm like just quite old.

**Bailey Seybolt:** And a knee thing.

**Bailey Seybolt:** Yesterday, I literally got x-rays on my back, my knee.

**Bailey Seybolt:** And I have PT for it.

**Jakub Rudnik:** just like it's stuff that it's like backing up.

**Jakub Rudnik:** don't.

**Jakub Rudnik:** I didn't get taken care of, and then, yeah, I had to, like, delay some doctors because of the move.

**Jakub Rudnik:** Then I pinched my, I'm like, just feel uncomfy all the time.

**Bailey Seybolt:** I know.

**Bailey Seybolt:** I finally started weight training to, like, deal with my sleep injuries.

**Jakub Rudnik:** Okay.

**Bailey Seybolt:** Hi, Steve.

**Bailey Seybolt:** Sorry for being late.

**Steve Krenzel (Seattle):** No worries.

**Steve Krenzel (Seattle):** How's it going?

**Steve Krenzel (Seattle):** Good.

**Steve Krenzel (Seattle):** How are you?

**Bailey Seybolt:** We're good.

**Bailey Seybolt:** We're just comparing back injuries.

**Steve Krenzel (Seattle):** Oh, no.

**Steve Krenzel (Seattle):** Who's, who's the worst?

**Jakub Rudnik:** Well, it started with, like, sleep injuries.

**Jakub Rudnik:** think I, like, pinched a nerve in my neck or my upper back that's, hurts my neck overnight, two nights ago.

**Steve Krenzel (Seattle):** And then I got, like, a soccer back thing, too.

**Jakub Rudnik:** So we're just talking about being in there, being older than what used to be.

**Jakub Rudnik:** And just, yeah, sleep injuries.

**Jakub Rudnik:** I like that, Bailey.

**Bailey Seybolt:** I'm going to steal that.

**Bailey Seybolt:** It's very depressing, but, you know.

**Steve Krenzel (Seattle):** I know that well, yeah.

**Bailey Seybolt:** I know Yeah.

**Steve Krenzel (Seattle):** Yeah.

**Steve Krenzel (Seattle):** Yeah.

**Steve Krenzel (Seattle):** Cool.

**Steve Krenzel (Seattle):** Just kind of jumping into things.

**Steve Krenzel (Seattle):** Two kind of fun things.

**Steve Krenzel (Seattle):** Over the last week, we shipped table of contents.

**Steve Krenzel (Seattle):** And what was the other thing on the resources page?

**Bailey Seybolt:** Oh, have blog categories now.

**Steve Krenzel (Seattle):** Oh, yeah.

**Steve Krenzel (Seattle):** Tags.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** So you can filter by tags and table of contents.

**Steve Krenzel (Seattle):** And in theory, today, we'll have embedded workflows, so.

**Bailey Seybolt:** Oh, yeah.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** I can see.

**Bailey Seybolt:** I didn't notice the table of contents.

**Steve Krenzel (Seattle):** That's awesome.

**Steve Krenzel (Seattle):** Thanks.

**Jakub Rudnik:** That's great news.

**Jakub Rudnik:** Well, thank you for, you know, for all the clients we have, things don't always move that fast.

**Steve Krenzel (Seattle):** So thank you very much.

**Jakub Rudnik:** And it's really nice to just, like, come into stuff moving forward.

**Steve Krenzel (Seattle):** Cool.

**Steve Krenzel (Seattle):** Yeah.

**Steve Krenzel (Seattle):** Likewise.

**Steve Krenzel (Seattle):** Azam shared this in earlier, like, a month or so ago.

**Steve Krenzel (Seattle):** But one of the things we've been consistently impressed with GrowthX is, like, every week it feels like something's moving forward with y'all.

**Steve Krenzel (Seattle):** So, we just want to reciprocate.

**Steve Krenzel (Seattle):** Yeah.

**Steve Krenzel (Seattle):** Thank All right.

**Steve Krenzel (Seattle):** Thank

**Jakub Rudnik:** We'll take it.

**Steve Krenzel (Seattle):** This is great.

**Jakub Rudnik:** That makes for a very healthy partnership, so right on.

**Bailey Seybolt:** So I'm just going to share the agenda, make sure we don't skip over anything that we had today.

**Steve Krenzel (Seattle):** Is Azam joining us today, Steve, or is it just the group?

**Steve Krenzel (Seattle):** He's out of office today.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** Cool.

**Bailey Seybolt:** All right, then.

**Bailey Seybolt:** Well, that's exciting.

**Bailey Seybolt:** I saw we had, you know, the blog tags and the table of contents.

**Bailey Seybolt:** So I will make sure that we capture the category or the tags going forward in the Airtable so that those are properly tagged when we stage them for you in the CMS now that we have access.

**Bailey Seybolt:** Cool.

**Bailey Seybolt:** And then do you want us to continue, and maybe this is a question for Azam when he's back, but do you want us to continue staging them and let you all press publish, or would you rather we set up publishing automatically once they're in?

**Steve Krenzel (Seattle):** I think for probably another week or two, we'll manually publish if you stage.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** That sounds good.

**Bailey Seybolt:** I guess that makes sense if you're all using your own images as well.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** That's great.

**Bailey Seybolt:** Well, I had written this before I saw that the blog categories, so we don't need to review them.

**Bailey Seybolt:** They are set up.

**Bailey Seybolt:** And then I think we have five more articles that are in review and then five that are in production to deliver this week.

**Bailey Seybolt:** So I'm just flagging that, but it may be if, you know, if Fathom's out of office, but that's why we have a bit of a backlog right now.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** so I will just leave those as is.

**Bailey Seybolt:** And then I think the big thing we wanted to sort of talk about today and define some next steps around was gathering more info on the existing library so we can embed that, those kind of playbooks in the blog.

**Bailey Seybolt:** And the way we were thinking about it is, you know, it'd be great to build a library.

**Bailey Seybolt:** Match to use cases in whatever format made sense.

**Bailey Seybolt:** And I think probably, you know, manually incorporating them for testing and to make sure it works makes sense.

**Bailey Seybolt:** But then eventually, you know, we could build it so that it was automated and just pulled in the ones that made most sense based on the context.

**Bailey Seybolt:** So I guess the questions were, one, sort of figuring out what is the best way to build out that library.

**Bailey Seybolt:** Like knowing what you have available, matching them to use cases.

**Bailey Seybolt:** And then I thought it probably made most sense, at least for the upcoming ones, to take a look at kind of the topics that we have approved from you.

**Bailey Seybolt:** I think we have like a few weeks of approved topics and see if we could identify prioritizing ones where you have like existing ones that we could pull in.

**Steve Krenzel (Seattle):** Cool.

**Steve Krenzel (Seattle):** Yeah, that'd be great.

**Steve Krenzel (Seattle):** And when you say library.

**Steve Krenzel (Seattle):** Yeah, would Thank

**Steve Krenzel (Seattle):** You're referring to, like, a collection of workflows related to the article that we're publishing?

**Bailey Seybolt:** Yeah, exactly.

**Bailey Seybolt:** Like, I'm thinking, let me pull up, yeah, so I was sort of looking at your website, at the ones you sort of already had embedded in the pages, and thinking, you know, I'm not sure sort of how many you have, but, like, if we could capture somehow what you already have and match them to the use cases that we talk about in content, then it would be pretty easy for us to kind of pull those in.

**Bailey Seybolt:** And then, so developing that library of seeing how many we have and what those use cases are and matching them to content, and then this approved to start is the sort of existing runway of our approved article topics we have.

**Bailey Seybolt:** So, we could take a look at this and think about which ones might make sense to prioritize first if we want to start testing.

**Bailey Seybolt:** Bling those in.

**Steve Krenzel (Seattle):** Okay.

**Steve Krenzel (Seattle):** Yeah, we do have a bunch of kind of pre-existing workflows that we somewhat haphazardly threw together.

**Steve Krenzel (Seattle):** And so I really want to probably consult with Azam on whether it's better to start with the article and then, or consult with you guys, start with the article and then think of one to three kind of workflows we could create and embed in it, because it's very easy for us to create a new workflow, or we should start with the workflows that we've already created and then kind of shape content around that.

**Steve Krenzel (Seattle):** If we had been more thoughtful about the list of workflows we have right now, I'd be more inclined to do the latter.

**Steve Krenzel (Seattle):** But I, like right now, the, if you go to our industries page, you'll see, like, each of these will have six workflows on them.

**Steve Krenzel (Seattle):** Yeah.

**Steve Krenzel (Seattle):** And those are kind of vetted and...

**Steve Krenzel (Seattle):** High quality.

**Steve Krenzel (Seattle):** I mean, maybe those are the best ones to start with.

**Steve Krenzel (Seattle):** We have about 110 that are less vetted.

**Steve Krenzel (Seattle):** And we could give you that spreadsheet if you think that'd be useful.

**Bailey Seybolt:** Yeah, I mean, I think it makes sense to the ones that you've identified on these industry pages.

**Bailey Seybolt:** mean, industries, that's a focus for content as well.

**Bailey Seybolt:** Like, that's one of the sort of high priority lanes of content we have.

**Bailey Seybolt:** So I think it would make sense to match that lane of content to sort of the existing workflows that you have.

**Bailey Seybolt:** I'm also a fan of always kind of repurposing what you already have to kind of test and see how it works over kind of making you do a bunch of extra work.

**Bailey Seybolt:** You know, if we can test with what we've got and, like, move quickly, that's always kind of better, I think.

**Bailey Seybolt:** But I'm totally open to how, you know, you want to do it, too.

**Steve Krenzel (Seattle):** Given I idea.

**Steve Krenzel (Seattle):** Go.

**Steve Krenzel (Seattle):** No, yeah, I agree.

**Steve Krenzel (Seattle):** That sounds like the most expedient way to do this is to probably start with the ones on the industry's pages and then as we, you know, come up with more topics, Azam and I can try to get ahead of that and just get workflows in place that will align with that topic.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** And I mean, and we can look back at the, you know, the 10 articles or 15 articles that we've already created too.

**Bailey Seybolt:** And if these make more sense to put in there, we can always update those instead or, you know, as well.

**Steve Krenzel (Seattle):** It doesn't have to just be the ones for next week.

**Bailey Seybolt:** Jacob, this is probably a question for you in terms of, like, delivering these for testing in terms of process.

**Bailey Seybolt:** Like, what's the best way to sort of, for the Logic team to kind of, you know, deliver them?

**Bailey Seybolt:** What's the best way to kind of incorporate these into the existing pipeline?

**Bailey Seybolt:** Or is that more of a engineering question that I can...

**Jakub Rudnik:** Um, so my, my thought on this...

**Jakub Rudnik:** Is to, was to get the like library or list or whatever.

**Jakub Rudnik:** And we just did that.

**Jakub Rudnik:** We've got our, you know, small batch and there is a larger batch behind that, but like, let's start with the most vetted, agreed there.

**Jakub Rudnik:** And so then let's take that, Bailey and I think with the content that we already have in motion right now and potentially going backwards, like identify some from these industry pages that do work within that content.

**Jakub Rudnik:** And like, what would it take for us to, to do this manually without like the engineering team behind?

**Jakub Rudnik:** So we identify like this document or workflow belongs right here in this section.

**Jakub Rudnik:** This blog is this type, whether that's like a product listicle, probably not like the best use or it's a, or top of funnel educational.

**Jakub Rudnik:** And then it fits in this section.

**Jakub Rudnik:** Like the example, I think we looked at last week was like, it had three examples of three different industries and each of those would be a really logical place.

**Jakub Rudnik:** So it's like, okay, example section three H3 is below that.

**Jakub Rudnik:** And then one document per H3.

**Jakub Rudnik:** If it's like, that's probably oversimplifying it.

**Jakub Rudnik:** you would do it, but like if you or the content producer is like, here's the section that triggers the document going in, then how does that actually get done?

**Jakub Rudnik:** That's probably just, I think it's just HTML embed, right?

**Jakub Rudnik:** And so then we identify like section, how we picked the document and then where we placed it.

**Jakub Rudnik:** And if we do that, I don't know how many times would be necessary, but basically like write a very short version of that, then engineering can build like the system.

**Jakub Rudnik:** To do that, but I think that like we need to know where those belong and how that fits into the content from like your editorial perspective, then engineering can, so I don't, does, is that answering the question like that's, that's my belief is yes, and do it that way.

**Jakub Rudnik:** And then too, as we talked through like today, I'm not sure exactly how they'll build up, but like if we document and show Kirkland, like, here's what we're thinking, here's what we have, right?

**Jakub Rudnik:** Like here's library, here's the places that they go in and the types of content, then.

**Jakub Rudnik:** I the automation will make more sense and we'll get a better product at the other end when we've kind of had it.

**Steve Krenzel (Seattle):** Would it be helpful if I share my screen real quick to show you how we were thinking of embedding?

**Steve Krenzel (Seattle):** might be useful context to have.

**Steve Krenzel (Seattle):** Cool.

**Steve Krenzel (Seattle):** Let from a hopefully this makes the integration really easy.

**Steve Krenzel (Seattle):** All we're doing is putting special strings basically in the in the content.

**Steve Krenzel (Seattle):** So they give its logic workflow.

**Steve Krenzel (Seattle):** Some call this the slug, but like the slug of the of the workflow.

**Steve Krenzel (Seattle):** And then this is just a caption and like this is this is just a draft that I've got a bunch of sprinkled in here this content.

**Steve Krenzel (Seattle):** Now when I view this over here, ignore some of the formatting, you know, oddities.

**Steve Krenzel (Seattle):** But this is automatic.

**Steve Krenzel (Seattle):** It gets embedded based on the slug, and then you can click into it, you can interact with it, but then everywhere that kind of special string is in StoryBlock, we insert a different workflow.

**Steve Krenzel (Seattle):** so that's kind of, so in theory, if we can just have the content generate these with references to really, to real slugs, it'll just kind of just work.

**Jakub Rudnik:** Yeah, that, you know, I'm not the engineer that is, you know, but that looks really logical, and that it's got a repeatable process, plus Bailey, it looks like how we have, well, you have to do like CTAs in Webflow, for instance, like it looks very similar to that.

**Jakub Rudnik:** So it should be something that, when they understand that logic and see if it looks like it's been built, you know, no way that will work.

**Jakub Rudnik:** So, yeah, we can show, you know, after we've done this a couple of times, just to get the editorial placement, how we feel, and I think bringing that to Kirkland or Stevie and the team and that.

**Jakub Rudnik:** It should make a lot of sense.

**Steve Krenzel (Seattle):** It should work for workflows.

**Jakub Rudnik:** That's sweet.

**Jakub Rudnik:** I'm really excited about this.

**Jakub Rudnik:** This is one of those things that, yeah, I was really pumped about thinking over the weekend and how it'll work and seeing like, okay, we'll have traffic and then we'll have really obvious ways for it to convert and show people your product.

**Steve Krenzel (Seattle):** Cool.

**Bailey Seybolt:** Then I guess the question is, do you have, in that full library that you have, what's the best way, I guess, to deliver?

**Bailey Seybolt:** Or kind of those use cases and their connections to those workflows?

**Bailey Seybolt:** Like, do you have access to that somewhere that you could share with me so we can start sort of pulling out some of those or highlighting the ones that seem like the most useful or, you know, highest?

**Steve Krenzel (Seattle):** Yeah, we have.

**Steve Krenzel (Seattle):** I mean, the immediate link that comes to mind, we don't have this publicly linked anywhere, but it's just like logic writing slash workflows.

**Steve Krenzel (Seattle):** Because you'll see most of these are marked as in draft, even some of the ones that aren't.

**Steve Krenzel (Seattle):** Mark this draft, we still don't publicly link to, because we kind of created a huge quantity of workflows that we thought might be interesting, and now we just need to go through and filter down to the highest quality of them.

**Steve Krenzel (Seattle):** But this is kind of the large set that we're working with.

**Steve Krenzel (Seattle):** Yeah, okay.

**Steve Krenzel (Seattle):** This isn't the easiest to digest.

**Steve Krenzel (Seattle):** We also have a spreadsheet that I can give you that is just kind of a big list of the workflows, too.

**Steve Krenzel (Seattle):** But this is kind of the list.

**Bailey Seybolt:** No, this is great.

**Bailey Seybolt:** mean, think that sharing the spreadsheet would be useful, too, but I think this is great.

**Steve Krenzel (Seattle):** Cool.

**Steve Krenzel (Seattle):** I think the spreadsheet's a little out of date with this list, so I'll just sync them up and then share that with you.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** That sounds great.

**Bailey Seybolt:** And then I will take a look at them, and then for the content we're working on this week and also for next week, I'll prioritize articles that kind of match, hopefully, some of the higher priority.

**Bailey Seybolt:** Let's go.

**Bailey Seybolt:** let

**Bailey Seybolt:** Workflows that we've got on the list, so we can try it out.

**Steve Krenzel (Seattle):** Fun.

**Steve Krenzel (Seattle):** This is a small amount of data, but we had two, so we have a link on our site now to, like, book a 15-minute demo with a founder, and we got our first two bookings through that, and one was for, like, marketing automation, and the other is in the logistics space and trucking, so just a fun data point to share.

**Bailey Seybolt:** That's exciting.

**Bailey Seybolt:** It's also interesting, because, actually, I updated our CTA in the blog post, so that it links to that instead of the sign-up, because that's where I was sending people, which seemed kind of too high intent for a lot of the content we're producing, so that's extra exciting to hear.

**Steve Krenzel (Seattle):** Yeah.

**Steve Krenzel (Seattle):** I was peeking at our Engage sessions on Looker, and that's looking pretty promising, so.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** All good signals.

**Steve Krenzel (Seattle):** Yeah.

**Bailey Seybolt:** All good.

**Bailey Seybolt:** Awesome.

**Bailey Seybolt:** So looking at, I think that's kind of everything I had in terms of to-dos for today.

**Bailey Seybolt:** Is there anything else that's on your mind, content-wise?

**Steve Krenzel (Seattle):** No, I don't think so.

**Jakub Rudnik:** Can I share or ask one question maybe of you, Bailey, but I'm sure we're all aligned and then have like one little thing I found.

**Jakub Rudnik:** The, let's just look at the Looker and the early traffic and there's like a lot of clusters, um, right?

**Jakub Rudnik:** We've got just a bunch and, um, as we're setting the categories for the blog and just, I would want us to align categories to clusters as best as possible.

**Jakub Rudnik:** And then that those probably also end up being used as like a tag for the workflows or something like to connect to the content.

**Jakub Rudnik:** I don't know if that one's as necessary, but just for reporting, I would imagine that you would want those.

**Jakub Rudnik:** So it might be...

**Jakub Rudnik:** Cluster might be like adding a different tag or something, but just something to think about with how many, it looks like a lot of, at least there, looked like a lot of clusters.

**Jakub Rudnik:** I'm trying to map over.

**Bailey Seybolt:** Yeah, that might make sense because I think the blog categories didn't entirely align with the clusters, that we sort of mapped them more closely to search intent.

**Bailey Seybolt:** Because I think the clusters had like, the topic clusters are there's like workflow and process automation and then automation for business users.

**Bailey Seybolt:** But there's enough overlap between those from a search intent perspective that I think it didn't totally make sense to tag them separately on the blog.

**Bailey Seybolt:** But we can go back and look at that as well.

**Jakub Rudnik:** Yeah, might be, this is, it was a little bit of a half-baked thought, but with one of our clients who's got like 500 pieces, having the tag slash categories from their blog mapping to...

**Jakub Rudnik:** Boo, the OS, like something that we're having to retroactively do.

**Jakub Rudnik:** So it's a pain, but also there's usefulness there.

**Jakub Rudnik:** So I don't know if this is like changing our clusters or if it's like adding a separate tag and just making sure we have that documented.

**Jakub Rudnik:** So I just want to put that on your radar before it got too far with content.

**Jakub Rudnik:** I mean, you can always like get a spreadsheet and update, but there's just some, the bigger it is, the harder it is to map.

**Bailey Seybolt:** Yeah, that's a good one.

**Bailey Seybolt:** I'll go back and take a look at them.

**Bailey Seybolt:** It may be just maybe splitting them out into more categories and mapping those back to the clusters or like creating more categories that like do a better job telling the story then rather than everything tagged automation.

**Jakub Rudnik:** Okay, then we can let me know it again.

**Bailey Seybolt:** Yeah, I'll take a look and I'll see if I can think of the best way to do it and then run it by you and see if you think it makes sense.

**Jakub Rudnik:** Okay, cool.

**Jakub Rudnik:** And then Steve, this is more for you and I don't know exactly where to put it.

**Jakub Rudnik:** Or where you all are and like testing different things, but I was just poking around and like the site and CTAs and went to the signup page.

**Jakub Rudnik:** Like through one of the workflows, I think it was like, okay, this is good.

**Jakub Rudnik:** this is a post that I've like bookmarked because I've had people done this a couple of clients.

**Jakub Rudnik:** And then I've heard people, you know, post on LinkedIn or talk about this type of tip on a podcast.

**Jakub Rudnik:** And just like very simple, like blurred view of the product behind the signup page has like seen big lifts.

**Jakub Rudnik:** I think this is like one very good, you know, experiment.

**Jakub Rudnik:** And maybe, I don't know, I don't know this person directly or like have their data, but I've seen similar type of thing.

**Jakub Rudnik:** So it's just, I want to try to like throw those things your way when I see them.

**Steve Krenzel (Seattle):** I really appreciate that.

**Jakub Rudnik:** So I will try to document these like more formally, but I just was like, oh, this is here and I don't want to.

**Steve Krenzel (Seattle):** This is great.

**Steve Krenzel (Seattle):** And it's incredibly timely because right now we're about to overhaul our signup flow because right now we offload to WorkOS.

**Steve Krenzel (Seattle):** we just kind of take you to a WorkOS owned like signup page.

**Steve Krenzel (Seattle):** And we don't own any of the Chrome there other than like our logo.

**Steve Krenzel (Seattle):** But we want to bring that back.

**Steve Krenzel (Seattle):** Onto our property and we're not really sure what the best way to do that.

**Steve Krenzel (Seattle):** And this, this is like incredibly timely cause this.

**Jakub Rudnik:** Well, good.

**Jakub Rudnik:** I'm glad to be connected to those.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** Let me know.

**Jakub Rudnik:** I would love to see like what else you're doing.

**Jakub Rudnik:** Feel free to like, you know, loop me in or ping, whatever.

**Jakub Rudnik:** Like there's always one.

**Jakub Rudnik:** I'd like to see it in two.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** Might have ideas.

**Jakub Rudnik:** Again, scribe was like very PLG focused and spent so much like they had a really great, we had a great, um, growth team.

**Jakub Rudnik:** And so I was like working side by side with them.

**Jakub Rudnik:** So often like more watching what they're doing, but there's, I think a lot that can be learned from like their flows over here and like how, again, embedding the product essentially into content.

**Jakub Rudnik:** I know that that's not your only, um, signup flow, but there's just a lot, I think that can be connected.

**Jakub Rudnik:** So, um, feel free to let me in and, you know, it helps us to understand where we're sending people to on the CTS.

**Steve Krenzel (Seattle):** Cool.

**Steve Krenzel (Seattle):** Um, backing up one, one notch.

**Steve Krenzel (Seattle):** I did have some questions.

**Steve Krenzel (Seattle):** When you, you were talking about clusters and seeing, seeing.

**Steve Krenzel (Seattle):** Clusters of some sort, when you're referring to clusters, what are you, can you say more about that?

**Steve Krenzel (Seattle):** Is that like clustered content, clusters of users coming in, or like, yeah.

**Jakub Rudnik:** Cluster, more like topic of, like umbrella topics of within your blog or the content that we're producing.

**Jakub Rudnik:** So we have, let me pull up the right OS here.

**Jakub Rudnik:** I have that.

**Jakub Rudnik:** Uh, Bailey, do you have the link to the content OS?

**Jakub Rudnik:** It's not popping up for me.

**Jakub Rudnik:** Thank you.

**Jakub Rudnik:** I can share.

**Jakub Rudnik:** But yeah, so like topic clusters in content, yeah.

**Jakub Rudnik:** Yeah, umbrella topics is probably the best way to put that.

**Jakub Rudnik:** And then, so we, um, so like workflow and process automation, automation for business.

**Jakub Rudnik:** There's, like, if, you you've done a little bit with content, so, like, kind of, like, in the hub and spoke model, like, that would be called a cluster more on, like, the execution standpoint, like, how HubSpot used to do this, if you're familiar.

**Jakub Rudnik:** But I think it's, like, we don't think of it quite exactly that way.

**Jakub Rudnik:** But, again, like, thematically, what are we, what are the personas or the topics and then all the content in individual assignments that fall underneath of those.

**Jakub Rudnik:** And so that, to me, your blog categories are doing the same purposes just for, like, the UX when someone's on that blog and then for all those tags and how it would be surfaced.

**Jakub Rudnik:** So I would, there's definitely reasons that those two wouldn't match up one for one, but ultimately we want to align those as closely as possible, I think.

**Steve Krenzel (Seattle):** Got it.

**Steve Krenzel (Seattle):** And does this list of topic clusters somehow map into Looker in any way or were you just kind of comparing, like, going back and forth and comparing?

**Jakub Rudnik:** Yeah, those do...

**Jakub Rudnik:** That's why I wanted to double check in was, I just seen this and hadn't mapped over to the OS, but those should be the cohorts.

**Jakub Rudnik:** And that's where I'm not, maybe this is like something that is just set up differently, but if we have four clusters, we have all these different cohorts.

**Jakub Rudnik:** Maybe cohorts are just mapped incorrectly, we have to work with the data team, but with the amount of content we have to have this many cohorts, like seemed off.

**Jakub Rudnik:** So I would want to see those at like, you know, the individual clusters so we can see which ones are performing best, you know, first with impressions of the traffic and ultimately like conversions, but we would want to see where that traffic's going.

**Jakub Rudnik:** So to me, actually, now that I'm getting the OS, I think it's slightly different where the clusters or the cohorts aren't the clusters, there's some other tag.

**Jakub Rudnik:** Does that make sense, Bailey?

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** I'm getting lost in my own words.

**Bailey Seybolt:** That wasn't.

**Jakub Rudnik:** Like, do you get it?

**Jakub Rudnik:** It's more of, like, did I explain that well, just to be clear?

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** Because if we have four clusters, each of those should be a cohort.

**Jakub Rudnik:** So somewhere on the back end, we have to reconnect those.

**Bailey Seybolt:** Yeah, it looks like there's, like, a duplication or something.

**Bailey Seybolt:** I'm not sure.

**Bailey Seybolt:** I can take a look and see when Ada set this up, what happened there.

**Jakub Rudnik:** Okay.

**Jakub Rudnik:** But, yeah, so then let's just map that back.

**Jakub Rudnik:** But then for you, Steve, you should be able to come in as we see this traffic growing and see, like, a third of our traffic's going to this cluster, a third over here.

**Jakub Rudnik:** And then we can double-click and look at the individual articles and see where that is.

**Jakub Rudnik:** But from a longer-term strategic level, it's, like, what – there's a couple things it'll tell us.

**Jakub Rudnik:** It's, like, what has the most traction with Google?

**Jakub Rudnik:** Like, if we publish 25 articles of all four of these clusters, like, where is Google showing us that we have signals and authority?

**Jakub Rudnik:** And then – and, like, is there the volume there?

**Jakub Rudnik:** There's a – and for us, it's, like, do we need to double-click because something isn't working?

**Jakub Rudnik:** Do we need to do

**Jakub Rudnik:** More because something's really working and others aren't.

**Jakub Rudnik:** So I think there's kind of like a decision tree that we can get off of those, but that's where the high-level clusters help us at least to see when we can come into the individual URLs.

**Steve Krenzel (Seattle):** Okay, cool.

**Steve Krenzel (Seattle):** This is helpful.

**Jakub Rudnik:** Thank you.

**Jakub Rudnik:** So we'll remap that.

**Jakub Rudnik:** Yeah, Bailey, I have to see where they're mapping, but it looks like maybe it's just like to the URL level rather than the cohort.

**Bailey Seybolt:** Yeah.

**Jakub Rudnik:** And I'll look at the log categories, too, so we can better align them with that for tracking.

**Jakub Rudnik:** Those, yeah, and those may be actually set up pretty closely, but I identified something with the incorrect.

**Jakub Rudnik:** That's a problem.

**Jakub Rudnik:** Okay, sorry.

**Jakub Rudnik:** Took over a lot there.

**Jakub Rudnik:** Thank you.

**Bailey Seybolt:** Oh, that's great.

**Bailey Seybolt:** Yeah, Steve, was there anything else that you wanted to add?

**Steve Krenzel (Seattle):** No, I think that's everything.

**Steve Krenzel (Seattle):** The action items I have get you a spreadsheet of the workflows.

**Steve Krenzel (Seattle):** And we'll ship the embedded workflow.

**Steve Krenzel (Seattle):** Thank

**Steve Krenzel (Seattle):** So we can actually start embedding.

**Bailey Seybolt:** Yeah, that's perfect.

**Bailey Seybolt:** And I will take a look at the cohorts and see what needs to be updated, too, for me.

**Steve Krenzel (Seattle):** Great.

**Jakub Rudnik:** Thank you, guys.

**Bailey Seybolt:** All right.

**Jakub Rudnik:** Thanks, everyone.

**Jakub Rudnik:** Bye.
