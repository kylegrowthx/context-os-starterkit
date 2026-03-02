# CheckThat: Screen-by-Screen Product Experience v1

<metadata>
purpose: Complete screen-by-screen UX plan with metrics, content, and ASCII layouts for every CheckThat view
audience: Product, Engineering, Design, Leadership
related: docs/products/checkthat/product-vision-v1.md, docs/products/checkthat/organic-growth-strategy-v1.md
domain: product
confidence: draft
last_updated: 2026-02-14
</metadata>

---

## How This Doc Works

Every screen gets four things: what it is, what's on it, which metrics show, and a rough ASCII layout. Screens are grouped by journey stage: public (no auth), authenticated (logged in), and system (onboarding, settings, upgrade).

Tier gating is called out inline. If a section says `[PRO+]` it means that element is locked or absent on Free.

---

## Navigation (Global)

Persistent across all pages. Two states: logged out and logged in.

```
┌─────────────────────────────────────────────────────────────────────┐
│  ☐ CheckThat          Categories  Answers  Tools  Learn            │
│                                                    [Log in] [Start free] │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│  ☐ CheckThat          Categories  Answers  Tools  Learn            │
│                                            [Dashboard]  [Avatar ▾] │
└─────────────────────────────────────────────────────────────────────┘
```

- Logo links home.
- Categories, Answers, Tools, Learn — the four public discovery paths.
- Logged in: Dashboard link replaces CTAs. Avatar dropdown has Settings, Billing, Log out.
- Search bar (expandable) on every page for brand/category/question lookup.

---

# PART 1: PUBLIC SCREENS (No Auth Required)

These are the open index. Anyone can see them. They drive organic traffic and feed the signup funnel.

---

## 1.1 HOME / LANDING PAGE

**Purpose:** Explain what CheckThat is in 5 seconds. Show the scale of the index. Get people into the data.

**Primary CTA:** "See how AI talks about your market" → links to Categories or search.
**Secondary CTA:** "Track your brand free" → signup.

```
┌─────────────────────────────────────────────────────────────────────┐
│  NAV                                                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│       The open AI visibility index for B2B.                         │
│       See how ChatGPT, Perplexity, and Claude answer                │
│       the questions your buyers ask.                                │
│                                                                     │
│       ┌───────────────────────────────────┐                         │
│       │ Search brands, categories, or     │  [Search]               │
│       │ questions...                      │                         │
│       └───────────────────────────────────┘                         │
│                                                                     │
│       172 categories  ·  5,800+ brands  ·  2.6M+ AI responses      │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  HOW AI SEES YOUR MARKET                                            │
│                                                                     │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                 │
│  │ Expense     │  │ CRM         │  │ Analytics   │                 │
│  │ Management  │  │             │  │             │                 │
│  │             │  │             │  │             │                 │
│  │ 34 brands   │  │ 51 brands   │  │ 28 brands   │                 │
│  │ tracked     │  │ tracked     │  │ tracked     │                 │
│  └─────────────┘  └─────────────┘  └─────────────┘                 │
│                                                                     │
│  [Browse all 172 categories →]                                      │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  QUESTIONS BUYERS ARE ASKING AI RIGHT NOW                           │
│                                                                     │
│  "Best expense tool for a 200-person finance team?"                 │
│   → ChatGPT mentions: Ramp, Brex, Airbase                          │
│   → Perplexity mentions: Ramp, Navan, Center                       │
│   → Claude mentions: Brex, Ramp, Divvy                             │
│   [See full answer →]                                               │
│                                                                     │
│  "What CRM is best for real estate agents?"                         │
│   → ChatGPT mentions: Follow Up Boss, kvCORE, LionDesk            │
│   → ...                                                             │
│   [See full answer →]                                               │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  HOW IT WORKS                                                       │
│                                                                     │
│  1. We map buyer       2. We ask 5 AI        3. We track who       │
│     questions for         engines the same       shows up, how      │
│     every B2B             questions, every       they're positioned │
│     category.             week.                  and what changed.  │
│                                                                     │
│  [Track your brand free →]                                          │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  TRUSTED BY (logos or proof points)                                 │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│  FOOTER: About · Pricing · Blog · API · Terms · Privacy            │
└─────────────────────────────────────────────────────────────────────┘
```

**Metrics on this page:** Total categories, brands tracked, AI responses collected. These update live as the index grows.

---

## 1.2 CATEGORIES BROWSER (`/categories/`)

**Purpose:** Browse the full index by market. Find your world. Entry point to brands and answers.

