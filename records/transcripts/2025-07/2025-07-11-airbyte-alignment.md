# Airbyte Alignment

<metadata>
date: 2025-07-11
time: 20:00 UTC
duration: 28 minutes
organizer: daniel@growthxlabs.com
participants: Daniel Lopes, Marcel Santilli, Kirkland Gee, George Haikal, Ben Church
fathom_recording_id: 73734917
fathom_url: https://fathom.video/calls/349093692
share_url: https://fathom.video/share/sTcxgU6SJsiSbx2KYFLxNgzw1s_syjFK
source: fathom
enriched_on: 2026-03-03 12:34 UTC
</metadata>

---

## Summary

GrowthX aligned on Airbyte's content refresh sprint execution — targeting 100 article refreshes per week starting early next week once the Webflow publishing workflow is finalized. A critical issue emerged: the refresh AI is pulling incorrect statistics despite instructions to exclude them, which Kirkland will address by adding a fact-checker to the workflow. Beyond Airbyte, the team discussed emerging client demand for goal-tracking and performance reporting (George showcased a tool built for AugmentCode), plus fundamental infrastructure challenges with Google Search Console API limits for large websites that will require BigQuery integration.

---

## Context

This was an internal GrowthX team alignment meeting on the Airbyte engagement — a major client in the data integration and open-source tools space. Airbyte is an existing client expecting a sprint of content refreshes (updating 50-100+ articles weekly for their engineering resources) before moving into net-new content and special projects. The meeting included GrowthX leadership (Daniel Lopes), the account lead managing client communication (George Haikal), the engineer building the publishing infrastructure (Ben Church), and the SEO/technical architect overseeing the refresh workflow (Kirkland Gee). Daniel led the discussion to unblock next steps after some delays and ensure everyone understood the execution plan and dependencies.

---

## Relevance

**To GrowthX Delivery:**
- Refresh workflows are becoming a high-volume delivery model. This meeting established a target of 100 article refreshes per week, which will require scalability testing and process refinement.
- AI-driven refresh tools are hallucinating stats even when instructed not to — Kirkland investigating adding a fact-checker into the workflow as a potential fix to maintain quality at scale.
- Publishing workflow integration with Webflow (their CMS) is the critical blocker. Ben and Kirkland to finalize early next week; without this, the entire sprint stalls.
- Airtable intermediate step in the originally planned workflow was eliminated in favor of direct Atlas-to-Webflow publishing for speed.

