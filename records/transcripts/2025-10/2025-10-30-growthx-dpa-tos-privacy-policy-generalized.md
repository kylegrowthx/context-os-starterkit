# GrowthX DPA, ToS, Privacy Policy (generalized)

<metadata>
date: 2025-10-30
time: 18:01 UTC
duration: 25 minutes
organizer: yousef@growthxlabs.com
participants: Yousef Hamade, Bridget McGillivray, Jonathan Ng, Samantha Mita
fathom_recording_id: 98118662
fathom_url: https://fathom.video/calls/457814498
share_url: https://fathom.video/share/-VNBYKX9JJ2MS2-xvoNVX7tXUvpaqw5Y
source: fathom
enriched_on: 2026-03-02 21:56 UTC
</metadata>

---

## Summary

GrowthX's legal counsel from Goodwin Law (Jonathan Ng, Samantha Mita) aligned with Yousef Hamade and Bridget McGillivray on the legal framework for CheckThat.ai, a B2B LLM monitoring dashboard launching in Nov/Dec 2025. The team agreed on a hybrid legal model: Privacy Policy for logged-out users (GrowthX as controller), Terms of Service and DPA for paying customers (GrowthX as processor). Jonathan will draft the DPA with PII filtering, Privacy Policy with GDPR data subject rights, and cookie policy by mid-next week; Samantha will draft the ToS; Yousef will implement the Consent Management Provider to control cookie deployment.

---

## Context

GrowthX is preparing CheckThat.ai for launch — a web-based B2B dashboard that tracks brand mentions and citations in LLMs. The product accepts user inputs (domains, product categories, keywords, prompts) and returns competitive intelligence. Pricing will include free and paid tiers with Stripe handling payments. Google Sign-In integration is a launch blocker, requiring both Privacy Policy and Terms of Service to be live on the website before go-live. This meeting brought in external legal counsel (Goodwin Law) to define the legal framework for a product that collects minimal user PII but processes customer business data and generates IP that GrowthX may want to reuse for training. The key tension was balancing GrowthX's desire to own all customer inputs and outputs against market practice (OpenAI typically grants customer ownership) and potential friction during enterprise sales.

---

## Relevance

### To CheckThat Product
- Legal framework is a hard blocker for Nov/Dec launch; PP and ToS must be live to enable Google Sign-In integration
- Privacy-first design: minimal PII collection (just email, company, job title) simplifies compliance and DPA obligations
- DPA will include PII filtering guidance (e.g., named entity replacement) to allow reuse of customer prompts/outputs for model training without violating data processor restrictions
- Cookie consent via CMP needed across all geographies (not just EU) to manage tracking and prevent pre-consent firing, especially if Meta Pixel deployed in future

### To GrowthX Legal / Compliance
- Customer friction expected around IP ownership (common negotiation point); ToS states GrowthX owns inputs/outputs, but larger customers can negotiate via MSA
- GDPR readiness signals (data subject rights for access/deletion/export) create operational burden to fulfill requests but signal compliance maturity
- Free/paid tier blurs user classification; hybrid model (PP for logged-out, DPA for logged-in) handles both prosumer and business-customer use cases
- Goodwin Law committed to drafts by mid-next week (Jonathan: DPA + PP + cookie policy; Samantha: ToS)

### To GrowthX Business Development
- Product positioned as self-serve B2B tool with strategic pricing (free tier + premium tiers), reducing need for sales cycles and custom MSAs
- Legal framework supports future enterprise deals with large customers who will want to negotiate IP/data handling terms
- Goodwin flagged that negotiating ownership away from customer default (OpenAI model) can be a sales friction point; frame as negotiable for deals above X ARR

---

## Overview

- **Product Scope:** Focus on the `checkthat.ai` B2B dashboarding tool launching in Nov/Dec, which tracks brand mentions in LLMs.
- **Hybrid Legal Model:** A Privacy Policy (PP) covers logged-out users, while Terms of Service (ToS) and a DPA govern paying business customers.
- **IP Strategy:** GrowthX will claim ownership of all user inputs and outputs for model training, a point of potential customer friction that can be negotiated.
- **Critical Path:** The PP and ToS are required for Google Sign-In integration and must be live on `checkthat.ai` before launch.

