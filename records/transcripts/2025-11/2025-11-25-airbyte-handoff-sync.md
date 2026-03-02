# Airbyte handoff sync

<metadata>
date: 2025-11-25
time: 16:30 UTC
duration: 33 minutes
organizer: Erik O'Brien
participants: Carrie Chowske, Joe Sovar, Erik O'Brien
fathom_recording_id: 104236308
fathom_url: https://fathom.video/calls/485423939
share_url: https://fathom.video/share/Z1wQSNyUdK13rD6Fjv5Tj-4srXDM6_pv
source: fathom
enriched_on: 2026-03-02 14:30 UTC
</metadata>

---

## Summary

Carrie Chowske handed off the Airbyte account to Erik O'Brien, confirming that Joe Sovar is fully capable of managing content production and has been effectively performing the role for weeks. The team walked through Airbyte's custom Airtable OS (which uses an "effort value" system to balance 25–100 pieces/week), reviewed critical blockers (a Webflow code-snippet bug preventing TLDR automation across ~600 pages), and outlined weekly reporting priorities (sessions, industry PSEO performance, and LLM traffic—particularly a surge in Claude referrals). Erik is inheriting a healthy account with 4 weeks of pre-approved content, a week-ahead delivery pipeline, and a satisfied client (Tanmay), with continued 1:1 support from Carrie available.

---

## Context

Airbyte is a data integration platform client generating significant GrowthX revenue through a 25–100 pieces/week content contract. The account is being handed from Carrie Chowske to Erik O'Brien as part of a planned transition, with Joe Sovar continuing as the content producer. Airbyte is currently in the middle of an internal "Sprint" (a strategic planning period), after which they expect to reassess their content strategy and potentially consolidate their three concurrent work streams with GrowthX. The relationship is healthy: Tanmay (the Airbyte stakeholder) is satisfied with output quality, Joe delivers consistently a week ahead of schedule, and the team has established clear processes and documented workflows via Airtable.

---

## Relevance

**To GrowthX Delivery:**
- Custom Airtable OS uses "effort value" formula to manage scope (target 80–90 units/week) — replicable template for managing variable-volume contracts that prevent 100-piece batches.
- Webflow auto-publish pipeline breaks code snippets (affecting TLDR rollout to ~600 pages) — engineering ticket needed; Joe proposing 50-piece/week limit for manual review if bug persists.
- PSEO production capped at ~30/week due to 1-hour research time per page — critical capacity constraint for content scaling.
- Kirkland (engineering) owns automation tickets for industry pages and use cases pipeline — coordination via tickets gets faster response than direct contact.

**To CheckThat:**
- Airbyte seeing surge in Claude referrals in last 3–4 months (ballooned significantly) — validates CheckThat value for tracking LLM traffic alongside traditional SEO.
- Tanmay (stakeholder) interested in scrunch prompts and AI visibility — team expected to set up Cloudflare tracking for agent traffic attribution.

**To GrowthX Business Development:**
- Account in excellent health: client satisfied, content delivered 1 week ahead, team delivering on scope. Renewal risk is low.
- Strategic reset coming post-Sprint (early 2026) — expansion opportunity if Airbyte consolidates work streams or scales. Current content sufficient through early January.
- Three concurrent work streams (editorial, PSEO, use cases/industry pages) — potential to pitch expansion once Sprint outcomes clarify.

---

## Overview

- **Joe is the content engine.** Joe Sovar is already managing content production, consistently delivering high-quality output a week ahead of schedule.
- **Airtable manages a complex scope.** The Airtable OS uses a custom "effort value" system to balance the 25–100 piece/week contract, as 100 pieces is unmanageable.
- **A critical Webflow bug blocks automation.** The auto-publish pipeline breaks code snippets in articles, forcing manual publishing and blocking the rollout of TLDRs to \~600 pages.
- **Reporting focuses on new initiatives.** Weekly reports highlight performance of the latest content (e.g., industry pages), sessions, and LLM traffic (notably, a recent surge from Claude).

---

## Key Topics

### Content Production & Airtable OS

  - **Production Status:** Joe Sovar manages all content creation, consistently delivering high-quality output a week ahead of schedule.
  - **Contract Scope:** The 25–100 pieces/week contract is managed via a custom "effort value" system in Airtable, as 100 pieces is unmanageable for manual review.
      - **Effort Value System:** Assigns a numerical value to each content type (e.g., Refresh = 1 unit) to track weekly output against the contract.
      - **Target:** 80–90 units/week for a balanced workload.
  - **Content Pipeline:** The "Priority Planning" view schedules content 4 weeks out.
      - **PSEO Pages:** A key focus. Production is limited to \~30/week due to the 1-hour research time per page.
      - **Editorial Pages:** Require review by Tanmay, who is fast and focuses on accuracy and formatting (e.g., images every 400 words).
      - **PSEO Pages:** Do not require client review; they are generated and published directly.
  - **Upcoming Work:**
      - **Use Cases Project:** A new content initiative.
          - **Design:** Awaiting a Webflow mockup from the design team for client approval.
          - **Pipeline:** Kirkland (who built the industry page pipeline) is assigned to automate content delivery.
      - **TLDR Rollout:** Adding TLDRs to \~600 existing pages. This is blocked by the Webflow bug.

### Webflow Automation Bug

  - **Problem:** The auto-publish pipeline breaks code snippets in articles.
  - **Impact:** This forces manual publishing and blocks the efficient rollout of TLDRs to \~600 pages.
  - **Mitigation:** Joe suggested a 50-piece/week limit to allow for manual review and code embedding if the bug persists.

