# Building an AI Agent Workspace — Study Guide

> **For:** Non-developers who want to understand and replicate an AI-powered knowledge system
> **Goal:** Master the building blocks, mental models, and architecture behind AI agent workspaces like the GrowthX CEO OS
> **Time Investment:** 8-12 hours (comprehensive read + setup)
> **Last Updated:** 2026-03-02

<metadata>
purpose: Teach non-developers how to understand and build AI agent workspaces using Claude Code, Cowork, Cursor, and structured repos
audience: Smart professionals, founders, operators — not engineers
related: building-ai-skills-study-guide-v1.md, ../../CLAUDE.md, ../../context/context-routing.md
domain: product
confidence: current
sensitivity: internal
context_tier: 2
last_updated: 2026-03-02
</metadata>

## How to Use This Guide

This is a concept-first guide. It starts with the mental models you need, then builds up to the practical architecture. You don't need to read it cover to cover. Here's how to navigate:

**"I don't understand any of this yet."** Start at Part 1. Read the whole thing. It's designed to build one concept on top of the last.

**"I get AI chat but not agents or skills."** Jump to Part 2 (the building blocks) and Part 3 (how they connect).

**"I want to build my own version."** Skim Parts 1-3, then focus on Part 4 (the GrowthX blueprint) and Part 5 (how to start from scratch).

**"I just need a reference."** Go straight to the Appendices — the glossary and cheat sheets are there.

---

## Part 1: The Big Picture — Why This Exists

### 1.1 The Problem This Solves

Here's what happens when most people use AI: they open ChatGPT or Claude, type a question, get an answer, and move on. Every new conversation starts from zero. The AI knows nothing about you, your company, your preferences, or your past work. You repeat yourself constantly. You copy-paste context. You explain your writing style for the hundredth time.

This is like having a brilliant assistant who gets amnesia every morning.

The system described in this guide solves that problem. Instead of starting from zero every time, you build a structured knowledge base that the AI reads automatically. It knows your company. It knows your voice. It knows your clients, your processes, your decision-making frameworks. You teach it once, and it remembers.

The GrowthX CEO OS is a working example. It's a folder of markdown files — not code, not a database, not a fancy app — that turns Claude into an AI assistant who understands a specific business deeply. It has 3,200+ files covering everything from company strategy to client meeting transcripts to writing style guides.

### 1.2 The Core Insight: Context Is the Product

The single most important idea in this guide:

**The quality of AI output is determined by the quality of context you give it.**

This is not a technology problem. It's an information architecture problem. The AI model (Claude, GPT, etc.) is the engine. Context is the fuel. Bad fuel, bad output. Good fuel, great output.

Most people focus on the engine — which model is best, what settings to use, how to phrase their prompt perfectly. That matters, but it's 20% of the equation. The other 80% is the context: what information does the AI have access to, how is it organized, and when does it get loaded?

This guide teaches you how to build the fuel system.

### 1.3 Two Mental Models to Hold Onto

Before we go further, two frameworks that will make everything else click:

**Mental Model 1: The Briefing Folder**

Imagine you're hiring a world-class consultant. Before their first day, you prepare a briefing folder. It contains your company overview, org chart, current strategy, key clients, brand guidelines, and recent meeting notes. The better this folder, the faster the consultant becomes useful.

An AI agent workspace is that briefing folder — except the AI reads it in seconds, follows it precisely, and never forgets it.

CLAUDE.md is the table of contents. Skills are the playbooks. Rules are the policies. Records are the filing cabinets. The whole system is a briefing folder designed for a machine reader.

**Mental Model 2: The Layer Cake**

There are four layers to this system, from bottom to top:

```
Layer 4: TOOLS (Claude Code, Cowork, Cursor)
         ↑ These are the hands that do the work
Layer 3: SKILLS & RULES (SKILL.md, .cursorrules)
         ↑ These are the playbooks and policies
Layer 2: CONTEXT (docs, voice guides, roles, records)
         ↑ This is the knowledge the AI draws from
Layer 1: STRUCTURE (folders, CLAUDE.md, INDEX.md, README.md)
         ↑ This is the map that tells the AI where to find things
```

You build from the bottom up. Structure first, then context, then skills, then pick your tools. Most people start at the top (picking a tool) and wonder why it doesn't work. That's like buying a race car before building the road.

---

## Part 2: The Building Blocks — A Glossary That Actually Explains Things

