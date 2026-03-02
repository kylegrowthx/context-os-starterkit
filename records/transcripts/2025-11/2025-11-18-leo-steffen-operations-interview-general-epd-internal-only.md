# Leo Steffen -Operations Interview | General EPD (internal only)

<metadata>
date: 2025-11-18
time: 18:59 UTC
duration: 62 minutes
organizer: Bridget McGillivray
participants: Bridget McGillivray, Leonardo Steffen
fathom_recording_id: 102550491
fathom_url: https://fathom.video/calls/477563086
share_url: https://fathom.video/share/ssz8sN76Jtpz2FHj7YgRUHGvawszSt1r
source: fathom
enriched_on: 2026-03-02 15:30 UTC
</metadata>

---

## Summary

Bridget McGillivray interviewed Leonardo Steffen for GrowthX's Chief of Staff to the CTO role. The conversation focused on how Steffen manages multiple projects simultaneously, prioritizes competing demands, and handles complex organizational dynamics. Key examples included cutting scope on a Wi-Fi library project at GuestLogix to meet a critical deadline, and escalating a multi-tenancy merge review at Ryan Tax through the director to unblock other teams—both demonstrating his pragmatic, efficiency-first approach. Steffen's "generalizing specialist" profile and ability to navigate hierarchical organizations align well with the role's need for a high-leverage partner to Daniel (the CTO) managing 15-20 engineers across 4-5 simultaneous product lanes.

---

## Context

GrowthX is interviewing Leonardo Steffen for a newly created Chief of Staff role to Daniel, the CTO. This is a specialized staff role—not a traditional EA or administrative position, but a strategic "force multiplier" designed to provide context-switching support and QA oversight across the engineering and product org. Steffen is a contract full-stack engineer currently at Ryan Tax (a large, Texas-based tax consulting firm), based in Passo Fundo, Brazil. He has been actively interested in the GrowthX role since applying earlier and waited for the right position to open that matched his skill set. Bridget McGillivray, who has held a traditional Chief of Staff role to a CEO, conducted this interview to assess Steffen's fit, focusing on his ability to manage multiple priorities simultaneously and navigate complex organizational structures.

---

## Relevance

- **To GrowthX Delivery and Operations:** Steffen's pragmatic problem-solving approach and comfort with scope reduction could shape how GrowthX manages timelines and complexity. His experience running large, hierarchical teams and unblocking process bottlenecks is directly applicable to supporting Daniel's multi-lane engineering org. His use of ChatGPT for planning and decision-making suggests alignment with GrowthX's AI-forward mindset.

- **To GrowthX Org Dynamics:** Steffen explicitly mentioned adapting to GrowthX's writing culture and asynchronous communication style, which fits the international, distributed team structure. His humility ("I'm not afraid of saying I don't know") and ability to mentor younger engineers suggest he'll integrate well with the team. His efficiency-first mindset may help counter scope creep and meetings overhead.

- **To Role Execution:** The Chief of Staff role requires weekly prioritization conversations with Daniel, helping identify must-haves vs. nice-to-haves and then owning QA, vendor research, or other high-leverage work as needed. Steffen's track record of doing three weeks of deep preparation (onboarding documentation, ramp-up planning) indicates he takes structural investment seriously. His experience escalating issues through hierarchy (director at Ryan Tax) is a key capability for unblocking cross-team dependencies.

---

## Overview

- **Role Context:** The CTO needs a "force multiplier" to manage a 15–20 person Eng org and 4–5 simultaneous product lanes, requiring a partner for context-switching and QA.
- **Problem-Solving:** At GuestLogix, Steffen cut scope on a Wi-Fi library project, prioritizing a working app for a critical deadline over a reusable library that was causing delays.
- **Process Navigation:** At Ryan Tax, Steffen navigated a bureaucratic org by escalating review requests to a director, leveraging their authority to unblock a critical multi-tenancy merge.
- **Candidate Fit:** Steffen's "generalizing specialist" profile and efficiency-first mindset align with the role's need for a flexible, high-leverage partner.

---

## Key Topics

### The CTO's Need for a "Force Multiplier"

  - The CTO (Daniel) requires a Chief of Staff to manage a 15–20 person Eng org and 4–5 simultaneous product lanes.
  - The role is a "force multiplier" to provide context-switching support and QA oversight, enabling the CTO to focus on high-leverage work.