### Reporting & Client Management

  - **Reporting Focus:** Weekly reports highlight performance of the latest content initiatives (e.g., industry pages) and overall traffic sessions.
  - **Client Input:** Tanmay often provides new keyword ideas, which can change the weekly content plan.
  - **Key Metrics:**
      - **LLM Referrals:** A high-interest topic. Traffic from Claude has seen a significant recent surge.
      - **TLDR Experiment:** An A/B test is concluding. Early data was positive, leading to the decision to roll out TLDRs site-wide.
  - **Looker Dashboard:**
      - **Performance:** The dashboard is slow and can break with timeframes \>2 months.
      - **Filters:** Exclude "non-growthx" and "batch refresh" content for accurate performance analysis.

### Future Strategy

  - **Current Strategy:** Sufficient content exists for the rest of the year and into early 2025.
  - **Strategic Reset:** A major strategy reset is expected in the new year, driven by the outcome of Airbyte's internal "Sprint."

---

## Action Items

**Joe Sovar (GrowthX)**
- Add remaining PSEO to reach 75; then produce/publish ~30 PSEO/wk
- Create new engineering ticket re: Webflow code-snippet embed; coordinate w/ Kirkland to close

**Erik O'Brien (GrowthX)**
- Review past weekly syncs; prep weekly reporting for Tanmay (sessions, industry PSEO, LLM referrals)

---

## Transcript
**Carrie Chowske:** Interesting times.

**Erik O'Brien:** Can you hear me okay?

**Carrie Chowske:** Johnny, put my headphones in.

**Carrie Chowske:** I have, like, background noise today.

**Carrie Chowske:** Hello?

**Carrie Chowske:** Hey, Joe.

**Erik O'Brien:** Oh, I can hear you fine.

**Erik O'Brien:** Okay.

**Carrie Chowske:** As long as it's not creating, like, a lot of noise, because I'm just being lazy about the headphones.

**Carrie Chowske:** I'm being lazy a lot this week.

**Carrie Chowske:** I'm not going to lie.

**Carrie Chowske:** Like, I'm just, anyway.

**Carrie Chowske:** Not in anything important, but just kind of, like, wiped out.

**Carrie Chowske:** So, the great news with Airbyte, I'm going to TLDR the whole meeting by saying that Joe knows what the hell he's doing, and he's been doing the job that he's going to be doing starting next week already, basically.

**Carrie Chowske:** He really hasn't needed my involvement.

**Carrie Chowske:** I do very, I've been doing very minimal edits for him.

**Carrie Chowske:** Tanmay has been very happy with the outputs we've been sending.

**Carrie Chowske:** Joe is a whiz, so you don't have to really worry about that part of it.

**Carrie Chowske:** The other part, for you, is going to be juggling of all the things that they have going on.

**Carrie Chowske:** So that's pretty much it.

**Carrie Chowske:** I wanted to show you what their content OS looks like, what you'll be working with. It's very organized, but also very customized to my workflow.

**Carrie Chowske:** So I just wanted to make sure that you were clear on it.

**Carrie Chowske:** And then I can record looms on anything that you're like, hey, could you maybe give me a keeper video on this one?

**Carrie Chowske:** And I'm happy to do it.

**Carrie Chowske:** If that's okay.

**Carrie Chowske:** And then you can ask me any, you can ask us any questions.

**Carrie Chowske:** that work?

**Erik O'Brien:** Yeah, absolutely.

**Carrie Chowske:** So anything that's in this priority planning view, which is somewhere down here, I have it in my favorites, this priority planning view here, is basically the next, what, four weeks worth of content already scheduled out.

**Carrie Chowske:** This has all already been approved by Tanmay.

**Carrie Chowske:** We're good to go on it, especially with all these PSEO ones or all those industry pages.

**Carrie Chowske:** And the only...

**Carrie Chowske:** The we spread them out is that they take an hour just for the researcher.

**Carrie Chowske:** So Joe can't really do many more than like 30 of them a week.

**Carrie Chowske:** Sorry, my computer just decided to reset itself.

**Carrie Chowske:** That was fun.

**Carrie Chowske:** The screen just flashed.

**Carrie Chowske:** That was fun.

**Carrie Chowske:** Anyway, so that's the only reason that we have them split up.

**Carrie Chowske:** Otherwise, we kind of we probably would have done them all together because they run pretty smoothly.

**Carrie Chowske:** There's no like there's nothing in there that needs to like be edited significantly.

**Carrie Chowske:** We take out like a couple instances of it trying to say that there's real time sync.

**Carrie Chowske:** That's about it.

**Carrie Chowske:** And then that'll be similar to what we end up doing for them for the use cases pages that we were talking about yesterday.

**Carrie Chowske:** So that's already been set up.

**Carrie Chowske:** But anyway, so there's like for all the different like content types, this controls a really this is you're going to be like, Carrie, you're doing the most all the time.

**Carrie Chowske:** Because I was trying their scope is really weird.

**Carrie Chowske:** I don't know if you've looked at their contract for this particular.

**Carrie Chowske:** So the contract for them says 25 to 100 pieces weekly.

**Carrie Chowske:** The only time we've ever done 100 is when we were batching a bunch of refreshes and we never want to do that again because it's not manageable for Joe to generate that much content in a week.

**Carrie Chowske:** Am I right?

**Carrie Chowske:** Especially since Joe had to do it four times.

