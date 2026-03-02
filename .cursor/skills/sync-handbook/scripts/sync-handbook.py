#!/usr/bin/env python3
"""
Syncs the GrowthX Handbook (Mintlify site) to growthx-context/docs/handbook/.
Also handles one-time migration of existing docs/ content.

Usage:
  # First-time migration + sync
  python sync-handbook.py --migrate --handbook-path /path/to/handbook --context-path /path/to/context [--dry-run]

  # Regular sync
  python sync-handbook.py --handbook-path /path/to/handbook --context-path /path/to/context [--dry-run] [--force] [--verbose]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
from datetime import date
from pathlib import Path
from typing import Optional

EXCLUDE_DIRS = {"context", "scratchpad", ".cursor", ".agents", ".skills", "node_modules", ".git"}
CONTEXT_ONLY_DIRS = {"finance", "business", "sales"}
SKIP_FILES = {"README.md", "INDEX.md"}
HANDBOOK_BASE_URL = "https://handbook.growthx.ai"
DEFAULT_ACCESS = "build-team"

# ---------------------------------------------------------------------------
# Frontmatter parsing
# ---------------------------------------------------------------------------

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(content: str) -> "tuple[dict, str]":
    """Return (frontmatter_dict, body) from an MDX file's content."""
    m = FRONTMATTER_RE.match(content)
    if not m:
        return {}, content
    raw = m.group(1)
    body = content[m.end():]
    fm = {}
    for line in raw.splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip().strip('"').strip("'")
    return fm, body


