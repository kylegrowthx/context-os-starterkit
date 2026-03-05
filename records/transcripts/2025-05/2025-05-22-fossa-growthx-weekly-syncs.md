# Fossa <> GrowthX Weekly Syncs

<metadata>
date: 2025-05-22
time: 18:01 UTC
duration: 13 minutes
organizer: Aida Knežević (aida@growthxlabs.com)
participants: Marcus Derencius, Aida Knežević, Jakub Rudnik, Kyle Gaudreau, Andy Drukarev, Aaron Williams, Kevin Wang
fathom_recording_id: 64243877
fathom_url: https://fathom.video/calls/306864805
share_url: https://fathom.video/share/skia-8xA4yYk6FnjDji39cfnxsBxzvRz
source: fathom
enriched_on: 2026-03-04 14:30 UTC
</metadata>

---

## Summary

GrowthX and FOSSA aligned on the workflow for building CVE (Common Vulnerabilities and Exposures) pages: Marcus will create a process to pull data from three source websites via APIs or scraping, process it, and populate a template, with the first CVE page targeted for completion by end of day. The team clarified that GrowthX will manually trigger updates initially, though they discussed potential for future automation with daily checks for data changes. Andy agreed to discuss design and publishing approach (including possible GitHub integration) with FOSSA engineers, while Jakub and Aida emphasized GrowthX's commitment to supporting the project over the next month and identified the CWE series publication as a parallel priority requiring workarounds due to the lack of a CMS.

---

## Context

FOSSA is a software security company that GrowthX is partnering with to build CVE (vulnerability) content. This is a content production engagement where GrowthX delivers the editorial work and data collection strategy, while FOSSA provides the domain expertise and publishing infrastructure. The relationship is time-bound to approximately one month from this meeting (mid-May 2025), creating urgency around completing current projects (CVE pages and the CWE series) and identifying high-impact work that can be handed off or completed before the engagement ends. Both teams are working through technical constraints—primarily the lack of a content management system on FOSSA's side—which is requiring them to problem-solve around GitHub integration and manual processes.

---

## Relevance

**To GrowthX Delivery:**
- CVE page workflow requires pulling data from multiple APIs/sources and ensuring accurate, complete extraction of security metrics—demonstrates need for robust data pipeline development skills and attention to data quality in technical content.
- Identified need to work around lack of CMS with GitHub-based publishing, showing adaptability to client infrastructure constraints.
- Confirmed one-month window (through mid-June) for project completion raises stakes on prioritization and hand-off quality.

**To GrowthX Business Development:**
- FOSSA engagement is revenue-generating content work ($200k+/year category), with potential for expansion if CWE series and CVE work succeed.
- Client expressed appreciation for proactive support and willingness to extend engagement if additional high-impact work is identified.
- CMS-less publishing constraint suggests potential upsell opportunity around content infrastructure consulting.

**To CheckThat:**
- CVE and CWE content directly relevant to security-focused AI visibility; opportunity to audit how well this content appears in LLM outputs and knowledge bases.
- Security vulnerabilities and CWE topics may have high AI-engine search volume; potential for CheckThat positioning within the security software vertical.

---

## Overview

- Marcus will develop a workflow to pull, process, and publish CVE data, starting with a sample CVE to test the process
- Updates to CVE pages will need to be manually triggered by GrowthX, with potential for future automation
- First CVE page expected to be ready by end of day, pending successful data retrieval
- FOSSA team to provide more clarity on design and publishing process after internal engineering discussion

---

## Key Topics

### CVE Page Template and Data Sourcing

  - Template shared by Aida contains necessary information
  - Data to be pulled from three websites via APIs or scraping
  - Challenge: Ensuring accurate extraction of all details, especially security metrics
  - Goal: Find a CVE example with comprehensive information to populate the full template

### Data Refresh Process

  - GrowthX to manually trigger updates initially
  - Potential for daily automated checks for changes in source data
  - Ideal scenario: Set up notifications for updates to trigger corresponding changes
  - Need to monitor all three source websites for complete updates

### Timeline and Next Steps

  - Marcus aims to have first CVE page ready by end of day, pending successful data retrieval
  - Andy to discuss design and publishing process with FOSSA engineers
  - Consideration of GitHub integration for content management

### Ongoing Partnership and Additional Support

  - GrowthX team (Jakub/Aida) offering continued support for the next month
  - Focus on wrapping up existing projects and identifying areas for additional assistance
  - Emphasis on completing CWE series publication
  - Acknowledgment of challenges due to lack of CMS, working on solutions

---

## Action Items

**Marcus Derencius (GrowthX)**
- Start CVE page build process: get data from the three source websites, process via workflow, and populate template for one comprehensive CVE example by end of day

**Andy Drukarev (FOSSA)**
- Call with FOSSA engineers to discuss CVE page data flow and publishing process (including GitHub integration approach), then report back to team

- After initial CVE page build is complete, evaluate design aspects and discuss with team

