# Rapyd <> GrowthX - AI Lead Qualification

<metadata>
date: 2025-07-07
time: 17:29 UTC
duration: 27 minutes
organizer: vivek@growthxlabs.com
participants: Mara Leighton, Vivek Shankar (GrowthX), Marc Winitz, Mark Stiltner, Nicolette Mychajluk (Rapyd)
fathom_recording_id: 72561685
fathom_url: https://fathom.video/calls/344528183
share_url: https://fathom.video/share/sKjSXwNx3pR8mbstRePJLKjekxoHVEby
source: fathom
enriched_on: 2026-03-03 14:22 UTC
</metadata>

---

## Summary

Rapyd's team presented a lead qualification challenge: they receive high inbound volume but currently filter leads manually through complex criteria (country, currency, business duration, revenue, website authenticity, compliance checks), eliminating 80% before human SDR involvement. Marc Winitz and Mark Stiltner proposed a two-phase approach where GrowthX could help automate V1 (AI-driven lead scoring to identify qualified prospects) and eventually V2 (personalized content generation and HubSpot integration). Mara Leighton committed to briefing GrowthX's engineering team and developing an initial proposal, while Mark will share detailed qualification criteria via Slack.

---

## Context

Rapyd is a fintech payments platform specializing in handling complex payment corridors and compliance requirements across international markets. The company has successfully used AI to automate their internal compliance process (reducing processing time from weeks to 30 minutes), and they're exploring similar approaches for lead qualification. Marc Winitz (VP-level strategic thinker) and Mark Stiltner (execution lead who's already prototyped solutions in ChatGPT) are seeking to reduce the manual burden on their SDR team by building an AI system that qualifies inbound leads before human review. This conversation was an initial exploration to assess whether GrowthX's content automation and AI workflow expertise could be applied to this sales operations problem.

---

## Relevance

**To GrowthX Delivery:**
- Opportunity to apply content generation workflows (blog, email, landing page automation) to a new domain: lead qualification and personalized sales outreach
- Potential engagement to design end-to-end AI workflow for lead scoring and qualification, similar to Rapyd's internal compliance automation success
- Requires understanding of lead qualification complexity: linear yes/no criteria process with subjective validation elements (e.g., "professional website free of typos")

**To CheckThat:**
- Rapyd's qualification process involves website authenticity, social media presence, and compliance verification — overlaps with AI visibility and verification expertise
- Potential application of CheckThat technology for lead verification (website legitimacy, real company validation)

**To GrowthX Business Development:**
- Strong early signal: Rapyd has internal mandate, AI success track record, and budget for process automation
- Marc Winitz indicated "high interest" but emphasize this is exploratory; no formal project or timeline pressure yet
- Two-phase approach: V1 (lead scoring) realistic near-term, V2 (HubSpot + content personalization) longer-term vision
- Potential follow-up contacts: Yana Pearson (Global Demand Gen) for SDR operations insight, Mikael (Marketing Ops) for HubSpot integration questions

---

## Overview

- Rapyd seeks to automate complex lead qualification process, currently manual and time-intensive
- Goal: Efficiently identify quality leads from large inbound volume before human SDR involvement
- Two-phase approach: V1 focuses on lead scoring/filtering; V2 aims for personalized content generation
- GrowthX to review qualification criteria and propose AI-driven solution leveraging their expertise

---

## Key Topics

### Current Lead Qualification Process

  - Manual, multi-step process including:
      - Basic criteria: country, currency, business duration, revenue
      - Detailed verification: website authenticity, social media presence, company/individual legitimacy
      - Compliance checks: anti-money laundering, sanctions screening
  - Process is time-consuming, often eliminating 80% of leads before deeper evaluation

### Automation Goals

  - Streamline initial qualification to identify promising leads quickly
  - Reduce human involvement in early stages of lead assessment
  - Potentially integrate with HubSpot for seamless workflow
  - Future vision: Customize outreach (emails, landing pages) based on qualified lead data

### GrowthX's Potential Role

  - Leverage AI expertise to design end-to-end automated workflow
  - Adapt blog content generation skills to lead qualification and personalized outreach
  - Collaborate on process re-engineering using AI, similar to Rapyd's compliance automation success

### Project Phases

1.  V1 (Initial Focus):
    
      - Develop AI-driven lead scoring system
      - Identify qualified leads worth human follow-up
      - Provide coherent analysis of large lead volumes

2.  V2 (Future Expansion):
    
      - HubSpot integration
      - Personalized content generation (emails, landing pages) for ICPs
      - Automated sales team preparation with targeted talking points

### Technical Considerations

  - Linear qualification process with yes/no criteria (no complex weighting system)
  - Potential for nuanced interpretation of subjective criteria (e.g., website professionalism)
  - Opportunity to flag unclear information for human review

