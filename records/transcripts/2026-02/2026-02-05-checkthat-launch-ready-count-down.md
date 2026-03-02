# CheckThat: Launch Ready Count Down

<metadata>
date: 2026-02-05
time: 16:00 UTC
duration: 26 minutes
organizer: stevie@growthx.ai
participants: Marcel Santilli, Daniel Lopes, Jason Gong, Pedro Steimbruch, Jose Farias, Estevão Mascarenhas, Leonardo Carpenedo Steffen, Stevie Kim
fathom_recording_id: 120058367
fathom_url: https://fathom.video/calls/556128938
share_url: https://fathom.video/share/CHZhgPqJnkxybRpv9fgWLsGBQz4WYzHy
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Team confirmed launch readiness and will proceed with go-live, contingent on monitoring system performance. The `/sources` endpoint occasionally takes 12-22 seconds for high-usage workspaces—not a launch blocker, as it only affects existing customers. Manual welcome email sending is required due to an EU/US regulatory issue with Customer.io; Customer support automation via Intercom will improve response times.

---

## Context

This is the final technical standup before CheckThat's public launch. The team had already tested the product extensively and built more features than originally planned, creating a large surface area for potential issues. On launch day, the team will maintain minimal deployments (preview environments only, no production merges) and stay in close communication to rapidly respond to any issues. The engineering focus is on system stability, performance monitoring, and ensuring new users have a good onboarding experience. Marketing and growth teams were in a separate concurrent meeting handling launch amplification.

---

## Relevance

**For Marcel (CEO):**
- Team is unified and confident; launch proceeding as planned
- Only non-blocking issues identified; no show-stoppers
- Manual welcome email workaround in place (Yusuf setup pending for @checkthat.ai inbox)

**For Engineering:**
- Focus on stability and monitoring; hold non-critical UI merges post-launch
- Subcategory cap deployment needed before launch (small, low-risk change)
- `/sources` endpoint slowness expected for high-usage workspaces; monitor but not a blocker
- New frontend error (`maximum call stack exceeded`) requires passive monitoring

**For Product/Growth:**
- Onboarding is refactored and tested; ready for new user volume
- Personal email block live; may generate support questions (Intercom automation mitigates)
- Intercom welcome automation and pop-up needed for support responsiveness
- PostHog access rollout in progress (team access now available)

---

## Overview

- **Launch Proceeding:** The team is confident in the build's stability and will proceed with launch, focusing on system monitoring and minor fixes.
- **Performance Bottleneck:** The `/sources` endpoint is slow (up to 22s) for workspaces with many prompts. This is not a launch blocker, as it only affects existing, high-usage customers.
- **Email Complication:** Welcome emails via Customer.io are blocked by a regulatory issue (EU server for US users). Jason will send emails manually as a workaround.
- **Intercom Automation:** Stevie will add an auto-reply and a proactive pop-up message to improve the user support experience.

---

## Key Topics

### System Health & Performance

  - **Sentry Errors:**
      - `maximum call stack exceeded`: A new frontend error (likely an infinite loop) appeared after the analytics deployment. Not user-facing; requires monitoring.
      - Onboarding template errors: Resolved. Caused by a temporary database replication lag.
      - Inertia error in `context_controller`: A single, non-reproducible event.
  - **`/sources` Endpoint Performance:**
      - **Problem:** The endpoint is slow for some users (up to 22s).
      - **Cause:** Aggregation of data from many prompts in high-usage workspaces.
      - **Status:** Not a launch blocker. The team will monitor feedback from existing customers.
  - **Webhook Failure:**
      - **Problem:** A recent deploy of the "internal URL" feature broke the flow webhook.
      - **Cause:** Cloudflare's security rules blocked the webhook path.
      - **Resolution:** Reverted the deploy. The team will whitelist the webhook path to prevent future issues.

