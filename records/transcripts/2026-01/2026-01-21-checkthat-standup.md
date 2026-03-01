# CheckThat Standup

<metadata>
date: 2026-01-21
time: 15:59 UTC
duration: 48 minutes
organizer: Stevie Kim (stevie@growthx.ai)
participants:
  - name: Estevão Mascarenhas
    email: estevao@growthx.ai
    affiliation: GrowthX
    role: Product/Engineering
  - name: Marcel Santilli
    email: marcel@growthxlabs.com
    affiliation: GrowthX Labs
    role: Advisor
  - name: Jason Gong
    email: jason@growthx.ai
    affiliation: GrowthX
    role: Marketing
  - name: Jose Farias
    email: jose@growthx.ai
    affiliation: GrowthX
    role: Engineering (Architecture)
  - name: Pedro Steimbruch
    email: pedro@growthx.ai
    affiliation: GrowthX
    role: Engineering
  - name: Daniel Lopes
    email: daniel@growthx.ai
    affiliation: GrowthX
    role: Engineering/Product Lead
  - name: Leonardo Carpenedo Steffen
    email: leonardo@growthx.ai
    affiliation: GrowthX
    role: QA/Testing
  - name: Stevie Kim
    email: stevie@growthx.ai
    affiliation: GrowthX
    role: Operations/Product
fathom_recording_id: 115983859
fathom_url: https://fathom.video/calls/538436070
share_url: https://fathom.video/share/BZp8aX752bWJBwmCj_5hu8F76ymrn_zx
source: fathom
enriched_on: 2026-02-28 10:15 UTC
</metadata>

---

## Summary

Team synced on pre-launch progress across visibility features, platform architecture, and QA strategy. Core focus is manual production testing to catch data-specific bugs before launch, with parallel work on subcategory re-architecture, onboarding stability, and billing system design.

---

## Context

CheckThat is in final sprint before launch with three stabilization tracks running: visibility features (Google AI Overview probes, competitor backfilling), onboarding flow (brand cloning workaround with future architecture simplification), and user management (billing RFC, workspace owner concept to prevent abuse). The team emphasized that production data testing will uncover bugs that local testing misses, driving the decision to prioritize manual QA over test automation this week. This is a cross-functional checkpoint where engineering blockers are minimal but architecture decisions (subcategory unification, MarTech integration) will shape post-launch roadmap.

---

## Relevance

**Product Development**
- Pre-launch testing strategy and QA execution
- Architecture decisions affecting long-term maintenance (subcategory model unification)
- Onboarding flow design and edge-case handling

**Engineering**
- Bug fixes in visibility features (Google AI Overview webhook issue, probe counts)
- Workspace switching refresh issue and workspace ID cookie implementation
- Subcategory re-architecture impact on data scoping and UI correctness

**Operations & Monetization**
- Billing RFC requirements and workspace owner concept for abuse prevention
- Audit trail implementation (post-launch)
- MarTech stack evaluation (Segment vs RudderStack, Customer.io vs HubSpot)

**QA & Delivery**
- Manual production testing approach and test script setup
- Test coverage across critical client accounts and new user onboarding
- Bug triage and Linear ticket assignment

---

## Overview

- **Testing Strategy:** Manual production testing prioritized this week over test automation. Production data will uncover data-specific bugs and edge cases that local syncs and automated tests miss, especially for new user sign-ups and brand-specific variations.
- **Subcategory Architecture:** Jose is re-architecting subcategories into a single, first-class model (currently fragmented across three mechanisms). This unifies data scoping for overview charts and eliminates brand duplication by making workspaces directly subcategorizable.
- **Onboarding Flow:** Estevão implemented a brand cloning workaround that lets new users access the app immediately while deep research runs in the background. Enforce subcategory selection during sign-up to prevent empty-workspace edge cases.
- **Google AI Overview:** Pedro shipped a temporary fix hiding non-persisted probe results. Investigate root cause on Flow side (empty webhook responses). Implement probe-immediately feature (~15 min) to improve perceived responsiveness.
- **Prompt Count Display:** Overview shows only probed counts, not total prompts. Deferred UI fix to post-launch to avoid screen clutter; will create support ticket for future improvement.
- **Workspace Switching Bug:** Hard refresh sometimes required after switching workspaces—likely due to workspace ID migration to cookies. Low priority (affects internal team only), but should be recorded and triaged.
- **Billing & Abuse Prevention:** Estevão writing billing RFC. Introduce workspace "owner" concept limiting free ownership to one per user. Audit trail (using PaperTrail) deferred to post-launch.
- **MarTech Stack:** Daniel evaluating Segment vs RudderStack for CDP and Customer.io vs HubSpot for event-based email nurturing. Requires sync with Jason on HubSpot capabilities.

