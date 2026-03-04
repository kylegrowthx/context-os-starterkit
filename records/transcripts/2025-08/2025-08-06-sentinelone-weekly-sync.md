# SentinelOne Weekly Sync

<metadata>
date: 2025-08-06
time: 14:02 UTC
duration: 31 minutes
organizer: Sydney Go (GrowthX)
participants: Sydney Go (GrowthX), Ankit Pahuja (SentinelOne), Mahati Rapol (SentinelOne)
fathom_recording_id: 78816095
fathom_url: https://fathom.video/calls/371935684
share_url: https://fathom.video/share/sZSWeshRAxVuQqQsJashJyxBuCzFm4_s
source: fathom
enriched_on: 2026-03-03 18:15 UTC
</metadata>

---

## Summary

GrowthX and SentinelOne finalized the CVE database template, deciding to add EPSS exploitability scores and defer SentinelOne-specific sections to Phase 2 pending security researcher review. Sydney will deliver Figma mockups and sample pages by end of week. The team approved three AI cybersecurity content lanes (behavioral AI/autonomous security, AI threat landscape, and foundational knowledge) and agreed to start with Google Docs collaboration before moving to SentinelOne's ContentStack CMS. LLM citation tracking via Scrunch shows SentinelOne has strong presence against competitors like CrowdStrike and Palo Alto, with listicles and foundational pieces generating the most citations.

---

## Context

SentinelOne is a cybersecurity platform client engaged with GrowthX on a major content initiative across three fronts: a proprietary CVE database, AI cybersecurity thought leadership, and LLM visibility tracking. This is an ongoing program with strategic importance to both SentinelOne's PMM team (led by Mahati Rapol) and GrowthX's content delivery (led by Sydney Go), with Ankit Pahuja driving technical requirements from the SentinelOne side. The team is in Week 1 of execution on the CVE database build and content ideation phases. SentinelOne is also managing concurrent priorities including Black Hat attendance and a recent acquisition, which is impacting team bandwidth through mid-to-late August.

---

## Relevance

**To GrowthX Delivery:**
- CVE database requires Figma design template and engineering coordination with SentinelOne's development team to build the page framework — Sydney to deliver by end of week
- Content workflow confirmed: start with Google Docs for calibration (2-3 articles), then establish CMS integration once SentinelOne's ContentStack setup is finalized (target: early September)
- SEO meta generation (titles, descriptions, keyword placement) now required for all CVE pages at publish time
- External reference links should use no-index tags to preserve SEO value

**To CheckThat:**
- Scrunch dashboard demonstrates strong LLM citation tracking across Perplexity, ChatGPT, and Grok — listicles and foundational knowledge pieces are high-citation formats
- Competitor analysis shows CrowdStrike and Palo Alto Networks dominating LLM citations; opportunity to analyze their content strategies and differentiate SentinelOne's approach
- AI cybersecurity content lanes (behavioral AI, threat landscape, foundational knowledge) are validated LLM optimization targets

**To GrowthX Business Development:**
- Account health: SentinelOne PMM team bandwidth constrained through mid-August (Black Hat, acquisition), but leadership buy-in is strong
- Expansion opportunity: CVE database Phase 2 (security researcher validation) and CMS workflow could extend engagement scope
- Reference potential: successful AI cybersecurity content and LLM visibility wins are compelling case studies for similar B2B security clients

---

## Overview

- CVE database design finalized: EPSS exploitability scores to be added to vulnerability details; SentinelOne-specific sections ("how it helps" / capabilities) deferred to Phase 2; external references kept with no-index links; searchability tags (vendor, vulnerability type, platform) approved
- Figma template with sample CVE pages to be delivered by end of week for SentinelOne leadership presentation
- Three AI cybersecurity content lanes approved (behavioral AI/autonomous security, AI threat landscape, foundational AI cybersecurity knowledge); ideas added to Content OS for team approval via Google Docs
- ContentStack CMS integration timeline to be clarified next week (currently in setup phase); initial articles to be collaborated on in Google Docs before CMS workflow established
- Scrunch LLM citation dashboard shows SentinelOne strong presence across Perplexity, ChatGPT, Grok; CrowdStrike and Palo Alto are top competitors; listicles and foundational knowledge pieces are high-citation content types

---

## Key Topics

### CVE Database Development

  - EPSS (Exploit Prediction Scoring System) scores to be added to vulnerability details
  - SentinelOne-specific sections (capabilities, how it helps) removed from initial phase due to potential inaccuracies
  - Tags for searchability (vendor, vulnerability type, platform) approved
  - External references to be kept with no-index links
  - Figma template to be created for design review and leadership presentation

