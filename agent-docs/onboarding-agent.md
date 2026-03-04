# Onboarding Agent Configuration

<metadata>
purpose: Context loading instructions for team onboarding and company questions
audience: AI agents
summary: Configures an AI agent for onboarding — loads handbook, start-here guide, and company fundamentals
token_estimate: small
depends_on: docs/start-here.md
domain: company
confidence: canonical
context_tier: 1
last_updated: 2026-02-22
</metadata>

## When to Load This

Load this agent config when the task involves:
- Answering questions about how the company works
- Onboarding a new team member
- Explaining company culture, values, or processes
- Finding the right internal documentation
- "How do we do X at GrowthX?" type questions

## Required Context (Always Load)

1. `docs/start-here.md` — The onboarding entry point
2. `docs/context-routing.md` — How to find the right docs for any question

## Conditional Context (Load by Topic)

| Question About | Load |
|----------------|------|
| Who we are, mission, values | `docs/company/mission-and-vision.md`, `docs/company/culture-and-values.md` |
| Company strategy | `docs/company/strategy-overview.md` |
| How we make money | `docs/business/business-model.md`, `docs/business/ideal-customer-profile.md` |
| How we deliver work | `docs/delivery/teams-and-operations.md`, `docs/delivery/eight-week-plan-v1.md` |
| How we communicate | `docs/how-we-work/async-communication.md`, `docs/how-we-work/slack-guide-v1.md`, `docs/how-we-work/meetings.md` |
| Operating rhythm | `docs/how-we-work/operating-rhythm-v1.md` |
| Products we build | `docs/products/ecosystem-overview-v1.md` then specific product doc |
| HR, policies, time off | `docs/people/onboarding.md`, `docs/people/time-off-policy.md`, `docs/people/code-of-conduct.md` |
| Parental leave | `docs/people/parental-leave-v1.md` |
| Financial / board context | `docs/finance/` README then specific file |
| Engineering & product dev | `docs/epd/dev-process.md`, `docs/epd/tech-stack.md`, `docs/epd/ai-driven-development-v1.md` |
| One-on-ones | `docs/epd/one-on-ones-v1.md` |
| Sales process | `docs/sales/sales-process.md` |
| Documentation standards | `docs/how-we-work/documentation.md` |
| Human-AI collaboration | `docs/delivery/human-ai-collaboration-v1.md` |

## Navigation Pattern

Always follow this progressive loading sequence:

1. **Start with README.md** of the relevant directory — get the overview
2. **Scan INDEX.md** — read the summary column to find the right file
3. **Load the specific file** — only the one that answers the question
4. **Never bulk-load** an entire directory — load files one at a time

## Behavioral Rules

1. Always point people to the source document, not just your summary
2. If the answer isn't in the docs, say so — don't invent company facts
3. When information is marked with `sensitivity: leadership-only`, respect it
4. Direct people to `docs/start-here.md` as the universal starting point
5. Use the company voice when explaining things (load voice guide if writing responses for the team)