### Launch Readiness & Blockers

  - **Customer.io Welcome Emails:**
      - **Problem:** A regulatory issue (EU server for US users) blocks automated welcome emails.
      - **Resolution:** Jason will send emails manually. This is not a launch blocker.
  - **Onboarding Enhancements:**
      - **Subcategory Cap:** Estevão will deploy a cap on subcategories to prevent performance issues from excessive data.
      - **Personal Email Block:** A block for personal email domains is live. The generic error message from Clerk (`this email is blocked`) may cause user confusion and support tickets.
  - **Intercom Support:**
      - **Goal:** Improve support responsiveness and proactively help users.
      - **Actions:** Stevie will add an automated welcome message and a proactive pop-up ("Are you running into trouble?").

### Team Focus & Work Completed

  - **Jose:** Monitor system stability; passively work on the probing cadence.
  - **Pedro:**
      - Added user email to Sentry reports for better context.
      - Moved context and percentage generation to background jobs.
      - Fixed overview stats tab-switching bug.
  - **Estevão:**
      - Refactored the complex onboarding "brand" step into simpler controllers.
      - Will cap subcategories and competitors in onboarding.
      - Will hold off on non-critical UI merges until after launch.
  - **Stevie:**
      - Coordinate on the Customer.io email issue.
      - Set up Intercom automation.
      - Invite the team to PostHog.

---

## Decisions & Commitments

- **Launch Proceeding:** Team unanimously agrees to proceed with launch. No blockers identified.
- **Minimal Deployments:** No production merges on launch day beyond critical fixes. Preview environments only for testing.
- **Subcategory Cap:** Approved for deployment (low-risk, small change).
- **Customer.io Emails:** Manual email workaround accepted; Jason will handle until infrastructure issue is resolved by Yusuf.
- **Intercom Automation:** Stevie will set up auto-reply and proactive pop-up to improve response times and user experience.
- **Monitoring & Communication:** Team commits to staying alert and in close communication throughout launch day.

---

## Open Questions

- **Customer.io EU/US Regulatory Issue:** Will Yusuf need to migrate the Customer.io instance to a US server, or can the regulatory issue be resolved another way? Timeline unknown.
- **/sources Endpoint Performance:** Is there a scalable solution beyond monitoring feedback, or will this require a refactor after launch?
- **PostHog Access:** Rollout status unclear—GrowthX Labs team has access, but Estevão's access attempted two days ago failed. Stevie to send manual invites if needed.
- **Intercom Pop-up Feasibility:** Can a proactive "Are you running into trouble?" pop-up be implemented, or does Intercom's UI placement make this difficult?

---

## Action Items

**Estevão Mascarenhas**
- Deploy onboarding cap on competitors/subcategories to prod

**Pedro Steimbruch**
- Tag Stevie in Customer.io thread re: EU instance/welcome emails

**Jose Farias**
- Keep plate clear; monitor systems; handle issues
- Work on probing cadence

**Stevie Kim**
- Create Intercom welcome automation (auto-reply + pop-up)

**Jason Gong**
- Call Yusuf re: @checkthat.ai inbox for Jason/Marcel

---

## Transcript
**Stevie Kim:** Thank you.

**Stevie Kim:** Hey, I just realized that I have a meeting conflict and there's like a launch ready meeting right now with Marcel and Daniel and some other folks.

**Stevie Kim:** So if you guys want to just do stand up without me, I'll watch the recording.

**Jose Farias:** That sounds good.

**Jose Farias:** I wonder if we should join that, though.

**Jose Farias:** Probably.

**Stevie Kim:** Well, I think it's like, let's see, it's post-amplification, so it's more content stuff.

**Stevie Kim:** Yeah.

**Stevie Kim:** So go ahead and just do it without me.

**Stevie Kim:** I think the only thing was that 404 error that a user saw.

**Stevie Kim:** I haven't ever seen it during onboarding, but it's something to look into.

**Stevie Kim:** But yeah, I'll watch the recording.

**Stevie Kim:** Sounds good.

**Jose Farias:** That was the output, downtime.

**Jose Farias:** But yeah, sounds I thought it might be because it looked around the same time.

**Jose Farias:** Cool.

**Jose Farias:** All right.

