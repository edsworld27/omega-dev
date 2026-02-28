#!/usr/bin/env python3
"""
HIVE SCANNER — Omega Constitution V10
Scans the Hive telegram_inbox for pending FOUNDER_JOB files.
Returns a formatted list for Claude Code / Antigravity to pick up.
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime

# Configuration
HIVE_DIR = os.path.expanduser(
    os.getenv("OMEGA_HIVE_DIR", "~/Documents/Omega Constitution Pack/Omega System Public/Constution V10/USER SPACE/dev-work/hive")
)
INBOX_DIR = os.path.join(HIVE_DIR, "telegram_inbox")
PROCESSED_FILE = os.path.join(INBOX_DIR, ".processed.json")


def load_processed():
    """Load list of already-processed job IDs."""
    if os.path.exists(PROCESSED_FILE):
        try:
            with open(PROCESSED_FILE, 'r') as f:
                data = json.load(f)
                # Handle old format (plain list) vs new format (dict)
                if isinstance(data, list):
                    return {"processed": data}
                return data
        except:
            pass
    return {"processed": []}


def save_processed(data):
    """Save processed job IDs."""
    with open(PROCESSED_FILE, 'w') as f:
        json.dump(data, f, indent=2)


def mark_processed(job_id: str):
    """Mark a job as processed."""
    data = load_processed()
    if job_id not in data["processed"]:
        data["processed"].append(job_id)
        save_processed(data)


def scan_inbox() -> list:
    """Scan telegram_inbox for FOUNDER_JOB files with STATUS: PENDING."""
    if not os.path.exists(INBOX_DIR):
        return []

    jobs = []
    processed = load_processed()["processed"]

    for filename in sorted(os.listdir(INBOX_DIR)):
        if not filename.startswith("FOUNDER_JOB") or not filename.endswith(".md"):
            continue

        filepath = os.path.join(INBOX_DIR, filename)
        job_id = filename.replace(".md", "")

        # Skip already processed
        if job_id in processed:
            continue

        # Read and check status
        with open(filepath, 'r') as f:
            content = f.read()

        if "STATUS**: PENDING" in content or "STATUS: PENDING" in content:
            # Extract key info (multiple formats supported)
            # Format 1: **Project Name**: X
            # Format 2: # FOUNDER_JOB-001: X
            name_match = re.search(r'\*\*Project Name\*\*:\s*(.+)', content)
            if not name_match:
                name_match = re.search(r'^# FOUNDER_JOB-\d+:\s*(.+)$', content, re.MULTILINE)
            if not name_match:
                # Extract from filename
                name_match = re.search(r'FOUNDER_JOB-\d+-(.+)\.md', filename)

            # Format 1: **Kit**: `X` or Format 2: **KIT**: X
            kit_match = re.search(r'\*\*Kit\*\*:\s*`?([^`\n]+)`?', content, re.IGNORECASE)
            if not kit_match:
                kit_match = re.search(r'\*\*KIT\*\*:\s*(.+)', content)

            # Format 1: **Requested Mode**: `X` or Format 2: **MODE**: X
            mode_match = re.search(r'\*\*Requested Mode\*\*:\s*`?([^`\n]+)`?', content)
            if not mode_match:
                mode_match = re.search(r'\*\*MODE\*\*:\s*(.+)', content)

            jobs.append({
                "id": job_id,
                "file": filepath,
                "name": name_match.group(1).strip() if name_match else "Unknown",
                "kit": kit_match.group(1).strip() if kit_match else "unknown",
                "mode": mode_match.group(1).strip() if mode_match else "FULL DISCOVERY",
                "content": content
            })

    return jobs


def format_jobs_for_agent(jobs: list) -> str:
    """Format pending jobs for Claude Code / Antigravity."""
    if not jobs:
        return "No pending jobs in the Hive inbox."

    output = f"# Pending FOUNDER_JOBs ({len(jobs)})\n\n"
    output += f"Scanned: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"

    for job in jobs:
        output += f"## {job['id']}\n"
        output += f"- **Project**: {job['name']}\n"
        output += f"- **Kit**: {job['kit']}\n"
        output += f"- **Mode**: {job['mode']}\n"
        output += f"- **File**: `{job['file']}`\n\n"

    output += "---\n\n"
    output += "**Next Step**: Pick a job, read its file, and begin scaffolding.\n"
    output += "Use `claim_job(job_id)` to mark as BUILDING before starting.\n"

    return output


def claim_job(job_id: str) -> bool:
    """Claim a job by updating its status to BUILDING."""
    filepath = os.path.join(INBOX_DIR, f"{job_id}.md")
    if not os.path.exists(filepath):
        return False

    with open(filepath, 'r') as f:
        content = f.read()

    # Update status
    content = content.replace("STATUS**: PENDING", "STATUS**: BUILDING")
    content = content.replace("STATUS: PENDING", "STATUS: BUILDING")

    with open(filepath, 'w') as f:
        f.write(content)

    return True


def complete_job(job_id: str, summary: str = "Build complete") -> bool:
    """Mark a job as complete."""
    filepath = os.path.join(INBOX_DIR, f"{job_id}.md")
    if not os.path.exists(filepath):
        return False

    with open(filepath, 'r') as f:
        content = f.read()

    # Update status
    content = content.replace("STATUS**: BUILDING", "STATUS**: COMPLETE")
    content = content.replace("STATUS: BUILDING", "STATUS: COMPLETE")

    # Add completion note
    content += f"\n\n---\n## Completion\n**Completed**: {datetime.now().isoformat()}\n**Summary**: {summary}\n"

    with open(filepath, 'w') as f:
        f.write(content)

    # Mark as processed
    mark_processed(job_id)

    return True


# CLI Interface
if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        cmd = sys.argv[1]

        if cmd == "scan":
            jobs = scan_inbox()
            print(format_jobs_for_agent(jobs))

        elif cmd == "claim" and len(sys.argv) > 2:
            job_id = sys.argv[2]
            if claim_job(job_id):
                print(f"Claimed: {job_id}")
            else:
                print(f"Failed to claim: {job_id}")

        elif cmd == "complete" and len(sys.argv) > 2:
            job_id = sys.argv[2]
            summary = sys.argv[3] if len(sys.argv) > 3 else "Build complete"
            if complete_job(job_id, summary):
                print(f"Completed: {job_id}")
            else:
                print(f"Failed to complete: {job_id}")

        else:
            print("Usage:")
            print("  python hive_scanner.py scan           # List pending jobs")
            print("  python hive_scanner.py claim JOB_ID   # Claim a job")
            print("  python hive_scanner.py complete JOB_ID [summary]  # Complete a job")
    else:
        # Default: scan and print
        jobs = scan_inbox()
        print(format_jobs_for_agent(jobs))
