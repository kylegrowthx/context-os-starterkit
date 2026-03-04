"""
Assemble a complete transcript .md from Fireflies raw data.

Usage:
    python3 format-meeting.py <summary_file> <transcript_file> [-o output.md]
    python3 format-meeting.py <summary_file> <transcript_file> --duration 60 --meeting-link "https://..."

Inputs:
    summary_file   — raw text output from fireflies_get_summary
    transcript_file — raw text output from fireflies_get_transcript

Optional args:
    -o, --output      Output file path (default: stdout)
    --duration        Meeting duration in minutes (not in summary data)
    --meeting-link    Zoom/Meet link (not in summary data)
    --attendees       Comma-separated "Name <email>" pairs for richer metadata

The script produces a complete .md with all deterministic sections filled.
LLM placeholder comments mark sections that need enrichment.
"""
import sys
import re
import argparse
from datetime import datetime
from pathlib import Path

SUMMARY_FIELDS = [
    "Keywords",
    "Action Items",
    "Shorthand Bullet",
    "Notes",
    "Overview",
    "Bullet Gist",
    "Gist",
    "Short Summary",
    "Transcript Chapters",
]


def parse_top_level(text):
    """Extract top-level key-value pairs before the Summary blob."""
    fields = {}
    lines = text.split("\n")
    summary_start = None

    for i, line in enumerate(lines):
        if line.startswith("Summary:"):
            summary_start = i
            break
        if ":" in line:
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()

    if summary_start is not None:
        first_line = lines[summary_start].partition(":")[2].strip()
        rest = "\n".join(lines[summary_start + 1 :])
        fields["_summary_blob"] = (first_line + "\n" + rest).strip()

    return fields


def parse_summary_blob(blob):
    """Split the Summary blob into named sub-fields."""
    pattern = r"(?:,\s*)?(" + "|".join(re.escape(f) for f in SUMMARY_FIELDS) + r"):\s*"
    markers = list(re.finditer(pattern, blob))
    if not markers:
        return {}

    result = {}
    for i, m in enumerate(markers):
        name = m.group(1)
        start = m.end()
        end = markers[i + 1].start() if i + 1 < len(markers) else len(blob)
        content = blob[start:end].strip().rstrip(",").strip()
        result[name] = content
    return result


def parse_transcript_file(text):
    """Parse the raw fireflies_get_transcript output."""
    speakers = []
    sentences_text = ""

    speakers_match = re.search(r"Speakers:\s*(.*?)(?:\n\w+:|$)", text, re.DOTALL)
    if speakers_match:
        speakers = [s.strip() for s in speakers_match.group(1).strip().split(",") if s.strip()]

    sentences_match = re.search(r"Sentences:\s*(.*?)(?:\nTitle:|$)", text, re.DOTALL)
    if sentences_match:
        sentences_text = sentences_match.group(1).strip()

    return speakers, sentences_text


def format_transcript_md(sentences_text):
    """Convert raw sentences into markdown-formatted transcript."""
    if not sentences_text:
        return "No transcript captured (audio not available)."

    lines = sentences_text.split("\n")
    output = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        colon_idx = line.find(":")
        if 0 < colon_idx < 60:
            speaker = line[:colon_idx].strip()
            text = line[colon_idx + 1 :].strip()
            if text:
                output.append(f"**{speaker}:** {text}")
        else:
            if output:
                output[-1] += " " + line
            else:
                output.append(line)

    return "\n\n".join(output) if output else "No transcript captured (audio not available)."