---

## Key Topics

### Product Scope & Launch Timeline

  - **Product:** `checkthat.ai`, a web-based dashboard for tracking brand mentions and citations in LLMs.
  - **Launch:** Nov/Dec 2025.
  - **Audience:** Primarily B2B, though open to anyone. GrowthX will treat all logged-in users as business customers.
  - **Data Collected:**
      - **User Profile:** Name, email, company, job title.
      - **Tracking:** IP address, browser info, cookies.
      - **Customer Inputs:** Domains, product categories, keywords, and prompts to track.
      - **Billing:** Details (name, address) via third-party processor (e.g., Stripe).

### Legal Documentation Strategy

  - **Hybrid Model:** A two-part legal structure to manage user types.
      - **Logged-Out Users → Privacy Policy (PP):** Covers website visitors. GrowthX acts as a data controller.
      - **Paying Customers → ToS & DPA:** Applies to all logged-in users. GrowthX acts as a data processor.
  - **DPA Inclusion:** The DPA will be referenced by default in the ToS.
      - **Rationale:** Simplifies compliance, especially for EU users where DPAs are mandatory.
  - **Cookie Consent:** A broad cookie policy will be drafted.
      - **Action:** GrowthX must implement a Consent Management Provider (CMP) to manage the banner and prevent cookies from firing before user consent.
  - **GDPR Readiness:** The PP will include data subject rights (access, deletion, etc.) to project GDPR readiness.
      - **Note:** This creates a compliance obligation for GrowthX to fulfill user requests.

### Intellectual Property (IP) & Data Use

  - **GrowthX IP Ownership:** The ToS will state GrowthX owns all user inputs (prompts) and outputs (recommendations).
      - **Purpose:** To use this data for training and improving its models.
  - **Potential Customer Friction:** This ownership claim is a common point of negotiation.
      - **Market Context:** Competitors like OpenAI often grant customers ownership and only request a right to anonymize data for training.
      - **GrowthX Position:** The ToS is a click-through agreement. For larger customers, this point can be negotiated in a separate Master Service Agreement (MSA).
  - **Privacy vs. IP Conflict:** A DPA restricts GrowthX from commingling customer PII.
      - **Risk:** If prompts or outputs contain PII, GrowthX must filter it to comply with the DPA while still using the data for IP purposes.
      - **Solution:** Use techniques like named entity replacement (e.g., replacing "Bridget" with "Purple7").

---

## Action Items

**Jonathan Ng**
- Draft DPA incl. PII filtering; send to Yousef/Bridget
- Draft broad cookie policy + banner; send to Yousef/Bridget
- Draft Privacy Policy incl. GDPR rights + logged-out controller; send to Yousef/Bridget

**Yousef Hamade**
- Implement CMP; configure EU cookie blocking; deploy banner on checkthat.ai

**Samantha Mita**
- Draft TOS (web-only, free/paid, 3P payments, IP ownership); send to Yousef/Bridget

---

## Transcript
**Jonathan Ng:** Before we get started, we'd love to introduce you to my colleague, Sam Mita.

**Jonathan Ng:** She's on our technology transactions team, also does some data privacy with me, and she'll be helping out on the terms of service side of the house.

**Bridget McGillivray:** Cool.

**Samantha Mita:** Happy to be here.

**Samantha Mita:** Nice to meet you both.

**Bridget McGillivray:** Nice to meet you.

**Jonathan Ng:** Yeah.

**Yousef Hamade:** Nice to meet you, too.

**Jonathan Ng:** Nice to meet you.

**Jonathan Ng:** Each piece of the documentation serves a different purpose, and each has a different shelf life.

**Jonathan Ng:** Privacy policies are usually good for about six to 12 months, and they need to be future-facing for about that long.

**Jonathan Ng:** Terms of service, those just have to get updated when the products change.

**Jonathan Ng:** And DPAs tend to have a longer shelf life just because they're slightly broader.

**Jonathan Ng:** So I'll take a beat in case you guys have any initial questions.

