# Nebius (GrowthX.ai)

<metadata>
date: 2025-07-16
time: 14:02 UTC
duration: 32 minutes
organizer: Marcel Santilli (GrowthX)
participants: Roman Chernin (Nebius), Konstantin Drozdov (Nebius), Mashrur Haider (Nebius), Marcel Santilli (GrowthX)
fathom_recording_id: 74500067
fathom_url: https://fathom.video/calls/352914928
share_url: https://fathom.video/share/5LobP54Nzsq2TNu_37Myua_6RhUsofLu
source: fathom
enriched_on: 2026-03-03 14:25 UTC
</metadata>

---

## Summary

Marcel Santilli walked Nebius's product and GTM team through GrowthX.ai's unique AI-driven content creation platform, which combines expert human judgment with AI workflows, processing 1-2M workflow runs monthly across customers like Webflow, Grammarly, and Sentinel One. The team discussed GrowthX.ai's three-layer architecture (expert layer, AI workflows, infrastructure), their use of multiple models (Claude, Perplexity) for different tasks, and their interest in model fine-tuning and open-source optimization as they scale. Nebius positioned their AI Studio and Cloud infrastructure as potential partners in this transition, with interest in exploring agentic systems and efficient open-source deployments.

---

## Context

Nebius is an AI infrastructure company split into two layers: Nebius Cloud (physical AI infrastructure with compute, storage, networking) and Nebius AI Studio (high-level inference and fine-tuning, competing with Fireworks and Together AI). The meeting was initiated by Nebius's GTM team—Roman Chernin (co-founder/CBO), Konstantin Drozdov (GTM), and Mashrur Haider (product manager)—to learn from Marcel Santilli, founder of GrowthX.ai, about how AI-native SaaS companies like GrowthX.ai build and scale. This was an exploratory conversation to understand customer needs and pain points as Nebius expands its AI Studio offering to AI-centric SaaS builders.

---

## Relevance

- **To GrowthX Delivery:** GrowthX.ai's platform design—workflows-as-code, human-in-the-loop review, and parallel processing with a "judge" system—offers a model for hybrid expert/AI delivery that other service businesses could adopt. Fine-tuning on validated feedback loops could dramatically reduce review cycles.

- **To GrowthX Business Development:** Potential partnership with Nebius for infrastructure and model optimization as GrowthX.ai scales. Nebius is actively building for AI-native SaaS, and GrowthX.ai is a reference customer for the content/marketing vertical. Open-source model transition could reduce dependency on frontier models and improve unit economics.

- **To CheckThat:** GrowthX.ai's data generation engine (1-2M validated workflows monthly on publicly available data) and feedback loops are directly applicable to CheckThat's AI evaluation and ranking needs. The "judge" system discussed for parallel workflows could improve prompt evaluation methodology.

---

## Overview

- GrowthX.ai operates a sophisticated AI-powered content creation service with human expertise in the loop, delivering content-as-a-service for brands like Webflow, Grammarly, and Sentinel One
- Their platform uses various AI models (Claude, Perplexity) and custom workflows built by an AI coding agent, processing 1-2M workflow activities monthly
- Technical infrastructure relies on Render (hosting), Temporal (runtime), and Langchain (traceability), with custom failovers for rapid model testing and swapping
- Nebius aims to provide value in the AI infrastructure and model optimization layer, particularly for companies building AI-centric SaaS products
- GrowthX.ai is interested in model fine-tuning on accumulated validated feedback data and transitioning to open-source models as they scale, aligning directly with Nebius's research on agentic systems and cost-efficient model orchestration

---

## Key Topics

### Nebius Overview and Product Offerings

Nebius operates a two-layer platform designed for different customer segments. Nebius Cloud provides physical infrastructure optimized for AI workloads—compute, storage, networking—plus managed services like Kubernetes and model training, targeting AI researchers and companies building bespoke models. Nebius AI Studio is the higher-level platform for AI SaaS companies who don't want to manage infrastructure directly. It offers pre-hosted models, fine-tuning, bring-your-own-model capabilities, and developer tools (evals, traceability, data management). Roman emphasized that AI Studio competes with Fireworks and Together AI, but Nebius's vertical integration across infrastructure and services gives them cost and performance advantages.