def format_date_time(date_string):
    """Parse ISO date string into (YYYY-MM-DD, HH:MM UTC)."""
    try:
        dt = datetime.fromisoformat(date_string.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d"), dt.strftime("%H:%M") + " UTC"
    except (ValueError, AttributeError):
        return "unknown", "unknown"


def clean_notes_for_key_topics(notes_text):
    """Convert Fireflies Notes into clean Key Topics markdown."""
    if not notes_text:
        return "_No key topics available._"

    cleaned = notes_text.strip()
    cleaned = re.sub(r"\([\d:]+\)", "", cleaned)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned


def clean_overview(overview_text):
    """Clean up the overview bullets."""
    if not overview_text:
        return "_No overview available._"
    cleaned = overview_text.strip()
    if not cleaned.startswith("-"):
        lines = cleaned.split("\n")
        formatted = []
        for line in lines:
            line = line.strip()
            if line and not line.startswith("-"):
                formatted.append(f"- {line}")
            elif line:
                formatted.append(line)
        cleaned = "\n".join(formatted)
    return cleaned


def clean_action_items(action_items_text):
    """Clean up action items, preserving speaker grouping."""
    if not action_items_text:
        return "_No action items recorded._"
    cleaned = action_items_text.strip()
    cleaned = re.sub(r"\([\d:]+\)", "", cleaned)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned


def assemble_md(top_level, summary_fields, speakers, transcript_md, args):
    """Build the complete markdown file."""
    title = top_level.get("Title", "Untitled Meeting")
    fireflies_id = top_level.get("Id", "")
    date_str = top_level.get("DateString", "")
    organizer = top_level.get("Organizer Email", "")
    date, time = format_date_time(date_str)

    participants = ", ".join(speakers) if speakers else "unknown"
    if args.attendees:
        participants = args.attendees

    duration_str = f"{args.duration} minutes" if args.duration else "unknown"
    meeting_link = args.meeting_link or ""
    transcript_url = f"https://app.fireflies.ai/view/{fireflies_id}" if fireflies_id else ""

    keywords = summary_fields.get("Keywords", "")
    short_summary = summary_fields.get("Short Summary", "_No summary available._")
    overview = clean_overview(summary_fields.get("Overview", ""))
    notes = clean_notes_for_key_topics(summary_fields.get("Notes", ""))
    action_items = clean_action_items(summary_fields.get("Action Items", ""))

    sections = []

    sections.append(f"# {title}")
    sections.append("")

    meta_lines = [
        "<metadata>",
        f"date: {date}",
        f"time: {time}",
        f"duration: {duration_str}",
        f"organizer: {organizer}",
        f"participants: {participants}",
        f"fireflies_id: {fireflies_id}",
    ]
    if meeting_link:
        meta_lines.append(f"meeting_link: {meeting_link}")
    meta_lines.append(f"transcript_url: {transcript_url}")
    if keywords:
        meta_lines.append(f"keywords: {keywords}")
    meta_lines.append("source: fireflies")
    meta_lines.append("</metadata>")
    sections.append("\n".join(meta_lines))

    sections.append("\n---\n")
    sections.append("## Summary\n")
    sections.append(f"<!-- LLM: Rewrite in GrowthX voice. Lead with the most important outcome. 2-3 sentences. -->\n{short_summary}")

    sections.append("\n---\n")
    sections.append("## Context\n")
    sections.append("<!-- LLM: Why this meeting happened, who these people are, where it fits in ongoing work -->")

    sections.append("\n---\n")
    sections.append("## Relevance\n")
    sections.append("<!-- LLM: Multi-dimensional impact to GrowthX areas. Concrete bullets with numbers/names/dates. -->")

    sections.append("\n---\n")
    sections.append("## Decisions & Commitments\n")
    sections.append("<!-- LLM: Explicit decisions made + promises/commitments by specific people -->")

    sections.append("\n---\n")
    sections.append("## Open Questions\n")
    sections.append("<!-- LLM: Items raised but not resolved that need follow-up -->")

    sections.append("\n---\n")
    sections.append("## Overview\n")
    sections.append(overview)

    sections.append("\n---\n")
    sections.append("## Key Topics\n")
    sections.append(notes)

    sections.append("\n---\n")
    sections.append("## Action Items\n")
    sections.append(action_items)

    sections.append("\n---\n")
    sections.append("## Transcript\n")
    sections.append(transcript_md)

    return "\n".join(sections) + "\n"


def main():
    parser = argparse.ArgumentParser(description="Assemble transcript .md from Fireflies data")
    parser.add_argument("summary_file", help="Path to fireflies_get_summary output")
    parser.add_argument("transcript_file", help="Path to fireflies_get_transcript output")
    parser.add_argument("-o", "--output", help="Output file path (default: stdout)")
    parser.add_argument("--duration", type=int, help="Meeting duration in minutes")
    parser.add_argument("--meeting-link", help="Zoom/Meet link")
    parser.add_argument("--attendees", help="Comma-separated participant names")
    args = parser.parse_args()

    with open(args.summary_file, "r") as f:
        summary_raw = f.read()
    with open(args.transcript_file, "r") as f:
        transcript_raw = f.read()

    top_level = parse_top_level(summary_raw)
    summary_fields = parse_summary_blob(top_level.get("_summary_blob", ""))
    speakers, sentences_text = parse_transcript_file(transcript_raw)
    transcript_md = format_transcript_md(sentences_text)

    result = assemble_md(top_level, summary_fields, speakers, transcript_md, args)

    if args.output:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, "w") as f:
            f.write(result)
        print(f"Wrote {args.output}", file=sys.stderr)
    else:
        print(result)


if __name__ == "__main__":
    main()