---

## Action Items

**Mara Leighton (GrowthX)**
- Brief engineering team on lead qualification problem. Workshop potential solutions. Identify gaps in understanding.
- Review qualification criteria from Mark. Prepare questions for subject matter experts (Yana Pearson, Mikael) if needed.
- Develop initial thoughts/proposal on lead qualification automation. Schedule follow-up meeting to present.

**Mark Stiltner (Rapyd)**
- Send qualification criteria and workflow details to Mara and Vivek via Slack.

---

## Transcript

*Opening pleasantries about time off and Colorado omitted for brevity.*

**Mara Leighton:** So I'm not sure how much was covered in the weekly sync, but the goal here is just understanding what is the current state, what are the pain points, and what's the ideal end state, and then the details we can go over in the future.

**Marc Winitz:** We're in exploration mode right now, trying to understand what a use case like this could look like and whether GrowthX could help. Our business has very specific qualification requirements at the top of the funnel, and we generate a lot of inbound volume, but we don't have the capacity to have humans involved early on. Standard data enrichment is useful but doesn't give us enough information to justify sending to an SDR. However, based on other things Rapyd has done with AI, we're able to look at different data sources, fill in information, and get a much clearer picture before even taking it to an SDR.

Let me give you an example. We're currently using AI to gather data and see if prospects make sense for our compliance process, which is very time-intensive and burdensome. We're thinking we could do something similar for top-of-funnel lead qualification. For instance, we'd want to know the prospect's actual use case, what they're trying to do from a payment perspective — are they trying to collect money or disperse money? What corridors are involved, meaning what currencies and countries? There are multiple factors like this we'd like to get answers to.

Mark has already started work on this, and I'll let him expand from here. This is why we wanted to get together.

**Mark Stiltner:** The current lead qualification process has significant complexity. When someone comes in, we look at form data and ensure it meets basic criteria: What country are they in? Is it on our approved list? What countries do they want to do business in? What currencies do they want? How long have they been in business — at least six months? Are they processing at least a million dollars in annual revenue? This basic qualification already kicks out 80% of inbound leads before we even begin deeper review.

But there's more. After basic checks, we do anti-money laundering and sanctions verification because threat actors will spin up fake websites and try to access payment systems. We do detailed verification: whois.net searches, internet history checks, social media verification, and LinkedIn verification — Is this a real person? Do they really work for that company? Has the company been around? Is there third-party news validating their employment? This entire ID verification step is comprehensive.

Once leads pass both basic and ID verification — right country, right currency, real company, real person, minimum six months in business — we have a qualified lead we can follow up with. But then we need to go deeper into what they actually want to accomplish.

That's where we want to automate. Right now we're doing manual scoring, but we'd like to run ABM at scale. Once we know all this information about a company from the qualification process, we want to customize emails, landing pages, messaging, and sales team prep. Instead of SDRs sending a list of 10 questions, we fill out 4-5 ourselves, provide contextual elements, and send a well-formulated email saying, "Here's what we know about you. Here's how we think we can help. Here are a couple other questions." Speed matters — a lot of the time, whoever gets back first wins the deal, even if we have a better proposition.

Ultimately, we want to integrate this with HubSpot so that when someone fills out our website form, it goes through this process and automatically sends a personalized email.

**Mara Leighton:** That's great. I love how you're thinking about this. I have a few follow-up questions. What stage is currently automated? Is everything you described being done manually — the ID verification, the deep research to determine leads are genuine?

**Mark Stiltner:** Everything is manual right now. I've proof-of-concepted these ideas in ChatGPT to make sure they could work. I said, "Run a search on whois.net, look at this person on LinkedIn, check these criteria, and see what you can come back with." It works, so I have proof of concept that it'll function. But it's a series of prompts, not a fully automated workflow yet.

**Mara Leighton:** Knowing you've already started thinking about this, what would be most ideal for us to help with? How do you see us fitting in?

**Mark Stiltner:** From my perspective, you guys know how to build really well-thought-out, automated end-to-end workflows with content. You've done that with blogs. It doesn't seem like a huge leap from blog to landing page or blog to email. I'm looking at you to bring that technical expertise and say, "Blog is one use case. Here's another." Can you help us build that same thing and run it at scale?

It doesn't have to be limited to contact forms on our website. Once we have it running at scale, we could proactively target everyone we think is a customer profile and run an ABM campaign for them. Or we could take every attendee at an event and run this process for them.

**Marc Winitz:** That proactive scraping approach is good, but we're not quite ready for that yet. Right now we're trying to solve the problem of having too much stuff we can't get to — whether it's inbound, content we're generating, or event leads. We'll grab 500 contacts at a trade event and start qualifying them, but then getting the BDR team involved is really difficult. I want to see if we can solve for this.

