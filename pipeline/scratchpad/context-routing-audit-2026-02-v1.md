# Context Routing & Project Audit — February 2026

<metadata>
purpose: Audit of growthx-context project structure vs documentation accuracy
audience: Marcel, AI agents
related: CLAUDE.md, context/context-routing.md, INDEX.md
domain: company
confidence: current
sensitivity: internal
context_tier: 2
last_updated: 2026-02-27
</metadata>

---

## Executive Summary

The growthx-context knowledge base has grown significantly since the last documentation pass (Feb 9, 2026). The project now contains **44,271 files** across 10 top-level directories — but CLAUDE.md, context-routing.md, and the root INDEX.md still describe the structure from an earlier era.

The core architecture is solid. The tiered loading system, pipeline flow, sensitivity classification, and metadata schema are all well-designed and don't need rethinking. What needs work is **catching the docs up to reality** — new directories exist that agents can't find, path references are broken, and file counts are stale.

This document covers every discrepancy found and recommends specific fixes, grouped by priority.

---

## Priority 1: Broken References (Agents Will Fail)

These are paths or claims that will cause an AI agent to error or load the wrong thing.

### 1.1 — `knowledge/aeo/` path no longer exists

**Where it's wrong:** CLAUDE.md line 31, context-routing.md lines 44 and 71

Both files reference `knowledge/aeo/README.md` as the AEO hub. That directory has been renamed to `knowledge/seo-aeo/`. An agent following the routing instructions will get a file-not-found error.

**Fix:** Replace all references to `knowledge/aeo/` with `knowledge/seo-aeo/` in both CLAUDE.md and context-routing.md.

### 1.2 — "9 AI executive personas" should be 10

**Where it's wrong:** CLAUDE.md line 16

The roles directory contains 10 roles (the original 9 plus `aeo-expert-v1.md`). The README in `context/roles/` correctly lists all 10. CLAUDE.md is the only file that's wrong.

**Fix:** Change "9 AI executive personas" → "10 AI executive personas"

### 1.3 — Duplicate skill entry in CLAUDE.md

**Where it's wrong:** CLAUDE.md lines 59–60

"Scrape Website" appears twice in the skills table with identical content.

**Fix:** Remove the duplicate row.

---

## Priority 2: Missing Directories in Documentation (Agents Can't Route Here)

These are real, populated directories that CLAUDE.md and context-routing.md don't know about. An agent asked to work with this data has no guidance on how to find or use it.

### 2.1 — `records/contacts/` (248 files) — Barely mentioned

Contains 190 external contact dossiers and 61 employee dossiers in an `employees/` subdirectory. This is a mature, well-structured system with its own README, INDEX, and a dedicated Contact Dossier skill — but CLAUDE.md doesn't list it in the "Where Things Live" table or "When to Load More Context" section.

**Fix:** Add to CLAUDE.md's directory table and add a routing entry like: "Looking up a person? Search `records/contacts/` for dossiers, `records/contacts/employees/` for team members."

### 2.2 — `records/meetings/` (1,947 files) — Not mentioned anywhere

The largest records subdirectory by far. Date-organized (YYYY-MM folders from April 2024 through Feb 2026) with structured meeting data distinct from raw transcripts. Neither CLAUDE.md nor context-routing.md references it.

**Fix:** Add to CLAUDE.md's records description. Add to context-routing.md's "Records: Search Protocol" table. Clarify the relationship between `records/meetings/` (structured meeting data) and `records/transcripts/` (enriched transcripts).

### 2.3 — `records/prospects/` (24 files) — Not mentioned anywhere

Contains research folders for 5 prospect/churned accounts (Eon, GetAccept, Pluralsight, Simple Life, Spendesk) with deal room materials, competitive research, and deliverables. Has its own README and INDEX.

**Fix:** Add to CLAUDE.md and context-routing.md. Natural home in the "Client Work" task stack — something like: "Past prospects? Search `records/prospects/` for deal research and deliverables."

### 2.4 — `projects/` (40,658 files) — Not mentioned anywhere

This is the elephant in the room by file count (92% of all files), though most of it is the Fathom backup JSON dump. Contains two project directories: `fathom-backup/` (API backup data) and `acespremortho/` (scraped website). Has no INDEX.md.

**Fix:** Add to CLAUDE.md's directory table with a note that this is project-specific working data (not core knowledge base content). Add a `projects/INDEX.md`. Consider whether `projects/` needs a "Search only — never bulk-load" warning similar to `records/`.

### 2.5 — `docs/sales/` — Placeholder exists but undocumented

Has a README marked "Coming Soon" and an empty INDEX. Not mentioned in CLAUDE.md or context-routing.md.

**Fix:** Either add it to the docs table with a "(coming soon)" note, or leave it undocumented until populated. Low priority either way.

### 2.6 — `docs/products/contentos/` and `docs/products/output/` — Placeholders

Both have READMEs but no content. The ecosystem is partially documented (CheckThat is well-covered) but ContentOS and Output.ai are stubs.

**Fix:** No documentation change needed until content arrives. Just be aware these exist when the product docs expand.

---

## Priority 3: Stale Counts & Minor Inaccuracies

These won't cause agent failures but create a misleading picture of the knowledge base's scale.

### 3.1 — Root INDEX.md is outdated

