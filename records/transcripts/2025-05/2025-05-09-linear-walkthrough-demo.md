# Linear Walkthrough (Demo)

<metadata>
date: 2025-05-09
time: 15:31 UTC
duration: 19 minutes
organizer: vivek@growthxlabs.com
participants: Vivek Shankar, Elvis Goren, Nemanja Simic, Uros Popic, Marisol Smith
fathom_recording_id: 61770136
fathom_url: https://fathom.video/calls/295735899
share_url: https://fathom.video/share/VYrYDw7oK8NYoPzrSAA9ssTU-yPat74R
source: fathom
enriched_on: 2026-03-03 19:32 UTC
</metadata>

---

## Summary

Vivek Shankar walked the GrowthX delivery team through Linear's core features and use cases — explaining how it functions as a task management and Slack notification system for recurring client-related work like Monday updates, Looker reports, and post-call notes. The team discussed Linear's customizable views, filtering options, and task-creation workflows, with action items around exploring the tool and troubleshooting a Smith.ai Slack integration issue.

---

## Context

This was an internal training session for the GrowthX delivery team — Elvis Goren, Nemanja Simic, Uros Popic, and Marisol Smith — to learn how to use Linear, a project management tool that Vivek Shankar (the organizer) had set up for tracking client-related tasks and work cadence. The team had been using Linear but lacked clear guidance on its purpose and functionality, so Vivek delivered this walkthrough to clarify how to best leverage the tool. The meeting also surfaced a technical issue with the Smith.ai internal Slack channel integration not receiving Linear notifications, which required follow-up with the build team.

---

## Relevance

- **To GrowthX Delivery:** Linear is now the primary system for tracking recurring client deliverables (Monday updates, Looker reports, meeting agendas, post-call notes) and one-off project tasks. Team should check "My Issues" daily and update task status directly from Slack. Marcel expects visible activity in Linear as a demonstration of operational rigor.

- **To GrowthX Operations:** The Smith.ai internal Slack channel integration is broken — Linear cards created for that project aren't pushing notifications to Slack. This needs immediate follow-up with Daniel (build team) to diagnose whether it's a configuration issue or channel permission problem. May affect the workflow for other client channels as well.

---

## Overview

- Linear serves as an efficient task management and reminder system, integrating with Slack for notifications
- Primary use: recurring client-related tasks (e.g., updates, reports) and one-off project tasks
- Customizable views and filters help manage tasks across multiple projects
- Some potential integration issues noted (e.g., Smith.ai channel, Airtable integration request)

---

## Key Topics

### Linear Basics and Navigation

  - Landing page shows all projects (clients, delivery team, build team)
  - Kanban-style board with customizable columns (backlog, to-do, in progress, done, canceled)
  - "My Issues" view aggregates tasks across all projects
  - Inbox shows cards/projects where user is tagged
  - Filtering options available to focus on specific clients or task types

### Task Creation and Management

  - Easy task creation using "+" button
  - Option to set tasks as recurring
  - Assign tasks to team members
  - Add context, comments, and tag others within tasks
  - Tasks automatically move between columns based on status updates

### Slack Integration

  - Linear tasks appear as notifications in relevant Slack channels
  - Team members can update task status directly from Slack
  - Some channels (e.g., Smith.ai) may have integration issues

### Use Cases and Best Practices

  - Vivek uses Linear for client comps, updates, and recurring tasks (e.g., Monday updates, Looker reports, meeting agendas)
  - Recommends checking "My Issues" daily to stay on top of tasks
  - Encourages team to use Linear in ways that best suit their workflow
  - Suggests maintaining some activity in Linear to demonstrate usage to management

### Communication Cadence

  - Monday: Weekly update sent (previous week recap, current week plan, outstanding issues)
  - Pre-meeting: Agenda sent with relevant charts
  - Post-meeting: Call notes distributed the following day

---

## Action Items

**Marisol Smith (GrowthX)**
- Ask Daniel about potential Linear-Airtable integration for task syncing

**Nemanja Simic (GrowthX)**
- Review Linear basics — open app, check My Issues, Inbox for relevant tasks/updates

