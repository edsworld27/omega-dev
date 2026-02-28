#!/usr/bin/env python3
"""
OMEGA ONBOARD - User Onboarding
================================

Sets up a new user's environment and guides them through first use.

USAGE:
    python omega_onboard.py
"""

import os
import sys
from pathlib import Path
from datetime import datetime

# Get paths
SCRIPT_DIR = Path(__file__).parent.resolve()
RULES_DIR = SCRIPT_DIR.parent
CONTROL_DIR = RULES_DIR.parent
ROOT_DIR = CONTROL_DIR.parent

DROP_ZONE = ROOT_DIR / "00 User" / "00_Drop_Zone"
SEND_OFF = ROOT_DIR / "00 User" / "01_Send_Off"
PROJECTS = ROOT_DIR / "Projects"
CONTEXT_FILE = RULES_DIR / "03_Context" / "CONTEXT_DEV.md"


def print_banner():
    print("""
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║                  OMEGA ONBOARDING                         ║
║                                                           ║
║              Welcome to the Omega System                  ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
""")


def ensure_folders():
    """Make sure all required folders exist."""
    folders = [
        DROP_ZONE,
        SEND_OFF,
        PROJECTS,
        RULES_DIR / "03_Context",
    ]

    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)

    return True


def create_readme_files():
    """Create README files in key folders."""

    # Drop Zone README
    readme = DROP_ZONE / "README.md"
    if not readme.exists():
        readme.write_text("""# DROP ZONE

Drop your project files here.

The AI will:
1. Analyze what you dropped
2. Ask clarifying questions
3. Organize your project
4. Start building

## What to drop

- Project briefs
- Design files
- Existing code
- Reference materials
""")

    # Send Off README
    readme = SEND_OFF / "README.md"
    if not readme.exists():
        readme.write_text("""# SEND OFF

Completed deliverables appear here.

When work is done, the AI places
final outputs here for you to collect.
""")


def setup_context():
    """Create initial context file."""
    context = CONTEXT_FILE

    if not context.exists():
        context.write_text(f"""# Project Context

**Created:** {datetime.now().strftime('%Y-%m-%d')}
**Phase:** Onboarding Complete

---

## Status

System initialized and ready.

## Next Steps

1. Drop project files in `00 User/00_Drop_Zone/`
2. Open in AI IDE
3. Tell AI: "Read constitution and help me"

## Constitution

Fetch from: https://github.com/edsworld27/omega-constitution
""")


def ask_ide():
    """Ask which IDE the user is using."""
    print("""
Which AI IDE are you using?

  1. Claude Code (Anthropic CLI)
  2. Cursor
  3. VS Code + Copilot
  4. Windsurf / Other
  5. Skip this step

""")

    choice = input("Enter 1-5: ").strip()

    if choice == "1":
        setup_claude_code()
    elif choice == "2":
        setup_cursor()
    elif choice == "3":
        setup_vscode()
    else:
        print("\nSkipping IDE setup. You can configure manually later.\n")


def setup_claude_code():
    """Setup for Claude Code."""
    print("""
╔═══════════════════════════════════════════════════════════╗
║                   CLAUDE CODE SETUP                       ║
╚═══════════════════════════════════════════════════════════╝

Claude Code will read CLAUDE.md files automatically.

Your setup is ready! Just run Claude Code in this folder.

TIP: Tell Claude:
  "Read the constitution from GitHub and follow INSTRUCTOR.xml"

""")

    # Create root CLAUDE.md if not exists
    claude_md = ROOT_DIR / "CLAUDE.md"
    if not claude_md.exists():
        claude_md.write_text("""# OMEGA SYSTEM - AI RULES

## First Actions
1. Read context: `Omega Control/00 Rules/03_Context/CONTEXT_DEV.md`
2. Fetch constitution: https://github.com/edsworld27/omega-constitution
3. Follow INSTRUCTOR.xml

## Constitution URL
https://raw.githubusercontent.com/edsworld27/omega-constitution/main/INSTRUCTOR.xml

## Store URL
https://raw.githubusercontent.com/edsworld27/omega-store/main/TREEMAP.md
""")
        print("✓ Created CLAUDE.md")


def setup_cursor():
    """Setup for Cursor."""
    print("""
╔═══════════════════════════════════════════════════════════╗
║                     CURSOR SETUP                          ║
╚═══════════════════════════════════════════════════════════╝

Creating .cursorrules file...
""")

    cursorrules = ROOT_DIR / ".cursorrules"
    cursorrules.write_text("""# OMEGA SYSTEM RULES

Read and follow the Omega Constitution:
https://github.com/edsworld27/omega-constitution

Key file: INSTRUCTOR.xml

Local context: Omega Control/00 Rules/03_Context/CONTEXT_DEV.md

Store (kits/skills): https://github.com/edsworld27/omega-store
""")
    print("✓ Created .cursorrules\n")


def setup_vscode():
    """Setup for VS Code."""
    print("""
╔═══════════════════════════════════════════════════════════╗
║                    VS CODE SETUP                          ║
╚═══════════════════════════════════════════════════════════╝

For VS Code + Copilot, create .github/copilot-instructions.md

""")

    github_dir = ROOT_DIR / ".github"
    github_dir.mkdir(exist_ok=True)

    instructions = github_dir / "copilot-instructions.md"
    instructions.write_text("""# Copilot Instructions

Follow the Omega Constitution:
https://github.com/edsworld27/omega-constitution

Read INSTRUCTOR.xml for rules.

Local context: Omega Control/00 Rules/03_Context/CONTEXT_DEV.md
""")
    print("✓ Created .github/copilot-instructions.md\n")


def main():
    print_banner()

    print("Setting up your Omega System...\n")

    # Ensure folders
    print("📁 Creating folders...")
    ensure_folders()
    print("   ✓ Folders ready\n")

    # Create READMEs
    print("📄 Creating README files...")
    create_readme_files()
    print("   ✓ READMEs created\n")

    # Setup context
    print("📝 Setting up context...")
    setup_context()
    print("   ✓ Context initialized\n")

    # Ask about IDE
    ask_ide()

    # Done
    print("""
╔═══════════════════════════════════════════════════════════╗
║                   ONBOARDING COMPLETE!                    ║
╚═══════════════════════════════════════════════════════════╝

Your Omega System is ready!

NEXT STEPS:
  1. Drop your project files in: 00 User/00_Drop_Zone/
  2. Open this folder in your AI IDE
  3. Tell the AI: "Read the constitution and help me"

The constitution will guide everything from here.

CONSTITUTION: https://github.com/edsworld27/omega-constitution
STORE:        https://github.com/edsworld27/omega-store
""")


if __name__ == "__main__":
    main()
