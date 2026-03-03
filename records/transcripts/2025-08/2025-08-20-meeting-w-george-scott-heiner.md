# Meeting w/George (Scott Heiner)

<metadata>
date: 2025-08-20
time: 22:07 UTC
duration: 78 minutes
organizer: George Haikal
participants: George Haikal, Scott Heiner, Aida Knežević
fathom_recording_id: 81921199
fathom_url: https://fathom.video/calls/387056345
share_url: https://fathom.video/share/GZv13ugusFx3eduup5HwLBXcJijZ24gy
source: fathom
enriched_on: 2026-03-03 12:45 UTC
</metadata>

---

## Summary

George Haikal (GrowthX) and Scott Heiner (Surge AI) mapped out a comprehensive narrative for explaining Surge's end-to-end process and technology platform to customers and prospects. The meeting covered Surge's three core competitive pillars—proprietary platform technology, expert internal team, and curated workforce—demonstrating how each layer contributes to rapid project delivery and quality assurance through multiple data signals. The key challenge identified is balancing transparency about processes without creating decision paralysis: customers need to understand Surge's sophistication without getting lost in quality-control minutiae, while Scott emphasized that the real differentiator isn't just the technology or the experts or the workforce alone, but the combination of all three.

---

## Context

George Haikal reached out to Scott Heiner, Surge AI's co-founder, to develop a v1 narrative for how Surge works—a critical need for GrowthX's messaging work with Surge. Aida Knežević from GrowthX Labs was invited but remained silent throughout the call. George and Scott are collaborating to surface Surge's operational complexity and translate it into compelling customer and prospect-facing communication. The backdrop is a broader challenge Surge faces: historically being "vague and quiet" about its process, leaving customers potentially undervaluing what they're actually getting for the premium they pay.

---

## Relevance

**To GrowthX Delivery:**
- Messaging framework for Surge's operational sophistication—three pillars (platform, internal team, workforce) with multiple quality signals embedded throughout
- Opportunity to position Surge differently from commodity vendors (like Mercore) and other platforms that lack rapid UI creation capability
- Key positioning tension: emphasize technology without underselling the human expertise and workforce management that make the platform valuable

**To GrowthX Business Development:**
- Expansion potential in explaining Surge's quality control and data reliability to new prospects—clear articulation of "why our data is better" beyond just "we have experts"
- Renewal/upsell angle: customers who understand the full process (workforce filtering, honeypot testing, peer review, session playback, AI detection, rejection rates) are less likely to leave or downgrade

**To CheckThat / Product:**
- Surge's native LLM integration for real-time task validation and quality checks is relevant to CheckThat research on AI governance and validation frameworks
- Reference for how platform companies embed AI into workflow—applicable to CheckThat's own product positioning

---

## Overview

- Surge AI's competitive edge stems from three core pillars: proprietary technology platform, expert internal team, and curated workforce of "Surgers"
- Platform enables rapid UI creation, workforce management, and quality control through multiple data signals and review processes
- Balancing transparency about processes with focus on end results is key challenge in customer communication

---

## Key Topics

### Surge AI's End-to-End Process

- Customer submits data request (e.g., finance experts writing LLM prompts for SEC filings)
- Internal team creates tailored instructions and UI using Surge platform (typically within 1 day)
- Project launched to filtered subset of Surge workforce
- Multiple quality control measures applied (e.g., LLM helpers, review scores, time analytics)
- Data reviewed internally and by selected Surgers before delivery to customer

### Technology Platform Advantages

- Rapid UI creation (hours vs. weeks for competitors like Mercore)
- Native LLM integration for real-time task validation
- Sophisticated workforce filtering and management tools
- Extensive quality signals and analytics (e.g., Surger profiles, review scores, time spent)
- Ability to "impersonate" Surgers to understand their experience

### Quality Control Measures

- Multiple data signals used to evaluate Surger performance:
  - Time spent on tasks
  - Peer review scores
  - Performance on "honeypot" tasks with known answers
  - Historical rejection rates
  - Review behavior when evaluating others' work
