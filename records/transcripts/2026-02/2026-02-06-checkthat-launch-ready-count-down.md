# CheckThat: Launch Ready Count Down

<metadata>
date: 2026-02-06
time: 16:00 UTC
duration: 50 minutes
organizer: stevie@growthx.ai
participants: Jason Gong, Pedro Steimbruch, Jose Farias, Estevão Mascarenhas, Leonardo Carpenedo Steffen, Stevie Kim, Marcel Santilli, Daniel Lopes
fathom_recording_id: 120412607
fathom_url: https://fathom.video/calls/557658561
share_url: https://fathom.video/share/KUr5d2crLzjs3ThHSVceNemxvNAxRFFq
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

CheckThat launched the day before this meeting, and the team gathered to assess performance and tackle critical blockers. Post-launch numbers were lower than expected — the dashboard showed zero conversions due to broken analytics tracking — but the team identified the root cause: new users are getting empty workspaces because the onboarding bootstrap process relies on a `leaderboard` tag that ~2,000 newly added prompts don't have. The team also prioritized three other high-impact issues: incorrect category selection creating a stuck user experience, Customer.io's need to migrate to a US instance for email zones, and the impersonation feature lacking security controls. Estevão committed to fixing the analytics and bootstrap logic immediately; Stevie will document the category selection problem and potential solutions; Jason will review the US Customer.io campaign; and Jose will finish cadence optimization to reduce infrastructure costs.

---

## Context

CheckThat is GrowthX's strategic bet — an AI visibility index for B2B competitive research. The product launched on February 5, 2026, with a focus on making it easy for users to research competitors and customize AI prompts by industry. The team consists of GrowthX engineers (Estevão, Leonardo, Jose, Pedro) and growth/product leadership (Stevie, Jason). Marcel Santilli is the CheckThat founder and CEO overseeing product strategy, and Daniel Lopes is also involved in product decisions. This was the immediate post-launch check-in: the team had ~24 hours of real user data and needed to understand what was working, what broke, and what to fix first to unblock the user experience.

---

## Relevance

**To CheckThat Product & Launch:**
- Onboarding is the critical path to user retention. Empty workspaces and inability to change category selection are deal-breakers that will kill conversion rates and user activation metrics.
- Analytics visibility is broken: the `event_checkout_completed` event is misconfigured and showing zero conversions when ~13 accounts have actually engaged post-onboarding (changing competitors, customizing prompts). Estevão must fix this before scaling acquisition.
- Category matching is a product design problem, not just a UX fix. The team identified three potential solutions: an "escape hatch" in onboarding, inferring categories from competitor selections, or using mention data to suggest the right category. This needs priority given Jason is driving new user acquisition.

**To GrowthX Infrastructure & Operations:**
- Customer.io's email zone architecture (zones tied to accounts, not workspaces) creates a hard requirement for a US instance. This is blocking email deliverability in the US and needs Jason's approval before the US cutover can execute.
- Impersonation feature (used by Marcel to view user workspaces for support) lacks logging, expiration, and formal access controls. This is a regulatory risk, especially in Europe, and requires legal review and a formal policy before the product scales.
- Jose's cadence optimization work is critical for controlling infrastructure spend as the product scales with more users.

**To GrowthX Growth & Operations:**
- Weekend on-call coverage is not yet formalized but the team will use informal communication. This approach works for now but will need structure if user volume grows.

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

**Estevão Mascarenhas**
- Fix onboarding analytics: add onboarding-complete event; update dashboards; document first pageview; add library/custom prompts
- Update bootstrap: add all shared library prompts to workspaces; ignore leaderboard flag
- Post to Daniel/Marcel: confirm leaderboard definition
- Filter onboarding subcategory dropdown to show only subcategories w/ prompts

**Stevie Kim**
- Fix onboarding analytics: add onboarding-complete event; update dashboards; document first pageview; add library/custom prompts
- Review impersonation compliance/security; consult legal if needed
- Create categories/brands doc; share w/ Daniel, Marcel, Jason

**Jose Farias**
- Finish cadence optimization to halve spend

**Jason Gong**
- Review Pedro's US Customer.io welcome campaign; approve; then execute US cutover checklist

---

## Transcript
**Jose Farias:** Hey, good morning.

**Jose Farias:** Hello.

**Pedro Steimbruch:** Hey, guys.

**Pedro Steimbruch:** You.

**Pedro Steimbruch:** So what was the feeling yesterday after?

**Jose Farias:** I think it went okay from a technical perspective anyway.

**Stevie Kim:** I don't think we got too many signups.

**Jose Farias:** Do you know the feeling there, Stevie?

**Jose Farias:** Did we expect more or was it on par?

**Stevie Kim:** I don't know what the expectation was, but we definitely didn't get a ton, especially, yeah.

**Stevie Kim:** So, I mean, I can't remember.

**Stevie Kim:** I'm going to put together a board.

**Stevie Kim:** I already have like a dashboard, actually.

**Stevie Kim:** And if I can find out where I'm at here with all my windows and tabs and all that.

**Stevie Kim:** But where did it go?

**Stevie Kim:** There it is.

**Stevie Kim:** I've never had like all these analytics.

**Stevie Kim:** I've always worked on on-prem, air-gapped environments, and all that fun stuff, for the most part, with some managed cloud, but I never had a ton of data on my users, so it was always a lot of user interviews.

**Stevie Kim:** So this is kind of fun for me.

**Stevie Kim:** So I'm kind of figuring out what to track, and so this will probably change.

**Stevie Kim:** But I've put together, like, an activation and a sign-up conversion rate funnel.

**Stevie Kim:** Oh, I think, yeah, I've got it just for today.

**Stevie Kim:** Let's just do, like, the last 24 hours.

**Stevie Kim:** So, yeah, unfortunately, like, yeah, there weren't a lot of people that even went.

**Stevie Kim:** soon.

**Stevie Kim:** Through the sign-up, the onboarding flow.

**Stevie Kim:** Wait, this isn't right, because yesterday, oh, I guess it was, yeah, at night.

**Stevie Kim:** Yeah, so I guess nobody converted in the last 24 hours.

**Pedro Steimbruch:** I think, I'm not sure, because I can see some events on customer.io.

**Pedro Steimbruch:** A lot of welcoming mails going out.

**Pedro Steimbruch:** Welcoming mails, not sure.

**Pedro Steimbruch:** Oh, you're welcoming mails.

**Stevie Kim:** Because yesterday, like, so if I show the last seven days.

**Stevie Kim:** Oh, okay, so yesterday, okay, this is weird, because yesterday for, I had it showing in the last 24 hours, and there were, like, three people that converted, so I don't know why this isn't showing anymore.

