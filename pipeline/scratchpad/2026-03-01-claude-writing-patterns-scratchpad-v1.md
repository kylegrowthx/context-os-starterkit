<metadata>
purpose: Running log of all writing patterns discovered during extensive research on Claude/AI writing skills, techniques, and prompting approaches
audience: GrowthX team, writers, content strategists, AI practitioners
domain: AI writing systems, prompting engineering, content creation
confidence: high
last_updated: 2026-03-01
related_files: context/voice/writing-style-context-v2.md, .cursor/skills/copywriting/SKILL.md, .cursor/skills/growthx-writing/SKILL.md
</metadata>

# Claude Writing Patterns Scratchpad

**Date Started:** 2026-03-01
**Purpose:** Consolidated reference of proven patterns for effective AI-assisted writing
**Status:** Active research log — add findings as discovered

---

## Prompting Patterns for Writing

### 1. Contract-Style System Prompts
Treat prompts as formal contracts with explicit sections:

- **Identity**: "You are a [specific role with domain expertise]"
- **Rules**: Explicit constraints, style guidelines, output boundaries
- **Scope**: What is and is not in scope
- **Output Format**: Exact formatting specification

**Example Application:**
Instead of "Write a blog post," frame as: "You are a B2B content strategist specializing in AI visibility. Your constraint is 1200 words. Output must include [sections]. Tone is conversational but authoritative."

**When to Use:** High-stakes content (longform, client-facing, brand-critical)
**Effectiveness:** 70%+ improvement in output consistency vs vague prompts

---

### 2. 4-Block Pattern
Separate prompts into four distinct blocks for clarity:

1. **INSTRUCTIONS** — Detailed steps or approach
2. **CONTEXT** — Background, constraints, domain knowledge
3. **TASK** — Specific assignment with success criteria
4. **OUTPUT FORMAT** — Exact formatting, structure, length

**Example Structure:**
```
## INSTRUCTIONS
[Step-by-step approach]

## CONTEXT
[Domain knowledge, constraints, audience]

## TASK
[Specific deliverable with success criteria]

## OUTPUT FORMAT
[Markdown structure, length, example]
```

**When to Use:** Complex, multi-step writing projects; when handoff clarity matters
**Effectiveness:** Reduces clarification rounds by 60%+

---

### 3. XML Tag Structuring
Use semantic XML tags to create isolated context zones:

- `<role>` — Primary persona or expertise
- `<constraint>` — Boundaries and non-negotiables
- `<context>` — Background information
- `<task>` — The actual work
- `<example>` — Worked examples
- `<format>` — Output specification
- `<criteria>` — Success metrics

**Example:**
```xml
<role>You are a SaaS copywriter specializing in B2B fintech</role>
<constraint>Max 150 words, no jargon, no hype</constraint>
<context>Target audience is CFOs with 10+ years experience</context>
<task>Write a headline and subheadline for an expense management tool</task>
<format>Markdown, plain language</format>
<criteria>Score above 85 on clarity; pass the jargon audit</criteria>
```

**When to Use:** When you need semantic clarity and context isolation
**Effectiveness:** Prevents context bleed; improves isolation of constraints

---

### 4. Role/Persona Assignment
Prime domain-specific knowledge and vocabulary through explicit role definition:

**High-Specificity Roles:**
- Not: "You are a writer"
- Yes: "You are a technical content strategist with 8 years in B2B SaaS marketing, fluent in both developer and product manager vocabularies"

**Role Stacking** (for complex tasks):
- Primary role: "Head of Marketing"
- Secondary personas: "Product Manager perspective," "Customer perspective," "Finance lens"

**Effect:** Activates domain-specific language patterns, reasoning shortcuts, cultural knowledge.

**When to Use:** Any domain-specific writing; content requiring nuanced insider perspective
**Effectiveness:** 40-50% improvement in domain vocabulary accuracy

---

### 5. Few-Shot / Multishot Prompting
Provide 3-5 diverse examples in `<example>` tags before the task:

**Structure:**
```
<example>
Task: [similar writing task]
Output: [desired result - good example]
</example>

<example>
Task: [another variation]
Output: [desired result]
</example>

[Repeat 3-5 times with diverse scenarios]

Now your task: [actual assignment]
```

**Diversity Matters:**
- Vary length, tone, complexity
- Include both strong and "mediocre but acceptable" examples
- Show the range of acceptable output

**When to Use:** Establishing new tone, format, or style; complex structures
**Effectiveness:** 50-70% improvement in output consistency vs zero-shot

---

### 6. Chain of Thought (CoT)
Explicitly request step-by-step reasoning for complex writing tasks:

**Trigger Phrases:**
- "Let's think through this step by step"
- "Show your reasoning before you write"
- "Break this into phases: [phase names]"

**Structure:**
```
Before writing, address:
1. Who is the reader and what do they need?
2. What's the core message in 1 sentence?
3. What objections might they have?
4. What's the strongest supporting evidence?
5. How should we structure this for retention?

Now write the piece.
```

**When to Use:** High-stakes content; when stakes demand careful reasoning
**Effectiveness:** 60%+ improvement in argument quality; fewer revisions

---

### 7. Tree of Thought (ToT)
Branch exploration of multiple writing approaches before converging on one:

**Application for Writing:**
```
Generate 3 alternative approaches to [writing task]:

Approach A: [Description - pros/cons]
Approach B: [Description - pros/cons]
Approach C: [Description - pros/cons]

Evaluate each against [criteria].
Choose the strongest approach.
Then write the piece using that approach.
```

**Use Case:** Strategic content, major campaigns, brand-defining pieces
**When to Use:** Decisions between substantively different writing styles or structures
**Effectiveness:** Surfaces creative alternatives; prevents tunnel vision

---

### 8. Self-Correction / Reflexion Loop
Generate → Critique → Refine pattern for iterative improvement:

**Structure:**
```
Step 1: Write the initial draft
Step 2: Review against these criteria:
  - Clarity (rate 1-10)
  - Engagement (rate 1-10)
  - Accuracy (rate 1-10)
  - Brand voice match (rate 1-10)

Step 3: Identify weaknesses
Step 4: Revise addressing weaknesses
Step 5: Output final version
```

**When to Use:** Any task where quality matters; self-editing phase
**Effectiveness:** 30-40% improvement vs single-pass writing

---

### 9. Chain of Density (CoD)
MIT/Salesforce technique: iterative compression and refinement.

**Pattern:**
1. **First Pass:** Write normally, capturing all ideas
2. **Compression 1:** Rewrite at 80% density — remove filler, tighten language
3. **Compression 2:** Rewrite at 60% density — keep only essential, add sophistication
4. **Final:** Rewrite at target density with target tone/voice

**Effect:** Forces clarity; eliminates jargon naturally; increases impact per word.

**When to Use:** Longform pieces that need to feel dense and sophisticated
**Effectiveness:** 50%+ improvement in information density; 30% shorter without losing substance

---

### 10. Negative Prompting
Specify what NOT to include; limit to top 3-5 hard constraints:

**Format:**
```
Write [task] WITHOUT:
1. [Specific anti-pattern, jargon, or approach]
2. [Second constraint]
3. [Third constraint]

These constraints are non-negotiable.
```

**Examples of Strong Negatives:**
- "No marketing hype, no corporate-speak, no passive voice"
- "No bullet points, no lists, no second-person address"
- "No citations, no external links, no assumptions about prior knowledge"

**Warning:** More than 5 negatives reduce effectiveness; rephrase as positive instructions instead.

**When to Use:** Preventing specific bad patterns; course-correcting previous iterations
**Effectiveness:** 40% reduction in unwanted patterns; prevents bad habits

---

## Writing Workflow Patterns

### 1. Research → Outline → Draft → Edit → Format Pipeline
Sequential workflow with clear handoff points:

**Phase 1: Research (20% of time)**
- Gather sources, interviews, data
- Build research document with quotes, stats, insights
- Organize findings by theme

**Phase 2: Outline (15% of time)**
- Convert research into logical flow
- Define sections and key arguments
- Map examples to points

**Phase 3: Draft (40% of time)**
- Write freely, capture voice
- Focus on completeness over polish
- Use outline as guardrail, not straitjacket

**Phase 4: Edit (20% of time)**
- Cut and refine
- Verify facts, quotes, attribution
- Improve clarity and rhythm

**Phase 5: Format (5% of time)**
- Apply final style, markdown, brand guidelines
- Check links, images, metadata
- Deliver

**When to Use:** Any significant content project (1000+ words, client-facing, strategic)
**Effectiveness:** Produces highest quality; prevents cramming all work into draft phase

---

### 2. Prompt Chaining
Sequential micro-tasks fed forward, each task output becomes next task input:

**Example Chain:**
```
Task 1: Research [topic] → Output: Research Summary
Task 2: Create outline from research → Output: Structured outline
Task 3: Write section 1 from outline + research → Output: Draft section 1
Task 4: Write section 2 → Output: Draft section 2
Task 5: Synthesize into cohesive draft → Output: Full draft
Task 6: Edit for voice and clarity → Output: Final version
```

**Benefits:**
- Each task is small and focused
- Early errors don't cascade to final output
- Easy to inject human review at any stage
- Output of one task directly feeds next task

**When to Use:** Content projects; when you want granular control and review points
**Effectiveness:** Highest quality for complex tasks; takes more tokens

---

### 3. Multi-Agent Pipeline
Researcher + Writer + Editor agents with explicit handoffs:

**Researcher Agent:**
- Gathers sources, builds research brief
- Output: `research-brief.md` with quotes, stats, themes

**Writer Agent:**
- Reads research brief and outline
- Writes draft with voice and flow
- Output: `draft.md`

**Editor Agent:**
- Reviews for clarity, facts, voice consistency
- Suggests revisions
- Output: `edit-notes.md` with specific changes

**Orchestrator Role:**
- Manages workflow
- Resolves conflicts between agents
- Approves final output

**When to Use:** High-stakes content; complex research needs; when you have time for deliberate process
**Effectiveness:** Highest quality; most time-intensive approach

---

### 4. Spiral Method (Dan Shipper)
Content conversion: one comprehensive asset spirals into 15-20 platform-specific pieces.

**Core Concept:**
- Start with one definitive long-form piece (8000+ words, maximal research)
- Spiral outward into smaller assets, each building on previous:

**Spiral Sequence:**
1. **Core Asset** (8000+ words) — Definitive guide, research compendium
2. **Medium-Form** (2000-3000) — Key sections extracted and reframed
3. **Short-Form** (400-800) — Tweetable/Linkedable summaries
4. **Social** (100-150 chars) — Hooks, angles, variations
5. **Email** (150-300) — Newsletter hooks, issue templates
6. **Podcast Notes** (300-500) — Episode summary, quotes, timestamps
7. **Community** (Slack/Discord snippets) — Micro-content for closed groups
8. **Visuals** (Infographics, slides) — Data/framework visualization

**When to Use:** Strategic pillar content; content campaigns; building asset libraries
**Effectiveness:** 5-10x ROI on initial research investment

---

### 5. Extended Thinking for Complex Documents
Allocate 16k+ token budgets for complex reasoning before writing:

**When to Trigger:**
- Novel frameworks or approaches
- Integration of many disparate sources
- Complex arguments requiring careful construction
- Strategic content with competitive implications

**Structure:**
```
PHASE 1: Extended thinking (16k tokens)
- Explore the landscape
- Test multiple frameworks
- Build the strongest argument
- Map dependencies and flow

PHASE 2: Write (8k tokens)
- Compose based on thinking phase
- Single-pass write without hesitation

PHASE 3: Polish (4k tokens)
- Final revisions and polish
```

