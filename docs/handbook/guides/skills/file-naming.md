<metadata>
purpose: Enforce file naming and versioning conventions
source: https://handbook.growthx.ai/guides/skills/file-naming
sync_type: auto
access: build-team
last_synced: 2026-03-02
</metadata>

# File naming

A passive skill that enforces consistent file naming conventions across the workspace. Applies automatically whenever files are created or renamed — no trigger phrase needed.

## Trigger phrases

This skill activates automatically when creating or renaming any file. No explicit trigger needed.

## What it does

Enforces a simple naming convention: `descriptive-name-v1.md` — lowercase, hyphens between words, version suffix. Scratchpad files get a date prefix: `YYYY-MM-DD-descriptive-name-v1.md`.

Handles version management: minor updates edit in place (update `last_updated` in metadata), major changes create a new version (`-v2`) and move the old file to `/archive`.

Catches common mistakes: spaces in filenames, uppercase letters, underscores, missing version suffixes, abbreviations instead of descriptive names, and scratchpad files missing date prefixes.

## Install

<CodeGroup>

```bash Cursor
mkdir -p .cursor/skills/file-naming
curl -o .cursor/skills/file-naming/SKILL.md \
  https://raw.githubusercontent.com/marcelsantilli/growthx-ceo-os/main/.cursor/skills/file-naming/SKILL.md
```

```bash Claude Code
mkdir -p .agents/skills/file-naming
curl -o .agents/skills/file-naming/SKILL.md \
  https://raw.githubusercontent.com/marcelsantilli/growthx-ceo-os/main/.cursor/skills/file-naming/SKILL.md
```

</CodeGroup>

<Note>
Requires access to the [growthx-context](https://github.com/marcelsantilli/growthx-ceo-os) repository (private).
</Note>
