# EPD All-Hands

<metadata>
date: 2025-07-16
time: 16:59 UTC
duration: 71 minutes
organizer: Daniel Lopes
participants: Ben Church, Brad Herman, Bridget McGillivray, Clint Shryock, Daniel Lopes, Felipe Lima, George Haikal, Georgemaine Lourens, Gianpiero Puleo, Jason Gong, Kirkland Gee, Kyle Gaudreau, Marcel Santilli, Marcus Derencius, Matthew Panzarino, Nicolas Castellanos, Pedro Steimbruch, Renato Silva, Stéfano Zanata, Tucker Barker, Katia Pembayun
fathom_recording_id: 74571073
fathom_url: https://fathom.video/calls/353115449
share_url: https://fathom.video/share/gNmLExhHfxacX6GNHwC4JSQZfn8ao_Ju
source: fathom
enriched_on: 2026-03-03 14:25 UTC
</metadata>

---

## Summary

GrowthX's first all-hands meeting for the Engineering, Product, and Design (EPD) team, with 21 engineers, designers, and product staff fully assembled as a team. Daniel Lopes presented the company's year-one thesis: validating "services as software" by proving one well-equipped person can perform as a team through AI and automation. The meeting centered on team structure (staying flat at ~15 people with no traditional managers), new engineering frameworks (Webflow publishing automation, programmatic SEO templates, TipTap AI-assisted editing, and image generation workflows), and alignment on how these tools enable delivering content and product work at scale for clients.

---

## Context

GrowthX's first year mission is to prove that services (content marketing agency work) can be productized through software and AI. The company recently closed funding and has now fully assembled its Engineering, Product, and Design team—12 product engineers, 4 designers, and support staff. Daniel Lopes, who leads the team, is operating with radical autonomy, holding weekly 1:1s with every product engineer (no managers or traditional product managers) and running planning through continuous feedback. The team sits across three functional areas (Strategy, Production, and AI Engineering) and rotates through Client Ops to stay grounded in real agency workflows and user problems. This all-hands was the first time the fully staffed team met together, marking a milestone in the company's buildout.

---

## Relevance

**To GrowthX Delivery:**
- New Webflow publishing automation (Ben Church) dramatically reduces the manual work mapping Webflow enums and collection fields, enabling faster project delivery for clients using Webflow.
- Programmatic SEO framework with templated article generation (Kirkland Gee) allows spinning up PSEO campaigns in 5 minutes instead of days—ready for use with clients like SIT (Slack alternatives, tool comparisons).
- TipTap AI-assisted editing (Brad Herman) with text selection AI, full document edits, and custom prompts is improving production team velocity, though reliability needs tuning before demo to clients.
- Image generation workflows (Daniel Lopes, Gianpiero Puleo) handling both HTML-to-image and GPT-based creation give delivery teams new capabilities for marketing asset production.
- Client Ops rotation ensures all engineers stay connected to real client pain points and helps teams spot blockers early.

**To CheckThat:**
- Programmatic SEO frameworks demonstrate how templated, data-driven content creation can scale; this informs CheckThat's potential role in content strategy and AI visibility workflows.
- AI-assisted editing and image generation workflows are proof points for AI augmenting human work, relevant to CheckThat's positioning in the AEO space.

**To GrowthX Business Development:**
- This is the first milestone showing the team is fully assembled and building production capabilities—strong signal for case studies and investor updates.
- New automation tools (Webflow, PSEO templates, TipTap) are differentiators for new business pitches and client expansion within existing accounts.
- Team structure (flat, autonomous engineers) and continuous innovation demonstrate operational efficiency and pace that can be marketed to prospects evaluating GrowthX versus traditional agencies.

---

## Overview

- GrowthX's year one goal: Validate the "services as software" concept by March 2024, focusing on enabling one person to perform as a team
- Team structure: Staying flat with \~15 people, no traditional product managers or engineering managers for now
- Key focus areas: Strategy, Production, and AI Engineering functions to scale the agency and serve target clients
- Recent demos showcase advancements in Webflow publishing, programmatic SEO, AI-assisted editing, and image generation

---

## Key Topics

### Team Structure and Focus

  - First fully assembled EPD team with all critical lanes staffed (though spread thin)
  - Aiming for \~15 people total, adding a couple more in ML/AI
  - Staying flat organizationally for at least the first year
  - No traditional product managers; engineers have autonomy on feature decisions
  - Daniel holding weekly 1:1s with all 12 product team members for alignment

### Year One Goals and Strategy

  - Validate "services as software" concept by March 2024 (1 year from fundraising)
  - Enable one well-equipped person to perform as a team
  - Focus on serving specific client types (Ideal Customer Profile - ICP)
  - Three key functions: Strategy, Production, and AI Engineering
  - Building tools for content marketers/creators to match programmer productivity gains

### Client Ops Engineering Team

  - Acts as first line of defense for understanding agency needs
  - Rotates responsibility for triaging tickets, answering Slack support, and being strategy sprint consultant
  - Conducts R\&D (e.g., testing agent-based refreshing)
  - Other team members encouraged to spend time with Client Ops for context

### Webflow Publishing Workflow (Ben)

  - New declarative approach to handle Webflow's complex collection structures and enums
  - Generator tool creates config files and types, reducing manual work
  - Potential for public release to gain community goodwill (Webflow CPO is an angel investor)

### Programmatic SEO Framework (Kirkland)

  - Utilizes existing researcher workflows with templated questions
  - Article draft workflow uses markdown templates stored as Atlas artifacts
  - Enables quick setup of programmatic SEO campaigns (5 minutes for non-complex cases)
  - Multiple pipelines already using this approach

### AI-Assisted Editing (Brad)

  - TipTap-based WYSIWYG editor with custom AI integrations
  - Features include text selection AI actions, full document edits, and artifact context inclusion
  - Upcoming AI assistant feature in development
  - Need to improve prompting and consider UI placement (popover vs. sidebar)

### Image Generation Workflows (Daniel/GP)

  - Two main workflows: HTML template to image conversion and GPT-based image creation
  - GPT Images workflow generates ideas and creates images based on article content and art direction
  - HTML templating engine creates flexible, variable-based templates for marketing materials
  - New artifact type in Atlas for HTML templates with preview functionality

---

## Action Items

**Brad Herman (GrowthX)**
- Discuss with Kirkland Gee on improving prompts for TipTap AI assistant
- Demo TipTap AI features to delivery team once AI assistant and improved prompts are ready

**Kirkland Gee (GrowthX)**
- Discuss with Brad Herman on improving prompts for TipTap AI assistant

**Daniel Lopes (GrowthX)**
- Schedule breakout room/shaping discussion next week regarding AI editing features

---

## Transcript
**Daniel Lopes:** This meeting is being recorded.

**Daniel Lopes:** Always in the office.

**Daniel Lopes:** Do you ever work for him?

**George Haikal:** I do.

**Daniel Lopes:** never seen you work for him.

**George Haikal:** Yeah, sometimes.

**Daniel Lopes:** A few times.

**George Haikal:** But calls here, I like better.

**George Haikal:** Especially when there's no one in the office.

**George Haikal:** It's really good.

**George Haikal:** But I'll leave after my calls and go home and finish up the actual work.

**Daniel Lopes:** Before we start showing you, guys.

**Daniel Lopes:** Hello, hello.

**Daniel Lopes:** Tucker, nice to see you.

**Daniel Lopes:** It's been a while since we haven't had a mad ability.

**Tucker Barker:** Yeah, it's good to see everybody here.

**Daniel Lopes:** Tucker's been silently building our team with a lot of much guidance for me.

**Daniel Lopes:** This shows, like, a bunch of great people show up in the pipeline.

**Daniel Lopes:** Yep, sounds good.

**Daniel Lopes:** All right, one, one try.

**Tucker Barker:** The best.

**Daniel Lopes:** We'll miss you here next week, Tucker.

**Daniel Lopes:** Next one you should tag along.

**Tucker Barker:** I'll definitely make the next one.

**Tucker Barker:** The summer's been busy, for sure.

**Daniel Lopes:** Your Coinbase shirt is lasting.

**Tucker Barker:** I'm going get some more growthx shirts.

**Daniel Lopes:** I have like four.

**Daniel Lopes:** All right.

**Ben Church:** I still feel like definitely the new guy is the swag, you know, leg, right?

**Ben Church:** I'm looking around, I guess I'm like, everybody alone grows, and I'm like, man, I need some growthx on me now.

**Ben Church:** need like a backlog.

**Kyle Gaudreau:** Dude, I didn't have swag until like maybe like a week or so ago, so I feel you.

**Kyle Gaudreau:** And I've been here many months now.

**Kyle Gaudreau:** We got to be better on the swag train.

**Kyle Gaudreau:** We're getting there.

**Kyle Gaudreau:** We got shirts now.

**Kirkland Gee:** We got two different types of hats.

**Kirkland Gee:** Do you like a good hat?

**Kirkland Gee:** I need a growth-type hat.

**Kyle Gaudreau:** We'll have to send some out.

**Kyle Gaudreau:** What do you got there, Ben?

**George Haikal:** What was that?

**George Haikal:** All for you, Kirkland.

**Kyle Gaudreau:** Oh, I love it.

**Ben Church:** This is the one that can't leave my office, but I like, so it's not my production hat.

**Ben Church:** Like, if I'm doing anything in production where I might nuke the database, this goes on the head.

**Daniel Lopes:** Okay, that's five minutes for everybody to enjoy.

**Daniel Lopes:** Oh, eat more.

**Daniel Lopes:** I think just bread.

**Daniel Lopes:** GP is probably not joining.

**Daniel Lopes:** Wait a little bit.

**Daniel Lopes:** Yeah, 10.AI notekers, it's wild.

