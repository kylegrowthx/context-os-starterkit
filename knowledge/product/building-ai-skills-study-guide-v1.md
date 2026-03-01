# Building Skills for Claude, Claude Code & Cursor — Study Guide

> **For:** Marcel Santilli, CEO of GrowthX — AI-native B2B content agency
> **Goal:** Build better, more effective skills across Claude Code and Cursor for GrowthX workflows
> **Time Investment:** 40-60 hours (comprehensive)
> **Last Updated:** 2026-02-27
> **Sources:** 500+ (deduplicated across 14 research categories)

## How to Use This Guide

This is a reference document, not a linear course. The field of AI coding assistants and skills is expanding rapidly, and this guide captures the current state as of February 2026. Skip around based on what you're building next.

**Start here if you're new to skills:** Read Part 1 for foundations, then jump to Part 2 (Claude Code) or Part 3 (Cursor) depending on your primary tool.

**Start here if you know prompt engineering but not skills:** Jump directly to Part 2 or 3 — skills are prompt engineering applied to automation and agent loops.

**Start here if you're building complex workflows:** Read Part 6 (Agentic AI) and Part 8 (Skill Architecture).

The appendices are organized by topic — use Appendix A as a research library and reference tool.

---

## Part 1: Foundations — What Skills Are and Why They Matter

### 1.1 The Skill Paradigm Shift

For the first decade of modern AI coding assistants, the dominant pattern was autocomplete. GitHub Copilot, for instance, watched your keystrokes and predicted the next line of code. It was fast, lightweight, and context-aware within a single file.

Around 2024-2025, the paradigm shifted. As transformer models grew more capable and prompt engineering matured, AI coding assistants evolved beyond autocomplete. The new pattern is **agent mode**: tools that can reason across larger contexts, chain operations together, call external APIs, and maintain state across multiple turns of conversation.

Skills emerged from this shift as the fundamental unit of reusable agent capability. A **skill** is a declarative specification of a repeatable task that an AI agent can learn and execute. Unlike a traditional function, a skill includes not just *what to do* but also *how to explain what to do to the AI*. It combines:

1. **Trigger** — A description of when/why the skill should run
2. **Instructions** — Detailed steps, context, constraints, and examples
3. **Context** — Background knowledge, templates, or reference material
4. **Output spec** — How the result should be formatted or delivered

The emergence of skills reflects a deeper truth: AI agents don't execute code directly like traditional programs. Instead, they read instructions and reason about how to accomplish them. This means the quality of instruction writing directly determines the quality of AI performance — more than it ever did for human developers.

Claude Code skills, Cursor rules, GitHub Copilot instructions, and MCP servers are all different implementations of this same fundamental idea. They're all ways of teaching an AI agent to do something reliably, repeatably, and well.

**Why this matters for GrowthX:** You operate at the intersection of content, strategy, and AI. Skills let you teach Claude, Cursor, and other agents your voice, your processes, and your strategic thinking. Instead of repetitively explaining "this is how we write" or "this is how we approach competitor research," you encode that knowledge once in a skill and reuse it across projects. At scale, this multiplies your leverage.

### 1.2 Anatomy of a Skill

All modern skills follow a common structure. Let's break down the universal elements, then see how they differ across tools.

**Universal Elements:**

1. **Name/ID** — A short, descriptive identifier (e.g., `growthx-writing`, `competitor-research`)
2. **Trigger/Description** — Plain English description of when and why to use this skill. Examples: "Write LinkedIn posts in GrowthX voice," "Pull meeting transcript from Fireflies"
3. **Metadata** — Type, category, tags, version, author, last_updated (varies by tool, but all have some form of this)
4. **Instructions** — The core logic. This is typically the largest section. It includes:
   - Clear, sequential steps
   - Examples or demonstrations (few-shot prompting)
   - Constraints and guardrails
   - Format specifications
   - When to ask for clarification vs. proceeding
5. **Context/Reference Material** — External docs, templates, style guides, personas, decision trees
6. **Input/Output Spec** — What the skill expects to receive and what it should produce

**How Skills Differ Across Tools:**

| Aspect | Claude Code SKILL.md | Cursor Rules (.cursorrules) | GitHub Copilot instructions.md | MCP Server |
|--------|-----|-----|-----|-----|
| **Format** | Markdown with YAML frontmatter | Text or markdown | Markdown or JSON | TypeScript/Python server |
| **Storage** | `.cursor/skills/[name]/SKILL.md` | `.cursorrules` or `.cursor/rules/` | `.github/copilot-instructions.md` | Separate codebase |
| **Scope** | Slash commands, custom actions | Project-wide, IDE-wide | Repository-wide | External tools/APIs |
| **Trigger** | Explicit (`/skill-name`) or keyword-based | Always-on or file-glob-based | Always-on | Tool invocation |
| **Execution** | In-message (Claude Code reads it) | In-editor (Cursor reads it) | In-editor (Copilot reads it) | RPC call (external) |
| **Capabilities** | Reasoning, planning, content generation | Context management, code patterns | Autocompletion, suggestions | Function calling, tool use |

The pattern is consistent: all of them are instructional documents that teach an AI agent how to behave. The differences are in *scope* (single-file vs. project vs. external) and *mechanism* (in-context vs. file-based vs. protocol-based).

### 1.3 Key Mental Models

**Model 1: Context Window as Scarce Resource**

Every skill you write competes for space in the AI's context window. A modern Claude or Copilot has 200k tokens of context (roughly 150k words), but you don't own all of that. Some is used for conversation history, file content, previous responses, and system prompts.

This means: *good skills are dense, not verbose*. They pack maximum signal into minimum tokens. Compare two approaches:

Bad approach:
```
This is a skill for writing content in the GrowthX voice. We are a B2B
content marketing agency founded in 2019. We specialize in SEO-optimized
thought leadership for SaaS companies. Our ideal clients are VP+ at
growth-focused tech firms. Our writing is direct, clear, and real...
[continues for 500 words about the company]
```

Good approach:
```
**GrowthX Voice:** B2B content marketing agency. Writing style: direct,
clear, real — no jargon, no filler, no passive voice. Audience:
VP+ at growth-focused SaaS. Example: [one strong piece]. Reference:
context/voice/writing-style-context-v2.md
```

The second approach uses links and references instead of full repetition. It's less than 1/5 the tokens.

**Model 2: Prompt-as-Code**

Traditional code is a set of instructions for a computer to execute. Prompts are instructions for an AI to interpret and reason about.

This distinction matters because:
- Code is deterministic; prompts are probabilistic
- Code syntax matters; prompt semantics matter
- Code is optimized for readability by humans who know the language; prompts are optimized for clarity to a language model

Treating prompts as code means applying software engineering disciplines:
- **Versioning** (`writing-skill-v2.md` vs. `writing-skill-v3.md`)
- **Testing** (does this prompt produce expected outputs across 10 test cases?)
- **Composition** (can this skill call other skills?)
- **Documentation** (what does this do? when should it be used?)

This is still emerging as a discipline, but the best teams (Anthropic, Vercel, Cursor) are moving this direction.

**Model 3: Declarative vs. Imperative**

Most skills are **imperative** — they say "do this, then that." Example: "First, research the competitor. Second, extract pricing. Third, summarize strengths."

Some tools support **declarative** — they say "this is the desired outcome; figure out how." Example: ".cursorrules says 'Always use TypeScript for new files' and Cursor figures out when/how to apply it."

Declarative skills are more reusable because they're less prescriptive. But imperative skills are easier to debug because you see exactly what's happening step-by-step.

Best practice: Use declarative rules for constraints and standards, imperative instructions for complex workflows.

**Model 4: Skill Composition**

The most advanced teams build skills that call other skills. For example, your GrowthX "pull meeting" skill might internally chain:
1. Download transcript from Fireflies (Fireflies MCP)
2. Enrich transcript with speaker names and roles (speaker-enrichment skill)
3. Extract action items (action-item-extraction skill)
4. Link to contacts (contact-linking skill)
5. Update Notion (Notion MCP)

This composition is powerful because it avoids repetition and lets you evolve individual skills independently.

---

## Appendix A: Curated Source Library

Organize ALL sources (500+) into these categories. Use this format for each:
- **[Title]** — URL — Type (doc/blog/repo/guide/video/tutorial/research) — 1-line summary


### A1. Claude Code & Claude Skills (Official Docs & Guides)