```
┌─────────────────────────────────────────────────────────────────────┐
│  NAV                                                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  B2B Software Categories                                            │
│  172 categories · 5,800+ brands · Updated weekly                    │
│                                                                     │
│  ┌──────────────────────────────────────────┐                       │
│  │ Search categories...                     │                       │
│  └──────────────────────────────────────────┘                       │
│                                                                     │
│  Filter: [All] [Marketing] [Sales] [Finance] [Engineering]         │
│          [Security] [HR] [Analytics] [Infrastructure]               │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────────────────────────────────────────────────┐       │
│  │ Expense Management                              34 brands │       │
│  │ How AI ranks expense tools for finance teams              │       │
│  │ Top mentioned: Ramp · Brex · Airbase · Navan             │       │
│  │ ░░░░░░░░░░░░░░░░░░░░░░ 312 questions tracked            │       │
│  └──────────────────────────────────────────────────────────┘       │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────┐       │
│  │ CRM                                             51 brands │       │
│  │ How AI recommends CRMs by industry and team size          │       │
│  │ Top mentioned: HubSpot · Salesforce · Pipedrive           │       │
│  │ ░░░░░░░░░░░░░░░░░░░░░░░░░░ 487 questions tracked        │       │
│  └──────────────────────────────────────────────────────────┘       │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────┐       │
│  │ Product Analytics                               28 brands │       │
│  │ ...                                                       │       │
│  └──────────────────────────────────────────────────────────┘       │
│                                                                     │
│  [Load more categories]                                             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Each category card shows:** Category name, brand count, one-line description, top mentioned brands, question count.

**Sort options:** Alphabetical, most brands, most questions tracked, recently updated.

---

## 1.3 CATEGORY DETAIL (`/categories/[category]/`)

**Purpose:** The hub page for a market. Shows every brand AI talks about in this space, the questions buyers ask, and how answers differ by engine.

```
┌─────────────────────────────────────────────────────────────────────┐
│  NAV                                                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Expense Management                                                 │
│  34 brands · 312 questions tracked · 5 AI engines                   │
│  Last probed: Feb 13, 2026                                          │
│                                                                     │
├───────────────┬─────────────────────────────────────────────────────┤
│               │                                                     │
│  ON THIS PAGE │  AI VISIBILITY RANKINGS                             │
│               │                                                     │
│  Rankings     │  How often each brand is mentioned when buyers      │
│  Questions    │  ask AI about expense management tools.             │
│  Engines      │                                                     │
│  Trends       │  #   Brand        Recall   Engines   Trend         │
│               │  ──────────────────────────────────────────         │
│               │  1   Ramp         87%      5/5       ▲ +4%         │
│               │  2   Brex         81%      5/5       ▬ 0%          │
│               │  3   Airbase      64%      4/5       ▲ +7%         │
│               │  4   Navan        58%      4/5       ▼ -3%         │
│               │  5   Center       41%      3/5       ▲ +12%        │
│               │  6   Divvy        38%      3/5       ▼ -8%         │
│               │  7   Emburse      29%      2/5       ▬ 0%          │
│               │  ...                                                │
│               │  [See all 34 brands →]                              │
│               │                                                     │
│               ├─────────────────────────────────────────────────────┤
│               │                                                     │
│               │  TOP BUYER QUESTIONS                                │
│               │                                                     │
│               │  "Best expense tool for startups?"                  │
│               │   ChatGPT: Ramp, Brex │ Claude: Brex, Ramp         │
│               │   [See full answer →]                               │
│               │                                                     │
│               │  "Ramp vs Brex for Series A?"                       │
│               │   ChatGPT: Ramp │ Claude: Brex │ Perplexity: Ramp  │
│               │   [See full answer →]                               │
│               │                                                     │
│               │  "Best expense tool for 200+ employees?"            │
│               │   ...                                               │
│               │                                                     │
│               │  [See all 312 questions →]                          │
│               │                                                     │
│               ├─────────────────────────────────────────────────────┤
│               │                                                     │
│               │  ENGINE COMPARISON                                  │
│               │                                                     │
│               │  Who does each AI engine favor in this category?    │
│               │                                                     │
│               │           ChatGPT  Perplexity  Claude  Gemini  G.AI│
│               │  Ramp     #1       #1          #2      #1      #2  │
│               │  Brex     #2       #3          #1      #2      #1  │
│               │  Airbase  #3       #2          #4      #3      #3  │
│               │  Navan    #4       #4          #3      #5      #4  │
│               │                                                     │
│               ├─────────────────────────────────────────────────────┤
│               │                                                     │
│               │  VISIBILITY TREND (last 60 days)                    │
│               │                                                     │
│               │  100%│                                               │
│               │     │  ·····Ramp····················                │
│               │  75%│    ·····Brex·············                      │
│               │     │         ···Airbase····▲                       │
│               │  50%│              ···Navan··▼                       │
│               │     │                                               │
│               │  25%│                                               │
│               │     └──────────────────────────────                 │
│               │      Jan 15  Jan 29  Feb 5  Feb 13                 │
│               │                                                     │
│               │  [Track your brand in this category →]              │
│               │                                                     │
└───────────────┴─────────────────────────────────────────────────────┘
```

**Metrics on this page:**
- Recall % per brand (how often mentioned across all prompts in category)
- Engine coverage (mentioned in how many of the 5 engines)
- Trend (% change in recall over last 30 days, ▲ up / ▼ down / ▬ flat)
- Engine-by-engine ranking table
- Time-series chart of visibility over 60 days

**CTA:** "Track your brand in this category" → signup or dashboard.

---

## 1.4 BRAND PROFILE (`/[brand]/`)

**Purpose:** Everything AI says about one brand. The research page a buyer or marketer lands on.

```
┌─────────────────────────────────────────────────────────────────────┐
│  NAV                                                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌────┐  Ramp                                                       │
│  │logo│  Corporate expense management platform                      │
│  └────┘  ramp.com · Expense Management · Founded 2019               │
│                                                                     │
│  [Track this brand]  [Compare]                                      │
│                                                                     │
├──────────┬──────────┬──────────┬──────────┬──────────┬──────────────┤
│ Overview │ Pricing  │ Alts     │ Reviews  │ Product  │ AI Visibility│
├──────────┴──────────┴──────────┴──────────┴──────────┴──────────────┤
│                                                                     │
│  AI VISIBILITY SNAPSHOT                                             │
│                                                                     │
│  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐       │
│  │ RECALL     │ │ SENTIMENT  │ │ ENGINES    │ │ TREND      │       │
│  │            │ │            │ │            │ │            │       │
│  │   87%      │ │  Positive  │ │    5/5     │ │   ▲ +4%    │       │
│  │ mentioned  │ │ "reliable, │ │ all engines│ │  30-day    │       │
│  │ in category│ │  modern"   │ │ mention    │ │  change    │       │
│  └────────────┘ └────────────┘ └────────────┘ └────────────┘       │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  HOW AI DESCRIBES RAMP                                              │
│                                                                     │
│  ┌─ ChatGPT ─────────────────────────────────────────────┐          │
│  │ "Ramp is a corporate card and expense management       │          │
│  │  platform known for savings automation and real-time   │          │
│  │  spending controls..."                                 │          │
│  │  Sources cited: ramp.com, TechCrunch, G2              │          │
│  └────────────────────────────────────────────────────────┘          │
│                                                                     │
│  ┌─ Perplexity ──────────────────────────────────────────┐          │
│  │ "Ramp offers a comprehensive expense management        │          │
│  │  solution that includes corporate cards, bill pay..."  │          │
│  │  Sources cited: ramp.com, Forbes, NerdWallet           │          │
│  └────────────────────────────────────────────────────────┘          │
│                                                                     │
│  ┌─ Claude ──────────────────────────────────────────────┐          │
│  │ "Ramp is a financial operations platform focused on    │          │
│  │  expense management and cost reduction..."             │          │
│  │  Sources cited: ramp.com, Crunchbase                   │          │
│  └────────────────────────────────────────────────────────┘          │
│                                                                     │
│  + Gemini  + Google AI    [Expand all]                              │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  BUYER QUESTIONS WHERE RAMP APPEARS                                 │
│                                                                     │
│  Question                              Engines  Position            │
│  ─────────────────────────────────────────────────────              │
│  "Best expense tool for startups?"     5/5      #1 in 3 engines    │
│  "Ramp vs Brex?"                       5/5      Featured           │
│  "Best corporate card for mid-market?" 4/5      #2 in 2 engines    │
│  "Expense tools with savings insights" 3/5      #1 in 2 engines    │
│  ...                                                                │
│  Showing 10 of 47 questions  [See all →]                           │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  CATEGORIES                          COMPETITORS IN AI              │
│  Expense Management                  Brex · Airbase · Navan        │
│  Corporate Cards                     Center · Divvy · Emburse      │
│  Spend Management                    [Compare head to head →]       │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  RELATED                                                            │
│  Lists: Top FinTech Tools · Best Expense Tools for Startups         │
│  Learn: What is AEO? · How AI Picks Expense Tools                  │
│                                                                     │
│  [Is this your brand? Track it free →]                              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Metrics on this page:**
- Recall % in primary category
- Sentiment summary (positive/neutral/negative + key descriptors AI uses)
- Engine coverage (X/5)
- 30-day trend
- Per-question engine count and position
- Source citations per engine

