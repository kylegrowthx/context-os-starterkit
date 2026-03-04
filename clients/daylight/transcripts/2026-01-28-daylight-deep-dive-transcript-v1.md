# Daylight <> GrowthX — Deep Dive
**Date:** January 28, 2026
**Duration:** 52 minutes
**Participants:** Maya Rotenberg (Daylight, CMO), Lior Liberman (Daylight), George Haikal (GrowthX), Kathy Lam (GrowthX), Ademilade Shodipe-Dosunmu (GrowthX)
**Source:** Fireflies

---

## Summary

Deep dive into Daylight's product architecture and the cybersecurity landscape. The discussion centered on how cloud-native infrastructures and AI-driven attacks are rendering traditional MDR solutions inadequate. Maya explained that legacy solutions fail in distributed environments where context is crucial, leading to alert overload and double spending. Daylight's model combines deep integration with an AI-driven investigation engine and proactive security experts. Customers report zero open threats within weeks of implementation. Pricing is positioned as more affordable than premium MDRs, with plans to evolve toward an AI-based pricing model.

## Key Takeaways

- Traditional MDR solutions fail in cloud-native environments — lack context, create alert overload, and cause double spending on investigations
- Daylight combines deep integrations, an AI investigation engine, and proactive security experts for full coverage
- Customers see zero open threats within weeks of onboarding
- Pricing is below premium MDRs, with plans to evolve toward AI-based pricing
- Product architecture: integrates deeply into customer environments for context-aware detection and response

## Action Items

**Maya Rotenberg:**
- Send demo video showing investigation process within the platform
- Provide demo video explaining Webflow usage
- Upload updated brand/style guides for marketing materials
- Share slides from the sales deck presentation

**Kathy Lam:**
- Review demo videos and provide feedback
- Coordinate any additional questions related to CMS/blog uploads

---

## Transcript

**Maya Rotenberg:** This meeting is being recorded. Hello. Hi, Kathy.

**Kathy Lam:** Maya. How are you doing?

**Maya Rotenberg:** Fine. I was just reading the agenda. It seems like a very loaded agenda for 45 minutes.

**Kathy Lam:** Maybe we can extend it a little bit.

**Maya Rotenberg:** Let's do our best. Let's try to cover it all and then you can tell me what's missing.

**Kathy Lam:** Okay, perfect. And in fact, based on how quickly we did our first meeting, I feel like we'll run through this pretty quickly. Did you actually look at the agenda on notion or like the simple agenda in this calendar?

**Maya Rotenberg:** The simple agenda in the calendar. So there's more. Okay, good.

**Kathy Lam:** Don't look at the notion document.

**Maya Rotenberg:** Okay. So I was thinking of actually going through the sales deck first. In the sales deck, there's an architecture slide so we could go deeper because you wanted to understand the small differences. The sales deck ends with the poc. So we can talk about what's going with the poc and then you can stop me at any point and ask me more questions. That's perfect. I'll trust you to guide me.

**Kathy Lam:** We can start. You invited someone else, but I don't.

**Maya Rotenberg:** Think Lior, she's our head of product. But the time didn't work and.

**Kathy Lam:** Yeah.

**Maya Rotenberg:** Cool.

**Kathy Lam:** We can go ahead and get started.

**Maya Rotenberg:** Just a sec. Okay, so nutshell. Okay. Hopefully you're seeing the light. Yep.

**Kathy Lam:** The world is changing.

**Maya Rotenberg:** Yeah. Okay, so we'll jump right into how the world is changing. What we're basically saying, and I think that we've talked about it before again, that. The attack surface has changed significantly in the past few years. It's cloud native and there's AI native threats, which changes everything when it comes to cybersecurity. And just things operate differently now. The MDR services that are, we're calling it legacy, but it's called the standard mdr. Obviously they were built for the perimeter based security. What do I mean by that? That previously you had a network and everything was deterministic and predictable. A malicious file is a malicious file regardless of who's using it. Okay. However, in this world, everything is about context. There's no perimeter anymore. Everything is distributed. You have things coming in and coming out to your environment by design. And it's all about who's doing what and what is the action impacting. So you cannot. There's no deterministic questions anymore. It's not a question of the alerts that you're getting is no longer an alert of a malicious file. It's an alert of suspicious activity identified. And then you have questions. Who is the user? What was that? What systems did this? Suspicious activity attached. You need to collect data from a lot of systems because this is how information flows today from one environment to another. You cannot look at silos like you used to, and that changes the whole way of investigation. Okay, I can give. I can go more in depth. You tell me if this is the level that you need.

