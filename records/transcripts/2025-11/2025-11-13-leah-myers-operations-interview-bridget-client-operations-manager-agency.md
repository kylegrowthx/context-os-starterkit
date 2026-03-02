# Leah Myers -Operations Interview - Bridget | Client Operations Manager - Agency

<metadata>
date: 2025-11-13
time: 21:29 UTC
duration: 40 minutes
organizer: bridget@growthxlabs.com
participants: Bridget McGillivray, Leah Myers
fathom_recording_id: 101594101
fathom_url: https://fathom.video/calls/471897023
share_url: https://fathom.video/share/xDH-juyNiZEKg1PVYsJGc7uF9JaSqXiR
source: fathom
enriched_on: 2026-03-02 17:45 UTC
</metadata>

---

## Summary

Bridget McGillivray interviewed Leah Myers for a Client Operations Manager role to build foundational systems and data infrastructure for the agency's scaling from 50 to 200+ clients. Leah's experience at Apollo—building a CS org from scratch by integrating product usage data with GTM data in Vitally and implementing tiered health scores—directly aligns with the agency's immediate needs for ending "step zero" operations (manual Notion databases, scattered data, vibes-based health scoring). The agency is executing a critical transition from a $13M services agency to a customer-facing product company in 2-3 months while separating editor and client relationship management roles. Both parties expressed strong alignment and enthusiasm; next steps include Bridget aligning with Andy on process and scheduling a final interview round (potentially the following week).

---

## Context

The client is an undisclosed agency transitioning from a B2B services model to a platform company. Currently operating at $13M ARR with 50 clients, they're building a proprietary platform (going customer-facing in 2-3 months) while managing a hybrid business model. The organization is led by operations-minded leadership (Bridget McGillivray oversees company-wide ops, HR, finance, IT, legal) and is acutely aware that their current operational infrastructure cannot support the growth trajectory. Data is scattered across Notion, Airtable, and Google Docs; health scores are manual and subjective ("vibes-based"). The agency is in the middle of a major org design overhaul—separating the editor role (content production, behind-the-scenes work) from the client account management role (relationship ownership, strategic engagement). They're desperate to move fast on hiring someone who can build the foundational systems (data pipelines, health score models, playbooks, dashboards) before the platform launch.

---

## Relevance

**To GrowthX Delivery:**
- This interview reveals a services-to-platform transition pattern that may be relevant to other agency clients or future engagements. The challenge of moving from subjective ("vibes-based") health scoring to data-driven metrics in a services context is methodologically significant.
- Leah's philosophy of automating team tasks before they become bottlenecks and her emphasis on treating internal stakeholders (CSMs, editors) as "internal customers" aligns with GrowthX's approach to delivery process design.
- The data integration pattern (Snowflake product data + Salesforce GTM data via Vitally) is a replicable model for clients struggling with multi-source truth.

**To GrowthX Business Development:**
- This is an actively hiring client with urgency (candidate in late-stage talks with another company; interview process accelerating to as soon as next week). High-touch, responsive delivery could strengthen the relationship or uncover upsell opportunities around data ops, GTM tech stack optimization, or content strategy for platform launch.
- The $13M ARR agency transitioning to platform is a potential reference customer if the hire succeeds and the platform launch delivers.

**To GrowthX Operations:**
- Leah's AI experience (trained an Intercom chatbot after a "hard fail" to limit scope) and her emphasis on thoughtful tool adoption mirrors GrowthX's approach to tooling decisions. Her philosophy of learning from failures before wide rollout is worth noting for team discussions.

---

## Overview

- Leah Myers's experience at Apollo—building a CS org from scratch by integrating product usage data (Snowflake) with GTM data (Salesforce) in Vitally—directly matches the agency's needs.
- The agency is at "step zero" with operations, using manual Notion databases for "vibes-based" health scores and lacking a single source of truth for metrics.
- A key challenge is the hybrid business model: a services agency ($13M ARR) transitioning to a customer-facing product company in 2–3 months.
- The role is critical for building foundational systems (health scores, playbooks) and a data baseline to support scaling from 50 to 200+ clients.

---

## Key Topics

### Agency's Operational State

  - **Business Model:** A services agency ($13M ARR) using a proprietary platform internally, transitioning to a customer-facing product company in 2–3 months.
  - **Current State:** "Step zero" operations.
      - **Data:** Scattered across Notion, Airtable, and Google Docs.
      - **Health Scores:** Manual, "vibes-based" scores in Notion databases.
      - **Metrics:** No single source of truth; basic revenue/churn data requires manual hacking.
  - **Key Challenges:**
      - **Role Ambiguity:** Editors currently manage client relationships, a role separation is underway.
      - **Scaling:** Current manual processes cannot support growth from 50 to 200+ clients.
      - **Mindset Shift:** Unlearning SaaS-centric ops to fit the services model.

### Leah Myers's Relevant Experience

  - **Apollo Case Study:** Built a CS org from scratch, solving for "janky" product usage data.
      - **Data Pipeline:** Integrated product usage data (Snowflake) with GTM data (Salesforce) in Vitally.
      - **Health Scores:** Implemented two distinct scores: one for onboarding risk and one for renewal likelihood.
      - **Team Enablement:** Created dashboards for CSMs to review account health before calls and for execs to track team effectiveness at scale.
  - **Automation Philosophy:** Automate personal tasks on the 2nd–3rd repetition; proactively identify and automate team tasks before they become bottlenecks.
  - **AI Experience:** Early adopter; trained an Intercom chatbot after a "hard fail" to limit its scope and prevent internal issues.

### Role & Fit

  - **Candidate Motivation:** Seeks a role with significant impact and autonomy to build systems from a "blank slate."
  - **Hiring Manager Perspective:** The role is a "must-have" to build foundational systems and a data baseline.
  - **Urgency:** The agency needs to move quickly, as the candidate is in late-stage talks with another company.

---

## Action Items

**Bridget McGillivray (GrowthX)**
- Align with Andy (hiring partner) on next steps with Leah; send Leah interview status update; schedule final round interview ("Steinman" session, potentially next week)

**Leah Myers (Candidate)**
- Email Bridget with status update on other late-stage interview process

---

