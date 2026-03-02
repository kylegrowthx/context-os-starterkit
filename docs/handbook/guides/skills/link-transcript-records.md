<metadata>
purpose: Sync meeting records, contacts, and indexes after transcript enrichment
source: https://handbook.growthx.ai/guides/skills/link-transcript-records
sync_type: auto
access: build-team
last_synced: 2026-03-02
</metadata>

# Link transcript records

The final step in the transcript pipeline. After a transcript is enriched, this skill updates the matching meeting record, creates or updates contact dossiers for external participants, and keeps all INDEX files in sync.

## Trigger phrases

- "Link transcript" or "update meeting record"
- "Sync transcript contacts"
- "Link contacts to transcript" or "post-process transcript"

## What it does

Works on any enriched transcript regardless of source (Fireflies or Fathom). Five-step workflow:

1. **Read transcript** — extract metadata, participants, title, summary, source
2. **Update meeting record** — find or create the matching record in `records/meetings/`, add transcript link, enrich attendee table with roles and contact dossier links
3. **Update contact dossiers** — identify external participants, match against existing dossiers, add transcript references and timeline entries, auto-create dossiers for significant new contacts with `confidence: low`
4. **Tag transcript** — add a Related Contacts section linking to dossier files
5. **Update INDEX files** — keep transcripts, contacts, and meetings indexes current

Supports batch mode for processing multiple transcripts at once — deduplicates contacts across all transcripts and batches INDEX updates.

## Install

<CodeGroup>

```bash Cursor
mkdir -p .cursor/skills/link-transcript-records
curl -o .cursor/skills/link-transcript-records/SKILL.md \
  https://raw.githubusercontent.com/marcelsantilli/growthx-ceo-os/main/.cursor/skills/link-transcript-records/SKILL.md
```

```bash Claude Code
mkdir -p .agents/skills/link-transcript-records
curl -o .agents/skills/link-transcript-records/SKILL.md \
  https://raw.githubusercontent.com/marcelsantilli/growthx-ceo-os/main/.cursor/skills/link-transcript-records/SKILL.md
```

</CodeGroup>

<Note>
Requires access to the [growthx-context](https://github.com/marcelsantilli/growthx-ceo-os) repository (private).
</Note>
