# Abnormal AI / GrowthX AI, Inc Introduction

<metadata>
date: 2025-09-10
time: 21:33 UTC
duration: 39 minutes
organizer: Yousef Hamade
participants: Yousef Hamade (GrowthX), Domenico Ortiz (Abnormal AI), Marilyn Waidelich (Abnormal AI)
fathom_recording_id: 86440223
fathom_url: https://fathom.video/calls/407019077
share_url: https://fathom.video/share/CRmiNiunfxvGNSwC5k-4PXZxR_YApttA
source: fathom
enriched_on: 2026-03-02 00:45 UTC
</metadata>

---

## Summary

Yousef Hamade (GrowthX's IT/cybersecurity lead) met with Abnormal AI's Domenico Ortiz and Marilyn Waidelich to evaluate Abnormal's AI-driven email security platform for GrowthX's SOC2 compliance needs. Abnormal demonstrated its behavioral AI approach that analyzes 43,000+ signals per email and integrates via API with Google Workspace without requiring a gateway. GrowthX is moving forward with a 7-day risk assessment in Q4 (targeting November), with pricing starting at $25K minimum and to be negotiated through their existing partner GuidePoint Security.

---

## Context

GrowthX and Abnormal AI have an existing business partnership — GrowthX is a GTM and content marketing services provider that has been generating content and driving organic visibility for Abnormal's products. This meeting was initiated by Yousef Hamade, who leads cybersecurity and IT at GrowthX and is responsible for the company's security infrastructure as they scale. GrowthX grew from 25 employees in January 2025 to 75 by September 2025 and is pursuing SOC2 compliance certification within the next several months. The company currently runs on Google Workspace, Okta for MFA, and Sentinel One for EDR/MDR. Yousef had evaluated Abnormal months prior but wanted a fresh look at how the platform works and integrates. Marilyn Waidelich was assigned as the account executive managing the relationship.

---

## Relevance

**To GrowthX Delivery:**
- GrowthX is pursuing SOC2 compliance and email security is a critical control for certification; Abnormal's lightweight API integration (no gateway required) aligns with their modern security posture using Google Workspace, Okta, and Sentinel One
- Abnormal's 7-day risk assessment is low-lift and requires minimal internal effort from GrowthX's already-stretched security team
- The decision timeline aligns with Q4 (likely November) and won't block other priorities

**To GrowthX Business Development:**
- Existing partnership with Abnormal creates cross-selling and reference opportunity; successful adoption strengthens the relationship and differentiates GrowthX's services positioning
- GuidePoint Security is already an established partner for GrowthX (Sentinel One procurement) — using them for Abnormal quote reduces contracting friction and speeds deal closure
- Account health signal: GrowthX is actively investing in security infrastructure and tooling as it scales; suggests stable, growth-stage customer with budget predictability

**To CheckThat:**
- Conversation demonstrates GrowthX's hands-on approach to vendor evaluation and technical validation; GrowthX's content strategy work (helping Abnormal rank in AI responses) may inform CheckThat positioning to security buyers

---

## Overview

- GrowthX (75 employees) seeks email security for SOC2 compliance; experiencing basic phishing attempts
- Abnormal offers AI-driven protection against advanced threats, account compromise, and spam without traditional gateway
- Pricing starts at $25K minimum; official quote/pricing to be provided through GrowthX's preferred partner (GuidePoint Security)
- GrowthX interested in evaluating; potential Q4 timeline for decision (likely November)

---

## Key Topics

### GrowthX Current Security Posture

  - 75 employees (100 total mailboxes including shared)
  - Using Google Workspace with native security features
  - Implementing Okta for MFA, Sentinel One for EDR/MDR
  - Experiencing basic phishing/impersonation attempts, but no major breaches
  - Finance team adept at spotting invoice fraud attempts

### Abnormal AI Solution Overview

  - API-based integration with Google Workspace (no gateway required)
  - Core offering: Inbound Email Security against advanced threats
  - Add-ons: Account Compromise protection, AI Security Mailbox, Graymail management
  - New AI Phishing Coach feature for user training (details TBD)
  - Behavioral AI analyzes 43,000+ signals per email for context-aware protection
  - 7-day risk assessment offered to demonstrate value with minimal customer effort

### Technical Integration & User Experience

  - Quick API integration with Google Workspace (minutes to set up)
  - No quarantine or user digest emails; suspicious emails moved to deletions folder
  - False positives can be reported by admins for re-analysis and model improvement
  - Integrates with existing security stack (Okta, Sentinel One) via REST API

### Pricing and Partnership

  - $25K minimum annual contract, specific per-user pricing to be provided
  - Typically sold through channel partners; GuidePoint Security identified as GrowthX's preferred reseller
  - Official quote to be provided through Tom Wish at GuidePoint Security

---

## Action Items

**Marilyn Waidelich**
- Reach out to Tom at GuidePoint Security and provide him with a quote for GrowthX AI, Inc
- Send follow-up email to Yousef Hamade recapping next steps, including security hub info and offerings overview

---

## Transcript

**Marilyn Waidelich:** Hi, Yousef.

**Marilyn Waidelich:** How are you?

**Yousef Hamade:** Doing well.

**Marilyn Waidelich:** How about yourself?

**Marilyn Waidelich:** Good.

**Marilyn Waidelich:** Nice to meet you.

**Yousef Hamade:** Nice to meet you, too.

**Yousef Hamade:** Did I pronounce that correctly, Yousef?

**Yousef Hamade:** Yes, that is correct.

**Marilyn Waidelich:** Okay.

**Marilyn Waidelich:** Awesome.

**Marilyn Waidelich:** Alrighty.

**Marilyn Waidelich:** Are we waiting for anyone else on your side?

**Marilyn Waidelich:** Okay.

**Marilyn Waidelich:** Domenico, did you want to kick it off or did you want me to?

**Domenico Ortiz:** Yeah, yeah.

**Domenico Ortiz:** Yousef, thanks so much for joining us today.

**Domenico Ortiz:** Really appreciate the time to meet with us and letting us take you underneath the hood of abnormal.

**Domenico Ortiz:** Why don't introduce you to Marilyn?

**Domenico Ortiz:** She's going to be your point of contact moving forward.

**Domenico Ortiz:** Yeah, I'll let her kick us off.

**Marilyn Waidelich:** Great.

**Marilyn Waidelich:** Yeah.

**Marilyn Waidelich:** Thanks for setting this up.

**Marilyn Waidelich:** So my name is Marilyn.

**Marilyn Waidelich:** I'm the account executive aligned to GrowthX here at abnormal.

**Marilyn Waidelich:** Normal.

**Marilyn Waidelich:** And I know we got this meeting scheduled pretty quickly here, but I definitely have a few notes from Domenico on, you know, the size.

**Marilyn Waidelich:** And it looks like we

**Marilyn Waidelich:** We have a partnership with you guys in place, and you're on Google, you had some interest in looking at abnormal for email security.

**Marilyn Waidelich:** So we'd love to learn more, hear more about your role, responsibilities over at GrowthX, and then we'll kind of go from there.

**Yousef Hamade:** So to start, yes, GrowthX actually is a partner with Abnormal.

**Yousef Hamade:** We help you guys with some of your GTM strategy, content creation, et cetera.

**Yousef Hamade:** And so I actually tried setting this up through our contacts there, and may have just been lost somewhere in the fold between your marketing team and your GTM team.

**Yousef Hamade:** So I did just decide to go online and fill out the form, and we were able to get this scheduled.

**Yousef Hamade:** So...

**Marilyn Waidelich:** Way faster.

**Yousef Hamade:** Yeah, somehow.

**Yousef Hamade:** Uh...

**Yousef Hamade:** And so from a, my role here, so I am cybersecurity and IT for, for growthx.

**Yousef Hamade:** I work closely with the leadership here.

**Yousef Hamade:** I'm actually a consultant myself.

**Yousef Hamade:** And so you may actually see my name elsewhere at various times versus with different leads.

**Yousef Hamade:** I am the only one.

**Yousef Hamade:** I use Hamade out there.

**Yousef Hamade:** So if you do come across my name on other leads, you know, those may or may not be active engagements as well.

**Marilyn Waidelich:** That's funny because I was looking for you on LinkedIn and I couldn't find you.

**Yousef Hamade:** So I wonder if it's under a different company.

**Yousef Hamade:** It's not under the same company.

**Yousef Hamade:** It's under Confidential.

**Marilyn Waidelich:** There you got it.

**Marilyn Waidelich:** Oh, I found it.

**Marilyn Waidelich:** Okay.

**Marilyn Waidelich:** Yeah, we're connected with a few people.

**Marilyn Waidelich:** Like, I know Eric Kropp.

**Marilyn Waidelich:** I don't know if you know him.

**Marilyn Waidelich:** Somewhere.

**Yousef Hamade:** I've got a lot of connections on LinkedIn.

**Yousef Hamade:** So, you know, my background is cybersecurity and IT.

**Yousef Hamade:** I help manage both here at GrowthX.

**Yousef Hamade:** GrowthX, as an overall organization, is a little over a year old in its current firm, but was founded at the end of December of last year.

**Marilyn Waidelich:** When I joined in January, we were about 25 people, and now we're about 75 people.

**Yousef Hamade:** Wow.

**Yousef Hamade:** And continue to grow, and we help organizations like Abnormal with third GTM needs in terms of generating traffic content, you know, making sure you show up in AI responses, and all those other good things that help with your organization's visibility.

**Yousef Hamade:** And so from one aspect, we are viewed as a marketing agency.

**Yousef Hamade:** From other aspects, we are a human augmented AI marketing agency.

**Yousef Hamade:** That's kind of a very simple way of viewing it.

**Yousef Hamade:** That being said, we would like to get to SOC2 in the next several months.

**Yousef Hamade:** It's obviously having good email security is a key cybersecurity control that we want to have in place.

**Yousef Hamade:** Given the partnership between GrowthX and Abnormal, I think it makes sense to take a good look at you guys first.

**Yousef Hamade:** That being said, I did take a look at you guys in a previous life many months ago.

**Yousef Hamade:** And I've since killed all those brain cells. But while I'm very familiar with email security and the email security space, I kind of forget most about how your tool actually works and integrates with our Google workspace, and I may ask a bunch of dumb questions as a result of that.

**Marilyn Waidelich:** No, makes sense.

**Marilyn Waidelich:** And hopefully I can answer all of them.

**Marilyn Waidelich:** If it's one that I don't know, I can get my solutions engineer, who's my technical counterpart, aligned to you guys and make sure I get it answered.

**Marilyn Waidelich:** So it makes sense.

**Marilyn Waidelich:** And yeah, I love that we're using you too, because one thing about Abnormal is we like, they purchase products for us to use that all have to do with AI, so we can move faster and smarter.

**Marilyn Waidelich:** And I actually sold to Abnormal at my past company, and I loved that about them, that they like really implement these AI driven products like yours into our environment.

**Yousef Hamade:** So yeah, that's really cool.

**Yousef Hamade:** I love the partnership.

**Yousef Hamade:** So we're more of a service to you, but that's, that's fine.

**Yousef Hamade:** If you actually go take a look at some of your blog content — that's actually content that GrowthX is generating on your behalf.

**Marilyn Waidelich:** Oh, so you did that.

**Marilyn Waidelich:** Okay.

**Yousef Hamade:** Cool.

**Yousef Hamade:** That's what the organization is doing because that drives organic traffic to your site and helps you guys rank in AI responses and things like that.

**Yousef Hamade:** When people ask about, hey, what good email security tools should I be looking at for, you know, my Google's workspace users to protect against business email compromise?

**Marilyn Waidelich:** Yeah.

**Marilyn Waidelich:** Yeah.

**Yousef Hamade:** Love it.

**Marilyn Waidelich:** Okay.

**Yousef Hamade:** This is super helpful.

**Marilyn Waidelich:** So just a few quick questions for you and then maybe if it would be helpful, I can go into just a refresher overview and like quick demo or something.

**Marilyn Waidelich:** But just want to understand, so you're on Google today, you have a hundred mailboxes that you'd be looking to protect.

**Marilyn Waidelich:** Yes.

**Yousef Hamade:** And that's like.

**Yousef Hamade:** That's kind of the, how do non-human accounts work for you guys?

**Yousef Hamade:** Because some of those are shared mailboxes and things like that.

**Marilyn Waidelich:** We won't license anything that's a shared mailbox, just the warm body mailboxes.

**Yousef Hamade:** Yeah, so that's where our difference in number of, is it 75, is it 100?

**Marilyn Waidelich:** Okay, so maybe we call it 75 then?

**Marilyn Waidelich:** Yep.

**Marilyn Waidelich:** Okay.

**Marilyn Waidelich:** And then Google today, how is it working for you?

**Marilyn Waidelich:** Are you seeing specific attacks bypassed that have kind of led to you reaching out?

**Marilyn Waidelich:** Has there been any attacks that are concerning more than others?

**Yousef Hamade:** Or is it really just SOC 2, like we just want to get email security?

**Yousef Hamade:** Well, we're a new startup and luckily any of the attacks against us have been very basic so far and easy for our users to spot. You know, people like to impersonate our CEO or other folks in very low-level sort of phishing, spear phishing — those sort of campaigns that everybody is kind of used to.

**Yousef Hamade:** Like Google itself hasn't been doing a fantastic job of identifying and flagging those things.

**Yousef Hamade:** And, you know, so we really are looking for, you know, we may not turn off the feature of Google, but, you know, we're looking for a more purpose-driven solution.

**Yousef Hamade:** And then I know with other tools, sometimes they include various, you know, we'll call it phishing tests or even user training modules and things like that for not just email.

**Yousef Hamade:** Well, but overall, world-level security training, I just don't know what you guys are offering in that space there.

**Yousef Hamade:** And then outside of email, you know, Google Drive and those other sort of things, what are you guys doing for security there these days?

**Marilyn Waidelich:** Okay, got it.

**Marilyn Waidelich:** So it sounds like so far today, there's kind of the executive impersonations.

**Marilyn Waidelich:** Is there any kind of, like, vendor invoice fraud that you're experiencing?

**Yousef Hamade:** So luckily, our, you know, finance guy is pretty adept at spotting those because he is experienced and he knows to look out for them.

**Yousef Hamade:** But, you know, that's because we're still 75 people and have the finance guy, you know.

**Yousef Hamade:** And so, but, you know, if someone were to slip malware into one...

**Yousef Hamade:** So those things, would he catch that or not?

**Marilyn Waidelich:** Okay, great.

**Marilyn Waidelich:** So it sounds like it may be something you're interested in exploring, how to protect against.

**Yousef Hamade:** Okay.

**Marilyn Waidelich:** And then final one, are you seeing any account takeovers?

**Marilyn Waidelich:** So, you know, we're an actual attacker who's getting login credentials from an employee at GrowthX and then coming on top of an existing email thread, like anything from internal to internal traffic?

**Yousef Hamade:** Not yet.

**Yousef Hamade:** So, again, like for that, you know, strong auth and things like that, we are currently using Google Native Authentication.

**Yousef Hamade:** We're going to be switching that very soon to our OctaAuth, which does enforce strong MFA.

**Yousef Hamade:** And so, you know, getting into that is going to be pretty hard for folks.

**Marilyn Waidelich:** You just answered one of my other questions.

**Marilyn Waidelich:** So thank you.

**Marilyn Waidelich:** Okay.

**Marilyn Waidelich:** So you're on Google.

**Marilyn Waidelich:** You've been to Okta for MFA.

**Marilyn Waidelich:** It sounds like you're not doing any kind of like phishing simulations or training yet.

**Yousef Hamade:** that's up in the air.

**Marilyn Waidelich:** Yes.

**Marilyn Waidelich:** And then anything like for endpoint detection response, like CrowdStrike?

**Yousef Hamade:** Yeah.

**Yousef Hamade:** So we were on Sentinel-1.

**Marilyn Waidelich:** Sentinel-1.

**Yousef Hamade:** Okay.

**Yousef Hamade:** These days.

**Yousef Hamade:** So, and we do have their MDR as well.

**Yousef Hamade:** So.

**Marilyn Waidelich:** Awesome.

**Yousef Hamade:** I know everybody likes to integrate with CrowdStrike.

**Yousef Hamade:** Like, nah, I'm CrowdStrike guy.

**Marilyn Waidelich:** No, we have a, we have a partnership with them, but we also are REST API.

**Yousef Hamade:** So we'll be able to integrate into any of the tools that you want us to integrate into.

**Marilyn Waidelich:** So we'll, at the right time, you know, my solutions engineer and I can kind of walk you through that and best practices there.

**Marilyn Waidelich:** Definitely Okta.

**Yousef Hamade:** And we are, we also do have Kanji deployed on all of our corporate owned devices and do have device trust.

**Yousef Hamade:** And up between Kanji and Okta, so we can actually use our machines as a device factor.

**Yousef Hamade:** Not everybody has corporate managed devices, but those who do, we can use it for device trust.

**Marilyn Waidelich:** Okay, awesome.

**Marilyn Waidelich:** Great.

**Marilyn Waidelich:** That is super, super helpful.

**Marilyn Waidelich:** Sounds like executive impersonations we're experiencing today, vendor invoice fraud a little bit, but finance team is crushing it on stopping those.

**Marilyn Waidelich:** And then account takeovers, not so much, but all of them can be top of mind.

**Marilyn Waidelich:** Those are all big buckets that we plan to.

**Marilyn Waidelich:** And then we also do have some different like add-ons, which I'll share.

**Marilyn Waidelich:** And we could kind of see where your head's at on some of these things.

**Marilyn Waidelich:** So would it be helpful if I just kind of give you like a quick high-level overview of our offerings and just who we are?

**Marilyn Waidelich:** Or do you feel good on who we are and maybe just get into like the offerings and a quick demo?

**Marilyn Waidelich:** Like what would be most valuable?

**Yousef Hamade:** Yeah.

**Yousef Hamade:** I know who you guys are.

**Yousef Hamade:** Let's go with offerings and demo.

**Marilyn Waidelich:** Okay, perfect.

**Marilyn Waidelich:** Don't want to waste any time.

**Marilyn Waidelich:** All right.

**Marilyn Waidelich:** So really, these are the top, you guys can see my screen, okay, right?

**Marilyn Waidelich:** Yes.

**Marilyn Waidelich:** Okay, these are the top four use cases that we're helping our customers with.

**Marilyn Waidelich:** So that first bucket I already just talked about, it's that advanced email threats, the executive impersonations, vendor invoice fraud, really our bread and butter product.

**Marilyn Waidelich:** It's our inbound email security.

**Marilyn Waidelich:** The second is account compromise.

**Marilyn Waidelich:** Legacy tools, they're not scanning internal to internal traffic, and attackers are able to get login credentials, even if you have a lock down place, we've seen it happen, where an account's compromised, right?

**Marilyn Waidelich:** And then they come on top, they do an attack, it's never going to get stopped because they're not even scanning that.

**Marilyn Waidelich:** So these attacks, we can help.

**Marilyn Waidelich:** It's a big differentiator.

**Marilyn Waidelich:** The third is just automating the whole process.

**Marilyn Waidelich:** That's right.

**Marilyn Waidelich:** So if a user does go, sounds like your employee base right now is really good at spotting them.

**Marilyn Waidelich:** When they do go and report that attack potentially, you know, instead of your team or whoever over at GrowthX having to like manually triage those, we're going to take care of that autonomously, remediate them for you.

**Marilyn Waidelich:** And then we have a nice window visibility into that for your team to see as well, which I could show you in the demo.

**Marilyn Waidelich:** So it's our AI security mailbox.

**Yousef Hamade:** And with all these male solutions, like dealing with false positives tends to be more problematic than anything else.

**Yousef Hamade:** so wanting to make sure that we have, you know, that's easy to deal with either through self-service and self-service policies or even at an administrative level going in there.

**Marilyn Waidelich:** And I'm tweaking a lot of this and things.

**Marilyn Waidelich:** Just like that, too.

**Yousef Hamade:** Exactly.

**Marilyn Waidelich:** Yeah.

**Marilyn Waidelich:** And you hit the nail on the head there because what our AI security mailbox is actually going to do is if those end users, it will close that feedback loop with the end user without you having to do anything.

**Marilyn Waidelich:** So we have pre-generated AI responses for that and saying like, hey, no, this is marked safe because X, Y, Z.

**Marilyn Waidelich:** Or if you want it to go do another passive analyzation, then we could do that.

**Marilyn Waidelich:** But if it was a false positive, granted, no email security tool is ever perfect, then okay, we can go ahead and for future no to let those ones through.

**Marilyn Waidelich:** But our efficacy is very, very high.

**Marilyn Waidelich:** So if we get to a point of you doing a risk assessment with us, you'll be able to actually see that false positives aren't common with abnormal.

**Marilyn Waidelich:** really is a set it and forget it tool where you aren't needing to maintain, make rules, tune, do anything, really.

**Marilyn Waidelich:** It's a whole new way of thinking about email security, really.

**Yousef Hamade:** Now, when it does...

**Yousef Hamade:** So when, like, to me, one of the most annoying thing of some of the email security tools is like some of the email digests and things like that, that you may get once a day or something like that.

**Yousef Hamade:** Do you guys have better integrations with, say, Slack or something like that?

**Yousef Hamade:** So when things are being held, like notifications can be more real time, but less annoying?

**Marilyn Waidelich:** Yeah, no, I definitely, I definitely know that we integrate, we're at SAPI, so I know we can integrate.

**Marilyn Waidelich:** I want to check exactly on, like, the notifications.

**Marilyn Waidelich:** I don't think we're sending out, I mean, if, if a user wants something to be sent out, like a report, I think we can do that, but I don't think we're proactively doing that.

**Yousef Hamade:** I mean, everybody has held messages all the time, right?

**Marilyn Waidelich:** And, like, sometimes those held messages are things that actually should come through.

**Marilyn Waidelich:** You're saying the quarantine — no, we don't do any of that.

**Yousef Hamade:** Oh, yeah, definitely not.

**Marilyn Waidelich:** Yeah, so with those, you know.

**Marilyn Waidelich:** I remember at one of my old companies, we had a vendor, and I was like, where's this email?

**Marilyn Waidelich:** And it was just in some sandbox that I'd then go in and release.

**Marilyn Waidelich:** It's a terrible user experience.

**Marilyn Waidelich:** No, but yeah, you won't be dealing with that here.

**Marilyn Waidelich:** Okay.

**Yousef Hamade:** No sandboxing.

**Yousef Hamade:** They just show up in spam folder then or something like that.

**Marilyn Waidelich:** Yeah, so if it's not malicious, and this is actually getting to this third bucket here, sometimes not every email is malicious, right?

**Yousef Hamade:** Yep.

**Marilyn Waidelich:** You don't want it in your inbox.

**Marilyn Waidelich:** It's spam, right?

**Marilyn Waidelich:** So what we have is an add-on called Graymail, and what the platform is going to be able to do is actually, since we have that normal baseline of behavior for your organization, we'll be able to say, okay, these are all of the emails that Yousef needs to see to get his job done.

**Marilyn Waidelich:** Like, they're important emails, and they should be in his primary inbox.

**Marilyn Waidelich:** Everything else is going to be sorted into what we call Graymail, and then Graymail is going to be actually to ask an app,

**Marilyn Waidelich:** Where it's basically taking all those spams that aren't malicious, putting it in a different folder.

**Marilyn Waidelich:** Now, let's say you go in your gray mail and you're like, hey, why wasn't that in my primary inbox?

**Marilyn Waidelich:** All you have to do is drag it and then for future, our behavioral model will know, okay, these emails, Yousef actually wants in its primary inbox.

**Marilyn Waidelich:** And in the future, all those will be sent to your primary inbox.

**Yousef Hamade:** Okay.

**Yousef Hamade:** What about stuff that does get false positives?

**Marilyn Waidelich:** So a false positive, let me actually show, yeah, I'll show you that in a demo.

**Marilyn Waidelich:** Basically what you'll do though, is if you go in and you're like, okay, abnormal marked, this is malicious and it's not.

**Marilyn Waidelich:** Then what you'll do is you'll essentially just click a button and I can show you how to do it.

**Marilyn Waidelich:** You'll mark it as safe and then it sends it, you'll click submit a detection 360 case.

**Marilyn Waidelich:** It takes like one second to click this button and then automatically that's going to go into a second round of analysis in our platform.

**Marilyn Waidelich:** And we're going

**Marilyn Waidelich:** We're come back to you and say no, like, or we're going to say, hey, this is why we marked it, blah, blah, blah, for future, we're going to learn and all of these ones we will, you know, it's going to continuously learn and develop.

**Marilyn Waidelich:** So ones that come in like that will not be marked.

**Marilyn Waidelich:** Or if we're like, no, like, this is malicious or something, we'll come back to you with the reasonings why and kind of a detection report onto like the analysis there.

**Yousef Hamade:** Yeah.

**Yousef Hamade:** Okay.

**Yousef Hamade:** And I assume you guys also do that with links, not just attachments?

**Marilyn Waidelich:** Yeah, yeah, or attacks.

**Marilyn Waidelich:** So just be all, yeah.

**Marilyn Waidelich:** Yeah.

**Marilyn Waidelich:** Okay.

**Marilyn Waidelich:** And then the fourth bucket, so I already talked about is graymail, and we are actually, we just released, I need to like make sure it's out officially, but our AI phishing coach, so we're kind of making our way into that training space.

**Marilyn Waidelich:** We're not as big or developed as like a know before or other platforms.

**Marilyn Waidelich:** We're more, it's more of like a targeted, but you can kind of see the roadmap and direction we're headed.

**Marilyn Waidelich:** With launching this.

**Marilyn Waidelich:** So that's one area we're playing in.

**Yousef Hamade:** Do you guys do phishing sims as well?

**Marilyn Waidelich:** Or is that part of that?

**Marilyn Waidelich:** Yeah, it is part of that.

**Marilyn Waidelich:** And what I can do, because that area is so new, I'd have to have my solutions engineer review it with you.

**Marilyn Waidelich:** But what I could do on a follow-on is like have him show you a demo too.

**Yousef Hamade:** Gotcha, okay.

**Marilyn Waidelich:** Okay.

**Marilyn Waidelich:** So yeah, basically our goal is to be at that behavioral AI platform for your email security.

**Marilyn Waidelich:** InBounds are a core product.

**Marilyn Waidelich:** These are all add-ons.

**Marilyn Waidelich:** And this is typically what makes up our offerings.

**Marilyn Waidelich:** So maybe what I'll do is just quickly jump into a quick demo and then show you an example of an executive impersonation.

**Marilyn Waidelich:** Since that was one that you mentioned.

**Marilyn Waidelich:** So first, when you get access to this, you're going to be able to jump in here into your dashboard.

**Marilyn Waidelich:** And this is really the one-stop shop of what's going on.

**Marilyn Waidelich:** So you're going to see the number of attacks stopped.

**Marilyn Waidelich:** What's the attack frequency?

**Marilyn Waidelich:** By which types?

**Marilyn Waidelich:** You can even see like, you know, phishing, social engineering, invoice payment fraud, and so on.

**Marilyn Waidelich:** Go down here, you'll be able to see the different trending attacks.

**Marilyn Waidelich:** You'll able to see the strategy of the attack, even the origin, where are they coming from?

**Marilyn Waidelich:** Who's attacking you most frequently?

**Marilyn Waidelich:** From what country?

**Marilyn Waidelich:** Blah, blah, blah.

**Marilyn Waidelich:** Then you can even see the most impersonated entities and recipients from employees.

**Marilyn Waidelich:** So it's giving you this really nice window of visibility into your kind of threat landscape site and just attacks.

**Marilyn Waidelich:** So this is a nice place that you need to go to like, you know, the executives or report, make reports, whatever it is, kind of that, that one, nice job shop.

**Marilyn Waidelich:** Where you're going be spending most of your time is in a threat log.

**Marilyn Waidelich:** This is where all of the attacks that our platform has stopped and remediated are going to live.

**Yousef Hamade:** Just going back for a second, on the impersonation side, we actually feed everybody's personal emails in as a secondary email within Google.

**Yousef Hamade:** So...

**Yousef Hamade:** From our HRS, HCM system.

**Yousef Hamade:** So we have all their secondary email addresses.

**Yousef Hamade:** So, you know, if I email in from my personal email address, is it going to pick that up or is it going to enjoy that?

**Marilyn Waidelich:** So it is going to pick it up. And actually, this is a really good example of what I was just going to show you.

**Marilyn Waidelich:** And one thing, too, is when we get integrated into your Google environment, what we do is we integrate.

**Marilyn Waidelich:** That takes like 60 seconds.

**Marilyn Waidelich:** We look back like 45 to 9 days.

**Marilyn Waidelich:** We get an understanding of what's normal behavior for growthx.

**Marilyn Waidelich:** So if that is normal behavior for you guys, it's not going to be a signal that we're like, oh, this is weird that it was from the personal email.

**Marilyn Waidelich:** It's only the things that are outside of your guys' unique normal behavioral basis.

**Yousef Hamade:** baseline, that are going to get blocked.

**Yousef Hamade:** Gotcha.

**Marilyn Waidelich:** So a quick example here for you is, let's just use this one.

**Marilyn Waidelich:** So what do we have?

**Marilyn Waidelich:** Let's look at the email.

**Marilyn Waidelich:** We have Jonathan Green, the CFO at enterprise.com.

**Marilyn Waidelich:** So for you, that'd be growthx.com.

**Marilyn Waidelich:** Reaching out to Josh Waters, Senior Director of Accounting.

**Marilyn Waidelich:** And he's saying, Josh, can you assist in getting two checks out today for vendor ProLea Systems?

**Marilyn Waidelich:** I'm not available at the moment, but will you get the consolidated wiring, blah, blah, blah, blah.

**Marilyn Waidelich:** Yeah.

**Marilyn Waidelich:** Yeah.

**Marilyn Waidelich:** Okay, he's asking for a payment.

**Marilyn Waidelich:** There's no links.

**Marilyn Waidelich:** There's no attachments.

**Marilyn Waidelich:** It's sent from an iPhone.

**Marilyn Waidelich:** Very much like you just said, could be sent from a personal Gmail account, right?

**Yousef Hamade:** That's a reputable domain.

**Marilyn Waidelich:** Maybe not.

**Marilyn Waidelich:** sense.

**Marilyn Waidelich:** Although this, maybe not.

**Marilyn Waidelich:** Even though this NVT8765, it's a little suspicious, right?

**Yousef Hamade:** Like, yeah.

**Yousef Hamade:** domain.

**Marilyn Waidelich:** It could very well be annoying.

**Marilyn Waidelich:** It's not going to get stopped by a traditional tool.

**Marilyn Waidelich:** And the reason is because it's going to pass all these sender authentications to a domain.

**Marilyn Waidelich:** There's no known bad.

**Marilyn Waidelich:** There's no bad links, no attachments.

**Marilyn Waidelich:** There's nothing that these older security tools are programmed to look forward to stop something like this.

**Marilyn Waidelich:** Other than the same name matching.

**Marilyn Waidelich:** So what do we do with that integration?

**Marilyn Waidelich:** Like I mentioned, we're ingesting all these different signals.

**Marilyn Waidelich:** And for this specific attack, you can see over 43,000 signals were analyzed.

**Marilyn Waidelich:** Although not one single signal is deterministic, our platform is going to populate the top ones for you to review.

**Marilyn Waidelich:** For this specific one, you can see that out of 8,000 emails that have been sent from Jonathan Green, zero have ever been sent from this account.

**Marilyn Waidelich:** So we're going to say possible executive impersonation.

**Marilyn Waidelich:** This is weird.

**Marilyn Waidelich:** Here, Josh Waters and Jonathan Green.

**Marilyn Waidelich:** And even though they're both in finance and in the same department, they've actually never corresponded over email before.

**Marilyn Waidelich:** So that's weird.

**Marilyn Waidelich:** That's a typical contact, impossible communication, whatever it be.

**Marilyn Waidelich:** It's pretty straight, for example.

**Marilyn Waidelich:** And then here, using our natural language processing computer vision, we're actually able to pick up on words like financial request, urgent, and figure out the overall tone of the message and flag that as a suspicious financial request.

**Marilyn Waidelich:** So then from there, what we're going to do is we're going to automatically remediate this in real time.

**Marilyn Waidelich:** So you can see it came in August 23rd, 10-12.

**Marilyn Waidelich:** It was remediated August 23rd, 10-12, moved to our default, which is our deletions folder.

**Marilyn Waidelich:** And if, in fact, you looked at this and you said, hey, this should have been safe, like this was the false positive, that's where you would click this button, select remediation options.

**Marilyn Waidelich:** You'd mark it as safe.

**Marilyn Waidelich:** You'd submit a detection 360 case.

**Marilyn Waidelich:** You'd like to remediate.

**Yousef Hamade:** So that would be the process for a false positive.

**Yousef Hamade:** That's cool.

**Yousef Hamade:** How the you in this context?

**Yousef Hamade:** Is that me as Yousef, the IT administrator, or me as Yousef, as one of the people copied on the emails, right?

**Marilyn Waidelich:** You as Yousef, the IT administrator.

**Yousef Hamade:** Okay.

**Yousef Hamade:** So, how would the user know that this email didn't get delivered, other than looking at their deletions folder, assuming that this goes in their deletions and not some other deletions?

**Marilyn Waidelich:** They wouldn't, because we're taking care of this before it ever hits their inbox.

**Yousef Hamade:** Okay.

**Yousef Hamade:** And when you guys integrate with Google, how is the integration with Google actually occurring?

**Marilyn Waidelich:** Are you guys doing an API-based integration, or are you guys in the mail flow, like?

**Marilyn Waidelich:** Yeah.

**Marilyn Waidelich:** Apologies, because I honestly kind of skipped over.

**Marilyn Waidelich:** How we work, I'll kind of go backwards, but yeah, so basically, I'll show you this.

**Yousef Hamade:** Okay, go ahead.

**Yousef Hamade:** Go ahead, sorry.

**Marilyn Waidelich:** So, you guys are not a secure email gateway, right?

**Marilyn Waidelich:** Yeah, we're not.

**Marilyn Waidelich:** So, what we're going to be doing is, for you in this scenario that we've been talking about, it would really be scenario A.

**Marilyn Waidelich:** 76% of our customers don't use a secure email gateway.

**Marilyn Waidelich:** So, we've taken a complete different approach to email security, and actually, it's why Gartner opened up their first Magic Quadrant since 2014 with Abnormal, because that's like the legacy way of doing things.

**Marilyn Waidelich:** Now, of course, some organizations are going to want that secure email gateway no matter what.

**Marilyn Waidelich:** So, then in that use case, we'll actually supplement it, and we'll say, okay, well, anything that does get through the gateway, that may not be stopped from a known bandwidth.

**Marilyn Waidelich:** Link or a known bad domain.

**Marilyn Waidelich:** That's when we'll come in to get the more A.

**Marilyn Waidelich:** So it's really built to meet your preference and how you want to set up email security in your environment.

**Marilyn Waidelich:** Like, you don't have to do DLP, for example.

**Marilyn Waidelich:** So, like, if you wanted a secure email gateway for that, you could use that.

**Yousef Hamade:** Gotcha.

**Yousef Hamade:** But, like, if, like, by most of the segs in this case, we're talking about the proof points and minecasts of the world, right?

**Yousef Hamade:** Like, that's safe.

**Marilyn Waidelich:** Yeah.

**Marilyn Waidelich:** Actually, a lot of my boss and majority of my team all came from proof points and most of our leadership.

**Marilyn Waidelich:** But, yes.

**Marilyn Waidelich:** So, like, proof point and minecasts are huge.

**Yousef Hamade:** Yeah.

**Marilyn Waidelich:** Secure email gateways. You know, there's Microsoft, Proofpoint, Mimecast — we can supplement any of them. I just got off a call with a customer where they layer us on top of their existing gateway.

**Yousef Hamade:** It just depends on what works for you.

**Yousef Hamade:** Like – I'm not going to turn off the Google feature that they give me for free as part of it, too.

**Yousef Hamade:** No.

**Yousef Hamade:** But where they do their thing, but yeah.

**Marilyn Waidelich:** Yeah, we actually would not advise that.

**Marilyn Waidelich:** We advise you to use the native capabilities within Google and then use us to layer on top of that.

**Marilyn Waidelich:** So a little bit about the API integration.

**Marilyn Waidelich:** What we would do is, if you'd like to move forward with evaluating us, we'd do a risk assessment and integrate into your Google environment. It literally takes a few clicks. If we had more time, I could have shown you today, but essentially we let that sit for seven days.

**Marilyn Waidelich:** We schedule a checkpoint seven days after that and we'll come back and we'll do a findings review with you.

**Marilyn Waidelich:** And we'll say, hey, this is all the attacks within seven days that we have picked up on. We'll review it with you. If you want a second checkpoint, we'll do another checkpoint, you know, seven days after that.

**Marilyn Waidelich:** It's optional.

**Marilyn Waidelich:** And then from there, customers typically see everything they need to see.

**Marilyn Waidelich:** And then they decide if they would like to move forward.

**Marilyn Waidelich:** So that's something that we can run with you.

**Yousef Hamade:** So that's part of the, we'll call it sales process as a, you know.

**Marilyn Waidelich:** And it's not a typical like proof of value that's like a lot of lift or stress or whatever.

**Marilyn Waidelich:** Like I, I'm not even kidding when I say the first call is probably 15 minutes max with five of that being the integration.

**Marilyn Waidelich:** And then the kind of findings call can be like an hour.

**Marilyn Waidelich:** So it's like an hour and 15 with no lift, unless you want to go and play around in the portal.

**Marilyn Waidelich:** Because at that first checkpoint, you'll get access to the portal where you can go and play around and it will have all your data.

**Yousef Hamade:** Got it.

**Yousef Hamade:** All right.

**Yousef Hamade:** Cool.

**Yousef Hamade:** I know I think we're actually over time, but can you quickly walk me through modules and pricing?

**Marilyn Waidelich:** Yeah, let me just quick slide through here's what all your modules are.

**Marilyn Waidelich:** So with your user counts, you'll.

**Marilyn Waidelich:** Probably fall out around our minimum, which is 25K.

**Marilyn Waidelich:** So we're 25K minimum.

**Marilyn Waidelich:** Now we can, depending on like how it goes, you know, we could get as much, we'd probably like bundle as much as we can of the products in that 25K.

**Marilyn Waidelich:** Like we want to make it the most value for you, unless you like, if you saw value in all of them, you know, so we would just see like what add-ons or whatever, or you could just do the primary inbound email security.

**Marilyn Waidelich:** So we'd cross that bridge when we get there, but I could send you this and kind of like more on our offerings.

**Marilyn Waidelich:** Really, would, everyone buys inbound email security, and then all of these are optional.

**Yousef Hamade:** Okay.

**Yousef Hamade:** Yes, please.

**Yousef Hamade:** And also like pricing on, on everything.

**Yousef Hamade:** I know, I know we're at or below your minimums, but like, cool.

**Yousef Hamade:** Cool.

**Yousef Hamade:** That doesn't tell me anything, right? In terms of price per user per month, price per user per year, or anything like that. Even if our spend is $14,000 but we have to hit the $25,000 minimum, I need to know that math.

**Yousef Hamade:** Okay, but, like, if we jump up to 200 users, what's the cost going to be?

**Yousef Hamade:** I need to know that.

**Yousef Hamade:** Those, those sorts of things.

**Yousef Hamade:** Um, right, so don't just tell me it's $25,000 minimum.

**Yousef Hamade:** Like, I need to know, like, line out of pricing, what each one of these things is really costing.

**Marilyn Waidelich:** Yeah, um, really just the $25,000 minimum is just because I want to be transparent that if we're not in the ballpark, don't want to waste anyone's time.

**Marilyn Waidelich:** But what we do for getting you an official quote is that we actually go through the channel.

**Marilyn Waidelich:** So, do you have a partner that you'd like to work with?

**Marilyn Waidelich:** Because to get you an official, like, show you the unit pricing, I'd actually have to give it to them to give to you.

**Yousef Hamade:** Okay, so you guys don't do direct sales?

**Marilyn Waidelich:** We primarily sell through resellers. If it's a non-starter, then we will make an exception to do direct, but it's an exception and approval process.

**Marilyn Waidelich:** And like we would need justification of the why, but it can definitely be done.

**Yousef Hamade:** Why is because selling through partners sucks, but.

**Marilyn Waidelich:** You know, it's funny, my last company, it was all direct and here they're very much, you know, channel focused.

**Marilyn Waidelich:** But if you do not want to go through a partner, then we can definitely, you know, make an exception.

**Yousef Hamade:** Give me just a second.

**Yousef Hamade:** So can you tell me if GuidePoint Security is on your partner list?

**Marilyn Waidelich:** They are.

**Yousef Hamade:** They're a really strategic partner of ours.

**Yousef Hamade:** Yeah.

**Yousef Hamade:** Cool.

**Yousef Hamade:** Then I will send you Tom's contact info. Let me just grab this for you. I'll drop it in the chat here. If you guys can loop in Tom, that would be appreciated. Tom is who we bought Sentinel One through, and I've worked with him for like seven or eight years at this point. He's a good contact with a strong relationship that spans from three jobs ago. I did engage him for us here at GrowthX, particularly for stuff like this.

**Yousef Hamade:** And, you know, if they are on your channel, then let's engage Tom.

**Marilyn Waidelich:** Okay, sounds good.

**Marilyn Waidelich:** And, sorry, you said you threw it in the chat.

**Yousef Hamade:** Uh, did I, no, I think I said it.

**Marilyn Waidelich:** Only to my note taker, and not to everybody.

**Yousef Hamade:** I was like, I might be missing it.

**Marilyn Waidelich:** That's my fault. There you go. Now, if for whatever reason you and Tom fall out or don't want to go through Tom, I have other partners I can bring in too.

**Yousef Hamade:** I appreciate that. Like I said, we have an existing relationship through Tom for Sentinel One, so we already have paperwork set up with them, which will make it easier to go through them.

**Marilyn Waidelich:** So do I need to engage Tom, or would you prefer to reach out to him directly and let him know you were talking to me here at GrowthX?

**Yousef Hamade:** I'll reach out to him directly. Don't worry about it.

**Marilyn Waidelich:** And I'll just work on getting him a quote that he can actually turn over to you, and then we can set up a call and review it.

**Marilyn Waidelich:** So you can really look at that line item by line item cost.

**Marilyn Waidelich:** I just keep telling you, based on, you know, I was trying to give you a little bit of range.

**Marilyn Waidelich:** You're probably at that minimum.

**Marilyn Waidelich:** And...

**Marilyn Waidelich:** I wanted to just make sure we weren't like out of the ballpark here, because what we'll need if you do want to do the risk assessment is alignment on timing, which do you have an active project for this, like when you would want to make a decision?

**Yousef Hamade:** Nothing here is an active project.

**Marilyn Waidelich:** It's just, you know, stuff we need to get done.

**Marilyn Waidelich:** How's that?

**Yousef Hamade:** It's on the list of tools that the C-suite knows we need to purchase, and whether or not that's this quarter, given that we've only got a few days less in the quarter, probably not, but I think it is a Q4 sort of timeline that we're looking at.

**Yousef Hamade:** I just need to put together the right stuff with them.

**Yousef Hamade:** You know, I said the same with Sentinel-1, and we ended up closing.

**Yousef Hamade:** In like two and a half weeks, but, you know, this is probably closer to, I'll call it November, time frame.

**Yousef Hamade:** Okay.

**Yousef Hamade:** Just from where management's attention is and all of that, but.

**Yousef Hamade:** Perfect.

**Marilyn Waidelich:** That's all I need.

**Marilyn Waidelich:** Yeah.

**Marilyn Waidelich:** So for the risk assessment, it's that, it's alignment on, you know, ballpark pricing.

**Marilyn Waidelich:** And then I'll also just shoot over in a follow-up, this security hub, just if you want to take a look at all of our accreditations and compliance, it literally is a one-stop shop for anything you could ask before.

**Yousef Hamade:** And part of this management, yeah.

**Marilyn Waidelich:** Yep.

**Yousef Hamade:** Yep.

**Marilyn Waidelich:** Yes.

**Yousef Hamade:** Perfect.

**Yousef Hamade:** All good.

**Marilyn Waidelich:** All right.

**Marilyn Waidelich:** All right.

**Marilyn Waidelich:** Well, thank you so much for your time.

**Marilyn Waidelich:** It was awesome meeting you.

**Marilyn Waidelich:** I'll send a follow-up, recap the next steps, and reach out to Tom.

**Marilyn Waidelich:** I'll get him a quote, and we'll probably touch base, you know, all on a call together to run through some pricing, it sounds like.

**Yousef Hamade:** Great, sounds good.

**Yousef Hamade:** Okay, thank you.

**Marilyn Waidelich:** Thanks, Yousef.