def build_metadata_block(fm: dict, rel_path: str) -> str:
    """Generate a <metadata> block from YAML frontmatter."""
    purpose = fm.get("description", fm.get("title", ""))
    url_path = rel_path.replace(".mdx", "").replace(".md", "")
    if url_path.endswith("/index"):
        url_path = url_path[: -len("/index")]
    source = f"{HANDBOOK_BASE_URL}/{url_path}"
    today = date.today().isoformat()
    lines = [
        "<metadata>",
        f"purpose: {purpose}",
        f"source: {source}",
        "sync_type: auto",
        f"access: {DEFAULT_ACCESS}",
        f"last_synced: {today}",
        "</metadata>",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# File helpers
# ---------------------------------------------------------------------------


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def strip_version_suffix(stem: str) -> str:
    """Remove trailing -v1, -v2 etc. from a filename stem."""
    return re.sub(r"-v\d+$", "", stem)


def collect_mdx_files(handbook_path: Path) -> list[Path]:
    """Collect all .mdx files from the handbook, excluding irrelevant dirs."""
    results = []
    for f in sorted(handbook_path.rglob("*.mdx")):
        rel = f.relative_to(handbook_path)
        parts = rel.parts
        if any(p in EXCLUDE_DIRS for p in parts):
            continue
        results.append(f)
    return results


def collect_image_files(handbook_path: Path) -> list[Path]:
    """Collect image files from the handbook."""
    exts = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico"}
    results = []
    for f in sorted(handbook_path.rglob("*")):
        if f.suffix.lower() in exts:
            rel = f.relative_to(handbook_path)
            if not any(p in EXCLUDE_DIRS for p in rel.parts):
                results.append(f)
    return results


# ---------------------------------------------------------------------------
# Migration
# ---------------------------------------------------------------------------


def build_handbook_stem_set(handbook_path: Path) -> dict[str, str]:
    """Build a mapping of (dir/normalized_stem) -> handbook relative path."""
    mdx_files = collect_mdx_files(handbook_path)
    stems = {}
    for f in mdx_files:
        rel = f.relative_to(handbook_path)
        rel_str = str(rel)
        parent = str(rel.parent) if str(rel.parent) != "." else ""
        stem = f.stem
        if parent:
            key = f"{parent}/{stem}"
        else:
            key = stem
        stems[key] = rel_str
    return stems


def find_handbook_match(
    context_rel: str,
    handbook_stems: dict[str, str],
) -> Optional[str]:
    """Check if a context doc file has a handbook equivalent."""
    p = Path(context_rel)
    stem = p.stem
    normalized = strip_version_suffix(stem)
    parent = str(p.parent) if str(p.parent) != "." else ""

    if parent:
        key = f"{parent}/{normalized}"
    else:
        key = normalized

    if key in handbook_stems:
        return handbook_stems[key]

    if parent:
        key_exact = f"{parent}/{stem}"
        if key_exact in handbook_stems:
            return handbook_stems[key_exact]

    return None


def run_migrate(context_path: Path, handbook_path: Path, dry_run: bool, verbose: bool):
    """One-time migration: split existing docs/ into private-docs/ and archive/."""
    docs_path = context_path / "docs"
    archive_path = docs_path / "archive"
    pre_sync_path = archive_path / "pre-handbook-sync"
    private_path = docs_path / "private-docs"

    if not docs_path.exists():
        print("ERROR: docs/ directory not found at", docs_path)
        sys.exit(1)

    handbook_stems = build_handbook_stem_set(handbook_path)
    if verbose:
        print(f"Found {len(handbook_stems)} handbook files")
        for k, v in sorted(handbook_stems.items()):
            print(f"  {k} -> {v}")

    existing_archive_files = []
    if archive_path.exists():
        for f in archive_path.rglob("*.md"):
            existing_archive_files.append(f.relative_to(archive_path))

    all_docs = sorted(docs_path.rglob("*.md"))

    to_archive = []
    to_private = []
    to_skip = []

    for f in all_docs:
        rel = f.relative_to(docs_path)
        rel_str = str(rel)

        if f.name in SKIP_FILES:
            to_skip.append(rel_str)
            continue

        if rel.parts[0] == "archive":
            to_skip.append(rel_str)
            continue

        parts = rel.parts
        top_dir = parts[0] if len(parts) > 1 else None

        if top_dir in CONTEXT_ONLY_DIRS:
            to_private.append(rel_str)
            continue

        match = find_handbook_match(rel_str, handbook_stems)
        if match:
            to_archive.append((rel_str, match))
        else:
            to_private.append(rel_str)

    print("\n=== Migration Plan ===\n")
    print(f"Files to ARCHIVE (handbook has equivalent): {len(to_archive)}")
    for ctx, hb in to_archive:
        print(f"  {ctx}  ->  archive/pre-handbook-sync/{ctx}  (handbook: {hb})")

    print(f"\nFiles to PRIVATE-DOCS (no handbook equivalent): {len(to_private)}")
    for p in to_private:
        print(f"  {p}  ->  private-docs/{p}")

    print(f"\nFiles to SKIP (README/INDEX/archive): {len(to_skip)}")
    for s in to_skip:
        print(f"  {s}")

    if dry_run:
        print("\n[DRY RUN] No files moved.")
        return

    print("\nExecuting migration...")

    for ctx_rel, _ in to_archive:
        src = docs_path / ctx_rel
        dst = pre_sync_path / ctx_rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(dst))
        if verbose:
            print(f"  ARCHIVE: {ctx_rel}")

    for ctx_rel in to_private:
        src = docs_path / ctx_rel
        dst = private_path / ctx_rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(dst))
        if verbose:
            print(f"  PRIVATE: {ctx_rel}")

    for ctx_rel in to_private + [a[0] for a in to_archive]:
        src_dir = docs_path / Path(ctx_rel).parent
        try:
            while src_dir != docs_path:
                if src_dir.exists() and not any(src_dir.iterdir()):
                    src_dir.rmdir()
                    if verbose:
                        print(f"  RMDIR: {src_dir.relative_to(docs_path)}")
                src_dir = src_dir.parent
        except (OSError, StopIteration):
            pass

    for old_readme in [
        docs_path / d / "README.md"
        for d in CONTEXT_ONLY_DIRS
        if (docs_path / d / "README.md").exists()
    ]:
        rel = old_readme.relative_to(docs_path)
        dst = private_path / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(old_readme), str(dst))

    for old_index in [
        docs_path / d / "INDEX.md"
        for d in CONTEXT_ONLY_DIRS
        if (docs_path / d / "INDEX.md").exists()
    ]:
        rel = old_index.relative_to(docs_path)
        dst = private_path / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(old_index), str(dst))

    for d in list(CONTEXT_ONLY_DIRS) + ["company", "how-we-work", "delivery", "epd", "people", "products"]:
        dir_path = docs_path / d
        if dir_path.exists():
            remaining_readmes = list(dir_path.rglob("README.md")) + list(dir_path.rglob("INDEX.md"))
            for rm_file in remaining_readmes:
                rm_rel = rm_file.relative_to(docs_path)
                dst = pre_sync_path / rm_rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(rm_file), str(dst))
            try:
                shutil.rmtree(str(dir_path))
            except OSError:
                pass

    if (docs_path / "start-here.md").exists():
        pass

    print(f"\nMigration complete. {len(to_archive)} archived, {len(to_private)} moved to private-docs.")


