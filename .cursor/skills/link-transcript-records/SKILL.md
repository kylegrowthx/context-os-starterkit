---
name: link-transcript-records
description: Update meeting records, contact dossiers, and INDEX files after a transcript has been enriched. Works on any transcript regardless of source (Fireflies or Fathom). Triggers on "link transcript", "update meeting record", "sync transcript contacts", "link contacts to transcript", "post-process transcript".
---

# Link Transcript Records

After a transcript is enriched and saved to `records/transcripts/`, this skill syncs all related records: the meeting record in `records/meetings/`, contact dossiers in `records/contacts/`, and INDEX files.

This is a **cross-cutting** skill — it works on any enriched transcript regardless of whether it came from Fireflies or Fathom.

## Inputs / Outputs

| | What | Example |
|---|---|---|
| **Input** | Path to an enriched transcript `.md` file | `records/transcripts/2026-02/2026-02-26-flodesk-growthx-intro.md` |
| **Output** | Updated meeting record, contact dossiers, INDEX files | `records/meetings/2026-02/2026-02-26-flodesk-growthx-intro.md` updated |

## When to Trigger

- After `enrich-fireflies-transcript` completes
- After `enrich-fathom-transcript` completes
- When user says "link transcript", "update meeting record", "sync transcript contacts"
- When a transcript exists but its meeting record or contacts haven't been updated

## Workflow

### Step 1: Read the Transcript

Read the enriched transcript file and extract:
- **Date** from metadata
- **Fireflies ID** or **Fathom recording ID** from metadata
- **Transcript URL** from metadata
- **Participants** from metadata
- **Title** from the H1 heading
- **Summary** (first 2-3 sentences)
- **Source** (`fireflies` or `fathom`) from metadata

### Step 2: Update Meeting Record

Search `records/meetings/YYYY-MM/` for a matching meeting record:
- Match by date prefix + title keyword overlap (2+ matching words)
- Account for timezone shifts (+/- 1 day on date)

**If found**, update the meeting record:

```markdown
has_transcript: true
fireflies_id: <meeting_id>  (or fathom_recording_id for Fathom)
transcript_url: <url>
transcript_file: records/transcripts/YYYY-MM/YYYY-MM-DD-filename.md
last_updated: <today's date>
```

Update the `## Transcript` section:
```markdown
## Transcript

Full transcript available: [View transcript](../transcripts/YYYY-MM-DD-filename.md)
```

Enrich the Attendees table with roles and titles learned from the transcript. For each attendee:
- Fill in Role if we learned it from the transcript
- Fill in Company from email domain or transcript context
- Link to contact dossier if one exists: `[dossier](../contacts/firstname-lastname-v1.md)`

