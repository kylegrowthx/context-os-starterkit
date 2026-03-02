# Lane Sync: Client Ops Kick-Off

<metadata>
date: 2025-12-02
time: 18:00 UTC
duration: 29 minutes
organizer: daniel@growthxlabs.com
participants: Kirkland Gee, Marcus Derencius, Nicolas Castellanos, Isaac Dudek, Sergey Kaplich, Tamyres Ogasawara, Daniel Lopes
enriched_on: 2026-03-01 00:00 UTC
fathom_recording_id: 105651253
fathom_url: https://fathom.video/calls/491735953
share_url: https://fathom.video/share/tyK71gHttyJ9fanf9Q4DTF8afxJdwQp8
source: fathom
</metadata>

---

## Summary

Kick off the client ops cycle and onboard new team members.

---

## Context

GrowthX held its client operations cycle kick-off meeting on December 2, 2025, bringing together the core client ops engineering team for planning and onboarding. The team includes three new engineers joining in this cycle: Tamyres Ogasawara (Brazil, 10 years of SEO and tech experience), Sergey Kaplich (New York, 7 years of content marketing and recent pivot to front-end development), and Isaac Dudek (Los Angeles, long career in web development who will split time between client ops and the product team). The meeting was facilitated by Kirkland Gee and included existing engineers Marcus Derencius and Nicolas Castellanos, with Daniel Lopes joining from leadership.

---

## Relevance

- **To GrowthX Delivery:**
  - Onboarding methodology: New team members will learn through pairing sessions on real client work rather than solo tickets, reducing ramp-up risk and knowledge loss.
  - Agentic pipeline migration completion: Clearing the backlog of pending client feedback by EOW frees the team to focus on new work and eliminates tracking overhead.
  - Framer workflow debugging: The intermittent publishing bug affects client deliverables. User error (not keeping MCP plugin open) is suspected but requires observation with the delivery team to confirm.
  - Nano Banana image generation adoption: High-quality infographic generation now viable with minimal setup (just prompt, reference images, brand colors) — represents major efficiency gain for clients needing on-brand visuals.

- **To GrowthX Business Development:**
  - New account readiness: Three strong new hires (combined 20+ years of tech/content experience) signal team scaling capacity to support new client growth.
  - Delivery capability expansion: Nano Banana workflow and competitor content gap analysis tools represent new service offerings with quantifiable quality improvements over prior image generation attempts.
  - Client satisfaction signals: Framer publishing workflow issues must be resolved to maintain delivery quality; unclear scope of Pages Inventory feature requires clarification to set client expectations.

---

## Overview

- **Onboarding Focus:** The cycle's top priority is onboarding new team members (Tamyres, Sergey, Isaac) via pairing sessions on key tickets.
- **Agentic Pipeline Closure:** The team will finalize the multi-month agentic pipeline migration, closing any tickets lacking client feedback by EOW to clear the backlog.
- **Framer Workflow Debug:** A persistent, intermittent Framer publishing bug will be debugged. The primary hypothesis is user error (failing to keep the MCP plugin open), but a workflow-side parsing issue is also suspected.
- **New Tech Adoption:** The team will push for wider adoption of the new "Nano Banana" image generation workflow, which produces high-quality, on-brand infographics with minimal effort.

---

## Key Topics

### Onboarding & Cycle Plan

  - **Primary Goal:** Onboard new team members (Tamyres, Sergey, Isaac) through hands-on pairing sessions.
  - **Ticket Assignment:** New members will not take on solo tickets this cycle.
  - **On-Call Role:** A lighter workload allows the on-call engineer (Kirkland) to provide immediate support for critical bugs or new client requests.
  - **Local Setup:** New members must install the local development environment (Atlas) to participate in pairing and debugging.

### Agentic Pipeline Migration

  - **Status:** The multi-month migration of client workflows to an agentic model is nearly complete.
  - **Blocker:** A few tickets are pending client feedback for final review.
  - **Decision:** All pending tickets will be closed by EOW if no feedback is received.
      - **Rationale:** This clears the backlog and removes the mental overhead of tracking unfinished work.
      - **Action:** Clients will be notified that they must file a new, reprioritized ticket if they still need the work.