# ---------------------------------------------------------------------------
# Sync
# ---------------------------------------------------------------------------


def run_sync(
    handbook_path: Path,
    context_path: Path,
    dry_run: bool,
    force: bool,
    verbose: bool,
):
    """Sync handbook .mdx files to docs/handbook/ as .md."""
    output_path = context_path / "docs" / "handbook"
    manifest_path = output_path / ".sync-manifest.json"

    manifest = {}
    if manifest_path.exists() and not force:
        manifest = json.loads(manifest_path.read_text())

    mdx_files = collect_mdx_files(handbook_path)
    image_files = collect_image_files(handbook_path)

    new_manifest = {}
    stats = {"new": 0, "updated": 0, "unchanged": 0, "deleted": 0, "images": 0}
    changes = []

    for mdx in mdx_files:
        rel = mdx.relative_to(handbook_path)
        rel_str = str(rel)
        target_name = rel.with_suffix(".md")
        target_path = output_path / target_name

        src_hash = file_hash(mdx)
        prev = manifest.get(rel_str, {})

        if not force and prev.get("source_hash") == src_hash and target_path.exists():
            new_manifest[rel_str] = prev
            stats["unchanged"] += 1
            continue

        content = mdx.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(content)
        metadata = build_metadata_block(fm, rel_str)
        title = fm.get("title", rel.stem.replace("-", " ").title())
        output_content = f"{metadata}\n\n# {title}\n\n{body}"

        if target_path.exists():
            action = "updated"
            stats["updated"] += 1
        else:
            action = "new"
            stats["new"] += 1

        changes.append((action, str(target_name)))

        if not dry_run:
            target_path.parent.mkdir(parents=True, exist_ok=True)
            target_path.write_text(output_content, encoding="utf-8")

        new_manifest[rel_str] = {
            "target": str(target_name),
            "source_hash": src_hash,
            "last_synced": date.today().isoformat(),
        }

    existing_targets = set()
    if output_path.exists():
        for f in output_path.rglob("*.md"):
            if f.name not in SKIP_FILES and f.name != ".sync-manifest.json":
                existing_targets.add(str(f.relative_to(output_path)))

    expected_targets = {v["target"] for v in new_manifest.values()}
    for et in existing_targets - expected_targets:
        stats["deleted"] += 1
        changes.append(("deleted", et))
        if not dry_run:
            (output_path / et).unlink(missing_ok=True)

    for img in image_files:
        rel = img.relative_to(handbook_path)
        target = output_path / rel
        if not dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(str(img), str(target))
        stats["images"] += 1

    print("\n=== Sync Summary ===\n")
    print(f"New:       {stats['new']}")
    print(f"Updated:   {stats['updated']}")
    print(f"Unchanged: {stats['unchanged']}")
    print(f"Deleted:   {stats['deleted']}")
    print(f"Images:    {stats['images']}")

    if changes:
        print("\nChanges:")
        for action, path in changes:
            print(f"  [{action.upper()}] {path}")

    if dry_run:
        print("\n[DRY RUN] No files written.")
        return new_manifest

    if not dry_run:
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(json.dumps(new_manifest, indent=2), encoding="utf-8")

    generate_readme_index(output_path, handbook_path)

    print(f"\nSync complete. {stats['new']} new, {stats['updated']} updated, {stats['deleted']} deleted.")
    return new_manifest


# ---------------------------------------------------------------------------
# README / INDEX generation
# ---------------------------------------------------------------------------


def get_file_description(file_path: Path) -> str:
    """Extract a short description from a synced .md file's metadata block."""
    try:
        content = file_path.read_text(encoding="utf-8")
        m = re.search(r"purpose:\s*(.+)", content)
        if m:
            return m.group(1).strip()
        m = re.search(r"^# (.+)", content, re.MULTILINE)
        if m:
            return m.group(1).strip()
    except Exception:
        pass
    return file_path.stem.replace("-", " ").title()


