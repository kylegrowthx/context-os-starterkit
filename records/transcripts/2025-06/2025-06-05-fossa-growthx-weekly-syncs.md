# Fossa <> GrowthX Weekly Syncs

<metadata>
date: 2025-06-05
time: 18:02 UTC
duration: 8 minutes
organizer: aida@growthxlabs.com
participants: Andy Drukarev (FOSSA), Jakub Rudnik (GrowthX), Aida Knežević (GrowthX)
fathom_recording_id: 66778751
fathom_url: https://fathom.video/calls/317657430
share_url: https://fathom.video/share/xnpzBA9s-RYSxs4wgrXVGaHCrsarwSUw
source: fathom
enriched_on: 2026-03-03 12:00 UTC
</metadata>

---

## Summary

FOSSA and GrowthX approved the CVE page mockup and are proceeding with bulk content creation: 375 CVE pages to be generated from 2025 vulnerabilities. Key pending task is adding Marcus (GrowthX engineer) to FOSSA's GitHub; Andy committed to this. The teams also discussed tweaks to the CVE page design (removing MIT license mention, clarifying metrics) and FOSSA's CMS implementation challenges, which is blocking their content team's independent publishing ability.

---

## Context

This is a recurring weekly sync between FOSSA (a developer security company offering OSS compliance and CVE tracking) and GrowthX (a B2B content marketing firm). The teams are collaborating on a 12-month, 1,500-page content project with a quarterly delivery target of 375 pages. FOSSA pays GrowthX to create SEO-optimized pages for CVEs and CWEs (Common Weaknesses). The relationship is mid-project; 20 of 28 planned CWE articles are complete, and now GrowthX is beginning the larger CVE backlog. The contract end date is June 13, 2025, so the team is racing to finalize GitHub access and page generation logic.

---

## Relevance

- **To GrowthX Delivery:** CVE page design approved. Template mirrors FOSSA's existing registry design, scaling pattern to 375 pages. Key design revisions needed: remove MIT license reference (applies to packages, not CVEs), clarify fixture metrics ("9 100% fixed" and "95%" require product owner clarification). Marcus (GrowthX engineer) needs GitHub access to push pages; Aida handling notification and clarification on the metrics detail.

- **To GrowthX Business Development:** Account is on track. Delivered 20 of 28 CWE articles; remaining 8 won't complete in time due to delivery focus on CVE backlog, but contract accommodates this. CVE bulk creation starts immediately upon GitHub access. Project end date is June 13 — tight but achievable given existing Airtable workflow setup. FOSSA's CMS implementation remains challenging ("uphill battle"), but not a blocker for this engagement.

- **To CheckThat:** CVE/CWE generation suggests strong SEO content strategy opportunity. FOSSA's reliance on manual code-level changes (no CMS) shows market gap; CMS and programmatic content publishing are friction points for security companies wanting to scale content.

---

## Overview

- CVE page mockup approved; minor tweaks needed (remove MIT license mention, clarify "9 100% fixed" and "95%" metrics)
- 375 CVE pages to generate from 2025 vulnerabilities; GrowthX has Airtable grid ready to run
- GitHub access for Marcus (GrowthX engineer) pending; Andy committed to adding today
- CMS implementation for FOSSA in progress; facing challenges but not blocking current deliverables
- Contract timeline: June 13, 2025 project end date; team confident in timeline

---

## Key Topics

### CVE Page Development

- Mockup mirrors FOSSA's registry design perfectly; approved by Andy with minor revisions
- Design tweaks required:
  - Remove MIT license mention (applies to software packages, not CVEs)
  - Clarify "9 100% fixed" metric (unknown what it refers to; Aida to ask Marcus)
  - Clarify or remove "95%" metric (unknown context)
  - CVEs can impact multiple package versions with different licenses; design should account for this nuance
- GrowthX to compile prioritized list of CVEs from 2025
- 375 CVE pages ready to generate once GitHub access granted
- Grid/workflow in Airtable already prepared and ready to run

### Project Timeline and Deliverables

  - Contract goal: 1,500 pages over 12 months (375 pages/quarter)
  - Current focus: Delivering backlog of 375 CVE pages
  - Project end date: June 13, 2025
  - 20 CWE articles completed; 8 remaining CWE articles likely won't be completed