This use case is similar to how we solved our compliance process — which is handled by a different team but was blocking time to revenue. Our CEO got directly involved, and we sat engineers down with the compliance team. They essentially hacked together processes to automate what was very complex, removing the human element entirely. What took us a month — including back-and-forth with prospects for additional information — now takes 30 minutes. That's the power we're after for lead qualification.

As for where you fit in, I'm not entirely clear. It's more a conversation between us to figure out how much we do versus how much GrowthX does. What I will say is I've watched your workshops and what you're building with Atlas. You guys clearly understand process re-engineering with AI. The question is how much or how little you get involved.

**Mara Leighton:** That makes complete sense. I'm also trying to determine if we're supplementing something you've already started building or if we're building from scratch. What sounds like is my next step will be bringing this to our engineering team to workshop it with them. What's your ideal timeline? That helps me understand rollout.

**Vivek Shankar:** I have a question about the outputs.

**Vivek Shankar:** You mentioned newsletters. What other content are we talking about? Just a series of follow-up emails? Landing pages too? ICP-specific content from your blog?

**Mark Stiltner:** Yes, I'd love to get to the level where we generate a custom landing page for each person with links to relevant blog posts, case studies, and e-books from our website. Then a series of emails — one initial email and a couple of follow-ups. We'd definitely leverage our existing content.

**Mara Leighton:** Do you have a resource that lists all the qualification criteria in one place? That would help me give engineering maximum visibility.

**Mark Stiltner:** I can share the whole qualifying criteria I was working with. I can share the raw materials and even my workflow, though I'm torn about whether sharing my approach might anchor people to my thinking or open up better paths. I'd prefer to share the raw materials.

**Marc Winitz:** No, I want Mark to share his thinking. How would you attack this problem? Could you attack it? What would that look like? We can always compare after you've done your work and see if there's a better way.

Ultimately, at the end of the day, this is about taking a large amount of top-of-funnel inbound and determining if there's something there or not. It eventually goes to a human, but we want to cut down that process — find the needles in the haystack. Out of 500 leads, look at 100, or 20, or however many are qualified enough. The output might not be just content. It could be a directional score — checking data sources, AI analysis, determining if it's probably worth someone's time to take a closer look. That's the output.

**Mara Leighton:** So V1 is solving the pain point, winning back time, and making this data dump coherent and comprehensive — the analysis piece. V2 is HubSpot integration, building ICP-specific content, separate email flows, separate landing pages. And Marc mentioned prepping the sales team with talking points based on which ICP bucket they fit into and what's worked to close similar deals. Anything else critical we should understand?

**Vivek Shankar:** Do you have weights on each criterion? Someone might not have a LinkedIn profile, but they're in the right business with good revenue. How do you prioritize?

**Mark Stiltner:** There's no weighting. It's a yes-to-all-or-kicked-out approach — a linear flow. Is the website real? Yes or no. There are validation steps beneath that, and theoretically you could weight individual criteria like a privacy policy at 1.0 and a shipping policy at 0.5. But the SDR team walks through a linear yes-or-no process, and if it's yes all the way, you're good.

**Mara Leighton:** If some information isn't readily available, we can flag it during human review — "Privacy policy was unclear" — that should be straightforward to build in.

**Marc Winitz:** I'll share the whole process with you.

**Mark Stiltner:** You'll see it's fairly linear. The subjective part is criteria like "Is it a professional template free of typos?" That's easy for a human. But if you tell that to AI, it'll find a typo on the Library of Congress website and reject it if you don't phrase it carefully.

**Mara Leighton:** What's your timeline? I need to brief engineering accurately.

**Marc Winitz:** We have high interest, but there's no formal project yet. This is early conversation. We're not asking for huge effort right now — just this discussion, you talk to your team, and we go from there. Timelines get established based on what comes back. Sooner is better, but there's no external pressure beyond this being an ongoing issue we'd like to solve.

**Marc Winitz:** One resource I'd offer: if you need more insight into the qualification process, you could talk with Yana Pearson, who runs Global Demand Gen for us. She works with the sales organization on lead activity and can give you good context on what the SDRs are dealing with. And on the HubSpot/MarTech side, there's Mikael on my team who runs marketing operations. He could answer questions about lead flows and how this integrates.

**Mara Leighton:** My next step is chatting with our team to make sure we haven't missed anything, then addressing secondary questions with subject matter experts and bringing it back to you. This has been super helpful and an exciting problem. Thanks for bringing us in.

**Marc Winitz:** This is good for starting the conversation. When you're ready with initial thoughts, it can be a separate meeting if needed.

**Mara Leighton:** I'll keep you posted as soon as I hear from the engineering team. Thanks for your time.

**Mark Stiltner:** I'll send you the qualification criteria on Slack.

**Marc Winitz:** Perfect. Thank you.
