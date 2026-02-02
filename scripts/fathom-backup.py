#!/usr/bin/env python3
"""
Fathom Meeting Transcript Backup Script

Fetches meetings and transcripts from Fathom.video API.
Usage:
  FATHOM_API_KEY=your_key python fathom-backup.py
  
Or export the key first:
  export FATHOM_API_KEY=your_key
  python fathom-backup.py
"""

import os
import sys
import json
import time
import requests
from datetime import datetime

API_KEY = os.environ.get("FATHOM_API_KEY")
BASE_URL = "https://api.fathom.ai/external/v1"

def fetch_meetings(limit=10, include_transcript=True, include_summary=True, max_retries=3):
    """Fetch recent meetings from Fathom API."""
    if not API_KEY:
        print("Error: FATHOM_API_KEY environment variable not set")
        sys.exit(1)
    
    params = {
        "include_transcript": str(include_transcript).lower(),
        "include_summary": str(include_summary).lower(),
        "include_action_items": "true"
    }
    
    headers = {"X-Api-Key": API_KEY}
    
    meetings = []
    cursor = None
    
    while len(meetings) < limit:
        if cursor:
            params["cursor"] = cursor
        
        # Retry logic for transient errors
        for attempt in range(max_retries):
            response = requests.get(
                f"{BASE_URL}/meetings",
                headers=headers,
                params=params
            )
            
            if response.status_code == 200:
                break
            elif response.status_code in [500, 502, 503, 504]:
                if attempt < max_retries - 1:
                    wait = 2 ** attempt  # exponential backoff
                    print(f"Got {response.status_code}, retrying in {wait}s...")
                    time.sleep(wait)
                else:
                    print(f"Error: API returned {response.status_code} after {max_retries} attempts")
                    print(response.text)
                    sys.exit(1)
            else:
                print(f"Error: API returned {response.status_code}")
                print(response.text)
                sys.exit(1)
        
        data = response.json()
        meetings.extend(data.get("items", []))
        
        cursor = data.get("next_cursor")
        if not cursor:
            break
    
    return meetings[:limit]


def display_meetings(meetings):
    """Display meeting summary."""
    print(f"\n{'='*60}")
    print(f"Found {len(meetings)} meetings")
    print(f"{'='*60}\n")
    
    for i, meeting in enumerate(meetings, 1):
        title = meeting.get("title") or meeting.get("meeting_title") or "Untitled"
        created = meeting.get("created_at", "Unknown date")
        recorded_by = meeting.get("recorded_by", {}).get("name", "Unknown")
        url = meeting.get("url", "")
        
        # Transcript stats
        transcript = meeting.get("transcript", [])
        transcript_lines = len(transcript)
        
        # Summary
        summary = meeting.get("default_summary", {})
        summary_text = summary.get("markdown_formatted", "No summary")[:200]
        
        print(f"{i}. {title}")
        print(f"   Date: {created}")
        print(f"   Recorded by: {recorded_by}")
        print(f"   URL: {url}")
        print(f"   Transcript segments: {transcript_lines}")
        if summary_text and summary_text != "No summary":
            print(f"   Summary preview: {summary_text}...")
        print()


def save_backup(meetings, filename=None):
    """Save meetings to JSON file."""
    if not filename:
        filename = f"fathom_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)
    
    with open(filepath, "w") as f:
        json.dump(meetings, f, indent=2)
    
    print(f"\nBackup saved to: {filepath}")
    return filepath


if __name__ == "__main__":
    print("Fetching last 10 meetings from Fathom...")
    meetings = fetch_meetings(limit=10)
    display_meetings(meetings)
    
    # Optionally save to file
    if meetings:
        save = input("Save backup to JSON file? (y/n): ").strip().lower()
        if save == 'y':
            save_backup(meetings)
