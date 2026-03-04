# External Partner - Product Walkthru of BHE 

<metadata>
date: 2025-11-06
time: 22:22 UTC
duration: 32 minutes
organizer: erik@growthx.ai
participants: Erik O'Brien, Meshach Cisero, Jonathan Parfait
fathom_recording_id: 99898078
fathom_url: https://fathom.video/calls/464892406
share_url: https://fathom.video/share/gac7rF49J19jg5XPRMmNDk-kt_zBNX2x
source: fathom
enriched_on: 2026-03-02 16:45 UTC
</metadata>

---

## Summary

Walkthrough of Bloodhound Enterprise (BHE) for a content partner.

---

## Context

Erik O'Brien from GrowthX, a B2B content marketing agency, met with Jonathan Parfait and Meshach Cisero from SpecterOps to understand Bloodhound Enterprise (BHE) for content development purposes. GrowthX partners with organizations to create targeted content that improves AI visibility and search rankings, and SpecterOps is a content partner. The meeting was primarily educational—Jonathan gave Erik a comprehensive walkthrough of BHE's product experience, use cases, and market positioning so that Erik could develop marketing and educational content informed by real customer context and BHE's messaging framework.

---

## Relevance

- **To GrowthX Delivery:** SpecterOps is a content partner. Understanding BHE's technical messaging, analogy frameworks (the Manhattan/fortress model), and customer pain points (prioritization via Exposure metric) directly informs content strategy for identity security and attack path management.
- **To GrowthX Business Development:** SpecterOps operates in the identity security space with focus on pen testing and attack path management. BHE targets Identity Security teams, technical CISOs, and post-pen-test scenarios. M&A due diligence is a high-value use case. Opportunity for GrowthX to co-market or develop vertical-specific content (financials, manufacturing).
- **To CheckThat:** BHE uses AI-driven analysis to identify and prioritize attack paths. The concept of data-driven risk prioritization via metrics (Exposure %) parallels CheckThat's approach to AI visibility—quantifying and prioritizing impact at scale rather than manual analysis.

---

## Overview

- **Proactive Defense:** BHE builds a "fortress" around critical assets (Tier 0) by mapping all attack paths and identifying "chokepoints"—single remediation points that neutralize many paths at once.
- **Prioritization with Metrics:** The "Exposure" metric quantifies risk as the % of identities that can abuse a path. This data-driven prioritization ensures teams fix the most impactful issues first, avoiding guesswork.
- **Open Source vs. Enterprise:** BHE automates the manual analysis of the open-source Bloodhound CE, providing dashboards, metrics, and built-in remediation guidance essential for enterprise scale.
- **Key Personas & Use Cases:** BHE is sold to Identity Security teams and technical CISOs, often after a pen test using Bloodhound CE reveals risk. M\&A due diligence is a key use case.

---

## Key Topics

### The Problem: Active Directory Security

  - Active Directory (AD) is a legacy identity provider not built for modern security threats.
  - Attackers exploit complex, organic relationships within AD to escalate privileges and compromise critical assets.
  - The goal is to prevent attackers from reaching these high-value targets, such as Domain Admins.

### The Solution: Bloodhound Enterprise (BHE)

  - BHE provides a proactive defense by building a "fortress" around critical assets (Tier 0).
  - **Process:**
    1.  **Identify Tier 0:** Automatically discovers critical assets (e.g., Domain Admins).
    2.  **Map Paths:** Uses collectors (`SharpHound` for AD, `AzureHound` for Azure/Entra ID) to map all possible attack paths to Tier 0.
    3.  **Find Chokepoints:** Identifies single points where remediation neutralizes multiple paths.
  - **Prioritization:** The "Exposure" metric quantifies risk, enabling teams to fix the most impactful issues first.
      - **Example:** A finding with 99% exposure is "Critical" because nearly all identities can abuse it.

### Product Experience & Key Metrics

  - **Attack Paths Page:** The homepage lists findings (chokepoints) with severity based on Exposure. Each finding includes a description and remediation guidance.
  - **Posture Dashboard:** Tracks risk reduction over time.
      - **Exposure:** Overall risk trend.
      - **Attack Paths:** Total number of paths. Remediation of a single chokepoint can cause a drastic drop (e.g., 40% in a 2-week trial).

