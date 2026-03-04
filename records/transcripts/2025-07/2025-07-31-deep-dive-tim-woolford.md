# Deep Dive (Tim Woolford)

<metadata>
date: 2025-07-31
time: 17:43 UTC
duration: 41 minutes
organizer: george@growthx.ai
participants: George Haikal, Aida Knezevic, Sydney Go, Tim Woolford
fathom_recording_id: 77771957
fathom_url: https://fathom.video/calls/368593454
share_url: https://fathom.video/share/Pxq9p3KyyW-CgLQWDCWBgN4NfzNeKxar
source: fathom
enriched_on: 2026-03-03 17:30 UTC
</metadata>

---

## Summary

Deep dive with Tim Woolford, Product Marketing lead at SentinelOne, to inform content strategy and enrich workflows for producing cybersecurity content.

---

## Context

This deep dive was conducted with Tim Woolford, Product Marketing lead at SentinelOne (a NASDAQ-listed cybersecurity company). Tim leads SentinelOne's product marketing function, overseeing messaging, positioning, pricing, and sales enablement—he's been with SentinelOne for nearly 2.5 years. GrowthX is developing content strategy around SentinelOne's Singularity Platform and AI-driven security capabilities to inform a multi-channel content effort. The meeting served as an expert research session to deepen GrowthX's understanding of SentinelOne's product architecture, AI differentiators (particularly behavioral AI and Purple AI), competitive positioning against CrowdStrike, and use cases—directly informing artifact-building and future content production.

---

## Relevance

**To GrowthX Delivery:**
- Behavioral AI is a critical messaging pillar for SentinelOne content—detection at both device layer (agent-based) and platform layer (identity/user anomaly detection) differentiates from reactive competitors
- Platform architecture (central OCSF data lake + Purple AI + hyper-automation) is complex but sellable: position as unified (not "duct-taped") solution vs. competitors who claim single pane of glass but integrate via bubbled gum and duct tape
- MITRE evaluation results are potent proof points: 12 alerts vs. Palo Alto's 178,000 (88% fewer alerts) and 5 consecutive years as Gartner MQ leader for Endpoint
- Content should emphasize: fastest threat detection/response, cost-effectiveness vs. Splunk and CrowdStrike, ease of implementation, open ecosystem
- Concrete use case example from transcript: detecting data exfiltration via impossible travel + behavioral baselines (e.g., "user sending petabytes to Uzbekistan at 3am") illustrates AI value for SOC teams

**To CheckThat:**
- SentinelOne's AI positioning differs from GenAI buzzword marketing—Tim emphasized 10+ years of AI/ML in legacy AV, first to launch generative AI SOC analyst (Purple AI) before any competitor
- Purple AI is 6-12 months ahead of CrowdStrike's Charlotte AI in functionality (Charlotte launched as vaporware, expensive, hard to use, but improving rapidly)
- Autonomous SOC philosophy: humans always in the loop, customizable automation, control in customer hands (direct response to CrowdStrike kernel integration risks post-outage)

**To GrowthX Business Development:**
- Expansion opportunity: SentinelOne considering AI pricing index project (currently paused internally but mentioned as "programmatic" item after current engagement)
- Health signal: deep willingness to share materials (videos, demo assets, TCO reports, behavioral AI docs, zero-day detection stories) and follow-up on knowledge gaps (delegating cloud security details to team member)
- Account structure: Tim is key expert, but George Haikal (organizer) managing broader engagement with multiple contacts at SentinelOne (Brian the CMO, others); Aida/Sydney as GrowthX leads

---

## Overview

- SentinelOne's Singularity Platform is an AI-driven cybersecurity solution that unifies defense, outpaces threats, and enhances analyst capabilities
- Behavioral AI is a key differentiator, allowing for proactive threat detection at both device and platform levels
- The platform consolidates tools, reduces alert fatigue (88% fewer alerts than competitors), and offers a single, unified console for comprehensive security management
- SentinelOne's AI capabilities, including Purple AI (Gen AI SOC analyst), set it apart from competitors like CrowdStrike's Charlotte AI

---

## Key Topics

### SentinelOne Platform Overview

  - Singularity Platform: AI-driven cybersecurity solution
  - Addresses key challenges: fragmented security landscape, evolving adversaries, resource constraints
  - Unifies defense: integrates 10-40+ disparate security tools into one platform
  - AI-driven: proactive threat detection and response
  - Enhances analyst capabilities: AI handles heavy lifting, making security teams more effective

### Behavioral AI and Threat Detection

  - Built into the agent at device layer and at platform level
  - Detects anomalous behavior for users, devices, and identities
  - Example: Flags unusual data transfers or impossible travel scenarios
  - Proactive approach: Can block and remediate threats without needing platform connection
  - Customizable: Customers can adjust automation levels and control logic

### Platform Architecture

  - Central data lake using OCSF for ingestion and normalization
  - Native data sources: Cloud, Endpoint, Identity
  - Ingests competitor/partner logs and alert data
  - Purple AI and hyper-automation layer for workflow automation
  - Provides SIM, XDR, EDR, Cloud, and EPP capabilities

### Key Differentiators

  - Single, unified console and data lake (not "duct-taped" solutions)
  - AI infusion throughout the platform
  - Industry-leading Cloud Workload Protection Platform (CWPP)
  - One-click rollback capability
  - Cost-effective and easy to implement
  - Open ecosystem for integration

### Product Highlights

  - Endpoint/EDR: Highest accuracy, least noise, 88% fewer alerts than competitors
  - Cloud Security (CNAP): Comprehensive risk management and exposure analysis across multi-cloud environments
  - SIM: AI-driven real-time detection, much cheaper and easier to use than Splunk

