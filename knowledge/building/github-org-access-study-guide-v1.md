# GitHub Organization Access & Team Structure — Study Guide

<metadata>
purpose: Study guide for organizing a GitHub org with layered access, teams, and repo classification
audience: GrowthX founders and engineering leadership
related: docs/epd/github-repos-v1.md, docs/how-we-work/slack.md
domain: engineering, operations
confidence: high
last_updated: 2026-03-02
</metadata>

> **For:** Marcel, Daniel, and engineering leadership at GrowthX
> **Goal:** Design and implement a 4-layer access model for the GrowthX GitHub org (~100 repos) that keeps everything in one org while protecting sensitive repos (exec transcripts, 1:1s, founder-only content) from broad engineering access
> **Time Investment:** 2–3 hours to read, 4–8 hours to implement with Yousef
> **Last Updated:** 2026-03-02

---

## How to Use This Guide

This guide is structured in five parts. Parts 1–2 give you the conceptual foundation. Part 3 is the GrowthX-specific implementation plan — the section you'll actually execute from. Parts 4–5 cover security hardening and ongoing maintenance.

If you're short on time, read Part 3 and the Quick Reference in the appendix.

---

## Part 1: Foundations — How GitHub Access Actually Works

### The Three Layers of GitHub Permissions

GitHub's permission model operates across three layers, and understanding how they interact is the whole game.

**Layer 1: Organization roles** determine what someone can do at the org level — managing teams, creating repos, changing settings, viewing billing. The built-in roles are Owner (full control), Member (default, access determined by teams), Billing Manager (payment only), Moderator (member + community management), and Outside Collaborator (specific repo access only, not a full member). There's also a special Security Manager role that grants read access to ALL repos plus security alert visibility — useful for a dedicated security person but dangerous if assigned carelessly.

**Layer 2: Team memberships** are the primary mechanism for controlling who can access which repos. Teams can be given Read, Triage, Write, Maintain, or Admin access on a per-repo basis. This is where most of the day-to-day access management happens. Teams can be nested (child teams inherit parent permissions) and can be visible or secret (secret teams are only visible to their members and org owners).

**Layer 3: Repository roles** are the actual permission sets applied at the repo level. The hierarchy from least to most access: Read → Triage → Write → Maintain → Admin. Each level includes everything below it plus additional capabilities. Admin is the only level that can delete repos, manage branch protection, and change repo settings.

**The critical rule:** Permissions are additive. If someone gets Write from Team A and Admin from Team B on the same repo, they have Admin. There's no way to subtract permissions — you can only add. This means your team structure needs to be designed so that broader teams have lower permissions and narrower teams add higher permissions where needed.

### Key Concepts

**Base permissions** are the default access level every org member gets on every repo. Setting this to "No permission" means members can't see private repos unless explicitly granted access through a team. Setting it to "Read" enables innersource (everyone can browse and learn from all code). For GrowthX, "No permission" is the right default given the sensitive content planned for some repos.

**Nested teams** let you create hierarchy. If "Engineering" (parent) has Read on most repos, and "Product Engineering" (child) has Write on Atlas and Flow, then Product Engineering members get both Read on most repos AND Write on Atlas/Flow. The parent should only have permissions safe for every possible child member.

**Secret teams** are invisible to non-members and non-owners. They're perfect for the founders-only layer. Important limitation: secret teams cannot be nested. They must be standalone.

**Custom repository roles** (Enterprise Cloud feature) let you create up to 20 custom roles from 40+ fine-grained permissions. You pick a base role (Read, Write, Maintain, Admin) and add specific permissions on top. This is how you could create an "eng-admin" role that has nearly everything Admin has but without repo deletion.

**Custom organization roles** (also Enterprise Cloud) let you delegate org-level tasks — like managing teams, managing certain repos, or viewing audit logs — without granting full Owner access.

### Sources

- [Roles in an Organization — GitHub Docs](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization)
- [Repository Roles for an Organization — GitHub Docs](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization)
- [About Teams — GitHub Docs](https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams)
- [About Custom Repository Roles — GitHub Enterprise Cloud Docs](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/about-custom-repository-roles)

---

## Part 2: The Single-Org Decision (and Why It's Right)

### Why GrowthX Should Stay in One Org

