# GrowthX Context

GrowthX's organizational knowledge base. Everything we know about how we work, who we serve, what we're building, and how we write -- codified for humans and AI agents.

---

## Why This Exists

1. **Onboarding takes too long.** New hires spend weeks absorbing tribal knowledge. This repository gets them productive faster.
2. **AI can't match our voice.** Generic AI output sounds generic. Feed it this context, and it writes like us.
3. **Knowledge lives in heads.** When people leave, knowledge leaves. This captures it.

The goal: anyone (human or AI) can understand GrowthX and produce on-brand work by reading this repository.

---

## Directory Map

```
growthx-context/
├── docs/                    # The GrowthX Handbook (company, business, delivery, EPD, finance)
├── knowledge/               # Study guides and learning materials
│   └── aeo/                 # AEO & AI Visibility knowledge hub (7 docs, 103 sources)
├── research/                # Research scratchpads and competitive intelligence
├── roles/                   # AI executive personas (9 roles)
├── writing-guidelines/      # Voice, tone, and style standards
├── personal-context/        # Founder context files
├── customers/               # Client documentation and transcripts
├── transcripts/             # Meeting transcripts (55+ files)
├── memos/                   # Strategic memos and vision docs
├── scratchpad/              # Work-in-progress documents
├── outputs/                 # Completed research deliverables
├── prompts/                 # Reusable AI prompt templates
├── scripts/                 # Utility scripts (Fireflies, Fathom)
├── sources/                 # People and sources indexes
├── downloads/               # External content archives (Lenny's Podcast)
├── public-docs/             # Public-facing documentation (CheckThat)
├── leadership-docs/         # Legacy leadership docs (migrated to docs/finance)
├── claude.md                # AI system context file
└── INDEX.md                 # Global sitemap of every directory and file
```

---

## Quick Start

### For Onboarding
1. [docs/start-here.md](docs/start-here.md) -- Your comprehensive onboarding guide
2. [docs/company/](docs/company/) -- Who we are (mission, vision, values)
3. [docs/business/](docs/business/) -- How we make money
4. [writing-guidelines/writing-style-context-v2.md](writing-guidelines/writing-style-context-v2.md) -- How we write

### For AI Content Generation
1. Load [claude.md](claude.md) as system context
2. Load [writing-guidelines/writing-style-context-v2.md](writing-guidelines/writing-style-context-v2.md)
3. Load relevant docs from [docs/](docs/) based on the task
4. Generate content

### For AEO & AI Visibility
Start at [knowledge/aeo/README.md](knowledge/aeo/README.md) -- the consolidated hub with guides, research, and 103 indexed sources.

### For AI Executive Personas
See [roles/README.md](roles/README.md) -- 9 AI personas from Performance Coach to CTO.

---

## Directory Overview

| Directory | What's There | README | INDEX |
|---|---|---|---|
| [docs/](docs/) | The GrowthX Handbook -- company, business, delivery, EPD, finance, products | [README](docs/README.md) | [INDEX](docs/INDEX.md) |
| [knowledge/](knowledge/) | Study guides (AEO, writing, operations, leadership, LinkedIn) | [README](knowledge/README.md) | [INDEX](knowledge/INDEX.md) |
| [research/](research/) | Research scratchpads, competitive briefs, databases | [README](research/README.md) | [INDEX](research/INDEX.md) |
| [roles/](roles/) | AI executive personas (9 roles + inner circle) | [README](roles/README.md) | [INDEX](roles/INDEX.md) |
| [writing-guidelines/](writing-guidelines/) | Voice, tone, style guide | [README](writing-guidelines/README.md) | [INDEX](writing-guidelines/INDEX.md) |
| [personal-context/](personal-context/) | Founder context files | [README](personal-context/README.md) | [INDEX](personal-context/INDEX.md) |
| [customers/](customers/) | Client docs and transcripts | [README](customers/README.md) | [INDEX](customers/INDEX.md) |
| [transcripts/](transcripts/) | Meeting transcripts (55+ files) | [README](transcripts/README.md) | [INDEX](transcripts/INDEX.md) |
| [memos/](memos/) | Strategic memos and vision docs | [README](memos/README.md) | [INDEX](memos/INDEX.md) |
| [scratchpad/](scratchpad/) | Work-in-progress documents | [README](scratchpad/README.md) | [INDEX](scratchpad/INDEX.md) |
| [outputs/](outputs/) | Completed research deliverables | [README](outputs/README.md) | [INDEX](outputs/INDEX.md) |
| [prompts/](prompts/) | Reusable AI prompt templates | [README](prompts/README.md) | [INDEX](prompts/INDEX.md) |
| [scripts/](scripts/) | Utility scripts | [README](scripts/README.md) | [INDEX](scripts/INDEX.md) |
| [sources/](sources/) | People and sources indexes | [README](sources/README.md) | [INDEX](sources/INDEX.md) |
| [downloads/](downloads/) | External content archives | [README](downloads/README.md) | [INDEX](downloads/INDEX.md) |
| [public-docs/](public-docs/) | Public-facing docs | -- | [index.md](public-docs/index.md) |
| [leadership-docs/](leadership-docs/) | Legacy (migrated to docs/finance) | [README](leadership-docs/README.md) | [INDEX](leadership-docs/INDEX.md) |

---

## Navigation

Every directory has:
- **README.md** -- Overview of what's in the directory and why it exists
- **INDEX.md** -- Complete file listing (sitemap) for the directory

For the full project sitemap, see [INDEX.md](INDEX.md).

---

## File Naming & Versioning

- **Format:** `descriptive-name-v1.md` (lowercase, hyphens, version suffix)
- **Minor updates:** Edit in place, update `last_updated` in header
- **Major changes:** Create new version (`-v2`), move old to `/archive`

---

**Last updated:** February 2026
