# Lovable Templates Check-In

<metadata>
date: 2026-01-05
time: 21:30 UTC
duration: 35 minutes
organizer: megan@growthx.ai
participants:
  - name: George Haikal
    role: Co-founder
    affiliation: GrowthX
    email: george@growthx.ai
  - name: Georgemaine Lourens
    role: Design & Operations
    affiliation: GrowthX
    email: georgemaine@growthx.ai
  - name: Nicolas Castellanos
    role: Engineering
    affiliation: GrowthX
    email: nicolas.castellanos@growthx.ai
  - name: Megan Dickey
    role: Client Manager
    affiliation: GrowthX
    email: megan@growthx.ai
fathom_recording_id: 111909458
fathom_url: https://fathom.video/calls/520700708
share_url: https://fathom.video/share/X_Fg1sxTJw5B7YV98ePEkEJeCNiee8Vf
source: fathom
enriched_on: 2026-02-28 14:23 UTC
</metadata>

---

## Summary

Team aligned on scaling Lovable template production by hiring 1–2 contractors to double website template output to 10/week. Georgemaine will research and document the "Tools" template workflow for Nicolas to automate. Critical conversion bug identified: logged-out users cannot remix templates—Megan escalating to Lovable for immediate fix.

---

## Context

GrowthX is delivering content marketing and template services to Lovable, a low-code web and tool builder platform. December performance exceeded expectations: 150 signups from templates and guides generated approximately $37.5k in value at Lovable's $250 customer lifetime value—more than covering the $25k monthly contract. The client is highly bought-in and pushing for increased production to capitalize on the momentum.

The core constraint blocking scale is Georgemaine's review cycle (45–60 minutes per template), not contractor quality. Bruno, the current contractor, is consistent and responsive but defaults to minimalist design (black-and-white bento grids). The team has approved hiring 1–2 additional contractors to hit 10 website templates per week while Georgemaine and Nicolas develop a repeatable workflow for more complex "Tools" templates (PDF generators, calculators, databases). This parallel approach allows immediate revenue impact without sacrificing product innovation.

---

## Relevance

**Strategic Opportunity**
- December's $37.5k in value driven from GrowthX content validates template production as a high-ROI lever
- Client is actively seeking expansion; timing allows GrowthX to increase contract value while building new service lines

**Operational Execution**
- Contractor ramp is straightforward (previous hire took ~1 week)
- Georgemaine's research phase is the critical path item for unlocking more complex template types

**Risk & Dependencies**
- "Remix" bug is creating silent conversion losses—requires Lovable engineering fix
- Staging environment is down, blocking design review with Sebastian
- Tools workflow definition relies on Georgemaine's platform research, which Nicolas then automates

---

## Overview

- **Strong ROI justifies scaling:** December's 150 signups (from templates/guides) generated ~$37.5k in value (at Lovable's $250 LTV), exceeding our ~$25k contract.
- **Immediate ramp-up approved:** We will hire 1–2 new contractors to double website template production to 10/week, leveraging the current successful strategy.
- **New "Tools" template workflow is the next priority:** Georgemaine will research the Lovable platform to define the process for building more complex templates, which Nicolas will then automate.
- **Critical conversion bug identified:** Logged-out users cannot "remix" templates, causing significant lost signups. Megan will escalate this to Lovable for an immediate fix.

---

## Key Topics