**Stevie Kim:** So I'll have to check that out, because this did used to show that a couple of people.

**Stevie Kim:** you yeah.

**Stevie Kim:** So, love it.

**Stevie Kim:** So, yeah.

**Stevie Kim:** And

**Stevie Kim:** Oh, I'm sorry.

**Stevie Kim:** I'm sorry.

**Stevie Kim:** I'm looking at the wrong chart.

**Stevie Kim:** So activation is later on.

**Stevie Kim:** This is the one I should be looking at, the signup conversion.

**Stevie Kim:** Yes.

**Stevie Kim:** Good morning.

**Stevie Kim:** Let's have some coffee.

**Stevie Kim:** Yeah, my bad.

**Stevie Kim:** So anyway, okay.

**Stevie Kim:** So yeah, so this is the signup flow.

**Stevie Kim:** And I've broken it into, you know, the different steps.

**Stevie Kim:** Same with the page view time.

**Stevie Kim:** Like, up here, I wanted to see, like, how long people, the average time spent on each stage of the onboarding flow.

**Stevie Kim:** I don't know how helpful it will be.

**Stevie Kim:** But yeah, it still shows that there were zero people that converted and 67 people bounced.

**Stevie Kim:** But I, I know, I mean, I watched signup.

**Stevie Kim:** I watched recordings of.

**Stevie Kim:** So something's iffy with the tracking here, and I'll figure that out.

**Stevie Kim:** But I am using the event checkout completed.

**Stevie Kim:** So, yeah, that's one of the ones that Daniel had put in.

**Stevie Kim:** So something's not right there.

**Estevão Mascarenhas:** Yeah, this one is when someone completes the Stripes checkout.

**Estevão Mascarenhas:** So it's only for paying once.

**Estevão Mascarenhas:** I don't know if you have one that represents the completion of the onboarding.

**Estevão Mascarenhas:** I will check that, but I can also add it.

**Estevão Mascarenhas:** Yeah, that would be great.

**Stevie Kim:** And just let me know what it's called, and then I'll swap that.

**Stevie Kim:** So, yeah, so the activation one is further on.

**Stevie Kim:** you've already come, like, see that this is what's funny.

**Stevie Kim:** Like, this is showing, like, they completed.

**Stevie Kim:** organized.

**Stevie Kim:** For of a thing it's it's think

**Stevie Kim:** It's the, yeah, I can't remember what event it is, but it's basically the last step of the onboarding flow.

**Stevie Kim:** So it's wonky there.

**Stevie Kim:** So maybe I could just put that there.

**Stevie Kim:** Anyway, the completed, I don't want to take the whole statement.

**Stevie Kim:** But anyway, this is the product analytics dashboard.

**Stevie Kim:** Feel free to create your own or add to this.

**Stevie Kim:** And, yeah, or anything that you want me to set up, I can set up.

**Stevie Kim:** But that's kind of what I'm tracking.

**Stevie Kim:** So that's not bad, you know, and I don't know what's expected.

**Stevie Kim:** As I said, like, this is a new area for me, so I don't know what's typical for more the TLP side.

**Pedro Steimbruch:** I would say that 10% that is visiting or going through the onboarding is a great rate.

**Pedro Steimbruch:** Yeah, think it's a great percentage of people that are clicking and sign up.

**Stevie Kim:** Yeah.

**Pedro Steimbruch:** Yeah, we have more than 5% conversion rate.

**Pedro Steimbruch:** What's the first event, the page view?

**Pedro Steimbruch:** Which page view is that one?

**Stevie Kim:** I cannot remember.

**Stevie Kim:** I'll have to look at the show details.

**Stevie Kim:** don't think it really, oh, it doesn't say, oh, yeah, I'll have to look at it because I don't remember offhand and I'll, I'll put a description in there because if I don't remember it after creating it in two days, yeah, I don't know, I'll figure that out.

**Stevie Kim:** I'll get this all a little bit more polished up.

**Stevie Kim:** So we have like.

**Stevie Kim:** Very accurate visibility to the database.

**Jose Farias:** Sorry, I interrupted, but I was looking at the database.

**Jose Farias:** This might be interesting.

**Jose Farias:** Just confirming we didn't have any, like, paid upgrades.

**Jose Farias:** I don't think anyone's paying.

**Jose Farias:** There's one account that's paying, it's Marcel's.

**Jose Farias:** So I don't think that counts.

**Jose Farias:** Yeah.

**Stevie Kim:** And I think that's what that last, that completed step is, is if they, yeah.

**Stevie Kim:** So, yeah, and I'll figure out.

**Stevie Kim:** I can't remember what I have the page view on, because that was the onboarding.

**Stevie Kim:** I think it's just, like, the path is just onboarding.

**Jose Farias:** That's what I have it set, too.

**Stevie Kim:** So, yeah, if you guys want to, like, dig into what I.

**Stevie Kim:** So, yeah.

**Stevie Kim:** Set up and, and, you know, fix things, edit things, feel free.

**Jose Farias:** Sounds good.

**Jose Farias:** I, I kept tabs on like the data intensive stuff.

**Jose Farias:** That's primarily what I was looking at.

**Jose Farias:** Sorry to jump in.

**Jose Farias:** Did you have anything else you wanted to cover, Stevie?

**Jose Farias:** No, no, feel free.

**Stevie Kim:** Cool.

**Jose Farias:** So, so yesterday I was mostly like watching dashboards and like making sure stuff stayed online.

**Jose Farias:** And fortunately the thing that worried me most with, which is the data intensive stuff that held up pretty well.

**Jose Farias:** I have some data about how customers are using the data intensive parts of the product.

**Jose Farias:** So, this is interesting, competitor changes are about as common as changing your prompts in bulk.

**Jose Farias:** So, I thought people would.

**Jose Farias:** I just select their competitors during the onboarding and just let it sit that way.

**Jose Farias:** But no, it seems some amount of people, like 13 at least, are changing their competitors actively.

**Jose Farias:** And about the same amount of accounts, 13, changed their prompts that we've assigned them after the onboarding.

**Jose Farias:** That's good.

**Stevie Kim:** That's good.

**Stevie Kim:** I mean, I expected the competitors, to be honest, because I, even myself, I fiddle with those more than the prompts.

**Stevie Kim:** But that's really good that you saw 13.

**Stevie Kim:** That's kind of part of the activation that I'm trying to capture.

**Stevie Kim:** Yeah, so I'm trying to differentiate between library prompts and custom prompts.

**Stevie Kim:** And I think there are events for that.