**Jakub Rudnik (GrowthX)**
- Proactively identify additional high-impact projects that GrowthX can help complete before engagement end date (mid-June)

---

## Transcript

**Andy Drukarev:** I'm running around to do various things, but all right. How about you all?

**Jakub Rudnik:** Good, good. Same exact thing.

**Marcus Derencius:** Yeah, I'm here in San Francisco and it's got some interesting work going on. Nice, nice.

**Aida Knežević:** So, yeah, for today, I mean, we're basically going to discuss the build process for the CVE pages.

**Aida Knežević:** I shared the template with everyone, but I'm going to drop the link again in the chat.

**Aida Knežević:** And, yeah, mean, Andy, you can take it away with any questions that you have.

**Aida Knežević:** And I think Marcus, you know, can figure out how he can best support.

**Aida Knežević:** Yeah.

**Andy Drukarev:** No, I think this, like, feels like it has the information, obviously, that we need.

**Andy Drukarev:** I mean, I think the question becomes, like, uh...

**Andy Drukarev:** First of all, how are we actually pulling in this data?

**Andy Drukarev:** How often is it refreshed?

**Andy Drukarev:** So on and so forth.

**Andy Drukarev:** kind of what the backend would actually look like.

**Marcus Derencius:** Okay, so we're going to have a workflow, so that will be the process we can trigger as needed.

**Marcus Derencius:** And the workflow starts from getting the information, processing, and populating the template, and then publishing.

**Marcus Derencius:** So that's the workflow.

**Marcus Derencius:** just have to define which are going to be the first ones we're going to start.

**Marcus Derencius:** And then—okay, so great.

**Aida Knežević:** You want to pick, like, do you need a specific CVE number that we can, we're going to generate?

**Marcus Derencius:** Yeah, just to have the most different ones—because the template has a lot of information, not all CVEs have all the details. So just to have a good example, we have, like, one that has a lot of information, and one that has just a little bit, just to have some examples.

**Marcus Derencius:** Then we do the process of getting all the data, processing, and populating the template. You're doing that with APIs, right?

**Aida Knežević:** Sorry?

**Aida Knežević:** You're using APIs to get the data?

**Marcus Derencius:** Yes, so you've got, like, three websites, so you can see how we can access it, if it's API or scraping.

**Aida Knežević:** Okay.

**Marcus Derencius:** If the data is going to be well organized, then we can make sure we have consistency.

**Marcus Derencius:** All right, so the challenge now is to see if we can get, like, the privilege, right?

**Marcus Derencius:** Just as everyone, we have security metrics.

**Marcus Derencius:** If we can get every detail correctly from the source, it should be API or scraping.

**Marcus Derencius:** So that's, like, the most challenge to get the information.

**Aida Knežević:** OK, all right.

**Aida Knežević:** That makes sense.

**Aida Knežević:** Andy, do you have, like, a list, like, because you're closer to the industry than we are, are there any, like, specific CVEs that you think would be a good place for us to start?

**Aida Knežević:** I don't know, like, or we can just, I can just go and do some, like, keyword research and see which ones are interesting from, like, a volume standpoint.

**Aida Knežević:** But, yeah, just curious.

**Andy Drukarev:** I mean, I would just pick one.

**Andy Drukarev:** Like, to me, the initial is less about search volume and traffic, more about figuring out what the process is for building and maintaining them. So I think we just pick one and run with it. Okay.

**Aida Knežević:** Marcus, do you want to do the one that I picked out in the template?

**Aida Knežević:** Does that seem like a good one for you?

**Marcus Derencius:** Yeah, I started kind of doing that already.

**Marcus Derencius:** I got through the CV, went through the three websites.

**Marcus Derencius:** was going through every field we have in the template and see where is that information exactly.

**Marcus Derencius:** It's easy to get the correct information because some content I'm going to generate, but other must be correct as the original source.

**Marcus Derencius:** So I was checking every API.

**Marcus Derencius:** So yeah, I can do that. I can start with that. But this doesn't have a lot of information on the NVD website, so it seems very limited. So probably I would try to find a big one that has all the details so I can see how we populate that in the template. Once we have the process of getting the data, processing, and publishing them, if you need to update it, you just have to rerun our workflow and update the data.

**Aida Knežević:** Okay, so is the updating, I mean the rerunning, that's something that we would have to do on our end, right?

**Marcus Derencius:** Yes.

**Aida Knežević:** Okay, so that answers the question for you, Andy, so it would have to be triggered by us.

**Aida Knežević:** Okay.

**Marcus Derencius:** Yeah, can, if the data is reorganized, we can try to trigger a refresh, we can have a daily process that goes through the API and see if there's any change.

**Marcus Derencius:** We just have to define, oh, this is the most reliable source of information in Sydney, so just have, like, the most reliable source.

**Marcus Derencius:** for you

**Marcus Derencius:** For those details, then we can automate some of this question.

**Marcus Derencius:** Okay.

**Marcus Derencius:** I think we could probably do some automation.