GitHub's official guidance is to minimize the number of organizations. The benefits of staying single-org are significant for GrowthX specifically.

First, public repos for CheckThat and Output keep their stars, forks, and discoverability under the main GrowthX org — this matters for developer relations and community building. Splitting to a new org means losing that association or managing awkward cross-org references.

Second, CI/CD, GitHub Actions, secrets, webhooks, and integrations are all wired to the current org. Transferring repos to a new org breaks these connections and requires reconnecting everything — a multi-day effort with risk of downtime.

Third, @-mentions and cross-team collaboration only work within an org. Engineers in one org can't easily reference or discover work in another.

Fourth, under the same GitHub Enterprise account, you don't pay double for seats across orgs — but you do have to manage user provisioning in two places, which is operationally annoying.

The only reason to split would be if you needed fundamentally different visibility or access policies that can't be modeled with teams. Since GitHub's team + custom role system is expressive enough for GrowthX's needs (4 layers, sensitive repos excluded from broad access), one org works.

### When You Might Revisit This

Daniel's point about Output potentially spinning off is valid. If Output becomes a standalone product with its own engineering team, community, and release cycle, it may make sense to give it its own org at that point. But that's a future decision — for now, it lives as repos in the main org with its own team permissions.

### Sources

- [Best Practices for Organizations and Teams — GitHub Blog](https://github.blog/enterprise-software/devops/best-practices-for-organizations-and-teams-using-github-enterprise-cloud/)
- [Best Practices for Structuring Organizations — GitHub Enterprise Cloud Docs](https://docs.github.com/en/enterprise-cloud@latest/admin/user-management/managing-organizations-in-your-enterprise/best-practices-for-structuring-organizations-in-your-enterprise)

---

## Part 3: The GrowthX 4-Layer Access Model

This is the implementation plan. It maps directly to the conversation between Marcel and Daniel about needing "three layers" plus a secret founders layer on top.

### Layer Overview

```
┌─────────────────────────────────────────────────────────────┐
│  LAYER 1: Org Owners (Marcel, Daniel, IT lead)              │
│  ── Full org admin. Can see/do everything.                  │
│  ── Manages org settings, billing, team structure.          │
│  ── 2-3 people maximum.                                     │
├─────────────────────────────────────────────────────────────┤
│  LAYER 1.5: Founders (Secret Team)                          │
│  ── Marcel + Daniel only.                                   │
│  ── Admin on: exec-transcripts, founders-private, 1:1-notes │
│  ── These repos are invisible to everyone else.             │
├─────────────────────────────────────────────────────────────┤
│  LAYER 2: Eng-Admin / DevOps (Secret Team)                  │
│  ── Jacopo, Stefano, Clint, Marcus + founders.              │
│  ── Admin on nearly all repos (except founders-private).    │
│  ── Can manage branch protection, CI/CD, deployments.       │
│  ── Think of this as the "break glass" team.                │
├─────────────────────────────────────────────────────────────┤
│  LAYER 3: Engineering (Visible Parent Team)                 │
│  ── All engineers.                                          │
│  ── Write access on their lane's repos.                     │
│  ── Read access on shared repos.                            │
│  ── Nested sub-teams: product-eng, client-ops-eng, ai-infra │
├─────────────────────────────────────────────────────────────┤
│  LAYER 4: Non-Engineering (Visible Team)                    │
│  ── Ops, Marketing, Design, Content.                        │
│  ── Read access to website, docs, content repos.            │
│  ── No access to core product repos.                        │
│  ── Can create issues but not push code.                    │
└─────────────────────────────────────────────────────────────┘
```

### Detailed Team Structure

**Org Owners** (Layer 1)
- Members: Marcel, Daniel, IT lead (Yousef or equivalent)
- Purpose: Full org administration. This is the GitHub "Owner" role at the org level.
- Rule: Minimum 2, maximum 3-4 owners. Owners should have 2FA with hardware keys.

**@growthx/founders** (Layer 1.5 — Secret Team)
- Members: Marcel, Daniel
- Type: Secret (invisible to non-members/non-owners)
- Repo access: Admin on all founder-private repos
- Purpose: Exec meeting transcripts, 1:1 notes, board materials, sensitive strategy docs
- Note: Cannot be nested (secret team limitation). That's fine — it's standalone by design.

**@growthx/eng-admin** (Layer 2 — Secret Team)
- Members: Jacopo, Stefano, Clint, Marcus, Marcel, Daniel
- Type: Secret
- Repo access: Admin on all repos EXCEPT founder-private repos
- Purpose: Infrastructure management, CI/CD, deployment, branch protection, emergency access
- Why secret: Engineers are used to this pattern. It prevents confusion about who has elevated access and avoids "why do they have admin and I don't" conversations.
- Note: Also cannot be nested. Standalone is correct here too.

**@growthx/engineering** (Layer 3 — Visible Parent Team)
- Members: All engineers
- Type: Visible
- Repo access: Read on all non-sensitive repos (base level)
- Purpose: Innersource visibility, cross-team awareness
- Child teams (nested under engineering):

  **@growthx/product-eng**
  - Members: Engineers on Atlas, Flow, Flow Studio, CheckThat
  - Repo access: Write on product repos (atlas, flow, flow-studio, checkthat-*)

  **@growthx/client-ops-eng**
  - Members: Forward-deployed engineers
  - Repo access: Write on client workflow repos, agentic pipeline repos

  **@growthx/ai-infra**
  - Members: Output / AI framework team
  - Repo access: Write on output-*, ai-infra repos

  **@growthx/website**
  - Members: Engineers working on growthx.com
  - Repo access: Write on website frontend, strapi

**@growthx/non-engineering** (Layer 4 — Visible Team)
- Members: Ops, marketing, design, content, delivery
- Type: Visible
- Repo access: Read on website, docs, content-related repos. No access to product code repos.
- Purpose: File issues, review content, access design assets
- Optional child teams: @growthx/design, @growthx/content, @growthx/ops

### Repo Classification

Every repo should be classified into one of four tiers. This determines which teams get access and at what level.

**Tier A — Founder-Private** (🔴 Most restricted)
- Examples: exec-transcripts, founders-private, board-materials, 1-on-1-notes
- Visibility: Private
- Access: @growthx/founders (Admin) + Org Owners only
- Branch protection: Require PR review from another founder
- Who can create: Org Owners only

**Tier B — Infrastructure / Sensitive** (🟠 Restricted)
- Examples: deploy configs, secrets management, CI/CD pipelines, terraform, production env configs
- Visibility: Private
- Access: @growthx/eng-admin (Admin), @growthx/engineering (Read)
- Branch protection: Require review from eng-admin member
- Who can create: Eng-admin team

**Tier C — Product / Engineering** (🟡 Standard)
- Examples: flow, atlas, flow-studio, checkthat-*, output-*, client pipelines, website
- Visibility: Private (or Internal if using Enterprise — visible to all org members)
- Access: Relevant sub-team (Write), @growthx/engineering parent (Read), @growthx/eng-admin (Admin)
- Branch protection: Require 1 reviewer, require CI pass
- Who can create: Engineering team leads

**Tier D — Public / Open Source** (🟢 Open)
- Examples: checkthat (if open-sourced), blog posts, documentation, open-source tools
- Visibility: Public
- Access: @growthx/engineering (Write), everyone else (Read via public)
- Branch protection: Require 2 reviewers, require CI pass, require CODEOWNERS review
- Who can create: Team leads with Owner approval

### Implementation Checklist

Here's the step-by-step for Yousef (or whoever implements this):

**Phase 1: Prep (1 hour)**
1. Audit all ~100 repos. Spreadsheet with columns: repo name, current visibility, current access, proposed tier (A/B/C/D), proposed team(s)
2. Identify which repos are actively used vs archived/dead. Archive dead repos.
3. Document current CI/CD integrations per repo (GitHub Actions, webhooks, deploy keys)

**Phase 2: Org Settings (30 min)**
1. Set base member permissions to "No permission"
2. Restrict repo creation to Owners only (or Owners + specific teams)
3. Require 2FA for all org members
4. Enable secret scanning and Dependabot alerts org-wide
5. Review and clean up outside collaborators

**Phase 3: Create Teams (1 hour)**
1. Create secret team: @growthx/founders → add Marcel, Daniel
2. Create secret team: @growthx/eng-admin → add Jacopo, Stefano, Clint, Marcus, Marcel, Daniel
3. Create visible team: @growthx/engineering → add all engineers
4. Create child teams under engineering: product-eng, client-ops-eng, ai-infra, website
5. Create visible team: @growthx/non-engineering → add non-eng staff
6. Optional: create child teams under non-engineering as needed

**Phase 4: Assign Repo Access (2-3 hours)**
1. For each Tier A repo: grant @growthx/founders Admin. Confirm no other teams have access.
2. For each Tier B repo: grant @growthx/eng-admin Admin, @growthx/engineering Read
3. For each Tier C repo: grant relevant sub-team Write, @growthx/engineering Read, @growthx/eng-admin Admin
4. For each Tier D repo: grant @growthx/engineering Write, confirm public visibility
5. Remove all individual user permissions — access should flow through teams only

**Phase 5: Branch Protection & Rulesets (1-2 hours)**
1. Create org-level rulesets for common patterns (require PR, require CI, block force push)
2. Apply Tier A ruleset to founder-private repos
3. Apply standard ruleset to all Tier C repos
4. Set up CODEOWNERS files in critical repos
5. Use "evaluate" mode first, then switch to "active" after confirming expected behavior

**Phase 6: Verify & Document (1 hour)**
1. Have one person from each layer verify they can/can't access what they should/shouldn't
2. Document the team structure and tier model in a README in a `.github` repo or internal wiki
3. Set a calendar reminder to audit access quarterly

### Sources

- [Managing Team Access to an Organization Repository — GitHub Docs](https://docs.github.com/articles/managing-team-access-to-an-organization-repository)
- [About Custom Repository Roles — GitHub Enterprise Cloud Docs](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/about-custom-repository-roles)
- [Best Practices for Managing Teams in GitHub Orgs — GitGuardian](https://blog.gitguardian.com/best-practices-for-managing-developer-teams-in-github-orgs/)
- [Use Teams, Roles, and Users to Manage Repository Access — GitHub](https://resources.github.com/learn/pathways/administration-governance/essentials/use-teams-roles-users-to-manage-repository-access/)

---

## Part 4: Security Hardening

### Branch Protection & Rulesets

GitHub recently introduced **rulesets** as the successor to branch protection rules. The key advantage: rulesets can be defined at the org level and applied across multiple repos, and multiple rulesets can stack on the same branch. Branch protection rules are per-repo and only one can apply at a time.

For GrowthX, create three org-level rulesets:

**Ruleset: "Standard"** — Apply to all Tier C and D repos
- Require pull request before merge (1 approval minimum)
- Require status checks to pass (CI/CD)
- Block force pushes
- Block branch deletion on main/production

**Ruleset: "Sensitive"** — Apply to Tier B repos
- Everything in Standard, plus:
- Require 2 approvals
- Require review from @growthx/eng-admin
- Require signed commits

**Ruleset: "Founder-Private"** — Apply to Tier A repos
- Require pull request before merge (1 approval from @growthx/founders)
- Block force pushes
- Restrict who can push: @growthx/founders only

Start all rulesets in "evaluate" mode to test without blocking anyone, then switch to "active" once confirmed.

### CODEOWNERS

Create a `CODEOWNERS` file in the `.github/` directory of critical repos. This ensures the right people must review changes to sensitive files.

Example for a product repo:
```
# Default owners
* @growthx/product-eng

# Infrastructure files require eng-admin review
Dockerfile @growthx/eng-admin
docker-compose.yml @growthx/eng-admin
.github/ @growthx/eng-admin
terraform/ @growthx/eng-admin

# Deployment configs
deploy/ @growthx/eng-admin
```

### Additional Security Measures

**2FA enforcement**: Require 2FA for all org members. This is table stakes. Anyone who doesn't enable 2FA within a grace period gets removed from the org automatically.

**SAML SSO + SCIM** (if on Enterprise Cloud): Connect your identity provider. SCIM automates provisioning — when someone leaves the company, removing them from your IdP automatically removes their GitHub access. Without SCIM, removing someone from your SAML provider only logs them out of the web session; their SSH keys and tokens remain active.

**Secret scanning**: Enable across all repos. GitHub will alert you if anyone accidentally commits API keys, tokens, or passwords.

**Dependabot**: Enable security alerts and automated PRs for dependency vulnerabilities.

**Audit log streaming**: GitHub retains audit logs for 90 days. If you need longer retention for compliance, stream logs to an external service (Datadog, Splunk, AWS S3).

### Sources

- [About Rulesets — GitHub Docs](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)
- [Rulesets Best Practices — GitHub Well-Architected](https://wellarchitected.github.com/library/governance/recommendations/managing-repositories-at-scale/rulesets-best-practices/)
- [About Code Owners — GitHub Docs](https://docs.github.com/articles/about-code-owners)
- [Securing GitHub Organizations — Medium](https://medium.com/@anshumaansingh10jan/how-to-secure-and-configure-github-organizations-for-optimal-security-5fbc43bc4f1d)

---

## Part 5: Ongoing Maintenance

### Quarterly Access Review

Set a recurring calendar event. Every quarter:

1. Review org member list. Remove anyone who's left the company or changed roles.
2. Review each team's membership. Are the right people in the right teams?
3. Review outside collaborator access. Any freelancers who no longer need access?
4. Check for repos with individual user permissions (should be zero — all access through teams).
5. Review audit log for unusual activity (unexpected admin actions, repo deletions, permission changes).

### When Someone Joins

New engineers: Add to @growthx/engineering, then add to the relevant sub-team (product-eng, client-ops-eng, ai-infra, or website). They automatically inherit Read on all engineering repos plus Write on their lane's repos.

New non-engineering: Add to @growthx/non-engineering (and relevant child team if they exist). They get Read on content/docs repos.

Promotion to eng-admin: Add to @growthx/eng-admin. They get Admin on nearly all repos. This should require approval from an existing Owner.

### When Someone Leaves

Remove from all teams. If using SCIM, this happens automatically when they're deprovisioned from your IdP. If not using SCIM, manually remove them and also revoke any personal access tokens and SSH keys associated with their account.

### When a New Repo is Created

1. Classify it into a tier (A/B/C/D)
2. Set visibility (private for A/B/C, public for D)
3. Assign team access according to the tier model
4. Apply the appropriate org-level ruleset
5. Add CODEOWNERS file if the repo has infrastructure or deployment code

### Common Pitfalls to Avoid

**Don't grant individual user access to repos.** Always go through teams. Individual permissions are invisible in team audits and create shadow access that's hard to track.

**Don't make too many people Owners.** Three is ideal. Four is the max. Every Owner can see and do everything, including accessing founder-private repos.

**Don't set base permissions to Read or Write.** With sensitive content in the org, "No permission" is the right default. Let teams grant access explicitly.

**Don't forget about GitHub Apps and tokens.** Personal access tokens (classic) inherit the user's permissions. Fine-grained PATs can be scoped to specific repos. Audit which tokens and GitHub Apps have access to sensitive repos.

**Don't skip the repo audit.** Of ~100 repos, a meaningful number are probably dead. Archive them. It reduces the surface area and makes the access matrix simpler.

### Sources

- [Everything You Wanted to Know about GitHub Access Control — ConductorOne](https://www.conductorone.com/guides/everything_you_wanted_to_know_about_github_access_control/)
- [GitHub Security Best Practices — Rewind](https://rewind.com/blog/top-github-compliance-concerns/)

---

## Appendix A: Quick Reference — The 4-Layer Model

| Layer | Team Name | Type | Members | Default Repo Access | Sees Founder Repos? |
|-------|-----------|------|---------|---------------------|---------------------|
| 1 | Org Owners | Org role | Marcel, Daniel, IT lead | Everything (Admin) | Yes |
| 1.5 | @growthx/founders | Secret team | Marcel, Daniel | Admin on Tier A repos | Yes (they own them) |
| 2 | @growthx/eng-admin | Secret team | Jacopo, Stefano, Clint, Marcus + founders | Admin on all except Tier A | No |
| 3 | @growthx/engineering | Visible parent | All engineers | Read on Tier C/D repos | No |
| 3.x | @growthx/product-eng etc. | Visible child | Lane-specific engineers | Write on lane repos | No |
| 4 | @growthx/non-engineering | Visible team | Ops, design, content | Read on select repos | No |

## Appendix B: Repo Tier Cheat Sheet

| Tier | Color | Visibility | Who Has Access | Example Repos |
|------|-------|-----------|----------------|---------------|
| A | 🔴 | Private | Founders + Owners only | exec-transcripts, board-materials |
| B | 🟠 | Private | Eng-admin (Admin), Engineering (Read) | terraform, deploy-configs, secrets |
| C | 🟡 | Private | Sub-team (Write), Engineering (Read), Eng-admin (Admin) | flow, atlas, website, output |
| D | 🟢 | Public | Engineering (Write), Public (Read) | open-source tools, docs |

## Appendix C: GitHub Permission Level Reference

| Repo Role | Can View | Can Triage Issues | Can Push Code | Can Manage Settings | Can Delete Repo |
|-----------|----------|-------------------|---------------|---------------------|-----------------|
| Read | ✅ | ❌ | ❌ | ❌ | ❌ |
| Triage | ✅ | ✅ | ❌ | ❌ | ❌ |
| Write | ✅ | ✅ | ✅ | ❌ | ❌ |
| Maintain | ✅ | ✅ | ✅ | ✅ (limited) | ❌ |
| Admin | ✅ | ✅ | ✅ | ✅ | ✅ |

## Appendix D: Implementation Timeline

| Phase | Task | Time | Who |
|-------|------|------|-----|
| 1 | Audit all repos, classify into tiers | 1 hour | Yousef + Daniel |
| 2 | Configure org settings (base permissions, 2FA, security) | 30 min | Marcel or IT lead |
| 3 | Create all teams, add members | 1 hour | Yousef |
| 4 | Assign repo access per tier model | 2-3 hours | Yousef |
| 5 | Set up rulesets and CODEOWNERS | 1-2 hours | Eng-admin member |
| 6 | Verify access, document, communicate | 1 hour | Marcel + Yousef |
| **Total** | | **6-8 hours** | |

## Appendix E: Curated Source Library

### Official GitHub Documentation
- [Roles in an Organization](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization)
- [Repository Roles for an Organization](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization)
- [About Teams](https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams)
- [About Rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)
- [About Code Owners](https://docs.github.com/articles/about-code-owners)
- [About Custom Repository Roles](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/about-custom-repository-roles)
- [About Custom Organization Roles](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-peoples-access-to-your-organization-with-roles/about-custom-organization-roles)
- [Best Practices for Structuring Organizations](https://docs.github.com/en/enterprise-cloud@latest/admin/user-management/managing-organizations-in-your-enterprise/best-practices-for-structuring-organizations-in-your-enterprise)
- [Managing Team Access to Repos](https://docs.github.com/articles/managing-team-access-to-an-organization-repository)

### GitHub Blog & Well-Architected
- [Best Practices for Orgs and Teams — GitHub Blog](https://github.blog/enterprise-software/devops/best-practices-for-organizations-and-teams-using-github-enterprise-cloud/)
- [Rulesets Best Practices — GitHub Well-Architected](https://wellarchitected.github.com/library/governance/recommendations/managing-repositories-at-scale/rulesets-best-practices/)
- [Required Review by Specific Teams in Rulesets — GitHub Changelog (Nov 2025)](https://github.blog/changelog/2025-11-03-required-review-by-specific-teams-now-available-in-rulesets/)

### Third-Party Guides
- [Best Practices for Managing Teams in GitHub Orgs — GitGuardian](https://blog.gitguardian.com/best-practices-for-managing-developer-teams-in-github-orgs/)
- [Everything You Wanted to Know about GitHub Access Control — ConductorOne](https://www.conductorone.com/guides/everything_you_wanted_to_know_about_github_access_control/)
- [Securing GitHub Organizations — Anshumaan Singh](https://medium.com/@anshumaansingh10jan/how-to-secure-and-configure-github-organizations-for-optimal-security-5fbc43bc4f1d)
- [Structuring GitHub Enterprise — DEV Community](https://dev.to/this-is-learning/structuring-github-enterprise-best-practices-from-the-org-level-down-45i5)
- [GitHub Configuration Checklist for SOC 2 — Delve](https://delve.co/blog/github-configuration-checklist-for-soc-2-compliance)
- [Use Teams, Roles, and Users to Manage Repository Access — GitHub Resources](https://resources.github.com/learn/pathways/administration-governance/essentials/use-teams-roles-users-to-manage-repository-access/)
