# Parloa Product Deep Dive

<metadata>
date: 2026-02-04
time: 16:32 UTC
duration: 50 minutes
organizer: william@growthx.ai
participants: Jim Vaillancourt, Moin Ahmed, Marianna Khalifman, Trent Larsen, Dora Kuo, William Leborgne, Maren Ockels
fathom_recording_id: 119715362
fathom_url: https://fathom.video/calls/554537874
share_url: https://fathom.video/share/M-EcyT1NhHRhpYYSzNh7tMLzZsSRm78c
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Parloa's Agent Management Platform (AMP) delivers three core competitive advantages: voice-first excellence (7+ years of VoIP expertise enabling ultra-low latency), rapid enterprise deployment (simulation engine reduces implementation cycles from weeks to minutes), and GDPR-compliant EU architecture. Critical marketing gap identified: the website fails to highlight "best in class for voice" and enterprise capabilities on high-traffic pages (homepage, platform page), causing qualified buyers to bounce; a recorded demo is needed to showcase product speed and convert pipeline.

---

## Context

This deep dive involved William Leborgne (GrowthX) and Jim Vaillancourt (Lionhurst, Google Ads agency) meeting with Parloa's solution engineering team (Trent Larsen, Marianna Khalifman, Dora Kuo) to understand Parloa's product strategy, technical architecture, and market positioning. The conversation was driven by a need to create high-quality marketing content that accurately represents Parloa's differentiators and solves a customer education problem: high-intent traffic is bouncing from the website because core product advantages aren't clearly communicated.

Trent Larsen presented Parloa's composable Agent Management Platform across three dimensions: the voice-first infrastructure (7+ years in telephony, EU-hosted SBC with Azure backend), the rapid deployment model (simulation engine stress-tests agents with hundreds of scenarios pre-launch), and GDPR compliance architecture (short-lived anonymized caches, 28-day data deletion). A live demo of the Kronos Medical Provider line demonstrated multi-patient verification, API integration, and human escalation in action. The underlying insight: the market conflates CX transformation with technology features, when Parloa's real value is orchestrating better experiences—especially for "unhappy path" scenarios that competitors ignore.

---

## Relevance

**For GrowthX (Marketing & Content)**
- Parloa's three-pillar differentiation framework ("leading in voice," "global coverage & local answers," "engineered for enterprise") provides a clear positioning narrative for B2B content.
- The misalignment between market perception (tech tool) and reality (CX transformation platform) is a core messaging opportunity.
- Technical credibility points (EU-hosted architecture, GDPR compliance, simulation engine, TTS fine-tuning in GUI) give substance to claims of "best in class for voice."
- "Unhappy path" design focus is a cutting differentiator in a market obsessed with happy-path automation.

**For Lionhurst (Paid Media & Website Optimization)**
- Homepage and platform page traffic converts at near-zero because differentiators are hidden. Updated messaging and a recorded 3-minute demo will directly impact pipeline.
- Clear positioning ("best in class for voice," "enterprise-ready capabilities," "rapid deployment") needed in above-the-fold content.
- Regional audience segmentation required: European buyers care about GDPR/data ownership; US buyers care about speed-to-deployment and voice quality.
- Competitor comparison chart and "leading in voice" proof points are high-intent conversion drivers.

**For Parloa's Internal Teams**
- Marketing narrative needs to shift from "we have AI agents" to "we solve the CX transformation problem competitors leave broken."
- Sales enablement: The simulation engine and rapid deployment story (3-week implementation vs. minutes for changes) is a quantifiable efficiency differentiator that resonates with enterprise buyers.
- Website content gap is actively causing customer acquisition leakage.

---

## Decisions & Commitments

**GrowthX will:**
- Build content (case studies, messaging frameworks, thought leadership) positioning Parloa as a holistic CX transformation platform, not a technology tool.
- Develop content that clearly explains the EU-hosted Azure architecture for GDPR-sensitive European audiences and addresses the US data ownership concern.

**Lionhurst will:**
- Update the website (homepage, platform page) to feature core differentiators, especially "best in class for voice" and enterprise-ready capabilities.
- Produce a recorded demo (or series of 3-minute clips) showcasing Parloa's speed, voice quality, and simulation engine—similar to the live Kronos Medical demo shown in this call.

**Parloa will:**
- Provide hands-on access to the Agent Management Platform (AMP) for prospects to experience voice quality and deployment speed firsthand.
- Develop messaging architecture that bridges contact-center-native stakeholders and digital-native audiences without diluting the "leading in voice" story.

---

## Open Questions

- **Language Detection & Switching:** Automatic language detection is possible but currently not implemented because current STT models cannot reliably recognize multiple languages in a single conversation. When will dynamic STT models enable real-time language switching without creating separate agents?
- **US Data Ownership Sensitivity:** While Azure is hosted regionally in the EU, it is Microsoft (US) owned. How should marketing messaging address European prospects' concerns about US data ownership in the context of evolving regulatory landscapes (especially post-2025 US administration)?
- **Competitive Positioning on "Engineered for Enterprise":** Trent noted that other vendors (Vapi, Google Dialogflow, AWS SageMaker) claim composable architectures, but Parloa's simulation engine and deployment speed are differentiators. What quantifiable benchmarks prove Parloa's advantage (e.g., implementation time, iteration cycles, time-to-production)?
- **Video/Demo Format Strategy:** Is a single 3-5 minute recorded walkthrough better for conversion, or should Parloa invest in a library of focused 1-2 minute demos addressing specific use cases (e.g., healthcare benefits verification, authentication, escalation)?
- **Dora Kuo's Follow-Up:** The only recorded action item is "Email Dora meeting recording" (assigned to Marianna). Are there other follow-ups or technical deep-dives needed with Dora's team?

---

## Overview

- **Voice-First Platform:** Parloa's 7+ years of VoIP experience enable ultra-low latency, natural-sounding voice AI. Its Agent Management Platform (AMP) simplifies TTS fine-tuning (e.g., for company names) directly in the GUI, eliminating the need to work with external providers like Azure or Eleven Labs.
- **Rapid Enterprise Deployment:** The AMP's simulation engine accelerates implementation by stress-testing agents with hundreds of scenarios pre-launch. This de-risks projects and enables changes in minutes, avoiding the multi-week delays common with legacy systems.
- **GDPR-Compliant Architecture:** The platform uses EU-hosted Azure servers and short-lived, anonymized data caches (deleted after 28 days) to ensure strict GDPR compliance, a key differentiator for European clients.
- **Marketing Gap:** The website fails to highlight core differentiators like "best in class for voice," causing high-intent traffic to bounce. A recorded demo is needed to showcase the product's speed and capability.