This section defines every concept you need to understand. They're ordered so each one builds on the last.

### 2.1 Models vs. Agents

**A model** is the AI brain. Claude, GPT-4, Gemini — these are models. A model takes text in and produces text out. It's very good at reasoning, writing, and analysis, but it can only work with whatever you put in front of it. It doesn't do anything on its own. It waits for you.

**An agent** is a model with a loop. Instead of just responding once, an agent can: read information, make a plan, take actions (edit files, search the web, call APIs), observe the results, and then decide what to do next. It loops through this cycle until the task is done.

Think of it this way: a model is a person sitting at a desk answering questions. An agent is a person who can get up, walk to the filing cabinet, pull documents, make phone calls, write memos, and come back with a completed project.

Claude (the chatbot) is a model. Claude Code and Cowork are agents built on that model.

### 2.2 Context Window

The context window is the AI's working memory. It's how much information the model can hold in its head at once. Modern models like Claude have a 200,000-token context window — roughly 150,000 words, or about 500 pages of text.

That sounds like a lot, but it fills up fast. Your conversation history, the files being read, the skill instructions, and the system prompts all compete for space. This is why you don't dump everything into the AI at once. You load what's relevant to the current task.

The GrowthX system handles this with tiered loading: the AI always has the 50-line CLAUDE.md overview, loads task-specific files on demand, and only searches through large archives (like 1,944 meeting records) when explicitly needed.

### 2.3 Prompts vs. Context vs. Instructions

People use these words interchangeably, but they mean different things in this world:

**A prompt** is what you type right now. "Write me a LinkedIn post about AEO." It's the immediate request.

**Context** is background information the AI has access to — your company docs, style guides, client records, past work. It's not an instruction; it's knowledge the AI draws from.

**Instructions** are persistent rules that shape how the AI behaves across all interactions. "Always write in active voice." "Never generate financial content without asking." These sit in CLAUDE.md, skills, and rules files.

The key distinction: prompts are ephemeral (one conversation), context is reference material (loaded as needed), and instructions are persistent (always active). A well-built workspace means you write fewer prompts because the context and instructions handle most of the heavy lifting.

### 2.4 CLAUDE.md — The Entry Point

CLAUDE.md is the most important file in the system. It sits at the root of your project and gets loaded into every single conversation. It's the first thing the AI reads.

It does three jobs:

1. **Orients the AI** — "This is a knowledge base for GrowthX, a B2B content marketing agency."
2. **Maps the territory** — "Here's what's in each folder and when to load it."
3. **Sets the rules** — "Don't invent facts. Don't bulk-load records. Flag sensitive content."

Think of CLAUDE.md as the one-page brief you'd give a new hire on their first morning. Not the entire employee handbook — just enough to know what the company does, where to find things, and what not to screw up.

The GrowthX CLAUDE.md is about 90 lines. That's it. It fits in roughly 500 tokens. But it's the navigational backbone that makes 3,200+ other files accessible.

**AGENTS.md** is the same thing, but for Cursor. Both files contain the same information — they exist separately because Claude Code reads CLAUDE.md and Cursor reads AGENTS.md. You keep them in sync.

### 2.5 Skills

A skill is a reusable playbook for a specific task. When you say "research this topic and create a study guide," the AI doesn't figure out the process from scratch each time. It reads a skill file that contains the exact steps, quality criteria, output format, and file paths.

Each skill lives in its own folder with a `SKILL.md` file inside it. The SKILL.md has:

- **A name and description** — what it does and when to trigger it
- **Inputs and outputs** — what goes in, what comes out, where files get saved
- **Step-by-step instructions** — the actual workflow
- **Quality checks** — how to know if the output is good enough
- **Examples** — concrete demonstrations

The GrowthX system has 19 skills, covering everything from "Write a LinkedIn post in our voice" to "Pull a meeting transcript from Fireflies, enrich it, and link it to contact records."

Skills are the highest-leverage thing you can build. Every time you find yourself explaining the same process to the AI, that's a skill waiting to be written. Write it once and reuse it indefinitely — though you'll refine skills over time as your processes evolve, just like you'd update any playbook.

**The key insight:** Skills aren't code. They're written instructions in plain English (markdown). You don't need to be a developer to write a skill. If you can write a clear process document, you can write a skill.

### 2.6 Rules