### AI Cybersecurity Content Strategy

  - Three content lanes identified: behavioral AI/autonomous security, AI threat landscape, foundational AI cybersecurity knowledge
  - Content ideas added to Content OS for SentinelOne team approval
  - Initial articles to be shared via Google Docs for collaboration before establishing CMS workflow
  - ContentStack (not Contentful) implementation timeline to be clarified next week

### LLM Citation Tracking (Scrunch)

  - SentinelOne showing good presence across tracked LLMs (Perplexity, ChatGPT, Grok)
  - Key competitors in LLM citations: CrowdStrike and Palo Alto Networks
  - Listicles and foundational knowledge pieces getting high citations
  - Scrunch prompts to be reviewed and potentially expanded by SentinelOne team

---

## Action Items

**Sydney Go (GrowthX)**
- Finalize CVE database proposal and create Figma template with sample pages. Send to Mahati for leadership presentation by end of week.
- Generate 2-3 calibration articles for AI cybersecurity content lanes and send to SentinelOne team via Google Docs for feedback before establishing CMS workflow.
- Send complete list of current Scrunch LLM citation tracking prompts to Ankit for review and priority suggestions.

**Ankit Pahuja (SentinelOne)**
- Review Scrunch prompts list and suggest additions/removals. Identify priority topic areas for LLM citation tracking.

**Mahati Rapol (SentinelOne)**
- Review Figma CVE template and sample pages to present to leadership team and security team for buy-in.
- Provide ContentStack CMS setup timeline clarity by Monday or Tuesday (target: early September).

---

## Transcript

**Sydney Go:** So if there's any other data feeds you want to add to this, we can definitely do that. I did try my hand at generating one of the sample CVE pages. This is kind of what it'll look like. And then there's a little bit of information up front, like a little table for a review of what it is. And then this one I think is a part of the template: the critical impact on users, affected products, discovery timeline, and vulnerability analysis. So I think this one will get changed based on what threat actually is. So these are all still in code, but then they'll change based on what data we pull. And then the impact assessment with technical references. And then the part that I would need you to review is how SentinelOne helps, just to make sure that we are representing SentinelOne correctly, or we can remove that part if it's going to get too complicated.

**Ankit Pahuja:** Yeah, there's feedback I had about the section where we talk about SentinelOne capabilities for a specific CVE.

**Mahati Rapol:** Hello, I'm here now.

**Sydney Go:** We were just talking about the CVE page template. Let's start from the top. You wanted to talk about the data sources?

**Ankit Pahuja:** Yep. So overall feedback: we did look at this template and some others from yesterday and we have some analysis. Sydney, we have found there's an exploitability gap with EPSS scores. We've seen search volumes and demand around people searching for EPSS scores, specifically for CVEs. CVSS is one thing, but EPSS is more around exploitability.

**Mahati Rapol:** I just want to be sure who's determining these scores. Is EPSS a standard like CVSS?

**Ankit Pahuja:** Let me dig deeper on who is generating these scores.

**Mahati Rapol:** That's the question. I think we need to make sure we're getting it from a credible source.

**Ankit Pahuja:** Yeah, so there are government agencies that have introduced EPSS and it's been used widely.

**Mahati Rapol:** Okay, can we write that down? We definitely need this to be verified by our team internally to make sure it's credible.

**Sydney Go:** So you would like that to go into the vulnerability details section, is that correct?

**Ankit Pahuja:** I'm not sure if this comes from NVD, the National Vulnerability Database. I think this would come from ExploitDB as a data source you already have, because it's more around exploitability score.

**Sydney Go:** All right, and then for the title and ID in the vulnerability details, is there anything we want to add or remove?

**Ankit Pahuja:** I think that looks good. Do you think we should add a CVE ID here, or is it already in multiple places on the page?

**Sydney Go:** We could remove it from here. If it'll be more visible in the table, we can move it from the subtitle to the table. If there'll be a big header with lots of text, then it'll be more visible in the table. Otherwise, you can leave it in the headline.

**Ankit Pahuja:** Yeah, I'm fine either way, because the H1 will include CVE ID. So it would be a bit repetitive.

**Sydney Go:** And in the overview, how do you feel about the critical impact?

**Ankit Pahuja:** Everything else looked fine, honestly. What I had apprehensions about were the SentinelOne sections. For each CVE, adding SentinelOne sections on how it helps and its capabilities is very difficult to do at the scale we want to build, and we could generate a lot of failures. Mahati, what do you think about having SentinelOne sections for each CVE?

**Mahati Rapol:** I would not put this because it is AI-generated and could be wrong. At scale, this is a bad idea. We would not include this without a security researcher reviewing it. I would put this as a Phase 2, not Phase 1.

