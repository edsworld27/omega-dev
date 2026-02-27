# OMEGA CONSTITUTION PACK — v9

**Build anything with AI, the right way.**

---

## Read This First

**[START HERE/START_HERE.md](START_HERE/START_HERE.md)** — The training manual. Has everything you need with diagrams.

That's the only doc you need to read as a human.

---

## Quick Start

**Just want to go?** Copy this into your AI:

```
You are the OMEGA CONSTRUCTOR.

Read CONSTITUTION/SECURITY.xml, FRAMEWORK.xml, INSTRUCTOR.xml.
Read USER SPACE/SESSION_CONTEXT.md.

Ask me what I want to build.
```

**Want to skip questions?** Use [START HERE/OMEGA_LITE.md](START HERE/OMEGA_LITE.md) or [CONSTITUTION/JUST_BUILD.md](CONSTITUTION/JUST_BUILD.md)

---

## The Master Daemon

Omega comes with self-healing background scripts (auto-updating project maps, security scanners, and changelogs).
To turn them on, run this command from the `Constution V10` folder:

```bash
python3 CONSTITUTION/python/omega_daemon.py
```

---

## What's What

```text
┌────────────────────────────────────────────────────────────┐
│                                                            │
│   FOR YOU (Human)              FOR AI (Agent)              │
│   ───────────────              ──────────────              │
│                                                            │
│   • START HERE/                • CONSTITUTION/*.xml        │
│     (training & run docs)        (rules, security, modes)  │
│                                                            │
│   • STORE/                     • STORE/                    │
│     (link to omega-store repo)                           │
│                                                            │
│   • USER SPACE/                                            │
│     (your project files)                                   │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

**You don't need to read XML.** That's the AI's rulebook.

---

## Modes

| Mode | Tokens | For |
|:-----|:-------|:----|
| Full Discovery | ~40k | AI guides you through everything |
| Quick Start | ~40k | You filled seeds, AI validates |
| Lite | ~8k | Small models, simple projects |
| Just Build | ~3k | Skip to code |

Details in [START HERE/START_HERE.md](START HERE/START_HERE.md)

---

*Built by Ed. Powered by the Omega Formula Stack.*