[1]. **10-Step Prompt Structure Guide** — https://aimaker.substack.com/p/the-10-step-system-prompt-structure-guide-anthropic-claude — guide — Anthropic Claude prompt structure
[2]. **20 Claude Code CLI Commands That Will Make You a Terminal Wizard** — https://rowanblackwoon.medium.com/20-claude-code-cli-commands-that-will-make-you-a-terminal-wizard-e22fd4365496 — blog — Essential CLI commands for power users
[3]. **2025 Complete Guide to Fixing Claude API 429 Errors** — https://www.cursor-ide.com/blog/claude-api-429-error-fix-en — guide — Rate limiting solutions
[4]. **5 Must-Have QA Skills for Claude Code in 2026** — https://qaskills.sh/blog/must-have-qa-skills-claude-code-2026 — guide — QA-focused skill guide
[5]. **5 Ways to Integrate Claude Code Into Your GitHub Workflow** — https://medium.com/@homotechnologicus/5-ways-to-integrate-claude-code-into-your-github-workflow-3eee785c7b62 — blog — Five strategies for GitHub workflow integration
[6]. **9 Ways Claude Code Helps Me with Testing and Debugging** — https://medium.com/@joe.njenga/9-ways-claude-code-helps-me-with-testing-and-debugging-like-a-pro-tester-69c8776282ab — blog — Nine practical debugging strategies
[7]. **@anthropic-ai/claude-agent-sdk** — https://www.npmjs.com/package/@anthropic-ai/claude-agent-sdk — Repo — Claude Agent SDK npm package
[8]. **A complete guide to Claude Code permissions** — https://www.eesel.ai/blog/claude-code-permissions — blog — Comprehensive permissions guide
[9]. **A complete guide to Claude pricing in 2025** — https://www.eesel.ai/blog/claude-pricing — guide — Comprehensive 2025 pricing guide
[10]. **A complete guide to hooks in Claude Code** — https://www.eesel.ai/blog/hooks-in-claude-code — blog — Complete guide to Claude Code hooks and automation
[11]. **A Comprehensive Guide to the Claude Code SDK** — https://apidog.com/blog/a-comprehensive-guide-to-the-claude-code-sdk/ — guide — SDK comprehensive guide
[12]. **A developer's guide to the Claude Code JetBrains integration** — https://www.eesel.ai/blog/claude-code-jetbrains-integration — blog — Complete JetBrains integration guide
[13]. **A Month with Cursor and Claude-Dev: My Thoughts** — https://jasonroell.com/2024/10/10/a-month-with-cursor-and-claude-dev-my-thoughts/ — blog — Month-long experience report
[14]. **A Native IDE for Claude Code** — https://eclipsesource.com/blogs/2025/12/02/theiacon-2025-native-claude-code-ide-integration/ — blog — EclipseSource blog on Claude Code IDE
[15]. **A practical guide to automating git workflows with Claude Code** — https://www.eesel.ai/blog/git-workflows-claude-code — blog — Git automation with Claude Code
[16]. **A practical guide to debug with Claude Code in 2025** — https://www.eesel.ai/blog/debug-with-claude-code — guide — 2025 debugging best practices
[17]. **A practical guide to the Claude code context window size** — https://www.eesel.ai/blog/claude-code-context-window-size — blog — Practical guide to understanding context window sizes
[18]. **A practical guide to the Claude Code GitHub integration** — https://www.eesel.ai/blog/claude-code-github-integration — blog — Practical guide to GitHub integration workflow
[19]. **A practical guide to your terminal configuration for Claude Code** — https://www.eesel.ai/blog/terminal-configuration-claude-code — blog — Terminal configuration best practices
[20]. **A week with Claude Code: lessons, surprises and smarter workflows - DEV Community** — https://dev.to/ujja/a-week-with-claude-code-lessons-surprises-and-smarter-workflows-23ip — blog — Developer's week-long experience with Claude Code and lessons learned
[21]. **Add Function Calling to Your Twilio Voice and Claude ConversationRelay Integration** — https://www.twilio.com/en-us/blog/developers/tutorials/product/function-calling-twilio-voice-anthropic-claude-integration — tutorial — Tutorial integrating Claude function calling with Twilio
[22]. **Agent Browser: Web Automation Skill for Claude Code** — https://mcpmarket.com/tools/skills/agent-browser-1 — Doc — MCP Market's agent browser documentation
[23]. **Agent SDK overview - Claude API Docs** — https://platform.claude.com/docs/en/agent-sdk/overview — doc — Official Agent SDK overview and capabilities
[24]. **Agent SDK overview - Claude Docs** — https://docs.claude.com/en/api/agent-sdk/overview — Doc — Claude Agent SDK documentation
[25]. **Agent SDK reference - Python - Claude API Docs** — https://platform.claude.com/docs/en/agent-sdk/python — doc — Complete Python API reference for Agent SDK
[26]. **Agent SDK reference - TypeScript - Claude API Docs** — https://platform.claude.com/docs/en/agent-sdk/typescript — doc — TypeScript API reference
[27]. **Agent Skills - Claude API Docs** — https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview — doc — Overview of agent skills architecture and usage
[28]. **Agentic Workflows with Claude: Architecture Patterns, Design Principles & Production Patterns** — https://medium.com/@reliabledataengineering/agentic-workflows-with-claude-architecture-patterns-design-principles-production-patterns-72bbe4f7e85a — blog — Deep dive into agentic workflow architecture
[29]. **Agents That Build Agents - Building Autonomous Browsing with Claude Code** — https://dev.to/viniciusdallacqua/agents-that-build-agents-building-autonomous-browsing-with-claude-code-pn5 — Blog — DEV Community's Claude browser guide
[30]. **AI agents | Claude** — https://claude.com/solutions/agents — guide — Anthropic's guide to building AI agents with Claude
[31]. **AI Learning Resources & Guides from Anthropic** — https://www.anthropic.com/learn — doc — Central Anthropic learning resources hub
[32]. **Alignment Science Blog - Anthropic** — https://alignment.anthropic.com/ — blog — Anthropic's alignment research blog
[33]. **Alignment studies from Anthropic** — https://dx13.co.uk/articles/2025/01/04/ai-alignment/ — article — Summary of Anthropic alignment studies
[34]. **Anthropic Academy: Claude API Development Guide** — https://www.anthropic.com/learn/build-with-claude — guide — Official Anthropic learning platform with courses on Claude development
[35]. **Anthropic brings 'extended thinking' to Claude** — https://www.rdworldonline.com/anthropic-brings-extended-thinking-to-claude-which-can-solve-complex-physics-problems-with-96-5-accuracy/ — article — Article on extended thinking capabilities and performance improvements
[36]. **Anthropic Courses** — https://anthropic.skilljar.com/ — course — Official Anthropic course platform
[37]. **Anthropic Launches Message Batches API** — https://aiintransit.medium.com/anthropic-launches-message-batches-api-for-cost-effective-querying-with-claude-ai-3bd4ba3a003e — blog — Article on batch API capabilities and benefits
[38]. **Anthropic Launches Skills and Microsoft 365 Integration for Claude** — https://www.theneuron.ai/explainer-articles/anthropic-launches-skills-and-microsoft-365-integration-for-claude-transform-your-ai-assistant-into-a-specialized-expert — blog — The Neuron article on Claude Skills and integration
[39]. **Anthropic Prompt Library Examples** — https://www.aipromptlibrary.app/blog/anthropic-prompt-library-examples — article — Anthropic example prompts
[40]. **Anthropic Research** — https://www.anthropic.com/research — doc — Research page listing papers and projects
[41]. **Anthropic Research-Backed Prompting** — https://promptgenius.net/prompts/chatgpt/resources/anthropic-guide — resource — Research-backed Anthropic guide
[42]. **Anthropic Tool Calling - Exa** — https://docs.exa.ai/reference/anthropic-tool-calling — Doc — Exa's Anthropic tool calling guide
[43]. **Anthropic's Claude Code Comes to Web and Mobile** — https://thenewstack.io/anthropics-claude-code-comes-to-the-web-and-mobile/ — article — New Stack article on web deployment
[44]. **Anthropic's Claude Code: What CEOs Must Know About Security** — https://businesschief.com/news/anthropics-claude-code-what-ceos-must-know-about-security — article — Executive summary of security considerations
[45]. **Apple's Xcode now supports the Claude Agent SDK** — https://www.anthropic.com/news/apple-xcode-claude-agent-sdk — Blog — Anthropic's Xcode Claude SDK announcement
[46]. **Automate Your Documentation with Claude Code & GitHub Actions** — https://medium.com/@fra.bernhardt/automate-your-documentation-with-claude-code-github-actions-a-step-by-step-guide-2be2d315ed45 — guide — Documentation automation guide
[47]. **Automated Documentation with Claude Code: Docusaurus Agent** — https://medium.com/@dan.avila7/automated-documentation-with-claude-code-building-self-updating-docs-using-docusaurus-agent-2c85d3ec0e19 — guide — Docusaurus documentation automation
[48]. **Batch processing - Claude API Docs** — https://platform.claude.com/docs/en/build-with-claude/batch-processing — doc — Official batch processing API documentation
[49]. **Benchmark System · ruvnet/claude-flow Wiki** — https://github.com/ruvnet/claude-flow/wiki/Benchmark-System — wiki — Benchmarking system architecture
[50]. **Best practices and lessons for fine-tuning Anthropic's Claude 3 Haiku** — https://aws.amazon.com/blogs/machine-learning/best-practices-and-lessons-for-fine-tuning-anthropics-claude-3-haiku-on-amazon-bedrock/ — blog — Best practices for fine-tuning
[51]. **Best Practices for Claude Code - Claude Code Docs** — https://code.claude.com/docs/en/best-practices — doc — Official Claude Code best practices documentation covering workflows and optimization
[52]. **Best practices for Claude Code subagents** — https://www.pubnub.com/blog/best-practices-for-claude-code-sub-agents/ — blog — Best practices for effective subagents
[53]. **Browser MCP - Automate your browser using VS Code, Cursor, Claude, and more** — https://browsermcp.io/ — Doc — Browser MCP homepage
[54]. **Build AI Agents with Claude Agent SDK and Microsoft Agent Framework** — https://devblogs.microsoft.com/semantic-kernel/build-ai-agents-with-claude-agent-sdk-and-microsoft-agent-framework/ — blog — Guide integrating Claude with Microsoft agent frameworks
[55]. **Build RAG With Claude 3.5 & Pgvector** — https://www.tigerdata.com/blog/retrieval-augmented-generation-with-claude-sonnet-3-5-and-pgvector — guide — Guide to RAG with pgvector
[56]. **Building a Community | Adventures in Claude** — https://adventuresinclaude.ai/posts/2026-02-16-building-a-community — blog — Community building with Claude
[57]. **Building a RAG Application in 10 min with Claude 3 and Hugging Face** — https://medium.com/@myscale/building-a-rag-application-in-10-min-with-claude-3-and-hugging-face-10caea4ea293 — guide — Quick RAG implementation guide
[58]. **Building agents with the Claude Agent SDK** — https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk — blog — Anthropic engineering blog on agent SDK usage
[59]. **Building AI-driven workflows powered by Claude Code and other tools** — https://uxdesign.cc/designing-with-claude-code-and-codex-cli-building-ai-driven-workflows-powered-by-code-connect-ui-f10c136ec11f — blog — UX-focused guide to building AI-driven workflows
[60]. **Building an Agentic Workflow in Claude that Researches, Writes and Publishes Content** — https://medium.com/@niall.mcnulty/building-an-agentic-workflow-in-claude-that-researches-writes-and-publishes-content-automatically-3ec08ff6f56f — blog — Tutorial on building automated research and publishing workflows
[61]. **Building Effective Agents with Anthropic's Best Practices and smolagents** — https://huggingface.co/blog/Sri-Vigneshwar-DJ/building-effective-agents-with-anthropics-best-pra — Blog — Hugging Face's effective agents guide
[62]. **Building Effective AI Agents** — https://www.anthropic.com/research/building-effective-agents — Blog — Anthropic's agent building research
[63]. **Building Effective AI Agents: A Guide from Anthropic** — https://medium.com/accredian/building-effective-ai-agents-a-guide-from-anthropic-e66b533ff091 — Blog — Accredian's Anthropic guide
[64]. **Building with extended thinking - Claude API Docs** — https://platform.claude.com/docs/en/build-with-claude/extended-thinking — doc — Documentation on extended thinking capability
[65]. **Building with MCP: Anthropic Guidance and Code Execution** — https://obot.ai/resources/learning-center/mcp-anthropic/ — Blog — Obot's MCP and code execution guide
[66]. **Can Claude Code generate documentation from code** — https://milvus.io/ai-quick-reference/can-claude-code-generate-documentation-from-code — article — Q&A on documentation generation
[67]. **Can Claude Code help write unit tests** — https://milvus.io/ai-quick-reference/can-claude-code-help-write-unit-tests — article — Q&A on test generation
[68]. **Can Claude Code Really Generate Professional Documentation** — https://apidog.com/blog/claude-code-generate-documentation-from-code/ — article — Analysis of documentation generation
[69]. **Can Claude Code refactor legacy code** — https://milvus.io/ai-quick-reference/can-claude-code-refactor-legacy-code — article — Q&A on legacy refactoring
[70]. **Checkpoints for Claude Code - Never lose your work again** — https://claude-checkpoints.com/ — guide — Guide to checkpoint system
[71]. **Claude & Discourse-related development** — https://meta.discourse.org/t/claude-discourse-related-development-how-good-is-it/394773/2 — forum — Community forum discussion on Claude integration
[72]. **Claude (language model) - Wikipedia** — https://en.wikipedia.org/wiki/Claude_(language_model) — article — Wikipedia overview of Claude
[73]. **Claude 4.5 Benchmarks on Hugging Face and Industry Coding Standards** — https://huggingface.co/blog/Laser585/claude-4-benchmarks — blog — Benchmark analysis on HuggingFace
[74]. **Claude 4.5: Function Calling and Tool Use - Composio** — https://composio.dev/blog/claude-function-calling-tools — blog — Guide to implementing function calling with Claude 4.5
[75]. **Claude : Retrieval Augmented Generation** — https://medium.com/@judeaugustinej/claude-retrieval-augmented-generation-810f36fd6fce — blog — Medium article on Claude RAG implementation
[76]. **Claude Agent SDK Tutorial: Create Agents Using Claude Sonnet 4.5** — https://www.datacamp.com/tutorial/how-to-use-claude-agent-sdk — Guide — DataCamp's Claude Agent SDK tutorial
[77]. **Claude Agent SDK | Promptfoo** — https://www.promptfoo.dev/docs/providers/claude-agent-sdk/ — doc — Promptfoo integration guide
[78]. **Claude AI by Anthropic - first impression** — https://forum.aiprm.com/t/claude-ai-by-anthropic-first-impression/16635 — forum — Community impressions and discussions
[79]. **Claude AI Custom Instructions: A Real Example That Actually Works** — https://www.jdhodges.com/blog/claude-ai-custom-instructions-a-real-example-that-actually-works/ — blog — Real-world example of working custom instructions
[80]. **Claude AI for Enterprises and Developers** — https://theaichronicler.com/claude-ai-for-enterprises-and-developers-a-privacy-focused-long-context-assistant-use-cases-best-practices-integration-tips/ — guide — AI Chronicler guide on Claude enterprise use
[81]. **Claude API Structured Output: Complete Guide to Schema-Guaranteed Responses** — https://thomas-wiegold.com/blog/claude-api-structured-output/ — guide — Schema-guaranteed responses guide
[82]. **Claude Best Practices Anthropic** — https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices — doc — Official Claude best practices
[83]. **Claude Browser Agent: Automate Any Website Task Instantly** — https://juliangoldie.com/claude-browser-agent/ — Blog — Julian Goldie's browser agent guide
[84]. **Claude Code + Microsoft Foundry: Enterprise AI Coding Agent Setup** — https://devblogs.microsoft.com/all-things-azure/claude-code-microsoft-foundry-enterprise-ai-coding-agent-setup/ — blog — Microsoft guide on Claude Code enterprise setup
[85]. **Claude Code 2.0: Checkpoints, Subagents, and Autonomous Coding** — https://skywork.ai/blog/claude-code-2-0-checkpoints-subagents-autonomous-coding/ — blog — Overview of version 2.0 features
[86]. **Claude Code 2.0: VS Code Extension + 30h Autonomous Coding** — https://smartscope.blog/en/generative-ai/claude/claude-code-2-0-release/ — blog — Release notes for Claude Code 2.0
[87]. **Claude Code [Beta] - IntelliJ IDEs Plugin | Marketplace** — https://plugins.jetbrains.com/plugin/27310-claude-code-beta- — doc — JetBrains marketplace listing for Claude Code
[88]. **Claude Code arrives on the web** — https://tessl.io/blog/anthropic-brings-claude-code-to-the-web-and-mobile/ — blog — Article on web and mobile release
[89]. **Claude Code Assistant Plugin for JetBrains IDEs** — https://plugins.jetbrains.com/plugin/29457-claude-code-assistant — doc — Official assistant plugin for JetBrains
[90]. **Claude Code Automatic PR Documentation Generator** — https://github.com/marketplace/actions/claude-code-automatic-pr-documentation-generator — tool — GitHub Actions for auto documentation
[91]. **Claude Code Automation Cookbook: Recipes for AI Agents** — https://egghead.io/courses/claude-code-automation-cookbook-recipes-for-ai-agents — course — Course on automation recipes for Claude Code
[92]. **Claude Code Batch API Complete Guide: Large-scale Processing and CI/CD Automation** — https://smartscope.blog/en/generative-ai/claude/claude-code-batch-processing/ — guide — Comprehensive batch API guide with CI/CD automation
[93]. **Claude Code Best Practices · Claude Code Best Practices** — https://rosmur.github.io/claudecode-best-practices/ — guide — Community-driven best practices resource
[94]. **Claude Code Best Practices: Tips from Power Users for 2025** — https://www.sidetool.co/post/claude-code-best-practices-tips-power-users-2025 — blog — Power user tips for 2025
[95]. **Claude Code Context Window: Optimize Your Token Usage** — https://claudefa.st/blog/guide/mechanics/context-management — guide — Guide to token usage optimization
[96]. **Claude Code Deep Thinking: Unlock Better Results** — https://claudefa.st/blog/guide/performance/deep-thinking-techniques — guide — Guide to deep thinking techniques in Claude Code
[97]. **Claude Code Down in 2026: Complete Status Guide** — https://www.adventureppc.com/blog/claude-code-down-in-2026-complete-status-guide-error-fixes-what-to-do-during-outages — guide — Outage handling guide
[98]. **Claude Code for Data Analysis** — https://vincent.codes.finance/posts/claude-code-data-analysis/ — blog — Finance-focused data analysis
[99]. **Claude Code for data science: A first look** — https://www.sjoerddehaan.com/tech/claude-code-data-science-1.html — blog — Data science first impressions
[100]. **Claude Code for Enterprise | Claude by Anthropic** — https://claude.com/product/claude-code/enterprise — doc — Enterprise product page
[101]. **Claude Code for Scientists** — https://www.neuroai.science/p/claude-code-for-scientists — blog — Scientific computing with Claude Code
[102]. **Claude Code for Scientists - DeepLearning.AI** — https://learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant/lesson/33kzr/refactoring-a-jupyter-notebook-&-creating-a-dashboard — course — DeepLearning.AI course module
[103]. **Claude Code for the Rest of Us: Setup Guide & Use Cases** — https://www.whytryai.com/p/claude-code-beginner-guide — guide — Beginner-friendly setup and use cases
[104]. **Claude Code for VS Code - Visual Studio Marketplace** — https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code — doc — Official VS Code marketplace listing
[105]. **Claude Code Free Course for Beginners** — https://medium.com/data-science-in-your-pocket/claude-code-free-course-for-beginners-by-anthropic-3e9d28520f53 — course — Free beginner course
[106]. **Claude Code GitHub Actions - Claude Code Docs** — https://code.claude.com/docs/en/github-actions — doc — Official documentation on GitHub Actions integration
[107]. **Claude Code GUI - IntelliJ IDEs Plugin | Marketplace** — https://plugins.jetbrains.com/plugin/29342-claude-code-gui — doc — Alternative GUI plugin for JetBrains
[108]. **Claude Code Hooks: A Practical Guide to Workflow Automation | DataCamp** — https://www.datacamp.com/tutorial/claude-code-hooks — tutorial — DataCamp tutorial on using Claude Code hooks for automation
[109]. **Claude Code IDE integrations for JetBrains IDEs and VS Code** — https://medium.com/vibecodingpub/claude-code-ide-integrations-for-jetbrains-ides-and-vs-code-71023d27b86d — blog — Comparison of IDE integrations
[110]. **Claude Code in CI/CD: Automation with GitHub Actions and GitLab** — https://noqta.tn/en/blog/claude-code-ci-cd — blog — CI/CD automation comparison guide
[111]. **Claude Code in Enterprise Development: Security Patterns and Integration Strategies** — https://www.maisumhashim.com/blog/claude-code-enterprise-security-integration-strategies — blog — Enterprise patterns and strategies
[112]. **Claude Code MCP Server: Complete Setup Guide** — https://www.ksred.com/claude-code-as-an-mcp-server-an-interesting-capability-worth-understanding/ — Guide — KSRed's Claude Code MCP guide
[113]. **Claude Code MCP Servers for Product Managers** — https://www.prodmgmt.world/claude-code/mcp — guide — Guide to MCP servers specifically for product managers
[114]. **Claude Code Official Documentation by Anthropic | ClaudeLog** — https://claudelog.com/faqs/claude-code-docs/ — doc — Indexed and organized Claude Code documentation reference
[115]. **Claude Code on the web - Claude Code Docs** — https://code.claude.com/docs/en/claude-code-on-the-web — doc — Official web interface documentation
[116]. **Claude Code on the web | Claude** — https://claude.com/blog/claude-code-on-the-web — blog — Anthropic announcement of web interface
[117]. **Claude Code Opus 4.6 Performance Tracker** — https://marginlab.ai/trackers/claude-code/ — tracker — Real-time performance metrics
[118]. **Claude Code overview - Claude Code Docs** — https://code.claude.com/docs/en/overview — doc — Official comprehensive overview of Claude Code features and capabilities
[119]. **Claude Code Permissions: Safe vs Fast Development Modes** — https://claudefa.st/blog/guide/development/permission-management — guide — Comparison of permission modes
[120]. **Claude Code Plugin Best Practices for Large Codebases** — https://skywork.ai/blog/claude-code-plugin-best-practices-large-codebases-2025/ — guide — Large codebase best practices
[121]. **Claude Code Plus - IntelliJ IDEs Plugin | Marketplace** — https://plugins.jetbrains.com/plugin/28343-claude-code-plus — doc — Claude Code Plus plugin listing
[122]. **Claude Code power user customization: How to configure hooks** — https://claude.com/blog/how-to-configure-hooks — blog — Anthropic blog on advanced hook configuration for power users
[123]. **Claude Code Pricing Guide: Which Plan Saves You Money** — https://www.ksred.com/claude-code-pricing-guide-which-plan-actually-saves-you-money/ — guide — Analysis of pricing plans for cost optimization
[124]. **Claude Code Rules Directory: Modular Instructions That Scale** — https://claudefa.st/blog/guide/mechanics/rules-directory — blog — Claude Fast guide on modular rules
[125]. **Claude Code Security Best Practices** — https://www.backslash.security/blog/claude-code-security-best-practices — blog — Security best practices guide
[126]. **Claude code security: enterprise best practices & risk mitigation** — https://www.mintmcp.com/blog/claude-code-security — blog — Enterprise security and risk mitigation
[127]. **Claude Code Skill for Bulk Refactoring** — https://mcpmarket.com/tools/skills/code-refactor — skill — Bulk refactoring skill
[128]. **Claude Code skills: Automating FDA-required documentation** — https://thoughtbot.com/blog/claude-code-skills-automating-fda-required-documentation-for-software-as-a-medical-device — blog — Compliance documentation automation
[129]. **Claude Code Slash Commands: The Power User Guide** — https://medium.com/ai-ml-human-training-coaching/claude-code-power-user-slash-commands-the-complete-primer-e6ff143b3913 — blog — Power user guide to slash commands
[130]. **Claude Code Sub-Agent Delegation Setup.md** — https://gist.github.com/tomas-rampas/a79213bb4cf59722e45eab7aa45f155c — gist — Setup guide for subagent delegation
[131]. **Claude Code Tutorial: How to Generate, Debug and Document Code** — https://www.codecademy.com/article/claude-code-tutorial-how-to-generate-debug-and-document-code-with-ai — tutorial — Complete code generation and documentation tutorial
[132]. **Claude Code VS Code extension: A complete guide in 2025** — https://www.eesel.ai/blog/claude-code-vs-code-extension — guide — Complete 2025 guide to VS Code extension usage
[133]. **Claude Code VS Code Extension: Setup & Integration Guide** — https://claudefa.st/blog/tools/extensions/claude-code-vscode — guide — Comprehensive setup guide for VS Code extension
[134]. **Claude Code vs Cursor: Complete comparison guide in 2026** — https://northflank.com/blog/claude-code-vs-cursor-comparison — blog — Detailed feature comparison
[135]. **Claude Code vs Cursor: Deep Comparison for Dev Teams [2025]** — https://www.qodo.ai/blog/claude-code-vs-cursor/ — blog — Team-focused comparison
[136]. **Claude Code vs Cursor: Full Comparison for Developers in 2026** — https://uibakery.io/blog/claude-code-vs-cursor — blog — Developer-focused comparison
[137]. **Claude Code vs Cursor: What to Choose in 2026** — https://www.builder.io/blog/cursor-vs-claude-code — blog — Comprehensive comparison guide
[138]. **Claude Code vs Cursor: Which is Best for Your Dev Workflow** — https://www.cbtnuggets.com/blog/technology/devops/claude-code-vs-cursor/ — blog — Workflow comparison guide
[139]. **Claude code with MCP is all you need** — https://composio.dev/blog/cluade-code-with-mcp-is-all-you-need — Blog — Composio's Claude MCP article
[140]. **Claude Code: Best practices for agentic coding** — https://www.anthropic.com/engineering/claude-code-best-practices — blog — Anthropic engineering best practices for agentic coding
[141]. **Claude Code: Part 3 - Conversation Management and Context** — https://dev.to/letanure/claude-code-part-3-conversation-management-and-context-3l28 — blog — Deep dive into conversation and context management
[142]. **Claude Code: Tips and Tricks for Advanced Users** — https://cuttlesoft.com/blog/2026/02/03/claude-code-for-advanced-users/ — blog — Advanced tips and tricks
[143]. **Claude Computer Use - Hyperbrowser** — https://docs.hyperbrowser.ai/agents/claude-computer-use — Doc — Hyperbrowser's Claude Computer Use guide
[144]. **Claude Cookbook** — https://platform.claude.com/cookbook/ — guide — Official Claude cookbook with recipes and examples
[145]. **Claude fine-tuning: a complete guide to customizing Anthropic's AI model** — https://pieces.app/blog/claude-fine-tuning — guide — Complete fine-tuning customization guide
[146]. **Claude for Refactoring Legacy Code in Large Projects** — https://claude-ai.chat/guides/refactoring-legacy-code/ — guide — Legacy code refactoring guide
[147]. **Claude Image | Ultimate Guide to Claude AI Image Analysis, Vision & Generation 2026** — https://claude-image.pro/ — guide — Comprehensive 2026 guide to Claude vision capabilities
[148]. **Claude is still the best coder** — https://forum.cursor.com/t/claude-is-still-the-best-coder/93613 — forum — Cursor community discussion
[149]. **CLAUDE MD Python** — https://github.com/ruvnet/claude-flow/wiki/CLAUDE-MD-Python — wiki — Python-specific CLAUDE.md patterns
[150]. **Claude Opus 4.5 Benchmarks (Explained)** — https://www.vellum.ai/blog/claude-opus-4-5-benchmarks — blog — Analysis of benchmark results
[151]. **Claude Pricing Explained: Subscription Plans & API Costs** — https://intuitionlabs.ai/articles/claude-pricing-plans-api-costs — guide — Comprehensive pricing breakdown for Claude
[152]. **Claude Projects Guide: How to Use & Maximise AI Collaboration Tools** — https://www.instituteofaistudies.com/insights/how-to-use-claudes-projects — guide — Institute guide on using Claude projects effectively
[153]. **Claude Projects: Complete Guide + Setup Tutorial (2025)** — https://medium.com/@melissaonwuka/claude-projects-complete-guide-setup-tutorial-2025-3b9a60033b59 — guide — Complete 2025 setup tutorial for Claude projects
[154]. **Claude Prompt Engineering Best Practices (2026): Checklist and Templates** — https://promptbuilder.cc/blog/claude-prompt-engineering-best-practices-2026 — guide — Comprehensive 2026 checklist and templates for Claude prompt engineering
[155]. **Claude Prompt Engineering: We Tested 25 Popular Practices** — https://www.dreamhost.com/blog/claude-prompt-engineering/ — blog — Empirical testing of 25 prompt engineering practices with results
[156]. **Claude Security Explained: Benefits, Challenges & Compliance** — https://www.reco.ai/learn/claude-security — guide — Compliance and security overview
[157]. **Claude Skills API Implementation Guide - Error Handling** — https://smartscope.blog/en/generative-ai/claude/claude-skills-api-implementation/ — guide — Error handling in skills API
[158]. **Claude Skills Solve the Context Window Problem** — https://tylerfolkman.substack.com/p/the-complete-guide-to-claude-skills — blog — Tyler Folkman guide on Claude Skills
[159]. **Claude SWE-Bench Performance** — https://www.anthropic.com/research/swe-bench-sonnet — research — Official SWE-Bench results
[160]. **Claude Vision for Document Analysis - A Developer's Guide** — https://getstream.io/blog/anthropic-claude-visual-reasoning/ — blog — Developer guide to document analysis with Claude vision
[161]. **Claude Vision: Practical Use Cases for Images, PDFs, and Diagrams** — https://c-ai.chat/blog/claude-vision/ — blog — Practical examples of Claude vision use cases
[162]. **Claude with replit - Tips & Tricks** — https://replit.discourse.group/t/claude-with-replit/8434 — forum — Replit community tips for Claude
[163]. **Claude's extended thinking** — https://www.anthropic.com/news/visible-extended-thinking — blog — Anthropic blog on extended thinking visibility
[164]. **claude-cookbooks/misc/prompt_caching.ipynb** — https://github.com/anthropics/anthropic-cookbook/blob/main/misc/prompt_caching.ipynb — notebook — Jupyter notebook example of prompt caching
[165]. **CLAUDE.md best practices - From Basic to Adaptive - DEV Community** — https://dev.to/cleverhoods/claudemd-best-practices-from-basic-to-adaptive-9lm — blog — Community guide covering CLAUDE.md evolution from basic to advanced configurations
[166]. **CLAUDE.md: Best Practices Learned from Optimizing Claude Code** — https://arize.com/blog/claude-md-best-practices-learned-from-optimizing-claude-code-with-prompt-learning/ — blog — Advanced CLAUDE.md optimization patterns based on real-world experimentation
[167]. **Claude: enterprise security configurations and deployment controls** — https://www.datastudios.org/post/claude-enterprise-security-configurations-and-deployment-controls-explained — guide — Enterprise deployment and controls
[168]. **ClaudeLog - Claude Code Docs, Guides, Tutorials & Best Practices** — https://claudelog.com/mechanics/claude-md-supremacy/ — guide — Community resource hub with CLAUDE.md patterns and optimization strategies
[169]. **CLI Debugging Workflow - Claude Code** — https://developertoolkit.ai/en/claude-code/lessons/debugging/ — guide — Structured debugging workflows for CLI
[170]. **Client SDKs - Claude API Docs** — https://platform.claude.com/docs/en/api/client-sdks — doc — Available SDK documentation
[171]. **Code Execution with MCP** — https://www.anthropic.com/engineering/code-execution-with-mcp — Blog — Anthropic's code execution with MCP
[172]. **Code modernization | Claude** — https://claude.com/solutions/code-modernization — guide — Anthropic code modernization solutions
[173]. **Coding at the Speed of Thought: Cursor IDE and Claude Sonnet** — https://medium.com/@anandnair/coding-at-the-speed-of-thought-my-experience-with-cursor-ide-and-claude-sonnet-12e6d3bda00a — blog — Personal experience with both tools
[174]. **Common workflows - Claude Code Docs** — https://code.claude.com/docs/en/common-workflows — doc — Official documentation on common Claude Code workflows
[175]. **Configure Claude Code hooks to automate your workflow** — https://www.gend.co/blog/configure-claude-code-hooks-automation — blog — Guide to configuring hooks for workflow automation
[176]. **Configure MCP Servers on VSCode, Cursor & Claude Desktop** — https://spknowledge.com/2025/06/06/configure-mcp-servers-on-vscode-cursor-claude-desktop/ — Guide — Configuration guide for multiple MCP clients
[177]. **Configuring MCP Tools in Claude Code - The Better Way** — https://scottspence.com/posts/configuring-mcp-tools-in-claude-code — Blog — Scott Spence's MCP configuration guide
[178]. **Connect Claude Code to tools via MCP - Claude Code Docs** — https://code.claude.com/docs/en/mcp — doc — Official documentation on Model Context Protocol integration
[179]. **Connect to external tools with MCP - Claude API Docs** — https://platform.claude.com/docs/en/agent-sdk/mcp — doc — API documentation on connecting external tools via MCP
[180]. **Context Window Depletion | ClaudeLog** — https://claudelog.com/mechanics/context-window-depletion/ — guide — Guide to managing context window depletion
[181]. **Context windows - Claude API Docs** — https://platform.claude.com/docs/en/build-with-claude/context-windows — doc — Documentation on context windows and token limits
[182]. **Contextual Retrieval in AI Systems** — https://www.anthropic.com/news/contextual-retrieval — blog — Anthropic announcement on contextual retrieval improvements
[183]. **Conversational Development With Claude Code - Part 14: Installing MCP Servers** — https://dev.to/cristiansifuentes/conversational-development-with-claude-code-part-14-installing-mcp-servers-in-claude-code-3jg0 — Blog — DEV Community's Claude MCP guide
[184]. **Conversational Development With Claude Code - Part 16: Installing Claude Code in GitHub** — https://dev.to/cristiansifuentes/conversational-development-with-claude-code-part-16-installing-claude-code-in-github-with-actions-2mnf — blog — GitHub Actions setup tutorial
[185]. **Conversational Development With Claude Code - Part 9: Building Specialized Sub‑Agents** — https://dev.to/cristiansifuentes/conversational-development-with-claude-code-part-9-building-specialized-sub-agents-for-parallel-delivery-2i7f — blog — Guide to building specialized subagents
[186]. **Cooking with Claude Code: The Complete Tutorial & Guide | Sid Bharath** — https://www.siddharthbharath.com/claude-code-the-complete-guide/ — guide — Comprehensive tutorial covering Claude Code setup, commands, workflows, and best practices
[187]. **Create custom subagents - Claude Code Docs** — https://code.claude.com/docs/en/sub-agents — doc — Official documentation on creating custom subagents
[188]. **Create Reliable Unit Tests with Claude Code** — https://dev.to/alfredoperez/create-reliable-unit-tests-with-claude-code-4e8p — tutorial — Reliable test creation guide
[189]. **Cursor Agent vs. Claude Code** — https://www.haihai.ai/cursor-vs-claude-code/ — blog — Agent capability comparison
[190]. **Cursor vs Claude Code – Looking for Community Feedback** — https://forum.cursor.com/t/cursor-vs-claude-code-looking-for-community-feedback/148153 — forum — Community feedback discussion
[191]. **Cursor vs. Claude Code: in-depth comparison for dev teams** — https://decode.agency/article/cursor-vs-claude-code/ — blog — Agency perspective on comparison
[192]. **Custom Instructions for Claude Projects: A Comprehensive Guide** — https://salesforcefromscratch.co.uk/custom-instructions-for-claude-projects-a-comprehensive-guide/ — guide — Detailed guide on setting custom instructions for Claude projects
[193]. **Define success criteria and build evaluations - Claude API Docs** — https://platform.claude.com/docs/en/test-and-evaluate/develop-tests — doc — Evaluation framework documentation
[194]. **Demystifying evals for AI agents** — https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents — Blog — Anthropic's evals engineering post
[195]. **Documentation - Claude API Docs** — https://platform.claude.com/docs/en/home — doc — Complete Claude API documentation covering all models, features, and APIs
[196]. **Does Claude Code support Jupyter notebook workflows** — https://milvus.io/ai-quick-reference/does-claude-code-support-jupyter-notebook-workflows — article — Q&A on Jupyter integration
[197]. **Effective context engineering for AI agents** — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents — Blog — Anthropic's context engineering engineering post
[198]. **Embeddings - Claude API Docs** — https://platform.claude.com/docs/en/build-with-claude/embeddings — doc — Official embeddings API documentation
[199]. **Embeddings - Claude Docs** — https://docs.claude.com/en/docs/build-with-claude/embeddings — doc — Alternative embeddings documentation
[200]. **Enabling Claude Code to work more autonomously** — https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously — blog — Anthropic announcement on autonomous Claude Code features including checkpoints
[201]. **Enhancing RAG with contextual retrieval** — https://platform.claude.com/cookbook/capabilities-contextual-embeddings-guide — doc — Anthropic cookbook on contextual embeddings
[202]. **Exploring Embeddings and LLMs: Amazon Titan Embedding V2, Claude 3.5** — https://repost.aws/articles/AR3KH3VFZ0RGWmOTOM5nE8hQ/exploring-embeddings-and-llms-amazon-titan-embedding-v2-claude-3-5-and-opensearch-serverless — article — Comparison of embedding and LLM options
[203]. **Exploring the Claude Cookbooks: A Software Engineer's Guide to LLM Recipes** — https://typevar.dev/articles/anthropics/claude-cookbooks — blog — Software engineer's perspective on Claude cookbook usage
[204]. **Extend Claude with skills - Claude Code Docs** — https://code.claude.com/docs/en/skills — doc — Official documentation on how to build and extend Claude Code with custom skills using SKILL.md files and YAML frontmatter
[205]. **Extended thinking tips - Claude API Docs** — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/extended-thinking-tips — doc — Tips for effective extended thinking usage
[206]. **Extended Thinking: How to Make Claude Actually Think Before It Answers** — https://dev.to/rajeshroyal/extended-thinking-how-to-make-claude-actually-think-before-it-answers-33po — blog — Guide to leveraging extended thinking for better reasoning
[207]. **Findings from a pilot Anthropic–OpenAI alignment evaluation exercise** — https://openai.com/index/openai-anthropic-safety-evaluation/ — article — Joint safety evaluation results
[208]. **Fine-tune Anthropic's Claude 3 Haiku in Amazon Bedrock** — https://aws.amazon.com/blogs/machine-learning/fine-tune-anthropics-claude-3-haiku-in-amazon-bedrock-to-boost-model-accuracy-and-quality/ — blog — Guide to boosting accuracy through fine-tuning
[209]. **Fine-tune Claude 3 Haiku in Amazon Bedrock** — https://www.anthropic.com/news/fine-tune-claude-3-haiku — blog — Anthropic announcement on fine-tuning
[210]. **Fine-Tuning Claude - A Practical Guide** — https://medium.com/@heyamit10/fine-tuning-claude-a-practical-guide-477ac6e8dcf2 — guide — Practical fine-tuning guide
[211]. **Fine-tuning for Anthropic's Claude 3 Haiku model in Amazon Bedrock** — https://aws.amazon.com/blogs/aws/fine-tuning-for-anthropics-claude-3-haiku-model-in-amazon-bedrock-is-now-generally-available/ — blog — AWS announcement of fine-tuning availability
[212]. **Fix software bugs faster with Claude** — https://claude.com/blog/fix-software-bugs-faster-with-claude — blog — Anthropic blog on bug fixing strategies
[213]. **Function Calling & Tool Use with Claude 3** — https://blog.mlq.ai/claude-function-calling-tools/ — blog — Overview of Claude function calling and tool use patterns
[214]. **Get structured output from agents - Claude API Docs** — https://platform.claude.com/docs/en/agent-sdk/structured-outputs — doc — Agent SDK structured outputs
[215]. **Getting Started with Claude Code for Data Scientists** — https://www.dataquest.io/blog/getting-started-with-claude-code-for-data-scientists/ — guide — Data science getting started guide
[216]. **Getting started with Model Context Protocol (MCP) on Claude for Desktop** — https://support.anthropic.com/en/articles/10949351-getting-started-with-model-context-protocol-mcp-on-claude-for-desktop — Doc — Official Claude Desktop MCP setup guide
[217]. **GitHub - 1rgs/jsonformer-claude** — https://github.com/1rgs/jsonformer-claude — repo — JSON formatter for Claude
[218]. **GitHub - aminanvary/Custom-Instructions** — https://github.com/aminanvary/Custom-Instructions — repo — Collection of custom instructions for Claude and related AI tools
[219]. **GitHub - anthropics/claude-agent-sdk-demos** — https://github.com/anthropics/claude-agent-sdk-demos — repo — Demonstrations of Agent SDK capabilities
[220]. **GitHub - anthropics/claude-agent-sdk-python** — https://github.com/anthropics/claude-agent-sdk-python — repo — Official Python Agent SDK repository
[221]. **GitHub - anthropics/claude-agent-sdk-typescript** — https://github.com/anthropics/claude-agent-sdk-typescript — repo — TypeScript Agent SDK
[222]. **GitHub - anthropics/claude-code** — https://github.com/anthropics/claude-code — repo — Official Claude Code repository with source code and examples
[223]. **GitHub - anthropics/claude-code-action** — https://github.com/anthropics/claude-code-action — repo — Official Claude Code GitHub Action for automation
[224]. **GitHub - anthropics/courses** — https://github.com/anthropics/courses — repo — Educational courses repository
[225]. **GitHub - anthropics/prompt-eng-interactive-tutorial** — https://github.com/anthropics/prompt-eng-interactive-tutorial — repo — Interactive tutorial from Anthropic on prompt engineering
[226]. **GitHub - anthropics/skills: Public repository for Agent Skills** — https://github.com/anthropics/skills — repo — Official Anthropic repository containing 75+ example skills demonstrating different capabilities
[227]. **GitHub - auchenberg/claude-code-mcp** — https://github.com/auchenberg/claude-code-mcp — Repo — Claude Code MCP implementation
[228]. **GitHub - BexTuychiev/firecrawl-claude-code-skill** — https://github.com/BexTuychiev/firecrawl-claude-code-skill — repo — Firecrawl skill implementation
[229]. **GitHub - browserbase/agent-browse: Claude Agent SDK with web browsing** — https://github.com/browserbase/agent-browse — Repo — Browserbase agent browse repository
[230]. **GitHub - carterlasalle/aipromptxml** — https://github.com/carterlasalle/aipromptxml — repo — XML helper tool for Claude prompts
[231]. **GitHub - catlog22/Claude-Code-Workflow** — https://github.com/catlog22/Claude-Code-Workflow — repo — Multi-agent cadence framework with JSON-driven orchestration
[232]. **GitHub - ChrisWiles/claude-code-showcase** — https://github.com/ChrisWiles/claude-code-showcase — repo — Comprehensive project showcase with hooks, skills, agents, and GitHub Actions
[233]. **GitHub - Cranot/claude-code-guide** — https://github.com/Cranot/claude-code-guide — repo — Auto-updated complete Claude Code CLI guide
[234]. **GitHub - darraghh1/my-claude-setup** — https://github.com/darraghh1/my-claude-setup — repo — Complete Claude Code configuration framework with hooks, agents, and MCP servers
[235]. **GitHub - davila7/claude-code-templates** — https://github.com/davila7/claude-code-templates — repo — CLI tool for configuring and monitoring Claude Code
[236]. **GitHub - disler/claude-code-hooks-mastery** — https://github.com/disler/claude-code-hooks-mastery — repo — Repository demonstrating hook mastery with examples
[237]. **GitHub - firecrawl/firecrawl-claude-plugin** — https://github.com/firecrawl/firecrawl-claude-plugin — repo — Firecrawl plugin for Claude Code
[238]. **GitHub - hesreallyhim/awesome-claude-code** — https://github.com/hesreallyhim/awesome-claude-code — repo — Curated list of 75+ Claude Code skills, hooks, commands, and plugins
[239]. **GitHub - instantlyeasy/claude-code-sdk-ts** — https://github.com/instantlyeasy/claude-code-sdk-ts — repo — Fluent TypeScript SDK wrapper
[240]. **GitHub - ItMeDiaTech/rag-cli** — https://github.com/ItMeDiaTech/rag-cli — repo — Local RAG plugin for Claude Code with Chroma vector embeddings
[241]. **GitHub - karanb192/claude-code-hooks** — https://github.com/karanb192/claude-code-hooks — repo — Growing collection of useful Claude Code hooks for reuse
[242]. **GitHub - lst97/claude-code-sub-agents** — https://github.com/lst97/claude-code-sub-agents — repo — Collection of specialized subagents for full-stack development
[243]. **GitHub - luongnv89/claude-howto** — https://github.com/luongnv89/claude-howto — repo — Visual, example-driven guide to Claude Code with copy-paste templates
[244]. **GitHub - majkonautic/NOVA_claude-code-mcp-guide** — https://github.com/majkonautic/NOVA_claude-code-mcp-guide — repo — Complete MCP integration guide for Claude Code with Docker templates
[245]. **GitHub - OneRedOak/claude-code-workflows** — https://github.com/OneRedOak/claude-code-workflows — repo — Production workflows from AI-native startup
[246]. **GitHub - p32929/ccheckpoints** — https://github.com/p32929/ccheckpoints — repo — Community checkpoint system for Claude Code
[247]. **GitHub - Pimzino/claude-code-spec-workflow** — https://github.com/Pimzino/claude-code-spec-workflow — repo — Spec-driven development workflow
[248]. **GitHub - PleasePrompto/notebooklm-skill** — https://github.com/PleasePrompto/notebooklm-skill — repo — Google NotebookLM skill for Claude Code
[249]. **GitHub - ruvnet/claude-flow** — https://github.com/ruvnet/claude-flow — repo — Multi-agent swarm platform for Claude with enterprise architecture
[250]. **GitHub - SawyerHood/dev-browser: A Claude Skill** — https://github.com/SawyerHood/dev-browser — Repo — Dev Browser skill repository
[251]. **GitHub - shanraisshan/claude-code-best-practice** — https://github.com/shanraisshan/claude-code-best-practice — repo — Community repository with Claude Code best practice examples and patterns
[252]. **GitHub - shinpr/claude-code-workflows** — https://github.com/shinpr/claude-code-workflows — repo — Production-ready development workflows powered by specialized AI agents
[253]. **GitHub - siteboon/claudecodeui** — https://github.com/siteboon/claudecodeui — repo — Mobile and web UI for Claude Code
[254]. **GitHub - steipete/claude-code-mcp** — https://github.com/steipete/claude-code-mcp — Repo — Claude Code MCP server repository
[255]. **GitHub - sugyan/claude-code-webui** — https://github.com/sugyan/claude-code-webui — repo — Web-based interface for Claude CLI
[256]. **GitHub - ThamJiaHe/claude-prompt-engineering-guide** — https://github.com/ThamJiaHe/claude-prompt-engineering-guide — repo — Comprehensive guide integrating MCP, skills, and best practices
[257]. **GitHub - touwaeriol/claude-code-plus** — https://github.com/touwaeriol/claude-code-plus — repo — GUI plugin for Claude Code in JetBrains
[258]. **GitHub - vultuk/claude-code-web** — https://github.com/vultuk/claude-code-web — repo — Web interface with multi-session support
[259]. **GitHub - wesammustafa/Claude-Code-Everything-You-Need-to-Know** — https://github.com/wesammustafa/Claude-Code-Everything-You-Need-to-Know — repo — All-in-one master guide to Claude Code mastery
[260]. **GitHub - wshobson/agents** — https://github.com/wshobson/agents — repo — Multi-agent orchestration framework for Claude Code
[261]. **GitHub - ykdojo/claude-code-tips** — https://github.com/ykdojo/claude-code-tips — repo — 45 tips collection with examples
[262]. **GitHub - zebbern/claude-code-guide** — https://github.com/zebbern/claude-code-guide — repo — Setup and command guide for Claude Code
[263]. **GitHub - zilliztech/claude-context** — https://github.com/zilliztech/claude-context — repo — Code search MCP for Claude Code enabling full codebase context
[264]. **Handling stop reasons - Claude Docs** — https://docs.claude.com/en/api/handling-stop-reasons — doc — Documentation on handling stop reasons
[265]. **Hooks reference - Claude Code Docs** — https://code.claude.com/docs/en/hooks — doc — Official documentation on Claude Code hooks and their configuration
[266]. **How Anthropic teams use Claude Code** — https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf — doc — Anthropic internal case study on how their teams use Claude Code
[267]. **How Claude Code Got Better by Protecting More Context** — https://hyperdev.matsuoka.com/p/how-claude-code-got-better-by-protecting — blog — Blog on context protection improvements
[268]. **How Claude Code works - Claude Code Docs** — https://code.claude.com/docs/en/how-claude-code-works — doc — Official explanation of Claude Code architecture and operations
[269]. **How do I use Claude Code for data analysis** — https://milvus.io/ai-quick-reference/how-do-i-use-claude-code-for-data-analysis — article — Q&A on data analysis
[270]. **How I use Claude Code (+ my best tips)** — https://www.builder.io/blog/claude-code — blog — Builder.io founder's tips on Claude Code including hook usage
[271]. **How I Use Every Claude Code Feature** — https://blog.sshh.io/p/how-i-use-every-claude-code-feature — blog — Feature-by-feature walkthrough
[272]. **How I'm Using (New) VS Code Claude Code 2.0 Extension to Code 10x Faster** — https://medium.com/@joe.njenga/how-im-using-new-vs-code-claude-code-2-0-extension-to-code-10x-faster-1c78d1ade62c — blog — Personal experience with VS Code extension version 2.0
[273]. **How Prompt Caching Actually Works in Claude Code** — https://www.claudecodecamp.com/p/how-prompt-caching-actually-works-in-claude-code — article — Technical explanation of caching
[274]. **How Sub-Agents Work in Claude Code: A Complete Guide** — https://medium.com/@kinjal01radadiya/how-sub-agents-work-in-claude-code-a-complete-guide-bafc66bbaf70 — blog — Complete subagent workflow guide
[275]. **How to Build a RAG System With Anthropic Claude on AWS** — https://www.tigerdata.com/blog/how-to-build-rag-system-with-claude-on-aws — guide — AWS guide to building RAG with Claude
[276]. **How to build Claude AI Agents | Architecture, Deployment Guide** — https://dextralabs.com/blog/claude-ai-agents-architecture-deployment-guide/ — guide — Architecture and deployment guide for Claude agents
[277]. **How to Build Claude Skills: Lesson Plan Generator Tutorial | Codecademy** — https://www.codecademy.com/article/how-to-build-claude-skills — tutorial — Interactive tutorial teaching skill development with a practical lesson plan generator project
[278]. **How to Create a Claude Code Skill: A Web Scraping Example with Firecrawl** — https://www.firecrawl.dev/blog/claude-code-skill — tutorial — Firecrawl skill tutorial
[279]. **How to Create Agents with Claude Agents SDK** — https://blog.getbind.co/2025/10/03/how-to-create-agents-with-claude-agents-sdk/ — guide — Agent creation guide
[280]. **How to create custom Skills | Claude Help Center** — https://support.claude.com/en/articles/12512198-how-to-create-custom-skills — doc — Step-by-step guide for creating custom skills in Claude with examples and best practices
[281]. **How to create Skills for Claude: steps and examples | Claude** — https://claude.com/blog/how-to-create-skills-key-steps-limitations-and-examples — blog — Anthropic blog post explaining skill creation steps, limitations, and practical examples
[282]. **How to Do Unit Testing on Claude Code** — https://usagebar.com/blog/how-to-do-unit-testing-on-claude-code — guide — Unit testing guide
[283]. **How to Fine-Tune Claude 3.7 Sonnet for Vision AI** — https://blog.roboflow.com/fine-tune-claude-3-7-sonnet/ — guide — Vision fine-tuning guide
[284]. **How to Generate Documentation & Unit Tests with Claude Code Plugin** — https://skywork.ai/blog/how-to-generate-documentation-unit-tests-claude-code-plugin/ — guide — Documentation and testing automation
[285]. **How to get consistent structured output from Claude** — https://dev.to/heuperman/how-to-get-consistent-structured-output-from-claude-20o5 — blog — Consistency patterns
[286]. **How to implement tool use - Claude API Docs** — https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use — doc — Step-by-step implementation guide for tool use with Claude
[287]. **How to Install Claude Code: Terminal, IDE, Web & Desktop Setup** — https://www.bannerbear.com/blog/how-to-install-claude-code-terminal-ide-web-desktop-setup/ — guide — Installation guide for all Claude Code interfaces
[288]. **How to Set Up a Claude Project that Answers Questions about Your Class** — https://learning.northeastern.edu/ai-student-guides-claude-project-to-answer-questions-about-class/ — guide — Practical guide to setting up Claude projects for educational contexts
[289]. **How to Set Up Claude Code CLI (Beginner Guide)** — https://shellypalmer.com/how-to-set-up-claude-code-cli-beginner-guide/ — guide — Beginner guide to CLI setup
[290]. **How to Turn Claude Code Into Your Personal AI Assistant** — https://www.theneuron.ai/explainer-articles/how-to-turn-claude-code-into-your-personal-ai-assistant — blog — The Neuron guide on Claude Code customization
[291]. **How to Use Checkpoints in Claude Code** — https://claudelog.com/faqs/how-to-use-checkpoints-in-claude-code/ — guide — Guide to using checkpoints
[292]. **How to use Claude 3 AI Custom Instructions feature** — https://www.geeky-gadgets.com/claude-3-custom-instructions/ — guide — Guide to using custom instructions in Claude 3
[293]. **How to Use Claude Code for Refactoring & Clean Code** — https://www.arsturn.com/blog/how-to-use-claude-code-to-refactor-and-clean-up-your-codebase — guide — Code cleanup guide
[294]. **How to use Claude Code on the Web** — https://apidog.com/blog/claude-code-web/ — guide — Guide to web interface usage
[295]. **How to Use Claude Code Plugin for Safe Refactoring & Migration** — https://skywork.ai/blog/how-to-use-claude-code-plugin-for-refactoring-migration-guide/ — guide — Safe refactoring practices
[296]. **How to Use Claude Code Safely: A Non-Technical Guide** — https://www.producttalk.org/how-to-use-claude-code-safely/ — guide — Non-technical safety guide
[297]. **How to Use Claude Code: A Guide to Slash Commands, Agents, Skills, and Plug-ins** — https://www.producttalk.org/how-to-use-claude-code-features/ — guide — Comprehensive guide to Claude Code features
[298]. **How to Use Model Context Protocol (MCP) with Claude** — https://www.codecademy.com/article/how-to-use-model-context-protocol-mcp-with-claude-step-by-step-guide-with-examples — tutorial — Codecademy step-by-step guide to MCP integration with Claude
[299]. **How to Use Prompt Caching in Claude API: Complete 2026 Guide** — https://www.aifreeapi.com/en/posts/claude-api-prompt-caching-guide — guide — Comprehensive 2026 prompt caching guide
[300]. **How to Write a Good CLAUDE.md File** — https://www.builder.io/blog/claude-md-guide — blog — Builder.io guide on writing effective CLAUDE.md files with practical examples
[301]. **how-to-use-claude-code-for-debugging | ClaudeLog** — https://claudelog.com/faqs/how-to-use-claude-code-for-debugging/ — guide — Guide to using Claude Code for debugging
[302]. **I Built a Web App Using Claude Code** — https://medium.com/towards-data-engineering/i-built-a-web-app-using-claude-code-heres-exactly-how-200f0b39e5e0 — blog — Personal experience building web app
[303]. **I mastered the Claude Code workflow | by Ashley Ha | Medium** — https://medium.com/@ashleyha/i-mastered-the-claude-code-workflow-145d25e502cf — blog — Personal journey mastering Claude Code workflows
[304]. **I've organised the Claude Code commands, including some hidden ones** — https://dev.to/akari_iku/ive-organised-the-claude-code-commands-including-some-hidden-ones-op0 — blog — Guide to documented and hidden Claude Code commands
[305]. **Increase output consistency - Claude API Docs** — https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/increase-consistency — doc — Output consistency guide
[306]. **Inside Claude Code Skills: Structure, prompts, invocation | Mikhail Shilkov** — https://mikhail.io/2025/10/claude-code-skills/ — blog — Deep dive into Claude Code skill architecture, prompts, and invocation patterns
[307]. **Integrating Claude Code Plugin with VSCode & JetBrains** — https://skywork.ai/blog/integrating-claude-code-plugin-vscode-jetbrains-ultimate-guide/ — guide — Guide to integrating both VS Code and JetBrains
[308]. **Integrating Claude Code with GitHub Actions** — https://stevekinney.com/courses/ai-development/integrating-with-github-actions — course — Course on GitHub Actions integration
[309]. **Introducing advanced tool use on the Claude Developer Platform** — https://www.anthropic.com/engineering/advanced-tool-use — blog — Anthropic engineering blog on advanced tool use capabilities
[310]. **Introducing Claude Code Documentation Standards** — https://dev.to/nasrulhazim/introducing-claude-code-documentation-standards-automated-documentation-with-built-in-linting-51c — blog — Documentation standards framework
[311]. **Introducing Claude Opus 4.5** — https://www.anthropic.com/news/claude-opus-4-5 — blog — Announcement of Claude Opus 4.5 capabilities
[312]. **Introducing the Message Batches API | Claude** — https://claude.com/blog/message-batches-api — blog — Anthropic announcement of batch processing API
[313]. **Introducing the Model Context Protocol** — https://www.anthropic.com/news/model-context-protocol — blog — Anthropic announcement introducing the Model Context Protocol
[314]. **Introduction to Model Context Protocol - Anthropic Courses** — https://anthropic.skilljar.com/introduction-to-model-context-protocol — Guide — Official Anthropic course on MCP
[315]. **JetBrains IDEs - Claude Code Docs** — https://code.claude.com/docs/en/jetbrains — doc — Official JetBrains IDE integration documentation
[316]. **Learning from Anthropic about building effective agents** — https://maa1.medium.com/learning-from-anthropic-about-building-effective-agents-2a7469941428 — Blog — Medium's Anthropic agents article
[317]. **LLM API Pricing Comparison (2025): OpenAI, Gemini, Claude** — https://intuitionlabs.ai/articles/llm-api-pricing-comparison-2025 — comparison — Comparative pricing analysis across LLM providers
[318]. **Managing context on the Claude Developer Platform** — https://claude.com/blog/context-management — blog — Anthropic blog on context management strategies
[319]. **Managing Multiple Claude Code Sessions Without Worktrees** — https://blog.gitbutler.com/parallel-claude-code — blog — Guide to managing parallel Claude Code sessions
[320]. **Mastering Claude's Context Window: A 2025 Deep Dive** — https://sparkco.ai/blog/mastering-claudes-context-window-a-2025-deep-dive — guide — Deep dive into context window optimization for 2025
[321]. **Mastering Context Management in Claude Code CLI** — https://lalatenduswain.medium.com/mastering-context-management-in-claude-code-cli-your-guide-to-efficient-ai-assisted-coding-83753129b28e — blog — Advanced context management strategies
[322]. **Mastering Prompt Engineering for Claude** — https://www.walturn.com/insights/mastering-prompt-engineering-for-claude — guide — In-depth guide on advanced prompt engineering for Claude
[323]. **MCP Clients Explained: VS Code, Claude & Cursor Comparison** — https://www.arsturn.com/blog/mcp-clients-explained-a-deep-dive-into-vs-code-claude-and-cursor — Blog — In-depth MCP client comparison
[324]. **MCP Integrations - VSCode, Cursor, Claude Desktop, Zed & More** — https://mcpez.com/integrations — Doc — MCPez integrations overview
[325]. **Mitigating the risk of prompt injections in browser use** — https://www.anthropic.com/research/prompt-injection-defenses — Research — Anthropic's prompt injection defenses research
[326]. **Models overview - Claude API Docs** — https://platform.claude.com/docs/en/about-claude/models/overview — doc — Overview of Claude models and specifications
[327]. **Modernization with Claude Code: from COBOL to cloud migrations** — https://codingscape.com/blog/modernization-with-claude-code-from-cobol-to-cloud-migrations — blog — Legacy to cloud migration guide
[328]. **More Understanding of XML Tags In Claude Prompt** — https://medium.com/@ywian/more-understanding-of-xml-tags-in-claude-prompt-2dc162b55ad9 — blog — Deep dive into XML tag functionality
[329]. **Multishot prompting Anthropic** — https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/multishot-prompting — doc — Anthropic multishot guide
[330]. **My 7 essential Claude Code best practices for production-ready AI in 2025** — https://www.eesel.ai/blog/claude-code-best-practices — blog — Seven essential practices for production Claude Code usage
[331]. **My Claude Code Setup** — https://psantanna.com/claude-code-my-workflow/workflow-guide.html — guide — Personal workflow guide showing complete Claude Code setup
[332]. **My Data Extraction Stack with Claude Code** — https://medium.com/@yaron.been/my-data-extraction-stack-with-claude-code-the-missing-feature-32b22d62f6a2 — blog — Production data extraction stack
[333]. **Navigating Claude Code API Errors: Common Issues and Solutions** — https://www.oreateai.com/blog/navigating-claude-code-api-errors-common-issues-and-solutions/4d90e3c488530e129c8256664acb105e — guide — Error troubleshooting guide
[334]. **Part 4 - Using Cursor and Claude to Create Automated Tests with Playwright** — https://dev.to/chiefremote/part-4-using-cursor-and-claude-to-create-automated-tests-with-playwright-2p7j — tutorial — Playwright test automation
[335]. **Performance Benchmarking · ruvnet/claude-flow Wiki** — https://github.com/ruvnet/claude-flow/wiki/Performance-Benchmarking — wiki — Performance benchmark patterns
[336]. **Pricing - Claude API Docs** — https://platform.claude.com/docs/en/about-claude/pricing — doc — Official Claude API pricing documentation
[337]. **Programmatic tool calling - Claude API Docs** — https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling — doc — Guide to programmatic tool calling within Claude Code
[338]. **Project Structure for AI | Cursor & Claude Code** — https://developertoolkit.ai/en/shared-workflows/context-management/file-organization/ — guide — Developer Toolkit guide on project structure for AI
[339]. **Prompt caching - Claude API Docs** — https://platform.claude.com/docs/en/build-with-claude/prompt-caching — doc — Official prompt caching documentation
[340]. **Prompt caching with Claude** — https://claude.com/blog/prompt-caching — blog — Anthropic blog on prompt caching benefits
[341]. **Prompt engineering best practices | Claude** — https://claude.com/blog/best-practices-for-prompt-engineering — blog — Anthropic blog post on effective prompt engineering techniques
[342]. **Prompt engineering overview - Claude API Docs** — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview — doc — Overview of prompt engineering concepts and techniques for Claude
[343]. **Prompt engineering overview Anthropic** — https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview — doc — Anthropic prompt overview
[344]. **Prompt engineering techniques and best practices: Learn by doing with Anthropic's Claude 3 on Amazon Bedrock** — https://aws.amazon.com/blogs/machine-learning/prompt-engineering-techniques-and-best-practices-learn-by-doing-with-anthropics-claude-3-on-amazon-bedrock/ — blog — AWS guide on Claude prompt engineering techniques
[345]. **Prompting best practices - Claude API Docs** — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices — doc — Official Claude API prompting best practices guide
[346]. **python-testing skill** — https://playbooks.com/skills/laurigates/claude-plugins/python-testing — skill — Python testing skill for Claude
[347]. **Quickstart - Claude API Docs** — https://platform.claude.com/docs/en/agent-sdk/quickstart — doc — Quick start guide for Agent SDK
[348]. **Quickstart - Claude Code Docs** — https://code.claude.com/docs/en/quickstart — doc — Official quickstart guide
[349]. **Reduce Claude Code Cron Automation Failures by 90%** — https://smartscope.blog/en/generative-ai/claude/claude-code-cron-error-handling-retry-deep-dive/ — guide — Error handling and retry strategies
[350]. **Retrieval augmented generation (RAG) for projects** — https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects — doc — Official RAG documentation for Claude projects
[351]. **Retrieval augmented generation - Claude Console** — https://platform.claude.com/cookbook/capabilities-retrieval-augmented-generation-guide — guide — RAG cookbook and implementation guide
[352]. **Revolutionizing AI Development: How Claude Code's Sub Agents Transform Task Management** — https://htdocs.dev/posts/revolutionizing-ai-development-how-claude-codes-sub-agents-transform-task-management/ — blog — Analysis of subagent impact on task management
[353]. **Security - Claude Code Docs** — https://code.claude.com/docs/en/security — doc — Official Claude Code security documentation
[354]. **Security Lessons from Claude Code's First Year** — https://www.harmonic.security/resources/security-lessons-from-claude-codes-first-year — report — Security lessons learned from deployment
[355]. **Semantic Code Search in Claude Code** — https://medium.com/@jldavern/semantic-code-search-in-claude-code-the-missing-feature-32b22d62f6a2 — blog — Semantic search in Claude Code
[356]. **Shipyard | Claude Code CLI Cheatsheet** — https://shipyard.build/blog/claude-code-cheat-sheet/ — guide — Quick reference for CLI commands and cheatsheet
[357]. **Skill authoring best practices - Claude API Docs** — https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices — doc — Official best practices for writing high-quality skills with clear descriptions and structured instructions
[358]. **Skills for enterprise - Claude API Docs** — https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise — doc — Enterprise skills documentation
[359]. **skills/skills/skill-creator/SKILL.md at main · anthropics/skills** — https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md — repo — Anthropic's official skill creator template showing the structure for building production skills
[360]. **Slash commands - Claude Code Docs** — https://code.claude.com/docs/en/slash-commands — doc — Official documentation on slash commands
[361]. **Slash Commands in the SDK - Claude API Docs** — https://platform.claude.com/docs/en/agent-sdk/slash-commands — doc — API documentation on slash command implementation
[362]. **Stream responses in real-time - Claude API Docs** — https://platform.claude.com/docs/en/agent-sdk/streaming-output — doc — Agent SDK streaming guide
[363]. **Streaming Messages - Claude API Docs** — https://platform.claude.com/docs/en/build-with-claude/streaming — doc — Streaming API documentation
[364]. **Streamlined CI/CD Pipelines Using Claude Code & GitHub Actions** — https://medium.com/@itsmybestview/streamlined-ci-cd-pipelines-using-claude-code-github-actions-74be17e51499 — blog — CI/CD automation with Claude Code
[365]. **Structured outputs - Claude API Docs** — https://platform.claude.com/docs/en/build-with-claude/structured-outputs — doc — Structured outputs documentation
[366]. **Sub-Agents Guide - claude v0.5.3** — https://hexdocs.pm/claude/guide-subagents.html — doc — Hex documentation on subagents
[367]. **Subagents in the SDK - Claude API Docs** — https://platform.claude.com/docs/en/agent-sdk/subagents — doc — API documentation for subagents
[368]. **Test-Driven Development with Claude Code** — https://stevekinney.com/courses/ai-development/test-driven-development-with-claude — course — TDD course with Claude Code
[369]. **The \'think\' tool: Enabling Claude to stop and think** — https://www.anthropic.com/engineering/claude-think-tool — blog — Anthropic engineering blog on the think tool
[370]. **The Art of Fine-Tuning: A Guide for ChatGPT & Claude** — https://www.walturn.com/insights/the-art-of-fine-tuning-a-guide-for-chatgpt-claude — guide — Comparative fine-tuning guide
[371]. **The Claude 3 Model Family: Opus, Sonnet, Haiku** — https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf — paper — Model card documentation
[372]. **The Claude Code Playbook: 5 Tips Worth $1000s in Productivity** — https://blog.whiteprompt.com/the-claude-code-playbook-5-tips-worth-1000s-in-productivity-22489d67dd89 — blog — High-value productivity tips
[373]. **The Complete Guide to Building Agents with the Claude Agent SDK** — https://nader.substack.com/p/the-complete-guide-to-building-agents — Blog — Nader's comprehensive Claude Agent SDK guide
[374]. **The Complete Guide to Building Skills for Claude** — https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf — guide — Comprehensive Anthropic resource detailing skill architecture, templates, and real-world examples
[375]. **The Ultimate Claude Code Guide: Every Hidden Trick, Hack, and Power Feature** — https://dev.to/holasoymalva/the-ultimate-claude-code-guide-every-hidden-trick-hack-and-power-feature-you-need-to-know-2l45 — guide — Comprehensive hidden features guide
[376]. **The Ultimate Guide to Building Your Agentic AI Workflow With Claude Cowork** — https://aimaker.substack.com/p/claude-cowork-review-agentic-ai-guide — guide — Comprehensive guide to building agentic workflows
[377]. **Token counting - Claude API Docs** — https://platform.claude.com/docs/en/build-with-claude/token-counting — doc — Token counting API documentation
[378]. **Tool calling with Claude - Exa** — https://docs.exa.ai/reference/tool-calling-with-claude — doc — Exa documentation on implementing tool calling with Claude
[379]. **Tool use - Amazon Bedrock** — https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-anthropic-claude-messages-tool-use.html — doc — AWS Bedrock documentation on Claude tool use
[380]. **Tool use with Claude - Claude API Docs** — https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview — doc — Official documentation on Claude tool use and function calling
[381]. **Tool use with Claude - Claude API Docs** — https://docs.anthropic.com/en/docs/build-with-claude/tool-use — Doc — Official Claude tool use documentation
[382]. **TypeScript SDK V2 interface (preview) - Claude API Docs** — https://platform.claude.com/docs/en/agent-sdk/typescript-v2-preview — doc — V2 preview documentation
[383]. **Understanding Claude Code Permissions and Security Settings** — https://www.petefreitag.com/blog/claude-code-permissions/ — blog — Detailed permissions explanation
[384]. **Understanding Claude's Personalization Features | Claude Help Center** — https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features — doc — Guide to Claude's personalization and custom instructions
[385]. **Understanding usage and length limits | Claude Help Center** — https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits — doc — Support documentation on usage and token limits
[386]. **Unlocking Efficiency: A Practical Guide to Claude Prompt Caching** — https://medium.com/@mcraddock/unlocking-efficiency-a-practical-guide-to-claude-prompt-caching-3185805c0eef — blog — Practical prompt caching guide
[387]. **Use Claude Code in VS Code - Claude Code Docs** — https://code.claude.com/docs/en/vs-code — doc — Official VS Code extension documentation
[388]. **Use Claude for Web Scraping: Tutorial for 2026** — https://decodo.com/blog/claude-web-scraping — tutorial — 2026 web scraping tutorial
[389]. **Use function calling with Anthropic to enhance Claude on Google Cloud** — https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-claude-3-tool-use — doc — Google Cloud guide on Claude tool use via Vertex AI
[390]. **Use prompt templates and variables - Claude API Docs** — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompt-templates-and-variables — doc — Guide to prompt templates and variables
[391]. **Use Skills in Claude | Claude Help Center** — https://support.claude.com/en/articles/12512180-use-skills-in-claude — doc — Official guide on discovering, using, and managing skills within Claude
[392]. **Use XML tags to structure your prompts - Claude API Docs** — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/use-xml-tags — doc — Official documentation on XML tag usage
[393]. **Using Agent Skills with the API - Claude API Docs** — https://platform.claude.com/docs/en/build-with-claude/skills-guide — doc — Guide to using agent skills with the Claude API
[394]. **Using Anthropic's developer resources and setup** — https://www.linkedin.com/learning/ai-powered-development-with-the-anthropic-api/using-anthropic-s-developer-resources-and-setup — course — LinkedIn Learning course on Anthropic resources
[395]. **Using Anthropic's Message Batches API with Temporal** — https://stevekinney.com/writing/anthropic-batch-api-with-temporal — blog — Integration guide for batch API with Temporal workflows
[396]. **Using Claude Code and Aider to Refactor Large Projects** — https://codenotary.com/blog/using-claude-code-and-aider-to-refactor-large-projects-enhancing-maintainability-and-scalability — blog — Refactoring large codebases
[397]. **Using Claude Code to Modernize Legacy Codebases** — https://www.rakeshgohel.com/blog/using-claude-code-to-modernize-legacy-codebases — blog — Modernization strategies
[398]. **Using CLAUDE.MD files: Customizing Claude Code for your codebase | Claude** — https://claude.com/blog/using-claude-md-files — blog — Anthropic blog explaining CLAUDE.md customization and context management
[399]. **Using extended thinking | Claude Help Center** — https://support.claude.com/en/articles/10574485-using-extended-thinking — doc — Guide to using extended thinking feature
[400]. **Using FireCrawl MCP server with Claude Code for web scraping** — https://composio.dev/blog/using-firecrawl-mcp-server-with-claude-code-for-web-scraping — blog — FireCrawl integration for scraping
[401]. **Using the GitHub Integration | Claude Help Center** — https://support.claude.com/en/articles/10167454-using-the-github-integration — doc — Support documentation on GitHub integration
[402]. **Video Tutorials & Guides - Lovable** — https://lovable.dev/videos/anthropic — video — Lovable video tutorials on Anthropic
[403]. **Video Tutorials | Anthropic Help Center** — https://support.claude.com/en/collections/10548294-video-tutorials — doc — Video tutorial collection
[404]. **Vision - Claude API Docs** — https://platform.claude.com/docs/en/build-with-claude/vision — doc — Official documentation on Claude's vision capabilities
[405]. **Vision - Claude Docs** — https://docs.claude.com/en/docs/build-with-claude/vision — doc — Vision capabilities documentation
[406]. **We Got Claude to Fine-Tune an Open Source LLM** — https://huggingface.co/blog/hf-skills-training — blog — HuggingFace article on fine-tuning
[407]. **Web Scraping with Claude AI: Python Guide** — https://oxylabs.io/blog/claude-web-scraping — guide — Python scraping guide
[408]. **Web Scraping With Claude in 2026: Automating Data Extraction** — https://medium.com/@datajournal/web-scraping-with-claude-in-2025-automating-data-extraction-effortlessly-15f0a6c8020c — guide — Automated data extraction guide
[409]. **Web Scraping with Claude: AI-Powered Parsing in Python** — https://brightdata.com/blog/web-data/web-scraping-with-claude — blog — Python scraping with Claude
[410]. **What are projects? | Claude Help Center** — https://support.claude.com/en/articles/9517075-what-are-projects — doc — Help center documentation on Claude projects
[411]. **What is --output-format in Claude Code** — https://claudelog.com/faqs/what-is-output-format-in-claude-code/ — guide — Output format options guide
[412]. **What is Sub-Agent Delegation in Claude Code** — https://claudelog.com/faqs/what-is-sub-agent-delegation-in-claude-code/ — guide — Explanation of subagent delegation
[413]. **Writing a good CLAUDE.md | HumanLayer Blog** — https://www.humanlayer.dev/blog/writing-a-good-claude-md — blog — Best practices for writing effective CLAUDE.md files to guide Claude Code behavior
[414]. **Writing effective tools for AI agents** — https://www.anthropic.com/engineering/writing-tools-for-agents — Blog — Anthropic's tool design engineering post
[415]. **Your complete guide to slash commands Claude Code** — https://www.eesel.ai/blog/slash-commands-claude-code — guide — Complete slash command reference

