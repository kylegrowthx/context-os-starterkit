---
name: client-work
description: Create deliverables and materials for client accounts using deep client context. Use when creating strategy docs, reports, proposals, content, presentations, or client-facing comms. Triggers on "for [client]", "client work", "draft for", "create for", "prepare for", "write for", "[client name]".
---

# Client Work

Create materials and deliverables for client accounts, grounded in deep account context.

## Inputs / Outputs

| | What | Path |
|---|---|---|
| **Input** | Deliverable request from user (what to create, for which client) | Conversational |
| **Agent config** | `agent-docs/client-work-agent.md` (always load) | -- |
| **Client context** | `clients/[client-name]/[client-name]-client-context-v1.md` (always load) | -- |
| **Client artifacts** | Additional files from the file map in the context file | Varies by task |
| **Output** | Finished deliverable | `clients/[client-name]/deliverables/[project]/` |

## Workflow

### 1. Identify the Client

Determine which client from the request. Look in `clients/` for matching directories.

### 2. Load Context

1. Read `agent-docs/client-work-agent.md` for behavioral rules and routing
2. Read the client's context file: `clients/[client-name]/[client-name]-client-context-v1.md`
3. Review the **file map** in the context file — it tells you which files to load for which purpose

### 3. Load Task-Specific Artifacts

Based on what you're creating, load the relevant files from the file map:

| Creating | Load these sections from the file map |
|----------|--------------------------------------|
| Strategy, recommendations | Current Strategy, Research & Data |
| Content in client's voice | Brand & Voice |
| Reports, audits | Current Strategy, Research & Data |
| Proposals, SOWs | Current Strategy + review Engagement History |
| Client emails, updates | Review Relationship Context in the context file |
| Presentations | Current Strategy |

If you need information not covered by the file map, search the client's `transcripts/` directory.

### 4. Clarify the Deliverable

Before drafting, confirm with the user:
- What specifically are they creating? (format, length, level of detail)
- Who is the audience? (client stakeholders, internal team, external)
- Any specific points to hit or avoid?
- Which project/phase does this belong to?

### 5. Draft and Deliver

- Draft the material using the loaded context
- Match voice to audience: client's brand voice for their content, your company voice for materials you're presenting
- Reference prior work and active workstreams — new materials should feel continuous, not from scratch
- Save to `clients/[client-name]/deliverables/[project-name]/` using `descriptive-name-v1.md` naming

### 6. Post-Delivery

Remind the user to update the client context file if:
- The engagement scope or strategy changed
- Active workstreams shifted
- New important artifacts were created (add to file map)

## Example Usage

User: "Draft a proposal for Brex on expanding our tools engagement"

1. Load `agent-docs/client-work-agent.md`
2. Load `clients/brex/brex-client-context-v1.md`
3. From file map, load Current Strategy files (strategy document, current state assessment)
4. Review engagement history for context on how the relationship has evolved
5. Confirm scope and audience with user
6. Draft and save to `clients/brex/deliverables/[project-name]/proposal-name-v1.md`