**Stevie Kim:** I just probably need to put both in.

**Jose Farias:** Nice.

**Jose Farias:** Yeah.

**Jose Farias:** I will also need to differentiate between...

**Jose Farias:** Internal users, hopefully, if we have the email, could just filter out the domain.

**Stevie Kim:** Yeah, there's a toggle for that, but since we all use some test accounts, some of those don't get captured.

**Jose Farias:** Right, that makes sense.

**Jose Farias:** Cool.

**Jose Farias:** Well, yeah, getting into the stand-up sort of flow.

**Jose Farias:** So yesterday, I worked on that, getting some data, looked at some of the Sentry stuff that was worrying.

**Jose Farias:** Nothing too big.

**Jose Farias:** Estevão and myself collaborated on the one bug, I think, that could impact sign-ups.

**Jose Farias:** We have what we suspect is a race condition.

**Jose Farias:** Estevão tracked it down.

**Jose Farias:** Estevão, where going through the onboarding, some users might have had the app crash for them.

**Jose Farias:** with impression there?

**Jose Farias:** Of

**Jose Farias:** Not too many.

**Jose Farias:** think it was like, what was it, Estevão, like three?

**Jose Farias:** Yeah, was, no, it was fewer than that.

**Jose Farias:** Okay.

**Estevão Mascarenhas:** So that's good.

**Jose Farias:** Not too many people, but that was, that I remember is the only bug that actually like impacts like signups and like the app being usable at all.

**Stevie Kim:** And honestly, one of those was like already in the customer.

**Jose Farias:** Oh, yeah?

**Jose Farias:** Yeah, Webflow.

**Stevie Kim:** Ah.

**Jose Farias:** Yeah.

**Jose Farias:** Yeah.

**Jose Farias:** So that was a different bug, I think.

**Jose Farias:** That was the 404, right?

**Jose Farias:** You're referencing from the output?

**Jose Farias:** Yeah, yeah.

**Stevie Kim:** Oh, I didn't realize we had a different, we had another outage.

**Jose Farias:** Okay.

**Jose Farias:** It was a different, yeah.

**Jose Farias:** So that one was caused by an outage.

**Jose Farias:** Uh, this one that we're talking about is, it seems, was talked about a different root cause.

**Jose Farias:** I am optimistic that, Estevão, the...

**Jose Farias:** fix that he deployed should work, hopefully it will, we'll keep an eye on it.

**Jose Farias:** Other than that, we got some, what I would consider to be feature requests more than bugs, quite a few of them.

**Jose Farias:** I think we can just start tackling those because does anyone have any bugs on their radar that are like high priority or should, can we just start tackling the feature requests?

**Jose Farias:** Nothing.

**Jose Farias:** Cool.

**Jose Farias:** Yeah, no, I don't think so.

**Jose Farias:** So for the rest of the day today, I think what I'll do is I might grab one of the feature requests, but I feel like we have a, I need to finish the cadence stuff because it'll half our spend.

**Jose Farias:** Like I feel like that's, I don't know if it's on our radar and like, I know money isn't necessarily an issue with startups, but I don't know.

**Jose Farias:** I think it's worth it.

**Jose Farias:** agree.

**Jose Farias:** agree.

**Stevie Kim:** A lot of, a lot of these requests.

**Stevie Kim:** I

**Stevie Kim:** And stuff are, anyone can take them.

**Stevie Kim:** It's very, like, I'm gonna, you know, like, once I get, you know, the analytics in place and stuff, I, you know, I can tackle some of those.

**Stevie Kim:** They're pretty lightweight for the most part.

**Stevie Kim:** I will say that there's some, I don't think we need to start today, but next week, there's some workflows that need to be done or improved for the growth side of things.

**Stevie Kim:** Again, I can start to tackle those or anyone else.

**Stevie Kim:** Yeah, because I haven't actually used the new output workflows.

**Stevie Kim:** So I should probably dig into that code base because I don't know how much things have changed since we migrated those over.

**Stevie Kim:** But yeah, just wanted to highlight that.

**Stevie Kim:** Maybe we should start to look at those when we have some bandwidth, maybe next week.

**Jose Farias:** Sounds good.

**Jose Farias:** Okay, yeah.

**Jose Farias:** Then I'll focus on the cadence of, I'll wrap it up saying, I'm having a hard time, like, fully mentally committing to any one task, just because, like, my brain is always like, we're launching, like, watch the dashboards, are we still online?

**Jose Farias:** Like, that kind of thing.

**Jose Farias:** So I'm a little bit slow, admittedly, but I think it's worth it.

**Jose Farias:** Like, this needs proper attention.

**Jose Farias:** Anyway, that's me.

**Estevão Mascarenhas:** Sorry, go ahead.

**Pedro Steimbruch:** Yeah, I was just saying, I tackled some requests from yesterday, this morning.

**Pedro Steimbruch:** I worked on the, I worked on the setup customer in the US.

**Pedro Steimbruch:** It's, it's done, the work there.

**Pedro Steimbruch:** And, apparently, we were sending emails from Europe.

**Pedro Steimbruch:** I'm not sure what Jason was doing manually, but if you go to customer.io portal, we have for team account, you can see that we are sending emails, welcome emails to users.

**Pedro Steimbruch:** But as Josef requested, this morning I created an account on my email because I couldn't create an account with the team's email.

**Pedro Steimbruch:** And the zone is tied to the account, not to the workspace in the customer.io.

**Pedro Steimbruch:** So I created one with my account, I cloned the campaign, I imported the users, I connected to RudderStack, and we are receiving events there already.

**Pedro Steimbruch:** I want someone, maybe Jason, to review the campaign I created and if it's okay to start sending emails from there.

**Pedro Steimbruch:** And then we need a checklist to turn off the Europe instance and start using the...

**Pedro Steimbruch:** test this one.

**Pedro Steimbruch:** ...

**Pedro Steimbruch:** ...

**Pedro Steimbruch:** ...

**Pedro Steimbruch:** ...

**Pedro Steimbruch:** U.S.

**Pedro Steimbruch:** Instance to send emails.

**Pedro Steimbruch:** There is a small checklist there to enable the campaign on the U.S., disable on Europe.

**Pedro Steimbruch:** What else?

**Pedro Steimbruch:** Remove DNS entries from Cloudflare for the Europe instance.

**Pedro Steimbruch:** And there is the list there.

**Pedro Steimbruch:** I need to double check.

**Pedro Steimbruch:** I checked a few page generations that SESC reported yesterday.

**Pedro Steimbruch:** I implemented the seven-day trading average for prompt show page charts.

**Pedro Steimbruch:** Did the impersonate feature.