**Daniel Lopes:** It's kind of crazy that zone doesn't solve this.

**Daniel Lopes:** It's just, that sounds like, it should be like a bomb project, you know, like, not like a three-year thing.

**Kirkland Gee:** It's never been prioritized, that's all.

**Kirkland Gee:** know, they've been probably on a backlog somewhere that they've looked at every single sprint planning for two years and been like, ah, we'll get to it.

**Daniel Lopes:** Yeah.

**Ben Church:** At this point, I always wonder if Zoom has engineers.

**Ben Church:** This probably hasn't changed, like, since 2020.

**Ben Church:** everyone.

**Ben Church:** Thank you Thank Thank Thank

**Daniel Lopes:** Oh, nice.

**Daniel Lopes:** Oh, it's funny.

**Daniel Lopes:** Oh, he's already here.

**Daniel Lopes:** Oh, yeah, Stephen has two emails, I guess.

**Daniel Lopes:** But we can start with .

**Daniel Lopes:** And then he can watch the recording.

**Daniel Lopes:** Let's see.

**Daniel Lopes:** Cool.

**Daniel Lopes:** All right, everyone.

**Daniel Lopes:** Thanks for being here.

**Daniel Lopes:** Let me just, like, get the deck ready here.

**Daniel Lopes:** Our first all-hands engineering product and design team.

**Daniel Lopes:** I feel like that's the first time they actually have, like, that I consider the team, like, fully assembled, where we have all the different lanes that we think are important or staffed just, you know, like, everybody spreads super thin still.

**Daniel Lopes:** It's going to be, like, like, four people in one area, four people in another area.

**Daniel Lopes:** And four people in another area, then we're going to swap here and there.

**Daniel Lopes:** But four is a good number.

**Daniel Lopes:** You get the Beatles with four, not with eight people.

**Daniel Lopes:** So same thing for the usual pizza rule.

**Daniel Lopes:** So I think that's a good starting point for all the lanes.

**Daniel Lopes:** Add count-wise, I think we're going to shoot for probably something.

**Daniel Lopes:** Maybe we're going to add a couple of more people.

**Daniel Lopes:** Another thing that we did recently was hire Stevie.

**Daniel Lopes:** So Stevie is joining the week after the on-site.

**Daniel Lopes:** And Stevie, she's an engineer that has been focused on products for the last 10 years or something.

**Daniel Lopes:** But she will be everywhere.

**Daniel Lopes:** Not a traditional product manager that you go ask and just ask her what to do.

**Daniel Lopes:** But more like one of us that will be supporting in different roles and getting insights from different parts of the org.

**Daniel Lopes:** And she'll start on the Strategy Springs with George and the team there.

**Daniel Lopes:** But for today's agenda, we have a few minutes.

**Daniel Lopes:** Cook FOIs first, and then a couple of reminders and things that we also uncovered during the series, things that we think might be an important milestone for the company if it turns out to be true.

**Daniel Lopes:** But we're not sure, so it's more of an assumption, an experiment we're running, so I want to share that with everybody here so we have full context.

**Daniel Lopes:** And yeah, so the first thing is the client ops engineering team, we're running in cycle system, and yesterday we introduced a new thing where one person of every cycle will be the person dedicated to triage the tickets, to answer the support tickets from the team in Slack, but also be the strategy sprint consultant.

**Daniel Lopes:** And just to clarify for the folks that haven't been here long enough, or that I haven't had the chance to share enough context, but the client, I see the client ops.

**Daniel Lopes:** almost like our first line of defense of understanding how can we actually serve our agency properly.

**Daniel Lopes:** And like their job is like, it's the people that can be on all the products at the same time.

**Daniel Lopes:** So if you're hitting like a small bug or something, they're getting blocked there, they have the autonomy to change.

**Daniel Lopes:** They should be the people that can like pull you out of your existing projects if something's super important and it's blocking important client.

**Daniel Lopes:** And they're also the people that will be doing like a lot of R&D stuff for us.

**Daniel Lopes:** Like some of the guys there are doing this cycle, for example, they're testing some things around agents for refreshing.

**Daniel Lopes:** Because refreshing is something that we know has different, like we don't have any workflows that are like agent-based.

**Daniel Lopes:** But refreshing is something we know could take different tactics and it would be nice to have something that can figure out what is the tactic to run depending on the size of the article and things like that.

**Daniel Lopes:** So that's the kind of stuff that we're doing with.

**Daniel Lopes:** And like...

**Daniel Lopes:** Same thing with images before.

**Daniel Lopes:** we ran for a while figuring out how we're doing it.

**Daniel Lopes:** So that came from the client ops engineering team figuring it out.

**Daniel Lopes:** And everyone else is just building the features for them and for the rest of the work to function.

**Daniel Lopes:** And we can always swap folks.

**Daniel Lopes:** If you want to spend time in the client ops team, just let me know.

**Daniel Lopes:** And you're there for why we buffer time or something like that.

**Daniel Lopes:** And you're always helpful.

**Daniel Lopes:** And I'm also thinking about having periods where you can just come up with a bunch of workflows and spend the whole work or most of the work building workflows for a couple of days or something like that.

**Daniel Lopes:** Just to keep us in the loop.

**Daniel Lopes:** Because the client ops team is building workflows all the time.

**Daniel Lopes:** The rest of the org is not.

**Daniel Lopes:** So until we close that gap where we make building workflows easier, we have to force ourselves to go back.

**Daniel Lopes:** So that's just a couple of things there.

**Daniel Lopes:** And in the future, we might start also doing.

**Daniel Lopes:** What I usually call a proactive support.

**Daniel Lopes:** That's something that we use to do at KNRP.

**Daniel Lopes:** would just look at Sentry and see who is the impacted user, have the email associated and things like that, and then reach out.

**Daniel Lopes:** Or actively check at what is crashing, and then tell people, hey, we fixed this.

**Daniel Lopes:** Here's how we fix it.

**Daniel Lopes:** You were impacted, just so you know.

**Daniel Lopes:** Because we get people, like yesterday, for example, I got the message from, I got the feedback from Andy that some folks on the team were thinking that the AI feature, the tip-tap AI feature, ask AI feature, is unreliable.

**Daniel Lopes:** But again, then I saw that the team was fixing it at the same time.

**Daniel Lopes:** So that feature is super important.

**Daniel Lopes:** So that would be the kind of one that we would want to say, hey, I saw that it didn't work for you.

**Daniel Lopes:** just made changes.

**Daniel Lopes:** Just to maintain the confidence with that person that that thing works, or that at least we're trying to make it work.

**Daniel Lopes:** So next week we're probably better, or something like that.

**Daniel Lopes:** But that's for the future and the next cycle.

**Daniel Lopes:** And...

**Daniel Lopes:** Another thing that you might have seen that like I switched a lot of our, now I have a ton of one-on-ones in my calendar and the way to, and I have one-on-ones with pretty much everybody every week.

**Daniel Lopes:** So all 12 folks in the product team.

**Daniel Lopes:** And the way I'm thinking about the sessions is more like a short-term solution until we hit certain points.

**Daniel Lopes:** And in my mind, the first year of growthx is like, it's the most important year for us.

**Daniel Lopes:** And that's a period that it would be important for us to like deliver on many things at the same time, but it's super hard to keep the threads aligned.

**Daniel Lopes:** And since I'm the one in the middle of everything, that's a hack for us to be like a loosely coupled org with like people working different projects at the same time.

**Daniel Lopes:** But without having the time and the ways of building proper context sharing practices.

**Daniel Lopes:** So, and we'll be, we'll stay pretty flat for, for at least this year.

**Daniel Lopes:** So I think I had.

**Daniel Lopes:** To be around 15 people, we're kind of excited that we're going to be.

**Daniel Lopes:** We're just missing probably a couple of people around the ML and AI part for the data science and machine learning.

**Daniel Lopes:** And that's something that we're probably going to add this year still, but we don't have any plans to have a traditional product manager.

**Daniel Lopes:** So you all have the autonomy to decide what that feature should look like or that workflow should look like.

**Daniel Lopes:** And we also don't have all the engineering managers for now and no plans to add.

**Daniel Lopes:** So this would be like you have full autonomy to figure out.

**Daniel Lopes:** I'm the check that you have guaranteed in the calendar that if you're confused or something, let's talk about it and let's clarify.

**Daniel Lopes:** And we can use the sessions as more like in design team, it's pretty normal to have design reviews of the team.

**Daniel Lopes:** And engineering is pretty normal to have code reviews as well.

**Daniel Lopes:** But those are like too strict.

**Daniel Lopes:** And in my mind, those are more like project reviews.

**Daniel Lopes:** Like work reviews and more like brainstorming than just like me checking if you're doing a good work.

**Daniel Lopes:** And so it's like more like let's brainstorm in the direction things are going.

**Daniel Lopes:** Let's see if it's aligned with the other groups.

**Daniel Lopes:** Let's see if there's any rabbit hole that might be coming ahead of time that we can predict and direct feedback on like specific work.

**Daniel Lopes:** Not like am I doing a good work in this project?

**Daniel Lopes:** How is it going in that previous project?

**Daniel Lopes:** How it went?

**Daniel Lopes:** So because we're to have all this fast feedback, we can keep it really close to reality.

**Daniel Lopes:** And but I also have 12 people to meet plus the leadership team.

**Daniel Lopes:** So like if you could help me prepare the agenda.

**Daniel Lopes:** Like I do have Alice going through our Gitbot every day and like summarizing things for me and all that.

**Daniel Lopes:** And like I'm following everything and I also answer my Gitbot almost every day.

**Daniel Lopes:** But it would be nice like if you have like things that you're struggling or things that you want to talk about, you want to project related things to or anything, just like put it in the agenda before and it helps.