**Mahati Rapol:** By Phase 2, we'll probably have a partner in security labs or research team that could help validate these. Then we can think about it at that point.

**Sydney Go:** Okay, understood.

**Mahati Rapol:** Is this specifically for us or for some other third party?

**Sydney Go:** It would look like assets from our own resources.

**Mahati Rapol:** So SentinelOne resources and the threat?

**Sydney Go:** This one specifically is from FXA, if I'm not mistaken. It would be the threats, whoever is affected by the threat, plus SentinelOne.

**Mahati Rapol:** If we are creating backlinks to another website, I think we need to think about this. I would be okay if it's just SentinelOne resources that touch on the topic relevant to the CVE database. I'm being cautious on the Phase 1 approach. Based on that, we can make a call later. But why do we want to create backlinks to other vendors?

**Sydney Go:** Yeah, that makes sense.

**Ankit Pahuja:** We have links to external references to the databases. That's good and okay. And we can also keep those as no-index links. Any external can be no-index.

**Sydney Go:** So you said everything else looked okay. The reason I added tags is to help with searchability through the database. Do you want that functionality?

**Mahati Rapol:** Vendor tags, vulnerability type tags, platform tags—yes, I would say yes for anything that helps searchability. References, yes. External references, yes, because this is not SentinelOne-generated, it's reference content and we want to give them credit for it.

**Sydney Go:** Okay, awesome. I will finalize these and do one last pass, then start generating content this week.

**Mahati Rapol:** Sure. Go ahead.

**Ankit Pahuja:** What does the next step look like? Would we work on a design template once we know the parameters, and then start generating content or storing it somewhere?

**Sydney Go:** We'll start generating content while I coordinate with engineering to build the page out for you. We would need access to your CMS if you want us to build the page, or I could ask engineering to work with your engineers to get this running faster. It depends on how involved you want our engineering team to be.

**Ankit Pahuja:** Yeah, I think design would be crucial because then a brand team will have a say on how it looks.

**Sydney Go:** So do you want us to get in touch with your design team, or will you take care of creating these pages and we just create the content?

**Ankit Pahuja:** Mahati, would you like to take that up?

**Mahati Rapol:** Can we wait for a go-ahead from our end before your design resources work on this? I want to make sure somebody from our end is reviewing the template. And there's a meeting early next week where I want to make sure leadership and security folks have an idea of what we're building. I want to get their buy-in.

**Sydney Go:** Okay, got it. Do you want us to send over a design proposal in Figma so you can present it?

**Mahati Rapol:** If you can, that would be great. So I can reference this as a requirements doc and we can look at the Figma. That'll be helpful.

**Sydney Go:** Got it. I'll get you that Figma template and a couple of sample pages by end of week so you can present it.

**Ankit Pahuja:** Just one thing: while we're creating content for the CVE pages, we might also want to generate SEO information—title, description, and keywords in the right places. That's one addition I didn't see in the templates. When published, we might not have to redo that.

**Sydney Go:** Yes, that is a good addition. Yeah, we'll do that as well. I'll send over the finalized proposal by end of week, along with the templates and everything. You can review it and tell us next week if you want approval. I'll generate some sample pages so we can start there.

**Sydney Go:** Okay, the next thing I wanted to bring up are the content lanes and ideation we did for AI cybersecurity content. Ada mentioned this to you last week—this is the strategy we're going with. We're going to make top-of-funnel content with some middle-of-funnel keywords to capture the AI cybersecurity space. These are three lanes we ideated: behavioral AI and autonomous security, AI threat landscape, and foundational AI cybersecurity knowledge. This is specifically to get attention from LLMs. Apart from actual threats, it's also targeting natural language processing concepts. We will cross-check with your cybersecurity 101 content to see if you have existing pieces. If they exist, we won't create them. We have ideas already in the Content OS that we'd like for you to approve. I've created a pending approval column, so you can mark approved or delete. You can also leave comments to tell us if ideas are priorities or if you already have content on that topic.

**Sydney Go:** I'll send this over. But we would need CMS access to stage the articles. So do you want us to create the content and stage it in your CMS, or just send over the text for you to publish?

**Mahati Rapol:** Ideally, we would want you to create the content. But to start off, let's get a couple of pieces in Google Docs so we can collaborate on direction and messaging. Once we have two or three finalized, we can set up a workflow.

**Sydney Go:** Yeah, that makes sense. You said you're moving to Contentful. Do you know the timeline?

**Mahati Rapol:** Everyone this week is at Black Hat. Most of the leadership and PMM team are there. We just had an acquisition, so there's a lot going on. Please give us a week and a half to ten days because it's been back-to-back for all of us.