**Uros Popic (GrowthX)**
- Review Linear basics — open app, check My Issues, Inbox for relevant tasks/updates

**Elvis Goren (GrowthX)**
- Ping Daniel re Linear integration with Smith AI internal Slack channel not working

---

## Transcript
**Vivek Shankar:** Sorry, I was on mute.

**Vivek Shankar:** Oh, no, no, you're good.

**Vivek Shankar:** Sorry, we're late.

**Elvis Goren:** I was just in a, we were just doing a pod sync, so.

**Elvis Goren:** No, no, no worries at all.

**Vivek Shankar:** What's on?

**Vivek Shankar:** How are you?

**Vivek Shankar:** Nice to meet you.

**Vivek Shankar:** Finally talked to you.

**Nemanja Simic:** Yeah, yeah, I know, right?

**Vivek Shankar:** I exchanged quite a few messages, but yeah, nice to see you.

**Nemanja Simic:** Before I joined GrowthX, I actually found Vivek randomly on LinkedIn and was reading his substack on marketing stuff, and then I messaged him about GrowthX, and then I got introduced to Tile from there. Well, long storied history. That's how the world works nowadays.

**Nemanja Simic:** Why so many  notetakers, man?

**Elvis Goren:** Who's?

**Elvis Goren:** Uh, why don't you do this?

**Vivek Shankar:** But I think it's everybody's, is on call, so, yeah.

**Vivek Shankar:** I've, like, canceled my wife.

**Nemanja Simic:** This is gonna, okay.

**Elvis Goren:** Can I, I'm gonna remove some of these.

**Elvis Goren:** I can't see.

**Elvis Goren:** Hey, Uros.

**Elvis Goren:** Hey, Marisol.

**Vivek Shankar:** How are you?

**Vivek Shankar:** Hi Vivek, nice to meet you.

**Uros Popic:** Hi, nice meeting you.

**Vivek Shankar:** Yeah, nice to meet

**Vivek Shankar:** Yeah, thanks for taking that time, man.

**Vivek Shankar:** I appreciate it.

**Vivek Shankar:** Yeah, sure.

**Vivek Shankar:** So what can I help you with?

**Vivek Shankar:** Because Mara didn't tell me much, but it was just like, I think you guys need to learn linear, but I think it's a pretty easy tool to use.

**Vivek Shankar:** So yeah, just curious to know.

**Vivek Shankar:** Yeah, I don't know.

**Vivek Shankar:** I don't know what we're supposed to be doing in there.

**Elvis Goren:** So we're doing like standups and stuff like just that recent message from our cell.

**Elvis Goren:** I'm just I don't know.

**Elvis Goren:** So we have to like put our tasks in there, like is it daily tasks or weekly?

**Elvis Goren:** Like I thought it was originally just for the dev team.

**Elvis Goren:** So I don't know.

**Elvis Goren:** I just don't like even from this just from scratch, like what the goal is, like who it's for.

**Elvis Goren:** And then just give us like a little walkthrough because I have no idea.

**Elvis Goren:** Like I wasn't even like we had Stuart, I think, one of the directors for like a week.

**Elvis Goren:** And I didn't get I didn't get a chance to he was supposed to teach us.

**Elvis Goren:** And then I just it just never happened.

**Vivek Shankar:** Yeah, yeah.

**Vivek Shankar:** OK.

**Vivek Shankar:** No worries.

**Vivek Shankar:** So the way I'm using it is pretty straightforward.

**Vivek Shankar:** I would say it's kind of up to you.

**Vivek Shankar:** When I say you, I mean each and every one of you, how you want to use it.

**Vivek Shankar:** Like the way we're using it is just to keep reminders on repetitive tasks.

**Vivek Shankar:** So for example, the things we're using it for is mostly client comps, right, and updates.

**Vivek Shankar:** So we send a Monday update.

**Vivek Shankar:** send the, there's a looker report creation and the agenda creation before the sync.

**Vivek Shankar:** And then there's post call notes.

**Vivek Shankar:** So those three things are basically set up as like they're recurring tasks.

**Vivek Shankar:** They need to be done every single week.

**Vivek Shankar:** And it's assigned to one person in the team.