**Carrie Chowske:** Four times?

**Carrie Chowske:** Is that how many?

**Carrie Chowske:** And we're now going to do it again.

**Joe Sovar:** And I was thinking now when we will be doing those TLDRs on all of these refreshes once again, maybe we can suggest like doing 50 a week.

**Joe Sovar:** That way I can check each one to make sure that everything is in place.

**Joe Sovar:** If it will be 100 a week, that might be a bit tricky regarding the context and the articles and the articles editorial for the regular pipeline.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** to give you an idea of what this does.

**Carrie Chowske:** So all of these different content types in here, which are all these guys, right?

**Carrie Chowske:** So there's net new.

**Carrie Chowske:** I don't use net new anymore.

**Carrie Chowske:** That was the old, like, just catch all.

**Carrie Chowske:** So I don't really use it, but I didn't delete it because there's some in there marked as that.

**Carrie Chowske:** But refresh, PSEO, editorial.

**Carrie Chowske:** Editorial PSEO, which I interpreted to mean more like, it's a little more formulaic, but it still requires a little more effort than your traditional PSEO.

**Carrie Chowske:** And then just adding the TLDRs.

**Carrie Chowske:** And so what I did with those was, there's a formula that calculates a number for this.

**Carrie Chowske:** And so, like, this, if you click on this, this actually does work.

**Carrie Chowske:** There's nothing in on deck right now, so I have to fix that one.

**Carrie Chowske:** But, like, once you, like, prioritize it for the weeks that it's in, it'll tell you if it's within scope because those are valued based on the amount of effort that they take.

**Carrie Chowske:** So it's a really easy way to see, like, if we're over delivering or, like, under delivering.

**Carrie Chowske:** I usually try to get this in the 80s or 90s if I can.

**Carrie Chowske:** But it, you know, it's as long as we're not going crazy because it kind of gives us a good balance of, because there's no way to deliver.

**Carrie Chowske:** A pieces a week.

**Carrie Chowske:** It just isn't possible.

**Carrie Chowske:** I just don't, I don't know how we would possibly do it.

**Carrie Chowske:** Like it just doesn't, there's not enough hours, but like if we're saying that those re a simple refresh or a simple thing, like a TLDR is like one unit, then that's kind of how I calculated the rest of them.

**Carrie Chowske:** Does that make sense?

**Carrie Chowske:** You can use this or not saying, but like, this is totally, once you're there, it's just how I did it to make it work for my, my brain.

**Carrie Chowske:** So it's all based on like how they're prioritized.

**Carrie Chowske:** And then there's like a formula.

**Carrie Chowske:** I don't know if it's in this view yeah.

**Carrie Chowske:** There's a formula here that calculates the value of it based on what that is.

**Carrie Chowske:** And so whatever you have in here, it's adding all that up and going, oh yeah, it's less than a hundred.

**Carrie Chowske:** That's fine.

**Carrie Chowske:** That's all it's doing.

**Carrie Chowske:** It's all it is.

**Carrie Chowske:** It's really simple, but then I tend to do math every week.

**Carrie Chowske:** And then these are weird because the way that I set this up initially, I probably would have done it differently had I had a different way, but it's current week and then next week and then up next.

**Carrie Chowske:** And then there's an on deck that I don't have anything in there right now for.

**Carrie Chowske:** I need to move stuff around, but like what I.

**Carrie Chowske:** Normally we'll do because I have automation set to kick this over on the overnights over the weekend so that there's not stuff.

**Carrie Chowske:** And Joe is probably going to do this himself, but I'm just letting you know how it works.

**Carrie Chowske:** So when you're looking at it, you know what's happening.

**Carrie Chowske:** But like all of these, I would change to on deck because they're actually up for two weeks out from now.

**Carrie Chowske:** And then I just need to put new ones in that up next category.

**Carrie Chowske:** And all that stuff, Joe, is in this, all the PSEO is in this one that's marked high.

**Joe Sovar:** Yeah, for those Airtable functions, I will probably have much more questions for you.

**Joe Sovar:** Yeah.

**Carrie Chowske:** Literally all I've been doing, Joe, this is like the easiest one in the world, is I've been going and like putting this in and like going, okay, I need 30 of these.

**Carrie Chowske:** Cool.

**Carrie Chowske:** I'm just going to copy that field and I'm going to grab 30 of these PSEO and we're going to go with those next.

**Carrie Chowske:** So where are we at 45, so I need to get to 75, but I already put one in there and I'm going to go like that.

**Carrie Chowske:** And then those are, that's all that's left is that next group.

**Carrie Chowske:** So you probably in the next, like, you know, couple of weeks are going to be able to finish those.

**Carrie Chowske:** But that's why I have it set up this way.

**Carrie Chowske:** It's kind of, you know, it's because they put them in alphabetical order that I have the weird tags for them.

**Carrie Chowske:** But anyway, that's it.

**Carrie Chowske:** Right now, what we're working on, and this is important for you, Erik.

**Carrie Chowske:** Like, we're working on right now is a list of articles that Tanmay gave us that are, he approved the title since they changed so much.

**Carrie Chowske:** Because they had, like, they changed their pricing plans back.

**Carrie Chowske:** They eliminated some products.

**Carrie Chowske:** They changed the focus of what they were writing about.

**Carrie Chowske:** But anyway, Joe knows all that part of it.

**Carrie Chowske:** But in terms of, like, what we're currently working on for them is a bunch of, anything that is actually marked as approved to start is good to work on.

