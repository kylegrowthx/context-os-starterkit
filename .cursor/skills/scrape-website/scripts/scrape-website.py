#!/usr/bin/env python3
"""
Scrape an entire website to markdown via Jina Reader API.

Usage:
    python3 scrape-website.py <domain> <output_dir> [options]

Examples:
    python3 scrape-website.py example.com ./projects/example-site
    python3 scrape-website.py example.com ./projects/example-site --delay 1.0
    python3 scrape-website.py example.com ./projects/example-site --skip-robots
    python3 scrape-website.py example.com ./projects/example-site --include-categories

Requires: requests (pip install requests)
JINA_API_KEY must be set in environment or in .env file.
"""

import argparse
import json
import os
import re
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from urllib.parse import urljoin, urlparse

try:
    import requests
except ImportError:
    print("ERROR: 'requests' package required. Run: pip install requests")
    sys.exit(1)


JINA_BASE = "https://r.jina.ai/"

SITEMAP_CANDIDATES = [
    "/sitemap_index.xml",
    "/sitemap.xml",
    "/wp-sitemap.xml",
    "/sitemap-index.xml",
    "/sitemaps.xml",
    "/post-sitemap.xml",
    "/page-sitemap.xml",
]


def load_env(start_dir=None):
    # type: (Optional[str]) -> None
    """Load JINA_API_KEY from .env file if not already set."""
    if os.environ.get("JINA_API_KEY"):
        return
    search_dirs = []
    if start_dir:
        search_dirs.append(start_dir)
    search_dirs.append(os.getcwd())
    home = os.path.expanduser("~")
    for d in search_dirs:
        p = Path(d)
        while str(p) >= home:
            env_file = p / ".env"
            if env_file.exists():
                for line in env_file.read_text().splitlines():
                    line = line.strip()
                    if line.startswith("JINA_API_KEY"):
                        match = re.match(r"JINA_API_KEY\s*=\s*['\"]?([^'\"#\s]+)", line)
                        if match:
                            os.environ["JINA_API_KEY"] = match.group(1)
                            return
            p = p.parent
            if p == p.parent:
                break


def fetch_url(url, timeout=15):
    # type: (str, int) -> Optional[str]
    """Fetch a URL and return text content, or None on failure."""
    try:
        resp = requests.get(url, timeout=timeout, headers={"User-Agent": "GrowthX-Scraper/1.0"})
        if resp.status_code == 200:
            return resp.text
        return None
    except requests.RequestException:
        return None


def parse_robots_txt(base_url):
    # type: (str) -> Set[str]
    """Parse robots.txt and return set of disallowed paths for * user-agent."""
    robots_url = urljoin(base_url, "/robots.txt")
    content = fetch_url(robots_url)
    if not content:
        return set()

    disallowed = set()
    in_wildcard_block = False

    for line in content.splitlines():
        line = line.strip()
        if line.startswith("#"):
            continue
        lower = line.lower()
        if lower.startswith("user-agent:"):
            agent = line.split(":", 1)[1].strip()
            in_wildcard_block = agent == "*"
        elif lower.startswith("disallow:") and in_wildcard_block:
            path = line.split(":", 1)[1].strip()
            if path:
                disallowed.add(path)

    return disallowed


def is_disallowed(url_path, disallowed_paths):
    # type: (str, Set[str]) -> bool
    """Check if a URL path is blocked by robots.txt disallow rules."""
    for rule in disallowed_paths:
        if rule.endswith("*"):
            if url_path.startswith(rule[:-1]):
                return True
        elif url_path.startswith(rule):
            return True
    return False


def find_sitemaps(base_url):
    # type: (str) -> List[str]
    """Try common sitemap locations and return list of sitemap URLs found."""
    found = []
    for candidate in SITEMAP_CANDIDATES:
        url = urljoin(base_url, candidate)
        content = fetch_url(url, timeout=10)
        if content and ("<?xml" in content[:200] or "<urlset" in content[:500] or "<sitemapindex" in content[:500]):
            found.append(url)
    return found