**Sub-tabs:** Overview (default, shown above), Pricing, Alternatives, Reviews, Product/Features, AI Visibility (deeper data view). Each is a variant URL: `/ramp/pricing`, `/ramp/alternatives`, etc.

---

## 1.5 ANSWER PAGE (`/answers/[question-slug]/`)

**Purpose:** Two-layer page. Layer 1: the best editorial answer to a buyer question. Layer 2: how each AI engine actually answers it. This is CheckThat's most distinctive page type.

```
┌─────────────────────────────────────────────────────────────────────┐
│  NAV                                                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Best expense management tool for startups?                         │
│  Category: Expense Management · Last probed: Feb 13, 2026           │
│  5 AI engines tracked · 8 brands mentioned                          │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  OUR ANSWER                                                         │
│                                                                     │
│  [Comprehensive, editorial answer — 300-500 words.                  │
│   Written by editors, not just AI. Covers the question              │
│   thoroughly: what to look for, top options by use case,            │
│   trade-offs. Links to brand pages for each tool mentioned.         │
│   Goal: best answer to this question anywhere on the internet.]     │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  HOW AI ANSWERS THIS QUESTION                                       │
│                                                                     │
│  ┌─ ChatGPT (Feb 13, 2026) ─────────────────────────────┐          │
│  │                                                        │          │
│  │  Brands mentioned: Ramp (#1), Brex (#2), Mercury (#3) │          │
│  │                                                        │          │
│  │  "For startups, Ramp is often recommended for its      │          │
│  │   automated savings and easy onboarding. Brex is       │          │
│  │   popular for venture-backed companies with its..."    │          │
│  │                                                        │          │
│  │  Sources cited: ramp.com, brex.com, nerdwallet.com     │          │
│  └────────────────────────────────────────────────────────┘          │
│                                                                     │
│  ┌─ Perplexity (Feb 13, 2026) ───────────────────────────┐          │
│  │                                                        │          │
│  │  Brands mentioned: Ramp (#1), Navan (#2), Brex (#3)   │          │
│  │                                                        │          │
│  │  "The best expense management tools for startups       │          │
│  │   include Ramp for automated expense tracking..."      │          │
│  │                                                        │          │
│  │  Sources cited: ramp.com, g2.com, techcrunch.com       │          │
│  └────────────────────────────────────────────────────────┘          │
│                                                                     │
│  ┌─ Claude ──┐  ┌─ Gemini ──┐  ┌─ Google AI ┐                      │
│  │  [expand] │  │  [expand] │  │  [expand]  │                      │
│  └───────────┘  └───────────┘  └────────────┘                      │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  BRAND MENTIONS ACROSS ENGINES                                      │
│                                                                     │
│  Brand      ChatGPT  Perplexity  Claude  Gemini  Google AI         │
│  ────────────────────────────────────────────────────────           │
│  Ramp       #1       #1          #2      #1      #1                │
│  Brex       #2       #3          #1      #2      #3                │
│  Mercury    #3       —           #3      —       #2                │
│  Navan      —        #2          —       #3      —                 │
│  Airbase    —        —           #4      #4      #4                │
│                                                                     │
│  ● = mentioned   — = not mentioned                                  │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  HOW THIS ANSWER HAS CHANGED                                        │
│                                                                     │
│  ┌─────────────────────────────────────────────┐                    │
│  │  Jan 1     Jan 15    Feb 1     Feb 13       │                    │
│  │  ·─────·─────·─────·─────                   │                    │
│  │  Ramp: consistently #1 across all engines   │                    │
│  │  Brex: dropped from #1 to #2 in ChatGPT    │                    │
│  │  Mercury: appeared in ChatGPT on Jan 22     │                    │
│  │  Navan: disappeared from Claude on Feb 3    │                    │
│  └─────────────────────────────────────────────┘                    │
│                                                                     │
│  [Track this question for your brand →]                             │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  RELATED QUESTIONS                                                  │
│  · "Ramp vs Brex for startups?"                                     │
│  · "Best corporate card for pre-revenue companies?"                 │
│  · "Cheapest expense tool for small teams?"                         │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Metrics on this page:**
- Brand mention matrix (which brand appears in which engine, at what position)
- Source citations per engine
- Historical change log (when brands entered/exited answers)
- Engine count per brand

---

## 1.6 COMPARISON PAGE (`/comparisons/[brand]-vs-[brand]/`)

**Purpose:** Head-to-head. How AI sees two brands side by side across every engine.

```
┌─────────────────────────────────────────────────────────────────────┐
│  NAV                                                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Ramp vs Brex                                                       │
│  How AI engines compare these two expense management platforms      │
│                                                                     │
├──────────────────────────┬──────────────────────────────────────────┤
│                          │                                          │
│       RAMP               │          BREX                            │
│                          │                                          │
│  Recall: 87%             │  Recall: 81%                             │
│  Sentiment: Positive     │  Sentiment: Positive                     │
│  Engines: 5/5            │  Engines: 5/5                            │
│  Trend: ▲ +4%            │  Trend: ▬ 0%                             │
│                          │                                          │
│  AI says: "savings       │  AI says: "venture-backed,               │
│  automation, modern      │  premium corporate card,                 │
│  UX, fast onboarding"    │  global payments"                        │
│                          │                                          │
├──────────────────────────┴──────────────────────────────────────────┤
│                                                                     │
│  ENGINE-BY-ENGINE PREFERENCE                                        │
│                                                                     │
│  Engine       Prefers    Context                                    │
│  ──────────────────────────────────────────                         │
│  ChatGPT      Ramp       Mentions Ramp first in 71% of prompts     │
│  Perplexity   Ramp       Cites Ramp's savings features              │
│  Claude       Brex       Highlights Brex's global capabilities      │
│  Gemini       Ramp       Recommends Ramp for cost control           │
│  Google AI    Tie        Both mentioned equally                      │
│                                                                     │
│  Ramp wins: 3 engines · Brex wins: 1 engine · Tie: 1 engine        │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  QUESTIONS WHERE THEY COMPETE                                       │
│                                                                     │
│  Question                           Ramp    Brex                    │
│  ─────────────────────────────────────────────────                  │
│  "Best expense tool for startups?"  #1      #2                      │
│  "Ramp vs Brex?"                    feat.   feat.                   │
│  "Corporate card for mid-market?"   #2      #1                      │
│  "Best for international expenses?" —       #1                      │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  VISIBILITY OVER TIME                                               │
│                                                                     │
│  100%│ ·····Ramp·····················                               │
│     │    ···Brex··················                                  │
│   50%│                                                              │
│     └──────────────────────────────                                │
│      Jan 15    Feb 1     Feb 13                                     │
│                                                                     │
│  [Track these brands →]                                             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Metrics:** Recall %, sentiment, engine preference breakdown, head-to-head question matrix, trend comparison.

---

## 1.7 TOOLS (`/tools/`)

### 1.7a AI Visibility Checker

**Purpose:** Instant gratification. Type a brand, see how AI describes it. Product demo disguised as a free tool.