## Transcript
**Bridget McGillivray:** Hi, Leah.

**Leah Myers:** Hi, Bridget.

**Leah Myers:** How are you?

**Bridget McGillivray:** I'm good.

**Bridget McGillivray:** How are you?

**Leah Myers:** Doing well.

**Leah Myers:** Thanks for asking.

**Bridget McGillivray:** I am like really in the map.

**Bridget McGillivray:** So I was just looking at where you live on a map.

**Leah Myers:** Awesome.

**Leah Myers:** Love that.

**Leah Myers:** I'm in Oakland, Wisconsin.

**Leah Myers:** So you saw that other side of the state border from like Minneapolis, St.

**Bridget McGillivray:** Paul, essentially.

**Bridget McGillivray:** Yeah.

**Leah Myers:** Yeah.

**Leah Myers:** What are you based out of?

**Bridget McGillivray:** I live in Vancouver in British Columbia.

**Leah Myers:** Nice.

**Leah Myers:** Yeah.

**Bridget McGillivray:** So I've never really spent much time over there.

**Bridget McGillivray:** So I'm always like I got to reorient when I see those states and towns.

**Bridget McGillivray:** I'm like, where is that?

**Bridget McGillivray:** Do you know Joe Lerb?

**Bridget McGillivray:** I don't know if it's his last name actually.

**Bridget McGillivray:** Lerb?

**Bridget McGillivray:** Lerb?

**Leah Myers:** We're connected through him.

**Leah Myers:** I don't remember, honestly.

**Leah Myers:** LinkedIn is great, and I have over 500 connections, but I don't know that many people.

**Bridget McGillivray:** Okay, I just thought I would try.

**Bridget McGillivray:** was like, wait, how that's so interesting, because he was consulting for us until like two months ago.

**Leah Myers:** Okay.

**Bridget McGillivray:** He started his own like rev ops agency temporarily, so he was doing like HubSpot implementation for us, but then he got poached already to be full-time in a VC actually.

**Bridget McGillivray:** Um, so we sadly lost him, but, um, okay, that was funny.

**Leah Myers:** was like, oh, I wonder, um, because he does look familiar, but like, why would I, Catalyst, probably Catalyst.

**Leah Myers:** I did a trial of Catalyst when I was shopping for a customer success platform for Apollo.

**Leah Myers:** So, um, yeah, my, the manager of customer success at the time knew the founders of Catalyst directly, so we got like top-tier treatment from their sales.

**Leah Myers:** And I'm guessing I probably met him then.

**Bridget McGillivray:** Okay.

**Bridget McGillivray:** That makes sense.

**Leah Myers:** So it's a sales move.

**Bridget McGillivray:** That's a good one.

**Bridget McGillivray:** Cool.

**Bridget McGillivray:** Well, it's very nice to meet you.

**Bridget McGillivray:** was just also reading Andy's notes, speaking with you as well.

**Bridget McGillivray:** I run ops company-wide, I guess.

**Bridget McGillivray:** So I've got recruiting in HR and finance and IT and legal.

**Bridget McGillivray:** And I work with Andy also on customer operations.

**Bridget McGillivray:** And then I'm excited to help with this role because I also used to lead like RevOps as in it was one person in me at my old company.

**Bridget McGillivray:** And so anyway, I'm just like a huge fan of ops people in general, Swiss Army Knives, like behind the scenes doing all the magic.

**Bridget McGillivray:** So I'm excited to meet you.

**Leah Myers:** Cool, cool, cool.

**Leah Myers:** Excited to meet you as well, especially with that enthusiasm for ops.

**Leah Myers:** Because, yeah, I agree with that assessment.

**Bridget McGillivray:** Absolutely.

**Leah Myers:** We're the glue people, and literally everything breaks without the glue people.

**Bridget McGillivray:** Nice.

**Bridget McGillivray:** Well, I only really have, like, two main questions, but we can go kind of deep on them if that's cool.

**Leah Myers:** Let's do it.

**Bridget McGillivray:** Like, would love to hear about, if you have an example, I mean, I was trying to look at what you and Annie were talking about, but, like, tell me about, like, if you have some dashboards you've built, and, like, how you think about that, and, like, just in general, how you think about, like, using data to, like, push any projects forward you're doing, and, like, I don't know.

**Bridget McGillivray:** I know that's broad, but I'd just love to dive into, like, experience there you've built.

**Leah Myers:** Absolutely.

**Leah Myers:** And through the broad lens, I'm going to kind of meander a bit, so pop in and ask questions or tell me to skip parts if I'm getting a bit pedantic or whatever.

**Leah Myers:** But, like, I've never joined an organization that's had perfectly clean data or well-structured data even.

**Leah Myers:** So that's part of, like, what I like to do.

**Leah Myers:** Untangle these messy situations and bring clarity and actionable insights based on like this raw volume of amazing stuff that a company already has in place, like available, not necessarily like established or, you know, structured.

**Leah Myers:** So what I will use as an example is my time at Apollo, which I think I dove deep in with Andy, but it's a great example.

**Leah Myers:** So I'm going to do it again.

**Leah Myers:** When I joined, there was no customer success org whatsoever.

**Leah Myers:** There was no budget for a tool and the data was just crap.

**Leah Myers:** There was way too much of it, way too much because Apollo, what they do is like, find all of this data on the internet and then sell it to other people.

**Bridget McGillivray:** So like we had, right?

**Bridget McGillivray:** Like sales signals?

**Leah Myers:** Um, yeah.

**Bridget McGillivray:** Like clay or common rooms or?

**Leah Myers:** I'm sorry.

**Leah Myers:** Could you repeat?

**Leah Myers:** I'm sorry.

**Bridget McGillivray:** Is it like clay or common room or is it more like leads or what is it exactly?

**Leah Myers:** Leads.

**Leah Myers:** Yeah.

**Leah Myers:** I would say more like personnel information.

**Leah Myers:** Yeah.

**Leah Myers:** So LinkedIn, I believe, is one of their data sources.

**Leah Myers:** So company size and the amount of people that are, for instance, in an engineering team at an organization, if it's a B2B product that's selling an engineering tool, we would repackage that data and sell it to that engineering company and be like, hey, this is the total market that you're missing within your existing customer base, that sort of thing.

