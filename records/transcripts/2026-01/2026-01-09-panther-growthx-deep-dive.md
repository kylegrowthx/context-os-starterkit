# Panther <> GrowthX - Deep Dive

<metadata>
date: 2026-01-09
time: 18:00 UTC
duration: 61 minutes
organizer: kathy@growthx.ai
participants: Jack Naglieri (Panther), George Haikal (GrowthX), Dignory Carmona (GrowthX), Katie Campisi (Panther), Kathy Lam (GrowthX)
fathom_recording_id: 113154985
fathom_url: https://fathom.video/calls/525759144
share_url: https://fathom.video/share/ufrGZb_7xsm_futxG73veaGs5Rb3asoy
source: fathom
enriched_on: 2026-02-28T00:00:00Z
</metadata>

---

## Summary

Jack Naglieri and Katie Campisi from Panther presented their AI-centric platform repositioning to the GrowthX team, focusing on solving the alert fatigue crisis in modern security operations centers. The discussion covered Panther's AI SOC platform capabilities (alert triage, threat hunting, detection creation), demonstrated live product workflows, and aligned on a content strategy emphasizing pragmatic, technical, and transparent messaging for sophisticated security audiences.

---

## Context

Panther is in the midst of a significant strategic shift from a traditional SIEM competitor to an AI-native security platform. This meeting brought together Panther's product and content leaders with GrowthX's strategic team to establish a shared understanding of Panther's new positioning and develop a coherent content strategy for B2B audiences. The underlying business problem is urgent: security teams face an unsustainable alert fatigue crisis where they ignore 60% of alerts due to overwhelming data volumes, creating massive security blind spots and extending breach detection times (dwell time). Panther's answer is to automate the entire SOC lifecycle with AI agents that scale detection and response across petabytes of data while cutting costs by 50%+ versus legacy solutions.

GrowthX will use this context to develop thought leadership content that positions Panther as the pragmatic AI solution for teams moving away from both traditional SIEMs and managed security services.

---

## Relevance

- **Strategic positioning:** Panther's AI SOC platform narrative represents a significant market repositioning away from incremental SIEM improvements toward AI-first automation and cost efficiency.
- **Content strategy alignment:** The meeting established a clear, documented content voice (pragmatic, technical, transparent) and a proven content format (define concept → real-world examples → Panther solution → CTA) for GrowthX deliverables.
- **Competitive context:** Primary competitors (Google SecOps, CrowdStrike, Elastic, Splunk) lack Panther's AI-centric approach; secondary opportunity is teams leaving managed security services (e.g., Expel) or replacing homegrown tools.
- **Sales enablement:** Clear articulation of "aha moments" (alert triage agent, natural language co-pilot) and tangible ROI metrics (15–30 min → minutes for triage; ≥50% cost reduction) can be woven into all future content artifacts.
- **Product momentum:** Three near-term product updates (AI co-pilot rolling next week, formal March launch, new demo tabs) should be referenced in content to demonstrate continuous innovation.

---

## Overview

- **New AI-Centric Strategy:** Panther is repositioning as an "AI SOC platform" to solve the alert fatigue crisis, where security teams ignore 60% of alerts due to overwhelming data volumes (median: 4TB/day).
- **Core Value Prop:** The platform's AI agents compress triage time from 15–30 minutes to just minutes and cut costs by ≥50% versus legacy SIEMs, enabling teams to scale coverage without scaling headcount.
- **"Aha!" Moments:** The alert triage agent (auto-summaries, pivots) and natural language co-pilot (threat hunting, querying) are the key user workflows that demonstrate immediate value.
- **Content Strategy:** The voice must be pragmatic, technical, and transparent, using a proven format (define concept → real-world examples → weave in Panther as a solution) to build trust with a technical audience.

---

## Key Topics

### The Problem: A Broken SOC Model

  - **Alert Fatigue:** The core issue is that security teams cannot keep up with the volume of data and alerts.
      - **Data Volume:** Median enterprise log volume is 4TB/day, a scale legacy SIEMs struggle with.
      - **Result:** 60% of alerts are ignored, creating a massive security blind spot.
  - **Breach Costs:** Longer "dwell times" (time to detect/contain) directly increase the financial and reputational cost of a breach.

### The Solution: Panther's AI SOC Platform

  - **Core Capability:** Scalable detection and response across petabytes of log data.
  - **Key Differentiators:**
      - **Scalability:** Handles up to 100TB/day, with some customers processing multiple petabytes/month.
      - **Cost Efficiency:** Serverless architecture and data filtering cut costs by ≥50% vs. legacy SIEMs.
      - **AI-Driven Workflows:** AI agents automate tasks across the entire lifecycle.

### Product Demo: AI in Action

  - **Data Ingestion & Structuring:**
      - Ingests data from AWS, Azure, GCP, and webhooks.
      - Robust filtering drops non-security data to reduce cost and noise.
      - AI infers schemas from sample logs, simplifying onboarding.
  - **Detection Creation (AI Co-pilot):**
      - **Function:** Converts natural language into Python detection code.
      - **Status:** Rolling out to customers next week; formal launch in March.
      - **Significance:** Lowers the barrier to entry by reducing the need for direct Python knowledge.
  - **Alert Triage (AI SOC Analyst):**
      - **Function:** Automatically investigates and summarizes alerts.
      - **Process:** Enriches data, reads detection logic, and pivots to find related activity.
      - **Output:** A distilled summary with a risk judgment, visual flowchart, and actionable next steps.
  - **Threat Hunting & Querying (AI Co-pilot):**
      - **Function:** A full-screen chat interface for natural language queries.
      - **Capabilities:** Reporting, threat hunting, and querying all system data (pipelines, schemas, alerts).
      - **Significance:** Provides an intuitive abstraction layer over the entire SIEM, simplifying complex tasks.

### Content & Marketing Strategy

  - **Target Audience:** Sophisticated security teams seeking high automation and practical AI, not "turn-key" users.
  - **Competitive Landscape:**
      - **Primary:** Google SecOps, CrowdStrike, Elastic, Splunk.
      - **Secondary:** Teams offboarding from MDRs (e.g., Expel) or replacing homegrown tools.
  - **Content Voice & Tone:**
      - **Practical:** Rooted in real-world use cases and implementation details.
      - **Technical:** Speaks the language of engineers and CISOs without being opaque.
      - **Transparent:** Openly discusses capabilities, limits, and trade-offs of the technology.
  - **Effective Content Format (from Substack):**
    1.  **Define Concept:** Explain the topic in a security context.
    2.  **Provide Real Examples:** Show practical applications, weaving in Panther as a solution.
    3.  **Offer Actionable Advice:** Position the content as solving a problem.
    4.  **Include a CTA:** A soft ask to learn more about Panther's implementation.

---

## Action Items

**Jack Naglieri (Panther)**
- Send AI pitch deck + AI SOC demo materials to George/Kathy
- Update AI SOC deck: add Snowflake + Databricks to data lake slide
- Update AI SOC demo: add new tab for follow-on questions

**GrowthX (George, Kathy)**
- Ingest new Panther materials to inform content artifacts
- Adopt the defined content voice and format for all deliverables

---

## Transcript