**Daniel Lopes:** We also only have like 30 minutes.

**Daniel Lopes:** But I keep the slots pretty spaced.

**Daniel Lopes:** But if you go over the 30 minutes, that's fine.

**Daniel Lopes:** So that's why we have 30 minutes.

**Daniel Lopes:** And also, like, what you guys are doing is the most important stuff for me in the day at all.

**Daniel Lopes:** So, like, if I'm not available, I'll carve time.

**Daniel Lopes:** And I also work from 7 to 9 sometimes for certain stuff.

**Daniel Lopes:** So if you guys are in Europe and you're not having enough time to meet with me, we can probably find an alternative time.

**Daniel Lopes:** But important stuff, spending time together on actual work.

**Daniel Lopes:** And another thing that I wanted to check and just, like, share a bit of the context is that, like, why do we exist?

**Daniel Lopes:** Like, why I think this first year is so important.

**Daniel Lopes:** And to me, the only thing we care about this first year is, like, validating that this concept of services of software is actually possible.

**Daniel Lopes:** So that's the thesis.

**Daniel Lopes:** That's why we got the money.

**Daniel Lopes:** So

**Daniel Lopes:** We've the investment, and that's what we're trying to figure out.

**Daniel Lopes:** And the idea here is, in general, the whole AI space is essentially a race that we've never seen before.

**Daniel Lopes:** But if you've been in tech for more than 20 years, you probably have seen the 2000s, and then you saw the mobile transition with cloud stuff, then you saw the cloud stuff, and then you saw the mobile transition, and then you saw some of the crypto stuff.

**Daniel Lopes:** But this is very different than everything that came before, and everybody's super well-funded, and even incompetent players, which is kind of like muds the water quite a bit.

**Daniel Lopes:** So it's a different time.

**Daniel Lopes:** So we went from like a recession, a pre-recession, to now all the companies that are in the AI are getting a  ton of money.

**Daniel Lopes:** So essentially, the business pulled us out of recession if you're an AI company.

**Daniel Lopes:** So there is a lot on noise, and we need to figure things super fast and distinguish us from the noise.

**Daniel Lopes:** there's

**Daniel Lopes:** as fast as possible, and actually deliver on valuable things.

**Daniel Lopes:** And another thing that's happening is like our jobs are changing, and we need to be at the forefront.

**Daniel Lopes:** So what it means to be a developer today is completely different than before.

**Daniel Lopes:** What it means to be a designer will be different.

**Daniel Lopes:** And what it means to be like a content creation, like a writer or any other of the knowledge workers will completely change.

**Daniel Lopes:** So our year one goal, to me, I consider the first day of growthx, like the day after the fundraising.

**Daniel Lopes:** So we have March 1st, March 1st next year, to like make a huge progress in this direction.

**Daniel Lopes:** And I consider the fundraising as the day that I could actually build a team and stop building everything myself.

**Daniel Lopes:** And now that the team is assembled, it took like three to four months to have the whole team, which is like pretty fast for a normal pace.

**Daniel Lopes:** But now I have eight-ish months to like.

**Daniel Lopes:** Making good progress.

**Daniel Lopes:** And ideally, by the end of the year, we're going to have a good stride in that direction.

**Daniel Lopes:** And we already have that.

**Daniel Lopes:** So we have a lot of stuff with Atlas.

**Daniel Lopes:** have a lot of stuff with the flow project.

**Daniel Lopes:** We have a lot of workflows that the client ops engineering team built.

**Daniel Lopes:** And we still have a lot to go.

**Daniel Lopes:** And the main thing for the services of software thesis, the way I think about it is, essentially, I enabled a well-equipped person to perform as a team.

**Daniel Lopes:** So you can see the amount of code that Felipe, Brad, and me wrote during the Atlas project with some of the other folks.

**Daniel Lopes:** But the bulk of the commits came from the three of us.

**Daniel Lopes:** And it's a gigantic amount of code for that short period.

**Daniel Lopes:** And the same, like, I think we were, like, at 25,000 lines of code.

**Daniel Lopes:** Can I repeat, because for 150,000 lines of code, took us, like, five years.

**Daniel Lopes:** So on a team of four.

**Daniel Lopes:** And pretty much.

**Daniel Lopes:** Similar experience.

**Daniel Lopes:** So you can see the delta of how fast things can move now if you really take advantage of these tools, but these are not available for everybody.

**Daniel Lopes:** So that's what we're building here.

**Daniel Lopes:** We're trying to build the same set of tools for a different role that are not programmers.

**Daniel Lopes:** Programmers who are getting the first-hand glimpse of the future and things are getting built for us because they think they need that for AGI, essentially.

**Daniel Lopes:** That's why OpenAI trained so well their models.

**Daniel Lopes:** And same fact, Anthropoc just landed on Cloud Code as a good marketing thing that they were looking for applications and they landed on it.

**Daniel Lopes:** But OpenAI is actually training their models for being able to code.

**Daniel Lopes:** So those are two things we know it's going to keep improving.

**Daniel Lopes:** The other roles are not the same.

**Daniel Lopes:** So our job is to make the role of a content marketer or a content creator in that space.

**Daniel Lopes:** Closer to what you're experiencing as programmers.

**Daniel Lopes:** And to me, like the year one goal is like, can we scale our pilot content agents in this format?

**Daniel Lopes:** And like, can we build all the necessary tools for all the core functions for our pilot agency?

**Daniel Lopes:** And to me, these roles are slightly three, not three roles per se, not like job functions, but areas.

**Daniel Lopes:** And we have like the strategy area.

**Daniel Lopes:** We have Marcel, George, and Ada is like a good example.

**Daniel Lopes:** So those are just examples.

**Daniel Lopes:** names I'm giving you is just good examples for you to like visualize who you're working for.

**Daniel Lopes:** And that's the only person you work for.

**Daniel Lopes:** You don't work for the client, you work for them.

**Daniel Lopes:** And they work for the client.

**Daniel Lopes:** And what Marcel, George, and Ada will do is just they will like, first thing that they do is like architect the process.

**Daniel Lopes:** like they will be like, Marcel is already in house.

**Daniel Lopes:** Marketer, and he'll think about what are the things that are repeatable systems, what kind of templates we can have, how do I deconstruct my work as a high-level, high-experienced marketer in a way that systems can run or people can help systems execute.

**Daniel Lopes:** And then George and Aida are in that space as well, helping him with that.

**Daniel Lopes:** And then we also have a core part of that is like the calibration of input.

**Daniel Lopes:** So that's taking the strategy from the client conversations, like understand what the client wants, like understand the target audience, like understand the message, like calibrate the tone, like what are the success metrics, just like set up the whole project for success, but also set up the workspace for the AI systems to work for their person.

**Daniel Lopes:** So like, if we're translating this to a developer scenario, like this would be the equivalent of landing on a new code base and spending the first couple of weeks, just like writing the readme.

**Daniel Lopes:** So that'll let everyone understand.

**Daniel Lopes:** Adding a readme to every folder that matters, like figuring out all the dependencies that are listed in the cloud code or the cursor rules that should be checked.

**Daniel Lopes:** All the things that will make the experience of using a tool like cursor or cloud code perform 10x better than the random dude that doesn't know how these things work and just try it for 30 minutes and think this doesn't work.

**Daniel Lopes:** You know, so this stuff doesn't exist for our space.

**Daniel Lopes:** we're having to create like the artifacts feature.

**Daniel Lopes:** We are trying to add a knowledge base to parse the call.

**Daniel Lopes:** We're trying to like make their lives easier, essentially.

**Daniel Lopes:** And then another function here, a good representation of this role is like somebody like Simi, and they will like refine the production.

**Daniel Lopes:** They operate the production machine and they are not just button clickers.

**Daniel Lopes:** They're the people that are controlling like the quality of the output.

**Daniel Lopes:** They're like, they're adjusting.

**Daniel Lopes:** Just seeing it, they are like essentially our experienced editorial eye that knows when the article or the content is ready to be sent to the client or that meets their goal.

**Daniel Lopes:** And then the third person that I think is like the perfect representation is like Clarkson to me.

**Daniel Lopes:** It's just like, it's our AI workflow engineering skill and like the ideal person there will combine like deep knowledge about content creation and what kind of things we need to do in that space and also have a deep knowledge of like how LLMs work, can code because we all code the first environment and has also the experience to be able to create reliable production level AI systems.

**Daniel Lopes:** Like our workflows run like millions of tokens a day.

**Daniel Lopes:** So those are the three people we work for essentially.

**Daniel Lopes:** We work for Marcel, Jordan, Ada when we're thinking about strategy.

**Daniel Lopes:** So whenever your building features are on that area.

**Daniel Lopes:** Think about them.

**Daniel Lopes:** Same thing.

**Daniel Lopes:** Seedling is a good example.

**Daniel Lopes:** Kirkland is another one.

**Daniel Lopes:** If you're making data life worse, we're going against our year one goal.

**Daniel Lopes:** And so that's the primary thing in my mind.

**Daniel Lopes:** So we're not building a SaaS for general use in first year.

**Daniel Lopes:** We're building tools for these three functions.

**Daniel Lopes:** And so the number one thing is scaling the agency by making strategy, the production, the production and AI engineering.

**Daniel Lopes:** And in my mind, we're like a seed stage product.

**Daniel Lopes:** Although like we have series A, even like series B level of revenue, we are a seed stage product.

**Daniel Lopes:** So every day matters.

**Daniel Lopes:** So keep that in mind.

**Daniel Lopes:** And like a lot of things that we usually do at other companies, we can probably not do it at all here because we built the company to be able to shortcut the sense.

**Daniel Lopes:** So we can move as fast as possible.

**Daniel Lopes:** So we're building an internal tool.

