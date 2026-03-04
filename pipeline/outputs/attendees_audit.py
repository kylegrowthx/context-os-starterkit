#!/usr/bin/env python3
"""
Extract external attendees from meeting records and audit contact files.
"""

import json
import os
import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple, Set
import unicodedata

CONTACTS_DIR = "/sessions/determined-funny-bell/mnt/growthx-context/records/contacts"
MEETINGS_DIR = "/sessions/determined-funny-bell/mnt/growthx-context/records/meetings"
OUTPUT_FILE = "/sessions/determined-funny-bell/attendees-audit.json"

# Internal domain patterns
INTERNAL_DOMAINS = {"@growthxlabs.com", "@growthx.ai"}


def normalize_name(name: str) -> str:
    """
    Normalize a name to lowercase with hyphens.
    Handles special characters and accents.
    """
    # Remove leading/trailing whitespace
    name = name.strip()
    
    # Normalize unicode (decompose accents)
    name = unicodedata.normalize('NFD', name)
    name = ''.join(c for c in name if unicodedata.category(c) != 'Mn')
    
    # Convert to lowercase
    name = name.lower()
    
    # Replace spaces, underscores, and dots with hyphens
    name = re.sub(r'[\s_.]+', '-', name)
    
    # Remove special characters except hyphens
    name = re.sub(r'[^\w\-]', '', name)
    
    # Remove consecutive hyphens
    name = re.sub(r'-+', '-', name)
    
    # Remove leading/trailing hyphens
    name = name.strip('-')
    
    return name


def extract_name_from_email(email: str) -> str:
    """
    Extract a display name from an email address.
    firstname.lastname@company.com -> Firstname Lastname
    """
    # Get local part (before @)
    local = email.split('@')[0]
    
    # Remove c- prefix (contractor prefix)
    if local.startswith('c-'):
        local = local[2:]
    
    # Split on dots and hyphens
    parts = re.split(r'[.\-_]', local)
    
    # Capitalize each part
    parts = [part.capitalize() for part in parts if part]
    
    # Join with space
    return ' '.join(parts)


def parse_attendees(attendees_str: str) -> List[Tuple[str, str]]:
    """
    Parse attendees string format: "Name1 (email1), Name2 (email2), email3@example.com"
    Returns list of (name, email) tuples.
    """
    attendees = []
    
    # Split by comma (handle both comma + space and just comma)
    entries = [e.strip() for e in attendees_str.split(',')]
    
    for entry in entries:
        entry = entry.strip()
        if not entry:
            continue
        
        # Try to match "Name (email)" pattern
        match = re.match(r'^(.+?)\s*\(([^)]+)\)$', entry)
        
        if match:
            # Named entry
            name = match.group(1).strip()
            email = match.group(2).strip()
        else:
            # Email-only entry
            email = entry.strip()
            name = extract_name_from_email(email)
        
        attendees.append((name, email))
    
    return attendees


def is_internal_attendee(email: str) -> bool:
    """
    Check if an attendee is internal (GrowthX employee or contractor).
    """
    # Contractors have c- prefix in their email
    if re.search(r'@.*c-', email):
        return True
    
    # Check internal domains
    for domain in INTERNAL_DOMAINS:
        if email.endswith(domain):
            return True
    
    return False


def extract_company_from_email(email: str) -> str:
    """
    Extract company name from email domain.
    """
    # Get domain part
    domain = email.split('@')[1] if '@' in email else 'unknown'
    
    # Remove common TLDs
    domain = re.sub(r'\.(com|io|org|net|co|ai)$', '', domain)
    
    # Capitalize each word
    parts = domain.split('.')
    company = ' '.join([part.capitalize() for part in parts])
    
    return company


def contact_file_exists(name: str) -> Tuple[bool, str | None]:
    """
    Check if a contact file exists for a given name.
    Returns (exists, filename)
    """
    normalized = normalize_name(name)
    contact_file = f"{normalized}-v1.md"
    full_path = os.path.join(CONTACTS_DIR, contact_file)
    
    if os.path.exists(full_path):
        return True, contact_file
    
    return False, contact_file