**If no meeting record exists** (e.g., meeting wasn't synced from calendar yet), create one following the format used by the sync-meetings skill:

```markdown
# Meeting Title

<metadata>
date: YYYY-MM-DD
time: HH:MM ET
duration: X minutes
organizer: organizer_email
attendees: Name1 (email1), Name2 (email2)
calendar_event_id:
has_transcript: true
fireflies_id: <id>
transcript_url: <url>
transcript_file: records/transcripts/YYYY-MM/filename.md
last_updated: YYYY-MM-DD
</metadata>

---

## Attendees

| Name | Email | Role | Company | Contact File |
|------|-------|------|---------|--------------|
| ... | ... | ... | ... | ... |

---

## Transcript

Full transcript available: [View transcript](../transcripts/YYYY-MM-DD-filename.md)
```

### Step 3: Update Contact Dossiers

Apply the full contact-transcript-linking rule (`.cursor/rules/contact-transcript-linking.mdc`):

**3a: Identify external participants**

Separate participants into:
- **GrowthX team** — anyone with `@growthxlabs.com` or `@growthx.ai` email
- **External contacts** — everyone else

**3b: Match against existing dossiers**

Search `records/contacts/` for matching files:
1. Exact filename match: `firstname-lastname-v1.md`
2. Partial name match (first name + last name)
3. Email match in metadata blocks

**3c: Update existing dossiers**

For each external person who HAS a contact dossier:

1. Add transcript to `## Meeting Transcripts` section (if not already listed):
   ```markdown
   - `records/transcripts/YYYY-MM/YYYY-MM-DD-meeting-name.md`
   ```

2. Add timeline entry to `## Timeline` table:
   ```markdown
   | YYYY-MM-DD | Meeting: descriptive meeting name — one-line summary of what was discussed |
   ```

3. Extract and merge new details into appropriate sections:
   - New role/title → update Career Background
   - New personal details → update Personal section
   - New quotes → add to Key Quotes
   - New team members mentioned → update Their Team table

4. Update metadata — set `last_updated: YYYY-MM-DD`

5. Don't overwrite — only add new information, never remove existing content

**3d: Auto-create dossiers for significant new contacts**

Create a dossier (don't ask) if the person meets ANY of these criteria:
- They speak directly in the meeting (not just mentioned)
- They're a decision-maker, client contact, or prospect
- Personal details are shared about them

Skip dossier creation for:
- Passive attendees with no speaking role and no context
- People only mentioned by first name with no identifying info
- Bots, AI assistants, or automated participants

Create using the contact-dossier skill template (`.cursor/skills/contact-dossier/SKILL.md`). Set `confidence: low` for auto-created dossiers.

**3e: Tag the transcript with Related Contacts**

Add a `## Related Contacts` section to the transcript, placed after the metadata block and before the Summary section:

```markdown
## Related Contacts

- [Natalie Franke](../contacts/natalie-franke-v1.md) — CMO, Flodesk
- [Axel Florence](../contacts/axel-florence-v1.md) — Head of Growth, Flodesk
```

Rules:
- Only link contacts that have dossier files (existing or just-created)
- Include role and company after the name
- Skip GrowthX employees
- If a Related Contacts section already exists, merge new contacts (don't duplicate)

### Step 4: Update INDEX Files

**`records/transcripts/INDEX.md`**
- Add row for the new transcript if not already listed
- Follow existing format

**`records/contacts/INDEX.md`**
- Add rows for any newly created contact dossiers
- Format: `| [filename](filename) | Full Name | Company | Role | Tags |`
- Keep alphabetically sorted

**`records/meetings/INDEX.md`**
- Update if meeting record was modified or created

### Step 5: Report Back

After all updates, confirm:
- Meeting record: updated/created at `records/meetings/YYYY-MM/filename.md`
- Contacts updated: list of existing dossier files updated
- New dossiers created: list of new contact files auto-created
- INDEX files updated: which ones

## Batch Mode

When processing multiple transcripts at once (e.g., after a batch pull):

1. Collect all external participants across all new transcripts, deduplicate
2. Update existing contact dossiers with new transcript links, timeline entries, and details
3. Auto-create dossiers for significant new contacts
4. Tag every new transcript with a Related Contacts section
5. Update `records/contacts/INDEX.md` with any new dossier entries
6. Update `records/transcripts/INDEX.md` with all new transcript entries
7. Update `records/meetings/INDEX.md` for all modified meeting records

Batch the INDEX updates — do them once at the end, not per-transcript.

## Edge Cases

### No matching meeting record
Create a new meeting record using transcript metadata. Leave `calendar_event_id` empty.

### Contact name ambiguity
If a transcript mentions "Alex" but there are multiple Alex contacts, check company domain and transcript context before linking. If still ambiguous, skip the link rather than guessing wrong.

### Transcript already has Related Contacts
Merge new contacts into the existing section. Don't duplicate entries.

### Fathom vs Fireflies metadata
- Fireflies transcripts have `fireflies_id` and `transcript_url`
- Fathom transcripts have `fathom_recording_id`, `fathom_url`, and `share_url`
- The skill handles both — check which fields exist and use accordingly