def generate_readme_index(output_path: Path, handbook_path: Optional[Path] = None):
    """Generate README.md and INDEX.md for docs/handbook/ and each subdirectory."""
    if not output_path.exists():
        return

    dirs_to_process = [output_path]
    for d in sorted(output_path.rglob("*")):
        if d.is_dir() and d.name not in {".git", "__pycache__"}:
            dirs_to_process.append(d)

    for dir_path in dirs_to_process:
        md_files = sorted(
            f for f in dir_path.iterdir()
            if f.is_file() and f.suffix == ".md" and f.name not in SKIP_FILES
        )
        subdirs = sorted(d for d in dir_path.iterdir() if d.is_dir())
        rel_from_output = dir_path.relative_to(output_path)
        dir_label = str(rel_from_output) if str(rel_from_output) != "." else "handbook"

        readme_lines = [
            f"# {dir_label.replace('/', ' / ').title()}",
            "",
            f"Auto-synced from the [GrowthX Handbook]({HANDBOOK_BASE_URL}). Do not edit manually.",
            "",
            "---",
            "",
        ]

        if md_files:
            readme_lines.append("## Documents")
            readme_lines.append("")
            readme_lines.append("| Document | Description |")
            readme_lines.append("|----------|-------------|")
            for f in md_files:
                desc = get_file_description(f)
                readme_lines.append(f"| `{f.name}` | {desc} |")
            readme_lines.append("")

        if subdirs:
            readme_lines.append("## Subdirectories")
            readme_lines.append("")
            readme_lines.append("| Directory | Contents |")
            readme_lines.append("|-----------|----------|")
            for d in subdirs:
                count = len(list(d.rglob("*.md")))
                readme_lines.append(f"| [{d.name}/]({d.name}/) | {count} files |")
            readme_lines.append("")

        readme_lines.extend([
            "---",
            "",
            "## Maintenance",
            "",
            "This directory is auto-synced by `sync-handbook.py`. Edits here will be overwritten on next sync.",
            f"To update, edit the source at the [GrowthX Handbook]({HANDBOOK_BASE_URL}) and re-run the sync.",
            "",
            f"**Last synced:** {date.today().strftime('%B %Y')}",
            "",
        ])

        index_lines = [
            f"# Index: docs/handbook/{rel_from_output}" if str(rel_from_output) != "." else "# Index: docs/handbook/",
            "",
            f"> Complete file listing for `docs/handbook/{rel_from_output}`" if str(rel_from_output) != "." else "> Complete file listing for `docs/handbook/`",
            "",
            "See [README.md](README.md) for an overview.",
            "",
        ]

        if md_files:
            index_lines.append("## Files")
            index_lines.append("")
            index_lines.append("| File | Description |")
            index_lines.append("|------|-------------|")
            for f in md_files:
                desc = get_file_description(f)
                index_lines.append(f"| [{f.name}]({f.name}) | {desc} |")
            index_lines.append("")

        if subdirs:
            index_lines.append("## Subdirectories")
            index_lines.append("")
            index_lines.append("| Directory | Files |")
            index_lines.append("|-----------|-------|")
            for d in subdirs:
                count = len(list(d.rglob("*.md")))
                index_lines.append(f"| [{d.name}/]({d.name}/) | {count} |")
            index_lines.append("")

        readme_path = dir_path / "README.md"
        index_path = dir_path / "INDEX.md"

        readme_path.write_text("\n".join(readme_lines), encoding="utf-8")
        index_path.write_text("\n".join(index_lines), encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description="Sync GrowthX Handbook to context docs")
    parser.add_argument("--handbook-path", required=True, help="Path to growthx-handbook repo")
    parser.add_argument("--context-path", required=True, help="Path to growthx-context repo")
    parser.add_argument("--migrate", action="store_true", help="Run one-time migration before sync")
    parser.add_argument("--dry-run", action="store_true", help="Show what would change without writing")
    parser.add_argument("--force", action="store_true", help="Force full rebuild regardless of hashes")
    parser.add_argument("--verbose", action="store_true", help="Detailed logging")

    args = parser.parse_args()

    handbook_path = Path(args.handbook_path).resolve()
    context_path = Path(args.context_path).resolve()

    if not handbook_path.exists():
        print(f"ERROR: Handbook path not found: {handbook_path}")
        sys.exit(1)
    if not context_path.exists():
        print(f"ERROR: Context path not found: {context_path}")
        sys.exit(1)

    if args.migrate:
        print("=" * 60)
        print("PHASE 1: Migration")
        print("=" * 60)
        run_migrate(context_path, handbook_path, args.dry_run, args.verbose)
        print()

    print("=" * 60)
    print("PHASE 2: Sync")
    print("=" * 60)
    run_sync(handbook_path, context_path, args.dry_run, args.force, args.verbose)


if __name__ == "__main__":
    main()