### Customer Profile & Use Cases

  - **Personas:**
      - **Red Teams:** Often the initial contact, but typically lack budget.
      - **Identity Security Teams:** The primary buyers with budget.
      - **Technical CISOs:** Understand the problem from a pen-testing background.
  - **Sales Trigger:** Often reactive, following a pen test where consultants used Bloodhound CE and recommended the enterprise version.
  - **Key Use Case: M\&A Due Diligence:** Rapidly assess the risk of an acquired company.

### Competitive Landscape & Misconceptions

  - **Competitors:** BHE is 100% focused on proactive attack path management.
      - **CrowdStrike Identity:** A reactive tool focused on alerting on active attacks, not preventing the paths themselves.
  - **Misconception:** That Bloodhound CE can be used for enterprise-level defense.
      - **Reality:** CE is a manual tool for pen testers. BHE automates analysis, provides metrics, and includes remediation guidance, which is essential for scale.

---

## Action Items

- **Erik O'Brien (growthx.ai):** Use this context to inform content development.
- **Erik O'Brien (growthx.ai):** Contact Jonathan Parfait or Meshach Cisero with follow-up questions.

---

## Transcript
**Meshach Cisero:** This meeting is being recorded.

**Meshach Cisero:** Walk us through the product experience and really had with the customer lens in mind.

**Meshach Cisero:** He's one of our SEs and then Erik is one of our agency partners, Jonathan, that helps us kind of grow some of our content via their really kind of awesome AI workflow to kind of help us identify opportunities to increase our, I guess, LLM search visibility.

**Meshach Cisero:** So I think, you know, helping them walk through the product will give a better kind of insight into how we speak, how our customers are leveraging our product for value and really kind of helping kind of bring some of that context into some of the content that they write for us.

**Meshach Cisero:** So I will let Jonathan take it from here and Erik, feel free to, you know, give yourself an introduction if I didn't do it justice, but.

**Erik O'Brien:** No, you covered it.

**Erik O'Brien:** Yeah, good to go.

**Erik O'Brien:** Good to meet you, Jonathan.

**Jonathan Parfait:** I'll give you a quick introduction about myself.

**Jonathan Parfait:** So I've been at SpecterOps for going on three years now.

**Jonathan Parfait:** Majority of that time was actually as a technical account manager, working with our customers, making sure they're enabled on the product and really just successful and reducing them out of risk in their organization using Bloodhound Enterprise.

**Jonathan Parfait:** And then switched over to a sales role about a year ago around this time.

**Jonathan Parfait:** So I guess to kind of get started, Erik, like how familiar are you with the concepts around identity security, active directory?

**Erik O'Brien:** might just give us a good starting point on where to like start the conversation.

**Erik O'Brien:** Yeah, I know what those words mean, but I would say I'm not an expert by any means.

**Jonathan Parfait:** You're good.

**Jonathan Parfait:** No, that's good context.

**Jonathan Parfait:** definitely appreciate transparency.

**Jonathan Parfait:** Let's see.

**Jonathan Parfait:** I mean, I'll start by like...

**Jonathan Parfait:** like...

**Jonathan Parfait:** I'll start with just Active Directory as a whole, right?

**Jonathan Parfait:** I'm going try to boil down a very, like, foundational thing for organizations into something that's hopefully digestible.

**Jonathan Parfait:** But really, when I look at Active Directory, it's really one, like, a telephone book, if you would, for, like, your users, right?

**Jonathan Parfait:** And that was kind of a starting point, was that you had this concept of just, like, a user account.

**Jonathan Parfait:** You use that user account for whatever you need to do to get your task done.

**Jonathan Parfait:** Active Directory has been around for a very long time.

**Jonathan Parfait:** When I say a long time, like, in some of our older organizations, you're looking at, I don't know, let's say probably 20, 30 years, maybe even 40 years, right?

**Jonathan Parfait:** So, a lot of what we play into is the fact that these, this foundational concept of Active Directory has existed for a very long time.

**Jonathan Parfait:** It's always been used as a provider of, an identity provider, basically, and allowing for you to access resources, right?

**Jonathan Parfait:** a provider, Right.

**Jonathan Parfait:** And that's really how it was viewed when it was created.

**Jonathan Parfait:** And really wasn't of the mindset of the security implications of that, right?

**Jonathan Parfait:** And, you know, who is an administrator?

**Jonathan Parfait:** Who has control over certain things from an Active Directory standpoint?

**Erik O'Brien:** Are you following me there?

**Jonathan Parfait:** Yep.

**Jonathan Parfait:** Cool.

**Jonathan Parfait:** So within Active Directory, have various users.