**Pedro Steimbruch:** I'm not reverting that right now, Jose.

**Pedro Steimbruch:** I think that was a quick way.

**Pedro Steimbruch:** If I knew the clerk way to approach it, it would be even faster.

**Pedro Steimbruch:** But it took me less than an hour to implement that.

**Pedro Steimbruch:** So now Marcel can check.

**Pedro Steimbruch:** Like how workspaces look like.

**Pedro Steimbruch:** I also pinned the brand to the prompt show page, compare list, request from Marcel.

**Pedro Steimbruch:** I fixed the Google AI overview that was introduced after the migration.

**Pedro Steimbruch:** Okay, in the check that workflows.

**Pedro Steimbruch:** And I'm about to push some small improvements to the probe details page.

**Pedro Steimbruch:** And yeah, and I will wrap up for today.

**Pedro Steimbruch:** I will be off after that too.

**Jose Farias:** Great work.

**Jose Farias:** Real quick about the impersonation.

**Jose Farias:** I think that's fine.

**Jose Farias:** We don't have to revert.

**Jose Farias:** I agree with your reasoning.

**Jose Farias:** The one thing to watch out for there is, I don't know, like it seemed like we were very adamant to be compliant and regulatory stuff with customer IO and then with impersonations.

**Jose Farias:** Like this is a pretty big.

**Jose Farias:** Uh.

**Jose Farias:** I don't know.

**Jose Farias:** It has big security implications, right?

**Jose Farias:** Because the way it's implemented right now, which I think would be the same way with Quark, is any admin can impersonate.

**Pedro Steimbruch:** I think that's fine usually in US law.

**Jose Farias:** It's Europe that's more particular about that.

**Jose Farias:** So yeah, just wanted to bring that up.

**Jose Farias:** I'm usually very like, I'm not a fan of like impersonating, but it's common.

**Jose Farias:** So yeah.

**Jose Farias:** Any thoughts there?

**Jose Farias:** I don't know.

**Stevie Kim:** We did this a lot at Algorithmia and even DataRobot, be able to impersonate.

**Stevie Kim:** Typically, I mean, typically we just, because we had those close relationships with our customers, you know, we were like, hey, is it okay if we like impersonate you and debug your, you know, your model kind of thing.

**Stevie Kim:** And so this does feel a little bit weird, but you know.

**Stevie Kim:** We can also, as an admin, you know, you can go into anyone's workspace and, you know, you don't even have to impersonate them.

**Stevie Kim:** But, I mean, they would see you as a user if you did that.

**Stevie Kim:** So there's just a lot of weird things that we can do that probably aren't great for European law.

**Stevie Kim:** But that said, everybody does do it because it's hard to get around not doing it.

**Stevie Kim:** But I can, I can dig into a little bit of that just to make sure there isn't anything like glaringly.

**Jose Farias:** Yeah.

**Jose Farias:** I think to, to Stevan's point, usually that's accompanied by like access logs and like registering like the, oh, you're going to impersonate, like tell me why first and then you can go ahead.

**Jose Farias:** And so we haven't built any of that.

**Jose Farias:** And again, I think, I don't think that's a regulatory risk in the U.S.

**Stevie Kim:** I don't think, but I'm not a lawyer, so I can't make an actual like suggestion there.

**Jose Farias:** But yeah, so maybe just.

**Jose Farias:** Something to bounce off of an actual law person, which I don't know if you are, Stevie, maybe you have a background.

**Jose Farias:** No, I do not.

**Stevie Kim:** I know some folks.

**Estevão Mascarenhas:** In the past, this kind of impersonation work, like when there is a certification or regulatory enforcement, it usually requires to have like a small flow to impersonate.

**Estevão Mascarenhas:** Like you request, someone requests Y, it's usually has an expiration and gets logged.

**Estevão Mascarenhas:** That's mostly it.

**Estevão Mascarenhas:** So yeah, I agree.

**Estevão Mascarenhas:** It's fine.

**Estevão Mascarenhas:** It's just that I have the feeling that we never stopped to think about like how admins should access workspaces.

**Estevão Mascarenhas:** For example, the other customers, they have other admins enrolled to their workspace.

**Estevão Mascarenhas:** That's bad.

**Estevão Mascarenhas:** Like if they go to their user tabs, they're going to see like everyone from growthx there.

**Estevão Mascarenhas:** I think we need to stop and figure that out.

**Estevão Mascarenhas:** can clear that at some point.

**Stevie Kim:** Well, as long as it's the trial period.

**Stevie Kim:** I don't, I don't mind.

**Stevie Kim:** Like, that's fine.

**Stevie Kim:** They haven't paid us and they're getting all this for free.

**Stevie Kim:** However, and we set up their accounts and everything for them.

**Stevie Kim:** Once they convert, if they convert, then I, then we, then we definitely need to be able to, you know, convert them to an owner instead of just a member.

**Stevie Kim:** need to like remove all growthx admins and yeah.

**Estevão Mascarenhas:** Yeah.

**Estevão Mascarenhas:** Yeah, no, that's fine.

**Estevão Mascarenhas:** Yeah.

**Estevão Mascarenhas:** I have the feeling that this, like this need for regulatory need will come from like a big enterprise customer at some point.

**Estevão Mascarenhas:** Hey, do you have it?

**Estevão Mascarenhas:** Like, this is a, the amount of money that I want to view you guys.

**Estevão Mascarenhas:** Yeah.

**Estevão Mascarenhas:** You don't have it.

**Estevão Mascarenhas:** Yeah.

**Stevie Kim:** It's always just a checklist.

**Estevão Mascarenhas:** Yeah.

**Jose Farias:** Yeah.

**Estevão Mascarenhas:** Okay.

**Estevão Mascarenhas:** So I think we can figure out when, when that happens.

**Jose Farias:** Sorry to interrupt you.

**Estevão Mascarenhas:** Go ahead.

**Estevão Mascarenhas:** No, no, no.

**Estevão Mascarenhas:** Yeah, sure.

**Estevão Mascarenhas:** Yeah.

**Estevão Mascarenhas:** Okay.

**Estevão Mascarenhas:** Nice.

**Estevão Mascarenhas:** And by the way, that's, that's great.

**Estevão Mascarenhas:** I also.

**Estevão Mascarenhas:** I've already used that impersonation today to view the workspace that Stevie mentioned yesterday that was empty.

**Estevão Mascarenhas:** That was great.

**Estevão Mascarenhas:** It worked really nice.

**Estevão Mascarenhas:** Oh, great.

**Estevão Mascarenhas:** Yeah.

