# CheckThat: Launch Ready Count Down

<metadata>
date: 2026-02-02
time: 17:29 UTC
duration: 40 minutes
organizer: stevie@growthx.ai
speakers: Leonardo Carpenedo Steffen, Estevão Mascarenhas, Jose Farias, Stevie Kim, Daniel Lopes
fathom_recording_id: 118984526
fathom_url: https://fathom.video/calls/550962473
share_url: https://fathom.video/share/G5aSZtgsbqQMtmHaxj7PgNi6e2-c2xcx
source: fathom
enriched_on: 2026-02-27 14:35 UTC
</metadata>

---

## Summary

CheckThat team confirmed the product is launch-ready as of February 2. Key completions: historical data upgrade path and billing flow done; onboarding UI polish in progress. Phased rollout plan approved: remove waitlist today for internal testing, export to Customer.io for launch invites, then public announcement. Addressed scalability with separate backfill worker to isolate heavy database load from core app during traffic spikes.

---

## Context

CheckThat is GrowthX's strategic software bet—an AI visibility index for B2B brands that surfaces what companies are saying about your industry online. The team launched the beta and is now moving toward production. This is a final sync before going live to ensure the product is ready, infrastructure can handle launch traffic, and the team has clear next steps for onboarding users and supporting them post-launch.

The meeting brings together the core CheckThat build team (Leonardo, Estevão, Jose) with Daniel Lopes from GrowthX Labs (handling workflows and launch coordination) and Stevie Kim (GrowthX operations lead). The agenda: confirm billing and data readiness, validate the phased rollout plan, and clarify owner assignments for blocking work.

---

## Relevance

**CheckThat Product**
- Phased launch strategy: remove waitlist today, export to Customer.io, send invite emails via launch sequence, then public announcement
- Onboarding UI polish underway to strengthen first-user impression before wider rollout
- Billing flow complete; transactional email automation via Stripe launch config + Customer.io for lifecycle emails
- Historical data upgrade path near completion; unlock data by tier with automatic backfill on upgrade

**GrowthX Delivery**
- Workflows platform (Output.ai on Temporal) ready; separate Render services for API, worker, Redis with autoscaling
- Martech stack configured: RudderStack → Customer.io (campaigns), PostHog (analytics), Intercom (support), GA (verification needed)
- Support via Intercom with AI co-pilot trained on internal KB; escalation process and activity feed for context
- Database scalability plan: split backfill worker to protect core app from heavy load spikes during launch

**Business Development**
- Daniel Lopes (GrowthX Labs) owns launch coordination: waitlist export, Customer.io sync, Loom documentation for team workflows
- Stevie Kim drafting Intercom support guidelines to ensure consistent, fast user support post-launch

---

## Overview

- **Launch Readiness:** The product is nearly ready, with the historical data upgrade path and billing flow complete. The main focus is now on polishing the onboarding UI.
- **Scalability Plan:** The backfill process is being split into a separate worker to isolate its heavy database load. This allows for independent scaling to manage traffic spikes without impacting core app performance.
- **Support Strategy:** Intercom will serve as the initial support channel, using an AI co-pilot trained on an internal knowledge base to provide fast, consistent answers and capture user questions for future help content.
- **Phased Rollout:** A phased launch is planned to manage initial load. The waitlist will be removed today for internal testing, with a small group of users invited first, followed by a wider public announcement.

---

## Key Topics

### Launch Strategy & Phased Rollout

  - **Goal:** A phased launch to manage initial load and test system stability.
  - **Today:** Remove the waitlist for internal testing.
  - **Launch Day:** Export waitlist emails → import to Customer.io → send invites.
  - **Communication:** A small, contained announcement will precede a larger public post (e.g., on LinkedIn).

### Scalability & Performance

  - **Problem:** Unpredictable load from backfilling historical data could degrade core app performance during a launch traffic spike.
  - **Solution:** Split the backfill process into a separate worker with its own queues.
      - **Critical Queue:** Processes the last 7 days of data, which is required before a user can enter the app.
      - **Low-Priority Queue:** Handles all older data.
  - **Contingency Plan:**
      - **Slow Backfills:** Increase worker count.
      - **Database Lag (Replication/Contention):** Decrease worker count or upgrade the database tier.
  - **Trade-off:** Slower backfills for new users in exchange for maintaining core app stability.

### Product & Billing

  - **Historical Data Upgrade Path:**
      - **Status:** Wrapping up today.
      - **Functionality:** Users on free/lower-tier plans see a lock icon for data older than their plan allows. Clicking it triggers an upgrade modal.
      - **Post-Upgrade:** The system automatically backfills the newly unlocked data period.
      - **Scope:** Unlimited historical data for the Business plan is deferred to a follow-up PR to prioritize production testing.
  - **Billing Flow:**
      - **Status:** Complete.
      - **Missing:** No automated transactional emails (e.g., receipts, cancellations).
      - **Plan:** Use Stripe's UI settings to automate receipts and cancellation emails for launch. More complex lifecycle emails will be built in Customer.io.
  - **Onboarding UI:**
      - **Status:** Functional, but needs polish for a better first impression.
      - **Action:** Estevão will polish the UI today.
  - **Onboarding Brand Lookup Fix:**
      - **Problem:** A brand lookup in the onboarding flow caused incorrect data to be returned (e.g., "branch.io" matched "branch.co").
      - **Solution:** The lookup will now be skipped if a user explicitly states their brand is not found in the initial search results.

### Support & Analytics Stack

  - **Intercom:**
      - **Function:** Primary support channel.
      - **Knowledge Base:** Populated from Notion and code; used to train an AI co-pilot for fast, consistent answers.
      - **Process:** User questions → "All inbox" → team member assignment → AI-assisted reply.
      - **Admin Panel:** Includes an activity feed to view user events (page views, actions) for better support context.
  - **Martech Stack:**
      - **RudderStack:** Central data router.
      - **Customer.io:** Receives full user data and events for email campaigns.
      - **PostHog:** Receives events and offers superior session recording.
      - **Intercom:** Receives basic user data (name).
      - **Google Analytics (GA):** Jason will verify the GTM configuration to resolve console errors.

