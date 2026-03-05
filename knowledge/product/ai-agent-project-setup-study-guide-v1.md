# Setting Up a Repo for AI Coding Agents: Study Guide

> **For:** Non-developers who want to build fast and with quality using Claude Code and Cursor
> **Goal:** Configure a Next.js + React + shadcn project so AI agents write production-quality frontend code on the first pass
> **Stack:** Next.js 16 (App Router), React 19, TypeScript, Tailwind CSS 4, shadcn/ui, Clerk, Recharts
> **Time Investment:** 4-6 hours for initial setup, ongoing refinement
> **Last Updated:** 2026-03-04

<metadata>
purpose: Study guide for setting up AI-agent-optimized repos
audience: Non-developers building with Claude Code and Cursor
related: context/roles/cto-v1.md
domain: product
confidence: high
access: company
last_updated: 2026-03-04
</metadata>

---

## How to Use This Guide

Read Part 1 first. It explains why this matters and changes how you think about AI coding. Then work through Parts 2-5 in order. Each part builds on the previous one. Part 6 is your reference shelf for ongoing learning.

The core idea: AI coding agents are only as good as the context you give them. "Context engineering" is the term for this. Martin Fowler's team at Thoughtworks calls it "the foundation of AI-enabled development." Addy Osmani (engineering lead at Google) says specs are "the critical interface between humans and AI agents." Every reputable engineer building with these tools says the same thing: the quality of your setup determines the quality of your output.

This is not about learning to code. It's about learning to direct agents that code for you.

---

## Part 1: Foundations

### What is context engineering?

Context engineering is how you structure information so AI agents produce better code. Martin Fowler's team published the definitive primer: "Almost all forms of AI coding context engineering ultimately involve a bunch of markdown files with prompts." That's it. Markdown files that tell the agent what your project is, how it works, and what matters.

The agent reads these files before writing a single line of code. The better these files are, the better the code. Testing by the Next.js team showed that agents with no docs produced correct code 53% of the time. Agents with well-structured docs hit 100%. That's the difference between a frustrating experience and a productive one.

### The two tools and how they overlap

**Claude Code** runs in your terminal. It reads `CLAUDE.md` files, supports skills, hooks, slash commands, and subagents. It's the more powerful tool for complex tasks because it can execute code, run tests, and manage git.

**Cursor** is a code editor (fork of VS Code) with AI built in. It reads `.mdc` rule files in `.cursor/rules/`. It has Agent mode for complex coding, Tab completion for inline suggestions, and notepads for reusable reference docs.

Both tools read `AGENTS.md` (a cross-tool standard that Next.js helped establish). Both connect to MCP servers for external capabilities. You configure both. They're complementary, not competing.

### The mental model

Think of it as briefing a new developer on their first day. You wouldn't just say "build me a dashboard." You'd show them the codebase, explain the conventions, point to examples of good work, and tell them where the landmines are. That's exactly what you're doing with these configuration files. The difference is you do it once, and the agent reads it every single time.

### Common misconceptions

**"AI agents can figure it out from the code."** They can't. Without explicit rules, agents make inconsistent decisions about naming, file structure, imports, and patterns. They'll use deprecated APIs, mix client and server components randomly, and create files in the wrong places.

**"More instructions = better results."** Wrong. Every word consumes context tokens. The Trail of Bits team (security engineers who use Claude Code daily) found that concise, opinionated rules outperform verbose ones. Their principle: "Clarity over cleverness."

**"Vibe coding means no structure."** Andrej Karpathy coined "vibe coding" to describe building with AI through natural language. But the practitioners who ship quality software with this approach all invest heavily in project setup. The vibe is in the interaction, not the architecture.

---

## Part 2: The Configuration Files

This is the core of the guide. These are the files you create and maintain. Each one serves a different purpose.

### 2.1 CLAUDE.md — Your agent's persistent memory

CLAUDE.md is a file Claude reads at the start of every conversation. In 2026, the community consensus is that it's as essential as .gitignore. Run `/init` in Claude Code to generate a starter, then refine.

**What goes in it:**

Your tech stack and how the project is organized. Build, test, and lint commands. Code style rules. Architecture decisions the agent can't infer. Key patterns and conventions. Things the agent should never do.

**What stays out:**

API keys or credentials. Instructions that only apply to narrow tasks. Anything longer than 100 lines in the root file (use `@import` for details).

**Structure for your stack:**