### A10. AI Evaluation & Testing

[1]. **30 LLM evaluation benchmarks and how they work** — https://www.evidentlyai.com/llm-guide/llm-benchmarks — guide — Evidently AI comprehensive guide to LLM benchmarks
[2]. **A Complete Guide to LLM Evaluation and Benchmarking** — https://www.turing.com/resources/understanding-llm-evaluation-and-benchmarks — guide — Turing.com guide on evaluation and benchmarking
[3]. **An Engineer's Guide to AI Code Model Evals** — https://addyosmani.com/blog/ai-evals/ — blog — Addy Osmani guide on AI code evals
[4]. **An Introduction to LLM Benchmarking** — https://www.confident-ai.com/blog/the-current-state-of-benchmarking-llms — blog — Confident AI introduction to LLM benchmarking
[5]. **Benchmarks and Metrics for Evaluations of Code Generation** — https://arxiv.org/html/2406.12655v1 — academic — ArXiv article on code generation benchmarks
[6]. **Best LLM Evaluation Tools: Top 9 Frameworks** — https://www.zenml.io/blog/best-llm-evaluation-tools — blog — ZenML blog on evaluation frameworks
[7]. **Best prompt evaluation tools Braintrust** — https://www.braintrust.dev/articles/best-prompt-evaluation-tools-2025 — article — 2025 evaluation tools
[8]. **Build Prompt Evaluation Framework** — https://www.newline.co/@zaoyang/how-to-build-a-prompt-evaluation-framework--ebdc89a5 — guide — Building evaluation frameworks
[9]. **DeepEval GitHub repository** — https://github.com/confident-ai/deepeval — repo — DeepEval open-source evaluation framework
[10]. **Define your evaluation metrics | Vertex AI** — https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/determine-eval — doc — Google Vertex AI documentation on evaluation metrics
[11]. **Evaluation harness** — https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/eval-harness — Doc — Databricks' evaluation harness documentation
[12]. **Evaluation Metrics for AI Products That Drive Trust** — https://productschool.com/blog/artificial-intelligence/evaluation-metrics — guide — Product School guide on evaluation metrics
[13]. **How to Evaluate AI Outputs for Accuracy, Quality, and Bias** — https://medium.com/@dharamai2024/%EF%B8%8F-how-to-evaluate-ai-outputs-for-accuracy-quality-and-bias-a488b298ea45 — blog — Medium article on AI output evaluation
[14]. **LLM Benchmarks 2026 - Complete Evaluation Suite** — https://llm-stats.com/benchmarks — reference — LLM benchmarks reference site
[15]. **LLM Evaluation Frameworks, Metrics & Methods Explained** — https://qualifire.ai/posts/llm-evaluation-frameworks-metrics-methods-explained — blog — Qualifire blog on evaluation frameworks
[16]. **LLM Evaluation Metrics: The Ultimate LLM Evaluation Guide** — https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation — guide — Confident AI comprehensive evaluation metrics guide
[17]. **LLM Prompt Evaluation Frameworks OpenAI** — https://community.openai.com/t/llm-and-prompt-evaluation-frameworks/945070 — community — OpenAI evaluation frameworks
[18]. **Measuring AI Code Generation Quality: Metrics and Benchmarks** — https://www.gocodeo.com/post/measuring-ai-code-generation-quality-metrics-benchmarks-and-best-practices — blog — Gocodeo guide on code generation quality
[19]. **Microsoft PromptBench** — https://github.com/microsoft/promptbench — repo — Microsoft prompt benchmarking
[20]. **OpenAI Evals GitHub repository** — https://github.com/openai/evals — repo — OpenAI's evals framework for benchmarking
[21]. **Prompt Evaluation at Scale** — https://www.getmaxim.ai/articles/prompt-evaluation-frameworks-measuring-quality-consistency-and-cost-at-scale/ — article — Evaluating prompts at scale
[22]. **Prompt Evaluation Frameworks Helicone** — https://www.helicone.ai/blog/prompt-evaluation-frameworks — article — Evaluating prompt frameworks
[23]. **Prompt Evaluation Mirascope** — https://mirascope.com/blog/prompt-evaluation — guide — Mirascope evaluation guide
[24]. **Prompt Testing Frameworks Mirascope** — https://mirascope.com/blog/prompt-testing-framework — article — Testing frameworks for prompts
[25]. **promptfoo GitHub** — https://github.com/promptfoo/promptfoo — repo — Promptfoo testing framework
[26]. **The Definitive Guide to LLM Evaluation** — https://arize.com/llm-evaluation/ — guide — Arize comprehensive guide to LLM evaluation