**To GrowthX Business Development:**
- Client reporting needs emerging across all accounts — George demonstrated a custom goal-tracking tool built for AugmentCode that communicates long-term value of content work. This is becoming a baseline expectation for contract renewals.
- Airbyte engagement shows strong technical depth and scalability — team is solving for SEO data limitations, API constraints on large websites, and building custom reporting that could differentiate GrowthX's offering.
- Content inventory and automated tracking project (Daniel's side work) will eventually solve the reporting infrastructure challenge, but API limits from Google Search Console on large websites will require BigQuery integration for future clients.

**To CheckThat:**
- Discussion of LLM SEO benchmarking and ranking in "LLM search" surfaced lack of agreed-upon standards. This is a gap CheckThat could address.

---

## Overview

- Airbyte refresh workflow ready for execution; publishing workflow (Webflow integration) to be finalized by Ben and Kirkland early next week
- Critical issue: AI pulling incorrect statistics even when instructed not to; fact-checker addition being investigated as fix
- Target volume: 100 article refreshes per week starting next week; no Google Docs review required for initial sprint
- Client reporting emerging as standard requirement — George demonstrated goal-tracking tool for AugmentCode that communicates long-term content value
- Google Search Console API limits (50k rows/day) creating barriers for large-site reporting; requires BigQuery integration for future implementation

---

## Key Topics

### Airbyte Refresh Workflow Status

  - Publishing workflow to be finalized with Ben and Nem early next week
  - Current issue: AI pulling incorrect stats even when instructed not to
  - Kirkland to investigate adding fact-checker to refresher grid as potential fix
  - Initial sprint focus: Get content refreshed quickly, perfect quality less critical for now

### Airbyte Content Volume and Timeline

  - Target: 100 article refreshes per week
  - Next week's goal: \~50 articles (depending on when publishing is unblocked)
  - No Google Docs review for initial refresh sprint; direct publishing from Atlas

### SEO Tracking and Reporting

  - SEOtesting.com suggested, but may be unnecessary overhead
  - Alternative: Custom view in Data Studio/Looker Studio with regex filtering
  - Challenges with Google Search Console API limits for larger websites discussed
  - Potential solution: Focus on subfolder-level metrics for more comprehensive view

### Client Reporting Needs

  - Increasing demand for in-depth reporting across clients
  - George showcased a simple goal-tracking tool created for AugmentCode
  - Tool helps communicate long-term value and set expectations
  - Team considering integrating similar analytics view into Atlas

---

## Action Items

- **Kirkland Gee (GrowthX)**: Investigate the refresh workflow stats issue by adding fact-checker to the refresher grid; if that doesn't fix it, debug the workflow itself to determine if there's a deeper issue with the AI model pulling incorrect data.
- **Ben Church (GrowthX)**: Finalize the Webflow publishing workflow with Nem (Airbyte's content manager) early next week; test and confirm it works for updating live posts correctly.
- **Daniel Lopes (GrowthX)**: Create a ticket for Kirkland to review the refresh pipeline artifacts and personas to ensure they're correct for the Airbyte engineering resource content.
- **George Haikal (GrowthX)**: Refine the goal-tracking tool built for AugmentCode and share it with the team for evaluation of potential Atlas integration; continue documenting client reporting requirements across accounts.
- **Team**: Further develop scalable client reporting infrastructure to address emerging demand; evaluate SEOtesting.com vs. Data Studio/Looker Studio approach for Airbyte and future clients.

---

## Transcript
**George Haikal:** Hello, hello.

**George Haikal:** How's it going?

**Daniel Lopes:** Hey.

**Daniel Lopes:** It's been a while.

**Daniel Lopes:** I haven't been in the office much lately.

**George Haikal:** I know, man.

**George Haikal:** Like always, we've missed you when you're not here, but honestly, it's been a crazy week of recording and podcasts and pretty hectic in the office.

**George Haikal:** So it's probably good if you were trying to get a bunch done that you weren't in.

**Daniel Lopes:** Oh, yeah.

**Daniel Lopes:** Ben, nice to see you.

**Ben Church:** Nice to you again.

**Ben Church:** Back-to-back days.

**Daniel Lopes:** George, nice to see you in person.

**Ben Church:** See you in person.

**Ben Church:** Yeah.

**Daniel Lopes:** I think we're waiting for Kirk right now.

**Ben Church:** Give it like two, three more years, won't even know if there's a third dimension to anybody.

**George Haikal:** I know, right?

**Daniel Lopes:** Two minutes.

**Daniel Lopes:** I just need to run to the restroom real quick.

**Daniel Lopes:** I had back-to-back meetings.

**George Haikal:** I didn't have time.

**Daniel Lopes:** No problem.

**George Haikal:** What's up, Kirkland?

**Kirkland Gee:** How are you guys?

**Kirkland Gee:** How's your week?

**Ben Church:** Good.

**George Haikal:** Good, man.

**George Haikal:** This morning, I was in the office, the only one there, we were hosting Hypergrowth, one of our clients.

**George Haikal:** Um, because they were running a podcast, and their guest was the founder of Bolt, who was another client of ours, that churned.

**Kirkland Gee:** Yeah, awkward, okay.

**George Haikal:** Except he, like, he knew about us, but he was never involved in the projects.

**Kirkland Gee:** Interesting.

**George Haikal:** And the person who was, the person who was, was one of the main issues with the account.

**George Haikal:** And so, it was cool to meet him, he was super cool guy, and, like, we knew more about his users than he did.

**George Haikal:** But, uh, cause...

**George Haikal:** Yeah.

**George Haikal:** We went in with their team and did user analysis prompt.

**George Haikal:** We like analyzed all the sessions of the prompts that they were using in the app.

**George Haikal:** And so it was pretty, it was pretty funny, honestly.

**Kirkland Gee:** That's, that's actually so funny.

**George Haikal:** Yeah.

**George Haikal:** I got to tell Daniel that because he's the one who did most of that work.

**Kirkland Gee:** Yeah.

**George Haikal:** Yeah, Daniel, was just telling them, I caught up with Eric, the CEO of Bolt today.

**George Haikal:** He was in the office recording a podcast with the hyper growth guys.

**George Haikal:** And he knew about us, but he didn't, he like, it was clear.

**George Haikal:** He didn't, wasn't plugged into any of the work we're actually doing.

**George Haikal:** And we knew more about his users, what I could speak to when I was talking to him than like he did, essentially.

**Daniel Lopes:** Gosh.

**Daniel Lopes:** Yeah.

**George Haikal:** Because of all the stuff that you did.

**George Haikal:** So it's pretty funny.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** That's such a big challenge for us.

**Daniel Lopes:** We'll be like, that's the conversation I was having with like Bridget, Marcel.

**Daniel Lopes:** And everybody in the morning was, we have multiple layers of things to figure out, the Brio PMF, and figuring out the ICP is a multi-layered thing.

**Daniel Lopes:** And at a company like that, fast-growing, if we don't have access to the CEO, and that probably doesn't fit the long term.

**Daniel Lopes:** Oh, thank you.

**Daniel Lopes:** Yeah, anyway, the Airbyte stuff, George, Ben has been working on the publishing stuff, like we can publish stuff in Webflow, in their Webflow.

**Daniel Lopes:** I know Marcel moved things around to be easier to execute on the things that they're expecting, so it's more of a refresher play now than anything else.

**Daniel Lopes:** Ben has a ton of context on what is the kind of pages and why these things exist around their business.

**Daniel Lopes:** Kirkland has a lot of context on how we...

**Daniel Lopes:** Can do programmatic stuff.

**Daniel Lopes:** I just pulled everybody together to help us think about this because we will probably transition Ben out of the client ops work next week and client ops team would take over and helping like set up the proper pipeline and like integrate some of the web flow stuff and does that make sense?

**Daniel Lopes:** Do you have like more content?

**Daniel Lopes:** I don't know.

**Daniel Lopes:** I saw this document that was added to it.

**George Haikal:** Was that you that added or is it Marcel?

**George Haikal:** Yeah, I made the document.

**George Haikal:** Just like a little bit of context, which I mean, I think the only other thing I have to add is like, it's pretty much what that document said.

**George Haikal:** It's the first month essentially.

**George Haikal:** just want to test how much volume we can do on the refreshes and like as much as possible and try to impress them.

**George Haikal:** And I just met with them today, who's the CM that will be churning those out on how is using the refresh workflow.

**George Haikal:** And so.

**George Haikal:** Like, we have a baseline.

**George Haikal:** know we can get stuff out if the publishing is unblocked starting next week.

**George Haikal:** And Ben, he said you and him are meeting, like, early next week to run through the publishing, which is good.

**George Haikal:** There's just a small nuance right now in the refresher workflow that we can talk about that's giving him some trouble.

**George Haikal:** But that's the context I have so far to add.

**Ben Church:** So, like, as I understand, because there's, like, last week, there was a few things that were, like, mentioned, but never known, like, where in the priority it was.

**Ben Church:** So, as I understand, is, like, refresh is the main thing.

**Ben Church:** What was talked about is there's, like, that gong call thing.

**Ben Church:** That's a different thing.

**Ben Church:** That's, like, on the back burner until, like, it's fleshed out more.

**Ben Church:** There is net new content.

**Ben Church:** It sounds like that's also on the back burner.

**Ben Church:** It's just all refreshes.

**Ben Church:** Yeah, starting next week, me and him, my goal is, like, let's get that publish workflow, like, in, and then me and him just.

**Ben Church:** Sit, go through it.

**Ben Church:** If it works, awesome.

**Ben Church:** If it doesn't, we fix it.

**Ben Church:** Keep going until it works exactly as Nem needs it.

**Ben Church:** The piece of the refresh workflow that I'm not sure about was at one point someone, I think it might have been Nem, mentioned that Mario was talking about ranking higher in the LLM SEO stuff, whereas our refresh workflow has got an SEO score kind of checker.

**Ben Church:** It doesn't have anything for LLM stuff.

**Ben Church:** Is that a problem at all, or are we fine?

**Ben Church:** I'm just going traditional benchmarking on the SEO surfer.

**Kirkland Gee:** If you've got a benchmark for LLM search, I'm happy to do it.

**Kirkland Gee:** Everyone's asking.

**Kirkland Gee:** That's not a thing.

**Kirkland Gee:** Everybody's asking.

**Ben Church:** Yeah.

**Ben Church:** All right.

**Ben Church:** All right.

**Kirkland Gee:** At least there's not any agreed upon standard for how we would go about that.

**Kirkland Gee:** A lot of people have a lot of opinions.

**Kirkland Gee:** But, you know, cool.

**Ben Church:** So it sounds like publish is the thing missing from the refresher workflow.

**Ben Church:** And because we're refreshing all the engineering resources.

**Ben Church:** Yeah.

**Daniel Lopes:** I would also add, it would be nice to get the two of you, you Kirkland and you Ben, to check the pipeline, to check the artifacts, to check if the personas are correct.

**Daniel Lopes:** Because you're like, Kirkland knows what is possible to the maximum detail of the whole systems, plus knows everything about SEO to the best that we can.

**Kirkland Gee:** Knows everything is such a, that's so overstating it, but I'll take it.

**Daniel Lopes:** And Ben knows the personas, personas and everything for that client.

**Daniel Lopes:** So we might have to create like a custom artifact for like making sure, like for, just to give a little bit of context, like biological, for example, has all the things to fact check at the end.

**Daniel Lopes:** So fact checking is more like a custom workflow with the right persona in mind, making sure that the wording is correct.

**Daniel Lopes:** If this one is super technical, and we are refreshing by adding docs or something, I don't know what's the need there, or we're adding code snippets, then we might be like, oh, shoot, how do we do this?

**Daniel Lopes:** So just having you guys look at the refresh and see if it would refresh actually with stuff that programmers, or whoever's the persona that they're optimizing this for, because it's a technical product.

**Daniel Lopes:** So, yeah.

**George Haikal:** Yeah, that's something we talked about with Mario, but it sounded like it was a more down-the-line requirement when volume really, really increases.

**George Haikal:** Like what I heard from him, and we just sent the SoW to him, like the contract to get signed, is we showed him the refresh workflow live, and all it really did was change the formatting, add a little bit of new content.

**George Haikal:** And move the picture.

**George Haikal:** He was happy, and he loved it.

**George Haikal:** The issue that Nem's running into is it keeps pulling stats even when he instructs it not to.

**George Haikal:** And the links are all good.

**George Haikal:** The links are two reliable sources, but the stats that are actually showing up in the new article aren't the numbers that are in the linked article.

**George Haikal:** And they're actually incorrect.

**George Haikal:** And he said that's happening constantly.

**George Haikal:** And he's seen it in pretty much all of the refreshes that he's done.

**George Haikal:** And so he's had to manually go in and adjust it even when he gives it like polishing instructions to not show the statistics.

**George Haikal:** So if there's a way to get it to where it's just the links and you don't actually show stats in the new published article, I think that's fine.

**George Haikal:** Because Mario literally said there's so many pages that he's not even that concerned about perfect quality content right now.

**George Haikal:** It's just getting it refreshed and getting it to a better baseline than where it was before.

**George Haikal:** And then down the road, adding that expert artifact that can fact-check at the end and make it more high quality for net new stuff is something we talked about down the road.

**George Haikal:** But to me, it sounded like the priority was more fixing that initial thing.

**Kirkland Gee:** I'll take a look at that.

**Kirkland Gee:** I mean, we can just start by adding our fact checker into their refresher grid just after the refresh, like just run it and see if that fixes it.

**Kirkland Gee:** That might just like do it.

**Kirkland Gee:** And then if not, I can look at, okay, do we need to do something with the refresher workflow because there's something weird going on?

**Kirkland Gee:** Maybe it's using, I'm actually curious what model.

**Daniel Lopes:** I think it's for all.

**Kirkland Gee:** Yeah, it's on it.

**Kirkland Gee:** So it's for, yeah, the actual refresh is using Claude.

**Kirkland Gee:** So, okay, I made sure it wasn't like 3.5 or something, but it's on Sonic 4, so.

**Ben Church:** Okay.

**Ben Church:** I am just not going to look.

**Ben Church:** Calendar invite for Kirkland anyway, like the top of the week.

**Ben Church:** So just like, if you want to skip it, it's not necessary, don't do it, but we can always go through that artifact of the fine-tune code.

**Ben Church:** I can use my last little bit of airbite context for good use.

**Ben Church:** And then from that moment on, it'll just be like useless nodes in the brain until I'm like on my deathbed, I'm sure.

**Ben Church:** Cool, cool.

**Ben Church:** Okay, so that's pretty straightforward.

**Ben Church:** And then like after we get the refresh out, like what's the target for NEM again?

**Ben Church:** It's like 50 articles at the end of next week?

**George Haikal:** Next week, depending on what day in the week it gets out, that sounds about right.

**George Haikal:** But 100 a week is kind of what we were speaking to.

**George Haikal:** Okay.

**George Haikal:** And NEM said that wouldn't be a problem as long as publishing is unblocked.

**George Haikal:** And we went through it today.

**George Haikal:** Worst case, we just got to get the articles to a point where like no stats are mentioned at all for the first 100 of the first batch next week, just so we can get something out.

**George Haikal:** And then if it's like too complicated of an issue to solve in the next few days on your guys' end, we're completely unblocked outside of that publishing.

**Ben Church:** Okay, cool.

**Ben Church:** And then with the publishing, they're not doing the Google Docs review on these ones?

**Ben Church:** They're just sending it out?

**George Haikal:** Yes.

**George Haikal:** Yep.

**George Haikal:** Yep.

**George Haikal:** For this initial sprint of refreshes.

**Ben Church:** Cool.

**Ben Church:** Cool.

**Ben Church:** And then out of my own curiosity for Airbyte, the next statement of work, what item do you think it'll be?

**Ben Church:** Net new posts or gong call transcription stuff?

**Ben Church:** That's the one that I'm curious what they actually want for.

**Ben Church:** My brain can't help but ask like, what's up with that?

**George Haikal:** So the gong calls are more something we said we would experiment with and test and see how much capacity it would take to actually do.

**George Haikal:** So they're not expecting that in the statement of work.

**George Haikal:** The statement of work is this sprint refresh.

**George Haikal:** Getting to a volume of like 100 a week, the wording is much more broad in the SoW, and then the net new stuff.

**Ben Church:** Okay, cool.

**Ben Church:** And those Gong calls, if they do come up, is it for internal use or is it turning those into blog posts?

**George Haikal:** It would be, and he still needs to send us what an expected output looks like, but essentially it would be distilling the calls down to customer insights and then using those insights for something else.

**George Haikal:** But we would only work in the first part, which is distilling them down to whatever format they'd want.

**George Haikal:** And then that could be reused for any client of ours, and we could use that to inform artifacts.

**George Haikal:** That's kind of the way we were thinking through it in the simplest version of how we could approach it.

**Ben Church:** Cool, cool.

**Ben Church:** And then for the refresh stuff, that's my last question.

**Ben Church:** Nem is basically like, because he's the person as the content manager, he's the one that's like, this workflow works, I'm good, I'm unblocked, they're done.

**Ben Church:** Otherwise, if Nem's got problems, we've got problems.

**George Haikal:** If Nem's got problems, we definitely have problems.

**George Haikal:** Yeah, he's sharp, though, and he checks everything manually, and he understands the assignment.

**George Haikal:** He's ready to get going, and he's been on the account for a while, because obviously they've been an existing client prior to this new sprint.

**George Haikal:** So, yeah, he's good.

**Daniel Lopes:** Cool.

**George Haikal:** Cool.

**George Haikal:** that cover anything?

**George Haikal:** you guys need any more info?

**Daniel Lopes:** I don't think so.

**Daniel Lopes:** that's, like, for the strategy sprint ticket, it originally started pretty broad.

**Daniel Lopes:** Now it's, very specific, and, yeah.

**Daniel Lopes:** Do you, like, Kirkland, you got the only action item here that was not in the plan, in the ticket.

**Daniel Lopes:** Do you want me to add to the ticket, or, like, create a new ticket and sign it to you, or?

**Kirkland Gee:** Yeah, if you don't mind, just so I, because otherwise, come Monday, I'll forget.

**Daniel Lopes:** Yeah, sounds good.

**Kirkland Gee:** So Ben and I will look through all the artifacts and make sure all that stuff's good.

**Kirkland Gee:** And then on the publishing, I'm just like, to make sure this works, we're basically just updating the existing posts, not publishing new ones.

**Kirkland Gee:** So that's straightforward.

**Kirkland Gee:** Ben, you've done all of that. I know I looked at some of that stuff, but that should all be set. We're set to just update existing posts and not publish new ones?

**Ben Church:** Yeah, it should work for updating.

**Kirkland Gee:** I'm just testing that one out right now.

**Kirkland Gee:** Okay, cool.

**Ben Church:** I just remember, I remember there's like different, I think it's a different endpoint or like something's weird about updating a live post versus updating a draft post versus publishing a new post for like three different endpoints for Webflow for some reason.

**Kirkland Gee:** So I don't remember the exact details, but just, I want to make sure we don't forget about that.

**Ben Church:** Yeah, I'll choose one of theirs and just add a period.

**Kirkland Gee:** I'm sure they won't mind.

**Kirkland Gee:** Testing and stuff like that is the worst.

**Kirkland Gee:** You're testing a live post, and it's like, oh, God, what have I done?

**Kirkland Gee:** Okay.

**Kirkland Gee:** And then, yeah, I mean, that's straightforward.

**Kirkland Gee:** That's simple enough.

**Kirkland Gee:** Sorry, it's end of week, and my brain is completely fried.

**George Haikal:** You're preaching to the choir.

**George Haikal:** You're preaching to the choir.

**George Haikal:** Cool.

**George Haikal:** I'll get better at the tickets as well.

**George Haikal:** I saw that this meeting was on the calendar, and we only finalized the SOW.

**George Haikal:** And sent it out this morning.

**George Haikal:** So, like, the idea that I had, like, the fact checker and fixing the stats, like, that's just stuff Nem and I talked about in a meeting, so I didn't know.

**George Haikal:** I thought it would be more confusing to put that in a ticket, but it was just an idea in my head versus something that actually could be done.

**Daniel Lopes:** Yeah, no, it's good to talk about it.

**Kirkland Gee:** Only just looking at the doc you sent, there are a couple other questions, because we're all in the room.

**Kirkland Gee:** It says to batch around the pages through refresher, and then they want to dump them in Airtable.

**Kirkland Gee:** Do they still want to do that, or are we going to just publish them straight from Atlas?

**Kirkland Gee:** Do you know?

**George Haikal:** I'm checking the doc right now because I made this.

**Kirkland Gee:** Just because if they want us to put it in an air table and then get something and then put it back in Atlas and then publish it, that's kind of annoying.

**Kirkland Gee:** Especially if they're not reviewing it.

**Kirkland Gee:** I don't know if that's necessary.

**Kirkland Gee:** I think we're doing kind of full automated.

**Kirkland Gee:** Yeah, I think that sounds like a necessary step.

**George Haikal:** Yeah, no, that was just like said on the call that got pulled into it.

**Kirkland Gee:** yeah, yeah.

**Kirkland Gee:** And then they talked about using SEO testing.

**Kirkland Gee:** And then do we need to do anything with that?

**Kirkland Gee:** Does anyone need help setting up?

**George Haikal:** Is that what they're going to use?

**George Haikal:** No, that's going to be on our end.

**George Haikal:** NEM will, and I'll help NEM with that.

**Kirkland Gee:** And then last thing was under this prioritization method.

**Kirkland Gee:** Method, I think all of that's able to be done pretty manually in SEMrush.

**George Haikal:** Um...

**George Haikal:** Yeah, we already did that.

**George Haikal:** So I ran through that with Nem today.

**George Haikal:** There's an Airtable that has, like, the list of articles to be refreshed.

**Kirkland Gee:** Yep.

**Kirkland Gee:** Dope.

**Kirkland Gee:** Okay.

**Kirkland Gee:** But yeah, I think that's all good.

**George Haikal:** Is there a better way to, like, have you used SEOtesting.com?

**George Haikal:** Like, is there a better way to track all of this stuff?

**George Haikal:** Because we're going to have to report against it to them.

**Kirkland Gee:** I don't know.

**Kirkland Gee:** SEOtesting seems pretty unnecessary to me because you can just, like, set up a custom view in Data Studio and do a regex based on all the URLs and then just look at it period over period.

**Kirkland Gee:** If they want to use a tool like that, they can.

**Kirkland Gee:** But it just seems like a little bit of unnecessary overhead because we're not really, like, it's not like you're, I don't know, it does make it easier to annotate, right?

**Kirkland Gee:** So you know, like, what day these ones were done versus those ones.

**Kirkland Gee:** But you can also just, like I said, do a regex filter in GSC.

**George Haikal:** This is what Marcel said.

**George Haikal:** So we're definitely open to this. It wasn't what Airbyte requested — this is what Marcel said, so we're open to whatever's easiest.

**Kirkland Gee:** I mean, I don't know.

**Kirkland Gee:** Some people really, really love that tool.

**Kirkland Gee:** Essentially, all it is, like, is the same thing.

**Kirkland Gee:** Like, it's the same thing where you're just getting a period-over-period view.

**Kirkland Gee:** You just get to put little annotations on it to show when you made a change, right?

**Kirkland Gee:** Like, so if that's worth using a whole separate platform for this one thing, go for it.

**Kirkland Gee:** I just don't think you need to.

**Kirkland Gee:** Like, if we just make sure they have a Data Studio set up, or Looker Studio, whatever it's called now, you just, like I said, you can just do regex filtering.

**Kirkland Gee:** And those can be generated pretty easily.

**Kirkland Gee:** Like, you just throw all the URLs into Claude and ask it for a regex, and then throw it in there.

**Kirkland Gee:** The only thing is the amount of pages that we're doing.

**Kirkland Gee:** I don't even know if we're going to be able to do that.

**Kirkland Gee:** And with SEO testing, I don't know how they're going to do it with that many pages.

**Kirkland Gee:** You're probably going to want to just look at the subfolder as a whole, which is really a better way because we can get better numbers that way anyway — like, hey, we updated these hundred pages and the whole subfolder went up X clicks.

**Kirkland Gee:** I'm kind of just rambling out loud, but.

**George Haikal:** It's helpful, though.

**George Haikal:** We got to think about that more.

**Kirkland Gee:** I'll think about it more.

**Kirkland Gee:** Reporting and all of that stuff is like its own thing that we need to figure out.

**Kirkland Gee:** But that's a large task.

**Daniel Lopes:** Yeah, yeah.

**Daniel Lopes:** That is something that we're thinking about in the content inventory project.

**Daniel Lopes:** That would be tracking the project, tracking the website.

**Daniel Lopes:** then that would be like automatically checking the ones that would change.

**Daniel Lopes:** That's like a hard one.

**Kirkland Gee:** Yeah, it's between the GSC permissions are weird and whack.

**Kirkland Gee:** And then there's like the API limits on bigger websites are actually going to be a headache.

**Kirkland Gee:** There's a lot of annoying things.

**George Haikal:** Yeah, here, I'm going to pull something up.

**Daniel Lopes:** API limits?

**Daniel Lopes:** you mean the send and rush API limits?

**Kirkland Gee:** No, for Search Console, you can only get 50,000 rows of data per website per day.

**Kirkland Gee:** And so if you want URLs and queries by day for a bigger website like ClickUp, they have hundreds of thousands or millions of rows of data every single day.

**Kirkland Gee:** And so through the API, you actually can't get all of your data if you want to break them down by multiple properties.

**Kirkland Gee:** You have to just get like clicks for the entire website or clicks for each page, but not by query.

**Kirkland Gee:** And the most useful data for SEO is query data, right?

**Kirkland Gee:** Keyword data.

**Kirkland Gee:** And the only way to get around that is using their bulk data export into BigQuery out of Search Console.

**Kirkland Gee:** And it's just super annoying.

**Kirkland Gee:** And like we can't do that for clients.

**Kirkland Gee:** Anyways, me and Pedro were having a chat about it the other day.

**Kirkland Gee:** It's a weird problem to solve.

**Kirkland Gee:** I don't know what the right solution is, but at the end of the day, we don't necessarily need query data in our platform to report on whether a page is performing or not.

**Kirkland Gee:** So if we're just getting clicks and impressions by page by day, we're not really going to run into those issues unless the client has more than 50,000 pages all getting traffic, in which case we will run into that limit.

**Kirkland Gee:** And then backfilling data gets impossible at that point too, because you have to get today's data and you want yesterday's data, but you can't get more than 50K rows per day, regardless of when that data is from.

**Kirkland Gee:** Sorry, that's like a total rabbit hole.

**Kirkland Gee:** But it's a super annoying problem that all SEOs end up dealing with, because Google just wants you to pay to host all your SEO data in BigQuery.

**Ben Church:** It seems like later on we can scale up, though, like just take client's data, put it into our own BigQuery, and just move on there.

**Kirkland Gee:** Yeah, I know what the solution would be for backfilling, because that's the biggest thing to sort out. If we're pulling data through the API and we want page-level data backfilled for a bigger website, it gets kind of weird.

**Kirkland Gee:** We kind of just have to preserve historical data and limit the amount of detail that we're getting, right?

**Kirkland Gee:** Yeah.

**Daniel Lopes:** And then moving forward, we look at it forward-looking.

**Kirkland Gee:** But, George, like, I think, again, whether it's Data Studio or, like, at the end of the day, like, you can do this kind of thing just in Search Console if you just, if we have everything in a, like, consistent subfolder, which I think everything's in this, like, data engineering resources, most of it, although some of it's just in the blog, I guess.

**Kirkland Gee:** So, I don't know.

**George Haikal:** And like, it could be helpful to just sum up the entire subfolder and see the total.

**George Haikal:** But it's also helpful to see the individual results and understand what's important on each page so we could break that into a few different types of topics.

**George Haikal:** But yeah, I think that's like an, I'll think about it more.

**George Haikal:** It's an easier problem to solve.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** And like SEO testing, if it is worth it, then, you know, go for it.

**George Haikal:** Also, two more questions.

**George Haikal:** Well, this is not a question.

**George Haikal:** I just want to show you guys something because basically every client we have now is asking for more in-depth reporting. For example, AugmentCode is a custom Sprint client.

**George Haikal:** They want something for us to be able to track against what we're doing week by week.

**George Haikal:** And also something with goals set that he can show to his C-suite.

**George Haikal:** And so, okay, I froze.

**Daniel Lopes:** Let's wait for you guys to get back.

**George Haikal:** Did I get you guys back?

**Ben Church:** Yeah.

**George Haikal:** Cool.

**George Haikal:** So this is what I made quickly to show him the goals.

**George Haikal:** Basically, the inputs are pretty simple. The actions we're taking are pages we're going to be publishing per month, and it's going to take a while to get to the peak traffic number.

**George Haikal:** And then here's the peak traffic number.

**George Haikal:** This is a rough metric.

**George Haikal:** I'm going to fix it after this call.

**George Haikal:** I just wanted to publish it so I can show you guys.

**George Haikal:** And there's the brand lift percentage.

**George Haikal:** The other inputs are the average LTV, which we got right now from their paid stats, then the brand traffic multiple.

**George Haikal:** And then it's their investment, how much they're paying for this editorial lane.

**George Haikal:** And he liked this.

**George Haikal:** And so this helped us close the deal.

**George Haikal:** But it's still super early.

**George Haikal:** I mean, we talked about it yesterday.

**George Haikal:** So we made it very quickly.

**George Haikal:** But it's a very simple way to track and be able to communicate the value to a client easily.

**George Haikal:** And it's long-term value.

**Kirkland Gee:** This is so wild — we just vibe-coded this tool now, whereas I was doing this in spreadsheets before, you know what I mean?

**Kirkland Gee:** And like trying to figure out how to get the graphs to work.

**Kirkland Gee:** And now you can just be like, hey, Vercel, make this for me with all the parameters and it just works.

**George Haikal:** That's so dope.

**Daniel Lopes:** So yeah, it's kind of rough.

**George Haikal:** I mean, it's kind of rough seeing the numbers because these customer numbers aren't that high, but it's helpful for expectation setting.

**George Haikal:** And then it really communicates the long term value.

**George Haikal:** So this is what everyone's pretty much asking for.

**George Haikal:** And this isn't even including LLM referral stuff, which is like a black hole right now that everyone's asking for.

**George Haikal:** And I just got added to the Scrudge channel and I'm going to ask them, but any help there, anything you guys have done there would be amazing.

**George Haikal:** But I'm going to figure out how to start reporting more than just what Google Search Console provides.

**Daniel Lopes:** This is very aligned with what I was going to get shaped up for us building inside of Atlas as an analytics view.

**Kirkland Gee:** Because we should be able to, for an account, make a goal forecast and then find some way to track the actual traffic numbers onto that forecast.

**Kirkland Gee:** That's a super, everybody wants it, to your point, George.

**Kirkland Gee:** Literally every client is going to ask for something like this.

**Daniel Lopes:** Yeah, can you send me that, George?

**George Haikal:** Yeah, it still needs some editing, but I'll send the link in here.

**Daniel Lopes:** Cool.

**Daniel Lopes:** All right.

**Daniel Lopes:** I think we got everything covered, right?

**George Haikal:** Well, yeah, this was super helpful.

**George Haikal:** Thank you all.

**Daniel Lopes:** Thank you.

**Ben Church:** Of course.

**Daniel Lopes:** Have good weekend.

**Ben Church:** Have a weekend, guys.

**Ben Church:** Nice to see you all.

**Ben Church:** Bye-bye.