### Framer Publishing Workflow

  - **Issue:** A workflow for publishing content to Framer is intermittently failing, causing confusion.
  - **Symptoms:**
      - **Intermittent Failures:** The workflow fails unpredictably.
      - **False Negatives:** The workflow sometimes fails in Atlas but successfully publishes the content to Framer.
      - **Long Run Times:** One instance ran for 98 minutes, likely due to a timeout loop.
  - **Hypotheses:**
      - **User Error:** The delivery team may not be keeping the Framer MCP plugin open, which is required for the workflow to connect.
      - **Workflow Bug:** The workflow may be failing to parse the success message from Framer, leading to a false negative status in Atlas.
  - **Action:** Kirkland will meet with the delivery team to observe their process and rule out user error before debugging the workflow itself.

### New Tech Adoption

  - **"Nano Banana" Image Generation:**
      - **Performance:** The new workflow produces high-quality, on-brand infographics with consistent logos and colors.
      - **Efficiency:** Requires only a prompt, reference images, and brand colors—no HTML or complex setup.
      - **Goal:** Identify clients who can benefit from this workflow to improve efficiency and content quality.
  - **Content Gap Analysis:**
      - **Need:** A workflow to research competitor pages for a given keyword and generate a report.
      - **Status:** Unclear if this is already covered by the "Pages Inventory" feature in development. Kirkland will ask Daniel for clarification.

### Pairing Opportunities

  - Kirkland will schedule pairing sessions for new members on these tickets:
      - **Sunbit:** Generate case studies.
      - **Sanity:** Update a publishing workflow.
      - **Tag:** Add writing guidelines as an input to a translation workflow.
  - Marcus will pair with a new member on the Sanity ticket.

---

## Action Items

- **Kirkland Gee (GrowthX):**
    - Schedule pairing sessions for new members on Sunbit (case studies), Sanity (publishing workflow), and Tag (translation guidelines) tickets.
    - Meet with Andi Bailey (GrowthX) to observe the Framer publishing workflow process and rule out user error before debugging the workflow itself.
    - Ask Daniel Lopes (GrowthX) for clarification on the scope of the "Pages Inventory" feature in development.
    - Send a message to Andi Bailey (GrowthX) asking her to identify which clients would benefit from the new "Nano Banana" image generation workflow.

- **Marcus Derencius (GrowthX):**
    - Pair with a new member on the Sanity publishing workflow ticket.

- **Tamyres Ogasawara (GrowthX):**
    - Complete local development environment (Atlas) setup.

- **Sergey Kaplich (GrowthX):**
    - Complete local development environment (Atlas) setup.

- **Isaac Dudek (GrowthX):**
    - Complete local development environment (Atlas) setup.

---

## Transcript
**Kirkland Gee:** This meeting is being recorded.

**Tamyres Ogasawara:** Hello.

**Kirkland Gee:** Good morning.

**Sergey Kaplich:** Good afternoon.

**Sergey Kaplich:** Hey, hey.

**Isaac Dudek:** Hi.

**Kirkland Gee:** How are you all doing?

**Sergey Kaplich:** Pretty good.

**Isaac Dudek:** Not too bad.

**Kirkland Gee:** How was the rest of yesterday?

**Tamyres Ogasawara:** Honestly, still like, yeah, still.

**Tamyres Ogasawara:** It's studying a lot.

**Kirkland Gee:** I would say.

**Kirkland Gee:** It's a lot of information to kind of take in for a little bit.

**Tamyres Ogasawara:** For sure.

**Sergey Kaplich:** Yeah.

**Marcus Derencius:** Hello.

**Marcus Derencius:** Your face.

**Marcus Derencius:** Welcome.

**Tamyres Ogasawara:** Thank you.

**Isaac Dudek:** It's good to be here.

**Marcus Derencius:** Nice.

**Nicolas:** Hey.

**Kirkland Gee:** Hey, Nicolas.

**Nicolas:** Oh, nice background, Marcus. Where are you?

**Marcus Derencius:** Yeah, I'm in northeast of Brazil.

**Marcus Derencius:** Nice little town.

**Marcus Derencius:** Yeah, there's a swimming pool over there.

**Kirkland Gee:** Wow.

**Kirkland Gee:** Incredible.

**Kirkland Gee:** I'm trying to finish up my lunch. I was trying to finish it before we started this meeting, and there's just a tiny little bit left here.

**Kirkland Gee:** Have you guys all met yet?

**Nicolas:** No.

**Kirkland Gee:** No.

