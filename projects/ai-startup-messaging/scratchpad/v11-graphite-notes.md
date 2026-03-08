# V11 (Graphite-Inspired) — Improvement Notes

Version 11 borrows Graphite's messaging architecture well in spots — the generational framing, the outcome headlines, the exclusivity arc. But it misses several things Graphite does that make the page actually convert, and it dilutes its own best lines with redundancy and abstraction.

---

## 1. What Graphite Does Well That V11 Misses

### A. The title tag and hero are two separate moves

Graphite's title tag says "Code review for the age of AI" — that's the era frame. The hero says "The next generation of code review" — that's the generational claim. Two distinct beats. V11 buries "Website growth for the age of AI" in the *seventh section* of the page, long after most readers have made a judgment. The era frame should be the first thing someone reads (page title / meta), not a section header near the bottom.

### B. The category is named clearly and immediately

Graphite's sub-hero says "Graphite is the **AI code review platform**" — five words, crystal clear category. V11 says "GrowthX is the **AI growth platform**" which could mean anything. Growth hacking tool? Analytics dashboard? Ad optimizer? "AI growth platform" doesn't name a category anyone recognizes. Graphite succeeds because "code review" is a category every developer already uses. GrowthX needs the same clarity.

### C. Real social proof with specific velocity metrics

Graphite's case study carousel has:
- "Ramp ships code 3x faster"
- "Asana engineers save 7 hours per week"
- "How Shopify scaled their developer productivity"

Every proof point is a named company plus a speed metric. V11 has *zero named clients, zero metrics, zero case studies*. The trust bar says "Trusted by companies that don't wait for growth to happen" — which is an attitude statement, not proof. Graphite proves speed. V11 asserts it.

### D. A video that shows the product

Graphite puts a product video thumbnail directly below the hero. It's visual proof that the thing exists and works. V11 is entirely text. For a company selling a platform, the absence of any visual is a credibility gap.

### E. Friction removal is placed directly under the CTA

Graphite's "Free for your first 30 days. No credit card required. Synced with your GitHub account." sits immediately under the signup button — three objections killed at the moment of decision. V11's friction removal ("Start with a free growth audit. No commitment. No contract. Results in two weeks.") is placed as a third line in the hero, but it's not anchored to a CTA button. It floats.

### F. One feature architecture, not two

Graphite has outcome feature cards, then a "Everything you need to ship faster" grid — but the grid *expands on* the cards with detail, screenshots, and new content. V11 has outcome feature cards AND a feature grid AND an infrastructure section that all say overlapping things. The page argues with itself.

---

## 2. Weak Spots

### The category name

> "GrowthX is the AI growth platform where companies ship higher-performing content, faster — and compound the results every quarter."

"AI growth platform" is a nothing category. Nobody searches for it, nobody budgets for it, nobody has a line item for it. The sub-hero then tries to do too much — "ship higher-performing content" + "faster" + "compound the results every quarter" is three promises crammed into one sentence. Graphite's sub-hero makes one promise: "higher quality code, faster." Period.

### The trust bar is empty

> "Trusted by companies that don't wait for growth to happen."

This is a vibe, not a proof point. Without logos (Webflow, Abnormal AI, Lovable, Exec), it reads like a company that doesn't have clients worth naming. Every competitor puts logos here. Omitting them is a red flag, not a design choice.

### The feature grid reads like a spec doc

> **Full-stack growth intelligence** — Search performance, AI visibility, content health, competitive landscape. One unified signal.
> **AI content engine** — Strategy to draft to publish to optimize. Human calibration at every decision point.
> **Continuous optimization** — Decay detection. Gap analysis. Performance feedback loops.

"Full-stack growth intelligence" is enterprise jargon. "Human calibration at every decision point" is abstract. "Decay detection. Gap analysis. Performance feedback loops." — these are feature names in staccato, not outcomes. Compare to Graphite: "Don't miss a beat. Actionable Slack notifications that meet you where you are." That's an outcome + mechanism. V11's grid is all mechanism, no outcome.

### The three-audience insight is buried and reads like a brief

> "Three audiences matter now: the buyer, the AI agent, the training bot. Every piece of content is built for all three."

This is a genuinely differentiating insight — the idea that content now has three readers. But it's stuffed into a sub-bullet under an outcome card. It should be a standalone, punchy beat — possibly even part of the era framing — not an afterthought.

### The "compounding engine" section is a redundant second hero

> "The compounding AI growth engine built into your website."
> "Audit your content, ship new pages, optimize existing ones, track AI visibility — all in one system."

This reads like a second attempt at a hero headline. The page already has a hero. This section either needs to add something new (visual, proof, detail) or get cut.

### The infrastructure section makes vague claims

> "Where compounding happens. Organizations that adopt GrowthX see organic traffic accelerate."