**Carrie Chowske:** That's all stuff that Tanmay has approved and said this is good to go.

**Carrie Chowske:** And it's all in, it's all in this, somewhere in this priority planning, whether it's.

**Carrie Chowske:** And, you know, high, low, medium.

**Carrie Chowske:** I just, that's just, I've been moving stuff around within those as I, he gave me priorities to work on.

**Carrie Chowske:** So you can literally pull anything from there, Joe.

**Carrie Chowske:** There's nothing like, there's no reason that you can't pull any of those if they're marked proof to start.

**Carrie Chowske:** I cleaned all that up last week anyway, so.

**Carrie Chowske:** Okay, that is four weeks of content, right?

**Joe Sovar:** Mm-hmm.

**Joe Sovar:** Four weeks for it.

**Carrie Chowske:** Yeah, well, and I mean, we've already got this week done, so.

**Carrie Chowske:** Okay.

**Joe Sovar:** I need to do that before the holidays, basically.

**Joe Sovar:** So, yeah, in the next two and a half weeks.

**Joe Sovar:** Okay.

**Joe Sovar:** Yeah, yeah.

**Carrie Chowske:** And the only stuff that, that they review, Erik, is the editorial and the editorial PSEO.

**Carrie Chowske:** And they don't review the PSEO at all.

**Carrie Chowske:** We publish, we just generate, publish.

**Carrie Chowske:** That's it.

**Carrie Chowske:** They aren't reviewing that.

**Carrie Chowske:** That's Tanmay that does the review?

**Erik O'Brien:** Yeah, yeah.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** And he's really, he's really fast.

**Carrie Chowske:** Not very particular.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Which is nice for us.

**Carrie Chowske:** It does keep us moving.

**Carrie Chowske:** He's very much like he's looking for the formatting issues and like accuracy and relevance to his audience.

**Carrie Chowske:** He's like we're getting a decent enough output that he doesn't do like fine.

**Carrie Chowske:** He doesn't go through it like worried about little tiny commas and stuff.

**Carrie Chowske:** He doesn't do anything like that.

**Carrie Chowske:** He really is just checking to make sure that nothing's inaccurate and that, you know, we're we've got images every 400 words or something like that.

**Carrie Chowske:** I mean, they're honestly as particular as Tanmay is, he's actually very easygoing and very easy to please, which is which has been really great for me and Joe with as much as they've got going.

**Carrie Chowske:** So I have not set up any assignments for the use cases yet, but there is there is like a way to categorize those in here.

**Carrie Chowske:** So like they're all that we have like topic clusters, we have.

**Carrie Chowske:** Strategy, like how we've categorized the strategies.

**Carrie Chowske:** So like, and these have to do with like the topic clusters is how the Looker dashboard like shows it.

**Carrie Chowske:** The strategy is how like we know which, like what, what it came from, like where we're, like this is the, this gap analysis is what Tanmay gave me versus like we were working on like this sovereignty and flex architecture and like a bunch of like hybrid categories within that.

**Carrie Chowske:** So that's why we have those separated.

**Carrie Chowske:** And then show you like one other thing.

**Carrie Chowske:** What's the other thing that I'm forgetting, Joe?

**Carrie Chowske:** There's something else I'm forgetting.

**Carrie Chowske:** Am remembering something?

**Carrie Chowske:** I think that's it.

**Carrie Chowske:** That might be it.

**Carrie Chowske:** The rest might be for you, Joe.

**Carrie Chowske:** I think you mentioned all.

**Joe Sovar:** mentioned flex, but this with industries.

**Joe Sovar:** So these new ones are for these keyword gaps and this new one are.

**Joe Sovar:** Pro and plus pricing, but I think that's this one that we are doing right now for keyword gaps.

**Joe Sovar:** Okay.

**Carrie Chowske:** So hopefully that's not too much information overload because I just wanted to give you that context.

**Carrie Chowske:** You can refer back to it later if you get confused.

**Carrie Chowske:** You guys can change it if it works better for you.

**Carrie Chowske:** I'm not going to be heartbroken if I come back in here a year from now and see all different stuff.

**Carrie Chowske:** It's not going to bother me.

**Carrie Chowske:** It's just how I set it up because it made sense for me.

**Carrie Chowske:** Then the other stuff that I wanted to touch on was for the use cases project that we're working on.

**Carrie Chowske:** And I don't know what the plan is for, like, who manages the, like, coordinating with engineering.

**Carrie Chowske:** Do we know that answer?

**Carrie Chowske:** I assume it might be me.

**Erik O'Brien:** Okay.

**Carrie Chowske:** I mean, that means, okay.

**Joe Sovar:** I think if you place a ticket, they will respond faster and everything than me.

**Joe Sovar:** But, of course, some things I can ping them when necessary.

**Joe Sovar:** But, yeah, I think it's better if you ping them.

**Carrie Chowske:** So here's what I've got with them currently.

**Carrie Chowske:** Let me show this again.

**Carrie Chowske:** Okay.

**Carrie Chowske:** So I'm currently working on right now.

**Carrie Chowske:** So there's two tickets in here that are different.

**Carrie Chowske:** This one here is for design, which is them creating the collection, the template for the individual pages.

**Carrie Chowske:** I'm to think.

**Carrie Chowske:** And for them to like, so creating like the category page and then the individual pages.

**Carrie Chowske:** like three actual design and stuff and Webflow, because we have to do that before we can do the pipeline.

**Carrie Chowske:** So that's currently in the works.