### Competitive Landscape

  - Main competitor: CrowdStrike
  - SentinelOne's Purple AI currently 6-12 months ahead of CrowdStrike's Charlotte AI in functionality
  - Charlotte AI improving rapidly, but started as "vaporware" and had initial usability issues

---

## Action Items

**Tim Woolford (SentinelOne)**
- Send over assets on LLM attacks (WormGPT, GhostGPT) specifically related to SentinelOne's AI cybersecurity platform

- Forward additional information on Behavioral AI, particularly around the agent

- Share videos and demo assets that walk through examples of threat detection and response process

- Provide TCO (Total Cost of Ownership) reports from third parties showing why SentinelOne is cheaper than competitors

- Send more detailed information on SentinelOne's cloud security offerings

- Get someone else to answer question about how SentinelOne's behavioral AI detects zero-day threats, provide examples/stories

---

## Transcript
**George Haikal:** Hey.

**George Haikal:** Hey, sorry, when I'm on a different screen, I can't see the Zoom call, so whenever anyone says, yeah, scares me a bit.

**Aida Knezevic:** How are you?

**Aida Knezevic:** Great.

**Aida Knezevic:** We just got a really great call without...

**George Haikal:** Reach.

**George Haikal:** They are so nice, so lovely to work with.

**Aida Knezevic:** They really are perfect, perfect, perfect.

**George Haikal:** I feel like you and Hadassah are pretty similar, like both really smart, but also super personable and like to the point as well and just know what needs to be done and how to handle it.

**Aida Knezevic:** So yeah.

**Aida Knezevic:** Yeah, yeah.

**Aida Knezevic:** She's great.

**Aida Knezevic:** And it's also nice that we work with like two people.

**Aida Knezevic:** So they're like the main points of contact and it's like everything goes through them.

**Aida Knezevic:** So it's not, there's not a lot of cooks in the kitchen.

**George Haikal:** Nice.

**George Haikal:** Before Tim jumps on, I pinned you guys on Slack for metronome.

**George Haikal:** Just if you could send me like anything else you guys have been doing, I'm putting together the package, like shaping the lanes that we've actually done, what we're doing right now and like what we will continue to do so we can show them all the work and then pitch them on the pricing accordingly.

**George Haikal:** Because I don't want all the different stuff that you're doing to like, you know, just be looped into the regular stuff, but.

**George Haikal:** We're going above and beyond in a ton of ways.

**Sydney Arin Go:** I'll send you, I can send you everything on the editorial side, but anything outside of that, like, I know Aida were doing a custom pipeline for them, or that was in the works at some point, or will be in the works at some point.

**Aida Knezevic:** I don't know.

**Sydney Arin Go:** Am I imagining things?

**Sydney Arin Go:** I think there was something for Metro.

**Sydney Arin Go:** I'll back read and see, but so I can do the editorial, and if there's anything else in the pipeline, like the video stuff that I'm missing, just fill in there.

**Aida Knezevic:** Yeah, they wanted to do also an AI pricing index, but that kind of got the one inside.

**Aida Knezevic:** Yeah, yeah, yeah.

**Aida Knezevic:** So that's, like, one thing that's, like, programmatic that they might want to do after this.

**George Haikal:** Is there any more context for that, or?

**Aida Knezevic:** You might find it in Notion.

**George Haikal:** And it's basically, like, oh, that's what Chang was working on, right?

**Aida Knezevic:** Yes.

**Aida Knezevic:** So she was, to do, like, a bunch of pages with different.

**Aida Knezevic:** From pricing of different AI companies.

**George Haikal:** So that's basically the idea.

**George Haikal:** I just had to go back in my brain from the kickoff call of Maddie mentioning that Chang, who wasn't on the call, was working on that.

**George Haikal:** That was crazy.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** A lot of information.

**George Haikal:** Yeah.

**George Haikal:** Hopefully, Tim joins.

**George Haikal:** I confirmed and sent the agenda over email to him an hour ago.

**George Haikal:** But yeah, for these, Aida, I saw your agenda.

**George Haikal:** I'm also not an expert.

**George Haikal:** And so for me, I always start with more broad questions, honestly, because I can't even confirm if they're super specific, but they're accurate.

**George Haikal:** So on the outreach call, for example, Sydney and I, we started super broad and let them just run through the deck that they already used.

**Aida Knezevic:** And then we just dive in with questions.

**George Haikal:** Just to make sure whatever you're trying to figure out.

**George Haikal:** Yeah.

**George Haikal:** That has been working the best.

**Aida Knezevic:** Okay.

**George Haikal:** So far.

**George Haikal:** We'll give them a couple more minutes then.

**George Haikal:** I'll get out of here.

**George Haikal:** Is there anything else you guys need?

**Aida Knezevic:** No, I don't think so.

**George Haikal:** Tavern, Aida.

**George Haikal:** I did the kickoff stuff, followed up.

**George Haikal:** I'm getting on a call with two of their customers.

**George Haikal:** It's very similar to Monograph, and I know Joe is taking on, like, the initial stab, or added to the artifact, and Joe's taking the initial stab.

**George Haikal:** But that one seems pretty purely editorial, so I'll catch up with you after.

**Aida Knezevic:** Okay.

**George Haikal:** Hey, Tim, how's it going?

**Tim Woolford:** Good, how are you?

**Tim Woolford:** Apologies for being a little bit late.

**George Haikal:** No problem at all.

**George Haikal:** We get it.

**George Haikal:** We get it.

**George Haikal:** We're glad we found some time.

**George Haikal:** I feel like every person we've talked to up until now has mentioned you, obviously in a positive light, Craig and a few others.

**George Haikal:** So we're excited to get all that expertise out of your brain then.

**Tim Woolford:** Well, hopefully I can deliver.

**George Haikal:** Awesome.

