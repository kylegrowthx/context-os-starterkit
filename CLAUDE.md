# GrowthX CEO OS

Knowledge base for GrowthX. Not a codebase — no app, no build step. The product is context.

## What We Do

- **GrowthX (services)**: B2B content marketing. $200k+/year engagements. Main revenue driver.
- **CheckThat (software)**: Open AI visibility index for B2B. Strategic bet.

## Where Things Live

| Directory | What's There | Load When |
|-----------|-------------|-----------|
| `docs/handbook/` | Auto-synced mirror of handbook.growthx.ai — company, delivery, EPD, products, guides, tutorials, systems | Understanding GrowthX or answering company questions |
| `docs/private-docs/` | Internal docs not in the handbook — finance, business, sales, job specs | Financial questions, business model, sensitive internal docs |
| `docs/archive/` | Superseded docs and pre-handbook-sync backups | Historical reference only |
| `context/voice/` | How we write — style guide, LinkedIn style | Any writing or content task |
| `context/roles/` | How we think — 10 AI executive personas | Decision support, analysis, reasoning |
| `context/personal/` | Who Marcel is — user manual, psych profile | Working directly with Marcel |
| `knowledge/` | Study guides, reference materials, AEO research | Deep research or learning tasks |
| `pipeline/` | research/ → scratchpad/ → outputs/ (flows forward only) | Creating any deliverable |
| `records/` | Transcripts, meetings, contacts, customers, prospects, downloads | Search only — never bulk-load |
| `projects/` | Project-specific working data (Fathom backup, client scrapers) | Search only — never bulk-load |
| `sources/` | People and sources indexes | Finding experts or references |
| `prompts/` | Reusable prompt templates | Building AI workflows |

## When to Load More Context

Don't load everything. Read what you need for the task:

- **Writing content?** Read `context/voice/writing-style-context-v2.md` first. It's the definitive guide.
- **Company questions?** Start at `docs/handbook/start-here.md`, then drill into the relevant `docs/handbook/` subdirectory.
- **Financial/board questions?** Search `docs/private-docs/finance/` (access: founders/inner-circle).
- **Making decisions?** Load a role from `context/roles/` (e.g., `cfo-v1.md` for financial decisions).
- **AEO / AI visibility?** Start at `knowledge/seo-aeo/README.md` — consolidated hub with guides and research.
- **Looking up a person?** Search `records/contacts/` for dossiers, `records/contacts/employees/` for team members.
- **Client work?** Search `records/customers/` for client context, `records/transcripts/` for meeting notes.
- **Past prospects?** Search `records/prospects/` for deal research and deliverables.
- **Meeting history?** Search `records/meetings/` (structured data) or `records/transcripts/` (enriched transcripts).
- **Saving an article?** Use the `save-read` skill → saves to `knowledge/good-reads/`.
- **Creating deliverables?** Save drafts to `pipeline/scratchpad/`, finished work to `pipeline/outputs/`.

For detailed routing, task stacks, and sensitivity rules, see `context/context-routing.md`.

## Skills

Cursor auto-discovers skills from `.cursor/skills/`. For Claude Code, reference these directly.