```
┌─────────────────────────────────────────────────────────────────────┐
│  NAV                                                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  AI Visibility Checker                                              │
│  See how AI engines describe any B2B brand — instantly.             │
│                                                                     │
│  ┌────────────────────────────────────────┐                         │
│  │ Enter a brand name...                  │  [Check]                │
│  └────────────────────────────────────────┘                         │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  RESULTS FOR: Ramp                                                  │
│                                                                     │
│  ┌─ ChatGPT ──────────────┐  ┌─ Claude ───────────────┐            │
│  │ "Ramp is a corporate   │  │ "Ramp is a financial   │            │
│  │  card and expense..."  │  │  operations platform.."│            │
│  │ Sentiment: Positive    │  │ Sentiment: Positive    │            │
│  └────────────────────────┘  └────────────────────────┘            │
│                                                                     │
│  ┌─ Perplexity ───────────┐  ┌─ Gemini ───────────────┐            │
│  │ "Ramp offers expense   │  │ "Ramp is known for     │            │
│  │  management with..."   │  │  its AI-powered..."    │            │
│  │ Sentiment: Positive    │  │ Sentiment: Positive    │            │
│  └────────────────────────┘  └────────────────────────┘            │
│                                                                     │
│  Want deeper tracking? [Create free account →]                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 1.7b Prompt Tester

**Purpose:** Type any question, see how AI answers it across engines. Shows the raw multi-engine comparison.

```
┌─────────────────────────────────────────────────────────────────────┐
│  Enter any question a buyer might ask AI:                           │
│  ┌──────────────────────────────────────────────────┐               │
│  │ What's the best project management tool for...   │  [Test]       │
│  └──────────────────────────────────────────────────┘               │
│                                                                     │
│  ChatGPT says:          Perplexity says:       Claude says:         │
│  ┌──────────────┐       ┌──────────────┐       ┌──────────────┐    │
│  │ 1. Asana     │       │ 1. Monday    │       │ 1. Linear    │    │
│  │ 2. Monday    │       │ 2. Asana     │       │ 2. Asana     │    │
│  │ 3. ClickUp   │       │ 3. ClickUp   │       │ 3. Notion    │    │
│  └──────────────┘       └──────────────┘       └──────────────┘    │
│                                                                     │
│  [Save this prompt to your dashboard →]                             │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 1.8 LISTS (`/lists/`)

**Purpose:** Curated collections. Editorial picks backed by AI data. Good for SEO and browsing.

```
┌─────────────────────────────────────────────────────────────────────┐
│  NAV                                                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Lists                                                              │
│  Curated collections of B2B brands, backed by AI visibility data.   │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────┐       │
│  │  Top YC-backed B2B SaaS by AI Visibility                 │       │
│  │  42 brands · Updated Feb 13                               │       │
│  │  Which Y Combinator companies are AI engines              │       │
│  │  recommending to buyers?                                  │       │
│  └──────────────────────────────────────────────────────────┘       │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────┐       │
│  │  Fastest Rising B2B Brands in AI (last 30 days)           │       │
│  │  25 brands · Updated weekly                               │       │
│  │  The brands gaining visibility across AI engines fastest.  │       │
│  └──────────────────────────────────────────────────────────┘       │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────┐       │
│  │  Best Expense Tools for Startups                          │       │
│  │  12 brands · Updated Feb 10                               │       │
│  └──────────────────────────────────────────────────────────┘       │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 1.9 LEARN (`/learn/`)

**Purpose:** Educational content hub. Builds topical authority. Explains AEO, methodology, strategy.

Key pages: What is AEO · How AI Decides What to Recommend · Why Prompts Matter · Our Methodology · How We Measure Visibility.

Standard article layout — hero, body, related links, CTA. No ASCII needed; these are editorial pages.

---

## 1.10 PRICING PAGE (`/pricing/`)

```
┌─────────────────────────────────────────────────────────────────────┐
│  NAV                                                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Simple pricing. Start free.                                        │
│                                                                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐              │
│  │    FREE       │  │     PRO      │  │   BUSINESS   │              │
│  │    $0/mo      │  │   $249/mo    │  │  $1,500/mo   │              │
│  │               │  │              │  │              │              │
│  │ 50 custom     │  │ 500 custom   │  │ 2,000 custom │              │
│  │ prompts       │  │ prompts      │  │ prompts      │              │
│  │               │  │              │  │              │              │
│  │ 14 days       │  │ 60 days      │  │ Full archive │              │
│  │ history       │  │ history      │  │              │              │
│  │               │  │              │  │              │              │
│  │ Weekly        │  │ Near daily   │  │ Near daily   │              │
│  │ probing       │  │ probing      │  │ probing      │              │
│  │               │  │              │  │              │              │
│  │ 5 AI engines  │  │ 5 AI engines │  │ 8+ engines   │              │
│  │               │  │              │  │              │              │
│  │ 100K+ shared  │  │ Competitor   │  │ AEO          │              │
│  │ prompts       │  │ benchmarks   │  │ strategist   │              │
│  │               │  │              │  │              │              │
│  │ Unlimited     │  │ Export       │  │ Managed      │              │
│  │ users         │  │              │  │ prompts      │              │
│  │               │  │ Slack        │  │              │              │
│  │ Self-serve    │  │ support      │  │ Custom       │              │
│  │ support       │  │              │  │ reports      │              │
│  │               │  │              │  │              │              │
│  │ [Start free]  │  │ [Start Pro]  │  │ [Talk to us] │              │
│  └──────────────┘  └──────────────┘  └──────────────┘              │
│                                                                     │
│  All plans include: Full open index · Unlimited users ·             │
│  Company research database · 100,000+ shared prompts                │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

# PART 2: AUTHENTICATED SCREENS (Dashboard)

Everything behind login. The product experience that converts and retains.

---

## 2.1 DASHBOARD HOME

**Purpose:** The first thing you see after login. Your brand's AI visibility at a glance. Answer three questions immediately: Am I visible? How am I positioned? What changed?

