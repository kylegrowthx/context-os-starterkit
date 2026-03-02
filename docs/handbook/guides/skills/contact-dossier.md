<metadata>
purpose: Create and update structured contact profiles from meetings and CRM data
source: https://handbook.growthx.ai/guides/skills/contact-dossier
sync_type: auto
access: build-team
last_synced: 2026-03-02
</metadata>

# Contact dossier

Creates or updates contact dossiers in `/records/contacts/` with all known personal and professional context. Gathers information from transcripts, HubSpot, and user input to build comprehensive profiles that make every future conversation more informed.

## Trigger phrases

- "Create a contact" or "update contact"
- "Save contact" or "add to contacts"
- "Build a profile on [person]"

## What it does

Searches for existing contact files, then gathers context from all available sources: HubSpot (contacts, companies, deals, meetings), transcripts (personal details, professional context, key quotes, relationship history), and user-provided notes.

Produces a structured dossier with sections for personal details (location, family, interests), career background, how they think (decision-making style, priorities), key quotes from meetings, relationship to GrowthX, their team, a chronological timeline, and linked meeting transcripts.

Auto-triggers after processing transcripts that mention significant new contacts. Cross-links the contact file to related transcripts (and vice versa) and updates INDEX files.

## Install

<CodeGroup>

```bash Cursor
mkdir -p .cursor/skills/contact-dossier
curl -o .cursor/skills/contact-dossier/SKILL.md \
  https://raw.githubusercontent.com/marcelsantilli/growthx-ceo-os/main/.cursor/skills/contact-dossier/SKILL.md
```

```bash Claude Code
mkdir -p .agents/skills/contact-dossier
curl -o .agents/skills/contact-dossier/SKILL.md \
  https://raw.githubusercontent.com/marcelsantilli/growthx-ceo-os/main/.cursor/skills/contact-dossier/SKILL.md
```

</CodeGroup>

<Note>
Requires access to the [growthx-context](https://github.com/marcelsantilli/growthx-ceo-os) repository (private).
</Note>