---

## Key Topics

### Pre-Launch Testing Strategy

  - **Decision:** Prioritize manual production testing this week over test automation.
  - **Rationale:** Production data is the only way to find data-specific bugs, as local syncs are incomplete.
  - **Process:** Test critical client workspaces and edge cases (e.g., new sign-ups with no existing brand data).
  - **Tooling:** Leonardo will use a shared Google Doc for the test script and results.

### Onboarding & Subcategory Architecture

  - **Problem:** The current subcategory model is fragmented (3 separate mechanisms), causing incorrect overview charts and requiring brand duplication.
  - **Solution (Jose):** Re-architect subcategories into a single, first-class model.
      - **Benefit 1:** Fixes overview charts by scoping data to the workspace's specific subcategorization.
      - **Benefit 2:** Eliminates brand duplication by making workspaces directly subcategorizable.
  - **Onboarding Flow (Estevão):**
      - **Existing Brand:** Clones the public brand profile to a private workspace brand, allowing for a fast, non-blocking onboarding.
      - **New Brand:** Runs deep research in the background, letting the user access the app immediately.
  - **Edge Case:** Onboarding a brand with no subcategory match can result in an empty workspace.
      - **Resolution:** Enforce subcategory selection during sign-up to prevent this.

### Bug Fixes & Immediate Tasks

  - **Google AI Overview Probe:** A temporary fix hides non-persisted results. Pedro will investigate the root cause (empty webhook response) on the Flow side.
  - **Prompt Count Discrepancy:** The overview shows only *probed* prompts, not total prompts, causing confusion.
      - **Decision:** Defer a UI fix to post-launch to avoid screen clutter.
      - **Post-Launch Task:** Create ticket for "probed/total" count display option.
  - **Workspace Switching Bug:** Users sometimes need a hard refresh after switching workspaces.
      - **Cause:** Likely introduced by moving the workspace ID to a cookie.
      - **Impact:** Affects internal EMs, not a launch blocker.
  - **Immediate Tasks (Pedro):**
      - Investigate the Google AI probe issue on Flow side.
      - Implement "Run probes immediately" feature (~15 min).
      - Create an empty state for the prompt show page.

### Billing, User Management & MarTech

  - **Billing RFC:** Estevão is writing the Request for Comments for the billing system.
  - **Abuse Prevention:** To prevent users from creating multiple free workspaces, the team will introduce a workspace "owner" concept.
      - **Rule:** One free workspace ownership per user.
      - **Implementation:** Add an `owner` boolean to the `enrollment` model.
  - **Audit Trail:** An audit trail (using PaperTrail) is a post-launch priority.
      - **Rationale:** Crucial for support and GDPR compliance.
  - **MarTech Stack (Daniel):**
      - **Data Layer:** Evaluate Segment vs. RudderStack.
      - **Email Nurturing:** Evaluate Customer.io vs. HubSpot.
          - **Requirement:** Event-based nurturing (e.g., user action triggers email flow).
          - **Action:** Sync with Jason on HubSpot's capabilities.

---

## Action Items

**Pedro Steimbruch (GrowthX)**
- Investigate Flow webhook sending empty Google AI Overview responses
- Create post-launch ticket re: overview prompt counts (probed/total)
- Implement probe immediately after prompt creation
- Share prompt show page empty-state design w/ Daniel; then implement

**Daniel Lopes (GrowthX)**
- Record workspace-switch refresh bug; create Linear ticket
- Check study probing data; monitor costs; adjust API keys if needed
- Migrate CheckThat workflows to new framework; move to dedicated repo
- Decide CDP (Segment vs RudderStack); integrate Intercom via CDP/GTM
- Evaluate Customer.io vs HubSpot for email nurturing; sync w/ Jason on Slack

**Estevão Mascarenhas (GrowthX)**
- Enforce subcategory selection during onboarding
- Remove 'we will notify you when ready' copy from onboarding

**Stevie Kim (GrowthX)**
- Update 'Invite Users to Workspace' ticket: add owner flag + audit trail (post-launch)
- Run manual QA: 10 critical clients + new-account sign-ups; log bugs in Linear

