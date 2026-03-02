# Lovable Templates Check-In

<metadata>
date: 2026-01-12
time: 18:01 UTC
duration: 26 minutes
organizer: megan@growthx.ai
participants: George Haikal (VP of Revenue), Georgemaine Lourens (Operations), Nicolas Castellanos (Engineering), Megan Dickey (Product & Operations)
fathom_recording_id: 113556525
fathom_url: https://fathom.video/calls/527924506
share_url: https://fathom.video/share/oWctHZozhspTVwziBj3GdMbjUBND1v2r
source: fathom
enriched_on: 2026-02-28T16:30:00Z
enriched_by: Claude
</metadata>

---

## Summary

GrowthX team confirmed the $40K Lovable upsell (10 templates/week, 10 guides/week), strategized contractor hiring to scale to 15 templates/week for future upsells, and reviewed progress on the new Airtable workflow and the Lovable Tool Brief automation. Final upsell approval pending a call with the client.

---

## Context

This check-in centered on three operational focuses for the Lovable engagement: (1) confirming the approved $40K upsell and establishing the new production baseline (10 templates/week via contractor, 10 guides/week from in-house Jenny), (2) finding and onboarding a contractor who can scale to 10-15 templates/week to unlock future upsell opportunities without adding headcount, and (3) finalizing automation tooling (Lovable Tool Brief workflow in Atlas) and process improvements (new Airtable base for template tracking) to reduce manual work and accelerate delivery. The team also discussed strategic rationale: production volume is not a direct cost driver, so the $40K price reflects complexity reduction (removing review layers) rather than a linear volume increase.

---

## Relevance

- **Revenue:** $40K upsell increases core Lovable engagement and positions for future 15-template/week upsell if contractor hire succeeds
- **Operations:** New Airtable base and Lovable Tool Brief automation reduce manual work and handoffs across content and engineering
- **Hiring:** Contractor search strategy shifts from adding multiple team members to finding one highly scalable resource (10-15 templates/week)
- **Product:** Tool Brief automation will accelerate new feature delivery and reduce spec documentation burden on George
- **Risk Mitigation:** Georgemaine's 15-template buffer plan provides 3-week runway if contractor hire slips; candidate pipeline targets Wednesday submissions

---

## Overview

- **Lovable Upsell Approved:** The client accepted the $40k upsell for 10 templates/week and 10 guides/week.
- **Contractor Search Strategy:** The search for a new template contractor will prioritize candidates who can scale to 10–15 templates/week to support future upsells.
- **New Airtable Workflow:** A new Airtable base now centralizes template tracking and assignments, streamlining the production process.
- **Tool Automation Progress:** Nico is finalizing the "Lovable Tool Brief" automation, which will generate tech specs for new tools from simple inputs.

---

## Key Topics

### Lovable Upsell & Production Plan

  - The client accepted the $40k upsell, which includes:
      - **Templates:** 10/week (up from 5)
      - **Guides:** 10/week (down from 15 post-sprint)
  - **Rationale for Price:** The $40k price was approved because production volume is not a 1:1 cost driver. The previous 5→15 guide upsell was only $10k because removing manual review layers kept headcount flat, making the cost increase marginal.
  - **Guide Production:** Jenny will now produce 3 guides/day on Mon/Tues. Nico will use these as test data for the publishing automation.

### Template Contractor Search

  - **Goal:** Find a new contractor to increase template production from 5 to 10/week.
  - **Strategic Pivot:** The search now prioritizes candidates who can scale to 10–15 templates/week.
      - **Rationale:** This supports future upsells and simplifies management by consolidating work under one contractor.
  - **Contingency Plan:** If no suitable candidate is found by EOW, Georgemaine will create a 15-template batch to provide a 3-week buffer.
  - **Candidate Pipeline:** Marilia has shared the project with 3 new candidates, with submissions expected by Wednesday.

### New Airtable Workflow

  - Megan created a new Airtable base to centralize template tracking and assignments.
  - **Structure:**
      - **`Assignments` Tab:** Manages the production pipeline (Not Started → Ready to Publish → Published).
      - **`Keywords` Tab:** Organizes keywords by category with metrics (e.g., search volume).
  - **Process:**
      - Assign a keyword from the `Keywords` tab to the `Assignments` tab.
      - Track progress by adding links for the Lovable preview, Atlas workflow, and live page.
  - **Next Focus:** "Wedding websites" category, chosen for its simplicity compared to "startup landing pages."

