# Meeting w/George (Nick Apostolu)

<metadata>
date: 2025-08-18
time: 20:32 UTC
duration: 29 minutes
organizer: george@growthx.ai
participants: George Haikal, Nick Apostolu
fathom_recording_id: 81279965
fathom_url: https://fathom.video/calls/384350784
share_url: https://fathom.video/share/jSCVxUQzVFAXq7q3YSNa2Hf7WdAf1_yG
source: fathom
enriched_on: 2026-03-03 03:15 UTC
speaker_note: Sydney Go was a calendar invitee but did not participate in the meeting.
</metadata>

---

## Summary

George and Nick aligned on healthcare vertical strategy for Auth0 SDR enablement and sales materials. George is building custom SDR call briefs and account briefs to help Auth0's sales team close deals faster — GrowthX is handling the content creation. Nick shared Okta's healthcare positioning, breaking down six key sub-verticals (health systems, independent hospitals, provider groups, payers, pharma/life sciences, healthcare IT), each requiring different messaging and sales approaches. The team discussed Auth0 vs. Okta CIAM fit, key buying personas (CIO/CISO for workforce, Digital Teams/Patient Experience Officers for customer identity), and critical pain points including security, HIPAA compliance, legacy system integration, and M&A complexity. Nick committed to sharing healthcare-specific decks, market research, and messaging documents to accelerate GrowthX's content development.

---

## Context

Nick Apostolu is Senior Product Marketer for Okta's Healthcare vertical, covering the entire Okta suite (Okta Workforce, Okta Customer Identity, and Auth0) across all healthcare segments globally, with a focus on the U.S. He brings nearly 15 years of healthcare domain expertise, having worked at companies like Bearing Healthcare Solutions and RevCycle on patient portals, payment systems, and population health analytics. George Haikal leads custom engagement at GrowthX, an AI-powered growth marketing agency, and is building sales enablement tools for Auth0 — specifically SDR call briefs and account briefs that dynamically generate personalized talking points based on prospect company and industry. George previously worked at Rachel's team and Okta has a strong relationship with GrowthX for content and marketing support. This meeting was structured as an expert deep-dive to inform GrowthX's healthcare messaging and sales materials, similar to a prior session with Brad Pierce (Okta Retail expert) that generated strong insights for retail verticals.

---

## Relevance

**To GrowthX Delivery:**
- Healthcare vertical requires six sub-segment strategies (not one-size-fits-all), each with different personas, pain points, and product fits — Auth0 suits dev-heavy orgs (large payers, pharma), while Okta CIAM is better for smaller providers without in-house dev resources.
- Messaging must account for terminology nuance: "patient" for providers, "member" for payers, "customer-patient" for life sciences — critical for credibility.
- Key buying centers are often siloed — customer identity (Digital Teams, Patient Experience Officers) and workforce (CIO, CISO) may not communicate, requiring separate sales approaches.
- Purchasing consultants (Vizient, Kauffman Hall) sometimes vet vendors; this is a market dynamic to account for in sales strategy.

**To CheckThat:**
- Healthcare IT is cited as the largest AI adopter across all industry segments; CheckThat AI visibility research should prioritize healthcare IT as a growth opportunity.
- HIPAA compliance, consent management, fine-grained authorization (FGA), and FHIR smart integration are core security/compliance concerns driving AI visibility decisions in healthcare.

**To GrowthX Business Development:**
- Okta considers healthcare one of its "white whale" accounts with significant Fortune 500 presence; this engagement strengthens GrowthX's position as trusted strategic partner for Auth0/Okta sales enablement.
- Healthcare organizations are historically slow to adopt but have recently shifted to cloud — M&A is a major driver of identity/access consolidation, creating expansion and upsell opportunities.
- Average data breach cost in healthcare is $11M (2x global average), making security/cyber threat messaging a primary lever in deal conversations; GrowthX's materials should lead with this pain point for workforce identity use cases.

---

## Overview

- Healthcare vertical spans 6 sub-segments: health systems, independent hospitals, provider groups, payers, pharma/life sciences, healthcare IT
- Nuanced messaging needed (e.g., "patient" for providers, "member" for payers)
- Auth0 suits dev-heavy orgs (e.g., large payers, pharma); Okta CIAM better for smaller providers
- Key pain points: security/cyber threats, unifying disparate systems, time-to-value, extensibility

---

## Key Topics