### Workflows Framework

  - **Platform:** Output.ai, running in an isolated `checkthat` namespace on Temporo.
  - **Architecture:**
      - **Repo:** `checkthat-workflows`.
      - **Structure:** Workflows in `source/workflows`; shared agents in `source/gx` (do not modify).
      - **Deployment:** Separate Render services (API, worker, Redis). The worker is autoscaling.
  - **Known Gap:** No notification from workflows back to the app on failure. This is a potential source of "stuck" processes and will be addressed in a follow-up.

---

## Action Items

**Estevão Mascarenhas (GrowthX)**
- Post billing status update in billing task thread for Leonardo
- Add admin panel billing info + plan change
- Polish onboarding UI
- Remove waitlist; enable self-serve signups
- Remove brand lookup from onboarding when 'No' selected

**Leonardo Carpenedo Steffen (GrowthX)**
- Enable Stripe receipts/invoices/reminders; align w/ Stevie
- Create Linear ticket for Daniel: export waitlist to Customer.io + Loom

**Daniel Lopes (GrowthX Labs)**
- Share workflows env in CheckThat vault
- Share workflows docs link (docs.ai/output.ai) w/ team
- Record Loom: Martech/RudderStack/Customer.io/PostHog
- Check w/ Render re: workflow worker CPU probing
- Confirm w/ Jason phased launch plan
- Ship workflow execution cleanup: cancel >4h, purge >30d

**Stevie Kim (GrowthX)**
- Draft Intercom support guidelines

---

## Transcript
**Leonardo Carpenedo Steffen:** Thank you.

**Leonardo Carpenedo Steffen:** Thank you.

**Leonardo Carpenedo Steffen:** Daniel, you're if you're speaking.

**Leonardo Carpenedo Steffen:** Hey, no worries.

**Leonardo Carpenedo Steffen:** I have.

**Leonardo Carpenedo Steffen:** have.

**Leonardo Carpenedo Steffen:** So

**Leonardo Carpenedo Steffen:** I'm going to clean up the HCC today, so I'm in the bedroom.

**Leonardo Carpenedo Steffen:** I'll be walking around, if you guys don't mind.

**Leonardo Carpenedo Steffen:** No problem.

**Leonardo Carpenedo Steffen:** Thank you.

**Leonardo Carpenedo Steffen:** Are you doing CV?

**Daniel Lopes:** Oh, my gosh.

**Stevie Kim:** It's, I don't know.

**Stevie Kim:** I'm good.

**Stevie Kim:** What happened?

**Stevie Kim:** I don't, well, it's a, I can't remember what they called it.

**Stevie Kim:** I have a couple things going on, like, severe allergies in my eyes and sinuses.

**Stevie Kim:** I don't know.

**Stevie Kim:** I take Zyrtec every night, and so this is like, but sometimes I get hives, so I've got like kind of some hives around my eyes, but then also a chalazium, what is it called, chalazium, something, some nodule.

**Stevie Kim:** It's not a sty, it's similar to a sty, and that's inside my eye, so I have to put like this gel stuff, and both the bump and the gel make my vision really blurry in my right eye, but I have stuff going on in both eyes, so it's just.

**Stevie Kim:** Super fun.

**Daniel Lopes:** Great way to spend the weekends and start the Monday.

**Stevie Kim:** Wow.

**Leonardo Carpenedo Steffen:** Yeah.

**Daniel Lopes:** Sorry.

**Leonardo Carpenedo Steffen:** I hope we can get better.

**Daniel Lopes:** Thanks.

**Stevie Kim:** Yeah.

**Stevie Kim:** I haven't broken down to take Benadryl yet, but it might be the next step for the one part of my issue.

**Leonardo Carpenedo Steffen:** Yeah, I'd take something similar.

**Leonardo Carpenedo Steffen:** I think it's the same as Benadryl when I get any of those hives.

**Leonardo Carpenedo Steffen:** get, usually get in my, around my eyes and nose as well.

**Stevie Kim:** Yeah.

**Leonardo Carpenedo Steffen:** But it doesn't get swollen.

**Stevie Kim:** Yeah, I think the swelling is from the other thing.

**Stevie Kim:** It's just funny that I got hit with two different things at once.

**Stevie Kim:** I'm just, you know, lucky like that, I guess.

**Stevie Kim:** Gotcha.

**Stevie Kim:** in this video.

**Leonardo Carpenedo Steffen:** Thank you, guys.

**Leonardo Carpenedo Steffen:** you.

**Leonardo Carpenedo Steffen:** Stress, stress a little bit related.

**Leonardo Carpenedo Steffen:** Samitizing, yeah.

**Leonardo Carpenedo Steffen:** We're waiting for more people to join?

**Leonardo Carpenedo Steffen:** I don't know if he's joining today.

**Stevie Kim:** I don't think he's joining.

**Leonardo Carpenedo Steffen:** He's declined.

**Leonardo Carpenedo Steffen:** Let me take a look.

**Leonardo Carpenedo Steffen:** Pedro declined.

**Leonardo Carpenedo Steffen:** Marcel declined.

**Leonardo Carpenedo Steffen:** Jason is optional.

**Leonardo Carpenedo Steffen:** I guess we get, yeah.

**Daniel Lopes:** I'm ready.

**Leonardo Carpenedo Steffen:** How do you guys want to do this?

**Daniel Lopes:** you want to, because I wasn't, I didn't, I didn't know if we were going to join, Stevie.

**Stevie Kim:** Oh, yeah.

**Stevie Kim:** So usually like Pedro or someone else shows their screen, the linear board, while I take, you know, live notes.

**Stevie Kim:** Um, and so someone can, but since I, my vision's not that great right now, um, I'll just roll.

**Stevie Kim:** Fly on the note takers, but yeah, if someone wants to share the linear board, the launch ready, that would be wonderful.

**Stevie Kim:** Let me share the linear board here.

**Leonardo Carpenedo Steffen:** First time, so you guys can help me do this other times when needed.

**Leonardo Carpenedo Steffen:** I saw the message and Daniel says he was going to take care of it, but I could have done that.