**Jonathan Ng:** But otherwise, happy to just jump into it.

**Yousef Hamade:** Thanks.

**Yousef Hamade:** I don't have any objection to you.

**Bridget McGillivray:** No, let's do it.

**Yousef Hamade:** Perfect.

**Jonathan Ng:** Okay.

**Yousef Hamade:** Actually, just before we get started, Bridget, I think this is going to be specific to check that, right?

**Yousef Hamade:** At this point in time, or do we need to think about any of the other stuff as well?

**Bridget McGillivray:** Let's start with that.

**Bridget McGillivray:** Like, essentially, we have two different products launching probably by the end of the year.

**Bridget McGillivray:** One in November, so it's the one we want to prioritize.

**Bridget McGillivray:** The second one is going to be maybe in December, but I would imagine probably January, and it's going to be open source, so I think it's like an entirely different, yeah, very different conversation there.

**Bridget McGillivray:** still figuring out like licensing and working with your patent team as well and stuff, so that one's like not as baked, but this one is launching soon, so we'll focus on that.

**Jonathan Ng:** Yeah, awesome.

**Jonathan Ng:** Maybe we start there, and I think that's just like a threshold inquiry.

**Jonathan Ng:** We're still just talking B2B, right?

**Jonathan Ng:** Obviously, no expectation that consumers are going to, maybe prosumers, but still ideas like business users.

**Bridget McGillivray:** Yeah, I mean, it's like a dashboarding tool to see how your brand ranks in LLMs for like mentions and citations.

**Bridget McGillivray:** So, I mean, I guess anybody, it's going to be, there's going to be free capabilities, I guess anyone could go in there.

**Bridget McGillivray:** I don't know that we have plans to limit it to work emails or anything like that, but we could. I don't really see it being non-B2B people.

**Yousef Hamade:** Yeah.

**Yousef Hamade:** Yeah, so, Jonathan, I think in our last conversation, we talked about, you know, our intent is this is a B2B tool.

**Yousef Hamade:** If you're going to use the tool, we're going to treat you as a business customer, even though, again, there's free tiers and all of that that folks you may sign up to.

**Yousef Hamade:** But, yeah, yeah, that's, that's it.

**Jonathan Ng:** Yep, that makes total sense.

**Jonathan Ng:** Well, I think maybe taking a quick step back, it'll be helpful for us to understand the universe of this initial tool — the dashboarding tool, understanding sort of observability and LLM outputs. I would love to understand how will it integrate with your customer services? If at all, like what data you might need to pull from them to power it?

**Yousef Hamade:** Sure.

**Yousef Hamade:** So we're going to ask them to sign up for the tool or they'll be able to use certain functionality without signing up.

**Yousef Hamade:** But for the most part, you know, folks will need to sign up.

**Yousef Hamade:** I think we plan on supporting sign up and sign in with Google.

**Yousef Hamade:** And so that requires, just using that requires the privacy policy to be published on the website and also a public available terms of use.

**Yousef Hamade:** And so we have to post those two there.

**Yousef Hamade:** Again, we've talked about GDPR because anyone anywhere can sign up.

**Yousef Hamade:** And so we have to have some level of GDPR compliance as a result of that.

**Yousef Hamade:** The only information we plan on collecting is basic user profile information — name, email address, maybe phone number if they enroll in MFA, company, and maybe a job title or something like that.

**Yousef Hamade:** But we'd also have, you know, your standard bits of IP address, browser, cookies, et cetera, et cetera, et cetera.

**Yousef Hamade:** But we will need, probably need to put a cookie consent on the page anyhow for tracking cookies and all of that.

**Yousef Hamade:** And so that's why cookie consent policy comes into play there.

**Yousef Hamade:** And then in terms of the app itself, I think we're tracking, here are the domains you want to track.

**Yousef Hamade:** So this is your domain, these are the products or product categories that you want to track.

**Yousef Hamade:** And then at different tiers, these are the specific keywords or prompts that you want to track.

**Yousef Hamade:** So if you ask, like, who are the best X tool in Y category for C user scope, you know, that's a tracked prompt.

**Yousef Hamade:** So, you know, we're the best, you know, privacy lawyers for U.S.

