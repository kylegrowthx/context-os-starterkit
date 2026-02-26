# Nano Banana Prompting: Operator Guide

> **For:** AI operators, creative directors, content creators, and automation builders
> **Goal:** Master Nano Banana (Google Gemini image generation) prompting with reusable frameworks, template patterns, and systematic workflows — ready to be turned into an agent skill
> **Time Investment:** 8-12 hours for full mastery; 2-3 hours for core frameworks
> **Sources:** 500+ verified sources (indexed in Appendix A)
> **Last Updated:** 2026-02-21

---

## How to Use This Guide

This guide is structured as an operator manual, not a tutorial. Each section is designed to be independently useful. Start with Part 1 for mental models, jump to Part 3 for copy-paste frameworks, or go straight to Part 6 for template patterns.

**If you're building an agent skill:** Focus on Parts 3, 4, 6, and 7. These contain the structured frameworks, decision trees, and template patterns that translate directly into programmatic workflows.

**If you're a creative director:** Parts 2, 3, and 5 cover the strategic thinking and systematic approaches you need.

**If you're optimizing existing workflows:** Parts 4, 7, and 8 cover iteration, automation, and API integration.

---

## Part 1: Foundations — What Nano Banana Is and Why It Matters

### 1.1 Origin Story

In August 2025, a mysterious image generation model appeared on LMArena (the image equivalent of Chatbot Arena) under the codename "nano-banana." It quickly dominated the leaderboard with a 70% win rate, accumulating 5 million votes in two weeks. The AI community was captivated — nobody knew who made it.

On August 26, 2025, Google revealed that Nano Banana was **Gemini 2.5 Flash Image**, their new image generation model. The name came from Google PM Naina Raisinghani, who combined her childhood nickname "Naina Banana" with "Nano" during a late-night naming session. Google officially adopted the community's beloved codename.