- Session playback for detailed work analysis
- AI usage detection to ensure human-generated content
- Internal review process before customer delivery

### Workforce Management

- Curated teams of experts across various domains
- Detailed Surger profiles with performance metrics and work history
- Ability to quickly assemble specialized teams (e.g., "coders in the UK with 5+ years experience")

### Customer Interface

- Access to high-level project analytics
- Raw data delivery via CSV, JSON, or API
- Limited visibility into internal quality control processes

---

## Action Items

**George Haikal (GrowthX)**
- Package and communicate Surge's work process (tech platform, internal experts, workforce) for customers and prospects. Balance detail vs. vagueness to help customers understand quality without getting lost in process minutiae.

---

## Transcript

**George Haikal:** This meeting is being recorded. And so I think there's two best ways to do it. And you let me know which you'd prefer. I think first, like overall, and based on the meeting we had today, like getting to a version one of how Surge works, right? We already kind of covered the customer process from onboarding to actual delivery. But I guess the how we work from the platform side, how you use it and leverage it and at what stages, as well as the Surger process. How you evaluate them, how they're delivering their work, what they're seeing on their end. I think those are two things that I want to dive deep on. And then we can put together the entire story. So that's the first part is the story, then the second is the value props and differentiators of your tech and then showing it. I'm assuming a lot of it's through the platform. So it's like showing us how it works or how you'd normally run the process through it. That's kind of the two things that I was thinking.

**Scott Heiner:** Okay, that sounds good. Let me start with maybe an end-to-end demonstration of what it looks like when a customer makes a specific request for data, how we use our platform to produce that data. And then that will tie in also to what the Surger themselves sees.

**George Haikal:** Does that sound good? Sounds fantastic.

**Scott Heiner:** All right. Let me pull up. (Audio check on headphone setup with George) I'll show you what a customer request looks like.

**Scott Heiner:** This is a verbatim customer request. So this is them. They want some data from us. This is what they send to us. So what they're telling us is we like some raters, aka Surgers, with a background in finance. We want them to write prompts that you write to a large language model, attaching an SEC filing like a 10K or 10Q. And asking a question about that. So we just want the prompts here. And we want the human, the Surgers to write what the ideal answer would be. So that's the task at hand. We have to go out and find people that have a background in finance, have them find SEC filings, which they give a little bit of instructions on how to actually go find the documents they're looking for. And then ask questions about those SEC filings. And then also supply that correct answer to those questions. They have a couple different categories of questions they want people to ask.

**George Haikal:** So this is a fairly straightforward request, but this is verbatim what we've gotten from a customer in the past.

**Scott Heiner:** That's all we get from them. And sometimes it's even less detailed than this, sometimes way more, but let's call this an average amount. From there, we need to use our platform to spin up a UI and interface that lets Surgers complete the task and ensures data quality is high. The core thing that the Surge platform does is it allows us to spin up these labeling UIs super quickly to gather exactly what the customer is looking for.

**George Haikal:** And to be clear, this is like one of the main differentiators—it's the access you have to these experts, and how streamlined the process is.

**Scott Heiner:** Yeah, it's the streamlining of the process, and it's the combination of we have a very powerful platform and we have access to all the right people. In some ways, the UI creation part of our process is not that dissimilar from a Google Form Creator—you're picking and choosing questions, but it's made for labeling Gen AI data. I'll show you the finished project first. Basically, on the left we have all the instructions that someone on our team wrote to tell the Surgers what to do. You can't just take the brief—you have to look at it and anticipate all the ways people are going to mess it up. There's a requirement that you can only use documents from October 23 or later, and I can see people messing that up. So you have to write your own instructions to address that.

**George Haikal:** And how long does that take?

**Scott Heiner:** Creating the instructions and setting up the UI should take a day or a couple hours. Karina, one of our team members, wrote all these instructions, explaining the different types of prompts we need, documents to use, various important reminders—basically a spruce-up version of the brief. We get examples of what's good, what's bad, what to avoid. Over here on the right is our form interface: company name, filing date, all very basic. We have validation to ensure dates are in the right format, regex stuff. Here's where your prompt goes, here's where your ideal answer goes, and you're off to the races. It's unsexy but effective. We're writing instructions, putting together UIs, launching to Surgers. They see exactly this and fill it out.