---

## Key Topics

### Parloa's Core Value Proposition

  - **Mission:** Shift focus from transactional resolutions to meaningful customer relationships.
  - **Market Position:** An AI-augmented CX platform replacing rigid, NLU-based IVRs with adaptive, natural conversations.
  - **Key Capabilities:** Long-term memory, human-like interaction, and real-time service across all channels.

### Differentiators & Platform Architecture

Parloa's strategy is built on three pillars:

1.  **Leading in Voice**
    
      - **Foundation:** 7+ years of deep investment in phone infrastructure and VoIP.
      - **Result:** Ultra-low latency, natural-sounding voice AI.
      - **TTS Fine-Tuning:** The AMP simplifies pronunciation tuning (e.g., for company names) directly in the GUI.
          - **Why it matters:** This eliminates the need to work with external providers (Azure, Eleven Labs), streamlining development and testing.
      - **Language Handling:** Uses dedicated, language-specific agents for optimal quality.
          - **Why it matters:** On-the-fly language switching is avoided because current STT models cannot reliably transcribe and recognize multiple languages in a single conversation.

2.  **Global Coverage & Local Answers**
    
      - **Origin:** Berlin-based, with a native focus on AI safety and GDPR compliance.
      - **Team:** A diverse team representing 50 countries provides deep language and dialect expertise.

3.  **Engineered for Enterprise**
    
      - **Architecture:** A composable Agent Management Platform (AMP) for performance and reliability.
      - **Key Feature:** The simulation engine enables rapid iteration and deployment.
          - **Why it matters:** It stress-tests agents with hundreds of scenarios pre-launch, de-risking projects and allowing changes in minutes—a stark contrast to the multi-week delays of legacy systems.

### Live Demo: Kronos Medical Provider Line

  - **Use Case:** A doctor's office verifying patient benefits.
  - **Capabilities Demonstrated:**
      - Multi-patient verification from a single, complex utterance.
      - API call to check telehealth coverage details.
      - API call to confirm no open claims exist.
      - Seamless escalation to a human agent with call context.
  - **Performance:** The demo showcased the platform's speed, with Trent noting that conversational design can mask latency from slower legacy APIs.

### GDPR & Data Flow Architecture

  - **Call Flow:** Customer → Enterprise Contact Center → Parloa's EU-hosted SBC (Session Border Controller) → Parloa's Azure-hosted conversational platform.
  - **Data Handling:**
      - **Hosting:** EU-based Azure servers.
      - **Ownership:** Microsoft (US-owned).
          - **Why it matters:** This is a critical point for some European clients sensitive to US data ownership, requiring clear messaging.
      - **Storage:** Short-lived, anonymized data cache (deleted after 28 days).
          - **Why it matters:** This architecture ensures strict GDPR compliance by minimizing data persistence.

### Marketing & Content Strategy

  - **Core Insight:** The market misunderstands the true problem Parloa solves.
      - **Misconception:** Parloa is just another tech tool.
      - **Reality:** Parloa is a platform for holistic CX transformation, focused on orchestrating experiences, especially for "unhappy path" scenarios.
  - **Website Gap:** Core differentiators ("best in class for voice," enterprise capabilities) are missing from high-traffic pages (homepage, platform page).
      - **Impact:** This causes high-intent traffic to bounce, failing to convert into pipeline.
  - **Content Need:** A recorded demo (e.g., 3-minute clips) is required to showcase the platform's speed and capability.

---

## Action Items

**Marianna Khalifman (Parloa)**
- Email Dora Kuo meeting recording for offline review

**GrowthX (William Leborgne)**
- Create content positioning Parloa as CX transformation platform (not tech tool)
- Develop GDPR/data architecture messaging for European audiences

**Lionhurst (Jim Vaillancourt)**
- Update website homepage and platform page with core differentiators ("best in class for voice," enterprise capabilities)
- Produce recorded demo (3-minute format or series) showcasing product speed and voice quality

**Parloa (Trent Larsen / Product)**
- Provide hands-on AMP access for prospect self-serve evaluation
- Refine messaging architecture to address both contact-center-native and digital-native audiences

---

## Transcript
**Marianna Khalifman:** Our office is in SF.

**Marianna Khalifman:** I'm in SF at the moment, but I live in Mexico.

**William Leborgne:** Oh, wow.

**William Leborgne:** Cool.

**William Leborgne:** Yes.

**William Leborgne:** Yeah.

**William Leborgne:** Mixing it up a little bit.

**William Leborgne:** We're about in Mexico.

**William Leborgne:** I live in a town called San Miguel de Allende, which is about four hours north of Mexico City.

**Trent Larsen:** I was just there.

**Trent Larsen:** Really?

**William Leborgne:** Amazing.

**William Leborgne:** Yeah.

**William Leborgne:** It's such a pretty town, right?

**William Leborgne:** Yeah, it's crazy.

**Trent Larsen:** We were in Corretaro, doing some offshore development.

**Trent Larsen:** Conversational AI designers, a large consultancy.

**William Leborgne:** I was like, we have the weekend.

**Trent Larsen:** Should we hang around here?

**Trent Larsen:** Like, no, you should go to San Miguel because of...

**Trent Larsen:** Not a mistake.

**William Leborgne:** Yeah.

**William Leborgne:** It's crazy.

**Trent Larsen:** The amount of expats and the culture is very trending towards, I guess, some Americanized things and tourists.

**Marianna Khalifman:** Rubio an Cue those

**Trent Larsen:** But super cool.

**William Leborgne:** Yeah, it's different, though, than your typical, like, Cancun or whatnot, because it's the expats that are there are living there.

**William Leborgne:** And so there's more of an integration feeling to it.

**William Leborgne:** Yeah.

**William Leborgne:** Yeah, super cool.

**William Leborgne:** That's so fun.

**William Leborgne:** All right.

**William Leborgne:** Well, let's go ahead and dig in.

**William Leborgne:** I have, just FYI, I have some questions on the side that I sent to Dora in case we have time.