### Healthcare Landscape Overview

  - 800,000+ global healthcare companies, significant Fortune 500 presence
  - $11M avg. cost per data breach (2x global average)
  - Historically slow to adopt new tech, but recent shift to cloud
  - Unique challenges: HIPAA compliance, siloed architecture, on-prem legacy systems
  - Some orgs use purchasing consultants (e.g., Vizient, Kauffman Hall) to vet vendors

### Sub-Vertical Breakdown

  - Providers (largest segment): health systems, independent hospitals, provider groups
  - Payers: significant presence (e.g., Anthem, Aetna, Cigna)
  - Pharma/Life Sciences: dev-heavy orgs (e.g., Eli Lilly, Pfizer)
  - Healthcare IT: growing segment with increasing AI adoption

### Product Fit: Okta vs. Auth0

  - Auth0: Suits dev-heavy orgs (large payers, pharma) for custom implementations
  - Okta CIAM: Better for smaller providers, "plug-and-play" solution
  - Decision factors: in-house dev resources, desired customization, existing tech stack

### Key Personas and Buying Centers

  - Often separate owners for customer identity vs. workforce solutions
  - Customer identity: Digital teams, Patient Experience Officers
  - Workforce: CIO, CISO
  - Can be siloed, requiring separate sales approaches

### Pain Points and Solutions

  - Auth0:
      - Time-to-value, extensibility
      - 360° patient/member view (progressive profiling, CDP integration)
      - Consent management for HIPAA compliance
      - Smart on FHIR capability, fine-grained authorization (FGA)
  - Okta Workforce:
      - Security (automated threat detection/response)
      - Unified identity security fabric
      - Zero-trust architecture enablement
      - Okta Integration Network (8,000+ pre-built integrations)
      - IAM, governance, privileged access management

---

## Action Items

**Nick Apostolu (Okta)**
- Share healthcare-specific decks, market research, messaging docs, and other relevant materials with George via Slack or email
- Include abridged healthcare positioning deck and longer reference version used internally for AEs
- Provide official Okta messaging documents and market research conducted with partner firms focused on healthcare IAM

---

## Transcript
**George Haikal:** This meeting is being recorded.

**Nick Apostolu:** Absolutely, yeah.

**George Haikal:** Cool, man, where are you calling from?

**Nick Apostolu:** I'm based in Philly.

**George Haikal:** Nice.

**George Haikal:** I grew up on the East Coast, Boston.

**Nick Apostolu:** Oh, nice, nice.

**George Haikal:** Yeah, so you guys got us in the Super Bowl a couple years back.

**George Haikal:** Oh, yeah, I have a bunch of friends from Philly.

**George Haikal:** It's actually a really fun city.

**Nick Apostolu:** I love it.

**Nick Apostolu:** I'm a big fan.

**Nick Apostolu:** Obviously, I'm biased, but, yeah, it's a good time here.

**George Haikal:** Cool, man.

**George Haikal:** Yeah, we're here in San Francisco.

**George Haikal:** So the offices, a lot of the teams distributed as well, but most of the heads of the departments are here based in SF.

**George Haikal:** So kind of perfect timing with all the, you know, the AI craziness, as I'm sure you've heard.

**George Haikal:** And I know Rachel and your team over there is trying to leverage all the tools and capabilities.

**George Haikal:** So as much as possible, that's kind of why we stepped in to try to help and why we're talking today.

**George Haikal:** From you, just so I better understand how to tailor this, but it's going to be super, super casual.

**George Haikal:** just want to treat this as like, I want to uncover what we don't know and get as much expertise that you have as possible.

**George Haikal:** Because every step of the way, we've met with experts over at Auth0 to try to make the pieces of our workflow better.

**George Haikal:** And so we can add your expertise in there, in the healthcare side, but we'd love to hear like a little bit more about you.

**Nick Apostolu:** Yeah, sure.

**Nick Apostolu:** So I've been here for about a year and a half at this point in our product marketing org.

**Nick Apostolu:** So we've got a very matrixed org.

**Nick Apostolu:** I'm on the verticals and regions team.

**Nick Apostolu:** So we've got folks that are covering retail, financial services, manufacturing.

**Nick Apostolu:** During public sector and healthcare.

**Nick Apostolu:** Each of us are global.

**Nick Apostolu:** Obviously, like just the nature of the beast, right?

**Nick Apostolu:** Like we tend to lean towards America, but all of us have a bit of a reach.

**Nick Apostolu:** But I'm, so healthcare, and that spans payer, provider, life sciences, healthcare IT, as well as the entire Okta suite.