**Kirkland Gee:** Okay.

**Kirkland Gee:** I'm sure you guys have done plenty of introductions, but just for the sake of Marcus and Nico, because I think Daniel probably is coming to this meeting, might not, but he's already met you guys.

**Kirkland Gee:** We can just do a quick round of very short intros before we get into everything.

**Tamyres Ogasawara:** For sure.

**Tamyres Ogasawara:** Hello.

**Tamyres Ogasawara:** My name is Tamyres.

**Tamyres Ogasawara:** I'm from Brazil.

**Tamyres Ogasawara:** I'm 26.

**Tamyres Ogasawara:** I'm married.

**Tamyres Ogasawara:** I live in Sao Paulo, more specifically.

**Tamyres Ogasawara:** So that's why I was saying the Southeast is already killing me. It's so hot here.

**Tamyres Ogasawara:** It's starting the summer season.

**Tamyres Ogasawara:** So I'm here to work as a content ops engineer.

**Tamyres Ogasawara:** I've been working with SEO and working with tech in general for the past 10 years.

**Tamyres Ogasawara:** And I'm very happy to be here and to help you guys as much as I can.

**Sergey Kaplich:** Okay, I can go next.

**Sergey Kaplich:** My name is Sergey.

**Sergey Kaplich:** Originally, from Russia, but now I live in the United States.

**Sergey Kaplich:** I live here for four years already.

**Sergey Kaplich:** I live in New York.

**Sergey Kaplich:** It's pretty nice here.

**Sergey Kaplich:** I love it so much.

**Sergey Kaplich:** Yeah, I had a huge career in content marketing.

**Sergey Kaplich:** I spent there like seven years.

**Sergey Kaplich:** And after that, I moved to front-end engineer.

**Sergey Kaplich:** I work as a web developer.

**Sergey Kaplich:** I create like my own agency where I was making like websites and web apps.

**Sergey Kaplich:** And now I'm here working as a client operations engineer.

**Sergey Kaplich:** Yeah, that's pretty much it.

**Isaac Dudek:** I'm tech tool

**Isaac Dudek:** And I'm Isaac, based in L.A.

**Isaac Dudek:** I've actually lived all over California.

**Isaac Dudek:** I've been in the Bay Area for a bit and other parts, but L.A.

**Isaac Dudek:** is where I went to university and it's my preferred part of the state, so that's where I'm at now.

**Isaac Dudek:** Also had a long career in tech, web development.

**Isaac Dudek:** I think like a lot of people, it started when I was young and was really into video games.

**Isaac Dudek:** That sort of got me into coding.

**Isaac Dudek:** And, yeah, super excited to be here.

**Isaac Dudek:** There's so much amazing stuff going on.

**Isaac Dudek:** I will be working on the product team, but I think I'm doing some client-off stuff here in the beginning for a couple weeks.

**Isaac Dudek:** So, yeah, excited to help out.

**Kirkland Gee:** Awesome.

**Kirkland Gee:** And also they gave me enough time to eat my last two wings.

**Kirkland Gee:** So Marcus and Nico, if you can give these guys a quick intro to you guys as well.

**Nicolas:** Uh, sure.

**Nicolas:** Uh, I'm Nico.

**Nicolas:** I'm based in Uruguay, Montevideo.

**Nicolas:** I

**Nicolas:** I'm actually enjoying the hot weather right now.

**Nicolas:** I've been doing web and web development for like nine years now.

**Nicolas:** I joined in June.

**Nicolas:** And aside from work, I love go-karts and planes.

**Nicolas:** And that's me.

**Nicolas:** And welcome, you all.

**Marcus Derencius:** So I'm Marcos.

**Marcus Derencius:** I'm also from Sao Paulo, so I'm from Brazil.

**Marcus Derencius:** I split part of my time between Brazil and Europe.

**Marcus Derencius:** I like to stay in Portugal as well.

**Marcus Derencius:** So I've been a web developer for the last 20 years, guess.

**Marcus Derencius:** So I was building a lot of Ruby on Rails apps.

**Marcus Derencius:** And I was working remotely.

**Marcus Derencius:** That's why I travel a lot, because also I like sports.

**Marcus Derencius:** So here where I am, I do kitesurfing.

**Marcus Derencius:** In the winter, I do snowboarding.

**Marcus Derencius:** But also I like writing code a lot, so you're welcome.

