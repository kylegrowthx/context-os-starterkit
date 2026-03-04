# GitHub Teams & Permissions Proposal for GrowthX

<metadata>
purpose: Concrete team structure and permission mapping for adding the whole company to GitHub
audience: Marcel, Daniel, IT/DevOps
related: knowledge/building/github-org-access-study-guide-v1.md, docs/epd/github-repos-v1.md
domain: engineering, operations
confidence: high
access: founders
last_updated: 2026-03-02
</metadata>

> **Context:** GrowthX has ~96 people (targeting 135), ~100 repos in the `growthxai` org, and needs to bring the whole company into GitHub while protecting sensitive repos (exec transcripts, 1:1s, board materials) from broad access. Staying in one org. This document maps every department and role to specific GitHub teams with exact permissions.

---

## The Problem We're Solving

Today the GitHub org is mostly engineers. As the company grows, we need:

1. **Founders-only repos** for exec meeting transcripts, 1:1 notes, board materials, and strategic planning docs that even senior engineers shouldn't see.
2. **Eng-admin access** for a handful of trusted DevOps/senior engineers (Jacopo, Stefano, Clint, Marcus) who need Admin on infrastructure repos without being org Owners.
3. **Lane-specific write access** so product engineers can push to Atlas but not accidentally break Output configs, and vice versa.
4. **Company-wide read access** to the handbook, docs, and non-sensitive repos so delivery, marketing, sales, and ops can file issues, review content, and discover knowledge.
5. **No leakage** — a marketing hire shouldn't be able to browse production deploy secrets or founder strategy docs.

---

## Org-Level Settings (Do First)

Before creating any teams, configure these org-wide settings:

| Setting | Value | Why |
|---------|-------|-----|
| Base member permissions | **No permission** | Members see nothing unless granted via team. This is the foundation. |
| Repo creation | **Owners only** (or Owners + eng-admin via custom org role) | Prevent repo sprawl. New repos go through a gatekeeper. |
| 2FA requirement | **Required** | Table stakes for any org with production code. |
| Default repo visibility | **Private** | New repos start private. Explicitly make public only for open-source. |
| Fork policy | **Private forks only** (or disabled for sensitive repos) | Prevents code from leaking via forks. |
| Outside collaborator access | **Require admin approval** | Freelancers/contractors can't be added without review. |

---

## Complete Team Structure

### Tier 0: Org Owners

**Not a team — this is the GitHub Owner org role.**

| Who | Why |
|-----|-----|
| Marcel (CEO) | Org-level decisions, billing, sensitive repos |
| Daniel (CTO) | Engineering oversight, org settings |
| IT Lead (Yousef) | Day-to-day admin, provisioning, offboarding |

Three people. That's it. Owners can see everything, including secret teams and all private repos. Keep this list as small as possible.

---

### Tier 1: Secret Teams (Invisible to Non-Members)

#### `@growthxai/founders`

| | |
|---|---|
| **Type** | Secret |
| **Members** | Marcel, Daniel |
| **Purpose** | Founder-only sensitive repos |
| **Repo access** | Admin on: `exec-transcripts`, `founders-private`, `1-on-1-notes`, `board-materials`, `strategic-planning` |
| **Why secret** | These repos shouldn't even appear in anyone else's repo list |

#### `@growthxai/eng-admin`

| | |
|---|---|
| **Type** | Secret |
| **Members** | Jacopo, Stefano, Clint, Marcus, Marcel, Daniel |
| **Purpose** | DevOps / infrastructure / "break glass" access |
| **Repo access** | Admin on ALL repos **except** Tier 0 founder-private repos |
| **Why secret** | Standard DevOps pattern. Prevents "why do they have admin and I don't" questions. Engineers understand this. |

**Key distinction:** Eng-admin members are NOT org Owners. They can't change org settings, manage billing, or see the `@growthxai/founders` team. But they have Admin on every engineering and infrastructure repo.

---

### Tier 2: Engineering Teams (Visible, Nested)

#### `@growthxai/engineering` (Parent Team)

| | |
|---|---|
| **Type** | Visible |
| **Members** | All engineers (~25-30 people across all lanes) |
| **Purpose** | Innersource read access across all product repos |
| **Repo access** | **Read** on all Tier 2 (product/eng) repos |
| **Nesting** | Parent of all sub-teams below |

This parent team gives every engineer visibility into every product codebase — they can browse, clone, and learn, but can't push. Write access comes from their lane-specific sub-team.

#### `@growthxai/product-eng` (Child of engineering)