### Tool Automation Development

  - Nico is finalizing the "Lovable Tool Brief" automation.
  - **Functionality:** Generates a detailed tech spec for a new tool from simple inputs.
  - **Progress:**
      - Prompt-building and Lovable Cloud enablement workflows are complete.
      - Fixing a conflict with Lovable's new prompt box UI.
  - **Status:** Full pipeline in Atlas expected by EOD today.

---

## Action Items

**Nicolas Castellanos (GrowthX, Engineering)**
- Test publishing bot w/ Jenny's 3 guides/day; ping Georgemaine w/ staging link
- Fix Tools prompt box/Adel; build Atlas pipeline; start batch testing tonight
- Push Fri templates; test automation; ping Georgemaine w/ staging link

**Georgemaine Lourens (GrowthX, Operations)**
- Update Marilia: source 10–15/week template contractor; share candidate pipeline/dates

**George Haikal (GrowthX, VP of Revenue)**
- Review template page; intro Megan to Sebastian; update Georgemaine on next steps

**Megan Dickey (GrowthX, Product & Operations)**
- Add wedding websites to Airtable Assignments; set status Ready to publish

---

## Transcript

[Beginning of meeting: small talk and weekend updates, then transitions to business]

**Georgemaine Lourens:** I saw a response to our upsell in the Growth External channel. How are you guys feeling about that?

**Megan Dickey:** It seems reasonable to me. Templates are ultimately doing better than guides, so it makes sense to do 10 guides a week versus the steady state of 15.

**George Haikal:** The only thing in my head is the reason we gave them such a good price on the editorial upsell from 5 to 15. We only charged them 10K more because the cost doesn't incrementally go up with the number of guides. We're tripling the volume of guides, but the headcount is staying the same because we're removing the publishing as a blocker and review in general. If we're only going up from 5 to 10, the cost doesn't need to be as discounted. So the answer is: should it be $45K or $40K?

**Georgemaine Lourens:** They're doing $25K a month right now, right?

**George Haikal:** Monthly, yeah.

**Georgemaine Lourens:** So we're essentially doubling production on both sides, but not the price.

**George Haikal:** Correct. But it makes sense because production volume is not one-to-one with price. Just because we double the volume, we're also removing a ton of other layers—review and human work. So it shouldn't be one-to-one. I'll probably get an answer in 15 minutes.

**Megan Dickey:** Great. It sounds like we're good to start testing the publishing bot.

**Nicolas:** Yes, I'll test it.

**Megan Dickey:** Jenny will now produce three guides per day on Monday and Tuesday. Will is back Wednesday. When she finishes the three, she can ping Nico and he can test the bot.

**George Haikal:** A few questions on the contractor, Georgemaine. Is it worth it to find one that can do the entire template capacity—10 templates/week—versus splitting five with Bruno and five with another? Would that make it easier for you to manage?

**Georgemaine Lourens:** I think that would be even better. But if we can just find one, that would be great. And if we can find someone who can do 10, maybe we can even upsell 15.

**George Haikal:** Right, we're not going to stay at 10 for long if we do it right. When you're talking to contractors, make it clear there's an opportunity to grow. We're aiming to start now at 5, but the ideal person can grow to 10 or 15 per week.

**Georgemaine Lourens:** I can send Marilia a message about that. Worst case scenario, if we don't have a good contractor by end of week, I can spend three days making a 15-template batch. That gives us breathing space for three weeks while we search.

**Megan Dickey:** Do you feel that's feasible?

**Georgemaine Lourens:** Yeah, should take three days or less. But I'll assume we'll find someone by end of week. Marilia just shared the project with three new candidates, and submissions are expected by Wednesday.

**George Haikal:** Nice.

**Georgemaine Lourens:** Did you guys see the template page? Do you want to share it with Sebastian, or leave it until the deal is made?

**Megan Dickey:** It looked really good. I'm not sure what the process is.

**George Haikal:** I haven't looked yet, but if it looks good, it'd be the perfect time to intro Megan to Sebastian. I'll look at it after the Lovable call and we can get it going with Sebastian.