**Estevão Mascarenhas:** So just starting my update.

**Estevão Mascarenhas:** So I'm currently checking that.

**Estevão Mascarenhas:** So I posted on the channel.

**Estevão Mascarenhas:** Why is that?

**Estevão Mascarenhas:** Like we had 2,000 prompts that we added to the subcategories.

**Estevão Mascarenhas:** So the shared delivery, those were not being added to the workspaces because so at some point in November, we added the leaderboard tag flag to the prompts.

**Estevão Mascarenhas:** And in the migration, we set at that point, all the shared delivery prompts that were active to be leaderboard.

**Estevão Mascarenhas:** But we didn't like we don't tag any other prompts that we added after that with that flag.

**Estevão Mascarenhas:** So basically everything that we added just, I think it just changed the, I'm not even sure about that, but just.

**Estevão Mascarenhas:** Let's change the leaderboard metrics that we're showing.

**Estevão Mascarenhas:** So what I'm going to do right now, since we don't have a logic around what is a leaderboard, because we target all of those shared libraries, I will change the bootstrap operation to add all the shared library prompts to the user workspace.

**Estevão Mascarenhas:** And I will post a message to Daniel and Marcel, because I think Daniel did this.

**Estevão Mascarenhas:** Like, what was the reason?

**Estevão Mascarenhas:** I recall that we discussed that we only wanted, like, awareness and evaluation prompts to be leaderboard, but I think that got lost at some point.

**Estevão Mascarenhas:** Like, I'm just going to confirm that.

**Estevão Mascarenhas:** So I will ignore that flag for now, so we don't run in that issue again of empty workspaces.

**Estevão Mascarenhas:** And, yeah, and I will filter out subcategories in the dream onboarding.

**Estevão Mascarenhas:** Like, we're not going to show subcategories that there are no prompts available there.

**Estevão Mascarenhas:** I'm not sure if this is, like, I'm just trying to protect from that happening, because someone might be onboarding just when.

**Estevão Mascarenhas:** And someone in the admin panel created a subcategory, and we think we are just showing it.

**Estevão Mascarenhas:** Like, it could be empty without prompts.

**Estevão Mascarenhas:** I'm not sure if, I'm just thinking out loud if you guys agree, or if you guys have another idea how to fix that.

**Estevão Mascarenhas:** But basically, I want to prevent an empty subcategory to be picked and then lead to an empty workspace.

**Estevão Mascarenhas:** Do you have thoughts on that?

**Jose Farias:** So, Stevie, are we creating new subcategories at this point?

**Stevie Kim:** I'm not.

**Stevie Kim:** I'm refusing to, to be honest, because there's just too much risk right now of, like, you know, because it's not that there's risk.

**Stevie Kim:** I had, like, dedicated time to just sit down and do it to make sure all the prompts there, competitors are there, it's just that right now is not a good time.

**Stevie Kim:** So, I'm telling, like, delivery team, the people who are asking me for subcategories to be updated or new ones, I'm like, yeah, let's not do that until...

**Stevie Kim:** So...

**Stevie Kim:** So...

**Stevie Kim:** So...

**Stevie Kim:** After launch, I don't want any empty categories with empty dashboards.

**Stevie Kim:** Yeah, so that's kind of where I'm at right now.

**Stevie Kim:** I think next week is probably when I'm going to complete the requests from the delivery team, if all is well.

**Estevão Mascarenhas:** Yeah, like after we joined the stand-up, Marcel just sent a message telling me that he was planning to add subcategories.

**Estevão Mascarenhas:** So the feeling that I have is I think we're going to need some kind of status for a category, like in draft and publish it.

**Estevão Mascarenhas:** So people can figure out the category, like all the prompts, and then click publish, and then it gets available to public area and for users to pick up.

**Estevão Mascarenhas:** But like as a stopgap solution, I can just like hide those categories for now, subcategories for now.

**Stevie Kim:** That'd be great.

**Stevie Kim:** Yeah.

**Stevie Kim:** So are you just going to manually hide the ones that Marcel's creating until they're...

**Estevão Mascarenhas:** No, I'm going to put the check like...

**Estevão Mascarenhas:** I'm not going to list on that dropdown any subcategories that has no prompts.

**Estevão Mascarenhas:** Got it.

**Estevão Mascarenhas:** Basically, that's it.

**Estevão Mascarenhas:** But the thing is, if someone is adding prompt one at a time, if someone happens to be onboarding, it's going to start a workspace with just one or two or three, fewer prompts.

**Estevão Mascarenhas:** But I think until we have this publishing flow for categories, think maybe that's fine.

**Stevie Kim:** Well, another issue, too, is that it's not just the prompts, it's the amount of brands in that subcategory.

**Stevie Kim:** Like, if there's one brand in a subcategory, that isn't great either.

**Stevie Kim:** But it doesn't sound like Marcel's super concerned with that, unless he's just, like, going heads down on it and doing it, like, in one chunk of work.

**Stevie Kim:** But he did the lovable one, the layer, the vibe code one he created, and he just put lovable, and that's been in there for a few days at least, probably longer.

**Stevie Kim:** But that's just when

**Stevie Kim:** noticed it and that has like a single brand in there, but yeah, it doesn't look good for us to have that.

**Stevie Kim:** So if we can, yeah, put some checks around there and just not show those, that'd be great.

**Estevão Mascarenhas:** Yeah, I think like even if the user finds issue, it's not a blocking because like in the competitors part, they can, when they type to search a competitor, we show all the brands that we have in our catalogue.

**Estevão Mascarenhas:** We don't filter by super catalogue, so they can pick whatever brand we already have.

**Estevão Mascarenhas:** And for the prompts, they can go to like the prompt library page and add those manually if they want, like if they want to see that.

**Stevie Kim:** Yeah, it's more of the public pages or the public pages, like the categories and brands.

**Stevie Kim:** So that's like a lot of people, you know, first experience.

**Estevão Mascarenhas:** And so that's, that was where my concern came in, just that first experience.

**Estevão Mascarenhas:** Okay.

**Estevão Mascarenhas:** Yeah, so just wrapping up, sorry, I've been saying a lot of things.

**Estevão Mascarenhas:** So I'm working on that.

**Estevão Mascarenhas:** I will be.

**Estevão Mascarenhas:** Pick something next, I'm a bit lost what I will do next, but I'm going to pick from the P1 Stabilize Week.

**Estevão Mascarenhas:** I think P0 is done, right?

**Estevão Mascarenhas:** Maybe we can never even hide it, that milestone, and start just putting on the order.

**Estevão Mascarenhas:** Yeah, and the issue that Jose mentioned about the crash, yeah, it's weird thing, like just in production for a few users.

