---
name: research-to-study-guide
description: Deep research on any topic, with option for raw research only or full study guide. Use when the user asks to research a topic, create a study guide, learn about something, or needs to become an expert in an area. Triggers on keywords like "research", "study guide", "learn about", "deep dive", "become expert", "master", "understand".
---

# Research to Study Guide

Deep research on any topic, with the option for raw research only or a full study guide. Always load `agent-docs/research-agent.md` before starting.

## Inputs / Outputs

| | What | Path |
|---|---|---|
| **Input** | Topic, depth choice, and learner profile from user | Conversational |
| **Raw research** | Research findings (always produced) | `pipeline/research/[topic]-research-v1.md` |
| **Working draft** | Synthesis scratchpad (full mode only) | `pipeline/scratchpad/[topic]-research-scratchpad.md` |
| **Final output** | Finished study guide (full mode only) | `knowledge/[subdirectory]/[topic]-study-guide-v1.md` |
| **Prompts** | Full prompt templates for this workflow | `prompts/` subdirectory in this skill |

## Phase 0: Clarify Scope

Before doing any research, ask the user:

1. **What's the topic and goal?** What do they want to learn, and why?
2. **What depth?**
   - **Raw research only** — gather findings, save to `pipeline/research/`, stop there
   - **Full study guide** — raw research → scratchpad synthesis → finished study guide in `knowledge/`
3. **Who's the audience?** Role, experience level, what they'll use it for
4. **Any constraints?** Sources to include/exclude, time sensitivity, specific angles

### Audience Analysis (Do This First)

Before ANY research, answer:

| Question | Answer |
|----------|--------|
| WHO is learning this? | |
| WHAT do they care about vs noise? | |
| WHY do they need this? | |
| WHAT sources would they trust? | |
| WHAT should be excluded? | |

## Phase 1: Research Plan (Get Approval)

Create 3-5 questions per category:

### Required Categories

1. **Foundations** (Critical)
   - What is [topic] and why does it matter?
   - Core concepts and vocabulary
   - Mental models experts use
   - Common misconceptions

2. **Frameworks & Models** (Critical)
   - Established frameworks
   - Processes practitioners follow
   - Templates and tools

3. **Key Practitioners** (High)
   - Recognized experts
   - Their key contributions
   - Where experts agree/disagree

4. **Source Discovery** (High)
   - Essential books
   - Blogs/newsletters
   - Podcasts and videos
   - Courses

5. **Real Examples** (High)
   - Best documented examples
   - Instructive failures
   - Before/after transformations

6. **Skills & Practice** (Medium)
   - Skills that distinguish great practitioners
   - What to practice
   - Learning sequence

### Present Plan and Get Approval

Show the user:
- The research questions organized by category
- Where output files will be saved
- Estimated scope

**Wait for explicit user approval before proceeding.**

## Phase 2: Execute Research

Use web search to answer each question. For each:

```markdown
## Q[N]: [Question]

### Findings
[What you discovered]

### Sources
| Source | Type | Quality (1-5) | Notes |
|--------|------|---------------|-------|

### Gaps
[What's missing]
```

### Source Quality Rubric

| Score | Criteria |
|-------|----------|
| 5 | Authoritative expert, unique insights, practical |
| 4 | Respected source, solid content, actionable |
| 3 | Decent coverage, some value |
| 2 | Surface-level, generic, or dated |
| 1 | Low quality, unsupported claims |

Save all raw research to `pipeline/research/[topic]-research-v1.md`.

**If user chose raw research only: stop here.** Tell the user where to find the file and summarize key findings.

## Phase 3: Synthesize (Full Study Guide Only)

Take raw research from `pipeline/research/` and synthesize into a working draft at `pipeline/scratchpad/[topic]-research-scratchpad.md`.

## Phase 4: Quality Checkpoint (Full Study Guide Only)

Before producing the final study guide, evaluate:

| Metric | Target |
|--------|--------|
| Foundations covered | Yes |
| Frameworks found | 3+ |
| Experts identified | 5+ |
| Sources discovered | 30+ |
| Examples documented | 5+ |

**Quality Bands:**
- **Bad (0-0.4):** Must iterate — critical gaps
- **Acceptable (0.4-0.7):** Can proceed with limitations
- **Great (0.7-1.0):** Proceed to final output

If gaps exist, generate follow-up questions and iterate (max 3 times).

## Phase 5: Produce Study Guide (Full Study Guide Only)

Create study guide at `knowledge/[subdirectory]/[topic]-study-guide-v1.md`:

```markdown
# [Topic] Study Guide

> **For:** [Learner profile]
> **Goal:** [What they'll achieve]
> **Time Investment:** [Estimated hours]
> **Last Updated:** [Date]

## How to Use This Guide
[Brief instructions]

## Part 1: Foundations
[Core concepts, mental models, misconceptions]

## Part 2: Frameworks & Process
[Key frameworks with attribution and examples]

## Part 3-4: [Topic-Specific Sections]
[Adapt based on topic]

## Part 5: Skills & Practice
[How to get good]

## Appendix A: Curated Source Library
[Best sources organized by type]

## Appendix B: Templates & Tools
[Ready-to-use resources]

## Appendix C: Learning Path
[Recommended sequence]
```

### Subdirectory Routing

| Subdirectory | When to use | Examples |
|-------------|-------------|---------|
| `content/` | Writing, style, content creation | writing craft, hooks, engagement |
| `building/` | Company ops, leadership, scaling | handbooks, operator frameworks |
| `product/` | Product strategy, engineering, technical topics | product leadership, architecture |
| `domain/` | Industry-specific or specialized knowledge | market research, competitive analysis |

If the topic doesn't clearly fit one subdirectory, ask the user which one to use.

## Anti-Hallucination Rules

1. **NEVER guess URLs** — Only cite verified sources
2. **NEVER invent sources** — No fabricated books, authors, or frameworks
3. **NEVER fake statistics** — Say "not found" if you don't have data
4. **Trust web research** — Don't flag recent info as dubious
5. **Cite everything** — Every claim needs a source

## Example Usage

User: "Research company handbooks for me"

1. Clarify: Raw research or full study guide? Audience?
2. Present research plan with questions → get approval
3. Execute research → save to `/pipeline/research/company-handbooks-research-v1.md`
4. (If full mode) Synthesize → `/pipeline/scratchpad/company-handbooks-research-scratchpad.md`
5. (If full mode) Quality check → produce study guide at `/knowledge/building/company-handbook-study-guide-v1.md`

## Deep Reference

Full prompt template: [research-supervisor-workflow-prompt-v1.md](prompts/research-supervisor-workflow-prompt-v1.md)
