# Writing Agent Configuration

<metadata>
purpose: Context loading instructions for writing and editing tasks
audience: AI agents
summary: Configures an AI agent for writing tasks — loads voice guide, style rules, and output conventions
token_estimate: small
depends_on: context/voice/writing-style-context-v2.md
domain: writing
confidence: canonical
context_tier: 1
last_updated: 2026-02-22
</metadata>

## When to Load This

Load this agent config when the task involves:
- Writing blog posts, articles, or thought leadership
- Editing or reviewing existing content
- Creating social media posts
- Drafting customer-facing communication
- Any task where voice and tone matter

## Required Context (Always Load)

1. `context/voice/writing-style-context-v2.md` — The definitive GrowthX voice and style guide
2. `docs/context-routing.md` — For navigating to additional context

## Conditional Context (Load When Relevant)

| Condition | Load |
|-----------|------|
| Social media content | `context/voice/social-media-style-guide-template-v1.md` + `context/roles/social-media-v1.md` |
| Marketing / brand content | `context/roles/marketing-v1.md` |
| SEO / AEO content | `context/roles/aeo-seo-content-v1.md` + `knowledge/aeo/README.md` |
| Client-facing content | `docs/business/ideal-customer-profile.md` |
| Product content | `docs/products/ecosystem-overview-v1.md` or specific product doc (e.g., `docs/products/contentos-overview-v1.md`) |
| Thought leadership | `sources/people-index.md` (for references and citations) |
| Writing craft reference | `knowledge/content/writing-craft-study-guide-v1.md` |
| LinkedIn content | `knowledge/content/linkedin-engagement-study-guide-v1.md` + `knowledge/content/linkedin-hooks-study-guide-v1.md` |

## Output Conventions

- Save drafts to `pipeline/scratchpad/`
- Save finished content to `pipeline/outputs/`
- Use file naming: `topic-name-v1.md`
- Include lineage metadata in outputs (source_skill, input context)

## Behavioral Rules

1. Always follow the voice guide — read it before generating any content
2. Lead with the point — readers should know the main idea in 2 sentences
3. Use active voice, short sentences, concrete examples
4. Ground claims in specifics — numbers, examples, stories
5. Never generate content that contradicts existing docs
6. When unsure about facts, flag it rather than inventing
7. Never use em dashes in any output. Replace with periods, commas, or colons.
