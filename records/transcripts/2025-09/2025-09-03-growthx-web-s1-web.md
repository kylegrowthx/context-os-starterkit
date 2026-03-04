# GrowthX Web <> S1 Web

<metadata>
date: 2025-09-03
time: 18:00 UTC
duration: 23 minutes
organizer: Nicolas Castellanos
participants: Nicolas Castellanos, Aida Knezevic, John Nederveld, Joery Van Druten, Ankit Pahuja
fathom_recording_id: 84752877
fathom_url: https://fathom.video/calls/398930057
share_url: https://fathom.video/share/7hzmjffBVENnr2nC_Y4-nNnXgAiDu35W
source: fathom
enriched_on: 2026-03-02 02:47 UTC
</metadata>

---

## Summary

GrowthX and SentinelOne aligned on implementing a CVE (Common Vulnerabilities and Exposures) database — index page plus detail pages — directly in SentinelOne's new ContentStack CMS. Key decisions: GrowthX will set up content types in ContentStack (as isolated entry types to avoid conflicts), handle the data pipeline integration via ContentStack's Content Management API, and provide design handoff to SentinelOne's Next.js frontend team. Access bottleneck identified: Nicolas needs a SentinelOne email and VDI access (1-2 week process), while Sydney's access is immediate. Follow-up meeting scheduled between John and Nicolas to finalize field structure and documentation.

---

## Context

SentinelOne is undertaking a major technical rebrand, rebuilding their website from WordPress to a modern tech stack using ContentStack CMS and Next.js. As part of this migration, they need to implement a CVE (Common Vulnerabilities and Exposures) database feature — an index page for browsing and searching vulnerabilities, plus individual detail pages for each CVE. GrowthX has built the data pipeline to pull CVE data from official sources and transform it into articles. SentinelOne's technical team (John, Joery, Ankit) needed to align with GrowthX (Aida and Nicolas) on how to integrate this pipeline with ContentStack's content modeling layer, secure proper API access, and clarify the division of work between GrowthX's data/backend and SentinelOne's frontend development.

---

## Relevance

