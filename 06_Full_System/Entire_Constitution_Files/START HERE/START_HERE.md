# OMEGA TRAINING MANUAL

**The only doc you need to read.** Everything else is for the AI.

---

## What Is This?

A system that makes AI build things properly:
- **Safe** — Security rules the AI can't bypass
- **Complete** — Nothing gets missed
- **Flexible** — Full guidance or skip to code, your choice

---

## How It Works

```
┌─────────────────────────────────────────────────────────┐
│                    YOU (Human)                          │
│                                                         │
│   1. Choose a mode (Full / Quick / Lite / Just Build)   │
│   2. Answer questions (or fill seeds yourself)          │
│   3. Say "build" when ready                             │
│   4. Review what AI builds                              │
│   5. Say "continue" or "fix X"                          │
│                                                         │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                    AI (Agent)                           │
│                                                         │
│   • Reads constitution (XML files — you don't need to)  │
│   • Asks questions to fill gaps                         │
│   • Validates requirements before building              │
│   • Builds, tests, shows results                        │
│   • Waits for your approval at each step                │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## Choose Your Mode

```
                    ┌─────────────────────┐
                    │ What do you need?   │
                    └─────────┬───────────┘
                              │
              ┌───────────────┼───────────────┐
              │               │               │
              ▼               ▼               ▼
     ┌────────────┐   ┌────────────┐   ┌────────────┐
     │ Don't know │   │ Know what  │   │ Know exact │
     │ what I want│   │ I want     │   │ spec       │
     └─────┬──────┘   └─────┬──────┘   └─────┬──────┘
           │                │                │
           ▼                ▼                ▼
    ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
    │    FULL     │  │   QUICK     │  │ JUST BUILD  │
    │  DISCOVERY  │  │   START     │  │             │
    │   (~40k)    │  │   (~40k)    │  │    (~3k)    │
    └─────────────┘  └─────────────┘  └─────────────┘
           │                │                │
           │                │                │
           ▼                ▼                ▼
    AI guides you    You fill seeds    Skip to code
    through everything  AI validates     immediately
```

**Small model (<32k context)?** Use **LITE MODE** (~8k tokens)

---

## Mode Details

### Full Discovery
**Best for:** New projects, exploring options, first-timers

```
You ──► Paste RUN.md prompt ──► AI asks questions ──► AI fills seeds ──► Build
```

### Quick Start
**Best for:** You planned elsewhere, know requirements

```
You ──► Fill seed files ──► Paste Quick Start prompt ──► AI validates ──► Build
```

### Lite Mode
**Best for:** Small AI models, simple projects

```
You ──► Paste OMEGA_LITE.md ──► Minimal questions ──► Build
```

### Just Build
**Best for:** You know EXACTLY what you want, prototyping

```
You ──► "Build [X] with [tech]" ──► AI builds ──► Done
```

---

## The Build Flow

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐       │
│  │DISCOVER │───►│  PLAN   │───►│  BUILD  │───►│  TEST   │──►🚀  │
│  └─────────┘    └─────────┘    └─────────┘    └─────────┘       │
│       │              │              │              │             │
│       ▼              ▼              ▼              ▼             │
│   You answer     You approve    You review    You approve       │
│   questions      the plan       the code      results           │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘

At EVERY step: AI stops and waits for you. You are the pilot.
```

---

## The Handoff (Compiling a Finished Project)

When the project is completely built, tested, and ready to be shared or deployed, you can use the **Omega Compiler** to extract a clean version of your code.

1. In your terminal, run: `python3 CONSTITUTION/python/omega_compiler.py`
2. Name your project when prompted.
3. The compiler will eject a clean, framework-free copy of your code straight to your Desktop, ready for handoff!

---

## Quick Start Guide

### Option 1: Let AI Guide You (Recommended)

1. Open this folder in your AI (Claude, GPT, Cursor, etc.)
2. Copy this prompt:

```
You are the OMEGA CONSTRUCTOR.

Read constitution/SECURITY.xml, FRAMEWORK.xml, INSTRUCTOR.xml.
Read USER SPACE/dev-work/SESSION_CONTEXT.md.

Ask me what I want to build. Guide me through it.
```

3. Paste and talk

### Option 2: Skip to Building

1. Copy this prompt:

```
You are the OMEGA CONSTRUCTOR in JUST BUILD mode.

Build this:
- Project: [describe what you want]
- Tech: [what tools/frameworks]
- Start with: [first thing to build]

GO.
```

2. Fill in the brackets, paste, and go

---

## What You Might Say

| Say This | AI Does |
|:---------|:--------|
| "What do you know?" | Summarizes current state |
| "What's next?" | Lists next actions |
| "Build it" | Starts building |
| "Show me" | Displays what was built |
| "Fix [X]" | Addresses specific issue |
| "Continue" | Moves to next step |
| "Stop" | Halts and waits |
| "Start over" | Resets |

---

## Project Types