**Jonathan Parfait:** You have some users that are like yourself and myself, where even from like a SpecterOps perspective, right?

**Jonathan Parfait:** I know a lot about security.

**Jonathan Parfait:** I know a lot about IT.

**Jonathan Parfait:** But like I have no reason to be an administrator of anything, right?

**Jonathan Parfait:** Because all I am is a consumer of, you know, the applications that are hosted.

**Jonathan Parfait:** But in certain situations, like you need to be an administrator.

**Jonathan Parfait:** Furthermore, not only do you need to be an administrator of an application, you need to be an administrator of the domain totally, right?

**Jonathan Parfait:** And you actually are the person that configures settings for that domain.

**Jonathan Parfait:** And that's a lot of what we focus in on, right?

**Jonathan Parfait:** Is from like a, from the Active Directory perspective, you have certain assets or identities that are happening.

**Jonathan Parfait:** So far-reaching privileges, like a domain administrator or an enterprise administrator.

**Jonathan Parfait:** We kind of use this example to kind of really explain what we do without getting too in the weeds of like active directory terminology.

**Jonathan Parfait:** And I'm going to try to emulate Justin Kohler by no means am I Justin Kohler.

**Jonathan Parfait:** But this is his kind of his example that he provides, right?

**Jonathan Parfait:** So really when we look at active directory security as a whole, you know, one is Bloodhound from its original concept, right?

**Jonathan Parfait:** When it was originally released to the public and used internally by our pen testing teams, the overall goal of Bloodhound was really to understand from the attacker mindset, what are the possible ways that an attacker could actually compromise a domain fully or gain access to something like a domain admin account?

**Jonathan Parfait:** Um,

**Jonathan Parfait:** And it works really well from that perspective.

**Jonathan Parfait:** And that's really the persona that our open source or community edition really speaks to is more like that red team mindset of I have an asset.

**Jonathan Parfait:** How do I transition from this asset, like your user account, into someone that is of the level of having very high privileges or very far-reaching privileges like a domain administrator?

**Jonathan Parfait:** What we found over time was that that works perfectly for an attacker, but from the defensive perspective, really we need a bit more, right?

**Jonathan Parfait:** And really what we should focus in on are the assets that are critical.

**Jonathan Parfait:** So I mentioned domain administrators having far-reaching privileges, their critical assets, privileged assets within Active Directory.

**Jonathan Parfait:** Think of Manhattan as exactly that.

**Jonathan Parfait:** So we've got Google Maps here.

**Jonathan Parfait:** I've got home of Louisiana.

**Jonathan Parfait:** That's where I'm based out of all the way down South Louisiana and Manhattan, New York.

**Jonathan Parfait:** So let's pretend I am...

**Jonathan Parfait:** The victim here and the attacker wants to get to Manhattan.

**Jonathan Parfait:** This is basically what we'd call an attack path, right?

**Jonathan Parfait:** It's a path from point A to point B that an attacker could take to actually compromise Manhattan, in this case, or your tier zero objects.

**Jonathan Parfait:** So when we look at it from a strategic perspective, we know where an attacker wants to get to.

**Jonathan Parfait:** We don't always know where they're coming from.

**Jonathan Parfait:** So really what we want to do is build a fortress around what we know and what we know we want to protect.

**Jonathan Parfait:** In doing that, really what we look at is establishing what we call a tier zero asset group, where we would actually house, in this case, like, Manhattan, basically, do exactly what we did on the open source side.

**Jonathan Parfait:** We map every possible way that an attacker could take to actually get to one of these assets.

**Jonathan Parfait:** And we do that for every single identity within a customer's environment.

**Jonathan Parfait:** The next thing we do is we want to tackle and make sure we're prepared.

**Jonathan Parfait:** Prioritizing the right way, There's lots of attack paths.

**Jonathan Parfait:** There's lots of relationships that exist between user A and user B in Active Directory just organically, setting aside the risk element of it just in order for things to function correctly.

**Jonathan Parfait:** So really what we focus in on is where does a user, or in this case, a customer, where they want to focus their mediation efforts, and how can we make it to where it's the most efficient way possible?

**Jonathan Parfait:** And really how we approach that is by establishing that asset group.

**Jonathan Parfait:** But also when we're mapping the attack paths, rather than focusing right here, so let's say we're in Houma, and we want to get to Manhattan.

**Jonathan Parfait:** We could focus in on shutting down this path here, right?