Rules are persistent behavioral guidelines. Unlike skills (which are invoked for specific tasks), rules apply broadly and automatically.

In Cursor, rules live in `.cursor/rules/` as `.mdc` files. In Claude Code, they're embedded in CLAUDE.md or loaded from dedicated files. Examples from GrowthX:

- **File naming rule:** "All files use lowercase, hyphens, version suffix. Example: `competitor-brief-v1.md`"
- **Contact-transcript linking rule:** "After processing any transcript, update related contact dossiers and cross-link."
- **Skill registry sync rule:** "After creating or deleting a skill, update the skills table in both CLAUDE.md and AGENTS.md."

Rules are guardrails. They prevent the AI from doing things wrong without you having to remember to mention it every time.

### 2.7 MCP (Model Context Protocol) — The Universal Plug

MCP is a standard that lets AI agents connect to external tools and services. Think of it as a USB-C port for AI. Instead of building custom integrations for every combination of AI tool and external service, MCP provides one standard interface.

Through MCP, your AI agent can:
- Read and send emails (Gmail)
- Search and post in Slack
- Query your CRM (HubSpot)
- Read your Notion pages
- Pull data from Google Drive
- Access databases

You don't build MCP servers yourself (usually). They're pre-built connectors. You just turn them on. In Cowork, they appear as plugins. In Claude Code, they're configured in a settings file.

MCP is what turns a knowledgeable AI into a connected AI. Without it, the AI knows things but can't do things in your actual tools.

### 2.8 Repos, Git, and GitHub — Why Version Control for Non-Code

This is the concept that confuses people most. "Why GitHub? We're not writing software."

A repository (repo) is a folder with version history. Every change is tracked, timestamped, and reversible. You can see what changed, when, and why.