**Kathy Lam:** This is the level.

**Maya Rotenberg:** Okay, good. So we're basically saying that the two major shifts that happened is cloud native infrastructure and AI native attacks. Cloud native infrastructure is exactly what I just explained. That the way system works right now is core system information flows from one to another. And the second thing is AI natives attacks. Attackers are using AI to accelerate everything. Time to acceleration has dropped from, I think that I had the information somewhere two days to 25 minutes because of AI phishing. Emails are currently defined as a top threat to organizations because phishing has gotten so good that it's hard even for security managers to understand what is phishing because of AI. It looks indistinguishable from legitimate communication. And that just makes everything more complex. So what we're saying is that the solution that was good enough for six years ago is not relevant right now. And if you'll just continue doing what you did five years ago, three years ago, two years ago, you no longer have the ability to protect your organization. Because right now you have so many blind spots, you don't have a sufficient coverage of your system. Okay. And that leads me to what are the current solutions that you have in the market? Okay, this is where we're usually asking them. So what are you currently doing? If they are using with an MDR provider, meaning they're part of ICP number two, we're asking who are you working with, how that's going? Are you getting good coverage? Are you drowning in alerts? Because coverage and drowning in alerts are the two main pain points. Okay. This will open the door to understand why are they reaching out to us. If they are using an mdr, we'll also ask them, so what are you considering? If they're not using an mdr, that will be a question as well. And that's aisoc. AISOC is usually not something that they're currently using, but something they're exploring. They maybe did a pilot or two. And then our questions will be, what are you hoping those tools will solve you? Because we know that there is an expectation gap there of what they're hoping and what the tools can provide. So we will start with there. Have you thought about who's going to Operate the platform because we want to emphasize that you need someone to manage those tools. So those tools are complex. Every AI system is complex and you need someone to actually train it and run it. And we also share, you know, like from our experience, most teams we talk to realize that they need skilled people that are calibrating those systems takes time. There's another option that I'm not putting here. Another option is in house teams. In house teams is the ideal solution. You have full visibility, you can run your own playbooks. Da da da da da da da. The two problems are, as I think that we've covered in our last session, it's really expensive. One person, seven people. And talent is scarce in Western Europe, even more than in North America. But even in North America, in it's really hard to get the talent. It's really expensive. You end up going for juniors and then you pay double for that. Okay, so what we're saying is that traditional MDLs that offer 24. 7 coverage are giving you that coverage without hiring, which is perfect. But since they were not built for the cloud environment for the modern age, the they offer limited coverage. So they are not able to build the full picture of what's going on in your environment and they escalate too much. So what you end up doing is you actually have a team running investigations due to the MDR escalation. So you haven't saved anything. And that's why your team that you offloaded everything to an MDR and you're paying hundreds of thousands of dollars a year for that mdr. Your team is still doing investigations. So you're paying for a service that you're not getting.

**Kathy Lam:** You're double paying. Basically, yes.

