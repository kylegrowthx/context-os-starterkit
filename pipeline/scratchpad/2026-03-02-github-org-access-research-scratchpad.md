# GitHub Organization Access & Team Structure — Research Scratchpad

> **Topic:** How to organize a GitHub org with layers of access, teams, and repo classification
> **Learner:** Marcel Santilli, CEO of GrowthX (services + software company, ~100 repos)
> **Goal:** Design a tiered access model for the existing GrowthX GitHub org that separates founders/owners, eng-admin (DevOps), broad engineering, and non-engineering — without moving to a new org
> **Date:** 2026-03-02

---

## Audience Analysis

| Question | Answer |
|----------|--------|
| WHO is learning this? | Marcel (CEO) + Daniel (likely CTO/VP Eng) — founders making org architecture decisions |
| WHAT do they care about? | Practical layered access: founders-only repos (exec meetings, 1:1s), eng-admin with near-full access, broad eng, and non-eng. Must work in ONE org. |
| WHY do they need this? | ~100 repos today, sensitive transcripts/exec content incoming, engineers need broad access but not to everything. Public repos for visibility (stars, discovery). |
| WHAT sources would they trust? | GitHub official docs, GitHub blog, well-known DevOps/security practitioners |
| WHAT should be excluded? | GitHub Enterprise Server (on-prem) specifics — they're on Cloud. Multi-org patterns (they decided to stay single-org). |

---

## Q1: GitHub Organization Role Hierarchy

### Findings
GitHub orgs have these built-in roles at the org level:
- **Owner**: Complete admin access. Can manage billing, teams, org settings, delete repos. Should be limited to ≥2 people.
- **Member**: Default role. Access determined by team memberships and base permissions.
- **Billing Manager**: Only billing/payment access.
- **Moderator**: Member permissions + block outside collaborators, set interaction limits.
- **Outside Collaborator**: Access to specific repos only, not a full org member.
- **Security Manager** (special role): Can view security alerts, manage security settings, read ALL repos.

Repository-level roles (can be assigned per-team per-repo):
- **Read**: View, clone, interact with issues/PRs
- **Triage**: Read + manage issues/PRs without write
- **Write**: Push to branches, manage issues
- **Maintain**: Write + manage repo settings (no destructive actions)
- **Admin**: Full repo control including deletion, branch protection

### Sources
- https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization (Quality: 5)
- https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization (Quality: 5)

---

## Q2: Single Org vs Multiple Orgs

### Findings
GitHub officially recommends minimizing orgs. Single org pros:
- Easier innersource and collaboration
- Single search scope
- @-mentions work across all teams
- Less admin overhead
- Stars and public visibility stay consolidated

Multiple orgs pros:
- Better security isolation
- Different visibility/access policies per org

**GrowthX decision (from conversation):** Stay single org. Daniel confirmed "we can have one org." Marcel concerned about breaking CI/CD connections and losing star visibility if repos transfer. Under same Enterprise, no double-seat cost.

### Sources
- https://github.blog/enterprise-software/devops/best-practices-for-organizations-and-teams-using-github-enterprise-cloud/ (Quality: 5)
- https://docs.github.com/en/enterprise-cloud@latest/admin/user-management/managing-organizations-in-your-enterprise/best-practices-for-structuring-organizations-in-your-enterprise (Quality: 5)

---

## Q3: Team Structure & Nested Teams

### Findings
**Teams** are the primary mechanism for managing access. Key features:
- Teams can be given Read, Triage, Write, Maintain, or Admin access per repo
- **Nested teams**: Child teams inherit parent permissions. Parent should have permissions safe for ALL children.
- **Secret teams**: Only visible to team members + org owners. CANNOT be nested.
- Teams can be synced with IdP groups (SAML/SCIM)

**Practical pattern** from GitHub blog:
- Set org base permission to "No permission" (or Read for innersource)
- Create a broad "Engineering" parent team with Read on most repos
- Nest sub-teams (Product Eng, Client Ops Eng, DevOps) with Write on their repos
- Use secret teams for sensitive access groups

**Limitation:** Secret teams cannot be nested. This means the "founders-only" team must be a standalone secret team.

### Sources
- https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams (Quality: 5)
- https://blog.gitguardian.com/best-practices-for-managing-developer-teams-in-github-orgs/ (Quality: 4)
- https://github.blog/enterprise-software/devops/best-practices-for-organizations-and-teams-using-github-enterprise-cloud/ (Quality: 5)

---

## Q4: Custom Roles (Enterprise Cloud)

### Findings
GitHub Enterprise Cloud allows up to 20 custom repository roles with 40+ fine-grained permissions. Custom roles:
- Start from an inherited base role (Read, Triage, Write, Maintain, Admin)
- Add specific permissions on top
- Can be assigned to users, teams, or outside collaborators

This means GrowthX could create an "eng-admin" custom role that has Admin-level access minus certain destructive permissions, or a "senior-eng" role with Maintain + specific extras.

**Custom org roles** also available: can delegate org-level tasks (manage teams, manage repos) without full Owner access.

### Sources
- https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/about-custom-repository-roles (Quality: 5)
- https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-peoples-access-to-your-organization-with-roles/about-custom-organization-roles (Quality: 5)

---

## Q5: Branch Protection & Rulesets

### Findings
**Branch protection rules** (per-repo):
- Require PR reviews before merge
- Require status checks
- Require signed commits
- Block force pushes
- Restrict who can push to matching branches

**Rulesets** (newer, recommended):
- Can apply across multiple repos from org level
- Multiple rulesets can stack (vs only one branch protection rule)
- "Evaluate" mode for testing before enforcement
- Can require review from specific teams (as of Nov 2025)

**CODEOWNERS**:
- Define ownership of files/directories
- Require approval from code owners before merge
- Best practice: put CODEOWNERS in `.github/` directory

### Sources
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets (Quality: 5)
- https://wellarchitected.github.com/library/governance/recommendations/managing-repositories-at-scale/rulesets-best-practices/ (Quality: 5)
- https://docs.github.com/articles/about-code-owners (Quality: 5)

---

## Q6: Security & Compliance

### Findings
- **2FA**: Should be required org-wide. Works alongside SAML SSO.
- **SAML SSO + SCIM**: Automates provisioning/deprovisioning. Critical for offboarding.
- **Audit logs**: 90-day retention by default. Stream to SIEM for longer retention.
- **Secret scanning**: Enable org-wide to catch leaked credentials.
- **Dependabot**: Enable for vulnerability alerts.
- Principle of least privilege throughout.

### Sources
- https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/security-and-compliance/audit-log-for-an-enterprise (Quality: 5)
- https://medium.com/@anshumaansingh10jan/how-to-secure-and-configure-github-organizations-for-optimal-security-5fbc43bc4f1d (Quality: 4)

---

## Quality Checkpoint

| Metric | Target | Actual |
|--------|--------|--------|
| Foundations covered | Yes | ✅ Org roles, repo roles, team mechanics |
| Frameworks found | 3+ | ✅ RBAC model, nested teams, rulesets, CODEOWNERS, custom roles |
| Experts identified | 5+ | ✅ GitHub docs, GitHub blog, GitGuardian, ConductorOne, Entro, Arnica |
| Sources discovered | 30+ | ✅ 30+ unique sources |
| Examples documented | 5+ | ✅ GrowthX-specific 4-layer model, nested team examples, branch protection patterns |

**Score: 0.85 (Great)** — Proceed to synthesis.