**Carrie Chowske:** They're actually have a draft of it already.

**Carrie Chowske:** So I'm right.

**Carrie Chowske:** Currently, I think you saw probably I tagged you in this yesterday, but they have.

**Carrie Chowske:** They're currently in the process of like building out the page.

**Carrie Chowske:** So right now I just need like I just needed like a like a mock-up of it to show to Tam and to.

**Carrie Chowske:** Have them say yes or no or make any changes or whatever.

**Carrie Chowske:** This went fairly smoothly last time, so I'm hoping it will again.

**Carrie Chowske:** But I had given them like a, I'd given them a, like a wireframe to start with this time.

**Carrie Chowske:** it might even, hopefully, I'm hoping this one will go faster.

**Carrie Chowske:** But I'm happy to answer any questions too, because I literally just did this with them for the industry stuff.

**Carrie Chowske:** And then the other one is the one for the pipeline itself, which it looks like that got assigned to Kirkland.

**Carrie Chowske:** So that's great, because he did our other one.

**Carrie Chowske:** So he should know exactly what to do here.

**Carrie Chowske:** What he's doing is connecting, like there'll be pages that are linked to the industry pages we created, their connectors pages, which are all their little like integrations.

**Carrie Chowske:** And I think I listed them all here.

**Carrie Chowske:** I know I did actually.

**Carrie Chowske:** But anyway, so he'll have questions about that when he starts working on it.

**Carrie Chowske:** But it's going to be so similar to what he did before.

**Carrie Chowske:** And I think Joe knows enough, too, that I think you guys can probably.

**Carrie Chowske:** Probably do it without needing me to jump in, but I'm happy to if I need to.

**Carrie Chowske:** It's not a problem.

**Carrie Chowske:** And I think that's it.

**Carrie Chowske:** I don't think we have any other tickets open for them.

**Carrie Chowske:** No, we have one for that.

**Joe Sovar:** Oh, for the TLDR.

**Joe Sovar:** Yeah, we have, like, tables are embedded now in Webflow, but we need to figure out how to embed the code.

**Joe Sovar:** But we probably will need to place another ticket because Kirk can't close the one.

**Carrie Chowske:** Okay, I'll let you guys handle that then.

**Carrie Chowske:** The other thing that we are in the process of needing to do, and I was getting ready to kind of work out a way that we could add this into the existing, like, schedule to, like, so that Joe wouldn't go crazy having to generate all this, but is adding a TLDR into their existing content.

**Carrie Chowske:** But they've got, like, 600 pages that we've done for them.

**Carrie Chowske:** And there's a variety of disasters that occurred the last time we tried to...

**Carrie Chowske:** So we're trying, he's trying to make sure that we have a working pipeline to be able to do it without him having to redo and redo or manually do a bunch of stuff.

**Carrie Chowske:** So that's where we're at.

**Carrie Chowske:** And that's also why we don't have auto publishing.

**Carrie Chowske:** So there you go.

**Carrie Chowske:** Or send it to Suleiman to publish.

**Carrie Chowske:** It kind of is like a weird little custom bug that we have to deal with.

**Erik O'Brien:** And that's specific to the TLDRs.

**Erik O'Brien:** It's specific to Airbyte.

**Carrie Chowske:** And it's specific to Webflow.

**Carrie Chowske:** So there, what's, what happened, the short version of it, I guess, is that our pipeline, the auto publish step in our pipeline, messes up the table situation, which we did fix.

**Carrie Chowske:** But then it also is now messing up anytime we use a code snippet.

**Carrie Chowske:** And Tanmay wants an image, a code snippet, or a table every 400 words.

**Carrie Chowske:** And so for the pages that have those things on them, if we update them with our refresher and then try to publish from there, it'll break the tables or it'll break the code.

**Carrie Chowske:** And again, I think we fixed the table thing.

**Carrie Chowske:** Is that correct?

**Carrie Chowske:** The table.

**Carrie Chowske:** The one's fine.

**Carrie Chowske:** But now we've got the issue with the code snippets.

**Carrie Chowske:** So I just didn't want, because Joe has literally already refreshed those 600 articles three times since we took over this account in, what was that, July?

**Carrie Chowske:** August?

**Carrie Chowske:** Something like that?

**Carrie Chowske:** It wasn't that long ago.

**Joe Sovar:** Yeah, yeah.

**Carrie Chowske:** So anyway, in order to save his sanity, that's what I was trying to figure out, like make sure that we could get engineering, get us a workable solution before we started doing that.

**Carrie Chowske:** So.

**Joe Sovar:** Yeah, in case we can't do it, that's why I'm suggesting just 50 a week.

**Joe Sovar:** And that way I can check them and in worst case scenario, manually embed those codes and we will be good.

**Joe Sovar:** But hopefully they can resolve that.

**Joe Sovar:** So everything will be automated that way.

**Carrie Chowske:** And also now the nice thing is too, since this is going to be Joe's only account, since they've got, right now they have three different work streams with us.

**Carrie Chowske:** So it'll be his only account.

**Carrie Chowske:** Then there's a lead.

**Carrie Chowske:** It's got a little more capacity to do that stuff, but not, you know, not 100 a week like we were doing before.

**Erik O'Brien:** It's still crazy.

**Carrie Chowske:** That's not feasible.

**Carrie Chowske:** I'm going to say, unless it works perfectly, then maybe, but I doubt it.

**Carrie Chowske:** We're not there yet, but.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Then what do you guys look at on a weekly basis for their check-ins?