### A11. Workflow Automation

[1]. **AI Automation | Make** — https://www.make.com/en/ai-automation — tool — Make.com AI automation features
[2]. **APIpie.ai API Reference, Documentation, & Features Guide** — https://apipie.ai/docs/Integrations/Agent-Frameworks/Agno — Doc — APIpie's Agno integration guide
[3]. **Best AI Tools to Automate Blogs and Content Writing** — https://pinggy.io/blog/best_ai_tools_for_blog_and_content_writing/ — blog — Pinggy guide to content writing automation
[4]. **Code Graph: From Visualization to Integration** — https://www.falkordb.com/blog/code-graph/ — blog — FalkorDB blog on code graphs
[5]. **Durable Execution Solutions** — https://temporal.io/ — Doc — Temporal homepage
[6]. **GitHub - inngest/inngest** — https://github.com/inngest/inngest — Repo — Inngest official repository
[7]. **Inngest - AI** — https://www.inngest.com/ai — Doc — Inngest's AI-specific documentation
[8]. **Inngest vs Temporal: Durable execution that developers love** — https://www.inngest.com/compare-to-temporal — Blog — Inngest's comparison with Temporal
[9]. **Inngest vs. Temporal: Which one should you choose** — https://akka.io/blog/inngest-vs-temporal — Blog — Akka's Inngest vs Temporal comparison
[10]. **Jupyter AI: How to Do AI Coding Directly In Jupyter Notebooks** — https://medium.com/data-science-collective/jupyter-ai-how-to-do-ai-coding-directly-in-jupyter-notebooks-e86eb67196f7 — guide — Jupyter AI integration
[11]. **Kinde AI Code Review Automation** — https://www.kinde.com/learn/ai-for-software-engineering/code-reviews/ai-code-review-automation-building-custom-linting-rules-with-llms/ — guide — Kinde guide on AI code review
[12]. **Nx and AI - Why They Work so Well Together** — https://nx.dev/blog/nx-and-ai-why-they-work-together — blog — Nx blog on AI integration
[13]. **Pair Programming Guide: Benefits, Techniques & AI Integration** — https://talent500.com/blog/pair-programming-guide-techniques-benefits-ai-integration/ — guide — Talent500 comprehensive guide on pair programming

### A12. Knowledge Management & Documentation

[1]. **10 Revolutionary AI-Powered Knowledge Management Tools** — https://www.bitrix24.com/articles/10-revolutionary-ai-powered-knowledge-management-tools-to-transform-your-team.php — guide — Bitrix24 guide to AI knowledge management tools
[2]. **6 Best AI Tools for Coding Documentation** — https://www.index.dev/blog/best-ai-tools-for-coding-documentation — blog — Index guide on AI documentation tools
[3]. **AI and LLM Observability - Dynatrace Docs** — https://docs.dynatrace.com/docs/observe/dynatrace-for-ai-observability — Doc — Dynatrace's AI observability documentation
[4]. **AI in Knowledge Management: Overview, Key Features, and Top Tools** — https://document360.com/blog/ai-in-knowledge-management/ — blog — Document360 guide on AI in knowledge management
[5]. **AI in knowledge management: Use cases, applications, benefits and development** — https://www.leewayhertz.com/ai-in-knowledge-management/ — guide — LeewayHertz guide on AI knowledge management applications
[6]. **AI knowledge base: A complete guide for 2026** — https://www.zendesk.com/service/help-center/ai-knowledge-base/ — guide — Zendesk guide to AI knowledge bases
[7]. **AI model comparison** — https://docs.github.com/en/copilot/reference/ai-models/model-comparison — doc — GitHub documentation on model comparison
[8]. **AI-Based Knowledge Management System: Tools & Features** — https://www.livepro.com/ai-based-knowledge-management-system-overview/ — guide — Overview of AI knowledge management systems
[9]. **AI-Indexing GitHub repository** — https://github.com/NeaByteLab/AI-Indexing — repo — Code indexing examples for AI
[10]. **ALIGNMENT FAKING IN LARGE LANGUAGE MODELS** — https://assets.anthropic.com/m/983c85a201a962f/original/Alignment-Faking-in-Large-Language-Models-full-paper.pdf — paper — Research paper on alignment faking
[11]. **Alignment Research** — https://www.anthropic.com/research/team/alignment — doc — Alignment research team page
[12]. **API Documentation Best Practices 2026** — https://www.theneo.io/blog/api-documentation-best-practices-how-to-simplify-integration-for-developers-2026 — guide — Theneo guide on API documentation
[13]. **API Documentation with Workik AI** — https://workik.com/ai-powered-api-documentation — tool — Workik AI API documentation tool
[14]. **AST Parsing at Scale: Tree-sitter Across 40 Languages** — https://www.dropstone.io/blog/ast-parsing-tree-sitter-40-languages — blog — Dropstone research on tree-sitter
[15]. **AutoGen - Microsoft Research** — https://www.microsoft.com/en-us/research/project/autogen/ — Doc — Microsoft's AutoGen project overview
[16]. **AutoGen - AutoGen** — https://microsoft.github.io/autogen/stable//index.html — Doc — AutoGen official documentation
[17]. **Automatic Code Generation from Design Patterns** — https://www.researchgate.net/publication/224102052_Automatic_Code_Generation_from_Design_Patterns — academic — ResearchGate paper on design patterns
[18]. **Awesome-Code-LLM GitHub repository** — https://github.com/codefuse-ai/Awesome-Code-LLM — repo — Curated list of code LLM research
[19]. **Best Practices for API Documentation** — https://www.graphapp.ai/blog/best-practices-for-api-documentation — blog — Graph AI blog on API docs
[20]. **Codebases are uniquely hard to search semantically** — https://www.greptile.com/blog/semantic-codebase-search — blog — Greptile blog on semantic code search challenges
[21]. **Core Concepts in ast-grep's Pattern** — https://ast-grep.github.io/advanced/core-concepts.html — doc — ast-grep documentation on core concepts
[22]. **Customization Overview | Continue Docs** — https://docs.continue.dev/customize/overview — doc — Continue.dev customization documentation
[23]. **Document and Comment Code with AI** — https://dev.to/keploy/document-and-comment-code-with-ai-33a6 — blog — DEV Community guide on AI-assisted documentation
[24]. **Documentation standards for AI systems** — https://verifywise.ai/lexicon/documentation-standards-for-ai-systems — reference — Verifywise lexicon entry on documentation standards
[25]. **Documentation | ICO** — https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/explaining-decisions-made-with-artificial-intelligence/part-3-what-explaining-ai-means-for-your-organisation/documentation/ — guide — ICO guidance on AI documentation
[26]. **Gemini Code Assist overview** — https://developers.google.com/gemini-code-assist/docs/overview — doc — Google's Gemini Code Assist documentation
[27]. **Getting Better LLM Responses Using AI-Friendly Documentation** — https://www.aiboosted.dev/p/getting-better-llm-responses-using-ai-friendly-docs — blog — AIBoosted guide on AI-friendly documentation
[28]. **GitLab Knowledge Graph** — https://docs.gitlab.com/user/project/repository/knowledge_graph/ — doc — GitLab documentation on knowledge graphs
[29]. **How AI is shaping the Future of AI Knowledge Management** — https://www.clearpeople.com/blog/ai-future-knowledge-management-systems — blog — ClearPeople blog on future of knowledge management
[30]. **How AI Knowledge Management Helps Scale Enterprise Operations** — https://www.acrolinx.com/blog/how-ai-knowledge-management-helps-scale-enterprise-operations/ — blog — Acrolinx blog on enterprise knowledge management
[31]. **How to document and comment code using AI** — https://www.pluralsight.com/resources/blog/software-development/documenting-commenting-code-with-AI — blog — Pluralsight guide on AI-assisted documentation
[32]. **How to Document APIs for AI Consumption** — https://www.infobip.com/developers/blog/how-to-document-apis-for-ai-consumption-a-practical-guide — guide — Infobip guide on AI-friendly API documentation
[33]. **How to Optimize API Documentation for AI Discoverability** — https://nordicapis.com/how-to-optimize-api-documentation-for-ai-discoverability/ — guide — Nordic APIs guide on AI-discoverable docs
[34]. **How to optimize your docs for LLMs** — https://redocly.com/blog/optimizations-to-make-to-your-docs-for-llms — blog — Redocly guide on documentation optimization for LLMs
[35]. **How to use AI in knowledge management** — https://blog.box.com/ai-knowledge-management — blog — Box blog on AI knowledge management
[36]. **LLM-Friendly Documentation: Creating Content That AI Can Understand** — https://aronhack.com/llm-friendly-documentation-creating-content-that-ai-can-understand-and-process-effectively/ — guide — ARON HACK comprehensive guide on LLM-friendly documentation
[37]. **LLM-ready docs | GitBook Documentation** — https://gitbook.com/docs/publishing-documentation/llm-ready-docs — doc — GitBook guide to LLM-ready documentation
[38]. **LLM-ready Docs - DatoCMS** — https://www.datocms.com/docs/llm-ready-docs — doc — DatoCMS guide to LLM-ready documentation
[39]. **LLM01:2025 Prompt Injection** — https://genai.owasp.org/llmrisk/llm01-prompt-injection/ — Doc — OWASP's prompt injection risk documentation
[40]. **Making Your Documentation AI-Friendly: A Practical Guide** — https://dev.to/sudo_overflow/making-your-documentation-ai-friendly-a-practical-guide-2h1f — blog — DEV Community practical guide on AI-friendly documentation
[41]. **Optimizing technical documentations for LLMs** — https://dev.to/joshtom/optimizing-technical-documentations-for-llms-4bcd — blog — DEV Community guide on LLM-friendly documentation
[42]. **Parallel Tools - Instructor** — https://python.useinstructor.com/concepts/parallel/ — Doc — Instructor's parallel tools documentation
[43]. **Pattern-Based Code Generation** — https://www.researchgate.net/publication/2379461_Pattern-Based_Code_Generation_for_Well-Defined_Application_Domains — academic — ResearchGate paper on pattern-based generation
[44]. **Practical tips to optimize technical documentation for LLMs** — https://biel.ai/blog/optimizing-docs-for-ai-agents-complete-guide — blog — Biel.ai comprehensive guide on documentation optimization
[45]. **probe GitHub repository** — https://github.com/probelabs/probe — repo — AI-friendly semantic code search engine
[46]. **Program Synthesis using Natural Language** — https://www.microsoft.com/en-us/research/wp-content/uploads/2016/07/NLPSynthesis.pdf — academic — Microsoft research paper on NL synthesis
[47]. **Program synthesis using natural language | ResearchGate** — https://www.researchgate.net/publication/303099112_Program_synthesis_using_natural_language — academic — ResearchGate entry on NL synthesis
[48]. **Semantic Code Indexing with AST and Tree-sitter** — https://medium.com/@email2dineshkuppan/semantic-code-indexing-with-ast-and-tree-sitter-for-ai-agents-part-1-of-3-eb5237ba687a — blog — Medium series on AST indexing
[49]. **Semantic Code Search** — https://medium.com/@wangxj03/semantic-code-search-010c22e7d267 — blog — Medium article on semantic code search
[50]. **State Machines - Scale AI** — https://docs.gp.scale.com/docs/agents/state-machines — Doc — Scale AI's state machines documentation
[51]. **The Landscape of Transparent Documentation Standards for AI** — https://medium.com/@JerryCuomo/the-landscape-of-transparent-documentation-standards-for-ai-9b3b434d7fff — blog — Jerry Cuomo Medium article on AI documentation standards
[52]. **The Ultimate Guide to API Documentation Best Practices 2025** — https://www.theneo.io/blog/api-documentation-best-practices-guide-2025 — guide — Theneo comprehensive API documentation guide
[53]. **Theneo - Build Docs Developers Love** — https://www.theneo.io/ — tool — Theneo API documentation platform
[54]. **Tool search with embeddings** — https://platform.claude.com/cookbook/tool-use-tool-search-with-embeddings — guide — Guide to tool search using embeddings
[55]. **What Is Knowledge Management AI** — https://www.salesforce.com/service/ai/what-is-knowledge-management-ai/ — guide — Salesforce guide to knowledge management AI
[56]. **Writing documentation for AI: best practices** — https://docs.kapa.ai/improving/writing-best-practices — doc — Kapa.ai documentation best practices for AI

### A13. AI Safety & Security

[1]. **AI Guardrails: Enforcing Safety Without Slowing Innovation** — https://www.obsidiansecurity.com/blog/ai-guardrails — Blog — Obsidian Security's guardrails article
[2]. **Continuously hardening ChatGPT Atlas against prompt injection attacks** — https://openai.com/index/hardening-atlas-against-prompt-injection/ — Blog — OpenAI's prompt injection hardening article
[3]. **Indirect Prompt Injection: The Hidden Threat** — https://www.lakera.ai/blog/indirect-prompt-injection — Blog — Lakera's indirect prompt injection guide
[4]. **Permissions and Security - Tips | SFEIR Institute** — https://institute.sfeir.com/en/claude-code/claude-code-permissions-and-security/tips/ — guide — Permissions tips and tricks
[5]. **Prevent Prompt Injection IBM** — https://www.ibm.com/think/insights/prevent-prompt-injection — article — IBM injection prevention
[6]. **Prompt Injection & the Rise of Prompt Attacks** — https://www.lakera.ai/blog/guide-to-prompt-injection — Guide — Lakera's prompt injection guide
[7]. **Prompt Injection Attacks: The Most Common AI Exploit in 2025** — https://www.obsidiansecurity.com/blog/prompt-injection — Blog — Obsidian Security's prompt injection article
[8]. **Prompt injection defenses GitHub** — https://github.com/tldrsec/prompt-injection-defenses — repo — Defense against injection
[9]. **Prompt Shields Azure** — https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection — doc — Azure jailbreak detection
[10]. **Understanding prompt injections: a frontier security challenge** — https://openai.com/index/prompt-injections/ — Blog — OpenAI's prompt injection article
[11]. **What Is a Prompt Injection Attack** — https://www.ibm.com/think/topics/prompt-injection — Blog — IBM's prompt injection explanation
[12]. **What Is a Prompt Injection Attack?** — https://www.paloaltonetworks.com/cyberpedia/what-is-a-prompt-injection-attack — Blog — Palo Alto Networks' prompt injection explanation

### A14. Emerging Patterns & Community

