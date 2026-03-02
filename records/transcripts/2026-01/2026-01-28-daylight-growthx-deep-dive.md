# Daylight <> GrowthX - Deep Dive

<metadata>
date: 2026-01-28
time: 17:59 UTC
duration: 50 minutes
organizer: kathy@growthx.ai
participants:
  - name: Maya Rotenberg
    email: maya.rotenberg@daylight.ai
    affiliation: Daylight (VP Sales)
    role: external
  - name: Lior Liberman
    email: lior.liberman@daylight.ai
    affiliation: Daylight
    role: external
  - name: Kathy Lam
    email: kathy@growthx.ai
    affiliation: GrowthX
    role: organizer
  - name: George Haikal
    email: george@growthx.ai
    affiliation: GrowthX
    role: internal
  - name: Ademilade Shodipe-Dosunmu
    email: ademilade@growthx.ai
    affiliation: GrowthX
    role: internal
fathom_recording_id: 117890147
fathom_url: https://fathom.video/calls/547198879
share_url: https://fathom.video/share/jVdsUkiwsGy-SeaDSacxvn6LUgKLEzNf
source: fathom
enriched_on: 2026-02-28 12:00 UTC
</metadata>

---

## Summary

Daylight CEO Maya Rotenberg led GrowthX through a comprehensive review of Daylight's platform, architecture, and go-to-market approach. The session focused on how Daylight's "glass box" security platform fills gaps left by traditional MDRs through context-aware coverage, expert-augmented AI, and bidirectional tool integrations that eliminate alert backlogs and enable security teams to shift from reactive firefighting to strategic posture improvement.

---

## Context

Daylight is a next-generation managed detection and response (MDR) platform addressing critical failures in traditional security operations. Traditional MDRs (Expel, ReliQuest) and immature AI SOCs fail to provide the context, integration depth, and expert human judgment required to defend modern cloud-native infrastructure against AI-native threats. Daylight's differentiation centers on three pillars: (1) a "glass box" architecture that provides complete visibility into investigation logic, (2) deep, customer-specific integrations with 58+ custom playbooks per tool, and (3) expert security professionals who proactively improve the platform's knowledge base and lead live incident response rather than simply escalating to customers.

The meeting also covered Daylight's customer outcomes—Qualtrics went from ignoring all but critical alerts to a "zero open threats" backlog after a 3-week POC; Lovable achieved 24/7 operations and clean security posture in one month—and detailed the POC structure and pricing model (per-employee, significantly cheaper than premium MDRs).

---

## Relevance

- **Competitive Intelligence:** Daylight represents a significant threat to traditional MDR vendors (Expel, ReliQuest, others) due to AI-powered automation and expert augmentation, relevant for understanding the broader security market evolution and potential partnership or integration opportunities for GrowthX's CheckThat visibility product.
- **Sales Strategy & Content:** Daylight's value narrative ("glass box," "noise-free," "expert-augmented AI") and customer success stories (Qualtrics, Lovable) provide direct templates for GrowthX content marketing positioning and case study development.
- **Strategic Positioning:** Daylight's emphasis on context, bidirectional integrations, and proprietary detection rules (finding 60% of investigations) aligns with GrowthX's AEO/AI visibility focus and could be a model for how GrowthX positions CheckThat's detection and visibility capabilities.
- **Go-to-Market:** The 3-week POC structure and per-employee pricing model offer reference points for GrowthX's own SaaS positioning and engagement approach.

---

## Overview

- **Market Gap:** Traditional MDRs lack the context and integration depth to handle modern cloud-native, AI-native threats, escalating investigations back to customer teams at high rates, forcing "double paying" for security.
- **Daylight's Platform:** Three-pillar approach combining (1) context-aware integrations (58 custom playbooks per tool, bidirectional resolution), (2) proprietary detection rules on non-security logs (generates 60% of all investigations), and (3) expert-augmented AI service model.
- **Customer Outcomes:** Qualtrics eliminated alert backlog in 3 weeks; Lovable achieved 24/7 ops in one month; customers gain unprecedented visibility into security posture for the first time.
- **Differentiation:** Expert security professionals proactively improve detection rules and Daylight Knowledge, then lead live incident response—not just escalate—creating a service-driven moat competitors cannot replicate.

---

## Key Topics

### The Problem: Obsolete Security Models

  - **New Threat Landscape:** Cloud-native infrastructure and AI-native attacks (e.g., phishing indistinguishable from legitimate comms) make perimeter-based security models obsolete.
  - **Context is King:** Effective defense requires understanding user, system, and data context, which traditional MDRs cannot provide.
  - **Market Failures:**
      - **Traditional MDRs:** Offer limited coverage and high escalation rates, forcing customer teams to conduct investigations they paid to offload.
      - **AI SOCs:** Require skilled operators, offer only partial coverage (triage/investigation, not detect/respond), and are not mature enough for full automation.