**Scott Heiner:** Where it gets interesting is we have our own platform. Some companies like Mercore don't—they have to send people to the company's platform, which is really hard to use and takes weeks to set up something we create in a few hours.

**George Haikal:** Is that your answer to someone saying "I just want five Harvard lawyers in three hours"?

**Scott Heiner:** We can give you five Harvard lawyers in three hours, but where are they going to do the work and how do you know it's actually good? The platform is what lets us answer those questions. Scale had a platform too, but it was worse—harder to collect good data, harder for workers to get paid. The hardest thing to explain, but most important, is why this platform produces higher quality data than just using Google Forms or spreadsheets. Why can't you just take three Harvard lawyers and put them on a spreadsheet? What's the value add? There's no single answer—it's the signals thing. We've built many different signals into the platform that let us determine if someone is doing good work.

**Scott Heiner:** For example, we can call out to any large language model natively. We have LLM helpers that look at the document you uploaded, determine if it's a 10Q or 10K, check if the date is correct, verify the metadata is right. This AI thing helps make sure people are actually doing work well, and it's happening for the Surgers themselves—they press the check documents button. Their platforms don't have this, and they're not going to set it up for every project.

**George Haikal:** So you're evaluating Surgers against that too—if they get items wrong and have to redo them?

**Scott Heiner:** Yeah. We can see how often they're using it and what the results are. Although in this case it's hallucinating, but assuming it wasn't, yes, we track that.

**Scott Heiner:** So anyway, we end up launching this project. We launch this project, and it goes out to a team, a specific team of workers on our platform. So we have all these teams of sets of people on our platform—the scientists, the mathematicians, the coders, the poets, the bakers, the people in Australia, the people in the UK, and we can intersect them in any way. It's like, God, we need coders in the UK who have at least five years of experience in the real world. So it's super fluid from that perspective, and we have other ways to very easily filter our workforce. Like, this is our workforce page. We could say, hey, I want to see everyone that is a member of this top coders team. So everyone that's a member of that and signed up before a certain time and their average review score is above this on these certain projects and they're from this country. So it allows us to query all this super easily and get the best team for any given project, right? We can see how much money people have earned, if they're currently working, all this stuff. And so, again, I don't think other platforms have this in any way like we do. So it's very easy for us to filter our workforce to the absolute best people for any given project.

**Scott Heiner:** Okay, so we launched the project and then I'll go to the Surge review in a second. But essentially, they see a dashboard just like I am looking at a dashboard of lots of different projects that people on our team are running. It looks very similar to the Surger dashboard. They're seeing a bunch of projects that they could work on with their pay rate, what they might want to do. They're seeing these titles right here. So if I'm a worker, I see this project was launched. It's paying $27 an hour. I go and I do the tasks. And then on our side, we are watching the results come in. So this is our results viewer, which customers can see. And this is basically a table of all of the submissions that we're getting and all the data in there. So the company name, the filing date, the prompt, the answer, and all that stuff. So that's how we're viewing the data. And then basically, we just have a ton of signals that we can look at to help determine if the data is good or not. And this is one of the challenges we're going to have. There's no one thing here. It's a bunch of different stuff we're doing that—each thing on its own was maybe not that interesting, or maybe it is, I don't know, maybe we can make it interesting. But combined together, it's a super powerful thing.

**George Haikal:** So I'll give you some examples.

**Scott Heiner:** So we have a page called Surger Analytics. And the analytics are telling me, for each person here, how many responses did they submit in this project? How many have we rejected so far? So we may manually look at it and say, this isn't any good. So how many have we rejected? What was their median time spent on this project? Their review score, if it was reviewed by other people, which is another quality signal. And then how do they fare against the sort of the average for the rest of folks in the project? So here we can quickly see outliers on like, hey, who are the people that are taking the most amount of time? Who are people that are taking the least amount of time? That in and of itself doesn't actually tell you if they're good or not. They can be taking a ton of time because they're scamming you or they could be taking a ton of time because they're really freaking good. Thoughtful, yeah. Right. Or they could be taking no time because they are rushing through this, or they could be taking no time because they're brilliant, and this is easy. So, again, it's not no one signal is going to tell you exactly how this works. But when the culmination of them all becomes really, really powerful.