George Haikal: Morning, how are you doing?
George Haikal: I'm good, how are you doing?
Kathy Lam: I'm good.
Kathy Lam: A little bit ahead of the last minute.
George Haikal: Change?
George Haikal: It's okay.
George Haikal: Get it done.
George Haikal: Get it done.
Katie Campisi: Morning, Katie.
Katie Campisi: Hey, how are you guys doing?
Kathy Lam: Great to see you again.
Katie Campisi: You too.
George Haikal: Is it morning for you, Katie?
George Haikal: Are you based on the West Coast as well?
Katie Campisi: Yep.
George Haikal: Nice.
Katie Campisi: Yeah, I'm in Portland.
George Haikal: Nice.
Kathy Lam: Is it, it's cold-ish here, but not that cold?
Katie Campisi: How is it there?
Katie Campisi: Yeah, would say, let's see, low 40s, south of the cold-ish.
Katie Campisi: I think for here, it's cold, but I grew up in Maine, so I feel like I'm not allowed to really call this cold.
George Haikal: No, yeah.
George Haikal: Yeah, grew up in Boston, so East Coast as well.
Katie Campisi: Yeah.
Katie Campisi: We're spoiled over here with the weather, I would say.
Katie Campisi: Yes.
Katie Campisi: I grew up in Maine, lived in Boston for 10 years, and then moved out here.
Katie Campisi: And a lot of it is, I hated snow by the time I left, so I just didn't want to deal with it.
George Haikal: How have you felt losing the seasons, though?
George Haikal: I go back and forth.
George Haikal: forth.
George Haikal: I still have really good seasons here.
George Haikal: I'll be honest.
Katie Campisi: I will say we only get like those true spring and fall days where it feels like it's like 65 and sunny and things are changing like a few times a season.
Katie Campisi: So when it happens, I enjoy it.
Katie Campisi: But there's definitely a more abrupt transition between summer and winter.
Katie Campisi: So those shoulder seasons you've got to take.
Katie Campisi: But we still get leaves change more than I expected.
Katie Campisi: Oh, nice.
Katie Campisi: Yeah.
George Haikal: How long have been in Portland?
Katie Campisi: Five years.
George Haikal: Nice.
George Haikal: Nice.
George Haikal: It's a good amount of time.
Katie Campisi: Yeah.
George Haikal: Hey, Jack, how's it going?
Jack Naglieri: Good.
Jack Naglieri: How are y'all doing?
George Haikal: Good.
George Haikal: Thanks for making it.
George Haikal: Good to meet you.
Jack Naglieri: Yeah, yeah.
Kathy Lam: Likewise.
Kathy Lam: Yes, super stoked.
George Haikal: Yeah, exactly.
George Haikal: Would it be helpful, Jack, if give a little context just on myself and Kathy?
George Haikal: know it's our first time meeting and then we can kind of hear a little bit more about you and then jump into our agenda for the day.
Jack Naglieri: Amen.
Jack Naglieri: Amen.
Jack Naglieri: Sure.
Jack Naglieri: Sounds good.
George Haikal: Amazing.
George Haikal: I'll just go very quickly.
George Haikal: We kicked off earlier this week with Katie and the rest of the team, so super excited.
George Haikal: Basically, what we're doing is building the engine, the content engine that helps Panther become the best answers to the questions, you know, your customers and your market are asking.
George Haikal: Those answers to the questions give you the best shot on goal for visibility and for traction clicks, impressions, and ultimately what matters, which is signups.
George Haikal: We know for Panther, from what we've heard, like we're solving for awareness first and foremost, more people knowing about the product because once they do, they love it and they recommend it.
George Haikal: And so that's kind of where we're coming from, but we're also extremely open-minded since this is our first week.
George Haikal: In the first two weeks, we just want to come in and become experts on the business and you all and the product and the perspective that you want Panther to have and the perception you wanted to have in the market.
George Haikal: And so as part of our process today, we kind of want to jump in and do a deep dive on the product and then also understand from all the work you've done on Substack.
George Haikal: Just like the expertise that's in your head about how you want to talk about the product, what to say, what not to say, what stands out, and then maybe like where the perception gap is now versus where you want it to be moving into the future.
George Haikal: So those nuances of your expertise will want to capture at the end after the product demo, and we'll have it flow pretty smoothly end-to-end.
George Haikal: That's kind of where we're coming from for this meeting.
Jack Naglieri: Okay.
Jack Naglieri: Yeah, you know, I'm happy to step you through some like new materials.
Jack Naglieri: So for context, we gave a talk yesterday at a partner, and it was very AI-centric in terms of like how we're positioning the company, and this is likely going to carry into our marketing.
Jack Naglieri: And it's still early, like we just had a strategy session yesterday to just lay out the first cut of this.
Jack Naglieri: But I'm pretty confident that the core message that I...
Jack Naglieri: So I can give you that.
Jack Naglieri: think that'll be really helpful context.
Jack Naglieri: can give you just kind of the latest on how we're thinking about the product for this year, because it's also related to that, obviously, because everything flows from that main strategy.
Jack Naglieri: And then I can show you the demo.
Jack Naglieri: That's also very AI focused.
Jack Naglieri: And in terms of like external perception, I might need to like get back to you on some, I mean, I'm sure we'll have multiple conversations, but I'll give you like my top top of mind.
Jack Naglieri: then I might have some other thoughts after the call if I like once it sits with me for a little bit, but I'm happy to give you a brain dump base, basically with everything I just said.
Jack Naglieri: I hope that that helps.
George Haikal: Love that.
Jack Naglieri: Love that.
Jack Naglieri: I'm sorry.
Jack Naglieri: I'm a little congested still.
Jack Naglieri: Had surgery like a month ago, not even a month ago.
Jack Naglieri: So my nose is like still.
Jack Naglieri: It sounds so stuffy.
George Haikal: Did you get a septum?
Jack Naglieri: Yeah, I had a septoplasty.
George Haikal: Nice.
George Haikal: How relieving is it?
George Haikal: I've heard.
George Haikal: Good things.
George Haikal: I had a good friend who just got one done, and he said, like, it's life-changing.
Jack Naglieri: It's really good.
Jack Naglieri: Yeah.
Jack Naglieri: It's a tough recovery.
Jack Naglieri: Like, it's the first few weeks were really brutal, but I'm on, like, week three, and next week will be my month.
Jack Naglieri: So, yeah, it's been good.
Jack Naglieri: I've had breathing problems my whole life, so it's nice.
George Haikal: For sleep and exercise, too.
George Haikal: I could, sorry, I could nerd out on that all day, and we can get back to the demo, but yeah, the benefits I've heard are amazing.
George Haikal: 100%.
George Haikal: Cool.
George Haikal: And Kathy, sorry, do you want to introduce yourself as well, since you're kind of, we'll be driving this?
Kathy Lam: Sorry.
Kathy Lam: Yeah, yeah, definitely.
Kathy Lam: So, yeah, nice to meet you.
Kathy Lam: I think prior to GrowthX, I worked on growth teams at developer for startups, and then actually very early in my career, I was on the product marketing team at ArcSight, so I'm familiar with the space.
Kathy Lam: So, I know we originally had our, I think, product lock.
Kathy Lam: about
Kathy Lam: Through kind of scheduled at the very end.
Kathy Lam: I was wondering if you might have time for us to like, we'll reverse the order and then maybe do the walkthrough first.
Kathy Lam: Or I'm very interested in hearing about like the new kind of messaging that you talked about like at the meeting yesterday.
Kathy Lam: So whichever you're more ready for, I'd love to dive into that and then we can go from there.
Kathy Lam: And then George, I, yeah, I don't know if you wanted to intro yourself.
George Haikal: No, no, it's all good.
Kathy Lam: We can jump in.
George Haikal: Yeah.
George Haikal: Whatever you want to start with, Jack, if it's the demo and you want to flow to the AI positioning and then the product forward looking for the year, we're happy to follow wherever you want to start.
Jack Naglieri: Yeah.
Jack Naglieri: I mean, I think that the natural flow is the pitch and then the product.
Kathy Lam: Yeah.
Jack Naglieri: Yeah.
Jack Naglieri: Just to like set the stage of like what we're doing and everything.
Jack Naglieri: Yep.
Jack Naglieri: Okay.
Jack Naglieri: Cool.
Jack Naglieri: Let's do that.
Jack Naglieri: Mm, mm, mm, mm, mm, mm, mm, mm, mm, mm,
George Haikal: And then just as a caveat, like the more materials you all can throw over the fence to us, the better.
George Haikal: do a ton of our own research, right?
George Haikal: But to get your style, your tone, your writing guidelines, the company context, right?
George Haikal: Like the more materials we can ingest and develop, the better our initial artifacts will be for the content.
Jack Naglieri: So we'd love to send any of this over the fence.
Jack Naglieri: Okay.
Jack Naglieri: I'm just thinking about what things I would want to share since it's still kind of early.
Jack Naglieri: Like the company hasn't even seen most of this yet.
Kathy Lam: And we can adjust like as things change, just send it over and then we'll update all of our artifacts.
Jack Naglieri: Sure.
Jack Naglieri: That sounds good.
Jack Naglieri: Cool.
Jack Naglieri: So, you know, the pitch really starts with the fact that the traditional SOC model is broken where there's a heavy reliance on humans.
Jack Naglieri: Throughout the entire process from end to end.
Jack Naglieri: And, you know, I think the biggest bottleneck that tends to happen.
Jack Naglieri: is around alerting.
Jack Naglieri: So the fact is there's just not enough humans to monitor all the different signals that need to be monitored to keep organizations secure in, you know, 2026.
Jack Naglieri: And a lot of this stems from the fact that data volumes have continually increased year over year for, you know, 15, 20 years.
Jack Naglieri: It's never going to stop.
Jack Naglieri: And AI is actually just going to make it worse because there's going to be a massive proliferation of new applications that come up.
Jack Naglieri: And just a massive growth of existing ones.
Jack Naglieri: So the, you know, the median log volume that enterprises see is around four terabytes of logs per day, which is growing each year.
Jack Naglieri: And four terabytes of logs per day was previously seen as like an impossible volume, you know, maybe 10 years ago for any sim.
Jack Naglieri: And now that's just the standard, you know, to really just go from zero to one in a lot of these big enterprises.
Jack Naglieri: But the, the problems sort of like flow downstream.
Jack Naglieri: So you have a massive influx of data.
Jack Naglieri: And signals that have to be monitored from that data, you have a massive amount of alerts as well that are related to certain behaviors that could indicate suspicious or, like, high-risk behavior that could lead to, you know, damage, it could lead to a potential breach, or, you know, something that could cause harm to the organization.
Jack Naglieri: And the fact of the matter is that we don't have enough eyes and time to look at all this signal, so what ends up happening is, you know, 60% of them get ignored.
Jack Naglieri: And, you know, there's a lot of devil in the details in cyber, and there's a lot of high nuance as well.
Jack Naglieri: So it just, the amount of time, it just doesn't work, like, the math doesn't work, ultimately.
Jack Naglieri: And, you know, this flows into the fact that breaches, you know, are continuously getting expensive, and they get more expensive the longer the dwell time.
Jack Naglieri: So as breaches continue over time, you know, the organization ends up paying disproportionate amounts of money and also reputation.
Jack Naglieri: So there's a lot of challenges that exist in the modern SOC model.
Jack Naglieri: And, you know, our perspective is similar to the rest of industry of where can we apply AI in strategic ways to alleviate these problems?
Jack Naglieri: So the way that Panther really approaches this problem is, you know, our core strength is in detection response across petabytes of log data.
Jack Naglieri: So we want to be the most scalable SIEM, and we want to alleviate all these issues with good technology choices, with AI agents, with code-based workflows, and highly structured data.
Jack Naglieri: We think that these decisions strategically position us as a product to alleviate a lot of these problems and flow these benefits downstream into security teams.
Jack Naglieri: So what we end up seeing, you know, with our platform, which we're, you know, we will be calling, you know, a complete AI SOC platform, where we apply AI across the entire lifecycle.
Jack Naglieri: Detection and response to alleviate these core problems.
Jack Naglieri: What we end up seeing is when you apply AI and techniques like streaming analysis, which is our predominant way of analyzing data, we see a massive, massive reduction of triage time.
Jack Naglieri: And this really helps compress that time from an event happening in your organization or in your production environments to actually having a decision on what to do next.
Jack Naglieri: So, you know, previously it would take maybe, you know, 15 to 30 minutes to even get the alert.
Jack Naglieri: And then it would take another 15 to 30 minutes to triage the alert.
Jack Naglieri: And now we can compress that down into a few minutes.
Jack Naglieri: So that's going to continue getting better over time.
Jack Naglieri: But the latency has always been something that we want to continually drive down.
Jack Naglieri: And that's made possible through AI agents and streaming analysis, which is our primary way of doing detection.
Jack Naglieri: The further, you know, downstream benefit as well is that we can actually take more data in because.
Jack Naglieri: Because of these decisions that we've made around our architecture.
Jack Naglieri: So Panther is extremely, extremely scalable.
Jack Naglieri: can handle, you know, upwards of 100 terabytes of log data per day.
Jack Naglieri: And, you know, on the high end, our customers are doing multiple petabytes of logs per month.
Jack Naglieri: And that benefit flows into alerting as well, where it means the security team can continually onboard more signals.
Jack Naglieri: And they can scale their volume without having to scale their headcount linearly.
Jack Naglieri: And a lot of that benefit also comes from the fact that we are heavily code driven.
Jack Naglieri: So the predominant nature of doing detection in Panther is using Python.
Jack Naglieri: But now with AI agents, you don't have to write the Python directly.
Jack Naglieri: just express what you want in natural language.
Jack Naglieri: It will write the detection.
Jack Naglieri: will tune it for you, et cetera.
Jack Naglieri: And I'll talk about how AI plays a role across this whole life cycle.
Jack Naglieri: But there's a ton of benefits with these decisions that we've made, allowing teams to have much higher throughput and scale.
Jack Naglieri: For, you know, the next five, 10 years.
Jack Naglieri: And then finally cost,
Jack Naglieri: Everything has to make sense economically.
Jack Naglieri: There's always a trade-off between where we invest in compute and agents and all these things, and compute cost is going to be a huge bottleneck going into the next 10 years with agents.
Jack Naglieri: So it always has to be top of mind.
Jack Naglieri: We always need to be building sustainable programs, but the decisions that we've made allow security teams, both in our technology and pricing model choices, to save at least 50% on what it costs them prior with legacy sim.
Jack Naglieri: And we just think that these sort of primitives around AI agents and serverless and these decisions that we've made have allowed our customers to have an unfair advantage against attackers.
Jack Naglieri: So that's kind of like the high level of kind of what we do and what the benefits end up being.
Jack Naglieri: And then before I just go into like the downstream of like the how, is there any context I can add on like the problem statement and the values?
George Haikal: No, like this, this is helpful, I guess, maybe just a little bit more on the personal side, like what inspired you to want to come and solve this problem?
George Haikal: Like, give me a little bit of the background, like leading up to Panther.
Jack Naglieri: Yeah, so before Panther, was a security analyst, security engineer, working in Silicon Valley tech companies for about eight years, maybe round up to 10, if I count like some work I did in college, but worked in cyber teams for, you know, the first half of my career.
Jack Naglieri: And then during the time at Yahoo, which is where, you know, I went to work out of college, we just kept finding that the tools available for us at our scale never worked.
Jack Naglieri: And it required us to build a lot of scaffolding around the tools.
Jack Naglieri: And when we went to, when I joined Airbnb, it was really the same type of thing where we didn't want to just roll a traditional.
Jack Naglieri: Because we knew it would be too expensive, too slow, too limited in terms of its detection capability and automation capabilities.
Jack Naglieri: So we decided to build our own, which isn't always the best decision, obviously.
Jack Naglieri: But it did work out really well for us because we open sourced the project and it became widely adopted in the community.
Jack Naglieri: And those primitives really were the precursor into what Panther is now.
Jack Naglieri: And obviously, Panther is like the enterprise version.
Jack Naglieri: And it's used by even more companies, very similar to the ones that had adopted StreamAlert, which was the open source project.
Jack Naglieri: So that's kind of like the brief history of it.
Jack Naglieri: It was just more of like feeling that problem as a practitioner and then wanting to really think from first principles how to address the problem.
Jack Naglieri: And then now with AI, it's like the evolution of that.
Jack Naglieri: We're kind of in our like second wave of our product.
Jack Naglieri: So it's pretty exciting.
George Haikal: Yeah, that's amazing.
Jack Naglieri: Such an exciting time.
Jack Naglieri: Yeah.
Kathy Lam: I have one follow-up to that.
Kathy Lam: Are a lot of Panther customers...
Kathy Lam: There's folks who are using the open source and decide, like, they actually need a lot more of the enterprise features and they upgrade, or how do they find you now?
Jack Naglieri: No, it's not open core.
Jack Naglieri: I mean, we moved away from that model a very long time ago, but we did start.
Jack Naglieri: We started closed source.
Jack Naglieri: We had an open source community edition for about a year.
Jack Naglieri: We deprecated it in favor of enterprise, and that was a good decision.
Jack Naglieri: Open core models are just really hard to build a good business around.
Jack Naglieri: Yeah.
Jack Naglieri: So most of our awareness has been teams that are looking for the type of solution that we provide, which is, you know, the code-based workflows, data lake, AI agents.
Jack Naglieri: You know, AI agents is becoming the predominant reason that companies will buy Panther.
Jack Naglieri: It's a reason that we often hear during POC is...
Jack Naglieri: ...
Jack Naglieri: ...
Jack Naglieri: Is leading the pack across our competitors.
Jack Naglieri: So we're, you know, working really hard to maintain that and, you know, to deliver the best AI experience that we can, right?
Jack Naglieri: I don't like to ever position us directly against a competitor because I think that looking within and looking at your customer base is just a stronger position than trying to just beat out a competitor on their own product.
Jack Naglieri: But we've done an exceptional job of pursuing AI and listening to our customers and just making fast decisions.
Jack Naglieri: So I think that's been a big contributing factor to our success.
George Haikal: And then along those lines, when you're talking about listening to the customer and really solving for them, what are the, we heard something during the kickoff call, but like, tell me some language that customers are, that you're hearing from customers when they're switching to Panther or choosing Panther.
George Haikal: Like, what are some of those trigger moments that they're in from the words that you've heard and the language that they've used?
Jack Naglieri: feel like Katie would be able to answer that better than me, to be honest, because you often like relay a lot of that through the website and socials and stuff.
Jack Naglieri: So I'll let her get the context.
Katie Campisi: Yeah.
Katie Campisi: I mean, I know that we talked about this Monday.
Katie Campisi: I think what we talked about with it's not it's not just high cost.
Katie Campisi: There's also something that's happened that's prompted them to feel like they need better coverage.
Katie Campisi: So we have like first them people.
Katie Campisi: It's more their customer base or their team.
Katie Campisi: There's a need as they scale to need a true security tool and a SIM and compliance and all of that.
Katie Campisi: And then we have the larger teams who maybe they've they're feeling the growing pains of the tools they're on.
Katie Campisi: It's not flexible enough.
Katie Campisi: They are drowning in alerts.
Katie Campisi: They don't know how to filter them or they don't have the tools they need to filter them.
Katie Campisi: And they just don't feel unable to actually catch threats that they they know they're missing or they suspect that they're missing.
George Haikal: That's helpful.
George Haikal: That's helpful.
George Haikal: That's helpful.
George Haikal: Good to move towards the AI positioning.
George Haikal: Yeah.
Jack Naglieri: So we talked about the what we do, the benefits, and this is really the how.
Jack Naglieri: So Panther spans four key areas of detection and response today, and each one of them is complemented by AI in a slightly different way.
Jack Naglieri: But the whole idea is that we want to apply AI agents across this entire lifecycle to make the entire system smarter.
Jack Naglieri: And we're seeing really great success so far in our AI SOC analyst, which was the first agent that we had introduced.
Jack Naglieri: So all data in Panther is highly structured, and that's by design to enable the detectionist code, to enable the data lake, and now it's actually a massive benefit with AI agents.
Jack Naglieri: So we highly structure all the data coming in.
Jack Naglieri: Teams can filter, they can drop, they can do a lot of various ETL and...
Jack Naglieri: You know, data filtering type of work there.
Jack Naglieri: It's quite robust.
Jack Naglieri: think it's actually pretty underrated in terms of our platform.
Jack Naglieri: But once all the data gets structured, it gets put into a data lake.
Jack Naglieri: I'm showing the data lake here as Databricks because that was a presentation that I just gave.
Jack Naglieri: But it can actually be Databricks or Snowflake.
Jack Naglieri: So I need to have an updated version of the slide that sort of shows either or.
Jack Naglieri: And the next step of this process is detection.
Jack Naglieri: So we have a pretty robust detection correlation engine.
Jack Naglieri: It allows teams to declare various types of attacker techniques and tactics.
Jack Naglieri: So, for example, we can do more trivial detection that's looking at just certain patterns and logs.
Jack Naglieri: That's very low latency.
Jack Naglieri: We can do batch-based analysis, which looks backwards in time and does interesting aggregates and anomaly detection.
Jack Naglieri: And then we can do correlations as well where we're looking at sequences and batches of activity.
Jack Naglieri: So there's a lot of different ways to model the behaviors that are very important for an organization.
Jack Naglieri: And then on the right side of that is alerting.
Jack Naglieri: So this is once the detection engine has detected something that's relevant and important and urgent, it will create an alert.
Jack Naglieri: will page your team through whatever means you typically use.
Jack Naglieri: And then we actually now use AI in the middle of that.
Jack Naglieri: So what happens is we're building towards a path where we have an autonomous AI SOC analyst that will look at every single alert and will only truly escalate the things that are risky or inconclusive for your security team to take a look at.
Jack Naglieri: And that removes a massive amount of just sort of like baseline noise that is always happening.
Jack Naglieri: And that might be things like repetitive alerts.
Jack Naglieri: It could be something that was an engineer making a benign change.
Jack Naglieri: But the fact is that we can actually increase our coverage to 100%.
Jack Naglieri: So, you know, we're not ignoring half of the alerts anymore.
Jack Naglieri: And then it gives the security team a lot of breathing room to focus on the whole system and making sure.
Jack Naglieri: Making that we're getting the right data, that we're giving the AI agents the right context, and we're creating more detections and more signal for the AI to continue to analyze.
Jack Naglieri: So that's a really exciting part of the platform that we have today.
Jack Naglieri: I forgot to mention, on detection, we're introducing a detection engineer, detection writer agent very soon, and that will allow security teams to interact with the detections in natural language.
Jack Naglieri: So they can say, like, hey, I want to create a rule for anytime someone's logging into Okta from, you know, not a US or Europe country, and, you know, they have, like, five or more failed logins or something, right?
Jack Naglieri: You can express that just with natural language, it will create the detection, and then you can refine it as well, once you see certain alerts.
Jack Naglieri: But we want to make this loop more automated over time, and that's what we're planning to do.
Jack Naglieri: The final piece is really around the data at rest, so because everything is highly structured.
Jack Naglieri: It is very easily queryable, and we really think that where it's going is, you know, like a ChatGPT style of exploration of the data, where you're not doing it directly, you're just expressing what you're looking for, and the agent will go write all the queries for you, it will synthesize all the results, and then you can sort of steer the agent where to go next.
Jack Naglieri: But we do give direct access into the data through a pipe-based query language.
Jack Naglieri: So, yeah, this is in a nutshell, you know, how we express our AI SOC platform.
Jack Naglieri: We give security teams these four core parts of the system.
Jack Naglieri: We augment each of them with AI, and we connect them all together with AI as well.
Jack Naglieri: So, what the AI SOC analyst does on the alerting layer is transferable knowledge into the detection layer, which gets transferred into the co-pilot.
Jack Naglieri: Like, they're all able to access this, like, shared sort of synthesized learning.
Jack Naglieri: And that's really what makes
Jack Naglieri: It the product really strong and it's what customers are gravitating towards.
George Haikal: Love it.
George Haikal: Love it.
Jack Naglieri: This is very helpful.
Jack Naglieri: Mm-hmm.
Jack Naglieri: So that's, I mean, I can, we can, like, go transition into product and can show you what these things look like firsthand.
Jack Naglieri: Good.
Jack Naglieri: All right.
Jack Naglieri: Cool.
Jack Naglieri: So there's a lot of various ways of getting data into our system.
Jack Naglieri: So the the core part of any security program, you know, you're only as good as what you can see and the context that you have.
Jack Naglieri: So we can ingest data through a number of different means.
Jack Naglieri: Any of the hyperscalers, you know, Google, Azure, AWS, you can also send logs directly to us through a webhook.
Jack Naglieri: And then once the logs hit Panther, you have the option of adding filters either on the raw events or post-normalization.
Jack Naglieri: We all
Jack Naglieri: We have some pretty interesting features around testing the filters, so if there's a particular set of data that you don't have control over and you think isn't security relevant, you can actually express these filters and then you can run tests and actually want to make sure I'm logged in, yep, I'm not logged in, whoops.
Jack Naglieri: Classic.
Jack Naglieri: I thought I was logged into this instance, my bad.
George Haikal: We're building our own AI visibility tool that's in private beta right now, and so when I'm demoing it to some of our custom clients, same thing, it's like the logged in or logged out experience, make sure everything's buttoned up for the demo.
Jack Naglieri: It just means we have high security.
George Haikal: That's all that means.
Jack Naglieri: Got it, yeah, yeah.
Jack Naglieri: So, yeah, the filtering is really robust.
Jack Naglieri: You can enable to seeable filters.
Jack Naglieri: You have a lot of flexibility in how to drop data, and this has a lot of downstream benefits around speed and cost.
Jack Naglieri: So, you're not paying for data that isn't security relevant.
Jack Naglieri: So, we find that that's a very helpful feature for customers.
Jack Naglieri: All data...
Jack Naglieri: It's highly structured, like I mentioned.
Jack Naglieri: We follow a schema model that we built ourselves, but it's based on common parsers for things like CSV, JSON, et cetera.
Jack Naglieri: And then customers can see the data, the fields, the description of the fields.
Jack Naglieri: And then we also have a field discovery feature where if the schema changes in drifts over time, Panther will automatically adapt to that schema, and then you will be able to search all of that data.
Jack Naglieri: So we've done a lot in this area.
Jack Naglieri: And we've also done a lot on schema inference as well.
Jack Naglieri: So you can upload sample logs.
Jack Naglieri: It will generate those schemas for you using AI, and then you can save and apply it to your sections.
Jack Naglieri: let me just pull a random one.
Jack Naglieri: Let's do this one.
Jack Naglieri: So this was a schema that I uploaded and used AI to create.
Jack Naglieri: And you can create custom parsing logic here as well, which is what this did.
Jack Naglieri: So it's pretty extensive.
Jack Naglieri: I didn't write any of this.
Jack Naglieri: Our AI agent did it you.
Jack Naglieri: So pretty good.
Jack Naglieri: And yeah, this is the jump off point for everything else that we'll do in the system.
George Haikal: Love that.
Jack Naglieri: Cool.
Jack Naglieri: So transitioning into detection.
Jack Naglieri: So once you have data, the next logical step is signal.
Jack Naglieri: We want to be able to understand and model out what threats are important to customers.
Jack Naglieri: And we have a number of built-in detections as well.
Jack Naglieri: So if I just click out to the detections list, we can see all of the enabled detections.
Jack Naglieri: can filter by the various log types.
Jack Naglieri: We can get a quick trend line of which things have been triggering alerts.
Jack Naglieri: And we're able to just filter and drill down based on things like severity, log type, et cetera.
Jack Naglieri: If we want to create custom detections, we have various ways of doing that, which I mentioned in the overview.
Jack Naglieri: The most popular one.
Jack Naglieri: One is Python or our simple detection, and those are very low-latency streaming rules, and we'll use that as the demo here today.
Jack Naglieri: But the way that they work is really around, like, atomic-based analysis, so looking at, like, one particular attacker or tactic, something that is highly urgent, highly important that we want to get an alert on right away.
Jack Naglieri: Got it.
Jack Naglieri: We're rolling a co-pilot as well, and we're probably going to, we actually need to rename how we're talking about our AI for what it's worth.
Jack Naglieri: We actually want to move away from co-pilot because it's too synonymous with security co-pilot.
Jack Naglieri: Like, if I type AI co-pilot, there you go.
Jack Naglieri: Exactly.
Jack Naglieri: And I don't think we're going to out SEO Microsoft, so probably need to change it.
Jack Naglieri: So we were chatting about that last night.
Jack Naglieri: But the way that this works is instead of needing to write all of the Python code and fill out all the fields,
Jack Naglieri: It's directly, you just express what you want in natural language.
Jack Naglieri: So I said, you know, create a tech share when someone deletes a bucket in USC1 from a normal AWS account.
George Haikal: Got it.
George Haikal: this is solving for the gap, I think, Katie, you mentioned on the call Monday where you don't need to use Python anymore.
George Haikal: You won't need to.
George Haikal: When will this be available?
Katie Campisi: Or is it already available?
Katie Campisi: We're aiming for March.
George Haikal: Oh, God.
George Haikal: No, this is going out in the next release.
Katie Campisi: Oh, that's right.
Jack Naglieri: The formal launch will be March.
George Haikal: Yeah, yeah.
George Haikal: You're right.
Jack Naglieri: You're right.
Jack Naglieri: But yeah, this will go out to customers next week.
Jack Naglieri: I don't know.
Jack Naglieri: I don't know if we can say you don't need to know Python yet.
Jack Naglieri: I mean, I think if you blindly trust what we give you, I mean, it is right and it is tested.
Jack Naglieri: But you still need to, like, approve it.
Jack Naglieri: Yeah.
George Haikal: So I don't know.
Jack Naglieri: Approve it, approve it, yeah.
Jack Naglieri: I think if we wanted to say it, I'd be comfortable.
Jack Naglieri: But we are going to still show it, so it isn't completely abstracted away.
Jack Naglieri: I think if we were able to have this workflow in the Simple Detection Builder, then I would say 100% you can not need to know Python at all.
Jack Naglieri: But we do have this capability today where you can create rules that are non-Pythonic.
Jack Naglieri: But yeah, this certainly streamlines the process.
Jack Naglieri: It also pulls real logs and writes the test for you.
Jack Naglieri: So pretty strong.
Jack Naglieri: I don't know why it made it critical.
George Haikal: That's kind of overkill.
Kathy Lam: I'm curious, day to day, would the analysts be looking at the detection alert screen, or will they mostly be in here, like configuring?
Kathy Lam: Or like, on a good day, they're not even in here, and they're only responding to alerts that the AI agent could...
Kathy Lam: ...
Kathy Lam: ...
Jack Naglieri: ...
Jack Naglieri: ...
Jack Naglieri: Yeah, well, think it depends a little on the role of that person.
Jack Naglieri: So a security engineer is more likely to be on the detection layer and maybe like the automation layer, whereas analysts will be more so on like the alert queue and using agents to really like triage, which I'm about to show.
Jack Naglieri: So maybe I can progress into that.
Jack Naglieri: But yeah, the detection, you know, AI agent for detection, whatever we end up calling it, is super helpful for creating those detections.
Jack Naglieri: And then we get alerts about those detections.
Jack Naglieri: So we use AI to autonomously respond to these alerts.
Jack Naglieri: And what you end up getting is a really nice summary of really everything that happened related to this behavior and things that are highly related to that.
Jack Naglieri: So it's very uncommon that an attacker just does one thing.
Jack Naglieri: When you get an alert, it's kind of...
Jack Naglieri: A canary in the coal mine, so to say.
Jack Naglieri: So we want to use our agent to do all that context building and synthesis and reporting.
Jack Naglieri: So then what the analyst gets is a distilled summary, a judgment, and then they can make the next call based on their own intuition and context of what they know about the company.
Jack Naglieri: So this alert specifically is me going through and changing an alert destination severity routing.
Jack Naglieri: So that basically just means I updated a alert destination to where it won't get alerts anymore.
Jack Naglieri: And this could be indicative of someone as a malicious insider.
Jack Naglieri: It could be someone who gained access to the sim and wants to effectively disable defenses.
Jack Naglieri: So we have agents that are running on all of these alerts.
Jack Naglieri: And the way that it effectively works is it will use all the data and tools in Panther as disposal.
Jack Naglieri: So it will do things like getting enrichments on IPs.
Jack Naglieri: It will do
Jack Naglieri: Things like reading the detection logic, will look at alerts around the time of this detection, and then it will do things like writing pivot queries to look at Jack's, you know, administrative actions around the alert time.
Jack Naglieri: So this is looking at, let's see, what was the time?
Jack Naglieri: It was at 20.
Jack Naglieri: So this is about a 30-minute buffer around, and then we're annotating exactly why it's pivoting, which is really, really helpful.
Jack Naglieri: So this one is looking at a related behavior that was detected around that same time because we are looking at the other alerts.
George Haikal: So this found two related alerts.
Jack Naglieri: And then what we ended up getting is this, like, synthesis of what it found.
Jack Naglieri: So it gives me who I am.
Jack Naglieri: So I'm the CTO founder.
Jack Naglieri: I did a certain behavior, and then that is dictated as risky.
Jack Naglieri: And it's dictated as risky because we have certain evidence that was collected.
Jack Naglieri: So it's looking at things like the enrichments, it's looking at my behavior around that time, and then it's calculating a score that goes into that final judgment.
Jack Naglieri: And then we try to elevate the most important aspects of this behavior to our security analysts that are using our platform.
Jack Naglieri: And we keep it as like a three to five bullet summary.
Jack Naglieri: We explain, you know, what happened around the same time.
Jack Naglieri: We give a really nice visual flowchart of that behavior as well.
Jack Naglieri: Which is really helpful.
Jack Naglieri: think humans are very visual, obviously.
Jack Naglieri: And we don't really look at like lists of data very efficiently.
Jack Naglieri: So it can be really nice to see things visually.
Jack Naglieri: And then we get a set of next steps ultimately that we should be taking.
Jack Naglieri: So, you know, fix the configuration changes.
Jack Naglieri: Look at the deleted log source.
Jack Naglieri: Look at the alerts that were created around at the same time.
Jack Naglieri: Like these are actually really amazing suggestions on what to do next.
Jack Naglieri: And then I would take some action.
Jack Naglieri: Bye.
Jack Naglieri: Bye.
Jack Naglieri: So I would maybe reset Jack's account, would go change things back, et cetera.
Jack Naglieri: So it gives, it just saves a massive amount of time then needing to build all that context up.
George Haikal: And it does a very good job of doing these pivots.
Jack Naglieri: No, that's amazing.
George Haikal: Yeah.
George Haikal: That's amazing.
Jack Naglieri: Very impressive.
George Haikal: Thanks.
Kathy Lam: Is this probably where the aha moment is for, like, the main user for Panther?
Kathy Lam: Or is it the ability to quickly create the detection rules?
Kathy Lam: Like, which, like, if there's, like, one thing where, as they're onboarding and as they're, like, seeing Panther work.
Kathy Lam: But what is the aha moment?
Jack Naglieri: I think the aha moment is a combination of this workflow and the next workflow I'm going to show you.
Jack Naglieri: Okay.
Kathy Lam: Yeah.
George Haikal: Sorry for constantly.
George Haikal: No, it's blowing perfectly.
Jack Naglieri: great.
Jack Naglieri: It's okay.
Jack Naglieri: It's a good, it's a, you teed me up.
Jack Naglieri: Okay.
Jack Naglieri: The thing about the alert triage is it's probably the most frequent workflow in a sim because detections you only really need to do on a semi-infrequent basis, right?
Jack Naglieri: Because your threat models don't change very often, but the activity that's detected is every single hour, minute, et cetera, right?
Jack Naglieri: So this workflow is the most common, probably at par with search, which is the next thing that I wanted to show.
Jack Naglieri: So I just glazed it over in Richmond, so I don't think we need to necessarily talk about that.
Jack Naglieri: But we're calling our full-screen copilot.
Jack Naglieri: Again, we have to change the name of this, but we have a full-screen chat, effectively, where security teams can, just using natural language, can ask about any part of the system.
Jack Naglieri: And that was, you know, an important thing.
Jack Naglieri: Note of this AI co-pilot right here.
Jack Naglieri: So the co-pilot is useful for things like reporting.
Jack Naglieri: It's really great for threat hunting, which is what we're doing here.
Jack Naglieri: It's really great for querying data and having the agent go and answer questions about various data throughout your system.
Jack Naglieri: And what we're doing here is we're actually asking a follow-on question about that alert.
Jack Naglieri: We can do this in the context of the alert as well.
Jack Naglieri: So if we wanted to ask very specifically about that activity, I could ask a follow-on question, say, hey, like, for example, let's actually just do that.
Jack Naglieri: We'll do a live demo.
Jack Naglieri: Jack have a history of making changes to the site alert destination.
Jack Naglieri: Look back, you know, three, six months.
Jack Naglieri: So I can ask follow-on questions that kind of nudge the AI in the right direction, and I need to always incorporate this in my demo as a side note.
Jack Naglieri: I need to have a new tab for this.
Jack Naglieri: But it's a really important part of this workflow because the agent isn't going to know everything.
Jack Naglieri: It's only going to know the context and logs that are given to it.
Jack Naglieri: And as humans, we understand the people, process, and technology of the whole organization.
Jack Naglieri: So what we can do is we can kind of nudge the AI in the right direction, and it will self-correct itself in a lot of ways.
Jack Naglieri: So what it's doing right now is it's investigating my question, and it's going to write additional queries to try to answer what it is that I'm looking for.
Jack Naglieri: So it looks like it is finding a repeat of behavior because this is the demo that I do a lot.
Jack Naglieri: it should say, yeah, that's great.
Jack Naglieri: Actually, you know, it's kind of a funny side note.
Jack Naglieri: It's like AI agents make demos really hard because they're so good at understanding things like patterns.
Jack Naglieri: So it can often pick up that it's testing.
Jack Naglieri: Like I'm testing something, but I'm trying to create a real scenario.
Jack Naglieri: So anyway, it's just like a fun.
Jack Naglieri: Let side note, but yeah, this picked up rightfully that I have a history of modifying the destinations, and let's see what else it's saying, nearly identical pattern in October, yep, that's when I did it last, infrequent testing, anomalous email address detected, that's really interesting and correct, this was a email that I, it's like a throwaway junk email that I created in the past.
Jack Naglieri: Yeah, it's finding all the right things, which is great, and yes, Jack has the document history, and then I could ask it to like reincorporate this back into the main, into the main analysis, so like rerun, refinal analysis, this call, sorry, I can do that.
Jack Naglieri: So anyway, there's, there's that way of interacting in a chat based scenario, but if I wanted to zoom out even further, and look at the broad scope of the system.
Jack Naglieri: Or ask like an unrelated question, we have our AI co-pilot that is great for this.
Jack Naglieri: And this co-pilot has access to the entire sim from the data pipeline, the schemas, the detections, the alerts, the data itself, it can access everything.
Jack Naglieri: So I ask a question, know, on January 6th, Jack triggered two alerts, can you check for any deviations against his baseline around that time?
Jack Naglieri: And this can then can help identify if there's other sort of ancillary behaviors that weren't detected that we need to take some action on.
Jack Naglieri: So this is a really important data point for any sort of incident responder, but it looks at our baselines, which is a new feature that we rolled out in one of the previous releases.
Jack Naglieri: And the baselines help establish what normal means for a particular type of behavior.
Jack Naglieri: So I'm looking at Okta because Okta is the focal point of most organizations when it comes to access.
Jack Naglieri: And this data point can just kind of...
Jack Naglieri: Give me assurance that what we saw wasn't a deviation so it makes it more benign.
Jack Naglieri: So it's really helpful context and again it didn't require me doing any sort of searching through the system.
Jack Naglieri: It did a query against the the baselines with my email.
Jack Naglieri: I can click in and see what it found which is great.
Jack Naglieri: It did additional SQL queries as well to look at my activity in Okta around that time and did some other sort of searches that it felt were relevant.
Jack Naglieri: So yeah, this this workflow is one of the key aha moments as well because I think a lot of security teams are going to be moving towards this workflow of interacting with the sim because it alleviates the entire learning curve of all the components that we've built and it adds such an amazing abstraction over everything.
George Haikal: I love it.
Jack Naglieri: Yep.
Jack Naglieri: So that's detection, source's last bit is really just interacting with the data, and we're rolling a new natural language to Panther Flow feature very soon.
Jack Naglieri: So Panther Flow is our pipe-based queer language, very similar to Splunk's queer language and others in the market, and this will allow teams to just really quickly get to an answer of what they need without needing to learn the language.
Jack Naglieri: They can obviously accomplish this through the chat, as I just mentioned, but this workflow is really, really helpful if you want to create persistent dashboards and searches that you come back to.
Jack Naglieri: So in this particular example, I'm looking at Okta, I'm saying, you know, give me a summary of Jack's Okta activity on JN6, which is very similar to what we're looking at, and then we can sort of like dive through the data itself.
Jack Naglieri: We can also create visualizations that end up landing in these dashboards.
Jack Naglieri: So these dashboards are all backed by that same pipe-based data.
Jack Naglieri: language.
Jack Naglieri: And you can add filters across all the dashboards.
Jack Naglieri: And this can kind of be like a kind of like a mission control high level visual of this is looking at all the signals.
Jack Naglieri: things that may have generated alerts or things that are kind of happening in the background.
George Haikal: What does this might be jumping around, but it's definitely related to how useful all this information would be to a user.
George Haikal: Like what does onboarding look like for the product?
Jack Naglieri: So onboarding starts in data onboarding here.
Jack Naglieri: So back at log sources.
Jack Naglieri: then there's likely a pretty early workflow of connecting to the identity provider.
Jack Naglieri: So hooking the other up to Okta, for example, would be a really core workflow.
Jack Naglieri: And then turning the detections on.
Jack Naglieri: And I think the detection enablement is really based on the appetite of the team.
Jack Naglieri: We're rapidly evolving how detections are like the mechanics of detections, but prior we would have required teams to create a GitHub.
Jack Naglieri: Repo, create a fork of our open source rules, which we have just openly available in GitHub right here.
Jack Naglieri: And this is actually my own fork of it, but we'll go to the main one.
Jack Naglieri: And this has all of the built-in content and the detection logic, the queries, policies, etc.
Jack Naglieri: And then customers would decide, like, which ones are relevant for their threat models.
Jack Naglieri: They would turn those on, would onboard more data, would set up more enrichments.
Jack Naglieri: And, you know, it really requires, like, high context, right?
Jack Naglieri: Like, any security operations center has to be high context for it to be successful.
Kathy Lam: Is that the friction point?
Kathy Lam: Or was there, like, another friction point which made it more difficult for, like, new, like, for customers who didn't have SINs before to adopt Panther like this?
Jack Naglieri: So this isn't required.
Jack Naglieri: it's...
Jack Naglieri: um...
Jack Naglieri: All the rules come prepackaged in the system, but for the teams that want to declare everything as code, they would go through the GitHub workflow.
Jack Naglieri: There might even be a way for us to, I mean, I haven't tested this yet, but there's likely a way to just enable or disable the rules that you want using the code pilot.
Jack Naglieri: Yeah.
Jack Naglieri: I mean, it's certainly possible to do.
Jack Naglieri: I haven't gone through it, so I don't know how good it is, but yeah, it's not an area that we've invested in yet, because we're working on the mechanics of detection, so how they're enabled, how they're overridden and customized.
Jack Naglieri: So I think once that's in a stable state, then we'll think about what the AI-based workflow is, but it's a good question for sure.
George Haikal: Got it.
George Haikal: Makes sense.
George Haikal: That was great.
George Haikal: was wildly informative and helpful.
Jack Naglieri: Yeah.
Jack Naglieri: Yeah.
Jack Naglieri: I'm glad.
Jack Naglieri: Thanks.
Jack Naglieri: What else can we chat through?
Jack Naglieri: So we have about 15 minutes.
Jack Naglieri: What's the most useful context that I can provide for you all?
Kathy Lam: Maybe, I guess, one question is around, like, when a buyer is, like, looking at you guys, who are they comparing you against, usually?
Jack Naglieri: Yeah, that's a...
Jack Naglieri: I would say there's probably, like, five companies that come to mind here.
Jack Naglieri: It depends a little bit on where that security team is in their maturity.
Jack Naglieri: So what I mean is, like, sometimes security teams are onboarding, or they're offboarding from an MDR, like Expel.
Jack Naglieri: So there's, like, that flavor of customer where they're saying, okay, well, I want to bring this in-house, but I'm pulling away from, you know, an Expel or a similar.
Jack Naglieri: I
Jack Naglieri: think that's probably not extremely common for us, but it is one way that a customer would find Panther.
Jack Naglieri: I think Katie alluded to it as first sim.
Jack Naglieri: So typically they are coming from an MDR versus from nothing completely.
Jack Naglieri: The more common one that we would compete against is Google SecOps, that ecosystem, CrowdStrike, their ecosystem, Elastic, Splunk, the sort of like previous gen of sim.
Jack Naglieri: And I think it's really those four.
Jack Naglieri: I think we don't come up against Palo Alto very often.
Jack Naglieri: We don't come up against the pure sim players very often, like Exabean, Logarithm.
Jack Naglieri: It's not really the same type of buyer because the type of buyer that would get a sim like that, they don't, they just kind of want something to turn on versus like really build on.
Jack Naglieri: And our customers are really...
Jack Naglieri: Intentional about their security operations.
Jack Naglieri: And they want really high automation.
Jack Naglieri: They want to apply AI everywhere in a way that's very practical and useful.
Jack Naglieri: So that tends to be the dynamic that we see.
Jack Naglieri: And I don't know, Katie, if have anything that I missed that you wanted to add around competitive.
Katie Campisi: Thank you, Neal.
Jack Naglieri: Cool.
Jack Naglieri: And then there's homegrown.
Jack Naglieri: Sometimes teams have their own version of the sim that they build on top of the data lake or some other things like that.
Jack Naglieri: But, you know, those don't survive because, you know, the average 10 years is probably like two years of a security person.
George Haikal: So it's just generally a bad strategy to build your own.
George Haikal: Yeah.
Kathy Lam: Is it right to say that I think more sophisticated security teams are looking at you guys?
Kathy Lam: And the previous ones were just people who bought, like, sims off the shelf.
Kathy Lam: But here they really want to, like, customize it according to what they're doing in their scale.
Kathy Lam: I think I'm going to take a quick tangent and go, like, when you're reading, like, other marketing and there's something that, like, makes you get high from it, like, what makes you instantly, like, distrust something besides it being, feeling a little marketing?
Jack Naglieri: I would say no second-order thinking or depth, because a lot of security marketing is just , right?
Jack Naglieri: It's just like, oh, we're using AI everywhere, and, like, they don't actually talk about the impact of it or how it works or, like, real problems that security teams have.
Jack Naglieri: And that was always my problem with security vendors and their marketing.
Jack Naglieri: It's just always very fluffy and, like, lacked any substance.
Jack Naglieri: And I think as much as we can take, like, a pragmatic, technical approach, you know, of the right altitude, obviously, I think that's what makes people trust us.
Kathy Lam: Got it.
Kathy Lam: And when you say, like, content isn't deep enough, besides the fact that it's not first-order thinking, like, what's missing?
Kathy Lam: And then also, like, when you've read something where you've thought, like, hey, this was written by someone who's done the work, what is in that?
Jack Naglieri: I think it's just rooted in, like, practical use case.
Jack Naglieri: I just think a lot of the content I've read is just, like, I would read it and be like, okay, you didn't tell me anything that's interesting, novel, or even technical, you know?
Jack Naglieri: And, you know, my background is very technical, and, like, that's kind of where I trend.
Jack Naglieri: But it even applies to the leadership level, too.
Jack Naglieri: It's like, what are the benefits I'm getting from this?
Jack Naglieri: How can you back those benefits up?
Jack Naglieri: It's really just, like, being able to justify what you're saying in a particular way is really what I mean, you know?
Jack Naglieri: It doesn't always have to be down at the code level, but if we think about...
Jack Naglieri: But who our core champions are, they are technical people.
Jack Naglieri: And it's like what you said, like it's the type of person that wants to really get in and understand things.
Jack Naglieri: And as much as we can speak that language to them, I think we'll be successful in landing the right message to them.
Jack Naglieri: So, for example, if we're going to talk about AI agents, we should show them what it looks like and what its limits and capabilities are.
Jack Naglieri: like, transparency is a really key part of that, like showing the tradeoff.
Jack Naglieri: Like, hey, like AI is good at these things.
Jack Naglieri: It's bad at these things.
Jack Naglieri: So this is how you would bridge that gap.
Jack Naglieri: And here's like an actual example of that.
Jack Naglieri: Those are the types of things I think people would respect, right?
Jack Naglieri: They don't want to be sold to.
Jack Naglieri: I mean, obviously, like no one wants to be truly sold to in any context.
Jack Naglieri: But when you're solving real problems as a vendor and you can be kind of neutral about it in a way where it's like, you know, our product is, you know, not saying like our product is the best thing out there.
Jack Naglieri: And like solve all your problems, like people like automatically turn off.
Jack Naglieri: To that, CISOs included.
Jack Naglieri: But if you're more like, hey, this is an emerging trend, this is a pattern that we're seeing, here's what we've been learning, here's sort of the trade-offs, like that tone I think is much more, like will resonate much more to the people that we speak to.
Jack Naglieri: Because there's so much out there in terms of marketing for cyber, and a lot of it is so opaque in terms of what it's saying.
Jack Naglieri: And I never want to be, I never want to be that.
Jack Naglieri: And I never want to like oversell, you know.
Kathy Lam: So.
Kathy Lam: Besides like transparency, what other maybe two or three adjectives would you have for like Panther's voice, which is probably your voice?
Jack Naglieri: Practical.
Jack Naglieri: It's always been, that's always been my intention since we started the company.
Jack Naglieri: I always felt like there was like such a lack of good practice.
Jack Naglieri: Pragmatist content, right?
Jack Naglieri: Like, even the technical sort of, like, how you would configure security monitoring in Amazon, right?
Jack Naglieri: Like, how the teams are actually doing it versus what a vendor might say.
Jack Naglieri: Yeah, I think pragmatism is just so important.
Jack Naglieri: Like, what's actually happening today from the people on the ground.
Jack Naglieri: That's just so important to relay.
Jack Naglieri: And we had, so we did a webinar on MCP that was, I think, a great example of this, where we invited in about, like, three or four customers, and we just, I just interviewed them live on how they were doing MCP and what they had built.
Jack Naglieri: And there's just so much engagement.
Jack Naglieri: People were like, oh, my God, I want to know how you did that.
Jack Naglieri: Like, I'm having that same problem.
Jack Naglieri: So as much as, like, you can talk about implementation in real world, like, that's kind of where the pragmatism flows into.
Kathy Lam: Kind of a side note.
Kathy Lam: I've noticed in the past security vendors could not, like, easily...
Kathy Lam: Get a quote from a customer, whereas, like, Panther is very different.
Kathy Lam: Like, I'm seeing customer stories all around.
Kathy Lam: Like, what's different that makes them say, hey, we're not going to do security about obscurity.
Kathy Lam: We're going to, like, say, like, we use this and, like, our security is way better because of this.
Kathy Lam: Like, they actually raised their hand.
Jack Naglieri: I know.
Jack Naglieri: It's great.
Jack Naglieri: I mean, it's definitely far off from what I thought would happen.
Jack Naglieri: And I think it might be related to the pragmatism of our platform.
Jack Naglieri: You know, the fact that we do give security teams so much robust tooling to build these things themselves.
Jack Naglieri: Maybe it's that.
Jack Naglieri: But I'm not sure.
Jack Naglieri: I've never asked someone why they said yes to letting us reference them.
Kathy Lam: But, yeah, there are a lot of them.
Kathy Lam: And then I have this other question.
Kathy Lam: And then, George, may have some additional ones.
Kathy Lam: What's a, like, a natural way to lead them from something that is content?
Kathy Lam: Content-driven to finally going, and by the way, Panther solves this, like, without triggering that, like, allergic reaction going, oh, this is just a sales lead.
Kathy Lam: Like, I know what you said before where you're offering, like, practical information, you're talking about the trends, but is there a way you've seen it or a way, like, you've done it where people are like, oh, yeah, it makes sense?
Jack Naglieri: Yeah, well, I can speak to what's worked in the Substack, because I think that's fairly representative of the audience.
Jack Naglieri: So just to give, like, a very tangible example for a moment, this blog post that I wrote on MCP, this is, like, my best performing piece on Substack ever, and I think it's probably a combination of timing and the content.
Jack Naglieri: But when I look back at this piece, the thing that I felt worked really well was just kind of, like, laying out what MCP is in a security context, so it's kind of, like...
Jack Naglieri: defining it for security folks.
Jack Naglieri: Giving, you know, I think even, like, the style of how this is written, too, where it's, like, shorter, you know, not super long paragraphs.
Jack Naglieri: Like, I think this style tends to resonate a bit more with security folks.
Jack Naglieri: Giving real examples, so going back to procurementism, right?
Jack Naglieri: It's, like, this is what MCP is.
Jack Naglieri: This is kind of the architecture of it.
Jack Naglieri: Here's a real example.
Jack Naglieri: And I'm giving, like, a sim-based, you know, security example.
Jack Naglieri: I'm using Panther in all these examples, right?
Jack Naglieri: So it's, like, list alerts.
Jack Naglieri: This is from Panther's MCP server.
Jack Naglieri: And I'm giving a link to, like, various things, right?
Jack Naglieri: So it's just I want to give people the background information on a subject or a technique or something.
Jack Naglieri: Give, like, right-of-way examples and ways that they can do it themselves.
Jack Naglieri: And just position it as, like, solving a problem, right?
Jack Naglieri: Versus, like, you have to use our solution to solve this problem, you know?
Jack Naglieri: Like,
Jack Naglieri: It's a little, like, trickier, right?
Jack Naglieri: We're just kind of, like, weaving it throughout or adding it at the end is what I typically tend to do.
Jack Naglieri: Like, I've been much more forward about Panther recently, so I wonder if I can even find an example of that.
Jack Naglieri: But this is a very similar one.
Jack Naglieri: It's, like, let's talk about what agents are.
Jack Naglieri: Here's what an agent means.
Jack Naglieri: Like, an agent is, you know, a system that can understand the environment, make decisions, et cetera.
Jack Naglieri: Like, here's some workflows in SIEM.
Jack Naglieri: And then I think maybe at the end, I would say, and, you know, this is what we're looking, what we're working on at Panther.
Jack Naglieri: That's an actual implementation of this.
Jack Naglieri: These are the features of it.
Jack Naglieri: This is how it works.
Jack Naglieri: Like, click here to, like, watch a video on it or something.
Jack Naglieri: So I've been adding that more throughout these posts.
Jack Naglieri: But this style of writing, like, these are my two top performing ones on AI that happened last year.
Jack Naglieri: And they actually kind of follow the same form.
Jack Naglieri: Format in a lot of ways, right?
Jack Naglieri: It's like kind of lay out the background, give definitions, give practical examples, and then you have some CTA.
Jack Naglieri: And I think like that format works quite well.
George Haikal: Yeah, it's useful, it's valuable, and it's contextualized.
Jack Naglieri: makes sense.
Kathy Lam: And then lastly, like when you're writing something you're really proud of, like what's your process?
Kathy Lam: Like do you start with like something like a claim or a counter argument?
Kathy Lam: Like what's your typical process?
Jack Naglieri: I think my typical process is first kind of like picking like a category or some area that's interesting right now.
Jack Naglieri: And it could be areas that are topical, like MCP was just a topical thing, and we were building our own MCP server.
Jack Naglieri: So I was like, okay, we should write about this.
Jack Naglieri: It's important, and people are talking about it, right?
Jack Naglieri: So there's a relevance part of it.
Jack Naglieri: And then there's like a...
Jack Naglieri: So maybe, you know, like the piece I just did around threat modeling, that was just an idea.
Jack Naglieri: was like, okay, like we want to go deeper into like technical, practical AI content.
Jack Naglieri: And that's just something that I wanted to do in January.
Jack Naglieri: And I want to put another one out next week if I can swing it.
Jack Naglieri: But this was just inspired by that idea of like, how can I give more like practical, tangible examples of using AI for threat modeling, detection, and response.
Jack Naglieri: And this blog got picked up in the TLDR newsletter, which is huge, which is awesome.
Jack Naglieri: But I was so confused.
Jack Naglieri: I was like, I can't believe that they wanted this one.
Jack Naglieri: I just, I guess this is how like the world is.
Jack Naglieri: You have something that has very low expectations, and then it like does really well, you're like confused by it.
Jack Naglieri: But this was just expanding an idea that I had around AI and threat modeling.
Jack Naglieri: And then I just.
Jack Naglieri: I don't know.
Jack Naglieri: It's I think it's really just one or the other.
Jack Naglieri: It's like something that's practical and relevant to what's happening in industry.
Jack Naglieri: It's something that's practical and relevant to what's happening at Panther or something that's just technical security content that I think would resonate.
Jack Naglieri: It's kind of one of those.
Jack Naglieri: I got a jump for a customer meeting, but if there's anything, if you want to chat again, just hit me up on Slack and we can make some more time.
George Haikal: Thanks so much for your time.
Jack Naglieri: Thanks.
Jack Naglieri: Take care.
Katie Campisi: Bye.
Katie Campisi: Bye.