**Jose Farias:** Thanks.

**Stevie Kim:** All right.

**Stevie Kim:** Bye.

**Jose Farias:** Yeah.

**Stevie Kim:** Bye-bye.

**Jose Farias:** Okay.

**Jose Farias:** Hello.

**Jose Farias:** Hello.

**Jose Farias:** Stevie, let me know that she has a scheduling conflict.

**Jose Farias:** They

**Jose Farias:** I think we'll, at the very least, have some feedback from users and also internal.

**Jose Farias:** I'm sure, like, people will realize, like, oh, this works this way?

**Jose Farias:** Like, this shouldn't work this way and be, like, very vocal about it.

**Jose Farias:** We built a ton of stuff, way more than I would have advised, but, hey, it's all good.

**Jose Farias:** It just means the surface area is quite big.

**Jose Farias:** So I agree.

**Jose Farias:** Something is probably going to happen.

**Jose Farias:** I do think, I agree, we did enough testing that whatever happens, we should be able to handle.

**Jose Farias:** So let's just keep a level head and stay in communication, and I'm optimistic.

**Pedro Steimbruch:** I have some dead-ups this afternoon again.

**Pedro Steimbruch:** Yeah.

**Pedro Steimbruch:** But I'll be back.

**Jose Farias:** Yeah.

**Pedro Steimbruch:** Yeah.

**Pedro Steimbruch:** That sounds good.

**Jose Farias:** There's enough of us that I think we can cover everything.

**Jose Farias:** We should probably do the standup as usual, but I do want to call out, ever since we deployed the analytics stuff, the error rates went up a little bit in Sentry.

**Jose Farias:** This is frontend stuff.

**Estevão Mascarenhas:** Yeah, frontend stuff, specifically maximum call stack exceeded.

**Jose Farias:** There's an infinite loop or something somewhere.

**Jose Farias:** I don't know if it's user phasing, though.

**Jose Farias:** Just something to keep an eye on.

**Jose Farias:** And then the one other thing, I guess there's three things I would like to call out.

**Jose Farias:** That was the first one.

**Jose Farias:** Another is we started getting some missing template errors and stuff around onboarding.

**Jose Farias:** template stuff around onboarding.

**Jose Farias:** But I think that was either related to the output outage or the replication lag this morning.

**Jose Farias:** So I think we're fine.

**Jose Farias:** Has anyone looked at those?

**Jose Farias:** Yeah, I took a look.

**Estevão Mascarenhas:** I think it was the replication lag because what happened, I think it was me that was triggering it.

**Estevão Mascarenhas:** Because what happens is for every page that I was trying to navigate, it was sending me to the clerk sync room.

**Estevão Mascarenhas:** And I think it was sending in an inertial request, like a synchronous request.

**Estevão Mascarenhas:** So I don't think we have a template.

**Estevão Mascarenhas:** We probably should put something in place just to redirect the user there.

**Estevão Mascarenhas:** But it shouldn't happen.

**Estevão Mascarenhas:** Because, yeah, I was getting the waiting room in every request, like the asynchronous request, the pulling request.

**Estevão Mascarenhas:** But after the replication lag got fixed, I didn't get it anymore.

**Pedro Steimbruch:** Yeah, we got one inertia error in a context controller, context controller.

**Pedro Steimbruch:** But, yeah, I saw three inertia.

**Jose Farias:** I couldn't reproduce.

**Pedro Steimbruch:** I tried.

**Pedro Steimbruch:** I clicked it around.

**Pedro Steimbruch:** I couldn't reproduce it.

**Jose Farias:** If it's only the one time that it happened, I think, yeah, I'm checking the Sentry console.

**Jose Farias:** There's a single event.

**Jose Farias:** So I think we're fine.

**Jose Farias:** Just something to keep an eye on.

**Jose Farias:** And then the last thing, would it be, yeah, the sources endpoints are quite slow, sometimes like 12 seconds, 22 seconds in some instances.

**Jose Farias:** I have no clue what to do, though.

