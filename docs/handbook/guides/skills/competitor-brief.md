<metadata>
purpose: Produce comprehensive competitor analysis with perception scoring
source: https://handbook.growthx.ai/guides/skills/competitor-brief
sync_type: auto
access: build-team
last_synced: 2026-03-02
</metadata>

# Competitor brief

Generate deep competitor briefs that synthesize 200+ sources into a structured analysis. Each brief compares a target competitor against a focal company across company fundamentals, product capabilities, market perception, SEO/content effectiveness, and strategic positioning.

## Trigger phrases

- "Competitor brief" or "competitor analysis"
- "Competitive research on [company]"
- "Research [company] as a competitor"

## What it does

Two-phase process: research (scratchpad with 10 structured questions across company overview, funding, traction, acquisitions, products, pricing, analyst coverage, community sentiment, SEO, and content strategy) and synthesis (final brief with executive summary, company overview, product/feature analysis, analyst/review coverage, 15-dimension perception scoring, SEO/traffic analysis, and strategic assessment).

The 15-dimension perception scoring evaluates trust, innovation, ease of use, value, support quality, security, scalability, integration, domain expertise, thought leadership, product quality, speed, transparency, customer-centricity, and modernity — each scored 1-10 with rationale.

Supports parallel research agents for large batches and produces exactly 2 files per competitor: a research scratchpad and the final brief.

## Install

<CodeGroup>

```bash Cursor
mkdir -p .cursor/skills/competitor-brief
curl -o .cursor/skills/competitor-brief/SKILL.md \
  https://raw.githubusercontent.com/marcelsantilli/growthx-ceo-os/main/.cursor/skills/competitor-brief/SKILL.md
```

```bash Claude Code
mkdir -p .agents/skills/competitor-brief
curl -o .agents/skills/competitor-brief/SKILL.md \
  https://raw.githubusercontent.com/marcelsantilli/growthx-ceo-os/main/.cursor/skills/competitor-brief/SKILL.md
```

</CodeGroup>

<Note>
Requires access to the [growthx-context](https://github.com/marcelsantilli/growthx-ceo-os) repository (private).
</Note>
