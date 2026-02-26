<metadata>
purpose: Agent instructions for navigating and working with Marcel's Gmail
audience: AI agents (Claude, Cursor, etc.)
domain: operations
related_files: context/context-routing.md, context/personal/user-manual.md
last_updated: 2026-02-26
</metadata>

# Gmail Organization — Agent Instructions

How Marcel organizes his Gmail at `marcel@growthxlabs.com`. Follow these conventions when searching, triaging, drafting, or summarizing email.

## Account Overview

Marcel operates across **three email addresses**, all flowing into the same Gmail inbox:

| Address | Usage |
|---------|-------|
| `marcel@growthxlabs.com` | Primary personal/ops — investor intros, personal business, some outbound |
| `marcel@growthx.ai` | Company-facing — sales outbound, client conversations, HubSpot sequences |
| `marcel.santilli@growthx.ai` | Automated sequences — Ordinal/HubSpot outbound, inbound lead replies |

When searching for Marcel's conversations, check all three addresses. Sent mail may come from any of them depending on context.

## Core System: Numbered Triage Labels

Marcel's primary workflow is a **numbered triage system** using labels 1–9. These labels represent **action states**, not topics. They tell agents what to do with a thread, not what it's about.

| Label | Gmail Label ID | Meaning | Agent Behavior |
|-------|---------------|---------|----------------|
| **1: to respond** | `Label_1` | Marcel needs to reply to this thread | High priority. Draft a response or surface for review. |
| **2: FYI** | `Label_2` | Awareness only — no action needed | Read if relevant to current task, but don't flag for action. |
| **3: comment** | `Label_3` | Low-priority or spam-adjacent — cold outreach, bulk newsletters, event invites | Ignore unless specifically asked. Treat as noise. |
| **4: notification** | `Label_4` | System notifications, calendar acceptances | Skip. Only check if hunting for a specific confirmation. |
| **5: meeting update** | `Label_5` | Calendar invites, Zoom links, event RSVPs, scheduling changes | Check when looking for meeting logistics or scheduling context. |
| **6: awaiting reply** | `Label_6` | Marcel sent the last message and is waiting for a response | Monitor for follow-up opportunities. If thread is stale (7+ days), flag for re-engagement. |
| **7: actioned** | `Label_7` | Thread has been handled — no further action needed | Archive-equivalent. Don't surface unless searching history. |
| **8: marketing** | `Label_8` | SaaS notifications, Luma RSVPs, tool confirmations, Fyxer meeting summaries, beehiiv, Deel, Mercury alerts | Low priority. Search here for receipts, meeting summaries, or tool notifications. |
| **9: important** | `Label_9` | Manually flagged as important by Marcel | High signal. Treat like starred — these threads matter. |

### Triage Label Patterns (from 60-day analysis)

**Label 1 (to respond):** Podcast intro threads, investor email intros, capacity/staffing updates from team leads (e.g., Ryan Singer), partner follow-ups. These are threads where someone is waiting on Marcel.

**Label 2 (FYI):** Intro emails where Marcel is CC'd but doesn't need to act (e.g., Adam Coccari at HubSpot Ventures sending warm intros), team updates, industry news shared by contacts.

**Label 3 (comment):** Cold outreach from vendors, unsolicited pitches, low-value newsletters, event marketing. This is Marcel's "probably junk" bucket.

**Label 6 (awaiting reply):** Active sales threads where Marcel or Tyler sent the last message (Inworld, Cognition, Greenhouse, Obsidian), partner conversations waiting on the other side, intro threads where Marcel replied and is waiting for scheduling.

**Label 8 (marketing):** Vercel deploy notifications, Mercury bank alerts, Deel HR notifications, Apple receipts, Uber receipts, Luma event RSVPs, Fyxer AI meeting summaries, beehiiv newsletter metrics.

## Archive Labels (Topic-Based Filing)

Below the triage labels, Marcel uses **archive sublabels** for long-term filing by topic. These are mostly auto-applied by Gmail filters based on the receiving email alias.