**Leonardo Carpenedo Steffen:** So this is the board.

**Leonardo Carpenedo Steffen:** What are the, do you see the board?

**Leonardo Carpenedo Steffen:** What did I do here?

**Daniel Lopes:** I think we used the launch ready, right?

**Daniel Lopes:** That's the tag at the top.

**Daniel Lopes:** That's what you are.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Okay, cool.

**Leonardo Carpenedo Steffen:** So this we have in progress.

**Stevie Kim:** Yeah, so we can just go, everybody can give their status updates and if there's anything that is blocking or we want further discussion, we'll, you know, we just discuss it live right here.

**Stevie Kim:** treat it as a working session.

**Stevie Kim:** Sure.

**Stevie Kim:** Thank Thank

**Leonardo Carpenedo Steffen:** Cool.

**Estevão Mascarenhas:** Can I start?

**Estevão Mascarenhas:** Yeah.

**Leonardo Carpenedo Steffen:** Can I start?

**Leonardo Carpenedo Steffen:** Yeah.

**Leonardo Carpenedo Steffen:** Go ahead.

**Estevão Mascarenhas:** Yeah.

**Estevão Mascarenhas:** So for this one, I'm wrapping it up today.

**Estevão Mascarenhas:** So basically now we have the upgrade path when the user wants to see historical data older than what the current plan allows.

**Estevão Mascarenhas:** So if a user in the free plan wants to see 30 days, 45 days, or 60 days, they will see a lock icon on that option.

**Estevão Mascarenhas:** When they click it, they see the upgrade model.

**Estevão Mascarenhas:** When they upgrade, we start backfilling that period for them.

**Estevão Mascarenhas:** So it's almost there.

**Estevão Mascarenhas:** Just one thing that I'm leaving out for this PR, like I will open a follow-up, is that for the business plan, we are, like, in the pricing table that we have in the Notion doc, we are telling that we're going to show the unlimited historical.

**Estevão Mascarenhas:** Yeah, don't worry about that.

**Daniel Lopes:** Yeah, I'm not doing that at the moment.

**Estevão Mascarenhas:** think maybe 90 days can be the max, but let's see, I want to test this in production first, because locally it worked.

**Estevão Mascarenhas:** So I'm wrapping it up.

**Estevão Mascarenhas:** The billing task, I'm sorry, I intended to break it down and document the progress there, but I just rushed through it.

**Estevão Mascarenhas:** So I will leave a message there.

**Estevão Mascarenhas:** I know that you were testing, Leo, so I would just leave a message there.

**Estevão Mascarenhas:** What is, what we are missing, but it's not a blocker.

**Estevão Mascarenhas:** For example, we are not sending transactional emails.

**Estevão Mascarenhas:** We can send emails in the lifecycle, for example, when the subscription is ending, we can try to, yeah, trust the user, maybe offered some coupons or this kind of stuff.

**Estevão Mascarenhas:** But I think this can be like improvements on the flow.

**Estevão Mascarenhas:** Go ahead.

**Daniel Lopes:** That can also be part, like if you, if you just trigger the events, like for example, like also put an event on the, when you have to.

**Daniel Lopes:** Yeah, great, because that is one of the key parts from email campaigns.

**Daniel Lopes:** Now, all the emails can be controlled from Customer.io.

**Daniel Lopes:** So, like, you can have lifecycle emails, you can have, like, a subscription close to the date, that kind of stuff can be done for Customer.io.

**Daniel Lopes:** Ideally, it's all done through there.

**Leonardo Carpenedo Steffen:** Yeah.

**Leonardo Carpenedo Steffen:** Receipts, we can automate the...

**Leonardo Carpenedo Steffen:** I noticed that the receipts are not sent automatically, so I got it, I logged into Stripe, and I sent them to myself while I was testing, so you can send cancellation or...

**Daniel Lopes:** Receipts makes sense.

**Daniel Lopes:** Yeah, receipts would be ideal, but, I mean, like, all the things to, like, try to engage the client and, like, to get them to upgrade or to have reminders, that kind of stuff, and we can add, like, even if Stripe doesn't support, that can go through Customer.io.

**Daniel Lopes:** It's pretty easy to build the campaigns there.

**Daniel Lopes:** But, like, all the billing stuff, like, invoices, all the stuff, like, if you can't...

**Daniel Lopes:** if there's a way to turn on those things automatically in Stripe, that would be ideal.

**Stevie Kim:** Yeah.

**Stevie Kim:** I'm going to do that.

**Stevie Kim:** We some of that stuff already through the UI, but I wasn't sure exactly what we wanted, but there should be, there's settings for everything from, you know, reminding people that, oh, you're about to get charged, and then also like email, you know, receipts, invoices, that sort of thing.

**Stevie Kim:** So there's everything you could do that through the UI.

**Stevie Kim:** I'm just curious about like how much we want to do through the UI, through the back, versus the back end, because I think a lot of stuff that I originally set up in the UI is now done on the back end.

**Stevie Kim:** So I want to make sure like, you know, everything's consistent.

**Stevie Kim:** We know like what we're doing where, so someone doesn't go in and toggle something that we're taking care of on the back end or vice versa.

**Estevão Mascarenhas:** Yeah, perfect.

**Leonardo Carpenedo Steffen:** so we'll a look at the Stripe configs, just to make sure that we can automate it, least until we have.

**Leonardo Carpenedo Steffen:** A more elaborate policy to send in the emails to customers, but at least receipts, right?

**Leonardo Carpenedo Steffen:** And cancellation.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Yeah.

**Leonardo Carpenedo Steffen:** I'll do that.

**Leonardo Carpenedo Steffen:** Thanks.

**Leonardo Carpenedo Steffen:** I have the desk built in there.

**Leonardo Carpenedo Steffen:** No, thank you.

**Leonardo Carpenedo Steffen:** I already tagged 541.

**Leonardo Carpenedo Steffen:** So just a quick ask.

**Leonardo Carpenedo Steffen:** If you have anything that you want me to take a look, folks, just add label with my name here, and I'll take a look.