**Yousef Hamade:** with GDPR or startups.

**Yousef Hamade:** You know, we'd get you guys, right?

**Yousef Hamade:** Or you'd hope we'd get you guys as a response, right?

**Jonathan Ng:** Yeah, no, I appreciate that.

**Jonathan Ng:** That's really fulsome.

**Jonathan Ng:** Sam, I'm going to take a quick beat.

**Jonathan Ng:** Any questions from the IP side before I keep barreling forward?

**Samantha Mita:** No, keep going.

**Jonathan Ng:** Let's do it.

**Jonathan Ng:** All right.

**Jonathan Ng:** So I think that's really, that's really helpful understood on sort of how the service will work.

**Jonathan Ng:** Honestly, it's a little bit PII light.

**Jonathan Ng:** So I think it'll be quite simple on the DPA side.

**Jonathan Ng:** I think, though, there is one thing that's worth sussing out at a structural level.

**Jonathan Ng:** On our first call, we did talk about the idea that even a prosumer user will be using for, you know, business capacity.

**Jonathan Ng:** Free services do make that a little bit awkward.

**Jonathan Ng:** So structurally, one way that we could do it, because again, your privacy policy won't apply to B2B use.

**Jonathan Ng:** We could say, for the logged out experience, right, before you go through the order flows, agree to any terms, the privacy policy applies.

**Jonathan Ng:** Right?

**Jonathan Ng:** Which, there are pros and cons, we can talk about that.

**Jonathan Ng:** But it then means that after the customer converts into a paying user, then they're taken into DPA land.

**Jonathan Ng:** How does that ring for you?

**Jonathan Ng:** Or would you like me to talk through a little bit?

**Yousef Hamade:** That sounds about right for me, right?

**Yousef Hamade:** And actually, I forgot to add, we will be adding paid tiers that users can sign up with a credit card for.

**Yousef Hamade:** Now, we won't be a processor there, we're going to outsource that to Stripe or somebody else.

**Yousef Hamade:** And so, we will get some level of billing details associated with that.

**Yousef Hamade:** You know, I think we might get customer address or name on card or, you know, transaction identifiers and things like that.

**Yousef Hamade:** But that's the additional stuff.

**Yousef Hamade:** But that's also only once they sign up.

**Jonathan Ng:** Actually, thinking about this a little bit more, for most of your customers that you anticipate, do you think they'll go through a self-serve funnel and they won't have to approach in a sales cycle to sign an order form or anything?

**Yousef Hamade:** Yeah, that's, Bridget, correct me if I'm wrong, but that's, like, most of the users, that's what we want.

**Yousef Hamade:** Now, we will bundle this, or we may bundle this with services or things like that, and so we'll, you know, give them a subscription for a duration or something like that.

**Yousef Hamade:** But, you know, I think most of our users, we want to be able to go through a self-service funnel.

**Jonathan Ng:** Okay, that's super helpful.

**Jonathan Ng:** I'm going to give you a proposal. And you let me know if it doesn't map, but I think if we treat self-service prosumer users as paying businesses after they convert, I propose we draft a privacy policy that basically says if you're using our website or any services as part of our logged-out experience, the privacy policy attaches.

**Jonathan Ng:** Because we don't know, we don't know who you are, we don't know what you do, but any information you submit to us, we're going to process it as the controller.

**Jonathan Ng:** However, once you do create a paying account, we treat you as a business, and our terms will apply, including any sort of data processing terms.

**Jonathan Ng:** Then the decision that has to be made at this fork in the road is whether you want your DPA to be referenced by default in your terms with customers, or whether you want customers to have to ask you for a DPA.

**Jonathan Ng:** Pros and cons.

**Jonathan Ng:** Used to be that you as the processor in the U.S.

**Jonathan Ng:** did not have to provide it.

**Jonathan Ng:** Still most of the case.

**Jonathan Ng:** In the EU, processors have an independent obligation to provide a DPA.

**Jonathan Ng:** So I would say the easier thing for you to do is just say, if you're a business customer, you get our DPA.

**Jonathan Ng:** Easy peasy.