**Estevão Mascarenhas:** I push the fix, I will monitor it, I mark those as resolved in sentry, so if it comes back, I will be pinged if there's a regression there.

**Estevão Mascarenhas:** Yeah, and just one extra thing before I wrap up, I know that we never had this kind of issue, but should we maybe just informally discuss a little bit of on-call rotation, or we can just super communicate?

**Estevão Mascarenhas:** For example, will be around tomorrow, so if something pops up, I will be able to join, but Sunday I will be out with a place without the internet.

**Estevão Mascarenhas:** So I just want to hear your guys' thoughts about how we should do that.

**Estevão Mascarenhas:** I don't think we need a formal thing like PagerDuty for now.

**Estevão Mascarenhas:** I think just communicating is fine, I guess.

**Jose Farias:** I agree.

**Jose Farias:** We don't have a big influx of users yet, so that we have a ton of users hitting us all the time.

**Jose Farias:** So I think as long as someone is online, that's probably enough.

**Jose Farias:** Which I will be, I'll be around this weekend.

**Jose Farias:** mean, I have kids, but usually I'm able to like jump on.

**Jose Farias:** We can over-communicate like you said.

**Jose Farias:** Okay, nice.

**Estevão Mascarenhas:** I just want you to prevent like both of us, all of us three, like just go out and it's a coincidence, right?

**Estevão Mascarenhas:** But it can happen.

**Estevão Mascarenhas:** All right.

**Estevão Mascarenhas:** Yeah, I'm finished.

**Estevão Mascarenhas:** Thanks.

**Estevão Mascarenhas:** Thanks.

**Estevão Mascarenhas:** Thanks.

**Estevão Mascarenhas:** Thanks.

**Estevão Mascarenhas:** Thanks.

**Estevão Mascarenhas:** Thanks.

**Pedro Steimbruch:** Yeah, I just want to mention that you don't know exactly what to work on, and I'm seeing we have the post-launch is bloated right now.

**Pedro Steimbruch:** have so many things there.

**Pedro Steimbruch:** Maybe we should prioritize there.

**Stevie Kim:** That's one of the things I wanted to ask today, because I've been doing a lot of backlog, like I've been in the weeds in the backlog.

**Stevie Kim:** And I wanted to see what you guys wanted to do with the, like, just create new labels or something, or, because there is a lot in to do, most are either labeled growth, or they're tagged with, you know, one of the launch tier labels.

**Stevie Kim:** And so, you know, we can either repurpose the labels that exist and just change the description, or just change, you know.

**Stevie Kim:** Create new labels, but however you guys want that organized, I can tackle that.

**Stevie Kim:** But yeah, there's no, like, there's no, besides like the, you know, urgent, the priority, urgency, medium, you know, there's no other way we're really organizing that right now, because everything's going to be post-launch at this point.

**Estevão Mascarenhas:** Yeah, yeah, just to be clear, I was planning to, we still have a lot of tasks on P1, so I'm planning to tackle those in order, I try to prioritize there, like, what I meant is I don't, I don't see a specific task that needs, like, really attention now, so just follow that, that to do column there.

**Jose Farias:** That's good, Pedro, real quick, it's, it seems like Marcus merged that internal app URL thing again, just want to make sure.

**Jose Farias:** Or it's not the same thing?

**Jose Farias:** Okay, okay, cool.

**Pedro Steimbruch:** Just checking it.

**Jose Farias:** Nice.

**Jose Farias:** What was the difference?

**Jose Farias:** Just curious.

**Jose Farias:** Because I know we tried that last time and it didn't work.

**Pedro Steimbruch:** The last time the internal app URL was HTTPS.

**Jose Farias:** Ah, so we're not encrypting anymore?

**Pedro Steimbruch:** Yeah.

**Pedro Steimbruch:** Because, yeah, if we do, need to have a certificate on that internal domain.

**Pedro Steimbruch:** I think it's okay.

**Jose Farias:** Because, yeah, it's like internal.

**Pedro Steimbruch:** It's internal.

**Pedro Steimbruch:** Yeah.

**Pedro Steimbruch:** Cool.

**Jose Farias:** Right.

**Jose Farias:** I think that's, is that it?

**Jose Farias:** Yep.

**Stevie Kim:** Yeah, and just let me know, like, especially as we're post-launch and stuff, just let me know, like, what you guys need for me as far as support.

**Stevie Kim:** You know, if, if things are too chaotic or unprioritized or if you're not getting enough.

**Stevie Kim:** that's Exactly.

**Stevie Kim:** Context on tickets or whatever, just let me know and I'll try to make things a little bit smoother however I can.

**Estevão Mascarenhas:** Yeah, would say great work on checking the sessions.

**Estevão Mascarenhas:** I started doing that like at the beginning, but when I got heads down in issues, I stopped doing that.

**Estevão Mascarenhas:** So this issue that you found about the empty workspace, I think it was a critical one that only by watching the sessions you could.

**Stevie Kim:** I watched way too many of those.

**Stevie Kim:** I started playing an audio book because it was like, oh my God, I can't watch this on board one more time.

**Jose Farias:** But then I did catch some stuff.

**Stevie Kim:** They are super helpful, but yeah.

**Stevie Kim:** Yeah, you can get cross-eyed pretty quick.

**Jason Gong:** Did anything stand out there?

**Jason Gong:** Because what Nigel and I are doing now is just reaching out to the companies that seem more legit.

**Jason Gong:** to get get I'm I'm get

**Jason Gong:** Trying to help them actually, like, set it up.

**Jason Gong:** Like, is it clear what, at least for new users, like, is it prioritizing, like, we're prioritizing to, like, make it better?

**Stevie Kim:** Yeah, I mean, there's just some little things and stuff, but, like, some of the stuff we already knew.

**Stevie Kim:** It just, we couldn't get to it, you know, right away for the launch.

**Stevie Kim:** But there's nothing, like, huge that's standing out.

**Stevie Kim:** I think, like, you know, like, I made a ticket for, you know, just to add some descriptions.

**Stevie Kim:** But I think I did that, like, a few days ago.

**Stevie Kim:** But, know, the prompt page, like, if you go to the prompt page, like, there's no description.

**Stevie Kim:** Like, you're just, you just land there and you're like, oh, okay, this is.

**Jason Gong:** I think the thing that's still, like, probably the number one thing, just from using it myself and, like, showing to customers is, like, if you don't get the sub.

**Jason Gong:** Or the product category right because either we don't have it or maybe they're misplaced in the wrong one.