**George Haikal:** So just to let you know, I have to jump in about five.

**George Haikal:** Unfortunately, Tommy, I have another call.

**George Haikal:** But Aida and Sydney are the leads on the account anyway, so they're much more important than me here.

**George Haikal:** I guess what would be helpful is maybe a quick intro from you just so we better understand what you do high level.

**George Haikal:** And then we have an agenda with questions we can start super broad.

**George Haikal:** The purpose of this meeting is just we do deep dives with all the experts because it helps inform our content strategy.

**George Haikal:** And we build these artifacts that enrich our workflows to produce the final output, which is content, right?

**George Haikal:** So if you think of the product layer, the more expertise we can get, the more specific we can get on use cases, how the product solves it, AI, all of that, the better our content will be at the steps following.

**George Haikal:** And so we do that with everything.

**George Haikal:** Voice, style, tone, brain guidelines, product, et cetera.

**George Haikal:** So the point of this is super conversational, brain dump on us.

**George Haikal:** And yeah.

**Tim Woolford:** Sounds good.

**Tim Woolford:** Where do you want to start?

**George Haikal:** First, like high level, how long you've been there, what you usually do, and like what your main priorities and focuses are would be great.

**Tim Woolford:** Yeah.

**Tim Woolford:** So I lead the product marketing team as a function.

**Tim Woolford:** We handle all the sort of messaging, positioning, pricing, skewing, naming, and then the sort of bill of materials around any new product, new feature, or maintaining those as things mature.

**Tim Woolford:** And we also do sales enablement, a lot of stuff around events.

**Tim Woolford:** But the big sort of core thing and probably most relevant here is sort of messaging, positioning, and a lot of the documentation.

**Tim Woolford:** And I've been here for almost two and a half years, which makes me a grizzled veteran in the scope of SentinelOne people.

**George Haikal:** Grizzled veteran, I love it.

**George Haikal:** Honestly, for the sake of the flow of conversation, I'm going to drop two things.

**George Haikal:** Here is the notion that you should have access to.

**George Haikal:** Oh, by the way, Tim, I know we've had back and forth.

**George Haikal:** Do you have access to our Slack, our group Slack channel?

**Tim Woolford:** I don't know.

**Tim Woolford:** I'm not sure.

**Tim Woolford:** It's possible I haven't added and just haven't seen it.

**Tim Woolford:** That's all right.

**Tim Woolford:** We'll make sure you have access.

**George Haikal:** Happy to.

**George Haikal:** That's fine.

**George Haikal:** No problem.

**George Haikal:** We'll make sure you have access to the agenda.

**George Haikal:** then before I jump, any materials that we talked about today would be fantastic to have.

**George Haikal:** And yeah, we usually start with, like, if you have a deck that you run people through, generally.

**George Haikal:** It's fine.

**George Haikal:** then Aida and Sydney can take it from here and jump in with questions.

**George Haikal:** know we have a ton for you.

**George Haikal:** So with that, it was a good, very quick intro, and it was good to meet you, but I'm going to hop off and let them handle it.

**Tim Woolford:** Cool.

**George Haikal:** Sounds good.

**George Haikal:** Thank you, George.

**Aida Knezevic:** See you.

**Aida Knezevic:** Yeah.

**George Haikal:** Aida, I'm going to make you host, too.

**Aida Knezevic:** Oh, yeah.

**Aida Knezevic:** That's great.

**Aida Knezevic:** Thank you.

**Aida Knezevic:** All right.

**Aida Knezevic:** Great.

**Aida Knezevic:** Well, it's great to meet you, Tim.

**Aida Knezevic:** So, like George said, do you have a deck that you usually run people through when it comes to the product?

**Tim Woolford:** You can go ahead and share your screen, and we'll have the recording.

**Tim Woolford:** Yeah.

**Tim Woolford:** I can do this in anything from four or five minutes to, like, two days.

**Aida Knezevic:** How much time do you want me to spend on this?

**Aida Knezevic:** Let's do 20 minutes to start, and then we can, like, we can ask, like, follow-up questions as you're going through it.

**Tim Woolford:** Yeah.

**Tim Woolford:** Sounds good.

**Tim Woolford:** Are you seeing this?

**Aida Knezevic:** Can you me okay?

**Aida Knezevic:** Yeah.

**Tim Woolford:** Cool.

**Tim Woolford:** Cool.

**Tim Woolford:** All right.

**Tim Woolford:** So we are SentinelOne.

**Tim Woolford:** We have a platform called the Singularity Platform, which is built in AI, and we sort of fondly refer to it as our AI cybersecurity platform.

**Tim Woolford:** You know, when you think about cybersecurity, there's some key challenges that a lot of customers and users the globe over all experience.

**Tim Woolford:** Some of these will be pretty well understood, and some of these are a little unique.

**Tim Woolford:** You know, security is quite fragmented.

**Tim Woolford:** It can commonly be made up of anywhere from a dozen to four dozen or more disparate and separate tools that are all kind of used together in parallel by an organization to keep their organization safe.

**Tim Woolford:** Obviously, when you have that many different tools, some of them may talk to each other, some of them may not, but it's just a monstrous challenge to keep all those things together to manage them.

**Tim Woolford:** And, of course...

**Tim Woolford:** Ultimately, things are going to fall through the cracks, which are exactly what adversaries are looking to exploit.

**Tim Woolford:** Speaking of adversaries, these are constantly evolving.

**Tim Woolford:** Obviously, as long as cybercrime remains profitable, then cybercriminals will endeavor to profit from it.

**Tim Woolford:** So the bad guys are still bad.

**Tim Woolford:** They're constantly evolving.

**Tim Woolford:** They're now using AI, just like we are using AI.

**Tim Woolford:** I might use it to make funny pictures of cats.

