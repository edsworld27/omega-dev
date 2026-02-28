# CHANGES — Omega Ecosystem

> Complete changelog from v9.0 to present. Covers **all repos**.
> Repos: [LINKS.md](../DEV/LINKS.md) | Structure: [TREEMAP.md](TREEMAP.md)

---

## 🏛️ Omega Constitution

### v16.0 — 2026-02-26
**BATTLE-READY: The Ghost Agent (Phantom Engine) + Dual-Vector Handoff**
- **Dual-Vector Orchestration**: Seamless failover between `TerminalAgent` (Claude CLI) and `PhantomAgent` (Antigravity GUI).
- **Physical GUI Control**: `PhantomAgent` uses `pyautogui` + `osascript` to physically type, click, and navigate the IDE.
- **Multi-Monitor Support**: Dynamic AppKit detection for dual-monitor setups (Left/Right screen targeting).
- **UI Mapping System**: `landmarks.json` stores pixel-perfect coordinates for 'Accept All', 'Model Selector', 'Stop Generation'.
- **Ultra-Optimized Watchdog**: 10-minute idle timer + 'Spinning Wheel' detection + auto-rescue for macOS freezes.
- **Task-Based Routing**: Auto-switches models (Planning -> Gemini, Building -> Claude Opus) for peak efficiency.
- **Standalone Repo**: Full system shipped to `edsworld27/omega-claw`.

### v9.9.7 — 2026-02-26
**Tree Map + comprehensive changelog**
- `TREEMAP.md` — full ecosystem structure map (all 3 repos, every file, data flow diagram)
- `.cursorrules` Step 0: "Read TREEMAP.md first" — AI agents orient before reading Constitution
- `CHANGELOG.md` rewritten from scratch (this file)

### v9.9.6 — 2026-02-26
**Scenarios folder + multi-repo awareness**
- Added `CONSTITUTION/scenarios/` — SOPs for common agent operations
- `git-push-all-repos.md` — agents push ALL ecosystem repos, not just one
- Hardened `.gitignore` per SECURITY.xml §1.1

### v9.9.5 — 2026-02-26
**Environment cleanup**
- Removed misplaced root `.env.example` — env files belong only in omega-claw

### v9.9.4 — 2026-02-26
**Environment system**
- `.env.example` with placeholder config for Constitution repo
- Hardened `.gitignore` in both repos

### v9.9.3 — 2026-02-26
**omega.py offers Omega Claw installation**
- `omega.py` wizard asks "Install Omega Claw?" after project setup
- If yes → clones repo → asks for Telegram token → creates `.env`
- If no → skips, zero friction. Detects if already installed.

### v9.9.2 — 2026-02-26
**Evaluation + cross-agent sync**
- McKinsey-grade evaluation (7.8/10 overall)
- `SESSION_CONTEXT.md` updated with ecosystem state + repo URLs
- `DEV/LINKS.md` — central reference for all repo URLs + versions

### v9.9.1 — 2026-02-26
**Omega Claw standalone repo**
- Created https://github.com/edsworld27/omega-claw
- Referenced in Constitution docs so agents can discover it

### v9.9 — 2026-02-26
**🦀 Omega Claw MVP (built here, then extracted to own repo)**
- Built the full Telegram → Hive orchestration engine (12 files)
- Cherry-picked auth + logging from old mac-commander
- See Omega Claw section below for full file listing

### v9.8.1 — 2026-02-26
**Session sync**
- Full changelog covering v9.6–v9.8 across all context files

### v9.8 — 2026-02-26
**End-to-end Telegram → Hive loop**
- `omega-bot` MVP: stripped 30+ file mac-commander → 9 lean files
- `omega_job_watcher.py` daemon: watches `telegram_inbox/` for FOUNDER_JOBs
- Writes `PICKUP_ALERT.md` when new jobs detected
- `INSTRUCTOR.xml` Step 1: "Check for PICKUP_ALERT.md on session start"
- Wired into `omega_daemon.py` as background task

