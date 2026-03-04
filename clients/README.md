# Clients

Active client accounts. Each client gets its own directory with all context, deliverables, transcripts, and resources needed to do work for them.

## Directory Convention

```
clients/[client-name]/
  [client-name]-client-context-v1.md   # Start here — relationship, history, file map
  context/                              # Brand guides, personas, reference docs
  deliverables/                         # Work product organized by project/phase
  transcripts/                          # Meeting transcripts
  resources/                            # Data, CSVs, competitive research
  examples/                             # Reference examples of their content
```

## How to Use

1. **Start with the client context file** — it contains the relationship context, engagement history, and a file map pointing to every other relevant file.
2. Load the `agent-docs/client-work-agent.md` config for any client deliverable task.
3. Load additional files from the file map based on what you're creating.

## Active Clients

| Client | Directory | Status |
|--------|-----------|--------|
| Brex | `clients/brex/` | Active |
| Daylight | `clients/daylight/` | Active |
| Vercel | `clients/vercel/` | Active |
