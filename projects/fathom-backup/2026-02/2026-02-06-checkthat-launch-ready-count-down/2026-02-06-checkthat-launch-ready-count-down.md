# CheckThat: Launch Ready Count Down

<metadata>
date: 2026-02-06
time: 16:00 UTC
duration: 50 minutes
organizer: Stevie Kim (stevie@growthx.ai)
participants:
  - Marcel Santilli (marcel@growthxlabs.com) - Founder/CEO, CheckThat
  - Daniel Lopes (daniel@growthxlabs.com) - Content OS Lead, CheckThat
  - Jason Gong (jason@growthx.ai) - Growth/Sales, GrowthX
  - Pedro Steimbruch (pedro@growthx.ai) - Backend Engineer, GrowthX
  - Jose Farias (jose@growthx.ai) - Infrastructure/DevOps, GrowthX
  - Estevão Mascarenhas (estevao@growthx.ai) - Frontend Engineer, GrowthX
  - Leonardo Carpenedo Steffen (leonardo@growthx.ai) - Product/Engineering, GrowthX
  - Stevie Kim (stevie@growthx.ai) - Product Lead, GrowthX
fathom_recording_id: 120412607
fathom_url: https://fathom.video/calls/557658561
share_url: https://fathom.video/share/KUr5d2crLzjs3ThHSVceNemxvNAxRFFq
source: fathom
enriched_on: 2026-02-27T18:45:00Z
</metadata>

---

## Summary

The team reviewed post-launch metrics and identified four critical blockers: onboarding failures from empty workspaces (caused by missing leaderboard tags), broken analytics tracking (event_checkout_completed logging incorrectly), Customer.io US migration (email zones tied to accounts not workspaces), and impersonation compliance gaps (lacking logging and expiration controls). Action items were distributed across the team to fix these immediately while deferring non-critical category/workflow improvements to next week.

---

## Context

