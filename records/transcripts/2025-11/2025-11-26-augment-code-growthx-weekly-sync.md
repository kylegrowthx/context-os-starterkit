# Augment Code <> GrowthX Weekly Sync

<metadata>
date: 2025-11-26
time: 18:00 UTC
duration: 18 minutes
organizer: jason@growthx.ai
participants: Jason Gong, Edin Abazi, Sylvain Giuliani
fathom_recording_id: 104624279
fathom_url: https://fathom.video/calls/486809523
share_url: https://fathom.video/share/ycen5mk89Ni3TgWSrMvwWEDin87yHwtC
source: fathom
enriched_on: 2026-03-02 02:15 UTC
</metadata>

---

## Summary

Jason Gong and Edin Abazi from GrowthX met with Sylvain Giuliani from Augment Code to investigate a concerning PostHog reporting anomaly and align on content strategy for upcoming product launches. They confirmed that the apparent signup drop is a false signal caused by ad blockers and fraud filters affecting tracking data, while internal data shows actual week-over-week growth. GrowthX will expand tracking infrastructure to monitor install-page visits and deliver a content plan for the Code Reviews feature launching in two weeks, plus support for the Context Engine soft launch next week.

---

## Context

GrowthX is providing content marketing and go-to-market support to Augment Code, a developer-focused AI tooling company. Jason Gong leads GrowthX's engagement and is responsible for tracking content performance and conversion metrics. This is a weekly sync where the teams discuss campaign performance, data reliability, and strategic content planning for Augment Code's new product releases. The meeting was called specifically to investigate anomalies in PostHog signup reporting that were confusing stakeholders and threatening data-driven decision making across Augment Code.

---

## Relevance

**To GrowthX Delivery:**
- GrowthX is expanding its content analytics infrastructure by adding install-page visit tracking, improving measurement beyond signup events which are unreliable due to fraud filters and ad blockers.
- Content rewrite strategy is showing measurable improvement in install conversion rates, validating the focus on substance and quality over SEO optimization alone.
- Two major product launches require rapid content deployment: Code Reviews (two weeks out) and Context Engine (soft launch next week, public launch January).

**To GrowthX Business Development:**
- Account health signal is positive — Augment Code is expanding GrowthX's scope by requesting SEO-focused content plans for new products, indicating trust and growth potential.
- PostHog accuracy improvements are a priority for Augment Code, with potential to serve other downstream teams and expand CheckThat's relevance in developer analytics space.
- Multiple product releases in quick succession (Context Engine, Code Reviews) indicate strong product momentum and content demand.

---

## Overview

- **PostHog data is unreliable.** A sharp signup drop is a false signal from ad blockers and fraud filters; internal data shows week-over-week growth.
- **The complex install-first flow is a deliberate anti-fraud measure.** It prioritizes user quality over speed, but a redesign is in progress.
- **Content focus is shifting to support new products.** The team will deliver a content plan for the "Code Reviews" feature (launching in \~2 weeks) and the "Context Engine" (soft launch next week).

---

## Key Topics

### Signup Data Discrepancy

  - **Problem:** PostHog shows a sharp signup drop over the last two weeks, despite stable traffic to the install page.
  - **Cause:** The data is unreliable due to:
      - **Ad Blockers:** Block PostHog events, a common tool for the developer audience.
      - **Fraud Filters:** Aggressively remove fraudulent signups, which PostHog may still track.
  - **Validation:** Internal data (dbt project) confirms week-over-week signup growth, proving the PostHog signal is false.
  - **Action:** Augment Code will prioritize fixing PostHog's accuracy, as other teams now rely on it for reporting.

### User Onboarding Flow

  - **Current Flow:** A multi-step, install-first process designed to filter out low-quality users.
    1.  CTA → Install page
    2.  Code editor button → Deep link triggers editor
    3.  Extension install
    4.  Extension login button → Website login form
    5.  Account creation → Triggers "signup" event
  - **Rationale:** This high-friction flow is a direct response to past fraud issues.
  - **Future:** A redesign of the install page and related assets is in progress.

### Content Strategy & Product Roadmap

  - **Current Focus:** Rewriting underperforming articles to improve install conversion.
  - **New Priority:** Create a content plan for the upcoming "Code Reviews" feature.
      - **Launch:** In \~2 weeks.
      - **Request:** A list of existing and planned SEO-focused blog posts.
  - **Product Roadmap:**
      - **Context Engine (MCCP):**
          - **Soft Launch:** Next week (friends & family).
          - **Public Launch:** January.
      - **Code Reviews:**
          - **Launch:** In \~2 weeks.