[1]. **10 AI Code Review Tools** — https://www.digitalocean.com/resources/articles/ai-code-review-tools — guide — DigitalOcean guide on code review tools
[2]. **11 best AI content writing tools** — https://www.clearscope.io/blog/best-ai-content-writing-tools — blog — Clearscope guide to content writing tools
[3]. **12 Best AI Tools to Use for Content Creation** — https://www.getblend.com/blog/10-best-ai-tools-to-use-for-content-creation/ — blog — Getblend guide to content creation tools
[4]. **19 Best AI Content Writing Tools Reviewed** — https://thecmo.com/tools/best-ai-content-writing-tools/ — blog — CMO guide to content writing tools
[5]. **5 Approaches to Solve LLM Token Limits** — https://www.deepchecks.com/5-approaches-to-solve-llm-token-limits/ — blog — Deepchecks guide on token limit solutions
[6]. **5 metrics to measure AI-generated answers' decision-making impact** — https://www.glean.com/blog/metrics-ai-decision-impact — blog — Glean blog on measuring decision impact
[7]. **6 AI-Powered Code Linter Platforms** — https://www.augmentcode.com/tools/6-ai-powered-code-linter-platforms-for-quality-gate-automation — guide — Augment Code guide on AI linters
[8]. **8 best AI coding tools for developers: tested & compared** — https://blog.n8n.io/best-ai-for-coding/ — blog — n8n blog comparing AI coding tools
[9]. **8 best practices for creating architecture decision records** — https://www.techtarget.com/searchapparchitecture/tip/4-best-practices-for-creating-architecture-decision-records/ — guide — TechTarget guide on ADR best practices
[10]. **9 Automated Naming Conventions for Project Files** — https://www.getsortio.com/articles/digital-workspace-productivity/9-automated-naming-conventions-for-project-files-that-will-save-you-time-and-reduce-stress — guide — Sortio guide on automated naming
[11]. **A Beginner's Guide to Tree-sitter** — https://dev.to/shreshthgoyal/understanding-code-structure-a-beginners-guide-to-tree-sitter-3bbc — blog — DEV Community guide on tree-sitter
[12]. **A Beginner's Guide to Tree-sitter | Medium** — https://medium.com/@shreshthg30/a-beginners-guide-to-tree-sitter-6698f2696b48 — blog — Medium introduction to tree-sitter
[13]. **A Deep Dive Into ast-grep's Pattern** — https://betterprogramming.pub/deep-dive-into-ast-greps-pattern-7efc3eefc7c3 — blog — Better Programming deep dive on ast-grep
[14]. **A developer's guide to OpenAI SDKs in 2025** — https://www.eesel.ai/blog/openai-sdks — Blog — Eesel's OpenAI SDKs guide
[15]. **A Guide to Code Generation** — https://tomassetti.me/code-generation/ — guide — Strumenta comprehensive guide to code generation
[16]. **A Toolchain for AI-Assisted Code Specification, Synthesis** — https://atlascomputing.org/ai-assisted-fv-toolchain.pdf — academic — Paper on AI-assisted code specification
[17]. **Accelerate test-driven development with AI** — https://github.com/readme/guides/github-copilot-automattic — guide — GitHub Readme guide on TDD acceleration
[18]. **Adding Comments with an AI Code Generator** — https://www.ninjatech.ai/blog/using-ninjas-ai-code-generator-to-comment-your-code — blog — Ninja AI blog on comment generation
[19]. **ADR process - AWS Prescriptive Guidance** — https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html — guide — AWS guide on ADR process
[20]. **AI Code Review with Rovo Dev** — https://www.atlassian.com/software/rovo-dev/code-review — doc — Atlassian Rovo Dev code review features
[21]. **AI Copywriter & Content Writer - Copymatic** — https://copymatic.ai/ — tool — Copymatic AI copywriting tool
[22]. **AI Debugging Tools** — https://www.createq.com/en/software-engineering-hub/ai-debugging-tools — guide — Createq guide on AI debugging
[23]. **AI Debugging: Identifying and Fixing Model Errors** — https://focalx.ai/ai/ai-debugging/ — guide — FocalX guide on AI debugging
[24]. **AI for Automated Code Comments** — https://medium.com/@sayaleedamle/ai-for-automated-code-comments-7f5427ffb313 — blog — Medium article on automated comments
[25]. **AI for Education Prompt Library** — https://www.aiforeducation.io/prompt-library — resource — Educational prompt library
[26]. **AI generated Architecture Decision Records (ADR)** — https://adolfi.dev/blog/ai-generated-adr/ — blog — Adolfi blog on AI-generated ADRs
[27]. **AI Guardrails: Building Safe, Compliant AI** — https://witness.ai/blog/ai-guardrails/ — Blog — WitnessAI's guardrails guide
[28]. **AI Metrics: How to Measure and Evaluate AI Performance** — https://sendbird.com/blog/ai-metrics-guide — guide — Sendbird guide to AI metrics
[29]. **AI model performance metrics: In-depth guide** — https://nebius.com/blog/posts/ai-model-performance-metrics — guide — Nebius guide on performance metrics
[30]. **AI Native Universal Linter** — https://www.coderabbit.ai/blog/ai-native-universal-linter-ast-grep-llm — blog — CodeRabbit blog on AI native linting
[31]. **AI observability tools: A buyer's guide** — https://www.braintrust.dev/articles/best-ai-observability-tools-2026 — Guide — Braintrust's observability tools guide
[32]. **AI Pair Programming** — https://www.createq.com/en/software-engineering-hub/ai-pair-programming — guide — Createq guide to AI pair programming
[33]. **AI Prompt Library Notion Template** — https://www.notion.com/templates/ai-prompt-library — template — Notion prompt library template
[34]. **AI readable naming convention** — https://patterns.hattori.dev/design-pattern/ai-readable-naming-convention/ — guide — Hattori guide on AI-readable naming
[35]. **AI Token Pricing Optimization: Dynamic Cost Management** — https://kinde.com/learn/billing/billing-for-ai/ai-token-pricing-optimization-dynamic-cost-management-for-llm-powered-saas/ — Guide — Kinde's token pricing optimization
[36]. **AI Tokens Explained: Complete Guide to Usage, Optimization & Costs** — https://guptadeepak.com/complete-guide-to-ai-tokens-understanding-optimization-and-cost-management/ — Guide — Deepak Gupta's comprehensive token guide
[37]. **AI-assisted engineering: How AI is transforming software development** — https://getdx.com/blog/ai-assisted-engineering-hub/ — blog — GetDX blog on AI-assisted engineering
[38]. **AI-first debugging: Tools and techniques** — https://blog.logrocket.com/ai-debugging/ — blog — LogRocket blog on AI debugging
[39]. **AI-First Development Patterns for Modern Teams** — https://www.propelcode.ai/blog/ai-first-development-patterns-modern-teams — blog — Propel guide on AI-first development patterns
[40]. **AI-powered debugging tools** — https://graphite.com/guides/ai-powered-debugging-tools — guide — Graphite guide on AI debugging tools
[41]. **AI-Powered Pair Programming: best practices** — https://teachmeidea.com/ai%E2%80%91powered-pair-programming-best-practices-for-collaborating-with-an-ai-assistant/ — guide — TeachMeIdea guide on pair programming best practices
[42]. **Architectural Decision Records (ADRs)** — https://adr.github.io/ — resource — Official ADR website
[43]. **Architecture decision records overview** — https://cloud.google.com/architecture/architecture-decision-records — guide — Google Cloud guide on ADRs
[44]. **architecture-decision-record GitHub repository** — https://github.com/joelparkerhenderson/architecture-decision-record — repo — ADR examples and templates
[45]. **Are there industry-specific naming conventions?** — https://www.wisfile.ai/faq/are-there-industry-specific-naming-conventions-i-should-follow — faq — Wisfile FAQ on naming conventions
[46]. **Assessing AI Code Quality: 10 Critical Dimensions** — https://runloop.ai/blog/assessing-ai-code-quality-10-critical-dimensions-for-evaluation — blog — Runloop guide on code quality assessment
[47]. **Automatic code generation from design patterns** — https://ieeexplore.ieee.org/document/5387226 — academic — IEEE paper on automatic code generation
[48]. **Azure AI Model Router: When Dynamic Model Selection Actually Makes Sense** — https://codingwithramin.com/?p=578 — Blog — Coding with Ramin's Azure model router article
[49]. **Backend Coding AI Context: DDD and Hexagonal Architecture** — https://medium.com/@bardia.khosravi/backend-coding-rules-for-ai-coding-agents-ddd-and-hexagonal-architecture-ecafe91c753f — blog — Medium article on DDD with AI
[50]. **Best AI Code Assistants Reviews 2026 | Gartner Peer Insights** — https://www.gartner.com/reviews/market/ai-code-assistants — review — Gartner peer reviews of code assistants
[51]. **Best Automated Code Review Tools** — https://www.qodo.ai/blog/best-automated-code-review-tools-2026/ — blog — Qodo guide on automated code review
[52]. **Best Practices for Coding with AI in 2024** — https://blog.codacy.com/best-practices-for-coding-with-ai — blog — Codacy guide on coding with AI
[53]. **Best practices for pair programming with AI assistants** — https://graphite.com/guides/ai-pair-programming-best-practices — guide — Graphite guide on AI pair programming
[54]. **Best practices for writing code comments** — https://stackoverflow.blog/2021/12/23/best-practices-for-writing-code-comments/ — blog — Stack Overflow blog on commenting best practices
[55]. **Better AI Driven Development with Test Driven Development** — https://medium.com/effortless-programming/better-ai-driven-development-with-test-driven-development-d4849f67e339 — blog — Medium article on AI-driven TDD
[56]. **Bridging Natural Language and Formal Specification** — https://arxiv.org/pdf/2512.17334 — academic — ArXiv paper on NL and formal specifications
[57]. **Build a prompt library with Microsoft Lists** — https://pnp.github.io/blog/post/build-a-prompt-library-with-microsoft-lists/ — blog — Microsoft tutorial on building prompt libraries
[58]. **Build prompt library Microsoft Lists** — https://pnp.github.io/blog/post/build-a-prompt-library-with-microsoft-lists — guide — Building prompt library in Lists
[59]. **Building a Knowledge Graph of Your Codebase** — https://www.daytona.io/dotfiles/building-a-knowledge-graph-of-your-codebase — blog — Daytona guide on knowledge graphs
[60]. **Building an AI-Powered Linter** — https://alfaorigin.com/ai-powered-linter/ — blog — AlfaOrigin guide on AI linters
[61]. **C2S: Translating Natural Language Comments to Formal Program Specifications** — https://www.cs.purdue.edu/homes/lintan/publications/c2s-fse20.pdf — academic — Purdue paper on NL to specifications
[62]. **Chapter 12 - Observability** — https://azure.github.io/AI-in-Production-Guide/chapters/chapter_12_keeping_log_observability — Guide — Azure AI in Production observability guide
[63]. **Code Configuration | Continue** — https://docs.continue.dev/customization/code-config — doc — Continue.dev code configuration guide
[64]. **Code Organization Best Practices** — https://www.swiftorial.com/tutorials/artificial_intelligence/openai_api/best_practices/code_organization/ — guide — Swiftorial guide on code organization
[65]. **CodeRabbit | AI Code Review** — https://www.coderabbit.ai/ — tool — CodeRabbit AI code review platform
[66]. **Coding Like a Chef: Using Recipes (Design Patterns)** — https://algocademy.com/blog/coding-like-a-chef-using-recipes-design-patterns-to-write-reusable-code/ — blog — AlgoCademy blog on design patterns
[67]. **Cognee - Build a Knowledge Graph from a Python Repo** — https://www.cognee.ai/blog/deep-dives/repo-to-knowledge-graph — blog — Cognee guide on building knowledge graphs
[68]. **Commenting Conventions** — https://iis.uibk.ac.at/public/piater/courses/Coding-Style/ar01s02.html — reference — University guide on commenting conventions
[69]. **Comments in code written by AI** — https://www.mrlacey.com/2024/04/comments-in-code-written-by-ai.html — blog — Matt Lacey blog on AI-generated comments
[70]. **Context-Augmented Code Generation Using Programming Knowledge Graphs** — https://openreview.net/forum?id=EHfn5fbFHw — academic — OpenReview paper on knowledge graphs for code
[71]. **Cost Optimisation Strategies for Token Consumption** — https://chatbotkit.com/tutorials/cost-optimisation-strategies-for-token-consumption — Guide — ChatbotKit's cost optimization guide
[72]. **Cracking the Code: A Beginner's Guide to Design Patterns** — https://medium.com/@gangapuramvishal/cracking-the-code-a-beginners-guide-to-design-patterns-eab54ffacc30 — blog — Medium guide on design patterns
[73]. **Create, version and deploy prompts | Portkey** — https://portkey.ai/features/prompt-management — tool — Portkey prompt management platform
[74]. **Customize AI in Visual Studio Code** — https://code.visualstudio.com/docs/copilot/customization/overview — doc — VS Code AI customization overview
[75]. **Customize AI responses in VS Code** — https://code.visualstudio.com/docs/copilot/copilot-customization — doc — VS Code AI customization guide
[76]. **Debugging AI-Generated Code. Strategies** — https://medium.com/@e2larsen/debugging-ai-generated-code-5fd7cfcc5648 — blog — Medium article on debugging AI code
[77]. **Debugging AI-Generated Code: 8 Failure Patterns & Fixes** — https://www.augmentcode.com/guides/debugging-ai-generated-code-8-failure-patterns-and-fixes — guide — Augment Code guide on debugging
[78]. **Design Patterns and Refactoring** — https://sourcemaking.com/design_patterns — reference — SourceMaking design patterns reference
[79]. **Design Patterns For AI Interfaces** — https://www.smashingmagazine.com/2025/07/design-patterns-ai-interfaces/ — Blog — Smashing Magazine's AI interface patterns
[80]. **Design-Pattern-Code-Generator GitHub repository** — https://github.com/samujjwaal/Design-Pattern-Code-Generator — repo — Design pattern code generator tool
[81]. **Developer Experience (DX) - Guild.ai** — https://www.guild.ai/glossary/developer-experience-dx — guide — Guild.ai glossary entry on DX
[82]. **Developer Experience (DX): Building Better Internal Tools** — https://dasroot.net/posts/2026/01/developer-experience-building-better-internal-tools/ — blog — dasroot.net guide on DX and internal tools
[83]. **Developer Experience - Wikipedia** — https://en.wikipedia.org/wiki/Developer_Experience — reference — Wikipedia entry on developer experience
[84]. **Developer Experience(DX): Importance, Metrics, and Best Practices** — https://blog.bit.ai/developer-experience/ — blog — Bit.ai blog on DX best practices
[85]. **Developers with AI assistants need to follow the pair programming model** — https://stackoverflow.blog/2024/04/03/developers-with-ai-assistants-need-to-follow-the-pair-programming-model/ — blog — Stack Overflow article on AI pair programming
[86]. **Doc Driven Development** — https://docdd.ai/ — resource — Doc Driven Development resource
[87]. **Domain Driven Design in AI-Driven Era** — https://dev.to/aws-heroes/domain-driven-design-in-ai-driven-era-4l3h — blog — DEV Community article on DDD in AI era
[88]. **Domain-driven design** — https://en.wikipedia.org/wiki/Domain-driven-design — reference — Wikipedia entry on DDD
[89]. **Domain-Driven Design in Practice: Crafting an AI Assistant** — https://odsc.medium.com/domain-driven-design-in-practice-crafting-an-ai-assistant-step-by-step-a675e6f5ec11 — blog — ODSC Medium article on DDD with AI
[90]. **Domain-Driven Design with AI Assistance** — https://developertoolkit.ai/en/shared-workflows/development-workflows/domain-driven-design/ — guide — Developer Toolkit guide on DDD with AI
[91]. **DX: Developer Intelligence Platform** — https://getdx.com/ — tool — GetDX developer intelligence platform
[92]. **Dynamic LLM Routing in n8n** — https://medium.com/@zafer_kahraman/modular-llm-routing-in-n8n-switch-between-openai-ollama-instantly-a27b322ca052 — Blog — Medium's n8n routing article
[93]. **Effective Prompts for AI: The Essentials** — https://mitsloanedtech.mit.edu/ai/basics/effective-prompts/ — guide — MIT guide on effective prompts
[94]. **Enhancing Domain-Driven Design with Generative AI** — https://medium.com/inspiredbrilliance/enhancing-domain-driven-design-with-generative-ai-5447f909e1a7 — blog — Medium article on DDD enhancement
[95]. **Essential Best Practices for API Consumption** — https://www.lunar.dev/post/api-consumption — blog — Lunar blog on API consumption
[96]. **Evaluating the Code Quality of AI-Assisted Code Generation Tools** — https://arxiv.org/abs/2304.10778 — academic — ArXiv study comparing code generation tools
[97]. **Evolving Human-in-the-Loop: Building Trustworthy AI** — https://www.seekr.com/resource/human-in-the-loop-in-an-autonomous-future/ — Blog — Seekr's HITL evolution article
[98]. **Explainability in AI Policies** — https://dl.acm.org/doi/fullHtml/10.1145/3593013.3594074 — academic — ACM article on AI explainability policies
[99]. **FastAPI** — https://fastapi.tiangolo.com/ — Doc — FastAPI framework
[100]. **File Naming Conventions | Data Management** — https://datamanagement.hms.harvard.edu/plan-design/file-naming-conventions — guide — HMS guide on file naming
[101]. **File Naming Conventions: A Complete Guide** — https://rename.click/blog/file-naming-conventions — guide — RenameClick guide on file naming
[102]. **File Naming Conventions: Best Practices** — https://www.resourcespace.com/blog/file-naming-conventions — blog — ResourceSpace blog on naming conventions
[103]. **FREE AI Powered Architecture Decision Record Generator** — https://workik.com/ai-powered-architecture-decision-record-generator — tool — Workik AI ADR generator
[104]. **From 150K to 2K Tokens: Progressive Context Loading** — https://williamzujkowski.github.io/posts/from-150k-to-2k-tokens-how-progressive-context-loading-revolutionizes-llm-development-workflows/ — blog — William Zujkowski on context loading optimization
[105]. **generative_ai_project GitHub repository** — https://github.com/honestsoul/generative_ai_project — repo — Template for building GenAI applications
[106]. **Get started with prompt library** — https://learn.microsoft.com/en-us/microsoft-copilot-studio/prompt-library — doc — Microsoft guide to prompt libraries
[107]. **Getting Started with Flutter Lint** — https://dcm.dev/blog/2025/10/21/getting-started-flutter-static-analytics-lints — blog — DCM blog on Flutter linting
[108]. **GitHub - microsoft/autogen** — https://github.com/microsoft/autogen — Repo — AutoGen official repository
[109]. **GitHub - microsoft/semantic-kernel** — https://github.com/microsoft/semantic-kernel — Repo — Semantic Kernel official repository
[110]. **GitHub - n8n-io/n8n** — https://github.com/n8n-io/n8n — Repo — n8n official repository
[111]. **GitHub - wshobson/commands** — https://github.com/wshobson/commands — repo — Collection of production-ready slash commands
[112]. **GitHub Enterprise Cloud with Data Residency** — https://github.com/enterprise/data-residency — product — GitHub Enterprise data residency page
[113]. **GitLab Knowledge Graph | GitLab Knowledge Graph** — https://gitlab-org.gitlab.io/rust/knowledge-graph/ — resource — GitLab knowledge graph resource
[114]. **Goodbye Linters? How AI is Transforming API Validation** — https://medium.com/@rgranadosd/goodbye-linters-how-ai-is-transforming-api-validation-cbb5686e7fca — blog — Medium article on AI linting
[115]. **gptlint GitHub repository** — https://github.com/gptlint/gptlint — repo — GPTLint open-source linting tool
[116]. **GraphGen4Code | A Toolkit for Generating Code Knowledge Graphs** — https://wala.github.io/graph4code/ — tool — GraphGen4Code toolkit
[117]. **How AI assistants interpret code comments** — https://www.glean.com/perspectives/how-ai-assistants-interpret-code-comments-a-practical-guide — guide — Glean guide on AI comment interpretation
[118]. **How AI Code Assistants Are Revolutionizing Test-Driven Development** — https://www.qodo.ai/blog/ai-code-assistants-test-driven-development/ — blog — Qodo blog on TDD with AI
[119]. **How Does AI Pair Programming Work and Should I Use It?** — https://zenvanriel.com/ai-engineer-blog/how-does-ai-pair-programming-work-complete-guide/ — guide — Zen Van Riel complete guide on AI pair programming
[120]. **How To Build Multi-Turn AI Conversations With Rasa** — https://rasa.com/blog/multi-turn-conversation — blog — Rasa blog on multi-turn conversations
[121]. **How to Configure Continue** — https://docs.continue.dev/customize/deep-dives/configuration — doc — Continue deep-dive configuration guide
[122]. **How to Create AI Transparency and Explainability** — https://shelf.io/blog/ai-transparency-and-explainability/ — blog — Shelf guide on AI transparency
[123]. **How to Evaluate Generative AI Output Effectively** — https://clarivate.com/academia-government/blog/evaluating-the-quality-of-generative-ai-output-methods-metrics-and-best-practices/ — blog — Clarivate guide on evaluating AI output
[124]. **How to Handle Token Limits and Rate Limits** — https://www.typedef.ai/resources/handle-token-limits-rate-limits-large-scale-llm-inference — guide — TypeDef guide on handling token limits
[125]. **How to Structure Your README File** — https://www.freecodecamp.org/news/how-to-structure-your-readme-file/ — guide — FreeCodeCamp guide to README structure
[126]. **How to Use AI in Coding - 12 Best Practices** — https://zencoder.ai/blog/how-to-use-ai-in-coding — blog — Zencoder guide on AI coding best practices
[127]. **How to Use Continue CLI** — https://docs.continue.dev/guides/cli — doc — Continue CLI usage guide
[128]. **HyperWrite | AI Writing Assistant** — https://www.hyperwriteai.com — tool — HyperWrite AI writing assistance tool
[129]. **IEEE SA - Autonomous and Intelligent Systems (AIS) Standards** — https://standards.ieee.org/initiatives/autonomous-intelligence-systems/standards/ — standard — IEEE standards on autonomous systems
[130]. **Introducing AI assistants with memory** — https://www.perplexity.ai/hub/blog/introducing-ai-assistants-with-memory — blog — Perplexity blog on AI memory
[131]. **Introducing Lightning Web Components Recipes** — https://developer.salesforce.com/blogs/2018/12/introducing-lightning-web-components-recipes-patterns-and-best-practices — blog — Salesforce blog on LWC recipes
[132]. **ISO/IEC TS 6254:2025 - Information technology - Artificial intelligence** — https://www.iso.org/standard/82148.html — standard — ISO standard on AI explainability
[133]. **Keep the AI Vibe: Optimizing Codebase Architecture for AI** — https://medium.com/@richardhightower/ai-optimizing-codebase-architecture-for-ai-coding-tools-ff6bb6fdc497 — blog — Medium article on AI-friendly architecture
[134]. **Knowledge Graph Based Repository-Level Code Generation** — https://arxiv.org/html/2505.14394v1 — academic — ArXiv paper on knowledge graph code generation
[135]. **KPIs for gen AI: Measuring your AI success** — https://cloud.google.com/transform/gen-ai-kpis-measuring-ai-success-deep-dive — guide — Google Cloud guide on AI KPIs
[136]. **Lint (software)** — https://en.wikipedia.org/wiki/Lint_(software) — reference — Wikipedia entry on linting
[137]. **LLM observability tools: Monitoring, debugging, and improving AI systems** — https://medium.com/online-inference/llm-observability-tools-monitoring-debugging-and-improving-ai-systems-5af769796266 — Guide — Medium's LLM observability guide
[138]. **LLM Token Optimization: Cut Costs & Latency** — https://redis.io/blog/llm-token-optimization-speed-up-apps/ — blog — Redis blog on token optimization
[139]. **LLM-Prompt-Library GitHub repository** — https://github.com/abilzerian/LLM-Prompt-Library — repo — Collection of experimental prompts and templates
[140]. **Logz.io: Modern Observability Powered by AI** — https://logz.io/ — Doc — Logz.io homepage
[141]. **Maintain an architecture decision record (ADR)** — https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record — doc — Microsoft Azure Well-Architected guide on ADRs
[142]. **Managing AI APIs: Best Practices** — https://devops.com/managing-ai-apis-best-practices-for-secure-and-scalable-ai-api-consumption/ — blog — DevOps.com guide on AI API management
[143]. **Mastering AI Token Cost Optimization: Strategies** — https://10clouds.com/blog/a-i/mastering-ai-token-optimization-proven-strategies-to-cut-ai-cost/ — Guide — 10Clouds' token optimization guide
[144]. **Measuring the Performance of AI Code Generation** — https://www.walturn.com/insights/measuring-the-performance-of-ai-code-generation-a-practical-guide/ — guide — WaltTurn guide on measuring code generation performance
[145]. **Measuring the quality of generative AI systems** — https://www.sciencedirect.com/science/article/pii/S0950584925001417 — academic — ScienceDirect article on measuring AI output quality
[146]. **Model Routing in AI: Getting the Right Request to the Right Model** — https://medium.com/@simsketch/model-routing-in-ai-getting-the-right-request-to-the-right-model-dd21bab7c129 — Blog — Medium's model routing article
[147]. **Monorepo - AI-native monorepo | Bit** — https://bit.dev/solutions/monorepo/ — tool — Bit AI-native monorepo solution
[148]. **Monorepo vs Multi-Repo AI** — https://www.augmentcode.com/tools/monorepo-vs-multi-repo-ai-architecture-based-ai-tool-selection — guide — Augment Code guide on monorepo architectures
[149]. **Monorepos & AI** — https://monorepo.tools/ai — guide — Monorepo.tools guide on AI and monorepos
[150]. **Multi-LLM routing strategies for generative AI applications on AWS** — https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/ — Blog — AWS's LLM routing guide
[151]. **Naming Conventions for Python Files** — https://www.oreateai.com/blog/naming-conventions-for-python-files/ — blog — Oreate AI guide on Python naming
[152]. **Naming Conventions Rules** — https://alguidelines.dev/docs/agentic-coding/vibe-coding-rules/al-naming-conventions/ — guide — AL guidelines on naming conventions
[153]. **Naming Conventions: Guidelines for Clarity and Consistency** — https://camphouse.io/blog/naming-conventions — blog — Camphouse blog on naming conventions
[154]. **Narrato - AI Content Creation and Marketing Software** — https://narrato.io/ — tool — Narrato AI content creation platform
[155]. **NISTIR 8312 Four Principles of Explainable AI** — https://nvlpubs.nist.gov/nistpubs/ir/2021/NIST.IR.8312.pdf — doc — NIST official guidance on explainable AI
[156]. **OpenObserve: Open Source Observability Platform** — https://openobserve.ai — Doc — OpenObserve platform
[157]. **Overcoming Token Limits in LLMs** — https://medium.com/@akshit.kharbanda04/overcoming-token-limits-in-llms-a-practical-system-for-multi-chunk-context-retention-1e5ab9d5b3a6 — blog — Medium article on token limit solutions
[158]. **Pair Programming with AI** — https://pairprogramming.ai/ — resource — Pair programming with AI home page
[159]. **Production best practices | OpenAI API** — https://developers.openai.com/api/docs/guides/production-best-practices/ — doc — OpenAI API production best practices
[160]. **Program Synthesis from Natural Language Using RNNs** — https://homes.cs.washington.edu/~mernst/pubs/nl-command-tr170301.pdf — academic — University of Washington paper on NL synthesis
[161]. **Program synthesis using natural language | ICSE** — https://dl.acm.org/doi/10.1145/2884781.2884786 — academic — ACM paper on NL synthesis
[162]. **Prompt caching | Generative AI on Vertex AI** — https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/claude/prompt-caching — doc — Google Cloud prompt caching guide
[163]. **Prompt generation OpenAI** — https://platform.openai.com/docs/guides/prompt-generation — doc — OpenAI prompt generation
[164]. **Prompt Libraries Medium** — https://medium.com/generative-ai-revolution-ai-native-transformation/prompt-libraries-where-to-find-them-how-to-use-them-smartly-94975f431cf1 — article — Finding and using prompt libraries
[165]. **Prompt Libraries PromptBuilder** — https://promptbuilder.cc/prompt-libraries — tool — PromptBuilder prompt libraries
[166]. **Prompt management guide** — https://ergonis.com/blog/prompt-management-guide — guide — Ergonis guide to prompt management
[167]. **Prompt Management Systems** — https://docs.vibe-coding-framework.com/resources/tools-and-integrations/prompt-management-systems — doc — Vibe coding framework guide on prompt management
[168]. **prompt-library GitHub topics** — https://github.com/topics/prompt-library — resource — GitHub topic collection of prompt libraries
[169]. **Promptly AI Library** — https://www.promptly.fyi/library — tool — Promptly AI library tool
[170]. **Pydantic AI** — https://ai.pydantic.dev/ — Doc — Pydantic AI homepage
[171]. **Qlerify: AI-Powered Domain-Driven Design Tool** — https://www.qlerify.com/domain-driven-design-tool — tool — Qlerify DDD tool
[172]. **Readme Driven Development** — https://tom.preston-werner.com/2010/08/23/readme-driven-development — blog — Classic article on README-driven development
[173]. **README driven development** — https://dev.to/gregmartinez44/readme-driven-development-373k — blog — DEV Community article on README-driven development
[174]. **README file generator, powered by AI** — https://github.com/eli64s/readme-ai — repo — Readme-ai tool for AI-generated README files
[175]. **Repomix | Pack your codebase into AI-friendly formats** — https://repomix.com/ — tool — Repomix tool for creating AI-friendly codebase formats
[176]. **Rytr - Free AI Writer and Content Generator** — https://rytr.me/ — tool — Rytr AI writing assistant
[177]. **Spec-driven development with AI** — https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/ — blog — GitHub blog on spec-driven development
[178]. **static-code-analysis skill** — https://playbooks.com/skills/aj-geddes/useful-ai-prompts/static-code-analysis — resource — Playbooks static analysis skill
[179]. **Synthesis of Mathematical programs from Natural Language** — https://arxiv.org/abs/2304.03287 — academic — ArXiv paper on mathematical program synthesis
[180]. **tdd-ai GitHub repository** — https://github.com/allenheltondev/tdd-ai — repo — Script for TDD with generative AI
[181]. **Test-Driven Development for Code Generation** — https://arxiv.org/abs/2402.13521 — academic — ArXiv paper on TDD for code generation
[182]. **Test-Driven Development using Generative AI** — https://www.galaksiya.com/articles/test-driven-development-using-generative-ai-to-create-good-code — blog — Galaksiya guide on TDD with GenAI
[183]. **Test-Driven Development with AI** — https://www.readysetcloud.io/blog/allen.helton/tdd-with-ai/ — blog — Ready Set Cloud guide on TDD with AI
[184]. **Test-Driven Generation (TDG)** — https://chanwit.medium.com/test-driven-generation-tdg-adopting-tdd-again-this-time-with-gen-ai-27f986bed6f8 — blog — Chanwit Medium article on TDG
[185]. **The 12 key principles of the CLeAR AI transparency framework** — https://sendbird.com/blog/ai-transparency-guide/ai-transparency-principles — blog — Sendbird guide on AI transparency principles
[186]. **The 4 Dimensions of API Developer Experience** — https://blog.apilayer.com/four-dimensions-of-api-developer-experience/ — blog — apilayer blog on API DX dimensions
[187]. **The 6 best AI writing generators** — https://zapier.com/blog/best-ai-writing-generator/ — blog — Zapier guide to AI writing generators
[188]. **The AI Debugging Assistant** — https://www.kinde.com/learn/ai-for-software-engineering/ai-agents/the-ai-debugging-assistant-training-custom-models-on-your-codebases-error-patterns/ — guide — Kinde guide on AI debugging
[189]. **The AI-Assisted Developer Experience** — https://erikralston.medium.com/the-ai-assisted-developer-experience-ec53f64a1b98 — blog — Medium article on AI-assisted DX
[190]. **The Best AI Models for Coding** — https://blog.jetbrains.com/ai/2026/02/the-best-ai-models-for-coding-accuracy-integration-and-developer-fit/ — blog — JetBrains AI blog on coding models
[191]. **The complete guide to AI transparency, explainability, and interpretability** — https://blog.stackaware.com/p/ai-transparency-explainability-interpretability-nist-rmf-iso-42001 — blog — Stackaware guide on AI transparency
[192]. **The End of Human-Readable Code: Write for AI** — https://pixelmap.medium.com/the-end-of-human-readable-code-its-time-to-write-for-ai-15a21786c4a2 — blog — Medium provocative article on code for AI
[193]. **The File Naming Convention System That Actually Works** — https://renamer.ai/insights/file-naming-conventions-best-practices — guide — Renamer AI guide on file naming
[194]. **The Importance of Code Comments for Modern AI Assistants** — https://medium.com/@iZonex/the-importance-of-code-comments-for-modern-ai-coding-assistants-fbfced948a28 — blog — Medium article on comments for AI
[195]. **Top 5 AI Code Review Tools** — https://www.kdnuggets.com/top-5-ai-code-review-tools-for-developers — guide — KDnuggets guide on code review tools
[196]. **Towards Formal Verification of LLM-Generated Code** — https://arxiv.org/pdf/2507.13290 — academic — ArXiv paper on verifying LLM code
[197]. **Tree-sitter: Revolutionizing Parsing with an Incremental Parsing Library** — https://www.deusinmachina.net/p/tree-sitter-revolutionizing-parsing — blog — Deus in Machina blog on tree-sitter
[198]. **TreeSitter - the holy grail of parsing source code** — https://symflower.com/en/company/blog/2023/parsing-code-with-tree-sitter/ — blog — Symflower blog on tree-sitter
[199]. **Understand Code Like an Editor: Intro to Tree-sitter** — https://dev.to/rijultp/understand-code-like-an-editor-intro-to-tree-sitter-50be — blog — DEV Community tree-sitter introduction
[200]. **Understanding Architecture Decision Records (ADR)** — https://www.oreateai.com/blog/understanding-architecture-decision-records-adr-in-software-development/ — blog — Oreate AI guide on ADRs
[201]. **Unraveling Tree-Sitter Queries** — https://dev.to/shrsv/unraveling-tree-sitter-queries-your-guide-to-code-analysis-magic-41il — blog — DEV Community guide on tree-sitter queries
[202]. **Using LLM Extensions in VSCode for Code Understanding** — https://www.gocodeo.com/post/using-llm-extensions-in-vscode-for-ai-powered-code-understanding-and-search — blog — Gocodeo guide on code understanding
[203]. **Wharton Prompt Library** — https://gail.wharton.upenn.edu/prompt-library/ — resource — Wharton AI prompt library
[204]. **What are AI guardrails** — https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-are-ai-guardrails — Blog — McKinsey's guardrails explanation
[205]. **What is Developer Experience (DevEx, DX)?** — https://www.port.io/blog/developer-experience — guide — Port.io guide on DX
[206]. **What is long context and why does it matter for AI?** — https://cloud.google.com/transform/the-prompt-what-are-long-context-windows-and-why-do-they-matter — blog — Google Cloud blog on long context
[207]. **What Is the Difference Between Static Code Analysis and Linting?** — https://www.in-com.com/blog/what-is-the-difference-between-static-code-analysis-and-linting/ — guide — In-Com guide on analysis and linting
[208]. **What Is Token-Based Pricing for AI Models** — https://www.mindstudio.ai/blog/token-based-pricing — Blog — MindStudio's token pricing explanation
[209]. **Workik AI Code Debugger** — https://workik.com/ai-code-debugger — tool — Workik AI debugging tool
[210]. **Workik AI JavaScript Code Debugger** — https://workik.com/ai-powered-javascript-code-debugger — tool — Workik JavaScript debugging tool
[211]. **Workik Code Comment Generator** — https://workik.com/code-comment-generator — tool — Workik AI comment generation tool
[212]. **Workik Code Linting Tool** — https://workik.com/code-linter — tool — Workik AI code linting tool

### A2. Cursor Skills & Rules (Official Docs & Community)

[1]. **.CursorRules Rules - Mastering .cursorrules in Cursor IDE** — https://dotcursorrules.com — guide — DotCursorRules comprehensive guide to .cursorrules
[2]. **awesome-cursorrules GitHub repository** — https://github.com/PatrickJS/awesome-cursorrules — repo — Collection of Cursor rules and patterns
[3]. **Best Cursor Rules** — https://dotcursorrules.com/blog/best-cursor-rules-mastering-cursorrules-for-cursor-ide — blog — DotCursorRules blog on best practices
[4]. **Cursor IDE Rules for AI** — https://kirill-markin.com/articles/cursor-ide-rules-for-ai/ — blog — Kirill Markin guide on Cursor IDE rules
[5]. **Cursor Rules Guide** — https://design.dev/guides/cursor-rules/ — guide — Design.dev guide to Cursor rules
[6]. **Cursor – Rules for AI** — https://docs.cursor.com/context/rules-for-ai — doc — Official Cursor documentation on rules
[7]. **cursor-best-practices GitHub repository** — https://github.com/digitalchild/cursor-best-practices — repo — Best practices guide for Cursor
[8]. **cursor-guide GitHub repository** — https://github.com/slava-kudzinau/cursor-guide — repo — Comprehensive Cursor IDE guide with recipes
[9]. **How Cursor Actually Indexes Your Codebase** — https://towardsdatascience.com/how-cursor-actually-indexes-your-codebase/ — blog — Towards Data Science article on Cursor indexing
[10]. **Improving agent with semantic search** — https://cursor.com/blog/semsearch — blog — Cursor blog on semantic search improvements
[11]. **Mastering Cursor IDE: 10 Best Practices** — https://medium.com/@roberto.g.infante/mastering-cursor-ide-10-best-practices-building-a-daily-task-manager-app-0b26524411c1 — blog — Medium guide on Cursor best practices
[12]. **Mastering Cursor IDE: Thinking Models, Cursor Rules** — https://medium.com/@vignarajj/mastering-cursor-ide-thinking-models-cursor-rules-and-effective-usage-6e512437bbc3 — blog — Medium guide on Cursor features

### A3. Prompt Engineering (Techniques, Patterns, Best Practices)

