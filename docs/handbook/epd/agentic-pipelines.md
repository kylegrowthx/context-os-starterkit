<metadata>
purpose: The 5-step process for building, testing, and rolling out client AI pipelines.
source: https://handbook.growthx.ai/epd/agentic-pipelines
sync_type: auto
access: build-team
last_synced: 2026-03-02
</metadata>

# Agentic pipelines

This is the process for creating and deploying agentic pipelines for clients. The goal: build as many rules and guidelines into context artifacts and prompts as possible so the delivery team gets high-quality output with minimal rework.

<Info>
See also [Prompting fundamentals](/guides/ai/prompting-fundamentals) for the basics and [Prompt design fundamentals](/guides/ai/prompt-design-fundamentals) for advanced techniques like chain-of-thought, few-shot examples, and building production prompts.
</Info>

## Video tutorial

[Editing pipelines with cloud code: a step-by-step guide](https://www.loom.com/share/e9eddce4282349cf94f316b23f02d9ec)

## The 5-step process

<Steps>
  <Step title="Gain context">
    **Why:** You need to understand what "great" looks like to the client so you can bake rules and guidelines into context artifacts and prompts — reducing reopened tickets and downstream issues.

    **How:**
    1. Read through delivery team feedback on the pipeline for the specific customer
    2. Review strategy deep dives as needed
    3. Request top-performing articles or review analytics
    4. Request past articles that performed badly
    5. Pull topics from ContentOS or ask the content manager for upcoming topics
  </Step>
  <Step title="Create and edit context artifacts">
    **Why:** Some context artifacts are too long or contain instructions the agents can't execute, leading to poor output quality.

    <Warning>
    The context generator can sometimes remove important instructions from old artifacts or fabricate personas. Review generated artifacts carefully — you may want to skip the generator and edit manually until these issues are resolved.
    </Warning>

    **How:**
    1. Use the context generator
    2. Thoroughly review and edit the generated context artifacts
  </Step>
  <Step title="Build the pipeline">
    1. Copy from existing templates on the tech blog
    2. Update the pipeline as needed — add missing inputs, workflows, and configuration
  </Step>
  <Step title="Test">
    **Why:** Test as much as possible so the delivery team makes as few edits as possible and the client is thrilled with quality.

    **How:**
    1. Run the article pipeline for a topic that was run in the old pipeline. Test against known issues and writing guidelines. Compare output against the old pipeline.
       - If there are critical errors (there always are), update artifacts or prompts as needed
       - Repeat until critical issues are fixed and verified
    2. Review the article for readability, check that links contain cited statistics/sources, and check for other issues
    3. Run new topics and repeat as needed
    4. Ask for clarification or information from the content manager as needed
  </Step>
  <Step title="Review and sign-off">
    **Why:** Get sign-off from the delivery team to confirm they've tested the pipeline and don't see issues — so you don't get new tickets in the following weeks.

    **How:**
    1. Ping delivery owners and ask them to review pipeline output
    2. After review, close the ticket as done
  </Step>
</Steps>