**Jason Gong:** It's like that's like the one place that gets stuck where essentially the whole product builds on top of you having the right data.

**Jason Gong:** And if you don't get that right or if we don't have it, it feels kind of broken.

**Stevie Kim:** We've done a lot of thinking around that.

**Stevie Kim:** And like, so we don't want to, there's a lot of complexity around like letting them switch it.

**Stevie Kim:** But there's like improvements, you know, we want to make on the workflow itself that categorizes things.

**Jason Gong:** The workflow that matches the brand or the workflow that creates new categories.

**Jason Gong:** There's no, there's no workflow that creates new categories.

**Jason Gong:** Okay.

**Jason Gong:** Do you know if anyone's working on that or if that's a ticket or if Marcel's here?

**Jason Gong:** No, no.

**Stevie Kim:** It's just, I think.

**Stevie Kim:** I'm going to.

**Stevie Kim:** I'm

**Stevie Kim:** In back of all of our heads.

**Jason Gong:** Okay.

**Jason Gong:** That's good to know.

**Stevie Kim:** I think that's cool.

**Stevie Kim:** I might have created a ticket for it this week.

**Stevie Kim:** But, yeah, it's kind of in the – I've been digging into the workflows to understand exactly how they're working and where we could make improvements and stuff.

**Stevie Kim:** But I haven't had much time to look into that.

**Stevie Kim:** But, yeah, there's – we know it's an issue.

**Stevie Kim:** I don't think there's, like, a super easy silver bullet for it.

**Stevie Kim:** Anyone want to add some of the context from the conversations we've had around the categories?

**Jose Farias:** So I just want to add that while there are complexities to implementing that, they're mostly, like, product decisions.

**Jose Farias:** Right?

**Jose Farias:** Like, we can do it.

**Jose Farias:** But it's just that the whole product changes from under you, right?

**Jose Farias:** So there's, like, do we –

**Jose Farias:** Remove all your prompts and switch them to the proper category.

**Jose Farias:** What do we do with your competitors?

**Jose Farias:** Like that kind of thing.

**Jose Farias:** And yeah, just product questions that need answering.

**Jose Farias:** It does seem to me that we should prioritize it a little bit.

**Jose Farias:** I think because it's in the back burner and I agree with Jason that the product sort of like relies on this.

**Jose Farias:** So maybe we should prioritize that over other things.

**Stevie Kim:** Okay, I can spend some time on that, just trying to shape something and work with.

**Stevie Kim:** I have a feeling Daniel and Marcel are going to have a lot of opinions on this.

**Jose Farias:** So, and that's kind of why it hasn't gotten the attention because they've been hyper-focused on ContentOS.

**Stevie Kim:** So, yeah, I mean, I'll get something started because then at least it gives them a, they'll hop on.

**Stevie Kim:** If there's something to look at and go, wait, no, this is totally the wrong direction.

**Jason Gong:** Yeah, totally, totally.

**Jason Gong:** I guess the only thing for me is like, so I feel like we're coming at it from like parallel work streams, I guess.

**Jason Gong:** Marcel has shown me something he was noodling on that attempted to just map more categories in general.

**Jason Gong:** But I think that's just like stuck in kind of like, it's not really done.

**Jason Gong:** He doesn't have time.

**Jason Gong:** Um, I'm working on a version where like, we're literally asking these companies, Hey, come, come on a call and we'll kind of show you, uh, what this product's about and what your roadmap for optimizing AI visibility looks like.

**Jason Gong:** So, so we have to manually, essentially, when we get a call book, just do all that work, like figure out, cool, are you in the right category?

**Jason Gong:** We'll wait, we'll make a new workspace.

**Jason Gong:** And then we'll just like manually using like whatever Claude pick, like 200 custom props for you.

**Jason Gong:** And then we'll create the category if it doesn't exist.

**Jason Gong:** So we'll probably.

**Jason Gong:** Learn a bunch from doing that.

**Jason Gong:** And then it also sounds like, Stevie, you have a couple of tickets.

**Jason Gong:** So I don't know.

**Jason Gong:** I guess some way I think that's way to just in the back of my head.

**Stevie Kim:** But yeah, as I said, I'll put together some kind of doc.

**Jason Gong:** It won't be super heavy, but it can, like any learnings that you are gaining from talking to The only thing that I would just throw in however you can is like to have an escape hatch where they can at least flag or say like that is the issue.

**Jason Gong:** And I don't know where it is.

**Jason Gong:** Like if it's an onboarding on that screen, if they can't find something, they can, you know, because when I was going through that, I felt stuck because I had to essentially click the X or unintuitively pick something that doesn't match what I have in my head.

**Jason Gong:** Like if I'm a product marketer, it's like almost blasphemy to like pick a different category.

**Jason Gong:** So it's like very unlikely somebody will just do that.

**Jason Gong:** Just like, oh, cool.

**Jason Gong:** This is close enough.

**Jason Gong:** Click it, you know.

**Jason Gong:** So I think like you need an escape kind of path there to say like none of these match and then just type in something to have it either there or somewhere in the product.

**Jason Gong:** And I think that can be a band-aid until we figure this out because at least that tells us like if people are running into this a lot.

**Jason Gong:** Because I'm literally spending thousands of dollars like driving new users and if this is like, like I would like to know if this is like a more important issue or not.

**Stevie Kim:** They're not getting stuck in the onboarding phase on selecting categories.

**Stevie Kim:** They actually spend more time on competitors.

**Stevie Kim:** So we're going to actually cap the number of competitors because they get, they just spend forever.

**Stevie Kim:** Like they want to track every competitor it seems like.

**Stevie Kim:** So yeah, they actually spend less time on the category section.

**Stevie Kim:** But yeah.

**Jason Gong:** I think I did have one ticket where like if you flip that around and pick competitors.

**Jason Gong:** First, maybe we could just infer the category because it's interesting they spend more time on the competitor page.

**Estevão Mascarenhas:** Yeah, that's an interesting idea.

**Stevie Kim:** Yeah, it is.

**Stevie Kim:** It's been interesting to, like, hear even from, like, the current customers, like, what category they want to be because it's not always the one that their competitors are in.

**Stevie Kim:** But I'm also not exactly sure, you know, that's, I'm not talking directly to them.

**Stevie Kim:** So it's, you know, could be information filtered down that maybe, you know, something got lost in translation.

**Stevie Kim:** But, yeah, that's kind of an interesting thought.

**Estevão Mascarenhas:** Yeah, I think the issue is that we won't be able to, like, today we show the competitors based on the category.

**Estevão Mascarenhas:** So with all the categories, I don't think we have anything else to show relevant competitors.