**Maya Rotenberg:** Now, it is important to understand that as I think that we've talked last time, we are targeting Expel and ReliaQuest users and those are the premium mdr. So they're offering a significantly better experience than the other ones. But so a lot of CISOs are basically thinking, okay, this is as good as it gotta get. This is good enough. I can live with that. What we're trying to say is, no, this is still a pain and we can solve it. Which is harder to say inconvenienced than sound because those decisions that we're talking with have been experiencing it for 20 years. So it's really challenging to make them rethink everything that they've known and learned about MDLS in the past 20 years. Moving on to AI SOC. AI SOC promise automation, but they're not mature enough yet. They require Skilled operators. And you need 24. 7 staffing. Because if there's a breach at 2am, you still need someone managing the tool in order to respond. They're not doing everything automatically. In addition, they're only covering 50% of what we're calling it the 24.7cycle. The cycle is made of four stages. Detect, triage, investigate and respond. And AI SoC is only for triage and investigation. So you need someone to detect and you need someone to respond. And that's, that's a problem. And then the next one we're saying, so how does a solution looks like for the perfect world? Do you have a question or. Okay. And we're saying in a perfect world you'd have three things working together. The first thing is full coverage with context aware integration. Right? Because remember we said about cloud environment, all of the systems are talking with everything you have data bits and parts of that are all over the place. Everything is based on context. Everything depends on what system did what, who is the user, where is the data, et cetera. So you need a full coverage with context aware investigation that scales with your environment. It's not just about reading alerts from the tools, but actually pulling business context about the user, the device, the policies, understanding what suspicious behavior looks in your environment. Second thing is control and visibility. Your team needs to know exactly how decisions are made, what context was used, why alerts were resolved. The classic MDR is pretty much a black box. One of the advantages that AI SOC are building on is that they're providing full visibility because they don't have a service to protect. They don't need to make you dependent. They're working with you, not against you. So all of the AI SoC are emphasizing their visibility. We're calling ourselves the glass box versus the black box. I think that if you compare us to AI SoC, we're even more detailed because it's not just AI that is showing everything in all of these steps. Our security experts that are an additional layer are communicating everything and feeding back information into the platform. And then we're saying the third thing that you need in order to get to a perfect world where SOC is just running in the most efficient way, is that you need security experts. You need people on your team that sets the bar, that shows what great looks like, that understands what to do when there is a breach, that understands how to do advanced things like threat hunting and responding to an incident. And that's something that most mid sized enterprises do not have because there isn't a lot of talent and it Costs a lot of money. And we believe that once you have it, you have the full coverage with the context integrations, you have the control and with the visibility and you have that security expert within your team. When you combine all of this, you are able to get to the noise free security operations that scales with your business. Once you have a noise free soccer, you actually know what is your coverage, what are your problems, what steps do you need to do in order to improve what happens right now with 90% of the people that we're talking to, they're all stuck in firefighting mode. So you're always running after the next alert, the next investigation and you don't have a good grasp of how does your environment looks like and where are your security gaps and you're not taking strategic work work in order to improve your posture. Make sense?

**Kathy Lam:** Does out of the slides that you shared and the ones in the future, which one is the most engaging one? Is it the, the previous one?

**Maya Rotenberg:** We haven't got into that yet. Ah, got it.

**Kathy Lam:** Okay, sorry.

**Maya Rotenberg:** Now this is. Okay, this is the, this is by far the most engaging one. Because of our audience. This is actually. So I've talked about what's available in the market, the MDR and AI SoC. I talked about how does it look at the perfect world. And now I'm basically saying so this is how we are delivering noise free security operations. This is how we're offering to get you to that perfect world. This is basically how our platform is built with three parts. Okay. The integration layer. This is where everything needs to be connected to everything. This is how we're pulling the information to build the context. Then we have the agentic platform that has several components and the third layer is the security experts.

**Kathy Lam:** Okay, can I ask one question about integration depth? This is breath here.

**Maya Rotenberg:** Everything. Yeah.

**Kathy Lam:** So the architecture doc says like 90 to 100% of all alerts covered for Wiz Defend. Like, can you talk us what like deep integration means? Does it mean that it.

