# OMEGA SYSTEM - MASTER INDEX

> **The AI-Powered Project Orchestrator**

---

## Quick Start

```bash
python RUN.py              # Start the system
python RUN.py --onboard    # First-time setup
```

---

## Structure

```
omega-system/
├── RUN.py                    # Entry point
├── 00 User/
│   ├── 00_Drop_Zone/         # Drop your files here
│   └── 01_Send_Off/          # Finished work appears here
├── Omega Control/
│   └── 00 Rules/             # Control panel + Python scripts
│       ├── python/           # Automation scripts
│       └── 03_Context/       # Session tracking
├── Projects/
│   └── (your projects here)
└── MASTER_INDEX.md           # This file
```

---

## For Users

1. Clone this repo
2. Run `python RUN.py --onboard`
3. Drop your project files in `00 User/00_Drop_Zone/`
4. Open in your AI IDE and say: "Read the constitution and help me"

---

## The Quad Ecosystem (GitHub)

| Repo | Codename | Purpose |
|------|----------|---------|
| [omega-constitution](https://github.com/edsworld27/omega-constitution) | Brain | Protocols, Rules, Standards |
| [omega-store](https://github.com/edsworld27/omega-store) | Marketplace | Kits, Skills, Templates |
| [omega-claw](https://github.com/edsworld27/omega-claw) | Dispatch | Orchestration, Agents |
| [Omega-System](https://github.com/edsworld27/Omega-System) | Shell | This orchestrator |

---

## For AI

1. Fetch constitution: `https://github.com/edsworld27/omega-constitution`
2. Read `INSTRUCTOR.xml` for rules
3. Check local context: `Omega Control/00 Rules/03_Context/CONTEXT_DEV.md`
4. Follow the constitution's guidance
