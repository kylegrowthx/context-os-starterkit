# Agent Docs

Task-specific configurations that tell AI agents exactly which context files to load for different types of work.

## How It Works

When an AI agent receives a task, it checks `CLAUDE.md` for the task routing table, then loads the appropriate agent config from this directory. Each config specifies:
- **Required context** — files that must be loaded for every task of this type
- **Conditional context** — files loaded based on specific sub-tasks
- **Role recommendations** — which `context/roles/` personas to activate

## When to Load

Load the agent config that matches your task type before doing any work. Only one config should be active at a time.

## Files

| File | When to Use |
|------|------------|
| `client-work-agent.md` | Creating deliverables, materials, or strategies for client accounts |
| `writing-agent.md` | Writing blog posts, newsletters, thought leadership, product copy |
| `research-agent.md` | Researching topics, creating study guides, deep dives |
| `decision-agent.md` | Strategic decisions, analysis, multi-perspective evaluation |
| `onboarding-agent.md` | Answering questions from new team members about GrowthX |
| `context-engineering-guide.md` | Writing or editing files designed for AI agent consumption |