**Maya Rotenberg:** Yeah. So this is one of our problems. As I said that it's all about the small details. So this is a great example of a small detail. Everybody's saying that we can integrate to everything with CrowdStrike. Ta da da da da. Everyone has hundreds of integrations. But the thing is that when you have a certain tool, let's say Wiz. Wiz has hundreds. If we're Talking specifically about WizDefend, WizDefend has more than 60 different alert types. Okay. I'm thinking about the marketing parallel, but let's Say you have a WordPress and you're getting alerts, you have different alerts, every alert means something else and you need to run a different playbook in order to investigate it. So just having an integration to WordPress won't help you. If you want an investigation to run automatically, you need to have a customized playbook for every single type of alert. Okay. Here you have an alert about a user doing a wrong action. Here you have an alert about a suspicious someone took down an element in your system. You need a customized playbook. What you need to do is, and that's the 90%. So out of the 60 plus alerts of WizDefend, we are covering 58. We have 58 customized PlayBook for all of the alerts. What others are doing, they're looking at the top two or three alerts and they're writing customized playbook for only those two or three alerts. So what happens when an alert comes in that you don't have a customized playbook? Vuvo, you are not able to collect data because the AI doesn't work on itself. It needs to have a playbook to understand, okay, I need to take this piece and I need to correlate it to this and I need to compare it to this. If you don't have a playbook, what happens is you just collecting the basic information and throwing it over the wall to the SOC team, to the customer and saying, we got an alert, we are not able to reach a decision. Please check. It's useless. Yes, exactly. And this is, this is why I'm saying that the minute that our customers are doing the POC, the three week POC, everything changes. Because after experiencing a certain MDR for 20 years, they finally understand that there is a different experience. Okay, I'll go even more to length regarding each part and stop me when you want more data. So the first part, which is really important, the integration layer, we pull business context from everywhere. Security tools, identity, ta da da da da. And we have depth, but it's also bi directional. Okay, so which is something unique to us, what it means that if we get an alert, let's say from WizDefender, there's an issue we investigated and the verdict is that it's benign, meaning it's not an issue. Other companies are just showing you in their system. Okay, in daylight, system, benign, not an issue. But on Wiz Dashboard you will still have thousands, if not tens of thousands of alerts that are unresolved. What we're doing is a very simple thing. We're just communicating back to Wiz and saying this is resolved, this is the information because you need to show the platform information on why it was resolved. And then we're able to get companies into a zero backlog of alerts which might sound meaningless because you already investigated it, but for the mindset of a security engineer or a security manager, it's a lot because you're starting your day without any backlogs. And when you're used to having thousands, and I'm literally talking about thousands of alerts that are constantly there, it changes the mindset. It frees your, I don't know, mind capacity to focus on other things. Okay, what else do I want to talk about? Integrations. Oh, another really important thing. And that's because again, we build this system to serve AI. So we understood that integrations are critical. We have built the system in a way that is helping us build integrations in days. While the classic MDLs, it takes them months. When a company buys a new security tool, which happens all the time, right, there's new innovation, new tools coming in, they're reaching out to the mdls and saying okay, from now on we're using X. When can you cover it? Usually the answer is let's talk about it, let's do a negotiation, add it to the contract. Maybe in 12 months we can edit in a matter of days. And this is really should get people to a very high coverage where right now the average cover, well it changes. There's no average. But sometimes we can talk to 10,000 people. Companies that have about 40% visibility on the environment, it changes a lot. Okay, next thing is the oh one, one more thing again and if it's too much details then you can ignore it. We also have our own detection rules. Okay, what does that mean? We are pulling security alerts. So when you have a security tool that has a finding, we will take that alert and investigate. However, in addition we're also pulling all of the logs. For example, Okta is an identity to tool. Okay. And it's not a security tool. So there's no security alerts. But we have our own detection rules that we can run on the logs to find if there's been a suspicious activity and then we will investigate on it. Now this is something that is unique. I can't tell you that no one else is doing it, but very few companies are doing it. It's a very critical decision that we did early on to include detection. As I said, remember there's a four step cycle. So detection is the first Step. We wanted to cover the entire cycle, so we included detection. And right now we're seeing that 60% of all of our investigations result from detection. That means that companies that do not have that detection component are missing more than 50% of the things that they need to investigate.

**Kathy Lam:** So that leads to the extra backlogs. Okay, that makes sense.

**Maya Rotenberg:** No, it doesn't lead to extra backlogs. It leads to blind spots.

**Kathy Lam:** Blind spots. Okay.

**Maya Rotenberg:** You have the security alerts, you're investigating, everybody gets that, that's fine. But we're running detection on the logs of the tools itself. If you don't have the detection logs, you won't find something suspicious to investigate. So you will have less investigations, but you won't find things that you might need to know.

**Kathy Lam:** Okay, More false negatives.

