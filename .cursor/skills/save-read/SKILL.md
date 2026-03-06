---
name: save-read
description: Save an article, essay, or blog post to the good-reads collection. Scrapes the page via Jina, formats as markdown with metadata, names it properly, updates the good-reads README/INDEX, and adds the author/publication to sources/. Use when the user says "save read", "save this article", "good read", "save this post", "add to reading list", or shares a URL they want to keep.
---

# Save Read

Save an article to `knowledge/good-reads/` — scrape it, format it, catalog it.

## Paths

| What | Where |
|------|-------|
| Script | `.cursor/skills/save-read/scripts/save-read.py` |
| Output dir | `knowledge/good-reads/` |
| README | `knowledge/good-reads/README.md` |
| INDEX | `knowledge/good-reads/INDEX.md` |
| Sources | `sources/sources-index.md`, `sources/people-index.md` |
| API key | `JINA_API_KEY` in `.env` |

## Prerequisites

- `requests` Python package (standard)
- `JINA_API_KEY` in `.env`

## Environment Detection

This skill works in both **Cursor** and **Claude Code / Cowork**. Detect which environment you're in and set the context root accordingly.

### Cursor

```bash
# Cursor — project root is the workspace
CONTEXT="/Users/marcelsantilli_mac2/Dropbox/GrowthX AI/Projects/growthx-context"
```

### Claude Code / Cowork

```bash
# Claude Code — find the repo root (wherever CLAUDE.md lives)
CONTEXT="$(pwd)"
# Or if running from a subdirectory:
CONTEXT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
```

### Fallback: manual path via --output-dir

The script accepts `--output-dir` to override the output location. Use this if auto-detection fails:

```bash
python3 "$SCRIPT" "<url>" --output-dir "$CONTEXT/knowledge/good-reads"
```

## Workflow

### Step 1: Gather info from user

Required:
- **URL** — the article to save

Optional (ask if not obvious from context):
- **Tags** — topics this relates to (e.g., `creativity, craft, career`)
- **Why** — one sentence on why it resonated

Don't ask for title, author, or publication — the script auto-detects these from the page. You can override them if the auto-detection is wrong.

### Step 2: Run the scraper

Pick the right method based on your environment:

#### Method A: Python script (preferred — Cursor or Claude Code with network access)

```bash
SCRIPT="$CONTEXT/.cursor/skills/save-read/scripts/save-read.py"

python3 "$SCRIPT" "<url>" \
  --tags "tag1, tag2" \
  --why "Why this resonated" \
  --output-dir "$CONTEXT/knowledge/good-reads"
```

The script outputs JSON with all metadata:

```json
{
  "status": "ok",
  "file": "/path/to/knowledge/good-reads/2026-03-05-becoming-an-artist-v1.md",
  "filename": "2026-03-05-becoming-an-artist-v1.md",
  "title": "Becoming an Artist",
  "author": "Dan Hock",
  "publication": "danhock.co",
  "tags": ["creativity", "craft"],
  "why": "...",
  "saved": "2026-03-05",
  "url": "https://www.danhock.co/p/becoming-an-artist"
}
```

#### Method B: WebFetch fallback (Cowork / sandboxed environments)

If the Python script can't reach Jina (proxy restrictions, sandbox), use the WebFetch MCP tool instead:

1. **Fetch the article** using WebFetch with the URL. Prompt: "Return the full article content including title, author, and all body text. Preserve headings, quotes, and structure. Do not summarize."
2. **Build the file manually** following the File Format spec below — add `<metadata>` block, slugify the title for the filename, write to `knowledge/good-reads/`.
3. **Continue with Steps 3–7** as normal.

This produces the same output — just uses a different fetch method.

#### Method C: curl + Jina (Claude Code terminal with network access)

```bash
source "$CONTEXT/.env"
curl -s -H "Authorization: Bearer $JINA_API_KEY" \
     -H "Accept: text/markdown" \
     -H "X-Return-Format: markdown" \
     "https://r.jina.ai/<url>" > /tmp/article-raw.md
```

Then build the file manually with metadata and save to `knowledge/good-reads/`.

### Step 3: Review the scraped content

Open the generated file and verify:
1. Content scraped cleanly (no junk HTML, nav elements, etc.)
2. Title, author, publication are correct in metadata
3. Clean up any obvious scraping artifacts if needed

If auto-detected metadata is wrong, edit the `<metadata>` block at the top of the file.

### Step 4: Update INDEX.md

Add a row to the articles table in `knowledge/good-reads/INDEX.md`:

```markdown
| [filename](filename) | Author | Publication | tags | YYYY-MM-DD |
```

Update the total count at the bottom.

### Step 5: Update README.md

Update the stats section in `knowledge/good-reads/README.md`:
- Increment **Total articles** count
- Update **Last saved** date

### Step 6: Add author/publication to sources

Check if the author and publication already exist in `sources/`:

**For the author** — check `sources/people-index.md`:
- If already listed, no action needed
- If not listed and they're someone worth following (not a one-off), add them to the appropriate category with a note about what they write about

**For the publication** — check `sources/sources-index.md`:
- If already listed, no action needed
- If not listed and it's a publication worth following, add it to the appropriate category
- For personal blogs/substacks, only add if the author publishes regularly and the content is consistently good

**Don't auto-add everyone.** Sources is a curated list. Only add authors/publications that Marcel would actually want to follow. If unsure, mention the author/publication to Marcel and ask if they want it added.

### Step 7: Confirm to user

Report back:
- Article title and author
- File saved to (relative path)
- Tags applied
- Whether author/publication were added to sources (or why not)

## Naming Convention

Files follow the GrowthX naming standard with date prefix (like scratchpad files):

```
YYYY-MM-DD-slugified-title-v1.md
```

Examples:
- `2026-03-05-becoming-an-artist-v1.md`
- `2026-03-05-why-great-companies-lose-v1.md`
- `2026-03-10-the-age-of-average-v1.md`

## File Format

Each saved article looks like:

```markdown
<metadata>
source_url: https://example.com/article
title: Article Title
author: Author Name
publication: example.com
tags: tag1, tag2, tag3
why: One sentence on why this resonated
saved: 2026-03-05
access: personal
</metadata>

---

[Full article content in markdown]
```

## Edge Cases

- **Paywalled content**: Jina may only get the preview. Note this in the file if the content looks truncated.
- **PDF links**: Not supported — save these manually or use the pdf skill.
- **Twitter/X threads**: Jina handles these reasonably well. Tag with `twitter-thread`.
- **YouTube links**: Will only get the page metadata, not transcript. Note this.
- **Duplicate URLs**: Check INDEX.md before saving. If already saved, tell the user.
- **Sandbox/proxy blocked**: Fall back to Method B (WebFetch) or Method C (curl). Same output, different pipe.