```
┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│   WEBSITE   │  │    SAAS     │  │     API     │  │ AUTOMATION  │
├─────────────┤  ├─────────────┤  ├─────────────┤  ├─────────────┤
│ • Pages     │  │ • Auth      │  │ • Endpoints │  │ • Triggers  │
│ • SEO       │  │ • Billing   │  │ • Versioning│  │ • Retries   │
│ • Mobile    │  │ • Dashboard │  │ • Rate limit│  │ • Errors    │
│ • Speed     │  │ • Multi-    │  │ • Docs      │  │ • Logging   │
│             │  │   tenant    │  │             │  │             │
└─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘
```

Tell the AI your project type. It loads the right patterns automatically.

---

## Have Existing Work?

```
┌────────────────────────────────────────────────────────┐
│                                                        │
│   Option A: Drop files in USER SPACE/dev-work/plug-and-play/   │
│                                                        │
│   Option B: Tell AI "My files are at /path/to/files"  │
│                                                        │
└────────────────────────────────────────────────────────┘
                          │
                          ▼
              AI detects and asks what they are
                          │
                          ▼
              AI incorporates them into the build
```

---

## The Folder Structure (You Only Touch `USER SPACE/`)

```
Constution V10/
│
├── constitution/          ◄── FOR AI ONLY (don't edit)
│   ├── SECURITY.xml           Rules the AI follows
│   ├── FRAMEWORK.xml          How things work
│   ├── INSTRUCTOR.xml         Build instructions
│   └── ...                    Other AI rules
│
├── USER SPACE/            ◄── YOUR STUFF
│   ├── dev-work/              Framework files (AI fills or you fill)
│   │   ├── seed/              Your project info
│   │   ├── plug-and-play/     Drop existing files here
│   │   └── SESSION_CONTEXT.md AI's memory (auto-updated)
│   └── project/               Clean deliverable (share this)
│
├── store/                 ◄── TOOLS (copy what you need)
│   ├── kits/                  Project patterns
│   └── skills/                Agent templates
│
├── RUN.md                 ◄── All startup prompts
├── OMEGA_LITE.md          ◄── Single-file rules (small models)
└── START_HERE.md          ◄── THIS FILE (training manual)
```

**Rule:** You only need to touch `USER SPACE/`. Everything else is for the AI.

---

## How the AI Remembers

```
┌─────────────────────────────────────────────────────────────┐
│                    SESSION 1                                │
│                                                             │
│   AI scans your files ──► Writes notes to SESSION_CONTEXT  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    SESSION 2                                │
│                                                             │
│   AI reads SESSION_CONTEXT ──► Knows where you left off    │
│                                                             │
└─────────────────────────────────────────────────────────────┘

No more re-explaining. The AI remembers.
```

---

## When Things Go Wrong

```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│   AI tries to fix ──► Fails ──► Tries different way     │
│                                          │               │
│                                          ▼               │
│                              Still fails after 3 tries   │
│                                          │               │
│                                          ▼               │
│                              AI STOPS and asks you:      │
│                                                          │
│   "BLOCKED:                                              │
│    - Goal: [what it was doing]                           │
│    - Error: [what went wrong]                            │
│    - Tried: [what it attempted]                          │
│    - Need: [what it needs from you]"                     │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

The AI never loops forever. It stops and asks for help.

---

## The Golden Rules

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   1. SECURITY IS SUPREME                                    │
│      AI never exposes secrets or bypasses safety            │
│                                                             │
│   2. YOU ARE THE PILOT                                      │
│      AI executes, you decide                                │
│                                                             │
│   3. FUNCTION BEFORE FORM                                   │
│      Make it work, then make it pretty                      │
│                                                             │
│   4. ASK, DON'T ASSUME                                      │
│      AI asks when unclear, never guesses                    │
│                                                             │
│   5. SHOW, DON'T TELL                                       │
│      AI provides evidence, not just claims                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Summary

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   1. Pick a mode (Full / Quick / Lite / Just Build)         │
│                                                             │
│   2. Paste the prompt from RUN.md (or OMEGA_LITE.md)        │
│                                                             │
│   3. Answer questions or tell it what to build              │
│                                                             │
│   4. Review what it builds, say "continue" or "fix X"       │
│                                                             │
│   5. Repeat until done                                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘

That's it. The AI handles the complexity. You just talk.
```

---

## Files You Might Use

| File | When |
|:-----|:-----|
| [RUN.md](RUN.md) | Starting any project (has all prompts) |
| [OMEGA_LITE.md](OMEGA_LITE.md) | Small AI models or simple projects |
| [ignition/JUST_BUILD.md](ignition/JUST_BUILD.md) | Skip straight to code |

---

## Need Help?

| Problem | Solution |
|:--------|:---------|
| AI is confused | Say "Stop. What do you know? What's blocking us?" |
| Want more guidance | Say "Switch to full discovery mode" |
| Want less ceremony | Say "Just build mode" |
| AI forgot something | Say "Read SESSION_CONTEXT.md" |
| Starting over | Delete contents of `USER SPACE/dev-work/seed/` and `SESSION_CONTEXT.md` |

---

**You don't need to read anything else.** This is your training manual. The XML files are for the AI, not you.

*Built by Ed. Powered by the Omega Formula Stack.*