**When to Use:** Strategic, high-stakes, complex content only (not every task)
**Effectiveness:** Prevents false starts; dramatically improves argument strength

---

### 6. Context Window Spanning
Save state and continue writing across multiple sessions/windows:

**Implementation:**
- Create `[filename]-state.md` with current progress and next steps
- Document structure outline, research summary, voice guide, completed sections
- Include "Next Section: [title] — Focus on [key points]"
- Resume with full state context + task

**Example State File:**
```markdown
# Writing State for [Project]

## Completed
- Section 1: Introduction ✓
- Section 2: Background ✓

## In Progress
- Section 3: Core Framework (30% complete)

## Todo
- Section 4: Case Studies
- Section 5: Implementation
- Editing pass

## Voice Notes
- Tone: Conversational, insider knowledge
- Structure: Problem → Framework → Case Studies → Action
- Target: CFOs, 10+ years experience

## Next Steps
Resume Section 3, focusing on the dependency mapping before moving to case studies.
```

**When to Use:** Long projects (20k+ words); when context window becomes constraint
**Effectiveness:** Enables completion of large projects without losing voice/coherence

---

### 7. Pillar Content Decomposition
One long-form piece expands into 15-20 platform-specific assets:

**High-Level Process:**

1. **Core Pillar** (10,000 words) — Comprehensive guide
2. **Extract Medium-Form** (5 pieces, 2000 words each) — Key sections
3. **Create Short-Form** (5 pieces, 500 words each) — Tweetable summaries
4. **Generate Social** (20-30 variations, 100-150 chars) — Platform-specific hooks
5. **Develop Email** (3-5 email sequences) — Newsletter angles
6. **Build Visual** (3-5 infographics) — Data/framework visuals
7. **Produce Audio** (Podcast script, 2000 words) — Spoken format

**Decomposition Logic:**
- Pillar → Medium-Form: Extract chapters as standalone pieces
- Medium-Form → Short-Form: Create executive summaries
- Short-Form → Social: Generate hooks, statistics, provocative questions
- Social → Email: Reverse-engineer from social to email narrative
- All → Visual: Identify frameworks, data, processes to visualize
- All → Audio: Script conversational version

**When to Use:** Major campaign launches; strategic content investments; building content libraries
**Effectiveness:** 8-12x ROI on initial pillar investment; consistent messaging across channels

---

## Output Control Patterns

### 1. Tell What TO DO, Not What NOT to Do
Positive framing consistently outperforms negative constraints:

**Poor:** "Don't use jargon. Don't be too academic. Don't sound corporate."
**Better:** "Use everyday language. Be conversational. Sound like a smart friend explaining something important."

**Why:** Brain processes positive instructions faster and more accurately than negatives.

**Application:**
- Replace "avoid passive voice" with "use active voice throughout"
- Replace "don't be vague" with "be specific with examples and data"
- Replace "no corporate speak" with "use direct, clear language"

**Exception:** Hard constraints that are non-negotiable can be negative ("No citations," "No external links")

---

### 2. XML Format Indicators for Prose Sections
Use XML tags to indicate desired formatting of output:

**Example:**
```xml
<prose>
Write the introduction as flowing paragraphs, not bullets.
Feel free to use dialogue and anecdotes.
Target 500-700 words.
</prose>

<listicle>
Then provide a top 5 list with short explanations.
Format as numbered list with bold titles.
</listicle>

<summary>
Close with a 2-3 sentence executive summary.
</summary>
```

**Effect:** Prevents format mixing; allows varied output within single task
**When to Use:** Complex documents with multiple section types

---

### 3. Match Prompt Formatting to Desired Output Formatting
The structure of your prompt should mirror the structure of desired output:

**Example:**
If you want a document with:
- Introduction paragraph
- Three case studies (each with title, problem, solution, result)
- Action steps
- Conclusion