**Leah Myers:** So we had tons of attributes at the account level, at the contact level, more insights than we knew what to do with.

**Leah Myers:** And I identified a gap almost immediately that our own utilization data was janky, just not good.

**Leah Myers:** We had it piped into Salesforce.

**Leah Myers:** We had some old kind of like archaic definitions as to what it used to mean.

**Leah Myers:** Nobody was keeping up with the flows or macro, whatever Salesforce functionality was built for it at the time to keep it up to date.

**Leah Myers:** And I had to run a customer success team with it.

**Leah Myers:** So I went...

**Leah Myers:** Back to the source, the product management team, and asked for fresh flows.

**Leah Myers:** We didn't have a BI person at the time, I don't think.

**Leah Myers:** We hadn't hired the head of BI, so we had a lower-level analyst that was just making do, but didn't have the organizational know-how to whip the org into shape.

**Leah Myers:** So I had to navigate a bunch of missing components outside of my skill area to even begin getting in the data I needed to create the dashboard.

**Leah Myers:** That meant things to the end users and the executive level.

**Leah Myers:** Ultimately, was able to connect the product to the Snowflake, get the Snowflake, and connect that to Vitally, is what I ultimately implemented at Apollo.

**Leah Myers:** were looking at Yep, yep.

**Leah Myers:** Andy had mentioned that, too.

**Leah Myers:** I do love Vitally.

**Leah Myers:** It's a very lightweight plug-and-play tool.

**Leah Myers:** I had a great experience with it.

**Leah Myers:** 10 out of 10, do recommend.

**Leah Myers:** Sorry to interrupt, but getting into the

**Bridget McGillivray:** Snowflake, how'd you do that?

**Leah Myers:** With, from the engineering team and like, I just kind of connected people that knew Snowflake and our data and said, please figure it out.

**Bridget McGillivray:** it's like product data.

**Bridget McGillivray:** It's like just product usage.

**Leah Myers:** Okay, okay, okay, okay.

**Leah Myers:** Yeah, yeah.

**Leah Myers:** And then how did you get it into Vitally?

**Leah Myers:** Direct Connect.

**Leah Myers:** Well, maybe it was a census, like with a third-party tool.

**Leah Myers:** I forget exactly.

**Leah Myers:** I know that there's a Snowflake connector into Vitally directly.

**Leah Myers:** I believe if I'm remembering correctly.

**Leah Myers:** Otherwise, we used census quite a bit.

**Leah Myers:** And yeah, Fivetran is out of the, like, go-to-market tool into Snowflake and census is from Snowflake into the go-to-market tool, if I remember correctly.

**Bridget McGillivray:** yeah.

**Leah Myers:** Do you use it?

**Bridget McGillivray:** Were you using it?

**Bridget McGillivray:** Yeah.

**Leah Myers:** Oh my gosh, I love that.

**Leah Myers:** So I worked at, my last company was called Airbyte.

**Bridget McGillivray:** It's like a Fivetran competitor.

**Leah Myers:** was like, it would take Salesforce data, product data, whatever.

**Leah Myers:** Drop it in Snowflake.

**Leah Myers:** Yep, yep, yep.

**Leah Myers:** But I was laughing at your earlier comment because you were saying you've never worked at a company with, like, perfect data.

**Bridget McGillivray:** Like, I was legit at a data company that was pitching, like, get all your perfect data in one place.

**Bridget McGillivray:** And it was such a, it's always such a struggle.

**Bridget McGillivray:** There's just too much.

**Leah Myers:** And the definition of change.

**Leah Myers:** And people leave, and if it's not documented or handed off, the tribal knowledge is lost, and that's tech debt.

**Leah Myers:** So, like, it's never going to be perfect.

**Leah Myers:** But what we can do as operators is build a sustainable system and document it so other people can pick it up if we get hit by a bus tomorrow.

**Bridget McGillivray:** Like, that's my theory.

**Leah Myers:** No single one.

**Leah Myers:** Yeah.

**Leah Myers:** So, got all that connected.

**Leah Myers:** And then I was able to, like, apply meaningful go-to-market data because I had Snowflake data coming into Vitally.

**Leah Myers:** I had our, like, contract data, which had this weird relationship kind of between Stripe and Salesforce.

**Leah Myers:** But, like, I pulled all of that from Salesforce into Vitally.

**Leah Myers:** And then I could like marry them and they were in love.

**Leah Myers:** And we had a like a very light like headcount wise onboarding team, three individuals when I started.

**Leah Myers:** So I say I started the CS team.

**Leah Myers:** I did because it was a true startup and they had three people that were pulled from support and made onboarding that had no structure, no rigor, and just kind of got on the phone with people.

**Leah Myers:** So I, you know, like architected their, their journey, their customer journeys in tandem with them, but then had to like step through iterations as they had to adopt to like more formal structure, but then was able to start guiding them like, okay, within your first two calls, you should see this adoption point at your customers.

**Leah Myers:** Like they should have 50% of their users should have their email inboxes linked up here is where that is present in vitally.

**Leah Myers:** So like giving them the boots on the ground kind of insight as to like how their accounts are performing.

**Leah Myers:** So when they're 10 minutes before they're hopping.

**Leah Myers:** On the phone, we should be able to look at this and see, right?

**Leah Myers:** And then also, like, zooming out then to the executive view, I could say to that manager of CS or my boss, the SVP of RevOps, like, across all of those customers that are onboarding, those that are net new within the last seven days, this is how effective our onboarding team is at scale, like, and draw extrapolations like that.

**Leah Myers:** So, I mean, that was, like, the very first couple of weeks of the Vitality implementation and getting that team all set up, but then ultimately, like, bringing in, you know, renewal data, I implemented a health score, not a, oh, two health scores to start, because I think that onboarding period has a different measure of health than anything beyond that onboarding period.

**Leah Myers:** We need to understand those early risk factors versus, like, they're adopted and now, like, what is their likelihood of renewal sort of thing?

**Bridget McGillivray:** And yeah.

**Leah Myers:** And what's your involvement in, like, the definition?

**Bridget McGillivray:** Like, who, or who drives?