**Tim Woolford:** They're using it to steal your bank account details.

**Tim Woolford:** And so the attack surface is growing ever complicated.

**Tim Woolford:** They are getting better and faster and more well-funded and constantly changing how they come after what's important.

**Tim Woolford:** Ultimately, resource constraint is very real.

**Tim Woolford:** It's very real for every company with economic headwinds and even with economic tailwinds.

**Tim Woolford:** Having enough resource, be it time, money, or people, is a constant challenge for IT teams and certainly for security.

**Tim Woolford:** You often hear about a talent gap with, you know, sort of being able to attract and retain and pay enough for experienced professionals in the realm of cybersecurity.

**Tim Woolford:** Makes sense there?

**Tim Woolford:** Any questions?

**Tim Woolford:** Do you want to ask questions throughout or do you want to do them at the end?

**Aida Knezevic:** We can ask questions throughout.

**Aida Knezevic:** I think that'd be a good idea because we might forget.

**Aida Knezevic:** So, you mentioned a little bit about the resource constraints.

**Aida Knezevic:** I would love to have more details about the evolving adversaries.

**Aida Knezevic:** So, specific maybe threats that are emerging or that are becoming more and more difficult to contain.

**Tim Woolford:** Yeah.

**Tim Woolford:** So, you know, ransomware is always a hot topic.

**Tim Woolford:** Ransomware is always asked about by customers of any level of experience.

**Tim Woolford:** It gets the most coverage in the news and it probably is the most costly.

**Tim Woolford:** So, you always see ransomware come up and ransomware...

**Tim Woolford:** There is an umbrella term, what it actually means and how it works can be, you manner of things.

**Tim Woolford:** You are seeing a lot in the realm of social engineering.

**Tim Woolford:** You see a lot of people, a lot of attacks where the person is targeted as the entry point into an organization.

**Tim Woolford:** So, you know, endpoint, the physical device used to typically be where attacks would start and now it starts with identity and not just identity, but how a human interacts with an asset.

**Tim Woolford:** You know, you see a lot of, it was MGM in Vegas where they pretended to be a help desk person and came after the employee and found access that way.

**Tim Woolford:** You see a lot of infiltration where the targeted asset or resource is not the intended target, but it's a stepping stone to get there.

**Tim Woolford:** You see a lot of multi-pronged attacks, a lot of lateral movement.

**Tim Woolford:** But the evolution here is kind of away from the asset and more towards the person or the...

**Tim Woolford:** Person's interaction as a starting point.

**Tim Woolford:** You're also seeing AI start to do a lot of that heavy lifting as well.

**Tim Woolford:** It's quicker and easier and cheaper to create these tools to find ways to exploit just through rapid access to data, rapid access to processing.

**Tim Woolford:** Does that help?

**Aida Knezevic:** Yeah, absolutely.

**Sydney Arin Go:** Thanks.

**Sydney Arin Go:** I'm sorry.

**Sydney Arin Go:** Can I ask a follow-up question there?

**Sydney Arin Go:** I think you were talking a lot about account takeovers and those kinds of attacks.

**Sydney Arin Go:** But, so one of the things I've been seeing a lot recently is stuff on like WormGPT and GhostGPT.

**Sydney Arin Go:** Is there any way that SentinelOne's AI cybersecurity platform, like how do you want us to talk about how the AI cybersecurity platform handles those attacks?

**Tim Woolford:** Handles what, sorry?

**Sydney Arin Go:** The like LLM attacks that are coming out, like WormGPT, GhostGPT, those kind of things.

**Tim Woolford:** Yeah, it's, oh, can spend all day on this.

**Tim Woolford:** There's a couple of assets kind of specific.

**Tim Woolford:** In this space around LLM attacks that I'll attach and fought over afterwards.

**Tim Woolford:** But a lot of the, ultimately, once it touches something, the logic is kind of the same.

**Tim Woolford:** It's still going to be blocked and tackled.

**Tim Woolford:** Really, it still comes back to the entry point.

**Tim Woolford:** It still comes back to the logic of what it's trying to do.

**Tim Woolford:** And yeah, some of those are novel.

**Tim Woolford:** Some of those get weird.

**Tim Woolford:** But I think for us, the differentiator we have is being agent-based.

**Tim Woolford:** And so somewhere like a Microsoft, you're, and I can say this because I worked there for a decade, but you are waiting for something to get in a little bit before you can really block it.

**Tim Woolford:** With the agent approach that we use, you pick it up right as it knocks on the door.

**Tim Woolford:** So any odd behavior, any sort of sniffing that those things are doing, you tend to see, as opposed to others which are much more reactive.

**Tim Woolford:** So to answer your question, I would say...

**Tim Woolford:** You know, we fight AI with AI, and the nature of our architecture means we're extremely proactive as opposed to not.

**Tim Woolford:** And like I said, Sydney, I'll forward over some of the stuff that's specifically about that.

**Sydney Arin Go:** Thank you.

**Tim Woolford:** Yeah.

**Aida Knezevic:** Can you go on?

**Aida Knezevic:** Mm-hmm.

**Tim Woolford:** Cool.

**Tim Woolford:** So this one, this stuff's all pretty high level, but this is sort of what we share a lot with customers too, especially at the sort of initial kind of stage, is what does, you how do we solve those problems?

**Tim Woolford:** What does our platform allow you to do?

**Tim Woolford:** Well, it allows you to unify defense.

**Tim Woolford:** So you may have 10, 20, 30, 40 different platforms or point products within a solution.

**Tim Woolford:** So here is a platform that will pull all of those together.

**Tim Woolford:** It's open, it's unified, it can ingest everything, it can detect on ingestion, and it can store and retain things for as long as you need to.

**Tim Woolford:** All the data is always.

