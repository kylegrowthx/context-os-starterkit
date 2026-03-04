# Functional Roles

<metadata>
purpose: Index of AI persona roles mapped to business functions
audience: AI agents, Marcel / founder
last_updated: 2026-02
</metadata>

---

## What this is

This folder contains AI persona definitions for 15 business functions. Reference a role file (e.g., `@context/roles/ops-v1.md`) to have the agent think and act from that function's perspective.

Each role provides:
- **Leaders to channel** — Real operators whose thinking patterns to emulate
- **Decision frameworks** — Proven frameworks for the function's key decisions
- **Mental models** — How great leaders in this function think about problems
- **Voice and approach** — How the persona communicates
- **Context to reference** — Which company docs inform decisions

---

## The roles

| Function | File | Core focus |
|----------|------|------------|
| **CEO** | `ceo-v1.md` | Company vision, strategy, cross-functional alignment, systems thinking |
| **Product and engineering** | `product-engineering-v1.md` | Product roadmap, technical architecture, build vs. buy |
| **Design and brand** | `design-brand-v1.md` | Brand identity, visual communication, positioning |
| **Operations** | `ops-v1.md` | Capacity planning, delivery efficiency, systems at scale |
| **Sales** | `sales-v1.md` | Pipeline, deal velocity, qualification, revenue growth |
| **Coach** | `coach-v1.md` | Personal performance, uncomfortable truths, fierce accountability |
| **HR and people** | `hr-people-v1.md` | Hiring, org design, culture, retention |
| **Finance** | `finance-v1.md` | Unit economics, cash flow, pricing, capital allocation |
| **AEO, SEO, and content** | `aeo-seo-content-v1.md` | AI visibility, SEO, content strategy, CheckThat domain |
| **Marketing** | `marketing-v1.md` | Brand, demand generation, category design |
| **Social media** | `social-media-v1.md` | LinkedIn, audience growth, hooks, engagement |
| **Research analyst** | `research-analyst-v1.md` | Deep research, competitive intelligence, synthesis |
| **AI and ML** | `ai-ml-v1.md` | AI workflows, context engineering, human-AI collaboration |
| **Customer success** | `customer-success-v1.md` | Retention, health scoring, customer outcomes |
| **Engagement manager** | `engagement-manager-v1.md` | Client delivery, weekly calls, 8-week plan execution |

---

## How to use

**For functional expertise:**
```
@context/roles/ops-v1.md - Review our capacity plan for Q2. Do we have enough resources?
```

**For multiple perspectives:**
```
@context/roles/ops-v1.md @context/roles/finance-v1.md - We're considering hiring 3 more editors. Walk me through the ops and financial implications.
```

**For content creation:**
```
@context/roles/social-media-v1.md @context/voice/writing-style-context-v2.md - Write a LinkedIn post about this topic.
```

---

## Complementary pairs

| Decision type | Primary role | Pair with | Why |
|--------------|-------------|-----------|-----|
| Build vs. buy | product-engineering | finance | Technical feasibility meets unit economics |
| Hiring decisions | hr-people | ops | Culture fit meets capacity planning |
| Pricing changes | finance | sales | Margin impact meets sales reality |
| Go-to-market | marketing | sales | Brand strategy meets pipeline reality |
| Content strategy | aeo-seo-content | social-media | SEO strategy meets distribution |
| Client escalation | engagement-manager | customer-success | Delivery meets retention |
| Product strategy | product-engineering | ai-ml | Platform vision meets AI capability |
| Founder decisions | ceo | coach | Strategic clarity meets personal performance |

---

## Maintaining roles

- **Minor updates:** Edit the role file directly, update `last_updated`
- **Major changes:** Create a new version (`-v2`), move old to `/archive`
- **Adding new roles:** Follow the template structure in existing files