### GitHub Access

  - Andy apologized for delay in adding GrowthX engineer to FOSSA's GitHub
  - Aida provided engineer's email in chat
  - Andy to add access today, enabling further development

### CMS Implementation

  - Andy confirmed progress on CMS implementation
  - Facing some internal challenges ("uphill battle")
  - Recognized benefits of CMS for content publishing efficiency

---

## Action Items

**Andy Drukarev (FOSSA)**
- Add Marcus (GrowthX engineer) to FOSSA's GitHub repository using the email address Aida provided in chat.

**Aida Knežević (GrowthX)**
- Notify GrowthX delivery team of Andy's approval of the CVE page design mockup.
- Request removal of MIT license mention from the design.
- Clarify with Marcus what the "9 100% fixed" and "95%" metrics represent, so FOSSA product team can provide clearer requirements.
- Compile a prioritized list of CVEs from 2025 to target for bulk page generation.

---

## Transcript
**Jakub Rudnik:** Right back down, I it's like a very beautiful day today, but we had three days of like vicious heat after cold weather.

**Jakub Rudnik:** just popped up, did that.

**Jakub Rudnik:** How was the long weekend, Andy?

**Andy Drukarev:** Yeah, it was good, busy.

**Andy Drukarev:** A few more days out here in California than back east.

**Andy Drukarev:** Yeah, yeah, all good.

**Andy Drukarev:** So first, I have to apologize because I am way late on adding your engineer to our GitHub.

**Andy Drukarev:** I hope to do that today.

**Andy Drukarev:** Can you remind me the email?

**Andy Drukarev:** I guess it would be probably on the meeting invite as well.

**Aida Knežević:** I'm not, he hasn't been invited to this meeting, so I'm going to drop it in the chat.

**Andy Drukarev:** All right, and is, would that be the one associated with his GitHub?

**Andy Drukarev:** Do we know?

**Andy Drukarev:** Ah, good question.

**Aida Knežević:** Okay, let me ask him.

**Aida Knežević:** Okay, so yeah, they have to be linked.

**Aida Knežević:** Okay, great.

**Aida Knežević:** So did you get the chance to take a look at the CVE page that HeVibe Coded?

**Aida Knežević:** I did not.

**Andy Drukarev:** Did you share that?

**Andy Drukarev:** I apologize.

**Aida Knežević:** No, we shared it at the beginning of the week, but it's totally fine if you didn't see it.

**Aida Knežević:** I can share my screen.

**Aida Knežević:** So this is what it looks like, basically.

**Andy Drukarev:** Nice.

**Andy Drukarev:** That mirrors registry beautifully.

**Jakub Rudnik:** Yeah, it seemed like it went pretty quickly.

**Jakub Rudnik:** Like, crazy how live coding can be so effective if done well, so it's wild.

**Andy Drukarev:** Yeah.

**Andy Drukarev:** Yeah, this is awesome.

**Andy Drukarev:** Let's build it.

**Andy Drukarev:** Great.

**Aida Knežević:** So yeah, we'll let them know that you approved this.

**Aida Knežević:** And yeah, we can start knocking out the 300 plus pages.

**Aida Knežević:** It's 375 to be exact.

**Aida Knežević:** So we have a grid set up in Aerofs that's pretty much ready to run.

**Aida Knežević:** The one thing that we need to know from you is, do you want us to select CVEs?

**Aida Knežević:** Or do you have like a priority list that you want to share with us?

**Aida Knežević:** No?

**Aida Knežević:** Okay.

**Andy Drukarev:** Sorry, going back to the page, the CVE page.

**Andy Drukarev:** So there's a few things that we would need to tweak, obviously.

**Andy Drukarev:** This mentions the MIT license, but...

**Andy Drukarev:** That applies to software packages, not CVEs.

**Andy Drukarev:** So like that wouldn't be relevant here.

**Andy Drukarev:** I don't know what the 9, 100% fixed is in relation to, or the...

**Andy Drukarev:** Kind of 95% number.

**Andy Drukarev:** So it might just be that we kind of remove that whole little module.

**Andy Drukarev:** Okay, okay.

**Aida Knežević:** I'll let them know.

