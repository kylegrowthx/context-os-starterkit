# Fossa <> GrowthX Weekly Syncs

<metadata>
date: 2025-05-15
time: 18:01 UTC
duration: 19 minutes
organizer: aida@growthxlabs.com
participants: Aida Knežević, Andy Drukarev, Aaron Williams, Marcus Derencius
fathom_recording_id: 62912918
fathom_url: https://fathom.video/calls/300738962
share_url: https://fathom.video/share/FZJWKpZo7yaThYgFCYn7ngB2Y2xd-sp1
source: fathom
enriched_on: 2026-03-04 12:30 UTC
</metadata>

---

## Summary

GrowthX and FOSSA aligned on the CVE vulnerability pages project: GrowthX will deliver pages as markdown files for GitHub integration, with Aida selecting data sources and creating a content template by next week. FOSSA will grant GitHub branch access for staging and preview. Separately, 10 CWE blog articles are complete and awaiting final review, with Marcus to verify code snippets once Aida sends them.

---

## Context

FOSSA is a developer-focused open source software supply chain platform. This weekly sync between GrowthX's content and engineering team and FOSSA's product leadership covers two interconnected initiatives: CVE (Common Vulnerabilities and Exposures) vulnerability pages for FOSSA's website, and a series of CWE (Common Weakness Enumeration) blog articles. The CVE pages project is strategic for FOSSA's SEO and content marketing — it addresses how they surface vulnerability information programmatically while staying on-brand (dark mode). The CWE blog series (10 articles) is editorial content designed to drive organic traffic and establish thought leadership. Both projects highlight the challenge of publishing without a CMS, forcing FOSSA to manage everything through GitHub.

---

## Relevance

- **To GrowthX Delivery:** CVE pages require data source integration and template design before hand-off; Marcus is confident on technical publishing but needs clear design direction from FOSSA. 10 CWE blogs are written and ready for code review — this is billable delivery work nearing completion. Publishing timeline depends on FOSSA's CMS situation.
- **To GrowthX Business Development:** FOSSA lacks a CMS and has limited technical depth internally (Andy codes, Aaron focuses on architecture). This is expansion opportunity: GrowthX could own more of the publishing pipeline or propose a headless CMS solution. Client is engaged and moving fast (templating by next week).
- **To CheckThat:** CVE pages are inherently SEO-focused vulnerability content; CheckThat visibility in FOSSA's vulnerability database and registry could be a differentiation angle for AI visibility audits in the security/DevOps space.

---

## Overview

- **CVE pages:** GrowthX will deliver markdown files for GitHub integration; Aida to finalize data sources and create content template by next week; FOSSA to set up GitHub staging branch for preview
- **CWE blogs:** 10 articles complete and under Aida's review; Marcus to review code snippets once received; FOSSA working on publishing solution (no CMS currently)
- **Next steps:** Aida to sync with Marcus internally, then provide both teams with timeline and deliverables by early next week

---

## Key Topics

### CVE Vulnerability Pages Strategy

GrowthX and FOSSA discussed how to approach CVE pages: individual pages per vulnerability with programmatically-pulled data. Andy noted the strategic fit with FOSSA's registry work and emphasized they want near-publication-ready pages delivered. The balance is between speed and comprehensiveness—Andy wants to prioritize speed over advanced interactive elements, keeping the design on-brand (dark mode). Marcus confirmed the technical approach is straightforward: start with markdown, evolve to more advanced components if needed.

### Technical Architecture and Data Sources

FOSSA's website is a static GitHub-managed repo, mostly markdown with API flexibility but no CMS. This shapes the publishing workflow: GrowthX will deliver markdown files; FOSSA will integrate them via pull request workflow. Aaron will set up a staging branch for GrowthX to preview pages before publication. Aida identified a GitHub-accessible CVE data source via API as a starting point, with the goal of combining multiple data sources for richer pages.

### CVE Template and Design Definition

The critical next step is defining the template: what data comes from APIs, what gets written manually, what the page layout looks like. Aida will create a content mock-up and template for review. Marcus will assess the template for technical feasibility and determine the publishing process (markdown push → PR review → deploy). Andy suggested feeding FOSSA's existing registry page structure to an AI design tool (V0) to generate inspiration for CVE page layout.

### CWE Blog Series Delivery

10 CWE articles are written and complete, currently under Aida's review. Marcus will review code snippets once Aida sends them. FOSSA is working on their publishing solution for the series despite CMS constraints; they plan to get everything live soon. This represents a complete deliverable from GrowthX ready for handoff.