**Leonardo Carpenedo Steffen:** Yeah.

**Estevão Mascarenhas:** Okay.

**Estevão Mascarenhas:** So just finishing, wrapping up my update.

**Estevão Mascarenhas:** So my plan for today, I will add some billing-related information to our admin panel and the ability to change plans there, just in case we want to customize that for our customers.

**Estevão Mascarenhas:** And my plan for today is doing that.

**Estevão Mascarenhas:** And I want to get to polishing the onboarding UI.

**Estevão Mascarenhas:** It's functional, it's working, but I think we can improve.

**Estevão Mascarenhas:** For the first impression during our launch, it should be better than what it is.

**Estevão Mascarenhas:** It's not bad, but I want you to spend some time there, and I couldn't do it.

**Daniel Lopes:** Can we already turn it on, as in just for us, before we announce, so it can be way in production?

**Leonardo Carpenedo Steffen:** Yeah, I think so.

**Estevão Mascarenhas:** Remove the waitlist.

**Daniel Lopes:** We're getting a couple of people every other day signing up for the waitlist.

**Daniel Lopes:** We can just go see them and go through.

**Daniel Lopes:** And we can test ourselves, too.

**Estevão Mascarenhas:** Okay, I can do it today, as well.

**Estevão Mascarenhas:** I think one task, I'm not sure if it's in someone's plate, but we should get the emails off the waitlist, because we need to release an email for them, maybe an invite.

**Daniel Lopes:** We can do that on the day of the launch, and there's a way to just dump the data.

**Daniel Lopes:** We're going to use CustomerIO for all that, so we can just do an export from the console, Rails console, and load in CustomerIO in the segment.

**Daniel Lopes:** I can record the Lunax.

**Daniel Lopes:** Explaining how customario works, just so everybody has an idea, but probably won't Jason be the one doing all that, but I can, for everybody to have a conference.

**Stevie Kim:** So is Jason going to be responsible for taking those people on the waitlist and emailing them, or are you Daniel?

**Daniel Lopes:** Can you add a ticket, Leo, for me to export those users and load in customario and record a loom?

**Daniel Lopes:** Do you have the link?

**Leonardo Carpenedo Steffen:** Yeah.

**Leonardo Carpenedo Steffen:** Actually, I can do it.

**Daniel Lopes:** I can do that.

**Leonardo Carpenedo Steffen:** Okay, sounds good to you.

**Leonardo Carpenedo Steffen:** Yeah.

**Estevão Mascarenhas:** And just a final question, Daniel, can I work on the basic research flow because you are migrating?

**Estevão Mascarenhas:** Yeah.

**Estevão Mascarenhas:** Yeah, I finished.

**Daniel Lopes:** All right.

**Estevão Mascarenhas:** Okay.

**Estevão Mascarenhas:** Okay.

**Daniel Lopes:** I can give an update on that after you finish.

**Estevão Mascarenhas:** Yeah, yeah.

**Estevão Mascarenhas:** I have one task.

**Estevão Mascarenhas:** Basically, I will remove the brand lookup for the onboarding flow when it's in the onboarding flow because it was, we were having some issues there.

**Estevão Mascarenhas:** I was testing with a company called branch.io.

**Estevão Mascarenhas:** called do.

**Estevão Mascarenhas:** I I

**Estevão Mascarenhas:** And so I was typing the onboarding, and the basic research fired it because we didn't have it in our database.

**Estevão Mascarenhas:** And the basic research was doing a lookup in our database, and we have another branch company, branch.co, that is a totally different company, South Africa company.

**Estevão Mascarenhas:** So it was returning the description of this company because it was matching it.

**Estevão Mascarenhas:** So now what I did, just to recap, what I did is the first step on the onboarding, when the user types the domain, first we do a similar search on our site, and we show the options.

**Estevão Mascarenhas:** Hey, is this one of your brands?

**Estevão Mascarenhas:** If the user tells no, then I will skip this lookup.

**Estevão Mascarenhas:** So that's the change that I need to do there, so we don't run this issue again.

**Estevão Mascarenhas:** Yeah, that sounds good.

**Estevão Mascarenhas:** All right.

**Estevão Mascarenhas:** Okay, that's me.

**Daniel Lopes:** Okay, I can share my stuff real quick, so you all have an idea how things are working on, because now you can change different, the workflows.

**Daniel Lopes:** Then, oh, sorry.

**Daniel Lopes:** This is still, but essentially, check that workflows project on May will look like this.

**Daniel Lopes:** Should I close the session?

**Daniel Lopes:** It's like all matter.

**Daniel Lopes:** I'll just close everything here.

**Daniel Lopes:** We have, just to give a quick tour of the thing.

**Daniel Lopes:** So all the workflows, this is the folder structure.

**Daniel Lopes:** There is an env.

**Daniel Lopes:** I'll share the env is in the vault for check that.

**Daniel Lopes:** Use that.

**Daniel Lopes:** You're sharing the screen?

**Leonardo Carpenedo Steffen:** Yeah.

**Daniel Lopes:** Oh.

**Leonardo Carpenedo Steffen:** Just click on the tab on the top.

**Leonardo Carpenedo Steffen:** You guys see it?

**Daniel Lopes:** You want to see it?

**Daniel Lopes:** I don't see anything.

**Daniel Lopes:** And there's a tab on top of the Zoom, probably.

**Daniel Lopes:** Oh, there you go.

**Leonardo Carpenedo Steffen:** Okay.

**Leonardo Carpenedo Steffen:** Good.

**Leonardo Carpenedo Steffen:** So, yeah.

**Daniel Lopes:** So that's the folder structure.

**Daniel Lopes:** So we have the...

**Daniel Lopes:** The CloudMD will pull from the agents.

**Daniel Lopes:** So just so you know, you can add more stuff here if you need, but I haven't needed yet.

**Daniel Lopes:** All the workflows are inside the source.

**Daniel Lopes:** So there's clients, there's shared in the workflows.

**Daniel Lopes:** It's kind of similar structure from what we had in Flow, but we have prompts in this format and folders, and there's scenarios.

