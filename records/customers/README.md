# Customers (Archived)

<metadata>
purpose: Archive for past/inactive client engagements
audience: AI agents and team members referencing historical client work
summary: Archived client records. Active clients live in clients/ at the workspace root.
token_estimate: small
related: clients/README.md, records/transcripts/README.md, docs/context-routing.md
domain: records
confidence: canonical
context_tier: 3
last_updated: 2026-02-22
</metadata>

Archive for **past or inactive** client engagements. When a client engagement ends, move their directory here from `clients/`.

**Active clients live in `clients/` at the workspace root.** Do not create new client directories here.

## Directory Structure

```
records/customers/
  [client-name]/
    [client-name]-client-context-v1.md    # Overview and key context
    transcripts/                           # Client-specific meeting transcripts
      YYYY-MM-DD-meeting-description.md
```

## How to Use

1. **Search by client name** to find historical engagement context
2. **Start with the client context file** for an overview of the past engagement
3. **Search transcripts/ subdirectory** for specific meeting discussions
4. **Never bulk-load** — read files individually

## Adding a New Client

**Don't.** New clients go in `clients/` at the workspace root. Use the template at `clients/client-context-template-v1.md`.

When an engagement ends, move the client directory from `clients/` to `records/customers/`.