**Tim Woolford:** So everything's always in one place, ready to be queried or used, unlike a lot of other tools.

**Tim Woolford:** So great sort of umbrella back end to unify and integrate and pull everything together.

**Tim Woolford:** Ultimately, like we were just discussing, the intention there is to outpace that.

**Tim Woolford:** So the whole sort of proactive versus reactive, you know, moving towards automating as much as we can.

**Tim Woolford:** There's a careful differentiator here, too, of, you know, you always see, oh, AI is coming for our jobs.

**Tim Woolford:** That's a scary thing.

**Tim Woolford:** That's something to be avoided talking about.

**Tim Woolford:** We talk about it in the sense here of you already didn't have enough people to do these jobs.

**Tim Woolford:** Let AI help the ones you have to be more effective and more productive.

**Tim Woolford:** So it's definitely not an AI coming for the jobs.

**Tim Woolford:** You can't fire your security analysts because of this, but you can make them a whole lot better, which sort of dovetails into that last point.

**Tim Woolford:** You know, enhance your analysts.

**Tim Woolford:** Let Gen AI, let Agentec AI handle the heavy lifting.

**Tim Woolford:** Make every analyst.

**Tim Woolford:** faster and better at remediating threats.

**Tim Woolford:** So we sort of lean on those three pillars of, you know, we're faster, we're cheaper in the right scenario, and we simply have better security.

**Tim Woolford:** Keep going?

**Aida Knezevic:** Yep.

**Tim Woolford:** Just a little bit about sort of where we've come from, where we're going.

**Tim Woolford:** We lead with AI.

**Tim Woolford:** It's in our DNA.

**Tim Woolford:** You know, AI isn't just a buzzword for us.

**Tim Woolford:** We've been sort of using AI for, you know, since we began, just over 10 or 12 years ago.

**Tim Woolford:** So, you know, we changed and reinvented the legacy AV space, obviously very, very well known for Endpoint in the way we've used AI and ML to build out our behavior analytics and agent analytics.

**Tim Woolford:** Industry leader in AI for some time now.

**Tim Woolford:** We were the first in the cybersecurity space to announce and launch a generative AI SOC analyst, which obviously is the purple product.

**Tim Woolford:** to build And we...

**Tim Woolford:** We are well along our way to building out this journey of the Autonomous SOC.

**Tim Woolford:** And now if we take a look at the platform, you know, this, and we could spend a lot of time on this too, so please ask questions, but, you know, underneath it all, there's a central data lake.

**Tim Woolford:** The data lake is built using OCSF, so we ingest and normalize and hot store and retain pretty much anything you want to throw at it.

**Tim Woolford:** So underneath there, you see the native data sources such as Cloud, Endpoint, and Identity that come from, you know, our native sort of product offerings, but also ingesting competitor or partner logs and alert data into that data lake as well.

**Tim Woolford:** Over the top, we run Purple AI and hyper-automation, so automating the workflows in and out and through.

**Tim Woolford:** Purple, which obviously gives you SIM and XDR, EDR, Cloud, and EPP kind of capabilities on top of that.

**Tim Woolford:** Anything you'd want to dive deeper into sort of on the architecture of the platform?

**Aida Knezevic:** I would love to.

**Aida Knezevic:** We were talking to Brian, your CMO, earlier this week, and we would love to hear more about behavioral AI because he highlighted that as one of, like, the standout characteristics that we should talk about in content.

**Tim Woolford:** Okay.

**Tim Woolford:** Did he give any examples or any sort of reasons why he thought that?

**Aida Knezevic:** Just because it allows the platform to detect threats more efficiently just based on, you know, suspect behavior by users.

**Tim Woolford:** Yeah, in that realm and with that example, yeah, it pretty much is as straightforward as that.

**Tim Woolford:** but the...

**Tim Woolford:** There is behavioral AI built into the agent.

**Tim Woolford:** So at the device layer, you're going to see, is this behavior weird?

**Tim Woolford:** At the platform layer, you're going to see all the things you'd expect, like impossible travel, all the logic around exactly what it sounds like.

**Tim Woolford:** Is the behavior what I would expect for this person and this user, this identity, this device, and the way it interacts with other resources?

**Tim Woolford:** I think we do have a pretty compelling story there.

**Tim Woolford:** The agent element makes it super interesting.

**Tim Woolford:** And just sort of the agent being online or offline, having the ability to manage, block, remediate without needing the platform to necessarily be able to do that.

**Tim Woolford:** What else?

**Tim Woolford:** There's also some stuff on the BAI side that I can send over as well, particularly around the agent.

**Tim Woolford:** So, um, I don't I don't know what it to sort of go.

**Tim Woolford:** Go into it in that regard, but certainly more I can share.

**Aida Knezevic:** Yeah, just a quick follow-up.

**Aida Knezevic:** Do you ever get customers that are maybe concerned or have additional questions around the agents and sort of autonomous security?

**Aida Knezevic:** Do they ever want to know, okay, when does the autonomous detection loop a human in?

**Aida Knezevic:** Is there a specific time when that happens?

**Tim Woolford:** Yes, absolutely.

**Tim Woolford:** And I'll pull those apart a little bit because you mentioned the agent on its own.

**Tim Woolford:** The conversation around the agent obviously happens with the more technical, like a practitioner audience in general.

**Tim Woolford:** But specifically after, you know, the CrowdStrike incident, which was along those lines, we had a lot more conversations around how our agent is built.

**Tim Woolford:** It's relative.

**Tim Woolford:** It's

**Tim Woolford:** How it doesn't, you know, it's not as deeply integrated with the kernel.

**Tim Woolford:** Those kind of conversations and questions come up a lot.

**Tim Woolford:** I think it's mostly because of the nervousness around what CrowdStrike did.

