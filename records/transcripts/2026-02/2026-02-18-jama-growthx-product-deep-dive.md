# Jama <> GrowthX - Product Deep-Dive

<metadata>
date: 2026-02-18
time: 15:00 UTC
duration: 59 minutes
organizer: aida@growthxlabs.com
participants: Mario Maldari, Aida Knežević
fathom_recording_id: 123324974
fathom_url: https://fathom.video/calls/570075961
share_url: https://fathom.video/share/vKJARE9dSmCywrmsSyUwC5i-3XwmxyAB
source: fathom
enriched_on: 2026-03-01 00:00 UTC
speaker_note: Only Mario Maldari (Jama Software) and Aida Knežević (GrowthX) participated. Other names in metadata were calendar invitees but did not attend.
</metadata>

---

## Summary

Mario Maldari (Jama Software) gave GrowthX a comprehensive product deep-dive on Jama Connect, covering the platform's core value (live traceability connecting requirements, design, implementation, verification, and testing), three-pillar product structure (core Connect tool, Advisor AI add-on, and Interchange integrations), and key differentiators including built-in test management, free stakeholder licenses, and industry-expert-led Customer Success. GrowthX will use this knowledge to develop content artifacts and generate positioning materials for Jama's B2B campaigns.

---

## Context

Jama Software is a B2B SaaS leader in requirements management and live traceability for complex product development industries (aerospace & defense, medical devices, automotive). Mario Maldari, a product leader with 20 years in requirements management, led this structured product briefing to help GrowthX understand Jama's positioning, features, and messaging before content creation. The session was part of a broader engagement where GrowthX will develop content artifacts and marketing materials to support Jama's go-to-market strategy, with recurring syncs scheduled to align on deliverables and gather additional product context.

---

## Relevance

**To GrowthX Delivery:**
- Jama's product messaging centers on "live traceability" (preventing costly late-cycle rework), industry-specific solutions (Medical, A&D), and a three-pillar architecture (Connect + Advisor AI + Interchange integrations) — key themes for content creation
- Customer Success is a differentiator: Jama provides dedicated, industry-expert consultants vs. competitors who charge separately — valuable positioning angle for campaigns
- Security/compliance positioning varies by customer segment: SOC 2 for standard cloud, Customer Validated Cloud (CVC) for medical, GovCloud for A&D, on-premise for fully disconnected — need segment-specific messaging
- G2 leadership ranking is a third-party validation lever that should feature prominently in early-stage content

**To CheckThat:**
- Jama's Advisor AI add-on (requirement quality scoring, AI test case generation) represents AEO/AI visibility opportunity — potential case study or product comparison
- Requirements management industry is mature with established competitors (IBM, competitors mentioned); Jama differentiates on AI, integrations, and Customer Success

**To GrowthX Business Development:**
- Jama appears committed to this engagement: Mario is product leader (not sales), multiple stakeholders invited, materials shared, and recurring syncs already scheduled
- Medical and A&D are high-value, compliance-heavy verticals with repeatable engagement models and expansion potential
- Jama's high-touch Customer Success model suggests strong account growth potential — GrowthX could develop thought leadership content around this

---

## Overview