Compare to Graphite: "Where change happens. Organizations that adopt Graphite ship more code with smaller PRs and faster review cycles." Graphite names three specific metrics (more code, smaller PRs, faster cycles). V11 names zero — "organic traffic accelerate" is not a metric, it's a hope.

### The closing CTA is soft

> "Built for the companies shaping their markets. Now available as a platform."
> "Start with a free growth audit."

Graphite's version: "Built for the world's fastest engineering teams, now available for everyone." Then dual CTAs: "Request a demo" + "Start free trial." V11's version loses the "for everyone" democratization move by saying "as a platform" — which sounds like a product launch, not an invitation. And there's only one CTA.

---

## 3. Structural Improvements

### Move the era frame to the top of the page

Use "Website growth for the age of AI" as the equivalent of a title tag / page-level positioning statement. It should appear *before or alongside* the hero headline, not buried in section 7. Suggested structure:

- **Title tag / page header:** "Website growth for the age of AI"
- **Hero headline:** "The next generation of website growth."
- **Sub-hero:** "[Category claim] + [single outcome promise]"

### Add a real trust bar with logos

Replace "Trusted by companies that don't wait for growth to happen" with "Trusted by growth teams at" + logo wall (Webflow, Abnormal AI, Lovable, Exec). If the list is short, that's fine — Graphite only shows 4-5 logos. Quality over quantity.

### Add case studies with velocity metrics

Between the trust bar and the feature cards, add 2-3 case study tiles. Each should follow Graphite's pattern: Company name + speed metric in the headline.

Example:
- "Webflow × GrowthX — How Webflow's content engine produces 4x more pages per quarter"
- "Abnormal AI × GrowthX — From 0 to 200+ indexed pages in 6 months"

If you don't have publishable case studies, use anonymized metrics: "One SaaS client grew organic traffic 3x in 12 months."

### Collapse the two feature sections into one

The outcome cards ("Never run out of content again," "Know exactly how AI sees your brand," etc.) are strong. The feature grid ("Full-stack growth intelligence," "AI content engine," etc.) is weak. Don't run both.

Keep the outcome cards as the primary feature section. If you need a second feature tier, make it an "Everything you need" grid — but with outcome headlines, not capability labels.

### Promote the three-audience insight

Move "Three audiences matter now: the buyer, the AI agent, the training bot" out of a sub-bullet and into its own standalone beat. This is the most differentiated insight on the page. It could be part of the era-framing section or a callout between the feature cards and the infrastructure section.

### Kill the redundant second hero

Cut "The compounding AI growth engine built into your website" section entirely. It adds nothing the hero didn't already cover. If you want a mid-page reset, use a case study or a pull quote instead.

### Tighten the closing arc

The closing should be one clean section with two beats:

1. **Exclusivity arc:** "Built for the companies shaping their markets. Now available to every growth team."
2. **Dual CTA:** "Start with a free audit" + "Talk to our team"

---

## 4. Language and Tone Improvements

### Replace "AI growth platform" with a recognizable category

Options:
- "AI content marketing platform" — most literal
- "AI growth engine for B2B websites" — more specific
- "AI-powered content growth system" — emphasizes the system, not just the tool

The sub-hero should name one thing: what GrowthX *is*. Right now it's trying to be a platform, an engine, a system, and a team. Pick one.

### Rewrite the sub-hero as one clean promise

Current:
> "GrowthX is the AI growth platform where companies ship higher-performing content, faster — and compound the results every quarter."

The "— and compound the results every quarter" feels bolted on. Suggested replacement:

> "GrowthX is the AI content engine where B2B companies ship more content, rank faster, and compound the results."

Or, even tighter:

> "GrowthX is the AI content engine that ships, ranks, and compounds — faster than any team alone."

### Fix the feature grid language

Replace:

> **Full-stack growth intelligence** — Search performance, AI visibility, content health, competitive landscape. One unified signal.

With:

> **See everything that matters in one place.** Search rankings, AI visibility, content health, competitive moves. One dashboard. No tab-switching.

Replace:

> **AI content engine** — Strategy to draft to publish to optimize. Human calibration at every decision point.

With:

> **Go from strategy to published page, fast.** AI drafts the content. Humans approve the judgment calls. Every page ships with SEO and AI baked in.

Replace:

> **Continuous optimization** — Decay detection. Gap analysis. Performance feedback loops.

With:

> **Nothing decays without you knowing.** Traffic drops trigger alerts. Gaps surface as opportunities. The system gets smarter every month.

Replace:

> **Dedicated growth team** — Named strategists, not ticket queues. Strategy Sprint validates in eight weeks.

With:

> **A named team, not a ticket queue.** Dedicated strategists who know your market. Start with a Strategy Sprint — eight weeks to prove the model.