### GrowthX.ai Platform and Workflow

GrowthX.ai delivers content-as-a-service using a three-layer architecture: expert layer (award-winning editors and strategists), AI workflows (built by an AI coding agent), and infrastructure. The expert layer is critical because customers don't know what they want or what strategy works—GrowthX.ai gathers context artifacts (company description, product info, target personas) that the customer usually can't provide themselves. The workflows are reproducible blueprints based on expert processes (how a TechCrunch editor would approach an article), distilled into code. Each customer gets custom workflows and strategy, pulling different artifacts and using multiple AI models (Claude for generation, Perplexity for research) for different steps. The platform processes 1-2M workflow runs monthly across clients like Webflow, Grammarly, Sentinel One, and Augment Code.

### Technical Infrastructure and Challenges

GrowthX.ai uses Render for hosting, Temporal for workflow runtime, and Langchain for traceability. They've built custom failover and fallback systems to test and swap models rapidly—critical for responding to new model releases. They mostly use Claude 3.5 Sonnet, with Perplexity for research and other models for specific tasks. They're not compute cost-sensitive (customers pay $10-60k/month, so spending a few dollars per output is fine), and most processing is batch, except for an emerging Canva-like AI editor for real-time artifact editing. Marcel flagged that they haven't found great evals tools yet (tried Calto and Promptfu). The main infrastructure challenge is how to scale fine-tuning: they have thousands of validated workflow examples and human feedback loops, but haven't invested in building fine-tuned models yet because they're still iterating rapidly on strategies.

### Future Directions and Potential Collaborations

Marcel and Roman discussed two future directions. First, GrowthX.ai is exploring "mixture-of-experts" approach: running multiple workflow versions in parallel with a "judge" system to pick the best output, reducing dependency on frontier models. Second, as GrowthX.ai moves from internal platform to external product (in months, not years), they'll need to shift from relying solely on frontier models to using open-source and fine-tuned task-specific models. Nebius is actively researching how weaker open-source models plus a judge/evaluation system can outperform stronger closed models on equal compute. This alignment makes them natural partners for the optimization phase of GrowthX.ai's roadmap.

---

## Action Items

- **Marcel Santilli (GrowthX):** Dig deeper into Nebius AI Studio offerings and explore integration points with GrowthX.ai's infrastructure stack
- **Nebius team (Roman Chernin, Konstantin Drozdov, Mashrur Haider):** Stay in touch for potential partnership once GrowthX.ai moves from exploration/iteration phase to optimization and open-source transition phase
- **Both teams:** Maintain contact to collaborate on research into agentic systems, judge-based model selection, and efficient open-source model deployments as GrowthX.ai scales

---

## Transcript
**Mashrur Haider:** Good afternoon.

**Marcel Santilli:** How's it going?

**Konstantin Drozdov:** It's going amazingly.

**Konstantin Drozdov:** How about you?

**Marcel Santilli:** Pretty good.

**Marcel Santilli:** I'm on my second cup of coffee, so I'm only getting brighter from here, you know.

**Konstantin Drozdov:** But is it early for you now?

**Marcel Santilli:** 7 a.m., not too bad.

**Konstantin Drozdov:** Oof, 7 a.m. is early. Thank you for joining us.

**Marcel Santilli:** The meeting is being recorded.

**Marcel Santilli:** My pleasure.

**Marcel Santilli:** I usually get an early start.

**Marcel Santilli:** We have a two-year-old, so if I'm getting an early start, then, you know, later in the day is just fun, you know.

**Marcel Santilli:** There's no hope for productivity past, like, 5 p.m.

**Marcel Santilli:** for me, you know.