**Pedro Steimbruch:** Yeah, I did.

**Pedro Steimbruch:** It was slower before.

**Pedro Steimbruch:** Last week, I did the index thing.

**Pedro Steimbruch:** Remember?

**Pedro Steimbruch:** Yeah, I remember.

**Jose Farias:** Yeah.

**Pedro Steimbruch:** It should be two to five seconds now, mostly.

**Jose Farias:** Maybe, should we reduce the number of sources that we display at once?

**Pedro Steimbruch:** That might help, I think.

**Pedro Steimbruch:** We still need to aggregate.

**Pedro Steimbruch:** That's the aggregation that takes time.

**Pedro Steimbruch:** Ah, you're right.

**Jose Farias:** Yeah.

**Jose Farias:** And this isn't the async request, right?

**Jose Farias:** This is the normal one, the page navigation.

**Jose Farias:** Yeah.

**Pedro Steimbruch:** Yeah, one thing to call out is that we started getting a regression in 95, right, in the alerts lately, like, last week or so.

**Pedro Steimbruch:** They were more often, so.

**Pedro Steimbruch:** It might be just a volume.

**Jose Farias:** Like, because the table size has increased, and I'm looking at the slow requests in Sentry, and they're all for the URL sources page.

**Jose Farias:** Yeah.

**Pedro Steimbruch:** There's one for the diagnostics controller in the admin, but that's fine, like, if that errors out, it's not a problem.

**Pedro Steimbruch:** I mean, right now, I am navigating through the sources, and it's less than three seconds, would say, which is not sure why it would take.

**Jose Farias:** You know what it probably is?

**Jose Farias:** There must be.

**Jose Farias:** be.

**Jose Farias:** There

**Jose Farias:** Some amount of workspaces that are following so many prompts that we have, we just have that much more data for them.

**Estevão Mascarenhas:** Yeah.

**Jose Farias:** I mean, that won't stop launch.

**Jose Farias:** Stevie, we're talking about there's one endpoint that sometimes takes like over 20 seconds to load, which is the URL sources one.

**Jose Farias:** And we have a working theory that it only happens in workspaces that are following a lot of prompts.

**Jose Farias:** I think that we can launch and we can figure it out.

**Jose Farias:** Yeah.

**Stevie Kim:** That's not a blocker.

**Stevie Kim:** Yeah.

**Stevie Kim:** I mean, that's really right now.

**Stevie Kim:** That's only going to affect our current customers.

**Stevie Kim:** They're the only ones that have like that many prompts in their workspaces.

**Stevie Kim:** Yeah.

**Stevie Kim:** Because we'll see if they raise a problem or, you know, an issue with it.

**Jose Farias:** That sounds good.

**Jose Farias:** We are capping the number of subcategories, right?

**Jose Farias:** So in the onboarding, have we deployed that?

**Jose Farias:** No, not yet, not yet.

**Estevão Mascarenhas:** Not yet.

**Jose Farias:** Shouldn't do it.

**Estevão Mascarenhas:** I was trying to hold off deployments during this period, but if you think it's okay.

**Jose Farias:** I think it's a small enough change that's probably fine, just because that would be the other trigger, right?

**Jose Farias:** Like if someone adds a ton of subcategories and a ton, it could be like seven, that would also probably have other repercussions.

**Jose Farias:** Okay, we'll do that then.

**Estevão Mascarenhas:** Sounds good.

**Jose Farias:** Yeah, sounds good.

**Pedro Steimbruch:** I think the guys are still figuring out.

**Pedro Steimbruch:** So sorry, I was reading here.

**Pedro Steimbruch:** The guys, Jason and Yusuf, because it's what Jason wants to use to send welcome emails.

**Pedro Steimbruch:** And Yusuf pointed out.

**Pedro Steimbruch:** Bye.

**Pedro Steimbruch:** Super Bowl.

**Pedro Steimbruch:** Bye.

**Pedro Steimbruch:** Thank

**Pedro Steimbruch:** Just a few ago, that our instance is in Europe, and this is a major regulatory issue for sending emails through a Europe server.