### Sharpen the three-audience line

Current:
> "Ship content that ranks in search and appears in AI answers."
> "Three audiences matter now: the buyer, the AI agent, the training bot. Every piece of content is built for all three."

This is two beats doing one job. Combine them:

> "Every page you publish has three readers now: the buyer, the AI agent, and the training bot. We build for all three."

Or make it a standalone callout:

> **Your content has three audiences now.**
> The buyer researching a purchase. The AI agent summarizing options. The training bot learning what to recommend. GrowthX builds every page to win all three.

### Fix the infrastructure section

Current:
> **Built on top of your stack.** Integrates with your CMS, analytics, and marketing tools.
> **Synced with how AI actually works.** Trained on 2.6M+ AI responses. 172 categories mapped.
> **Where compounding happens.** Organizations that adopt GrowthX see organic traffic accelerate.

The first two are fine. The third is vague. Replace:

> **Where compounding happens.** Clients see 2-4x organic traffic growth within 12 months. Content production scales 5x without scaling headcount.

(Use real numbers if available. If not, use the most defensible range.)

### Fix the closing line

Current:
> "Built for the companies shaping their markets. Now available as a platform."

Replace:
> "Built for the companies shaping their categories. Now open to every B2B growth team."

"Shaping their categories" is more specific than "shaping their markets." "Open to every B2B growth team" is more inviting than "available as a platform."

---

## 5. What to Keep

These lines are strong. Don't cut them — build around them:

1. **"The next generation of website growth."** — The hero headline works. It's the right Graphite move.

2. **"Never run out of content again."** — Perfect outcome headline. Exactly what Graphite does with feature names.

3. **"Know exactly how AI sees your brand."** — Differentiated and vivid. Makes CheckThat tangible without naming it.

4. **"Stop content from decaying in silence."** — Visceral. "In silence" is doing real work — it names the hidden problem.

5. **"Compound every quarter, automatically."** — Strong velocity promise. Feels inevitable, not incremental.

6. **"Named strategists, not ticket queues."** — Sharp, memorable contrast. Best line in the feature grid.

7. **"Trained on 2.6M+ AI responses. 172 categories mapped."** — Concrete, specific, credible. Keep this anchored near the infrastructure section.

8. **"Your website isn't a brochure anymore."** — Good era-framing line. Could be promoted to the era section.

9. **"Start with a free growth audit. No commitment. No contract. Results in two weeks."** — Close to Graphite's 14-word friction removal. Tighten to remove "Start with a" and it's tighter.

---

## 6. Top 5 Highest-Impact Changes

### 1. Add real social proof — logos and case study metrics

**Why it's #1:** Without proof, nothing else on the page is credible. Graphite's page works because Shopify, Ramp, and Asana are right there with speed metrics. V11 has zero named clients. Add a logo bar and 2-3 case study tiles with velocity numbers. This single change does more for conversion than any copy rewrite.

### 2. Fix the category — replace "AI growth platform" with something specific

**Why it's #2:** The sub-hero is the line that tells the reader "this is for me" or "this isn't." "AI growth platform" doesn't trigger recognition in any buyer. Replace with "AI content engine for B2B" or "AI-powered content marketing platform." The reader should instantly know what shelf this sits on.

**Current:** "GrowthX is the AI growth platform where companies ship higher-performing content, faster — and compound the results every quarter."

**Suggested:** "GrowthX is the AI content engine where B2B companies ship more content, rank faster, and compound the results."

### 3. Move "for the age of AI" to the top and promote the three-audience insight

**Why it's #3:** The era frame is the strongest positioning move in V11, but it's buried in section 7. Move it to the title-tag position. Then take the three-audience insight ("the buyer, the AI agent, the training bot") and make it a standalone callout near the top — it's the single most differentiating idea on the page and it currently reads like an afterthought.

### 4. Cut redundant sections — kill the second hero and collapse the feature tiers

**Why it's #4:** V11 has two heroes ("The next generation of website growth" and "The compounding AI growth engine built into your website"), two feature sections (outcome cards and feature grid), and two infrastructure-ish sections. This makes the page feel long and unfocused. Cut the second hero entirely. Collapse the feature grid into the outcome cards (rewrite grid items as outcome headlines). This makes the page 30% shorter and twice as sharp.

### 5. Rewrite the feature grid in outcome language

**Why it's #5:** The outcome cards ("Never run out of content again," "Know exactly how AI sees your brand") are strong Graphite-style writing. The feature grid ("Full-stack growth intelligence," "Continuous optimization," "Decay detection. Gap analysis.") is spec-doc language that breaks the page's tone. Rewrite every grid item as an outcome with a mechanism — "See everything that matters in one place" instead of "Full-stack growth intelligence." Match the tone of the cards.