**Structure your prompt:**
```
## INTRODUCTION
[Task description for intro section]

## CASE STUDY 1
[Task description with structure: Problem | Solution | Result]

## CASE STUDY 2
[Same structure]

## CASE STUDY 3
[Same structure]

## ACTION STEPS
[Structure for this section]

## CONCLUSION
[Structure for this section]
```

**Effect:** Reduces revision; output naturally mirrors desired structure

---

### 4. Structured Output with JSON Schemas
For consistent, repeatable formats, define JSON schema:

**Example Schema for Headlines:**
```json
{
  "headlines": [
    {
      "variation": "number",
      "headline": "string",
      "subheadline": "string",
      "target_emotion": "string",
      "reasoning": "string"
    }
  ]
}
```

**When to Use:** Creating multiple variations of same format; API-compatible output; templated content
**Effectiveness:** 95%+ consistency in output format

---

### 5. Style Transfer via Writing Samples + Style Description
Provide a reference sample to establish tone/voice:

**Structure:**
```
## REFERENCE SAMPLE
[Paste 2-3 paragraphs of desired style]

## STYLE ANALYSIS
- Sentence length: Short, punchy (5-15 words average)
- Vocabulary: Everyday words, minimal jargon
- Tone: Conversational, insider knowledge, slightly irreverent
- Structure: Short declarative sentences, occasional longer complex sentences
- Metaphors: Industry-specific analogies

Now write [task] in this style.
```

**When to Use:** Matching established brand voice; teaching specific tone
**Effectiveness:** 70%+ improvement in voice consistency vs description alone

---

### 6. Custom Styles Feature
Leverage Claude's custom styles capability for preset response styles:

**How to Use:**
- Define a style once: "GrowthX Direct" = short sentences, active voice, no jargon, specific examples
- Reference in subsequent prompts: "Write in GrowthX Direct style"
- Claude applies preset formatting automatically

**When Available:** On Claude.ai, some Claude implementations, and certain integrations

---

### 7. Reading Level Optimization
Target Flesch Reading Ease score of 60-70 for most B2B content:

**Scoring Formula:**
- 90-100: Easy (5th grade)
- 60-70: Standard (college level) — **Target for B2B**
- 30-50: Difficult (graduate level)
- Below 30: Very difficult (academic)

**Achieving 60-70:**
- Average sentence length: 15-20 words
- Average word length: 4-5 characters
- Limit percentage of three-syllable+ words to 10-15%
- Use active voice (70%+)
- Break complex ideas into multiple sentences

**Quick Check:** Read aloud at normal pace. If you need to pause mid-sentence for breath, it's too complex.

**When to Use:** Any content for busy executives; accessibility priority
**Effectiveness:** 40% improvement in engagement and comprehension

---

## Quality Patterns

### 1. Self-Check Prompting
Build verification into the prompt itself:

**Structure:**
```
Write [task].

Before finishing, verify:
1. Does every claim have supporting evidence?
2. Is the tone consistent throughout?
3. Does it answer the reader's implicit questions?
4. Would a skeptical reader find this persuasive?
5. Is it under [word count]?

Only output the final version after self-check.
```

**When to Use:** Any high-stakes output; content requiring accuracy
**Effectiveness:** Catches 30-40% more errors vs no verification step

---

### 2. SELF-REFINE Loop
Systematic feedback + diagnosis + refinement:

**Cycle:**
1. **Initial Output** — First draft/attempt
2. **Feedback** — Specific critique (not vague, be precise)
3. **Diagnosis** — Why feedback applies; root cause analysis
4. **Refinement** — Targeted revision addressing diagnosis

**Example:**
```
FEEDBACK: The opening is too generic. Doesn't differentiate from other content on this topic.

DIAGNOSIS: The opening describes the problem (AI is changing marketing) without revealing the unique angle. The reader could get this from 100 other articles.

REFINEMENT: Rewrite opening to reveal the specific insight: [specific angle]. Make the reader think "oh, I hadn't considered this angle."
```