**Marcus Derencius:** I hope you like using code code, and let's have fun using AI for everything.

**Kirkland Gee:** Literally for everything.

**Kirkland Gee:** Okay, very cool.

**Kirkland Gee:** I know Stevie's in another meeting, so she messaged me and said we could just run this.

**Kirkland Gee:** I think moving forward, after at least the next couple of weeks, we'll just be running it without her anyways, so she can spend time helping the other product teams.

**Kirkland Gee:** And I'm going to kind of take over most of the prioritization work, and we'll run with that.

**Kirkland Gee:** I think Andy's not here, but she's in office, so she may also not be in this meeting.

**Kirkland Gee:** Context for new folks.

**Kirkland Gee:** This is just our cycle planning meeting.

**Kirkland Gee:** We'll kind of just talk through tickets that are coming up for this cycle.

**Kirkland Gee:** And normally we have Andy, who's like the...

**Kirkland Gee:** The head of everything on the client side, feels like, kind of has her hands on everything, knows all the context, knows which clients need attention, and is usually very helpful in, like, making sure we're not missing anything or get questions about a particular ticket that's been filed, things like that.

**Kirkland Gee:** But since she's not here, we'll go ahead and jump into some stuff.

**Kirkland Gee:** It's not, I don't think there's a whole lot going on looking at this next cycle.

**Kirkland Gee:** Like, finally are done with a lot of the bigger projects.

**Kirkland Gee:** There's not anything too crazy.

**Kirkland Gee:** A couple of things just to talk about.

**Kirkland Gee:** Again, big focus for this is going to be getting you guys up to speed on everything.

**Kirkland Gee:** I think we talked about this, but plan is not for you guys to be taking on really any issues of your own in this first two-week cycle, but just joining us on.

**Kirkland Gee:** I have a couple we'll talk about that I think will be good opportunities for you guys to get a feel for how certain pieces of things are working.

**Kirkland Gee:** The only big thing that I think would be...

**Kirkland Gee:** Really good to just be done with forever at the end of this two weeks is all the agentic pipelines.

**Kirkland Gee:** So for the last two or three months, we've been kind of migrating a lot of our customer workflows to have a more agentic model.

**Kirkland Gee:** We talked about some of those agentic workflows yesterday and how they're self-evaluating, all that stuff.

**Kirkland Gee:** It takes some time to set up the artifacts and the things that are being referenced for each customer and make sure that they're doing a good job.

**Kirkland Gee:** And if you look in linear, there's a whole project.

**Kirkland Gee:** We've been doing like 30 plus of these over the last few weeks, and basically all of them are done.

**Kirkland Gee:** I think there's like two that are left in review.

**Kirkland Gee:** Like we've done the work and we're just kind of waiting on customers to get back to us.

**Kirkland Gee:** I don't think there's anything really to think about on that other than making sure those last couple get closed out.

**Kirkland Gee:** And then we don't ever hopefully have to really think about that again.

**Kirkland Gee:** But Marcus, Nico, anything I'm forgetting or anything that you...

**Kirkland Gee:** I had a note to like, are there any specific...

**Kirkland Gee:** Delivery team folks that we're just not hearing from, I was going to check with Andy, but she's not here, so.

**Kirkland Gee:** But is there anything you guys need support or are just waiting?

**Marcus Derencius:** Yeah, I have, like, tickets there.

**Marcus Derencius:** just did a review and ping some editors, so they give some feedback so I can wrap up or pause the pic.

**Marcus Derencius:** So they didn't confirm, so I will list the items.

**Kirkland Gee:** so, yeah, I post on the Slack channel for them on the text on Slack.

**Kirkland Gee:** I think my thought is, like, by the end of this cycle, I just want to close this out.

**Kirkland Gee:** Like, if people haven't given us feedback over the next two weeks, if anything's still hanging, I think we can communicate that.

**Kirkland Gee:** But just, like, we're not going to touch it.

**Kirkland Gee:** They'll need to file a new issue and get reprioritized or something because, you know, the mental weight of just having this still sitting here is kind of annoying.

**Kirkland Gee:** And it's pretty much all done.

**Kirkland Gee:** So.

**Kirkland Gee:** So we can let them know if anybody's like really not getting back to us by like end of this week.

**Kirkland Gee:** Just say like, hey, if you don't get to us next week, this is we're going to mark this as done and move on.