**Tim Woolford:** We talk a lot about our testing, you know, making sure everything is properly vetted before it's pushed out.

**Tim Woolford:** To the second part of your question, a lot of that comes back to control, obviously.

**Tim Woolford:** So we push very hard that we leave control in the customer hands.

**Tim Woolford:** Like, you can stop updates, you can do things when they're convenient, you can roll back a lot easier than some of our competitors.

**Tim Woolford:** But also, to your point around that autonomous piece, it's fairly basic when you get set up.

**Tim Woolford:** And you can customize it, you can stop it, you can change the logic, you can build in the steps you want.

**Tim Woolford:** So it's a great question because it actually comes up a lot.

**Tim Woolford:** Like, a lot of people are nervous about, you know, what are you doing automatically versus what?

**Tim Woolford:** What do I need to do?

**Tim Woolford:** And our intention with the autonomous SOC is that the human is never, ever removed from the equation.

**Tim Woolford:** It's just what do they see?

**Tim Woolford:** What happens before it gets to the human?

**Tim Woolford:** And then what does it actually have control over?

**Aida Knezevic:** And all of those things are dictated by the customer rather than by us.

**Aida Knezevic:** Okay.

**Aida Knezevic:** That's great to know.

**Tim Woolford:** Thanks.

**Tim Woolford:** Yeah.

**Sydney Arin Go:** Can I?

**Tim Woolford:** Yeah.

**Sydney Arin Go:** So for, like, content purposes, can I ask you to tell us, like, how the step-by-step of how this works?

**Sydney Arin Go:** Like, when a threat is detected and all of that from, like, how does the behavioral AI baseline the behavior to how does it remove false positives and all of that?

**Sydney Arin Go:** Or would that take too much time?

**Tim Woolford:** It might take a bit of time, but let me try and do it quickly using this.

**Tim Woolford:** So if you had...

**Tim Woolford:** And try and use something that wouldn't just be automatically blocked.

**Tim Woolford:** If you had a person, and I always say this with a customer too, like people are your greatest, people are your greatest resource, but people are also your biggest liability.

**Tim Woolford:** And so say I'm cooking dinner and my daughter's running around making tons of noise like she always is and I click on the wrong link.

**Tim Woolford:** Cool, you've now breached me, the user, through email, you now have access to my credentials, you're now effectively a legitimate thing in the tool.

**Tim Woolford:** If you now start sending petabytes of data to Uzbekistan at three o'clock in the morning, the system's going to be that's odd behavior for user equals Tim Woolford, that doesn't make any sense.

**Tim Woolford:** So, you know, pretty cliche example, but pretty clear flag there.

**Tim Woolford:** You know, false positives will happen at the platform there.

**Tim Woolford:** And again, there's always going to be false positives.

**Tim Woolford:** It's part of the whole thing, but, you know, that kind of logic and reduction will...

**Tim Woolford:** will happen at the dashboard in the analytics lab, but to keep with my example, you know, you've got a multilateral problem where my identity's been breached.

**Tim Woolford:** If it recognizes that odd behavior, it's going to block everything, remediate, push back to MFA, reset password, you know, repair device, that kind of thing.

**Tim Woolford:** But say it kept going, you've now got a problem in endpoint email and ID.

**Tim Woolford:** Data Lake is going to piece all those things together.

**Tim Woolford:** Instead of seeing three separate alerts, you're going to see one incident because they're all related, so it's correlated them for you.

**Tim Woolford:** That is a function of SIM.

**Tim Woolford:** Having that visibility and dashboarding, that is a function of SIM.

**Tim Woolford:** Purple over the top is going to summarize it.

**Tim Woolford:** It's going to say, hey, SOC analyst, big problem with Tim.

**Tim Woolford:** This is what's happened.

**Tim Woolford:** These are the devices effective.

**Tim Woolford:** I've automatically blocked them.

**Tim Woolford:** Here are the next steps that you need to take.

**Tim Woolford:** Here are some query questions you could ask.

**Tim Woolford:** Hyper automation will probably already have those.

**Tim Woolford:** Types of workloads built out in terms of remediation and fixing stuff, so it would just be a case of execution, so you sort of see it coming all the way from the log data, I don't know if you can see my cursor or not, you know, up into the data lake, you've seen it, you know, having those SIM and XDR capabilities using PURPLE, using automation, and ultimately back to, you know, back to those devices to fix them up.

**Tim Woolford:** Does that kind of answer your question, or is that way off base?

**Sydney Arin Go:** Yeah, yeah, no, that's perfect, it's just thinking about how we can talk about SentinelOne's tool and how it all works with the whole system, really, and giving more clarity on how AI actually helps.

**Tim Woolford:** Yeah, and we have a couple of videos and sort of some demo assets that walk through examples like that, and I'm more than happy to share those as well.

**Tim Woolford:** Yeah.

**Tim Woolford:** Keep going?

**Aida Knezevic:** Mm-hmm.

**Tim Woolford:** Cool, so, yeah, customers.

**Tim Woolford:** So we just have a couple of sort of quotes sprinkled through these.

**Tim Woolford:** This starts getting just kind of a double click into some of the big kind of differentiators for the platform.

**Tim Woolford:** And this is a collection of slides that I usually pick three or four of them, and that's my customer conversation.

**Tim Woolford:** I would hope that no one would ever sit here and go through all of them, but I'm sure they do.

**Tim Woolford:** So when you think about the platform, just kind of coming back to those big problems we addressed at the beginning, it is one console.

**Tim Woolford:** That's a big deal.

**Tim Woolford:** A lot of vendors claim they have one dashboard, one console, and then when you double click or look behind the scenes, it's actually 50 different things stuck together with duct tape and bubble gum.