| | |
|---|---|
| **Members** | Engineers building Atlas, Flow, Flow Studio, CheckThat |
| **Repo access** | **Write** on: `atlas`, `flow`, `flow-studio`, `checkthat-*` (all CheckThat repos) |
| **Maps to** | EPD → Product Lane (Shape Up methodology) |

#### `@growthxai/client-ops-eng` (Child of engineering)

| | |
|---|---|
| **Members** | Forward-deployed engineers (FDEs) and client ops engineers |
| **Repo access** | **Write** on: client pipeline repos, agentic workflow repos, workspace configs |
| **Maps to** | EPD → Client Ops Eng Lane |

#### `@growthxai/ai-infra` (Child of engineering)

| | |
|---|---|
| **Members** | Output / AI framework team |
| **Repo access** | **Write** on: `output-*` repos, `output_workflows-rails`, `output-claude-plugins`, AI infrastructure repos |
| **Maps to** | EPD → AI Infra Lane |

#### `@growthxai/website-eng` (Child of engineering)

| | |
|---|---|
| **Members** | Engineers working on growthx.ai site |
| **Repo access** | **Write** on: website frontend (Next.js), strapi, `assets-redirect` |
| **Maps to** | Website team within EPD |

#### `@growthxai/design` (Child of engineering)

| | |
|---|---|
| **Members** | Designers |
| **Repo access** | **Write** on: design system repos, website frontend, component library |
| **Maps to** | EPD → Design |

---

### Tier 3: Non-Engineering Teams (Visible)

These teams bring the rest of the company into GitHub with appropriate read-only access. The key principle: they can see, file issues, and comment — but they can't push code.

#### `@growthxai/delivery`

| | |
|---|---|
| **Members** | EMs, Editors, Directors, SEO specialists, CCO, COO |
| **Repo access** | **Read** on: `handbook`, docs repos, `context-os-starterkit`, content-related repos |
| **Triage** on: product repos they file bugs against (Atlas, Flow) |
| **Purpose** | File issues, review docs, see client-facing product repos |
| **Size** | Largest team (~40-50 people) |

#### `@growthxai/sales`

| | |
|---|---|
| **Members** | VP Sales, AEs, SDRs |
| **Repo access** | **Read** on: `handbook`, `checkthat-*` (public-facing repos), marketing site |
| **Purpose** | Understand the product, file feature requests, reference docs in sales calls |

#### `@growthxai/marketing`

| | |
|---|---|
| **Members** | VP Marketing, content marketers, community, growth |
| **Repo access** | **Read** on: `handbook`, website repos, blog/content repos |
| **Triage** on: website repos (file issues for website updates) |
| **Purpose** | Content updates, website change requests, blog management |

#### `@growthxai/ops-finance`

| | |
|---|---|
| **Members** | Strategic Finance, Ops, HR/People |
| **Repo access** | **Read** on: `handbook` only |
| **Purpose** | Minimal access. These roles don't need code repos. |

#### `@growthxai/leadership`

| | |
|---|---|
| **Members** | CXOs, VPs, Heads of departments |
| **Repo access** | **Read** on: `handbook`, product repos, strategy repos |
| **Purpose** | Visibility into product progress without write access |
| **Note** | This is a visible team. It does NOT overlap with the secret `founders` team (which has its own private repos). |

---

### Special-Purpose Teams

#### `@growthxai/security`

| | |
|---|---|
| **Members** | IT lead + 1-2 designated security contacts |
| **GitHub role** | Assign the **Security Manager** org role |
| **Access** | Read on ALL repos + security alert visibility |
| **Purpose** | Triage Dependabot alerts, secret scanning, vulnerability management |
| **Why separate** | Security needs broad read access without Admin. The built-in Security Manager role is purpose-built for this. |

#### `@growthxai/contractors`

| | |
|---|---|
| **Type** | Not a team — use Outside Collaborator role |
| **Access** | Per-repo, granted case by case, requires admin approval |
| **Purpose** | Freelancers, external consultants, agency partners |
| **Rule** | Contractors never become org Members. They get invited to specific repos only. Access reviewed monthly. |

---

## Repo Classification Map

Every repo gets classified into a tier. Here's how each tier maps to team access:

| Tier | Visibility | founders | eng-admin | engineering | Sub-team | delivery | sales | marketing | ops |
|------|-----------|----------|-----------|-------------|----------|----------|-------|-----------|-----|
| **0: Founder-Private** | Private | Admin | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **1: Infrastructure** | Private | — | Admin | Read | — | ❌ | ❌ | ❌ | ❌ |
| **2: Product Code** | Private | — | Admin | Read | Write | ❌ | ❌ | ❌ | ❌ |
| **3: Handbook / Docs** | Private | — | Admin | Read | — | Read | Read | Read | Read |
| **4: Client-Facing** | Private | — | Admin | Read | Write | Read | Read | Read | ❌ |
| **5: Public / OSS** | Public | — | Admin | Write | Write | Read | Read | Read | Read |

