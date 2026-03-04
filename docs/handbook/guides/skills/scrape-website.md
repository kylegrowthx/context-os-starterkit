<metadata>
purpose: Scrape entire websites to markdown using Jina Reader API
source: https://handbook.growthx.ai/guides/skills/scrape-website
sync_type: auto
access: build-team
last_synced: 2026-03-02
</metadata>

# Scrape website

Scrapes all pages from a website and converts them to clean markdown files with YAML frontmatter. Discovers pages via XML sitemaps, respects robots.txt disallow rules, and organizes output files to mirror the URL path structure.

## Trigger phrases

- "Scrape website" or "scrape site"
- "Download website" or "crawl site"
- "Convert website to markdown" or "site to markdown"
- "Archive website" or "pull all pages from"

## What it does

Uses a Python script that automatically checks robots.txt, tries multiple sitemap locations (including WordPress-specific paths), recursively follows sitemap indexes, fetches each URL via Jina Reader API, and saves as markdown with source URL and scrape date in the frontmatter.

Resume-safe — skips already-downloaded files, so you can re-run after failures. Generates a README.md index of all scraped content and saves failed URLs to `.failed-urls.txt` for retry.

Rate limiting is built in (configurable delay between requests, automatic backoff on 429 responses). For large sites, expect ~6-8 seconds per page.

<Warning>
Requires a `JINA_API_KEY` in your `.env` file and the companion Python script from the growthx-context repo.
</Warning>

## Install

<CodeGroup>

```bash Cursor
mkdir -p .cursor/skills/scrape-website
curl -o .cursor/skills/scrape-website/SKILL.md \
  https://raw.githubusercontent.com/marcelsantilli/growthx-ceo-os/main/.cursor/skills/scrape-website/SKILL.md
```

```bash Claude Code
mkdir -p .agents/skills/scrape-website
curl -o .agents/skills/scrape-website/SKILL.md \
  https://raw.githubusercontent.com/marcelsantilli/growthx-ceo-os/main/.cursor/skills/scrape-website/SKILL.md
```

</CodeGroup>

<Note>
Requires access to the [growthx-context](https://github.com/marcelsantilli/growthx-ceo-os) repository (private). Also requires the companion `scrape-website.py` script from `.cursor/skills/scrape-website/scripts/`.
</Note>
