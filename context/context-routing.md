# Context Routing Guide

<metadata>
purpose: Detailed routing rules for AI agents navigating this knowledge base
audience: AI agents (Cursor, Claude Code) and humans designing agent workflows
summary: Explains HOW to load context efficiently — tiered loading, task stacks, sensitivity rules, and navigation patterns.
token_estimate: large
depends_on: []
related: ../CLAUDE.md, ../context/README.md, ../pipeline/README.md
domain: company
confidence: canonical
context_tier: 1
last_updated: 2026-02-27
</metadata>

CLAUDE.md tells agents what exists and when to load it. This doc explains HOW to load context efficiently and what to watch out for.

---

## Tiered Context Loading

Not all files are equal. Load the minimum context needed for the task.

| Tier | When Loaded | What's There | Token Budget |
|------|------------|--------------|-------------|
| **0 — Always** | Every conversation | CLAUDE.md (~50 lines) | ~500 tokens |
| **1 — Task-triggered** | When task type is identified | Style guide, relevant role, key docs | 2,000-5,000 tokens |
| **2 — On-demand** | When agent hits a specific question | Individual docs, study guides, research | 1,000-3,000 per file |
| **3 — Search-only** | Only via grep/search, never bulk-loaded | Transcripts, downloads, customer records | Variable |

**The rule:** Start at Tier 0. Escalate only when you need more information. Never skip to Tier 3 without checking Tier 1-2 first.

---

## Task Routing Stacks

Each task type has a recommended loading sequence. Load files in order — stop when you have enough context.

### Writing Content

```
1. context/voice/writing-style-context-v2.md     (always — the definitive guide)
2. context/voice/social-media-style-guide-template-v1.md  (if social media content)
3. context/roles/marketing-v1.md                 (if marketing content)
4. context/roles/aeo-seo-content-v1.md           (if SEO/AEO content)
5. docs/business/business-model.md               (if about GrowthX)
6. docs/products/ecosystem-overview-v1.md        (if about a specific product)
7. knowledge/content/                            (if about writing craft or LinkedIn)
8. knowledge/seo-aeo/                            (if about AEO/answer engines)
```

### Answering Company Questions

```
1. docs/start-here.md                             (orientation)
2. docs/company/strategy-overview.md              (if strategy question)
3. docs/business/business-model.md                (if business model question)
4. docs/business/ideal-customer-profile.md        (if ICP/sales question)
5. docs/delivery/                                 (if about how we deliver)
6. docs/finance/                                  (if financial — flag sensitivity)
```

### Making Strategic Decisions

```
1. context/roles/[relevant-role]-v1.md            (load the right persona)
2. docs/company/strategy-overview.md              (strategic context)
3. docs/business/business-model.md                (business context)
4. docs/finance/fiscal-plan-template.md           (if financial implications)
5. context/personal/[user-manual].md              (if advising the founder directly)
```

### Research / Deep Dives

```
1. knowledge/[relevant-topic]/README.md           (start at the hub)
2. pipeline/research/                             (check existing research)
3. sources/sources-index.md                       (find reference material)
4. records/downloads/                             (search — don't bulk-load)
```

### Client Work

```
1. clients/[client]/[client]-client-context-v1.md (client context — start here, use the file map)
2. clients/[client]/transcripts/                  (search for relevant meetings)
3. clients/[client]/context/                      (brand voice, personas, reference docs)
4. context/voice/writing-style-context-v2.md      (your company voice, if writing as yourself)
5. docs/delivery/                                 (how we deliver)
```

### Looking Up People

```
1. records/contacts/[firstname-lastname]-v1.md     (external contacts — 244 dossiers)
2. records/contacts/employees/[name]-v1.md         (team members — 61 dossiers)
3. records/transcripts/                            (search for meeting history)
4. records/meetings/                               (structured meeting data)
5. sources/people-index.md                         (expert references)
```

### Prospect / Sales Research

```
1. records/prospects/[company]/                    (past prospect research, deal rooms)
2. records/customers/active/                       (existing client context)
3. records/customers/churned/                      (churned client learnings)
4. docs/business/ideal-customer-profile.md         (ICP reference)
5. docs/sales/                                     (sales playbook — when populated)
```

### Creating Deliverables

```
1. Load the relevant task stack above FIRST
2. Save drafts to: pipeline/scratchpad/
3. Save finished work to: pipeline/outputs/
4. Never save directly to docs/ or knowledge/ without explicit instruction
```

---

## Access Classification

Content is classified into 8 access tiers. The canonical reference is `context/access-tiers-v1.md` — load it for full ring definitions, membership, and directory defaults.