### Example Repo Assignments

**Tier 0 — Founder-Private:**
`exec-transcripts`, `board-materials`, `founders-private`, `1-on-1-notes`, `strategic-planning`

**Tier 1 — Infrastructure:**
`terraform-*`, `deploy-configs`, `secrets-management`, `ci-cd-pipelines`, `.github` (org-level config)

**Tier 2 — Product Code:**
`flow`, `flow-studio`, `atlas`, `output-*`, `checkthat-backend`, `checkthat-frontend`, `checkthat-data`

**Tier 3 — Handbook / Docs:**
`handbook`, `context-os-starterkit`, `growthx-docs`, internal knowledge repos

**Tier 4 — Client-Facing:**
`starter`, client workspace templates, demo repos, API SDKs (`output_workflows-rails`)

**Tier 5 — Public / OSS:**
`context-os-starterkit` (already public), `output-claude-plugins`, any open-sourced tools, `checkthat` (if/when open-sourced)

---

## How This Maps to Your Existing Org Structure

From the GrowthX accountability chart (EOS):

```
CEO (Marcel) ──────────────────────── Org Owner + @founders
│
├── Sales (VP Sales)
│   └── AEs, SDRs ─────────────────── @sales (Read on handbook + CheckThat)
│
├── Customer Success (CCO)
│   └── EMs ────────────────────────── @delivery (Read on handbook + product)
│
├── Delivery (COO)
│   └── Editors, Production ────────── @delivery
│   └── FDEs ───────────────────────── @client-ops-eng (Write) + @delivery (via dual membership)
│   └── SEO Specialists ───────────── @delivery
│   └── Design/Dev (delivery) ──────── @design or @website-eng
│
├── Product/Engineering (CTO) ──────── Org Owner + @founders + @eng-admin
│   └── Product Eng ────────────────── @product-eng (Write on Atlas/Flow/CheckThat)
│   └── Client Ops Eng ────────────── @client-ops-eng (Write on workflows)
│   └── AI Infra ──────────────────── @ai-infra (Write on Output repos)
│   └── Website ───────────────────── @website-eng (Write on site repos)
│   └── Design ────────────────────── @design (Write on design system)
│
├── Marketing (VP Marketing)
│   └── Content, Community, Growth ── @marketing (Read + Triage on website)
│
└── Finance (Strategic Finance)
    └── Ops ────────────────────────── @ops-finance (Read on handbook only)
```

---

## Handling Edge Cases

### FDEs (Forward-Deployed Engineers)

FDEs sit between delivery and engineering. They're engineers who work embedded with client pods. They should be in:
- `@growthxai/engineering` (parent, for innersource Read)
- `@growthxai/client-ops-eng` (for Write on their repos)
- Optionally `@growthxai/delivery` (for visibility into delivery docs)

Dual team membership is fine — permissions are additive. They get the union of both teams' access.

### Directors and Senior Strategists

Directors are delivery leadership. They need Read on product repos to understand what's being built for clients, but no Write access. The `@growthxai/delivery` team with Read on product repos covers this.

### New Hires in Onboarding

When someone joins:
1. Add them to `@growthxai/engineering` or the appropriate non-eng team
2. Add them to their lane-specific sub-team
3. They immediately get the right access — no manual per-repo grants

When someone leaves:
1. Remove from all teams (or SCIM handles it automatically)
2. Review and revoke any PATs or SSH keys

### CheckThat Spin-Off (Future)

Daniel mentioned if Output/CheckThat does well, it may spin off. When that happens:
- Create a new org (`checkthat-ai` or similar)
- Transfer CheckThat repos to the new org
- Keep cross-references via GitHub's repo redirect (transfer creates automatic redirect)
- The `@growthxai/product-eng` team scope shrinks; a new org team structure covers CheckThat

Don't do this now. Revisit when CheckThat hits $5M+ ARR and has its own engineering team.

### Public Repos and Stars

All public repos stay in `growthxai`. This preserves:
- Star counts and social proof
- Discoverability (people finding GrowthX through GitHub)
- Backlinks to the org from blog posts, READMEs, etc.

The `context-os-starterkit` (1 star), `output-claude-plugins`, `starter` — these all stay public under `growthxai`.

---

## Implementation Priority