---

## Action Items

**Jason Gong**
- Add install-page visits to GrowthX tracking; report to Sylvain
- Send Sylvain SEO plan + post list for code review content
- Share rewrite before/after example w/ Sylvain

**Edin Abazi**
- Tag Sylvain on PRs for rewrites/experiments

---

## Transcript
**Jason Gong:** It was good.

**Jason Gong:** They just have to like review the content.

**Jason Gong:** I can give feedback before I shoot over to Edin.

**Jason Gong:** I think the content just looks much better.

**Jason Gong:** Like even if it might not perform that much better on SEO, but just like it passes the eye test a lot more.

**Jason Gong:** This meeting is being recorded.

**Jason Gong:** I was looking, I don't know if you spent much time on the Augment like funnel, but I know you mentioned like you had some thoughts on it.

**Jason Gong:** What exactly did you notice like when signing up for it?

**Edin Abazi:** Have you like tried the entire flow start to finish how it works?

**Jason Gong:** I've only up until like adding my payment method, which I'll probably do as well just to test it out.

**Jason Gong:** But like, yeah, did everything up until there.

**Edin Abazi:** The way it works right now is that say you.

**Edin Abazi:** You land on a post, on a guide, or a tool, article, whatever, and you see the CTA.

**Edin Abazi:** You click on the button, you get taken to the install page, you click on an additional button for your code editor.

**Edin Abazi:** You get taken to another page, which is supposed to trigger your code editor opening up.

**Jason Gong:** Yep.

**Edin Abazi:** And then the, yeah, the deep link opens, you have to click install on the extension.

**Edin Abazi:** The extension installs, and then you have a login button within the extension.

**Edin Abazi:** Then you have to press login, and then you get taken back to the website with a login form.

**Edin Abazi:** So nowhere within the flow itself is there a signup or anything.

**Jason Gong:** Sorry, nowhere within the flow is there.

**Edin Abazi:** There's no signup form anywhere.

**Edin Abazi:** It's all login forms, which, like, is fine, but, like, you're trying to optimize for, like, fast.

**Jason Gong:** I could probably give some suggestions on, like, the flow.

**Jason Gong:** My main question was just, like, if they changed anything, because, like, what I see is, like, we're driving, like, more people to the install page, but then it kind of just, like, I don't know what's happening after that, because they're not getting to whatever the sign-up event is.

**Jason Gong:** I mean, actually, the question was just, like, when this sign-up event occurs.

**Edin Abazi:** There's no, like, there's no sign-up in that entire flow.

**Jason Gong:** Well, like, I'm almost assuming, I mean, sign-up is just, like, some arbitrary event they made.

**Jason Gong:** Like, it might trigger at the screen I'm on right now, you know, which is, like, maybe it triggers here.

**Jason Gong:** I don't know.

**Jason Gong:** I mean, so, like, I think the flow can be better.

**Jason Gong:** I mean, I'm curious what other folks do, you know, like, I think you can just get somebody to sign up right from the beginning, and then at least you can nurture that email, you know.

**Jason Gong:** type of thing, and then send them to VS Code.

**Jason Gong:** I'm mainly just curious what has changed, because it feels like something happened like two weeks ago.

**Jason Gong:** What's up, Jason?

**Jason Gong:** Hey, Phil, how's it going?

**Sylvain Giuliani:** Well, good, let me just, I thought maybe I would go to the growthx office today, but I ended up in an office in the mission.

**Sylvain Giuliani:** Let me just connect to the Wi-Fi on my laptop.

**Jason Gong:** I don't even know if anyone's there.

**Sylvain Giuliani:** Is Marcel there today?

**Sylvain Giuliani:** That's cool.

**Sylvain Giuliani:** like, I drove by, I was like, oh, sure, I just did a meeting in BFS.

**Sylvain Giuliani:** was like, forget it.

**Jason Gong:** I'll go somewhere else.

**Sylvain Giuliani:** Where am I?

**Sylvain Giuliani:** Okay, cool.

**Sylvain Giuliani:** I'll just connect on my Wi-Fi for two seconds.

**Jason Gong:** Lots of questions for you today.

**Jason Gong:** I've been digging into this conversion funnel a little bit.

**Jason Gong:** Anyway, when you connect, I'll show you.

**Sylvain Giuliani:** What I've been looking at.

**Sylvain Giuliani:** Yeah, I can see it on my phone.

**Sylvain Giuliani:** Hold on, let me get Zoom started.