**Daniel Lopes:** I don't care about reusability much.

**Daniel Lopes:** I don't care about having the.

**Daniel Lopes:** Perfect, like, Figma design system.

**Daniel Lopes:** I don't care about uptime.

**Daniel Lopes:** So if the thing is down for, like, half a day, it doesn't matter.

**Daniel Lopes:** Like, the only thing that matters is to give the team the heads up.

**Daniel Lopes:** So, like, we're going to be down tomorrow for three hours.

**Daniel Lopes:** Create all your content before.

**Daniel Lopes:** That's totally possible.

**Daniel Lopes:** Like, you would never do that in another place.

**Daniel Lopes:** That would, like, you would be fired for sure.

**Daniel Lopes:** Here, if that's necessary for us to move fast on something that's meaningful to make these three roles more capable, we should totally do it.

**Daniel Lopes:** So, and another thing is, here, you can go straight to the top.

**Daniel Lopes:** Like, like, one thing that I see folks doing here sometimes is just, like, talking to folks that are also still onboarding and trying to get their take on things.

**Daniel Lopes:** And, like, everybody's super new here.

**Daniel Lopes:** So, I mean, this company is, like, started in March.

**Daniel Lopes:** And a lot of the roles on the delivery team, we're also trying to figure out, the same way we're trying to figure out the feature set and the systems, we're also trying to figure out how the people process works on the other side.

**Daniel Lopes:** They're not even sure if, like, the people that would have hired...

**Daniel Lopes:** ...

**Daniel Lopes:** The exact people that will be here next year.

**Daniel Lopes:** It's like, well, I don't know.

**Daniel Lopes:** I just should be straight up honest.

**Daniel Lopes:** We're trying to figure that out.

**Daniel Lopes:** And that's as part of a problem is figuring out the features.

**Daniel Lopes:** So, but all of our managers here, they are super high caliber ICs as well.

**Daniel Lopes:** And they are fully familiar with the functions.

**Daniel Lopes:** So if you have a question that's not available and it's related to strategy, go straight to Marcel.

**Daniel Lopes:** If you have a question related to GTN or anything, even like related to workflows, go straight to Jason.

**Daniel Lopes:** Kirkland is not available, go straight to Jason.

**Daniel Lopes:** And same thing, if it's something related to sales and I'm not available, go straight to Kyle and Regent.

**Daniel Lopes:** And if it's something related to content quality, Panzer, like don't talk to anybody in between, go straight to the top.

**Daniel Lopes:** And that would be the best shortcut that in other companies that would be supposed to have to talk to a product manager.

**Daniel Lopes:** And another thing that I wanted to share like real quick, and then we go to the demos.

**Daniel Lopes:** is the assumption that it might be already in the point where we have product market fit for a specific ICP.

**Daniel Lopes:** The ICP might be too small, or maybe I'm off here, but it looks like based on the strategy screens that certain clients are easy to onboard, and they are super happy during the transition to the next phase.

**Daniel Lopes:** Now we have to figure out if the next phase works, and also if we can find more of those.

**Daniel Lopes:** But if you're not fully familiar with ICP, the way to think about it in our context would be you have a large target audience with pain points.

**Daniel Lopes:** In our case, almost every B2B company needs high volume content for whatever kind of content.

**Daniel Lopes:** But that should bother still.

**Daniel Lopes:** And then the next stage down is B2B companies that need a high volume, they're volume dependent based on their GTM.

**Daniel Lopes:** And so that, for example, let's say they're, say, they're.

**Daniel Lopes:** Not sales led selling a million dollar contract five a year.

**Daniel Lopes:** They need to sell like dozens of things, you know, a month, but they really need to produce it on the content.

**Daniel Lopes:** And they are in markets, are not super overcrowded, there's like amazing players.

**Daniel Lopes:** They already took all the keywords and you can't make a dent.

**Daniel Lopes:** And, but they also have like established domain or like they are in the path to create one or they know how to create one.

**Daniel Lopes:** And so that's like pain points plus fit makes for a potential customer, but like the really good one would be somebody that's like has pain points, has the fit, they are ready to buy, and we are ready to serve them.

**Daniel Lopes:** And just based on some of the stuff we already viewed and some of the stuff the team is already super good at doing, it looks like we can have, we might have some of that.

**Daniel Lopes:** But the matrix to figure that out is a little bit more complex than just like the usual demographics or formal graphics or, or, or, or, or.

**Daniel Lopes:** Other things that we might have seen at other companies, because we serve like pretty much a bunch of different companies can automate things with what they are.

**Daniel Lopes:** So how do we handle that?

**Daniel Lopes:** So the way we're thinking about, give me one second, close my notion by accident.

**Daniel Lopes:** The way, this is like, we're still testing this, but no means like a final thing.

**Daniel Lopes:** We talked about this yesterday in the ship meetings, like it's super fresh.

**Daniel Lopes:** It's not validated at all.

**Daniel Lopes:** But I just wanted to share so you guys see where are we going.

**Daniel Lopes:** And so like, it would be breaking down the clients in a bunch of operational traits and a couple of financial health traits.

**Daniel Lopes:** And operational traits would be things like, how quickly can the decision get made there?

**Daniel Lopes:** Like, is it like a single DRI?

**Daniel Lopes:** Like, maybe it's the CEO and the CEO understands marketing.

**Daniel Lopes:** And like, he cares about it.

**Daniel Lopes:** Or it's a head of marketing.

**Daniel Lopes:** And that person will clear any blockers we have.

**Daniel Lopes:** And then you go down to.

**Daniel Lopes:** Like a community where there's a couple of two-to-three stakeholders.

**Daniel Lopes:** And then you have full bureaucracy.

**Daniel Lopes:** You have web flow.

**Daniel Lopes:** Some of the bigger players fit in this.

**Daniel Lopes:** So you need to clear the bar with a bunch of people.

**Daniel Lopes:** And all this stuff is like, do they have a team?

**Daniel Lopes:** And so this would be like, we'll be scoring all the clients against this and see which one has the highest.

**Daniel Lopes:** And then in retrospect, look if we could have served those clients today with the things we have now and try to guess.

**Daniel Lopes:** It's not going to be a precise client, but other things we look for is like content production history.

**Daniel Lopes:** Like let's say they have more than like, if they have a hundred page, for example, they care about their, their, their, they consider content something that is meaningful.

**Daniel Lopes:** That's kind of like another one kind of like a little bit related market difficulty and their content strategy buying is a huge importance thing as well.

**Daniel Lopes:** So like, this is not weighted at the question level.

**Daniel Lopes:** So that might be something we might have to do.

**Daniel Lopes:** But for example, we have.

**Daniel Lopes:** Clients like Vappy, where the CEO was there and he was pushing for important things, but they didn't really care about the content as an important strategy buy-in at the same level that some other clients do care.

**Daniel Lopes:** Like, for example, Tau is another client that we have that they haven't even launched, but they're preparing the whole roadmap for the future.

**Daniel Lopes:** And so we don't have to rush there, but it's still important.

**Daniel Lopes:** And then we have a bunch of other things that we're thinking about, but at the end, we'll validate this week that if the clients that we think are good, that we could serve, if there's four high, then this matrix is at least in a good direction.

**Daniel Lopes:** And so that's some of the stuff we've been working on on the other side of the company.

**Daniel Lopes:** And like I said, we were essentially running four experiments at the same time.

**Daniel Lopes:** It's not going to be a full scientific experiment.

**Daniel Lopes:** don't have time for like volume and data, so we run a lot of based on gut feeling.

**Daniel Lopes:** And yes, that we're going in right direction.

**Daniel Lopes:** But essentially, the GTM team is like, they will be like classifying the current and past clients using this matrix.

**Daniel Lopes:** And then probably the second thing we could try to do there is like, see if we can find more of those, you know.

**Daniel Lopes:** I don't know if it's like a thousand or like, it's just like, can we find something?

**Daniel Lopes:** And then the strategy team will just try to continue to pay attention to this ICP as they come to the funnel and see if we can still serve them well.

**Daniel Lopes:** And for all the team, we need to, we'll start with just the client ops engineering team, pay attention to like some of the critical folks that will be like doing the production side.

**Daniel Lopes:** So the production side, I think we're going to have a couple of folks like running production end to end.

**Daniel Lopes:** Like one person going from assignment all the way to trying to produce the article at the end.

**Daniel Lopes:** And if they raise their flags and like our foe is bad here, the UI is too slow here, like we got to fix it immediately.

**Daniel Lopes:** And, uh,

**Daniel Lopes:** And for now, would be just like me and probably Nicolas coding whatever they need there.

**Daniel Lopes:** But if you need more help, we'll pull you guys into this.

**Daniel Lopes:** And the general impact on EPD is like if we confirm the ICP, we're 0.70% of our efforts in these areas.

**Daniel Lopes:** And it will be on the three functions that we talked about.

**Daniel Lopes:** The strategy side, the production side, and the AI engineering side.

**Daniel Lopes:** And we're probably going to put more effort in the strategy and production side, but the AI engineer can't be abandoned.

**Daniel Lopes:** Because that's like we can't get, we need to keep getting better at creating workflows.

**Daniel Lopes:** So I hope that gives like a gist.

**Daniel Lopes:** I know it's a lot for 30 minutes, but I hope that gives a gist.

**Daniel Lopes:** And if you have questions, we can try to tackle that at the end.

**Daniel Lopes:** But we're probably going to run out of time, so we can cover that in our one-on-ones.

**Daniel Lopes:** And then we can switch to demos.

**Daniel Lopes:** For today, we have four people, if I remember correctly.

**Daniel Lopes:** we have Kirkland, Ben, Brad, and we will talk about images.

**Marcel Santilli:** I'll cover it.