**Aida Knežević:** I don't know what kind of cadence would be best, but one that maybe triggers, I don't know, is like, is once a month, is that enough?

**Aida Knežević:** Like, maybe just to do, I mean, from a CVE standpoint, I guess once the CVE is published, they release updates and patches, but at one point, the CVE is kind of like a done deal, I guess.

**Aida Knežević:** So, not sure if we would need to update it, like, consistently.

**Andy Drukarev:** Yeah.

**Andy Drukarev:** Yeah.

**Andy Drukarev:** Ideally, there is some sort of trigger where, you know, something changes, then on, like, it's almost like if there's an update to the NVD page or our sources, then it kind of triggers a corresponding update for us.

**Andy Drukarev:** But I don't know how possible that is.

**Marcus Derencius:** Yeah.

**Marcus Derencius:** Like, just confirm the most reliable source that I can check if they have, like, APIs that will get, like, a notification when something is changed that we just, we, we like, three sites right now as source, so you just have to query, maybe you have a CVE, then later you've got an entry on Xbox DB, so I don't, you just have, like, partial updates, so maybe you have to keep it.

**Marcus Derencius:** We're watching the three websites to see if there are new updates.

**Aida Knežević:** Okay, that makes sense.

**Aida Knežević:** So, I guess the next question for me is, Marcus, like, with your schedule, when do you think we could, like, have the first CVE ready?

**Aida Knežević:** Yeah, okay.

**Marcus Derencius:** I just need some time.

**Marcus Derencius:** I, I, will be working on today to, to, to, to have our

**Marcus Derencius:** Oh, details on the templates, if I can get out the details, it can be fast, maybe I need today to have a mother-sized date, that should go through.

**Aida Knežević:** Okay, okay, that makes sense.

**Aida Knežević:** I'm trying to think, I don't think I have any other questions.

**Aida Knežević:** Okay, Andy, is there anything else that you might need from us?

**Aida Knežević:** I know you mentioned a security SME that's on your team, so.

**Andy Drukarev:** Yeah, I mean, I think that once we get to having kind of a built version, you know, I'll definitely loop in some of my colleagues, but I think the information is pretty straightforward.

**Andy Drukarev:** Obviously, we'll need to talk about design at some point as well, but I think we've got to figure out how the data will flow first, and then we can have a conversation about design and publishing—like, how we're going to handle image files or GitHub integration. I have a call with some of my engineers tomorrow to talk through things like this. So I should have a clearer sense after that conversation.

**Aida Knežević:** Anything else, Jakub? Did you want to cover anything?

**Jakub Rudnik:** I mean, this is obviously the number one priority. And I think it's more of just keeping top of mind, but making sure we're wrapping up anything.

**Jakub Rudnik:** And looking forward to the next month—what do we need to do? What can we help execute on? What other things can we support? So don't hesitate to bring those things to us, but we should also be proactively looking at that. Aida's on top of the day-to-day with the other content things, but I want to make sure we have enough time to tie up any loose ends or projects we've started elsewhere. I know we started or at least drafted some other things on the PSEO side that probably have value down the road, so we want to make sure you can get as much as possible. Definitely that's it. However, we can support with those things so you're set up for success beyond the next month. So just keep those things in mind, and then probably collaborate more asynchronously when both sides think about what that means and what's missing or what we can add. So yeah, just don't hesitate.

**Jakub Rudnik:** I think it's the overall thought.

**Andy Drukarev:** I want to offer as much as we can over the next month.

**Jakub Rudnik:** We're still definitely partners for that time.

**Jakub Rudnik:** And yeah, I just wanted to say that. I'm putting that out there, but there's probably some things that will come out of that general sentiment.

**Andy Drukarev:** I appreciate that.

**Andy Drukarev:** Thanks, Jakub.

**Andy Drukarev:** Yeah, we'll think through on our end. I mean, obviously, the other big thing is getting the CWE series published.

**Andy Drukarev:** That's, again, going to be a major topic of conversation for tomorrow's call.

**Andy Drukarev:** Yeah, things definitely aren't straightforward right now without a CMS, so we're figuring it out as we go.

**Andy Drukarev:** But, yeah, appreciate that sentiment, and we'll definitely kind of take you up on it.

**Andy Drukarev:** Cool.

**Jakub Rudnik:** And again, that can apply—we've been doing ad hoc stuff here and there because you all have a lot on your plate. So same thing, we'll get to as many of those as we can if they come up. Yeah, I'll do my part on those, but keep it in mind.

**Andy Drukarev:** Okay, awesome.

**Aida Knežević:** Okay, perfect.

**Aida Knežević:** So, yeah, Marcus, just keep us updated.

**Aida Knežević:** I'm going to be out of office all next week, but you can coordinate with Jakub. If anything comes up, just let him know.

**Aida Knežević:** But yeah, I'm looking forward to seeing how it all works, like how it's all put together.

**Aida Knežević:** All right.

**Aida Knežević:** Thanks, guys.

**Aida Knežević:** See you next week. Thanks. Bye.