[1]. **11 Prompt Engineering Best Practices** — https://mirascope.com/blog/prompt-engineering-best-practices — blog — Mirascope guide on prompt engineering
[2]. **12 prompt engineering best practices and tips** — https://www.techtarget.com/searchenterpriseai/tip/Prompt-engineering-tips-and-best-practices — guide — TechTarget guide on prompt engineering
[3]. **16 Prompt Patterns** — https://www.prompthub.us/blog/prompt-patterns-what-they-are-and-16-you-should-know — guide — 16 key prompt patterns
[4]. **8 Best Prompt Engineering Tools in 2025** — https://mirascope.com/blog/prompt-engineering-tools — blog — Mirascope guide to prompt engineering tools
[5]. **Agentic Design Patterns Part 2: Reflection** — https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/ — Blog — DeepLearning.AI's article on reflection in agent design
[6]. **Agentic Knowledge Graph Construction** — https://learn.deeplearning.ai/courses/agentic-knowledge-graph-construction/information — Course — DeepLearning.AI's knowledge graph course
[7]. **Awesome AI System Prompts** — https://github.com/dontriskit/awesome-ai-system-prompts — repo — Curated system prompts
[8]. **Best practices for prompt engineering** — https://cloud.google.com/blog/products/application-development/five-best-practices-for-prompt-engineering — blog — Google Cloud guide on prompt engineering
[9]. **Best practices for prompt engineering with OpenAI API** — https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api — doc — OpenAI official prompt engineering guide
[10]. **Beyond prompt engineering: the shift to context engineering** — https://nearform.com/digital-community/beyond-prompt-engineering-the-shift-to-context-engineering — blog — Nearform blog on context engineering
[11]. **Chain of Thought PromptHub** — https://www.prompthub.us/blog/chain-of-thought-prompting-guide — guide — PromptHub CoT guide
[12]. **Chain-of-Thought Prompting** — https://www.promptingguide.ai/techniques/cot — Guide — Prompt Engineering Guide's CoT technique
[13]. **Chain-of-Thought Prompting** — https://learnprompting.org/docs/intermediate/chain_of_thought — Guide — Learn Prompting's CoT guide
[14]. **Chain-of-thought prompting 101** — https://www.k2view.com/blog/chain-of-thought-prompting/ — Blog — K2View's CoT introduction
[15]. **Chain-of-Thought Prompting Elicits Reasoning in Large Language Models** — https://arxiv.org/abs/2201.11903 — Paper — Original CoT research paper
[16]. **Chain-of-Thought Prompting: A Guide for LLM Applications and Agents** — https://www.comet.com/site/blog/chain-of-thought-prompting/ — Blog — Comet's CoT guide
[17]. **Chain-of-Thought Prompting: Helping LLMs Learn by Example** — https://deepgram.com/learn/chain-of-thought-prompting-guide — Guide — Deepgram's CoT guide
[18]. **Chain-of-Thought Prompting: Step-by-Step Reasoning with LLMs** — https://www.datacamp.com/tutorial/chain-of-thought-prompting — Guide — DataCamp's CoT tutorial
[19]. **Chain-of-Thought TechTarget** — https://www.techtarget.com/searchenterpriseai/definition/chain-of-thought-prompting — article — TechTarget CoT definition
[20]. **Complete Prompt Engineering Guide 2025** — https://aloaguilar20.medium.com/the-complete-prompt-engineering-guide-for-2025-mastering-cutting-edge-techniques-dfe0591b1d31 — guide — 2025 prompt engineering techniques
[21]. **Comprehensive Guide to Chain-of-Thought Prompting** — https://www.mercity.ai/blog-post/guide-to-chain-of-thought-prompting — Blog — Mercity's comprehensive CoT guide
[22]. **Context Engineering Guide** — https://www.promptingguide.ai/guides/context-engineering-guide — guide — Prompt Engineering Guide on context engineering
[23]. **Context engineering vs. prompt engineering** — https://www.elastic.co/search-labs/blog/context-engineering-vs-prompt-engineering — blog — Elastic blog on context vs prompt engineering
[24]. **Context Window DataCamp** — https://www.datacamp.com/blog/context-window — article — DataCamp context window guide
[25]. **CoT Prompting NVIDIA** — https://www.nvidia.com/en-us/glossary/cot-prompting/ — glossary — NVIDIA CoT glossary
[26]. **Effectively prompt Structured Output** — https://community.openai.com/t/how-to-effectively-prompt-for-structured-output/1355135 — community — OpenAI community structured output
[27]. **Few Shot Prompting Guide PromptHub** — https://www.prompthub.us/blog/the-few-shot-prompting-guide — guide — PromptHub few-shot guide
[28]. **Few Shot Prompting Performance** — https://www.cognativ.com/blogs/post/few-shot-prompting-improving-ai-model-performance/513 — article — Improving performance with few-shot
[29]. **Few-shot prompting Amazon Nova** — https://docs.aws.amazon.com/nova/latest/userguide/prompting-examples.html — doc — AWS Nova few-shot examples
[30]. **Few-Shot Prompting DataCamp** — https://www.datacamp.com/tutorial/few-shot-prompting — tutorial — DataCamp few-shot tutorial
[31]. **Few-Shot Prompting DigitalOcean** — https://www.digitalocean.com/community/tutorials/_few-shot-prompting-techniques-examples-best-practices — tutorial — DigitalOcean few-shot guide
[32]. **Few-Shot Prompting Guide** — https://www.promptingguide.ai/techniques/fewshot — guide — Few-shot prompting techniques
[33]. **Function Calling in AI Agents** — https://www.promptingguide.ai/agents/function-calling — guide — Prompt Engineering Guide on function calling
[34]. **General Tips for Designing Prompts** — https://www.promptingguide.ai/introduction/tips — guide — Prompt engineering guide tips section
[35]. **Guide For Meta Prompting** — https://www.godofprompt.ai/blog/guide-for-meta-prompting — guide — Meta-prompting guide
[36]. **HumanEval: Benchmark for Evaluating LLM Code Generation** — https://www.datacamp.com/tutorial/humaneval-benchmark-for-evaluating-llm-code-generation-capabilities — blog — DataCamp guide on HumanEval
[37]. **LLM Agents** — https://www.promptingguide.ai/research/llm-agents — Guide — Prompt Engineering Guide's LLM agents research
[38]. **Master Prompting Zero-Shot Few-Shot** — https://promptengineering.org/master-prompting-concepts-zero-shot-and-few-shot-prompting/ — guide — Mastering prompting concepts
[39]. **Meta Prompting GeeksforGeeks** — https://www.geeksforgeeks.org/artificial-intelligence/meta-prompting/ — article — GeeksforGeeks meta-prompting
[40]. **Meta Prompting Guide PromptHub** — https://www.prompthub.us/blog/a-complete-guide-to-meta-prompting — guide — PromptHub meta-prompting guide
[41]. **Meta Prompting IBM** — https://www.ibm.com/think/topics/meta-prompting — article — IBM meta-prompting overview
[42]. **Meta Prompting OpenAI Cookbook** — https://cookbook.openai.com/examples/enhance_your_prompts_with_meta_prompting — example — OpenAI meta-prompting examples
[43]. **Meta Prompting PromptingGuide** — https://www.promptingguide.ai/techniques/meta-prompting — guide — Meta-prompting techniques
[44]. **Meta-prompting GitHub** — https://github.com/meta-prompting/meta-prompting — repo — Meta-prompting repository
[45]. **Meta-Prompting prompts that write prompts** — https://medium.com/@AI_prompt_design/meta-prompting-ai-prompts-that-write-prompts-82b7e7ba563d — article — Meta-prompting deep dive
[46]. **Perfect JSON from AI** — https://genaiunplugged.substack.com/p/structured-outputs-json-prompts-guide — article — Structured outputs with JSON
[47]. **Prompt design strategies Gemini** — https://ai.google.dev/gemini-api/docs/prompting-strategies — doc — Google Gemini prompting strategies
[48]. **Prompt engineering** — https://en.wikipedia.org/wiki/Prompt_engineering — reference — Wikipedia entry on prompt engineering
[49]. **Prompt Engineering 2025 Trends** — https://profiletree.com/prompt-engineering-in-2025-trends-best-practices-profiletrees-expertise/ — article — 2025 trends and best practices
[50]. **Prompt engineering best practices 2025** — https://codesignal.com/blog/prompt-engineering-best-practices-2025/ — article — Latest best practices for prompt engineering
[51]. **Prompt Engineering Best Practices 2025** — https://garrettlanders.com/prompt-engineering-guide-2025/ — guide — 2025 best practices guide
[52]. **Prompt Engineering Best Practices: Tips, Tricks, and Tools** — https://www.digitalocean.com/resources/articles/prompt-engineering-best-practices — guide — DigitalOcean guide on prompt engineering
[53]. **Prompt Engineering Cheat Sheet for GPT-5** — https://www.freecodecamp.org/news/prompt-engineering-cheat-sheet-for-gpt-5/ — guide — FreeCodeCamp cheat sheet on prompt engineering
[54]. **Prompt Engineering Guide** — https://www.promptingguide.ai/ — resource — Comprehensive prompt engineering guide
[55]. **Prompt Engineering in 2025: Latest Best Practices** — https://www.news.aakashg.com/p/prompt-engineering — article — 2025 best practices
[56]. **Prompt Engineering Is Dead** — https://community.openai.com/t/prompt-engineering-is-dead-and-context-engineering-is-already-obsolete-why-the-future-is-automated-workflow-architecture-with-llms/1314011 — discussion — OpenAI community discussion on engineering evolution
[57]. **Prompt engineering patterns OpenAI** — https://community.openai.com/t/prompt-engineering-patterns/121040 — community — OpenAI community discussion on patterns
[58]. **Prompt Engineering Principles 2024** — https://www.prompthub.us/blog/prompt-engineering-principles-for-2024 — article — Core principles of prompt engineering
[59]. **Prompt Engineering Tools PromptLayer** — https://blog.promptlayer.com/top-5-prompt-engineering-tools-for-evaluating-prompts — article — Top prompt engineering tools
[60]. **Prompt engineering | OpenAI API** — https://platform.openai.com/docs/guides/prompt-engineering — doc — OpenAI API documentation on prompt engineering
[61]. **ReAct Prompting** — https://www.promptingguide.ai/techniques/react — Guide — Prompt Engineering Guide's ReAct technique
[62]. **Retrieval Augmented Generation (RAG)** — https://www.promptingguide.ai/techniques/rag — Guide — Prompt Engineering Guide's RAG technique
[63]. **Scalable Prompt Design Patterns** — https://latitude-blog.ghost.io/blog/5-patterns-for-scalable-prompt-design/ — article — Patterns for scalable prompt design
[64]. **Shot-Based Prompting LearnPrompting** — https://learnprompting.org/docs/basics/few_shot — guide — Shot-based prompting guide
[65]. **Structured output Amazon Nova** — https://docs.aws.amazon.com/nova/latest/userguide/prompting-structured-output.html — doc — AWS Nova structured output
[66]. **Structured outputs Gemini** — https://ai.google.dev/gemini-api/docs/structured-output — doc — Google Gemini structured output
[67]. **Structured outputs OpenAI** — https://developers.openai.com/api/docs/guides/structured-outputs/ — doc — OpenAI structured outputs
[68]. **Structured Outputs OpenAI Developer Guide** — https://medium.com/@piyushsonawane10/getting-structured-outputs-from-openai-models-a-developers-guide-3090e8120785 — article — Developer guide for structured outputs
[69]. **Structured Outputs Together.ai** — https://docs.together.ai/docs/json-mode — doc — Together.ai JSON mode
[70]. **Structured Prompting Guide** — https://www.cloudsquid.io/blog/structured-prompting — guide — Structured prompting techniques
[71]. **System Prompt Design** — https://fieldguidetoai.com/guides/system-prompt-design — guide — Guide to system prompt design
[72]. **System prompts collection** — https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools — repo — Collection of system prompts
[73]. **System Prompts Design Patterns** — https://tetrate.io/learn/ai/system-prompts-guide — guide — Design patterns for system prompts
[74]. **The New Skill in AI is Not Prompting, It's Context Engineering** — https://www.philschmid.de/context-engineering — blog — Philipp Schmid blog on context engineering
[75]. **The Ultimate Guide to Prompt Engineering** — https://www.lakera.ai/blog/prompt-engineering-guide — guide — Lakera comprehensive prompt engineering guide
[76]. **Top 7 Open-Source Tools for Prompt Engineering** — https://latitude-blog.ghost.io/blog/top-7-open-source-tools-for-prompt-engineering-in-2025 — blog — Latitude blog on open-source prompt tools
[77]. **Tree of Thoughts (ToT)** — https://www.promptingguide.ai/techniques/tot — Guide — Prompt Engineering Guide's ToT technique
[78]. **Ultimate Guide to Prompt Engineering in 2025** — https://medium.com/@generativeai.saif/the-ultimate-guide-to-prompt-engineering-in-2025-mastering-llm-interactions-8b88c5cf65b6 — guide — LLM interaction techniques
[79]. **Vanderbilt Prompt Patterns** — https://www.vanderbilt.edu/generative-ai/prompt-patterns/ — guide — Vanderbilt AI prompt patterns
[80]. **What is chain of thought (CoT) prompting** — https://www.ibm.com/think/topics/chain-of-thoughts — Blog — IBM's CoT explanation
[81]. **Zero-Shot One-Shot Few-Shot Codecademy** — https://www.codecademy.com/article/prompt-engineering-101-understanding-zero-shot-one-shot-and-few-shot — article — Zero/one/few-shot comparison
[82]. **Zero-Shot vs Few-Shot Shelf** — https://shelf.io/blog/zero-shot-and-few-shot-prompting/ — article — Zero-shot vs few-shot comparison

### A4. Context Engineering & Management

[1]. **An Exploratory Study of Code Retrieval** — https://www.preprints.org/manuscript/202510.0924/v1/download — academic — Preprints paper on code retrieval
[2]. **Build an AI prompt library in 5 steps** — https://www.ragan.com/build-an-ai-prompt-library-in-5-steps/ — guide — Ragan guide to building prompt libraries
[3]. **Building a Codebase Exploration Tool with RAG** — https://www.chitika.com/rag-codebase-exploration/ — blog — Chitika guide on codebase exploration
[4]. **Chunking and Context Windows** — https://www.typedef.ai/resources/tackle-chunking-context-windows-llm-data-pipelines — guide — Chunking for context windows
[5]. **code-graph-rag GitHub repository** — https://github.com/vitali87/code-graph-rag — repo — Code graph RAG for monorepos
[6]. **CodeRAG-Bench** — https://code-rag-bench.github.io/ — resource — Benchmarking tool for code RAG systems
[7]. **Context Engineering - Short-Term Memory Management with Sessions** — https://cookbook.openai.com/examples/agents_sdk/session_memory — Guide — OpenAI's memory management guide
[8]. **Context Engineering for Personalization** — https://developers.openai.com/cookbook/examples/agents_sdk/context_personalization/ — Guide — OpenAI's context engineering guide
[9]. **Context Engineering: Bringing Engineering Discipline to Prompts** — https://addyo.substack.com/p/context-engineering-bringing-engineering — blog — Addyo substack on context engineering
[10]. **Context Engineering: Foundations, Categories, and Techniques** — https://www.dailydoseofds.com/llmops-crash-course-part-5/ — blog — Daily Dose of DS blog on context engineering
[11]. **Context Length Guide 2025** — https://local-ai-zone.github.io/guides/context-length-optimization-ultimate-guide-2025.html — guide — Local AI Zone ultimate guide on context optimization
[12]. **Context Management and Memory Systems** — https://medium.com/@omark.k.aly/context-management-and-memory-systems-building-ai-that-remembers-f4c8a7abe882 — blog — Medium article on AI memory systems
[13]. **Context Window Management** — https://oneuptime.com/blog/post/2026-01-30-context-window-management/view — article — Context window management strategies
[14]. **Context Window Overflow** — https://redis.io/blog/context-window-overflow/ — article — Managing context window overflow
[15]. **Context-aware code generation: RAG and Vertex AI Codey APIs** — https://cloud.google.com/blog/products/ai-machine-learning/context-aware-code-generation-rag-and-vertex-ai-codey-apis — blog — Google Cloud blog on context-aware generation
[16]. **Guide to LLM Context Window** — https://prudentpartners.in/llm-context-window/ — guide — Understanding LLM context windows
[17]. **How to Build Custom Code RAG | Continue Docs** — https://docs.continue.dev/guides/custom-code-rag — doc — Continue guide on custom code RAG
[18]. **JetBrains Context Management** — https://blog.jetbrains.com/research/2025/12/efficient-context-management/ — article — Efficient context management
[19]. **Leveraging Generative AI for Enhancing Domain-Driven Software Design** — https://arxiv.org/pdf/2601.20909 — academic — ArXiv paper on DDD with GenAI
[20]. **LLM Context Management** — https://eval.16x.engineer/blog/llm-context-management-guide — guide — 16x engineer guide on context management
[21]. **LLM Context Management Strategies** — https://fast.io/resources/llm-context-management-strategies/ — guide — Strategic context management
[22]. **LLM Context Window Explanation** — https://medium.com/@tahirbalarabe2/what-is-llms-context-window-understanding-and-working-with-the-context-window-641b6d4f811f — article — Understanding context windows
[23]. **llm-context-limits GitHub repository** — https://github.com/taylorwilsdon/llm-context-limits — repo — Repository tracking context window limits
[24]. **LLMs with largest context windows** — https://codingscape.com/blog/llms-with-largest-context-windows — reference — Codingscape comparison of context windows
[25]. **Long Context Windows in Generative AI** — https://www.emerge.haus/blog/long-context-windows-in-generative-ai — blog — Emerge Haus blog on context windows
[26]. **Optimize your prompt size for long context window LLMs** — https://medium.com/google-cloud/optimize-your-prompt-size-for-long-context-window-llms-0a5c2bab4a0f — blog — Google Cloud Medium article on prompt optimization
[27]. **RAG architecture with Voyage AI embedding models** — https://aws.amazon.com/blogs/machine-learning/rag-architecture-with-voyage-ai-embedding-models-on-amazon-sagemaker-jumpstart-and-anthropic-claude-3-models/ — blog — RAG architecture using Voyage embeddings
[28]. **RAG for a Codebase with 10k Repos** — https://www.qodo.ai/blog/rag-for-large-scale-code-repos/ — blog — Qodo guide on codebase RAG
[29]. **Retrieval Augmented Generation (RAG) and Semantic Search for GPTs** — https://help.openai.com/en/articles/8868588-retrieval-augmented-generation-rag-and-semantic-search-for-gpts — Doc — OpenAI's RAG documentation
[30]. **Retrieval Augmented Generation (RAG) in Azure AI Search** — https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview — Doc — Microsoft's RAG documentation
[31]. **Retrieval-Augmented Generation (RAG)** — https://www.pinecone.io/learn/retrieval-augmented-generation/ — Guide — Pinecone's RAG learning guide
[32]. **Retrieval-augmented generation - Wikipedia** — https://en.wikipedia.org/wiki/Retrieval-augmented-generation — Blog — Wikipedia's RAG article
[33]. **Unlocking Full-Context AI Coding: RAG** — https://medium.com/@neverdecel/unlocking-full-context-ai-coding-real-time-codebase-assistance-with-rag-8ee8295fea5d — blog — Medium article on full-context RAG
[34]. **What is a context window?** — https://www.ibm.com/think/topics/context-window — guide — IBM guide on context windows
[35]. **What is RAG? - Retrieval-Augmented Generation AI Explained** — https://aws.amazon.com/what-is/retrieval-augmented-generation/ — Guide — AWS's RAG explanation
[36]. **What is retrieval-augmented generation (RAG)** — https://github.com/resources/articles/software-development-with-retrieval-augmentation-generation-rag — Blog — GitHub's RAG article
[37]. **What Is Retrieval-Augmented Generation (RAG)** — https://www.salesforce.com/agentforce/what-is-rag/ — Blog — Salesforce's RAG explanation
[38]. **What Is Retrieval-Augmented Generation aka RAG** — https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/ — Blog — NVIDIA's RAG explanation

### A5. MCP (Model Context Protocol)

[1]. **3 steps to build an MCP server from scratch** — https://www.merge.dev/blog/how-to-build-mcp-server — Blog — Merge's quick MCP server building guide
[2]. **Add and manage MCP servers in VS Code** — https://code.visualstudio.com/docs/copilot/customization/mcp-servers — Doc — VS Code's official MCP server configuration
[3]. **AI SDK Core: Model Context Protocol (MCP)** — https://ai-sdk.dev/docs/ai-sdk-core/mcp-tools — doc — Vercel AI SDK documentation on MCP
[4]. **Build an MCP server - Model Context Protocol** — https://modelcontextprotocol.io/docs/develop/build-server — Doc — Official MCP server development guide
[5]. **Build an MCP Server: Complete MCP Tutorial for Beginners** — https://www.codecademy.com/article/build-an-mcp-server — Guide — Codecademy's complete MCP server tutorial
[6]. **Building MCP Servers: Part 1 - Getting Started with Resources** — https://medium.com/@cstroliadavis/building-mcp-servers-536969d27809 — Blog — Medium article on MCP server development
[7]. **Building Your First MCP Server: A Beginners Tutorial** — https://dev.to/debs_obrien/building-your-first-mcp-server-a-beginners-tutorial-5fag — Blog — DEV Community beginner's MCP tutorial
[8]. **Connect to local MCP servers - Model Context Protocol** — https://modelcontextprotocol.io/docs/develop/connect-local-servers — doc — Official MCP documentation on local server connections
[9]. **Decoding the Discourse MCP Server: A Guide for AI Engineers** — https://skywork.ai/skypage/en/decoding-discourse-mcp-server/1981181836639784960 — guide — Guide to Discourse MCP integration
[10]. **Discourse MCP is here** — https://blog.discourse.org/2025/10/discourse-mcp-is-here/ — blog — Discourse integration with MCP announcement
[11]. **Dynamic Tool Discovery: Azure AI Agent Service + MCP** — https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/dynamic-tool-discovery-azure-ai-agent-service--mcp-server-integration/4412651 — blog — Microsoft blog on dynamic tool discovery
[12]. **GitHub - CoplayDev/unity-mcp: Unity MCP** — https://github.com/CoplayDev/unity-mcp — Repo — Unity MCP bridge repository
[13]. **GitHub - modelcontextprotocol/modelcontextprotocol** — https://github.com/modelcontextprotocol/modelcontextprotocol — Repo — Official Model Context Protocol specification and documentation repository
[14]. **GitHub - punkpeye/scraperis-mcp** — https://github.com/punkpeye/scraperis-mcp — repo — MCP for web scraping
[15]. **GitHub Copilot Added MCP. Now Your Security Team Has Questions** — https://www.scalekit.com/blog/github-copilot-mcp-enterprise-security-governance — blog — Scalekit blog on Copilot security governance
[16]. **GitHub copilot security risks: what enterprises need to know** — https://www.mintmcp.com/blog/github-copilot-security-risks — blog — MintMCP blog on Copilot security
[17]. **How I Connected My AI Agent to Any API With MCP** — https://dzone.com/articles/ai-agents-api-integration-with-mcp — Blog — DZone's MCP API integration guide
[18]. **How to Build Your Own MCP Server** — https://www.builder.io/blog/mcp-server — Blog — Builder.io's MCP server development tutorial
[19]. **How to Build Your Own MCP Server with Python** — https://www.freecodecamp.org/news/how-to-build-your-own-mcp-server-with-python/ — Guide — FreeCodeCamp's Python MCP server guide
[20]. **How to Set Up Model Context Protocol (MCP) in Continue** — https://docs.continue.dev/customize/deep-dives/mcp — doc — Continue guide for MCP setup
[21]. **MCP server: A step-by-step guide to building from scratch - Composio** — https://composio.dev/blog/mcp-server-step-by-step-guide-to-building-from-scrtch — Blog — Composio's comprehensive MCP server building guide
[22]. **Model context protocol (MCP) - OpenAI Agents SDK** — https://openai.github.io/openai-agents-python/mcp/ — doc — OpenAI documentation on MCP
[23]. **Model Context Protocol - Wikipedia** — https://en.wikipedia.org/wiki/Model_Context_Protocol — reference — Wikipedia entry on MCP
[24]. **Model Context Protocol · GitHub** — https://github.com/modelcontextprotocol — repo — Official Model Context Protocol repository
[25]. **Quickstart - Create a minimal MCP server with .NET** — https://learn.microsoft.com/en-us/dotnet/ai/quickstarts/build-mcp-server — Doc — Microsoft Learn's .NET MCP server quickstart
[26]. **Specification - Model Context Protocol** — https://modelcontextprotocol.io/specification/2025-11-25 — Doc — Official MCP specification document
[27]. **Tools - Model Context Protocol** — https://modelcontextprotocol.io/specification/2025-06-18/server/tools — doc — MCP specification on tools
[28]. **Understanding MCP Servers Across Different Platforms** — https://dev.to/darkmavis1980/understanding-mcp-servers-across-different-platforms-claude-desktop-vs-vs-code-vs-cursor-4opk — Blog — Comparison of MCP across platforms
[29]. **What is Model Context Protocol (MCP)? A guide** — https://cloud.google.com/discover/what-is-model-context-protocol — guide — Google Cloud guide to MCP
[30]. **What Is the Model Context Protocol (MCP) and How It Works** — https://www.descope.com/learn/post/mcp — guide — Comprehensive guide explaining MCP architecture and functionality
[31]. **Your MCP Client Just Got Superpowers: Arcade Tools** — https://dev.to/avoguru/your-mcp-client-just-got-superpowers-arcade-tools-are-now-in-cursor-vs-code-and-more-3pjj — Blog — DEV Community's Arcade Tools article

### A6. Agentic AI & Agent Frameworks