**Pedro Steimbruch:** They may need to change it to the US.

**Jose Farias:** Sorry, you cut off.

**Jose Farias:** What instance is in Europe?

**Pedro Steimbruch:** The Customer.io instance, the instance JSON configured for sending welcome emails.

**Pedro Steimbruch:** Got it.

**Pedro Steimbruch:** Got it.

**Pedro Steimbruch:** I'm not sure if that will delay the launch.

**Stevie Kim:** It has the potential to...

**Pedro Steimbruch:** Does...

**Stevie Kim:** Who's taking on that contact to JSON?

**Stevie Kim:** It's...

**Stevie Kim:** Does that already happen?

**Stevie Kim:** this point.

**Pedro Steimbruch:** yeah, JSON has to verify DNS entries for a customer.

**Pedro Steimbruch:** I will tag you, Stevie, the thread.

**Stevie Kim:** remember.

**Stevie Kim:** Yesterday, the has It's the yeah.

**Stevie Kim:** Let's go.

**Pedro Steimbruch:** Jason asked this morning to verify DNS entries for a customer.

**Pedro Steimbruch:** I did it.

**Pedro Steimbruch:** I added mails there for Jason, Marcel, and now Jason was asking if he would have access to the at check that AI inbox, and then I tagged Yusef to spin up inboxes for Jason and Marcel.

**Pedro Steimbruch:** And then Yusef figured out that customer was in Europe.

**Stevie Kim:** Okay, got it.

**Stevie Kim:** So everybody is aware then.

**Stevie Kim:** Yeah.

**Stevie Kim:** I'm not sure what is the next step there, but yeah.

**Stevie Kim:** Okay.

**Stevie Kim:** As I understand it.

**Pedro Steimbruch:** Okay.

**Pedro Steimbruch:** good.

**Pedro Steimbruch:** The welcome emails would use the tracking events that Daniel set up these days, right?

**Pedro Steimbruch:** These are sent to customers somehow, customer.io, and then customer would trigger the welcome emails, as far as I understood it.

**Jose Farias:** Yeah, I don't think there's any action items for us there.

**Pedro Steimbruch:** Yeah, I'm just pointing out that this has the potential to delay the launch.

**Pedro Steimbruch:** To delay the launch.

**Jose Farias:** Yeah, I think let's expect that it won't, and then if it does, then that's fine.

**Jose Farias:** I'm going to try to keep my plate relatively empty today, just so that I have the bandwidth to tackle anything.

**Jose Farias:** Coming back to the true stand-up nature.

**Jose Farias:** Okay.

**Jose Farias:** I'll just work on the probing cadence, which has been on the back burner for the last couple of days.

**Jose Farias:** I'll just work on that passively and keep an eye on things in case you break.

**Jose Farias:** And that's my plan for today.

**Pedro Steimbruch:** On my side, I started earlier because I knew I would have to be off during the afternoon.

**Pedro Steimbruch:** I set up DNSs.

**Pedro Steimbruch:** I added user email to sent reports.

**Pedro Steimbruch:** I was missing the user email there.

**Pedro Steimbruch:** We have the user ID.

**Pedro Steimbruch:** Now we have the user email in sentry logs and errors.

**Pedro Steimbruch:** I tried to merge the internal URL, which was breaking the flow web hook to the scrape response.

**Pedro Steimbruch:** I did it during the probe window.

**Pedro Steimbruch:** It was a mess.

**Pedro Steimbruch:** I had to revert it because the internal URL didn't work.

**Pedro Steimbruch:** Support Okay.-huh.

**Jose Farias:** Because of.

**Jose Farias:** Yeah.

**Pedro Steimbruch:** But.

**Pedro Steimbruch:** For an HTTPS, I spent an hour reverting it and making sure that we were able to receive webhooks again.

**Pedro Steimbruch:** I moved the context generation and percentage generation to background jobs.

**Pedro Steimbruch:** I did QA on the onboarding, fixed a few page generation issues for Saskia, and just fixed the overview stats when changing tabs.

