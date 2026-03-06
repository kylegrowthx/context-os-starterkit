# Daniel / Marília / Tucker 

<metadata>
date: 2025-03-12
time: 20:31 UTC
duration: 34 minutes
organizer: bridget@growthxlabs.com
participants: Daniel Lopes (GrowthX), Tucker Barker, Marília Caroline da Silva (GrowthX)
fathom_recording_id: 51610245
fathom_url: https://fathom.video/calls/250843679
share_url: https://fathom.video/share/aEgCjckQ6zWaEVumzVcb5FMXoxRyUYny
source: fathom
enriched_on: 2025-03-04 14:30 UTC
</metadata>

---

## Summary

Daniel walked Marília and Tucker through GrowthX's recruitment system—an AI-powered hiring workflow built on AirOps, Workable, and custom evaluation prompts that handles high-volume applications (700+ for content writer roles, 10-15/day for engineering). The team is exploring a new office with event space on the first floor and 10-15 desks on the second floor, and discussed whether to migrate to Greenhouse ATS as hiring scales. Tucker is starting officially April 7th and will explore sourcing workflows with their recruiting partner; Marília (day 3) will evaluate the system hands-on and help customize evaluation rubrics.

---

## Context

This is an onboarding and process walkthrough for two new GrowthX hires: Marília Caroline da Silva (GrowthX employee, day 3) and Tucker Barker (joining officially April 7th but starting part-time now). Daniel Lopes leads recruiting and built GrowthX's current system to solve a problem: after switching from staffing agencies, they discovered that high-volume applications (hundreds to thousands per role) made manual screening impossible. The recruitment workflow Daniel designed uses AI to standardize job descriptions, evaluate resumes and application answers against role-specific rubrics, and screen video interviews—reducing noise while surfacing qualified candidates. Tucker asked about ATS flexibility, noting his preference for Greenhouse; Daniel indicated the system is platform-agnostic and could migrate in about half a day. The session also included planning for a new two-floor office space that would serve both events (first floor) and local team coworking (second floor).

---

## Relevance

**To GrowthX Delivery & Operations:**
- New office setup (two-floor: events + coworking) will enable meetups and partner collaboration, supporting content marketing funnel and community-building initiatives
- Recruitment system documentation and tutorial will be key onboarding materials for Marília and future hires; Daniel is dedicating time to document the full process
- Current hiring volumes are unsustainable for manual screening: 700+ applications for content writer in 4 weeks; ~10-15 quality engineering applications/day after AI filtering

**To GrowthX Business Development:**
- Testing premise that AI-powered evaluation surfaces better candidates while reducing bias; early signals show strong applicant quality, especially for services roles
- Opportunity to explore automated sourcing via API integrations (Marcus has bandwidth) to supplement current inbound volume
- Office space positions GrowthX for events, partnerships, and scaling team presence in-person

**To Hiring & Scaling:**
- ATS migration decision pending: Tucker favors Greenhouse for scaling; Daniel open to evaluation and migration (low effort). Cost comparison and feature comparison needed before deciding
- Potential to replace or supplement Workable; system is designed to be platform-agnostic
- Tucker will connect with Quantum (recruiting partner) to streamline workflow, reduce manual uploads to Workable

---

## Overview

- GrowthX is exploring a new office space for events and coworking
- Current hiring process uses AirOps, Workable, and custom AI tools for candidate evaluation
- High volume of applications (100s-1000s) for some roles necessitates automation
- Team is open to adjusting or replacing current tools (e.g., considering Greenhouse ATS)

---

## Key Topics

### New Office Space

  - Planning for a two-floor setup:
      - First floor: Event space for meetups and partner companies
      - Second floor: 10-15 desks for local team members and temporary collaboration

### Onboarding Progress

  - Marília: Day 3, still getting up to speed
  - Tucker: Part-time until April 7th, focusing on understanding the business