def extract_urls_from_sitemap(sitemap_url, base_url):
    # type: (str, str) -> Tuple[List[str], List[str]]
    """Parse a sitemap XML and return (page_urls, child_sitemap_urls)."""
    content = fetch_url(sitemap_url, timeout=15)
    if not content:
        return [], []

    content = re.sub(r'\sxmlns="[^"]+"', "", content, count=1)

    try:
        root = ET.fromstring(content)
    except ET.ParseError:
        return [], []

    page_urls = []
    child_sitemaps = []

    for elem in root.iter():
        tag = elem.tag.split("}")[-1] if "}" in elem.tag else elem.tag
        if tag == "sitemap":
            loc_elem = elem.find("loc") if elem.find("loc") is not None else elem.find("{*}loc")
            for child in elem:
                child_tag = child.tag.split("}")[-1] if "}" in child.tag else child.tag
                if child_tag == "loc" and child.text:
                    child_sitemaps.append(child.text.strip())
        elif tag == "url":
            for child in elem:
                child_tag = child.tag.split("}")[-1] if "}" in child.tag else child.tag
                if child_tag == "loc" and child.text:
                    url = child.text.strip()
                    parsed = urlparse(url)
                    parsed_base = urlparse(base_url)
                    if parsed.netloc == parsed_base.netloc or parsed.netloc == "www." + parsed_base.netloc:
                        page_urls.append(url)

    return page_urls, child_sitemaps


def discover_all_urls(base_url):
    # type: (str) -> List[str]
    """Discover all page URLs from sitemaps, recursively following sitemap indexes."""
    print("Discovering sitemaps...")
    sitemaps = find_sitemaps(base_url)
    if not sitemaps:
        print("  No sitemaps found. Falling back to homepage only.")
        return [base_url]

    print(f"  Found {len(sitemaps)} sitemap(s): {', '.join(sitemaps)}")

    all_urls = set()
    processed_sitemaps = set()
    queue = list(sitemaps)

    while queue:
        sitemap_url = queue.pop(0)
        if sitemap_url in processed_sitemaps:
            continue
        processed_sitemaps.add(sitemap_url)

        print(f"  Parsing {sitemap_url}...")
        page_urls, child_sitemaps = extract_urls_from_sitemap(sitemap_url, base_url)
        all_urls.update(page_urls)
        for child in child_sitemaps:
            if child not in processed_sitemaps:
                queue.append(child)

    urls = sorted(all_urls)
    print(f"  Discovered {len(urls)} URLs total")
    return urls


def url_to_filepath(url, output_dir):
    # type: (str, Path) -> Path
    """Convert a URL to a local .md file path mirroring the URL structure."""
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    if not path:
        return output_dir / "index.md"
    return output_dir / (path + ".md")


def fetch_with_jina(url, api_key, retries=2):
    # type: (str, str, int) -> Optional[str]
    """Fetch a URL via Jina Reader API and return markdown content."""
    headers = {
        "Authorization": "Bearer " + api_key,
        "Accept": "text/markdown",
        "X-Return-Format": "markdown",
    }
    for attempt in range(retries + 1):
        try:
            resp = requests.get(JINA_BASE + url, headers=headers, timeout=45)
            if resp.status_code == 200:
                return resp.text
            if resp.status_code == 429:
                wait = 5 * (attempt + 1)
                print("    Rate limited, waiting %ds..." % wait)
                sys.stdout.flush()
                time.sleep(wait)
                continue
            print("    HTTP %d" % resp.status_code)
            sys.stdout.flush()
            if resp.status_code >= 500 and attempt < retries:
                time.sleep(2)
                continue
            return None
        except requests.RequestException as e:
            if attempt < retries:
                time.sleep(2)
                continue
            print("    Error: %s" % e)
            sys.stdout.flush()
            return None
    return None


def generate_index(output_dir, scraped_files, domain):
    # type: (Path, Dict[str, Path], str) -> None
    """Generate a README.md index of all scraped content."""
    lines = [
        "# %s — Site Scrape" % domain,
        "",
        "Scraped: %s" % time.strftime("%Y-%m-%d"),
        "Total pages: %d" % len(scraped_files),
        "",
        "## Pages",
        "",
        "| File | Source URL |",
        "|------|-----------|",
    ]
    for url in sorted(scraped_files.keys()):
        filepath = scraped_files[url]
        rel = filepath.relative_to(output_dir)
        lines.append("| `%s` | %s |" % (rel, url))

    lines.append("")
    readme = output_dir / "README.md"
    readme.write_text("\n".join(lines), encoding="utf-8")
    print("\nGenerated %s" % readme)
    sys.stdout.flush()


