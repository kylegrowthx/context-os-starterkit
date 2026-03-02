#!/usr/bin/env python3
"""
PDF to Markdown Converter

Converts PDF files to clean Markdown text. Handles three PDF types:
1. Text-based PDFs (extractable text via pdfplumber)
2. Image-based / scanned PDFs (OCR via Tesseract)
3. Oversized single-page PDFs (tiled rendering + OCR)

Dependencies:
    pip install pdfplumber pytesseract pillow

System dependencies:
    - Ghostscript (gs) for rendering
    - Tesseract OCR (tesseract) for image-based PDFs

Usage:
    python3 pdf-to-markdown.py <input.pdf> [--output output.md] [--dpi 200]

    If --output is omitted, writes to the same directory as the input with .md extension.

Examples:
    python3 pdf-to-markdown.py transcript.pdf
    python3 pdf-to-markdown.py scan.pdf --output clean-transcript.md --dpi 300
"""

import argparse
import os
import re
import subprocess
import sys
import tempfile

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def extract_text_pdfplumber(pdf_path: str) -> str:
    """Try direct text extraction with pdfplumber. Returns text or empty string."""
    try:
        import pdfplumber
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n\n"
        return text.strip()
    except Exception as e:
        print(f"  pdfplumber failed: {e}", file=sys.stderr)
        return ""


def get_page_info(pdf_path: str) -> list[dict]:
    """Get page count and dimensions using pypdf."""
    try:
        from pypdf import PdfReader
        reader = PdfReader(pdf_path)
        pages = []
        for i, page in enumerate(reader.pages):
            media_box = page.get("/MediaBox")
            if media_box:
                width = float(media_box[2]) - float(media_box[0])
                height = float(media_box[3]) - float(media_box[1])
            else:
                width, height = 612, 792  # default letter
            pages.append({"index": i, "width_pts": width, "height_pts": height})
        return pages
    except Exception as e:
        print(f"  pypdf page info failed: {e}", file=sys.stderr)
        return [{"index": 0, "width_pts": 612, "height_pts": 792}]


def is_oversized_page(page_info: dict, threshold_pts: float = 2000) -> bool:
    """A normal letter page is 612x792 pts. Anything much larger needs special handling."""
    return page_info["width_pts"] > threshold_pts or page_info["height_pts"] > threshold_pts


def render_page_gs(pdf_path: str, page_num: int, dpi: int, output_png: str) -> bool:
    """Render a single PDF page to PNG using Ghostscript."""
    try:
        result = subprocess.run(
            [
                "gs", "-q", "-dNOPAUSE", "-dBATCH",
                "-sDEVICE=pnggray",
                f"-r{dpi}",
                f"-dFirstPage={page_num + 1}",
                f"-dLastPage={page_num + 1}",
                f"-sOutputFile={output_png}",
                pdf_path,
            ],
            capture_output=True, text=True, timeout=120,
        )
        return result.returncode == 0 and os.path.exists(output_png)
    except Exception as e:
        print(f"  Ghostscript render failed: {e}", file=sys.stderr)
        return False


def ocr_image(image_path: str) -> str:
    """OCR a full image file."""
    import pytesseract
    from PIL import Image
    Image.MAX_IMAGE_PIXELS = None
    img = Image.open(image_path)
    return pytesseract.image_to_string(img, config="--psm 6 --oem 1")


def ocr_image_tiled(image_path: str, tile_height: int = 1500) -> str:
    """OCR a large image by tiling it into horizontal strips for better accuracy."""
    import pytesseract
    from PIL import Image
    Image.MAX_IMAGE_PIXELS = None

    img = Image.open(image_path)
    width, height = img.size
    full_text = ""

    for y in range(0, height, tile_height):
        box = (0, y, width, min(y + tile_height, height))
        tile = img.crop(box)
        text = pytesseract.image_to_string(tile, config="--psm 6 --oem 1")
        full_text += text + "\n"

    return full_text


# ---------------------------------------------------------------------------
# Post-processing: raw OCR text -> clean Markdown
# ---------------------------------------------------------------------------

