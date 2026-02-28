#!/usr/bin/env python3
"""
OMEGA RUN - Main Entry Point
=============================

Run this to start the Omega System.

USAGE:
    python omega_run.py              # Start normally
    python omega_run.py --onboard    # Run onboarding
    python omega_run.py --status     # Check system status
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

DROP_ZONE = ROOT_DIR / "00 User" / "00_Drop_Zone"
SEND_OFF = ROOT_DIR / "00 User" / "01_Send_Off"
CONTEXT_FILE = RULES_DIR / "03_Context" / "CONTEXT_DEV.md"


def print_banner():
    print("""
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║                    OMEGA SYSTEM                           ║
║                                                           ║
║         The AI-Powered Project Orchestrator               ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
""")


def check_status():
    """Check system status."""
    print("\n📊 SYSTEM STATUS\n")

    # Check folders exist
    folders = [
        ("Drop Zone", DROP_ZONE),
        ("Send Off", SEND_OFF),
        ("00 Rules", RULES_DIR),
        ("Context", CONTEXT_FILE.parent),
    ]

    for name, path in folders:
        status = "✓" if path.exists() else "✗"
        print(f"  {status} {name}: {path}")

    # Check drop zone contents
    print(f"\n📥 DROP ZONE CONTENTS:")
    if DROP_ZONE.exists():
        items = list(DROP_ZONE.iterdir())
        items = [i for i in items if not i.name.startswith('.')]
        if items:
            for item in items[:10]:
                print(f"  - {item.name}")
        else:
            print("  (empty)")

    # Check context
    print(f"\n📄 CONTEXT:")
    if CONTEXT_FILE.exists():
        with open(CONTEXT_FILE) as f:
            lines = f.readlines()[:10]
            for line in lines:
                print(f"  {line.rstrip()}")
    else:
        print("  (no context file)")


def check_drop_zone():
    """Check if there are files in the drop zone."""
    if not DROP_ZONE.exists():
        return []

    items = list(DROP_ZONE.iterdir())
    return [i for i in items if not i.name.startswith('.') and i.name != 'README.md']


def run_onboarding():
    """Run the onboarding process."""
    onboard_script = SCRIPT_DIR / "omega_onboard.py"
    if onboard_script.exists():
        subprocess.run([sys.executable, str(onboard_script)])
    else:
        print("Onboarding script not found. Creating basic setup...")
        basic_onboard()


def basic_onboard():
    """Basic onboarding if full script missing."""
    print("""
╔═══════════════════════════════════════════════════════════╗
║                    OMEGA ONBOARDING                       ║
╚═══════════════════════════════════════════════════════════╝

Welcome to the Omega System!

SETUP STEPS:
1. Drop your project files in: 00 User/00_Drop_Zone/
2. Tell your AI IDE to read the constitution from:
   https://github.com/edsworld27/omega-constitution
3. The AI will organize your project and guide you.

REFERENCES:
- Constitution: https://github.com/edsworld27/omega-constitution
- Store (kits/skills): https://github.com/edsworld27/omega-store

Ready to start? Drop your files and run your AI!
""")


def main():
    print_banner()

    if len(sys.argv) > 1:
        if sys.argv[1] == "--onboard":
            run_onboarding()
        elif sys.argv[1] == "--status":
            check_status()
        elif sys.argv[1] == "--help":
            print(__doc__)
        else:
            print(f"Unknown option: {sys.argv[1]}")
            print("Use --help for usage")
    else:
        # Default: check status and guide
        check_status()

        # Check if there are files to process
        dropped = check_drop_zone()
        if dropped:
            print(f"\n📦 Found {len(dropped)} item(s) in Drop Zone!")
            print("Ready for AI processing.")
        else:
            print("\n💡 TIP: Drop your project files in 00 User/00_Drop_Zone/")

        print("\n🤖 Open this folder in your AI IDE and say:")
        print('   "Read the constitution and help me with my project"')
        print("\n")


if __name__ == "__main__":
    main()
