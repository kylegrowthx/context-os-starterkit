#!/usr/bin/env python3
"""
Convert Fathom backup JSON dumps into formatted .md transcript files
matching the records/transcripts/ format.

Usage:
    python3 convert-to-transcript.py 2025-06/2025-06-30-ed-jason-weekly
    python3 convert-to-transcript.py --month 2025-06
    python3 convert-to-transcript.py --all
    python3 convert-to-transcript.py --all --dry-run
    python3 convert-to-transcript.py --all --force
"""

import argparse
import json
import math
import re
import sys
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
BACKUP_ROOT = SCRIPT_DIR
TRANSCRIPTS_ROOT = SCRIPT_DIR.parent.parent / "records" / "transcripts"

MONTH_DIR_PATTERN = re.compile(r"^\d{4}-\d{2}$")
MEETING_DIR_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}-.+$")


def load_json(path):
    if not path.exists():
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return None


def load_meeting(folder_path):
    """Read all JSON files from a meeting folder into a dict."""
    folder = Path(folder_path)
    if not folder.is_dir():
        return None

    meeting = {
        "folder": folder,
        "slug": folder.name,
        "metadata": load_json(folder / "metadata.json"),
        "summary": load_json(folder / "summary.json"),
        "participants": load_json(folder / "participants.json"),
        "action_items": load_json(folder / "action-items.json"),
    }

    transcript = load_json(folder / "transcript.json")
    if transcript is None:
        raw = load_json(folder / "transcript-raw.json")
        if raw and isinstance(raw, dict):
            transcript = raw.get("transcript")
    meeting["transcript"] = transcript

    return meeting


def strip_fathom_links(text):
    """Strip [text](fathom_url) markdown links, keeping just the text."""
    return re.sub(r"\[([^\]]+)\]\(https?://fathom\.video/[^)]*\)", r"\1", text)


def normalize_indent(text):
    """Strip common leading whitespace from non-empty lines, preserving relative nesting."""
    lines = text.split("\n")
    non_empty = [l for l in lines if l.strip()]
    if not non_empty:
        return text
    min_indent = min(len(l) - len(l.lstrip()) for l in non_empty)
    if min_indent == 0:
        return text
    return "\n".join(l[min_indent:] if len(l) > min_indent else l for l in lines)


def parse_summary_sections(markdown_str):
    """Split Fathom's markdown summary into named sections."""
    if not markdown_str:
        return {}

    clean = strip_fathom_links(markdown_str)
    sections = {}
    current_key = None
    current_lines = []

    for line in clean.split("\n"):
        h2_match = re.match(r"^##\s+(.+)$", line)
        if h2_match:
            if current_key:
                content = "\n".join(current_lines)
                sections[current_key] = normalize_indent(content).strip()
            current_key = h2_match.group(1).strip()
            current_lines = []
        else:
            current_lines.append(line)

    if current_key:
        content = "\n".join(current_lines)
        sections[current_key] = normalize_indent(content).strip()

    return sections


def parse_datetime(iso_str):
    if not iso_str:
        return None
    try:
        return datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
    except ValueError:
        return None


def compute_duration(meta):
    """Calculate meeting duration in minutes from recording or scheduled times."""
    start = parse_datetime(meta.get("recording_start_time"))
    end = parse_datetime(meta.get("recording_end_time"))

    if not start or not end:
        start = parse_datetime(meta.get("scheduled_start_time"))
        end = parse_datetime(meta.get("scheduled_end_time"))

    if start and end:
        delta = (end - start).total_seconds()
        return max(1, math.ceil(delta / 60))
    return None


def resolve_participant_names(participants, transcript):
    """Build a deduplicated participant name list from calendar invitees and transcript speakers."""
    names = []
    seen = set()

    if participants:
        for p in participants:
            name = p.get("name", "")
            email = p.get("email", "")
            display = p.get("matched_speaker_display_name")

            if display:
                key = display.lower()
                if key not in seen:
                    names.append(display)
                    seen.add(key)
            elif name and name != email:
                key = name.lower()
                if key not in seen:
                    names.append(name)
                    seen.add(key)
            elif email:
                local = email.split("@")[0]
                friendly = local.replace(".", " ").replace("-", " ").title()
                key = friendly.lower()
                if key not in seen:
                    names.append(friendly)
                    seen.add(key)

    if transcript and isinstance(transcript, list):
        for entry in transcript:
            speaker = entry.get("speaker", {})
            name = speaker.get("display_name", "")
            if name and name.lower() not in seen:
                names.append(name)
                seen.add(name.lower())

    return names