def clean_ocr_text(raw: str) -> str:
    """
    Clean up noisy OCR output into readable Markdown.

    Handles:
    - Speaker labels (e.g., "Marcel 1:23" or "Kristin Fracchia 4:56")
    - Excessive whitespace
    - Common OCR artifacts
    """
    lines = raw.split("\n")
    cleaned = []

    for line in lines:
        line = line.strip()
        if not line:
            cleaned.append("")
            continue

        # Skip lines that are pure noise (very short gibberish)
        if len(line) < 3 and not line[0].isalpha():
            continue

        # Collapse multiple spaces
        line = re.sub(r" {2,}", " ", line)

        # Detect speaker labels: "Name Timestamp" pattern
        # Common formats: "Marcel 1:23", "Kristin Fracchia 1:23:45", "Speaker Name HH:MM"
        speaker_match = re.match(
            r"^([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\s*[-—]?\s*(\d{1,2}:\d{2}(?::\d{2})?)\s*$",
            line,
        )
        if speaker_match:
            name = speaker_match.group(1)
            timestamp = speaker_match.group(2)
            cleaned.append(f"\n**{name}** [{timestamp}]\n")
            continue

        # Also detect speaker labels with different patterns from this specific PDF
        speaker_match2 = re.match(
            r"^([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\s+(\d[\d:hHmMsS]+)\s*$",
            line,
        )
        if speaker_match2:
            name = speaker_match2.group(1)
            timestamp = speaker_match2.group(2)
            cleaned.append(f"\n**{name}** [{timestamp}]\n")
            continue

        cleaned.append(line)

    text = "\n".join(cleaned)

    # Collapse 3+ blank lines into 2
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


# ---------------------------------------------------------------------------
# Main conversion pipeline
# ---------------------------------------------------------------------------

def convert_pdf_to_markdown(pdf_path: str, dpi: int = 200) -> str:
    """
    Convert a PDF to Markdown text.

    Strategy:
    1. Try direct text extraction (fastest, best quality)
    2. If that fails, render to image and OCR
    3. For oversized pages, use tiled OCR for accuracy
    """
    print(f"Converting: {pdf_path}")

    # Step 1: Try direct text extraction
    print("  Attempting direct text extraction...")
    text = extract_text_pdfplumber(pdf_path)
    if len(text) > 100:
        print(f"  Direct extraction succeeded: {len(text)} chars")
        return text

    # Step 2: Get page info to decide OCR strategy
    pages = get_page_info(pdf_path)
    print(f"  Pages: {len(pages)}")

    full_text = ""

    with tempfile.TemporaryDirectory() as tmpdir:
        for page_info in pages:
            page_idx = page_info["index"]
            oversized = is_oversized_page(page_info)

            if oversized:
                print(f"  Page {page_idx + 1}: oversized ({page_info['width_pts']:.0f}x{page_info['height_pts']:.0f} pts) — using tiled OCR at {dpi} DPI")
            else:
                print(f"  Page {page_idx + 1}: normal size — using standard OCR at {dpi} DPI")

            png_path = os.path.join(tmpdir, f"page_{page_idx}.png")

            if not render_page_gs(pdf_path, page_idx, dpi, png_path):
                print(f"  WARNING: Could not render page {page_idx + 1}", file=sys.stderr)
                continue

            if oversized:
                page_text = ocr_image_tiled(png_path, tile_height=1500)
            else:
                page_text = ocr_image(png_path)

            print(f"  Page {page_idx + 1}: extracted {len(page_text)} chars")
            full_text += page_text + "\n\n"

    if not full_text.strip():
        print("  ERROR: No text extracted from any method.", file=sys.stderr)
        return ""

    # Step 3: Clean up OCR output
    print("  Cleaning OCR output...")
    cleaned = clean_ocr_text(full_text)
    print(f"  Final output: {len(cleaned)} chars")

    return cleaned


def main():
    parser = argparse.ArgumentParser(
        description="Convert PDF files to clean Markdown text.",
        epilog="Handles text PDFs, scanned images, and oversized single-page layouts.",
    )
    parser.add_argument("input", help="Path to the input PDF file")
    parser.add_argument("--output", "-o", help="Output .md path (default: same dir, .md extension)")
    parser.add_argument("--dpi", type=int, default=200, help="DPI for rendering (default: 200, higher = slower but more accurate)")

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: File not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    # Default output path: same directory, same name, .md extension
    if args.output:
        output_path = args.output
    else:
        base = os.path.splitext(args.input)[0]
        output_path = base + ".md"

    # Convert
    markdown = convert_pdf_to_markdown(args.input, dpi=args.dpi)

    if not markdown:
        print("Error: Conversion produced no output.", file=sys.stderr)
        sys.exit(1)

    # Write output
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown)

    print(f"\nDone. Output: {output_path}")
    print(f"Characters: {len(markdown)}")


if __name__ == "__main__":
    main()