### Current Hiring Process Overview

  - Uses AirOps for job description generation and workflow management
  - Workable as the main ATS (Applicant Tracking System)
  - Custom AI tools for resume analysis and application question evaluation
  - Pyroflix for video interviews (chosen for transcript API capabilities)

### Automation and AI Integration

  - AI-powered ranking system for initial candidate screening
  - Customizable prompts and evaluation criteria
  - Automatic disqualification for "maybe" or "no" candidates (under review)
  - Slack integration for team notifications on new candidates

### Application Volume

  - High volume for some roles (e.g., 700+ for content writer in 4 weeks)
  - Engineering roles: \~10-15 quality applications per day after AI screening

### Potential Process Improvements

  - Considering migration to Greenhouse ATS for better scaling and features
  - Open to adjusting or removing current automation tools based on team needs
  - Exploring possibilities for automated sourcing and custom integrations

---

## Action Items

**Marília Caroline da Silva (GrowthX)**
- Review Workable system hands-on tomorrow; evaluate current recruitment process and provide feedback on customizing evaluation rubrics

**Daniel Lopes (GrowthX)**
- Document recruitment process in detail; write written tutorial for Marília and Tucker on current system, including how to customize questions and evaluation criteria

**Tucker Barker**
- Connect with Quantum (recruiting partner) to explore efficient recruitment workflow; discuss whether to eliminate manual uploads to Workable

---

## Transcript
**Daniel Lopes:** We found a nice place that I think we can do off-site and five people in the first floor will be like for events so we can host a bunch of meet-ups and stuff for other companies and partner with other companies and be more like an event space and then the second floor have like 10 or like 15 desks just for some of the local people and have the place for five people in and work together for a few days.

**Daniel Lopes:** Events are a main driver for leads—I organize one every month and it's a good investment.

**Daniel Lopes:** How's it been so far for both of you? Have you had some onboarding sessions already?

**Marília Caroline da Silva:** Yes, I'm still getting up to speed. Today's day three, so there's a lot to learn, but it's been great so far.

**Daniel Lopes:** What about you?

**Tucker Barker:** My onboarding is totally different since I'm just doing a couple of hours a day. Bridget and I have been catching up and trying to dial some things in.

**Tucker Barker:** I'm diving into the material—from my side, I want to know as much about the business as possible. Why do we do what we do?

**Daniel Lopes:** That way when you start talking to candidates, your pitch will be much better. Yeah, that makes sense. We can talk about that next week in our scheduled meeting.

**Daniel Lopes:** Let me walk you through the recruitment process. Bridget wanted me to give you both an understanding of how it works. What we have today is not set in stone—it's just what I came up with to handle higher volume on the services team. Let me back up a bit.

**Daniel Lopes:** When I joined, we were relying on agencies for staffing. Some placements were great, but most weren't. The issue wasn't just the pipeline—it was inconsistent job postings. Sometimes bad candidates came through simply because the job description didn't make sense. So I rethought the whole process and standardized how we generate job postings and describe what we're looking for.

**Daniel Lopes:** For the services team especially, we get a lot of great people applying—but with high volume, great candidates can slip through the cracks. Even with the system, we need someone to review and help calibrate. But this is what we've had so far. We can change anything—remove tools, swap systems, whatever works best for you.

**Daniel Lopes:** Let me walk you through the process. We use the same approach for marketing workflows. We have a tool called AirOps. You should both be added to it so you can see the work we do on the services side. Our programmers maintain it. Over time, we're transitioning to a platform we own, but we're still building that.

**Daniel Lopes:** In AirOps, we have a GrowthX folder with client names and a job openings grid. When you create a new role, you enter the job title, salary range, and a rough job description—doesn't have to be super detailed. Then the workflow generates a job expectations document. For example, for a head of talent role, it would generate broad qualifiers. You can customize this heavily to make it really refined.

**Daniel Lopes:** And it also, so from this, the job expectations is one of the things we use when we're evaluating the candidates that come to workable.

