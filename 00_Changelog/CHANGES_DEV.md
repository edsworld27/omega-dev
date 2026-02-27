# CHANGES_DEV — Constitution Changelog

**Purpose:** Track all changes to the Omega Constitution framework.

---

## v15.0 — 2026-02-27 (The "God-Mode" Architecture)

### 5-Repo Ecosystem Decoupling
- Completely decentralized the monolithic system into 5 distinct, highly-scalable repositories.
  1. `omega-constitution`: The raw XML rules data lake (Public)
  2. `omega-store`: The certified starter kits and templates (Public)
  3. `omega-claw`: The Python automation and orchestration suite (Public)
  4. `Omega-System`: The ultra-lightweight execution shell (Public)
  5. `omega-dev`: The private "FULL SYSTEM" sandbox (Private)
- Eradicated all submodules to prevent recursive Git lock issues.

### Zero-Install GitHub MCP
- Wrote the official `claude_desktop_config.json` documentation for `server-github`.
- Authorized the "God Prompt" method where Claude independently fetches `omega-index.md` from the cloud and builds applications without a local clone of the rules.

### The Omega Dev "Full System" Sandbox
- Master-nested all 4 public repositories inside the private `omega-dev/FULL SYSTEM/` directory.
- Achieved total visibility for the Architect: AI can now read `SECURITY.xml`, edit `omega-store` templates, and generate execution shell scripts in a single context window context.

---

## v14.0 — 2026-02-27 (The Omega Claw)

### Autonomous Safety Daemons
- Created `omega-claw/scripts/watchdog.py` with hard `MAX_RETRIES=3` infinite loop prevention.
- Added heuristic failover mechanisms for when AI compilation hallucinates.
- Created `omega-claw/ai/dev-mode/compressor.py` as an automatic context harvester.
- Wired a Git Post-Commit hook (`post-commit-compressor.sh`) to automatically compile a repository snapshot after every code push.

### Dynamic Replanning
- Updated `tasks.json` schema to include `meta: { dynamic_planning: true }`.
- Added strict cryptographic/string-match verification for reading `SECURITY.xml` before code generation begins.

---

## v13.0 — 2026-02-27 (The Execution Shell)

### The Lightweight Download
- Audited the `Omega-System` repository (formerly `Constution V10`).
- Deleted all internal Constitution logic, templates, and Python tools from the public download.
- Created the master `omega-index.md` manifest directly linking to external Repositories.
- Added "Day 1 Kit Upsell" logic directly into the shell's setup rules.

---

## v10.0 — 2026-02-26 (The Final Restructure)

### Environment Lockdown
- Injected `.cursorrules` into the root directory forcing adherence to the Constitution constraints.
- Removed legacy onboarding folders (`START HERE`, `STORE`, `Omega Claw v1`) from the execution tracking scope.
- Enforced hard IDE behavioral guidelines for AI-driven dev-mode execution.

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