**Sylvain Giuliani:** Syncy, syncy.

**Sylvain Giuliani:** Okay, let me.

**Sylvain Giuliani:** All right, I'm here.

**Sylvain Giuliani:** What's up, Edin?

**Edin Abazi:** Didn't see you on my phone.

**Edin Abazi:** What's up?

**Jason Gong:** How's it going?

**Jason Gong:** All right, cool.

**Jason Gong:** So, let's give you a quick update and then some of the digging I've been doing.

**Jason Gong:** But this week, traffic dropped because of a few articles that seem to have, like, just fell out of some rankings.

**Jason Gong:** So, we're going to rewrite them.

**Jason Gong:** And then the part that I want to dig into is, so, like, what I've been noticing over the last couple weeks is, like, you drive a lot of people to the install page, and then, but, like, signups is, like,

**Jason Gong:** Going in the opposite direction.

**Jason Gong:** I'm like, okay, so it's probably a bunch of reasons.

**Jason Gong:** Like maybe the quality of people is just like complete garbage.

**Jason Gong:** But like, I think what I see on my end is like the same article is not driving people to signups.

**Jason Gong:** So then I kind of dug a little bit deeper.

**Jason Gong:** And what I see is like, you know, the percentage of people are going to install relatively stable.

**Jason Gong:** And then it looks like maybe like two weeks ago, just like this signup event is just like not firing.

**Jason Gong:** Like the conversion to that has just dropped.

**Jason Gong:** this applies both like for our content.

**Jason Gong:** But it also seems to be happening on your homepage.

**Jason Gong:** And just like all these changes.

**Jason Gong:** Like the signup event.

**Sylvain Giuliani:** I don't know.

**Sylvain Giuliani:** Because, yeah, on PostHog, I guess it's the same thing on our own internal data, you know, like the dbt project. The shape is completely different.

**Edin Abazi:** So, yeah.

**Jason Gong:** It's funny, because, like, at Kite, we have the same problem, because, like, you're trying to install, you get something to install an extension, but you're trying to trigger it from a web page, and it's not, like, the easiest flow, you know?

**Edin Abazi:** I'm sorry, Zoom just decided to crash on my laptop.

**Sylvain Giuliani:** So I don't know when you actually cut.

**Sylvain Giuliani:** But, yeah.

**Sylvain Giuliani:** What I was saying is, like, we need to clean up postdoc on our side.

**Sylvain Giuliani:** Like, I don't super trust all of the data because our internal data — with dbt and SQL — shows the overall sign-up trend is going the opposite direction.

**Sylvain Giuliani:** We're actually growing week over week.

**Sylvain Giuliani:** And so I don't know what's happening between those things.

**Jason Gong:** Okay.

**Sylvain Giuliani:** So that's the, I mean, we have so much, like, fraud effort, right?

**Sylvain Giuliani:** So it's like, it could just be, like, something that is, like, blocking the tracking or, like, there's a million things that could happen here.

**Edin Abazi:** One more thing is that ad blockers block postdoc completely.

**Edin Abazi:** Yeah.

**Edin Abazi:** Developers tend to use ad blockers.

**Sylvain Giuliani:** So all the events are set aside with our own proxy. We proxy all the calls to our own domains for client-facing events. And I think signup events especially are set aside, which should make everything perfect — but the chart should not look like this, if you hear what I'm saying.

**Sylvain Giuliani:** This is, like, I can show you on our data real quick here.

**Sylvain Giuliani:** And, you know, let me show you this.

**Sylvain Giuliani:** It's a bit slow, I'm on my phone and WiFi, but let me load this data.

**Sylvain Giuliani:** You can see the weekly trend — before October there was lots of fraud, we did a big cleanup, and now the weekly numbers are going in the right direction. Same thing in the last few days — we had really good days of signup.

**Sylvain Giuliani:** If you look at PostHog, you can see dips on weekends, but interestingly the weekly numbers aren't trending the way they should. Without any fraud data, I'd assume PostHog should report even higher numbers.

**Sylvain Giuliani:** If we detect a new type of fraud, we react actively remove everybody from those charts here.

**Sylvain Giuliani:** So this is like the cleanness we can ever get every time, right?

**Jason Gong:** So that's what I mean.

**Jason Gong:** Okay, so that makes sense.

**Jason Gong:** I guess in terms of things where...

**Sylvain Giuliani:** We're going to fix it because other teams are adopting PostHug now to do reporting.

**Jason Gong:** things like that, right?

**Jason Gong:** yeah.

**Jason Gong:** Okay.