**Carrie Chowske:** I kind of give them a rundown. We've been trying to do more with SEO for them.

**Carrie Chowske:** They've been shifting a bit. Tanmay is very focused on traditional SEO.

**Carrie Chowske:** He wants to make sure there's a keyword in every title and pays attention to very traditional SEO fundamentals.

**Carrie Chowske:** But in terms of reporting, we've been looking at sessions more than clicks, looking at overall traffic instead of just search traffic.

**Carrie Chowske:** And they've been experimenting. Tanmay was reviewing the scrunch prompts.

**Carrie Chowske:** I'm not sure if he's finished reviewing them yet, but I know Airbyte is switching off scrunch, so I don't know what that'll mean going forward.

**Carrie Chowske:** But he was going to review them and see if there's anything he wanted to track or change or anything like that.

**Erik O'Brien:** Gotcha.

**Erik O'Brien:** And then was there some experiment you guys were tracking?

**Carrie Chowske:** Yeah, that was the TLDR thing. It's still ongoing, actually.

**Carrie Chowske:** Let me check the TLDR experiment data real quick. I was going to look at it yesterday but didn't get to it.

**Carrie Chowske:** That was from Jacob.

**Carrie Chowske:** He was wanting us to try out doing TLDRs.

**Carrie Chowske:** And that's why we're implementing them on all the pages.

**Carrie Chowske:** We decided from the early data that it was worth just doing because it wasn't hurting anything, even though it wasn't clear that it was helping either.

**Carrie Chowske:** So we were using SEO testing for that.

**Carrie Chowske:** And I can.

**Carrie Chowske:** And there's also a tag in scrunch for this test as well that you can look at the scrunch prompts we were tracking for this.

**Carrie Chowske:** But yeah, it's just about done.

**Carrie Chowske:** It should be done this week, I think.

**Carrie Chowske:** I think the final date on it's like the first.

**Carrie Chowske:** What are you talking about?

**Carrie Chowske:** Don't yell at me.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** So it's like, it's such a close little call.

**Carrie Chowske:** And then up until before we were getting a positive on all of these.

**Carrie Chowske:** So like last week when we checked it, it was all positive.

**Carrie Chowske:** So.

**Erik O'Brien:** So will we need to report on this moving forward or is this kind of wrapped up?

**Carrie Chowske:** I would give them a final report once it's done, but they were kind of set on doing it regardless, just based on the early data.

**Carrie Chowske:** And like, even this is not, I don't think that's even like, because we had a control group.

**Carrie Chowske:** But again, it can be in any number of things affecting it, so it's not even a true control group, you know what I mean?

**Carrie Chowske:** Yeah.

**Carrie Chowske:** But yeah, so it's got another two days on it, so.

**Carrie Chowske:** Gotcha.

**Erik O'Brien:** And the login for that's in 1Password, so.

**Erik O'Brien:** 1Pass, okay.

**Carrie Chowske:** Yeah, yeah, it's all, it's all like, it's access to all the ones that we've created for anybody, so it's just, you have to pick the one, and then it's in here, like when you, like where I just clicked on it, all three of these are actually the same test, it's just, it creates like one top level one, and then it does one for each group.

**Carrie Chowske:** Gotcha.

**Carrie Chowske:** You can see that, like, they're both gaining clicks over time, but, you know, one, one, up until, this was the only, this is the only time I looked at it where it wasn't as significant, or the test.

**Carrie Chowske:** group wasn't significantly ahead of the control, so I didn't have, I didn't have direct, like, I didn't have a direct involvement with that other than I set this test up, I said, I mean, I set up the, like, the tracking for the test, Jacob was really the one that was kind of, like, running that as, as, you know, part of, I guess he's, that's part of what he's going to be doing, I think, going forward as being, like, experimentation and stuff, so I think that's, yeah.

**Erik O'Brien:** All right, so, got the overview.

**Erik O'Brien:** Oh, gosh, I mean, just, yeah, go ahead, I'm sorry, ask what you're going to ask.

**Erik O'Brien:** I was getting to Looker, but when would you think the next refresh of Airtable is needed?

**Carrie Chowske:** Like, for, like, like, looking at their strategy and stuff?

**Carrie Chowske:** Yeah.

**Carrie Chowske:** I'm going to say probably not anytime soon. Once they're done with their Sprint, I think they're going to rethink and consolidate some of what they're doing.

**Carrie Chowske:** So I think it'll probably happen naturally when the Sprint is over.

**Carrie Chowske:** And we're good on content for the rest of the year.

**Carrie Chowske:** Like, there's plenty for Joe to work on and fulfill contractually, and they're fine with that.

**Carrie Chowske:** We've talked about that.

**Carrie Chowske:** So I think it's probably just going to depend on what the outcome of the Sprint is.

**Carrie Chowske:** And I don't know enough about that, like, that you're more plugged in on that.

**Carrie Chowske:** So, like I said, like I said yesterday in our call, it's, the perfect time to be doing this handover because with them coming off a Sprint on the context part of it, like, I think it'll be a good time in the new year to just kind of go, okay, where are we at?

**Carrie Chowske:** What do we want to do next?

**Carrie Chowske:** Yeah.

**Erik O'Brien:** Cool.

**Carrie Chowske:** And you've got enough content to go a few weeks into the new year, so it's not like you need a new strategy immediately on January 1st.

**Carrie Chowske:** Like, there's plenty there to keep you going, especially once those use cases and with the TLDRs.