**Jonathan Parfait:** Let's say we want to just make it to where it's not possible for me to get to it via PICI.

**Jonathan Parfait:** All that means is an attacker can come back here and get to it through South Alabama and get to Manhattan, right?

**Jonathan Parfait:** The more sustainable approach

**Jonathan Parfait:** This is a very simple example, but it really speaks to what the mindset here is when we focus on the findings in Bloodhound enterprise, really what we say is, let's shut down, make it to where the attacker cannot navigate any of the bridges going into the island of Manhattan.

**Jonathan Parfait:** So now we have built a secure fortress around our protected identities, and that way it doesn't really matter where the attacker can get to right here, because foundationally, all we're concerned about is making sure that the attacker can't get to Manhattan.

**Erik O'Brien:** Are you following there?

**Jonathan Parfait:** Does that make sense?

**Jonathan Parfait:** Yep.

**Jonathan Parfait:** Awesome.

**Jonathan Parfait:** So there's a couple things we do there.

**Jonathan Parfait:** One is we identify what we call these choke points.

**Jonathan Parfait:** That's exactly what this would be.

**Jonathan Parfait:** So, like, the Lincoln Tunnel here, the bridge right here between Jersey City and New York, or Lower Manhattan.

**Jonathan Parfait:** This is what we call choke points, right?

**Jonathan Parfait:** These are...

**Jonathan Parfait:** There are areas where if a customer focuses remediation efforts to make it to where an attacker cannot get to your, get to Manhattan in this case, via those routes, we basically neutralize the attacker.

**Jonathan Parfait:** We have achieved the goal of making sure that an attacker cannot get to our critical assets.

**Jonathan Parfait:** That's exactly what we're focusing on.

**Jonathan Parfait:** The other piece there is like, you can see right here where we've got one, two, three, four, five, six, seven, eight or so paths.

**Jonathan Parfait:** I'll just guesstimate here.

**Jonathan Parfait:** Let's call it eight, right?

**Jonathan Parfait:** Another thing we want to focus on is the fact that or the concept that an attacker may be able to navigate these particular access points.

**Jonathan Parfait:** But which ones are the most critical, right?

**Jonathan Parfait:** Which ones are ones that everyone has access to?

**Jonathan Parfait:** Let's say there's like a toll or something like that that exists in one of these bridges.

**Jonathan Parfait:** It's less likely that everyone will go that way because it's not free, right?

**Jonathan Parfait:** So let's shut down the areas where we know that 100.

**Jonathan Parfait:** 100% of the people in America can get to it this way, or the attackers in this case can get to it this way.

**Jonathan Parfait:** You want to focus on your remediation efforts on that one first, right?

**Jonathan Parfait:** So helping us customers prioritize that risk that exists in the environment.

**Jonathan Parfait:** I think we're good on the analogy here.

**Jonathan Parfait:** So I'm going to switch back.

**Jonathan Parfait:** I'm going switch over into Bloodhound Enterprise.

**Jonathan Parfait:** So when we look at Bloodhound Enterprise, this is basically what we do.

**Jonathan Parfait:** I'll throw out some terminology here.

**Jonathan Parfait:** That way you just have situational awareness, especially when you're looking at our documentation or look at some of our webinars as well.

**Jonathan Parfait:** So the way we achieve that goal in mapping everything is through currently two collectors.

**Jonathan Parfait:** One is a collector called SharpHound, and that's used to collect information from Active Directory.

**Jonathan Parfait:** The other collector is called AzureHound, and that's used to collect information about Azure and IntraID.

**Jonathan Parfait:** In both situations.

**Jonathan Parfait:** And that's where we actually analyze all that data.

**Jonathan Parfait:** And this is basically the end result of the analysis.

**Jonathan Parfait:** And this is what we call our attack pass page.

**Jonathan Parfait:** And this is the homepage that every single user of the product lands into.

**Jonathan Parfait:** You know, we touched on critical apps.

**Jonathan Parfait:** This is a lot of things that probably won't be very familiar to you.

**Jonathan Parfait:** But when we speak to, like, I do, identity security and cyber security.

**Jonathan Parfait:** Customers or potential customers, you know, they understand the concepts of things like domain admins group and the risks there.

**Jonathan Parfait:** So we don't usually have to get too complex in, like, the definitions there, right?

**Jonathan Parfait:** It's kind of like a well-known term around what's privileged and active director.

**Jonathan Parfait:** We do add some additional enrichments that, like, we really look at the concept, and achieve that goal from an attacker perspective.