**Maya Rotenberg:** Got it. Yeah. This is the system. I'll go quickly. You'll have it on the recording. Stop me if something doesn't make sense. So this is the data lake. This is just a place where we store all of the information we want all of the data on our system. We push all of the information to the data lake. Okay. A dedicated instance for every customer. Very secure. We save it for 90 days so we can have all of the capabilities to investigate something. Because many times when you have a breach, it didn't start in a second, there has been a suspicious activity for long. Then we have air. AIR is actually the investigation engine. Okay. It's made up of multiple of AI agents that are very specific. Every AI agents have a very specific core task. We did not, unlike many competitors, we did not build an AI agent who's a know it all. We have many specific AI agents and then we've built an AI infused orchestration layer that manages the different AI agents and it basically, you know, orchestrates over the entire information that runs between agents and agents and people. The AIR is pulling information from the data lake and also from Daylight Knowledge. Daylight Knowledge is a system where we are actually learning about the environment. We are learning about your business. What are the business critical assets? How does your employers look like? Do you have a lot of freelancers? What countries are suspicious, what countries are not? What time do you usually work? We learn about the different activities, so when something changes, we are able to learn it more. Context is coming both from pulling all of the data, but this is a very important part that many competitors have ignored and we see it as a very important part. Our security experts are contributing a lot to the knowledge by putting insights that they see as experts and infusing into doing daylight so we have a better understanding of the environment. And this is the ChatOps, this? Yes.

**Kathy Lam:** Is that per customer or is it tenant? Yes, that's tenant.

**Maya Rotenberg:** Specifically, every single customer has their own daylight knowledge.

**Kathy Lam:** Got it.

**Maya Rotenberg:** In addition, we have the chat ops. In many cases, sometimes you need to validate with the employee. For example, you saw someone from the Valdives entering a certain system and you know you don't have any full time employees in the Maldives, but maybe it's someone who, you know, took a vacation and decided that the Mrs. Works and you don't really know. So usually what our competitors are doing, they're reaching out to the customer and then the customer are reaching out to the employer. We have an automated system that is actually asking for validation. So the chat ops are talking to the employees directly. That's it. So a lot of different components within the Ajetic platform and then the third layer which is really important is the security experts. As I've mentioned several times, I think so far they're really different in their profile than others.

**Kathy Lam:** Great.

**Maya Rotenberg:** Anything that I forgot?

**Kathy Lam:** No. I think this is very impressive that you do this. Yeah.

**Maya Rotenberg:** Okay. This is usually what we're showing customers. An example. So this is a Wiz alert. Wiz is a cloud security tool and as you can see, many alerts are coming with no information. They're just coming with a log and a timestamp and a type of alert and that's it. So we're explaining them how we're actually going through and investigating, pulling, going to a cloudtrail system and pulling information according to the timestamp and then we're going into entry IDs like Okta identity system. We're pulling information based on data that we collected from the cloudtrail and then we're moving on and we're actually verifying the information, all done with less than a minute and providing a view that very few solutions out there right now are able to provide what changed in our customers. So this is a really important part, I think for the content, what I'm trying to do, and I think that I said it previously, I don't want to position us as an X percent better. It's about the transformation. And what do I mean by transformation? It means that once we are, you know, they are switching their solution or they're onboarding us. It impacts how the organization looks like they're changing roles and responsibility and that's because their soc, their security operation team or security team is starting to act in a very different way. Okay. I Gave three different examples. So Politrix act were not able to just handle all of their alerts. So for two years they ran just looking at their critical and high alerts and they were just, they thought that this is not something that is manageable. Within the three week POC we got them to a zero open threats. That means that their main security platforms did not have any alert breaklogs so they didn't need to make any hard decisions. They knew that they were actually reviewing all of the alerts. I can tell you that Qualtrics also made significant changes in the roles of responsibility because now their team has time to run actually projects to improve their posture. Lovable, lovable, needed to start at 24 7. It was a board level decision the CISO did not want to do, did not want to hire a classic MDR because he knew that he didn't have the team to support a classic mdr. They were thinking about maybe going to the in house route. Although it's a very small company and it's against their mindset to hire a lot of people. And within a month we were able to clean all of their systems again, zero open threats. We got them from zero to 24. 7 operational during the period of the POC. And Sixt Six is a 10,000 plus people organization. Both in Germany and the US they were a 25 year customer of MDRS and they're saying that for the first time they feel like they have a good understanding of what's going on. They understand where do they have blind spots, what is the coverage. They understand what are the most important things that they need to work on in order to improve their security. They did not have that understanding before because an MDR service wants to keep you as a service by making you think that you, you don't know your environment like they do. Questions?