| Label | Gmail Label ID | What's Filed Here | Auto-Routing Alias |
|-------|---------------|-------------------|-------------------|
| **Archives/AP & AR** | `Label_4451982147305217533` | Vendor invoices, payment confirmations, accounts payable/receivable (Exa, SchoolAI, Grammarly offboarding, bill.com) | `ap@growthxlabs.com`, `ap@growthx.ai` |
| **Archives/Contracts** | `Label_7763635233661955827` | SOWs, amendments, renewals via PandaDoc, legal correspondence | `legal@growthxlabs.com`, `legal@growthx.ai` |
| **Archives/GrowthX** | *(ID not yet confirmed)* | General company threads — internal ops, team comms | — |
| **Archives/Investors** | `Label_5844974038263899448` | Investor/advisor threads (Ryan Singer, Anthony Cessario), fundraising, cap table, Carta exports, some AR routing | `ar@growthxlabs.com`, `ar@growthx.ai` |
| **Archives/Personal** | `Label_5576783550406003735` | Tax memos (Andersen), 83(b) elections, personal legal, secondary transactions, wire instructions | — |
| **Archives/Sales** | `Label_5580979988848303200` | Inbound lead replies, prospect qualification threads, pipeline conversations | `sales@growthx.ai` |
| **Archives/Tools@ alias** | `Label_880303754161540189` | SaaS account emails — Anthropic, OpenAI, GitHub, DigitalOcean, infrastructure tooling | `tools@growthxlabs.com` |

## Email Alias Routing System

Marcel uses functional email aliases that auto-route to archive labels via Gmail filters. This is how topic-based filing happens automatically:

| Alias | Routes To | Example Content |
|-------|-----------|-----------------|
| `tools@growthxlabs.com` | Archives/Tools@ alias | API keys, SaaS account notices, infrastructure alerts |
| `ap@growthxlabs.com` / `ap@growthx.ai` | Archives/AP & AR | Vendor invoices, payment requests |
| `ar@growthxlabs.com` / `ar@growthx.ai` | Archives/Investors | BILL/Ramp payment confirmations, investor correspondence |
| `legal@growthxlabs.com` / `legal@growthx.ai` | Archives/Contracts | PandaDoc SOWs, contract amendments |
| `sales@growthx.ai` | Archives/Sales | Inbound lead replies, prospect threads |
| `gtm@growthx.ai` | Label_8 (marketing) or Label_3 (comment) | GTM-related notifications, mixed routing |

**Key insight:** The triage labels (1–9) and archive labels serve different purposes and are often applied together. A thread might be labeled both "6: awaiting reply" (action state) AND "Archives/Sales" (topic). Agents should use triage labels for workflow and archive labels for search/retrieval.

## Gmail Categories (Tabs)

Marcel uses Gmail's default category tabs as the first-level filter:

| Category | What Lives Here | Agent Behavior |
|----------|----------------|----------------|
| **Primary** (`CATEGORY_PERSONAL`) | Direct 1:1 emails — intros, investor threads, client conversations, team comms | **High-priority mail lives here.** Always check first. |
| **Updates** (`CATEGORY_UPDATES`) | SaaS notifications, receipts, Deel/HR alerts, tool confirmations | Low priority. Search for specific receipts or notifications. |
| **Promotions** (`CATEGORY_PROMOTIONS`) | Marketing emails, newsletters, event invites (AI Council, Warriors, We Work Remotely) | Lowest priority. Skip unless asked about events/newsletters. |
| **Forums** (`CATEGORY_FORUMS`) | Some inbound lead replies route here (via `sales@growthx.ai` CC patterns) | Check when looking for prospect replies not in Primary. |
| **Social** (`CATEGORY_SOCIAL`) | LinkedIn, Behance notifications | Almost never relevant. Ignore unless asked. |

## How Marcel Uses Stars

Starred emails are **reference bookmarks** — not a to-do list. Patterns observed:

- Tax and legal documents (83(b) election memos, engagement letters)
- Financial transactions (wire instructions, secondary sale details)
- Stock/equity documentation (Carta exports, grant agreements)

**Agent guidance:** If asked to find important documents, financial records, or legal files — search starred messages first.

## How Marcel Uses Drafts

Marcel keeps a small number of drafts (typically 2–5). These are usually:

- Reply-all intros where he's composing a warm intro response
- Follow-up emails to prospects or new connections
- Seasonal/holiday outreach drafts

Drafts are active work — don't treat them as archive.

## Email Patterns by Role

### As CEO (sales + partnerships)
- Threads carry both triage labels (usually Label_6 "awaiting reply") AND Archives/Sales
- Usually sent from `marcel@growthx.ai` or `marcel@growthxlabs.com`
- Follow-up pattern: Tyler (AE) handles initial call → Marcel jumps in to close ("Enjoyed chatting with Tyler about your use case...")
- CCs `tyler@growthx.ai` on deal threads

### As Founder (investor relations)
- Threads carry Label_2 (FYI) for awareness or Label_1 (to respond) for action
- Filed under Archives/Investors
- HubSpot Ventures (Adam Coccari) is an active referral source
- Pattern: investor intro → Marcel replies within hours → loops in EA (Dignory) for scheduling

### As Individual (personal/legal/finance)
- Threads filed under Archives/Personal
- Starred for reference
- Involves Andersen (tax), Madrona (investor), Bridget (ops)

## Search Strategy for Agents

### By action needed:
1. **What needs Marcel's reply?** → `label:Label_1` (1: to respond)
2. **What is Marcel waiting on?** → `label:Label_6` (6: awaiting reply)
3. **What's been handled?** → `label:Label_7` (7: actioned)

### By topic:
1. **Client/prospect conversations:** → `label:Label_5580979988848303200` (Archives/Sales) or `CATEGORY_PERSONAL` + company domain
2. **Inbound leads:** → `label:Label_5580979988848303200` or `to:sales@growthx.ai`
3. **Investor relations:** → `label:Label_5844974038263899448` (Archives/Investors)
4. **Legal/tax/finance:** → `is:starred` or `label:Label_5576783550406003735` (Archives/Personal)
5. **Contracts/SOWs:** → `label:Label_7763635233661955827` (Archives/Contracts)
6. **Vendor payments:** → `label:Label_4451982147305217533` (Archives/AP & AR)
7. **Tool/SaaS accounts:** → `label:Label_880303754161540189` (Archives/Tools@ alias)
8. **Meeting logistics:** → `label:Label_5` (5: meeting update)
9. **Receipts/notifications:** → `label:Label_8` (8: marketing) or `CATEGORY_UPDATES`

### By person:
When searching for a **person**, always try both `from:` and `to:` across all three email addresses.

## Important Contacts (Recurring)

| Person | Email | Context |
|--------|-------|---------|
| Adam Coccari | acoccari@hubspot.com | HubSpot Ventures — active referral partner |
| Tyler Pavlas | tyler@growthx.ai | GrowthX AE — on most sales threads |
| Dignory Carmona | dignory@growthx.ai | EA to Marcel — scheduling, logistics |
| Bridget McGillivray | bridget@growthx.ai | Ops — contracts, Carta, legal coordination |
| Nadia Hamade | hamadena@gmail.com | Personal — tax/legal documents |
| Ryan Singer | — | Advisor — capacity/staffing discussions |

## Rules for Agents

1. **Never bulk-read inbox.** Search with intent — use labels, categories, and sender filters.
2. **Primary tab is king.** If looking for anything Marcel cares about, start in `CATEGORY_PERSONAL`.
3. **Triage labels = action state.** Use labels 1–9 to understand what Marcel needs to do with a thread.
4. **Archive labels = topic filing.** Use Archives/* labels to find threads by subject matter.
5. **Stars = reference docs**, not action items. Check starred for legal, financial, and equity docs.
6. **Check all three addresses** when searching for Marcel's sent or received mail.
7. **Respect sensitivity.** Financial, legal, and equity threads (Archives/Personal, Archives/Investors, Archives/Contracts) contain confidential information. Flag before summarizing or sharing.
8. **Drafts are in-flight.** Don't modify or send drafts without explicit permission.
9. **Label_6 threads older than 7 days** may need a follow-up nudge — flag these proactively when reviewing pipeline.
10. **Alias routing is automatic.** Don't re-apply archive labels manually — Gmail filters handle this via the alias system.