### Performance & Opportunity

  - December performance validates scaling:
      - **Impressions:** 1.8M
      - **Signups:** 150
      - **Value Generated:** ~$37.5k (at Lovable's $250 LTV)
  - The client is highly engaged and eager to expand, creating a clear opportunity to increase production and contract value.

### Website Template Production

  - **Current Bottleneck:** Georgemaine's review time (45–60 min/template) is the primary constraint on scaling.
  - **Contractor Feedback:** The current contractor, Bruno, is consistent but needs design guidance to move beyond a minimalist style.
  - **Decision:** Hire 1–2 new contractors to double production to 10 website templates/week.
      - **Rationale:** This leverages a proven strategy for immediate impact while the "Tools" workflow is developed.
      - **Contingency:** Georgemaine will create 5 templates next week if new hires are not ready.

### "Tools" Template Workflow

  - **Goal:** Create a repeatable workflow for building more complex templates (e.g., PDF generators, calculators).
  - **Status:** The core technology is functional, but a defined, automatable workflow is still needed.
  - **Research Plan:** Georgemaine will test the Lovable platform to understand its capabilities and limitations.
      - **Objective:** Identify the specific steps and prompts required to build a tool, which will inform the automation design.
      - **Output:** A detailed research report for Nicolas.

### Technical & Product Development

  - **"Remix" Bug:** Logged-out users cannot remix templates → they are redirected to the homepage, causing lost conversions.
      - **Action:** Megan will escalate this to Lovable for an immediate fix.
  - **Automated Publishing:** Nicolas will create a PR to automate the guide publishing process, which Lovable has not yet implemented.
  - **New Template Page Design:** Georgemaine's new design for Sebastian is ready for review.
      - **Blocker:** The staging site is down.
      - **Dependency:** The interactive demo requires access to Lovable's internal LLM to generate functionality prompts.
  - **Future Idea: Component Library:** George proposed a component library (e.g., Framer-style sections) to make building more visual and intuitive, reducing reliance on text prompts.

---

## Action Items

**Georgemaine Lourens** (GrowthX)
- Review contractor templates; compile recurring feedback for automation
- Draft tools/apps workflow in Lovable; share with Nicolas; then pair to refine
- Fix staging deployment for template page design

**Megan Dickey** (GrowthX)
- Email Lovable re: logged-out remix bug; request fix
- Start Deals Desk thread re: pricing for 10 templates/week ramp-up

**George Haikal** (GrowthX)
- Reactivate Marilia chat; add Megan; source 1+ website template contractors

**Unassigned**
- Tag 2 guides/day in Airtable; Nicolas PRs; no Lovable review

**Nicolas Castellanos** (GrowthX)
- Send PR to Lovable re: automated publishing workflow

---

## Transcript

**Megan Dickey:** Back-to-back of the day, which is nice.

**Nicolas:** Hey, how's it going?

**Megan Dickey:** How you doing?

**George Haikal:** Good to see you.

**George Haikal:** It's been a while, Nico.

**Nicolas:** Yeah.

**Nicolas:** How were your holidays?

**George Haikal:** It was good. I was home for a week and then in Costa Rica for a week, so it was a good, relaxing, fun time.

**Nicolas:** Nice.

**George Haikal:** Yep, yep.

**George Haikal:** What about you?

**Nicolas:** Spend time with family and yeah, that was it. Just relax.

**Megan Dickey:** Yeah, about me.

**George Haikal:** Amazing.

**George Haikal:** Let me see.

**George Haikal:** Looks like Georgemaine accepted the invite, so he should be joining soon.

**George Haikal:** But Nico, we had a call with Lovable earlier today, all really good things. I basically backed into the math. They gave us an LTV number, so like the value of a signup for them. In December, if we're looking at December, between templates and guides, we've had 150 signups. And so if you do the math on their $250 LTV number, it's already creating like $37,000 in value for them, which is over and above our contract value, more than $10,000. So it seems, and Megan, correct me if I'm wrong, it seems like they're super bought in and excited to expand, both in editorial, but especially in templates, which is what we're going to cover today. But all good things, for sure.

**Nicolas:** Cool. That's great.

**George Haikal:** Hey, Georgemaine.

**Georgemaine Lourens:** Happy New Year, everyone.

**Megan Dickey:** Hey, happy New Year to you, too.

**Georgemaine Lourens:** Happy New Year.

**George Haikal:** Not much. Basically, we just had a great call with Lovable earlier today. The progress is amazing. They're super bought in, and we want to propose even more, especially on the templates side. And so there's a few routes that we could go, but I was curious as to one, the progress thus far on the contractor and how his output is and how confident you are in scaling up the existing portfolio website template work. And then, secondly, I think it sits with Nico, but it's the workflow for apps and tools.

**Georgemaine Lourens:** Cool. I can go first. Well, the contractor is super consistent, like, he's hitting all of his deadlines. I do think that he does need feedback to kind of iterate once or twice, but he seems super into it and he delivers all of his iterations within a day or so. But I'm not sure if we want to increase the production times two, then I would rather say, like, maybe it makes more sense to add another contractor instead of using the same one, because it's just going to be too much for him. He has a full-time job and a family on the side as well. And, but I do think that, yeah, we would have to see how that goes in terms of giving feedback, because it also takes quite a bit of time on my end to kind of go through all of it, give feedback, and do all of that stuff. But I think, like, if we get a lot of cash out of it, then it's definitely worth it.

**George Haikal:** How long is it taking you right now per template to review his work?

**Georgemaine Lourens:** I think my review just now took like 45 minutes to an hour.

**George Haikal:** Yeah, that's too long because how long does it take for you to do them yourself?

**Georgemaine Lourens:** To create them, I don't even remember. I think like maybe two times that or like five of them.

**Nicolas:** Is there any of that feedback like repetitive across templates? Like something we can kind of automate?

**Georgemaine Lourens:** Probably. I'll just have to go back and see, but I think, yeah, maybe we can help them out with that, I guess. I haven't looked at it from that angle yet, but we could maybe.

**Nicolas:** Yeah, I was thinking building something that can look at the page and come up with feedback.

**Georgemaine Lourens:** Yeah, I think the biggest part where he's kind of struggling is the graphic design part, because he can come up with cool interactions and simple layout, but then it's always the same minimalistic, Vercel, black and white, bento grid design. I think that's kind of like, after you had like six of them, then you've seen them. Like how many bento grids can you make, and how many black and white ones can you make. But maybe there is a way that we can automate the generation of themes. Maybe that is something that could help.

**George Haikal:** Yep. Okay.

**Georgemaine Lourens:** Interesting.

**Nicolas:** Yeah. On tools, I haven't made much progress. The thing works, it can build them, but I'm, yeah, I'm far away from getting a workflow. So, uh, I was thinking maybe early next week I can have something. But yeah, right now I haven't made much progress on it.

**George Haikal:** Is it more complex than we were thinking?

**Nicolas:** No, not really. No, it's just telling what to do. And then again, yeah, design. Because it needs some design. And in this case, might have like it's stuff that it's kind of like more straightforward to do because probably lists and actions and those kind of things. But no, it's not harder. I mean, probably like the design, it's harder than functionality with this.

**George Haikal:** Go ahead.

**Georgemaine Lourens:** I'll go. Is there something that I can do to help out here? Like, would it help if we pair on this maybe for like half a day or a couple of hours?

**Nicolas:** Yeah. Yeah. Yeah, I mean, if you want to go and try, like, Lovable and see what's the limit, basically, that's basically what I'm doing now.

**Georgemaine Lourens:** Do you mean by limits?

**Nicolas:** Yeah, seeing, like, what you can accomplish and how when you talk to it. That way, we build the tool in a way that can, like, walk Lovable through what you want to build. Make sense?

**Georgemaine Lourens:** Let me see if I understand. So as in, just try out and kind of, like, talk to Lovable in the chat and see if I can come up with my own tools and then share that with you for research?

**Nicolas:** Yeah, exactly.

**Georgemaine Lourens:** Okay.

**George Haikal:** It sounds like basically try to do one full wrap, like the same way you did with the portfolio website, maybe using an example as a starting point and then getting it to gray and then seeing, like, what that actually took and then what from that process could be automated or pulled into steps and instructions, right?

**Nicolas:** Yeah. Yeah, I think the key is being able to separate features in a way that Lovable can execute them. That's all.

**George Haikal:** Okay. Okay. Because, yeah, on our end and with the client, right, we want to be able to present something that we're confident we can deliver on in terms of an increase of at least to 10 templates per week. And so before I propose, before we propose increasing to 10 templates, just want to make sure we understand and have a repeatable process for like how much time is taking you all and then how many other people we need to hire for it. But my inclination, and so with that, right, if it's just 10 templates per week executing against our website strategy, that's fine. But like where the real room for growth is, are building out these other catalogs, like this tool, this database of different tools, right? And then we can move on from there to like other use cases for the marketplace that may be a little more complex. But the reason I think we should start with tools is because from what you all are saying, it's an easier starting point to actually develop and build these templates and build them same quality, same great quality, but just higher volume weekly. And so I'm trying to save more of your time eventually from 10 portfolio websites to a number of those plus more of the tools once we get that workflow working.

**Georgemaine Lourens:** Yeah, I think that makes sense. If what is worth, I think that's the better route to go. So I'll give it a shot, Nicolas, and I'll share what I got with you and then hopefully you can learn from it and maybe we can sit together and kind of pick the part to see how far we can get.

**George Haikal:** Amazing. And then one thing, before you joined the call, I was just telling them it's, like, insanely exciting. We went through the numbers today that Megan put together. In December alone, there's 1.8 million eyeballs on the templates. So it's insane. And, like, anything we want to do and test will be an amazing use case. But in December alone, templates and guides, already down to purchase, which is conversion, which is someone paying. There was 150 purchases, 150 people paid coming from a piece of content that we created. When we assigned the $250 lifetime value to that, which is what they have for a customer, that's already $38,000 in value that we created for them in a month. Over and above, they're paying us $25,000. So with the upsell, it'll be $35,000 to $40,000. So, like, we're in a really great spot to even push more and basically build out, like, the foundation for their entire marketplace. So we don't have to sacrifice increasing production until then. They do it right. And like the amount of feedback we're getting is instant. It's like where it's millions per month, right? And so where there's definitely an opportunity to pour more headcount resources into it too. Just want to make sure the structure is set up correctly for that, but then we can hire as many contractors as we need, right?

**Megan Dickey:** Yeah. Oh, yeah.

**Nicolas:** No, go on. Sorry, Megan.

**Nicolas:** On that, and I think it's related, George, did you talk to Sebastian about the thing we found, I think it was last week?

**Georgemaine Lourens:** I sent him a DM because I didn't want to alarm everyone in kind of like the external chat, but he didn't respond. And while we were talking, I was actually checking if the bug is still there. It's not. So I think they fixed it.

**Nicolas:** Oh, cool. That's great.

**Georgemaine Lourens:** Are you able to reproduce it?

**Nicolas:** I haven't tried, let me check.

**Georgemaine Lourens:** But I can't reproduce it anymore, so let's verify.

**Nicolas:** The problem was that you couldn't remix if you were logged out. Like the moment you try to remix, it will take you to the homepage without paying attention to the template.

**George Haikal:** And now it works, let's see.

**Nicolas:** Checking. No, it doesn't.

**Georgemaine Lourens:** It works when you're logged in, but...

**Nicolas:** Yeah, but it doesn't when you're logged out. And I think that's a problem.

**Georgemaine Lourens:** Yeah, it doesn't work when you're logged out. Yeah, that is still a problem, yes. Because it should reroute you to either logging in or something else.

**Nicolas:** Yeah, I mean, from my view, it should prompt you to register or log in and then get you back to the template.

**Georgemaine Lourens:** Well, I mean, this is lost conversion, right?

**Nicolas:** Yeah.

**Georgemaine Lourens:** Like if anyone clicks here, then they can't do anything. And that's it. That's not good.

**George Haikal:** No, it's not. Is that all written somewhere? Are they already aware of it? Or should we push to the front for them?

**Georgemaine Lourens:** Or should we push it to the front for them?

**Nicolas:** No, we can only push it. Yeah.

**Georgemaine Lourens:** If you want to push it, then go for it. Because I'm not good with external communication. Like I was raised to flag and sound the alarm. Like, yo, fix this straight away. No worries.

**George Haikal:** I don't want to step on your toes, Megan. So up to you, like, if you want to send it, totally fine with that. I'm happy to shoot it over too. But I know how it's weird with multiple cooks in the kitchen. So I don't want to step on your toes.

**Megan Dickey:** Yeah, no, no, you can go on ahead. That's all good.

**Georgemaine Lourens:** It's good if you do it, because you're kind of like the new face of the team.

**Megan Dickey:** Yeah, yeah, for sure. Okay, cool. That sounds good. Something I, yeah, like, so I definitely understand that there are a lot of moving parts and, like, still some uncertainty. Um, but my sense is that Sam, the, like, our main stakeholder now at Lovable is just wanting, like, a general timeline or, like, sense of when we can actually do this ramp up. And, like, I think, and my sense is that, like, obviously, like, the faster, the better, but that he's not necessarily, like, this needs to happen, like, tomorrow, but just, like, wants to be able to plan for it. Um, and I would like to get, be able to give him, like, some sort of estimate, but it's, I mean, I guess based on what I'm hearing, and, like, I obviously, I don't know how long things take from an engineering standpoint, so, like, I just, I just have no idea. But, like, I guess, are you, are we thinking maybe like a month out, two months out, or just even like a loose timeline, just so we can try to like manage those expectations.

**George Haikal:** I mean, if we hire another contractor in a week, correct me if I'm wrong, Georgemaine, if we have two contractors, we could do it next week. Like it's just depending on when we hire another contractor, if we're staying with websites, correct?

**Georgemaine Lourens:** Yeah. Yeah, the way that I'm looking at it is like, if it's urgent, then we could do either we could hire another contractor and then I review his work and then push it until it's done. And then we have like 10 until Nicolas gets to a point where he's comfortable. Or I could just jump in and do an additional five as well until we get to the point where Nicolas is comfortable. Another route could be, instead of kind of like estimating, we could just be transparent about the process and just kind of put some milestones. And then we can obviously push them or change them along the way. I feel like maybe transparency is the best way to go here because we're kind of like trying to figure out something that hasn't been done before, right? So maybe we just take them along for the ride and just kind of like show demos. I mean, that's one of Marcel's main principles, right? Kind of like show early and show often. And maybe that's also another route that we could take and then just kind of update them on the progress and show them what we have. Those are kind of like the three things that I can come up with. But it all depends on how you want to do this. What would work best for you? Because you're in those meetings speaking to them. So you need to be comfortable to kind of like meet their requirements.

**Megan Dickey:** Yeah. Yeah, like I'm kind of leaning toward like hiring another one or two more contractors and just focusing on websites. And then in the meantime, like kind of doing essentially both of your approaches, Georgemaine, of like doing like the contractor idea. But then also in the meantime, we're still fine tuning the tools and the apps workflows. And like we can also be sort of like demoing to them like as we're moving along. Like, OK, like here's where we're at right now. Like we're still thinking about this. But then we're still ultimately producing more templates because I think they're, yeah, I think they still they want to capitalize on any type of template sooner than later. And I feel like they maybe care less about like the type, but just like templates are working. Let's do more templates.

**Georgemaine Lourens:** OK. What do you think, George?

**George Haikal:** Yeah, no, I completely agree. Like right now, if we try to hire for another one or two contractors in the time that's going to take the vet and hire them, we can still make progress on the tool workflow, right? And we can take Lovable along for the ride. They're not really in a rush. We're more so the ones pressing on we want to do more as well. So it's like a mutual thing versus them pushing and us not being able to. So I think at the very least, we get a couple of contractors in and we can hit 10 templates at the website, in the website category. And then, you know, we'll be ready for the tools in two to three weeks. So we don't have to sacrifice increasing production until then.

**Georgemaine Lourens:** Okay. All right.

**George Haikal:** Let's do it then. For that to happen, Georgemaine, let me reactivate that chat with Marilia to source one more. You probably have feedback on, you know, what made Bruno good. And so, like, that's probably helpful for her when she's vetting others moving forward.

**Georgemaine Lourens:** Yeah, I think that's fine. If you can give the okay, if you can reactivate it with her, then I can just take the process.

**George Haikal:** Megan, I'm adding you to this chat.

**Megan Dickey:** Okay, great. Perfect. Yeah. So then in that case, like, yeah, I guess we could plan even just for like the next couple of weeks and the next couple of weeks to start doing maybe 10 templates, 10 website templates a week, assuming that if you think it's reasonable, we could actually bring someone on within the next two weeks.

**Georgemaine Lourens:** Should be reasonable, probably. Right?

**George Haikal:** Yeah. Yep. For sure. I mean, it took less than, it took about a week to get Bruno, right? Start to finish.

**Georgemaine Lourens:** Yeah, I think so. And worst case scenario, I can jump in for the upcoming week and just make five as well. Um, but speaking of templates, um, is Will on...

**Megan Dickey:** Yes, so Will's on vacation. Jenny, I tagged her in your thread. Yeah, Jenny is hovering for Will while he's out, and Will's out all of this week and then through Tuesday of next week.

**Georgemaine Lourens:** Okay. Yeah, maybe it makes sense to stick on the portfolio keyword then instead of trying to find a new one. It's one of the biggest anyway, so whichever way you try to chip away at it, it's always going to be good, I guess.

**Megan Dickey:** Yeah, for sure. Yeah, for sure. Yeah, I think we can try and keep it as like simple for Jenny as possible, and then we can kind of expand upon things when Will is back. Also, on the topic of, yeah, we are doing the ramp up for Lovable this week with the guides, and yeah. Nico, are you responsible for filing the PRs for every batch? Okay. So, and then, are you aware that we're giving, like, two a day this week?

**Nicolas:** Or is this, like, the first time? No, I didn't know. I usually push them on Wednesdays. That's, I think, they were getting them ready on Monday and leaving a couple days for the Lovable team to review them. And then we push them that Wednesday. So, yeah, essentially pushing five each Wednesday.

**Megan Dickey:** Okay. Yeah, because at this point, we're looking to do two a day, but, like, without that review layer. And so, with that, should Jenny tag in an Airtable, like, ready to publish? And then are you able to just sort of, like...

**Megan Dickey:** Yeah. Do those PRs, like, for two a day?

**Nicolas:** Yeah. Yeah, can do that.

**Megan Dickey:** Okay. Nicolas: Did we get any update on the automation for publishing?

**George Haikal:** Who needs to do it? Does it sit with them or us?

**Nicolas:** They said they were going to do it, but they haven't.

**George Haikal:** We can reactivate that. It's basically the automating publishing on their end of it.

**Nicolas:** I can also spend a couple hours and just push it as a PR and see what we get.

**George Haikal:** Cool.

**Georgemaine Lourens:** Okay.

**George Haikal:** Excuse me.

**George Haikal:** You. Bless you.

**Megan Dickey:** Yeah, what, specifically, what do we need from Lovable to make this automatic publishing a thing?

**Nicolas:** Just so I can... I mean, it's just some workflows in their GitHub organization, but that's all. I mean, that's... They just said they wanted to do it, so, yeah. But I can spend a couple hours sending us a PR and see if we can get it merged.

**Megan Dickey:** Okay, cool. Sweet. Thank you. Okay. That all sounds good.

**George Haikal:** Yeah, it sounds great. Let me see here. Pull up one more thing. Just to show you all, because it's exciting. Look, in November and December, so two months, sorry. I only said December. This is the problem. Progress, which is insane. Almost 3 million impressions, 11,000 clicks, 160. It's insane. Yeah. I mean, this is a lot of it's carried because of their name and their brand, but still, like, it's an amazing, like, we're capitalizing in a really great way. And it's only at five per week of each. So that's why pouring gas on it now, I think we're going to pay dividends. And what an amazing case study this can be, too. Like, this company raised $3 million. We took them from no visibility to, you know, X and driving. We're already driving $40,000 a month for them in signups. And this is month three, basically.

**Megan Dickey:** Yeah.

**George Haikal:** Same.

**Georgemaine Lourens:** Yeah, I know. I'm happy with that. Sounds like a reason to pay me a salary.

**George Haikal:** Yeah, we need to get you both, like, Lovable, dedicated salaries or stipends.

**Megan Dickey:** Yeah, because are y'all, because you have other jobs, right? Or are you only working on Lovable?

**Georgemaine Lourens:** No, we also work on other stuff.

**George Haikal:** A lot of other stuff, too. Like, Lovable's been the minority the last couple weeks, right? In terms of your time?

**Georgemaine Lourens:** Yeah, because the last two weeks are kind of like out of office.

**Nicolas:** So, yeah, I've been eating and listening to Christmas music, so.

**George Haikal:** It's nice, taking a break.

**Georgemaine Lourens:** I know, I know.

**George Haikal:** It was amazing. Back to it.

**George Haikal:** Cool, and then, like, the only thing that I think sits with us, Megan, is thinking through how to price out the increase in templates as well.

**Megan Dickey:** Yeah, for sure.

**George Haikal:** Because that's still more manual than, I think it can at least be $10,000 more.

**George Haikal:** Yeah. More, because, yeah, I mean, we could talk about it offline, too, but something along those...

**Megan Dickey:** Okay, for sure. Yeah, I think we also have that new channel, Deals Desk, that I think Bridget was maybe wanting any sort of upsell to run through, so we can kind of start a thread in there.

**George Haikal:** Yeah, more so than coming up with a proposal.

**Megan Dickey:** For sure. Yeah, got it.

**George Haikal:** All good things, though. And one final thing for you, Georgemaine.

**Georgemaine Lourens:** I remember before we went on the holiday break, you asked us to look into making a design of the template page for Sebastian, and I dropped it in the channel. Did you have a chance to look at it? Like, do I need to do anything more there, or?

**George Haikal:** Let me see, it's in the internal, or it's in the project, the available templates?

**Georgemaine Lourens:** It's in the project page.

**George Haikal:** I see that. Site not found.

**Georgemaine Lourens:** But lord, maybe the deployment is dead. I'll take a look after the call and see if I can get the staging up and running again.

**George Haikal:** No problem. But yeah, if this looks good, let me see Nico's comments.

**Nicolas:** Yeah, spoiler alert, it's amazing.

**Georgemaine Lourens:** You're biased.

**George Haikal:** And then without comments, what's the, say this gets approved, right? Like, what do you need from Lovable, if anything?

**Georgemaine Lourens:** If it gets approved, then we need to figure out a way to, like, part of the experience was that instead of kind of like reading about all of the additional functionality and themes that you could do, you can actually try them out in real time in the iframe. I got the theming working with their themes. But the thing that I couldn't get working was the prompting for adding more functionality. So there's kind of like list items that kind of says like, hey, you have a blog, you have a portfolio, and maybe you want to add a blog so you can write case studies, or maybe you're a visual artist, and you can add like an e-commerce store. And clicking that, like my ideal user experience would be that if you select that, and then you remix a template, then you would start off with a prompt that kind of like adds that functionality for you. And that is the piece that we need help with because we don't have access to their LLM. But that sounds kind of like a very straightforward thing to do. I mean, it's kind of like copy a prompt and then paste it in and send it off.

**George Haikal:** Cool. That makes sense. I was just thinking in my head, like what more we could do, and if there's something... If we could just build a component library as well, that could be really cool, but I think that's too niche right now. But it would be amazing to just have a number of tables that you could use or a number of types of blogs that someone could just pull in and use as they're building something, whether it's a website or whatever it is. I'll think about it more, but there's ways to tie in the work that we're doing to the way that their users are actually trying to build things. I think make it like visual and appear on the website.

**Georgemaine Lourens:** So I think I get what you're meaning. So instead of like having a prompt that does it for you, that maybe it's kind of like we just pull in existing things and it just kind of like shows up in real time.

**George Haikal:** Yeah, maybe. Cause like, you know, so if I'm trying to build a PDF generator, I can go to the template eventually and I can remix it and I can have the PDF generator that it gave me. I still need to understand what I want it to look like. And what to edit. And then I have to make the edits back and forth with Lovable and trust that it's going to make some correct. And then I have to like adjust again and go back and forth with it. If there's a way that within like the tool section, there's a tool builder, right, which is the prompt box, but also pulling in these component templates that we have into what you want to build. It could be easier. Maybe you can like edit each one individually. So you can edit, you know, exactly what you want your table to look like, and you can edit the table. And now this is a component that lives and you can save and then you can pull it into something that you're building. And that's agnostic of tool because then now it's just like a piece that you can pull into a website or a tool or whatever. And then you can sell that component on a marketplace to just like an idea that popped into into my head.

**Georgemaine Lourens:** Yeah, I think that's a bit more complex, but it kind of sounds like the components aspect that like Framer has on their website, where you can just pull something in and just tweak a build. I think that could be cool.

**George Haikal:** Because they're just super down for anything like that that's going to explode. This might sound crazy, but if we have an idea that explodes, we could get them to pay us $100,000, $200,000 a month, if what we're doing is working. So it's really up to the impact that we want to have and the resources that we want to put into it. And they're like a rocket ship right now. Let's see. Which one was the one you were talking about?

**Georgemaine Lourens:** I don't understand the navigation. Marketplace, I think.

**Georgemaine Lourens:** And then hit components. So they have these little components that do like one thing, right? Like a typewriter effect or like the glow thing. And you can just copy and paste that. But the way that you were talking about it made me seem like maybe there's a library somewhere that you can just kind of like, If you want something. These useful components from, and you can just tweak them and then pull them into your existing project.

**George Haikal:** Exactly. Or like, even when you're in the prop box, it's like, hey, I want you to create an FAQ section. Then like two or three recommendations of these components pop up and you can actually like visually see, do you want this one? Let's take the same way it recommends an answer. Like which answer is better? It's like, which one should you select? And they could pull from these. So like you add another visual, because everything that they're doing now is to make building easier for, yeah, for their user.

**Georgemaine Lourens:** Yeah, and I get that part because it's kind of like Lovable, so powerful, but most of the functionality is kind of like hidden within a language barrier that you have, right? But everyone can, if you can look at it and see what's possible, then it's much easier to kind of like pick what you want, because they just kind of have to, oh, I like this, I like how this works. And then just kind of make it look and feel like the style that you want. I think there's definitely something there, but it's your question of exploration.

**George Haikal:** Sure. Because we can do way better. This is just screenshots.

**Georgemaine Lourens:** I think this isn't really easy.

**George Haikal:** Cool, though. This is cool.

**Georgemaine Lourens:** Yeah, if you have some time this week, like if you want to take it out and then go for it and maybe I can spin off from there.

**George Haikal:** Yeah. Totally. Just popped into my head and now I have a little more time because we have some more help on our other accounts and I have a little more time.

**George Haikal:** Cool. Cool. I think that's it. Let me know when the render works for that new design page that you made, and then I'll put us in a group chat, all of us with Sebastian, to get his thoughts and then see what we need to do to get it implemented. But I think even that's a step in the right direction.

**Georgemaine Lourens:** Cool.

**Megan Dickey:** Yeah, and in the meantime, I'll flag that bug to the Lovable team.

**Georgemaine Lourens:** All right.

**George Haikal:** Amazing. Great stuff. Great to have everybody back.

**Georgemaine Lourens:** Let's do it.

**George Haikal:** Let's do it.

**Georgemaine Lourens:** Likewise.

**Megan Dickey:** Have a great day, guys. Thanks, everyone.

**George Haikal:** See you.

**Nicolas:** Bye.