**Tim Woolford:** This is one platform, one console, one data lake.

**Tim Woolford:** It's protection that works.

**Tim Woolford:** Customers believe it.

**Tim Woolford:** The analysts believe it, and we'll look at that in a second.

**Tim Woolford:** Like we talked about, AI is infused in everything.

**Tim Woolford:** We have an industry-leading CWPP or CNET platform.

**Tim Woolford:** We have one-click rollback.

**Tim Woolford:** Which is a big differentiator for us as well.

**Tim Woolford:** For the most part, we can generally claim, hey, we do all this at a lower cost.

**Tim Woolford:** And we have a lot of sort of flexible, logical pricing options that get us there.

**Tim Woolford:** It is very, very, very easy to implement our platform, which is a big, big differentiator for us too.

**Tim Woolford:** And I think we have one of the most open sort of ecosystem that pulls everything together in the background as well.

**Tim Woolford:** Anything there you want to dive into?

**Aida Knezevic:** No, I think we have a good idea of the AI, the way AI plays into it.

**Aida Knezevic:** Because a lot of our initial content is going to be focused on AI.

**Aida Knezevic:** So we want to get as much deep context on AI as possible.

**Aida Knezevic:** But we've gotten a lot of information so far.

**Aida Knezevic:** Oh, sorry.

**Aida Knezevic:** So consolidate tools.

**Aida Knezevic:** What kind of tools do you consolidate?

**Tim Woolford:** Well,

**Tim Woolford:** I would say there's, well, there's two things there.

**Tim Woolford:** There's vendor consolidation, which ultimately is use us instead of using four other places.

**Tim Woolford:** A lot of people are not going to use just us.

**Tim Woolford:** I think if you look through our customer book and Microsoft's customer book and anybody else's, you've probably got like four customers who are a total one-stop shop.

**Tim Woolford:** It's just not reality.

**Tim Woolford:** So, yes, you can reduce cost, reduce overhead, reduce management by using less vendors.

**Tim Woolford:** Consolidating tools might be you use a few less vendors because you now have more tools from a single vendor, but ultimately it's stitching them all together.

**Tim Woolford:** So we can make sense of the data from all of your tools a lot better than anybody else can.

**Tim Woolford:** And that's purely a function of ingestion and data lake and normalization.

**Tim Woolford:** Our normalization engine is pretty killer, actually.

**Tim Woolford:** It's, it's, um, that stuff gets pretty boring pretty quickly, but it's, it's pretty, um, pretty interesting.

**Tim Woolford:** Interesting when you sort of see the logic topology of how, topography, of how everything is normalized and stored.

**Tim Woolford:** I quite enjoy nerding out on that stuff, but it's like, man, that gets technical pretty fast.

**Aida Knezevic:** Yeah, yeah, fair enough.

**Aida Knezevic:** Anything else there?

**Aida Knezevic:** No, I'm all good.

**Tim Woolford:** There's a couple of TCO reports, sort of third-party ones that I can share as well, if that would be interesting.

**Aida Knezevic:** They sort of dive into some of the proof points about why we think we're cheaper.

**Aida Knezevic:** Okay.

**Tim Woolford:** There's a handful of slides here that just go a little bit deeper into some of the key kind of talking points of each part of the product or each sort of pillar of the product.

**Tim Woolford:** Do you want to walk through them or do you want me to just share those with you?

**Aida Knezevic:** I would love it if you could walk through them.

**Aida Knezevic:** I think we want to get, like, it's different when it's in slides and then when you talk about it.

**Tim Woolford:** I think...

**Tim Woolford:** We get a lot more information.

**Tim Woolford:** Sure.

**Tim Woolford:** Yeah, and these will start getting quite repetitive because, like I said, these should never really be presented the way I am, but I'm just trying to exhaustively get through them.

**Tim Woolford:** So when you think about endpoint or EDR, you know, we push here on having the highest accuracy and the least noise when it comes to traditional EPP or EDR.

**Tim Woolford:** Yeah, single pane of glass, like we talked about, one console, one dashboard, enhanced visibility, seeing everything all at once in one place with enough time to do something about it.

**Tim Woolford:** Obviously, that drives automation, which drives efficiency in the SOC.

**Tim Woolford:** And then, and I haven't seen these for a while, so I am just thinking on the fly here.

**Tim Woolford:** All of that reduces alert fatigue for SOC teams, like we talked about before, the resource constraints and problems.

**Tim Woolford:** And along the bottom there, you'll see this, this is our flagship product.

**Tim Woolford:** Endpointed is what we're known for, and we have the proof in the pudding.

**Tim Woolford:** So now five consecutive years, it needs to be updated, of Gartner, MQ leader, we performed very, very well in the MITRE evaluations.

**Tim Woolford:** Our customers love us with Gartner and we're FIGRAMP high certified.

**Tim Woolford:** The piece there on 88% fewer alerts, that's one I pushed on quite a bit.

**Tim Woolford:** When we went through the MITRE evaluation, and obviously they do the evaluation, not us, so we can sort of claim it quite well there.

**Tim Woolford:** But, you know, Palo Alto came back with, I think it was 178,000 separate alerts, and we had 12.

**Tim Woolford:** And so when you think about, you know, not just false positives, but noise and alert fatigue, going from hundreds of thousands to a dozen is pretty powerful when you sit down to actually triage and navigate through that stuff.

**Tim Woolford:** So we pushed pretty hard on that one.

**Aida Knezevic:** Okay, that is great to know.

**Tim Woolford:** Okay.

**Tim Woolford:** Okay.

**Tim Woolford:** Okay.

**Tim Woolford:** Okay.

**Tim Woolford:** Okay.

**Tim Woolford:** Okay.

**Tim Woolford:** Okay.

**Tim Woolford:** Okay.

