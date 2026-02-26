# Cursor for Knowledge Work: A Study Guide

<metadata>
purpose: Study guide on using Cursor AI for non-technical knowledge work
audience: Non-technical knowledge workers, content creators, operators
related: ../../docs/start-here.md, ../../context/voice/writing-style-context-v2.md
domain: tools, productivity
confidence: research-based
sensitivity: internal
context_tier: 2
last_updated: 2026-02-19
</metadata>

---

## Why This Guide Exists

Cursor is an AI-first code editor built on VS Code. It was designed for developers. But the principles underneath it (context engineering, rules, agent workflows, MCP integrations) apply to anyone doing complex knowledge work: writing, research, project management, content strategy.

This guide strips away the developer jargon and explains how to use Cursor's most powerful features for non-technical work. Think of it as a translation layer between "AI coding tool" and "AI thinking tool."

The honest caveat: Cursor has a learning curve. It looks like a code editor because it is one. If you've never touched VS Code, expect a ramp-up period. The payoff is an AI workspace that remembers your preferences, follows your rules, and connects to your tools.

---

## The Mental Model

Cursor isn't ChatGPT in a text editor. It's closer to a configurable AI workspace where you control three things:

1. **Context** — what the AI knows about your project
2. **Rules** — how the AI should behave
3. **Tools** — what external systems the AI can access

Get these three right and the AI stops feeling like a generic chatbot. It starts feeling like a junior teammate who read the handbook.

---

## Part 1: Setting Up Your Project

### Folder Structure

Cursor works on folders (called "workspaces"). Open a folder and everything inside it becomes available to the AI. For knowledge work, your folder might look like this:

```
my-project/
├── .cursor/
│   └── rules/          ← AI instructions live here
├── research/           ← source material
├── drafts/             ← work in progress
├── outputs/            ← finished deliverables
└── README.md           ← project overview
```

The `.cursor/rules/` directory is where the magic happens. Every file you put there shapes how the AI thinks about your project.

### The README Matters

Write a `README.md` at the root of your project. Describe what the project is, what you're trying to accomplish, and how files are organized. When you reference `@README.md` in a conversation, the AI instantly understands the lay of the land.

---

## Part 2: Rules — Your AI's Operating Manual

### What Rules Are

Rules are instruction files that tell Cursor's AI how to behave. They replaced the old `.cursorrules` file (now deprecated). In 2026, rules live as individual `.mdc` files inside `.cursor/rules/`.

Think of each `.mdc` file as a page in your AI's employee handbook. One page might cover writing style. Another might cover how to handle research. Another might describe your project's goals.

### Anatomy of an .mdc File

Each file has a header (frontmatter) and a body (instructions):

```
---
description: Writing style rules for all content
globs: drafts/**
alwaysApply: false
---

## Voice
Write like a smart friend explaining something important.
Be direct. No jargon. No filler.

## Structure
Lead with the point. Break ideas into pieces. Connect them. Summarize.

## Avoid
- Corporate speak (leverage, synergize, circle back)
- Passive voice when active works
- Filler phrases (it's important to note, at the end of the day)
```

The three frontmatter fields:

- **description**: What this rule does and when it should activate. Write it in plain English.
- **globs**: File patterns that trigger the rule. `drafts/**` means "apply this when working on anything in the drafts folder." Use `**/*` for everything.
- **alwaysApply**: Set to `true` if you want this rule active in every conversation, regardless of what files are open.

### Rules That Work for Knowledge Work

Here are starter rules worth creating:

**voice.mdc** — Your writing style. Paste your style guide here or summarize the key principles. The AI will follow them in every draft it produces.

**project-context.mdc** — What this project is about, who the audience is, what success looks like. Set `alwaysApply: true` so the AI always has this context.

**research-standards.mdc** — How to evaluate sources, what counts as credible, how to cite things. Attach to your research folder with `globs: research/**`.

**output-format.mdc** — Templates and formatting standards for deliverables. Attach to your outputs folder.

### Rules Best Practices

Keep each rule under 500 lines. One concern per file. Use specific instructions ("use active voice") rather than vague ones ("write well"). Include examples of what good looks like. Put the most important instructions first — the AI pays more attention to the beginning.

Update rules as you learn what works. They're living documents, not set-and-forget configs.

---

## Part 3: Context Engineering

Context engineering is the skill of giving the AI exactly the right information at the right time. Too little and it guesses. Too much and it gets confused. Here's how to manage it.

### @ Mentions

The `@` symbol is your primary tool for pointing the AI at specific context. Type `@` in any chat and you get options:

- **@filename** — reference a specific file ("read @research/competitor-analysis.md")
- **@folder** — reference an entire directory
- **@Web** — search the internet for current information
- **@Docs** — reference documentation you've indexed
- **@Codebase** — search across your entire project

