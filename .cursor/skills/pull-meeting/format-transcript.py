"""
Format a Fireflies transcript cache file into markdown.

Usage:
    python3 format-transcript.py <cache_file.txt> > /tmp/formatted_transcript.md

The cache file is the raw output from fireflies_get_transcript, saved to the
agent-tools directory. This script extracts the Sentences section and converts
each "Speaker: text" line into "**Speaker:** text" markdown format.
"""
import sys
import re


def format_transcript(cache_path):
    with open(cache_path, "r") as f:
        content = f.read()

    # Extract sentences section (between "Sentences:" and "Title:" or end of file)
    sentences_match = re.search(
        r"Sentences:\s*(.*?)(?:\nTitle:|$)", content, re.DOTALL
    )
    if not sentences_match:
        print("No transcript captured (audio not available).")
        return None

    sentences_raw = sentences_match.group(1).strip()
    if not sentences_raw:
        print("No transcript captured (audio not available).")
        return None

    lines = sentences_raw.split("\n")

    output = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Each line is "Speaker Name: dialogue text"
        colon_idx = line.find(":")
        if 0 < colon_idx < 60:
            speaker = line[:colon_idx].strip()
            text = line[colon_idx + 1 :].strip()
            if text:
                output.append(f"**{speaker}:** {text}")
        else:
            # Continuation or odd format — append to previous line
            if output:
                output[-1] += " " + line
            else:
                output.append(line)

    return "\n\n".join(output)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 format-transcript.py <cache_file.txt>")
        sys.exit(1)
    result = format_transcript(sys.argv[1])
    if result:
        print(result)
