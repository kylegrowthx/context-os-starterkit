# Data Sources for Account Assessment

This reference lists every data source to query during an account assessment, organized by collection phase. Use Notion search, Slack search, and browser tools as indicated.

## Phase 1: Notion — Account Metadata

### ClientDB
- **How to find**: Search Notion for the client name within the ClientDB database
- **Extract**: Account Name, Health Flag (🔴/🟡/🟢), MRR, Contract Term, Start Date, Renewal Date, Pod Assignment, EM, Current ME, Workstream Type, Latest Health Scores (Relationship, Quantity, Quality, Performance, Strategy on 1-5 scale)
- **Historical scores**: Scroll through weekly health score entries for trend data

### Client Strategy Sprint Tracker
- **How to find**: Query the Notion database "CLIENT STRATEGY SPRINT TRACKER" (data source: `collection://2102ba60-bc74-8058-b988-000b509f811f`) for the client name
- **Extract**: Sprint Kickoff Date, Sprint Length (weeks), Transition Date (when Sprint ends and Growth Execution begins), Contract Value (Sprint SOW), Opt-in or Opt-out model, Sprint Status (current week or Done), Director/EM assignments during Sprint, ME assignments during Sprint, related Strategy Sprint Project Page link
- **Why it matters**: These dates establish the engagement lifecycle. The Transition Date is the true Growth Execution start date; the Renewal Date in ClientDB is typically 12 months after the Transition Date. Without this data, timeline phases will be imprecise.

### Client Operating Manual
- **How to find**: Search Notion for "{Client Name} Operating Manual" or "{Client Name} Client Operating Manual"
- **Extract**: Client contacts (names, roles, emails), content pipeline details, Atlas workspace link, Claude project links, Google Drive folder link, Airtable ContentOS link, Fathom link, Linear ticket, editorial process notes, style preferences, brand guidelines, CMS (Webflow/WordPress/etc.)
- **Critical links to capture**: Atlas Editorial Pipeline URL, Claude Post-Process Project URL, Looker Backend URL, ContentOS Airtable URL, Google Drive folder URL, Linear publishing ticket URL, Fathom call recordings URL, Content Strategy page URL

### Atlas Editorial Pipeline (Required)
- **Why it's required**: Atlas is GrowthX's content operations platform. Every active account has an Atlas pipeline where articles move through production stages. The Atlas Editorial Pipeline link is the first entry in the Key Links table and must be present in every report.
- **How to find (try in order)**:
  1. Check the Client Operating Manual — some manuals include a direct Atlas URL (look for `atlas.growthx.ai` links or references to the Atlas workspace/pipeline)
  2. If not in the Operating Manual, search Slack: `atlas.growthx.ai in:#d-int-{clientslug}` — team members often share Atlas pipeline links when onboarding MEs or discussing production
  3. If still not found, search Slack more broadly: `atlas.growthx.ai {client name}` across all channels
- **URL pattern**: `https://atlas.growthx.ai/accounts/{id}/workspaces/{workspace_id}/projects/{project_id}/task_pipelines/{pipeline_id}`
- **If not found**: Flag it as a data gap in the report — "Atlas Editorial Pipeline URL not found in Operating Manual or Slack; confirm with EM"

### Editorial Checklist
- **How to find**: Search Notion for "Editorial Checklist - {Client Name}" or "Editorial Checklist {Client Name}"
- **Extract**: Link to the checklist page (include in Key Links table)

### Weekly Sync Notes
- **How to find**: Search Notion for "{Client Name}" filtered to recent weeks, look for sync/meeting notes with "Week" numbering
- **Extract**: Key discussion points, action items, performance data shared in syncs, client feedback, escalation decisions
- **Go back**: At least 4-6 weeks of sync notes for trend context

### Weekly Actions / Production Notes
- **How to find**: Search Notion for "Weekly Actions" or "Actions" related to the client
- **Extract**: Recent action items, status updates, pending client-side actions

## Phase 2: Slack — Internal Communications

### Internal Channel (#d-int-{client})
- **Search**: `in:#d-int-{clientslug}` for recent 60-90 days
- **What to look for**: ME assignment changes, EM transitions, internal escalations, production blockers, handoff discussions, team concerns, Airtable/pipeline issues
- **Key signals**: Messages from leadership (Andi, Marcel, Bridget, etc.), ME introduction messages, handoff threads

### External Channel (#d-ext-{client})
- **Search**: `in:#d-ext-{clientslug}` for recent 60-90 days
- **What to look for**: Client communications, content feedback, brand guideline changes, approval delays, sync scheduling, publishing confirmations
- **Key signals**: Messages from client contacts, content review threads, approval bottlenecks

### At-Risk Alerts
- **Search**: `in:#d-at-risk-alerts {client name}` for any mentions
- **What to look for**: When account was flagged, who flagged it, what action was proposed, resolution status
- **Channel**: #d-at-risk-alerts

## Phase 3: Performance Data

### Performance Reports (Notion)
- **How to find**: Search Notion for "{Client Name} Performance" or look for monthly performance report links in the ClientDB entry
- **Extract**: Pillar growth percentages, keyword ranking changes, traffic trends, SERP wins, AEO/Scrunch metrics

### Screaming Frog / Technical SEO
- **How to find**: Mentioned in sync notes or Slack channels
- **Extract**: Audit findings, technical issues, fixes implemented vs. pending

### Scrunch / CheckThat.ai
- **How to find**: Mentioned in sync notes, performance reports, or Slack
- **Extract**: AEO visibility scores, citation metrics, brand positioning trends

## Phase 4: Additional Context

### Google Drive
- **How to find**: Link in Client Operating Manual
- **Use**: Verify content volume, draft status, review pipeline

### Fathom
- **How to find**: Link in Client Operating Manual
- **Use**: Review recent call recordings for client sentiment and unwritten context