- **To GrowthX Delivery:** GrowthX is responsible for ContentStack content type setup, data pipeline integration (using ContentStack's Content Management API), and ContentStack API documentation handoff. Clear decision needed on GrowthX's role in frontend UI development — currently ambiguous whether GrowthX is building templates or just providing data. Access bottleneck: Nicolas (in Uruguay) needs SentinelOne email + VDI access (1-2 weeks, high friction).

- **To GrowthX Business Development:** Client is in midst of major technical transformation (WordPress → ContentStack, PHP → Next.js, brand refresh). SentinelOne team shows good collaboration signals (willingness to align on field structure, proactive design sharing via George Main). Early-stage project (started July 2025) suggests potential for additional content/SEO work during migration. Keep eye on whether CVE database becomes reference-able win for similar enterprise clients.

---

## Overview

- GrowthX to build CVE index page + individual CVE pages on SentinelOne's new ContentStack CMS
- SentinelOne team still in content modeling phase; alignment needed on field structure
- Access to ContentStack requires SentinelOne email + Okta authentication; process initiated for Nicolas
- Frontend will be built by SentinelOne team using Next.js, integrating with existing components

---

## Key Topics

### Project Overview & Scope

  - GrowthX building CVE index page (main browsing/search page) + individual CVE detail pages
  - Pages to be built directly in new ContentStack CMS, not WordPress
  - GrowthX responsible for setting up content types in ContentStack
  - Uncertainty about GrowthX's involvement in UI development; needs clarification

### Content Structure & Integration

  - Main content mostly free text (markdown)
  - Some structured fields needed for categorization on index page
  - John (S1) to ensure no duplicate fields in backend
  - CVE pages to be set up as isolated entry type to avoid conflicts
  - Search functionality to be integrated with Algolia

### Data Pipeline & API

  - GrowthX pulls data from official CVE sources, transforms into articles
  - Pipeline runs on GrowthX's internal tool
  - Nicolas to receive ContentStack read token to study API structure
  - Plan to use Content Management API for pushing data

### Access & Security

  - Sydney (GrowthX) has SentinelOne email, needs ContentStack access via Okta
  - Nicolas (Uruguay) needs SentinelOne email; process initiated (1-2 weeks)
  - VDI access required, expected to be slow

### Design & Frontend

  - Current design is early mock-up, being reviewed by SentinelOne team
  - George Main (designer) to share Figma file with SentinelOne team
  - SentinelOne building frontend with Next.js TypeScript
  - Will reuse existing components (e.g., breadcrumbs) where possible

---

## Action Items

**John Nederveld (SentinelOne)**
- Schedule follow-up meeting w/ Nicolas to align on ContentStack field setup and content organization
- File IT ticket for Sydney's ContentStack access

**Aida Knezevic (GrowthX)**
- Follow up w/ Sydney re VDI & Okta access confirmation, guide through login process

**Joery Van Druten (SentinelOne)**
- Initiate process for Nicolas Castellanos to get SentinelOne email (fill out form)

---

## Transcript

**Nicolas Castellanos:** Do it all right, thanks.

**Ankit Pahuja:** Hey, everyone.

**Joery Van Druten:** Wow. Oh, 11:30 p.m. I didn't expect you, man.

**Ankit Pahuja:** Yeah. Hey, Aida.

**Aida Knezevic:** Thank you so much for coming on the call, especially you, Ankit. I know it's very late for you. Nice to meet you, Joery.

**Joery Van Druten:** Nice to meet you.

**Aida Knezevic:** Perfect.

**Aida Knezevic:** So, yeah, I think I shared with Nicolas a little bit about what we're doing here. He has already built the pipeline to generate the CVE pages. So, today is just to help Nicolas understand how he can set up and launch these pages in ContentStack, and also on SentinelOne's side, what the team needs to do to give Nicolas the right access so we can set everything up.

**Joery Van Druten:** Well, I actually want to take a step back, because John and I don't know too much about this at the highest level. We know GrowthX is going to create a CVE database project and develop it, but that's about it. Let me give you a little background on our ContentStack situation. The project we're working on is a website refresh in combination with a brand refresh. We're basically building the site from scratch — from WordPress to ContentStack, and from PHP to Next.js. It's a whole new tech stack. There's absolutely no lift and shift of anything. We just started in July, so we're at the beginning of the project but making great progress. The foundation is set so we can start production, but we're still in the middle of content modeling. So when we heard you need access to ContentStack, we wanted to understand: what are you actually going to do in ContentStack? What are your expectations? Because we're still in the content modeling phase. John can give more of an update on the status there. Are we saying you know the data points, and it's more about how to integrate that data pipeline into ContentStack? We want to get a bit of an understanding of the scope of work.

**Aida Knezevic:** Okay. So I think it would be helpful to show you what the project looks like. We do want to build a CVE index page on your website — that's the hero, the main page where people can browse different CVEs, which would be categorized. They could search for different CVEs, and once they click, they'd be taken to a detail page that looks like this. The design is going to change — this is just a very early mock-up, but it will look something like this. It's very structured. There are specific sections that are going to appear on every page: overview, vulnerability analysis, how to mitigate, things like that. It's very programmatic — we build a template and then push the content. Nicolas, correct me if I'm wrong, but is it via an API to the website?

**Nicolas Castellanos:** Yeah, that's correct.

**Aida Knezevic:** So this is what we typically do. I understand you're migrating to a new CMS, which is a complicating factor, but it's not happening in the next month or two, so that gives us enough time to launch these pages on your site and migrate them with the rest of the site to your new CMS.

**Joery Van Druten:** No, no, we're going to build this in the new CMS. ContentStack is the new CMS. We absolutely don't want to have redundant work — we don't want to build it in WordPress and then move it over.

**Aida Knezevic:** Got it, got it. Yeah, okay.

**Joery Van Druten:** But that's the thing, right? We need direction on how to build it, because we're still in the content modeling phase. It's not that we can't do it, but there's absolutely some direction needed from John. For instance, if you have a hero here, we will have a hero module, right? We have breadcrumbs. We will have breadcrumbs. So we don't want to have all these redundant fields. That's where the alignment needs to happen. John, what are your thoughts?

**John Nederveld:** So first off, when you say you're going to be setting these up on our site, are you just going to be hitting our ContentStack API to create the pages? Or are you planning to actually enter ContentStack and set up the entry types? Do you have experience with ContentStack? And then also, who's doing the front-end work? Is the extent of GrowthX's involvement just adding the data into ContentStack via the API, and then all the front-end stuff is on our end?

**Nicolas Castellanos:** As for the data structure, my thinking was, yes — go into ContentStack and set up all the content types and everything to be able to hit the API and create all the stuff we need. As for the UI, Aida, I don't know — are we going to write all the UI for this?

**Aida Knezevic:** I'm not sure. I would have to check.

**Nicolas Castellanos:** Okay.

**Joery Van Druten:** Let's go back to the content types. John, what are your thoughts?

**John Nederveld:** Like you said, I want to make sure we don't have any duplicates in our field setup. It would be good to have an outline of what fields you need in ContentStack. If this content on the left is just one big rich text editor, that's one thing. But if we need to break up each section into their respective fields or groups, we can do that as well. And then the stuff on the sidebar and hero — just making sure we don't have too many duplicate fields in our backend.

**Nicolas Castellanos:** Yeah, most of that main content is just free text, like markdown. And then we need some structured fields for the index page to show categorized stuff.

**John Nederveld:** Okay, yeah, that makes sense to me. If we set this up as an entry type — since it's isolated — we can do it without any global fields. All of the fields will be specific to this entry type, so they're isolated and won't bleed into anything else we're working on. I think that would be the way to go for sure.

**Joery Van Druten:** And the search — how is that? Is that going to be integrated with Algolia search?

**John Nederveld:** Yeah, we'll have to set up an index in Algolia with this entry type, which we can do already. The individual article pages will be an entry type. The listing page doesn't necessarily need to be an entry type — we can create that in the codebase. The individual pages are where we'll need to actually store all of the fields of data.

**Joery Van Druten:** How far is this design?

**Aida Knezevic:** The design is still being reviewed by the SentinelOne team. This is just an early mock-up, so we do have to update it with some of the new branding elements. Can you share this with us?

**Aida Knezevic:** Yes. I'll add your emails just really quickly.

**Joery Van Druten:** Okay, so can you talk a little bit more about the pipeline? You have something where the data pipeline pulls data from somewhere and pushes it into ContentStack?

**Nicolas Castellanos:** Yeah, we get data from three official CVE sources, transform that into CVE articles, and then push that into ContentStack. That's the plan.

**John Nederveld:** Where is that going to run? Where will the pipeline code live and operate?

**Nicolas Castellanos:** That runs on our internal tool.

**John Nederveld:** Okay. Can you send me an example of a response — just the JSON that it sends back?

**Nicolas Castellanos:** Yeah. My plan was to get into how ContentStack works and write JSON that complies with that API. I saw it has a bunch of APIs. I think the one we need to use is the Content Management API.

**John Nederveld:** Yeah. I can give you a read token for now if that's all right. You can see how it looks.

**Nicolas Castellanos:** Yeah.

**John Nederveld:** That's perfect.

**John Nederveld:** Okay.

**Joery Van Druten:** So to get access to, to get access to content stack, you need.

**Joery Van Druten:** Okay.

**Joery Van Druten:** Okay.

**John Nederveld:** Okta.

**Nicolas Castellanos:** Ok.

**Joery Van Druten:** And we were, we did proficient one person.

**Joery Van Druten:** Is that you, Aida?

**Joery Van Druten:** Who did we get a SentinelOne email?

**Aida Knezevic:** I'm not, I didn't receive a SentinelOne email.

**Aida Knezevic:** So there are, there's Sydney, Marisol, Nicolas, and Sulemon.

**Aida Knezevic:** Those are the four people that, um, I sent over.

**Joery Van Druten:** Uh, I think only Sydney got, cause I only got two names.

**Aida Knezevic:** Ok.

**Joery Van Druten:** Ok.

**Joery Van Druten:** I think only Sydney has access.

**Aida Knezevic:** Ok.

**Joery Van Druten:** So, Nicolas, where are you, where are you located, Nicolas?

**Nicolas Castellanos:** In Uruguay, South America, next door, Argentina.

**Joery Van Druten:** Let me quickly see if that's gonna be an issue.

**Nicolas Castellanos:** I can, I can.

**Nicolas Castellanos:** Use our VPN also, if that's a problem.

**Joery Van Druten:** Oh, no.

**Joery Van Druten:** That is a problem.

**Joery Van Druten:** I don't make the rules.

**Joery Van Druten:** Trust me, Ankit and I are always like, really?

**Joery Van Druten:** More red tape?

**Joery Van Druten:** Uruguay.

**Joery Van Druten:** Oh, yeah, it's on the list.

**Joery Van Druten:** Okay.

**Joery Van Druten:** I will Slack, because I probably need some information from you.

**Joery Van Druten:** Basically, your address.

**Joery Van Druten:** I can then get you a SentinelOne email, and that's going to take forever again.

**Joery Van Druten:** So maybe in the meanwhile, what we can do is at least get Sydney proficient, John, because Sydney already has an email address.

**Joery Van Druten:** And then, I don't know if you use, like, something like 1Password or something.

**Joery Van Druten:** mean, you, because it takes, it takes one to two weeks before IT is going to set you up.

**Joery Van Druten:** Okay.

**Joery Van Druten:** Uh, let's see if that's because, okay, because Sydney should have been contacted, that's here, because you need to dial in with VDI, then you have to go through Octa, and that's the whole thing.

**Joery Van Druten:** It's not going to be ideal, it's going to be super slow, I'm going to warn you.

**Aida Knezevic:** Okay.

**Joery Van Druten:** That is totally out of Ankit in my control, that is not.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Okay, okay, I'll let her know that she should have access.

**Joery Van Druten:** So, she should have gotten an email notification?

**Joery Van Druten:** Yeah, from IT, like, a couple of weeks ago.

**Aida Knezevic:** Okay.

**Aida Knezevic:** All right.

**Aida Knezevic:** Well, I'll double check with her.

**Aida Knezevic:** Make sure that nothing ended up in spam.

**Joery Van Druten:** Because she is in Mexico, is that correct?

**Aida Knezevic:** No, that's Marisol.

**Joery Van Druten:** Marisol is in Chile, but Sydney is in Vancouver, Canada.

**Joery Van Druten:** Okay, then she should be fine.

**Aida Knezevic:** Yeah.

**Joery Van Druten:** Okay.

**Joery Van Druten:** We could not get Chile.

**Joery Van Druten:** That was...

**Joery Van Druten:** And again, out of Ankit in my control, it is just, but I saw that Uruguay was on the list, so that should not be a problem.

**Joery Van Druten:** So I can kick that off today.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Perfect.

**Aida Knezevic:** I don't have permissions to share the Figma file with you, but I DMed George Main, who is the designer and owns the file. He's going to share the designs with you so you can take a closer look.

**Joery Van Druten:** Cool. John, you should have a follow-up meeting with Nicolas to align on things and document the decisions made.

**John Nederveld:** Nicolas, I'm going to direct message you the docs for setting up ContentStack. They have a Postman collection with all of their routes, and I'll send you the read key so you can look at some responses from ContentStack and see how they format their JSON.

**Nicolas Castellanos:** Cool, thanks. So the other thing I need to understand is how we're building the frontend. I heard you guys are building the frontend, and you'll reuse some of the stuff you already have?

**John Nederveld:** We'll reuse what we can. We'll have some components like breadcrumbs already set up. We're rebuilding the site with Next.js TypeScript, so we'll be able to lift some of those components and reuse them. But a lot of it will be specific to this entry type.

**Nicolas Castellanos:** So this will be integrated inside your Next.js project?

**John Nederveld:** Yeah, yeah.

**Aida Knezevic:** By the way, Joery — Sydney just confirmed that she did get an email. Should she have also received instructions to access the CMS?

**Joery Van Druten:** No, that's separate. She should have got access to use VDI and then be able to access our Okta. Then John can request her to be added to ContentStack, and the ContentStack tile will show up on our Okta dashboard. As long as she can test that she has access to the Okta dashboard and can log in through Okta, she should be good. Then we can start the process for content access.

**Aida Knezevic:** Okay, got it. I'll follow up with her.

**Joery Van Druten:** Nicolas, just confirming — it's nicolas.castellanos@growthx.ai, right?

**Nicolas Castellanos:** It's Castellanos with double L.

**Joery Van Druten:** Okay. I'm going to fill this out right now and kick that off. And John, I'll give you Sydney's email so you can file an IT ticket to get her ContentStack access.

**John Nederveld:** Okay.

**Ankit Pahuja:** I was able to share Figma access with both Joery and John, so you should have the link.

**Aida Knezevic:** Cool. Thank you.

**Joery Van Druten:** Do you have any more questions, John?

**John Nederveld:** I think we're good for now. We'll continue collaborating on getting the field setup and ContentStack organized, and then do some tests and set up some posts with the API.

**Joery Van Druten:** Once things go live and something needs to be changed on the frontend, will that move over to you, Ankit?

**Ankit Pahuja:** In terms of content or design?

**Joery Van Druten:** UI and UX.

**Ankit Pahuja:** I'm not sure.

**Joery Van Druten:** Okay. Well, we'll get this going. Hopefully with Sydney's account, you'll get access, and we'll get Nicolas' account as soon as possible.

**Aida Knezevic:** Perfect. Thank you. Feel free to reach out over Slack if you have any questions in the meantime.

**Joery Van Druten:** Yeah, no problem. All right. Thank you.

**Aida Knezevic:** Bye.