**Aida Knežević:** Yeah.

**Andy Drukarev:** Yeah, because ultimately CVs can, you know, impact more than one version of the package, right?

**Andy Drukarev:** It could impact, you know, whatever, Postgres 1.5 through 1.10, and, you know, those versions could have different licenses, so on and so forth.

**Andy Drukarev:** Mm-hmm.

**Aida Knežević:** Okay, okay.

**Aida Knežević:** So just to check, so you want to remove the 95% one, and then...

**Aida Knežević:** MIT.

**Andy Drukarev:** Okay.

**Andy Drukarev:** I mean, I don't know what 9 100% fixed means, so that might be relevant, but I need to understand what it is.

**Andy Drukarev:** Okay, okay.

**Andy Drukarev:** That sounds good.

**Aida Knežević:** I'll ask Marcus in chat later.

**Aida Knežević:** Yep, great.

**Andy Drukarev:** Okay, perfect.

**Aida Knežević:** So I'll just put together a list of CVEs from this year that we could target for these pages.

**Aida Knežević:** And then it should be pretty easy to generate them and push them live to your site. Once you give Marcus access to your GitHub, we should be all set on that front.

**Aida Knežević:** Our end date is June 13th, so we have plenty of time to get everything in order by then.

**Andy Drukarev:** Excellent.

**Andy Drukarev:** We're still working on the CVEs.

**Andy Drukarev:** Sorry, the CWE series.

**Aida Knežević:** Ah, okay.

**Aida Knežević:** Yeah, that completely slipped my mind.

**Aida Knežević:** Are you any closer to implementing the CMS perhaps?

**Andy Drukarev:** Hmm.

**Jakub Rudnik:** Aida asking the questions that are keeping Andy up at night.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** Yeah.

**Andy Drukarev:** I say the answer to that question is yes.

**Andy Drukarev:** Okay.

**Andy Drukarev:** You know, I'm fighting somewhat of an uphill battle there.

**Aida Knežević:** No, I get it.

**Aida Knežević:** I was actually editing an article today for another client that was about just basically when it's like time to like upgrade your website and stuff like that.

**Aida Knežević:** And it was literally like your content team can't publish anything on your site because you don't have a CMS.

**Aida Knežević:** That was one of the reasons that AI came up with.

**Aida Knežević:** And I was like, oh, I know a case like this.

**Aida Knežević:** Yeah.

**Andy Drukarev:** I mean, I love the ability to go directly and make changes on the code level.

**Andy Drukarev:** Like that's great.

**Andy Drukarev:** It's just there are some situations where like CMS would be useful.

**Andy Drukarev:** Anyway.

**Andy Drukarev:** Yeah.

**Andy Drukarev:** totally get it.

**Andy Drukarev:** Neither here nor there.

**Andy Drukarev:** I think for, so, so for the CWE articles, we have, you know, kind of our, I guess, what, 20 that have been, that have.

**Andy Drukarev:** Done, and then we're probably not going to be able to get to the last eight.

**Andy Drukarev:** Is that right?

**Aida Knežević:** Yeah, so the last eight were, I mean, the ones that we did were basically during the weeks when we weren't delivering anything to you.

**Aida Knežević:** And so to put things to sort of get into the contract, so basically we were supposed to deliver you 1,500 pages over a 12-month period.

**Aida Knežević:** So over three months, that's 375 pages.

**Aida Knežević:** So now we're going to just deliver this backlog, and you're going to have those CWE pages in addition to that.

**Aida Knežević:** We were just, you know, were delivering them just to kind of have something, you know, that you could publish on your website in the meantime.

**Aida Knežević:** Yep, yep.

**Andy Drukarev:** Okay.

**Andy Drukarev:** Sounds good.

**Andy Drukarev:** I'll work on getting Marcus access to our GitHub, and we'll go from there.

**Andy Drukarev:** Okay, perfect.

**Aida Knežević:** Thank you.

**Aida Knežević:** Cool.

**Andy Drukarev:** Anything else?

**Andy Drukarev:** No, not from my end.

**Andy Drukarev:** Great.

**Andy Drukarev:** Great.

**Andy Drukarev:** Thank you.

**Aida Knežević:** See you next week.

**Aida Knežević:** Bye-bye.