**Jason Gong:** Well, I guess in any case, I mean, we're still thinking of things like within our control a little bit.

**Jason Gong:** So we're setting up some A/B testing to play around with the CTAs. We're still almost 100% focused on rewrites. As we're rewriting, we're focused on whether the content drives people to signup. So within the signup flow, is this where the signup event is triggered — where I give you my email and create an account?

**Sylvain Giuliani:** Yeah, here you have a signup event, yeah.

**Sylvain Giuliani:** So at that point, your account is created and we trigger a signup event on the backend — whether you had payment validation or not doesn't matter.

**Jason Gong:** Makes sense.

**Jason Gong:** I mean, we had some suggestions for this. I know it's like out of scope a little bit, but did you guys at any point try to just get people's email at the beginning and then nurture them?

**Sylvain Giuliani:** Yeah, we considered that.

**Sylvain Giuliani:** Thinking about it, to be honest, right now the biggest fight is fraud. It's okay to have friction and worry about converting people later. We don't do email first. The install-first flow is to ensure we're filtering for quality users.

**Sylvain Giuliani:** Like, before people could sign up on the web and then install, like, you know, our flow was, like, sign up first, install second.

**Sylvain Giuliani:** The problem is, like, you can install from lots of different places.

**Sylvain Giuliani:** You can install from LCLI.

**Sylvain Giuliani:** And so we just, we're standardizing on install first flow, basically.

**Sylvain Giuliani:** But this page has been redesigned, all this, like, install page and things like that are being redesigned.

**Jason Gong:** So I guess maybe the other metric I'll just add until you're more confident in the sign-up, then it's like, I'm just going to start tracking this, like, install page, because it's like, I think there's the risk that, like, okay, hey, we're just driving a bunch of low-quality people here, but it seems like at least this number follows, like, just a regular pattern.

**Sylvain Giuliani:** Yeah, yeah, so I think for now it's kind of, like, fine.

**Sylvain Giuliani:** think, like said, like, I'm trying to get the work prioritized to, you know, post-talk, I mean, to make post-talk more accurate for everyone, so.

**Jason Gong:** Okay, sounds good.

**Jason Gong:** So, okay, so we're doing a bunch of experiments on the CTAs, you know, and we're just entirely focused on refreshes, because it's still working really well.

**Jason Gong:** Like, I can see the install percentage improving every time we do.

**Jason Gong:** The refresh, the sign-up is just, yeah, that's the one we're, I'm a little confused by.

**Jason Gong:** So we're doing that, doing A-B testing, I think Marisol and Liz were talking to Jason, but it seems like that is, like, we're unblocking him, but we need to check that thread, and then the newsletter.

**Sylvain Giuliani:** I mean, I can, I mean, he's online this week, so.

**Jason Gong:** And then the newsletter, I think it's, it's slightly lower priority, but that it's also in our, in our queue.

**Jason Gong:** Anything, yeah, I mean, anything in particular?

**Sylvain Giuliani:** No, I think what we want to see is, like, we, so, like, it's only last time, we, we're releasing in two weeks code reviews, but we'd love to have, like, a better view of, like, what are we doing content-wise towards targeting code reviews.

**Sylvain Giuliani:** Just give me a list of these other 10 blog posts I really wrote about, and these other 20 more we're going to earn, whatever the numbers are.

**Sylvain Giuliani:** Just kind of give me SEO-specific for code review product content that we're doing.

**Sylvain Giuliani:** So I know we already did this thing, but I would love to get this is what we're doing for this code review project.

**Sylvain Giuliani:** And then there's more things going on, but basically the Context Engine and MCCP stuff I talked to you about last week — we're going to launch it next week in a super soft release, like a friends and family test. And the goal is to launch it properly in January after the holiday.

**Jason Gong:** So I'll share that with you. I'll share more details once we kick off the experiment. And I want to show you what good looks like for a rewrite, so you have a mental picture of the before and after.

**Sylvain Giuliani:** Sounds good. Send me an async update as things progress. Edin, you have access to PostHog, right? I invited you yesterday. Let me know when you push these things. Just tag me on the PRs to keep me in the loop.

**Edin Abazi:** Yeah, sounds good.

**Sylvain Giuliani:** Sounds good.

**Sylvain Giuliani:** Anything else?

**Jason Gong:** I think that's it.

**Jason Gong:** I'll do a short one.

**Jason Gong:** right.

**Jason Gong:** See you later.

**Jason Gong:** Thanks, guys.

**Jason Gong:** See you.

**Jason Gong:** Bye.