| Skill | Path | Trigger |
|-------|------|---------|
| Copywriting | `.cursor/skills/copywriting/SKILL.md` | Any writing task — posts, outreach, event pages, newsletters |
| Creating Hooks and Offers | `.cursor/skills/creating-hooks-and-offers/SKILL.md` | Creating campaigns, funnels, event pages, landing pages |
| GrowthX Writing | `.cursor/skills/growthx-writing/SKILL.md` | "Write", "draft", "edit", or "review" content |
| File Naming | `.cursor/skills/file-naming/SKILL.md` | Creating or renaming files |
| Post to Slack | `.cursor/skills/post-to-slack/SKILL.md` | "Post to Slack" / "Send a message to [channel]" |
| Pull Meeting | `.cursor/skills/pull-meeting/SKILL.md` | "Pull meeting" / "Get transcript from Fireflies" — master orchestrator that chains enrich + link skills |
| Research to Study Guide | `.cursor/skills/research-to-study-guide/SKILL.md` | "Research [topic]" / "Create a study guide" |
| Contact Dossier | `.cursor/skills/contact-dossier/SKILL.md` | "Create a contact", "update contact", "save contact", "build a profile on [person]" |
| Competitor Brief | `.cursor/skills/competitor-brief/SKILL.md` | "Competitor brief" / "competitor analysis" / "competitive research" / "research [company] as a competitor" |
| Update Notion Doc | `.cursor/skills/update-notion-doc/SKILL.md` | "Update Notion" / "Sync to Notion" |
| Sync Meetings | `.cursor/skills/sync-meetings/SKILL.md` | "Sync meetings" / "Pull calendar" / "Log meetings" / "Meeting history" — also runs weekly on schedule |
| Fathom Backup | `.cursor/skills/fathom-backup/SKILL.md` | "Backup fathom" / "Download fathom meetings" / "Continue fathom backup" / "Batch download" / "Get all meetings" |
| Convert Fathom Transcript | `.cursor/skills/convert-fathom-transcript/SKILL.md` | "Convert fathom" / "Fathom to transcript" / "Import fathom meetings" / "Process fathom dump" |
| Enrich Fathom Transcript | `.cursor/skills/enrich-fathom-transcript/SKILL.md` | "Enrich fathom transcript" / "Clean up fathom" / "Fix fathom speakers" / "Production-ready fathom transcript" |
| Enrich Fireflies Transcript | `.cursor/skills/enrich-fireflies-transcript/SKILL.md` | "Enrich fireflies transcript" / "Clean up fireflies" / "Fix fireflies transcript" / "Production-ready transcript" |
| Link Transcript Records | `.cursor/skills/link-transcript-records/SKILL.md` | "Link transcript" / "Update meeting record" / "Sync transcript contacts" / "Link contacts to transcript" / "Post-process transcript" |
| Scrape Website | `.cursor/skills/scrape-website/SKILL.md` | "Scrape website" / "scrape site" / "download website" / "crawl site" / "convert website to markdown" / "site to markdown" / "archive website" / "pull all pages from" |
| Account Health Scoring | `.cursor/skills/account-health-scoring/SKILL.md` | "Score {client}" / "health scores on {client}" / "how healthy is {client}" / "weekly health check on {client}" / "compare my scores for {client}" |
| Client Account Assessment | `.cursor/skills/client-account-assessment/SKILL.md` | "Account assessment" / "account deep-dive" / "full status on {client}" / "prep me for the {client} QBR" / "client snapshot" |
| Access Classification | `.cursor/skills/access-classification/SKILL.md` | "Classify access" / "tag access" / "audit access" / "access tier" / "who can see this" |
| Sync Handbook | `.cursor/skills/sync-handbook/SKILL.md` | "Sync handbook" / "update handbook docs" / "pull handbook changes" / "handbook to context" |
| SEO Domain Audit | `.cursor/skills/seo-domain-audit/SKILL.md` | "SEO audit on {domain}" / "audit {domain}" / "domain overview for {domain}" / "pull SEO metrics for {domain}" |
| Competitive SEO Landscape | `.cursor/skills/competitive-seo-landscape/SKILL.md` | "Competitive landscape for {domain}" / "competitor SEO analysis" / "benchmark {domain} against competitors" |
| AEO Audit | `.cursor/skills/aeo-audit/SKILL.md` | "AEO audit for {brand}" / "AI visibility report" / "how visible is {brand} to AI" / "AI engine optimization audit" |
| SEO + AEO Overview | `.cursor/skills/seo-aeo-overview/SKILL.md` | "Full SEO and AI overview for {domain}" / "comprehensive visibility report" / "combined SEO and AEO analysis" |
| Competitive Comparison Table | `.cursor/skills/competitive-comparison-table/SKILL.md` | "Competitive comparison table" / "side-by-side competitor comparison" / "compare all competitors SEO and AI" |
| Content Pages Audit | `.cursor/skills/content-pages-audit/SKILL.md` | "Content pages audit" / "content page detail" / "blog audit" / "audit content pages" / "per-page SEO audit" / "page-level audit" |
| Save Read | `.cursor/skills/save-read/SKILL.md` | "Save read" / "save this article" / "good read" / "save this post" / "add to reading list" / shares a URL to keep |

These are cross-cutting skills shared across all workspaces. Operational GTM skills (HubSpot, Ordinal, AEO prompts) live in gtm-brain/.cursor/skills/.

## Rules

| Rule | Trigger |
|------|---------|
| Contact–Transcript Linking | After processing any transcript, update related contact dossiers and cross-link between `records/contacts/` and `records/transcripts/`. See `.cursor/rules/contact-transcript-linking.mdc` for full spec. |
| Skill Registry Sync | After creating, renaming, or deleting a skill in `.cursor/skills/`, update the skills table in **both** `CLAUDE.md` and `AGENTS.md`. See `.cursor/rules/skill-registry-sync.mdc` for full spec. |
| Context Navigation | Navigation patterns for finding content in the knowledge base. See `.cursor/rules/context-navigation.mdc`. |
| File Naming | Naming conventions for all new files. See `.cursor/rules/file-naming.mdc`. |
| README Maintenance | Standards for keeping README and INDEX files up to date. See `.cursor/rules/readme-maintenance.mdc`. |
| Access Classification | Every file with metadata must have an `access` tier. Every directory README must have an access summary. See `.cursor/rules/access-classification.mdc`. |
| Handbook Sync | Files in `docs/handbook/` are auto-synced. Don't edit manually — edit growthx-handbook instead. See `.cursor/rules/handbook-sync.mdc`. |

## Universal Rules

1. **Don't invent facts** about GrowthX not in these docs
2. **Don't bulk-load** records/ or downloads/ — search them
3. **Newer docs win** when information conflicts
4. **Check access tiers** — every file has an `access` level (`personal` → `founders` → `inner-circle` → `exec` → `elt` → `build-team` → `company` → `public`). Check before loading or including in outputs. See `context/access-tiers-v1.md`.
5. **Flag sensitive content** — don't generate legal, compliance, or financial content without asking
6. **File naming**: `descriptive-name-v1.md` (lowercase, hyphens, version suffix)
7. **Voice**: Direct, clear, real. Like a smart friend explaining something important. No jargon, no filler, no passive voice.

## File Structure

Every directory has `README.md` (what's here, why) and `INDEX.md` (complete file listing). Root `INDEX.md` is the global sitemap.

Files use `<metadata>` tags for machine-readable context: purpose, audience, related files, domain, confidence, access, last_updated.

**Versioning:** Minor updates edit in place. Major changes create `-v2`, old goes to `/archive`.