- **Core Value:** Jama Connect is the "single source of truth" for complex product development, using "live traceability" to connect requirements to models (Cameo), defects (Jira), and tests, preventing costly late-cycle rework.
- **Product Structure:** The platform has three pillars: the core `Jama Connect` tool, the `Advisor` AI add-on (for requirement quality scoring and test generation), and the `Interchange` add-on (for integrations).
- **Key Differentiators:** Built-in test management (vs. competitors' separate tools), free stakeholder licenses for external review, and a high-touch Customer Success program with industry experts.
- **Positioning:** Marketing focuses on two angles: new features (e.g., AI) and pre-built, industry-specific "solutions" (e.g., Medical, A\&D) that accelerate compliance.

---

## Key Topics

### The Problem: Siloed Engineering & Costly Rework

  - **Challenge:** Complex product development (e.g., self-driving cars) creates silos between hardware, software, and test teams.
  - **Result:** This leads to costly late-cycle rework and recalls.
      - 60–70% of defects are found late in the cycle.
      - Fixing a defect in the field is hundreds of times more expensive than fixing it during requirements gathering.
  - **Solution:** Jama Connect provides a centralized platform for requirements management, connecting all development artifacts to ensure consistency and prevent errors.

### The Solution: Live Traceability & the V-Model

  - **Core Concept:** "Live traceability" is Jama's trademarked term for connecting requirements to all related artifacts across the development lifecycle.
  - **V-Model:** This industry-standard model illustrates the cost of defects over time.
      - **Left Side:** Requirements → Design → Implementation
      - **Right Side:** Verification → Validation → Operations
      - **Principle:** Finding and fixing issues earlier on the left side is far cheaper than later on the right.
  - **Suspect Triggers:** A critical feature that automatically flags downstream items (e.g., tests) as "suspect" when an upstream requirement changes, forcing a review and preventing out-of-sync work.

### Product Structure & Features

  - The platform has three pillars:
    1.  **`Jama Connect` (Core Product):**
          - **Traceability Information Model (TIM):** A visual map defining artifact relationships.
              - **Solid Lines:** Enforced relationships (e.g., every Stakeholder Need *must* have a System Requirement).
              - **Dotted Lines:** Optional relationships.
          - **Built-in Test Management:** A key differentiator, as competitors (e.g., IBM) require separate, licensed test tools.
          - **Impact Analysis:** A tool to visualize the full downstream impact of a proposed change before it's made.
          - **Review Center:** Manages formal requirement reviews and approvals.
              - **Free Stakeholder Licenses:** Allows external partners (e.g., clients) to participate in reviews without purchasing a full license, a major selling point.
          - **Live Traceability Explorer (LTE):** A high-level dashboard for senior management to track project progress and KPIs like traceability score.
    2.  **`Jama Connect Advisor` (AI Add-on):**
          - **Requirement Quality Scoring:** Analyzes requirement text against industry standards (INCOSI, EARS) to provide a quality score and suggest refinements.
          - **AI Test Case Generation:** Generates 10 test cases with steps from a requirement in seconds, saving significant manual effort.
    3.  **`Jama Connect Interchange` (Integration Add-on):**
          - **Integrations:** Connects to tools like Jira, Cameo, Simulink, and Excel.
          - **Excel Round-trip:** Allows complex calculations (e.g., risk analysis) to be performed in Excel and written back to Jama Connect.
          - **Open API:** Provides extensibility for custom integrations.

### Positioning & Differentiators

  - **Customer Success Program:** A key differentiator. Jama provides dedicated, industry-expert consultants to ensure successful implementation, unlike competitors who often charge for post-sale services.
  - **Security & Hosting:**
      - **SOC 2 Compliance:** Product and AWS hosting environment are SOC 2 certified, a critical requirement for IT teams.
      - **Hosting Options:**
          - **Standard Cloud:** For \~80% of customers.
          - **Customer Validated Cloud (CVC):** Isolated environment for medical customers to perform their own validation.
          - **GovCloud:** For A\&D customers with strict data residency and compliance needs (e.g., ITAR).
          - **On-Premise:** Available for customers requiring a fully disconnected environment.
  - **G2 Leadership:** Consistently ranked as a leader on G2, a powerful third-party validation tool for prospects.

---

## Action Items

**Mario Maldari (Jama Software)**
- Send brand/trademark rules to Aida; she'll update proofreader checklist
- Upload today's deck to shared folder for Aida

**Aida Knežević (GrowthX)**
- Check access to yesterday's docs; if blocked, notify Mario
- Send Slack follow-up to Mario re: today's call
- Schedule recurring sync with Mario

---

## Transcript
**Mario Maldari:** I'm good, how are you?

**Mario Maldari:** This meeting is being recorded.

**Aida Knežević:** Where are you based?

**Aida Knežević:** You're not in California, right?

**Mario Maldari:** No, I'm in Colorado.

**Aida Knežević:** Okay, okay.

**Mario Maldari:** Yeah, how about you?

**Aida Knežević:** I'm based in Europe, so I'm based in Sarajevo.

**Aida Knežević:** Oh, So I'm trying to create a map.

**Aida Knežević:** Do you have any people who are going to be working with us who are on the West Coast?

**Mario Maldari:** Yes, Deco, who will probably be our copywriter, she is in Portland, Oregon, so she is on the West Coast, yeah.

**Mario Maldari:** But there's probably not as much of a need for, like, direct interaction, you know, and overlap as we would need to, like, pass tasks back and forth.

**Aida Knežević:** Okay.

**Mario Maldari:** So, thankfully, for me, it's, this is a good time.

**Mario Maldari:** It's 8 a.m.

**Mario Maldari:** for me, so not, you know, not super early.

**Mario Maldari:** Hopefully not super late for you.

**Aida Knežević:** What time is it for you?

**Aida Knežević:** No, no, it's 4 p.m.

**Aida Knežević:** This is actually quite, this is one of my earlier calls.

**Mario Maldari:** Oh, really?

**Aida Knežević:** But we'll see.

**Aida Knežević:** We'll see what she says.

**Mario Maldari:** Yeah.

**Mario Maldari:** And I'm totally flexible too.

**Mario Maldari:** I've been up since 5.30.

**Mario Maldari:** So I went for a run this morning and I'm up early.

**Aida Knežević:** Oh, Nice.

**Mario Maldari:** Yeah.

**Mario Maldari:** I prefer it anyway.

**Mario Maldari:** I'm like, yeah, more of a morning person.

**Mario Maldari:** By like three o'clock, I'm like, oh my God, I'm starting to burn out.

**Aida Knežević:** Yeah.

**Aida Knežević:** Yeah.

**Aida Knežević:** Yeah.

**Aida Knežević:** Yeah.

**Aida Knežević:** I feel you.

**Aida Knežević:** I feel you.

**Mario Maldari:** All right.

**Mario Maldari:** Is it just going to be you today?

**Mario Maldari:** I think so.

**Mario Maldari:** Yeah.

**Mario Maldari:** I think we don't want to board funny with too many low level details, but yeah, I figured I'd go through some high level context, you know, in terms of like how we typically position the product itself, you know, go through some of the pain points that we try to address, almost like a typical pre-sales discussion with our prospects.

**Mario Maldari:** And then, then I'll show you the, the product a little bit.

**Aida Knežević:** I'll try to keep it sort of high level as not to get too deep into the weeds.

**Aida Knežević:** Okay.

**Mario Maldari:** But that, yeah, that was my idea for today, unless you had any other.

**Aida Knežević:** Yeah, think that's helpful just so we understand how the product works, what are the different nuances, any standout features that we should really focus on or be aware of, especially when it comes to things that some of your competitors might not be offering.

**Aida Knežević:** But yeah, that all sounds good.

**Mario Maldari:** Okay, perfect.

**Mario Maldari:** All right, well, let me go and share my screen here.

**Mario Maldari:** Did you want to record this or is it already recording?

**Aida Knežević:** It's recording.

**Aida Knežević:** We have a note taker in here.

**Mario Maldari:** Okay, perfect.

**Mario Maldari:** All right, let me know if you can see my screen okay?

**Aida Knežević:** Yes.

**Mario Maldari:** All right, perfect.

**Mario Maldari:** Well, I'll take you through some of these slides.

**Mario Maldari:** I'm not going to go through all of them, but I want to just give you a little bit of context.

**Mario Maldari:** And this is actually a presentation I give to our like analysts like Gartner and those folks in terms of, you know, how we are positioning ourselves and what the new features and functionality that we are offering.

**Mario Maldari:** And so I've been in this space for about 20 years, amazingly.

**Mario Maldari:** It's hard to imagine.

**Aida Knežević:** It's like I got a job out of college working on requirement software, and then here I am.

**Mario Maldari:** But really, this slide kind of shows what the evolution has been with product development.

**Mario Maldari:** So things are just getting more complex as we go.

**Mario Maldari:** There's more hardware involved, more software involved.

**Mario Maldari:** If you look at cars, for example, the evolution of the self-driving car, that's a perfect example.

**Mario Maldari:** You open the hood to your car.

**Mario Maldari:** used to be you could fix things on your own, but now there's computer chips and everything like that.

**Mario Maldari:** So just a lot more complexity built across the board.

**Mario Maldari:** And so really the problem that we have from trying to build these things is how do you keep track of it all?

**Mario Maldari:** Like you have hardware folks doing their thing, software folks doing their thing.

**Mario Maldari:** You know, everyone's in a silo, but there's dependencies between those teams that, you know, they need to.

**Mario Maldari:** To talk, communicate.

**Mario Maldari:** And that doesn't happen often.

**Mario Maldari:** And even when people attempt to do it with Excel and Word, like we mentioned yesterday, it falls apart at scale very quickly.

**Mario Maldari:** And so that's, you know, that's the biggest thing that we encounter across all of our prospects is siloed engineering teams.

**Mario Maldari:** And this is just a perennial problem.

**Mario Maldari:** Some get close to solving it.

**Mario Maldari:** You know, some, I realize it's a problem, but it's too expensive or too hard to do.

**Mario Maldari:** And, you know, and it falls apart very quickly.

**Mario Maldari:** And so in systems engineering, and this is a good concept for you guys to be well-versed in, is we have what's called the V model.

**Mario Maldari:** And this is kind of a, not my favorite graphic, to be honest with you, but it's, it is a V model.

**Mario Maldari:** And so, you know, at the top left of the V model from a systems engineering perspective is requirements management.

**Mario Maldari:** So, you're collecting requirements from the customers and.

**Mario Maldari:** So really what's the problem is there's no single source of truth, there's no one application where you can see it all, it's all over the place, and what it results in, we talked about this yesterday, you asked some really great questions yesterday, by the way, and you asked kind of what the result of, you know, not doing something, you know, is basically, and so we have these metrics that we've defined across the board and some good examples, you know, in terms of, you know, stuff that everyone's familiar with, know, Blue Origin, having failures, know, Wall Street Journal, you know, having problems, GM recalling cars, mean, the recalls, at least in the US, happens all the time.

**Mario Maldari:** And, you know, some of these things, you know, these are industry standards, you know, late detection of defects, you know, resulting in 60, 70% of, you know, problems that we have, a slower time to market, because you're finding issues late in the cycle.

**Mario Maldari:** So the recall, recall, recall,

**Mario Maldari:** They're probably the worst thing that can happen to your reputation and to your expense, right?

**Mario Maldari:** And so, you know, just these are real things.

**Mario Maldari:** I mean, I see this happen all the time.

**Mario Maldari:** And you could actually really trace it back to a lack of requirements management.

**Aida Knežević:** Yeah.

**Mario Maldari:** It's scary to think about, but, you know, like building planes, for example, you know, we hear all these problems with aircraft.

**Mario Maldari:** And it's like, geez, I hope they had requirements management software, you know, but it's true.

**Mario Maldari:** And so this really resonates well when we show prospects.

**Mario Maldari:** So it's kind of like the V model.

**Mario Maldari:** And we always say that the earlier in the V model you find your problems with your requirements, the less costly it is.

**Mario Maldari:** But the further along the V model, for example, if you're finding defects when you start testing, if your requirements are poorly written to begin with, and then you start finding problems with them, it gets more expensive as you go.

**Mario Maldari:** And once you release to the field your product, it just gets, you know, hundreds.

**Mario Maldari:** It's more expensive to fix the product.

**Mario Maldari:** So that's really, this always resonates with higher, you know, engineering managers.

**Mario Maldari:** Because at the end of the day, they're like, blah, blah, blah, blah, you know, what are you talking about in terms of cost?

**Mario Maldari:** What is this cost?

**Aida Knežević:** What's going to, how is this going to affect my bottom line?

**Mario Maldari:** And this chart does resonate with them.

**Mario Maldari:** So, you know, so we say, well, what's the solution?

**Mario Maldari:** And obviously, connecting everything, you know, together, taking that V model, and, you know, allowing traceability to occur between all of these components.

**Mario Maldari:** And so one of the biggest messages that we had when I joined the company four years ago was this concept of live traceability.

**Mario Maldari:** And you'll see that we've trademarked it.

**Mario Maldari:** And this is a unique industry term that we've defined.

**Mario Maldari:** And what it really means is that the messaging is that, hey, we understand that, you know,

**Mario Maldari:** You're going to be using tools like Simulink for your simulation.

**Mario Maldari:** You're going to be using tools like Cameo, Dassault Cameo for your modeling, Jira for defect management, things like that.

**Mario Maldari:** We understand that, but what we want to do is we want to integrate into those tools.

**Mario Maldari:** We want JAMA Connect to be the single source of truth, and we want to integrate into those tools and bring all of that information into a centralized source so that you can see, did your model change?

**Mario Maldari:** Oh, okay, your model change in Cameo, that's going to affect your downstream requirement, and you can see that within JAMA Connect.

**Mario Maldari:** So that's the concept of live traceability.

**Mario Maldari:** We say we're not trying to be those other products.

**Mario Maldari:** We can't.

**Mario Maldari:** We don't play in that space.

**Mario Maldari:** We do one thing, and we do it well, and it's requirements management.

**Mario Maldari:** But we want to see all of that work that's going on within one tool.

**Mario Maldari:** So that's really our live traceability message.

**Mario Maldari:** And if you search for it online on our blogs, you'll see tons of stuff.

**Mario Maldari:** Like our CEO, this was his vision.

**Mario Maldari:** So you'll ask, okay, what is JAMA Connect?

**Mario Maldari:** Like, what is it at the highest level?

**Mario Maldari:** What does it consist of?

**Mario Maldari:** And so last year we put together this, like, product stack that kind of represents, you know, really what the tool is.

**Mario Maldari:** And so we have this intelligence layer and AI.

**Mario Maldari:** And this is, really the big focus.

**Mario Maldari:** It's, like, sort of what we started talking about yesterday.

**Mario Maldari:** Like, what are the things that we're delivering in the next six months to a year?

**Mario Maldari:** And a lot of it is AI-focused.

**Mario Maldari:** And so we have this, and I'll show you some of this.

**Mario Maldari:** We have requirement quality scoring and multi-statement analysis.

**Mario Maldari:** And so, you know, when I was mentioning before, like, you're writing a requirement and you want to test a requirement.

**Mario Maldari:** If the requirement is no good to begin with, like, if it's ambiguous or poorly written, then certainly when.

**Mario Maldari:** You go to test it, your test is going to not be accurate as well.

**Mario Maldari:** So we use artificial intelligence to basically scan a requirement, look at the text of the requirement.

**Mario Maldari:** And then there's these standards, one's called INCOSI, which is the International Systems Engineering Standard.

**Mario Maldari:** So that's a big one for you to be familiar with, is INCOSI.

**Mario Maldari:** And then EARS, E-A-R-S, is another one.

**Mario Maldari:** And these are both like best practices for writing requirements, you know, related to systems engineering best practices, things like that.

**Mario Maldari:** And so what it'll do behind the scenes is like parse all of the content of the requirement, compare it to these rules that we have for INCOSI and EARS, and then return you a score.

**Mario Maldari:** And it could say, hey, Mario, your requirement is like 50%.

**Mario Maldari:** It's like really poorly written.

**Mario Maldari:** And you don't follow this rule.

**Mario Maldari:** You're not following that rule.

**Mario Maldari:** rule.

**Mario Maldari:** And you're that you've made you think going the

**Mario Maldari:** You know, I can help you.

**Mario Maldari:** Do you want to refine it?

**Mario Maldari:** And so I hit the refine button and it produces a version of the requirement that's rewritten and of a higher quality standard.

**Mario Maldari:** So that's like the first thing because garbage, there's the old adage, garbage in, garbage out, right?

**Mario Maldari:** And so this is to kind of prevent that from happening.

**Mario Maldari:** So that's one AI capability.

**Mario Maldari:** The other one that we're just released, I think last week, is test case generation.

**Mario Maldari:** And so, like, if you're working with a requirement and you're like, hey, I want to build a bunch of tests around this requirement, you can just click a button and it'll generate 10 test cases for you to review and say, okay, these look great.

**Mario Maldari:** And you can accept them.

**Mario Maldari:** It'll automatically link them to the requirement.

**Mario Maldari:** You can say, hey, you know, some of them are good.

**Mario Maldari:** I want to regenerate a bunch of test cases, you know, and you can click the button, regenerates a bunch of test cases.

**Mario Maldari:** So that's huge, right?

**Mario Maldari:** Because previously, and I did this for a job a long time ago.

**Mario Maldari:** If I had to write test cases manually, someone would send me 10 requirements, hey, figure out how to test this thing, write requirements.

**Mario Maldari:** So you'd manually write the requirements, get them reviewed, go through this really laborious, time-consuming process, and this just reduces it to seconds.

**Mario Maldari:** So it's huge.

**Mario Maldari:** And I think we're a little bit ahead of our competitions.

**Mario Maldari:** We're all fighting for the same thing.

**Mario Maldari:** Like, there's these common problems that we're all trying to solve, but, you know, this was a big win for us, so we're trying to get ahead of them with stuff like that.

**Mario Maldari:** So then at the middle layer, we have our kind of core features.

**Mario Maldari:** So you'll hear a lot about the traceability information model.

**Mario Maldari:** We call it the TIM.

**Mario Maldari:** It's abbreviated to TIM.

**Mario Maldari:** And that basically is a working model that governs your project.

**Mario Maldari:** It's like how the requirements relate to each other.

**Mario Maldari:** And I'll show you that in the actual tool.

**Mario Maldari:** And then, of course, requirements.

**Mario Maldari:** Management is the core functionality.

**Mario Maldari:** We have a review and approval center built in.

**Mario Maldari:** And so a lot of times what we see companies doing is they may have a tool like doors, like IBM doors, and they're managing their requirements in it, you know, great.

**Mario Maldari:** But then they go to review them and the engineering team is like, hey, like this tool is so hard to use.

**Mario Maldari:** I'm just going to email you an Excel export.

**Mario Maldari:** Can you review that and send it back to me?

**Mario Maldari:** And then you lose all the history, the audit trail.

**Mario Maldari:** As soon as you go outside the tool, it becomes worthless because then you lose everything.

**Mario Maldari:** And then five years from now, the FDA is like, hey, can you show me your audit trail for how you built this medical device?

**Mario Maldari:** And you don't have it, right?

**Mario Maldari:** And so keeping everything easy to use within the tool, that's kind of one of our mantras.

**Mario Maldari:** Like, you know, we'll make it easy for you so you don't leave, but please stay in the tool, keep everything in the tool.

**Mario Maldari:** You're developing, but the key is you're not rewriting that requirement every time.

**Mario Maldari:** You can easily reuse it across 100 projects, so it saves a lot of time.

**Mario Maldari:** And then test management, this is something we offer within the tool itself.

**Mario Maldari:** This is a differentiator for us, too, because tools like IBM's offering, they sell and license a separate test tool that you have to buy and then integrate into your requirements management.

**Mario Maldari:** So the fact that we have it built in with the same user interface, same workflow, it's pretty big for us.

**Mario Maldari:** That's kind of a differentiator.

**Mario Maldari:** And we're continuously working on test management, like adding features and functionality, because we are playing kind of a catch-up game with a code beamer, PTC code beamer.

**Mario Maldari:** We've lost some deals to them based on things that we don't have in our test center.

**Mario Maldari:** So we're really trying to keep.

**Mario Maldari:** Keep maintaining that and staying up with the competition on test management.

**Mario Maldari:** And then I mentioned to you about the integrations being so important to us.

**Mario Maldari:** Like if you can't integrate into an ecosystem, like if we go to talk to the U.S.

**Mario Maldari:** Air Force, which we are, you know, like this week, and they say, we have all these, you know, other tools that we're using.

**Mario Maldari:** Like how can we, you know, get you in there?

**Mario Maldari:** We like you, but how do you fit within our ecosystem?

**Mario Maldari:** And the IT guys are like, no, no, we don't want another tool.

**Mario Maldari:** So it's like the easier we fit in an ecosystem, the better.

**Mario Maldari:** And that's why we focus on integrations.

**Mario Maldari:** And then we have this concept.

**Mario Maldari:** This is big for you.

**Mario Maldari:** So there's really three pillars, right, of product for Java.

**Mario Maldari:** There is Java Connect, which is the main requirements, you know, tool, like basically everything in this workflow layer.

**Mario Maldari:** And then there's Java Connect Advisor, and that's all the AI.

**Mario Maldari:** So, you know, anything about natural language processing, you know, the test case generation, all of that is falling under the umbrella of JAMA Connect Advisor.

**Mario Maldari:** And then there's JAMA Connect Interchange, and that's where a lot of our integrations happen.

**Mario Maldari:** So these two, Advisor and Interchange, they're considered add-ons to the core product, and they are sold at an additional cost, right?

**Mario Maldari:** So definitely something for you to be aware of, and especially when we refer to them, we refer to them as add-ons, and that's, like, specific language.

**Mario Maldari:** And so, like, Interchange offers a Jira integration, an integration to Excel, where you can do, like, complex Excel functions.

**Mario Maldari:** You can, like, basically write things from JAMA Connect into Excel, can do some complex calculation on them, and then write that value back into JAMA Connect.

**Mario Maldari:** So this is big for, like, a lot of companies have complex risk management calculations.

**Mario Maldari:** And so this is very appealing to them to be able to keep their stuff, their formulas in Excel, but get the values back into JAMA Connect.

**Mario Maldari:** So, yeah, all of this is very important.

**Mario Maldari:** And API, if you are a software these days that does not have an open API, you are at a major disadvantage.

**Mario Maldari:** So the API basically, you know, when we talk to prospects and they're like, hey, do you have a pre-built integration to XYZ?

**Mario Maldari:** And we may not.

**Mario Maldari:** And we say, yes, but we have, you know, a fully open API and you can write that very easily yourself or with our help through the API.

**Mario Maldari:** It's like an extensibility, you know, platform.

**Mario Maldari:** And so a lot of customers will do that and utilize the API for that purpose.

**Mario Maldari:** So this is kind of like a all-in-one slide, you know, that kind of represents.

**Mario Maldari:** Everything at a very high level.

**Mario Maldari:** So any questions with this, Aida?

**Aida Knežević:** Is there anything, so for the AI capabilities, everything that you covered, those things are already available?

**Mario Maldari:** Yes, everything I mentioned, those things are available.

**Mario Maldari:** And then some that are kind of like sort of beta-ish that I'll call out as well when I start to show you the product.

**Mario Maldari:** All right, so this is kind of our old version of this chart, a little bit more simplistic, but basically saying the same thing in terms of, you know, what is JAMA Connect?

**Mario Maldari:** And then here, this kind of reinforces what I was just mentioning.

**Mario Maldari:** There's the core product, and then there's JAMA Connect Interchange and JAMA Connect Advisor.

**Mario Maldari:** And everything here is, these are trademarked.

**Mario Maldari:** This is a registered copyright.

**Mario Maldari:** Right, and I just, I say that because I'm, I'm the brand police now.

**Mario Maldari:** Right, so like whenever like, you know, someone's writing something.

**Mario Maldari:** Don't forget the registered trademark.

**Mario Maldari:** And we do have like brand rules that will communicate to you guys.

**Mario Maldari:** Like on first mention of JAMA Connect in a piece, we'll always do the registered trademark.

**Mario Maldari:** And then subsequent mentions, you know, we don't.

**Mario Maldari:** So we'll provide that stuff.

**Aida Knežević:** Okay, perfect.

**Aida Knežević:** Yeah, we have a proofreader checklist that is part of the workflow so we can incorporate that information there.

**Mario Maldari:** Okay, yeah, that's perfect.

**Mario Maldari:** Yeah, great.

**Mario Maldari:** And it's not too complex, I think, that once you get the rules, they're pretty easy.

**Mario Maldari:** Okay, so yeah, going through here, not too much.

**Mario Maldari:** There is this feature that we released a couple years ago that is kind of a big deal.

**Mario Maldari:** It's called the Live Traceability Explorer, or LTE.

**Mario Maldari:** And what it allows you to do, this is when we're trying to elevate our message to senior management.

**Mario Maldari:** And what it is, it's like a dashboard, basically.

**Mario Maldari:** Very, very high-level view of the data inside your requirements project.

**Mario Maldari:** Okay,

**Mario Maldari:** And it shows you basically coverage gaps, it shows you test gaps, it's a very high-level view, and it's meant to appeal to, you know, senior engineering managers who are like, I don't care about the details, just tell me how far along I am with the project, and, you know, am I on track or not?

**Mario Maldari:** And you'll see as I zoom in here that, you know, basically this gives you like a traceability score.

**Mario Maldari:** And so, you know, so this allows you really to see measurable improvement over time, which is always a big deal for, you know, senior management.

**Mario Maldari:** They want to say, you know, how are we doing?

**Mario Maldari:** You said that we were at 30% when we started this project.

**Mario Maldari:** I want to end this project at at least 90% as a KPI.

**Mario Maldari:** How are we doing towards that?

**Mario Maldari:** So this was appealing to them.

**Mario Maldari:** So, yeah, so this will continue to be something that we probably write content on, you know, and encourage with the field.

**Mario Maldari:** We'll start talking.

**Mario Maldari:** I'll show you this actually in the tool itself.

**Mario Maldari:** This is an example of a traceability information model.

**Mario Maldari:** And so what it really is, is a way of governing your traceability within your project.

**Mario Maldari:** And so it's different for every company in terms of their process of their implementation.

**Mario Maldari:** But what we have within JAMA are vertical.

**Mario Maldari:** We talked a little bit about this yesterday.

**Mario Maldari:** We have like semiconductor, we have automotive, we have industrial, we have aerospace and defense.

**Mario Maldari:** And so what we've done is we have these solutions that, you know, we have consultants that are experts in the field.

**Mario Maldari:** They've come from industry, you know, so a lot of our consultants in medical, for example, they worked within the medical industry for, you know, 20 years.

**Mario Maldari:** And they come and they say, hey, let's build a framework that is representative.

**Mario Maldari:** of 80% of all medical device companies and how they work.

**Mario Maldari:** And here's how their requirement flows from high level all the way down the V model to testing and to defects.

**Mario Maldari:** These are how the requirement types relate to each other within medical.

**Mario Maldari:** And so then we can go to a medical prospect and we can say, hey, you know, we heard that you guys are looking for a requirements management tool.

**Mario Maldari:** We have an out-of-the-box framework that, you know, if you adopt us, you'll be 80% to where you need to be for FDA compliance, for example.

**Mario Maldari:** And so it has like out-of-the-box reports.

**Mario Maldari:** It has, you know, these traceability information models.

**Mario Maldari:** It has requirement types that they're familiar with.

**Mario Maldari:** And this is true across all of those industries.

**Mario Maldari:** Aerospace and defense, same thing.

**Mario Maldari:** Semiconductor.

**Mario Maldari:** This is actually an example of a semiconductor one here.

**Mario Maldari:** And so it just, it's a step up.

**Mario Maldari:** And so when I do marketing...

**Mario Maldari:** Content.

**Mario Maldari:** There's a couple of things that I do.

**Mario Maldari:** I focus, one, on product stuff, like we talked about, like AI and all that stuff, like new exciting features.

**Mario Maldari:** But then I also will focus on solutions.

**Mario Maldari:** So I want to highlight the fact that we just released a whole new semiconductor solution package that, you know, is years in the making.

**Mario Maldari:** And, you know, we had a press release on it, for example, and then I'm generating some marketing content.

**Mario Maldari:** We're doing, like, videos, you know, how-to videos and things like that.

**Mario Maldari:** So that's really, like, in terms of product marketing, it's like there's features and then there's solutions.

**Mario Maldari:** And that's what we really spend a lot of our time doing.

**Mario Maldari:** I think, yeah, I mean, that's pretty much it for the slides, just seeing if there's anything else here.

**Mario Maldari:** You know, we talk a lot about G2.

**Mario Maldari:** I'm not sure if you're familiar with the G2 review rating system.

**Mario Maldari:** So, you know, here we are.

**Mario Maldari:** We've worked.

**Mario Maldari:** It's really hard to kind of like continue year after year, maintain this spot, right?

**Mario Maldari:** And this picture, you know, the pictures say it all, but that's here's Codebeamer, you know, main competitor.

**Mario Maldari:** Here's Polarian, Siemens Polarian, IBM.

**Mario Maldari:** So, you know, when we go in front of prospects and we show this to say, hey, you know, don't take our word for it.

**Mario Maldari:** Here's G2.

**Mario Maldari:** Here's a bunch of reviews, you know, read about it yourself.

**Mario Maldari:** So, so we write a lot of marketing content on this every, every quarter or season where this stuff comes out, we'll be generating, you know, top of funnel type of stuff.

**Mario Maldari:** So, so that's pretty important.

**Mario Maldari:** Here, if you're curious about kind of, you know, customers that we work with, you know, take a look at this.

**Mario Maldari:** I'll send you these slides too.

**Mario Maldari:** I'll, I'll put them in the share.

**Mario Maldari:** But this, this speaks a lot too, because, you know, when we go to prospects for the first time, especially in Europe.

**Mario Maldari:** Thank you.

**Mario Maldari:** Okay.

**Mario Maldari:** know, they'll ask us, well, you know, who do you guys work with?

**Mario Maldari:** Like, you know, can you tell us some names of customers that we might know?

**Mario Maldari:** So this really establishes a lot of credibility.

**Mario Maldari:** And I typically won't ever give a prospect this slide because we don't have, like, permission to use all these names.

**Mario Maldari:** And so it's one thing to show it on the screen, but then I'm very careful with what we, you know, what we say officially.

**Mario Maldari:** Let's see.

**Mario Maldari:** And so, yeah, the only thing I'd like to call out on this particular slide is, you know, what makes us differentiated from, you know, other requirements products.

**Mario Maldari:** And I'd say, like, we're all doing the same thing in terms of requirements traceability.

**Mario Maldari:** That's what a requirements tool does.

**Mario Maldari:** It's like, how do the requirements link to each other?

**Mario Maldari:** If one changes, do you see downstream impacts of that change?

**Mario Maldari:** But what, so I worked at IBM for 14 years, 15 years.

**Mario Maldari:** So I know what their stuff does.

**Mario Maldari:** You know, I know their practices.

**Mario Maldari:** I

**Mario Maldari:** I know enough about the other competition, too, where, you know, I'd say that, like, the biggest thing that we offer, you know, that is above and beyond what they offer is this customer success program.

**Mario Maldari:** And really what it is, is like the consultants that I mentioned that are industry experts.

**Mario Maldari:** What happens, like at IBM, for example, like we sold Doors, Doors Next Generation, and the sales team was like happy to close the deal, boom.

**Mario Maldari:** Boom.

**Mario Maldari:** Good luck.

**Mario Maldari:** If you need, you know, need help later, later down the road, later down the year, we'll generate a services contract.

**Mario Maldari:** We'll, you know, help you out.

**Mario Maldari:** We'll, you know, you can, you can charge, you know, we'll charge you for it, basically.

**Mario Maldari:** And what ends up happening is they're going off on their own.

**Mario Maldari:** They're doing implementation and things go wrong and things go very wrong.

**Mario Maldari:** And then problems happen, you know, they're mad, we're, we're unhappy, you know, it gets.

**Mario Maldari:** If you're a very complex, you know, automotive company, you may feel as though you need, you know, a lot of support.

**Mario Maldari:** And so, you know, they have pricing options basically for doing that.

**Mario Maldari:** But I think our biggest thing is like getting involved very early, building that relationship, and then making sure they're successful.

**Mario Maldari:** So a big differentiator.

**Mario Maldari:** And it works really well.

**Mario Maldari:** And these guys, mean, the consultants, they are like the best of the best.

**Mario Maldari:** You know, like we handpick them, we'll go and recruit them from their jobs, you know, and say, hey, you know, come over and be a consultant.

**Mario Maldari:** So the other thing, too, that you'll probably be writing about is a big thing is security these days, like cyber security.

**Mario Maldari:** And so people always ask, like, are you SOC 2 compliant?

**Mario Maldari:** And that's a big deal.

**Mario Maldari:** And so we're SOC 2 compliant at the product level.

**Mario Maldari:** So the product itself has been certified as SOC 2.

**Mario Maldari:** And then our hosting environment, which is done.

**Mario Maldari:** Through Amazon AWS, that's also SOC2 compliant.

**Mario Maldari:** So really important to go into a conversation with IT teams to say, we are SOC2 compliant, not an issue, we can send you our report, we have penetration testing that occurs twice a year, we can send you that report.

**Mario Maldari:** And so once you sell a prospect on the functionality and the tool, this is the next step.

**Mario Maldari:** Like the IT team comes along and they start poking around, asking questions, and they want to make sure that you're at that level.

**Mario Maldari:** So we've produced a lot of marketing material to highlight this stuff as well.

**Mario Maldari:** So basically saying, you know, we have those certifications and, you know, you can trust us, basically.

**Mario Maldari:** The other thing from a product perspective, I think that you should be aware of too, is like, like hosting is such a big thing.

**Mario Maldari:** Like everyone wants to be cloud hosted for the most part.

**Mario Maldari:** So, you know, they want to get rid of hardware infrastructure, you don't have to pay to have a server.

**Mario Maldari:** वेव्ड़िर.

**Mario Maldari:** So a

**Mario Maldari:** You're sitting in your basement, whatever, you know, like no one, no one, that's an old school model, right?

**Mario Maldari:** Aside from aerospace and defense, they are like, we need on-prem installation.

**Mario Maldari:** I want to be disconnected from the internet so nothing bad happens.

**Mario Maldari:** And so that's true of, internationally, that's true.

**Mario Maldari:** It's true in the US, it's true in Europe.

**Mario Maldari:** But, and so there is a component, like when I write marketing material, in the back of my mind, I'm like, all right, well, I don't want to alienate, you know, the on-prem customer.

**Mario Maldari:** So how do I produce this content that, you know, is favorable for both of those audiences?

**Mario Maldari:** So that's something that we consider.

**Mario Maldari:** And if you guys ever have questions on that, then, you know, we can figure out the best way to position that.

**Mario Maldari:** But, but yeah, we get yelled at by the A&D team.

**Mario Maldari:** Okay.

**Mario Maldari:** What about our customers?

**Aida Knežević:** Yeah, the, the, I did see that you have like different.

**Mario Maldari:** Different cloud deployment options.

**Mario Maldari:** Yeah.

**Aida Knežević:** I was curious about those.

**Mario Maldari:** Yeah, so.

**Aida Knežević:** The slide deck.

**Mario Maldari:** Yeah, so I don't know if I have, let's see, do I have that in here?

**Mario Maldari:** Not sure if there's anything specific to that.

**Mario Maldari:** But yeah, so there's the basic cloud hosting that, you know, 80% of the customers would use.

**Mario Maldari:** But then we have something called the customer validated cloud.

**Mario Maldari:** And that's something that's like very specific to medical.

**Mario Maldari:** Where we have them like in a separate bulkhead.

**Mario Maldari:** Like the way it's hosted, it's like they're isolated.

**Mario Maldari:** It's, you know, been validated for them.

**Mario Maldari:** They can do their own testing, their own validation.

**Mario Maldari:** So yeah, there are a few different options like that.

**Mario Maldari:** But I'd say those are probably the two core hosting options.

**Mario Maldari:** It's just like the basic hosting where you don't have to worry that if you're sharing a tenant with another, you know, product.

**Mario Maldari:** sharing tenant with you And

**Mario Maldari:** Or there's the very isolated, custom-validated cloud, which is CVC.

**Mario Maldari:** And then there's also something called the GovCloud.

**Mario Maldari:** That's probably the third option there.

**Mario Maldari:** And so that's very, yeah, that's for a case where you're an A&D customer, a defense customer, and you're like, we don't want it on-prem.

**Mario Maldari:** Well, we do like cloud.

**Mario Maldari:** We like the concept of cloud.

**Mario Maldari:** But there are things like ITAR restrictions, which is big in the U.S.

**Mario Maldari:** Like you can't, like if, like no one outside the U.S.

**Mario Maldari:** can access that data.

**Mario Maldari:** So it's considered ITAR protected.

**Mario Maldari:** And I forget what the equivalent is in Europe, but they have one too.

**Mario Maldari:** So that's where GovCloud comes in to play.

**Mario Maldari:** And it's like, has different, you know, standards and rigidity, you know, if you will, that apply to that hosting option.

**Mario Maldari:** Yeah.

**Mario Maldari:** And so we can go through all that.

**Mario Maldari:** But I'd say like 80% are regular AWS hosting, you know, works for them.

**Mario Maldari:** And then the other 20% is somewhere.

**Mario Maldari:** Okay, so let me show you the product itself.

**Aida Knežević:** Okay.

**Mario Maldari:** And let me get kind of situated here to kind of our main dashboard.

**Mario Maldari:** And so what I always say when I'm demoing this, like the prospects is, all right, you know, here's just the Java Connect.

**Mario Maldari:** It's a web-based offering.

**Mario Maldari:** And I say that because there are still these legacy tools out there, like IBM Doors, where you have a client server interface.

**Mario Maldari:** So it's like you have the server on one machine, and then you have like this desktop installation that you have to install on every machine that you want to use this on.

**Mario Maldari:** So, you know, it's web, Java Connect is totally web-based.

**Mario Maldari:** And this is a hosted, you know, a hosted instance that you're seeing here.

**Mario Maldari:** And typically the first thing that people will do when they come into a project.

**Mario Maldari:** podcast.

**Mario Maldari:** podcast.

**Mario Maldari:** I

**Mario Maldari:** And so what you're seeing here is basically a graphical description or depiction of everything that's, you know, of interest to me within this project here.

**Mario Maldari:** So, for example, I want to, like, add a widget that shows me all my system requirements as a bar chart, you know, that's what I've done here.

**Mario Maldari:** Or show me all my hardware test cases as a pie chart, you know, that shows here.

**Mario Maldari:** And so as, like, a program manager that's, like, running this project, I can add widgets that I feel are important to keep track of as I do my, you know, requirements, authoring, and things like that.

**Mario Maldari:** And then you'll see this is, like, the traceability information model, TIM, for this particular project.

**Mario Maldari:** So, you know, I'm looking at the way I work in this project is I get a stakeholder need requirement from whomever I'm building this, you know, in this case.

**Mario Maldari:** Thank you.

**Mario Maldari:** It's a orbital system, say a satellite.

**Mario Maldari:** So NASA will send me a stakeholder need and they'll say, hey, Mario, build it like this.

**Mario Maldari:** And then I'll break it up into system requirements, maybe a cybersecurity asset to keep track of.

**Mario Maldari:** And then I'll further break it down to hardware requirements, software requirements.

**Mario Maldari:** Basically, as I build this satellite, I'm breaking it down into the smaller components and finally getting to be the test cases and then any defects that occur during my testing.

**Mario Maldari:** So this basically governs the flow of that V model from high level all the way down.

**Mario Maldari:** And something important to call out, they actually, during my interview for the company, they actually asked me, so tell us the difference between the solid lines and the dotted lines in the traceability information model and really what that means is that like a...

**Mario Maldari:** If I develop this traceability information model with a solid line interaction between these two artifacts, the software itself will enforce any situation where I don't have a relationship.

**Mario Maldari:** So if their stakeholder need comes in for product X and I don't have a system requirement linked to it, the software will have a red flag and basically say, hey, Mario, like you said, you define your traceability information model saying every time you have a stakeholder need, you need a system requirement.

**Mario Maldari:** You don't.

**Mario Maldari:** Do you want to fix that?

**Mario Maldari:** And so it's a way of enforcing it where the dotted lines are optional.

**Mario Maldari:** You may have a cybersecurity asset.

**Mario Maldari:** You may not.

**Mario Maldari:** That's up to you.

**Aida Knežević:** So kind of an important concept, whether you write about that or not, I don't know, but it'll be important for you to know about.

**Mario Maldari:** So, so, yeah, this is just basically kind of a program, typical program management stuff, like what are you interested in tracking, add it to your dashboard, right?

**Mario Maldari:** And you could have.

**Mario Maldari:** Multiple dashboards.

**Mario Maldari:** you were a requirements program manager, you'd have a dashboard for that.

**Mario Maldari:** If you were a test lead or manager, you'd probably have your own dashboard for, you know, your testing stuff.

**Mario Maldari:** You can, like, them.

**Mario Maldari:** Yeah, totally.

**Aida Knežević:** Depending on what you want.

**Mario Maldari:** Yeah, okay.

**Mario Maldari:** Yeah, totally.

**Mario Maldari:** And they're all based on, like, filters and queries.

**Mario Maldari:** So if I wanted to create a filter or query that says, show me all the system requirements that have not been approved yet, you know, you have these logical, like any query, show me, say, you know, hardware, architectural design that have no downstream items or, you know.

**Mario Maldari:** So you can basically narrow down your search.

**Mario Maldari:** Once you do that, you can put on your dashboard.

**Mario Maldari:** So, yeah, a lot of different options there.

**Mario Maldari:** So, but then, you know, you say, okay, well, I want to start working with requirements.

**Mario Maldari:** How do I do that?

**Mario Maldari:** So you come into your explorer tree and you have a hierarchy, basically like any hierarchy that you'd have in software.

**Mario Maldari:** Depending on how people work, know, they could be looking at, you know, like weight, weight tolerance or speed or whatever the case would be.

**Mario Maldari:** Every requirement can be different based on what you're, what you're looking to track.

**Mario Maldari:** But when some of the, you know, so assume these are all just, yeah, they are, they're all just requirements, functional requirements.

**Mario Maldari:** And if I wanted to look at them from like a, you know, a more holistic view, like show me all of the functional requirements in this folder, I can look at them in a few different ways.

**Mario Maldari:** Like the list view, like if you were coming from Excel and I'm like, hey, I know you guys work in Excel and I want to show you a view of what things in Java look like that are analogous to your working in Excel.

**Mario Maldari:** Here's the list view.

**Mario Maldari:** This is probably really familiar to you because it's column and row-based and it's not such a big stretch, you know, to come into, because a lot of times people are like, well, Excel's easy, you know.

**Mario Maldari:** I just like working in Excel.

**Mario Maldari:** And then they're like, it seems like it's going to be really complicated to come into a formal requirements tool.

**Mario Maldari:** I'll always show them this.

**Mario Maldari:** And so this is very similar to the way you work.

**Mario Maldari:** You know, you can update your description here.

**Mario Maldari:** You know, you can update your name.

**Mario Maldari:** So total working model, very similar to Excel.

**Mario Maldari:** Some people like Word.

**Mario Maldari:** And so we have this thing called the document view.

**Mario Maldari:** So it's showing the same requirements under functional requirements, only very much like a Word document.

**Mario Maldari:** So people can scroll through and take a look at their, you know, requirements.

**Mario Maldari:** They can even export it to Word if they wanted to, you know, formally look at it in Word.

**Mario Maldari:** So a few different ways of viewing those same requirements.

**Mario Maldari:** And then what's most important probably is this trace view.

**Mario Maldari:** So you'll say, okay, well, how do these requirements that I'm looking at, what's their traceability downstream?

**Mario Maldari:** You know, so based on that traceability information model, I should be looking at, you know, know, stakeholder.

**Mario Maldari:** you.

**Mario Maldari:** And they should be traced down to that next level system requirement, right?

**Mario Maldari:** And if I don't, like I mentioned, the tool is going to say, hey, you know, according to your traceability information model, you said you're supposed to have another downstream item type.

**Mario Maldari:** You don't.

**Mario Maldari:** Do you want to fix that right now?

**Mario Maldari:** And so it allows me, it's kind of like a working model in terms of like my traceability, essentially.

**Mario Maldari:** So then I can scroll down and I can look, okay, you know, one level down, two levels down.

**Mario Maldari:** As far as my traceability goes, I should be able to navigate that chain of traceability from high level all the way down to these.

**Mario Maldari:** In this case, it's my test runs.

**Mario Maldari:** So I could see what's like failing, you know, what's still left to be executed.

**Mario Maldari:** And then I can totally customize this.

**Mario Maldari:** Like if I wanted to say, show me the test status.

**Mario Maldari:** Now I have a column here where I can show all my tests that have passed, the ones that have failed.

**Mario Maldari:** And at the end of the day, if I'm like launching the satellite and I...

**Mario Maldari:** They'll have failed test cases.

**Mario Maldari:** I can say, hey, we're not ready to go, guys.

**Mario Maldari:** Like, you know, we got a problem.

**Mario Maldari:** And it all goes back to the question is like, you know, was the requirement to begin with well written, right?

**Mario Maldari:** And because I'm running a test and it passed, but it passed because, you know, it was testing something that, you know, it didn't make sense.

**Mario Maldari:** And I passed a test based on a poorly written requirement.

**Mario Maldari:** It goes out the door and then they find a problem.

**Mario Maldari:** And so to that point, so if I'm looking at these functional requirements again, and I want to say, well, how, you know, how good are these requirements?

**Mario Maldari:** Let's let's use AI.

**Mario Maldari:** And this is where AI comes in.

**Mario Maldari:** So JAMA Connect Advisor, I want to do a batch analyze of these.

**Mario Maldari:** Oops, sorry.

**Mario Maldari:** Let me do that again.

**Mario Maldari:** Minimize the window.

**Mario Maldari:** Batch analyze of these items, 133 of them.

**Mario Maldari:** It's going to look at 133 fields.

**Mario Maldari:** You know, that sounds good.

**Mario Maldari:** Let's analyze.

**Mario Maldari:** So then I can start to look at the first item here and it says, oh, okay, you know, you're at 100%, nothing's flagged.

**Mario Maldari:** You're all good there.

**Mario Maldari:** I can start scrolling down through each of those 133 requirements and I can start to see my quality is starting to go down.

**Mario Maldari:** You know, I'm getting 91% instead of 100.

**Mario Maldari:** And so what's going on?

**Mario Maldari:** So it's saying, hey, it's flagging.

**Mario Maldari:** You're using absolute terms.

**Mario Maldari:** You're, you know, using universal language, which you should be more specific because if you're writing a test case to this requirement, you want to know exactly what you're, you know, testing.

**Mario Maldari:** You don't want to use ambiguous terms, things like that.

**Mario Maldari:** And so, you know, 91, it's not really that bad, but, you know, if I wanted to refine it, I can get a suggestion and say, well, tell me what you do differently, Mr.

**Mario Maldari:** AI.

**Mario Maldari:** And then, you know, AI would come up with some suggestions for how I could rewrite it.

**Mario Maldari:** And if I accept them, presumably it goes back.

**Mario Maldari:** So it's a way of, you know, before you get to linking any downstream requirements, you're making sure that the quality of your stuff is good.

**Mario Maldari:** So yeah, so that's a big deal.

**Mario Maldari:** And then we have reports, you know, that, you know, a lot of customers said, well, that's great, you can do an analysis, but I want a report that I can export and I can share with my team and we can work to correct these things.

**Mario Maldari:** So we offer that as well in terms of, you know, some of the functionality.

**Mario Maldari:** So that's how to get the quality in place.

**Mario Maldari:** And so assuming the quality is good, you know, and I'm ready to go with these requirements, maybe I want to do a test case generation and say, okay, you know, looking at this particular requirement for volume control, let's see what, how we can test this.

**Mario Maldari:** And then I can provide some context, like what type of test would it be for, you know, it's volume control.

**Mario Maldari:** So maybe it's a volume knob for, you know, receiver, I can say hardware.

**Mario Maldari:** It's, let's say, a functional test.

**Mario Maldari:** And then you can further qualify it by vertical.

**Mario Maldari:** Like, what industry are you in?

**Mario Maldari:** And, you know, what this does is kind of puts, like, nomenclature for, like, defense.

**Mario Maldari:** You know, like, what are the common things that a defense company would look for in testing?

**Mario Maldari:** So you can select the context, basically.

**Mario Maldari:** And I'll just say aerospace and defense.

**Mario Maldari:** And then generate test cases.

**Mario Maldari:** And, yeah, basically gives me 10 test cases that I can look at here.

**Mario Maldari:** And with steps, which is great.

**Mario Maldari:** So this is what I'm saying.

**Mario Maldari:** Like, this saves a ton of time.

**Mario Maldari:** This would probably take, I don't know, half a day to do 10 tests with these steps.

**Mario Maldari:** So I can look and I can review these, know, go through each of them.

**Mario Maldari:** I can say, okay, yeah, they all look, you know, look great.

**Mario Maldari:** Let's, you know, take them all.

**Mario Maldari:** And when I say, let's see if I...

**Mario Maldari:** Pick a location.

**Mario Maldari:** It's going to say, where do you want to save the tests?

**Mario Maldari:** And the nice thing about JAMA Connect is, like, it'll gray out anything that's not applicable.

**Mario Maldari:** It's like, hey, you you wouldn't put your test cases in your project management folder.

**Mario Maldari:** You'd actually put them in your test case and validation folder.

**Mario Maldari:** And so that's the only thing that's highlighted.

**Mario Maldari:** So it kind of helps with usability.

**Mario Maldari:** So I'll say I want to put it there.

**Mario Maldari:** And then for every test case I select, I would say generate selected test case.

**Mario Maldari:** And it would actually go and not only create each of those test cases in that folder, but more importantly, it would link them with traceability back to the original requirement.

**Mario Maldari:** And why that's important is if anything changed upstream with the requirement itself, all of these test cases that are linked will be marked what's called suspect.

**Mario Maldari:** And they'll have a suspect flag.

**Mario Maldari:** And basically what that means as a tester, if I'm a tester and I log in in the morning and I see all my 10 test cases.

**Mario Maldari:** Cases have this little red mark next to them.

**Mario Maldari:** I'd say, oh, shoot, something changed, like, with the core requirement that I'm testing.

**Mario Maldari:** Like, someone upstream must have changed, like, the hardware volume or whatever the case might be to the point where I need to reassess all of these test cases and make sure that they're still accurate and either modify them or maybe they just changed, like, some innocuous thing, like, they fixed a spelling error and it still flagged all my stuff.

**Mario Maldari:** That's because I want to know about that, but I can say, hey, okay, that's not a big deal.

**Mario Maldari:** I'll clear that suspect flag.

**Mario Maldari:** And really, to be honest with that's, like, if you would ask me, like, you know, say one thing that's important about traceability, like, why is traceability important?

**Mario Maldari:** Suspect triggers are probably the most important thing because it's one thing to link requirements to each other in terms of traceability, but what you're really trying to figure out is what changed in their relationship so that when you're building...

**Mario Maldari:** ...

**Mario Maldari:** Building this thing, you know that something like your stakeholder requirement, that's probably the biggest example, like, oh, NASA changed the requirement for what they want me to build.

**Mario Maldari:** They don't want it to go so high up into space.

**Mario Maldari:** They want it to orbit around the planet.

**Mario Maldari:** Everything, everything downstream of that one stakeholder requirement now is suspect.

**Mario Maldari:** Like, you change that, everything downstream.

**Mario Maldari:** And so that's why it's such a big deal.

**Mario Maldari:** And, you know, we have things that you'll, you'll read about called like impact analysis.

**Mario Maldari:** And so if I were, you know, working with these stakeholder requirements, and I said, hey, I'm going to make a change to this one.

**Mario Maldari:** I wonder who I'm going to impact downstream.

**Mario Maldari:** I can run this impact analysis.

**Mario Maldari:** And here's my source item that we're looking at, you know, kind of a main capability stakeholder need.

**Mario Maldari:** And then I can see, okay, direct relationship, it's linked to, you know, these eight or so.

**Mario Maldari:** So, you know, downstream requirements.

**Mario Maldari:** And then further downstream, it's linked to, you know, two degrees of separation, three degrees of separation, four degrees.

**Mario Maldari:** So I can assume that if I make a change to this, all of these guys are going to be marked as suspect.

**Mario Maldari:** I'm going to impact, you know, the hardware team.

**Mario Maldari:** I'm going to impact the software team.

**Mario Maldari:** And so it gives me a sense before I make a change of kind of the impact I'm going to make.

**Mario Maldari:** Like, so then I can go and I can use some of our, like, collaborative features and I can go to the, you'll see a sidebar here, comments.

**Mario Maldari:** And I can, like, at mention someone, you know, I can mention, you know, me in this case and say, about to make a big change.

**Mario Maldari:** And I can further qualify it saying, hey, you know, we need a decision on this.

**Mario Maldari:** And when I comment, it'll basically send me an email to my inbox and I can respond by email and say, hey, don't make that change yet.

**Mario Maldari:** Let me, let me talk to the other team.

**Mario Maldari:** And give me till Friday to figure this out.

**Mario Maldari:** And so this is part of our kind of collaborative feature.

**Mario Maldari:** And we talk a lot about that in JAMA.

**Mario Maldari:** It's like the collaboration.

**Mario Maldari:** And the same with the reviews.

**Mario Maldari:** You'll see, you know, these menu items up here.

**Mario Maldari:** We have a whole review center that's kind of a separate part of the tool.

**Mario Maldari:** And so they're basically like packages of requirements that I've sent to review.

**Mario Maldari:** And so this can be like my team.

**Mario Maldari:** I want them to, you know, review all these requirements, sign off on them officially.

**Mario Maldari:** Or maybe I want my folks at NASA to sign off on them.

**Mario Maldari:** I can actually, even though like NASA is not buying licenses to JAMA, you can include them in the review process.

**Mario Maldari:** So they'll get like a stakeholder license where you're going to invite to participate, but you don't pay for any licenses for them.

**Aida Knežević:** So that's a big selling feature for us too.

**Aida Knežević:** Like invite anyone you want, you know.

**Mario Maldari:** If you're ever, like, wanting to poke around and maybe even, like, the help is, like, you know, really useful, like, for reading about features or, like, if you're developing content that you want to, like, look at the review center, you know, how do we describe that?

**Mario Maldari:** You know, you could even take something like this, copy and paste into AI, generate a blog for review and approval.

**Aida Knežević:** Yeah, yeah.

**Mario Maldari:** So, you know, let me know if you do want that, but it might be, might be helpful for you to have access to, like, a demo environment, so.

**Aida Knežević:** Yeah, I think that especially the documentation is really helpful.

**Aida Knežević:** Now, this was great.

**Aida Knežević:** I think for, for me, it's important, like, obviously, like, the platform itself, when you're looking at it as somebody who's not part of the, like, doesn't do that every day, it seems there's a lot of, like, different parts.

**Aida Knežević:** But we, like, I understand what is the process, like, what are the issues that you're solving, what are the workflows that it supports, so that's the most.

**Mario Maldari:** Most important thing for us to understand and how it all functions together.

**Mario Maldari:** So this was a really great walkthrough.

**Mario Maldari:** Thank you.

**Mario Maldari:** Good.

**Mario Maldari:** Yeah, I never know.

**Mario Maldari:** It's like too high level, too low level, try to get in between.

**Aida Knežević:** Yeah, for us, it's important to understand what you do.

**Aida Knežević:** And then we have to also constrain the product feature matrix.

**Aida Knežević:** So that because sometimes AI might make conclusions that you might do something because generally speaking, platforms in your like your competitors might be doing it.

**Aida Knežević:** So it might infer that you also do it.

**Aida Knežević:** So we have this whole feature matrix that is used as kind of for the fact checking.

**Aida Knežević:** Yeah.

**Aida Knežević:** Yeah.

**Aida Knežević:** All right.

**Aida Knežević:** Great.

**Aida Knežević:** So this was really helpful.

**Aida Knežević:** We're going to use it to generate the artifacts that I'll share with you as soon as they're ready.

**Aida Knežević:** I've followed up on your email, so I just need access to the documents that you shared with me yesterday.

**Aida Knežević:** Over email.

**Aida Knežević:** I think you might just need to add my email address so that I can like type it in.

**Mario Maldari:** Yeah, let me know.

**Mario Maldari:** I think I did that right before this call.

**Mario Maldari:** So let me know.

**Aida Knežević:** Oh, okay.

**Aida Knežević:** So I'll double check.

**Aida Knežević:** All right.

**Aida Knežević:** Sorry.

**Aida Knežević:** I was in a million tabs open.

**Mario Maldari:** Yeah, I know.

**Mario Maldari:** I did it like pretty much right before the call.

**Aida Knežević:** So.

**Aida Knežević:** Okay, perfect.

**Aida Knežević:** I will double check and then I will let you know.

**Aida Knežević:** Yeah.

**Aida Knežević:** All right.

**Aida Knežević:** Great.

**Aida Knežević:** Well, this was really helpful.

**Aida Knežević:** Again, thank you so much for your time.

**Aida Knežević:** Of I can, I'll follow up in Slack later.

**Aida Knežević:** I'm not sure if you're in our Slack channel yet, but typically we use Slack for like all comms.

**Mario Maldari:** Yeah, we do too.

**Aida Knežević:** Okay, perfect.

**Mario Maldari:** Yeah.

**Aida Knežević:** In that case, I'll send a follow up in a little bit.

**Aida Knežević:** Okay.

**Aida Knežević:** And yeah, I'll let you know if we have any other questions.

**Mario Maldari:** Yeah, sounds great.

**Mario Maldari:** And then do we have our reoccurring meeting scheduled yet?

**Aida Knežević:** Is that, or is that what you were talking about at the beginning?

**Aida Knežević:** That was what I was talking about.

**Aida Knežević:** So that's going to be scheduled today.

**Mario Maldari:** Okay, perfect.

**Mario Maldari:** All right, great.

**Mario Maldari:** Well, yeah, in the meantime, let me know if there's anything that comes up.

**Aida Knežević:** Sure.

**Aida Knežević:** We'll talk soon.

**Aida Knežević:** Thank you so much.

**Aida Knežević:** Thank you.

**Aida Knežević:** Have a good day.

**Aida Knežević:** Bye-bye.

**Aida Knežević:** Thank you.