def format_metadata(meeting):
    meta = meeting.get("metadata") or {}
    participants = meeting.get("participants") or []
    transcript = meeting.get("transcript")

    date_str = ""
    rec_start = parse_datetime(meta.get("recording_start_time"))
    sched_start = parse_datetime(meta.get("scheduled_start_time"))
    dt = rec_start or sched_start
    if dt:
        date_str = dt.strftime("%Y-%m-%d")

    time_str = ""
    if rec_start:
        time_str = rec_start.strftime("%H:%M") + " UTC"
    elif sched_start:
        time_str = sched_start.strftime("%H:%M") + " UTC"

    duration = compute_duration(meta)
    duration_str = f"{duration} minutes" if duration else "unknown"

    organizer = ""
    recorded_by = meta.get("recorded_by") or {}
    if recorded_by.get("email"):
        organizer = recorded_by["email"]

    names = resolve_participant_names(participants, transcript)
    participants_str = ", ".join(names) if names else "unknown"

    recording_id = meta.get("recording_id", "")
    fathom_url = meta.get("url", "")
    share_url = meta.get("share_url", "")

    lines = [
        "<metadata>",
        f"date: {date_str}",
        f"time: {time_str}",
        f"duration: {duration_str}",
        f"organizer: {organizer}",
        f"participants: {participants_str}",
        f"fathom_recording_id: {recording_id}",
        f"fathom_url: {fathom_url}",
        f"share_url: {share_url}",
        "source: fathom",
        "</metadata>",
    ]
    return "\n".join(lines)


def format_action_items(action_items, summary_next_steps):
    """Format action items grouped by assignee. Falls back to summary Next Steps."""
    if action_items and isinstance(action_items, list) and len(action_items) > 0:
        grouped = {}
        for item in action_items:
            assignee = item.get("assignee") or {}
            name = assignee.get("name") or "Unassigned"
            desc = item.get("description", "")
            if desc:
                grouped.setdefault(name, []).append(desc)

        if grouped:
            parts = []
            for name, items in grouped.items():
                parts.append(f"**{name}**")
                for desc in items:
                    parts.append(f"- {desc}")
                parts.append("")
            return "\n".join(parts).rstrip()

    if summary_next_steps:
        return strip_fathom_links(summary_next_steps)

    return "_No action items recorded._"


def format_transcript(transcript_entries):
    """Convert transcript JSON array to **Speaker:** text markdown."""
    if not transcript_entries or not isinstance(transcript_entries, list):
        return "No transcript captured."

    lines = []
    for entry in transcript_entries:
        speaker = entry.get("speaker", {})
        name = speaker.get("display_name", "Unknown")
        text = entry.get("text", "").strip()
        if text:
            lines.append(f"**{name}:** {text}")

    if not lines:
        return "No transcript captured."

    return "\n\n".join(lines)


def build_document(meeting):
    """Assemble the full markdown document from meeting data."""
    meta = meeting.get("metadata") or {}
    summary_data = meeting.get("summary") or {}

    title = meta.get("title") or meta.get("meeting_title") or "Untitled Meeting"

    summary_md = summary_data.get("markdown_formatted", "")
    sections = parse_summary_sections(summary_md)

    meeting_purpose = sections.get("Meeting Purpose", "").strip()
    key_takeaways = sections.get("Key Takeaways", "").strip()
    topics = sections.get("Topics", "").strip()
    next_steps = sections.get("Next Steps", "").strip()

    summary_text = meeting_purpose if meeting_purpose else "_No summary available._"
    overview_text = key_takeaways if key_takeaways else "_No overview available._"

    if topics:
        topics_formatted = topics
    else:
        topics_formatted = "_No topics available._"

    action_text = format_action_items(
        meeting.get("action_items"), next_steps
    )
    transcript_text = format_transcript(meeting.get("transcript"))
    metadata_block = format_metadata(meeting)

    parts = [
        f"# {title}",
        "",
        metadata_block,
        "",
        "---",
        "",
        "## Summary",
        "",
        summary_text,
        "",
        "---",
        "",
        "## Context",
        "",
        "_To be generated by LLM._",
        "",
        "---",
        "",
        "## Relevance",
        "",
        "_To be generated by LLM._",
        "",
        "---",
        "",
        "## Overview",
        "",
        overview_text,
        "",
        "---",
        "",
        "## Key Topics",
        "",
        topics_formatted,
        "",
        "---",
        "",
        "## Action Items",
        "",
        action_text,
        "",
        "---",
        "",
        "## Transcript",
        transcript_text,
        "",
    ]

    return "\n".join(parts)