def get_all_meeting_files() -> List[str]:
    """
    Get all .md files from 2026-01 and 2026-02 meeting directories.
    """
    meeting_files = []
    
    for month in ['2026-01', '2026-02']:
        month_dir = os.path.join(MEETINGS_DIR, month)
        if os.path.isdir(month_dir):
            for file in os.listdir(month_dir):
                if file.endswith('.md'):
                    meeting_files.append(os.path.join(month_dir, file))
    
    return sorted(meeting_files)


def extract_attendees_from_file(filepath: str) -> List[Tuple[str, str]]:
    """
    Extract attendees from a meeting file.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract metadata block
        match = re.search(r'<metadata>(.*?)</metadata>', content, re.DOTALL)
        if not match:
            return []
        
        metadata = match.group(1)
        
        # Find attendees line
        attendees_match = re.search(r'attendees:\s*(.+?)(?:\n|$)', metadata)
        if not attendees_match:
            return []
        
        attendees_str = attendees_match.group(1).strip()
        return parse_attendees(attendees_str)
    
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return []


def get_relative_meeting_path(filepath: str) -> str:
    """
    Get relative path for a meeting file (e.g., 2026-01/filename.md)
    """
    parts = filepath.split('/')
    # Find index of '2026-01' or '2026-02'
    for i, part in enumerate(parts):
        if part in ['2026-01', '2026-02']:
            return '/'.join(parts[i:])
    return filepath


def main():
    """Main execution."""
    print("Extracting external attendees from meeting records...")
    
    # Get all meeting files
    meeting_files = get_all_meeting_files()
    print(f"Found {len(meeting_files)} meeting files\n")
    
    # Track attendees
    attendees_map: Dict[str, Dict] = {}  # Key: normalized email or name
    attendee_meetings: Dict[str, List[str]] = defaultdict(list)
    
    # Process each meeting file
    for filepath in meeting_files:
        relative_path = get_relative_meeting_path(filepath)
        attendee_list = extract_attendees_from_file(filepath)
        
        for name, email in attendee_list:
            # Skip internal attendees
            if is_internal_attendee(email):
                continue
            
            # Use email as key for uniqueness
            key = email.lower()
            
            if key not in attendees_map:
                has_contact, contact_file = contact_file_exists(name)
                
                attendees_map[key] = {
                    "name": name,
                    "email": email,
                    "company": extract_company_from_email(email),
                    "has_contact": has_contact,
                    "contact_file": contact_file if has_contact else None,
                }
            
            # Track which meetings this person attended
            attendee_meetings[key].append(relative_path)
    
    # Build output structure
    total_external = len(attendee_list) if attendee_list else 0
    unique_external = len(attendees_map)
    with_contact = sum(1 for a in attendees_map.values() if a["has_contact"])
    missing_contact = unique_external - with_contact
    
    output = {
        "total_external_attendees": len([1 for f in meeting_files for _, e in extract_attendees_from_file(f) if not is_internal_attendee(e)]),
        "unique_external_attendees": unique_external,
        "with_contact_records": with_contact,
        "missing_contact_records": missing_contact,
        "attendees": {}
    }
    
    # Add attendee details
    for email_key, attendee_info in sorted(attendees_map.items()):
        normalized_key = normalize_name(attendee_info["name"])
        attendee_info["meetings"] = sorted(attendee_meetings[email_key])
        output["attendees"][normalized_key] = attendee_info
    
    # Write JSON output
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"Audit complete! Results saved to {OUTPUT_FILE}\n")
    
    # Print summary
    print("=" * 70)
    print("ATTENDEES AUDIT SUMMARY")
    print("=" * 70)
    print(f"Total unique external attendees: {unique_external}")
    print(f"With contact records: {with_contact}")
    print(f"Missing contact records: {missing_contact}")
    print(f"Coverage: {with_contact}/{unique_external} ({100*with_contact//unique_external if unique_external > 0 else 0}%)\n")
    
    # List missing contacts
    if missing_contact > 0:
        print("MISSING CONTACT RECORDS:")
        print("-" * 70)
        missing_list = [
            (a["name"], a["email"], len(attendee_meetings[a["email"].lower()]))
            for a in attendees_map.values()
            if not a["has_contact"]
        ]
        missing_list.sort(key=lambda x: x[2], reverse=True)
        
        for name, email, meeting_count in missing_list:
            print(f"{name:40} {email:40} ({meeting_count} meetings)")
    
    print("=" * 70)


if __name__ == "__main__":
    main()
