# Client Work Agent Configuration

<metadata>
purpose: Context loading instructions for creating client deliverables and materials
audience: AI agents
summary: Configures an AI agent for client work — loads client context, routes to the right artifacts by deliverable type, and outputs to client directories
token_estimate: small
depends_on: clients/README.md
domain: client
confidence: canonical
context_tier: 1
last_updated: 2026-02-22
</metadata>

## When to Load This

Load this agent config when the task involves:
- Creating any deliverable for or about a specific client
- Drafting strategy docs, reports, proposals, or recommendations for a client
- Writing content on behalf of a client (using their voice)
- Preparing client-facing emails, updates, or presentations
- Reviewing or revising existing client work
- Any task where the output needs to reflect deep knowledge of a client account

## Required Context (Always Load)

1. `clients/[client-name]/[client-name]-client-context-v1.md` — The client context file. Read this first. It contains relationship context, engagement history, active workstreams, and a **file map** pointing to all other relevant files.
2. `context/voice/writing-style-context-v2.md` — GrowthX voice (for internal materials and your POV in client deliverables)

## Conditional Context (Use the File Map)

The client context file contains a file map organized by category. Load files based on what you're creating:

| Deliverable Type | Load From File Map |
|-----------------|-------------------|
| Strategy docs, recommendations, plans | Current Strategy + Research & Data sections |
| Content written in the client's voice | Brand & Voice section |
| Reports, audits, assessments | Current Strategy + Research & Data sections |
| Proposals, SOWs, scope expansions | Engagement History (in context file) + Current Strategy |
| Client-facing emails or updates | Relationship Context (in context file) + Brand & Voice |
| Presentations | Current Strategy section |

If the file map doesn't have what you need, search the client's `transcripts/` directory for relevant prior discussions.

## Behavioral Rules

1. **Always read the client context file first** — before generating anything. The file map tells you what else to load.
2. **Reference prior work** — check the engagement history and active workstreams. New materials should build on what came before, not start from scratch.
3. **Match the right voice** — use the client's brand voice for materials they'll publish. Use the GrowthX voice for materials you're presenting to the client.
4. **Know the relationship** — the context file has notes on communication preferences, decision-making style, and sensitivities. Use them.
5. **Search transcripts, don't bulk-load them** — transcripts are large. Search for specific topics rather than reading them whole.
6. **Flag stale context** — if the context file's `last_updated` date is more than a month old, tell the user it may need refreshing.
7. **Don't invent client facts** — if you don't have information about the client's business, goals, or preferences in the loaded context, say so rather than guessing.
8. **No em dashes in any output.** Replace with periods, commas, or colons. This applies to all client-facing and internal materials.

## Output Conventions

- Save work to `clients/[client-name]/deliverables/[project-name]/`
- Create a new subdirectory under `deliverables/` for each distinct project or phase
- Use file naming: `descriptive-name-v1.md` (lowercase, hyphens, version suffix)
- For quick one-off materials that don't belong to a project, save directly to `clients/[client-name]/deliverables/`

## After Completing Work

Remind the user to update:
- The **engagement history** section in the client context file if scope or strategy changed
- The **active workstreams** section if priorities shifted
- The **file map** if new important artifacts were created