**William Leborgne:** But, you know, obviously, like, let you lead.

**William Leborgne:** The goal here is, from our end, know that's, Jim, you with the paid agency?

**Jim Vaillancourt:** Yeah, I work at Lionhurst, and we are managing Google Ads, yeah, for Parloa.

**Jim Vaillancourt:** Okay, awesome.

**Jim Vaillancourt:** So I know we're both here just to absorb.

**William Leborgne:** I don't want to, obviously, step on your toes, and I want to make sure that we're getting the information that we have as well.

**William Leborgne:** But, broadly speaking, I think, for us, is we're getting this information so that we can.

**William Leborgne:** Put this into our agentic systems so that we can create really high quality content.

**William Leborgne:** So I have some broader questions.

**William Leborgne:** I don't know, Jim, if you have something on your agenda that you want to specifically cover.

**Jim Vaillancourt:** Yeah, no, we're just going to go through the walkthrough with them and learn more about the product.

**Jim Vaillancourt:** And so, yeah, we'll pop in with questions as we have them.

**Jim Vaillancourt:** All right.

**William Leborgne:** Sounds good.

**William Leborgne:** We'll do the same.

**Trent Larsen:** Okay, awesome.

**Trent Larsen:** Yeah, I'll kind of give you the spiel.

**Trent Larsen:** And I'm a solution engineer on our team, so we can go as deep technically as we want to when we go into the demo.

**Trent Larsen:** But this is kind of like a primer.

**Trent Larsen:** I'm assuming it'll be helpful just to understand, you know, what Parloa does, why we see ourselves different in the market, all that good stuff.

**Trent Larsen:** So just before we start, just a quick...

**Marianna Khalifman:** I'm...

**Marianna Khalifman:** I'm...

**Marianna Khalifman:** I'm...

**Marianna Khalifman:** So chiming in, I will record this meeting for Dora, who cannot join us, but she also would like to watch the product walkthrough after this meeting, so I will press record now.

**Marianna Khalifman:** Sounds good.

**William Leborgne:** Okay, cool.

**Trent Larsen:** So won't spend a lot of time on these slides.

**Trent Larsen:** Again, like our mission is helping customers or helping companies make the most meaningful relationships with their customers, which might sound paradoxical for an AI company, but it's our real belief that brands that win in this era have to shift their focus from resolutions to relationships.

**Trent Larsen:** And to get those relationships, you need to stop a deflection mentality and open up your voice channel, your chat channel, right, to experience the power of LLMs, how they interact with you, and how they can actually fit your brand identity.

**Trent Larsen:** So we're shaping that with leadership.

**Trent Larsen:** Being customers like Booking over in EMEA, HealthEquity in the U.S., who capture metrics like reduction in AHT, in reducing wait times, right, 24-7 support across digital channels.

**Trent Larsen:** But, you know, outside of just those customers, they are a testament to the volume of calls that we're handling and the types of complex use cases we're tackling.

**Trent Larsen:** But, obviously, the real crux of that is that we are able to deliver on that mission and support, you know, happy customers at the end of the day that are part of those enterprises.

**Trent Larsen:** So, again, if you're new here, right, the customer experience landscape is really shifting in work.

**Trent Larsen:** We're excited to be on that bleeding edge where we've gone from kind of this NLU-based interactions, right, dialogue flows that were scripted, deterministic, everyone's had to sit within a very laborious IVR tree.

**Trent Larsen:** And that's all being changed into kind of an AI augmented CX where you can have adaptive conversations, they're natural, you expect real-time service at any point in your customer journey, right?

**Trent Larsen:** So Parloa kind of stands in this space where traditionally you had to wait for that support and now you can get it instantly with a personal AI agent, right, across modalities that has the ability to have long-term memory, human-like conversations, and really just being treated to the highest degree of service that everyone's expecting.

**Trent Larsen:** So I'll pause there, just kind of the Parloa at a glance, see if there's any questions, anything I want to double down on before we'll dive into more kind of specific differentiators.

**Jim Vaillancourt:** It's all makes sense to me, and we have all the messaging docs from Parloa, so this is an alliance with what we've read through those.

**Jim Vaillancourt:** Okay, awesome.

**Trent Larsen:** To get a bit more detailed, right, there's a lot of noise in the market around AI and CX.

**Trent Larsen:** A lot of enterprises are struggling with the vendor noise and trying to sort through that.

**Trent Larsen:** So we try to be pretty clear on our differentiators, and you might have seen this in the pre-read material for our differentiators.

**Trent Larsen:** So we call this our five pillars.

**Trent Larsen:** I really only focus on three of them, to be honest.

**Trent Larsen:** Especially when I'm pitching or just describing how we're different in the enterprise, or sorry, in the marketplace.

**Trent Larsen:** So you'll see the five there.

**Trent Larsen:** The one I think that's most important is leading in voice.

**Trent Larsen:** So we won't necessarily get in the weeds on voice model orchestration or fine-tuning, but I think the takeaway is that when we've been in this space for seven-plus years, we've heavily invested into phone infrastructure and VoIP experience.

**Trent Larsen:** So what that means is you have that natural-sounding experience that has ultra-low latency, margin, across different languages.

**Trent Larsen:** So that's a lot of what we've invested in, whereas a lot of other companies are chat-first, which takes away a lot of the nuance, right, and having to craft the experience.

**Trent Larsen:** Yeah, go ahead.

**Trent Larsen:** Go ahead.

**William Leborgne:** Yeah, just on this one, something that came up in our conversations was around regional accents and also the empathy within the voice.

**William Leborgne:** Can you tell me a little bit more about that?

**William Leborgne:** Like, what is different that you guys have in that context that maybe your competitors don't?

**Trent Larsen:** Yeah, so the voice models who control a lot of the TTS playback, so the text-to-speech, obviously you have a caller input.

**Trent Larsen:** That's transcribed and processed by the LLM.

**Trent Larsen:** And then the text-to-speech engine is what you're basically hearing, right, over the phone.

**Trent Larsen:** So most of those are open source, right?

**Trent Larsen:** There's not necessarily anything special that Parloa does that others can't do.

**Trent Larsen:** So we're using Microsoft Azure Speech Studio and Eleven Labs as two examples.

**Trent Larsen:** Obviously, there's other TTS engines that we would consider as well.

**Trent Larsen:** know.

