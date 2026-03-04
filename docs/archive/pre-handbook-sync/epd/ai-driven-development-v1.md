<metadata>
purpose: Documents AI-native development philosophy, training resources, and the agentic pipeline build process
audience: EPD engineers, new hires
summary: How GrowthX uses AI as a strategic development partner — from planning-phase AI usage to building and deploying client agentic pipelines.
domain: engineering
confidence: canonical
context_tier: 1
last_updated: 2026-02-22
</metadata>

# AI-Driven Development

Our philosophy for using AI as a strategic partner in the development process — not just autocomplete.

## AI-driven vs. AI-assisted vs. vibe coding

We're at an inflection point where we should all strive to be truly AI-native. There's a significant delta in productivity when you learn to use AI not just as a coding assistant, but as a strategic partner early in the process.

For a startup like us, speed is everything. We need to ship the right features before our window closes, and we need code that is as bug-free as possible and somewhat easy to extend and iterate on. There's a difference between a mild productivity boost and a **3–10x multiplier** when it comes to how you use AI in the process.

The key insight: **use AI in the planning phase** — that's where most of the benefits are. Not just autocomplete. The tools have finally caught up to make this workflow easy and expected from everyone.

> **Info:** See also Human-AI collaboration for how we apply these principles in client delivery.

## Training videos

### Intro

- **4 min** — [Quick intro](https://www.loom.com/share/237eafc0ad74452588e89386947518fd)
- **7 min** — [CheckThat product overview + project structure + the feature we'll build](https://www.loom.com/share/3e8c7875cf6d48aebf7448f1b9ae2d02)

### Phase 1: Core UI for context & personas

- **35 min** — [Part 1: Planning](https://www.loom.com/share/34b8d6433d074ba8b8b585e6d24b3743)
- **1 hr** — [Part 2: Finishing the core](https://www.loom.com/share/105f4a4bc2a94152ba287604ad3b1d8b)

### Phase 2: Adding personas to prompts

**CheckThat Rails/React side:**
- **2 min** — [Recap of Phase 1](https://www.loom.com/share/830bc3399da74eb0b05e06ea695ac1a3)
- **40 min** — [Step 1: plan and review changes, then Step 2: execute on the plan](https://www.loom.com/share/51f57d0b37a54b49bbad46ccef212711)

**CheckThat AI workflows:**
- **5 min** — [Rails/React side: create the code to trigger the workflows](https://www.loom.com/share/fe6c2573ba4e48b28001f8ed9e436b84)

**Output/Flow side:**
- **40 min** — [Plan and execute the context generation workflow](https://www.loom.com/share/eb750fb244bf4c2690649c226743cdda)
- **10 min** — [Understanding the basics of debugging with Temporal](https://www.loom.com/share/086eebb629b644d2a758039dd9004904)
- **43 min** — [Plan and execute the personas generation workflow](https://www.loom.com/share/4b7f61720e4544369fcbf5c735d0bc3d)

### Conclusion

- [Takeaways](https://www.loom.com/share/d5e6d93b024c4e03853bcee7256867d9)

## Key takeaways

1. **Use AI in the planning phase** — This is where most of the productivity gains come from, not just autocomplete
2. **AI as strategic partner** — Think of AI as a collaborator who helps you design the solution, not just implement it
3. **3–10x multiplier** — The difference between AI-assisted and AI-driven development is significant
4. **End-to-end workflow** — Plan, review, execute across the full stack (Rails, React, AI workflows)

---

# Agentic Pipelines

The 5-step process for building, testing, and rolling out client AI pipelines.

This is the process for creating and deploying agentic pipelines for clients. The goal: build as many rules and guidelines into context artifacts and prompts as possible so the delivery team gets high-quality output with minimal rework.

> **Info:** See also Prompting fundamentals for the basics and Prompt design fundamentals for advanced techniques like chain-of-thought, few-shot examples, and building production prompts.

## Video tutorial

[Editing pipelines with cloud code: a step-by-step guide](https://www.loom.com/share/e9eddce4282349cf94f316b23f02d9ec)

## The 5-step process

### 1. Gain context

**Why:** You need to understand what "great" looks like to the client so you can bake rules and guidelines into context artifacts and prompts — reducing reopened tickets and downstream issues.

**How:**
1. Read through delivery team feedback on the pipeline for the specific customer
2. Review strategy deep dives as needed
3. Request top-performing articles or review analytics
4. Request past articles that performed badly
5. Pull topics from ContentOS or ask the content manager for upcoming topics

### 2. Create and edit context artifacts

**Why:** Some context artifacts are too long or contain instructions the agents can't execute, leading to poor output quality.

> **Warning:** The context generator can sometimes remove important instructions from old artifacts or fabricate personas. Review generated artifacts carefully — you may want to skip the generator and edit manually until these issues are resolved.

**How:**
1. Use the context generator
2. Thoroughly review and edit the generated context artifacts

### 3. Build the pipeline

1. Copy from existing templates on the tech blog
2. Update the pipeline as needed — add missing inputs, workflows, and configuration

### 4. Test

**Why:** Test as much as possible so the delivery team makes as few edits as possible and the client is thrilled with quality.

**How:**
1. Run the article pipeline for a topic that was run in the old pipeline. Test against known issues and writing guidelines. Compare output against the old pipeline.
   - If there are critical errors (there always are), update artifacts or prompts as needed
   - Repeat until critical issues are fixed and verified
2. Review the article for readability, check that links contain cited statistics/sources, and check for other issues
3. Run new topics and repeat as needed
4. Ask for clarification or information from the content manager as needed

### 5. Review and sign-off

**Why:** Get sign-off from the delivery team to confirm they've tested the pipeline and don't see issues — so you don't get new tickets in the following weeks.

**How:**
1. Ping delivery owners and ask them to review pipeline output
2. After review, close the ticket as done