**Nick Apostolu:** So I do Okta workforce, Okta customer identity, and Auth0 for customer.

**Nick Apostolu:** Got it.

**Nick Apostolu:** Well, before being here, I've been in healthcare for the vast majority of my career, whether it's RevCycle, Bearinghouse Solutions, as well as like payment portals and patient portals, different kinds of engagement stuff, or population health analytics.

**Nick Apostolu:** So that was the hands-on where healthcare are coming into the fold together and now taking all of that and thinking of how to like layer that into the story of identity and security.

**George Haikal:** Super interesting, man.

**George Haikal:** Super interesting.

**Nick Apostolu:** A lot of twists and turns got it to you.

**George Haikal:** Yeah, I mean, I feel you there.

**George Haikal:** I think my last three jobs have been, let see, private equity, then starting my own digital marketing business, then a pre-seed incubator accelerator, so venture capital and startups, and then here at GrowthX.

**George Haikal:** So kind of a crazy ride as well, but all intentional steps, right?

**George Haikal:** Like all thought through each way, so not random.

**George Haikal:** So I feel you there.

**George Haikal:** there.

**George Haikal:** Cool.

**George Haikal:** So again, actually just to give you a little context on us, right?

**George Haikal:** So right now we're helping, we're GrowthX, we're like an AI-powered growth marketing agency.

**George Haikal:** We do a lot of things.

**George Haikal:** Our bread and butter is like creating content for websites, but what we're helping Rachel with is more of our custom engagement, which is enabling the Auth0 SDRs with documents and materials to help them sell better.

**George Haikal:** And so we wanted to start as narrow as possible and where we landed was automatically generating a custom SDR call brief with all of the quick points an SDR would need based on a prospect name and the company that they work for.

**George Haikal:** And then the second document we have gotten to is a super comprehensive account brief.

**George Haikal:** So like a high level where an A, you could look at it.

**George Haikal:** An exec could come in and look at it and it would have everything a seller would need to know about this account in terms of persona, who they're speaking to, how to sell to them, how this company fits into the Auth0 product, what not to say to them, what to say to them.

**George Haikal:** So that's why we've been doing these expert deep dives is to get as narrow as possible in literally the language and the words that we're using to help these SDRs and these sellers.

**George Haikal:** And I know you oversee the Okta parts as well, not just Auth0.

**George Haikal:** So that would be some cool insight.

**George Haikal:** So that's kind of the perspective that I'm coming in from.

**George Haikal:** And the best way I did it last time, which I think you may know, I know it's a massive company, but Brad Pierce.

**Nick Apostolu:** That's my guy.

**George Haikal:** Yeah, Brad and I are the man.

**George Haikal:** Yeah, yeah.

**George Haikal:** So I did this exact same one with him.

**George Haikal:** For retail, like two weeks ago, he was the man.

**George Haikal:** And so what was helpful is he had a deck that he already just like ran people through or worked off of, like a presentation.

**George Haikal:** Totally fine if you don't have one, but that was a great starting point for us.

**George Haikal:** Do you have something similar, like any materials that you usually show or run through?

**Nick Apostolu:** Yeah, I think I know exactly what he's talking about, and I have a healthcare version.

**Nick Apostolu:** Give me one second.

**George Haikal:** No worries, man.

**George Haikal:** We can always go through the agenda, right, but the questions are a little more boring to go through, where I can just ask them and overlay them over the presentation you're already giving, and we can get in.

**Nick Apostolu:** I'm going to share my screen real quick.

**George Haikal:** What he said, did it look kind of like this?

**George Haikal:** Yeah, how many slides is this?

**George Haikal:** I think his was massive, if I remember correctly.

**George Haikal:** Yeah.

**George Haikal:** It looked like this.

**Nick Apostolu:** Yeah, it looked like this.

**Nick Apostolu:** Okay, cool.

**Nick Apostolu:** I can do, and how much of this do you want to walk through versus — I know you said you've got some questions as well.

**George Haikal:** Yeah, so I think if you want to walk through these at a high level, I can jump in and ask all the questions we have — basically, whatever I'm unclear on, I can stop you and ask.

**George Haikal:** I think Brad just sped through it and had a usual spiel that he gives to everybody.

**George Haikal:** And then like, you know, the more specific stuff, sometimes we skipped over, but we kind of just went through it relatively quickly.

**Nick Apostolu:** And then he shot it over after, which was helpful as well, because we can ingest everything and then incorporate Yep, and so what I'll do, I should have, I've got an abridged version for us, because I had to do this for our AEs as well.