### v9.7 — 2026-02-26
**Recursive Rule of 3 hierarchy**
- Replaced Rule of 5 with mathematically cleaner Rule of 3
- Infinite recursion: Founder → Mega-Manager → Manager → Worker
- For every 1-3 subordinates, spawn 1 manager tier
- Updated `MASTER_ORCHESTRATOR.md` with full scaling formula
- Updated `ConstitutionAgent` onboarding

### v9.6.1 — 2026-02-26
**Telegram Bot documentation**
- `DEV/ideation/CONSTITUTION_BOT.md` — full design doc

### v9.6 — 2026-02-26
**🤖 Constitution Telegram Bot backend**
- `ConstitutionAgent` — 4-step structured onboarding via Telegram
- Generates `FOUNDER_JOB-XXX.md` in `telegram_inbox/`
- Constitution-compliant with Kit, Mode, Rule of 3 instructions
- SQLite logging via `create_job()`

### v9.5.1 — 2026-02-25
**Management hierarchy**
- Rule of 5 management hierarchy (replaced by Rule of 3 in v9.7)

### v9.5 — 2026-02-25
**Infinite scale + mode autonomy**
- Infinite Agent Hive scaling
- Mode-based checkpoint autonomy
- Context offloading for AI context windows
- IDE routing rules
- Constitution Bot ideation begun

---

## 🦀 Omega Claw (https://github.com/edsworld27/omega-claw)

### v1.4 — 2026-02-26
**Environment configuration**
- `.env.example` with comprehensive placeholder config (Telegram, paths, future API keys, MCPs)
- `.gitignore` hardened per SECURITY.xml §1.1 (`.env`, `.pem`, `.key`, `.p12`, `.trusted_hashes.json`)

### v1.3 — 2026-02-26
**All 8 SECURITY.XML audit findings fixed**
- `agents/base_agent.py` — formal capability matrix: `AGENT_ROLE`, `PERMITTED_INPUTS`, `PERMITTED_OUTPUTS`, `FORBIDDEN_ACTIONS`, `MAX_BLAST_RADIUS` (§3.3)
- `agents/orchestrator_agent/__init__.py` — `fcntl.flock()` shared/exclusive locks on `active_conversations.json` (§3.7)
- `agents/orchestrator_agent/__init__.py` — `_escape_md()` escapes Markdown special chars in all user-supplied output (§2.2)
- `agents/reporter_agent/__init__.py` — capability matrix added (read-only, no write, no delete) (§3.3)
- `core/skill_loader.py` — forbidden import scanner blocks `subprocess`, `socket`, `http`, `urllib`, `requests`, `os.system` (§3.4)
- `core/skill_loader.py` — SHA-256 hash verification: trust-on-first-load, warns on handler modification (§3.4)
- `core/telegram_bot.py` — error handler returns generic "Something went wrong", full stack trace logs internally only (§0.8)
- `core/telegram_bot.py` — `BaseAgent.execute()` no longer leaks exception details (§0.8)

### v1.2 — 2026-02-26
**Critical security fixes (first 4 SECURITY.XML findings)**
- `core/telegram_bot.py` — deny-by-default auth: if `TELEGRAM_ALLOWED_USER_IDS` empty, rejects ALL users with `CRITICAL` log (§5.4)
- `core/telegram_bot.py` — generic error messages to Telegram, never leak `str(e)` (§0.8)
- `agents/orchestrator_agent/__init__.py` — input allowlist: `re.sub(r'[^a-zA-Z0-9 _-]', '', name)[:50]` on project names (§2.1)
- `db/database.py` — `os.chmod(DB_PATH, 0o600)` on new DB creation (owner read/write only) (§4.5)