**Vivek Shankar:** could be me, could be this, my, or me, or whoever, right?

**Vivek Shankar:** So there are tasks for that in linear, and then it just sends reminders in Slack.

**Vivek Shankar:** And you just move it.

**Vivek Shankar:** And it's just like a reminder to get, get those things done.

**Vivek Shankar:** That's it.

**Vivek Shankar:** There are some one-off tasks as well that I set up in there.

**Vivek Shankar:** For example, we

**Vivek Shankar:** We are scraping a lot of our clients' podcasts to get some extra stuff in to the articles and everything.

**Vivek Shankar:** So we're doing all of that.

**Vivek Shankar:** So there's a task for that too.

**Vivek Shankar:** And then I've been creating tasks and issues for the build team around the podcast and the podcast around the grid quality output and all that stuff.

**Vivek Shankar:** So I'm just following up on that.

**Vivek Shankar:** So let me share my screen to show you what all of that is like.

**Vivek Shankar:** So hopefully you can see this.

**Vivek Shankar:** Okay.

**Vivek Shankar:** So I am using Galileo here. Let me start from scratch. Generally there's a landing page and you'll most probably land on a page that looks like this, right? This shows three client projects — a delivery team, a build team, every single project that's out there.

**Vivek Shankar:** What I would do is you can filter for some of your things, right?

**Vivek Shankar:** So for now, I'll just pick Galileo, and then once I'm done with this, we can pick one of yours and kind of run through it.

**Vivek Shankar:** So pick on Galileo, and then once you open it, this is how the board looks. It's a pretty straightforward Kanban. There's backlog, to-do, progress, done — all these statuses up here.

**Vivek Shankar:** When you first come in, you'll probably see a lot of these tasks by default — gather context, deep dive, competitor research. I just deleted all of those and put them under canceled to clean up the thing.

**Vivek Shankar:** Okay, so this is the kind of thing I was talking about — post-meeting notes. I just created a recurring task.

**Vivek Shankar:** So this is basically Nika's job over here.

**Vivek Shankar:** And, you know, he just keeps updating the status every week.

**Vivek Shankar:** And it shows up in Slack as like a notification.

**Vivek Shankar:** So if I go to the internal canaleo panel, you can see like it gives these kind of little reminders over here.

**Vivek Shankar:** So like, you know, after meeting notes or whatever, this is assigned to Nika, and then he just changes it to like done or something like that, and it automatically does it.

**Vivek Shankar:** So as far as I know, Nika and Ismail don't actually come into linear at any point.

**Vivek Shankar:** They just handle everything in Slack.

**Vivek Shankar:** All I have to do is set up these kind of recurring tasks or repeated tasks, and then they just keep updating it within Slack, and it serves as a reminder for them.

**Vivek Shankar:** The example of the one-off task is this particular thing.

**Vivek Shankar:** And if you have questions, just let me know because I can't see you guys.

**Vivek Shankar:** So yeah.

**Vivek Shankar:** This is an example of a one-off task, which is the scraping internal Galileo resources.

**Vivek Shankar:** I just pasted all the context in here, and then it's just been going back and forth.

**Vivek Shankar:** But basically, this is a way to keep in touch what's going on with this, because this has been going on for quite a few weeks now.

**Vivek Shankar:** It's just a way to organize all the information in here.

**Vivek Shankar:** And then, for example, this last message, I just tagged Ismail in here within Linear, and in Slack, it just showed up as an update over here.

**Vivek Shankar:** I had a question for Kyle as well, and then I just updated it on Linear, and it showed up in Slack.

**Vivek Shankar:** Vivek, can you go back to your Linear?

**Elvis Goren:** Are you setting this up weekly tasks?

**Elvis Goren:** Or, like, what's the time frame of this?

**Elvis Goren:** Because, um...

**Elvis Goren:** Can I see how much you have in the purple that's on the side there?

**Vivek Shankar:** What is it?

**Elvis Goren:** The final column before canceled, done?

**Elvis Goren:** Yeah.

**Vivek Shankar:** Are you doing this on a weekly basis?

**Elvis Goren:** Because it can get, right?

