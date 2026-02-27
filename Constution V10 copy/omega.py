#!/usr/bin/env python3
"""
OMEGA SETUP — Interactive Project Setup

Run this to set up your project with a few questions.
Then copy the generated prompt into your AI.
"""

import os
import sys

# Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
USER_SPACE = os.path.join(SCRIPT_DIR, "USER SPACE")
DEV_WORK = os.path.join(USER_SPACE, "dev-work")
PROJECT = os.path.join(USER_SPACE, "project")
SEED_DIR = os.path.join(DEV_WORK, "seed")
LOGGING_DIR = os.path.join(USER_SPACE, "logging")
PLUG_AND_PLAY = os.path.join(DEV_WORK, "plug-and-play")
OMEGA_CLAW_DIR = os.path.join(SCRIPT_DIR, "omega-claw")
OMEGA_CLAW_REPO = "https://github.com/edsworld27/omega-claw.git"


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_banner():
    print("""
╔═══════════════════════════════════════════════════════════╗
║                    OMEGA CONSTITUTION                      ║
║              Build anything with AI, the right way         ║
╚═══════════════════════════════════════════════════════════╝
""")


def ask(question, options=None):
    """Ask a question, optionally with numbered options."""
    print(f"\n{question}")
    if options:
        for i, opt in enumerate(options, 1):
            print(f"  {i}. {opt}")
        while True:
            try:
                choice = input("\n→ ").strip()
                if choice.isdigit() and 1 <= int(choice) <= len(options):
                    return int(choice)
                print("Please enter a valid number.")
            except KeyboardInterrupt:
                print("\n\nCancelled.")
                sys.exit(0)
    else:
        return input("\n→ ").strip()


def setup_folders():
    """Create the basic folder structure."""
    folders = [
        os.path.join(PROJECT, "src"),
        os.path.join(PROJECT, "tests"),
        os.path.join(PROJECT, "public"),
        LOGGING_DIR,
        os.path.join(PLUG_AND_PLAY, "frontend"),
        os.path.join(PLUG_AND_PLAY, "backend"),
        os.path.join(PLUG_AND_PLAY, "existing"),
        os.path.join(PLUG_AND_PLAY, "designs"),
    ]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)


def write_project_seed(name, audience, purpose, project_type):
    """Write the PROJECT.md seed file."""
    content = f"""# PROJECT — {name}

## Overview
**Project Name:** {name}
**Project Type:** {project_type}
**Target Audience:** {audience}

## Purpose
{purpose}

## North Star
[AI will help define this based on your purpose]

## MVP Features
[AI will help identify these]

## Non-Goals
[AI will help identify these]

## Constraints
[Add any constraints: budget, timeline, technical limits]
"""
    os.makedirs(SEED_DIR, exist_ok=True)
    with open(os.path.join(SEED_DIR, "PROJECT.md"), 'w') as f:
        f.write(content)


def write_session_context(name, project_type, mode):
    """Write initial SESSION_CONTEXT.md."""
    content = f"""# SESSION CONTEXT

## Project
- **Name:** {name}
- **Type:** {project_type}
- **Mode:** {mode}

## Current State
- Phase: Pre-Production
- Checkpoint: CP-ONBOARD (Complete)
- Status: Ready for discovery

## Notes
- Project initialized via omega.py
- Seeds partially filled
- Ready for AI to continue discovery

## Next Action
- AI should read constitution and continue from CP-0
"""
    with open(os.path.join(DEV_WORK, "SESSION_CONTEXT.md"), 'w') as f:
        f.write(content)


def generate_prompt(name, project_type, mode, has_existing):
    """Generate the ready-to-paste prompt."""

    existing_note = ""
    if has_existing == 2:  # Frontend
        existing_note = "I have existing frontend code in plug-and-play/frontend/."
    elif has_existing == 3:  # Backend
        existing_note = "I have existing backend code in plug-and-play/backend/."
    elif has_existing == 4:  # Both
        existing_note = "I have an existing project in plug-and-play/existing/."
    elif has_existing == 5:  # Designs
        existing_note = "I have designs in plug-and-play/designs/."

    mode_map = {
        1: "FULL DISCOVERY",
        2: "QUICK START",
        3: "LITE",
        4: "JUST BUILD"
    }

    type_map = {
        1: "Website",
        2: "Web App (SaaS)",
        3: "API",
        4: "Automation",
        5: "Other"
    }

    prompt = f"""You are the OMEGA CONSTRUCTOR.

Read constitution/SECURITY.xml, FRAMEWORK.xml, INSTRUCTOR.xml, ONBOARDING.md.
Read USER SPACE/dev-work/SESSION_CONTEXT.md.

CONTEXT (from setup):
- Project: {name}
- Type: {type_map.get(project_type, 'Other')}
- Mode: {mode_map.get(mode, 'FULL DISCOVERY')}
{f'- {existing_note}' if existing_note else '- Starting fresh'}

Onboarding is complete. Continue from CP-0 (Seed Scan).
Activate the appropriate kit and proceed with discovery.
"""
    return prompt


def copy_to_clipboard(text):
    """Try to copy text to clipboard."""
    try:
        import subprocess
        if sys.platform == 'darwin':  # macOS
            subprocess.run(['pbcopy'], input=text.encode(), check=True)
            return True
        elif sys.platform == 'linux':
            subprocess.run(['xclip', '-selection', 'clipboard'], input=text.encode(), check=True)
            return True
    except:
        pass
    return False


