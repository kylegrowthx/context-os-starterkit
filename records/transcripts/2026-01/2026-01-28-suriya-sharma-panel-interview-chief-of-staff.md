# Suriya Sharma Panel Interview | Chief of Staff - Ops & Special Projects

---
**Meeting Date:** 2026-01-28
**Duration:** 46 minutes
**Enriched On:** 2026-03-01 00:00 UTC
**Source:** fireflies
**Transcript ID:** 01KFY02FCX13SEZY2E14TTBXN3

**Participants:**
- Suriya Sharma (candidate for Chief of Staff - Ops & Special Projects)
- Bridget McGillivray (GrowthX, Head of Customer Operations)
- Marcel Santilli (GrowthX, CEO)

---

## Summary

Suriya Sharma presented a data-driven proposal to restructure GrowthX's delivery from linear headcount scaling to a marketplace contractor platform. The core validation framework prioritized customer quality and trust first, then margin improvement, then contractor supply sustainability. The team converged on a narrow internal shadow pilot using real customer data, with Marcel emphasizing the hard problems: automated vetting at scale and sustainable supply acquisition across fragmented talent networks.

---

## Context

Suriya Sharma (candidate for Chief of Staff - Ops & Special Projects) came prepared with a pre-read document proposing a marketplace-style delivery platform. Marcel Santilli and Bridget McGillivray used the interview as a working session: Suriya presented her strategic thesis while Marcel and Bridget drilled into execution details, validation sequencing, and hard operational constraints. This was a high-engagement working interview—not a Q&A format—that moved from concept validation to specific implementation challenges around vetting automation and supply chain sustainability. Suriya showed deep ops thinking, willingness to engage directly with pushback, and grounded understanding of the cold-start problem in marketplace dynamics.

---

## Relevance to GrowthX

### Delivery & Operations
This directly addresses GrowthX's binding constraint: delivery scales only through linear headcount growth. Recent Time Doctor implementation and international hiring expansion have added operational overhead without structural relief. High editor turnover (mentioned in the conversation) compounds this. A contractor marketplace could unlock flexible, tiered capacity without fixed-cost commitments.

### Quality & Risk Management
The core risk is customer trust erosion from quality degradation or "slop that escapes"—the meeting cited $200–300k contracts at risk when editors miss review cycles. The validation framework (customer quality first, margins second, supply third) directly maps to this risk structure.

### Business Model & GTM
Resolves the tension between managed services (high-touch, high-margin) and marketplace (lower-touch, volume-based). Opens questions about market segmentation: Do we offer marketplace alongside managed services, or as internal working model only? This affects customer positioning and pricing power.

### Finance & Scaling
Potential upside: flex capacity without marginal hiring costs. Margin improvement only if vetting automation succeeds and supply acquisition doesn't require inefficient customer-acquisition-style spending. The discussion surfaced this isn't a simple cost reduction—it's a structural business model bet.

---

## Overview

- **Marketplace Delivery Model:** Proposed shift to algorithmic platform for scalable contractor matching to reduce costs and improve flexibility
- **Internal Pilot Testing:** Real customer data used to compare contractor output with current editors to verify quality without client awareness
- **Quality Assurance Focus:** Multi-step vetting processes including AI tools ensure contractors meet quality standards, requiring ongoing performance monitoring
- **Financial Feasibility Priorities:** Customer needs addressed first, followed by margin improvement and reduced operational overhead as part of pilot testing
- **Contractor Supply Strategies:** Use internal networks and freelance platforms to build contractor pools while ensuring quality, retention, and incentives
- **Prototyping and Scaling Plan:** Launch internal pilot to validate quality, with phased external testing based on successful outcomes and clear metrics

---

## Key Topics

### The Problem
GrowthX has strong demand, healthy margins, and proven customer outcomes. But the delivery model scales through linear headcount growth. High editor turnover compounds the problem. This creates two constraints: low scalability and lack of flexibility.

