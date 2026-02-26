---
name: contact-dossier
description: Create or update a contact dossier in /records/contacts. Use when the user mentions a person they've met, wants to save contact details, asks to "create a contact", "update a contact", or after processing transcripts that mention new or existing contacts.
---

# Contact Dossier

Create or update a contact file in `/records/contacts/` with all known personal and professional context.

## Inputs / Outputs

| | What | Example |
|---|---|---|
| **Input** | Person name + any context (meeting, transcript, user notes) | "Create a contact for Brian Mullen from Coralogix" |
| **Sources** | Transcripts, HubSpot, user-provided context, meeting notes | `records/transcripts/`, HubSpot MCP |
| **Output** | Contact dossier saved to records | `records/contacts/brian-mullen-v1.md` |

## Overview

This skill:
1. Searches for an existing contact file in `/records/contacts/`
2. Gathers context from available sources (transcripts, HubSpot, user input)
3. Creates or updates a structured dossier
4. Cross-links the contact file to related transcripts (and vice versa)
5. Updates `records/contacts/INDEX.md`

## When to Trigger

- User says "create a contact", "save contact", "add to contacts", "update contact"
- User asks to build a profile or dossier on someone
- After processing a transcript that mentions a significant contact not yet in `/records/contacts/` (auto-triggered by contact-transcript-linking rule — no user confirmation needed)
- User provides personal details about a person (SMS, notes, observations)

## Workflow

### Step 1: Check for Existing Contact

Search `records/contacts/` for a file matching the person's name:
- Filename pattern: `firstname-lastname-v1.md`
- Also search by company or email if name is ambiguous

If found: **update** the existing file (add new information, update timeline, refresh `last_updated`).
If not found: **create** a new file.

### Step 2: Gather Context

Pull from all available sources. Don't ask the user for things you can look up.

**HubSpot (if available):**
- Search contacts by name/email: `hubspot-search-objects` (objectType: contacts)
- Get company details: `hubspot-search-objects` (objectType: companies)
- Get associated deals: `hubspot-list-associations` (contacts → deals)
- Get associated meetings: `hubspot-list-associations` (contacts → meetings)
- Batch read for full details: `hubspot-batch-read-objects`
- Capture: name, title, email, company, lifecycle stage, deal info, meeting history

**Transcripts:**
- Search `records/transcripts/` for files mentioning this person
- Use grep to find their name across transcript files
- Read matching transcripts and extract:
  - Personal details (location, family, interests, background)
  - Professional context (role, priorities, how they think)
  - Relationship context (how they know Marcel, who introduced them)
  - Key quotes that reveal personality or priorities
  - Action items assigned to them
  - Timeline events

**User-provided context:**
- SMS/text conversations
- In-person observations
- Relationship notes
- Personal details not captured in meetings

### Step 3: Write the Dossier

Use this template structure. Not every section is required — include what you have.

```markdown
# Firstname Lastname — Contact Dossier

<metadata>
purpose: Contact dossier for Firstname Lastname, Title at Company
domain: sales, relationships
company: Company Name
role: Their Title
hubspot_contact_id: (if known)
hubspot_company_id: (if known)
tags: client, partner, investor, friend, advisor (pick relevant ones)
confidence: high | medium | low
last_updated: YYYY-MM-DD
</metadata>

---

**Role:** Title, Company
**Email:** work@company.com
**Personal Email:** personal@email.com (if known)

---

## Personal

- **Location:** Where they live, neighborhood details
- **Family:** Spouse, kids, relevant personal details
- **Interests:** Hobbies, sports, shared interests with Marcel
- Other personal context (neighbors, mutual friends, etc.)

---

## Career Background

- **Current Company** — role, when they started, what they're focused on
- **Previous roles** — relevant career history
- **Key connections** — people they know in common with Marcel/GrowthX

---

## How They Think

- Bullet points capturing their decision-making style
- What they prioritize
- How they approach problems
- What they value in partnerships

---

## Key Quotes (from meetings)

> Direct quotes that reveal personality or priorities

---

## Relationship to GrowthX

- How the relationship started (who introduced, when, context)
- Current deal status (if applicable)
- Relationship strength and personal connection

---

## Their Team

| Name | Title | Notes |
|------|-------|-------|
| Name | Title | Relevant context |

(Include if they're a decision-maker with a team we interact with)

---

## Timeline

| Date | Event |
|------|-------|
| **YYYY-MM-DD** | What happened — include meeting names, personal interactions, deal milestones |

---

## Meeting Transcripts

- `records/transcripts/YYYY-MM-DD-meeting-name.md`
```

### Section Guidelines

**Personal:** Capture everything — neighborhood, family, kids' schools, hobbies, shared interests. This is what makes relationships real. Never fabricate personal details.

**Career Background:** Focus on roles and connections relevant to the relationship with Marcel/GrowthX. Include mutual connections and shared professional history.

**How They Think:** Distill from their words in meetings. What do they prioritize? How do they make decisions? What frustrates them? This section should help anyone at GrowthX prepare for a conversation with this person.

**Key Quotes:** Pull 3-5 direct quotes from transcripts that best capture who this person is. Only use actual quotes from transcripts.

**Timeline:** Chronological record of every interaction — meetings, texts, chance encounters, deal milestones. This is the relationship history.

**Meeting Transcripts:** Always link to the source transcripts. Use relative paths from the repo root.

### Step 4: Cross-Link Transcripts

For every transcript referenced in the contact file, add or update a `## Participants` or `## Related Contacts` section in the transcript linking back to the contact dossier.

If the transcript already has a participants list in metadata, that's sufficient — no need to add a redundant section. But if the transcript doesn't reference `records/contacts/`, add a brief section after the metadata:

```markdown
## Related Contacts

- [Brian Mullen](../contacts/brian-mullen-v1.md) — CMO, Coralogix
```

Only add this for contacts that have dossier files. Don't create links for people without contact files.

### Step 5: Update INDEX.md

Add or update the entry in `records/contacts/INDEX.md`:

```markdown
| [firstname-lastname-v1.md](firstname-lastname-v1.md) | Title, Company | tags |
```

### Step 6: Report Back

After saving, confirm:
- File saved to: `records/contacts/<filename>.md`
- Contact: Name, Title at Company
- Sources used: (transcripts, HubSpot, user notes)
- Sections populated: (list which sections have content)
- Cross-links created: (list transcript files updated)

## Updating an Existing Contact

When updating (not creating), follow these principles:

1. **Don't overwrite** — merge new information with existing content
2. **Append to timeline** — add new events, don't reorganize old ones
3. **Update metadata** — refresh `last_updated` date
4. **Add new quotes** — if transcripts have new revealing quotes, add them
5. **Refresh deal info** — check HubSpot for current deal status
6. **Add new transcript links** — append new meeting references

## Edge Cases

### Person appears in transcript but not important enough for a dossier
Not everyone needs a contact file. Create dossiers for:
- People Marcel has direct interaction with
- Decision-makers at clients or prospects
- People with personal relationship context (neighbors, friends, advisors)
- Repeat contacts who appear in multiple transcripts

Skip dossiers for:
- One-time meeting attendees with no direct interaction
- People only mentioned by name but not present
- Large group participants with no individual context

### Multiple people at the same company
Create individual dossiers. Link them to each other in the "Their Team" section and to the same company record in `records/customers/` if one exists.

### Contact changes companies
Update the file in place: move old company to Career Background, update current role, refresh metadata. Don't create a new version unless the change is fundamental to the relationship.