---

## Action Items

**Aida Knežević (GrowthX)**
- Select data sources for CVE information and create content template for CVE pages (target: next week)
- Review and finalize 10 CWE blog articles, send to Marcus for code snippet review
- Sync with Marcus internally on both projects, then provide FOSSA with timeline and next steps

**Aaron Williams (FOSSA)**
- Set up GitHub branch and staging environment for GrowthX team to preview and test CVE pages

**Marcus Derencius (GrowthX)**
- Review code snippets in 10 CWE blog articles once received from Aida
- Assess CVE page template from Aida for technical feasibility and confirm publishing process

---

## Transcript
**Aida Knežević:** Regarding the CVE vulnerability pages that we were going to set up on your site, I'm going to drop a link to the Google Doc that Jacob initially shared, and I added some extra stuff to it.

**Aida Knežević:** I just generated a quick, like, HTML code of what a CVE vulnerability page could look like, just to, like, help us kind of frame, you know, like, the initial idea, I guess.

**Aida Knežević:** But, yeah, the main idea is just to basically have individual pages for each vulnerability that would contain specific, like, information, I'm assuming based on my very, like, I don't have a technical background, but this could be pulled in from an API, but I'll let you guys take it from here and curious to see, like, what the FOSSA team needs.

**Aida Knežević:** from us and sort of vice versa.

**Aida Knežević:** Yeah, I mean, I think I can start.

**Andy Drukarev:** Like, I think we like the idea of doing, you know, a bunch of these CVE pages.

**Andy Drukarev:** It's complementary to some of what we're working on or thinking about for FOSSA registry.

**Andy Drukarev:** You know, I think the thought, the hope was that it's something where you might be able to kind of build and deliver kind of the pages that are almost fully ready for us.

**Andy Drukarev:** if that's at all possible.

**Andy Drukarev:** And so, you know, I provided kind of that list of different sources that we could integrate.

**Andy Drukarev:** And yeah, I mean, I think I think that's kind of where the discussion lies is, you know, what are you able to kind of build on your end?

**Andy Drukarev:** What's realistic?

**Andy Drukarev:** What information would you need from us?

**Andy Drukarev:** So on and so forth.

**Marcus Derencius:** Okay, so to start, what is the workflow for generating the content, and also how should we publish or send you the pages?

**Andy Drukarev:** Yeah, so we don't have a CMS today.

**Andy Drukarev:** What we have is a collection of kind of static pages that we manage through GitHub.

**Andy Drukarev:** Most of our pages are written in Markdown, but I don't think that's a hard and fast requirement.

**Andy Drukarev:** But Aaron, I guess I would kind of defer to you here, not defer, but I think you might have some additional good context on, like, technical requirements for us to be able to publish.

**Aaron Williams:** Okay, yes, I think you hit the important parts.

**Aaron Williams:** The entire site itself is hosted in a GitHub repo.

**Aaron Williams:** So that gives us a fair amount of API flexibility, but doesn't give us a lot of CMS flexibility.

**Aaron Williams:** So we would want to work with you to figure out kind of what's the best structure for these pages, maybe starting with what you think the design of the page should look like.

**Aaron Williams:** And then that can help us instruct us whether we need to go through the markup route or whether we need to go turn these into full-fledged landing pages.

**Aaron Williams:** And so I think the key for us right now is we can work with you to figure out the right technical way to get the pages out of the site.

**Aaron Williams:** But we would want to figure that out and have you deliver us kind of the pages into the repo.

**Aaron Williams:** We don't have, you know, and between Andy and I, we don't have a whole lot of technical kind of depth.

**Aaron Williams:** We'd really like to be able to kind of hand that off and have you help us build all the way from design to actually getting it into the repo.

**Aaron Williams:** Okay.

**Marcus Derencius:** Yeah, that helps.

**Marcus Derencius:** It's kind of flexible.

**Marcus Derencius:** So first we can start with just publishing markdown. We're able to supply markdown content.

**Marcus Derencius:** The only, like, something that must be defined is how we're going to present, how is the layout, the page, if you're going to require, like, a more advanced components and styling.

**Marcus Derencius:** So that's, like, and we have to define that first, if we're going to have to change the...

**Marcus Derencius:** how the publishing process is going to go.

**Andy Drukarev:** So you would essentially need a mock-up of not only the content, but what the page design and page layout looks like?