[1]. **10 AI agent benchmarks** — https://www.evidentlyai.com/blog/ai-agent-benchmarks — Blog — Evidently AI's benchmark overview
[2]. **10 best AI workflow automation tools** — https://www.gumloop.com/blog/best-ai-workflow-automation-tools — blog — Gumloop guide to workflow automation tools
[3]. **11 Best AI Workflow Automation Tools for 2026** — https://slack.com/blog/productivity/9-best-ai-automation-tools-to-automate-tasks-and-streamline-workflows — blog — Slack guide to automation tools
[4]. **4 Agentic AI Design Patterns & Real-World Examples** — https://research.aimultiple.com/agentic-ai-design-patterns/ — Blog — AIM's agentic design patterns with examples
[5]. **4 Agentic AI Design Patterns to Build Intelligent Workflows** — https://www.projectpro.io/article/agentic-ai-design-patterns/1126 — Guide — ProjectPro's agentic design patterns guide
[6]. **5 approaches to building LLM agents** — https://tray.ai/resources/blog/5-approaches-to-building-llm-powered-agents — Blog — Tray's LLM agents guide
[7]. **7 Must-Know Agentic AI Design Patterns** — https://machinelearningmastery.com/7-must-know-agentic-ai-design-patterns/ — Blog — Machine Learning Mastery's agentic design patterns guide
[8]. **[2210.03629] ReAct: Synergizing Reasoning and Acting in Language Models** — https://arxiv.org/abs/2210.03629 — Paper — Original ReAct research paper on arxiv
[9]. **A Practical Guide for Designing, Developing, and Deploying Production-Grade Agentic AI Workflows** — https://arxiv.org/html/2512.08769v1 — Paper — Production-grade agentic workflows guide
[10]. **A practical guide to building agents** — https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf — Guide — OpenAI's agent building guide
[11]. **A practical guide to building agents** — https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/ — Guide — OpenAI's practical agent building guide
[12]. **A Streamlined Framework for Enhancing LLM Reasoning** — https://aclanthology.org/2025.acl-long.1383.pdf — Paper — ACL's LLM reasoning framework
[13]. **Adding Guardrails for AI Agents: Policy and Configuration Guide** — https://www.reco.ai/hub/guardrails-for-ai-agents — Guide — Reco's guardrails policy guide
[14]. **Advanced AI Workflow Automation Software & Tools - n8n** — https://n8n.io/ai/ — Doc — n8n's AI capabilities overview
[15]. **Agent and Multi-Agent Applications - AutoGen** — https://microsoft.github.io/autogen/stable//user-guide/core-user-guide/core-concepts/agent-and-multi-agent-application.html — Doc — AutoGen's agent applications documentation
[16]. **Agent Architectures: ReAct, Self-Ask, Plan-and-Execute** — https://apxml.com/courses/langchain-production-llm/chapter-2-sophisticated-agents-tools/agent-architectures — Course — LangChain production course on agent architectures
[17]. **Agent design patterns** — https://rlancemartin.github.io/2026/01/09/agent_design/ — Blog — R. Lance Martin's agent design patterns
[18]. **Agent Evaluation: Framework for Testing AI Agents** — https://langwatch.ai/blog/framework-for-evaluating-agents — Blog — LangWatch's agent evaluation framework
[19]. **Agent Evaluation: How to Test and Measure Agentic AI Performance** — https://machinelearningmastery.com/agent-evaluation-how-to-test-and-measure-agentic-ai-performance/ — Guide — Machine Learning Mastery's agent evaluation guide
[20]. **Agent Factory: The new era of agentic AI** — https://azure.microsoft.com/en-us/blog/agent-factory-the-new-era-of-agentic-ai-common-use-cases-and-design-patterns/ — Blog — Microsoft Azure's guide to agentic AI patterns
[21]. **Agent Frameworks vs Runtime vs Harnesses: What They Are** — https://www.analyticsvidhya.com/blog/2025/12/agent-frameworks-vs-runtimes-vs-harnesses/ — Blog — Analytics Vidhya's frameworks comparison
[22]. **Agent Management Interface Patterns** — https://www.lukew.com/ff/entry.asp?2106= — Blog — Luke W's agent interface patterns
[23]. **Agent READMEs: An Empirical Study of Context Files for Agentic Coding** — https://arxiv.org/html/2511.12884v1 — academic — ArXiv empirical study on context files
[24]. **Agent Retry Strategies** — https://docs.praison.ai/docs/best-practices/agent-retry-strategies — Doc — PraisonAI's retry strategies documentation
[25]. **Agent system design patterns** — https://docs.databricks.com/aws/en/generative-ai/guide/agent-system-design-patterns — Doc — Databricks' agent design patterns
[26]. **Agent: Function calling** — https://docs.bentoml.com/en/latest/examples/function-calling.html — doc — BentoML documentation on function calling
[27]. **Agentic AI API: Effective Integration Patterns** — https://addepto.com/blog/agentic-ai-api-how-to-make-your-ai-agent-talk-to-other-software-integration-patterns-that-work/ — Blog — Addepto's API integration patterns
[28]. **Agentic AI Design Patterns: Complete Implementation Guide** — https://www.aufaitux.com/blog/agentic-ai-design-patterns-guide/ — Guide — Au Fait UX's design patterns guide
[29]. **Agentic AI from First Principles: Reflection** — https://towardsdatascience.com/agentic-ai-from-first-principles-reflection/ — Blog — Towards Data Science's article on agentic reflection
[30]. **Agentic AI systems don't fail suddenly - they drift over time** — https://www.cio.com/article/4134051/agentic-ai-systems-dont-fail-suddenly-they-drift-over-time.html — Blog — CIO's article on agent drift
[31]. **Agentic AI Workflows: Why Orchestration with Temporal is Key** — https://intuitionlabs.ai/articles/agentic-ai-temporal-orchestration — Blog — Intuition Labs' Temporal orchestration guide
[32]. **Agentic AI, explained** — https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained — Blog — MIT Sloan's agentic AI explanation
[33]. **Agentic Design Patterns. From reflection to collaboration** — https://medium.com/@bijit211987/agentic-design-patterns-cbd0aae2962f — Blog — Medium's comprehensive agentic design patterns article
[34]. **Agentic Reasoning Patterns: 5 Powerful Frameworks for Smarter AI Agents** — https://servicesground.com/blog/agentic-reasoning-patterns/ — Blog — ServicesGround's agentic reasoning patterns guide
[35]. **Agentic Tool Calling Explained: How AI Agents Actually Think** — https://www.gauraw.com/agentic-tool-calling-explained-how-ai-agents-actually-think/ — Blog — Kumar Gauraw's tool calling explanation
[36]. **Agentic workflows for software development** — https://medium.com/quantumblack/agentic-workflows-for-software-development-dc8e64f4a79d — Blog — QuantumBlack's software development workflows
[37]. **Agentic Workflows Replace GitHub Actions for Repository Automations** — https://www.geeky-gadgets.com/agentic-workflow-permissions/ — Blog — Geeky Gadgets' agentic workflows article
[38]. **Agentic Workflows: Everything You Need to Know** — https://www.automationanywhere.com/rpa/agentic-workflows — Guide — Automation Anywhere's workflows guide
[39]. **Agentified Agent Assessment (AAA) & AgentBeats** — https://docs.agentbeats.org/ — Doc — AgentBeats documentation
[40]. **Agents and Ensemble Reasoning** — https://blog.vital.ai/2025/01/13/agents-and-ensemble-reasoning/comment-page-1/ — Blog — Vital AI's ensemble reasoning article
[41]. **Agents SDK** — https://developers.openai.com/api/docs/guides/agents-sdk — Doc — OpenAI Agents SDK documentation
[42]. **Agents with Human in the Loop: Everything You Need to Know** — https://dev.to/camelai/agents-with-human-in-the-loop-everything-you-need-to-know-3fo5 — Blog — DEV Community's HITL guide
[43]. **AgentWorkflow Guide: Build AI Agent Systems** — https://www.llamaindex.ai/blog/introducing-agentworkflow-a-powerful-system-for-building-ai-agent-systems — Blog — LlamaIndex's AgentWorkflow guide
[44]. **AI Agent Design Best Practices You Can Use Today** — https://hatchworks.com/blog/ai-agents/ai-agent-design-best-practices/ — Blog — Hatchworks' agent design best practices
[45]. **AI Agent Design Patterns: How to Build Reliable AI Agent Architecture** — https://www.comet.com/site/blog/ai-agent-design/ — Blog — Comet's AI agent design guide
[46]. **AI agent evaluation: A practical framework for testing multi-step agents** — https://www.braintrust.dev/articles/ai-agent-evaluation-framework — Blog — Braintrust's agent evaluation framework
[47]. **AI agent evaluation: comprehensive framework** — https://www.lxt.ai/blog/ai-agent-evaluation/ — Blog — LXT's agent evaluation framework
[48]. **AI agent evaluation: Metrics, strategies, and best practices** — https://wandb.ai/onlineinference/genai-research/reports/AI-agent-evaluation-Metrics-strategies-and-best-practices--VmlldzoxMjM0NjQzMQ — Blog — Weights & Biases' agent evaluation report
[49]. **AI Agent Evaluation: The Definitive Guide** — https://www.confident-ai.com/blog/definitive-ai-agent-evaluation-guide — Guide — Confident AI's agent evaluation guide
[50]. **AI Agent integrations | Workflow automation with n8n** — https://n8n.io/integrations/agent/ — Doc — n8n's agent integrations
[51]. **AI Agent Metrics: How Elite Teams Evaluate** — https://galileo.ai/blog/ai-agent-metrics — Blog — Galileo's agent metrics guide
[52]. **AI Agent Observability, Tracing & Evaluation with Langfuse** — https://langfuse.com/blog/2024-07-ai-agent-observability-with-langfuse — Blog — Langfuse's observability guide
[53]. **AI Agent Routing: Best Practices** — https://www.patronus.ai/ai-agent-development/ai-agent-routing — Guide — Patronus' agent routing guide
[54]. **AI Agent Routing: Tutorial & Examples** — https://fme.safe.com/guides/ai-agent-architecture/ai-agent-routing/ — Guide — Safe Software's routing guide
[55]. **AI Agent Tutorial 3: Tool Calling** — https://medium.com/@xzw0005/ai-agent-tutorial-3-tool-calling-b46d02d63eb6 — Blog — Medium's tool calling tutorial
[56]. **AI Agent Workflow Design Patterns - An Overview** — https://medium.com/binome/ai-agent-workflow-design-patterns-an-overview-cf9e1f609696 — Blog — Medium's workflow design patterns
[57]. **AI agentic workflows: a practical guide for n8n automation** — https://blog.n8n.io/ai-agentic-workflows/ — Blog — n8n's agentic workflows guide
[58]. **AI agents and tool calling: a complete technical guide** — https://spartner.software/kennisbank/ai-agents-tool-calling — guide — Spartner technical guide on tool calling
[59]. **AI Agents Design Patterns Explained** — https://medium.com/@aydinKerem/ai-agents-design-patterns-explained-b3ac0433c915 — Blog — Medium's AI agent design patterns article
[60]. **AI Agents Discovery with Lasso & CrowdStrike Falcon** — https://www.lasso.security/blog/ai-agents-discovery-lasso-crowdstrike-falcon — blog — Lasso blog on AI agent discovery
[61]. **AI Agents Need an Inference-Bearing Knowledge Graph** — https://squirro.com/squirro-blog/ai-agents-inference-knowledge-graphs — Blog — Squirro's knowledge graph article
[62]. **AI Agents With Human In The Loop** — https://cobusgreyling.medium.com/ai-agents-with-human-in-the-loop-f910d0c0384b — Blog — Medium's HITL agents article
[63]. **AI Agents | Stately** — https://stately.ai/docs/agents — Doc — Stately's AI agents documentation
[64]. **AI Coding Agents & IDEs (36 Tools)** — https://medium.com/@srini.hebbar/ai-coding-agents-ides-36-tools-3a9b3e7c1638 — blog — Medium article on AI coding agents
[65]. **AI Function Calling in 2025: Build Agents That Actually Work** — https://www.kidsil.net/2025/07/ai-function-calling/ — Blog — Comprehensive AI function calling guide
[66]. **AI Guardrails in Agentic Systems Explained** — https://www.altexsoft.com/blog/ai-guardrails/ — Blog — AltexSoft's guardrails guide
[67]. **AI Pair Programming Best Practices** — https://www.madebyagents.com/blog/ai-pair-programming-best-practices — blog — Made by Agents guide on pair programming best practices
[68]. **AI Token Counter & Cost Calculator** — https://agentdock.ai/tools/token-counter — Tool — AgentDock's token counter tool
[69]. **AI Workflow Automation Platform & Tools - n8n** — https://n8n.io/ — Doc — n8n homepage
[70]. **AI Workflow Automation Software & Tools | Make** — https://www.make.com/en — tool — Make.com automation platform
[71]. **AI workflow orchestration with state machines** — https://docs.spryker.com/docs/dg/dev/ai/ai-foundation/ai-foundation-workflow-state-machine.html — Doc — Spryker's state machine documentation
[72]. **AI-Assisted Domain-Driven Design** — https://agentic-design.ai/ai-driven-dev/ddd-with-ai — guide — Agentic Design guide on DDD with AI
[73]. **AI-powered code review with linting** — https://n8n.io/workflows/10034-ai-powered-code-review-with-linting-red-marked-corrections-in-google-sheets-and-slack/ — workflow — n8n workflow template for AI code review
[74]. **Alibaba releases Qwen with Questions, an open reasoning model** — https://venturebeat.com/ai/alibaba-releases-qwen-with-questions-an-open-reasoning-model-that-beats-o1-preview/ — Blog — VentureBeat's QwQ article
[75]. **Amazon Bedrock AgentCore Memory: Building context-aware agents** — https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-memory-building-context-aware-agents/ — Blog — AWS's agent memory guide
[76]. **An Introduction to CrewAI: A Multi-Agent Orchestration Framework** — https://mgx.dev/insights/an-introduction-to-crewai-a-multi-agent-orchestration-framework/dda4dd3c606c4241a282d8c76cadd23a — Blog — MGX's CrewAI introduction
[77]. **APIs for AI Agents: The 5 Integration Patterns** — https://composio.dev/blog/apis-ai-agents-integration-patterns — Blog — Composio's API integration patterns
[78]. **Architect's Guide to Agentic Design Patterns** — https://medium.com/@sunilraopalkar/architects-guide-to-agentic-design-patterns-the-next-10-patterns-for-production-ai-9ed0b0f5a5c3 — Blog — Medium's architectural agentic patterns
[79]. **atomic-agents GitHub repository** — https://github.com/BrainBlend-AI/atomic-agents — repo — Atomic agents for building AI agents
[80]. **AutoGen to Microsoft Agent Framework Migration Guide** — https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen/ — Guide — Migration guide from AutoGen to Agent Framework
[81]. **AutoGen: An Agentic Open-Source Framework for Intelligent Automation** — https://medium.com/@shravankoninti/autogen-an-agentic-open-source-framework-for-intelligent-automation-d1c374c46bbb — Blog — Medium's AutoGen overview
[82]. **Automate repository tasks with GitHub Agentic Workflows** — https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/ — Blog — GitHub's agentic workflows announcement
[83]. **Best AI agent integration platforms to consider in 2026** — https://nango.dev/blog/best-ai-agent-integration-platforms — Blog — Nango's integration platforms guide
[84]. **Best AI Coding Agents Summer 2025** — https://martinterhaak.medium.com/best-ai-coding-agents-summer-2025-c4d20cd0c846 — blog — Martin ter Haak blog on coding agents
[85]. **Best AI Workflow Automation Tools (2025)** — https://www.whalesync.com/blog/best-ai-workflow-automation-tools-2025 — blog — Whalesync guide to automation tools
[86]. **Best Practices for Building an Agent Router** — https://arize.com/blog/best-practices-for-building-an-ai-agent-router/ — Blog — Arize's agent router best practices
[87]. **Bridging Minds and Machines: Agents with Human-in-the-Loop** — https://www.camel-ai.org/blogs/human-in-the-loop-ai-camel-integration — Blog — Camel AI's HITL integration guide
[88]. **Build a RAG agent with LangChain** — https://docs.langchain.com/oss/python/langchain/rag — Doc — LangChain's RAG agent documentation
[89]. **Build AI agents with the Mistral Agents API** — https://mistral.ai/news/agents-api — Blog — Mistral's agents API announcement
[90]. **Build Custom AI Agents With Logic & Control** — https://n8n.io/ai-agents/ — Doc — n8n's custom agents documentation
[91]. **Build Multimodal Visual AI Agents Powered by NVIDIA NIM** — https://developer.nvidia.com/blog/build-multimodal-visual-ai-agents-powered-by-nvidia-nim/ — Blog — NVIDIA Developer's multimodal agents guide
[92]. **Build Powerful AI Agents With MindStudio** — https://www.mindstudio.ai — Doc — MindStudio platform
[93]. **Build your first AI agent | n8n workflow template** — https://n8n.io/workflows/6270-build-your-first-ai-agent/ — Guide — n8n's first AI agent template
[94]. **Building a multi agent system using CrewAI** — https://medium.com/pythoneers/building-a-multi-agent-system-using-crewai-a7305450253e — Blog — Medium's CrewAI tutorial
[95]. **Building Agentic Workflows with Inngest** — https://weaviate.io/blog/inngest-ai-workflows — Blog — Weaviate's Inngest agents guide
[96]. **Building AI Agents with Knowledge Graphs vs. Retrieval Augmented Generation** — https://medium.com/@senpubali7/building-ai-agents-with-knowledge-graphs-vs-retrieval-augmented-generation-a2730ec1915a — Blog — Medium's knowledge graph vs RAG article
[97]. **Building an Architecture Decision Record Writer Agent** — https://piethein.medium.com/building-an-architecture-decision-record-writer-agent-a74f8f739271 — blog — Medium article on ADR writer agents
[98]. **Building and evaluating alignment auditing agents** — https://alignment.anthropic.com/2025/automated-auditing/ — blog — Alignment auditing methodology
[99]. **Building Effective Agents :: Spring AI Reference** — https://docs.spring.io/spring-ai/reference/api/effective-agents.html — Doc — Spring AI's effective agents documentation
[100]. **Building LangGraph: Designing an Agent Runtime from first principles** — https://blog.langchain.com/building-langgraph/ — Blog — Technical deep dive on LangGraph design
[101]. **Building Self-Evolving Knowledge Graphs Using Agentic Systems** — https://medium.com/@community_md101/building-self-evolving-knowledge-graphs-using-agentic-systems-48183533592c — Blog — Medium's self-evolving knowledge graphs article
[102]. **Building smarter AI agents: AgentCore long-term memory deep dive** — https://aws.amazon.com/blogs/machine-learning/building-smarter-ai-agents-agentcore-long-term-memory-deep-dive/ — Blog — AWS's long-term memory guide
[103]. **Choose a design pattern for your agentic AI system** — https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system — Doc — Google Cloud's agentic design pattern guide
[104]. **Cline GitHub repository** — https://github.com/cline/cline — repo — Official Cline autonomous coding agent repository
[105]. **Coding Guidelines for Your AI Agents** — https://blog.jetbrains.com/idea/2025/05/coding-guidelines-for-your-ai-agents/ — blog — JetBrains blog on AI agent coding guidelines
[106]. **ContentBot - AI Content Automation and Workflows** — https://contentbot.ai/ — tool — ContentBot AI content creation tool
[107]. **Context Engineering - LLM Memory and Retrieval for AI Agents** — https://weaviate.io/blog/context-engineering — Blog — Weaviate's context engineering guide
[108]. **Context Window Management: Strategies for Long-Context AI Agents** — https://www.getmaxim.ai/articles/context-window-management-strategies-for-long-context-ai-agents-and-chatbots/ — guide — Maxim guide on context management
[109]. **CrewAI - AWS Prescriptive Guidance** — https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/crewai.html — Doc — AWS's CrewAI guide
[110]. **CrewAI: A Practical Guide to Role-Based Agent Orchestration** — https://www.digitalocean.com/community/tutorials/crewai-crash-course-role-based-agent-orchestration — Guide — DigitalOcean's CrewAI tutorial
[111]. **DataJoint Launches Agentic AI Control Layer for Scientific Workflows** — https://www.prnewswire.com/news-releases/datajoint-launches-agentic-ai-control-layer-for-scientific-workflows-enabling-defensible-and-reproducible-ai-in-regulated-rd-302697535.html — Blog — DataJoint's agentic control layer announcement
[112]. **Definitive Guide to Agentic Frameworks in 2026** — https://blog.softmaxdata.com/definitive-guide-to-agentic-frameworks-in-2026-langgraph-crewai-ag2-openai-and-more — Blog — SoftMax Data's comprehensive frameworks guide
[113]. **Designing a State-of-the-Art Multi-Agent System** — https://polarixdata.com/en/blog/designing-a-state-of-the-art-multi-agent-system/ — Blog — Polarix's multi-agent system design guide
[114]. **Designing a Tool Architecture for AI Agents - Dynamic Routing** — https://dev.to/kim_namhyun_e7535f3dc4c69/designing-a-tool-architecture-for-ai-agents-base-tools-toolkits-and-dynamic-routing-fdo — Blog — DEV Community's dynamic routing guide
[115]. **Designing Agentic AI Architectures: Core Patterns and Principles** — https://www.gocodeo.com/post/designing-agentic-ai-architectures-core-patterns-and-principles — Blog — Codeo's agentic architecture guide
[116]. **Designing Agentic AI Workflows: Six Steps for Enterprise-Ready Deployments** — https://www.faktion.com/post/designing-agentic-ai-workflows-our-insights-for-each-of-the-6-steps — Blog — Faktion's deployment guide
[117]. **Designing User Interfaces for Agentic AI** — https://codewave.com/insights/designing-agentic-ai-ui/ — Guide — Codewave's agentic AI UI design guide
[118]. **Discover 5773 AI Automation Workflows from the n8n Community** — https://n8n.io/workflows/categories/ai/ — Doc — n8n's AI workflows community collection
[119]. **Durable multi-agentic AI architecture with Temporal** — https://temporal.io/blog/using-multi-agent-architectures-with-temporal — Blog — Temporal's multi-agent architecture guide
[120]. **Enhance Your AI Coding Agent | Nx** — https://nx.dev/docs/features/enhance-ai — doc — Nx documentation on AI enhancement
[121]. **Error Handling in Agentic Systems: Retries, Rollbacks, and Graceful Failure** — https://agentsarcade.com/blog/error-handling-agentic-systems-retries-rollbacks-graceful-failure — Blog — Agents Arcade's error handling guide
[122]. **Error Recovery and Fallback Strategies in AI Agent Development** — https://www.gocodeo.com/post/error-recovery-and-fallback-strategies-in-ai-agent-development — Blog — Codeo's error recovery guide
[123]. **ESCARGOT: an AI agent leveraging large language models, dynamic graph of thoughts** — https://academic.oup.com/bioinformatics/article/41/2/btaf031/7972741 — Paper — ESCARGOT knowledge graph agent paper
[124]. **Evaluating AI Agents in 2025: A Practical Guide** — https://www.turingcollege.com/blog/evaluating-ai-agents-practical-guide — Guide — Turing College's agent evaluation guide
[125]. **Evaluating AI agents: Real-world lessons from building agentic systems at Amazon** — https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/ — Blog — AWS's agent evaluation guide
[126]. **Evaluation and Benchmarking of LLM Agents: A Survey** — https://arxiv.org/html/2507.21504v1 — Paper — Comprehensive LLM agents evaluation survey
[127]. **Everything You Need to Know About Reasoning Models** — https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/everything-you-need-to-know-about-reasoning-models-o1-o3-o4-mini-and-beyond/4406846 — Blog — Microsoft's reasoning models guide
[128]. **Exploring Effective Testing Frameworks for AI Agents** — https://www.getmaxim.ai/articles/exploring-effective-testing-frameworks-for-ai-agents-in-real-world-scenarios/ — Guide — Maxim's testing frameworks guide
[129]. **Exploring OpenAI's Swarm: An experimental framework** — https://medium.com/@michael_79773/exploring-openais-swarm-an-experimental-framework-for-multi-agent-systems-5ba09964ca18 — Blog — Medium's Swarm exploration
[130]. **Factory IDE | AI Coding Agents** — https://factory.ai/product/ide — tool — Factory IDE platform
[131]. **FastAPI Agents** — https://fastapi-agents.blairhudson.com/ — Doc — FastAPI Agents framework
[132]. **First impressions from testing 4 Coding Agents with Jupyter Notebooks** — https://www.leoniemonigatti.com/blog/coding-agent-jupyter-notebook.html — blog — Comparative analysis of coding agents
[133]. **Four Design Patterns for Event-Driven, Multi-Agent Systems** — https://www.confluent.io/blog/event-driven-multi-agent-systems/ — Blog — Confluent's event-driven patterns
[134]. **Function Calling vs Tool Use in AI Agents** — https://propelius.ai/blogs/function-calling-vs-tool-use-ai-agents/ — Blog — Comparison of function calling and tool use patterns
[135]. **GitHub - agno-agi/agno: The programming language for agentic software** — https://github.com/agno-agi/agno — Repo — Agno repository
[136]. **GitHub - browser-use/browser-use: Make websites accessible for AI agents** — https://github.com/browser-use/browser-use — Repo — Browser Use framework repository
[137]. **GitHub - crewAIInc/crewAI** — https://github.com/crewAIInc/crewAI — Repo — CrewAI official repository
[138]. **GitHub - getzep/graphiti: Build Real-Time Knowledge Graphs for AI Agents** — https://github.com/getzep/graphiti — Repo — Graphiti repository
[139]. **GitHub - langchain-ai/langgraph** — https://github.com/langchain-ai/langgraph — Repo — LangGraph official repository
[140]. **GitHub - livekit/agents-js: Build realtime multimodal AI agents** — https://github.com/livekit/agents-js — Repo — LiveKit agents-js repository
[141]. **GitHub - openai/openai-agents-js** — https://github.com/openai/openai-agents-js — Repo — OpenAI agents-js repository
[142]. **GitHub - openai/swarm: Educational framework exploring ergonomic multi-agent** — https://github.com/openai/swarm — Repo — OpenAI Swarm repository
[143]. **GitHub - statelyai/agent: Create state-machine-powered LLM agents** — https://github.com/statelyai/agent — Repo — Stately agents repository
[144]. **GitHub - strands-agents/sdk-typescript** — https://github.com/strands-agents/sdk-typescript — Repo — Strands SDK TypeScript repository
[145]. **GitHub - vercel-labs/agent-browser: Browser automation CLI for AI agents** — https://github.com/vercel-labs/agent-browser — Repo — Vercel's agent browser repository
[146]. **GitHub Next | Discovery Agent** — https://githubnext.com/projects/discovery-agent/ — tool — GitHub Next Discovery Agent
[147]. **Graphs Meet AI Agents: Taxonomy, Progress, and Future Opportunities** — https://arxiv.org/html/2506.18019v1 — Paper — Comprehensive survey on graphs and agents
[148]. **Guardrails - Docs by LangChain** — https://docs.langchain.com/oss/python/langchain/guardrails — Doc — LangChain's guardrails documentation
[149]. **Guardrails for AI Agents** — https://uxplanet.org/guardrails-for-ai-agents-24349b93caeb — Blog — UX Planet's guardrails article
[150]. **Guardrails for AI Agents** — https://www.agno.com/blog/guardrails-for-ai-agents — Blog — Agno's guardrails guide
[151]. **How a durable workflow engine works: you might not need a queue** — https://www.inngest.com/blog/how-durable-workflow-engines-work — Blog — Inngest's durable workflows explanation
[152]. **How Agentic Workflows Transform Enterprise Automation** — https://www.kore.ai/blog/agentic-workflows-and-how-are-they-redefining-process-automation-in-enterprises — Blog — Kore.ai's workflows article
[153]. **How APIs Power AI Agents: A Comprehensive Guide** — https://treblle.com/blog/api-guide-for-ai-agents — Guide — Treblle's API guide for agents
[154]. **How Human-in-the-Loop Is Evolving with AI Agents** — https://builtin.com/articles/human-in-the-loop-evolution — Blog — Built In's HITL evolution article
[155]. **How I Optimize Tokens While Building AI Agents** — https://pub.towardsai.net/how-i-optimize-tokens-while-building-ai-agents-without-killing-output-quality-804fedfb54fd — Blog — Towards AI's token optimization article
[156]. **How To Build Agentic GraphRAG** — https://memgraph.com/blog/build-agentic-graphrag-ai — Blog — Memgraph's GraphRAG guide
[157]. **How to Build an Evaluation Harness for your AI Agent** — https://odsc.ai/speakers-portfolio/how-to-build-an-evaluation-harness-for-your-ai-agent/ — Guide — ODSC's evaluation harness guide
[158]. **How to Build an Evaluation Harness for Your AI Agent** — https://medium.com/@Micheal-Lanham/how-to-build-an-evaluation-harness-for-your-ai-agent-before-it-books-the-wrong-flight-84de83a47207 — Blog — Medium's evaluation harness article
[159]. **How to build production-ready AI agents with RAG and FastAPI** — https://thenewstack.io/how-to-build-production-ready-ai-agents-with-rag-and-fastapi/ — Guide — The New Stack's production agents guide
[160]. **How to Build Vision AI Agents** — https://blog.roboflow.com/vision-agents/ — Blog — Roboflow's vision agents guide
[161]. **How to Evaluate AI Agents: Metrics, Benchmarks, and Real-World Practices** — https://medium.com/@sahin.samia/how-to-evaluate-ai-agents-metrics-benchmarks-and-real-world-practices-69a2674db899 — Blog — Medium's agent evaluation guide
[162]. **How to use Foundry Agent Service with function calling** — https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/tools/function-calling?view=foundry-classic — doc — Microsoft Azure guide on function calling
[163]. **How Tools Are Called in AI Agents** — https://medium.com/@sayalisureshkumbhar/how-tools-are-called-in-ai-agents-complete-2025-guide-with-examples-42dcdfe6ba38 — blog — Medium guide on tool calling
[164]. **Human-in-the-Loop for AI Agents: Best Practices, Frameworks, Use Cases** — https://www.permit.io/blog/human-in-the-loop-for-ai-agents-best-practices-frameworks-use-cases-and-demo — Blog — Permit.io's HITL guide
[165]. **Human-in-the-Loop in Agentic Workflows: From Definition to Walkthrough Demo** — https://orkes.io/blog/human-in-the-loop/ — Blog — Orkes' HITL workflows guide
[166]. **Human-in-the-loop in AI workflows: Meaning and patterns** — https://zapier.com/blog/human-in-the-loop/ — Blog — Zapier's HITL patterns guide
[167]. **I created an AI Agent to build README files** — https://medium.com/@filipespacheco/i-created-an-ai-agent-to-build-readme-files-here-is-what-i-learn-3ae207771d37 — blog — Medium post on building README files with AI
[168]. **Implementing Planning Agentic Pattern From Scratch** — https://www.dailydoseofds.com/ai-agents-crash-course-part-11-with-implementation/ — Guide — Daily Dose of Data Science's planning pattern guide
[169]. **Implementing ReAct Agentic Pattern From Scratch** — https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/ — Guide — Daily Dose of Data Science's ReAct implementation guide
[170]. **Index - Agent Development Kit (ADK)** — https://google.github.io/adk-docs/ — Doc — Google's ADK documentation
[171]. **Inngest - AI and backend workflows, orchestrated at any scale** — https://www.inngest.com/ — Doc — Inngest homepage
[172]. **Inngest Workflow - Mastra Docs** — https://mastra.ai/docs/workflows/inngest-workflow — Doc — Mastra's Inngest integration documentation
[173]. **Inngest: The Event-Driven Platform for Reliable Workflows and AI Orchestration** — https://medium.com/@moein.moeinnia/demystifying-inngest-the-event-driven-platform-for-reliable-workflows-and-ai-orchestration-388dc80c03af — Blog — Medium's Inngest explanation
[174]. **Integrations for AI Agents** — https://www.getknit.dev/blog/integrations-for-ai-agents — Blog — Knit's agent integrations guide
[175]. **Introducing Agent Development Kit for TypeScript** — https://developers.googleblog.com/introducing-agent-development-kit-for-typescript-build-ai-agents-with-the-power-of-a-code-first-approach — Blog — Google Developers' ADK announcement
[176]. **Introducing Swarm: OpenAI's New Open-Source Multi-Agent Framework** — https://www.kommunicate.io/blog/openai-swarm/ — Blog — Kommunicate's Swarm introduction
[177]. **Introduction - CrewAI** — https://docs.crewai.com/en/introduction — Doc — CrewAI official documentation
[178]. **Introduction to AI Agent Function Calling** — https://www.ema.co/additional-blogs/addition-blogs/ai-agent-function-calling — guide — EMA guide on function calling
[179]. **Introduction | LiveKit Documentation** — https://docs.livekit.io/agents/ — Doc — LiveKit Agents documentation
[180]. **Invincible Ai Content Workflows with Inngest and Directus** — https://directus.io/docs/tutorials/workflows/invincible-ai-content-workflows-with-inngest-and-directus — Guide — Directus's Inngest workflow tutorial
[181]. **KGARevion - An AI Agent for Knowledge-Intensive Biomedical QA** — https://zitniklab.hms.harvard.edu/projects/KGARevion/ — Doc — KGARevion project overview
[182]. **Kiro: Agentic AI development** — https://kiro.dev/ — tool — Kiro agentic development platform
[183]. **LangChain Agents: Build Scalable, Controlled Workflows** — https://www.langchain.com/agents — Doc — LangChain agents framework
[184]. **LangChain and LangGraph - AWS Prescriptive Guidance** — https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/langchain-langgraph.html — Doc — AWS's guide to LangChain and LangGraph
[185]. **LangChain and LangGraph Agent Frameworks Reach v1.0 Milestones** — https://blog.langchain.com/langchain-langgraph-1dot0/ — Blog — LangChain v1.0 announcement
[186]. **LangChain Python Tutorial: 2026's Complete Guide** — https://blog.jetbrains.com/pycharm/2026/02/langchain-tutorial-2026/ — Guide — PyCharm's LangChain tutorial
[187]. **LangGraph overview - Docs by LangChain** — https://docs.langchain.com/oss/python/langgraph/overview — Doc — LangGraph official documentation
[188]. **LangGraph State Machines: Managing Complex Agent Task Flows** — https://dev.to/jamesli/langgraph-state-machines-managing-complex-agent-task-flows-in-production-36f4 — Blog — DEV Community's LangGraph state machines guide
[189]. **LangGraph: Agent Orchestration Framework for Reliable AI Agents** — https://www.langchain.com/langgraph — Doc — LangChain's LangGraph framework overview
[190]. **LangGraph: Building Stateful AI Agents** — https://medium.com/@kevinnjagi83/langgraph-building-stateful-multi-ai-agents-b8427238da91 — Blog — Medium's LangGraph state agents article
[191]. **LLM Agents Improve Semantic Code Search** — https://arxiv.org/html/2408.11058v1 — academic — ArXiv paper on semantic search with LLM agents
[192]. **Long-term memory in agentic systems: Building context-aware agents** — https://www.moxo.com/blog/agentic-ai-memory — Blog — Moxo's long-term memory guide
[193]. **Making Sense of Memory in AI Agents** — https://www.leoniemonigatti.com/blog/memory-in-ai-agents.html — Blog — Leonie Monigatti's agent memory article
[194]. **Mastering AI agent observability: A comprehensive guide** — https://medium.com/online-inference/mastering-ai-agent-observability-a-comprehensive-guide-b142ed3604b1 — Guide — Medium's observability guide
[195]. **Mastering Project Context Files for AI Coding Agents** — https://eclipsesource.com/blogs/2025/11/20/mastering-project-context-files-for-ai-coding-agents/ — blog — EclipseSource guide on context files
[196]. **Mastering Retry Logic Agents: A Deep Dive into 2025 Best Practices** — https://sparkco.ai/blog/mastering-retry-logic-agents-a-deep-dive-into-2025-best-practices — Blog — Sparkco's retry logic guide
[197]. **Memory for AI Agents: A New Paradigm of Context Engineering** — https://thenewstack.io/memory-for-ai-agents-a-new-paradigm-of-context-engineering/ — Blog — The New Stack's agent memory guide
[198]. **Microsoft Agent Framework Multi-Turn Conversations** — https://learn.microsoft.com/en-us/agent-framework/user-guide/agents/multi-turn-conversation — doc — Microsoft Azure documentation on multi-turn conversations
[199]. **Microsoft Agent Framework Overview** — https://learn.microsoft.com/en-us/agent-framework/overview/agent-framework-overview — Doc — Microsoft Learn's Agent Framework guide
[200]. **Microsoft Agent Framework Workflows - Observability** — https://learn.microsoft.com/en-us/agent-framework/user-guide/workflows/observability — Doc — Microsoft's observability documentation
[201]. **Multi-agent Conversation Framework** — https://microsoft.github.io/autogen/0.2/docs/Use-Cases/agent_chat/ — Doc — AutoGen multi-agent framework documentation
[202]. **Multi-Agent Orchestration Redefined with Microsoft Semantic Kernel** — https://www.akira.ai/blog/multi-agent-with-microsoft-semantic-kernel — Blog — Akira's Semantic Kernel guide
[203]. **Multi-Agent Orchestration with OpenAI Swarm: A Practical Guide** — https://www.akira.ai/blog/multi-agent-orchestration-with-openai-swarm — Guide — Akira's Swarm guide
[204]. **Multi-agent Workflows: Use cases & architecture with Temporal** — https://temporal.io/blog/what-are-multi-agent-workflows — Blog — Temporal's multi-agent workflows guide
[205]. **Multimodal AI Agents: Text, Vision, and Speech in Action** — https://onereach.ai/blog/multimodal-ai-agents-enterprise-guide/ — Blog — OneReach's multimodal agents guide
[206]. **Navigating Modern LLM Agent Architectures** — https://www.wollenlabs.com/blog-posts/navigating-modern-llm-agent-architectures-multi-agents-plan-and-execute-rewoo-tree-of-thoughts-and-react — Blog — Wollen Labs' guide to agent architectures
[207]. **Nemotron Labs: 3 Ways to Bring Agentic AI to Computer Vision Applications** — https://blogs.nvidia.com/blog/ways-to-bring-agentic-ai-to-computer-vision-applications/ — Blog — NVIDIA's vision agents guide
[208]. **New OpenAI Swarm Framework Offers Experimental Tool** — https://campustechnology.com/articles/2024/10/29/new-openai-swarm-framework-offers-experimental-tool-for-multi-agent-ai-networks.aspx — Blog — Campus Technology's Swarm article
[209]. **Of course you can build dynamic AI agents with Temporal** — https://temporal.io/blog/of-course-you-can-build-dynamic-ai-agents-with-temporal — Blog — Temporal's dynamic agents blog
[210]. **OpenAI Agents SDK TypeScript** — https://openai.github.io/openai-agents-js/ — Doc — OpenAI Agents SDK TypeScript documentation
[211]. **OpenAI Swarm Framework Guide for Reliable Multi-Agents** — https://galileo.ai/blog/openai-swarm-framework-multi-agents — Blog — Galileo's Swarm guide
[212]. **OpenAI Swarm: A Hands-On Guide to Multi-Agent Systems** — https://www.analyticsvidhya.com/blog/2024/12/managing-multi-agent-systems-with-openai-swarm/ — Guide — Analytics Vidhya's Swarm guide
[213]. **OpenAI's Swarm: A Deep Dive into Multi-Agent Orchestration** — https://lablab.ai/t/openais-swarm-a-deep-dive-into-multi-agent-orchestration-for-everyone — Guide — Lablab's Swarm deep dive
[214]. **Orchestrating ambient agents with Temporal** — https://temporal.io/blog/orchestrating-ambient-agents-with-temporal — Blog — Temporal's ambient agents guide
[215]. **Orchestrating Multi-Agent AI With Semantic Kernel** — https://www.digitalbricks.ai/blog-posts/orchestrating-multi-agent-ai-with-semantic-kernel — Blog — Digital Bricks' Semantic Kernel guide
[216]. **Orchestrating Multi-Step Agents: Temporal/Dagster/LangGraph Patterns** — https://www.kinde.com/learn/ai-for-software-engineering/ai-devops/orchestrating-multi-step-agents-temporal-dagster-langgraph-patterns-for-long-running-work/ — Guide — Kinde's multi-step agent orchestration guide
[217]. **Orchestrating Specialist AI Agents with CrewAI: A Guide** — https://activewizards.com/blog/orchestrating-specialist-ai-agents-with-crewai-a-guide/ — Guide — ActiveWizards' CrewAI orchestration guide
[218]. **Pair Programming with AI Coding Agents** — https://zencoder.ai/blog/best-practices-for-pair-programming-with-ai-coding-agents — blog — Zencoder guide on pair programming with AI
[219]. **Plan-and-Execute Agents** — https://blog.langchain.com/planning-agents/ — Blog — LangChain's plan-and-execute agent patterns
[220]. **Prompt Injection Attacks in Large Language Models and AI Agent Systems** — https://www.mdpi.com/2078-2469/17/1/54 — Paper — Comprehensive prompt injection attacks paper
[221]. **Quickstart: Create and test a basic agent** — https://learn.microsoft.com/en-us/microsoft-365/agents-sdk/quickstart — Guide — Microsoft 365 Agents SDK quickstart
[222]. **ReAct agent from scratch with Gemini and LangGraph** — https://ai.google.dev/gemini-api/docs/langgraph-example — Guide — Google's ReAct agent tutorial
[223]. **ReAct Pattern: Combining Reasoning and Acting in AI Agents** — https://hopx.ai/blog/ai-agents/react-pattern-reasoning-acting/ — Blog — Hopx's guide to ReAct pattern
[224]. **ReAct vs Plan-and-Execute: A Practical Comparison** — https://dev.to/jamesli/react-vs-plan-and-execute-a-practical-comparison-of-llm-agent-patterns-4gh9 — Blog — DEV Community's comparison of ReAct and planning
[225]. **ReAct: Synergizing Reasoning and Acting in Language Models** — https://research.google/blog/react-synergizing-reasoning-and-acting-in-language-models/ — Blog — Google Research's ReAct paper announcement
[226]. **Reasoning beyond limits: Advances and open problems for LLMs** — https://www.sciencedirect.com/science/article/pii/S240595952500133X — Paper — Science Direct's LLM reasoning advances
[227]. **Reasoning models** — https://platform.openai.com/docs/guides/reasoning — Doc — OpenAI's reasoning models documentation
[228]. **Reasoning Models Don't Always Say What They Think** — https://assets.anthropic.com/m/71876fabef0f0ed4/original/reasoning_models_paper.pdf — paper — Research on reasoning model transparency
[229]. **Reasoning Models Generate Societies of Thought** — https://arxiv.org/html/2601.10825v1 — Paper — Reasoning models and thought societies paper
[230]. **Rovo Dev | Agentic AI for software teams** — https://www.atlassian.com/software/rovo-dev — tool — Atlassian Rovo Dev platform
[231]. **Scaling Agentic AI: Strategy for Enterprise-Wide Implementation** — https://aisera.com/blog/scaling-agentic-ai/ — Blog — Aisera's scaling guide
[232]. **Search-o1: Agentic Search-Enhanced Large Reasoning Models** — https://arxiv.org/pdf/2501.05366 — Paper — Search-o1 research paper
[233]. **Secrets of Agentic UX: Emerging Design Patterns** — https://uxmag.com/articles/secrets-of-agentic-ux-emerging-design-patterns-for-human-interaction-with-ai-agents — Blog — UX Magazine's agentic UX article
[234]. **Securing AI Agents with Layered Guardrails and Risk Taxonomy** — https://www.enkryptai.com/blog/securing-ai-agents-a-comprehensive-framework-for-agent-guardrails — Blog — Enkrypt AI's guardrails framework
[235]. **Semantic Kernel + AutoGen = Open-Source Microsoft Agent Framework** — https://visualstudiomagazine.com/articles/2025/10/01/semantic-kernel-autogen--open-source-microsoft-agent-framework.aspx — Blog — Visual Studio Magazine's coverage of Agent Framework
[236]. **Semantic Kernel Agent Architecture** — https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/agent-architecture — Doc — Semantic Kernel agent architecture documentation
[237]. **Semantic Kernel Agent Framework** — https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/ — Doc — Semantic Kernel agent framework documentation
[238]. **Semantic Kernel Agent Orchestration** — https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/agent-orchestration/ — Doc — Microsoft Learn's Semantic Kernel agent orchestration
[239]. **Semantic Kernel Agent Orchestration Advanced Topics** — https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/agent-orchestration/advanced-topics — Doc — Advanced Semantic Kernel topics
[240]. **Semantic Kernel: Multi-agent Orchestration** — https://devblogs.microsoft.com/semantic-kernel/semantic-kernel-multi-agent-orchestration/ — Blog — Microsoft's Semantic Kernel multi-agent blog
[241]. **Software Architecture That Agents Actually Like** — https://actuallymaybe.com/blog/agent-friendly-architecture/ — blog — Actually Maybe blog on agent-friendly architecture
[242]. **State Machines vs. AI Agents: Why Traditional Workflows Are Dead Technology** — https://www.autonoly.com/blog/686f3a9071d44a7c526e647b/state-machines-vs-ai-agents-why-traditional-workflows-are-dead-technology — Blog — Autonoly's workflows comparison
[243]. **State Management Frameworks - Agentic AI Architecture** — https://oboe.com/learn/agentic-ai-architecture-and-autonomous-systems-ien507/state-management-frameworks-gqmcec — Guide — Oboe's state management guide
[244]. **Steering AI Agents in Monorepos with AGENTS.md** — https://dev.to/datadog-frontend-dev/steering-ai-agents-in-monorepos-with-agentsmd-13g0 — blog — DEV Community guide on monorepo AI steering
[245]. **SWE-EVO: Benchmarking Coding Agents** — https://www.arxiv.org/pdf/2512.18470 — Paper — SWE-EVO benchmark paper
[246]. **Teach Your AI Agent How to Work in a Monorepo** — https://nx.dev/blog/nx-ai-agent-skills — blog — Nx blog on monorepo AI skills
[247]. **Temporal + AI Agents: The Missing Piece for Production-Ready Agentic Systems** — https://dev.to/akki907/temporal-workflow-orchestration-building-reliable-agentic-ai-systems-3bpm — Blog — DEV Community's Temporal agents guide
[248]. **The AI Agent Behavioral Validation Testing Playbook** — https://galileo.ai/learn/ai-observability/ai-agent-testing-behavioral-validation — Guide — Galileo's behavioral validation guide
[249]. **The best agentic IDEs heading into 2026** — https://www.builder.io/blog/agentic-ide — blog — Builder.io blog on agentic IDEs
[250]. **The Best Web Agents: Computer Use vs Operator vs Browser Use** — https://www.helicone.ai/blog/browser-use-vs-computer-use-vs-operator — Blog — Helicone's web agent comparison
[251]. **The Future of Debugging: AI Agents** — https://www.akira.ai/blog/ai-agents-for-debugging — blog — Akira blog on AI debugging
[252]. **The Hidden Economics of AI Agents: Managing Token Costs** — https://online.stevens.edu/blog/hidden-economics-ai-agents-token-costs-latency/ — Blog — Stevens Online's token economics article
[253]. **The Hidden Superpower Behind Modern AI Agents: The ReAct Pattern** — https://www.hexstream.com/tech-corner/the-hidden-superpower-behind-modern-ai-agents-the-react-pattern-and-why-langgraph-changes-everything — Blog — Hexstream's article on ReAct and LangGraph
[254]. **The Leading Multi-Agent Platform** — https://crewai.com/ — Doc — CrewAI homepage
[255]. **The Open Source Multi-Agent Orchestration Framework** — https://crewai.com/open-source — Doc — CrewAI open-source overview
[256]. **The Rise of Multimodal AI Agents: Building Vision, Voice & Text Systems** — https://getstream.io/blog/multimodal-ai-agents/ — Blog — GetStream's multimodal agents guide
[257]. **The role of knowledge graphs in building agentic AI systems** — https://zbrain.ai/knowledge-graphs-for-agentic-ai/ — Blog — ZBrain's knowledge graphs guide
[258]. **The ultimate LLM agent build guide** — https://www.vellum.ai/blog/the-ultimate-llm-agent-build-guide — Blog — Vellum's comprehensive agent building guide
[259]. **Thought: Internal Reasoning and the ReAct Approach** — https://huggingface.co/learn/agents-course/en/unit1/thoughts — Course — Hugging Face Agents Course on ReAct
[260]. **Token Cost Trap: Why Your AI Agent's ROI Breaks at Scale** — https://medium.com/@klaushofenbitzer/token-cost-trap-why-your-ai-agents-roi-breaks-at-scale-and-how-to-fix-it-4e4a9f6f5b9a — Blog — Medium's token cost analysis
[261]. **Token Optimization Strategies for AI Agents** — https://medium.com/elementor-engineers/optimizing-token-usage-in-agent-based-assistants-ffd1822ece9c — Blog — Medium's token optimization article
[262]. **Tool Calling Explained: The Core of AI Agents** — https://composio.dev/blog/ai-agent-tool-calling-guide — blog — Composio guide on tool calling
[263]. **Top 10 Low‑Code AI Workflow Automation Tools** — https://www.vellum.ai/blog/top-low-code-ai-workflow-automation-tools — blog — Vellum guide to low-code automation
[264]. **Top AI Agentic Workflow Patterns** — https://blog.bytebytego.com/p/top-ai-agentic-workflow-patterns — Blog — ByteByteGo's guide to agentic workflow patterns
[265]. **Top techniques to Manage Context Lengths in LLMs** — https://agenta.ai/blog/top-6-techniques-to-manage-context-length-in-llms — blog — Agenta guide on context length management
[266]. **Tutorial: Build an AI workflow in n8n** — https://docs.n8n.io/advanced-ai/intro-tutorial/ — Guide — n8n's AI workflow tutorial
[267]. **Ultimate Guide to AI Agent Routing** — https://botpress.com/blog/ai-agent-routing — Guide — Botpress's agent routing guide
[268]. **Use Foundry Agent Service with function calling** — https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/tools-classic/function-calling?view=foundry-classic — doc — Microsoft Azure documentation on function calling
[269]. **Vertex AI Agent Builder** — https://cloud.google.com/products/agent-builder — Doc — Google Cloud's Agent Builder
[270]. **Video Analytics AI Agents** — https://www.nvidia.com/en-us/use-cases/video-analytics-ai-agents/ — Blog — NVIDIA's video analytics guide
[271]. **Vision Agents** — https://visionagents.ai — Doc — Vision Agents homepage
[272]. **Vision AI Agents: How They Work & Real-World Examples** — https://www.labellerr.com/blog/vision-ai-agents-how-they-work-examples/ — Blog — Labellerr's vision agents guide
[273]. **Vision-Language Agents: Multimodal Intelligence** — https://www.emergentmind.com/topics/vision-language-agent — Blog — Emergent Mind's vision-language agents article
[274]. **Visual Agents at CVPR 2025** — https://voxel51.com/blog/visual-agents-at-cvpr-2025/ — Blog — Voxel51's CVPR 2025 visual agents article
[275]. **What are Agentic AI Workflows?** — https://temporal.io/blog/build-resilient-agentic-ai-with-temporal — Blog — Temporal's agentic AI workflows guide
[276]. **What are Agentic Workflows** — https://www.ibm.com/think/topics/agentic-workflows — Blog — IBM's agentic workflows explanation
[277]. **What are Plan and execute agents** — https://www.promptlayer.com/glossary/plan-and-execute-agents — Guide — PromptLayer's plan-and-execute glossary
[278]. **What is a ReAct Agent** — https://www.ibm.com/think/topics/react-agent — Blog — IBM's explanation of ReAct agents
[279]. **What Is Agentic Reasoning** — https://www.ibm.com/think/topics/agentic-reasoning — Blog — IBM's agentic reasoning explanation
[280]. **What Is AI Agent Memory** — https://www.ibm.com/think/topics/ai-agent-memory — Blog — IBM's agent memory explanation
[281]. **What is crewAI** — https://www.ibm.com/think/topics/crew-ai — Blog — IBM's explanation of CrewAI
[282]. **What is Human-in-the-Loop? A Guide to AI Agent Workflows** — https://beetroot.co/ai-ml/human-in-the-loop-meets-agentic-ai-building-trust-and-control-in-automated-workflows/ — Guide — Beetroot's HITL guide
[283]. **What is the Microsoft 365 Agents SDK** — https://learn.microsoft.com/en-us/microsoft-365/agents-sdk/agents-sdk-overview — Doc — Microsoft 365 Agents SDK documentation
[284]. **What's Good for AI Agents is Good for Engineers** — https://cleric.ai/blog/whats-good-for-ai-agents-is-good-for-engineers — blog — Cleric blog on AI-friendly architecture
[285]. **Why Agentic AI Needs Guardrails to Thrive** — https://aembit.io/blog/agentic-ai-guardrails-for-safe-scaling/ — Blog — Aembit's guardrails article
[286]. **Why observability is essential for AI agents** — https://www.ibm.com/think/insights/ai-agent-observability — Blog — IBM's agent observability article
[287]. **Writing AI Agents From Scratch: Planning Is The Key** — https://www.decodingai.com/p/ai-agents-planning — Blog — Decoding AI's guide to agent planning
[288]. **Zapier: Automate AI Workflows, Agents, and Apps** — https://zapier.com/ — tool — Zapier automation platform with AI
[289]. **Zero to One: Learning Agentic Patterns** — https://www.philschmid.de/agentic-pattern — Blog — Philipp Schmid's guide to learning agentic patterns
[290]. **𝜏-Bench: Benchmarking AI agents for the real-world** — https://sierra.ai/blog/benchmarking-ai-agents — Blog — Sierra's 𝜏-bench guide
[291]. **🦸🏻#11: How Do Agents Plan and Reason** — https://huggingface.co/blog/Kseniase/reasonplan — Blog — Hugging Face's agent reasoning article