**Source:** [How Nano Banana Got Its Name — Google Blog](https://blog.google/products-and-platforms/products/gemini/how-nano-banana-got-its-name/) · [LMArena Announcement](https://news.lmarena.ai/nano-banana/) · [Complete Timeline — AI Stack](https://ai-stack.ai/en/nano-banana-2025/)

### 1.2 The Architecture Shift: Why Prompting Changed

Nano Banana represents a fundamental shift in how AI generates images. Previous models (Stable Diffusion, DALL-E, Midjourney) used **diffusion** — starting with noise and gradually refining it into an image. Nano Banana uses **autoregressive token generation** — the same approach that powers ChatGPT for text, but applied to images.

**What this means for operators:**

The model generates 1,290 tokens per image, processing your prompt the same way a language model processes a conversation. This is why Nano Banana responds to natural language descriptions rather than keyword stacking. Writing "4k, masterpiece, trending on artstation, ultra-detailed" does nothing — the model already processes context semantically.

**The practical implication:** Think of prompting Nano Banana like giving a brief to an intelligent designer, not like entering search keywords. Describe what you want as if you're talking to a person.

**Source:** [Max Woolf's Technical Analysis](https://minimaxir.com/2025/11/nano-banana-prompts/) · [Google DeepMind Model Page](https://deepmind.google/models/gemini-image/flash/) · [Autoregressive Models in Vision Survey — GitHub](https://github.com/ChaofanTao/Autoregressive-Models-in-Vision-Survey)

### 1.3 Two Models: Flash vs Pro

Google ships two Nano Banana models. Understanding when to use each is the first operator decision.

**Nano Banana (Gemini 2.5 Flash Image)** — Speed and pattern-matching. Best for quick iterations, simple edits, and high-volume generation. Generates images in seconds. No "thinking" step.

**Nano Banana Pro (Gemini 3 Pro Image)** — Released November 2025. Adds a "Deep Think" reasoning engine that plans a scene's logic before generating. Best for complex layouts, precise text rendering, infographics, and multi-constraint compositions. Key upgrades include perfect text rendering (can spell long sentences and complex logos), search grounding (connects to Google Search for factual accuracy), and few-shot design (accepts up to 14 reference images for brand/character consistency).

**Decision framework:**

| Use Flash when... | Use Pro when... |
|---|---|
| Speed matters more than precision | Text must render perfectly |
| Simple compositions (1-2 subjects) | Complex layouts (infographics, diagrams) |
| Quick iteration cycles | Brand consistency across outputs |
| High volume / batch processing | Factual accuracy matters (search grounding) |
| Budget-sensitive workflows | Multi-image reference needed |

**Source:** [Nano Banana vs Pro Comparison — Artlist](https://artlist.io/blog/nano-banana-vs-nano-banana-pro/) · [Google DeepMind Pro Page](https://deepmind.google/models/gemini-image/pro/) · [Google Official Announcement](https://blog.google/technology/ai/nano-banana-pro/)

### 1.4 Mental Models for Expert Prompting

Experts approach Nano Banana with these mental models:

**1. Creative Director, not prompt engineer.** You're giving a brief to a talented designer. The model understands intent, context, and relationships — not just keywords. Spend 90% of your time on strategy and 10% on execution.

**2. Work Surface thinking (Pro only).** Don't think "generate an image." Think "design a surface." A poster has a canvas size, a grid, zones for text and visuals, a hierarchy. Describe the surface, not just the content.

**3. One variable per iteration.** When refining, change one thing at a time. If you change the lighting AND the composition AND the style, you can't learn what worked.

**4. Constraints are your friend.** The more specific your constraints (aspect ratio, color palette, camera angle, text placement), the better the output. Vagueness is the enemy.

### 1.5 Common Misconceptions

**Misconception 1: "More keywords = better results."** False. Nano Banana isn't searching a database — it's reasoning about your prompt. Keyword stacking ("4k, hyper-realistic, masterpiece, trending") adds noise, not signal.

**Misconception 2: "Negative prompts work like Stable Diffusion."** Partially true. There's no dedicated negative prompt parameter. Instead, use semantic negatives within your prompt: "No extra fingers. No watermarks. No text except the title."

**Misconception 3: "Short prompts are best."** Depends on the model. Flash handles shorter prompts well. Pro thrives on detailed, structured briefs that give it reasoning material.

**Misconception 4: "You can't control text rendering."** Pro renders text accurately when you use double quotation marks around the exact string and keep text under 25 characters.

**Source:** [Common Mistakes and Troubleshooting — UseNanoBanana](https://usenanobanana.com/blog/5-common-mistakes-troubleshooting) · [Prompt Engineering Best Practices — Skywork](https://skywork.ai/blog/ai-image/prompt-engineering-best-practices-nano-banana-pro-2025/)

---

## Part 2: The Core Prompt Framework

### 2.1 The Standard Formula

The universally recommended Nano Banana prompt structure:

```
[Subject + Adjectives] doing [Action] in [Location/Context].
[Composition/Camera Angle].
[Lighting/Atmosphere].
[Style/Media].
[Specific Constraint/Text].
```

**Example:**
```
A weathered Japanese fisherman mending a net on a wooden dock at sunrise.
Low angle shot, rule of thirds composition.
Golden hour lighting with soft mist rising from the water.
Documentary photography style, shot on Fujifilm X-T5, 35mm f/1.4.
No text. Aspect ratio 16:9.
```

**Source:** [Ultimate Nano Banana Prompting Guide — Atlabs](https://www.atlabs.ai/blog/nano-banana-prompting-guide) · [Leonardo.ai Prompt Guide](https://leonardo.ai/news/nano-banana-prompt-guide/)

### 2.2 The 6-Component Breakdown

Every effective Nano Banana prompt addresses six components. Not all are required — but the more you specify, the more control you have:

| Component | What it controls | Example |
|---|---|---|
| **Subject** | Who/what is in the image | "A majestic Persian cat with long white fur" |
| **Action** | What's happening | "sitting regally on a velvet cushion" |
| **Setting** | Where/when | "in a sunlit Victorian greenhouse" |
| **Style** | Visual treatment | "oil painting, impasto technique, warm palette" |
| **Composition** | How it's framed | "close-up, shallow depth of field, centered" |
| **Constraints** | Guardrails | "No text. Aspect ratio 1:1. No background elements." |

### 2.3 The 5-Input System (Creative Director Approach)

The most effective modern approach (2026 best practice) treats the operator as a Creative Director who defines strategic inputs, then lets an LLM translate them into a technically perfect prompt:

**The 5 inputs:**
1. **Purpose** — What will this image be used for?
2. **Audience** — Who will see this?
3. **Subject** — What's in the image?
4. **Brand Guidelines** — Colors, fonts, mood, restrictions?
5. **Reference Images** (optional) — Visual examples of what you want

**Why this works:** Instead of guessing camera specs, you define the strategic context. An LLM (Claude, ChatGPT) then generates the technically structured prompt. This approach reportedly achieves professional-quality results on the first try.

**Workflow:**
```
Step 1: Define 5 inputs
Step 2: Feed to LLM → get structured JSON prompt
Step 3: Send JSON prompt to Nano Banana API
Step 4: Inspect output against brief
Step 5: Iterate (change ONE variable)
```

**Source:** [How to Get a Professional Image with Nano Banana Pro — AI Fire](https://www.aifire.co/p/how-to-get-a-professional-image-with-nano-banana-pro-2026) · [Ultimate Nano Banana Pro Prompting Guide 2026 — Atlabs](https://www.atlabs.ai/blog/the-ultimate-nano-banana-pro-prompting-guide-mastering-gemini-3-pro-image)

### 2.4 Pseudo-Code Prompting (Pro Only)

Nano Banana Pro's reasoning engine recognizes structured logic. Instead of writing paragraphs, break your request into defined variables — like writing a creative brief in pseudo-code:

```
SCENE: Product photography setup
SUBJECT: Matte black wireless headphones
SURFACE: Polished marble table
BACKGROUND: Gradient from charcoal to soft grey
LIGHTING: Key light from upper left at 45°, soft fill from right
CAMERA: Canon EOS R5, 85mm f/1.8, eye-level
STYLE: Clean, minimal, luxury brand aesthetic
TEXT: "SoundWave Pro" in white sans-serif, upper right corner
CONSTRAINTS: No reflections. No props. Aspect ratio 4:5.
```

This approach achieves high consistency because each variable is isolated and the model can reason about them independently.

**Source:** [Nano Banana Pro High-Control Prompting — Higgsfield](https://higgsfield.ai/nano-banana-pro-prompt-guide) · [How to Prompt Nano Banana Pro — fofr.ai](https://www.fofr.ai/nano-banana-pro-guide)

### 2.5 Work Surface Approach (Pro Only)

For complex layouts like infographics, posters, or multi-element designs, think in terms of surfaces:

```
WORK SURFACE: A4 vertical poster
LAYOUT:
  - Header zone (top 15%): Title text
  - Hero zone (middle 50%): Main visual
  - Data zone (bottom 25%): 3-column stats
  - Footer zone (bottom 10%): Logo and URL
COMPONENTS:
  - Title: "2025 Climate Report" in bold serif, dark blue
  - Hero: Satellite view of melting ice shelf
  - Stats: Three circular charts showing temperature, CO2, sea level
  - Logo: [reference image provided]
STYLE: Scientific publication, clean, authoritative
COLOR PALETTE: Navy (#1a2744), white, ice blue (#b8d4e3)
```

**Source:** [Nano Banana Pro Complete Guide — AImage](https://aimage.ai/blog/nano-banana-pro-complete-guide-part-1-golden-rules-and-core-features) · [Google's 10 Golden Rules — Atlabs](https://www.atlabs.ai/blog/master-professional-ai-asset-creation-google%E2%80%99s-10-golden-rules-for-nano-banana-pro)

---

## Part 3: Advanced Techniques

### 3.1 Camera & Lens Specifications

Nano Banana Pro understands photography language. Specifying lens and camera settings controls depth of field, perspective distortion, and overall feel:

| Spec | What it controls | Example values |
|---|---|---|
| **Focal length** | Compression, perspective | 24mm (wide), 50mm (natural), 85mm (portrait), 200mm (compressed) |
| **Aperture** | Depth of field | f/1.4 (blurry bg), f/8 (sharp throughout), f/16 (everything sharp) |
| **Camera body** | Overall aesthetic | "Sony A7R V" (sharp), "Hasselblad 500C" (medium format), "iPhone 15 Pro" (mobile) |
| **Lens type** | Character | "anamorphic lens" (cinematic flare), "tilt-shift" (miniature effect), "macro lens" (extreme close-up) |

**Pro tip:** Combine with lighting: "Shot on Canon EOS R5 with 85mm f/1.4, Rembrandt lighting, golden hour sidelight."

**Source:** [Advanced Camera Angle Prompts — Sider](https://sider.ai/blog/ai-image/advanced-camera-angle-prompts-for-nano-banana-pro) · [Cinematic AI Prompting — SabbirZ](https://www.sabbirz.com/blog/cinematic-ai-prompting-for-nano-banana-the-complete-guide-to-camera-angles)

### 3.2 Text Rendering

Nano Banana Pro has breakthrough text rendering. To maximize accuracy:

1. **Use double quotation marks** around exact text: `The poster reads "SUMMER SALE 2026"`
2. **Keep text short** — under 25 characters for highest accuracy
3. **Specify font characteristics** — "bold sans-serif in white" beats just specifying the text
4. **Use a 3-level hierarchy** — title (large), subtitle (medium), body (small)
5. **Position explicitly** — "centered at the top" or "lower right corner"

**What doesn't work:** Long paragraphs, multiple text blocks with different fonts, text that wraps across lines unpredictably.

**Source:** [47 Hours Testing Text Rendering — HumAI Blog](https://www.humai.blog/i-spent-47-hours-testing-nano-banana-pros-text-rendering-for-infographics-heres-everything-i-learned-and-what-nobody-tells-you/) · [Typography Guide — PerfectCorp](https://www.perfectcorp.com/consumer/blog/generative-AI/nano-banana-ai-typography-guide)

### 3.3 Multi-Image References (Pro — 14-Image Context)

Nano Banana Pro accepts up to 14 reference images in a single prompt. This enables:

- **Brand consistency:** Upload logo, color palette, and previous assets
- **Character consistency:** Upload a character sheet and request new poses/scenes
- **Style transfer:** Upload reference images and say "Match this visual style exactly"
- **Composite requests:** "Use the character from Image 1, the background from Image 2, and the color palette from Image 3"

**Best practice:** Upload the most important reference as Image 1 — the model weights earlier images more heavily.

**Source:** [Multi-Reference 14 Images Guide — Apatero](https://apatero.com/blog/nano-banana-pro-multi-reference-14-images-5-faces-guide-2025) · [Character Consistency Cheat Sheet — Sider](https://sider.ai/blog/ai-image/nano-banana-pro-cheat-sheet-for-character-consistency)

### 3.4 Search Grounding (Pro Only)

Nano Banana Pro can connect to Google Search to generate factually accurate visuals. Enable this when creating:

- Diagrams of real-world processes
- Infographics with current data
- Visualizations of real places, buildings, or products
- Educational content requiring accuracy

**How to invoke:** Include a factual claim or request for real-world accuracy in your prompt. The model automatically decides when to ground via search.

**Reported accuracy improvement:** 32% better factual accuracy with search grounding enabled.

**Source:** [Search Grounding Practice — APIYi](https://help.apiyi.com/nano-banana-pro-search-grounding-realtime-news-generation-guide-en.html)

### 3.5 Negative Prompting (Semantic Negation)

Since there's no dedicated negative prompt parameter, use in-prompt semantic negatives:

```
[Your positive prompt here].
No extra fingers or hands. No text except the title.
Avoid watermarks. No busy background. No lens flare.
```

**Rule of thumb:** Keep negative prompts to 10-20 tokens. Too many negatives confuse the model.

**Source:** [How to Write Negative Prompts — Sider](https://sider.ai/blog/ai-image/how-to-write-negative-prompts-in-nano-banana-a-practical-guide) · [Best Practices — Skywork](https://skywork.ai/blog/nano-banana-gemini-prompt-engineering-best-practices-2025/)

### 3.6 Style Blending

Combine artistic styles using transition words:

- "Oil painting **meets** cyberpunk neon"
- "Studio Ghibli aesthetic **combined with** architectural blueprint"
- "Watercolor **mixed with** photorealistic rendering"

The model understands these as blend instructions and creates hybrid styles.

### 3.7 Brand Consistency System

For teams generating multiple assets, use a brand style system:

```
BRAND SYSTEM: [Brand Name]
PRIMARY COLORS: #1a2744 (navy), #f0c040 (gold), #ffffff (white)
TYPOGRAPHY: Bold sans-serif headers, light sans-serif body
MOOD: Professional, warm, trustworthy
PHOTOGRAPHY STYLE: Natural lighting, warm tones, shallow DoF
FORBIDDEN: Neon colors, dark backgrounds, script fonts
MASCOT/CHARACTER: [reference image uploaded]
```

Include this system prefix before every generation prompt to maintain consistency across an entire campaign.

**Source:** [Brand Style Prompt System — Skywork](https://skywork.ai/blog/nano-banana-brand-style-prompt-system-for-consistent-design/)

---

## Part 4: The Iteration Engine

### 4.1 The Brief → Generate → Inspect → Constrain Loop

The professional workflow follows four steps:

1. **Brief** — Write the modular prompt using any framework from Part 2
2. **Generate** — Produce 1-2 candidates
3. **Inspect** — Evaluate against the brief. What's right? What's wrong?
4. **Constrain/Isolate** — Change ONE variable to fix the biggest issue

**Critical rule:** Never change more than one variable per iteration. If you change lighting AND composition AND style, you lose the ability to learn what worked.

### 4.2 Conversational Editing (Multi-Turn)

Nano Banana supports iterative, conversational refinement. After generating an initial image:

- "Make the lighting warmer and more golden"
- "Move the text to the lower right corner"
- "Remove the background elements and make it plain white"
- "Keep everything the same but change the outfit to business casual"

Each instruction builds on the previous output without starting from scratch.

### 4.3 A/B Testing for Optimization

For marketing and content use cases, run systematic A/B tests:

1. Generate the same subject with 3 different lighting setups
2. Generate the same scene with 3 different compositions
3. Generate the same product with 3 different backgrounds
4. Test the variants on your audience (CTR, engagement, conversion)

Reported results: 40% CTR improvement from systematic prompt A/B testing.

**Source:** [Nano Banana A/B Testing for Higher CTR — Skywork](https://skywork.ai/blog/nano-banana-prompt-a-b-testing-for-higher-ctr/)

---

## Part 5: Operator-Level Integration

### 5.1 API Access

Nano Banana is accessible via:

| Platform | Model String | Best for |
|---|---|---|
| **Google AI Studio** | `gemini-2.5-flash-image` | Prototyping, testing |
| **Gemini API** | `gemini-2.5-flash-image-preview` | Production applications |
| **Vertex AI** | `gemini-2.5-flash-image` | Enterprise, compliance |
| **Nano Banana Pro** | `gemini-3-pro-image-preview` | Advanced features |

**API documentation:** [Gemini API Image Generation](https://ai.google.dev/gemini-api/docs/image-generation) · [Vertex AI Docs](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash-image)

### 5.2 Pricing & Quotas

The free tier provides limited daily generations. API pricing scales per image. Third-party providers (Fal.ai, Kie.ai) offer discounted rates — up to 50-79% savings via batch processing.

**Key operator consideration:** Batch API processing offers significant discounts. If generating 50+ images, always use batch mode.

**Source:** [API Pricing Guide — AIFreeAPI](https://www.aifreeapi.com/en/posts/nano-banana-pro-api-pricing) · [Batch Automation Guide — Skywork](https://skywork.ai/blog/nano-banana-api-pricing-and-batch-automation-guide/)

### 5.3 JSON-Structured Prompts (API)

For programmatic use, JSON-structured prompts achieve 92% better precision than natural language:

```json
{
  "subject": {
    "type": "product",
    "item": "matte black wireless headphones",
    "position": "centered on surface"
  },
  "environment": {
    "surface": "polished marble",
    "background": "gradient charcoal to grey",
    "lighting": "studio key light, upper left 45°"
  },
  "camera": {
    "body": "Canon EOS R5",
    "lens": "85mm f/1.8",
    "angle": "eye level",
    "composition": "rule of thirds"
  },
  "style": "luxury product photography",
  "constraints": {
    "aspect_ratio": "4:5",
    "text": null,
    "exclusions": ["reflections", "props"]
  }
}
```

**Source:** [JSON Prompt Format Guide — AI For Marketings](https://aiformarketings.com/blog/nano-banana-json-guide/) · [GitHub JSON Schema Gist](https://gist.github.com/alexewerlof/1d13401a7647339469141dc2960e66a9)

### 5.4 Automation Workflows

Nano Banana integrates with major automation platforms:

| Platform | Use Case | Source |
|---|---|---|
| **n8n** | Viral ad creation → social media publishing | [n8n Workflow](https://n8n.io/workflows/8428-create-viral-ads-with-ai-nanobanana-and-publish-on-socials-via-upload-post/) |
| **n8n** | Telegram bot → image generation → social posting | [n8n Telegram Workflow](https://n8n.io/workflows/11765-generate-ai-images-with-telegram-bot-and-auto-publish-to-social-media-using-nano-banana-pro/) |
| **Adobe Firefly** | Generative Fill in Photoshop | [Adobe Integration](https://blog.adobe.com/en/publish/2025/11/20/google-gemini-3-nano-banana-pro-firefly-photoshop) |
| **Figma** | UI/UX mockup generation plugin | [Figma Plugin](https://www.figma.com/community/plugin/1549333261761511637/nano-banana-pro-ai-figma-plugin-for-ai-image-generation-ad-creatives-ui-ux-mockups) |
| **Canva** | No-code image editing workflow | [Canva + Nano Banana](https://www.aifire.co/p/a-no-code-workflow-for-ai-image-editing-canva-nano-banana) |

### 5.5 Safety Filters & Content Policies

Nano Banana enforces content safety policies. Images are tagged with SynthID (invisible watermark) for AI provenance. Some generations may include a visible watermark depending on the platform and plan.

Key restrictions: The model won't generate photorealistic faces of real public figures, explicit content, or content that could be used for deception. Enterprise customers on Vertex AI have additional compliance controls.

**Source:** [Brand Safety Checklist — Skywork](https://skywork.ai/blog/nano-banana-brand-safety-and-ad-approval-checklist/) · [Watermark Guide — AIFreeAPI](https://www.aifreeapi.com/en/posts/nano-banana-pro-watermark-commercial-use)

---

## Part 6: Template Patterns by Use Case

### 6.1 Product Photography

```
A [PRODUCT] photographed in a [SETTING] studio setup.
[SURFACE] beneath, [BACKGROUND] behind.
[LIGHTING TYPE] from [DIRECTION].
Shot on [CAMERA], [LENS], [APERTURE].
[STYLE] aesthetic. No text. Aspect ratio [RATIO].
```

**Example:**
```
A ceramic coffee mug photographed in a minimalist studio setup.
Light oak wood surface beneath, cream gradient background behind.
Soft diffused lighting from upper left.
Shot on Hasselblad X2D, 80mm f/2.8.
Scandinavian design aesthetic. No text. Aspect ratio 4:5.
```

**Source:** [25 Product Photo Prompts — Skywork](https://skywork.ai/blog/nano-banana-product-photo-prompts-2025/)

### 6.2 Social Media Content

```
A [CONTENT TYPE] for [PLATFORM].
Subject: [DESCRIPTION].
Style: [VISUAL STYLE], [COLOR SCHEME].
Text: "[HEADLINE]" in [FONT STYLE], [POSITION].
Aspect ratio: [PLATFORM-SPECIFIC RATIO].
Brand colors: [HEX CODES].
```

**Platform ratios:** Instagram Feed (1:1), Instagram Story (9:16), LinkedIn (1.91:1), Twitter/X (16:9), YouTube Thumbnail (16:9)

### 6.3 Infographic

```
WORK SURFACE: [SIZE] [ORIENTATION] infographic
TITLE: "[TITLE]" in [FONT], [COLOR]
LAYOUT:
  - Header (top 10%): Title and subtitle
  - Section 1 (20%): [CONTENT] with [ICON/CHART TYPE]
  - Section 2 (20%): [CONTENT] with [ICON/CHART TYPE]
  - Section 3 (20%): [CONTENT] with [ICON/CHART TYPE]
  - Section 4 (20%): [CONTENT] with [ICON/CHART TYPE]
  - Footer (10%): Source attribution and logo
STYLE: [DESIGN STYLE]
COLOR PALETTE: [3-4 HEX CODES]
```

**Source:** [30 Infographic Prompts — Atlabs](https://www.atlabs.ai/blog/30-nano-banana-prompts-for-perfect-infographics-ultimate-infographic-lookbook)

### 6.4 UI/UX Mockup

```
A [DEVICE] screen showing a [APP TYPE] interface.
Screen: [SCREEN NAME/PURPOSE].
Layout: [LAYOUT DESCRIPTION].
Elements: [KEY UI ELEMENTS].
Style: [DESIGN SYSTEM], [COLOR THEME].
Font: [FONT STYLE].
Aspect ratio: [DEVICE RATIO].
```

**Source:** [UI Design with Nano Banana Pro — Raw Studio](https://raw.studio/blog/ui-design-with-nano-banana-pro-practical-use-cases-workflow-and-sample-prompts/) · [UX Planet Analysis](https://uxplanet.org/ui-design-with-nano-banana-pro-51aa803457d5)

### 6.5 Architecture / Interior Design

```
A [STYLE] [SPACE TYPE] with [KEY DESIGN ELEMENTS].
Materials: [FLOORING], [WALLS], [FURNITURE MATERIAL].
Lighting: [NATURAL/ARTIFICIAL], [TIME OF DAY].
Color palette: [WARM/COOL/NEUTRAL], [SPECIFIC COLORS].
View: [PERSPECTIVE TYPE], [CAMERA POSITION].
Style: [RENDER STYLE — photorealistic/watercolor/sketch].
Aspect ratio: 16:9.
```

**Source:** [Nano Banana for Architects — MyArchitectAI](https://www.myarchitectai.com/blog/nano-banana-for-architects) · [Interior Design Guide — CGWisdom](https://cgwisdom.com/blog/nano-banana-pro-in-interior-design-a-complete-guide-with-ready-made-prompts.html)

### 6.6 Character Sheet (Consistency)

```
A character reference sheet for [CHARACTER DESCRIPTION].
Show: front view, 3/4 view, side profile, back view.
Expression: [NEUTRAL/SMILING/SERIOUS].
Outfit: [DETAILED CLOTHING DESCRIPTION].
Style: [ART STYLE].
Background: plain white.
Consistent proportions across all views.
Label each view. Aspect ratio 16:9.
```

**Source:** [Character Consistency Cheat Sheet — Sider](https://sider.ai/blog/ai-image/nano-banana-pro-cheat-sheet-for-character-consistency) · [60+ Portrait Prompts — Filmora](https://filmora.wondershare.com/ai-prompt/gempix-2-prompts.html)

### 6.7 YouTube Thumbnail

```
A YouTube thumbnail for a video about [TOPIC].
Main visual: [SUBJECT with EXPRESSION/ACTION].
Background: [CONTRASTING, HIGH-ENERGY BACKGROUND].
Text: "[2-4 WORD HEADLINE]" in [BOLD, LARGE FONT], [COLOR].
Style: High contrast, saturated colors, dramatic.
Expression: [SURPRISED/EXCITED/INTENSE].
Aspect ratio: 16:9.
```

**Source:** [10 Thumbnail Templates — Skywork](https://skywork.ai/blog/youtube-thumbnail-templates-nano-banana-prompts-2025/)

### 6.8 Logo Design

```
A [LOGO TYPE] logo for [BRAND NAME].
Concept: [SYMBOL/ICON DESCRIPTION].
Style: [MINIMAL/VINTAGE/MODERN/GEOMETRIC].
Colors: [PRIMARY COLOR] on [BACKGROUND COLOR].
Text: "[BRAND NAME]" in [FONT STYLE].
Clean lines, scalable, professional.
Background: transparent/white.
Aspect ratio: 1:1.
```

**Source:** [Logo Design Prompts — LogoAI](https://www.logoai.com/design/blog/50-nano-banana-pro-prompts)

### 6.9 Food Photography

```
A [DISH/FOOD ITEM] styled for [CONTEXT].
Plating: [DESCRIPTION].
Props: [UTENSILS, GARNISH, SURFACE].
Lighting: [NATURAL/STUDIO], [DIRECTION].
Mood: [WARM/FRESH/RUSTIC/LUXURIOUS].
Shot on [CAMERA], overhead/45-degree angle.
Style: [EDITORIAL/COMMERCIAL/SOCIAL].
No text. Aspect ratio [RATIO].
```

**Source:** [Hyper-Realistic Food Photography — Sider](https://sider.ai/blog/ai-image/hyper-realistic-food-photography-prompts-with-nano-banana-pro)

### 6.10 Real Estate Virtual Staging

```
A [ROOM TYPE] staged with [STYLE] furniture.
Room features: [EXISTING ARCHITECTURAL ELEMENTS].
Furniture: [SPECIFIC PIECES AND PLACEMENT].
Flooring: [MATERIAL].
Lighting: [NATURAL from WINDOW POSITION].
Color scheme: [PALETTE].
Style: Real estate listing photography, bright and inviting.
Aspect ratio: 16:9.
```

**Source:** [Virtual Staging Tutorial — BananaDesigner](https://www.bananadesigner.com/pages/usecase/realestate/virtual-staging-tutorial) · [Real Estate Marketing — ThePaperlessAgent](https://thepaperlessagent.com/blog/googles-nano-banana-ai-game-changer-for-real-estate-marketing/)

---

## Part 7: Decision Trees for Operators

### 7.1 Model Selection

```
START → Does the image need precise text rendering?
  YES → Use Pro
  NO → Does it need complex layout (infographic, diagram)?
    YES → Use Pro
    NO → Does it need multi-image references?
      YES → Use Pro
      NO → Is speed/cost the priority?
        YES → Use Flash
        NO → Is quality the priority?
          YES → Use Pro
          NO → Use Flash (default)
```

### 7.2 Prompt Framework Selection

```
START → What are you generating?
  SIMPLE IMAGE (portrait, product, scene) → Standard Formula (2.1)
  COMPLEX LAYOUT (infographic, poster, diagram) → Work Surface (2.5)
  BRANDED CONTENT (campaign, series) → Brand System (3.7) + Pseudo-Code (2.4)
  API/AUTOMATION → JSON Structure (5.3)
  QUICK EXPLORATION → 5-Input System (2.3)
```

### 7.3 Troubleshooting

| Problem | Fix |
|---|---|
| Distorted hands/fingers | Add "anatomically correct hands" + specify hand position |
| Wrong text rendered | Use double quotes, keep under 25 chars, specify font |
| Style inconsistency | Use Brand System prefix + reference images |
| Too busy/cluttered | Add more constraints, use "clean" and "minimal" |
| Colors are off | Specify exact hex codes in prompt |
| Wrong aspect ratio | Always specify explicitly |
| Content safety block | Review prompt for restricted content, rephrase |

**Source:** [Fixing Distorted Hands — Sider](https://sider.ai/blog/ai-image/fixing-distorted-hands-in-nano-banana-prompts-a-practical-guide) · [Fix Common Issues — Dzine](https://www.dzine.ai/blog/fix-nano-banana-pro-issues/)

---

## Part 8: Competitive Landscape

### 8.1 When to Use What

| Model | Best for | Weakness |
|---|---|---|
| **Nano Banana (Flash)** | Speed, quick edits, high volume | Less precise on text, complex layouts |
| **Nano Banana Pro** | Text, infographics, brand consistency, complex scenes | Slower, more expensive |
| **Midjourney v7** | Artistic quality, aesthetic beauty | Less text rendering, no API (Discord-based) |
| **DALL-E 3** | ChatGPT integration, ease of use | Less photorealistic, fewer controls |
| **Flux** | Open source, customization, fine-tuning | Requires technical setup |
| **Stable Diffusion 3** | Local deployment, privacy, customization | Complex setup, less user-friendly |
| **Imagen 4** | Google ecosystem integration | Less community support |

**Source:** [Nano Banana vs Midjourney vs DALL-E — Skywork](https://skywork.ai/blog/nano-banana-vs-midjourney-vs-dalle-2025-comparison/) · [50+ Prompt Test Comparison — Spectrum AI Lab](https://spectrumailab.com/blog/nano-banana-pro-vs-midjourney-vs-dalle-3-comparison-2025)

---

## Appendix A: Curated Source Library (500+ Sources)

### Official Google Sources

1. [How Nano Banana Got Its Name — Google Blog](https://blog.google/products-and-platforms/products/gemini/how-nano-banana-got-its-name/)
2. [Gemini 2.5 Flash Image — Google DeepMind](https://deepmind.google/models/gemini-image/flash/)
3. [Gemini 3 Pro Image — Google DeepMind](https://deepmind.google/models/gemini-image/pro/)
4. [Nano Banana Pro Announcement — Google Blog](https://blog.google/technology/ai/nano-banana-pro/)
5. [Prompting Tips for Nano Banana Pro — Google Blog](https://blog.google/products/gemini/prompting-tips-nano-banana-pro/)
6. [Gemini API Image Generation Docs](https://ai.google.dev/gemini-api/docs/image-generation)
7. [Vertex AI Gemini 2.5 Flash Image Docs](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash-image)
8. [Vertex AI Gemini 3 Pro Image Docs](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/3-pro-image)
9. [Google AI Studio — Nano Banana Pro](https://aistudio.google.com/models/gemini-3-pro-image)
10. [Gemini 2.5 Flash Model Card (PDF)](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-2-5-Flash-Model-Card.pdf)
11. [Nano Banana Pro for Enterprise — Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/nano-banana-pro-available-for-enterprise)
12. [Google Workspace Nano Banana Pro Integration](https://workspaceupdates.googleblog.com/2025/11/workspace-nano-banana-pro.html)
13. [Google Codelab: Consistent Imagery with Nano Banana](https://codelabs.developers.google.com/gemini-consistent-imagery-notebook)
14. [Nano Banana Hackathon Kit — GitHub](https://github.com/google-gemini/nano-banana-hackathon-kit)
15. [Veo 3 + Nano Banana API Quickstart — GitHub](https://github.com/google-gemini/veo-3-nano-banana-gemini-api-quickstart)

### Expert Practitioner Sources

16. [Max Woolf — Nano Banana Prompt Engineering](https://minimaxir.com/2025/11/nano-banana-prompts/)
17. [Max Woolf — Nano Banana Pro Review](https://minimaxir.com/2025/12/nano-banana-pro/)
18. [Simon Willison — Nano Banana Can Be Prompt Engineered](https://simonwillison.net/2025/Nov/13/nano-banana-can-be-prompt-engineered/)
19. [Chase Jarvis — Professional's Guide to AI Image Mastery](https://chasejarvis.com/blog/nano-banana-prompts/)
20. [Chase Jarvis — Nano Banana Pricing Analysis](https://chasejarvis.com/blog/nano-banana-pricing/)
21. [Chase Jarvis — Style Cloning with Nano Banana Pro](https://chasejarvis.com/blog/how-to-clone-any-image-style-with-nano-banana-pro-weavy-style-transfer/)

### Comprehensive Guides

22. [Ultimate Nano Banana Prompting Guide — Atlabs](https://www.atlabs.ai/blog/nano-banana-prompting-guide)
23. [Ultimate Nano Banana Pro Prompting Guide 2026 — Atlabs](https://www.atlabs.ai/blog/the-ultimate-nano-banana-pro-prompting-guide-mastering-gemini-3-pro-image)
24. [30 Infographic Prompts — Atlabs](https://www.atlabs.ai/blog/30-nano-banana-prompts-for-perfect-infographics-ultimate-infographic-lookbook)
25. [90 Best Nano Banana Prompts — Atlabs](https://www.atlabs.ai/blog/90-best-nano-banana-prompts-the-only-ultimate-prompt-guide-you-will-need-for-nano-banana)
26. [Leonardo.ai Prompt Guide](https://leonardo.ai/news/nano-banana-prompt-guide/)
27. [Imagine.art Prompting Guide + 75 Prompts](https://www.imagine.art/blogs/nano-banana-pro-prompt-guide)
28. [Higgsfield High-Control Prompting](https://higgsfield.ai/nano-banana-pro-prompt-guide)
29. [KDnuggets Practical Guide](https://www.kdnuggets.com/nano-banana-practical-prompting-usage-guide)
30. [Prompt Engineering Best Practices — Skywork](https://skywork.ai/blog/ai-image/prompt-engineering-best-practices-nano-banana-pro-2025/)

### GitHub Repositories & Prompt Libraries

31. [awesome-nano-banana-pro-prompts (8000+ prompts) — YouMind-OpenLab](https://github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts)
32. [awesome-nanobanana-pro — ZeroLu](https://github.com/ZeroLu/awesome-nanobanana-pro)
33. [nanobananaprompt.org — Ultimate Prompt Library](https://nanobananaprompt.org/)
34. [nanoprompts.org — 400+ Free Prompts](https://nanoprompts.org/)
35. [JSON Prompt Schema Gist](https://gist.github.com/alexewerlof/1d13401a7647339469141dc2960e66a9)

### Academic & Research Papers

36. [Is Nano Banana Pro a Low-Level Vision All-Rounder? — arXiv](https://arxiv.org/abs/2512.15110)
37. [Pico-Banana-400K Dataset — arXiv](https://arxiv.org/abs/2510.19808)
38. [PaperBanana: Automating Academic Illustration — arXiv](https://arxiv.org/abs/2601.23265)
39. [Autoregressive Model Beats Diffusion — arXiv](https://arxiv.org/abs/2406.06525)

### Specialized Domain Guides

40. [Architecture — MyArchitectAI](https://www.myarchitectai.com/blog/nano-banana-for-architects)
41. [Interior Design — CGWisdom](https://cgwisdom.com/blog/nano-banana-pro-in-interior-design-a-complete-guide-with-ready-made-prompts.html)
42. [Food Photography — Sider](https://sider.ai/blog/ai-image/hyper-realistic-food-photography-prompts-with-nano-banana-pro)
43. [Fashion — Skywork](https://skywork.ai/blog/nano-bananas-aesthetic-intelligence-from-outfit-generation-to-styling-how-it-redefines-fashion-ai/)
44. [Fashion Lookbooks — Fibre2Fashion](https://emerge.fibre2fashion.com/blogs/10806/best-nano-banana-prompt-formulas-for-apparel-lookbooks-catalog-shots-and-campaign-banners)
45. [UI/UX Mockups — Raw Studio](https://raw.studio/blog/ui-design-with-nano-banana-pro-practical-use-cases-workflow-and-sample-prompts/)
46. [UI Design — UX Planet](https://uxplanet.org/ui-design-with-nano-banana-pro-51aa803457d5)
47. [Game Assets — APIYi](https://help.apiyi.com/nano-banana-pro-game-assets-generation-en.html)
48. [Comic/Manga — Medium](https://medium.com/@todasco/nano-banana-pro-can-make-a-comic-book-9def1e4736e0)
49. [Storyboarding — APIYi](https://help.apiyi.com/nano-banana-pro-storyboard-generation-guide-en.html)
50. [Real Estate Virtual Staging — BananaDesigner](https://www.bananadesigner.com/pages/usecase/realestate/virtual-staging-tutorial)

### Comparison & Benchmarking

51. [Nano Banana vs Midjourney vs DALL-E — Skywork](https://skywork.ai/blog/nano-banana-vs-midjourney-vs-dalle-2025-comparison/)
52. [50+ Prompt Test — Spectrum AI Lab](https://spectrumailab.com/blog/nano-banana-pro-vs-midjourney-vs-dalle-3-comparison-2025)
53. [Nano Banana vs Stable Diffusion — Sider](https://sider.ai/blog/ai-image/nano-banana-stable-diffusion)
54. [Nano Banana vs DALL-E 3 — WaveSpeed](https://wavespeed.ai/blog/posts/nano-banana-pro-vs-dalle-3-comparison/)
55. [Complete AI Image Comparison — Medium](https://medium.com/@inchristiely/ai-image-model-comparison-2025-midjourney-vs-chatgpt-vs-flux-vs-imagen-vs-nano-banana-9db41af5ef7a)

### API & Developer Resources

56. [Gemini API Docs](https://ai.google.dev/gemini-api/docs/image-generation)
57. [Fal.ai Nano Banana Pro API](https://fal.ai/models/fal-ai/nano-banana-pro/api)
58. [Kie.ai Cost-Effective API](https://kie.ai/nano-banana-pro)
59. [FreeCodeCamp Code Examples](https://www.freecodecamp.org/news/nano-banana-for-image-generation/)
60. [Codecademy Tutorial](https://www.codecademy.com/article/nano-banana-pro-tutorial)

### Automation & Workflow

61. [n8n — Viral Ads + Social Publishing](https://n8n.io/workflows/8428-create-viral-ads-with-ai-nanobanana-and-publish-on-socials-via-upload-post/)
62. [n8n — Telegram Bot + Social Media](https://n8n.io/workflows/11765-generate-ai-images-with-telegram-bot-and-auto-publish-to-social-media-using-nano-banana-pro/)
63. [n8n — VEO3 Video + Social](https://n8n.io/workflows/8270-generate-ai-viral-videos-with-nanobanana-and-veo3-shared-on-socials-via-blotato/)
64. [Adobe Firefly Integration](https://blog.adobe.com/en/publish/2025/11/20/google-gemini-3-nano-banana-pro-firefly-photoshop)
65. [Figma Plugin](https://www.figma.com/community/plugin/1549333261761511637/)
66. [Canva No-Code Workflow — AIFire](https://www.aifire.co/p/a-no-code-workflow-for-ai-image-editing-canva-nano-banana)

### Troubleshooting & Optimization

67. [Common Mistakes — UseNanoBanana](https://usenanobanana.com/blog/5-common-mistakes-troubleshooting)
68. [Fix Common Issues — Dzine](https://www.dzine.ai/blog/fix-nano-banana-pro-issues/)
69. [Error Codes Guide — LaoZhang](https://blog.laozhang.ai/en/posts/nano-banana-pro-troubleshooting-debugging)
70. [Fixing Distorted Hands — Sider](https://sider.ai/blog/ai-image/fixing-distorted-hands-in-nano-banana-prompts-a-practical-guide)

### Community & Learning

71. [Wikipedia — Nano Banana](https://en.wikipedia.org/wiki/Nano_Banana)
72. [DataCamp Tutorial](https://www.datacamp.com/tutorial/nano-banana-pro)
73. [Skillshare Course — Video Creation](https://www.skillshare.com/en/classes/gemini-3-nano-banana-veo-3-1-master-ai-video-creation/1955529291)
74. [Futurepedia Course — Create & Edit](https://www.futurepedia.io/courses/google-nano-banana-create-and-edit-in-minutes/)
75. [Egghead — Batch Generation Scripting](https://egghead.io/batch-generate-nano-banana-variations-with-ai-studio-and-scripting~ks0vr)

*Note: The complete source index exceeds 500 entries. The remaining 425+ sources are cataloged in the research scratchpad at `pipeline/scratchpad/2026-02-21-nano-banana-prompting-research-scratchpad.md` and cover product photography (50+), social media (40+), branding (35+), infographics (30+), character design (25+), architecture (20+), food photography (15+), real estate (15+), fashion (20+), UI/UX (20+), education (15+), video/thumbnails (20+), comparisons (25+), pricing (15+), ethics (10+), batch processing (15+), and community resources (30+).*

---

## Appendix B: Agent Skill Conversion Notes

This study guide is designed to be converted into an agent skill. Key conversion points:

**Prompt templates (Part 6)** can be parameterized directly — each `[PLACEHOLDER]` becomes an input variable.

**Decision trees (Part 7)** translate into conditional logic for model selection and framework routing.

**The Brand System (3.7)** becomes a persistent context that prefixes every generation request.

**The iteration engine (Part 4)** becomes a loop with inspection checkpoints.

**JSON structure (5.3)** is already API-ready for programmatic generation.

**Suggested skill structure:**
```
nano-banana-skill/
  SKILL.md           ← This guide, condensed to essential patterns
  templates/
    product-photo.md
    social-media.md
    infographic.md
    ui-mockup.md
    character-sheet.md
    thumbnail.md
    logo.md
    food-photo.md
    virtual-staging.md
  prompts/
    brand-system-prefix.md
    json-structure.md
  decision-trees/
    model-selection.md
    framework-selection.md
    troubleshooting.md
```

---

## Appendix C: Learning Path

**Week 1: Foundations (4 hours)**
- Read Parts 1-2 of this guide
- Generate 20 images using the Standard Formula
- Try each framework variant (pseudo-code, work surface, 5-input)

**Week 2: Advanced Techniques (4 hours)**
- Read Part 3 (camera specs, text rendering, multi-image)
- Generate 10 infographics using Work Surface approach
- Create a character sheet and generate 5 consistent scenes

**Week 3: Specialization (4 hours)**
- Pick 2-3 template patterns from Part 6 relevant to your work
- Generate 20+ images in your specialty area
- Run A/B tests on 3 prompt variants

**Week 4: Automation (4 hours)**
- Set up API access (Google AI Studio or Vertex AI)
- Build one automation workflow (n8n or direct API)
- Create a brand system for a real project
- Convert your best prompts into JSON templates

---

<metadata>
purpose: Comprehensive operator guide for Nano Banana (Google Gemini image generation) prompting
audience: AI operators, creative directors, content creators, automation builders
domain: product, AI, image generation
confidence: high
last_updated: 2026-02-21
related_files:
  - pipeline/scratchpad/2026-02-21-nano-banana-prompting-research-scratchpad.md
  - knowledge/product/nano-banana-prompting-study-guide-v1.md
</metadata>
