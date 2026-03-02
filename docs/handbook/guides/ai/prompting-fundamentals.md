<metadata>
purpose: How to write effective prompts and use AI tools across every role at GrowthX.
source: https://handbook.growthx.ai/guides/ai/prompting-fundamentals
sync_type: auto
access: build-team
last_synced: 2026-03-02
</metadata>

# Prompting fundamentals

This guide is for everyone — technical, non-technical, or somewhere in between. You'll learn to write clear prompts, use AI for drafting, editing, and brainstorming, choose the right tools, and troubleshoot when you're stuck.

For deeper coverage of prompt structure, techniques like chain-of-thought and few-shot examples, and building production-grade prompts, see our [Prompt design fundamentals](/guides/ai/prompt-design-fundamentals) guide.

Whether you're writing content, building strategies, answering questions, or organizing information — LLMs can help you do it better.

<Tip>
For how we build AI-powered workflows and agentic pipelines at GrowthX, see [Agentic pipelines](/epd/agentic-pipelines).
</Tip>

## ChatGPT vs. Claude

| Tool | Best for | Strengths |
|------|----------|-----------|
| **ChatGPT** | Structure, task breakdown, brainstorming with large context | Follows instructions well, multiple diverse models |
| **Claude** | Creative writing, long documents, ideation, coding | Expressive, better for storytelling and writing quality |

## What is an LLM?

An LLM (Large Language Model) predicts the next word in a sentence based on what came before. It's trained on massive datasets — billions of words from the internet, books, and other sources — using a neural network architecture called a "transformer."

An LLM's knowledge is limited to its training data. To get more accurate and relevant responses, provide additional context, examples, and data in your prompts.

**Why LLMs are transformative:**
- **Intelligent collaborator**: Analyzes complex information, generates creative alternatives, catches blind spots
- **Adapts through interaction**: Refines outputs based on feedback, builds on previous context
- **Performs best with clear guidance**: Needs specific role definition, relevant context, examples, and structured output formats

## Products vs. APIs

When using AI tools, understand the difference between products and their underlying APIs.

<CardGroup cols={2}>
  <Card title="Products (ChatGPT, Claude.ai)" icon="browser">
    Internet access, conversation memory, file upload, plugin integrations.
  </Card>
  <Card title="APIs (raw)" icon="code">
    No memory between calls, no internet access, text-only, needs custom code for features.
  </Card>
</CardGroup>

<Warning>
When using GrowthX workflows, always assume **API-level capabilities**. Workflows don't have web search or database access — they will fabricate information if asked to provide examples or case studies they don't have context for.
</Warning>

## Prompting basics

Good prompts = good results. Three core rules:

1. **Be specific**: Instead of "Help me," say "Summarize this email in 2 bullets for a team meeting."
2. **Give it a role**: "You're an operations manager drafting an SOP."
3. **Set the format**: Ask for tables, bullet points, headlines — whatever you need.

**Template:**

```
Act as a [role]. Write a [format] for [audience] in a [tone] tone. Include [goal or context].
```

<Tip>
You don't need the perfect prompt on the first try. Ask the AI to revise and improve its answer.
</Tip>

### Example: product launch announcement

```
You are the head of product marketing at an AI marketing automation company.
We're launching a new feature that auto-adjusts ad creative based on real-time behavior.

Our audience is growth marketers at DTC brands who care about reducing CAC
and increasing ROAS.

Write a LinkedIn post announcing the feature in a clear, non-technical tone.
Highlight the pain point (ads fatigue fast), the value (real-time personalization),
and the result (higher ROAS, less manual testing).

Use a confident, sharp tone. Start with a bold hook. Format with short paragraphs.
Include a CTA to book a demo.
```

**Why it works:** Sets a role, focuses on audience and tone, includes specific structure and format instructions.

## Intermediate techniques

### Chain-of-thought prompting

Ask the LLM to break a task into steps:

```
Help me plan a user interview study. First, list goals and think step by step.
Then, write 5 questions. Then, draft a recruitment message.
```

### Voice matching

Get the AI to mimic a brand or person's voice:

```
Rewrite this blog post to sound like [well-known writer].
```

<Note>
This works best for people with substantial public writing. Otherwise, provide voice samples directly in your prompt.
</Note>

### Translation and reformatting

Convert between formats, tones, or styles:

```
Turn this product description into a tweet thread.
```

## Advanced use cases

### Marketing