**Tim Woolford:** Okay.

**Tim Woolford:** Thank

**Tim Woolford:** Excuse me.

**Tim Woolford:** Gosh, let me kill those.

**Tim Woolford:** When it comes to CNAP and cloud security, this is the area that I'm newest to, so I will bluff my way through this.

**Tim Woolford:** Again, on the bottom there, you know, Gartner Pair Insights leader, G2 leader, and a few hundred awards now.

**Tim Woolford:** Cloud security is relatively new for us.

**Tim Woolford:** We acquired a company called PingSafe about a year and a half ago and quickly integrated it.

**Tim Woolford:** into the platform.

**Tim Woolford:** It is, again, unified and comprehensive, so same sort of argument as before in terms of pulling everything together.

**Tim Woolford:** Focus on what's important from, you know, exploit paths and multi-cloud ingestion.

**Tim Woolford:** One of the things that's really interesting here is our ability to look at risk and exposure across the cloud portfolio.

**Tim Woolford:** So we, we have a really, really good kind of hunting line.

**Tim Woolford:** So line.

**Tim Woolford:** In terms of showing me all the things that are problematic and prioritize them for me.

**Tim Woolford:** So more AI there as well.

**Tim Woolford:** More, very much an outward looking, show me my infrastructure the way the attackers see it.

**Tim Woolford:** So it's all kind of built around risk management as opposed to clean up afterwards, which is great.

**Tim Woolford:** I will send you some more stuff on cloud.

**Tim Woolford:** You will very quickly find the gaps in my knowledge with cloud security.

**Aida Knezevic:** But any questions on that one?

**Aida Knezevic:** No, I think this is great.

**Sydney Arin Go:** I'm sorry.

**Sydney Arin Go:** I had one.

**Sydney Arin Go:** So you talked a little bit about, you called them hunters.

**Sydney Arin Go:** How does SentinelOne's behavioral AI detect zero-day threats?

**Sydney Arin Go:** And do you have any stories about that, like a threat that the system detected because of either behavior or there was inconsistency somewhere?

**Tim Woolford:** Yes.

**Tim Woolford:** Being in the cloud realm, you...

**Tim Woolford:** Like I said, you're going to find the extent of my knowledge there.

**Sydney Arin Go:** So let me get somebody else to answer that for you, and I'll get some stuff sent over.

**Sydney Arin Go:** Thank you.

**Tim Woolford:** Sim, I think we've kind of covered most of this already.

**Tim Woolford:** Just kind of a lot of that AI-driven real-time detection, real-time visibility, most importantly, see everything from everywhere, see it with enough time to do something about it.

**Tim Woolford:** We say we're, you know, stuff on, everyone says that stuff on the bottom, but we, you know, we feel like we have enough good stuff to lean on to make those claims.

**Tim Woolford:** It is much, much cheaper than Splunk.

**Tim Woolford:** It is much, much easier to use than Splunk.

**Tim Woolford:** You know, you've all heard the stories of people setting a Splunk query overnight, coming back in the morning, and it's timed out or failed.

**Sydney Arin Go:** Sydney, you look like that may have happened to you at some point.

**Sydney Arin Go:** I'm not happy to me, but I've heard stories.

**Tim Woolford:** And so we, you know, Union Purple and stuff in there every time.

**Tim Woolford:** Being hot storage, being much easier to use query in natural language, we hang our hat on being a lot easier to use, a lot faster, a lot cheaper.

**Tim Woolford:** So Splunk is probably our biggest target there in the legacy sim space.

**Tim Woolford:** We do a lot around Splunk augmentation.

**Tim Woolford:** We do a lot around Windows event logs, around log storage, and simply just retention.

**Tim Woolford:** Our retention model, like I said, is keeping everything hot, keeping everything on, and being able to do that cost-effectively as well.

**Tim Woolford:** Anything there?

**Aida Knezevic:** I had a quick question, and I realize I probably should have asked this earlier, when you were talking about your competitors, CrowdStrike.

**Aida Knezevic:** But I know that they also have, I think it's called Charlotte, which is their version of Purple AI.

**Aida Knezevic:** And I was curious if you had any knowledge around how their AI is kind of performing, and whether it's kind of up to par.

**Aida Knezevic:** From what I've heard, it's not that good, but I would like to hear it from

**Tim Woolford:** You as well?

**Tim Woolford:** So for a long time, Charlotte was vaporware.

**Tim Woolford:** It was a very, very powerful, very effective marketing exercise.

**Aida Knezevic:** They did a fantastic job of selling something that did not exist.

**Tim Woolford:** Relatively, what's that?

**Aida Knezevic:** Wow, okay, yeah.

**Tim Woolford:** Yeah, I mean, for the first year or so, you literally couldn't buy it.

**Tim Woolford:** And, you know, I'm not throwing stones because it's pretty typical to pre-announce something and, you know, build pipeline for a long time.

**Tim Woolford:** When it first came out, it was expensive and very, very difficult to use.

**Tim Woolford:** From what I understand and what I've seen, they've made remarkable headway in the last sort of six months.

**Tim Woolford:** So I would say, hopefully without bias, I think Purple is probably still six to 12 months ahead in terms of functionality.

**Tim Woolford:** I would say CrowdStrike make us nervous.

**Tim Woolford:** Charlotte is definitely improving very, very quickly.

**Tim Woolford:** sort of Then, when do something

**Tim Woolford:** And to be fair, they managed to sell a product that didn't exist extremely effectively.

**Tim Woolford:** You had CrowdStrike customers who very, very sincerely believed they were using Charlotte when you couldn't even buy it.

**Tim Woolford:** So they did something very well there.

**Tim Woolford:** But to answer your question, I would say Purple is still more capable, more advanced, but Charlotte is quick.