### A7. AI Coding Assistants (Copilot, Windsurf, Aider, etc.)

[1]. **5 tips for writing better custom instructions for Copilot** — https://github.blog/ai-and-ml/github-copilot/5-tips-for-writing-better-custom-instructions-for-copilot/ — blog — GitHub Blog guide on best practices for Copilot instructions
[2]. **About GitHub Copilot coding agent** — https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent — doc — GitHub documentation on coding agents
[3]. **Adding repository custom instructions for GitHub Copilot** — https://docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot — doc — Official GitHub documentation for adding custom instructions to Copilot
[4]. **Agentic Coding Tools Explained: Complete Setup Guide** — https://www.ikangai.com/agentic-coding-tools-explained-complete-setup-guide-for-claude-code-aider-and-cli-based-ai-development/ — Guide — Ikangai's Aider setup guide
[5]. **AI Coding Assistants Comparison 2026** — https://seedium.io/blog/comparison-of-best-ai-coding-assistants/ — blog — Seedium comparison guide for 2026
[6]. **Aider - AI Agent** — https://aiagentstore.ai/ai-agent/aider — Blog — AI Agent Store's Aider review
[7]. **Aider - AI Pair Programming in Your Terminal** — https://aider.chat/ — Doc — Aider homepage
[8]. **Aider Documentation** — https://aider.chat/docs/ — Doc — Aider official documentation
[9]. **Aider FAQ** — https://aider.chat/docs/faq.html — doc — Aider documentation FAQ section
[10]. **Aider GitHub repository** — https://github.com/Aider-AI/aider — repo — Official Aider open-source repository
[11]. **Aider Usage Documentation** — https://aider.chat/docs/usage.html — doc — Aider usage documentation
[12]. **awesome-copilot instructions documentation** — https://github.com/github/awesome-copilot/blob/main/docs/README.instructions.md — doc — Comprehensive instructions documentation in awesome-copilot
[13]. **awesome-windsurf repository** — https://github.com/ichoosetoaccept/awesome-windsurf — repo — Collection of awesome resources for Windsurf
[14]. **Best AI Coding Assistants as of February 2026** — https://www.shakudo.io/blog/best-ai-coding-assistants — blog — Current rankings of AI coding assistants
[15]. **Building a Brilliant AI Copilot: Using Knowledge Graphs** — https://medium.com/@dan.avila7/building-a-brilliant-ai-copilot-using-knowledge-graphs-as-a-codebase-7b8c701b6763 — blog — Medium article on knowledge graphs
[16]. **Building Code Knowledge Graphs for Modern Software Engineering** — https://adapts.ai/blog/building-code-knowledge-graphs-for-modern-software-engineering/ — blog — Adapts blog on knowledge graphs
[17]. **Choosing the Right Brain: AI Models in GitHub Copilot Explained** — https://medium.com/@anil.goyal0057/choosing-the-right-brain-ai-models-in-github-copilot-explained-0a8d8cd34494 — blog — Medium article on Copilot models
[18]. **Choosing the Right Model in GitHub Copilot** — https://techcommunity.microsoft.com/blog/azuredevcommunityblog/choosing-the-right-model-in-github-copilot-a-practical-guide-for-developers/4491623 — blog — Microsoft blog on model selection
[19]. **Codeium Windsurf IDE rules file** — https://dev.to/yardenporat/codium-windsurf-ide-rules-file-1hn9 — blog — DEV Community guide to Windsurf rules configuration
[20]. **Codeium Windsurf IDE Rules: Boost Coding Efficiency** — https://kitemetric.com/blogs/codeium-windsurf-ide-rules-boost-coding-efficiency — blog — Guide on Windsurf rules for efficiency
[21]. **Coding Agents 101: The Art of Actually Getting Things Done** — https://devin.ai/agents101 — Guide — Devin's coding agents guide
[22]. **Cognition | Introducing Devin, the first AI software engineer** — https://cognition.ai/blog/introducing-devin — Blog — Cognition's Devin announcement
[23]. **Comparing 5 AI Coding Assistants** — https://dev.to/bekahhw/comparing-5-ai-coding-assistants-18l4 — blog — DEV Community comparison of coding assistants
[24]. **Customize GitHub Copilot in JetBrains with Custom Instructions** — https://devblogs.microsoft.com/java/customize-github-copilot-in-jetbrains-with-custom-instructions/ — blog — Microsoft guide for JetBrains IDE configuration
[25]. **Devin AI - Wikipedia** — https://en.wikipedia.org/wiki/Devin_AI — Blog — Wikipedia article on Devin AI
[26]. **Devin | The AI Software Engineer** — https://devin.ai/ — Doc — Devin AI homepage
[27]. **Everything I Know About GitHub Copilot Instructions** — https://dev.to/anchildress1/everything-i-know-about-github-copilot-instructions-from-zero-to-onboarded-for-real-4nb0 — blog — DEV Community comprehensive guide to Copilot instructions
[28]. **Getting Started with Aider** — https://blog.openreplay.com/getting-started-aider-ai-coding-terminal/ — blog — OpenReplay guide to Aider setup
[29]. **GitHub awesome-copilot repository** — https://github.com/github/awesome-copilot — repo — Community-contributed instructions and configurations for Copilot
[30]. **GitHub Copilot Business** — https://github.com/features/copilot/copilot-business — product — GitHub Copilot Business page
[31]. **GitHub Copilot CLI is now generally available** — https://github.blog/changelog/2026-02-25-github-copilot-cli-is-now-generally-available/ — blog — GitHub Changelog on Copilot CLI
[32]. **GitHub Copilot Custom Instructions Complete Guide** — https://smartscope.blog/en/generative-ai/github-copilot/github-copilot-custom-instructions-guide/ — guide — Comprehensive guide to Copilot custom instructions setup and best practices
[33]. **GitHub Copilot in VS Code** — https://code.visualstudio.com/docs/copilot/overview — doc — VS Code Copilot overview documentation
[34]. **GitHub Copilot in VS Code cheat sheet** — https://code.visualstudio.com/docs/copilot/reference/copilot-vscode-features — doc — VS Code Copilot feature reference
[35]. **GitHub Copilot in VS Code settings reference** — https://code.visualstudio.com/docs/copilot/reference/copilot-settings — doc — VS Code Copilot settings documentation
[36]. **GitHub Copilot · Plans & pricing** — https://github.com/features/copilot/plans — product — GitHub Copilot pricing page
[37]. **GitHub Copilot · Your AI pair programmer** — https://github.com/features/copilot — tool — GitHub Copilot official page
[38]. **GitHub Copilot's High Thinking Mode** — https://www.arsturn.com/blog/github-copilots-high-thinking-mode-how-gpt-5-makes-it-a-reality — blog — Arsturn blog on thinking mode
[39]. **GitHub for Beginners: Test-driven development with GitHub Copilot** — https://github.blog/ai-and-ml/github-copilot/github-for-beginners-test-driven-development-tdd-with-github-copilot/ — blog — GitHub blog on TDD with Copilot
[40]. **Human in the Loop (HITL)** — https://docs.copilotkit.ai/langgraph/human-in-the-loop — Doc — CopilotKit's HITL documentation
[41]. **Managing Copilot: Governance and GitHub Copilot** — https://resources.github.com/beyond-the-commit/governance-and-github-copilot/ — guide — GitHub Resources guide on Copilot governance
[42]. **Managing policies and features for GitHub Copilot in your enterprise** — https://docs.github.com/enterprise-cloud@latest/copilot/managing-copilot/managing-copilot-for-your-enterprise/managing-policies-and-features-for-copilot-in-your-enterprise — doc — GitHub Enterprise documentation on Copilot policies
[43]. **Managing policies and features for GitHub Copilot in your organization** — https://docs.github.com/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-github-copilot-features-in-your-organization/managing-policies-for-copilot-in-your-organization — doc — GitHub documentation on organization policies
[44]. **Mastering GitHub Copilot Custom Instructions with .github/copilot-instructions.md** — https://medium.com/@anil.goyal0057/mastering-github-copilot-custom-instructions-with-github-copilot-instructions-md-f353e5abf2b1 — blog — Medium article on file-based instruction customization
[45]. **Mastering GitHub Copilot customization with Copilot-instructions** — https://medium.com/@frank.laule/mastering-github-copilot-customization-with-copilot-instructions-83e8cc1ca10a — blog — Medium guide on Copilot-instructions customization
[46]. **OpenHands - Open-Source AI Software Craft** — https://oss-ai-swe.org/open-hands/ — Doc — OpenHands project overview
[47]. **OpenHands vs SWE-agent: A Detailed Comparison** — https://openalternative.co/compare/openhands/vs/swe-agent — Blog — Detailed OpenHands vs SWE-agent comparison
[48]. **OpenHands vs SWE-Agent: Best AI Coding Agent 2026** — https://localaimaster.com/blog/openhands-vs-swe-agent — Blog — Comparison of OpenHands and SWE-Agent
[49]. **OpenHands | The Open Platform for Cloud Coding Agents** — https://openhands.dev/ — Doc — OpenHands homepage
[50]. **OpenHands: An Open Platform for AI Software Developers as Generalist Agents** — https://arxiv.org/abs/2407.16741 — Paper — OpenHands research paper
[51]. **Repository map | Aider** — https://aider.chat/docs/repomap.html — doc — Aider documentation on repository mapping
[52]. **Set up GitHub Copilot in VS Code** — https://code.visualstudio.com/docs/copilot/setup — doc — VS Code Copilot setup guide
[53]. **Specifying coding conventions | Aider** — https://aider.chat/docs/usage/conventions.html — doc — Aider guide on coding conventions configuration
[54]. **Supported AI models in GitHub Copilot** — https://docs.github.com/en/copilot/reference/ai-models/supported-models — doc — GitHub documentation on supported models
[55]. **The Best AI Coding Assistants: A Full Comparison of 17 Tools** — https://axify.io/blog/the-best-ai-coding-assistants-a-full-comparison-of-17-tools — blog — Detailed comparison of coding assistants
[56]. **Top 15 AI Coding Assistant Tools to Try in 2026** — https://www.qodo.ai/blog/best-ai-coding-assistant-tools/ — blog — Comprehensive comparison of AI coding assistants
[57]. **Tune GitHub Copilot Settings in VS Code** — https://dev.to/pwd9000/tune-github-copilot-settings-in-vs-code-32kp — blog — DEV Community guide on Copilot tuning
[58]. **Under the hood: Exploring the AI models powering GitHub Copilot** — https://github.blog/ai-and-ml/github-copilot/under-the-hood-exploring-the-ai-models-powering-github-copilot/ — blog — GitHub Blog on Copilot models
[59]. **Use custom instructions in VS Code** — https://code.visualstudio.com/docs/copilot/customization/custom-instructions — doc — VS Code's guide to customizing Copilot with custom instructions
[60]. **Using Aider AI for code generation** — https://symflower.com/en/company/blog/2024/using-aider-for-code-generation/ — Blog — Symflower's Aider guide
[61]. **Welcome to Windsurf** — https://docs.windsurf.com/windsurf/getting-started — doc — Official Windsurf documentation getting started guide
[62]. **Which AI model should I use with GitHub Copilot?** — https://github.blog/ai-and-ml/github-copilot/which-ai-model-should-i-use-with-github-copilot/ — blog — GitHub Blog on model selection
[63]. **Windsurf Editor Changelog** — https://windsurf.com/changelog — doc — Official changelog tracking Windsurf features and updates
[64]. **Windsurf Rules Directory** — https://windsurf.com/windsurf/directory — doc — Official Windsurf rules directory and patterns
[65]. **YAML config file | Aider** — https://aider.chat/docs/config/aider_conf.html — doc — Aider YAML configuration guide

### A8. Tool Use & Function Calling

[1]. **JSON Schema for LLM Tools** — https://blog.promptlayer.com/how-json-schema-works-for-structured-outputs-and-tool-integration/ — article — JSON schema for LLMs
[2]. **Structured data Amazon Bedrock** — https://aws.amazon.com/blogs/machine-learning/structured-data-response-with-amazon-bedrock-prompt-engineering-and-tool-use/ — article — Bedrock structured data responses
[3]. **Tool & Function Calling | Use Tools with OpenRouter** — https://openrouter.ai/docs/guides/features/tool-calling — Doc — OpenRouter's tool calling documentation
[4]. **Tool Use & API Integration** — https://www.digitaldividedata.com/agentic-ai/tool-use-api-integration — Guide — Digital Divide Data's tool use guide
[5]. **What Is Tool Calling?** — https://www.ibm.com/think/topics/tool-calling — guide — IBM guide on tool calling

### A9. Skill/Plugin Architecture & Design