```
┌─────────────────────────────────────────────────────────────────────┐
│  NAV (logged in)                                                    │
├────────────┬────────────────────────────────────────────────────────┤
│            │                                                        │
│  SIDEBAR   │  Good morning, Marcel.            Last probe: 4h ago   │
│            │                                                        │
│  Dashboard │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ │
│  ● Home    │  │ RECALL   │ │SENTIMENT │ │ ENGINES  │ │ TREND    │ │
│  Prompts   │  │          │ │          │ │          │ │          │ │
│  Library   │  │   72%    │ │ Positive │ │   4/5    │ │  ▲ +6%   │ │
│  Compete   │  │ mentions │ │ 81% pos  │ │ engines  │ │ 30-day   │ │
│  Insights  │  │ across   │ │ 12% neu  │ │ mention  │ │ recall   │ │
│  Reports   │  │ tracked  │ │  7% neg  │ │ you      │ │ change   │ │
│  Settings  │  │ prompts  │ │          │ │          │ │          │ │
│            │  └──────────┘ └──────────┘ └──────────┘ └──────────┘ │
│            │                                                        │
│            │  VISIBILITY OVER TIME                                  │
│            │  ┌────────────────────────────────────────────────┐    │
│            │  │ 100%│                                          │    │
│            │  │     │        ·····•·····•·····•                │    │
│            │  │  75%│  ·····•                  •····           │    │
│            │  │     │ •                             •···       │    │
│            │  │  50%│                                          │    │
│            │  │     │                                          │    │
│            │  │  25%│                                          │    │
│            │  │     └──────────────────────────────────────    │    │
│            │  │      Dec    Jan     Feb                        │    │
│            │  │                                                │    │
│            │  │  ── Your brand   ·· Category avg               │    │
│            │  └────────────────────────────────────────────────┘    │
│            │                     [PRO+ shows competitor lines]       │
│            │                                                        │
│            │  ENGINE BREAKDOWN                                      │
│            │  ┌────────────────────────────────────────────────┐    │
│            │  │ ChatGPT    ████████████████░░░░  82%  ▲ +3%   │    │
│            │  │ Perplexity ██████████████░░░░░░  71%  ▬  0%   │    │
│            │  │ Claude     ████████████░░░░░░░░  64%  ▲ +9%   │    │
│            │  │ Gemini     ██████████░░░░░░░░░░  55%  ▼ -2%   │    │
│            │  │ Google AI  ████████░░░░░░░░░░░░  44%  ▲ +11%  │    │
│            │  └────────────────────────────────────────────────┘    │
│            │                                                        │
│            │  WHAT CHANGED THIS WEEK                                │
│            │  ┌────────────────────────────────────────────────┐    │
│            │  │ ▲ Appeared in Claude's answer to "best         │    │
│            │  │   project management for remote teams"          │    │
│            │  │                                                 │    │
│            │  │ ▼ Dropped from Gemini's answer to "affordable  │    │
│            │  │   tools for startups"                           │    │
│            │  │                                                 │    │
│            │  │ ● Brex overtook you in Perplexity for          │    │
│            │  │   "expense tools for mid-market"                │    │
│            │  └────────────────────────────────────────────────┘    │
│            │                                                        │
│            │  PROMPT USAGE                                          │
│            │  ███████████████████████░░░░░  38/50 custom prompts   │
│            │                                 [Upgrade for 500 →]    │
│            │                                                        │
└────────────┴────────────────────────────────────────────────────────┘
```

**Metrics on this screen:**
- Recall % (overall and per engine)
- Sentiment breakdown (% positive / neutral / negative)
- Engine coverage (X/5)
- 30-day trend (% change)
- Visibility time series chart (your brand, category avg, competitors on PRO+)
- Per-engine bar chart with trend arrows
- Change log (appeared, disappeared, overtaken events)
- Prompt usage (X/limit with upgrade CTA on Free)

---

## 2.2 PROMPTS MANAGER

**Purpose:** Create, organize, and track your custom prompts. See results per prompt.

```
┌────────────┬────────────────────────────────────────────────────────┐
│            │                                                        │
│  SIDEBAR   │  Custom Prompts                    38/50 used          │
│            │                                                        │
│            │  [+ New prompt]   Filter: [All ▾]  Sort: [Recent ▾]   │
│            │                                                        │
│            │  ┌────────────────────────────────────────────────┐    │
│            │  │ "Best expense tool for Series A startups?"     │    │
│            │  │                                                 │    │
│            │  │ Status: Active · Last probed: 4h ago            │    │
│            │  │ You appear: Yes (4/5 engines)                   │    │
│            │  │ Position: #1 in ChatGPT, #2 in Claude           │    │
│            │  │ Competitors: Brex (#1 Claude), Airbase (#3)     │    │
│            │  │                                                 │    │
│            │  │ [View details]  [Edit]  [Archive]               │    │
│            │  └────────────────────────────────────────────────┘    │
│            │                                                        │
│            │  ┌────────────────────────────────────────────────┐    │
│            │  │ "What CRM integrates best with Slack?"          │    │
│            │  │                                                 │    │
│            │  │ Status: Active · Last probed: 4h ago            │    │
│            │  │ You appear: No (0/5 engines)          ⚠ Gap     │    │
│            │  │ Top mentions: HubSpot, Salesforce, Pipedrive    │    │
│            │  │                                                 │    │
│            │  │ [View details]  [Edit]  [Archive]               │    │
│            │  └────────────────────────────────────────────────┘    │
│            │                                                        │
│            │  ┌────────────────────────────────────────────────┐    │
│            │  │ "Ramp vs Brex vs Airbase?"                      │    │
│            │  │                                                 │    │
│            │  │ Status: Pending review · Queued for probing     │    │
│            │  │                                                 │    │
│            │  │ [View details]  [Edit]  [Archive]               │    │
│            │  └────────────────────────────────────────────────┘    │
│            │                                                        │
│            │  ...                                                   │
│            │                                                        │
│            │  ░░░░░░░░░░░░░░░░░░░░░░░░░  38/50                    │
│            │  [Upgrade to Pro for 500 prompts →]                    │
│            │                                                        │
└────────────┴────────────────────────────────────────────────────────┘
```

**Prompt detail view (expanded or click-through):**

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  "Best expense tool for Series A startups?"                         │
│  Custom prompt · Created Jan 20 · Probed 12 times                   │
│                                                                     │
│  YOUR BRAND'S PRESENCE                                              │
│                                                                     │
│  Engine       Mentioned?  Position  What AI says about you          │
│  ──────────────────────────────────────────────────────────         │
│  ChatGPT      Yes         #1        "modern UX, savings automation" │
│  Perplexity   Yes         #1        "fast onboarding, integrations" │
│  Claude       Yes         #2        "expense management platform"   │
│  Gemini       Yes         #2        "corporate card with controls"  │
│  Google AI    No          —         Not mentioned                    │
│                                                                     │
│  COMPETITORS IN THIS ANSWER                                         │
│                                                                     │
│  Brand      ChatGPT  Perplexity  Claude  Gemini  Google AI         │
│  ──────────────────────────────────────────────────────────         │
│  You        #1       #1          #2      #2      —                  │
│  Brex       #2       #3          #1      #1      #1                 │
│  Airbase    #3       —           #3      #3      #2                 │
│  Mercury    —        #2          —       —       #3                 │
│                                                                     │
│  TREND (last 8 probes)                                              │
│  ┌──────────────────────────────────────────┐                       │
│  │  #1 │ ●  ●     ●  ●  ●  ●               │  You                 │
│  │  #2 │       ●                 ●  ●       │                      │
│  │  #3 │                                    │                      │
│  │  —  │                                    │                      │
│  │     └─────────────────────────────────   │                      │
│  │      Jan 20  Jan 27  Feb 3  Feb 10       │                      │
│  └──────────────────────────────────────────┘                       │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 2.3 SHARED PROMPT LIBRARY

**Purpose:** Browse 100,000+ pre-built buyer questions. Find relevant ones to add or learn from.