**Estevão Mascarenhas:** We're going to show like just a mess of a list with like our brands.

**Estevão Mascarenhas:** Yeah.

**Jason Gong:** I mean, I do know like you run that deep research at the beginning, right?

**Jason Gong:** Or maybe that happens after you pick competitors, but I'm sure that just tells you who the competitors are.

**Jason Gong:** It's going to be fairly accurate.

**Jason Gong:** But anyway, I'm not trying to find a solution, but I think the two things, like one, I guess we need a process to make the index better and onboard and see what the right info.

**Jason Gong:** then two, I think people like it's going to be impossible to get absolutely everything right.

**Jason Gong:** And they need like some path to kind of either fix it themselves or like flag it for us.

**Jason Gong:** Like in any case, we'll need both of those things.

**Jason Gong:** So I'm going to work on the former because we're going to jump on a bunch of calls.

**Jason Gong:** And then I think the latter would be really helpful as I'm driving more people.

**Pedro Steimbruch:** Yeah, I just want to flag out today morning I replied to someone.

**Pedro Steimbruch:** And Intercom asking to change their category.

**Stevie Kim:** Oh, yeah.

**Stevie Kim:** Yeah.

**Stevie Kim:** No, it's as we've known.

**Stevie Kim:** I mean, Jason, you and I have talked about this for a couple of weeks now.

**Stevie Kim:** And it's just something that we couldn't tackle for the launch.

**Stevie Kim:** But, yeah, it's a known issue.

**Stevie Kim:** I'll get something together.

**Stevie Kim:** I'll just focus on it today.

**Pedro Steimbruch:** I think one nice idea is it's a layer of things, right?

**Pedro Steimbruch:** I think the most reliable ways to determine the category based on mentions, right?

**Pedro Steimbruch:** The prompts that gather more mentions for a specific brand, we see from where these prompts are.

**Pedro Steimbruch:** And that's the category we should.

**Pedro Steimbruch:** Because at least they will see the dashboard as full.

**Pedro Steimbruch:** As we're

**Pedro Steimbruch:** We can give them, right?

**Stevie Kim:** Yeah, but like a lot of prompts don't show any brands are mentioned.

**Stevie Kim:** Like, I mean, there's very, like, or I'm sorry, a lot of brands aren't mentioned, like the smaller ones especially aren't being mentioned.

**Stevie Kim:** So we'll have to figure out what to do with those.

**Pedro Steimbruch:** Yeah, yeah, but that's why I mentioned it's a layer of things.

**Pedro Steimbruch:** Then I think that what Jason suggested is it's very interesting to infer the category based on the competitors they choose.

**Pedro Steimbruch:** These are good ideas.

**Pedro Steimbruch:** Yeah.

**Estevão Mascarenhas:** Yeah, just to add that, like, Jason and Stevie was showing earlier this meeting that she put together, like, a funnel of her onboarding process.

**Estevão Mascarenhas:** So I think we'll be clear, like, when there's a drop, like, there's a churn in a certain step of the onboarding.

**Estevão Mascarenhas:** That's great.

**Estevão Mascarenhas:** And I was going to suggest, I know that I never worked with PostHog, but I know that it has...

**Estevão Mascarenhas:** As experiments, and I think we should start taking a look on that, because if we change the onboarding, we should always be optimizing it, right?

**Pedro Steimbruch:** So be more data-driven now that we have something in place.

**Estevão Mascarenhas:** But I agree, Stevie, I saw Daniel working on workflows that I think he was trying to tackle that, like how to categorize brands, but it was like in the output channel, maybe he was just exploring.

**Estevão Mascarenhas:** I think it's worth to check with him.

**Estevão Mascarenhas:** Yeah, just to add that our subcategorization, it's not great.

**Estevão Mascarenhas:** Like I was testing it a lot, since the beginning.

**Estevão Mascarenhas:** This was one of the first things that we didn't check that, and we definitely need to improve it.

**Estevão Mascarenhas:** But I think he's tackled on that, but just, yeah.

**Stevie Kim:** Yeah, that's why it'll be helpful to put everything in a doc, like, you know, as, yeah, everybody's ideas, basically.

**Stevie Kim:** It's just, like, I'll just state the problem and, you know, have, like, all these different...

**Stevie Kim:** Different ideas, and the assumptions we're making, and all of that, and I'll just get that done today, because it's, I'm not going to do like some heavy multi-page PRD.

**Stevie Kim:** And then I can just share it out for Monday, and maybe that can be our discussion for that second meeting, because it has Marcel and Daniel in it.

**Stevie Kim:** So, and I'll share it, like, I'll try to share it.

**Stevie Kim:** As soon as I get, like, just, like, the scaffolding done on it, so everyone can contribute.

**Stevie Kim:** Sound good?

**Estevão Mascarenhas:** Yeah, awesome.

**Pedro Steimbruch:** Yeah, I have one more thing to flag out for you, Jason.

**Pedro Steimbruch:** I migrated the customer IO to the US instance.

**Jason Gong:** Oh, okay.

**Pedro Steimbruch:** I would like you to review the campaign I created there.

**Pedro Steimbruch:** I tried to copy and paste it.

**Jason Gong:** I

**Jason Gong:** There is no export and import, so I did it manually.

**Pedro Steimbruch:** Yeah, we are sending emails from, welcome emails, right?

**Pedro Steimbruch:** You said you guys were doing that manually yesterday, but actually, customer AIO is sending welcome emails from Europe.

**Jason Gong:** Oh, it was actually working yesterday?

**Jason Gong:** And running?

**Pedro Steimbruch:** Okay.

**Jason Gong:** Yes.

**Jason Gong:** Don't tell Yusuf.

**Jason Gong:** Okay, cool.

**Pedro Steimbruch:** Yeah, so I have the checklist for us to start working with the U.S.

**Pedro Steimbruch:** I just want you to review the campaign and give me the thumbs up that we can start sending emails from there.

**Pedro Steimbruch:** Okay.

**Jason Gong:** And then I will go through the checklist to disable Europe and enable U.S.

**Jason Gong:** Sounds good.

**Jason Gong:** Okay.

**Pedro Steimbruch:** Let's see.

**Jason Gong:** Thanks, everyone.

**Jason Gong:** everyone.

**Jason Gong:** Thanks, everyone.

**Jason Gong:** Thanks, Thanks, everyone.

**Jason Gong:** We'll

**Jason Gong:** Yeah, no, thanks a lot.

**Stevie Kim:** Yeah, happy Friday.

**Stevie Kim:** Happy Friday.

**Jason Gong:** Bye.

**Jason Gong:** Friday.