### The Marketplace Concept
Restructure delivery into a marketplace that:
- Taps into global specialized contractor talent
- Uses tiered skill levels and algorithmic task matching
- Enables rapid capacity scaling without fixed headcount
- Includes rigorous vetting, clear task definitions, and built-in learning loops

### Validation Priorities (in order)
1. Can we maintain quality and customer trust?
2. Can we improve margins with this model?
3. Can we access the right contractors to meet customer needs?

Marcel's framing: "You can always improve margins on something that's working. It doesn't matter if you improve margins on something that's not working."

### Vetting Contractors
- Give contractors access to the internal AI tool
- Have them complete tasks using blinded customer data
- Compare output to existing employee work
- Include an onboarding/test period before full deployment
- Over time, identify signals that predict success to reduce vetting intensity

### Key Risks and Mitigations
| Risk | Mitigation |
|------|------------|
| Quality degradation | Narrow pilot scope, internal QA |
| Cannibalization of core business | Internal-first use, segment products clearly |
| Pricing uncertainty | Iterative testing with prospects and customers |
| Operational complexity | Avoid overbuilding, use third-party tools |

### MVP Platform Features
- Contractor login and authentication
- Task assignment routing
- Third-party payment integration (don't build payments infrastructure)
- QA routing to grade contractor output

### Contractor Sourcing
- Internal employee networks
- Existing recruiters
- Freelance marketplaces (Upwork, Fiverr)
- Former editors who left on good terms
- Data labeling marketplaces as a model (Scale AI, Surge)

Marcel highlighted the cold start problem: contractors won't stay engaged without consistent work volume. Supply acquisition requires treating contractors like customers with acquisition costs and retention strategies.

---

## Decisions & Commitments

### Explicit Agreements
- **Prioritize quality validation first:** Don't chase margin optimization until customer quality and trust are proven sustainable.
- **Narrow internal pilot scope:** Focus on specific task types, small contractor cohort, and limited customer datasets—not end-to-end build.
- **Third-party payments, not custom build:** Use existing payment infrastructure (Stripe, Wise, or marketplace payment providers) to avoid multi-year build cycle. Marcel cited payment infrastructure lessons from Scale AI and Everlance to emphasize this.
- **Concurrent workstreams:** Parallel tracks for MVP platform build and contractor sourcing while awaiting infrastructure decisions.

### Validation Sequencing
1. **Can we maintain quality and customer trust?** (top priority—hard stop if fails)
2. **Can we improve margins while maintaining quality?** (secondary—more unknowns here)
3. **Can we access sustainable, diverse contractor supply?** (tertiary—operations challenge, not viability blocker)

### Critical Implementation Assumption
Marcel's framing: "You can always improve margins on something that's working. It doesn't matter if you improve margins on something that's not working." This pins the entire effort to proof-of-quality first, efficiency second.

---

## Open Questions

**Strategic:**
- Should the marketplace be customer-facing (customers know they're matched to contractors) or internal-only (managed services facade)?
- How do we segment the market: reserved managed services tier vs. marketplace tier?
- Over time, do all delivery move to marketplace, or do we maintain a premium managed services tier?

**Execution:**
- How do we automate vetting at scale without creating manual bottlenecks (the "army of recruiters" problem)?
- What's the minimum viable vetting signal that predicts contractor success without requiring human-in-the-loop?
- How do we calibrate the quality bar across different task types (articles vs. newsletters vs. specialized content)?
- Where is the sustainable supply edge: freelance platforms (Upwork, Fiverr), data labeling networks (Scale AI, Surge, Handshake), internal networks, or recruiting firms?

**Financial:**
- What pricing models maintain margin improvement while remaining competitive with managed services?
- What's the acquisition cost of contractor supply across different sourcing channels?
- What's the payback period on contractor sourcing and vetting investment?

---

## Action Items

### Suriya Sharma (Candidate, GrowthX)
- Build MVP platform with contractor login, task assignment, and third-party payment integration (defer custom payment infrastructure)
- Develop grading rubric and SLA framework for evaluating contractor output quality, delivery speed, and consistency
- Define narrow scope of tasks and content types for pilot (e.g., article creation only, not newsletters)
- Source initial contractor cohort using internal employee networks, existing recruiters, and freelance marketplaces (Upwork, Fiverr, data labeling platforms like Scale AI and Surge)
- Design contractor onboarding flow and test assignment protocol that mirrors real customer tasks with blinded customer data
- Establish internal QA process: contractors produce work in parallel with existing editors on same customer data, blind comparison and grading
- Conduct post-pilot pricing experiments with prospects and customers once quality validation is complete

### Marcel Santilli (GrowthX, CEO)
- Review and align on contractor vetting signal framework (current full-time hiring workflows + what adapts vs. what changes for contractors)
- Confirm third-party payment infrastructure options and decision criteria
- Provide existing editor hiring and vetting workflows as baseline for contractor comparison

### Bridget McGillivray (GrowthX, Head of Customer Operations)
- Identify and recruit early test contractor cohort: recent ex-editors open to freelance work, plus new talent for diversity
- Define SLA expectations for contractor deliverables (turnaround time, revision cycles)
- Design training module and test assignment content that reflects real customer work

---

## Full Transcript

**Bridget McGillivray:** Hey, Suriya. How are you?

**Suriya Sharma:** I'm good. How are you?

**Bridget McGillivray:** Good, thanks. I totally thought this was at one o'clock for some reason, just in another world, but at least I saw the Slack notification.

**Suriya Sharma:** Yeah, no, this definitely happens to me a lot.

**Bridget McGillivray:** Oh, Marcel's in the office.

**Marcel Santilli:** What's up?

**Bridget McGillivray:** Hey. We're gonna be eating during this, right?

**Marcel Santilli:** Yeah, we're gonna be eating during this. No, I've been recording. We were recording some videos for product launch next week. That was good. But good to see you again.

**Suriya Sharma:** Yeah, you too.

**Marcel Santilli:** Thanks for wanting to do this and turning it around so quickly.

**Suriya Sharma:** Of course. Happy to be here.

**Marcel Santilli:** Yeah, excited to keep the conversation going. Bridget, why don't you take it away?

**Bridget McGillivray:** I saw your pre-read, but whatever you want to share would probably be helpful if we're all looking at the same thing. We'll keep it super interactive and try to ask questions throughout. More conversational than anything. Any questions from you before we start?

**Marcel Santilli:** Actually, why don't you give me three minutes to quickly read it? I'll probably be better with context. I didn't get a chance to read it before.

**Suriya Sharma:** Sure.

**Bridget McGillivray:** We'll take a three minute pause. I'm just going to go get water.

**Marcel Santilli:** Awesome. Yeah, let's jump in. You can approach this like we kind of have some familiarity with the concept, but it's mostly a "here's what I'm thinking" kind of discussion. We want to ask questions and discuss things as we go. But if you want to start with an elevator pitch—even though I've read the pre-read, it's always good to hear your thought process behind this.

**Suriya Sharma:** Yeah, of course. So the elevator pitch is: I do think this is something GrowthX should invest time and limited resources into exploring. I think it could really unlock scalability and build financial leverage with fewer editors needed per account. And I think we can do it without sacrificing quality.

The risks are manageable with the phased internal first approach and potential upside is significant. So I do think that this is something that's worth pursuing in kind of a limited resources fashion.

The problem today is GrowthX has strong demand, healthy margins and proven customer outcomes. But the delivery model still scales primarily through just linear headcount growth. There's not really a systematic, automated way to match customer tasks with each editor based on their expertise and customer knowledge. And Bridget mentioned there's high turnover in the role, which makes this even tougher. This creates two main constraints: low scalability and lack of flexibility.

Now that customer demand is really growing quickly, it seems like a good time to explore this as either an additional growth lever or a fully new delivery model.

**Marcel Santilli:** Yeah, like for example, last week we implemented Time Doctor. So there's a lot of things around trying to get people to submit or self report on what they're doing, how they're doing it, then have to ask a lot of people about like, hey, if there are quality issues, why are there quality issues? And then figure out the quality issue is a performance issue.

And then even if you arrive at all those conclusions where like, hey, this person's taking four times more to do the same thing and their output quality sucks, then you still have to then go, cool, let's go hire somebody. And then it's like two more months to hire and onboard, right? So that becomes pretty hard.

And it's either they quit their jobs and come work for us full time or they don't work for us at all. Because managing like Upwork is pretty hard. We try to do freelancer stuff in Upwork and we still do like one off things. But like for these types of roles, it's pretty difficult, you know, because we have to give them access to Notion and a bunch of other things. So like there's just too much there, right.

And so that's a little bit of extra context. The number of times even now that a customer will lose trust in us—and the main reason, or one of the main reasons is often slop that a person didn't catch or just kind of let it go through, and like including like major logos. Like so you're talking like 200, 300 grand contract that is at risk because some editor decided to not read the damn thing they're supposed to read, you know. And so that's a little bit of the context of like, and the urgency for it too, you know.

**Suriya Sharma:** Yeah, that makes a lot of sense. And so definitely I think like the learning, built in learning loops and quality signals and feedback is definitely something I think that has to be true for success both of GrowthX in general, but then also for this marketplace. It's one of the things kind of I listed here is like making sure that there are standards for the production time and the production quality and making sure there's ways to kind of monitor. That definitely makes a lot of sense.

**Suriya Sharma:** So to elaborate: the initiative would involve restructuring delivery into a marketplace that taps into global specialized contractor talent, uses tiered skill levels and algorithmic task matching, and enables rapid capacity scaling without fixed headcount. We can flex capacity based on our needs.

What must be true: First, we need a platform that's way easier to access than giving contractors Notion access and everything else. Simple onboarding is critical. We need clear expectations and transparent performance feedback. We need rigorous vetting and tiering—you guys have that process for full-time hires, but for contractors we need to move faster while not lowering standards.

We also need clear task definition. Bridget, you mentioned articles vs. newsletters. We need to be distinct about what goes to the marketplace versus what stays in managed services. And we need built-in learning loops to improve routing and standards while maintaining the high quality bar we have today.

**Bridget McGillivray:** How do you think we could do vetting?

**Suriya Sharma:** A couple things. First, looking at someone's work product is the best way to understand how they'll perform. Give them access to the internal AI tool, have them produce work, then compare it to your gold standard work from existing employees. You could even give them blinded customer data and compare their output directly. How does the contractor hold up?

That comparison data could also help train the AI model to judge itself. Beyond work product, look at experience and past work—have they worked with similar companies or content types? That matters.

But while there's more accessibility to talent with a marketplace approach, the quality variance will be real. You need to account for that in vetting.

**Suriya Sharma:** And critically, after hiring, there needs to be a test period—an onboarding period—where we see their work in real time and validate it against our standards. When they create net new materials, they need to achieve the level of customer trust and quality we maintain.

**Bridget McGillivray:** Absolutely. They won't know how to use our platform right away, so there need to be training modules they complete. Then: take a fake customer, have them run some articles, compare to what proven performers created, and keep them in a training pattern before taking off the training wheels.

**Suriya Sharma:** Exactly. Mini pilots with each contractor—intensive at first, but critical for maintaining quality. Over time you'll identify success signals and can reduce testing rigor. The key risks: quality degradation would be a huge disservice to our customers and damage reputation—that's the most important thing. Then there's cannibalization of the core business. If we offer this as a lower price point, we need to make sure we're not cannibalizing managed services. We figure out later if we want to transition everyone over while maintaining the high-touch white glove impression.

Pricing uncertainty is another risk—getting the contractor incentives right while protecting our margins. The goal here is financial leverage.

And operational complexity: payments infrastructure, trust-building with contractors, managing a large contractor pool. These are real overhead challenges.

To mitigate quality risk: narrow pilot scope with internal QA. To mitigate cannibalization: internal-first testing and clear product segmentation. To mitigate pricing risk: iterative testing with prospects and customers. To mitigate operational complexity: avoid overbuilding and stay iterative. Build for proof of success, then build the next piece. Don't get ahead of validation.

**Marcel Santilli:** So just to understand: are you suggesting we build the end-to-end platform first, or where do we start? What exactly do you mean by "internal only"?

**Suriya Sharma:** An internal pilot that runs side-by-side with existing customers. Our editors create articles and newsletters as normal. In parallel, a contractor does the same work. We compare quality, speed, and output side-by-side. And the customer themselves won't know that we're kind of doing this dual side testing—it'll just be internally, but we'll be using real customer information.

**Marcel Santilli:** So we keep running a customer the way we're running today and then we're creating like a shadow approach here. So for the work—do we hire people we already have, or source freelancers? Who's doing the work in the shadow channel?

**Suriya Sharma:** We'd source freelancers. Build an MVP so contractors have access—just enough to test, not a full platform. Login, task assignment, payments. If quality is consistent and meets standards internally, we move to a small external beta with customers.

**Marcel Santilli:** Before we go deeper: do we build payments infrastructure first, or test first then build?

**Suriya Sharma:** Minimum infrastructure to test the model internally. If we can partner with a third-party payment tool, great—we don't build that ourselves. The goal is building only what's needed to validate. Minimum infrastructure: contractor login, task assignment layer, third-party payment integration, and a QA routing layer to grade output. Don't overbuild before validation.

**Marcel Santilli:** Got it. When we talk about validation, what exactly are we validating? Imagine I pull you into a board meeting next week—what are the things we're telling the board we need to validate? The marketplace concept exists; you don't need to validate that. You need to validate that you can actually *build* a marketplace given the cold start problem. This isn't a yes/no—it's a "how." What are the questions of the how?

**Suriya Sharma:** A couple things. One: can we maintain our quality and customer trust? Second: can we do this in a way that improves margins? Can we source contractors, route work to them, and operate the platform better than today? We need to ensure operational overhead and sourcing/onboarding costs don't make margins worse. Third: does this actually work for our customers? Can we access the right contractor types and tap into global talent to match customer needs?

**Marcel Santilli:** How would you rank these three?

**Suriya Sharma:** Customer needs first—if it can't do that, it's a hard stop. I'd rank cost benefits third because intuitively there will be cost efficiencies. Validate customer impact first, then help our top line and build trust without damaging reputation. If those two work, I feel good moving forward. The cost piece can be optimized later with efficiencies and automations.

**Marcel Santilli:** I agree—that's the exact order I'd do. And the way to think about it: you can always improve margins on something that's working. It doesn't matter if you improve margins on something that's not working. Always solve for effectiveness first, efficiency second. Go in the right direction slow rather than fast in the wrong direction. Effective first, efficient second.

Assume we have great engineers and build an MVP. About payments: don't try to build one yourself. It'll take a year. At Scale AI, it's a nightmare—different countries have different banking and AML laws.

**Bridget McGillivray:** You have scars from that. Suriya, didn't you build a payment engine at Everlance?

**Suriya Sharma:** Yeah, it was an adventure.

**Marcel Santilli:** Exactly. So let's assume we use a third-party solution. Say we have a working MVP by Monday—what's the first thing you'd do?

**Suriya Sharma:** Once we have the MVP, we solidify the guardrails. Be really narrow: specific task types, specific contractor subset, specific customer/prospect subset. Then we get out and validate.

We need clear grading structures for all contractor output and clear SLAs for delivery speed. We launch internally on existing customer work in shadow mode—editors and contractors work in parallel. We do internal QA and compare outputs. If quality is good and speed is good, we're moving in the right direction.

**Marcel Santilli:** Who's doing the work in this shadow example? Where did the contractors come from?

**Suriya Sharma:** While we build the MVP infrastructure in parallel, we find sourcers to locate contractors. Multiple methods: First, leverage internal employees—they know people open to contractor work. Second, reach out to existing recruiters with contractor opportunities. Third, tap into freelance marketplaces like Upwork where people advertise services.

Also, we can reach out to ex-editors who left on good terms—high performers from our past could be good test cases. But we want diversity in the cohort. We need to understand which sourcing channels are efficient and what quality they deliver. We don't want to bias toward people we already know are good.

**Bridget McGillivray:** I actually just interviewed an ex-editor today who wants to go back to freelancing. That could work. That could be a test subject. But also find people fresh to this to see what the real experience looks like.

**Marcel Santilli:** Are there businesses or models similar to what you found in research, beyond Upwork? Anything else you've seen?

**Suriya Sharma:** Webflow has a similar model. They have a certification program—Webflow-certified professionals can add it to their resume and build templates for the marketplace. It's a flywheel: position GrowthX as a top tool, incentivize people to learn and get certified, and you tap into a huge network while boosting your contractor supply. They encourage people to join by building the certification into their marketplace rather than cold-outreach.

There's also Fiverr, but the key is being specific about the type of freelancing and talent you're targeting.

**Marcel Santilli:** The biggest one you missed: data labeling networks. Companies like Scale AI, Surge, Handshake, and others have tens of thousands to hundreds of thousands of people doing task-based work to create training data. It's a fully vetted network. People list what they do and their expertise. Platforms like Outlier, Surge Data Annotation, Merkle, etc. Some do this fractionally, many make it their main income.

Critical thing: marketplace liquidity. If you recruit the right person but give them one job every six weeks, they can't make a living. You need enough demand and liquidity so contractors get consistent work and don't bail.

**Bridget McGillivray:** When you say "managed services," are you thinking: core in-house editor team doing premium delivery, versus customers matched to contractors through the marketplace?

**Suriya Sharma:** That's the key question. Once we validate quality, throughput, and contractor supply, we decide: do we segment managed services from the marketplace, or mix them? Is this customer-facing (they know they're using a marketplace), or just our internal model? That depends on quality, throughput, steady supply, and what customers will pay. We validate that with customers and prospects. Where is GrowthX in this process today?

**Marcel Santilli:** About 18 months ago we started hiring internationally for editors. We built workflows in our ATS where candidates complete assignments and fill out questions that we auto-vet. We have video recording systems that transcribe answers and rate them against role frameworks. We have a lot that can be repurposed.

The bottleneck: it's all downstream to human vetting—our best editors or head of content conducting final interviews. That's massive. If we move to contractors, we can't scale that human interview layer. We know how to vet full-time employees, but the bar for contractors is different: we don't care about cultural fit or AI-nativeness if someone has good taste, moves fast, and delivers quality. We do 500 pages a week—we have endless sample assignments to test with.

The real hard part: calibration. How do you take any human and run them through a system that identifies their strengths and promotes them? Judging content quality is hard—it's a whole machine learning field. We have Netflix content scientists on our hiring radar.

The other hard part: sustainable supply. People don't magically know to apply to you. You need existing supply channels (recruiting, marketplaces) or buy supply through ads and acquisition—which gets expensive fast. Data labeling companies solve this by using existing marketplaces, but it's a bait-and-switch dynamic.

The core challenge: finding supply sources and routing them through self-serve vetting at scale while incentivizing them. That's harder than ongoing management. Without supply or automated vetting, the whole thing breaks down.

**Suriya Sharma:** That's a super interesting problem with real challenges.

**Marcel Santilli:** Thank you. Bridget and I will debrief on our end. Great job all around.

**Suriya Sharma:** Thank you.

**Bridget McGillivray:** Thank you, Suriya. I appreciate the work.

**Marcel Santilli:** Talk soon.

**Suriya Sharma:** Bye.

**Bridget McGillivray:** Bye.