**Leonardo Carpenedo Steffen (GrowthX)**
- Set up QA sheet in Google Docs; create tabs for test types
- Run manual QA: 10 critical clients + new-account sign-ups; log bugs in Linear
- Triage bugs in Linear; assign to milestones

---

## Transcript

**Jose Farias:** Thank you.

**Stevie Kim:** Be right back, I gotta let my dog in.

**Stevie Kim:** Thank you.

**Daniel Lopes:** Hey, hey.

**Daniel Lopes:** Morning.

**Daniel Lopes:** Good morning.

**Jose Farias:** Morning.

**Daniel Lopes:** I don't know if Marcel is joining today.

**Daniel Lopes:** Hopefully not.

**Daniel Lopes:** We can probably start with Fathom.

**Daniel Lopes:** Feel free to read, Stevie.

**Stevie Kim:** Hey, so I feel like we just met, so I don't really have anything new.

**Stevie Kim:** No, yeah, so Jose fleshed out the "invite user to workspace" ticket and did a couple other things last night, but yeah, I don't think I have anything that's changed.

**Stevie Kim:** There are some interesting import-export requests coming from Ask CheckThat—either wanting to import topic clusters together with prompts or export imports for customers to edit and import back.

**Stevie Kim:** So I told them we're not creating that functionality right now.

**Stevie Kim:** We're hyper-focused on just the launch and core functionality and user experience.

**Stevie Kim:** But I thought that was kind of interesting feedback.

**Daniel Lopes:** Yeah, maybe we use this meeting more like a daily standup, since I wasn't the one that scheduled it. But it's useful to have a time like this when we have this set of to-dos that have to be done every day so we can go through the list together.

**Daniel Lopes:** Maybe I can pull the list and then you guys give me an update on how each thing is going and what are you thinking ahead.

**Daniel Lopes:** Because one of the things that I'm kind of worried about is that we need to carve time to do manual testing.

**Daniel Lopes:** I saw your spreadsheet, Leo.

**Daniel Lopes:** I don't know how you're thinking about that—how do you think about doing that if it's going to be automated?

**Daniel Lopes:** But I would highly suggest that we do a shift to manual testing this week before we think about automating anything.

**Leonardo Carpenedo Steffen:** I was just exploring some of the alternatives to manually or automate the tests since we're going to have to do them manually anyway, and I was hoping that AI-assisted record-and-playback testing tools are better these days.

**Leonardo Carpenedo Steffen:** But I haven't had a chance to test them yet.

**Daniel Lopes:** Yeah, I don't think that's going to work.

**Daniel Lopes:** I would just like to manually go through everything because the real challenge that I think it will be is the kind of stuff that we were talking about yesterday.

**Daniel Lopes:** It's just like going through, get a list of like 10 critical clients, go through every screen and see like, does this screen make sense?

**Daniel Lopes:** I think the list of tests you have makes sense, but then find the actual clients that we need to impersonate, go into their workspace and look if the data is correct.

**Daniel Lopes:** And look at the probes and like really do a bunch of clicking around and see if everything makes sense.

**Daniel Lopes:** And then next week we can automate the happy path of everything, if everything goes well.

**Daniel Lopes:** But like in my experience, I usually do this even by myself, and I usually find a ton of stuff in a week before launch.

**Daniel Lopes:** And this is a seven-feature project that is pretty large.

**Daniel Lopes:** And the data is going to be all in production.

**Daniel Lopes:** So it's really hard to reproduce locally.

**Daniel Lopes:** Anyway, so we have...

**Daniel Lopes:** Sorry, go ahead.

**Leonardo Carpenedo Steffen:** No, I just took the scenarios from the plan you described, and took some other information that was already in all the documentation that was attached to that plan, and I just simply created a script because it's going to be easier to follow and divide the work in a sheet.

**Leonardo Carpenedo Steffen:** Yeah, I agree.

**Daniel Lopes:** That's perfect.

**Daniel Lopes:** Yeah, that's great.

**Daniel Lopes:** But my main point is just like the production data will be the one that's going to uncover everything because the probing is all like a sheet of data and it varies so much based on prompt and all that.

**Daniel Lopes:** And when we sync locally, we sync just a chunk of it, not the whole thing.

**Daniel Lopes:** So we're going to be testing production.

**Leonardo Carpenedo Steffen:** Is that it?

**Leonardo Carpenedo Steffen:** Yeah.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Click around production and see some problems.

**Daniel Lopes:** Cool.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So we have the visibility stuff, the sign-up and onboarding, your QA and doing on the laws.

