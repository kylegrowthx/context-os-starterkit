---
name: scrape-website
description: Scrape an entire website to markdown files using Jina Reader API. Discovers all pages via XML sitemaps, respects robots.txt disallow rules, converts each page to clean markdown, and saves with YAML frontmatter. Use when the user wants to scrape a website, download site content, archive a client's website, convert a site to markdown, mirror web pages, or audit website content. Triggers on "scrape website", "scrape site", "download website", "crawl site", "convert website to markdown", "site to markdown", "archive website", "pull all pages from", "mirror site".
---

# Scrape Website

Scrape all pages from a website to local .md files using XML sitemaps + Jina Reader API.

## Paths

| What | Where |
|------|-------|
| Script | `.cursor/skills/scrape-website/scripts/scrape-website.py` |
| Output convention | `projects/<domain-slug>/` |
| API key | `JINA_API_KEY` in `.env` |

## Prerequisites

- `requests` Python package (standard — already installed)
- `JINA_API_KEY` in `.env` (script auto-discovers from `.env` up the directory tree)

## Script Reference

```bash
python3 .cursor/skills/scrape-website/scripts/scrape-website.py <domain> <output_dir> [options]
```

| Flag | Default | Purpose |
|------|---------|---------|
| `--delay` | 0.5 | Seconds between requests |
| `--skip-robots` | false | Ignore robots.txt |
| `--include-categories` | false | Include WordPress `/category/` pages |
| `--no-resume` | false | Re-download existing files |
| `--no-index` | false | Skip README.md generation |

The script automatically:
1. Checks `robots.txt` and filters disallowed paths
2. Tries multiple sitemap locations (`sitemap_index.xml`, `sitemap.xml`, `wp-sitemap.xml`, etc.)
3. Recursively follows sitemap indexes to discover all child sitemaps
4. Fetches each URL via Jina Reader API (`https://r.jina.ai/<url>`)
5. Saves as `.md` with YAML frontmatter (`source_url`, `scraped_at`)
6. Skips already-downloaded files (resume-safe)
7. Generates `README.md` index of all scraped content
8. Saves failed URLs to `.failed-urls.txt` for retry

## Workflow

### Step 1: Determine output path

Convention: `projects/<domain-slug>/` where domain-slug strips `www.` and replaces dots with hyphens if needed. Keep it simple — usually just the domain name.

Examples:
- `acespremortho.com` → `projects/acespremortho/`
- `www.relay.app` → `projects/relay/`
- `docs.example.com` → `projects/docs-example/`

### Step 2: Run the scrape

```bash
CONTEXT="/Users/marcelsantilli_mac2/Dropbox/GrowthX AI/Projects/growthx-context"
SCRIPT="$CONTEXT/.cursor/skills/scrape-website/scripts/scrape-website.py"

python3 "$SCRIPT" <domain> "$CONTEXT/projects/<slug>"
```

Set `block_until_ms` high enough — estimate 6-8 seconds per page. For a 100-page site, set to 900000 (15 min).

### Step 3: Handle failures

If any URLs failed, they're saved in `.failed-urls.txt`. Retry them:

```bash
# Re-run the same command — it skips already-downloaded files and retries failures
python3 "$SCRIPT" <domain> "$CONTEXT/projects/<slug>"
```

For persistent failures, fetch individual pages with curl + Jina:

```bash
curl -s -H "Authorization: Bearer $JINA_API_KEY" \
     -H "Accept: text/markdown" \
     -H "X-Return-Format: markdown" \
     "https://r.jina.ai/<full-url>" > output.md
```

### Step 4: Report results

After scraping completes, report to the user:
- Total pages found vs successfully scraped
- Output directory path
- Any failures
- Breakdown by content type if obvious (blog posts, pages, etc.)

## Output Structure

Files mirror the URL path structure:

```
projects/<slug>/
├── README.md                    # Auto-generated index
├── index.md                     # Homepage (/)
├── about.md                     # /about/
├── blog/
│   ├── first-post.md            # /blog/first-post/
│   └── second-post.md           # /blog/second-post/
├── services/
│   └── consulting.md            # /services/consulting/
└── .failed-urls.txt             # Any failures (if applicable)
```

Each `.md` file has YAML frontmatter:

```yaml
---
source_url: https://example.com/about/
scraped_at: 2026-02-27
---
```

## Rate Limits and Performance

- Default 0.5s delay between requests (configurable with `--delay`)
- Jina handles rate limiting with 429 responses — script auto-retries with backoff
- Server errors (5xx) get 2 automatic retries
- For large sites (500+ pages), consider `--delay 1.0` to be conservative
- ~6-8 seconds per page including fetch time + delay

## Edge Cases

- **No sitemap found**: Script falls back to homepage URL only. Manually provide URLs or find links on the homepage.
- **Sitemap returns HTML (redirect)**: Common with misconfigured WordPress. The script tries multiple sitemap paths to work around this.
- **WordPress category pages**: Filtered by default (low-value index pages). Use `--include-categories` if needed.
- **Sites with both www and non-www**: Script normalizes and deduplicates.