**Daniel Lopes:** And you can run the scenarios.

**Daniel Lopes:** And if you just ask Cloud to do things, it will know which commands to run.

**Daniel Lopes:** You have to do output space dev to initiate.

**Daniel Lopes:** I'll send you the tutorial.

**Daniel Lopes:** We'll have the docs as well, how to install the framework and all that, get it running.

**Daniel Lopes:** But all the workflows are inside of this folder here.

**Daniel Lopes:** You can change anything here.

**Daniel Lopes:** Just be mindful that the study uses the citation scraper.

**Daniel Lopes:** And don't change the GX folder.

**Daniel Lopes:** That is the common agents that we're going to run in the separate NPM package.

**Daniel Lopes:** change everything else with fair game.

**Daniel Lopes:** And if you want to change the...

**Daniel Lopes:** The pipelines, let me know, because the pipeline, this part is actually like a prototype of what we are doing in the ContentOS.

**Daniel Lopes:** So all the content-related stuff, maybe assign it to me first, and then if I don't have bandwidth, I can explain how to do, because this has direct impact on how we're doing the new features on the ContentOS side.

**Daniel Lopes:** Everything else, feel free to change, and the GX folder, don't change, to me.

**Daniel Lopes:** And this is going to be Ben and me working on this.

**Daniel Lopes:** Makes sense.

**Daniel Lopes:** And we have all the docs as well.

**Daniel Lopes:** I'll share the docs.

**Daniel Lopes:** We have the docs website already, and it's in here.

**Daniel Lopes:** has most of the things explaining how to install, how to use.

**Daniel Lopes:** This is the Getting Started Guide, and that's how we would run the project.

**Daniel Lopes:** So it's under docs.ai, and the password is output.ai.

**Leonardo Carpenedo Steffen:** That's all I did.

**Daniel Lopes:** Yeah, and last week I did all the Martech stuff and I'll record alone explaining how it works too, but it's essentially sending all the data to RogerStack.

**Daniel Lopes:** RogerStack is the one that distributes the data, so it's distributing to Customer.io.

**Daniel Lopes:** Intercon only gets the name of the users.

**Daniel Lopes:** Oh yeah, let me show the Intercon as well real quick because that's going to be something we're probably going to need this week and I don't have time to join tomorrow.

**Daniel Lopes:** But Intercon, everybody should have received the invite.

**Daniel Lopes:** Alice loaded all the knowledge from the Notion that I extracted from our code base into here.

**Daniel Lopes:** So there is documents about troubleshooting, documents about how the public edit works, and all that.

**Daniel Lopes:** And then somebody asks a question, it will pop up on the All inbox.

**Daniel Lopes:** So we're going to have to figure out the rotation where like everybody's here whenever you start.

**Daniel Lopes:** Like immediately it goes to assigns it to you.

**Daniel Lopes:** So you can have as many people in here answer at the same time and the assignment, all that happens kind of transparently.

**Daniel Lopes:** And when you start replying, if somebody asks you a question, you can click on this and you can ask co-pilot.

**Daniel Lopes:** And then you can ask the co-pilot to answer the question.

**Daniel Lopes:** And then it will pull from the knowledge base.

**Daniel Lopes:** And then you can copy and apply here.

**Daniel Lopes:** So basically it makes replying support tickets super fast.

**Daniel Lopes:** And after the questions are answered, if there's things that are not there, there are ways to make that be part of the knowledge base.

**Daniel Lopes:** It makes the whole process of answering support so much easier that I think it's not worth for us wasting our time trying to recruit somebody that will be able to reverse engineer and learn how the product works and all that in this first month.

**Daniel Lopes:** But then maybe the next month we start thinking about how much is the load and all that.

**Daniel Lopes:** And then we start end.

**Daniel Lopes:** Think about dedicated support people here.

**Daniel Lopes:** Hope that makes sense.

**Daniel Lopes:** Any questions?

**Estevão Mascarenhas:** Just a quick question.

**Estevão Mascarenhas:** How do, like, should we have a process to keep those docs updated like we did?

**Estevão Mascarenhas:** It would be nice, but like, every time, it does make sense.

**Daniel Lopes:** Like, every time we change something big, just like, think about adding to the support, internal support.

**Daniel Lopes:** Because we can also revert, reverse this into, like, an external help center later.

**Daniel Lopes:** So this is the path to an external help center.

**Daniel Lopes:** And we can also later turn on FIN.

**Daniel Lopes:** FIN is the agent that automatically answers.

**Daniel Lopes:** So if we keep these documents organized, FIN will do a good job.

**Daniel Lopes:** And then it creates the path for both things, a public help center and FIN doing a good job.

**Stevie Kim:** Nice.

**Leonardo Carpenedo Steffen:** Yeah, so those are the two things.

**Daniel Lopes:** Customer.io.

**Daniel Lopes:** I don't know if you saw that, but it's getting the username.

**Daniel Lopes:** So like in here, that is the job the Rudder Stack is doing with Intercont.

**Daniel Lopes:** Well, all the scripts are coming from Rudder Stack, and the Rudder Stack does the identification and all that.

**Daniel Lopes:** Same thing with POST-HOG.

**Daniel Lopes:** So all the identification and the events are going to POST-HOG.

**Daniel Lopes:** Customer I.O.

**Daniel Lopes:** gets the same.

**Daniel Lopes:** Customer I.O.

**Daniel Lopes:** gets more identification and the events.

**Daniel Lopes:** So you can build their flow for sending emails or whatever, whenever some event happens or time-based.

**Daniel Lopes:** And the last thing, Jason had a couple of more things.

**Daniel Lopes:** One, they're not supported by Rudder Stack.

**Daniel Lopes:** One was like de-anonymizing people that land on the website through a tool that's not super popular.

**Daniel Lopes:** That I think we can wait.

**Daniel Lopes:** I don't think it's a blocker for the launch.

**Daniel Lopes:** That's one more thing to say.

**Daniel Lopes:** GA is going through.

**Daniel Lopes:** Ideally, I'll ask Jason to double check because GA was firing some errors on the content.

**Daniel Lopes:** So I think, please stay