**Daniel Lopes:** He's...

**Daniel Lopes:** So those are the three core things.

**Pedro Steimbruch:** Can I jump so I can explain what I'm working on and how I see that?

**Daniel Lopes:** So today I shipped the Google AI overview probe results that are not persisted.

**Pedro Steimbruch:** Okay, so I shipped a workaround for now that is not to display the Google AI overview probe that doesn't have a response.

**Pedro Steimbruch:** We are not displaying the probe table right now.

**Pedro Steimbruch:** Okay, I need to investigate on the Flow side why we are sending the webhook with an empty response.

**Pedro Steimbruch:** There is probably a niche on the Flow side.

**Pedro Steimbruch:** Okay, that "compare visibility only shows last two days" is basically done already.

**Pedro Steimbruch:** We need to decide what to do with other two things.

**Pedro Steimbruch:** I only remember one on that ticket.

**Pedro Steimbruch:** Okay, the one thing that I remember, it's related to that ticket.

**Pedro Steimbruch:** It isn't that ticket.

**Pedro Steimbruch:** Besides...

**Pedro Steimbruch:** The visibility issue is that counting of prompts we are showing in the overview. As I explained yesterday, yeah, that one—if today you add 200 prompts, we are still showing only 50 because you only have 50 prompts that were probed.

**Daniel Lopes:** So that's the thing.

**Pedro Steimbruch:** And even if you hover over the actual app, that info icon, you will see that this is basically what it says in the helper text.

**Pedro Steimbruch:** It's maybe we need to improve it, but I'm not sure. But this task is basically done.

**Pedro Steimbruch:** I don't think we need to do anything right.

**Pedro Steimbruch:** Got it.

**Daniel Lopes:** That makes sense.

**Daniel Lopes:** Like, I don't want to pollute the screen.

**Daniel Lopes:** This is probably one of the things that will come as support tickets, but another option here would be like "372 probed out of 500 total" or something like this.

**Daniel Lopes:** And then like have some sort of like this.

**Daniel Lopes:** But that's going to pollute the screen and add more stuff, but maybe we don't need to do that now.

**Daniel Lopes:** But we can create a ticket for post-launch.

**Daniel Lopes:** I can write that down and do it afterwards.

**Daniel Lopes:** Maybe you can take notes on that, Stevie.

**Daniel Lopes:** Maybe that makes sense.

**Daniel Lopes:** Or, Pedro, if you want to create a separate ticket for post-launch.

**Pedro Steimbruch:** I can do that.

**Pedro Steimbruch:** No problem.

**Pedro Steimbruch:** Yeah, yeah.

**Pedro Steimbruch:** I was not sure what we should do with that.

**Pedro Steimbruch:** I can do that.

**Daniel Lopes:** I think we can just experiment with the idea of creating the design, but we don't have to do that now.

**Daniel Lopes:** This is what you have is enough.

**Daniel Lopes:** Okay.

**Pedro Steimbruch:** So if I go back to Linear so I can finish my notes...

**Pedro Steimbruch:** Yeah, right.

**Pedro Steimbruch:** Yeah, not true.

**Pedro Steimbruch:** And then I need to investigate in Flow.

**Pedro Steimbruch:** Then I will work on this.

**Pedro Steimbruch:** This should be very quick.

**Pedro Steimbruch:** I'll run probes immediately.

**Pedro Steimbruch:** It should be like 15 minutes, and adjust an empty state for the prompt show page.

**Pedro Steimbruch:** And then I...

**Pedro Steimbruch:** I...

**Pedro Steimbruch:** Probably jump in to "invite users to workspace" then, I'm still divided.

**Pedro Steimbruch:** Yeah, if I get there before Steffen, we need to see, yeah.

**Pedro Steimbruch:** Sounds good.

**Daniel Lopes:** If you could share the UI design for the blank state, you can tag me and then I can give some feedback if anything.

**Jose Farias:** We already have some state for backfilling the prompts.

**Jose Farias:** I can share what it is.

**Jose Farias:** Cool.

**Daniel Lopes:** Nice.

**Jose Farias:** I might jump in here because that competitor visibility ticket actually did result in quite a bit of work that I failed to capture in other tickets.

**Jose Farias:** I alluded to this yesterday and then I failed to create the actual tickets, but worth mentioning—there's like some conversation happening and we actually talked about multiple issues.

