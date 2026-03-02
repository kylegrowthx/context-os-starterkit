# Webflow <> GrowthX - 2026 Executive Planning Session

<metadata>
date: 2026-02-04
time: 19:01 UTC
duration: 57 minutes
organizer: team@growthxlabs.com
participants: Kelly We, Meg Murray, Kirat Chhina, Colin Lateano, Michael Huard, Jason Gong, Luke Stahl, Vivian Hoang, Anushri Gupta, Darin LaFramboise, Rachel Wolan, Vic Plummer, Zach Plata, Liz Kushnereit, Raymond Camden, Ismail Ajagbe, Kirkland Gee, Team GrowthX
fathom_recording_id: 119785489
fathom_url: https://fathom.video/calls/554059475
share_url: https://fathom.video/share/GwsrTZHnsFY8tfukG5Sm-u7gsf-mbzzC
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

GrowthX and Webflow agreed to pivot content strategy from underperforming use case guides to programmatic SEO (PSEO) targeting middle-funnel intent, while maintaining strong integration page performance, and proceeding with unstyled code components as a new workstream. Clear next steps include PSEO topic prioritization, renewal scope documentation, and code component prototyping with standardized approach to styling via exposed props and README documentation.

---

## Context

This is a quarterly business review (QBR) between GrowthX and Webflow's product and marketing leadership, occurring seven months into a content partnership focused on developer SEO and technical enablement. Q4 2025 showed strong performance from integration pages (600+ published, 28 #1 rankings, 105 first-page keywords) but disappointing traction from use case guides despite rising impressions. The meeting addresses a strategic inflection point: whether to double down on integration pages, explore programmatic SEO to capture earlier-funnel decision-making queries, and how to execute on code components that GrowthX is building as part of an expansion workstream. A core tension exists around brand positioning: Webflow's preference for "authentic" developer-first content conflicts with the data-driven reality that SEO-optimized templates (what GrowthX calls "programmatic content") appear to win AI answer engine results more effectively than product-grounded alternatives.

---

## Relevance

- **Strategic pivot and content funnel architecture**: Understanding how GrowthX structures multi-stage content funnels (PSEO → integration pages → code components/DevDocs) and interlinking strategy to compound traffic and conversion opportunities.
- **AEO/SEO strategy tension**: How to balance authentic, product-grounded developer content against programmatically optimized templates that win AI visibility—relevant to anyone navigating the SEO→AEO transition.
- **Programmatic content authenticity debate**: Colin Lateano's pushback on "SEO slop" and the resolution (data-driven approach to show what actually works in AEO) is a template for client conversations around content quality vs. performance.
- **Code component design system**: The decision to use unstyled primitives with exposed props and mandatory READMEs (rather than opinionated styling) applies to any component library strategy.
- **Scope management and renewal planning**: How GrowthX frames capacity reallocation (moving away from low-performing use case guides toward PSEO) and distinguishes between existing scope vs. add-ons in contract renewal conversations.
- **Working across agency and client teams**: The collaboration model between GrowthX (strategy + content execution), Webflow (product/marketing input), and Kirkland/technical implementation reflects how to coordinate on integrated projects.

---

## Overview

- **Strategy Pivot:** Shifting from use case guides to programmatic SEO (PSEO) to capture middle-funnel intent (e.g., "how to build X in Webflow"), linking to existing integration pages and new code components.
- **PSEO Content Debate:** Webflow prefers authentic, product-grounded content over "SEO slop" (e.g., listicles). GrowthX will provide data showing that programmatic content, while less authentic, is effective for winning AI answer engine optimization (AEO).
- **Code Component Plan:** The initial 100 components will be unstyled primitives (e.g., buttons, sliders) that inherit a user's design system via exposed props, requiring a `README` for each component to guide setup.
- **Scope & Renewal:** The PSEO pivot fits the current contract by reallocating capacity from integration pages. Top-of-funnel educational content is a potential add-on for the renewal.

---

## Key Topics

### Q4 Performance & Strategy Pivot

  - **Integration Pages:** High-performing workstream.
      - **Status:** \~600 of \~700 pages published.
      - **Results:** 28 \#1 keywords, 105 first-page keywords.
  - **Use Case Guides:** Underperforming workstream.
      - **Status:** \~20 published; scaling to 5/week.
      - **Results:** Low clicks despite rising impressions.
  - **2026 Proposal:** Pivot capacity from use case guides to PSEO.
      - **Workstreams:**
        1.  **Integration Pages:** Maintain & optimize.
        2.  **Programmatic SEO (PSEO):** New focus.
        3.  **Code Components:** New workstream.

### Programmatic SEO (PSEO) Strategy

  - **Goal:** Capture middle-funnel intent (e.g., "how to build a database in Webflow").
  - **Funnel:** PSEO → Integration Pages → Code Components/Dev Docs.
  - **Webflow Concern:** Avoid "SEO slop" (e.g., listicles) to maintain brand authenticity.
  - **GrowthX Rationale:** Programmatic content is effective for winning AEO.
  - **Decision:** GrowthX will present data to inform a joint strategy.