**Vivek Shankar:** So what happens is the recurring tasks are automatically created weekly. Once Nika moves it to done, it just switches back to to-do for the following week. It doesn't keep increasing in size in the done column — it just keeps cycling over.

**Vivek Shankar:** Okay, cool.

**Elvis Goren:** Yeah, the chart makes sense. I guess I didn't really know who was using it for what. Do you use custom views? You can set a custom view for all your clients, right?

**Elvis Goren:** I don't use it for.

**Vivek Shankar:** All my clients, but Linear has this thing called My Issues over here.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** So when you go to My Issues, everything, this is something I check just by default at the start of each week.

**Vivek Shankar:** And this is something I told the guys to do as well.

**Vivek Shankar:** Not the start of each week, at the start of each day.

**Vivek Shankar:** Just check, like, you know, in case you miss the notification on Slack or you don't see it, just come in and check here.

**Vivek Shankar:** It will just give you the to-do, the backlog, whatever stuff.

**Vivek Shankar:** And then you can even filter this.

**Vivek Shankar:** So there's, like, a bunch of filters you can go through.

**Vivek Shankar:** If you don't, if you want to see, like, everything that you've done, you can just hit all under Completed Issues.

**Vivek Shankar:** It shows you, like, every single thing that you have done and moved into the done status or whatever.

**Vivek Shankar:** And this is across every single project that you are involved in.

**Vivek Shankar:** So I just put it on none because I just want to see the ones that are upcoming or that I have to do.

**Vivek Shankar:** If you go into Inbox, this will show you all the cards or the projects on which you're

**Vivek Shankar:** You have been tagged, right?

**Vivek Shankar:** So this is an example where this is a build project where, you know, I had just kind of tagged him like, okay, this is not working or whatever.

**Vivek Shankar:** I messaged Daniel.

**Vivek Shankar:** He created a card and then he just subscribed me to this card.

**Vivek Shankar:** Like he just added me to it or something.

**Vivek Shankar:** And then basically Kirk's been updating this and I just follow it from my inbox, right?

**Vivek Shankar:** I don't use views as such. I just come to My Issues to see the stuff that's relevant to me, and then I check inbox for updates.

**Elvis Goren:** I'm trying to do this by myself. So you're on all projects?

**Elvis Goren:** When I go to projects, I get an overview. But if I go to issues, I see this.

**Vivek Shankar:** I filtered this.

**Vivek Shankar:** I hit filter and typed in a client name. Go to Smith.ai, and then I click on this. You'll have to click issues and then you can do this.

**Elvis Goren:** Like when you click on yours, you get right to the chart. How do you do that?

**Vivek Shankar:** It's happening for Smith as well now. I just selected issues and left it there, and it comes here.

**Elvis Goren:** The way to create things is pretty easy.

**Vivek Shankar:** Pretty straightforward. You just hit the plus button.

**Vivek Shankar:** You fill in everything, and then if you click make recurring, that's it. It's a pretty straightforward tool to use.

**Vivek Shankar:** Hi, Vivek.

**Marisol Smith:** Can we have an integration with Airtable? So whenever a task in Airtable is assigned to me, I want it on Linear.

**Vivek Shankar:** I don't know about that. You have to ask Daniel or somebody from the build team. The only integration I know about is between Slack and Linear.

**Elvis Goren:** So they all integrate with the internal client channels, each one?

**Vivek Shankar:** Yes. You'll get notifications the minute you start. Let me show you.

**Vivek Shankar:** You should see a notification pop up in the SmithAI channel.

**Vivek Shankar:** Yeah.

**Elvis Goren:** Cool.

**Elvis Goren:** I'll probably see in a bit.

**Elvis Goren:** All right.

**Elvis Goren:** I mean, it makes sense to me.

**Elvis Goren:** Anyone else, guys?

**Elvis Goren:** No, that makes sense.

**Nemanja Simic:** When Marcel talked about daily stand-ups, are these through Linear as well? Or through GeekBot for our pods?

**Vivek Shankar:** I don't think he was referring to Linear. I think he was referring to Slack communications — the General channel, the Delivery General channel.