**Roman Chernin:** Hi, Marcel.

**Marcel Santilli:** Hey, Roman.

**Roman Chernin:** Good to see you again.

**Roman Chernin:** It's a new age, indeed.

**Roman Chernin:** Like, we have, like, four people talking and two recording.

**Konstantin Drozdov:** Yeah, yeah.

**Konstantin Drozdov:** And the funny thing, two agents joined before actual people, so, yeah.

**Roman Chernin:** They could speak without us.

**Marcel Santilli:** We're pretty good about being on time.

**Marcel Santilli:** And, you know, I got to learn from them.

**Marcel Santilli:** But so good to connect.

**Roman Chernin:** Yeah, great to connect.

**Roman Chernin:** And thank you for making time with us.

**Roman Chernin:** Let's run, like, we know who you are.

**Roman Chernin:** Like, let's run a quick round of intro from our side.

**Roman Chernin:** And Roman, I'm co-founder and chief business officer of Nebius.

**Konstantin Drozdov:** And my name is Kosta.

**Konstantin Drozdov:** Kosta, I'm in the GTM team of Nebius AI Studio.

**Mashrur Haider:** And I'm sure I'm the tech product manager for AI Studio.

**Mashrur Haider:** Nice to meet you.

**Marcel Santilli:** Yeah.

**Roman Chernin:** Yeah, great.

**Roman Chernin:** And actually, what we're doing, like, Nebius, actually, we have two layers of what we do.

**Roman Chernin:** Like, the first layer that, like, already more mature, let's say, and got significant traction is there.

**Roman Chernin:** AI Cloud, so we built across different regions, physical infrastructure, and then run hyperscaler type of software platform on top of that, that provides access to AI-centric compute, storages, networking, and the layer of orchestration and managed services on top of that, like all the managed Kubernetes, managed learn to train models, and so on and so forth.

**Roman Chernin:** And then the second layer is AI Studio—an interface platform that's competing with Fireworks and Together AI. It's for companies that don't need to go deep into infrastructure. We pre-host models, run them efficiently, handle all the ops, and provide tooling for fine-tuning, bringing your own model, inference, and more. We're building towards platforms like Amazon Bedrock and Google Vertex, with developer tools for building real applications: evals, pipelines, data management and observability.

**Roman Chernin:** Customers are, it's not like black and white, but like ultimately you can think about it like Nebius Cloud is for those who go deep in AI research and do like a lot of things themselves.

**Roman Chernin:** And Nebius AI Studio is ultimately for AI, new AI SaaS companies like who actually build SaaS, new type of SaaS like product, AI centric.

**Roman Chernin:** Could be new companies like yourself, or digital companies that bring AI into their capabilities.

**Roman Chernin:** We have customers doing workloads across both layers. For example, if I'm building a platform like Avatar with a bespoke video model, I might use Cloud to train that model, but in the final pipeline with audio models and LLMs, I'd use AI Studio for the off-the-shelf components. It's not black and white—but ultimately Cloud is for research and deep AI work, while AI Studio is for product and application layer.

**Marcel Santilli:** Yeah, that's amazing.

**Marcel Santilli:** Congrats on all the traction.

**Marcel Santilli:** I first heard of you all when I saw one of the billboards while driving.

**Roman Chernin:** Yeah.

**Marcel Santilli:** And your brand color is my favorite color, so that helps too.

**Roman Chernin:** Yeah, thank you.

**Marcel Santilli:** Green is my favorite color.

**Roman Chernin:** So great job with the brand as well.

**Roman Chernin:** Yeah, thank you for the warm words.

**Roman Chernin:** Yeah, so that's actually like where we are and the purpose of this call, we actually like we as a team with Costa and Mashrur, we are focusing on AI Studio now and we are talking with different people who build this new SaaS applications like to learn more about like your experience, how you build, how you, what infrastructure, use maybe what we struggle with, what we can bring on the market that will like serve better than existing customers.

