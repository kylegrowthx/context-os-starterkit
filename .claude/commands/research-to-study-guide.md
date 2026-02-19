Deep research on any topic, with the option for raw research only or a full study guide.

Load `agent-docs/research-agent.md` before starting.

## Phase 0: Clarify Scope

Before doing any research, ask the user:

1. **What's the topic and goal?** What do they want to learn, and why?
2. **What depth?**
   - **Raw research only** — gather findings, save to `pipeline/research/`, stop there
   - **Full study guide** — raw research → scratchpad synthesis → finished study guide in `knowledge/`
3. **Who's the audience?** Role, experience level, what they'll use it for
4. **Any constraints?** Sources to include/exclude, time sensitivity, specific angles

## Phase 1: Research Plan (Get Approval)

Generate 3-5 research questions per category:

1. **Foundations** (Critical) — What is it, why it matters, core concepts, mental models, misconceptions
2. **Frameworks & Models** (Critical) — Established frameworks, processes, templates and tools
3. **Key Practitioners** (High) — Recognized experts, key contributions, where experts agree/disagree
4. **Source Discovery** (High) — Essential books, blogs, newsletters, podcasts, videos, courses
5. **Real Examples** (High) — Best documented examples, instructive failures, before/after transformations
6. **Skills & Practice** (Medium) — Distinguishing skills, what to practice, learning sequence

Present the research plan to the user showing:
- The questions you'll research
- Where output files will be saved
- Estimated scope

**Wait for explicit user approval before proceeding.**

## Phase 2: Execute Research

Use web search to answer each question. For each, document: findings, sources (with quality score 1-5), and gaps.

Source quality: 5 = authoritative expert with unique insights; 4 = respected, actionable; 3 = decent coverage; 2 = surface-level or dated; 1 = low quality.

Save all raw research to `pipeline/research/[topic]-research-v1.md`.

**If user chose raw research only: stop here.** Tell the user where to find the file and summarize key findings.

## Phase 3: Synthesize (Full Study Guide Only)

Take raw research and synthesize into a working draft at `pipeline/scratchpad/[topic]-research-scratchpad.md`.

## Phase 4: Quality Checkpoint (Full Study Guide Only)

Before producing the final study guide, evaluate:
- Foundations covered? Yes/No
- Frameworks found: target 3+
- Experts identified: target 5+
- Sources discovered: target 30+
- Examples documented: target 5+

Quality bands: Bad (0-0.4) must iterate; Acceptable (0.4-0.7) can proceed; Great (0.7-1.0) proceed to final output.

If gaps exist, generate follow-up questions and iterate (max 3 times).

## Phase 5: Produce Study Guide (Full Study Guide Only)

Create study guide at `knowledge/[subdirectory]/[topic]-study-guide-v1.md` with structure:
- Header with learner profile, goal, time investment, date
- How to Use This Guide
- Part 1: Foundations
- Part 2: Frameworks & Process
- Parts 3-4: Topic-specific sections
- Part 5: Skills & Practice
- Appendix A: Curated Source Library
- Appendix B: Templates & Tools
- Appendix C: Learning Path

Subdirectory routing:
- `knowledge/content/` — writing, style, content creation
- `knowledge/building/` — company ops, leadership, scaling
- `knowledge/product/` — product strategy, engineering, technical
- `knowledge/domain/` — industry-specific or specialized knowledge

If unclear, ask the user.

## Anti-Hallucination Rules

1. NEVER guess URLs — only cite verified sources
2. NEVER invent sources — no fabricated books, authors, or frameworks
3. NEVER fake statistics — say "not found" if you don't have data
4. Trust web research — don't flag recent info as dubious
5. Cite everything — every claim needs a source
