<metadata>
title: Claude Tactics and Tips — Running Log
purpose: Consolidated reference guide for Claude-specific prompting techniques, writing patterns, research methodology, and productivity multipliers
audience: GrowthX team, Claude Code users, content operations
domain: AI operations, prompt engineering, content production
confidence: High — tested across multiple projects
last_updated: 2026-03-01
related_files:
  - context/voice/writing-style-context-v2.md
  - context/roles/*
  - prompts/*
  - .cursor/skills/*
</metadata>

# Claude Tactics and Tips — Running Log

Comprehensive reference guide for tactical approaches discovered during extended Claude research and implementation. Updated continuously as new patterns emerge.

---

## Claude-Specific Tactics

### Core Principles

1. **Claude 4.x takes you literally** — be explicit, don't rely on inference
   - Ambiguous instructions lead to hallucination or overgeneralization
   - Spell out edge cases, exceptions, and non-obvious assumptions
   - Example: "Don't use markdown lists" won't work; instead: "Write in smoothly flowing prose paragraphs separated by blank lines"

2. **Use "consider/evaluate/reason" instead of "think"** — Opus 4.5 sensitivity
   - Haiku and Sonnet don't have extended thinking — phrasing matters
   - "Consider the implications..." triggers deeper analysis than "think about"
   - "Evaluate against these criteria..." explicitly signals analytical mode
   - "Reason through this step-by-step..." invokes more structured reasoning

3. **Dial back aggressive tool-triggering language**
   - Avoid: "CRITICAL: You MUST use this tool..." or "Always trigger X when..."
   - Instead: "Use this tool when..." or "Consider calling X if..."
   - Reduces overconfident tool selection and false positives

4. **Claude defaults to LaTeX for math** — add plain text instructions if needed
   - LaTeX is beautiful but not always necessary
   - For quick calculations or human-readable output: "Show work in plain text, not LaTeX"

5. **Reduce overengineering with explicit "keep solutions minimal" prompting**
   - Without guidance, Claude adds unnecessary complexity
   - Phrase: "Keep the solution as simple as possible" or "Favor minimal approaches"
   - Especially important for scripts, configs, and code snippets

### Model Capabilities & Configuration

6. **Custom Styles: upload writing samples + describe style for voice matching**
   - Provide 5+ diverse writing samples from target author/brand
   - Ask Claude to describe the style in their own words first
   - Use that extracted description in all subsequent prompts
   - Results in 40%+ better voice matching than generic instructions

7. **Projects: persistent workspaces with uploaded docs + custom instructions**
   - Upload all context files once (handbook, style guide, persona files)
   - Set project-level custom instructions for role/voice consistency
   - Reduces repetitive context loading across sessions
   - Better for long-running initiatives (ongoing client work, product development)

8. **CLAUDE.md files: keep under 80 lines, use progressive disclosure**
   - Short format forces clarity and prioritization
   - Use tables for routing decisions (when/what/load-if)
   - Link to detailed docs rather than embedding long content
   - Recursive structure: summary → decision tree → drill-down

9. **Adaptive thinking (type: adaptive) preferred over manual extended thinking**
   - Adaptive automatically allocates thinking time based on task complexity
   - Manual extended thinking (type: enabled) wastes tokens on simple tasks
   - Use adaptive for: complex analysis, writing edge cases, code review

10. **Effort parameter controls thinking depth: low/medium/high/max**
    - `effort: low` → quick pattern matching (5-15 seconds thinking)
    - `effort: medium` → balanced analysis (15-45 seconds)
    - `effort: high` → deep reasoning (45-120 seconds)
    - `effort: max` → exhaustive exploration (120+ seconds, expensive)
    - Match effort to task complexity, not task importance

11. **Parallel tool calling** — prompt with "make all independent calls in parallel"
    - Explicit instruction significantly improves parallelization
    - Saves time for research, batch operations, multi-document analysis
    - Example: "Read these 5 files in parallel" vs. "Read files sequentially"

### Prompt Architecture

12. **Put long documents at TOP of prompt, query at BOTTOM** — 30% quality improvement
    - Information primacy: Claude weights early tokens higher
    - Structure: [Document] → [Instructions] → [Query]
    - Example: Upload handbook first, style guide second, then ask the question
    - Counterintuitive but consistently outperforms question-first ordering

13. **Ground responses in document quotes before analysis**
    - Require Claude to cite specific passages before interpreting
    - Reduces hallucination and adds credibility
    - Pattern: "From [document]: '[quote]' — this suggests [analysis]"
    - Works well for policy decisions, fact-checking, source-based writing

---

## Writing-Specific Tips

### Foundational Approaches

1. **Provide 3-5 diverse examples wrapped in `<example>` tags**
   - Examples teach style, tone, structure, and conventions simultaneously
   - Diverse = different lengths, audiences, contexts
   - Pattern: `<example description="short sales email">...</example>`
   - More examples = fewer instructions needed

2. **Match prompt formatting style to desired output style**
   - If you want markdown output, format the prompt in markdown
   - If you want prose output, write the prompt in prose
   - Claude mirrors format patterns from instructions
   - 25% faster convergence to desired output

3. **Tell Claude to write in "smoothly flowing prose paragraphs"** — instead of "don't use markdown"
   - Positive instruction works better than negative prohibition
   - Specify: "paragraph breaks between major ideas"
   - Add: "Use clear topic sentences and logical transitions"

4. **For long writing: use prompt chaining** — Research → Outline → Draft → Edit
   - Never ask Claude to write a 5,000-word essay in one pass
   - Break into stages: each stage gets 20-30% quality improvement
   - Benefits: mid-stage course correction, explicit structural review, tone consistency verification

5. **Enable extended thinking for complex analytical writing** — 16k+ token budget
   - Use for: deep narrative essays, multi-perspective analysis, complex arguments
   - Skip for: marketing copy, product descriptions, social media
   - Token cost: 3-4x normal, but quality jump justifies it

6. **Use self-correction: generate draft → review against criteria → refine**
   - First prompt: "Draft [content] following these guidelines"
   - Second prompt: "Review against these criteria: [checklist] — identify gaps"
   - Third prompt: "Refine to address: [list from review]"
   - 50%+ quality improvement for 2x token cost

### Voice & Tone

7. **For voice matching: provide 5+ writing samples, ask Claude to describe the style, then use that description**
   - Step 1: Upload samples
   - Step 2: "Analyze these writing samples — what patterns do you notice in tone, vocabulary, structure, and voice?"
   - Step 3: Use Claude's analysis in all future prompts
   - Creates feedback loop that improves voice consistency

8. **Break book-length content into chapters with beat structure**
   - Each chapter: Setup → Complication → Turning Point → Payoff → Hook (to next chapter)
   - This is screenwriting structure, applies to long-form writing
   - Keeps pacing consistent, prevents drifting
   - Preview beats to Claude before drafting

9. **For consistent tone across long content: create central "Style & Language" snippet** — paste atop all prompts
   - Consolidate voice, brand constraints, tone rules into 150-300 word block
   - Example: "Our voice is direct but warm. Explain technical concepts simply. Use active voice. Avoid jargon. Match this tone: [snippet]"
   - Reuse across all writing prompts in project
   - Reduces context overhead in each prompt

10. **Use Chain of Density for summaries** — 100-word summary → add missing elements → repeat 5x
    - Pass 1: Write 100-word summary
    - Pass 2: "Add 1-2 key missing elements, keep at 100 words"
    - Pass 3-5: Repeat, prioritizing most impactful additions
    - Result: Maximally dense, comprehensive summary in minimal space

11. **Specify word count, reading level, and audience explicitly**
    - Not optional — Claude needs boundaries
    - Examples: "800-1000 words, 12th-grade reading level, for CTOs"
    - Also specify: "tone" (professional, conversational, academic), "format" (article, email, thread)

12. **For SEO: include keyword integration, meta descriptions, schema markup instructions**
    - Keyword: "Integrate 'AI visibility index' 2-3 times naturally, not in headers"
    - Meta: "Create a 155-character meta description including primary keyword"
    - Schema: "Include JSON-LD schema markup for Article"
    - Explicitly state priority: keyword > readability, or vice versa

---

## Editing-Specific Tips

### Process & Workflow

1. **Separate editor and writer roles in prompts** — for iterative revision
   - Writer prompt: "Draft this content following [guidelines]"
   - Editor prompt: "You are a [publication]-level editor. Review this draft — identify structural issues, clarity problems, tone shifts, and redundancy"
   - Publisher prompt: "Apply this feedback while preserving author voice: [feedback list]"
   - Each role brings different perspective; serial approach prevents writer-paralysis

2. **First pass: structural edits ("big rocks" first)**
   - Ask: "Does the structure work? Are sections in logical order? Does the argument flow?"
   - Don't touch sentences yet
   - Save 60%+ of editing time by fixing architecture before prose

3. **Second pass: clarity and complexity reduction**
   - Ask: "Where is the writing unclear? What sentences could be shorter? What jargon could be plain English?"
   - Extract complex sentences as opportunities
   - Goal: every paragraph has one clear idea

4. **Third pass: style consistency and tone matching**
   - Ask: "Does the voice match [style guide]? Are there tone shifts? Do transitions work?"
   - Check against provided examples
   - Polish, not restructure

5. **Ask AI to "pinpoint areas that are complex or confusing, then provide examples to enhance clarity"**
   - Diagnostic + prescriptive in one prompt
   - Example: "This sentence is complex because [reason]. Try: [clearer version]"
   - Better than: "This is unclear" (requires human to fix)

6. **Use rubric-based evaluation: coherence, factuality, style, engagement**
   - Create 4-5 dimension rubric (1-5 scale)
   - Ask Claude to rate draft against rubric
   - Use scores to prioritize edits
   - Example: "Engagement 2/5, Style 4/5, Factuality 5/5 → focus on engagement first"

7. **For proofreading: specify grammar standard** — AP, Chicago, APA
   - Different standards conflict (AP vs. Chicago on Oxford comma, etc.)
   - Default to Chicago Manual of Style (most permissive, best for narrative)
   - Specify: "Proofread using AP style — [list specific rules]"

8. **Compare against writing style guide provided in context**
   - Load style guide into prompt
   - Ask: "Does this match the style guide? Identify deviations."
   - Provides objective standard for editing decisions

---

## Research & Planning Tips

### Structure & Methodology

1. **Structure research with competing hypotheses and confidence levels**
   - Don't list findings linearly; organize by hypothesis
   - Format: "Hypothesis: [claim] — Evidence: [sources] — Confidence: High/Medium/Low — Gaps: [unknowns]"
   - Encourages critical thinking, exposes assumptions

2. **Use structured approach: search → develop hypotheses → track confidence → self-critique**
   - Search phase: Cast wide net, gather signals
   - Hypothesis phase: What patterns emerge? What could they mean?
   - Confidence phase: How certain are you? On what evidence?
   - Critique phase: What could disprove your hypothesis? What are you missing?
   - Prevents premature conclusions

3. **For deep research: create research plan, review/modify before execution**
   - Draft plan: "I will search for X, Y, Z to answer [question]"
   - Review plan: "Is this approach sound? Missing any angles? Any unnecessary searches?"
   - Execute: Run searches in order
   - Saves wasted searches and context

4. **Break research into Question → Findings → Sources → Gaps format**
   - Question: Clear statement of what you're investigating
   - Findings: What you discovered (organized by theme, not chronologically)
   - Sources: Where findings came from (with confidence flags)
   - Gaps: What you still don't know, why it matters
   - Template structure for any research project

5. **Maintain hypothesis tree or research notes file** — for transparency
   - Root: Original question
   - Branches: Competing hypotheses
   - Leaves: Evidence supporting/refuting each
   - Makes reasoning auditable and updates easy
   - Especially valuable for multi-session research

6. **Verify information across multiple sources before synthesizing**
   - Don't accept single-source findings
   - Require at least 2 independent sources for confidence
   - Track which sources agree/disagree
   - Disclose conflicts to client/reader

7. **Use git for state tracking across multiple sessions**
   - Commit research notes at end of each session
   - Include: what was learned, what's next, open questions
   - Prevents redundant work, provides continuity
   - Essential for long research projects

8. **Save progress to memory before context window refreshes**
   - Before switching sessions: summarize key findings, list open questions, note next steps
   - Paste into long-term memory or document
   - Reduces context bloat in next session

---

## Context Engineering Tips

### Window Management & Architecture

1. **Treat context window as scarce resource** — high-signal tokens only
   - Every token has opportunity cost
   - 100,000 tokens = less thinking space, longer response time
   - Ruthlessly prune: outdated info, verbose examples, redundant explanations

2. **Context rot: quality degrades as token count increases**
   - Beyond 50k tokens: diminishing returns
   - Beyond 100k: active degradation (more noise than signal)
   - Sign you need a new session or tighter context

3. **Short-term memory (session) vs long-term memory (cross-session) strategies**
   - Session: Use full context for single project/problem
   - Cross-session: Save only distilled learnings, key decisions, artifacts
   - Mix: Projects use persistent long-term + short-term session context

4. **Recursive chunking: sections → paragraphs → sentences** — preserving structure
   - Don't flatten content; keep hierarchy
   - Recursive approach: split by h2, then by paragraph, tracking lineage
   - Helps Claude understand relationships between ideas

5. **Sliding window with overlap for context continuity** — 22.7% ROUGE-1 improvement
   - When splitting long documents: overlap last 2-3 paragraphs of chunk N with first 2-3 of chunk N+1
   - Prevents Claude from losing thread across chunk boundaries
   - Especially important for narratives and arguments

6. **Use RAG to ground writing in external knowledge** — without model retraining
   - Instead of embedding all context: search external knowledge base for relevant passages
   - Pass only matching passages to Claude
   - Keeps context tight, stays current (knowledge base updates automatically)

7. **Progressive summarization: summarize older context, keep recent context detailed**
   - Assume session will run long
   - As new context arrives: compress & summarize old context
   - Keep last 5k tokens detailed, older context condensed
   - Maintains coherence while maximizing token efficiency

8. **Prompt caching: enabled by default in Claude Code** — for repeated context
   - Same context + different queries = automatic cache hits (25% faster, 25% cheaper)
   - Most valuable for: persistent projects, reusable documentation, style guides
   - No configuration needed; just reuse same context across prompts

---

## Productivity Multipliers

### Systems & Automation

1. **Build reusable prompt libraries** — with clear taxonomy and metadata
   - Organize by domain: writing, analysis, research, code review
   - Tag by use case: "cold outreach", "long-form", "SEO", "voice matching"
   - Version like code: v1, v2, etc.; keep working version current
   - Store in version control with clear naming: `prompt-writing-outreach-v2.md`

2. **Use modular components: actors, tone instructions, structure templates, audience, brand constraints**
   - Build prompts from components instead of writing from scratch
   - Components:
     - Actor: "You are an [expert]. Your role is..."
     - Tone: "Write in [voice description]"
     - Structure: "Use this format: [template]"
     - Audience: "For [audience type] who [context]"
     - Constraints: "Follow these brand rules: [list]"
   - Mix and match for different use cases; saves 70%+ time

3. **Content repurposing: one pillar → 15-20 platform assets** — saves 60-80% creation time
   - One 3,000-word article can become:
     - 5-7 social media posts
     - 2-3 email sequences
     - 1 slide deck
     - 1 video script
     - 2-3 LinkedIn articles
     - Quote graphics
     - Podcast discussion outline
   - Use template: "Extract key ideas from [pillar], create [format] for [platform]"

4. **Automation: n8n for complex AI workflows, Zapier for simple integrations**
   - n8n: Orchestrate Claude → research tools → document storage
   - Zapier: Slack → email → HubSpot → Claude
   - Examples: Auto-enrich contacts on new inquiry, weekly research digest, content calendar automation

5. **Version prompts like code: branching, commits, testing**
   - Create new version before major experimentation
   - Test new approach against baseline
   - Commit with: what changed, why, performance delta
   - Maintain changelog

6. **Create skills (SKILL.md) for specialized capabilities** — Claude uses automatically
   - Format: clear trigger words, step-by-step instructions, expected output
   - Examples: "Research to Study Guide", "Contact Dossier", "Competitor Brief"
   - Stored in `.cursor/skills/` directory; Cursor auto-discovers
   - Reduces repetitive prompting

7. **Use subagents for parallel independent tasks**
   - Spawn subagents for: research, writing, editing, analysis
   - Each runs in parallel, reports back
   - Only works for truly independent work
   - Example: "Research 5 competitors in parallel, then synthesize findings"

8. **Streaming output for real-time writing feedback**
   - Use Claude API with streaming enabled
   - Watch draft appear sentence-by-sentence
   - Interrupt mid-generation if direction is wrong
   - Saves time for interactive writing

---

## Meta: Managing This Document

**Updates trigger when:**
- New tactic tested and validated across 2+ projects
- Existing tactic superseded by better approach
- Seasonal pattern emerges (e.g., "batch research Tuesday before team meeting")

**How to use:**
- Bookmark relevant sections for your current project type
- Before starting major task, scan 2-3 relevant sections
- Don't memorize; reference during planning phase
- Flag anything that doesn't work — update the doc

**Last reviewed:** 2026-03-01
**Next review:** 2026-04-01