**Roman Chernin:** And we, again, believe that there are a lot of reasons why we have right to win in this because like it's, it follows our approach vertical integration when we kind of optimize along the full stack, both from technology and from the cost structure perspective.

**Roman Chernin:** So, uh, we see that this market is very much about.

**Roman Chernin:** But like this vertical integration and providing, extracting the best from each layer, like either like new chips that coming and you need inference running on that, either cost structure when you want to provide all the flexibility of different types of arrangements, like we're not necessarily, like people not necessarily want to reserve, they want to do a pay the go, they want to do spots.

**Roman Chernin:** And it's also difficult to do if you're not control underlying infrastructure and you need always like arbitrage, the kind of supply demand.

**Roman Chernin:** So we know we can build something that's like helpful for the people like yourself.

**Roman Chernin:** We are, I would say, not first, like in the meat of this kind of journey with AI Studio and we just want to align and see where is the right spot.

**Marcel Santilli:** So yeah, let me learn more about like use cases.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** I can give.

**Marcel Santilli:** Kind of a high level, like I think we're pretty unique.

**Marcel Santilli:** And so in the kind of our go to market, because service is softer and our platform is used only by our employees.

**Marcel Santilli:** And so everything is delivered as a service, at least for the next like month or so still.

**Marcel Santilli:** And so like the way we kind of think about it is there's three layers or service, there's the expert layer, and then there's the AI workflows and infrastructure layer.

**Marcel Santilli:** And the service is because people don't know what they want, and also because they don't know the right strategies, and you've got to get the right inputs from them as well and align expectations.

**Marcel Santilli:** And no matter how good your platform is, if you don't do that, especially in marketing and growth and sales, right, they just don't know.

**Marcel Santilli:** We start an engagement with the company, and we say, hey, give me a description of all your products.

**Marcel Santilli:** And they're like, go to our website, but it's outdated.

**Marcel Santilli:** Hey, give me a description of your company.

**Marcel Santilli:** These artifacts—the big picture context you need to feed AI workflows—they're not readily available.

**Marcel Santilli:** And if you put the burden on the customer, they end up doing a pretty bad job, right?

**Marcel Santilli:** Like if you use copy AI in Jasper, customers log in and think, "Okay, what do I fill in here?"

**Marcel Santilli:** I don't know what to put here.

**Marcel Santilli:** I'm just going to type really bad sentences.

**Marcel Santilli:** And then you get really bad output because you have really bad context and then bad inputs too, right?

**Marcel Santilli:** So that's what we kind of do.

**Marcel Santilli:** So digging in a bit deeper, think of it as content-as-a-service.

**Marcel Santilli:** And then we have like award-winning managing editors, like our content officer ran TechCrunch for 10 years.

**Marcel Santilli:** Some of our managing directors were at comms for Shopify or Apple.

**Marcel Santilli:** So they're like the best in class.

**Marcel Santilli:** We run all content operations from ideation through to publishing.

**Marcel Santilli:** Strategy, execution, publishing—all major brands like Webflow, Grammarly, Normal Security, Sentinel One, Galileo, Surge AI, Augment Code. We run all their content, newsletters, A to Z with expert review.

**Marcel Santilli:** Under the hood, we build an AI coding agent that constructs workflows as code, plus a runtime layer that executes them. We have human interventions at different steps as needed.

**Marcel Santilli:** Human interventions are done by editors. We're building an expert layer that orchestrates where interventions happen, how to evaluate them, and how to learn from them so we can reconfigure the code—the AI workflow.

**Marcel Santilli:** That's what we do. I can walk you through a quick example. The input might be a company name and website, then it goes through multiple processes—all coded as a workflow with a runtime infrastructure. Each step pulls different data: could be an API, a server, different things. In this case, we scrape and prioritize pages from the website to learn from. Then we research, fact-check, enrich sections, and create jobs-to-be-done descriptions.