**George Haikal:** That makes this a lot easier. Nice, man.

**Nick Apostolu:** Cool, let's go slideshow.

**Nick Apostolu:** So, all right.

**Nick Apostolu:** So, uh...

**Nick Apostolu:** What I did there is like, one, obviously, there's just like an example of like recent wins that we've got, but the landscape, the challenges for a number of the organizations, and kind of really the next steps here for where you can find information.

**Nick Apostolu:** That's one of the things that I take for them, how to engage.

**Nick Apostolu:** And I'll probably go back and forth between this and the longer version, just because again, there's like interesting tidbits and whatnot that I can pull.

**Nick Apostolu:** But ultimately, spanning the entire ecosystem, the goal is to have an integrated and secure digital identity.

**Nick Apostolu:** And that spans, right, providers, members, their partners, contractors, there's a lot of different things that come into the fold with when it comes to healthcare, and all of them have very like nuanced.

**Nick Apostolu:** Uh, pain points and needs.

**Nick Apostolu:** Yep.

**Nick Apostolu:** Yep.

**Nick Apostolu:** Um, there's a lot of different types of organizations that we run into.

**Nick Apostolu:** Uh, I think I have definitions on this.

**George Haikal:** And for context here — so those six sub-verticals.

**George Haikal:** Like what we did for retail was there were four different personas within retail — grocery, food and bath.

**George Haikal:** Then there was travel and hospitality.

**George Haikal:** And so we broke down the persona quote unquote into those super niche segments and then tag them with like the actual incoming prospecting company.

**George Haikal:** So getting this narrow is fantastic for us.

**George Haikal:** Cause like essentially we would build a, like a master expert document in each one of these fields that would help enable the sell.

**George Haikal:** So that's kind of like how deep we're trying to go.

**George Haikal:** So yeah, already off to a great start.

**Nick Apostolu:** In there, I've got definitions for each of them. Some of them are different.

**Nick Apostolu:** Even for example, health systems, independent hospitals, provider groups — they're all standard providers, like what you'd think of when you think of a doctor.

**Nick Apostolu:** It's just the size and scale, right?

**Nick Apostolu:** So Mayo Clinic would be a health system, but something like AdvoCare, which is primary care and where I go in Philly with multiple locations — that's a provider group.

**Nick Apostolu:** That falls on the provider group.

**Nick Apostolu:** So the need, the sophistication, the budget, all of that is very different.

**George Haikal:** Very different.

**Nick Apostolu:** When it comes to the different organization types.

**George Haikal:** Which is the biggest, like of these six, like what's the biggest breakdown or the largest percentage within the breakdown of like your actual customers today?

**George Haikal:** Do you know the breakdown in terms of numbers and revenue?

**Nick Apostolu:** Yes, by number and revenue, I'd say provider in general — specifically health systems and independent hospitals — would be the largest.

**Nick Apostolu:** Payers are definitely significant there as well.

**Nick Apostolu:** And then Pharma and Life Sciences, we've got some of the big ones.

**Nick Apostolu:** And that's a very interesting use case as well. I was sharing this with Rachel too — the nuance and complexity of Okta versus Auth0 on the customer identity side is tricky. If you're looking at a payer like Anthem, Aetna, or Cigna — massive companies with all these developer resources — it's very different.

**Nick Apostolu:** Same goes for Pharma and Life Sciences with Eli Lilly, Pfizer.

**Nick Apostolu:** You know who these organizations are globally, especially in the U.S.

**Nick Apostolu:** They've got all these development resources.

**Nick Apostolu:** So a platform like Auth0 makes sense in their direct-to-consumer flows. If you're talking about even midsize or some of the larger health systems —

**Nick Apostolu:** In the U.S., not all of them have a dev team.

**Nick Apostolu:** So having a platform that's developer-first where you build on top of it — like Auth0 — doesn't always make sense.

**Nick Apostolu:** Whereas Okta customer identity is more of a true plug-and-play — you press a toggle and your identity solution is on.

**George Haikal:** It's a no code option.

**Nick Apostolu:** But that said, there's a lot of nuance that goes into it as well.

**Nick Apostolu:** Because even if they don't have a ton of dev resources, they might be looking to tie together a patient portal, educational resources, outreach, donors — all of that.

**Nick Apostolu:** And having something that can unify all that in a streamlined way like Auth0 is where it comes down to a decision tree.

**Nick Apostolu:** But what we also know about the space is there's a massive opportunity.