### v1.1 — 2026-02-26
**Skills auto-loader — plug-and-play system**
- `core/skill_loader.py` — NEW: scans `skills/` directory on boot
- Reads `skill.json` config → validates required fields → dynamically imports `handler.py` using `importlib`
- `core/intent_agent.py` — added `register_patterns()` for dynamic keyword injection from skills
- `agents/__init__.py` — added `SkillAgent` wrapper class that turns loaded skill handlers into proper agents
- `agents/__init__.py` — `AgentRegistry._load_skills()` groups handlers by intent prefix and registers `SkillAgent` instances
- `core/orchestrator.py` — wired `SkillLoader` into `Orchestrator.__init__()` to inject skill patterns into IntentAgent on boot
- **Verified**: test `hello-skill` auto-loaded → `"hello"` classified as `hello:greet` → 3 agents registered (orchestrator, report, hello)

### v1.0 — 2026-02-26
**Initial release — full Omega Claw MVP**

**Entry point + config:**
- `main.py` — boots logging → initializes SQLite → starts Telegram polling
- `requirements.txt` — only 2 deps: `python-telegram-bot>=20.0`, `python-dotenv>=1.0.0`
- `.env.example` — config template with `TELEGRAM_BOT_TOKEN`, `TELEGRAM_ALLOWED_USER_IDS`, `OMEGA_HIVE_DIR`, `OMEGA_CLAW_DB`
- `README.md` — architecture diagram, setup instructions, agent documentation

**Agent layer:**
- `agents/base_agent.py` — abstract base class with intent registry pattern, `can_handle()`, `execute()`, `get_available_intents()`
- `agents/__init__.py` — `AgentRegistry` — loads orchestrator + reporter, routes intents by prefix
- `agents/orchestrator_agent/__init__.py` — 4-step onboarding wizard (name → audience → kit → mode), generates `FOUNDER_JOB-XXX.md` files in `telegram_inbox/`, logs to SQLite via `create_job()`, manages conversation state in `active_conversations.json`
- `agents/reporter_agent/__init__.py` — reads `master-job-board.md` from Hive + SQLite job history, formats Telegram-friendly status reports

**Core engine:**
- `core/telegram_bot.py` — Telegram interface: `TELEGRAM_ALLOWED_USER_IDS` whitelist auth, `/start` command, message handler that routes through Orchestrator, message splitting for 4096-char Telegram limit
- `core/orchestrator.py` — message router: receives text → IntentAgent classifies → AgentRegistry routes → agent executes → response returned, logs every command to SQLite
- `core/intent_agent.py` — keyword-based classifier (NO LLM, NO API costs): maps natural language to `agent:action` intents, 6 patterns across orchestrator (build/status/cancel) and reporter (hive/jobs/full)
- `core/logging_setup.py` — cherry-picked from old commander: `RedactingFilter` hides bot tokens and passkeys in log output using regex patterns

**Data layer:**
- `db/__init__.py` — package init
- `db/database.py` — SQLite at `~/.omega-claw/omega_claw.db`, two tables: `jobs` (id, name, kit, mode, status, timestamps, summary) and `command_log` (user_id, message, intent, response, timestamp), helper functions: `init_db()`, `log_command()`, `create_job()`, `update_job_status()`, `get_all_jobs()`, `get_recent_commands()`

**Plug-and-play scaffolds:**
- `skills/README.md` — how to create skills
- `skills/_template/skill.json` — template config: name, intents, handler reference
- `skills/_template/handler.py` — template with `execute()` function
- `mcps/README.md` — future MCP connection configs

---

## 🏪 Omega Store (https://github.com/edsworld27/omega-store)

### v1.0 — 2026-02-25
**Initial release**
- `kits/website/` — full website kit with preproduction, production, testing phases
- `kits/_template/` — kit creation template
- `skills/` — 5 agent skill definitions (orchestrator, analyst, classifier, guardian, writer)
- `mcps/MCP_CONFIG.md` — MCP connection configuration guide
- `examples/example-taskflow/` — reference implementation with seed files
- `ai-assistants/AI_ASSISTANTS.md` — AI assistant definitions