**Carrie Chowske:** We're doing plenty for them with those work streams, even without the editorial content. I'm sure they're going to want to reassess that in the new year.

**Carrie Chowske:** On there, I think their Looker is pretty straightforward.

**Carrie Chowske:** don't think I've done anything custom for it.

**Carrie Chowske:** There is one thing, but it's not anything that ever needs updating.

**Carrie Chowske:** And Joe knows all this too, because he's already been updating their Looker.

**Carrie Chowske:** But when you go to, like, their cohorts, like this down here, when we did the batch refreshes, we grouped, I did a quick little grouping of them so we could see how those were doing.

**Carrie Chowske:** And batch one, for whatever reason, is consistently killing the other ones.

**Carrie Chowske:** It's also a much larger batch, which might be part of that.

**Carrie Chowske:** Usually when I do reporting for them, I exclude not just the non-growthx content, but also the batch refresh, because those aren't included in their other groupings.

**Carrie Chowske:** So, and this often, you have to kind of play around with it because they have so many pages on their site.

**Carrie Chowske:** I'm talking like thousands of pages, and we've done over a thousand, I think, for them.

**Carrie Chowske:** This takes forever to load, and then if you try to do more than two months, it often will break.

**Carrie Chowske:** won't show you, though.

**Carrie Chowske:** The chart won't show you the whole time period.

**Carrie Chowske:** The table's usually correct, but the chart's usually wrong.

**Carrie Chowske:** Like if I try to do this like back to August or something, it'll do it this way.

**Carrie Chowske:** And then do you report on cohorts weekly or?

**Carrie Chowske:** It kind of depends on what we've been working on.

**Carrie Chowske:** Like I had, because we had just started in September, we had done, we were doing stuff for their new product that they had rolled out.

**Carrie Chowske:** They had done a new pricing tier, and they were promoting like a hybrid deployment for their data connection.

**Carrie Chowske:** We had been reporting on how that content was doing.

**Carrie Chowske:** So I was specifically looking at those subcategories: cloud and hybrid architecture, and security, privacy, and compliance.

**Carrie Chowske:** Those were the two main ones we were reporting on.

**Carrie Chowske:** So I would report on those because we had just started publishing content on them in October.

**Carrie Chowske:** So I was giving them weeklies on that, but they've killed that product.

**Carrie Chowske:** That's the product that they killed.

**Carrie Chowske:** So I don't know that we necessarily need to go that deep.

**Carrie Chowske:** This industry, PSEO is literally those industry pages.

**Carrie Chowske:** I can't, they'll probably be interested in that, but it's still relatively new.

**Carrie Chowske:** This isn't even going to give you a Delta in sessions because we weren't publishing them back in August.

**Carrie Chowske:** I think we've only been doing them since the end of last month.

**Carrie Chowske:** Right, Joe?

**Carrie Chowske:** So, um, but I know he'll be interested.

**Carrie Chowske:** And how those are performing.

**Carrie Chowske:** He's very, like I said, he's very traditional SEO with a lot of stuff.

**Carrie Chowske:** Like he does definitely pay attention to keywords, but yeah.

**Erik O'Brien:** I'll just look at your other weekly syncs to see kind of what you're reporting on.

**Erik O'Brien:** But anything else that you guys call out like on a weekly basis that I need to be aware of?

**Carrie Chowske:** Yeah, Tanmay's been asking a lot about the scrunch, like how scrunch works and stuff and like what we can do with that and what we can look at.

**Carrie Chowske:** And I think they were going to set it up so that they could check like the, because you know you've got that like section in there where to like look at what agents are sending you traffic.

**Carrie Chowske:** And they were going to set that up.

**Carrie Chowske:** I don't know if they've done that.

**Carrie Chowske:** That was like a couple calls ago.

**Carrie Chowske:** We talked about that.

**Carrie Chowske:** He said, let me know when you got it set up.

**Carrie Chowske:** Do they have access?

**Erik O'Brien:** Yes, they have access to Scrunch, yeah.

**Erik O'Brien:** Okay.

**Carrie Chowske:** But I think it's like a thing on their end they have to do because they have to add it for like Cloudflare to like tell it to let it track this thing or whatever.

**Erik O'Brien:** So I don't know.

**Carrie Chowske:** I don't know enough about the technical part of that of it to tell you exactly what it is, but I know they have to set it up on their end.

**Erik O'Brien:** Gotcha.

**Carrie Chowske:** But yeah, I kind of just do it.

**Carrie Chowske:** What I typically will do is based on like where we're focusing our efforts, you know, so like I said, right now I would have, like this week I probably would have reported to them on like anything I could give them about the early signals from those industry pages that we did because those are the newest thing we've done and then kind of give them a recap of like, you know, if we were still doing the other stuff I would have, you know, kind of said to them, okay, here's where we're at with this a month out.

**Carrie Chowske:** And like, so I just try to like report on the stuff that we've been, where we've been putting our biggest production efforts, like giving them, giving them the, the.

**Carrie Chowske:** The wins there and like anything that we think we need to adjust based on that.

**Carrie Chowske:** But they're usually also pretty, Tanmay especially, like usually has ideas and will just straight up give you like, let's do these keywords.

**Carrie Chowske:** Okay, let's do these keywords.

**Carrie Chowske:** I mean, so like you can crumb up with a whole strategy for him and he'll just tell you like a week later, like we're doing something else.

**Carrie Chowske:** So that's fine.

