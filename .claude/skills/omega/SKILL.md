---
name: omega
description: Initialize Omega Constitution - the universal AI operating system for any IDE
user-invocable: true
allowed-tools: Read, Glob, Bash, Write
---

# /omega — Omega Constitution Loader

This is the ONLY skill needed. Running `/omega` loads the entire Omega Constitution which contains ALL capabilities, skills, patterns, and rules.

## What This Does

1. Loads the Omega Constitution (The Brain)
2. Syncs to user's version
3. Activates ALL skills defined in the constitution
4. Works in ANY IDE (Claude Code, Cursor, Antigravity, VS Code, etc.)

## Execution

### Step 1: Detect Environment

Check if running in Omega DEV Panel or user project:

```bash
# Check for local constitution
ls -la "omega-constitution" 2>/dev/null || \
ls -la "00 Rules" 2>/dev/null || \
ls -la ".omega" 2>/dev/null
```

### Step 2: Load Constitution

**If Omega DEV Panel:**
```
Read: Omega System DEV MODE/omega-dev/06_Full_System/Dev Version (Edit)/omega-constitution DEV/Entire_Constitution_Files/omega-constitution-main/INSTRUCTOR.xml
```

**If User Project (has constitution):**
```
Read: ./omega-constitution/INSTRUCTOR.xml
# or
Read: ./00 Rules/INSTRUCTOR.xml
```

**If No Constitution (new user):**
```
Fetch from GitHub:
curl -s https://raw.githubusercontent.com/edsworld27/omega-constitution/main/INSTRUCTOR.xml
```

### Step 3: Load Context & Structure

```
Read: 03_Context/CONTEXT_DEV.md (if exists)
Read: TREEMAP.md (if exists)
Read: USER SPACE/dev-work/seed/ (if exists)
```

### Step 4: Confirm Initialization

Display:
```
═══════════════════════════════════════════════════════════
  OMEGA CONSTITUTION LOADED
═══════════════════════════════════════════════════════════

  You are now operating under Omega Constitution governance.

  All skills, protocols, and patterns are active.

  Core Protocols:
  - INSTRUCTOR.xml (Teaching)
  - SECURITY.xml (Protection)
  - PROMPTING.xml (Communication)
  - SOURCES.xml (Knowledge + Claude Cookbooks)

  Memory: 03_Context/CONTEXT_DEV.md
  Structure: TREEMAP.md

  Ready for instructions.
═══════════════════════════════════════════════════════════
```

## The Constitution IS the Skill System

When you load the constitution, you have access to:

| Capability | Source |
|------------|--------|
| Context Management | CONTEXT_PROTOCOL.xml |
| Quality Standards | QUALITY.xml |
| Security Rules | SECURITY.xml |
| Publishing Protocol | GITHUB_PUBLISHING.xml |
| Claude Patterns | SOURCES.xml → Claude Cookbooks |
| Fractal Memory | FRACTAL_PROTOCOL.xml |
| All Blueprints | blueprints/*.md |
| All Kits & Skills | omega-store |

**No separate skills needed. The constitution contains everything.**

## Arguments

$ARGUMENTS

- `/omega` — Full initialization
- `/omega context` — Quick context load
- `/omega publish` — Publishing protocol
- `/omega security` — Security rules
- `/omega [topic]` — Load specific protocol