### Problem-Solving: Prioritizing User Value over Engineering Purity

  - **Context:** At GuestLogix, the Android app needed an offline Wi-Fi service for in-flight use.
  - **Dilemma:** Build the service as a reusable library (per a tech lead's request) or integrate it directly into the app.
  - **Decision:** After one month of work, the library approach proved too complex and risked missing the deadline. Steffen advocated for the direct integration.
  - **Rationale:** Prioritized user value (a working app) over engineering purity (reusability), using the deadline and risk of a non-functional product as the primary arguments.

### Navigating Bureaucracy: Unblocking a Critical Merge

  - **Context:** At Ryan Tax, a critical multi-tenancy merge was blocked by delayed code reviews, stalling other teams. The deadline was today.
  - **Challenge:** The org's bureaucracy and a contractor status limited Steffen's direct influence over reviewers.
  - **Action:**
      - Categorized review feedback into critical, good-to-have, and cosmetic.
      - Escalated the issue to the director, who used their authority to push for reviews.
      - Secured agreement from reviewers to approve the merge after only the critical changes were made, unblocking the project.
  - **Root Cause:** The project was broken down horizontally (by controller) instead of vertically (by full-stack feature), creating interdependencies and a single large branch that was difficult to review.

### Work Style & Feedback

  - **Energizers:** Solving new problems, learning, and operating as a "generalizing specialist."
  - **Drainers:** Process overhead (e.g., 5-layer story tracking) and unproductive debates (e.g., Vim vs. Emacs).
  - **Constructive Feedback:** A colleague suggested sharing detailed written plans in stand-ups to provide more context.
  - **Positive Feedback:** Praised for adaptability and humility, especially in admitting when knowledge is lacking.
  - **Self-Improvement:** Learning to say "no" to manage workload and avoid overcommitment.

---

## Action Items

**Leonardo Steffen (GrowthX candidate)**
- Email Daniel & Tucker your 3-week ramp-up plan

**Bridget McGillivray (GrowthX)**
- Email GP re: Leonardo interview outcome

---

## Transcript
**Leonardo Steffen:** Hi, how's it going?

**Bridget McGillivray:** Good.

**Leonardo Steffen:** I'm doing great. Thanks for your time.

**Bridget McGillivray:** Yeah, no worries. Sorry, I'm a little bit late.

**Leonardo Steffen:** I was just running late. I was wondering if you were joining with the two note takers here.

**Bridget McGillivray:** Yeah, you know, we're switching from Fathom and moving to Fireflies, but we haven't really made the switch yet. So I'm always nervous about having multiple recording systems, but I like the redundancy.

**Leonardo Steffen:** I just thought it gave me access to the live transcription.

**Bridget McGillivray:** Cool.

**Leonardo Steffen:** Okay, I'm trying to see it now.

**Bridget McGillivray:** So where are you based?

**Leonardo Steffen:** I am based in Passo Fundo, a city in the southernmost state of Brazil.

**Leonardo Steffen:** It's the northern part of the southern state.

**Bridget McGillivray:** Okay, I see it. We have a bunch of people in Brazil actually. One of our recruiters is in Florianapolis, and we have an engineer down right on the border—on the border of Uruguay, actually.

**Leonardo Steffen:** Probably somewhere around Uruguayana or thereabouts.

**Bridget McGillivray:** We have a bunch of, lots of Brazilians.

**Bridget McGillivray:** It's nice to meet you, though.

**Bridget McGillivray:** I'm excited to talk to you.

**Bridget McGillivray:** I've heard great things.

**Leonardo Steffen:** Good.

**Leonardo Steffen:** Yeah, I'm excited.

**Leonardo Steffen:** You know, I've been kind of chasing Tucker and Daniel as ever.

**Leonardo Steffen:** Ever since I first applied, there was no, I mean, I didn't match the exact role that they had.

**Leonardo Steffen:** And they had more, one that was going to be more for me.

**Leonardo Steffen:** I just waited and waited.

**Leonardo Steffen:** So when it came, was like, perfect.

**Leonardo Steffen:** Yeah.

**Leonardo Steffen:** It just, when I read the description that Tucker sent me, was like, okay, wow.

**Leonardo Steffen:** This is just exactly what I, what I looked for and never, never really found.

**Leonardo Steffen:** It's different.

**Leonardo Steffen:** That's for sure.

**Bridget McGillivray:** Like I, so Daniel asked me to interview you and meet you because I've been a chief of staff before, but more traditional, like to a CEO and it's more like special projects based.

**Bridget McGillivray:** But Daniel had, you know, and there's such thing as chief of staff to CTOs, right?

**Bridget McGillivray:** But it's generally more.

**Bridget McGillivray:** Sometimes it can lean even all, like, I mean, I've seen a bunch of staffs who are, like, EAs, basically, and then all the way to, like, you know, super, super, super, super, super senior role.

**Bridget McGillivray:** Like, it's this huge realm, but I love the way Daniel was so thoughtful about going through it and, like, being so specific to him and our company and what he needs to be, like, he needs a force multiplier.

**Bridget McGillivray:** Because, I mean, one, we have, like, 15 to 20 people on the Eng.org, right?

**Bridget McGillivray:** Like, it's just a lot of people for Daniel to be overseeing.

**Bridget McGillivray:** We also are running, like, we have very ambitious goals and plans, so we have, like, four or five separate, like, lanes right now that are, like, pretty isolated from each other, not in a bad way.

**Bridget McGillivray:** They're just, like, we're tackling, like, multiple different platforms and products at once.

**Bridget McGillivray:** So it's a lot of context switching, I think, for him, too.

**Bridget McGillivray:** And then some days he needs, like, some months he's going heads down in one, and then, like, you can't just put the other ones in the back, right?

**Bridget McGillivray:** So he's...

**Bridget McGillivray:** He's really looking for, like, Daniel to help have eyes everywhere and then, like, really also bring the QA aspect as well, just so he feels reassured that, like, somebody else is keeping an eye on things.

**Bridget McGillivray:** But I think it's such a cool role.

**Bridget McGillivray:** Like, when he finally wrote it out, I was like, this is awesome.

**Bridget McGillivray:** Like, this is going to be such a high leverage thing for him.

**Leonardo Steffen:** Yeah, I understood exactly what he was looking for. Someone who could help him do the work that he doesn't have the time to do or doesn't want to do. Basically, an extension of his capacity.

**Bridget McGillivray:** Like, if there was more hours in the day, you know, he could it, but it's not, unfortunately.

**Bridget McGillivray:** But he wanted me to spend time, like, a lot of, you know, with that comes, like, for you would come a lot of organization.

**Bridget McGillivray:** And like context switching yourself and like trying to keep tabs on things.

**Bridget McGillivray:** I wanted to like double click a little bit into like past experience through that lens of like managing multiple projects at once.

**Bridget McGillivray:** And like, how do you, you know, that's sort of what I want us to talk about today is like some examples of where you've like overseen multiple things at once.

**Bridget McGillivray:** And like, how do you prioritize?

**Bridget McGillivray:** How do you make sure they all have progress going?

**Bridget McGillivray:** And like, what kind of tools do you use to keep yourself organized so that like, you know, if he's kind of asking you to keep an eye on things, it doesn't drop again, right?

**Leonardo Steffen:** Like, so that's kind of what I wanted to spend time today on with you, if that makes sense.

**Leonardo Steffen:** Yeah, sure.

**Leonardo Steffen:** So on my previous job, right now I'm working at a company that does a lot of, it's kind of a very traditional company.

**Leonardo Steffen:** Like a large organization with a very high, with lots of levels in their hierarchy.

**Leonardo Steffen:** So everything is processes, and you have to ask for approval, and things don't work if you don't talk to the right person, and nobody says, oh, I'm blocked.

**Leonardo Steffen:** So it's a bit different than what I'm used to.

**Leonardo Steffen:** I ended up organizing their onboarding documentation.

**Leonardo Steffen:** They had a page, a wiki page, with onboarding, because I was tossed into a project, a very complex project.

**Leonardo Steffen:** I didn't know about those rules, Microsoft rules engine that they were using, and I didn't, and I got a Windows computer.

**Leonardo Steffen:** I haven't touched Windows in like 15 years or so.

**Bridget McGillivray:** Me neither.

**Leonardo Steffen:** Yeah, so I had to start to relearn Windows or relearn Windows altogether.

**Leonardo Steffen:** Then onboard myself.

**Leonardo Steffen:** And

**Leonardo Steffen:** Help the team, a new team of people who joined our team to be, I had to onboard them because the project was growing.

**Leonardo Steffen:** So to do that, I organized the entire wiki page.

**Leonardo Steffen:** So that was something that I had to do to keep things.

**Bridget McGillivray:** So did you onboard yourself first, build the program through doing it, and then, okay.

**Leonardo Steffen:** I onboarded myself, figured out all of the details that were not clear in the documentation, talked to the 52 different people that I was told that I had to talk to.

**Leonardo Steffen:** It took me almost a month to onboard myself.

**Bridget McGillivray:** And you also had a different role and responsibilities at the time, or was that your core focus?

**Leonardo Steffen:** I was a full stack engineer.

**Leonardo Steffen:** So I was hired to work at this front-end, back-end part of it.

**Leonardo Steffen:** The project, the new solution that the company is offering.

**Leonardo Steffen:** But I had to onboard myself because everybody was just busy.

**Bridget McGillivray:** Yep.

**Bridget McGillivray:** I didn't want to stop others to do that.

**Leonardo Steffen:** So I got the documentation. It was really bad—it didn't have all the details I needed. I figured it out, talked to people, wrote it down, and then updated it. When my director said they wanted to onboard five new developers and asked if I could help, I was like, okay, great. Here's the documentation—you're all set. I didn't have to spend any more time on it. The approach was self-organized.

**Leonardo Steffen:** But that gives you a hint. I like to plan, but I'm not a plan freak. A lot of people can't live with uncertainty, but I can. And I live in chaos.

**Leonardo Steffen:** I get a lot of different projects. I have my own projects going. I have kids—two in one city, one in another city, and parents in several different places. So I organize myself. I don't make a large master plan, but when I decide to do something, I plan it and I go with it.

**Leonardo Steffen:** And if something goes wrong, well, just change the plan, replan.

**Leonardo Steffen:** And I've been using AI for that a lot.

**Bridget McGillivray:** Do you have, like, an example of some time when you had to, like, make a hard decision to deprioritize something, basically?

**Leonardo Steffen:** Yes, at GuestLogix, I was responsible for the core platform.

**Leonardo Steffen:** For the Android application, and other microservice that was for identity, it was a Python service.

**Leonardo Steffen:** And we were growing the mobile Android application.

**Leonardo Steffen:** We needed to put it to run in airplanes without internet connectivity.

**Leonardo Steffen:** So I had to, it wouldn't work with Bluetooth, so I had to kind of reverse engineer the iOS Wi-Fi service, Wi-Fi library or service, and make it and create one for Android.

**Leonardo Steffen:** But it was a lot of work.

**Leonardo Steffen:** People wanted me to make it as a library, whereas I could have done it very quickly just in the app. So I spent a month working on it and got it to work. Then they wanted it as a library so that...

**Leonardo Steffen:** The other Android apps, the Flutter and the React Native apps could use it.

**Leonardo Steffen:** But it ended up taking me another month just to package it as a library, and it was not done.

**Leonardo Steffen:** So that's when I told them, well, not work.

**Leonardo Steffen:** We're going to have to change it.

**Leonardo Steffen:** We're going to have to stop doing it and use it as just as a part of the Android app without not making it as a library.

**Leonardo Steffen:** He was a little bit, I mean, the other guy, he was not the director of engineering, he was the tech lead of the iOS app.

**Leonardo Steffen:** didn't like it because he was the one who kind of wanted it to be made as a library.

**Leonardo Steffen:** He didn't like it that much, but at the end, if we didn't have that part of the app working, we wouldn't have a product attached.

**Leonardo Steffen:** So it was kind of a decision where we had to decide whether to continue the idea because of the beauty of the engineering or we wanted something quick to put it to test, right?

**Leonardo Steffen:** What was like the criteria you used to make the decision?

**Leonardo Steffen:** Time.

**Leonardo Steffen:** I mean, time versus, it was cost versus benefit.

**Leonardo Steffen:** I mean, both leaving it in the app or in the app code versus extracting it as a library would give the exact same results from a user standpoint.

**Leonardo Steffen:** We would see that it was different.

**Leonardo Steffen:** We would know that we could reuse it for another app or other apps, us as engineers.

**Leonardo Steffen:** But we're not there to make engineers happy.

**Leonardo Steffen:** We would know that's an...

**Leonardo Steffen:** And make users get back to our application and test it and validate it.

**Leonardo Steffen:** So that was it.

**Leonardo Steffen:** It was a hard conversation.

**Leonardo Steffen:** There was one person who didn't like it.

**Leonardo Steffen:** Others were just supportive because it just made sense.

**Leonardo Steffen:** We had worked almost two months in this, but it was not ready.

**Leonardo Steffen:** So it doesn't make sense.

**Bridget McGillivray:** What was the main, like the person in opposition, like what was their main argument?

**Leonardo Steffen:** For, to having the library?

**Bridget McGillivray:** Yeah, like the one person you said who was like quite in opposition with everybody else.

**Leonardo Steffen:** Reusability.

**Leonardo Steffen:** It does make sense, right?

**Leonardo Steffen:** It does make sense to take that part of the code and put it in and make it, turn it into a library.

**Leonardo Steffen:** But it is a lot harder to test, right?

**Leonardo Steffen:** You have to make several different combinations to be able to test things.

**Leonardo Steffen:** It's not something that you can just run on my IDE.

**Leonardo Steffen:** It was not that simple.

**Leonardo Steffen:** So it was just that.

**Leonardo Steffen:** The tradeoff was, do we continue working until we're done?

**Leonardo Steffen:** It could take an extra month.

**Leonardo Steffen:** could take like 90 days.

**Leonardo Steffen:** Or do we just stop now, throw the two months of the extra, the added month to trying to make it into a library?

**Leonardo Steffen:** Do we throw it away and just use it as it was in the beginning, just coding the app?

**Leonardo Steffen:** So I always tend to think of things like, is this required for now, for what we want now?

**Leonardo Steffen:** Or is it something that people just want because they're attached to the IDE?

**Leonardo Steffen:** Just very invested.

**Leonardo Steffen:** Yeah.

**Bridget McGillivray:** Once you get invested in something, you tend to get attached to what you're working on.

**Bridget McGillivray:** Yeah, I mean, I just find everything's like, everything is a good idea at some point.

**Bridget McGillivray:** It's like sequencing it and in what order should we do it, basically?

**Bridget McGillivray:** Like, we should do, you should do all those things at some point in time, but like, what do you want to do now and first?

**Bridget McGillivray:** Like very tactically, how did you go about making your proposal? What was the team structure? Who did you have to get buy-in from?

**Leonardo Steffen:** Well, first we had a deadline. I told the team we wouldn't be able to deliver in time if we kept trying to make it as a library. And if we did push to deliver, we wouldn't have time to test the app.

**Leonardo Steffen:** It would probably crash during the flight and be useless.

**Leonardo Steffen:** That was my argument. We didn't have time because we wanted to do something that wouldn't deliver any user value—it would just be for us as engineers. But if there's no users, there's no us as engineers in a company. So I was trying to stress that we had to get this done. Packaging it as a library could wait—we just had to make it fast and working.

**Bridget McGillivray:** Let me rephrase that.

**Bridget McGillivray:** So you, the deadline's approaching, you need a decision made, like what tools do you use to push the decision?

**Bridget McGillivray:** Are you like, is it like a meeting everybody's in?

**Bridget McGillivray:** And then like, how did you present your recommendation and drive a decision?

**Leonardo Steffen:** I usually look around the team and identify the strongest opponent—the person who's against what I'm trying to do. I talk to them to see if they can convince me or explain their reasoning. I explain my reasoning and we try to find middle ground. If I'm wrong, I'm wrong. It's fine. I usually just have conversations. I don't use formal tools for making decisions.

**Bridget McGillivray:** What I meant was more about writing culture. We have a big emphasis on putting your thoughts into words, pre-reads, that kind of thing. Were you using anything like that?

**Leonardo Steffen:** I write a lot and I write emails to myself. I also talk a lot with ChatGPT. I asked ChatGPT to pretend to be a GP to do a mock coding interview with me. I've never had a coding interview that encouraged AI use—usually it's the opposite. But I have lots of projects in my ChatGPT—each with its own chats and items.

**Leonardo Steffen:** I don't like to mix the chat.

**Leonardo Steffen:** And I have one particular project that I call Brain Dump, which I just go in and toss all the ideas.

**Leonardo Steffen:** have kind of a brainstorming, and then I separate things.

**Leonardo Steffen:** But when I'm lost and I know that I have to make a decision or try to propose something to people who I know are probably not going to like, when I brainstorm with myself, just write all the aspects, the things that I know, the things that I don't, try to be honest with myself, because it's not, I can't say it is impossible for me to be completely wrong in my assumptions.

**Leonardo Steffen:** Yeah, it's better to admit it out loud or something like, these are the risks inherent in this recommendation.

**Bridget McGillivray:** because I don't, I'm making assumptions here.

**Bridget McGillivray:** Or I have no enough information here to know.

**Leonardo Steffen:** And one thing about prioritizing ideas or work pieces, sometimes things are not just easy to differentiate what's the priority.

**Leonardo Steffen:** Or if everything has the same high priority, I just try to pick the smallest first or the easiest first to be able to move things across and make decisions on those.

**Bridget McGillivray:** Yeah, do you have a way of like, say there was 10 things on your plate, how would you try to stack rank the priority?

**Bridget McGillivray:** You mentioned like, maybe do smaller things first, but like, what would be the criteria for you to pick this as the number one thing this week?

**Bridget McGillivray:** And if you have like an example, that would be helpful too.

**Leonardo Steffen:** Let me think, but the whole idea is to...

**Leonardo Steffen:** If everything is high priority, right, or kind of similar, if nothing is critical and has to be done first, then I go with what's quicker to get across the board.

**Leonardo Steffen:** It's less things for people to worry about, and it's one more thing done in the end.

**Leonardo Steffen:** Yeah, true.

**Leonardo Steffen:** A software development task or an engineering or whatever other task, it's not always easy to see the size of it.

**Leonardo Steffen:** So if I can see that something's easy, I go with that one first.

**Leonardo Steffen:** There's another one that I see that is not, I mean, that is larger than the one that I found easy or more difficult than that one.

**Leonardo Steffen:** That one can take a lot more time.

**Leonardo Steffen:** So I go with the maybe low-hanging fruits or.

**Leonardo Steffen:** Quicker or what's a must-have.

**Leonardo Steffen:** So you asked me for an example, and I just got one here.

**Leonardo Steffen:** I'm working, right now we're trying to finish this multi-tenancy merge to the rules engine service, the workflows engine that I'm working and building with the team now.

**Leonardo Steffen:** And we have this large feature branch.

**Leonardo Steffen:** I asked the team, the other devs, to just push their code into that branch because we wouldn't be able to merge everything to the main branch without causing a lot of trouble.

**Leonardo Steffen:** So I asked everybody to push their code in that same branch.

**Leonardo Steffen:** The branch has been there for a month or so, and it's been ready since Monday last week.

**Leonardo Steffen:** And I've been asking people, please review, please review, let's review this, this is large.

**Leonardo Steffen:** Thank you.

**Leonardo Steffen:** you.

**Leonardo Steffen:** you.

**Leonardo Steffen:** There's a lot of people blocked because of this.

**Leonardo Steffen:** We're done.

**Leonardo Steffen:** So people saying that they're blocked because of this work.

**Leonardo Steffen:** And I keep saying it was ready.

**Leonardo Steffen:** At the finish line.

**Bridget McGillivray:** Yeah, it was ready.

**Leonardo Steffen:** So last week on Thursday, from Monday to Wednesday, there was no move in that.

**Leonardo Steffen:** No reviews, nothing.

**Leonardo Steffen:** No, it was just silent.

**Leonardo Steffen:** And then Thursday, I got 16, 18 reviews, comments there with things to change.

**Leonardo Steffen:** So I sat with the other Davin that's working with me.

**Leonardo Steffen:** And I was like, OK, so let's make a plan.

**Leonardo Steffen:** Let's plan how to get through all the change recommendations.

**Leonardo Steffen:** We made a plan dividing and it's splitting into critical.

**Leonardo Steffen:** Not kind of not critical, but good to have.

**Leonardo Steffen:** And cosmetic were low-priority things.

**Leonardo Steffen:** And we decided that we were going to work on the critical ones, talk with the people who commanded out to see if they were okay with approving the branch, the pull request, without the other ones, without the things that were not critical.

**Leonardo Steffen:** Because we needed to move this forward.

**Leonardo Steffen:** And they were okay with that.

**Leonardo Steffen:** And I didn't want to tell them that we are going to take a lot more time now, because we had three days that we could have gotten this feedback and worked on them, on all the teachers, but we didn't.

**Leonardo Steffen:** So just try to reduce the scope of the changes that we had to make.

**Leonardo Steffen:** Is that because there was a big deadline or something?

**Bridget McGillivray:** Or you just wanted to hold everybody to like a, let's get it out?

**Bridget McGillivray:** There's a big...

**Leonardo Steffen:** Business folks are anxious.

**Leonardo Steffen:** They want to see this work.

**Leonardo Steffen:** They want to see this thing working.

**Leonardo Steffen:** So they've been asking where is it, where it is, and what's the progress?

**Leonardo Steffen:** And it's hard to just tell them what or the exact progress on items that are this complex database.

**Leonardo Steffen:** So we were supposed to finish this today.

**Leonardo Steffen:** Yeah, we were.

**Leonardo Steffen:** The deadline was today.

**Leonardo Steffen:** And people...

**Bridget McGillivray:** hear the was not done.

**Leonardo Steffen:** No, it is done.

**Leonardo Steffen:** It is done because we cut scope.

**Leonardo Steffen:** Because we had it last week on Monday.

**Leonardo Steffen:** was done.

**Leonardo Steffen:** But on Thursday, some people started to look at it and found other things.

**Leonardo Steffen:** Most of the things were just like, oh, I have to give feedback, so I'll give feedback.

**Leonardo Steffen:** It's not really necessary.

**Leonardo Steffen:** could have done it long ago.

**Leonardo Steffen:** Yeah.

**Bridget McGillivray:** What do you think was the reason why it took so long?

**Bridget McGillivray:** Like, who were the people that had to be involved and why were they taking so long?

**Bridget McGillivray:** Like, I know you mentioned the company is just bureaucratic in general.

**Leonardo Steffen:** To be honest with you, my perception is that they were blocked.

**Leonardo Steffen:** Okay.

**Leonardo Steffen:** And it was looking bad.

**Leonardo Steffen:** To just go to our standup meeting every day and say that they were blocked and hear me and the other guys say, well, you can, we are waiting for reviews or waiting for WordPress reviews.

**Leonardo Steffen:** So I guess it's more like the kind of company where people just do work because they fear of being called out.

**Leonardo Steffen:** But who needed to review it?

**Bridget McGillivray:** Was it different people?

**Bridget McGillivray:** people.

**Leonardo Steffen:** Different Different people.

**Leonardo Steffen:** people.

**Leonardo Steffen:** Different engineers.

**Leonardo Steffen:** There's a rule that requires two devs to review everything.

**Bridget McGillivray:** And what were they doing?

**Bridget McGillivray:** Like, what were they doing instead of reviewing this if it was like a company-wide, you know, urgent thing?

**Leonardo Steffen:** It was a team-wide, not a company-wide, but the company is going to use it.

**Leonardo Steffen:** They were doing other tasks. There were other things to do, but not things that were due today. The issue was that this was the top priority, and their downstream work was blocked waiting for the review.

**Leonardo Steffen:** We built the foundation for multi-tenancy on all databases—splitting databases, migration tools to copy data from one table to another. But the front-end changes don't work without the back-end changes. Until we had this code merged, nothing moved forward.

**Bridget McGillivray:** I guess like how, if you were to go back in time, what would have, what could you have done to make things move faster?

**Bridget McGillivray:** Like the way I'm hearing it is, it would help them to review sooner because it was like bottlenecking other things.

**Bridget McGillivray:** It was the priority.

**Bridget McGillivray:** So how could you have made it go faster?

**Leonardo Steffen:** Looking back, the issue was how we broke down the stories. Ziya proposed we split things to parallelize, but we ended up breaking things down horizontally instead of vertically.

**Leonardo Steffen:** I only realized how wrong this was when we got to the point where everything was interlocked. It wasn't "I do this full stack, then you do that full stack." It was front-end pieces scattered, back-end pieces scattered, all interdependent, so you couldn't make progress independently.

**Leonardo Steffen:** And on top of that, because of how the stories were broken down into tasks, we couldn't merge pieces of code to main without breaking the build.

**Leonardo Steffen:** Yeah, everything was interdependent.

**Bridget McGillivray:** So what was your original intent when you went horizontal instead of vertical in the beginning?

**Bridget McGillivray:** What was the original idea for that being the right path?

**Leonardo Steffen:** The API has several different controllers. It made sense to let one person work on everything related to one controller, another person on another controller, and so on. But what I didn't account for was that there's a framework underlying all those parts.

**Leonardo Steffen:** When you touch any part, you have to change the framework. But framework changes can't go together with the other code changes—they have to go in a separate branch. So every person working on a controller also has to change the framework, and they all get blocked waiting for each other. It's a mess.

**Bridget McGillivray:** Like if you were, okay, so say you had the opportunity, like back to the original question, to rewind and like make a new plan to get it done faster.

**Bridget McGillivray:** What would that look like then?

**Bridget McGillivray:** Or what would you at least try next?

**Bridget McGillivray:** Doesn't have to be, no, that it would be perfect.

**Leonardo Steffen:** I would try to start from the front end perspective, because at the end of the day we're building something for people. But even doing vertical full-stack slices, we'd have the same problem—everyone touching the framework creates the same bottleneck. So really, the problem is the architecture itself.

**Bridget McGillivray:** Yeah.

**Bridget McGillivray:** What about, like, in terms of just getting people to move faster?

**Bridget McGillivray:** And obviously, it's a game of just competing priorities and things like that.

**Bridget McGillivray:** Is there anything you could have done to get people reviewing a week earlier?

**Leonardo Steffen:** I tried. I talked to several people, reviewed their code, offered help, spoke up in team meetings.

**Leonardo Steffen:** But the thing is, I had to go to the director and ask him to push people to review. Because the organization is very hierarchical. I'm a contractor—if I ask them to do something, they'll do it when they're free. But if their boss asks, they'll prioritize it.

**Leonardo Steffen:** That's fair.

**Bridget McGillivray:** I mean, even if you were, even if there was more of a flat org, sometimes you just need, like, you just need Daniel to just freaking go push somebody.

**Bridget McGillivray:** Like, I always have that situation, too, where I'm like, certain people's voice carries more weight, even if it's flat, you know.

**Bridget McGillivray:** It's just, because they are always worried that you might be missing some piece of context that, you know, and then it will lead them in the wrong direction.

**Bridget McGillivray:** It's usually people just, like, protecting themselves, not, not.

**Bridget McGillivray:** trying to do anything malicious or anything, but yeah, that makes sense.

**Bridget McGillivray:** It's like, so maybe you would have gone to the director earlier and asked them to push because they were aligned.

**Bridget McGillivray:** Yeah.

**Bridget McGillivray:** Yeah.

**Leonardo Steffen:** I would have asked him explicitly, just told him, I would have told him to please ask Fathom to review.

**Leonardo Steffen:** So I told him, but not, maybe I didn't, I did not emphasize it enough that we needed this and we needed it now.

**Leonardo Steffen:** Yeah.

**Bridget McGillivray:** Help me help you.

**Bridget McGillivray:** What, what are like, what, what are things that energize you and what are things that drain you?

**Leonardo Steffen:** Things that energize me, problems, or learning.

**Leonardo Steffen:** We've We've got those.

**Bridget McGillivray:** Yeah.

**Leonardo Steffen:** No, new things.

**Leonardo Steffen:** So that's why I like the idea for a generic.

**Leonardo Steffen:** Generalist, yeah.

**Leonardo Steffen:** I always called myself a generalizing specialist, but some people told me that that did not sound good.

**Leonardo Steffen:** I just, that's who I am.

**Leonardo Steffen:** I can put another name, but, well, I like to learn things.

**Leonardo Steffen:** I like to get out of my comfort zone.

**Leonardo Steffen:** So I told Daniel that I have this kind of, I'm addicted to not knowing or to, not sure if I can say, I can say being behind, but, well, addicted to not knowing what I'm doing and having to learn it, you know, having to figure out, it's exciting to me.

**Leonardo Steffen:** What trains me is, you know, people dragging their feet to get something done, you know, or just trying to...

**Leonardo Steffen:** Spark little conflicts because of things that don't really matter.

**Leonardo Steffen:** What do you mean by that one?

**Leonardo Steffen:** Well, discussions in general about things that are not really critical to get something done.

**Leonardo Steffen:** Some people have preferences like let's use Vim or Emacs or Ruby or Python.

**Leonardo Steffen:** But if it's something that you have people that, let's say, one person comes in and says, Python is better for this, this, and that.

**Leonardo Steffen:** And you have three people that already work with Ruby.

**Leonardo Steffen:** And that person is trying to convince the others and creates a kind of a bad environment of talking, trashing the language that the others know.

**Leonardo Steffen:** It just creates a bad environment.

**Leonardo Steffen:** You know, and that kind of thing drains me because it's not productive, you know?

**Leonardo Steffen:** Yeah.

**Leonardo Steffen:** That is going to add to what we're trying to do.

**Leonardo Steffen:** And the person is going to do what the others are doing anyways, but just keep thrashing the other ones, what the others are doing already.

**Leonardo Steffen:** So I've seen a lot of that, and that's one of the things that drains me a lot.

**Leonardo Steffen:** The other thing that drains me is processes, excessive processes.

**Leonardo Steffen:** I'm really tired of having to, of getting lost in this, the way the team that I'm working at right now organizes this work is they have an epic, then they have a user story, then they have, or a feature, then they have a user story, then they have a technical story, then they have a task.

**Leonardo Steffen:** So there's a lot of layers to just something that I want to get them, you know, that drains me a lot because I don't, I end up.

**Leonardo Steffen:** Not knowing where something is and I have to waste my time to figure it out, to find it, or just to look for work, look for pieces of work that are duplicated and that people already did, but somebody else added it in there because they didn't know where to put.

**Leonardo Steffen:** And that's one of the things that drains me as well, heavyweight process.

**Leonardo Steffen:** Yeah, those are good answers.

**Bridget McGillivray:** Yeah.

**Leonardo Steffen:** How big is the company you're in today?

**Bridget McGillivray:** How big is it?

**Leonardo Steffen:** The company that I'm contracting to is, you know, Ryan, Ryan Tax.

**Leonardo Steffen:** It's from Daleks, from Texas.

**Leonardo Steffen:** Ryan.

**Leonardo Steffen:** It's one of the best, the biggest tax consulting firm, Ryan Tax firm.

**Leonardo Steffen:** The team that, well, they're pretty big.

**Leonardo Steffen:** I don't know what the size of the company is, but but my team is.

**Leonardo Steffen:** right back.

**Leonardo Steffen:** 14, 15, or so.

**Leonardo Steffen:** Okay.

**Bridget McGillivray:** Yeah.

**Leonardo Steffen:** There's a lot of people to give stand-up status, status of the stand-up.

**Bridget McGillivray:** Yeah.

**Bridget McGillivray:** What would be both constructive, like what's some constructive feedback you've received recently, as well as positive, like keep doing that feedback?

**Leonardo Steffen:** Constructive feedback.

**Leonardo Steffen:** So I write a lot of stuff to myself, but the team, the daily meetings were just too slow.

**Leonardo Steffen:** People were being too detailed.

**Leonardo Steffen:** They were talking a lot.

**Leonardo Steffen:** And I could tell that others were just zoning out.

**Leonardo Steffen:** They're not even paying attention.

**Leonardo Steffen:** So I just kept my plans to myself and added them to stories or sent them as message to the people who were interested.

**Leonardo Steffen:** And one of my, one of the guys who's been pairing with me for a while, I sent him, I shared with him the plan that I had to the work I was doing.

**Leonardo Steffen:** And he told me that I could talk more and use those, use the things that I wrote to give as status to the team.

**Leonardo Steffen:** Because I'm really always shallow in my status.

**Leonardo Steffen:** I don't care about the details, but he said he did and appreciated the written docs I sent him. That was constructive feedback.

**Bridget McGillivray:** So he wanted you to share more detail and communicate more broadly.

**Leonardo Steffen:** Yes, talk more in stand-up. Though I have to say, our current stand-ups have too much. With 16 or 17 team members, it takes almost an hour. Stand-ups should be quick—what I did yesterday, what I'm doing today, am I blocked? If people want to sync, they should meet separately. I prefer meaningful communication, not just noise.

**Leonardo Steffen:** It could be a chat message, doesn't have to be a meeting. One good thing I've done is always turn my camera on in meetings and encourage the team to do the same—let people see faces, not just names or numbers. I started that and people adopted it. But I don't think you need to be in a meeting every day if you have nothing to say.

**Leonardo Steffen:** Yeah, that's a lot.

**Bridget McGillivray:** No value.

**Leonardo Steffen:** As for positive feedback, I'm proud of what I've accomplished at places like GuestLogix and ThoughtWorks. People have told me I'm good at switching between projects.

**Leonardo Steffen:** That's because I don't really care about specific technologies—I know we're going to have to learn. I never pretend to know more than I do. I work with a lot of younger people, and one of them on Angular said, "I thought you were a pro or genius." I said, "No, I'm learning. You're going to teach me." That gave a good vibe to the team.

**Bridget McGillivray:** Yeah, being humble, essentially.

**Bridget McGillivray:** Yeah.

**Leonardo Steffen:** I'm not afraid of saying I don't know, and I'm not afraid to empower others to say it too.

**Bridget McGillivray:** It makes things move faster when everyone admits they don't know and we're willing to wing it and try. To learn, you have to start from "I don't know."

**Leonardo Steffen:** If you pretend to know everything, you won't learn. You end up sitting alone trying to catch up with what you told others you know.

**Bridget McGillivray:** Personally, what are some things you're working on developing—skills, capabilities, that kind of thing?

**Leonardo Steffen:** I'm trying to say no to incoming work more. Everything excites me—every project, every task. I'm trying to be more selective and only commit to what I can actually do with the time I have. I keep adding things to my board knowing I won't do them all.

**Leonardo Steffen:** So it's kind of what Daniel's going through.

**Leonardo Steffen:** And I'm, I was already thinking of hiring someone to help me, an assistant to help me with paying bills or taking care of the cats or whatever, other things that I have to do.

**Leonardo Steffen:** Like.

**Leonardo Steffen:** Yeah, but then I decided to build a bot or automate some of the tasks.

**Leonardo Steffen:** Now I have this project to take care of.

**Leonardo Steffen:** So try to be a bit more realistic to what I can do with my personal time.

**Leonardo Steffen:** know, I have X hours to work, and then I have some other hours to family and personal.

**Bridget McGillivray:** Make the most efficient.

**Bridget McGillivray:** Yeah, you sound like you're someone who's very efficiency-minded in all things, too.

**Bridget McGillivray:** So try to make the most of every.

**Leonardo Steffen:** Yeah, I did not sleep last night.

**Bridget McGillivray:** How come?

**Leonardo Steffen:** Because I had to finish.

**Leonardo Steffen:** I had work that I had to plan and finish and deliver.

**Leonardo Steffen:** And I have this little project that I'm doing here as well.

**Leonardo Steffen:** And I wanted to prepare.

**Leonardo Steffen:** For the conversation, and I wanted to just do everything.

**Leonardo Steffen:** So I did not sleep.

**Leonardo Steffen:** I drank, I don't know, a lot of coffee.

**Leonardo Steffen:** So you've been awake since yesterday?

**Bridget McGillivray:** Oh, my gosh.

**Bridget McGillivray:** I hope you can take a nap after this or just go to bed.

**Leonardo Steffen:** And this is what I do when I'm extremely excited.

**Leonardo Steffen:** And I was extremely excited last week as well.

**Leonardo Steffen:** And the beginning of the week when Tucker sent me an email, when I spoke with Daniel, it's just when something gets me excited, it's like I can't stop.

**Bridget McGillivray:** Yeah, energized.

**Bridget McGillivray:** I know we don't have too much time left.

**Bridget McGillivray:** So anything I can answer for you?

**Bridget McGillivray:** Obviously, I'm not as well-versed in anything in the engineering world in our company.

**Bridget McGillivray:** But if there's anything about the role or even the company or whatever that I can answer.

**Leonardo Steffen:** So, you know the role, and you know what, the person...

**Leonardo Steffen:** The that's to be hired for this position is going to do, right, or be able to show the role into.

**Leonardo Steffen:** What are some things that would make you or help you or you would ask if I were to join with the role that they're telling you?

**Leonardo Steffen:** What would you ask me to help you with or help Daniel with?

**Leonardo Steffen:** Yeah.

**Bridget McGillivray:** I think I see so much value in these roles.

**Bridget McGillivray:** Like, obviously, I'm biased because I've been in this kind of, like, executive leadership support role before.

**Bridget McGillivray:** But they, especially when you have such a big org and you have so many lanes going and, like, we're moving so fast and everything feels like, at the end of the day, it falls on engineering to, like, ship faster.

**Bridget McGillivray:** I think, Daniel, like, you just do carry a lot of weight on you.

**Bridget McGillivray:** To get things done.

**Bridget McGillivray:** So like the, I think the number one thing is like try to help him be more efficient in whatever way possible.

**Bridget McGillivray:** And it's totally going to change every week.

**Bridget McGillivray:** It's like you guys might get together every Monday morning and you just talk about like what absolutely needs to get done by the end of this week and how can you guys tackle it together, right?

**Bridget McGillivray:** I think one thing is like kind of forcing that question every week of like what has to get done.

**Bridget McGillivray:** Okay, great.

**Bridget McGillivray:** Daniel, it's not just on you.

**Bridget McGillivray:** Like I'm here now and I can help.

**Bridget McGillivray:** Why don't you take those two things and I'll take these two things or whatever it is.

**Bridget McGillivray:** So like every week's different, right?

**Bridget McGillivray:** Because things pop up, priorities change.

**Bridget McGillivray:** So like I personally like that about the role.

**Bridget McGillivray:** It's like, you know, you might look back at last week and be like, hey, we believe we said that was the most important.

**Bridget McGillivray:** And like we ended up dropping it, right?

**Bridget McGillivray:** Or like whatever.

**Bridget McGillivray:** You just, it just makes you be real with yourself of like.

**Bridget McGillivray:** What's important, and like, I was just talking to somebody else actually who was helping with like some of our support team stuff, but like, what he does is he runs a weekly update and it's like, what's the most important thing you have to get done?

**Bridget McGillivray:** And then like, where are you probably going to drop the ball this week?

**Leonardo Steffen:** And just like on Monday up front, but like allow yourself to, like give yourself space to drop the ball because like we're not going to get everything done when there's this many things.

**Bridget McGillivray:** I live that.

**Leonardo Steffen:** I just don't know about that.

**Leonardo Steffen:** Yeah.

**Bridget McGillivray:** So I think like, I know that's a very broad thing, but that's like the, that's the mentality to have in these kind of roles is like, how can, because if you can make Daniel even like 10% more efficient, that means you've made the entire engineering product design org more efficient, which is making the company whole more efficient, right?

**Bridget McGillivray:** So it's like thinking of wherever he is, like, he's so mission critical.

**Bridget McGillivray:** And it's not just him.

**Bridget McGillivray:** It's the whole world of EPD below him too and around him.

**Bridget McGillivray:** How can we make that a little bit more efficient every week?

**Bridget McGillivray:** And what can you take off his plate?

**Bridget McGillivray:** So some weeks it's like he might just want you doing heavy QA all week.

**Bridget McGillivray:** Another time he might want you going and looking for different vendors we should use that are more efficient.

**Bridget McGillivray:** Or maybe he wants you looking into cost stuff or who knows what it is, right?

**Bridget McGillivray:** It's like it'll change all the time.

**Bridget McGillivray:** And so I think you already have this mentality, but you very quickly develop this instinct also to be like, okay, that sounds like a nice to have for this week at least.

**Leonardo Steffen:** Like maybe next week also.

**Bridget McGillivray:** Maybe we keep kicking it down the road, but eventually it's like need to make space for that.

**Bridget McGillivray:** It's no longer nice to have.

**Bridget McGillivray:** It's become a must have.

**Bridget McGillivray:** And obviously you want to avoid thing going from like, it's nice to have to like, .

**Bridget McGillivray:** We should have done that.

**Leonardo Steffen:** But like, that just happens too.

**Bridget McGillivray:** So yeah, you'll quickly be able, once you get this feed and have the context, you'll be able to help him.

**Bridget McGillivray:** Even it's nice just having a second person like, yeah, rationalize with you.

**Bridget McGillivray:** Like, yes, that is a nice to have.

**Bridget McGillivray:** Okay, we both agree on that.

**Bridget McGillivray:** Here's why, because here's the other things we should do.

**Bridget McGillivray:** Okay, good.

**Bridget McGillivray:** We agree.

**Bridget McGillivray:** Let's like, you know, it's nice to give, like, to have a partner, a thought partner there as well.

**Bridget McGillivray:** So I think about it like that, right?

**Bridget McGillivray:** It's, it's gonna, whatever he is doing is your world.

**Bridget McGillivray:** So yeah, I got that from the conversation with him.

**Leonardo Steffen:** So apparently, the description, the job description is exactly what it is.

**Leonardo Steffen:** It's not one thing.

**Leonardo Steffen:** It's many and those many are, some are, some gonna happen more, some are gonna happen last.

**Leonardo Steffen:** And if

**Leonardo Steffen:** Everything can change in a day.

**Leonardo Steffen:** So I was writing a, last week I was writing the plan for my first three weeks of ramping myself up.

**Leonardo Steffen:** I was going to say Tucker, but I didn't because I felt like, well, this is maybe too much.

**Bridget McGillivray:** No, it's great.

**Bridget McGillivray:** I love that stuff.

**Bridget McGillivray:** Send it to, send it to Daniel and Tucker after.

**Bridget McGillivray:** Yeah, yeah.

**Bridget McGillivray:** Let's see.

**Bridget McGillivray:** Also because like we're very writing, like I mentioned this earlier, like the more we can write and share, because then you can do it stuff async, right?

**Bridget McGillivray:** If there's a lot of writing culture of like, here's what I need your input on, or here's, it's more of an FYI, here's what I'm going to do kind of thing.

**Bridget McGillivray:** And like that way people can operate in their own time as well.

**Bridget McGillivray:** Especially because we're very international.

**Bridget McGillivray:** So time zones don't always align.

**Bridget McGillivray:** But yeah, that's, that's, that's exactly it.

**Bridget McGillivray:** It's like, you will work on all of those things at some point in time.

**Bridget McGillivray:** It just depends which one.

**Bridget McGillivray:** It's like the mission critical for the week, basically, like even for the month, like literally the week or the day.

**Leonardo Steffen:** Yeah.

**Leonardo Steffen:** Oh, and you just, you said that and I'm, I'm the one who's known to be always cutting down scope of things.

**Leonardo Steffen:** Just asking, is it really important?

**Leonardo Steffen:** Is it really necessary?

**Leonardo Steffen:** So I guess that's, that's something that will help.

**Bridget McGillivray:** I, it's so often, it's like, we should do all of those things at some point and be at some, like at which point is the hard, harder decision to make.

**Bridget McGillivray:** Yeah.

**Bridget McGillivray:** You do it together and obviously there's other people involved too for lots of things, but like you think through it together and kind of like, okay, yeah, let's build conviction on it and, and why.

**Bridget McGillivray:** And then, and then you'd be able, you'll be able to go make like my, like decisions too that knowing how Daniel.

**Bridget McGillivray:** And you are aligned on how you think about things as well.

**Bridget McGillivray:** So that takes time, obviously, to get on the same page.

**Bridget McGillivray:** But then it means he can have like a mini, like a force multiplier elsewhere.

**Leonardo Steffen:** Mini Daniel.

**Bridget McGillivray:** Mini Daniel.

**Bridget McGillivray:** Awesome.

**Bridget McGillivray:** Well, I do need to go, but it was so nice to meet you.

**Bridget McGillivray:** I'll just check in.

**Bridget McGillivray:** Have you already talked to GP?

**Bridget McGillivray:** Or is that later?

**Bridget McGillivray:** Yeah, I did.

**Leonardo Steffen:** Yeah, it was really good.

**Leonardo Steffen:** Okay, cool.

**Leonardo Steffen:** Oh, right.

**Bridget McGillivray:** Well, then I'll just check in with them and let them know how our convo went.

**Bridget McGillivray:** And then I'm sure Tucker will be the one to get in touch about next steps.

**Bridget McGillivray:** Or I'm not sure if he has any plans for any more steps or not.

**Bridget McGillivray:** And we can go from there.

**Leonardo Steffen:** Okay.

**Leonardo Steffen:** Thank you, Bridget.

**Leonardo Steffen:** Yeah, awesome.

**Bridget McGillivray:** great week.

**Leonardo Steffen:** And thanks for your time.

**Leonardo Steffen:** Thanks for the conversation.

**Leonardo Steffen:** Thanks.

**Bridget McGillivray:** Bye.

**Bridget McGillivray:** Cheers.
