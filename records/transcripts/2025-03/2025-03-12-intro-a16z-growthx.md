# Intro: a16z <> GrowthX

<metadata>
date: 2025-03-12
time: 16:30 UTC
duration: 31 minutes
organizer: Marcel Santilli
participants: Seema Amble, Zach Cohen, Marcel Santilli
fathom_recording_id: 51531237
fathom_url: https://fathom.video/calls/251375173
share_url: https://fathom.video/share/sFe6wgky3XycdBeZydSSy3pJqcx8-c2j
source: fathom
enriched_on: 2026-03-04 20:45 UTC
</metadata>

---

## Summary

Marcel Santilli presented GrowthX's AI-powered content and marketing platform to Seema Amble and Zach Cohen at Andreessen Horowitz. GrowthX has reached $7M ARR in six months with 75% gross margins, serving clients like Ramp, Abnormal Security, and Reddit by combining AI workflows with expert knowledge and human review. Marcel detailed the company's architecture — representing workflows as code with a robust runtime layer — and roadmap to $23M revenue in 2023, with plans for Series B at $18-20M run rate. a16z indicated strong interest and offered continued partnership.

---

## Context

GrowthX is a B2B content and growth marketing services company founded by Marcel Santilli, combining AI-powered workflows with expert practitioners. The company has grown from zero to $7M ARR in six months through word-of-mouth and direct outreach. Seema Amble and Zach Cohen are part of a16z's AI applications team, which has been actively researching marketing automation and AI-native companies. This introductory meeting served as a platform for Marcel to showcase GrowthX's unique architecture and business traction to potential strategic partners or investors.

---

## Relevance

- **To GrowthX Business Development:** a16z is an active investor and strategic partner in AI-native marketing; team expressed strong interest and offered ongoing support. Potential follow-up discussions for Series B capital or strategic partnership. Multiple deals ($432k, Abnormal $25k/month, Ramp $40k/month) demonstrate strong enterprise market fit.

- **To GrowthX Delivery:** GrowthX hiring world-class experts (former heads of SEO from TripAdvisor and Financix, G2, ClickUp, major publications) as managing directors, enabling differentiation and 74% gross margins. International hiring via vetting workflows allows cost-effective scaling while maintaining quality.

- **To CheckThat:** Frontier data generation through closed-loop feedback from actual client workflows is unique moat. Marcel discussed how GrowthX's data is "front-tier data" that OpenAI and competitors pay billions to generate artificially, giving potential advantage for model training.

---

## Overview

- GrowthX reached $7M ARR in 6 months with 40 employees and 75% gross margins
- Platform represents workflows as code with a robust runtime layer, combining AI, expert knowledge, and human review
- Average deal size is $156k; recent deals range from $25-40k/month to $432k contracts
- Clients include Ramp ($40k/month), Abnormal Security ($25k/month), Reddit, and others
- Marcel recently raised Series A and targets $23M revenue in 2023 with Series B at $18-20M run rate in Q3/Q4

---

## Key Topics

### Marcel's Background and GrowthX Origin

  - Marcel's career spans IBM, HP, HashiCorp, Scale AI, and DeepGram
  - Built successful content marketing initiatives (e.g., SecurityIntelligence.com, TechBeacon.com)
  - Started GrowthX after workshops revealed demand for AI-powered content strategy
  - Closed initial $27k/month deal with Ramp, leading to full-time focus on GrowthX

### GrowthX Technology and Approach

  - Represents marketing workflows as code, similar to infrastructure-as-code
  - Built runtime layer for executing complex, parallel workflows
  - Combines AI, expert knowledge, and human-in-loop processes
  - Focuses on content creation, distribution, and conversion
  - Adapts workflows for each client while maintaining core similarities

### Team and Expertise

  - Hiring industry experts as managing directors (e.g., former TripAdvisor, G2, ClickUp leaders)
  - Utilizes international talent for cost-effective execution
  - 40 employees currently, with plans to invest in capacity building

### Business Model and Financials

  - \~$7M ARR achieved in 6 months
  - 75% gross margins in Q4 2022
  - Average deal size of $156k
  - Clients include Ramp, Abnormal Security, Reddit, and others
  - Recently raised $12M in funding