**Jonathan Ng:** Does that ring for you or do you rather segment it a little bit?

**Yousef Hamade:** That sounds about right to me, particularly since like, you there's all kinds of like, I'll call it 2BPR adjacent laws these days.

**Yousef Hamade:** You know, CCPA, CPRA, and the funding market we solve on and, you know, those.

**Yousef Hamade:** And so, probably the easiest way to go.

**Yousef Hamade:** Now, the other twist to this is...

**Yousef Hamade:** I think we own all content in the platform, so if they say give us a prompt and then we generate stuff for it, we can reuse that prompt, we can reuse all the data we present to them, et cetera, et cetera, et cetera, cetera.

**Yousef Hamade:** Because, you know, we, you know, if they tell us a new category, that's now in our category list that we present to other customers, right?

**Jonathan Ng:** So I'll weigh in on this from a privacy perspective, and then I'll defer to Sam from an IP perspective.

**Jonathan Ng:** If you do agree to a DPA with all customers, one of the primary restrictions on processing that you agree to is with respect to personal information.

**Jonathan Ng:** You're only going to use it for the purpose of that one customer, and you won't commingle it with personal information you gather from other customers.

**Jonathan Ng:** What makes that tricky is if PII is in the prompts or in the outputs, you would need some sort of filtering mechanism to actually comply with your DPA.

**Jonathan Ng:** What a lot of businesses in your situation do is something like named entity replacement.

**Jonathan Ng:** So if it spits out, I don't know, Bridget as an example of a technical operator, you would just swap that out to Purple7.

**Jonathan Ng:** You know, and that way you can still use the prompt from a privacy perspective without violating your DPA.

**Jonathan Ng:** And yeah, I'll pass it to Sam on the IP front.

**Jonathan Ng:** Sam, not to put you on the spot.

**Jonathan Ng:** The thing that I'm thinking about is like, there is a fundamental decision from an IP perspective about owning inputs and outputs versus licensing.

**Jonathan Ng:** So I'll let you speak to that.

**Samantha Mita:** I think typically we recommend that our clients own inputs and outputs. But, you know, we understand that that can be an area for friction with your potential customers, so just want to call that out.

**Samantha Mita:** It sounds like you're intending a lot of people to just come onto your website, go through the click-through process, and so there's not a lot of negotiation.

**Samantha Mita:** So, you know, depending on how sophisticated your future customers are, I don't know if they're going to be reading through everything, but we can absolutely put language in that says that GrowthX will own all inputs, that you'll be able to use it for training of your own systems.

**Samantha Mita:** Just want to flag that if someone sees it, they might want to, you know, engage with your sales team or someone, because we do see that that is one of the more negotiated points.

**Samantha Mita:** So, obviously, your call there, but we can, for sure, fine, like, they would just go shoot it into an MSA or something, right?

**Bridget McGillivray:** Yeah.

**Bridget McGillivray:** Yeah, that works.

**Samantha Mita:** Okay, yeah, that's fine then.

**Jonathan Ng:** Yeah, yeah, yeah.

**Yousef Hamade:** Cool.

**Yousef Hamade:** One of the other things that I forgot to mention is we may, like, look at the website, if they give us a website and say, hey, look, you know, this is the prompt you're trying to hit.

**Yousef Hamade:** Here are some recommendations that you can make to your website to increase visibility or things like that.

**Yousef Hamade:** And, you know, we're allowing them to use those recommendations, but I think they're still our recommendations.

**Yousef Hamade:** And, you know, if they don't produce the desired outcome, that's not on us.

**Jonathan Ng:** Yeah.

**Yousef Hamade:** Yeah.

**Yousef Hamade:** Just want to, you know, make sure that, like, those sort of things are clear.

**Jonathan Ng:** Yeah, I want to say something on the IP side. Please go ahead.

**Bridget McGillivray:** No, go ahead.

**Yousef Hamade:** Okay.

**Jonathan Ng:** Okay, I'll, I'll, we'll make that happen.

**Jonathan Ng:** You may see some friction on that, as Sam said.

**Jonathan Ng:** I will say market probably is not veering towards ownership of inputs and outputs right now.