**Sydney Go:** Congratulations on that.

**Mahati Rapol:** We're on ContentStack, not Contentful. We're still in the works on setting it up and configuring it. I should have a clear picture next week by Monday or Tuesday.

**Sydney Go:** Yeah, I just want to know from our end how we can set things up so we don't have to wait long for the engineering team to catch up with information when we're ready to go. But there's no rush on all of this.

**Sydney Go:** We will send you the calibration articles this week. We'd appreciate your feedback so we can get the content engine running and calibrate it to create content you like and approve of.

**Mahati Rapol:** Absolutely. We'll try our best. This is PMM work, so I want to set realistic expectations.

**Sydney Go:** No worries. Has Ada walked you through the Scrunch dashboard yet?

**Mahati Rapol:** Not yet.

**Sydney Go:** Okay, I can do a quick walkthrough. We've got six minutes. Do you want to see what the Scrunch dashboard looks like?

**Mahati Rapol:** Yes.

**Sydney Go:** So Scrunch is what we use to track LLM citations. SentinelOne is doing pretty good. You've got good presence on different LLMs we're tracking: Perplexity, ChatGPT, and Grok. The prompts we're tracking are around behavioral analysis, identity and access management, and machine learning. So I can give you the prompts we're currently tracking. This is one of the seed prompts: "What are the best AI-driven cybersecurity platforms for real-time threat detection and response?" The way this works is it pings the LLM every day and tells us SentinelOne's presence. Presence is if you're mentioned, position is where, citation is if your link appeared, and sentiment is if it's positive or negative. For example, here CrowdStrike appears as number one, SentinelOne as number four. It's volatile—sometimes you don't get cited at all, other times you're all over the response.

**Sydney Go:** We've started looking at what's actually getting cited. For here it's top 10 cybersecurity platforms and top AI cybersecurity tools. What we're noticing in the cybersecurity space is a lot of listicles are getting cited, sometimes from third parties. The LLMs cite a lot of third-party lists on top of first-party lists. CrowdStrike gets cited quite a bit. I think your biggest competitors in the LLM citation space are CrowdStrike and Palo Alto. If you look at the sources here, you can see Palo Alto's top cited link is on artificial intelligence and machine learning, which is why we've added more generic keywords to our content ideas. This is a concept related to artificial intelligence and cybersecurity. If you see more foundational knowledge pieces, that's why we selected those keywords. We also have some listicles. For example, EDR tools. SentinelOne does have an article on this and it is getting cited. So content is trending in the right direction for LLM citations.

**Sydney Go:** And as for the prompts, we can always add more if these aren't all the ones you want tracking.

**Mahati Rapol:** Okay, Ankit, do you want to take that as an action item?

**Ankit Pahuja:** Yes. Can you invite me to the tool, Sydney?

**Sydney Go:** I'm not sure how we can give access to the tool, but we're creating a Looker dashboard to make this easier to parse. I only have access to your dashboard and my other customer dashboards. I don't know how access works with the tool. They're pretty hands-on, so I will ask the team how we can give you access. For now, I can send you all the prompts we're tracking. You can tell me if any aren't things you want to track. It would also help if you told us what topic areas you'd like us to dig into. Generally, for LLM citations, these are very valuable to your product marketing teams, because a lot of bottom-funnel searches on LLM and ChatGPT are around "what is the best cybersecurity solution?"

**Ankit Pahuja:** Just send me the list of topics. I'll look at it and circle back.

**Sydney Go:** Awesome. I really wanted to make sure we finished on time. So that was Scrunch. I'll send you the prompts and you can tell me if there's anything you want to add or remove. We're still waiting on the deep dive with Ali.

**Sydney Go:** So our next steps are: finalize the CVE database with Figma and everything, send you the Content OS so you can start approving ideas, send calibration articles, and send the Scrunch prompts for you to check on. Am I missing anything?

**Mahati Rapol:** No, I think we're good.

**Sydney Go:** Actually, I just realized, Mahati, I think this is the first time we've met.

**Mahati Rapol:** It was 30 minutes, but good to see you. It is nice to finally meet you.

**Sydney Go:** I've heard your voice and seen your face on the calls so many times. I felt like I already knew you. I just completely forgot to introduce myself. I'm sorry.

**Mahati Rapol:** No problem at all. All good.

**Mahati Rapol:** August has been crazy, especially the last two weeks. This month is going to be super crazy. So probably September is when I'm going to breathe.

**Sydney Go:** Thank you for all of your help on all of this and all the feedback. It's always appreciated. Thank you so much.

**Mahati Rapol:** Sure. Take care. See you next week. Bye.
