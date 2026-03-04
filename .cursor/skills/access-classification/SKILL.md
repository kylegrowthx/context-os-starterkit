---
name: access-classification
description: Classify files with access tiers and update directory READMEs. Use when tagging files with access levels, auditing access metadata, bulk-classifying directories, or checking that files have proper access fields. Triggers on "classify access", "tag access", "audit access", "access tier", "who can see this".
---

# Access Classification

Tag files with the correct `access` tier and ensure directory READMEs include access summaries.

## Inputs / Outputs

| | What | Example |
|---|---|---|
| **Input** | A file, directory, or glob pattern to classify | `docs/finance/`, `records/customers/active/`, or a single file path |
| **Output** | Updated metadata blocks with `access` field, updated README.md files | Files edited in place |

## Reference

Load `context/access-tiers-v1.md` before starting. It contains:
- The 8-ring hierarchy: `personal` → `founders` → `inner-circle` → `exec` → `elt` → `build-team` → `company` → `public`
- Directory default mappings
- Ring membership definitions
- Classification rules

## Process

### Single file classification

1. Read the file
2. Check if it has a `<metadata>` block
3. If yes, check for an existing `access` field
4. If no `access` field, determine the correct tier:
   a. Start with the directory default from `context/access-tiers-v1.md`
   b. Read the file content to check if it should be MORE restrictive
   c. Look for signals: financial data → `inner-circle` or `founders`, personal data → `personal`, client revenue/contracts → `inner-circle`, general client ops → `exec`
5. Add the `access` field to the metadata block (after `sensitivity` if present)
6. If a `sensitivity` field exists, keep it for backward compatibility

### Directory classification

1. Read the directory's README.md
2. Add or update the access summary section:
   ```markdown
   ## Access

   **Default access:** `[tier]`
   **Contains restricted content:** [Yes/No] — [brief note if yes]
   ```
3. Process each `.md` file in the directory that has a `<metadata>` block
4. Apply the single file process to each
5. Report a summary: how many files tagged, what tiers assigned, any files that need manual review

### Bulk audit

When asked to audit access across the whole repo:

1. Start with high-risk directories first: `context/personal/`, `docs/finance/`, `records/customers/`
2. Then process remaining directories in order of sensitivity
3. Generate an audit report listing:
   - Files with `access` field already set
   - Files where `access` was added
   - Files with no metadata block (skip these, report them)
   - Files that need manual review (ambiguous content)
4. Save the audit report to `pipeline/scratchpad/YYYY-MM-DD-access-audit-report-v1.md`

## Classification signals

Use these heuristics when content is ambiguous:

| Signal | Likely tier |
|--------|------------|
| Marcel's psychology, personality, personal preferences | `personal` |
| Cap table, valuation, equity splits, board votes | `founders` |
| Fiscal plans, compensation, hiring plans, strategic pivots | `inner-circle` |
| Client P&L, churn analysis, revenue by client, contract terms | `inner-circle` |
| Client operating manuals, engagement strategy | `exec` |
| Revenue targets, quarterly goals, department budgets | `elt` |
| Delivery playbooks, technical docs, internal tools | `build-team` |
| Contact dossiers, meeting transcripts, prospect research | `build-team` |
| Company handbook, culture, policies, onboarding | `company` |
| Study guides, reference materials, writing style | `company` |
| Published content, public product docs | `public` |

## Rules

- When content spans multiple tiers, classify at the MOST restrictive tier present
- Never downgrade a file's access without explicit approval from Marcel
- Always preserve the existing `sensitivity` field — add `access` alongside it
- Files without `<metadata>` blocks should be flagged for review, not silently skipped
- The audit report should be honest about gaps — don't pretend everything is classified
