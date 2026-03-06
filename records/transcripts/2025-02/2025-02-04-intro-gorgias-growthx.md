# Intro: Gorgias <> GrowthX

<metadata>
date: 2025-02-04
time: 17:16 UTC
duration: 34 minutes
organizer: Marcel Santilli (fwd.digital)
participants: Marcel Santilli (fwd.digital), Bruno Santilli (GrowthX Labs), Guillaume Aubert (Gorgias), Maxime Sutra (Gorgias), Arnaud Jeannin (Gorgias)
fathom_recording_id: 45537376
fathom_url: https://fathom.video/calls/225370247
share_url: https://fathom.video/share/gnNpZN_HnPMz2FTdzDdDW4qXjLFFAuSM
source: fathom
enriched_on: 2026-03-04 12:00 UTC
</metadata>

---

## Summary

Marcel Santilli demonstrated fwd.digital's technical approach to AI-powered content generation, walking the Gorgias growth team (Max, Guillaume, Arnaud) through custom TypeScript workflows, research agents, and a proprietary runtime layer that orchestrates multi-step content pipelines from research through publication. Ramp case study showed organic traffic growing from 0 to significant volume since September engagement, with fwd.digital's pricing at 10 cents per word delivered through a fully-staffed dedicated team. Next steps: Marcel to send Max a detailed pitch for Gorgias' Director of Integrated Content, covering the technical differentiation from simple AI-powered solutions, the step-by-step process (website inspection, persona development, jobs-to-be-done analysis, keyword surfacing, competitive analysis, search volume filtering), and timeline for engagement and results.

---

## Context