**Kathy Lam:** Impressive. No, I don't think so. Ade, do you have any questions here?

**Ademilade Shodipe-Dosunmu:** Okay, yeah, I actually had one. Yes, sorry. I was interested in like the human in the loop model. Like how does your escalation system work? Is it for nuanced decisions? Is it a thing where your agents triage the issues, do the investigations at one point, at what point do they escalate to the human security experts?

**Maya Rotenberg:** Okay, so first of all, and this is something that is really important, I don't want us to talk about escalation process. The fact that our security experts are different and have a different profile, that means that also the role within the system is different in all other systems. Humans are there in order to do escalations. Our security experts are doing some escalations, but they're doing a very, a small part of their job is actually escalation. A larger part of their role is actually proactively improving the system by adding more knowledge and improving detection rules. So that's just a very high level. I don't want us to go, I want us to have a different language when we're talking about it than our competitors. So it's not just escalation. To your point, when we are starting, when we're onboarding a new customer, we are every verdict that is a certain severity level goes through our experts. And with time we are saying to the customer, okay, all of the alerts that are coming from Wiz and are this type of alert class, we have enough information to see that the AI is doing a good enough job. So we're not going to do that. And with time we're just kicking off more and more and more to being automated. And that means that whenever the system flags itself that its confidence is low. And, and our system is rating every single investigation with a confidence rating. So we're investigating everything that is above 50 that is lower than 60% confidence or 65% confidence changes from customer to customer. And also when we the system alerts that there might be a live breach, a live incident, in that scenario, our experts are immediately kicked in. That is also a big differentiating to others because once you have a live incident, that's when you call the CISO and you said there's a live incident. All hands on deck. And then you leave it because you're an MDR analyst in our case, because those are security experts and this is where they shine, then we are actually working and leading our customers through those incidents. And whenever we have an incident and we're getting permission from the customer, we are writing a report on it. We already have two reports live. We're writing like a blog article on it. And we had a third time that the customer approved an incident. So another blog post should be live tomorrow morning.

**Kathy Lam:** Awesome. You are going to the MAS slide. That. That's actually one of the questions I had.

**Maya Rotenberg:** Yeah. So this is the services that we have. Very important. I wrote it also in the report. It's very important that we position ourselves as a service security services company. Mdr, it is the leading product. We started from it because it's where the biggest pain lies. But there are others. There's threat hunting, which is a completely different service. It's actually, it's a training Exercise, you are saying, okay, I believe that there is an intruder, there is an attacker in the system. Now I'm going to have to look and find it. This is something that usually enterprises are doing every three months or so in order to find detection gaps in your system. Okay. Another one is phishing. So there are very good email security systems like Abnormal and Sublime that are doing amazing job, but they're pushing a lot of alerts, tons of alerts. And you need to have people investigating and responding to it. And this is where many small enterprise find it challenging. It's not a very complicated investigation, but it's massive amounts of alerts. This is usually where AI SoC tools shine because the investigation is not critical, but you have high quantity. So we're doing that as well. Data loss prevention, again, it's more like it's an exercise that companies usually do every six months. And if you don't have the security expertise you need to outsource it. An incident report, that's like an mayday service. You got breached. Now you need to hire an incident responder within hours. You need them in order to do the investigation to ensure that there's no live attack in the system right now and to write a full report about what happened so you can submit it to the regulations and the insurance. And there's a whole bureaucracy that comes with a breach. So that's something that we are not yet offering.

**Kathy Lam:** I have one question. You mentioned threat hunting. Phishing and DLP were coming soon, but they are already up, like available.

**Maya Rotenberg:** Yeah. So this is an ongoing discussion within our company. What happens is that threat hunting, we're Currently, we have two design partners, so it's not 100% live. It will be in a few weeks. And phishing and dlp, we are currently offering it to customers, but in a not full range. So we're covering 80% of what we want to cover in phishing. We are covering 50% of what we want to cover in DLP. There is a concern that when we're doing the sales deck that people will, if we say coming soon, they will say, oh my God, you're not covering phishing at all. So. But as a standalone service, it's not there yet.