### Code Component Execution Plan

  - **Priority:** Start with unstyled primitives (e.g., buttons, sliders) to prove the system, then add complexity.
  - **Styling:** Components will be unstyled to ensure they inherit a user's design system.
      - **Mechanism:** Expose props for users to connect their own variables (e.g., `buttonText` prop connects to a site's primary text color variable).
      - **Requirement:** Each component needs a `README` explaining its props and how to connect them.
  - **Development:**
      - **Repo:** Use the `Webflow examples` GitHub repo.
      - **Workflow:** Fork the repo for development, then merge approved components into the main branch.

---

## Decisions & Commitments

**Strategy Direction**
- Agreed to pivot content capacity from use case guides (low-performing despite scaling to 5/week) to programmatic SEO targeting middle-funnel decision queries ("how to build X in Webflow").
- Commit to maintaining and optimizing existing integration pages while establishing PSEO as primary new growth lever.
- Added DevDocs to the content funnel interlinking strategy (previously missing); acknowledged that not all activation pathways should lead to code components—some point to existing API docs and guides.

**PSEO & AEO Methodology**
- GrowthX will provide data-driven evidence on whether programmatic SEO templates (including comparison content that looks like "listicles") actually win AI answer engine results, versus Webflow's aesthetic preference for product-grounded content.
- Decision to decouple strategic recommendation from execution: GrowthX will present opportunity + evidence, Webflow decides whether to proceed, and both revisit after gathering results.
- Agreed to approach content on a tiered basis: glossary/dictionary content (lower authenticity, high traffic), Reddit/Hacker News tier (community-driven, opinionated), and product-integrated approaches (most authentic, requires DevRel/product marketing involvement).

**Code Components**
- Confirmed that initial 100 components will be unstyled primitives (buttons, sliders, etc.) to test the system before complexity.
- Styling approach: components expose props that users connect to their own design variables; no opinionated default styles imposed by Webflow or GrowthX.
- Every component requires a README documenting exposed props and how to wire them to a user's design system.
- App templates are a lower-priority follow-up; focus is on filling component gaps first.

**Renewal & Scope**
- Current contract covers two lanes: integration pages + code components. PSEO pivot fits within existing capacity by reallocating use case guide production.
- Top-of-funnel educational content (beginner dev concepts) is a potential add-on for renewal, not in current scope.
- Liz to draft renewal scope document clarifying three lanes (integrations, PSEO, code components) and coverage plan.

**Collaboration & Feedback Loops**
- Colin committed to adding GrowthX bots to GA4 for real-time performance tracking (previously delayed 4 months); GSC access already in place.
- Agreed that Webflow's internal marketing and positioning shifts don't require immediate PSEO strategy updates unless user search intent actually changes.
- Colin to poll Webflow team (via Slack channel) on priority code component gaps to guide Kirkland's build sequencing.

---

## Open Questions

**PSEO Content Quality & Approach**
- What specific templates and topic framings qualify as "authentic" versus "SEO slop"? Webflow to decide after seeing GrowthX data on AEO performance.
- How do we format and maintain consistency at scale for templated programmatic content across 1,300+ identified high-intent keywords?
- Should comparison/listicle-style content appear in Webflow blog (publishing decision) or only in developer docs?

**Code Components & Testing**
- What is the complete list of priority component gaps from Webflow's perspective? (Colin to poll team; Kirkland to work from emerging patterns if list is unavailable.)
- How do we validate that unstyled, prop-based components work consistently across vastly different Webflow site design systems? (Kirkland to test across 5+ templates with different styling approaches.)
- Should components live in a shared repo with other Webflow examples, or in a standalone repository?

**Content Funnel Measurement**
- What counts as "success" for PSEO, integration pages, and code components individually? How do we measure compounding effect across the funnel?
- How often should Webflow update GrowthX on internal marketing/positioning shifts that might affect content strategy? (Answer: only major intent shifts, not tactical messaging changes.)
- What Amplitude/product engagement metrics should GrowthX track beyond GA4 and GSC to understand conversion signal from PSEO → integration pages → adoption?

**Organizational Readiness**
- Can Kirkland work autonomously on component development, or does every implementation decision require Webflow sign-off? (Implied: focus on process documentation first, then build.)
- What is the approval workflow for code components before they merge into the public examples repo?

---

## Action Items

**GrowthX – Liz Kushnereit**
- Add DevDocs to interlinking diagram; share updated diagram w/ Colin
- Draft renewal scope doc clarifying three lanes (integrations + programmatic + code components) and coverage plan; send to Colin
- Prepare data-driven evidence on whether programmatic SEO (listicle-style comparison content) wins in AI answer engine results

**Webflow – Colin Lateano**
- Add GrowthX bots to GA4; share access w/ Jason + Liz
- Schedule PSEO topics working session w/ Liz, Jason, Luke, Vivian (post-RKO, target late Feb)
- Schedule scoping/coverage sync w/ Liz re: renewal discussion
- Send Loom video + technical docs to Kirkland explaining code component styling approach, prop exposure, and testing methodology
- Poll Webflow team (via Slack) for priority code component gaps; share prioritized list w/ Kirkland

**Webflow – Zach Plata**
- Add Kirkland to code components GitHub repo; share common naming scheme and existing component examples
- Clarify whether to add new components to existing Webflow examples repo or create standalone repo for open-source visibility

**GrowthX – Kirkland Gee**
- Fork code components repo for development (do not commit to public repo until approved)
- Build 5–10 initial components as primitives (buttons, sliders, etc.) with unstyled approach and exposed props
- Write README documentation for each component explaining prop connections to design system variables
- Test components across 5+ different Webflow site templates with varying design system approaches to validate consistency

---

## Transcript
**Liz Kushnereit:** This meeting is being recorded.

**Kirkland Gee:** Hello.

**Liz Kushnereit:** Hi, Vivian.

**Vivian Hoang:** Hi.

**Vivian Hoang:** I don't think we've met, but I have the SEO lead here at Webflow.

**Liz Kushnereit:** I'm just going to sit in on the call.

**Liz Kushnereit:** Yeah, great.

**Liz Kushnereit:** We're happy to have you.

**Liz Kushnereit:** I think Jason's jumping in as well.

**Liz Kushnereit:** Thank you.

**Liz Kushnereit:** Thank you.

**Liz Kushnereit:** .

**Liz Kushnereit:** Thank you.

**Jason Gong:** Thank you.

**Jason Gong:** Thank you.

**Jason Gong:** Thank you.

**Jason Gong:** Everyone.

**Liz Kushnereit:** I think we're just waiting on call.

**Jason Gong:** Thank Thank you.

**Jason Gong:** Thank

**Jason Gong:** Oh, there's the man.

**Colin Lateano:** Colin's here.

**Liz Kushnereit:** Oh, great.

**Liz Kushnereit:** Okay.

**Liz Kushnereit:** Well, thanks, everyone.

**Liz Kushnereit:** Full house today.

**Liz Kushnereit:** Cool.

**Liz Kushnereit:** So I put together a little bit of a hefty QBR for us to go through.

**Liz Kushnereit:** And then if we have time, I think.

**Jason Gong:** Liz, you're showing your Slack window.

**Liz Kushnereit:** I don't know.

**Liz Kushnereit:** Oh, sorry.

**Liz Kushnereit:** That was not intentional.

**Liz Kushnereit:** Thanks.

**Liz Kushnereit:** How's that?

**Liz Kushnereit:** Good.

**Liz Kushnereit:** Okay.

**Liz Kushnereit:** So we'll go through a foundations check, make sure we're still aligned on vision, existing work streams, how Q4 went, our go forward strategy, what we're thinking, Q1, 2026 in general, a conversation about AI visibility, and then some other opportunities we'd like to talk about.

**Liz Kushnereit:** The go forward strategy has a bit of a mention of code components with some open questions we have.

**Liz Kushnereit:** So if there's some extra time, it'd be great.

**Liz Kushnereit:** Great to talk through those with Kirkland on the call.

**Liz Kushnereit:** And yeah, and then so feel free to interrupt me as we go, but it should kind of all flow pretty well.

**Liz Kushnereit:** So to reiterate our foundations check, think, especially for me needing to go a bit back in time about the original relationship and what the goal was of that, I just want to reaffirm the content principles that we are approaching this with.

**Liz Kushnereit:** So especially as we explore expansion and other opportunities and where we want to take this content, we want to reiterate that we're staying consistent with developer-first product-grounded content that's truly useful, especially in 2026 with so much AI-generated content.

**Liz Kushnereit:** I think what the user actually uses and what's rewarded is also just something that's truly, truly useful.

**Liz Kushnereit:** So that's just kind of a slide to reiterate that.

**Liz Kushnereit:** I think you guys can test me on that as we go through the presentation, and then we can have kind of an open conversation.

**Liz Kushnereit:** you.

**Liz Kushnereit:** you.

**Liz Kushnereit:** About it.

**Liz Kushnereit:** So our existing lanes, looking back at Q4, obviously integration pages of our two lanes, our first being integration pages is our big heavy lifter, pretty successful.

**Liz Kushnereit:** I know we were really only looking at the kind of performance we can track in Google Search Console, but these did really, really well and we're continuing to work on them.

**Liz Kushnereit:** I think we published something like 600.

**Liz Kushnereit:** There's maybe like 100-ish left.

**Liz Kushnereit:** And yeah.

**Liz Kushnereit:** And then yesterday I was looking up, since the last time we met for QBR, we now have 28 number one Webflow Plus tool keywords and then 105 on the first page, which is, we should have those, but it's just cool to see how those worked out.

**Liz Kushnereit:** And then for use case guides, this is a more recent work stream we've been launching.

**Liz Kushnereit:** And so across the past two months, we've published about 20 and these are what those results look like.

**Liz Kushnereit:** So not a ton of clicks.

**Liz Kushnereit:** We are seeing...

**Liz Kushnereit:** A lot of early indications of traffic and impressions, but overall just upward frequency, but not as huge of a lift as we saw with integrations, which could be for a number of reasons.

**Liz Kushnereit:** And also we're scaling these to like, I think five a week is the output we've set up with.

**Liz Kushnereit:** And then I mentioned the top query there when I was looking into this is, can you build a database in Webflow?

**Liz Kushnereit:** And that kind of feeds into the rest of this conversation.

**Liz Kushnereit:** So our go forward strategy and where we'd like to go.

**Liz Kushnereit:** So we talked about this a little bit in last week's weekly call, but I wanted to get a lot deeper into it.

**Liz Kushnereit:** So the proposal that we have for this quarter and this year, and as we like talk about renewing the contract, is to move into these three lanes, which is maintaining integration pages.

**Liz Kushnereit:** And I can better define and talk about what that looks like in this kind of new structure, but also optimizing or pivoting use case guides into programmatic content.

**Liz Kushnereit:** And so he.

**Liz Kushnereit:** Here I put some examples of what those templates would look like.

**Liz Kushnereit:** And this is based on some research we've done about where we think the biggest opportunity is.

**Liz Kushnereit:** And I'll talk way more in depth about this in a minute.

**Liz Kushnereit:** And then also code components.

**Liz Kushnereit:** Again, we're already having this conversation and I've kicked this off this week.

**Liz Kushnereit:** And so these would be our three lanes.

**Liz Kushnereit:** And now I want to go into how they kind of all make sense.

**Liz Kushnereit:** So I'll start with programmatic SEO, even though it's sort of our second lane, but it paints the entire picture.

**Liz Kushnereit:** It provides the context for our other two lanes.

**Liz Kushnereit:** But with this content, we'd like to shift into more decision capture and less of like very specific extension of an integration page.

**Liz Kushnereit:** And now we're trying to go earlier in the decision-making process, whereas like use cases a little bit after.

**Liz Kushnereit:** And from our research, we saw about 1,300 high intent keywords we've already identified that we could pursue.

**Liz Kushnereit:** And that's just from a little bit of research.

**Liz Kushnereit:** I added.

**Liz Kushnereit:** These graphs on the right-hand side for programmatic programs we've done for RAMP and SIT.

**Liz Kushnereit:** And so you can just kind of let the data speak for itself about the approach we took there.

**Liz Kushnereit:** The idea is that we'd be able to scale this content pretty quickly once we've established our templates and how we do those content engines.

**Liz Kushnereit:** And so that would be mostly a growthx thing, really not a lift for Webflow unless some web dev is needed about putting this into the CMS.

**Liz Kushnereit:** And so what this looks like all packaged together is that our programmatic content would be pulling all the weight of capturing intent.

**Liz Kushnereit:** So how to build a database in Webflow, Webflow CMS automation.

**Liz Kushnereit:** And then that content, once the user has, you know, decided in that template that there's some comparison given about different tools that you can build a database with depending on your use case.

**Liz Kushnereit:** And so if you're doing X thing, maybe this tool is better, maybe this tool, maybe that tool, but whatever that.

**Liz Kushnereit:** Internally links into an existing integration page.

**Liz Kushnereit:** Integration pages, we'll talk about become optimized.

**Liz Kushnereit:** And then based on setting up that integration, what's like the logical next step enablement beyond integration is actually building.

**Liz Kushnereit:** And that can also lead to our internal linking or some sort of drive mechanism into our code components.

**Liz Kushnereit:** And so I put together this diagram for what that looks like in a specific use case.

**Liz Kushnereit:** So programmatic SEO here, how to build an e-commerce website, Webflow.

**Liz Kushnereit:** We answer that with one of our programmatic pieces, right?

**Liz Kushnereit:** Some kind of job base.

**Liz Kushnereit:** We're giving very specific recommendations.

**Liz Kushnereit:** We have a decision gate for the user where they decide like which tool they actually want to use to do that with.

**Liz Kushnereit:** That drives them to their Webflow integration or existing pages.

**Liz Kushnereit:** And then now they want to know how to build an add to cart button.

**Liz Kushnereit:** And then we can also drive them to code components.

**Liz Kushnereit:** So this is kind of what the compounding.

**Liz Kushnereit:** And content structure looks like and what we're envisioning moving forward.

**Liz Kushnereit:** I think what I want to point out as we have this diagram up is that each work stream or each lane can be siloed success, like can be a successful silo.

**Liz Kushnereit:** It doesn't necessarily depend on the success of another in order for it to be.

**Liz Kushnereit:** think integration pages proves that.

**Liz Kushnereit:** But they do have the ability to help the other, right?

**Liz Kushnereit:** And so there could be some sort of exponential uptick in how these pages perform based on how we connect all of this content together.

**Colin Lateano:** Can you explain a little bit about how the content would be connected together?

**Colin Lateano:** Knowing that these are individual lanes, is there a job to then reconnect and figure out our inventory and how they interlink?

**Liz Kushnereit:** Yes.

**Liz Kushnereit:** So with integration pages, that would be sort of the next step, the kind of basic, like we need to refresh them because this is sort of the middle step.

**Liz Kushnereit:** So as we're producing programmatic, of course, we'll include.

**Liz Kushnereit:** include those internal linking to our existing pages, but we do need to go back in time with integration pages, make sure those are accurate because we have done some housekeeping and seen that some of the tools either change name or use case or something or another, some screenshots, standardizing that page structure and the internal linking, we do need to do that lift to make sure we're moving into the different work streams, and then building our CTAs and what those look like.

**Liz Kushnereit:** And I haven't quite defined or given a prototype of what sort of CTA it would be, but that is precisely the idea of how they would link.

**Liz Kushnereit:** Yeah, and then, and so throughout this presentation, I just put like what success looks like for each work stream to provide our own suggestion and recommendation of that.

**Liz Kushnereit:** So for integration pages, of course, this is just the same sort of momentum about increasing impressions and internal linking to components and seeing what that looks like.

**Liz Kushnereit:** And then with code components, I just sort of dropped this in, but this is kind of like a higher view.

**Liz Kushnereit:** But- So that that

**Liz Kushnereit:** And much different goals, but looking for strong engagement, reuse and reference in different workflows, and then positive qualitative feedback from developers.

**Liz Kushnereit:** For this one, that's a lot harder to track, but not something that we can't entirely build out, would just require a bit more thinking.

**Liz Kushnereit:** And then I'd left some open questions here for us to talk about if we have some extra time after the call or at the end of my presentation.

**Liz Kushnereit:** And then before I check in with y'all, I do want to talk about AEO tracking and visibility and how this also relates to this kind of compounding content structure.

**Liz Kushnereit:** But specifically for this programmatic lane, I think how we would approach this is we would immediately take all of those questions that we're trying to answer and that we're building these programmatic pieces for and put them into an AI visibility tool and then constantly be tracking how those are performing.

**Liz Kushnereit:** So we're also making sure that Webflow is...

**Liz Kushnereit:** The answer to these questions.

**Liz Kushnereit:** And that is a bit of more of an experiment and a little bit different than what we've done because we didn't have the ability to do so.

**Liz Kushnereit:** And so now we'll be able to do that and be able to ensure and potentially update our strategy or our approach if needed that we are winning that AI answer.

**Liz Kushnereit:** So I'll stop there, but that's basically the big proposal for moving forward in 2026 with our existing work streams.

**Liz Kushnereit:** If there's any questions or thoughts, anything at all?

**Colin Lateano:** Lots of thoughts.

**Colin Lateano:** Okay.

**Colin Lateano:** I'm trying to figure out how I want to frame this.

**Colin Lateano:** Can we go back to the interlink slide?

**Liz Kushnereit:** I don't know.

**Liz Kushnereit:** This is a great slide.

**Colin Lateano:** The workflow diagram.

**Colin Lateano:** I, I, this is, I, I would add one.

**Colin Lateano:** It's done remains.

**Colin Lateano:** at dapat.

**Colin Lateano:** Carbet.

**Colin Lateano:** Onion.

**Colin Lateano:** Thank

**Colin Lateano:** Well, I would say there's one other part of interlinking is in our activation and mutation, not every pathway is going to lead to the net new code components, apps, samples, whatever it is, what we would like to see on this.

**Colin Lateano:** And this is the strategy that we worked out in summer.

**Colin Lateano:** So I'm really glad to see that it's taken shape.

**Colin Lateano:** I know it takes time to do it.

**Colin Lateano:** So I appreciate you calling it out and drawing it.

**Colin Lateano:** I'd love to reshare this with other people internally.

**Colin Lateano:** I would love to turn the activation and implementation to also include in a separate but same pillar or same column our dev docs because part of this is we may not be using GrowthX to edit and modify the dev docs, but sometimes the answers in the integration page of how you activate and build are not net new components we need to offer a customer.

**Colin Lateano:** Sometimes it's just you need to call a certain API and this is where we need you to go.

**Colin Lateano:** And so as long as we know that our interlinking strategy.

**Colin Lateano:** The of this is net new things to help make onboarding a first success faster, but also interlinking to our existing guides or existing references in our API strategy.

**Colin Lateano:** I think this is a really great funnel that we're trying to create to drive both early observation into time of first success.

**Colin Lateano:** I'm very interested in, if that makes sense in terms of strategy, how we would make determinations of the high intent search traffic and the job-based programmatic SEO.

**Colin Lateano:** I know earlier you shared the methods you've done with ramp and then those similar strategies, were they in the same vein or was ramp much closer to real decisioning or just general traffic capture of like, what is payroll?

**Colin Lateano:** And are we approaching that same path in this programmatic method?

**Liz Kushnereit:** Yeah, I think this is definitely...

**Liz Kushnereit:** More complex and more compounding than I think we've done with any other client to date.

**Liz Kushnereit:** So it was not drawing that many lines to other pages.

**Liz Kushnereit:** But I do think what your feedback is very helpful, and I didn't consider it in here because I guess we don't own those pages, right?

**Liz Kushnereit:** But absolutely, I think we would be able to build that into this funnel structure about how we also drive to DevDocs and just keep moving around.

**Liz Kushnereit:** I think I would need a little bit to work through what that looks like, but I think that that's actually very intuitive and the natural next step.

**Liz Kushnereit:** And the only reason it's not here is because I didn't think about it.

**Liz Kushnereit:** Yeah.

**Colin Lateano:** So, okay.

**Colin Lateano:** But in the other model where your previous experience of generally just capturing high-intent search traffic or just unique long-tail keywords, ramp, card issuance, questions, or things like that, is that still the topic line that you'd want to aim for for Webflow?

**Colin Lateano:** Or-

**Colin Lateano:** Are we having a much more opinionated view of the topics that we want to talk about?

**Liz Kushnereit:** Less opinionated?

**Liz Kushnereit:** definitely would be more because, again, there's something that's not true.

**Liz Kushnereit:** Like with Webflow, we also have these very delicate partner relationships, right, or that we want to always support that.

**Liz Kushnereit:** So it's opinionated in the sense that Webflow is what you're doing this with.

**Liz Kushnereit:** Ideally, right, like only in that case, Webflow versus Webflow competitors.

**Liz Kushnereit:** But when we're doing our programmatic content going through multiple tools, so let's see, like what our templates look like, those are less opinionated.

**Liz Kushnereit:** If I'm answering your question, I'm not sure that I am, but like those are more so just like these are your use cases.

**Liz Kushnereit:** We're trying to answer it.

**Liz Kushnereit:** These are the questions that like beginner devs put into chat GPT and stuff like that.

**Liz Kushnereit:** And then this is how we do it.

**Liz Kushnereit:** And then the more difficult part.

**Liz Kushnereit:** Which is something we're exploring with other clients.

**Liz Kushnereit:** It's like, how do you still recommend Webflow in that response?

**Liz Kushnereit:** Which is a bit more nuanced and experimental, and I don't fully have an answer to that.

**Liz Kushnereit:** But that is sort of how I said, yeah.

**Jason Gong:** your question like being opinionated about like some technical solution or maybe more being opinionated about like, hey, Webflow is better than this tool?

**Colin Lateano:** It's the latter.

**Colin Lateano:** I'm, because if I think about, I came from a competitor of Ramp.

**Colin Lateano:** We did a lot of back and forth.

**Colin Lateano:** How do we beat Ramp at market?

**Colin Lateano:** And we don't.

**Colin Lateano:** Bill.com.

**Colin Lateano:** But the whole thing of this domain was there's not a lot of strong interest to have a programmatic SEO plan of top 10 CMS companies and Webflow is number one as a listicle.

**Colin Lateano:** And so I'm curious, what is the template we're trying to propose to be still?

**Colin Lateano:** Helpful and informative for answers, but not, I'm not going to say SEO slop, but not a method of saying best web, visual designing APIs, Webflow is number one, Figma is number two.

**Colin Lateano:** That type of opinionated view, I think, is not where we struggled before, because the original GrowthX plan was developer SEO.

**Colin Lateano:** And the first articles that we were getting at the door were, how do we take the standard approach to SEO of listicle or highly opinionated Webflow is the best, rah, rah, and not so much.

**Colin Lateano:** Like, line nine here is very interesting, but I'm curious how we are going to format that at scale and maintain a view of these types of templated answers and topics.

**Jason Gong:** Yeah, I mean, let's feel free to.

**Jason Gong:** Chime in.

**Jason Gong:** But yeah, so I guess we did start this engagement.

**Jason Gong:** We tried a few of the like, you know, top headless CMSs, I think.

**Colin Lateano:** I think we tried some stuff like that.

**Jason Gong:** Yeah.

**Jason Gong:** I think the spectrum here is like, it's like that stuff.

**Jason Gong:** I think it's hard or just flat out, you know, you guys don't really want to do at this sort of scale.

**Jason Gong:** There's the example that Liz used of like, how do you build a e-commerce website?

**Jason Gong:** That's like, still like very top of the funnel.

**Jason Gong:** You talk about products in there.

**Jason Gong:** But that one is like, maybe a bit more unoffensive, like the way you could write that.

**Jason Gong:** And then there's some stuff in the middle that I think we'll just have to work out maybe with getting an approval workflow of like, like, for example, like, what is the best way to host an e-commerce website?

**Jason Gong:** Like, I don't know where that falls.

**Jason Gong:** And you're like, hey, we don't want to crap on competitors or whatever.

**Colin Lateano:** Yeah.

**Jason Gong:** So I think, I guess high level, it's like, we see an opportunity there.

**Jason Gong:** We haven't really fully done the work yet.

**Jason Gong:** But the work there is to kind of just like flag.

**Jason Gong:** that.

**Jason Gong:** Yeah.

**Jason Gong:** Yeah.

**Jason Gong:** And then I think the stuff that you guys have that maybe we don't have with other customers is like some of these articles, it's pretty clear that cool.

**Jason Gong:** It's like an SEO slop type top 10 tools that really drives the AI answer.

**Jason Gong:** And to be honest, like when we look at that space, like at least at the moment, that is what shapes a lot of these like product decision type of like prompts and chat GPT.

**Colin Lateano:** Okay, I think that's, so I really want in this conversation, I really want to say, if that is your opinion, and you have data to say, that is actually driving answer engine responses.

**Colin Lateano:** There is a world that we can probably have a great discussion on.

**Colin Lateano:** We're coming from a gut feeling, a vibe of, we don't want to be in a space of producing what we feel is SEO slop.

**Colin Lateano:** But truth be told, if that's actually driving

**Colin Lateano:** And there's a world where I can swallow my pride and say, sure.

**Colin Lateano:** I just would love to, I don't think we had, and maybe this is just, I didn't do a good job of fostering the agency relationship of just, I'd love to understand your opinion of it, of what is the best strategy to perform and actually succeed here.

**Colin Lateano:** Because at the of the day, we want to get more eyes on our developer platform and we want to get more adoption.

**Colin Lateano:** It is, we have a strong stylistic preference to not look like the others.

**Colin Lateano:** But if you're telling me that's actually what's driving chat GPT responses, then maybe we need to have a conversation about what these templates and topics are.

**Jason Gong:** Yeah.

**Jason Gong:** I mean, I think our goal there is like, I mean, whether it's on the SEO side or on the like AI visibility side, just like do a bit of work to paint that picture.

**Jason Gong:** Because like there will be content there that like, I think, you know, we can just start working on.

**Jason Gong:** And then there's some stuff that kind of borders.

**Jason Gong:** There's this category that we haven't totally done before.

**Jason Gong:** And there's also the, like, I see Vivian here.

**Jason Gong:** I know you guys, you know, you all work on that area as well.

**Jason Gong:** So that's probably another consideration.

**Jason Gong:** There's always this overlap when we start publishing on the blog.

**Jason Gong:** So I think that's just work on our side, but just like to show an example, it's like, you know, this is like another client.

**Jason Gong:** I mean, they still have this problem with like cursors, just kind of like all anyone ever thinks about and nobody thinks about the other guys.

**Jason Gong:** But like some things we've been able to get in front of this, like we're never, it's going to be really, really hard to get in front of who's the best AI coding assistant.

**Jason Gong:** But like there are these kind of like niches that we're targeting.

**Jason Gong:** And if you look at, you know, the stuff that shapes them, like we've done a pretty good job with Augment, especially with just like, you know, getting in here.

**Jason Gong:** Right.

**Jason Gong:** And this question six months ago did not mention them at all.

**Jason Gong:** And like, you know, for what it is, you know, these articles, I'd love to know your take if it's slop or not, but it's like.

**Jason Gong:** They are programmatic, right?

**Jason Gong:** Like they do at the end of the day look like SEO content, but at least for a pretty big category of prompts that like are at the bottom of the funnel, people researching products, like this is the stuff that shifts mentions there.

**Jason Gong:** So we'll paint that picture and then I think there is a decision, but we don't have to make that right now.

**Colin Lateano:** Okay.

**Colin Lateano:** I, the, the takeaway I'd love to have on this is because we're talking about how I'm reading the political correctness of saying how hard it is to work with Webflow in terms of actually how to approach an SEO strategy.

**Colin Lateano:** And so I'm, I, I'd love to come from set this next, have this QBR and set our next strategy talk about what is your, as an agency that we are paying for the strategic advice, what is the best path forward to actually win in this?

**Colin Lateano:** In these answers, in these long-tail questions, less from how do we stylistically want to appear in search results, then I want to get results.

**Colin Lateano:** And so if the answer is these listicles do work, I'd love us to actually have that equal playing field.

**Colin Lateano:** Please come bring the evidence and conversations so I'm able to come back and defend the choices being made here.

**Jason Gong:** I mean, I think it makes sense to decouple the, like, strategy work from, like, can we actually, like, spend time executing on it?

**Jason Gong:** You know, that shouldn't stop us from at least flagging the opportunity for you all.

**Colin Lateano:** And the second part I'd love to understand, at least before we jump to the next topic line, is what can we provide data, feedback loops, in any manner to know that what you're doing is working?

**Colin Lateano:** Now, I'm working right now.

**Colin Lateano:** We just got our GA4 site set up, so I can start adding.

**Colin Lateano:** your bots or whatever it is to the analytics suite.

**Colin Lateano:** I'm sorry that took four months, but what else can we provide in order to actually make sure this is a performance cycle that you're able to get constant feedback on if your strategy is working?

**Jason Gong:** I think, yeah, GA4 and GSC, like GSC, we already have, I think the conversion, because we're publishing content so low in the funnel, like even for existing users, I think, I don't know, like some version of like the Amplitude stuff is still helpful, but I know, I think we have a fairly outdated notion on like what we want to see there, so maybe we can resurface that.

**Jason Gong:** But I think out of those three things, I mean, for most customers, like that's what we get and enough to like, you know, iterate strategy and form a view.

**Colin Lateano:** Okay.

**Colin Lateano:** Okay.

**Colin Lateano:** Yeah, the last part on this topic generation and how to know we're doing the right AEO.

**Colin Lateano:** or SEO plan is we are going through our own campaign waves of solution marketing and how we talk about Webflow.

**Colin Lateano:** Is it, if we include you in how we're positioning ourselves or changes in what we're marketing and pushing out, would that shift the programmatic SEO or do you believe that the answers are the answers and it's a distinct view?

**Colin Lateano:** An example of that is if we're pushing a marketing campaign to talk about hybrid SEO, I mean hybrid CMS instead of headless CMS, does that really change how you would approach programmatic SEO?

**Colin Lateano:** Because the questions that customers are asking are not hybrid or headless.

**Colin Lateano:** Basically, how often should I keep you updated on our internal branding and marketing conversations?

**Jason Gong:** Sorry, don't

**Jason Gong:** Cut you off, Liz, but the stuff that shapes what we do is mostly what people are already searching for and where the intent lives.

**Jason Gong:** So unless that's shifting, I think that that would be like the biggest thing that changes what we work on.

**Jason Gong:** I mean, if you're going to change like how you talk about yourself, that's going to change like how we talk about you and all the articles.

**Jason Gong:** But that's like kind of a smaller shift and more tactical.

**Jason Gong:** Does answer your question?

**Luke Stahl:** I was going to weigh in a little bit just because I think, Colin, some of that goes to like if the content becomes just a glossary or a dictionary and you don't have the tie back to it.

**Luke Stahl:** So it's like if you like that IDE or you're, you know, the AI assistant example that you brought up, if you're just explaining 10 different IDEs out there, which ones are the best and you're not actually using them, then you're just a dictionary.

**Luke Stahl:** If you're at the end, it's like we're building, doing this way or that way, and you can tie that back to your actual company.

**Luke Stahl:** Then you're more opinionated.

**Luke Stahl:** like, yeah, I've used these ones.

**Luke Stahl:** I've used Claude.

**Luke Stahl:** I've used Cursor.

**Luke Stahl:** I've used this.

**Luke Stahl:** And this is my workflow at the end.

**Luke Stahl:** That's more opinionated and then get people, it gets the readers a little bit more like, oh, hey, now we know why Webflow is even saying anything about it in the first place.

**Luke Stahl:** So it's like that idea of like difference from just being a dictionary, glossary, and then more opinionated content.

**Luke Stahl:** Like when you say something about like the best e-commerce stack for Webflow, how do we decide that?

**Luke Stahl:** Like how do you, you know, who is saying it's the best one here and how do you pick and choose which ones go in there?

**Luke Stahl:** That's part of the question.

**Luke Stahl:** The thing about like how to build a database in Webflow, I don't have many objections about that as long as you're actually showing something that works.

**Luke Stahl:** I actually think that that would be okay.

**Luke Stahl:** And that would make sense as long as it's not like a broken workflow by any means.

**Luke Stahl:** But yeah, I just, we did a lot of those like best of type things at Builder.

**Luke Stahl:** if you go check out their blog, but that's coming from the dev advocates who are using those things.

**Luke Stahl:** And then they're always tying it back to their visual IDE now that they claim from Fusion.

**Luke Stahl:** And it's like they plug themselves in and it makes sense, you know?

**Luke Stahl:** So it's like we could touch on a bunch of different AI hot topic keywords, but if it doesn't tie into like our product, then it needs to tie into our opinions as the authors.

**Luke Stahl:** And if there's no author and it's just coming from Webflow Team, then it's just a glossary dictionary type thing.

**Jason Gong:** So that's kind of where my mind sets with this.

**Jason Gong:** Yeah, that makes sense.

**Jason Gong:** I mean, like, I guess we think back to like the early engagement, we like tiered it out as like, you know, glossary dictionary tier.

**Jason Gong:** And then there's like Reddit and there's like Hacker News, you know, and I think maybe we're coming back to that again.

**Jason Gong:** So like the work here for us is to like map that out and tier the kind of opportunities there.

**Jason Gong:** And then I think similar to before, we'll probably like run into it like, cool, this, this, like this, it makes sense to publish this content type.

**Jason Gong:** But maybe, you know, like at Webflow, it's still a little bit challenging to do this without.

**Jason Gong:** inside out.

**Jason Gong:** And

**Jason Gong:** Product marketing involved or DevRel involved, and maybe we punt that.

**Jason Gong:** then to answer your question, Colin, if you're changing kind of broadly how you're describing yourself, I don't think that really changes a ton.

**Jason Gong:** I mean, it's just like, tell us, and then we'll be consistent in how we describe Webflow and all of our content.

**Jason Gong:** It's kind of the only thing that changes.

**Colin Lateano:** I think that's a good chapter end on that.

**Colin Lateano:** We should follow up on strategy and plan for this.

**Colin Lateano:** I agree with approaching re-engaging this top-of-funnel SEO strategy.

**Colin Lateano:** Let's go figure out our topics and how we want to approach that in a separate meeting, if possible.

**Liz Kushnereit:** Yes.

**Liz Kushnereit:** Yes.

**Liz Kushnereit:** Cool.

**Liz Kushnereit:** And just to clarify, this is very like middle of funnel, how to build a database in Webflow, how to build e-commerce site in Webflow, and then, which is a segue into other opportunities we identified.

**Liz Kushnereit:** So the first one is like, if we think of that whole diagram we just talked through, like that other step is also informational.

**Liz Kushnereit:** This is just another opportunity that we can just kind of have a thought experiment with.

**Liz Kushnereit:** But we did do some research on very like basic, what is blank, beginner dev kind of concepts.

**Liz Kushnereit:** And by and large, Webflow doesn't own any of that, or it's not the domain authority on that.

**Liz Kushnereit:** That is where I see, personally, more of what we've accomplished with Augment in terms of like how we frame it.

**Liz Kushnereit:** It's a bit less opinionated than what I'm proposing with programmatic, but it is still an option to capture that side of the story, the informational piece and educational, and we do see an opportunity there.

**Liz Kushnereit:** Not a huge lift.

**Liz Kushnereit:** This could look like not a huge amount of output every week, but this would be like another way to just continue to create that structure.

**Liz Kushnereit:** And then the only other opportunity we identified is taking a look at blog pages.

**Liz Kushnereit:** We just saw that it's had a bit of a dip.

**Liz Kushnereit:** Something that we can offer is refreshes.

**Liz Kushnereit:** think it's just legacy pieces have performed really, really well.

**Liz Kushnereit:** And there's, you know, we haven't done like a full content audit, but it seems like those might not have been refreshed in a while.

**Liz Kushnereit:** And that's something that we can also offer just for that uptake, but just pointing that out.

**Liz Kushnereit:** And yeah, that's about it for my presentation.

**Liz Kushnereit:** So if we have any questions about either of these opportunities, we can talk through, or we can just pivot to getting a little bit of a working session on code components.

**Colin Lateano:** Vivian.

**Colin Lateano:** you have any immediate thoughts about proposals and partnerships on this?

**Vivian Hoang:** No, I think I'm aligned with some of the proposed middle of funnel topics.

**Vivian Hoang:** But I think as far as like the blog and refreshes, I also handle that with our other agency and internal content team.

**Colin Lateano:** Okay.

**Colin Lateano:** Okay.

**Colin Lateano:** Yeah.

**Colin Lateano:** So for now, probably we're going to stick to developer-related topics, which is still a very high interest of Webflow, but okay.

**Colin Lateano:** Yeah.

**Liz Kushnereit:** I can do a little write-up on this with the other strategy pieces, just because the full funnel, this is still very developer-focused and just beginner, dangerous dev, whatever, like teaching them what these very basic topics are and then having a nuanced recommendation of Webflow as a tool, which is really what we're do with Augment right now, And so

**Liz Kushnereit:** So that's just an option I can put into a more detailed write-up, but yeah, but heard on blog.

**Colin Lateano:** I'd love that write-up.

**Colin Lateano:** I'd love to understand that strategy on it.

**Colin Lateano:** And what I would really also have to understand is in our current scope of work, how is all of this achievable in the current work?

**Colin Lateano:** Are we talking about anything being a augment to what our operating plan is so far?

**Colin Lateano:** I know the Kogobones part, let's not talk about that, but the- great question.

**Liz Kushnereit:** This?

**Liz Kushnereit:** No.

**Liz Kushnereit:** This, my proposal here is we just move around our capacity.

**Liz Kushnereit:** And so, like, we're not publishing this huge amount of integration pages.

**Liz Kushnereit:** We're just optimizing.

**Liz Kushnereit:** And then now we're spending more time with our programmatic.

**Liz Kushnereit:** The two at the end are specifically, if we wanted to move into that top of funnel, like being educational for devs, that would be an expansion, yes.

**Colin Lateano:** Right.

**Colin Lateano:** But that is the expansion that we already are talking, we already are working on that contract for, correct?

**Liz Kushnereit:** For code components or, sorry.

**Colin Lateano:** Well, okay.

**Colin Lateano:** So we were using the words three lanes, but we have two active contracts.

**Liz Kushnereit:** Right.

**Colin Lateano:** So is there a new scope enhancement that has to happen in order to accomplish the strategy?

**Liz Kushnereit:** No.

**Liz Kushnereit:** So I just, I did want to sync with you so that I can write in more accurate language into the renewal.

**Liz Kushnereit:** And these, the existing contract is this, these two lanes.

**Colin Lateano:** Okay.

**Liz Kushnereit:** Yeah.

**Liz Kushnereit:** The third.

**Liz Kushnereit:** And then if we were to, the only expansion is that top of funnel, that would be like another add-on if we wanted to.

**Liz Kushnereit:** And code components, we've already in flight with that.

**Liz Kushnereit:** So, yeah.

**Colin Lateano:** Okay.

**Colin Lateano:** Let's, let's, let's grab some time, uh, off this QBR on that then.

**Liz Kushnereit:** Okay.

**Liz Kushnereit:** Cool.

**Liz Kushnereit:** Cool.

**Colin Lateano:** Before jumping into the working session that we have, Webflow side of the house, any questions on the strategy or the go forward proposal for 2027 that's happening in this?

**Colin Lateano:** It has been mostly me talking.

**Colin Lateano:** It's mostly Liz talking, but then me number two.

**Luke Stahl:** I didn't know when or if you want to address it in this one or another call, but the potential idea of like building out a workflow to discover topics based off of more opinionated topics.

**Luke Stahl:** that kind of goes back to that story of like who we follow from DevRel, who could be, you know, following RSS feeds, all this stuff.

**Luke Stahl:** I don't need to bring it to here, but I don't know if you want me to.

**Colin Lateano:** So just you let me know.

**Colin Lateano:** I think figuring out what topics we want to talk about to address the PSEO, I think that's the right time to bring it up.

**Colin Lateano:** And if we're not going to do a working session now on that, I think we can just save that.

**Luke Stahl:** Proposal.

**Luke Stahl:** Cool.

**Luke Stahl:** Fair enough.

**Colin Lateano:** We were working on our own topics of what we would want to try to chase as high-level views and how to have workflows to generate ideas for it, but we're talking just on a strategy today.

**Colin Lateano:** Vic, Ray, any thoughts on operating procedures on this so far?

**Colin Lateano:** Okay.

**Colin Lateano:** Cool.

**Colin Lateano:** I appreciate the presentation.

**Colin Lateano:** Will this be available for me to reference internally as well?

**Liz Kushnereit:** Yeah.

**Liz Kushnereit:** I dropped the link in the channel, but I owe you a longer doc on the strategic direction, so I'll also get that ready for you to be able to share.

**Colin Lateano:** Great.

**Colin Lateano:** Great.

**Colin Lateano:** Appreciate it.

**Liz Kushnereit:** Cool.

**Liz Kushnereit:** Okay.

**Liz Kushnereit:** So I'm going to hand it over to Kirkland if that's okay, but basically just wanted to get some of these open questions since we have like an eight-week sprint.

**Colin Lateano:** I don't want to play too much.

**Liz Kushnereit:** Yeah.

**Liz Kushnereit:** Thank

**Kirkland Gee:** If you can actually leave your screen share up just so I can.

**Liz Kushnereit:** I just put a tiny little component in the bottom right for you about summarizing.

**Kirkland Gee:** Yeah, I know we had a long conversation about this.

**Kirkland Gee:** Basically, the end of the conversation was like, there's a lot more to figure out.

**Kirkland Gee:** And apologies, I'm getting over like a cold.

**Kirkland Gee:** So if I start coughing or you can't understand me, I apologize.

**Kirkland Gee:** Basically, think the biggest thing is component priority order.

**Kirkland Gee:** That, to me, makes sense of just like starting with, I mean, it seems like, in my mind, you guys just correct me if I'm wrong on this.

**Kirkland Gee:** But if, let's say, we're going to do the first hundred as like a test case to make sure this all works, make sure we can do things.

**Kirkland Gee:** Because it's probably like bare minimum, like the, I don't know what words you'd want to use, like, but the primitives, right, of things like buttons and sliders and whatever else.

**Kirkland Gee:** That's pretty easy to just pull from what exists out there.

**Kirkland Gee:** have or something You

**Kirkland Gee:** And then maybe 10 of those 100 or 5 of those 100 or something more complex, something like you talked about that middleware example, or just some kind of like more feature-rich component.

**Kirkland Gee:** Is there any reason to think about priority or sequencing any differently than that?

**Colin Lateano:** Luke, this is a question I want to also put back on you.

**Colin Lateano:** Knowing that AppGen is not as key in strategy, is there any interest in potentially having GrowthX focus on app templates, app examples, over having code components as a installable library that fills a lot of our native component gaps?

**Luke Stahl:** I think there'll be, so regardless of AppGen, there's going to be the push for standalone apps and everything.

**Luke Stahl:** So like from a cloud perspective, what you can build, you know, I mean, obviously you can build a lot of things.

**Luke Stahl:** But having maybe some templates in place for examples there, you know, typical apps that then you launch, that could be a cool thing to have in play.

**Luke Stahl:** Whether it's like these are to-do apps, these are weather apps, these are blah, blah apps, you know, different apps you can spin on up and have it.

**Luke Stahl:** I don't know.

**Luke Stahl:** That could be an idea.

**Colin Lateano:** Okay.

**Colin Lateano:** So I don't disagree with us getting our sea legs on having a bunch of components that fulfill a gap that's not in our current library.

**Colin Lateano:** default.

**Colin Lateano:** Yeah.

**Kirkland Gee:** I think that's just a much easier thing to kind of prove out and get some of the other questions answered first and then have a couple of app examples and like figure out the nuts and bolts and then we can scale that better.

**Kirkland Gee:** That's how I'm thinking about it.

**Colin Lateano:** And that's what I was testing there as well.

**Colin Lateano:** If we have a marketing push to fulfill the standalone apps, maybe we would push harder on that.

**Colin Lateano:** But it sounds like this is still a good way to get going because components is the major gap of getting started.

**Kirkland Gee:** Okay, cool.

**Kirkland Gee:** So the other big question is just around styling.

**Kirkland Gee:** We talked a little bit about how we want to approach that.

**Kirkland Gee:** I don't know if you've come to any kind of big ideas on that because, you know, it seems like there's sort of two approaches of like how opinionated we want to be.

**Kirkland Gee:** And I feel like being more opinionated is in some ways easier and faster, but probably less long-term useful than making them...

**Colin Lateano:** It's less durable to have highly opinionated styles in these components, especially because part of the value add of our code components are that you can then apply your own style sheets to this.

**Colin Lateano:** And so we want your design library to be...

**Colin Lateano:** We want your design system to be applicable to this.

**Colin Lateano:** So the dream to have this be very flexible would be the real value that we could have in this library.

**Kirkland Gee:** And then, so my question on that, how do...

**Kirkland Gee:** I guess this is mostly like a logistics question, but like what's the right way for me to start exploring how to do that like in code, right?

**Kirkland Gee:** Like understanding, okay, how do I write these components to make, is there a good way to test?

**Kirkland Gee:** Like, oh, this is going to plop into five different Webflow websites with very different styling configurations.

**Kirkland Gee:** I know we talked about like having some instructions about, oh, you should set up your styling this way to make it work.

**Kirkland Gee:** Um, I guess what I'm getting is like, I could take forever and figure it out, but I feel like you guys can probably save me a lot of steps on like how some of that's going to work out.

**Colin Lateano:** Well, nothing is default in how this would work.

**Colin Lateano:** So it would be, we would suggest, we would create a, we would create a standard approach saying by default, we're assuming that these, that, that, components would contain styles with a, with different variants.

**Colin Lateano:** We want to have respected and.

**Colin Lateano:** You need to either update those styles or merge it into your already established class library.

**Colin Lateano:** We should not assume anybody using this function is completely new to frontend.

**Colin Lateano:** And that's one part of it.

**Colin Lateano:** So we can come in with an opinion of this is the class and style structure that these are inherently having, but you can change that later on.

**Kirkland Gee:** Right.

**Kirkland Gee:** Here are the things, essentially, like we could give them the knobs to change by default.

**Kirkland Gee:** Would that be the right way to think about it?

**Colin Lateano:** I believe so.

**Colin Lateano:** And Vic and Ray, is that, in your opinion, the right way to go about these imports?

**Vic Plummer:** I think for now, yeah.

**Kirkland Gee:** What I'm imagining is like, okay, let's just use a button as an example.

**Kirkland Gee:** There's a code component that you import as a button.

**Kirkland Gee:** By default, we're going to set it up where you plug in a few variables and you can adjust the corners, the color, the font, the web.

**Kirkland Gee:** Whatever, the size, the padding, like whatever those set of things we decide that people want to adjust are.

**Kirkland Gee:** And we just try to keep as many of those names like consistent across things, you know.

**Vic Plummer:** Have we chatted about like inheritance at all?

**Vic Plummer:** Because there is like there is the ability to inherit styles from Webflow itself and like cross the shadow down barrier.

**Vic Plummer:** And so maybe we have like some instructions on like some general like defaults.

**Vic Plummer:** But if we're inheriting styles, maybe we just use what they have.

**Vic Plummer:** That way it kind of looks more like what their site looks like.

**Vic Plummer:** But I mean, I think Webflow already has kind of like when you go and you like click a button, when you add a button element, there's like a generic style that they use, right?

**Vic Plummer:** That I think we can totally emulate.

**Kirkland Gee:** Yeah, because we're not building buttons.

**Kirkland Gee:** We're building something more complex.

**Vic Plummer:** Yeah, but like if you go into, sorry, there's like, yeah, they're like, they have like a nav bar and stuff like that that's kind of just very general and it's always the same.

**Vic Plummer:** Like when you see it unsound, you know, that's exactly what it is.

**Colin Lateano:** Zach, I didn't know you were on the call.

**Colin Lateano:** When it comes to inheriting, to having co-components get imported with inheritances or should we come in with any preset classes that we could establish across the entire library?

**Zach Plata:** Zach, don't think we need to, like keeping it bare bones is probably easiest while still having examples that show how you can bring in those variables like Vic said from the site into like a variant of a button or whatever more complex component we build.

**Colin Lateano:** Do we need to have any declarations on the import to say that this code is waiting on a variable?

**Colin Lateano:** Pretty much Kirkland's asking, what are the instructions we need to give to make sure this is importable to inherit your styles if we're not going to come in and say these are the styles that are being imported with it?

**Zach Plata:** Yeah, so like some components we've seen are like they expose props as like they have like a string prop for like this is the class name prop that we're going to append to it.

**Zach Plata:** I could see a world where like maybe we expose a button component and there's a prop specifically for like button text that we tell users like, hey, just add in or connect your variable that deals with your text, primary text color on your Webflow site.

**Zach Plata:** And so I think exposing props can be the way that we can support that in a more like a modular way, I guess, for multiple consumers because we can't assume every consumer is going to have their like primary text variables set up the same way.

**Zach Plata:** So it probably makes more sense to just expose the props.

**Zach Plata:** And then just in the instructions of like pulling in the component, be like, hey, set your variables to these certain props if you want to connect your design system.

**Kirkland Gee:** Yeah, so that would mean the experience of this is like they import their code component.

**Kirkland Gee:** It's sitting there.

**Kirkland Gee:** It probably looks like nothing initially.

**Kirkland Gee:** And then they need to what, go rename their classes?

**Kirkland Gee:** Is that how you're imagining that works?

**Kirkland Gee:** Or do you just like, maybe this is me being dumb.

**Kirkland Gee:** I'm still figuring out how some of this stuff works.

**Colin Lateano:** Is it possible that we can probably make a loom of this and follow up with you?

**Colin Lateano:** Because we're talking about jargon that's also very unique to Webflow.

**Kirkland Gee:** Yeah, sure.

**Kirkland Gee:** I think like my, yeah, the takeaway for me is like, if there's any sort of documentation or like help you guys can give me of like, you know, hey, here's how we would probably do it.

**Kirkland Gee:** That would be super helpful.

**Colin Lateano:** Yeah.

**Kirkland Gee:** Um, so I can start sort of exploring and playing around with some different.

**Kirkland Gee:** I don't know.

**Kirkland Gee:** don't know.

**Kirkland Gee:** don't don't don't

**Kirkland Gee:** Approaches, because it's like, you want to be able to scale this to not just one, but like 100 different components and keep a semi-coherent approach to doing this.

**Colin Lateano:** The takeaway to that question for today, because we'll follow up with you on how you'd want to approach it is, no, we should not have an opinion on styles for this.

**Colin Lateano:** And we have a, we have variable representation in our properties that you can then apply your variables to it from your already existing styling and your design system at Webflow onto this.

**Colin Lateano:** But in order to make that work effectively, because we're making interesting and components that are not just very, very strict atomic components, we're going to have to have a explainer, a readme on every single component that says, this component uses these seven variable properties.

**Colin Lateano:** You need to make sure that you are appending them properly in your style when you import this.

**Colin Lateano:** So every component has to come with a readme is what we're getting at.

**Colin Lateano:** And we'll show you how to.

**Colin Lateano:** We'll make a loom to explain and link some dev docs on how we need that to be observed consistently for this creation.

**Kirkland Gee:** Okay, great.

**Kirkland Gee:** That would be perfect.

**Kirkland Gee:** And then, like, if I just go spin up a website on GrowthX's Webflow, just a new site, could I start?

**Kirkland Gee:** Is there anything that I would need to just start testing and playing around with this?

**Colin Lateano:** There's no entitlement limitation, right?

**Kirkland Gee:** All right.

**Colin Lateano:** Well, that's more of question.

**Vic Plummer:** Zach?

**Vic Plummer:** Oh.

**Colin Lateano:** Okay.

**Zach Plata:** But we could probably, because it's the same workspace, I assume, as the main Webflow on Webflow site.

**Colin Lateano:** Well, for testing right now, it wouldn't be Webflow on Webflow.

**Kirkland Gee:** Yeah, I can just use, like, our, just, I mean, we have, you know, an account that links to other clients that have their websites on Webflow.

**Kirkland Gee:** I can just make a starter site or something and just do that for now.

**Zach Plata:** Yeah.

**Kirkland Gee:** Okay, perfect.

**Kirkland Gee:** I think that'll work.

**Kirkland Gee:** And then the only other thing would be, like, it would probably be, like, you.

**Kirkland Gee:** Good.

**Kirkland Gee:** I mean, could, would it, would it make sense to like, what I'm imagining is, yeah, I want to test this.

**Kirkland Gee:** have five or 10 components.

**Kirkland Gee:** actually want to go import them into like five different websites that have very different stylings and like see how they all look and like make sure, just some verification before we go to a hundred.

**Kirkland Gee:** Do you guys have any sort of libraries like that?

**Kirkland Gee:** Or is it just like, should I just spin up a few from free templates and like use that?

**Zach Plata:** Like, do you have any recommendations?

**Zach Plata:** Typically when I do testing, I just use different templates.

**Zach Plata:** that's the free ones.

**Zach Plata:** But yeah, if there's like others in particular you're seeing that are like maybe paid or something, we could see if we can get something set up.

**Zach Plata:** Uh, I mean, it's like a test.

**Kirkland Gee:** I don't, yeah, I don't think it's that important.

**Kirkland Gee:** I just, you know, I don't want to assume that because in my explicit test site where I set everything up, that it works correctly, that it's just as simple of an experience in a different environment.

**Zach Plata:** Yeah, it'll be probably wildly different depending on like how people set up their design system.

**Kirkland Gee:** So I think

**Kirkland Gee:** Whatever works in the templates is probably fine.

**Kirkland Gee:** I've used enough community Webflow templates over the years to know that people do very different things with their...

**Zach Plata:** I remember one template, the H1 on the website, like each word was its own span, but not even just a span, its own H1 element.

**Zach Plata:** Like every word was a separate H1 in the heading, and I just wanted to die.

**Zach Plata:** Oh no.

**Zach Plata:** This is a long time Sounds like a semantic nightmare.

**Kirkland Gee:** But yeah, okay, I think that's all super clear to me.

**Kirkland Gee:** So once I get kind of some clear documentation from you guys, I can get started on exploring some of this.

**Kirkland Gee:** And the only other thing would be like, if there are, Colin, like any components that you just know, you're like, this is a gap, we get asked about this, like we should do this first.

**Kirkland Gee:** If there is any list or anything, send it.

**Kirkland Gee:** If not, I'll try to be my best educated guess on where to start.

**Colin Lateano:** I will, I will explore and see if there's any.

**Colin Lateano:** The that we know is obvious and clear, there's a few members at Webflow who are still active on their own agency world, so I'll ask them and just get a poll, but as far as I'm aware right now, there's not like a very clear list of needs.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** Okay, cool.

**Colin Lateano:** Are you in the shared GrowthX channel?

**Colin Lateano:** we message in there?

**Kirkland Gee:** Okay.

**Kirkland Gee:** Yes.

**Kirkland Gee:** You can tag me in there.

**Kirkland Gee:** Okay.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** My working theory, though, is like, if we get five of them right, I can do 500, right?

**Kirkland Gee:** Like, in theory, if we can just get a system that works, the idea is it shouldn't be that hard to scale to a lot more of them, so I'm not, like, incredibly concerned about getting the exact perfect place to start, but if we have clear direction, I can take it.

**Zach Plata:** Yeah.

**Zach Plata:** A question for a Webflow team, like, as they're building out these code components, we have our whatever repo, code component examples repo on GitHub.

**Zach Plata:** Webflow examples, do we want them to add to that or do we think it's worth it just having a new standalone repo of like multiple component examples?

**Zach Plata:** This would be for like open source just viewing.

**Colin Lateano:** I think it's worth being viewable, of course.

**Colin Lateano:** I think having the Git available so that you can do your own imports and also if we're making any contribution to the web in general.

**Colin Lateano:** And these components are, I mean, effectively, they're just available to be imported.

**Colin Lateano:** Anyone can use off of Webflow too, which is, we have a very opinionated view of how to import.

**Colin Lateano:** I think having it be in the examples is absolutely fine as long as we can make sure that these are the ones that are referenceable.

**Colin Lateano:** Well, no, these are all going to be our own trusted components, aren't they?

**Colin Lateano:** Yeah, they just live in the same shared repo.

**Raymond Camden:** I just vote for having like a common naming scheme.

**Raymond Camden:** versus a random API demo.

**Raymond Camden:** Does that make sense?

**Zach Plata:** Yeah.

**Zach Plata:** Kirkland, I'll throw this in the channel, too.

**Zach Plata:** You might have already seen it.

**Zach Plata:** We started one with a few different code component examples.

**Zach Plata:** One goes into ShadCN components before we realized ShadCN just has a few nuances that don't play well.

**Zach Plata:** And so I figured if you want, you can probably just start adding to these.

**Zach Plata:** Well, maybe to unblock, you could continue if you're already working in a repo, just having that tailored and we can figure out how to merge after the fact into this one that I sent in.

**Kirkland Gee:** Yeah, well, no, mean, because I haven't started writing code for any of this yet, right?

**Kirkland Gee:** Just kind of trying to make sure I'm clear on what we, some of these things.

**Kirkland Gee:** So, yeah, I think I can, yeah, this is super helpful.

**Kirkland Gee:** And I can look at, like, how some of these are set up and try to mimic.

**Kirkland Gee:** do Say

**Kirkland Gee:** You know, try to make them look as well put together as this is.

**Kirkland Gee:** Yeah, that makes sense.

**Kirkland Gee:** Yeah, very cool.

**Kirkland Gee:** Okay.

**Kirkland Gee:** Yeah, so there's no reason, I mean, this is all open source, there's no reason I couldn't just clone this and start working right out of there, right?

**Zach Plata:** No.

**Zach Plata:** And we can probably just add you to the list.

**Colin Lateano:** The only thing is that in the examples, I'd rather not, until we're, I'd rather not have that be a testing ground.

**Kirkland Gee:** Yeah, yeah, I can like fork off a, like a copy of it for the time being.

**Kirkland Gee:** And then once we're happy, right, I can merge anything that I've done in that fork into the primary repo.

**Kirkland Gee:** But yeah, no, same, I'm not going to start like throwing new stuff into a public repository, hoping it works.

**Colin Lateano:** Yeah, okay, great.

**Colin Lateano:** Worth saying, just, but yeah.

**Kirkland Gee:** 100%.

**Kirkland Gee:** Okay, Liz, Jason, I feel really good about at least starting to make some progress on this.

**Liz Kushnereit:** Then I think that's it.

**Liz Kushnereit:** Unless anyone has anything else, but thanks for everyone's time.

**Liz Kushnereit:** I'll post some follow-up, and then I think Kirkland and I have some pretty clear to-dos.

**Kirkland Gee:** Yep, sounds great.

**Colin Lateano:** Thank you, everyone, on GrowthX side.

**Colin Lateano:** I'm looking forward to the presentation, to review that, and we'll, Liz, let's catch up very soon on scoping and coverage, and then let's kick off a topic meeting probably after RKO, which is next week, so sometime later, Feb.

**Liz Kushnereit:** Okay, sounds good.

**Colin Lateano:** Great.

**Colin Lateano:** Thanks, everyone.

**Vic Plummer:** Bye.

**Vic Plummer:** Bye.

**Vic Plummer:** Bye.