**Marcel Santilli:** This is all the jobs-to-be-done step. At the very end, you get something back. We have infrastructure running this, plus a Canva-like editor for interactive sessions. This is the content dashboard our delivery teams use daily—a pipeline running the entire end-to-end process: assignment, research, outline, draft, fact-checking. Each piece runs through our AI workflow infrastructure. Over time, the coding agent can rebuild these workflows.

**Marcel Santilli:** Happy to talk through the challenges and infrastructure stack. Right now we have a few hundred active workflows, but we've built thousands. We're running about 1-2 million workflow runs or activities per month. We're using Langchain for traceability. For evals, we haven't found anything great yet—we tried Calto and Promptfu. For infrastructure, we use Render for hosting and Temporal for runtime. That's the high-level overview.

**Konstantin Drozdov:** Cool.

**Konstantin Drozdov:** That's very interesting, Marcel.

**Konstantin Drozdov:** The number one thing that stood out when I checked your website was the integration of human-in-the-loop into the entire process.

**Konstantin Drozdov:** It's a very exciting solution.

**Konstantin Drozdov:** And on our end, I guess, we would be very excited to learn about the AI layer, as it's the one where we see ourselves bringing the most value or planning to bring the most value to the market.

**Konstantin Drozdov:** I'm curious to learn more about your workflows, model setup, and feedback as the creator. What's working well, and what could LLM or inference providers improve to make your customers' lives better?

**Marcel Santilli:** We've built custom failovers and fallbacks to swap and test models quickly. Since everything is code, we can swap entire workflows when new model versions come out. We mostly use Claude 3.5 Sonnet. We definitely want to invest in fine-tuning—our workflow outputs have human feedback loops, and final output is validated with multiple layers of feedback. We could replace steps or fine-tune smaller models. There's appetite for that, but no massive pain points yet since it's internal. When we go public, in months not years, we'll need alternatives beyond frontier models. We'll use frontier models selectively and shift to open-source and task-specific fine-tuned models for the proven workflows.

**Konstantin Drozdov:** Okay, super clear.

**Konstantin Drozdov:** Mashrur, before I give you a chance to ask a question, I have one more, Marcel.

**Konstantin Drozdov:** I saw you advertise that each customer gets a unique, fine-tuned version of your solution. How do you achieve this?

**Marcel Santilli:** Each customer gets a custom strategy. There are different contexts—company description, product info, personas—which we call "artifacts." Our workflows pull different artifacts and different inputs.

**Marcel Santilli:** In some cases, we build fully custom workflows. For example, a healthcare customer's CMO is a holistic doctor with an endocrinology background. We created an expert-in-the-loop workflow to replicate her expertise and make her review steps easier.


**Marcel Santilli:** We collect feedback and comments, then ask: can we add another workflow step—20, 30, or 40 steps—to get quality closer to 95% instead of 98%? That way, her review comments improve.

**Marcel Santilli:** So we're not fine-tuning models today.

**Marcel Santilli:** We refresh artifacts, tweak inputs, give custom instructions, or build custom workflow steps.

**Konstantin Drozdov:** And since this is kind of, in a sense, not real-time inference, or this real-time inference is not really affecting the end user, since you have these layers of experts and managers working with the solution, this is the reason why you kind of didn't explore a fuller automation of the whole pipeline, where you can use different tuned models to just eliminate the instances where you have to ask experts for validation and can rely more and more on the model outputs.

**Marcel Santilli:** There's a lot changing too quickly to do customer-specific fine-tuned models right now. Even in steady state, topics change constantly and there are too many variables. Over time though, we could fine-tune on specific steps. For instance, the planner step—taking research and generating outlines—we have thousands of validated examples. We definitely have appetite for that, but haven't invested heavily yet. We're a company less than a year old, so we're focused on keeping up with demand. That's where we see the most value right now.

**Konstantin Drozdov:** Okay.

**Konstantin Drozdov:** Yeah, super clear.

**Konstantin Drozdov:** Mashrur, it's your chance.