**Daniel Lopes:** So everybody that applies to workable, they have to answer application questions.

**Daniel Lopes:** So it's like, depends on the role, but it's like maybe three to four application questions.

**Daniel Lopes:** They have all the resume, the resume is mandatory.

**Daniel Lopes:** we run them through two checks.

**Daniel Lopes:** One check is how much of a fit they are based on the questions and based on the job expectations.

**Daniel Lopes:** So we're going to use this document here to see if the candidate, the resume, and the answers match that.

**Daniel Lopes:** And if they match really high, we'll have like a higher grade workable.

**Daniel Lopes:** So if this is like completely miswritten, it will not work.

**Daniel Lopes:** So, then the next step is the interview process.

**Daniel Lopes:** So the interview process,

**Daniel Lopes:** I'll show you in work.

**Daniel Lopes:** We're just like walking through the spreadsheet, how I would post a new job.

**Daniel Lopes:** Like I was saying, we don't have to use this.

**Daniel Lopes:** can just do everything.

**Daniel Lopes:** But then we have two steps.

**Daniel Lopes:** One is the resume analysis.

**Daniel Lopes:** Read the PDF and decide if the PDF is a good fit or not.

**Daniel Lopes:** The PDF of the resume.

**Daniel Lopes:** another one is the questions.

**Daniel Lopes:** Read each question and see, I have a rubric for each question.

**Daniel Lopes:** So you control the rubric and you control the resume rubric as well.

**Daniel Lopes:** So like this step here person, we're going to do like a designer role.

**Daniel Lopes:** We want to do like a product designer.

**Daniel Lopes:** Let's say salary is, other is not using for anything in the grid now.

**Daniel Lopes:** So I can just leave it free.

**Daniel Lopes:** But let's say, for example, I was looking at a job posting from base camp today, there's haven't seen us there.

**Daniel Lopes:** They just posted a design and I think the job description was pretty spot on.

**Daniel Lopes:** with what I wanted for the first designing.

**Daniel Lopes:** So I'm just going to copy this, but let's say we have one, or it doesn't have to be as detailed like that at all, could be like four paragraphs.

**Daniel Lopes:** So around this, I duplicate the description of what our company does.

**Daniel Lopes:** When I run the workflow in AirOps, there's an execution URL that sends a request to our backend to process the job expectations document. I'm recording this walkthrough so I can send it to you.

**Daniel Lopes:** The output shows expectations for the role—broad qualifications, minimum years of experience, tech skills needed—all based on that job description. I'd customize this and paste it into Notion. We store all job expectations in our Notion hiring workspace under an employee handbook folder. Each role gets a document with the job expectations.

**Daniel Lopes:** We don't stay in AirOps long-term—it's just for setting up the rubric. Then we move everything to Notion, and our evaluation workflows read from Notion. That way you can constantly change and adapt things. Here's an example for a managing editor role. The URLs are public but not hosted anywhere, so people can't find them—they're public for API consumption only.

**Daniel Lopes:** After we generate the job expectations, the next step is to generate interview evaluation rubrics. The two main things we evaluate are resume analysis and application question analysis.

**Daniel Lopes:** For resume analysis, we define what we're looking for—technical experience, soft skills, company culture fit. For a managing editor, that includes writing quality, publication experience, and journalism background. For programmers, it's tech stack knowledge and whether they're founders. For designers, it's design tool proficiency, HTML/CSS, front-end frameworks like Tailwind, accessibility expertise, prototyping tools—basically everything in the job description.