**Jonathan Ng:** Like OpenAI, for instance, takes the perspective that like outputs to the extent ownable and inputs are owned by the customer.

**Jonathan Ng:** And they just ask for a right to anonymize so it doesn't reference the customer and use it for their own purposes.

**Jonathan Ng:** But many companies do take the ownership position.

**Jonathan Ng:** And Bridget, as you said, right, like that can be negotiated, including as a sales motion, right?

**Jonathan Ng:** You can say for all these extra things you want, you have to pay extra, you have to get on our forms.

**Jonathan Ng:** Okay, I think I'm pretty set on what I need from the, okay, actually two other quick things.

**Jonathan Ng:** On privacy, so I think I heard you say that you do want to have some level of GDPR readiness or at least say...

**Jonathan Ng:** And that via GDPR language in the privacy policy and also a cookie banner.

**Jonathan Ng:** For the cookie banner, I can do one of two things.

**Jonathan Ng:** I can send you a cookie chart where you can list out all the cookies that you'll actually use, and I can draft a tailored cookie banner for that.

**Jonathan Ng:** That's technically what GDPR requires.

**Jonathan Ng:** If you will use the full mix of functional, necessary, marketing, blah, blah, blah, I can just prepare a very fulsome cookie banner that will capture everything under the sun.

**Jonathan Ng:** Some early stage companies prefer that because it just gives them breathing room as they onboard more cookies onto their site.

**Jonathan Ng:** Any preference?

**Yousef Hamade:** I think that one we still haven't quite figured out how we're going to do cookie consent, and a lot of the tools will help us manage that as well, but we should have something there.

**Jonathan Ng:** Okay, so let's just go with a broad cookie policy. You'll need to work with a consent management provider to action the banner itself, right?

**Jonathan Ng:** Yep.

**Jonathan Ng:** And that CMP should plug into all your systems to actually make sure the cookies don't fire in the EU until that banner is actioned, right?

**Jonathan Ng:** By any chance, will you be using the Metapixel on the site?

**Yousef Hamade:** Like Facebook?

**Jonathan Ng:** Yeah.

**Yousef Hamade:** I don't think so at this point in time, but maybe in the future.

**Jonathan Ng:** Okay.

**Jonathan Ng:** I only ask because the Metapixel is like the subject of a lot of litigation in the US.

**Jonathan Ng:** And where companies do use the Metapixel, I recommend that you also drop the cookie banner on US-facing pages. It used to be cookie banner only for EU visitors, but if you use the Metapixel, I do recommend you have the cookie banner for US and EU visitors. It's going to be annoying in the future, but just a heads-up. Really annoying litigation.

**Jonathan Ng:** I can get into it, but just a flag.

**Yousef Hamade:** Yeah, I think my thoughts is we just put the banner on everybody and make things perfect or not.

**Jonathan Ng:** And just a reminder, like, as you know, the cookie should not fire.

**Bridget McGillivray:** Oh, sorry?

**Bridget McGillivray:** Marketing won't like that.

**Jonathan Ng:** No, definitely not.

**Bridget McGillivray:** I don't think we're going to do that.

**Yousef Hamade:** Well, we'll figure that one out.

**Jonathan Ng:** Okay.

**Jonathan Ng:** Well, I will say there's room for, like, risk.

**Jonathan Ng:** There's always room for risk, right?

**Jonathan Ng:** I would say where there is no gray area is in the EU, where, like, the cookies should not drop and pixels should not fire until EU data subjects have exercised their option, right?

**Jonathan Ng:** In the US, different, but we can get to that.

**Jonathan Ng:** In the privacy policy itself, if you do want to project some level of GDPR readiness, the most onerous thing is including data subject rights.

**Jonathan Ng:** That's to access, deletion, correction, export.

**Jonathan Ng:** There's a burden associated with actually offering and complying with those.

**Jonathan Ng:** But it is the first thing that people check for, for GDPR readiness.

**Jonathan Ng:** I will include them in the draft privacy policy, and you let me know if you have any concerns with complying with any of those requirements. Sound good?

**Yousef Hamade:** The requirements are basically to be email, a phone number, and form submission, and then do the thing they ask us to do, right?