**When to Use:** Iterative improvement; when initial output is close but needs refinement
**Effectiveness:** Each cycle improves output 20-30%

---

### 3. Rubric-Based Evaluation
Define evaluation criteria with performance levels:

**Example Rubric:**
| Criteria | Excellent (4) | Good (3) | Fair (2) | Poor (1) |
|----------|--------------|---------|---------|---------|
| **Clarity** | Crystal clear; reader never confused | Generally clear; one ambiguous section | Some unclear passages; requires re-reading | Confusing throughout |
| **Evidence** | Every claim supported by data/example | Most claims supported; 1-2 gaps | Some claims unsupported | Few claims supported |
| **Voice** | Consistent, unmistakably GrowthX | Mostly consistent; few tone shifts | Some voice inconsistency | Voice unclear or inconsistent |
| **Structure** | Flows perfectly; easy to follow | Good flow; logical progression | Organization could be clearer | Disjointed, hard to follow |

**Usage:** Before finalizing, rate against rubric. Revise any section scoring below 3.

**When to Use:** Quality gates; before client handoff; self-evaluation
**Effectiveness:** Objective quality measurement; prevents subjective debates

---

### 4. Adaptive Thinking vs Extended Thinking for Different Task Complexities

**Adaptive Thinking (Fast):**
- Use for straightforward writing tasks
- Headlines, social copy, short-form content
- Well-established formats and approaches
- Execution focus, not exploration

**Extended Thinking (Slow):**
- Use for novel frameworks or complex arguments
- Integration of many disparate sources
- Strategic decisions between multiple approaches
- Research synthesis and original frameworks

**Decision Rule:**
- If you know the approach, use adaptive (fast)
- If you're unsure how to approach it, use extended (slow)

---

### 5. Ground Responses in Quotes from Source Documents First
Establish factual foundation before interpretation:

**Structure:**
```
## EVIDENCE
[Quote 1 from source]
"[Direct quote]" — [Source]

[Quote 2 from source]
"[Direct quote]" — [Source]

## INTERPRETATION
Based on this evidence, here's what it means:
[Your analysis and synthesis]

## APPLICATION
In the context of [domain], this means:
[Practical implication]
```

**When to Use:** Research-heavy content; content requiring credibility
**Effectiveness:** Increases perceived authority 50%+; easier to fact-check

---

## Framework Patterns

### 1. RACE Framework
Role, Action, Context, Execute — covers 80% of daily writing prompts:

**Structure:**
- **Role**: "You are a [specific role]"
- **Action**: "Write [specific deliverable]"
- **Context**: "[Background, constraints, audience]"
- **Execute**: "[Go!]"

**Example:**
```
Role: You are a B2B content strategist specializing in AI visibility.

Action: Write a 1200-word article.

Context:
- Target: CMOs at $50M+ companies
- Tone: Insider knowledge, conversational
- Angle: How to measure AI visibility of competitors
- Format: Article with sections and examples

Execute: Write the article now.
```

**When to Use:** Most writing tasks (simple → moderate complexity)
**Effectiveness:** Works 80% of the time with standard quality

---

### 2. CRISPE Framework
Capacity/Role, Insight, Statement, Personality, Experiment:

**Structure:**
- **Capacity/Role**: Define expertise and perspective
- **Insight**: Reveal unique angle or understanding
- **Statement**: Core message in one sentence
- **Personality**: How you'll show up (tone, voice)
- **Experiment**: What you'll try differently

**Example:**
```
Capacity: You're a former VP of Marketing at a $500M SaaS company, now an advisor.

Insight: Most marketing teams measure the wrong thing — they track visibility, not decision-influence.

Statement: The next competitive advantage is making AI decisions visible to the right stakeholder, not just visible.

Personality: You write like a mentor — wise, slightly provocative, always specific with examples.

Experiment: Use surprising statistics and reverse conventional wisdom once per section.
```