**Jonathan Parfait:** Yeah.

**Jonathan Parfait:** But by and large, this is all like concepts that are very familiar to a customer.

**Jonathan Parfait:** But this is your tiers of our asset group.

**Jonathan Parfait:** Kind of like some key things here in how we approach this, right?

**Jonathan Parfait:** So one thing I always emphasize to my customers and potential customers is like we're automatically identifying a lot of this stuff, right?

**Jonathan Parfait:** So and the reason why I do that is because I want to make sure they understand that like once they actually install the collectors and they successfully collect, we're going to automatically identify the privileged resources that we know we can identify automatically, and we're going to analyze that data.

**Jonathan Parfait:** So the expectation is when they successfully collect, we go through our analysis process, they're going to get a general understanding of where their risk is and what their risk is for their organization.

**Jonathan Parfait:** And that is produced with this metric here that we call exposure.

**Jonathan Parfait:** Again, this goes back to prioritizing.

**Jonathan Parfait:** So exposure within the BHU product really represents...

**Jonathan Parfait:** The percentage of users or computers identities that can actually abuse that attack path.

**Jonathan Parfait:** going back to the example with, you know, the bridges and saying that there's one bridge that we know that everyone can access freely, no issues, we want to shut that one down first.

**Jonathan Parfait:** That's exactly what exposure speaks to.

**Jonathan Parfait:** So really helping customers understand, one, in this particular case, what's their security risk?

**Jonathan Parfait:** It's not uncommon for us to load data and we see 100% exposure.

**Jonathan Parfait:** It happens quite often.

**Jonathan Parfait:** The other piece of that is now we're looking at kind of like these choke points over to the right or the findings.

**Jonathan Parfait:** For each of these findings, we have this critical moderate load, the severity labeling.

**Jonathan Parfait:** That's all based on the exposure metric.

**Jonathan Parfait:** So you can see here for this particular finding here.

**Jonathan Parfait:** So that's why we're representing it as critical is because there's 99% exposure.

**Jonathan Parfait:** Same thing goes for this one here.

**Jonathan Parfait:** You can see exposure is 44%, so that's why we're showing that the exposure for the attack path or the choke point is 44%.

**Jonathan Parfait:** We kind of provide a description of why we're calling it as a risk.

**Jonathan Parfait:** So for this one, for example, it's because if you own an object in Active Directory, you can basically make any change you want to it.

**Jonathan Parfait:** And again, this is all around identities within Active Directory that should not have the ability to take control or make changes to your quote-unquote tiers or objects or those critical assets.

**Jonathan Parfait:** For each of these findings, we'll give remediation guidance to the customer on how to actually fix it.

**Jonathan Parfait:** So that's pretty, pretty crucial.

**Jonathan Parfait:** The main reason why, and sorry, I'm kind of going in and out of like a very technical talk track and then like a little bit more...

**Jonathan Parfait:** Like, some of highlights we provide from a marketing perspective because I'm trying to, like, thread the needle here.

**Jonathan Parfait:** But one of things we like to highlight here as well is, you know, with open source, there are customers or potential customers that have used open source to kind of achieve some of these defensive concepts.

**Jonathan Parfait:** A lot of the challenge with that is the fact that you're manually analyzing this stuff and it's not really based on, like, metrics like exposure, right?

**Jonathan Parfait:** So it's a bit of a guessing game.

**Jonathan Parfait:** Sure, you can find some things, but to find everything, it's a bit challenging on the CE or open source side.

**Jonathan Parfait:** Again, that's the reason why we developed Enterprise.

**Jonathan Parfait:** But a big part of that is making sure that those customers that have used open source before realize that, one, they're no longer going to have to be burdened with analyzing this data manually.

**Jonathan Parfait:** It's really about allowing the Enterprise version to do that for you, produce the metrics, help you prioritize.

**Jonathan Parfait:** As well as from, like, a...

**Jonathan Parfait:** From a remediation standpoint, a lot of those customers that have used Community Edition in the past, they have to manually produce some of these remediation gadgets, right?

**Jonathan Parfait:** Where we have it built into the product and it's a lot easier, it's a little bit easier for not only the administrators to consume and those power users, but also potentially even other teams are tasked with actually like the individual task of remediating the findings.

**Jonathan Parfait:** Any questions so far?

**Erik O'Brien:** Nothing specific to the product yet.

**Jonathan Parfait:** Okay, cool.