The global INDEX.md was "last generated February 2026" but reflects an earlier state. It references `records/customers/lovable/` (flat structure) rather than the current `active/` and `churned/` subdirectory model. Doesn't list `records/contacts/`, `records/meetings/`, `records/prospects/`, or `projects/`.

**Fix:** Regenerate the root INDEX.md to reflect current structure.

### 3.2 — records/README.md file counts are stale

Claims ~57 transcripts (actual: 189), ~54 customers (actual: 431 files across active/churned). Doesn't mention contacts (248 files), meetings (1,947 files), or prospects (24 files).

**Fix:** Update file counts and add the missing subdirectory entries.

### 3.3 — knowledge/ subdirectories have grown

The INDEX.md lists categories (content, building, product, aeo) from the original structure. New subdirectories exist: `ai/` (7 files), `growthx/` (3 files), `people-company/` (1 file), `productivity/` (7 files), `revenue/` (4 files), `social/` (4 files), `writing/` (4 files). Also a loose file: `hubspot-crm-system-guide-v1.md` sitting at the knowledge root.

**Fix:** Update `knowledge/INDEX.md` and `knowledge/README.md` to reflect all current subdirectories. Move the loose HubSpot file into an appropriate subdirectory or add it to the index.

### 3.4 — Missing INDEX.md files

These directories lack the INDEX.md that the project convention requires:

- `context/` (no INDEX.md at root level)
- `projects/` (no INDEX.md)
- `records/email/` (empty dir, no INDEX)
- `records/slack/` (1 file, no INDEX)
- `records/assets/` (1 file, no INDEX)

**Fix:** Create INDEX.md files for `context/` and `projects/` at minimum. The empty/single-file records subdirs can wait.

---

## Priority 4: Context Routing Improvements

These aren't bugs — they're opportunities to make the routing smarter.

### 4.1 — No task stack for "People Lookup"

With 248 contact dossiers and 61 employee files, people lookup is a real workflow. Context-routing.md has no stack for it.

**Suggested stack:**
```
### Looking Up People

1. records/contacts/[firstname-lastname]-v1.md    (external contacts)
2. records/contacts/employees/[name]-v1.md         (team members)
3. records/transcripts/                            (search for meeting history)
4. records/meetings/                               (structured meeting data)
5. sources/people-index.md                         (expert references)
```

### 4.2 — No task stack for "Prospect / Sales Research"

There's a whole `records/prospects/` directory and a `docs/sales/` placeholder, but no routing for sales-related tasks.

**Suggested stack:**
```
### Prospect Research / Sales Support

1. records/prospects/[company]/                    (past prospect research)
2. records/customers/active/                       (existing client context)
3. records/customers/churned/                      (churned client learnings)
4. docs/business/ideal-customer-profile.md         (ICP reference)
5. docs/sales/                                     (when populated)
```

### 4.3 — "Records: Search Protocol" table is incomplete

The table lists only transcripts, customers, and downloads. Should also include:

| Directory | Size | How to Access |
|-----------|------|---------------|
| `records/contacts/` | 248 files | Search by name: `firstname-lastname-v1.md` |
| `records/contacts/employees/` | 61 files | Search by name or browse INDEX by department |
| `records/meetings/` | 1,947 files | Search by YYYY-MM folder, then by date prefix |
| `records/prospects/` | 24 files | Navigate to `records/prospects/[company]/` |

### 4.4 — `.cursor/rules/` only partially documented

CLAUDE.md lists 2 of 5 rules. The unlisted rules are: `context-navigation.mdc`, `file-naming.mdc`, and `readme-maintenance.mdc`. These are useful context for agents.

**Fix:** Add all 5 rules to the CLAUDE.md Rules table.

### 4.5 — Sensitivity classification could include new directories

The sensitivity table in context-routing.md doesn't classify `records/contacts/`, `records/prospects/`, or `context/personal/employees/`. Employee dossiers in particular likely warrant "Internal" or "Leadership-only" classification.

**Fix:** Add rows for contacts (internal), employees (internal), and prospects (internal).

---

## Recommended Update Sequence

If you want to tackle this, here's the order I'd suggest:

1. **CLAUDE.md** — Fix the 3 broken references (P1), add missing directories to the table, update counts
2. **context/context-routing.md** — Fix `aeo/` path, add People Lookup and Prospect stacks, expand Records search table
3. **Root INDEX.md** — Regenerate to reflect current structure
4. **records/README.md** — Update file counts and add missing subdirectories
5. **knowledge/README.md + INDEX.md** — Update subdirectory listings
6. **Create missing INDEX.md files** — `context/INDEX.md`, `projects/INDEX.md`

Estimated effort: ~2 hours of focused editing, or I can do it for you right now.

---

## What's Working Well

To be clear — the bones of this system are excellent:

- **Tiered context loading** is a genuinely smart pattern. Most AI knowledge bases dump everything into one context window. Yours doesn't.
- **The pipeline flow** (research → scratchpad → outputs) is clean and actually being used.
- **Metadata schema** is consistent and machine-readable across files.
- **Skills registry** in CLAUDE.md is comprehensive (21 skills, well-triggered).
- **Sensitivity classification** catches the right things.
- **README + INDEX convention** is followed almost everywhere — the few gaps are in newer directories.

The system hasn't broken down. It's just grown faster than the documentation could keep up.