**Pedro Steimbruch:** This is merged now.

**Pedro Steimbruch:** Thanks, Jose, for the heads up there.

**Pedro Steimbruch:** Yeah, of course.

**Estevão Mascarenhas:** Okay, I can go next.

**Estevão Mascarenhas:** Just a comment on the webhook that was being blocked by Cloudflare.

**Estevão Mascarenhas:** We had that in the CMS part.

**Estevão Mascarenhas:** So there was a page there that we were getting blocked because Cloudflare was thinking it was a .NET injection attack because of the custom rules.

**Estevão Mascarenhas:** So I think Jacopo disabled that or just allowed like some basic.

**Estevão Mascarenhas:** Security rules.

**Estevão Mascarenhas:** But I think we can also, if it's not yet, can also ignore the web who path to apply those rules as a solution.

**Estevão Mascarenhas:** Encountered?

**Estevão Mascarenhas:** Yeah.

**Estevão Mascarenhas:** I think we can kind of whitelist that path.

**Estevão Mascarenhas:** Well, just add in the context.

**Estevão Mascarenhas:** So on my side, was, this morning I was testing onboarding a lot because yesterday I was working on the brand step of the onboarding.

**Estevão Mascarenhas:** So the first step after the signup.

**Estevão Mascarenhas:** So I did some refactoring there because it's a complex step.

**Estevão Mascarenhas:** Like there's lots that can happen.

**Estevão Mascarenhas:** Like the user can add, can input an existing brand.

**Estevão Mascarenhas:** It can pick for similar brands.

**Estevão Mascarenhas:** can reject that similar brands that we show the user.

**Estevão Mascarenhas:** We can, it can add a brand that we don't, that don't exist.

**Estevão Mascarenhas:** needs to wait for the basic researcher.

**Estevão Mascarenhas:** So there's a lot going on.

**Estevão Mascarenhas:** And it was becoming complex to handle it.

**Estevão Mascarenhas:** So I broke it down in multiple controllers and multiple pages.

**Estevão Mascarenhas:** Each one was simpler now.

**Estevão Mascarenhas:** But yeah, I had to do a lot of testing and ask Pedro to help me with that this morning.

**Estevão Mascarenhas:** It looks good.

**Estevão Mascarenhas:** I tested in production when it went live.

**Estevão Mascarenhas:** So I think we are good there.

**Estevão Mascarenhas:** Stevie will want to take another look as well, just for the sake of it.

**Estevão Mascarenhas:** But I think it's fine.

**Estevão Mascarenhas:** I tested it a lot.

**Estevão Mascarenhas:** And yeah, I will do the cap competitors and subcategory tasks then.

**Estevão Mascarenhas:** And then I will try also to not do anything else.

**Estevão Mascarenhas:** Like there was some UI push that I was going to keep doing.

**Estevão Mascarenhas:** But I think I will do and leave in a branch until like the peak of traffic settles down a bit.

**Estevão Mascarenhas:** So yeah, I think that's it on my side.

**Jose Farias:** Yeah, that sounds good.

**Jose Farias:** We can deploy to like preview instances and such.

**Jose Farias:** But the main...

**Jose Farias:** Branch, let's take a slow day today in terms of like merging, in terms of deploying to prod.

**Jose Farias:** Cool.

**Stevie Kim:** So, yeah, I'll try to figure out, I'm assuming that it's not going to stop the launch either, the customer IO thing.

**Stevie Kim:** I just skimmed that thread.

**Stevie Kim:** Looks like Daniel's out of office today.

**Stevie Kim:** But I'll ping Jason and, you know, I'll flag it for Marcel as well.

**Stevie Kim:** But, yeah, I can't imagine that we're going to suspend launch for it.

**Stevie Kim:** But, yeah, I'll continue to, you know, keep an eye on the site.

**Stevie Kim:** And then, then, yeah.

**Stevie Kim:** PostHog and Intercom.

**Stevie Kim:** I need to create some automated messaging for Intercom.