This was an introductory call between Marcel Santilli (GrowthX / fwd.digital) and the growth team at Gorgias, a customer service platform (Guillaume Aubert, Maxime Sutra, and Arnaud Jeannin). The connection originated from a casual conversation at Saster conference where Marcel spoke and met Gorgias' CTO, who discussed their AI work. Maxime had also learned about fwd.digital's deep-dive content strategy for Ramp through a mutual contact (Jia) and their own past test with Arabs (which didn't deliver strong results). Gorgias is exploring whether they can replicate fwd.digital's programmatic content generation approach at scale without hiring additional headcount.

---

## Relevance

**To GrowthX Delivery:**
- Config-file-based workflow approach using TypeScript and AI coding agents (Cursor) enables rapid scaling without traditional no-code platform limitations
- Ramp case study demonstrates 4-month trajectory from research kickoff to measurable organic traffic gains; deep-dive, multi-step content pipelines (research, persona development, jobs-to-be-done, outline, draft, calibration, post-processing) are core to quality differentiation
- Dedicated, fully-staffed team management model is the key differentiator from pure AI-powered content tools; weekly syncs, editorial oversight, and calibration loops built into the process
- Pricing at 10 cents per word scales better than hiring in-house or outsourcing to agencies; strategy emphasizes planting seed content then enriching over time rather than perfection on first publish

**To GrowthX Business Development:**
- Gorgias is a high-potential B2B SaaS prospect (Series-A-track company, strong growth team, technical sophistication); interest in programmatic content suggests fit for broader strategic partnership
- Gorgias' need to pitch this internally (to Director of Integrated Content) indicates deal requires education and structured proposal; Max requested specific differentiation message and process flow details
- Potential for extended engagement: Marcel mentioned possibilities for multiple projects, platform access, and collaborative testing

**To CheckThat:**
- Gorgias' interest in AI-driven content at scale connects to AI visibility and search ranking outcomes; strong case study (Ramp) demonstrates measurable organic lift, which is valuable reference for CheckThat value prop
- Workflow emphasis on research agents, vector databases, and query generation are relevant to CheckThat's AI engine visibility and content relevance scoring

---

## Overview

- fwd.digital offers a comprehensive, AI-assisted content generation service built on a custom TypeScript-based workflow engine, with human expertise and dedicated team management in the loop
- Their approach combines advanced AI workflows (research agents, vector databases, AI coding agents like Cursor) with multi-step content pipelines (research, persona development, jobs-to-be-done, outline, draft, calibration, post-processing) for scalable, high-quality content creation
- The service includes in-depth research, strategy development, and content calibration tailored to the client's brand and goals, delivered by a fully-staffed team that meets weekly and continuously tweaks workflows based on feedback
- Performance metrics from Ramp show significant organic traffic growth starting September 2024; pricing at 10 cents per word is competitive with offshore hiring and less expensive than traditional agencies
- Key differentiator: doesn't just scrape top 10 results and feed GPT; instead uses custom research guidance, vector databases, and multi-stage editor review to decompose high-quality content generation from first principles

---

## Key Topics

### fwd.digital's Technical Approach

  - Utilizes a custom-built framework with config files and TypeScript for flexible, scalable workflows
  - Employs AI coding agents and a proprietary runtime layer for efficient process execution
  - Creates modular, reusable components for various content generation tasks
  - Integrates with existing tools (e.g., AirOps) for user-friendly interfaces

### Content Generation Process

  - Starts with comprehensive research on the client's business, audience, and competitors
  - Develops personas and "jobs to be done" to inform content strategy
  - Uses AI to generate search queries and identify relevant topics
  - Implements a multi-step workflow for each piece of content, including research, outlining, drafting, and post-processing
  - Incorporates human editors throughout the process for quality control and brand alignment

### Differentiation from Other AI Solutions

  - Goes beyond simple keyword scraping and GPT-based generation
  - Utilizes custom research guidance and vector databases for more relevant, high-quality content
  - Focuses on scalability without sacrificing quality or brand voice
  - Provides a fully-staffed, dedicated team to manage the process and understand the client's business

### Performance and Pricing

  - Demonstrated significant organic traffic growth for clients like Ramp
  - Offers competitive pricing at around 10 cents per word
  - Aims for both quality and volume, with a strategy of "planting seeds" and enriching over time

---

## Action Items

**Marcel Santilli (fwd.digital)**
- Send Guillaume Aubert info on Busius, Brazil travel recommendations (personal favor; Marcel mentioned Busius as a favorite town outside Rio during conversation about Guillaume's upcoming Brazil trip)
- Send Max a detailed recap message for Gorgias' Director of Integrated Content including: (a) pitch for fwd.digital's solution; (b) differentiation from other AI-powered content tools; (c) detailed, step-by-step breakdown of the machine process (website inspection to understand business, persona development, jobs-to-be-done research, AI-driven search query generation, competitive analysis, search volume filtering, content clustering for editorial vs. programmatic tracks)

**Maxime Sutra (Gorgias)**
- Pitch fwd.digital solution internally to Director of Integrated Content/Marketing + SEO team for potential engagement

---

## Transcript
**Bruno Santilli:** This meeting is being recorded.

**Bruno Santilli:** Hey, hey, hey.

**Marcel Santilli:** What's going on, man?

**Bruno Santilli:** I'm trying to find a nice background here to look professional. Work it out by office here. You don't look tired, man.

**Marcel Santilli:** Oh, yeah. I got back last night. I woke up four in the morning, then left at 6:30, and got back at 11.

**Bruno Santilli:** Different time zones?

**Marcel Santilli:** No, same time zone. Seattle is right along the same line.

**Bruno Santilli:** That's cool. Well, I had a small errand to run this morning. I had to return a car I purchased two weeks ago. I bought a four-by-four to get into deep tropical forest, but turns out it only had a two-wheel-drive system that didn't lock. So I had to get towed out of a lot of sticky situations. I washed it and took it right back to the store.

**Marcel Santilli:** And they took it?

**Bruno Santilli:** Oh yeah, they returned the money. Now I'm looking at another vehicle. I'll send you some videos. You're going to love it. I know the family is going to enjoy doing adventures like that.

**Marcel Santilli:** It's cool.

**Bruno Santilli:** How many cakeoffs do you want to do next Monday?

**Marcel Santilli:** You forgot to do three. You've got to grow now.

**Bruno Santilli:** Just let me check with the customer about the Zoom link.

**Guillaume Aubert:** Hello, Marcel.

**Marcel Santilli:** Hey, how are you?

**Arnaud Jeannin:** Hi.

**Guillaume Aubert:** Nice to meet you guys.

**Marcel Santilli:** Nice to meet you. I never know if folks prefer Google Meet or Zoom. There are things I hate about both.

**Max:** Nice to meet you. You guys are brothers?

**Marcel Santilli:** We are brothers.

**Marcel Santilli:** I'm in Brazil right now. The company has been taking off and my brother asked for help, and it's been a lot of fun.

**Bruno Santilli:** We're in Brazil.

**Guillaume Aubert:** I'm going to Brazil in 20 days.

**Marcel Santilli:** Is it your first time in Brazil?

**Guillaume Aubert:** Not the first time in Brazil, but my first time during Carnival.

**Marcel Santilli:** You've got to go to Busius when you're there. It's a little town just outside Rio, really nice. I'll send you some stuff. It's one of our favorites. You can Google it and make everyone jealous.

**Guillaume Aubert:** Thanks.

**Marcel Santilli:** Well, it's awesome to connect. I have a cool backstory. I was invited to speak at Saster this past year, and your CTO was there. We chatted backstage about what you all do with AI. I've also heard great things from Jia. So I'm excited to connect. Maybe we can do a quick round of intros on your end, and we can do the same on ours.

**Max:** Sure, I can start. I'm Max, leading the growth department at Gorgias for a while now. I spoke with Kaban, my mentor, about your deep-dive playbook, and I was really excited about it. A couple of months ago we had a call with Arabs, but it wasn't that relevant for us. The reason I reached out to you, Marcel, is because what you did for them is impressive — the directory, the metrics, the AI work. I want to understand what it involves, how it works, and if we can replicate it to have programmatic flows that generate articles and drive traction versus just AI-powered articles. I read the article on Ipagros and it's quite technical. I asked Guillaume and Arnaud to join. Both are growth engineers — Guillaume leads the team, and Arnaud was recently hired. We can go deep into the technical aspects.

**Marcel Santilli:** That's amazing. We don't have a ton of time, but let me jump in. I'll give a quick background, and we can spend more time later. After our deep-dive work, we started running workshops teaching people how to replicate what we built. We realized the existing tooling wasn't scaling. I brought on my CTO co-founder Daniel, who was the product and engineering lead at IFTTT — that workflow automation platform with 4-10 million users running billions of recipes monthly. The company has evolved tremendously. Let me share my screen. One of the first things we do is set a strategy using research agents. We built our own runtime layer. We use AirOps as a UI because they built great things, but underneath the hood is what matters for technical teams like yours.

**Marcel Santilli:** We built a config-file approach, similar to Terraform. With knowledge work, drag-and-drop tools just don't work. We built a framework that plugs into AI coding agents like Cursor, representing workflows as files with prompts, steps, and activities. That's essentially auto-documentation of the flow. What used to take weeks to build in AirOps, we now build instantaneously. The more customers we get, the better the system gets. Let me show you a company contacts generator — it scrapes your website, enriches different sections, generates AI contacts, and returns a brief. All represented in code. I've never shown this to anyone, but you're engineers, so the level should be right. We just finished a Series A round, actually signed the term sheet yesterday. Everyone is obsessed with GUI tools, but we believe we need a paradigm shift. We're starting with outcomes — that's why we deliver everything in services. We use that process to describe the work in config files. Then we build a library of tools, almost like little modules we can spin up quickly. For example, we're doing thousands of pages for drug comparisons for Hims with a custom knowledge base. Everything is in TypeScript. We can generate workflows that are self-contained and plug into coding agents with our runtime layer.

**Marcel Santilli:** This is all the work happening right now. One is running live, generating code rates, inputs, outputs, and descriptions. It generates search queries and processes them. That's the behind-the-scenes work. Then we take all of this and generate a strategy — whether you want programmatic or editorial content. We come up with something we call a content OS to manage content workflows. It looks very different per client. For DeepGram, we had 3,000 pages, which looked very different. Programmatic is very different from individual portals. Once we have that, we move content along both from editorial and programmatic angles. With Hims, we use our APIs, and we have a fully staffed research agent team. We look at sources and use them throughout the process. For drafting and outline planning with programmatic content, we feed it some level of outline or template because it's fairly templated. You end up with really well-written pages. We go through a calibration process to ensure it meets your standards. That's super critical.

**Marcel Santilli:** Let me show you some examples. We did work for Homebase and when you look at sources, you can see how to calculate annual income and this page ranks for annual income in ChatGPT. We've done similar work for Ramp with enrichment. We also did per diem articles. Then there's another cool example — a landlord hub resource covering 80 state laws. That could be really problematic. We've done articles like that for DeepGram, and they rank really well and do really well. You can see we chose clusters of technical questions people have around the tool.

**Max:** So just to clarify — step one is your crawler inspects the website to figure out what you sell, correct? Then how do you detect keywords to write about? I think I missed that part.

**Marcel Santilli:** Yeah, absolutely. Let me show you the researcher flow output. This is easier to see in this format. Essentially, the client we picked up a couple weeks ago — this AI tool — the workflow does research coming up with background details and starting to understand their target audience, personas, products, and features. It develops personas deeper, which we use for kickoff and calibration. It's usually pretty decent and spot-on. It goes deeper into what motivates individuals and their industry dynamics. Then we do what we call jobs-to-be-done research. We take those personas and understand what jobs they need to do through their experience. If you're a data engineer or developer, we have examples like Norm Security, Galileo AI, Strappy headless CMS, and others. We take that context and use it in our workflows because we need to feed more context about your company. Then we take the jobs-to-be-done, the search queries, and identify your audience competitors and direct competitors, understanding all assignments that could be relevant.

**Max:** How do you find the search queries?

**Marcel Santilli:** Using our workflow from the jobs-to-be-done, we generate these queries. For example, "AI tools for marketing data insights."

**Max:** So your AI first figures out your business, then your model returns a list of queries to create content around, right?

**Marcel Santilli:** Correct. But not just create content. This is still research. We then understand your direct competitors and what they rank for.

**Marcel Santilli:** That informs editorial content. On the programmatic side, we come up with clusters. Sometimes you already have ideas for clusters you want to develop — like per diem and expense categories, which the Ramp team already had. Everything we do can be customized. For example, Hims needed a cover image generator, which we built in a day or two. But the really important part is you get a fully staffed team dedicated to you that understands your business. With Ramp, Bailey is the lead. We post updates, the team sends things over, and we meet weekly. It's a full, fully staffed team. So it's not just the tech. Instead of buying a tool or hiring an expensive agency without tools, we're the merge of both. We have the tech, engineers, and knowledge, and we'll expose more of the platform over time. But you need an expert in the loop — an editor who can review at multiple places.

**Max:** So what I hear is useful. I'm going to pitch this to our Director of Integrated Content and Marketing/SEO. I need to be very clear and non-jargon in how I pitch what you do. Can you guide me through two things? First, what are the different steps of the flow — inspecting, finding queries, analyzing competitors, looking at search volume, et cetera. Second, can you pitch why your solution is different from just getting AI-powered copies? We tested AI-powered solutions before with Arabs, and the content quality wasn't great, and the output team wasn't good either. I need to be very detailed on that differentiation to get the vote to move forward.

**Marcel Santilli:** Yeah, absolutely. I apologize for jumping around. You guys wanted to see underneath the hood. Normally, I can send you a recording later of how we pitch to non-technical people. But I was so excited to show you the underneath.

**Max:** Maybe we can start with that.

**Marcel Santilli:** Yeah, absolutely. Let me show you the first 12 weeks. In the first four weeks, we pick up the engagement and show the content quality. We do all this research using AI workflows, because we need to understand your company, space, competitors, and opportunities. We do a deep audit of everything. Then we start the kickoff and immediately develop a content strategy while starting calibration in parallel. By week three, ideally you feel good about calibration. Maybe week four if it's technical. By week four, we're already publishing and feel good about the content strategy. It's not 12 months of planned content, but it gives direction and goals. This is the direction we're going. These are the types of topics and pages we want to develop. We feel really good about the foundation of content because we developed one bullseye that you felt good about, gave feedback, and that feedback helps us tweak the workflows. Once we have the strategy, we adapt the entire workflow. These aren't one workflow — they're an ensemble of multiple really complex workflows with many editor-in-the-loop steps.

**Marcel Santilli:** We might start with a keyword. We have custom research guidance with a custom researcher app. These are apps we show underneath the hood. They're all the apps these workflows call. We start research on one topic. We set a research goal. The workflow goes through agents that come up with questions to answer. For example, "What are the most efficient design principles for user-friendly real-time voice agents, particularly for developers?" We find sources, go through every one, filter them. Only the ones we determine are relevant and good quality get processed and stored in a vector database for content generation. That's different from tools that just scrape the top 10 results, shove them in a database, and call it a day. We take years of expertise from publishing millions of pages and growing sites, decomposing from first principles how to generate amazing, high-quality content at scale. We use AI to go deeper and assist editors, not replace humans completely. We generate the outline. Editors review it. We generate the title, editor reviews, article generation, and post-processing steps. That's where we adapt to your brand and voice, doing cross-linking, CTAs, and other things you determine during calibration. For some clients, we might have a fact-checker at the end, multiple feedback steps, and reprocessing. You end up with a final article that an editor spends an hour polishing. Then we publish on your behalf and handle all the grunt work. Because of that, we do this at scale without adding burden to you.

**Max:** Can you share the performance from Ramp?

**Marcel Santilli:** Yeah, absolutely. Let me show you. This is one of our slides that's really helpful. This is the high-level view of all steps to generate one article. You can see how complex they are, but they adapt to you based on feedback. With Ramp, this is their overall traffic. This is one of the clusters — maybe the per diem or expense category one. You can see examples of content we've generated. Like "What is the FICA formula?" This page ranks for annual income. We've done similar enrichment for Ramp. They don't want to go all-out; we could do more in depth, but we also did per diem articles for Homebase with similar work for Ramp.

**Marcel Santilli:** And they're doing really well. Another cool example is a landlord hub resource covering 80 state laws. That could be really problematic. We've done articles like that for DeepGram, and they rank really well and do really well. You can see we chose clusters of technical questions people have around the tool.

**Max:** When did you start working with them?

**Marcel Santilli:** In September.

**Max:** So organic traffic started growing from September?

**Marcel Santilli:** Yeah. And the way we think about it — I can send you other examples like Strappy and a few others — ultimately, first, you want to ensure you have a really powerful engine with high-quality content that scales without hiring 50 people. Then we systematically ramp up publishing to see signals. The first signal is getting indexed. You can't just publish 3,000 pages and get indexed. There's a lot involved. We watch that. You see impressions. Okay, now we're getting impressions. You tweak things and get clicks. Halfway through, we ask: what clusters worked really well? What seeds have we planted? What have we tried? Can we double down and enrich over time? We're better off planting 100 seeds and enriching them five, six, maybe more times a year than planting the perfect seed once in lower volume. It's quality and volume. And it all comes out to about 10 cents a word — less than hiring an inexpensive offshore person.

**Max:** Do we need growth engineers to implement each style of the project on our side?

**Marcel Santilli:** As much as I'd like to work with you and maybe expose some of our platform for other projects, we're essentially end-to-end, turnkey, outcome-based.

**Max:** So obviously you want to collaborate on content quality and understand what's going on, but there's no technical requirement on our side?

**Marcel Santilli:** Correct.

**Max:** Perfect. Thank you for the presentation. I see we're at time. What would be super useful is if you could send me a recap message with the best way to pitch it to my Director of Integrated Content. Really emphasize how you're different from the rest. Most AI solutions take the first 10 results and build a cheap application — that's it. Explain deeply how you're different and the different steps the machine does: inspecting the website, surfacing keywords, competitive analysis, search volume filtering. I'd appreciate a proposal with that.

**Marcel Santilli:** I'll pass the water and follow up with you.

**Marcel Santilli:** Awesome, sounds good. I'm really excited. I'd love to work with you all and come up with a kickoff, maybe other cool projects where you can use our platform and test it out.

**Max:** Amazing. Thank you so much.

**Marcel Santilli:** Thanks. Take care. Bye-bye.