**Marcus Derencius:** Yeah, how the final product should be.

**Marcus Derencius:** So, so, because if you just, like, regenerate it.

**Marcus Derencius:** If a markdown is enough, just so we can generate a markdown file and we can try to push to the...

**Marcus Derencius:** We pull automatically, and then we just review the pull request and publish.

**Marcus Derencius:** I don't know if it's how we are deploying the website right now, but then we can find this final way of publishing the content.

**Marcus Derencius:** I was looking at the Google Docs to see if there's anything on the page that would be complex, like needing JavaScript or something more advanced. Looking quickly, I didn't see anything too complex.

**Marcus Derencius:** So, yeah, so we can start, let's start imagining just, we're going to provide you a markdown.

**Marcus Derencius:** We can put it on the website and then as soon as we get more clear the idea of design, if it's going to be more advanced, then we can use it.

**Marcus Derencius:** I think that makes sense, too.

**Aaron Williams:** Did you have a wish list of interactive elements, or were you thinking that we could get away with kind of flat text, or like, you know, mostly text?

**Andy Drukarev:** Yeah, I mean, I think, you know, there's always the balance between speed and quality.

**Andy Drukarev:** I, for these, lean towards speed.

**Andy Drukarev:** And so, you know, I think it needs to be on brand for the rest of our site, obviously, which is basically dark mode.

**Andy Drukarev:** Like, that's our brand right now.

**Andy Drukarev:** But aside from that, you know, the harder part right now is making sure that we are able to kind of appropriately synthesize all of the different CVE information from all the different sources.

**Andy Drukarev:** And so, you know, it's really two things that need to be tackled, right?

**Andy Drukarev:** It's page layout design, and then...

**Andy Drukarev:** It's how do we programmatically take all these different CVE data sources and combine them into a really good page.

**Andy Drukarev:** So I think those are the two things that we need to tackle.

**Marcus Derencius:** Okay.

**Marcus Derencius:** Yeah.

**Marcus Derencius:** So, yeah, we have how we generate the content and the publishing, so, and the design.

**Marcus Derencius:** So those, like, three buckets of things to define something.

**Marcus Derencius:** But, yeah, I think that just to generate page, it's kind of straight, it is straightforward, so, like, you have a easy way to publish a new page, then we have the content, so then I...

**Marcus Derencius:** So, yeah, I think, so, like, publishing the pages is simple, it's easy, it looks really good.

**Marcus Derencius:** So it's just more like defining the content.

**Aida Knežević:** Yeah, I found a GitHub doc that is accessible, I think, via an API that allows us to pull like information about different CVEs.

**Aida Knežević:** And I think we could use that for these pages.

**Aida Knežević:** Now, how, I mean, I'm not sure how we would integrate that into the pages.

**Aida Knežević:** That's for the engineering team.

**Aida Knežević:** But I did find this as a resource and I added it to the doc.

**Aaron Williams:** How do you usually work?

**Andy Drukarev:** I mean, I guess, Aida, what are your initial thoughts on like how we kind of start to tackle these two challenges, right?

**Andy Drukarev:** The layout and the design and then the actual, you know, data sources and content generation.

**Andy Drukarev:** So.

**Aida Knežević:** From a design standpoint, how have you been designing things? For example, how did you design the registry?

**Aida Knežević:** That's sort of because if you already have a way that you like things to look like, is there a design team involved or do you have like a template for a page that we could kind of use, but maybe tweak a little bit?

**Andy Drukarev:** No, probably not. The CEO and I have coded everything. So I think the recommendation would be to feed the registry page structure to V0, tell it to create something similar, and then export the code.

**Aida Knežević:** Marcus, FOSSA has registry pages on their website. I'll send them to you so you can take a look—not as a template, but just as inspiration.

**Aida Knežević:** From a content generation standpoint, I just need to know what data is going to be pulled via an API about a specific CVE, and what data is not going to be pulled, what data we have to generate.

**Aida Knežević:** So we just need to decide what is the data source that we're going to use for these pages.

**Aida Knežević:** I have the GitHub link here, but this is something that I think Marcus can take a look at and then let me know what is probably the best data source we can use for these pages, and what types of information are going to be pulled in programmatically.

**Aida Knežević:** Once I know that, I can give suggestions for additional like H2.

**Aida Knežević:** These H3s we can add to each page.

**Aida Knežević:** And that is relatively, like, it's a straightforward process for me.