**Bridget McGillivray:** I was like the definition of those things.

**Leah Myers:** It depends on the resources available.

**Leah Myers:** I've totally done it on my own with a hope, prayer, and some logic and hypothesis.

**Leah Myers:** But if I have a resource that is able to help me capacity-wise in BI and run some statistical analyses and stuff, I definitely use that partner to the best of my ability.

**Bridget McGillivray:** We have a very different business model today, but we're going to launch actually two different platforms in the next two to three months.

**Bridget McGillivray:** So it will become more of a product company.

**Bridget McGillivray:** But the way we started, which was very smart of Marcel, our CEO, was like, he's like, I don't want to burn millions of dollars to find a product and hope there's product market fit.

**Bridget McGillivray:** I'm just going to land a bunch of customers today and do everything behind the scenes.

**Bridget McGillivray:** So it's like a services business today.

**Bridget McGillivray:** It's just almost like an agency.

**Bridget McGillivray:** And we learned from them.

**Bridget McGillivray:** So then our team uses our tool today.

**Bridget McGillivray:** Like, it's not exposed to the customers.

**Bridget McGillivray:** But it's an entire platform proprietary we've built where we can see – you would find it very interesting to go look at.

**Bridget McGillivray:** You can see who on our team is using it, how they're using it, if they're using it well.

**Bridget McGillivray:** Like, anyway, we're making it a lot – we improve it as we go because we learn what the customer is like and then build the platform.

**Bridget McGillivray:** So it's like you don't have to, like, burn money to get product market fit.

**Bridget McGillivray:** You kind of, like, have paying customers.

**Bridget McGillivray:** Like, we have, like, 13 million ARR already.

**Bridget McGillivray:** And then we take the money and we can, like, build the platform at the same time.

**Bridget McGillivray:** The very approach – I've normally been in SaaS where it's the opposite, right?

**Bridget McGillivray:** It's, like, just try to, at all costs, get people into the platform and then complain for better or for worse and make it better and better.

**Leah Myers:** But we hide it today.

**Bridget McGillivray:** But then we will be launching it.

**Bridget McGillivray:** So there's, like, almost, like, two different business models.

**Bridget McGillivray:** So…

**Bridget McGillivray:** Which is why it's just more complicated, I think, than most where it's like, we still need the fundamentals of like, account health in the agency and like, customer success metrics and like, our people, you know, but that definition of what success looks like is very different because there's no product signal, there is no product for the customer to use.

**Leah Myers:** A though, like when, I'm just going to speak as though I'm on the team, okay?

**Leah Myers:** When our CSMs are using the product on behalf of our customers, essentially, are we monitoring their utilization in alignment with the customer that they're currently serving?

**Leah Myers:** So like, do they have like a pseudo login for customer A when they're performing work for them versus customer B?

**Bridget McGillivray:** Um, they have, they have, use their own login.

**Bridget McGillivray:** Um, but each client has a workspace.

**Leah Myers:** Okay.

**Leah Myers:** Yeah.

**Bridget McGillivray:** Yeah.

**Bridget McGillivray:** So they go in and it's actually not the CSM people that do it.

**Bridget McGillivray:** I mean, we're totally reworking a bit.

**Bridget McGillivray:** But today, it's been the editors, because we're doing a lot of content production.

**Bridget McGillivray:** So the editors go in, they kick off the workflows, like here's the assignment brief, here's the outline for the article.

**Bridget McGillivray:** Now, write the article, fact check the article, add links in the article.

**Bridget McGillivray:** It's actually all becoming agentic now, too, where you just hit play, and it goes bam, bam, bam, bam, bam.

**Bridget McGillivray:** And it like spits out an article at end, which is then edited by a human.

**Bridget McGillivray:** So it's our editors that go in there today.

**Bridget McGillivray:** I would say there's like the biggest gap in like ability is the people who use it best are very good with prompting and AI.

**Bridget McGillivray:** they understand like the limitations of LLMs or like the importance of the context that it's using in the first place.

**Bridget McGillivray:** Like, did you give it good instructions?

**Bridget McGillivray:** Did you give it good documentation?

**Bridget McGillivray:** Um, so anyways, it's, we're in this like...

**Bridget McGillivray:** Awkward transition phase where soon we want our customers to be in the platform and our team will still use it as well.

**Bridget McGillivray:** But I think that there's a, we can eventually get it to the place where it's button clicky enough that then we go sell it and somebody, any marketer who's like a little bit more AIA savvy could go in there and operate it as well.

**Bridget McGillivray:** I don't know if that answers your question.

**Leah Myers:** It does.

**Leah Myers:** It does.

**Leah Myers:** So there's some sort of like identification that when an editor, and sorry for using CSM.

**Bridget McGillivray:** No, that works.

**Leah Myers:** It's acclimating to the structure of the pods.

**Leah Myers:** So there's some sort of identification, like when an editor is going in there and performing a workflow, hitting that play button, working with the prompts, like that action is associated with a customer identifier, customer profile to some extent.

**Leah Myers:** So it seems reasonable to me with this limited information that we could kind of assume.

**Leah Myers:** Associate the level of interaction and utilization within the product itself to the output and or satisfaction, how the commercial metrics are on, you know, renewal and all that too.

**Leah Myers:** We could marry those things.

**Bridget McGillivray:** Yeah, I think so.

**Bridget McGillivray:** Like, it's all there.

**Bridget McGillivray:** And it's like, how, like, even simple things, like how many articles are being done every week?

**Bridget McGillivray:** Everything is going to be in one platform at the end.

**Bridget McGillivray:** That is totally the goal for the next, like, three months.

**Bridget McGillivray:** Today is just a little bit scattered where they, like, plan a lot of the articles that they're going to do in Airtable.

**Bridget McGillivray:** And then they take the one they want to do and they put it in our content OS, which is our platform.

**Bridget McGillivray:** And then when they want the customer to edit it as well, they dump it into a Google Doc and share it with a customer.

**Bridget McGillivray:** All the edits are in Google Doc.

**Bridget McGillivray:** So the AI is not learning from that, obviously.

**Bridget McGillivray:** If we get our customers into the platform and we're all editing.

**Bridget McGillivray:** Everything within our platform together, then it's learning from that.