**Kirkland Gee:** I've doing that a lot.

**Kirkland Gee:** Yesterday I went through and probably closed out like you guys probably saw some things like 15 tickets.

**Kirkland Gee:** I was just like, this is no one's thought about this in three months.

**Kirkland Gee:** It's done.

**Kirkland Gee:** If you need it, refile it.

**Kirkland Gee:** It's kind of my philosophy is like if no one's thought about it in three months, we don't need it.

**Kirkland Gee:** Probably.

**Kirkland Gee:** So a couple of things just to kind of talk through.

**Kirkland Gee:** There's a newsletter pipeline I need to ask Andy about.

**Kirkland Gee:** I'll skip this for now.

**Kirkland Gee:** I know, Marcus, you saw this, a little weird bug where it's probably easy.

**Kirkland Gee:** I don't know what's easier to share my screen because I can't share Notion and Linear at the same time.

**Kirkland Gee:** But we're like some random link showed up in some research that was redirecting to something spammy.

**Kirkland Gee:** I don't know.

**Marcus Derencius:** It's probably worth just adding a filter, like you said, some kind of validation.

**Marcus Derencius:** Yeah, that's not tweaking well.

**Kirkland Gee:** There's no real way to know for sure whether that redirect is malicious or not.

**Kirkland Gee:** It could have just been redirected to some other page.

**Kirkland Gee:** I don't know, maybe if the redirect returns to not the same domain, that's probably a signal that something's wrong.

**Marcus Derencius:** Yeah, it's not an absolute rule, so you cannot rule that.

**Kirkland Gee:** I don't know, I don't think it's happening a ton, but it got filed, so we'll take a look at it.

**Kirkland Gee:** And then this one, I know Marcus, you briefly looked at this too.

**Kirkland Gee:** I put you on this, but Nico, if you have any interest.

**Kirkland Gee:** Basically, I've been trying to get a workflow to publish on Framer working with their MCP server for like three weeks.

**Kirkland Gee:** And I'm at the point where sometimes it works.

**Kirkland Gee:** There's no rhyme or reason. You have to be logged in and use the URL related to your account that you're logged in with, with the plugin open in their CMS to get the workflow to even run at all or to connect to their MCP server.

**Kirkland Gee:** And it's like very often, if I'm just running it locally, it works most of the time, but in Atlas, it will run, but then it won't return like a success back, but the post will still show up in Framer sometimes.

**Kirkland Gee:** And I'm just like hitting my wits end of like, I can't sort it out.

**Kirkland Gee:** So I need to tag one of you guys in to see if you can see something I'm not sure about.

**Marcus Derencius:** And what machine were you running in Framer, the desktop app on your machine, or the client was using the Framer desktop?

**Marcus Derencius:** So that's what I understand.

**Kirkland Gee:** So someone has to be running.

**Kirkland Gee:** You can even just do it in the web browser, like on Framer.com.

**Kirkland Gee:** If you're logged in, you have to turn on the plugin. Basically, this is not hyper-technical, but let me show you an example.

**Kirkland Gee:** So, basically, if you go into whatever website we're in on Framer, either desktop app or web, you have to go into plugins, and you have to run the MCP plugin here.

**Kirkland Gee:** And then I have it set up where this URL is an input into that workflow.

**Kirkland Gee:** And so then, if you go use this as an input, run the workflow, it's, in theory, supposed to go talk to Framer and back and forth and publish.

**Marcus Derencius:** From what I understand, it's going to work until you keep this page.

**Marcus Derencius:** Open.

**Marcus Derencius:** If you close the browser on your machine, it's going to stop working.

**Kirkland Gee:** So that's what I understand.

**Kirkland Gee:** That's what I thought too.

**Kirkland Gee:** But I'm running into places where like the delivery team, even though I think I've made this very clear, maybe they are like not keeping this open or their browser is like sleeping that page while it's running or something is maybe a possibility.

**Kirkland Gee:** But even when it works from Atlas, like there are places where the workflow is failing, like it's not getting a success back, but it is showing up in Framer.

**Kirkland Gee:** But like this one I published fine, but where's the, not this one.

**Kirkland Gee:** I think it's this one that has a bunch of failed.

**Kirkland Gee:** No, that one doesn't even have the publish.

**Kirkland Gee:** Have they really tried this?