**Stevie Kim:** And in the past, as a female, I've gotten some weird messages on Intercom once they find out I'm a girl.

**Stevie Kim:** So I will be throwing any of those, you know, your guys' way if they are a real customer, but maybe it's a little flaky sounding.

**Stevie Kim:** It's just happened in the past, like at Algorathmia when we were like doing this open marketplace, you know.

**Stevie Kim:** Yeah, you know, you can get some iffy messages.

**Stevie Kim:** So I just wanted to add that.

**Estevão Mascarenhas:** Absolutely.

**Jose Farias:** Yeah, don't feel, yeah, you shouldn't deal with that.

**Stevie Kim:** All right.

**Stevie Kim:** Yeah, that's it.

**Stevie Kim:** Just also the analytics stuff.

**Stevie Kim:** And then, yeah, I mean, I think I'm with you guys just.

**Stevie Kim:** Also, oh, I want to, you know, like not going heads down on anything.

**Stevie Kim:** I did want.

**Stevie Kim:** I to say that just, you know, we should be including ourselves in the amplification of everything.

**Stevie Kim:** So, you know, getting on LinkedIn, all the socials and stuff, spending a little bit of time on that.

**Jose Farias:** Sorry, Stevie, real quick.

**Jose Farias:** You mentioned PostHog.

**Jose Farias:** I don't think I have access.

**Jose Farias:** Is that something you could put me?

**Stevie Kim:** Yeah, I'll invite you guys.

**Stevie Kim:** I don't know.

**Stevie Kim:** Like, I think Daniel just, like, invited just a few of us because Jason, no, Jason invited me, actually.

**Stevie Kim:** I don't know.

**Stevie Kim:** It's the rollout hasn't, yeah, it's been a little bit.

**Jose Farias:** Yeah, it's okay.

**Stevie Kim:** But yeah, yeah.

**Stevie Kim:** Whoever wants access, yeah, if everybody wants access, I'll just give all of you guys access because it's not like we have to pay proceed, I don't think, for that.

**Pedro Steimbruch:** The team at GrowthX Labs has access.

**Pedro Steimbruch:** Oh, does it?

**Stevie Kim:** Ah.

**Pedro Steimbruch:** I was able to sign into it today to check.

**Pedro Steimbruch:** Okay, cool.

**Stevie Kim:** it recent?

**Estevão Mascarenhas:** Because I tried like two days ago and it prompted me to create a new workspace.

**Estevão Mascarenhas:** I tried this morning.

**Estevão Mascarenhas:** Okay.

**Estevão Mascarenhas:** Yeah, that's nice.

**Estevão Mascarenhas:** Okay.

**Stevie Kim:** So, yeah, just let me know if that doesn't work for anybody and I'll send an email invite.

**Stevie Kim:** That's good.

**Estevão Mascarenhas:** Just before I wrap up, just a note that I added the block for personal emails.

**Estevão Mascarenhas:** Like I added a comprehensive list of Gmail, Outlook, these kind of providers.

**Estevão Mascarenhas:** There are more than 100 entries there.

**Estevão Mascarenhas:** The thing is, it's very subtle the way that we tell the user.

**Estevão Mascarenhas:** Right now, it's just the label and the placeholder that is telling, hey, this is a work email during sign up.

**Estevão Mascarenhas:** So, just in case that we get that through intercom.

**Estevão Mascarenhas:** Because the message that the clerk tells the user is, hey, this email is blocked from access.

**Estevão Mascarenhas:** It's very generic.

**Estevão Mascarenhas:** So, we might get those.

**Estevão Mascarenhas:** Kind of ask questions like, hey, I cannot use my email here.

**Estevão Mascarenhas:** Yeah, just a heads up on that.

**Jose Farias:** Sounds good.

**Jose Farias:** Jason, we're just about to wrap up.

**Jose Farias:** There is nothing on our minds that would block the launch or anything like that.

**Jose Farias:** Did you have anything you would like to go over?

**Jason Gong:** No, I mean, there's a thread on Customer.io, apparently.