CheckThat soft-launched on February 5, 2026. The launch showed weak signup volume but did stay online (a priority for Jose's infrastructure work), with ~67 people bouncing during onboarding. Early positive signals emerged: 13 accounts already changed competitors post-launch, and 13 changed their assigned prompts, suggesting meaningful user engagement beyond signup. Jason Gong is driving new user acquisition through manual outreach and demo calls, requiring high-quality onboarding and category selection to avoid friction. The team is operating in post-launch stabilization mode, prioritizing P1 (critical blockers) and deferring feature requests to next week. GrowthX is playing a support/operations role (email, customer success, growth) while CheckThat's content team (Marcel, Daniel) focuses on prompt curation and category definition.

---

## Relevance

- **Product/Engineering (CheckThat):** Empty workspace bug and category selection friction are top UX issues affecting onboarding completion and user activation.
- **Infrastructure/DevOps:** Jose needs to finalize cadence optimization (will halve spend), monitor the race condition fix deployed, and maintain weekend coverage.
- **Growth/Sales:** Jason is driving customers and needs category/competitor selection to work smoothly; incorrect selection is a major blocker for his demo calls.
- **Backend Engineering:** Pedro must complete Customer.io US migration and manage impersonation feature compliance.
- **Frontend/Analytics:** Estevão owns onboarding bootstrap fix, subcategory filtering, and event tracking (onboarding-complete event).
- **Product Leadership:** Stevie is organizing the post-launch backlog, creating a categories/brands decision doc, and managing feature requests vs. stabilization priorities.
- **Content/Curation:** Marcel and Daniel own category definitions and prompt curation; category accuracy directly impacts new user experience and product viability.

---

## Overview

- **Onboarding is a critical blocker.** A bug creating empty workspaces and the difficulty of fixing a wrong category selection are the top user-facing issues.
- **Analytics tracking is broken.** The `event_checkout_completed` event is incorrectly logging signups, showing 0 conversions. A new, accurate event is required to fix the dashboard.
- **Customer.io is migrating to the US.** This move is required because email zones are tied to individual accounts, not workspaces. The new US campaign needs Jason's review before go-live.
- **Impersonation is live but needs controls.** The new feature lacks logging and expiration, creating a regulatory risk (especially in Europe) and requiring a formal access policy.

---

## Key Topics

### Onboarding & Workspace Issues

  - **Empty Workspaces Bug:**
      - **Problem:** New users get empty workspaces because \~2,000 shared library prompts added after November lack the `leaderboard` tag. The onboarding logic incorrectly relies on this tag to bootstrap workspaces.
      - **Fix:** Estevão will modify the bootstrap process to add *all* active shared library prompts, ignoring the tag for now.
  - **Empty Subcategories:**
      - **Problem:** Marcel is creating new subcategories, which can appear in the onboarding dropdown before prompts are added, leading to a poor user experience.
      - **Interim Fix:** Estevão will hide subcategories from the dropdown if they contain no prompts.
      - **Long-Term Fix:** A "draft/publish" status for categories is needed to prevent this.
  - **Incorrect Category Selection:**
      - **Problem:** Users get stuck if they select the wrong product category, as there's no way to change it. This is a critical issue because the entire product experience depends on this initial choice.
      - **Solution:** Stevie will create a doc today outlining the problem and potential solutions, including:
          - An "escape hatch" in onboarding to flag incorrect categories.
          - Inferring categories from competitor selections.
          - Using mention data to suggest categories.
      - **Rationale:** Jason is driving new users, and this issue is a major source of friction.

### Analytics & Tracking

  - **Broken Signup Conversion Funnel:**
      - **Problem:** The `event_checkout_completed` event is incorrectly used to track onboarding completion, causing the dashboard to show 0 conversions.
      - **Solution:** Estevão will add a new, accurate event for onboarding completion.
  - **User Behavior Insights:**
      - **Finding:** Users are actively engaged post-onboarding.
      - **Metric:** \~13 accounts have changed their competitors, and \~13 have customized their prompts.

### System & Infrastructure

  - **Customer.io US Migration:**
      - **Problem:** Customer.io's email zones are tied to individual accounts, not workspaces, requiring a US instance to send emails from the correct region.
      - **Status:** Pedro has created a US account, cloned the welcome campaign, and connected RudderStack.
      - **Action:** Jason must review the new US campaign before go-live.
  - **Impersonation Feature:**
      - **Status:** Pedro implemented a quick impersonation feature for Marcel to view user workspaces.
      - **Risk:** The current implementation lacks logging and expiration, creating a regulatory risk, particularly in Europe.
      - **Action:** A formal access policy is needed.
  - **Weekend On-Call:**
      - **Decision:** No formal rotation is needed yet. The team will use informal communication to ensure coverage.

---

## Action Items

**Estevão Mascarenhas (GrowthX - Frontend/Analytics)**
- Fix onboarding analytics: add onboarding-complete event; update dashboards; document first pageview; add library/custom prompts
- Update bootstrap: add all shared library prompts to workspaces; ignore leaderboard flag
- Post to Daniel/Marcel: confirm leaderboard definition
- Filter onboarding subcategory dropdown to show only subcategories w/ prompts

**Stevie Kim (GrowthX - Product Lead)**
- Fix onboarding analytics: add onboarding-complete event; update dashboards; document first pageview; add library/custom prompts
- Review impersonation compliance/security; consult legal if needed
- Create categories/brands doc; share w/ Daniel, Marcel, Jason

**Jose Farias (GrowthX - Infrastructure/DevOps)**
- Finish cadence optimization to halve spend

**Jason Gong (GrowthX - Growth/Sales)**
- Review Pedro's US Customer.io welcome campaign; approve; then execute US cutover checklist

---

## Transcript

**Jose Farias:** Hey, good morning. Hello.

**Pedro Steimbruch:** Hey, guys. You. So what was the feeling yesterday after?

**Jose Farias:** I think it went okay from a technical perspective anyway.

**Stevie Kim:** I don't think we got too many signups.

**Jose Farias:** Do you know the feeling there, Stevie? Did we expect more or was it on par?

**Stevie Kim:** I don't know what the expectation was, but we definitely didn't get a ton, especially. So I'm going to put together a board. I already have a dashboard, actually. I've never had like all these analytics. I've always worked on on-prem, air-gapped environments. I never had a ton of data on my users, so it was always user interviews. So this is kind of fun for me. I've put together an activation and a sign-up conversion rate funnel. So unfortunately, there weren't a lot of people going through the sign-up onboarding flow. I guess nobody converted in the last 24 hours.

**Pedro Steimbruch:** I think, I'm not sure, because I can see some events on customer.io. A lot of welcoming mails going out.

**Stevie Kim:** Because yesterday, if I show the last seven days, there were like three people that converted yesterday. I don't know why this isn't showing anymore. I'm looking at the wrong chart. So activation is later on. This is the signup conversion chart. So it still shows zero people converted and 67 people bounced. But I know I watched recordings of signups, so something's iffy with the tracking. I'm using the event checkout completed, which is one Daniel put in. So something's not right there.

**Estevão Mascarenhas:** Yeah, this one is when someone completes the Stripes checkout. So it's only for paying. I don't know if you have one that represents the completion of the onboarding. I can add it.

**Stevie Kim:** That would be great. Let me know what it's called and I'll swap that. This is the product analytics dashboard. Feel free to create your own or add to this. That's kind of what I'm tracking.

**Pedro Steimbruch:** I would say that 10% visiting or going through the onboarding is a great rate. We have more than 5% conversion rate. What's the first event, the page view?

**Stevie Kim:** I cannot remember. I'll have to look at the show details. I'll have to look at it because I don't remember offhand. I'll put a description in there. We have accurate visibility to the database.

**Jose Farias:** Sorry, I interrupted, but I was looking at the database. This might be interesting. Just confirming we didn't have any paid upgrades. There's one account that's paying, it's Marcel's. So I don't think that counts. Yesterday I was mostly watching dashboards and making sure stuff stayed online. Fortunately the data intensive stuff held up pretty well. I have some data about how customers are using it. Competitor changes are about as common as changing your prompts in bulk. Some amount of people, like 13 at least, are changing their competitors actively. About 13 accounts changed their prompts after onboarding. That's good. I'm having a hard time fully mentally committing to any one task because my brain is always like, we're launching, watch the dashboards, are we still online? So I'm a little bit slow, but I think it's worth it. This needs proper attention.

**Stevie Kim:** That's good. I expected the competitors, to be honest. I fiddle with those more than the prompts. That's really good that you saw 13. That's part of the activation I'm trying to capture. I'm differentiating between library prompts and custom prompts. I feel like we need to finish the cadence stuff because it'll half our spend. There's some workflows that need to be done or improved for the growth side next week. I haven't used the new output workflows yet. I should dig into that codebase. I'll just focus on it today.

**Jose Farias:** Sounds good. So yesterday, I looked at some of the Sentry stuff that was worrying. Nothing too big. Estevão and I collaborated on a bug that could impact sign-ups. We have what we suspect is a race condition. Some users might have had the app crash during onboarding. Not too many people, fewer than three. That's the only bug that actually impacts signups. Other than that, we got some feature requests. I think we can start tackling those. Nothing critical on my radar.

**Estevão Mascarenhas:** So that's good.

**Stevie Kim:** And honestly, one of those was already in the customer.

**Jose Farias:** Yeah, Webflow. Yeah. So that was a different bug. The 404. Yeah, so one was caused by an outage. This one seems different. I'm optimistic that Estevão's fix should work. We'll keep an eye on it.

**Pedro Steimbruch:** Yeah, I tackled some requests from yesterday this morning. I worked on the US customer.io setup. It's done. Apparently, we were sending emails from Europe. I created an account on my email because I couldn't with the team's email. The zone is tied to the account, not the workspace. I cloned the campaign, imported the users, connected to RudderStack, and we're receiving events already. I want someone, maybe Jason, to review the campaign and confirm we can start sending from there. Then we need a checklist to turn off Europe and start using the US instance. Remove DNS entries from Cloudflare for the Europe instance. I checked page generations that SESC reported. I implemented a seven-day moving average for prompt show page charts. Did the impersonate feature. I think that was a quick way. It took less than an hour. Now Marcel can check how workspaces look. I pinned the brand to the prompt show page. I fixed the Google AI overview that was introduced after the migration. I'm about to push improvements to the probe details page. I will wrap up for today.

**Jose Farias:** Great work. Real quick about the impersonation. I think that's fine. I agree with your reasoning. The thing to watch out for is regulatory stuff. We were adamant about compliance with customer.io. This has big security implications because any admin can impersonate right now. That's Europe that's more particular about that. I'm not a fan of impersonating but it's common. Any thoughts?

**Stevie Kim:** We did this a lot at Algorithmia and DataRobot. Typically we'd get close relationships with customers and ask permission. As an admin, you can go into anyone's workspace and not impersonate them. There's a lot of weird things we can do that probably aren't great for European law. But everybody does it because it's hard not to. I can dig into that to make sure there isn't anything glaringly obvious.

**Jose Farias:** Yeah, that's usually accompanied by access logs and registering like, hey, you're going to impersonate, tell me why first. We haven't built any of that. I don't think that's a regulatory risk in the US.

**Stevie Kim:** I don't think but I'm not a lawyer, so I can't make an actual suggestion there. I know some folks.

**Estevão Mascarenhas:** In the past, this kind of impersonation work with certification or regulatory enforcement usually requires a flow where you request, someone requests Y, it usually has an expiration and gets logged. I agree, it's fine. It's just that I feel we never stopped to think about how admins should access workspaces. For example, customers have other admins enrolled to their workspace. That's bad. If they go to their user tabs, they'll see everyone from growthx there. I think we need to figure that out. Can we clear that at some point?

**Stevie Kim:** Well, as long as it's the trial period, I don't mind. They haven't paid us and they're getting all this for free. Once they convert, then we definitely need to convert them to an owner instead of just a member. We need to remove all growthx admins.

**Estevão Mascarenhas:** Yeah, that's fine. I have the feeling this regulatory need will come from a big enterprise customer at some point. Like, hey, do you have this? The amount of money I want to spend with you guys. Yeah, you don't have it.

**Stevie Kim:** It's always just a checklist.

**Jose Farias:** Yeah. Okay. So I think we can figure out when that happens.

**Estevão Mascarenhas:** So I'm currently checking something. I posted on the channel. We had 2,000 prompts added to subcategories. The shared library ones weren't being added to workspaces because at some point in November, we added the leaderboard tag flag to prompts. In the migration, we set all active shared library prompts to leaderboard. But we don't tag any other prompts added after that with that flag. So what I'm going to do, since we don't have logic around what is a leaderboard, is change the bootstrap operation to add all shared library prompts to the user workspace. I'll post a message to Daniel and Marcel because I think Daniel did this. I recall we discussed that we only wanted awareness and evaluation prompts to be leaderboard. I'll confirm that. I'll ignore that flag for now so we don't run into empty workspaces again. I'll filter out subcategories in the onboarding that have no prompts available. I'm trying to protect from that happening. Someone might be onboarding just when someone creates a subcategory, so I want to prevent an empty subcategory from being picked and leading to an empty workspace.

**Jose Farias:** So Stevie, are we creating new subcategories at this point?

**Stevie Kim:** I'm refusing to, to be honest. There's too much risk right now. I've dedicated time to sit down and do it to make sure all the prompts and competitors are there. It's just not a good time. I'm telling the delivery team, the people asking for subcategories, let's not do that until after launch. I don't want any empty categories with empty dashboards. I think next week is when I'll complete requests from the delivery team, if all is well.

**Estevão Mascarenhas:** Yeah, like after standup, Marcel just sent a message saying he was planning to add subcategories. The feeling I have is we're going to need some kind of status for a category, like draft and publish. So people can configure the category with all the prompts, then click publish, and it gets available to the public. But as a stopgap, I can just hide those categories for now.

**Stevie Kim:** That'd be great. Are you going to manually hide the ones Marcel's creating until they're ready?

**Estevão Mascarenhas:** No, I'm going to put a check to not list any subcategories that have no prompts on that dropdown. But if someone is adding prompts one at a time, if someone happens to be onboarding, it might start a workspace with just one or two or three prompts. But until we have this publishing flow for categories, I think maybe that's fine.

**Stevie Kim:** Another issue is it's not just the prompts, it's the amount of brands in that subcategory. If there's one brand in a subcategory, that isn't great either. But it doesn't sound like Marcel's super concerned unless he's going heads down on it in one chunk of work. He did the lovable one, the vibe code one. He just put lovable, and that's been in there for a few days. That has a single brand, but yeah, it doesn't look good for us. If we can put some checks and not show those, that'd be great.

**Estevão Mascarenhas:** Yeah, I think even if the user finds an issue, it's not blocking because in the competitors part, when they search for a competitor, we show all brands we have in our catalogue. We don't filter by subcategory, so they can pick whatever brand we have. For the prompts, they can go to the prompt library page and add those manually. Yeah, I've already used that impersonation today to view the workspace that Stevie mentioned yesterday that was empty. That worked really nice. Just starting my update. I'm currently checking something. I posted on the channel. I'm a bit lost what I'll do next, but I'm going to pick from the P1 Stabilize Week. I think P0 is done. The issue that Jose mentioned about the crash, it's a weird thing, just in production for a few users. I pushed the fix, I'm monitoring it, I marked those as resolved in Sentry so if it comes back I'll be pinged. Should we maybe just informally discuss an on-call rotation? I'll be around tomorrow, but Sunday I'll be out without internet. I don't think we need a formal thing like PagerDuty for now. I think just communicating is fine.

**Jose Farias:** I agree. We don't have a big influx of users yet. So as long as someone is online, that's probably enough. I'll be around this weekend. We can over-communicate. I just want to prevent all of us going out and it being a coincidence. But it can happen.

**Estevão Mascarenhas:** Yeah, I'm finished. Thanks.

**Pedro Steimbruch:** Yeah, I just want to mention that you don't know exactly what to work on, and the post-launch backlog is bloated. We have so many things there. Maybe we should prioritize there.

**Stevie Kim:** That's one of things I wanted to ask today. I've been in the backlog weeds. I wanted to see what you guys wanted to do. We can create new labels or repurpose existing ones. Everything's going to be post-launch at this point. Maybe next week we start looking at workflows that need improvement for the growth side of things. Anybody can take them. They're pretty lightweight for the most part. Yeah, I'll just state the problem and have all these different ideas, assumptions we're making. I'll get that done today. Not going to do a heavy multi-page PRD. I'll share it Monday and maybe that can be our discussion for that second meeting with Marcel and Daniel. I'll share it as soon as I get the scaffolding done so everyone can contribute.

**Estevão Mascarenhas:** Yeah, awesome. Yeah, just to be clear, we still have a lot of tasks on P1, so I'm planning to tackle those in order. I don't see a specific task that needs attention now, so just follow that to-do column.

**Pedro Steimbruch:** I have one more thing to flag for Jason. I migrated customer.io to the US instance. I would like you to review the campaign I created there. I tried to copy and paste it. There's no export and import, so I did it manually. We are sending welcome emails, right? You said you guys were doing that manually yesterday, but actually customer.io is sending welcome emails from Europe.

**Jason Gong:** Oh, it was actually working yesterday? And running?

**Pedro Steimbruch:** Yes.

**Jason Gong:** Don't tell Yusuf.

**Pedro Steimbruch:** Yeah, so I have a checklist for us to start working with the US. I just want you to review the campaign and give me the thumbs up that we can start sending emails from there.

**Jason Gong:** Okay, cool. And then I'll go through the checklist to disable Europe and enable US. Sounds good. Thanks, everyone.

**Jose Farias:** That's good. Real quick, it seems like Marcus merged that internal app URL thing again. Just want to make sure or it's not the same thing?

**Pedro Steimbruch:** Just checking it.

**Jose Farias:** Nice. What was the difference? Just curious. Because I know we tried that last time and it didn't work.

**Pedro Steimbruch:** The last time the internal app URL was HTTPS. Because if we do, need to have a certificate on that internal domain. I think it's okay.

**Jose Farias:** Because it's like internal.

**Pedro Steimbruch:** It's internal. Yeah.

**Jose Farias:** Right. I think that's it.

**Stevie Kim:** Yeah, and just let me know, especially as we're post-launch, what you guys need from me for support. If things are too chaotic or unprioritized or if you're not getting enough context on tickets, just let me know and I'll try to smooth things. Great work on checking the sessions. I started doing that at the beginning, but when I got heads down on issues, I stopped. This issue you found about the empty workspace, I think it was critical. You only could've found it by watching the sessions. I watched way too many of those. I started playing an audiobook because it was like, oh my God, I can't watch this onboarding one more time. But yeah, you can get cross-eyed pretty quick.

**Jason Gong:** Did anything stand out there? Because what Nigel and I are doing now is just reaching out to companies that seem more legit to help them actually set it up. Is it clear what we're prioritizing, like make it better? Yeah, I mean, there's just some little things. We already knew about them. We couldn't get to them right away for the launch. Nothing huge is standing out. The thing that's still probably the number one thing, just from using it myself and showing to customers, is if you don't get the sub, the product category right because either we don't have it or they're misplaced, that's the one place that gets stuck. The whole product builds on top of having the right data. If you don't get that right or we don't have it, it feels broken. We've done a lot of thinking around that. We don't want to let them switch it but there's improvements we want to make on the workflow itself. The workflow that matches the brand. There's no workflow that creates new categories. Okay. Do you know if anyone's working on that or if that's a ticket or if Marcel's here? No. I think it's in the back of all our heads. I might've created a ticket for it this week. I've been digging into the workflows to understand exactly how they're working and where we could make improvements. But I haven't had much time. But yeah, there's we know it's an issue. I don't think there's a super easy silver bullet for it. So I just want to add that while there are complexities to implementing that, they're mostly like product decisions, right? Like, we can do it. But it's just that the whole product changes from under you, right? So there's like, do we remove all your prompts and switch them to the proper category? What do we do with your competitors? Like that kind of thing. And yeah, just product questions that need answering. It does seem to me that we should prioritize it a little bit. I think because it's in the back burner and I agree with Jason that the product relies on this. So maybe we should prioritize that over other things. Okay, I can spend some time on that. I have a feeling Daniel and Marcel are going to have a lot of opinions on this. So that's kind of why it hasn't gotten the attention because they've been hyper-focused on ContentOS. So I'll get something started so at least it gives them something to look at and they can say, wait, no, this is totally the wrong direction. I guess the only thing for me is I feel like we're coming at it from parallel work streams. Marcel showed me something he was noodling on that attempted to just map more categories in general. But I think that's just stuck. It's not really done. He doesn't have time. I'm working on a version where we're literally asking these companies, hey, come on a call and we'll show you what this product's about and what your roadmap for optimizing AI visibility looks like. So we have to manually do all that work. Figure out, are you in the right category? We'll make a new workspace. Then we'll just manually using whatever Claude pick 200 custom props for you. Then we'll create the category if it doesn't exist. So we'll probably learn a bunch from doing that. And then it also sounds like you have a couple of tickets. I don't know. I guess some way I think that's way to just in the back of my head. But yeah, as I said, I'll put together some kind of doc. It won't be super heavy but any learnings you're gaining from talking to people, the only thing I would just throw in however you can is like an escape hatch where they can at least flag or say like that is the issue. I don't know where it is. Like if it's an onboarding on that screen, if they can't find something, because when I was going through that, I felt stuck because I had to click the X or unintuitively pick something that doesn't match what I have in my head. Like if I'm a product marketer, it's like almost blasphemy to pick a different category. So it's very unlikely somebody will just do that. Like, oh, cool, this is close enough. Click it. So you need an escape kind of path there to say like none of these match and then just type in something to have it either there or somewhere in the product. And I think that can be a band-aid until we figure this out because at least that tells us like if people are running into this a lot. Because I'm literally spending thousands of dollars driving new users and if this is like a more important issue or not.

**Stevie Kim:** They're not getting stuck in the onboarding phase on selecting categories. They actually spend more time on competitors. So we're going to actually cap the number of competitors because they get, they just spend forever. Like they want to track every competitor it seems like. So yeah, they actually spend less time on the category section. But yeah.

**Jason Gong:** I think I did have one ticket where like if you flip that around and pick competitors first, maybe we could just infer the category because it's interesting they spend more time on the competitor page.

**Estevão Mascarenhas:** Yeah, that's an interesting idea.

**Stevie Kim:** Yeah, it is. It's been interesting to hear even from current customers what category they want to be in because it's not always the one their competitors are in. But I'm also not exactly sure. I'm not talking directly to them. So it could be information filtered down that maybe something got lost in translation. But yeah, that's kind of an interesting thought.

**Estevão Mascarenhas:** Yeah, I think the issue is we won't be able to today. We show the competitors based on the category. So with all the categories, I don't think we have anything else to show relevant competitors. We're just going to show a mess of a list with our brands. Yeah.

**Jason Gong:** I mean, I do know you run that deep research at the beginning, right? Or maybe that happens after you pick competitors, but I'm sure that just tells you who the competitors are. It's going to be fairly accurate. But anyway, I'm not trying to find a solution. I think the two things, like one, I guess we need a process to make the index better and onboard and see what the right info is. Then two, I think people, it's going to be impossible to get absolutely everything right. And they need like some path to either fix it themselves or flag it for us. Like in any case, we'll need both of those things. So I'm going to work on the former because we're going to jump on a bunch of calls. And then I think the latter would be really helpful as I'm driving more people.

**Pedro Steimbruch:** Yeah, I just want to flag out today morning I replied to someone in Intercom asking to change their category.

**Stevie Kim:** Oh, yeah. Yeah. No, it's as we've known. I mean, Jason, you and I have talked about this for a couple of weeks now. And it's just something that we couldn't tackle for the launch. But yeah, it's a known issue. I'll get something together. I'll just focus on it today. I think one nice idea is it's a layer of things, right? I think the most reliable ways to determine the category based on mentions, right? The prompts that gather more mentions for a specific brand, we see from where these prompts are. And that's the category we should. Because at least they will see the dashboard as full. That's why I mentioned it's a layer of things. Then I think what Jason suggested is it's very interesting to infer the category based on the competitors they choose. These are good ideas. Yeah. Just to add that, Jason and Stevie showed earlier this meeting the funnel of the onboarding process. So I think we'll be clear when there's a drop, like there's churn in a certain step of the onboarding. That's great. And I was going to suggest, I know that I never worked with PostHog, but it has experiments, and I think we should start looking at that, because if we change the onboarding, we should always be optimizing it, right? So be more data-driven now that we have something in place. But I agree Stevie, I saw Daniel working on workflows that I think he was trying to tackle how to categorize brands. It was like in the output channel, maybe he was just exploring. I think it's worth checking with him. Yeah, just to add that our subcategorization isn't great. I was testing it a lot since the beginning. This was one of the first things that we didn't check that, and we definitely need to improve it. But I think he's tackled that. Yeah, that's why it'll be helpful to put everything in a doc, everybody's ideas, basically.

**Stevie Kim:** It's just, I'll state the problem and have all these different ideas and assumptions we're making. I'll get that done today. I'm not going to do a heavy multi-page PRD. Then I can share it out for Monday, and maybe that can be our discussion for that second meeting because it has Marcel and Daniel in it. I'll try to share it as soon as I get the scaffolding done so everyone can contribute. Sound good?

**Estevão Mascarenhas:** Yeah, awesome.

**Pedro Steimbruch:** Yeah, I have one more thing to flag out for you, Jason.

**Jason Gong:** Thanks, everyone. Everyone. Thanks, everyone.