**Jonathan Ng:** Yeah.

**Jonathan Ng:** The annoying thing is like lining up all of your like microsystems and making sure that you can actually spit out or action all of the information that they want.

**Jonathan Ng:** But like every company has to deal with it.

**Yousef Hamade:** If you're going to do it early, great.

**Yousef Hamade:** Okay.

**Jonathan Ng:** There we go.

**Jonathan Ng:** Perfect.

**Jonathan Ng:** Okay, Sam, I talked for a long time.

**Jonathan Ng:** I will turn it over to you now on the toss.

**Samantha Mita:** Not too many questions.

**Samantha Mita:** I just want to make sure, Yousef, I think I heard you say an app.

**Samantha Mita:** Is it like a mobile app or it's just like web?

**Yousef Hamade:** It's web.

**Samantha Mita:** Okay.

**Samantha Mita:** Okay.

**Samantha Mita:** Just want to make sure.

**Samantha Mita:** So, no mobile app.

**Samantha Mita:** That's helpful. I'll make sure to not include that.

**Samantha Mita:** I don't think I have too many other questions.

**Samantha Mita:** Seems pretty standard.

**Samantha Mita:** You will have a free option.

**Samantha Mita:** So, I'll make sure to put language for that in.

**Samantha Mita:** I don't think I have too many other questions.

**Samantha Mita:** If I do want anything, I'll definitely follow up with you directly, but I don't think I have anything else at this time.

**Samantha Mita:** Payment will just be through your third-party credit card processor, correct?

**Samantha Mita:** Okay, cool.

**Yousef Hamade:** Yeah.

**Jonathan Ng:** And Sam, I think then stepping into your territory very briefly, it sounds like majority of customers are going to go through a self-serve funnel.

**Jonathan Ng:** Is there any need for Goodwin to separately prepare a paper MSA for bigger customers that will want to negotiate?

**Jonathan Ng:** Or do you just want the self-serve terms first and then deal with the paper later?

**Bridget McGillivray:** Yeah, whenever we have MSAs, it's always their paper anyways.

**Jonathan Ng:** It'd be great if you can get away from that, because that's going to cost you a lot in the long run.

**Jonathan Ng:** But yeah, I hear you.

**Jonathan Ng:** It'll be a process.

**Jonathan Ng:** Okay.

**Jonathan Ng:** I think I'm hearing, let's just do TOS first, and then we'll paper MSA if it comes.

**Bridget McGillivray:** Yeah, let's do that.

**Samantha Mita:** Sure, cool.

**Samantha Mita:** Easy.

**Jonathan Ng:** Easy peasy. Right. Inevitably, there will be things that come up in the drafting process that I forgot to ask about, so Yousef, I may reach out further or I'll just drop questions in the draft.

**Samantha Mita:** Same here.

**Bridget McGillivray:** Thank you.

**Jonathan Ng:** Of course, thank you guys for listening to me drone on for 25 minutes.

**Jonathan Ng:** Timing-wise, I think I can get this to you by mid-next week.

**Jonathan Ng:** That sound okay?

**Bridget McGillivray:** Yeah, that should be good.

**Jonathan Ng:** Thanks for making time, everyone. It's been a couple weeks getting everyone together.

**Yousef Hamade:** Yeah, this week's pretty busy, but we got it done.

**Bridget McGillivray:** Almost over.

**Jonathan Ng:** For your viz, it's M&A Wonderland right now.

**Jonathan Ng:** So, if you guys are exploring strategic exits in the future, buyers are going crazy.

**Bridget McGillivray:** Hey, we can dream.

**Yousef Hamade:** Bridget, just one thing for you to keep in mind. This is a critical blocker for launch. With Google Sign-In, anyone outside our domains can sign up, so it's critical that we have the Privacy Policy and ToS posted on checkthat.ai before launch.

**Bridget McGillivray:** Yeah, yeah.

**Yousef Hamade:** Okay.

**Yousef Hamade:** Cool.

**Yousef Hamade:** Thanks, folks.

**Yousef Hamade:** Thanks so much, everyone. Take care.