GitHub is a website that hosts repos and adds collaboration features (multiple people can work on the same repo, review each other's changes, etc.).

Here's why you use it for a knowledge base:

**Version history.** When you update your company strategy doc, the old version isn't deleted — it's preserved. You can see exactly what changed and when. This matters because the AI reads these files, and you need to know what it's working with.

**Collaboration.** Multiple people can contribute knowledge, review additions, and maintain the system together.

**Portability.** Your knowledge base is a folder of text files. It's not locked into any vendor. Clone it and you have a complete copy that works with any AI tool.

**Plain text is AI-friendly.** Git isn't required for the AI to work — it can read files from any folder. But markdown files in a Git repo happen to be the simplest, most universal format for AI context. No databases to configure, no APIs to build, no conversion needed. Git just adds version tracking on top.

You don't need to know Git commands. Desktop apps like GitHub Desktop or VS Code handle this with buttons and menus. Or you can use the GitHub website directly.

### 2.9 Markdown — The Language of AI Context

Markdown is a simple way to format text using plain characters. A `#` makes a heading. `**bold**` makes bold. `- item` makes a bullet. It's readable by both humans and machines.

Every file in this system is markdown (`.md` extension). Why?

- It's plain text, so it's tiny and fast to process
- The AI understands markdown structure (headings, lists, tables) natively
- It works everywhere — any text editor, any AI tool, any platform
- It's version-control friendly (Git tracks text changes cleanly)

You don't need special software to write markdown. Any text editor works. But tools like Cursor, VS Code, or even Notion (which exports to markdown) make it easier.

### 2.10 The Three Tools: Claude Code, Cowork, and Cursor

These are three different interfaces to AI agents. They all do similar things but for different users and workflows.

**Claude Code** is a terminal tool that works best for people comfortable typing commands. You interact with it in a text-based interface (no buttons or menus). It reads your entire project, edits files, runs scripts, and manages git workflows. Claude Code reads `CLAUDE.md` automatically. It's free to use with a Claude subscription.

**Cowork** is a desktop application that works best for people who prefer visual interfaces. You open the Claude desktop app, grant it access to a folder on your computer, and talk to it in natural language. It can read, create, and edit files, connect to external services through plugins (MCP), and execute multi-step tasks. It requires a paid Claude subscription (Pro at $20/month or higher). Cowork and Claude Code are separate products built on the same AI — they share the same underlying power but offer different interaction styles.

**Cursor** is a standalone code editor (similar to VS Code) that has AI built deeply into the editing experience. You write and edit files in it, and the AI assists you — suggesting changes, executing tasks, navigating your project. Cursor reads `AGENTS.md` and `.cursorrules` automatically. It has "agent mode" where the AI can take multi-step actions autonomously. Cursor costs $20/month.

Anyone can use any of these tools. The "developer vs. non-developer" framing is about comfort, not gatekeeping.

| If you... | Use |
|-----------|-----|
| Are comfortable in a terminal | Claude Code |
| Prefer a visual desktop app | Cowork |
| Work with files in an editor (code or text) | Cursor |
| Want all three (they complement each other) | All of them |

The knowledge base you build works with all three. CLAUDE.md serves Claude Code and Cowork. AGENTS.md serves Cursor. Skills work across both. The context is tool-agnostic.

---

## Part 3: How the Pieces Connect — The Architecture

### 3.1 The Full Picture

Here's how everything fits together in a system like the GrowthX CEO OS:

```
YOU (prompt: "Write a LinkedIn post about AEO")
 │
 ▼
TOOL (Cowork / Claude Code / Cursor)
 │
 ├─ Reads CLAUDE.md → Understands the project, knows where things are
 │
 ├─ Identifies task type → "This is a writing task"
 │
 ├─ Loads skill → growthx-writing/SKILL.md
 │   └─ Skill says: "First read the style guide"
 │
 ├─ Loads context → context/voice/writing-style-context-v2.md
 │   └─ Now knows: direct, clear, real. Like Paul Graham meets Naval.
 │
 ├─ Loads domain knowledge → knowledge/seo-aeo/README.md
 │   └─ Now knows: what AEO is, current research, key concepts
 │
 ├─ Applies rules → "File naming: lowercase-hyphens-v1.md"
 │
 ├─ Drafts output → pipeline/scratchpad/aeo-linkedin-post-draft.md
 │
 ├─ Quality checks → Does it pass the style guide criteria?
 │
 └─ Final output → pipeline/outputs/aeo-linkedin-post-v1.md
```

Notice what happened: you wrote one sentence. The AI did eight things. It navigated a knowledge base, loaded the right context, followed a playbook, applied rules, and produced a formatted output in the right location. That's the leverage.

### 3.2 Tiered Context Loading — Don't Load Everything

The biggest mistake people make is trying to stuff everything into the AI at once. The GrowthX system uses four tiers:

**Tier 0 — Always loaded** (every conversation): CLAUDE.md. About 500 tokens. This is the map.

**Tier 1 — Task-triggered** (when the AI identifies what you're doing): Style guide for writing tasks. Role persona for decision tasks. Relevant skills. 2,000-5,000 tokens.

**Tier 2 — On-demand** (when the AI hits a specific question): Individual study guides, specific docs, research files. 1,000-3,000 tokens per file.

**Tier 3 — Search-only** (never loaded in full, only searched): Meeting transcripts, customer records, downloads. The GrowthX system has 3,200+ files here. The AI searches them with keywords, reads only the matches.

This is context engineering in practice: right information, right time, right amount.

### 3.3 The Pipeline — How Work Flows

Deliverables move through three stages, always forward:

```
pipeline/research/  →  pipeline/scratchpad/  →  pipeline/outputs/
  (raw material)         (working drafts)        (finished work)
```

Research gets collected and organized. Scratchpad holds drafts being refined. Outputs contain polished, deliverable work. Files don't move backward. This is a one-way flow.

This might seem like a trivial detail, but it solves a real problem: without it, drafts and final versions get mixed together, and neither you nor the AI can tell what's done and what's still in progress.

### 3.4 README and INDEX — The Navigation System

Every directory in the system has two files:

**README.md** explains what's in the directory and how to use it. It's the "welcome sign" for both humans and AI agents. When the AI enters a directory, it reads the README first to understand what it's looking at.

**INDEX.md** lists every file in the directory. It's the complete table of contents. When the AI needs to find a specific file, it checks the INDEX.

This is the equivalent of a library having a card catalog (INDEX) and a "how to use this section" guide (README) in every aisle. Without these, the AI wastes tokens reading files that aren't relevant, or misses files that are.

### 3.5 Metadata — Machine-Readable Context About Context

Files in the system use `<metadata>` tags to describe themselves:

```xml
<metadata>
purpose: The definitive GrowthX voice and style guide
audience: All content creators, writers, AI agents
domain: writing
confidence: canonical
sensitivity: internal
last_updated: 2026-02-09
</metadata>
```

This helps the AI make decisions about files without reading the full content. If two files conflict, the one with a more recent `last_updated` wins. If a file is marked `sensitivity: leadership-only`, the AI knows not to include it in client-facing work. If `confidence: aspirational`, the AI knows it's a plan, not a fact.

Think of metadata as the label on a filing cabinet drawer — it tells you what's inside before you open it.

---

## Part 4: The GrowthX Blueprint — A Real Example

### 4.1 What the GrowthX CEO OS Actually Contains

This is a real system running in production. Here's the architecture:

```
growthx-context/                     ← Root folder
├── CLAUDE.md                        ← Entry point for Claude Code / Cowork
├── AGENTS.md                        ← Entry point for Cursor
├── INDEX.md                         ← Global file listing (sitemap)
│
├── docs/                            ← Company handbook (reference)
│   ├── company/                     ← Vision, strategy, values
│   ├── business/                    ← Business model, ICP, pricing
│   ├── delivery/                    ← How client work gets done
│   ├── products/                    ← Product documentation
│   ├── finance/                     ← Fiscal plans, board meetings
│   └── people/                      ← HR, policies, onboarding
│
├── context/                         ← Prescriptive context (how to do things)
│   ├── voice/                       ← Writing style guide
│   ├── roles/                       ← 10 AI executive personas (CFO, CMO, etc.)
│   ├── personal/                    ← User manual, psychological profile
│   └── context-routing.md           ← Master navigation guide
│
├── knowledge/                       ← Study guides and research (45 files)
│   ├── seo-aeo/                     ← SEO + AEO research hub
│   ├── ai/                          ← AI product leadership
│   ├── building/                    ← Leadership, scaling
│   ├── content/                     ← Writing mastery
│   └── product/                     ← Product knowledge (this guide lives here)
│
├── pipeline/                        ← Work in progress
│   ├── research/                    ← Raw material
│   ├── scratchpad/                  ← Working drafts
│   └── outputs/                     ← Finished deliverables
│
├── records/                         ← Archives (3,200+ files, search-only)
│   ├── meetings/                    ← 1,944 meeting records
│   ├── transcripts/                 ← 186 enriched transcripts
│   ├── contacts/                    ← 244 contact dossiers
│   ├── customers/                   ← Client context
│   └── prospects/                   ← Deal research
│
├── .cursor/                         ← Cursor-specific configuration
│   ├── skills/                      ← 19 skill playbooks
│   └── rules/                       ← 5 behavioral rules
│
├── prompts/                         ← Reusable prompt templates
└── sources/                         ← Expert and source indexes
```

### 4.2 The Skill Library

GrowthX has 19 skills. Here are a few that show the range:

**Research to Study Guide** — Takes a topic, runs web research, evaluates source quality, and synthesizes findings into a structured study guide. This is the skill that created the document you're reading right now.

**Contact Dossier** — When you meet someone or process a meeting transcript, this skill creates or updates a structured profile in `/records/contacts/`. It pulls from HubSpot, transcripts, and your notes to build a complete picture.

**GrowthX Writing** — Any time you write content, this skill loads the voice guide and applies quality checks. It ensures everything sounds like "a smart friend explaining something important."

**Pull Meeting** — A master skill that chains three other skills together: pulls a transcript from Fireflies, enriches it (fixes speakers, adds context), and then links it to contact records.

The pattern: each skill encodes a process that would otherwise require you to explain the same steps every time. Write once, use forever.

### 4.3 The Role System

The `context/roles/` directory contains 10 AI executive personas. When you need strategic analysis, you don't just ask Claude to think. You load a specific persona:

- **CFO** — For financial decisions, budget analysis, unit economics
- **CMO** — For marketing strategy, brand positioning, content direction
- **COO** — For operations, process design, team structure
- **CTO** — For technical decisions, architecture, build-vs-buy

Each role file contains: the persona's priorities, how they think about problems, what frameworks they use, and what questions they ask. When the AI loads the CFO role, it thinks about your question through a financial lens — margins, cash flow, ROI — instead of giving generic advice.

This is a force multiplier. One person with 10 AI advisors who understand the business.

### 4.4 How Rules Keep Things Consistent

Five rules run in the background:

1. **Contact-transcript linking** — After any transcript is processed, contacts mentioned in it get their dossiers updated with a link back to the transcript. This builds relationship history automatically.

2. **Skill registry sync** — When you create or delete a skill, both CLAUDE.md and AGENTS.md get updated. Without this rule, the two files drift apart.

3. **Context navigation** — How the AI should navigate the repo (check README first, use INDEX for file listings, never bulk-load records).

4. **File naming** — All files follow `lowercase-hyphen-name-v1.md`. Consistency matters because the AI relies on predictable patterns to find things.

5. **README maintenance** — When files are added or removed, README and INDEX files stay current.

Rules are the invisible infrastructure that keeps the whole system coherent as it grows.

---

## Part 5: Building Your Own — A Starter Map

### 5.0 Practical Setup (Cowork Edition)

If you're using Cowork (the desktop app), here's the literal first-time setup:

1. Open the Claude desktop app (download from claude.ai if you don't have it)
2. Make sure you have a paid subscription (Pro at $20/month minimum)
3. Create a folder on your computer — call it something like `my-workspace`
4. In the Claude desktop app, switch to Cowork mode and select that folder
5. Claude now has access to read and write files in that folder
6. Create a `CLAUDE.md` file in that folder (see below for what to put in it)
7. Start talking to Claude — it will read CLAUDE.md automatically

That's the whole setup. Everything else in this guide is about what to put in that folder and how to organize it.

### 5.0.1 When This System Isn't Worth It

This system has overhead. Creating folders, writing skills, maintaining CLAUDE.md — it takes time. It's not worth it if you're using AI for occasional one-off questions or simple tasks.

It starts paying off when you have repeated work: writing in the same voice weekly, running the same research process for different clients, onboarding new team members who need access to the same knowledge. The more repetition in your work, the higher the return on building a structured workspace.

A good rule of thumb: if you explain the same context to AI more than three times, it's worth structuring.

### 5.1 Start Smaller Than You Think

You don't need 3,200 files to get value. The GrowthX system grew over time. Here's how to start with almost nothing and build incrementally.

**Week 1: The Minimum Viable Workspace**

Create a folder. Add three files:

```
my-workspace/
├── CLAUDE.md          ← What your project is, where things are
├── docs/
│   └── about.md       ← Your company/project overview
└── context/
    └── voice.md       ← How you want the AI to write
```

Your CLAUDE.md can be 20 lines:

```markdown
# My Workspace

[One sentence about what this is.]

## Where Things Live

| Directory | What's There |
|-----------|-------------|
| docs/     | Company reference docs |
| context/  | How we write and think |

## Rules

1. Don't invent facts not in these docs
2. Write in active voice, be direct
3. When in doubt, ask
```

Your `docs/about.md` can be simple:

```markdown
# About [Your Company]

We do [what you do] for [who you serve]. We've been operating since [year].
Our main focus right now is [current priority].
```

Your `context/voice.md` can start with just preferences:

```markdown
# Writing Voice

Write like a smart friend explaining something important.
Be direct. No jargon. No filler. Active voice.
Our audience is [who reads your content].
```

That's it. Open this folder in Cowork or Claude Code, and the AI already knows more about your work than it would from a blank conversation.

**Week 2-3: Add Skills and Records**

As you find yourself repeating instructions, write them down as skills:

```
.cursor/skills/
├── writing/SKILL.md        ← Your writing process
└── research/SKILL.md       ← How you want research done
```

Start saving useful artifacts:

```
records/
├── meetings/               ← Meeting notes
└── contacts/               ← People you meet
```

**Month 2+: Add Structure and Depth**

Add README.md and INDEX.md to each directory. Create more skills. Build out your knowledge base. Add roles if you want AI personas. Set up MCP connections to your tools.

The system grows organically. You don't design it all upfront.

### 5.2 Seven Principles for Building Well

**1. Structure before content.** Get the folder layout and CLAUDE.md right before writing 50 documents. A good map with 5 files beats a messy pile of 500.

**2. Skills are your highest leverage.** Every time you explain a process to the AI more than twice, write a skill. This is where compounding happens.

**3. Don't bulk-load.** Your CLAUDE.md should point to things, not contain everything. Tiered loading is the whole game.

**4. README and INDEX everywhere.** Every folder needs a welcome sign (README) and a table of contents (INDEX). The AI uses these to navigate. Without them, it guesses.

**5. Name files predictably.** `lowercase-hyphens-v1.md`. Always. The AI relies on patterns to find things. Consistency beats creativity in file naming.

**6. Keep CLAUDE.md short.** Under 100 lines. It loads in every conversation. If it's 500 lines, you're wasting tokens on context that isn't always relevant.

**7. Version, don't delete.** When you rewrite a doc, create `name-v2.md` and move the old one to `/archive`. History matters, and the AI can reference both versions when needed.

### 5.3 Common Mistakes

**Mistake: Writing skills that are too vague.**
"Write good content" is not a skill. "Load the writing style guide, apply these 5 quality checks, save drafts to scratchpad, final output to pipeline/outputs/" — that's a skill. Specificity is everything.

**Mistake: Putting everything in CLAUDE.md.**
CLAUDE.md is a map, not an encyclopedia. Point to files; don't inline their contents. If your CLAUDE.md is over 200 lines, you're probably inlining too much.

**Mistake: No metadata on files.**
Without `last_updated` and `confidence` tags, the AI can't resolve conflicts between files. Metadata takes 30 seconds to add and prevents hours of confusion later.

**Mistake: Ignoring the pipeline.**
Without clear stages (research → scratchpad → outputs), drafts and finished work live in the same place. You end up sending drafts to clients or overwriting finished work.

**Mistake: Starting with tools instead of structure.**
"Which AI tool should I use?" is the wrong first question. "How should I organize my knowledge?" is the right one. The structure works across all tools.

---

## Part 6: Context Engineering — The Meta-Skill

### 6.1 What It Is

Context engineering is the discipline of designing what information AI agents have access to, when they access it, and in what format. It's the meta-skill behind everything in this guide.

Prompt engineering asks: "How do I write the best instruction for this task?"
Context engineering asks: "How do I build a system that gives agents the right information at the right time for any task?"

Prompt engineering is a conversation skill. Context engineering is an architecture skill. The first gets you a good answer. The second gets you a good system.

### 6.2 The Four Questions

Every context engineering decision comes down to four questions:

1. **Does the agent have the right information?** If the AI doesn't know your writing style, it can't write in your voice. If it doesn't know your client history, it can't give relevant advice.

2. **Is the information in the right format?** A 50-page PDF dump is technically "context," but it's bad context. A 20-line summary with links to details is good context. Format determines whether the AI can actually use what you give it.

3. **Is it loaded at the right time?** Loading your entire client database for a writing task wastes tokens. Loading just the style guide and relevant topic research is efficient. Timing matters.

4. **Does the agent have the right tools?** Knowledge without action is just information. MCP connections, file access, and skill instructions turn knowledge into capability.

### 6.3 Why Most Agent Failures Are Context Failures

When AI gives bad output, the instinct is to blame the model. "It's not smart enough." But most of the time, the model is perfectly capable. It just didn't have the right context.

Common context failures:

- **Missing context:** The AI doesn't know your company has a specific writing style, so it writes generic corporate prose.
- **Stale context:** The AI uses an outdated strategy doc because nothing told it a newer version exists.
- **Overloaded context:** You dumped 10 documents into the conversation and the AI can't tell which parts matter for this specific task.
- **Disconnected context:** The AI knows your writing style and knows your client's situation, but no skill ties those two pieces together for this specific deliverable.

The system in this guide addresses each of these failures: metadata tracks freshness, tiered loading prevents overload, skills connect the right context for the right task, and CLAUDE.md ensures nothing critical is missing.

---

## Appendix A: Glossary

| Term | Plain English Definition |
|------|------------------------|
| **Agent** | An AI that can take actions in a loop — read, plan, do, observe, repeat |
| **AGENTS.md** | Entry point file for Cursor (same content as CLAUDE.md) |
| **CLAUDE.md** | Entry point file for Claude Code/Cowork — the project's "constitution" |
| **Cowork** | Anthropic's desktop AI agent for non-developers |
| **Claude Code** | Anthropic's terminal-based AI agent for developers |
| **Context engineering** | The discipline of designing information flow for AI agents |
| **Context window** | How much information an AI can hold at once (~200K tokens for Claude) |
| **Cursor** | AI-first code editor with built-in agent capabilities |
| **Git** | Version control system — tracks every change to every file |
| **GitHub** | Website that hosts Git repos with collaboration features |
| **INDEX.md** | Complete file listing for a directory (table of contents) |
| **Markdown** | Simple text formatting language (`.md` files) |
| **MCP** | Model Context Protocol — universal standard for connecting AI to external tools |
| **Metadata** | Machine-readable tags on files (purpose, audience, freshness, sensitivity) |
| **Model** | The AI brain (Claude, GPT, etc.) — takes text in, produces text out |
| **Pipeline** | Three-stage workflow: research → scratchpad → outputs |
| **Prompt** | The immediate instruction you give the AI in a conversation |
| **README.md** | Explanation of what's in a directory and how to navigate it |
| **Repo** | A folder with version history (short for "repository") |
| **Rules** | Persistent behavioral guidelines the AI follows automatically |
| **Skill** | A reusable playbook for a specific task (SKILL.md file) |
| **Tiered loading** | Loading context in layers — always/task-triggered/on-demand/search-only |
| **Tokens** | Units of text the AI processes (1 token ≈ ¾ of a word) |

## Appendix B: Cheat Sheet — What File Does What

| File/Folder | Purpose | Who Reads It |
|-------------|---------|-------------|
| `CLAUDE.md` | Project entry point and navigation map | Claude Code, Cowork |
| `AGENTS.md` | Same as CLAUDE.md, for Cursor | Cursor |
| `README.md` (in any dir) | Explains what's in this directory | AI agents + humans |
| `INDEX.md` (in any dir) | Lists every file in this directory | AI agents + humans |
| `.cursor/skills/*/SKILL.md` | Playbook for a specific task | All tools |
| `.cursor/rules/*.mdc` | Behavioral rule (Cursor format) | Cursor |
| `context/voice/*.md` | Writing style and voice guidelines | Any writing task |
| `context/roles/*.md` | AI executive personas | Decision/analysis tasks |
| `docs/**/*.md` | Company reference material | Company questions |
| `knowledge/**/*.md` | Study guides and research | Learning/research tasks |
| `pipeline/research/` | Raw research material | Research tasks |
| `pipeline/scratchpad/` | Working drafts | Any deliverable in progress |
| `pipeline/outputs/` | Finished deliverables | Completed work |
| `records/**/*.md` | Archives (contacts, meetings, clients) | Search only — never bulk-load |

## Appendix C: Learning Path

**Phase 1: Understand (Week 1)**
Read Parts 1-3 of this guide. Open the GrowthX repo in Cursor or clone it to see the structure firsthand. Read the CLAUDE.md and navigate the folders.

**Phase 2: Build the Foundation (Week 2)**
Create your own workspace folder. Write a CLAUDE.md. Add a docs/ directory with your core reference material. Add a context/ directory with your voice/style preferences.

**Phase 3: Add Skills (Week 3-4)**
Write your first two skills — start with whatever process you repeat most often. Follow the SKILL.md format from this guide or the GrowthX examples.

**Phase 4: Connect and Scale (Month 2+)**
Set up MCP connections to your key tools (Slack, email, CRM). Add rules for consistency. Build out your records and knowledge directories. Add README.md and INDEX.md to every folder.

**Phase 5: Teach Others (Month 3+)**
Share this guide. Walk someone through your system. The best test of understanding is explaining it to someone else.

## Appendix D: Curated Sources

**Official Documentation**

- [Claude Code Overview](https://code.claude.com/docs/en/overview) — How Claude Code works, CLAUDE.md spec, skills format
- [Claude Code Skills Documentation](https://code.claude.com/docs/en/skills) — Detailed skill creation guide
- [Get Started with Cowork](https://support.claude.com/en/articles/13345190-get-started-with-cowork) — Cowork setup and usage
- [Model Context Protocol](https://modelcontextprotocol.io/) — MCP specification and pre-built servers
- [Cursor Agent Skills](https://cursor.com/docs/context/skills) — Cursor's skill system
- [Cursor Agent Best Practices](https://cursor.com/blog/agent-best-practices) — How to work effectively with Cursor agents

**Key Articles**

- [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — Anthropic's engineering team on context design
- [Context Engineering vs Prompt Engineering](https://neo4j.com/blog/agentic-ai/context-engineering-vs-prompt-engineering/) — Why the shift matters
- [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) — Anthropic's announcement of MCP

**In This Repo**

- [Building Skills for Claude, Claude Code & Cursor — Study Guide](building-ai-skills-study-guide-v1.md) — Deep technical reference on skill building
- [CLAUDE.md](../../CLAUDE.md) — The actual entry point file for this project
- [Context Routing Guide](../../context/context-routing.md) — How context loading works in practice