**Jonathan Parfait:** Trying to think of other areas.

**Jonathan Parfait:** So typically during demo, we'll touch on this part.

**Jonathan Parfait:** And then the next thing we focus on is posture.

**Jonathan Parfait:** So basically posture is like our main dashboard page for the product.

**Jonathan Parfait:** It tells you a few things.

**Jonathan Parfait:** One is, again, just your general.

**Jonathan Parfait:** Like, health check on where things stand today.

**Jonathan Parfait:** can see in this particular, you can see the changes over time as well.

**Jonathan Parfait:** You can see areas where maybe it went down to 99%.

**Jonathan Parfait:** This is a demo environment.

**Jonathan Parfait:** Ideally, in customer environments, we're going to see that the exposure, you know, kind of dip lower and lower progressively as they're executing on remediations.

**Jonathan Parfait:** Same thing for, so this is exposure.

**Jonathan Parfait:** You can also look at dashboarding around the number of findings that exist in an environment during a given period of time.

**Jonathan Parfait:** Same thing for this attack path metric here.

**Jonathan Parfait:** And this is really intended to, one, show the level and the scale of risk in the organization based off of the actual relationships leading up to one of those choke points.

**Jonathan Parfait:** And really, it's intended to kind of show the fact that as you're working through

**Jonathan Parfait:** You're reducing that risk progressively, and in most cases at very large intervals, meaning if you remove one of those findings on the first page, you stand to see a lot of those attack paths drop down quite drastically.

**Jonathan Parfait:** I mean, we've seen things like during trials, like a, I think it was like a 40% reduction in attack paths, and that was just during like a two-week trial frame, or a two-week trial period.

**Jonathan Parfait:** So, very impactful.

**Jonathan Parfait:** And then over to the left is basically a listing of all the attack paths that have existed in the environment, as well as like the current count and net change over time.

**Jonathan Parfait:** Honestly, as far as like the product, this is really like the high-level overview.

**Jonathan Parfait:** Do you have any questions, or any areas that you want to focus in on a bit more from like just additional context?

**Erik O'Brien:** I think on the product, I've got a pretty good understanding.

**Erik O'Brien:** I guess when it comes to customers, who are you guys talking to most often?

**Erik O'Brien:** Is it the identity teams, or is it kind of red team security practitioners?

**Erik O'Brien:** Yeah, it's a mix.

**Jonathan Parfait:** would say like, kind of like our first wave of customer was definitely red teams, right?

**Jonathan Parfait:** Like that was our core use case or users from like a bloodhound open source perspective.

**Jonathan Parfait:** We still speak to a lot of red teamers.

**Jonathan Parfait:** In general, what tends to happen, at least in the accounts I've worked with, is like we'll start with the red team and potentially transition into like an identity security team, exposure management or attack surface management type team.

**Jonathan Parfait:** That's really where we get a lot of traction in terms of like them having the budget to buy something.

**Jonathan Parfait:** Red teamers is a bit challenging because sometimes they don't have that much budget.

**Jonathan Parfait:** And then, yeah, like, CISOs, especially those CISOs that are a lot more technical, right?

**Jonathan Parfait:** They understand the problem.

**Jonathan Parfait:** Maybe they've historically been, like, pen testers or red teamers.

**Jonathan Parfait:** We tend to get a lot of traction from those types of personas.

**Jonathan Parfait:** It's a bit diverse.

**Jonathan Parfait:** One, because identity security as a practice for a lot of organizations is something that's kind of the latest thing, right?

**Jonathan Parfait:** So a lot of times you won't have, like, a defined identity security team, per se, which you may have as a team that's focused in on administrating things like Active Directory and Azure and InterID.

**Jonathan Parfait:** So it's about really understanding within the organization who is kind of the responsible party in terms of risk in the environment, especially when it relates to, like, things like pen testing and identity security.

**Erik O'Brien:** Our identity as a whole.

**Erik O'Brien:** Then I guess if you had to split like prospective customers out from like those that are reacting to something that's happened versus those that are proactive, how would you split that out?

**Jonathan Parfait:** That's a tricky one.

**Jonathan Parfait:** I think what we see most often is it's more on the reactive side, and it's mainly because, especially here lately, I think we've seen a lot more customers that have gone through pen tests annually in the past.

**Jonathan Parfait:** And during that pen test, consultants used Bloodhound, open source.

**Jonathan Parfait:** And then in the reporting and in the outbrief of that pen test, they were told that they used Bloodhound, and then they realized that we have an enterprise version.