**Vivek Shankar:** Oh, Delivery.

**Vivek Shankar:** Where is...

**Vivek Shankar:** Down a little bit, right above the DataGrid one, yeah.

**Nemanja Simic:** Yeah, there we go.

**Nemanja Simic:** Yeah, so, yeah, he's talking about clients and everything, and then every Monday...

**Nemanja Simic:** Third point, stand-ups are not optional.

**Nemanja Simic:** If we were your manager, ask someone multiple times to update stand-ups, we're linear, and it keeps not getting done.

**Vivek Shankar:** Yeah, I think this, he just meant the GeekBot.

**Vivek Shankar:** and linear thing is more about tasks related to the client itself.

**Vivek Shankar:** I don't think he's...

**Vivek Shankar:** I think what he's just trying to say is, like, we need to use linear on some extent, but I don't think this is for client comms as such.

**Vivek Shankar:** It's more for, like, internal, and it's more like, I know he takes a look at these internal client channels and the external channels quite a bit.

**Vivek Shankar:** So I think he just wants to see, like, updates going on, right?

**Vivek Shankar:** Like, can show you an example of, like, I'll show you Galileo, because...

**Vivek Shankar:** I remember he sort of, he highlighted this on a client call as well.

**Vivek Shankar:** Sorry, this is the internal channel.

**Vivek Shankar:** I'll show you the external one.

**Vivek Shankar:** Basically, it's like, so this is kind of the cadence on which we communicate.

**Vivek Shankar:** So every Monday, like Geekha sends this thing out, which is like, here's what we did last week.

**Vivek Shankar:** This is what we're doing this week.

**Vivek Shankar:** These are some outstanding issues that we've given or whatever based on the conversations.

**Vivek Shankar:** So we send this and then, you know, I keep chiming in with like questions or whatever.

**Vivek Shankar:** And then before the meeting, I send out the agenda.

**Vivek Shankar:** And then I put like the chart in there because it's like easy for them to view.

**Vivek Shankar:** And then after that, there's like a post called Notes, which goes out the next day.

**Vivek Shankar:** So Nika sent this.

**Vivek Shankar:** I think this is what Marcel is really referring to when he just comes up.

**Vivek Shankar:** And then he just wants to see this kind of thing going.

**Vivek Shankar:** Regularly.

**Vivek Shankar:** yeah.

**Vivek Shankar:** The linear thing is more like an internal sort of, what do you call it?

**Vivek Shankar:** Just like a sanity check.

**Vivek Shankar:** Manager, yeah.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Okay, that makes sense.

**Nemanja Simic:** Yeah, I was confused about how Linear and daily stand-ups connect. I opened Linear once.

**Vivek Shankar:** The main thing — can I stop sharing Linear, or is there anything else you want to look at?

**Vivek Shankar:** It feels a bit disembodied talking to a blank screen.

**Vivek Shankar:** I think when I presented Linear to the guys, I was like, use it for whatever utility you find in it. Marisol wants Airtable tasks coming in directly — if that makes sense, go ahead. I find it useful from a manager's perspective. We have five accounts with multiple things going on, and it's nice to have automated reminders instead of manually pinging everybody. Use it however you find useful. If you're asking how to keep Marcel happy, as long as you have a few cards in there, he'll know you're using it. Beyond that, do your thing.

**Marisol Smith:** The internal Smith AI channel isn't connected to Linear — the comment never made it to Slack. Do we have to do anything?

**Vivek Shankar:** No, you don't have to do anything. I'll ping Daniel to see why that's happening. Let me test by creating a test card and assigning it to Elvis.

**Vivek Shankar:** I just created a test issue. Let me know if that shows up.

**Elvis Goren:** Yeah, I just created one too.

**Vivek Shankar:** That's weird. Just ask Daniel about this — it isn't happening like it should.

**Elvis Goren:** It shows connected, but anyway, if no one has questions, Vivek, thanks a lot.

**Vivek Shankar:** Thanks. If you have any questions, let me know.

**Elvis Goren:** Thank you so much, Vivek.

**Uros Popic:** Nice meeting you.

**Vivek Shankar:** Thank you. Bye.