**Daniel Lopes:** Take a look on the console, whenever you are deploying things to production, just to see if there is any alerts here.

**Daniel Lopes:** I think everything is looking good now, but there was a bunch of stuff that was misconfigured by Jason on the Google Tag Manager.

**Daniel Lopes:** And RedoStack was just going to add things, so if they're misconfigured on the other side, they will screen in our dev console.

**Daniel Lopes:** But yeah, so it's, and the interclines here, so it's going to pop up.

**Daniel Lopes:** It's going to pop up also in the production, in the logged-in experience, but I think that's not a bad thing for the beginning.

**Daniel Lopes:** Session recording, session recording is part of, we do session recording of Sentry and PostHog.

**Daniel Lopes:** PostHog one is better, so if you're going to start looking at how people use things, PostHog is a better place, let's say.

**Daniel Lopes:** Another thing I was going to say, like on the support side, this is the thing I was going to say.

**Daniel Lopes:** On the support side, a common workflow that I always had when I was doing support myself is I couldn't send by the fire.

**Daniel Lopes:** You can see what they did in here in the page views, but even the better place will be to go to their users page and look at their activity feed.

**Daniel Lopes:** So I added the activity feed at the bottom.

**Daniel Lopes:** Added the activity feed here.

**Daniel Lopes:** Activity feed will show the page views and the other events.

**Daniel Lopes:** So when people start doing things, they will show up as events in here as well, like Workspace switched and all that.

**Daniel Lopes:** So you can have an idea what the person did.

**Daniel Lopes:** And the admin checkbox that you had was moved to here.

**Daniel Lopes:** That's everything that I had.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Take a look on the framework or on the workflows.

**Daniel Lopes:** And I was even thinking about putting the workflows in the same repo as the Rails app.

**Daniel Lopes:** Put the entire app in the same app and be just a folder inside of the, maybe alongside the app in the Rails, be like a.

**Daniel Lopes:** Workflows folder, and then you have everything in the same code base, but I didn't do that.

**Daniel Lopes:** Could be something we do next week, because it has a little bit of tweaks that we have to do on render, but all the workflows are running on their own.

**Daniel Lopes:** Oh, yeah, one lesson that I want to show, because it impacts production.

**Daniel Lopes:** All the workflows are running in their own namespace now, so we have, if you go to your, if you log in in Temporo, and you go to namespaces, there is a bunch.

**Daniel Lopes:** There's a check that one here.

**Daniel Lopes:** And if you go, click on that, go into workflows, and these are our workflows.

**Daniel Lopes:** So they're isolated, you can do whatever you want there, and the deploy on render is also separate.

**Daniel Lopes:** So now we have, under check that, there is these three things here, are related to the workflows.

**Daniel Lopes:** It requires a Redis, and an API, and the worker.

**Daniel Lopes:** The worker is the one that gets hammered by the executions.

**Daniel Lopes:** So it has the autoscale ready set up, and it's autoscaling well.

**Daniel Lopes:** So...

**Daniel Lopes:** So...

**Daniel Lopes:** All right, you can see the CPU is heating.

**Daniel Lopes:** I need to check with the guys what we need to do, but CPU is usually not a problem, but you can see the probing happening.

**Daniel Lopes:** Everything that I had on my side.

**Jose Farias:** Cool, I can go next.

**Jose Farias:** Great work with that, by the way.

**Jose Farias:** Using output now is gonna be great.

**Jose Farias:** So I started working on tying the probing cadence to people's pricing tier.

**Jose Farias:** And that has the follow on effect of doing our own probing, the library prompts, doing them every other day.

**Jose Farias:** So I'm tackling both in the same work.

**Jose Farias:** However, I did pause that to focus on launch day stuff.

**Jose Farias:** The one The

**Jose Farias:** thing that's top of mind for me, or was before this weekend, was backfilling.

**Jose Farias:** It's very hard to predict what the load is going to be and where it's going to hurt.

**Jose Farias:** So the best we can do right now is make sure we have the right levers to pull and the right knobs to dial when we do launch.

**Jose Farias:** And so what we're doing for that is we're splitting the backfill into its own worker.

**Jose Farias:** So things like processing webhooks, Ahoy events, and all the rest of the background stuff that happens for operations of the app happens in one worker, and then backfilling happens on its own worker with its own queues.

**Jose Farias:** And then what that allows us to do is scale that up and down.

**Jose Farias:** If the database is being hit enough that it might go down, we can either upgrade the database or scale down the workers.

**Jose Farias:** these numbers.

**Jose Farias:** Nice.

**Jose Farias:** Scaling down the workers means people will have to wait more for the backfilling to complete.

**Jose Farias:** So it's like a bit of a give or take situation.

**Daniel Lopes:** It's not a big deal.

**Daniel Lopes:** Like if you're putting backfill like seven days and just to have no blank data, that's enough.

**Daniel Lopes:** then the backfills.

**Jose Farias:** Right.

**Jose Farias:** That's exactly what we're doing.

**Jose Farias:** When you onboard, we backfill the first seven days, the latest seven days in a critical queue.

**Jose Farias:** And all the rest goes in a low priority queue.

**Jose Farias:** And then Stevon is working on a banner that we will show.

**Jose Farias:** If the backfilling of the, not this last seven days, because you wouldn't be even let into the app if we didn't do the seven days.

**Jose Farias:** So the seven days complete, you're let into the app.

**Jose Farias:** And if you immediately expand the date range in a chart for some reason, you'll see the banner essentially, which is like.

**Jose Farias:** Here we're backfilling.

**Jose Farias:** I don't think that's going to be a big deal.

**Jose Farias:** Things to watch out for are those backfills taking too long.

**Jose Farias:** Even the seven-day backfills taking too long, I think that is not very likely because, again, we're limiting those to the priority queue.

**Jose Farias:** Even if we get a bunch of signups, they're all processing seven days per workspace, so even large accounts in the business plan don't delay other accounts.

**Jose Farias:** But if that starts taking too long, then the thing to be done there is to increase the number of workers.

**Jose Farias:** Second thing to watch out for is replication lag.