**Jose Farias:** I can identify six, out of which four are done and then two aren't. For one thing, the title—"ticket visibility only for the last two days."

**Jose Farias:** That, Pedro, you said is fixed.

**Jose Farias:** I assume you mean because of the backfilling when switching competitors, correct?

**Jose Farias:** That's what you're thinking.

**Jose Farias:** Okay, so that was one thing, right?

**Jose Farias:** The main, the big hairy one, which was fixed when we shipped backfilling when you switch competitors.

**Jose Farias:** Then there's another issue that came up about how many days we backfill.

**Jose Farias:** We are now backfilling based on your plan.

**Jose Farias:** So if you're on the free plan, we backfill 14 days.

**Jose Farias:** If you're on the pro, we do 60.

**Jose Farias:** And then if you're on unlimited, which is an unlisted, like, GrowthX-only plan that's not limited for anything, we do 70 currently.

**Jose Farias:** Ideally, we would have a whole history, but let's just have it at the end for now.

**Daniel Lopes:** Yeah, yeah.

**Daniel Lopes:** It makes sense.

**Jose Farias:** Another thing is that the probe count is weird because of the things that we just talked about.

**Jose Farias:** But the other ticket about probing immediately might fix that because if we probe immediately after adding, then that would increase the count, right?

**Jose Farias:** Is that not correct?

**Pedro Steimbruch:** Yeah, but that can provide a wrong understanding or misunderstanding because if we increase, that will increase, of course, because we are getting those statistics directly from the probes table.

**Pedro Steimbruch:** But the charts below it are based on snapshots, so we can provide the wrong picture.

**Jose Farias:** I mean, I don't think anyone is actually, like, looking at the chart and being like, "Well, that number divided by 572..."

**Jose Farias:** Honestly, they are, though.

**Stevie Kim:** Like, the EMs are, at least.

**Stevie Kim:** I don't, I kind of doubt, like, real, you know, real customers would, but our EMs are very much, like, going like "this number isn't..."—they're looking at the prompts page, comparing it to the, you know, this overview, comparing it to competitors, so that's why, like, I had those tooltips, because they just were comparing everything, but it's all scoped differently.

**Pedro Steimbruch:** Yeah, even like, imagine someone on boards that doesn't have a subcategory, so basically has no prompts, and then it adds prompts, we'll start probing, we'll show probes and prompts in these statistics, but right below will be an empty state.

**Daniel Lopes:** Yeah, that is the kind of stuff that you need to uncover during testing, you know, because that is the kind of stuff that we need to figure out with blank slates and tooltips and UI design.

**Daniel Lopes:** You can't solve a lot of stuff with that kind of work.

**Daniel Lopes:** Like, in this case, for example, we can always say, like, something like "last 24 hours" or like starting, like, or "a day before," or something like that, and then the chart here will always be, like, the day before anyway.

**Daniel Lopes:** So there are ways around it with copy at the stage that we are.

**Daniel Lopes:** But we need to, like, document all these variations and figure out what paths of UI work.

**Daniel Lopes:** That's the kind of stuff that ideally we won't cover doing right now, since we're getting feedback from the EMs already and they're testing this.

**Daniel Lopes:** But maybe a lot of this will be a batch of, like, UI tweaks for a good reason.

**Daniel Lopes:** And then we can do that next week.

**Daniel Lopes:** Okay, that sounds good.

**Jose Farias:** To wrap up this ticket, the final thing I have to say about it is there is one outstanding thing that we should create a ticket for, which is switching workspaces appears to be glitchy.

**Jose Farias:** I assume this was introduced when we removed the ID from the URL and put it in the cookies.

**Jose Farias:** When you switch a workspace, you need to hard refresh.

**Jose Farias:** Or maybe not hard refresh, but just refresh to get the new stuff, at least sometimes.

**Jose Farias:** Yeah, you're right.

**Daniel Lopes:** Yeah, that's in there.

**Daniel Lopes:** So I think, yeah, I think this is...

**Daniel Lopes:** It can be... just switch it... yeah, I can record it.

**Daniel Lopes:** It's only going to affect our EMs, but...

**Daniel Lopes:** Switching... It means... Can do that.

**Jose Farias:** Okay, so that's all the big things that came out of that ticket.

**Jose Farias:** I might as well, since I'm talking already, just finish my round of what I'm doing and what I plan to do today.

**Jose Farias:** That sounds good?

**Jose Farias:** Yeah, sounds good.