**Bridget McGillivray:** And it's like, it will just get so much better at spitting out first drafts that are like 98% ready to go.

**Bridget McGillivray:** So it's like, so the answer is yes, like it's going to be there.

**Bridget McGillivray:** I think parts of it are there.

**Bridget McGillivray:** We can definitely get some efficiency metrics and like deliverability, you know, are we like doing our delivery correctly?

**Bridget McGillivray:** Some of it's going to be like coming from Airtable for a little bit longer and other things.

**Bridget McGillivray:** But anyways, I digress.

**Leah Myers:** That makes sense.

**Leah Myers:** And with the rapid product launch, like you said, the next two to three months-ish that this is going be customer facing, then it does come down to like, do we need to over-engineer for this temporary state when we're going to be launching soon?

**Leah Myers:** So yeah, totally understood.

**Bridget McGillivray:** Exactly.

**Bridget McGillivray:** Like we use notion very heavily today for, for things.

**Bridget McGillivray:** And of

**Bridget McGillivray:** Which, like, pains me because even just a health score, it's like Notion databases suck.

**Bridget McGillivray:** They're not going anywhere.

**Bridget McGillivray:** They're just in Notion, first of all.

**Bridget McGillivray:** And then they don't have snapshots of anything.

**Bridget McGillivray:** So then you end up making this, like, beastly, crazy.

**Bridget McGillivray:** It's just a crazy spreadsheet, essentially, in Notion to try to track.

**Bridget McGillivray:** And everybody's, like, manually putting in what they think the health score is because it's just services today.

**Bridget McGillivray:** It's, like, vibes.

**Bridget McGillivray:** So, anyways, we're, like, in the little kindergarten phase, which I like because I'm, like, I love, like, building from, I love blank space to build more than anything.

**Bridget McGillivray:** So I'm, like, all right, like, we could take this in 1,000 directions.

**Bridget McGillivray:** Like, let's just  try one and see what happens.

**Bridget McGillivray:** That's kind of, like, my mindset with all this stuff.

**Bridget McGillivray:** Anyways, what, tell me, okay, this is philosophical e-question.

**Bridget McGillivray:** I haven't actually thought how I wanted to phrase it, but, like, how do you think about when to automate?

**Bridget McGillivray:** When and versus when to not automate something.

**Leah Myers:** Oh, I've been asked that question so much in my career.

**Leah Myers:** And I used to have a canned answer for it, but I'm a out of practice.

**Leah Myers:** I've been on a personal sabbatical for like the last year and a half.

**Leah Myers:** So I've been out of need to be staffed.

**Bridget McGillivray:** about that next too.

**Leah Myers:** Okay.

**Leah Myers:** When to automate something.

**Leah Myers:** Like, when it becomes, okay, so if I'm automating something for myself as the operator, like if I'm doing it for the second or third time, exact same way that needs to be automated, period.

**Leah Myers:** What I've found with my customer facing teams is they don't get annoyed until like the 80th or 90th time they do something the same.

**Leah Myers:** So I try to proactively when I'm meeting with my stakeholders, suss out, like, what are you repeatedly doing?

**Leah Myers:** Because if you're doing it the exact same way, the exact same time, like by the third time, you should know this needs to be automated.

**Leah Myers:** That's my answer.

**Leah Myers:** Yeah, that's a good answer.

**Bridget McGillivray:** It's actually so true.

**Bridget McGillivray:** One thing we've been spending.

**Bridget McGillivray:** A of time on is just because even our team is not in a platform, it's like just trying to figure out what everyone's doing all day.

**Bridget McGillivray:** Not that I think they're, I know they're all very busy and like keeping customers happy, but like there's no, I can't compare any of the CSMs even or like account managers, whatever the editors, it's like everyone's, there's no apples to apples going on.

**Bridget McGillivray:** So then I don't know, we don't know how to make like, you know, is it true to, can we actually compare this pods output to this groups or whatever?

**Bridget McGillivray:** So yeah, people, it's actually wild to me how long it takes people to realize something is like inefficient.

**Bridget McGillivray:** Yeah.

**Bridget McGillivray:** Even in this era of like AI being the shortcut, like people still haven't, don't think of it as the shortcut.

**Bridget McGillivray:** But, um, the unknown is scary and causes pause and people feel like sometimes it's easier to just start doing something manually.

**Bridget McGillivray:** Yeah.

**Leah Myers:** AI automated systems processes, that sort of.

**Leah Myers:** Like, I have found strength in this career path I've chosen because I'll pause, but then, like, aim to solve at scale to standardize a process for teams of people.

**Bridget McGillivray:** Yeah.

**Bridget McGillivray:** And I like that a lot.

**Bridget McGillivray:** I think it's fun.

**Bridget McGillivray:** Yeah.

**Bridget McGillivray:** Yeah.

**Bridget McGillivray:** And it's like, you want to, you have to balance optimizing for, like, the best performer because they're incredible and, like, get it.

**Bridget McGillivray:** But it's very unlikely they're all like that.

**Bridget McGillivray:** you don't optimize for the worst person because then you're just making something silly that shouldn't even be there.

**Bridget McGillivray:** So you kind of have like, adjust the elevation to, like, yeah.

**Bridget McGillivray:** Yeah.

**Bridget McGillivray:** Tell me about your sabbatical.

**Bridget McGillivray:** I want to know what you did.

**Bridget McGillivray:** Did you learn anything new?

**Bridget McGillivray:** Did you teach yourself something?

**Leah Myers:** Yeah.

**Leah Myers:** So I just need to take a break from the tech world and ops.

**Leah Myers:** I'm really proud of the work I've done.

**Leah Myers:** But my, I need to...

**Leah Myers:** And I don't regret it.

**Leah Myers:** My partner is a business owner and he's a contractor, but then he's an artist.

**Bridget McGillivray:** It's dark now, but there's some of his art.

**Leah Myers:** And so I've really focused a lot of energy on his go-to-market strategy for his art.

**Leah Myers:** So this time last year, he had zero retail partners.

**Leah Myers:** We are dropping off our initial stocking order at our fifth tomorrow.

**Leah Myers:** And I built a website for him, plug-and-play kind of website.