**Jose Farias:** If we increase the number of workers, we're increasing the number of writes that we do to the database, and we have a read-write split, so they need to be replicated.

**Jose Farias:** If that starts being a problem, then we need to decrease the number of workers.

**Jose Farias:** And I think those are the two.

**Jose Farias:** two things that could go wrong.

**Jose Farias:** I don't know if we need to go viral for this to be a problem, but a steady low number of signups that aren't concurrent won't be a problem, I don't think.

**Jose Farias:** This would only be a problem if we actually start getting a ton of signups at once.

**Daniel Lopes:** That would be a great problem to have.

**Daniel Lopes:** We don't mind that at all.

**Leonardo Carpenedo Steffen:** It would be good to have a plan for when we go viral, but I don't think there's, I mean, in my opinion, we don't have to do anything right now.

**Leonardo Carpenedo Steffen:** And have a plan for when this begins to be a problem.

**Jose Farias:** Yeah, I think the plan for now can just be that, like, if it's slow, increase the workers.

**Jose Farias:** If replication lag is a problem, decrease the workers.

**Jose Farias:** If none of that works, then we need to bump up the tier of the database.

**Jose Farias:** Basically spend more money is the thing.

**Jose Farias:** So I think we can, that's.

**Daniel Lopes:** And we can pause some of the things in the background as well, like remove Ahoy for a while, or while we split from the separate database, that kind of stuff.

**Daniel Lopes:** You guys have all the levers there for the tweaking on the back end easily.

**Daniel Lopes:** Just make sure we have the number, like if there is any setting that has to be done through like configuration that it's an MVVars, but like it's already like.

**Daniel Lopes:** We're going to have an on-call.

**Leonardo Carpenedo Steffen:** Well, we can talk about that later.

**Leonardo Carpenedo Steffen:** I guess I'm disrupting the same.

**Leonardo Carpenedo Steffen:** Yeah.

**Jose Farias:** Okay.

**Jose Farias:** Yeah, that all sounds good.

**Jose Farias:** Cool.

**Jose Farias:** And that's what I'm working on right now.

**Jose Farias:** I'm about to wrap that up.

**Jose Farias:** So I'm going to move on to go back to the cadence, the probing cadence, tying it to the pricing tiers.

**Jose Farias:** Sorry, I just thought of another thing that could go wrong, which is database contention.

**Jose Farias:** Too many workers writing to the database at once.

**Jose Farias:** Yes, replication lag could be one thing to one problem.

**Jose Farias:** Another would be.

**Jose Farias:** resource contention.

**Jose Farias:** I think bumping the database would be the solution.

**Jose Farias:** So all in all, I think we have default answers to all the things that could go wrong.

**Jose Farias:** If something else goes wrong, it's hard to predict.

**Jose Farias:** don't think it will, but that's launching.

**Jose Farias:** Yeah, exactly.

**Daniel Lopes:** I think we should be good.

**Daniel Lopes:** If things go bad, we put more help here.

**Daniel Lopes:** Distribute people and support.

**Daniel Lopes:** have Jacopo join here and we just turn things off.

**Jose Farias:** Sounds good.

**Jose Farias:** And the split between like a soft, like that's the thing that I wanted to double check.

**Daniel Lopes:** I didn't see if Jason's message, he replied to the message.

**Daniel Lopes:** That's why I was suggesting that we do like a small contained messaging first and then LinkedIn post and that kind of stuff.

**Stevie Kim:** What was the response on that?

**Stevie Kim:** Or if any?

**Daniel Lopes:** I don't think he replied.

**Daniel Lopes:** I'll check.

**Daniel Lopes:** Just to confirm, because like at least one day split where we get like 200 people and then another day where if you get the thousands come separate, that would be ideal.

**Daniel Lopes:** Is there anything top of mind that you all are, like anything we might not be thinking, anything that are tickets that we're not going to have time to cover?

**Stevie Kim:** You know, there's just the, there's some kind of quality of life in P1, tickets in P1, I'm not worried about those, it's, yeah, I think we're in a good spot, you know, I think we're all kind of just thinking like about the right things, like the onboarding experience and the performance.

**Stevie Kim:** So, I don't think that there's anything that is more critical than those right now.

**Stevie Kim:** The team's done a great job in making sure that.

**Stevie Kim:** There aren't the blank chart problems that we were having before, that the metrics are making more sense and things are more intuitive, but there's obviously a lot of polish that can be done everywhere, but I think we're in a good spot.

**Leonardo Carpenedo Steffen:** There's only one thing that I, sorry, did I cut you?

**Stevie Kim:** I was done, I was just asking if anybody else had anything to add.

**Leonardo Carpenedo Steffen:** One of the things that I was thinking this weekend was that I don't think we have any help page or something like that.

**Leonardo Carpenedo Steffen:** While I was testing, I didn't see anything, at least not that I can find.

**Leonardo Carpenedo Steffen:** Any we have anything, a help or a guide or something?

**Leonardo Carpenedo Steffen:** Yeah, that's one thing I'm start working on.

**Daniel Lopes:** That's the thing that I think the intercon would cover for a bit, and then we can have a help center afterwards.

**Daniel Lopes:** We have, like, a couple of ways of knowing what they ask.

**Stevie Kim:** So I brought that up, too, and Marcel said that, and I think that's where maybe Jason's work is coming into play with the Learning Center and the Masterclass and everything, so, and then we have this knowledge base and intercom, so like Daniel said, that's, you know, in the future, but, yeah.

**Daniel Lopes:** Yeah, there's this split where, like, the learn part that I think Marcel and Jason are thinking about will be the actual kind of traffic that we want for people that would purchase the product, as in, like, it's more of, like, a product marketing thing.

**Daniel Lopes:** Like, understand how SEO works, understand, like, questions about AEO, GEO, the differences, but the mini website that would explain the thing that we're doing in the study, like, all these things would go in the slash learn.

**Daniel Lopes:** So you, like, people learn about.

**Daniel Lopes:** But I think we still want to have like a help.checkthat.ai.

**Stevie Kim:** Yeah, that's what I was more referring to, like how the metrics are, you know, like, because people are asking that.