**Kirkland Gee:** Interesting.

**Kirkland Gee:** Maybe I need to actually dig deeper into what they're even, because from what I understood, Bailey was basically saying, hey, I'm running this, let go find, maybe I'm just looking at the wrong thing.

**Kirkland Gee:** Yeah, so this was, okay, it's in the deep dives.

**Kirkland Gee:** I just was missing this.

**Kirkland Gee:** Yeah, so like all of these are failing.

**Kirkland Gee:** And some of them were because there were like missing inputs or things like that.

**Kirkland Gee:** But this one in particular, at least, for no reason I can gather, like this ran for 98 minutes.

**Marcus Derencius:** Yeah, that's one that I did some debugging, so it was not getting a collection data, it was offline.

**Marcus Derencius:** the MCP was offline and kept trying one at time.

**Kirkland Gee:** So maybe it is just that they're not keeping it open.

**Kirkland Gee:** And that's why it's doing or something.

**Kirkland Gee:** Maybe that hasn't been super clear.

**Kirkland Gee:** Because when I've run it, I've seen cases where it fails in Atlas, but does actually publish.

**Kirkland Gee:** Because I think it's just not returning some, like I'm not parsing the success message properly in the workflow somehow.

**Kirkland Gee:** But, okay.

**Kirkland Gee:** I just wanted to talk about that because I'm feeling like lost.

**Kirkland Gee:** But maybe it is just as simple as they're not keeping the plugin open.

**Marcus Derencius:** Yeah, I did debugging and found the diagnosis. It was not running because the plugin wasn't running on Framer.

**Marcus Derencius:** So that's why I was going to ask you, if you're, you really have to run the plugin before running the workflows.

**Kirkland Gee:** Okay, I'll take this. I've already talked to Andi Bailey so much, so I'll have a meeting with her and ask, hey, can you show me how you're doing this? That way we can make sure there's not some miscommunication. If I come up with some other bug, I'll tap one of you guys back in.

**Kirkland Gee:** But if it's that simple and I'm just maybe too trusting, but okay.

**Kirkland Gee:** So that's that.

**Kirkland Gee:** There's another client that wants to do the same thing.

**Kirkland Gee:** So once I work out and make sure what's going on there, we can set it up for Tiro because they're also on Framer.

**Kirkland Gee:** And then another thing I wanted to talk about, I think I showed you, I think you guys have all seen this, but there's a new like Nano Banana image creation workflow that's doing really well.

**Kirkland Gee:** Like it's so much better than any of the stuff that we've done before with Nano Banana Pro.

**Kirkland Gee:** I don't have like a ton of image generation tickets right now or anything, but I think it could be worth us like just trying to start.

**Kirkland Gee:** I don't know if we just ask people like where it's most useful.

**Kirkland Gee:** I just think we should use it because this is like for Galileo, like this is the kind of stuff that it's generating just off of prompts and some reference images.

**Kirkland Gee:** And some of these aren't.

**Kirkland Gee:** Perfect, but like this one here is like, it's so small, but like it's pretty solid, the logos are really consistent, like, he kind of made up some logos in some cases, but like that one's correct.

**Kirkland Gee:** And for Strapi, it, like they've been so particular about images and it finally did a really, really good job.

**Kirkland Gee:** I just gotta remember, where is it, this one?

**Kirkland Gee:** Yes.

**Kirkland Gee:** Like this is very cool, like their logo's staying in the top right, super consistently, logos not changing, fonts aren't changing, colors are pretty consistent.

**Kirkland Gee:** So I just think we can do a lot with this.

**Marcus Derencius:** And did you need help from Katia for those, or you just rolled the points?

**Kirkland Gee:** No, this is like super simple, like this Strapi one, literally all I did was give it this, and say, hey, here's the background.

**Kirkland Gee:** is skewer.

**Kirkland Gee:** And you

**Kirkland Gee:** And then make informational infographics based on the content in the article.

**Kirkland Gee:** Here's your brand colors.

**Marcus Derencius:** And that's it.

**Kirkland Gee:** That's a book.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** You don't need do any HTML, any, anything.

**Kirkland Gee:** Like, it's really, really good if you just give it good reference images.

**Kirkland Gee:** Nice.

**Kirkland Gee:** So, Galio is, like, not quite as good.

**Kirkland Gee:** Again, like, this is very, very consistent.