**Marcel Santilli:** I know those a lot, but hopefully this is mostly like things we talked about before.

**Marcel Santilli:** But I'm curious, is there anything that on my end and Kyle's end, like we're talking to a lot of people every day.

**Marcel Santilli:** We're talking, you know, I'm in the weeds with customers.

**Marcel Santilli:** I am demoing Atlas in the studio three or five times a day, essentially.

**Marcel Santilli:** And so getting reactions from VCs, getting reactions from customers, from prospects, if there's ever anything, if there's any quick ones or anything, but also like just overall, like we have a lot of insights to share.

**Marcel Santilli:** just try not to like overwhelm, you know, or reactions and things.

**Marcel Santilli:** But if there's ever anything, always happy to answer, but I don't know if anyone has any questions or anything.

**Marcel Santilli:** I that I can help give context to.

**Daniel Lopes:** Yeah, feel free to unmute then.

**Ben Church:** I want to go all the way back up the stack for a question.

**Ben Church:** On the on-call rotation with the client ops engineer, we're going way, way back, this first couple of slides.

**Ben Church:** What are you two thinking about how to get some of those insights over the line from the client-focused engineering teams over to, like, more product-focused engineering teams?

**Ben Church:** Like, I'm definitely coming away with stronger opinions having to do the workflow for the first time than I did in the vacuum.

**Daniel Lopes:** Yeah, yeah.

**Daniel Lopes:** Like, you are a great example, Genki, you guys are just creating workflows, so you kind of fit in that persona.

**Daniel Lopes:** And it will be in that persona for a while, until you stop creating workflows, if you have free time, keep doing it.

**Daniel Lopes:** But I think the plan is...

**Daniel Lopes:** It's like, I'm still going to be like in all the planning cycles and like seeing like, so if you file a ticket, we'll keep that in mind.

**Daniel Lopes:** We're also going to have the, Stevie will be playing that role as well of being more of a product person across all from strategy all the way to support and raising that as features that are needed.

**Daniel Lopes:** So that's kind of like something that if you are a product manager, you can like see the gaps of things and think about features that can be done.

**Daniel Lopes:** Some of you guys have this capacity too.

**Daniel Lopes:** So I've seen like Peter building a feature that I saw you doing that as well, Ben.

**Daniel Lopes:** So like anything that you find that that will move things in the right direction, you can just like put in a ticket.

**Daniel Lopes:** And then if we have time, we can just do that, like we don't need to like do the sprints or anything on that side.

**Daniel Lopes:** And we can always think about the, we can roughly estimate things too.

**Daniel Lopes:** So like, if it's like, like half a day, probably worth doing.

**Daniel Lopes:** If it's going to move the needle, if it's like five days or two days or three days, that's probably worth shaping a little bit.

**Daniel Lopes:** And then we'll talk about shaping next week.

**Marcel Santilli:** And I don't know if it's possible, like one thing too related, somewhat related to that, Daniel, is like back in the day, me building workflows in air ops and other places, like where I was spending like thousands of hours doing this stuff.

**Marcel Santilli:** I think there's one of the bigger lessons I learned, I know now the speed of creating workflows is way faster, was sometimes like thinking through the architecture first made a huge, huge impact, obviously.

**Marcel Santilli:** And like the way I was thinking about it originally, it was kind of like thinking of the function behind the steps, not just the steps themselves or the prompts.

**Marcel Santilli:** And definitely don't go into prompts as much, but like the way I was thinking about it is like, for instance, like there was like critic step, right?

**Marcel Santilli:** Like, so, so like a critic step, like we.

**Marcel Santilli:** Recently, you know, Pedro worked on the one for Biologica, and it was like, you're trying to think of like, who's the best critic for this that can be, have a critical judgment step on this.

**Marcel Santilli:** And sometimes like what we've been experimenting a lot of the strategy sprints and even before, it was just like, sometimes the sequence or how we think about the function of the step goes a much like kind of shortcuts to a better output, you know?

**Marcel Santilli:** And whereas like before, I remember just spending like two weeks trying to refactor our main draft workflow back in the day, and it was just like, this is useless.

**Marcel Santilli:** And then I had to take a step back and re-architect the thing, and then I found a better path, you know?

**Marcel Santilli:** And so it's like, you're getting stuck.

**Marcel Santilli:** Like, don't push too hard, you know?

**Marcel Santilli:** It's almost like it's just it.

**Daniel Lopes:** I think like now we have like full stack spectrum.

**Daniel Lopes:** Like I said, it's three functions.

**Daniel Lopes:** So some stuff will be like featured that are missing on the stereo side, some stuff is featured that are missing on the production side, so the grid doesn't work.

**Daniel Lopes:** Or tippy-tap AI doesn't work.

**Daniel Lopes:** Where he doesn't put...

**Daniel Lopes:** Produce the right results or something like that.

**Daniel Lopes:** Like those, like if you see that, like when you have an idea, you probably can just like file a ticket and try to fix it.

**Daniel Lopes:** If it's small, if it's bigger things, if it's related to workflows, might be a little harder because you need to change the framework or not.

**Daniel Lopes:** So you like just bring in our one-on-ones or like tag me and that's going to be enough because I'm going to be holding all the trends for the next six months.

**Daniel Lopes:** So yeah, I can prioritize anything.

**Daniel Lopes:** And so that's the short answer.

**Daniel Lopes:** Like it's just a shortcut.

**Daniel Lopes:** Cool.

**Daniel Lopes:** Demos, Kirkman, do you want to go first?

**Ben Church:** He said he was fixing his audio.

**Daniel Lopes:** Oh, okay.

**Daniel Lopes:** Then you are up next and you want to cover the web stuff?

**Ben Church:** Sure.

**Ben Church:** After all the chat and the high-level stuff, this is going to be extremely underwhelming, but we'll make it quick.

**Ben Church:** Make it quick.

**Ben Church:** So I'm sent I'm over.

**Ben Church:** Sure.

**Ben Church:** Let's go to desktop.

**Ben Church:** Boom.

**Ben Church:** Yeah.

**Ben Church:** So this, the preface here is like likely a bit of overengineering and hit some nice little like roadblocks along the way.

**Ben Church:** However, I think useful.

**Ben Church:** And what I'm going to demo is like part of the new Webflow publish workflow.

**Ben Church:** So like the TLDR is like a lot of our clients want publishing to Webflow, right?

**Ben Church:** That's a reasonable request.

**Ben Church:** And to actually create the workflow for Webflow, it's quite annoying because, let's see if can pull open Bruno here, give an example.

**Ben Church:** You have for these different collections.

**Ben Church:** Let's see if I can kick this one off.

**Ben Church:** You have different fields.

**Ben Church:** And a lot of the time, the slug, like the identifier needs to fit the field, doesn't match what the display name is, right?

**Ben Church:** So people go and change the display name.

**Ben Church:** And this slug remains the same.

**Ben Church:** So you can imagine you change like, hey, this is our, the start is our call to action text.

**Ben Church:** And now it's like our FAQ footer text, but the slug doesn't match up.

**Ben Church:** So we had in our workflows a lot of time was like coercion to this.

**Ben Church:** Like you have to go understand what the web flow is today and then like how things map.

**Ben Church:** At the same time, there's like transforms from like a URL to a web flow type.

**Ben Church:** There's, you know, different coercions from enums.

**Ben Church:** This is another crazy one where you guys see it in here.

**Ben Church:** Let's go into case study collection.

**Ben Church:** think we'll see it.

**Ben Church:** And you'll find in a lot of these, they'll have enum fields and these enum fields are huge, right?

**Ben Church:** They're authors.

**Ben Church:** So you could have like a hundred authors.

**Ben Church:** It could be blog types, under blogs.

**Ben Church:** And this blows up pretty big with web flow itself or barebytes web flow.

**Ben Church:** Some of the pride kicked me out, but you can see on the side here, like these are all their cat.

**Ben Church:** categories and enums, and it just gets crazy.

**Ben Church:** So in here is where we have the good call Webflow publishing workflow that was written by hand.

**Ben Church:** And like, you know, the workflow itself isn't too big.

**Ben Church:** The activities all, you know, nuanced understanding of Webflow and the types all written by hand to do this.

**Ben Church:** So I did this for Airbyte in the first iteration, and they had just so many different types and enums, it just started getting out of hand.

**Ben Church:** We're at the point where someone's like, hey, we need a blog type.

**Ben Church:** And I'm like, oh, my God, this is to take me another half day to do.

**Ben Church:** So instead, we made it declarative.

**Ben Church:** So I head over to the new publish generic.

**Ben Church:** So this handles both updates and adding new Webflow articles, whereas before, those were also separate workflows.

**Ben Church:** And the workflow file, very skinny.

**Ben Church:** Activities file, very skinny, and all the logic essentially lives in Webflow Client Config.

**Ben Church:** And you can see, like, say for blog here, you can see, like, all the enums to resolve, right?

**Ben Church:** If you want to do a company updates, you can now just save that, and we'll do our best match to get it back to this ID.

**Ben Church:** But I'll keep scrolling down.

**Ben Church:** This is just for two different types of collections.

**Ben Church:** Anywho, this is still a lot to write.

**Ben Church:** So we also have a generator in the project.

**Ben Church:** Let's go up and grab.

**Ben Church:** I think that's my most recent one.

**Ben Church:** So I'll put it out to the right spot.

**Ben Church:** There's my...

**Ben Church:** There you go.

**Ben Church:** We'll make this a little bigger.

**Ben Church:** .com.

**Ben Church:** Oops.

**Ben Church:** Getting out of that.

**Ben Church:** Lost my cursor.

**Ben Church:** Oh, and then you can go select what types of categories you want to start publishing.

**Ben Church:** So for here, you can do blog posts.