```
┌────────────┬────────────────────────────────────────────────────────┐
│            │                                                        │
│  SIDEBAR   │  Shared Prompt Library              103,847 prompts    │
│            │                                                        │
│            │  ┌────────────────────────────────────────┐            │
│            │  │ Search prompts...                      │            │
│            │  └────────────────────────────────────────┘            │
│            │                                                        │
│            │  Category: [Expense Management ▾]                      │
│            │  Type: [All ▾]  Engine: [All ▾]  Brand: [Any ▾]       │
│            │                                                        │
│            │  ┌────────────────────────────────────────────────┐    │
│            │  │ "Best expense tool for startups?"              │    │
│            │  │ Category: Expense Management · 5 engines       │    │
│            │  │ Brands mentioned: Ramp, Brex, Airbase, +4     │    │
│            │  │ Your brand: Mentioned (4/5)                     │    │
│            │  │ [View answer] [Add to my tracking]              │    │
│            │  └────────────────────────────────────────────────┘    │
│            │                                                        │
│            │  ┌────────────────────────────────────────────────┐    │
│            │  │ "What expense tools have the best mobile app?" │    │
│            │  │ Category: Expense Management · 5 engines       │    │
│            │  │ Brands mentioned: Expensify, Ramp, SAP, +6    │    │
│            │  │ Your brand: Not mentioned ⚠                    │    │
│            │  │ [View answer] [Add to my tracking]              │    │
│            │  └────────────────────────────────────────────────┘    │
│            │                                                        │
│            │  ...                                                   │
│            │                                                        │
└────────────┴────────────────────────────────────────────────────────┘
```

**Key detail:** Each prompt shows whether your brand appears. Prompts where you're NOT mentioned are flagged — these are gaps to investigate or close.

---

## 2.4 COMPETITIVE BENCHMARKS `[PRO+]`

**Purpose:** You vs. competitors across all tracked prompts. The war room view.

```
┌────────────┬────────────────────────────────────────────────────────┐
│            │                                                        │
│  SIDEBAR   │  Competitive Benchmarks              [PRO+]           │
│            │                                                        │
│            │  Your brand vs. top competitors in Expense Management  │
│            │                                                        │
│            │  OVERALL RECALL                                        │
│            │  ┌────────────────────────────────────────────────┐    │
│            │  │  You       ████████████████████████░░  87%     │    │
│            │  │  Brex      ██████████████████████░░░░  81%     │    │
│            │  │  Airbase   ████████████████░░░░░░░░░░  64%     │    │
│            │  │  Navan     ██████████████░░░░░░░░░░░░  58%     │    │
│            │  │  Center    ██████████░░░░░░░░░░░░░░░░  41%     │    │
│            │  └────────────────────────────────────────────────┘    │
│            │                                                        │
│            │  RECALL BY ENGINE                                      │
│            │  ┌────────────────────────────────────────────────┐    │
│            │  │         ChatGPT  Perp.  Claude  Gemini  G.AI  │    │
│            │  │  You    92%      85%    71%     68%     49%   │    │
│            │  │  Brex   88%      74%    79%     72%     63%   │    │
│            │  │  Airbase 61%     68%    58%     51%     44%   │    │
│            │  │  Navan  55%      62%    49%     48%     40%   │    │
│            │  └────────────────────────────────────────────────┘    │
│            │                                                        │
│            │  HEAD-TO-HEAD TREND (last 60 days)                     │
│            │  ┌────────────────────────────────────────────────┐    │
│            │  │ 100%│                                          │    │
│            │  │     │  ═══You═══════════════════════            │    │
│            │  │  75%│    ───Brex────────────────────            │    │
│            │  │     │       ···Airbase·········▲               │    │
│            │  │  50%│         ···Navan·····▼                    │    │
│            │  │     └──────────────────────────────            │    │
│            │  │      Dec 15   Jan 1  Jan 15  Feb 13            │    │
│            │  └────────────────────────────────────────────────┘    │
│            │                                                        │
│            │  WHERE YOU WIN / WHERE YOU LOSE                        │
│            │  ┌────────────────────────────────────────────────┐    │
│            │  │ ✓ WINNING                                      │    │
│            │  │   "best expense tool for startups" — #1 in 3   │    │
│            │  │   "corporate card with savings" — #1 in 4      │    │
│            │  │                                                 │    │
│            │  │ ✗ LOSING                                       │    │
│            │  │   "expense tools for global teams" — Brex #1   │    │
│            │  │   "best expense tools for enterprise" — not    │    │
│            │  │   mentioned in 3/5 engines                      │    │
│            │  │                                                 │    │
│            │  │ ⚠ GAPS (not mentioned, competitors are)        │    │
│            │  │   "affordable expense tool for nonprofits"      │    │
│            │  │   "expense tool with mileage tracking"          │    │
│            │  └────────────────────────────────────────────────┘    │
│            │                                                        │
│            │  [Export benchmark report]                              │
│            │                                                        │
└────────────┴────────────────────────────────────────────────────────┘
```

**Metrics:** Recall % per competitor, per engine. Head-to-head trend. Win/lose/gap analysis per prompt.

**Free tier:** This screen shows a preview with blurred competitor data and an upgrade CTA.

---

## 2.5 INSIGHTS `[ALL TIERS, depth varies]`

**Purpose:** The "so what" screen. Answers the three questions: Where do you show up? How are you positioned? What should you do next?

