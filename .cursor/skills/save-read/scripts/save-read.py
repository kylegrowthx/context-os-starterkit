#!/usr/bin/env python3
"""
save-read.py — Scrape a single article via Jina Reader API and save as markdown
with metadata, following GrowthX naming conventions.

Usage:
    python3 save-read.py <url> [--title "Custom Title"] [--author "Author Name"]
                                [--publication "Publication"] [--tags "tag1,tag2"]
                                [--why "Why this resonated"]
                                [--output-dir /path/to/good-reads]

Output: A properly named .md file in knowledge/good-reads/ with full metadata.
Prints JSON to stdout with file details for the calling skill to use.
"""

import argparse
import json
import os
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

import requests


def find_env_file():
    """Find JINA_API_KEY from .env — checks script dir upward, then cwd upward, then env var."""
    # Search from script location (works in Cursor where script is in .cursor/skills/)
    for start in [Path(__file__).resolve().parent, Path.cwd()]:
        current = start
        for _ in range(10):
            env_path = current / ".env"
            if env_path.exists():
                with open(env_path) as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith("JINA_API_KEY"):
                            key = line.split("=", 1)[1].strip().strip("'\"")
                            return key
            current = current.parent
    return os.environ.get("JINA_API_KEY")


def slugify(text):
    """Convert text to lowercase-hyphenated slug."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    text = text.strip('-')
    return text


def extract_metadata_from_jina(markdown_text, url):
    """Try to extract title, author, publication from Jina markdown output."""
    metadata = {"title": None, "author": None, "publication": None}

    # Jina often returns title as first H1
    title_match = re.search(r'^#\s+(.+)$', markdown_text, re.MULTILINE)
    if title_match:
        metadata["title"] = title_match.group(1).strip()

    # Try to find author patterns
    author_patterns = [
        r'(?:by|author|written by)[:\s]+([A-Z][a-z]+ [A-Z][a-z]+)',
        r'\*\*([A-Z][a-z]+ [A-Z][a-z]+)\*\*',  # Bold name near top
    ]
    for pattern in author_patterns:
        match = re.search(pattern, markdown_text[:2000], re.IGNORECASE)
        if match:
            metadata["author"] = match.group(1).strip()
            break

    # Derive publication from domain
    parsed = urlparse(url)
    domain = parsed.netloc.replace("www.", "")
    metadata["publication"] = domain

    return metadata


def scrape_article(url, api_key):
    """Fetch article content via Jina Reader API."""
    jina_url = f"https://r.jina.ai/{url}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "text/markdown",
        "X-Return-Format": "markdown",
    }

    resp = requests.get(jina_url, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.text


def build_article_file(content, url, title, author, publication, tags, why, saved_date):
    """Build the final markdown file with metadata header."""
    tag_str = ", ".join(tags) if tags else ""

    header = f"""<metadata>
source_url: {url}
title: {title}
author: {author}
publication: {publication}
tags: {tag_str}
why: {why}
saved: {saved_date}
access: personal
</metadata>

---

"""
    return header + content


def generate_filename(title, saved_date):
    """Generate filename: YYYY-MM-DD-slugified-title-v1.md"""
    slug = slugify(title)
    # Truncate slug to reasonable length
    if len(slug) > 60:
        slug = slug[:60].rstrip('-')
    return f"{saved_date}-{slug}-v1.md"


def main():
    parser = argparse.ArgumentParser(description="Save an article to good-reads")
    parser.add_argument("url", help="URL of the article to save")
    parser.add_argument("--title", help="Article title (auto-detected if omitted)")
    parser.add_argument("--author", help="Author name (auto-detected if omitted)")
    parser.add_argument("--publication", help="Publication name (auto-detected from domain)")
    parser.add_argument("--tags", help="Comma-separated tags", default="")
    parser.add_argument("--why", help="Why this resonated", default="")
    parser.add_argument("--output-dir", help="Output directory",
                        default=None)
    args = parser.parse_args()

    # Find API key
    api_key = find_env_file()
    if not api_key:
        print(json.dumps({"error": "JINA_API_KEY not found in .env or environment"}))
        sys.exit(1)

    # Resolve output dir — works from Cursor, Claude Code, or explicit path
    if args.output_dir:
        output_dir = Path(args.output_dir)
    else:
        # Strategy 1: Walk up from script location (.cursor/skills/save-read/scripts/ -> repo root)
        script_dir = Path(__file__).resolve().parent
        repo_root_from_script = script_dir.parent.parent.parent
        candidate = repo_root_from_script / "knowledge" / "good-reads"

        if candidate.exists() or (repo_root_from_script / "CLAUDE.md").exists():
            output_dir = candidate
        else:
            # Strategy 2: Check cwd for CLAUDE.md (Claude Code typically runs from repo root)
            cwd = Path.cwd()
            if (cwd / "CLAUDE.md").exists():
                output_dir = cwd / "knowledge" / "good-reads"
            else:
                # Strategy 3: Walk up from cwd to find CLAUDE.md
                search = cwd
                found = False
                for _ in range(10):
                    if (search / "CLAUDE.md").exists():
                        output_dir = search / "knowledge" / "good-reads"
                        found = True
                        break
                    search = search.parent
                if not found:
                    # Last resort: use script-relative path
                    output_dir = candidate

    output_dir.mkdir(parents=True, exist_ok=True)

    # Scrape
    print(f"Scraping: {args.url}", file=sys.stderr)
    try:
        content = scrape_article(args.url, api_key)
    except Exception as e:
        print(json.dumps({"error": f"Failed to scrape: {str(e)}"}))
        sys.exit(1)

    # Extract metadata from content
    detected = extract_metadata_from_jina(content, args.url)

    title = args.title or detected["title"] or "Untitled"
    author = args.author or detected["author"] or "Unknown"
    publication = args.publication or detected["publication"] or "Unknown"
    tags = [t.strip() for t in args.tags.split(",") if t.strip()] if args.tags else []
    why = args.why or ""
    saved_date = date.today().isoformat()

    # Build file
    article_md = build_article_file(content, args.url, title, author, publication, tags, why, saved_date)

    # Generate filename
    filename = generate_filename(title, saved_date)
    filepath = output_dir / filename

    # Write
    with open(filepath, "w") as f:
        f.write(article_md)

    # Output JSON for the skill to consume
    result = {
        "status": "ok",
        "file": str(filepath),
        "filename": filename,
        "title": title,
        "author": author,
        "publication": publication,
        "tags": tags,
        "why": why,
        "saved": saved_date,
        "url": args.url,
        "content_length": len(content),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
