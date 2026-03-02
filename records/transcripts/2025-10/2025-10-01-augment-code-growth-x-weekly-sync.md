# Augment Code <> Growth X - Weekly Sync

<metadata>
date: 2025-10-01
time: 16:31 UTC
duration: 20 minutes
organizer: Jason Gong
participants: Jason Gong, Nathalie Schrans, Edin Abazi, Sylvain Giuliani, Molisha Shah
fathom_recording_id: 91167141
fathom_url: https://fathom.video/calls/427050152
share_url: https://fathom.video/share/m5NHDdXtS_FMqtqDrTQVt2c1uUQ_5L9B
source: fathom
enriched_on: 2026-03-02 14:30 UTC
</metadata>

---

## Summary

GrowthX and Augment Code aligned on Auggie CLI development progress: the frontend is mostly complete with Sanity CMS managing commands, categories, tags, and FAQ sections. The team decided to postpone the download count feature for V1 and will return markdown files from the endpoint to be stored locally by the CLI tool. Edin will start a Slack thread with Chris to confirm technical implementation details, and the internal testing launch is pushed to the following week with public release potentially the week after, with AJ as the first user.

---

## Context

Augment Code is an external client building Auggie, an AI coding assistant CLI tool. GrowthX is delivering growth marketing services to Augment Code, focusing on content strategy and visibility. This weekly sync brings together Jason Gong (GrowthX founder leading the client relationship), Edin Abazi (GrowthX lead on development and design), and Sylvain Giuliani (Augment Code's co-founder). The meeting addresses both the content strategy evolution for Augment Code's visibility and the technical implementation details of the Auggie CLI feature, which is a core product milestone.

---

## Relevance

**To GrowthX Delivery:**
- Confirmed CMS strategy using Sanity for command management and SEO optimization with per-command FAQ sections, expanding GrowthX's technical advisory scope beyond content strategy
- Identified scope reduction decision: postponing download count feature for V1 demonstrates discipline in prioritization and feature gating, a lesson applicable to other product-focused clients
- Technical implementation pattern (endpoint returning markdown, CLI storing locally) aligns with modern development practices that GrowthX should track for future SEO/content positioning

**To GrowthX Business Development:**
- Augment Code pushing launch timeline (internal testing next week, public release following week) reflects strong internal velocity and confidence, suggesting account expansion potential in product marketing services
- Sylvain requesting detailed content analytics and performance clustering analysis ("top-performing content clusters") indicates readiness for deeper strategic engagement and potential retainer expansion
- Strategy discussion scheduled for next Wednesday at GrowthX office signals high-touch engagement and relationship depth

---

## Overview

- Content strategy is evolving; team to share coherent plan for next few weeks
- Auggie CLI development is progressing; frontend mostly ready, backend details to be finalized
- Launch timeline for Auggie CLI adjusted to next week for internal testing, public release week after
- In-depth strategy discussion scheduled for next Wednesday at GrowthX office

---

## Key Topics

### Content Strategy and Performance

  - Team close to finalizing coherent content strategy for coming weeks
  - Direct traffic anomaly detected, likely bot activity; filtered out without impacting signup numbers
  - Growth trends positive; ChatGPT remains challenging to crack compared to Perplexity and Gemini
  - Sylvain requested analysis of top-performing content clusters for potential doubling down

### Auggie CLI Development

  - Frontend mostly complete, awaiting integration of download count feature
  - Sanity CMS used for managing commands, categories, and tags
  - FAQ section added per command for SEO benefits
  - Hosting and data management decisions:
      - Markdown files to be returned by endpoint, stored locally by CLI tool
      - Download count feature postponed for V1 launch
      - Chris to confirm technical implementation details

### Launch Timeline and Content

  - Launch delayed by a week; internal testing next week, potential public share week after
  - AJ to be first user for testing and feedback
  - Sylvain to have dev rel review and expand command list in shared spreadsheet

### Analytics Dashboard

  - Development of automated stats dashboard delayed due to resource constraints
  - Screenshots to be used temporarily until automation is complete

---

## Action Items

**Edin Abazi (GrowthX)**
- Start Slack thread with Chris re: Auggie CLI tech details (markdown file return, input handling, endpoint behavior)

**Sylvain Giuliani (Augment Code)**
- Ask dev rel to review command list in spreadsheet/JSON, add new commands as follow-up
- Create and send doc with target metrics (internal traffic, etc.) before next Wednesday meeting at GrowthX office

---

## Transcript
**Jason Gong:** This meeting is being recorded.

**Jason Gong:** Okay.

**Jason Gong:** Just waiting for Syl.

**Nathalie Schrans:** Hey everyone.

**Edin Abazi:** Hello.

**Jason Gong:** Hey Natalie.

**Nathalie Schrans:** How's everyone's day going?

**Jason Gong:** Good.

**Sylvain Giuliani:** What's up gang?

**Jason Gong:** Oh, how goes.

**Sylvain Giuliani:** Good, good.

**Sylvain Giuliani:** Good. Give me two seconds.

**Jason Gong:** Just need to send this.

**Sylvain Giuliani:** Okay, cool. Sorry, just want to send this before I forget. Awesome.

**Jason Gong:** Let's do it.

**Sylvain Giuliani:** Let's do it.

**Jason Gong:** So, we'll do a quick update, then I brought Ed, who leads all kind of our dev and design, so we can show you the Auggie CLI stuff.

**Sylvain Giuliani:** Excited.

**Jason Gong:** Cool.

**Jason Gong:** So, I'll just get started.

**Jason Gong:** Okay, so we're still publishing a bunch.

**Jason Gong:** I think the main kind of high level on the content side is kind of pretty close to coming up with an actual coherent strategy.

**Jason Gong:** with what we're going to do for the next couple weeks.

**Jason Gong:** We'll share that soon, and we're going to move things into this kind of different strategy.

**Jason Gong:** And then, yeah, I said the thing in the Slack thread, but there was all that direct traffic, which now kind of almost looks like a crawl or something like that.

**Jason Gong:** So I basically filtered that out, but basically I saw that.

**Sylvain Giuliani:** Yeah, I saw your message, haven't investigated that.

**Sylvain Giuliani:** I mean, this is kind of like the bane of my existence right now.

**Sylvain Giuliani:** It's like, there's so much like bot traffic in general that is like, you know, I mean, one of the, like, one of the things I was thinking is like, is this just like, then you count like LLM bots?

**Jason Gong:** Like, I mean, I know OpenAI, everyone is like, kind of like a good citizen, right?

**Sylvain Giuliani:** But I'm like, is there like another type of tool, like, you know, like Manus or something?

**Sylvain Giuliani:** That, you know, that is, like, basically hitting us through just the sheer amount of requests, right, to, to, to, I think you probably will.

**Jason Gong:** I mean, we have, like, what comment now, I've been playing around with that, and it's, like, yeah, if I just ran that and asked it to look at all your MCP servers, like, you would see that.

**Sylvain Giuliani:** Yeah, so, like, that's, like, kind of, a bad, I don't know if you guys see that with other customers, but, like, I mean, there's so much, like, automated traffic on our website nowadays, that is, like, hard to tell.

**Sylvain Giuliani:** You know, it's hard to tell what's the real number.

**Sylvain Giuliani:** We see that because of the fraud and all that stuff, right, too, but, like, it's just kind of, insane, yeah.

**Jason Gong:** I guess I'll let you know, but yeah, traffic is kind of noisy now.

**Jason Gong:** I will say after you remove that, it doesn't seem like there's any other case of that happening, and it didn't really change any of the signup numbers, so whatever that bot was, at least it wasn't downloading things. We'll just remove that from the data. Things are still growing.

**Jason Gong:** I think a big unlock from our side will be some of the work we're doing around structure and then some of the work Natalie's doing around just, like, cleaning up things we've already published.

**Jason Gong:** Like, one example for the SEO side, everything's moving in the right direction.

**Jason Gong:** I want to say, like, ChatGPT has still, like, been kind of hard to crack.

**Jason Gong:** If you dig into a lot of these, it's a lot of, like, perplexity and Gemini at the moment.

**Jason Gong:** That's where you're getting more awareness in the prompt.

**Jason Gong:** Nothing's like Silverbolt, like, for example, ChatGPT likes coding tool versus coding assistant.

**Jason Gong:** And ChatGPT just appends in 2025.

**Jason Gong:** Like, every article it cites has this in the title.

**Jason Gong:** So we're just kind of cleaning up things we're publishing to optimize for that, basically.

**Jason Gong:** And then once we have some more details and resources, we're going to experiment with something like this for our other clients.

**Sylvain Giuliani:** Yeah.

**Sylvain Giuliani:** One thing I was looking at, kind of looking back to our conversation from last week, is that I haven't had the time, but because we're also doing a big content strategy internally, I was wondering: what are the top performing pieces or clusters of content in terms of SEO and conversion?

**Sylvain Giuliani:** I know we're talking about a couple hundred signups, so I'm not going to over-index on this, but I was wondering if there's anything interesting we can double down on. Maybe pick some of that content and put it on the main website, or invest in things like interview series.

**Sylvain Giuliani:** Like, I'll give you the specific examples.

**Sylvain Giuliani:** Like, I know we've writing content about spec-driven development, right?

**Sylvain Giuliani:** And internally, we're thinking, should we build a feature for that?

**Sylvain Giuliani:** Do we want to do, you know, kind of like interview series about how to do spec-driven development, right?

**Sylvain Giuliani:** We do have content on spec-driven development that's about three weeks old. Is it picking up with our team? Again, I'm not saying we should over-index on this, but that's where the question comes from. I think at a piece of content or topic level, analytics or reporting would be really helpful.

**Jason Gong:** Does that make sense?

**Jason Gong:** Yeah, that makes sense.

**Jason Gong:** I mean, I think, yeah, seeing what works helps.

**Jason Gong:** And then there's things that you can do to, like, optimize for that.

**Jason Gong:** Like, for example, like, kudos, you know, we know them now because they're in a lot of the searches we want to do.

**Jason Gong:** And, like, they know the content that works for them, which is why, they like, pull it.

**Jason Gong:** You know, even though it's, like, in the blog, they have it here, for example.

**Jason Gong:** Okay.

**Sylvain Giuliani:** So we'll have some suggestions there. Sounds good.

**Jason Gong:** Let's see.

**Jason Gong:** And then on Auggie CLI, I think I want to spend most of the time there.

**Jason Gong:** Maybe, I mean, I brought Ed in just to, like, walk you through just how that's all set up.

**Jason Gong:** So it's basically all set up now.

**Jason Gong:** There's some, like, open questions still of, like, when somebody types that command into the terminal, like, where is it going to grab that info?

**Jason Gong:** I think we talked about Sandy, but Ed had a different suggestion.

**Jason Gong:** Maybe we can do that very quickly.

**Jason Gong:** I've been building kind of the workflows in the background, and if you tell me those are more or less in line, we can do the rest. I think there are some questions around the arguments. Looking at the Cloud Code ones, they have arguments. So you have space to add a parameter or something like that, and I wasn't totally sure how that works here.

**Jason Gong:** Just replace, our equivalent, we called it input.

**Sylvain Giuliani:** Yep, yep, yep.

**Sylvain Giuliani:** I think that's, that's, yeah.

**Sylvain Giuliani:** Yeah, I I wish I could, like, bring Chris, but, like, he's in another meeting right now.

**Sylvain Giuliani:** But, yeah, I think that's, like, that's, that's fine.

**Sylvain Giuliani:** We can move async. I'll message Chris. He's the one implementing how we input arguments into the command. Makes sense. I don't have the latest spec in front of me, but that sounds good.

**Jason Gong:** But the site is basically built.

**Jason Gong:** It's not merged yet, but we'll create a...

**Edin Abazi:** I share my screen and, like, walk through it?

**Sylvain Giuliani:** Yeah, yeah, go for it.

**Edin Abazi:** One second.

**Edin Abazi:** I'm sorry about the background noise. My son's crying.

**Edin Abazi:** So the front end is basically ready minus the number of downloads, which will come once we decide on how we're going to host all these.

**Edin Abazi:** So everything, like the title and the rest, are hardcoded into the site just like the rest of the website was, but the collections themselves, the items are all from Sanity.

**Edin Abazi:** So we do have three types of content, which is, like, the commands themselves, and we have categories and then tags.

**Edin Abazi:** But then, like, this entire, like, command item, we do have, like, the submitter, which does the description, excerpt, and then we do have, like, some basic logic of, like, getting some related commands from the same category.

**Edin Abazi:** We can, like, enhance this, like, let it down the line.

**Edin Abazi:** In terms of Sanity, right now I don't have a local version because I haven't merged into the main branch yet. There's just a new folder with command-related files and the commands themselves.

**Edin Abazi:** We have the title, which we agreed would be lowercase with dashes in the middle. There's the excerpt, which if you toggle on goes to the top of the popular section on the homepage. Then there are tags, FAQ, and the submitter field.

**Edin Abazi:** I initially thought we would use a global FAQ, but that wouldn't make sense SEO-wise, so we need specific FAQs for each item.

**Sylvain Giuliani:** What do you mean here?

**Edin Abazi:** Oh, I meant FAQ, sorry. Each command needs its own FAQ.

**Jason Gong:** We're thinking about just adding SEO stuff in there. So for the debugger workflow, the FAQ would be like "What is the best way to debug?" or "How does an agent debug code?" — things that people search for that might pull that content.

**Sylvain Giuliani:** Okay, but this is just like, like you said, like just SEO benefit that we can fill in and then that just kind of like, yeah, go, go, that makes sense.

**Edin Abazi:** Yeah.

**Sylvain Giuliani:** Okay, cool.

**Edin Abazi:** Thank you.

**Edin Abazi:** So for hosting the commands themselves, it can technically be done through Sanity if it's just markdown being pulled.

**Edin Abazi:** I was thinking about the, I don't know, timeline-wise how we're thinking about doing the like third-party submissions and then like that entire process of like people submitting and then like the team approving or like denying different submissions, it can be done through Sanity.

**Sylvain Giuliani:** Technically, technically like we can even use those as a database as well, like if it's approved.

**Edin Abazi:** It automatically goes to, like, the actual database of the commands.

**Edin Abazi:** In terms of account downloads, that can be done as well.

**Edin Abazi:** We can just do, like, a read-only field that would, like, change based on, like, when somebody hits the endpoint.

**Edin Abazi:** I don't know how scalable it would be through Sanity, because technically it's not a traditional database.

**Edin Abazi:** It all depends on how big this might end up going.

**Edin Abazi:** either way, like, even, I think it's fine, because, like, later on, later down the line, like, it can be easily switched to, like, an actual database.

**Sylvain Giuliani:** Yeah, so I think, like, a couple of things, yeah, just to kind of, like, you know, reduce the scope so we can ship at least a V1.

**Sylvain Giuliani:** I think let's forget about download count for now.

**Sylvain Giuliani:** Let's not try to understand what it is right now, and those numbers are going to be zero at the beginning anyway.

**Sylvain Giuliani:** So we can figure that out later on.

**Sylvain Giuliani:** I think that that's kind of like completely fine.

**Sylvain Giuliani:** From the implementation point of view, let's loop Chris in.

**Sylvain Giuliani:** What he told me last time is that Sanity should just return a plain markdown file from the endpoint.

**Sylvain Giuliani:** And then the CLI, the way we're going to implement it, will take that markdown file and store it locally in the command folders.

**Sylvain Giuliani:** And then the CLI tool will be able to handle that itself. I think that's right, but let's get a quick Slack thread to confirm. Chris is essentially implementing this week and next week, so he should be on top of it pretty quickly.

**Sylvain Giuliani:** So let's take those two decisions now. Return a markdown file, and let's confirm that with Chris. I'm pretty sure that's what he wants to do, not a full JSON file, just hit the endpoint, return markdown file, and handle the rest on the client.

**Edin Abazi:** Okay.

**Edin Abazi:** I guess, like, it's worth having another chat with him just to, like, lay down all the technical stuff.

**Jason Gong:** Yeah, I think that's fine.

**Sylvain Giuliani:** And if we have to generate a quick call to just kind of, like, hash it out in, like, 15 minutes or something, I think that's also fine completely.

**Sylvain Giuliani:** Okay.

**Sylvain Giuliani:** Yeah, I mean, that's kind of the latest I heard from him.

**Sylvain Giuliani:** But, I mean, I had a chat with him yesterday, and I was like, hey, are you close to implementing, like, the import comment feature stuff, right?

**Sylvain Giuliani:** And he's like, oh, I'm actually going to start working this.

**Sylvain Giuliani:** And then on this one, same thing, right, like, the, well, not this one, but, like, the input stuff, same thing.

**Sylvain Giuliani:** Let's have a quick thread on how we want to handle the input implementation.

**Sylvain Giuliani:** And then just to close up on CLI, the spreadsheet JSON is still the latest place to get all the commands that's going to be uploaded right now.

**Jason Gong:** I think Natalie sent you one here.

**Jason Gong:** Yeah, see one thing that's missing is maybe, like, the reference from, like, the other sites, but basically, like, all of these are cool.

**Sylvain Giuliani:** Yeah, so what I'm going to do is ask one of our dev rel to review this quickly and then probably add a bunch of new ones.

**Jason Gong:** So, like, if I ask him to add more stuff there, that's still, like, the source of truth that you're going to import inside the team, right?

**Jason Gong:** And we're just going release the list.

**Jason Gong:** I haven't checked if all of these can be generated the way we built it, but just work down the list and make sure we have everything. When are you launching?

**Sylvain Giuliani:** I mean, if it's...

**Sylvain Giuliani:** No, I think the, I mean, there's no hard, I mean, basically the goal is to launch next week, but like there's tons of things that I took priorities from launch recently.

**Sylvain Giuliani:** And so we're probably going to delay it by another week, just to be transparent.

**Sylvain Giuliani:** So there's not a hard date when we want to launch. I want to launch with clean commands and good examples. AJ was supposed to record videos for launch but got pulled into another project.

**Sylvain Giuliani:** I would say let's get the website running end to end next week, and then we can start polishing. AJ will be the first user. Let's use that timeline: next week AJ can test it, the week after we can potentially launch publicly.

**Jason Gong:** Okay, so pretty clear on that one.

**Jason Gong:** We're still building the analytics dashboard. The person supposed to build it got pulled into other stuff, so we'll use screenshots for now until we automate these stats. But as soon as Edin is done with Auggie CLI, we can shift over to that.

**Jason Gong:** And yeah, that's basically it.

**Jason Gong:** I know you wanted a session to kind of share a little bit more about a lot of the longer-term things you're thinking about, so I think we can still try to schedule that sometime whenever you're free basically.

**Sylvain Giuliani:** Yeah, I think we still have the slot for next week, right?

**Jason Gong:** I actually had it on my calendar for this week, but it was next week.

**Sylvain Giuliani:** Yeah, I was actually going to ask you about that. So let's...

**Jason Gong:** What about next week? Yeah, Wednesday is pretty open all afternoon, and Thursday is also pretty open.

**Sylvain Giuliani:** Yeah, let's do next Wednesday. I can come around lunch and stay at your office. I have one interview in the middle, but I can come to your office Jason and we can spend an hour and a half. I'll send a calendar invite to block it.

**Sylvain Giuliani:** Yeah, sounds good.

**Jason Gong:** There you go.

**Jason Gong:** Unblock my calendar.

**Jason Gong:** Yeah, the main thing is just shipping the product and then we can refocus.

**Sylvain Giuliani:** A lot of strategy things for next week.

**Sylvain Giuliani:** Okay, sounds good.

**Sylvain Giuliani:** And then hopefully by then I'll send you a document async about what metrics we're targeting going forward, like internal traffic and things like that. You can have a mini pre-read before the meeting.

**Jason Gong:** That's good.

**Jason Gong:** Cool.

**Jason Gong:** All right.

**Sylvain Giuliani:** We'll see you in the next one. Thanks, man. Talk soon.

**Jason Gong:** I appreciate it. Sounds good.

**Sylvain Giuliani:** Bye.
