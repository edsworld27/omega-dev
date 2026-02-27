# CHANGES_DEV — Constitution Changelog

**Purpose:** Track all changes to the Omega Constitution framework.

---

## v9.5 — 2026-02-26

### Context Offloading & Daemon Automation
- Added `omega_reporter.py` script to run in background daemon
- Daemon aggressively scans `project/` for structural violations
- Violations are logged to a lightweight `USER SPACE/logging/` folder
- Drastically reduces XML token overhead for autonomous IDE agents
- `omega.py` wizard now automatically scaffolds `logging/`

### Constitution Bot Integration (v9.6)
- Created the new `ConstitutionAgent` in the Python Telegram backend (`mac-commander`).
- Agent controls a structured 4-step interview directly from the Telegram UI.
- Securely drops `FOUNDER_JOB-[ID].md` into `dev-work/hive/telegram_inbox/` for Claude Code to execute.
- Wired natural language triggers into `SimpleBrain` pattern matcher.

### Recursive Rule of 3 Hierarchy (v9.7)
- Replaced the "Rule of 5" with the **Rule of 3** across the entire framework.
- Hierarchy is now infinitely recursive: 3 Workers → 1 Manager → 3 Managers → 1 Mega-Manager → ...
- Updated `MASTER_ORCHESTRATOR.md` with recursive spawn and merge protocols.
- Updated `ConstitutionAgent` to instruct Claude Code to use Rule of 3 in FOUNDER_JOBs.

### Omega Bot MVP (v9.8)
- Stripped the bloated `mac-commander` (30+ files, 8 agents) into the lean `omega-bot/` (9 files, 2 agents).
- New architecture: **IntentAgent** (keyword classifier) → **Orchestrator** (router) → **ConstitutionAgent** + **ReporterAgent**.
- Zero LLM dependencies — runs free, no API costs.
- Added `omega_job_watcher.py` daemon to detect new `FOUNDER_JOB` files from Telegram.
- Daemon writes `PICKUP_ALERT.md` to `dev-work/` for Claude Code to detect on session start.
- Updated `INSTRUCTOR.xml` protocol: Step 1 is now "Check for PICKUP_ALERT.md".
- Updated `CONSTITUTION_BOT.md` ideation doc to point to `omega-bot/`.

### Omega Claw (Next — In Planning)
- Planning to rebrand `omega-bot/` → `omega-claw/` as the canonical agentic orchestration engine.
- Will add SQLite for job history tracking.
- Architecture finalized: LLM-free, file-based job drops, Constitution-governed.

### Omega Claw Standalone (v9.9)
- Created standalone `omega-claw` repo: **https://github.com/edsworld27/omega-claw**
- Full codebase: 20 files, 765 lines — OrchestratorAgent, ReporterAgent, IntentAgent, SQLite, Telegram.
- Added `skills/_template/` — plug-and-play skill system with auto-loadable `skill.json` + `handler.py`.
- Added `mcps/` — plug-and-play MCP config system for wiring external services.
- Updated Constitution README + SESSION_CONTEXT.md to reference omega-claw repo.
- Pushed to GitHub and live.

### Mode-Based Checkpoint Autonomy
- Updated `INSTRUCTOR.xml` Prime Directives
- Added explicit `<checkpoint_autonomy>` block
- Autonomous IDE extensions (Antigravity/Cursor) can now self-approve non-critical checkpoints when operating in `JUST BUILD` or `QUICK START` mode.
- Preserved strict human-gates for CP-5 (Dependencies) and CP-10 (Release).

### IDE Agent Routing
- Added explicit `<directory_enforcement>` to `INSTRUCTOR.xml`
- AI must now write production code exclusively into `USER SPACE/project/`
- Added `.cursorrules` to root, binding native IDE agents (Cursor/Antigravity) to the Constitution

### Constitution Bot Ideation
- Replaced `future-kits/` with `ideation/CONSTITUTION_BOT.md`
- Added vision for remote Telegram orchestration
- Moved bot backend secrets to `ideation/resource/` and added to `.gitignore`

---

## v9.4 — 2026-02-26

### Structured Onboarding Flow
- Created ONBOARDING.md with mandatory interview sequence
- Added CP-ONBOARD checkpoint (before CP-0)
- Rewrote RUN.md with single master prompt
- Enforces: Mode → Project Type → Existing Work → Purpose
- One question at a time, no deviation

### DEV Workspace
- Created DEV/ folder for meta-development
- CONTEXT_DEV.md — working memory
- CHANGES_DEV.md — this changelog
- IMPLEMENTATION_DEV.md — roadmap
- Using constitution to build constitution

### README as Navigation Hub
- Simplified to links only
- Points to all other docs

---

## v9.3 — 2026-02-26

### Path Structure Update
- Updated all `user-input/` references to `USER SPACE/dev-work/`
- Files updated:
  - FRAMEWORK.xml, PRACTICES.xml, INSTRUCTOR.xml
  - All ignition prompts (FRESH_BUILD, IMPORT, RESUME, etc.)
  - START_HERE.md, RUN.md
  - TECH_STACK.md seed template

---

## v9.2 — 2026-02-26

### Kit Creation Framework
- Created `omega-store/kits/_template/` skeleton
- Added KIT_EXPORT_GUIDE.md (320 lines)
- Updated KIT_CREATION_GUIDE.md with quick start
- Moved incomplete kits to DEV/future-kits/

### USER SPACE Restructure
- Split into `dev-work/` and `project/`
- dev-work/ = framework files
- project/ = clean deliverable
- Updated omega_compiler.py to use new paths

### Repository Split
- Created omega-store repo (https://github.com/edsworld27/omega-store)
- omega-constitution = framework only
- omega-store = kits, skills, mcps

---

## v9.1 — Earlier

### Initial v9 Setup
- Plug-and-play kit architecture
- Kit auto-discovery via kit.config.md
- Python daemon system (watchers)
- Constitution compliance test suite
- Training manual with ASCII diagrams

---

## Format

```
## vX.X — YYYY-MM-DD

### Category
- Change description
- Files affected
```

---

*This is our changelog for the constitution itself, not user projects.*