**Jose Farias:** Okay, so I've honestly been spending quite a bit of time like jumping between tickets that aren't necessarily assigned to me, but I'll do either review or guide the architecture or like comment or something or push something real quick.

**Jose Farias:** So I've been doing a lot of that.

**Jose Farias:** And looking at the blockers, I'm not super worried about any of them because they don't require like hard, architectural, difficult things.

**Jose Farias:** However, in the stabilization week part, there are two tickets that do require summary architecture.

**Jose Farias:** So I'm actually purposefully tackling those because they're hairy, essentially.

**Jose Farias:** I'll talk about these real quick.

**Jose Farias:** So that one requires—it doesn't necessarily require—but it'll make our lives easier if we re-architect to have a single subcategory model.

**Jose Farias:** Sorry, subcategorization model, which is a joint table.

**Jose Farias:** We currently have three ways to subcategorize: there's a joint table for prompts, there's a joint table for brands, and then brands have a primary subcategory relationship.

**Jose Farias:** So there's three ways to access a subcategorization.

**Jose Farias:** If we standardize, we can treat the subcategorization as a primary entity and then do a bunch of powerful object-oriented things around that.

**Jose Farias:** Specifically, it'll help with fixing the subcategory charts in the overview.

**Jose Farias:** We currently scope that to the subcategory, but that's wrong.

**Jose Farias:** We should scope that to the subcategorization, which includes the prompts for the workspace specifically.

**Jose Farias:** I'm sorry this was long-winded and very difficult.

**Jose Farias:** Okay, so that requires re-architecture, and that's why I'm tackling that.

**Jose Farias:** And the next thing that I was planning to do is stop duplicating the brands by essentially implementing that path that I hadn't seen before, but Daniel gave me clarity on the path forward for that, which is now that we would have a subcategorization first-class model, we can make the workspace subcategorizable.

**Jose Farias:** And so workspaces can choose their own subcategories.

**Jose Farias:** If they haven't, we fall back to their brand.

**Jose Farias:** And that's how we would fix the need to have multiple brands, duplicate ones in the private—if that makes sense.

**Jose Farias:** I think it does.

**Daniel Lopes:** How would you handle the shared library in this case?

**Daniel Lopes:** Like for this categorization of the prompt in the shared library?

**Jose Farias:** So when you first create the workspace, if your chosen subcategories match the brand's, actually, there's no need for a conditional.

**Jose Farias:** Just let, upon onboarding, we just subcategorize your workspace and use that for the bootstrapping.

**Daniel Lopes:** Yeah, makes sense.

**Daniel Lopes:** And like during the onboarding phase, like the flow that Pedro had—if you're coming in and somehow we can't find a subcategory—I think we need to find a subcategory.

**Daniel Lopes:** As in like, that's going to be weird, you know what I mean?

**Daniel Lopes:** I don't know.

**Daniel Lopes:** It's unrelated to what you're saying, but like since we're talking about subcategory, like Pedro brought up a case—if you go to the onboarding and we don't find a good subcategory for you, you're going to end up with no prompts.

**Daniel Lopes:** And then you go into the shared library, you could see all the prompts from all the other categories and can add whatever you want.

**Jose Farias:** You might have no category.

**Daniel Lopes:** You know, I don't know if we force that anywhere.

**Daniel Lopes:** So that's completely unrelated, but since we were thinking about subcategorization, I was trying to think all the edge cases that you could have.

**Daniel Lopes:** But that's an excellent point.

**Jose Farias:** I do think like Pedro mentioned, things would break essentially.

**Jose Farias:** Like, yeah, that's an edge case that we haven't really built for.

**Jose Farias:** I don't think it would be hard to solve.

**Stevie Kim:** Well, isn't there a miscellaneous under niche categories?

**Stevie Kim:** I mean.

**Stevie Kim:** Right.

**Stevie Kim:** I don't think we do.

**Daniel Lopes:** I purposefully try to avoid a catch-all like this.

**Jose Farias:** I agree.

**Jose Farias:** But we might.

**Daniel Lopes:** I don't think we do.

**Daniel Lopes:** We have niche solutions.

**Jose Farias:** So the thing with a fallback, though, is that it becomes kind of useless because, okay, say we categorize you into that, and then we treat you like any other workspace that does have a legitimate subcategory.

**Jose Farias:** Well, you're going to have charts, you're going to have prompts, and they're like...

**Jose Farias:** Because nothing makes sense.

**Daniel Lopes:** Yeah, right.

**Jose Farias:** Exactly.