### Future Growth and Strategy

  - Targeting $23M revenue in 2023
  - Considering acquisitions of smaller agencies to expand expertise
  - Potential Series B raise in Q3/Q4 2023, aiming for $18-20M run rate

---

## Action Items

- **Marcel Santilli (GrowthX):** Continue scaling operations, maintain Series B pipeline targeting $18-20M run rate by Q3/Q4
- **Seema Amble and Zach Cohen (a16z):** Stay in touch, provide partnership support and strategic guidance
- **Both:** Schedule in-person coffee meeting in San Francisco in coming weeks/months

---

## Transcript

**Seema Amble:** How are you?

**Marcel Santilli:** Happy Wednesday. Yeah, likewise. Where are you based?

**Seema Amble:** I'm in San Francisco.

**Marcel Santilli:** What about you?

**Seema Amble:** Right now I'm at home in Oakland Hills, around Montclair, but we have an office in SF as well.

**Seema Amble:** Well, I think Zach is in transit.

**Zach Cohen:** Hey, sorry, I'm stuck in New York traffic, but that's so lovely, you know. It's better than a podcast. So I'm excited to dive in.

**Marcel Santilli:** Yeah. I was in New York last year. I haven't been back in a while. San Francisco feels like it's coming back, but New York was like, wow. There's a lot of people. We go out to dinner and it's packed, like totally Tuesday. It's wild.

**Zach Cohen:** Yeah, if you're doing good weather or the month's turning to good weather, it gets crazy. But New York in August is the best month, which is a hot take in my opinion.

**Marcel Santilli:** Yeah, literally.

**Seema Amble:** Well, Marcel, great to meet you. Zach and I will do quick intros. We've heard really great things about GrowthX, so excited to chat more.

**Marcel Santilli:** Yeah, likewise.

**Seema Amble:** Zach, you want to go first?

**Zach Cohen:** Let's do it. So I've been here a little over two years, working alongside the AI applications team. We've spent a lot of time as one of the deep dives in the marketing space. We've looked at basically every angle — market research, user research, content creation, marketing automation, new-age agencies with AI. Any part of marketing, we've touched and looked at. And it feels like a pretty obvious space for AI to really disrupt. We've seen it all the way from SMBs to enterprises paying hundreds of thousands of dollars for content creation or content and AI platforms.

**Seema Amble:** I was at General Atlantic before this, spending a lot of time in consumer internet and ad tech for a couple of years. Then I'm Seema, a partner on our large team here with Zach. As Zach mentioned, we've been spending a lot of time in marketing. We've probably met 50-plus companies this year. I've been here for five years. Before that, I spent about a decade investing in software, so I looked at the last generation of Martech as well. Anyway, it seems like you've got some really great logos and things are working. We'd love to understand what's been going on and why you decided to build this business.

**Marcel Santilli:** Yeah, it's been a wild journey but a lot of fun. I'm originally from Brazil, grew up in Texas, and started my career at large enterprises like IBM. One thing that struck me was IBM spending millions on ads and content syndication. That's still happening — Abnormal Security just closed and they're spending $3.2 million a year on content syndication, which is their lowest ROI marketing initiative. But marketers get measured by leads, so they waste money on vanity metrics.

I realized early on that if we took a fraction of that spend and built great content, we could be bigger than the New York Times. I started building websites in high school, then an agency in college. I convinced IBM's general manager to let me spin up SecurityIntelligence.com — somehow it's still out there 15 years later. In the first year, we drove $17 million in contributed revenue and over $50 million in pipeline. We published 300 articles, won a B2B Best Marketing Site Award, and had the highest ROI of any marketing initiative.

That led to HP asking me to build something similar. We hired managing editors from Wire and Computer World and created TechBeacon.com. I built a contributor network where we'd approach speakers at conferences and offer to pay them per word to publish with us. Over time, experts were begging to publish for free. The site grew to a million visitors per month, all organic, with a newsletter of 200,000 subscribers. It became 52% of all leads for the company. The ROI was insane — we spent $20-30k a month to run it but generated over a million dollars in traffic monthly.