```markdown
# Project Overview

Next.js 16 App Router project with React 19, TypeScript strict mode,
Tailwind CSS 4, and shadcn/ui components.

## Tech Stack
- Next.js 16 (App Router) — server components by default
- React 19 — use React Server Components, avoid 'use client' unless needed
- TypeScript — strict mode, no `any` types
- Tailwind CSS 4 — utility-first, no custom CSS unless unavoidable
- shadcn/ui — use for all UI components (built on Radix UI primitives)
- Clerk — authentication (use @clerk/nextjs, NOT deprecated withAuth/authMiddleware)
- Recharts — data visualization (always wrap in 'use client' components)

## Commands
- `npm run dev` — start dev server
- `npm run build` — production build
- `npm run lint` — ESLint check
- `npm run type-check` — TypeScript strict check

## Code Style
- Functional components only, no classes
- Named exports for components, default export for pages
- One component per file
- Colocate related files (component + types + tests in same directory)
- Use server components by default. Only add 'use client' for interactivity
- Import shadcn components from @/components/ui/
- Use Tailwind utilities, not inline styles or CSS modules

## File Structure
- app/ — routes and pages (App Router)
- components/ — shared UI components
- components/ui/ — shadcn/ui components
- lib/ — utilities and helpers
- types/ — shared TypeScript types
- public/ — static assets

## Architecture Decisions
- All data fetching in server components or server actions
- Client components only for: forms, interactive charts, auth UI
- Recharts components must be in 'use client' files with ResponsiveContainer
- Clerk middleware in middleware.ts for route protection

## Don't
- Don't use pages/ directory (App Router only)
- Don't use CSS modules or styled-components
- Don't import from @clerk/clerk-react (use @clerk/nextjs)
- Don't create API routes for data that can use server actions
- Don't use default exports except for page.tsx and layout.tsx files
```

**Hierarchy:** You can place CLAUDE.md files at multiple levels. Root-level rules apply everywhere. Child-directory rules apply only when working in that directory. For a monorepo, each package gets its own CLAUDE.md.

**The Trail of Bits principles** worth adopting: "No speculative features." "No premature abstraction." "Replace, don't deprecate." These prevent the kind of over-engineering that agents love to do.

### 2.2 Cursor Rules (.mdc files)

The old `.cursorrules` file is deprecated. Modern Cursor uses `.mdc` files in `.cursor/rules/`. Each file has YAML frontmatter and a markdown body.

**File format:**

```markdown
---
description: Enforce Next.js App Router patterns and server-first architecture
globs: "app/**/*"
alwaysApply: false
---

# Next.js App Router Conventions

- Use server components by default
- Only add 'use client' when component needs interactivity, browser APIs, or React hooks
- Data fetching happens in server components or server actions, never in client components
- Use Next.js Image component for all images
- Use Next.js Link component for all internal navigation
- Dynamic routes use [param] folder naming
- Loading states use loading.tsx files
- Error boundaries use error.tsx files
```

**Rule types:**

| Type | When it fires | Use for |
|------|--------------|---------|
| Always | Every prompt | Core project rules |
| Auto Attached | Files match a glob pattern | Directory-specific patterns |
| Agent Requested | Agent decides to use it | Optional reference material |
| Manual | You explicitly invoke it | Rare workflows |

**Recommended rule files for your stack:**

```
.cursor/rules/
├── project-overview.mdc      (Always — tech stack, structure)
├── nextjs-patterns.mdc       (Auto — app/**)
├── component-standards.mdc   (Auto — components/**)
├── shadcn-usage.mdc          (Agent Requested — UI component patterns)
├── clerk-auth.mdc            (Auto — **/auth/** and middleware.ts)
├── recharts-patterns.mdc     (Auto — **/charts/** or **/dashboard/**)
└── typescript-standards.mdc  (Always — type safety rules)
```

**Key practice:** Add rules only when you notice the agent making the same mistake repeatedly. Start lean. Build up from experience, not from imagination.

### 2.3 AGENTS.md — The cross-tool standard

AGENTS.md is read by Claude Code, Cursor, GitHub Copilot, and other agents automatically. Next.js generates one when you run `create-next-app`. Its purpose is to point agents at bundled documentation instead of relying on training data.

For Next.js projects, the default AGENTS.md tells agents to read docs bundled in `node_modules/next/dist/docs/`. This means agents always use documentation matching your installed version, with no network request needed.

If you use `create-next-app`, you get both AGENTS.md and CLAUDE.md generated automatically. Customize them from there.

### 2.4 MCP Servers — Extending agent capabilities

MCP (Model Context Protocol) connects agents to external tools and data. Configure these in `.cursor/mcp.json` for Cursor or via `/mcp` in Claude Code.