**Stevie Kim:** And I've talked to Nigel too, and he's got a lot of good experience around what people ask.

**Stevie Kim:** And so do the ENs.

**Stevie Kim:** So we've gotten some feedback already on like the typical questions that the users or customers or prospects are needing to know.

**Stevie Kim:** Yeah.

**Daniel Lopes:** That is a good thing for like maybe Stevie, you and Nigel and whoever else was involved on this, can take a look at the internal knowledge of Intercon, see if there's anything amazing there.

**Daniel Lopes:** And then after the launch, like maybe next week, you don't have to do it this week, but like after the launch, like next week or the following one, we start, we turn on the public help center and we start rewriting.

**Daniel Lopes:** The things there, because I think I have all the things there, as in like, but it's reversed from code.

**Daniel Lopes:** So it's reversed how the logic for like calculations work, what happens if my workspace is empty and why, that kind of stuff is in there.

**Daniel Lopes:** But it's not the same level that if you would be answering, a person would be answering.

**Daniel Lopes:** You just could take a look at the documents.

**Stevie Kim:** I do have a question about the depth that we want to explain to people about, you know, how we're doing things.

**Stevie Kim:** Maybe not so much the calculations, but how we're probing and everything, because we don't want, we want to be aligned on the depth of what we expose to people.

**Daniel Lopes:** Yeah, yeah.

**Daniel Lopes:** I think it really depends, you know, so that's why I wanted to put the identification there.

**Daniel Lopes:** Because if you know, if you see the session, you see it's a legit person from a legit company, trying to understand how the product works, because they want to use

**Daniel Lopes:** I think we can be as transparent as they need, but we don't have to add any information, but if it's like a competitor or somebody on the Gmail, then maybe we try to be a little bit more, just start to solve their problem.

**Stevie Kim:** That's fair.

**Stevie Kim:** I can write it.

**Daniel Lopes:** Like we had like a canopy, we had the guide for how to answer support tickets.

**Daniel Lopes:** can adapt it and then show just so we are on the same page and how to.

**Daniel Lopes:** Exactly like answering what you asked, I had the document for that, and we could use one here.

**Daniel Lopes:** Oh, one thing that it can be a problem is none of the workflows, they, I was about to ship today actually like something to track the stay of execution.

**Daniel Lopes:** So like if a, if a workflow gets, hangs for more than like four hours, a market that's canceled and.

**Daniel Lopes:** And also another one will purge old executions after 30 days, so the table is not infinitely growing, but there is not a lot of logic in the workflows to post back if there's a failure.

**Daniel Lopes:** So like, for example, this stuff that Stebon was saying, like, ideally we would send back a notification to the app to like act on it, but we don't have that implemented.

**Daniel Lopes:** So it would be something on the processors and changing the code of the workflows.

**Daniel Lopes:** If you guys start to hit problems with like people complaining about things stuck, that's probably why.

**Daniel Lopes:** That's just one of the gaps we have in the system.

**Daniel Lopes:** But I will ship the cleaning stuff today.

**Stevie Kim:** And just to confirm, oh, sorry.

**Stevie Kim:** Sorry, real quick.

**Jose Farias:** Speaking of people writing in with suggestions, that's one thing I would like to, I think everyone on this call specifically has like product development experience, but not everyone in the company does.

**Jose Farias:** So once.

**Jose Farias:** We ship.

**Jose Farias:** I'm sure lots of feedback is going to come our way.

**Jose Farias:** And yeah, just a friendly reminder, this is normal.

**Jose Farias:** It's part of launching.

**Jose Farias:** And sometimes that feedback is phrased in a way like, why didn't we just do this?

**Jose Farias:** Or why doesn't it work the obvious way?

**Jose Farias:** And it's like, we did a ton of things.

**Jose Farias:** So yeah, just brace for feedback.

**Jose Farias:** We'll take it one at a time and we'll eventually make the people that matter happy.

**Jose Farias:** Yeah.

**Jose Farias:** That's a great point.

**Stevie Kim:** I just wanted to confirm that, Daniel, did you cancel our next meeting?

**Stevie Kim:** I did.

**Stevie Kim:** Yeah.

**Daniel Lopes:** I don't know if you want to have two meetings on the same day because that's just a legacy from my calendar that probably stood there and nobody deleted.

**Daniel Lopes:** I mean, so that one is a little bit more cross-functional.

**Stevie Kim:** I don't think anyone here wants extra meetings if they're not necessary.

**Stevie Kim:** I think today the one, yeah, it can definitely cancel because we went over.

**Stevie Kim:** But yeah, there's, I'm, I'm, I'm thinking of maybe moving that one.

**Stevie Kim:** Well, it depends, like, it just depends upon if we keep this stand up for any length of time versus it because like originally it was just for like launch.

**Stevie Kim:** But if people find it helpful to have every day, we can keep it.

**Stevie Kim:** Otherwise, we can do a cross-functional one once a week, like with what was, you know, previously occurring.

**Daniel Lopes:** I can't imagine that at least the next week will be a good one because you're going to get so much inbound, so much things happening.

**Daniel Lopes:** like this week and next, probably a good idea.

**Daniel Lopes:** But up to you, like whatever you all decide to do.

**Daniel Lopes:** I'm finding it helpful, like as I watch the recordings, not all of them, but like it's just, and I see that you all discuss a bunch of stuff that it would take longer to do in Slack or it wouldn't be done.

**Daniel Lopes:** So at least in this like final week or in next week, I think it's useful.

**Stevie Kim:** But not you.

**Stevie Kim:** All right.

**Stevie Kim:** Well, thanks, everybody.

**Stevie Kim:** Thanks for accommodating my one-eyed status.

**Daniel Lopes:** Thank you for joining.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Good luck, everybody.

**Daniel Lopes:** Good job.

**Daniel Lopes:** You're looking really cool.

**Daniel Lopes:** I think it's going to be smooth.

**Daniel Lopes:** All right.

**Daniel Lopes:** See you.

**Daniel Lopes:** Awesome.

**Daniel Lopes:** Go.