Fast forward through HashiCorp (went from $6-100 million in two years), Scale AI, and DeepGram. At DeepGram, my wife and I went through a difficult IVF journey with multiple miscarriages. We have a 22-month-old daughter, Zabela, our miracle baby. Scale was a very hard place to work as a leader, so I left and joined DeepGram, which was much better for my mental health. I wanted to get back to building, so I delegated as CMO and spent two days a week stitching together LLM workflows. I combined everything I knew about content strategy — ideation, research, opportunity finding, publishing — and built workflows with human editors in the loop. We published 3,000 pages, got 24x traffic growth, and 4x revenue growth. That's when I thought, "Oh crap, this works."

I launched a newsletter called AIminds.com and got to 300,000 subscribers. People started asking me to show them what I did. I ran workshops where 170 people paid $500 each — a great way to find ICP. But after the first workshop, people said, "This is amazing, but I don't need the tool. I need the strategy. I need you to adapt AI workflows to my needs and have humans in the loop to do the grunt work and check quality." I said yes to two workshops, and they became eight.

Then in September, Ramp signed a $27,000 a month deal after one 30-minute meeting with Eric and Karim. Karim is now a huge investor in us. I quit my job, partnered with my CTO Daniel (who built IFTTT), and things snowballed. We're about to hit $7 million ARR, have 40 people, and just closed our Series A. We moved really fast. We didn't need the money badly, but we wanted to double down on engineering talent especially.

**Seema Amble:** Yeah, we'd love to hear about the tech behind it. I'm impressed that Eric and Karim usually don't buy software directly. I'm curious how you got them to buy this on one go.

**Marcel Santilli:** It was actually a really cool story. I was interviewing to be CMO at Ramp way back.

**Marcel Santilli:** And I met Eric, and we had two meetings.

**Marcel Santilli:** And we really hit it off.

**Marcel Santilli:** And it was very early on around.

**Marcel Santilli:** But then I got an offer from scale.

**Marcel Santilli:** And I knew the CEO Alex for a couple years already.

**Marcel Santilli:** And you know, it was kind of like I brainer a little bit.

**Marcel Santilli:** It was early in the Ramp process. I got an offer from Scale, and I knew CEO Alex Krizhevsky, so I took that. But Ramp became incredibly successful. Years later, someone I knew became interim CMO of Ramp and said, "Eric's going to be in San Francisco. Why don't you show him what you've been doing?" I did. Karim was in the room too — I didn't even know who he was. But by the end, Eric said, "This is really impressive. This is really freaking cool." Karim said, "Everyone we hire from now on, I want them to be able to do this." Then he said, "Why don't you work from here today?" And after I left, he came back and said, "I know you're probably not raising, but if you do, I'd love to invest and work with you." Five days later, we signed a contract. That was the biggest turning point. I called my wife and said, "This is legit. I'm going to build this. I'm going to quit my job and walk away from millions of dollars."

**Marcel Santilli:** We came into this building custom workflows for each customer, then adapting those workflows with the right context and tweaking. But complexity became unmanageable with existing tools on the market.

**Zach Cohen:** When you say custom workflows, what does that mean exactly? Were you building bespoke workflows for each customer?

**Marcel Santilli:** They're bespoke in the sense that they're adapted to the company. The core workflows are similar — how you do research, etc. — but they're customized by persona, style, and targeting. Everything broke when we tried to do this with existing tools. Daniel, my CTO, had experience building distributed infrastructure at IFTTT, similar to Zapier. So we decided to represent workloads as code and build a runtime layer.

What excites me is the paradigm shift. Look at Cursor and GitHub — they made coding better by representing things in code. Terraform did the same for infrastructure as code. But everyone's obsessed with building low-code, no-code drag-and-drop tools. They don't scale because they're just abstracting code underneath. Code itself is way better. Developers would give 20% of their salary to keep Cursor.

The problem is knowledge work isn't well documented in companies. How do you produce content? How do you write an email? How do you prospect a client? We solve this by representing workflows as code with a robust runtime layer that can run things in parallel, retry, and handle observability. Experts architect the workflows and iterate on outputs. Clients give us direct feedback, creating a closed-loop system. This is frontier data that OpenAI pays billions to generate artificially. We're actually doing the work, getting real results, and learning from that.

Our framework works like a coding agent that understands how to build code — the workflows, prompts, steps, activities, and documentation. For example, one of our clients, Smith AI, wants to create a sales funnel guide. We break it down into research questions, find sources across multiple places, check them, and compile. With Deep Research, you wouldn't go as deep unless you prompted excessively. Because we represent this as code, we can evolve it and learn from diffs. Runtime execution is crazy fast — two minutes for a process that would take hours with a low-code tool. Every workflow is auto-documented by AI. The market opportunity is huge. Content budgets are enormous.