**Carrie Chowske:** Sometimes it's nice, you know, because then you don't have to like, okay, that's fine.

**Carrie Chowske:** Great.

**Carrie Chowske:** I'll do that now.

**Erik O'Brien:** Those are the main questions. Coming out of three months of strategy sprints where we don't really do reporting, I'm just trying to pick up on what they care about.

**Carrie Chowske:** The thing is that they will, no matter what you prepare for them, they will always ask you a question that you have not, you do not have an answer for.

**Carrie Chowske:** It happens to me every week and I think I really got to where I thought I could predict what they were going to ask.

**Carrie Chowske:** Especially Tanmay, and he'll just have something new every week that he's like, what about this?

**Carrie Chowske:** And so the more you can stay on top of a lot of the trends too in GEO, they're very much about that.

**Carrie Chowske:** Kyle would often be my go-to on that one.

**Joe Sovar:** I think LLM referrals are something they care about a lot in the last months or so.

**Carrie Chowske:** Yeah, they definitely do.

**Carrie Chowske:** What referrals they're getting from LLMs.

**Carrie Chowske:** Yeah, I do almost always pull this for them to show them like which LLMs they're getting traffic from.

**Carrie Chowske:** Like everybody else, they're mostly getting traffic from ChatGPT.

**Carrie Chowske:** But they've gotten a lot lately from Claude.

**Carrie Chowske:** Like their Claude numbers have like ballooned in the last like three or four months.

**Carrie Chowske:** Interesting.

**Erik O'Brien:** Yeah.

**Carrie Chowske:** I thought that was interesting too because Claude doesn't strike me as a very tech-forward tool, and it doesn't usually have citations to link out once you have web browsing turned on.

**Erik O'Brien:** Well, I know we're at time.

**Erik O'Brien:** Any other things we didn't cover that we should have?

**Carrie Chowske:** I think we're good.

**Carrie Chowske:** I hit on all the things I wanted to make sure that you knew what to look for because, like I said, I tend to get very, like, I'll make it so it works for me and then other people look at it and go, I don't know what the heck you're doing here, Carrie.

**Carrie Chowske:** So if you hit anything like that, please ask me.

**Carrie Chowske:** I don't mind explaining it and then you can make it work for you. Joe is just great with getting the content done on time.

**Carrie Chowske:** We're delivering out a week ahead. We're delivering next week's content to Tanmay today.

**Carrie Chowske:** So Joe's out far enough ahead, too, that we're not, you know, we're never playing catch up with them.

**Carrie Chowske:** And they're pretty happy with what we've been doing.

**Carrie Chowske:** So, and I think the same is true for the Sprint.

**Carrie Chowske:** So it's an account that's in really good shape.

**Carrie Chowske:** It's, it's, it's.

**Carrie Chowske:** Sad to hand it off, actually, in a lot of ways.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** So, yeah, but you can rely on Joe for a lot of answers, too.

**Carrie Chowske:** So he knows everything I do.

**Carrie Chowske:** He watches every call, and he absorbs more of the information in it, usually, than I do.

**Joe Sovar:** Yeah, Carrie, nevertheless, I still have many questions for you down the road, especially regarding strategy things, et cetera.

**Joe Sovar:** Yeah, I mean, I'm on content most of the time, and Carrie is doing all these high-level things.

**Carrie Chowske:** Yeah, Joe's a great partner in crime for this kind of stuff, so I think you're going to enjoy working with him a lot.

**Carrie Chowske:** He knows his stuff.

**Carrie Chowske:** Awesome.

**Carrie Chowske:** Love to hear that.

**Erik O'Brien:** miss you with him.

**Carrie Chowske:** Yeah, thanks, Carrie.

**Joe Sovar:** I'm going to miss working with you, too.

**Carrie Chowske:** Anyway, I still have my – we've left our one-to-ones on the calendar, too, for a little bit, too, so if he has questions.

**Carrie Chowske:** So if you want to jump on at all and if you want him to jump on, Joe.

**Carrie Chowske:** So just let me know.

**Carrie Chowske:** Like we can also, the three of us can still coordinate as long as we need to.

**Carrie Chowske:** I really don't mind.

**Carrie Chowske:** Like it's not, you know, it's not a hassle.

**Carrie Chowske:** This was an easy, like I said, it started off as an account.

**Carrie Chowske:** I thought it was going to kill me.

**Carrie Chowske:** And then it turned out to be a really fun one.

**Erik O'Brien:** Well, I hope I have the same experience.

**Erik O'Brien:** I do too.

**Erik O'Brien:** Hassle, but it sounds like you guys have left it in a great place for me.

**Erik O'Brien:** So excited to, yeah, I think the transition from the sink or the sprint rather, will tell us a lot of where they want to go next.

**Erik O'Brien:** Yeah, for sure.

**Carrie Chowske:** Sure.

**Erik O'Brien:** Cool.

**Erik O'Brien:** I appreciate the rundown.

**Erik O'Brien:** It's a little oiled machine.

**Carrie Chowske:** So there you go.

**Carrie Chowske:** You guys have done an awesome, awesome job.

**Erik O'Brien:** Oh, thank you.

**Carrie Chowske:** Thank you.

**Carrie Chowske:** All right.

**Carrie Chowske:** Let me know if you need anything else, but otherwise we're good to go.

**Carrie Chowske:** All right.

**Erik O'Brien:** All right.

**Erik O'Brien:** Thanks, Bye.

**Erik O'Brien:** Bye.

**Erik O'Brien:** Bye.