**Aida Knežević:** It's not super complex.

**Aida Knežević:** So I think the biggest thing is just, like, understanding, like, deciding which data source we're going to integrate with and how we're going to do that and where that plugs into our internal workflows in Aeroops, which is something that we have to figure out internally.

**Andy Drukarev:** Talking to Jacob about this originally, think his thought, which was exciting to us, was that you have, like, kind of individual data sources for CVE pages, but the ability to potentially kind of combine the best of, you multiple data sources into a more comprehensive page.

**Andy Drukarev:** And so I think that, directionally, is very interesting to us.

**Andy Drukarev:** Okay.

**Andy Drukarev:** But, you know, I guess the question is just, like, what the next step looks like there.

**Aida Knežević:** Marcus, so from your side, what do you think could be the next step or is there any other information that you need from me or from FOSSA to put this together?

**Marcus Derencius:** Publishing the page is simple—there's nothing more I need on technical details. I just need to see a template. On the content side, you need to define the data sources and how you'll generate each page.

**Aida Knežević:** Okay, so you want us to pick basically the data sources, and then you're going to basically just like pull the data, right?

**Marcus Derencius:** Yeah, and how, what should be a page, what's the content of the one page, and then we make the workflows for that.

**Aida Knežević:** Mm-hmm, okay, okay, that makes sense, okay, I understand.

**Aida Knežević:** So, I guess to you it doesn't seem like an overly complex project?

**Marcus Derencius:** It's not overly complex, but the content is important—each CVE has an ID and technical details. You need to make sure the content is valid and correct.

**Aida Knežević:** Yeah, yeah, exactly, yeah.

**Aida Knežević:** Yeah, that's my job, okay.

**Aida Knežević:** Right, so I think we just need to decide on the data sources and put together a template—a content mock-up of what these CVEs should look like. What's the best way to preview this, though?

**Aida Knežević:** If I put something together next week for one CVE, how can we preview it to show it to the FOSSA team?

**Marcus Derencius:** If we get access to the GitHub repo, we can create a staging environment. I'd suggest creating a branch where we can test things out.

**Aaron Williams:** Andy, don't see any issues with that, you?

**Aaron Williams:** Okay, let's make that happen. That way we can see it in full context and not have it as a separate thing.

**Aida Knežević:** Okay, do you guys have, like, any other questions or concerns?

**Aida Knežević:** Like, right now I'm pretty clear on what I have to do.

**Aida Knežević:** I don't think you guys have to do anything, so now it's, like, up to me to, like, just decide on the data sources and put together, like, the template, but do you have any other questions or, like, concerns?

**Andy Drukarev:** No, no.

**Andy Drukarev:** Okay, okay, great to hear.

**Aida Knežević:** I am excited because it's been a long time coming to, like, put something together, so I'm excited to get started with this.

**Aida Knežević:** I'll put something together tomorrow and share it with Marcus as soon as possible. My goal is to have this ready next week. Marcus, what's your schedule looking like these days?

**Marcus Derencius:** Yeah, I'm flexible. We can definitely work something out.

**Aida Knežević:** Yeah, they updated our AirOps grid today, and their notifications are blowing up on Slack.

**Aida Knežević:** So the engineering team is pretty busy today, but we can definitely work something out next week.

**Aida Knežević:** On the editorial content front, the 10 CWE blogs are done, but I'm reviewing them today and tomorrow. Those should be ready for you soon.

**Andy Drukarev:** Will you be able to get an engineer to look over the code again?

**Aida Knežević:** Yeah, absolutely. Marcus, can you review the code snippets once I send them?

**Marcus Derencius:** Yeah, no problem.

**Andy Drukarev:** On our end, it's been a real challenge to actually build the series the way we want to without a CMS. We're working on it, and our hope is to get everything up sooner than later.

**Aida Knežević:** I'm happy we're going to finish out the series. From our end, those are the two priorities: the CWE editorial series and the CVE SEO initiative.

**Andy Drukarev:** Exactly. Those are my two priorities.

**Aida Knežević:** I think we're all aligned. You're all basically waiting for me to give you next steps. I'll sync with Marcus internally and then get back to you tomorrow or early next week.

**Andy Drukarev:** Perfect.

**Aida Knežević:** Thanks, guys. Have a great rest of your day. If you have any questions, let me know in Slack.

**Andy Drukarev:** Will do. Thanks, Aida.

**Aaron Williams:** Thank you.