| Ring | Label | Who | Action |
|------|-------|-----|--------|
| 0 | `personal` | Founder only | Never load without explicit approval |
| 1 | `founders` | Founders | Never include in any output without founder approval |
| 2 | `inner-circle` | Founders + VP Ops, Chief of Staff | Never include in client-facing or company-wide outputs |
| 3 | `exec` | Executive team | Flag before including in outputs below exec level |
| 4 | `elt` | Extended leadership | Flag before including in outputs below ELT level |
| 5 | `build-team` | Eng, product, design, delivery (no editors/contractors) | Generate freely for internal team use |
| 6 | `company` | All employees | Generate freely, don't share externally |
| 7 | `public` | Anyone | Generate freely |

Every file's `<metadata>` block includes an `access` field. When no field exists, use directory defaults from `context/access-tiers-v1.md`.

**Hard rules:**
- Never generate legal, compliance, or financial content without flagging
- Never include fiscal plans, board meeting content, or valuation data in client-facing outputs
- Never share personal context (psych profile, user manual) externally
- When information conflicts between docs, prefer the newer document
- When content spans multiple tiers, classify at the most restrictive tier present

---

## Pipeline Rules

Files flow forward through the pipeline. Never backward.

```
pipeline/research/  →  pipeline/scratchpad/  →  pipeline/outputs/
    (raw material)       (working drafts)        (finished work)
```

| Stage | What Goes Here | What "Done" Means | Next Step |
|-------|---------------|-------------------|-----------|
| `research/` | Raw research, competitive briefs, data gathering | Material is organized and ready to inform a deliverable | Move key findings to scratchpad/ as a draft |
| `scratchpad/` | Drafts, working docs, experiments | Document is polished enough to share or publish | Graduate to outputs/ |
| `outputs/` | Finished deliverables, published content | Delivered to client or published externally | Archive or reference |

**Process traces:** When a skill produces output, include a trace in the file's metadata:

```xml
<metadata>
source_skill: research-to-study-guide
input_files: [pipeline/research/topic-raw-notes.md]
output_stage: scratchpad
last_updated: 2026-02-27
</metadata>
```

---

## Records: Search Protocol

The `records/` directory contains 3,200+ files. Never bulk-load them.

| Directory | Size | How to Access |
|-----------|------|--------------|
| `records/meetings/` | ~1,944 files | Search by YYYY-MM folder, then by date-prefixed meeting name |
| `records/customers/` | ~420 files | Navigate to `records/customers/active/[client]/` or `churned/[client]/`. Active clients also live in `clients/`. |
| `records/downloads/` | ~427 files | Grep for topics. Most are Lenny's Podcast transcripts. |
| `records/contacts/` | ~244 dossiers | Search by name: `firstname-lastname-v1.md` |
| `records/contacts/employees/` | ~61 dossiers | Search by name or browse INDEX by department |
| `records/transcripts/` | ~186 files | Search by date (YYYY-MM-DD prefix) or grep for keywords |
| `records/prospects/` | ~24 files | Navigate to `records/prospects/[company]/` for deal research |
| `records/slack/` | 1 file | Slack channel index |
| `records/email/` | Empty | Placeholder for future email archives |

**Search strategy:**
1. Use grep/search with specific keywords — never `read *`
2. Start with README.md or INDEX.md in each directory to understand what's there
3. Read only the specific files that match your query
4. If you need meeting context, search by date or participant name

---

## Navigation Patterns

### "I don't know where to look"

1. Read CLAUDE.md (Tier 0 — you already have this)
2. Check the root INDEX.md for a global sitemap
3. Check the README.md in the most relevant directory
4. Search/grep for keywords across the repo

### "I need to understand GrowthX"

Start at `docs/start-here.md`. It links to everything else.

### "I need to write something"

Always load `context/voice/writing-style-context-v2.md` before writing anything. No exceptions.

### "I need a persona for analysis"

Pick from `context/roles/`. The README.md lists all roles with when to use each one.

### "I found conflicting information"

1. Check `last_updated` in metadata — newer wins
2. Check `confidence` in metadata — canonical > current > research > aspirational
3. If still unclear, flag the conflict and ask

---

## Metadata Schema

Files use `<metadata>` XML tags for machine-readable context:

```xml
<metadata>
purpose: [1 sentence — what this file is for]
audience: [who reads this]
related: [2-4 relative paths to connected files]
domain: [company|business|delivery|product|finance|aeo|writing|research]
confidence: [canonical|current|research|aspirational]
access: [personal|founders|inner-circle|exec|elt|build-team|company|public]
context_tier: [0|1|2|3]
last_updated: [YYYY-MM-DD]
</metadata>
```

**Confidence levels:**
- **canonical** — Source of truth, actively maintained
- **current** — Accurate as of last_updated, may drift
- **research** — Findings and analysis, not official position
- **aspirational** — Future plans, not yet implemented