**Trent Larsen:** engine.

**Trent Larsen:** we

**Trent Larsen:** But when it comes to regional pronunciation, those voice models are only as good as how they're tuned.

**Trent Larsen:** So when it comes down to pronouncing your company name or if you have a specific product name, that tuning process, Parloa is able to abstract and inject into our UI.

**Trent Larsen:** And I can show you when we dive in here, but it's basically the ability to do that within our GUI.

**Trent Larsen:** So within Parloa and not having to go to that model provider, adjust the language, all of the testing and development around the interaction happens within Parloa.

**Trent Larsen:** So let me see.

**Trent Larsen:** So let's just use this one, for example.

**Trent Larsen:** So there's multiple channels, right?

**Trent Larsen:** I can create phone, chat, whatever channel we're going to be deployed in.

**Trent Larsen:** But each of these channels has the ability to fine-tune the interaction.

**Trent Larsen:** So I can select that voice provider, select the voice, and also fine-tune some of those pronunciation controls.

**Trent Larsen:** So this all happening in one place is a differentiator, which might not sound that crazy, but it actually is a big leap from how you traditionally have to manage voice models in the NLU days.

**William Leborgne:** Are there other examples other than, for instance, a company or a product name where somebody would use that?

**William Leborgne:** In versus, you know, from Madrid, like they would all have different, and that gives that extra edge in terms of the quality of the interaction from a voice perspective.

**Trent Larsen:** Yeah, so those would simply be, oh, I'm going too fast.

**Trent Larsen:** Those would be different voices that you're selecting from our library of providers.

**Trent Larsen:** So Azure is the text-to-speech provider, right?

**Trent Larsen:** They're the voice model, and they have multiple dialects to choose from.

**Trent Larsen:** So, again, Parloa isn't, we're not necessarily unique.

**Trent Larsen:** We do have a relationship with Azure, so the infrastructure that we're hosting makes these voices available in our UI.

**Trent Larsen:** But it's more of the conversational engine behind the voice.

**Trent Larsen:** So, um...

**Trent Larsen:** ...

**Trent Larsen:** Anybody can use these voices across, across regions.

**Trent Larsen:** It's, it's really how you're orchestrating the actual conversation behind that voice, right?

**Trent Larsen:** The, the voice is only as good as, as what it's actually saying.

**Trent Larsen:** Like, sure, it sounds great, but handle a dynamic, multi-term, multi-intent conversation.

**Trent Larsen:** And that's where, you know, having that voice, uh, alongside our AI agent studio is really where, where the power shines.

**William Leborgne:** Okay.

**William Leborgne:** That's really helpful.

**Trent Larsen:** Mm-hmm.

**Trent Larsen:** Um, great question though.

**Trent Larsen:** Uh, let's move on to global coverage and local answers.

**Trent Larsen:** So I think Will, this gets at your question where, um, since we are based out of the Dock region, right?

**Trent Larsen:** We were, we're born out of Berlin.

**Trent Larsen:** Uh, we have more of a, a bias towards AI safety, uh, as well as obviously being.

**Trent Larsen:** Being GDPR compliant, so we moved really quick in that regulatory space, and this gets to that point, too, of fine-tuned languages, where, you know, there's a lot of .ai startups in the past, like, three or four years, right?

**Trent Larsen:** GBT41 came out in 2022, who can just deploy an agent really quick using those same voices, but they struggle when it comes to the European region, right?

**Trent Larsen:** Because they aren't used to handling all those different languages and dialects.

**Trent Larsen:** So this is definitely a differentiator, because our enterprises are multinationals, usually by default.

**Trent Larsen:** So it also helps that our team represents 50 different countries, so, you know, when it comes to testing voice models, a lot of that you can do with synthetic data, but...

**Trent Larsen:** There's live calls and live data that you need to process.

**Trent Larsen:** So it helps having a very diverse team at Parloa.

**Trent Larsen:** And the last one of these five I'll speak to is engineer for enterprises.

**Trent Larsen:** So, you we made a conscious architecture decision to invest, not just to develop AI agents writ large, but an agent management platform, right?

**Trent Larsen:** That is purpose-built to ensure performance and reliability.

**Trent Larsen:** So we did that with this composable view in mind so that you have localized agent versions.

**Trent Larsen:** You can configure, again, across languages, across regions, deploy in different channels, different markets.

**Trent Larsen:** So that is, I think, a talking point for other vendors.

**Trent Larsen:** But our team's actually doing it by being able to compose these experiences within our platform for a variety of use cases.

**Trent Larsen:** So you can have one agent.

**Trent Larsen:** That's adaptable, right?

**Trent Larsen:** Your agent definition scales, and it doesn't take, you know, a six-week sprint, but you can deploy changes in a matter of seconds.

**Trent Larsen:** So I think that is it from the differentiation standpoint.

**Trent Larsen:** Again, you might have seen this slide, too, in the pre-read materials, but that composable nature, there's vendors that sit kind of all across the spectrum, but typically, people are familiar with some of the ADKs.

**Trent Larsen:** Google has a popular one, and actually a very good one, AWS.

**Trent Larsen:** You you can build on SageMaker.

**Trent Larsen:** Vapi is another one that exposes their SDK, and we don't typically associate ourselves with that.

**Trent Larsen:** While we could expose a lot of the developer functionality, we choose not to because of that composable architecture.

**Trent Larsen:** Again, it kind of marries the best of both worlds, and that's where we are finding our swim lane.

**Trent Larsen:** Okay.

**Trent Larsen:** Okay.

**Trent Larsen:** And so, yeah, I'll pause there.

**Trent Larsen:** don't think this is just the final slide again on kind of the overview of Parloa AMP.

**Trent Larsen:** So our agent management platform, again, is designed around the lifecycle.

**Trent Larsen:** So when we talk about AMP, you really can't talk about Parloa without the entire agent lifecycle.

**Trent Larsen:** So designing within that UI that we'll dive into, being able to do test cycles and iterations at rapid speed.

**Trent Larsen:** So it's no longer having to piece together these nodes and say, if this, then that, you know, did this action execute, right?

**Trent Larsen:** that you can drive a robust set of simulated conversations and do that across dozens, if not hundreds, of use test cases to stress and expose any vulnerabilities in your agent build.

**Trent Larsen:** So that is a huge part of making AI.