| Step | What | Who | Time |
|------|------|-----|------|
| 1 | Configure org settings (base permissions, 2FA, repo creation policy) | Marcel + IT | 30 min |
| 2 | Audit all ~100 repos, classify by tier, archive dead repos | Yousef + Daniel | 1-2 hours |
| 3 | Create secret teams: `founders`, `eng-admin` | Marcel | 15 min |
| 4 | Create `engineering` parent team + sub-teams, assign members | Yousef | 1 hour |
| 5 | Create non-eng teams: `delivery`, `sales`, `marketing`, `ops-finance`, `leadership` | Yousef | 30 min |
| 6 | Assign repo access per tier model (the big one) | Yousef + eng-admin | 2-3 hours |
| 7 | Remove all individual user permissions (force through teams) | Yousef | 30 min |
| 8 | Set up org-level rulesets for branch protection | Eng-admin | 1 hour |
| 9 | Add CODEOWNERS to critical repos | Eng leads | 1 hour |
| 10 | Invite non-engineering staff to org, assign to teams | Yousef + People | 1 hour |
| 11 | Test: have one person from each tier verify access | Everyone | 30 min |
| 12 | Document in a `.github/profile/README.md` or internal wiki | Yousef | 30 min |

**Total estimated time: 8-10 hours** spread across 2-3 days.

---

## Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Someone accidentally gets access to founder-private repos | Low | High | Secret team + "No permission" base ensures these repos are invisible by default. Only Owners + founders team members see them. |
| Engineer pushes to wrong repo | Medium | Medium | Branch protection rulesets prevent direct pushes to main. CODEOWNERS require team-specific review. |
| Freelancer/contractor access lingers | Medium | Medium | Monthly audit of outside collaborators. Calendar reminder. |
| Too many Owners appointed over time | Medium | High | Hard rule: max 3-4 Owners. Document this policy. Custom org roles for delegated admin tasks. |
| Eng-admin member leaves company | Low | High | Immediate removal from team. Revoke PATs/SSH keys. SCIM automates if connected. |
| New repo created without proper team assignment | High | Low | Restrict repo creation to Owners. Create a "new repo checklist" in the `.github` repo. |
| Non-eng staff confused by GitHub | Medium | Low | Create a "GitHub for non-engineers" one-pager. Limit their interaction to issues and docs browsing. |

---

## Summary: All Teams at a Glance

| Team | Type | Size | Primary Access Level | Key Repos |
|------|------|------|---------------------|-----------|
| Org Owners | Org role | 3 | Everything | All |
| `@growthxai/founders` | Secret | 2 | Admin | Founder-private repos |
| `@growthxai/eng-admin` | Secret | 6 | Admin (almost all) | All except founder-private |
| `@growthxai/engineering` | Visible (parent) | ~25-30 | Read | All product repos |
| `@growthxai/product-eng` | Visible (child) | ~8-10 | Write | Atlas, Flow, CheckThat |
| `@growthxai/client-ops-eng` | Visible (child) | ~5-8 | Write | Client workflows, pipelines |
| `@growthxai/ai-infra` | Visible (child) | ~4-6 | Write | Output repos, AI infra |
| `@growthxai/website-eng` | Visible (child) | ~3-4 | Write | Website, Strapi |
| `@growthxai/design` | Visible (child) | ~3-4 | Write | Design system, website |
| `@growthxai/delivery` | Visible | ~40-50 | Read + Triage | Handbook, product repos |
| `@growthxai/sales` | Visible | ~5-8 | Read | Handbook, CheckThat |
| `@growthxai/marketing` | Visible | ~5-8 | Read + Triage | Handbook, website |
| `@growthxai/ops-finance` | Visible | ~5-8 | Read | Handbook only |
| `@growthxai/leadership` | Visible | ~8-10 | Read | Handbook, product repos |
| `@growthxai/security` | Security Manager role | 2-3 | Read (all) + security alerts | All |

**Total: 3 org owners, 2 secret teams, 1 parent eng team with 5 children, 5 non-eng teams, 1 security team.**

That's 14 teams to manage ~96 people across ~100 repos. Clean, auditable, and scalable to 300+.

---

## Sources

- [Roles in an Organization — GitHub Docs](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization)
- [About Teams — GitHub Docs](https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams)
- [Best Practices for Orgs and Teams — GitHub Blog](https://github.blog/enterprise-software/devops/best-practices-for-organizations-and-teams-using-github-enterprise-cloud/)
- [Best Practices for Managing Teams in GitHub Orgs — GitGuardian](https://blog.gitguardian.com/best-practices-for-managing-developer-teams-in-github-orgs/)
- [Managing Team Access to Repos — GitHub Docs](https://docs.github.com/articles/managing-team-access-to-an-organization-repository)
- [About Custom Repository Roles — GitHub Enterprise Cloud Docs](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/about-custom-repository-roles)
- [About Rulesets — GitHub Docs](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)