**Ben Church:** Let's go down to data engineering resources.

**Ben Church:** You hit enter, and I'll go make all the, you know, API calls to get all the collections, the collection information, and all the enums per collection, and generate this file for you, in addition to the types for Zod.

**Ben Church:** And the debug information, in case you want to see if something went wrong.

**Ben Church:** Thank you.

**Ben Church:** So now, anytime a client needs a Webflow publishing workflow, you can just generate it, instead of making a bunch of API calls yourself and writing it.

**Ben Church:** So, should take less than a minute after I spend it.

**Daniel Lopes:** Yeah, that's so cool.

**Marcel Santilli:** By the way, the CPO of Webflow is our angel investor.

**Marcel Santilli:** And obviously Webflow is a customer.

**Marcel Santilli:** And so if there's any angle here of taking this more publicly, because like this is such a pain in the .

**Marcel Santilli:** I've done integrations for like Webflow when I was trying to automate publishing using Aerofs and NAN and a bunch of others.

**Marcel Santilli:** And like this thing is such a big pain in the  for every single person that has a Webflow site.

**Marcel Santilli:** So I feel like this would be a huge like gaining community love if there's a way to like.

**Marcel Santilli:** Like, I don't know, I can't, I can't think of it and it's not urgent at all.

**Marcel Santilli:** And as Daniel describes me, I'm the chief destruction officer.

**Marcel Santilli:** So, but this is really  cool.

**Daniel Lopes:** All right.

**Ben Church:** Cool.

**Ben Church:** Awesome.

**Ben Church:** Yeah, cool.

**Ben Church:** All right, that's it.

**Daniel Lopes:** Awesome.

**Daniel Lopes:** Thanks, Ben.

**Daniel Lopes:** Kirkman, ready?

**Kirkland Gee:** Yeah, I'm ready now.

**Kirkland Gee:** I'm outside, so I apologize if my audio sucks.

**Daniel Lopes:** My headphones died in the last couple of minutes of this.

**Daniel Lopes:** That's good.

**Kirkland Gee:** You know, it is what it is.

**Kirkland Gee:** But I'll try to be.

**Kirkland Gee:** Quick, because what I got going on isn't anything too crazy, but basically we just, you know, been trying to do programmatic stuff for a while, bunch of different workarounds and ways of doing programmatic SEO.

**Kirkland Gee:** And essentially we now have just a couple of like frameworks to work with to make this a lot easier.

**Kirkland Gee:** Obviously there's still going to be edge cases where we need custom data ingestion and all that crazy stuff.

**Kirkland Gee:** But for like most of the programmatic SEO where it's like, hey, you know, for, we want this list of ingredients or requirements for this type of document for every city in the country, or we want to compare some list of a hundred tools, all of them against each other.

**Kirkland Gee:** We have some ways of doing that.

**Kirkland Gee:** So this is in the GrowthX workspace in Atlas, but there's some predefined configurations for this.

**Kirkland Gee:** essentially what we're doing is using, Daniel kind of made one custom workflow and then we're making use of our existing researcher workflows.

**Kirkland Gee:** But essentially all we have to do is use our existing researcher, pass in a list of questions that we want to ask and just interpolate whatever variables.

**Kirkland Gee:** Like we want to know use cases and benefits for a given topic.

**Kirkland Gee:** Some of the others are much more complex in terms of the amount of questions that we're asking.

**Kirkland Gee:** And then we have a version of our article draft workflow that takes in a template and then writes the article based on that template rather than taking in an outline that's generated.

**Kirkland Gee:** And so we're doing this by creating templates in the artifacts in Atlas.

**Kirkland Gee:** So you can define exactly what you want the article to look like in just plain markdown.

**Kirkland Gee:** And then you run this and you're going to get an article that matches that template with whatever research information provided.

**Kirkland Gee:** Same thing if you want to do a comparison.

**Kirkland Gee:** In this case, we're doing the same thing, but we're just providing the two different tools, running two research steps with the same set of questions, one for each tool, and then populating that comparison article template with whatever was researched.

**Kirkland Gee:** And then we can run whatever other steps, fact checking, internal linking, FAQ generation that we would typically do after that.

**Kirkland Gee:** So there's a bunch of cases where this is being used already, like SIT, or however you pronounce this, has a...

**Kirkland Gee:** Couple of different article templates they're using.

**Kirkland Gee:** So like alternatives for Slack or comparing different tools together or doing an overview of tools.

**Kirkland Gee:** And again, the way that they kind of got around this is they just have different artifacts, right?

**Kirkland Gee:** So here is their template for tool A versus tool B.

**Kirkland Gee:** They want an introduction.

**Kirkland Gee:** They want this information, blah, blah, blah, how it integrates.

**Kirkland Gee:** And then we're addressing all of that in the research.

**Kirkland Gee:** So again, it's really not anything crazy fancy, but we already have five or six different pipelines using this kind of setup.

**Kirkland Gee:** And it's just making those general programmatic use cases, one, the outputs better, and two, just a lot less workarounds and weird, funny stuff we have to do on the front end.

**Kirkland Gee:** And now if like someone needs a PSEO campaign, unless it's something super complicated, we can spin that up in five minutes by just copying over those templates, filling out the template, filling out the research questions.

**Kirkland Gee:** And if they don't like the outputs, all they have to do is change the artifacts.

**Kirkland Gee:** They don't have to actually go ask us to do more workflow stuff.

**Kirkland Gee:** They can just change the template they're working with.

**Kirkland Gee:** So, super simple.

**Daniel Lopes:** Yeah, that's super helpful.

**Daniel Lopes:** And that's like the one thing that I think it's missing to like really nail all the programmatic SEO stuff is the concept of a knowledge base.

**Daniel Lopes:** Because now we just use the research or whatever is public on the internet.

**Daniel Lopes:** So it's based on perplexity.

**Daniel Lopes:** So whatever perplexity can do.

**Daniel Lopes:** But in the future, we'll be able to just like load a database of all the things you care about.

**Daniel Lopes:** And we can pull from there.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** And we like we have some cases where we might be doing something like that now, but it's a custom where it's separate from this.

**Kirkland Gee:** But yeah, once we have a knowledge base, you just plug in whatever data you want included.

**Kirkland Gee:** And then we can do some really cool stuff with that.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Awesome.

**Daniel Lopes:** That's amazing.

**Daniel Lopes:** Thanks for doing that, Kirkland.

**Daniel Lopes:** Next one.

**Daniel Lopes:** Red, are you ready?

**Brad Herman:** Sure.

**Brad Herman:** There we go.

**Daniel Lopes:** Can you hear me?

**Daniel Lopes:** Yeah.

**Brad Herman:** Yes.

**Brad Herman:** Sweet.

**Brad Herman:** How's the audio quality?

**Brad Herman:** I just got these new headphones and I like still don't know.

**Brad Herman:** It doesn't sound great when it comes through.

**Brad Herman:** Let me see, okay, let's see, share my screen here, content, okay, yeah, so just, I want to show you guys this tip-tap stuff real quick, apparently, more people are using it than I realized, which you don't find out until it breaks, generally, which is the unfortunate reality of, you know, work in our day and age, but anyways, so one thing I'm working on right now, and this is just up right now, is kind of like a playground, essentially, where you can actually use this outside of, like, the, your typical pipeline or artifact generation, so trying to turn off my autocomplete, so you'll be able to come in here and actually generate documents and, like, modify your prompts and that sort of thing and kind of get away from using Claude, like, entirely, and what this will do, will push you into essentially the, the, the,

**Brad Herman:** flow that I'll show you here in just a minute.

**Brad Herman:** One second.

**Brad Herman:** What happened?

**Brad Herman:** Let me go to workspace.

**Brad Herman:** Sorry, work in progress.

**Brad Herman:** And this damn toolbar keeps covering my stuff.

**Brad Herman:** I don't like Zoom.

**Brad Herman:** Sorry, guys.

**Brad Herman:** There we go.

**Brad Herman:** Okay.

**Brad Herman:** So I'm going go into a context artifact right now just to show you because it's a little easier than, like, digging into a pipeline.

**Brad Herman:** But essentially, you know, what we built was we're using this back-end thing, which is backed by Prozmere, which is called TipTap.

**Brad Herman:** And TipTap is essentially like a what-you-see-is-what-you-get editor that allows you to do a lot of really cool things.

**Brad Herman:** And it's very extensible.

**Brad Herman:** has, like, a massive set of plug-ins and whatnot.

**Brad Herman:** We kind of built our own for everything, though, here because we want to be able to control, you know, more advanced features.-environatory doing takes know before the

**Brad Herman:** We want to be able to control the AI side of things, et cetera.

**Brad Herman:** There's some stuff that we could probably leverage later, like actually like collaborative document editing and that sort of stuff.

**Brad Herman:** But we didn't go that far because obviously we only had about a month to build the entire system in this.

**Brad Herman:** But some of the things that we built into this are AI powered.

**Brad Herman:** So if you select any text, for instance, you've got these AI shortcuts where you can come in and actually take care of like some very common like use cases.

**Brad Herman:** You'll see verified technical accuracy, simplify, you know, brand voice, et cetera, editorial, et cetera, like that.

**Brad Herman:** You can also jump in and ask AI directly to not only work directly on like, you know, individual pieces of text, but you can also, you know, do like full document edits.

**Brad Herman:** So here I'm going to refresh and there's also hot keys built in as well.

**Brad Herman:** So I can say like, you know, add some 1950s baby names in a bullet.

**Brad Herman:** List, limit to six, there we go, and oh, I'm not running my server, typical problem of live demos, one second, let me run the server, over my index, node is incompatible, course, one second, there we go, there we go, copy and paste this, server is almost running,

**Brad Herman:** There we go.