**When to Use:** Content requiring strong POV; when you want personality to shine
**Effectiveness:** 70%+ improvement in POV clarity and distinctiveness

---

### 3. CO-STAR Framework
Context, Objective, Style, Tone, Audience, Response Format:

**Structure:**
```
Context: [Background situation]

Objective: [What you want to achieve; desired outcome]

Style: [Writing approach and structure]

Tone: [Emotional tenor and attitude]

Audience: [Who is reading; what they care about]

Response Format: [How output should be structured]
```

**Example:**
```
Context: We're launching a new AI visibility product in a crowded market.

Objective: Create a landing page headline that differentiates us and captures attention.

Style: Provocative but credible; challenges conventional thinking.

Tone: Confident insider, not hype-y marketer.

Audience: Marketing leaders at B2B tech companies, skeptical of AI claims.

Response Format:
- Main headline (60 chars max)
- Subheadline (90 chars max)
- 2-3 sentence supporting statement
- Brief reasoning for why this approach works
```

**When to Use:** Complex multi-dimensional tasks; when all dimensions matter equally
**Effectiveness:** High - ensures all dimensions are considered

---

### 4. AIDA / PAS / BAB Applied to LLM Prompting
Copywriting frameworks adapted for AI prompting:

**AIDA (Attention, Interest, Desire, Action):**
- **Attention**: Hook with surprising insight or stat
- **Interest**: Develop the insight; why does it matter?
- **Desire**: Show the benefit of understanding this
- **Action**: Clear next step for reader

**PAS (Problem, Agitation, Solution):**
- **Problem**: What's wrong with status quo?
- **Agitation**: Why should they care urgently?
- **Solution**: How do you fix it?

**BAB (Before, After, Bridge):**
- **Before**: Current unsatisfying situation
- **After**: Desired future state
- **Bridge**: How to get from before to after

**When Applying to Prompts:**
Structure your request to follow AIDA/PAS/BAB logic, so the AI naturally follows that flow:

```
[ATTENTION] Here's what most marketers get wrong about AI visibility:

[INTEREST] The real advantage isn't knowing your competitors' AI capabilities —

[DESIRE] It's knowing which AI decisions actually influence buying. Here's why:

[ACTION] Write an article that moves the reader through this journey.
```

**When to Use:** Persuasive or narrative content; when you want reader transformation
**Effectiveness:** More engaging narratives; higher conversion on CTAs

---

### 5. 3 C's Framework
Context, Constraints, Creativity:

**Structure:**
- **Context**: What's the situation? What led us here?
- **Constraints**: What are the real boundaries? (Not just "be concise" — what specifically?)
- **Creativity**: Where can we be bold? What's not constrained?

**Example:**
```
Context: We've been positioning as a data tool. We want to shift to "decision confidence."

Constraints:
- Cannot claim to reduce risk (legal won't approve)
- Must work for both technical and non-technical audiences
- Cannot make AI sound less scary (honesty is brand)

Creativity:
- Play with the "confidence" angle in unexpected ways
- Lean into the tension between power and responsibility
- Challenge conventional AI marketing language
```

**When to Use:** Strategy and positioning work; content needing both boundaries and permission to experiment
**Effectiveness:** Prevents overly conservative outputs; gives AI freedom within guardrails

---

## Meta Notes

**Research Methodology:** These patterns compiled from:
- Claude API documentation and best practices
- Prompt engineering research (Anthropic, OpenAI, academic papers)
- Field testing across GrowthX writing projects
- Pattern recognition across 100+ writing prompts

**Update Cadence:** Add patterns as discovered. Move tested patterns from "experimental" to "proven" section.

**Cross-References:**
- See `context/voice/writing-style-context-v2.md` for GrowthX-specific voice
- See `.cursor/skills/copywriting/SKILL.md` for copywriting-specific patterns
- See `.cursor/skills/growthx-writing/SKILL.md` for GrowthX writing workflow

**Versioning:** This is v1. Major revisions will spawn v2 and move old to /archive/.