**Kirkland Gee:** Galio is having a bit of, like, weirdness with the logos and stuff.

**Kirkland Gee:** I just think there's got to be other places where this could save us a ton of headache and give the team a lot better.

**Kirkland Gee:** Basically, anybody that's wanted, like, an infographic.

**Kirkland Gee:** And, again, context for everyone else.

**Kirkland Gee:** Trying to generate AI infographics, if you haven't tried to do it before, is, like, was literally impossible.

**Kirkland Gee:** And then Nano Banana Pro came out, like, last week or week before.

**Kirkland Gee:** And it, like, two hours of tinkering with the prompt in the workflow, and it's getting great results.

**Kirkland Gee:** So I was going to ask Andy, where should we prioritize this?

**Kirkland Gee:** So I think I'll just have to send her a message after this, and if I get anything, I'll file some extra tickets for that stuff.

**Kirkland Gee:** Same thing with this one.

**Kirkland Gee:** I saw this, like, actually, maybe one of you guys know.

**Kirkland Gee:** There's this ticket that someone had a request on a long time ago that got followed up on two different times about doing, like, no, that was a different thing.

**Kirkland Gee:** But there's this thing about content gap analysis, and there's a separate request about, like, competitor research stuff.

**Kirkland Gee:** Where people are kind of looking for a workflow to, for a given, you know, keyword a page wants to rank for, do some research on the other pages and give them some kind of report or something.

**Kirkland Gee:** I think that's going to be in, like, the pages inventory feature that Daniel and Brad are working on.

**Kirkland Gee:** I'm pretty sure that's included, but I wasn't 100% sure on how much of that is actually built in or what it actually does.

**Kirkland Gee:** So I was going to ask Daniel.

**Kirkland Gee:** I don't know if you guys happen to know.

**Kirkland Gee:** And then I have these three down here, just as notes, Sunbit needs to generate some case studies, there's a sanity publishing workflow, and there's a simple one for tag about adding guidelines as an input to a translation workflow, to like give a translation workflow writing guidelines for how to translate, so to speak.

**Kirkland Gee:** I think these are all good things for you guys to kind of pair with one of us on, because they're not super complicated, but they're good examples of the kind of things that we do pretty regularly of like automating publishing, creating some unique structure of content based on some kind of artifact input, and then kind of tweaking an existing pipeline.

**Kirkland Gee:** Right now, I just have myself assigned to these three. Marcus and Nico, I don't know what your weeks look like in terms of other tickets going on, but my plan for this week is to spend a lot of time with the new folks and help you guys get up to speed. If you guys want to pair with them on something, the idea is just for everyone to absorb as much information as possible over the next couple of weeks.

**Marcus Derencius:** Yeah, I can take a look at the Sanity publishing one, because I did the first one and it has some updates. We can pair together so I can help onboard someone.

**Kirkland Gee:** Yeah, I will tag you on that one.

**Kirkland Gee:** That's all the notes I had on things worth explicitly talking about.

**Kirkland Gee:** Looking at the cycle, there's a bunch of stuff that, like, in review just popped over from last cycle.

**Kirkland Gee:** I went through all of these.

**Kirkland Gee:** There's not anything that I think, like, we need to do anything on right now.

**Kirkland Gee:** Like, all of these are just waiting on somebody else.

**Kirkland Gee:** They're pretty much done.

**Kirkland Gee:** It's just, like, needs a stamp.

**Kirkland Gee:** A couple things opened up that were in progress from last time. A lot of this is because of the holiday last week — people just didn't get information to me, and now they are.

**Kirkland Gee:** And there's only a couple of unassigned tickets that are to do.

**Kirkland Gee:** So feel free to pick these up.

**Kirkland Gee:** This is that translation guidelines one that I was just talking about.

**Kirkland Gee:** I actually threw this one for me.

**Kirkland Gee:** Tiro, this is on Framer, so I'll tend to throw that to me as well, but I may pass that off.

**Kirkland Gee:** And there's a couple other small things.

**Kirkland Gee:** So any questions, anything you guys want to talk through?

**Kirkland Gee:** think this is pretty straightforward.

**Kirkland Gee:** It's also like compared to last cycle, like we were at, like, the scope is not a real number, by the way.

**Kirkland Gee:** These like point estimates, none of them are real.

**Kirkland Gee:** They're all made up.