**Trent Larsen:** So, yeah.

**Trent Larsen:** safe and compliant in your business.

**Trent Larsen:** then again, we talked about deployment, kind of multi-region stance, and then being able to monitor, improve your agents as they go.

**Trent Larsen:** Yeah, go ahead, This is super helpful.

**William Leborgne:** I just want to, there's two things that Dora had shared with us that I want to make sure that I get your take on.

**William Leborgne:** One is, you just talked a little bit about those differentiators, and I just want to understand, like, updating the agents in this sort of enterprise format, is this something that's really unique and or just done much better by Parloa than some of your competitors, let's say PolyAI or something else?

**William Leborgne:** What does that look like?

**William Leborgne:** And then the second part to this question is, something that came up a lot with about the actual implementation, that, like, setting up Parloa and getting it up and running and scaling it is better than competitors?

**William Leborgne:** Yeah.

**William Leborgne:** Would you also say that's...

**William Leborgne:** Differentiator, and if so, how and why?

**Trent Larsen:** Yeah, so we talked about the channels.

**Trent Larsen:** So, right, you can have chat or voice.

**Trent Larsen:** I wouldn't say this functionality is necessarily unique in the market, but it is quite dynamic.

**Trent Larsen:** When I say dynamic, I mean for me to stand up an environment and assign specific variables to that environment, right, be it language, authentication, greeting, like those multi-environment settings, I think, are a bit easier to manage within Parloa.

**Trent Larsen:** So I wouldn't say they're not available on other platforms, but the intuitive nature of being able to, you know, prompt...

**Trent Larsen:** the agent assign, yep, I want this language versus this one.

**Trent Larsen:** And frankly, better guardrails around how you're able to release those configuration changes and deploy them across a production tenant or maybe a staging environment.

**Trent Larsen:** I think that is important for agent builders to have that capability, right?

**Trent Larsen:** So I wouldn't say it's a huge differentiator, but it is important in the talks about safety, compliance, guardrails.

**Trent Larsen:** It does fit in there.

**Trent Larsen:** And ease of use is what I'm hearing.

**William Leborgne:** That is a core differentiator.

**William Leborgne:** Got it.

**William Leborgne:** it.

**William Leborgne:** Yep.

**William Leborgne:** And there was, was there a second question there?

**Trent Larsen:** The second part was just about the, the actual, the implementation at how, you know, a lot of these

**William Leborgne:** As we'll get into sort of this pilot purgatory and get really frustrated and Parloa, a big differentiator is that, you know, we can get people set up and scaled very quickly.

**William Leborgne:** I just want to understand what that means exactly.

**William Leborgne:** She used examples of Booking.com and Ikea.

**William Leborgne:** But yeah, just trying to understand a little bit more what does that mean and how is that, what does that experience look like for the actual user?

**Trent Larsen:** Yeah, so I would say, I don't have a good example of this visually, but historically, and when I was actually on site in Mexico, they were talking about Amelia and kind of a more rules-based flow that they were debugging.

**Trent Larsen:** And it was like, hey, my FTE or FTE has to take three weeks to be able to re-engineer this, right?

**Trent Larsen:** You get either scope creep or a new requirement from the business.

**Trent Larsen:** And it's like, this is three weeks.

**Trent Larsen:** Like that's the actual amount of time.

**Trent Larsen:** So when they went on the platform to start.

**Trent Larsen:** Building, they were like, oh, we released these changes just in minutes.

**Trent Larsen:** I think part of that is the iterative design process where you can simulate those conversations, right?

**Trent Larsen:** We can take, this is just a happy path, healthcare interaction, but we can run these scenarios through.

**Trent Larsen:** And this is what helps accelerate our implementation timeline when we understand the use case, we've done the right discovery, and maybe we've even ingested transcripts and other data from the client that we can use to influence the build and then show the agent's performance before we even go live, right?

**Trent Larsen:** So we already have a really high degree of confidence in the agent, in the tasks it can handle, just based off of...

**Trent Larsen:** What we've done in that kind of pre-sales process, right?

**Trent Larsen:** So, you know, these conversations are happening live.

**Trent Larsen:** We have live authentication running with this doctor's office.

**Trent Larsen:** So he's calling in, checking in on patient benefits and coverage, right?

**Trent Larsen:** We're hitting live tool calls and it's all flowing as expected.

**Trent Larsen:** So that's kind of the, I guess, visual way of describing how we're able to accelerate the delivery timeline because we can role play all these videos before having to test in like a pre-production environment and go through each individual flow node.

**Trent Larsen:** Like it doesn't work like that.

**Trent Larsen:** We have like the entire conversation at our fingertips that we can, we can run and simulate or even.

**Trent Larsen:** You know, unit test parts of this agent.

**Trent Larsen:** The platform is designed to do that for any workflows, be it like a very simple authentication or password reset or doing something more complex, like understanding your health care benefits, you know, for a doctor's office.

**Trent Larsen:** That's really helpful.

**William Leborgne:** Yeah.

**Trent Larsen:** Cool.

**Trent Larsen:** I'm going to transition now and just give this a live call here, and you can see kind of how it plays out.

**Trent Larsen:** Thank you for calling the Kronos Medical Provider line.

**Trent Larsen:** This is Mark, your AI assistant.

**Trent Larsen:** How may I help you today?

**Trent Larsen:** Hey, Mark.

**Trent Larsen:** Yeah, I'm in a really big rush, and I was hoping to get a couple of patients verified.

**Trent Larsen:** I have my MPI here if you want that.

**Trent Larsen:** It's 784-742-3845.

**Trent Larsen:** And then the two patients I had, one was, I think Andrew is 112-2356, and then Mark's ID is 9964-115.

**Trent Larsen:** Anna Arado is active under an HMO plan, effective from September 30th, 2025.

**Trent Larsen:** Mark Gallo is active under a PPO plan, effective from September 24th, 2025.

**Trent Larsen:** Do you need details about specific benefits or anything else for another member?

**Trent Larsen:** Yeah, know, Anna was questioning if she had telehealth services available because she is going to be traveling.

**Trent Larsen:** Okay.

**Trent Larsen:** Yes.

**Trent Larsen:** Telehealth services are included in Anna's benefits and are covered at the same rate of in-person visits with a $20 copay per visit for primary care and behavioral health.

**Trent Larsen:** Is there anything else you need for Anna or Mark?

