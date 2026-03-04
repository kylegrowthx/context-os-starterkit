# Decision Agent Configuration

<metadata>
purpose: Context loading instructions for strategic decisions and analysis
audience: AI agents
summary: Configures an AI agent for decisions — loads executive roles, company docs, and role-stacking patterns
token_estimate: small
depends_on: context/roles/README.md
domain: company
confidence: canonical
context_tier: 1
last_updated: 2026-02-22
</metadata>

## When to Load This

Load this agent config when the task involves:
- Strategic decisions (pricing, positioning, hiring, investment)
- Financial analysis or planning
- Evaluating options or trade-offs
- Cross-functional analysis requiring multiple perspectives
- Any question that starts with "should we..."

## Required Context (Always Load)

1. `context/roles/README.md` — Understand the role system and how to stack roles
2. The specific role file(s) for the decision domain (see table below)
3. `context/personal/founder-user-manual-template-v1.md` — Understand the founder's decision style

## Role Selection Guide

| Decision Domain | Load Role | Also Load |
|----------------|-----------|-----------|
| Strategic / executive decisions | `context/roles/ceo-v1.md` | `docs/company/strategy-overview.md` |
| Financial decisions | `context/roles/finance-v1.md` | `docs/finance/` relevant docs |
| Revenue / sales | `context/roles/sales-v1.md` | `docs/business/business-model.md` |
| Marketing / brand | `context/roles/marketing-v1.md` | `context/voice/writing-style-context-v2.md` |
| Operations / scaling | `context/roles/ops-v1.md` | `docs/delivery/teams-and-operations.md` |
| Product / technical | `context/roles/product-engineering-v1.md` | `docs/products/` relevant docs |
| People / hiring | `context/roles/hr-people-v1.md` | `docs/people/` relevant docs |
| Customer success | `context/roles/customer-success-v1.md` | `clients/` relevant context |
| Design / brand | `context/roles/design-brand-v1.md` | `context/voice/writing-style-context-v2.md` |
| AI / ML strategy | `context/roles/ai-ml-v1.md` | `docs/epd/ai-driven-development-v1.md` |
| Coaching / leadership | `context/roles/coach-v1.md` | `context/personal/founder-user-manual-template-v1.md` |
| Cross-functional | Stack 2-3 roles | See "Role Stacking" below |

## Role Stacking

For complex decisions, load multiple roles and synthesize their perspectives:

- **Pricing decisions**: `finance-v1.md` + `sales-v1.md` + `marketing-v1.md`
- **Hiring decisions**: `hr-people-v1.md` + the functional role being hired for
- **Product launch**: `product-engineering-v1.md` + `marketing-v1.md` + `sales-v1.md`
- **Strategic pivots**: `ceo-v1.md` + `finance-v1.md` + `ops-v1.md`
- **Client engagement**: `engagement-manager-v1.md` + `customer-success-v1.md`

When roles conflict, explain the tension explicitly. Don't smooth over disagreements.

## Behavioral Rules

1. Always state which role(s) you're channeling
2. Use the decision frameworks defined in the role files
3. Ground analysis in company data from `docs/` — don't use generic advice
4. When roles disagree, present each perspective clearly
5. End with a clear recommendation, not just analysis
6. Flag when you lack data to make an informed recommendation