**Nick Apostolu:** This is a global figure, 800,000 healthcare companies.

**Nick Apostolu:** That's a blanket term since there are different types of healthcare companies with significant Fortune 500 presence.

**Nick Apostolu:** M&A is a huge sticking point — unifying different digital portfolios as well as workforce systems.

**Nick Apostolu:** If you have two different active directories, you need to tie them together.

**Nick Apostolu:** That's where Okta Workforce can come into the play.

**Nick Apostolu:** The IT market's in a boom right now — not just across technology, but AI.

**Nick Apostolu:** It's the largest adopter of AI across all industry segments.

**Nick Apostolu:** And the TAM is really just an Okta internal figure.

**Nick Apostolu:** This matters at Okta because some of our white whale accounts are coming from the healthcare space.

**Nick Apostolu:** There are several unique attributes here as well.

**Nick Apostolu:** One interesting thing is the way you refer to the end user — similar to how retail has different segments.

**Nick Apostolu:** For a provider organization, it's "patient" rather than "customer."

**Nick Apostolu:** For a payer, it's "member" rather than "patient" or "customer." For life sciences, it's more complex — they're technically often patients, like in clinical trials.

**Nick Apostolu:** But some orgs view them as customers as well.

**Nick Apostolu:** Eli Lilly, for example, with their direct-to-consumer GLP-1 and telehealth offerings, views them as customers who happen to be patients.

**Nick Apostolu:** So there's a lot of nuance there.

**Nick Apostolu:** On the customer identity side, HIPAA is involved because interactions like sign-on, consent management, and data input touch PHI (Protected Health Information).

**Nick Apostolu:** Healthcare has historically been slow to move.

**Nick Apostolu:** There's a lot of siloed architecture and on-prem technology. Though in the last couple of years, we've seen a significant shift.

**Nick Apostolu:** To the cloud. Another interesting dynamic: sometimes we run into purchasing organizations.

**Nick Apostolu:** Firms like Vizient and Kauffman Hall act as digital transformation consultants, vetting vendors for healthcare organizations.

**George Haikal:** That's an interesting market dynamic we've run into.

**Nick Apostolu:** Yeah.

**George Haikal:** So when you, so when you, so like when you're selling to someone before they say yes, they loop in this consultant sometimes to.

**Nick Apostolu:** It's not guaranteed. We've had plenty of success without going that route.

**Nick Apostolu:** But I've heard anecdotally that certain organizations rely on Vizient, for example, which has a network of preferred partners they operate with.

**Nick Apostolu:** Same with firms like Deloitte or other GSIs — they help build tech stacks.

**Nick Apostolu:** "Here's who we work with and where we've had success."

**George Haikal:** Makes sense.

**Nick Apostolu:** I have several personas here. For us, they're pretty standardized across the ecosystem.

**George Haikal:** By that, you mean all of the different verticals or what?

**Nick Apostolu:** Yes. Obviously the messaging varies, but the people we're

**Nick Apostolu:** Speaking to are generally somewhat similar.

**Nick Apostolu:** From a customer identity standpoint, we typically lean on identity-powered customer or patient journeys.

**Nick Apostolu:** To be clear, this is Okta jargon, but it's about speed, scale, and securing the digital front door.

**Nick Apostolu:** I'll share like some of the official messaging documents as well on this.

**Nick Apostolu:** On the workforce side, we focus on protecting against cyber threats — a critical issue given the frequency and scale of attacks in healthcare.

**Nick Apostolu:** Nearly $11 million per breach in healthcare — twice the global average.

**Nick Apostolu:** It's always top of mind.

**Nick Apostolu:** There's obviously reputational damage that comes with that.

**Nick Apostolu:** There's operational and financial impact, plus HIPAA fines.

**Nick Apostolu:** The Change Healthcare breach a couple years ago is a cautionary tale.

**Nick Apostolu:** Nobody wants to be the next Change Healthcare.

**Nick Apostolu:** That applies to clinical workforce, but there's also the back office.

**Nick Apostolu:** Provisioning, deprovisioning, governing access — managing who can use what and when.

**Nick Apostolu:** Another interesting dynamic: clinicians wear multiple hats. In an academic medical center, someone might be a professor one moment and operating as a clinician the next.

**Nick Apostolu:** The access levels needed for resources vary greatly based on their role at any given time.

**Nick Apostolu:** That's another complexity to keep in mind.

**George Haikal:** Definitely.