```
┌────────────┬────────────────────────────────────────────────────────┐
│            │                                                        │
│  SIDEBAR   │  Insights                                              │
│            │                                                        │
│            │  ┌────────────────────────────────────────────────┐    │
│            │  │                                                 │    │
│            │  │  YOUR AI VISIBILITY SCORE              72/100   │    │
│            │  │  ██████████████████████████████████░░░░░░░░░░  │    │
│            │  │                                                 │    │
│            │  │  Recall: 87%  Sentiment: 81% pos  Engines: 4/5 │    │
│            │  │  vs. category avg: +14%                         │    │
│            │  │  vs. top competitor: -6% (Brex: 78/100)        │    │
│            │  │                                                 │    │
│            │  └────────────────────────────────────────────────┘    │
│            │                                                        │
│            │  ─────────────────────────────────────────────         │
│            │                                                        │
│            │  WHERE YOU SHOW UP                                     │
│            │  ┌────────────────────────────────────────────────┐    │
│            │  │ ● Strong presence (mentioned in 4+ engines)    │    │
│            │  │   17 prompts — you're well-positioned here     │    │
│            │  │                                                 │    │
│            │  │ ◐ Partial presence (1-3 engines)               │    │
│            │  │   12 prompts — room to grow                    │    │
│            │  │                                                 │    │
│            │  │ ○ Not mentioned (competitors are)              │    │
│            │  │   9 prompts — these are your gaps              │    │
│            │  │                                                 │    │
│            │  │ [View all prompts by visibility →]              │    │
│            │  └────────────────────────────────────────────────┘    │
│            │                                                        │
│            │  HOW YOU'RE POSITIONED                                  │
│            │  ┌────────────────────────────────────────────────┐    │
│            │  │                                                 │    │
│            │  │  AI describes you as:                           │    │
│            │  │  "savings automation" (71% of mentions)         │    │
│            │  │  "modern UX" (54%)                              │    │
│            │  │  "fast onboarding" (41%)                        │    │
│            │  │  "corporate card" (38%)                         │    │
│            │  │                                                 │    │
│            │  │  AI does NOT associate you with:               │    │
│            │  │  "global payments" (Brex owns this)            │    │
│            │  │  "enterprise scale" (SAP, Coupa own this)      │    │
│            │  │  "receipt scanning" (Expensify owns this)      │    │
│            │  │                                                 │    │
│            │  └────────────────────────────────────────────────┘    │
│            │                                                        │
│            │  WHAT TO DO NEXT                                       │
│            │  ┌────────────────────────────────────────────────┐    │
│            │  │                                                 │    │
│            │  │  1. CLOSE THE GOOGLE AI GAP          Priority: │    │
│            │  │     You're mentioned in 4/5 engines   ██████░  │    │
│            │  │     but not Google AI. Google AI                │    │
│            │  │     cites nerdwallet.com and g2.com            │    │
│            │  │     — ensure you're listed there.              │    │
│            │  │                                                 │    │
│            │  │  2. OWN "ENTERPRISE EXPENSE"          Priority: │    │
│            │  │     3 prompts about enterprise expense ████░░░  │    │
│            │  │     tools don't mention you. Create             │    │
│            │  │     content targeting this segment.             │    │
│            │  │                                                 │    │
│            │  │  3. DEFEND AGAINST BREX               Priority: │    │
│            │  │     Brex overtook you in Claude for    ████░░░  │    │
│            │  │     2 prompts last week. Monitor and            │    │
│            │  │     consider positioning adjustments.           │    │
│            │  │                                                 │    │
│            │  │  [PRO+: See full action plan]                   │    │
│            │  │  [BUSINESS: Talk to your AEO strategist]        │    │
│            │  └────────────────────────────────────────────────┘    │
│            │                                                        │
└────────────┴────────────────────────────────────────────────────────┘
```

**Tier gating on Insights:**
- **Free:** Shows visibility score, "where you show up" summary, and top 1 recommendation. Rest blurred with upgrade CTA.
- **Pro:** Full insights, all recommendations, exportable.
- **Business:** Everything Pro has + strategist annotations, custom analysis, scheduled reviews.

---

## 2.6 REPORTS & EXPORT `[PRO+]`

**Purpose:** Generate and download reports. Weekly/monthly summaries. Shareable with stakeholders.

```
┌────────────┬────────────────────────────────────────────────────────┐
│            │                                                        │
│  SIDEBAR   │  Reports                              [PRO+]          │
│            │                                                        │
│            │  GENERATE REPORT                                       │
│            │  ┌────────────────────────────────────────────────┐    │
│            │  │ Report type:  [Visibility summary ▾]           │    │
│            │  │ Period:       [Last 30 days ▾]                 │    │
│            │  │ Include:      ☑ Competitors  ☑ Trends          │    │
│            │  │               ☑ Recommendations                │    │
│            │  │ Format:       [PDF ▾]                           │    │
│            │  │                                                 │    │
│            │  │ [Generate report]                               │    │
│            │  └────────────────────────────────────────────────┘    │
│            │                                                        │
│            │  RECENT REPORTS                                        │
│            │  ┌────────────────────────────────────────────────┐    │
│            │  │ Feb 2026 Visibility Summary        [Download]  │    │
│            │  │ Generated Feb 10 · PDF · 12 pages              │    │
│            │  ├────────────────────────────────────────────────┤    │
│            │  │ Jan 2026 Competitive Benchmark     [Download]  │    │
│            │  │ Generated Jan 31 · PDF · 8 pages               │    │
│            │  └────────────────────────────────────────────────┘    │
│            │                                                        │
│            │  EXPORT DATA                                           │
│            │  [Export all prompt data as CSV]                        │
│            │  [Export engine comparison as CSV]                      │
│            │  [Export change log as CSV]                             │
│            │                                                        │
└────────────┴────────────────────────────────────────────────────────┘
```

---

# PART 3: SYSTEM SCREENS

---

## 3.1 SIGNUP / ONBOARDING

**Purpose:** Get from "interested" to "seeing my data" in under 2 minutes.

```
STEP 1: CREATE ACCOUNT
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  Track how AI talks about your brand.                               │
│  Free. No credit card.                                              │
│                                                                     │
│  Email:     ┌─────────────────────────────┐                         │
│             │                             │                         │
│             └─────────────────────────────┘                         │
│  Password:  ┌─────────────────────────────┐                         │
│             │                             │                         │
│             └─────────────────────────────┘                         │
│                                                                     │
│  [Create free account]                                              │
│                                                                     │
│  or continue with [Google] [Microsoft]                              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘

STEP 2: ADD YOUR BRAND
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  What brand do you want to track?                                   │
│                                                                     │
│  ┌──────────────────────────────────────────┐                       │
│  │ Search for your brand...                 │                       │
│  └──────────────────────────────────────────┘                       │
│                                                                     │
│  ┌──────────────────────────────────────────┐                       │
│  │ ☐ Ramp — Expense Management              │ ← Found in index     │
│  │   Already tracking: 47 shared prompts     │                       │
│  │   Historical data: 84 days available      │                       │
│  └──────────────────────────────────────────┘                       │
│                                                                     │
│  Don't see your brand? [Add it manually]                            │
│                                                                     │
│  [Continue →]                                                       │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘

STEP 3: SELECT CATEGORIES
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  Which categories does Ramp compete in?                             │
│  (We auto-detected these based on AI data)                          │
│                                                                     │
│  ☑ Expense Management (34 brands, 312 questions)                    │
│  ☑ Corporate Cards (22 brands, 187 questions)                       │
│  ☐ Spend Management (18 brands, 143 questions)                      │
│  ☐ Accounts Payable (29 brands, 201 questions)                      │
│                                                                     │
│  [Continue →]                                                       │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘

STEP 4: YOUR DASHBOARD IS READY
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  ✓ Your brand is set up.                                            │
│                                                                     │
│  We found Ramp in 47 shared prompts across 2 categories.            │
│  84 days of historical data loaded into your dashboard.             │
│                                                                     │
│  Here's your snapshot:                                              │
│                                                                     │
│  Recall: 72%  ·  Engines: 4/5  ·  Trend: ▲ +6%                    │
│                                                                     │
│  [Go to dashboard →]                                                │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Key design principle:** No cold start. If the brand exists in the index, historical data loads instantly. The user sees value before they've done anything.

---

## 3.2 UPGRADE PROMPTS (Inline)

These aren't separate screens — they're inline nudges that appear contextually throughout the product.

```
PROMPT LIMIT NUDGE (on Prompts screen):
┌─────────────────────────────────────────────────────────────────────┐
│  ░░░░░░░░░░░░░░░░░░░░░░░░░░░  45/50 custom prompts used           │
│  You're close to your limit. Upgrade to Pro for 500 prompts,       │
│  60 days of history, and near-daily probing.                        │
│  [Upgrade to Pro — $249/mo →]                                       │
└─────────────────────────────────────────────────────────────────────┘