<AccordionGroup>
  <Accordion title="Beginner → Advanced → Expert prompts">
    **Beginner:**
    > Write three ad variations for new pet owners: one funny, one sentimental, one direct.

    **Advanced:**
    > You are a copywriter at a DTC pet brand. Write three 50-word ad variations for new pet owners: one funny (light sarcasm), one sentimental (emotional pull), and one direct (value-first). Use a clear call to action at the end of each.

    **Expert:**
    > You're a senior copywriter for a premium pet wellness brand. Write 3 ad variations targeting new dog owners (millennial parents) on Instagram. (1) Funny: playful and snarky, (2) Sentimental: nostalgic, emotional, (3) Direct: results-oriented. Each should include: a scroll-stopping hook, 2-line body, CTA, and hashtags.
  </Accordion>
</AccordionGroup>

### Sales

<AccordionGroup>
  <Accordion title="Beginner → Advanced → Expert prompts">
    **Beginner:**
    > Roleplay as a skeptical prospect. I'll respond and you push back.

    **Advanced:**
    > Act as a skeptical marketing ops lead at a mid-market SaaS company. I'll introduce our AI lead scoring product, and you challenge me with tough objections around integration, pricing, and data accuracy. Stay in character for three rounds.

    **Expert:**
    > You are a skeptical buyer at a B2B SaaS company with a history of overhyped AI tools. We're selling an intent-based lead scoring product. You care about integration with HubSpot, measurable ROI within 90 days, and clarity on how the AI works. I'll pitch you. Your job is to ask probing, high-friction questions that expose weak spots.
  </Accordion>
</AccordionGroup>

### Ops

<AccordionGroup>
  <Accordion title="Beginner → Advanced → Expert prompts">
    **Beginner:**
    > Create an onboarding checklist for a new client based on this task list.

    **Advanced:**
    > Here is a task list [paste]. Create a structured onboarding checklist grouped by phase: Pre-Kickoff, Week 1, and Week 2. Include internal and client-facing tasks, and flag items requiring sign-off or dependencies.

    **Expert:**
    > You are an operations lead at a marketing agency onboarding a new eComm client. Based on this task list [paste], build a 3-phase onboarding checklist: (1) Internal prep, (2) Client kickoff, (3) Week 1 execution. Each phase should include: task owner, due date suggestion, internal vs. client-facing label, and blockers to flag. Format as a table.
  </Accordion>
</AccordionGroup>

### Product

<AccordionGroup>
  <Accordion title="Beginner → Advanced → Expert prompts">
    **Beginner:**
    > Suggest edge-case tests for a feature that lets users upload images and tag friends.

    **Advanced:**
    > Generate a list of 10 edge case tests for an image upload feature with tagging. Include scenarios involving unsupported file types, slow connections, duplicate tags, and mobile interruptions.

    **Expert:**
    > You are a QA lead working on a feature that allows users to upload images and tag friends in a social app. Generate a test matrix of edge cases across these categories: file size, format support, concurrent uploads, tagging errors, permission conflicts, mobile vs. desktop. For each, include: test name, risk level (low/med/high), and expected behavior if the test fails.
  </Accordion>
</AccordionGroup>

## When you're stuck

### Output is just "okay" despite good context

<AccordionGroup>
  <Accordion title="Prompts to improve output quality">
    **Beginner:** Ask the AI what a more effective prompt would be given the context you've provided.

    **Advanced:** Ask it to create a reusable prompt that includes tone, audience, and article structure based on the brand guidelines, call notes, and content samples you've uploaded.

    **Expert:** Ask it to act as a senior AI strategist and write a prompt that will generate a full draft — specifying audience, tone, format, and brand-specific voice cues in a reusable format.
  </Accordion>
</AccordionGroup>

### Getting repetitive or overly safe responses

<AccordionGroup>
  <Accordion title="Prompts to break out of safe mode">
    **Beginner:** Ask for 3 versions — one safe, one bold, one surprising.

    **Advanced:** Ask for the same paragraph in 3 styles: polished/safe, emotional/story-driven, and edgy/opinionated.

    **Expert:** Ask for variations with rationale and best-use channel (web, email, social) for each.
  </Accordion>
</AccordionGroup>

### AI misunderstands the task

<AccordionGroup>
  <Accordion title="Prompts to realign understanding">
    **Beginner:** Ask it to explain what it thinks you're asking before it writes.

    **Advanced:** Ask it to summarize its understanding in one sentence and explain its approach.

    **Expert:** Ask it to interpret your task, explain its reasoning for format and tone, list its assumptions, and surface questions it would ask before proceeding.
  </Accordion>
</AccordionGroup>

## Know the limits

- LLMs can hallucinate — always verify facts
- Don't share sensitive data unless in a secure setup
- Outputs may carry bias — stay critical
- AI is a brainstorming partner, not a decision-maker

## Helpful tools

- **Voice input**: Dictate ideas and ask AI to clean them up
- **Custom GPTs**: Create internal tools based on your docs and templates
- **Chrome extensions**: Right-click to send text to ChatGPT
- **Prompt libraries**: Keep a shared doc of your favorite prompts