**Kathy Lam:** Got it. And most people are using your MDR services and they're attaching the other additional ones.

**Maya Rotenberg:** Yes, all classic MDR providers are offering threat hunting and phishing and dlp. Some, not a lot. Some are offering incident response, but that's like the odd one. But everything else, people are accustomed to getting that from their MDR provider.

**Kathy Lam:** Excellent.

**Maya Rotenberg:** But you should know that there's also companies that are. That are an expert in threat hunting. And that's all they do, just threat hunting. So. So there are. The competition landscape is more complex than that.

**Kathy Lam:** Got it. Okay, this makes sense. Which slide has the most skeptical responses? When they look at it, they're like, oh, they question it a bit and they say this isn't for me or something?

**Maya Rotenberg:** Um, definitely the customers.

**Kathy Lam:** Oh, because they don't.

**Maya Rotenberg:** Definitely. They don't think again. And this is why. And I think that I wrote it in one of the comments. They're used to seeing marketing slides that are over promising. One of the things that you won't see here and that we should try to minimize in our content is other competitors are talking a lot about different metrics. MTTR mean time to respond, MTTA mean time to acknowledge escalation rate, stuff like that. They're seeing unbelievable percentage all over the place. They don't believe it. They even when you're talking to them about metrics, they don't want to. They're telling you immediately during the sales calls, let's not talk about metrics. I want to understand how you work. I want to see the architecture. I don't want to see bullshit. That's basically what they're saying. So they don't believe that the transformation. That's not a good setup for them.

**Kathy Lam:** Yeah, that makes sense.

**Maya Rotenberg:** Cool.

**Kathy Lam:** I think we're almost at time, but I think you've covered quite a lot. I do have some other questions after the slide that I will ask.

**Maya Rotenberg:** Okay, so this is just how we're doing the three week proof of concept, the POC first week. We're just doing monitoring. We're not providing service to the customer because we need to learn the system to understand what's suspicious, what's not. We are. The entire solution is based on context. Context based on the information from your system and the information that we build on your environment. What we call the daylight knowledge. It's a key component. We need a week to build it in order to start running. And then you get two weeks of full service with meetings twice a week and full report at the end. And this is where the conversation changes. And what you said, you have questions. This is actually the system and what customers are seeing. But do you want to ask questions?

**Kathy Lam:** I think one question I had is when a person gets an alert, like what does it look like? Does it look like it's here in the dashboard or is there another thing that shows?

**Maya Rotenberg:** So it's a case. But when, when the system gets an alert, they're not seeing it because you need to understand in the day you get 300, 400 alerts. So it's not like we're telling them every time we are sending them we are connected to their slack or teams or whatever the company uses and we are showing them, telling them that something in a high severity has come through or something like that. And we're sending links to the platform. Okay. And all of the information is within the platform. Okay, let me look for a good. No, I'll send you a demo, a video, a six minute video that actually shows you a good example because this is just a demo file without the investigation. I'll send you one real one so you can actually. So that they're going into the timeline and they can see all of the steps. This is what we got from Wiz, this is what we pulled from CrowdStrike. This is how we correlated the data and all of the information is, is within the system.

**Kathy Lam:** Got it. Let me see. I think. Oh, when, when you hear a customer object that they say they'll come back in a year is. Have, have you guys been able to respond with anything else that, that will get them to come back faster or. Actually no.

**Maya Rotenberg:** This is why we'll give you a try. Yeah. This is why we're starting with. The world is changing to make them understand that they're currently, they feel like they're making the safer choice but they're actually making a conscious decision to stay with a limited, limited coverage. So they're, it feels to them that they're doing the safe choice of staying with what they know, but they're actually choosing to be blind and we're focusing on that, we're explaining, we're trying to estimate if they've done a poc. That's great. Although we've never been in a problem of someone who did a poc, understood what is their situation and didn't move on. But in order to get people to do the poc, we're trying to estimate the coverage. We're trying to explain the level of risk from AI attacks that are getting more aggressive every single quarter. But right now it's very limited impact. I think right now many CISOs just feel overwhelmed because there's so much confusion when it comes to AI in security. And it feels to them like the safer choices do nothing, don't change anything. Who's going to blame you for sticking with IBM, right?