**Scott Heiner:** Here's another thing. I can go to, let's go to Benjamin Baker's profile. So I click into his profile. And I'm going to see a ton of information on Benjamin Baker that also allows me to understand who the heck this guy is and whether I should trust his work. So I can see how much he's earned lifetime on the platform, how that relates to other workers. I can see how long he's been on the platform. I can see the number of teams we've put him on. So how many teams have our internal people put him on? And I can see which of those have been marked as low-quality teams versus high-quality teams. I hover over this, and I can see, okay, this guy's actually been removed from eight different teams. He's been removed essentially, saying we don't want to work with this team anymore. And if I'm looking at it, I see a bunch of different codenames. I see Volps and Bonito and Tide and Meta and Zebra. Okay, he's basically worked on most of our clients, and he's been removed from a team on almost all of them. That makes me a little sus of what's going on. But then I have other metrics. He has had 878 of his tasks reviewed by other Surgers, and his average score is 76, which is decent. On other, we have these honeypot tasks that we insert into the projects where we have a known answer, and we test if people can get the known answer correct. He's got 95% of that. That's pretty good, too. We can see that in his lifetime, we have rejected 12% of his work. That's pretty interesting. We can see that when he reviews other people's work, he usually gives, on average, a score of 80%, which is not a good sign. It basically means that he is not being critical. He's probably rubber stamping stuff. And then we can see every project he's ever participated in in his lifetime. And we can go over here for a sample of his work and just look at directly his work on a bunch of different projects that he's done. We can see all the messages he's sent in chats to us, which is zero here. We can see what projects are currently available to him on his dashboard. We can see all the gold standards. These are the honeypot questions. We can see his responses to all of those. We can go to his LinkedIn. We can read his bio. And so we have all this really rich information about him. If we want to, we can also, asking your question around their view, can impersonate him. So now this is exactly what Benjamin Baker sees. These are all the projects on his dashboard. I mean, he has like 50 things that he could work on. And he could click into any of these and, you know, start doing the work on that.

**Scott Heiner:** So at a project level, we have all this information about all the work being done on our finance project. And then we can also see all this user-specific information. We can also go back and watch his sessions, like every keystroke he makes on the platform. And then we have some off-platform quality analytics, too. Like we have certain dashboards that are looking at how likely it is that any given person is using AI a bunch to do their work, which we don't want because we need human work. So there's probably even more than that. But that's like all the quality signals that we are combining to determine, like, if we should trust someone's work, how much scrutiny to give them. And then also there's just a ton of we're going to look at a lot of the data ourselves.

**Scott Heiner:** So we've gotten these 30 responses here, 30 responses. And what we did, what Karina did in this case, was she launched what we call a review project, which is now she's sending out the same responses to be reviewed by other people, maybe we select other Surgers, any team of Surgers we want. So it could be one way we could do this is I collect these 30. I look at some of the results myself and I pick out three people that are doing phenomenal work. I make them my review team and I send this review to those three people. And I say, look, I trust you guys because I saw how good your work was. And now whenever we run this project, I want you three to look at everything we do. Like that's one way to do it. There's other ways to determine who's going to be the review team too. But so those all get reviewed. And in the results viewer, we get these review scores. So this is the checkboxes score up to 100, basically a thumbs up. This line is basically medium, 50%, like take it or leave it. The X is, this is not good. So we've gone through this data set and selected, there's like. This one has the X, like something about it is wrong. We're probably just going to reject it, so we can reject this. That goes kind of against this little mark against Benjamin on his record. And we go through this to make sure this is all looking really high quality. And then we ship it off to the customer, and they see something similar, minus they don't actually see like our review scores and our review process.