**Leah Myers:** I'm not that big of a developer.

**Leah Myers:** What did you use?

**Leah Myers:** Not WordPress.

**Bridget McGillivray:** Webflow, what did you use?

**Leah Myers:** Webflow, yes.

**Bridget McGillivray:** Thank you.

**Leah Myers:** And then, yeah, a bunch of like artist markets and stuff we've been at.

**Leah Myers:** And now the holiday season is coming, trying to get into more on the Saturdays and stuff.

**Leah Myers:** So I don't know.

**Leah Myers:** I've just been in this art space and it's been fun.

**Leah Myers:** And I have a 13-year-old and she's been really into soccer.

**Leah Myers:** So I've leaned into being a soccer mom.

**Leah Myers:** Yeah.

**Leah Myers:** Just in.

**Leah Myers:** Enjoying life.

**Leah Myers:** And I've got three cats and a dog.

**Leah Myers:** So I just run my floofy, soft, wonderful things.

**Leah Myers:** Very cool.

**Bridget McGillivray:** What, what is, um, what's like a must have in your next role?

**Leah Myers:** Um, difficult problems.

**Leah Myers:** I, I was telling you, like, throughout my career, I've been at like enterprise company to start and then smaller and smaller.

**Leah Myers:** And I want to go where I can really make an impact.

**Bridget McGillivray:** We'll have like the, the proverbial seat at the table, the latitude to make the decision and apply my knowledge.

**Leah Myers:** Like I'm a smart cookie.

**Leah Myers:** I promise you I am.

**Leah Myers:** And I want to do good things.

**Leah Myers:** Yeah.

**Bridget McGillivray:** Hey, I get that too.

**Bridget McGillivray:** I also like really like being early and that's the blank slate thing I'm going to talk about.

**Bridget McGillivray:** Um, like literally, I know I sound like I'm exaggerating, but I don't think I am like anything is better than what exists today.

**Bridget McGillivray:** Like it can always be made a little bit better.

**Leah Myers:** It's like, yeah.

**Bridget McGillivray:** There is nothing that is in place right now that I'm like, that is perfect and that will last a year.

**Bridget McGillivray:** It's like everything feels kind of taped together and like even the next version might be taped together, but you just get like a little bit better over time if you just keep like pushing kind of and moving forward.

**Bridget McGillivray:** So I like that.

**Bridget McGillivray:** Yeah, I agree.

**Bridget McGillivray:** like every day is like, oh, impact literally every day because it's like very easy to identify.

**Bridget McGillivray:** Even if it's low hanging fruit, like, oh, that probably saves someone an hour in the future.

**Leah Myers:** Right.

**Leah Myers:** Well, and like even something as small as a checklist could demystify like the day-to-day for the editor workflow, right?

**Leah Myers:** Like check, check, check.

**Leah Myers:** Everybody is at least doing these three things every time they open up the product, whatever it might be.

**Leah Myers:** And then we can like derive some measurable results from that and see those results and iteratively improve.

**Leah Myers:** And like you said, yeah, nothing is ever perfect.

**Leah Myers:** Maybe I'll give it like, maybe it could be perfect for...

**Bridget McGillivray:** Literally one day, then another thing is going change, another data flow is going to break, something's going to happen, and it's not going to be perfect anymore.

**Bridget McGillivray:** Yeah, it's funny.

**Bridget McGillivray:** Tell me about how you use AI.

**Bridget McGillivray:** I know you've had the year off, but have you been dabbling in things?

**Bridget McGillivray:** I guess in your past, it would have been a bit more early on, but did you use...

**Bridget McGillivray:** ...in your past jobs and things?

**Leah Myers:** Yeah, at the very front end of this AI boom, I managed a tool called Intercom at Apollo.

**Leah Myers:** I own the support team as well as the CS ops team.

**Leah Myers:** So Intercom was one of the first ones out with an AI chatbot.

**Leah Myers:** I turned that thing on.

**Leah Myers:** It sucked real bad.

**Leah Myers:** I turned it off.

**Leah Myers:** I trained it better.

**Leah Myers:** And then limited its reach because it's like, we didn't issue...

**Leah Myers:** We were a month-to-month sort of like pretty cheap product if you were just at ground floor.

**Leah Myers:** And people would be like, can I get a refund?

**Leah Myers:** And the AI chatbot would be like, yes, here's an internal email address you should not know.

**Leah Myers:** And it just created havoc the first time I turned it on.

**Leah Myers:** So I learned a lot from that first hard fail.

**Leah Myers:** And I trained it up better and limited its scope.

**Leah Myers:** So we didn't have our internal billing team screaming at me.

**Leah Myers:** Um, and yeah, so that just dipped the toe in really, um, since I've been out, um, I haven't done a ton with it.

**Leah Myers:** Like there's some automated tools in so many websites.

**Leah Myers:** on the art side, there's like Fine Art America, which I considered putting his artwork on, but the margins are crap.

**Leah Myers:** So I didn't, but in the meantime, I was testing it out.

**Leah Myers:** Like it applied so many keywords to like a single picture I would upload.

**Leah Myers:** That's neat.

**Leah Myers:** Um, not gonna lie.

**Leah Myers:** I use it for my resume updates.

**Leah Myers:** Otherwise I would, it would take so long to do everything, but.

**Leah Myers:** Like the Corbett's mine.

**Leah Myers:** So I have, right away, I bought like a $40 lifetime pass one of the early AI chatbots.

**Leah Myers:** So I have like 17 different LLMs I can tap into at any given time.

**Leah Myers:** And I've gotten good at deciphering like the value of each individual and all that.

**Bridget McGillivray:** Yeah.

**Bridget McGillivray:** All right.

**Bridget McGillivray:** Great.

**Bridget McGillivray:** I just, I always want to make sure everyone's excited about it.

**Bridget McGillivray:** And like, we try to be to the extent possible.

**Bridget McGillivray:** It's very hard when you're just running ahead of a moving train, you know, always like every day, but try to like look for AI native tooling, you know, like Marcel's big on like, don't just default to like your old, the tools you've all used for the last 10 years.

**Bridget McGillivray:** Like there's way, probably way better new versions of everything, you know?