**Brad Herman:** Let's see if anybody's added in my favorite missing environment variables.

**Brad Herman:** There we go.

**Brad Herman:** So now it's actually going to work.

**Brad Herman:** Some of the stuff that I built into this is kind of cool.

**Brad Herman:** So it'll actually ask, like, clarifying questions.

**Brad Herman:** If it needs to, it'll apply.

**Brad Herman:** You can decide to accept and reject changes, either one by one or overall.

**Brad Herman:** So just added that in.

**Brad Herman:** You can also add in auto accept, just kind of like a cursor.

**Brad Herman:** Some other things that you can do, which is kind of cool, is you can actually include artifacts as context, just like you would, like, within cursor.

**Brad Herman:** So you see here, you can reference different ones.

**Brad Herman:** You can also come here and say, let's do the writing guidelines and audience personas.

**Brad Herman:** And that'll include everything as context.

**Brad Herman:** You can also add selections directly.

**Brad Herman:** So we can work directly on, like, a specific piece of content.

**Brad Herman:** Or you can have it rewrite the whole document if you want.

**Brad Herman:** right.

**Brad Herman:** I'm watching.

**Brad Herman:** So really cool things that we can do with this.

**Brad Herman:** Like I said, the next thing that's coming up is the context artifacts.

**Brad Herman:** And also there's this like nice helper here, which I guess a lot of people didn't know existed.

**Brad Herman:** It'll tell you like how to actually use it and how to use keyboard shortcuts and that sort of stuff.

**Brad Herman:** But the next thing that's coming up, like we said, is we're trying to build out this AI assistant, which of course is.

**Daniel Lopes:** Quick question from Marcel, what is the context if you don't select anything in that case of the article?

**Brad Herman:** So if you don't select anything, the context is the full document and then a prompt, which we kind of wrote moderately well.

**Brad Herman:** Kirkland and I are actually going to talk a little bit later today about improving our prompting so that we can get a lot better results.

**Brad Herman:** And the other thing, too, right now is that it doesn't allow you to change the model.

**Brad Herman:** So I think the default.

**Brad Herman:** Fathomodel is Claude 3.5, but I need to go in and check.

**Daniel Lopes:** There's like six files I have to dig through to figure out what the default is.

**Daniel Lopes:** We'll be nice to switch to four.

**Brad Herman:** Yeah, yeah, so we switch to four, or yeah, it might have even been like, oh, no, it's not 03.

**Brad Herman:** It is Claude, but I can't remember which one.

**Brad Herman:** So we'll switch that to four on the default and then allow you to change it as well.

**Brad Herman:** We do, we have talked, yep.

**Marcel Santilli:** Yeah, sorry, I was just going to say something so I don't forget, but I, I would imagine there's like kind of like two modes just for us to think about, like one mode is your pipeline production mode, what you're checking, you're going through, and it's going to be a lot less exploratory, right?

**Marcel Santilli:** And then, so that's one mode for, and then the next mode is kind of like more like playground or so off, I need to rethink the whole thing, playground mode, you know?

**Marcel Santilli:** And so our editors are mostly like in one of those two modes.

**Brad Herman:** It's either like, I need to tweak something.

**Marcel Santilli:** Right?

**Marcel Santilli:** Like, kind of like what you showed first, and I think we're solving it.

**Daniel Lopes:** We can probably take that offline, because I think we're almost out of time, and I have another 10 minutes more.

**Marcel Santilli:** sounds good.

**Brad Herman:** But, yeah, that makes sense.

**Brad Herman:** But, yeah, we're definitely thinking about that, Marcel, and we can go into details, you know, like you said, offline, but that's kind of one of the things that, like, Kirkland and I are going to talk about is, like, how we improve, like, the prompting, and, you know, there's been some talk about if you're working on an output, for instance, like, should we actually surface the entire pipeline details and all of the data that is across the pipeline into the context?

**Brad Herman:** Like, potentially, not sure, you know, so there's a lot of improvements that we can make here, and we'll continue to, like, iterate on this and try to get, you know, better and better results out of the tooling.

**Daniel Lopes:** And then, you know, we can talk about knowledge base.

**Daniel Lopes:** Yeah, we'll, like, we'll have, like, a break album, like, a shaping and discussion thing around this feature next week, because, like, just general, like, editing with AI is just such a core thing that you're doing that.

**Daniel Lopes:** So next week, it'll be a big thing.

**Daniel Lopes:** Yep.

**Daniel Lopes:** It's just like, it just doesn't make sense how fast Brad moves.

**Brad Herman:** So, like, things like that.

**Daniel Lopes:** send him a draft like a day before, and then it works.

**Daniel Lopes:** And it's been like this for the past couple of months.

**Daniel Lopes:** It's always amazing.

**Daniel Lopes:** Trying to justify my salary if I can.

**Brad Herman:** And hopefully we turn this into a multi-billion dollar company.

**Matthew Panzarino:** Yeah, I mean, just advocating from my end for a demo, once you, like, are in a state where you're like, hey, I think I've collated this into a nice package of updates, we need to demo this for the delivery team.

**Matthew Panzarino:** Because I think most of them are not using this right.

**Brad Herman:** Like, not right.

**Matthew Panzarino:** Like, they're not using it as much as they could.

**Brad Herman:** Because they don't know what it's capable of.

**Matthew Panzarino:** And now you've obviously just added some new features.

**Brad Herman:** So I think it for them would be lovely.

**Brad Herman:** Yeah, yeah, definitely.

**Brad Herman:** I would love to do that.

**Brad Herman:** And, like, so once we get this, like, AI assistant stuff kicked off, and then, like, Kirkland and I, you know, ping around some ideas to kind of make these.

**Brad Herman:** The output's a little more reliable and higher quality.

**Brad Herman:** I think we'll be in a good place to do that.

**Matthew Panzarino:** Yeah, and the right rail, mean, that would be amazing.

**Matthew Panzarino:** Because the popover, honestly, makes it, it's like a presentation thing.

**Matthew Panzarino:** It makes it seem like an aside or like a little tool tip.

**Matthew Panzarino:** Maybe you should use it, maybe not.

**Matthew Panzarino:** It just feels a little bit more lightweight than it actually is because it's a popover.

**Brad Herman:** The reason that we did the popover just for now, for context, is that originally we did have like this full right rail, you know, version of it.

**Brad Herman:** And it was hard to, you know, in a demo like this on this output, right, where you have like multiple output fields of a pipeline step, you theoretically could have like five documents all within the output.

**Brad Herman:** And when you start talking to it and it's just in the right rail, like managing the context of, oh, no, I'm actually talking about document two and surfacing those changes to that document and pulling the context.

**Brad Herman:** From that specific document.

**Brad Herman:** Whereas with the pop-up now, as you'll see here, like you can actually like start one and you see you're working on like this, you know, document D is just a test.

**Brad Herman:** And then you have this one markdown brief as well.

**Brad Herman:** So now I've got multiple, you know, I've got multiple, oh, they're overlapping actually, but I've got multiple versions of it now.

**Brad Herman:** So I can have several conversations going on about different documents.

**Brad Herman:** So just kind of need to figure out how we manage that context and knowing which document we're actually talking about in the event that you have multiple documents on a page.

**Daniel Lopes:** To me, this is the perfect example of like, perfect is the enemy of good here and engineering complexity in our setting, year one should drive prioritization.

**Daniel Lopes:** So like, it would be great to have a sidebar.

**Daniel Lopes:** When we got to the sidebar during the launch, like, this is another problem.

**Daniel Lopes:** This is going to be a rabbit hole in itself.

**Daniel Lopes:** Let's  with this for now.

**Daniel Lopes:** And then we'll figure.

**Daniel Lopes:** After the right UI and everything, but if we were shipping a self-service product, we'd have to figure that out before, but we'll figure that out as we go.

**Daniel Lopes:** Yeah, so like another one that I want to share, thanks for all the stuff you've done, Brad, it's super amazing.

**Daniel Lopes:** Yeah, so just to recap some of the stuff we were talking about also yesterday on Cycle.

**Daniel Lopes:** So for us, making that editor really work, even if not everybody's using, if somebody that knows how that works can use that, let's say Daryl next week is the one running an experiment, or Pander, knows how that works, and that is actually working well end-to-end, we can put more energy into making that look better and all that.

**Daniel Lopes:** So we don't have the whole, we don't need to immediately the whole work to use it, it's just like the people that actually understand the business end-to-end, yeah, super fast, and that, that is the short-term cycle feedback that I.

**Daniel Lopes:** Need for us to like say, yep, that's the direction, you know, so, and then one thing that I wanted to show is something that we've been toying with, we're a little late, so it's going to be 10 minutes more, think, GP had like 12 minutes in looms recorded, and I'm just going to speed through like all the parts of the past here, just to be respectful of your time, but we've been trying to figure out images for a while.

**Daniel Lopes:** So, have two main workflows now, one will convert HTML templates into images, and another one that relies heavily on, it's like on top of a GPT image will create images from scratch, and we're essentially removing recraft, because GPT image replaces recraft if you know how to use it, but it's super hard to use it, so not a lot of people realize that this can be done.

**Daniel Lopes:** So, we now have a workflow called GPT images, you can see that in the studio, and let me go up super fast here.

**Daniel Lopes:** And what it does is come up with a bunch of image ideas, select the best one, and generate the images.

**Daniel Lopes:** But what happens behind this, let's see what happened here today.

**Daniel Lopes:** Let's see if the quality is good.

**Daniel Lopes:** So in this case, the input is the whole article, the size you want, and we have an art direction.

**Daniel Lopes:** So this is for firework.

**Daniel Lopes:** So in this case, you're generating something that's a mix of illustration and stock image.

**Daniel Lopes:** Sometimes, so like we have like the photo should be ultra-realistic, stock photo style, HDR.