**Scott Heiner:** So, and that's the end of the process. Like we send this data set off, they see it. Actually, I can just show you exactly what they see. This is the customer view now. So they basically see the title of the project, some high-level analytics when they're available. And then the raw data set, they can take it off our platform in a CSV or a JSON, or they can do it via the API. And that's basically the process. The thing that we have historically been very quiet about and very vague about is—is what is going on between when you guys get a spec and when you deliver this data back to us? Like customers, they understand we have a platform. They may understand that we're going to write some instructions for them. They may understand that we are going to put together a team of the top workers and make sure that it's like the right people are working on the project. But what is everything else that Surge is doing to be great?

**Scott Heiner:** And in the past, we've been hesitant a little bit about that because it's for sure true that as soon as you start sharing any type of detail, people just want more information. They want to nitpick your process and they start looking less at the end result, looking at this actual data and being like, great, this is exactly what I was looking for. And they start questioning the process like, well, did you get it reviewed by one person each or two people each? What happened if one person said it wasn't good, but one person said it was good? And we're basically like, dude, don't worry about any of that. We're going to do all that work and then you're going to see something great at the end of the day. Of course, the downside here is that if they don't know what we're doing, they can't really value it. Because as much as we want everyone to be looking at data and saying, oh, my God, Surge did such a great job, the only way you can know that we did a great job here is to actually, like, take 15 minutes out of your day, read these prompts, read these answers, maybe go look at the filing yourself and be like, oh, they got the answer right. Like, there's no objective one single thing that instantly is just like, cool, like, this is perfect. It's all kind of vibes-based. So that's where, like, I don't know, McCord gets points for having their McCord doxing or something because they're demonstrating externally. We know what we're doing. We're being really thoughtful about this. Whereas there's probably some people that have spent tons of money on us that are like, I have no idea how Surge does it. Maybe some people like that. Maybe some people are like, what am I paying for?

**George Haikal:** Really, really, really helpful. And I think there's, I mean, we both know there's somewhere in between of the silence and open sourcing everything where this how we work can be communicated in a way. Like, language is a little more vague, but still super impactful. So that's what this meeting was for. I think I got plenty of information. Like this was super detailed. So I appreciate it. And now it's on us to go figure out, okay, how do we package and communicate this? I guess, is there anything else that sticks out in terms of evaluations, quality checks, differentiators in this last minute here that you've got to call out?

**Scott Heiner:** I think that the thing where Edwin's always been really interested in positioning us as a technology company, and I totally understand why. We don't want to be seen as just another BPO-style vendor that has a bunch of people working in spreadsheets. I totally get that. And then there's a flip side of that, which is, but also part of our secret sauce is not just the human element of the Surgers, but it's our FTEs, honestly, who are overseeing this whole process and steering it. And every data collection is unique in some way. And so you need this, like. That has really good intuitions, can look at data and instantly know whether it's good or bad, and then can use our tools effectively to create really great data. And so I think there's a risk of, like, if we do this correctly, what customers and the public at large would come away with is, Surge has amazing technology being leveraged by geniuses, basically. And it's not just, oh, if I just bought this technology, I could just do this myself. If I could just build this technology, I could just do this myself. Or if I just hired geniuses, I could do this myself. I think it's really, like, the combination there of, like, you're not just paying for our tech, you're paying for, like, our genius. And part of the genius is we've built this amazing tech.

**George Haikal:** So that's going to be a little even including the access to experts at scale.

**Scott Heiner:** Not even that. Like, that's, like, the third piece of it. It's, like, our technology, our super genius internal folks, and then our amazing workforce. And those three things together allow us to produce this amazing data. And, yeah, I don't know that that message is out there at all right now. So that's what I would like to get across.

**George Haikal:** Thank you for the masterclass, man. I know you have to jump.

**Scott Heiner:** I know you have to jump.

**George Haikal:** Yes, sir. No problem. It was great. Awesome, man.

**Scott Heiner:** Appreciate it.

**George Haikal:** Let me know if you need anything else.

**Scott Heiner:** Appreciate it, Scott.

**George Haikal:** Have a good one. (End of call)