**Jonathan Parfait:** I failed to mention that earlier because I got really deep into like explaining what...

**Jonathan Parfait:** We do, but like overall, Bloodhound is kind of like the standard when it comes to how can you identify from an identity perspective, how to kind of like maneuver within environment from a pen testing perspective.

**Jonathan Parfait:** I mean, we're talking like 80% 90% of all pen tests are using Bloodhound, the open source version, to actually identify that.

**Jonathan Parfait:** Quick note on Verticals, like Verticals, where it's played really, really well is like financials, like we play very well in the financial industry.

**Jonathan Parfait:** Engineering, like manufacturing, we've got some customers that are manufacturing as well.

**Jonathan Parfait:** The one that really shines the most for us is actually like financials.

**Erik O'Brien:** Oh, let's see.

**Erik O'Brien:** Oh, let's see.

**Erik O'Brien:** Yeah, think you covered most of the kind of pre-baked questions I had for you.

**Jonathan Parfait:** Man, I'm not that good.

**Erik O'Brien:** Well, you covered the analogy.

**Erik O'Brien:** It was super helpful.

**Jonathan Parfait:** That kind of led me to come to my own conclusions there.

**Erik O'Brien:** But I guess, is there any kind of misconceptions about Bloodhound that you guys want to get out in front of?

**Erik O'Brien:** Or is there, you know, I think we heard in the kickoff, like, you guys are trying to create this new identity attack path management kind of category.

**Erik O'Brien:** How is that separate from, like, what you guys may see from other competitors?

**Jonathan Parfait:** You know, I think the biggest thing from a competitive standpoint is that, like, we are 100% focused on really...

**Jonathan Parfait:** The attack path management concept, right?

**Jonathan Parfait:** There's a lot of companies out there that have, and they do it actively, right?

**Jonathan Parfait:** Like there's other companies out there that are focused on other areas of security and then have kind of expanded their platform into identity security.

**Jonathan Parfait:** So someone like a CrowdStrike, for example, right?

**Jonathan Parfait:** They are, they basically are an EDR provider that uses signals based on their EDR collector, plus an acquisition that they did to produce output from an identity security perspective.

**Jonathan Parfait:** While they're a competitor, they're really not because they don't even do the same thing that we do, right?

**Jonathan Parfait:** We are very invested and pro, or sorry, invested and focused on the proactive concept of making sure it's not possible for an attacker to maneuver, whereas there's other solutions out there like CrowdStrike Identity that's more focused on like, hey, like we'll alert.

**Jonathan Parfait:** Do preventions based off of what's actively happening in your environment.

**Jonathan Parfait:** I mean, a lot of that comes down to, like, it's not a very sustainable approach when you look at realistically, right?

**Jonathan Parfait:** It would be better to be a bit more proactive and shut down those paths versus, like, trying to sit adjacent to them and maybe do some interrupts or even just alerting based off of behavior.

**Jonathan Parfait:** One big misconception that I think I'm always interested in us conveying is, you know, the possibility of using CE at an enterprise level.

**Jonathan Parfait:** It really just isn't possible.

**Jonathan Parfait:** I think that's probably one of the larger assumptions that a customer will make.

**Jonathan Parfait:** And I don't think it's a fault of anything we do necessarily.

**Jonathan Parfait:** I think we're doing a better job of, like, drawing distinction between the two.

**Jonathan Parfait:** But I think just naturally as consumers, we think anytime there's a product and there's, like, a community edition or a light or starter version that it's somehow, like, a trimmed-down capability that is actually, like, achievable.

**Jonathan Parfait:** And it's a very...

**Jonathan Parfait:** There's dark difference between the two, and I can actually kind of show you what the difference is, right?

**Jonathan Parfait:** So if you wanted to use Bloodhound Community Edition, this is the only page that you would get.

**Jonathan Parfait:** So you can search for things.

**Jonathan Parfait:** You can do kind of like that Google Maps point A to point B thing.

**Jonathan Parfait:** You can do these cipher queries where basically you can like do free text queries against the data set.

**Jonathan Parfait:** But I don't think a lot of customers out there, potential customers out there, realize how daunting this task actually is to actually produce risk set versus using the enterprise version, where this is only included in the enterprise version, where we're analyzing data for you, giving you that prioritized guidance and remediation guidance.

**Jonathan Parfait:** This is really the more sustainable approach, and I think a lot of customers out there make the assumption that they can like.