**Georgemaine Lourens:** Sebastian was looking for design ideas on where to take this. Can we pass it off as an idea so his design team can riff off it, or does it need iteration?

**George Haikal:** We'll get that done today and let you know.

**Nicolas:** On Tools, I have the workflow that builds the prompt and the workflow that enables Lovable Cloud. Now I'm dealing with a new prompt box from Adel that changed how you respond to Lovable. The template builder we have is probably failing with that. I'll get that fixed. By end of day, I should have the full pipeline in Atlas orchestrating everything.

**Nicolas:** On templates, I'll push the ones you sent me last Friday today and test the automation with them.

**Georgemaine Lourens:** Could you ping me once you have a staging link up for review?

**Nicolas:** Yep.

**Megan Dickey:** I tweaked the Airtable to track everything that's been published and make it clearer. The Assignments tab manages the pipeline: Not Started → Ready to Publish → Published. You can pop in the Lovable preview, Atlas link, and live link. Categories include graphic design portfolio, general portfolio, landing pages, e-commerce, and resume. These are based on top keywords Will pulled from a Google Sheet.

**Georgemaine Lourens:** So as soon as we have one keyword, we add a line with whatever status we want to start in?

**Megan Dickey:** Right. You can see all the keywords by category. These are based on Will's sheet, but there are tons more. Once you decide on an assignment, you add a record.

**Georgemaine Lourens:** Are we summing up potential search volume, keyword difficulty, and cost per click on the assignments?

**Megan Dickey:** We have total volume. I could add the others, but I think total volume is enough for now.

**Georgemaine Lourens:** For the next one, we should focus on wedding websites. That's the easiest compared to startup landing pages, which are complex.

**Megan Dickey:** I'll set wedding websites to Ready to Publish.

**Megan Dickey:** I also started keyword research for apps and tools, still working through it.

**George Haikal:** This is awesome, Megan. This looks great.

**Megan Dickey:** I followed Marcel's video step by step. Took a few hours, but Airtable can get confusing quickly, so this breakdown really helped.

**George Haikal:** Isn't it amazing how it all comes together? It's step by step, but at the end it's insanely robust.

**George Haikal:** We're approved on the $40K, by the way. This is good stuff and a starting point. A lot more to come if we do it right.

**Nicolas:** I made good progress last week. Got the workflow that builds the prompt and the workflow that enables Lovable Cloud. What I'm dealing with now is a new box for answering questions in Lovable prompts. Working on that, but I should have the whole thing by end of day.

**George Haikal:** Could you send the workflow or is it in Flow?

**Nicolas:** Yes, it's in Flow. I just pushed it. Look for "Lovable Tool Brief."

**George Haikal:** Will it work just from normal inputs?

**Nicolas:** Anything at all. You can be as scripted as you want. If you want specific features, you can add that. The workflow will generate a tech spec that works as a prompt for Lovable. That goes into a file in Lovable, and we have the piece of the workflow for generating templates that will have Lovable do a step-by-step through all the things.

**George Haikal:** How often are you including example images and personas?

**Nicolas:** Personas, always, when you want. Usually you want to build a tool for a specific persona, but you don't need to add it if you don't want to. It's optional.

**Georgemaine Lourens:** You should make this a dropdown for the artifacts.

**George Haikal:** Under brand, these should eventually be pulled in—the different personas. I go in and pull out persona one, persona two and make them individual ones.

**Georgemaine Lourens:** Can you select those when you generate? The flow isn't connected to Fathom.

**George Haikal:** Right, because if you don't manually input the persona into the brand pulling from the artifact, you won't have one to select for generate. Don't let that distract you for now.

**George Haikal:** I'll look at this after, but this is amazing. How confident are you that we could start testing this?

**Nicolas:** Tonight I'll start cranking through and testing it.

**George Haikal:** Amazing. That's awesome. Super exciting.

**George Haikal:** I think that's it?

**Megan Dickey:** Yeah.

**George Haikal:** Great work, everybody.

**Megan Dickey:** Thanks, guys.

**Georgemaine Lourens:** Have a great rest of your day. See you guys on Slack.

**George Haikal:** Likewise. You guys too. Bye.