**Trent Larsen:** Could you please clarify your question?

**Trent Larsen:** No problem.

**Trent Larsen:** Just let me know what you'd like to ask about Anna or Mark and I'll help right away.

**Trent Larsen:** Yeah, Mark was saying he had an open claim, but I'm not sure if that's true.

**Trent Larsen:** Can you just check on that?

**Trent Larsen:** Mark Gallo does not have any open claims on his account.

**Trent Larsen:** Is there anything else I can help you with today?

**Trent Larsen:** Okay.

**Trent Larsen:** Yeah, I think he might have submitted a claim, but...

**Maren Ockels:** Take your time.

**Trent Larsen:** Just let me know if you need details about a specific claim or claim status for Mark, I can connect you with a specialist who can assist further.

**Trent Larsen:** Would you like me to transfer you now?

**Trent Larsen:** Yeah, you know what?

**Trent Larsen:** That'd be great.

**Trent Larsen:** I'm forwarding you to a specialist that can help you with your claim inquiries.

**Trent Larsen:** All right, so if I pop over into Genesis, we'll see this call.

**Trent Larsen:** We'll comment on the email.

**Trent Larsen:** Did you transfer it?

**Trent Larsen:** Okay.

**Trent Larsen:** Okay.

**Trent Larsen:** Okay.

**Trent Larsen:** Okay.

**Trent Larsen:** All right.

**Trent Larsen:** So there you have it, kind of both legs of the call there, where that gets escalated out into...

**Trent Larsen:** The human agent, contact center queue, and they have some just quick details that Parloa can port over around the nature of the call.

**Trent Larsen:** But again, kind of going through this in a very, let's say, design-centric mentality, obviously routing and having that call escalation logic baked in, that happens for virtually all of the agents that we build, voice agents specifically.

**Trent Larsen:** FAQs, so we have the knowledge base that Parloa houses and can either be accessed via API or if clients choose to store their knowledge in Parloa, that is available also.

**Trent Larsen:** then API-enabled skills, so whenever we're doing some type of authentication, obviously we're hitting a RESTful endpoint to retrieve that information.

**Trent Larsen:** Information and to provide the verification that we need.

**Trent Larsen:** So we saw kind of all three of those play out at points in the conversation.

**Trent Larsen:** Yeah, it's quite fast.

**William Leborgne:** Go ahead.

**William Leborgne:** Yep.

**Trent Larsen:** Yeah, we have intentional design choices, again, or infrastructure choices, I should say, around that latency.

**Trent Larsen:** Because, again, you have kind of a chained API approach of the speech-to-text.

**Trent Larsen:** So anything I'm saying is the caller has to be transcribed, then processed by the LLM, and then outputted with the voice model.

**Trent Larsen:** And verified, right?

**William Leborgne:** It's connecting to some database to then be able to find that information, retrieve it incredibly quickly.

**William Leborgne:** Yep.

**Trent Larsen:** Exactly.

**Trent Larsen:** Yeah, so some APIs will take longer than others.

**Trent Larsen:** You know, this is just a mock endpoint and very simple data table that we've spun.

**Trent Larsen:** up to represent just an agnostic CRM, but there's obviously other systems that might have higher degrees of latency, which is actually a benefit for the voice channel because we can design the conversational structure to support even higher latency retrievals, right?

**Trent Larsen:** You can ask questions, you can, like, most of us are just accustomed to being put on hold.

**Trent Larsen:** It's like, great, all right, now 30 minutes, let me do another task, but you can actually engage your customers in a way that typically was never available before while you're retrieving, verifying, or checking the status on something.

**Trent Larsen:** So, yeah, that's a question of, like, well, I've got some legacy application and might need some middleware or other infrastructure that's going to sit in between the LLM, which isn't really ever a problem because...

**Trent Larsen:** We can still design the conversation in a natural way that flows regardless of the backend systems.

**William Leborgne:** You mentioned that a lot, or maybe most of your clients are, you know, multinational, they want multiple languages.

**William Leborgne:** Does, if they call in, does the AI just automatically, it would be the same voice, but it would just switch into Spanish or German or whatever language just automatically?

**Trent Larsen:** Yeah, so the way we build our agents currently is around a regional language preference, meaning some of those voice models that we talked about earlier, right, like Catalan versus Mexican Spanish, like they do index higher in those language nuances.

**Trent Larsen:** So we build language specific agents.

**Trent Larsen:** Despite the fact that this agent, even though it speaks English, could speak Spanish.

**Trent Larsen:** So automatic language detection is a possibility, but it oftentimes doesn't provide the best experience, just based on that fact that the language isn't going to be fine-tuned, and we're not flipping these voice models on the fly.

**Trent Larsen:** So we would typically stand up a dedicated agent and have a multi-agent handoff between this agent that could respond back and say, hey, well, like, and say it in Spanish, and then say, hey, I'm actually going to get you to an agent that's best fit for that interaction, right?

**Trent Larsen:** I see.

**William Leborgne:** Okay, got it.

**William Leborgne:** Yeah.

**Trent Larsen:** And a lot of that, again, is just architecture, the way the chained voice processing works is you have to do this.

**Trent Larsen:** Speech-to-Text.

**Trent Larsen:** And if I say something in Spanish, it might capture a few words, but it's not necessarily going to know that every single grammatical nuance was in Spanish versus English.

**Trent Larsen:** The model doesn't automatically transcribe that and instantly recognize the language.

**Trent Larsen:** It's just going purely off of more of an English-driven approach.

**Trent Larsen:** So in the future, when we have more dynamic STT models, then that can become a reality.

**Jim Vaillancourt:** So Trent, is the software required to say that they're an AI agent when it answers phone calls, like in the example you just said?

**Trent Larsen:** It's purely a design choice around the client.

**Jim Vaillancourt:** Gotcha.

**Trent Larsen:** So in here, you know, we could insert variables as well.

**Trent Larsen:** Right.

**Trent Larsen:** We saw these earlier in the environments.

**Trent Larsen:** One of these variables could be a personalized approach and say, hey, you know, I'm addressing Jim and we would initiate kind of a webhook or API call before that conversation even initiates, before the interaction is live to feed your CRM record in.

**Trent Larsen:** So there's a variety of things you could do on that welcome message.

**Trent Larsen:** But yeah, it's kind of a pure design choice.