**Nick Apostolu:** From your standpoint, what are the other things that are most top of mind that you'd like to understand? I know I'll share all of this — there are a lot of different angles we could explore.

**George Haikal:** Absolutely. I wanted to see where you'd naturally go — that usually indicates what's most important.

**George Haikal:** For us, what we're looking for is messaging — which you already covered.

**George Haikal:** We'll get the rest of the deck and messaging documents to dive deeper there.

**George Haikal:** The second is who we're selling to — who the SDRs are actually speaking with.

**George Haikal:** We covered the six-segment breakdown, but is there anything else high-level you want to share about the buying centers?

**Nick Apostolu:** What we see often — especially at larger organizations — is a separation: there are different owners for

**Nick Apostolu:** Customer identity versus workforce. Often the CIO and CISO own the workforce side.

**Nick Apostolu:** On the digital/customer side, they might have a Patient Experience Officer.

**Nick Apostolu:** It's interesting because the two groups — both focused on identity — operate like completely separate businesses.

**Nick Apostolu:** They don't even talk to each other about purchasing. One group can be an advocate, the other completely unaware. They need to walk down the hall and talk.

**Nick Apostolu:** Generally speaking, that's the pattern.

**Nick Apostolu:** We encounter IT regularly across multiple fronts.

**Nick Apostolu:** Workforce IT is involved, and if they have developers or engineers, they're also involved in customer identity.

**George Haikal:** Got it.

**George Haikal:** That makes a ton of sense.

**George Haikal:** What are the biggest pain points you're solving for each persona? Specifically, what are the top problems Auth0 and Okta address?

**Nick Apostolu:** For Auth0, time-to-value is key, along with platform extensibility — you can customize it as needed.

**Nick Apostolu:** There's also the ability to pull in data from multiple sources for a 360-degree view of the patient or member — progressive profiling, connecting to CDPs for preference data.

**Nick Apostolu:** All combined with security. Auth0 also handles consent management for HIPAA — critical for delegating access like parent-child relationships.

**Nick Apostolu:** Smart on FHIR capability, standards support, and fine-grained authorization (FGA) are also big wins.

**Nick Apostolu:** Controlling access to specific resources is critical on the customer side.

**Nick Apostolu:** On workforce, security is a big one.

**Nick Apostolu:** It's one of the strongest selling points. Automating threat detection and response — given the $11M cost of breaches — is top of mind.

**Nick Apostolu:** There's also a unified identity security fabric — pulling all ecosystem pieces together and managing them with a single source of identity. Whether federating into multiple apps or after merging with another health system where you have separate directories —

**Nick Apostolu:** You plug into Okta and tie them together, tightening security posture and creating a pathway toward zero-trust architecture.

**Nick Apostolu:** There's also the Okta Integration Network with about 8,000 pre-built integrations — no custom code needed.

**Nick Apostolu:** You just connect the dots, and Okta handles the API maintenance.

**Nick Apostolu:** Beyond just IAM, there's governance and privileged access — protecting private keys and architecture.

**Nick Apostolu:** All of this is done through an orchestration layer.

**Nick Apostolu:** It automates as many tasks as possible.

**Nick Apostolu:** It's no longer a manual task that drives teams crazy.

**Nick Apostolu:** It's an always-on engine that runs continuously.

**George Haikal:** This is really helpful.

**George Haikal:** I could talk about this for another hour, but we'll get the deck and materials. What those materials don't have is all the context you just provided.

**George Haikal:** Your expertise and color were really helpful.

**George Haikal:** This gets us to really specific, niche documents we're creating for SDRs.

**Nick Apostolu:** I'm happy to share all of this. There are also other decks and market research I've done with partners.

**Nick Apostolu:** They're healthcare-specific with an IAM focus.

**Nick Apostolu:** There are already insights we can pull into this.

**Nick Apostolu:** I've got a lot of things I can send.

**George Haikal:** Fantastic, Nick. Share over Slack, however is easiest.

**George Haikal:** I'll keep you updated on progress — we're trying to make all your sellers' lives easier.

**George Haikal:** Hopefully that ripples throughout the entire organization.

**George Haikal:** So I'll keep you updated on the progress.

**Nick Apostolu:** I talked to Rachel and she was really excited about this.

**Nick Apostolu:** So I'm looking forward to it.

**George Haikal:** Let's do it. Hopefully we talk again soon, but for now, thanks a lot.

**Nick Apostolu:** Of course, thanks for the time today. Have a good one.

**George Haikal:** You too.