**Daniel Lopes:** So this is kind of hard to write still, like you need to understand how to write this.

**Daniel Lopes:** But so like designers, or like junkier, or some people, like they can do this much better than an engineer.

**Daniel Lopes:** But so we need to be able to fill out how it should look like a little bit, but we also can provide a bunch of reference images.

**Daniel Lopes:** So the reference images are, like, this is one, and another one.

**Daniel Lopes:** So this came from Firework blog, and this is another one.

**Daniel Lopes:** So you see one is kind of gray with, like, a person on top and has UI things on it.

**Daniel Lopes:** And then in this case, the output will be something, let's see.

**Daniel Lopes:** There's one, another one, another one, another one.

**Daniel Lopes:** So it's not going to be all gray, so we're going to render a bunch in that, the, the, the, team select in the, in the, outputs.

**Daniel Lopes:** But, so this is the image generation one.

**Daniel Lopes:** It does really well for different kinds of, like, reference images.

**Daniel Lopes:** And, so that's available.

**Daniel Lopes:** Another thing that, Jean-Pierre was working on, is this.

**Daniel Lopes:** Let me check off my sharing here, and I will switch to his.

**Daniel Lopes:** Deck, one sec.

**Daniel Lopes:** So he built an HTML templating engine.

**Daniel Lopes:** So we have here two loans.

**Daniel Lopes:** One I will put in 1.5.

**Daniel Lopes:** Let me see if I stop my sharing.

**Daniel Lopes:** One sec, one more, because I think I need to enable the audio for that.

**Daniel Lopes:** So share, share sound.

**Daniel Lopes:** One sec.

**Daniel Lopes:** I don't know if you can hear him when I play the sound.

**Daniel Lopes:** He is doing okay.

**Daniel Lopes:** I definitely am, and so is my wife.

**Daniel Lopes:** So first of all, I wanted to thank everybody for your thoughts and for reaching out and checking in.

**Daniel Lopes:** We're doing well, and yeah, I'm just looking forward to being back full-time, working with you all.

**Daniel Lopes:** As part of it, though, I think, unfortunately, I won't be able to join the whole hands tomorrow morning, so I wanted to record a loom to show a little bit of the work that we've been doing with HTML templates.

**Daniel Lopes:** So I started with Airbyte because I think it was a good example, but I think the same now can be applied to pretty much any client.

**Daniel Lopes:** So here on Figma, you can see that these are essentially their guidelines for any sort of marketing material or content that they want to put out.

**Daniel Lopes:** They have very specific guidelines, you know, in terms of having like a particular grid in two different or actually even three different color schemes.

**Daniel Lopes:** Some of them are text only.

**Daniel Lopes:** Some of them have an error image.

**Daniel Lopes:** Some of them come with illustrations.

**Daniel Lopes:** You can see there are different patterns.

**Daniel Lopes:** And what I will show you, though, is also that rather than sort of blindly going and trying to replicate every single possible template, we try to kind of be a little bit smart and create some templates that have flexibility in terms of like working with variables to have a little bit of variance in terms of like color scheme, layout, etc., and grouping them where it makes sense.

**Daniel Lopes:** So it won't be like 100% coverage, but think it's to be enough for our client teams to be able to produce enough.

**Daniel Lopes:** Content.

**Daniel Lopes:** To give an example, but again, I'm going to go into HTML and CSS in a bit.

**Daniel Lopes:** You can see that like these six here, they can be kind of the same template.

**Daniel Lopes:** Like this could be the same between left and right, just within your image.

**Daniel Lopes:** that just requires like a re-layouting a little bit the title.

**Daniel Lopes:** Same goes with the color scheme in between here.

**Daniel Lopes:** It can be like three variants between like white, this light blue, and this dark blue.

**Daniel Lopes:** And so essentially what you will see is that for these six templates, we kind of have like one HTML template in CSS with a bunch of variables that will allow the LLM to sort of kind of produce a combination of the three.

**Daniel Lopes:** And same goes here.

**Daniel Lopes:** Like the other one that I wanted to try was like those from before they were with images.

**Daniel Lopes:** This instead is just text, but with different combinations, like in terms of like whether it's aligned left or like centered.

**Daniel Lopes:** And also you can see that the sort of highlight if you want, or whatever you want to call it, the text in different color comes in a slightly different tone of blue.

**Daniel Lopes:** The logo is kind of the same, but can be centered or left and that kind of affects the illustration.

**Daniel Lopes:** So once again, like this can be like one HTML and CSS template with sort of like a few

**Daniel Lopes:** A few variables to play around with.

**Daniel Lopes:** So with that in mind, I think what we worked on as kind of two parts, like the important one is the workflow, I'm going to get to there in a second.

**Daniel Lopes:** But also, before talking to Daniel, I kind of went a little bit the extra mile, or maybe I should say clogged, went the extra mile for the most part, and sort of added support for HTML templates into the artifacts.

**Daniel Lopes:** So you can see here that now in Atlas, we got an HTML template for, oh, well, the color scheme is weird, maybe because I'm looking at, because I'm in dark mode, we'll fix that.

**Daniel Lopes:** But anyway, essentially an artifact has like the HTML and CSS code here, that's really all there is, but there's a nice little preview that kind of shows what this template is, a list in the variants that you put here.

**Daniel Lopes:** So that can help, I guess, like us or clients selecting which one is the right template for us.

**Daniel Lopes:** And then, I mean, if you edit, it's it's not the same as we have in all other context artifacts, so variable name, maybe the only one here, like we need to specify a canvas size, because that's sort of like what, that's what kind of allows us to render the preview the way that we saw before.

**Daniel Lopes:** And yes, I think I'm also running out of time with Loom.

**Daniel Lopes:** So I'm going to kind of pause here for this one.

**Daniel Lopes:** And then he would show the workflow.

**Daniel Lopes:** ...presses the HTML, converts to PNG, and saves it.

**Daniel Lopes:** In terms of the input and output, nothing too similar from what we have on a lot of other workflows, we have the HTML template itself, which we're going to go through in a second to see an example of it.

**Daniel Lopes:** We're going to get the article content, the variations, the namespace, optional out-of-direction, and then hero images.

**Daniel Lopes:** The hero images are given as an input because I don't think the workflow should try to do too much.

**Daniel Lopes:** We have other workflows that are a lot better at generating illustration or photography type of images, so we should generate them in a different step of the pipeline and pass them into this workflow as needed.

**Daniel Lopes:** And then the output schema will have just an array of images.

**Daniel Lopes:** And the hero images are optional, so if your past and the template supports it, then great, otherwise they're just not going to get used.

**Daniel Lopes:** ...

**Daniel Lopes:** And in terms of the HTML template itself, like, I committed two to the repo, both for error bytes, but one is an example with a hero image and one without the hero image.

**Daniel Lopes:** The important part is that it contains a section with template instructions, and if you go look at the prompts, you will see that the LM actually looks for this, so that it understands, like, what variants can play with, what variables can play with, and so forth.

**Daniel Lopes:** And then, even, like, other constraints that you might put in, like, you know, if there's no hero image, like, the title is max of any characters, because, like, it might shift the layout and cannot be too long or whatnot.

**Daniel Lopes:** Other than that, it's a regular sort of, you know, HTML page with CSS, and, yeah, just, like, once again, variants of, sorry, variables in terms of the variant in terms of the hero image, if they want to insert one or not.

**Daniel Lopes:** And I work with Yusef to sort of, like, create some spaces in our AWS storage so that some assets are going to be statically accessed, like, for example, the logo doesn't have to be generated dynamically, it's always there, and so it can be just part of the template.

**Daniel Lopes:** So let me copy this entire thing, and let's just try and run one workflow.

**Daniel Lopes:** So, HTML inputs goes here, the article, I got it saved here, so I can put it there, variations, let's just leave the same, growthx is namespace, and let's just do a text only just for the sake of trying this.

**Daniel Lopes:** So, we'll see if I can make it within the time of the second loom, hopefully it's quick enough.

**Daniel Lopes:** But yeah, it's analyzing the template, so in a bit you should start like processing whatever many, however many variations it decided it wants to do.

**Daniel Lopes:** I got a minute and 50 seconds left, so I think that you can do, let me move myself, okay, saving it, let me wait until it's done.

**Daniel Lopes:** And so, if we go to the output, we got the five variations that we requested, and you can see that they're sort of like variations of, like, those different HTML templates that we saw in different combinations of.

**Daniel Lopes:** Color scheme, title, set title, and colors.

**Daniel Lopes:** That's all there is to it.

**Daniel Lopes:** I think now we can just produce more HTML templates and just try it out on other clients.

**Daniel Lopes:** Everything is committed to my branches.

**Daniel Lopes:** Unfortunately, I was planning to merge them as soon as someone reviewed them, like, first thing on Monday.

**Daniel Lopes:** Obviously, that didn't happen, and now we have some conflicts, but hopefully they can be so quickly.

**Daniel Lopes:** Well, thank you for...

**Daniel Lopes:** Awesome.

**Daniel Lopes:** This has been a challenge for a while, so maybe, like, since you...

**Daniel Lopes:** I was the one working on this, like, his solution for this was pretty  awesome, and it works great with a lot of the harder things.

**Daniel Lopes:** But, yeah, thanks, everybody.

**Daniel Lopes:** This was our first...

**Daniel Lopes:** First all, hands.

**Daniel Lopes:** I hope you had a good time, and if you have any comments or feedback afterwards, let me know.

**Daniel Lopes:** And, yeah, looking forward to our one-on-ones and to next week.

**Daniel Lopes:** See you, everyone.

**Daniel Lopes:** Bye.

**Daniel Lopes:** See ya.

**Daniel Lopes:** ya.