**Daniel Lopes:** Then we create an evaluation rubric. We categorize all the application questions and define what we care about. For a designer role, that might be: design process and problem solving, UI and UX execution, technical competence with front-end skills, communication (since we're remote and async), project management, and accessibility. That's six categories. For every question a candidate answers, we see which category it fits and what we're looking for. You can rewrite these categories as much as you want.

**Daniel Lopes:** The workflow also generates question ideas based on those categories—questions you could actually ask in the application. When you post a job, you copy the job description to Workable, grab the application questions from the workflow, and add video interview questions to Pyroflix. All applications get automatically ranked. That's the flow.

**Daniel Lopes:** It also has some other suggestions, but this is we're not using for anything.

**Daniel Lopes:** So these are suggestions for ideas for take-home assignment.

**Daniel Lopes:** With the take-home assignment for the design, it could be a greater low fidelity, a wider frame, and then some other things and maximum time and whatever.

**Daniel Lopes:** The workflow also generates ideas for live phone screen questions—those suggestions are available if you need them. That's the gist of it.

**Daniel Lopes:** In Workable, it's pretty straightforward. We have so many applications that without ranking, people fall through the cracks. Currently we auto-disqualify "maybe" and "no" candidates, but with you two helping, I'm not sure that's a good idea anymore. Those "maybe" candidates often include great people—the AI sometimes misses them. If you spend time refining the prompts, the top-ranked (green/star) candidates are usually really solid.

**Daniel Lopes:** When you review a candidate in Workable, you see an AI assessment that explains why they got that rating. You can see their key strengths, areas of concern, potential next steps, and seniority assessment. All of this also posts to Slack. We have separate channels for the services team and engineering/product team, and everyone gets these notifications so they can jump in if they want to review profiles.

**Daniel Lopes:** All candidates go to "Applied" first. If they complete a video interview, they stay in the Applied section—we don't automatically move them to Assessment or Video stages. We control the ranking completely, so you can change anything: add steps, remove steps, customize prompts. Whatever works for you.

**Daniel Lopes:** For video interviews, we use Pyroflix. We chose it specifically because it has a transcript API, so we can process the interviews. If you don't think video screening is necessary, we can remove that step entirely.

**Marília Caroline da Silva:** So video interviews are moved manually?

**Daniel Lopes:** Yeah, you move them manually. When you do that, nothing happens—they don't get any emails, they just appear here. The tool we use is Pyroflix. It's not perfect, but it's the only one I could find with a transcript API for processing. One annoying limitation: you can't send video interviews in bulk from Workable. You have to go one by one. But whatever you think is the right flow, we can remove, add, or change.

**Daniel Lopes:** When candidates complete a video interview, we evaluate it the same way—scoring them as recommended, good (green), maybe, or no, with reasoning. That's the whole process. Does that make sense? Will that help you understand how to organize things?

**Daniel Lopes:** I can make it less technical if you want, and I'll give you access to all the documents so you can customize the prompts and everything.

**Daniel Lopes:** I think we can have all of them in Ocean and...

**Daniel Lopes:** What your thoughts?

**Daniel Lopes:** Like I said, happy to remove everything.

**Daniel Lopes:** The main thing that we experienced is just the amount of people we got in bound, and a lot of them are actually really, really good.

**Daniel Lopes:** So some of our best people are in bound, especially for the services team.

**Daniel Lopes:** And even for the programmers, there are some really good people that actually, the only reason why I didn't follow through so far was because I didn't have the whole rubric done for the interview process that I'm starting that I saw essentially two weeks ago.

**Tucker Barker:** So I wonder, it's obviously going to be so different for each side, right?

**Tucker Barker:** I'm curious.

**Tucker Barker:** I haven't gone into the depths of workable yet of how many applicants were getting for each image role.

**Daniel Lopes:** For programmers, the volume is more reasonable because we only post on Workable's automated job boards and We Work Remotely—two places. We're getting about 10-15 quality applications per day after AI filtering. It's doable to screen manually for programmers.

**Marília Caroline da Silva:** Workable's ranking is not great.

**Daniel Lopes:** For other roles, it's completely different. For example, the content writer role posted four weeks ago got 700 applications. Depending on where we post, we can get anywhere from 15 to 100+ applications per day. It really depends. For the services team, I didn't initially find the best job boards or communities—I was mostly relying on Workable's LinkedIn automation, and we don't even have a dedicated LinkedIn recruiter. If we did, we'd get even more volume. There's no way to manually screen 700+ applications.

**Daniel Lopes:** This system doesn't have to be exactly what we have, but you need some automation to handle volume. That's our philosophy: anything that can be done with AI to make your life easier, let us know. We have developers like Marcus who has bandwidth and isn't fully allocated. If you want automated sourcing, API integrations with specific job boards, or anything else—it's a half-day effort. Recruiting is critical for growing the services side, which is the core business. For programmers, it's less urgent since the pipeline is good.

**Tucker Barker:** I love the idea. There will be certain roles in the future where this automation will be handy. For now, it's a small pool—I can review 50 to 100 profiles a day no problem. But Marília, your experience will be totally different with way more profiles to evaluate.

**Marília Caroline da Silva:** Yeah, definitely.

**Daniel Lopes:** And then what roles do you need to evaluate?

**Marília Caroline da Silva:** I still need to evaluate how it works, like probably I'll have my hands on it tomorrow, if possible.

**Daniel Lopes:** Yeah, yeah.

**Daniel Lopes:** I will organize things a little bit more and I will describe the documents and like I was depending on the hour on this and give you a tutorial, a written tutorial so you can follow the whole thing and if you want to start customizing the questions and everything you calibrate the rate based on all your customers.

**Tucker Barker:** One question for later: how much of this depends on Workable specifically? Is it all built for Workable, or could we integrate with a different ATS?

**Daniel Lopes:** Super easy to migrate. We have an API client that talks to Workable—it's simple, and migration would take about half a day.

**Tucker Barker:** That's good to know. I'm biased toward Greenhouse—I think it's the best ATS out there. I'd look at pricing too.

**Tucker Barker:** Workable is probably more cost-effective, but Greenhouse scales better for recruiting and has great job board integration.

**Daniel Lopes:** I've used Greenhouse before, and also Lever. I heard good things about Hibob too. If both of you prefer Greenhouse, we can definitely evaluate it. I'm happy to check pricing. If you want to keep using Workable, I can write a tutorial. Either way, we have the resources to help with whatever is painful for you. Long-term, we need to scale hiring regardless, so it's worth getting this right.

**Daniel Lopes:** The main issue with Workable's native AI features is that you have zero control—it's all black boxes. I want to decide what I care about in each question, set those criteria, and control the evaluation. It's the same problem with marketing tools: features come as black boxes with no customization. Ideally, we want an AI assistant that handles the boring parts but lets us stay in control of what matters.

**Daniel Lopes:** If you have any questions, let me know. I'll spend the next hour documenting everything in more detail. Feel free to put time on my calendar—both of you are priority. We have a meeting scheduled for next week too.

**Tucker Barker:** I'm going to connect with Quantum (a recruiting partner) to see how we can work more efficiently. We shouldn't need to manually upload candidates to Workable—that's unnecessary. But they'll probably want to share candidates with you for approval before uploading.

**Daniel Lopes:** We have options on the services side—there's an agency for technical candidates (Rick Rooney). On the programmer side, our current recruiting partner is finding great candidates, but with you directly involved, you'll understand company culture and exactly what we need at each stage. We have a lot of strong backend people now but are lacking on the frontend side—you'd be able to calibrate that much better and faster than me. You'll see where the product problems are too. It's just much better to have you here and involved.

**Tucker Barker:** Right now I'm still at my previous company and working a couple of hours a day under the radar. April 7th is my first official day here. I can probably give two to three hours a day, sporadic throughout the day.

**Daniel Lopes:** If you see anything that seems wrong, we can change it. Whatever works best for you—we're flexible.

**Marília Caroline da Silva:** All right.

**Daniel Lopes:** Thank you.

**Tucker Barker:** Thanks for taking the time.

**Daniel Lopes:** Great to meet you.