**Kathy Lam:** Yeah. But then yeah, you're sticking your head in the sand as part of the onboarding process. I know your system takes a week to kind of learn, but is there still a lot of input that the customer needs to give you in order to be able to train what to do after the system gets an alert or is this mostly from your team side?

**Maya Rotenberg:** So they have an onboarding checklist that they need to fill in and they need to go through it's 12 steps. Well, they need to tell us, connect us to the HR system so we can understand freelancers and employees. We need them to highlight what are the business critical assets. There's like a checklist that once we know that about the environment, it's enough. We usually for a poc we'll do a partial checklist because we don't want the customers to work hard in a poc. But then when we are onboarding them for real, then we'll ask them to complete the knowledge.

**Kathy Lam:** And is the same security team that works with them during the poc, the same team that continues with them after they renew?

**Maya Rotenberg:** There's only one security team. This is the structure and this is how it will remain. We believe that all of the personalization are coming from the system, not the security experts. The security experts are all very active on the platform. Slack teams, whatever it is, they're communicating but their identity doesn't really matter. Which is a big difference because with traditional MDR everybody wants a dedicated analyst so the analyst will learn them and will understand how to work with them. And for us everything is automated. We are learning. You know, okay, this company wants every, the CISO wants to get all of the alerts. This one, the it is more in control. We are learning the environment very, very quickly and we are responding to it. And so what we're actually educating our customers that it doesn't really matter who your security experts, it's one team for all.

**Kathy Lam:** Got it? One. One last question. Is your pricing model based on like an endpoint, an employee, like a flat fee? How, how does it work?

**Maya Rotenberg:** Okay.

**Kathy Lam:** And how does it compare with your competitors?

**Maya Rotenberg:** Yes, right now we're doing it per employee because it's very, very easy and very transparent. But we're not communicating it, we're not making it public. It's just a middle ground right now. It's not going to continue on that way. We'll probably move to a pricing that is more AI based but not right now. And pricing, look, at the end of the day we are significantly cheaper than other MDR solutions. But since we are not able to communicate our pricing, then Right now it's not something that I'm focusing on.

**Kathy Lam:** Got it. But during the sales process, they'll talk about how it's just a more efficient process than Expel and Reliant Quest.

**Maya Rotenberg:** And more efficient in what? The outcomes or the pricing? I didn't understand both.

**Kathy Lam:** Like, because we're. We're not. I think during the sales process, when the customer asks about pricing, they are.

**Maya Rotenberg:** Like the answer that they will get. The answer they will get vary from customer to customer to. The majority will say it's about employees. But sometimes we'll see it's a very complicated system or a very simple system and will adjust accordingly.

**Kathy Lam:** Got it. Okay. We'll leave that often not. And be vague about that. I think once we see a.

**Maya Rotenberg:** Like, we could. I have no problem saying that because we have a different architecture, then we're not as expensive or significantly less expensive than the others. But yeah, right now we can go into further details.

**Kathy Lam:** Got it. I think you answered most of the questions. There was one thing I wanted to ask you later, which was to. If you have like a recording of like, how do you upload blogs to your cms? But we can do that later. Or like now if you want, I.

**Maya Rotenberg:** Can record it and share it.

**Kathy Lam:** Okay, perfect. And you.

**Maya Rotenberg:** So I owe you two videos. One is about the investigation within the system. How does it look like. And the other one is for the webflow.

**Kathy Lam:** Perfect. Yeah, we're very familiar with webflow. And then this last question. Sorry. We have a way to generate blog images that will be like. You want that, right? Okay, we'll set up the workflow to do that.

**Maya Rotenberg:** I did upload style guides. Yes. But it's slightly outdated.

**Kathy Lam:** Okay. I noticed it was left out. Yes.

**Maya Rotenberg:** Let me upload something that is more up to date.

**Kathy Lam:** Okay, perfect. And then. Yeah, this is perfect. Do you think it would be worthwhile for us to have the slides? Or I'll just get it from the video.

**Maya Rotenberg:** Sure. I can share with you the slides. No problem.

**Kathy Lam:** Okay, great. Thanks so much. Maya was great.

**Maya Rotenberg:** Thank you. Bye.

**Kathy Lam:** Bye.