**Trent Larsen:** And a lot of times it's based off of where their end clients are in their customer journey.

**Trent Larsen:** Like if they're going from a very rigid IVR, a lot of times they'll choose to not make it so conversational, which is odd, right?

**Trent Larsen:** You think, don't we want to make it the best experience?

**Trent Larsen:** But it's kind of handholding those end callers through just a progressive exposure to...

**Trent Larsen:** AI.

**Trent Larsen:** So it kind of depends on the disclosure there.

**Trent Larsen:** Okay.

**Maren Ockels:** I have a question as well.

**Maren Ockels:** It's actually about the pillar number three that you were talking about.

**Maren Ockels:** I'm from Germany.

**Maren Ockels:** So I have a very dedicated view on the, no, can you go three slides further?

**Maren Ockels:** Not back, but further?

**Maren Ockels:** Yeah, that one.

**Maren Ockels:** The point one, where you talk about the GDPR.

**Maren Ockels:** So I wonder how this is, like, because I don't understand the technical part behind this so much.

**Maren Ockels:** So maybe my, my question sounds a little bit strange or even stupid or funny.

**Maren Ockels:** I don't know.

**Maren Ockels:** more you know, Chat den, Would done, done.

**Maren Ockels:** So I wonder how is it technically working?

**Maren Ockels:** So you have Parloa in the middle and you have the voice on the one side and the CCAS on the other side.

**Maren Ockels:** But how is it technically connected?

**Maren Ockels:** So how is the data flow through this process?

**Trent Larsen:** Yeah, let me see if I can find this slide here.

**William Leborgne:** I think these are good ones.

**Trent Larsen:** So let me go back here.

**Trent Larsen:** Sorry, I'm going to do some screen dynamic.

**Trent Larsen:** Can you see this one?

**Trent Larsen:** So again, when there's a customer calling in, and we'll just use voice as the primary channel, that usually is a PSTN connection.

**Trent Larsen:** So it's a public switch telephone network or POTS, right?

**Trent Larsen:** Like over a copper line.

**Trent Larsen:** And that hits the enterprise's contact center.

**Trent Larsen:** Most companies we work with, right, have a contact center.

**Trent Larsen:** So they have some level of call management happening and software that's running behind their telephone system.

**Trent Larsen:** And that typically has what we call SIP trunk.

**Trent Larsen:** So SIP trunk is basically just the mechanism where you're able to pass a voice call over the internet with things like a SIP invite.

**Trent Larsen:** Or SIP refer, which basically just says what system is allowed to take this call.

**Trent Larsen:** Again, you kind of whitelist IP addresses and make sure that that call traffic is allowable.

**Trent Larsen:** So Parloa would be one of those recipients or destination of that traffic.

**Trent Larsen:** If they don't have a contact center or they don't have SIP trunking capabilities, I think there's maybe a small number of clients that we work with who just forward numbers directly over copper lines, over PSTN, which is also possible.

**Trent Larsen:** So that hits one of Parloa's SBCs.

**Trent Larsen:** So we have our own telephony infrastructure and basically our conversational platform is a Azure-hosted VM, so traffic kind

**Trent Larsen:** It can get streamed into our voice gateway, which is where that STT process happens, right?

**Trent Larsen:** Calls are transcribed into text, and then they're sent to our LLM orchestrator, which is able to then...

**Maren Ockels:** Okay, so let me interrupt here.

**Maren Ockels:** So just catch this up in my words.

**Maren Ockels:** So this part, this SPC, is a server that is hosted by you, and there the traffic and the magic is done?

**Maren Ockels:** Correct, yep.

**Maren Ockels:** Okay.

**Maren Ockels:** The server is hosted where?

**William Leborgne:** Our session border control is hosted in the EU.

**Maren Ockels:** Okay, and the server owner, is it an EU owner or is it an American owner?

**Maren Ockels:** Oh, Is it ADS?

**Trent Larsen:** AWS?

**Maren Ockels:** It would be Azure.

**Trent Larsen:** Okay, so it's Microsoft.

**William Leborgne:** Okay, so it's US-owned.

**Trent Larsen:** Yes, but since it's hosted regionally, right, so we...

**Trent Larsen:** Yeah, and I understand.

**Maren Ockels:** It's just there's some companies here are very sensitive about this, especially what is currently happening in the US.

**Maren Ockels:** Therefore, some are sensitive if the owner of the server is a US company, and therefore I'm asking, because it's important for me to be able to write things in the ad, or if I should not write things in the ad.

**Maren Ockels:** Yeah, definitely.

**Maren Ockels:** Got Got it.

**Trent Larsen:** Okay.

**Trent Larsen:** Thank you.

**Maren Ockels:** Yep.

**Trent Larsen:** So, yeah, essentially, the AI agent sits on the backside of how we're orchestrating the LLM and the other voice models.

**Trent Larsen:** So that's kind of the key point at which data traffic is accessed.

**Trent Larsen:** And, yeah, the way that we're able to manage conversation state and turn management happens alongside the LLM gateway as well.

**Trent Larsen:** So we use kind of a short-lived cache to only hold the active conversation context because data otherwise will get deleted after 28 days.

**Trent Larsen:** So that data doesn't persist, but it's anonymized.

**Trent Larsen:** So we obviously do have analytics that are running on the back end of Azure where we have...

**Trent Larsen:** We event stream and we pulled data in to various databases to run those analytics.

**William Leborgne:** I've got a quick question and I know we're coming up on time.

**William Leborgne:** This is honestly me digging into your brain, Trent, in terms of things that you feel like are not, are misunderstood about Parloa.

**William Leborgne:** Is there anything in everything that you've shown us that is maybe like you're seeing this as a misunderstanding or a lack of understanding within the industry and within your customer audience or your audience generally?

**William Leborgne:** And if so, what would you want, like how would you want to change that?

**William Leborgne:** Like if there was a piece of content that actually like rectified something that was misunderstood, what would that be?

**William Leborgne:** That's a good question.

**Trent Larsen:** I guess the...

**Trent Larsen:** The one thing is, like, all companies are actually tackling the problem, right, of CX transformation, how they're guiding the customer journey and actually solving the problems within the legacy contact center.

**Trent Larsen:** It's typically something that requires deep industry expertise, right, of being able to orchestrate these experiences.