### The Solution: Daylight's "Glass Box" Platform

  - **Three Pillars:**
    1.  **Context-Aware Coverage:** Deep, bidirectional integrations pull business context from all systems (security, identity, HR).
    2.  **Visibility & Control:** A "glass box" platform shows all investigation steps, enabling customer teams to understand and trust decisions.
    3.  **Expert-Augmented AI:** Senior security experts proactively improve the system and lead incident response.
  - **Integration Depth vs. Breadth:**
      - **Depth:** Custom playbooks for each alert type (e.g., 58 for WizDefend's 60+ alerts). This enables full automation; competitors only cover 2-3 alert types, escalating all others.
      - **Breadth:** New integrations built in days, not months, ensuring rapid coverage for new tools.
      - **Bidirectional:** Resolves alerts in the source tool (e.g., Wiz), creating a "zero backlog" state that frees up security team capacity.
  - **Proprietary Detection Rules:**
      - Runs detection rules on logs from non-security tools (e.g., Okta) to find suspicious activity.
      - **Impact:** This capability generates 60% of all investigations, filling critical blind spots missed by tools that only process security alerts.
  - **Platform Architecture:**
      - **Data Lake:** Stores all data for 90 days to enable deep historical investigations.
      - **AIR (Agentic Investigation Engine):** Orchestrates multiple, specific AI agents.
      - **Daylight Knowledge:** A customer-specific knowledge base (assets, users, policies) built from data and expert contributions.
      - **ChatOps:** Automates direct employee validation for suspicious activity.

### The Transformation: Customer Outcomes

  - **Qualtrics:** Went from ignoring all but critical alerts to a "zero open threats" backlog after a 3-week POC, enabling strategic posture improvement.
  - **Lovable:** Achieved 24/7 operations and a clean security posture within one month, avoiding the need for an expensive in-house team.
  - **10,000-person organization:** Gained a clear understanding of their security posture and blind spots for the first time after 25 years with traditional MDRs.

### The Service: Expert-Augmented AI

  - **Expert Role:** Proactively improves the platform by refining detection rules and contributing to Daylight Knowledge.
  - **Escalation:** Experts intervene immediately for live incidents or when the AI's confidence rating is low (\<60-65%).
  - **Incident Response:** Daylight experts lead customers through live incidents, a key differentiator from competitors who only escalate.

### Sales & Pricing

  - **POC (Proof of Concept):** A 3-week engagement designed to prove the transformation.
      - **Week 1:** Monitoring to build the customer's Daylight Knowledge base.
      - **Weeks 2-3:** Full service with twice-weekly meetings.
  - **Pricing:** Per-employee model for simplicity, though not publicly communicated. Significantly less expensive than premium MDRs.

---

## Action Items

**Maya Rotenberg (Daylight)**
- Email Kathy 2 videos: real investigation demo + Webflow blog upload walkthrough
- Upload updated Daylight style guide to shared folder for Kathy
- Email Kathy sales deck slides

**Kathy Lam (GrowthX)**
- Set up Webflow to auto-generate blog images per Daylight style guide

---

## Transcript
**Maya Rotenberg:** This meeting is being recorded.

**Kathy Lam:** Hi, Kathy. Maya. How are you doing?

**Maya Rotenberg:** Fine.

**Kathy Lam:** I was just reading the agenda.

**Maya Rotenberg:** It seems like a very loaded agenda for 45 minutes.

**Kathy Lam:** Maybe we can extend it a little bit?

**Maya Rotenberg:** Let's do our best. Let's try to cover it all. And then you can tell me what's missing.

**Kathy Lam:** Okay, perfect. And in fact, based on... How quickly we did our first meeting, I feel like we'll run to this pretty quickly. Did you actually look at the agenda on Notion or like the simple agenda in this calendar?

**Maya Rotenberg:** The simple agenda in the calendar. So there's more? good. Don't look at the Notion document. So I was thinking of actually going through the sales deck first. In the sales deck, there's an architecture slide. So we could go deeper because you wanted to understand the small differences. The sales deck ends with the POC, so we can talk about what's going for the POC. And then you can stop me at any point and ask me more questions. That's perfect. you to guide me.

**Kathy Lam:** We can start.

**Maya Rotenberg:** You invited someone else, but I don't think. Leo, she's our head of product, but the time didn't work. And yeah.

**Kathy Lam:** Cool. We can go ahead and get started.

**Maya Rotenberg:** Just this time. So, not sure. Hopefully, you're seeing the right.

**Kathy Lam:** Yep.

**Maya Rotenberg:** The world is changing. Yeah. So we'll jump right into how the world is changing. What we're basically saying, and I think that we've talked about it before, again, that the attack surface has changed significantly in the past few years. It's cloud-native, and there's AI-native threats, which changes everything when it comes to cybersecurity, and just things operate differently. Now, the MDR services that are, we're calling it legacy, but it's called the standard MDR, obviously, they were built for the perimeter-based security. What do I mean by that? That previously, you had a network. And everything was deterministic and predictable. A malicious file is a malicious file regardless of who's using it. Okay? However, in this world, everything is about context. There's no perimeter anymore. Everything is distributed. You have things coming in and coming out to your environment by design. And it's all about who's doing what and what is the action impacting. So you cannot, there's no deterministic questions anymore. It's not a question of, the alert that you're getting is no longer an alert of a malicious file. It's an alert of suspicious activity identified. And then you have questions. Who is the user? What was that, what systems did this suspicious activity touch? You need to collect data from a lot of systems because this is how a with different details have they'll Information flows today from one environment to another. You cannot look at silos like you used to, and that changes the whole way of investigation. Okay? I can go more in depth. You tell me if this is the level that you need.

**Kathy Lam:** This is the level.

**Maya Rotenberg:** Okay, good. So we're basically saying that the two major shifts that happened is cloud-native infrastructure and AI-native text. Cloud-native infrastructure is exactly what I just explained, that the way system works right now is cross-system. Information flows from one to another. And the second thing is AI-natives attacks. Attackers are using AI to accelerate everything. Time to acceleration has dropped from, I think that I had the information somewhere, two days to 25 minutes because of AI. Phishing emails are currently defined as a top. A threat to organizations because phishing has gotten so good that it's hard even for security managers to understand what is phishing because of AI. It looks indistinguishable from legitimate communication. And that just makes everything more complex. So what we're saying is that the solution that was good enough for six years ago is not relevant right now. And if you'll just continue doing what you did five years ago, three years ago, two years ago, you no longer have the ability to protect your organization. Because right now you have so many blind spots, you don't have a sufficient coverage of your system. Okay? And that leads me to what are the current solutions that you have in the market? This is where we're usually asking them, so what are you currently doing? If they are using with an MDR, what We're asking, who are you working with? How that's going? Are you getting good coverage? Are you drowning in alerts? Because coverage and drowning in alerts are the two main pain points, okay? This will open the door to understand what, you know, why are they reaching out to us? If they're using an MDR, we'll also ask them, so what are you considering? If they're not using an MDR, that will be a question as well, and that's AI SOC. AI SOC is usually not something that they're currently using, but something they're exploring, they'll maybe need a pilot or two. And then our questions will be, what are you hoping those tools will solve you? Because we know that there is an expectation gap there of what they're hoping and what the tools can provide. So we will start with there. Have you thought about who's going to operate the platform? Because we want to emphasize that you need someone to manage those tools. So those tools. are complex. Every AI system is complex, and you need someone to actually train it and run it. And we also share, you know, like, from our experience, most teams we talk to realize that they need skilled people that are calibrating those systems, takes time, da-da-da. There's another option that I'm not putting here.

**Kathy Lam:** Another option is in-house teams.

**Maya Rotenberg:** In-house teams is the ideal solution. You have full visibility. You can run your own playbooks, da-da-da-da-da-da-da. The two problems are, as I think that we've covered in our last session, it's really expensive, one person, seven people, and talent is scarce. In Western Europe, even more than in North America, but even in North America, it's really hard to get the talent. It's really expensive. You end up going for juniors, and then you pay double for that. Okay, so what we're saying is that traditional MDLs that offer 24-7 coverage... we're cognitant on not Thank They are giving you that coverage without hiring, which is perfect. But since they were not built for the cloud environment for the modern age, they offer limited coverage. So they are not able to build the full picture of what's going on in your environment. And they escalate too much. So what you end up doing is you actually have a team running investigations due to the MDR escalation. So you haven't saved anything. And that's why your team, that you offloaded everything to an MDR and you're paying hundreds of thousands of dollars a year for that MDR, your team is still doing investigations. So you're paying for a service that you're not really getting.

**Kathy Lam:** You're double paying, basically.

**Maya Rotenberg:** Yes. Now, it is important to understand that, as I think that we've talked last time, we are targeting Expel and ReliQuest users. And those are the premium MDR. So they're offering a significantly better experience than the other ones. But... But so a lot of CISOs are basically thinking, okay, this is as good as it's going to get. This is good enough. I can live with that. What we're trying to say is, no, this is still a pain and we can solve it, which is harder to say and convince than sound. Because the CISOs that we're talking with have been experiencing it for 20 years. So it's really challenging to make them rethink everything that they've known and learned about MDLs in the past 20 years. Moving on to AI SOC. AI SOC promised automation, but they're not mature enough yet. They require skilled operators and you need 24-7 staffing because if there's a breach at 2 a.m., you still need someone managing the tool in order to respond. They're not doing everything automatically. In addition, they're only covering 50% of the, what we're calling it. The 24-7 cycle, the cycle is made of four stages, detect, triage, investigate, and respond. And AI SOC is only for triage and investigation. So you need someone to detect and you need someone to respond and that's a problem. And then the next one we're saying, so how does a solution look like for the perfect world? Do you have a question or? And we're saying in a perfect world, you'd have three things working together. The first thing is full coverage with context-aware integration, right? Because remember we said about cloud environment, all of the systems are talking with everything. You have data, bits and parts of data all over the place. Everything is based on context. Everything depends on what system did what, who is the user, where is the data, et cetera. at that. Thank you. So you need a full coverage with context-aware investigation that scales with your environment. It's not just about reading alerts from the tools, but actually pulling business context about the user, the device, the policies, understanding what suspicious behavior looks in your environment. Second thing is control and visibility. Your team needs to know exactly how decisions are made, what context was used, why alerts were resolved. The classic MDR is pretty much a black box. One of the advantages that AI SOC are building on is that they're providing full visibility because they don't have a service to protect. They don't need to make you dependent. They're working with you, not against you. So all of the AI SOC are... ... ... Emphasizing their visibility. We're calling ourselves the glass box versus the black box. I think that if you compare us to AI SOC, we're even more detailed because it's not just AI that is showing everything and all of the steps. Our security experts that are an additional layer are communicating everything and feeding back information into the platform. And then we're saying the third thing that you need in order to get to a perfect world where SOC is just running in the most efficient way is that you need security experts. You need people on your team that sets the bar, that shows what great looks like, that understands what to do when there is a breach, that understands how to do advanced things like threat hunting and responding to an incident. And that's something that most mid-size enterprise do not have. Because there isn't a lot of talent and it costs a lot of money. And we believe that once you have it, you have the full coverage with the context integrations, you have the control and the visibility, and you have that security expert within your team. When you combine all of this, you are able to get to the noise-free security operations that scales with your business. Once you have a noise-free SOC, you actually know what is your coverage, what are your problems, what steps do you need to do in order to improve. What happens right now with 90% of the people that we're talking to, they're all stuck in firefighting mode. So you're always running after the next alert, the next investigation, and you don't have a good grasp of how does your environment look like and where are your security gaps. And you're not taking strategic work in order to improve your posture. Make sense?

**Kathy Lam:** Out of the slides that you shared and the ones in the future, which one is the most engaging one?

**Maya Rotenberg:** Is it the previous one? We haven't gotten to that yet. Got it.

**Kathy Lam:** Okay, sorry.

**Maya Rotenberg:** Now, this is by far the most engaging one because of our audience. This is actually, so I've talked about what's available in the market, the MDR and AI SOC. I talked about how does it look at the perfect world, and now I'm basically saying, so this is how we are delivering noise-free security operations, okay? This is how we're offering to get you to that perfect world. And this is basically how our platform is built with three parts, okay? The integration layer, this is where everything needs to be connected to everything. This is how we're pulling the information to build the context. to you you you you to get Then we have the agentic platform that has several components, and the third layer is the security experts, okay?

**Kathy Lam:** Can I ask one question about integration depth versus breadth here? You Yeah. So the architecture doc says, like, 90 to 100% of all alerts covered for WizDefend. Like, can you walk us what, like, deep integration means? Does it mean that it...

**Maya Rotenberg:** Yeah. So this is one of our problems, as I said, that it's all about the small details. So this is a great example of a small detail. Everybody's saying that we can integrate to everything. Wiz, Kraut, Stai, ta-ta-ta-ta-ta, everyone has hundreds of integrations. But the thing is that when you have a certain tool, let's say Wiz, Wiz has hundreds. If we're talking specifically about WizDefend, WizDefend has more than 60 different alert types. Okay, I'm thinking about the marketing parallel, but let's say you have a WordPress and you're getting alerts. You have different alerts. Every alert means something else and you need to run a different playbook in order to investigate it. So just having an integration to WordPress won't help you. You need, if you want an investigation to run automatically, you need to have a customized playbook for every single type of alert. Okay, here you have an alert about a user doing a wrong action. Here you have an alert about a suspicious, someone took down an element in your system. You need a customized playbook. What you need to do is, and that's the 90%, so out of the 60 plus alerts of WizDefend, we are covering 58. We have 58 customized playbook for all of the alerts. What others are doing, they're looking at the top two or three alerts, and they're writing customized playbook for only those two or three alerts. So what happens when an alert comes in that you don't have a customized playbook? You are not able to collect data because the AI doesn't work on itself. You have a playbook to understand, okay, I need to take this piece, and I need to correlate it to this, and I need to compare it to this. If you don't have a playbook, what happens is you're just collecting the basic information and throwing it over the wall to the SOC team, to the customer, and saying, we got an alert, we are not able to reach a decision, please check. That's useless. Yes, exactly. And this is why I'm saying that the minute that our customers are doing the POC, the three-week POC, everything changes. Because after experiencing a certain MDR for 20 years, they finally understand that there is a different experience. Okay, I'll go even more to length regarding each part and stop me when you want more data. So the first part, which is really important, the integration layer, we pull business context from everywhere, security tools, identity, ta-ta-ta-ta-ta-ta, and we have depth, but it's also bidirectional, okay, so which is something unique to us. What it means is that if we get an alert, let's say, from WizDefend that there's an issue, we investigate it, and the verdict is that it's benign, meaning it's not an issue. Other companies are just showing you in their system, okay, in Daylight System, benign, not an issue, but on WizDashboard, will still have thousands, if not tens of thousands of alerts that are unresolved. What we're doing is a very simple thing, we're just communicating back to Wiz and saying, this is resolved, this is the... Information because you need to show the platform information on why it was resolved. And then we're able to get companies into a zero backlog of alerts, which might sound meaningless because you already investigated it. But for the mindset of a security engineer or a security manager, it's a lot because you're starting your day without any backlogs. And when you're used to having thousands, and I'm literally talking about thousands of alerts that are constantly there, it changes the mindset. It frees your, I don't know, mind capacity to focus on other things. What else do I want to talk about? Integrations. Oh, another really important thing. And that's because, again, we build the system to serve AI. So we understood that indications are critical. We have built the system in a way that is helping us build integrations in days, while the classic MDRs, it takes them months. When a company buys a new security tool, which happens all the time, right? There's new innovation, new tools coming in. They're reaching out to the MDRs and saying, okay, from now on, we're using X. When can you cover it? Usually, the answer is, let's talk about it. Let's do a negotiation, add it to the contract, maybe in 12 months. We can add it in a matter of days. And this really should get people to a very high coverage. Well, right now, the average coverage, well, it changes. There's no average, but sometimes we can talk to 10,000 people, companies, that have about 40% visibility on their environment. It changes a lot. okay, next thing is the... ... ... time. Oh, one more thing, again, and if it's too much details, then you can ignore it. We also have our own detection rules. Okay, what does that mean? We are pulling security alerts. So when you have a security tool that has a finding, we will take that alert and investigate. However, in addition, we're also pulling all of the logs. For example, Okta is an identity tool. Okay? And it's not a security tool, so there's no security alerts. But we have our own detection rules that we can run on the logs to find if there's been a suspicious activity. And then we will investigate on it. Now, this is something that is unique. I can't tell you that no one else is doing it, but very few companies are doing it. It's a very critical decision that we did early on to include detection. As I said, remember, there's a four-step cycle, so detection is the first step. We wanted to cover the entire cycle, so we included detection, and right now we're seeing that 60% of all of our investigations result from detection. That means that companies that do not have that detection component are missing more than 50% of the things that they need to investigate.

**Kathy Lam:** So that leads to the extra backlogs. Okay, that makes sense.

**Maya Rotenberg:** No, it doesn't lead to extra backlogs. It leads to blind spots.

**Kathy Lam:** Blind spots, okay.

**Maya Rotenberg:** So you have the security alerts, you're investigating, everybody gets that, that's fine. But we're running detection on the logs of the tools itself. If you don't have the detection logs, you won't find something suspicious to investigate. So you will have less investigations, but you won't find things that you might need to know.

**Kathy Lam:** Yeah, more faults, negatives, got it.

**Maya Rotenberg:** Yeah. This is the system. I'll go quickly. You'll We it on the recording. Stop me if something doesn't make sense. So this is the data lake. This is just a place where we store all of the information. We want all of the data on our system. We push all of the information to the data lake, okay? A dedicated instance for every customer, very secure. We save it for 90 days. So we can have all of the capabilities to investigate something because many times when you have a breach, it didn't start in a second. There has been a suspicious activity for long. Then we have AIR. AIR is actually the investigation engine, okay? It's made up of multiple of AI agents that are very specific. Every AI agent has a very specific core task. We did not, unlike many competitors, we did We did not build an AI agent who's a know-it-all. We have many specific AI agents. And then we've built an AI-infused orchestration layer that manages the different AI agents. And it basically, you know, orchestrates over the entire information that runs between agents and agents and people. The AIR is pulling information from the data lake and also from Daylight Knowledge. Daylight Knowledge is a system where we are actually learning about the environment. We are learning about your business. What are the business critical assets? How does your employers look like? Do you have a lot of freelancers? What countries are suspicious? What countries are not? What time do you usually work? We learn about the different activities. So when something changes, we are able to learn it more. Context is coming both from pulling all of the data, but this is a very important part that many competitors have ignored, and we see it as a very important part. Our security experts are contributing a lot to the knowledge by pulling insights that they see as experts and infusing it into daylight so we have a better understanding of the environment. And this is the chat at tops. Yes.

**Kathy Lam:** Is that per customer, or is it tenant? Yes. That's tenant-specific.

**Maya Rotenberg:** Every single customer has their own daylight knowledge.

**Kathy Lam:** Got it.

**Maya Rotenberg:** In addition, we have the chat tops. In many cases, sometimes you need to validate with the employee. For example, you saw someone from the Maldives entering a certain system, and you know you don't have any full-time employees in the Maldives. But maybe it's someone who, you know, took a vacation and decided that it misses works. Thank Thank Thank And you don't really know. So usually what our competitors are doing, they're reaching out to the customer, and then the customer are reaching out to the employer. We have an automated system that is actually asking for validation. So the chat ops are talking to the employees directly. That's it. So a lot of different components within the Adjetic platform. And then the third layer, which is really important, is the security experts. As I've mentioned several times, I think, so far, they're really different in their profile than others.

**Kathy Lam:** Right.

**Maya Rotenberg:** Anything that I forgot?

**Kathy Lam:** No, I think this is very impressive that you do this.

**Maya Rotenberg:** Yeah. This is usually what we're showing customers and examples. So this is a Weez Alert.

**Kathy Lam:** Weez is a cloud security tool.

**Maya Rotenberg:** And as you can see, many alerts are coming with no information. They're just coming with a log and... A timestamp and a type of alert, and that's it. So we're explaining them how we're actually going through and investigating, pulling, going to a Cloud Rail system and pulling information according to the timestamp. And then we're going into entry IDs like OctaEZ identity system. We're pulling information based on data that we collected from the Cloud Rail. And then we're moving on, and we're actually verifying the information, all done with less than a minute, and providing a view that very few solutions out there right now are able to provide. What changed in our customers? So this is a really important part, I think, for the content. What I'm trying to do, and I think that I said it previously, I don't want to position us as an X percent better. It's about a transformation. And what do I mean by transformation? It means that once we are... You know, they are switching their solution or they're onboarding us. It impacts how the organization looks like. They're changing roles and responsibility. And that's because their SOC, their security operation team or security team, is starting to act in a very different way. Okay? I gave three different examples. So Qualtrics were not able to just handle all of their alerts. So for two years, they ran just looking at their critical and high alerts. And they were just, they thought that this is not something that is manageable. Within the three-week POC, we got them to a zero open threats. That means that their main security platforms did not have any alert backlogs. So they didn't need to make any hard decisions. They knew that they were actually reviewing all of the alerts. And I can tell you that Qualtrics also... So made significant changes in the roles of responsibility because now their team has time to run, actually, projects to improve their posture. Lovable. Lovable needed to start at 24-7. It was a board-level decision. The CISO did not want to hire a classic MDR because he knew that he didn't have the team to support a classic MDR. They were thinking about maybe going to the in-house route, although it's a very small company and it's against their mindset to hire a lot of people. And within a month, we were able to clean all of their systems. Again, zero open threats. We got them from zero to 24-7 operational during the period of the POC. In 60, the 10,000. Latin-class people organization, both in Germany and the U.S., they were a 25-year customer of MDRs, and they're saying that for the first time, they feel like they have a good understanding of what's going on. They understand where do they have blind spots, what is the coverage, they understand what are the most important things that they need to work on in order to improve their security. They did not have that understanding before, because an MDR service wants to keep you as a service by making you think that you don't know your environment like they do.

**Kathy Lam:** Questions? No, I don't think so. Ade, do you have any questions here?

**Maya Rotenberg:** Yeah, I actually had one.

**Ademilade Shodipe-Dosunmu:** Yes. Sorry. I was interested in, like, the human in the loop model. Like, how does your escalation...

**Maya Rotenberg:** Okay, so first of all, and this is something that is really important, I don't want us to talk about escalation process. The fact that our security experts are different and have a different profile, that means that also their role within the system In all other systems, humans are there in order to do escalations. Our security experts are doing some escalations, but they're doing a very small part of their job is actually escalation. A larger part of their role is actually proactively improving the system by adding more knowledge and improving detection rules. So that's just a very high level. I don't want us to go. I want us to have a different language when we're talking about it than our competitors, so it's not just escalation. To your point, when we're onboarding a new customer, every verdict that is a certain severity level goes through our experts. And with time, we are saying to the customer, okay, all of the alerts that are coming from Weez and are this type of alert class, we have enough information to see that the AI is doing a good enough job, so we're not going to do that. And with time, we're just kicking off more and more and more to being automated. And that means that whenever the system flags itself that its confidence is low, and our system is rating every single investigation with a confidence rating, so we're investigating everything. That is above 50, that is lower than 60% confidence or 65% confidence changes from customer to customer. And also when the system alerts that there might be a live breach, a live incident, in that scenario, our experts are immediately kicked in. That is also a big differentiating to others because once you have a live incident, that's when you call the system. And you said, there's a live incident, all hands on deck, and then you leave it because you are an MDR analyst. In our case, because those are security experts and this is where they shine, then we are actually working and leading our customers through those incidents. And whenever we have an incident and we're getting permission from the customer, we are writing a report on it. We already have two reports live. We're writing like a blog article on it. And we had a third time that... The approved an incident, so another blog post should be live tomorrow morning.

**Kathy Lam:** Awesome. You were going to the math slide? That's actually one of the questions I had.

**Maya Rotenberg:** Yeah. So this is the services that we have. Very important. I wrote it also in the report. It's very important that we position ourselves as a service, security services company. MDR, it is the leading product we started for me because it's where the biggest pain lies. But there are others. There's threat hunting, which is a completely different service. It's actually, it's a training exercise. You are saying, okay, there's, I believe that there is an intruder. There is an attacker in the system. Now I'm going to have to look and find it. This is something that usually enterprises are doing every three months or so. and to to to and In order to find detection gaps in your system, okay? Another one is phishing. So there are very good email security systems like Abnormal and Sublime that are doing an amazing job, but they're pushing a lot of alerts, tons of alerts. And you need to have people investigating and responding to it. And this is where many small enterprises find it challenging. It's not a very complicated investigation, but it's massive amounts of alerts. This is usually where AI SOC tools shine, okay? Because the investigation is not critical, but you have high quantity. So we're doing that as well. Death loss prevention, again, it's more like it's an exercise that... The companies usually do every six months. And if you don't have the security expertise, you need to outsource it. An incident report, that's like a Mayday service. You got breached. Now you need to hire an incident responder within hours. You need them in order to do the investigation to ensure that there's no live attack in the system right now. And to write a full report about what happened, so you can submit it to the regulations and the insurance. And there's a whole bureaucracy that comes with a breach. So that's something that we are not yet offering.

**Kathy Lam:** I have one question. You mentioned threat hunting, phishing, and DOP were coming soon, but they are already available now.

**Maya Rotenberg:** so this is an ongoing discussion within our company. What happens is that threat hunting will currently, we have two design partners. So it's not 100% live.

**Kathy Lam:** It will be in a few weeks.

**Maya Rotenberg:** And phishing in DLP, are currently offering it to customers, but in a not full range. So we're covering 80% of what we want to cover in phishing. We're covering 50% of what we want to cover in DLP. There's a concern that when we're doing the sales deck, that people will, if we'll say coming soon, they will say, oh, my God, you're not covering phishing at all. So, but as a standalone service, it's not there yet.

**Kathy Lam:** Got it. And most people are using your MDR services and they're attaching the other additional ones.

**Maya Rotenberg:** Yes, all classic MDR providers are offering threat hunting and phishing in DLP. Some, not a lot. Some are offering incident response, but that's like the odd one. But everything else, people are accustomed to getting that from their MDR provider.

**Kathy Lam:** Excellent. Excellent. Excellent.

**Maya Rotenberg:** But you should know that there's also companies that are an expert in threat hunting, and that's all they do, just threat hunting. So the competition, the landscape is more complex than that.

**Kathy Lam:** Got it. Okay, this makes sense.

**Maya Rotenberg:** Yes.

**Kathy Lam:** Which slide has the most skeptical responses? When they look at it, they're like, oh, they question it a bit, and they say, this isn't for me, or something.

**Maya Rotenberg:** Definitely the customers. Oh, because they don't. They don't think, again, and this is why, and I think that I wrote it in one of the comments, they're used to seeing marketing slides that are overpromising. One of the things that you won't see here, and that we should try to minimize in our content, is other competitors are talking a lot. We about different metrics. MTTR, mean time to respond. MTTA, mean time to acknowledge. Escalation rate, stuff like that. They're seeing unbelievable percentage all over the place. They don't believe it. They even, when you're talking to them about metrics, they don't want to, they're telling you immediately during the sales calls, let's not talk about metrics. I want to understand how you work. I want to see the architecture. I don't want to see . That's basically what they're saying. So they don't believe the transformation. That's not a good seller for them.

**Kathy Lam:** Yeah, that makes sense. Cool. I think we're almost at time, but I think you've covered quite a lot. I do have some other questions after the slide that I will ask.

**Maya Rotenberg:** So this is just how we're doing the three-week proof of concept, the POC. Yep. First, we... We're just doing monitoring. We're not providing service to the customer because we need to learn the system to understand what's suspicious, what's not. We are, the entire solution is based on context. Context based on the information from your system and the information that we build on your environment, what we call the daylight knowledge. It's a key component. We need a week to build it in order to start running. And then you get two weeks of full service with meetings twice a week and full report at the end. And this is where the conversation changes. And, well, you said you have questions. This is actually the system and what customers are seeing. But do you want to ask questions?

**Kathy Lam:** I think one question I had is when a person gets an alert, like, what does it look like? Does it look like it's here in the dashboard or is there another thing that shows?

**Maya Rotenberg:** So. So it's a case, but when the system gets an alert, they're not seeing it because you need to understand it a day, you get 300, 400 alerts. So it's not like we're telling them every time. We are sending them, we are connected to their Slack or Teams or whatever the company uses. And we are showing them, telling them that something in a high severity has come through or something like that. and we're sending links to the platform, okay? And all of the information is within the platform, okay? Let me look for a good... I'll send you a demo, a video, a six-minute video that actually shows you a good example because this is just a demo file without the investigation. I'll send you one real one. So you can actually, so that they're going into the timeline, and they can see all of the steps. This is what we got from Weez. This is what we pulled from CrowdStrike. This is how we correlated the data, and all of the information is within the system.

**Kathy Lam:** Got it. Let me see. I think, oh. So when you hear a customer object that they say they'll come back in a year, have you guys been able to respond with anything else that will get them to come back faster or actually just give you a try?

**Maya Rotenberg:** Yeah, this is why we're starting with The World is Changing, to make them understand that they're currently, they feel like they're making the safer choice. But they're actually making a conscious decision to stay with a limited budget. So it feels to them that you're doing the safe choice of staying with what they know, but they're actually choosing to be blind. And we're focusing on that, we're explaining, we're trying to estimate if they've done a POC, that's great, although we've never been in a problem of someone who did a POC understood what is their situation and didn't move on. But in order to get people to do the POC, we're trying to estimate their coverage. We're trying to explain the level of risk from AI attacks that are getting more aggressive every single quarter. But right now, it's very limited impact. I think right now, many CISOs just feel overwhelmed, because there's so much confusion when it comes to AI insecurity. And it feels to them that... Like the safer choices, do nothing. Don't change anything. Who's going to blame you for sticking with IBM, right?

**Kathy Lam:** Yeah, but then, yeah, you're sticking your head in the sand. As part of the onboarding process, I know your system takes a week to kind of learn, but is there still a lot of input that the customer needs to give you in order to be able to, like, what to do after the system gets an alert? Or is this mostly from your team side?

**Maya Rotenberg:** So they have an onboarding checklist that they need to fill in, and they need to go through. It's 12 steps where they need to tell us, connect us to the HR system so we can understand freelancers and employees. We need them to highlight what are the business critical assets. There's, like, checklist that once we know that about the environment, it's enough. And we usually, for a POC, we'll do a partial checklist because we don't want the customers to work hard in a POC. But then when we're onboarding them for real, then we'll ask them to complete the knowledge.

**Kathy Lam:** And is the same security team that works with them during the PLC the same team that continues with them after they renew?

**Maya Rotenberg:** There's only one security team. This is the structure and this is how it will remain. We believe that all of the personalization are coming from the system, not the security experts. The security experts are all very active on the platform, Slack, Teams, whatever it is. They're communicating, but their identity doesn't really matter, which is a big difference because with traditional MDR, everybody wants a dedicated analyst. So the analyst will learn them and will understand how to work with them. And for us, everything is automated. We are learning, you know, okay, this company wants, the CISO wants to get all of the alerts. This one, the IT is more in control. We are learning the environment. Very, very quickly, and we are responding to it. So what we're actually educating our customers that it doesn't really matter who your security experts, it's one team for.

**Kathy Lam:** Got it. One last question. Is your pricing model based on like an endpoint, an employee, like a flat fee?

**Maya Rotenberg:** How does it work?

**Kathy Lam:** How does it compare with your competitors?

**Maya Rotenberg:** Yes. Right now, we're doing it per employee because it's very, very easy and very transparent. But we're not communicating it. We're not making it public. It's just a middle ground right now. It's not going to continue on that way. We'll probably move to a pricing that is more AI based. But not right now. pricing, look, at the end of the day, we are significantly cheaper than other MDR solutions. But since we are not able to communicate our pricing, then right now it's not something that I'm focusing on.

**Kathy Lam:** Got it. But during the sales process, they'll talk about how it's just a more efficient process than Expel and ReliantQuest.

**Maya Rotenberg:** And more efficient in what?

**Kathy Lam:** outcomes or the pricing? didn't understand. Both. Because we're not... I think during the sales process, when the customer asks about pricing, they are like...

**Maya Rotenberg:** The answer they will get vary from customer to customer. The majority will say it's about employees, but sometimes we'll say it's a very complicated system or a very simple system and we'll adjust accordingly.

**Kathy Lam:** Got it. We'll leave that off and not be vague about that. I think once we see a...

**Maya Rotenberg:** We could... I have no problem saying that because we have a different architecture, then we're not as expensive or significantly less expensive than the others.

**Kathy Lam:** But yeah, right now we can go into further details. Got it. I think you answered most of the questions. There was one thing I wanted to ask you later, which was to, if you have like a recording of like, how do you upload blogs to your CMS? But we can do that later or like now if you want.

**Maya Rotenberg:** I can record it and share it.

**Kathy Lam:** Okay, perfect.

**Maya Rotenberg:** So I owe you two videos. One is about the investigation within the system. How does it look like? And the other one is for the Webflow.

**Kathy Lam:** Perfect. Yeah, we're very familiar with Webflow. And then this last question, sorry. We have a way to generate blog images that will be like, you want that, right? Okay, we'll set up the Webflow to do that.

**Maya Rotenberg:** I did upload a style guide. Yes, but it's slightly outdated.

**Kathy Lam:** But.

**Maya Rotenberg:** Let me upload something that is more up-to-date.

**Kathy Lam:** Okay, perfect. Thank you. Yeah, this is perfect. Do you think it would be worthwhile for us to have the slides or I'll just get it from the video?

**Maya Rotenberg:** Sure, can share with you the slides, no problem.

**Kathy Lam:** Okay, great. Thanks so much, Maya. It was great. Thank you. Bye. Bye.

