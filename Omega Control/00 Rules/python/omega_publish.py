#!/usr/bin/env python3
"""
OMEGA PUBLISH - Git Publishing
===============================

Publishes the omega-system repo to GitHub.

USAGE:
    python omega_publish.py "commit message"
    python omega_publish.py --status
"""

import os
import sys
import subprocess
from pathlib import Path

# Get paths
SCRIPT_DIR = Path(__file__).parent.resolve()
RULES_DIR = SCRIPT_DIR.parent
CONTROL_DIR = RULES_DIR.parent
ROOT_DIR = CONTROL_DIR.parent


def run_cmd(cmd, cwd=None):
    """Run a command and return output."""
    result = subprocess.run(
        cmd,
        cwd=cwd or ROOT_DIR,
        capture_output=True,
        text=True
    )
    return result.stdout.strip(), result.stderr.strip(), result.returncode


def check_status():
    """Check git status."""
    print("\n📊 GIT STATUS\n")

    stdout, stderr, code = run_cmd(["git", "status", "--short"])

    if code != 0:
        print(f"Error: {stderr}")
        return

    if stdout:
        print("Changes:")
        for line in stdout.split('\n'):
            print(f"  {line}")
    else:
        print("No changes to commit.")

    # Show current branch
    stdout, _, _ = run_cmd(["git", "branch", "--show-current"])
    print(f"\nBranch: {stdout}")

    # Show remote
    stdout, _, _ = run_cmd(["git", "remote", "-v"])
    if stdout:
        print(f"\nRemote:")
        for line in stdout.split('\n')[:2]:
            print(f"  {line}")


def publish(message):
    """Publish changes to GitHub."""
    print(f"\n🚀 PUBLISHING TO GITHUB\n")
    print(f"Message: {message}\n")

    # Add all changes
    print("Adding changes...")
    stdout, stderr, code = run_cmd(["git", "add", "-A"])
    if code != 0:
        print(f"Error adding: {stderr}")
        return False

    # Check if there are changes
    stdout, _, _ = run_cmd(["git", "status", "--porcelain"])
    if not stdout:
        print("No changes to commit.")
        return True

    # Commit
    print("Committing...")
    stdout, stderr, code = run_cmd(["git", "commit", "-m", message])
    if code != 0:
        print(f"Error committing: {stderr}")
        return False
    print(f"  ✓ Committed")

    # Push
    print("Pushing to GitHub...")
    stdout, stderr, code = run_cmd(["git", "push"])
    if code != 0:
        print(f"Error pushing: {stderr}")
        return False
    print(f"  ✓ Pushed")

    print("\n✅ PUBLISHED SUCCESSFULLY\n")
    return True


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        check_status()
        sys.exit(0)

    if sys.argv[1] == "--status":
        check_status()
    elif sys.argv[1] == "--help":
        print(__doc__)
    else:
        message = " ".join(sys.argv[1:])
        publish(message)


if __name__ == "__main__":
    main()