**Jose Farias:** Nothing makes sense.

**Stevie Kim:** But wouldn't they select their own?

**Jose Farias:** That's the we have one.

**Jose Farias:** As long as we have one that matches.

**Jose Farias:** I think we have enough that would at least...

**Stevie Kim:** We have so many.

**Stevie Kim:** I would be surprised that...

**Jose Farias:** I mean...

**Jose Farias:** That's a good point.

**Stevie Kim:** You know, like, to be fair, we didn't have insurance, so I put that one in.

**Jose Farias:** So we have more than we have now.

**Stevie Kim:** Yeah.

**Jose Farias:** Okay so okay so moving past that I also took a look at something that I was going to send Daniel a message about.

**Jose Farias:** So you know how when you create an account or when you create a workspace, I say you clone a brand?

**Jose Farias:** That's the onboarding workaround.

**Jose Farias:** So what ends up happening is when you clone a brand, it clones it with all the subcategories because we have those joint tables.

**Jose Farias:** But then the workspace that's created, is not subcategorized.

**Jose Farias:** So there's this weird thing where it's like, okay, the brand is subcategorized, but the workspace is not.

**Jose Farias:** Well, then when you look at the charts in the overview, the workspace is not subcategorized, so nothing shows up.

**Jose Farias:** But that's like the first thing that a user sees when they log in.

**Jose Farias:** So that's the empty state.

**Jose Farias:** And that was actually why Estevão said we need to enforce subcategory selection during onboarding.

**Jose Farias:** That's really to prevent that edge case.

**Daniel Lopes:** Yeah, that makes sense.

**Daniel Lopes:** Makes sense.

**Daniel Lopes:** So now I understand the purpose of the...

**Jose Farias:** Yep.

**Daniel Lopes:** ...enforce during onboarding and make sure that when the user comes in, they've already set the subcategory.

**Daniel Lopes:** So that when they log in and they see the overview, there's data there.

**Jose Farias:** Yeah, and plus...

**Jose Farias:** Like, if we're moving towards the workspace being subcategorized, that becomes even more essential because if we start from there, then everything else is in place.

**Daniel Lopes:** Cool.

**Daniel Lopes:** That makes sense.

**Daniel Lopes:** Yeah, I understand now.

**Daniel Lopes:** Okay.

**Daniel Lopes:** So Estevão, maybe you can share more details about what you're working on?

**Estevão Mascarenhas:** Yeah.

**Estevão Mascarenhas:** So I had my Alright, so I had my work on, on the onboarding and I've been thinking about the billing system.

**Estevão Mascarenhas:** I'll talk about the billing system first.

**Estevão Mascarenhas:** So I've been thinking about it and I've been working on the billing system.

**Estevão Mascarenhas:** So the way that I'm thinking about it is that we have a user, and then we have a workspace.

**Estevão Mascarenhas:** Each workspace has workspace members who are invited into that workspace.

**Estevão Mascarenhas:** And then each workspace member also has an enrollment, which is the relationship between the workspace and the user.

**Estevão Mascarenhas:** So the thing that I'm working on is, you know, to prevent abuse like creating multiple free workspaces, one approach would be to add an "owner" boolean to the enrollment model.

**Estevão Mascarenhas:** So one free workspace ownership per user.

**Estevão Mascarenhas:** That's a constraint that we're thinking about.

**Estevão Mascarenhas:** So I'm working on the billing RFC and I'm also working on the onboarding.

**Estevão Mascarenhas:** So on the onboarding side, I have the cloning part working, but I still need to actually enforce the subcategory selection.

**Estevão Mascarenhas:** And I also need to remove some of the copy from the UI.

**Estevão Mascarenhas:** Like "we will notify you when ready."

**Estevão Mascarenhas:** So those are like the two main things that I'm working on, is enforcing subcategory selection and removing copy from the onboarding.

**Estevão Mascarenhas:** So I'm also thinking about it as... Actually, with the cloning approach, we're kind of blocking with the current approach.

**Estevão Mascarenhas:** Instead, we're kind of like... actually this is an interim approach.

**Estevão Mascarenhas:** It's a workaround, because the actual architecture change would be to have the workspace be subcategorized.

**Estevão Mascarenhas:** But in the interim, we're cloning the brand.

**Estevão Mascarenhas:** So that the user can access the app immediately while the deep research is happening.

**Estevão Mascarenhas:** And then at some point, when we move to the workspace being subcategorized, we can eliminate the need for cloning altogether.