**Jonathan Parfait:** We use our free version to do that.

**Jonathan Parfait:** But it does come up.

**Jonathan Parfait:** I mean, it's something that comes up during trials, especially if, or even conversations with customers, especially if they've used it in the past.

**Jonathan Parfait:** But again, it's really just about educating them on the differences and showing the value, or the benefits, really.

**Jonathan Parfait:** I'm trying to think of other things.

**Jonathan Parfait:** Meshach, anything you could think of?

**Meshach Cisero:** I think you got most of them.

**Meshach Cisero:** I'm trying to think of that as well, but I think you covered most.

**Jonathan Parfait:** Again, like, I am, I was just, I used to be a customer of Bloodhound Enterprise, too.

**Jonathan Parfait:** And, like, one of the reasons why we bought it was because, like, we were going through a merger and acquisition, and, like, we had no idea.

**Jonathan Parfait:** of the risk levels of the organization that we were actually merging with, right?

**Jonathan Parfait:** So it really spoke to the use case, and we have this use case, and we've got white papers on it, which is like this M&A concept, right?

**Jonathan Parfait:** Where you have organizations that, at scale, that's how they grow, right?

**Jonathan Parfait:** They acquire companies.

**Jonathan Parfait:** In order to do that, you have to be very rapid in understanding, one, from a risk perspective, who you're acquiring, and then also how do you manage that risk?

**Jonathan Parfait:** So I definitely think there's like some tie-ins there from a marketing standpoint in terms of like getting that messaging out in a very eloquent way in which like when CISOs are actually going through that M&A process, they have the understanding that they can use a tool like this to actually help them make sure things stay secure.

**Jonathan Parfait:** Yep.

**Jonathan Parfait:** Another thing, I'm just thinking out loud here, but like another thing, isn't that like we really try

**Jonathan Parfait:** Try to convey during our demos as well as like from marketing perspective is like how crucial it is that we're putting metrics alongside these findings, right?

**Jonathan Parfait:** And what I mean by that is even when we generate certain findings within the platform, like there's other tools out here that will tell you if you have this particular finding in your environment.

**Jonathan Parfait:** The challenge is when you have 10 of these in your environment, right?

**Jonathan Parfait:** And which ones do you prioritize?

**Jonathan Parfait:** I think any person that's of a project management background would say, hey, I've got a year to achieve it.

**Jonathan Parfait:** We'll break it up into four quarters of work.

**Jonathan Parfait:** That's 25 and we're good to go, right?

**Jonathan Parfait:** You're either super lucky and you find the thing that's really, really bad.

**Jonathan Parfait:** That's really, really bad.

**Jonathan Parfait:** That's like the ticking time bomb in your environment.

**Jonathan Parfait:** You're either super lucky.

**Jonathan Parfait:** You can get that on the first go just blindly or you're really unlucky and you wait a whole year, right?

**Jonathan Parfait:** So being able to...

**Jonathan Parfait:** To really bubble and bring to light where risk exists in the environment from a very factual basis is super crucial for our customers and actually helps them to a large degree reduce the risk in their environment very quickly.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** I know we're a little bit over time as well.

**Erik O'Brien:** I want to be respectful of your time.

**Erik O'Brien:** I think I've got enough, at least from a kind of top-down level view of kind of Bloodhound Enterprise.

**Erik O'Brien:** Again, that analogy really is helpful.

**Jonathan Parfait:** So whoever came up with that, genius.

**Jonathan Parfait:** Our VP of product, Justin Kohler.

**Jonathan Parfait:** I'm giving him a look at it.

**Erik O'Brien:** Yeah, if there's any other follow-up questions or if I have any other kind of general questions as we get into some of the content development, I think I got your email, so I might just ping you.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Or work through Meshach to kind of coordinate additional follow-ups, but super appreciate the time and the walkthrough.

**Meshach Cisero:** Yeah, thank you, Jonathan, for sure.

**Jonathan Parfait:** I really do appreciate it as well.

**Jonathan Parfait:** Yeah, of course.

**Meshach Cisero:** Happy to help anytime.

**Meshach Cisero:** Sorry about starting the meeting off a little late, guys.

**Meshach Cisero:** I know it's late in the evening, but the quarter-hour start throws me off just a little bit.

**Jonathan Parfait:** throws you off, yeah.

**Jonathan Parfait:** All right, guys, good chatting with you all.

**Meshach Cisero:** You too.

**Meshach Cisero:** See ya.