Use these aggressively. Instead of saying "look at my research," say "@research/competitor-analysis.md — summarize the key findings." Specificity makes the AI dramatically better.

### Notepads

Notepads are reusable context bundles. They're Markdown files that can include text, instructions, and @file references. Create them in Cursor's Notepads panel.

The value: instead of re-explaining your project context in every new chat, create a Notepad called "Project_Brief" and reference it with `@Project_Brief`. One mention loads everything.

Good Notepads for knowledge work:

- **Project_Brief** — goals, audience, constraints, key decisions made so far
- **Style_Guide** — your writing voice and formatting preferences
- **Source_Index** — list of key reference materials with @file links
- **Current_Sprint** — what you're working on this week

Keep Notepads focused. One topic per Notepad. If a Notepad is getting long, split it.

### Session Hygiene

This is the single most overlooked practice: **start new chats for new tasks.**

After a long conversation, the AI accumulates old context that can interfere with new tasks. Cursor shows your context usage in the chat window. When it gets heavy, the AI starts summarizing older context and quality drops.

The rule: new task, new chat. Reference your Notepads and rules to quickly reload relevant context in the fresh session.

---

## Part 4: Agent Mode

Agent mode is where Cursor goes from "AI that responds to prompts" to "AI that executes multi-step tasks." Instead of answering one question at a time, the agent can read files, search your project, write drafts, and iterate.

### The Plan-First Workflow

The biggest mistake people make with agent mode is letting the AI start executing immediately. The proven workflow is:

1. **Research** — let the agent read relevant files and search for context
2. **Clarify** — the agent asks questions before proceeding
3. **Plan** — the agent produces a detailed plan for your approval
4. **Build** — only after you approve the plan does it start producing output

You can enforce this by pressing `Shift+Tab` to enter Plan Mode. In Plan Mode, the agent maps out what it will do before doing it. You review the plan, adjust it, then let it execute.

This saves an enormous amount of rework. Without a plan, the AI guesses at your intent and often gets it wrong. With a plan, you catch misunderstandings before they become wasted drafts.

### Multi-Step Task Example

Say you're writing a research brief. Here's what agent mode looks like:

1. You prompt: "Create a research brief on B2B content marketing trends. Use @research/sources.md for source material. Follow @Style_Guide. Save to drafts/."
2. The agent reads your sources, reads your style guide, and produces a plan: "I'll cover five trends, structure as intro → trend analysis → implications → recommendations. Each trend gets one section with supporting data."
3. You approve (or adjust) the plan.
4. The agent writes the full brief, following your rules and referencing your sources.

### When Agent Mode Struggles

Agent mode works best with clear, bounded tasks. It struggles with ambiguous creative work ("write something interesting about AI"). Give it structure: specific inputs, clear outputs, defined constraints.

If the output quality drops, check your context. Usually the issue is that the agent doesn't have enough information, not that it's incapable. Add more @references or refine your rules.

---

## Part 5: MCP Integrations

MCP (Model Context Protocol) is what lets Cursor talk to external tools. Without MCP, the AI only sees files in your folder. With MCP, it can query databases, search documentation, manage project tools, and more.

### How MCP Works

MCP servers are small programs that connect Cursor to external services. You configure them in a `.cursor/mcp.json` file. When the agent needs external data, it calls the relevant MCP server.

Two connection types:

- **stdio** — runs locally on your machine. Simple to set up. Good for personal tools.
- **SSE** — connects to remote servers over HTTP. Good for team-shared tools and cloud services.

### MCP Servers Worth Knowing

For knowledge work, these are the most useful:

**Notion MCP** — Read and write Notion pages and databases. Query your team's knowledge base from inside Cursor. If your company runs on Notion, this is the first MCP to install.

**Context7** — Fetches current documentation for any library or tool. Instead of relying on the AI's training data (which might be outdated), Context7 pulls the latest docs on demand.

**Knowledge Graph / Memory MCPs** — Give the AI persistent memory across sessions. Tools like Cognee build a knowledge graph from your documents, letting the agent find connections between concepts over time.

**Web Search MCPs** — Let the agent search the internet for current information without you having to copy-paste from a browser.

### Setup Tips

Start with one or two MCP servers. Each server adds to the agent's context window, and too many at once can cause confusion. Add them incrementally as you identify real needs.

Put project-specific MCPs in `.cursor/mcp.json` (at the project root). Put general-purpose MCPs in `~/.cursor/mcp.json` (your global config).

If you're on a team, consider Docker's MCP Gateway. It centralizes MCP servers behind a single proxy, making it easier to manage credentials and share configurations.

---

## Part 6: Model Selection

Cursor lets you switch between AI models. Different models have different strengths. For knowledge work:

- **Claude** — strong at writing, reasoning, and following complex instructions. Best default for content and research tasks.
- **GPT-4o** — good at broad knowledge and conversational tasks.
- **DeepSeek R1** — optimized for logical reasoning and analytical tasks.
- **Cursor's Composer model** — optimized for code execution but useful for structured, multi-step tasks.

The practical advice: use a reasoning-heavy model (Claude or DeepSeek) for planning, then switch to your preferred model for execution. Cursor supports this workflow natively.

---

## Part 7: Daily Workflow

Here's what a productive day in Cursor looks like for knowledge work:

**Morning setup**: Open your project folder. Check your rules are current. Start a fresh chat. Load your `@Project_Brief` notepad.

**Deep work**: Use agent mode with Plan Mode enabled. Reference specific files with @ mentions. Let the agent draft, then review and iterate. Start new chats for new tasks.

**Research**: Use @Web for internet searches. Use MCP integrations for your team's tools (Notion, docs, etc.). Save findings to your research folder.

**End of day**: Review outputs. Update rules if you learned something about what works. Move finished work to your outputs folder.

### Keyboard Shortcuts Worth Memorizing

| Action | Shortcut |
|--------|----------|
| Open chat | Cmd+L (Mac) / Ctrl+L |
| Toggle Plan Mode | Shift+Tab |
| New chat | Cmd+Shift+L |
| Reference file | Type @ then filename |
| Toggle agent mode | Click the model selector |
| Quick actions | Cmd+K (inline editing) |

---

## Part 8: Common Pitfalls

**Pitfall: Treating Cursor like ChatGPT.** Cursor's power comes from project context, rules, and integrations. If you're just typing prompts without any of that, you're getting 20% of the value. Invest the time to set up rules and structure your project.

**Pitfall: Giant context windows.** More context isn't always better. When you dump everything into a conversation, the AI spreads its attention thin. Be surgical with @ references. Point at exactly what matters.

**Pitfall: Never updating rules.** Rules should evolve. When the AI produces something you don't like, ask yourself: "Could a rule have prevented this?" If yes, add or update a rule.

**Pitfall: Long, sprawling chat sessions.** After 20-30 exchanges, start fresh. The AI's quality degrades as context fills up. New task, new chat.

**Pitfall: Skipping Plan Mode.** Letting the agent build without a plan feels faster. It's not. The rework costs more time than the planning saves. Always plan first for anything non-trivial.

---

## Quick-Start Checklist

1. Install Cursor (cursor.com)
2. Open your project folder
3. Create `.cursor/rules/` directory
4. Write your first rule: `project-context.mdc` with `alwaysApply: true`
5. Write a `voice.mdc` rule with your writing preferences
6. Create a Notepad called "Project_Brief" with your goals and constraints
7. Start a chat, reference `@Project_Brief`, and give your first task
8. Use Plan Mode (Shift+Tab) for any multi-step task
9. Add one MCP integration (Notion is a good first choice)
10. Start new chats for new tasks. Keep sessions focused.

---

## Resources

- [Cursor Best Practices (GitHub)](https://github.com/digitalchild/cursor-best-practices) — Community-maintained guide
- [Awesome Cursor Rules (GitHub)](https://github.com/PatrickJS/awesome-cursorrules) — Configuration examples
- [Awesome Cursor Rules MDC (GitHub)](https://github.com/sanjeed5/awesome-cursor-rules-mdc) — Curated .mdc files
- [Cursor Rules Generator](https://cursor.directory/generate) — Auto-generate .mdc files for your project
- [Cursor MCP Server Directory](https://cursor.directory/mcp) — Browse available MCP servers
- [Cursor MCP Setup Guide (2026)](https://claudefa.st/blog/tools/mcp-extensions/cursor-mcp-setup) — Step-by-step MCP configuration
- [Cursor Advanced Tips (2026)](https://eastondev.com/blog/en/posts/dev/20260126-cursor-advanced-tips/) — Power-user techniques
- [Cursor Agent Mode Guide (2026)](https://eastondev.com/blog/en/posts/dev/20260110-cursor-agent-complete-guide/) — Complete agent walkthrough
- [Context Engineering in Cursor](https://stevekinney.com/courses/ai-development/cursor-context) — Deep dive on @ mentions and context
- [Cursor Notepads Guide](https://stevekinney.com/courses/ai-development/cursor-notepads) — Notepad setup and usage
- [Best Cursor Settings 2026](https://mindevix.com/ai-usage-strategy/best-cursor-ai-settings-2026/) — Optimized configuration
- [Cursor AI Review (2026)](https://prismic.io/blog/cursor-ai) — Feature overview and workflow analysis
- [Cursor 2.4 Release Notes](https://theagencyjournal.com/cursors-fresh-2-4-drop-agents-level-up-and-cli-gets-smarter/) — Latest agent capabilities
- [MCP Complete Guide](https://www.honogear.com/en/blog/engineering/mcp-guide) — MCP across Cursor and Claude Code