def resolve_output_path(meeting):
    """Determine output path: records/transcripts/YYYY-MM/YYYY-MM-DD-slug.md"""
    meta = meeting.get("metadata") or {}
    slug = meeting["slug"]

    dt = parse_datetime(meta.get("recording_start_time")) or \
         parse_datetime(meta.get("scheduled_start_time"))

    if dt:
        month_dir = dt.strftime("%Y-%m")
    else:
        # Extract from folder name (YYYY-MM-DD-...)
        match = re.match(r"(\d{4}-\d{2})-\d{2}-.+", slug)
        month_dir = match.group(1) if match else "unknown"

    out_dir = TRANSCRIPTS_ROOT / month_dir
    return out_dir / f"{slug}.md"


def find_meeting_folders(path):
    """List meeting subfolders inside a year-month directory."""
    folders = []
    p = Path(path)
    if not p.is_dir():
        return folders
    for child in sorted(p.iterdir()):
        if child.is_dir() and MEETING_DIR_PATTERN.match(child.name):
            if (child / "metadata.json").exists():
                folders.append(child)
    return folders


def find_all_downloaded():
    """Find all downloaded meeting folders across all months."""
    folders = []
    for child in sorted(BACKUP_ROOT.iterdir()):
        if child.is_dir() and MONTH_DIR_PATTERN.match(child.name):
            folders.extend(find_meeting_folders(child))
    return folders


def resolve_in_place_path(meeting):
    """Place the .md file inside the source meeting folder."""
    folder = meeting["folder"]
    slug = meeting["slug"]
    return folder / f"{slug}.md"


def process_meeting(folder_path, dry_run=False, force=False, in_place=False):
    """Convert a single meeting folder. Returns (output_path, status)."""
    meeting = load_meeting(folder_path)
    if not meeting or not meeting.get("metadata"):
        return (None, "skip:no-metadata")

    out_path = resolve_in_place_path(meeting) if in_place else resolve_output_path(meeting)

    if out_path.exists() and not force:
        return (out_path, "skip:exists")

    if dry_run:
        return (out_path, "dry-run")

    doc = build_document(meeting)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(doc)

    return (out_path, "written")


def main():
    parser = argparse.ArgumentParser(
        description="Convert Fathom backup dumps to transcript .md files"
    )
    parser.add_argument(
        "meeting",
        nargs="?",
        help="Relative path to a meeting folder (e.g. 2025-06/2025-06-30-ed-jason-weekly)",
    )
    parser.add_argument(
        "--month",
        help="Process all meetings in a year-month directory (e.g. 2025-06)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Process all downloaded meetings",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview output filenames without writing",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing transcript files",
    )
    parser.add_argument(
        "--in-place",
        action="store_true",
        help="Write .md into the source meeting folder instead of records/transcripts/",
    )

    args = parser.parse_args()

    if not args.meeting and not args.month and not args.all:
        parser.print_help()
        sys.exit(1)

    folders = []

    if args.meeting:
        folder = BACKUP_ROOT / args.meeting
        if not folder.is_dir():
            print(f"Error: folder not found: {folder}", file=sys.stderr)
            sys.exit(1)
        folders = [folder]

    elif args.month:
        month_dir = BACKUP_ROOT / args.month
        if not month_dir.is_dir():
            print(f"Error: month directory not found: {month_dir}", file=sys.stderr)
            sys.exit(1)
        folders = find_meeting_folders(month_dir)

    elif args.all:
        folders = find_all_downloaded()

    if not folders:
        print("No meeting folders found.")
        sys.exit(0)

    stats = {"written": 0, "skip:exists": 0, "skip:no-metadata": 0, "dry-run": 0}

    base_path = BACKUP_ROOT if args.in_place else TRANSCRIPTS_ROOT

    for folder in folders:
        out_path, status = process_meeting(
            folder, dry_run=args.dry_run, force=args.force, in_place=args.in_place
        )
        stats[status] = stats.get(status, 0) + 1

        if status == "written":
            print(f"  wrote  {out_path.relative_to(base_path)}")
        elif status == "dry-run":
            print(f"  [dry]  {out_path.relative_to(base_path)}")
        elif status == "skip:exists":
            print(f"  skip   {out_path.relative_to(base_path)} (exists)")
        elif status == "skip:no-metadata":
            print(f"  skip   {folder.name} (no metadata)")

    print()
    print(f"Done. {len(folders)} meetings scanned.")
    print(f"  Written:     {stats.get('written', 0)}")
    print(f"  Skipped:     {stats.get('skip:exists', 0)} (already exist)")
    print(f"  No metadata: {stats.get('skip:no-metadata', 0)}")
    if args.dry_run:
        print(f"  Dry run:     {stats.get('dry-run', 0)}")


if __name__ == "__main__":
    main()
