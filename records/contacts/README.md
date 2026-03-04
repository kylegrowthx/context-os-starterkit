# Contacts

Personal CRM. People Marcel has met, works with, or wants to stay in touch with.

---

## How to Use

1. **One file per person.** Named `firstname-lastname-v1.md`.
2. **Search first.** Use grep/search to find contacts by name, company, or tag.
3. **Load individually.** Read specific contact files — never bulk-load.
4. **Keep notes current.** Update after meetings, intros, or meaningful interactions.

## Subdirectories

| Directory | What's There |
|-----------|-------------|
| [employees/](employees/) | GrowthX team directory — sourced from Slack, one file per employee |

## Creating & Updating Contacts

Use the **Contact Dossier** skill (`.cursor/skills/contact-dossier/SKILL.md`) to create or update a contact file. The skill gathers context from HubSpot, transcripts, and user-provided notes.

Contacts and transcripts are **cross-linked**:
- Contact files link to their meeting transcripts in `## Meeting Transcripts`
- Transcript files link back to contacts in `## Related Contacts`

This happens automatically when transcripts are processed (see the contact–transcript linking rule in `.cursor/rules/contact-transcript-linking.mdc`).

## Contact File Structure

Each contact file includes:

- **Metadata** — name, company, role, HubSpot IDs, tags, last_updated
- **Personal** — location, family, interests, shared connections with Marcel
- **Career Background** — relevant work history and professional network
- **How They Think** — decision-making style, priorities, values
- **Key Quotes** — direct quotes from meeting transcripts
- **Relationship to GrowthX** — how the connection started, deal status, personal relationship
- **Their Team** — if they manage people we interact with
- **Timeline** — chronological record of every interaction
- **Meeting Transcripts** — links to source transcripts in `records/transcripts/`

---

See [INDEX.md](INDEX.md) for a complete listing.
