# GrowthX Ecosystem FAQ v1

<metadata>
purpose: Internal FAQ for how Services, CheckThat, and OS fit together — every product combination explained
audience: All GrowthX team members (Sales, CS, Leadership)
related: docs/products/ecosystem-strategy.md, docs/products/checkthat/pricing-and-monetization-v1.md, docs/products/services-and-platform-faq.md
domain: product-strategy
confidence: draft — needs leadership validation on open questions
sensitivity: internal
context_tier: 1
last_updated: 2026-02-13
</metadata>

---

## What Are We Actually Selling?

Three things. They work independently and they work together.

**Services** — GrowthX's core business. AI-powered content marketing for B2B. Strategy Sprints (8 weeks, ~$20k) that convert into Growth Execution contracts (12 months, ~$17k/month). This is the engine that does $12M+ ARR today.

**CheckThat** — The open AI visibility index for B2B. Tracks how AI engines answer buyer questions and where your brand stands. Free tier, Pro at $249/mo, Business at $1,500/mo. This is the data moat and the top-of-funnel lead gen engine.

**OS (ContentOS)** — The platform that powers content operations. Context, strategy, execution, optimization — all in one place. Clients log in, see their strategy, see their work. Two modes: Self-Operated (~$2k/mo) and GrowthX-Operated ($10k+/mo, bundled into Services engagements).

---

## The Product Matrix

Here's every way a customer can engage with us, and what that looks like:

| Combination | Services | CheckThat | OS | Who This Is |
|------------|----------|-----------|-----|------------|
| **Services Alone** | X | | | Legacy clients or clients who haven't migrated to the platform yet. This is the pre-OS world. Over time, this should shrink — every Services client should be on OS. |
| **Services + CheckThat** | X | X | | Services client who also uses CheckThat for AI visibility data. CheckThat informs the content strategy Services executes. No OS platform access (yet). |
| **Self Serve CheckThat** | | X | | Someone who signed up for CheckThat on their own. Free or Pro tier. No services relationship. This is the high-volume, low-touch motion. Could be Nigel's pipeline today. |
| **Full Package** | X | X | X | The ideal state. Services executes the strategy, CheckThat provides AI visibility intelligence, OS is the platform where it all lives. This is the premium engagement. |
| **Services + OS** | X | | X | Services client on the platform but not using CheckThat. This could exist, but the question is: should it? If OS is the delivery platform for Services, and CheckThat data feeds OS, then CheckThat should probably be included. |
| **Self Serve CheckThat + OS** | | X | X | Customer who runs their own content operations on OS and uses CheckThat for AI visibility data. No GrowthX services team involved. Self-operated mode. |
| **Self Serve OS** | | | X | Customer who wants the content ops platform but doesn't need AI visibility tracking (yet) and doesn't want GrowthX's services team. Pure self-serve platform play. |

---

## The Open Questions (and How to Think About Them)

### Where there's OS, is there always CheckThat?

**The argument for yes:** OS includes a native CheckThat integration. If the platform's value prop is "context, strategy, execution, optimization," then AI visibility data (from CheckThat) is core to the optimization and strategy layers. Stripping it out weakens the product.

**The argument for no:** Some customers might want the content ops platform without caring about AI visibility yet. Forcing CheckThat in could complicate pricing or feel like bloat.

**Recommendation to resolve:** Bundle CheckThat (at minimum Free or Pro level) into every OS subscription. The marginal cost to serve is low (~$6/mo for Free, ~$96/mo for Pro). The value add is high. It makes OS stickier, and it feeds more data back into the CheckThat index. If a customer says "I just want the platform, not the AI visibility stuff," they can ignore it — but it's there when they're ready.

### Can a client have OS without CheckThat, or vice versa?

**CheckThat without OS:** Absolutely. This is the primary self-serve motion. Someone signs up for CheckThat Free or Pro. They don't need OS. They just want to see how they show up in AI answers. This is a huge addressable market and should be frictionless.

**OS without CheckThat:** Technically possible, but it weakens the OS value prop. See above — the recommendation is to bundle CheckThat into OS.

### What happens if clients don't want the OS? Just CheckThat?

This is a clean, standalone product. Two paths:

1. **Self-serve (Free + Pro):** Customer signs up, uses the open index, upgrades to Pro when they want more prompts and historical data. No human touch required. This is the Canva/Datadog model — product-led growth.

2. **Sales-assisted (Business tier at $1,500/mo):** Customer wants managed prompt strategy, dedicated AEO strategist, custom reports. This is a services-light motion attached to the software. 18-month contracts preferred.

**The agency pricing question:** If a customer wants CheckThat Business without OS, we're essentially providing AI visibility consulting bundled with the software. The $1,500/mo Business tier already covers this. If the scope expands beyond what Business includes (custom research, deep strategy work), that's upsell territory into Services or a custom SOW. Don't invent a new pricing tier — route them to the existing structure.

### Where does CheckThat Pro live in all of this?

CheckThat Pro ($249/mo) is the self-serve paid tier. It sits between Free and Business:

- **Free → Pro trigger:** Customer wants more than 50 prompts, more than 14 days of history, or near-daily probing instead of weekly.
- **Pro → Business trigger:** Customer wants a human. Managed prompt strategy, dedicated strategist, custom reports.
- **Pro → Services trigger:** Customer realizes they need help creating the content that improves their AI visibility, not just measuring it. This is the handoff from product to services.

Pro is the engine that qualifies serious customers and covers infrastructure costs. It doesn't need OS. It doesn't need Services. It stands on its own.

### Will there be tiers for OS as well?

Based on the current architecture, OS has two modes (not tiers in the traditional sense):

| Mode | Price | What You Get |
|------|-------|-------------|
| **Self-Operated** | ~$2k/mo | Full platform access, native integrations (CheckThat, ExpertLayer, Output.ai), light-touch support. You run it. |
| **GrowthX-Operated** | $10k+/mo | Everything above, plus expert account managers, domain experts, forward-deployed engineers, strategic advising, full execution. We run it for you. |

**The question behind the question:** Should there be a lighter self-serve OS tier (cheaper than $2k/mo) for smaller companies? That depends on unit economics and whether the platform creates enough value at lower price points to justify the support cost. This is a pricing decision that needs Marcel and Bridget.

---

## How to Talk About This to Customers

### "What do you guys actually offer?"

"We help B2B companies show up where their buyers are looking — especially in AI. We have three products. CheckThat shows you how AI engines talk about your brand. Our platform (OS) manages your content operations. And our services team executes the strategy. You can use any one of them, or all three together."

### "I just want to see how we show up in AI. What do I need?"

"Start with CheckThat. It's free for basic tracking. If you want to go deeper — more prompts, historical data, competitor benchmarks — Pro is $249 a month. No platform needed, no services commitment."

### "We need help with our content, not just data."

"That's our services business. We'd start with a Strategy Sprint — 8 weeks where we audit everything and build a plan. Then Growth Execution, where our team runs the strategy on your behalf. The platform (OS) is where you see it all happening."

### "We want everything."

"Full Package. CheckThat feeds the AI visibility intelligence. The platform shows the strategy and work. Our team executes. This is the fastest path because every piece informs the others."

### "We're already a services client. Do we need CheckThat too?"

"You don't need to pay for it separately. But you should be looking at the data — it directly shapes what we prioritize in your content strategy. Let me show you your category in the open index."

### "What's the cheapest way to get started?"

"CheckThat Free. Zero dollars. You'll see your category, the questions buyers ask, and how AI engines answer them. When you want to track your own brand, Pro is $249/mo."

---

## The Customer Journey (Ideal State)

Here's how someone should move through the ecosystem:

**Step 1: Discovery.** They find CheckThat through organic search (the open index), a referral, or marketing. They see their category data for free.

**Step 2: Self-serve activation.** They sign up for CheckThat Free, add their brand, start tracking. They see where they stand.

**Step 3: Upgrade trigger.** They hit the limits of Free (need more prompts, more history, faster probing) and upgrade to Pro.

**Step 4: Strategy need.** They see the data but don't know what to do about it. Two paths: CheckThat Business (managed AI visibility) or a conversation about Services.

**Step 5: Full engagement.** They want someone to actually fix the problem, not just measure it. Strategy Sprint → Growth Execution → Full Package on OS.

Not everyone follows this path. Some start at Step 5 because they already know they need help. That's fine. The ecosystem is designed so every entry point leads somewhere productive.

---

## Internal Decision Tree: What to Sell

When you're talking to a prospect, use this:

**"Do they want to measure, or do they want help?"**

- **Measure only** → CheckThat (Free, Pro, or Business depending on scale and service need)
- **Help with content** → Services (Sprint → Execution)
- **Both** → Services + CheckThat (and OS when ready)

**"Do they have a content team?"**

- **Yes, and they want to run their own ops** → Self-Operated OS (+ CheckThat)
- **Yes, but they need strategic direction** → Services + OS
- **No** → Full Package (we are the team)

**"What's their budget?"**

- **$0** → CheckThat Free. Let the product do the work.
- **$250-$1,500/mo** → CheckThat Pro or Business. Self-serve with optional support.
- **$2k-$10k/mo** → Self-Operated OS + CheckThat. They run it.
- **$10k+/mo** → Services (GrowthX-Operated OS + CheckThat). We run it.
- **$200k+/year** → Full Package. The whole thing.

---

## What Still Needs To Be Decided

These are flagged for leadership. The FAQ above represents the best current thinking, but these need explicit calls:

1. **Is CheckThat always bundled into OS, or optional?** Recommendation: bundle at minimum Pro level.
2. **Does "Services Alone" (without OS) continue to exist, or do all Services clients migrate to OS?** Current trajectory suggests migration, but timeline unclear.
3. **Is there a lighter OS tier below $2k/mo for smaller companies?** Depends on unit economics.
4. **How do we handle agency/partner pricing?** No current framework. Needed if agencies want to resell or use CheckThat for their clients.
5. **Do CheckThat Business customers get any OS access, or is Business purely software + managed strategy?** Clarifying this avoids confusion at the Business/Services boundary.
6. **What's the handoff protocol when a CheckThat customer wants Services?** Who owns the lead, how does the conversation happen, what changes in their billing?