def main():
    parser = argparse.ArgumentParser(description="Scrape a website to markdown via Jina Reader API")
    parser.add_argument("domain", help="Domain to scrape (e.g. example.com)")
    parser.add_argument("output_dir", help="Output directory for .md files")
    parser.add_argument("--delay", type=float, default=0.5, help="Delay between requests in seconds (default: 0.5)")
    parser.add_argument("--skip-robots", action="store_true", help="Skip robots.txt checking")
    parser.add_argument("--include-categories", action="store_true", help="Include WordPress /category/ pages")
    parser.add_argument("--resume", action="store_true", default=True, help="Skip already-downloaded files (default: true)")
    parser.add_argument("--no-resume", action="store_true", help="Re-download all files")
    parser.add_argument("--no-index", action="store_true", help="Skip generating README.md index")
    args = parser.parse_args()

    resume = not args.no_resume

    domain = args.domain.replace("https://", "").replace("http://", "").rstrip("/")
    base_url = "https://" + domain
    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    load_env(str(output_dir))
    api_key = os.environ.get("JINA_API_KEY")
    if not api_key:
        print("ERROR: JINA_API_KEY not found in environment or .env file")
        sys.exit(1)

    # robots.txt
    disallowed = set()
    if not args.skip_robots:
        print("Checking robots.txt...")
        disallowed = parse_robots_txt(base_url)
        if disallowed:
            print("  Disallowed paths: %s" % ", ".join(sorted(disallowed)))
        else:
            print("  No disallow rules found")
        sys.stdout.flush()

    # discover URLs
    urls = discover_all_urls(base_url)

    # filter
    filtered = []
    blocked_count = 0
    category_count = 0
    for url in urls:
        parsed = urlparse(url)
        if not args.skip_robots and is_disallowed(parsed.path, disallowed):
            blocked_count += 1
            continue
        if not args.include_categories and "/category/" in parsed.path:
            category_count += 1
            continue
        filtered.append(url)

    if blocked_count:
        print("Filtered %d URLs blocked by robots.txt" % blocked_count)
    if category_count:
        print("Filtered %d category index pages (use --include-categories to include)" % category_count)
    print("Scraping %d pages...\n" % len(filtered))
    sys.stdout.flush()

    # scrape
    success = 0
    skipped = 0
    failed = []
    scraped_files = {}

    for i, url in enumerate(filtered, 1):
        filepath = url_to_filepath(url, output_dir)
        filepath.parent.mkdir(parents=True, exist_ok=True)

        print("[%d/%d] %s" % (i, len(filtered), url))
        sys.stdout.flush()

        if resume and filepath.exists() and filepath.stat().st_size > 100:
            print("  Skipped (already exists)")
            sys.stdout.flush()
            scraped_files[url] = filepath
            skipped += 1
            success += 1
            continue

        content = fetch_with_jina(url, api_key)
        if content:
            source_header = "---\nsource_url: %s\nscraped_at: %s\n---\n\n" % (url, time.strftime("%Y-%m-%d"))
            filepath.write_text(source_header + content, encoding="utf-8")
            size_kb = filepath.stat().st_size / 1024
            print("  Saved -> %s (%.1f KB)" % (filepath.relative_to(output_dir), size_kb))
            scraped_files[url] = filepath
            success += 1
        else:
            failed.append(url)
            print("  FAILED")
        sys.stdout.flush()

        if i < len(filtered):
            time.sleep(args.delay)

    # summary
    print("\n" + "=" * 60)
    print("Done: %d/%d succeeded" % (success, len(filtered)))
    if skipped:
        print("  (%d skipped / already downloaded)" % skipped)
    if failed:
        print("  %d failed:" % len(failed))
        for u in failed:
            print("    - %s" % u)

        failed_file = output_dir / ".failed-urls.txt"
        failed_file.write_text("\n".join(failed) + "\n", encoding="utf-8")
        print("  Failed URLs saved to %s" % failed_file)

    # index
    if not args.no_index and scraped_files:
        generate_index(output_dir, scraped_files, domain)

    sys.stdout.flush()
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