**Essential MCP servers for your stack:**

| Server | What it does | Config |
|--------|-------------|--------|
| **shadcn/ui MCP** | Browse, search, install shadcn components via natural language | [ui.shadcn.com/docs/mcp](https://ui.shadcn.com/docs/mcp) |
| **next-devtools-mcp** | Live build errors, runtime errors, TypeScript errors, route info | [github.com/vercel/next-devtools-mcp](https://github.com/vercel/next-devtools-mcp) |
| **Context7** | Fetches latest version-specific docs for any library | Prevents outdated API usage |
| **Playwright** | Browser automation for testing | E2E test generation |
| **GitHub** | Repo, issue, PR management via natural language | Standard dev workflow |

**Cursor MCP config example (.cursor/mcp.json):**

```json
{
  "mcpServers": {
    "next-devtools": {
      "command": "npx",
      "args": ["-y", "next-devtools-mcp@latest"]
    },
    "shadcn-ui": {
      "command": "npx",
      "args": ["-y", "shadcn-ui-mcp@latest"]
    }
  }
}
```

---

## Part 3: The Workflow

### 3.1 The PRP framework (Product Requirements Prompt)

This is the most important workflow for non-developers. Cole Medin popularized it and it's now widely adopted. The idea: before you ask the agent to build anything, you create a specification document with three parts.

**Part 1: PRD (Product Requirements Document)**
What you're building and why. Written in plain language. Include acceptance criteria: what does "done" look like?

**Part 2: Curated Codebase Intelligence**
Examples of good code from your project. If you want a new dashboard page, point to an existing one that's well-built. Agents perform dramatically better when they can see patterns to follow. Cole Medin's repo stores these in an `examples/` folder.

**Part 3: Agent Runbook**
Step-by-step execution instructions. "First create the route. Then create the page component. Then add the data fetching. Then add the chart. Then run the type checker. Then run the linter." This prevents agents from taking shortcuts.

**Why this works:** You give the agent everything it needs to ship correct code on the first pass. Addy Osmani (Google) calls this "specification-driven development" and argues it produces better results than iterative back-and-forth prompting.

### 3.2 Plan Mode before coding

In Claude Code, press Shift+Tab twice to enter Plan Mode. The agent researches, analyzes, and plans without changing any files. In Cursor, use "Ask" mode before switching to "Agent" mode.

Every reputable source emphasizes this: planning before implementation is non-negotiable. "Vibe coding" works for throwaway MVPs, but anything you want to maintain requires structured thinking first.

### 3.3 Git workflow

Always have the agent create a new branch for each task. This isolates its work and gives you a safety net to discard changes if they go wrong. This is the single most important safety practice.

### 3.4 Session management

Start fresh sessions per task. In Claude Code, use `/clear` between unrelated tasks. Compact proactively at 70% context usage. If you've corrected the agent more than twice on the same issue, clear and start fresh. Context degradation is the primary failure mode.

---

## Part 4: Claude Code Power Features

### 4.1 Skills

Skills are specialized prompt templates that inject domain-specific instructions when activated. They live in `.claude/skills/` (project) or `~/.claude/skills/` (global). Each skill needs a `SKILL.md` file with YAML frontmatter describing when to use it.

The most important concept: **Progressive Disclosure.** Show just enough information to help the agent decide what to do next, then reveal more details as needed. Don't dump everything upfront.

### 4.2 Slash Commands

Store reusable prompts as markdown files in `.claude/commands/`. Name the file after the command. Use `$ARGUMENTS` for variable input. These are powerful for repeatable workflows like "create a new page with the standard layout" or "add a chart component to this page."

Example: `.claude/commands/new-page.md`
```markdown
Create a new page at app/$ARGUMENTS/page.tsx following these conventions:
- Server component by default
- Import layout from components/layouts/
- Add proper TypeScript types
- Include loading.tsx and error.tsx siblings
- Follow existing page patterns in the codebase
```

Then invoke with: `/new-page dashboard/analytics`

### 4.3 Hooks

Hooks are shell commands that fire at specific lifecycle points. They're more reliable than instructions in CLAUDE.md because an instruction can be "forgotten" as context grows, but a hook fires every single time.

Use cases: block dangerous commands (rm -rf), auto-run linters after edits, validate file naming conventions, enforce commit message formats.

### 4.4 Subagents

Delegate complex subtasks to specialized agents. Useful for: research tasks while you continue building, running comprehensive test suites, code review of generated output. The official guidance: simple control loops outperform multi-agent systems. Use subagents selectively.

---

## Part 5: Stack-Specific Setup

### 5.1 Next.js 16 + App Router

Server components are the default. Only add `'use client'` when a component needs interactivity, browser APIs, or React hooks (useState, useEffect, etc.). Data fetching happens in server components or server actions. Route structure follows the app/ directory (no pages/ directory).

The bundled docs system means agents always have version-correct Next.js documentation without network requests.

### 5.2 Tailwind CSS 4

Tailwind v4 simplified installation to a single command: `npm install tailwindcss @tailwindcss/postcss postcss`. Configure in `postcss.config.mjs`. Keep utility classes in JSX. For repeated patterns, abstract with `@apply` in globals.css. Tell the agent to prefer Tailwind utilities over custom CSS in your CLAUDE.md and rules.

### 5.3 shadcn/ui

shadcn/ui is not a traditional component library. Components are copied into your project (typically `components/ui/`) and you own the code. This is good for agents because they can see and modify the source.

**Critical:** Install the shadcn MCP server so agents can browse, search, and install components via natural language instead of guessing at APIs.

**Compatibility note:** shadcn/ui v4 with React 19 may have quirks. Verify during initial setup. Check the shadcn docs for React 19 compatibility notes.

### 5.4 Clerk Authentication

Clerk provides official AI prompts for Cursor rules. Use them. Key rules to enforce:

- Use `@clerk/nextjs`, not `@clerk/clerk-react`
- Never reference deprecated APIs (`withAuth`, `authMiddleware`, `_app.tsx`, `pages/` structure)
- Middleware goes in `middleware.ts` at the project root
- Use `auth()` for server-side authentication in App Router

Add Clerk's official prompts to your `.cursor/rules/clerk-auth.mdc` file. They maintain these to match the current SDK version.

### 5.5 Recharts

Recharts uses browser-only APIs, so every chart component needs `'use client'` at the top. Always wrap charts in `<ResponsiveContainer>` for proper sizing. Tell the agent this in your rules because it will forget otherwise.

Pattern to enforce:
```tsx
'use client'
import { ResponsiveContainer, LineChart, Line, XAxis, YAxis } from 'recharts'

export function RevenueChart({ data }: { data: ChartData[] }) {
  return (
    <ResponsiveContainer width="100%" height={400}>
      <LineChart data={data}>
        {/* chart config */}
      </LineChart>
    </ResponsiveContainer>
  )
}
```

### 5.6 TypeScript Strict Mode

This is the single most impactful quality tool for non-developers. TypeScript's type checker catches bugs that would otherwise reach production. Enable strict mode in `tsconfig.json` and tell the agent: no `any` types, no type assertions without justification.

---

## Part 6: Quality Guardrails

### The non-developer's testing stack

You don't need to write tests manually. But you need the agent to write them and you need them to run automatically.

1. **TypeScript strict mode** — catches type errors at build time
2. **ESLint** — catches code quality issues. Enable "Iterate on lints" in Cursor so it auto-fixes
3. **Pre-commit hooks** (via Husky + lint-staged) — run type-check and lint before every commit
4. **Build check** — `npm run build` catches server/client boundary issues
5. **Playwright** (optional) — E2E tests for critical user flows

Tell the agent to run `npm run build && npm run lint && npm run type-check` after completing any feature. If any fail, it fixes them before declaring done.

---

## Appendix A: Curated Source Library

### Official Documentation (Read These First)
- [Claude Code Best Practices](https://code.claude.com/docs/en/best-practices) — Anthropic's official guide
- [Cursor Rules Docs](https://cursor.com/docs/context/rules) — How .mdc files work
- [Cursor Agent Best Practices](https://cursor.com/blog/agent-best-practices) — Official agent workflow guide
- [Next.js AI Agents Guide](https://nextjs.org/docs/app/guides/ai-agents) — AGENTS.md and bundled docs
- [shadcn/ui MCP Server](https://ui.shadcn.com/docs/mcp) — AI integration for shadcn
- [Clerk AI Prompts for Next.js](https://clerk.com/docs/ai-prompts/nextjs) — Official Clerk rules for agents

### Expert Articles (Deep Understanding)
- [Context Engineering for Coding Agents](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html) — Martin Fowler / Birgitta Böckeler. The definitive primer.
- [How to Write a Good Spec for AI Agents](https://addyosmani.com/blog/good-spec/) — Addy Osmani. Specification-driven development.
- [Using CLAUDE.md Files](https://claude.com/blog/using-claude-md-files) — Anthropic's official guide to CLAUDE.md.
- [The Perfect Cursor AI Setup for React and Next.js](https://www.builder.io/blog/cursor-ai-tips-react-nextjs) — Builder.io. Practical setup walkthrough.
- [How I Use Claude Code](https://www.builder.io/blog/claude-code) — Builder.io. Real workflow patterns.
- [How I Use Every Claude Code Feature](https://blog.sshh.io/p/how-i-use-every-claude-code-feature) — Shrivu Shankar. Comprehensive feature walkthrough.

### Practitioner Repos (Copy and Adapt)
- [Trail of Bits Claude Code Config](https://github.com/trailofbits/claude-code-config) — Opinionated defaults from security engineers. Excellent CLAUDE.md template.
- [Cole Medin Context Engineering Intro](https://github.com/coleam00/context-engineering-intro) — PRP framework, examples folder pattern, full Claude Code guide.
- [awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) — Curated .cursorrules and .mdc examples for many stacks.
- [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) — Curated skills, hooks, commands, and plugins.
- [Chris Wiles Claude Code Showcase](https://github.com/ChrisWiles/claude-code-showcase) — Full project config example with hooks, skills, agents, commands.

### Guides and Tutorials
- [Claude Code Customization Guide](https://alexop.dev/posts/claude-code-customization-guide-claudemd-skills-subagents/) — alexop.dev. CLAUDE.md, skills, and subagents explained.
- [Writing a Good CLAUDE.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md) — HumanLayer. What to include, what to cut.
- [Cursor AI Complete Guide 2025](https://medium.com/@hilalkara.dev/cursor-ai-complete-guide-2025-real-experiences-pro-tips-mcps-rules-context-engineering-6de1a776a8af) — Comprehensive Cursor setup and workflow.
- [Skill Authoring Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) — Anthropic. How to write good skills.

---

## Appendix B: Project Scaffold Checklist

Use this checklist when setting up a new project:

**Foundation:**
- [ ] Run `npx create-next-app@latest` with TypeScript, ESLint, App Router, Tailwind CSS
- [ ] Verify AGENTS.md and CLAUDE.md were generated
- [ ] Enable TypeScript strict mode in tsconfig.json
- [ ] Install shadcn/ui: `npx shadcn@latest init`
- [ ] Install Clerk: `npm install @clerk/nextjs`
- [ ] Install Recharts: `npm install recharts`

**Agent Configuration:**
- [ ] Customize CLAUDE.md with stack details, commands, and conventions (see template in Part 2.1)
- [ ] Create `.cursor/rules/` directory with initial rule files
- [ ] Add Clerk's official AI prompts to `.cursor/rules/clerk-auth.mdc`
- [ ] Configure `.cursor/mcp.json` with shadcn and next-devtools MCP servers
- [ ] Create `examples/` directory with reference components (minimum: one page, one form, one chart)

**Quality Guardrails:**
- [ ] Install Husky + lint-staged for pre-commit hooks
- [ ] Configure ESLint with Next.js recommended rules
- [ ] Add build + lint + type-check script to package.json
- [ ] Initialize git repo, set up main branch protection

**Workflow:**
- [ ] Create `.claude/commands/` with common slash commands (new-page, new-component)
- [ ] Create PRPs/ directory for feature specifications
- [ ] Set up initial git branch strategy (main → feature branches)

---

## Appendix C: Learning Path

### Week 1: Setup and Foundations
1. Read Martin Fowler's context engineering article (30 min)
2. Read Addy Osmani's spec writing guide (20 min)
3. Run through the Project Scaffold Checklist above
4. Build one simple page to test the setup

### Week 2: Workflow Mastery
1. Study Cole Medin's PRP framework and create your first PRP
2. Read the Builder.io Cursor setup guide
3. Practice Plan Mode → Agent Mode workflow on 3 small features
4. Study the Trail of Bits CLAUDE.md template and adapt it

### Week 3: Power Features
1. Create 3 slash commands for your most common tasks
2. Set up 2-3 MCP servers (shadcn, next-devtools, Context7)
3. Write your first skill for a repeatable workflow
4. Read the Claude Code hooks guide and add one protective hook

### Week 4: Quality and Iteration
1. Review all generated code with `npm run build && npm run lint`
2. Refine your CLAUDE.md based on repeated agent mistakes
3. Add rules to `.cursor/rules/` for any recurring issues
4. Update your examples/ directory with best outputs so far

### Ongoing
- Every time the agent makes a mistake you've seen before, add a rule
- Every time you repeat the same prompt, create a slash command
- Every time you write a good PRP, save it as a template
- Review and trim your CLAUDE.md monthly (keep it under 100 lines)
