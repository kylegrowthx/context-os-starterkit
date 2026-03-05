# Joe - sync on inbound

<metadata>
date: 2025-06-18
time: 16:31 UTC
duration: 29 minutes
organizer: kyle@growthxlabs.com
participants: Joe Lehr, Kyle Gaudreau
fathom_recording_id: 69177517
fathom_url: https://fathom.video/calls/329288417
share_url: https://fathom.video/share/yq3fFbw4BfW91FW_n_8qf3pnDBJsCsVs
source: fathom
enriched_on: 2026-03-03 00:00 UTC
</metadata>

---

## Summary

Joe and Kyle aligned on the HubSpot implementation strategy to migrate inbound sales processes from Adio, prioritizing deal stage definitions, required field enforcement, and BANT criteria to ensure deal stage progression is rigorous. Joe will build the core architecture in HubSpot next week, starting with pipeline stages and email sequences for webinar follow-ups, while Kyle will define reporting metrics and clarify questions around execution phase deal creation. The migration target is end of July or early August, ideally before onboarding new sales representatives.

---

## Context

Joe Lehr is a fractional consultant helping Kyle Gaudreau (GrowthX's head of sales) build out the inbound sales motion in HubSpot. This sync was focused on defining the next phase of HubSpot implementation after Kyle documented pipeline stage definitions. The broader context: GrowthX is scaling inbound and currently uses Adio, but the team has decided HubSpot is a better fit for managing deal data, reporting, and supporting future team scaling. Joe brings experience from previous companies (Tango, Bardeen) where he built sales operations architecture. Kyle is thinking about how to implement processes that will scale as new AEs join the team, not just for him and Bruno's current reality.

---

## Relevance

- **To GrowthX Delivery:** Process clarity and deal metadata are foundational to handing off account information to delivery teams. Kyle emphasized the need for better documentation and briefs passed along with deals, and Joe validated that note handoffs are mission-critical for delivery enablement.

- **To GrowthX Business Development:** Setting up BANT criteria, closed-loss tracking, and inbound reporting is essential for improving deal quality, forecasting accuracy, and understanding win/loss patterns. The team identified a pattern of deals moving to proposal prematurely, so required field enforcement will surface deals that aren't truly qualified.

- **To GrowthX Business Development:** Forecasting approach will use Google Sheets with Apps Script pulling HubSpot deal data, since HubSpot doesn't natively handle the two-deal-type problem (sprint vs. execution phase) where a $15k standard engagement may lead to a $60k/month expansion deal. Kyle needs clear answers on when to create execution phase deals (proposal vs. contract stage).

---

## Overview

- Prioritizing HubSpot setup for inbound, including pipeline stages, BANT criteria, and sequencing
- Aiming for swift transition from Adio to HubSpot, ideally before onboarding new AEs
- Focus on establishing foundational processes and reporting capabilities in HubSpot
- Need to define clear criteria for deal stage progression and implement required fields

---

## Key Topics

### HubSpot Implementation Strategy

  - Joe to start building in HubSpot next week, focusing on core architecture
  - Mariela to help with webinar list sequencing, starting emails by Monday/Tuesday
  - Emphasis on multi-touch (not yet multi-channel) approach for initial outreach
  - Discussion on enforcing field completion for stage progression (e.g., closed loss details)

### Pipeline Stage Definitions

  - Kyle created a document outlining pipeline stages
  - Debate on when to move deals to "Engaged" stage (post-meeting occurrence vs. scheduling)
  - Consideration of implementing BANT criteria as a requirement for moving to proposal stage
  - Decision to use text fields for BANT, with potential for future automation

### Deal Creation and Management

  - Need to clarify process for creating execution phase deals
  - Challenge: accurately reflecting potential deal values (e.g., $15k standard vs. $60k/month potential)
  - Plan to use Google Sheets with Apps Script for initial forecasting, pulling data from HubSpot

### Sequencing and Reporting

  - Immediate need for basic sequences: DQ, giving a chance, qualified (didn't book)
  - Future consideration for additional sequences: closed-lost reasons, recent intros, etc.
  - Emphasis on developing comprehensive reporting capabilities in HubSpot
  - Key metrics: inbound leads, qualification rates, stage progression, forecasting

### Transition Timeline

  - Aim to move off Adio by end of July/early August
  - Priority on having HubSpot fully implemented before onboarding new AEs

---

## Action Items

**Joe Lehr (Consultant)**
- Implement deal stages in HubSpot as per Kyle's document

- Build initial email sequence in HubSpot for webinar list follow-up. Enable Mariela to review/adjust copy by Friday, so emails can start going out Monday/Tuesday.

- Set up new form field capture for inbound analysis in HubSpot

- Add BANT criteria as text fields in HubSpot, required for moving to proposal stage. Text field preferred over dropdown to reduce initial setup overhead.

- Start building basic reporting dashboards in HubSpot (inbound metrics, deal stages, forecasting, etc.). Clarify with Kyle which insights he needs first.


**Kyle Gaudreau (GrowthX)**
- List out specific reporting questions and metrics needed for HubSpot dashboards (inbound volume, qualification rates, stage progression, forecast visibility)

- Clarify the logic for when to create execution phase deals (currently $15k standard vs. $60k/month potential structure needs definition)

---

## Transcript

**Joe Lehr:** Definitely this time. I'm good, man. Just rocking and rolling.

**Kyle Gaudreau:** Good. Hope you're feeling better.

**Joe Lehr:** I don't know. I was overdue to catch something, honestly. So I did. But, you know, all that matters is the boys are good. But I appreciate the patience. Definitely a lot of stuff to do, which is good.

**Kyle Gaudreau:** Yeah, I saw your message earlier. Didn't have a chance to respond. I was just putting it out there.

**Joe Lehr:** You want to jump in? Yeah, let's do it. Let me record this, if you don't mind.

**Kyle Gaudreau:** I think it should automatically email it to you afterwards.

**Joe Lehr:** Thank you. Let me share my screen. Is anything else you want to cover?

**Kyle Gaudreau:** Oh, the last thing — Biologica. No idea why you're invited to that. That's definitely not needed. Not that we don't want to help, it's just, you know, I don't know if it would be a great use of your time. I'll just stand there and smile awkwardly.

**Joe Lehr:** Okay, cool. So good to know.

**Joe Lehr:** I just want to walk you through HubSpot first. It plays well into this pipeline stage definition. So next week, I'm going to start focusing on really building in HubSpot. The quick thing for this Friday is we have that email — so we're going to use that to help with sequencing the folks that you highlighted from the webinar list. I'm so bad at saying names. Mariela?

**Kyle Gaudreau:** Mariela. God damn it. You're not the first one who's messed that up.

**Joe Lehr:** My brother's John. We kept it simple. Simple for simple dudes. But she's great. We had a chance to sync last week. We're just going to look through that list, refine it a bit more. Some folks will just require a manual touch sent from Gmail with delegated access, so she could go into that Gmail account and send from there. That means there won't be a sequence or multi-thread. She could make a note to follow up. Some folks just won't be sequenced from HubSpot because they don't have much in the pipeline with us in the past. But what she'll do is review all contacts and use a field to enroll in the sequence. If it's yes, then it'll be multi-touch, not multi-channel yet. Have you used HubSpot before?

**Kyle Gaudreau:** Yeah, on the CRM side not as much, but I'm quite familiar with the marketing side. More of a Salesforce guy. Not that I prefer Salesforce, but more companies use that.

**Joe Lehr:** If you've used Apollo or SalesLoft, the ability to have a sequence utilizes a template assigned to a task. You'd have a tab, send out this email, you open the tab, and there's the templatized email with the person's information and email already filled in. The ideal state would be she tweaks the first sentence so it's personalized, then sends, and the next touch points are automated. That's the goal for V1 — let's email some people. She knows how to write copy and is pretty good with Fathom. I want to pick it up by Friday so she can adjust the copy, and then Monday, Tuesday, emails start going out. I was speaking with Bridget yesterday.

**Joe Lehr:** It's definitely going to require some deep dive, heads down time for the deal approach and how to properly build deals. But I think that's secondary. First, let's just build the architecture of the day-to-day in HubSpot. That's where the pipeline stage definitions come in. One of the immediate value-adds is that you cannot move to a stage unless you have certain fields filled out. That's really important. I love this document you put together. I'd be curious if there are fields that come to mind — existing or net new — that we should incorporate. Obviously, closed loss. Now we'll enforce closed loss detail and closed loss theme. We can start collecting that data, which helps with inbound analysis. Can we look at why it was closed loss? That would be helpful.

**Kyle Gaudreau:** Yeah, I haven't spent much time thinking about that explicitly, but can definitely think about it more. Unfortunately, my week is pretty packed.

**Joe Lehr:** I could take a stab. What fields do you feel need to be updated?

**Kyle Gaudreau:** When you say that, do you mean updated in association with it being ready to move to the next step, or more in the form of the typical deal at intro?

**Joe Lehr:** More so the former. If you want to create, I'm going to try creating the intro stage automatically. Intro truly is — they showed interest in having an initial meeting. But how do we get to engaged? What are those two or three things that would be really helpful to know to steer the conversation, especially as you're working deals with Bruno?

**Kyle Gaudreau:** I don't want to overcomplicate this, but the way I thought about it was the exit criteria into engaged — whether it should be when the meeting is scheduled versus when the follow-up call actually occurs. The concern is someone could schedule, then cancel, and they never truly become engaged like we thought. How frequently that happens is debatable. But if we hold true to that, then what's the logic for stamping a meeting date? The key question is: once a follow-up meeting occurs, how do we hold that and truly define it as engaged?

**Joe Lehr:** The way I've done that in the past was not on the deal, but on the lead. I'm not suggesting that, but the lead status would be things like meeting booked, meeting rescheduled. You want to analyze both the deal funnel and the inbound funnel. Meeting canceled can hurt numbers if you're using something like Chili Pipe. More nuanced lead statuses would be: discovery required, further discovery required, nurture, disqualification. We'd do all that before creating a deal until someone was qualified. What you're saying, I align with that. We'll iterate on this either way.

**Kyle Gaudreau:** My mindset was clarity and accountability more than a revamp. Given we're in transition, additional complexity may not be ideal. But what I was solving for — we had a bunch of deals in proposal that never should have been proposal.

**Kyle Gaudreau:** We had a meeting, sent them an SoW, they weren't engaged, and we need better clarity on that. My aim was to make the progression from intro to engaged to proposal to contract far more clear. I didn't get a chance to think too much about fields though.

**Joe Lehr:** Now that we're having this conversation, how do we better prevent going to proposal? Maybe something like BANT that requires folks to actually put in information and holds them accountable. You create a proposal, but the timing field shows you didn't even capture timing — it's unknown. That helps standardize and enables better coaching.

**Kyle Gaudreau:** That's a good point. I had played around with BANT criteria before, but I was indexing towards simplicity for now.

**Joe Lehr:** Speaking to simplicity, BANT aligns with simplicity, right? As a former rep, I don't want to fill out many fields. I'm trying to do deals — you pay me for deals closed, not data maintained. But BANT could be easy to manage if we have it pop up as one of the few required fields. I've built this before where you need just two or three of them.

**Kyle Gaudreau:** I think something like BANT honestly does make sense. We're kind of doing it to an extent, just not documented in a consistent way. In terms of prioritizing and assessing fit, it aligns well with how we're thinking.

**Joe Lehr:** We could literally require BANT to get to proposal. You don't need BANT for engaged — that's up to the rep. Intro calls are created, they show clear interest. To proposal now, you actually need to have BANT verified. We could keep it high-level, even true or false just to hold people accountable. But we could make it a text field, dropdown field — pretty easy.

**Kyle Gaudreau:** I'd prefer text, unless there's some common pattern for dropdown that would make sense.

**Joe Lehr:** It's you and Bruno right now, right? Better to have BANT set now so new AEs don't implement their own way. This is what we're doing — the expectation is you managing BANT in the interview process. Have you used BANT before? How do you ensure you maintain it?

**Kyle Gaudreau:** Sellers are going to tell during the interview. I've learned that many times.

**Joe Lehr:** One of the best reps I know is terrible with data. You flat out lied to me — it never contains data. But we can also automate this with note takers or other tools.

**Kyle Gaudreau:** The aspiration eventually is to start manual, find where we can get real time savings, and automate. We should have a ton of opportunities around that.

**Joe Lehr:** My old company, Tango, did SOPs with automation AI. You create an SOP and it helps people understand where to click on their computer. It can update based on calls and workflows.

**Kyle Gaudreau:** I saw something from a guy who used to work on that earlier this week — a different use case, but about leveraging workflow to create documentation. I'd love to get to that point where we have a common set of fields we can populate, eventually creating briefs that get passed to the delivery team. When I was on services, I was handed accounts with almost no context. I could look at recordings, but if I need something to pop out, it's useful. I really want to enable the team better so this process gets enriched and captured for the handoff stage.

**Joe Lehr:** I do fractional work for an AI workflow tool called Bardeen. I also worked at a customer success platform. That note handoff thing was critical. There was no automation, but at least a template where you pull fields and ask people to fill it in. But you guys have your offsite next week, right?

**Kyle Gaudreau:** I don't know if we're considering it an offsite, but yeah, it's going to be a weird week. I don't have a lot on my calendar, but it feels like team and heads down time.

**Joe Lehr:** I'm trying not to bug you guys, doing heads down work myself to get some things pushed through. What would you want to see following this conversation? I'll get deal stages in and work with you on importing fields. Is it just literally one field? What would you want to see?

**Kyle Gaudreau:** I just want on a spreadsheet to have this be the source of truth of what moves over and what stage it's at. That's probably the most ideal for you to move over to HubSpot. What's our timeline to move off Adio? I feel like someone mentioned it recently.

**Joe Lehr:** We could do it by the end of July, maybe August if needed. It's not urgent, but why can't we do it quickly? I'll probably put my foot in my mouth later, but if we do it thoughtfully, let's get all the companies over, move defaults over. The tricky thing is the deals — you have two deals and it's not fully clear. That's something I'll work with you and Bridget on. She has insider knowledge: this is actually this dollar amount, we should close this, we shouldn't create that one.

**Kyle Gaudreau:** When do we create execution phase deals? In HubSpot, how that works is probably going to be different. Do we create it at contract phase or proposal phase? We have two deal types — sprint and execution phase. That gives clarity on pipeline from an ARR perspective. Execution phase is created because we don't assume ARR from sprint. That's my understanding.

**Joe Lehr:** There's an example with one of our deals: it's $15k standard, but there's an approach where it's $60k a month. How do we reflect that in forecasting? I was talking to Bridget about this yesterday. Forecasting will happen in Google Sheets. There's something called Apps Script — I could create a button that pulls data, or have it run every morning. But we have to align on what property fields and associations are needed. Is it a deal object? I don't want to build a custom database because it's a waste of time and will get replaced by a real tool.

**Kyle Gaudreau:** If we over-engineer this and then decide to move away from the process... we will move away from the process, for sure.

**Joe Lehr:** I want to push you guys to get a real tool because it'll ease the pain. It's about finding the right tool and going through the pain first. Before deciding on HubSpot, we said let Kyle go through the pain first, and when we evaluate tools, there's native integration considerations.

**Kyle Gaudreau:** In terms of timing, my mindset is indexing towards speed as much as possible. As we're bringing on AEs, it would be ideal to onboard them into HubSpot rather than messy in-between stuff. I'm totally aligned with you, Joe.

**Joe Lehr:** One of my clients did hypergrowth, Series D, but never had the opportunity to put in the foundations because they grew so quickly. Monster teams — 10 people on RevOps — and the foundations just aren't there. It sounds obvious, but you just gotta get the foundation set. So what would you want to see as I start building in HubSpot? What would be awesome? Is it getting the stages in? Should I build BANT?

**Kyle Gaudreau:** At stages and how we handle BANT — I don't feel strongly between text and dropdown, but true-false feels too basic. My hesitation on dropdown is the time to think about what those options should be. I'd prefer text.

**Joe Lehr:** I hear you. Put a line in text and maybe move to automation later where that takes care of it.

**Kyle Gaudreau:** The other two things on my mind — how do we handle sequences and reporting. That's the main stuff. We need the basics: DQ, giving a chance, qualified, didn't book. But we also need to think about sequences around key moments like closed-losses, sliced by closed-lost reasons, recent intros. We'll do some manual for now, but I want to start with the basics and then connect the dots on what comes next. Adio has next to no reporting. I need to tell and monitor a clear story from inbound to weekly happenings to forecasts. Basically: how many inbounds this week? How many qualified? How many at each stage? That doesn't have to be a prereq to transition, but I'd love to do that as we get onto HubSpot. Even if it's just cleaner data we can use outside HubSpot, that's fine.

**Kyle Gaudreau:** I'm a very numbers-centric person. Having the lack of reporting is a weird place to be.

**Joe Lehr:** I'm the same way. I'm a data person — that's my whole skill. What you're asking for, those dashboards are mission-critical and should live in HubSpot. I've built those before, so that's not a challenge. But I need to know: are you looking for dashboards to give you insight into stalled deals that should be closed loss, or deals stuck in proposal for 50 days? You want all of that, but where do we start?

**Joe Lehr:** Do you want me to find time tomorrow to discuss the inbound analysis piece and new form field capture, or do this async?

**Kyle Gaudreau:** I'm off tomorrow because it's Juneteenth. I can catch up on Friday.

**Joe Lehr:** I'll see if I can find time. If not, early next week.

**Kyle Gaudreau:** I have openings on Friday. I have heads down time blocked, but we can work around it.

**Joe Lehr:** I have to leave at 3 because of family photos.

**Kyle Gaudreau:** We can meet before that. All good.

**Joe Lehr:** Nice chatting, Kyle.

**Kyle Gaudreau:** Likewise. See you next week.