**Jose Farias:** Right.

**Jason Gong:** So we're just going to manually do it.

**Jason Gong:** Is there a way to just send from, you know, team a check that or Jason a check that?

**Jose Farias:** From Customer.io?

**Jose Farias:** No, just like the same way, you know, send like a, like email inbox.

**Jose Farias:** I would have to check.

**Jose Farias:** Is anyone familiar with that setup?

**Pedro Steimbruch:** Yousef said check that is added as an alias or something.

**Jason Gong:** But Yusef should be able to create an inbox.

**Pedro Steimbruch:** Yeah.

**Pedro Steimbruch:** For you guys, from that thread, I'm saying that, from what he mentioned in the thread.

**Jason Gong:** Okay.

**Jason Gong:** Yusuf was here.

**Jason Gong:** He literally just left, so it might be a...

**Jason Gong:** I'll call.

**Jason Gong:** Let's see.

**Jason Gong:** And then intercom, I guess, what was the welcome message you were, did you type me on?

**Jason Gong:** Oh, yeah.

**Stevie Kim:** So I didn't realize that we didn't have any, anything around, like, any automation as far as, like, the first response.

**Stevie Kim:** So at least when I was at Algorithm, you know, we set up, I set up, like, just at least a welcome message, you know, saying, hey, we'll get to you, you know, soon.

**Jason Gong:** I think the only thing that might be really impactful is, like, if we can get it to pop.

**Jason Gong:** And just say like, hey, are you running into trouble?

**Jason Gong:** know?

**Jason Gong:** Yeah.

**Stevie Kim:** It's just, if it takes us like three hours to get someone or, you know, like eight hours to get to someone, it's just nice to have like some kind of, you know, some acknowledgement that we received their message and also like maybe point them to, you know, some information or whatever.

**Stevie Kim:** We can add that.

**Jason Gong:** But is it possible to have it pop up?

**Jason Gong:** Because I think it is like somewhat hidden.

**Jason Gong:** I think there are corners you can run in the product.

**Jason Gong:** So I just want to.

**Stevie Kim:** Yeah, I'm sure there.

**Stevie Kim:** Yeah, I'm sure you can have it pop up.

**Jason Gong:** Okay.

**Jason Gong:** Could you, could you add that?

**Stevie Kim:** I can look into it if I have time today.

**Jason Gong:** What's a, I mean, I guess like, is there any high priority thing for the launch?

**Jason Gong:** Because I just want to make sure people have like a good experience once they get in.

**Stevie Kim:** You mean as far as what engineering has been tackling?

**Jason Gong:** Yeah, like what's prioritized like today currently if you're checking that?

**Stevie Kim:** Not a lot of margins.

**Stevie Kim:** So just like making sure that, you know, we have like all eyes on the site, making sure, you know, everything is stable and performant and working on, you know, some things here and there.

**Stevie Kim:** But yeah, I missed part of it because I was on your meeting, but no, I was there for like seven minutes and bounced to this one.

**Stevie Kim:** So Jose, anything you want to add to that?

**Stevie Kim:** Yeah, basically you're going to do tiny merges today.

**Jose Farias:** We are aware there is the sources and points are quite slow sometimes for some workspaces.

**Jose Farias:** Our working theory is that this happens when workspaces follow a lot of prompts that I might tackle that.

**Jose Farias:** That's the larger thing, I guess.

**Jose Farias:** Other than that, it's tiny things like not choosing too many subcategories in the onboarding, like that kind of thing.

**Jose Farias:** No big merges, no database migration.

**Jose Farias:** Just keeping an eye on the system.

**Jose Farias:** Okay, cool.

**Jason Gong:** I'll be planning around nine, but keep you updated.

**Jose Farias:** Sounds perfect.

**Jose Farias:** All right.

**Jason Gong:** See you, everyone.

**Jason Gong:** All right.

**Jose Farias:** Thanks, y'all.

**Estevão Mascarenhas:** Bye-bye.

**Stevie Kim:** Bye.
