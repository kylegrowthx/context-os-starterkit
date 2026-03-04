<metadata>
purpose: Track repetitive manual processes across the business to identify automation opportunities
audience: Founder, operators, anyone looking to reduce manual work
summary: Living document for brain-dumping repetitive workflows, organized by category with time cost, pain level, and automation potential for each process.
domain: operations
confidence: working
context_tier: 2
last_updated: 2026-02-27
</metadata>

# Process & Automation Tracker

A running inventory of repetitive manual work. Brain dump processes here — they'll get organized, scored, and turned into an automation backlog.

## How to use this

Describe what you do. Be specific about steps, tools, and frequency. Each process gets scored on:

| Field | What it captures |
|-------|-----------------|
| **Frequency** | How often (per call, daily, weekly, monthly) |
| **Time per occurrence** | Rough estimate in minutes |
| **Pain level** | Low / Medium / High |
| **Tools involved** | What you currently use |
| **Automation ideas** | What could replace or reduce the manual work |
| **Status** | Not started / Exploring / In progress / Automated |

---

## 1. Client Work

### 1.1 Client Call Workflow

**Status:** Not started
**Pain level:** High
**Total estimated time per call:** ~60-90 min (for a 30-min call)

The ratio is off — a 30-minute call generates 60+ minutes of surrounding work. This is the single biggest time sink.

#### Pre-call (~15-20 min)

| Step | What happens | Frequency | Time | Tools |
|------|-------------|-----------|------|-------|
| Review last call notes | Pull up previous meeting notes, scan action items, check what was promised | Per call | 5-10 min | Notion |
| Check deliverable status | See where things stand on active workstreams | Per call | 5 min | Notion, Slack |
| Prepare agenda | Write up talking points, questions, updates to share | Per call | 5-10 min | Notion |

**What's painful:** Context-switching between Notion pages, Slack threads, and deliverable trackers to piece together "where are we with this client." No single view.

**Automation ideas:**
- Auto-generate pre-call brief from last meeting transcript + open action items + recent deliverable activity
- AI agent that pulls context from client folder, recent Slack threads, and Notion and produces a one-page prep doc
- Template pre-populated agenda based on engagement week number

#### During call (~30 min)

| Step | What happens | Frequency | Time | Tools |
|------|-------------|-----------|------|-------|
| Run the meeting | Facilitate discussion, present updates, take live notes | Per call | 30 min | Zoom/Google Meet |
| Capture action items | Write down commitments and next steps in real-time | Per call | Embedded | Notion or scratch notes |

**What's painful:** Splitting attention between facilitating and capturing. Things get missed. Fireflies records but the raw transcript needs processing.

**Automation ideas:**
- Fireflies transcript auto-summarized into structured format (decisions, action items, open questions)
- AI extracts action items and maps them to owners automatically
- Live AI note-taker that produces structured notes during the call

#### Post-call (~20-30 min)

| Step | What happens | Frequency | Time | Tools |
|------|-------------|-----------|------|-------|
| Write follow-up summary | Summarize key points, decisions, action items | Per call | 10-15 min | Notion, Email/Slack |
| Update Notion docs | Move action items, update status pages, log meeting notes | Per call | 5-10 min | Notion |
| Send follow-up message | Share summary with client and internal team | Per call | 5 min | Slack, Email |
| Update client context doc | Keep the running client context file current | Per call | 5-10 min | This repo |

**What's painful:** Triple-entry — writing the summary, then updating Notion, then updating the context doc. Same information reformatted three times for three destinations.

**Automation ideas:**
- Transcript-to-structured-summary pipeline (Fireflies → AI → formatted output)
- Auto-update Notion pages from structured summary
- Auto-draft follow-up Slack/email from call summary
- Auto-append meeting notes to client context doc in this repo
- Single "process call" action that handles all post-call updates

#### Recurring maintenance (~15-30 min/week per client)

| Step | What happens | Frequency | Time | Tools |
|------|-------------|-----------|------|-------|
| Keep Notion current | Ensure project pages, timelines, and status are accurate | Weekly | 10-15 min | Notion |
| Sync context across tools | Make sure Slack, Notion, and repo context match | Weekly | 5-10 min | Multiple |
| Review open action items | Check nothing fell through the cracks | Weekly | 5-10 min | Notion |

**What's painful:** Information lives in too many places. Notion is the client-facing source of truth, this repo is the AI-facing source of truth, Slack has the real-time context. Keeping them in sync is entirely manual.

**Automation ideas:**
- Notion → repo sync for client status updates
- Weekly auto-generated "open items" digest per client
- Slack bot that surfaces stale action items

---

## 2. Internal Ops

*No processes documented yet. Brain dump here.*

---

## 3. Content Production

*No processes documented yet. Brain dump here.*

---

## 4. Sales & Pipeline

*No processes documented yet. Brain dump here.*

---

## 5. Admin & Finance

*No processes documented yet. Brain dump here.*

---

## Automation Priority Matrix

Once enough processes are documented, prioritize by plotting **pain x frequency**:

| | Low frequency | High frequency |
|---|---|---|
| **High pain** | Fix when you can | Automate first |
| **Low pain** | Ignore for now | Quick wins |

## Next Steps

- Keep brain-dumping processes into this doc
- Score and prioritize the backlog quarterly
- Build or buy automations starting with the top-right quadrant