**Kirkland Gee:** We kind of vaguely use them to sort of guess how long things would take, but we don't live by them at all.

**Kirkland Gee:** But this week, this cycle is going to be a little slower than last in some ways.

**Kirkland Gee:** Yeah, any other questions?

**Sergey Kaplich:** Yeah, I have a question.

**Sergey Kaplich:** Like, will you assign me as a containment to these tickets or should we assign ourselves?

**Kirkland Gee:** So normally we tend to assign ourselves, I think, for the most part, unless, like, in this meeting, we might say, like, oh, somebody should go take care of this one and take care of that one.

**Kirkland Gee:** But we historically have just kind of picked things up as we can, right?

**Kirkland Gee:** mean, there's a lot of the stuff that we're already assigned to is from previous weeks where we already started working on it and then it's come back again.

**Kirkland Gee:** And, like, I picked up a couple of these yesterday when I was doing cycle planning that I was, like, I'm either have the context on this or I'm the best person to handle that.

**Kirkland Gee:** So generally feel free to anything that's unassigned is always up for grabs.

**Kirkland Gee:** We generally assign ourselves.

**Kirkland Gee:** But as the team gets bigger and we start doing more stuff, maybe we start assigning a little bit more at the front end.

**Sergey Kaplich:** About this one you mentioned — you're going to pair with some of us. Should we assign ourselves, or will you let us know when you have time and we'll do it all together?

**Kirkland Gee:** My plan was to book some calendar time right after this meeting to work through some of these.

**Sergey Kaplich:** Got it, awesome, thanks.

**Sergey Kaplich:** And I have one more question.

**Sergey Kaplich:** On this doc, which you showed on the top, it was that you're on call during this cycle.

**Sergey Kaplich:** Can you please tell me a little bit how you work with on calls, and how it works, and what actually you are doing at this time?

**Kirkland Gee:** Yeah, so on call here is very different than if you've been an on call engineer in a previous job.

**Kirkland Gee:** All it really means is one of us, in theory, is going to have a few less tickets assigned so that we can keep an eye on it.

**Kirkland Gee:** Anything that's coming in and make sure like if there's a bug, if there's something that's breaking, that's like super important, that on-call person can jump on that and they won't be pulled away from some deeper, more complex work.

**Kirkland Gee:** That's basically, there's like a channel for BEPD client support, I think is the right channel, where as tickets are filed, they show up there.

**Kirkland Gee:** And you'll find Marcus, whether Marcus is on-call or not, he seems to always look at every single issue that comes in somehow.

**Kirkland Gee:** But that's just the idea.

**Kirkland Gee:** So that one of us is like designated as the right person for that.

**Kirkland Gee:** And if any like new customers are coming on, need like engineering support, the first person they'll go to is the on-call person.

**Sergey Kaplich:** Got it.

**Sergey Kaplich:** Awesome.

**Kirkland Gee:** It makes sense.

**Kirkland Gee:** Thank you.

**Sergey Kaplich:** Yeah.

**Marcus Derencius:** One question — does everyone have Atlas running on your machines so you can run workflows? You know, you have to have Atlas running locally to help with any of the tickets.

**Isaac Dudek:** Yeah, I'm in the process of setting that stuff up.

**Tamyres Ogasawara:** I don't have everything working yet, but it's on the list.

**Tamyres Ogasawara:** Yeah, I haven't set it up yet, but I'm going to do it, yeah.

**Marcus Derencius:** Yeah, so if you get stuck for any reason, we have documentation on how to run stuff. The faster you can get it running, the sooner you can help with the tickets and issues.

**Sergey Kaplich:** Awesome, yeah.

**Kirkland Gee:** 100%.

**Kirkland Gee:** Cool, any other questions?

**Kirkland Gee:** Thoughts?

**Kirkland Gee:** Okay, cool.

**Kirkland Gee:** I'm going to send a follow-up in the client ops channel and tag Andi on a couple of those questions to make sure we're not missing anything. You guys can expect some calendar invites from me to work on these things. I'll probably have all four of us working together so I don't have to pair off individually at first. And then we'll go from there.

**Sergey Kaplich:** Sounds great.

**Kirkland Gee:** Thanks, everybody.

**Kirkland Gee:** Thank you.

**Kirkland Gee:** Marcus, enjoy the pool.

**Sergey Kaplich:** Thanks.