**Trent Larsen:** Like, everything we're talking about is, like, there's a lot of tech, but it really is conversational design, right?

**Trent Larsen:** Like, how am I going to just navigate this scenario someone calls in?

**Trent Larsen:** Like, usually people aren't just calling in to have a chat, they're pissed off, right?

**Trent Larsen:** Like, being able to design agents for that unhappy path, I think is...

**Trent Larsen:** It's a super critical point where it's not just a use case or workflow or a context set or automation.

**Trent Larsen:** It's truly how do we orchestrate the best experiences for our customers.

**Trent Larsen:** I think that is a big way to kind of cut through what other companies are doing.

**Trent Larsen:** Like, Parloa is building a platform to solve that problem holistically rather than just at a specific point in the journey or in the contact center.

**Trent Larsen:** So I think that would maybe be my answer if that helps.

**Trent Larsen:** A lot, actually, honestly.

**William Leborgne:** Like, it focuses it more on, in some ways, the jobs to be done, but almost more like just the broader pain point and cutting through the noise of, like, this is all the technical, cool stuff that we can do and be more like, this is the core thing that we are solving.

**William Leborgne:** And it's got to be a mindset shift.

**William Leborgne:** So, yeah.

**William Leborgne:** Very helpful.

**William Leborgne:** Yeah.

**Trent Larsen:** I think everyone acknowledges CX is broken.

**Trent Larsen:** Everyone still has that service provider who's not modernizing.

**Trent Larsen:** The tech is a part of it, and it's a big part of it, but it's now a question of, well, if you had to design that experience and deploy it, what are the actual steps?

**Trent Larsen:** How would you start tackling that problem?

**Trent Larsen:** And I think we're coming at it from just a very transformative way.

**Trent Larsen:** Like, there are less barriers in terms of having to stand up automation, and it's more like, how do we address the biggest pain points that your customers are facing today?

**Trent Larsen:** Awesome.

**Trent Larsen:** Yeah, and I know we're at time here.

**Jim Vaillancourt:** We're bleeding into our weekly meeting, like Parlois, but I want to cut off soon.

**Jim Vaillancourt:** But, Trent, just want to say.

**Jim Vaillancourt:** Thank you.

**Jim Vaillancourt:** That was really interesting how you walked through, especially like the interactive demo that you did and showing the live interaction with customer support.

**Jim Vaillancourt:** I'd say I have more of a comment than any questions here, and this may be known, this may be being worked on and more related to marketing than anything else.

**Jim Vaillancourt:** But as far as the differentiators you shared, like best in class for voice, GDHPR compliant, well, that's shared a little bit on the site.

**Jim Vaillancourt:** But from our standpoint, what we're trying to do is get people to the website who are going to convert and become pipeline.

**Jim Vaillancourt:** We're trying to drive pipeline.

**Jim Vaillancourt:** And our current issue is that we can drive very qualified traffic, people at large companies who are looking for AI customer support, AI contact centers, but they don't convert, right?

**Jim Vaillancourt:** So they visit the site, they're 30 seconds, they leave.

**Jim Vaillancourt:** And hearing this, this one.

**Jim Vaillancourt:** Walkthrough and your differentiators.

**Jim Vaillancourt:** I mean, two-thirds of all traffic is going land on the homepage or the platform page, at least for new users who aren't going to like a careers page or events page.

**Jim Vaillancourt:** So those two pages specifically, they don't even mention best in class for voice.

**Jim Vaillancourt:** And so, and also like enterprise ready capabilities.

**Jim Vaillancourt:** There's just, I guess what you shared is not well represented on the website in terms of content.

**Jim Vaillancourt:** And we've had brief discussions with Dora and Marianna about this, but what you shared was extremely useful.

**Jim Vaillancourt:** And what I'm trying to think about is how can we, you know, kind of take this experience that you shared and make it, have it on the website so that people better understand differentiators.

**Jim Vaillancourt:** Because you shared that chart that had all of the other competitors in the various categories related to Parloa.

**Jim Vaillancourt:** There's so many, especially in U.S.

**Jim Vaillancourt:** where you don't have great brand awareness.

**Jim Vaillancourt:** And if we're not getting these differentiators right in front of them, that's a problem.

**Jim Vaillancourt:** And then also, you know, working with other large software companies, I know that recorded demos are huge as far as resources that people like to interact with.

**Jim Vaillancourt:** Like what you shared today, if we could get, you know, that into a three-minute demo or break it up into three-minute demo chunks, I mean, that would be an amazing resource to have on the website.

**Jim Vaillancourt:** Mm-hmm.

**Trent Larsen:** Yeah, for sure.

**Trent Larsen:** Yeah, I think that our team, and Marianna can speak to it maybe more intimately, is moving to more hands-on access to our agents, for sure.

**Trent Larsen:** The leading in voice and global coverage is a bit tricky, right?

**Trent Larsen:** A little bit of a signal you have to ingest first and know, like we're saying, what type of experience?

**Trent Larsen:** Like, are they contact center native stakeholders, or are they more digital-centric?

**Trent Larsen:** So, I think the kind of multimodal CX, like do-it-all, is...

**Trent Larsen:** is a bit noisy.

**Trent Larsen:** Like, I think I see it in other vendors.

**Trent Larsen:** But the voice channel is the hardest to automate.

**Trent Larsen:** So I think it's important to emphasize, and it's also tricky, right, to find the line between how you can also appeal to a digital native stakeholder.

**Trent Larsen:** But yeah, the kind of getting into the hands of users, I think we're absolutely moving in that direction, for sure.

**Trent Larsen:** Cool.

**Jim Vaillancourt:** All right, well, thanks, Trent.

**Jim Vaillancourt:** Yeah, appreciate it for your time.

**Trent Larsen:** Hope it was helpful.

**Trent Larsen:** And I'll let me know if you need anything else.

**Trent Larsen:** If you want to dive deeper, I can share.

**Trent Larsen:** Thank you so much, Trent, for hosting us today.

**William Leborgne:** Yeah, thank you.

**Marianna Khalifman:** And thank all for joining.

**Jim Vaillancourt:** Appreciate it.

**William Leborgne:** Talk soon.

**William Leborgne:** Yeah, bye, everyone.

**William Leborgne:** We'll see you guys.

**Jim Vaillancourt:** Bye-bye.

**Jim Vaillancourt:** Thank you.