HISTORY CUTOFF NUDGE (on Dashboard chart):
┌─────────────────────────────────────────────────────────────────────┐
│  │ ████  visible data  ░░░░░░  blurred beyond 14 days              │
│  │                                                                  │
│  Your free plan shows 14 days. Unlock 60 days of trend data.       │
│  [Upgrade to Pro →]                                                 │
└─────────────────────────────────────────────────────────────────────┘

COMPETITOR BLUR (on Benchmarks screen):
┌─────────────────────────────────────────────────────────────────────┐
│  You       ████████████████████████░░  87%                          │
│  ░░░░░░░   ░░░░░░░░░░░░░░░░░░░░░░░░  ░░%   ← blurred             │
│  ░░░░░░░   ░░░░░░░░░░░░░░░░░░░░░░░░  ░░%   ← blurred             │
│                                                                     │
│  See how you compare to competitors.  [Unlock with Pro →]           │
└─────────────────────────────────────────────────────────────────────┘

BUSINESS UPSELL (on Insights screen):
┌─────────────────────────────────────────────────────────────────────┐
│  Want someone to build your AI visibility strategy?                 │
│  Business includes a dedicated AEO strategist who interprets        │
│  your data and tells you exactly what to do.                        │
│  [Talk to us about Business →]                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 3.3 SETTINGS

```
┌────────────┬────────────────────────────────────────────────────────┐
│            │                                                        │
│  SIDEBAR   │  Settings                                              │
│            │                                                        │
│  Profile   │  WORKSPACE                                             │
│  Billing   │  Name:    [Marcel's Workspace    ]                     │
│  Team      │  Brand:   Ramp  [Change brand]                         │
│  Notifs    │  Categories: Expense Management, Corporate Cards       │
│  API       │              [Manage categories]                        │
│            │                                                        │
│            │  TEAM MEMBERS (unlimited on all plans)                  │
│            │  marcel@ramp.com          Owner                        │
│            │  sarah@ramp.com           Member                       │
│            │  [Invite team member]                                   │
│            │                                                        │
│            │  PLAN                                                   │
│            │  Current: Free (50 prompts · 14 days history)          │
│            │  [Upgrade to Pro →]   [Compare plans]                   │
│            │                                                        │
│            │  NOTIFICATIONS                                          │
│            │  ☑ Weekly visibility digest (email)                     │
│            │  ☑ Alert when you appear/disappear from an answer       │
│            │  ☑ Alert when a competitor overtakes you                 │
│            │  ☐ Daily probe results                                  │
│            │                                                        │
│            │  API ACCESS [PRO+]                                      │
│            │  [Generate API key]                                     │
│            │                                                        │
└────────────┴────────────────────────────────────────────────────────┘
```

---

# PART 4: SCREEN MAP

How everything connects:

```
                        ┌──────────────┐
                        │   HOME (/)   │
                        └──────┬───────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
     ┌────────▼──────┐ ┌──────▼──────┐ ┌───────▼──────┐
     │  CATEGORIES   │ │   ANSWERS   │ │    TOOLS     │
     │  /categories/ │ │  /answers/  │ │   /tools/    │
     └───────┬───────┘ └──────┬──────┘ └──────┬───────┘
             │                │               │
     ┌───────▼───────┐ ┌─────▼──────┐        │
     │ CATEGORY      │ │  ANSWER    │        │
     │ DETAIL        │ │  DETAIL    │        │
     └───────┬───────┘ └────────────┘        │
             │                                │
     ┌───────▼───────┐                        │
     │ BRAND PROFILE │◄───────────────────────┘
     │ /[brand]/     │
     └───────┬───────┘
             │
     ┌───────▼───────┐
     │  COMPARISON   │
     │ /comparisons/ │
     └───────────────┘


     ═══════════════════ AUTH WALL ═══════════════════

     ┌───────────────────────────────────────────────┐
     │               SIGNUP / ONBOARDING              │
     │  create account → add brand → select cats →    │
     │  → dashboard ready                             │
     └──────────────────────┬────────────────────────┘
                            │
                   ┌────────▼────────┐
                   │   DASHBOARD     │
                   │   HOME          │
                   └────────┬────────┘
                            │
         ┌──────────┬───────┼───────┬──────────┐
         │          │       │       │          │
    ┌────▼───┐ ┌───▼────┐ ┌▼────┐ ┌▼───────┐ ┌▼──────┐
    │PROMPTS │ │LIBRARY │ │COMP │ │INSIGHTS│ │REPORTS│
    │MANAGER │ │BROWSER │ │BENCH│ │        │ │EXPORT │
    │        │ │        │ │PRO+ │ │        │ │ PRO+  │
    └────────┘ └────────┘ └─────┘ └────────┘ └───────┘
```

---

# PART 5: METRICS GLOSSARY

Every metric referenced in this doc, defined.

| Metric | Definition | Where it appears |
|--------|-----------|-----------------|
| **Recall %** | % of tracked prompts where your brand is mentioned in at least one engine | Dashboard, Category, Brand, Benchmarks |
| **Sentiment** | How AI describes you — positive, neutral, negative. Derived from language analysis of AI responses | Dashboard, Brand, Insights |
| **Engine Coverage** | How many of the 5 AI engines mention your brand (X/5) | Dashboard, Brand, Prompt detail |
| **Trend (30d)** | % change in recall over the last 30 days. ▲ up, ▼ down, ▬ flat | Dashboard, Category, Brand, Benchmarks |
| **Position** | Where your brand appears in the AI's response (#1 = mentioned first, #2 = second, etc.) | Prompt detail, Answer page, Comparison |
| **AI Visibility Score** | Composite 0-100 score combining recall, sentiment, engine coverage, and trend | Insights |
| **Sources Cited** | Which URLs the AI engine references when mentioning your brand | Brand profile, Answer page |
| **Probe Frequency** | How often prompts are sent to AI engines. Weekly (Free), near-daily (Pro/Business) | Settings, Dashboard |
| **Prompt Usage** | Custom prompts used vs. limit (50/500/2,000) | Dashboard, Prompts, Settings |
| **Category Average** | Mean recall % across all brands in a category — your benchmark | Dashboard chart, Insights |
| **Win/Lose/Gap** | Prompts where you outrank competitors (win), they outrank you (lose), or you're absent (gap) | Benchmarks, Insights |
| **Alignment** | Whether AI describes your brand the way you want to be described vs. how you actually are | Insights |
| **Change Events** | Discrete events: appeared in an answer, disappeared, position changed, competitor overtook | Dashboard feed, Notifications |