**Mashrur Haider:** Marcel, thank you for the overview. What you're doing is interesting because you're generating data that gives you competitive advantage.

**Mashrur Haider:** The planning step is very difficult. If you can fine-tune or apply reinforcement learning to promote planning ability, that would be powerful. I was going to ask about retaining data for training, but you already answered that.

**Marcel Santilli:** There's no proprietary data. Even artifacts we generate are based on publicly available data—no CRM data or anything like that. We process public data in a unique way, and the output is marketing content that goes on their sites, integration pages, developer docs—all public anyway.

**Mashrur Haider:** Is planning done by humans, or does a model generate the plan first then humans verify?

**Marcel Santilli:** The planning is based on expert processes. Like me as a process architect, I think through how I'd write a thought leadership or technical article—start with the topic, research, gather info, outline the flow.

**Marcel Santilli:** Workflows are based on experts with 10-20 years of experience. We replicate their expert process—the "messy middle"—and distill it into reproducible blueprint code. We test, tweak, and polish with feedback. Processes evolve over time. V1 works, then as customers use it, editors identify failure modes and we fix them by tweaking artifacts, changing inputs or steps, or creating new versions.

**Mashrur Haider:** The workflow evolves as you go. Are you using Claude for the whole process, or different models for different stages?

**Marcel Santilli:** We use almost every model for different tasks. For research, Perplexity mostly, and a few others for specific deep research.

**Marcel Santilli:** Parallelization makes a huge difference for these steps.

**Marcel Santilli:** We're not compute cost-sensitive because customers pay $10-60k/month, so spending a couple dollars per output is fine. We're not trying to be ultra-efficient or chase low latency yet. That's one benefit of being an internal platform.


**Roman Chernin:** Can we consider most workloads asynchronous? Do you need real-time response?

**Marcel Santilli:** It's mostly batch processing, except for some chat features. We have a Canva-like AI editor where you can pull artifacts. For those, some latency is okay, but not too much. Over time, if we can speed up, we can enable more real-time. Right now it's batch—most processes take 1-2 minutes, sometimes up to 3 minutes since they're in-depth.

**Roman Chernin:** Have you thought about running pipelines in parallel with a judge system to pick the best output?

**Marcel Santilli:** Many workflows are already parallelized. Our deep researcher takes a topic, breaks it into questions based on company context and persona, runs deep research on each, then aggregates. That takes about 2 minutes. Perplexity deep research is slow, so there's a bottleneck. In the future, we could run multiple iterations and workflows, then have a human or system choose the best output instead of trying to optimize a single path.

**Roman Chernin:** You can have a system, not just a human, make the choice. We've done research on building agentic systems. When you have a weaker model with multiple runs and a trained judge, the weak model plus judge can outperform a stronger model. We explored this because we wanted open-source systems to compete with expensive frontier models. Can you do more runs of a weaker model on equal compute and have a judge pick the best?

**Marcel Santilli:** We'd be super interested in that to accelerate our process. We know we need to do it and it will reduce frontier model dependency. Right now we're iterating so much that frontier models are the shortcut.

**Roman Chernin:** Yeah, yeah, that's obviously the right way to go.

**Marcel Santilli:** That's exactly what we want to do—mixture of experts with a judge system, but not just an LLM judge—a workflow as judge.

**Roman Chernin:** Right, the workflow.

**Marcel Santilli:** Plus evaluations, plus human reinforcement learning, plus evaluation of human feedback.

**Roman Chernin:** So you could start building that now.

**Marcel Santilli:** Yeah, we have some of that, but I have to run.

**Roman Chernin:** This has been super helpful, thank you. It was exciting to talk with you. Let's stay in touch, especially when you shift from exploring to optimizing and moving to open-source.

**Marcel Santilli:** Thanks so much. That sounds great. I appreciate this meeting and I'll dig deeper into AI Studio. Let's stay in touch.

**Roman Chernin:** Thank you, Marcel. Take care.

**Marcel Santilli:** Cheers.