**Bridget McGillivray:** So I'm looking at finance tools right now.

**Bridget McGillivray:** I'm like, okay, I'm going to go just look at these like new AI native ones.

**Bridget McGillivray:** And then, and then I can go back and look at the ones I'm familiar with and compare, you know, so things like.

**Bridget McGillivray:** I mean, it's just the kind of like the mindset here, right?

**Bridget McGillivray:** Of like using it as your first instinct on things.

**Bridget McGillivray:** Yeah.

**Bridget McGillivray:** Cool.

**Bridget McGillivray:** Well, I can go over a few minutes.

**Bridget McGillivray:** you have any questions for me?

**Leah Myers:** Oh, we are at time.

**Leah Myers:** I know.

**Leah Myers:** I've really enjoyed your conversation.

**Leah Myers:** I have like a big list of maybes depending on like what we covered.

**Leah Myers:** Okay.

**Leah Myers:** This is a good one.

**Leah Myers:** What are the biggest gaps that you want this role to close immediately when the person joins?

**Bridget McGillivray:** Oh my gosh.

**Bridget McGillivray:** Everything.

**Bridget McGillivray:** No, I'm just kidding.

**Bridget McGillivray:** So we have, what's happening right now is like, and Andy is amazing.

**Bridget McGillivray:** Her and I are spread so thin.

**Bridget McGillivray:** Actually, so is a lot of people.

**Bridget McGillivray:** And so her and I get together and we have the ideas.

**Bridget McGillivray:** We're like, you know, we know what a health system should look like.

**Bridget McGillivray:** We can help drive the definitions.

**Bridget McGillivray:** And then it's like, we maybe have time to like put together like a , here's how you can put your scores in.

**Bridget McGillivray:** Like I was explaining the notion.

**Bridget McGillivray:** And we're like, okay, now we need all of the account owners to like do their scores, go into the first meeting.

**Bridget McGillivray:** And like, I didn't, it wasn't easy for them.

**Bridget McGillivray:** I didn't train them on it.

**Bridget McGillivray:** And then I'm realizing, I'm like, wait, this is such a nightmare to update every week.

**Bridget McGillivray:** Like this is actually not a good system.

**Bridget McGillivray:** And then it makes them not bought into it because they're like, this is so, you have to like make it good enough and like get feedback.

**Bridget McGillivray:** It's almost like, I feel like ops people are like kind of PMs for our own company, like for our own operations.

**Bridget McGillivray:** Like the customer success team is like our customer.

**Bridget McGillivray:** It's like, does it work for you?

**Bridget McGillivray:** Right.

**Bridget McGillivray:** And is it helping make a difference or is it just busy work making you fill out something or whatever?

**Bridget McGillivray:** So I think like, it's that, it's like, we've got, I feel, and I have like the ideas and then it's just like, we don't have the time to go build something and build something that works.

**Bridget McGillivray:** And then try to make it better and like make it work for the rest of the team too.

**Bridget McGillivray:** So there's.

**Bridget McGillivray:** Like there's literally no shortage of things to be worked on.

**Bridget McGillivray:** Like we're so early.

**Bridget McGillivray:** We literally started talking about health scores like a month ago, but we have like a version one of how to do it.

**Bridget McGillivray:** And then it was like, okay, if someone has health flag on their account, what do we do about it?

**Bridget McGillivray:** So then we started, we use linear for tickets.

**Bridget McGillivray:** We're like, okay, let's just like start collecting that.

**Bridget McGillivray:** Cause we're like, right now we're kind of treating all accounts equally, but that shouldn't be the case.

**Bridget McGillivray:** There's drastic price difference.

**Bridget McGillivray:** There's drastic like ICP difference.

**Bridget McGillivray:** Cause we've changed so much over the year.

**Bridget McGillivray:** So then like, okay, we put together like a linear ticket point for it, but now it's like, okay, how do we want to manage that?

**Bridget McGillivray:** And that's like in a different place than the health score.

**Bridget McGillivray:** So it's just like this kind of thing is like, you clearly like, this is like your world.

**Bridget McGillivray:** And like, you could bring it to life.

**Bridget McGillivray:** And then like, think far enough down the road to have like, okay, we have 50 customers today.

**Bridget McGillivray:** And like, this is painful.

**Bridget McGillivray:** And so when, how are we?

**Bridget McGillivray:** We're ever going to even have 200 next year, right?

**Bridget McGillivray:** Like, I'm talking about, like, our big services clients.

**Bridget McGillivray:** So, like, having, like, seeing ahead around the corner, thinking about that, and then just, like, we are really not metrics-driven because it's not in one place.

**Bridget McGillivray:** It's not set up.

**Bridget McGillivray:** Like, nothing is set up.

**Bridget McGillivray:** There is no data, like, baseline.

**Bridget McGillivray:** So, even this morning, the CEO was asking for, like, just, like, revenue metrics and churn things and revenue by health score.

**Bridget McGillivray:** And, like, I could hack it together with five things.

**Bridget McGillivray:** It would take me long.

**Bridget McGillivray:** So, it's not like it's, like, okay, as a business, what do we want to track and at what cadence?

**Bridget McGillivray:** Okay, what's the definition of that metric, first of all?

**Bridget McGillivray:** And then we kind of define it.

**Bridget McGillivray:** And then, okay, what do we need to track it?

**Bridget McGillivray:** Like, what are the inputs?

**Bridget McGillivray:** What's, you know, I mean, you know what I'm talking about.

**Bridget McGillivray:** And then.

**Leah Myers:** I do.

**Bridget McGillivray:** So, that's, like, we're at step zero.

**Bridget McGillivray:** And then I'll need.

**Bridget McGillivray:** So anyway, I know I'm rambling.

**Bridget McGillivray:** What I mean to say is there's like plenty to be done and like a lot of enthusiasm around this.

**Bridget McGillivray:** So there'll be a lot of support for it too, which I think is important.

**Bridget McGillivray:** It's not a nice to have.

**Bridget McGillivray:** This is like must have like business critical stuff.

**Bridget McGillivray:** Um, so cause the numbers just helps get through to everybody when you're trying to like change a process or like change roles, even our scopes and stuff.

