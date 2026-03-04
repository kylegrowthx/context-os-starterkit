# Access Tiers

<metadata>
purpose: Canonical reference for the 8-ring access classification system used across this knowledge base
audience: AI agents (Cursor, Claude Code) and humans managing file access
related: context/context-routing.md, CLAUDE.md, AGENTS.md
domain: company
confidence: canonical
sensitivity: internal
access: company
context_tier: 1
last_updated: 2026-03-02
</metadata>

This document defines who can see what. Every file in this knowledge base has an `access` tier that controls who should have visibility. Agents must check a file's `access` tier before loading it into context or including it in outputs.

---

## The 8 Rings

Access flows outward. Each ring includes everyone in the rings inside it.

| Ring | Label | Who | Examples |
|------|-------|-----|----------|
| 0 | `personal` | Marcel only | Psych profile, personal user manual, personal financial details |
| 1 | `founders` | Marcel + Daniel Lopes | Cap table, valuation, board materials, co-founder dynamics, equity |
| 2 | `inner-circle` | Founders + Bridget (VP Ops), George (Chief of Staff) | Fiscal plans, hiring plans, compensation data, strategic pivots |
| 3 | `exec` | Executive team | Client P&L, churn analysis, org-wide metrics, leadership decisions |
| 4 | `elt` | Extended leadership team | Revenue targets, quarterly goals, department budgets, strategic roadmap |
| 5 | `build-team` | Eng, product, design, delivery leads (not editors/contractors) | Delivery playbooks, client operating manuals, internal tools, technical architecture |
| 6 | `company` | All employees | Company handbook, culture, onboarding, policies, how-we-work, writing style |
| 7 | `public` | Anyone | Published content, CheckThat public docs, marketing materials |

---

## Ring Membership

Current membership as of 2026-03-02. Update this section when the team changes.

**Ring 0 — personal:** Marcel Santilli

**Ring 1 — founders:** Marcel Santilli, Daniel Lopes

**Ring 2 — inner-circle:** Founders + Bridget (VP of Ops), George (Chief of Staff)

**Ring 3 — exec:** Inner circle + executive team leads (TBD — populate as roles are filled)

**Ring 4 — elt:** Exec + extended leadership (department heads, senior managers)

**Ring 5 — build-team:** ELT + full-time engineering, product, design, and delivery team members. Excludes freelance editors, part-time contractors, and external collaborators.

**Ring 6 — company:** All employees including editors, contractors, and part-time staff.

**Ring 7 — public:** No restrictions.

---

## How Access Works in Metadata

Every file with a `<metadata>` block must include an `access` field:

```xml
<metadata>
purpose: Fiscal plan for 2026
audience: Leadership team
related: docs/finance/fiscal-plan-2025.md
domain: finance
confidence: canonical
sensitivity: leadership-only
access: inner-circle
context_tier: 2
last_updated: 2026-02-09
</metadata>
```

The `access` field replaces `sensitivity` as the primary access control. The `sensitivity` field is retained for backward compatibility but `access` is authoritative when both are present.

---

## Access vs. Sensitivity Mapping

The old three-level `sensitivity` system maps to the new `access` tiers:

| Old sensitivity | New access (default) | Notes |
|----------------|---------------------|-------|
| `public` | `public` | Direct mapping |
| `internal` | `company` | Most internal content is company-wide |
| `leadership-only` | `inner-circle` or `exec` | Depends on content — financial = inner-circle, operational = exec |

---

## Directory Defaults

When a file has no `access` field yet, assume the default for its directory:

| Directory | Default access | Rationale |
|-----------|---------------|-----------|
| `context/personal/` | `personal` | Marcel's personal context |
| `docs/finance/` (board meetings, cap table, valuation) | `founders` | Board-level financial data |
| `docs/finance/` (fiscal plans, compensation, hiring) | `inner-circle` | Operational financial data |
| `docs/finance/` (pricing, market size, growth strategy) | `exec` | Strategic but not sensitive |
| `records/customers/` | `exec` | Client data requires leadership visibility |
| `records/customers/` (revenue, P&L, contract terms) | `inner-circle` | Financial client data |
| `context/roles/` | `build-team` | AI personas used by technical team |
| `docs/delivery/` | `build-team` | Delivery processes |
| `docs/epd/` | `build-team` | Engineering/product/design |
| `records/contacts/` | `build-team` | External contact dossiers |
| `records/transcripts/` | `build-team` | Meeting transcripts |
| `records/meetings/` | `build-team` | Meeting records |
| `records/prospects/` | `build-team` | Pre-sales research |
| `knowledge/` | `company` | Study guides and reference |
| `docs/company/` | `company` | Company handbook |
| `docs/people/` | `company` | HR and policies |
| `docs/how-we-work/` | `company` | Communication and tools |
| `docs/business/` | `company` | Business model (non-financial) |
| `context/voice/` | `company` | Writing style |
| `records/contacts/employees/` | `company` | Employee profiles |
| `docs/products/checkthat/public/` | `public` | Public product docs |
| `pipeline/` | Inherited | Inherits from source material |
| `projects/` | `build-team` | Project working data |
| `sources/` | `company` | Reference indexes |
| `prompts/` | `build-team` | Prompt templates |
| `records/downloads/` | `company` | External reference content |

---

## Agent Rules

### Before loading any file

1. Check the file's `access` field in metadata.
2. If no `access` field exists, use the directory default from the table above.
3. If the current task context doesn't justify access to that ring, do not load the file.

### Before including content in outputs

1. Never include `personal` or `founders` content in any output without Marcel's explicit approval.
2. Never include `inner-circle` content in client-facing or company-wide outputs.
3. Never include `exec` or `elt` content in outputs visible to build-team or below.
4. When in doubt, flag the access level and ask.

### When creating new files

1. Always include an `access` field in the metadata block.
2. Default to the directory default unless the content clearly belongs to a different ring.
3. If a file contains mixed-access content, classify it at the most restrictive ring present.

---

## README Access Markers

Every directory README.md should include an access summary near the top:

```markdown
## Access

**Default access:** `build-team`
**Contains restricted content:** Yes — see individual file metadata for overrides.
```

This lets agents and humans quickly understand the access level of a directory without reading every file.

---

## Changelog

- **2026-03-02** — v1 created. 8-ring model established. Replaces the 3-level sensitivity system.