**Estevão Mascarenhas:** So the workaround is really temporary.

**Estevão Mascarenhas:** Yeah.

**Estevão Mascarenhas:** Okay, great.

**Daniel Lopes:** Yeah, I understand.

**Daniel Lopes:** All right.

**Daniel Lopes:** Cool.

**Daniel Lopes:** So then for the manual QA, we need to pick 10 critical clients, and then you guys need to look at...

**Daniel Lopes:** Actually, hold on.

**Daniel Lopes:** Let me verify this because I want to make sure we're aligned on what the QA should look like.

**Daniel Lopes:** So the idea is to pick 10 critical clients and 5 new-account users.

**Daniel Lopes:** And go through and log each screen, and go check if things are working correctly.

**Daniel Lopes:** And for bugs, we're going to log each bug in Linear.

**Daniel Lopes:** Is that the idea?

**Leonardo Carpenedo Steffen:** Yeah, that's the idea.

**Leonardo Carpenedo Steffen:** Yes.

**Daniel Lopes:** Okay.

**Daniel Lopes:** And then we need to get started on this now.

**Daniel Lopes:** So, you guys have...

**Daniel Lopes:** Stevie, can you help with the 10 critical clients?

**Daniel Lopes:** Like, I think you have the list.

**Stevie Kim:** Yeah, I can definitely help with that.

**Stevie Kim:** I have a rough list. I can refine it quickly.

**Daniel Lopes:** Cool.

**Daniel Lopes:** And then for the new-account users, maybe we need to do a test sign-up?

**Daniel Lopes:** Yeah, I have a plan for that.

**Leonardo Carpenedo Steffen:** Yeah, I have a plan for that.

**Daniel Lopes:** Okay, cool.

**Daniel Lopes:** So then Leo, you're going to set up the Google Doc.

**Daniel Lopes:** Make sure you have the tabs for different test types, and then we start testing it as soon as we can.

**Leonardo Carpenedo Steffen:** Yeah, I'm going to set that up today.

**Daniel Lopes:** Cool.

**Daniel Lopes:** All right, next is Daniel.

**Daniel Lopes:** Can I talk about what I'm working on?

**Daniel Lopes:** So I have a few things in progress.

**Daniel Lopes:** I have the competitor visibility, the billing RFC, the MarTech stack evaluation.

**Daniel Lopes:** And actually, I've got to make sure I carve out time to check on the study probing data and monitor costs and adjust API keys if needed.

**Daniel Lopes:** And I'm also thinking about the infrastructure thing, which is like the migration of CheckThat workflows to a new framework and moving to a dedicated repo.

**Daniel Lopes:** And then I'm also thinking about the CDP and integrating Intercom via CDP or GTM layer.

**Daniel Lopes:** And then I've got the MarTech evaluation of Customer.io vs HubSpot.

**Daniel Lopes:** So there's like a lot there.

**Daniel Lopes:** But the thing is, the things that are directly pre-launch are like just manual testing and monitoring probing costs.

**Daniel Lopes:** Maybe verify that we're within the bounds for the API keys.

**Daniel Lopes:** And then the things that are post-launch are like MarTech stack, CDP, Intercom integration, and workflow migration.

**Daniel Lopes:** So I'm going to focus on the pre-launch things now and then tackle the post-launch things next week.

**Daniel Lopes:** And I also want to sync with Jason about HubSpot for email nurturing, specifically around event-based nurturing.

**Daniel Lopes:** Does HubSpot support event-based email nurturing?

**Jason Gong:** I think HubSpot has workflows that you can set up with event triggers.

**Jason Gong:** I think so.

**Daniel Lopes:** Okay, cool.

**Daniel Lopes:** Let me think about the time zone offset.

**Daniel Lopes:** So actually, let me find...

**Daniel Lopes:** Actually, I'm looking for the time zone offset for a scheduled time.

**Daniel Lopes:** Is that in the model?

**Daniel Lopes:** Actually, don't worry about it.

**Daniel Lopes:** I'll figure that out myself.

**Daniel Lopes:** Okay, cool.

**Daniel Lopes:** So I think that's pretty much it.

**Daniel Lopes:** Okay, so we need to focus this week on the manual testing and monitoring the study probing costs.

**Daniel Lopes:** And then next week we'll work on the MarTech stack and workflow infrastructure.

**Daniel Lopes:** So we're good.

**Daniel Lopes:** All right, I think that's a wrap.

**Daniel Lopes:** Thank you all.