**Seema Amble:** How much human involvement is involved to make this work?

**Marcel Santilli:** Right now we're focused on content and growth — content distribution and conversion. Clients range from tutorial and programmatic SEO, long-form content, landing page enrichment, to creative projects. Hers is doing drug comparisons to compete with GoodRx. Webflow wants us to enrich their marketplace. Stacklets wants starter kits for template pages so users don't search tools but get pre-built solutions.

The expertise is most critical. We're hiring managing directors who are world-class experts. Dave started Monday as head of content SEO — he built Finanix to $600 million over 13 years. Jacob did content marketing for G2 and other platforms. Kirk Clint built all AI tooling at ClickUp. We hired an editor-in-chief from a major publication who's joining next week. Underneath, we have pod leads and mini-pods of three people. We hire internationally and use workflows to vet people at scale, similar to Mercer. We have 40 people now, and the headcount-to-revenue ratio is still great.

We have 60 deals in our pipeline and a waitlist, so we're investing heavily in capacity. Gross margin will dip Q1-Q2 as we scale, then come back up.

**Zach Cohen:** So the model is 75% of what you build reusable for the next client, 25% customization, with experts doing the final 20%?

**Marcel Santilli:** Exactly. Take Yellow OAI — they want to run their entire marketing function on our platform. They're launching a podcast and want us to repurpose it into content. We built that in an hour. Our engine is like a coding agent that understands code — workflows, prompts, steps, activities, documentation. We call it the Task Hub (how experts and humans review) and the Learn Engine (training domain-specific models). It's verticalized. We have recruiting internally.

**Zach Cohen:** And this budget comes from their marketing team?

**Marcel Santilli:** Mostly from the CEO directly. Abnormal's mandate is to be AI-native. Reddit's COO said, "We need to be more AI-native. Go figure it out." People use AI tools but have no internal knowledge. They try to learn prompting, but everything changes weekly. They hire agencies doing old-school work. Reddit fired two agencies that were expensive and delivering the same output. Companies want expert fractional CMOs, AI workflows, automation, tooling, and people doing grunt work — all for 10 cents a word, the same as outsourcing. That's a no-brainer. White-glove service, expert leadership, automation, future-proofing AI, and they don't hire freelancers. Average deal is $156k.

**Zach Cohen:** Incredible numbers.

**Seema Amble:** We're not seeing those in the market to be fair.

**Marcel Santilli:** Yeah, right now we just signed a $432,000 contract after one meeting. We told them we're booked through April. Abnormal is $25k/month. Another deal is $40k/month. All 12-month contracts.

**Seema Amble:** Nice.

**Marcel Santilli:** I've got to run, but I'd love to keep building this relationship. We're moving super fast. Our goal is $23 million this year, which is literally just closing three deals a week like we've been doing. If nothing changes, we hit that. We raised $12 million but just enough. We're not burning through it fast. Now we're investing more aggressively ahead.

**Seema Amble:** What's your milestone for raising Series B?

**Marcel Santilli:** Q3/Q4, anywhere from $18-20 million run rate. We cap valuation fairly low so employees have low exercise costs. We're trying to be very employee-friendly with great benefits. I've been burned on equity multiple times, so I want the opposite. High leverage model means we can really scale with great people.

One big opportunity for Series B is acquiring smaller well-run agencies. Multiple have reached out asking to partner or merge. We have $3 million revenue agencies with amazing talent we could buy at a reasonable multiple and immediately make more efficient with our platform. For example, we need e-commerce expertise — we could acquire a $3M e-commerce agency and scale it with their expertise and our infrastructure.

**Seema Amble:** Amazing progress. We've looked at a lot of companies in this category and very few are working as well as you are. Congratulations. You obviously have an incredible background and know what you're doing. We'd love to stay in touch. If there are ways we can be helpful, please keep us posted.

**Marcel Santilli:** We love that. Definitely likewise. In the next few weeks or months, since we're all in the Bay Area, let's grab coffee or spend time in person.

**Seema Amble:** Totally. Thanks, everyone.