def install_omega_claw():
    """Clone and set up Omega Claw for remote Telegram control."""
    import subprocess
    
    if os.path.exists(OMEGA_CLAW_DIR):
        print("\n🦀 Omega Claw is already installed!")
        print(f"   Location: {OMEGA_CLAW_DIR}")
        return True
    
    print("\n🦀 Installing Omega Claw...")
    print(f"   Cloning from: {OMEGA_CLAW_REPO}")
    
    try:
        subprocess.run(["git", "clone", OMEGA_CLAW_REPO, OMEGA_CLAW_DIR], check=True)
    except Exception as e:
        print(f"\n❌ Failed to clone: {e}")
        print(f"   You can manually clone: git clone {OMEGA_CLAW_REPO}")
        return False
    
    print("\n✅ Omega Claw installed!")
    
    # Ask for Telegram token
    print("\n🔑 To go live, you need a Telegram Bot Token.")
    print("   Get one free from @BotFather on Telegram (takes 60 seconds).")
    token = ask("Paste your Telegram Bot Token (or press Enter to skip):")
    
    if token and token.strip():
        env_path = os.path.join(OMEGA_CLAW_DIR, ".env")
        with open(env_path, 'w') as f:
            f.write(f"TELEGRAM_BOT_TOKEN={token.strip()}\n")
            f.write(f"OMEGA_HIVE_DIR={os.path.join(DEV_WORK, 'hive')}\n")
        print("\n✅ Token saved to .env")
        print("\n🚀 To start Omega Claw:")
        print(f"   cd {OMEGA_CLAW_DIR}")
        print("   pip install -r requirements.txt")
        print("   python main.py")
    else:
        print("\n⏭️  Skipped. Add your token later in omega-claw/.env")
    
    return True


def main():
    clear()
    print_banner()

    print("Let's set up your project.\n")

    # Intent
    intent = ask("What do you need?", [
        "Build something",
        "Learn how this works first",
        "Get help with a question"
    ])

    if intent == 2:
        print("\n📚 LEARN MODE")
        print("\nThe Omega Constitution is a framework that makes AI build things properly.")
        print("\nKey concepts:")
        print("  • Constitution — XML rules the AI follows")
        print("  • Seeds — Your project requirements (AI fills them via questions)")
        print("  • Kits — Project templates (website, saas, api, automation)")
        print("  • USER SPACE — Where your files go")
        print("  • project/ — Clean deliverable folder")
        print("\nRead START HERE/START_HERE.md for the full training manual.")
        print("\nRun this script again when you're ready to build!")
        return

    if intent == 3:
        print("\n❓ HELP MODE")
        print("\nCommon questions:")
        print("  • 'Where do I put files?' → USER SPACE/dev-work/plug-and-play/")
        print("  • 'How do I start?' → Run this script or paste GO.md prompt")
        print("  • 'What's a kit?' → Project template with patterns for your type")
        print("  • 'Where's my code?' → USER SPACE/project/")
        print("\nFor more help, read START HERE/START_HERE.md")
        return

    # Mode
    mode = ask("How would you like to work?", [
        "Full Discovery — Guide me through everything",
        "Quick Start — I know what I want, validate and build",
        "Lite — Minimal questions, simple build",
        "Just Build — Skip to code"
    ])

    # Project Type
    project_type = ask("What are you building?", [
        "Website — Marketing site, landing page, portfolio",
        "Web App — SaaS, dashboard, user accounts",
        "API — Backend service, REST/GraphQL",
        "Automation — Workflows, integrations, scripts",
        "Other — Tell the AI what"
    ])

    # Existing Work
    has_existing = ask("Do you have existing work?", [
        "Starting fresh — Nothing built yet",
        "Have frontend — UI exists, need backend",
        "Have backend — API exists, need frontend",
        "Have both — Existing project, need help",
        "Have designs — Wireframes/mockups, no code"
    ])

    # Project Details
    print("\n" + "─" * 50)
    name = ask("What's your project called? (working name is fine)")
    audience = ask("Who is this for? (e.g., 'small business owners')")
    purpose = ask("In 1-2 sentences, what's the core purpose?")

    # Setup
    print("\n⚙️  Setting up your project...")
    setup_folders()

    # Optional: Omega Claw
    claw = ask("Want to install Omega Claw for remote Telegram control?", [
        "Yes — Install Omega Claw",
        "No — Skip for now"
    ])
    if claw == 1:
        install_omega_claw()

    type_names = {1: "Website", 2: "Web App", 3: "API", 4: "Automation", 5: "Other"}
    mode_names = {1: "Full Discovery", 2: "Quick Start", 3: "Lite", 4: "Just Build"}

    write_project_seed(name, audience, purpose, type_names.get(project_type, "Other"))
    write_session_context(name, type_names.get(project_type, "Other"), mode_names.get(mode, "Full Discovery"))

    # Generate prompt
    prompt = generate_prompt(name, project_type, mode, has_existing)

    # Output
    clear()
    print_banner()

    print("✅ PROJECT SETUP COMPLETE\n")
    print(f"  Project: {name}")
    print(f"  Type: {type_names.get(project_type, 'Other')}")
    print(f"  Mode: {mode_names.get(mode, 'Full Discovery')}")

    if has_existing > 1:
        locations = {
            2: "plug-and-play/frontend/",
            3: "plug-and-play/backend/",
            4: "plug-and-play/existing/",
            5: "plug-and-play/designs/"
        }
        print(f"\n📁 Put your existing files in:")
        print(f"   USER SPACE/dev-work/{locations.get(has_existing, 'plug-and-play/')}")

    print("\n" + "═" * 55)
    print("COPY THIS PROMPT INTO YOUR AI:")
    print("═" * 55)
    print(prompt)
    print("═" * 55)

    # Try to copy to clipboard
    if copy_to_clipboard(prompt):
        print("\n📋 Prompt copied to clipboard!")
    else:
        print("\n📋 Copy the prompt above and paste into your AI.")

    print("\n🚀 You're ready to go!")


if __name__ == "__main__":
    main()