**Bridget McGillivray:** It's like, we're doing it because this, these numbers are like not where we want them to be or, whoa, we're doing way better here than there.

**Bridget McGillivray:** Let's double down like those kinds of things.

**Bridget McGillivray:** So, um, anyway, yeah, drawing correlation.

**Leah Myers:** No, all good.

**Leah Myers:** And I so strongly aligned, especially to like you had mentioned, our like CSMs for the editors and strategic account managers, all of those, those are internal customers to operations folks.

**Leah Myers:** I've always called those internal customers versus external customers.

**Leah Myers:** So if I take care of my internal customers, they take care of my external customers.

**Leah Myers:** And then the power of data and correlation.

**Leah Myers:** So showing the value of what we perceive to be the driving force behind the change we're asking people to make so that it gets them bought in, gets them convinced, or hopefully.

**Leah Myers:** I mean, sometimes you just have to go with your gut and say, please trust me, but build that trust along the way.

**Leah Myers:** Like, it's crazy, actually.

**Bridget McGillivray:** Like, we're hiring more.

**Bridget McGillivray:** Like, all the editors kind of just fell into this account management role, but none of them have background in, like, commercial relationships or, like, customer relationships even.

**Bridget McGillivray:** Sounds like what you were describing before, but some of them, turns out, they're great at it.

**Bridget McGillivray:** Others, they're going to need more help, but they have potential.

**Bridget McGillivray:** And some are just, like, not good at it and don't want to do it, which is fine.

**Bridget McGillivray:** Like, that's what the editor role is for.

**Bridget McGillivray:** Like, you can be behind the scenes.

**Bridget McGillivray:** Do it.

**Bridget McGillivray:** Like, that's what we're, separation we're creating today now is, like, you're either an editor.

**Bridget McGillivray:** You stay behind the scenes or you're a connect out manager and you own the relationship.

**Bridget McGillivray:** So we're separating those like this month, making it clear, defining the roles and then like hiring against those profiles.

**Bridget McGillivray:** Because before we were kind of like trying to hire both and there's not that many people who ever did both of those things.

**Bridget McGillivray:** It was a very weird thing.

**Bridget McGillivray:** We'd end up with either you're good at one or the other, but you have to do everything.

**Bridget McGillivray:** And it was like setting people up for failure.

**Bridget McGillivray:** So role clarity is going to help as well.

**Bridget McGillivray:** And then once we have role clarity, it's like, we need lots of playbooks, like just simple stuff, like how to onboard a client.

**Bridget McGillivray:** What are the questions you should ask?

**Bridget McGillivray:** I feel like that one's huge.

**Bridget McGillivray:** Like what are the questions you ask at these stages to know that things are healthy if you don't have like product metrics or adoption metrics to point to?

**Bridget McGillivray:** So it's like a verified outcome.

**Leah Myers:** At the very least, we should understand what the customer's goal is with us and then measuring ourselves against that period.

**Leah Myers:** And it could be anything.

**Bridget McGillivray:** Maybe it's like, oh my god, this person edited our article 600 times.

**Bridget McGillivray:** Like, that's not good.

**Bridget McGillivray:** You know, this other customer did three edits and was very happy, you know?

**Bridget McGillivray:** So, like, maybe it came out better in the first place.

**Bridget McGillivray:** I don't know, I'm just like spitballing, but, like, we can figure out what, how to measure if, like, something is going smoothly and is, like, easier to serve customers.

**Bridget McGillivray:** Um, so.

**Bridget McGillivray:** Yeah.

**Leah Myers:** All the things on my mind.

**Leah Myers:** Exciting.

**Leah Myers:** These are exciting problems that I think would be exciting to help solve.

**Leah Myers:** Um, very cool.

**Leah Myers:** Very cool.

**Leah Myers:** Nice.

**Bridget McGillivray:** Well, um, so nice to meet you.

**Leah Myers:** Love talking to you.

**Leah Myers:** Love your energy.

**Bridget McGillivray:** Um, I will chat with Andy, though.

**Bridget McGillivray:** She's probably offline.

**Bridget McGillivray:** Uh, she's still online.

**Bridget McGillivray:** Um, we'll get back to the next steps.

**Bridget McGillivray:** I think the next step she has planned is, like, a...

**Bridget McGillivray:** Steinman, essentially.

**Bridget McGillivray:** But yeah, we're trying to move very fast.

**Bridget McGillivray:** So we will be quick to let you know the steps.

**Bridget McGillivray:** Do you have any considerations that we need to know of?

**Leah Myers:** Or all good?

**Leah Myers:** As far as like interview processes?

**Bridget McGillivray:** I am late stage with one other company.

**Bridget McGillivray:** Okay, just keep us posted if anything tolerates there.

**Leah Myers:** Okay.

**Bridget McGillivray:** Yeah.

**Leah Myers:** But I would love to move forward with y'all with a rapid pace.

**Leah Myers:** I don't know.

**Leah Myers:** I'm excited.

**Leah Myers:** Talking to you and talking to Andy just makes me so excited.

**Bridget McGillivray:** I love Andy.

**Bridget McGillivray:** We just keep down over like trying to do ops in a service-heavy business, which is new for both of us.

**Bridget McGillivray:** And then like we can see the light at the end of the tunnel to when it's like platform, which automatically makes life easier because it's like data and like everything's in there.

**Bridget McGillivray:** So we're going, but like we need to get from A to B.

**Bridget McGillivray:** And anyway, it's like, it's very new.

**Bridget McGillivray:** I've had to like try to unlearn SaaS a bit as well, which has honestly been one of the harder things of like, okay, this is different.

**Bridget McGillivray:** This is not like SaaS product or support, ticketed support, whatever.

**Bridget McGillivray:** It's like, it's different.

**Bridget McGillivray:** So anyways, yes, it's fun.

**Bridget McGillivray:** There's lots to do.

**Bridget McGillivray:** There's no shortage of things to do.

**Bridget McGillivray:** But we could try to accelerate and like get this done even by next week, I think, too.

**Leah Myers:** So that'd be amazing.

**Bridget McGillivray:** Awesome.

**Leah Myers:** I'm here with you.

**Leah Myers:** Thank you.

**Bridget McGillivray:** Thank you so much.
