# GrowthX Docs

Company documentation split into three areas: the auto-synced handbook, private internal docs, and archived content.

---

## Structure

```
docs/
├── handbook/           ← Auto-synced from handbook.growthx.ai
│   ├── company/        ← Who we are
│   ├── how-we-work/    ← Communication & tools
│   ├── delivery/       ← Client operations
│   ├── epd/            ← Engineering, Product, Design
│   ├── people/         ← HR & careers
│   ├── products/       ← CheckThat, ContentOS, Output
│   ├── systems/        ← Tools & platforms
│   ├── guides/         ← AI, writing, marketing, skills
│   └── tutorials/      ← Step-by-step walkthroughs
│
├── private-docs/       ← Content NOT in the handbook
│   ├── business/       ← Business model, ICP, economics
│   ├── finance/        ← Board meetings, fiscal plans
│   ├── sales/          ← Pre-sales (placeholder)
│   └── ...             ← Other unique-to-context files
│
└── archive/            ← Superseded docs, pre-sync backups
    └── pre-handbook-sync/  ← Originals replaced by handbook
```

---

## How to Navigate

| If you want to understand... | Look here |
|------------------------------|-----------|
| Company, culture, how we work | `handbook/` |
| Guides on AI, writing, marketing | `handbook/guides/` |
| Our products (CheckThat, etc.) | `handbook/products/` |
| Client delivery processes | `handbook/delivery/` |
| Engineering & product development | `handbook/epd/` |
| Tools and systems we use | `handbook/systems/` |
| Financial plans, board meetings | `private-docs/finance/` |
| Business model, ICP | `private-docs/business/` |
| Job specs, onboarding details | `private-docs/people/` |
| Older versions of docs | `archive/` |

---

## Handbook Sync

The `handbook/` directory is automatically synced from the [GrowthX Handbook](https://handbook.growthx.ai) using the `sync-handbook` skill.

- **Do not edit** files in `handbook/` directly — they will be overwritten
- **To update**: edit the source in growthx-handbook, then run the sync
- **New private content** goes to `private-docs/`, not `handbook/`

To sync:

```bash
python3 .cursor/skills/sync-handbook/scripts/sync-handbook.py \
  --handbook-path "/path/to/growthx-handbook" \
  --context-path "/path/to/growthx-context"
```

---

## Access

**Default access:** `build-team`
**Contains restricted content:** Yes — `private-docs/finance/` is `founders`/`inner-circle`

---

**Last updated:** March 2026
